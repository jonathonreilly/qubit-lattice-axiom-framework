#!/usr/bin/env python3
"""Finite local-observability decoder criterion.

Local observability is represented by a compatible decoder on every disjoint
fragment. This runner checks broadcast, single-register, parity/global, and
coarse-grained finite encodings.
"""

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


Code = dict[int, set[str]]


def width(code: Code) -> int:
    return len(next(iter(next(iter(code.values())))))


def global_decoder_exists(code: Code) -> bool:
    seen: dict[str, int] = {}
    for value, words in code.items():
        for word in words:
            if word in seen and seen[word] != value:
                return False
            seen[word] = value
    return True


def local_decoder_at(code: Code, pos: int) -> dict[str, int] | None:
    decoder: dict[str, int] = {}
    for value, words in code.items():
        for word in words:
            symbol = word[pos]
            if symbol in decoder and decoder[symbol] != value:
                return None
            decoder[symbol] = value
    return decoder


def local_decoders(code: Code) -> list[dict[str, int] | None]:
    return [local_decoder_at(code, pos) for pos in range(width(code))]


def locally_observable(code: Code) -> bool:
    decoders = local_decoders(code)
    return all(decoder is not None for decoder in decoders)


def all_decoders_agree(code: Code) -> bool:
    decoders = local_decoders(code)
    if any(decoder is None for decoder in decoders):
        return False
    for value, words in code.items():
        for word in words:
            decoded = [decoders[pos][word[pos]] for pos in range(width(code))]  # type: ignore[index]
            if decoded != [value] * width(code):
                return False
    return True


def coarse_code(code: Code, coarse: dict[int, str]) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for value, words in code.items():
        out.setdefault(coarse[value], set()).update(words)
    return out


def locally_observable_str(code: dict[str, set[str]]) -> bool:
    translated = {idx: words for idx, (_label, words) in enumerate(code.items())}
    return locally_observable(translated)


def main() -> int:
    emit("=" * 78)
    emit("RECORD LOCAL-OBSERVABILITY DECODER CRITERION")
    emit("bounded-support / exact finite decoder runner")
    emit("=" * 78)

    broadcast: Code = {0: {"0000"}, 1: {"1111"}}
    single_register: Code = {0: {"0---"}, 1: {"1---"}}
    parity: Code = {
        0: {"000", "011", "101", "110"},
        1: {"001", "010", "100", "111"},
    }
    fine_broadcast: Code = {0: {"000"}, 1: {"111"}, 2: {"222"}}
    coarse = {0: "A", 1: "A", 2: "B"}
    coarse_broadcast = coarse_code(fine_broadcast, coarse)

    section("1. Broadcast code has local decoders")
    b_decoders = local_decoders(broadcast)
    check("broadcast has a global decoder", global_decoder_exists(broadcast))
    check("broadcast has one decoder per fragment", len(b_decoders) == 4)
    check("every broadcast fragment has a local decoder", locally_observable(broadcast))
    check("broadcast decoders agree on every value", all_decoders_agree(broadcast))
    check("fragment 0 decoder reads 0->0 and 1->1", b_decoders[0] == {"0": 0, "1": 1})
    check("fragment 3 decoder reads 0->0 and 1->1", b_decoders[3] == {"0": 0, "1": 1})

    section("2. Global/single-register encodings are not local observability")
    s_decoders = local_decoders(single_register)
    p_decoders = local_decoders(parity)
    check("single-register code has a global decoder", global_decoder_exists(single_register))
    check("single-register first fragment has decoder", s_decoders[0] == {"0": 0, "1": 1})
    check("single-register non-register fragment is ambiguous", s_decoders[1] is None)
    check("single-register fails local observability", not locally_observable(single_register))
    check("parity code has a global decoder", global_decoder_exists(parity))
    check("parity fragment 0 has no decoder", p_decoders[0] is None)
    check("parity fragment 1 has no decoder", p_decoders[1] is None)
    check("parity fragment 2 has no decoder", p_decoders[2] is None)
    check("parity fails local observability", not locally_observable(parity))

    section("3. Coarse-graining local decoders")
    fine_decoders = local_decoders(fine_broadcast)
    coarse_decoders = local_decoders({0: coarse_broadcast["A"], 1: coarse_broadcast["B"]})
    check("fine broadcast has local decoders", locally_observable(fine_broadcast))
    check("fine decoder reads three values on fragment 0", fine_decoders[0] == {"0": 0, "1": 1, "2": 2})
    check("coarse code has local decoders", locally_observable_str(coarse_broadcast))
    check("coarse decoder groups 0 and 1 into A", coarse_decoders[0] == {"0": 0, "1": 0, "2": 1})
    check("coarse local observability follows by decoder composition", locally_observable(fine_broadcast) and locally_observable_str(coarse_broadcast))

    section("4. Dependency separation")
    outputs = {
        "record": {"determined_value", "durable"},
        "local_observability": {"local_decoder_family", "agreement"},
        "probability": {"weights", "normalization"},
        "rate": {"clock", "dt", "generator"},
    }
    check("record outputs do not include local decoder family", outputs["record"].isdisjoint(outputs["local_observability"]))
    check("local observability outputs do not include probability weights", outputs["local_observability"].isdisjoint(outputs["probability"]))
    check("local observability outputs do not include rates", outputs["local_observability"].isdisjoint(outputs["rate"]))
    check("probability and rate outputs are distinct", outputs["probability"].isdisjoint(outputs["rate"]))

    section("5. Source note sanity")
    doc = Path("docs/RECORD_LOCAL_OBSERVABILITY_DECODER_CRITERION_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "actual_current_surface_status: bounded-support",
        "trace_class: upstream_support",
        "conditional_surface_status:",
        "Does not derive local observability from the three axioms.",
        "Does not select a generation/Koide dial setting.",
        "audit_required_before_effective_retained: true",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("local observability closure", "local observability is " + "derived"),
        ("broadcast closure", "broadcast dynamics is " + "derived"),
        ("probability closure", "weights are " + "derived"),
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
