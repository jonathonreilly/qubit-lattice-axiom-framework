#!/usr/bin/env python3
"""Exact and numerical checks for the SU(3) Wilson plane-kernel theorem.

Paired note:
SU3_WILSON_PLANE_KERNEL_CHARACTER_POSITIVITY_AND_COMPOSED_GRAM_NARROW_THEOREM_NOTE_2026-07-09.md
"""

from __future__ import annotations

import itertools
import math
import os
import sys
from fractions import Fraction

import numpy as np


PASS = 0
FAIL = 0
N_SERIES = 26
BETA_VALUES = (0.15, 0.5, 1.0, 2.0)
RNG = np.random.default_rng(20260709)


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    if bool(cond):
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {name}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


# ---------------------------------------------------------------------------
# Exact Laurent-polynomial arithmetic.  Coefficients remain Python int objects.
# ---------------------------------------------------------------------------
def poly_clean(poly):
    return {tuple(k): int(v) for k, v in poly.items() if v}


def poly_add(a, b, scale_b=1):
    out = dict(a)
    for exponent, coefficient in b.items():
        out[exponent] = out.get(exponent, 0) + scale_b * coefficient
        if out[exponent] == 0:
            del out[exponent]
    return out


def poly_scale(a, scalar):
    return poly_clean({exponent: scalar * coefficient for exponent, coefficient in a.items()})


def poly_mul(a, b):
    if not a or not b:
        return {}
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            exponent = tuple(x + y for x, y in zip(ea, eb))
            out[exponent] = out.get(exponent, 0) + ca * cb
    return poly_clean(out)


def poly_conj(a):
    return {tuple(-x for x in exponent): coefficient for exponent, coefficient in a.items()}


def constant_term_sparse_dot(a, b):
    return sum(
        coefficient * b.get(tuple(-x for x in exponent), 0)
        for exponent, coefficient in a.items()
    )


def complete_homogeneous_su3(k: int):
    if k < 0:
        return {}
    out = {}
    for i in range(k + 1):
        for j in range(k - i + 1):
            ell = k - i - j
            exponent = (i - ell, j - ell)
            out[exponent] = out.get(exponent, 0) + 1
    return out


def permutation_sign(perm):
    inversions = sum(
        perm[i] > perm[j]
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def jacobi_trudi_su3(p: int, q: int, complete):
    a = p + q
    b = q
    indices = (
        (a, a + 1, a + 2),
        (b - 1, b, b + 1),
        (-2, -1, 0),
    )
    result = {}
    for perm in itertools.permutations(range(3)):
        term = {(0, 0): 1}
        for row in range(3):
            term = poly_mul(term, complete[indices[row][perm[row]]])
        result = poly_add(result, term, permutation_sign(perm))
    return result


def su3_dimension(label):
    p, q = label
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def tail_bound(beta: float, dimension: int, nmax: int = N_SERIES):
    x = dimension * beta
    assert x < nmax + 2
    return x ** (nmax + 1) / math.factorial(nmax + 1) / (1.0 - x / (nmax + 2))


def eval_laurent_su3(poly, theta1, theta2):
    out = np.zeros(np.broadcast(theta1, theta2).shape, dtype=np.complex128)
    for (m1, m2), coefficient in poly.items():
        out += coefficient * np.exp(1j * (m1 * theta1 + m2 * theta2))
    return out


def eval_laurent_su2(poly, theta):
    out = np.zeros(np.shape(theta), dtype=np.complex128)
    for (m,), coefficient in poly.items():
        out += coefficient * np.exp(1j * m * theta)
    return out


def exact_coefficient(multiplicities, label, beta: float, nmax=N_SERIES):
    b = Fraction(str(beta))
    value = Fraction(0, 1)
    for n in range(nmax + 1):
        value += Fraction(multiplicities[(label, n)], math.factorial(n)) * (b / 2) ** n
    return value


def build_part_a_data():
    section("Exact character positivity for SU(3)")

    chi3 = {(1, 0): 1, (0, 1): 1, (-1, -1): 1}
    chi3bar = {tuple(-x for x in exponent): coefficient for exponent, coefficient in chi3.items()}
    h = poly_add(chi3, chi3bar)
    h_powers = [{(0, 0): 1}]
    for _ in range(N_SERIES):
        h_powers.append(poly_mul(h_powers[-1], h))
    assert all(type(v) is int for power in h_powers for v in power.values())
    print(
        f"  Built h^n through n={N_SERIES}; terms(h^{N_SERIES})="
        f"{len(h_powers[-1])}, max coefficient={max(h_powers[-1].values())}"
    )

    complete = {k: complete_homogeneous_su3(k) for k in range(-2, 11)}
    labels8 = [(p, total - p) for total in range(9) for p in range(total + 1)]
    characters = {label: jacobi_trudi_su3(*label, complete) for label in labels8}

    z1 = {(1, 0): 1}
    z2 = {(0, 1): 1}
    z3 = {(-1, -1): 1}
    delta = poly_mul(poly_mul(poly_add(z1, z2, -1), poly_add(z1, z3, -1)), poly_add(z2, z3, -1))
    density = poly_mul(delta, poly_conj(delta))
    density_ct = density.get((0, 0), 0)
    check("Weyl-density normalization", density_ct == 6, f"CT[|Delta|^2]={density_ct}")

    dimension_failures = [
        (label, sum(characters[label].values()), su3_dimension(label))
        for label in labels8
        if sum(characters[label].values()) != su3_dimension(label)
    ]
    max_dim = max(su3_dimension(label) for label in labels8)
    check(
        "Jacobi-Trudi characters have the SU(3) dimensions",
        not dimension_failures,
        f"labels={len(labels8)}, max dimension={max_dim}, failures={len(dimension_failures)}",
    )

    char_density = {
        label: poly_mul(poly_conj(characters[label]), density) for label in labels8
    }
    orth_failures = 0
    worst_orth = 0
    for left in labels8:
        for right in labels8:
            numerator = constant_term_sparse_dot(characters[left], char_density[right])
            assert numerator % 6 == 0
            observed = numerator // 6
            expected = int(left == right)
            worst_orth = max(worst_orth, abs(observed - expected))
            orth_failures += observed != expected
    check(
        "Full pairwise character orthonormality",
        orth_failures == 0,
        f"pairs={len(labels8) ** 2}, failures={orth_failures}, max residual={worst_orth}",
    )

    multiplicities = {}
    for label in labels8:
        g_label = char_density[label]
        for n, power in enumerate(h_powers):
            numerator = constant_term_sparse_dot(power, g_label)
            assert numerator % 6 == 0
            value = numerator // 6
            assert value >= 0
            multiplicities[(label, n)] = value

    expected_n1 = {(1, 0): 1, (0, 1): 1}
    n1_bad = [
        (label, multiplicities[(label, 1)], expected_n1.get(label, 0))
        for label in labels8
        if multiplicities[(label, 1)] != expected_n1.get(label, 0)
    ]
    check("Multiplicity anchors at n=1", not n1_bad, f"failures={len(n1_bad)}")

    expected_n2 = {
        (0, 0): 2,
        (1, 1): 2,
        (1, 0): 1,
        (0, 1): 1,
        (2, 0): 1,
        (0, 2): 1,
    }
    n2_bad = [
        (label, multiplicities[(label, 2)], expected_n2.get(label, 0))
        for label in labels8
        if multiplicities[(label, 2)] != expected_n2.get(label, 0)
    ]
    n2_dim_sum = sum(
        multiplicities[(label, 2)] * su3_dimension(label) for label in labels8
    )
    check(
        "Multiplicity anchors at n=2",
        not n2_bad and n2_dim_sum == 36,
        f"failures={len(n2_bad)}, dimension sum={n2_dim_sum}",
    )

    dimension_residuals = []
    for n in range(9):
        observed = sum(
            multiplicities[(label, n)] * su3_dimension(label)
            for label in labels8
            if sum(label) <= n
        )
        dimension_residuals.append(observed - 6**n)
    check(
        "Exact dimension sums through n=8",
        all(x == 0 for x in dimension_residuals),
        f"max residual={max(map(abs, dimension_residuals))}",
    )

    labels4 = [label for label in labels8 if sum(label) <= 4]
    coefficient_exact = {}
    coefficient_float = {}
    ctilde2 = {}
    print("  Coefficient table c_lambda^(26)(beta):")
    for beta in BETA_VALUES:
        values = []
        for label in labels4:
            exact = exact_coefficient(multiplicities, label, beta)
            coefficient_exact[(label, beta)] = exact
            coefficient_float[(label, beta)] = float(exact)
            values.append(float(exact))
        print(
            f"    beta={beta:>4}: "
            + " ".join(f"({p},{q})={coefficient_float[((p, q), beta)]:.9e}" for p, q in labels4)
        )
        b = Fraction(str(beta))
        ctilde2[beta] = {
            label: float(
                sum(
                    Fraction(multiplicities[(label, n)], math.factorial(n)) * (b / 2) ** n
                    for n in range(3)
                )
            )
            for label in labels4
            if sum(label) <= 2
        }
    tail_2 = tail_bound(2.0, 3)
    check("Exponential-series tail", tail_2 < 1e-6, f"T(2,26)={tail_2:.6e}")

    angles = np.linspace(0.0, 2.0 * np.pi, 64, endpoint=False)
    theta1, theta2 = np.meshgrid(angles, angles, indexing="ij")
    density_grid = eval_laurent_su3(density, theta1, theta2)
    char_grids = {
        label: eval_laurent_su3(characters[label], theta1, theta2) for label in labels4
    }
    base_trace_real = np.cos(theta1) + np.cos(theta2) + np.cos(theta1 + theta2)
    max_quad_residual = 0.0
    max_quad_allowance = 0.0
    quad_failures = 0
    quadrature = {}
    for beta in BETA_VALUES:
        kernel_grid = np.exp(beta * base_trace_real)
        allowance = tail_bound(beta, 3) + 1e-9
        for label in labels4:
            extracted = np.mean(
                kernel_grid * np.conj(char_grids[label]) * density_grid / 6.0
            )
            quadrature[(label, beta)] = extracted
            residual = abs(extracted - coefficient_float[(label, beta)])
            max_quad_residual = max(max_quad_residual, residual)
            max_quad_allowance = max(max_quad_allowance, allowance)
            quad_failures += residual > allowance
    check(
        "Independent direct-exponential quadrature cross-extraction",
        quad_failures == 0,
        f"max residual={max_quad_residual:.3e}, max allowed={max_quad_allowance:.3e}, failures={quad_failures}",
    )

    beta_bad = 0.5
    c11 = coefficient_float[((1, 1), beta_bad)]
    subtraction = 2.0 * c11 + 1.0
    bad_kernel = np.exp(beta_bad * base_trace_real) - subtraction * char_grids[(1, 1)]
    bad_extracted = np.mean(
        bad_kernel * np.conj(char_grids[(1, 1)]) * density_grid / 6.0
    )
    check(
        "Wrong-kernel rejector detects a negative (1,1) coefficient",
        bad_extracted.real < -0.5,
        f"extracted={bad_extracted.real:+.9e}{bad_extracted.imag:+.2e}i, subtraction={subtraction:.9e}",
    )

    sys.dont_write_bytecode = True
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05 import (  # noqa: E501
        bessel_i_positive_series_interval,
    )

    max_ab = 0.0
    ab_failures = 0
    interval_failures = 0
    max_bessel_tail = 0.0
    for n in (0, 1, 2, 3):
        for beta in (0.15, 1.0, 2.0):
            mmax = 35
            kmax = n + 2 * mmax
            form_a = math.fsum(
                (beta / 2.0) ** k / math.factorial(k) * math.comb(k, (k + n) // 2)
                for k in range(kmax + 1)
                if (k - n) % 2 == 0 and k >= n
            )
            term_b = (beta / 2.0) ** n / math.factorial(n)
            form_b = 0.0
            for m in range(mmax + 1):
                form_b += term_b
                term_b *= (beta / 2.0) ** 2 / ((m + 1) * (m + n + 1))
            lower, upper, tail = bessel_i_positive_series_interval(beta, n)
            max_ab = max(max_ab, abs(form_a - form_b))
            ab_failures += abs(form_a - form_b) > 1e-13
            interval_failures += not (lower <= form_b <= upper)
            max_bessel_tail = max(max_bessel_tail, tail)
    check(
        "U(1) binomial and Bessel combinatorial forms agree",
        ab_failures == 0,
        f"max |A-B|={max_ab:.3e}, failures={ab_failures}",
    )
    check(
        "U(1) combinatorial values lie in certified Bessel intervals",
        interval_failures == 0,
        f"max tail={max_bessel_tail:.3e}, failures={interval_failures}",
    )

    density2 = {(0,): 2, (2,): -1, (-2,): -1}
    density2_ct = density2[(0,)]
    h2 = {(1,): 2, (-1,): 2}
    h2_powers = [{(0,): 1}]
    for _ in range(N_SERIES):
        h2_powers.append(poly_mul(h2_powers[-1], h2))
    labels2 = list(range(9))
    characters2 = {
        r: {(exponent,): 1 for exponent in range(-r, r + 1, 2)} for r in labels2
    }
    g2 = {r: poly_mul(poly_conj(characters2[r]), density2) for r in labels2}
    multiplicities2 = {}
    for r in labels2:
        for n, power in enumerate(h2_powers):
            numerator = constant_term_sparse_dot(power, g2[r])
            assert numerator % 2 == 0
            value = numerator // 2
            assert value >= 0
            multiplicities2[(r, n)] = value
    check("SU(2) Weyl-density normalization", density2_ct == 2, f"CT={density2_ct}")

    dim2_residuals = []
    for n in range(9):
        observed = sum(multiplicities2[(r, n)] * (r + 1) for r in labels2)
        dim2_residuals.append(observed - 4**n)
    check(
        "SU(2) exact dimension sums through n=8",
        all(x == 0 for x in dim2_residuals),
        f"max residual={max(map(abs, dim2_residuals))}",
    )

    theta = np.linspace(0.0, 2.0 * np.pi, 256, endpoint=False)
    density2_grid = eval_laurent_su2(density2, theta)
    max_su2_residual = 0.0
    max_su2_allowance = 0.0
    su2_failures = 0
    for beta in BETA_VALUES:
        kernel = np.exp(2.0 * beta * np.cos(theta))
        allowance = tail_bound(beta, 2) + 1e-9
        for r in labels2:
            exact = Fraction(0, 1)
            b = Fraction(str(beta))
            for n in range(N_SERIES + 1):
                exact += Fraction(multiplicities2[(r, n)], math.factorial(n)) * (b / 2) ** n
            series = float(exact)
            quad = np.mean(kernel * np.conj(eval_laurent_su2(characters2[r], theta)) * density2_grid / 2.0)
            residual = abs(quad - series)
            max_su2_residual = max(max_su2_residual, residual)
            max_su2_allowance = max(max_su2_allowance, allowance)
            su2_failures += residual > allowance
    check(
        "SU(2) quadrature cross-extraction",
        su2_failures == 0,
        f"max residual={max_su2_residual:.3e}, max allowed={max_su2_allowance:.3e}, failures={su2_failures}",
    )

    return {
        "characters": characters,
        "multiplicities": multiplicities,
        "coefficient_float": coefficient_float,
        "ctilde2": ctilde2,
        "labels8": labels8,
    }


# ---------------------------------------------------------------------------
# Explicit representation matrices for the n <= 2 irreducible set.
# ---------------------------------------------------------------------------
LAMBDA2 = ((0, 0), (1, 0), (0, 1), (2, 0), (0, 2), (1, 1))


def symmetric_basis_matrix():
    columns = []
    for i in range(3):
        vector = np.zeros(9, dtype=np.complex128)
        vector[3 * i + i] = 1.0
        columns.append(vector)
    for i in range(3):
        for j in range(i + 1, 3):
            vector = np.zeros(9, dtype=np.complex128)
            vector[3 * i + j] = 1.0 / math.sqrt(2.0)
            vector[3 * j + i] = 1.0 / math.sqrt(2.0)
            columns.append(vector)
    return np.column_stack(columns)


SYM_BASIS = symmetric_basis_matrix()


def gell_mann_basis():
    zero = 0.0
    i = 1j
    matrices = [
        [[zero, 1, zero], [1, zero, zero], [zero, zero, zero]],
        [[zero, -i, zero], [i, zero, zero], [zero, zero, zero]],
        [[1, zero, zero], [zero, -1, zero], [zero, zero, zero]],
        [[zero, zero, 1], [zero, zero, zero], [1, zero, zero]],
        [[zero, zero, -i], [zero, zero, zero], [i, zero, zero]],
        [[zero, zero, zero], [zero, zero, 1], [zero, 1, zero]],
        [[zero, zero, zero], [zero, zero, -i], [zero, i, zero]],
        [[1 / math.sqrt(3), zero, zero], [zero, 1 / math.sqrt(3), zero], [zero, zero, -2 / math.sqrt(3)]],
    ]
    return np.asarray(matrices, dtype=np.complex128) / math.sqrt(2.0)


GELL_MANN = gell_mann_basis()


def haar_su3(n: int, rng: np.random.Generator):
    gaussian = rng.standard_normal((n, 3, 3)) + 1j * rng.standard_normal((n, 3, 3))
    q, r = np.linalg.qr(gaussian)
    diagonal = np.diagonal(r, axis1=1, axis2=2)
    phases = diagonal / np.abs(diagonal)
    q = q * phases[:, None, :]
    determinant = np.linalg.det(q)
    q *= np.exp(-1j * np.angle(determinant) / 3.0)[:, None, None]
    return q


def sym2_batch(u):
    kron = np.einsum("nij,nkl->nikjl", u, u, optimize=True).reshape((-1, 9, 9))
    return np.einsum("ap,npq,qb->nab", SYM_BASIS.conj().T, kron, SYM_BASIS, optimize=True)


def adjoint_batch(u):
    ut = np.einsum("nij,bjk->nbik", u, GELL_MANN, optimize=True)
    transformed = np.einsum("nbik,nlk->nbil", ut, np.conj(u), optimize=True)
    return np.einsum("aij,nbji->nab", GELL_MANN, transformed, optimize=True)


def representation_batches(u):
    n = len(u)
    sym = sym2_batch(u)
    return {
        (0, 0): np.ones((n, 1, 1), dtype=np.complex128),
        (1, 0): u,
        (0, 1): np.conj(u),
        (2, 0): sym,
        (0, 2): np.conj(sym),
        (1, 1): adjoint_batch(u),
    }


def representation_flat(u):
    batches = representation_batches(u)
    return np.concatenate([batches[label].reshape((len(u), -1)) for label in LAMBDA2], axis=1)


def character_from_eigenangles(poly, u):
    eigenvalues = np.linalg.eigvals(u)
    theta1, theta2 = np.angle(eigenvalues[:2])
    return sum(
        coefficient * np.exp(1j * (m1 * theta1 + m2 * theta2))
        for (m1, m2), coefficient in poly.items()
    )


def ctilde_table(part_a, beta: float):
    return {label: part_a["ctilde2"][beta][label] for label in LAMBDA2}


def run_part_b(part_a):
    section("Explicit matrix elements for the n<=2 irreducible set")
    pairs_u = haar_su3(20, RNG)
    pairs_v = haar_su3(20, RNG)
    max_unitarity = 0.0
    max_homomorphism = 0.0
    max_character_tie = 0.0
    max_kernel_identity = 0.0
    coefficients = ctilde_table(part_a, 0.5)

    for u, v in zip(pairs_u, pairs_v):
        du = {label: value[0] for label, value in representation_batches(u[None]).items()}
        dv = {label: value[0] for label, value in representation_batches(v[None]).items()}
        duv = {label: value[0] for label, value in representation_batches((u @ v)[None]).items()}
        w = u @ v.conj().T
        dw = {label: value[0] for label, value in representation_batches(w[None]).items()}
        for label in LAMBDA2:
            identity = np.eye(du[label].shape[0])
            max_unitarity = max(
                max_unitarity,
                float(np.linalg.norm(du[label] @ du[label].conj().T - identity)),
                float(np.linalg.norm(dv[label] @ dv[label].conj().T - identity)),
            )
            max_homomorphism = max(
                max_homomorphism,
                float(np.linalg.norm(duv[label] - du[label] @ dv[label])),
            )
            exact_character = character_from_eigenangles(part_a["characters"][label], u)
            max_character_tie = max(max_character_tie, abs(np.trace(du[label]) - exact_character))

        left = sum(coefficients[label] * np.trace(dw[label]) for label in LAMBDA2)
        right = sum(
            coefficients[label] * np.sum(du[label] * np.conj(dv[label]))
            for label in LAMBDA2
        )
        max_kernel_identity = max(max_kernel_identity, abs(left - right))

    check(
        "Explicit representation matrices are unitary",
        max_unitarity <= 1e-12,
        f"max ||D D^dag-I||={max_unitarity:.3e}",
    )
    check(
        "Explicit representation matrices respect composition",
        max_homomorphism <= 1e-12,
        f"max ||D(UV)-D(U)D(V)||={max_homomorphism:.3e}",
    )
    check(
        "Explicit characters tie to the exact torus polynomials",
        max_character_tie <= 1e-10,
        f"max |trace D-chi|={max_character_tie:.3e}",
    )
    check(
        "Pointwise truncated-kernel spectral identity",
        max_kernel_identity <= 1e-12,
        f"max residual={max_kernel_identity:.3e}",
    )
    return coefficients


# ---------------------------------------------------------------------------
# Composed two-slice integral at L_s = 2.
# ---------------------------------------------------------------------------
def trace_product_real(a, b):
    return np.real(np.einsum("nij,nji->n", a, b, optimize=True))


def trace_cross_real(a, b):
    return np.real(np.einsum("nij,nij->n", a, np.conj(b), optimize=True))


def observables(u1, u2):
    tr1 = np.trace(u1, axis1=1, axis2=2)
    tr2 = np.trace(u2, axis1=1, axis2=2)
    tr12 = np.einsum("nij,nji->n", u1, u2, optimize=True)
    return np.column_stack(
        (
            np.ones(len(u1), dtype=np.complex128),
            tr1,
            tr2,
            tr12,
            np.conj(tr1),
            np.conj(tr2),
            np.conj(tr12),
            math.sqrt(3.0) * u1[:, 0, 0],
            math.sqrt(3.0) * u2[:, 0, 1],
            tr1 * tr2,
        )
    )


def composed_mc(beta, n_samples, rng, temporal="full", conjugate_reflected=True):
    assert n_samples >= 100_000 and n_samples % 10 == 0
    batch_size = n_samples // 10
    numerator = np.zeros((10, 10), dtype=np.complex128)
    denominator = 0.0
    batch_grams = []
    for _ in range(10):
        u10 = haar_su3(batch_size, rng)
        u20 = haar_su3(batch_size, rng)
        u11 = haar_su3(batch_size, rng)
        u21 = haar_su3(batch_size, rng)
        bminus = beta * trace_product_real(u10, u20)
        bplus = beta * trace_product_real(u11, u21)
        if temporal == "full":
            temporal_weight = np.exp(
                beta * (trace_cross_real(u10, u11) + trace_cross_real(u20, u21))
            )
        elif temporal == "truncated":
            x1 = beta * trace_cross_real(u10, u11)
            x2 = beta * trace_cross_real(u20, u21)
            temporal_weight = (1.0 + x1 + 0.5 * x1 * x1) * (1.0 + x2 + 0.5 * x2 * x2)
        else:
            raise ValueError(temporal)
        weights = np.exp(bplus + bminus) * temporal_weight
        fminus = observables(u10, u20)
        fplus = observables(u11, u21)
        reflected = np.conj(fminus) if conjugate_reflected else fminus
        batch_numerator = np.einsum(
            "n,ni,nj->ij", weights, reflected, fplus, optimize=True
        )
        batch_denominator = float(np.sum(weights))
        batch_grams.append(batch_numerator / batch_denominator)
        numerator += batch_numerator
        denominator += batch_denominator
    gram = numerator / denominator
    batch_grams = np.asarray(batch_grams)
    entry_error = np.std(batch_grams, axis=0, ddof=1) / math.sqrt(10.0)
    mc_noise = float(np.max(entry_error))
    herm_err = float(np.max(np.abs(gram - gram.conj().T)))
    hermitian = (gram + gram.conj().T) / 2.0
    eigenvalues = np.linalg.eigvalsh(hermitian)
    return {
        "gram": gram,
        "hermitian": hermitian,
        "eigenvalues": eigenvalues,
        "entry_error": entry_error,
        "mc_noise": mc_noise,
        "herm_err": herm_err,
        "batch_grams": batch_grams,
    }


def factor_stream(beta, rng, n_stream=4000):
    assert n_stream >= 4000 and n_stream % 10 == 0
    batch_size = n_stream // 10
    batches = []
    for _ in range(10):
        u1 = haar_su3(batch_size, rng)
        u2 = haar_su3(batch_size, rng)
        f = observables(u1, u2)
        exp_bplus = np.exp(beta * trace_product_real(u1, u2))
        a_w = f.T * exp_bplus[None, :] / batch_size
        d1flat = representation_flat(u1)
        d2flat = representation_flat(u2)
        matrix = np.einsum(
            "in,na,nb->iab",
            a_w,
            np.conj(d1flat),
            np.conj(d2flat),
            optimize=True,
        )
        batches.append(matrix)
    batches = np.asarray(batches)
    return np.mean(batches, axis=0), batches


def normalized_factor_gram(m_a, m_b, c_joint):
    raw = np.einsum("iab,ab,jab->ij", np.conj(m_a), c_joint, m_b, optimize=True)
    return raw / raw[0, 0], raw


def run_part_c(part_a):
    section("Composed two-slice SU(3) form at L_s=2")
    c1_results = {}
    for beta in (0.15, 0.75):
        result = composed_mc(beta, 200_000, RNG)
        c1_results[beta] = result
        minimum = float(result["eigenvalues"][0])
        threshold = max(3.0 * result["mc_noise"], 5e-3)
        print(
            f"  Full-weight beta={beta}: min_eig={minimum:+.6e}, mc_noise={result['mc_noise']:.3e}, "
            f"herm_err={result['herm_err']:.3e}, eigenvalues={np.array2string(result['eigenvalues'], precision=5)}"
        )
        check(
            f"Full-weight Gram at beta={beta} is PSD within sampling error",
            minimum > -threshold,
            f"min eig={minimum:+.6e}, negative allowance={threshold:.3e}",
        )
        check(
            f"Full-weight sampling error at beta={beta} is controlled",
            result["mc_noise"] < 0.05,
            f"mc_noise={result['mc_noise']:.3e}",
        )
        check(
            f"Full-weight Hermiticity residual at beta={beta} is sampling-sized",
            result["herm_err"] < 10.0 * result["mc_noise"] + 1e-12,
            f"herm_err={result['herm_err']:.3e}, allowance={10.0 * result['mc_noise'] + 1e-12:.3e}",
        )

    beta = 0.15
    direct = composed_mc(beta, 100_000, RNG, temporal="truncated")
    seed_a = int(RNG.integers(0, 2**63 - 1))
    seed_b = int(RNG.integers(0, 2**63 - 1))
    m_a, m_a_batches = factor_stream(beta, np.random.default_rng(seed_a))
    m_b, m_b_batches = factor_stream(beta, np.random.default_rng(seed_b))

    dims = {label: su3_dimension(label) for label in LAMBDA2}
    coefficients = ctilde_table(part_a, beta)
    b = Fraction(str(beta))
    expected_coefficients = {
        (0, 0): float(1 + b * b / 4),
        (1, 0): float(b / 2 + b * b / 8),
        (0, 1): float(b / 2 + b * b / 8),
        (2, 0): float(b * b / 8),
        (0, 2): float(b * b / 8),
        (1, 1): float(b * b / 4),
    }
    expected_w155 = np.concatenate(
        [np.full(dims[label] ** 2, expected_coefficients[label], dtype=np.float64) for label in LAMBDA2]
    )
    w155 = np.concatenate(
        [np.full(dims[label] ** 2, coefficients[label], dtype=np.float64) for label in LAMBDA2]
    )
    c_joint = np.outer(w155, w155)
    factor, factor_raw = normalized_factor_gram(m_a, m_b, c_joint)

    factor_batches = []
    for index in range(10):
        batch_factor, _ = normalized_factor_gram(
            m_a_batches[index], m_b_batches[index], c_joint
        )
        factor_batches.append(batch_factor)
    factor_batches = np.asarray(factor_batches)
    factor_error = np.std(factor_batches, axis=0, ddof=1) / math.sqrt(10.0)
    combined_sigma = np.sqrt(direct["entry_error"] ** 2 + factor_error**2)
    difference = np.abs(direct["gram"] - factor)
    allowance = 6.0 * combined_sigma + 1e-3
    violation_ratio = difference / allowance
    max_ratio = float(np.max(violation_ratio))
    check(
        "Direct truncated integral matches independent spectral factorization",
        np.all(difference <= allowance),
        f"max |direct-factor|={np.max(difference):.3e}, max violation ratio={max_ratio:.3f}",
    )

    same_raw = np.einsum(
        "iab,ab,jab->ij", np.conj(m_a), c_joint, m_a, optimize=True
    )
    same_hermitian = (same_raw + same_raw.conj().T) / 2.0
    same_minimum = float(np.linalg.eigvalsh(same_hermitian)[0])
    check(
        "Same-stream factorization is a manifest Gram matrix",
        same_minimum >= -1e-10,
        f"min eig={same_minimum:+.6e}",
    )

    check(
        "Factorization coefficients match independent order-two representation-ring formulas",
        w155.tobytes() == expected_w155.tobytes(),
        f"bytes={len(w155.tobytes())}, max value residual={np.max(np.abs(w155 - expected_w155)):.3e}",
    )

    consistency_difference = float(np.max(np.abs(c1_results[0.15]["gram"] - direct["gram"])))
    consistency_allowance = 0.05 + 5.0 * (c1_results[0.15]["mc_noise"] + direct["mc_noise"])
    per_link_remainder_bound = (
        math.exp(3.0 * beta) - 1.0 - 3.0 * beta - 0.5 * (3.0 * beta) ** 2
    )
    print(
        f"  Truncation diagnostic: per-link sup |k-ktilde_2| <= {per_link_remainder_bound:.9e}; "
        f"observed Gram difference={consistency_difference:.3e}"
    )
    check(
        "Full and truncated composed Grams agree within the Monte Carlo smoke-test tolerance",
        consistency_difference <= consistency_allowance,
        f"observed={consistency_difference:.3e}, allowance={consistency_allowance:.3e}",
    )

    linear = composed_mc(1.0, 100_000, RNG, conjugate_reflected=False)
    linear_minimum = float(linear["eigenvalues"][0])
    check(
        "No-conjugation control is non-PSD",
        linear_minimum < -1e-3,
        f"min eig={linear_minimum:+.6e}, mc_noise={linear['mc_noise']:.3e}",
    )

    zero = composed_mc(0.0, 100_000, RNG)
    target = np.zeros((10, 10), dtype=np.complex128)
    target[0, 0] = 1.0
    zero_difference = float(np.max(np.abs(zero["gram"] - target)))
    zero_allowance = 6.0 * zero["mc_noise"] + 1e-3
    check(
        "Beta=0 Gram matches the exact rank-one anchor",
        zero_difference <= zero_allowance,
        f"max residual={zero_difference:.3e}, allowance={zero_allowance:.3e}",
    )
    absolute_eigenvalues = np.sort(np.abs(zero["eigenvalues"]))[::-1]
    second_largest = float(absolute_eigenvalues[1])
    check(
        "Beta=0 non-leading spectrum vanishes within sampling error",
        second_largest <= zero_allowance,
        f"second-largest |eig|={second_largest:.3e}, allowance={zero_allowance:.3e}",
    )


def main():
    print("=" * 88)
    print("SU(3) Wilson plane-kernel character positivity and composed two-slice Gram")
    print("Exact multiplicities, independent cross-extractions, and L_s=2 composed integral")
    print("=" * 88)
    part_a = build_part_a_data()
    run_part_b(part_a)
    run_part_c(part_a)

    section("Summary")
    if FAIL:
        print("  One or more checks genuinely failed; see the observed values above.")
    else:
        print("  All exact, discriminating, representation, and composed-integral checks passed.")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
