#!/usr/bin/env python3
"""Check for Lemma L9a (PROOF.md): reflection positivity of the Wilson action.
Part 1: exact enumeration, Z2 gauge theory on a 4 (time) x 2 (space) periodic lattice (16 links, 2^16 configurations),
        link reflection t -> 1 - t and site reflection t -> -t. RP matrix M_ij = <theta(F_i) F_j>, F_i = indicators of
        the positive-half link configurations; PSD for beta >= 0. (beta < 0 is NOT a usable control for Z2: observed PSD too, presumably via a pi-flux relabelling [not proven here];
        the control is a non-RP crossing term F_x theta(F_{x+1}).)
Part 2: the load-bearing SU(N) step of the Osterwalder-Seiler argument: the kernel K(W, V) = exp(beta Re tr(W V^dag))
        on SU(N) is positive definite for beta >= 0 (Schur product theorem), checked on random point sets; fails for beta < 0.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
import time, itertools as it, numpy as np
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0; rng = np.random.default_rng(1978)
def check(n, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))
Tt, Sx = 4, 2
lid = {}
for t in range(Tt):
    for x in range(Sx): lid[("s", t, x)] = len(lid); lid[("t", t, x)] = len(lid)
nl = len(lid); conf = ((np.arange(2 ** nl)[:, None] >> np.arange(nl)[None, :]) & 1) * -2 + 1  # +-1
def S_of(beta, bad=0.0, refl="link"):
    P = np.zeros(len(conf)); tm = 0 if refl == "link" else Tt - 1  # control: crossing term F_x theta(F_{x+1}), not of the form sum F theta F
    for x in range(Sx): P += (bad / beta) * conf[:, lid[("s", 1, x)]] * conf[:, lid[("s", tm, (x + 1) % Sx)]]
    for t in range(Tt):
        for x in range(Sx):
            P += conf[:, lid[("s", t, x)]] * conf[:, lid[("t", t, (x + 1) % Sx)]] * conf[:, lid[("s", (t + 1) % Tt, x)]] * conf[:, lid[("t", t, x)]]
    return -beta * P
def rp_matrix(beta, refl, bad=0.0):
    if refl == "link":  # t -> 1 - t; positive half t in {1, 2}
        pos = [("s", 1, x) for x in range(Sx)] + [("s", 2, x) for x in range(Sx)] + [("t", 1, x) for x in range(Sx)]
        th = lambda k: ("s", (1 - k[1]) % Tt, k[2]) if k[0] == "s" else ("t", (-k[1]) % Tt, k[2])
    else:  # site reflection t -> -t; positive half t in {0, 1, 2} (plane t = 0 and t = 2 fixed)
        pos = [("s", t, x) for t in (0, 1, 2) for x in range(Sx)] + [("t", t, x) for t in (0, 1) for x in range(Sx)]
        th = lambda k: ("s", (-k[1]) % Tt, k[2]) if k[0] == "s" else ("t", (-k[1] - 1) % Tt, k[2])
    pi = [lid[k] for k in pos]; ni = [lid[th(k)] for k in pos]
    w = np.exp(-S_of(beta, bad, refl)); w /= w.sum(); bits = 2 ** np.arange(len(pi))
    a = (conf[:, pi] < 0) @ bits; b = (conf[:, ni] < 0) @ bits; n = 2 ** len(pi)
    M = np.zeros((n, n)); np.add.at(M, (b, a), w); return M
for refl in ("link", "site"):
    ev = {beta: np.linalg.eigvalsh((lambda M: (M + M.T) / 2)(rp_matrix(beta, refl))) for beta in (0.3, 1.0)}
    ev[-0.5] = np.linalg.eigvalsh((lambda M: (M + M.T) / 2)(rp_matrix(0.3, refl, bad=1.0)))
    sym = max(np.abs(rp_matrix(b, refl) - rp_matrix(b, refl).T).max() for b in (0.3, 1.0))
    check(f"1 [{refl} reflection] Z2 Wilson action: RP matrix symmetric and PSD for beta = 0.3, 1.0; control (crossing term F_x theta F_x+1) not PSD",
          sym < 1e-14 and ev[0.3].min() > -1e-14 and ev[1.0].min() > -1e-14 and ev[-0.5].min() < -1e-6,
          f"min eig: {ev[0.3].min():.1e}, {ev[1.0].min():.1e}, control {ev[-0.5].min():.1e}; asym {sym:.0e}")
def haar(N, k):
    Z = (rng.normal(size=(k, N, N)) + 1j * rng.normal(size=(k, N, N))) / np.sqrt(2); Q, R = np.linalg.qr(Z)
    Q = Q * (np.diagonal(R, axis1=1, axis2=2) / abs(np.diagonal(R, axis1=1, axis2=2)))[:, None, :]
    return Q / np.linalg.det(Q)[:, None, None] ** (1 / N)
for N in (2, 3):
    W = haar(N, 60); G = np.real(np.einsum("iab,jab->ij", W, np.conj(W)))  # Re tr(W_i W_j^dag)
    mins = {b: np.linalg.eigvalsh(np.exp(b * G)).min() for b in (0.5, 2.0, 6.0, -1.0)}
    check(f"2 SU({N}) kernel exp(beta Re tr W V^dag) PSD on 60 Haar points for beta = .5, 2, 6; control beta = -1 not PSD",
          min(mins[b] for b in (0.5, 2.0, 6.0)) > -1e-9 and mins[-1.0] < -1e-6, ", ".join(f"beta {b}: {m:.1e}" for b, m in mins.items()))
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
