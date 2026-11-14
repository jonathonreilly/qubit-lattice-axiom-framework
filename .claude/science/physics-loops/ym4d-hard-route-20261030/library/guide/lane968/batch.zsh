#!/bin/zsh
LAB=/Users/jonBridger/ym4d-worker/repo/scripts/lab_ops.py
REPO=/Users/jonBridger/ym4d-worker/repo
cd $REPO
got=0
for i in {1..60}; do
  if python3 $LAB numeric-lock acquire --holder gap-avgcurv-968 --purpose "row 968 tilt GUIDE batch, about 1 h" --ttl-hours 2 | grep -q '"acquired"'; then got=1; break; fi
  sleep 60
done
[[ $got == 1 ]] || { echo "NO LOCK after 60 min"; exit 1 }
trap "cd $REPO && python3 $LAB numeric-lock release --holder gap-avgcurv-968 | grep status" EXIT
free=$(memory_pressure | awk '/free percentage/ {gsub("%","",$NF); print $NF}')
echo "lock acquired $(date -u +%H:%M:%S); memory free ${free}%"
(( free >= 50 )) || { echo "LOW MEMORY"; exit 2 }
cd /tmp/gap-avgcurv-968
: > logs/tilt_results.jsonl; : > logs/tilt_err.log
run() { perl -e 'alarm shift; exec @ARGV' 1500 nice python3 -I scripts/tilt.py "$@" >> logs/tilt_results.jsonl 2>> logs/tilt_err.log }
KU=(0 0.3 0.5 0.7 1.0 1.5 2.5)
KS=(0 0.6 1.0 1.4 1.9 2.6 4.0)
sd=100
for k in $KU; do sd=$((sd+1)); run u1 8 6 1.3 $k 400 2000 2 $sd; done
for k in $KS; do sd=$((sd+1)); run su2 8 6 2.3 $k 400 2000 2 $sd; done
echo "stage 1 done $(date -u +%H:%M:%S)"
for k in $KU; do sd=$((sd+1)); run u1 16 6 1.3 $k 400 2000 2 $sd; done
for k in $KS; do sd=$((sd+1)); run su2 12 6 2.3 $k 400 2000 2 $sd; done
echo "stage 2 done $(date -u +%H:%M:%S)"
for k in $KS; do sd=$((sd+1)); run su2 16 6 2.3 $k 400 2000 2 $sd; done
for k in $KU; do sd=$((sd+1)); run u1 24 6 1.3 $k 400 2000 2 $sd; done
echo "BATCH done $(date -u +%H:%M:%S)"
