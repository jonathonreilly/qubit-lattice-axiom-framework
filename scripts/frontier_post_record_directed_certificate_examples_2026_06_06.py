#!/usr/bin/env python3
"""Exact finite rational reversal theorem and adversarial verification modes."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/POST_RECORD_DIRECTED_CERTIFICATE_EXAMPLES_2026-06-06.md"

Word = tuple[str, ...]
Law = dict[Word, Fraction]
Statistic = Callable[[Word], int]

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class FiniteCertificate:
    law_id: str
    orientation: str | None
    statistic_id: str
    kind: str
    expected: Fraction
    threshold: int | None = None


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
    print(f"\n{'-' * 78}\n{title}\n{'-' * 78}")


def reverse_word(word: Word) -> Word:
    return tuple(reversed(word))


def reverse_law(law: Law) -> Law:
    out: defaultdict[Word, Fraction] = defaultdict(Fraction)
    for word, mass in law.items():
        out[reverse_word(word)] += mass
    return dict(out)


def valid_law(law: Law) -> bool:
    return bool(law) and all(mass >= 0 for mass in law.values()) and sum(
        law.values(), Fraction(0)
    ) == 1


def expectation(law: Law, statistic: Statistic) -> Fraction:
    return sum(
        (mass * statistic(word) for word, mass in law.items()), Fraction(0)
    )


def distribution(law: Law, statistic: Statistic) -> dict[int, Fraction]:
    out: defaultdict[int, Fraction] = defaultdict(Fraction)
    for word, mass in law.items():
        out[statistic(word)] += mass
    return dict(sorted(out.items()))


def probability_cmp(
    law: Law, statistic: Statistic, threshold: int, relation: str
) -> Fraction:
    if relation == "gt":
        return sum(
            (mass for word, mass in law.items() if statistic(word) > threshold),
            Fraction(0),
        )
    if relation == "le":
        return sum(
            (mass for word, mass in law.items() if statistic(word) <= threshold),
            Fraction(0),
        )
    raise ValueError(f"unknown relation: {relation}")


def letter_count(word: Word) -> tuple[tuple[str, int], ...]:
    return tuple(sorted(Counter(word).items()))


def count_pushforward(law: Law) -> dict[tuple[tuple[str, int], ...], Fraction]:
    out: defaultdict[tuple[tuple[str, int], ...], Fraction] = defaultdict(Fraction)
    for word, mass in law.items():
        out[letter_count(word)] += mass
    return dict(out)


SIGNED_EDGES = {
    ("A", "B"): 1,
    ("B", "A"): -1,
    ("B", "C"): 1,
    ("C", "B"): -1,
}


def signed_drift(word: Word) -> int:
    return sum(SIGNED_EDGES.get(edge, 0) for edge in zip(word, word[1:]))


def marker_lag(word: Word) -> int:
    return word.index("M") if "M" in word else len(word)


def low_high_event(word: Word) -> int:
    return int(len(word) >= 2 and word[0] == "L" and word[-1] == "H")


STATISTICS: dict[str, Statistic] = {
    "signed_drift": signed_drift,
    "marker_lag": marker_lag,
    "low_high_event": low_high_event,
}

TRANSITION_LAW: Law = {
    ("A", "B", "C"): Fraction(1, 4),
    ("A", "C", "B"): Fraction(1, 4),
    ("B", "A", "C"): Fraction(1, 4),
    ("C", "B", "A"): Fraction(1, 4),
}
MARKER_LAW: Law = {
    ("A", "M", "B", "B"): Fraction(1, 2),
    ("A", "B", "M", "C"): Fraction(1, 3),
    ("M", "C", "A", "B"): Fraction(1, 6),
}
BOUNDARY_LAW: Law = {
    ("L", "A", "H"): Fraction(1, 2),
    ("H", "A", "L"): Fraction(1, 6),
    ("L", "B", "A"): Fraction(1, 3),
}

LAWS = {
    "transition": (TRANSITION_LAW, signed_drift),
    "marker": (MARKER_LAW, marker_lag),
    "boundary": (BOUNDARY_LAW, low_high_event),
}


def verify_certificate(
    law_id: str, law: Law, certificate: FiniteCertificate
) -> tuple[str, Fraction | None]:
    if not valid_law(law):
        return "invalid_law", None
    if certificate.orientation not in {"forward", "reversed"}:
        return "missing_orientation", None
    if certificate.law_id != law_id:
        return "scope_mismatch", None
    statistic = STATISTICS.get(certificate.statistic_id)
    if statistic is None:
        return "unknown_statistic", None
    oriented = law if certificate.orientation == "forward" else reverse_law(law)
    if certificate.kind == "expectation":
        value = expectation(oriented, statistic)
    elif certificate.kind == "probability_gt" and certificate.threshold is not None:
        value = probability_cmp(oriented, statistic, certificate.threshold, "gt")
    elif certificate.kind == "probability_le" and certificate.threshold is not None:
        value = probability_cmp(oriented, statistic, certificate.threshold, "le")
    else:
        return "invalid_certificate", None
    return ("verified", value) if value == certificate.expected else ("value_mismatch", value)


def source_boundary_checks() -> None:
    section("Source theorem and scope guards")
    text = NOTE.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    report("source note exists", NOTE.is_file())
    required = (
        "**Claim type:** positive_theorem",
        "E_mu_rev[f] = E_mu[f o rho]",
        "signed-transition drift: -1/2 forward, 1/2 reversed",
        "marker lag: 7/6 forward, 11/6 reversed",
        "low-to-high boundary event: 1/2 forward, 1/6 reversed",
        "a physical orientation or arrow",
        "Any physical use requires separate retained-grade bridge theorems.",
    )
    for needle in required:
        report(f"source contains: {needle}", needle in flat)
    forbidden = (
        "Record derives the orientation",
        "Record supplies the probability law",
        "the examples select a physical arrow",
        "arrow_or_dynamics_bridge bucket remains",
    )
    for phrase in forbidden:
        report(f"source excludes overclaim: {phrase}", phrase not in flat)


def general_law_checks() -> None:
    section("General reversal identities on all three laws")
    for law_id, (law, statistic) in LAWS.items():
        reversed_law = reverse_law(law)
        report(f"{law_id}: law is normalized", valid_law(law))
        report(f"{law_id}: all masses are nonnegative", all(m >= 0 for m in law.values()))
        report(f"{law_id}: reversed law is normalized", valid_law(reversed_law))
        report(f"{law_id}: reversal is involutive", reverse_law(reversed_law) == law)
        transport = expectation(reversed_law, statistic) == expectation(
            law, lambda word: statistic(reverse_word(word))
        )
        report(f"{law_id}: expectation transport identity", transport)
        report(
            f"{law_id}: letter-count pushforward is reversal invariant",
            count_pushforward(reversed_law) == count_pushforward(law),
        )


def transition_checks() -> None:
    section("Example 1: signed transition drift")
    law = TRANSITION_LAW
    reversed_law = reverse_law(law)
    expected_f = {-2: Fraction(1, 4), -1: Fraction(1, 2), 2: Fraction(1, 4)}
    expected_r = {-2: Fraction(1, 4), 1: Fraction(1, 2), 2: Fraction(1, 4)}
    report("transition forward distribution is exact", distribution(law, signed_drift) == expected_f)
    report("transition reversed distribution is exact", distribution(reversed_law, signed_drift) == expected_r)
    report("transition forward expectation is -1/2", expectation(law, signed_drift) == Fraction(-1, 2))
    report("transition reversed expectation is 1/2", expectation(reversed_law, signed_drift) == Fraction(1, 2))
    report("transition forward positive tail is 1/4", probability_cmp(law, signed_drift, 0, "gt") == Fraction(1, 4))
    report("transition reversed positive tail is 3/4", probability_cmp(reversed_law, signed_drift, 0, "gt") == Fraction(3, 4))
    report("transition count pushforwards agree", count_pushforward(law) == count_pushforward(reversed_law))
    forward = FiniteCertificate("transition", "forward", "signed_drift", "expectation", Fraction(-1, 2))
    reversed_cert = FiniteCertificate("transition", "reversed", "signed_drift", "expectation", Fraction(1, 2))
    bad = FiniteCertificate("transition", "forward", "signed_drift", "expectation", Fraction(0))
    wrong = FiniteCertificate("other", "forward", "signed_drift", "expectation", Fraction(-1, 2))
    missing = FiniteCertificate("transition", None, "signed_drift", "expectation", Fraction(-1, 2))
    report("transition forward certificate verifies", verify_certificate("transition", law, forward) == ("verified", Fraction(-1, 2)))
    report("transition reversed certificate verifies", verify_certificate("transition", law, reversed_cert) == ("verified", Fraction(1, 2)))
    report("transition wrong value is rejected", verify_certificate("transition", law, bad) == ("value_mismatch", Fraction(-1, 2)))
    report("transition wrong law id is rejected", verify_certificate("transition", law, wrong) == ("scope_mismatch", None))
    report("transition missing orientation is rejected", verify_certificate("transition", law, missing) == ("missing_orientation", None))


def marker_checks() -> None:
    section("Example 2: marker lag")
    law = MARKER_LAW
    reversed_law = reverse_law(law)
    expected_f = {0: Fraction(1, 6), 1: Fraction(1, 2), 2: Fraction(1, 3)}
    expected_r = {1: Fraction(1, 3), 2: Fraction(1, 2), 3: Fraction(1, 6)}
    report("marker forward distribution is exact", distribution(law, marker_lag) == expected_f)
    report("marker reversed distribution is exact", distribution(reversed_law, marker_lag) == expected_r)
    report("marker forward expectation is 7/6", expectation(law, marker_lag) == Fraction(7, 6))
    report("marker reversed expectation is 11/6", expectation(reversed_law, marker_lag) == Fraction(11, 6))
    report("marker forward lag<=1 probability is 2/3", probability_cmp(law, marker_lag, 1, "le") == Fraction(2, 3))
    report("marker reversed lag<=1 probability is 1/3", probability_cmp(reversed_law, marker_lag, 1, "le") == Fraction(1, 3))
    report("marker count pushforwards agree", count_pushforward(law) == count_pushforward(reversed_law))
    cert = FiniteCertificate("marker", "forward", "marker_lag", "expectation", Fraction(7, 6))
    tail = FiniteCertificate("marker", "forward", "marker_lag", "probability_le", Fraction(2, 3), 1)
    bad = FiniteCertificate("marker", "forward", "marker_lag", "probability_le", Fraction(1, 3), 1)
    report("marker expectation certificate verifies", verify_certificate("marker", law, cert) == ("verified", Fraction(7, 6)))
    report("marker tail certificate verifies", verify_certificate("marker", law, tail) == ("verified", Fraction(2, 3)))
    report("marker wrong tail value is rejected", verify_certificate("marker", law, bad) == ("value_mismatch", Fraction(2, 3)))


def boundary_checks() -> None:
    section("Example 3: low-to-high boundary event")
    law = BOUNDARY_LAW
    reversed_law = reverse_law(law)
    report("boundary forward distribution is exact", distribution(law, low_high_event) == {0: Fraction(1, 2), 1: Fraction(1, 2)})
    report("boundary reversed distribution is exact", distribution(reversed_law, low_high_event) == {0: Fraction(5, 6), 1: Fraction(1, 6)})
    report("boundary forward probability is 1/2", expectation(law, low_high_event) == Fraction(1, 2))
    report("boundary reversed probability is 1/6", expectation(reversed_law, low_high_event) == Fraction(1, 6))
    report("boundary event is reversal sensitive", expectation(law, low_high_event) != expectation(reversed_law, low_high_event))
    report("boundary count pushforwards agree", count_pushforward(law) == count_pushforward(reversed_law))
    forward = FiniteCertificate("boundary", "forward", "low_high_event", "expectation", Fraction(1, 2))
    reversed_cert = FiniteCertificate("boundary", "reversed", "low_high_event", "expectation", Fraction(1, 6))
    missing = FiniteCertificate("boundary", None, "low_high_event", "expectation", Fraction(1, 2))
    report("boundary forward certificate verifies", verify_certificate("boundary", law, forward) == ("verified", Fraction(1, 2)))
    report("boundary reversed certificate verifies", verify_certificate("boundary", law, reversed_cert) == ("verified", Fraction(1, 6)))
    report("boundary missing orientation is rejected", verify_certificate("boundary", law, missing) == ("missing_orientation", None))


def malformed_law_checks() -> None:
    section("Malformed-law rejection")
    cert = FiniteCertificate("bad", "forward", "signed_drift", "expectation", Fraction(0))
    report("empty law is rejected", verify_certificate("bad", {}, cert) == ("invalid_law", None))
    report("negative-mass law is rejected", verify_certificate("bad", {("A",): Fraction(2), ("B",): Fraction(-1)}, cert) == ("invalid_law", None))
    report("unnormalized law is rejected", verify_certificate("bad", {("A",): Fraction(1, 2)}, cert) == ("invalid_law", None))


def independent_mode() -> None:
    section("Independent direct-summation reconstruction")
    fixtures = (
        ([("ABC", 1, 4), ("ACB", 1, 4), ("BAC", 1, 4), ("CBA", 1, 4)], "drift", Fraction(-1, 2), Fraction(1, 2)),
        ([("AMBB", 1, 2), ("ABMC", 1, 3), ("MCAB", 1, 6)], "lag", Fraction(7, 6), Fraction(11, 6)),
        ([("LAH", 1, 2), ("HAL", 1, 6), ("LBA", 1, 3)], "event", Fraction(1, 2), Fraction(1, 6)),
    )

    def independent_stat(word: str, kind: str) -> int:
        if kind == "drift":
            scores = {"AB": 1, "BA": -1, "BC": 1, "CB": -1}
            return sum(scores.get(word[i : i + 2], 0) for i in range(len(word) - 1))
        if kind == "lag":
            return word.find("M") if "M" in word else len(word)
        return int(word.startswith("L") and word.endswith("H"))

    for rows, kind, expected_forward, expected_reversed in fixtures:
        total = sum((Fraction(n, d) for _, n, d in rows), Fraction(0))
        forward = sum((Fraction(n, d) * independent_stat(word, kind) for word, n, d in rows), Fraction(0))
        reversed_value = sum((Fraction(n, d) * independent_stat(word[::-1], kind) for word, n, d in rows), Fraction(0))
        forward_counts = Counter((tuple(sorted(Counter(word).items())), Fraction(n, d)) for word, n, d in rows)
        reversed_counts = Counter((tuple(sorted(Counter(word[::-1]).items())), Fraction(n, d)) for word, n, d in rows)
        report(f"{kind}: independent law normalizes", total == 1)
        report(f"{kind}: independent forward value", forward == expected_forward, str(forward))
        report(f"{kind}: independent reversed value", reversed_value == expected_reversed, str(reversed_value))
        report(f"{kind}: independent count data are reversal invariant", forward_counts == reversed_counts)


def hostile_mode() -> None:
    section("Hostile controls")
    cert = FiniteCertificate("transition", "forward", "signed_drift", "expectation", Fraction(-1, 2))
    report("hostile empty law rejected", verify_certificate("transition", {}, cert)[0] == "invalid_law")
    report("hostile unnormalized law rejected", verify_certificate("transition", {("A",): Fraction(2)}, cert)[0] == "invalid_law")
    report("hostile negative law rejected", verify_certificate("transition", {("A",): Fraction(2), ("B",): Fraction(-1)}, cert)[0] == "invalid_law")
    report("hostile wrong law id rejected", verify_certificate("other", TRANSITION_LAW, cert)[0] == "scope_mismatch")
    missing = FiniteCertificate("transition", None, "signed_drift", "expectation", Fraction(-1, 2))
    report("hostile missing orientation rejected", verify_certificate("transition", TRANSITION_LAW, missing)[0] == "missing_orientation")
    unknown = FiniteCertificate("transition", "forward", "unknown", "expectation", Fraction(0))
    report("hostile unknown statistic rejected", verify_certificate("transition", TRANSITION_LAW, unknown)[0] == "unknown_statistic")
    invalid = FiniteCertificate("transition", "forward", "signed_drift", "tail", Fraction(0))
    report("hostile invalid certificate kind rejected", verify_certificate("transition", TRANSITION_LAW, invalid)[0] == "invalid_certificate")
    bad = FiniteCertificate("transition", "forward", "signed_drift", "expectation", Fraction(99))
    report("hostile wrong expected value rejected", verify_certificate("transition", TRANSITION_LAW, bad) == ("value_mismatch", Fraction(-1, 2)))


MUTATIONS = (
    "drift_forward",
    "marker_reversed",
    "boundary_reversed",
    "count_pushforward",
    "source_scope",
)


def intentional_failure_mode(mutation: str) -> None:
    selected = MUTATIONS if mutation == "all" else (mutation,)
    section(f"Intentional-failure controls: {', '.join(selected)}")
    for item in selected:
        if item == "drift_forward":
            report("mutation drift forward expected as zero", expectation(TRANSITION_LAW, signed_drift) == 0)
        elif item == "marker_reversed":
            report("mutation marker reversed expected as 7/6", expectation(reverse_law(MARKER_LAW), marker_lag) == Fraction(7, 6))
        elif item == "boundary_reversed":
            report("mutation boundary reversed expected as 1/2", expectation(reverse_law(BOUNDARY_LAW), low_high_event) == Fraction(1, 2))
        elif item == "count_pushforward":
            damaged = {word[:-1]: mass for word, mass in TRANSITION_LAW.items()}
            report("mutation damaged map preserves count pushforward", count_pushforward(damaged) == count_pushforward(TRANSITION_LAW))
        elif item == "source_scope":
            mutated = NOTE.read_text(encoding="utf-8") + "\nRecord derives the orientation.\n"
            report("mutation source still excludes physical derivation", "Record derives the orientation" not in mutated)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("normal", "independent", "hostile", "intentional-failure"),
        default="normal",
    )
    parser.add_argument("--mutation", choices=("all",) + MUTATIONS, default="all")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.mode == "normal":
        source_boundary_checks()
        general_law_checks()
        transition_checks()
        marker_checks()
        boundary_checks()
        malformed_law_checks()
    elif args.mode == "independent":
        independent_mode()
    elif args.mode == "hostile":
        hostile_mode()
    else:
        intentional_failure_mode(args.mutation)

    print(f"\nSUMMARY: PASS={PASS} FAIL={FAIL}")
    if args.mode == "normal":
        print("FORMAL_DIRECTED_REVERSAL_THEOREM=TRUE")
        print("PHYSICAL_ORIENTATION_BRIDGE=OPEN")
        print("CLOCK_KERNEL_RECORD_DYNAMICS_BRIDGES=OPEN")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
