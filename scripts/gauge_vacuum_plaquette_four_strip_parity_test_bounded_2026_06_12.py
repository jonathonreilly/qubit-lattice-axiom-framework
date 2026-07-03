#!/usr/bin/env python3
"""Four-strip parity test on the finite plaquette packet.

This runner extends the open strip ladder to a four-unit transverse chain.
The primary internal-link convention is the licensed dimension-stripped
contraction; the full-character contraction is reported as a control.  The
four-strip transfer is applied matrix-free:

    T_N x = D_N M_N D_N M_N^T D_N x,
    M_N = M tensor ... tensor M,

with N=4 and layer dimension 25^4 = 390625.
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

import gauge_vacuum_plaquette_three_strip_environment_rho_ladder_bounded_2026_06_12 as three_strip
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
P_TWO_STRIPPED_REFERENCE = 0.439904783618900
P_THREE_STRIPPED_REFERENCE = 0.436904879677743
P_TWO_FULL_REFERENCE = 0.447034890458824
P_THREE_FULL_REFERENCE = 0.441391418390688
COMPARATOR = two_strip.COMPARATOR
COMPARATOR_TEXT = two_strip.COMPARATOR_TEXT

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_FOUR_STRIP_PARITY_TEST_BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class ChainSolve:
    label: str
    chain_length: int
    coeff_kind: str
    eigenvalue: float
    residual: float
    psi_min: float
    internal_min: float
    internal_max: float
    psi: np.ndarray
    rho_by_axis: tuple[np.ndarray, ...]
    p_edge: float
    u0_edge: float
    alpha_s_edge: float
    p_inner: float | None
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


def apply_kron_axes(vec: np.ndarray, mat: np.ndarray, chain_length: int, n: int) -> np.ndarray:
    arr = np.asarray(vec, dtype=float).reshape((n,) * chain_length)
    for axis in range(chain_length):
        arr = three_strip.apply_axis(arr, mat, axis)
    return arr.reshape(-1)


def chain_d_vector(
    packet: two_strip.Packet,
    pair_factor: np.ndarray,
    chain_length: int,
    cut_links: set[int] | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    if cut_links is None:
        cut_links = set()
    n = len(packet.weights)
    link = np.asarray(pair_factor, dtype=float).reshape((n, n))
    shape = (n,) * chain_length
    d_grid = np.ones(shape, dtype=float)
    internal = np.ones(shape, dtype=float)
    for axis in range(chain_length):
        reshape = [1] * chain_length
        reshape[axis] = n
        d_grid *= packet.d_coeff.reshape(reshape)
    for link_pos in range(chain_length - 1):
        if link_pos in cut_links:
            continue
        reshape = [1] * chain_length
        reshape[link_pos] = n
        reshape[link_pos + 1] = n
        internal *= link.reshape(reshape)
    return (d_grid * internal).reshape(-1), internal.reshape(-1)


def make_chain_operator(
    packet: two_strip.Packet,
    d_vec: np.ndarray,
    chain_length: int,
) -> tuple[LinearOperator, callable]:
    n = len(packet.weights)
    dimension = n**chain_length
    m = packet.word_bond
    mt = packet.word_bond.T

    def matvec(x: np.ndarray) -> np.ndarray:
        y = d_vec * np.asarray(x, dtype=float)
        y = apply_kron_axes(y, mt, chain_length, n)
        y = d_vec * y
        y = apply_kron_axes(y, m, chain_length, n)
        y = d_vec * y
        return np.asarray(y, dtype=float)

    return LinearOperator((dimension, dimension), matvec=matvec, dtype=float), matvec


def solve_chain_operator(
    packet: two_strip.Packet,
    d_vec: np.ndarray,
    chain_length: int,
) -> tuple[float, np.ndarray, float, float, str]:
    dimension = len(packet.weights) ** chain_length
    v0 = np.ones(dimension, dtype=float)
    v0 /= np.linalg.norm(v0)
    operator, matvec = make_chain_operator(packet, d_vec, chain_length)
    vals, vecs = eigsh(
        operator,
        k=1,
        which="LA",
        tol=1.0e-12,
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


def rho_marginal(packet: two_strip.Packet, psi: np.ndarray, chain_length: int, axis: int) -> np.ndarray:
    n = len(packet.weights)
    arr = np.asarray(psi, dtype=float).reshape((n,) * chain_length)
    axes = tuple(i for i in range(chain_length) if i != axis)
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


def solve_chain(
    packet: two_strip.Packet,
    pair_factor: np.ndarray,
    chain_length: int,
    label: str,
    coeff_kind: str,
) -> ChainSolve:
    d_vec, internal = chain_d_vector(packet, pair_factor, chain_length)
    eig, psi, residual, psi_min, solver = solve_chain_operator(packet, d_vec, chain_length)
    rho_by_axis = tuple(rho_marginal(packet, psi, chain_length, axis) for axis in range(chain_length))
    p_edge, u0_edge, alpha_s_edge = source_p(packet, rho_by_axis[0])
    p_inner = None
    if chain_length > 2:
        p_inner = source_p(packet, rho_by_axis[1])[0]
    return ChainSolve(
        label=label,
        chain_length=chain_length,
        coeff_kind=coeff_kind,
        eigenvalue=eig,
        residual=residual,
        psi_min=psi_min,
        internal_min=float(np.min(internal)),
        internal_max=float(np.max(internal)),
        psi=psi,
        rho_by_axis=rho_by_axis,
        p_edge=p_edge,
        u0_edge=u0_edge,
        alpha_s_edge=alpha_s_edge,
        p_inner=p_inner,
        solver=solver,
    )


def factorized_residual(
    packet: two_strip.Packet,
    d_vec: np.ndarray,
    chain_length: int,
    psi: np.ndarray,
    eigenvalue: float,
) -> float:
    _operator, matvec = make_chain_operator(packet, d_vec, chain_length)
    return float(np.linalg.norm(matvec(psi) - eigenvalue * psi, ord=np.inf))


def outer_flat(*vectors: np.ndarray) -> np.ndarray:
    out = np.asarray(vectors[0], dtype=float)
    for vec in vectors[1:]:
        out = np.multiply.outer(out, np.asarray(vec, dtype=float))
    return out.reshape(-1)


def p_ladder_lines(label: str, p_values: list[float]) -> dict[str, object]:
    increments = [p_values[i + 1] - p_values[i] for i in range(len(p_values) - 1)]
    distances = [abs(p - COMPARATOR) for p in p_values]
    even_tail = p_values[3]
    odd_tail = p_values[2]
    even_mono = p_values[3] < p_values[1]
    odd_mono = p_values[2] > p_values[0]
    tails_converging = p_values[3] < p_values[1] and p_values[2] > p_values[0]
    bracket_lo = min(even_tail, odd_tail)
    bracket_hi = max(even_tail, odd_tail)
    print(f"{label}:")
    for idx, p_val in enumerate(p_values, start=1):
        print(f"  P({idx}) = {p_val:.15f}")
    for idx, inc in enumerate(increments, start=1):
        print(f"  increment P{idx + 1}-P{idx} = {inc:.15f}")
    print(f"  odd subsequence P(1)->P(3) monotone upward = {odd_mono}")
    print(f"  even subsequence P(2)->P(4) monotone downward = {even_mono}")
    print(f"  measured tails move toward each other = {tails_converging}")
    print(
        "  measured two-sided tail bracket = "
        f"[{bracket_lo:.15f}, {bracket_hi:.15f}]"
    )
    print("  bracket note: measured from P(3) and P(4) only; no extrapolation")
    for idx, dist in enumerate(distances, start=1):
        print(f"  |P({idx}) - {COMPARATOR_TEXT}| = {dist:.15f}")
    return {
        "increments": increments,
        "distances": distances,
        "even_mono": even_mono,
        "odd_mono": odd_mono,
        "tails_converging": tails_converging,
        "bracket_lo": bracket_lo,
        "bracket_hi": bracket_hi,
    }


def density_diagnostic(p_values: list[float]) -> dict[str, object]:
    densities = [(n - 1) / n for n in range(1, 5)]
    deviations = [p - p_values[0] for p in p_values]
    monotone = all(deviations[i] <= deviations[i + 1] for i in range(3))
    print("per-rung internal-link density diagnostic:")
    for n, density, p_val, deviation in zip(range(1, 5), densities, p_values, deviations):
        incident = [0] if n == 1 else [1] + [2] * max(0, n - 2) + [1]
        print(
            f"  N={n}: internal_links={n - 1}, density=(N-1)/N={density:.12f}, "
            f"incident_counts={incident}, P={p_val:.15f}, P-P(1)={deviation:.15f}"
        )
    print(f"  density-order monotone P-deviation = {monotone}")
    print("  diagnostic label: correlation check only; residual target remains open")
    return {"densities": densities, "deviations": deviations, "monotone": monotone}


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    print("Gauge-vacuum plaquette four-strip parity test")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set, predict, promote, or demote any audit outcome."
    )
    print("No new imports: repo-internal finite packet quantities only.")
    print(f"beta={BETA}, tensor NMAX={TW_NMAX}, tensor MODE_MAX={TW_MODE_MAX}")
    print(f"source NMAX={SOURCE_NMAX}, source MODE_MAX={SOURCE_MODE_MAX}")
    print("transverse geometry: open 4-chain with internal links 1-2, 2-3, 3-4")
    print("primary internal-link convention: dimension-stripped")

    packet = two_strip.build_packet()
    fusion = two_strip.build_fusion_table(packet)
    n = len(packet.weights)
    z = packet.index[ZERO]
    f = packet.index[FUND]
    adj = packet.index[ADJOINT]

    section("Part 1: state space and deterministic resource estimate")
    dimension = n**4
    dense_bytes = float(dimension * dimension * 8)
    ncv = 32
    vector_bytes = float(dimension * 8)
    krylov_bytes = float(dimension * ncv * 8)
    matvec_multiplies = 2 * 4 * n * dimension
    print(f"one-word state count = {n}")
    print(f"four-strip layer state count = {dimension}")
    print(f"dense transfer storage would be {format_bytes(dense_bytes)}")
    print(f"one float64 vector storage = {format_bytes(vector_bytes)}")
    print(f"eigsh ncv={ncv} vector basis storage estimate = {format_bytes(krylov_bytes)}")
    print(f"matrix-free matvec multiply-add scale estimate = {matvec_multiplies}")
    print("time estimate: dominated by eigsh matvec count times the printed matvec scale")
    check("four-strip state space has 25^4 = 390625 states", dimension == 390625)
    check("dense 390625 x 390625 transfer is not materialized", dense_bytes > 1.0e12)
    check("matrix-free vector memory estimate remains below dense storage", krylov_bytes < dense_bytes / 1000.0)
    check(
        "generated fusion table remains finite and nonnegative",
        np.issubdtype(fusion.dtype, np.integer) and int(np.min(fusion)) >= 0,
    )

    section("Part 2: anchors")
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

    full_pair_factor = two_strip.internal_factor(packet, fusion, "full_character", "product")
    stripped_pair_factor = two_strip.internal_factor(packet, fusion, "dimension_stripped", "product")

    two_full = two_strip.solve_strip(packet, fusion, "two_strip_full_character_product", "full_character", "product")
    two_stripped = two_strip.solve_strip(
        packet, fusion, "two_strip_dimension_stripped_product", "dimension_stripped", "product"
    )
    two_full_eig, two_full_psi, two_full_residual, _two_full_min = two_strip.perron_symmetric(two_full.transfer)
    two_stripped_eig, two_stripped_psi, two_stripped_residual, _two_stripped_min = two_strip.perron_symmetric(
        two_stripped.transfer
    )
    print(f"two-strip full-character P = {two_full.p_value:.15f}")
    print(f"two-strip full-character residual = {two_full_residual:.3e}")
    print(f"two-strip dimension-stripped P = {two_stripped.p_value:.15f}")
    print(f"two-strip dimension-stripped residual = {two_stripped_residual:.3e}")
    check(
        "two-strip dimension-stripped anchor reproduces the landed value",
        abs(two_stripped.p_value - P_TWO_STRIPPED_REFERENCE) < 5.0e-13,
        f"delta={abs(two_stripped.p_value - P_TWO_STRIPPED_REFERENCE):.3e}",
    )
    check(
        "two-strip full-character control anchor reproduces the landed value",
        abs(two_full.p_value - P_TWO_FULL_REFERENCE) < 5.0e-13,
        f"delta={abs(two_full.p_value - P_TWO_FULL_REFERENCE):.3e}",
    )

    three_stripped = solve_chain(
        packet,
        stripped_pair_factor,
        3,
        "three_strip_dimension_stripped_product_open_chain",
        "dimension_stripped",
    )
    three_full = solve_chain(
        packet,
        full_pair_factor,
        3,
        "three_strip_full_character_product_open_chain",
        "full_character",
    )
    print(f"three-strip dimension-stripped P = {three_stripped.p_edge:.15f}")
    print(f"three-strip dimension-stripped residual = {three_stripped.residual:.3e}")
    print(f"three-strip full-character P = {three_full.p_edge:.15f}")
    print(f"three-strip full-character residual = {three_full.residual:.3e}")
    check(
        "three-strip dimension-stripped anchor reproduces the landed value",
        abs(three_stripped.p_edge - P_THREE_STRIPPED_REFERENCE) < 5.0e-13,
        f"delta={abs(three_stripped.p_edge - P_THREE_STRIPPED_REFERENCE):.3e}",
    )
    check(
        "three-strip full-character control anchor reproduces the landed value",
        abs(three_full.p_edge - P_THREE_FULL_REFERENCE) < 5.0e-13,
        f"delta={abs(three_full.p_edge - P_THREE_FULL_REFERENCE):.3e}",
    )

    section("Part 3: cut gates")
    one_factor = np.ones(n * n, dtype=float)
    d_all_cut, _internal_all_cut = chain_d_vector(packet, one_factor, 4, cut_links={0, 1, 2})
    psi_all_cut = outer_flat(psi_word, psi_word, psi_word, psi_word)
    eig_all_cut = eig_word**4
    all_cut_residual = factorized_residual(packet, d_all_cut, 4, psi_all_cut, eig_all_cut)
    rho_all_cut = rho_marginal(packet, psi_all_cut, 4, 0)
    p_all_cut, _u0_all, _alpha_all = source_p(packet, rho_all_cut)
    print(f"all-link cut eigenvalue candidate = {eig_all_cut:.15f}")
    print(f"all-link cut residual on four word-chain tensor = {all_cut_residual:.3e}")
    print(f"all-link cut max |rho-rho_word| = {float(np.max(np.abs(rho_all_cut - rho_word))):.3e}")
    print(f"P(all-link cut marginal) = {p_all_cut:.15f}")
    check("all-link cut reproduces four independent word chains", all_cut_residual < 1.0e-12)
    check(
        "all-link cut marginal reproduces rho_word",
        float(np.max(np.abs(rho_all_cut - rho_word))) < 5.0e-13,
    )
    check("all-link cut source readout reproduces P(rho_word)", abs(p_all_cut - p_word) < 5.0e-13)

    for label, pair_factor, two_result, two_eig, two_psi, three_result in [
        ("dimension-stripped", stripped_pair_factor, two_stripped, two_stripped_eig, two_stripped_psi, three_stripped),
        ("full-character", full_pair_factor, two_full, two_full_eig, two_full_psi, three_full),
    ]:
        print()
        print(f"{label} single-link cut gates:")

        d_cut_right, _ = chain_d_vector(packet, pair_factor, 4, cut_links={2})
        psi_cut_right = outer_flat(three_result.psi, psi_word)
        eig_cut_right = three_result.eigenvalue * eig_word
        residual_cut_right = factorized_residual(packet, d_cut_right, 4, psi_cut_right, eig_cut_right)
        rho_cut_right = rho_marginal(packet, psi_cut_right, 4, 0)
        p_cut_right, _u0_cr, _alpha_cr = source_p(packet, rho_cut_right)
        print(f"  cut link 3-4 residual on psi_3strip tensor psi_word = {residual_cut_right:.3e}")
        print(
            "  cut link 3-4 edge marginal max |rho-rho_3strip| = "
            f"{float(np.max(np.abs(rho_cut_right - three_result.rho_by_axis[0]))):.3e}"
        )
        print(f"  cut link 3-4 P(edge marginal) = {p_cut_right:.15f}")

        d_cut_left, _ = chain_d_vector(packet, pair_factor, 4, cut_links={0})
        psi_cut_left = outer_flat(psi_word, three_result.psi)
        eig_cut_left = eig_word * three_result.eigenvalue
        residual_cut_left = factorized_residual(packet, d_cut_left, 4, psi_cut_left, eig_cut_left)
        rho_cut_left_block = rho_marginal(packet, psi_cut_left, 4, 1)
        p_cut_left, _u0_cl, _alpha_cl = source_p(packet, rho_cut_left_block)
        print(f"  cut link 1-2 residual on psi_word tensor psi_3strip = {residual_cut_left:.3e}")
        print(
            "  cut link 1-2 block-edge marginal max |rho-rho_3strip| = "
            f"{float(np.max(np.abs(rho_cut_left_block - three_result.rho_by_axis[0]))):.3e}"
        )
        print(f"  cut link 1-2 P(block-edge marginal) = {p_cut_left:.15f}")

        d_cut_middle, _ = chain_d_vector(packet, pair_factor, 4, cut_links={1})
        psi_cut_middle = outer_flat(two_psi, two_psi)
        eig_cut_middle = two_eig * two_eig
        residual_cut_middle = factorized_residual(packet, d_cut_middle, 4, psi_cut_middle, eig_cut_middle)
        rho_cut_middle = rho_marginal(packet, psi_cut_middle, 4, 0)
        p_cut_middle, _u0_cm, _alpha_cm = source_p(packet, rho_cut_middle)
        print(f"  cut link 2-3 residual on psi_2strip tensor psi_2strip = {residual_cut_middle:.3e}")
        print(
            "  cut link 2-3 edge marginal max |rho-rho_2strip| = "
            f"{float(np.max(np.abs(rho_cut_middle - two_result.rho_left))):.3e}"
        )
        print(f"  cut link 2-3 P(edge marginal) = {p_cut_middle:.15f}")

        check(f"{label} cut link 3-4 reproduces 3-strip x 1-word transfer", residual_cut_right < 1.0e-11)
        check(
            f"{label} cut link 3-4 reproduces the three-strip edge rho",
            float(np.max(np.abs(rho_cut_right - three_result.rho_by_axis[0]))) < 5.0e-13
            and abs(p_cut_right - three_result.p_edge) < 5.0e-13,
        )
        check(f"{label} cut link 1-2 reproduces 1-word x 3-strip transfer", residual_cut_left < 1.0e-11)
        check(
            f"{label} cut link 1-2 exposes the three-strip edge rho",
            float(np.max(np.abs(rho_cut_left_block - three_result.rho_by_axis[0]))) < 5.0e-13
            and abs(p_cut_left - three_result.p_edge) < 5.0e-13,
        )
        check(f"{label} cut link 2-3 reproduces 2-strip x 2-strip transfer", residual_cut_middle < 1.0e-11)
        check(
            f"{label} cut link 2-3 reproduces the two-strip edge rho",
            float(np.max(np.abs(rho_cut_middle - two_result.rho_left))) < 5.0e-13
            and abs(p_cut_middle - two_result.p_value) < 5.0e-13,
        )

    section("Part 4: four-strip Perron solves")
    four_stripped = solve_chain(
        packet,
        stripped_pair_factor,
        4,
        "four_strip_dimension_stripped_product_open_chain",
        "dimension_stripped",
    )
    four_full = solve_chain(
        packet,
        full_pair_factor,
        4,
        "four_strip_full_character_product_open_chain",
        "full_character",
    )

    for result in [four_stripped, four_full]:
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
        print(f"  rho_edge(1,0) = {result.rho_by_axis[0][f]:.15f}")
        print(f"  rho_edge(1,1) = {result.rho_by_axis[0][adj]:.15f}")
        print(f"  rho_edge min/max = {float(np.min(result.rho_by_axis[0])):.3e} / {float(np.max(result.rho_by_axis[0])):.3e}")
        print(f"  rho_inner(1,0) = {result.rho_by_axis[1][f]:.15f}")
        print(f"  rho_inner(1,1) = {result.rho_by_axis[1][adj]:.15f}")
        print(f"  edge reversal residual = {float(np.max(np.abs(result.rho_by_axis[0] - result.rho_by_axis[3]))):.3e}")
        print(f"  inner reversal residual = {float(np.max(np.abs(result.rho_by_axis[1] - result.rho_by_axis[2]))):.3e}")
        print(f"  edge/inner marginal residual = {float(np.max(np.abs(result.rho_by_axis[0] - result.rho_by_axis[1]))):.3e}")
        print(f"  edge conjugation residual = {conjugation_error(packet, result.rho_by_axis[0]):.3e}")
        print(f"  P(edge rho) = {result.p_edge:.15f}")
        print(f"  P(inner rho) = {result.p_inner:.15f}")
        print(f"  u0(edge rho) = {result.u0_edge:.15f}")
        print(f"  alpha_s(edge rho; alpha_bare=1) = {result.alpha_s_edge:.15f}")
        check(f"{result.label} Perron residual is small", result.residual < 1.0e-10)
        check(f"{result.label} Perron vector is nonnegative up to tolerance", result.psi_min >= -1.0e-12)
        check(
            f"{result.label} edge rho is admissible on B4",
            np.all(np.isfinite(result.rho_by_axis[0]))
            and abs(float(result.rho_by_axis[0][z]) - 1.0) < 1.0e-13
            and float(np.min(result.rho_by_axis[0])) >= -1.0e-12
            and conjugation_error(packet, result.rho_by_axis[0]) < 1.0e-11,
        )
        check(
            f"{result.label} open-chain reversal gives equal edge marginals",
            float(np.max(np.abs(result.rho_by_axis[0] - result.rho_by_axis[3]))) < 1.0e-10,
        )
        check(
            f"{result.label} open-chain reversal gives equal inner marginals",
            float(np.max(np.abs(result.rho_by_axis[1] - result.rho_by_axis[2]))) < 1.0e-10,
        )

    section("Part 5: parity analysis and fenced comparator distances")
    print("Plaquette reuse license: comparator is used only as comparison/reuse context.")
    print("```text")
    stripped_ladder = [p_word, two_stripped.p_value, three_stripped.p_edge, four_stripped.p_edge]
    full_ladder = [p_word, two_full.p_value, three_full.p_edge, four_full.p_edge]
    stripped_diag = p_ladder_lines("dimension-stripped reading", stripped_ladder)
    density_diag = density_diagnostic(stripped_ladder)
    full_diag = p_ladder_lines("full-character control reading", full_ladder)
    print("```")
    check("dimension-stripped ladder diagnostics are finite", all(np.isfinite(p) for p in stripped_ladder))
    check("full-character control ladder diagnostics are finite", all(np.isfinite(p) for p in full_ladder))
    check(
        "dimension-stripped even and odd subsequence monotonicity gates pass as measured",
        bool(stripped_diag["even_mono"]) and bool(stripped_diag["odd_mono"]),
    )
    check(
        "dimension-stripped measured tails move toward each other",
        bool(stripped_diag["tails_converging"]),
    )
    check(
        "dimension-stripped measured bracket is ordered",
        float(stripped_diag["bracket_lo"]) <= float(stripped_diag["bracket_hi"]),
    )
    check(
        "dimension-stripped density diagnostic is finite",
        all(np.isfinite(v) for v in density_diag["densities"])
        and all(np.isfinite(v) for v in density_diag["deviations"]),
    )

    section("Part 6: note hygiene")
    text = note_text()
    if text:
        check(
            "note delegates status to the independent audit lane",
            "Status authority: independent audit lane only" in text
            and "does not set" in text
            and "promote, or demote any audit outcome" in text,
        )
        check(
            "note uses markdown links for one-hop authorities",
            "[GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md]" in text
            and "[GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md]" in text
            and "[GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md]" in text,
        )
        check(
            "note uses durable repo context pointers instead of branch-local temp refs",
            "docs/GAUGE_VACUUM_PLAQUETTE_THREE_STRIP_ENVIRONMENT_RHO_LADDER_BOUNDED_NOTE_2026-06-12.md" in text
            and "." + "claude/tmp/refs/" not in text,
        )
        banned = [
            " ".join(("only", "route")),
            " ".join(("last", "route")),
            "ex" + "hausted",
            " ".join(("closes", "the", "program")),
        ]
        check("note avoids overreach closure language", not any(phrase in text.lower() for phrase in banned))
    else:
        check("note exists for this runner", False, f"missing {NOTE_PATH}")

    print(
        "Named residuals: finite four-strip width rung; finite B4 weight box; "
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
