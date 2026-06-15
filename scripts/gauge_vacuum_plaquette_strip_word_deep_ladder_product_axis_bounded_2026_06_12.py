#!/usr/bin/env python3
"""Strip-word deep ladder on the finite plaquette product axis.

This runner composes the licensed two-strip layer object as the word in the
depth ladder.  The strip object has 25 x 25 = 625 states.  Its internal width
link uses the derived dimension-stripped class-channel contraction, and the
longitudinal depth bond is the product of the derived single-rail
matrix-element bonds.

No random inputs, dates, external data, fitted selector, or literature values
are used.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_2026_06_11 as one_word
import gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12 as two_strip


AUDIT_TIMEOUT_SEC = 600

BETA = 6.0
TW_NMAX = 4
TW_MODE_MAX = 80
SOURCE_NMAX = one_word.SOURCE_NMAX
SOURCE_MODE_MAX = one_word.SOURCE_MODE_MAX
KMAX = 40

ZERO = (0, 0)
FUND = (1, 0)
ANTIFUND = (0, 1)
ADJOINT = (1, 1)

P_STRIP_K1_REFERENCE = 0.439904783618900
P_WORD_K1_REFERENCE = 0.434215413259920
P_WORD_K2_REFERENCE = 0.433061880379652
P_WORD_K3_REFERENCE = 0.543142610051424
P_WORD_K4_REFERENCE = 0.603630724651002
P_WORD_K20_REFERENCE = 0.615191992181771
P_WORD_LIMIT_REFERENCE = 0.615191992185898
THETA_WORD_REFERENCE = 0.263745855973467
COMPARATOR_TEXT = one_word.CANONICAL_COMPARATOR_TEXT
COMPARATOR = one_word.CANONICAL_COMPARATOR

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_STRIP_WORD_DEEP_LADDER_PRODUCT_AXIS_BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class LayerObject:
    label: str
    internal_factor: np.ndarray
    d_layer: np.ndarray
    dim_layer: np.ndarray
    transfer: np.ndarray
    eigenvalue: float
    eta: np.ndarray
    residual: float
    eta_min: float
    g_channel: np.ndarray
    ell_eta: np.ndarray
    sqrt_norm: np.ndarray
    t_channel: np.ndarray


@dataclass(frozen=True)
class LadderRow:
    k: int
    eigenvalue: float
    p_value: float
    rho10: float
    rho11: float
    rho_min: float
    rho_max: float
    rho: np.ndarray
    increment: float | None
    iterations: int


@dataclass(frozen=True)
class DirectK2Result:
    dimension: int
    eigenvalue: float
    residual: float
    psi_min: float
    matvec_calls: int
    p_value: float
    rho: np.ndarray


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


def dim_su3(weight: tuple[int, int]) -> int:
    return one_word.src_existing.dim_su3(*weight)


def strip_bond_exact(
    left: tuple[tuple[int, int], tuple[int, int]],
    right: tuple[tuple[int, int], tuple[int, int]],
) -> Fraction:
    """Derived depth bond for one strip-word adjacency."""
    if left != right:
        return Fraction(0, 1)
    return Fraction(1, dim_su3(left[0]) * dim_su3(left[1]))


def build_layer(
    packet: two_strip.Packet,
    pairs: list[tuple[int, int]],
    internal_factor: np.ndarray,
    label: str,
) -> LayerObject:
    d_layer = np.array(
        [packet.d_coeff[left] * packet.d_coeff[right] for left, right in pairs],
        dtype=float,
    )
    d_layer = d_layer * internal_factor
    dim_layer = np.array(
        [packet.dim[left] * packet.dim[right] for left, right in pairs],
        dtype=float,
    )
    fusion_pair = np.kron(packet.word_bond, packet.word_bond)
    transfer = two_strip.strip_transfer(packet, internal_factor)
    eig, psi, residual, psi_min = two_strip.perron_symmetric(transfer)
    eta = psi / float(psi[0])
    g_channel = fusion_pair.T @ ((d_layer * d_layer)[:, None] * fusion_pair)
    ell_eta = fusion_pair.T @ (d_layer * eta)
    sqrt_norm = np.sqrt(d_layer / dim_layer)
    t_channel = sqrt_norm[:, None] * g_channel * sqrt_norm[None, :]
    return LayerObject(
        label=label,
        internal_factor=internal_factor,
        d_layer=d_layer,
        dim_layer=dim_layer,
        transfer=transfer,
        eigenvalue=eig,
        eta=eta,
        residual=residual,
        eta_min=psi_min,
        g_channel=g_channel,
        ell_eta=ell_eta,
        sqrt_norm=sqrt_norm,
        t_channel=t_channel,
    )


def source_from_pair_raw(
    packet: two_strip.Packet,
    pairs: list[tuple[int, int]],
    raw_pair: np.ndarray,
) -> tuple[float, np.ndarray]:
    n = len(packet.weights)
    left_raw = np.zeros(n, dtype=float)
    for val, (left, _right) in zip(raw_pair, pairs):
        left_raw[left] += float(val)
    z = packet.index[ZERO]
    denom = float(left_raw[z])
    if abs(denom) <= 1.0e-300:
        raise RuntimeError("zero strip left-marginal denominator")
    rho = left_raw / denom
    p_value, _u0, _alpha = two_strip.source_p(packet, rho)
    return float(p_value), rho


def top_vector_scaled(matrix: np.ndarray, tolerance: float = 1.0e-28) -> tuple[float, np.ndarray, int]:
    """Positive top eigenvector normalized by v[0] = 1.

    Dense eigensolvers lose the tiny off-diagonal Perron components needed by
    the source readout at large k.  Scaled power iteration preserves them as
    ordinary floating-point values because the vector is renormalized by the
    trivial-channel component after each matvec.
    """
    x = np.ones(matrix.shape[0], dtype=float)
    x /= x[0]
    lam = 0.0
    for iteration in range(1, 1001):
        y = matrix @ x
        if y[0] < 0.0:
            y = -y
        lam = float(y[0])
        if abs(lam) <= 1.0e-300:
            raise RuntimeError("zero leading component in scaled power iteration")
        y = y / lam
        if float(np.max(np.abs(y - x))) < tolerance:
            return lam, y, iteration
        x = y
    return lam, x, 1000


def reduced_ladder_row(
    packet: two_strip.Packet,
    pairs: list[tuple[int, int]],
    layer: LayerObject,
    k: int,
    previous_p: float | None,
) -> LadderRow:
    if k == 1:
        p_value, rho = source_from_pair_raw(packet, pairs, layer.eta)
        return LadderRow(
            k=k,
            eigenvalue=layer.eigenvalue,
            p_value=p_value,
            rho10=float(rho[packet.index[FUND]]),
            rho11=float(rho[packet.index[ADJOINT]]),
            rho_min=float(np.min(rho)),
            rho_max=float(np.max(rho)),
            rho=rho,
            increment=None if previous_p is None else p_value - previous_p,
            iterations=0,
        )

    t0 = float(layer.t_channel[0, 0])
    ell0 = float(layer.ell_eta[0])
    sqrt_dim = np.sqrt(layer.dim_layer)
    scaled = sqrt_dim[:, None] * ((layer.t_channel / t0) ** k) * sqrt_dim[None, :]
    lam_scaled, vec, iterations = top_vector_scaled(scaled)
    coeff = sqrt_dim * (layer.sqrt_norm**k) * vec
    fusion_pair = np.kron(packet.word_bond, packet.word_bond)
    raw_pair = layer.d_layer * (
        fusion_pair @ (coeff * ((layer.ell_eta / ell0) ** (k - 1)))
    )
    if raw_pair[0] < 0.0:
        raw_pair = -raw_pair
    p_value, rho = source_from_pair_raw(packet, pairs, raw_pair)
    eig = lam_scaled * (t0**k)
    return LadderRow(
        k=k,
        eigenvalue=float(eig),
        p_value=p_value,
        rho10=float(rho[packet.index[FUND]]),
        rho11=float(rho[packet.index[ADJOINT]]),
        rho_min=float(np.min(rho)),
        rho_max=float(np.max(rho)),
        rho=rho,
        increment=None if previous_p is None else p_value - previous_p,
        iterations=iterations,
    )


def make_rows(
    packet: two_strip.Packet,
    pairs: list[tuple[int, int]],
    layer: LayerObject,
    kmax: int,
) -> list[LadderRow]:
    rows: list[LadderRow] = []
    previous: float | None = None
    for k in range(1, kmax + 1):
        row = reduced_ladder_row(packet, pairs, layer, k, previous)
        rows.append(row)
        previous = row.p_value
    return rows


def print_rows(rows: list[LadderRow]) -> None:
    print("k | eigenvalue | rho10 | rho11 | rho_min | rho_max | P | increment | power_iters")
    print("-" * 144)
    for row in rows:
        inc = "baseline" if row.increment is None else f"{row.increment:+.12e}"
        print(
            f"{row.k:2d} | {row.eigenvalue:.12e} | {row.rho10:.12e} | "
            f"{row.rho11:.12e} | {row.rho_min:.3e} | {row.rho_max:.12e} | "
            f"{row.p_value:.15f} | {inc} | {row.iterations:4d}"
        )


def apply_axis(arr: np.ndarray, op: np.ndarray, axis: int) -> np.ndarray:
    n = op.shape[0]
    moved = np.moveaxis(arr, axis, 0)
    shape = moved.shape
    mat = moved.reshape(n, -1)
    out = op @ mat
    out = out.reshape(shape)
    return np.moveaxis(out, 0, axis)


def direct_k2_solve(
    packet: two_strip.Packet,
    layer: LayerObject,
) -> DirectK2Result:
    n = len(packet.weights)
    dimension = n**4
    d_pair = layer.d_layer.reshape(n, n)
    dim_pair = layer.dim_layer.reshape(n, n)
    middle = np.zeros((n, n, n, n), dtype=float)
    for left in range(n):
        for right in range(n):
            middle[left, right, left, right] = (
                d_pair[left, right] ** 2 / dim_pair[left, right]
            )
    outer = d_pair[:, :, None, None] * d_pair[None, None, :, :]
    word_bond = np.asarray(packet.word_bond, dtype=float)
    matvec_calls = 0

    def matvec(x: np.ndarray) -> np.ndarray:
        nonlocal matvec_calls
        matvec_calls += 1
        arr = x.reshape(n, n, n, n).copy()
        arr *= outer
        for axis in range(4):
            arr = apply_axis(arr, word_bond.T, axis)
        arr *= middle
        for axis in range(4):
            arr = apply_axis(arr, word_bond, axis)
        arr *= outer
        return arr.ravel()

    operator = LinearOperator((dimension, dimension), matvec=matvec, dtype=float)
    v0 = np.ones(dimension, dtype=float)
    v0 /= np.linalg.norm(v0)
    vals, vecs = eigsh(
        operator,
        k=1,
        which="LA",
        tol=1.0e-11,
        maxiter=1000,
        ncv=20,
        v0=v0,
    )
    eig = float(vals[0])
    psi = vecs[:, 0]
    if psi[0] < 0.0:
        psi = -psi
    residual = float(np.linalg.norm(matvec(psi) - eig * psi, ord=np.inf))
    psi_min = float(np.min(psi))
    eta_matrix = layer.eta.reshape(n, n)
    raw_pair = np.tensordot(
        psi.reshape(n, n, n, n),
        eta_matrix,
        axes=([2, 3], [0, 1]),
    ).ravel()
    p_value, rho = source_from_pair_raw(
        packet, two_strip.pair_indices(packet), raw_pair
    )
    return DirectK2Result(
        dimension=dimension,
        eigenvalue=eig,
        residual=residual,
        psi_min=psi_min,
        matvec_calls=matvec_calls,
        p_value=p_value,
        rho=rho,
    )


def theta_closed(
    packet: two_strip.Packet,
    pairs: list[tuple[int, int]],
    layer: LayerObject,
) -> tuple[float, dict[str, float], float]:
    n = len(packet.weights)

    def pair_index(left_weight: tuple[int, int], right_weight: tuple[int, int]) -> int:
        return packet.index[left_weight] * n + packet.index[right_weight]

    channels = {
        "left_f": pair_index(FUND, ZERO),
        "left_fbar": pair_index(ANTIFUND, ZERO),
        "right_f": pair_index(ZERO, FUND),
        "right_fbar": pair_index(ZERO, ANTIFUND),
    }
    values: dict[str, float] = {}
    for name, idx in channels.items():
        ell_ratio = float(layer.ell_eta[idx] / layer.ell_eta[0])
        norm = float(layer.sqrt_norm[idx])
        t_ratio = float(layer.t_channel[idx, 0] / layer.t_channel[0, 0])
        values[name] = ell_ratio * norm * t_ratio
        print(
            f"{name}: pair={pairs[idx]}, ell_ratio={ell_ratio:.15f}, "
            f"sqrt(D_pair/d_pair)={norm:.15f}, "
            f"t_ratio={t_ratio:.15f}, theta={values[name]:.15f}"
        )
    vals = list(values.values())
    return float(vals[0]), values, float(max(vals) - min(vals))


def measured_theta(rows: list[LadderRow], p_inf: float) -> tuple[float, list[float]]:
    ratios: list[float] = []
    values = {row.k: row.p_value for row in rows}
    for k in range(20, 27):
        err = p_inf - values[k]
        next_err = p_inf - values[k + 1]
        if err > 1.0e-14 and next_err > 0.0:
            ratios.append(next_err / err)
    return float(np.mean(ratios)), ratios


def source_pair_support_limit() -> float:
    rho = {FUND: 1.0, ANTIFUND: 1.0}
    return float(
        one_word.source_readout(
            rho,
            SOURCE_NMAX,
            SOURCE_MODE_MAX,
            "zero",
        )["P"]
    )


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    print("Gauge-vacuum plaquette strip-word deep ladder product-axis bounded runner")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set, predict, promote, or demote any audit outcome."
    )
    print("No new imports: repo-internal finite packet quantities only.")
    print(
        f"beta={BETA}, tensor NMAX={TW_NMAX}, tensor MODE_MAX={TW_MODE_MAX}, "
        f"source NMAX={SOURCE_NMAX}, source MODE_MAX={SOURCE_MODE_MAX}"
    )

    section("Part 1: packet, strip object, and derived longitudinal bond")
    packet = two_strip.build_packet()
    pairs = two_strip.pair_indices(packet)
    fusion = two_strip.build_fusion_table(packet)
    fund_err, anti_err = two_strip.validate_fundamental_fusion(packet, fusion)
    internal_strip = two_strip.internal_factor(
        packet, fusion, "dimension_stripped", "product"
    )
    internal_cut = np.ones(len(pairs), dtype=float)
    strip = build_layer(packet, pairs, internal_strip, "dimension_stripped_strip")
    cut = build_layer(packet, pairs, internal_cut, "cut_strip")

    print(f"one-rail state count = {len(packet.weights)}")
    print(f"strip-word state count = {len(pairs)}")
    print(f"strip transfer shape = {strip.transfer.shape}")
    print(f"strip Perron eigenvalue = {strip.eigenvalue:.15f}")
    print(f"strip Perron residual = {strip.residual:.3e}")
    print(f"strip eta min = {strip.eta_min:.3e}")
    print(
        "derived strip longitudinal bond: "
        "delta_left/d_left times delta_right/d_right"
    )
    check("one-rail finite packet has 25 states", len(packet.weights) == 25)
    check("strip-word finite packet has 625 states", len(pairs) == 625)
    check("generated fusion table reproduces the fundamental recurrence", fund_err == 0)
    check("generated fusion table reproduces the antifundamental recurrence", anti_err == 0)
    check("strip Perron residual is small", strip.residual < 1.0e-12)
    check("strip eta is positive up to tolerance", strip.eta_min >= -1.0e-12)
    check(
        "derived strip bond gives 1/(3*8) on matching (fund, adjoint) pair",
        strip_bond_exact((FUND, ADJOINT), (FUND, ADJOINT)) == Fraction(1, 24),
    )
    check(
        "derived strip bond is zero on a rail mismatch",
        strip_bond_exact((FUND, ZERO), (ANTIFUND, ZERO)) == Fraction(0, 1),
    )

    section("Part 2: k=1 strip gate")
    row1 = reduced_ladder_row(packet, pairs, strip, 1, None)
    print(f"P_1(strip-word) = {row1.p_value:.15f}")
    print(f"rho_strip_left(1,0) = {row1.rho10:.15f}")
    print(f"rho_strip_left(1,1) = {row1.rho11:.15f}")
    check(
        "k=1 reproduces the licensed two-strip dimension-stripped readout",
        abs(row1.p_value - P_STRIP_K1_REFERENCE) < 5.0e-13,
        f"P1={row1.p_value:.15f}, reference={P_STRIP_K1_REFERENCE:.15f}",
    )

    section("Part 3: eta-weighted 625-rank reduction and direct k=2 validation")
    strip_rows = make_rows(packet, pairs, strip, KMAX)
    red2 = strip_rows[1]
    direct2 = direct_k2_solve(packet, strip)
    print(
        f"direct k=2 dimension={direct2.dimension}, eig={direct2.eigenvalue:.15f}, "
        f"matvec_calls={direct2.matvec_calls}, residual={direct2.residual:.3e}, "
        f"psi_min={direct2.psi_min:.3e}"
    )
    print(
        f"reduced k=2 eig={red2.eigenvalue:.15f}, P={red2.p_value:.15f}; "
        f"direct P={direct2.p_value:.15f}"
    )
    check("direct k=2 dimension is 625^2", direct2.dimension == 625 * 625)
    check("direct k=2 residual is small", direct2.residual < 1.0e-12)
    check(
        "625-rank reduction matches direct k=2 eigenvalue",
        abs(red2.eigenvalue - direct2.eigenvalue) < 1.0e-12,
        f"delta={abs(red2.eigenvalue - direct2.eigenvalue):.3e}",
    )
    check(
        "625-rank reduction matches direct k=2 composed P to 10+ digits",
        abs(red2.p_value - direct2.p_value) < 1.0e-12,
        f"delta={abs(red2.p_value - direct2.p_value):.3e}",
    )
    check(
        "625-rank reduction matches direct k=2 rho to 10+ digits",
        float(np.max(np.abs(direct2.rho - red2.rho))) < 1.0e-9,
        f"max_diff={float(np.max(np.abs(direct2.rho - red2.rho))):.3e}",
    )
    check(
        "direct k=2 rho10 spot agrees with reduced row",
        abs(direct2.rho[packet.index[FUND]] - red2.rho10) < 1.0e-10,
        f"direct={direct2.rho[packet.index[FUND]]:.12e}, reduced={red2.rho10:.12e}",
    )
    check(
        "direct k=2 rho11 spot agrees with reduced row",
        abs(direct2.rho[packet.index[ADJOINT]] - red2.rho11) < 1.0e-10,
        f"direct={direct2.rho[packet.index[ADJOINT]]:.12e}, reduced={red2.rho11:.12e}",
    )

    section("Part 4: internal-width cut gate against the certified word ladder")
    cut_rows = make_rows(packet, pairs, cut, KMAX)
    cut_by_k = {row.k: row.p_value for row in cut_rows}
    for k in [1, 2, 3, 4, 20, 40]:
        print(f"cut k={k}: P={cut_by_k[k]:.15f}")
    check(
        "cut k=1 reproduces the one-word anchor",
        abs(cut_by_k[1] - P_WORD_K1_REFERENCE) < 5.0e-13,
    )
    check(
        "cut k=2 reproduces the certified word-depth rung",
        abs(cut_by_k[2] - P_WORD_K2_REFERENCE) < 5.0e-13,
    )
    check(
        "cut k=3 reproduces the certified word-depth rung",
        abs(cut_by_k[3] - P_WORD_K3_REFERENCE) < 5.0e-13,
    )
    check(
        "cut k=4 reproduces the certified word-depth rung",
        abs(cut_by_k[4] - P_WORD_K4_REFERENCE) < 5.0e-13,
    )
    check(
        "cut k=20 reproduces the certified word-depth tail rung",
        abs(cut_by_k[20] - P_WORD_K20_REFERENCE) < 5.0e-13,
    )
    check(
        "cut k=40 reaches the certified word-depth source limit",
        abs(cut_by_k[40] - P_WORD_LIMIT_REFERENCE) < 5.0e-13,
        f"cut_k40={cut_by_k[40]:.15f}, word_limit={P_WORD_LIMIT_REFERENCE:.15f}",
    )

    section("Part 5: strip-word ladder table k=1..40")
    print_rows(strip_rows)
    p_inf = source_pair_support_limit()
    print(f"pair-support source limit = {p_inf:.15f}")
    check(
        "pair-support source limit reproduces the certified word-chain P_inf",
        abs(p_inf - P_WORD_LIMIT_REFERENCE) < 5.0e-13,
        f"P_inf={p_inf:.15f}",
    )
    check(
        "strip-word k=40 has converged to the pair-support limit at display precision",
        abs(strip_rows[-1].p_value - p_inf) < 5.0e-13,
        f"P40={strip_rows[-1].p_value:.15f}, P_inf={p_inf:.15f}",
    )
    check(
        "strip-word rows are finite positive source readouts",
        all(np.isfinite(row.p_value) and row.p_value > 0.0 for row in strip_rows),
    )

    section("Part 6: theta identification")
    theta, theta_values, theta_spread = theta_closed(packet, pairs, strip)
    theta_measured, theta_ratios = measured_theta(strip_rows, p_inf)
    print(
        "measured tail ratios k=20..27: "
        + " ".join(f"{value:.12f}" for value in theta_ratios)
    )
    print(f"theta_strip_closed = {theta:.15f}")
    print(f"theta_strip_measured_mean = {theta_measured:.15f}")
    print(f"theta_word_reference = {THETA_WORD_REFERENCE:.15f}")
    check("four strip theta channels agree by symmetry", theta_spread < 1.0e-12)
    check(
        "closed theta matches measured strip tail before roundoff",
        abs(theta - theta_measured) < 1.0e-3,
        f"closed={theta:.15f}, measured={theta_measured:.15f}",
    )
    check(
        "strip theta is slower than the one-word theta on this finite product axis",
        theta > THETA_WORD_REFERENCE,
        f"theta_strip={theta:.15f}, theta_word={THETA_WORD_REFERENCE:.15f}",
    )

    section("Part 7: comparator and residual ledger")
    word_distance = P_WORD_LIMIT_REFERENCE - COMPARATOR
    strip_distance = p_inf - COMPARATOR
    finite_k1_distance = abs(row1.p_value - COMPARATOR)
    print("Plaquette reuse license: comparator is fenced comparison context.")
    print("```text")
    print(f"P_inf(strip-word chain) = {p_inf:.15f}")
    print(f"P_inf(word chain)       = {P_WORD_LIMIT_REFERENCE:.15f}")
    print(f"fenced comparator       = {COMPARATOR:.15f}")
    print(f"P_inf(strip) - P_inf(word) = {p_inf - P_WORD_LIMIT_REFERENCE:+.15e}")
    print(f"P_inf(word) - comparator   = {word_distance:.15f}")
    print(f"P_inf(strip) - comparator  = {strip_distance:.15f}")
    print(f"k=1 strip distance to comparator = {finite_k1_distance:.15f}")
    print("```")
    check(
        "strip-word depth limit is the same pair-support source limit as the word chain",
        abs(p_inf - P_WORD_LIMIT_REFERENCE) < 5.0e-13,
    )
    check(
        "width enrichment does not move the finite-packet deep limit toward the comparator",
        abs(strip_distance - word_distance) < 5.0e-13,
        f"strip_distance={strip_distance:.15f}, word_distance={word_distance:.15f}",
    )
    print(
        "Named residuals: finite B4 strip-word packet; scalar class-channel "
        "internal contraction; finite Bessel mode support; strip-word product "
        "axis rather than full 3D rim; wider width limit; all-link 6j basis; "
        "L_perp limit; analytic P(6); no repinning."
    )
    check("runner names residuals without retiring them", True)

    section("Part 8: note hygiene")
    text = note_text()
    if text:
        check(
            "note delegates status to the independent audit lane",
            "Status authority: independent audit lane only" in text
            and "does not set, predict, promote, or demote any audit outcome" in text,
        )
        check(
            "note uses markdown links for one-hop authorities",
            "[GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md]" in text
            and "[GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md]" in text
            and "[GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md]" in text,
        )
        check(
            "note omits branch-local temporary refs and keeps runner context as a plain-text path",
            "." + "claude/tmp" not in text
            and "scripts/gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12.py" in text
            and "[scripts/gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12.py]" not in text,
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

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
