#!/usr/bin/env python3
"""GUIDE (row 918): g(a) from Delta(a) = 2 g(a) - g(2a): g(2) = D2/2 + D4/4 + D8/8 + tail, g(4) = D4/2 + D8/4 + tail.
Tail bound: g(16) <= g(8) (monotone in t) and g(8) <= D8/2 + g(16)/2 gives g(8) <= D8 ... we report
g_lo = truncated sum (tail >= 0) and g_hi = g_lo + (last D)/(2^k) (using g(next) <= g(last) <= last D).
Free-wall ladder ratios k = g(after)/g(before), join excess E = g(after) - 2 g(before), seed S = e^g - 1."""
import json, glob
import numpy as np
rng = np.random.default_rng(1)

def D(prefix, a, tag, beta):
    fn = f"out/{prefix}_{a}_{tag}_{beta}.log"
    try:
        r = [json.loads(l) for l in open(fn) if '"Delta"' in l][-1]
        return r['Delta'], r['dDelta']
    except Exception:
        return None

def gs(prefix, tag, beta, n=20000):
    d = {a: D(prefix, a, tag, beta) for a in (2, 4, 8)}
    if any(v is None for v in d.values()): return None
    s = {a: rng.normal(m, e, n) for a, (m, e) in d.items()}
    g2 = s[2]/2 + s[4]/4 + s[8]/8; g2hi = g2 + s[8]/8
    g4 = s[4]/2 + s[8]/4; g4hi = g4 + s[8]/4
    g8 = s[8]/2; g8hi = s[8]
    return {2: (g2, g2hi), 4: (g4, g4hi), 8: (g8, g8hi)}, d

def q(x): return f"{np.median(x):.3f} [{np.percentile(x,16):.3f}, {np.percentile(x,84):.3f}]"

if __name__ == '__main__':
    for beta in ('2.3', '2.5'):
        print(f"beta {beta}")
        for ladder in (["2x2x2", "4x2x2", "4x4x2", "4x4x4"], ["3x3x3", "6x3x3"]):
            res = {tg: gs('spfw', tg, beta) for tg in ladder}
            for tg in ladder:
                if res[tg] is None: print('  ', tg, 'missing'); continue
                G, d = res[tg]
                print(f"  {tg}: Delta(2,4,8) = " + ", ".join(f"{m:.4f}({e:.4f})" for m, e in d.values())
                      + " | g(2) " + q(G[2][0]) + " g(4) " + q(G[4][0]) + " g(8) <= " + q(G[8][1]))
            for t in (2, 4):
                for x, y in zip(ladder[:-1], ladder[1:]):
                    if res[x] is None or res[y] is None: continue
                    g0 = res[x][0][t][0]; g1 = res[y][0][t][0]
                    print(f"   a={t} {x}->{y}: k = {q(g1/g0)}  E = g1 - 2 g0 = {q(g1 - 2*g0)}  S_before = {q(np.expm1(g0))}")
