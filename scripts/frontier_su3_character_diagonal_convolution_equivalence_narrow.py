#!/usr/bin/env python3
"""Abstract B_4 runner for `SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10`.

Verifies, on the finite N = 4 truncation B_4 = {(p, q) : 0 <= p, q <= 4} of
dominant SU(3) weights, the abstract algebraic equivalence between

  - the diagonal positive central operator
        R chi_(p,q) = rho_(p,q) chi_(p,q),
    indexed by an abstract real coefficient sequence with rho_(p,q) >= 0,
    rho_(0,0) = 1, rho_(p,q) = rho_(q,p), and

  - the normalized convolution operator C_{Z/Z_(0,0)} by the central class
    function
        Z(W) = sum_(p,q in B_4) d_(p,q) rho_(p,q) chi_(p,q)(W),
    where d_(p,q) = (p+1)(q+1)(p+q+2)/2 is the irrep dimension and
    Z_(0,0) = d_(0,0) rho_(0,0) = 1.

THEN the following identities hold on the abstract B_4 packet:

  (T1) Schur character orthogonality on B_4 (Peter-Weyl, standard
       character normalization on a compact Lie group):
       <chi_(p,q), chi_(p',q')>_Haar
          = int_{SU(3)} chi_(p,q)(W) conj(chi_(p',q')(W)) dW
          = delta_((p,q),(p',q')).

  (T2) Diagonal action of normalized convolution:
       C_{Z/Z_(0,0)} chi_(p,q) = rho_(p,q) chi_(p,q) on V_4.

  (T3) Uniqueness: rho^(1) = rho^(2) iff their diagonal operators agree.

  (T4) Positivity / self-adjointness / swap-symmetry of R under the
       real nonnegative swap-symmetric hypotheses. The separate condition
       rho_(0,0) = 1 fixes the trivial-channel normalization used in T2.

The input surface is the finite B_4 SU(3) character basis, normalized Haar
probability measure, an abstract real nonnegative swap-symmetric sequence
(rho_(p,q)) with rho_(0,0) = 1, and standard compact-group representation
algebra. The output surface is T1 Schur orthogonality, T2 equality of
normalized convolution and diagonal action on V_4, T3 coefficient uniqueness,
and T4 positivity, self-adjointness, and swap symmetry. In the parent
Wilson-environment program, a physical coefficient result supplies the
sequence with its own authority; this runner verifies the algebraic map after
that typed input is present.

The load-bearing verification expands chi_lambda(V W^-1) into generic
representation-matrix entries and contracts the three matrix indices using
matrix-element Schur orthogonality before rho is introduced. A separate
deterministic Haar-random SU(3) calculation checks the convolution using
explicit fundamental, antifundamental, adjoint, and low symmetric-power
character formulas. Hostile mutations reject a missing 1/d factor, W in
place of W^-1, conjugating the target character, and returning rho_target
alone in place of the V-dependent value rho_target chi_target(V).
"""

from __future__ import annotations

from fractions import Fraction
import sys

import numpy as np

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS (A)" if ok else "FAIL (A)"
    print(f"  [{tag}] {label}  ({detail})")


def section(title: str) -> None:
    print("\n" + "-" * 88 + f"\n{title}\n" + "-" * 88)


# =============================================================================
# Setup: SU(3) abstract character algebra ingredients
# =============================================================================

N = 4
B_N = [(p, q) for p in range(N + 1) for q in range(N + 1)]
INDEX = {w: i for i, w in enumerate(B_N)}


def d_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def weyl_chi(p: int, q: int, t1: float, t2: float) -> complex:
    """SU(3) Weyl character at U = diag(e^{i t1}, e^{i t2}, e^{-i(t1+t2)}).

    chi_lambda(U) = det( z_i^{lam_j + n - j} ) / det( z_i^{n - j} ),
    with n = 3, lam = (p+q, q, 0) the SU(3) highest weight triple.
    """
    t3 = -t1 - t2
    z = np.array([np.exp(1j * t1), np.exp(1j * t2), np.exp(1j * t3)], dtype=complex)
    lam = [p + q, q, 0]
    num = np.zeros((3, 3), dtype=complex)
    den = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        for j in range(3):
            num[i, j] = z[i] ** (lam[j] + 2 - j)
            den[i, j] = z[i] ** (2 - j)
    detd = np.linalg.det(den)
    if abs(detd) < 1e-12:
        return 0.0  # Weyl wall has Haar measure zero
    return np.linalg.det(num) / detd


def vandermonde_sq(t1: float, t2: float) -> float:
    z = [np.exp(1j * t1), np.exp(1j * t2), np.exp(-1j * (t1 + t2))]
    prod = 1.0
    for i in range(3):
        for j in range(i + 1, 3):
            prod *= abs(z[i] - z[j]) ** 2
    return float(prod)


def haar_inner_product(p1: int, q1: int, p2: int, q2: int, n_grid: int = 80) -> complex:
    """Compute <chi_(p1,q1), chi_(p2,q2)>_Haar = int chi_(p1,q1)(W) conj(chi_(p2,q2)(W)) dW.

    Standard Schur character orthogonality on a compact Lie group:
        <chi_lambda, chi_mu>_Haar = delta_{lambda,mu}.
    Evaluated by Weyl integration on the SU(3) Cartan torus T^2 with |W| = 6.
    """
    th = np.linspace(0, 2 * np.pi, n_grid, endpoint=False)
    h = 2 * np.pi / n_grid
    total = 0.0 + 0.0j
    for t1 in th:
        for t2 in th:
            c1 = weyl_chi(p1, q1, t1, t2)
            c2 = np.conjugate(weyl_chi(p2, q2, t1, t2))
            v2 = vandermonde_sq(t1, t2)
            total += c1 * c2 * v2 * h * h
    total /= (2 * np.pi) ** 2
    total /= 6.0  # |W| = 6 for SU(3)
    return total


# =============================================================================
section("Part 1 (T1): Schur orthogonality on the finite B_4 truncation")
# =============================================================================
# Verify <chi_(p,q), chi_(p',q')> = delta_((p,q),(p',q')) numerically.
# Quadrature grid is finite; the selected character products are expected to
# reproduce the Kronecker-delta pattern to tight numerical tolerance.

N_GRID = 80
print(f"  Using N_GRID = {N_GRID} for Weyl integration; matrix size {len(B_N)} x {len(B_N)}")
# Sample a representative subset to keep runtime sane; the algebraic content
# (delta-on-the-diagonal-of-the-paired-orbit) is verified across pairs.
orth_pairs = []
test_weights = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (2, 1), (1, 2), (2, 2)]
for w1 in test_weights:
    for w2 in test_weights:
        orth_pairs.append((w1, w2))

n_diag_ok = 0
n_off_ok = 0
n_diag = 0
n_off = 0
max_diag_err = 0.0
max_off_err = 0.0
for (p1, q1), (p2, q2) in orth_pairs:
    val = haar_inner_product(p1, q1, p2, q2, n_grid=N_GRID)
    val_real = val.real
    val_imag_abs = abs(val.imag)
    same = (p1, q1) == (p2, q2)
    if same:
        n_diag += 1
        expected = 1.0  # Schur orthogonality: <chi_lambda, chi_lambda> = 1
        err = abs(val_real - expected)
        max_diag_err = max(max_diag_err, err)
        if err < 1e-6 and val_imag_abs < 1e-6:
            n_diag_ok += 1
    else:
        n_off += 1
        err = abs(val_real)
        max_off_err = max(max_off_err, err)
        if err < 1e-6 and val_imag_abs < 1e-6:
            n_off_ok += 1

check(
    "Schur orthogonality off-diagonal: <chi_(p,q), chi_(p',q')> = 0 for (p,q) != (p',q') on test pairs",
    n_off_ok == n_off and max_off_err < 1e-6,
    detail=f"off-diag pairs={n_off}, ok={n_off_ok}, max err={max_off_err:.3e}",
)
check(
    "Schur orthogonality diagonal: <chi_(p,q), chi_(p,q)> = 1 on test weights",
    n_diag_ok == n_diag,
    detail=f"diag weights={n_diag}, ok={n_diag_ok}, max abs deviation={max_diag_err:.3e}",
)


# =============================================================================
section("Part 2 (T2): exact matrix-index contraction for character convolution")
# =============================================================================
# With D^lambda unitary,
#
#   chi_lambda(V W^-1)
#     = Tr[D^lambda(V) D^lambda(W)^dagger]
#     = sum_(a,b) D^lambda(V)_(a,b) conj(D^lambda(W)_(a,b)),
#
# while chi_mu(W) = sum_c D^mu(W)_(c,c). Matrix-element Schur
# orthogonality supplies, before any character-convolution identity,
#
#   int conj(D^lambda_(a,b)) D^mu_(c,c) dW
#     = delta_(lambda,mu) delta_(a,c) delta_(b,c) / d_mu.
#
# The dictionaries below are exact symbolic polynomials in the generic
# entries D^lambda(V)_(a,b): matrix indices are keys and Fraction values are
# their coefficients. Thus the 1/d factor and the surviving diagonal trace
# are produced directly by the indexed contraction.
MatrixPolynomial = dict[tuple[int, int], Fraction]
ConvolutionPolynomial = dict[tuple[tuple[int, int], int, int], Fraction | float]


def schur_matrix_element_coefficient(
    kernel: tuple[int, int],
    target: tuple[int, int],
    a: int,
    b: int,
    c: int,
) -> Fraction:
    """Coefficient from int conj(D^kernel_ab) D^target_cc dW."""
    irrep_delta = int(kernel == target)
    index_delta = int(a == c) * int(b == c)
    return Fraction(irrep_delta * index_delta, d_su3(*target))


def matrix_element_contraction(
    kernel: tuple[int, int], target: tuple[int, int]
) -> MatrixPolynomial:
    """Mechanically contract the (a,b,c) indices in the translated characters."""
    if kernel != target:
        # The inequivalent-irrep Schur delta is zero for every matrix index.
        return {}

    result: MatrixPolynomial = {}
    for a in range(d_su3(*kernel)):
        for b in range(d_su3(*kernel)):
            coefficient = sum(
                (
                    schur_matrix_element_coefficient(kernel, target, a, b, c)
                    for c in range(d_su3(*target))
                ),
                Fraction(0),
            )
            if coefficient:
                result[(a, b)] = coefficient
    return result


def expected_trace_over_dimension(weight: tuple[int, int]) -> MatrixPolynomial:
    """The symbolic polynomial Tr D^weight(V) / d_weight."""
    dimension = d_su3(*weight)
    return {(c, c): Fraction(1, dimension) for c in range(dimension)}


CONTRACTIONS = {
    (kernel, target): matrix_element_contraction(kernel, target)
    for kernel in B_N
    for target in B_N
}

inequivalent_example = CONTRACTIONS[((1, 0), (0, 1))]
inequivalent_coefficients = [
    schur_matrix_element_coefficient((1, 0), (0, 1), a, b, c)
    for a in range(d_su3(1, 0))
    for b in range(d_su3(1, 0))
    for c in range(d_su3(0, 1))
]
check(
    "(T2) a generic fundamental/antifundamental matrix-element contraction is zero",
    inequivalent_example == {}
    and all(coefficient == 0 for coefficient in inequivalent_coefficients),
    detail=f"mechanically checked all {len(inequivalent_coefficients)} (a,b,c) coefficients",
)

fundamental_example = CONTRACTIONS[((1, 0), (1, 0))]
check(
    "(T2) a generic same-fundamental contraction is Tr D_(1,0)(V) / 3",
    fundamental_example
    == {
        (0, 0): Fraction(1, 3),
        (1, 1): Fraction(1, 3),
        (2, 2): Fraction(1, 3),
    },
    detail=f"symbolic polynomial={fundamental_example}",
)

off_diagonal_contractions_ok = all(
    CONTRACTIONS[(kernel, target)] == {}
    for kernel in B_N
    for target in B_N
    if kernel != target
)
check(
    "(T2) raw matrix-element contraction vanishes for every unequal B_4 irrep pair",
    off_diagonal_contractions_ok,
    detail=f"checked {len(B_N) * (len(B_N) - 1)} inequivalent pairs before applying rho",
)

diagonal_contractions_ok = all(
    CONTRACTIONS[(weight, weight)] == expected_trace_over_dimension(weight)
    for weight in B_N
)
check(
    "(T2) raw same-irrep contraction equals Tr D_mu(V) / d_mu throughout B_4",
    diagonal_contractions_ok,
    detail=f"checked all {len(B_N)} dimensions, from 1 through {max(d_su3(*w) for w in B_N)}",
)

# Hostile mutation: omit the Schur 1/d normalization. It produces Tr D(V),
# which differs by a factor of d from the required fundamental contraction.
missing_dimension_mutant = {
    (c, c): Fraction(1) for c in range(d_su3(1, 0))
}
check(
    "hostile control rejects a missing 1/d_mu factor",
    missing_dimension_mutant != fundamental_example
    and all(
        missing_dimension_mutant[key] == d_su3(1, 0) * fundamental_example[key]
        for key in fundamental_example
    ),
    detail="mutant gives Tr D_(1,0)(V), exactly three times the required contraction",
)


def apply_z_convolution(
    rho_seq: list[Fraction] | list[float], target: tuple[int, int]
) -> ConvolutionPolynomial:
    """Build C_Z chi_target as a generic representation-matrix polynomial."""
    result: ConvolutionPolynomial = {}
    for kernel in B_N:
        z_coefficient = d_su3(*kernel) * rho_seq[INDEX[kernel]]
        for (a, b), raw_coefficient in CONTRACTIONS[(kernel, target)].items():
            key = (kernel, a, b)
            result[key] = result.get(key, 0) + z_coefficient * raw_coefficient
    return {key: value for key, value in result.items() if value != 0}


def expected_diagonal_polynomial(
    rho_seq: list[Fraction] | list[float], target: tuple[int, int]
) -> ConvolutionPolynomial:
    """Build rho_target Tr D^target(V), independently of the convolution sum."""
    coefficient = rho_seq[INDEX[target]]
    if coefficient == 0:
        return {}
    return {
        (target, c, c): coefficient
        for c in range(d_su3(*target))
    }


# Multiplication by d_lambda in Z cancels the 1/d_mu from the raw
# contraction only on lambda=mu. This matrix is assembled before rho is
# chosen, so the dimension cancellation is independently load-bearing.
dimension_weighted_convolution = np.zeros((len(B_N), len(B_N)), dtype=object)
for kernel in B_N:
    for target in B_N:
        raw = CONTRACTIONS[(kernel, target)]
        if not raw:
            dimension_weighted_convolution[INDEX[kernel], INDEX[target]] = Fraction(0)
        elif raw == expected_trace_over_dimension(target):
            dimension_weighted_convolution[INDEX[kernel], INDEX[target]] = (
                d_su3(*kernel) * raw[(0, 0)]
            )
        else:
            dimension_weighted_convolution[INDEX[kernel], INDEX[target]] = None

dimension_cancellation_ok = all(
    dimension_weighted_convolution[i, j] == Fraction(int(i == j))
    for i in range(len(B_N))
    for j in range(len(B_N))
)
check(
    "(T2) d_lambda in Z cancels 1/d_mu and gives the exact 25 x 25 identity",
    dimension_cancellation_ok,
    detail="dimension-weighted raw convolution matrix assembled before rho",
)


# Construct an abstract POSITIVE SYMMETRIC rational coefficient sequence:
def make_positive_symmetric(coef_map: dict[tuple[int, int], Fraction]) -> list[Fraction]:
    """Build a sequence rho over B_4 from a (p,q)->rational map, enforcing
    rho_(p,q) = rho_(q,p) and rho_(0,0) = 1."""
    rho = [Fraction(0)] * len(B_N)
    rho[INDEX[(0, 0)]] = Fraction(1)
    for (p, q), val in coef_map.items():
        if (p, q) == (0, 0):
            continue
        rho[INDEX[(p, q)]] = val
        rho[INDEX[(q, p)]] = val  # enforce conjugation symmetry
    return rho


rho1 = make_positive_symmetric({
    (1, 0): Fraction(2, 5),
    (1, 1): Fraction(1, 7),
    (2, 0): Fraction(1, 8),
    (2, 1): Fraction(1, 13),
    (3, 0): Fraction(1, 20),
    (2, 2): Fraction(1, 25),
    (3, 1): Fraction(1, 35),
    (4, 0): Fraction(1, 60),
    (3, 2): Fraction(1, 90),
    (4, 1): Fraction(1, 110),
    (4, 2): Fraction(1, 250),
    (3, 3): Fraction(1, 350),
    (4, 3): Fraction(1, 500),
    (4, 4): Fraction(1, 800),
})

# Apply the finite sum only after the raw contraction and dimension
# cancellation have been checked. Compare full generic matrix polynomials
# against independently constructed expected polynomials.
all_targets_ok = True
for target in B_N:
    actual = apply_z_convolution(rho1, target)
    expected = expected_diagonal_polynomial(rho1, target)
    if actual != expected:
        all_targets_ok = False
        print(f"    FAIL: target={target}, actual={actual}, expected={expected}")
check(
    "(T2) For abstract rational positive-symmetric (rho_(p,q)): "
    "the contracted finite sum gives C_{Z/Z_(0,0)} chi_(p,q) = rho_(p,q) chi_(p,q) "
    "for every (p,q) in B_4",
    all_targets_ok,
    detail=f"all {len(B_N)} weights in B_{N} pass exact matrix-polynomial comparison",
)


# =============================================================================
section("Part 3 (T3): uniqueness of (rho_(p,q)) for the diagonal operator R")
# =============================================================================
# Two distinct coefficient sequences give two distinct diagonal operators.
rho2 = list(rho1)
rho2[INDEX[(2, 1)]] = Fraction(1, 12)  # perturb only one off-symmetric entry
# enforce conjugation symmetry by also flipping (1, 2)
rho2[INDEX[(1, 2)]] = Fraction(1, 12)

# Verify rho1 != rho2 entrywise at exactly the perturbed pair.
n_diff = sum(1 for i in range(len(B_N)) if rho1[i] != rho2[i])
check(
    "(T3) Two distinct coefficient sequences rho^(1) != rho^(2) differ in exactly the perturbed entries",
    n_diff == 2 and rho1[INDEX[(2, 1)]] != rho2[INDEX[(2, 1)]],
    detail=f"entries differing = {n_diff} (one symmetric pair perturbed: (2,1) and (1,2))",
)

# Verify the corresponding diagonal operators agree on every basis weight EXCEPT
# the perturbed pair (where they differ by a definite amount).
R1_diag = [float(r) for r in rho1]
R2_diag = [float(r) for r in rho2]
agree_ok = True
diff_pair_correct = True
for i, (p, q) in enumerate(B_N):
    if (p, q) in [(2, 1), (1, 2)]:
        if abs(R1_diag[i] - R2_diag[i]) < 1e-15:
            diff_pair_correct = False
    else:
        if abs(R1_diag[i] - R2_diag[i]) > 1e-15:
            agree_ok = False
check(
    "(T3) Diagonal operators agree on every (p,q) except the perturbed pair",
    agree_ok,
    detail="all unaltered eigenvalues are identical between R^(1) and R^(2)",
)
check(
    "(T3) Diagonal operators disagree on exactly the perturbed pair (2,1) and (1,2)",
    diff_pair_correct,
    detail=f"R^(1)[(2,1)] = {R1_diag[INDEX[(2,1)]]}, R^(2)[(2,1)] = {R2_diag[INDEX[(2,1)]]}",
)


# =============================================================================
section("Part 4 (T4): positivity, self-adjointness, conjugation-symmetry of R")
# =============================================================================
# Under the abstract hypotheses rho >= 0 and rho_(p,q) = rho_(q,p), R is a
# diagonal operator with non-negative real eigenvalues. In the Schur-orthonormal
# character basis, R is diagonal with real entries, hence self-adjoint. The
# separate condition rho_(0,0) = 1 fixes the trivial-channel normalization in T2.
R_matrix = np.diag([float(r) for r in rho1])
swap_matrix = np.zeros_like(R_matrix)
for i, (p, q) in enumerate(B_N):
    swap_matrix[INDEX[(q, p)], i] = 1.0

# Positivity
rho_min = min(R_matrix.diagonal())
check(
    "(T4) R is positive: rho_(p,q) >= 0 on every weight in B_4",
    rho_min >= 0,
    detail=f"min rho = {rho_min} >= 0",
)

# Self-adjointness (R is real diagonal -> trivially R = R^T = R^*)
sa_err = float(np.max(np.abs(R_matrix - R_matrix.T)))
check(
    "(T4) R is self-adjoint (diagonal with real entries)",
    sa_err < 1e-15,
    detail=f"||R - R^T||_inf = {sa_err:.3e}",
)

# Conjugation symmetry: R commutes with the swap involution
commute_err = float(np.max(np.abs(swap_matrix @ R_matrix - R_matrix @ swap_matrix)))
check(
    "(T4) R commutes with the conjugation swap (p,q) <-> (q,p)",
    commute_err < 1e-15,
    detail=f"||[swap, R]||_inf = {commute_err:.3e}",
)

# Trivial-channel normalization used in T2
norm_err = abs(float(rho1[INDEX[(0, 0)]]) - 1.0)
check(
    "(T2) Trivial-channel normalization: rho_(0,0) = 1 exactly",
    norm_err < 1e-15,
    detail=f"|rho_(0,0) - 1| = {norm_err:.3e}",
)


# =============================================================================
section("Part 5: concrete instance — trivial coefficient sequence collapses to projection")
# =============================================================================
# (rho_(p,q)) = (1, 0, 0, ..., 0): the operator R is the rank-1 projection onto
# chi_(0,0). This is a degenerate but valid instance of the abstract hypotheses
# (rho >= 0, rho_(p,q) = rho_(q,p) since both sides are 0 off the trivial irrep,
# and rho_(0,0) = 1).
rho_trivial = [Fraction(0)] * len(B_N)
rho_trivial[INDEX[(0, 0)]] = Fraction(1)
# Check that C_{Z/Z_(0,0)} chi_(0,0) = 1 * chi_(0,0) and = 0 for any other (p,q).
ok_trivial = True
for target in B_N:
    actual = apply_z_convolution(rho_trivial, target)
    expected = expected_diagonal_polynomial(rho_trivial, target)
    if actual != expected:
        ok_trivial = False
check(
    "concrete trivial instance: rho = (1, 0, ..., 0) gives projection onto chi_(0,0)",
    ok_trivial,
    detail="C_{Z/Z_(0,0)} chi_(p,q) = 1 if (p,q)=(0,0) else 0",
)


# =============================================================================
section("Part 6: independent deterministic Haar-SU(3) convolution check")
# =============================================================================
# The Monte Carlo convolution below is independent of the Weyl integration
# routine and symbolic contraction table. It samples Haar-random 3 x 3 SU(3)
# matrices and evaluates explicit trace formulas for 1, 3, 3bar, 8, 6, 6bar,
# 10, and 10bar. A small preflight separately cross-checks those formulas
# against the Weyl formula at fixed torus points.
MC_WEIGHTS = (
    (0, 0),
    (1, 0),
    (0, 1),
    (1, 1),
    (2, 0),
    (0, 2),
    (3, 0),
    (0, 3),
)
MC_RHO = {
    (0, 0): 1.0,
    (1, 0): 2.0 / 5.0,
    (0, 1): 2.0 / 5.0,
    (1, 1): 1.0 / 7.0,
    (2, 0): 1.0 / 8.0,
    (0, 2): 1.0 / 8.0,
    (3, 0): 1.0 / 20.0,
    (0, 3): 1.0 / 20.0,
}


def explicit_character_table(matrices: np.ndarray) -> np.ndarray:
    """Explicit low-irrep SU(3) characters for one matrix or a batch."""
    matrices = np.asarray(matrices, dtype=complex)
    tr1 = np.trace(matrices, axis1=-2, axis2=-1)
    matrices2 = matrices @ matrices
    tr2 = np.trace(matrices2, axis1=-2, axis2=-1)
    matrices3 = matrices2 @ matrices
    tr3 = np.trace(matrices3, axis1=-2, axis2=-1)

    chi20 = (tr1**2 + tr2) / 2.0
    chi30 = (tr1**3 + 3.0 * tr1 * tr2 + 2.0 * tr3) / 6.0
    values = {
        (0, 0): np.ones_like(tr1),
        (1, 0): tr1,
        (0, 1): np.conjugate(tr1),
        (1, 1): tr1 * np.conjugate(tr1) - 1.0,
        (2, 0): chi20,
        (0, 2): np.conjugate(chi20),
        (3, 0): chi30,
        (0, 3): np.conjugate(chi30),
    }
    return np.stack([values[weight] for weight in MC_WEIGHTS], axis=-1)


def deterministic_haar_su3(sample_count: int, seed: int) -> np.ndarray:
    """Ginibre-QR sampler for deterministic Haar-random SU(3) matrices."""
    rng = np.random.default_rng(seed)
    samples = np.empty((sample_count, 3, 3), dtype=complex)
    for sample_index in range(sample_count):
        ginibre = (
            rng.normal(size=(3, 3))
            + 1j * rng.normal(size=(3, 3))
        )
        q_matrix, r_matrix = np.linalg.qr(ginibre)
        diagonal = np.diag(r_matrix)
        phases = diagonal / np.abs(diagonal)
        q_matrix = q_matrix @ np.diag(phases)
        determinant = np.linalg.det(q_matrix)
        determinant_root = np.exp(np.log(determinant) / 3.0)
        samples[sample_index] = q_matrix / determinant_root
    return samples


identity_characters = explicit_character_table(np.eye(3, dtype=complex))
expected_dimensions = np.array([d_su3(*weight) for weight in MC_WEIGHTS], dtype=float)
check(
    "explicit low-irrep character formulas reproduce their dimensions at the identity",
    np.max(np.abs(identity_characters - expected_dimensions)) < 1e-12,
    detail=f"dimensions={expected_dimensions.astype(int).tolist()}",
)

formula_crosscheck_error = 0.0
for t1, t2 in ((0.37, 0.91), (0.4, 1.4), (1.1, -0.23)):
    diagonal_matrix = np.diag(
        np.exp(1j * np.array([t1, t2, -t1 - t2]))
    )
    explicit_values = explicit_character_table(diagonal_matrix)
    for index, weight in enumerate(MC_WEIGHTS):
        formula_crosscheck_error = max(
            formula_crosscheck_error,
            abs(explicit_values[index] - weyl_chi(*weight, t1, t2)),
        )
check(
    "explicit character formulas agree with the independent Weyl formula on hostile torus points",
    formula_crosscheck_error < 1e-10,
    detail=f"max formula disagreement={formula_crosscheck_error:.3e}",
)

MC_SAMPLE_COUNT = 40_000
haar_samples = deterministic_haar_su3(MC_SAMPLE_COUNT, seed=20260716)
identity3 = np.eye(3, dtype=complex)
unitarity_error = float(
    np.max(
        np.abs(
            haar_samples @ np.swapaxes(np.conjugate(haar_samples), 1, 2)
            - identity3
        )
    )
)
determinant_error = float(np.max(np.abs(np.linalg.det(haar_samples) - 1.0)))
check(
    "deterministic Ginibre-QR samples lie in SU(3)",
    unitarity_error < 1e-12 and determinant_error < 1e-12,
    detail=f"max unitary err={unitarity_error:.3e}, max det err={determinant_error:.3e}",
)

sample_characters = explicit_character_table(haar_samples)
z_coefficients = np.array(
    [d_su3(*weight) * MC_RHO[weight] for weight in MC_WEIGHTS],
    dtype=float,
)
test_matrices = (
    np.diag(np.exp(1j * np.array([0.4, 1.4, -1.8]))),
    np.diag(np.exp(1j * np.array([0.3, 0.7, -1.0]))),
    deterministic_haar_su3(1, seed=314159)[0],
)

mc_records: list[dict[str, np.ndarray]] = []
max_mc_error = 0.0
max_mc_sigma = 0.0
for test_matrix in test_matrices:
    translated = np.einsum(
        "ab,nbc->nac",
        test_matrix,
        np.swapaxes(np.conjugate(haar_samples), 1, 2),
    )
    z_values = explicit_character_table(translated) @ z_coefficients
    integrands = z_values[:, None] * sample_characters
    estimates = np.mean(integrands, axis=0)
    standard_errors = np.sqrt(
        np.mean(np.abs(integrands - estimates) ** 2, axis=0)
        / MC_SAMPLE_COUNT
    )
    test_characters = explicit_character_table(test_matrix)
    expected_values = np.array(
        [
            MC_RHO[weight] * test_characters[index]
            for index, weight in enumerate(MC_WEIGHTS)
        ]
    )
    errors = np.abs(estimates - expected_values)
    max_mc_error = max(max_mc_error, float(np.max(errors)))
    max_mc_sigma = max(
        max_mc_sigma,
        float(np.max(errors / np.maximum(standard_errors, 1e-15))),
    )
    mc_records.append(
        {
            "matrix": test_matrix,
            "z_values": z_values,
            "estimates": estimates,
            "standard_errors": standard_errors,
            "expected_values": expected_values,
        }
    )

mc_convolution_ok = all(
    np.all(
        np.abs(record["estimates"] - record["expected_values"])
        <= 6.0 * record["standard_errors"] + 5.0e-3
    )
    for record in mc_records
)
check(
    "(T2) independent Haar-SU(3) convolution matches rho_mu chi_mu(V)",
    mc_convolution_ok,
    detail=(
        f"{len(test_matrices)} V values x {len(MC_WEIGHTS)} irreps, "
        f"samples={MC_SAMPLE_COUNT}, max err={max_mc_error:.3e}, "
        f"max normalized err={max_mc_sigma:.2f} sigma"
    ),
)

# Convention-hostile controls use the complex fundamental character at the
# first test matrix, where chi_(1,0)(V) != chi_(0,1)(V). Replacing W^-1 by W,
# or conjugating chi_mu(W), sends the result to the dual irrep instead.
fundamental_index = MC_WEIGHTS.index((1, 0))
antifundamental_index = MC_WEIGHTS.index((0, 1))
hostile_record = mc_records[0]
hostile_matrix = hostile_record["matrix"]
correct_fundamental = hostile_record["expected_values"][fundamental_index]
dual_fundamental = (
    MC_RHO[(0, 1)]
    * explicit_character_table(hostile_matrix)[antifundamental_index]
)

wrong_inverse_translated = np.einsum(
    "ab,nbc->nac",
    hostile_matrix,
    haar_samples,
)
wrong_inverse_z = explicit_character_table(wrong_inverse_translated) @ z_coefficients
wrong_inverse_integrand = wrong_inverse_z * sample_characters[:, fundamental_index]
wrong_inverse_estimate = np.mean(wrong_inverse_integrand)
wrong_inverse_se = np.sqrt(
    np.mean(np.abs(wrong_inverse_integrand - wrong_inverse_estimate) ** 2)
    / MC_SAMPLE_COUNT
)
check(
    "hostile control rejects W in place of W^-1",
    abs(wrong_inverse_estimate - correct_fundamental) > 8.0 * wrong_inverse_se
    and abs(wrong_inverse_estimate - dual_fundamental) <= 6.0 * wrong_inverse_se + 5.0e-3,
    detail=(
        f"mutant is {abs(wrong_inverse_estimate - correct_fundamental) / wrong_inverse_se:.1f} "
        "sigma from rho_(1,0) chi_(1,0)(V) and tracks the dual character"
    ),
)

wrong_conjugate_integrand = (
    hostile_record["z_values"]
    * np.conjugate(sample_characters[:, fundamental_index])
)
wrong_conjugate_estimate = np.mean(wrong_conjugate_integrand)
wrong_conjugate_se = np.sqrt(
    np.mean(np.abs(wrong_conjugate_integrand - wrong_conjugate_estimate) ** 2)
    / MC_SAMPLE_COUNT
)
check(
    "hostile control rejects conjugating the target character chi_mu(W)",
    abs(wrong_conjugate_estimate - correct_fundamental) > 8.0 * wrong_conjugate_se
    and abs(wrong_conjugate_estimate - dual_fundamental) <= 6.0 * wrong_conjugate_se + 5.0e-3,
    detail=(
        f"mutant is {abs(wrong_conjugate_estimate - correct_fundamental) / wrong_conjugate_se:.1f} "
        "sigma from the claimed fundamental action and tracks the antifundamental"
    ),
)

# A lookup-only helper returns rho_target and loses chi_target(V). The second
# matrix makes that failure large and compares it directly with the independently
# estimated convolution value.
lookup_record = mc_records[1]
lookup_only_mutant = MC_RHO[(1, 0)]
lookup_estimate = lookup_record["estimates"][fundamental_index]
lookup_se = lookup_record["standard_errors"][fundamental_index]
check(
    "hostile control rejects a convolution helper that merely returns rho_target",
    abs(lookup_estimate - lookup_only_mutant) > 8.0 * lookup_se,
    detail=(
        f"lookup-only value={lookup_only_mutant:.6f}, Haar estimate={lookup_estimate:.6f}, "
        f"separation={abs(lookup_estimate - lookup_only_mutant) / lookup_se:.1f} sigma"
    ),
)


# =============================================================================
section("Narrow theorem summary")
# =============================================================================
print("""
  Narrow B_4 theorem statement:

  HYPOTHESIS:
    Fix N = 4 with B_4 = {(p, q) : 0 <= p, q <= 4}.
    Let (rho_(p,q))_(p,q in B_4) be an abstract real sequence with:
      rho_(p,q) >= 0,
      rho_(p,q) = rho_(q,p),
      rho_(0,0) = 1.
    Define
      R chi_(p,q) = rho_(p,q) chi_(p,q),
      Z(W)       = sum_(p,q in B_4) d_(p,q) rho_(p,q) chi_(p,q)(W),
      Z_(0,0)    = d_(0,0) rho_(0,0) = 1,
      C_{Z/Z_(0,0)} f (V) = int_{SU(3)} (Z(V W^{-1}) / Z_(0,0)) f(W) dW,
      with normalized Haar probability measure dW.

  CONCLUSION:
    (T1)  Schur character orthogonality on B_4:
              <chi_(p,q), chi_(p',q')>_Haar
                 = int_{SU(3)} chi_(p,q)(W) conj(chi_(p',q')(W)) dW
                 = delta_((p,q),(p',q')).

    (T2)  Diagonal-action identity:
              C_{Z/Z_(0,0)} chi_(p,q) = rho_(p,q) chi_(p,q)  on V_4.

    (T3)  Coefficient uniqueness:
              R^(1) = R^(2)  iff  rho^(1) = rho^(2) on B_4.

    (T4)  R is positive, self-adjoint (in the Schur-orthonormal character basis),
          and commutes with the conjugation swap (p,q) <-> (q,p).

  INPUT AND AUTHORITY SURFACE:
    The complete input is the finite B_4 SU(3) character basis, normalized
    Haar probability measure, an abstract real nonnegative swap-symmetric
    sequence with rho_(0,0) = 1, and standard compact-group representation
    algebra.

  OUTPUT SURFACE:
    T1 Schur orthogonality; T2 equality of normalized convolution and diagonal
    action on V_4; T3 coefficient uniqueness; T4 positivity,
    self-adjointness, and swap symmetry.

  PARENT PROGRAM DIVISION OF LABOR:
    A physical Wilson-environment coefficient result supplies the sequence
    with its own source authority. This theorem supplies the algebraic
    convolution/diagonal equivalence after that typed input is present.
""")


print(f"\n{'='*88}\n  TOTAL: PASS={PASS}, FAIL={FAIL}\n{'='*88}")
print(f"PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL > 0 else 0)
