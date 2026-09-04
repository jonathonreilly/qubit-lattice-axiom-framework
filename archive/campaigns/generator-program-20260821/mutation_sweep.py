#!/usr/bin/env python3
"""Run the block-106 runner under every mutation; report per-run gate tallies.

For each mutation: expect exit != 0, exactly one FAIL line, and record which
gate letter failed. Baseline run must be all-PASS (except any gate the
supervisor knows is pending, e.g. the note-scope gate before the note lands).
"""
import re
import subprocess
import sys

RUNNER = "scripts/admissibility_dirac_kahler_closure_audit_two_2026_08_21.py"

def run(mutation=None):
    cmd = [sys.executable, RUNNER] + (["--mutation", mutation] if mutation else [])
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    fails = re.findall(r"^\[FAIL\] ([A-Z])", p.stdout, re.M)
    passes = len(re.findall(r"^\[PASS\]", p.stdout, re.M))
    return p.returncode, passes, fails

helpout = subprocess.run([sys.executable, RUNNER, "--help"], capture_output=True, text=True).stdout
m = re.search(r"--mutation\s*\{([^}]*)\}", helpout, re.S)
muts = [x.strip() for x in m.group(1).split(",")] if m else []
print(f"mutations declared: {len(muts)}")

rc, np_, nf = run()
print(f"BASELINE: exit={rc} PASS={np_} FAIL={nf}")

bad = []
for mu in muts:
    rc, np_, fails = run(mu)
    ok = rc != 0 and len(fails) == 1
    print(f"{'OK ' if ok else 'BAD'} {mu}: exit={rc} fails={fails}")
    if not ok:
        bad.append(mu)
print(f"SWEEP DONE: {len(muts) - len(bad)}/{len(muts)} clean; bad={bad}")
