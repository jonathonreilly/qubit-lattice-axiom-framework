#!/usr/bin/env python3
"""Verifier for the D3 upper-bound import-scope gate.

The runner checks the current repo prose anchors and the finite set
composition used by docs/D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md.
It does not prove Bertrand's theorem, atomic stability, or a framework-native
dimension-selection theorem.
"""
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PASS_COUNT = 0
FAIL_COUNT = 0


PATHS = {
    "gate_note": ROOT / "docs" / "D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md",
    "lower_note": ROOT / "docs" / "DIMENSION_SELECTION_NOTE.md",
    "upper_wrapper": ROOT / "docs" / "DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md",
    "bertrand_support": ROOT / "docs" / "BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md",
    "coulomb_support": ROOT / "docs" / "COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md",
}


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"[{status}] {name}{suffix}")


def read_text(label: str) -> str:
    path = PATHS[label]
    check(f"{label} exists", path.exists(), path.relative_to(ROOT).as_posix())
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def has(text: str, needle: str) -> bool:
    return needle in text


def has_re(text: str, pattern: str) -> bool:
    return re.search(pattern, text, flags=re.MULTILINE | re.DOTALL) is not None


def main() -> None:
    print("D3 upper-bound import-scope gate")
    print("=" * 58)

    gate = read_text("gate_note")
    lower = read_text("lower_note")
    upper = read_text("upper_wrapper")
    bertrand = read_text("bertrand_support")
    coulomb = read_text("coulomb_support")

    check(
        "gate status is branch-local exact support, not promotion",
        has(gate, "exact-support branch-local import-scope gate")
        and has(gate, "not an audit\nverdict")
        and has(gate, "not a repo-wide dimension-selection promotion"),
    )
    check(
        "gate names the current lower-bound finite set",
        has(gate, "L_runner = {3,4,5}"),
    )
    check(
        "gate identifies Bertrand as the decisive current uniqueness import",
        has(gate, "depends on the Bertrand upper-bound\nimport")
        and has(gate, "Atomic stability supplies compatible companion support"),
    )
    check(
        "gate forbids repo-wide authority edits",
        has(gate, "active review queue")
        and has(gate, "audit ledger")
        and has(gate, "publication matrix"),
    )

    check(
        "lower note is scoped as lower-bound support only",
        has(lower, "lower-bound support only")
        and has(lower, "not a unique-dimension\ntheorem"),
    )
    check(
        "lower note reports d<=2 failure and d=3,4,5 pass",
        has(lower, "d <= 2  -> fails")
        and has(lower, "d >= 3  -> passes those runner criteria for d = 3, 4, 5"),
    )
    check(
        "lower note keeps upper wrapper non-load-bearing for that row",
        has(lower, "wrapper is not load-bearing for the bounded claim here"),
    )
    check(
        "lower note requires separate review for framework-internal d<=3",
        has(lower, "derive `d <= 3` inside the framework must be reviewed separately"),
    )

    check(
        "upper wrapper is explicitly named-import-only",
        has(upper, "Named Non-Derivation Imports")
        and has(upper, "bounded named-import wrapper"),
    )
    check(
        "upper wrapper records independent audit authority",
        has(upper, "independent audit lane only"),
    )
    check(
        "upper wrapper contains Bertrand route and d<=3 bound",
        has(upper, "Bertrand's theorem")
        and has(upper, "stable bounded orbits under gravity require `d <= 3`"),
    )
    check(
        "upper wrapper contains atomic route and d<=4 bound",
        has(upper, "Tangherlini")
        and has(upper, "Ehrenfest")
        and has(upper, "stable hydrogen-like atoms require `d <= 4`"),
    )
    check(
        "upper wrapper marks standard Coulomb spectrum only at d=3",
        has(upper, "canonical infinite-bound-state Coulomb spectrum existing only at\n`d = 3`"),
    )
    check(
        "upper wrapper forbids internal-derivation overread",
        has(upper, "This is NOT a re-derivation of Bertrand's theorem")
        and has(upper, "This is NOT a re-derivation of the atomic-stability upper bound")
        and has(upper, "This is NOT a framework-level derivation of `d = 3`"),
    )

    check(
        "Bertrand support note keeps theorem import boundary explicit",
        has(bertrand, "not claim a complete framework-internal proof of Bertrand's theorem")
        and has(bertrand, "does not retire the Bertrand theorem import completely"),
    )
    check(
        "Bertrand support note verifies circular-orbit sign classification",
        has(bertrand, "circular orbits only for integer `d = 3`; `d = 4` is marginal")
        and has(bertrand, "d >= 5` is unstable"),
    )
    check(
        "Coulomb support note keeps admitted-premise boundary explicit",
        has(coulomb, "admitted premises")
        and has(coulomb, "does not supply a framework-native electromagnetic sector"),
    )
    check(
        "Coulomb support note does not close D3 chain by itself",
        has(coulomb, "does\nnot close the D=3 chain by itself")
        and has(coulomb, "does not prove a full hydrogenic `d = 3` spectrum"),
    )

    lower_runner_support = {3, 4, 5}
    checked_positive_dims = set(range(1, 9))
    bertrand_upper = {d for d in checked_positive_dims if d <= 3}
    atomic_ground_upper = {d for d in checked_positive_dims if d <= 4}
    atomic_strict_spectrum = {3}

    lower_and_bertrand = lower_runner_support & bertrand_upper
    lower_and_atomic_ground = lower_runner_support & atomic_ground_upper
    lower_and_atomic_strict = lower_runner_support & atomic_strict_spectrum

    check("lower support set is exactly the checked current finite set", lower_runner_support == {3, 4, 5})
    check("Bertrand upper set over checked positive dims is d<=3", bertrand_upper == {1, 2, 3})
    check("atomic weaker stability upper set over checked positive dims is d<=4", atomic_ground_upper == {1, 2, 3, 4})
    check("lower intersect Bertrand is unique d=3", lower_and_bertrand == {3}, str(sorted(lower_and_bertrand)))
    check(
        "lower intersect weaker atomic stability is not unique",
        lower_and_atomic_ground == {3, 4},
        str(sorted(lower_and_atomic_ground)),
    )
    check("lower intersect strict atomic spectrum is unique if separately used", lower_and_atomic_strict == {3})
    check(
        "Bertrand is decisive under current weaker atomic-stability scope",
        lower_and_bertrand == {3} and lower_and_atomic_ground != {3},
    )
    check(
        "atomic companion support is compatible with Bertrand-selected d=3",
        3 in lower_and_atomic_ground and 3 in lower_and_bertrand,
    )

    forbidden_gate_patterns = [
        r"framework-internal derivation of Bertrand's theorem;\n-\s+a framework-internal derivation of atomic stability;\n-\s+a full dimension-selection theorem",
        r"does not claim:\n\n-\s+a framework-internal derivation",
    ]
    check(
        "gate non-claims include framework derivation firewall",
        all(has_re(gate, pattern) for pattern in forbidden_gate_patterns),
    )
    check(
        "gate records future work as import retirement or explicit import support",
        has(gate, "retire the Bertrand import")
        and has(gate, "keep the dimension lane\n  explicitly import-supported"),
    )
    check(
        "runner path is cited by gate note",
        has(gate, "scripts/frontier_d3_upper_bound_import_scope_gate_2026_06_06.py"),
    )
    check(
        "runner cache path is cited by gate note",
        has(gate, "logs/runner-cache/frontier_d3_upper_bound_import_scope_gate_2026_06_06.txt"),
    )

    print("=" * 58)
    print("COMPOSITION:")
    print(f"  lower runner support: {sorted(lower_runner_support)}")
    print(f"  Bertrand upper:       d <= 3 -> {sorted(bertrand_upper)}")
    print(f"  atomic weak upper:    d <= 4 -> {sorted(atomic_ground_upper)}")
    print(f"  lower & Bertrand:     {sorted(lower_and_bertrand)}")
    print(f"  lower & atomic weak:  {sorted(lower_and_atomic_ground)}")
    print("STATUS: exact-support import-scope gate; audit_required_before_effective_retained=true")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")

    if FAIL_COUNT:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
