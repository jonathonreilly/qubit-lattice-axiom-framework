#!/usr/bin/env python3
"""Harness audit of C4b's c4b_closure.py: wrap sympy.solve so that every solution returned to the runner is
back-substituted into ALL its equations.  sympy.solve(eqs, unknowns) silently discards equations that involve only
parameters (shown in chk_B H1), so a PASS built on `solve(...) == expected` can hide an inconsistency.
Runs the C4b sections given on the command line, unchanged, and reports any solution that fails back-substitution.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
TGT = os.path.join(HERE, "..", "C4b_walker_closure")
sys.path.insert(0, TGT)
import sympy as sp
_orig = sp.solve
BAD = []
def wrapped(eqs, *args, **kw):
    out = _orig(eqs, *args, **kw)
    if isinstance(eqs, (list, tuple)) and kw.get("dict") and isinstance(out, list):
        for s_ in out:
            res = [sp.expand(e.subs(s_)) for e in eqs]
            nz = [r for r in res if sp.simplify(r) != 0]
            if nz:
                BAD.append((s_, nz[:3]))
                print(f"   [AUDIT] solution {s_} leaves {len(nz)} nonzero equations, e.g. {nz[:3]}", flush=True)
    return out
sp.solve = wrapped
sys.argv = ["c4b_closure.py"] + sys.argv[1:]
os.chdir(TGT)
src = open(os.path.join(TGT, "c4b_closure.py")).read()
exec(compile(src, "c4b_closure.py", "exec"), {"__name__": "__main__"})
print(f"AUDIT: {len(BAD)} solutions failed back-substitution")
