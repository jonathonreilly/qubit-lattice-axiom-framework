#!/usr/bin/env python3
"""Supplied single-particle convolution and ordered 2x2/4x4 block diagnostics.
Finite covariance samples and exact point counterexamples; no physical chirality,
physical mass, neighborhood gap or universal momentum-mixing necessity is claimed.
The original nearest-neighbor exclusion theorem is deferred separately.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ('docs/ONE_QUBIT_TICK_UPDATE_COVARIANCE_LIMITS_BOUNDED_THEOREM_NOTE_2026-10-21.md',)

import sys, os, signal, time, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'
if not __debug__: raise RuntimeError('Optimized Python is unsupported')
sys.stdout.reconfigure(line_buffering=True)
_STARTED = time.monotonic()
def _timeout(*args):
    raise TimeoutError('Owning 300-second aggregate cap exceeded; streamed diagnostics retained')
signal.signal(signal.SIGALRM, _timeout)
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np, sympy as sp
from scipy.linalg import expm

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.diag([1., -1]).astype(complex); AL = [SX, SY, SZ]


def rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            R = np.zeros((3, 3))
            for i in range(3): R[i, perm[i]] = sg[i]
            if np.isclose(np.linalg.det(R), 1): out.append(R)
    return out


def spin_of(R):
    ang = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if np.isclose(ang, 0): return np.eye(2)
    w, vecs = np.linalg.eig(R); ax = np.real(vecs[:, np.argmin(abs(w - 1))]); ax /= np.linalg.norm(ax)
    for s in (1, -1):
        V = np.cos(ang / 2) * np.eye(2) - 1j * np.sin(ang / 2) * s * (ax[0] * SX + ax[1] * SY + ax[2] * SZ)
        if all(np.allclose(V @ AL[j] @ V.conj().T, sum(R[i, j] * AL[i] for i in range(3))) for j in range(3)): return V
    raise RuntimeError('no spin rotation')


def main():
    # (1) symbolic
    cx, cy, cz = sp.symbols('cx cy cz', real=True); ar, ai, br, bi, cr, ci = sp.symbols('ar ai br bi cr ci', real=True)
    a = ar + sp.I * ai; b = br + sp.I * bi; c = cr + sp.I * ci
    alpha = a + 2 * b * (cx + cy + cz); beta2 = 4 * (cr ** 2 + ci ** 2) * (3 - cx ** 2 - cy ** 2 - cz ** 2)
    norm = sp.expand(alpha * sp.conjugate(alpha) + beta2 - 1)
    poly = sp.Poly(norm, cx, cy, cz)
    coeff_xy = poly.coeff_monomial(cx * cy); coeff_xx = poly.coeff_monomial(cx ** 2)
    check('(1) supplied polynomial: mixed and diagonal quadratic coefficients match expansion',
          sp.simplify(coeff_xy - 8 * (br ** 2 + bi ** 2)) == 0 and sp.simplify(coeff_xx - 4 * (br ** 2 + bi ** 2) + 4 * (cr ** 2 + ci ** 2)) == 0,
          f'c_x c_y coefficient {sp.factor(coeff_xy)}; c_x^2 coefficient {sp.factor(coeff_xx)}')
    # Finite covariance check of one seeded complex coefficient instance, not a classification theorem.
    rots = rotations(); rng = np.random.default_rng(0); ks = rng.uniform(-np.pi, np.pi, (20, 3))
    p = rng.normal(size=3) + 1j * rng.normal(size=3)
    U_ans = lambda k: (p[0] + 2 * p[1] * np.sum(np.cos(k))) * np.eye(2) - 2j * p[2] * sum(np.sin(k[i]) * AL[i] for i in range(3))
    cov = sum(all(np.allclose(spin_of(R) @ U_ans(R.T @ k) @ spin_of(R).conj().T, U_ans(k)) for k in ks) for R in rots)
    check('(1b) supplied ansatz: seeded complex coefficients pass all 24 rotations at 20 momenta', cov == 24, f'{cov}/24')
    # (2) split-step
    def S(i, k): return np.cos(k[i]) * np.eye(2) - 1j * np.sin(k[i]) * AL[i]
    UL = lambda k: S(2, k) @ S(1, k) @ S(0, k)
    spec = lambda k: np.sort(np.angle(np.linalg.eigvals(UL(k))))
    n_spec = sum(all(np.allclose(spec(R @ k), spec(k), atol=1e-9) for k in ks) for R in rots)
    n_op = sum(all(np.allclose(spin_of(R) @ UL(R.T @ k) @ spin_of(R).conj().T, UL(k), atol=1e-9) for k in ks) for R in rots)
    check('(2) fixed sampled split-step comparisons: 12 spectral and 4 operator symmetries', n_spec == 12 and n_op == 4, f'spectrum {n_spec}/24, operator {n_op}/24')
    # (3) supplied same-site mixing of forward/reverse order blocks
    UR = lambda k: S(0, k) @ S(1, k) @ S(2, k); Z2 = np.zeros((2, 2)); beta = np.block([[Z2, np.eye(2)], [np.eye(2), Z2]])
    UD = lambda k, th: np.block([[UL(k), Z2], [Z2, UR(k)]]) @ expm(-1j * th * beta)
    th = 0.1; g0 = np.min(abs(np.angle(np.linalg.eigvals(UD(np.zeros(3), th))))); gd = np.min(abs(np.angle(np.linalg.eigvals(UD(np.full(3, np.pi / 2), th)))))
    check('(3) point eigenphase distances at theta=.1: origin .1 and corner zero', abs(g0 - th) < 1e-9 and gd < 1e-9, f'origin distance {g0:.5f}; corner distance {gd:.1e}')
    axis = UD(np.array([th,0.,0.]), th)
    axis_zero = np.min(abs(np.angle(np.linalg.eigvals(axis))))
    check('axis t=theta has an exact zero-phase eigenvalue for the supplied mixing',
          axis_zero < 1e-12, f'axis minimum eigenphase distance {axis_zero:.3e}')
    # Independent factorization: along this axis both order blocks are exp(-it sigma_x).
    axis_generator = np.kron(np.eye(2), SX)
    exact_axis = expm(-1j*th*axis_generator) @ expm(-1j*th*beta)
    check('axis factorization and commuting generators',
          np.linalg.norm(axis-exact_axis)<1e-12 and np.linalg.norm(axis_generator@beta-beta@axis_generator)<1e-12)
    delta = .23; corner = UD(np.full(3,np.pi/2),th)
    shifted = np.exp(-1j*delta)*corner
    shifted_dist = np.min(abs(np.angle(np.linalg.eigvals(shifted))))
    check('onsite scalar phase moves the corner zero without mixing momentum',
          abs(shifted_dist-delta)<1e-12 and np.linalg.norm(corner@corner-np.eye(4))<1e-12,
          f'corner distance after scalar phase {shifted_dist:.5f}; pointwise only')
    h=1e-5
    derivs=[]
    for block in (UL,UR):
        derivs.append(np.column_stack([np.array([np.trace(s @ (1j*(block(h*e)-block(-h*e))/(2*h))).real/2 for s in AL]) for e in np.eye(3)]))
    check('forward and reverse blocks have the same origin derivative determinant sign',
          all(np.linalg.det(d)>0 for d in derivs) and all(np.allclose(d,np.eye(3),atol=1e-9) for d in derivs))
    k=np.array([.2,.3,.4]); quarter_order=S(2,k)@S(0,k)@S(1,k)
    check('quarter-turn factor order matches reverse trace but not reverse matrix at a generic point',
          abs(np.trace(quarter_order)-np.trace(UR(k)))<1e-12 and np.linalg.norm(quarter_order-UR(k))>1e-3)
    print('per_element: supplied polynomial coefficients are expanded symbolically; no general exclusion is concluded.')
    print('per_site: the supplied linear single-particle carrier and spin action are choices, not framework record dynamics.')
    print('per_mode: covariance is sampled at 20 momenta; axis/corner/scalar-shift identities have explicit point controls.')
    print('per_block: forward/reverse 2x2 blocks and one 4x4 mixing are checked; a physical mass class is not classified.')
    print('lattice_wide: checked and not executed — no many-body realization, global gap proof or universal mass prescription is supplied.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
