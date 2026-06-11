# Trace Gate — koide-staggered-first-order (block01 + block02)

## Block01

```yaml
trace_class: direct_blocker_closure
target_claim_id: koide_r_half_index_readout_non_susy_staggered_dirac_gate_meta_note_2026-06-05
target_blocker_text: "does the actual matter action deliver a first-order det D (Pfaffian/index, count-once) or the second-order modulus? ... its first-order construction is not yet done"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "channel-generality test (done in block02)"
```

## Block02

```yaml
trace_class: direct_blocker_closure
target_claim_id: koide_staggered_first_order_generation_determinant_bounded_theorem_note_2026-06-11
target_blocker_text: "the probe coupling FORM A = a*I + b*U_R + c*U_R^T (the C_3[111] rotation channel) is a declared probe, not a derived Yukawa ... other C_3-equivariant couplings are not enumerated here"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "the remaining selection is the named owner-decision premise (reading section); no further derivation cycle is queued on this atom at the bilinear level"
```

Block02 closes block01's declared channel-generality residual at the
bilinear level: the complete equivariant channel space is classified and
the holomorphy/tying localization is proven over all of it. Out-of-scope
residuals (interacting actions, non-equivariant couplings, reading-section
selection) are declared, not silently closed.
