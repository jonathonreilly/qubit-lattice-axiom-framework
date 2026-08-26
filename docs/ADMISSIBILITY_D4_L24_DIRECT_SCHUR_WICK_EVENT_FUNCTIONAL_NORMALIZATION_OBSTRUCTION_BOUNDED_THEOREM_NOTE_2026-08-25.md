---
claim_id: admissibility_d4_l24_direct_schur_wick_event_functional_normalization_obstruction_bounded_theorem_note_2026-08-25
claim_type: bounded_theorem
claim_scope: "On the fixed Block-192 periodic L24, m=2/7 six-fixture action family, the Block-194 rank-four eight-projector PVM, the labeled incoming/outgoing-to-upper/lower exterior-form coordinate identification, and the exact determinant functional preregistered in Block 201, the action/event intertwiner exists as diag(z_in I16,z_out I16) with U(1)^2 isometric gauge and one physical weight orbit. All seven nonempty restrictions Q_0,Q_2,Q_4,Q_02,Q_04,Q_24,Q_024 reconstruct directly and from covariance/Schur restriction on all six carriers and nine squared radii. Nevertheless the first required D1 one-crossing test fails: all eight exact amplitudes equal one large negative rational, all eight raw weights equal about 3.9383002918494e13 instead of 1/8, and their raw sum is about 3.15064023347954e14 instead of one. The preregistered stop seals gluing, the 729-word census, other-carrier probability values, and the selector. This rejects only the displayed unrescaled typed determinant functional; it is not a no-go for other direct functionals, a covariant POVM/null outcome, support/filling, Nambu or OS/GNS constructions, an open causal boundary, Record/Born dynamics, gravity, or a TOE."
parents:
  - admissibility_d4_l24_exterior_natural_e8_insertion_obstruction_bounded_theorem_note_2026-08-25
upstream_dependencies:
  - minimal_axioms
actual_current_surface_status: demotion
target_claim_type: bounded_theorem
trace_class: negative_route_pruning
reachability_to_target: rejects_one_frozen_direct_functional_and_promotes_causal_boundary_portfolio_route
artifact_role: theorem
conditional_surface_status: partial-narrowing
hypothetical_axiom_status: unchanged
admitted_observation_status: none
target_claim_id: admissibility_d4_l24_direct_schur_wick_event_functional_2026-08-25
target_blocker_text: "The action/event coordinate map exists and its gauge is harmless, but the frozen determinant law does not produce a normalized raw one-event distribution even on the first required D1 boundary."
next_trace_action: "Execute the L12 cyclic-to-causal boundary kill gate before further event-functional enumeration; keep covariant POVM/null and action-derived support as the next insertion alternatives."
claim_type_reason: "The carrier identities, CAR commutant, intertwiner gauge quotient, determinant-lemma engine, and exact D1 normalization contradiction are finite exact algebra. Standing is demoted because only one fixed functional is rejected and materially different action-to-probability constructions remain open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
preregistration_commit: f80e9673ad836e14e1478318198d063190f24294
discarded_prepacket_float_pilots: 1
primary_checks_passed: 6
primary_mutations_rejected: 31
independent_checks_passed: 11
independent_mutations_rejected: 17
physical_fixtures_typed: 6
frozen_squared_radii_checked: 9
boundary_restrictions_per_fixture: 7
intertwiner_linear_family_dimension: 2
intertwiner_isometric_gauge: U1_squared
intertwiner_physical_weight_orbits: 1
d1_one_shot_amplitude_classes: 1
d1_one_shot_weight_classes: 1
d1_raw_normalization: failed_exactly
d1_gluing: sealed_by_one_shot_failure
d1_full_census: sealed
other_carrier_probability_values: sealed
strong_history_positivity: not_tested
causal_process: sealed
no_go_discipline_gate: PASS_for_exact_frozen_functional_FAIL_for_broad_probability_or_history_no_go
negative_disposition: partial-narrowing
minimal_axiom_update: none
obligation_retirement: 0
toe_percentage_movement: 0
---

# L24 Direct Schur/Wick Event-Functional Normalization Obstruction

**Date:** 2026-08-25

**Campaign block:** 201

**Type:** `bounded_theorem`

**Standing:** proposed bounded theorem; independent audit unset

Primary runner:
[`admissibility_d4_l24_direct_schur_wick_event_functional_2026_08_25.py`](../scripts/admissibility_d4_l24_direct_schur_wick_event_functional_2026_08_25.py).

Independent no-import checker:
[`independent_admissibility_d4_l24_direct_schur_wick_event_functional_2026_08_25.py`](../scripts/independent_admissibility_d4_l24_direct_schur_wick_event_functional_2026_08_25.py).

SHA/input-bound cached stdout:
[`primary`](../logs/runner-cache/admissibility_d4_l24_direct_schur_wick_event_functional_2026_08_25.txt)
and
[`independent`](../logs/runner-cache/independent_admissibility_d4_l24_direct_schur_wick_event_functional_2026_08_25.txt).

## 1. Result Up Front

Block 201 answers the most important uncertainty left by Block 200: the
incoming/outgoing action pair and the Block-194 event fiber are not merely
equal-dimensional.  They have one labeled exterior-form coordinate
identification, unique up to independent incoming and outgoing phases.  The
whole `U(1)^2` family gives identical determinant weights, so no state,
boundary, phase, or fitted intertwiner is needed at this interface.

That positive structural result does not rescue the proposed probability
law.  On the first preregistered D1 one-crossing gate, all eight outcome
amplitudes are the same exact negative rational.  Consequently all eight raw
weights are equal but enormous rather than `1/8`, and their sum is enormous
rather than one.  The mismatch is not a small numerical residual.

The functional therefore fails before gluing.  No post-normalization,
per-depth factor, occupation conditioning, or fitted prefactor is attempted.
The full D1 history census, other five carrier probability tables, and
selector remain sealed.

This is genuine route pruning but zero TOE closure: it retires no obligation,
changes no axiom, and moves no lane percentage.  It says that this exact
functional is wrong as a raw probability law, not that the action cannot
generate probabilities by another construction.

## 2. Registration And Protocol Disclosure

The frozen packet landed before exact target execution at
`f80e9673ad836e14e1478318198d063190f24294`.  It fixes:

- all six physical incoming/outgoing carriers and all seven nonempty boundary
  subsets of `{0,2,4}`;
- the labeled action/event intertwiner problem and its complete gauge quotient;
- the determinant signs, `det(Q_B)^(-1)`, slot order, conjugate leg, and
  `w=conjugate(a)a`;
- raw one-shot `1/8` and sum-one as the first target; and
- gluing and every larger census as conditional on that first target passing.

Before preregistration, one floating-point pilot used bare `J=I`.  Its full
provenance and output are disclosed in the packet's
[`PREFLIGHT_WITNESSES.md`](../.claude/science/physics-loops/toe-axiom-closure-block201-direct-schur-wick-event-functional-20260825/PREFLIGHT_WITNESSES.md).
It is discarded as evidence, supplied no exact target, and was not used as an
expected value, threshold, mutation oracle, or formula-repair guide.  The
evidentiary runners recompute the target exactly after the packet freeze.

## 3. Seven Exact Action Restrictions On Six Typed Carriers

Let

\[
 Q_s=I_{12}+{2I_{12}-V-V^T\over4(m^2+s)},\qquad m={2\over7},
\tag{1}
\]

where `V` is the periodic coarse-time shift.  For each nonempty
`B subset {0,2,4}`, the scalar restriction is

\[
 S_B=(Q_s)_{BB}-(Q_s)_{BI}(Q_s)_{II}^{-1}(Q_s)_{IB}
     =\bigl((Q_s^{-1})_{BB}\bigr)^{-1}.
\tag{2}
\]

The runners construct `Q_0,Q_2,Q_4,Q_02,Q_04,Q_24,Q_024`, verify every nested
Schur and determinant identity, and then pair the incoming and outgoing
`C^16` fibers in time-major, sector-major, form-mask-minor order.  The six
squared-radius pairs are

| fixture | incoming | outgoing |
|---|---:|---:|
| D1 | `0` | `1` |
| D2 | `0` | `2` |
| D3 | `0` | `3` |
| H1 | `1` | `5/4` |
| H2 | `3/2` | `(7+sqrt(3))/4` |
| X1 | `3/4` | `(10+sqrt(3))/4` |

For each physical endpoint `p`, the internal factor

\[
 D(p)=mI_{16}+i\sum_{a=1}^3\sin p_a\,G_a
\tag{3}
\]

obeys

\[
 D(p)^\dagger D(p)=(m^2+s(p))I_{16}.
\tag{4}
\]

Thus the paired restrictions are fully typed and invertible.  Block 200
constructed only the D1 `Q_024/Q_02` pair; the other subsets and five carriers
are honest Block-201 extensions rather than inherited results.

## 4. The Intertwiner Exists And Its Gauge Is Harmless

Let `e_S`, ordered by four-bit mask, be the common exterior-form basis.  The
labeled coordinate map is

\[
 J_0(|\mathrm{in}\rangle\otimes e_S)
   =|\mathrm{upper}\rangle\otimes e_S,
 \qquad
 J_0(|\mathrm{out}\rangle\otimes e_S)
   =|\mathrm{lower}\rangle\otimes e_S.
\tag{5}
\]

The runner does not infer (5) from dimension.  It rebuilds the form labels,
all four creation/annihilation pairs, and sector parity.  Commutation with the
joint number projectors makes either `C^16` block diagonal in the 16 distinct
occupation signatures; the connected creation graph then makes every
diagonal entry equal.  The common `C^16` CAR commutant is therefore scalar.
Sector parity removes off-diagonal sector maps, giving the complete linear
family

\[
 J=\operatorname{diag}(z_{\rm in}I_{16},z_{\rm out}I_{16}).
\tag{6}
\]

Isometry reduces (6) to `U(1)^2`.  Reflection and proper-cubic transformations
are checked as family equations, with coordinate reflection kept distinct
from the OS/fiber reflection.  No untracked off-diagonal connector is added
to manufacture a common phase.

For a crossing-independent

\[
 D=\operatorname{diag}(e^{i\phi_{\rm in}}I_{16},
                       e^{i\phi_{\rm out}}I_{16}),
\tag{7}
\]

every paired `Q_B` commutes with `I_B tensor D`, and every determinant matrix
is similar to its `J_0` representative.  Hence the two-phase family has one
physical weight orbit.  The runner also gives an exact counterexample showing
that crossing-dependent sector phases do not commute with temporal
off-diagonal blocks and are not gauge.

## 5. Frozen Determinant Functional

For a word `alpha=(alpha_1,...,alpha_n)` on boundary `B`, define

\[
 a_B(\alpha)={1\over\det Q_B}
 \sum_{\epsilon\in\{0,1\}^n}(-1)^{n-|\epsilon|}
 \det\!\left[Q_B+\bigoplus_j
       (I-\epsilon_j\widetilde F_{\alpha_j})\right],
 \qquad
 w_B(\alpha)=\overline{a_B(\alpha)}a_B(\alpha).
\tag{8}
\]

Each effect has rank four.  Writing `F=XV^dagger`, the matrix determinant
lemma reduces every word-dependent determinant to

\[
 \det(M-XV^\dagger)=\det(M)
 \det(I-V^\dagger M^{-1}X),
\tag{9}
\]

whose largest order at three crossings is 12.  Exact direct determinants on
two pre-target controls reproduce (9).  The empty word is one, all eight
effects sum to identity, and an explicit matrix unit distinguishes that
effect coarse-graining from nonselective Lueders dephasing.

Equation (8) gives entrywise nonnegative atomic weights only.  Even a later
normalization/gluing pass would establish at most a classical commutative
Euclidean cylinder.  No off-diagonal decoherence functional or strong
history positivity is constructed here.

## 6. Exact D1 One-Shot Failure

For the required D1 boundary at coarse site zero, all eight labels give

\[
 a_0(\alpha)=-{N\over D},\qquad \alpha=0,\ldots,7,
\tag{10}
\]

with the exact integers

```text
N=397057821388476763185195891442395249257078436444087984809836687566566563840050849647266598466270625713533761064056647307548182501068985607888603636627975935117954129061303984342653446982215785550975402431313254676023846982044788663353698475001064197807156278993628303195366426831296563917183339265105791737073513557189790838581024525882906036383349509472046279698077946413023227143006066426916169897634076977444937443505939856255166534452720109532059
D=63270219555459197323100187647803987052156730384784430421550103162941535898462076233901120801713999612809163369718150479244703352556860717802483333296864995503964745778194203949963194925430371421092311245610180742914064821237891482901404250218173737346539993240033700404612795247430773060191883986857211550274144992431328567741044021986140002025474078956226407892181849484824938629278092596014227154343045785190400000000000000000000000000000000
```

Therefore

\[
 w_0(\alpha)=\left({N\over D}\right)^2
 \simeq 3.93830029184942757\times10^{13}\ne {1\over8},
\tag{11}
\]

and

\[
 \sum_{\alpha=0}^7w_0(\alpha)
 =8\left({N\over D}\right)^2
 \simeq3.15064023347954206\times10^{14}\ne1.
\tag{12}
\]

The equal labels show that this is not a broken outcome symmetry.  The exact
rational mismatch shows that it is not roundoff.  Gauge similarity shows that
choosing another allowed intertwiner cannot change it.

Because (11)--(12) fail, the preregistered residual

\[
 \Delta_{00}^{02}=\sum_{c=0}^7w_{024}(0,0,c)-w_{02}(0,0)
\tag{13}
\]

is not evaluated.  The `729`-value D1 census, all other carrier probability
values, and the selector are likewise not evaluated.

## 7. Scientific Disposition And Axiom Consequence

The positive result is that the action/event typing problem is clear at this
surface: a physical coordinate intertwiner exists and its residual gauge is
probability-invisible.  The negative result is that the frozen determinant
law has the wrong absolute normalization at its first required event.

Dividing (11) by its sum would manufacture a normalized table, but it would
insert a new per-depth rule after reading the target and would no longer be
the preregistered action-derived functional.  The same applies to a boundary
state, filling, selected occupation sector, or fitted prefactor.  Those can be
studied only as newly typed physical constructions with their own authority
and retirement audit.

No minimal-axiom edit follows.  Admissibility requires a probability
distribution but does not say that (8) supplies it.  One failed candidate
formula is evidence about downstream realization, not evidence that the
axiom is wrong or incomplete.  There is zero obligation retirement and zero
TOE percentage movement.

The efficient pivot is the independently ranked L12 cyclic-to-causal boundary
gate.  The covariant POVM/null and action-derived support routes remain the
next insertion alternatives.  Gravity remains separately live and is not
inferred from this event-functional result.

## 8. No-Go Discipline Gate

### N1 -- alternative-route enumeration

The broad claim “the action cannot generate probabilities” is rejected.  The
narrow claim is only that the exact functional (8), with its frozen carrier,
typing, and no-rescaling rule, fails a required raw D1 normalization gate.

| family | attack on the narrow result | outcome and honesty marker |
|---|---|---|
| carrier reconstruction | replace an incorrectly cut or ordered `Q_0` by the literal action restriction | `ATTEMPTED`: direct Schur and inverse-covariance routes agree for all seven subsets on all six typed carriers; D1 `Q_0` is not an indexing shortcut |
| action/event typing | derive a nontrivial physical map instead of assuming equal dimensions | `ATTEMPTED`: the complete CAR/sector solution is (6), with the labeled representative (5) |
| residual intertwiner gauge | vary the two sector phases to change the target weights | `ATTEMPTED`: exact similarity under (7) gives one physical weight orbit; crossing-dependent phases are rejected |
| determinant evaluation | challenge rank-four compression, signs, or `det(Q)^{-1}` using a disjoint direct calculation | `ATTEMPTED`: exact direct controls and the no-import checker reproduce the frozen expansion and the D1 mismatch |
| event relabeling or context covariance | permute the eight outcomes or rotate/reflect the detector context | `ATTEMPTED`: all eight exact amplitudes and weights are equal, so every relabeling preserves the same normalization failure |
| post-normalization or occupation conditioning | divide by the observed sum or select one Fock sector | `ATTEMPTED`: this algebraically changes the raw law but violates the frozen terminal obligation and becomes a different imported functional, not a rescue of (8) |

These are six materially different object/mechanism/obligation challenges to
the exact narrow claim.  A POVM/null outcome, support/filling, Nambu, OS/GNS,
open boundary, or a different direct functional changes the primary object
and remains live; none is presented as failing here.

### N2 -- wall-independence audit

There is one load-bearing failed obligation, `W_N`: raw D1 one-event
normalization for (8).  Intertwiner existence and gauge invariance pass.
Gluing, the D1 census, other carriers, and the selector are downstream sealed
targets, not additional independent walls.  A pairwise independence table is
therefore unnecessary after collapsing the raw list to `{W_N}`.

### N3 -- hidden-wall scan

- “Registered” and “frozen” identify the preregistered carrier, effect, and
  formula authorities; they do not grant probability status.
- “Canonical” is not used to select `J`.  The labeled map is derived, and the
  full residual family is quotiented exactly.
- “By construction” is used only for displayed definitions whose identities
  the runners independently recompute.
- No “standard QFT,” background state, bridge context, natural filling, or
  assumed boundary is used.
- The no-post-normalization rule is load-bearing and explicit in the target,
  not a hidden condition.

No hidden condition enlarges the single narrow wall.

### N4 -- residual matching

| cited witness | witness residual | present residual | match / use |
|---|---|---|---|
| [Block 194 PVM/M2 note](ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md) | derives the eight rank-four effects, reflection, and detector orientation | raw normalization of (8) | input authority only; not negative evidence |
| [Block 199 event-history note](ADMISSIBILITY_D4_L24_EVENT_HISTORY_INTERFACE_HANKEL_PROCESS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md) | complete one-/two-event tables do not select a unique triple law | D1 one-event normalization of (8) | no; motivation only and dropped as proof |
| [Block 200 exterior-insertion note](ADMISSIBILITY_D4_L24_EXTERIOR_NATURAL_E8_INSERTION_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-25.md) | full-exterior projective `E8` insertion fails in one representation family | direct determinant normalization | no as a negative witness; used only for exact carrier/formula provenance |
| Block 201 primary and no-import runners | reconstruct the typed carrier/map and evaluate the frozen rational target | exact residual (11)--(12) | yes; direct evidence |

No prior mismatched residual is used to broaden the claim.

### N5 -- rhetoric and resolution audit

- `per_element:` all eight exact D1 one-crossing amplitudes and weights are
  checked, not symmetry representatives.
- `per_site:` all seven Schur restrictions at coarse sites `0,2,4` are
  checked; probability values at sites two and four are not needed to refute
  the universal target and are not claimed negative.
- `per_mode:` all nine radii are checked for carrier typing; the probability
  target is executed only on the preregistered first D1 pair.
- `per_block:` action restriction, CAR intertwiner, gauge quotient,
  determinant engine, and raw normalization are checked in order.
- `lattice_wide:` checked and not executed -- gluing, the 729-word census,
  the five remaining probability cylinders, a causal process, response,
  Record/Born law, gravity, axioms, and TOE closure remain untested.

The phrase is “the frozen typed determinant functional fails raw D1
normalization,” never “the action has no probability law.”  The primary
cached stdout carries these five resolution classes.

### N6 -- partial-closure and primitive scan

No claim equivalent to “a new axiom is required” or “no retained primitive
supplies this” is made.  The minimal axioms already require a local
probability distribution; they do not privilege equation (8).  A convention
rename cannot turn the exact value (12) into one.

Legitimate partial-closure routes remain explicit: derive a boundary/state or
support from the action and later audit that import; derive a covariant
POVM/null completion; construct a different normalized direct functional; or
obtain a positive open-boundary object and then test its event marginals.
Those are new physics constructions, not silent repairs to (8), and no axiom
edit is justified by this block.

### N7 -- strongest steelman

A hostile reviewer should argue that the determinant expression has probably
been normalized against the wrong object: `det(Q_B)` may be the bare Gaussian
vacuum normalization while registered event probabilities require an
action-derived state, open boundary, physical support, or normalized
generating functional.  A covariant POVM/null construction could also change
the event insertion without touching the successful CAR intertwiner.  The
terminal obligation is concrete: derive that extra object before observing
probabilities, prove its unit and gluing laws, and reproduce all lower
marginals without a fitted factor.  This is a strong reason to pivot to the
L12 causal-boundary gate and then revisit probabilities.

The steelman defeats a broad action/probability no-go.  It does not rescue the
exact frozen formula (8), because it changes its normalization object or
event insertion.

### N8 -- cross-cycle echo

- Block 191's missing common temporal carrier was retired by Block 192's exact
  L24 enlargement.  The analogous lesson is to keep a newly derived boundary
  or support route live rather than call the present mismatch axiomatic.
- Block 199's underdetermined three-event law motivated an action-native
  insertion.  Blocks 200 and 201 now prune two different insertion families,
  but their residuals stay distinct and neither closes the causal-boundary
  alternative.
- Historical normalization walls in the repository have sometimes closed
  after an explicit source/state import and a later retirement audit.  That
  mechanism could apply to a newly preregistered functional, but cannot be
  retrofitted into (8) after its target was read.
- Other apparent no-gos have been retired by convention or representation
  changes.  Here a convention alone cannot change the exact rational, while a
  representation or boundary change is already preserved as an untested
  route.

No similar retired wall supplies an unconsidered rescue inside the exact
claim.

**N1--N8 disposition:** `PASS` for the narrow frozen-functional theorem.
`FAIL` for a broad action/probability/history/axiom no-go, which is not
shipped.

## 9. TOE Accounting

| item | before | after | reason |
|---|---:|---:|---|
| obligations retired | `0` | `0` | a candidate realization failed; no retained positive chain closed |
| minimal axioms | unchanged | unchanged | one downstream formula does not test axiom adequacy |
| TOE lane percentages | unchanged | unchanged | no audited retained end-to-end theorem landed |
| route confidence | direct functional ranked first | exact displayed family rejected | cheap kill gate paid off; portfolio pivots |

This is significant scientific progress in route confidence, but it must not
be counted as TOE percentage progress.

## 10. Reproduction Summary

Primary baseline:

```text
[PASS] P0
[PASS] T0
[PASS] T1
[PASS] T2
[PASS] T3
[PASS] S
TOTAL: PASS=6 FAIL=0
```

Primary mutation harness:

```text
baseline_exit=0; rejected=31; gate_matches=31; total=31; harness_failures=0
```

Independent no-import baseline:

```text
TOTAL: PASS=11 FAIL=0
```

Independent mutation harness:

```text
TOTAL: PASS=18 FAIL=0
```

No review-loop was used.  Audit status remains unset and can be assigned only
by the independent audit lane.
