# Historic intake: Scheme-Independence of the Cl(3) Gauge-Yukawa Ratio

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

April-era claimed THEOREM: on the staggered Cl(3) lattice with a = l_Planck, y_t/g_s = 1/sqrt(6) holds to all orders in perturbation theory in any scheme, with corollary m_t/m_W = (g_s/g_2) sqrt(2)/sqrt(6). Proof is a three-step argument (lattice is the theory, Ward identity fixes the ratio non-perturbatively, Gamma_5-central vertex factorization protects it), checked numerically by Z_y/Z_g = 1 to machine precision on small random SU(3) configurations.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The April 'all orders in any scheme' y_t/g_s = 1/sqrt(6) THEOREM claim — pulled WITH the flags: its load-bearing Ward input was later ledger-demoted to audited_renaming and the May chain contradicts it; the era claim beside its demotion trail.

## Provenance (pinned)

- Original path: `docs/YT_SCHEME_INDEPENDENCE_THEOREM.md`
- Source commit: `7bfb3d129239c3ca1f5cd045372b360c9302adf1`
- git blob: `68cd722017cb71f97feba8f7fbe32f023595f4a3`
- sha256: `7f49e041aa493ef6a1dced050c7fc9ad9ab3ff0cf9e54a7037cd2786f2e12d67`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch08/2424_YT_SCHEME_INDEPENDENCE_THEOREM.md](../../archive_unlanded/historic_intake_originals/branch08/2424_YT_SCHEME_INDEPENDENCE_THEOREM.md)
- Lines: 149; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_yt_scheme_independence​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/YT_UNBOUNDED_PROGRAM_NOTE.md` — April program note whose 'already closed' list includes the later-demoted Ward item — flag carried.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): Stated as a self-contained theorem, but its load-bearing Ward-identity input is later classified in this same branch (idx 2401) as audited-renaming and not authority.
- Extraction scope (triage compression; may reflect later context): Scheme-independence of the RATIO y_t/g_s only, not of y_t or g_s individually; depends on A1-A5.
- Extraction red flags: Title-overclaim risk: labelled 'THEOREM (self-contained proof)' and 'holds to all orders in any scheme', while the same-branch May notes retire the Ward-identity authority it rests on and show 1/sqrt(6) does not fix the physical readout.
- Supersession (as known at extraction): CONTRADICTED IN SPIRIT by the May PR #230 chain: 2401 finds yt_ward_identity is audited-renaming not authority, and 2413 shows the current surface (with 1/sqrt(6) held fixed) admits four different y_t/g_s values 0.408248/0.384900/0.288675/0.367423.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
