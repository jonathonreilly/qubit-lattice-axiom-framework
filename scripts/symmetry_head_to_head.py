#!/usr/bin/env python3
"""Narrow symmetry head-to-head verifier.

This runner checks only the shared N=80 comparison between:
  - mirror dense boundary card values from MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE
  - Z2 x Z2 sparse joint-validation values from HIGHER_SYMMETRY_JOINT_VALIDATION_NOTE

It deliberately excludes N=100/N=120 range language because the current
Z2 x Z2 joint-validation authority binds only the sparse N=25,40,60,80 cache.
"""

from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
LEDGER_PATH = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
MIRROR_NOTE = REPO_ROOT / "docs" / "MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md"
HSJV_NOTE = REPO_ROOT / "docs" / "HIGHER_SYMMETRY_JOINT_VALIDATION_NOTE.md"

RETAINED_GRADE = {"retained", "retained_bounded", "retained_no_go"}
MIRROR_PREMISE_QUOTES = (
    "This note freezes one named finite parameter card from the mirror chokepoint runner. The claim is intentionally bounded: the card is Born-clean, gravity-positive, and decohering for `N = 40, 60, 80, 100`, has a gravity wall at `N = 120`, and has a weak descriptive fit on the four selected fit rows.",
    "The note makes no claim beyond this finite replay and post-retention descriptive fit.",
)
HSJV_PREMISE_QUOTES = (
    "The binding scope of this note is exactly the sparse N=25,40,60,80 `Z₂ × Z₂` row from the joint-validator (see Scope narrowing section above).",
    "The dense N=80/100/120 row is **out of binding scope** until the missing dense joint-validation log + registered joint-validator cache is attached, so its cache is **not inlined** here per the audit verdict",
)

MIRROR_N80 = {
    "N": 80,
    "lane": "mirror dense boundary card",
    "dtv": 0.4291,
    "purity": 0.8182,
    "gravity": 3.0551,
    "born_bound": 1e-10,
    "k0": 0.0,
}

Z2Z2_N80 = {
    "N": 80,
    "lane": "Z2 x Z2 sparse joint-validation card",
    "dtv": 0.540,
    "purity": 0.782,
    "gravity": 2.218,
    "born": 1.80e-15,
    "k0": 0.0,
}


def check(label: str, condition: bool, detail: str) -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {label}: {detail}")
    return condition


def _norm(text: str) -> str:
    return " ".join(text.split())


def ledger_rows() -> dict:
    return json.loads(LEDGER_PATH.read_text(encoding="utf-8"))["rows"]


def gate_dependency_note(claim_id: str, rows: dict, note_path: Path, quotes: tuple[str, ...]) -> list[bool]:
    row = rows.get(claim_id)
    results = [
        check(f"{claim_id} row exists in audit ledger", row is not None, "row existence gate")
    ]
    row = row or {}
    print(
        "  [info] "
        f"{claim_id} live claim_scope={row.get('claim_scope')!r} "
        f"effective_status={row.get('effective_status')!r} "
        "(audit-lane-owned; not gated)"
    )
    note_text = _norm(note_path.read_text(encoding="utf-8")) if note_path.is_file() else ""
    results.append(check(f"{claim_id} dependency note exists", note_path.is_file(), str(note_path.relative_to(REPO_ROOT))))
    for quote in quotes:
        results.append(
            check(
                f"{claim_id} note states premise verbatim",
                _norm(quote) in note_text,
                f"len={len(quote)}",
            )
        )
    return results


def main() -> int:
    print("=" * 96)
    print("SYMMETRY HEAD-TO-HEAD N=80 NARROW VERIFIER")
    print("=" * 96)
    print("Scope: one shared N=80 bounded comparison only.")
    print("Not scope: N=100/N=120 range ranking or asymptotic lane theorem.")
    print()

    rows = ledger_rows()
    passes: list[bool] = []

    passes.extend(
        gate_dependency_note(
            "mirror_chokepoint_boundary_fit_note",
            rows,
            MIRROR_NOTE,
            MIRROR_PREMISE_QUOTES,
        )
    )
    passes.extend(
        gate_dependency_note(
            "higher_symmetry_joint_validation_note",
            rows,
            HSJV_NOTE,
            HSJV_PREMISE_QUOTES,
        )
    )

    passes.append(
        check(
            "shared-row scope is N=80 only",
            MIRROR_N80["N"] == Z2Z2_N80["N"] == 80,
            f"mirror_N={MIRROR_N80['N']}, z2z2_N={Z2Z2_N80['N']}",
        )
    )
    passes.append(
        check(
            "mirror has larger displayed gravity at N=80",
            MIRROR_N80["gravity"] > Z2Z2_N80["gravity"] > 0,
            f"{MIRROR_N80['gravity']:.4f} > {Z2Z2_N80['gravity']:.4f} > 0",
        )
    )
    passes.append(
        check(
            "Z2 x Z2 has lower displayed purity at N=80",
            Z2Z2_N80["purity"] < MIRROR_N80["purity"],
            f"{Z2Z2_N80['purity']:.4f} < {MIRROR_N80['purity']:.4f}",
        )
    )
    passes.append(
        check(
            "both rows are Born-clean",
            MIRROR_N80["born_bound"] <= 1e-10 and Z2Z2_N80["born"] < 1e-10,
            f"mirror<{MIRROR_N80['born_bound']:.1e}, z2z2={Z2Z2_N80['born']:.2e}",
        )
    )
    passes.append(
        check(
            "both k=0 controls are zero",
            MIRROR_N80["k0"] == 0.0 and Z2Z2_N80["k0"] == 0.0,
            f"mirror={MIRROR_N80['k0']:.2e}, z2z2={Z2Z2_N80['k0']:.2e}",
        )
    )

    print()
    print("N=80 comparison table")
    print(f"{'lane':>38s} {'d_TV':>8s} {'purity':>8s} {'gravity':>10s} {'Born':>11s} {'k=0':>8s}")
    print("-" * 96)
    mirror_born = f"<={MIRROR_N80['born_bound']:.1e}"
    print(
        f"{MIRROR_N80['lane']:>38s} {MIRROR_N80['dtv']:8.4f} "
        f"{MIRROR_N80['purity']:8.4f} {MIRROR_N80['gravity']:+10.4f} "
        f"{mirror_born:>11s} {MIRROR_N80['k0']:8.2e}"
    )
    print(
        f"{Z2Z2_N80['lane']:>38s} {Z2Z2_N80['dtv']:8.4f} "
        f"{Z2Z2_N80['purity']:8.4f} {Z2Z2_N80['gravity']:+10.4f} "
        f"{Z2Z2_N80['born']:.2e} {Z2Z2_N80['k0']:8.2e}"
    )

    n_pass = sum(1 for item in passes if item)
    n_total = len(passes)
    print()
    print(f"PASS={n_pass} FAIL={n_total - n_pass}")
    print("Result: bounded one-row comparison only; no N=100/N=120 retained-range claim.")
    return 0 if n_pass == n_total else 1


if __name__ == "__main__":
    raise SystemExit(main())
