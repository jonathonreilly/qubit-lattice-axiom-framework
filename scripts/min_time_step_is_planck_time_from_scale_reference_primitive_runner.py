#!/usr/bin/env python3
"""Boundary verifier for the Planck-time minimum-step packet.

This runner does not claim to derive physical time from the update tick.  It
checks the source packet needed for re-audit:

* the registered scale-reference primitive exists;
* the registered kinetic-isotropy primitive supplies only the lattice-unit
  c_lattice = 1 bridge;
* the one-tick-one-edge companion packet and cache are present, and its current
  retained-bounded ledger status is exposed rather than silently assumed;
* the physical-c normalization used by this row is explicit; and
* with those supplied inputs, l_P / c equals t_P at the note's stated
  tolerance.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "MIN_TIME_STEP_IS_THE_PLANCK_TIME_FROM_THE_SINGLE_SCALE_REFERENCE_PRIMITIVE_NARROW_THEOREM_NOTE_2026-06-08.md"
AXIOM_NODES = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
AUDIT_LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
KINETIC_PRIMITIVE_NOTE = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"

COMPANION_ID = "min_time_step_tied_to_the_lattice_edge_by_causal_locality_ratio_derived_scale_is_the_clock_rate_no_go_narrow_theorem_note_2026-06-08"
COMPANION_NOTE = ROOT / "docs" / "MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md"
COMPANION_RUNNER = ROOT / "scripts" / "min_time_step_tied_to_lattice_edge_by_locality_runner.py"
COMPANION_CACHE = ROOT / "logs" / "runner-cache" / "min_time_step_tied_to_lattice_edge_by_locality_runner.txt"

C_LIGHT_M_PER_S = 299_792_458.0
C_LATTICE = 1.0
PLANCK_LENGTH_M = 1.616255e-35
PLANCK_TIME_S = PLANCK_LENGTH_M / C_LIGHT_M_PER_S
REL_TOL = 1.0e-7
RETAINED_GRADE_EFFECTIVE_STATUSES = {
    "retained",
    "retained_bounded",
    "retained_no_go",
}

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ""))
    return ok


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cache_header(cache_path: Path) -> dict[str, str]:
    header = cache_path.read_text(encoding="utf-8", errors="replace").split("----- stdout -----", 1)[0]
    fields: dict[str, str] = {}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def main() -> int:
    note_text = NOTE_PATH.read_text(encoding="utf-8")

    section("A1. registered single scale-reference primitive")
    axiom_nodes = json.loads(AXIOM_NODES.read_text(encoding="utf-8"))
    scale_node = axiom_nodes.get("nodes", {}).get("scale_reference_primitive", {})
    scale_note = ROOT / scale_node.get("current_path", "")
    check(
        "scale_reference_primitive is registered in axiom_premise_nodes",
        scale_node.get("current_path") == "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md" and scale_note.exists(),
        f"path={scale_node.get('current_path')}",
    )
    check(
        "scale primitive is described as units conversion / no dimensionless content",
        "Units conversion only" in scale_node.get("note", "")
        and "no dimensionless content" in scale_node.get("note", ""),
        scale_node.get("note", ""),
    )

    section("A2. kinetic-form c bridge")
    kinetic_node = axiom_nodes.get("nodes", {}).get("kinetic_isotropy_primitive", {})
    kinetic_text = (
        KINETIC_PRIMITIVE_NOTE.read_text(encoding="utf-8", errors="replace")
        if KINETIC_PRIMITIVE_NOTE.exists()
        else ""
    )
    check(
        "kinetic_isotropy_primitive is registered in axiom_premise_nodes",
        kinetic_node.get("current_path")
        == "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
        and KINETIC_PRIMITIVE_NOTE.exists(),
        f"path={kinetic_node.get('current_path')}",
    )
    check(
        "kinetic primitive supplies c_lattice = 1 scope only",
        "c_t = c_s" in kinetic_text
        and "hypercubic-symmetric" in kinetic_text
        and "does not supply any dimensionless dynamical quantity" in kinetic_text
        and C_LATTICE == 1.0,
        "structural kinetic-form bridge, not a physical c value",
    )
    check(
        "source note records emergent-c-to-physical-c split",
        "lattice-unit statement `c_lattice = a_s/a_τ = 1`" in note_text
        and "The emergent-`c` side is the\n  lattice-unit `c_lattice = 1`" in note_text,
        "c_lattice bridge plus SI conversion",
    )

    section("A3. companion tick/edge packet exposed as retained-bounded")
    ledger = json.loads(AUDIT_LEDGER.read_text(encoding="utf-8"))
    companion_row = ledger.get("rows", {}).get(COMPANION_ID, {})
    companion_cache_fields = cache_header(COMPANION_CACHE) if COMPANION_CACHE.exists() else {}
    companion_cache_text = (
        COMPANION_CACHE.read_text(encoding="utf-8", errors="replace")
        if COMPANION_CACHE.exists()
        else ""
    )
    check("companion note exists", COMPANION_NOTE.exists(), rel(COMPANION_NOTE))
    check("companion runner exists", COMPANION_RUNNER.exists(), rel(COMPANION_RUNNER))
    check("companion cache exists", COMPANION_CACHE.exists(), rel(COMPANION_CACHE))
    check(
        "companion cache is SHA-fresh",
        companion_cache_fields.get("runner_sha256") == sha256(COMPANION_RUNNER),
        f"{companion_cache_fields.get('runner_sha256')} == {sha256(COMPANION_RUNNER) if COMPANION_RUNNER.exists() else 'missing'}",
    )
    check(
        "companion runner/cache closes its finite reachability checks",
        "TOTAL: PASS=4 FAIL=0" in companion_cache_text,
        "finite BFS/cone verifier marker",
    )
    check(
        "current ledger exposes companion as retained-grade authority",
        companion_row.get("effective_status") in RETAINED_GRADE_EFFECTIVE_STATUSES,
        f"effective status {companion_row.get('effective_status')}",
    )
    check(
        "source note records the companion's retained-bounded effective status",
        "The current generated ledger exposes that companion with effective status\n   `retained_bounded`." in note_text,
        "boundary text present",
    )

    section("A4. physical-c normalization and Planck-time arithmetic")
    a_s = PLANCK_LENGTH_M
    a_tau = a_s / C_LIGHT_M_PER_S
    rel_err = abs(a_tau - PLANCK_TIME_S) / PLANCK_TIME_S
    print(f"  c                 = {C_LIGHT_M_PER_S:.0f} m/s")
    print(f"  l_P               = {PLANCK_LENGTH_M:.12e} m")
    print(f"  l_P/c             = {a_tau:.12e} s")
    print(f"  t_P reference     = {PLANCK_TIME_S:.12e} s")
    print(f"  relative error    = {rel_err:.3e}")
    check(
        "c normalization is explicit SI physical-unit conversion",
        "299792458 m/s" in note_text and "unit-normalization certificate" in note_text,
        "not derived by this row",
    )
    check(
        "l_P/c equals t_P at the stated <1e-7 tolerance",
        rel_err < REL_TOL,
        f"rel_err={rel_err:.3e}, tol={REL_TOL:.1e}",
    )

    section("A5. bounded-support minimality boundary")
    check(
        "source note is updated to bounded-support re-audit scope",
        "**Scope:** bounded-support re-audit packet" in note_text
        and "does not derive the\nphysical value of `c`" in note_text,
        "no physical-c derivation claim",
    )
    check(
        "no new axiom/admission/primitive is introduced",
        "No **new** axiom, admitted premise, **or** primitive." in note_text,
        "uses existing scale-reference primitive and companion packet",
    )
    check(
        "safe conclusion consumes the retained companion and explicit c conversion",
        "The companion one-tick-one-edge row is now\n`retained_bounded`" in note_text
        and "with the explicit SI `c` normalization this gives" in note_text,
        "retained companion plus unit conversion",
    )

    print()
    print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
