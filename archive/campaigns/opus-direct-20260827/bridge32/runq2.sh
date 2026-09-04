#!/bin/zsh
cd "$(dirname "$0")"
while pgrep -f "t23_struct.py" > /dev/null; do sleep 15; done
python3 t32_dK.py 64 4,6,8,10,12,16,20,25,32,40 TT,conf,V0a > t32_L64.log 2>&1
python3 t14_scan.py 64 2.7,4,6,8 1 conf,TT > t14_L64.log 2>&1
echo ALLDONE >> t32_L64.log
