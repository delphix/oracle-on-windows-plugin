#
# Copyright (c) 2020 by Delphix. All rights reserved.
#
# Author: Jatinder Luthra
# Date: 09-23-2020
###########################################################

$programName = 'vdb_childProvision.ps1'
$delphixToolkitPath = $env:DLPX_TOOLKIT_PATH
$oraInstName = $env:ORACLE_INST
$oraUser = $env:ORACLE_USER
$oraPwd = $env:ORACLE_PASSWD
$oraUnq = $env:ORA_UNQ_NAME
$oraDBName = $env:ORA_DB_NAME
$oraBase = $env:ORACLE_BASE
$oracleHome = $env:ORACLE_HOME
$virtMnt = $env:VDB_MNT_PATH
$oraVDBSrc = $env:ORA_VDB_SRC

$scriptDir = "${delphixToolkitPath}\scripts"

. $scriptDir\delphixLibrary.ps1
. $scriptDir\oracleLibrary.ps1

log "Executing $programName"

$Env:ORACLE_BASE=$oraBase
$Env:ORACLE_SID=$oraUnq
$Env:ORACLE_HOME=$oracleHome

log "ORACLE_BASE: $oraBase"
log "ORACLE_HOME: $oracleHome"
log "ORACLE_SID: $oraUnq"
log "PARENT_VDB: $oraVDBSrc"

$initfile = "${virtMnt}\${oraUnq}\init${oraUnq}.ora"
$masterinit = ${initfile}+".master"

log "Provision Child VDB, $oraUnq STARTED"

$PSDefaultParameterValues['*:Encoding'] = 'ascii'

## copy master init to database

log "Copy master file ${masterinit} to $oracleHome\database\init${oraUnq}.ora"

if ((Test-Path "$oracleHome\database\init${oraUnq}.ora")) {
	mv "$oracleHome\database\init${oraUnq}.ora" "$oracleHome\database\init${oraUnq}.ora.bak" -force
	cp ${masterinit} "$oracleHome\database\init${oraUnq}.ora"
}
else {
	cp ${masterinit} "$oracleHome\database\init${oraUnq}.ora"
}

######### Create new ccf.sql file ######

log "Moving ccf.sql file to ccf.sql.old STARTED"

$ccf_file_old = "$virtMnt\$oraUnq\ccf_old.sql"
$ccf_file_new = "$virtMnt\$oraUnq\CCF.SQL"

mv $ccf_file_new $ccf_file_old -force

log "Moving ccf.sql file to ccf.sql.old FINISHED"

log "Create Script for new control file, $ccf_file_new STARTED"

extract_string "STARTUP NOMOUNT" ";" $ccf_file_old > $ccf_file_new

(Get-Content -path $ccf_file_new -Raw) -replace 'REUSE DATABASE','REUSE SET DATABASE' | Set-Content -Path $ccf_file_new
(Get-Content -path $ccf_file_new -Raw) -replace 'NORESETLOGS','RESETLOGS' | Set-Content -Path $ccf_file_new
(Get-Content -path $ccf_file_new -Raw) -replace $oraVDBSrc, $oraUnq | Set-Content -Path $ccf_file_new
(Get-Content -path $ccf_file_new -Raw) -replace '-- STANDBY LOGFILE','' | Set-Content -Path $ccf_file_new
echo ";" >> $ccf_file_new

remove_empty_lines $ccf_file_new

log "Create Script for new control file, $ccf_file_new FINISHED"

########### startup nomount #############

startup_nomount

###########  create control file ############

execute_ctrl_file $ccf_file_new

######### get database sate ##########

get_db_status

########## Perform Media recovery ##########

$logFiles = "$delphixToolkitPath\logs\$oraUnq\logFileslist.txt"

log "Extract Log Files for Child VDB, $logFiles STARTED"

 $sqlQuery=@"
 WHENEVER SQLERROR EXIT SQL.SQLCODE
 set serveroutput off
 set feedback off
 set heading off
 set echo off
 select member from v`$logfile order by group# ;
 exit
"@

log "[SQL Query - get_childVDB_LogFiles] $sqlQuery"

$result = $sqlQuery |  . $Env:ORACLE_HOME\bin\sqlplus.exe -silent " /as sysdba"

log "[SQL - get_childVDB_LogFiles] $result"

echo $result > $logFiles

remove_empty_lines $logFiles

log "Extract Log Files for Child VDB, $logFiles FINISHED"

### apply each log for media recovery

$applyRedoLog = "$delphixToolkitPath\logs\$oraUnq\applyredo.log"

log "Perform Media Recovery for Child VDB, $oraUnq STARTED"

ForEach ($log in (Get-Content $logFiles))
{
echo "#########################" >> $applyRedoLog
echo $log >> $applyRedoLog
$sqlQuery=@"
RECOVER DATABASE USING BACKUP CONTROLFILE
$log
"@

log "[SQL Query - Media Recovery]: $sqlQuery"

$sqlQuery |  . $Env:ORACLE_HOME\bin\sqlplus.exe " /as sysdba" >> $applyRedoLog
}

$logContent = Get-Content $applyRedoLog

if ($logContent -like "*Media recovery complete*"){
log "Media Recovery Completed"
}
else {
log "Media Recovery Failed. Check logFile, $applyRedoLog"
exit 1
}

log "Perform Media Recovery for Child VDB, $oraUnq FINISHED"
log "Media Recovery LogFile, $applyRedoLog"

##### open db with reset logs ########

db_open_resetlogs

######### control file create #####

log "Moving ccf.sql file to ccf.sql.orig STARTED"

mv "$virtMnt\$oraUnq\ccf.sql" "$virtMnt\$oraUnq\ccf_orig.sql" -force

log "Moving ccf.sql file to ccf.sql.original FINISHED"

create_control_file $virtMnt $oraUnq

####### get database state ##########

get_db_status

log "Provision Child VDB, $oraUnq FINISHED"
