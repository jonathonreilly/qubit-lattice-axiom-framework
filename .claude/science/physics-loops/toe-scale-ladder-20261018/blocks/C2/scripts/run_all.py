#!/usr/bin/env python3
"""Run all C2 runners and sum their PASS/FAIL counts."""
import re, subprocess, sys, pathlib
here = pathlib.Path(__file__).parent
P = F = 0
for s in ['witness_supplied_ingredients.py', 'witness_os0_surface.py', 'rg_one_loop_analytic.py', 'rg_independent_numeric.py']:
    out = subprocess.run([sys.executable, str(here / s)], capture_output=True, text=True).stdout
    m = re.search(r'TOTAL: PASS=(\d+) FAIL=(\d+)', out)
    p, f = (int(m.group(1)), int(m.group(2))) if m else (0, 1)
    print(f"{s}: PASS={p} FAIL={f}")
    P += p; F += f
print(f"TOTAL: PASS={P} FAIL={F}")
sys.exit(0 if F == 0 else 1)
