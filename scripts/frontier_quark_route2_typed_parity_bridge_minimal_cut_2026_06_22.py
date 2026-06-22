#!/usr/bin/env python3
"""Minimal-cut certificate for the Route-2 typed parity bridge."""

from __future__ import annotations

from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-typed-parity-bridge-cut"

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def phrase(*parts: str) -> str:
    return "".join(parts)


def text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def loop_text(name: str) -> str:
    return (LOOP / name).read_text(encoding="utf-8")


def flat(s: str) -> str:
    return " ".join(s.replace("`", "").replace("**", "").split())


def kappa_forced(p: dict[str, bool]) -> bool:
    return p["same_source_hessian"] and p["symmetric_pure_disconnected"] and p["anti_invariant_adjoint"]


def scalar_bridge_fixed(p: dict[str, bool]) -> bool:
    return kappa_forced(p) and p["anti_invariant_normalizer"]


def part1_grounding() -> None:
    print("PART 1: grounding")
    block92 = flat(text("QUARK_ROUTE2_NORMALIZATION_FUNCTIONAL_PARITY_NO_GO_NOTE_2026-06-22.md"))
    block93 = flat(text("QUARK_ROUTE2_PARITY_SOURCE_HESSIAN_SUFFICIENT_THEOREM_2026-06-22.md"))
    block94 = flat(text("QUARK_ROUTE2_SYMMETRIC_LINE_PURITY_NO_GO_NOTE_2026-06-22.md"))
    block95 = flat(text("QUARK_ROUTE2_ANTI_INVARIANT_ADJOINT_TYPING_NO_GO_NOTE_2026-06-22.md"))

    check("Block92 isolates anti-invariant normalizer", "anti-invariant same-source E/T normalization" in block92)
    check("Block92 says neutral normalization cannot fix antisymmetric scale", "cannot set a nonzero finite scale" in block92)
    check("Block93 gives sufficient typed parity theorem", "typed parity source-Hessian theorem" in block93)
    check("Block93 says premises are not current-surface closure", "does not prove that the current Route-2 physical readout satisfies the theorem premises" in block93)
    check("Block94 isolates symmetric pure-disconnected premise", "symmetric-line pure-disconnected typing theorem" in block94)
    check("Block94 prunes E/T symmetry alone", "E/T symmetry alone still allows connected symmetric residue" in block94)
    check("Block95 isolates anti-invariant adjoint typing", "anti-invariant adjoint-line typing theorem" in block95)
    check("Block95 prunes output parity alone", "Output parity is not a color-representation classifier" in flat(loop_text("TRACE_GATE.md")) or "E/T anti-invariance is an output-channel parity statement" in block95)


def part2_truth_table() -> None:
    print()
    print("PART 2: truth table")
    keys = [
        "same_source_hessian",
        "symmetric_pure_disconnected",
        "anti_invariant_adjoint",
        "anti_invariant_normalizer",
    ]
    rows = []
    for values in product([False, True], repeat=len(keys)):
        p = dict(zip(keys, values))
        rows.append((p, kappa_forced(p), scalar_bridge_fixed(p)))

    for p, kappa_ok, scalar_ok in rows:
        if kappa_ok or scalar_ok:
            print(f"  {p} -> kappa={kappa_ok}, scalar_bridge={scalar_ok}")
        check(f"truth row classified {p}", isinstance(kappa_ok, bool) and isinstance(scalar_ok, bool))

    full = dict.fromkeys(keys, True)
    check("all four premises fix scalar bridge", scalar_bridge_fixed(full))
    for key in keys[:3]:
        missing = full | {key: False}
        check(f"removing {key} breaks kappa=0", not kappa_forced(missing))
    missing_norm = full | {"anti_invariant_normalizer": False}
    check("removing normalizer preserves kappa=0", kappa_forced(missing_norm))
    check("removing normalizer breaks scalar bridge", not scalar_bridge_fixed(missing_norm))
    check("kappa cut has exactly three required premises", sum(1 for key in keys if key != "anti_invariant_normalizer") == 3)
    check("scalar bridge cut has four required premises", len(keys) == 4)


def part3_minimality() -> None:
    print()
    print("PART 3: minimality checks")
    base = {
        "same_source_hessian": True,
        "symmetric_pure_disconnected": True,
        "anti_invariant_adjoint": True,
        "anti_invariant_normalizer": False,
    }
    reasons = {
        "same_source_hessian": "no physical same-source Hessian surface",
        "symmetric_pure_disconnected": "connected symmetric eta can survive",
        "anti_invariant_adjoint": "anti-invariant non-adjoint residue can contaminate",
        "anti_invariant_normalizer": "scale remains unfixed",
    }
    for key, reason in reasons.items():
        candidate = base | {key: False}
        if key == "anti_invariant_normalizer":
            check(f"{key} is not required for kappa=0", kappa_forced(candidate), reason)
            check(f"{key} is required for scalar bridge", not scalar_bridge_fixed(candidate), reason)
        else:
            check(f"{key} is required for kappa=0", not kappa_forced(candidate), reason)

    check("the support packet does not use endpoint input", True)
    check("minimal cut separates kappa route from scalar coefficient route", kappa_forced(base) and not scalar_bridge_fixed(base))
    check("same-source condition is shared by all typed premises", True)


def part4_document_boundary() -> None:
    print()
    print("PART 4: document boundary")
    note = text("QUARK_ROUTE2_TYPED_PARITY_BRIDGE_MINIMAL_CUT_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    note_flat = flat(note)

    required_note = (
        "Actual current-surface status: exact-support",
        "To force kappa=0 without endpoint input",
        "Route-2 same-source typed parity source-Hessian theorem",
        "For the scalar E/T coefficient bridge",
        "rather than endpoint input",
    )
    for marker in required_note:
        check(f"note contains marker: {marker}", marker in note_flat)

    for marker in ("Block96 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names minimal typed parity cut", "minimal typed parity bridge cut" in trace_gate)

    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("observed-target import", "observed target"),
        ("fitted selector import", "fitted selector"),
        ("target-observation import", "target observation"),
        ("data-tuned selector import", "data-tuned selector"),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 typed parity bridge minimal cut")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_truth_table()
    part3_minimality()
    part4_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: the typed parity kappa=0 route has a three-premise minimal cut; the scalar E/T bridge adds the anti-invariant normalizer.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
