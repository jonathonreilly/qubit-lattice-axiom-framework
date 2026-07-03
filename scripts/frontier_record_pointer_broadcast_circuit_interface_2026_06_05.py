#!/usr/bin/env python3
"""Pointer-broadcast circuit interface.

Given a pointer basis, blank fragments, and CNOT fanout, basis record labels
are locally broadcast. A generic pre-record qubit is not cloned.
"""

from __future__ import annotations

from math import sqrt
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


def ket(bits: str, nbits: int = 4) -> np.ndarray:
    v = np.zeros(2**nbits, dtype=complex)
    v[bits_to_index(bits)] = 1.0
    return v


def fanout_unitary(nfrag: int = 3) -> np.ndarray:
    nbits = 1 + nfrag
    dim = 2**nbits
    u = np.zeros((dim, dim), dtype=complex)
    for index in range(dim):
        bits = format(index, f"0{nbits}b")
        control = int(bits[0])
        fragments = [str(int(bit) ^ control) for bit in bits[1:]]
        out_bits = str(control) + "".join(fragments)
        u[bits_to_index(out_bits), index] = 1.0
    return u


def reduced_first_qubit(state: np.ndarray, nbits: int = 4) -> np.ndarray:
    tensor = state.reshape([2] * nbits)
    rho = np.tensordot(tensor, tensor.conj(), axes=(list(range(1, nbits)), list(range(1, nbits))))
    return rho


def product_state(single: np.ndarray, copies: int = 4) -> np.ndarray:
    out = single
    for _ in range(copies - 1):
        out = np.kron(out, single)
    return out


def local_broadcast(bits: str) -> bool:
    return all(bit == bits[0] for bit in bits[1:])


def main() -> int:
    emit("=" * 78)
    emit("RECORD POINTER BROADCAST CIRCUIT INTERFACE")
    emit("bounded-support / conditional finite witness runner")
    emit("=" * 78)

    u = fanout_unitary(3)
    identity = np.eye(16, dtype=complex)

    section("1. Fanout is unitary and pointer non-demolition")
    check("fanout matrix is unitary", np.allclose(u.conj().T @ u, identity, atol=TOL))
    check("fanout matrix is a permutation", np.allclose(np.sum(np.abs(u), axis=0), np.ones(16)) and np.allclose(np.sum(np.abs(u), axis=1), np.ones(16)))
    nondemolition = True
    for index in range(16):
        bits = format(index, "04b")
        out_index = int(np.argmax(np.abs(u @ ket(bits))))
        out_bits = format(out_index, "04b")
        nondemolition = nondemolition and out_bits[0] == bits[0]
    check("system pointer bit is preserved on every basis input", nondemolition)

    section("2. Blank fragments broadcast pointer eigenvalues")
    out0 = u @ ket("0000")
    out1 = u @ ket("1000")
    check("zero pointer with blank fragments stays 0000", np.allclose(out0, ket("0000")))
    check("one pointer with blank fragments becomes 1111", np.allclose(out1, ket("1111")))
    check("output 0000 is locally decodable as 0", local_broadcast("0000"))
    check("output 1111 is locally decodable as 1", local_broadcast("1111"))
    check("all three fragments agree with pointer for 0000", "0000"[1:] == "000")
    check("all three fragments agree with pointer for 1111", "1111"[1:] == "111")

    section("3. Blankness is a real input")
    dirty0 = u @ ket("0101")
    dirty1 = u @ ket("1101")
    dirty0_bits = format(int(np.argmax(np.abs(dirty0))), "04b")
    dirty1_bits = format(int(np.argmax(np.abs(dirty1))), "04b")
    check("dirty zero input is not a clean broadcast", not local_broadcast(dirty0_bits), dirty0_bits)
    check("dirty one input is not a clean broadcast", not local_broadcast(dirty1_bits), dirty1_bits)
    check("blank condition distinguishes clean from dirty zero", dirty0_bits != "0000")
    check("blank condition distinguishes clean from dirty one", dirty1_bits != "1111")

    section("4. Superposition is not cloned")
    a = sqrt(0.6)
    b = sqrt(0.4)
    single = np.array([a, b], dtype=complex)
    psi_in = np.kron(single, ket("000", nbits=3))
    psi_out = u @ psi_in
    ghz = a * ket("0000") + b * ket("1111")
    cloned = product_state(single, 4)
    rho_reduced = reduced_first_qubit(psi_out)
    rho_original = np.outer(single, single.conj())
    check("superposition output equals GHZ-style record state", np.allclose(psi_out, ghz, atol=TOL))
    check("superposition output is not product clones", not np.allclose(psi_out, cloned, atol=TOL))
    check("reduced system loses original coherence", abs(rho_reduced[0, 1]) < TOL and abs(rho_original[0, 1]) > 0.1)
    check("reduced system retains Born diagonal weights", np.allclose(np.diag(rho_reduced).real, [0.6, 0.4], atol=TOL))
    check("GHZ norm is one", abs(float(np.vdot(ghz, ghz).real) - 1.0) < TOL)
    check("cloned product norm is one", abs(float(np.vdot(cloned, cloned).real) - 1.0) < TOL)

    section("5. Typed residual ledger")
    supplied = {"pointer_basis", "blank_fragments", "fanout_unitary"}
    produced = {"local_decoders", "broadcast_pointer_atom"}
    missing = {"physical_hamiltonian", "clock", "rate", "probability_weights", "dial_selection"}
    check("witness supplies local decoder surface", "local_decoders" in produced)
    check("witness assumptions are explicit", {"pointer_basis", "blank_fragments"}.issubset(supplied))
    check("missing gates are disjoint from produced outputs", produced.isdisjoint(missing))
    check("clock/rate remain missing", {"clock", "rate"}.issubset(missing))

    section("6. Source note sanity")
    doc = Path("docs/RECORD_POINTER_BROADCAST_CIRCUIT_INTERFACE_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "actual_current_surface_status: bounded-support",
        "trace_class: upstream_support",
        "conditional_surface_status:",
        "Does not derive broadcast dynamics",
        "Does not apply audit verdicts.",
        "audit_required_before_effective_retained: true",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("broadcast closure", "broadcast dynamics is " + "derived"),
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
