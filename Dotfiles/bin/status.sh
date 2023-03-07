#! /bin/bash

st=$(nmcli | grep " conectado " | sed '1q;d' | awk '{print $2}' )

if [ $st ]; then
	ip="%{F#D1FFFF}>> $(ifconfig wlp0s20f3 | grep "inet " | awk '{print $2}')"
	echo ${ip}
else

	echo "%{F#FF0000}Desconectado" | tr [:lower:] [:upper:]
fi
