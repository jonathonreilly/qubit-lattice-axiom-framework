# Historic intake: GW150914 Echo Prediction: Derived from Lattice Axioms

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: pre_seeding_mainline_deleted
Era: april_pre_reset — dated 2026-04-12; framework axiom a = l_Planck

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

A five-step chain from lattice discreteness (lambda_min = 2 l_Planck, so f(R_S + a) = a/(R_S+a) > 0 and no horizon forms; Fermi floor R_min = N^(1/3) a) places the GW150914 remnant's surface at epsilon = R_min/R_S = 3.70e-21 with ln(1/epsilon) = 47.05, giving a zero-parameter echo prediction t_echo = 67.66 ms and f_echo = 14.8 Hz for M = 62 M_sun, chi = 0.67 (58.09 ms / 17.2 Hz non-spinning; N_baryons = 7.37e58, R_min = 6.78e-16 m, R_S = 1.83e5 m, f_min = 8.8e-41, Kerr spin enhancement 1.1735).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

GW150914 echo prediction 68+/-3 ms — falsifiable against LIGO O1-O3, disagreeing with Abedi et al.; named notable deletion; wrapper must cross-flag its dependency on the frozen-stars runner attacked by 3080/3091.

## Provenance (pinned)

- Original path: `docs/GW_ECHO_DERIVED_NOTE.md`
- Source commit: `a52dc368136d4835addfcd60f04ae0ebf1324f4a`
- git blob: `8ac1cda4576fa52e5d76eb170e66cefcaaa58ebc`
- sha256: `02d2887eac11a4de20de60e34516fa5b9653d8d6b051d29326b8e6dd0d8027ea`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/recovery/3611_GW_ECHO_DERIVED_NOTE.md](../../archive_unlanded/historic_intake_originals/recovery/3611_GW_ECHO_DERIVED_NOTE.md)
- Lines: 199; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_gw_echo_derived​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_frozen_stars_rigorous​.py`; historic runner (unpinned, not in this packet): `scripts/gw150914_echo_search​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): Testable with existing LIGO O1/O2/O3 data: confirmed if echoes are detected at 68 +/- 3 ms, refuted if at t >> 68 ms (e.g. Abedi's ~100 ms) or absent.
- Extraction scope (triage compression; may reflect later context): All inputs determined (M and chi from LIGO, a = l_Planck from the framework axiom, m = m_nucleon from the SM); free parameters ZERO; the prediction is logarithmically insensitive to surface location — a factor-of-10 change in epsilon shifts t_echo by only ~5%.
- Extraction red flags: Self-listed estimates: the Kerr correction uses the standard ECO tortoise factor (Cardoso et al. 2016) rather than a full Kerr tortoise integral on the lattice; the surface reflection coefficient is assumed ~1 (perfect reflection) with partial absorption reducing amplitude; and the frozen-star EOS at nuclear density is not modelled, the Planck-scale hard floor being used directly.
- Supersession (as known at extraction): Disagrees with Abedi et al. (2017): 67.66 ms vs ~100 ms and epsilon 3.70e-21 vs 5.15e-31 — Abedi's 100 ms would require the surface ~6 billion Planck lengths above R_S.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_derived
intake_directive: owner_2026-08-05
```

Independent audit still required.
