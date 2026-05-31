#!/usr/bin/env python3
"""
Q1 physical orientation/basepoint probe.

This runner tests the corrected last-mile question:

    Can the oriented C3 frame/basepoint needed by the Q1 sign closeout be
    derived as physical from the current repository surface?

Result:
  - The oriented generator half has a strong bounded bridge: the same
    matrix g used in the Q1 coefficient identity is the proper spatial
    C_3[111] rotation about the Z^3 body diagonal, and the full taste-cube
    descent carries it onto T_1.
  - The full P_ORIENT premise still does not close: the current surface does
    not derive the microscopic full-cube source law / selected-line endpoint
    that chooses the physical based readout.

No PDG masses, fitted selectors, or observed lepton inputs are used.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    PASSES.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}")
    if detail:
        for line in detail.splitlines():
            print(f"       {line}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def read_rel(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


BASIS8 = [
    (0, 0, 0),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 1),
]
INDEX8 = {alpha: idx for idx, alpha in enumerate(BASIS8)}
T1 = [INDEX8[(1, 0, 0)], INDEX8[(0, 1, 0)], INDEX8[(0, 0, 1)]]


def cycle_bits(alpha: tuple[int, int, int]) -> tuple[int, int, int]:
    a, b, c = alpha
    return (c, a, b)


def cube_cycle() -> sp.Matrix:
    u = sp.zeros(8)
    for j, alpha in enumerate(BASIS8):
        u[INDEX8[cycle_bits(alpha)], j] = 1
    return u


def matrix_unit(n: int, i: int, j: int) -> sp.Matrix:
    e = sp.zeros(n)
    e[i, j] = 1
    return e


def compress_t1(x: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([[sp.simplify(x[i, j]) for j in T1] for i in T1])


def avg_c3(u: sp.Matrix, x: sp.Matrix) -> sp.Matrix:
    out = sp.zeros(u.rows)
    uk = sp.eye(u.rows)
    for _ in range(3):
        out += uk * x * uk.T
        uk = u * uk
    return sp.simplify(out / 3)


def main() -> int:
    section("A. Spatial C3[111] fixes an oriented generator")

    g = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    g2 = g**2
    tau = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])

    n = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    theta = 2 * sp.pi / 3
    n_cross = sp.Matrix(
        [
            [0, -n[2], n[1]],
            [n[2], 0, -n[0]],
            [-n[1], n[0], 0],
        ]
    )
    rodrigues = sp.simplify(
        sp.cos(theta) * sp.eye(3)
        + sp.sin(theta) * n_cross
        + (1 - sp.cos(theta)) * (n * n.T)
    )

    record(
        "A.1 Rodrigues rotation by +2*pi/3 about (1,1,1) equals g",
        sp.simplify(rodrigues - g) == sp.zeros(3),
        f"g={g}",
    )
    record(
        "A.2 g is a proper spatial rotation",
        g**3 == sp.eye(3) and sp.det(g) == 1,
        f"det(g)={sp.det(g)}, g^3=I",
    )
    record(
        "A.3 a transposition mirrors the oriented generator",
        tau * g * tau == g2 and tau * g2 * tau == g,
        "tau swaps g and g^2.",
    )

    section("B. Full taste-cube descent carries the same g to T1")

    u8 = cube_cycle()
    p1 = sp.zeros(8)
    for i in T1:
        p1[i, i] = 1

    i100 = INDEX8[(1, 0, 0)]
    i010 = INDEX8[(0, 1, 0)]
    qf = sp.simplify(3 * avg_c3(u8, matrix_unit(8, i010, i100)))
    qb = sp.simplify(3 * avg_c3(u8, matrix_unit(8, i100, i010)))
    q2 = sp.simplify(sp.I * (qf - qb))

    record(
        "B.1 T1 is invariant under the full cube C3 action",
        u8 * p1 == p1 * u8,
        "P_T1 commutes with U8.",
    )
    record(
        "B.2 restricted full-cube C3 action is exactly the Q1 generator g",
        compress_t1(u8) == g,
        "U8|T1 = g.",
    )
    record(
        "B.3 forward/backward full-cube orbit sources descend to g and g^2",
        compress_t1(qf) == g and compress_t1(qb) == g2,
        "P1 Qf P1 = g, P1 Qb P1 = g^2.",
    )
    record(
        "B.4 the C3-odd Hermitian orbit channel descends to i(g-g^2)",
        compress_t1(q2) == sp.I * (g - g2),
        "P1 i(Qf-Qb) P1 = i(g-g^2).",
    )

    section("C. Q1 sign in the physically oriented g carrier")

    eta_aps = sp.Rational(2, 9)
    s_q1 = sp.Rational(10, 9) * sp.eye(3) - eta_aps * g - eta_aps * g2
    coeff_g = sp.Rational(-2, 9)
    odd_line = sp.I * (g - g2)
    odd_projection = sp.simplify(
        sp.trace(s_q1 * odd_line) / sp.trace(odd_line * odd_line)
    )

    record(
        "C.1 Q1 source has coeff_g=-2/9 in the spatial/taste g frame",
        s_q1 == sp.Rational(10, 9) * sp.eye(3) + coeff_g * g + coeff_g * g2,
        f"S_Q1={s_q1}",
    )
    record(
        "C.2 oriented positive readout gives +eta_APS",
        -coeff_g == eta_aps,
        f"-coeff_g={-coeff_g}, eta_APS={eta_aps}",
    )
    record(
        "C.3 Q1 still has no intrinsic odd projection",
        odd_projection == 0,
        "The orientation comes from spatial/taste structure, not from Q1 alone.",
    )

    section("D. Repo firewalls around physical basepoint closure")

    spatial_runner = read_rel("scripts/frontier_koide_c3_spatial_rotation.py")
    taste_note = read_rel("docs/KOIDE_TASTE_CUBE_CYCLIC_SOURCE_DESCENT_NOTE_2026-04-18.md")
    s3_note = read_rel("docs/S3_TASTE_CUBE_DECOMPOSITION_NOTE.md")
    selected_no_go = read_rel(
        "docs/CHARGED_LEPTON_SELECTED_LINE_GENERATION_SELECTOR_NO_GO_NOTE_2026-04-27.md"
    )
    parity_note = read_rel("docs/NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23.md")
    aps_parity_note = read_rel(
        "docs/KOIDE_PHASE_APS_ETA_PARITY_ROUTE_NARROW_THEOREM_NOTE_2026-05-23.md"
    )
    pmns_note = read_rel(
        "docs/PMNS_GRAPH_FIRST_FORWARD_CYCLE_RESIDUAL_SWAP_BRIDGE_NARROW_THEOREM_NOTE_2026-05-24.md"
    )

    record(
        "D.1 existing C3 runner already isolates this as the physical-observable bridge",
        "physical-observable bridge identifying the selected-line Brannen phase with this ambient invariant"
        in flat(spatial_runner),
    )
    record(
        "D.2 taste-cube descent still leaves the microscopic source law open",
        "does **not** yet derive" in taste_note
        and "microscopic full-cube source law" in taste_note
        and "final mass/amplitude readout primitive" in taste_note,
    )
    record(
        "D.3 taste-cube physical-carrier reading is still gated",
        "staggered-Dirac realization derivation target" in taste_note
        and "currently an open gate" in s3_note,
    )
    record(
        "D.4 selected-line generation/basepoint no-go still requires based endpoint or source law",
        "basepoint is additional physical data" in selected_no_go
        and "BASED_ENDPOINT_OR_SOURCE_LAW_REQUIRED=TRUE" in selected_no_go,
    )
    record(
        "D.5 retained bounded parity algebra supplies the delta odd line and fixed loci",
        "transpositions send delta to -delta" in parity_note
        or "sends `delta -> -delta`" in parity_note
        or "sends `delta \u2192 -delta`" in parity_note,
    )
    record(
        "D.6 APS+parity support still names delta=eta_APS as the remaining gap",
        "single remaining gap is the physical identification" in flat(aps_parity_note),
    )
    record(
        "D.7 PMNS graph-first forward convention is not imported as Koide orientation closure",
        "Does **not** uniquely select between the forward 3-cycle" in pmns_note
        and "Does **not** identify the active sector" in pmns_note,
    )

    section("E. Verdict")

    oriented_generator_lands = all(
        ok
        for name, ok, _ in PASSES
        if name.startswith("A.") or name.startswith("B.") or name.startswith("C.")
    )
    physical_basepoint_still_open = all(
        ok
        for name, ok, _ in PASSES
        if name.startswith("D.1")
        or name.startswith("D.2")
        or name.startswith("D.3")
        or name.startswith("D.4")
        or name.startswith("D.6")
    )

    record(
        "E.1 oriented generator is physically sourced as bounded spatial/taste support",
        oriented_generator_lands,
        "The same g is a proper spatial C3[111] rotation and the T1 descent image.",
    )
    record(
        "E.2 full physical P_ORIENT remains open because the selected endpoint/source law is not derived",
        physical_basepoint_still_open,
        "The missing theorem is now narrower: source law / endpoint / delta=eta_APS identification.",
    )

    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_total = len(PASSES)
    print()
    print("=" * 88)
    print("Summary")
    print("=" * 88)
    print(f"PASSED: {n_pass}/{n_total}")
    for name, ok, _ in PASSES:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print()
    if n_pass == n_total:
        print("VERDICT: physical orientation/basepoint probe lands bounded support, not full closure.")
        print("KOIDE_Q1_PHYSICAL_ORIENTATION_BASEPOINT_PROBE=BOUNDED_SUPPORT")
        print("SPATIAL_C3_FIXES_ORIENTED_GENERATOR_G=TRUE")
        print("TASTE_CUBE_DESCENT_CARRIES_G_TO_T1=TRUE")
        print("Q1_DELTA_PLUS_FROM_SPATIAL_TASTE_G_FRAME=TRUE")
        print("Q1_ALONE_DERIVES_ODD_ORIENTATION=FALSE")
        print("PARITY_BASEPOINT_SUPPORT_AVAILABLE=TRUE")
        print("MICROSCOPIC_FULL_CUBE_SOURCE_LAW_DERIVED=FALSE")
        print("SELECTED_LINE_ENDPOINT_BASEPOINT_DERIVED=FALSE")
        print("P_ORIENT_FULL_CURRENT_SURFACE_CLOSURE=FALSE")
        print("NEXT_THEOREM=derive_full_cube_source_law_selects_forward_oriented_channel_and_selected_line_endpoint")
        return 0

    print("VERDICT: physical orientation/basepoint probe has failing checks.")
    print("KOIDE_Q1_PHYSICAL_ORIENTATION_BASEPOINT_PROBE=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
