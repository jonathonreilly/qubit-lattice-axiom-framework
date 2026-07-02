#!/usr/bin/env python3
"""Scope-boundary repair checker for the Poisson/CHSH teleportation row.

The repair does not prove the native preparation/readout theorem. It verifies
that the row is framed as an open gate, that the old stale minimal-axiom link is
gone, and that the original bounded diagnostic still runs on the restricted
small surfaces.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "TELEPORTATION_RESOURCE_FROM_POISSON_NOTE.md"
ORIGINAL = ROOT / "scripts" / "frontier_teleportation_resource_from_poisson.py"
HELPER = ROOT / "scripts" / "frontier_bell_inequality.py"
RALA_NOTE = DOCS / "TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md"
HELPER_REQUIRED = (
    "def build_H1",
    "def build_H2_tensor",
    "def build_pair_hop_X",
    "def build_poisson",
    "def build_sublattice_Z",
    "def build_cell_taste_operator",
    "def taste_identity_check",
    "def chsh_horodecki",
    "def lattice_1d",
    "def lattice_2d",
    "def lattice_3d",
)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def has_phrase(text: str, phrase: str) -> bool:
    return " ".join(phrase.split()) in " ".join(text.split())


def main() -> int:
    print("Teleportation Poisson resource scope repair")
    print("=" * 72)

    note = NOTE.read_text(encoding="utf-8")

    print()
    print("A. Boundary wording")
    print("-" * 72)
    check("note declares open_gate type", "**Type:** open_gate" in note)
    check("note declares open_gate claim type", "**Claim type:** open_gate" in note)
    check("note has no source-side status authority", "Status authority" not in note)
    check(
        "note says this is not a deterministic-resource theorem",
        has_phrase(note, "not as a deterministic-resource theorem"),
    )
    check(
        "note preserves small-surface diagnostic value",
        has_phrase(note, "small-surface Poisson/CHSH calculation is still useful")
        and has_phrase(note, "high ideal state-teleportation fidelity"),
    )
    check(
        "note leaves native carrier derivation open",
        has_phrase(note, "not that the last taste bit has been derived as a native physical carrier")
        and has_phrase(note, "missing native preparation/readout theorem remains"),
    )
    check(
        "note does not claim matter or FTL teleportation",
        "does not claim matter teleportation" in note
        and "faster-than-light transport" in note,
    )

    print()
    print("B. Dependency hygiene")
    print("-" * 72)
    helper_source = HELPER.read_text(encoding="utf-8")
    rala_source = RALA_NOTE.read_text(encoding="utf-8")
    stale_axiom_pair = "A" + "1+A" + "2"
    stale_status_token = "retain" + "ed_bounded"
    check(
        "stale minimal axiom link removed",
        "MINIMAL_AXIOMS_2026-05-03.md" not in note
        and "MINIMAL_AXIOMS_2026-05-20.md" not in note
        and stale_axiom_pair not in note,
    )
    check(
        "current named framework baseline cited",
        "MINIMAL_AXIOMS_2026-06-04.md" in note
        and "Lattice, Quantum, and Record" in note,
    )
    check(
        "adjacent notes are source references, not status imports",
        "Ledger snapshot" not in note
        and "audited_clean" not in note
        and stale_status_token not in note,
    )
    check(
        "Poisson/CHSH helper source is linked in note",
        "Load-bearing helper source" in note
        and "scripts/frontier_bell_inequality.py" in note,
    )
    check(
        "Poisson/CHSH helper source is present and untruncated",
        len(helper_source.splitlines()) > 500
        and all(required in helper_source for required in HELPER_REQUIRED),
    )
    check(
        "retained-axis RALA source is cited and source-visible",
        "TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md" in note
        and "Retained-Axis Operator Algebra" in rala_source
        and "T8 (RALA teleportation closure)" in rala_source,
    )

    print()
    print("C. Original bounded diagnostic")
    print("-" * 72)
    result = subprocess.run(
        [
            sys.executable,
            str(ORIGINAL.relative_to(ROOT)),
            "--trials",
            "16",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    output = result.stdout
    check(
        "original runner exits cleanly",
        result.returncode == 0,
        f"returncode={result.returncode}",
    )
    check("original runner covers null control", "Case: 1d_null" in output)
    check("original runner covers 1d Poisson case", "Case: 1d_poisson_chsh" in output)
    check("original runner covers 2d Poisson case", "Case: 2d_poisson_chsh" in output)
    check(
        "original runner reports diagnostic-only postselection",
        "Postselected branches" in output and "diagnostics only" in output,
    )
    check(
        "original runner exposes helper source packet",
        "Source packet: scripts/frontier_bell_inequality.py" in output
        and "required_symbols=11 PASS" in output,
    )
    check(
        "original runner verifies last-taste carrier checks",
        "Last-taste carrier checks:" in output
        and "X=xi_last/logical-flip PASS" in output
        and "Z_last Pauli PASS" in output,
    )
    check(
        "original runner verifies retained-axis source guard",
        "Retained-axis source: docs/TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md" in output
        and "ledger=retained_bounded" in output,
    )
    check(
        "original runner reconciles null Bell-label tie",
        "traced Bell max-label tie: Phi+, Psi+" in output
        and "best fixed-env postselected branch: Bell overlap=0.500000 (" in output,
    )
    check(
        "original runner does not promote the result",
        "independent hardening before promotion" in output
        and "not by itself a teleportation resource derivation" in output,
    )

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: row is ready for re-audit as an open_gate bounded diagnostic.")
        return 0
    print("VERDICT: teleportation Poisson scope repair checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
