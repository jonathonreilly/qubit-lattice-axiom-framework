---
claim_id: admissibility_dirac_kahler_refined_alphabet_macrorealist_landscape_bounded_theorem_note_2026-08-26
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_REFINED_ALPHABET_MACROREALIST_LANDSCAPE_BOUNDED_THEOREM_NOTE_2026-08-26.md
claim_type: bounded_theorem
claim_scope: "Exact finite ranks for one twelve-column class-value refinement over six normalized contexts; a self-contained deterministic proof and evaluation of all four upper dichotomic three-slot facets on 48 declared design points; and calibrated values at seven declared q samples. No richer-alphabet, continuum-q, physical joint-law, macrorealist, hidden-variable, measurement, dynamics, gravity, or continuum conclusion is supplied."
runner: scripts/admissibility_dirac_kahler_refined_alphabet_macrorealist_landscape_2026_08_26.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the finite twelve-column and seven-q diagnostics do not supply an identified joint instrument, an exhaustive alphabet, or a continuum parameter classification"
source_of_blocker_text: review_loop
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Derive an identified joint instrument, then analyze a declared richer structured alphabet or the exact q-dependent rational family without replacing finite samples by a continuum claim."
conditional_surface_status: "stacked on unmerged ancestor artifacts; scientific content is proposed for retention and remains audit-required"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite-dimensional ranks, RREF pivots, normalization identities, deterministic truth-table facets, rational values, and probability-component sign checks"
audit_required_before_effective_retained: true
bare_retained_allowed: false
parent_ref: origin/physics-loop/toe-axiom-closure-block209-three-direction-rule-geometry-20260826
parent_commit: 07f0613c8730de54cd50403c809f7102bc1534bf
current_main: 76df4becc8233080bc5a10a4baf55f83e80f8f2d
registered: 0
adopted: 0
axiom_movement: none
---

# Finite refined-alphabet ranks and complete four-facet null diagnostics

**Date:** 2026-08-26

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — author proposal only; independent audit is
required before any effective retained status.

**Standing:** conditional support on an unmerged PR stack. Nothing is
registered, adopted, or added to the axioms.

## Result

The runner preserves five exact finite results.

1. On the declared Block 171 bench, the twelve outcomes
   `(x,k)` with `x in {0,1,2,3}` and
   `k in {0,1/5,-1/5}` all have support. The single `W9-L5` system has
   shape `(5,12)`, ranks `(4,4)`, and is solvable.
2. Stacking the six declared contexts
   `(W9,W2) x (5,4,2)` with one unit-sum row gives a `25 x 12`
   coefficient system with ranks `(8,9)`. The augmented column is an exact
   RREF pivot, so no unit-sum real twelve-weight reproduces those six
   marginals. This excludes that declared weight before nonnegativity is
   considered; it does not exclude arbitrary unnormalized real vectors,
   richer alphabets, or hidden-variable models.
3. Context normalization creates six exact coefficient-row relations:
   for each context, the sum of its four component rows equals the unit-sum
   row, on both coefficient and target sides. Therefore the 25-row
   coefficient matrix has rank at most `19`. Neither 19 nor 25 outcomes is a
   generic spanning threshold; outcome count alone proves no
   richer-alphabet consistency or simplex result.
4. For deterministic dichotomic values `Q1,Q2,Q3 in {-1,+1}`, define
   `Cij=Qi Qj`. The four upper facets are

   ```text
    C12 + C23 - C13 <= 1
    C12 - C23 + C13 <= 1
   -C12 + C23 + C13 <= 1
   -C12 - C23 - C13 <= 1
   ```

   Their sign triples have product `-1`. On all eight assignments each
   left side is exactly `1` or `-3`, which proves the finite deterministic
   bound without importing a physics premise.
5. Under the expressly proposed W9 formation-weight reading, all four facets
   are evaluated on four chains and three balanced cell splits: `48` exact
   values. The 52-profile calibration set contains all four record-free
   free-level profiles and all 48 pinned profiles, hence every profile used by
   the landscape; all `208` components are nonnegative and every profile sums
   to one. Every facet value is strictly below
   one. The maximum remains unique at
   `((3,4,5),01|23,a)`; it is the exact 944/945-digit rational carried by
   the runner, and `18 K_max < 1`. Including the fourth facet changes the
   minimum to `((3,4,5),03|12,d)`, approximately `-0.045148834` for
   display only.

At the seven declared temporal-dial values
`{-2,-1,-1/2,0,1/2,1,2}`, all `392` used profile components are
nonnegative and every profile is normalized. The sampled `K` values are
positive, nonmonotone, and below one, with maximum at `q=-2` and minimum at
`q=1/2`. This is a seven-point null sample, not a theorem for all real
`q`.

## Authority and dependencies

The construction is inherited from, and does not alter:

- [Block 171 committed bench](ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md)
- [Block 202 finite substitution diagnostics](ADMISSIBILITY_DIRAC_KAHLER_RECORD_PINNING_MIXTURE_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-08-26.md)
- [Block 209 finite three-direction gluing](ADMISSIBILITY_DIRAC_KAHLER_THREE_DIRECTION_RULE_GEOMETRY_BOUNDED_THEOREM_NOTE_2026-08-26.md)
- [Minimal Axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Axiom/premise registry](audit/data/axiom_premise_nodes.json)
- [Gravity-mainline campaign charter](../.claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md)

The exact implementation is
[the Block-210 runner](../scripts/admissibility_dirac_kahler_refined_alphabet_macrorealist_landscape_2026_08_26.py).

## Refined unit-sum system

For each outcome column, the runner reads the landed Block 171 profile in each
of six contexts. The target is the corresponding record-free profile. The
last row imposes `sum_o w_o=1`.

The exact measurements are:

| system | shape | rank coefficient | rank augmented | conclusion |
| --- | ---: | ---: | ---: | --- |
| one refined context `W9-L5` | `5 x 12` | 4 | 4 | real unit-sum solutions exist |
| six-context refined stack | `25 x 12` | 8 | 9 | no real unit-sum solution |
| Block 202 class-zero baseline | `25 x 4` | 4 | 5 | no real unit-sum solution |

The refined RREF pivot columns are
`(0,1,3,4,6,7,9,10,12)`; column `12` is the augmented column. This is a
literal exact incompatibility certificate for the declared affine system.

The phrase “linear inconsistency” is used only for the linear equations after
the unit-sum affine row is included. It must not be read as exclusion of every
unnormalized real vector. Nonnegativity is not needed for this declared
unit-sum incompatibility, but it would be needed to interpret a consistent
weight as a probability distribution.

## Complete finite facet landscape

The diagnostic correlation is imposed as

```text
Cij = sum_x sum_y s(x)s(y) w_i(x) P(y at j | pin x at i).
```

Here `w_i` is the record-free W9 profile, and the pinned profile is treated as
a conditional. Neither identification is derived from the framework. Thus the
48 values are conditional algebraic diagnostics, not observed temporal
correlations.

The four chains are `(2,3,4)`, `(2,3,5)`, `(2,4,5)`, and `(3,4,5)`.
The splits are `01|23`, `02|13`, and `03|12`. Combining them with all
four deterministic facets gives `4 x 3 x 4 = 48` exact evaluations.

Probability calibration is part of the theorem, not an inference from
normalization:

- landscape: a 52-profile calibration superset containing every used profile,
  208 components, zero normalization defects, and zero negative components;
- seven-q sample: 392 components, zero normalization defects, zero negative
  components.

The result is null: all evaluated facets are strictly satisfied. A satisfied
necessary inequality does not establish macrorealism, noninvasive
measurability, or physical correctness of the proposed joint reading.

## Seven-point dial boundary

At the committed spatial dial
`{g_re:1/3,g_im:1/4}`, the holonomy action has zero remaining free symbols.
At the best landscape design, the seven exact temporal-dial samples are:

| q | display-only K |
| ---: | ---: |
| `-2` | `+0.075571541` |
| `-1` | `+0.074844544` |
| `-1/2` | `+0.069580018` |
| `0` | `+0.055673917` |
| `1/2` | `+0.045250004` |
| `1` | `+0.047294914` |
| `2` | `+0.056216274` |

The exact values, not these decimal displays, are gated. They show finite
movement and one sampled turning point. They do not prove that no other real
`q` crosses the bound: a nonzero rational function can agree with any finite
sample and differ elsewhere. An all-`q` claim would require deriving the
exact `K(q)`, locating its real poles and extrema, and proving the relevant
inequality on every declared interval.

## Interpretation boundary

- “Alphabet” means twelve declared substitution columns. It does not mean an
  exhaustive measurement-outcome space.
- “Landscape” means 48 finite facet evaluations, not a parameter space.
- The ranks exclude one unit-sum real twelve-weight. They do not exclude
  unnormalized real vectors, richer structured alphabets, or classical models.
- The W9 formation-weight and pinned-conditional identifications are proposed,
  not derived.
- The four-facet and seven-q null results neither establish macrorealism nor
  make a violation impossible.
- No landed number is corrected, and no measurement postulate, Born rule,
  dynamics, gravity, generic-parameter theorem, or continuum limit is supplied.

## No-Go Discipline Gate

The gated negative is: **the declared twelve-column, six-context affine system
has no unit-sum real solution, and the complete four-facet diagnostic has no
violation among the 48 landscape evaluations or seven q samples.** No stronger
classical-model or continuum no-go is claimed.

### N1 — alternative-route enumeration

| normalized route | attack and exact outcome | honesty marker |
| --- | --- | --- |
| four-column baseline | Re-run the class-zero Block 202 alphabet on the same six contexts; ranks `(4,5)` remain incompatible. | `ATTEMPTED` |
| twelve-column class-value refinement | Add the first declared class-value triple; the single context is solvable but the six-context unit-sum stack has ranks `(8,9)`. | `ATTEMPTED` |
| single-context relaxation | Remove five contexts; ranks `(4,4)` show that the declared columns are not intrinsically inconsistent. | `ATTEMPTED` |
| complete deterministic facet family | Add the previously omitted fourth upper facet and check all 48 finite values; no evaluated violation appears. | `ATTEMPTED` |
| temporal-dial sample | Evaluate the best declared design at seven exact q values with full probability calibration; no sampled violation appears, but continuum q stays open. | `ATTEMPTED` |
| alternate joint instrument | Treat the W9 formation weight and pinned conditional as imposed rather than identified; the resulting values are conditional and cannot close the physical-instrument wall. | `ATTEMPTED` |

The routes differ in terminal obligation: column enrichment, context removal,
polytope completion, parameter sampling, and joint-instrument identification.
None is marked ruled out by prior authority.

### N2 — wall-independence audit

The collapsed wall set is:

- `W1`: the declared twelve structured outcome columns;
- `W2`: the declared six contexts together with unit sum;
- `W3`: the proposed W9 formation-weight/conditional joint reading;
- `W4`: the finite 48+7 design and q set;
- `W5`: componentwise probability calibration.

| pair | closing first closes second? | closing second closes first? | independent? |
| --- | :---: | :---: | :---: |
| `W1,W2` | no | no | yes |
| `W1,W3` | no | no | yes |
| `W1,W4` | no | no | yes |
| `W1,W5` | no | no | yes |
| `W2,W3` | no | no | yes |
| `W2,W4` | no | no | yes |
| `W2,W5` | no | no | yes |
| `W3,W4` | no | no | yes |
| `W3,W5` | no | no | yes |
| `W4,W5` | no | no | yes |

More columns need not change contexts; identified probabilities need not satisfy
a facet; and a finite null sample does not identify a joint law or classify a
continuum.

### N3 — hidden-wall scan

| phrase class | occurrence and classification |
| --- | --- |
| “declared” / “by construction” | Bench, alphabet columns, contexts, joint diagnostic, splits, facets, and q samples are imposed choices. |
| “standard” | No standard physical instrument is imported. The deterministic facet proof is supplied explicitly. |
| “framework provides” / “naturally” / “obviously” | No load-bearing positive occurrence appears. The first class-value triple is one attempt, not a natural exhaustive alphabet. |
| “generic” / “threshold” | The former 25-outcome threshold is withdrawn. Six normalization relations instead prove only a rank ceiling of 19. |
| “probability” | Sum one and componentwise nonnegativity are separately measured before that word is used. |
| “registered” / “canonical” | Nothing is registered or adopted, and no premise weight is inferred. |

No hidden condition expands `W1-W5`.

### N4 — residual matching

| cited source | source residual | residual here | exact match? | disposition |
| --- | --- | --- | :---: | --- |
| [Block 171](ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md) | constructs the finite bench and profiles | unit-sum compatibility and four-facet values | no | construction authority only |
| [Block 202](ADMISSIBILITY_DIRAC_KAHLER_RECORD_PINNING_MIXTURE_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-08-26.md) | four-column common-weight obstruction | twelve-column obstruction on the same six contexts | partial | baseline comparison only; not proof for the refined columns |
| [Block 209](ADMISSIBILITY_DIRAC_KAHLER_THREE_DIRECTION_RULE_GEOMETRY_BOUNDED_THEOREM_NOTE_2026-08-26.md) | finite three-direction gluing and face-offset boundary | refined marginal weights and finite facets | no | stack authority only, not a witness |
| [Axiom/premise registry](audit/data/axiom_premise_nodes.json) | accepted premise inventory | physical joint-instrument identification | no | supplies no such selector |

Only the current exact RREF and evaluated facet table certify the current
negative statements.

### N5 — rhetoric audit and five resolution levels

N5: per_element: The twelve declared substitution outcomes, six marginal contexts, four deterministic facet signs, and seven q values are finite imposed algebraic objects. They do not constitute a measurement alphabet, identified joint law, continuum dial, hidden-variable model, or physical selector; nothing is registered or adopted.
per_site: The single declared W9-L5 context is solvable at ranks (4,4), while the six-context unit-sum real system has ranks (8,9) with an augmented pivot. Six normalization relations cap the 25-row coefficient rank at 19; they do not create an outcome-count threshold, and every richer structured alphabet remains open.
per_mode: The complete four deterministic upper facets are evaluated on four chains and three splits, giving 48 exact values. The 52-profile calibration set contains every landscape profile used; all profiles sum to one and all 208 components are nonnegative. Every facet is strictly below one, conditional on the proposed W9 formation-weight reading.
per_block: At the seven declared q values, all 392 used profile components are nonnegative and the profiles are normalized; the sampled K values move nonmonotonically and stay below one. No continuum-q conclusion, no claim that tuning cannot cross, and no structurally different instrument is excluded.
lattice_wide: The results are a finite null sample and a twelve-column incompatibility certificate on one bench. They neither establish macrorealism nor exclude classical models, richer alphabets, joint-pin instruments, other carriers, or other parameter values; all content remains proposed_retained and TOE movement is zero.

The runner checks all five lines verbatim, and the canonical cache preserves
them in executed evidence.

### N6 — partial-closure path scan

| possible path | status | what it could close |
| --- | --- | --- |
| richer structured class-value family | open construction route | could test whether additional columns restore a unit-sum or simplex solution |
| exact parameterized column theorem | open algebraic route | could prove generic rank only after a declared column family and minors are derived |
| identified joint instrument | open physical bridge | could justify interpreting the finite facet values as temporal correlations |
| exact rational `K(q)` analysis | open continuum route | could classify real-q intervals after poles and extrema are proved |
| joint-pin or stronger-coupling instrument | open instrument route | could explore facet values outside the single-pin construction |

No new axiom is declared necessary, and no open route is converted into a
permanent impossibility.

### N7 — hostile steelman

A hostile reviewer should reject “the refined alphabet excludes a classical
model”: a still richer structured alphabet may solve the six-context problem,
and the current contradiction includes unit sum. The reviewer should also
reject “tuning cannot violate the bound”: seven samples cannot constrain a
nonconstant rational function between or beyond them. Finally, even a complete
finite four-facet table is conditional on the proposed formation-weight and
conditional-profile identifications. The strongest constructive attacks are to
derive a parameterized column family and solve its simplex feasibility, derive
the exact `K(q)` inequality on real intervals, and construct an identified
joint instrument. Those terminal obligations remain open. None changes the
current exact ranks, probability checks, or finite null values.

### N8 — cross-cycle echo and decision cut

[Block 202](ADMISSIBILITY_DIRAC_KAHLER_RECORD_PINNING_MIXTURE_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-08-26.md)
already leaves the joint identification and richer instrument open.
[Block 209](ADMISSIBILITY_DIRAC_KAHLER_THREE_DIRECTION_RULE_GEOMETRY_BOUNDED_THEOREM_NOTE_2026-08-26.md)
likewise preserves finite algebra while refusing to infer a physical selector
or unbuilt transport. Those analogous walls are not treated as closed by a
finite sample here. Their repair mechanism—derive the missing map or structured
family and then test it explicitly—remains the required next step.

Decision: retain the exact finite rank, normalization-relation, truth-table,
probability-calibration, and 48+7 value results as `proposed_retained`.
Withdraw the 25-outcome threshold, incomplete three-facet landscape,
normalization-only probability reading, all-q/no-tuning inference, arbitrary
real-vector exclusion, and any physical or classical-model conclusion.
Register no premise, adopt no object, and move no TOE percentage.

## Verification contract

The runner declares 29 claim-only mutations. Each must fail exactly its mapped
gate. Baseline output must remain below the runner-output cap, and the canonical
cache must bind the runner plus every declared authority input.

## Decision

This block is useful finite evidence. Its repaired form keeps the exact
twelve-column incompatibility, complete four-facet null landscape, and seven-q
sample while preserving every scientifically live escape that the finite
calculations do not close.
