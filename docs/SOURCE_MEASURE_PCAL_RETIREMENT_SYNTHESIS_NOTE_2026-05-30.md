---
claim_id: source_measure_pcal_retirement_synthesis_note_2026-05-30
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Source/Measure P-Cal Retirement Synthesis

**Claim type:** bounded_theorem / exact-support synthesis.
**Role:** integrates the first three source/measure physics-loop routes against
the P-cal/Y_T source-scale blocker.
**Status:** exact-support; not unbounded retained Y_T closure by this note
alone.
**Primary runner:** `scripts/frontier_source_measure_pcal_retirement_synthesis.py`
**Generated output:** `outputs/source_measure_pcal_retirement_synthesis_2026-05-30.json`

## Result

The source/measure campaign reduces the old Tier-A P-cal blocker to one
semantic bridge:

```text
physical source is a smooth sharp-record probability intervention.
```

If that bridge is accepted as native to the qubit/LSP source-measure surface,
then P-cal closes on the finite sharp-record source sector and the Y_T scalar
source-scale blocker closes:

```text
lambda = 1,
y_33 = 1/sqrt(6).
```

If that bridge is not accepted, the campaign still leaves three exact support
theorems and the remaining blocker is narrower than before.

## What is now closed

1. **RN-cocycle route.**
   [`SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md`](SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md)
   proves that a normalized sharp-record RN source family with primitive score
   forces

   ```text
   W(h) = log E_0 exp(hO).
   ```

   The logarithm is the normalizer of the source measure update, not a separate
   scalar-additivity assumption.

2. **Cumulant/Mobius route.**
   [`SOURCE_MEASURE_PCAL_CUMULANT_MOBIUS_THEOREM_NOTE_2026-05-30.md`](SOURCE_MEASURE_PCAL_CUMULANT_MOBIUS_THEOREM_NOTE_2026-05-30.md)
   proves that `log Z` is the finite partition-lattice generator of connected
   source responses.  Raw `Z^p` or `M^p` does not generate unit connected
   responses unless `p=1`.

3. **Sharp-record tangent-space route.**
   [`SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md`](SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md)
   proves that finite sharp-record probability space has a canonical RN score
   tangent and Fisher pairing.  The signed record has unit Fisher norm; scaling
   by `lambda` changes the norm to `lambda^2`.

Together these close the algebraic part of the P-cal blocker.  The `F_p` wall
is no longer a free functional ambiguity once the object is a source-measure
tangent, RN normalizer, or connected-response generator.

## What remains

The remaining question is not algebraic:

```text
Is a physical source, in this framework, a smooth intervention on the
probability law of sharp projective records?
```

If yes, then the RN/tangent/cumulant package is the retained route to P-cal.
If no, the package is exact support and the framework still needs either:

- an explicit accepted source-action/source-measure premise, or
- a strict same-source top/W pole-response certificate that cancels the source
  scale directly.

## Impact on Y_T

The current Y_T Tier-A closure note already proves:

```text
accepted source-measure/P-cal surface -> lambda = 1 -> y_33 = 1/sqrt(6).
```

This campaign supplies the missing source-measure support underneath that
accepted surface.  Conditional on audit accepting the single bridge above, the
Y_T scalar source-scale bound would be retired.  Without that acceptance, the
Y_T result remains bounded by the same explicit source-measure premise, but the
premise is now sharply localized.

This route does not use the old Ward identity, `H_unit`, or `y_t_bare`.

## Status boundary

```yaml
actual_current_surface_status: exact-support
trace_class: direct_blocker_closure_candidate
target_blocker_text: "P-cal / physical top source unit"
source_of_blocker_text: "observable-principle P-cal residual and Y_T primitive-unit source/action no-go"
reachability_to_target: partially_closes
artifact_role: synthesis
closed_if_single_bridge_accepted:
  - P-cal on the finite sharp-record source sector
  - lambda = 1 for the normalized Y_T top source
  - y_33 = 1/sqrt(6)
remaining_if_not_accepted:
  - physical source is a smooth sharp-record probability intervention
  - strict same-source top/W pole-response certificate
proposal_allowed: false
proposal_allowed_reason: >
  The three algebraic routes converge, but independent audit must decide
  whether the remaining source-measure bridge is native or still admitted.
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Non-claims

This note does not claim:

- unbounded retained Y_T closure on the current surface;
- that independent audit has accepted the remaining source-measure bridge;
- closure for generic non-record/non-smooth/non-RN interventions;
- a production top-correlator measurement;
- a strict same-source top/W pole-response certificate;
- derivation of `v`, Planck scale, `g_2`, or running bridges;
- use of `H_unit`, `yt_ward_identity`, `y_t_bare`, PDG values, `alpha_LM`,
  plaquette/u0, or a fitted selector.

## Verification

Run:

```text
python3 scripts/frontier_source_measure_pcal_rn_cocycle.py
python3 scripts/frontier_source_measure_pcal_cumulant_mobius.py
python3 scripts/frontier_source_measure_sharp_record_tangent_space.py
python3 scripts/frontier_source_measure_pcal_retirement_synthesis.py
```

Expected result for every runner:

```text
SUMMARY: PASS=... FAIL=0
```
