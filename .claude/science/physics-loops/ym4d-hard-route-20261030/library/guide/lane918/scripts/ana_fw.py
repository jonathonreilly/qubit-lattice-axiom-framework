#!/usr/bin/env python3
"""GUIDE (row 918, family 3): free-wall thermal log-sums g(a; B) and doubling ratios from fwti logs (T = 12).
g(a; B) - (a/12) g(12; B) by trapezoid TI (ana_ti.integ). Ladder steps (b,b,b)->(2b,b,b)->(2b,2b,b)->(2b,2b,2b);
join excess E = g(after) - 2 g(before), ratio k = g(after)/g(before). Errors by Gaussian propagation."""
import json, sys
import numpy as np
def load(fn):
    rows = [json.loads(l) for l in open(fn) if l.startswith('{')]
    return rows

def integ(bs, f, df, bout):
    bs = np.concatenate([[0.0], bs]); f = np.concatenate([[0.0], f]); df = np.concatenate([[0.0], df])
    k = int(np.nonzero(np.isclose(bs, bout))[0][0])
    h = np.diff(bs[:k+1])
    val = (0.5*h*(f[:k] + f[1:k+1])).sum()
    w = np.zeros(k+1); w[:k] += 0.5*h; w[1:k+1] += 0.5*h
    err = np.sqrt(((w*df[:k+1])**2).sum())
    return val, err


def g_of(t, tag, beta, T=12):
    ref = load(f"out/fwti_{T}_{tag}.log"); rows = load(f"out/fwti_{t}_{tag}.log")
    bs = np.array([r['beta'] for r in ref])
    f = np.array([r['Nc']*r['P'] - (t/T)*q['Nc']*q['P'] for r, q in zip(rows, ref)])
    df = np.array([np.hypot(r['Nc']*r['dP'], (t/T)*q['Nc']*q['dP']) for r, q in zip(rows, ref)])
    return integ(bs, f, df, beta)

for beta in (2.3, 2.5):
    print(f"beta {beta}")
    for b in (2, 3, 4):
        if b < 4:
            tags = [f"{b}x{b}x{b}", f"{2*b}x{b}x{b}", f"{2*b}x{2*b}x{b}", f"{2*b}x{2*b}x{2*b}"]
        else:
            tags = ["4x4x4", "8x4x4"]
        for t in (2, 3, 4):
            try: gs = [g_of(t, tg, beta) for tg in tags]
            except Exception as e: print('  missing', b, t, e); continue
            line = f"  b={b} a={t}: g = " + ", ".join(f"{g:.3f}({e:.3f})" for g, e in gs)
            ks = []
            for (g0, e0), (g1, e1) in zip(gs[:-1], gs[1:]):
                k = g1/g0; ek = abs(k)*np.hypot(e1/g1 if g1 else 0, e0/g0 if g0 else 0)
                E = g1 - 2*g0; eE = np.hypot(e1, 2*e0)
                ks.append(f"k={k:.2f}({ek:.2f}) E={E:+.3f}({eE:.3f})")
            line += " | " + "; ".join(ks) + f" | S_0 = e^g - 1 = {np.expm1(gs[0][0]):.3g}"
            print(line)
