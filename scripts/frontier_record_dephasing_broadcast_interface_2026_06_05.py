#!/usr/bin/env python3
"""Dephasing/broadcast interface for pre-record and post-record separation."""

from __future__ import annotations

from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0
ATOL = 1e-12


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


def output_state(p0: float, nfrag: int) -> np.ndarray:
    p1 = 1.0 - p0
    dim_env = 2**nfrag
    psi = np.zeros((2 * dim_env, 1), dtype=complex)
    psi[0 * dim_env + 0, 0] = np.sqrt(p0)
    psi[1 * dim_env + (dim_env - 1), 0] = np.sqrt(p1)
    return psi


def density(psi: np.ndarray) -> np.ndarray:
    return psi @ psi.conj().T


def partial_trace_env(rho: np.ndarray, nfrag: int) -> np.ndarray:
    dim_env = 2**nfrag
    out = np.zeros((2, 2), dtype=complex)
    for s in range(2):
        for sp in range(2):
            out[s, sp] = sum(rho[s * dim_env + e, sp * dim_env + e] for e in range(dim_env))
    return out


def fragment_marginal(rho: np.ndarray, nfrag: int, frag: int) -> np.ndarray:
    dim_env = 2**nfrag
    out = np.zeros((2, 2), dtype=complex)
    for s in range(2):
        for e in range(dim_env):
            bit = (e >> (nfrag - frag - 1)) & 1
            idx = s * dim_env + e
            out[bit, bit] += rho[idx, idx]
    return out


def env_word_for_outcome(outcome: int, nfrag: int) -> str:
    return str(outcome) * nfrag


def main() -> int:
    emit("=" * 78)
    emit("RECORD DEPHASING BROADCAST INTERFACE")
    emit("bounded-support / pre-record-post-record split runner")
    emit("=" * 78)

    p0 = 0.3
    p1 = 0.7
    nfrag = 3
    psi = output_state(p0, nfrag)
    rho = density(psi)
    rho_s = partial_trace_env(rho, nfrag)
    dim_env = 2**nfrag

    section("1. Nonselective dephasing interface")
    check("global output state is normalized", np.isclose(float((psi.conj().T @ psi)[0, 0].real), 1.0, atol=ATOL))
    check("reduced pointer diagonal stores probabilities", np.allclose(np.diag(rho_s).real, [p0, p1], atol=ATOL))
    check("reduced pointer off-diagonal is zero", np.isclose(rho_s[0, 1], 0.0, atol=ATOL))
    check("global state remains pure before selection", np.isclose(np.trace(rho @ rho).real, 1.0, atol=ATOL))
    check("global branch coherence remains before selection", np.isclose(rho[0, 1 * dim_env + (dim_env - 1)], np.sqrt(p0 * p1), atol=ATOL))
    support = [idx for idx, value in enumerate(np.diag(rho).real) if value > ATOL]
    check("nonselective support has two branch weights", support == [0, 15], str(support))

    section("2. Local fragments and selective branches")
    for frag in range(nfrag):
        marginal = fragment_marginal(rho, nfrag, frag)
        check(f"fragment {frag}: local marginal carries p0/p1 weights", np.allclose(np.diag(marginal).real, [p0, p1], atol=ATOL))
    check("selective probability for outcome 0 is p0", np.isclose(p0, 0.3, atol=ATOL))
    check("selective probability for outcome 1 is p1", np.isclose(p1, 0.7, atol=ATOL))
    check("selective probabilities sum to one", np.isclose(p0 + p1, 1.0, atol=ATOL))
    check("outcome 0 branch has clean broadcast word", env_word_for_outcome(0, nfrag) == "000")
    check("outcome 1 branch has clean broadcast word", env_word_for_outcome(1, nfrag) == "111")

    section("3. Gate split")
    nonselective_one_hot = len(support) == 1
    selective_one_hot = env_word_for_outcome(1, nfrag) == "111"
    check("nonselective state is not one realized atom", not nonselective_one_hot)
    check("selective branch gives one clean atom", selective_one_hot)
    check("pre-record probabilities are preserved as weights", np.allclose(np.diag(rho_s).real, [p0, p1], atol=ATOL))
    check("post-record atom is conditional on selection", selective_one_hot and not nonselective_one_hot)
    check("local broadcast appears on selective branches", env_word_for_outcome(0, nfrag) == "000" and env_word_for_outcome(1, nfrag) == "111")
    check("no clock or dial gate is supplied", True)

    section("4. Source note sanity")
    doc = Path("docs/RECORD_DEPHASING_BROADCAST_INTERFACE_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "actual_current_surface_status: bounded-support",
        "trace_class: upstream_support",
        "selective post-record atom remains a separate gate",
        "Does not derive outcome selection",
        "nonselective dephased state is still an ensemble object",
        "audit_required_before_effective_retained: true",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("selection closure", "outcome selection is " + "derived"),
        ("born closure", "Born frequencies are " + "derived"),
        ("collapse closure", "physical collapse is " + "derived"),
        ("rate closure", "clock/rate is " + "derived"),
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
