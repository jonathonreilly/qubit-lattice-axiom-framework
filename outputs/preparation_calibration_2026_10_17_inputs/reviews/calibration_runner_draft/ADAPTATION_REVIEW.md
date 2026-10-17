# Calibration corroboration source draft

Only preparation_calibration_2026_10_17.py and this review were created here.
No runner execution, import, compile, scientific run, Git, PR, audit, W,
editable prompt or checkpoint modification occurred. One Python edit replaced
text only. There is no successful run count or PASS evidence at drafting time.

Read the publication THEOREM_NOTE.md, its SOURCE_IDENTITY_AND_DEPENDENCIES.json,
original corrected CANDIDATE_V2.md and CORRECTIONS.json completely. Their exact
pins remain as supplied in the inventory; no current independent hash check is
claimed by this text-only drafting handoff. The proposal is explicitly based
on PR9667's controlled two-rail apparatus, not PR9668's endpoint apparatus.
This is source-exposed author corroboration, not an independent reconstruction
of its analytical reviews or ancestral runtime theorem. Separate analytical
reviews remain necessary implementation-independent support.

The runner constructs local Q operators with Kronecker products of occupation,
annihilation and creation matrices. It compares their positive outer-product
representations and complement representations at two unequal signed rational
hoppings, checks the identity trace and scaling at both calibration endpoints,
and assembles the nine isolation and five pulse channels explicitly. These
local checks do not prove every real-h statement by numerical sampling; the
analytical Gram argument supplies that quantified result.

Polynomial arithmetic over Q[d] computes the projection-difference
discriminant from its determinant and trace; a separately constructed actual
rational rank-one projector checks that realization. Polynomial multiplication
checks the monotonicity factorization, and squared comparison retains the
actual d=2/3 versus epsilon=1 counterexample. The sign argument on the full
interval remains an analytical proof; no monotonicity sweep is used.

The ramp/pulse integrals, endpoint slopes and derivative factorization are
exact local polynomial arithmetic. Global profile maxima, full-space Duhamel,
unitary invariance, trace contractivity and complete output estimates are
analytical premises. The modeled work sums the variations of all pulses;
the peak load uses the maximum of the three disjoint pulse windows. No
whole-device operator or energy expectation is computed. The all-occupied
clock check is only its explicit bond-count expression, not a generic no-go.

Exact source constants are embedded and source-pinned through the package.
There are no external scientific data reads or dynamic scientific imports.
The one manifest and its frozen files are integrity reads only. Root must
expand the literal AUDIT_INPUT_PATHS with every manifest row, using schema
{"files":[{"path":"repo-relative", "bytes":123, "sha256":"..."}]}.
The manifest itself is declared but not listed as its own row. It must be the
first tuple entry, and the manifest must contain at least one frozen file.
All reads require regular files and reject symlink ancestors below the repo.
The runner does not self-hash; the canonical envelope owns the source pin and
external 30-second timeout/resource caps. Root may choose the final canonical
basename and package path together before binding them.

## Required final work

Root must inspect the complete source, syntax/import-inert check it, expand and
bind inputs, execute bounded baseline and scratch mutations, and create the
canonical envelope cache. No cached result exists from this drafting task.
Check source freshness against the publication note before integration.

## Mutation cases, one meaningful failure per family

Each mutation must fail on the intended arithmetic family, not an earlier
integrity mismatch. Source mutations need no self-pin adjustment. Preserve
baseline source and logs, and run mutations only on scratch copies.

- Local Q: change the |11> Gram coefficient from 2|h| to |h|; Gram check fails.
- Complement/identity: replace 2|h|I by |h|I in comp; complement Gram fails.
  Separately drop trace identity scaling's xi factor to test retained scalar.
- Projection: change determinant=-b_squared to +b_squared; polynomial
  discriminant fails. Change actual diff[1][1] only to challenge the distinct
  rational projector realization.
- Monotonicity: replace factor 3d-1 by 2d-1 on the factorized RHS; identity fails.
- Counterexample: replace its d=2/3 test value with d=0; squared comparison fails.
- Profile: change pulse quartic coefficient30 to29; unit-area check fails.
- Isolation: remove one kappa*c edge from edge_magnitudes; assembled Aiso
  formula check fails. This tests literal channel accounting.
- Pulse accounting: change a Q norm from2 to1 in norms; area-norm check fails.
  Change the first occupation identity from1/2 to1; identity-area check fails.
- Duhamel ceiling: reduce target10 to9; rational bracket check fails.
- Peak/work: double pulse_peaks only after area checks; peak or work ceiling
  fails. Change work's factor2 on the sum to3 for isolated work failure.
- Slew: change the numerator10 to12 in the squared pulse-slew expression;
  squared20 ceiling fails.
- Trace composition: change epsilon from10^-9 to10^-8; squared seed trace
  contribution fails. Change the trace conversion factor2 to1 on its LHS;
  pure-seed trace comparison fails.
- Resource counts: change added preparation count9 to8 in channels; channel
  identity fails. Change four endpoint occupations to three in the occupied
  clock expression; its energy identity fails.
- Integrity separately: tamper one frozen file without updating its hash, and
  replace a same-byte file or ancestor directory with a symlink. Both must
  fail before arithmetic and must not count as mathematical mutation coverage.
