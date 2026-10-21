#!/bin/bash
# sequential, one core, nice 10; every step is checkpointed / restartable
cd "$(dirname "$0")"
nice -n 10 python3 r8_routeB.py bstar 32 0.0 1.5707963267948966 L1 > logs/r8_lapse.out 2>&1
nice -n 10 python3 r8_symbolic.py > logs/r8_symbolic.log 2>&1
for th in 0.2 0.05; do nice -n 10 python3 r8_gold.py author $th 48 >> logs/r8_gold.out 2>&1; done
for th in 0.05 0.0125 0.003 0.0; do nice -n 10 python3 r8_gold.py own $th 48 >> logs/r8_gold.out 2>&1; done
for L in 64 96 128 160; do nice -n 10 python3 r8_routeA.py $L >> logs/r8_routeA.out 2>&1; done
echo QUEUE_DONE >> logs/r8_gold.out
