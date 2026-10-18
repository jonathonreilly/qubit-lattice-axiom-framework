#!/usr/bin/env python3
"""Referee check 2 (same family): are the singular values of the chirality-odd block real Dirac gaps?
Single-charge directions: H is exactly block-diagonal in node pairs (s, s+c). For each pair, the
true mass = half the direct gap (E3-E2)/2 of H0(q)+H(eps) minimised over q, at eps = 0.02, 0.01, 0.005.
Also the Dirac-mass component of the 2x2 block along P_c (P_111 = 1, P_100 = sx, P_010 = sy, P_001 = sz;
the unique M with h_s M + M h_s' = 0) and the tensor remainder.
Multi-charge directions: half the band-centre direct gap (E9-E8)/2 of the full 16-band H (uniform trace removed)."""
import sys
VAR = sys.argv[1] if len(sys.argv) > 1 else 'A1-A1'
sys.argv = ['orders_group.py', VAR]
sys.path.insert(0, '/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/hier/H2/scripts')
import numpy as np
import orders_group as og
from scipy.optimize import minimize
NODES, NID = og.NODES, og.NID
PAU = og.PAU; I2 = np.eye(2)
rng0 = np.random.default_rng(99)
EPSL = [0.02, 0.01, 0.005]
def Hfull(fs, eps): return sum((eps**(n+1)) * fs[n] for n in range(og.NMAX))
def h_node(s, q): return sum(((-1)**s[j]) * q[j] * PAU[j] for j in range(3))
def minimise(g, sc, nstart=7):
    best = g(np.zeros(3))
    for x0 in [np.zeros(3)] + [rng0.normal(size=3) * sc for _ in range(nstart - 1)]:
        r = minimize(g, x0, method='Nelder-Mead', options=dict(xatol=1e-15, fatol=1e-18, maxiter=2500))
        best = min(best, r.fun)
    return best
def pair_gap(H, s, sp, eps):
    idx = [2*NID[s], 2*NID[s]+1, 2*NID[sp], 2*NID[sp]+1]; Hp = H[np.ix_(idx, idx)]
    def g(q):
        A = np.zeros((4, 4), complex); A[:2, :2] = h_node(s, q); A[2:, 2:] = h_node(sp, q)
        e = np.linalg.eigvalsh(A + Hp); return (e[2] - e[1]) / 2
    return max(minimise(g, eps), 0.0)
def mid_gap(H, eps):
    H = H - np.trace(H).real / 16 * np.eye(16)
    def g(q):
        e = np.linalg.eigvalsh(og.H0(q) + H); return (e[8] - e[7]) / 2
    return max(minimise(g, eps), 0.0)
def slope(v):
    if v[-1] < 1e-13 or v[-2] < 1e-13: return 'gapless'
    return f"{np.log(v[-2]/v[-1])/np.log(2):.2f}"
Pc = {(1, 1, 1): I2, (1, 0, 0): PAU[0], (0, 1, 0): PAU[1], (0, 0, 1): PAU[2]}
summary = []
for ki, (key, mats) in enumerate(og.REPS.items()):
    if key[0] in ('000', 'hw2'): continue
    for li, (order, phi) in enumerate(og.fixed_lines(mats)):
        tch = []
        for ti in range(8):
            v = mats[og.GID[(ti, og.oidx(np.eye(3, dtype=int)))]] @ phi
            tch.append(1 if np.allclose(v, phi) else (-1 if np.allclose(v, -phi) else 0))
        cvec = None
        if all(x != 0 for x in tch):
            for c in NODES:
                if all(tch[ti] == (-1)**int(np.dot(c, og.TR[ti])) for ti in range(8)): cvec = c
        rng = np.random.default_rng(1000 * ki + 17 * li + 0)
        fs = og.f_eval(og.generic_maps(mats, rng), mats, phi)
        fs = [f / np.linalg.norm(f) if np.linalg.norm(f) > 1e-10 else 0 * f for f in fs]
        od, _ = og.orders(fs)
        fin = sorted(set(int(round(x)) for x in od if np.isfinite(x)))
        if not fin: continue
        head = f"{key[0]:>3} {key[1]:<4} dir{li:<2} c={cvec} sv-orders={fin}"
        if cvec is not None and sum(cvec) % 2 == 1:
            true_orders = []; txt = ''
            for s in NODES:
                if og.CHI[NID[s]] > 0: continue
                sp = tuple((a + b) % 2 for a, b in zip(s, cvec))
                gaps = []; svs = []
                for eps in EPSL:
                    H = Hfull(fs, eps)
                    Mb = H[2*NID[sp]:2*NID[sp]+2, 2*NID[s]:2*NID[s]+2]
                    svs.append(np.linalg.svd(Mb, compute_uv=False)[-1])
                    gaps.append(pair_gap(H, s, sp, eps))
                Mb1 = fs[0][2*NID[sp]:2*NID[sp]+2, 2*NID[s]:2*NID[s]+2]
                P = Pc[cvec]; mD = abs(np.trace(P @ Mb1)) / 2; mT = np.linalg.norm(Mb1 - np.trace(P @ Mb1) / 2 * P)
                so = slope(svs) if svs[-1] > 1e-13 else 'inf'; go = slope(gaps)
                true_orders.append(go)
                txt += f"\n     pair {s}-{sp}: sv order {so}, true-gap order {go}, gap/sv@0.005={gaps[-1]/max(svs[-1],1e-300):.3f}; order-1 block: Dirac part {mD:.3f}, tensor part {mT:.3f}"
            summary.append((head, true_orders))
            print(head + "  TRUE pair-gap orders: " + str(true_orders) + txt)
        else:
            mg = [mid_gap(Hfull(fs, e), e) for e in EPSL]
            summary.append((head, ['mid:' + slope(mg)]))
            print(head + f"  multi-charge band-centre half-gap {['%.2e' % x for x in mg]} -> order {slope(mg)}")
        sys.stdout.flush()
print("\nSUMMARY of true-gap orders across massive odd-charge directions:")
from collections import Counter
allo = Counter(o for _, os in summary for o in os)
print(dict(allo))
