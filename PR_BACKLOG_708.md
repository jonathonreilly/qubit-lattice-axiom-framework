# Cycle 708 — BACKLOGGED (seventh), and the first test of step 11

Branch: `physics-loop/a2-wellposedness-20260726`
Commits: `c732a93612` (science), `c5d4d12b3a` (receipt + value gate)
Runner: 7 PASS / 0 FAIL, cold-run at `c732a93612`, PIN MATCH `e824f3df…`.
Step 11 inference audit: **clean**.
Cluster-cap evaluator: **BACKLOG**.

## What the audit did catch

Two real defects, during the cycle, before submission:

1. `pinv_annihilates_const = True  # by definition of the Moore-Penrose pinv`
   — a hardcoded pass. Replaced by an explicit exact construction of `H⁺`
   checked against `H·H⁺ = I − J/n`. The evaluator independently confirmed:
   *"genuinely replaced by an explicit exact construction, and no comparable
   hardcoded pass survives."*
2. A prose claim about A2's antecedent that **no ledger row covered**. Found by
   the `DIRECTION` check; W2 was rewritten to state it.

Running the audit also exposed two bugs in the linter itself (a normalization
asymmetry and a brittle prefix match), both fixed on
`methodology/inference-audit-20260726`.

## What the audit did NOT catch — the important finding

The evaluator's verdict on the audit:

> "W5 is the decisive overreach … Calling this a repair 'without new input'
> repeats the campaign's diagnosed failure mode. **Listing the family in the
> Hypotheses column does not cure the headline claim.** … The inference audit
> is therefore **syntactically complete but not substantively discriminating**."

This is exact and it is the most useful output of the cycle. I recorded the
supplied operator-family hypothesis in W5's Hypotheses cell — and then titled
the note *"…and Covariance Repairs It Without New Input"*. The linter checked
that the hypothesis was **written down**. It could not check that the headline
**respected** it.

**Generalization: a mechanical check makes a defect visible; it does not make
you honest about it.** The reader of a title is exactly the person who will not
read the ledger.

Fixed as a second layer (`TAG` + `HEADLINE`, pushed to the methodology branch):
hypotheses must now be tagged `[supplied]` or `[satisfied]`, and any
`[supplied]` row forces a qualifier in the title. The self-test now includes
this note as a fixture and fires `HEADLINE` on it, naming W3 and W5 — the two
rows the evaluator flagged.

## Accepted objections

- **W5** — the `A=0, B=-1` forcing holds only after assuming the range-1
  scalar linear-convolution proper-cubic-covariant family, and the cited
  classification *itself states* those operator hypotheses are supplied, not
  derived. "Repairs it without new input" is false. This was the same move as
  cycle 705's imported objective.
- **W3** — logically correct (a singular pseudoinverse cannot equal an
  invertible `L^{-1}`), but the Bell convention "is not established as
  repo-wide authority for the gravity lane". It shows a **cross-lane convention
  mismatch**, not that gravity's A2 is generally unsatisfiable. The title
  overstated this too.
- **W1/W2** — the parent theorem is formulated on infinite `Z^3`, so a finite
  periodic obstruction clarifies regulator/domain requirements rather than
  invalidating the parent's conditional implication.
- **Ledger quality** — W4 omits restricted-A2 as a hypothesis, and several
  falsifiers (notably W3's) cannot occur under their own definitions. A
  falsifier that cannot occur is the same defect as an absent one.

## Honest salvage, not attempted here

What survives, correctly scoped: the periodic zero mode blocks a finite
covariant `G_0` (Z1/Z2); the cross-lane convention mismatch (Z3, retitled as
such); the two priced repairs (Z6 mass changes the operator, Z7 Dirichlet
breaks the translation invariance the parent *derives* from A2 — the evaluator
called Z7 "accurate"). Dropped entirely: any claim that covariance repairs A2
without new input.

That is a regulator/domain clarification on a critical row, not a repair. It
should be retitled accordingly and every `[supplied]` row surfaced in the
title before any resubmission.
