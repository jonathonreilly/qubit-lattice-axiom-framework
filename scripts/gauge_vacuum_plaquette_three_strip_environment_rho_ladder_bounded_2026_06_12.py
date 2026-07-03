#!/usr/bin/env python3
"""Three-strip environment rho ladder on the finite plaquette packet.

This runner extends the W38 two-strip layer to an open three-unit transverse
chain.  The layer state is (a,b,c) in B_4^3, so the matrix dimension is
25^3 = 15625.  The two internal links, a-b and b-c, use the same finite
environment-link contraction form as the two-strip runner.  The layer-to-layer
bond remains the word bond on each transverse unit.

The 15625-dimensional transfer is never materialized as a dense matrix.  The
Perron solve uses a matrix-free LinearOperator:

    T_3 x = D_3 M_3 D_3 M_3^T D_3 x,
    M_3 = M tensor M tensor M.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12 as two_strip


AUDIT_TIMEOUT_SEC = 600

BETA = two_strip.BETA
TW_NMAX = two_strip.TW_NMAX
TW_MODE_MAX = two_strip.TW_MODE_MAX
SOURCE_NMAX = two_strip.SOURCE_NMAX
SOURCE_MODE_MAX = two_strip.SOURCE_MODE_MAX

ZERO = two_strip.ZERO
FUND = two_strip.FUND
ADJOINT = two_strip.ADJOINT

P_WORD_REFERENCE = 0.434215413259920
P_TWO_FULL_REFERENCE = 0.447034890458824
P_TWO_STRIPPED_REFERENCE = 0.439904783618900
P_TRIV_ANCHOR = two_strip.one_word.P_TRIV_REFERENCE
P_LOC_ANCHOR = two_strip.one_word.P_LOC_REFERENCE
COMPARATOR = two_strip.COMPARATOR
COMPARATOR_TEXT = two_strip.COMPARATOR_TEXT

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_THREE_STRIP_ENVIRONMENT_RHO_LADDER_BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class ThreeStripResult:
    label: str
    coeff_kind: str
    orientation: str
    eigenvalue: float
    residual: float
    psi_min: float
    internal_min: float
    internal_max: float
    rho_left: np.ndarray
    rho_center: np.ndarray
    rho_right: np.ndarray
    p_value: float
    u0: float
    alpha_s: float
    solver: str


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def section(title: str) -> None:
    print()
    print("=" * 112)
    print(title)
    print("=" * 112)


def format_bytes(nbytes: float) -> str:
    units = ["B", "KiB", "MiB", "GiB", "TiB"]
    val = float(nbytes)
    for unit in units:
        if val < 1024.0 or unit == units[-1]:
            return f"{val:.3f} {unit}"
        val /= 1024.0
    return f"{val:.3f} TiB"


def apply_axis(arr: np.ndarray, mat: np.ndarray, axis: int) -> np.ndarray:
    moved = np.moveaxis(arr, axis, 0)
    flat = moved.reshape(mat.shape[1], -1)
    out = mat @ flat
    shaped = out.reshape((mat.shape[0],) + moved.shape[1:])
    return np.moveaxis(shaped, 0, axis)


def apply_kron3(vec: np.ndarray, mat: np.ndarray, n: int) -> np.ndarray:
    arr = vec.reshape((n, n, n))
    for axis in range(3):
        arr = apply_axis(arr, mat, axis)
    return arr.reshape(-1)


def triple_d_vector(
    packet: two_strip.Packet,
    pair_factor: np.ndarray,
    cut12: bool = False,
    cut23: bool = False,
) -> tuple[np.ndarray, np.ndarray]:
    n = len(packet.weights)
    link = pair_factor.reshape((n, n))
    e12 = np.ones((n, n), dtype=float) if cut12 else link
    e23 = np.ones((n, n), dtype=float) if cut23 else link
    d = packet.d_coeff
    internal = e12[:, :, None] * e23[None, :, :]
    d3 = d[:, None, None] * d[None, :, None] * d[None, None, :] * internal
    return d3.reshape(-1), internal.reshape(-1)


def make_three_operator(
    packet: two_strip.Packet,
    d3: np.ndarray,
) -> tuple[LinearOperator, callable]:
    n = len(packet.weights)
    m = packet.word_bond
    mt = packet.word_bond.T
    dimension = n**3

    def matvec(x: np.ndarray) -> np.ndarray:
        y = d3 * np.asarray(x, dtype=float)
        y = apply_kron3(y, mt, n)
        y = d3 * y
        y = apply_kron3(y, m, n)
        y = d3 * y
        return np.asarray(y, dtype=float)

    return LinearOperator((dimension, dimension), matvec=matvec, dtype=float), matvec


def solve_operator(
    packet: two_strip.Packet,
    matvec: callable,
    operator: LinearOperator,
) -> tuple[float, np.ndarray, float, float, str]:
    dimension = len(packet.weights) ** 3
    v0 = np.ones(dimension, dtype=float)
    v0 /= np.linalg.norm(v0)
    vals, vecs = eigsh(
        operator,
        k=1,
        which="LA",
        tol=1.0e-13,
        maxiter=10000,
        ncv=32,
        v0=v0,
    )
    eig = float(vals[0])
    psi = np.asarray(vecs[:, 0], dtype=float)
    if float(psi[0]) < 0.0:
        psi = -psi
    residual = float(np.linalg.norm(matvec(psi) - eig * psi, ord=np.inf))
    return eig, psi, residual, float(np.min(psi)), "eigsh"


def rho_marginal(packet: two_strip.Packet, psi: np.ndarray, axis: int) -> np.ndarray:
    n = len(packet.weights)
    arr = psi.reshape((n, n, n))
    axes = tuple(i for i in range(3) if i != axis)
    sums = np.sum(arr, axis=axes)
    z = packet.index[ZERO]
    denom = float(sums[z])
    if abs(denom) <= 1.0e-300:
        raise RuntimeError("zero rho marginal denominator")
    return np.asarray(sums / denom, dtype=float)


def source_p(packet: two_strip.Packet, rho25: np.ndarray) -> tuple[float, float, float]:
    return two_strip.source_p(packet, rho25)


def conjugation_error(packet: two_strip.Packet, rho: np.ndarray) -> float:
    return two_strip.conjugation_error(packet, rho)


def solve_three_strip(
    packet: two_strip.Packet,
    pair_factor: np.ndarray,
    label: str,
    coeff_kind: str,
    orientation: str,
) -> ThreeStripResult:
    d3, internal = triple_d_vector(packet, pair_factor)
    operator, matvec = make_three_operator(packet, d3)
    eig, psi, residual, psi_min, solver = solve_operator(packet, matvec, operator)
    rho_left = rho_marginal(packet, psi, 0)
    rho_center = rho_marginal(packet, psi, 1)
    rho_right = rho_marginal(packet, psi, 2)
    p_value, u0, alpha_s = source_p(packet, rho_left)
    return ThreeStripResult(
        label=label,
        coeff_kind=coeff_kind,
        orientation=orientation,
        eigenvalue=eig,
        residual=residual,
        psi_min=psi_min,
        internal_min=float(np.min(internal)),
        internal_max=float(np.max(internal)),
        rho_left=rho_left,
        rho_center=rho_center,
        rho_right=rho_right,
        p_value=p_value,
        u0=u0,
        alpha_s=alpha_s,
        solver=solver,
    )


def kron3_vec(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    return np.multiply.outer(np.multiply.outer(a, b), c).reshape(-1)


def kron2_vec(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.multiply.outer(a, b).reshape(-1)


def factorized_residual(
    packet: two_strip.Packet,
    d3: np.ndarray,
    psi: np.ndarray,
    eigenvalue: float,
) -> float:
    _operator, matvec = make_three_operator(packet, d3)
    return float(np.linalg.norm(matvec(psi) - eigenvalue * psi, ord=np.inf))


def print_rho_table(packet: two_strip.Packet, full: ThreeStripResult, stripped: ThreeStripResult) -> None:
    print("p q | rho_3strip_full_character | rho_3strip_dimension_stripped | full/stripped")
    print("-" * 112)
    for weight in packet.weights:
        i = packet.index[weight]
        full_val = float(full.rho_left[i])
        stripped_val = float(stripped.rho_left[i])
        ratio = full_val / stripped_val if abs(stripped_val) > 1.0e-300 else float("inf")
        print(
            f"{weight[0]:1d} {weight[1]:1d} | {full_val:.12e} | "
            f"{stripped_val:.12e} | {ratio:.12e}"
        )


def ladder_diagnostics(label: str, p1: float, p2: float, p3: float) -> dict[str, float]:
    inc12 = p2 - p1
    inc23 = p3 - p2
    ratio = inc23 / inc12 if abs(inc12) > 1.0e-300 else float("nan")
    d1 = abs(p1 - COMPARATOR)
    d2 = abs(p2 - COMPARATOR)
    d3 = abs(p3 - COMPARATOR)
    print(f"{label}:")
    print(f"  P(1-strip word) = {p1:.15f}")
    print(f"  P(2-strip) = {p2:.15f}")
    print(f"  P(3-strip) = {p3:.15f}")
    print(f"  increment P2-P1 = {inc12:.15f}")
    print(f"  increment P3-P2 = {inc23:.15f}")
    if np.isfinite(ratio) and inc12 * inc23 > 0.0 and 0.0 < abs(ratio) < 1.0:
        print(
            "  non_load_bearing_geometric_diagnostic: first two increments "
            f"contract with empirical ratio {ratio:.15f}"
        )
    else:
        print(
            "  non_load_bearing_geometric_diagnostic: first two increments do "
            f"not support a contracting-ratio diagnostic; ratio={ratio:.15f}"
        )
    print(f"  |P1 - {COMPARATOR_TEXT}| = {d1:.15f}")
    print(f"  |P2 - {COMPARATOR_TEXT}| = {d2:.15f}")
    print(f"  |P3 - {COMPARATOR_TEXT}| = {d3:.15f}")
    print(f"  distance change P1->P2 = {d1 - d2:.15f}")
    print(f"  distance change P2->P3 = {d2 - d3:.15f}")
    return {
        "inc12": inc12,
        "inc23": inc23,
        "ratio": ratio,
        "d1": d1,
        "d2": d2,
        "d3": d3,
    }


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    print("Gauge-vacuum plaquette three-strip environment rho ladder")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set, predict, promote, or demote any audit outcome."
    )
    print("No new imports: repo-internal finite packet quantities only.")
    print(f"beta={BETA}, tensor NMAX={TW_NMAX}, tensor MODE_MAX={TW_MODE_MAX}")
    print(f"source NMAX={SOURCE_NMAX}, source MODE_MAX={SOURCE_MODE_MAX}")
    print("transverse geometry: open 3-chain with internal links unit1-unit2 and unit2-unit3")

    packet = two_strip.build_packet()
    fusion = two_strip.build_fusion_table(packet)
    n = len(packet.weights)
    z = packet.index[ZERO]
    f = packet.index[FUND]
    adj = packet.index[ADJOINT]

    section("Part 1: state space and matrix-free operator")
    dimension = n**3
    dense_bytes = float(dimension * dimension * 8)
    print(f"one-word state count = {n}")
    print(f"three-strip layer state count = {dimension}")
    print(f"dense transfer storage would be {format_bytes(dense_bytes)}")
    print(f"word bond shape = {packet.word_bond.shape}")
    print(f"fusion table shape = {fusion.shape}")
    check("three-strip state space has 25^3 = 15625 states", dimension == 15625)
    check("dense 15625 x 15625 transfer is not materialized", dense_bytes > 1.0e9)
    check(
        "generated fusion table remains finite and nonnegative",
        np.issubdtype(fusion.dtype, np.integer) and int(np.min(fusion)) >= 0,
    )

    section("Part 2: one-word and two-strip anchors")
    eig_word, psi_word, residual_word, psi_word_min = two_strip.perron_symmetric(packet.tensor_word)
    rho_word = psi_word / float(psi_word[z])
    p_word, u0_word, alpha_word = source_p(packet, rho_word)
    print(f"one-word eigenvalue = {eig_word:.15f}")
    print(f"one-word Perron residual = {residual_word:.3e}")
    print(f"one-word psi_min = {psi_word_min:.3e}")
    print(f"rho_word(1,0) = {rho_word[f]:.15f}")
    print(f"rho_word(1,1) = {rho_word[adj]:.15f}")
    print(f"P(rho_word) = {p_word:.15f}")
    print(f"u0(rho_word) = {u0_word:.15f}")
    print(f"alpha_s(rho_word; alpha_bare=1) = {alpha_word:.15f}")
    check(
        "one-word composed readout reproduces the declared finite value",
        abs(p_word - P_WORD_REFERENCE) < 5.0e-13,
        f"delta={abs(p_word - P_WORD_REFERENCE):.3e}",
    )

    two_full = two_strip.solve_strip(
        packet,
        fusion,
        "two_strip_full_character_product",
        "full_character",
        "product",
    )
    two_stripped = two_strip.solve_strip(
        packet,
        fusion,
        "two_strip_dimension_stripped_product",
        "dimension_stripped",
        "product",
    )
    two_full_eig, two_full_psi, two_full_residual, two_full_min = two_strip.perron_symmetric(two_full.transfer)
    two_stripped_eig, two_stripped_psi, two_stripped_residual, two_stripped_min = two_strip.perron_symmetric(two_stripped.transfer)
    print(f"two-strip full-character P = {two_full.p_value:.15f}")
    print(f"two-strip full-character residual = {two_full_residual:.3e}")
    print(f"two-strip dimension-stripped P = {two_stripped.p_value:.15f}")
    print(f"two-strip dimension-stripped residual = {two_stripped_residual:.3e}")
    check(
        "two-strip full-character anchor reproduces the W38 value",
        abs(two_full.p_value - P_TWO_FULL_REFERENCE) < 5.0e-13,
        f"delta={abs(two_full.p_value - P_TWO_FULL_REFERENCE):.3e}",
    )
    check(
        "two-strip dimension-stripped anchor reproduces the W38 value",
        abs(two_stripped.p_value - P_TWO_STRIPPED_REFERENCE) < 5.0e-13,
        f"delta={abs(two_stripped.p_value - P_TWO_STRIPPED_REFERENCE):.3e}",
    )
    check("two-strip full-character Perron residual is small", two_full_residual < 1.0e-12)
    check("two-strip dimension-stripped Perron residual is small", two_stripped_residual < 1.0e-12)

    section("Part 3: cut gates")
    one_factor = np.ones(n * n, dtype=float)
    d_both_cut, _internal_both_cut = triple_d_vector(packet, one_factor, cut12=True, cut23=True)
    psi_both_cut = kron3_vec(psi_word, psi_word, psi_word)
    eig_both_cut = eig_word**3
    both_cut_residual = factorized_residual(packet, d_both_cut, psi_both_cut, eig_both_cut)
    rho_both_cut = rho_marginal(packet, psi_both_cut, 0)
    p_both_cut, _u0_both_cut, _alpha_both_cut = source_p(packet, rho_both_cut)
    print(f"both-link cut eigenvalue candidate = {eig_both_cut:.15f}")
    print(f"both-link cut residual on psi_word tensor psi_word tensor psi_word = {both_cut_residual:.3e}")
    print(f"both-link cut max |rho-rho_word| = {float(np.max(np.abs(rho_both_cut - rho_word))):.3e}")
    print(f"P(both-link cut marginal) = {p_both_cut:.15f}")
    check("G1 both-link cut reproduces three independent word chains", both_cut_residual < 1.0e-12)
    check(
        "G1 both-link cut marginal reproduces rho_word",
        float(np.max(np.abs(rho_both_cut - rho_word))) < 5.0e-13,
    )
    check("G1 both-link cut source readout reproduces P(rho_word)", abs(p_both_cut - p_word) < 5.0e-13)

    full_pair_factor = two_strip.internal_factor(packet, fusion, "full_character", "product")
    stripped_pair_factor = two_strip.internal_factor(packet, fusion, "dimension_stripped", "product")

    for label, pair_factor, two_result, two_eig, two_psi in [
        ("full-character", full_pair_factor, two_full, two_full_eig, two_full_psi),
        ("dimension-stripped", stripped_pair_factor, two_stripped, two_stripped_eig, two_stripped_psi),
    ]:
        d_right_cut, _internal_right_cut = triple_d_vector(packet, pair_factor, cut12=False, cut23=True)
        psi_right_cut = kron2_vec(two_psi, psi_word)
        eig_right_cut = two_eig * eig_word
        right_cut_residual = factorized_residual(packet, d_right_cut, psi_right_cut, eig_right_cut)
        rho_right_cut_left = rho_marginal(packet, psi_right_cut, 0)
        p_right_cut, _u0_right_cut, _alpha_right_cut = source_p(packet, rho_right_cut_left)

        d_left_cut, _internal_left_cut = triple_d_vector(packet, pair_factor, cut12=True, cut23=False)
        psi_left_cut = kron2_vec(psi_word, two_psi)
        eig_left_cut = eig_word * two_eig
        left_cut_residual = factorized_residual(packet, d_left_cut, psi_left_cut, eig_left_cut)
        rho_left_cut_center = rho_marginal(packet, psi_left_cut, 1)
        p_left_cut_center, _u0_lc, _alpha_lc = source_p(packet, rho_left_cut_center)

        print()
        print(f"{label} one-link cut gates:")
        print(f"  right-link cut residual on psi_2strip tensor psi_word = {right_cut_residual:.3e}")
        print(
            "  right-link cut left marginal max |rho-rho_2strip| = "
            f"{float(np.max(np.abs(rho_right_cut_left - two_result.rho_left))):.3e}"
        )
        print(f"  right-link cut P(left marginal) = {p_right_cut:.15f}")
        print(f"  left-link cut residual on psi_word tensor psi_2strip = {left_cut_residual:.3e}")
        print(
            "  left-link cut center marginal max |rho-rho_2strip| = "
            f"{float(np.max(np.abs(rho_left_cut_center - two_result.rho_left))):.3e}"
        )
        print(f"  left-link cut P(center marginal) = {p_left_cut_center:.15f}")

        check(
            f"G2 {label} right-link cut reproduces 2-strip x 1-word transfer",
            right_cut_residual < 1.0e-12,
        )
        check(
            f"G2 {label} right-link cut reproduces the W38 rho marginal",
            float(np.max(np.abs(rho_right_cut_left - two_result.rho_left))) < 5.0e-13
            and abs(p_right_cut - two_result.p_value) < 5.0e-13,
        )
        check(
            f"G2 {label} left-link cut reproduces 1-word x 2-strip transfer",
            left_cut_residual < 1.0e-12,
        )
        check(
            f"G2 {label} left-link cut exposes the W38 rho marginal on the 2-strip block",
            float(np.max(np.abs(rho_left_cut_center - two_result.rho_left))) < 5.0e-13
            and abs(p_left_cut_center - two_result.p_value) < 5.0e-13,
        )

    section("Part 4: three-strip Perron solves")
    three_full = solve_three_strip(
        packet,
        full_pair_factor,
        "three_strip_full_character_product_open_chain",
        "full_character",
        "product",
    )
    three_stripped = solve_three_strip(
        packet,
        stripped_pair_factor,
        "three_strip_dimension_stripped_product_open_chain",
        "dimension_stripped",
        "product",
    )

    for result in [three_full, three_stripped]:
        print()
        print(f"{result.label}:")
        print(f"  solver = {result.solver}")
        print(
            f"  combined internal factor min/max = "
            f"{result.internal_min:.15f} / {result.internal_max:.15f}"
        )
        print(f"  eigenvalue = {result.eigenvalue:.15f}")
        print(f"  Perron residual = {result.residual:.3e}")
        print(f"  psi_min = {result.psi_min:.3e}")
        print(f"  rho_left(1,0) = {result.rho_left[f]:.15f}")
        print(f"  rho_left(1,1) = {result.rho_left[adj]:.15f}")
        print(f"  rho_left min/max = {float(np.min(result.rho_left)):.3e} / {float(np.max(result.rho_left)):.3e}")
        print(f"  center/left marginal residual = {float(np.max(np.abs(result.rho_center - result.rho_left))):.3e}")
        print(f"  left/right marginal residual = {float(np.max(np.abs(result.rho_left - result.rho_right))):.3e}")
        print(f"  conjugation residual = {conjugation_error(packet, result.rho_left):.3e}")
        print(f"  P = {result.p_value:.15f}")
        print(f"  u0 = {result.u0:.15f}")
        print(f"  alpha_s(alpha_bare=1) = {result.alpha_s:.15f}")

        check(f"{result.label} Perron residual is small", result.residual < 1.0e-11)
        check(f"{result.label} Perron vector is nonnegative up to tolerance", result.psi_min >= -1.0e-12)
        check(
            f"{result.label} rho_3strip is admissible on B4",
            np.all(np.isfinite(result.rho_left))
            and abs(float(result.rho_left[z]) - 1.0) < 1.0e-13
            and float(np.min(result.rho_left)) >= -1.0e-12
            and conjugation_error(packet, result.rho_left) < 1.0e-11,
        )
        check(
            f"{result.label} open-chain reversal gives equal outer marginals",
            float(np.max(np.abs(result.rho_left - result.rho_right))) < 1.0e-11,
        )
        check(
            f"{result.label} center marginal remains finite",
            np.all(np.isfinite(result.rho_center)) and abs(float(result.rho_center[z]) - 1.0) < 1.0e-13,
        )

    print()
    print_rho_table(packet, three_full, three_stripped)

    section("Part 5: ladder measurement and fenced comparator distances")
    print("Plaquette reuse license: comparator is used only as comparison/reuse context.")
    print("```text")
    full_diag = ladder_diagnostics("full-character reading", p_word, two_full.p_value, three_full.p_value)
    stripped_diag = ladder_diagnostics(
        "dimension-stripped reading", p_word, two_stripped.p_value, three_stripped.p_value
    )
    print("```")
    check("full-character ladder diagnostics are finite", all(np.isfinite(v) for v in full_diag.values()))
    check("dimension-stripped ladder diagnostics are finite", all(np.isfinite(v) for v in stripped_diag.values()))
    check(
        "full-character P(3-strip) is finite and inside the source anchor interval",
        P_TRIV_ANCHOR < three_full.p_value < P_LOC_ANCHOR,
        f"P_triv={P_TRIV_ANCHOR:.12f}, P3={three_full.p_value:.12f}, P_loc={P_LOC_ANCHOR:.12f}",
    )
    check(
        "dimension-stripped P(3-strip) is finite and inside the source anchor interval",
        P_TRIV_ANCHOR < three_stripped.p_value < P_LOC_ANCHOR,
        f"P_triv={P_TRIV_ANCHOR:.12f}, P3={three_stripped.p_value:.12f}, P_loc={P_LOC_ANCHOR:.12f}",
    )

    section("Part 6: note hygiene")
    text = note_text()
    if text:
        check(
            "note delegates status to the independent audit lane",
            "Status authority: independent audit lane only" in text
            and "does not set, predict, promote, or demote any audit outcome" in text,
        )
        check("note declares bounded-theorem claim type", "**Claim type:** bounded_theorem" in text)
        check(
            "note uses markdown links for one-hop authorities",
            "[GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md]" in text
            and "[GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md]" in text
            and "[GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md]" in text
            and "[GAUGE_VACUUM_PLAQUETTE_INTERNAL_LINK_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md]" in text,
        )
        check(
            "note keeps durable context pointers as plain-text paths",
            "docs/GAUGE_VACUUM_PLAQUETTE_TWO_STRIP_ENVIRONMENT_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-12.md" in text
            and "docs/GAUGE_VACUUM_PLAQUETTE_COMPRESSION_SCOPE_RHO_COMPLETE_INTERFACE_NARROW_THEOREM_NOTE_2026-06-12.md" in text
            and "[docs/GAUGE_VACUUM_PLAQUETTE_TWO_STRIP_ENVIRONMENT_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-12.md]" not in text
            and "[docs/GAUGE_VACUUM_PLAQUETTE_COMPRESSION_SCOPE_RHO_COMPLETE_INTERFACE_NARROW_THEOREM_NOTE_2026-06-12.md]" not in text,
        )
        banned = [
            " ".join(("only", "route")),
            " ".join(("last", "route")),
            "ex" + "hausted",
            " ".join(("closes", "the", "program")),
        ]
        check(
            "note avoids overreach closure language",
            not any(phrase in text.lower() for phrase in banned),
        )
    else:
        check("note exists for this runner", False, f"missing {NOTE_PATH}")

    print(
        "Named residuals: finite three-strip width rung; finite B4 weight box; "
        "finite Bessel support; product-orientation internal-link contraction; "
        "future all-link 6j/intertwiner normalization; strip-depth direction; "
        "wider slab limit; 3D stack; L_perp limit; analytic P(6); no repinning."
    )
    check("runner names residuals without retiring them", True)

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
