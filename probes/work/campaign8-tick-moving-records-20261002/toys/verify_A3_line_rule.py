#!/usr/bin/env python3
"""Coordinator's independent check of A3 Step 7 (written from the statement, not from A3's code).
Claim: on a ring (N >= 5), for ANY strictly range-1 tick U with d components per site and ANY state psi,
the time-symmetric net flow J(x->y) = Re K(x,y) - Re K(y,x), K(x,y) = <psi'|P_y U P_x|psi>, psi' = U psi,
(i) obeys continuity P'(y) = P(y) + sum_x J(x->y), and (ii) satisfies the outflow bound sum_y J+(x->y) <= P(x),
so T(x->y) = J+(x->y)/P(x) is a consistent one-site move rule.
Ticks tested: random inhomogeneous coin-shift-coin walks (d=2) and random single brickwork layers (d=1, d=2)."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np
from scipy.stats import unitary_group

rng = np.random.default_rng(4242)


def coin_shift_coin(N, d=2):
    D = N * d
    C1 = np.zeros((D, D), complex); C2 = np.zeros((D, D), complex)
    for x in range(N):
        C1[x*d:(x+1)*d, x*d:(x+1)*d] = unitary_group.rvs(d, random_state=rng)
        C2[x*d:(x+1)*d, x*d:(x+1)*d] = unitary_group.rvs(d, random_state=rng)
    S = np.zeros((D, D), complex)
    for x in range(N):
        S[((x + 1) % N)*d + 0, x*d + 0] = 1      # component 0 moves right
        S[((x - 1) % N)*d + 1, x*d + 1] = 1      # component 1 moves left
    return C2 @ S @ C1


def brickwork(N, d, offset):
    D = N * d
    U = np.zeros((D, D), complex)
    for p in range(N // 2):
        a, b = (2 * p + offset) % N, (2 * p + 1 + offset) % N
        idx = [a*d + i for i in range(d)] + [b*d + i for i in range(d)]
        U[np.ix_(idx, idx)] = unitary_group.rvs(2 * d, random_state=rng)
    return U


def check(U, N, d, psi):
    P = np.array([np.linalg.norm(psi[x*d:(x+1)*d])**2 for x in range(N)])
    psi2 = U @ psi
    P2 = np.array([np.linalg.norm(psi2[x*d:(x+1)*d])**2 for x in range(N)])
    K = np.zeros((N, N), complex)
    for x in range(N):
        px = np.zeros_like(psi); px[x*d:(x+1)*d] = psi[x*d:(x+1)*d]
        v = U @ px
        for y in range(N):
            K[x, y] = np.vdot(psi2[y*d:(y+1)*d], v[y*d:(y+1)*d])
    J = K.real - K.real.T
    # range-1 support check
    for x in range(N):
        for y in range(N):
            if min((x - y) % N, (y - x) % N) > 1:
                assert abs(K[x, y]) < 1e-12, "tick is not range-1"
    cont = np.max(np.abs(P + J.sum(axis=0) - P2))
    out = np.array([np.clip(J[x], 0, None).sum() for x in range(N)])
    viol = np.max(out - P)
    return cont, viol


N = 8
worst_c, worst_v, nviol, ntot = 0.0, -1.0, 0, 0
for trial in range(800):
    kind = trial % 4
    if kind == 0:
        d = 2; U = coin_shift_coin(N, d)
    elif kind == 1:
        d = 1; U = brickwork(N, 1, trial % 2)
    elif kind == 2:
        d = 2; U = brickwork(N, 2, trial % 2)
    else:
        d = 3; U = brickwork(N, 3, trial % 2)
    psi = rng.normal(size=N*d) + 1j * rng.normal(size=N*d)
    if trial % 5 == 0:     # include the just-formed-record state (support on one site)
        psi = np.zeros(N*d, complex); psi[0:d] = rng.normal(size=d) + 1j * rng.normal(size=d)
    psi /= np.linalg.norm(psi)
    c, v = check(U, N, d, psi)
    worst_c = max(worst_c, c); worst_v = max(worst_v, v); ntot += 1
    nviol += v > 1e-12
print("ticks tested: %d (coin-shift-coin d=2; brickwork d=1,2,3), ring N=%d" % (ntot, N))
print("continuity error max = %.2e" % worst_c)
print("outflow bound: max(sum J+ - P) = %.3e ; violations (>1e-12): %d" % (worst_v, nviol))
