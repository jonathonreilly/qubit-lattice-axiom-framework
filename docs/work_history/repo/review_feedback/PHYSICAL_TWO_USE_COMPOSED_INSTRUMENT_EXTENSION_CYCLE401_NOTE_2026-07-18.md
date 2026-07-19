# Physical two-use composed-instrument extension — Cycle 401

Date: 2026-07-18

Authority: none

Audit: unset

Constitutional effect: none. This cycle changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, or audit-status surface and
drafts no axiom language.

Companion runner:

```text
scripts/physical_two_use_composed_instrument_extension_cycle401_2026_07_18.py
```

## Result up front

Cycle 401 changes exactly the Cycle-398 `W5` condition from single-menu
normalization incidence to a declared physical same-program two-use grammar.
Every one of the 51 Cycle-398 bank programs is applied twice with the same
program label and two fresh blank pointers. The actual ordered branch operator
is extracted from the fixed physical composition tensor and retains its
effect and conditional CP tag.

Five exhaustive coarse presentations are constructed for each program:
ordered-fine, first-pointer marginal, second-pointer marginal, unordered-pair
symmetrization, and same-versus-different pointer. This gives 1,645 ordered
fine branches, 255 composed menus, and 3,277 effect occurrences.

Appending the complete declared grammar to the Cycle-398 `98 x 55`, rank-31
system yields 353 menus, 636 classes, exact rank 192, and affine dimension
444. Composition creates 581 new effect classes, and the rank gain is 161.
This is a strong positive change from the single-menu grammar.

Effect equality is used only for incidence variables. Equal effects are not
used to merge distinct processes. The composed census contains 785
effect/process pairs; 50 effect classes carry multiple process tags, with as
many as 15 retained tags for one effect class.

Born selection: not claimed. Universal menu eligibility: not claimed.
Actuality, sampling, and frequency: not claimed. A global composition theorem,
minimum content, and axiom pressure: not claimed.

## Exact finite grammar

The same-program two-use grammar is:

1. Source programs are exactly the 51 physically compiled Cycle-398 programs
   in their seven fixed banks. Their one-use outcome counts are distributed as
   `3x3`, `6x4`, `14x5`, `20x6`, `4x7`, and `4x8` programs/outcomes.
2. A program is applied twice without changing its label between uses. The
   ordered fine pointer is `(a,b)`, where `a` is the first-use pointer and `b`
   is the second-use pointer.
3. For one-use blocks `K_a`, the extracted two-use operator is checked against
   `K_b K_a`. Its effect is `(K_b K_a)^dagger (K_b K_a)` and its process tag is
   the Choi matrix of that single-branch CP map.
4. Every declared coarse group is an exhaustive, disjoint partition of the
   ordered `n^2` branches. Its effect is the sum of branch effects, while its
   process is the Choi sum of the retained branch operators.
5. Exactly five grouping families are admitted. There is no sampling: every
   source program, every ordered branch, and all five deterministic grouping
   rules are enumerated.

The grammar is exhaustive only under these bounds. It excludes cross-program
composition, program rewrite between uses, idle labels, third or later uses,
and arbitrary set partitions of the ordered branches.

## Declared grouping families

For `n` one-use outcomes and fine index `i(a,b)=an+b`:

| family | exhaustive groups | effect occurrences over all 51 programs |
|---|---|---:|
| ordered-fine | singleton `{i(a,b)}` for every ordered pair | 1,645 |
| first-pointer marginal | fixed `a`, all `b` | 283 |
| second-pointer marginal | fixed `b`, all `a` | 283 |
| unordered-pair symmetrization | `{i(a,a)}` and `{i(a,b),i(b,a)}` for `a<b` | 964 |
| same-versus-different pointer | all `a=b` versus all `a!=b` | 102 |
| **total** | **255 complete menus** | **3,277** |

The first-pointer marginal recovers the original one-use effects because the
second instrument is exhaustive. Its process tag remains the two-use
nonselective continuation and is not identified with the one-use process.

## Actual physical composition and CP tags

For each fixed bank the runner computes the actual two-use tensor from the
same `128 x 16` controlled update used in Cycle 398. It extracts every lawful
program block at the ordered pointer pair and verifies equality with the
direct `K_b K_a` product. Off-diagonal program-write blocks remain zero.

Every fine and coarse effect is positive, every coarse menu sums to identity,
and every retained Choi tag is positive and Hermitian within tolerance. The
first-pointer effect-recovery residual is checked over all 283 outcomes.

The largest actual-tensor/direct-product extraction residual is
`9.614813431917819e-17`, and the off-diagonal program residual is zero. The
largest composed-menu completeness residual is `2.843626111939516e-15`.
The smallest numerical coarse-Choi eigenvalue is
`-2.7755575615628923e-16`, its largest Hermiticity residual is
`8.045235935650967e-17`, and the largest first-pointer effect-recovery residual
is `4.783309287441108e-16`.

The actual contact is load-bearing in composition. Recompiling the same source
rows with identity in place of contact changes every bank's fixed two-use
update and changes ordered effects and conditional processes. Unlike one-use
effects, two-use effects contain the intervening contact conjugation and can
therefore change under contact deletion.

The smallest bankwise two-use-update change is `1.1502005721977573`. The
largest ordered-effect change is `0.05565495916190494`, and the largest
ordered-process Choi change is `0.472944059339986`. Every bank has a nonzero
effect and process change.

## Effect quotient and process separation

The 3,277 composed occurrences reduce to 616 equal-effect keys. Thirty-five of
those keys coincide with Cycle-398 classes, so the combined system contains
`55 + 616 - 35 = 636` effect classes. The remaining 581 are new.

Process tags are never deduplicated merely because their effects agree. The
616 effect keys support 785 distinct effect/process pairs and 785 distinct
process tags. Fifty effect keys have multiple process tags; the largest
multiplicity is 15. The largest same-effect/different-process Choi separator
is `0.8683729074638544`.

Thus the supplied effect-functionality premise supports the incidence
quotient, while no process-functionality premise is introduced.

## Exact cumulative rank ledger

Every incidence matrix is integer. Numerical rank is cross-checked with exact
SymPy integer rank at each cumulative step:

| appended family | shape | effect classes | exact rank | incremental classes | incremental rank |
|---|---:|---:|---:|---:|---:|
| Cycle-398 baseline | `98 x 55` | 55 | 31 | — | — |
| ordered-fine | `149 x 305` | 305 | 72 | 250 | 41 |
| first-pointer marginal | `200 x 305` | 305 | 72 | 0 | 0 |
| second-pointer marginal | `251 x 435` | 435 | 115 | 130 | 43 |
| unordered-pair symmetrization | `302 x 564` | 564 | 155 | 129 | 40 |
| same-versus-different pointer | `353 x 636` | 636 | 192 | 72 | 37 |

The final rank gain over Cycle 398 is 161. The trace label is nonnegative and
normalizes all 353 menus to residual `8.214149943827704e-15`; exactly one
zero-effect class has trace label zero. It is retained only as a finite
arithmetic witness. No numerical grade is selected or interpreted as
probability.

The zero class/rank increment of the first-pointer family is an exact effect
identity at the incidence level. It does not erase the new continuation
process tags and is not generalized to the other four families.

## Physical M2 retention

For each of the seven banks, Cycle 401 rechecks

```text
E G_logical = G_physical E
```

at L=3 and held L=6. The two-use products remain inside the inherited local
role constraint and physical code space. Per bank, maximum matter-transition
and two-use controlled supports remain `20 M2` and `29 M2`; the two-use patch
is `65 M2` and inherited two-use overhead is `32 M2`.

If all seven banks are co-located, their two-pointer/program auxiliary account
is `63 M2`, or `86 M2` including one shared inherited base. Bank selection and
program preparation remain supplied; this is not autonomous bank genesis.

All seven banks and two-use products are checked under all 24 proper-cubic
frames, giving 168 bank-frame tests. Separately, all 353 composed/retained
menus are rotated and re-quotiented in every frame; the incidence matrix is
unchanged. The one-particle mass fixture and physical/logical contact
intertwiner are rechecked without retuning.

All 14 bank/size `E G_logical = G_physical E` residuals are zero; the largest
physical-isometry residual is `1.6177905143728115e-15`. Maximum held-L6
two-use leakage is `2.4699200717095924e-16`, with zero constraint residual.
Physical two-use frame residuals, branch failures, and incidence-frame
failures are zero. The largest rotated-menu completeness residual is
`2.843626111939516e-15`. The mass relative residual is
`2.220446049250313e-16`, and the contact-intertwiner residual is zero.

## Deletion and domains

Deleting one ordered fine branch from each program gives a visible
completeness defect, with minimum `0.04072349026477888`. Deleting one complete
coarse group from every one of the 255 presentations also gives a visible
defect, with minimum `0.04072349026477874`. Of the 3,277 tested final-branch CP
deletions, 3,157 delete a nonzero operator and change the Choi matrix by at
least `0.0007130951928696339`; 120 delete an exactly zero operator and are
explicitly inventoried as zero changes.

The composed-menu row deletion ledger is:

| family | deletion rank 191 | deletion rank 192 |
|---|---:|---:|
| ordered-fine | 20 | 31 |
| first-pointer marginal | 0 | 51 |
| second-pointer marginal | 35 | 16 |
| unordered-pair symmetrization | 20 | 31 |
| same-versus-different pointer | 32 | 19 |

Eight malformed grouping domains reject: empty family, empty group, missing
branch, duplicate branch, out-of-range branch, noninteger branch label, zero
pointer outcomes, and nine pointer outcomes. No host repair occurs.

## Supplied-structure inventory

The following remain explicit inputs:

1. the 51-program table and seven Cycle-398 fixed banks;
2. the decision to reuse the same program for both ordered uses;
3. preparation of the program state and two fresh blank pointers;
4. the five deterministic coarse-grouping rules and their admission;
5. the Cycle-383 13-decimal effect key and supplied effect-functionality
   premise;
6. the definition of an occurrence-level process tag as the Choi sum of its
   retained Kraus branches;
7. the positive-root one-use compiler and actual contact postcomposition;
8. the bank invocation and fixed two-use schedule;
9. the M2 embedding, local constraints, L=3/L=6 fixtures, and frame transport;
10. the mass and contact fixtures; and
11. the trace normalization witness.

No sampling rule, cross-program schedule, arbitrary-partition eligibility,
autonomous program/menu/grouping genesis, or universal menu eligibility is
supplied. No numerical grade, Born selector, probability interpretation,
actual-history sampler, Record-formation rule, or frequency theorem is
supplied or derived.

## Status-split provenance

The landed-in-pinned-main-base substrate is Cycle 317's bounded physical
dilation/compiler, Cycle 321's finite effect/program/process surface, and
Cycle 323's three-M2 fixed-carrier embedding. The Cycle-349/350/351 campaign
commit is `06cb17dcb26c7b6d0aa4377b6f1125bdc3d210bf`; it was not an ancestor of
pinned main base `0355ac4728f57d9fdc62cb27764bbd33e6e8b8df` at construction.
Cycles 381, 383, 385, 390, 394, 398, and 401 are campaign inputs or outputs at
Cycle-401 construction. Future landing is allowed and does not change this
historical certificate.

## No-Go Discipline Gate

The skill freshness check fetched and followed the complete current
`origin/main` no-go-discipline skill. The dirty worktree was not moved.

Gate disposition: PASS only for the finite census and first-pointer
effect-incidence redundancy. The four other families add effect classes and
rank, so any composition-wide nonforcing claim fails.

### N1 — Alternative route enumeration

| distinct route | actual result | honesty marker |
|---|---|---|
| ordered-fine branches | all 1,645 actual ordered branches add 250 classes and 41 rank cumulatively | ATTEMPTED |
| first-pointer marginal | recovers one-use effects; adds zero classes/rank but retains two-use process tags | ATTEMPTED |
| second-pointer marginal | adds 130 classes and 43 rank cumulatively | ATTEMPTED |
| unordered-pair symmetrization | adds 129 classes and 40 rank cumulatively | ATTEMPTED |
| same-versus-different pointer | adds 72 classes and 37 rank cumulatively | ATTEMPTED |
| effect/process separator route | preserves 785 effect/process pairs, including 50 equal-effect multi-process classes | ATTEMPTED |

Five routes positively defeat a broader no-rank reading; the narrow
first-pointer effect identity is the only zero-rank statement.

### N2 — Condition-independence audit

The load-bearing conditions are:

- `W1`: exactly the 51 Cycle-398 bank programs;
- `W2`: same program label on both uses;
- `W3`: exactly two ordered uses of the actual fixed carrier;
- `W4`: exactly the five declared exhaustive coarse-grouping rules;
- `W5`: equal-effect incidence quotient with occurrence-level process tags.

| pair | changing first automatically changes second? | reverse? | independent? |
|---|---|---|---|
| W1/W2 | no | no | yes |
| W1/W3 | no | no | yes |
| W1/W4 | no | no | yes |
| W1/W5 | no | no | yes |
| W2/W3 | no | no | yes |
| W2/W4 | no | no | yes |
| W2/W5 | no | no | yes |
| W3/W4 | no | no | yes |
| W3/W5 | no | no | yes |
| W4/W5 | no | no | yes |

No condition pair collapses; every finite claim retains all five.

### N3 — Hidden-condition scan

“Canonical” appears only for the explicit effect-key and ordered tuple/index
conventions and is covered by `W3`/`W5`. “Registered” is not used as a synonym
for eligibility. There are no unclassified occurrences of “we assume,” “by
construction,” “as is standard,” “the framework provides,” “bridge context,”
“background,” “naturally,” “obviously,” or “standard QFT.” No hidden condition
remains.

### N4 — Residual matching

| witness | witness residual | Cycle-401 residual | match? |
|---|---|---|---|
| Cycle 323 runner | fixed-carrier two-use tensor, physical embedding, support, covariance | actual source tensor and physical two-use controls | yes |
| Cycle 383 note/runner | equal effects can retain distinct CP processes | occurrence-level effect/Choi quotient with 50 multi-process effect keys | yes |
| Cycle 398 note/runner | `98 x 55`, exact rank-31 single-menu baseline and seven banks | exact starting incidence and physical program inventory | yes |

No prior negative witness is borrowed, and no nonmatching residual is used.

### N5 — Rhetoric audit

Tested resolutions are ordered branch, coarse outcome, complete composed menu,
effect-incidence class, occurrence-level CP tag, fixed bank, L3/held-L6
embedding, and proper-cubic frame. Cross-program, three-use, arbitrary
partition, arbitrary new-effect, and lattice-wide autonomous eligibility
resolutions are not tested. Therefore the only no-rank sentence is the exact
first-pointer effect-incidence identity within this grammar.

### N6 — Partial-closure path scan

No missing-primitive or new-axiom classification is made. Live constructive
extensions include cross-program ordered pairs, a supplied program rewrite
between uses, third/later uses, additional coarse partitions, and new source
program/effect families. Autonomous grouping eligibility is also separate.
These change declared conditions and remain available without constitutional
classification.

### N7 — Steelman

A hostile reviewer should argue: “Five hand-selected coarse families are a
small subset of all set partitions of an `n^2` outcome instrument, and using
the same program twice omits cross-program products and program rewrites. A
third use may create still more effects. Even the first-pointer zero-rank
result is only an effect identity; its process tag is new. Therefore Cycle 401
cannot establish composition-wide saturation or nonforcing.”

That steelman is correct and defeats every broader claim. It does not defeat
the finite positive rank table or the first-pointer effect identity, which
follows directly from exhaustiveness of the second use.

### N8 — Cross-cycle echo

| prior cycle | similar boundary | retirement mechanism | implication here |
|---|---|---|---|
| Cycle 383 | effect equality did not settle CP-process equality | retained effect and process quotients separately | equal composed effects cannot erase process tags |
| Cycle 390 | same-program two-use products were physically checked but not admitted as a broad menu family | Cycle 401 explicitly admits five composed presentations | physically present composition can add incidence only after a declared grouping surface |
| Cycle 398 | all 2–8 single-menu partitions on 55 classes saturated rank 31 | changing W5 to physical composition creates 581 classes and 161 rank | scoped saturation must not be generalized across grammar changes |

The cross-cycle echo is positive evidence against a broad negative claim.

## Optimal next constructive campaign

The highest-value next test changes only `W2`: compose ordered pairs of
different programs within one fixed bank, with an explicit physical program
rewrite between uses and a covariance/domain audit. This separates genuinely
cross-program process generation from the same-program effects measured here.

## Reproduction

```bash
python3 scripts/physical_two_use_composed_instrument_extension_cycle401_2026_07_18.py
```

Expected terminal line:

```text
RESULT PHYSICAL_TWO_USE_COMPOSED_INSTRUMENT_EXTENSION_EXACT_RANK_GAIN
```
