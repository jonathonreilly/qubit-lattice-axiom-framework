---
claim_id: dynamics_clause_the_covariant_plaquette_clause_is_frustration_free_exactly_at_the_rokhsar_kivelson_point_and_unrecorded_plaquettes_polarize_the_ice_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting: doubled coordinates with soldered link fields E_l = s_l . e_l (open PR 9066). A plaquette clause is a covariant generator on the four link sites around a plaquette site that commutes with the corner Gauss sums. (i) The eight rotations fixing a plaquette site split the 16 link configurations into four orbits (flippable 2, opposite 2, adjacent 4, odd 8). The covariant plaquette clauses are -g (U + U^dag) plus one potential per orbit. (ii) The members that annihilate the symmetric flippable state and every other configuration form one ray, g (P_flip - U - U^dag) = 2g |-><-| (positive for g >= 0): the Rokhsar-Kivelson projector. (iii) On the ice space, the sum of these projectors over plaquettes is the Laplacian of the plaquette-flip graph. Its zero-energy states are the uniform superpositions of the flip classes, so under the trace rule such a state records every configuration of its class with equal probability. On the coarse 2x2x2 torus there are 9600 ice states in 937 classes (largest 864, 760 frozen), and the pure-ring (V = 0) ground state on the largest class is not uniform. (iv) Take the exact-Gauss compression of the two-site clause at D = 0. An unrecorded plaquette qubit with cube-record field B n sees B n + J sum_l E_l e_l. Its energy is -B/2 on the flippable and opposite orbits, -sqrt(B^2 + J^2)/2 on odd and -sqrt(B^2 + 2 J^2)/2 on adjacent configurations. Summed over plaquettes, this is minimized on the 2x2x2 torus by exactly the 8 uniformly polarized ice states, which have no flippable plaquette. The plaquette clause, the Gauss law, soldering, the trace rule, the records and the dynamics clause are supplied, not adopted. No photon phase, flip-class structure on larger tori or physical identification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_the_covariant_plaquette_clause_and_the_rokhsar_kivelson_point_2026_09_24.py
---

# The covariant plaquette clause: frustration-free at the Rokhsar–Kivelson point

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** supplied models and finite certificates; unaudited.

## Result

Open PR 9066 showed that a U(1) link field moves only under a term of
Admissibility shape, such as a plaquette ring clause. This note looks at
that clause in the soldered setting.

- **Its form.** The covariant plaquette clause is a ring coupling `g` plus
  one potential for each of four orbits of link configurations.
- **Its frustration-free point.** Suppose each plaquette term annihilates
  the uniform ice state locally. Then the clause is the Rokhsar–Kivelson
  projector `2g |−⟩⟨−|`, which fixes `V = g`.
  - Summed over plaquettes, it is the Laplacian of the flip graph.
  - Its ground states are the uniform superpositions of the flip classes.
  - Read by the trace rule, they record uniform ice measures. These are
    the measures the landed positive-rule selection picks (below).
- **What the plaquette sites must do.** If they stay unrecorded, the
  two-site clause couples them to their links. Their energy then favours
  uniformly polarized ice, which has no flippable plaquette, at a scale far
  above the ring. For the ring to act, the plaquette sites must be recorded
  (open PR 9066's setting).

## Setting and decision points

- **Roles, soldering and Gauss law.** Doubled coordinates (D-roles); links
  soldered, with `E_l = s_l · ê_l` (D-sold); an exact Gauss law or its
  compression (D-gauss).
- **The plaquette clause.** A covariant generator on a plaquette site's
  four link neighbours that commutes with the corner Gauss sums (D-star).
- **Records and odds.** The trace rule (D-tr), the two-site clause (D-dyn),
  and records acting as fields (D-pattern).

None is adopted.

## Theorem 1 — four orbits and one ring

The eight rotations fixing a plaquette site act on the four link fields.
They permute the links, with a sign where a link's direction is reversed.
Written relative to the circulation around the plaquette, the 16
configurations fall into four orbits:

| Orbit | Size | Circulation pattern |
|---|---|---|
| flippable | 2 | all four along the circulation, or all four against |
| opposite | 2 | alternating |
| adjacent | 4 | two adjacent along, two against |
| odd | 8 | one against the other three |

The covariant plaquette clauses are
`−g (U + U†) + V_f P_flip + V_o P_opp + V_a P_adj + V_1 P_odd`. With the
ring, that is the five-parameter family of open PR 9066.

## Theorem 2 — the frustration-free member is the Rokhsar–Kivelson projector

Require that the clause annihilate the symmetric flippable state
`|a⟩ + |b⟩` and every non-flippable configuration.
- On the non-flippable orbits the clause is diagonal, so `V_o = V_a = V_1 = 0`.
- On the flippable pair it gives `(V_f − g)(|a⟩ + |b⟩)`, so `V_f = g`.

The solutions form one ray: `g (P_flip − U − U†) = 2g |−⟩⟨−|`, with
`|−⟩ = (|a⟩ − |b⟩)/√2`. Its eigenvalues are 0 and `2g`, so it is positive
for `g ≥ 0`. ∎

## Theorem 3 — its ground states record uniform ice measures

On the ice space, `Σ_p 2g |−_p⟩⟨−_p|` has two parts:
- on the diagonal, `g` times the number of flippable plaquettes;
- off the diagonal, `−g` for each flip.

That is `g` times the Laplacian of the plaquette-flip graph. A graph
Laplacian is positive, and its kernel is spanned by the indicator vectors
of the connected components. So the zero-energy states are the uniform
superpositions of the flip classes. ∎

**Records.** Under the trace rule, a class's uniform state records every
ice configuration of that class with equal probability. The landed
`COULOMB_MEASURE_SELECTION_HARD_STATIC_ICE_RULES_ADMIT_EVERY_ICE_MEASURE_POSITIVE_RULES_SELECT_THE_UNIFORM_ONE_BOUNDED_THEOREM_NOTE_2026-09-22.md`
finds that positive static rules select the uniform ice measure.
- On each flip class, the Rokhsar–Kivelson ground state records the
  uniform measure of that class.
- The uniform ice measure is the mixture of these zero-energy states,
  weighted by class size.

**On the 2x2x2 coarse torus** there are 9600 ice states in 937 flip
classes:
- the largest class has 864 states;
- 760 states are frozen, with no flippable plaquette.

On the largest class, the Laplacian's smallest eigenvalues are 0 and
0.970. The pure ring (`V = 0`) ground state there is far from uniform: its
amplitude spread is 2.7 times its mean.

## Theorem 4 — unrecorded plaquette qubits polarize the ice

Compress the two-site clause onto a Gauss sector, the exact-Gauss limit of
open PR 9066, and take `D = 0`. Consider the bonds from an unrecorded
plaquette qubit to its four links:
- **Heisenberg part.** It keeps `J E_l (s_p · ê_l)`.
- **Compass part.** It couples link components transverse to `ê_l`, which
  are off-diagonal in `E_l`, so it drops out.

With its cube records giving a field `B n̂`, the plaquette qubit sees

    B_eff = B n̂ + J Σ_l E_l ê_l .

- **Orbit energies.** The link sum vanishes on the flippable and opposite
  orbits. It has size 1 on odd and `√2` on adjacent configurations. The
  plaquette's ground energy `−|B_eff|/2` is therefore:
  - `−B/2` on the flippable and opposite orbits, the highest;
  - `−√(B² + J²)/2` on odd configurations;
  - `−√(B² + 2J²)/2` on adjacent configurations.
- **Minimizers.** A plaquette is adjacent exactly when its opposite links
  agree. So the summed potential is lowest when every plaquette is
  adjacent, which forces the field to be uniform along each axis. On the
  2x2x2 torus the minimizers are exactly the 8 uniformly polarized ice
  states, and none has a flippable plaquette.
- **Scale.** The potential is of order `J` for `B ≲ J`, and `J²/(4B)` above
  that. The fourth-order ring is of order `h⁴/U³`. So unrecorded plaquettes
  freeze the ice into a polarized state before the ring can act.

The Moriya coupling adds a term that depends on the circulation. It is not
treated here.

## What this means for the lanes

- **Photon lane.** The supplied Rokhsar–Kivelson Hamiltonian of the ice
  notes is the frustration-free member of the covariant plaquette clause.
  Its records are the uniform measure of the landed selection.
- **Where the ring can act.** Plaquette sites have to be recorded, or
  otherwise stop coupling to their links. Otherwise the ice polarizes.
- **Phase.** No phase of the plaquette family is derived here. That
  includes the pure-ring point of open PR 9066.

## Checks

The runner has 4 checks and all pass in about 1 s.

| Check | Result |
|---|---|
| Orbits | Stabilizer of order 8; orbit sizes 2, 2, 4, 8. The flippable orbit is the corner-neutral pair. |
| Frustration-free | Solution space of dimension 1, coefficients (ring, flippable, opposite, adjacent, odd) = (1, 1, 0, 0, 0), eigenvalues {0, 2}. |
| Ground states | 9600 ice states, 937 classes (largest 864, 760 frozen). Laplacian row sums 0. Largest-class spectrum starts 1e-15, 0.9696. Pure-ring amplitude spread 2.738. |
| Unrecorded plaquettes | At B/J = 4 the orbit energies are −2.0 (flippable, opposite), −2.06155 (odd) and −2.12132 (adjacent). The 8 minimizers are uniform along each axis, with 0 flippable plaquettes. |

## What this does not do

- It adopts no plaquette clause, Gauss law or record pattern.
- It derives no photon phase, and does not place the soft-Gauss route of
  open PR 9066 in any phase.
- It does not study flip classes on larger tori, or the Moriya term in
  Theorem 4.
