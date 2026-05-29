# Koide Q=2/3 Block-Weight Frontier

**Date:** 2026-05-29
**Claim type:** bounded_theorem
**Status:** bounded support / open_gate localization. This note does not
approve a new import, does not set an audit verdict, and does not promote
charged-lepton Koide to a derived theorem.
**Primary runner:** `scripts/koide_q23_block_weight_frontier_2026_05_29.py`
with cache `logs/runner-cache/koide_q23_block_weight_frontier_2026_05_29.txt`.

## Scope

This is the source-only salvage from the Koide Q=2/3 weighting campaign. It
keeps the exact algebraic content and strips the branch-local campaign
history, self-audit language, and global no-go/import conclusions.

The retained upstream Koide surface already supplies the algebraic equivalence
between `Q=2/3` and the C_3 character-norm split:
[CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
and
[KOIDE_Q_TWO_THIRDS_Z3_CHARACTER_NORM_SPLIT_RECASTING_THEOREM_NOTE_2026-05-10.md](KOIDE_Q_TWO_THIRDS_Z3_CHARACTER_NORM_SPLIT_RECASTING_THEOREM_NOTE_2026-05-10.md).
The retained anticommuting-operator surface supplies the chiral implication:
[KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md](KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md),
with the retained bounded equivariant obstruction in
[KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md).

## Exact algebra kept

On the C_3 generation surface, write the square-root mass vector as a
democratic component plus an orthogonal doublet component. With
`E_+ = 3 a^2` and `E_perp = 6 |b|^2`,

`Q = (sum s_i^2) / (sum s_i)^2 = 1/3 + (2/3) |b|^2/a^2`.

Thus `Q=2/3` is equivalent to `|b|^2/a^2=1/2`, or `E_+ = E_perp`.
The structural issue is not the algebraic identity; it is the physical
selection of the weight assigned to the two C_3 isotypes.

Three canonical weightings are cleanly separated:

| Weighting | Isotype power split | Koide value |
|---|---:|---:|
| democratic endpoint | `(1,0)` | `Q=1/3` |
| equal block count | `(1/2,1/2)` | `Q=2/3` |
| dimension / Plancherel trace | `(1/3,2/3)` | `Q=1` |

The equal-block rule is the rule that gives the observed charged-lepton
Koide value. This note does not derive that rule from the one-qubit operator
algebra on the `Z^3` spatial substrate. It records it as the bounded frontier:
the candidate rule is visible and exact, but still an open input until a
separate derivation or explicit approval exists.

## What the review rejected

The source campaign contained stronger stages that are not landed here:

- "first-principles derivation from Axiom 1 / Axiom 2";
- "the framework predicts Q=1" as a global conclusion;
- "chirality is a confirmed irreducible import";
- broad route-closing no-go language without a complete no-go-discipline
  package.

Those are not needed for the durable algebra. The landed claim is narrower:
the C_3 block-weight algebra is exact, the equal-block rule gives `Q=2/3`,
the dimension-weighted trace gives `Q=1`, and the current source stack still
has to decide or derive which physical weighting applies to charged leptons.

## Counting-vs-splitting localization

The retained C_3-equivariant anticommuting obstruction gives a useful
localization. C_3-equivariant generation operators commute with the
singlet/doublet grading and therefore cannot be the chiral operator used by
the retained anticommuting-operator theorem. Operators that anticommute with
that grading necessarily split the C_3 orbit.

So the charged-lepton Koide frontier is sharply located: the same C_3 orbit
that organizes the three-generation count does not by itself choose the
orbit-splitting chiral/equal-block weighting. That is an open_gate
localization, not an approved new premise.

## Audit expectation

The independent auditor should treat this as a bounded theorem candidate:
the algebra and runner are exact, while the equal-block physical selection
is explicitly not derived or approved here.
