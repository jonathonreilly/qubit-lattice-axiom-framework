# Historic intake: FH/LSZ Numba Seed-Independence Audit

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_no_go
Stratum: branch_only_never_mainlined
Era: may_june_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Chunks001 and 002 have different metadata seeds but identical gauge-evolution signatures — identical plaquette mean, identical selected mass fit, identical dE/ds slope — with no numba_gauge_seed_v1 marker proving the gauge evolution was seeded inside run_volume_numba; the scalar stochastic rows differ only because they use a separate NumPy RNG. The harness now seeds per volume and the combiner rejects unmarked chunks and duplicate gauge signatures across distinct seeds. PASS=8 FAIL=0.

Original verdict: Historical chunk001/chunk002 are production-format diagnostics only and must be rerun under the patched harness or excluded before contributing to L12 combination.
Scope: Evidence-quality gate; closes no physics.


## Why pulled (supervisor decision, on the record)

REPRODUCIBILITY DEFECT: two 'independent' published chunks share an identical gauge ensemble (numba RNG never seeded) — invalidates the first two production checkpoints; audit work order.

## Provenance (pinned)

- Original path: `docs/YT_FH_LSZ_NUMBA_SEED_INDEPENDENCE_AUDIT_NOTE_2026-05-02.md`
- Source commit: `05bae6b336cd54d6c31c9a3536d51c5e5eedfa7a`
- git blob: `cfa0c4aa335e70ec708517725235b90f2a6114ac`
- sha256: `8eefdd92c08767b270bef4db7d5dd8c0bbfec25254f7570d4871b233552e89a6`
- Lines: 52; runners named: scripts/frontier_yt_fh_lsz_chunk_combiner_gate.py, scripts/frontier_yt_fh_lsz_numba_seed_independence_audit.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

A real reproducibility defect found post hoc: two chunks published as independent production evidence shared an identical gauge ensemble because numba's RNG was never seeded.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
