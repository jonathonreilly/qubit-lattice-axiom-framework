#!/usr/bin/env python3
"""X1, X3, X4 on constant links, N' = 1. Criteria: CRITERIA.md."""
import os, sys, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ex_core import *

s3 = 1 / 3**0.5
DIRS = {
    "D3": [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]],
    "D2": [[1, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 0]],
    "D4": [[1, 0, 0], [0, 1, 0], [0, 0, 1], [s3, s3, s3]],
    "T2": [[1, 0, 0], [0, 1, 0], [1, 0, 0], [0, 1, 0]],
}
def ce(L): return (1 / 9) * (1 - L**-2)

def run(name, a, L, k, verbose=False):
    V = constant_links(DIRS[name], a)
    ch = Chain(1, L, 4, k)
    pb = Problem(ch, V)
    t0 = time.time()
    U, lam, gn, rn = pb.solve(pb.initial(), verbose=verbose)
    fs = ch.fields(U)
    S = [float(wilson(x)) for x in fs]
    f, E = flux_stats(V)
    I = float(I_grad(V))
    e = S[-2] - S[-1]
    Y = S[0] - S[-1]
    c1 = ce(L) / 2
    C = (c1 * I - e) / (f * E)
    return dict(name=name, a=a, L=L, k=k, f=f, E=E, I=I, e=e, Y=Y, S=S, eI=e / I, C=C, g=gn, r=rn, fl=[flux_stats(x)[0] for x in fs], t=time.time() - t0)

out = []
for name in DIRS:
    for a in [0.2, 0.2 / 2.5**0.5, 0.2 / 2.5]:
        for L in [3, 5]:
            r = run(name, a, L, 1); out.append(r)
            print(f"{name} a={a:.4f} L={L} k=1 f={r['f']:.5f} E={r['E']:.5e} I={r['I']:.5e} e={r['e']:.5e} e/I={r['eI']:.5f} C_eff={r['C']:.4f} g,r={r['g']:.0e},{r['r']:.0e} t={r['t']:.1f}", flush=True)
json.dump(out, open("x_const_1.json", "w"))

print("--- L scan, fixed f L^0 and fixed f L^2", flush=True)
for name in ["D3", "D2"]:
    for L in [3, 5, 7, 9]:
        for a in [0.08, 0.24 / L]:
            r = run(name, a, L, 1); out.append(r)
            print(f"{name} a={a:.4f} L={L} k=1 f={r['f']:.5f} e/I={r['eI']:.5f} C_eff={r['C']:.4f} f_lvl={r['fl']} g,r={r['g']:.0e},{r['r']:.0e} t={r['t']:.1f}", flush=True)
json.dump(out, open("x_const_2.json", "w"))

print("--- levels", flush=True)
for name in ["D3", "D2", "D4", "T2"]:
    for a in [0.2, 0.08]:
        r1 = run(name, a, 3, 1)
        r2 = run(name, a, 3, 2); out.append(r2)
        e2 = r2['S'][-2] - r2['S'][-1]
        print(f"{name} a={a} L=3: e^(1)={r1['e']:.6e} e_(k=2 top)={e2:.6e} excess_diff/E={(e2-r1['e'])/r1['E']:.3e} Y2={r2['Y']:.6e} e_0={r2['S'][0]-r2['S'][1]:.6e} ratio e_0/e_1={(r2['S'][0]-r2['S'][1])/e2:.5f} f_lvl={r2['fl']} g,r={r2['g']:.0e},{r2['r']:.0e} t={r2['t']:.1f}", flush=True)
json.dump(out, open("x_const_3.json", "w"))
