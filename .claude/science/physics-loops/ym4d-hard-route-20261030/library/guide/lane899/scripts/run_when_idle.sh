#!/bin/sh
# Waits (at most about 9 minutes) for the 1-minute load average to fall below 8,
# then runs the guide script once, single thread, lowest priority.
S="$1"
i=0
while [ $i -lt 36 ]; do
  L=$(sysctl -n vm.loadavg | awk '{print $2}')
  if awk -v l="$L" 'BEGIN{exit !(l < 8.0)}'; then
    echo "load $L at start" > "$S/out/slab_ladder_guide.out"
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 \
      nice -n 19 python3 -I "$S/scripts/slab_ladder_guide.py" >> "$S/out/slab_ladder_guide.out" 2>&1
    echo "exit $?" >> "$S/out/slab_ladder_guide.out"
    exit 0
  fi
  i=$((i+1))
  sleep 15
done
echo "NOT RUN: 1-minute load stayed at or above 8 for 9 minutes (last $L)" > "$S/out/slab_ladder_guide.out"
exit 0
