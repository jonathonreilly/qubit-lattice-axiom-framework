#!/usr/bin/env python3
"""Record production residual checklist runner.

This runner classifies finite examples by gate:

kernel support, produced durable record, post-record history, local
observability, and clocked rate support. It does not derive any of those gates.
"""

from __future__ import annotations

from dataclasses import dataclass
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


@dataclass(frozen=True)
class GateModel:
    name: str
    instrument: bool = False
    kernel: bool = False
    realized_atom: bool = False
    durable: bool = False
    append_count: bool = False
    local_fragments: bool = False
    redundant: bool = False
    clock: bool = False
    rate: bool = False


def supports_kernel(model: GateModel) -> bool:
    return model.instrument and model.kernel


def supports_produced_record(model: GateModel) -> bool:
    return model.realized_atom and model.durable


def supports_history(model: GateModel) -> bool:
    return supports_produced_record(model) and model.append_count


def supports_local_observability(model: GateModel) -> bool:
    return supports_produced_record(model) and model.local_fragments and model.redundant


def supports_clocked_rate(model: GateModel) -> bool:
    return supports_produced_record(model) and model.clock and model.rate


def locally_readable(code: dict[int, set[str]]) -> bool:
    """Each fragment position determines the record value for all codewords."""
    width = len(next(iter(next(iter(code.values())))))
    for pos in range(width):
        seen: dict[str, set[int]] = {}
        for value, words in code.items():
            for word in words:
                seen.setdefault(word[pos], set()).add(value)
        if any(len(values) > 1 for values in seen.values()):
            return False
    return True


def main() -> int:
    emit("=" * 78)
    emit("RECORD PRODUCTION RESIDUAL CHECKLIST")
    emit("bounded-support / audit-checklist runner")
    emit("=" * 78)

    models = {
        "kernel_only": GateModel("kernel_only", instrument=True, kernel=True),
        "single_register": GateModel(
            "single_register",
            instrument=True,
            kernel=True,
            realized_atom=True,
            durable=True,
            append_count=True,
        ),
        "global_parity": GateModel(
            "global_parity",
            instrument=True,
            kernel=True,
            realized_atom=True,
            durable=True,
            append_count=True,
            local_fragments=True,
            redundant=False,
        ),
        "broadcast": GateModel(
            "broadcast",
            instrument=True,
            kernel=True,
            realized_atom=True,
            durable=True,
            append_count=True,
            local_fragments=True,
            redundant=True,
        ),
        "clocked_broadcast": GateModel(
            "clocked_broadcast",
            instrument=True,
            kernel=True,
            realized_atom=True,
            durable=True,
            append_count=True,
            local_fragments=True,
            redundant=True,
            clock=True,
            rate=True,
        ),
    }

    section("1. Gate classification examples")
    check("kernel-only supports kernel", supports_kernel(models["kernel_only"]))
    check("kernel-only does not produce record", not supports_produced_record(models["kernel_only"]))
    check("kernel-only does not support history", not supports_history(models["kernel_only"]))
    check("kernel-only does not support local observability", not supports_local_observability(models["kernel_only"]))
    check("kernel-only does not support clocked rates", not supports_clocked_rate(models["kernel_only"]))

    check("single register produces durable record", supports_produced_record(models["single_register"]))
    check("single register supports history append", supports_history(models["single_register"]))
    check("single register does not imply local observability", not supports_local_observability(models["single_register"]))
    check("single register does not imply clocked rates", not supports_clocked_rate(models["single_register"]))

    check("global parity produces a determined durable record", supports_produced_record(models["global_parity"]))
    check("global parity supports history append", supports_history(models["global_parity"]))
    check("global parity does not satisfy local observability", not supports_local_observability(models["global_parity"]))

    check("broadcast satisfies local observability", supports_local_observability(models["broadcast"]))
    check("broadcast does not imply clocked rates", not supports_clocked_rate(models["broadcast"]))
    check("clocked broadcast supports clocked rates", supports_clocked_rate(models["clocked_broadcast"]))

    section("2. Local readability finite-code witness")
    broadcast_code = {0: {"000"}, 1: {"111"}}
    parity_code = {
        0: {"000", "011", "101", "110"},
        1: {"001", "010", "100", "111"},
    }
    check("broadcast code is locally readable", locally_readable(broadcast_code))
    check("parity code is not locally readable", not locally_readable(parity_code))
    check("parity code has both global values", set(parity_code) == {0, 1})
    check("parity code needs full word to compute value", all((sum(int(bit) for bit in word) % 2) == value for value, words in parity_code.items() for word in words))
    check("single fragment 0 occurs in both parity values", any(word[0] == "0" for word in parity_code[0]) and any(word[0] == "0" for word in parity_code[1]))
    check("single fragment 1 occurs in both parity values", any(word[1] == "1" for word in parity_code[0]) and any(word[1] == "1" for word in parity_code[1]))

    section("3. Audit target dependency matrix")
    targets = {
        "probability_over_possible_records": {"instrument", "kernel"},
        "produced_record": {"realized_atom", "durable"},
        "post_record_history": {"realized_atom", "durable", "append_count"},
        "local_objective_record": {"realized_atom", "durable", "local_fragments", "redundant"},
        "physical_rate": {"realized_atom", "durable", "clock", "rate"},
    }
    check("five audit targets classified", len(targets) == 5)
    check("probability target does not require realized atom", "realized_atom" not in targets["probability_over_possible_records"])
    check("produced-record target does not require local fragments", "local_fragments" not in targets["produced_record"])
    check("history target requires append_count", "append_count" in targets["post_record_history"])
    check("local objective target requires redundancy", "redundant" in targets["local_objective_record"])
    check("physical rate target requires clock and rate", {"clock", "rate"}.issubset(targets["physical_rate"]))
    check("clock is not required for post-record history", "clock" not in targets["post_record_history"])
    check("redundancy is not required for physical rate target", "redundant" not in targets["physical_rate"])
    check("no target has empty dependency set", all(bool(reqs) for reqs in targets.values()))

    section("4. Source note sanity")
    doc = Path("docs/RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "actual_current_surface_status: bounded-support",
        "trace_class: upstream_support",
        "conditional_surface_status:",
        "Does not derive an instrument",
        "Does not identify nonselective density states with realized records.",
        "Does not select a generation/Koide dial setting.",
        "audit_required_before_effective_retained: true",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("instrument closure", "instrument is " + "derived"),
        ("production closure", "production law is " + "derived"),
        ("local observability closure", "local observability is " + "derived"),
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
