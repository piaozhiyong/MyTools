@echo off
:start
net use \\192.168.3.199 "123456" /user:"wudr"
net time \\192.168.3.199 /set /y
net use * /del /y
::ÿ������ִ��һ��start
ping localhost -n 300 > nul

goto start
pause