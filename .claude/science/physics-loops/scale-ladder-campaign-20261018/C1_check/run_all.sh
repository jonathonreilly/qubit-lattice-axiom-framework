#!/bin/sh
# C1 checker: run from this directory. ~6 min total on 4 cores.
for s in chk1_det_selection chk2_subgroup_channels chk3_anomaly_bdg chk4_slice_inversion; do python3 $s.py > $s.log 2>&1; done
python3 probe_tomega.py 5 > probe_tomega.log 2>&1
grep -H "TOTAL" chk*_*.log | grep -v firstrun > run_all_aggregate.log
