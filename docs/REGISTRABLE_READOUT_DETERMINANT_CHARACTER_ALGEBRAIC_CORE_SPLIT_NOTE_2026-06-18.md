# Registrable Readout Determinant-Character Algebraic Core Split

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Boundary:** source-side algebraic split only; effective status is pipeline-derived after independent audit ratification and dependency closure.
**Status authority:** independent audit lane only. This note does not set or predict an audit outcome and does not edit audit ledgers, queues, Tier-A registries, publication-status surfaces, active review queues, lane registries, or front-door status files.
**Primary runner:** [`scripts/frontier_registrable_readout_determinant_character_algebraic_core_split_2026_06_18.py`](../scripts/frontier_registrable_readout_determinant_character_algebraic_core_split_2026_06_18.py)
**Cached log:** [`logs/runner-cache/frontier_registrable_readout_determinant_character_algebraic_core_split_2026_06_18.txt`](../logs/runner-cache/frontier_registrable_readout_determinant_character_algebraic_core_split_2026_06_18.txt)

## Purpose

The audited conditional row for
`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`
(context handle, not a citation-graph dependency) separates two facts:

1. the zero-phase determinant-character step is valid algebra; and
2. the physical strong-CP mass readout and AC_phi_lambda species readout
   identifications are separate supplied/readout-context bridges.

This note isolates only the first fact as a small algebraic core. It does not
claim the physical bridges, does not reduce any Tier-A admission, and does not
change the parent row's audit status. It gives the reviewer and auditor a
clean source artifact that can be inspected independently of the downstream
strong-CP and AC_phi_lambda consequences.

## Algebraic Core

Fix a supplied finite readout context with:

- a finite central-sector decomposition by orthogonal idempotents
  `{e_j}`;
- a fixed `K`/CPT conjugation acting on determinant phase by
  `arg z -> -arg z`;
- a sector-factored determinant datum `z = prod_j z_j` with
  `z_j in C^x`;
- a scalar determinant phase contribution whose phase-bearing part is an
  `R`-valued group homomorphism of the per-sector phase data.

Use the current Record axiom in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only for its
finite scalar additivity and content-determination sentences. `K`/CPT orbit
constancy is not axiom content under the 2026-06-29 foundation reset; it
enters through the supplied-context bridge
[`KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md`](KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md)
— T1 (orbit constancy from the supplied ORBIT-INDEXING property plus the
axiom's content-determination sentence) and T2 (the
determinant-character/log-character homomorphism boundary registered as named
supplied-context structure). Record itself supplies no readout context,
determinant datum, homomorphism boundary, physical source/action
interpretation, mass readout, species readout, or occupancy rule.
(2026-07-04: premise relocation per the conditional-audit
`missing_bridge_theorem` repair note; the algebraic core below is unchanged.)

**Theorem.** In the supplied determinant-character/log-character context above,
the homomorphic determinant phase contribution is identically zero. Equivalently,
inside this supplied homomorphism class, the determinant-character phase index
is `k = 0`, and the determinant datum that can survive registration is
modulus/log-modulus type.

## Proof

1. Orthogonal idempotents are pairwise-disjoint record labels in the supplied
   context. Finite scalar additivity over disjoint records removes cross-record
   interference terms from a scalar readout.
2. Sector factorization gives `det = prod_j z_j`, so the determinant phase is
   the sum of per-sector phases modulo `2 pi`.
3. The determinant-character/log-character boundary says the phase-bearing
   contribution is a group homomorphism from that phase group to `(R,+)`.
   This is the supplied boundary, not a consequence of Record finite
   additivity.
4. Any additive `R`-valued functional on an abelian group is odd:
   `g(-x) = -g(x)`, with no regularity hypothesis.
5. `K`/CPT orbit constancy makes the same scalar even:
   `g(-x) = g(x)`.
6. Even and odd together force `g(x) = 0` for every phase datum.
7. `log|z|` is additive and `K`/CPT-even, so modulus/log-modulus data is the
   determinant-class datum that survives this algebraic core.

The hostile guard is explicit: K-even phase functions such as `cos(theta)`,
and finite record sums such as `sum_j cos(theta_j)`, are still
phase-dependent. They are not excluded by Record alone. They are outside this
core only because they are not determinant-character/log-character
homomorphisms of the phase data.

## What This Split Does Not Claim

- It does not identify the physical strong-CP mass-orientation readout with
  this supplied determinant-character/log-character surface.
- It does not prove that no action-level or non-registrable orientation datum
  remains on a physical strong-CP surface.
- It does not identify AC_phi_lambda species data with an unordered
  Record-registrable mass multiset.
- It does not prove or use `|delta| = 2/9`, R-eta, R2, or any Koide value
  bridge.
- It does not derive the determinant-character/log-character boundary from
  Record.
- It introduces no new axiom, primitive, admission, normalization,
  comparator, fitted value, or measured input.

## Relation To The Parent Conditional Row

The parent note remains the broader conditional bridge map. This split keeps
its useful algebra while refusing to launder the still-open physical
readout identifications into the theorem. Downstream routes that want to use
the algebra for strong-CP or AC_phi_lambda still need their own independently
reviewed physical-readout bridge theorems.

## Runner Certificate

The runner verifies:

- central idempotent disjointness and finite additivity removing cross terms;
- determinant phase additivity on sector products;
- additive implies odd, `K`/CPT orbit constancy implies even, and even plus odd
  forces the phase functional to zero;
- modulus/log-modulus survives;
- K-even phase-dependent hostile functions remain possible outside the
  homomorphism boundary;
- the parent note carries the conditional boundary language and this split note
  carries no bridge-discharge wording.
