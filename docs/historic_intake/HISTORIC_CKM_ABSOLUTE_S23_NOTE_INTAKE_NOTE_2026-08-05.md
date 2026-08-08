# Historic intake: Absolute S_23 Normalization Without PDG V_cb Calibration

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Determines the absolute S_23 normalization without using PDG V_cb as input, via five attacks (wavefunction renormalization, Symanzik continuum extrapolation S_23(L) = 0.271 L^{-1.62} giving K_continuum = 2.49, V_us as a calibration-free test, physical NNI coefficient from mass splitting, and direct L = 4..16 computation), predicting V_cb to 4.6% of PDG (1.8 sigma).

Original verdict: V_cb is predicted at 4.6% without V_cb input, with the best non-circular determination identified among the five attacks.
Scope: Bounded; includes an explicit circularity analysis of which determinations remain non-circular.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

V_cb predicted at 4.6% without V_cb input via five attacks with the best non-circular determination identified — the April magnitude program's flagship.

## Provenance (pinned)

- Original path: `docs/CKM_ABSOLUTE_S23_NOTE.md`
- Source commit: `ebfd8c112cf96c45904a9d4ed88c7cd4c402e366`
- git blob: `1db4f05cf9394ba62319602b1ad34021211eb61d`
- sha256: `0195de7b2de67988b0fb838a34c28db68bb575b5c55e88db1a0fb9fad59d23ae`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch01/160_CKM_ABSOLUTE_S23_NOTE.md](../../archive_unlanded/historic_intake_originals/branch01/160_CKM_ABSOLUTE_S23_NOTE.md)
- Lines: 135; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_ckm_absolute_s23(.py)`

## Attached evidence (registered with, not as, this claim)

- `docs/CKM_C23_ANALYTIC_NOTE.md` — c_23 mechanism identification with finite-volume flags.
- `docs/CKM_K_RATIO_ANALYTIC_NOTE.md` — Sector-dependent matching factor analytic form.
- `docs/CKM_NNI_COEFFICIENTS_NOTE.md` — NNI coefficients from the lattice; parameter-count reduction.
- `docs/CKM_RATIO_ROUTE_NOTE.md` — EW asymmetry derived parameter-free; scale gap named.
- `docs/CKM_S23_C13_CLOSURE_NOTE.md` — Full 3x3 with J still ~100x off; c_13 tension flagged.
- `docs/CKM_S23_MATCHING_NOTE.md` — Status DERIVED over one fitted parameter — overclaim documented.
- `docs/CKM_THERMALIZED_OVERLAP_NOTE.md` — FALSIFIES the EWSB-axis-enhancement mechanism earlier ratio-route notes used — flag carried.
- `docs/CKM_VCB_CLOSURE_NOTE.md` — V_cb assembly leaning on a ~70x scheme-dependent matching factor — flagged.
- `docs/CKM_V_CB_EXACT_NOTE.md` — Exact 2x2 block solve replacing the linear estimate.
- `docs/CKM_V_UB_EXACT_NOTE.md` — V_ub structural suppression; factor-2 miss honest.

## Flags carried

none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded
intake_directive: owner_2026-08-05
```

Independent audit still required.
