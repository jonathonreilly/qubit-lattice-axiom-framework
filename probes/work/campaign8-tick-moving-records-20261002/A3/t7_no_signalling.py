"""Check 7: no-signalling with moving records.

Two records far apart: A in bond (0,1), B in bond (4,5) of a ring; linked possibilities
Psi(a,b), a,b in {L,R}.  One tick: gate G_A^(s) on A's bond (setting s = 0/1 chosen at A),
gate G_B^(r) on B's bond.  Configuration index 2a+b.

(1) B's single-tick odds after the tick do not depend on s (EXACT; checked).
(2) For several equivariant rules, B's two-tick record statistics
        g(b, b') = Prob(B at b at tick t, B at b' at tick t+1)
    are compared across A's settings s.  A difference would let a reader of B's two
    successive positions learn A's setting.
(3) Joint LP: does ANY equivariant coupling exist, for all four setting pairs at once,
    whose two-tick statistics at B do not depend on s and at A do not depend on r?
"""
import itertools
import numpy as np
from scipy.optimize import linprog
from common import haar_unitary, rand_state, mh_split, rule_from_flow, lp_coupling

rng = np.random.default_rng(23)
ALL = np.ones((4, 4), bool)


def g_B(pi):
    g = np.zeros((2, 2))
    for a, b, a2, b2 in itertools.product(range(2), repeat=4):
        g[b, b2] += pi[2 * a + b, 2 * a2 + b2]
    return g


def g_A(pi):
    g = np.zeros((2, 2))
    for a, b, a2, b2 in itertools.product(range(2), repeat=4):
        g[a, a2] += pi[2 * a + b, 2 * a2 + b2]
    return g


def coupling_min(U, Psi):
    piMH, K, Psin = mh_split(U, Psi, 4, 1)
    P = np.abs(Psi) ** 2
    T, ex = rule_from_flow(piMH - piMH.T, P)
    return P[:, None] * T, ex, piMH


def coupling_seq(GA, GB, Psi, first):
    I2 = np.eye(2)
    steps = [np.kron(GA, I2), np.kron(I2, GB)]
    if first == 'B':
        steps = steps[::-1]
    psi = Psi.copy()
    T = np.eye(4)
    for S in steps:
        pi, ex, _ = coupling_min(S, psi)
        P = np.abs(psi) ** 2
        Tk = np.where(P[:, None] > 1e-15, pi / np.maximum(P[:, None], 1e-300), np.eye(4))
        T = T @ Tk
        psi = S @ psi
    return (np.abs(Psi) ** 2)[:, None] * T


def joint_ns_lp(Psi, GAs, GBs):
    """Feasibility of couplings pi^{sr} (s,r in {0,1}) with Born marginals and two-tick
    no-signalling in both directions."""
    P = np.abs(Psi) ** 2
    nv = 4 * 16
    A, b = [], []
    def var(s, r, i, j):
        return (2 * s + r) * 16 + 4 * i + j
    for s, r in itertools.product(range(2), repeat=2):
        Pn = np.abs(np.kron(GAs[s], GBs[r]) @ Psi) ** 2
        for i in range(4):
            row = np.zeros(nv); row[[var(s, r, i, j) for j in range(4)]] = 1; A.append(row); b.append(P[i])
        for j in range(3):
            row = np.zeros(nv); row[[var(s, r, i, j) for i in range(4)]] = 1; A.append(row); b.append(Pn[j])
    for r in range(2):            # B's two-tick statistics independent of s
        for bb, bb2 in itertools.product(range(2), repeat=2):
            row = np.zeros(nv)
            for a, a2 in itertools.product(range(2), repeat=2):
                row[var(0, r, 2 * a + bb, 2 * a2 + bb2)] += 1
                row[var(1, r, 2 * a + bb, 2 * a2 + bb2)] -= 1
            A.append(row); b.append(0.0)
    for s in range(2):            # A's two-tick statistics independent of r
        for aa, aa2 in itertools.product(range(2), repeat=2):
            row = np.zeros(nv)
            for bb, bb2 in itertools.product(range(2), repeat=2):
                row[var(s, 0, 2 * aa + bb, 2 * aa2 + bb2)] += 1
                row[var(s, 1, 2 * aa + bb, 2 * aa2 + bb2)] -= 1
            A.append(row); b.append(0.0)
    res = linprog(np.zeros(nv), A_eq=np.array(A), b_eq=np.array(b), bounds=(0, None), method='highs')
    return res.status == 0


trials = 400
stats = {k: [] for k in ('MIN-MH', 'L1', 'SEQ-A-first', 'SEQ-B-first', 'SEQ-AVG', 'MH-direct')}
marg_diff, cond_diff, n_mh_valid, n_min_valid, ns_feasible = 0.0, 0.0, 0, 0, 0
for tr in range(trials):
    Psi = rand_state(4, rng)
    GAs = [haar_unitary(2, rng), haar_unitary(2, rng)]
    GBs = [haar_unitary(2, rng), haar_unitary(2, rng)]
    GB = GBs[0]
    gs = {k: [] for k in stats}
    minvalid, mhvalid = True, True
    margs, conds = [], []
    for s in range(2):
        U = np.kron(GAs[s], GB)
        P = np.abs(Psi) ** 2
        Pn = np.abs(U @ Psi) ** 2
        margs.append(np.array([Pn[0] + Pn[2], Pn[1] + Pn[3]]))
        pimin, ex, piMH = coupling_min(U, Psi)
        minvalid &= ex <= 1e-12
        mhvalid &= piMH.min() >= -1e-12
        ok, piL1, _ = lp_coupling(P, Pn, ALL, 'moves')
        piA = coupling_seq(GAs[s], GB, Psi, 'A')
        piB = coupling_seq(GAs[s], GB, Psi, 'B')
        gs['MIN-MH'].append(g_B(pimin)); gs['L1'].append(g_B(piL1))
        gs['SEQ-A-first'].append(g_B(piA)); gs['SEQ-B-first'].append(g_B(piB))
        gs['SEQ-AVG'].append(g_B(0.5 * (piA + piB))); gs['MH-direct'].append(g_B(piMH))
        # B's conditional move odds given configuration (A at L, B at L) under SEQ-AVG
        piAVG = 0.5 * (piA + piB)
        conds.append(piAVG[0, 1] + piAVG[0, 3])
    marg_diff = max(marg_diff, float(np.abs(margs[0] - margs[1]).max()))
    cond_diff = max(cond_diff, abs(conds[0] - conds[1]) / max(np.abs(Psi[0]) ** 2, 1e-12))
    for k in stats:
        if k == 'MIN-MH' and not minvalid:
            continue
        if k == 'MH-direct' and not mhvalid:
            continue
        stats[k].append(float(np.abs(gs[k][0] - gs[k][1]).max()))
    n_min_valid += minvalid; n_mh_valid += mhvalid
    ns_feasible += joint_ns_lp(Psi, GAs, GBs)

print(f"{trials} random trials (linked Psi, random gates; two settings at A)")
print(f"  (1) max change of B's single-tick odds with A's setting          = {marg_diff:.1e}")
print(f"      max change of B's conditional move odds (SEQ-AVG, from LL)    = {cond_diff:.3f}")
print("  (2) max change of B's two-tick statistics g(b,b') with A's setting:")
for k, v in stats.items():
    note = ''
    if k == 'MIN-MH':
        note = f'  (rule valid in {n_min_valid}/{trials} trials for both settings)'
    if k == 'MH-direct':
        note = f'  (pi_MH >= 0 in {n_mh_valid}/{trials} trials for both settings)'
    print(f"      {k:12s}: {max(v) if v else float('nan'):.3e}{note}")
print(f"  (3) trials where SOME equivariant coupling has two-tick no-signalling both ways: "
      f"{ns_feasible}/{trials}")
