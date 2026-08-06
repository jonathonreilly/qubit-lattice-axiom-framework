# Historic intake: CKM Final Assessment: Routes Tried, Routes Remaining, Honest Verdict

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_bounded
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Full inventory of CKM routes tried: solidly derived are the NNI texture, eps = 1/3, |V_us| = sqrt(m_d/m_s) = 0.2234 (0.4% from PDG via Gatto-Sartori-Tonin), the hierarchy ordering, delta ~ 2 pi/3 and J ~ 1e-5 in order of magnitude; not derived are V_cb (factor 2-4), V_ub (factor 3-4), O(1) NNI coefficients (worst 38%) and the precise CP phase (120 vs 68.5 degrees, 75% off).

Original verdict: No new route bypasses the compute bottleneck; the gap is diagnosed as computational rather than conceptual, and the lane stays BOUNDED.
Scope: Includes a table of mass-ratio attempts for V_cb (sqrt(m_s/m_b) 3.2x, sqrt(m_c/m_t) 2.0x, m_s/m_b 0.44x, m_c/m_t 0.18x) and three untried routes.


## Why pulled (supervisor decision, on the record)

Terminal route inventory: the CKM gap diagnosed as computational (S_23 bottleneck), not conceptual — with the derived list exact.

## Provenance (pinned)

- Original path: `docs/CKM_FINAL_ASSESSMENT.md`
- Source commit: `d53b9b8cc7f6b4a6aeb0d87eee48969b0bc42922`
- git blob: `05dc3fc73684f63141a9b0d0231ec69ce6494c00`
- sha256: `8ad980ae8894dc902dc1be8d1639c1e44e6389cd9f3271b827e3d5f26c888fa9`
- Lines: 285; runners named: frontier_ckm_c23_analytic.py, frontier_ckm_derived.py, frontier_ckm_dynamical_selection.py, frontier_ckm_from_mass_hierarchy.py, frontier_ckm_from_texture.py, frontier_ckm_higgs_from_anomaly.py, frontier_ckm_higgs_from_gauge.py, frontier_ckm_higgs_from_vev.py

## Attached evidence (registered with, not as, this claim)

- `docs/CKM_INVARIANTS_NOTE.md` — Route-4 status: sole remaining gap is the S_23 absolute scale.
- `docs/CKM_S23_SHARPENING_NOTE.md` — Codex-deliverable assessment; priorities named.

## Flags carried

none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
