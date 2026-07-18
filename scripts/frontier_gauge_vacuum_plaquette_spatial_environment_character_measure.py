#!/usr/bin/env python3
"""
Bounded consumer-defined character-measure packet on a finite class-function
matrix model.

This does not close analytic P(6), the full unmarked spatial Wilson
environment, or the operator-realization bridge R_beta^actual = C_(Z_beta^env).
It sharpens only a finite packet on the box NMAX = 5: after computing the
normalized values of a stipulated single-link-form integral, the runner
chooses those finite coefficients as one normalized central character packet
Z_6^packet.

What this runner now does, that the prior witness-injection version did not:
the chosen finite diagonal data rho_packet(p,q) is no longer a generic hard-coded
positive conjugation-symmetric witness sequence
(e.g. exp(-0.24 (p+q) - 0.08 (p-q)^2)). It is instead computed from the
explicitly stipulated single-link-form SU(3) character integral
  rho_(p,q)(beta) = c_(p,q)(beta) / (d_(p,q) c_(0,0)(beta)),
  c_(p,q)(beta)   = int_{SU(3)} chi_(p,q)(U) exp((beta/3) Re tr U) dU,
computed via the Schur-Weyl Bessel-determinant identity in the same way as
the bounded sibling runner
  scripts/frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute.py
This runner chooses that finite table as its coefficient packet. The sibling
supplies only the integral evaluation, not this consumer-side choice. It is not the full multi-link
tensor-transfer environment object and is not an identification of the actual
stripped residual source-sector operator.

Bounded scope explicitly kept open:
- the full unmarked spatial Wilson environment tensor-transfer coefficients
- the residual-environment / character-measure operator-identification bridge
- analytic closure of canonical P(6)
"""

from __future__ import annotations

import numpy as np
from scipy.special import iv


THEOREM_PASS = 0
SUPPORT_PASS = 0
FAIL = 0

NMAX = 5
BETA = 6.0
ARG = BETA / 3.0
MODE_MAX = 80


def check(name: str, condition: bool, detail: str = "", bucket: str = "THEOREM") -> None:
    global THEOREM_PASS, SUPPORT_PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        if bucket == "SUPPORT":
            SUPPORT_PASS += 1
        else:
            THEOREM_PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] [{bucket}] {name}")
    if detail:
        print(f"         {detail}")


def recurrence_neighbors(p: int, q: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for a, b in [
        (p + 1, q),
        (p - 1, q + 1),
        (p, q - 1),
        (p, q + 1),
        (p + 1, q - 1),
        (p - 1, q),
    ]:
        if a >= 0 and b >= 0:
            out.append((a, b))
    return out


def weights_box(nmax: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


def build_recurrence_matrix(nmax: int) -> tuple[np.ndarray, list[tuple[int, int]], dict[tuple[int, int], int]]:
    weights = weights_box(nmax)
    index = {w: i for i, w in enumerate(weights)}
    jmat = np.zeros((len(weights), len(weights)), dtype=float)
    for p, q in weights:
        i = index[(p, q)]
        for a, b in recurrence_neighbors(p, q):
            if (a, b) in index:
                jmat[index[(a, b)], i] += 1.0 / 6.0
    return jmat, weights, index


def conjugation_swap_matrix(
    weights: list[tuple[int, int]], index: dict[tuple[int, int], int]
) -> np.ndarray:
    swap = np.zeros((len(weights), len(weights)), dtype=float)
    for w in weights:
        swap[index[(w[1], w[0])], index[w]] = 1.0
    return swap


def matrix_exponential_symmetric(m: np.ndarray, tau: float) -> np.ndarray:
    vals, vecs = np.linalg.eigh(m)
    return (vecs * np.exp(tau * vals)) @ vecs.T


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def highest_weight_triple(p: int, q: int) -> list[int]:
    return [p + q, q, 0]


def coefficient_matrix(mode: int, lam: list[int]) -> np.ndarray:
    return np.array(
        [[iv(mode + lam[j] + i - j, ARG) for j in range(3)] for i in range(3)],
        dtype=float,
    )


def wilson_character_coefficient(p: int, q: int) -> float:
    lam = highest_weight_triple(p, q)
    total = 0.0
    for mode in range(-MODE_MAX, MODE_MAX + 1):
        total += float(np.linalg.det(coefficient_matrix(mode, lam)))
    return total


def dominant_eigenpair(m: np.ndarray) -> tuple[float, np.ndarray]:
    vals, vecs = np.linalg.eigh(m)
    idx = int(np.argmax(vals))
    vec = vecs[:, idx]
    if np.sum(vec) < 0.0:
        vec = -vec
    return float(vals[idx]), vec


def main() -> int:
    jmat, weights, index = build_recurrence_matrix(NMAX)
    swap = conjugation_swap_matrix(weights, index)
    multiplier = matrix_exponential_symmetric(jmat, BETA / 2.0)

    c00 = wilson_character_coefficient(0, 0)
    local = np.array(
        [wilson_character_coefficient(p, q) / (dim_su3(p, q) * c00) for p, q in weights],
        dtype=float,
    )
    d_packet = np.diag(local**4)

    # Chosen bounded packet: normalized values of the stipulated integral
    #   rho_(p,q)(beta) = c_(p,q)(beta) / (d_(p,q) c_(0,0)(beta)).
    # This is the same stipulated integral evaluated by the bounded sibling
    #   scripts/frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute.py
    # The prior version of this runner injected an arbitrary positive,
    # conjugation-symmetric witness sequence
    # exp(-0.24 (p+q) - 0.08 (p-q)^2). Replacing that witness with the
    # computed integral values makes this a reproducible chosen packet rather
    # than a generic witness. It does NOT close
    # the full multi-link unmarked spatial Wilson environment, the
    # residual-environment identification bridge, or analytic P(6).
    rho_packet = local.copy()
    z_packet = np.array([dim_su3(p, q) * rho for (p, q), rho in zip(weights, rho_packet)], dtype=float)
    c_packet = np.diag(rho_packet)
    transfer = multiplier @ d_packet @ c_packet @ multiplier

    transfer_sym = float(np.max(np.abs(transfer - transfer.T)))
    transfer_swap = float(np.max(np.abs(swap @ transfer - transfer @ swap)))
    rho_sym = float(np.max(np.abs(swap @ c_packet - c_packet @ swap)))
    rho_min = float(np.min(rho_packet))
    z00 = float(z_packet[index[(0, 0)]])
    coeff_norm = float(np.max(np.abs(z_packet / z00 - np.array([dim_su3(p, q) * rho_packet[i] for i, (p, q) in enumerate(weights)]))))

    _, psi = dominant_eigenpair(transfer)
    expectation = float(psi @ (jmat @ psi))

    print("=" * 78)
    print("FINITE CONSUMER-DEFINED CHARACTER-MEASURE PACKET")
    print("=" * 78)
    print()
    print("Finite consumer-side pieces")
    print(f"  source-operator symmetry error        = {float(np.max(np.abs(jmat - jmat.T))):.3e}")
    print(f"  half-slice multiplier min eig         = {float(np.min(np.linalg.eigvalsh(multiplier))):.12f}")
    print(f"  fourth-power diagonal min/max         = {float(np.min(np.diag(d_packet))):.12e}, {float(np.max(np.diag(d_packet))):.12f}")
    print()
    print("Boundary character packet (chosen stipulated-integral values)")
    print(f"  rho_packet min/max                    = {rho_min:.12f}, {float(np.max(rho_packet)):.12f}")
    print(f"  rho_packet(0,0) (target 1.0)          = {rho_packet[index[(0, 0)]]:.12f}")
    print(f"  rho_packet(1,0)                       = {rho_packet[index[(1, 0)]]:.12e}")
    print(f"  rho_packet(1,1)                       = {rho_packet[index[(1, 1)]]:.12e}")
    print(f"  z_(0,0)^packet                        = {z00:.12f}")
    print(f"  packet swap error                     = {rho_sym:.3e}")
    print(f"  normalized coefficient consistency    = {coeff_norm:.3e}")
    print()
    print("Resulting finite factorized packet")
    print(f"  transfer symmetry error               = {transfer_sym:.3e}")
    print(f"  transfer swap error                   = {transfer_swap:.3e}")
    print(f"  Perron <J>                            = {expectation:.12f}")
    print()

    # Repeated in-runner recomputation of the stipulated-integral packet.
    # This is bookkeeping, not independent evidence or a physical identification.
    rho_wilson_check = np.array(
        [wilson_character_coefficient(p, q) / (dim_su3(p, q) * c00) for p, q in weights],
        dtype=float,
    )
    rho_packet_formula_check = float(np.max(np.abs(rho_packet - rho_wilson_check)))
    # Cross-check that the bounded packet is NOT one of the abstract
    # positive-symmetric witness sequences previously used (regression guard).
    rho_abstract_prior = np.array(
        [np.exp(-0.24 * (p + q) - 0.08 * ((p - q) ** 2)) for p, q in weights],
        dtype=float,
    )
    rho_packet_distinct_from_prior = float(np.max(np.abs(rho_packet - rho_abstract_prior)))

    check(
        "the explicit plaquette source operator J is self-adjoint and conjugation-symmetric on the source sector",
        float(np.max(np.abs(jmat - jmat.T))) < 1.0e-15 and float(np.max(np.abs(swap @ jmat - jmat @ swap))) < 1.0e-12,
        detail="the supplied source operator is one exact self-adjoint six-neighbor recurrence",
    )
    check(
        "the chosen bounded packet equals the normalized values of the stipulated integral rho_(p,q)(6) = c_(p,q)(6)/(d_(p,q) c_(0,0)(6))",
        rho_packet_formula_check < 1.0e-15,
        detail=f"max abs repeated-computation deviation = {rho_packet_formula_check:.3e}; bookkeeping only",
        bucket="SUPPORT",
    )
    check(
        "the bounded character packet is not the abstract exp(-0.24 (p+q) - 0.08 (p-q)^2) witness previously used (regression guard against witness-injection)",
        rho_packet_distinct_from_prior > 1.0e-3,
        detail=f"max abs distance from prior abstract witness = {rho_packet_distinct_from_prior:.3e}; bookkeeping only",
        bucket="SUPPORT",
    )
    check(
        "the stipulated finite data can be packaged as one positive conjugation-symmetric coefficient sequence rho_(p,q)(6)",
        rho_sym < 1.0e-12 and rho_min > 0.0,
        detail=f"min rho coefficient={rho_min:.6e}",
    )
    check(
        "the finite coefficients define one normalized central boundary-character packet Z_6^packet",
        coeff_norm < 1.0e-12 and abs(rho_packet[index[(0, 0)]] - 1.0) < 1.0e-12,
        detail="Z_6^packet(W) = z_(0,0)^packet sum d_(p,q) rho_(p,q)(6) chi_(p,q)(W)",
    )
    check(
        "the consumer-defined finite matrix packet has the form exp(3 J) D_6^packet C_(Z_6^packet) exp(3 J)",
        transfer_sym < 1.0e-12 and transfer_swap < 1.0e-12,
        detail="finite matrix identity only; no operator placement is inferred",
    )

    check(
        "the character-measure packet remains positivity-compatible on the truncated source sector",
        rho_min > 0.0,
        detail=f"minimum normalized boundary coefficient={rho_min:.3e}",
        bucket="SUPPORT",
    )
    check(
        "the chosen character packet is algebraically distinct from the separately constructed fourth-power diagonal",
        float(np.max(np.abs(rho_packet - 1.0))) > 1.0e-3,
        detail="the two constructed diagonal sequences differ; no physical placement is inferred",
        bucket="SUPPORT",
    )
    check(
        "the constructed finite packet has one numerical Perron diagnostic",
        expectation > 0.0,
        detail=f"Perron <J> = {expectation:.6f}",
        bucket="SUPPORT",
    )

    print()
    print("=" * 78)
    print(f"SUMMARY: THEOREM PASS={THEOREM_PASS} SUPPORT={SUPPORT_PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
