# The Axiom Surface Does Not Select a Complex-vs-Realified Occupancy Grain

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

Grant an invertible complex matter block `A`. Even with that grant, the
[four axioms](MINIMAL_AXIOMS_2026-06-29.md) do not entail whether its additive,
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

They therefore realize distinct occupancy grains while satisfying the same
granted carrier symmetries and additive-readout requirements. The current
axiom surface does not select between them.

This is a current-surface non-entailment result. It does not rule against a
future physical CAR/action theorem that derives a specific Gaussian measure.

## Exact countermodels

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
exact finite examples, then checks the scaling degrees `n` and `2n` for
`n=1,2,3,4`.

## Scope

The result grants a complex carrier and a determinant-style readout. It does
not derive a physical matter action, Berezin measure, K/CPT structure,
determinant line, polarization, orbit quotient, or record-to-action map. It
does not set `r`, `delta`, or any mass, and it does not force `r=1/2`.

The live governance target is recorded in
`docs/audit/data/owner_governed_premise_nodes.json` as AC(i), the matter-action
occupancy grain. That registry identifies the target and is not a proof
premise here.

## No-Go Discipline Gate

### N1 — alternative route enumeration

| Route tested against the countermodel | Marker | Result and authority/check |
|---|---|---|
| Complex carrier structure | ATTEMPTED | Both `F_C` and `F_R` are functorially constructed from the same complex block; runner Parts A–B. |
| Complex-basis similarity invariance | ATTEMPTED | Both are unchanged by `S A S^(-1)`; runner Part B. |
| K/conjugation evenness | ATTEMPTED | Both depend on `|det_C A|`; runner Part B. K/CPT is an extra grant because the [axiom memo](MINIMAL_AXIOMS_2026-06-29.md) does not supply it. |
| Empty-zero plus block additivity | ATTEMPTED | Both vanish on the empty determinant and add on direct sums; Record clause in the [axiom memo](MINIMAL_AXIOMS_2026-06-29.md), runner Part C. |
| Positive scale response | ATTEMPTED | Both respond covariantly but with degrees `n` and `2n`; runner Part D. |
| Pointwise realized-state evaluation | ATTEMPTED | Evaluating the same carrier at a realized state does not select the functional; [realized-state primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) boundary. |

No prior negative row is used as evidence.

### N2 — wall independence

The scoped claim has one wall: `W_grain`, the physical choice between the
complex determinant line and its realification. Carrier existence is granted,
so it is not counted as another wall.

### N3 — hidden-wall scan

The proof text was scanned for `we assume`, `by construction`, `as is
standard`, `the framework provides`, `bridge context`, `background`,
`naturally`, `obviously`, `standard QFT`, `registered`, and `canonical`.

| Hit | Classification |
|---|---|
| granted invertible complex block and determinant-style readout | explicit hypotheses that strengthen the countermodel |
| `registered` in governance/coordinate discussion | non-load-bearing target or route description |
| scan terms appearing in this checklist sentence | audit metadata, not proof steps |

No hidden action, measure, polarization, or physical carrier selector is used.

### N4 — residual matching

| Prior negative witness | Witness residual | Current residual | Match/disposition |
|---|---|---|---|
| none | n/a | AC(i) complex-vs-realified physical occupancy grain | direct countermodels; no witness citation to drop |

The determinant identity is recomputed by the runner rather than inherited
from a prior row.

### N5 — rhetoric and resolution audit

The result is checked per scalar block, per finite matrix block, under block
composition, and for complex dimensions `1` through `4`. It supports the
finite-carrier statement above. It makes no claim about a continuum action,
an interacting measure, every possible determinant construction, or a future
physical carrier theorem.

### N6 — partial-closure paths

| Candidate path | Current status | What it would address |
|---|---|---|
| action-native CAR/Berezin theorem | no retained physical carrier/measure theorem on the current surface | derive the complex first-power grain from the physical action |
| real or Majorana action theorem | no retained physical carrier/measure theorem on the current surface | derive a real determinant or Pfaffian grain if that action is selected |
| registered-mass coordinate package | algebraically reconstructs `r` after mass data are supplied | removes the determinant explanation from the claim; does not discharge AC(i)'s physical role |
| owner-approved narrow premise | presently the live governance treatment | supplies the grain without deriving it |

These paths are preserved. The no-go does not propose a new primitive or
classify a future action theorem as impossible.

### N7 — steelman

The strongest objection is that the Qubit axiom uses `M_2(C)`, so the complex
field should privilege `det_C` and the realification should be regarded as
double bookkeeping. That objection would succeed after a theorem identifies
the physical charged-lepton action with a complex Berezin Gaussian on one
canonical determinant line. The Qubit axiom supplies the local algebra but not
that action, measure, determinant line, or polarization. The realified
functional remains basis-invariant, additive, and K-even on the current
surface, so the objection names a viable theorem target without invalidating
the countermodel.

### N8 — cross-cycle echo

| Similar mechanism | Was its wall retired? | Applicability here |
|---|---|---|
| strong-CP K-real determinant phase chain | phase orientation was treated on a supplied action/readout surface | phase erasure does not choose determinant modulus power; the residuals differ |
| registered mass coordinates | values reconstructed from a supplied realized state | changes the explanatory scope and leaves the physical action grain unproved |
| owner-governed AC adoption | Tier-A bookkeeping was retired by governance | records the premise transparently but is not theorem derivation |

These mechanisms have been checked and do not refute the narrow
current-surface result.

**Gate result: PASS.** N1–N8 support the finite-carrier non-entailment claim.

## Verification

Run:

```bash
python3 scripts/acphilambda_record_outcome_orbit_occupancy_non_supply_no_go_2026_07_04.py
```

Expected result: `PASS=41`, `FAIL=0`.
