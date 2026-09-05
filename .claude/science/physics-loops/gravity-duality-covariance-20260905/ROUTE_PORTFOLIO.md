# Route portfolio — block 215 (the plane-or-sum question)

## Prior-art sweep (skill step 2), origin/main refreshed 2026-09-05T11:05Z = 4407b6a0e0a38074d9b38710da6ed3a83c9e5e56
Commands (run from the block-214 worktree, results identical on the block-215 worktree):
- `git grep -n -iE "(D16.*D34|D34.*D16|D25.*D16|duality parameter)" origin/main -- 'docs/*.md'` — 1 hit, an intake note's commit line (context only).
- `git grep -n -iE "(hodge (star|complement).*(proportional|multiple)|cross-grade|cross-parity|grade parity)" origin/main -- 'docs/*.md'` — 4 hits, all the FULL128 two-cell parity notes and a DM-neutrino note (different objects; context only).
- `git ls-tree -r --name-only origin/main -- docs/ | grep -iE "dualit|parity|gluing|rigid"` — parity/gluing titles from other lanes (fermion parity, commensuration period parity, gauge multiplaquette gluing); none on a cell form's duality parameters.
- `git grep -n -iE "(proper cubic rotation|cubic (group|rotation)).*(cell form|hodge|dirac|kähler|kahler|weight)" origin/main -- 'docs/*.md'` — 1 hit (stencil orbit note; context only).
- `git grep -n -iE "(schur|intertwin).*(hodge|star)|(hodge|star).*(schur|intertwin)" origin/main -- 'docs/*.md'` — carrier-orbit / seven-site-star notes (a different "star": the seven-site stencil; context only).
- `git ls-tree ... | grep -iE "covarian|isotrop|rotation"` — 20 titles (kinetic isotropy primitive, cubic anisotropy sections, covariant law notes); none computes a covariance locus of a Dirac-Kähler cell form's duality parameters.
- Stack sweep on this branch: `git grep -n -iE "rotation" HEAD -- 'docs/ADMISSIBILITY_DIRAC_KAHLER_*.md'` — Block 201 (COVARIANT_RULE_IDENTIFICATION 2026-08-26) carries "all 24 proper cubic rotations by exact intertwiners" for the nearest-neighbour rule encoding; Block 213 `N6` names "derive the assembly from the rule's covariance" as an open non-axiom route; Block 214 exhibits the plane and records "No premise prefers it."
Classification: **open after the matched-hit review**. Block 201's intertwiners are inputs (machinery), not the result; no landed or stacked note computes what the rotations do to `D07, D16, D25, D34` or to the curved family's shears.

## Routes
| id | route | artifact | approach family | expected trace | score |
| --- | --- | --- | --- | --- | --- |
| R-A | twisted-covariance census: the 24 proper rotations with the corner-sign gauge, every subgroup class, every gauge class, symbolic moduli; the exact locus per subgroup; shear survival | theorem note + runner | F-cov (fixed-subspace linear algebra) | upstream_support, partially_closes REOPEN 1 conditionally | **selected** — exact either way; answers the wall as posed |
| R-A' | the star lemma: the plane = the star-proportional cross block in the lane's signature | lemma inside R-A | F-star | supports R-A (gives the plane its name) | selected (part of R-A) |
| R-B | positivity as selector | control inside R-A | F-pos | prunes (known: W1 + D16 = 1/4 is PD off the plane) | control only |
| R-C | grade-parity preservation as selector | lemma inside R-A | F-parity | prunes onsite (every parameter breaks parity); identifies s = 0 as parity preservation under overlap | control / lemma |
| R-D | the record readout as selector | none | — | not runner-able: no readout object exists at the cell-form level of the chain | recorded, not attempted |
| R-E | a principle tying the parameters to the moduli (REOPEN 5) | — | — | deferred: no candidate principle named | queued, not attempted |

Dramatic-step gate: R-A changes the lane state either way — it either names the plane by the axiom's own symmetry (conditional on the covariance reading) or proves that no proper-rotation subgroup distinguishes it (then REOPEN 1 needs a non-symmetry principle). Corollary-churn check: not a corollary of Block 214 (which computed loci of `det M`, not of the symmetry action).
