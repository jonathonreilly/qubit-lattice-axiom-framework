#!/usr/bin/env python3
"""Blank-boundary reset no-go for clean record broadcast."""

from __future__ import annotations

from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0
TOL = 1e-10


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


def bits_to_index(bits: str) -> int:
    return int(bits, 2)


def fanout_bits(bits: str) -> str:
    control = int(bits[0])
    return bits[0] + "".join(str(int(bit) ^ control) for bit in bits[1:])


def clean_broadcast(bits: str) -> bool:
    return all(bit == bits[0] for bit in bits[1:])


def reset_target(bits: str) -> str:
    return bits[0] + (bits[0] * 3)


def reset_matrix() -> np.ndarray:
    m = np.zeros((16, 16), dtype=complex)
    for index in range(16):
        bits = format(index, "04b")
        m[bits_to_index(reset_target(bits)), index] = 1.0
    return m


def main() -> int:
    emit("=" * 78)
    emit("RECORD BLANK-BOUNDARY RESET NO-GO")
    emit("exact negative boundary / finite-unitary runner")
    emit("=" * 78)

    all_bits = [format(i, "04b") for i in range(16)]
    blank_inputs = ["0000", "1000"]
    fanout_outputs = {bits: fanout_bits(bits) for bits in all_bits}

    section("1. Fanout is clean only on blank fragments")
    clean_inputs = [bits for bits in all_bits if clean_broadcast(fanout_outputs[bits])]
    check("blank zero input broadcasts cleanly", fanout_outputs["0000"] == "0000")
    check("blank one input broadcasts cleanly", fanout_outputs["1000"] == "1111")
    check("only blank inputs give clean broadcast", set(clean_inputs) == set(blank_inputs), str(clean_inputs))
    check("nonblank zero input fails clean broadcast", not clean_broadcast(fanout_outputs["0101"]), fanout_outputs["0101"])
    check("nonblank one input fails clean broadcast", not clean_broadcast(fanout_outputs["1101"]), fanout_outputs["1101"])
    check("fanout preserves old fragment data reversibly", len(set(fanout_outputs.values())) == 16)

    section("2. Closed clean reset is many-to-one")
    targets = [reset_target(bits) for bits in all_bits]
    zero_targets = {reset_target("0" + env) for env in [format(i, "03b") for i in range(8)]}
    one_targets = {reset_target("1" + env) for env in [format(i, "03b") for i in range(8)]}
    check("all zero-pointer env inputs collapse to one clean target", zero_targets == {"0000"})
    check("all one-pointer env inputs collapse to one clean target", one_targets == {"1111"})
    check("reset target set has size two", len(set(targets)) == 2, str(sorted(set(targets))))
    check("reset map is not injective", len(set(targets)) < len(targets))

    section("3. Matrix is not unitary/isometric")
    r = reset_matrix()
    gram = r.conj().T @ r
    rank = np.linalg.matrix_rank(r, tol=TOL)
    check("reset matrix has rank two", rank == 2, f"rank={rank}")
    check("reset matrix fails isometry condition", not np.allclose(gram, np.eye(16), atol=TOL))
    check("two orthogonal inputs share the same image", reset_target("0000") == reset_target("0001"))
    e0 = np.zeros(16); e0[bits_to_index("0000")] = 1
    e1 = np.zeros(16); e1[bits_to_index("0001")] = 1
    check("input pair is orthogonal", abs(float(np.vdot(e0, e1))) < TOL)
    image_overlap = np.vdot(r @ e0, r @ e1)
    check("image pair is not orthogonal", abs(float(image_overlap.real)) > 0.99)

    section("4. Extra sink restores injectivity at label level")
    sink_outputs = {(reset_target(bits), bits[1:]) for bits in all_bits}
    check("adding old fragment state as sink gives 16 labels", len(sink_outputs) == 16)
    check("sink labels keep clean broadcast target", all(clean_broadcast(target) for target, _sink in sink_outputs))
    check("sink route is not the closed four-qubit reset route", len(sink_outputs) > len(set(targets)))

    section("5. Source note sanity")
    doc = Path("docs/RECORD_BLANK_BOUNDARY_RESET_NO_GO_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "actual_current_surface_status: no-go",
        "trace_class: negative_route_pruning",
        "conditional_surface_status:",
        "Does not derive blank fragments",
        "Does not apply audit verdicts.",
        "audit_required_before_effective_retained: true",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("blank closure", "blank fragments are " + "derived"),
        ("reset closure", "erasure is " + "derived"),
        ("hamiltonian closure", "Hamiltonian is " + "derived"),
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
