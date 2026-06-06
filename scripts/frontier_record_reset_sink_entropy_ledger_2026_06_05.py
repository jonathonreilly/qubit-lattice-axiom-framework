#!/usr/bin/env python3
"""Finite entropy ledger for reset-with-sink record production."""

from __future__ import annotations

from math import log2
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


def reset_with_sink(s: str, old_fragments: str, sink: str) -> tuple[str, str, str]:
    clean_fragments = "".join(str(int(bit) ^ int(s)) for bit in sink)
    return s, clean_fragments, old_fragments


def clean_broadcast(s: str, fragments: str) -> bool:
    return all(bit == s for bit in fragments)


def entropy_bits(labels: set[tuple[str, ...]]) -> float:
    return log2(len(labels))


def main() -> int:
    emit("=" * 78)
    emit("RECORD RESET SINK ENTROPY LEDGER")
    emit("bounded-support / finite information-accounting runner")
    emit("=" * 78)

    section("1. Reversible ledger by fragment count")
    for k in range(1, 6):
        blank_inputs = [(s, e, "0" * k) for s in "01" for e in bitstrings(k)]
        full_outputs = {reset_with_sink(s, e, g) for s, e, g in blank_inputs}
        visible_outputs = {(s_out, clean) for s_out, clean, _old in full_outputs}
        sink_by_pointer = {
            s: {old for s_out, _clean, old in full_outputs if s_out == s}
            for s in "01"
        }
        reblanked_outputs = {
            (s_out, clean, "0" * k) for s_out, clean, _old in full_outputs
        }

        check(f"k={k}: blank input support has 2^(k+1) labels", len(blank_inputs) == 2 ** (k + 1))
        check(f"k={k}: full output support preserves cardinality", len(full_outputs) == len(blank_inputs))
        check(f"k={k}: all visible outputs are clean broadcasts", all(clean_broadcast(s, clean) for s, clean in visible_outputs))
        check(f"k={k}: visible clean record has two labels", len(visible_outputs) == 2)
        check(f"k={k}: sink stores 2^k labels for pointer 0", len(sink_by_pointer["0"]) == 2**k)
        check(f"k={k}: sink stores 2^k labels for pointer 1", len(sink_by_pointer["1"]) == 2**k)
        check(f"k={k}: full entropy is k+1 bits", entropy_bits(full_outputs) == k + 1, f"{entropy_bits(full_outputs):.1f}")
        check(f"k={k}: visible entropy is one bit", entropy_bits(visible_outputs) == 1, f"{entropy_bits(visible_outputs):.1f}")
        check(f"k={k}: hidden old-fragment ledger is k bits", entropy_bits({(old,) for old in sink_by_pointer['0']}) == k, f"{entropy_bits({(old,) for old in sink_by_pointer['0']}):.1f}")
        check(f"k={k}: reblanking sink is many-to-one", len(reblanked_outputs) == 2)

    section("2. k=3 witness details")
    k = 3
    blank_inputs = [(s, e, "0" * k) for s in "01" for e in bitstrings(k)]
    witness_outputs = {inp: reset_with_sink(*inp) for inp in blank_inputs}
    check("k=3 witness has sixteen blank-sink inputs", len(blank_inputs) == 16)
    check("old fragment 101 is recoverable from sink for pointer 0", witness_outputs[("0", "101", "000")][2] == "101")
    check("old fragment 101 is recoverable from sink for pointer 1", witness_outputs[("1", "101", "000")][2] == "101")
    check("pointer 0 visible fragments reset to 000", witness_outputs[("0", "101", "000")][1] == "000")
    check("pointer 1 visible fragments reset to 111", witness_outputs[("1", "101", "000")][1] == "111")
    reblank_map = {
        output: (output[0], output[1], "000") for output in witness_outputs.values()
    }
    check("k=3 reblank map has sixteen domain labels", len(reblank_map) == 16)
    check("k=3 reblank map has two range labels", len(set(reblank_map.values())) == 2)
    check("k=3 reblank map loses three finite bits", entropy_bits(set(witness_outputs.values())) - entropy_bits(set(reblank_map.values())) == 3)

    section("3. Source note sanity")
    doc = Path("docs/RECORD_RESET_SINK_ENTROPY_LEDGER_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "actual_current_surface_status: bounded-support",
        "trace_class: upstream_support",
        "finite sink-memory ledger",
        "Does not derive sink blankness",
        "Does not identify finite support entropy with heat or action.",
        "audit_required_before_effective_retained: true",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("cost closure", "thermodynamic cost is " + "derived"),
        ("rate closure", "rates are " + "derived"),
        ("dial closure", "dial location is " + "selected"),
        ("heat identity", "finite support entropy " + "is heat"),
        ("audit verdict", "promoted to " + "retained"),
    ]
    for label, phrase in forbidden_wording:
        check(f"forbidden wording absent: {label}", phrase not in text)

    section("SCORECARD")
    emit(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
