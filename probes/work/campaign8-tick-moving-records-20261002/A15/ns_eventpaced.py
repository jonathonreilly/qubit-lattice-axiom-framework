#!/usr/bin/env python3
"""A15 task 3: no-signalling of event-paced beats (supplied 4-qubit toy, exact linear algebra).
Qubits: b (distant), a1, a2, a3. Random joint pure possibility (seeded).
Distant condition at b: no record / record with menu Z / record with menu X (b's content averaged out).
Local event-paced step: a1 may form a record with linear chance tr(F rho), F = diag(0.3, 0.8) (A9 Thm 1),
instrument E_k = sqrt(F) P_k sqrt(F), no-record branch sqrt(1-F) (A9 Thm 2c). The beat: if a1 formed, the
pair gate exp(-i th SWAP) acts on (a2, a3), else not. Then a3 forms a record with menu Z.
Rules compared:
  REC  : gate controlled by a1's RECORD (event-paced by records)            -> must not signal
  POSS : gate fires iff the uncut possibility at a1 has weight(1) > 1/2       -> nonlinear pacing
  ANGLE: gate angle = th * weight(1) at a1 (pace set by possibilities)       -> nonlinear pacing
Reported: max total-variation distance of the local record statistics between distant conditions."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np
from scipy.linalg import expm

I2 = np.eye(2); X = np.array([[0, 1], [1, 0]]); Z = np.diag([1.0, -1.0])
SW = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], complex)
def kron(*ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out
def on(op, site, n=4):      # single-site operator
    ops = [I2] * n; ops[site] = op; return kron(*ops)
def pair(op4, i, n=4):      # two-site operator on adjacent (i, i+1)
    return kron(*([I2] * i), op4, *([I2] * (n - i - 2)))
P = [np.diag([1.0, 0.0]), np.diag([0.0, 1.0])]
Hx = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
PX = [Hx @ p @ Hx for p in P]
F = np.diag([0.3, 0.8]); sF = np.sqrt(F); s1F = np.sqrt(np.eye(2) - F)

def local_stats(rho, rule, th):
    """joint odds of (a1 formed?, a1 content, a3 content) given the snapshot rho on all 4 qubits."""
    out = {}
    # uncut possibility at a1 before this tick's formation (used only by the nonlinear rules)
    R = rho.reshape(2, 2, 4, 2, 2, 4)          # (b, a1, a2a3) x (b, a1, a2a3)
    ra1 = np.einsum('xiyxjy->ij', R)
    p1 = float(np.real(ra1[1, 1]))
    branches = [(('none', None), on(s1F, 1))] + [(('form', k), on(sF @ P[k] @ sF, 1)) for k in (0, 1)]
    for key, K in branches:
        r1 = K @ rho @ K.conj().T
        if rule == 'REC':
            fire, ang = key[0] == 'form', th
        elif rule == 'POSS':
            fire, ang = p1 > 0.5, th
        else:
            fire, ang = True, th * p1
        if fire:
            G = pair(expm(-1j * ang * SW), 2)
            r1 = G @ r1 @ G.conj().T
        for m in (0, 1):
            M = on(P[m], 3)
            out[(key, m)] = out.get((key, m), 0.0) + float(np.real(np.trace(M @ r1 @ M)))
    return out

def distant(rho, cond):
    if cond == 'none':
        return [rho]
    proj = P if cond == 'Z' else PX
    return [on(proj[k], 0) @ rho @ on(proj[k], 0) for k in (0, 1)]   # unnormalized branches

rng = np.random.default_rng(20261002)
worst = {'REC': 0.0, 'POSS': 0.0, 'ANGLE': 0.0}
for trial in range(200):
    v = rng.normal(size=16) + 1j * rng.normal(size=16); v /= np.linalg.norm(v)
    rho = np.outer(v, v.conj())
    th = rng.uniform(0.2, 1.4)
    for rule in worst:
        stats = {}
        for cond in ('none', 'Z', 'X'):
            agg = {}
            for br in distant(rho, cond):
                w = np.real(np.trace(br))
                st = local_stats(br / w, rule, th)
                for k2, val in st.items():
                    agg[k2] = agg.get(k2, 0.0) + w * val
            stats[cond] = agg
        keys = set().union(*[set(s) for s in stats.values()])
        for c1 in ('Z', 'X'):
            tv = 0.5 * sum(abs(stats[c1].get(k, 0) - stats['none'].get(k, 0)) for k in keys)
            worst[rule] = max(worst[rule], tv)
for rule, tv in worst.items():
    print("rule %-5s: max TV of local record odds between distant conditions over 200 random snapshots = %.3e" % (rule, tv))
