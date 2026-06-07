#!/usr/bin/env python3
"""Source-packet checks for the axiom-first RP parent row.

This runner does not apply an audit verdict.  It verifies that the parent row
is wired to the Wilson-plane sign-repair packet and that the packet keeps the
promised status boundary.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE = ROOT / "docs" / "AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md"
BRIDGE_NOTE = ROOT / "docs" / "RP_WILSON_TEMPORAL_GAUGE_BRIDGE_SIGN_AND_POSITIVITY_REPAIR_NOTE_2026-06-06.md"
BRIDGE_RUNNER = ROOT / "scripts" / "frontier_rp_wilson_temporal_gauge_sign_and_positivity_repair_2026_06_06.py"
BRIDGE_CACHE = ROOT / "logs" / "runner-cache" / "frontier_rp_wilson_temporal_gauge_sign_and_positivity_repair_2026_06_06.txt"
FREE_CACHE = ROOT / "logs" / "runner-cache" / "axiom_first_rp_two_step_transfer_matrix_positivity.txt"


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def require_text(label: str, text: str, needle: str) -> None:
    check(label, needle in text, needle)


def main() -> int:
    print("axiom-first RP parent source-packet verifier 2026-06-07")
    for path in [PARENT_NOTE, BRIDGE_NOTE, BRIDGE_RUNNER, BRIDGE_CACHE, FREE_CACHE]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    parent = PARENT_NOTE.read_text()
    bridge = BRIDGE_NOTE.read_text()
    bridge_cache = BRIDGE_CACHE.read_text()
    free_cache = FREE_CACHE.read_text()

    require_text("parent cites bridge note", parent, "RP_WILSON_TEMPORAL_GAUGE_BRIDGE_SIGN_AND_POSITIVITY_REPAIR_NOTE_2026-06-06.md")
    require_text("parent names latest blocker", parent, "derive the full Wilson-plaquette gauge-half sesquilinear PSD form")
    require_text("parent uses corrected Wilson sign", parent, "S_0 := -beta Re Tr[U_+ U_-^dag]")
    require_text("parent names ferromagnetic weight", parent, "exp(+beta Re Tr[U_+ U_-^dag])")
    require_text("parent records character positivity route", parent, "powers/fusion products have non-negative multiplicities")
    require_text("parent records Gram factorization", parent, "G = W diag(kappa) W^dag")
    require_text("parent keeps audit boundary", parent, "any downstream row retained.")

    require_text("bridge note fixes failed sign root", bridge, "S_0 := -beta")
    require_text("bridge note proves exact coefficient positivity", bridge, "tensor-power multiplicities")
    require_text("bridge note rejects grid exactness", bridge, "finite grid is spectrally-convergent")
    require_text("bridge note has wrong-sign teeth", bridge, "antiferromagnetic")
    require_text("bridge note says no new axiom", bridge, "introduces **no** new axiom")

    require_text("bridge cache passed", bridge_cache, "TOTAL: 17 PASS / 0 FAIL")
    require_text("free two-step cache passed", free_cache, "PASS=7 FAIL=0")
    require_text("free two-step cache has BdagB", free_cache, "T_hat^2 = B^dag B")

    banned_parent_phrases = [
        "author-applied retained status",
        "does not set or predict an audit outcome",
    ]
    for phrase in banned_parent_phrases:
        check(f"parent status firewall present: {phrase}", phrase in parent)

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
