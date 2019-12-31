#!/bin/sh

clear

chmod +x ~

echo 'Cleaning old processes...'
str=`ps -Af | grep relation.py | grep -v "grep"`
arr=($(echo $str))
pid=${arr[1]}
kill -9 $pid

echo 'Done!'
echo 'Starting ...'
/usr/local/bin/python relation.py &
echo 'Done!'
