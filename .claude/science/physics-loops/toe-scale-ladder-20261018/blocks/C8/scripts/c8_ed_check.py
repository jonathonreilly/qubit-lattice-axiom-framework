#!/usr/bin/env python3
"""C8 independent check of the second-order response formula (different implementation path).

On a periodic L^3 lattice, with q = 2 pi/L along z, the perturbed generator H_a + lambda (O_q + O_q^dag)
couples momenta along chains k, k+q, ..., k+(L-1)q. Each chain is a 4L x 4L Hermitian matrix,
diagonalised exactly; the Dirac-sea energy E(lambda) = sum of negative eigenvalues. The lambda^2
coefficient [E(l)+E(-l)-2E(0)]/(2 l^2) (Richardson in l) is compared with the closed-form
Clifford-trace formula of c8_core summed on the same k grid.

Independent pieces: H(k) here is i*Log of the explicit 4x4 matrix M U0 M (eigendecomposition),
not the Clifford-vector formula -rho x.Gamma; vertices are explicit matrices (M4 uses a
finite-difference derivative of the matrix log); the response is exact diagonalisation, not
perturbation theory. Shared: the walk coefficients F (imported premise) and the vertex definitions.
"""
from __future__ import annotations

import sys
import functools
import itertools

import numpy as np
from scipy.linalg import expm

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import c8_core as cc

print = functools.partial(print, flush=True)
PASS = FAIL = 0


def check(name, ok):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"{'PASS' if ok else 'FAIL'} [numerical] {name}")


I2 = np.eye(2); t1 = np.array([[0, 1], [1, 0]], complex); t2 = np.array([[0, -1j], [1j, 0]]); t3 = np.diag([1.0, -1]).astype(complex)
TAU = [np.kron(t1, I2), np.kron(t2, I2)]
ALPHA = [-np.kron(t3, x) for x in (t1, t2, t3)]


def Umat(W, k):
    c = np.cos(k); sn = np.sin(k)
    ph = np.array([1.0, c.sum(), c[0]*c[1] + c[0]*c[2] + c[1]*c[2], c.prod()])
    f, h1, h2 = W.F @ ph
    b0, b1, b2 = W.b
    g = [sn[i]*(b0 + b1*(c[(i+1) % 3] + c[(i+2) % 3]) + b2*c[(i+1) % 3]*c[(i+2) % 3]) for i in range(3)]
    U0 = f*np.eye(4) + 1j*(h1*TAU[0] + h2*TAU[1]) - 1j*sum(g[i]*ALPHA[i] for i in range(3))
    M = expm(0.5j*W.theta*(np.cos(W.chi)*TAU[0] + np.sin(W.chi)*TAU[1]))
    return M @ U0 @ M, np.array(g)


def Hmat(W, k):
    U, _ = Umat(W, k)
    lam, V = np.linalg.eig(U)
    return 1j*(V @ np.diag(np.log(lam/np.abs(lam))) @ np.linalg.inv(V))


def Omat(W, coupling, eps, km, ka, kb):
    if coupling in ('M1', 'M2'):
        U, g = Umat(W, km)
        f = np.real(np.trace(U))/4
        rho = np.arccos(f)/np.sqrt(1 - f*f) if coupling == 'M1' else 1.0
        P = rho*g
        return -0.5*sum(eps[i, j]*ALPHA[i]*P[j] for i in range(3) for j in range(3))
    if coupling == 'M4':
        d = 1e-5; E = np.eye(3)
        dH = [(Hmat(W, km + d*E[i]) - Hmat(W, km - d*E[i]))/(2*d) for i in range(3)]
        return -0.5*sum(eps[i, j]*np.sin(km[j])*dH[i] for i in range(3) for j in range(3))
    if coupling == 'L2':
        return 0.5*(Hmat(W, ka) + Hmat(W, kb))
    raise ValueError


def chain_energy(Hs, Os, lam):
    L = len(Hs)
    A = np.zeros((4*L, 4*L), complex)
    for j in range(L):
        A[4*j:4*j+4, 4*j:4*j+4] = Hs[j]
        jp = (j + 1) % L
        A[4*jp:4*jp+4, 4*j:4*j+4] += lam*Os[j]
        A[4*j:4*j+4, 4*jp:4*jp+4] += lam*Os[j].conj().T
    A = 0.5*(A + A.conj().T)
    ev = np.linalg.eigvalsh(A)
    return ev[ev < 0].sum()


def ed_vs_formula(W, coupling, pol, L):
    qh, eps = cc.tt_eps('z', pol)
    q = 2*np.pi/L
    grid = 2*np.pi*np.arange(L)/L
    lams = (2e-3, 1e-3)
    tot = {l: 0.0 for l in lams}
    pert = 0.0
    for kx, ky in itertools.product(grid, grid):
        ks = [np.array([kx, ky, kz]) for kz in grid]
        Hs = [Hmat(W, k) for k in ks]
        Os = [Omat(W, coupling, eps, k + 0.5*q*qh, k + q*qh, k) for k in ks]
        E0 = chain_energy(Hs, Os, 0.0)
        for l in lams:
            tot[l] += (chain_energy(Hs, Os, l) + chain_energy(Hs, Os, -l) - 2*E0)/(2*l*l)
        km = np.array([k + 0.5*q*qh for k in ks])
        pert += -np.sum(cc.Fval(W, coupling, eps, qh, km, 0.5*q))
    ed = (4*tot[lams[1]] - tot[lams[0]])/3
    return ed, pert


print("ED (exact diagonalisation of k-chains) vs second-order Clifford-trace formula, same k grid")
for name, theta, chi in (('bstar', 0.3, np.pi/2), ('iso', 0.3, 0.0), ('gold', 0.4, np.pi/2)):
    W = cc.Walk(name, theta=theta, chi=chi)
    for coupling, pol in (('M1', 'A'), ('M1', 'B'), ('M2', 'B'), ('M4', 'A'), ('L2', 'A')):
        for L in (6,):
            ed, pt = ed_vs_formula(W, coupling, pol, L)
            rel = abs(ed - pt)/abs(pt)
            print(f"  {name} theta={theta} chi={chi:.2f} {coupling}{pol} L={L}: ED {ed:.12f}  formula {pt:.12f}  rel {rel:.1e}")
            check(f'{name} {coupling}{pol} L={L}: exact-diagonalisation lambda^2 coefficient = second-order formula (rel < 1e-6)', rel < 1e-6)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
