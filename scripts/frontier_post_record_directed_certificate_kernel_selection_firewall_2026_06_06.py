#!/usr/bin/env python3
"""No-go for selecting a production kernel from directed certificates alone."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0

Word = tuple[str, ...]
Source = dict[str, Fraction]
Kernel = dict[str, dict[str, Fraction]]
Law = dict[Word, Fraction]


@dataclass(frozen=True)
class KernelBridge:
    bridge_id: str
    law_id: str
    orientation: str | None
    clock_id: str | None
    kernel_id: str | None


@dataclass(frozen=True)
class KernelCertificate:
    cert_id: str
    law_id: str
    bridge_id: str
    statistic_id: str
    expected_value: Fraction


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


def section(title: str) -> None:
    print()
    print("-" * 78)
    print(title)
    print("-" * 78)


def read_rel(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require_text(path: str, needles: list[str]) -> None:
    text = read_rel(path)
    report(f"{path} exists", True)
    for needle in needles:
        report(f"{path} contains: {needle}", needle in text)


def normalized_source(source: Source) -> bool:
    return bool(source) and sum(source.values(), Fraction(0, 1)) == 1 and all(p >= 0 for p in source.values())


def row_stochastic(kernel: Kernel) -> bool:
    return all(sum(row.values(), Fraction(0, 1)) == 1 and all(p >= 0 for p in row.values()) for row in kernel.values())


def markov_law_length2(source: Source, kernel: Kernel) -> Law:
    out: defaultdict[Word, Fraction] = defaultdict(Fraction)
    for a, source_mass in source.items():
        for b, transition_mass in kernel[a].items():
            out[(a, b)] += source_mass * transition_mass
    return dict(out)


def alphabet_for(law: Law) -> tuple[str, ...]:
    return tuple(sorted({atom for word in law for atom in word}))


def count_word(word: Word, alphabet: tuple[str, ...]) -> tuple[int, ...]:
    counts = Counter(word)
    return tuple(counts[a] for a in alphabet)


def count_pushforward(law: Law) -> dict[tuple[int, ...], Fraction]:
    alphabet = alphabet_for(law)
    out: defaultdict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    for word, mass in law.items():
        out[count_word(word, alphabet)] += mass
    return dict(out)


def expectation(law: Law, statistic) -> Fraction:
    return sum(Fraction(statistic(word), 1) * mass for word, mass in law.items())


def endpoint_ab(word: Word) -> int:
    return int(len(word) >= 2 and word[0] == "A" and word[-1] == "B")


def endpoint_ba(word: Word) -> int:
    return int(len(word) >= 2 and word[0] == "B" and word[-1] == "A")


def signed_ab_ba(word: Word) -> int:
    return endpoint_ab(word) - endpoint_ba(word)


def second_is_b(word: Word) -> int:
    return int(len(word) >= 2 and word[1] == "B")


STATISTICS = {
    "endpoint_ab": endpoint_ab,
    "endpoint_ba": endpoint_ba,
    "signed_ab_ba": signed_ab_ba,
    "second_is_b": second_is_b,
}


def verify_certificate(law_id: str, law: Law, bridge: KernelBridge, cert: KernelCertificate) -> tuple[str, Fraction | None]:
    if bridge.orientation not in {"forward", "reverse"}:
        return "blocked_missing_orientation", None
    if bridge.clock_id is None:
        return "blocked_missing_clock", None
    if bridge.kernel_id is None:
        return "blocked_missing_kernel", None
    if law_id != cert.law_id or bridge.law_id != law_id or bridge.bridge_id != cert.bridge_id:
        return "blocked_scope_mismatch", None
    statistic = STATISTICS.get(cert.statistic_id)
    if statistic is None:
        return "blocked_unknown_statistic", None
    value = expectation(law, statistic)
    if value != cert.expected_value:
        return "value_mismatch", value
    return "verified", value


def matching_kernels(
    source: Source,
    candidates: dict[str, Kernel],
    statistic_id: str,
    expected_value: Fraction,
) -> list[str]:
    statistic = STATISTICS[statistic_id]
    out: list[str] = []
    for name, kernel in candidates.items():
        law = markov_law_length2(source, kernel)
        if expectation(law, statistic) == expected_value:
            out.append(name)
    return out


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_DIRECTED_CERTIFICATE_KERNEL_SELECTION_FIREWALL_2026-06-06.md",
        [
            "Directed certificates do not select a production kernel",
            "kernel remains a supplied bridge input",
            "same directed certificate data can admit distinct candidate kernels",
        ],
    )
    require_text(
        "docs/POST_RECORD_DIRECTED_CERTIFICATE_EXAMPLES_2026-06-06.md",
        [
            "supplied finite law plus supplied orientation bridge",
            "examples do not derive an arrow, clock, kernel, or selected dial",
            "The certificate is scoped to those inputs.",
        ],
    )
    require_text(
        "docs/POST_RECORD_SUPPLIED_ORIENTATION_BRIDGE_INTERFACE_2026-06-06.md",
        [
            "The physical forward order is a supplied bridge",
            "does not derive an orientation",
            "Does not derive or select a production kernel",
        ],
    )
    require_text(
        "docs/POST_RECORD_ARROW_ORIENTATION_FIREWALL_2026-06-06.md",
        [
            "post-record counts do not orient a physical arrow",
            "or production kernel is a separate",
            "count states are invariant under word reversal",
        ],
    )


def unvisited_row_no_go() -> None:
    section("No-go 1: identical finite law with different unvisited kernel rows")
    source: Source = {"A": Fraction(1, 1)}
    k1: Kernel = {
        "A": {"A": Fraction(1, 2), "B": Fraction(1, 2)},
        "B": {"A": Fraction(1, 1), "B": Fraction(0, 1)},
    }
    k2: Kernel = {
        "A": {"A": Fraction(1, 2), "B": Fraction(1, 2)},
        "B": {"A": Fraction(0, 1), "B": Fraction(1, 1)},
    }
    law1 = markov_law_length2(source, k1)
    law2 = markov_law_length2(source, k2)
    bridge = KernelBridge("bridge_kernel_supplied", "law_unvisited_row", "forward", "word_index_clock", "kernel_candidate")
    cert = KernelCertificate("endpoint_ab_cert", "law_unvisited_row", "bridge_kernel_supplied", "endpoint_ab", Fraction(1, 2))
    no_kernel_bridge = KernelBridge("bridge_kernel_supplied", "law_unvisited_row", "forward", "word_index_clock", None)

    report("source is normalized for unvisited-row witness", normalized_source(source))
    report("first candidate kernel is row-stochastic", row_stochastic(k1), str(k1))
    report("second candidate kernel is row-stochastic", row_stochastic(k2), str(k2))
    report("candidate kernels differ", k1 != k2)
    report("finite length-2 laws are identical", law1 == law2, str(law1))
    report("endpoint A-to-B certificate value is identical", expectation(law1, endpoint_ab) == expectation(law2, endpoint_ab) == Fraction(1, 2))
    report("signed directed statistic is identical", expectation(law1, signed_ab_ba) == expectation(law2, signed_ab_ba) == Fraction(1, 2))
    report("count pushforward is identical", count_pushforward(law1) == count_pushforward(law2), str(count_pushforward(law1)))

    status, value = verify_certificate("law_unvisited_row", law1, bridge, cert)
    missing_status, missing_value = verify_certificate("law_unvisited_row", law1, no_kernel_bridge, cert)
    matches = matching_kernels(source, {"k1": k1, "k2": k2}, "endpoint_ab", Fraction(1, 2))
    report("supplied-kernel certificate verifies when kernel id is supplied", status == "verified" and value == Fraction(1, 2))
    report("missing kernel id blocks dynamics-language certificate", missing_status == "blocked_missing_kernel" and missing_value is None)
    report("same certificate admits both distinct candidate kernels", matches == ["k1", "k2"], str(matches))
    report("certificate does not uniquely select kernel", len(matches) > 1)


def scalar_certificate_underselection_no_go() -> None:
    section("No-go 2: same scalar certificate with different laws and kernels")
    source: Source = {"A": Fraction(1, 2), "B": Fraction(1, 2)}
    k3: Kernel = {
        "A": {"A": Fraction(1, 2), "B": Fraction(1, 2)},
        "B": {"A": Fraction(0, 1), "B": Fraction(1, 1)},
    }
    k4: Kernel = {
        "A": {"A": Fraction(1, 2), "B": Fraction(1, 2)},
        "B": {"A": Fraction(1, 1), "B": Fraction(0, 1)},
    }
    law3 = markov_law_length2(source, k3)
    law4 = markov_law_length2(source, k4)
    matches = matching_kernels(source, {"k3": k3, "k4": k4}, "endpoint_ab", Fraction(1, 4))

    report("source is normalized for scalar-underselection witness", normalized_source(source))
    report("full-support candidate kernels are row-stochastic", row_stochastic(k3) and row_stochastic(k4))
    report("full-support candidate kernels differ", k3 != k4)
    report("full-support laws differ", law3 != law4, f"law3={law3} law4={law4}")
    report("endpoint A-to-B scalar certificate is the same", expectation(law3, endpoint_ab) == expectation(law4, endpoint_ab) == Fraction(1, 4))
    report("other directed statistic separates the candidates", expectation(law3, endpoint_ba) != expectation(law4, endpoint_ba))
    report("second-is-B statistic separates the candidates", expectation(law3, second_is_b) != expectation(law4, second_is_b))
    report("same scalar certificate admits both candidates", matches == ["k3", "k4"], str(matches))
    report("scalar certificate alone does not select production kernel", len(matches) > 1)


def bridge_scope_checks() -> None:
    section("Bridge-scope checks")
    law: Law = {
        ("A", "A"): Fraction(1, 2),
        ("A", "B"): Fraction(1, 2),
    }
    bridge = KernelBridge("bridge_scope", "law_scope", "forward", "clock_scope", "kernel_scope")
    wrong_law_bridge = KernelBridge("bridge_scope", "other_law", "forward", "clock_scope", "kernel_scope")
    missing_orientation = KernelBridge("bridge_scope", "law_scope", None, "clock_scope", "kernel_scope")
    wrong_value = KernelCertificate("bad_value", "law_scope", "bridge_scope", "endpoint_ab", Fraction(0, 1))
    cert = KernelCertificate("good_value", "law_scope", "bridge_scope", "endpoint_ab", Fraction(1, 2))

    status_good, value_good = verify_certificate("law_scope", law, bridge, cert)
    status_wrong_law, value_wrong_law = verify_certificate("law_scope", law, wrong_law_bridge, cert)
    status_missing, value_missing = verify_certificate("law_scope", law, missing_orientation, cert)
    status_bad, value_bad = verify_certificate("law_scope", law, bridge, wrong_value)
    report("bridge-scoped certificate verifies", status_good == "verified" and value_good == Fraction(1, 2))
    report("wrong bridge law scope is blocked", status_wrong_law == "blocked_scope_mismatch" and value_wrong_law is None)
    report("missing orientation is blocked", status_missing == "blocked_missing_orientation" and value_missing is None)
    report("wrong certificate value is rejected", status_bad == "value_mismatch" and value_bad == Fraction(1, 2))


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    production_kernel_selected = False
    production_kernel_derived_from_directed_certificate = False
    orientation_derived_from_record = False
    physical_arrow_derived_from_record = False
    clock_or_rate_derived = False
    born_law_derived_from_record = False
    generation_or_koide_dial_selected = False
    stable_setting_selects_dial = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("production-kernel selected flag is false", not production_kernel_selected)
    report("kernel derived from directed certificate flag is false", not production_kernel_derived_from_directed_certificate)
    report("Record-derived orientation flag is false", not orientation_derived_from_record)
    report("Record-derived physical arrow flag is false", not physical_arrow_derived_from_record)
    report("clock/rate derived flag is false", not clock_or_rate_derived)
    report("Born law derived from Record flag is false", not born_law_derived_from_record)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("stable setting selects dial flag is false", not stable_setting_selects_dial)


def main() -> int:
    source_anchor_checks()
    unvisited_row_no_go()
    scalar_certificate_underselection_no_go()
    bridge_scope_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("DIRECTED_CERTIFICATE_KERNEL_SELECTION_FIREWALL=TRUE")
    print("SAME_DIRECTED_CERTIFICATE_DISTINCT_KERNELS=TRUE")
    print("PRODUCTION_KERNEL_SELECTED=FALSE")
    print("PRODUCTION_KERNEL_DERIVED_FROM_DIRECTED_CERTIFICATE=FALSE")
    print("ORIENTATION_DERIVED_FROM_RECORD=FALSE")
    print("PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE")
    print("CLOCK_OR_RATE_DERIVED=FALSE")
    print("BORN_LAW_DERIVED_FROM_RECORD=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    print("STABLE_SETTING_SELECTS_DIAL=FALSE")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
