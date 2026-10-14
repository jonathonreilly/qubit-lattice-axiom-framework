#!/bin/bash
cd "$(dirname "$0")"
export OMP_NUM_THREADS=2
while pgrep -f "f4_run.py A120" > /dev/null; do sleep 2; done
python3 f4_run.py C0p 4 0.25 6 0.003 2 0 1,2,4 fb > ../f4_C0p.out 2>&1
python3 f4_run.py SL68 4 0.5 2 0.003 2 R 1,8,16,32 > ../f4_SL68.out 2>&1
python3 f4_run.py B150 5 0.25 6 0.003 2 R 1,2,4 fb > ../f4_B150.out 2>&1
python3 f4_run.py Dnrk4 4 0.5 2 0.0015 4 R 1,2,4 fb > ../f4_Dnrk4.out 2>&1
python3 f4_run.py SL88 4 0.5 2 0.003 2 R 1,8,16,32 fb8 > ../f4_SL88.out 2>&1
echo QUEUE_DONE > ../queue2.done
