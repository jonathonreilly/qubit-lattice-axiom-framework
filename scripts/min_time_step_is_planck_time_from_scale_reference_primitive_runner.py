#!/usr/bin/env python3
"""Boundary verifier for the Planck-time minimum-step packet.

This runner does not claim to derive physical time from the update tick.  It
checks the source packet needed for re-audit:

* the registered scale-reference primitive exists;
* the registered kinetic-isotropy primitive supplies only the lattice-unit
  c_lattice = 1 bridge;
* the one-tick-one-edge companion packet and cache are present, and its current
  ledger status is read from the tracked ledger shard and matched by the note,
  so the tick/edge tie is used as a supplied premise rather than silently
  assumed to be an established bridge;
* the physical-c normalization used by this row is explicit; and
* with those supplied inputs, l_P / c equals t_P at the note's stated
  tolerance.
"""

from __future__ import annotations

import hashlib
import json
from math import sqrt
from pathlib import Path

AUDIT_TIMEOUT_SEC = 120
# Mutable repository authorities and companion evidence consumed below.
AUDIT_INPUT_PATHS = (
    'docs/MIN_TIME_STEP_IS_THE_PLANCK_TIME_FROM_THE_SINGLE_SCALE_REFERENCE_PRIMITIVE_NARROW_THEOREM_NOTE_2026-06-08.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md',
    'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md',
    'docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md',
    'docs/audit/data/skill_axiom_baseline_manifest.json',
    'docs/audit/data/axiom_premise_nodes.json',
    'docs/MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md',
    'scripts/min_time_step_tied_to_lattice_edge_by_locality_runner.py',
    'logs/runner-cache/min_time_step_tied_to_lattice_edge_by_locality_runner.txt',
    'docs/audit/data/ledger/mi/min_time_step_tied_to_the_lattice_edge_by_causal_locality_ratio_derived_scale_is_the_clock_rate_no_go_narrow_theorem_note_2026-06-08.json',
    'docs/audit/data/ledger/po/post_record_clock_rate_interface_2026-06-06.json',
)


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "MIN_TIME_STEP_IS_THE_PLANCK_TIME_FROM_THE_SINGLE_SCALE_REFERENCE_PRIMITIVE_NARROW_THEOREM_NOTE_2026-06-08.md"
AXIOM_NODES = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
LEDGER_SHARDS = ROOT / "docs" / "audit" / "data" / "ledger"
KINETIC_PRIMITIVE_NOTE = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"

COMPANION_ID = "min_time_step_tied_to_the_lattice_edge_by_causal_locality_ratio_derived_scale_is_the_clock_rate_no_go_narrow_theorem_note_2026-06-08"
COMPANION_NOTE = ROOT / "docs" / "MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md"
COMPANION_RUNNER = ROOT / "scripts" / "min_time_step_tied_to_lattice_edge_by_locality_runner.py"
COMPANION_CACHE = ROOT / "logs" / "runner-cache" / "min_time_step_tied_to_lattice_edge_by_locality_runner.txt"
CLOCK_RATE_NO_GO_ID = "post_record_clock_rate_interface_2026-06-06"

C_LIGHT_M_PER_S = 299_792_458.0
C_LATTICE = 1.0
PLANCK_LENGTH_M = 1.616255e-35
# Independent rounded numerical fixtures, used only for an arithmetic consistency diagnostic.
HBAR_J_S = 1.054571817e-34
G_M3_KG_S2 = 6.67430e-11
PLANCK_TIME_S = sqrt(HBAR_J_S * G_M3_KG_S2 / C_LIGHT_M_PER_S ** 5)
DISPLAY_PLANCK_TIME_S = 5.3912464e-44
REL_TOL = 1.0e-7

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


def ledger_row(claim_id: str) -> dict:
    """Read one row from the git-tracked ledger shard (source of truth)."""
    shard = LEDGER_SHARDS / claim_id[:2] / f"{claim_id}.json"
    if not shard.exists():
        return {}
    return json.loads(shard.read_text(encoding="utf-8"))


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

    section("A3. companion tick/edge packet and its current ledger status")
    companion_row = ledger_row(COMPANION_ID)
    companion_type = companion_row.get("claim_type")
    companion_status = companion_row.get("effective_status")
    print(f"  companion row: claim_type={companion_type}, effective_status={companion_status}")
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
        "companion cache matches its self-contained runner SHA and successful exit",
        companion_cache_fields.get("runner_sha256") == sha256(COMPANION_RUNNER)
        and companion_cache_fields.get("status") == "ok"
        and companion_cache_fields.get("exit_code") == "0",
        f"{companion_cache_fields.get('runner_sha256')} == {sha256(COMPANION_RUNNER) if COMPANION_RUNNER.exists() else 'missing'}",
    )
    check(
        "companion runner/cache closes its finite reachability checks",
        "TOTAL: PASS=4 FAIL=0" in companion_cache_text,
        "finite BFS/cone verifier marker",
    )
    check(
        "companion row is present in the tracked ledger shard",
        bool(companion_row) and companion_type is not None and companion_status is not None,
        f"{COMPANION_ID[:2]}/{COMPANION_ID}.json",
    )
    check(
        "source note states the companion's current claim type and effective status",
        f"That companion row is an `{companion_type}` (current effective status `{companion_status}`);" in note_text,
        f"{companion_type} / {companion_status}",
    )
    check(
        "source note states the Planck-time identification conditionally on the supplied tie",
        "Then, conditional on the tie, the minimum time step is the Planck time" in note_text
        and "this step is\n   a supplied premise, not a derived bridge" in note_text,
        "tick/edge tie used as a supplied premise",
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
        "rounded l_P/c fixture agrees with independent sqrt(hbar G/c^5) fixture within <1e-7",
        rel_err < REL_TOL,
        f"rel_err={rel_err:.3e}, tol={REL_TOL:.1e}",
    )

    check(
        "source note displays the arithmetic fixture at its stated tolerance",
        "5.3912464×10^-44 s" in note_text
        and abs(DISPLAY_PLANCK_TIME_S - a_tau) / a_tau < REL_TOL,
        "rounded numerical consistency only; no empirical precision claim",
    )

    section("A5. bounded-support minimality boundary")
    check(
        "source note is updated to bounded-support re-audit scope",
        "**Scope:** bounded-support re-audit packet" in note_text
        and "does not derive the\nphysical value of `c`" in note_text,
        "no physical-c derivation claim",
    )
    check(
        "no new axiom/primitive is introduced",
        "No **new** axiom or primitive." in note_text,
        "uses existing scale-reference primitive and companion packet",
    )
    check(
        "safe conclusion is conditional on the open tick/edge gate plus explicit c conversion",
        f"The companion one-tick-one-edge row is an\n`{companion_type}` (`{companion_status}`), so `a_τ = a_s/c` holds only when that tie is\nsupplied" in note_text
        and "with the explicit SI `c` normalization this gives" in note_text,
        "supplied tie plus unit conversion",
    )
    clock_row = ledger_row(CLOCK_RATE_NO_GO_ID)
    check(
        "source note states the clock-rate no-go row's current claim type and status",
        bool(clock_row)
        and f"a `{clock_row.get('claim_type')}` row, currently `{clock_row.get('effective_status')}`" in note_text,
        f"{clock_row.get('claim_type')} / {clock_row.get('effective_status')}",
    )

    print()
    print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
