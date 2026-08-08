# Historic intake: Strong-Field Regime: Horizon Structure and Framework Breakdown

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: no_go
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Diagnoses a fundamental non-unitarity: the transfer-matrix spectral radius exceeds 1 at ALL field strengths (1.27 at f=0.5, maximal 1.98 at f=1, symmetric about f=1), transmission after 20 layers rises to 6.9e+5 at f=1, and wavepackets inside r_h are amplified 30-130x rather than trapped, so the f=1 surface AMPLIFIES instead of absorbing.

Original verdict: Honest negative: the framework does not contain strong-field GR or any black-hole analog, and its gravitational predictions are reliable only for f < 0.1.
Scope: Discrete path-sum propagator with cos^2 kernel and 1/L^p attenuation; horizon radius fit r_h = 0.048*ms + 0.76 (R^2 = 0.986) versus expected 0.080*ms.
Escape conditions (negative claims): Two named escapes: a normalized kernel that enforces unitarity, or a field equation that self-consistently limits f < 1; a true horizon would require an amplitude-attenuation mechanism absent from S = L(1-f).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The non-unitarity diagnosis: transfer spectral radius > 1 at ALL field strengths — the framework does not contain strong-field GR; reclassifies the Hawking-analog result; two escapes named.

## Provenance (pinned)

- Original path: `docs/STRONG_FIELD_REGIME_NOTE.md`
- Source commit: `2dfb2c7e50276de5d4a3d64233392d5503a03c25`
- git blob: `ddf50a3e8cf828efc8c14bd0accf022d30d226fb`
- sha256: `5f64e26c507b513ee403c79376bc59dffda76a92bd0de2a2132c0fe9541cea8b`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch06/2001_STRONG_FIELD_REGIME_NOTE.md](../../archive_unlanded/historic_intake_originals/branch06/2001_STRONG_FIELD_REGIME_NOTE.md)
- Lines: 162; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_strong_field_regime(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Reclassifies a previously reported 'Hawking analog' amplification as a propagator normalization artifact, and restricts the validity of the framework's headline gravity results to f < 0.1.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_no_go
intake_directive: owner_2026-08-05
```

Independent audit still required.
