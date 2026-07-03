# AC_phi_lambda Occurrence-Clock Composition Delta-Blindness
**Date:** 2026-07-02
**Claim type:** bounded composition theorem / route adjudication
**Scope:** exact composition of the landed occurrence kernel with the
finer-record doublet clock on the supplied circulant 3-space; no value,
Born-interface derivation, objectivity, empirical measurement semantics, or
occurrence-production derivation.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, or claim
`AC_phi_lambda` retirement.
**Primary runner:** [`scripts/acphilambda_occurrence_clock_composition_delta_blindness_2026_07_02.py`](../scripts/acphilambda_occurrence_clock_composition_delta_blindness_2026_07_02.py)

## Claim
Let the circulant generation surface have character basis `chi_k`, projectors `P_k = |chi_k><chi_k|`, and
```text
H = a I + b C + conj(b) C^T,  U = exp(-i H),  D_chi(rho) = sum_k P_k rho P_k.
```
T14-1: because `U` is diagonal in the `chi` basis, each occupancy
`o_k = <chi_k|rho|chi_k>` is invariant under every native step for all
`(a, |b|, delta)`.
T14-2: if the occurrence event law reads only occupancies, for example
`p(v)=o_v`, then every registered stream over any event times has a law
independent of `delta`, the doublet phase `phi`, and the inter-event step
counts.
In that precise sense, occupancy-reading event streams are completely `delta`-blind: the doublet clock phase never enters the registered stream.
T14-3: `delta`-registration through events requires a coherence-reading conditional law, which the landed occurrence bridge leaves supplied.
Therefore the panel's route (c) adjudicates to the registered-pattern normal form: the value wall relocates into the supplied conditional law.
This is not a terminal no-go.

## Frame And Retained Inputs
The occurrence bridge is the landed source
[`RECORD_OCCURRENCE_THINNED_IID_FREQUENCY_BRIDGE_2026-07-01.md`](RECORD_OCCURRENCE_THINNED_IID_FREQUENCY_BRIDGE_2026-07-01.md).
Ledger row `record_occurrence_thinned_iid_frequency_bridge_2026-07-01` has
`audit_status` `unaudited` and `effective_status` `unaudited`; audit statuses pending.
Its pinned boundary says the theorem does not derive `a`, `p`, the physical
instrument/trigger, IID reset/preparation, a clock/rate, objectivity, or
empirical measurement semantics.
That bridge supplies the finite sparse-record kernel once those surfaces are supplied.

The finer-record clock note is the landed source
[`ACPHILAMBDA_POINTER_LABELED_REFINEMENT_FINER_RECORD_CLOCK_2026-07-02.md`](ACPHILAMBDA_POINTER_LABELED_REFINEMENT_FINER_RECORD_CLOCK_2026-07-02.md).
Ledger row `acphilambda_pointer_labeled_refinement_finer_record_clock_2026-07-02` has `audit_status` `unaudited` and `effective_status` `unaudited`; audit statuses pending.
Its note-file pins are map pins: `D_chi` erases the `chi_1`-`chi_2`
coherence in one application, preserves occupancies, and advances the doublet
phase by `2 sqrt(3) |b| sin delta` per native step before an event.

The retained circulant anchor is
[`BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md`](BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md).
Ledger row `brannen_circulant_is_forced_c3_covariant_record_preserving_generation_form_bounded_theorem_note_2026-06-15` has `effective_status` `retained_bounded`.
Ledger scope authority: Hermitian generators commuting with the cyclic shift
`C` have Brannen circulant form and commute with `S=C+C^2`; the row does not derive `C`, `S`, `r`, `delta`, or the coupling values.
The source pins used here are `circulant form` and `(a, |b|, delta)`.

Context only, not dependency links:
`PR #4840` `ACPHILAMBDA_K_EVEN_REGISTRATION_CORRECTION_REGISTERED_PATTERN_2026-07-02`
for registered-pattern normal form, with panel route (c) gated on the occurrence lane;
`PR #4845` `ACPHILAMBDA_CROSS_ARC_UNIT_CLASSIFICATION_WIRING_2026-07-02`
for the single shared frontier.

## Occupancy Invariance
Work in the character basis. The projectors `P_k` commute with `H`, hence with `U`. For any density matrix `rho`,
```text
o_k(U rho U^dagger) = Tr(P_k U rho U^dagger) = Tr(U^dagger P_k U rho) = Tr(P_k rho) = o_k(rho).
```
Equivalently, `U = diag(exp(-i lambda_0), exp(-i lambda_1), exp(-i lambda_2))`,
so the diagonal entry of `U rho U^dagger` is
`exp(-i lambda_k) rho_kk exp(i lambda_k) = rho_kk`.
No condition on `(a, |b|, delta)` is used.
Thus the doublet clock can rotate coherences while never moving the
character-basis occupancies.

## Delta-Blindness Of Occupancy-Reading Streams
Let event times be arbitrary native steps `t_1 < t_2 < ...`,
with `n_j = t_j - t_{j-1}`.
At an event, take the conditional law to be the `D_chi`-registered occupancy
law `p(v)=o_v`.
Before the first event,
```text
rho^-_1 = U^n1 rho U^dagger^n1.
```
Its diagonal is the initial diagonal. The nonselective event map gives
```text
rho^+_1 = D_chi(rho^-_1) = diag(o_0, o_1, o_2).
```
Before the second event,
```text
rho^-_2 = U^n2 rho^+_1 U^dagger^n2 = diag(o_0, o_1, o_2).
```
Therefore
```text
P(V_1=i, V_2=j) = o_i o_j.
```
The same induction gives the finite stream law
```text
P(V_1=v_1, ..., V_m=v_m) = product_l o_{v_l}.
```
More generally, any event rule that is a fixed function of the occupancy vector
sees the same occupancy vector at every event.
The Bernoulli thinning realization selects which attempts fire, but after
conditioning on those event times it contributes no `delta` channel to the
registered values.
The law has no dependence on `lambda_k`, on `delta`, on the accumulated phase
`phi`, or on the inter-event counts.

## What Delta-Registration Requires
The doublet phase is not absent from the state. With `(d1, d2) = (chi_2, chi_1)`,
```text
rho_d1d2(n) = exp(i (lambda_d2 - lambda_d1) n) rho_d1d2(0),
lambda_d2 - lambda_d1 = 2 sqrt(3) |b| sin delta.
```
It lives in the coherence. A coherence-reading law can see it. For example, with
```text
|+> = (|chi_1> + |chi_2>) / sqrt(2),  p_+ = <+|rho(n)|+>,
```
one obtains a term depending explicitly on `(lambda_d2 - lambda_d1)n`.
That discriminator separates the theorem from a false claim that all event
readouts are blind.
The blindness result is only for occupancy-reading laws.

Because the occurrence bridge leaves `p` supplied, a coherence-reading
conditional law is an admitted supplied surface, not a derivation.
The ratio idea also fails on dial count:
```text
clock rate / event rate = 2 sqrt(3) |b| sin(delta) / a_act.
```
It contains both the coupling magnitude `|b|` and the activation probability `a_act`, and both are outside the retained circulant-plus-occurrence surface.

## What This Moves
Route (c), the occurrence-statistics route from the panel context, is
adjudicated for occupancy-reading streams.
It lands in the registered-pattern normal form rather than in a value derivation.
The value wall sits in the supplied conditional law `p`, the Born-interface
admission class.
Together with the registered-pattern panel and the cross-arc wiring context,
the panel route table is complete at the level of route placement.
The single frontier remains: the shared supplied-interface target.

## What Does Not Move
- No value of `delta` is derived.
- The conditional law `p` is not derived, per the bridge's own boundary.
- The Born-interface admission class is untouched.
- Occurrence statistics themselves remain the sparse thinned-IID algebra.
- Coherence-reading laws are not forbidden.
- Objectivity, empirical measurement semantics, reset, trigger, and rate normalization are not derived.
- `W_cycle_holonomy_value`, `W_defect_identity_unit`, and `W_defect_readout_selection` remain the only wall names used here.

## Audit Consequence If Retained
If retained by an independent lane, this note supplies a bounded composition
fact: composing the landed occurrence kernel with the finer-record doublet
clock gives exact `delta`-blindness for occupancy-reading registered streams.
Downstream rows may cite that fact to reject occupancy-only occurrence
statistics as a value channel.
They still need a supplied or derived coherence-reading `p` to register
doublet phase content through events.

## Non-Claims
- No derivation of Born weights.
- No claim that coherence-reading laws are forbidden; they are the named supplied surface.
- No claim that event times carry the doublet phase into occupancy readouts.
- No derivation of `a_act`, `|b|`, `p`, reset, objectivity, or empirical semantics.
- No claim that the single shared frontier is solved.
- No terminal negative claim beyond the bounded occupancy-reading closure.

## No-Go Gate N1-N8
### N1
Alternative route enumeration:
occupancy-reading occurrence route - CLOSED HERE exactly;
coherence-reading route - OPEN as a SUPPLIED surface, the Born-interface
admission class, not a derivation;
ratio route - CLOSED by two free dials;
single-frontier target - OPEN, sister-shared.

### N2
Wall-independence audit: the occupancy result uses `[H,P_k]=0` and not a value assumption. The value wall is not converted into a theorem.

### N3
Hidden-wall scan: the event law `p`, trigger, reset, rate, objectivity, and empirical semantics are all supplied or open exactly where the occurrence bridge says they are.

### N4
Residual matching: the doublet phase remains present in coherence; the registered stream loses it when the readout ignores coherence. This matches the finer-record clock note's erasure pin.

### N5
Rhetoric audit: the result is a bounded composition theorem. It does not assert a value, a measurement primitive, or an audit outcome.

### N6
Partial-closure path scan: a coherence-reading supplied law can still register phase content. A same-surface derivation of such a law would be a separate Born-interface admission result.

### N7
Steelman: "the blindness is obvious since `[H, P_k] = 0`."
Reply: obvious once stated, but it finally adjudicates the gated panel route
and pins where the wall sits in occurrence coordinates.
Concession: no value or Born-interface law is derived.

### N8
Cross-cycle echo: the same pattern recurs when a registrable normal form exists but a value law is not supplied. Slot typing moves; value derivation does not.

## Verification
Run command:
```bash
python3 scripts/acphilambda_occurrence_clock_composition_delta_blindness_2026_07_02.py
```
Measured close:
```text
TOTAL: PASS=97 FAIL=0
```
