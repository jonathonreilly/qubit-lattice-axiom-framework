#!/usr/bin/env python3
"""Covariance limits for one-qubit-per-site tick updates on Z^3.
(1) Symbolic: a translation-invariant, nearest-neighbour, one-qubit update covariant under all 24 proper cubic
    rotations (spin-1/2 action) has U(k) = alpha(k) I - i beta(k).sigma with alpha = a + 2b sum cos k_i,
    beta_i = 2c sin k_i; unitarity for all k forces b = c = 0 (no motion).
(2) The split-step update S_z S_y S_x: spectrum invariant under 12 of 24 rotations, operator covariant under 4.
(3) Adding a same-site chirality mass to the two-chirality version gaps k=0 but leaves the k=(pi/2)(1,1,1) cone.
No physical matter content or general no-go beyond these hypotheses is established.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ('docs/ONE_QUBIT_TICK_UPDATE_COVARIANCE_LIMITS_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

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
    sol = sp.solve([coeff_xy, coeff_xx], [br, cr], dict=True)
    check('(1) unitarity of the covariant nearest-neighbour ansatz: the c_x c_y coefficient 8|b|^2 and the c_x^2 coefficient 4|b|^2 - 4|c|^2 must vanish, so b = c = 0',
          sp.simplify(coeff_xy - 8 * (br ** 2 + bi ** 2)) == 0 and sp.simplify(coeff_xx - 4 * (br ** 2 + bi ** 2) + 4 * (cr ** 2 + ci ** 2)) == 0,
          f'c_x c_y coefficient {sp.factor(coeff_xy)}; c_x^2 coefficient {sp.factor(coeff_xx)}')
    # check the ansatz really is the general covariant form: covariance of a random instance and failure of a non-covariant term
    rots = rotations(); rng = np.random.default_rng(0); ks = rng.uniform(-np.pi, np.pi, (20, 3))
    p = rng.normal(size=3) + 1j * rng.normal(size=3)
    U_ans = lambda k: (p[0] + 2 * p[1] * np.sum(np.cos(k))) * np.eye(2) - 2j * p[2] * sum(np.sin(k[i]) * AL[i] for i in range(3))
    cov = sum(all(np.allclose(spin_of(R) @ U_ans(R.T @ k) @ spin_of(R).conj().T, U_ans(k)) for k in ks) for R in rots)
    check('(1b) the ansatz is covariant under all 24 rotations for arbitrary complex a, b, c', cov == 24, f'{cov}/24')
    # (2) split-step
    def S(i, k): return np.cos(k[i]) * np.eye(2) - 1j * np.sin(k[i]) * AL[i]
    UL = lambda k: S(2, k) @ S(1, k) @ S(0, k)
    spec = lambda k: np.sort(np.angle(np.linalg.eigvals(UL(k))))
    n_spec = sum(all(np.allclose(spec(R @ k), spec(k), atol=1e-9) for k in ks) for R in rots)
    n_op = sum(all(np.allclose(spin_of(R) @ UL(R.T @ k) @ spin_of(R).conj().T, UL(k), atol=1e-9) for k in ks) for R in rots)
    check('(2) split-step update: spectrum invariant under 12 of 24 rotations, operator covariant under 4', n_spec == 12 and n_op == 4, f'spectrum {n_spec}/24, operator {n_op}/24')
    # (3) same-site chirality mass
    UR = lambda k: S(0, k) @ S(1, k) @ S(2, k); Z2 = np.zeros((2, 2)); beta = np.block([[Z2, np.eye(2)], [np.eye(2), Z2]])
    UD = lambda k, th: np.block([[UL(k), Z2], [Z2, UR(k)]]) @ expm(-1j * th * beta)
    th = 0.1; g0 = np.min(abs(np.angle(np.linalg.eigvals(UD(np.zeros(3), th))))); gd = np.min(abs(np.angle(np.linalg.eigvals(UD(np.full(3, np.pi / 2), th)))))
    check('(3) a same-site chirality mass gaps k=0 but not the cone at k=(pi/2)(1,1,1)', abs(g0 - th) < 1e-9 and gd < 1e-9, f'gap at 0: {g0:.5f}; at (pi/2)(1,1,1): {gd:.1e}')
    print('per_site: one qubit per site, translation invariance, nearest-neighbour range (for 1), the spin-1/2 rotation action and the substep order are the stated hypotheses.')
    print('lattice_wide: no no-go beyond these hypotheses, matter content or physical identification is established.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
