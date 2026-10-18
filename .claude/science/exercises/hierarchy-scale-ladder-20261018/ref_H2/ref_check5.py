#!/usr/bin/env python3
"""Referee check 5: the PR #9702 projective structure (I R I^-1 R^-1 = A2(R), E1/2 at k*, E5/2 at -k*),
which none of the worker's 8 variants realises. D_PR(g) = D_w(g) Lambda(prop g), Lambda = A2 on nodes
{111, hw2} (-k* and -k*+pi e_i), 1 on {000, hw1}. Re-run sv orders, generic-Fix rank, and exact pair-block
true gaps (single charge)."""
import sys
sys.argv = ['orders_group.py', 'A1-A1']
sys.path.insert(0, '/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/hier/H2/scripts')
import numpy as np
import orders_group as og
from scipy.optimize import minimize
B = [s for s in og.NODES if sum(s) in (2, 3)]
DPR = []
for (ti, k) in og.GAM:
    p = og.oidx(og.PROP[k]); a = og.a2(p)
    Lam = np.kron(np.diag([a if s in B else 1 for s in og.NODES]), np.eye(2))
    DPR.append(og.DN[og.GID[(ti, k)]] @ Lam)
DPR = np.array(DPR)
rng = np.random.default_rng(5)
for _ in range(300):
    a, b = rng.integers(og.NG, size=2); X = DPR[a] @ DPR[b]; Y = DPR[og.MUL[a, b]]
    ph = np.vdot(Y.ravel(), X.ravel()) / np.vdot(Y.ravel(), Y.ravel()); assert np.allclose(X, ph * Y)
I = og.GID[(0, og.oidx(-np.eye(3, dtype=int)))]
comm = []
for k in range(48):
    if og.DET[k] != 1: continue
    R = og.GID[(0, k)]; C = DPR[I] @ DPR[R] @ np.linalg.inv(DPR[I]) @ np.linalg.inv(DPR[R])
    comm.append((og.a2(k), np.allclose(C, og.a2(k) * np.eye(16)) or np.allclose(C, -og.a2(k) * np.eye(16)) and False))
print("I R I^-1 R^-1 = A2(R) * 1 for all proper R:", all(ok for _, ok in comm))
for _ in range(10):
    q = rng.normal(size=3); g = int(rng.integers(og.NG)); ti, k = og.GAM[g]
    assert np.allclose(DPR[g] @ og.H0(q) @ DPR[g].conj().T, og.H0(og.OH[k] @ q))
print("H0 covariant under D_PR: yes")
og.DN = DPR
NID = og.NID; PAU = og.PAU
Pc = {(1, 1, 1): np.eye(2), (1, 0, 0): PAU[0], (0, 1, 0): PAU[1], (0, 0, 1): PAU[2]}
def h_node(s, q): return sum(((-1)**s[j]) * q[j] * PAU[j] for j in range(3))
r0 = np.random.default_rng(42)
def pair_gap(H, s, sp, eps):
    idx = [2*NID[s], 2*NID[s]+1, 2*NID[sp], 2*NID[sp]+1]; Hp = H[np.ix_(idx, idx)]
    def g(q):
        A = np.zeros((4, 4), complex); A[:2, :2] = h_node(s, q); A[2:, 2:] = h_node(sp, q)
        e = np.linalg.eigvalsh(A + Hp); return (e[2] - e[1]) / 2
    best = g(np.zeros(3))
    for x0 in [np.zeros(3)] + [r0.normal(size=3) * eps for _ in range(6)]:
        best = min(best, minimize(g, x0, method='Nelder-Mead', options=dict(xatol=1e-15, fatol=1e-18, maxiter=2500)).fun)
    return max(best, 0)
allfin = set(); pertrue = []
for ki, (key, mats) in enumerate(og.REPS.items()):
    if key[0] in ('000', 'hw2'): continue
    for li, (order, phi) in enumerate(og.fixed_lines(mats)):
        Hs = og.stab(mats, phi)
        tch = []
        for ti in range(8):
            v = mats[og.GID[(ti, og.oidx(np.eye(3, dtype=int)))]] @ phi
            tch.append(1 if np.allclose(v, phi) else (-1 if np.allclose(v, -phi) else 0))
        cvec = None
        if all(x != 0 for x in tch):
            for c in og.NODES:
                if all(tch[ti] == (-1)**int(np.dot(c, og.TR[ti])) for ti in range(8)): cvec = c
        rr = np.random.default_rng(1000 * ki + 17 * li)
        fs = og.f_eval(og.generic_maps(mats, rr), mats, phi)
        fs = [f / np.linalg.norm(f) if np.linalg.norm(f) > 1e-10 else 0 * f for f in fs]
        od, sv = og.orders(fs)
        fin = sorted(set(int(round(x)) for x in od if np.isfinite(x))); allfin |= set(fin)
        nm = sum(1 for x in od if np.isfinite(x))
        line = f"{key[0]:>3} {key[1]:<4} dir{li:<2} |Stab|={len(Hs):<3} c={cvec} sv-orders={fin} n_massive_sv={nm}"
        if cvec is not None and sum(cvec) % 2 == 1 and fin:
            tr = []
            for s in og.NODES:
                if og.CHI[NID[s]] > 0: continue
                sp = tuple((a + b) % 2 for a, b in zip(s, cvec))
                gaps = [pair_gap(sum((e**(n+1)) * fs[n] for n in range(7)), s, sp, e) for e in (0.01, 0.005)]
                tr.append('gapless' if min(gaps) < 1e-13 else f"{np.log(gaps[0]/gaps[1])/np.log(2):.1f}")
            line += f"  TRUE pair-gap orders {tr}"
            pertrue.append(set(x for x in tr if x != 'gapless'))
        print(line); sys.stdout.flush()
print("\nall sv orders seen:", sorted(allfin))
print("max distinct true-gap orders per single-charge direction:", max((len(s) for s in pertrue), default=0),
      "; true orders seen:", sorted(set().union(*pertrue)) if pertrue else [])
