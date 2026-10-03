#!/bin/bash
# Re-runs the cheap checks and collects their output in outputs.txt (each run < 60 s, < 300 MB).
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1
cd "$(dirname "$0")"
: > outputs.txt
run () { echo "===== $* =====" >> outputs.txt; /usr/bin/time -l nice -n 10 python3 "$@" >> outputs.txt 2> time.tmp; grep -E "real|maximum resident" time.tmp | tr -s ' ' >> outputs.txt; }
run e1_conveyor_bond.py
run e2_bond_bond.py
run e15_triangle.py
run e17_triangle_2tick.py
run e18_triangle_line.py
run e16_partial_cut.py
run e12_certificate.py
run e3_plaquettes.py 2 tick 5 1 01 01
run e3_plaquettes.py 2 lattice 12 3 01 01
LPMETHOD=highs-ds run e9_forced_scan.py 400 8 tick
LPMETHOD=highs-ds run e9_forced_scan.py 400 9 tick real
run e9_forced_scan.py 20 9 lattice real
LPMETHOD=highs-ds run e10_rings.py 6 2 3 01 60 2 lattice
LPMETHOD=highs-ds run e10_rings.py 6 2 3 01 60 2 tick
LPMETHOD=highs-ds run e10_rings.py 6 2 3 12 60 3 lattice
run e19_laneM_setting.py
run e20_general_phi.py
rm -f time.tmp
