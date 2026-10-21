#!/bin/bash
cd "$(dirname "$0")"
while pgrep -f run_queue.sh > /dev/null; do sleep 20; done
for th in 0.0 0.003; do nice -n 10 python3 r8_gold.py own $th 64 >> logs/r8_gold.out 2>&1; done
echo QUEUE2_DONE >> logs/r8_gold.out
