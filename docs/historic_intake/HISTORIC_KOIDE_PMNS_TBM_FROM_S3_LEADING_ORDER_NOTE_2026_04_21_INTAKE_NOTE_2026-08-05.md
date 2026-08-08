# Historic intake: Koide Loop Iteration 3 — I5 Attack: PMNS TBM from S_3 Axis Permutations

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

If the Majorana mass matrix respects the full S_3 cubic symmetry while charged leptons break it diagonally, then M_nu = alpha I + beta(J - I) is diagonalized exactly by V_TBM as the simultaneous real eigenbasis of the C_3 symmetrizer and P_23, giving sin^2 theta_12 = 1/3, sin^2 theta_13 = 0 and sin^2 theta_23 = 1/2 — leaving the reactor angle 8.57 deg as the dominant gap.

Original verdict: INTERMEDIATE — V_TBM is forced as the leading-order PMNS matrix but I5 is not closed, since theta_13 != 0 requires a Z_2-breaking mechanism.
Scope: Leading order only, under the named ansatz that Majorana respects S_3 while Dirac does not, which is itself undreived; 35/35 symbolic checks.
Escape conditions (negative claims): Consistency with the existing retained PMNS no-gos is checked and attributed to bank difference: those no-gos concern the Dirac single-Higgs probe bank while this uses a Majorana S_3-invariant mass bank, and at rho = I/3 the retained J_chi = 0 result is recovered.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

S_3-symmetric Majorana + diagonal charged-lepton breaking forces V_TBM exactly — INTERMEDIATE with the ansatz admitted; the I5 lane's leading-order base.

## Provenance (pinned)

- Original path: `docs/KOIDE_PMNS_TBM_FROM_S3_LEADING_ORDER_NOTE_2026-04-21.md`
- Source commit: `6cd86a9477bc76aea156478c9e7bdc31eafb9b0e`
- git blob: `727da6c536882ed116be09c18076ff89de763bf1`
- sha256: `9de7caf4af49bf397effe2b63c37a930b7a38b6e2526ed171ff52eb07e3c5401`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch03/889_KOIDE_PMNS_TBM_FROM_S3_LEADING_ORDER_NOTE_2026-04-21.md](../../archive_unlanded/historic_intake_originals/branch03/889_KOIDE_PMNS_TBM_FROM_S3_LEADING_ORDER_NOTE_2026-04-21.md)
- Lines: 172; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_koide_pmns_tbm_from_s3(.py)`; historic runner (unpinned, not in this packet): `scripts/frontier_koide_c3_spatial_rotation(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

The load-bearing symmetry ansatz is admitted to be an ansatz, and the note escapes prior no-gos by changing the observable bank.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
