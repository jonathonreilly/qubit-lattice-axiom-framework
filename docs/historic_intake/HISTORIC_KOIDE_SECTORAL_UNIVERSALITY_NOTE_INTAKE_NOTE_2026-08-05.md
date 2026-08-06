# Historic intake: Koide Sectoral Universality Note

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_measurement
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Q_l = 0.666661 (PDG pole, -0.001% from 2/3), but Q_d = 0.730582 framework-native / 0.731428 PDG self-scale / 0.744497 at common scale mu=m_b (+9.6% to +11.7%), and Q_u = 0.848838 self-scale / 0.888373 at M_Z (+27.3% to +33.3%). Bringing Q_u to 2/3 would need sqrt(m_t) rescaled by A=0.339401, i.e. an effective m_t ~ 19.89 GeV, which no retained theorem produces.

Original verdict: KOIDE_UNIVERSALITY = CHARGED_LEPTON_ONLY (PASS=20 FAIL=0) — the Koide invariant is a sector-specific statement of the charged-lepton sector, not a universal law.
Scope: Cross-sector comparator using PDG masses for comparison only; falsifies the strong universality reading of Prediction 3 on the current observation surface and does not promote Koide in any sector.
Escape conditions (negative claims): A cross-sector universality theorem would have to supply an explicit sector-dependent spectral correction, which the retained stack does not have; no scheme (self-scale, common-scale running to m_b or M_Z) closes the gap.

## Why pulled (supervisor decision, on the record)

Self-falsification of Koide universality: Q_u ~ 0.85, Q_d ~ 0.73 — the invariant is charged-lepton-ONLY (20/20); a stated prediction falsified on the record.

## Provenance (pinned)

- Original path: `docs/KOIDE_SECTORAL_UNIVERSALITY_NOTE.md`
- Source commit: `4c3906a20b8570e70a14c5b8d96fe6110647d003`
- git blob: `b8f252677c015bb58965c2f6d3f4f2530a0eb632`
- sha256: `0d906ebf527210f1d4126d333f04b2447f5a2fb8842f4b30530cb2ddbb1a2591`
- Lines: 211; runners named: scripts/frontier_koide_sectoral_universality.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

This is a self-falsification of a stated prediction of the charged-lepton Koide-cone derivation; the note carries it as an honest negative rather than repairing it.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
