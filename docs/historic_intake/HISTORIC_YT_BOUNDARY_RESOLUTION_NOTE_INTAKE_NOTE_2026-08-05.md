# Historic intake: y_t Boundary Resolution: V-Scheme to MSbar at M_Planck

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_bounded_result
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Attributes the 6.5% top-mass overshoot (184 vs 173.0 GeV) to scheme inconsistency rather than matching: the 1-loop V-to-MSbar conversion with r_1 = a_1/4 + (5/12) beta_0 = 3.83 reduces alpha_V = 0.093 to alpha_MSbar(M_Pl) = 0.084 (2-loop: 0.082), and using MSbar g3 for gauge evolution gives m_t = 171.8 GeV (-0.7%) and 171.0 GeV (-1.1%), closing 82-89% of the 11 GeV overshoot. The mechanism is the -8 g_3^2 term in the y_t beta function, which inflates y_t by ~6% when g3 ~ 1.07 but not when g3 ~ 0.49.

Original verdict: The y_t gate is declared CLOSED at matching precision, with the residual -1.1% (2 GeV) inside perturbative matching uncertainty and requiring no new physics.
Scope: Matching-precision level with 2-loop SM RGE and threshold corrections included; alpha_plaq = 0.092 remains an input.


## Why pulled (supervisor decision, on the record)

The 'Gate CLOSED at matching precision' claim WITH its own cross-validation flag — the audit pair against 2312.

## Provenance (pinned)

- Original path: `docs/YT_BOUNDARY_RESOLUTION_NOTE.md`
- Source commit: `e4da5c4f283aee94865ed984677b359ae3906ed3`
- git blob: `56c1887693965df5dd9aef9d9dad1db770ffe9a2`
- sha256: `496a12a983c49e6bdf0de8d99ec946c69c049981e4d92933c6896d0afc09bc08`
- Lines: 93; runners named: scripts/frontier_yt_boundary_resolution.py, scripts/frontier_yt_formal_theorem.py, scripts/frontier_yt_matching.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Self-declared 'Gate CLOSED' while its own cross-validation notes the alpha_s needed for exact m_t = 173 is 0.086 against the derived 0.084 (3.3% low); the closure rests on a scheme conversion whose exactness is not independently checked.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
