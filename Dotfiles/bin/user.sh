#! /bin/bash

e="%{F#FF006C}$(whoami)"

if [ $e ];then
	echo ${e^^}
fi
