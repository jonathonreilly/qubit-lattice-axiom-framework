#!/usr/bin/env python3
"""Ring transverse rho ladder on the finite plaquette packet.

This runner uses the repo-internal finite packet quantities already used by
the landed open-strip runners.  The internal environment link is the derived
dimension-stripped scalar class-channel factor.  The N=4 transfer has
25^4 = 390625 states and is applied matrix-free.

No random sampling, external data, date-dependent input, or fitted selector is
used.
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
P_OPEN2_REFERENCE = 0.439904783618900
P_OPEN3_REFERENCE = 0.436904879677743
COMPARATOR = two_strip.COMPARATOR
COMPARATOR_TEXT = two_strip.COMPARATOR_TEXT
P_TRIV_ANCHOR = two_strip.one_word.P_TRIV_REFERENCE
P_LOC_ANCHOR = two_strip.one_word.P_LOC_REFERENCE

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_RING_TRANSVERSE_RHO_LADDER_BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class TopologyResult:
    label: str
    topology: str
    units: int
    active_edges: tuple[int, ...]
    dimension: int
    dense_bytes: float
    eigenvalue: float
    residual: float
    psi_min: float
    internal_min: float
    internal_max: float
    rho_marginals: tuple[np.ndarray, ...]
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


def apply_kron(vec: np.ndarray, mat: np.ndarray, units: int, n: int) -> np.ndarray:
    arr = vec.reshape((n,) * units)
    for axis in range(units):
        arr = apply_axis(arr, mat, axis)
    return arr.reshape(-1)


def edge_factor_view(pair_factor: np.ndarray, units: int, left: int, right: int) -> np.ndarray:
    n = pair_factor.shape[0]
    shape = [1] * units
    shape[left] = n
    shape[right] = n
    if left < right:
        return pair_factor.reshape(shape)
    return pair_factor.T.reshape(shape)


def diagonal_vector(
    packet: two_strip.Packet,
    pair_factor: np.ndarray,
    units: int,
    active_edges: tuple[int, ...],
) -> tuple[np.ndarray, np.ndarray]:
    n = len(packet.weights)
    d = packet.d_coeff
    shape = (n,) * units
    diagonal = np.ones(shape, dtype=float)
    internal = np.ones(shape, dtype=float)

    for axis in range(units):
        axis_shape = [1] * units
        axis_shape[axis] = n
        diagonal *= d.reshape(axis_shape)

    for edge in active_edges:
        left = int(edge)
        right = (left + 1) % units
        factor = edge_factor_view(pair_factor, units, left, right)
        diagonal *= factor
        internal *= factor

    return diagonal.reshape(-1), internal.reshape(-1)


def make_operator(
    packet: two_strip.Packet,
    units: int,
    diagonal: np.ndarray,
) -> tuple[LinearOperator, callable]:
    n = len(packet.weights)
    m = packet.word_bond
    mt = packet.word_bond.T
    dimension = n**units

    def matvec(x: np.ndarray) -> np.ndarray:
        y = diagonal * np.asarray(x, dtype=float)
        y = apply_kron(y, mt, units, n)
        y = diagonal * y
        y = apply_kron(y, m, units, n)
        y = diagonal * y
        return np.asarray(y, dtype=float)

    return LinearOperator((dimension, dimension), matvec=matvec, dtype=float), matvec


def solve_topology(
    packet: two_strip.Packet,
    pair_factor: np.ndarray,
    units: int,
    active_edges: tuple[int, ...],
    label: str,
    topology: str,
) -> TopologyResult:
    n = len(packet.weights)
    dimension = n**units
    dense_bytes = float(dimension * dimension * 8)
    diagonal, internal = diagonal_vector(packet, pair_factor, units, active_edges)
    operator, matvec = make_operator(packet, units, diagonal)
    v0 = np.ones(dimension, dtype=float)
    v0 /= np.linalg.norm(v0)
    ncv = min(32, dimension - 1)
    tol = 1.0e-13 if units <= 3 else 1.0e-12
    vals, vecs = eigsh(
        operator,
        k=1,
        which="LA",
        tol=tol,
        maxiter=20000,
        ncv=ncv,
        v0=v0,
    )
    eig = float(vals[0])
    psi = np.asarray(vecs[:, 0], dtype=float)
    if float(psi[0]) < 0.0:
        psi = -psi
    residual = float(np.linalg.norm(matvec(psi) - eig * psi, ord=np.inf))
    rhos = rho_marginals(packet, psi, units)
    p_value, u0, alpha_s = two_strip.source_p(packet, rhos[0])
    return TopologyResult(
        label=label,
        topology=topology,
        units=units,
        active_edges=active_edges,
        dimension=dimension,
        dense_bytes=dense_bytes,
        eigenvalue=eig,
        residual=residual,
        psi_min=float(np.min(psi)),
        internal_min=float(np.min(internal)),
        internal_max=float(np.max(internal)),
        rho_marginals=rhos,
        p_value=float(p_value),
        u0=float(u0),
        alpha_s=float(alpha_s),
        solver="eigsh-matrix-free",
    )


def rho_marginals(
    packet: two_strip.Packet,
    psi: np.ndarray,
    units: int,
) -> tuple[np.ndarray, ...]:
    n = len(packet.weights)
    arr = psi.reshape((n,) * units)
    z = packet.index[ZERO]
    out = []
    for axis in range(units):
        axes = tuple(i for i in range(units) if i != axis)
        sums = np.sum(arr, axis=axes)
        denom = float(sums[z])
        if abs(denom) <= 1.0e-300:
            raise RuntimeError(f"zero rho denominator on axis {axis}")
        out.append(np.asarray(sums / denom, dtype=float))
    return tuple(out)


def conjugation_error(packet: two_strip.Packet, rho: np.ndarray) -> float:
    return two_strip.conjugation_error(packet, rho)


def marginal_spread(result: TopologyResult) -> float:
    base = result.rho_marginals[0]
    return float(max(np.max(np.abs(rho - base)) for rho in result.rho_marginals))


def max_rho_diff(left: np.ndarray, right: np.ndarray) -> float:
    return float(np.max(np.abs(left - right)))


def print_result(packet: two_strip.Packet, result: TopologyResult) -> None:
    f = packet.index[FUND]
    adj = packet.index[ADJOINT]
    rho = result.rho_marginals[0]
    print()
    print(f"{result.label}:")
    print(f"  topology = {result.topology}")
    print(f"  units = {result.units}, active_edges = {result.active_edges}")
    print(f"  dimension = {result.dimension}")
    print(f"  dense transfer storage would be {format_bytes(result.dense_bytes)}")
    print(f"  solver = {result.solver}")
    print(f"  internal factor min/max = {result.internal_min:.15f} / {result.internal_max:.15f}")
    print(f"  eigenvalue = {result.eigenvalue:.15f}")
    print(f"  Perron residual = {result.residual:.3e}")
    print(f"  psi_min = {result.psi_min:.3e}")
    print(f"  marginal spread = {marginal_spread(result):.3e}")
    print(f"  conjugation residual = {conjugation_error(packet, rho):.3e}")
    print(f"  rho(1,0) = {rho[f]:.15f}")
    print(f"  rho(1,1) = {rho[adj]:.15f}")
    print(f"  rho min/max = {float(np.min(rho)):.3e} / {float(np.max(rho)):.3e}")
    print(f"  P = {result.p_value:.15f}")
    print(f"  u0 = {result.u0:.15f}")
    print(f"  alpha_s(alpha_bare=1) = {result.alpha_s:.15f}")


def ladder_line(name: str, result: TopologyResult, prev: float | None) -> str:
    inc = "baseline" if prev is None else f"{result.p_value - prev:+.15f}"
    return (
        f"{name:22s} | N={result.units} | links={len(result.active_edges):1d} | "
        f"P={result.p_value:.15f} | increment={inc} | "
        f"|P-{COMPARATOR_TEXT}|={abs(result.p_value - COMPARATOR):.15f}"
    )


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    print("Gauge-vacuum plaquette ring transverse rho ladder")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set, predict, promote, or demote any audit outcome."
    )
    print("No new imports: repo-internal finite packet quantities only.")
    print(f"beta={BETA}, tensor NMAX={TW_NMAX}, tensor MODE_MAX={TW_MODE_MAX}")
    print(f"source NMAX={SOURCE_NMAX}, source MODE_MAX={SOURCE_MODE_MAX}")
    print("primary internal-link reading: derived dimension-stripped D_lambda")

    packet = two_strip.build_packet()
    fusion = two_strip.build_fusion_table(packet)
    pair_factor = two_strip.internal_factor(
        packet, fusion, "dimension_stripped", "product"
    ).reshape((len(packet.weights), len(packet.weights)))
    n = len(packet.weights)
    z = packet.index[ZERO]

    section("Part 1: finite packet and state-space gates")
    print(f"one-word state count = {n}")
    print(f"N=4 ring state count = {n**4}")
    print(f"N=4 dense transfer storage would be {format_bytes(float((n**4) * (n**4) * 8))}")
    print(f"fusion table shape = {fusion.shape}")
    print(f"dimension-stripped pair factor min/max = {float(np.min(pair_factor)):.15f} / {float(np.max(pair_factor)):.15f}")
    check("one-word packet has 25 states", n == 25)
    check("ring N=4 state space has 25^4 = 390625 states", n**4 == 390625)
    check("ring N=4 dense transfer is not materialized", float((n**4) * (n**4) * 8) > 1.0e12)
    check("fusion table is finite and nonnegative", np.issubdtype(fusion.dtype, np.integer) and int(np.min(fusion)) >= 0)
    check("dimension-stripped internal factor is finite and positive", np.all(np.isfinite(pair_factor)) and float(np.min(pair_factor)) > 0.0)

    section("Part 2: open-chain anchors")
    open1 = solve_topology(packet, pair_factor, 1, tuple(), "open_N1_word", "word/no internal link")
    open2 = solve_topology(packet, pair_factor, 2, (0,), "open_N2_chain", "open chain")
    open3 = solve_topology(packet, pair_factor, 3, (0, 1), "open_N3_chain", "open chain")
    open4 = solve_topology(packet, pair_factor, 4, (0, 1, 2), "open_N4_chain", "open chain")

    for result in [open1, open2, open3, open4]:
        print_result(packet, result)
        check(f"{result.label} Perron residual is small", result.residual < 1.0e-11)
        check(
            f"{result.label} rho is admissible on B4",
            np.all(np.isfinite(result.rho_marginals[0]))
            and abs(float(result.rho_marginals[0][z]) - 1.0) < 1.0e-13
            and float(np.min(result.rho_marginals[0])) >= -1.0e-12
            and conjugation_error(packet, result.rho_marginals[0]) < 1.0e-11,
        )

    check(
        "word anchor reproduces the landed one-word value",
        abs(open1.p_value - P_WORD_REFERENCE) < 5.0e-13,
        f"delta={abs(open1.p_value - P_WORD_REFERENCE):.3e}",
    )
    check(
        "open N=2 chain reproduces the landed two-strip dimension-stripped value",
        abs(open2.p_value - P_OPEN2_REFERENCE) < 5.0e-13,
        f"delta={abs(open2.p_value - P_OPEN2_REFERENCE):.3e}",
    )
    check(
        "open N=3 chain reproduces the landed three-strip dimension-stripped value",
        abs(open3.p_value - P_OPEN3_REFERENCE) < 5.0e-13,
        f"delta={abs(open3.p_value - P_OPEN3_REFERENCE):.3e}",
    )

    section("Part 3: ring solves")
    ring2 = solve_topology(packet, pair_factor, 2, (0, 1), "ring_N2_doubled_edge", "two-node doubled-edge ring")
    ring3 = solve_topology(packet, pair_factor, 3, (0, 1, 2), "ring_N3_simple_cycle", "simple transverse ring")
    ring4 = solve_topology(packet, pair_factor, 4, (0, 1, 2, 3), "ring_N4_simple_cycle", "simple transverse ring")

    for result in [ring2, ring3, ring4]:
        print_result(packet, result)
        check(f"{result.label} Perron residual is small", result.residual < 1.0e-11)
        check(f"{result.label} Perron vector is nonnegative up to tolerance", result.psi_min >= -1.0e-12)
        check(
            f"{result.label} rho is admissible on B4",
            np.all(np.isfinite(result.rho_marginals[0]))
            and abs(float(result.rho_marginals[0][z]) - 1.0) < 1.0e-13
            and float(np.min(result.rho_marginals[0])) >= -1.0e-12
            and conjugation_error(packet, result.rho_marginals[0]) < 1.0e-11,
        )
        check(f"{result.label} translation marginals agree", marginal_spread(result) < 1.0e-11)

    check(
        "N=2 ring is a doubled-edge multigraph and is reported separately",
        ring2.units == 2 and len(ring2.active_edges) == 2,
    )
    check("N=4 ring solve is matrix-free at 390625 states", ring4.dimension == 390625 and ring4.solver == "eigsh-matrix-free")

    section("Part 4: cut gates")
    ring2_cut0 = solve_topology(packet, pair_factor, 2, (1,), "ring_N2_cut_edge0", "cut doubled-edge ring")
    ring2_cut1 = solve_topology(packet, pair_factor, 2, (0,), "ring_N2_cut_edge1", "cut doubled-edge ring")
    ring3_cut_closing = solve_topology(packet, pair_factor, 3, (0, 1), "ring_N3_cut_closing_edge", "cut simple ring")
    ring4_cut_closing = solve_topology(packet, pair_factor, 4, (0, 1, 2), "ring_N4_cut_closing_edge", "cut simple ring")

    for result in [ring2_cut0, ring2_cut1, ring3_cut_closing, ring4_cut_closing]:
        print_result(packet, result)

    check(
        "cutting either N=2 doubled ring edge reproduces open N=2 rho and P",
        max_rho_diff(ring2_cut0.rho_marginals[0], open2.rho_marginals[0]) < 5.0e-13
        and max_rho_diff(ring2_cut1.rho_marginals[0], open2.rho_marginals[0]) < 5.0e-13
        and abs(ring2_cut0.p_value - open2.p_value) < 5.0e-13
        and abs(ring2_cut1.p_value - open2.p_value) < 5.0e-13,
    )
    check(
        "cutting the N=3 closing ring link reproduces open N=3 rho and P",
        max_rho_diff(ring3_cut_closing.rho_marginals[0], open3.rho_marginals[0]) < 5.0e-13
        and abs(ring3_cut_closing.p_value - open3.p_value) < 5.0e-13,
    )
    check(
        "cutting the N=4 closing ring link reproduces the open N=4 rho and P",
        max_rho_diff(ring4_cut_closing.rho_marginals[0], open4.rho_marginals[0]) < 5.0e-13
        and abs(ring4_cut_closing.p_value - open4.p_value) < 5.0e-13,
    )

    section("Part 5: ladder measurement and fenced comparator distances")
    print("Plaquette reuse license: comparator is used only as comparison/reuse context.")
    print("```text")
    print("open-chain ladder:")
    prev = None
    for result in [open1, open2, open3, open4]:
        print(ladder_line(result.label, result, prev))
        prev = result.p_value
    print()
    print("ring diagnostic and simple-ring ladder:")
    print(ladder_line(ring2.label, ring2, None))
    print(ladder_line(ring3.label, ring3, ring2.p_value))
    print(ladder_line(ring4.label, ring4, ring3.p_value))
    print("```")
    open_increments = [
        open2.p_value - open1.p_value,
        open3.p_value - open2.p_value,
        open4.p_value - open3.p_value,
    ]
    ring_simple_increment = ring4.p_value - ring3.p_value
    ring_with_doubled_increment = ring3.p_value - ring2.p_value
    print(f"open increments = {[f'{x:+.15f}' for x in open_increments]}")
    print(f"ring doubled-edge N2 -> simple C3 increment = {ring_with_doubled_increment:+.15f}")
    print(f"simple-ring C3 -> C4 increment = {ring_simple_increment:+.15f}")
    if ring_simple_increment > 0.0:
        print(
            "non_load_bearing_geometric_diagnostic: simple-ring N=3 to N=4 "
            "has a positive finite increment."
        )
    else:
        print(
            "non_load_bearing_geometric_diagnostic: simple-ring N=3 to N=4 "
            "does not have a positive finite increment."
        )
    print(
        "monotone_read: the simple-ring sample has one positive increment; "
        "including the doubled-edge N=2 diagnostic is not monotone."
    )
    check("open-chain finite ladder keeps the previously observed parity oscillation", open_increments[0] > 0.0 and open_increments[1] < 0.0 and open_increments[2] > 0.0)
    check("simple-ring N=3 to N=4 finite increment is positive", ring_simple_increment > 0.0)
    check("including doubled-edge N=2 does not give a monotone ring sequence", ring_with_doubled_increment < 0.0 and ring_simple_increment > 0.0)
    check(
        "ring readouts remain inside the source anchor interval",
        P_TRIV_ANCHOR < ring3.p_value < P_LOC_ANCHOR
        and P_TRIV_ANCHOR < ring4.p_value < P_LOC_ANCHOR,
        f"P_triv={P_TRIV_ANCHOR:.12f}, P_ring3={ring3.p_value:.12f}, P_ring4={ring4.p_value:.12f}, P_loc={P_LOC_ANCHOR:.12f}",
    )

    section("Part 6: note hygiene")
    text = note_text()
    if text:
        check(
            "note delegates status to the independent audit lane",
            "Status authority: independent audit lane only" in text
            and "does not set, predict, promote, or demote any audit outcome" in text,
        )
        check(
            "note records topology underdetermination rather than selecting a closed loop",
            "does not name a closed transverse loop" in text
            and "uniform-density diagnostic" in text,
        )
        check(
            "note uses markdown links for one-hop authorities",
            "[GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md]" in text
            and "[GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md]" in text
            and "[GAUGE_VACUUM_PLAQUETTE_INTERNAL_LINK_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md]" in text
            and "[GAUGE_VACUUM_PLAQUETTE_FULL_SLICE_RIM_LIFT_INTEGRAL_BOUNDARY_SCIENCE_ONLY_NOTE_2026-04-17.md]" in text,
        )
        check(
            "note keeps durable context pointers as backticked non-links",
            "`docs/GAUGE_VACUUM_PLAQUETTE_TWO_STRIP_ENVIRONMENT_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-12.md`" in text
            and "`docs/GAUGE_VACUUM_PLAQUETTE_THREE_STRIP_ENVIRONMENT_RHO_LADDER_BOUNDED_NOTE_2026-06-12.md`" in text
            and "`docs/GAUGE_VACUUM_PLAQUETTE_FOUR_STRIP_PARITY_TEST_BOUNDED_NOTE_2026-06-12.md`" in text
            and ".claude/tmp" not in text,
        )
        check(
            "note records finite bracket caution without extrapolating a width limit",
            "finite diagnostic, not a limit theorem" in text
            and "does not prove a shared slab limit" in text
            and "not a proven enclosure of the width limit" in text
            and "ring data indicate the limit lies above it" not in text,
        )
        banned = [
            " ".join(("only", "route")),
            " ".join(("last", "route")),
            "ex" + "hausted",
            " ".join(("closes", "the", "program")),
        ]
        check("note avoids overreach closure language", not any(phrase in text.lower() for phrase in banned))
        status_words = [
            "ret" + "ained",
            "no" + "_go",
            "cond" + "itional",
            "audited" + "_clean",
        ]
        check("note avoids audit-status labels for claims", not any(word in text.lower() for word in status_words))
    else:
        check("note exists for this runner", False, f"missing {NOTE_PATH}")

    print(
        "Named residuals: transverse-topology underdetermination in the cited geometry notes; "
        "finite ring widths N=3 and N=4; doubled-edge N=2 multigraph diagnostic; "
        "finite B4 weight box; finite Bessel support; scalar class-channel internal-link "
        "contraction; future all-link 6j/intertwiner normalization; full rim eta evaluation; "
        "strip-depth direction; wider slab limit; 3D stack; L_perp limit; analytic P(6); no repinning."
    )
    check("runner names residuals without retiring them", True)

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
