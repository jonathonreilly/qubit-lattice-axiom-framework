#!/usr/bin/env python3
"""Supplied single-particle convolution and ordered 2x2/4x4 block diagnostics.
Exact cubic averaging projection, finite covariance samples and point counterexamples; no physical chirality,
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


# Exact coordinates use the complex-linear Pauli basis (I, sigma_x, sigma_y,
# sigma_z). Rational basis inputs span the complex domain by complex linearity.
from fractions import Fraction
SITES = ((0, 0, 0), (1, 0, 0), (-1, 0, 0),
         (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def exact_rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        parity = (-1) ** sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
        for signs in itertools.product((-1, 1), repeat=3):
            if parity * signs[0] * signs[1] * signs[2] == 1:
                out.append(tuple(tuple(signs[i] if j == perm[i] else 0 for j in range(3)) for i in range(3)))
    return tuple(out)


def rotate_vector(R, v):
    return tuple(sum(R[i][j] * v[j] for j in range(3)) for i in range(3))


def coefficient_action(R, kernel):
    result = [None] * 7
    for g, coefficient in zip(SITES, kernel):
        h = rotate_vector(R, g)
        result[SITES.index(h)] = (coefficient[0], *rotate_vector(R, coefficient[1:]))
    return tuple(result)


def cubic_average(kernel):
    # Direct 24-term action; does not use the closed coefficient formula.
    images = [coefficient_action(R, kernel) for R in exact_rotations()]
    return tuple(tuple(sum(image[h][j] for image in images) * Fraction(1, 24)
                       for j in range(4)) for h in range(7))


def closed_projection(kernel, denominator=6, vector_sign=1):
    # Independent trace-coordinate formula. Optional wrong parameters are
    # negative controls only, never the definition of the projection.
    a = kernel[0][0]
    b = sum(row[0] for row in kernel[1:]) * Fraction(1, denominator)
    c = sum(sum(g[i] * row[i + 1] for i in range(3))
            for g, row in zip(SITES[1:], kernel[1:])) * Fraction(vector_sign, denominator)
    return ((a, 0, 0, 0),) + tuple((b, *(c * x for x in h)) for h in SITES[1:])


def exact_projection_checks():
    group = exact_rotations()
    product = lambda R, Q: tuple(tuple(sum(R[i][k] * Q[k][j] for k in range(3))
                                      for j in range(3)) for i in range(3))
    check('exact cubic rotations: 24 distinct signed integer matrices, closed under composition',
          len(group) == len(set(group)) == 24 and all(product(R, Q) in group for R in group for Q in group))
    basis = []
    for slot in range(7):
        for component in range(4):
            basis.append(tuple(tuple(int((h, j) == (slot, component)) for j in range(4)) for h in range(7)))
    averages = [cubic_average(kernel) for kernel in basis]
    check('exact group average equals trace-coordinate formula on all 28 complex-linear basis inputs',
          all(avg == closed_projection(kernel) for kernel, avg in zip(basis, averages)))
    check('exact covariance: all 24 actions fix each of the 28 averaged basis inputs',
          all(coefficient_action(R, avg) == avg for R in group for avg in averages))
    check('exact idempotence on all 28 basis inputs',
          all(cubic_average(avg) == avg for avg in averages))
    bad_normalization = sum(avg != closed_projection(kernel, denominator=5) for kernel, avg in zip(basis, averages))
    bad_sign = sum(avg != closed_projection(kernel, vector_sign=-1) for kernel, avg in zip(basis, averages))
    check('negative control: erroneous 1/5 neighbor normalization is rejected', bad_normalization > 0,
          f'{bad_normalization}/28 basis mismatches')
    check('negative control: reversed g dot v sign is rejected', bad_sign > 0,
          f'{bad_sign}/28 basis mismatches')
    # B_ez=I: exact coefficients give a normalized origin but zero at the
    # all-pi/2 corner. This output is covariant and explicitly nonunitary.
    output = cubic_average(basis[4 * SITES.index((0, 0, 1))])
    expected = ((0, 0, 0, 0),) + ((Fraction(1, 6), 0, 0, 0),) * 6
    origin = sum(row[0] for row in output)
    corner = sum(sp.exp(-sp.I * sp.pi * sum(h) / 2) * row[0] for h, row in zip(SITES, output))
    check('exact nonunitary output: B_ez=I gives I/6 on six neighbors, A(0)=I and A(pi/2,pi/2,pi/2)=0',
          output == expected and origin == 1 and sp.simplify(corner) == 0)


def main():
    exact_projection_checks()
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
