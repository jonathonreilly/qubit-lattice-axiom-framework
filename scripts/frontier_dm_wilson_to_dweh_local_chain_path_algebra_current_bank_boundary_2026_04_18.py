#!/usr/bin/env python3
"""Conditional supplied-input or documentary diagnostics.
No unique physical target, semantic exhaustion or absence theorem follows
from microscopic-selector text or the Wilson keyword inventory.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ('docs/DM_WILSON_TO_DWEH_LOCAL_CHAIN_PATH_ALGEBRA_CURRENT_BANK_BOUNDARY_NOTE_2026-04-18.md',)

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PASS_COUNT = 0
FAIL_COUNT = 0
BOUNDARY_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def boundary(name: str, detail: str = "") -> None:
    global BOUNDARY_COUNT
    BOUNDARY_COUNT += 1
    msg = f"  [BOUNDARY] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)


def read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


KNOWN_NONCLOSING_PATH_HITS = {
    "docs/DM_LEPTOGENESIS_TRANSPORT_STATUS_NOTE_2026-04-16.md",
    "scripts/frontier_perron_frobenius_step2_nilpotent_chain_helper_layer_2026_04_19.py",
}


def is_excluded_review_stack(rel: str) -> bool:
    explicit = {
        "docs/DM_PF_COMPRESSED_ROUTE_ATTACK_PLAN_NOTE_2026-04-18.md",
        "scripts/DM_EFFECTIVE_PARENT_one_clock_transfer_boundary_2026_04_18.py",
    }
    prefixes = (
        "docs/DM_EFFECTIVE_PARENT_",
        "docs/DM_WILSON_TO_DWEH_",
        "docs/DM_WILSON_DIRECT_DESCENDANT_",
        "docs/DM_WILSON_PARENT_CORRECTNESS_AUDIT_",
        "scripts/DM_EFFECTIVE_PARENT_",
        "scripts/frontier_dm_wilson_to_dweh_",
        "scripts/frontier_dm_wilson_direct_descendant_",
        "scripts/frontier_dm_wilson_parent_correctness_audit_",
        "scripts/DM_WILSON_DIRECT_DESCENDANT_",
    )
    return rel in explicit or rel.startswith(prefixes)


def files_with_all(tokens: list[str]) -> list[str]:
    hits: list[str] = []
    for folder, suffix in (("docs", "*.md"), ("scripts", "*.py")):
        for path in sorted((ROOT / folder).glob(suffix)):
            rel = str(path.relative_to(ROOT))
            if is_excluded_review_stack(rel):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            if all(token in text for token in tokens):
                hits.append(rel)
    return hits


def historical_inventory() -> int:
    print("=" * 88)
    print("DM WILSON-TO-dW_e^H LOCAL CHAIN PATH-ALGEBRA CURRENT-BANK BOUNDARY")
    print("=" * 88)

    generic_boundary = read(
        "docs/DM_WILSON_TO_DWEH_HERMITIAN_SOURCE_FAMILY_CURRENT_BANK_BOUNDARY_NOTE_2026-04-18.md"
    )
    chain_target = read("docs/DM_WILSON_TO_DWEH_LOCAL_CHAIN_PATH_ALGEBRA_TARGET_NOTE_2026-04-18.md")
    minimal_cert = read("docs/DM_WILSON_TO_DWEH_LOCAL_PATH_ALGEBRA_MINIMAL_CERTIFICATE_NOTE_2026-04-18.md")

    print("\n" + "=" * 88)
    print("PART 1: GENERIC DOCUMENTARY INPUT DOES NOT PROVE NONREALIZATION")
    print("=" * 88)
    print("UNSCORED SCOPE: supplied reconstruction/documentary context; no unique-target or absence theorem follows.")
    print("UNSCORED SCOPE: supplied reconstruction/documentary context; no unique-target or absence theorem follows.")

    print("\n" + "=" * 88)
    print("PART 2: THE LOCAL PATH ALGEBRA WOULD AUTOMATICALLY INDUCE THAT GENERIC ROUTE")
    print("=" * 88)
    check(
        "The local chain target note says the Hermitian shadow of Phi_chain gives a canonical 9-channel Wilson Hermitian source family",
        "canonical Wilson Hermitian source family" in chain_target
        and "spanning a copy of `Herm(3)`" in chain_target,
    )
    check(
        "The minimal-certificate note says the whole structured route is equivalent to Phi_chain plus the descended identity into dW_e^H",
        "exactly one minimal local" in minimal_cert
        and "`dW_W o Phi_chain = dW_e^H`" in minimal_cert,
    )

    print("\n" + "=" * 88)
    print("PART 3: OPTIONAL HISTORICAL KEYWORD INVENTORY")
    print("=" * 88)
    local_hits = files_with_all(["Phi_chain", "dW_e^H"])
    path_hits = files_with_all(["path-algebra", "dW_e^H"])
    unclassified_path_hits = [hit for hit in path_hits if hit not in KNOWN_NONCLOSING_PATH_HITS]
    check(
        "Historical keyword inventory has no Phi_chain/dW_e^H hits outside exclusions",
        len(local_hits) == 0,
        f"hits={local_hits}",
    )
    check(
        "Historical path-algebra keyword hits match the supplied allowlist",
        len(unclassified_path_hits) == 0,
        f"classified_nonclosing={len(path_hits) - len(unclassified_path_hits)}, unclassified={unclassified_path_hits}",
    )
    if path_hits:
        boundary(
            "Current main contains classified path-algebra/dW_e^H mentions, but they are status/helper artifacts rather than the local Wilson certificate",
            f"classified_nonclosing={len(path_hits) - len(unclassified_path_hits)}",
        )

    print("\n" + "=" * 88)
    print("PART 4: BOTTOM LINE")
    print("=" * 88)
    print("UNSCORED SCOPE: supplied reconstruction/documentary context; no unique-target or absence theorem follows.")
    print("UNSCORED SCOPE: supplied reconstruction/documentary context; no unique-target or absence theorem follows.")

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} BOUNDARY={BOUNDARY_COUNT} HARD_ISSUES={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


def main() -> int:
    if "--historical-inventory" in sys.argv[1:]:
        return historical_inventory()
    print("DOCUMENTARY DEFAULT: no scientific or mathematical assertions are scored.")
    print("The generic Wilson inventory proves neither absence nor necessity of a local path-algebra certificate.")
    print("Optional --historical-inventory preserves the old keyword/allowlist tests; they are not semantic exhaustion.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
