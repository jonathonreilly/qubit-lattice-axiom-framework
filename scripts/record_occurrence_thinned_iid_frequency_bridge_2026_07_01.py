#!/usr/bin/env python3
"""Self-contained verifier for a thinned-IID record-frequency bridge."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product
import math
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "RECORD_OCCURRENCE_THINNED_IID_FREQUENCY_BRIDGE_2026-07-01.md"

PASS = 0
FAIL = 0
BOT = "bot"


def flat(text: str) -> str:
    return " ".join(text.replace("`", "").replace("**", "").split())


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f" -- {detail}" if detail and not ok else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def section(title: str) -> None:
    print()
    print(title)


def kernel(a: Fraction, p: dict[str, Fraction]) -> dict[str, Fraction]:
    q = {BOT: 1 - a}
    for value, prob in p.items():
        q[value] = a * prob
    return q


def history_weight(history: tuple[str, ...], q: dict[str, Fraction]) -> Fraction:
    out = Fraction(1)
    for symbol in history:
        out *= q[symbol]
    return out


def enumerate_histories(q: dict[str, Fraction], n: int) -> list[tuple[tuple[str, ...], Fraction]]:
    symbols = list(q)
    return [(history, history_weight(history, q)) for history in product(symbols, repeat=n)]


def expectation(histories: list[tuple[tuple[str, ...], Fraction]], fn: Callable[[tuple[str, ...]], Fraction]) -> Fraction:
    return sum(weight * fn(history) for history, weight in histories)


def variance(histories: list[tuple[tuple[str, ...], Fraction]], fn: Callable[[tuple[str, ...]], Fraction]) -> Fraction:
    mean = expectation(histories, fn)
    return sum(weight * (fn(history) - mean) ** 2 for history, weight in histories)


def multinomial_probability(counts: dict[str, int], q: dict[str, Fraction]) -> Fraction:
    n = sum(counts.values())
    coeff = Fraction(math.factorial(n))
    for count in counts.values():
        coeff /= math.factorial(count)
    prob = coeff
    for symbol, count in counts.items():
        prob *= q[symbol] ** count
    return prob


def count_event_probability(histories: list[tuple[tuple[str, ...], Fraction]], target: dict[str, int]) -> Fraction:
    out = Fraction(0)
    for history, weight in histories:
        counts = Counter(history)
        if all(counts[symbol] == count for symbol, count in target.items()):
            out += weight
    return out


def conditional_recorded_mean(
    histories: list[tuple[tuple[str, ...], Fraction]],
    value: str,
    m: int,
) -> Fraction:
    numerator = Fraction(0)
    denominator = Fraction(0)
    for history, weight in histories:
        record_count = sum(1 for symbol in history if symbol != BOT)
        if record_count == m:
            denominator += weight
            numerator += weight * Fraction(history.count(value), m)
    return numerator / denominator


def conditional_recorded_variance(
    histories: list[tuple[tuple[str, ...], Fraction]],
    value: str,
    m: int,
) -> Fraction:
    mean = conditional_recorded_mean(histories, value, m)
    numerator = Fraction(0)
    denominator = Fraction(0)
    for history, weight in histories:
        record_count = sum(1 for symbol in history if symbol != BOT)
        if record_count == m:
            denominator += weight
            freq = Fraction(history.count(value), m)
            numerator += weight * (freq - mean) ** 2
    return numerator / denominator


def part1_one_attempt_kernel() -> tuple[dict[str, Fraction], dict[str, Fraction], Fraction]:
    section("PART 1: one-attempt thinned kernel")
    a = Fraction(1, 4)
    p = {"0": Fraction(3, 5), "1": Fraction(2, 5)}
    q = kernel(a, p)
    check("q(bot)=3/4", q[BOT] == Fraction(3, 4), q[BOT])
    check("q(0)=3/20", q["0"] == Fraction(3, 20), q["0"])
    check("q(1)=1/10", q["1"] == Fraction(1, 10), q["1"])
    check("kernel normalizes", sum(q.values(), Fraction(0)) == 1)
    check("activation recovered from non-bot mass", q["0"] + q["1"] == a)
    check("conditional p recovered from q/a", q["0"] / a == p["0"] and q["1"] / a == p["1"])
    check("bot mass is explicit no-record mass", q[BOT] == 1 - a)
    return q, p, a


def part2_exact_histories(q: dict[str, Fraction], p: dict[str, Fraction], a: Fraction) -> list[tuple[tuple[str, ...], Fraction]]:
    section("PART 2: exact finite-history enumeration")
    n = 4
    histories = enumerate_histories(q, n)
    f_bot = lambda h: Fraction(h.count(BOT), n)
    f_0 = lambda h: Fraction(h.count("0"), n)
    f_1 = lambda h: Fraction(h.count("1"), n)
    f_rec = lambda h: Fraction(n - h.count(BOT), n)

    check("all histories enumerated", len(histories) == 3**n)
    check("history weights normalize", sum(weight for _, weight in histories) == 1)
    check("E[F_bot]=1-a", expectation(histories, f_bot) == 1 - a)
    check("E[F_0]=a p0", expectation(histories, f_0) == a * p["0"])
    check("E[F_1]=a p1", expectation(histories, f_1) == a * p["1"])
    check("E[M/N]=a", expectation(histories, f_rec) == a)
    check("Var(F_bot)=a(1-a)/N", variance(histories, f_bot) == a * (1 - a) / n)
    check("Var(F_0)=q0(1-q0)/N", variance(histories, f_0) == q["0"] * (1 - q["0"]) / n)
    check("Var(F_1)=q1(1-q1)/N", variance(histories, f_1) == q["1"] * (1 - q["1"]) / n)
    check("Var(M/N)=a(1-a)/N", variance(histories, f_rec) == a * (1 - a) / n)
    return histories


def part3_count_laws(histories: list[tuple[tuple[str, ...], Fraction]], q: dict[str, Fraction], a: Fraction) -> None:
    section("PART 3: multinomial and zero-record laws")
    n = 4
    target_counts = {BOT: 2, "0": 1, "1": 1}
    enumerated = count_event_probability(histories, target_counts)
    closed_form = multinomial_probability(target_counts, q)
    check("enumerated count probability matches multinomial", enumerated == closed_form, (enumerated, closed_form))
    zero_counts = {BOT: n, "0": 0, "1": 0}
    check("P(M=0)=(1-a)^N", count_event_probability(histories, zero_counts) == (1 - a) ** n)
    record_count_law = {
        m: sum(weight for history, weight in histories if sum(1 for symbol in history if symbol != BOT) == m)
        for m in range(n + 1)
    }
    binomial_law = {
        m: Fraction(math.comb(n, m)) * a**m * (1 - a) ** (n - m)
        for m in range(n + 1)
    }
    check("record-count law is binomial", record_count_law == binomial_law)


def part4_recorded_only_conditionals(histories: list[tuple[tuple[str, ...], Fraction]], p: dict[str, Fraction]) -> None:
    section("PART 4: recorded-only conditional frequencies")
    for m in [1, 2, 3, 4]:
        check(f"E[G_0 | M={m}]=p0", conditional_recorded_mean(histories, "0", m) == p["0"])
        check(
            f"Var(G_0 | M={m})=p0(1-p0)/m",
            conditional_recorded_variance(histories, "0", m) == p["0"] * (1 - p["0"]) / m,
        )
    check("recorded-only statistic is intentionally undefined at M=0", "M>0" in NOTE.read_text(encoding="utf-8"))


def part5_special_cases(p: dict[str, Fraction]) -> None:
    section("PART 5: special cases")
    q_total = kernel(Fraction(1), p)
    check("a=1 has no bot mass", q_total[BOT] == 0)
    check("a=1 reduces to p on A", q_total["0"] == p["0"] and q_total["1"] == p["1"])
    q_zero = kernel(Fraction(0), p)
    check("a=0 has only bot mass", q_zero[BOT] == 1 and q_zero["0"] == 0 and q_zero["1"] == 0)
    zero_histories = enumerate_histories(q_zero, 3)
    check("a=0 always gives zero records", expectation(zero_histories, lambda h: Fraction(3 - h.count(BOT), 3)) == 0)


def part6_boundary_and_note() -> None:
    section("PART 6: note boundary")
    note = NOTE.read_text(encoding="utf-8")
    note_flat = flat(note)
    headings = [
        "## Claim",
        "## Finite Theorem",
        "## Explicit Witness",
        "## Boundary",
        "## Non-Claims",
        "## No-Go Discipline",
        "## Verification",
    ]
    for heading in headings:
        check(f"note includes {heading}", heading in note)
    markers = [
        "supplied occurrence kernel",
        "supplied IID reset/preparation protocol",
        "does not derive a, p",
        "Rows that count only recorded tokens",
        "sparse records do not force a total-record model",
        "This is not an audit verdict",
    ]
    for marker in markers:
        check(f"note contains marker: {marker}", marker in note_flat)
    required_open = [
        "the record-writing instrument or trigger",
        "the activation law a",
        "the conditional selection law p",
        "IID reset/preparation between repeated attempts",
        "clock/rate normalization",
        "local objectivity or redundant broadcast",
        "the physical observable/context being sampled",
    ]
    for marker in required_open:
        check(f"open supplier retained in boundary: {marker}", marker in note_flat)
    banned = [
        "../outputs/",
        ".claude/",
        "audited_clean",
        "current_status",
        "effective_status",
        "CLAIM_STATUS_CERTIFICATE",
        "retained",
        "therefore record occurrence is derived",
        "therefore every trial records",
        "therefore IID reset is derived",
        "therefore finite counts derive probabilities",
        "therefore empirical measurement semantics are closed",
    ]
    for marker in banned:
        check("banned marker absent from note", marker not in note_flat)


def main() -> int:
    print("Record occurrence thinned-IID frequency bridge")
    print("TRACE: bounded_sparse_frequency_normal_form")
    q, p, a = part1_one_attempt_kernel()
    histories = part2_exact_histories(q, p, a)
    part3_count_laws(histories, q, a)
    part4_recorded_only_conditionals(histories, p)
    part5_special_cases(p)
    part6_boundary_and_note()
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS -- supplied sparse activation plus IID reset gives thinned multinomial histories; occurrence and reset suppliers remain explicit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
