# Historic intake: CKM Clean Derivation Note

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

Assembles what is genuinely derived in the April CKM chain — NNI texture from a sequential EWSB cascade, Froggatt-Nielsen epsilon = 1/3 from the Z_3 group order, the Cabibbo angle via Gatto-Sartori-Tonin, delta_CP scale = 2 pi/3 from Z_3 eigenvalue spacing, the hierarchy ordering, and EWSB breaking C3 in inter-valley amplitudes — against a sharp boundary of six items that are not (V_cb and V_ub values, NNI O(1) coefficients, precise delta_CP, continuum/thermodynamic limits, dynamical fermions).

Original verdict: A clean derived/not-derived boundary for the CKM lane, with paper-safe wording that avoids claiming delta_CP = 68 degrees when the framework gives 120.
Scope: Lane status BOUNDED; all lattice computations at finite L (<= 8 for overlaps, 12 for production) with ~98% volume spread and no continuum extrapolation.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The CKM chain's derived/not-derived boundary WITH the live discrepancy on the record (framework delta_CP = 120 vs PDG 65.5) — the lane's honest claim surface.

## Provenance (pinned)

- Original path: `docs/CKM_CLEAN_DERIVATION_NOTE.md`
- Source commit: `c8a115dc33c7565caf57e90cb3a30b9cef69e7d5`
- git blob: `2123664a4c4451f475283df7a251a1ffde4f931e`
- sha256: `598893504f0063e7cca4a03f3d2a09a5b88b2cc46368d3d8d5da725da30d61f9`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch01/178_CKM_CLEAN_DERIVATION_NOTE.md](../../archive_unlanded/historic_intake_originals/branch01/178_CKM_CLEAN_DERIVATION_NOTE.md)
- Lines: 287; runners named: historic runner (unpinned, not in this packet): `frontier_ckm_closure​.py`; historic runner (unpinned, not in this packet): `frontier_ckm_from_mass_hierarchy​.py`; historic runner (unpinned, not in this packet): `frontier_ckm_with_ewsb​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_ckm_c23_analytic​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_ckm_closure​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_ckm_from_mass_hierarchy​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_ckm_nni_coefficients​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_ckm_with_ewsb​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/CKM_CLOSURE_NOTE.md` — Chain assembly + Higgs-charge blocker dissolution.
- `docs/CKM_DERIVED_NOTE.md` — Wolfenstein-from-geometry obstruction inventory.
- `docs/CKM_DIRECT_HAMILTONIAN_NOTE.md` — Direct-Hamiltonian mechanism demonstration, no quantitative match.
- `docs/CKM_FIRST_PRINCIPLES_NOTE.md` — Zero-input claim with |V_ub| 20x off under 'order-of-magnitude' status — overclaim documented.
- `docs/CKM_FROM_TEXTURE_NOTE.md` — Z_3 Fourier texture: qualitatively right, quantitatively wrong, gap named.
- `docs/CKM_FULL_CLOSURE_NOTE.md` — 'Full Closure' title over J off by ~360x — overclaim documented in place.
- `docs/CKM_LATTICE_DIRECT_NOTE.md` — Clean route-pruning negative: no mixing without gauge fluctuations; scoped.
- `docs/CKM_MASS_MATRIX_FIX_NOTE.md` — Rank-1 extraction bug record + GST restoration.
- `docs/CKM_TEXTURE_DERIVATION_NOTE.md` — Democratic-texture analytic derivation; GST sharp.
- `docs/CKM_WITH_EWSB_NOTE.md` — EWSB C3->Z2 breaking; exact structural component.
- `docs/CKM_WOLFENSTEIN_CASCADE_THEOREM.md` — Wolfenstein-as-cascade with by-construction flag.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Records a live discrepancy: the framework's delta_CP is 120 degrees while the observed value is ~68.
- Supersession (as known at extraction): none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded
intake_directive: owner_2026-08-05
```

Independent audit still required.
