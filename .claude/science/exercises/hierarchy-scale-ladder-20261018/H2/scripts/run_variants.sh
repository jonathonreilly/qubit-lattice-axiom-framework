#!/bin/zsh
# runs the 8 node-representation variants one at a time, each under the 0.4 GB watchdog
cd ${0:a:h}
for v in A1-A1 A2-A1 A1-A2 A2-A2 A1-B1 A2-B1 A1-B2 A2-B2; do
  echo "start $v $(date -u +%H:%MZ)" >> run_variants.log
  zsh capped.sh orders_$v.out python3 orders_group.py $v
  echo "done $v $(date -u +%H:%MZ)" >> run_variants.log
done
echo ALLDONE >> run_variants.log
