"""Check 2: two-component coin-shift walk on a ring (supplied Dirac-type model, d=2).

U = S (C x 1): coin C on each site, then up-part shifts right, down-part shifts left.
Every tick is strictly range 1, but the site graph is a ring (it has a cycle), so the
net flow is fixed by equivariance only up to a circulation.

Rules compared (all equivariant if feasible):
  MH      : T = pi_MH / P             (pi_MH >= 0 here; 'chirality-follows')
  MIN-MH  : T = J_MH^+ / P            (no counterflow, MH net flow)
  L1      : LP coupling minimising the probability of moving (circulation by L1)
They agree on single-tick record odds and differ in two-tick readable statistics.
Also: conveyor (pure shift) - MH rides it, L1 does not move.  Traced MH flow = index.
"""
import numpy as np
from common import (rand_state, site_probs, mh_split, rule_from_flow, rule_from_coupling,
                    lp_coupling, ring_allowed, tv)

N, TICKS = 8, 30
rng = np.random.default_rng(7)
allowed = ring_allowed(N)


def coin_shift(C):
    d = 2
    U = np.zeros((N * d, N * d), complex)
    for x in range(N):
        for t in range(d):
            for s in range(d):
                y = (x + 1) % N if s == 0 else (x - 1) % N
                U[y * d + s, x * d + t] += C[s, t]
    return U


def shift_only(d, direction=+1):
    U = np.zeros((N * d, N * d), complex)
    for x in range(N):
        for s in range(d):
            U[((x + direction) % N) * d + s, x * d + s] = 1.0
    return U


def traced_flow(U, d):
    """Sum over a basis of states of J_MH across bond (x, x+1): ||U_{x+1,x}||^2 - ||U_{x,x+1}||^2."""
    Ub = U.reshape(N, d, N, d)
    out = []
    for x in range(N):
        y = (x + 1) % N
        out.append(float(np.sum(np.abs(Ub[y, :, x, :]) ** 2) - np.sum(np.abs(Ub[x, :, y, :]) ** 2)))
    return np.array(out)


def stats(pi):
    """Probability of moving and mean signed displacement in one tick (ring, NN)."""
    move = sum(pi[x, y] for x in range(N) for y in range(N) if x != y)
    disp = sum(pi[x, (x + 1) % N] - pi[x, (x - 1) % N] for x in range(N))
    return move, disp


def run(U, d, psi0, label):
    psi = psi0.copy()
    P = site_probs(psi, N, d)
    Q = {'MH': P.copy(), 'MIN-MH': P.copy(), 'L1': P.copy()}
    worst = {k: 0.0 for k in Q}
    min_pi = 0.0
    excess = -1.0
    acc = {k: np.zeros(2) for k in Q}
    for t in range(TICKS):
        piMH, K, psin = mh_split(U, psi, N, d)
        Pn = site_probs(psin, N, d)
        min_pi = min(min_pi, float(piMH.min()))
        T_mh = rule_from_coupling(np.maximum(piMH, 0), P)
        T_min, ex = rule_from_flow(piMH - piMH.T, P)
        excess = max(excess, ex)
        ok, piL1, _ = lp_coupling(P, Pn, allowed, 'moves')
        T_l1 = rule_from_coupling(piL1, P)
        for k, T in (('MH', T_mh), ('MIN-MH', T_min), ('L1', T_l1)):
            Q[k] = Q[k] @ T
            worst[k] = max(worst[k], float(np.abs(Q[k] - Pn).max()))
            acc[k] += np.array(stats(P[:, None] * T))
        psi, P = psin, Pn
    print(f"[{label}]  min entry of pi_MH = {min_pi:.2e};  MIN-MH outflow excess = {excess:.2e}")
    for k in Q:
        mv, dp = acc[k] / TICKS
        print(f"   {k:7s}: max|Q_t-P_t| = {worst[k]:.1e};  mean P(move)/tick = {mv:.4f}; "
              f"mean signed displacement/tick = {dp:+.4f}")


if __name__ == '__main__':
    H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    U = coin_shift(H)
    e0 = np.zeros(N * 2, complex); e0[0] = 1 / np.sqrt(2); e0[1] = 1j / np.sqrt(2)
    run(U, 2, e0, 'Hadamard coin-shift, record formed at site 0, coin (1,i)/sqrt2')
    run(U, 2, rand_state(2 * N, rng), 'Hadamard coin-shift, random possibility state')
    th = 0.3
    Cth = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    run(coin_shift(Cth), 2, rand_state(2 * N, rng), 'rotation coin theta=0.3, random state')
    # Conveyor: d=1 shift with a plane wave (uniform odds)
    k = 2 * np.pi * 1 / N
    pw = np.exp(1j * k * np.arange(N)) / np.sqrt(N)
    run(shift_only(1, +1), 1, pw, 'd=1 conveyor (pure shift), uniform odds')
    run(shift_only(1, +1), 1, rand_state(N, rng), 'd=1 conveyor (pure shift), random state')
    # traced MH flow (sum over a basis) = index, same across every cut
    for lab, UU, d in (('coin-shift Hadamard', U, 2), ('d=1 right shift', shift_only(1, +1), 1),
                       ('d=2 right shift', shift_only(2, +1), 2)):
        tf = traced_flow(UU, d)
        # cross-check by summing J_MH over basis states
        tot = np.zeros(N)
        for i in range(N * d):
            e = np.zeros(N * d, complex); e[i] = 1
            piMH, _, _ = mh_split(UU, e, N, d)
            J = piMH - piMH.T
            tot += np.array([J[x, (x + 1) % N] for x in range(N)])
        print(f"[traced flow] {lab:20s}: HS formula per cut = {np.round(tf, 12)}; "
              f"basis sum of J_MH = {np.round(tot, 12)}")
