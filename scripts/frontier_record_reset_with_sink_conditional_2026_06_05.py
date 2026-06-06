#!/usr/bin/env python3
"""Reversible reset with explicit sink bits."""

from __future__ import annotations

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


def reset_with_sink(bits: str) -> str:
    """Input bits are s eee ggg. Output is s (g xor s)(g xor s)(g xor s) eee."""
    s = int(bits[0])
    e = bits[1:4]
    g = bits[4:7]
    new_fragments = "".join(str(int(bit) ^ s) for bit in g)
    return bits[0] + new_fragments + e


def clean_broadcast(bits: str) -> bool:
    return all(bit == bits[0] for bit in bits[1:4])


def main() -> int:
    emit("=" * 78)
    emit("RECORD RESET WITH EXPLICIT SINK CONDITIONAL")
    emit("bounded-support / reversible finite construction runner")
    emit("=" * 78)

    all_inputs = [format(i, "07b") for i in range(128)]
    outputs = {bits: reset_with_sink(bits) for bits in all_inputs}

    section("1. Map is reversible")
    check("all 128 inputs have outputs", len(outputs) == 128)
    check("output labels are unique", len(set(outputs.values())) == 128)
    check("pointer bit is preserved", all(bits[0] == out[0] for bits, out in outputs.items()))
    check("map is not many-to-one", len(set(outputs.values())) == len(outputs))

    section("2. Blank sink gives clean broadcast for arbitrary old fragments")
    blank_sink_inputs = [bits for bits in all_inputs if bits[4:7] == "000"]
    blank_outputs = [outputs[bits] for bits in blank_sink_inputs]
    check("there are sixteen pointer/fragment inputs with blank sink", len(blank_sink_inputs) == 16)
    check("all blank-sink outputs have clean broadcast fragments", all(clean_broadcast(out) for out in blank_outputs))
    check("old fragment memory is stored in sink", all(outputs[bits][4:7] == bits[1:4] for bits in blank_sink_inputs))
    check("zero pointer blank-sink outputs have 000 fragments", all(outputs[bits][1:4] == "000" for bits in blank_sink_inputs if bits[0] == "0"))
    check("one pointer blank-sink outputs have 111 fragments", all(outputs[bits][1:4] == "111" for bits in blank_sink_inputs if bits[0] == "1"))

    section("3. Nonblank sink is not a free clean reset")
    dirty_sink_inputs = [bits for bits in all_inputs if bits[4:7] != "000"]
    dirty_clean_count = sum(1 for bits in dirty_sink_inputs if clean_broadcast(outputs[bits]))
    check("dirty sink inputs exist", len(dirty_sink_inputs) == 112)
    check("not all dirty-sink outputs are clean", dirty_clean_count < len(dirty_sink_inputs), f"{dirty_clean_count}/{len(dirty_sink_inputs)}")
    check("example dirty sink can fail clean broadcast", not clean_broadcast(outputs["0000101"]), outputs["0000101"])
    check("sink blankness remains an input", dirty_clean_count != len(dirty_sink_inputs))

    section("4. Relation to no-go")
    closed_targets = {bits[0] + bits[0] * 3 for bits in [format(i, "04b") for i in range(16)]}
    sink_targets = {(outputs[bits][0:4], outputs[bits][4:7]) for bits in blank_sink_inputs}
    check("closed clean reset target set has size two", len(closed_targets) == 2)
    check("sink route keeps sixteen target+sink labels", len(sink_targets) == 16)
    check("sink labels refine the two clean targets", {target for target, _sink in sink_targets} == closed_targets)

    section("5. Source note sanity")
    doc = Path("docs/RECORD_RESET_WITH_SINK_CONDITIONAL_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "actual_current_surface_status: bounded-support",
        "trace_class: upstream_support",
        "conditional_surface_status:",
        "Does not derive sink blankness",
        "Does not apply audit verdicts.",
        "audit_required_before_effective_retained: true",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("sink closure", "sink blankness is " + "derived"),
        ("production closure", "production dynamics is " + "derived"),
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
