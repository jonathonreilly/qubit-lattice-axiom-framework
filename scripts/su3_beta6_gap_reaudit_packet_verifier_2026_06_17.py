#!/usr/bin/env python3
"""Restricted-packet verifier for the SU(3) beta=6 conditional gap row.

This runner packages the source-side support now available for
`SU3_BETA6_GAP_BULK_CRITICALITY_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-09.md`.
It checks:

1. the parent beta=6 conditional reduction and its guardrails;
2. the explicit-constant analyticity floor for the lower end of the premise;
3. the Wilson transfer-kernel / reflection-positivity support notes; and
4. SHA-fresh cached outputs for the relevant runners.

It does not audit the row, promote status, retag the ledger, or claim an
unconditional beta=6 gap theorem.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def sha256_file(rel: str) -> str:
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status} {name}{suffix}")


def cache_meta(cache_text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in cache_text.splitlines():
        if ": " not in line or line.startswith("-----"):
            continue
        key, value = line.split(": ", 1)
        if key in {"runner", "runner_sha256", "exit_code", "status"}:
            out[key] = value.strip()
    return out


def has(text: str, needle: str) -> bool:
    compact_text = " ".join(text.split())
    compact_needle = " ".join(needle.split())
    return (
        needle in text
        or compact_needle in compact_text
        or compact_needle.lower() in compact_text.lower()
    )


PARENT_NOTE = "docs/SU3_BETA6_GAP_BULK_CRITICALITY_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-09.md"
FLOOR_NOTE = "docs/SU3_BULK_CRITICALITY_PREMISE_RIGOROUS_FLOOR_NOTE_2026-06-09.md"
WILSON_TRANSFER_NOTE = "docs/WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md"
RP_BRIDGE_NOTE = "docs/AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
RP_SIGN_REPAIR_NOTE = "docs/RP_WILSON_TEMPORAL_GAUGE_BRIDGE_SIGN_AND_POSITIVITY_REPAIR_NOTE_2026-06-06.md"

PARENT_RUNNER = "scripts/frontier_su3_beta6_gap_bulk_criticality_reduction_2026_06_09.py"
FLOOR_RUNNER = "scripts/frontier_su3_bulk_criticality_rigorous_floor_2026_06_09.py"
WILSON_TRANSFER_RUNNER = "scripts/wilson_su3_gauge_transfer_kernel_positivity_2026-05-30.py"
RP_BRIDGE_RUNNER = "scripts/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.py"
RP_SIGN_REPAIR_RUNNER = "scripts/frontier_rp_wilson_temporal_gauge_sign_and_positivity_repair_2026_06_06.py"

CACHES = {
    PARENT_RUNNER: "logs/runner-cache/frontier_su3_beta6_gap_bulk_criticality_reduction_2026_06_09.txt",
    FLOOR_RUNNER: "logs/runner-cache/frontier_su3_bulk_criticality_rigorous_floor_2026_06_09.txt",
    WILSON_TRANSFER_RUNNER: "logs/runner-cache/wilson_su3_gauge_transfer_kernel_positivity_2026-05-30.txt",
    RP_BRIDGE_RUNNER: "logs/runner-cache/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.txt",
    RP_SIGN_REPAIR_RUNNER: "logs/runner-cache/frontier_rp_wilson_temporal_gauge_sign_and_positivity_repair_2026_06_06.txt",
}


def check_cache(runner: str, needles: list[str]) -> None:
    cache = CACHES[runner]
    check(f"{runner} exists", (ROOT / runner).is_file())
    check(f"{cache} exists", (ROOT / cache).is_file())
    cache_text = read(cache)
    meta = cache_meta(cache_text)
    check(f"{cache} records runner path", meta.get("runner") == runner, f"runner={meta.get('runner')}")
    check(f"{cache} exits zero", meta.get("exit_code") == "0", f"exit_code={meta.get('exit_code')}")
    check(f"{cache} status ok", meta.get("status") == "ok", f"status={meta.get('status')}")
    live_sha = sha256_file(runner)
    check(
        f"{cache} sha matches source",
        meta.get("runner_sha256") == live_sha,
        f"cache={meta.get('runner_sha256')}, live={live_sha}",
    )
    for needle in needles:
        check(f"{cache} contains {needle!r}", has(cache_text, needle))


def main() -> int:
    print("SU(3) beta=6 conditional gap restricted packet verifier")
    print("=" * 76)

    parent = read(PARENT_NOTE)
    floor = read(FLOOR_NOTE)
    wilson = read(WILSON_TRANSFER_NOTE)
    rp_bridge = read(RP_BRIDGE_NOTE)
    rp_sign = read(RP_SIGN_REPAIR_NOTE)

    for rel in [
        PARENT_NOTE,
        FLOOR_NOTE,
        WILSON_TRANSFER_NOTE,
        RP_BRIDGE_NOTE,
        RP_SIGN_REPAIR_NOTE,
    ]:
        check(f"{rel} exists", (ROOT / rel).is_file())

    parent_needles = [
        "open_gate / conditional fixed-lattice reduction",
        "independent audit lane only",
        "No second-order bulk critical point occurs",
        "This is a reduction theorem, not an unconditional mass-gap theorem.",
        "Not an unconditional `beta=6` gap.",
        "2026-06-15 audit-unlock residual certificate",
        "2026-06-16 transfer-kernel dependency-edge repair",
        "no-second-order-bulk-critical-point premise",
        "does not claim a beta=6 gap",
        "does not retag any ledger row",
        "WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md",
        "AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
        "su3_beta6_gap_reaudit_packet_verifier_2026_06_17.py",
        "does not prove the missing no-second-order-bulk-criticality theorem",
    ]
    for needle in parent_needles:
        check(f"parent records {needle!r}", has(parent, needle))

    check(
        "parent keeps fixed-lattice scope separate from continuum physics",
        has(parent, "fixed-spacing lattice-units `0++` gap at `beta=6`")
        and has(parent, "physical-units or continuum mass-gap theorem"),
    )
    check(
        "parent identifies the exact remaining blocker",
        has(parent, "framework-native theorem ruling out a")
        and has(parent, "second-order bulk critical point")
        and has(parent, "`beta = 6`"),
    )

    floor_needles = [
        "explicit-constant convergence floor",
        "0.0047",
        "0.078%",
        "remaining",
        "Balaban-class RG-constructive work",
        "does not promote, demote, or set the audit status",
    ]
    for needle in floor_needles:
        check(f"rigorous floor records {needle!r}", has(floor, needle))
    check(
        "floor clears only the lower edge of the premise interval",
        has(floor, "premise interval") and has(floor, "(0, 6]") and has(floor, "0.0047, 6]"),
    )

    wilson_needles = [
        "gauge-kernel positivity half",
        "positive semidefinite",
        "reflection-positivity theorem for the full interacting",
        "does NOT close the full interacting reflection positivity",
        "gauge kernel alone",
    ]
    for needle in wilson_needles:
        check(f"Wilson transfer note records {needle!r}", has(wilson, needle))

    rp_bridge_needles = [
        "Wilson Plaquette Temporal-Gauge Bridge",
        "does not set the target row's status",
        "does **not** mean a full interacting `SU(N)` proof",
        "bosonic half",
        "plane-kernel positivity",
    ]
    for needle in rp_bridge_needles:
        check(f"RP bridge records {needle!r}", has(rp_bridge, needle))

    rp_sign_needles = [
        "Sign Repair",
        "sign** of the weight",
        "antilinearity",
        "does not promote this note or change any audited claim scope",
        "full interacting `SU(N)` finite",
    ]
    for needle in rp_sign_needles:
        check(f"RP sign repair records {needle!r}", has(rp_sign, needle))

    cache_needles = {
        PARENT_RUNNER: [
            "TOTAL: PASS=10 FAIL=0",
            "SCOPE: conditional fixed-lattice reduction plus diagnostics only",
            "no-second-order-bulk-point premise remains open",
        ],
        FLOOR_RUNNER: [
            "SUMMARY: PASS=15 FAIL=0",
            "cleared 0.078% of the interval",
            "Balaban-class RG-constructive work -- open, not claimed",
        ],
        WILSON_TRANSFER_RUNNER: [
            "SCORECARD PASS=6 FAIL=0",
            "C4_wilson_transfer_kernel_gram_PSD",
        ],
        RP_BRIDGE_RUNNER: [
            "TOTAL: 16 PASS / 0 FAIL",
            "integrated three-factor RP Gram PSD",
        ],
        RP_SIGN_REPAIR_RUNNER: [
            "TOTAL: 17 PASS / 0 FAIL",
            "sign is load-bearing",
        ],
    }
    for runner, needles in cache_needles.items():
        check_cache(runner, needles)

    check(
        "restricted packet is non-promotional",
        has(parent, "not an audit verdict or status promotion")
        and has(floor, "does not promote, demote, or set the audit status")
        and has(rp_bridge, "does not set the target row's status")
        and has(rp_sign, "does not promote this note or change any audited claim scope"),
    )
    check(
        "remaining positive route is exactly the bulk-criticality theorem",
        "remaining `(beta0,6]` window" not in parent
        and has(parent, "second-order bulk critical point")
        and has(floor, "Balaban-class RG-constructive work"),
    )

    print("=" * 76)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        return 1
    print(
        "SU(3) beta=6 packet is source-side re-audit ready: the lower-edge "
        "analyticity floor and transfer/RP dependencies are cached, while the "
        "no-second-order-bulk-criticality theorem on the remaining window is "
        "still explicitly open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
