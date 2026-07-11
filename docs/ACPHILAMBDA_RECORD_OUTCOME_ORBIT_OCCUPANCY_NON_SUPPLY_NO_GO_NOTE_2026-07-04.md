# The Axiom Surface Does Not Select a Complex-vs-Realified Determinant Power

**Date:** 2026-07-04; countermodel repair 2026-07-11
**Type:** no_go
**Claim type:** no_go
**Status authority:** independent audit lane. This source proposal does not
set or predict an audit verdict.
**Primary runner:**
[`scripts/acphilambda_record_outcome_orbit_occupancy_non_supply_no_go_2026_07_04.py`](../scripts/acphilambda_record_outcome_orbit_occupancy_non_supply_no_go_2026_07_04.py)
**Runner cache:**
[`logs/runner-cache/acphilambda_record_outcome_orbit_occupancy_non_supply_no_go_2026_07_04.txt`](../logs/runner-cache/acphilambda_record_outcome_orbit_occupancy_non_supply_no_go_2026_07_04.txt)

## Narrow no-go claim

Grant an auxiliary invertible complex block carrier. Even with that grant, the
[four axioms](MINIMAL_AXIOMS_2026-06-29.md) do not entail whether an additive,
K-even determinant readout uses one complex determinant grain or the
realified two-power grain.

Two functionals on the same carrier are

```text
F_C(A) = log |det_C A|,
F_R(A) = log det_R R(A) = 2 F_C(A),
```

where `R(A)` is the realification. Both are similarity invariant, invariant
under complex conjugation, zero on the empty block, and additive under block
direct sum. Under the positive scale deformation `A -> exp(t) A` on an
`n`-dimensional complex block,

```text
d/dt F_C(exp(t)A) at t=0 = n,
d/dt F_R(exp(t)A) at t=0 = 2n.
```

They therefore realize distinct raw determinant-power normalizations on the
same carrier.
The record-level construction below shows that both extend the same
four-axiom model and satisfy the same scalar-readout requirements. The current
axiom surface does not select between them.

This is a current-surface non-entailment result. It does not rule against a
future physical CAR/action theorem that derives a specific Gaussian measure.

## Same-model conservative extensions

Take any model of Lattice, Qubit, Admissibility, and the record-locking clauses.
Keep its lattice, one-site possibility algebra, admissibility rule, records,
and record contents fixed. For a finite pairwise-disjoint record collection
`C`, let `N(C)` be its cardinality, set the exact mathematical witness
`lambda=2`, and grant the same auxiliary carrier assignment in both
extensions:

```text
A(C) = lambda I_(N(C)),
A(empty) = the 0 x 0 block.
```

Now define two scalar readout laws on that unchanged record model:

```text
I_C(C) = F_C(A(C)) = N(C) log(lambda),
I_R(C) = F_R(A(C)) = 2 N(C) log(lambda).
```

Both readouts are determined by record content alone: they use no site label,
state selector, or choice among local possibilities. Both give one answer on
every finite supplied record collection, obey `I(empty)=0`, and are additive
on pairwise-disjoint unions because `N(C union D)=N(C)+N(D)`. The same formula
is used in every state, so neither law privileges a state. All non-readout
parts of the four-axiom model are identical between the two extensions.

This construction is a model interpretation for the non-entailment proof. It
is not a derived or admitted physical record-to-action map, matter action, or
charged-lepton carrier, and it has no downstream authority as one.

## Exact determinant identities

The determinant identity

```text
det_R R(A)=det_C(A) conjugate(det_C(A))=|det_C(A)|^2
```

holds for every complex matrix. For invertible `A`, both logarithmic
functionals are defined. If `A` and `B` are independent blocks, then

```text
F_C(A direct-sum B)=F_C(A)+F_C(B),
F_R(A direct-sum B)=F_R(A)+F_R(B).
```

Complex conjugation leaves both values unchanged. Similarity
`A -> S A S^(-1)` leaves both determinants unchanged. Thus neither basis
invariance, K-evenness, nor additive composition distinguishes the
functionals.

The runner verifies the identities for generic symbolic `2 x 2` matrices and
exact finite examples, checks the two record-model extensions for collection
sizes `0` through `4`, and checks the scaling degrees `n` and `2n` for
`n=1,2,3,4`.

## Scope

The result grants an auxiliary complex carrier assignment and compares two
determinant-style readout laws on it. That assignment is part of the explicit
countermodel construction, not hidden physical input. Since `F_R=2F_C`, this
witness proves underdetermination of the raw determinant-power normalization;
it does not prove that two inequivalent matter actions or Gaussian measures
exist. Calling either functional a physical occupancy law would require the
action/readout bridge that is absent from this construction.

The result does not derive a physical matter action, Berezin measure, K/CPT
structure, determinant line, polarization, orbit quotient, or physical
record-to-action map. It does not set `r`, `delta`, or any mass, and it does
not force `r=1/2`.

The live governance target is recorded in
`docs/audit/data/owner_governed_premise_nodes.json` as AC(i), the matter-action
occupancy grain. That registry identifies the target and is not a proof
premise here. This note does not discharge that physical target. It isolates a
necessary non-selection subclaim beneath it: Record additivity does not choose
the raw complex-versus-realified determinant power.

## No-Go Discipline Gate

### N1 — alternative route enumeration

| Route tested against the countermodel | Marker | Result and authority/check |
|---|---|---|
| Complex carrier structure | ATTEMPTED | Both `F_C` and `F_R` are constructed from the same granted complex block; runner Parts A–B. |
| Complex-basis similarity invariance | ATTEMPTED | Both are unchanged by `S A S^(-1)`; runner Part B. |
| K/conjugation evenness | ATTEMPTED | Both depend on `|det_C A|`; runner Part B. K/CPT is an extra grant because the [axiom memo](MINIMAL_AXIOMS_2026-06-29.md) does not supply it. |
| Record compatibility | ATTEMPTED | The two laws extend the same record model, vanish on the empty collection, and add on disjoint unions through the same carrier assignment; Record clause in the [axiom memo](MINIMAL_AXIOMS_2026-06-29.md), runner Part C. |
| Positive scale response | ATTEMPTED | Both respond covariantly but with degrees `n` and `2n`; runner Part D. |
| Pointwise realized-state evaluation | ATTEMPTED | Evaluating the same carrier at a realized state does not select the functional; [realized-state primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) boundary. |

No prior negative row is used as evidence.

### N2 — wall independence

The scoped claim has one wall: `W_power`, the choice of raw determinant power
on the granted auxiliary carrier. Carrier existence and the carrier assignment
are explicit countermodel grants, so they are not counted as further walls.

### N3 — hidden-wall scan

The proof text was scanned for `we assume`, `by construction`, `as is
standard`, `the framework provides`, `bridge context`, `background`,
`naturally`, `obviously`, `standard QFT`, `registered`, and `canonical`.

| Hit | Classification |
|---|---|
| granted auxiliary carrier assignment and determinant-style readout laws | explicit model interpretation used to strengthen the countermodel; not a physical bridge |
| `registered` in governance/coordinate discussion | non-load-bearing target or route description |
| `canonical` in the steelman | hypothetical determinant-line theorem target, not a proof step |
| scan terms appearing in this checklist sentence | audit metadata, not proof steps |

No hidden action, measure, polarization, or physical carrier selector is used.

### N4 — residual matching

| Prior negative witness | Witness residual | Current residual | Match/disposition |
|---|---|---|---|
| none | n/a | raw complex-vs-realified determinant-power selector on the granted finite carrier | direct countermodels; no witness citation to drop |

The determinant identity is recomputed by the runner rather than inherited
from a prior row.

### N5 — rhetoric and resolution audit

The result is checked per scalar block, per finite matrix block, for finite
disjoint record collections of sizes `0` through `4`, under block composition,
and for complex dimensions `1` through `4`. It supports the finite-carrier
statement above. It makes no claim about a continuum action, an interacting
measure, every possible determinant construction, or a future physical
carrier theorem.

### N6 — partial-closure paths

| Candidate path | Current status | What it would address |
|---|---|---|
| action-native CAR/Berezin theorem | future physical theorem outside the four axioms and this note | derive the complex first-power grain from the physical action |
| real or Majorana action theorem | future physical theorem outside the four axioms and this note | derive a real determinant or Pfaffian grain if that action is selected |
| normalized-readout convention | `F_R/2=F_C` is exact on this carrier | removes the factor-two distinction at the coordinate level; does not derive the matter action that AC(i) asks for |
| registered-mass coordinate package (`docs/ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md`) | contextual algebraic reconstruction after mass data are supplied; not a proof dependency here | removes the determinant explanation from the claim; does not discharge AC(i)'s physical role |
| owner-governed premise registry (`docs/audit/data/owner_governed_premise_nodes.json`) | current governance treatment; not a proof dependency here | supplies the grain without deriving it |

These paths are preserved. The no-go does not propose a new primitive or
classify a future action theorem as impossible.

### N7 — steelman

The strongest objection is that `F_R=2F_C` makes these two readouts a
normalization pair, not evidence for two inequivalent matter theories; one can
adopt `F_R/2` and recover `F_C` without new physics. In addition, the Qubit
axiom uses `M_2(C)`, so a physical complex Berezin action might privilege
`det_C` once a canonical determinant line is derived. This objection correctly
limits the result: the countermodel does not establish an action-level
statistical dichotomy and cannot discharge AC(i). It does not refute the
narrow non-entailment claim, because neither the factor-one normalization nor
the physical Berezin/action bridge appears in the four axioms. The convention
and action routes remain available.

### N8 — cross-cycle echo

| Similar mechanism | Was its wall retired? | Applicability here |
|---|---|---|
| strong-CP determinant-readout route (`docs/STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md`) | contextual comparison; not a witness dependency | phase erasure on a supplied action/readout surface does not choose determinant modulus power; the residuals differ |
| registered mass coordinates (`docs/ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md`) | contextual comparison; not a witness dependency | reconstruction from a supplied realized state changes the explanatory scope and leaves the physical action grain unproved |
| owner-governed AC adoption (`docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md`) | contextual governance history; not a witness dependency | records the premise transparently but is not theorem derivation |

These mechanisms have been checked and do not refute the narrow
current-surface result.

**Gate result: PASS.** N1–N8 support the finite-carrier determinant-power
non-entailment claim with the action-level residual kept outside scope.

## Verification

Run:

```bash
python3 scripts/acphilambda_record_outcome_orbit_occupancy_non_supply_no_go_2026_07_04.py
```

Expected result: `PASS=54`, `FAIL=0`.
