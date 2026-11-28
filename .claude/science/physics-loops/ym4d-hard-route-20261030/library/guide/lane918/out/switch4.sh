#!/bin/bash
cd "$(dirname "$0")/.."
until grep -q "END spfw_8_6x3x3_2.3" out/queue_split.log; do sleep 3; done
pkill -f "run_queue.sh out/q_split.txt"; sleep 2; pkill -f "scripts/split.py 2 2 2 2 2.5"
echo "queue_split stopped after the 2.3 free-wall ladder" >> out/queue_split.log
scripts/run_queue.sh out/q4.txt > out/queue4.log 2>&1
