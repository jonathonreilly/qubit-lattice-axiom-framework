# Historic intake: FH/LSZ Numba Seed-Independence Audit

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: branch_only_never_mainlined
Era: may_june_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

Registered as a bounded registration of a historical negative claim; no live no-go is asserted by this wrapper — no-go discipline applies at audit adjudication.

## The claim (as stated by the original, supervisor-compressed)

Chunks001 and 002 have different metadata seeds but identical gauge-evolution signatures — identical plaquette mean, identical selected mass fit, identical dE/ds slope — with no numba_gauge_seed_v1 marker proving the gauge evolution was seeded inside run_volume_numba; the scalar stochastic rows differ only because they use a separate NumPy RNG. The harness now seeds per volume and the combiner rejects unmarked chunks and duplicate gauge signatures across distinct seeds. PASS=8 FAIL=0.

Original verdict: Historical chunk001/chunk002 are production-format diagnostics only and must be rerun under the patched harness or excluded before contributing to L12 combination.
Scope: Evidence-quality gate; closes no physics.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

REPRODUCIBILITY DEFECT: two 'independent' published chunks share an identical gauge ensemble (numba RNG never seeded) — invalidates the first two production checkpoints; audit work order.

## Provenance (pinned)

- Original path: `docs/YT_FH_LSZ_NUMBA_SEED_INDEPENDENCE_AUDIT_NOTE_2026-05-02.md`
- Source commit: `05bae6b336cd54d6c31c9a3536d51c5e5eedfa7a`
- git blob: `cfa0c4aa335e70ec708517725235b90f2a6114ac`
- sha256: `8eefdd92c08767b270bef4db7d5dd8c0bbfec25254f7570d4871b233552e89a6`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch07/2244_YT_FH_LSZ_NUMBA_SEED_INDEPENDENCE_AUDIT_NOTE_2026-05-02.md](../../archive_unlanded/historic_intake_originals/branch07/2244_YT_FH_LSZ_NUMBA_SEED_INDEPENDENCE_AUDIT_NOTE_2026-05-02.md)
- Lines: 52; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_yt_fh_lsz_chunk_combiner_gate​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_yt_fh_lsz_numba_seed_independence_audit​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: A real reproducibility defect found post hoc: two chunks published as independent production evidence shared an identical gauge ensemble because numba's RNG was never seeded.
- Supersession (as known at extraction): Invalidates the first two production checkpoints of the sweep (idx 2192, 2194) as independent evidence and forces the replacement-rerun wave at idx 2193-2197.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_no_go
intake_directive: owner_2026-08-05
```

Independent audit still required.
