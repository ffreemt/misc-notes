%echo off
REM run-push comment1 comment 2
IF "%1"=="" GOTO HAVE_0

REM IF "%2"=="" GOTO HAVE_1
REM IF "%3"=="" GOTO HAVE_2
setlocal
    git pull
    set comment=%*
    echo comment: %comment%
    REM git commit -am "%comment%" && git push
    git add . && git commit -am "%comment%" && git push
    GOTO END
:HAVE_0
    echo.
    echo Provide at least one word as comment
    git add . && git commit -am "update" && git push
:END
