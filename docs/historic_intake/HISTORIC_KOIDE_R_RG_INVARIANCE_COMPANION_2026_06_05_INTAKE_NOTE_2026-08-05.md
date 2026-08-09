# Historic intake: RG-invariance of the Koide modulus r, and two sharpenings

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: branch_only_never_mainlined
Era: unknown

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

r = |b|^2/a^2 is degree-0 homogeneous, so every flavor-uniform term in the SM 1-loop Yukawa RGE (gauge terms including -8 g3^2, and the trace T) cancels in the ratio; numerically over ~33 e-folds M_Z to GUT the absolute top Yukawa moves 0.99 -> 0.46 (~53%) while r_up moves 0.773 -> 0.786 (1.6%) and r_down 0.597 -> 0.578 (3.3%). That residual is an order of magnitude too small to carry r from a fixed point {0, 1/2, 1} to a generic value, so the 'flow picks a generic r' escape is closed.

Original verdict: A ratio quasi-fixed-point does not exist; plus two sharpenings — QCD RG-invariance of r derived from color-perpendicular-to-generation, and a category error foreclosing the whole 'geometric/overlap ratio fixes r' class (the three generations are orthonormal Brillouin-corner momentum eigenstates, C3 hopping is a unitary permutation not a small overlap integral). Runner PASS=27 FAIL=0.
Scope: Closes the one un-killed candidate from the prior 4-for-4 dynamics no-go; sector targets r_lep=1/2, r_up~0.77, r_down~0.597, r_nu~0.238 are labelled observational comparison, not derivation inputs. No audit status set.
Escape conditions (negative claims): Any mechanism setting a generic r must be intrinsically non-uniform/relational, acting on the singlet-vs-doublet isotype balance itself rather than any overall scale or flavor-blind coupling; three live directions named (degree-0-ratio spectral/arithmetic invariant, precision-stable cross-sector source law, or r as a recorded outcome with a Born measure over the dial).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Exact ratio RG-invariance (flavor-uniform terms cancel) + a prior published estimate self-corrected by three orders — clean theorem with an honesty record.

## Provenance (pinned)

- Original path: `docs/KOIDE_R_RG_INVARIANCE_COMPANION_2026-06-05.md`
- Source commit: `6ee7ab1ea022f0395c2e7dbcbdbf3711f8db190e`
- git blob: `f1d840aca89c44ec87b99d7a561de7fc64b3f689`
- sha256: `50ba0bc0de32ef4b499f6badf1bd11e02414d4dff36c47191120621166fc0088`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch04/1076_KOIDE_R_RG_INVARIANCE_COMPANION_2026-06-05.md](../../archive_unlanded/historic_intake_originals/branch04/1076_KOIDE_R_RG_INVARIANCE_COMPANION_2026-06-05.md)
- Lines: 109; runners named: historic runner (unpinned, not in this packet): `scripts/koide_r_rg_invariance_2026_06_05​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Self-corrects an earlier published estimate off by three orders of magnitude; r_up flagged as scheme-soft at ~2% (m_t pole vs MSbar over [150,173] GeV gives r_up in [0.760, 0.773]).
- Supersession (as known at extraction): Corrects a prior optimistic estimate (~0.001% for r_down) that omitted the -(3/2)Y_u^dag Y_u cross term; the honest figure is 3.3%.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
