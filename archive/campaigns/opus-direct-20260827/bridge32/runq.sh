#!/bin/zsh
cd "$(dirname "$0")"
while pgrep -f "t19_big.py" > /dev/null; do sleep 10; done
python3 t23_struct.py 64 0.06 1 imp short > t23_L64.log 2>&1
python3 t14_scan.py 64 2.7,4,6,8 1 conf,TT > t14_L64.log 2>&1
echo DONE >> t23_L64.log
