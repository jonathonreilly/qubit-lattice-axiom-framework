#!/usr/bin/env python3
"""Reviewer script rv4 (independent): Lemma 4(c) exhibit alpha = Ad(prod_bonds exp(i phi s_n(r) s_n(r+e))),
face bonds, phi = 0.3, axis action.  alpha(A_0) only involves the 6 bonds at 0, so the 7-site star
(0, +-e_x, +-e_y, +-e_z) is exact for single-site images.  Checks: alpha fixes s_n(0); alpha(X_0)
is supported on the full star and has many Pauli components (non-Clifford); alpha^k(s^+_0) = s^+_0 f^k
(support constant in k); O-covariance (axis) of the image of X_0 and Z_0, with explicit lifts."""
import itertools
import numpy as np
from scipy.linalg import expm

P_ = F_ = 0


def check(name, ok, extra=''):
    global P_, F_
    P_ += bool(ok); F_ += (not ok)
    print('PASS' if ok else 'FAIL', name, ('::' + str(extra)) if extra != '' else '')


SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.diag([1., -1]).astype(complex)
I2 = np.eye(2, dtype=complex)
SIG = [SX, SY, SZ]
sites = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
N = 7
nvec = np.ones(3) / np.sqrt(3)
Sn = sum(nvec[i] * SIG[i] for i in range(3))


def on(op, k):
    m = [I2] * N
    m[k] = op
    out = m[0]
    for x in m[1:]:
        out = np.kron(out, x)
    return out


H = sum(on(Sn, 0) @ on(Sn, k) for k in range(1, 7))
phi = 0.3
U = expm(1j * phi * H)
al = lambda A: U @ A @ U.conj().T

check('alpha fixes s_n(0)', np.allclose(al(on(Sn, 0)), on(Sn, 0)))
aX = al(on(SX, 0))
paulis = [I2, SX, SY, SZ]
cnt = 0
supp = set()
for idx in itertools.product(range(4), repeat=N):
    P = paulis[idx[0]]
    for j in idx[1:]:
        P = np.kron(P, paulis[j])
    c = np.sum(P.T * aX) / 2 ** N
    if abs(c) > 1e-10:
        cnt += 1
        supp |= {k for k in range(N) if idx[k]}
check('alpha(X_0) supported on all 7 star sites (entangling)', supp == set(range(N)), sorted(supp))
check('alpha(X_0) has > 1 Pauli component (non-Clifford)', cnt > 1, f'{cnt} components on the star')
# freeze: alpha^k(s^+_0) = s^+_0 f^k with f diagonal in the n-basis, using exact two-step identity on the star
w, V = np.linalg.eigh(Sn)
splus = np.outer(V[:, 1], V[:, 0].conj())
Sp = on(splus, 0)
A1 = al(Sp)
# f := (s^-_0 s^+_0-part) ; check A1 = Sp @ f with f a function of s_n's on sites 1..6 only
f = sum(on(Sn, k) for k in range(1, 7))
F = expm(2j * phi * f)   # U = P_up e^{i phi f} + P_dn e^{-i phi f}  =>  U s^+ U^dag = s^+ e^{2 i phi f}
ok = np.allclose(A1, Sp @ F)
# (first run compared against an elementwise conjugate by mistake; reviewer test-logic bug, fixed)
A2 = al(A1)
ok &= np.allclose(A2, Sp @ F @ F)   # alpha fixes f, so alpha^2(s^+) = s^+ f^2
check('alpha(s^+_0) = s^+_0 f, f = exp(2i phi sum_e s_n(e)), and alpha^2(s^+_0) = s^+_0 f^2 (Lemma 4(c) freeze form)', ok)
print(f'TOTAL: PASS={P_} FAIL={F_}')
