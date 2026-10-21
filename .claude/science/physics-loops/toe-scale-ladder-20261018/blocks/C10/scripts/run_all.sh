#!/bin/sh
# C10 runners; writes ../logs/<name>.log and ../logs/run_all.log (never overwrite: refuses if logs exist)
cd "$(dirname "$0")" || exit 1
L=../logs
for f in c10_exact c10_numeric run_all; do [ -e $L/$f.log ] && { echo "log $L/$f.log exists; move it first"; exit 1; }; done
nice -n 10 python3 c10_exact.py > $L/c10_exact.log 2>&1
nice -n 10 python3 c10_numeric.py > $L/c10_numeric.log 2>&1
python3 - <<'PY' > $L/run_all.log
import re
P=F=0
for n in ('c10_exact','c10_numeric'):
    t=open(f'../logs/{n}.log').read(); m=re.findall(r'TOTAL: PASS=(\d+) FAIL=(\d+)',t)[-1]
    print(f'{n}: PASS={m[0]} FAIL={m[1]}'); P+=int(m[0]); F+=int(m[1])
print(f'TOTAL: PASS={P} FAIL={F}')
PY
cat $L/run_all.log
