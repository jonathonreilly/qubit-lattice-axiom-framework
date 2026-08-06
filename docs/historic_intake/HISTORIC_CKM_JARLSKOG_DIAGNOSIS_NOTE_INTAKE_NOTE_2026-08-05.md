# Historic intake: CKM Jarlskog Invariant Diagnosis

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_analysis
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Diagnoses why J collapses in the NNI framework: if the Z_3 phase survived diagonalization intact J would be 3.05e-5 (0.99x PDG) since sin(2 pi/3) = 0.866 is within 1% of the needed 0.875 — the loss is entirely phase washout from M M^dag phase dilution, perturbative eigenvector rotation, and near-degenerate EW ratios.

Original verdict: Not a code bug but a genuine physics constraint: the simplest NNI plus single-Z_3-phase framework cannot reproduce V_ub and J simultaneously.
Scope: Diagnostic of the single-phase NNI texture with phase confined to M_13, 1.4% up/down EW weight mismatch and extreme mass hierarchy m_u/m_t ~ 1e-5.
Escape conditions (negative claims): Three named resolutions: phases in both sectors, phase in M_23 rather than only M_13, or independent c_13^u/c_13^d.

## Why pulled (supervisor decision, on the record)

The Jarlskog structural diagnosis: phase-loss in diagonalization is a genuine physics constraint of single-phase NNI (J would be 0.99x PDG if the phase survived) — three named resolutions; the family's terminal understanding.

## Provenance (pinned)

- Original path: `docs/CKM_JARLSKOG_DIAGNOSIS_NOTE.md`
- Source commit: `5e3931471d9aa25b2884a0ca2ec81f99ec7313fd`
- git blob: `1dc5db99c616fc491a4a1fc316b57b21817c2970`
- sha256: `3eba7c59f4f653689cd8582a9caca37fb296b74fea33a59f0bc3a5a0da092f77`
- Lines: 129; runners named: frontier_ckm_full_closure.py, scripts/frontier_ckm_jarlskog_diagnosis.py

## Attached evidence (registered with, not as, this claim)

- `docs/CKM_JARLSKOG_CLOSURE_NOTE.md` — Sector-phase attempt: J within 3.7% at the cost of V_ub +17.8% and a fitted mismatch — flag on the record.
- `docs/CKM_JARLSKOG_FIX_NOTE.md` — Full Z_3^3 attempt; delta_CP worsens to 69% off — flagged.
- `docs/CKM_J_DERIVED_NOTE.md` — Four attacks: J or angles, not both; internal gap-figure inconsistency recorded.

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
