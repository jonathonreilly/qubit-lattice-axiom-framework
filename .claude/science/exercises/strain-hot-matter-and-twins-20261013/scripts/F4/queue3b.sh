#!/bin/bash
cd "$(dirname "$0")"
export OMP_NUM_THREADS=2
while [ ! -f ../queue2.done ]; do sleep 3; done
python3 f4_run.py D2 4 0.5 2 0.003 2 R 1,2,4 fb > ../f4_D2.out 2>&1
python3 f4_run.py J240 8 0.25 10 0.003 2 R 1 > ../f4_J240.out 2>&1
python3 f4_run.py J344 8 0.15 16 0.003 2 R 1 > ../f4_J344.out 2>&1
echo QUEUE_DONE > ../queue3.done
