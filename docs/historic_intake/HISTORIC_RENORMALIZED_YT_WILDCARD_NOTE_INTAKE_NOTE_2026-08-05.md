# Historic intake: Cl(3) Non-Renormalization Theorem for Yukawa-Gauge Matching

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

Independent Clifford-centrality route: 31/31 PASS establishing G_5 central in Cl(3) with center span{I,G5}, 1-loop Yukawa vertex factorization to relative error 5e-17, and explicitly Z_Y = Z_scalar != Z_g (ratio -2.03). V-scheme boundary condition gives m_t = 174.2 GeV (+0.7%); 1-loop-extrapolated g_3 gives 109.0 GeV (-37%).

Original verdict: Z_Y = Z_g is the WRONG question and does not hold even on the lattice; the gap is CLOSED by reframing to UV boundary-condition protection.
Scope: d=3 staggered lattice, L=8, m=0.1, Cl(3) 8x8 representation; non-renormalization is a d=3 lattice result only, does not extend to continuum d=4.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The honest wildcard route: Z_Y = Z_g is the WRONG QUESTION — 31/31 centrality algebra with the title flag; the lane's true mechanism statement.

## Provenance (pinned)

- Original path: `docs/RENORMALIZED_YT_WILDCARD_NOTE.md`
- Source commit: `ccab562ebde768c686cd884f8c8429266485f466`
- git blob: `a0bee07f7cd47512ec1577257bea2148217ef963`
- sha256: `57f6d479d2472e0343a000246b956af729c0f3aeb167bce09731521e6727c943`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch06/1803_RENORMALIZED_YT_WILDCARD_NOTE.md](../../archive_unlanded/historic_intake_originals/branch06/1803_RENORMALIZED_YT_WILDCARD_NOTE.md)
- Lines: 192; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_renormalized_yt_wildcard​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Title says 'Non-Renormalization Theorem' while the body's headline finding is that the sought identity Z_Y = Z_g is false; the 1-loop-extrapolated boundary condition is off by -37%.
- Supersession (as known at extraction): Wildcard route independent of the Ward-identity approach in idx 1800/1802; feeds the consolidated note idx 1802.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
