"""Check 1: one record, one possibility per site (d=1), ring N=8, brickwork ticks.

Supplied model.  Each tick is ONE layer of nearest-neighbour 2x2 gates on disjoint bonds
(layer A on (0,1),(2,3),..., layer B on (1,2),...,(7,0)), alternating.  Each tick is
strictly range 1, so a record never needs to move more than one site.

Derived rule (minimal, flow-not-swap): on an active bond (a,b) with net flow
F = P_t(a) - P_{t+1}(a):  T(a->b) = F^+/P_t(a),  T(b->a) = F^-/P_t(b).
We check (i) J_MH equals that forced flow, (ii) exact equivariance of the record
distribution at every tick, (iii) Monte Carlo trajectories, (iv) counterexample rules.
"""
import numpy as np
from common import (haar_unitary, rand_state, site_probs, mh_split, rule_from_flow,
                    tv, mc_trajectories, chi2_check, ring_allowed, lp_coupling)

N, TICKS, M = 8, 40, 200_000
rng = np.random.default_rng(20261002)
bondsA = [(0, 1), (2, 3), (4, 5), (6, 7)]
bondsB = [(1, 2), (3, 4), (5, 6), (7, 0)]


def layer(bonds, gates):
    U = np.eye(N, dtype=complex)
    for (a, b), G in zip(bonds, gates):
        U[np.ix_([a, b], [a, b])] = G
    return U


def dirac_gate(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -1j * s], [-1j * s, c]])


def build_ticks(kind):
    Us = []
    for t in range(TICKS):
        bonds = bondsA if t % 2 == 0 else bondsB
        if kind == 'dirac':
            gates = [dirac_gate(np.pi / 4) for _ in bonds]
        else:
            gates = [haar_unitary(2, rng) for _ in bonds]
        Us.append((bonds, layer(bonds, gates)))
    return Us


def run(kind, psi0, label):
    ticks = build_ticks(kind)
    psi = psi0.copy()
    P = site_probs(psi, N, 1)
    Q_min = P.copy()
    Q_cx = {k: P.copy() for k in ('SYM', 'SYM_BOND', 'DECOH', 'LOCAL_BORN')}
    worst_eq, worst_flow_diff, worst_excess = 0.0, 0.0, -1.0
    worst_cx = {k: 0.0 for k in Q_cx}
    T_list, P_list = [], [P.copy()]
    for (bonds, U) in ticks:
        piMH, K, psin = mh_split(U, psi, N, 1)
        Pn = site_probs(psin, N, 1)
        J = piMH - piMH.T
        # forced flow on each active bond
        F = np.zeros((N, N))
        for (a, b) in bonds:
            f = P[a] - Pn[a]
            F[a, b], F[b, a] = f, -f
        worst_flow_diff = max(worst_flow_diff, float(np.abs(J - F).max()))
        T, excess = rule_from_flow(J, P)
        worst_excess = max(worst_excess, excess)
        T_list.append(T)
        Q_min = Q_min @ T
        worst_eq = max(worst_eq, float(np.abs(Q_min - Pn).max()))
        # --- counterexample rules (all local, all one-site moves) ---
        Tsym = np.zeros((N, N))
        for x in range(N):
            for dx in (-1, 0, 1):
                Tsym[x, (x + dx) % N] += 1 / 3
        Tsb = np.eye(N)
        for (a, b) in bonds:
            Tsb[a, a] = Tsb[b, b] = 0.5
            Tsb[a, b] = Tsb[b, a] = 0.5
        Tdec = np.abs(U.T) ** 2          # T[x,y] = |U[y,x]|^2 (re-formation odds, no re-cut)
        Tlb = np.zeros((N, N))
        for x in range(N):
            nb = [(x - 1) % N, x, (x + 1) % N]
            w = np.array([Pn[y] for y in nb])
            if w.sum() > 0:
                for y, wy in zip(nb, w):
                    Tlb[x, y] += wy / w.sum()
            else:
                Tlb[x, x] = 1
        for k, Tk in (('SYM', Tsym), ('SYM_BOND', Tsb), ('DECOH', Tdec), ('LOCAL_BORN', Tlb)):
            Q_cx[k] = Q_cx[k] @ Tk
            worst_cx[k] = max(worst_cx[k], tv(Q_cx[k], Pn))
        psi, P = psin, Pn
        P_list.append(P.copy())
    # Monte Carlo
    X0 = rng.choice(N, size=M, p=P_list[0] / P_list[0].sum())
    hists = mc_trajectories(T_list, X0, rng)
    worst_tv_mc, worst_p, worst_chi = 0.0, 1.0, 0.0
    for h, Pt in zip(hists, P_list):
        worst_tv_mc = max(worst_tv_mc, tv(h / M, Pt))
        stat, dof, p = chi2_check(h, Pt, M)
        if dof > 0:
            worst_p = min(worst_p, p)
            worst_chi = max(worst_chi, stat / dof)
    print(f"[{label}] ticks={TICKS} N={N}")
    print(f"   max|J_MH - forced flow|              = {worst_flow_diff:.2e}")
    print(f"   max outflow excess (<=0 feasible)     = {worst_excess:.2e}")
    print(f"   exact propagation max|Q_t - P_t|      = {worst_eq:.2e}")
    print(f"   MC (M={M}) max TV over ticks         = {worst_tv_mc:.4f};  "
          f"worst chi2/dof = {worst_chi:.2f}; min p = {worst_p:.3g} "
          f"(Bonferroni 0.001/{TICKS+1} = {0.001/(TICKS+1):.1e})")
    for k, v in worst_cx.items():
        print(f"   counterexample {k:11s}: max TV(Q_t, P_t) = {v:.4f}")
    return P_list


if __name__ == '__main__':
    e0 = np.zeros(N, complex); e0[0] = 1.0
    run('dirac', e0, 'Dirac-type brickwork theta=pi/4, record formed at site 0')
    run('random', e0, 'random-gate brickwork, record formed at site 0')
    run('random', rand_state(N, rng), 'random-gate brickwork, random possibility state')
    # L1-minimal coupling equals the derived rule on a tree tick (sanity)
    ticks = build_ticks('random')
    psi = rand_state(N, rng)
    worst = 0.0
    for (bonds, U) in ticks[:10]:
        P = site_probs(psi, N, 1)
        piMH, K, psin = mh_split(U, psi, N, 1)
        Pn = site_probs(psin, N, 1)
        allowed = np.eye(N, dtype=bool)
        for (a, b) in bonds:
            allowed[a, b] = allowed[b, a] = True
        ok, piL1, val = lp_coupling(P, Pn, allowed, 'moves')
        T, _ = rule_from_flow(piMH - piMH.T, P)
        piMin = P[:, None] * T
        worst = max(worst, float(np.abs(piMin - piL1).max()))
        psi = psin
    print(f"[tree tick] max|pi_min(J_MH^+) - pi_L1-minimal LP| over 10 ticks = {worst:.2e}")
