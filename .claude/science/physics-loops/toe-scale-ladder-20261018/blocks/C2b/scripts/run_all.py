#!/usr/bin/env python3
"""Run all C2b runners and print the combined TOTAL line (about 8 minutes on one core)."""
import os
import re
import subprocess
import sys

here = os.path.dirname(os.path.abspath(__file__))
runners = ['kip_group_theory.py', 'kip_parameter_selection.py', 'kip_flow.py', 'kip_collins_toy.py']
P = F = 0
for r in runners:
    out = subprocess.run([sys.executable, os.path.join(here, r)], capture_output=True, text=True)
    print(f"===== {r} (exit {out.returncode})")
    with open(os.path.join(here, '..', 'logs', r.replace('.py', '.runall.log')), 'x') as fh:
        fh.write(out.stdout + out.stderr)
    print(out.stdout, end='')
    if out.stderr.strip():
        print(out.stderr, end='')
    m = re.findall(r'TOTAL: PASS=(\d+) FAIL=(\d+)', out.stdout)
    if m:
        P += int(m[-1][0]); F += int(m[-1][1])
    else:
        F += 1
        print(f"FAIL [runner] {r} printed no TOTAL line")
print(f"TOTAL: PASS={P} FAIL={F}")
sys.exit(1 if F else 0)
