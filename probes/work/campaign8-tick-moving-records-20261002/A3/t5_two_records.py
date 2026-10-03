"""Check 5: several records (hard-core: one qubit per site), brickwork ticks on a ring N=8.

Configuration-level rules (the record configuration C is an n-subset of sites):
  MIN-MH : pi_MH(C,C') = Re[Psi'(C')^* U(C',C) Psi(C)],  J = pi - pi^T,  T = J^+/P
           (validity requires the outflow bound; configuration space has loops)
  L1     : LP coupling on one-step-reachable pairs minimising the probability of any move
  SEQ    : settle the active bonds one at a time (their gates commute); each sub-step is a
           matching on configurations, so its minimal rule is forced and always valid;
           SEQ-AVG averages over all bond orders (a convex mix of valid equivariant rules).
Local rule (fails): each active bond moves its single record with that bond's own
  marginal odds, independently of other bonds.
Plus the analytic two-bond example: no rule built from P_t and bond marginals can work.
"""
import itertools
import numpy as np
from common import haar_unitary, mh_split, rule_from_flow, rule_from_coupling, lp_coupling, tv, \
    mc_trajectories, chi2_check
from manybody import sector, gate_full, nc_two_site, configs_of, one_step_reachable

N, n, TICKS, M = 8, 2, 30, 200_000
rng = np.random.default_rng(99)
bondsA = [(0, 1), (2, 3), (4, 5), (6, 7)]
bondsB = [(1, 2), (3, 4), (5, 6), (7, 0)]
states = sector(N, n)
confs = configs_of(states, N)
nc = len(states)
reach = np.array([[one_step_reachable(C, Cp, N) for Cp in confs] for C in confs])


def layer_gates(bonds):
    gs = []
    for (a, b) in bonds:
        G = gate_full(N, [a, b], nc_two_site(haar_unitary(2, rng), 2 * np.pi * rng.random()))
        gs.append(G[np.ix_(states, states)])
    return gs


def bond_local_rule(P, Pn, bonds):
    rules = []
    for (a, b) in bonds:
        pa = sum(P[i] for i, C in enumerate(confs) if a in C and b not in C)
        pb = sum(P[i] for i, C in enumerate(confs) if b in C and a not in C)
        pan = sum(Pn[i] for i, C in enumerate(confs) if a in C and b not in C)
        f = pa - pan
        ta = max(f, 0) / pa if pa > 1e-15 else 0.0
        tb = max(-f, 0) / pb if pb > 1e-15 else 0.0
        rules.append((a, b, ta, tb))
    T = np.zeros((nc, nc))
    for i, C in enumerate(confs):
        for j, Cp in enumerate(confs):
            prob = 1.0
            for (a, b, ta, tb) in rules:
                ca = (a in C, b in C); cpa = (a in Cp, b in Cp)
                if ca == (True, False):
                    prob *= ta if cpa == (False, True) else (1 - ta) if cpa == (True, False) else 0.0
                elif ca == (False, True):
                    prob *= tb if cpa == (True, False) else (1 - tb) if cpa == (False, True) else 0.0
                else:
                    prob *= 1.0 if cpa == ca else 0.0
            T[i, j] = prob
    return T


def seq_rule(Psi, gates, order):
    T = np.eye(nc)
    psi = Psi.copy()
    worst = -1.0
    for k in order:
        P = np.abs(psi) ** 2
        piMH, K, psin = mh_split(gates[k], psi, nc, 1)
        Tk, ex = rule_from_flow(piMH - piMH.T, P)
        worst = max(worst, ex)
        T = T @ Tk
        psi = psin
    return T, worst


def run(Psi0, label):
    Psi = Psi0.copy()
    P = np.abs(Psi) ** 2
    keys = ('L1', 'SEQ', 'SEQ-AVG', 'BOND-LOCAL')
    Q = {k: P.copy() for k in keys}
    worst = {k: 0.0 for k in keys}
    n_bad_min, worst_ex_min, worst_ex_seq, order_spread, min_diag_seq = 0, -1.0, -1.0, 0.0, 1.0
    T_list, P_list = [], [P.copy()]
    for t in range(TICKS):
        bonds = bondsA if t % 2 == 0 else bondsB
        gates = layer_gates(bonds)
        U = np.eye(nc, dtype=complex)
        for G in gates:
            U = G @ U
        piMH, K, Psin = mh_split(U, Psi, nc, 1)
        Pn = np.abs(Psin) ** 2
        _, ex = rule_from_flow(piMH - piMH.T, P)
        worst_ex_min = max(worst_ex_min, ex)
        n_bad_min += ex > 1e-12
        ok, piL1, _ = lp_coupling(P, Pn, reach, 'moves')
        T_l1 = rule_from_coupling(piL1, P)
        T_seq, exs = seq_rule(Psi, gates, [0, 1, 2, 3])
        worst_ex_seq = max(worst_ex_seq, exs)
        Ts = []
        for order in itertools.permutations(range(4)):
            To, exo = seq_rule(Psi, gates, list(order))
            worst_ex_seq = max(worst_ex_seq, exo)
            Ts.append(To)
        T_avg = sum(Ts) / len(Ts)
        order_spread = max(order_spread, max(float(np.abs((P[:, None] * (Ta - Tb))).max())
                                             for Ta in Ts[:6] for Tb in Ts[-6:]))
        min_diag_seq = min(min_diag_seq, float(T_avg.min()))
        T_bl = bond_local_rule(P, Pn, bonds)
        for k, T in (('L1', T_l1), ('SEQ', T_seq), ('SEQ-AVG', T_avg), ('BOND-LOCAL', T_bl)):
            Q[k] = Q[k] @ T
            worst[k] = max(worst[k], tv(Q[k], Pn) if k == 'BOND-LOCAL' else float(np.abs(Q[k] - Pn).max()))
        T_list.append(T_avg)
        Psi, P = Psin, Pn
        P_list.append(P.copy())
    X0 = rng.choice(nc, size=M, p=P_list[0] / P_list[0].sum())
    hists = mc_trajectories(T_list, X0, rng)
    worst_tv_mc, worst_p = 0.0, 1.0
    for h, Pt in zip(hists, P_list):
        worst_tv_mc = max(worst_tv_mc, tv(h / M, Pt))
        stat, dof, p = chi2_check(h, Pt, M)
        if dof > 0:
            worst_p = min(worst_p, p)
    print(f"[{label}] configs={nc}, ticks={TICKS}")
    print(f"   simultaneous MIN-MH: ticks breaking the outflow bound = {n_bad_min}/{TICKS} "
          f"(largest excess {worst_ex_min:.3e})  -> not a valid rule on those ticks")
    print(f"   L1 (LP)   exact max|Q_t-P_t| = {worst['L1']:.1e}")
    print(f"   SEQ (fixed bond order) exact max|Q_t-P_t| = {worst['SEQ']:.1e}; sub-step outflow excess <= {worst_ex_seq:.1e}")
    print(f"   SEQ-AVG (all 24 orders) exact max|Q_t-P_t| = {worst['SEQ-AVG']:.1e}; min entry of T = {min_diag_seq:.2e}")
    print(f"   order dependence: max |pi_order - pi_order'| = {order_spread:.3e}")
    print(f"   SEQ-AVG Monte Carlo (M={M}): max TV = {worst_tv_mc:.4f}, min chi2 p over {TICKS+1} ticks = {worst_p:.3g}")
    print(f"   BOND-LOCAL (independent, bond-marginal odds): max TV(Q_t, P_t) = {worst['BOND-LOCAL']:.4f}")


if __name__ == '__main__':
    e = np.zeros(nc, complex); e[confs.index((0, 4))] = 1.0
    run(e, 'two records formed at sites 0 and 4 (product start)')
    v = rng.normal(size=nc) + 1j * rng.normal(size=nc); v /= np.linalg.norm(v)
    run(v, 'random linked (entangled) possibility state')

    print("[two-bond example] Psi = (|L,L> + e^{i phi}|R,R>)/sqrt2, Hadamard on each bond")
    Hd = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    UU = np.kron(Hd, Hd)                      # basis LL, LR, RL, RR
    for phi in (0.0, np.pi / 2):
        Psi = np.array([1, 0, 0, np.exp(1j * phi)]) / np.sqrt(2)
        Pn = np.abs(UU @ Psi) ** 2
        P = np.abs(Psi) ** 2
        m1 = np.array([P[0] + P[1], P[2] + P[3]]); m1n = np.array([Pn[0] + Pn[1], Pn[2] + Pn[3]])
        m2 = np.array([P[0] + P[2], P[1] + P[3]]); m2n = np.array([Pn[0] + Pn[2], Pn[1] + Pn[3]])
        print(f"   phi={phi:.3f}: P_t={np.round(P,3)}, P_t+1={np.round(Pn,3)}; "
              f"bond-1 odds {np.round(m1,3)}->{np.round(m1n,3)}, bond-2 odds {np.round(m2,3)}->{np.round(m2n,3)}")
