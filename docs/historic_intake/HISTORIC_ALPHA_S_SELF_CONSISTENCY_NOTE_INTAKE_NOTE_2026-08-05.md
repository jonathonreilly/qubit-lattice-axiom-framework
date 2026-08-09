# Historic intake: Alpha_s Self-Consistency: Can the Lattice Constrain alpha_s?

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

alpha_s(M_Pl) = 0.092 is NOT derived from first principles: the chain g_bare = 1 -> alpha_bare = 1/(4pi) = 0.07958 -> c_1 = pi^2/3 -> alpha_V = -ln(1 - c_1 alpha_bare)/c_1 = 0.0923 has no free parameters once g = 1 and log resummation are adopted, but g = 1 is a natural normalization selected by no dynamical mechanism (no free-energy extremum, no beta=6 phase transition for SU(3)).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The honest alpha_s terminal: 0.092 NOT first-principles — conditional on g_bare = 1 and scheme, Landau-pole flag on the record; the era's central coupling claim properly bounded.

## Provenance (pinned)

- Original path: `docs/ALPHA_S_SELF_CONSISTENCY_NOTE.md`
- Source commit: `141e0646d05ed0f3af60bbffde7184f292266915`
- git blob: `38bb2657e9e27c1f6c8f307cfb5d56be6b88b654`
- sha256: `4c4a3b46815a4a49a5a40c75faff17d5031c51065a77444b41aef6c448e5f917`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch01/50_ALPHA_S_SELF_CONSISTENCY_NOTE.md](../../archive_unlanded/historic_intake_originals/branch01/50_ALPHA_S_SELF_CONSISTENCY_NOTE.md)
- Lines: 146; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_alpha_s_self_consistency​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/ALPHA_S_DETERMINATION_NOTE.md` — The parameter-eliminated claim form; rides the honest terminal.
- `docs/ALPHA_S_DM_RATIO_RESULT_2026-04-12.md` — Earliest preliminary with self-doubt on the record.
- `docs/ALPHA_S_ROBUSTNESS_NOTE.md` — Five-scheme robustness evidence.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): The lattice constrains alpha_s only conditionally — the value is uniquely determined by lattice geometry and SU(3) group theory given g = 1, which is itself unselected.
- Extraction scope (triage compression; may reflect later context): Bounded: 17/17 runner PASS, 8 exact and 9 bounded results; conditional on g=1 and the V-scheme log-resummation prescription.
- Extraction red flags: Flags that the V-scheme coupling hits a Landau pole under perturbative QCD running, confirming it is not an MS-bar coupling.
- Supersession (as known at extraction): none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded
intake_directive: owner_2026-08-05
```

Independent audit still required.
