#!/usr/bin/env python3
"""Verify the additive D3 native stable-orbit upper-bound composition note."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0


PATHS = {
    "note": "docs/D3_NATIVE_STABLE_ORBIT_UPPER_BOUND_COMPOSITION_NOTE_2026-06-09.md",
    "lower": "docs/DIMENSION_SELECTION_NOTE.md",
    "stable": "docs/BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md",
    "coulomb": "docs/COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md",
    "legacy_wrapper": "docs/DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md",
    "legacy_gate": "docs/D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md",
    "stable_runner": "scripts/bertrand_stable_orbit_green_kernel_bridge.py",
    "coulomb_runner": "scripts/frontier_coulomb_stability_scaling_repair.py",
    "self_runner": "scripts/d3_native_stable_orbit_upper_bound_composition_2026_06_09.py",
    "stable_cache": "logs/runner-cache/bertrand_stable_orbit_green_kernel_bridge.txt",
    "coulomb_cache": "logs/runner-cache/frontier_coulomb_stability_scaling_repair.txt",
    "self_cache": "logs/runner-cache/d3_native_stable_orbit_upper_bound_composition_2026_06_09.txt",
}


def report(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def text(label: str) -> str:
    rel = PATHS[label]
    path = ROOT / rel
    report(f"{rel} exists", path.exists())
    return path.read_text(encoding="utf-8") if path.exists() else ""


def flat(body: str) -> str:
    return " ".join(body.split())


def cites(body: str, rel: str) -> bool:
    return rel in body or Path(rel).name in body


def source_checks() -> None:
    note = text("note")
    lower = text("lower")
    stable = text("stable")
    coulomb = text("coulomb")
    legacy_wrapper = text("legacy_wrapper")
    legacy_gate = text("legacy_gate")

    for label in (
        "stable_runner",
        "coulomb_runner",
        "self_runner",
        "stable_cache",
        "coulomb_cache",
    ):
        text(label)

    note_paths = [
        PATHS["lower"],
        PATHS["stable"],
        PATHS["coulomb"],
        PATHS["legacy_wrapper"],
        PATHS["legacy_gate"],
        PATHS["stable_runner"],
        PATHS["coulomb_runner"],
        PATHS["self_runner"],
        PATHS["stable_cache"],
        PATHS["coulomb_cache"],
        PATHS["self_cache"],
    ]
    for rel in note_paths:
        report(f"composition note cites {rel}", cites(note, rel))

    note_flat = flat(note)
    stable_flat = flat(stable)
    coulomb_flat = flat(coulomb)
    lower_flat = flat(lower)

    report(
        "note is additive and source-side only",
        "additive source-support wrapper" in note
        and "source-side proposal" in note
        and "without editing any retained/audited source note" in note_flat,
    )
    report(
        "note forbids audit/status side effects",
        "direct_effective_status_change_allowed_from_this_note: false" in note
        and "does not write an\naudit verdict" in note
        and "set an effective status" in note
        and "any edit to `docs/audit/**`" in note,
    )
    report(
        "note names native stable-orbit edge as load-bearing",
        "native stable-circular-orbit edge" in note
        and "U_stable = {d : d <= 3}" in note
        and "full all-bounded-orbits-are-closed Bertrand theorem is not consumed" in note,
    )
    report(
        "note keeps Coulomb edge companion-only",
        "U_Coulomb_weak = {d : d <= 4}" in note
        and "compatible companion support, not the unique\nselector" in note,
    )
    report(
        "lower note exposes only checked finite packet",
        "lower-bound support only" in lower
        and "d >= 3  -> passes those runner criteria for d = 3, 4, 5" in lower,
    )
    report(
        "stable support note derives Green-kernel potential shape",
        "V(r) = -k/r^(d-2)" in stable
        and "k(d-2)(4-d)/r_c^d" in stable,
    )
    report(
        "stable support note gives d=3 stable and d>=5 unstable classification",
        "circular orbits only for integer `d = 3`" in stable_flat
        and "`d = 4` case is marginal" in stable_flat
        and "`d >= 5` is unstable" in stable,
    )
    report(
        "stable support note does not consume full Bertrand closure theorem",
        "The exact all-`L` closed-orbit theorem is not consumed" in stable_flat
        and "stable-circular-orbit edge" in stable_flat,
    )
    report(
        "Coulomb support note remains bounded companion support",
        "does not prove a full hydrogenic `d = 3` spectrum" in coulomb
        and "does not close the D=3 chain by itself" in coulomb_flat,
    )
    report(
        "legacy-named wrapper consumes native stable-orbit edge",
        "Native Stable-Orbit Edge" in legacy_wrapper
        and "U_stable = {d : d <= 3}" in legacy_wrapper
        and "full Bertrand closed-orbit theorem as an imported premise" in legacy_wrapper,
    )
    report(
        "legacy-named gate consumes native stable-orbit edge",
        "# D3 Upper-Bound Native Stable-Orbit Scope Gate" in legacy_gate
        and "exact-support branch-local native-stable-edge gate" in legacy_gate,
    )
    report(
        "note non-claims block overread",
        "full framework-internal proof of Bertrand's closed-orbit theorem" in note
        and "framework-native electromagnetic sector or hydrogenic spectrum" in note
        and "full dimension-selection theorem from the minimal axioms" in note,
    )
    report(
        "note declares source-only audit boundary without retained-grade promotion",
        "source-side composition certificate only" in note
        and "retained-grade source" in note
        and "Independent audit owns any effective-status change" in note,
    )
    report(
        "note records current lower and upper composition text",
        "L_runner = {3,4,5}" in note
        and "{3,4,5} intersect {d : d <= 3}" in note
        and "{3,4,5} intersect {d : d <= 4}" in note,
    )
    report(
        "note permits wrapper/gate wiring without changing support-note claim",
        "now consume this native stable-orbit edge" in note
        and "Later source repairs may wire the\nlegacy-named wrapper/gate" in note,
    )


def composition_checks() -> None:
    lower_set = {3, 4, 5}
    checked_positive_dims = set(range(1, 9))
    native_stable_upper = {d for d in checked_positive_dims if d <= 3}
    coulomb_weak_upper = {d for d in checked_positive_dims if d <= 4}
    strict_spectrum = {3}

    lower_stable = lower_set & native_stable_upper
    lower_coulomb = lower_set & coulomb_weak_upper
    lower_strict = lower_set & strict_spectrum

    report("lower support set is exactly {3,4,5}", lower_set == {3, 4, 5})
    report("native stable upper set over checked dims is d<=3", native_stable_upper == {1, 2, 3})
    report("Coulomb weak upper set over checked dims is d<=4", coulomb_weak_upper == {1, 2, 3, 4})
    report("strict d=3 spectrum set is singleton {3}", strict_spectrum == {3})
    report("lower intersect native stable upper is {3}", lower_stable == {3}, str(sorted(lower_stable)))
    report("lower intersect Coulomb weak upper is {3,4}", lower_coulomb == {3, 4}, str(sorted(lower_coulomb)))
    report("lower intersect strict spectrum is {3}", lower_strict == {3}, str(sorted(lower_strict)))
    report("native stable edge is decisive while weak Coulomb is not", lower_stable == {3} and lower_coulomb != {3})
    report("Coulomb companion remains compatible with selected d=3", 3 in lower_coulomb and 3 in lower_stable)


def cache_checks() -> None:
    stable_cache = text("stable_cache")
    coulomb_cache = text("coulomb_cache")
    report("stable-orbit cache certifies PASS=8", "SCORECARD: PASS=8" in stable_cache)
    report("Coulomb cache certifies PASS=53 FAIL=0", "SUMMARY: PASS=53 FAIL=0" in coulomb_cache)


def main() -> int:
    print("D3 native stable-orbit upper-bound additive composition")
    print("=" * 76)
    source_checks()
    composition_checks()
    cache_checks()
    print("=" * 76)
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
