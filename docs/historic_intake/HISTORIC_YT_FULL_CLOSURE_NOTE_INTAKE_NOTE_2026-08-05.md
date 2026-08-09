# Historic intake: y_t Full Closure: Tracing All Inputs to the Framework

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

Resolves the three review sub-gaps: SM running is a consequence of derived particle content (b_3 = 11 N_c/3 - 2 n_f/3 = 7, b_2 = 19/6, b_1 = -41/10 all from derived representations), alpha_s(M_Pl) = 0.093 follows algebraically from g_bare = 1 through alpha_lat = 0.0796 and tadpole resummation with the single computed coefficient c_V^(1) = 2.136, and lattice-to-continuum matching is bounded at ~3-10% with 2-loop matching at ~0.1%.

Original verdict: BOUNDED with all inputs traced and a single ~10% computable matching uncertainty: m_t = 184 GeV, 6.5% above observed, inside a [172, 194] GeV band that encompasses 173.0.
Scope: Conditional on A5, the bare UV theorem and Cl(3) preservation; no new assumptions.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The boundary-decomposition claim (all inputs traced, ~10% matching uncertainty) WITH the wide-band flag [172,194] — the era's y_t boundary statement.

## Provenance (pinned)

- Original path: `docs/YT_FULL_CLOSURE_NOTE.md`
- Source commit: `7deacd8da1657be8a694c53dd310b38863010e78`
- git blob: `44fde23e582601db3b6ba907bb62bff8171de939`
- sha256: `0145b15989c727de7df7f1667de2aad311953d62867db322744071247fcde6a0`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch07/2310_YT_FULL_CLOSURE_NOTE.md](../../archive_unlanded/historic_intake_originals/branch07/2310_YT_FULL_CLOSURE_NOTE.md)
- Lines: 154; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_yt_cl3_preservation​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_yt_full_closure​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: The claimed uncertainty band [172, 194] GeV is wide enough to contain the observed value by construction, and its central value disagrees with two sibling notes from the same lane and week.
- Supersession (as known at extraction): Its 184 GeV central value is superseded within days by the re-schemed 171.0 GeV (idx 2142, 2306) and the 181.6 GeV step-scaling value (idx 2168) — three different numbers for the same lane in one week.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded_result
intake_directive: owner_2026-08-05
```

Independent audit still required.
