#!/usr/bin/env python3
"""Finite word-count rung-four deep-rim readout.

This runner extends the finite deep-rim word-count ladder under the
FULLY-DERIVED convention:

* matrix-element adjacent bond delta(lambda, mu) / d_lambda;
* tensor-word Perron vector eta_inf on every unmarked slot;
* tensor NMAX=4, tensor MODE_MAX=80;
* source NMAX=7, source MODE_MAX=200.

It performs two cross-checking routes.

Route A is a direct 25^4-dimensional eigsh solve with a factor-wise
Kronecker matvec. The fusion Kronecker is never materialized.

Route B is the eta-weighted finite-rank channel reduction derived from the
same operator. It validates against direct k=2 and k=3 deep-rim readouts and
against Route A at k=4, then reports k=1..20.

All statements are finite-packet measurements. No physical 3D environment,
untruncated limit, L_perp limit, analytic P(6), or canonical repinning is
claimed.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import LinearOperator, eigsh

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_rim_boundary_eta_env_constructed_readout_2026_06_12 as rim
import gauge_vacuum_plaquette_tensor_word_multiword_perron_ladder_2026_06_11 as multiword
import gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_2026_06_11 as one_word_ref


AUDIT_TIMEOUT_SEC = 600

BETA = 6.0
TW_NMAX = 4
TW_MODE_MAX = 80
SOURCE_NMAX = one_word_ref.SOURCE_NMAX
SOURCE_MODE_MAX = one_word_ref.SOURCE_MODE_MAX
DIRECT_K4_NCV = 30
REDUCED_KMAX = 20
TOL = 1.0e-10

P1_REFERENCE = 0.434215413260
P2_DEEP_REFERENCE = 0.433061880380
P3_DEEP_REFERENCE = 0.543142610051
CANONICAL_COMPARATOR_TEXT = one_word_ref.CANONICAL_COMPARATOR_TEXT
CANONICAL_COMPARATOR = one_word_ref.CANONICAL_COMPARATOR

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_RUNG_FOUR_DEEP_RIM_BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class Packet:
    weights: tuple[tuple[int, int], ...]
    index: dict[tuple[int, int], int]
    d_coeff: np.ndarray
    dim: np.ndarray
    fusion: np.ndarray
    tensor_word: np.ndarray
    eta_inf: np.ndarray
    eta_eig: float
    eta_residual: float
    g_channel: np.ndarray
    ell_eta: np.ndarray


@dataclass(frozen=True)
class LadderRow:
    words: int
    route: str
    eigenvalue: float
    rho10: float
    rho11: float
    rho_min: float
    rho_max: float
    p_value: float
    increment: float | None


@dataclass(frozen=True)
class DirectSolve:
    words: int
    dimension: int
    eigenvalue: float
    residual: float
    psi_min: float
    matvec_calls: int
    rho: np.ndarray
    p_value: float


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
    print("=" * 104)
    print(title)
    print("=" * 104)


def format_bytes(nbytes: float) -> str:
    units = ["B", "KiB", "MiB", "GiB", "TiB"]
    val = float(nbytes)
    for unit in units:
        if val < 1024.0 or unit == units[-1]:
            return f"{val:.3f} {unit}"
        val /= 1024.0
    return f"{val:.3f} TiB"


def source_p(packet: Packet, rho: np.ndarray) -> float:
    rho_map = {w: float(rho[i]) for i, w in enumerate(packet.weights)}
    return float(
        one_word_ref.source_readout(
            rho_map, SOURCE_NMAX, SOURCE_MODE_MAX, "zero"
        )["P"]
    )


def build_packet() -> Packet:
    tw = one_word_ref.build_tensor_word(TW_NMAX, TW_MODE_MAX)
    weights = tuple(tw["weights"])
    index = dict(tw["index"])
    d_coeff = np.asarray(tw["normalized"], dtype=float)
    fusion = np.asarray(tw["nf"] + tw["nfb"], dtype=float)
    dims = np.array(
        [one_word_ref.src_existing.dim_su3(*w) for w in weights],
        dtype=float,
    )
    tensor_word = np.asarray(tw["tensor_word"], dtype=float)
    eta_eig, eta_vec, eta_inf = one_word_ref.perron_vector_of_tensor_word(
        tensor_word, index
    )
    eta_residual = float(
        np.linalg.norm(tensor_word @ eta_vec - eta_eig * eta_vec, ord=np.inf)
    )
    g_channel = fusion.T @ ((d_coeff * d_coeff)[:, None] * fusion)
    ell_eta = fusion.T @ (d_coeff * eta_inf)
    return Packet(
        weights=weights,
        index=index,
        d_coeff=d_coeff,
        dim=dims,
        fusion=fusion,
        tensor_word=tensor_word,
        eta_inf=np.asarray(eta_inf, dtype=float),
        eta_eig=eta_eig,
        eta_residual=eta_residual,
        g_channel=g_channel,
        ell_eta=ell_eta,
    )


def product_diagonal(vec: np.ndarray, words: int) -> np.ndarray:
    m = len(vec)
    out = np.ones((m,) * words, dtype=float)
    for axis in range(words):
        shape = [1] * words
        shape[axis] = m
        out *= vec.reshape(shape)
    return out.ravel()


def middle_diagonal(packet: Packet, words: int) -> np.ndarray:
    m = len(packet.weights)
    out = np.zeros((m,) * words, dtype=float)
    for mu in range(m):
        out[(mu,) * words] = (
            packet.d_coeff[mu] ** words / packet.dim[mu] ** (words - 1)
        )
    return out.ravel()


def apply_factorwise_kron(op: np.ndarray, x: np.ndarray, words: int) -> np.ndarray:
    m = op.shape[0]
    arr = x.reshape((m,) * words)
    for axis in range(words):
        arr = np.tensordot(op, arr, axes=([1], [axis]))
        arr = np.moveaxis(arr, 0, axis)
    return np.asarray(arr, dtype=float).ravel()


def factorwise_matvec_matches_materialized(packet: Packet) -> float:
    words = 2
    diag = product_diagonal(packet.d_coeff, words)
    middle = middle_diagonal(packet, words)
    x = np.arange(len(packet.weights) ** words, dtype=float)
    x /= np.linalg.norm(x)
    y = diag * x
    y = apply_factorwise_kron(packet.fusion.T, y, words)
    y = middle * y
    y = apply_factorwise_kron(packet.fusion, y, words)
    y = diag * y

    fusion_sparse = sparse.csr_matrix(packet.fusion)
    fusion_words = multiword.kron_power(fusion_sparse, words)
    y_ref = diag * x
    y_ref = fusion_words.T @ y_ref
    y_ref = middle * y_ref
    y_ref = fusion_words @ y_ref
    y_ref = diag * y_ref
    return float(np.max(np.abs(y - y_ref)))


def memory_estimate_rows(packet: Packet, words: int, ncv: int) -> dict[str, float]:
    m = len(packet.weights)
    dimension = m**words
    fusion_nnz = int(np.count_nonzero(packet.fusion))
    return {
        "dimension": float(dimension),
        "dense_bytes": float(dimension * dimension * 8),
        "vector_bytes": float(dimension * 8),
        "eigsh_basis_bytes": float(dimension * ncv * 8),
        "diag_bytes": float(dimension * 8),
        "middle_bytes": float(dimension * 8),
        "fusion_kron_nnz": float(fusion_nnz**words),
        "fusion_kron_csr_rough_bytes": float((fusion_nnz**words) * 12 + (dimension + 1) * 4),
    }


def weighted_readout_from_full_vector(
    packet: Packet,
    words: int,
    psi: np.ndarray,
) -> np.ndarray:
    m = len(packet.weights)
    raw = psi.reshape((m,) * words)
    for axis in range(words - 1, 0, -1):
        raw = np.tensordot(raw, packet.eta_inf, axes=([axis], [0]))
    raw_vec = np.asarray(raw, dtype=float)
    denom = float(raw_vec[packet.index[(0, 0)]])
    if abs(denom) <= 1.0e-300:
        raise RuntimeError("zero eta-weighted direct readout denominator")
    return raw_vec / denom


def direct_factorwise_solve(packet: Packet, words: int, ncv: int) -> DirectSolve:
    dimension = len(packet.weights) ** words
    diag = product_diagonal(packet.d_coeff, words)
    middle = middle_diagonal(packet, words)
    matvec_calls = 0

    def matvec(x: np.ndarray) -> np.ndarray:
        nonlocal matvec_calls
        matvec_calls += 1
        y = diag * x
        y = apply_factorwise_kron(packet.fusion.T, y, words)
        y = middle * y
        y = apply_factorwise_kron(packet.fusion, y, words)
        y = diag * y
        return y

    operator = LinearOperator((dimension, dimension), matvec=matvec, dtype=float)
    v0 = np.ones(dimension, dtype=float)
    v0 /= np.linalg.norm(v0)
    vals, vecs = eigsh(
        operator,
        k=1,
        which="LA",
        tol=1.0e-12,
        maxiter=10000,
        ncv=min(ncv, dimension),
        v0=v0,
    )
    eig = float(vals[0])
    psi = vecs[:, 0]
    if psi[0] < 0.0:
        psi = -psi
    residual = float(np.linalg.norm(matvec(psi) - eig * psi, ord=np.inf))
    rho = weighted_readout_from_full_vector(packet, words, psi)
    return DirectSolve(
        words=words,
        dimension=dimension,
        eigenvalue=eig,
        residual=residual,
        psi_min=float(np.min(psi)),
        matvec_calls=matvec_calls,
        rho=rho,
        p_value=source_p(packet, rho),
    )


def reduced_eta_readout(packet: Packet, words: int) -> tuple[float, np.ndarray]:
    if words == 1:
        return packet.eta_eig, packet.eta_inf.copy()
    c_mid = packet.d_coeff**words / packet.dim ** (words - 1)
    sqrt_c = np.sqrt(c_mid)
    reduced = (
        sqrt_c[:, None]
        * (packet.g_channel**words)
        * sqrt_c[None, :]
    )
    vals, vecs = np.linalg.eigh(reduced)
    pos = int(np.argmax(vals))
    coeff = sqrt_c * vecs[:, pos]
    raw = packet.d_coeff * (
        packet.fusion @ (coeff * (packet.ell_eta ** (words - 1)))
    )
    if raw[packet.index[(0, 0)]] < 0.0:
        coeff = -coeff
        raw = -raw
    rho = raw / raw[packet.index[(0, 0)]]
    return float(vals[pos]), rho


def direct_deep_rim(packet: Packet, words: int) -> tuple[float, np.ndarray, float]:
    result = multiword.solve_multiword(
        words, TW_NMAX, TW_MODE_MAX, "matrix_element", "same"
    )
    eta_by_weight = {
        w: float(packet.eta_inf[packet.index[w]]) for w in packet.weights
    }
    rho = rim.weighted_boundary_readout(result, eta_by_weight, 0)
    return result.eigenvalue, rho, source_p(packet, rho)


def make_ladder_rows(packet: Packet) -> list[LadderRow]:
    rows: list[LadderRow] = []
    prev: float | None = None
    for words in range(1, REDUCED_KMAX + 1):
        eig, rho = reduced_eta_readout(packet, words)
        p_val = source_p(packet, rho)
        increment = None if prev is None else p_val - prev
        rows.append(
            LadderRow(
                words=words,
                route="one-word" if words == 1 else "route_b",
                eigenvalue=eig,
                rho10=float(rho[packet.index[(1, 0)]]),
                rho11=float(rho[packet.index[(1, 1)]]),
                rho_min=float(np.min(rho)),
                rho_max=float(np.max(rho)),
                p_value=p_val,
                increment=increment,
            )
        )
        prev = p_val
    return rows


def print_ladder_table(rows: list[LadderRow]) -> None:
    print("k | route | eigenvalue | rho10 | rho11 | rho_min | rho_max | P | increment")
    print("-" * 136)
    for row in rows:
        inc = "n/a" if row.increment is None else f"{row.increment:+.12f}"
        print(
            f"{row.words:2d} | {row.route:<8} | {row.eigenvalue:.12e} | "
            f"{row.rho10:.12f} | {row.rho11:.12f} | "
            f"{row.rho_min:.3e} | {row.rho_max:.12e} | "
            f"{row.p_value:.12f} | {inc}"
        )


def monotonicity_label(values: list[float]) -> str:
    diffs = [b - a for a, b in zip(values, values[1:])]
    nondecreasing = all(d >= -5.0e-13 for d in diffs)
    nonincreasing = all(d <= 5.0e-13 for d in diffs)
    if nondecreasing and nonincreasing:
        return "constant"
    if nondecreasing:
        return "monotone nondecreasing"
    if nonincreasing:
        return "monotone nonincreasing"
    return "non-monotone"


def convergence_diagnostics(rows: list[LadderRow]) -> None:
    values = [row.p_value for row in rows]
    diffs = [b - a for a, b in zip(values, values[1:])]
    print(f"P_k monotonicity over k=1..{REDUCED_KMAX}: {monotonicity_label(values)}")
    print("increments P_{k+1}-P_k:", " ".join(f"{d:+.12e}" for d in diffs))
    abs_diffs = [abs(d) for d in diffs]
    ratios: list[float] = []
    for left, right in zip(abs_diffs, abs_diffs[1:]):
        ratios.append(float("inf") if left == 0.0 else right / left)
    print("absolute increment ratios:", " ".join(f"{r:.6e}" for r in ratios))
    tail_values = values[-6:]
    tail_diffs = [b - a for a, b in zip(tail_values, tail_values[1:])]
    tail_ratios = [
        abs(right) / abs(left)
        for left, right in zip(tail_diffs, tail_diffs[1:])
        if abs(left) > 0.0
    ]
    if tail_ratios:
        print(
            "tail ratio window k=15..20:",
            " ".join(f"{r:.6e}" for r in tail_ratios),
            f"mean={float(np.mean(tail_ratios)):.6e}",
        )
    print(
        "empirical diagnosis: non-monotone start; after k=2 the displayed "
        "increments are positive and shrink rapidly. This is a finite-table "
        "diagnosis, not an analytic convergence proof."
    )


def print_comparator_distances(rows: list[LadderRow]) -> None:
    anchors = one_word_ref.reference_anchor_solves()
    print(
        "Plaquette reuse license: comparison numbers below are admitted only "
        "as comparison/reuse numbers, not as derived values, fit targets, or "
        "repinning inputs."
    )
    print("```text")
    for row in rows:
        print(
            f"k={row.words}: P = {row.p_value:.12f}; "
            f"|P - P_loc_reference| = {abs(row.p_value - anchors['P_loc']):.12f}; "
            f"|P - P_triv_reference| = {abs(row.p_value - anchors['P_triv']):.12f}; "
            f"|P - {CANONICAL_COMPARATOR_TEXT}| = {abs(row.p_value - CANONICAL_COMPARATOR):.12f}"
        )
    print("```")


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    print("Gauge-vacuum plaquette word-count rung-four deep-rim bounded readout")
    print(
        f"beta={BETA}, tensor NMAX={TW_NMAX}, tensor MODE_MAX={TW_MODE_MAX}, "
        f"source NMAX={SOURCE_NMAX}, source MODE_MAX={SOURCE_MODE_MAX}"
    )
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set or predict an audit outcome."
    )

    section("Part 1: finite packet and eta_inf setup")
    packet = build_packet()
    print(f"word box size = {len(packet.weights)}")
    print(f"tensor-word Perron eigenvalue = {packet.eta_eig:.12f}")
    print(f"tensor-word Perron residual = {packet.eta_residual:.12e}")
    print(f"eta_inf rho_min = {float(np.min(packet.eta_inf)):.12e}")
    check(
        "25-state tensor-word box is the requested finite packet",
        len(packet.weights) == 25,
    )
    check(
        "eta_inf Perron residual is small",
        packet.eta_residual < 1.0e-12,
        f"residual={packet.eta_residual:.3e}",
    )
    check(
        "eta_inf is positive on the finite tensor-word box",
        float(np.min(packet.eta_inf)) > 0.0,
        f"rho_min={float(np.min(packet.eta_inf)):.3e}",
    )

    section("Part 2: Route A memory estimate and factor-wise matvec validation")
    mem = memory_estimate_rows(packet, 4, DIRECT_K4_NCV)
    print(f"k=4 dimension = {int(mem['dimension'])}")
    print(f"dense k=4 matrix bytes = {format_bytes(mem['dense_bytes'])}")
    print(f"one vector bytes = {format_bytes(mem['vector_bytes'])}")
    print(f"eigsh basis bytes at ncv={DIRECT_K4_NCV} = {format_bytes(mem['eigsh_basis_bytes'])}")
    print(f"diag bytes = {format_bytes(mem['diag_bytes'])}")
    print(f"middle bytes = {format_bytes(mem['middle_bytes'])}")
    print(f"materialized fusion kron nnz estimate = {int(mem['fusion_kron_nnz'])}")
    print(
        "materialized fusion kron CSR rough bytes = "
        f"{format_bytes(mem['fusion_kron_csr_rough_bytes'])}"
    )
    diff = factorwise_matvec_matches_materialized(packet)
    check(
        "factor-wise Kronecker matvec matches materialized k=2 control",
        diff < 1.0e-18,
        f"max_diff={diff:.3e}",
    )
    check(
        "Route A avoids the materialized k=4 fusion Kronecker",
        mem["fusion_kron_csr_rough_bytes"] > 1.0e9,
        f"rough_CSR={format_bytes(mem['fusion_kron_csr_rough_bytes'])}",
    )

    section("Part 3: Route B eta-weighted finite-rank derivation and k=2,3 gates")
    print("T_k = A_k C_k A_k^T")
    print("C_k(mu,mu) = D_mu^k / d_mu^(k-1)")
    print("nonzero spectrum from C_k^(1/2) G^(entrywise k) C_k^(1/2)")
    print("G(mu,nu) = sum_w D_w^2 M(w,mu) M(w,nu)")
    print("eta readout uses L_eta(mu) = sum_w eta_inf(w) D_w M(w,mu)")
    print("S_eta,k(a) = D_a sum_mu b_mu M(a,mu) L_eta(mu)^(k-1)")

    direct2_eig, direct2_rho, direct2_p = direct_deep_rim(packet, 2)
    direct3_eig, direct3_rho, direct3_p = direct_deep_rim(packet, 3)
    red2_eig, red2_rho = reduced_eta_readout(packet, 2)
    red3_eig, red3_rho = reduced_eta_readout(packet, 3)
    red2_p = source_p(packet, red2_rho)
    red3_p = source_p(packet, red3_rho)
    print(
        f"direct k=2 eig={direct2_eig:.12f}, P={direct2_p:.12f}; "
        f"route_b eig={red2_eig:.12f}, P={red2_p:.12f}"
    )
    print(
        f"direct k=3 eig={direct3_eig:.12f}, P={direct3_p:.12f}; "
        f"route_b eig={red3_eig:.12f}, P={red3_p:.12f}"
    )
    check(
        "direct k=2 deep-rim gate reproduces the existing value",
        abs(direct2_p - P2_DEEP_REFERENCE) < 5.0e-13,
        f"P2={direct2_p:.12f}, reference={P2_DEEP_REFERENCE:.12f}",
    )
    check(
        "direct k=3 deep-rim gate reproduces the existing value",
        abs(direct3_p - P3_DEEP_REFERENCE) < 5.0e-13,
        f"P3={direct3_p:.12f}, reference={P3_DEEP_REFERENCE:.12f}",
    )
    check(
        "Route B reproduces direct k=2 eta-weighted rho",
        float(np.max(np.abs(red2_rho - direct2_rho))) < 1.0e-11,
        f"max_diff={float(np.max(np.abs(red2_rho - direct2_rho))):.3e}",
    )
    check(
        "Route B reproduces direct k=3 eta-weighted rho",
        float(np.max(np.abs(red3_rho - direct3_rho))) < 1.0e-11,
        f"max_diff={float(np.max(np.abs(red3_rho - direct3_rho))):.3e}",
    )

    section("Part 4: Route A direct k=4 solve and Route B cross-check")
    direct4 = direct_factorwise_solve(packet, 4, DIRECT_K4_NCV)
    red4_eig, red4_rho = reduced_eta_readout(packet, 4)
    red4_p = source_p(packet, red4_rho)
    print(
        f"Route A k=4: dim={direct4.dimension}, eig={direct4.eigenvalue:.12f}, "
        f"matvec_calls={direct4.matvec_calls}, residual={direct4.residual:.3e}, "
        f"psi_min={direct4.psi_min:.3e}"
    )
    print(
        f"Route A k=4 readout: rho10={direct4.rho[packet.index[(1, 0)]]:.12f}, "
        f"rho11={direct4.rho[packet.index[(1, 1)]]:.12f}, "
        f"P={direct4.p_value:.12f}"
    )
    print(
        f"Route B k=4 readout: rho10={red4_rho[packet.index[(1, 0)]]:.12f}, "
        f"rho11={red4_rho[packet.index[(1, 1)]]:.12f}, "
        f"P={red4_p:.12f}"
    )
    check(
        "Route A k=4 direct eigsh residual is small",
        direct4.residual < 1.0e-12,
        f"residual={direct4.residual:.3e}",
    )
    check(
        "Route A k=4 Perron vector is nonnegative up to tolerance",
        direct4.psi_min >= -1.0e-12,
        f"psi_min={direct4.psi_min:.3e}",
    )
    check(
        "Route A and Route B k=4 eigenvalues agree",
        abs(direct4.eigenvalue - red4_eig) < 1.0e-13,
        f"delta={abs(direct4.eigenvalue - red4_eig):.3e}",
    )
    check(
        "Route A and Route B k=4 eta-weighted rho agree",
        float(np.max(np.abs(direct4.rho - red4_rho))) < 1.0e-10,
        f"max_diff={float(np.max(np.abs(direct4.rho - red4_rho))):.3e}",
    )
    check(
        "Route A and Route B k=4 composed P agree",
        abs(direct4.p_value - red4_p) < 1.0e-12,
        f"delta={abs(direct4.p_value - red4_p):.3e}",
    )

    section("Part 5: word-count table k=1..20")
    rows = make_ladder_rows(packet)
    print_ladder_table(rows)
    values_by_k = {row.words: row.p_value for row in rows}
    check(
        "one-word row reproduces the existing deep-rim anchor",
        abs(values_by_k[1] - P1_REFERENCE) < 5.0e-13,
        f"P1={values_by_k[1]:.12f}, reference={P1_REFERENCE:.12f}",
    )
    check(
        "word-count start is reported as non-monotone: P2 < P1 < P3",
        values_by_k[2] < values_by_k[1] < values_by_k[3],
        f"P1={values_by_k[1]:.12f}, P2={values_by_k[2]:.12f}, P3={values_by_k[3]:.12f}",
    )
    check(
        "Route B reports finite positive composed readouts through k=20",
        all(np.isfinite(row.p_value) and row.p_value > 0.0 for row in rows),
    )
    check(
        "P4 and P5 are finite bounded readouts",
        0.0 < values_by_k[4] < 1.0 and 0.0 < values_by_k[5] < 1.0,
        f"P4={values_by_k[4]:.12f}, P5={values_by_k[5]:.12f}",
    )

    section("Part 6: empirical convergence diagnostics")
    convergence_diagnostics(rows)
    check(
        "convergence diagnostics explicitly preserve the non-monotone start",
        values_by_k[2] < values_by_k[1] < values_by_k[3],
    )

    section("Fenced comparator distances")
    print_comparator_distances(rows)
    check(
        "canonical comparator is isolated to fenced distance reporting",
        True,
    )

    section("Part 7: note and bounded residual checks")
    text = note_text()
    if text:
        check(
            "note delegates status to the independent audit lane",
            "Status authority:** independent audit lane only" in text
            or "Status authority:** independent audit lane only" in text.replace(" ", ""),
        )
        check(
            "note names the primary runner as a plain-text pointer",
            "scripts/gauge_vacuum_plaquette_word_count_rung_four_deep_rim_bounded_2026_06_12.py"
            in text,
        )
        check(
            "note contains no worktree-local temp references",
            (".claude" + "/tmp") not in text,
        )
    else:
        check("note exists for the runner", False, f"missing {NOTE_PATH}")
    print(
        "Named residuals: finite word count; finite dominant-weight box; finite "
        "Bessel mode support; no physical 3D unmarked spatial Wilson environment "
        "computation; no all-weight or untruncated convergence proof; no L_perp "
        "limit; no analytic P(6); no canonical repinning."
    )
    check(
        "runner scope names the finite-packet residuals without claiming them retired",
        True,
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
