#!/usr/bin/env python3
"""Referee spot checks on HIER-2 R5 (same family). Imports the worker's module (top-level only).
(1) protected zeros: generic rank of the RL block of Fix(Stab phi) (charge-projected) vs number of masses found;
(2) order-2 chirality-even terms on order-3 pairs: Weyl-point offset |Delta|/2 vs the pair mass, and the
    true direct gap of H0(q)+H(eps) minimised over q (single-charge directions: exact 4x4 pair blocks);
(3) subgroup completeness: extra fixed lines from random 3-generator subgroups."""
import sys, itertools
VAR = sys.argv[1] if len(sys.argv) > 1 else 'A1-A1'
sys.argv = ['orders_group.py', VAR]
sys.path.insert(0, '/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/hier/H2/scripts')
import numpy as np
import orders_group as og
from scipy.optimize import minimize

NODES, NID, DN, NG = og.NODES, og.NID, og.DN, og.NG
iL, iR = og.iL, og.iR
rng0 = np.random.default_rng(777)

def fix_generic_rank(Hs, cvec, nsamp=3):
    Tt = [np.kron(np.diag([(-1.0)**int(np.dot(s, t)) for s in NODES]), np.eye(2)) for t in og.TR]
    DH = DN[Hs]; best = 0
    for _ in range(nsamp):
        X = og.herm(16, rng0)
        X = np.einsum('hij,jk,hlk->il', DH, X, DH.conj()) / len(Hs)
        T111 = Tt[NID[(1, 1, 1)]]; X = (X - T111 @ X @ T111) / 2
        if cvec is not None:
            chi = [(-1.0)**int(np.dot(cvec, t)) for t in og.TR]
            X = sum(chi[a] * Tt[a] @ X @ Tt[a] for a in range(8)) / 8
        sv = np.linalg.svd(X[np.ix_(iR, iL)], compute_uv=False)
        best = max(best, int(np.sum(sv > 1e-9 * max(1, sv.max()))))
    return best

def Hfull(fs, eps):
    return sum((eps**(n+1)) * fs[n] for n in range(og.NMAX))

def weyl_point(Hblk, s):
    # node block 2x2: mu + beta.sigma ; H0_s(q)=sum (-1)^{s_j} q_j sigma_j -> zero at q_j = -(-1)^{s_j} beta_j
    beta = np.array([0.5*np.real(np.trace(og.PAU[j] @ Hblk)) for j in range(3)])
    mu = 0.5*np.real(np.trace(Hblk))
    return np.array([-((-1)**s[j]) * beta[j] for j in range(3)]), mu

def pair_gap(fs, eps, s, sp):
    H = Hfull(fs, eps)
    idx = [2*NID[s], 2*NID[s]+1, 2*NID[sp], 2*NID[sp]+1]
    Hp = H[np.ix_(idx, idx)]
    def g(q):
        Hq = og.H0(q)[np.ix_(idx, idx)] + Hp
        e = np.linalg.eigvalsh(Hq); return (e[2] - e[1]) / 2
    sc = max(eps**2, 1e-12)
    best = g(np.zeros(3))
    starts = [np.zeros(3)] + [rng0.normal(size=3) * sc for _ in range(12)]
    for x0 in starts:
        r = minimize(g, x0, method='Nelder-Mead', options=dict(xatol=1e-14, fatol=1e-16, maxiter=4000))
        best = min(best, r.fun)
    return best

def mid_gap(fs, eps, nlow):
    # full 16x16: min over q of the direct gap at the band centre (bands 7,8 0-based), as a diagnostic
    H = Hfull(fs, eps)
    def g(q):
        e = np.linalg.eigvalsh(og.H0(q) + H); return (e[8] - e[7]) / 2
    sc = eps**2; best = g(np.zeros(3))
    for x0 in [np.zeros(3)] + [rng0.normal(size=3) * sc for _ in range(12)]:
        r = minimize(g, x0, method='Nelder-Mead', options=dict(xatol=1e-14, fatol=1e-16, maxiter=4000))
        best = min(best, r.fun)
    return best

out = []
for ki, (key, mats) in enumerate(og.REPS.items()):
    lines = og.fixed_lines(mats)
    for li, (order, phi) in enumerate(lines):
        Hs = og.stab(mats, phi)
        tch = []
        for ti in range(8):
            gg = og.GID[(ti, og.oidx(np.eye(3, dtype=int)))]
            v = mats[gg] @ phi
            tch.append(1 if np.allclose(v, phi) else (-1 if np.allclose(v, -phi) else 0))
        cvec = None
        if all(x != 0 for x in tch):
            for c in NODES:
                if all(tch[ti] == (-1)**int(np.dot(c, og.TR[ti])) for ti in range(8)): cvec = c
        rng = np.random.default_rng(1000 * ki + 17 * li + 0)   # worker's seed sd=0
        fs = og.f_eval(og.generic_maps(mats, rng), mats, phi)
        fs = [f / np.linalg.norm(f) if np.linalg.norm(f) > 1e-10 else 0 * f for f in fs]
        od, sv = og.orders(fs)
        nm = sum(1 for x in od if np.isfinite(x))
        rk = fix_generic_rank(Hs, cvec if (cvec is not None and sum(cvec) % 2 == 1) else None)
        if cvec is not None and sum(cvec) % 2 == 0: rk_note = 'even-charge'
        else: rk_note = ''
        fin = sorted(set(int(round(x)) for x in od if np.isfinite(x)))
        line = f"{key[0]:>3} {key[1]:<4} dir{li:<2} c={cvec} orders={fin} n_sv_massive={nm} genericFixRank_RL={rk} {rk_note}"
        flag = '' if (rk == nm or rk_note) else '  <-- RANK MISMATCH'
        line += flag
        if 3 in fin:
            if cvec is not None:
                # identify pairs; per pair singular values and Weyl offsets at eps
                for s in NODES:
                    if og.CHI[NID[s]] < 0:
                        sp = tuple((a + b) % 2 for a, b in zip(s, cvec))
                        for eps in (0.02, 0.01):
                            H = Hfull(fs, eps)
                            Mb = H[2*NID[sp]:2*NID[sp]+2, 2*NID[s]:2*NID[s]+2]
                            m = np.linalg.svd(Mb, compute_uv=False)
                            qL, muL = weyl_point(H[2*NID[s]:2*NID[s]+2, 2*NID[s]:2*NID[s]+2], s)
                            qR, muR = weyl_point(H[2*NID[sp]:2*NID[sp]+2, 2*NID[sp]:2*NID[sp]+2], sp)
                            gap = pair_gap(fs, eps, s, sp)
                            line += (f"\n      pair {s}-{sp} eps={eps}: sv={np.array2string(m, precision=3)} |Delta|/2={np.linalg.norm(qL-qR)/2:.3e}"
                                     f" dmu={muL-muR:.2e} true_min_gap={gap:.3e}")
            else:
                for eps in (0.02, 0.01):
                    line += f"\n      multi-charge eps={eps}: smallest sv={sv[-1] if False else np.sort(og.masses(fs, eps))[0]:.3e} mid_gap={mid_gap(fs, eps, 0):.3e}"
                    # node-diagonal axial parts at this eps
                    H = Hfull(fs, eps)
                    offs = [np.linalg.norm(weyl_point(H[2*i:2*i+2, 2*i:2*i+2], s)[0]) for i, s in enumerate(NODES)]
                    line += f" max|weyl offset|={max(offs):.3e}"
        print(line); sys.stdout.flush()

# (3) subgroup completeness spot check: random 3-generator subgroups of Gamma
print("\nsubgroup completeness: random 3-generator subgroups")
newlines = 0
for key, mats in og.REPS.items():
    known = [phi for _, phi in og.fixed_lines(mats)]
    MA = np.array(mats)
    for _ in range(150):
        gens = rng0.integers(NG, size=3)
        Hc = og.closure(list(gens))
        P = MA[list(Hc)].mean(axis=0); w, v = np.linalg.eigh((P + P.T) / 2)
        if np.sum(w > 0.5) == 1:
            phi = v[:, np.argmax(w)]
            imgs = MA @ phi
            if not any(np.max(np.abs(imgs @ psi)) > 1 - 1e-8 for psi in known):
                newlines += 1; print("  NEW fixed line not in worker list:", key)
print("new lines found:", newlines)
