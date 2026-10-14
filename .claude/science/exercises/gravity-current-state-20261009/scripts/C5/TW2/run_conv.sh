#!/bin/bash
export OMP_NUM_THREADS=2
cd "$(dirname "$0")"
for G in "8 0.25 10:240" "6 0.25 8:168" "10 0.2 12:340"; do
  args=${G%%:*}; N=${G##*:}
  for P in S T L; do
    /usr/bin/time -l python3 tw2_conv.py $P $args 0.003 > tw2_conv_${P}_${N}.out 2> tw2_conv_${P}_${N}.time
  done
done
echo done > run_conv.done
