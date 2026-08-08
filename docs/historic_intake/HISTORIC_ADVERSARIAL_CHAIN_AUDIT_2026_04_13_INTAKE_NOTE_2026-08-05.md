# Historic intake: Adversarial Chain Audit: y_t and DM Closure Claims

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

Hostile audit of the y_t and dark-matter closure chains finds neither is zero-parameter: the y_t chain imports the observed Higgs VEV v = 246 GeV (HIGH severity) plus PDG quark masses and electroweak couplings, and the DM chain assumes all 8 tastes couple to sphalerons (N_taste/N_gen = 8/3, HIGH) with a g_* inconsistency (106.75 vs 110.75).

Original verdict: Both closure claims fail zero-parameter status; the genuinely framework-derived core is smaller (alpha_plaq = 0.092, y_t/g_s = 1/sqrt(6), Z_gauge = 1, R_base = 31/9, Sommerfeld factor, x_F ~ 25).
Scope: Audit of GATE_CLOSURE_CASE_YT_DM_2026-04-13.md, tracing every input of both chains to source.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Hostile chain audit: the y_t chain imports the observed v = 246 GeV (HIGH severity) + g_* inconsistency (106.75 vs 110.75) — direct adverse evidence against the pulled zero-import closure claim; audit lane needs both sides.

## Provenance (pinned)

- Original path: `docs/ADVERSARIAL_CHAIN_AUDIT_2026-04-13.md`
- Source commit: `48fb3d50ebf30425a908334a183c1b322a8d7d78`
- git blob: `6af84efe463194ca1fdc59b8d318a04a0be26c5d`
- sha256: `7aee2fbf50801c1af0912ea712af31a4b814307bcb957da260cd7726e6789abd`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch01/40_ADVERSARIAL_CHAIN_AUDIT_2026-04-13.md](../../archive_unlanded/historic_intake_originals/branch01/40_ADVERSARIAL_CHAIN_AUDIT_2026-04-13.md)
- Lines: 445; runners named: historic runner (unpinned, not in this packet): `frontier_alpha_s_determination(.py)`; historic runner (unpinned, not in this packet): `frontier_bbn_from_framework(.py)`; historic runner (unpinned, not in this packet): `frontier_dm_native_eta(.py)`; historic runner (unpinned, not in this packet): `frontier_ewpt_gauge_closure(.py)`; historic runner (unpinned, not in this packet): `frontier_freezeout_from_lattice(.py)`; historic runner (unpinned, not in this packet): `frontier_yt_boundary_resolution(.py)`; historic runner (unpinned, not in this packet): `frontier_yt_matching(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Cross-stratum flags

- Attaches across strata to [idx 3620](HISTORIC_YT_ZERO_IMPORT_CLOSURE_NOTE_INTAKE_NOTE_2026-08-05.md) (`docs/YT_ZERO_IMPORT_CLOSURE_NOTE.md`, stratum recovery) — Hostile chain audit: the y_t chain imports the observed v = 246 GeV (HIGH severity) + g_* inconsistency (106.75 vs 110.75) — direct adverse evidence against the pulled zero-import closure claim; audit lane needs both sides.

## Flags carried

Names an internal inconsistency in g_* (106.75 vs 110.75) and substantial hidden observational imports in a chain advertised as closed.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_analysis
intake_directive: owner_2026-08-05
```

Independent audit still required.
