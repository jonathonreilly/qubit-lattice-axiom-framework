#!/usr/bin/env python3
"""Exact independence checks for the PMNS relative-action selector.

This runner tests the load-bearing negative boundary, not the conditional
PMNS optimizer.  It grants a positive matrix, a closure-feasible set, and the
log-det Legendre identity, then exhibits deterministic intrinsic selectors
that agree on all granted static data but select different feasible points.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PREMISE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {name}{suffix}")
    return condition


def relative_action(y: np.ndarray) -> float:
    if not np.allclose(y, y.conj().T, atol=1e-13, rtol=0.0):
        raise ValueError("relative-action argument must be Hermitian")
    if float(np.min(np.linalg.eigvalsh(y))) <= 0.0:
        raise ValueError("relative-action argument must be positive definite")
    sign, logdet = np.linalg.slogdet(y)
    if sign <= 0:
        raise ValueError("positive-definite matrix has invalid determinant sign")
    return float(np.trace(y).real - logdet - y.shape[0])


def frobenius_divergence(y: np.ndarray) -> float:
    delta = y - np.eye(y.shape[0])
    return float(np.trace(delta.conj().T @ delta).real)


def dual_value_at_stationary_source(y: np.ndarray) -> tuple[float, np.ndarray]:
    if not np.allclose(y, y.conj().T, atol=1e-13, rtol=0.0):
        raise ValueError("dual argument must be Hermitian")
    if float(np.min(np.linalg.eigvalsh(y))) <= 0.0:
        raise ValueError("dual argument must be positive definite")
    eye = np.eye(y.shape[0])
    k_star = np.linalg.inv(y) - eye
    sign, logdet = np.linalg.slogdet(eye + k_star)
    if sign <= 0:
        raise ValueError("dual stationary source left K > -I")
    value = float(logdet - np.trace(k_star @ y).real)
    return value, k_star


def block_diag(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    out = np.zeros((a.shape[0] + b.shape[0], a.shape[1] + b.shape[1]))
    out[: a.shape[0], : a.shape[1]] = a
    out[a.shape[0] :, a.shape[1] :] = b
    return out


def part1_foundation_firewall() -> None:
    print("\nPART 1: CURRENT FOUNDATION CONTAINS NO SELECTOR PREMISE")
    registry = json.loads(PREMISE_REGISTRY.read_text(encoding="utf-8"))
    expected = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    canonical = set(registry["canonical_ids"])
    check(
        "the supplied-premise registry is the reviewed four-node foundation",
        canonical == expected,
        f"canonical_ids={sorted(canonical)}",
    )

    nodes = registry["nodes"]
    minimal_text = (ROOT / nodes["minimal_axioms"]["current_path"]).read_text(encoding="utf-8")
    realized_text = (ROOT / nodes["realized_state_primitive"]["current_path"]).read_text(encoding="utf-8")
    kinetic_text = (ROOT / nodes["kinetic_isotropy_primitive"]["current_path"]).read_text(encoding="utf-8")
    scale_text = (ROOT / nodes["scale_reference_primitive"]["current_path"]).read_text(encoding="utf-8")

    check(
        "the minimal-axiom authority withholds log-det, source/action, and state selection",
        all(token in minimal_text for token in ("log-det", "source/action", "A law privileges no states")),
    )
    check(
        "the realized-state primitive grants evaluation but explicitly withholds selection",
        "This is pointwise evaluation, not a state-selection rule" in realized_text
        and "It does not supply a state, state-selection rule" in realized_text,
    )
    check(
        "the remaining approved primitives explicitly supply no selector",
        all(token in kinetic_text for token in ("no mass ratio", "selector", "is supplied"))
        and all(token in scale_text for token in ("no mass ratio", "selector", "is supplied")),
    )


def part2_legendre_identity_does_not_orient_selection() -> None:
    print("\nPART 2: EXACT TWO-COMPLETION SELECTOR WITNESS")
    y_a = np.diag([2.0, 1.0, 1.0])
    y_b = np.diag([3.0, 1.0, 1.0])
    # Explicit finite static packet: H_seed=I, the source domain is exactly
    # {Y_a,Y_b}, and the granted closure readout has C(Y_a)=C(Y_b)=0.
    # This is not a claim that these matrices lie on the numerical PMNS surface.
    feasible = [y_a, y_b]

    actions = np.array([relative_action(y) for y in feasible])
    expected = np.array([1.0 - math.log(2.0), 2.0 - math.log(3.0)])
    check(
        "the two closure-feasible positive matrices have the exact stated actions",
        np.max(np.abs(actions - expected)) < 1e-14,
        f"actions={actions}",
    )
    check(
        "minimum-action and maximum-action laws select different unique points",
        int(np.argmin(actions)) == 0 and int(np.argmax(actions)) == 1,
        f"argmin={np.argmin(actions)}, argmax={np.argmax(actions)}",
    )

    dual_residuals = []
    for y in feasible:
        dual, _k = dual_value_at_stationary_source(y)
        dual_residuals.append(abs(dual - relative_action(y)))
    check(
        "the same log-det Legendre identity holds at both differently selected points",
        max(dual_residuals) < 1e-14,
        f"max residual={max(dual_residuals):.3e}",
    )

    permutation = np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
    conjugated = [permutation @ y @ permutation.T for y in feasible]
    conjugated_actions = np.array([relative_action(y) for y in conjugated])
    check(
        "both selector laws are basis-covariant rather than label-privileging",
        np.max(np.abs(conjugated_actions - actions)) < 1e-14
        and int(np.argmin(conjugated_actions)) == 0
        and int(np.argmax(conjugated_actions)) == 1,
    )


def part3_naturality_does_not_choose_the_objective() -> None:
    print("\nPART 3: EXACT NATURAL-OBJECTIVE PREFERENCE REVERSAL")
    y_c = np.diag([0.1, 1.0, 1.0])
    y_d = np.diag([2.0, 2.0, 1.0])
    feasible = [y_c, y_d]
    action_values = np.array([relative_action(y) for y in feasible])
    frobenius_values = np.array([frobenius_divergence(y) for y in feasible])

    check(
        "relative action uniquely prefers the second feasible matrix",
        int(np.argmin(action_values)) == 1,
        f"S_rel={action_values}",
    )
    check(
        "a positive seed-zero spectral divergence uniquely prefers the first",
        int(np.argmin(frobenius_values)) == 0,
        f"D_F={frobenius_values}",
    )

    q = np.array([[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
    invariance_residual = max(
        abs(relative_action(q @ y @ q.T) - relative_action(y))
        + abs(frobenius_divergence(q @ y @ q.T) - frobenius_divergence(y))
        for y in feasible
    )
    check(
        "both objectives are invariant under orthogonal basis changes",
        invariance_residual < 1e-14,
        f"residual={invariance_residual:.3e}",
    )

    z = np.diag([1.5, 0.75])
    direct_sum_residual = max(
        abs(relative_action(block_diag(y, z)) - relative_action(y) - relative_action(z))
        + abs(
            frobenius_divergence(block_diag(y, z))
            - frobenius_divergence(y)
            - frobenius_divergence(z)
        )
        for y in feasible
    )
    check(
        "both objectives are additive on independent direct-sum blocks",
        direct_sum_residual < 1e-14,
        f"residual={direct_sum_residual:.3e}",
    )


def part4_source_free_minimum_is_the_seed() -> None:
    print("\nPART 4: THE SOURCE-FREE RELATIVE-ACTION MINIMUM IS THE SEED")
    eye = np.eye(3)
    direction = np.array([[2.0, 1.0, 0.0], [1.0, -1.0, 0.5], [0.0, 0.5, 1.0]])
    first_variation = float(np.trace((eye - np.linalg.inv(eye)) @ direction).real)
    second_variation = float(np.trace(direction @ direction).real)
    dual_at_seed, k_seed = dual_value_at_stationary_source(eye)

    check(
        "the first variation vanishes at Y=I",
        abs(first_variation) < 1e-15,
        f"D S[I](V)={first_variation:.3e}",
    )
    check(
        "the Hessian is strictly positive in a nonzero Hermitian direction",
        second_variation > 0.0,
        f"D2 S[I](V,V)={second_variation:.6f}",
    )
    check(
        "the seed has zero action and zero dual source",
        abs(relative_action(eye)) < 1e-15
        and abs(dual_at_seed) < 1e-15
        and np.linalg.norm(k_seed) < 1e-15,
    )


def main() -> int:
    print("DM LEPTOGENESIS PMNS RELATIVE-ACTION SELECTOR INDEPENDENCE")
    print("Exact claim: the current supplied foundation and static packet do not")
    print("entail that a physical off-seed source minimizes relative action.")

    part1_foundation_firewall()
    part2_legendre_identity_does_not_orient_selection()
    part3_naturality_does_not_choose_the_objective()
    part4_source_free_minimum_is_the_seed()

    print("\nRESULT")
    print("  The Legendre identity determines a functional pointwise.")
    print("  It does not supply an oriented physical source-selection law.")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    raise SystemExit(main())
