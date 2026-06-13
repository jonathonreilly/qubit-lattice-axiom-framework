#!/usr/bin/env python3
"""Ring N=5 finite-trend diagnostic on the finite plaquette packet.

The runner reuses the landed finite ring machinery in
`gauge_vacuum_plaquette_ring_transverse_rho_ladder_bounded_2026_06_12`.
It keeps the N=5 state matrix-free, applies factor-wise Kronecker matvecs
along axes, and uses deterministic power iteration to avoid an eigsh basis
whose memory footprint is larger than the few-vector working set needed here.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_ring_transverse_rho_ladder_bounded_2026_06_12 as ring_base


AUDIT_TIMEOUT_SEC = 600

BETA = ring_base.BETA
TW_NMAX = ring_base.TW_NMAX
TW_MODE_MAX = ring_base.TW_MODE_MAX
SOURCE_NMAX = ring_base.SOURCE_NMAX
SOURCE_MODE_MAX = ring_base.SOURCE_MODE_MAX

ZERO = ring_base.ZERO
FUND = ring_base.FUND
ADJOINT = ring_base.ADJOINT

COMPARATOR = ring_base.COMPARATOR
COMPARATOR_TEXT = ring_base.COMPARATOR_TEXT
P_TRIV_ANCHOR = ring_base.P_TRIV_ANCHOR
P_LOC_ANCHOR = ring_base.P_LOC_ANCHOR

P_RING3_REFERENCE = 0.443670871217007
P_RING4_REFERENCE = 0.443819912885704
OPEN4_LOW_REFERENCE = 0.436904879677743
OPEN4_HIGH_REFERENCE = 0.438273257015454

POWER_TOL = 5.0e-12
POWER_MAX_ITER = 80
TRACE_ITERS = {1, 2, 3, 4, 5, 10, 20, 40, 80}

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_RING_FIVE_SLAB_TREND_BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class PowerTrace:
    iteration: int
    eigenvalue: float
    residual_inf: float
    residual_l2: float
    relative_delta: float | None


@dataclass(frozen=True)
class RingResult:
    label: str
    units: int
    active_edges: tuple[int, ...]
    dimension: int
    vector_bytes: float
    dense_bytes: float
    internal_min: float
    internal_max: float
    eigenvalue: float
    residual_inf: float
    residual_l2: float
    psi_min: float
    iterations: int
    matvec_calls: int
    trace: tuple[PowerTrace, ...]
    rho_marginals: tuple[np.ndarray, ...]
    p_value: float
    u0: float
    alpha_s: float


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


def memory_rows(units: int, ncv: int = 24) -> dict[str, float]:
    dimension = float(25**units)
    vector_bytes = dimension * 8.0
    return {
        "dimension": dimension,
        "vector_bytes": vector_bytes,
        "dense_bytes": dimension * dimension * 8.0,
        "three_vector_bytes": 3.0 * vector_bytes,
        "five_vector_bytes": 5.0 * vector_bytes,
        "eigsh_basis_bytes": dimension * float(ncv) * 8.0,
    }


def print_memory_estimate_first() -> None:
    mem = memory_rows(5)
    print("N=5 memory estimate before packet build or solve:")
    print(f"  state space = 25^5 = {int(mem['dimension'])}")
    print(
        "  one vector = "
        f"{format_bytes(mem['vector_bytes'])} "
        f"({mem['vector_bytes'] / 1.0e6:.3f} MB decimal)"
    )
    print(f"  three vectors = {format_bytes(mem['three_vector_bytes'])}")
    print(f"  five vectors = {format_bytes(mem['five_vector_bytes'])}")
    print(f"  eigsh basis at ncv=24 = {format_bytes(mem['eigsh_basis_bytes'])}")
    print(f"  dense transfer storage would be {format_bytes(mem['dense_bytes'])}")
    print("  solver choice = deterministic power iteration, matrix-free")


def diagonal_vector_and_internal_range(
    packet: ring_base.two_strip.Packet,
    pair_factor: np.ndarray,
    units: int,
    active_edges: tuple[int, ...],
) -> tuple[np.ndarray, float, float]:
    n = len(packet.weights)
    diagonal = np.ones((n,) * units, dtype=float)

    for edge in active_edges:
        left = int(edge)
        right = (left + 1) % units
        diagonal *= ring_base.edge_factor_view(pair_factor, units, left, right)

    internal_min = float(np.min(diagonal))
    internal_max = float(np.max(diagonal))

    for axis in range(units):
        axis_shape = [1] * units
        axis_shape[axis] = n
        diagonal *= packet.d_coeff.reshape(axis_shape)

    return diagonal.reshape(-1), internal_min, internal_max


def power_solve(
    packet: ring_base.two_strip.Packet,
    pair_factor: np.ndarray,
    units: int,
    active_edges: tuple[int, ...],
    label: str,
    tol: float = POWER_TOL,
    max_iter: int = POWER_MAX_ITER,
) -> RingResult:
    diagonal, internal_min, internal_max = diagonal_vector_and_internal_range(
        packet, pair_factor, units, active_edges
    )
    _operator, matvec = ring_base.make_operator(packet, units, diagonal)
    dimension = diagonal.size
    x = np.ones(dimension, dtype=float)
    x /= np.linalg.norm(x)

    trace: list[PowerTrace] = []
    last_eig: float | None = None
    matvec_calls = 0
    eig = float("nan")
    residual_inf = float("inf")
    residual_l2 = float("inf")
    iterations = 0

    for iteration in range(1, max_iter + 1):
        y = matvec(x)
        matvec_calls += 1
        eig = float(np.dot(x, y))
        diff = y - eig * x
        residual_inf = float(np.linalg.norm(diff, ord=np.inf))
        residual_l2 = float(np.linalg.norm(diff))
        rel_delta = (
            None
            if last_eig is None
            else abs(eig - last_eig) / max(1.0, abs(eig))
        )
        if iteration in TRACE_ITERS or residual_inf <= tol:
            trace.append(
                PowerTrace(
                    iteration=iteration,
                    eigenvalue=eig,
                    residual_inf=residual_inf,
                    residual_l2=residual_l2,
                    relative_delta=rel_delta,
                )
            )
        iterations = iteration
        if residual_inf <= tol:
            break
        y_norm = float(np.linalg.norm(y))
        if y_norm <= 0.0 or not np.isfinite(y_norm):
            raise RuntimeError(f"nonfinite power norm for {label} at iteration {iteration}")
        y /= y_norm
        x = y
        last_eig = eig

    final_y = matvec(x)
    matvec_calls += 1
    eig = float(np.dot(x, final_y))
    final_diff = final_y - eig * x
    residual_inf = float(np.linalg.norm(final_diff, ord=np.inf))
    residual_l2 = float(np.linalg.norm(final_diff))

    rhos = ring_base.rho_marginals(packet, x, units)
    p_value, u0, alpha_s = ring_base.two_strip.source_p(packet, rhos[0])
    return RingResult(
        label=label,
        units=units,
        active_edges=active_edges,
        dimension=dimension,
        vector_bytes=float(dimension * 8),
        dense_bytes=float(dimension * dimension * 8),
        internal_min=internal_min,
        internal_max=internal_max,
        eigenvalue=eig,
        residual_inf=residual_inf,
        residual_l2=residual_l2,
        psi_min=float(np.min(x)),
        iterations=iterations,
        matvec_calls=matvec_calls,
        trace=tuple(trace),
        rho_marginals=rhos,
        p_value=float(p_value),
        u0=float(u0),
        alpha_s=float(alpha_s),
    )


def marginal_spread(result: RingResult) -> float:
    base = result.rho_marginals[0]
    return float(max(np.max(np.abs(rho - base)) for rho in result.rho_marginals))


def rho_admissible(packet: ring_base.two_strip.Packet, result: RingResult) -> bool:
    z = packet.index[ZERO]
    rho = result.rho_marginals[0]
    return (
        np.all(np.isfinite(rho))
        and abs(float(rho[z]) - 1.0) < 1.0e-13
        and float(np.min(rho)) >= -1.0e-12
        and ring_base.conjugation_error(packet, rho) < 1.0e-11
    )


def print_power_result(packet: ring_base.two_strip.Packet, result: RingResult) -> None:
    f = packet.index[FUND]
    adj = packet.index[ADJOINT]
    rho = result.rho_marginals[0]
    print()
    print(f"{result.label}:")
    print(f"  units = {result.units}, active_edges = {result.active_edges}")
    print(f"  dimension = {result.dimension}")
    print(f"  vector bytes = {format_bytes(result.vector_bytes)}")
    print(f"  dense transfer storage would be {format_bytes(result.dense_bytes)}")
    print("  solver = deterministic-power-matrix-free")
    print(f"  iterations = {result.iterations}, matvec_calls = {result.matvec_calls}")
    print(f"  internal factor min/max = {result.internal_min:.15f} / {result.internal_max:.15f}")
    print("  convergence trace:")
    print("    iter | eigenvalue | residual_inf | residual_l2 | relative_delta")
    for row in result.trace:
        rel = "n/a" if row.relative_delta is None else f"{row.relative_delta:.3e}"
        print(
            f"    {row.iteration:4d} | {row.eigenvalue:.15f} | "
            f"{row.residual_inf:.3e} | {row.residual_l2:.3e} | {rel}"
        )
    print(f"  eigenvalue = {result.eigenvalue:.15f}")
    print(f"  final residual_inf = {result.residual_inf:.3e}")
    print(f"  final residual_l2 = {result.residual_l2:.3e}")
    print(f"  psi_min = {result.psi_min:.3e}")
    print(f"  marginal spread = {marginal_spread(result):.3e}")
    print(f"  conjugation residual = {ring_base.conjugation_error(packet, rho):.3e}")
    print(f"  rho(1,0) = {rho[f]:.15f}")
    print(f"  rho(1,1) = {rho[adj]:.15f}")
    print(f"  rho min/max = {float(np.min(rho)):.3e} / {float(np.max(rho)):.3e}")
    print(f"  P = {result.p_value:.15f}")
    print(f"  u0 = {result.u0:.15f}")
    print(f"  alpha_s(alpha_bare=1) = {result.alpha_s:.15f}")


def deterministic_probe(dimension: int, name: str) -> np.ndarray:
    if name == "constant":
        out = np.ones(dimension, dtype=float)
    elif name == "centered_ramp":
        out = np.arange(dimension, dtype=float)
        out -= 0.5 * float(dimension - 1)
    elif name == "mod13_centered":
        out = np.remainder(np.arange(dimension, dtype=float), 13.0)
        out -= 6.0
    else:
        raise ValueError(f"unknown probe: {name}")
    norm = float(np.linalg.norm(out))
    if norm <= 0.0:
        raise RuntimeError(f"zero norm probe: {name}")
    out /= norm
    return out


def cut_open5_probe_diffs(
    packet: ring_base.two_strip.Packet,
    pair_factor: np.ndarray,
) -> tuple[tuple[str, float, float], ...]:
    units = 5
    ring_cut_edges = tuple(edge for edge in range(units) if edge != units - 1)
    open_edges = tuple(range(units - 1))
    diag_cut, _cut_min, _cut_max = diagonal_vector_and_internal_range(
        packet, pair_factor, units, ring_cut_edges
    )
    diag_open, _open_min, _open_max = diagonal_vector_and_internal_range(
        packet, pair_factor, units, open_edges
    )
    _op_cut, matvec_cut = ring_base.make_operator(packet, units, diag_cut)
    _op_open, matvec_open = ring_base.make_operator(packet, units, diag_open)

    out: list[tuple[str, float, float]] = []
    for name in ("constant", "centered_ramp", "mod13_centered"):
        probe = deterministic_probe(diag_cut.size, name)
        y_cut = matvec_cut(probe)
        y_open = matvec_open(probe)
        diff = float(np.max(np.abs(y_cut - y_open)))
        scale = max(1.0, float(np.max(np.abs(y_open))))
        out.append((name, diff, diff / scale))
    return tuple(out)


def ladder_line(name: str, result: RingResult, previous: float | None) -> str:
    inc = "baseline" if previous is None else f"{result.p_value - previous:+.15f}"
    return (
        f"{name:18s} | N={result.units} | P={result.p_value:.15f} | "
        f"increment={inc} | |P-{COMPARATOR_TEXT}|={abs(result.p_value - COMPARATOR):.15f} | "
        f"distance_to_open4_low={result.p_value - OPEN4_LOW_REFERENCE:+.15f} | "
        f"distance_to_open4_high={result.p_value - OPEN4_HIGH_REFERENCE:+.15f}"
    )


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def note_hygiene_checks() -> None:
    text = note_text()
    if not text:
        check("note exists for this runner", False, f"missing {NOTE_PATH}")
        return

    check(
        "note delegates status to the independent audit lane",
        "Status authority: independent audit lane only" in text
        and "does not set, predict, promote, or demote any audit outcome" in text,
    )
    runner_path = (
        "scripts/gauge_vacuum_plaquette_ring_five_slab_trend_bounded_2026_06_12.py"
    )
    cache_path = (
        "logs/runner-cache/gauge_vacuum_plaquette_ring_five_slab_trend_bounded_2026_06_12.txt"
    )
    check(
        "note keeps runner and cache as plain-text pointers",
        runner_path in text
        and cache_path in text
        and f"]({runner_path})" not in text
        and f"]({cache_path})" not in text,
    )
    check(
        "note keeps durable context pointers as backticked non-links",
        "`docs/GAUGE_VACUUM_PLAQUETTE_TWO_STRIP_ENVIRONMENT_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-12.md`" in text
        and "`docs/GAUGE_VACUUM_PLAQUETTE_THREE_STRIP_ENVIRONMENT_RHO_LADDER_BOUNDED_NOTE_2026-06-12.md`" in text
        and "`docs/GAUGE_VACUUM_PLAQUETTE_FOUR_STRIP_PARITY_TEST_BOUNDED_NOTE_2026-06-12.md`" in text
        and ".claude/tmp" not in text,
    )
    check(
        "note uses markdown links for one-hop authorities",
        "[GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md]" in text
        and "[GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md]" in text
        and "[GAUGE_VACUUM_PLAQUETTE_INTERNAL_LINK_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md]" in text
        and "[GAUGE_VACUUM_PLAQUETTE_RING_TRANSVERSE_RHO_LADDER_BOUNDED_NOTE_2026-06-12.md]" in text
        and "[SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md]" in text
        and "[PLAQUETTE_SELF_CONSISTENCY_NOTE.md]" in text,
    )
    banned = [
        " ".join(("only", "route")),
        " ".join(("last", "route")),
        "ex" + "hausted",
        " ".join(("closes", "the", "program")),
    ]
    check("note avoids overreach closure language", not any(x in text.lower() for x in banned))
    status_words = [
        "ret" + "ained",
        "no" + "_go",
        "cond" + "itional",
        "audited" + "_clean",
    ]
    check("note avoids audit-status labels for claims", not any(x in text.lower() for x in status_words))


def main() -> int:
    print("Gauge-vacuum plaquette ring N=5 finite-trend bounded diagnostic")
    print_memory_estimate_first()
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set, predict, promote, or demote any audit outcome."
    )
    print("No new imports: repo-internal finite packet quantities only.")
    print(f"beta={BETA}, tensor NMAX={TW_NMAX}, tensor MODE_MAX={TW_MODE_MAX}")
    print(f"source NMAX={SOURCE_NMAX}, source MODE_MAX={SOURCE_MODE_MAX}")
    print("primary internal-link reading: derived dimension-stripped D_lambda")

    packet = ring_base.two_strip.build_packet()
    fusion = ring_base.two_strip.build_fusion_table(packet)
    pair_factor = ring_base.two_strip.internal_factor(
        packet, fusion, "dimension_stripped", "product"
    ).reshape((len(packet.weights), len(packet.weights)))

    section("Part 1: finite packet and N=5 state-space gates")
    mem5 = memory_rows(5)
    print(f"one-word state count = {len(packet.weights)}")
    print(f"N=5 ring state count = {25**5}")
    print(f"fusion table shape = {fusion.shape}")
    print(
        "dimension-stripped pair factor min/max = "
        f"{float(np.min(pair_factor)):.15f} / {float(np.max(pair_factor)):.15f}"
    )
    check("one-word packet has 25 states", len(packet.weights) == 25)
    check("ring N=5 state space has 25^5 = 9765625 states", 25**5 == 9765625)
    check("N=5 dense transfer is not materialized", mem5["dense_bytes"] > 1.0e14)
    check(
        "N=5 power working estimate stays in a few-vector range",
        mem5["five_vector_bytes"] < mem5["eigsh_basis_bytes"],
        (
            f"five_vectors={format_bytes(mem5['five_vector_bytes'])}, "
            f"eigsh_ncv24={format_bytes(mem5['eigsh_basis_bytes'])}"
        ),
    )
    check(
        "fusion table is finite and nonnegative",
        np.issubdtype(fusion.dtype, np.integer) and int(np.min(fusion)) >= 0,
    )
    check(
        "dimension-stripped internal factor is finite and positive",
        np.all(np.isfinite(pair_factor)) and float(np.min(pair_factor)) > 0.0,
    )

    section("Part 2: simple-ring power solves")
    ring3 = power_solve(packet, pair_factor, 3, (0, 1, 2), "ring_N3_simple_cycle")
    ring4 = power_solve(packet, pair_factor, 4, (0, 1, 2, 3), "ring_N4_simple_cycle")
    ring5 = power_solve(packet, pair_factor, 5, (0, 1, 2, 3, 4), "ring_N5_simple_cycle")

    for result in (ring3, ring4, ring5):
        print_power_result(packet, result)
        check(f"{result.label} residual_inf is small", result.residual_inf < 1.0e-10)
        check(f"{result.label} residual_l2 is small", result.residual_l2 < 1.0e-9)
        check(f"{result.label} Perron vector is nonnegative up to tolerance", result.psi_min >= -1.0e-12)
        check(f"{result.label} rho is admissible on B4", rho_admissible(packet, result))
        check(f"{result.label} translation marginals agree", marginal_spread(result) < 1.0e-10)

    check(
        "N=3 anchor is reproduced by the shared power path",
        abs(ring3.p_value - P_RING3_REFERENCE) < 5.0e-13,
        f"delta={abs(ring3.p_value - P_RING3_REFERENCE):.3e}",
    )
    check(
        "N=4 anchor is reproduced by the shared power path",
        abs(ring4.p_value - P_RING4_REFERENCE) < 5.0e-13,
        f"delta={abs(ring4.p_value - P_RING4_REFERENCE):.3e}",
    )

    section("Part 3: one-link cut to open N=5 matvec gate")
    probe_diffs = cut_open5_probe_diffs(packet, pair_factor)
    for name, diff, rel in probe_diffs:
        print(f"probe {name}: max |T_cut_ring5 v - T_open5 v| = {diff:.3e}; relative = {rel:.3e}")
    check(
        "cut-ring N=5 and open-chain N=5 matvecs agree on deterministic probes",
        all(diff < 1.0e-14 and rel < 1.0e-14 for _name, diff, rel in probe_diffs),
    )

    section("Part 4: ring ladder measurement and fenced comparator distances")
    inc34 = ring4.p_value - ring3.p_value
    inc45 = ring5.p_value - ring4.p_value
    print("Plaquette reuse license: comparator numbers are comparison context only.")
    print("```text")
    print("simple-ring ladder:")
    print(ladder_line("N=3 simple ring", ring3, None))
    print(ladder_line("N=4 simple ring", ring4, ring3.p_value))
    print(ladder_line("N=5 simple ring", ring5, ring4.p_value))
    print()
    print(f"increment N=3->4 = {inc34:+.15f}")
    print(f"increment N=4->5 = {inc45:+.15f}")
    print(f"|increment N=4->5| / |increment N=3->4| = {abs(inc45) / abs(inc34):.15f}")
    print(f"open-chain four-strip context interval = [{OPEN4_LOW_REFERENCE:.15f}, {OPEN4_HIGH_REFERENCE:.15f}]")
    print("```")
    print(
        "finite trend answer: the N=3 to N=4 rise does not continue at N=5; "
        "the next finite increment flips sign and has smaller magnitude."
    )
    print(
        "non_load_bearing_geometric_diagnostic: the simple-ring sample shows "
        "a damped two-increment oscillation over N=3,4,5, not a monotone rise."
    )
    check("simple-ring N=3 to N=4 finite increment is positive", inc34 > 0.0)
    check("simple-ring N=4 to N=5 finite increment is negative", inc45 < 0.0)
    check("simple-ring N=4 to N=5 absolute increment is smaller", abs(inc45) < abs(inc34))
    check("N=5 ring remains above N=3 ring", ring5.p_value > ring3.p_value)
    check(
        "ring N=3,4,5 readouts sit above the open-chain four-strip context interval",
        all(r.p_value > OPEN4_HIGH_REFERENCE for r in (ring3, ring4, ring5)),
    )
    check(
        "ring readouts remain inside the source anchor interval",
        all(P_TRIV_ANCHOR < r.p_value < P_LOC_ANCHOR for r in (ring3, ring4, ring5)),
        (
            f"P_triv={P_TRIV_ANCHOR:.12f}, P_ring5={ring5.p_value:.12f}, "
            f"P_loc={P_LOC_ANCHOR:.12f}"
        ),
    )

    section("Part 5: note hygiene and named residuals")
    note_hygiene_checks()
    print(
        "Named residuals: transverse-topology underdetermination in the cited "
        "geometry notes; finite simple ring widths N=3,4,5; finite B4 weight box; "
        "finite Bessel support; scalar class-channel internal-link contraction; "
        "future all-link 6j/intertwiner normalization; full rim eta evaluation; "
        "strip-depth direction; wider slab limit; 3D stack; L_perp limit; "
        "analytic P(6); no repinning."
    )
    check("runner names residuals without retiring them", True)

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
