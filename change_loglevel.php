<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Change Log Level</title>
        <meta charset="utf-8">
    </head>
    <body>
    <?php
        $startTime = microtime();
        function recursiveDirScan($dir, $logFileName){
            if(substr($dir, -1) != '/'){
                $dir .= '/';
            }
            foreach(scandir($dir) as $itemID => $item){
                if(is_file($dir.$item) && $item == $logFileName){
                    return $dir.$item;
                }

                if(is_dir($dir.$item) && $item != '.' && $item != '..'){
                    return recursiveDirScan($dir.$item.'/', $logFileName);
                }
            }
        }
        function backupLogFile($path, $backupDir, $backupLogName){
            $logContent = file_get_contents($path);
            $backupLog = fopen($backupDir.$backupLogName, 'w');
            if(fwrite($backupLog, $logContent) === FALSE){
                echo "Cannot write to file: " . $backupDir . $backupLogName;
                exit;
            }
            fclose($backupLog);

            echo "Created backup log: " . $backupDir . $backupLogName . "<br>";
        }

        function changeLogLevel($log){
            $logContent = file_get_contents($log);
            if($logContent){
                $changedLog = str_replace('TRACE', 'ERROR', $logContent);
                if(file_put_contents($log, $changedLog)){
                    return true;
                }
            }

            return false;
        }

        $logbackDir = ''; // main directory
        $logFileName = ''; // log file name
        $backupDir = ''; // backup directory
        $levelFrom = ''; // log level to replace
        $levelTo = '';   // new log level

        foreach(scandir($logbackDir) as $itemID => $item){
            if(is_file($logbackDir.$item) && $item != $logFileName){
                continue;
            }

            if($item == '.' || $item == '..'){
                continue;
            }

            $backupLogName = $logFileName . '-' . $item;

            if(is_dir($logbackDir.$item)){
                $logPath = recursiveDirScan($logbackDir.$item, $logFileName);
                if(!$logPath || $logPath == ''){
                    continue;
                }

                echo "Working on file: " . $logPath . "<br>";

                backupLogFile($logPath, $backupDir, $backupLogName);
                if(changeLogLevel($logPath, $levelFrom, $levelTo)){
                    echo "Log level changed successfully on: " . $logPath . "<br>";
                }else{
                    echo "Could not change log level on: " . $logPath . "<br>";
                }
            }

            echo "<hr>";
        }

        $totalTime = microtime() - $startTime;
        echo 'Execution Time: ' . $totalTime . ' seconds';
    ?>
    </body>
</html>
