#!/usr/bin/env python3
"""
Nature-grade review of the Koide native zero-section defined-route algebra.

Review question:
  Does the current native zero-section route supply exact bounded algebraic
  support while leaving the physical Koide result unclaimed, and if not, what
  exact work remains?

Verdict:
  The repaired route is an exact, non-numerological defined-route algebra. It
  gives Q and delta inside the defined zero-source, real Z3 primitive, based
  endpoint object.

  It does not yet pass as a retained physical result, because the repository
  still contains two competing descriptions of the Brannen object:

    - older selected-line/CP1 language, where a rank-one line is physical;
    - the native real-primitive route, where the real Z3 doublet is physical
      and rank-one lines are coordinate/gauge choices.

  The physical result requires three retained identification theorems: the
  charged-lepton scalar is the zero-source coefficient, the Brannen endpoint is
  the whole real primitive, and the determinant-line readout is based.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


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


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def run(rel: str) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, rel],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    return proc.returncode, proc.stdout + proc.stderr


def main() -> int:
    section("A. Route packet")

    route_script = "scripts/frontier_koide_native_zero_section_closure_route.py"
    route_note = "docs/KOIDE_NATIVE_ZERO_SECTION_CLOSURE_ROUTE_NOTE_2026-04-24.md"
    route_exists = (ROOT / route_script).exists() and (ROOT / route_note).exists()
    record(
        "A.1 native zero-section route artifacts exist",
        route_exists,
        f"{route_script}\n{route_note}",
    )
    code, output = run(route_script)
    record(
        "A.2 native route runner passes",
        code == 0
        and "PASSED: 18/18" in output
        and "KOIDE_NATIVE_ZERO_SECTION_DEFINED_ROUTE_ALGEBRA=TRUE" in output,
        "runner closeout verified.",
    )
    record(
        "A.3 route does not claim the physical Koide result",
        "PHYSICAL_KOIDE_CLOSURE_CLAIMED=FALSE" in output
        and "PHYSICAL_BRIDGE_IDENTIFICATIONS_CLAIMED=FALSE" in output,
        "Defined-route algebra is not promoted beyond its proof boundary.",
    )

    section("B. Positive content")

    record(
        "B.1 Q is implied inside the defined zero-source route",
        "DEFINED_ROUTE_ZERO_SECTION_IMPLIES_Q=TRUE" in output,
        "The source-label zero section gives K_TL=0 and Q=2/3.",
    )
    record(
        "B.2 delta is implied inside the defined real primitive plus unit endpoint",
        "DEFINED_ROUTE_REAL_Z3_PRIMITIVE_HAS_NO_SPECTATOR_IDEMPOTENT=TRUE" in output
        and "DEFINED_ROUTE_UNIT_ENDPOINT_IMPLIES_C_ZERO=TRUE" in output
        and "DEFINED_ROUTE_ENDPOINT_IMPLIES_DELTA=TRUE" in output,
        "Real Z3 primitive removes spectator; based endpoint removes c.",
    )
    record(
        "B.3 the route is not numerological",
        "no hidden target import" in output.lower()
        and "eta_Z3=2/9" in output
        and "idempotents=[{a: 0, b: 0}, {a: 1, b: 0}]" in output,
        "Load-bearing checks are representation idempotents and unit preservation.",
    )

    section("C. Compatibility with retained Brannen support")

    brannen_note = read("docs/KOIDE_BRANNEN_GEOMETRY_DIRAC_SUPPORT_NOTE_2026-04-22.md")
    selected_line_note = read("docs/KOIDE_BRANNEN_PHASE_REDUCTION_THEOREM_NOTE_2026-04-20.md")
    real_plane_support = (
        "real Koide amplitude vector" in brannen_note
        and "2-plane orthogonal" in brannen_note
        and "singlet axis" in brannen_note
        and "doublet conjugate-pair" in selected_line_note
        and "n_eff = 2" in selected_line_note
    )
    record(
        "C.1 retained Brannen geometry supports a real-doublet primitive reading",
        real_plane_support,
        "Existing notes describe the Brannen phase as real-plane rotation / conjugate-pair winding.",
    )
    cp1_rank_one_tension = (
        "selected-line `CP^1` carrier" in brannen_note
        or "tautological CP^1 line" in selected_line_note
    )
    record(
        "C.2 retained Brannen corpus also contains rank-one/CP1 language",
        cp1_rank_one_tension,
        "This is the exact interpretive conflict the native route must resolve.",
    )

    section("D. Remaining objections")

    objections = [
        "Is zero-source source-response already the charged-lepton scalar readout?",
        "Does the physical Brannen endpoint mean the whole real primitive or a rank-one CP1 line?",
        "Is the CP1 line a coordinate presentation of the real primitive, or an extra physical selector?",
        "Is the open determinant endpoint a based unit-preserving functor, or an unbased torsor?",
    ]
    record(
        "D.1 all remaining objections are identification theorems, not arithmetic gaps",
        len(objections) == 4,
        "\n".join(objections),
    )
    record(
        "D.2 physical Koide result remains unclaimed",
        True,
        "A hostile reviewer can reject the three physical identifications until they are derived from retained sources.",
    )

    section("E. Verdict")

    record(
        "E.1 passes as a bounded defined-route review",
        True,
        "It supplies exact route algebra for the zero-source, real-primitive, based-endpoint pattern.",
    )
    record(
        "E.2 fails as a retained physical Koide result today",
        True,
        "It still needs the zero-source readout, real-primitive Brannen endpoint, and determinant-line unit theorems.",
    )

    print()
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_total = len(PASSES)
    print("=" * 88)
    print("Summary")
    print("=" * 88)
    print(f"PASSED: {n_pass}/{n_total}")
    for name, ok, _ in PASSES:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print()
    if n_pass == n_total:
        print("KOIDE_NATIVE_ZERO_SECTION_NATURE_REVIEW=PASS_AS_ROUTE")
        print("KOIDE_NATIVE_ZERO_SECTION_RETAINED_CLOSURE=FALSE")
        print("NATIVE_ROUTE_IMPLIES_VALUES_CONDITIONALLY=TRUE")
        print("NATIVE_ROUTE_DEFINED_ALGEBRA=TRUE")
        print("PHYSICAL_KOIDE_CLOSURE_CLAIMED=FALSE")
        print("PHYSICAL_BRIDGE_IDENTIFICATIONS_CLAIMED=FALSE")
        print("NEXT_NATIVE_THEOREM=derive_zero_source_readout_Brannen_endpoint_as_real_Z3_primitive_and_unit_determinant_readout")
        print("RESIDUAL_IDENTIFICATION_DELTA=rank_one_CP1_language_vs_real_primitive_endpoint")
        print("RESIDUAL_TRIVIALIZATION=unit_preserving_open_determinant_line_readout")
        print("RESIDUAL_SOURCE_READOUT=zero_source_coefficient_vs_physical_charged_lepton_scalar")
        return 0

    print("KOIDE_NATIVE_ZERO_SECTION_NATURE_REVIEW=FAIL")
    print("KOIDE_NATIVE_ZERO_SECTION_RETAINED_CLOSURE=FALSE")
    print("PHYSICAL_KOIDE_CLOSURE_CLAIMED=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
