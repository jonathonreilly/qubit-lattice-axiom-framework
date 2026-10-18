#!/bin/sh
cd "$(dirname "$0")"
while pgrep -f "prod.py 4 0.0 4000 0 102" >/dev/null || pgrep -f "prod.py 4 -0.5 4000 0 103" >/dev/null; do sleep 10; done
cat jobs3.txt | xargs -P 3 -L 1 sh -c 'python prod.py $0 $1 $2 $3 $4 $5 $6 $7 >> prod1.log 2>&1'
