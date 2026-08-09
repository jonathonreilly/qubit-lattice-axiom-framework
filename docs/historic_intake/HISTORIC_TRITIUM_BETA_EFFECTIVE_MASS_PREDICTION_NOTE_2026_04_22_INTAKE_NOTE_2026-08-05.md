# Historic intake: Tritium Beta-Decay Effective Mass m_beta Prediction

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

On the retained neutrino chain (m_1 = 4.37, m_2 = 9.71, m_3 = 50.4 meV) plus PDG 2024 NO PMNS, the incoherent sum m_beta^2 = sum |U_ei|^2 m_i^2 = 12.89 + 28.30 + 56.96 = 98.14 meV^2 gives m_beta = 9.86 meV — 1.23% of the KATRIN 2022 bound, 4.9% of KATRIN's final target, 24.7% of Project 8's ~40 meV reach, and only 1.0 meV above the NO minimum of 8.90 meV, with m_3 supplying 58% of m_beta^2 despite |U_e3|^2 = 0.0224.

Original verdict: A single-valued Majorana-phase-independent prediction m_beta = 9.86 meV, falsifiable by any beta-decay detection above ~15 meV.
Scope: Retained light-neutrino surface plus PDG PMNS NO; does not close the solar-gap lane, derive PMNS angles, or address the M_R = 0 Dirac surface.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Falsifiable single-valued m_beta = 9.86 meV prediction (Majorana-phase-independent) — with the observable-corrected input flagged.

## Provenance (pinned)

- Original path: `docs/TRITIUM_BETA_EFFECTIVE_MASS_PREDICTION_NOTE_2026-04-22.md`
- Source commit: `0009ff9fd09141790e40f399a29ced192123deea`
- git blob: `10abc2194fe951ca9197457e1d788224e1359958`
- sha256: `c3922b4c0809c2466de6107cee4e0bb6248650dfc2a33447b418c71c6e06799c`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch07/2079_TRITIUM_BETA_EFFECTIVE_MASS_PREDICTION_NOTE_2026-04-22.md](../../archive_unlanded/historic_intake_originals/branch07/2079_TRITIUM_BETA_EFFECTIVE_MASS_PREDICTION_NOTE_2026-04-22.md)
- Lines: 124; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_tritium_beta_mass_prediction​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: m_2 is observable-corrected via the measured Delta m^2_21 rather than derived, and the PMNS angles are PDG imports, so the 'derived prediction' status is partly data-fed.
- Supersession (as known at extraction): Third leg of the three-observable neutrino fingerprint (with the Sigma m_nu and m_bb companion notes of the same date); depends on the retained chain rather than superseding it.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_prediction
intake_directive: owner_2026-08-05
```

Independent audit still required.
