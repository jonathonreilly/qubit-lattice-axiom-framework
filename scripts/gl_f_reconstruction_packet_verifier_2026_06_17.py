#!/usr/bin/env python3
"""Restricted-packet verifier for the GL(F) Berezin/RP reconstruction row.

This runner checks the source-side packet around
`GL_F_FROM_BEREZIN_RP_RECONSTRUCTION_NARROW_THEOREM_NOTE_2026-06-10.md`.
It verifies that:

1. the parent GL(F) reconstruction note keeps the matter-functional/action
   surface as the only named residual;
2. the identification bridge decomposes the old opaque bridge into clauses
   and keeps clause I-4 undiscovered;
3. the substep-1 forcing/no-go/discriminator notes preserve the hard-core
   tie and the conditional role of GL(F); and
4. all relevant runner caches are SHA-fresh.

It does not audit the row, promote status, add an admission, retag the ledger,
or claim that the framework already supplies the matter functional.
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


PARENT_NOTE = "docs/GL_F_FROM_BEREZIN_RP_RECONSTRUCTION_NARROW_THEOREM_NOTE_2026-06-10.md"
BRIDGE_NOTE = "docs/GL_F_IDENTIFICATION_BRIDGE_DECOMPOSITION_NARROW_THEOREM_NOTE_2026-06-11.md"
FORCING_NOTE = "docs/STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md"
NO_GO_NOTE = "docs/STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md"
DISCRIMINATOR_NOTE = "docs/STAGGERED_DIRAC_SUBSTEP1_STATISTICS_GL_F_CONDITIONAL_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-06-10.md"

PARENT_RUNNER = "scripts/gl_f_berezin_rp_reconstruction_check_2026_06_10.py"
BRIDGE_RUNNER = "scripts/gl_f_identification_bridge_check_2026_06_11.py"
FORCING_RUNNER = "scripts/audit_companion_staggered_dirac_substep1_grassmann_forcing_bridge_2026_05_16.py"
NO_GO_RUNNER = "scripts/frontier_staggered_dirac_substep1_statistics_agnostic_no_forcing_discriminator.py"
DISCRIMINATOR_RUNNER = "scripts/staggered_dirac_substep1_statistics_selection_check_2026_06_10.py"

CACHES = {
    PARENT_RUNNER: "logs/runner-cache/gl_f_berezin_rp_reconstruction_check_2026_06_10.txt",
    BRIDGE_RUNNER: "logs/runner-cache/gl_f_identification_bridge_check_2026_06_11.txt",
    FORCING_RUNNER: "logs/runner-cache/audit_companion_staggered_dirac_substep1_grassmann_forcing_bridge_2026_05_16.txt",
    NO_GO_RUNNER: "logs/runner-cache/frontier_staggered_dirac_substep1_statistics_agnostic_no_forcing_discriminator.txt",
    DISCRIMINATOR_RUNNER: "logs/runner-cache/staggered_dirac_substep1_statistics_selection_check_2026_06_10.txt",
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
    print("GL(F) Berezin/RP reconstruction restricted packet verifier")
    print("=" * 76)

    parent = read(PARENT_NOTE)
    bridge = read(BRIDGE_NOTE)
    forcing = read(FORCING_NOTE)
    no_go = read(NO_GO_NOTE)
    discriminator = read(DISCRIMINATOR_NOTE)

    for rel in [
        PARENT_NOTE,
        BRIDGE_NOTE,
        FORCING_NOTE,
        NO_GO_NOTE,
        DISCRIMINATOR_NOTE,
    ]:
        check(f"{rel} exists", (ROOT / rel).is_file())

    parent_needles = [
        "conditional finite-block theorem",
        "matter-functional/action surface",
        "GL_F_IDENTIFICATION_BRIDGE_DECOMPOSITION_NARROW_THEOREM_NOTE_2026-06-11.md",
        "only the matter-functional/action-surface clause remains open",
        "This repair does not promote this row",
        "does not claim a statistics-forcing theorem from the baseline axioms alone",
        "gl_f_reconstruction_packet_verifier_2026_06_17.py",
        "does not derive the matter-functional/action-surface clause",
    ]
    for needle in parent_needles:
        check(f"parent records {needle!r}", has(parent, needle))

    bridge_needles = [
        "conditional-support certificate",
        "first three have exact finite support",
        "matter-functional clause",
        "source note does not discharge that clause",
        "TOTAL: PASS=39 FAIL=0",
        "matter-functional clause (I-4) is NOT discharged",
        "HARD-CORE ESCAPE",
        "Sets, promotes, or changes **no** row's effective status",
    ]
    for needle in bridge_needles:
        check(f"identification bridge records {needle!r}", has(bridge, needle))
    check("identification bridge has no stale PASS=36 expectation", "PASS=36" not in bridge)

    forcing_needles = [
        "two-candidate surface only",
        "NOT a statistics-forcing theorem",
        "hard-core-boson frame ties",
        "statistics selection remains an open input",
        "TOTAL: PASS=45, FAIL=0",
    ]
    for needle in forcing_needles:
        check(f"forcing bridge records {needle!r}", has(forcing, needle))

    no_go_needles = [
        "compatible, not forced",
        "hard-core-boson reading remains",
        "Conclusion (the no-go)",
        "does not do that registration",
    ]
    for needle in no_go_needles:
        check(f"statistics no-go records {needle!r}", has(no_go, needle))

    discriminator_needles = [
        "Conditional discriminator",
        "not supplied here",
        "retained no-go stands",
        "No unconditional statistics selection",
        "TOTAL: PASS=24 FAIL=0",
    ]
    for needle in discriminator_needles:
        check(f"GL(F) discriminator records {needle!r}", has(discriminator, needle))

    cache_needles = {
        PARENT_RUNNER: [
            "TOTAL: PASS=48 FAIL=0",
            "remaining boundary is only the matter-functional/action-surface supplier",
            "bridge cache validates the sibling packet without rerunning it here",
        ],
        BRIDGE_RUNNER: [
            "TOTAL: PASS=39 FAIL=0",
            "matter-functional clause I-4 remains explicitly not discharged",
            "HARD-CORE ESCAPE",
        ],
        FORCING_RUNNER: [
            "TOTAL: PASS=45, FAIL=0",
            "SCOPE-BOUNDARY",
            "hard-core-boson frame ties",
        ],
        NO_GO_RUNNER: [
            "PASS=34 FAIL=0",
            "SUBSTEP-1 IS A COMPATIBILITY, NOT A FORCING",
        ],
        DISCRIMINATOR_RUNNER: [
            "TOTAL: PASS=24 FAIL=0",
            "GL(F) is NOT retained and NOT a",
            "unconditionally, the retained 2026-05-25 no-go stands",
        ],
    }
    for runner, needles in cache_needles.items():
        check_cache(runner, needles)

    check(
        "packet leaves exactly the matter-functional supplier open",
        has(parent, "only the matter-functional/action-surface clause remains open")
        and has(bridge, "matter-functional clause (I-4) is NOT discharged")
        and has(no_go, "Axiom 1 / Axiom 2 baseline plus pure operator-algebra")
        and has(discriminator, "not supplied here"),
    )
    check(
        "packet is non-promotional",
        has(parent, "does not promote this row")
        and has(bridge, "changes **no** row's effective status")
        and has(forcing, "independent audit lane only")
        and has(no_go, "independent audit lane only")
        and has(discriminator, "independent audit lane only"),
    )

    print("=" * 76)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        return 1
    print(
        "GL(F) reconstruction packet is source-side re-audit ready: the "
        "kinematic identification clauses and runner caches are coherent, "
        "while the matter-functional/action-surface supplier remains the "
        "single explicit open pin."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
