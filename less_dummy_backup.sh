#!/bin/bash
OF=../my-backup-$(date +%Y%m%d).tar.gz
tar czf $OF /home/nicolo/Scrivania/base_script 
