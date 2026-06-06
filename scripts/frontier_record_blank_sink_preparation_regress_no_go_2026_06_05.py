#!/usr/bin/env python3
"""Blank-sink preparation regress no-go for record reset dynamics."""

from __future__ import annotations

from itertools import product
from math import floor, log2
from pathlib import Path


PASS = 0
FAIL = 0


def emit(line: str = "") -> None:
    print(line)


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    emit(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    emit()
    emit("-" * 78)
    emit(title)
    emit("-" * 78)


def bitstrings(width: int) -> list[str]:
    return [format(i, f"0{width}b") for i in range(2**width)]


def entropy_bits(labels: set[tuple[str, ...]]) -> float:
    return log2(len(labels))


def closed_blank(g: str) -> str:
    return "0" * len(g)


def outer_sink_blank(g: str, h: str) -> tuple[str, str]:
    return h, g


def main() -> int:
    emit("=" * 78)
    emit("RECORD BLANK-SINK PREPARATION REGRESS NO-GO")
    emit("no-go / finite capacity ledger runner")
    emit("=" * 78)

    section("1. Closed blanking is many-to-one")
    for k in range(1, 6):
        domain = bitstrings(k)
        closed_outputs = {closed_blank(g) for g in domain}
        outer_inputs = [(g, "0" * k) for g in domain]
        outer_outputs = {outer_sink_blank(g, h) for g, h in outer_inputs}

        check(f"k={k}: arbitrary old sink has 2^k labels", len(domain) == 2**k)
        check(f"k={k}: closed blanking range has one label", len(closed_outputs) == 1)
        check(f"k={k}: closed blanking is not injective", len(closed_outputs) < len(domain))
        check(f"k={k}: closed blanking loses k finite bits", log2(len(domain)) - log2(len(closed_outputs)) == k)
        check(f"k={k}: outer-sink blank-boundary domain has 2^k labels", len(outer_inputs) == 2**k)
        check(f"k={k}: outer-sink route preserves support", len(outer_outputs) == len(outer_inputs))
        check(f"k={k}: outer-sink route stores old word", all(out[1] == g for (g, _h), out in zip(outer_inputs, [outer_sink_blank(g, h) for g, h in outer_inputs])))
        check(f"k={k}: inner sink is blank after outer-sink route", all(out[0] == "0" * k for out in outer_outputs))

    section("2. Repeated clean resets require growing exported capacity")
    k = 3
    for cycles in range(1, 6):
        exported_words = {
            tuple(word_tuple)
            for word_tuple in product(bitstrings(k), repeat=cycles)
        }
        check(
            f"cycles={cycles}: exported support size is 2^(k*m)",
            len(exported_words) == 2 ** (k * cycles),
            str(len(exported_words)),
        )
        check(
            f"cycles={cycles}: exported capacity is k*m bits",
            entropy_bits({tuple(words) for words in exported_words}) == k * cycles,
            f"{entropy_bits({tuple(words) for words in exported_words}):.1f}",
        )

    for capacity_bits in (0, 3, 6, 9):
        max_cycles = floor(capacity_bits / k)
        next_cycles = max_cycles + 1
        check(
            f"B={capacity_bits}: max arbitrary cycles floor(B/k)",
            max_cycles == capacity_bits // k,
            str(max_cycles),
        )
        check(
            f"B={capacity_bits}: next cycle exceeds fixed capacity",
            k * next_cycles > capacity_bits,
            f"need {k * next_cycles}",
        )

    section("3. k=3 reset-stack witness")
    k = 3
    domain = bitstrings(k)
    closed_outputs = {closed_blank(g) for g in domain}
    outer_outputs = {outer_sink_blank(g, "0" * k) for g in domain}
    check("k=3 closed preparation collapses eight labels", len(domain) == 8 and len(closed_outputs) == 1)
    check("k=3 outer sink restores eight output labels", len(outer_outputs) == 8)
    check("k=3 old sink word 101 moves outward", outer_sink_blank("101", "000") == ("000", "101"))
    check("k=3 fixed 9-bit environment supports three cycles, not four", 3 * 3 <= 9 and 4 * 3 > 9)

    section("4. Source note sanity")
    doc = Path("docs/RECORD_BLANK_SINK_PREPARATION_REGRESS_NO_GO_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "actual_current_surface_status: no-go",
        "trace_class: negative_route_pruning",
        "closed finite blank-sink preparation",
        "Does not derive a low-record boundary",
        "Does not say open-system erasure is impossible.",
        "audit_required_before_effective_retained: true",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("boundary closure", "low-record boundary is " + "derived"),
        ("sink closure", "sink blankness is " + "derived"),
        ("cost closure", "thermodynamic cost is " + "derived"),
        ("rate closure", "rates are " + "derived"),
        ("dial closure", "dial location is " + "selected"),
        ("audit verdict", "promoted to " + "retained"),
    ]
    for label, phrase in forbidden_wording:
        check(f"forbidden wording absent: {label}", phrase not in text)

    section("SCORECARD")
    emit(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
