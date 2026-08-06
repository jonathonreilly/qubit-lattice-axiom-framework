# Historic intake: GW150914 Echo Prediction: Derived from Lattice Axioms

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_derived
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

Original verdict: Testable with existing LIGO O1/O2/O3 data: confirmed if echoes are detected at 68 +/- 3 ms, refuted if at t >> 68 ms (e.g. Abedi's ~100 ms) or absent.
Scope: All inputs determined (M and chi from LIGO, a = l_Planck from the framework axiom, m = m_nucleon from the SM); free parameters ZERO; the prediction is logarithmically insensitive to surface location — a factor-of-10 change in epsilon shifts t_echo by only ~5%.


## Why pulled (supervisor decision, on the record)

GW150914 echo prediction 68+/-3 ms — falsifiable against LIGO O1-O3, disagreeing with Abedi et al.; named notable deletion; wrapper must cross-flag its dependency on the frozen-stars runner attacked by 3080/3091.

## Provenance (pinned)

- Original path: `docs/GW_ECHO_DERIVED_NOTE.md`
- Source commit: `a52dc368136d4835addfcd60f04ae0ebf1324f4a`
- git blob: `8ac1cda4576fa52e5d76eb170e66cefcaaa58ebc`
- sha256: `02d2887eac11a4de20de60e34516fa5b9653d8d6b051d29326b8e6dd0d8027ea`
- Lines: 199; runners named: scripts/frontier_gw_echo_derived.py, scripts/frontier_frozen_stars_rigorous.py, scripts/gw150914_echo_search.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Self-listed estimates: the Kerr correction uses the standard ECO tortoise factor (Cardoso et al. 2016) rather than a full Kerr tortoise integral on the lattice; the surface reflection coefficient is assumed ~1 (perfect reflection) with partial absorption reducing amplitude; and the frozen-star EOS at nuclear density is not modelled, the Planck-scale hard floor being used directly.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
