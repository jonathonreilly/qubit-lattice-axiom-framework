#!/usr/bin/env python3
"""Finite record-instrument kernel interface.

This runner verifies the typed bridge:

    pre-record state + supplied instrument
      -> probability kernel over possible record atoms
      -> selected branch state when one outcome is realized
      -> one-hot post-record atom/count update.

It does not derive the instrument, Born rule, reference state, local
observability, record production, rates, time, or a dial selection.
"""

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


def dagger(a: np.ndarray) -> np.ndarray:
    return a.conj().T


def tr(a: np.ndarray) -> complex:
    return np.trace(a)


def is_hermitian(a: np.ndarray) -> bool:
    return np.allclose(a, dagger(a), atol=TOL)


def min_eig(a: np.ndarray) -> float:
    return float(np.min(np.linalg.eigvalsh((a + dagger(a)) / 2)))


def is_positive(a: np.ndarray) -> bool:
    return min_eig(a) >= -1e-9


def is_density(a: np.ndarray) -> bool:
    return is_hermitian(a) and is_positive(a) and abs(tr(a).real - 1.0) < TOL


def probabilities(rho: np.ndarray, kraus: list[np.ndarray]) -> np.ndarray:
    return np.array([tr(k @ rho @ dagger(k)).real for k in kraus])


def branch_state(rho: np.ndarray, k: np.ndarray, p: float) -> np.ndarray:
    return k @ rho @ dagger(k) / p


def one_hot(n: int, i: int) -> np.ndarray:
    v = np.zeros(n)
    v[i] = 1.0
    return v


def main() -> int:
    emit("=" * 78)
    emit("RECORD INSTRUMENT KERNEL INTERFACE")
    emit("bounded-support / exact conditional finite-matrix runner")
    emit("=" * 78)

    section("1. Supplied instrument gives a probability kernel")
    rho = np.array(
        [
            [0.7, 0.2 + 0.1j],
            [0.2 - 0.1j, 0.3],
        ],
        dtype=complex,
    )
    gamma = 0.4
    k0 = np.array([[1.0, 0.0], [0.0, np.sqrt(1 - gamma)]], dtype=complex)
    k1 = np.array([[0.0, np.sqrt(gamma)], [0.0, 0.0]], dtype=complex)
    kraus = [k0, k1]
    identity = np.eye(2, dtype=complex)
    resolution = sum(dagger(k) @ k for k in kraus)
    effects = [dagger(k) @ k for k in kraus]
    mu = probabilities(rho, kraus)

    check("rho is Hermitian", is_hermitian(rho))
    check("rho is positive", is_positive(rho), f"min_eig={min_eig(rho):.6f}")
    check("rho has trace one", abs(tr(rho).real - 1.0) < TOL)
    check("instrument resolves identity", np.allclose(resolution, identity, atol=TOL))
    check("each effect is positive", all(is_positive(e) for e in effects))
    check("kernel entries are nonnegative", bool(np.all(mu >= -TOL)), str(mu.tolist()))
    check("kernel is normalized", abs(float(np.sum(mu)) - 1.0) < TOL, str(mu.tolist()))
    check("kernel is not a one-hot realized atom", not (np.allclose(mu, [1, 0]) or np.allclose(mu, [0, 1])))

    branches = [branch_state(rho, k, p) for k, p in zip(kraus, mu)]
    check("branch 0 is a density state", is_density(branches[0]))
    check("branch 1 is a density state", is_density(branches[1]))
    check("branch probabilities equal traces before normalization", abs(tr(k0 @ rho @ dagger(k0)).real - mu[0]) < TOL)
    check("nonselective state is trace one", abs(tr(sum(k @ rho @ dagger(k) for k in kraus)).real - 1.0) < TOL)
    check("nonselective density state is not a record atom object", sum(k @ rho @ dagger(k) for k in kraus).shape != one_hot(2, 0).shape)

    section("2. Realized record atom versus predictive expectation")
    count = np.array([2.0, 5.0])
    e0 = one_hot(2, 0)
    e1 = one_hot(2, 1)
    realized0 = count + e0
    realized1 = count + e1
    expected = count + mu
    check("realized atom e0 is one-hot", np.allclose(e0, [1, 0]))
    check("realized atom e1 is one-hot", np.allclose(e1, [0, 1]))
    check("realized update for outcome 0 is integral", np.allclose(realized0, np.round(realized0)), str(realized0.tolist()))
    check("realized update for outcome 1 is integral", np.allclose(realized1, np.round(realized1)), str(realized1.tolist()))
    check("predictive expected update is fractional", not np.allclose(expected, np.round(expected)), str(expected.tolist()))
    check("expected update is not either realized update", not np.allclose(expected, realized0) and not np.allclose(expected, realized1))
    delta = np.array([1.0, 0.0])
    check("delta kernel collapses to realized update", np.allclose(count + delta, realized0))

    section("3. Sequential instruments compose into a history kernel")
    p0 = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
    p1 = np.array([[0.0, 0.0], [0.0, 1.0]], dtype=complex)
    second = [p0, p1]
    second_resolution = sum(dagger(l) @ l for l in second)
    joint = np.zeros((2, 2))
    for r, k in enumerate(kraus):
        for s, l in enumerate(second):
            joint[r, s] = tr(l @ k @ rho @ dagger(k) @ dagger(l)).real
    conditionals = np.zeros((2, 2))
    for r in range(2):
        conditionals[r] = joint[r] / mu[r]
    history_atom = one_hot(4, 2)  # outcome word (1,0) in lexicographic order.

    check("second instrument resolves identity", np.allclose(second_resolution, identity, atol=TOL))
    check("joint history kernel entries are nonnegative", bool(np.all(joint >= -TOL)), str(joint.tolist()))
    check("joint history kernel is normalized", abs(float(np.sum(joint)) - 1.0) < TOL)
    check("joint marginal recovers first kernel", np.allclose(np.sum(joint, axis=1), mu, atol=TOL))
    check("conditional kernels normalize branchwise", np.allclose(np.sum(conditionals, axis=1), [1, 1], atol=TOL))
    check("joint equals first kernel times conditional", np.allclose(joint, mu[:, None] * conditionals, atol=TOL))
    check("history atom is one-hot in product alphabet", np.allclose(np.sum(history_atom), 1.0) and np.count_nonzero(history_atom) == 1)
    check("word append gives length two history labels", len(("jump", "z0")) == 2)

    section("4. Coarse-graining commutes with kernels and atoms")
    ka = np.sqrt(0.25) * p0
    kb = np.sqrt(0.75) * p0
    kc = p1
    split = [ka, kb, kc]
    split_resolution = sum(dagger(k) @ k for k in split)
    split_mu = probabilities(rho, split)
    coarse = np.array([[1.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    coarse_mu = coarse @ split_mu
    z_mu = np.array([rho[0, 0].real, rho[1, 1].real])
    split_counts = np.array([1.0, 2.0, 3.0])
    split_atom_b = one_hot(3, 1)
    split_atom_c = one_hot(3, 2)
    branch_a = branch_state(rho, ka, split_mu[0])
    branch_b = branch_state(rho, kb, split_mu[1])

    check("three-outcome split instrument resolves identity", np.allclose(split_resolution, identity, atol=TOL))
    check("split kernel is normalized", abs(float(np.sum(split_mu)) - 1.0) < TOL, str(split_mu.tolist()))
    check("coarse probability push-forward matches grouped outcomes", np.allclose(coarse_mu, z_mu, atol=TOL), str(coarse_mu.tolist()))
    check("coarse one-hot map sends split labels a,b to same atom", np.allclose(coarse @ one_hot(3, 0), coarse @ split_atom_b))
    check("coarse one-hot map sends label c to second atom", np.allclose(coarse @ split_atom_c, one_hot(2, 1)))
    check("coarse count update commutes for grouped label", np.allclose(coarse @ (split_counts + split_atom_b), coarse @ split_counts + coarse @ split_atom_b))
    check("coarse count update commutes for c label", np.allclose(coarse @ (split_counts + split_atom_c), coarse @ split_counts + coarse @ split_atom_c))
    check("split sublabels can share the same selective state", np.allclose(branch_a, branch_b, atol=TOL))

    section("5. Source note sanity")
    doc = Path("docs/RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "actual_current_surface_status: bounded-support",
        "trace_class: upstream_support",
        "conditional_surface_status:",
        "Does not derive a physical instrument",
        "Does not force a record-letter prior",
        "audit_required_before_effective_retained: true",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("instrument closure", "instrument is " + "derived"),
        ("atom/probability collapse", "record atom is " + "the probability"),
        ("expectation closure", "expected count is " + "a realized count"),
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
