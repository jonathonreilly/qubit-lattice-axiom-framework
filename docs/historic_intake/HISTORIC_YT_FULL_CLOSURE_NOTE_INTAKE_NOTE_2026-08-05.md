# Historic intake: y_t Full Closure: Tracing All Inputs to the Framework

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

Resolves the three review sub-gaps: SM running is a consequence of derived particle content (b_3 = 11 N_c/3 - 2 n_f/3 = 7, b_2 = 19/6, b_1 = -41/10 all from derived representations), alpha_s(M_Pl) = 0.093 follows algebraically from g_bare = 1 through alpha_lat = 0.0796 and tadpole resummation with the single computed coefficient c_V^(1) = 2.136, and lattice-to-continuum matching is bounded at ~3-10% with 2-loop matching at ~0.1%.

Original verdict: BOUNDED with all inputs traced and a single ~10% computable matching uncertainty: m_t = 184 GeV, 6.5% above observed, inside a [172, 194] GeV band that encompasses 173.0.
Scope: Conditional on A5, the bare UV theorem and Cl(3) preservation; no new assumptions.


## Why pulled (supervisor decision, on the record)

The boundary-decomposition claim (all inputs traced, ~10% matching uncertainty) WITH the wide-band flag [172,194] — the era's y_t boundary statement.

## Provenance (pinned)

- Original path: `docs/YT_FULL_CLOSURE_NOTE.md`
- Source commit: `7deacd8da1657be8a694c53dd310b38863010e78`
- git blob: `44fde23e582601db3b6ba907bb62bff8171de939`
- sha256: `0145b15989c727de7df7f1667de2aad311953d62867db322744071247fcde6a0`
- Lines: 154; runners named: scripts/frontier_yt_cl3_preservation.py, scripts/frontier_yt_full_closure.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

The claimed uncertainty band [172, 194] GeV is wide enough to contain the observed value by construction, and its central value disagrees with two sibling notes from the same lane and week.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
