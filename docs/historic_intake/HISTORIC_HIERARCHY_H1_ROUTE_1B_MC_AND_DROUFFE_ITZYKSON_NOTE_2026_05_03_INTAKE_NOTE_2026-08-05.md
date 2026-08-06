# Historic intake: Hierarchy H1 Route 1B — Wilson MC and Drouffe-Itzykson Cross-Check

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_numerical_diagnostic_cross_check
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Three independent methods agree on the SU(3) single-plaquette block at beta = 6 to ten digits — Drouffe-Itzykson Bessel determinant 0.4225317397, Haar quadrature 0.4225317396, framework Perron solve 0.4225317396 (pairwise diffs 1.476e-10) — while L=2 pure-Python Wilson MC gives <P>(6) = 0.624, 5% above the canonical bulk 0.5934, making the Pade extraction of higher onset coefficients unstable.

Original verdict: One substantive result (3-way 10-digit agreement validating the framework Perron solve by an entirely different analytic route) and one quantified obstruction: closing Route 1A via MC needs a compiled-language implementation, ~1-2 months plus MC runtime; loop stopped.
Scope: Loop iteration 2; single-plaquette block cross-check is exact, but the MC arm is finite-volume L=2 only (L=3 estimated ~55 hours in pure Python).


## Why pulled (supervisor decision, on the record)

Three independent methods (Drouffe-Itzykson, Haar, framework Perron) agree to ten digits — external validation of framework machinery.

## Provenance (pinned)

- Original path: `docs/HIERARCHY_H1_ROUTE_1B_MC_AND_DROUFFE_ITZYKSON_NOTE_2026-05-03.md`
- Source commit: `40bf858be7a8249c8cc4e85e8e293180bf772e60`
- git blob: `fbc3876131bcc6c2ef37f45b95a117415491308e`
- sha256: `acc88f4f0b09ba751f667ec7c0f6b41dde4d559ae4916d742ec693907165fa9b`
- Lines: 184; runners named: scripts/frontier_hierarchy_wilson_mc_kernel.py, scripts/frontier_hierarchy_drouffe_itzykson_check.py, scripts/frontier_hierarchy_pade_resum.py

## Attached evidence (registered with, not as, this claim)

- `docs/HIERARCHY_H1_ROUTE_1B_HAAR_KERNEL_NOTE_2026-05-03.md` — Route-1A grading (months-grade).

## Flags carried

Pade analyzer explicitly unstable on the finite-volume data; L=2 MC coefficients dominated by finite-volume contamination.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
