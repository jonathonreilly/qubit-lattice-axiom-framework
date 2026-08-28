---
claim_id: admissibility_d4_h1_phase_contact_product_multi_certificate_bounded_theorem_note_2026-08-28
claim_type: bounded_theorem
claim_scope: "For the preregistered Block-228 reduced controller-phase/contact product, all four unequal raw same-source cylinders reduce to bounded common joins, yielding 45 exact rows, but canonical fixture 21 at n=4 with root/seam contacts {1,4} has three normal forms: two stranded adjacent-certificate residues and one restored abort. This is a counterexample to that frozen reduced table only. A separate one-cell coalescence diagnostic closes every one of 2,046 contact subsets through length ten; rank, full state, CP, fairness, Record writing, gravity, and TOE closure remain open."
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_narrowing
target_claim_id: admissibility_d4_h1_full_state_contact_repair_phase_contact_boundary_bounded_theorem_note_2026-08-28
target_blocker_text: "generate every controller-phase/contact/boundary cylinder, then establish termination, confluence, restoration, and CP"
source_of_blocker_text: block227_post_result_panel
reachability_to_target: exact_multicertificate_coalescence_cell
artifact_role: theorem
runner: scripts/admissibility_d4_h1_phase_contact_product_2026_08_28.py
packet_helper_runner: scripts/independent_admissibility_d4_h1_phase_contact_product_2026_08_28.py
next_trace_action: "preregister H-T-L-L to P-H-T-L as a component-coalescence law; test every contact subset, arbitrary-length rank and critical pairs, then labelled full state and CP"
conditional_surface_status: "same-source product completion positive; frozen multi-certificate table nonconfluent at fixture 21; one-cell reduced coalescence route strongly positive but unpromoted"
bare_retained_allowed: false
parent_commit: 118fb0ce3c
preregistration_commit: 7568353e36
no_go_discipline_status: fail_demoted_partial_attempt_with_named_untested_routes
axiom_amendment: none
obligation_retirement: 0
toe_percentage_movement: 0
---

# Phase/Contact Product Multi-Certificate Boundary

**Date:** 2026-08-28

**Type:** bounded theorem / exact reduced-table counterexample.

Primary runner:
[admissibility_d4_h1_phase_contact_product_2026_08_28.py](../scripts/admissibility_d4_h1_phase_contact_product_2026_08_28.py).

Independent reduced runner:
[independent_admissibility_d4_h1_phase_contact_product_2026_08_28.py](../scripts/independent_admissibility_d4_h1_phase_contact_product_2026_08_28.py).

No-go-discipline packet:
[ADMISSIBILITY_D4_H1_PHASE_CONTACT_PRODUCT_MULTI_CERTIFICATE_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md](ADMISSIBILITY_D4_H1_PHASE_CONTACT_PRODUCT_MULTI_CERTIFICATE_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md).

## Result up front

Block 228 clears the phase/contact source ambiguity but not multi-certificate
confluence. Fifty raw rows contain four exact same-source forks. Both sides
of every fork reduce to one identical bounded state, so the precompiler emits
45 disjoint complete cylinders without priority.

The first 20 canonical zero/one/two-contact fixtures have exactly their
declared normal form. Fixture 21 is the first failure:

```text
R-H-T_F-T-T-T_F-A
```

Contact at the seam first can create an `L` certificate that moves into the
root-contact response. Depending on the legal order, two certificates remain
as `R-H-T-L-L-T-A` or `R-P-H-T-L-L-A`; processing the root contact first
reaches `R-P-P-P-P-P-S`. There is no cycle and no live participant. The
failure is therefore a finite nonjoinable certificate-multiplicity cell in the
selected table.

## What advanced

This block replaces Block 227's missing-cell uncertainty with two concrete
facts:

1. read/write-footprint product completion really can resolve all four exact
   controller/contact same-cylinder forks mechanically;
2. the remaining scheduler dependence is localized to adjacent visible abort
   certificates rather than contact detection, boundary typing, or an unknown
   controller phase.

That is route progress, not TOE percentage progress.

## Strong coalescence diagnostic

After the fail-fast result froze, a separate route diagnostic added only

```text
H-T-L-L -> P-H-T-L.
```

It passes every contact subset on `R-H-T^n-A`, `1<=n<=10`: 2,046 fixtures,
249,006 reachable states, 576,990 transitions, maximum 513 states in one
fixture, unique declared normal forms, and no cycles. This result does not
belong to the Block-228 table. It is the preregistered starting candidate for
Block 229 and remains reduced-word evidence until rank, translated overlaps,
labelled darts, CP, and fairness pass.

## Verification

- primary science checks: `10/10`;
- primary mutation checks: `5/5`;
- raw/completed table: `50/45` rows, `4/4` common joins;
- first failing fixture: `21`, `n=4`, contacts `(1,4)`;
- primary table SHA-256:
  `43d54670f255530f774604a5080e77edbd2f4945bb092224f8b163e65d6d3fde`;
- mutation fingerprint SHA-256:
  `81487a93a8b583016c8ead58988c11545e49017440f6b501d0d472434b42edce`;
- primary runner SHA-256:
  `d0a9d9071b38948b835959a90aaa8b8870443e4cbd0c5e909ed8f87edbc767c6`.
- independent checks: `12/12`;
- independent runner SHA-256:
  `6ebd81c89fff84b4abb960b81d9ab30c7afc99ab90d61cdada1fad2259fd118d`.

The arbitrary-length rank, full-state carrier, projectors, CP, fairness,
physical time, permanent Record writing, probability-form selection, gravity,
and law selection are unexecuted. No axiom update, audit verdict,
retained-status promotion, obligation retirement, or TOE percentage movement
is claimed.
