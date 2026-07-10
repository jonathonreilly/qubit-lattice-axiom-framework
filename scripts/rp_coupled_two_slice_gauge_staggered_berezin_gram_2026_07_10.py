#!/usr/bin/env python3
"""Coupled two-slice SU(3) + staggered Berezin/OS Gram checks.

Paired note:
RP_COUPLED_TWO_SLICE_GAUGE_STAGGERED_BEREZIN_GRAM_NARROW_THEOREM_NOTE_2026-07-10.md
"""

from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
import sys

import numpy as np


AUDIT_TIMEOUT_SEC = 600

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import su3_wilson_plane_kernel_character_positivity_composed_gram_2026_07_09 as su3_supplier


PASS = 0
FAIL = 0
MASS_EXACT = Fraction(1, 1)
MASS_MC = 4.0 / 5.0
BETA_MC = 3.0 / 4.0
N_SAMPLES = 100_000
N_BATCHES = 10
RNG = np.random.default_rng(20260710)
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if bool(cond):
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {name}{suffix}")
    return bool(cond)


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


# ---------------------------------------------------------------------------
# Exact exterior algebra over Fraction coefficients.
# A monomial is the increasing tuple of occupied generator indices.
# ---------------------------------------------------------------------------
def exterior_wedge(left, right):
    if set(left).intersection(right):
        return None, 0
    inversions = sum(a > b for a in left for b in right)
    return tuple(sorted(left + right)), (-1 if inversions % 2 else 1)


def exterior_add(left, right):
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = out.get(monomial, Fraction(0, 1)) + coefficient
        if out[monomial] == 0:
            del out[monomial]
    return out


def exterior_scale(poly, scalar):
    return {monomial: scalar * coefficient for monomial, coefficient in poly.items() if scalar * coefficient}


def exterior_mul(left, right):
    out = {}
    for monomial_left, coefficient_left in left.items():
        for monomial_right, coefficient_right in right.items():
            monomial, sign = exterior_wedge(monomial_left, monomial_right)
            if monomial is not None:
                out[monomial] = out.get(monomial, Fraction(0, 1)) + (
                    sign * coefficient_left * coefficient_right
                )
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def exterior_generator(index):
    return {(index,): Fraction(1, 1)}


ONE = {(): Fraction(1, 1)}


def nilpotent_factor(left, right, coefficient):
    return exterior_add(ONE, exterior_scale(exterior_mul(left, right), coefficient))


def bareiss_determinant(matrix):
    """Exact determinant with fraction-free Bareiss elimination."""
    n = len(matrix)
    if n == 0:
        return Fraction(1, 1)
    work = [list(row) for row in matrix]
    sign = 1
    previous = Fraction(1, 1)
    for pivot_index in range(n - 1):
        pivot_row = next(
            (row for row in range(pivot_index, n) if work[row][pivot_index] != 0),
            None,
        )
        if pivot_row is None:
            return Fraction(0, 1)
        if pivot_row != pivot_index:
            work[pivot_index], work[pivot_row] = work[pivot_row], work[pivot_index]
            sign *= -1
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, n):
            for column in range(pivot_index + 1, n):
                work[row][column] = (
                    work[row][column] * pivot
                    - work[row][pivot_index] * work[pivot_index][column]
                ) / previous
        previous = pivot
        for row in range(pivot_index + 1, n):
            work[row][pivot_index] = Fraction(0, 1)
    return sign * work[-1][-1]


def principal_minors(matrix):
    minors = []
    for size in range(1, len(matrix) + 1):
        for indices in itertools.combinations(range(len(matrix)), size):
            submatrix = [[matrix[row][column] for column in indices] for row in indices]
            minors.append((indices, bareiss_determinant(submatrix)))
    return minors


def fraction_matrix_text(matrix):
    return "[" + ",\n   ".join("[" + ", ".join(str(value) for value in row) + "]" for row in matrix) + "]"


def exact_weight(n_sites: int, crossing_sign: int = 1):
    """Return exp(-S) for independent massive crossing pairs.

    Generator order per site is (bar0, chi0, bar1, chi1).  The retained
    temporal matrix convention is M_01=+1/2, M_10=-1/2, hence
    exp(-S_cross)=(1+bar1 chi0/2)(1-bar0 chi1/2).  crossing_sign=-1
    flips the relative sign by replacing M_10=-1/2 with M_10=+1/2.
    """
    weight = ONE
    for site in range(n_sites):
        offset = 4 * site
        bar0, chi0, bar1, chi1 = [exterior_generator(offset + index) for index in range(4)]
        site_weight = nilpotent_factor(bar0, chi0, -MASS_EXACT)
        site_weight = exterior_mul(site_weight, nilpotent_factor(bar1, chi1, -MASS_EXACT))
        relative_coefficient = Fraction(1 if crossing_sign == 1 else -1, 2)
        site_weight = exterior_mul(
            site_weight,
            nilpotent_factor(bar1, chi0, relative_coefficient),
        )
        site_weight = exterior_mul(
            site_weight,
            nilpotent_factor(bar0, chi1, Fraction(-1, 2)),
        )
        weight = exterior_mul(weight, site_weight)
    return weight


def exact_theta(monomial, n_sites: int, phased: bool = True, site_reflection: bool = False):
    """Antilinear antiautomorphism on a real-coefficient monomial."""
    phase = Fraction(-1 if phased else 1, 1)
    mapping = {}
    if site_reflection:
        for site in range(n_sites):
            offset = 4 * site
            mapping[offset] = offset + 1
            mapping[offset + 1] = offset
    else:
        for site in range(n_sites):
            offset = 4 * site
            mapping[offset + 2] = offset + 1
            mapping[offset + 3] = offset
    out = ONE
    for generator in reversed(monomial):
        out = exterior_mul(out, {(mapping[generator],): phase})
    return out


def exact_gram(basis, n_sites: int, crossing_sign: int = 1, phased: bool = True, site_reflection: bool = False):
    weight = exact_weight(n_sites, crossing_sign=crossing_sign)
    top = tuple(range(4 * n_sites))
    gram = []
    for left in basis:
        row = []
        theta_left = exact_theta(left, n_sites, phased=phased, site_reflection=site_reflection)
        for right in basis:
            integrand = exterior_mul(exterior_mul(theta_left, {right: Fraction(1, 1)}), weight)
            # With product dbar0 dchi0 dbar1 dchi1 at each site, the top
            # coefficient has integration sign (+1): there are 2*n_sites pairs.
            row.append(integrand.get(top, Fraction(0, 1)))
        gram.append(row)
    return gram


def run_exact_blocks():
    section("BLOCK 1: one-site, one-color exact Berezin Gram")
    basis = [(), (2,), (3,), (2, 3)]
    gram = exact_gram(basis, 1)
    minors = principal_minors(gram)
    print("  basis = {1, bar_chi_1, chi_1, bar_chi_1 chi_1}, m=1")
    print("  Gram =")
    print("   " + fraction_matrix_text(gram).replace("\n", "\n   "))
    print("  principal minors = " + ", ".join(str(value) for _, value in minors))
    check("toy Gram is exactly Hermitian", gram == [list(row) for row in zip(*gram)])
    check(
        "all toy principal minors are nonnegative exact rationals",
        all(value >= 0 for _, value in minors),
        f"min principal minor={min(value for _, value in minors)}",
    )
    check(
        "toy Gram matches the sign-fixing anchor",
        gram
        == [
            [Fraction(5, 4), 0, 0, -1],
            [0, Fraction(1, 2), 0, 0],
            [0, 0, Fraction(1, 2), 0],
            [-1, 0, 0, 1],
        ],
    )

    section("BLOCK 2: exact sign and reflection falsifiers")
    wrong_crossing = exact_gram(basis, 1, crossing_sign=-1)
    wrong_crossing_min = min(value for _, value in principal_minors(wrong_crossing))
    check(
        "flipped relative temporal-hop sign is decisively non-PSD",
        wrong_crossing_min < 0,
        f"min exact principal minor={wrong_crossing_min}",
    )

    # On the complex-rescaled complete basis {i*1, bar, chi, bar chi}, a
    # reflection that does not conjugate scalar coefficients multiplies both
    # legs of G_00 by i and gives -G_00=-5/4 exactly.  It also sends the
    # (0,3) and (3,0) entries to the same -i, so the matrix is non-Hermitian.
    no_conjugation_negative_diagonal = -gram[0][0]
    no_conjugation_nonhermitian = gram[0][3] != 0
    check(
        "theta without scalar conjugation fails on the complex complete basis",
        no_conjugation_negative_diagonal < 0 and no_conjugation_nonhermitian,
        "wrong G_00=-5/4 and wrong G_03=G_30=-i (non-Hermitian)",
    )

    site_basis = [(), (0,), (1,), (0, 1)]
    site_gram = exact_gram(site_basis, 1, site_reflection=True, phased=False)
    site_min = min(value for _, value in principal_minors(site_gram))
    check(
        "site-reflection plane on slice 0 is non-PSD",
        site_min < 0,
        f"min exact principal minor={site_min}",
    )

    section("BLOCK 3: two-site, one-color exact tensor test")
    # Plus generators in per-site order are (2,3,6,7).  The selected basis
    # contains all one-generator legs and three genuinely cross-site products.
    masks = (0, 1, 2, 4, 8, 5, 10, 15)
    plus_generators = (2, 3, 6, 7)
    basis_two = [
        tuple(plus_generators[index] for index in range(4) if mask & (1 << index))
        for mask in masks
    ]
    gram_two = exact_gram(basis_two, 2)
    minors_two = principal_minors(gram_two)
    print(f"  basis masks={masks}; principal minors checked={len(minors_two)}")
    check("two-site exact Gram is Hermitian", gram_two == [list(row) for row in zip(*gram_two)])
    check(
        "two-site exact Gram is PSD by every exact principal minor",
        all(value >= 0 for _, value in minors_two),
        f"min principal minor={min(value for _, value in minors_two)}",
    )
    return gram


# ---------------------------------------------------------------------------
# Coupled SU(3) + staggered Monte Carlo.  Gauge links are sampled exactly as
# supplier.composed_mc: four independent Haar arrays per batch.  Fermions are
# integrated analytically per configuration by determinant/inverse Wick data.
# ---------------------------------------------------------------------------
def trace_product_real(left, right):
    return np.real(np.einsum("nij,nji->n", left, right, optimize=True))


def trace_cross_real(left, right):
    return np.real(np.einsum("nij,nij->n", left, np.conj(right), optimize=True))


def build_staggered_matrix(u0, u1, mass: float, crossing_sign: int = 1):
    batch = len(u0[0])
    n_slice = 6
    matrix = np.zeros((batch, 2 * n_slice, 2 * n_slice), dtype=np.complex128)
    links_by_time = ((u0, +1.0), (u1, -1.0))
    for time, (links, eta) in enumerate(links_by_time):
        offset = time * n_slice
        for x in range(2):
            neighbor = 1 - x
            forward = links[x]
            backward = np.conj(np.swapaxes(links[neighbor], 1, 2))
            rows = slice(offset + 3 * x, offset + 3 * (x + 1))
            columns = slice(offset + 3 * neighbor, offset + 3 * (neighbor + 1))
            matrix[:, rows, columns] += 0.5 * eta * (forward - backward)
    identity = np.arange(n_slice)
    matrix[:, identity, n_slice + identity] = 0.5
    matrix[:, n_slice + identity, identity] = -0.5 if crossing_sign == 1 else 0.5
    massive = matrix.copy()
    diagonal = np.arange(2 * n_slice)
    massive[:, diagonal, diagonal] += mass
    return matrix, massive


def slice_observables(u_left, u_right):
    """Return c+A bilinear data for 14 mixed plus-algebra observables."""
    batch = len(u_left)
    nobs = 14
    n_slice = 6
    constants = np.zeros((batch, nobs), dtype=np.complex128)
    matrices = np.zeros((batch, nobs, n_slice, n_slice), dtype=np.complex128)
    tr_left = np.trace(u_left, axis1=1, axis2=2)
    tr_right = np.trace(u_right, axis1=1, axis2=2)
    tr_loop = np.einsum("nij,nji->n", u_left, u_right, optimize=True)

    constants[:, 0] = 1.0
    constants[:, 1] = tr_left
    constants[:, 2] = tr_right
    constants[:, 3] = tr_loop
    constants[:, 4] = np.conj(tr_left)

    identity = np.eye(n_slice, dtype=np.complex128)
    projector0 = np.zeros((n_slice, n_slice), dtype=np.complex128)
    projector0[:3, :3] = np.eye(3)
    matrices[:, 5] = identity
    matrices[:, 6] = projector0
    matrices[:, 7, :3, 3:] = u_left
    matrices[:, 8, 3:, :3] = u_right
    matrices[:, 9, :3, :3] = np.einsum("nij,njk->nik", u_left, u_right, optimize=True)

    matrices[:, 10] = tr_left[:, None, None] * identity
    matrices[:, 11, :3, 3:] = tr_loop[:, None, None] * u_left
    matrices[:, 12] = (0.5 + 0.25j) * tr_right[:, None, None] * projector0
    matrices[:, 12, 3:, :3] += np.conj(tr_left)[:, None, None] * u_right
    constants[:, 13] = tr_left + (0.2 - 0.1j) * tr_right
    matrices[:, 13, :3, 3:] = (0.3 + 0.2j) * tr_right[:, None, None] * u_left
    scales = np.asarray([1.0] + [0.5] * 4 + [0.2] * 5 + [0.1] * 4)
    constants *= scales[None, :]
    matrices *= scales[None, :, None, None]
    return constants, matrices


def fermion_gram_samples(inverse, constants_minus, matrices_minus, constants_plus, matrices_plus, conjugate_reflection=True):
    n_slice = inverse.shape[1] // 2
    c00 = inverse[:, :n_slice, :n_slice]
    c01 = inverse[:, :n_slice, n_slice:]
    c10 = inverse[:, n_slice:, :n_slice]
    c11 = inverse[:, n_slice:, n_slice:]

    if conjugate_reflection:
        reflected_constants = np.conj(constants_minus)
        reflected_matrices = np.conj(np.swapaxes(matrices_minus, -1, -2))
    else:
        reflected_constants = constants_minus
        reflected_matrices = np.swapaxes(matrices_minus, -1, -2)

    trace_minus = np.einsum("bnij,bji->bn", reflected_matrices, c00, optimize=True)
    trace_plus = np.einsum("bnij,bji->bn", matrices_plus, c11, optimize=True)
    left_products = np.einsum("bnij,bjk->bnik", reflected_matrices, c01, optimize=True)
    right_products = np.einsum("bnij,bjk->bnik", matrices_plus, c10, optimize=True)
    crossed = np.einsum("bipq,bjqp->bij", left_products, right_products, optimize=True)
    one_point_minus = reflected_constants - trace_minus
    one_point_plus = constants_plus - trace_plus
    return np.einsum("bi,bj->bij", one_point_minus, one_point_plus, optimize=True) - crossed


class GramAccumulator:
    def __init__(self, nobs):
        self.numerator = np.zeros((nobs, nobs), dtype=np.complex128)
        self.denominator = 0.0
        self.batch_grams = []

    def add(self, sample_weights, sample_grams):
        numerator = np.einsum("b,bij->ij", sample_weights, sample_grams, optimize=True)
        denominator = float(np.real(np.sum(sample_weights)))
        self.numerator += numerator
        self.denominator += denominator
        self.batch_grams.append(numerator / denominator)

    def result(self):
        gram = self.numerator / self.denominator
        batches = np.asarray(self.batch_grams)
        entry_error = np.std(batches, axis=0, ddof=1) / math.sqrt(len(batches))
        mc_noise = float(np.max(np.abs(entry_error)))
        herm_err = float(np.max(np.abs(gram - gram.conj().T)))
        hermitian = (gram + gram.conj().T) / 2.0
        return {
            "gram": gram,
            "hermitian": hermitian,
            "eigenvalues": np.linalg.eigvalsh(hermitian),
            "mc_noise": mc_noise,
            "herm_err": herm_err,
            "batch_grams": batches,
        }


def run_coupled_mc():
    section("BLOCKS 4-6: coupled d=1, L_s=2, N_c=3 Haar x exact-Wick Monte Carlo")
    assert N_SAMPLES >= 100_000 and N_SAMPLES % N_BATCHES == 0
    batch_size = N_SAMPLES // N_BATCHES
    baseline = GramAccumulator(14)
    wrong_crossing = GramAccumulator(14)
    no_conjugation = GramAccumulator(14)
    max_antihermiticity = 0.0
    max_det_imag = 0.0
    min_det_real = math.inf

    for batch_index in range(N_BATCHES):
        # Same four-link Haar sampling and ten-batch structure as supplier.composed_mc.
        u10 = su3_supplier.haar_su3(batch_size, RNG)
        u20 = su3_supplier.haar_su3(batch_size, RNG)
        u11 = su3_supplier.haar_su3(batch_size, RNG)
        u21 = su3_supplier.haar_su3(batch_size, RNG)
        bminus = BETA_MC * trace_product_real(u10, u20)
        bplus = BETA_MC * trace_product_real(u11, u21)
        crossing_gauge = BETA_MC * (
            trace_cross_real(u10, u11) + trace_cross_real(u20, u21)
        )
        gauge_weight = np.exp(bminus + bplus + crossing_gauge)

        hopping, massive = build_staggered_matrix((u10, u20), (u11, u21), MASS_MC)
        wrong_hopping, wrong_massive = build_staggered_matrix(
            (u10, u20), (u11, u21), MASS_MC, crossing_sign=-1
        )
        max_antihermiticity = max(
            max_antihermiticity,
            float(np.max(np.abs(hopping + np.conj(np.swapaxes(hopping, 1, 2))))),
        )
        determinants = np.linalg.det(massive)
        wrong_determinants = np.linalg.det(wrong_massive)
        max_det_imag = max(max_det_imag, float(np.max(np.abs(np.imag(determinants)))))
        min_det_real = min(min_det_real, float(np.min(np.real(determinants))))
        inverse = np.linalg.inv(massive)
        wrong_inverse = np.linalg.inv(wrong_massive)

        constants_minus, matrices_minus = slice_observables(u10, u20)
        constants_plus, matrices_plus = slice_observables(u11, u21)
        sample_baseline = fermion_gram_samples(
            inverse,
            constants_minus,
            matrices_minus,
            constants_plus,
            matrices_plus,
            conjugate_reflection=True,
        )
        sample_wrong_crossing = fermion_gram_samples(
            wrong_inverse,
            constants_minus,
            matrices_minus,
            constants_plus,
            matrices_plus,
            conjugate_reflection=True,
        )
        sample_no_conjugation = fermion_gram_samples(
            inverse,
            constants_minus,
            matrices_minus,
            constants_plus,
            matrices_plus,
            conjugate_reflection=False,
        )
        baseline.add(gauge_weight * np.real(determinants), sample_baseline)
        wrong_crossing.add(gauge_weight * np.real(wrong_determinants), sample_wrong_crossing)
        no_conjugation.add(gauge_weight * np.real(determinants), sample_no_conjugation)
        print(f"  completed batch {batch_index + 1}/{N_BATCHES}")

    result = baseline.result()
    wrong_result = wrong_crossing.result()
    no_conjugation_result = no_conjugation.result()
    minimum = float(result["eigenvalues"][0])
    allowance = 3.0 * result["mc_noise"]
    wrong_minimum = float(wrong_result["eigenvalues"][0])
    wrong_allowance = 3.0 * wrong_result["mc_noise"]
    no_conj_minimum = float(no_conjugation_result["eigenvalues"][0])
    no_conj_allowance = 3.0 * no_conjugation_result["mc_noise"]

    print(
        "  BLOCK 4 baseline: "
        f"min_eig={minimum:+.6e}, mc_noise={result['mc_noise']:.3e}, "
        f"3*mc_noise={allowance:.3e}, herm_err={result['herm_err']:.3e}"
    )
    print("  baseline eigenvalues=" + np.array2string(result["eigenvalues"], precision=6))
    check(
        "BLOCK 4 coupled mixed Gram is PSD within 3*mc_noise",
        minimum >= -allowance,
        f"min eig={minimum:+.6e}, negative allowance={allowance:.3e}",
    )
    check(
        "BLOCK 4 Hermiticity residual is sampling-sized",
        result["herm_err"] <= 10.0 * result["mc_noise"],
        f"herm_err={result['herm_err']:.3e}, allowance={10.0 * result['mc_noise']:.3e}",
    )
    check(
        "BLOCK 4 sampling noise is controlled",
        result["mc_noise"] < 0.05,
        f"mc_noise={result['mc_noise']:.3e}",
    )

    print(
        "  BLOCK 5 flipped crossing: "
        f"min_eig={wrong_minimum:+.6e}, mc_noise={wrong_result['mc_noise']:.3e}, "
        f"3*mc_noise={wrong_allowance:.3e}"
    )
    print(
        "  BLOCK 5 no conjugation: "
        f"min_eig={no_conj_minimum:+.6e}, mc_noise={no_conjugation_result['mc_noise']:.3e}, "
        f"3*mc_noise={no_conj_allowance:.3e}, herm_err={no_conjugation_result['herm_err']:.3e}"
    )
    check(
        "BLOCK 5 flipped crossing-hop sign is decisively non-PSD",
        wrong_minimum < -wrong_allowance and wrong_minimum < -1e-3,
        f"min eig={wrong_minimum:+.6e}, decisive threshold={-max(wrong_allowance, 1e-3):+.3e}",
    )
    check(
        "BLOCK 5 no-conjugation reflection is decisively non-PSD",
        no_conj_minimum < -no_conj_allowance and no_conj_minimum < -1e-3,
        f"min eig={no_conj_minimum:+.6e}, decisive threshold={-max(no_conj_allowance, 1e-3):+.3e}",
    )

    check(
        "BLOCK 6 staggered hopping matrix is anti-Hermitian",
        max_antihermiticity < 1e-12,
        f"max ||M+M^dag||_max={max_antihermiticity:.3e}",
    )
    check(
        "BLOCK 6 det(M+mI) is real and strictly positive per sample",
        max_det_imag < 1e-9 and min_det_real > 0.0,
        f"max |Im det|={max_det_imag:.3e}, min Re det={min_det_real:.6e}",
    )
    return {
        "baseline": result,
        "wrong_crossing": wrong_result,
        "no_conjugation": no_conjugation_result,
    }


def run_ledger_guard():
    section("BLOCK 7: retained dependency-status guard")
    rows = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))["rows"]
    required = {
        "su3_wilson_plane_kernel_character_positivity_and_composed_gram_narrow_theorem_note_2026-07-09": "positive_theorem",
        "gauge_temporal_gauge_mixed_kernel_spatial_link_factorization_narrow_theorem_note_2026-05-10": "positive_theorem",
        "staggered_only_det_positivity_case_a_note_2026-05-17": "positive_theorem",
        "axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28": "bounded_theorem",
    }
    retained = {"retained", "retained_bounded", "retained_no_go"}
    details = []
    ok = True
    for claim_id, claim_type in required.items():
        row = rows.get(claim_id)
        row_ok = bool(
            row
            and row.get("claim_type") == claim_type
            and row.get("audit_status") == "audited_clean"
            and row.get("effective_status") in retained
        )
        ok = ok and row_ok
        details.append(
            f"{claim_id}:"
            + ("missing" if row is None else f"{row.get('audit_status')}/{row.get('effective_status')}")
        )
    check("all four load-bearing dependency rows are clean retained-grade", ok, "; ".join(details))


def main() -> int:
    print("Coupled two-slice SU(3) + staggered Berezin/OS Gram runner")
    print(
        f"parameters: d=1 L_s=2 N_c=3 beta={BETA_MC} m={MASS_MC} "
        f"samples={N_SAMPLES} batches={N_BATCHES} seed=20260710"
    )
    run_exact_blocks()
    run_coupled_mc()
    run_ledger_guard()
    print()
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
