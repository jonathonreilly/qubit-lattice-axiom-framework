# Historic intake: Neutrinoless Double-Beta Effective Majorana Mass m_bb Prediction

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

From the retained masses m_1 = 4.37, m_2 = 9.71, m_3 = 50.4 meV and PDG 2024 PMNS angles (|U_e1|^2 = 0.6752, |U_e2|^2 = 0.3001, |U_e3|^2 = 0.02241), the effective Majorana mass window is m_bb in [0.00, 6.96] meV — below the KamLAND-Zen bound (28-122 meV), below Legend-1000's ~17 meV reach, and at the edge of nEXO's ~7-15 meV. Structurally, |U_e1|^2 m_1 = 2.95 meV and |U_e2|^2 m_2 = 2.92 meV are nearly equal, placing m_1 in the NO cancellation funnel.

Original verdict: A falsifiable window: non-detection at Legend-1000 is consistent, and a detection near 7 meV would indicate constructively aligned Majorana phases.
Scope: Operates on the bounded Majorana-seesaw surface with the admitted Higgs/CW EW lane; the specific value within the window depends on undetermined Majorana phases alpha_i.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Falsifiable m_bb window (~7 meV) with the observable-corrected input flagged.

## Provenance (pinned)

- Original path: `docs/NEUTRINOLESS_DOUBLE_BETA_MBB_PREDICTION_NOTE_2026-04-22.md`
- Source commit: `0009ff9fd09141790e40f399a29ced192123deea`
- git blob: `e78ba1e0e0cc4ea766d6ec35139659e8f347a02a`
- sha256: `f82154ab01e44956f4a2641e727ae635b59fcbc05c40ec04d35bc1cca6bb438d`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch04/1182_NEUTRINOLESS_DOUBLE_BETA_MBB_PREDICTION_NOTE_2026-04-22.md](../../archive_unlanded/historic_intake_originals/branch04/1182_NEUTRINOLESS_DOUBLE_BETA_MBB_PREDICTION_NOTE_2026-04-22.md)
- Lines: 101; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_neutrinoless_double_beta_mbb_prediction​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: m_2 is observable-corrected via the observed Delta m^2_21 rather than derived, and the solar-gap lane remains open.
- Supersession (as known at extraction): Depends on the observable-corrected m_2 from NEUTRINO_MASS_SUM_PREDICTION_2026-04-22; note the retained 'M_R currently zero' surface would make m_bb vanish trivially, so this note deliberately works on a different surface.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_measurement_derived_prediction_window
intake_directive: owner_2026-08-05
```

Independent audit still required.
