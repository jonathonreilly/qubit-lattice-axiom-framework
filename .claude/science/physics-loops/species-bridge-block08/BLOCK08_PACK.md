# Block08 pack — species bridge AC_phi_lambda(iii) minimum form (2026-06-13)

Branch: physics-loop/species-bridge-decomposition-block08-20260613 (base
origin/main; landed notes only). Adversarially verified before commit
(workflow wod0q9n6t, 5 verifiers + synthesis; verdict fix_then_proceed;
all required fixes applied).

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: staggered_dirac_realization_gate_note_2026-05-03
target_blocker_text: "AC_phi_lambda(iii): the abstract-sector -> physical-species bridge"
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "across-fermion-type alignment (CKM/PMNS); the interpretive identification itself is retained (contentless), not derived away"
```

## Certificate

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: "AC_phi_lambda(iii) = derived M_3(C) support + two vacuities (naming, carrier-triplet) + one contentless interpretive identification"
claim_type_reason: "derived support and both vacuities are computed witnesses; contentlessness argued from checks 4+7 with check 8 made probative by orbit-averaging contrast"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Adversarial verification (workflow wod0q9n6t) and fixes applied

Verdict: fix_then_proceed. The decomposition (Steps A-D) is sound; the
KEY question -- is carrier-triplet vacuity honestly scoped (unitarily-
equivalent-as-C_3-carriers, NOT physical interchangeability) -- resolved
YES (the chirality-flip objection does not break it). Fixes applied:
- checks 8-9 were non-probative (trace readout conjugation-invariant
  under ANY unitary; check 9 only counted dict keys) -> check 8 rebuilt
  as a genuine orbit-averaging contrast (generic separates spread~6;
  C_3-equivariant forced equal spread 0); check 9 rebuilt as per-input-
  type computed witnesses (rigid char triples; carrier equivalence;
  equipartition).
- softened the cross-registry "weakest admission" superlative to a
  within-AC_phi_lambda comparison.
- added scorecard-reading guidance (contentlessness argued from 4+7,
  not an independent 10-fact proof).
- nits: U_R is a ker-D symmetry not a D-symmetry; C_3-equivalence is
  automatic (eps supplies the canonical intertwiner); eps not diagonal
  in the Hamming basis (carrier choice orthogonal to chirality);
  su(3)->color analogy grade-restricted to the C_3 grade.

## V1-V5

- V1: sharpens AC_phi_lambda(iii) to minimum form (the registry's
  named species-bridge residual).
- V2: new content: the carrier-triplet vacuity (eps C_3-intertwiner)
  and the orbit-averaging contentlessness test; the decomposition.
- V3: no -- consumes the staggered hw-structure + labeling no-go.
- V4: yes -- reduces (iii) to a contentless interpretive identification.
- V5: no -- distinct from blocks 01-04 (magnitude/reading selection);
  this is the species bridge. First species-bridge PR this campaign.

Disposition: pass (local), post adversarial verification. Independent
audit required.
