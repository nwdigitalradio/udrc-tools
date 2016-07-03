#!/bin/bash

#Author: John D. Hays, K7VE
#License: Public Domain
#No Warranty for any purpose

if [ -z "$1" ] || [ -z "$2" ]; then
	echo usage: $0 interface start\|stop
	exit
fi
	
# Argument '$1' is the interface to the Internet, e.g. eth0 or wlan0
IPADDR=`ifconfig $1 | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | sed 's/inet addr://'`

#Remote Control is specific to ircDDBGateway and should be set to match the
#one used in the gateway configuration
RemoteControl=""

# Ports to be redirected
DExtraPorts="30001"
DCSPorts=`seq 30051 30059`
DPlusPorts=`seq 20001 20009`
CCSPorts=`seq 30061 30065`
CSRouting="40000"
IPRouting="40001"

#Remove any collection of ports which are not used in your gateway
UDPPorts="$DPlusPorts $DExtraPorts $DCSPorts $CCSPorts $CSRouting $RemoteControl"

for j in $UDPPorts; do
        PORTS="$PORTS $j UDP"
done

#If you are running D-STAR DATA Uncomment
#PORTS="$PORTS $IPRouting TCP"

if [ "$2" = "start" ]; then
	upnpc -r $PORTS
else
        upnpc -d $PORTS
fi
echo done
