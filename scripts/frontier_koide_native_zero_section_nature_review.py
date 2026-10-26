#!/usr/bin/env python3
"""Actual one-child contract for the supplied finite native-zero algebra.
Documentary historical strings and open questions are not scientific checks.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ('docs/KOIDE_NATIVE_ZERO_SECTION_NATURE_REVIEW_NOTE_2026-04-24.md', 'scripts/frontier_koide_native_zero_section_closure_route.py', 'docs/KOIDE_NATIVE_ZERO_SECTION_CLOSURE_ROUTE_NOTE_2026-04-24.md', 'docs/KOIDE_BRANNEN_PHASE_REDUCTION_THEOREM_NOTE_2026-04-20.md', 'docs/KOIDE_BRANNEN_GEOMETRY_DIRAC_SUPPORT_NOTE_2026-04-22.md')
PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    PASSES.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}")
    if detail:
        for line in detail.splitlines():
            print(f"       {line}")


def historical(name, condition, detail=""):
    print(f"HISTORICAL_UNSCORED old assertion={name!r}; observed={bool(condition)}; old detail={detail!r}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def run(rel: str) -> tuple[int, str]:
    try:
        proc = subprocess.run([sys.executable, rel], cwd=ROOT, check=False,
                              text=True, capture_output=True, timeout=120)
    except subprocess.TimeoutExpired as exc:
        return 124, f"CHILD_TIMEOUT: {exc}"
    except OSError as exc:
        return 127, f"CHILD_EXECUTION_ERROR: {exc}"
    return proc.returncode, proc.stdout + proc.stderr


def main() -> int:
    PASSES.clear()
    for p in AUDIT_INPUT_PATHS:
        if not (ROOT/p).is_file():
            print(f"FAIL missing input {p}")
            return 1
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
        and output.splitlines().count("PASSED: 16/16") == 1
        and output.splitlines().count("SUPPLIED_ROUTE_MATH_CHECKS=PASS") == 1
        and "[FAIL]" not in output
        and "CHILD_" not in output,
        "runner closeout verified.",
    )
    record(
        "A.3 route does not claim the physical Koide result",
        "PHYSICAL_IDENTIFICATION_PROVED=FALSE" in output,
        "Defined-route algebra is not promoted beyond its proof boundary.",
    )

    section("B. Child output contract (not independent proof)")
    record("B.1 child reports all16 actual mathematical conditions successful",
           code == 0 and output.splitlines().count("SUPPLIED_ROUTE_MATH_CHECKS=PASS") == 1 and output.splitlines().count("PASSED: 16/16") == 1)
    record("B.2 child explicitly declares its supplied endpoint law",
           "SUPPLIED_ENDPOINT_LAW=selected*eta+c; selected=1,c=0" in output)
    historical("B.3 old non-numerological provenance assertion",
               "no hidden target import" in output.lower() and "eta_Z3=2/9" in output
               and "idempotents=[{a: 0, b: 0}, {a: 1, b: 0}]" in output,
               "Withdrawn: finite sum and flags do not prove independent physical endpoint selection.")

    section("C. Unscored historical text observations, not proof suppliers")

    brannen_note = read("docs/KOIDE_BRANNEN_GEOMETRY_DIRAC_SUPPORT_NOTE_2026-04-22.md")
    selected_line_note = read("docs/KOIDE_BRANNEN_PHASE_REDUCTION_THEOREM_NOTE_2026-04-20.md")
    real_plane_support = (
        "real Koide amplitude vector" in brannen_note
        and "2-plane orthogonal" in brannen_note
        and "singlet axis" in brannen_note
        and "doublet conjugate-pair" in selected_line_note
        and "n_eff = 2" in selected_line_note
    )
    historical(
        "C.1 retained Brannen geometry supports a real-doublet primitive reading",
        real_plane_support,
        "Existing notes describe the Brannen phase as real-plane rotation / conjugate-pair winding.",
    )
    cp1_rank_one_tension = (
        "selected-line `CP^1` carrier" in brannen_note
        or "tautological CP^1 line" in selected_line_note
    )
    historical(
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
    historical(
        "D.1 all remaining objections are identification theorems, not arithmetic gaps",
        len(objections) == 4,
        "\n".join(objections),
    )
    historical(
        "D.2 physical Koide result remains unclaimed",
        True,
        "A hostile reviewer can reject the three physical identifications until they are derived from retained sources.",
    )

    section("E. Verdict")

    historical(
        "E.1 passes as a bounded defined-route review",
        True,
        "It supplies exact route algebra for the zero-source, real-primitive, based-endpoint pattern.",
    )
    historical(
        "E.2 fails as a retained physical Koide result today",
        True,
        "It still needs the zero-source readout, real-primitive Brannen endpoint, and determinant-line unit theorems.",
    )

    print("INFO: supplied zero source, affine endpoint form, selected=1 and c=0 are premises.")
    print("INFO: physical readout, phase, anomaly and dynamics identification are not proved; questions above are not exhaustive.")
    n_pass=sum(bool(ok) for _,ok,_ in PASSES)
    print(f"PASSED: {n_pass}/{len(PASSES)}")
    print("ONE_CHILD_CONTRACT_ONLY; NO_PHYSICAL_OR_AUDIT_VERDICT")
    return 0 if n_pass==len(PASSES) else 1

if __name__ == "__main__":
    sys.exit(main())
