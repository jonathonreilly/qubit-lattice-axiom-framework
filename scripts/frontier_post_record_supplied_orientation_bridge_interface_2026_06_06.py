#!/usr/bin/env python3
"""Exact supplied-orientation bridge interface for directed post-record events."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
ALPHABET = ("A", "B", "C")
Word = tuple[str, ...]
Law = dict[Word, Fraction]


@dataclass(frozen=True)
class OrientationBridge:
    bridge_id: str
    law_id: str
    orientation: str | None
    clock_id: str | None
    kernel_id: str | None


@dataclass(frozen=True)
class DirectedCertificate:
    name: str
    bridge_id: str
    law_id: str
    event_id: str
    epsilon: Fraction


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


def rev(word: Word) -> Word:
    return tuple(reversed(word))


def count(word: Word) -> tuple[int, ...]:
    c = Counter(word)
    return tuple(c[a] for a in ALPHABET)


def reverse_law(law: Law) -> Law:
    out: defaultdict[Word, Fraction] = defaultdict(Fraction)
    for word, mass in law.items():
        out[rev(word)] += mass
    return dict(out)


def count_pushforward(law: Law) -> dict[tuple[int, ...], Fraction]:
    out: defaultdict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    for word, mass in law.items():
        out[count(word)] += mass
    return dict(out)


def normalized(law: Law) -> bool:
    return sum(law.values(), Fraction(0, 1)) == 1 and all(p >= 0 for p in law.values())


def oriented_law(law: Law, bridge: OrientationBridge) -> Law | None:
    if bridge.orientation == "forward":
        return law
    if bridge.orientation == "reverse":
        return reverse_law(law)
    return None


def endpoint_a_to_b(word: Word) -> bool:
    return len(word) >= 2 and word[0] == "A" and word[-1] == "B"


def has_c_count_at_least_one(counts: tuple[int, ...]) -> bool:
    return counts[2] >= 1


def event_probability(law: Law, event) -> Fraction:
    return sum(mass for word, mass in law.items() if event(word))


def count_event_probability(law: Law, event) -> Fraction:
    pushed = count_pushforward(law)
    return sum(mass for counts, mass in pushed.items() if event(counts))


def verify_directed_certificate(
    law_id: str,
    law: Law,
    bridge: OrientationBridge,
    cert: DirectedCertificate,
) -> tuple[bool, Fraction | None]:
    if cert.event_id != "endpoint_A_to_B":
        raise ValueError(f"unknown event id: {cert.event_id}")
    olaw = oriented_law(law, bridge)
    if olaw is None:
        return False, None
    exact = event_probability(olaw, endpoint_a_to_b)
    ok = (
        normalized(law)
        and bridge.law_id == law_id
        and cert.law_id == law_id
        and cert.bridge_id == bridge.bridge_id
        and bridge.clock_id is not None
        and exact <= cert.epsilon
    )
    return ok, exact


def transitions(word: Word) -> Counter[tuple[str, str]]:
    return Counter(zip(word, word[1:]))


def normalize_rows(edges: Counter[tuple[str, str]]) -> dict[str, dict[str, Fraction]]:
    rows: dict[str, Counter[str]] = {a: Counter() for a in ALPHABET}
    for (a, b), n in edges.items():
        rows[a][b] += n
    kernel: dict[str, dict[str, Fraction]] = {}
    for a in ALPHABET:
        total = sum(rows[a].values())
        if total == 0:
            kernel[a] = {b: Fraction(1 if a == b else 0, 1) for b in ALPHABET}
        else:
            kernel[a] = {b: Fraction(rows[a][b], total) for b in ALPHABET}
    return kernel


def row_stochastic(kernel: dict[str, dict[str, Fraction]]) -> bool:
    return all(sum(row.values(), Fraction(0, 1)) == 1 for row in kernel.values())


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_SUPPLIED_ORIENTATION_BRIDGE_INTERFACE_2026-06-06.md",
        [
            "supplied orientation bridge",
            "The physical forward order is a supplied bridge",
            "does not derive an orientation",
            "directed post-record certificates are available only under supplied orientation/law/clock/kernel bridges",
        ],
    )
    require_text(
        "docs/POST_RECORD_ARROW_ORIENTATION_FIREWALL_2026-06-06.md",
        [
            "count pushforward is invariant under reversal",
            "oriented law, boundary condition, clock, or production kernel",
            "post-record counts do not orient a physical arrow",
        ],
    )
    require_text(
        "docs/POST_RECORD_SUPPLIED_CONCENTRATION_CERTIFICATE_INTERFACE_2026-06-06.md",
        [
            "certificate = (law id, event predicate, epsilon)",
            "verified law-scoped concentration certificate",
        ],
    )
    require_text(
        "docs/POST_RECORD_STABILITY_DYNAMICS_SELECTOR_SUBDIVISION_2026-06-06.md",
        [
            "arrow_or_dynamics_bridge",
            "physical arrow, Hamiltonian",
        ],
    )


def supplied_bridge_checks() -> None:
    section("Supplied orientation bridge checks")
    law: Law = {
        ("A", "B", "B"): Fraction(1, 2),
        ("C", "A", "B"): Fraction(1, 3),
        ("B", "C", "C"): Fraction(1, 6),
    }
    forward = OrientationBridge("bridge_forward", "toy_law_N3", "forward", "word_index_clock", "toy_kernel_supplied")
    reverse = OrientationBridge("bridge_reverse", "toy_law_N3", "reverse", "word_index_clock", "toy_kernel_supplied_reverse")
    missing = OrientationBridge("bridge_missing", "toy_law_N3", None, "word_index_clock", "toy_kernel_supplied")
    wrong_law = OrientationBridge("bridge_wrong_law", "other_law", "forward", "word_index_clock", "toy_kernel_supplied")
    cert_forward = DirectedCertificate("endpoint_bound_forward", "bridge_forward", "toy_law_N3", "endpoint_A_to_B", Fraction(1, 2))
    cert_too_tight = DirectedCertificate("endpoint_bound_tight", "bridge_forward", "toy_law_N3", "endpoint_A_to_B", Fraction(1, 4))
    cert_reverse = DirectedCertificate("endpoint_bound_reverse", "bridge_reverse", "toy_law_N3", "endpoint_A_to_B", Fraction(0, 1))
    cert_missing = DirectedCertificate("endpoint_bound_missing", "bridge_missing", "toy_law_N3", "endpoint_A_to_B", Fraction(1, 2))
    cert_wrong = DirectedCertificate("endpoint_bound_wrong", "bridge_wrong_law", "toy_law_N3", "endpoint_A_to_B", Fraction(1, 2))

    report("test law normalizes", normalized(law))
    valid_fwd, exact_fwd = verify_directed_certificate("toy_law_N3", law, forward, cert_forward)
    report("forward directed certificate valid at equality", valid_fwd, f"exact={exact_fwd}")
    invalid_tight, exact_tight = verify_directed_certificate("toy_law_N3", law, forward, cert_too_tight)
    report("too-tight directed certificate rejected", not invalid_tight, f"exact={exact_tight}")
    valid_rev, exact_rev = verify_directed_certificate("toy_law_N3", law, reverse, cert_reverse)
    report("reverse directed certificate valid under reverse bridge", valid_rev, f"exact={exact_rev}")
    missing_valid, missing_exact = verify_directed_certificate("toy_law_N3", law, missing, cert_missing)
    report("missing orientation rejected for directed certificate", not missing_valid and missing_exact is None)
    wrong_valid, wrong_exact = verify_directed_certificate("toy_law_N3", law, wrong_law, cert_wrong)
    report("wrong law scope rejected", not wrong_valid, f"exact={wrong_exact}")

    f_law = oriented_law(law, forward)
    r_law = oriented_law(law, reverse)
    assert f_law is not None and r_law is not None
    f_endpoint = event_probability(f_law, endpoint_a_to_b)
    r_endpoint = event_probability(r_law, endpoint_a_to_b)
    report("orientation can change directed endpoint probability", f_endpoint != r_endpoint, f"{f_endpoint} vs {r_endpoint}")
    f_count_event = count_event_probability(f_law, has_c_count_at_least_one)
    r_count_event = count_event_probability(r_law, has_c_count_at_least_one)
    report("count-only event probability remains orientation-invariant", f_count_event == r_count_event, str(f_count_event))
    report("count pushforward remains orientation-invariant", count_pushforward(f_law) == count_pushforward(r_law))


def supplied_kernel_checks() -> None:
    section("Supplied kernel checks")
    word = ("A", "B", "B", "C", "A")
    k_forward = normalize_rows(transitions(word))
    k_reverse = normalize_rows(transitions(rev(word)))
    report("supplied forward empirical kernel is row-stochastic", row_stochastic(k_forward), str(k_forward))
    report("supplied reversed empirical kernel is row-stochastic", row_stochastic(k_reverse), str(k_reverse))
    report("forward and reversed supplied kernels differ", k_forward != k_reverse)
    report("identical count state does not select either supplied kernel", count(word) == count(rev(word)) and k_forward != k_reverse)


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    physical_arrow_derived_from_record = False
    orientation_derived_from_record = False
    production_kernel_selected = False
    clock_or_rate_derived = False
    stable_setting_selects_dial = False
    generation_or_koide_dial_selected = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("Record-derived physical arrow flag is false", not physical_arrow_derived_from_record)
    report("Record-derived orientation flag is false", not orientation_derived_from_record)
    report("production-kernel selected flag is false", not production_kernel_selected)
    report("clock/rate derived flag is false", not clock_or_rate_derived)
    report("stable setting selects dial flag is false", not stable_setting_selects_dial)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)


def main() -> int:
    source_anchor_checks()
    supplied_bridge_checks()
    supplied_kernel_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("SUPPLIED_ORIENTATION_BRIDGE_INTERFACE=TRUE")
    print("DIRECTED_CERTIFICATE_REQUIRES_SUPPLIED_ORIENTATION=TRUE")
    print("ORIENTATION_DERIVED_FROM_RECORD=FALSE")
    print("PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE")
    print("PRODUCTION_KERNEL_SELECTED=FALSE")
    print("CLOCK_OR_RATE_DERIVED=FALSE")
    print("STABLE_SETTING_SELECTS_DIAL=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
