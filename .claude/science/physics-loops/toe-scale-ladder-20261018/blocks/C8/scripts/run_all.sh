#!/usr/bin/env bash
# C8 runner. Default: fast scripts are rerun; the production lattice integrals (about 50 min on one
# core) are resumed from logs/c8_results.json (each entry recomputes only if missing).
# FULL=1 deletes the checkpoint and recomputes everything (run the three jobs separately if a
# 25-minute job limit applies).
set -u
cd "$(dirname "$0")/.."
[ "${FULL:-0}" = 1 ] && rm -f logs/c8_results.json
nice -n 10 python3 scripts/c8_exact.py            > logs/c8_exact.log 2>&1
nice -n 10 python3 scripts/c8_continuum_exact.py  > logs/c8_continuum_exact.log 2>&1
nice -n 10 python3 scripts/c8_continuum.py        > logs/c8_continuum.log 2>&1
[ "${SKIP_ED:-0}" = 1 ] || nice -n 10 python3 scripts/c8_ed_check.py > logs/c8_ed_check.log 2>&1
for j in A B C D; do nice -n 10 python3 scripts/c8_lattice.py $j > logs/c8_lattice_$j.resume.out 2>&1; done
nice -n 10 python3 scripts/c8_tt_mass.py          > logs/c8_tt_mass.log 2>&1
nice -n 10 python3 scripts/c8_gold_bound.py       > logs/c8_gold_bound.log 2>&1
nice -n 10 python3 scripts/c8_report.py           > logs/c8_report.log 2>&1
{
  for f in c8_exact c8_continuum_exact c8_continuum c8_ed_check c8_tt_mass c8_gold_bound c8_report; do
    echo "$f: $(grep '^TOTAL' logs/$f.log)"
  done
  awk '/^TOTAL/ {split($2,a,"="); split($3,b,"="); p+=a[2]; f+=b[2]} END {print "TOTAL: PASS=" p " FAIL=" f}' \
    logs/c8_exact.log logs/c8_continuum_exact.log logs/c8_continuum.log logs/c8_ed_check.log logs/c8_tt_mass.log logs/c8_gold_bound.log logs/c8_report.log
} > logs/run_all.log
cat logs/run_all.log
