#!/bin/bash
# Reproduce: exact covariant subspaces, real-form unitarity ideals, Singular certificates.
set -e
cd "$(dirname "$0")"
python3 t0.py                                   # groups, SU(2) lifts, covariant dims 7/11/15
for g in O T D4; do python3 tosing_real.py $g; done
for g in O T D4; do echo "== $g"; (cat sysR_$g.sing certR.sing; echo 'quit;') > cert_$g.sing; ./runsing.sh cert_$g.sing; done
(cat sysR_D4.sing d4comp.sing; echo 'quit;') > comp_D4.sing; ./runsing.sh comp_D4.sing | sed -n '/number of minimal/,$p'
python3 eqsO.py O >/dev/null && python3 radO.py  # sympy-only cross-check for O (needs gb_O.pkl from gbO.py)
