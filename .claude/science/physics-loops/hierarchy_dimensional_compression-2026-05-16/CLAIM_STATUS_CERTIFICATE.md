# Claim-Status Certificate

**Loop:** hierarchy_dimensional_compression-2026-05-16
**Date:** 2026-05-16
**Block:** single source-and-runner rescope block

## Target

`hierarchy_dimensional_compression_note`
(audit_status before this block: `audited_numerical_match`, class G,
281 descendants).

## Audit-flagged load-bearing step (verbatim from auditor)

> Using the same residual ratio R, the dimension-4 effective-potential-
> like inverse fourth root R^(-1/4) ~= 0.96468 is in the right few-
> percent range, while the inverse sixteenth root R^(-1/16) ~= 0.99105
> is too small.

The auditor's verdict observed that this conclusion was load-bearing
**against the imported observed prefactor C_obs**, making the within-
scope claim a numerical-closeness match to observation rather than a
first-principles closure.

## What this block did

1. Rewrote `docs/HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md` so the
   within-scope claim is purely intra-framework dimensional arithmetic
   on the staggered Dirac condensate-density ratio R, inheriting the
   (1/4) D=4 reading from the 2026-05-10 sister bounded theorem note
   `HIERARCHY_HEAT_KERNEL_D4_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-05-10.md`.
2. Demoted the `v_obs / v_pred = C_obs` comparison to a non-load-
   bearing `external context` print block that is explicitly excluded
   from runner PASS gates.
3. Rebuilt the runner `scripts/frontier_hierarchy_dimensional_compression.py`
   so its PASS gates are: (a) `R^(-1/4)` reproduces via two independent
   algebraic routes; (b) `R^(-1/4)` and `R^(-1/16)` differ by > 2%;
   (c) the structural identity `1/D = 4/2^D` holds at D=4; (d) the
   same identity fails at all D in {1,2,3,5,6,8}; (e) audit-transparent
   self-attestation that no observed target is referenced before the
   PASS block.
4. Refreshed cached runner output in `logs/runner-cache/`.

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: |
  The within-scope claim after this block is intra-framework
  dimensional arithmetic on the staggered Dirac condensate-density
  ratio, plus the inherited (1/4) D=4 admission from the 2026-05-10
  heat-kernel sister bounded theorem note. The runner's PASS gates
  no longer depend on imported observed values. The block does NOT
  derive the determinant-to-VEV theorem or close the effective-
  potential-density bridge; those remain open per the parent note's
  "What is still open" section.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Promotion Value Gate (workflow step 7)

This block is a rescope-for-audit move, not a bounded → retained
promotion. The V1-V5 gate applies to retained-positive promotion
campaigns; this block does not propose status promotion. For the
honest record:

| # | Answer |
|---|---|
| V1 | The auditor's verdict flagged the C_obs comparison as the load-bearing G-class step. This block retires that load-bearing surface by demoting C_obs to non-PASS external context and replacing the PASS gates with intra-framework arithmetic and the structural 1/D = 4/2^D identity (verified to fail at D≠4). |
| V2 | New runner gates (1)-(4) named above; new source-note structure separating within-scope arithmetic from external context; explicit audit-transparency self-attestation gate (5). |
| V3 | The within-scope arithmetic is elementary; the structural value comes from re-anchoring the load-bearing surface, not from new math. |
| V4 | The non-trivial content is the rescope itself: moving the observation-comparison out of the PASS gates so the runner can be re-audited as `audited_clean` on intra-framework content, with the (1/4) admission cross-referenced to the 2026-05-10 sister derivation. |
| V5 | Not a one-step variant of an already-landed cycle. The 2026-05-10 audited-scope narrowing companion documented the scope split in prose; this block reflects that split inside the parent note itself and inside the runner's PASS structure, which the 2026-05-10 companion explicitly did not do. |

## No-Go Discipline Gate

Not applicable — this block makes no `no_go`, no
`stretch_attempt_negative`, no `bounded_with_named_walls`, and no
derived-no-go-boundary claim. The block only rescopes a bounded
diagnostic so its PASS surface is intra-framework. The N1-N8 gate is
for negative-claim shipments and is not engaged here.

## Review-loop disposition

`pending` (no separate review-loop invocation inside the 60-minute
budget; the rescoped note + runner is itself the deliverable for
audit-lane re-review).

## Independent audit handoff

The independent audit lane is required to ratify any effective status
change. This certificate proposes that the next audit pass on
`hierarchy_dimensional_compression_note`:

- check that the runner's PASS gates do not reference any observed
  target value (gates 1-5 above);
- check that the source note's load-bearing surface is the intra-
  framework arithmetic + inherited (1/4) admission, not the C_obs
  comparison;
- check that the `external context` block is honestly labeled and
  excluded from PASS gates;
- check that the inherited (1/4) admission is correctly cross-referenced
  to the 2026-05-10 heat-kernel sister bounded theorem note (which the
  audit lane should treat as the upstream derivation surface for the
  (1/4) exponent).

If those checks pass, the parent row can re-audit as `audited_clean` at
bounded-theorem grade, with the open work (effective-potential-density
bridge, per-determinant readout primitive derivation, staggered-Dirac
realization gate, continuum-limit corrections) explicitly recorded in
the note's "What is still open" section.
