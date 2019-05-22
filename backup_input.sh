#!/bin/bash
if [ -z "$1" ]; then
	echo usage $0 directory
	exit
fi
SRCD=$1
TGTD="/home/nicolo/Scrivania/"
OF=backup-$(date +%Y%m%d).tar.gz
tar cvzf $TGTD$OF $SRCD
