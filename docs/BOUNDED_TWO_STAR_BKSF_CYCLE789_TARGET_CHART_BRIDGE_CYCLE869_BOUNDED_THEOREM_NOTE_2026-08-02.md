# Bounded two-star BKSF bridge for the Cycle789 target chart — Cycle869

**Date:** 2026-08-02

**Claim type:** bounded_theorem

**Authority:** none

**Audit:** unset

**Result scope:** partial executable bridge

**Frozen target:**
[`BOUNDED_TWO_STAR_BKSF_CYCLE789_TARGET_CHART_BRIDGE_CYCLE869_TARGET_SPEC_2026-08-02.md`](work_history/repo/review_feedback/BOUNDED_TWO_STAR_BKSF_CYCLE789_TARGET_CHART_BRIDGE_CYCLE869_TARGET_SPEC_2026-08-02.md),
SHA-256
`2220b3f4a35fa1ad80a9069c0c2436bd7418fc5c9896b0bc62974340fa0b05e9`.

The frozen scratch target's historical `Retained source commit` / `Retained
inputs` labels are provenance wording only.  Cycle869 imports no audit grade;
the theorem note treats those inputs as landed, supplied science.

**Primary runner:**
[`frontier_cycle869_bounded_two_star_bksf_cycle789_chart_bridge_2026_08_02.py`](../scripts/frontier_cycle869_bounded_two_star_bksf_cycle789_chart_bridge_2026_08_02.py)

**Independent structural verifier:**
[`frontier_cycle869_bounded_two_star_bksf_cycle789_chart_bridge_independent_check_2026_08_02.py`](../scripts/frontier_cycle869_bounded_two_star_bksf_cycle789_chart_bridge_independent_check_2026_08_02.py)

Circuit ordinals, colours, transvection depth, and route-macro indices below
are supplied circuit structure.  They are not physical time, duration, rate,
or energy.

## Direct landed inputs

- the [Cycle703 local-Gauss/OpenReference BKSF two-cell
  intertwiner](RECURRENT_ENDPOINT_INCIDENCE_PHYSICAL_M2_COMPILER_TOURNAMENT_CYCLE703_NOTE_2026-07-25.md)
  and proper-cubic tableau surfaces;
- the [Cycle707 literal spacing-16 PatchGraph/repetition
  placement](LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md)
  and returned Manhattan router;
- the [Cycle709 signed four-transvection local-seam
  compiler](LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md)
  and radius-one serial rail cleanup;
- the [Cycle789 direct even-CAR character
  construction](THREE_REGISTER_COMPANION_INPUT_CIRCUIT_CYCLE789_BOUNDED_THEOREM_NOTE_2026-07-30.md),
  global-JW target rows, encoded sectors, and primary/held charts; and
- the [landed Cycle720 half-edge companion and one-edge gauge
  diagnostics](RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md)
  used to keep the live full-algebra route explicit.

The runner pins each directly imported landed Python file by SHA-256 and also
pins the complete dynamically loaded repo-local helper closure: 45 helper
paths, closure SHA-256
`41bb2d352bea3d43677b574fbf6cc111800590a344366ec4a60e1e708d233530`.
When Git metadata is present it additionally requires package base commit
`1900b64260f39f075c59f2e353079c44e8ede031` to exist.  The independent
verifier reconstructs the same closure and byte-pins the primary runner.  Both
resolve the repository root from their own `scripts/` locations; neither has
an absolute scratch path, archived-source path, or ambient `PYTHONPATH`
dependency.

## Result

Cycle869 gives an exact executable bounded bridge for one canonical seam,
plus an exact signed operator transport over its proper-cubic family.  Let
`P_OR` be the signed Cycle703
OpenReference seam row, `N` the natural PatchGraph-plus-rail address map, `E`
the Cycle709 four-transvection Clifford, and `T` the exact signed target
tableau.  The runner obtains

```text
E N(P_OR) E^dagger = T(P_OR)
```

with zero signed generator failures.  For the syndrome-ancilla Cycle789-style
character

```text
J_a(P) = H_a controlled(P) H_a,
```

the complete primitive tableau obeys

```text
E J_a(N(P_OR)) = J_a(T(P_OR)) E
```

on every ambient physical Pauli generator.  The explicit
`E^-1 ; J_source ; E` state circuit and the bounded target character differ by
only projective phase: a deterministic random state on the 20-site active
union has phase-aligned residual `3.602116257391375e-16` and phase numerically
equal to one.

The same local row cannot simply be substituted for every Cycle789 global-JW
edge target.  Its direct-basis commutator Gram differs on 22 pairs in primary
`(3,2,2)` and 76 pairs in held `(5,3,2)`.  This is a route-specific
discriminator of that literal substitution, not a representation-independent
negative.  The landed one-edge gauge has the exact full even-CAR algebra, but
its available logical orientation grows and is not compiled here as a bounded
literal common `E`.  Therefore the overall result is partial.

## Corrected literal resource inventory

The canonical two-cell code placement and the complete bridge resource are
not the same census.

| resource | exact count |
|---|---:|
| Cycle707 code-placement M2 | 39 |
| distinct character ancilla M2 | 1 |
| declared bridge-register M2 | 40 |
| declared registers touched by this word | 20 |
| declared registers not touched by this word | 20 |
| distinct routed-footprint locations | 155 |
| transit-only routing locations | 135 |

Thus the result has **39 code-placement M2**, **40 declared bridge-register
M2**, and **155 distinct routed-footprint locations**.  The primary runner
acceptance-gates all three counts, plus the 20/135 touched/transit split.  It
never calls 39 the complete bridge resource.

The physical `E` factor weights are `(14,13,1,1)`.  The source and bounded
character weights are 12 and 13.  The active word uses 20 sites of L1 diameter
24.  `E`, the character, and `E^-1` use `74/15/74` primitive gates.  The
returned realization has 3,327 NN gates, maximum route distance 24, zero
nearest-neighbour, operand-order, or route-return failures, and 111 macros
that detect deletion of their first nontrivial route SWAP.

The Cycle655 one-hot selection geometry enumerates and returns all 3,327 gates
with zero selected-order or token-return failures; deleting its first clock
shift changes the word.  This is not promoted to a blank-bypass controller.
The basis-H opcode retains the landed Cycle707 bypass residual
`1.0823922002923938` and work leakage one.

## Two overlapping stars and shared rails

The selected two-star legs are

```text
A: (0,0,0) --+y--> (0,1,0)
B: (0,1,0) --+x--> (1,1,0).
```

They share cell `(0,1,0)`.  Raw AB and BA differ on two symplectic generator
images.  The landed serial rail cleanup is exact in both directions:

```text
cleanup * AB = BA
cleanup * BA = AB.
```

The rail registers are indices 1 and 5 at literal sites `(-8,0,-8)` and
`(0,8,-8)`, distance 16.  Cleanup uses seven primitive and 37 returned NN
gates, with maximum route distance 16, zero route failures, and
`H-CNOT-H`/CZ residual `4.463374267214424e-16`.

The complete interface target stabilizer rank is acceptance-gated at 120,
equal to `168-48`; deleting one selected independent row must and does lower
the rank from **120 to 119**.  The two overlapping cube views are also gated
to exactly 80 shared abstract addresses: **76 graph-edge and four rail**
addresses.  They agree on every address, occupy 84 shared M2, and their 276-M2
union is exactly the primary placement.

## Primary, held, and route-specific chart discrimination

No parameters are refitted.

| fixture | cells / seams | literal code+rail M2 | global-JW edge max | bounded candidate physical max | diameter max | Gram tests / failures |
|---|---:|---:|---:|---:|---:|---:|
| `(3,2,2)` | `12 / 20` | 276 | 24 | 16 | 29 | `11,476 / 22` |
| held `(5,3,2)` | `30 / 59` | 717 | 36 | 17 | 29 | `75,466 / 76` |

The literal counts obey `18N+3M` and `<=27N`: `276<=324` and `717<=810`.
Every decoded candidate/global-JW difference is Z-only, with maximum weight 18
and 30.  The candidate is locally bounded, but its nonzero Gram census means
it is not the complete Cycle789 direct-character target algebra.

The landed half-edge companion independently has zero Gram, Hermiticity,
relation-centralizer, relation-commutator, or phase-contradiction failures on
both fixtures.  The landed one-edge gauge has zero common-`E` logical,
leakage, coordinate, stabilizer, or phase failures and uses every shared edge
register exactly once.  Its maximum local term weights are 17 and 18.
However, the available raw tableau logical-X maximum grows from 45 to 131;
Cycle869 does not present that object as a bounded physical isometry.

## Covariance and projective phase

The signed seam character and signed four-factor `E` diagrams close on all 24
proper-cubic frames.  Sequential and direct transports agree on all 576
ordered frame products with zero character, factor, group, cell, or phase-only
diagram failures.

This is a canonical/coframe-transported finite family.  It does not claim one
frozen coordinate word is invariant.  Signed operator covariance is exact;
the canonical state lift is executed separately up to its reported projective
phase.  The runner does not infer 576 dense state-vector executions.

## Active controls

- deleting the four transvections gives `(13,12,1,14)` generator failures;
- exhaustive search over every nonzero axis in `im(S-I)`, where
  `rank(S-I)=3`, finds no depth-one, -two, or -three word; depth four closes;
- deleting one controlled-character Pauli gives two tableau failures;
- a wrong character row gives 11, a wrong first sign gives 13, and reversing
  the factor schedule gives 14 failures;
- dirty repetition and dirty character-ancilla seeds retain the exact
  intertwiner with residuals below `3.7e-16`;
- all 3,164 returned `route_swap` gates are replayed and all 155 distinct
  routed labels return; and
- the interface cleanup and main route both detect nontrivial SWAP deletion.

Dirty-seed closure is finite robustness of the intertwiner, not autonomous
sector preparation, admission, enforcement, or repair.

## Supplied, derived, and open

Supplied:

- the frozen target at its historical source commit and the distinct current
  package base commit;
- Cycle703 OpenReference/local-Gauss BKSF charts and local incidence order;
- Cycle707 placement, repetition convention, Manhattan support order, and
  blank route corridors;
- Cycle709 transvection signs, supplied coframe, colour order, and cleanup
  predicate;
- Cycle789 direct character tags, global-JW chart, encoded sectors, finite
  boundary, and kept syndrome-register convention; and
- Cycle720 half-edge/edge-gauge diagnostics.

Cycle869-derived:

- the frozen `TERM_INDEX=2` controlled-character bridge and exact
  `E J = J E` signed tableau;
- the actual ancilla address, corrected 39+1 register inventory, and separate
  155-location returned-route footprint;
- the literal two-star AB/BA cleanup and gated 120-to-119/shared-address
  controls;
- the primary/held direct-substitution Gram discriminator; and
- the dirty-input, deletion, controller-selection, and 24/576 character
  transport tests.

Open:

- a bounded literal full-algebra `E` replacing the landed edge-gauge growing
  logical orientation;
- compilation of that `E`, every Cycle789 edge-gauge character, and `E^-1`
  on the primary and held shared banks;
- one complete three-register signed Cycle789 channel on the edge-gauge
  quotient; and
- autonomous sector preparation, enforcement, controller genesis, and repair.

## Exact boundary and no-go discipline

This theorem is finite: one canonical seam, its transported 24/576 operator
family, one two-star interface in a canonical open box, primary `(3,2,2)`, and
held `(5,3,2)`.  It makes no periodic, arbitrary-graph, all-volume,
constant-depth, autonomous-controller, occurrence, physical-time,
Record/Born, source/gravity, or prediction claim.

There is **no no-go** in Cycle869.  The nonzero Gram values reject only the
specified direct substitution.  Because no broad negative, named wall, or
axiom-pressure conclusion is made, N1--N8 is not invoked.

## Reproduction

From the repository root run:

```bash
python3 -u scripts/frontier_cycle869_bounded_two_star_bksf_cycle789_chart_bridge_2026_08_02.py
python3 -u scripts/frontier_cycle869_bounded_two_star_bksf_cycle789_chart_bridge_independent_check_2026_08_02.py
```

Expected terminals:

```text
CYCLE869_BOUNDED_TWO_STAR_BKSF_CHART_BRIDGE_PASS
CYCLE869_BOUNDED_TWO_STAR_BKSF_CHART_BRIDGE_INDEPENDENT_PASS
```

The independent checker does not import or execute the primary runner and
does not consume its receipt.  It reconstructs the literal route/resource
census, overlap ranks and addresses, primary/held Gram census, edge-gauge
boundary, and signed 24/576 diagrams directly from content-pinned landed
modules.  The primary runner separately performs the dense 20-site
state/tableau comparison.

Cold hashes for this package are:

```text
b3f9a8f1251f8156f24ba09126aa6d44599ccc93f95e73921417640d90d1071f  primary runner
f151e0241943b8edba311e8ca2b95556bc5530e186e77441fd4af2ba67d84ac4  independent verifier
15c65f747ca6440e90faf03d1f3ee1c857b9e7130d851aa613d516250541e51e  primary report
77dbd0ccf84389bfd2d9fdf818b5a91a95d684693a2033322f034da6c35d0794  independent report
```

Authority remains `none`; audit remains `unset`.  Only a separate audit lane
may apply a verdict.
