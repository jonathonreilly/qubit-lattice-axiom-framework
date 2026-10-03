#!/usr/bin/env python3
"""Coordinator's independent check of A25 (own code, from the report's statements).

Linearized spin-2 field in Fourier form on the staggered layout: every half-step difference has symbol i*s_k,
s_k = 2 sin(k_k/2). Potential V = 1/4 h:inc(h), inc(h)_ij = eps_ikl eps_jmn d_k d_m h_ln -> -eps eps s_k s_m h_ln.
Kinetic: hdot = M pi, (M pi)_ij = 2 pi_ij - delta_ij tr pi.  Tick K(tau/2) P(tau) K(tau/2): h += tau/2 M pi; pi -= tau dV/dh.
Claims checked:
 (1) exactly 4 non-unit eigenvalues of the tick at every k != 0 (2 polarizations), cos(theta) = 1 - tau^2 s^2/2;
 (2) power traces tr(T^n) = 8 + sum over the 4 (guards against Jordan-block splitting);
 (3) continuous time (Option R form, generator H = 1/2 pi M pi + V): omega^2 = eig(M Vmat) has exactly two
     nonzero values = s^2, all others 0 (no negative omega^2 from the conformal sector);
 (4) gauge invariance Vmat D = 0 and the constraint identity R M = -Div D^T;
 (5) collocated central differences (s_k = sin k_k): the potential vanishes at all 8 zone corners -> doublers.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import itertools
import numpy as np

EPS3 = np.zeros((3, 3, 3))
for i, j, k in itertools.permutations(range(3)):
    EPS3[i, j, k] = np.linalg.det(np.eye(3)[[i, j, k]])

# orthonormal basis of symmetric 3x3 matrices (6 of them), as 9-vectors
B = []
for i in range(3):
    E = np.zeros((3, 3)); E[i, i] = 1; B.append(E.ravel())
for i, j in ((0, 1), (0, 2), (1, 2)):
    E = np.zeros((3, 3)); E[i, j] = E[j, i] = 1 / np.sqrt(2); B.append(E.ravel())
B = np.array(B).T   # 9 x 6

def ops(s):
    inc = -np.einsum('ikl,jmn,k,m->ijln', EPS3, EPS3, s, s).reshape(9, 9)
    Vmat = B.T @ (0.5 * inc) @ B          # dV/dh with V = 1/4 h:inc h  (inc symmetric)
    Mfull = 2 * np.eye(9) - np.outer(np.eye(3).ravel(), np.eye(3).ravel())
    M = B.T @ Mfull @ B
    # gauge generator D xi = s_i xi_j + s_j xi_i (times i; drop the common factor), Hamiltonian row R h
    D = np.zeros((9, 3))
    for i in range(3):
        for j in range(3):
            D[3 * i + j, j] += s[i]; D[3 * i + j, i] += s[j]
    D = B.T @ D
    Rrow = (np.outer(s, s).ravel() - (s @ s) * np.eye(3).ravel()) @ B   # -(d_i d_j h_ij - d^2 tr h) up to sign
    return Vmat, M, D, Rrow

def tick(s, tau):
    Vmat, M, _, _ = ops(s)
    n = 6
    K = np.eye(2 * n); K[:n, n:] = (tau / 2) * M
    P = np.eye(2 * n); P[n:, :n] = -tau * Vmat
    return K @ P @ K

rng = np.random.default_rng(11)
tau = 0.5
worst_cos, worst_tr, counts = 0.0, 0.0, set()
worst_w2, worst_gauge, worst_row = 0.0, 0.0, 0.0
neg_w2 = 0
for trial in range(400):
    k = rng.uniform(-np.pi, np.pi, 3)
    if trial < 8:
        k = np.array([np.pi if b else 0.3 for b in np.binary_repr(trial, 3)], float)   # include zone-edge/corner points
    s = 2 * np.sin(k / 2); s2 = s @ s
    T = tick(s, tau)
    lam = np.linalg.eigvals(T)
    nonunit = lam[np.abs(lam - 1) > 1e-6]
    counts.add(len(nonunit))
    c = 1 - tau ** 2 * s2 / 2
    worst_cos = max(worst_cos, np.max(np.abs(nonunit.real - c)) if len(nonunit) else 0)
    # power traces: tr T^n = 8 + 4 * 2cos(n theta)/2 ... (two pairs e^{+-i theta})
    th = np.arccos(c)
    for npow in (1, 2, 3, 5):
        tr = np.trace(np.linalg.matrix_power(T, npow)).real
        worst_tr = max(worst_tr, abs(tr - (8 + 4 * np.cos(npow * th))))
    Vmat, M, D, Rrow = ops(s)
    w2 = np.sort(np.linalg.eigvals(M @ Vmat).real)
    neg_w2 += np.sum(w2 < -1e-10)
    worst_w2 = max(worst_w2, np.max(np.abs(w2 - np.array([0, 0, 0, 0, s2, s2]))))
    worst_gauge = max(worst_gauge, np.abs(Vmat @ D).max())
    # constraint propagation: R (M pi) = -Div(D^T pi): with D^T pi ~ 2 s_j pi_ij and Div ~ s_i -> check R M = c * s.D^T
    lhs = Rrow @ M
    rhs = s @ D.T
    ratio = np.linalg.lstsq(rhs[:, None], lhs, rcond=None)[0][0]
    worst_row = max(worst_row, np.abs(lhs - ratio * rhs).max())
print("(1) non-unit eigenvalue counts over 400 momenta (incl. zone edges/corner):", sorted(counts))
print("    max |Re(lambda) - (1 - tau^2 s^2/2)| = %.2e" % worst_cos)
print("(2) power-trace mismatch max = %.2e" % worst_tr)
print("(3) continuous-time omega^2 = eig(M V): max deviation from {0,0,0,0,s^2,s^2} = %.2e ; negative count %d" % (worst_w2, neg_w2))
print("(4) |V D| max = %.2e ; R M proportional to Div D^T: residual %.2e" % (worst_gauge, worst_row))
# (5) collocated central differences: symbol s_k = sin k ; corners
zs = []
for corner in itertools.product((0.0, np.pi), repeat=3):
    s = np.sin(np.array(corner))
    Vmat, _, _, _ = ops(s)
    zs.append(np.abs(Vmat).max())
print("(5) collocated central differences: max|V| at the 8 corners =", np.round(zs, 15))

# Robust spectrum check (eig of defective matrices splits Jordan blocks numerically): compare characteristic
# polynomials at random complex points.  Tick: det(z - T) = (z-1)^8 (z^2 - 2cz + 1)^2 ; generator: det(z - MV) = z^4 (z - s^2)^2
worst_T, worst_G = 0.0, 0.0
for trial in range(400):
    k = rng.uniform(-np.pi, np.pi, 3)
    if trial < 8:
        k = np.array([np.pi if b else 0.3 for b in np.binary_repr(trial, 3)], float)
    s = 2 * np.sin(k / 2); s2 = s @ s; c = 1 - tau ** 2 * s2 / 2
    T = tick(s, tau); Vmat, M, _, _ = ops(s)
    for z in rng.normal(size=3) + 1j * rng.normal(size=3):
        a = np.linalg.det(z * np.eye(12) - T); b = (z - 1) ** 8 * (z * z - 2 * c * z + 1) ** 2
        worst_T = max(worst_T, abs(a - b) / max(1.0, abs(b)))
        a = np.linalg.det(z * np.eye(6) - M @ Vmat); b = z ** 4 * (z - s2) ** 2
        worst_G = max(worst_G, abs(a - b) / max(1.0, abs(b)))
print("(1') char poly of the tick vs (z-1)^8 (z^2-2cz+1)^2: max rel. mismatch %.2e" % worst_T)
print("(3') char poly of M V vs z^4 (z-s^2)^2 (continuous time): max rel. mismatch %.2e" % worst_G)
