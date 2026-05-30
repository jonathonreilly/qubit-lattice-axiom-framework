#!/usr/bin/env python3
"""Audit-companion runner for
POISSON_SELF_GRAVITY_ZERO_COUPLING_EXACT_REDUCTION_NARROW_THEOREM_NOTE_2026-05-17.

Narrow theorem: the zero-coupling reduction of
`scripts/poisson_self_gravity_loop.py` is a bit-exact code-level
identity, not a numerical coincidence.

Three parts proven:

  Part 1: `_poisson_like_field(..., coupling=0.0)` returns the
          identically-zero field on every lattice cell, by the
          IEEE-754 invariant `0.0 * y = 0.0` for finite `y`.

  Part 2: `_self_consistent_loop` converges in <= 2 iterations at
          `epsilon * source_strength = 0`, with the returned field
          identically zero and final `field_delta = 0.0`.

  Part 3: With `field_layers == 0`, `_propagate_from_sources` reduces
          to the bare lattice propagator: per-offset phase factor
          becomes `complex(cos(k*L), sin(k*L))`, recovering the free
          centroid and free escape probability bit-exactly.

Class A: purely algebraic identity on the loop runner's own code.
No fitted parameters, no observational comparator, no literature
import. Does NOT promote `poisson_self_gravity_loop_note` or transit
the conditional upstream `minimal_source_driven_field_probe_note`.
"""

from __future__ import annotations

import math
import os
import random
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

# Import the loop runner module as the source-of-truth for the
# function bodies under test. (Side-effects: top-level constants and
# function definitions only. No script side-effects run on import.)
import scripts.poisson_self_gravity_loop as psg  # noqa: E402
import scripts.minimal_source_driven_field_probe as m  # noqa: E402


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


# ----------------------------------------------------------------------
# Stub lattice for Part 1 — exercises kernel ONLY through arbitrary
# position table and loop ranges; deliberately does NOT reuse the
# upstream Lattice3D, so the identity is provably independent of the
# inherited primitives.
# ----------------------------------------------------------------------
class StubLat:
    def __init__(self, nl: int, npl: int, positions: list[tuple[float, float, float]]):
        assert len(positions) == nl * npl, (
            f"position table size {len(positions)} != nl*npl {nl*npl}"
        )
        self.nl = nl
        self.npl = npl
        self.pos = positions
        self.layer_start = [layer * npl for layer in range(nl)]


def _make_stub_lat(nl: int, npl: int, seed: int) -> StubLat:
    rng = random.Random(seed)
    positions: list[tuple[float, float, float]] = []
    for layer in range(nl):
        for i in range(npl):
            positions.append(
                (
                    rng.uniform(-10.0, 10.0),
                    rng.uniform(-10.0, 10.0),
                    rng.uniform(-10.0, 10.0),
                )
            )
    return StubLat(nl=nl, npl=npl, positions=positions)


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact bit-equality + structural reduction) for")
    print("POISSON_SELF_GRAVITY_ZERO_COUPLING_EXACT_REDUCTION_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: prove the runner's zero-coupling reduction is a bit-exact code identity")
    print("=" * 88)

    # ==================================================================
    section("Part 1: kernel identity _poisson_like_field(..., coupling=0.0) == 0")
    # ==================================================================
    # Sub-test A: empty source_nodes early-return is identically zero.
    stub = _make_stub_lat(nl=4, npl=9, seed=20260517)
    fld_empty = psg._poisson_like_field(
        stub,
        source_nodes=[],
        weights=[],
        coupling=0.0,
    )
    ok_empty_shape = (
        len(fld_empty) == stub.nl
        and all(len(row) == stub.npl for row in fld_empty)
    )
    check(
        "Part 1.A — empty source: shape is (nl, npl)",
        ok_empty_shape,
        detail=f"shape=({len(fld_empty)}, {len(fld_empty[0]) if fld_empty else 0})",
    )
    ok_empty_zero = all(v == 0.0 for row in fld_empty for v in row)
    check(
        "Part 1.A — empty source: every entry is bit-exactly 0.0",
        ok_empty_zero,
        detail="all entries `v == 0.0` (not `abs(v) < tol`)",
    )

    # Sub-test B: non-empty source with coupling=0.0; vary weights, src,
    # screening params; identity must hold bit-exactly in every case.
    cases = [
        # (source_nodes, weights, FIELD_EPS_override, FIELD_MU_override, label)
        ([0, 5, 10], [1 / 3.0, 1 / 3.0, 1 / 3.0], 0.5, 0.08, "uniform 3-src"),
        ([2, 17], [0.7, 0.3], 0.1, 1.5, "weighted 2-src tight kernel"),
        ([0], [1.0], 2.0, 0.01, "single src wide screen"),
        ([1, 3, 5, 7, 9, 11], [0.1, 0.1, 0.2, 0.3, 0.2, 0.1], 0.5, 0.5, "6-src strong screen"),
        ([0, 1, 2, 3, 4], [0.0, 0.0, 1.0, 0.0, 0.0], 0.5, 0.08, "weight-spike"),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8], [1 / 9.0] * 9, 0.5, 0.08, "uniform 9-src"),
    ]
    for src_nodes, weights, feps, fmu, label in cases:
        # Temporarily override the module-level constants used inside
        # the kernel function; restore after.
        old_eps = psg.FIELD_EPS
        old_mu = psg.FIELD_MU
        try:
            psg.FIELD_EPS = feps
            psg.FIELD_MU = fmu
            fld = psg._poisson_like_field(
                stub,
                source_nodes=src_nodes,
                weights=weights,
                coupling=0.0,
            )
        finally:
            psg.FIELD_EPS = old_eps
            psg.FIELD_MU = old_mu
        all_bit_zero = all(v == 0.0 for row in fld for v in row)
        check(
            f"Part 1.B — non-empty: coupling=0.0 -> field == 0.0 bit-exactly ({label})",
            all_bit_zero,
            detail=f"FIELD_EPS={feps} FIELD_MU={fmu} nsrc={len(src_nodes)}",
        )

    # Sub-test C: IEEE-754 invariant 0.0 * y = 0.0 over the actual
    # numerical regime used by the kernel (r in [FIELD_EPS, ~]).
    rng = random.Random(20260517)
    n_stress = 10000
    max_abs = 0.0
    for _ in range(n_stress):
        # r in [0.5, 100], FIELD_MU in [0.01, 10], so multiplicand y
        # spans many decades but stays finite.
        r = rng.uniform(0.5, 100.0)
        mu = rng.uniform(0.01, 10.0)
        y = math.exp(-mu * r) / r
        z = 0.0 * y
        if z != 0.0:
            max_abs = max(max_abs, abs(z))
    check(
        f"Part 1.C — IEEE-754 stress: 0.0 * y == 0.0 bit-exactly for {n_stress} random finite y",
        max_abs == 0.0,
        detail=f"max |0.0 * y| over stress sweep = {max_abs}",
    )

    # ==================================================================
    section("Part 2: outer-loop convergence in <= 2 iter at eps*s = 0")
    # ==================================================================
    # Use the real Lattice3D so we exercise the runner's actual outer
    # loop on its actual lattice. We do NOT use the upstream lattice
    # for any value injection; the convergence claim only depends on
    # the loop runner's own code.
    lat = m.Lattice3D.build(psg.NL_PHYS, psg.PW, psg.H)
    source_nodes = psg._source_cluster_nodes(lat)

    # Case 2A: epsilon = 0, source_strength > 0
    fld_2a, w_2a, conv_2a, niter_2a, delta_2a = psg._self_consistent_loop(
        lat,
        source_strength=1.0,
        epsilon=0.0,
        source_nodes=source_nodes,
        gain=1.0e6,  # arbitrary; irrelevant when raw_field is all zero
        max_iters=psg.MAX_ITERS,
    )
    check(
        "Part 2.A — eps=0, s>0: converged",
        conv_2a,
    )
    check(
        "Part 2.A — eps=0, s>0: n_iter <= 2",
        niter_2a <= 2,
        detail=f"n_iter = {niter_2a}",
    )
    check(
        "Part 2.A — eps=0, s>0: final field_delta == 0.0 bit-exactly",
        delta_2a == 0.0,
        detail=f"field_delta = {delta_2a}",
    )
    check(
        "Part 2.A — eps=0, s>0: returned field is identically zero",
        all(v == 0.0 for row in fld_2a for v in row),
    )

    # Case 2B: source_strength = 0, epsilon > 0
    fld_2b, w_2b, conv_2b, niter_2b, delta_2b = psg._self_consistent_loop(
        lat,
        source_strength=0.0,
        epsilon=1.0,
        source_nodes=source_nodes,
        gain=1.0e6,
        max_iters=psg.MAX_ITERS,
    )
    check(
        "Part 2.B — s=0, eps>0: converged",
        conv_2b,
    )
    check(
        "Part 2.B — s=0, eps>0: n_iter <= 2",
        niter_2b <= 2,
        detail=f"n_iter = {niter_2b}",
    )
    check(
        "Part 2.B — s=0, eps>0: final field_delta == 0.0 bit-exactly",
        delta_2b == 0.0,
        detail=f"field_delta = {delta_2b}",
    )
    check(
        "Part 2.B — s=0, eps>0: returned field is identically zero",
        all(v == 0.0 for row in fld_2b for v in row),
    )

    # Case 2C: both zero (degenerate doubly-zero case)
    fld_2c, w_2c, conv_2c, niter_2c, delta_2c = psg._self_consistent_loop(
        lat,
        source_strength=0.0,
        epsilon=0.0,
        source_nodes=source_nodes,
        gain=1.0,
        max_iters=psg.MAX_ITERS,
    )
    check(
        "Part 2.C — s=0, eps=0: converged",
        conv_2c,
    )
    check(
        "Part 2.C — s=0, eps=0: n_iter <= 2",
        niter_2c <= 2,
        detail=f"n_iter = {niter_2c}",
    )
    check(
        "Part 2.C — s=0, eps=0: final field_delta == 0.0 bit-exactly",
        delta_2c == 0.0,
        detail=f"field_delta = {delta_2c}",
    )

    # Case 2D: gain independence — sweep across many gain values; all
    # must give bit-identical results.
    for gain in [1e-6, 1e-3, 1.0, 1e3, 1e6, 1e9]:
        _, _, conv_g, niter_g, delta_g = psg._self_consistent_loop(
            lat,
            source_strength=1.0,
            epsilon=0.0,
            source_nodes=source_nodes,
            gain=gain,
            max_iters=psg.MAX_ITERS,
        )
        check(
            f"Part 2.D — eps=0 gain={gain:.0e}: still converges in <= 2 iter, delta=0.0",
            conv_g and niter_g <= 2 and delta_g == 0.0,
            detail=f"conv={conv_g} n_iter={niter_g} delta={delta_g}",
        )

    # ==================================================================
    section("Part 3: bare-lattice propagator reduction (centroid, escape)")
    # ==================================================================
    # Build the bare-lattice free propagator (zero field, origin source).
    zero_field = [[0.0 for _ in range(lat.npl)] for _ in range(lat.nl)]
    free_amps = psg._propagate_from_sources(lat, zero_field, m.K, [lat.nmap[(0, 0, 0)]])

    # Run the converged eps=0 loop (which is provably zero field) and
    # compute the same observables.
    loop_field, _, _, _, _ = psg._self_consistent_loop(
        lat,
        source_strength=1.0,
        epsilon=0.0,
        source_nodes=source_nodes,
        gain=1.0,
        max_iters=psg.MAX_ITERS,
    )
    loop_amps = psg._propagate_from_sources(lat, loop_field, m.K, [lat.nmap[(0, 0, 0)]])

    # Centroid shift exact zero (bit-equality on the floats produced)
    z_free = psg._centroid_z(free_amps, lat)
    z_loop = psg._centroid_z(loop_amps, lat)
    check(
        "Part 3.A — centroid_z(loop, eps=0) == centroid_z(free) bit-exactly",
        z_loop == z_free,
        detail=f"z_loop={z_loop:.18e} z_free={z_free:.18e}",
    )

    # Escape probability exact unity (bit-equality of detector probs)
    p_free = psg._detector_prob(free_amps, lat)
    p_loop = psg._detector_prob(loop_amps, lat)
    check(
        "Part 3.B — detector_prob(loop, eps=0) == detector_prob(free) bit-exactly",
        p_loop == p_free,
        detail=f"p_loop={p_loop:.18e} p_free={p_free:.18e}",
    )

    # Bit-equality of the amplitude vector itself: every detector cell
    # must agree exactly with the free propagator.
    det_start = lat.layer_start[lat.nl - 1]
    n_det = lat.npl
    amps_equal = all(
        loop_amps[det_start + i] == free_amps[det_start + i] for i in range(n_det)
    )
    check(
        "Part 3.C — detector amplitudes bit-identical to bare lattice propagator",
        amps_equal,
        detail=f"checked {n_det} detector cells",
    )

    # Reduction of the local field update lf to zero on the zero field
    # (this is the structural reason for the bare propagator reduction):
    # for any cell (si, di), lf = 0.5 * (sf[si] + df[di]) = 0; act =
    # L * (1.0 - 0) = L. We verify this directly on the zero field.
    arbitrary_layer = 0
    sf = zero_field[arbitrary_layer]
    df = zero_field[min(arbitrary_layer + 1, lat.nl - 1)]
    all_lf_zero = all(0.5 * (sf[si] + df[di]) == 0.0 for si in range(lat.npl) for di in range(lat.npl))
    check(
        "Part 3.D — local field update lf == 0.0 bit-exactly on zero field",
        all_lf_zero,
        detail=f"checked all {lat.npl * lat.npl} (si, di) pairs in layer 0",
    )

    # ==================================================================
    section("Part 4: cross-check vs cached run")
    # ==================================================================
    cache_path = os.path.join(
        ROOT, "logs", "runner-cache", "poisson_self_gravity_loop.txt"
    )
    cached_ok = False
    cached_lines: list[str] = []
    if os.path.exists(cache_path):
        with open(cache_path, "r") as f:
            cached_lines = f.read().splitlines()
        # Find the reduction-check block
        red = {
            "zero-epsilon centroid shift": None,
            "zero-epsilon escape ratio": None,
            "zero-epsilon iters/residual": None,
        }
        for line in cached_lines:
            for key in red:
                if key in line:
                    red[key] = line.strip()
        cached_ok = (
            red["zero-epsilon centroid shift"] is not None
            and "+0.000000e+00" in red["zero-epsilon centroid shift"]
            and red["zero-epsilon escape ratio"] is not None
            and "1.000000" in red["zero-epsilon escape ratio"]
            and red["zero-epsilon iters/residual"] is not None
        )
        if cached_ok:
            check(
                "Part 4 — cached run: zero-epsilon shift = +0.000000e+00 (matches theorem)",
                True,
                detail=red["zero-epsilon centroid shift"],
            )
            check(
                "Part 4 — cached run: zero-epsilon escape = 1.000000 (matches theorem)",
                True,
                detail=red["zero-epsilon escape ratio"],
            )
            check(
                "Part 4 — cached run: iter count <= 2 (matches Part 2)",
                "2 /" in red["zero-epsilon iters/residual"],
                detail=red["zero-epsilon iters/residual"],
            )
        else:
            check(
                "Part 4 — cached run parse",
                False,
                detail=f"failed to parse expected reduction block: {red}",
            )
    else:
        # If the cache isn't present at audit time, this part is
        # informational only — the theorem proper is established by
        # Parts 1-3.
        print(f"  [INFO] cache not found at {cache_path} — Part 4 skipped (Parts 1-3 stand)")

    # ==================================================================
    section("SCORECARD")
    # ==================================================================
    print()
    print(f"  PASS = {PASS}")
    print(f"  FAIL = {FAIL}")
    print()

    # Boundary guards (printed only, not counted in PASS/FAIL)
    boundary_guards = [
        "Does NOT promote poisson_self_gravity_loop_note or change its independent audit posture.",
        "Does NOT claim nonzero-coupling convergence, weak-field saturation, or backreaction.",
        "Does NOT ratify the upstream minimal_source_driven_field_probe_note.",
        "Does NOT depend on V3 sibling's _run_loop (different runner, different short-circuit).",
        "Holds on standards-compliant IEEE-754 float64 implementations (CPython on x86_64/arm64).",
    ]
    print("  [BOUNDARY] explicit boundary guards (printed only):")
    for g in boundary_guards:
        print(f"    - {g}")

    print()
    if FAIL == 0:
        print("  STATUS: ALL EXACT-IDENTITY CHECKS PASS")
        print("  CLOSURE: Zero-coupling reduction of the Poisson self-gravity loop")
        print("           runner is a bit-exact code identity, not a numerical")
        print("           coincidence. Class A narrow theorem.")
        return 0
    else:
        print("  STATUS: FAIL — bit-exact identity broke")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
