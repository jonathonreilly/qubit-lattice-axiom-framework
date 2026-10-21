---
claim_id: one_qubit_tick_update_covariance_limits_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Under the stated hypotheses (one qubit per site, translation invariance, nearest-neighbour range, spin-1/2 action of rotations): no nontrivial unitary update is covariant under all 24 proper cubic rotations; the split-step update's covariance group; and a same-site chirality mass leaving a cone ungapped. No no-go beyond these hypotheses."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/one_qubit_tick_update_covariance_limits_2026_10_21.py
---

# Covariance limits for one-qubit tick updates

Claim type: bounded_theorem.
Primary runner: `scripts/one_qubit_tick_update_covariance_limits_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md), which has zero premise weight, leaves the tick update of the odds open. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) require the admissibility rule to be covariant under translations and proper cubic rotations. This note asks what that covariance permits for an update with one qubit per site, where a rotation acts on the qubit as the spin-1/2 rotation.

## No nearest-neighbour covariant update moves anything

Write the translation-invariant nearest-neighbour update as

    U(k) = A_0 + sum over the six neighbour vectors h of A_h exp(-i k.h).

Covariance means A_{Rh} = V_R A_h V_R^dag for every rotation R, where V_R is its spin rotation.

- **The on-site term A_0** commutes with every V_R, so by Schur's lemma it is a multiple a of the identity.
- **The hop A_{e_z}** commutes with the quarter-turns about z, so it lies in the span of I and sigma_z: b I + c sigma_z.
- **The other hops** follow by covariance. The half-turn about x gives A_{-e_z} = b I - c sigma_z, and the threefold rotations carry z to x and y.

Hence

    U(k) = (a + 2b sum_i cos k_i) I - 2i c sum_i sin k_i sigma_i.

A unitary U must have unit identity component, |alpha|^2 + |beta|^2 = 1. In terms of c_i = cos k_i:

- the coefficient of c_x c_y is 8|b|^2, so it vanishes only if b = 0;
- the coefficient of c_x^2 is then -4|c|^2, so c = 0.

Only U = a I remains, which moves nothing. The runner checks these coefficients symbolically. It also checks that the ansatz is covariant for arbitrary complex a, b and c.

## The split-step update

The update S_z S_y S_x, with S_i = cos k_i - i sigma_i sin k_i, reaches beyond nearest neighbours. Its spectrum is invariant under 12 of the 24 rotations. As an operator it is covariant, with the spin rotation, under 4 of them. The quarter-turns map it to the opposite-order product, which has the opposite chirality.

## Mass and the doubler

Form the two-chirality cell diag(S_z S_y S_x, S_x S_y S_z) and add the same-site chirality mass exp(-i th beta). This gaps k = 0 by th. The cone at k = (pi/2)(1,1,1) stays at zero quasi-energy, so the mass leaves a massless doubler.

## Consequence and scope

Full covariance with one qubit per site therefore needs a larger cell or a coupling beyond nearest neighbours. A mass that removes the doubler must couple across momentum. These results hold only under the hypotheses stated. No matter content, general no-go or physical identification is established.
