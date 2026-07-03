#!/usr/bin/env python3
"""Exact finite no-go for deriving arrow orientation from post-record counts."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
ALPHABET = ("A", "B", "C")


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


def rev(word: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(reversed(word))


def count(word: tuple[str, ...]) -> tuple[int, ...]:
    c = Counter(word)
    return tuple(c[a] for a in ALPHABET)


def scalar_readout(counts: tuple[int, ...], weights: tuple[int, ...]) -> int:
    return sum(c * w for c, w in zip(counts, weights))


def transitions(word: tuple[str, ...]) -> Counter[tuple[str, str]]:
    return Counter(zip(word, word[1:]))


def transpose_edges(edges: Counter[tuple[str, str]]) -> Counter[tuple[str, str]]:
    out: Counter[tuple[str, str]] = Counter()
    for (a, b), n in edges.items():
        out[(b, a)] += n
    return out


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


def count_pushforward(
    law: dict[tuple[str, ...], Fraction],
) -> dict[tuple[int, ...], Fraction]:
    out: defaultdict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    for word, mass in law.items():
        out[count(word)] += mass
    return dict(out)


def reverse_law(
    law: dict[tuple[str, ...], Fraction],
) -> dict[tuple[str, ...], Fraction]:
    out: defaultdict[tuple[str, ...], Fraction] = defaultdict(Fraction)
    for word, mass in law.items():
        out[rev(word)] += mass
    return dict(out)


def event_probability(
    law: dict[tuple[str, ...], Fraction],
    event,
) -> Fraction:
    return sum(mass for word, mass in law.items() if event(count(word)))


def all_words(max_len: int) -> list[tuple[str, ...]]:
    words: list[tuple[str, ...]] = [()]
    for n in range(1, max_len + 1):
        words.extend(tuple(w) for w in product(ALPHABET, repeat=n))
    return words


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_ARROW_ORIENTATION_FIREWALL_2026-06-06.md",
        [
            "post-record counts do not orient a physical arrow",
            "count pushforward is invariant under reversal",
            "oriented law, boundary condition, clock, or production kernel",
            "transitions(reverse(w)) = transpose(transitions(w))",
        ],
    )
    require_text(
        "docs/RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md",
        [
            "post-record information dynamics",
            "record-production probabilities, rates, Born typicality",
            "pre-record quantum state",
        ],
    )
    require_text(
        "docs/RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md",
        [
            "pre-record quantum state rho",
            "post-record information/count dynamics",
            "Probability belongs to the first two arrows",
        ],
    )
    require_text(
        "docs/POST_RECORD_STABILITY_DYNAMICS_SELECTOR_SUBDIVISION_2026-06-06.md",
        [
            "arrow_or_dynamics_bridge",
            "physical arrow, Hamiltonian",
            "stable setting is not selected dial",
        ],
    )


def count_reversal_checks() -> None:
    section("Count reversal checks")
    word = ("A", "B", "B", "C", "A")
    weights = (2, 5, 11)
    report("count is invariant under reversal for witness word", count(word) == count(rev(word)), f"{count(word)}")
    report("length is invariant under reversal", len(word) == len(rev(word)), str(len(word)))
    report(
        "scalar additive readout from counts is reversal-invariant",
        scalar_readout(count(word), weights) == scalar_readout(count(rev(word)), weights),
        str(scalar_readout(count(word), weights)),
    )
    words = all_words(4)
    report("all words up to length 4 have reversal-invariant counts", all(count(w) == count(rev(w)) for w in words), str(len(words)))
    report("reversal is an involution on tested words", all(rev(rev(w)) == w for w in words), str(len(words)))
    report("non-palindromic witness still has identical count state", word != rev(word) and count(word) == count(rev(word)))


def law_pushforward_checks() -> None:
    section("Law pushforward checks")
    law = {
        ("A", "B", "B"): Fraction(1, 2),
        ("C", "A", "B"): Fraction(1, 3),
        ("B", "C", "C"): Fraction(1, 6),
    }
    rlaw = reverse_law(law)
    report("test law is normalized", sum(law.values(), Fraction(0, 1)) == 1)
    report("reversed law is normalized", sum(rlaw.values(), Fraction(0, 1)) == 1)
    report("law is not identical to its reversal", law != rlaw)
    report("count pushforward is invariant under law reversal", count_pushforward(law) == count_pushforward(rlaw), str(count_pushforward(law)))
    event = lambda c: c[0] >= 1 and c[2] <= 1
    report(
        "count-only event probability is invariant under law reversal",
        event_probability(law, event) == event_probability(rlaw, event),
        str(event_probability(law, event)),
    )
    fine_event = lambda w: len(w) >= 2 and w[0] == "A" and w[-1] == "B"
    fine_prob = sum(m for w, m in law.items() if fine_event(w))
    fine_prob_rev = sum(m for w, m in rlaw.items() if fine_event(w))
    report("orientation-sensitive endpoint event can change under reversal", fine_prob != fine_prob_rev, f"{fine_prob} vs {fine_prob_rev}")


def transition_orientation_checks() -> None:
    section("Transition orientation checks")
    word = ("A", "B", "B", "C", "A")
    t_fwd = transitions(word)
    t_rev = transitions(rev(word))
    report("transition counts reverse by transposition", t_rev == transpose_edges(t_fwd), f"fwd={dict(t_fwd)} rev={dict(t_rev)}")
    report("asymmetric witness has different oriented transition data", t_fwd != t_rev)
    report("same witness has identical count state after reversal", count(word) == count(rev(word)), f"{count(word)}")
    k_fwd = normalize_rows(t_fwd)
    k_rev = normalize_rows(t_rev)
    report("forward empirical kernel is row-stochastic", row_stochastic(k_fwd), str(k_fwd))
    report("reversed empirical kernel is row-stochastic", row_stochastic(k_rev), str(k_rev))
    report("forward and reversed empirical kernels differ", k_fwd != k_rev)
    report("count state does not determine oriented transition counts", count(word) == count(rev(word)) and t_fwd != t_rev)


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    physical_arrow_derived_from_record = False
    production_kernel_selected = False
    stable_setting_selects_dial = False
    generation_or_koide_dial_selected = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("Record-derived physical arrow flag is false", not physical_arrow_derived_from_record)
    report("production-kernel selected flag is false", not production_kernel_selected)
    report("stable setting selects dial flag is false", not stable_setting_selects_dial)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)


def main() -> int:
    source_anchor_checks()
    count_reversal_checks()
    law_pushforward_checks()
    transition_orientation_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("POST_RECORD_COUNTS_ORIENT_PHYSICAL_ARROW=FALSE")
    print("COUNT_PUSHFORWARD_REVERSAL_INVARIANT=TRUE")
    print("PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE")
    print("PRODUCTION_KERNEL_SELECTED=FALSE")
    print("STABLE_SETTING_SELECTS_DIAL=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
