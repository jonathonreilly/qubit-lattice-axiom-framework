# Historic intake: DM Lane: Nucleation Finding - Detonation Regime

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_bounded
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The bounce computation gives T_c = 222.6 GeV, T_n = 200.5 GeV, T_n/T_c = 0.90, at which the driving pressure is too large for Boltzmann friction to balance: the force-balance equation has no solution below the Jouguet velocity, pushing the wall into the detonation regime v_w > c_s where diffusion-transport baryogenesis fails.

Original verdict: Does not invalidate the DM relic ratio R, but the transport sector has a genuine dynamical issue the earlier v_w range [0.006, 0.048] did not capture; the lane stays BOUNDED on transport.
Scope: At taste scalar mass m_s = 120 GeV with the 1-loop Daisy high-T potential and nucleation criterion S_3/T = 140 - all four flagged as possible sources of the problem.


## Why pulled (supervisor decision, on the record)

The nucleation NEGATIVE: no force-balance solution — the wall runs away (detonation problem), conflicting with its same-day sibling; the pair goes to audit together.

## Provenance (pinned)

- Original path: `docs/DM_NUCLEATION_FINDING_NOTE.md`
- Source commit: `81a4efe78660d1bb27dc930c5e7cd8d8f2cc9149`
- git blob: `32567a847a81ec90ed88b4e85e297e794cdb301d`
- sha256: `9830bfa861dad46cb784020eea5ba96483adc39ed4764a8f58333d488c1271fc`
- Lines: 71; runners named: scripts/frontier_dm_nucleation.py

## Attached evidence (registered with, not as, this claim)

- `docs/DM_NUCLEATION_TEMPERATURE_NOTE.md` — The conflicting positive measurement (T_n = 180.6, v/T = 0.80) with MC-calibrated R_NP flagged.

## Flags carried

Negative finding: the framework does not uniquely predict m_s, and the detonation outcome depends on that undetermined mass; also directly inconsistent with the sibling nucleation-temperature note's T_n/T_c.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
