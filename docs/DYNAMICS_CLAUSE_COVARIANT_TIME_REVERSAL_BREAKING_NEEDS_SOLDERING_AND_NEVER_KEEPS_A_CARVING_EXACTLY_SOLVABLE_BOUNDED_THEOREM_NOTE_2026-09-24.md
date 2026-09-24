---
claim_id: dynamics_clause_covariant_time_reversal_breaking_needs_soldering_and_never_keeps_a_carving_exactly_solvable_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Three-spin terms s^alpha_i s^beta_m s^gamma_k on a site m and two neighbours are the smallest time-reversal-odd terms, and lie in m's neighbourhood (star terms). (i) Under possibility covariance the only three-spin form is the scalar chirality s_i . (s_m x s_k), and its covariant sum over neighbour pairs vanishes: a proper rotation swaps any ordered pair of neighbour directions while the chirality changes sign. (ii) Under the four landed actions, covariant T-odd three-spin star terms on perpendicular pairs span dimensions 18, 12, 12 and 12 (trivial, sign twist, axis, full soldering). (iii) None of them has Kitaev's solvable pattern s^a_i s^c_m s^b_k (a, b the bond axes to i and k, c the third axis): the intersection is zero for all four actions. (iv) On the 8-site cube carving, Kitaev-pattern terms commute with all six loop operators. All 12 covariant T-odd terms under full soldering are nonzero on the cube, and no nonzero combination of them commutes with all six loop operators. So a covariant T-odd star term does not keep the cube exactly solvable. In exactly solvable carvings, time-reversal breaking has to come from record contents. No chiral phase, Weyl node or physical identification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_covariant_time_reversal_breaking_and_kitaev_solvability_2026_09_24.py
---

# Covariant time-reversal breaking needs soldering and never keeps a carving exactly solvable

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite certificates under supplied covariance; unaudited.

## Result

Chiral matter needs time reversal or parity to be broken somewhere. The
campaign's clause has parity-odd content already, the Moriya coupling of
open PR 9050. Its time-reversal-odd content would start with three-spin
terms on a site and two of its neighbours. Those are star terms, inside one
Admissibility neighbourhood.
- **Possibility covariance allows none.** The only internally invariant
  three-spin form is the scalar chirality `s_i·(s_m × s_k)`. A proper
  rotation swaps any ordered pair of neighbour directions, and the
  chirality changes sign under the swap, so the covariant sum vanishes.
- **Soldering allows some,** 12 dimensions of them on perpendicular pairs.
- **None keeps a carving exactly solvable.**
  - Kitaev's chirality term `s^a_i s^c_m s^b_k`, which maps to
    next-nearest Majorana hopping, is never covariant under any landed
    action.
  - On the cube carving, every covariant T-odd term breaks the loop
    operators.

So in the exactly solvable Majorana media of open PRs 9048 and 9054, time
reversal can be broken only by the record contents. Those are the fields on
dangling axes, which the scan of open PR 9054 found gapped.

## Setting and decision points

- **The site and its neighbours.** A site `m` and neighbours `i`, `k`,
  perpendicular or collinear. The term is
  `s^α_i s^β_m s^γ_k = s^γ_k s^β_m s^α_i` (the factors commute), and it is
  odd under time reversal.
- **The actions.** The four landed actions of the soldering menu, and
  possibility covariance (every internal rotation).
- **Carvings.** Open PR 9048: the cube, with loop operators, one per face,
  equal to the product of the Paulis along the axis perpendicular to the
  face.

The dynamics clause and any star term are supplied decision points. None is
adopted.

## Theorem 1 — possibility covariance excludes time-reversal-odd star terms

An internally invariant three-spin tensor is proportional to `ε_{αβγ}`, so
the term is a sum of scalar chiralities `χ_{imk} = s_i·(s_m × s_k)`.
- **The swap.** The 24 proper rotations act on ordered pairs of neighbour
  directions. The half-turn about the bisector of `d_i` and `d_k` exchanges
  them.
- **The sign.** Covariance needs the coefficient to be the same on
  `(i, k)` and `(k, i)`. But `χ_{kmi} = −χ_{imk}`.
- **So it vanishes.** Every covariant coefficient is zero, for
  perpendicular and for collinear pairs. ∎

## Theorem 2 — soldering allows them, but not in solvable form

- **Dimensions.** Group-averaging over the 24 rotations gives the covariant
  T-odd terms on perpendicular pairs. Their space has dimension 18, 12, 12
  and 12 under the trivial, sign-twist, axis and full actions.
- **Kitaev's pattern.** It is `s^a_i s^c_m s^b_k`, where `a` and `b` are
  the bond axes to `i` and `k` and `c` is the third axis. On a carving,
  where every site has one bond per axis, it maps to next-nearest Majorana
  hopping and keeps the loop operators conserved.
- **No overlap.** The intersection of the covariant space with the span of
  the 12 Kitaev-pattern terms is zero, for every action. ∎

## Theorem 3 — on the cube, covariant time-reversal breaking breaks solvability

- **Kitaev-pattern terms** commute with all six loop operators.
- **Covariant terms.** Take the 12 covariant T-odd terms under full
  soldering, evaluated on the cube's triples. All 12 are nonzero there, and
  their commutators with the six loop operators have full rank. So no
  nonzero covariant combination commutes with all six loop operators. ∎

## What this means for the lanes

- **Chirality lane.**
  - Parity-odd content (the Moriya coupling) is covariant under soldering.
  - Time-reversal-odd content in the dynamics needs soldering and a star
    term.
  - Even then it breaks the exact solvability that gives the Majorana and
    Z2 content.
  - Within exactly solvable carvings, time reversal is broken only by
    records.
- **The ladder of the synthesis.** Chirality sits beyond the solvable
  sector. A chiral Majorana phase would need a star term that breaks
  solvability, or record contents different from those scanned in open PR
  9054.

## Checks

The runner has 4 checks and all pass in about 2 s.

| Check | Result |
|---|---|
| Possibility covariance | Every group-averaged scalar-chirality coefficient is 0, for perpendicular and for collinear pairs. |
| Covariant T-odd terms | Dimensions 18, 12, 12, 12 (trivial, sign twist, axis, full). |
| Kitaev pattern | 12 pattern terms; intersection 0 with every covariant space. |
| Cube | Kitaev-pattern commutators 0. The 12 covariant terms are all nonzero on the cube, and none of their combinations preserves the loops. |

## What this does not do

- It adopts no star term and no covariance.
- It covers three-spin terms. Longer T-odd terms, and the 3D networks of
  open PR 9054, are not treated. The cube is the certificate.
- It claims no chiral phase, Weyl node, Chern number or physical
  identification.
