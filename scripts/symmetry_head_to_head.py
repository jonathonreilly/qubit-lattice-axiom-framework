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

RETAINED_GRADE = {"retained", "retained_bounded", "retained_no_go"}

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


def ledger_rows() -> dict:
    return json.loads(LEDGER_PATH.read_text(encoding="utf-8"))["rows"]


def main() -> int:
    print("=" * 96)
    print("SYMMETRY HEAD-TO-HEAD N=80 NARROW VERIFIER")
    print("=" * 96)
    print("Scope: one shared N=80 bounded comparison only.")
    print("Not scope: N=100/N=120 range ranking or asymptotic lane theorem.")
    print()

    rows = ledger_rows()
    passes: list[bool] = []

    for claim_id in (
        "mirror_chokepoint_boundary_fit_note",
        "higher_symmetry_joint_validation_note",
    ):
        row = rows[claim_id]
        passes.append(
            check(
                f"{claim_id} retained-grade dependency",
                row.get("effective_status") in RETAINED_GRADE,
                f"effective_status={row.get('effective_status')}",
            )
        )

    hsjv_scope = rows["higher_symmetry_joint_validation_note"].get("claim_scope") or ""
    passes.append(
        check(
            "Z2 x Z2 source scope includes sparse N=80",
            "N=25,40,60,80" in hsjv_scope and "no N=120" in hsjv_scope,
            hsjv_scope,
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
