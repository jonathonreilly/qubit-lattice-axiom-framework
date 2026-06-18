#!/usr/bin/env python3
"""Restricted-packet verifier for the Koide records/objectivity conditional row.

This runner checks the source-side packet around
`KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md`.

It verifies that the algebraic selector calculation is cached and coherent,
that both selector inputs remain supplied rather than derived, and that the
supporting Koide/readout notes preserve the block-weight boundary. It does not
audit the row, promote status, add an admission, retag the ledger, or claim a
framework-native derivation of the equal-block metric or objectivity selector.
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


def has(text: str, needle: str) -> bool:
    compact_text = " ".join(text.split())
    compact_needle = " ".join(needle.split())
    return (
        needle in text
        or compact_needle in compact_text
        or compact_needle.lower() in compact_text.lower()
    )


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


PARENT_NOTE = "docs/KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md"
Q23_NOTE = "docs/KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md"
FROBENIUS_NO_GO_NOTE = "docs/KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md"
READOUT_DEMARCATION_NOTE = "docs/KOIDE_READOUT_LANE_DEMARCATION_NOTE_2026-05-30.md"
PRE_RECORD_NOTE = "docs/PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md"

PARENT_RUNNER = "scripts/frontier_koide_records_objectivity_conditional_2026_05_31.py"
Q23_RUNNER = "scripts/koide_q23_block_weight_frontier_2026_05_29.py"
KAPPA_RUNNER = "scripts/frontier_koide_kappa_block_total_frobenius_algebraic_narrow.py"
FROBENIUS_RUNNER = "scripts/frontier_koide_frobenius_isotype_split_uniqueness.py"
PRE_RECORD_RUNNER = "scripts/frontier_pre_record_reference_state_tracial_derivation.py"
CIRCULANT_RUNNER = "scripts/frontier_koide_circulant_q_two_thirds_algebraic_narrow.py"

CACHES = {
    PARENT_RUNNER: "logs/runner-cache/frontier_koide_records_objectivity_conditional_2026_05_31.txt",
    Q23_RUNNER: "logs/runner-cache/koide_q23_block_weight_frontier_2026_05_29.txt",
    KAPPA_RUNNER: "logs/runner-cache/frontier_koide_kappa_block_total_frobenius_algebraic_narrow.txt",
    FROBENIUS_RUNNER: "logs/runner-cache/frontier_koide_frobenius_isotype_split_uniqueness.txt",
    PRE_RECORD_RUNNER: "logs/runner-cache/frontier_pre_record_reference_state_tracial_derivation.txt",
    CIRCULANT_RUNNER: "logs/runner-cache/frontier_koide_circulant_q_two_thirds_algebraic_narrow.txt",
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
    print("Koide records/objectivity restricted packet verifier")
    print("=" * 76)

    parent = read(PARENT_NOTE)
    q23 = read(Q23_NOTE)
    frobenius = read(FROBENIUS_NO_GO_NOTE)
    readout = read(READOUT_DEMARCATION_NOTE)
    pre_record = read(PRE_RECORD_NOTE)

    for rel in [
        PARENT_NOTE,
        Q23_NOTE,
        FROBENIUS_NO_GO_NOTE,
        READOUT_DEMARCATION_NOTE,
        PRE_RECORD_NOTE,
    ]:
        check(f"{rel} exists", (ROOT / rel).is_file())

    parent_needles = [
        "open_gate / conditional-support certificate",
        "equal-block metric",
        "records/objectivity maximization",
        "does not select the singlet/doublet sector measure",
        "supplied equal-block (1,1) metric",
        "supplied records/objectivity maximization selector",
        "17/17 checks passed",
        "koide_records_objectivity_packet_verifier_2026_06_17.py",
        "does not derive either selector input",
    ]
    for needle in parent_needles:
        check(f"parent records {needle!r}", has(parent, needle))
    check("parent has no stale 13/13 count", "13/13" not in parent)

    q23_needles = [
        "equal-block rule gives `Q=2/3`",
        "dimension-weighted trace gives `Q=1`",
        "does not derive that rule",
        "open_gate localization",
    ]
    for needle in q23_needles:
        check(f"Q23 frontier records {needle!r}", has(q23, needle))

    frobenius_needles = [
        "do not force the Frobenius normalization",
        "Conditional Corollary Kept Out Of Scope",
        "does not claim",
        "any new axiom or audit verdict",
    ]
    for needle in frobenius_needles:
        check(f"Frobenius no-go records {needle!r}", has(frobenius, needle))

    readout_needles = [
        "the readout supplies the formula, not r=1/2",
        "readout itself supplies no rule",
        "dynamics/evidence lane",
        "does not rank them",
    ]
    for needle in readout_needles:
        check(f"readout demarcation records {needle!r}", has(readout, needle))

    pre_record_needles = [
        "unique tracial-state characterization",
        "pre-record identification",
        "demoted to a separate open admission",
        "not part of the audited claim",
    ]
    for needle in pre_record_needles:
        check(f"pre-record note records {needle!r}", has(pre_record, needle))

    cache_needles = {
        PARENT_RUNNER: [
            "17/17 checks passed",
            "THE HONEST RESULT: Q=2/3 is a CONDITIONAL, not a forced theorem.",
            "Both hypotheses (i)+(ii) remain explicit inputs",
        ],
        Q23_RUNNER: [
            "PASS=19 FAIL=0",
            "equal-block rule",
            "does not derive or approve that physical rule",
        ],
        KAPPA_RUNNER: [
            "PASS=67 FAIL=0",
            "No PDG observed values",
            "selection-principle authority",
        ],
        FROBENIUS_RUNNER: [
            "PASS=24 FAIL=0",
            "do not force the Frobenius normalization",
        ],
        PRE_RECORD_RUNNER: [
            "PASS=12 FAIL=0",
            "pre-record identification remains open",
        ],
        CIRCULANT_RUNNER: [
            "PASS=23 FAIL=0",
            "Open derivation gaps",
        ],
    }
    for runner, needles in cache_needles.items():
        check_cache(runner, needles)

    check(
        "packet leaves both selector inputs open",
        has(parent, "two selector inputs remain supplied")
        and has(q23, "physical selection of the weight")
        and has(frobenius, "do not force the Frobenius normalization")
        and has(readout, "the readout itself supplies no rule"),
    )
    check(
        "packet is non-promotional",
        has(parent, "no audit-status change")
        and has(q23, "does not set an audit verdict")
        and has(readout, "sets no audit outcome")
        and has(pre_record, "not part of the audited claim"),
    )

    print("=" * 76)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        return 1
    print(
        "Koide records/objectivity packet is source-side re-audit ready: "
        "the conditional algebra is cached, the stale 13/13 count is gone, "
        "and both selector inputs remain explicit open pins."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
