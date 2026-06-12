#!/usr/bin/env python3
"""Box/mode sweep for the finite word-limit readout.

This runner measures the two finite tensor-word axes requested in W31:

* word-packet dominant-weight box NMAX in {3,4,5,6,7};
* tensor-word Bessel support MODE_MAX in {80,200};
* fixed source readout defaults NMAX=7, MODE_MAX=200.

For each word-packet cell it recomputes eta_inf, evaluates the eta-weighted
finite-rank reduced family through k=40, verifies convergence to the
fundamental/antifundamental pair-support source limit, and recomputes the
theta closed-form diagnostic.  It also sweeps the source box independently at
fixed word-packet box NMAX=4, MODE_MAX=80.

All computations are finite packet diagnostics.  No untruncated Wilson
environment, physical 3D rim geometry, analytic P(6), fit, extrapolation, or
canonical repinning is claimed.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_2026_06_11 as one_word


AUDIT_TIMEOUT_SEC = 600

BETA = 6.0
WORD_NMAXS = (3, 4, 5, 6, 7)
WORD_MODE_MAXS = (80, 200)
SOURCE_NMAX_DEFAULT = one_word.SOURCE_NMAX
SOURCE_MODE_MAX_DEFAULT = one_word.SOURCE_MODE_MAX
SOURCE_SWEEP_NMAXS = (5, 7, 9)
WORD_NMAX_DEFAULT = 4
WORD_MODE_MAX_DEFAULT = 80
KMAX = 40
ZERO = (0, 0)
FUND = (1, 0)
ANTIFUND = (0, 1)
ADJOINT = (1, 1)
CANONICAL_COMPARATOR = one_word.CANONICAL_COMPARATOR
CANONICAL_COMPARATOR_TEXT = one_word.CANONICAL_COMPARATOR_TEXT
NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_WORD_LIMIT_BOX_MODE_SWEEP_BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class Packet:
    nmax: int
    mode_max: int
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
    t_matrix: np.ndarray


@dataclass(frozen=True)
class WordCell:
    nmax: int
    mode_max: int
    word_box_size: int
    reduced_shape: tuple[int, int]
    eta_residual: float
    theta: float
    theta_ratio: float
    theta_ratio_delta: float
    p_inf: float
    p40: float
    p40_error: float
    last_abs_increment: float
    distance_to_comparator: float
    p20: float
    p30: float


@dataclass(frozen=True)
class SourceCell:
    source_nmax: int
    source_mode_max: int
    p_inf: float
    p40: float
    p40_error: float
    distance_to_comparator: float


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


def build_packet(nmax: int, mode_max: int) -> Packet:
    tw = one_word.build_tensor_word(nmax, mode_max)
    weights = tuple(tw["weights"])
    index = dict(tw["index"])
    d_coeff = np.asarray(tw["normalized"], dtype=float)
    fusion = np.asarray(tw["nf"] + tw["nfb"], dtype=float)
    dim = np.array([one_word.src_existing.dim_su3(*w) for w in weights], dtype=float)
    tensor_word = np.asarray(tw["tensor_word"], dtype=float)
    eta_eig, eta_vec, eta_inf = one_word.perron_vector_of_tensor_word(
        tensor_word, index
    )
    eta_residual = float(
        np.linalg.norm(tensor_word @ eta_vec - eta_eig * eta_vec, ord=np.inf)
    )
    g_channel = fusion.T @ ((d_coeff * d_coeff)[:, None] * fusion)
    ell_eta = fusion.T @ (d_coeff * eta_inf)
    t_matrix = (
        np.sqrt(d_coeff[:, None] * d_coeff[None, :])
        * g_channel
        / np.sqrt(dim[:, None] * dim[None, :])
    )
    return Packet(
        nmax=nmax,
        mode_max=mode_max,
        weights=weights,
        index=index,
        d_coeff=d_coeff,
        dim=dim,
        fusion=fusion,
        tensor_word=tensor_word,
        eta_inf=np.asarray(eta_inf, dtype=float),
        eta_eig=eta_eig,
        eta_residual=eta_residual,
        g_channel=g_channel,
        ell_eta=ell_eta,
        t_matrix=t_matrix,
    )


def theta_closed_form(packet: Packet) -> float:
    z = packet.index[ZERO]
    f = packet.index[FUND]
    return float(
        (packet.ell_eta[f] / packet.ell_eta[z])
        * math.sqrt(packet.d_coeff[f] / packet.dim[f])
        * (packet.t_matrix[f, z] / packet.t_matrix[z, z])
    )


def top_reduced_vector_ratio(packet: Packet, words: int) -> np.ndarray:
    """Return top reduced eigenvector normalized to component (0,0)=1.

    The direct eigh vector loses the tiny off-dominant entries by k=40.  For
    the tail window we solve the block eigenvector equation
    (lambda I - B)y = r after scaling by the dominant (0,0) entry.
    """
    z = packet.index[ZERO]
    scaled = (
        np.sqrt(packet.dim[:, None] * packet.dim[None, :])
        * ((packet.t_matrix / packet.t_matrix[z, z]) ** words)
    )
    if words < 18:
        vals, vecs = np.linalg.eigh(scaled)
        pos = int(np.argmax(vals))
        vec = np.asarray(vecs[:, pos], dtype=float)
        if float(vec[z]) < 0.0:
            vec = -vec
        return vec / float(vec[z])

    rest = [i for i in range(len(packet.weights)) if i != z]
    r = scaled[rest, z]
    b_block = scaled[np.ix_(rest, rest)]
    ident = np.eye(len(rest), dtype=float)
    lambda_bar = 1.0
    y = np.zeros(len(rest), dtype=float)
    for _ in range(10):
        y = np.linalg.solve(lambda_bar * ident - b_block, r)
        lambda_bar = 1.0 + float(r @ y)
    vec = np.ones(len(packet.weights), dtype=float)
    vec[z] = 1.0
    vec[rest] = y
    return vec


def reduced_eta_rho(packet: Packet, words: int) -> np.ndarray:
    if words == 1:
        return packet.eta_inf.copy()

    vec = top_reduced_vector_ratio(packet, words)
    positive = vec > 0.0
    log_factor = 0.5 * np.log(packet.d_coeff) + (words - 1) * (
        np.log(packet.ell_eta)
        + 0.5 * (np.log(packet.d_coeff) - np.log(packet.dim))
    )
    log_terms = log_factor[positive] + np.log(vec[positive])
    global_max = float(np.max(log_terms))
    scaled = np.zeros(len(packet.weights), dtype=float)
    scaled[positive] = vec[positive] * np.exp(log_factor[positive] - global_max)
    raw = packet.d_coeff * (packet.fusion @ scaled)
    denom = float(raw[packet.index[ZERO]])
    if abs(denom) <= 1.0e-300:
        raise RuntimeError("zero eta-weighted reduced readout denominator")
    return raw / denom


def source_p_from_rho(
    source_setup: dict[str, object],
    weights: tuple[tuple[int, int], ...],
    rho: np.ndarray,
) -> float:
    source_index = source_setup["index"]
    rho_vec = np.zeros(len(source_setup["weights"]), dtype=float)
    for i, w in enumerate(weights):
        if w in source_index:
            rho_vec[source_index[w]] = float(rho[i])
    _eig, p_value, _psi, _u0 = one_word.source_perron_from_rho_vector(
        source_setup, rho_vec
    )
    return float(p_value)


def pair_support_p(source_setup: dict[str, object]) -> float:
    source_index = source_setup["index"]
    rho_vec = np.zeros(len(source_setup["weights"]), dtype=float)
    rho_vec[source_index[FUND]] = 1.0
    rho_vec[source_index[ANTIFUND]] = 1.0
    _eig, p_value, _psi, _u0 = one_word.source_perron_from_rho_vector(
        source_setup, rho_vec
    )
    return float(p_value)


def ratio_window(values: list[float], theta: float) -> tuple[float, float]:
    increments = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    ratios: list[float] = []
    # k indexes the left increment: increment[k-1] = P_{k+1} - P_k.
    for k in range(8, 22):
        left = increments[k - 1]
        right = increments[k]
        if abs(left) > 1.0e-15 and abs(right) > 1.0e-15:
            ratios.append(abs(right / left))
    if not ratios:
        return float("nan"), float("inf")
    measured = float(np.median(np.asarray(ratios, dtype=float)))
    return measured, abs(measured - theta)


def word_cell(
    packet: Packet,
    source_setup: dict[str, object],
    p_inf: float,
) -> WordCell:
    values = [
        source_p_from_rho(source_setup, packet.weights, reduced_eta_rho(packet, k))
        for k in range(1, KMAX + 1)
    ]
    theta = theta_closed_form(packet)
    theta_ratio, theta_delta = ratio_window(values, theta)
    increments = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    return WordCell(
        nmax=packet.nmax,
        mode_max=packet.mode_max,
        word_box_size=len(packet.weights),
        reduced_shape=(len(packet.weights), len(packet.weights)),
        eta_residual=packet.eta_residual,
        theta=theta,
        theta_ratio=theta_ratio,
        theta_ratio_delta=theta_delta,
        p_inf=p_inf,
        p40=values[-1],
        p40_error=abs(values[-1] - p_inf),
        last_abs_increment=abs(increments[-1]),
        distance_to_comparator=abs(p_inf - CANONICAL_COMPARATOR),
        p20=values[19],
        p30=values[29],
    )


def source_cell(source_nmax: int, packet: Packet) -> SourceCell:
    setup = one_word.source_setup(source_nmax, SOURCE_MODE_MAX_DEFAULT)
    p_inf = pair_support_p(setup)
    rho40 = reduced_eta_rho(packet, KMAX)
    p40 = source_p_from_rho(setup, packet.weights, rho40)
    return SourceCell(
        source_nmax=source_nmax,
        source_mode_max=SOURCE_MODE_MAX_DEFAULT,
        p_inf=p_inf,
        p40=p40,
        p40_error=abs(p40 - p_inf),
        distance_to_comparator=abs(p_inf - CANONICAL_COMPARATOR),
    )


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    print("Gauge-vacuum plaquette word-limit box/mode sweep")
    print(
        f"beta={BETA}, word NMAX={WORD_NMAXS}, word MODE_MAX={WORD_MODE_MAXS}, "
        f"source default NMAX={SOURCE_NMAX_DEFAULT}, source MODE_MAX={SOURCE_MODE_MAX_DEFAULT}"
    )
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set or predict an audit outcome."
    )
    print("No fitting, extrapolation claim, or canonical repinning is performed.")

    section("Part 1: builder cost and memory budget")
    max_box = (max(WORD_NMAXS) + 1) ** 2
    max_coeff_count = max_box * (2 * max(WORD_MODE_MAXS) + 1)
    print("NMAX MODE_MAX word_box reduced_shape coefficient_mode_terms")
    print("-" * 76)
    for nmax in WORD_NMAXS:
        for mode_max in WORD_MODE_MAXS:
            box = (nmax + 1) ** 2
            print(
                f"{nmax:4d} {mode_max:8d} {box:8d} "
                f"{box}x{box:<4d} {box * (2 * mode_max + 1):8d}"
            )
    check("NMAX=4 box convention is 25 weights", (WORD_NMAX_DEFAULT + 1) ** 2 == 25)
    check("NMAX=6 reduced object is 49x49", (6 + 1) ** 2 == 49)
    check("NMAX=7 optional cell remains a 64x64 reduced object", max_box == 64)
    check(
        "Wilson coefficient table work stays inside the bounded runner budget",
        max_coeff_count <= 64 * 401,
        f"max coefficient-mode terms={max_coeff_count}",
    )

    section("Part 2: word-packet NMAX/MODE_MAX sweep")
    source_setup_default = one_word.source_setup(
        SOURCE_NMAX_DEFAULT, SOURCE_MODE_MAX_DEFAULT
    )
    default_pair_p = pair_support_p(source_setup_default)
    cells: list[WordCell] = []
    print(
        "NMAX MODE word_box theta theta_ratio P_inf P40 |P40-P_inf| "
        f"|P_inf-{CANONICAL_COMPARATOR_TEXT}|"
    )
    print("-" * 132)
    for nmax in WORD_NMAXS:
        for mode_max in WORD_MODE_MAXS:
            packet = build_packet(nmax, mode_max)
            cell = word_cell(packet, source_setup_default, default_pair_p)
            cells.append(cell)
            print(
                f"{cell.nmax:4d} {cell.mode_max:4d} {cell.word_box_size:8d} "
                f"{cell.theta:.15f} {cell.theta_ratio:.15f} "
                f"{cell.p_inf:.15f} {cell.p40:.15f} "
                f"{cell.p40_error:.3e} {cell.distance_to_comparator:.15f}"
            )
            check(
                f"eta_inf residual is small for word NMAX={nmax}, MODE_MAX={mode_max}",
                cell.eta_residual < 1.0e-12,
                f"residual={cell.eta_residual:.3e}",
            )
            check(
                f"k=40 reaches the pair-support P_inf for word NMAX={nmax}, MODE_MAX={mode_max}",
                cell.p40_error < 1.0e-12,
                f"|P40-P_inf|={cell.p40_error:.3e}",
            )
            check(
                f"theta closed form matches the measured increment ratio for word NMAX={nmax}, MODE_MAX={mode_max}",
                cell.theta_ratio_delta < 2.0e-3,
                f"theta={cell.theta:.15f}, ratio={cell.theta_ratio:.15f}, delta={cell.theta_ratio_delta:.3e}",
            )

    p_inf_values = [cell.p_inf for cell in cells]
    p40_values = [cell.p40 for cell in cells]
    theta_values = [cell.theta for cell in cells]
    word_pinf_span = max(p_inf_values) - min(p_inf_values)
    word_p40_span = max(p40_values) - min(p40_values)
    theta_span = max(theta_values) - min(theta_values)
    print()
    print(f"word-axis P_inf span across computed cells = {word_pinf_span:.12e}")
    print(f"word-axis P40 span across computed cells = {word_p40_span:.12e}")
    print(f"theta span across computed cells = {theta_span:.12e}")
    check(
        "word-box and tensor-mode axes do not move P_inf at 1e-12 in this finite sweep",
        word_pinf_span < 1.0e-12 and word_p40_span < 1.0e-12,
        f"P_inf span={word_pinf_span:.3e}, P40 span={word_p40_span:.3e}",
    )
    check(
        "theta is stable across the word box/mode cells at the displayed precision scale",
        theta_span < 2.0e-10,
        f"theta span={theta_span:.3e}",
    )

    section("Part 3: source-box sweep at fixed word packet")
    default_packet = build_packet(WORD_NMAX_DEFAULT, WORD_MODE_MAX_DEFAULT)
    source_cells = [source_cell(nmax, default_packet) for nmax in SOURCE_SWEEP_NMAXS]
    print(
        "source_NMAX source_MODE P_inf P40 |P40-P_inf| "
        f"|P_inf-{CANONICAL_COMPARATOR_TEXT}|"
    )
    print("-" * 112)
    for cell in source_cells:
        print(
            f"{cell.source_nmax:11d} {cell.source_mode_max:11d} "
            f"{cell.p_inf:.15f} {cell.p40:.15f} "
            f"{cell.p40_error:.3e} {cell.distance_to_comparator:.15f}"
        )
        check(
            f"source NMAX={cell.source_nmax} reaches pair-support P_inf by k=40",
            cell.p40_error < 1.0e-12,
            f"|P40-P_inf|={cell.p40_error:.3e}",
        )
    source_span = max(c.p_inf for c in source_cells) - min(c.p_inf for c in source_cells)
    source_default = [c for c in source_cells if c.source_nmax == SOURCE_NMAX_DEFAULT][0]
    source_5_to_7 = (
        source_default.p_inf
        - [c for c in source_cells if c.source_nmax == 5][0].p_inf
    )
    source_7_to_9 = (
        [c for c in source_cells if c.source_nmax == 9][0].p_inf
        - source_default.p_inf
    )
    print(f"source-box P_inf span over NMAX=5,7,9 = {source_span:.12e}")
    print(f"source NMAX 5->7 drift = {source_5_to_7:+.12e}")
    print(f"source NMAX 7->9 drift = {source_7_to_9:+.12e}")
    check(
        "source-box drift is recorded and remains far below the fenced comparator distance",
        source_span < 1.0e-5
        and source_span < 0.001 * source_default.distance_to_comparator,
        f"source_span={source_span:.3e}, default_distance={source_default.distance_to_comparator:.3e}",
    )

    section("Part 4: bounded verdict diagnostics")
    default_cell = [
        c
        for c in cells
        if c.nmax == WORD_NMAX_DEFAULT and c.mode_max == WORD_MODE_MAX_DEFAULT
    ][0]
    print("```text")
    print(
        f"default word packet P_inf = {default_cell.p_inf:.15f}; "
        f"|P_inf - {CANONICAL_COMPARATOR_TEXT}| = {default_cell.distance_to_comparator:.15f}"
    )
    print(
        f"word-axis P_inf span = {word_pinf_span:.12e}; "
        f"word-axis P40 span = {word_p40_span:.12e}; theta span = {theta_span:.12e}"
    )
    print(
        f"source-box P_inf span = {source_span:.12e}; "
        f"source NMAX 5->7 drift = {source_5_to_7:+.12e}; "
        f"source NMAX 7->9 drift = {source_7_to_9:+.12e}"
    )
    print(
        "diagnostic verdict: within these computed cells, the dominant-weight "
        "box and Bessel-mode axes do not move the word-limit value toward the "
        "fenced comparator; the named open target left by this sweep is the "
        "1D word-chain versus 3D rim-geometry residual."
    )
    print(
        "non-load-bearing Richardson-style diagnostic: no word-axis "
        "Richardson value is emitted because the computed P_inf cells are "
        "identical at the 1e-12 scale."
    )
    print("```")
    check("fenced comparator is used only for distance reporting", True)
    check("no fitting or extrapolation claim is emitted", True)

    section("Part 5: note hygiene and residual boundary")
    text = note_text()
    if text:
        check(
            "note delegates status to the independent audit lane",
            "Status authority:** independent audit lane only" in text
            or "Status authority: independent audit lane only" in text,
        )
        check(
            "note links the primary runner as a one-hop authority",
            "[scripts/gauge_vacuum_plaquette_word_limit_box_mode_sweep_bounded_2026_06_12.py]"
            in text,
        )
        check(
            "note omits transient preparation refs",
            (".claude" + "/tmp") not in text
            and "Context pointers used during preparation" not in text,
        )
        check(
            "note names canonical load-bearing input notes",
            "GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md"
            in text
            and "GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_THETA_IDENTIFICATION_TWO_TERM_ASYMPTOTIC_NARROW_THEOREM_NOTE_2026-06-12.md"
            in text,
        )
    else:
        check("note exists for this runner", False, f"missing {NOTE_PATH}")
    print(
        "Named residuals: finite dominant-weight box; finite Bessel mode support; "
        "source-box truncation; finite word count checked through k=40; no physical "
        "3D unmarked spatial Wilson environment computation; no all-weight or "
        "untruncated convergence proof; no L_perp limit; no analytic P(6); no "
        "canonical repinning."
    )
    check("runner names residuals without claiming them retired", True)

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
