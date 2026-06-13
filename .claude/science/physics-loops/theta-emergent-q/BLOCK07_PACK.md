# Block07 pack — theta emergent-Q bridge, weighting half (2026-06-13)

Branch: physics-loop/theta-emergent-q-weighting-block07-20260611 (stacked
on block06). Adversarially verified before commit (workflow wq5viaoq8,
6 verifiers + synthesis; verdict fix_then_proceed; all 5 required fixes
applied).

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: theta_gauge_substrate_no_winding_carrier_emergent_q_bridge_bounded_theorem_note_2026-06-11
target_blocker_text: "whether the scaling limit forces an emergent integer sector functional with nonvacuous weighting"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "existence half (does a nonvacuous Q emerge); the 0-vs-pi choice; dressed-fermion Fujikawa Jacobian under RG"
```

Partial: closes the WEIGHTING (CP-odd) half; existence half + 0-vs-pi +
spontaneous CPV remain open.

## Claim status certificate

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: "reality of the measure is RG-stable => no CP-odd theta weighting (theta in {0,pi}), conditional on K-reality + site-diagonal A + real per-plaquette (Wilson) action + conjugation-equivariant blocking"
claim_type_reason: "exact identities + genuine finite-model marginalization with reality-drop and symmetry-drop discriminators; reality reframing (not CP) reconciled with the framework CPT convention"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Adversarial verification (workflow wq5viaoq8) and fixes applied

Verdict: fix_then_proceed (no load-bearing claim wrong; conclusions
survive every refutation). 5 required fixes, ALL applied:
1. Garbled `det(KMK)=conj det M` one-liner -> corrected two-step
   (entrywise conjugation for CP-invariance; eps-chirality for reality);
   note + runner check-3 string fixed.
2. Site-diagonality was an undeclared load-bearing premise -> added as a
   consumed premise + NEW violation-class check 5 (non-site-diagonal
   K-real coupling gives complex det).
3. RG checks 9-11 were tautologies -> replaced with a GENUINE exact
   marginalization on a finite Z_3 model + two discriminators
   (reality-drop -> complex; symmetry-drop -> asymmetric marginal).
4. Reality pins theta to {0,pi}, not 0 -> retitled/rescoped; cite and
   REFINE the retained 06-07 no-go.
5. Real-action provenance mislabel -> cite WILSON_ACTION_SURFACE_SELECTOR
   _REAL_POSITIVE + flag it as an admitted (unaudited) convention.
Nits folded: "CP" relabeled to REALITY/conjugation with explicit CPT-note
reconciliation (M->M* is T, not CP); Fujikawa-Jacobian residual; 3D-vs-4D
dimension-independence residual; softened "unphysical"/"inverts
completely"/"proven impossible"; spontaneous-CPV residual.

## V1-V5

- V1: closes the weighting half of block06's named emergent-Q bridge.
- V2: new content: reality-is-RG-invariant via genuine marginalization;
  the {0,pi} refinement of 06-07; the conjugation/C reframing.
- V3: no -- consumes the staggered determinant reality (block05) + Wilson
  real-positive action; generic math alone does not give it.
- V4: yes -- removes the CP-violating possibility from the emergent-Q
  question; theta sandwiched within {0,pi}.
- V5: no -- block06 was the substrate carrier (pi_0=0); this is the
  scaling-limit weighting. Different parents/mechanisms. 3rd strong_cp
  PR this campaign.

## Cluster-cap (3rd strong_cp-family PR; volume cap removed by #3557)

Evaluator brief applied locally: new load-bearing premise (reality
RG-invariance + genuine marginalization), distinct artifact (weighting
half vs block06's carrier), independently reviewable (stacked on block06,
recomputes block05's det reality), high value (completes the gauge-side
sandwich). Verdict: OPEN.

Disposition: pass (local), post adversarial verification. Independent
audit required.
