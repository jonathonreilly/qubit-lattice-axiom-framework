#!/usr/bin/env python3
"""A29 check: A25 S17 found the Wilson-type patch of the collocated spin-2 tick unstable (stepped tick, |eig| 1.41 at
r = 0.01). Is the patch also unstable in CONTINUOUS time (Option R), where there is no CFL or step at all?

Continuous time: omega^2 = eig(M (V_c + W)); stable iff every eigenvalue is real and >= 0.
V_c: collocated central-difference EH form (g = sin k).  W = r * sum_a (2 - 2 cos k_a)^2 on all 6 components
(A25's 'r*sum_a |Delta_a h|^2', Frobenius weights), and the traceless-only variant (no W on the trace).
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import itertools
import numpy as np

EPS3 = np.zeros((3, 3, 3))
for i, j, k in itertools.permutations(range(3)):
    EPS3[i, j, k] = np.linalg.det(np.eye(3)[[i, j, k]])
B = []
for i in range(3):
    E = np.zeros((3, 3)); E[i, i] = 1; B.append(E.ravel())
for i, j in ((0, 1), (0, 2), (1, 2)):
    E = np.zeros((3, 3)); E[i, j] = E[j, i] = 1 / np.sqrt(2); B.append(E.ravel())
B = np.array(B).T
M = B.T @ (2 * np.eye(9) - np.outer(np.eye(3).ravel(), np.eye(3).ravel())) @ B
tr = B.T @ np.eye(3).ravel(); tr /= np.linalg.norm(tr)
P_tl = np.eye(6) - np.outer(tr, tr)            # traceless projector in the orthonormal basis


def V_of(g):
    inc = -np.einsum('ikl,jmn,k,m->ijln', EPS3, EPS3, g, g).reshape(9, 9)
    return B.T @ (0.5 * inc) @ B


grid = np.linspace(-np.pi, np.pi, 17)
for r in (0.01, 0.05, 0.25):
    for label, Wproj in (("full", np.eye(6)), ("traceless-only", P_tl)):
        worst_neg, worst_im, where = 0.0, 0.0, None
        for k in itertools.product(grid, repeat=3):
            k = np.array(k)
            w = r * np.sum((2 - 2 * np.cos(k)) ** 2)
            lam = np.linalg.eigvals(M @ (V_of(np.sin(k)) + w * Wproj))
            neg = max(0.0, -lam.real.min()); im = np.abs(lam.imag).max()
            if neg > worst_neg:
                worst_neg, where = neg, np.round(k / np.pi, 3)
            worst_im = max(worst_im, im)
        rate = np.sqrt(worst_neg)
        print(f"r={r:<5} W {label:15s}: most negative omega^2 = {-worst_neg:.4f} at k/pi = {where}; "
              f"max |Im omega^2| = {worst_im:.2e}; growth rate sqrt = {rate:.3f} per unit time "
              f"(x{np.exp(rate * 0.5):.3f} per tau=0.5)")

print("\nTrue growth rate: max over k of |Im sqrt(lambda)| (complex omega^2 also grows)")
for r in (0.01, 0.05, 0.25):
    for label, Wproj in (("full", np.eye(6)), ("traceless-only", P_tl)):
        g_best, where = 0.0, None
        for k in itertools.product(grid, repeat=3):
            k = np.array(k)
            w = r * np.sum((2 - 2 * np.cos(k)) ** 2)
            lam = np.linalg.eigvals(M @ (V_of(np.sin(k)) + w * Wproj)).astype(complex)
            gr = np.abs(np.sqrt(lam).imag).max()
            if gr > g_best:
                g_best, where = gr, np.round(k / np.pi, 3)
        print(f"r={r:<5} W {label:15s}: max growth {g_best:.3f} per unit time at k/pi = {where} "
              f"(x{np.exp(g_best * 0.5):.3f} per tau=0.5)")
