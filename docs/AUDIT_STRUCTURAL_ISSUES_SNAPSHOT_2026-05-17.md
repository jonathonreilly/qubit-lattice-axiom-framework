# Audit-Process Structural Issues Snapshot — 2026-05-17

**Claim type:** meta
**Status:** read-only diagnostic snapshot of recurring infrastructure / pipeline issues in audit verdicts. Not a claim under audit.

**Diagnostic tool:** `scripts/audit_structural_issues_verifier.py`
**Cached output:** `logs/runner-cache/audit_structural_issues_verifier.txt`

## Summary

| # | Issue | Count | Severity |
|---|---|---:|---|
| ISS-1 | Orchestrator not consuming `helper_runner_paths` | 3 | **HIGH** (active gap) |
| ISS-2 | Stale-numerics pattern (note tables disagree with runner) | 16 | MEDIUM (mechanical fix per case) |
| ISS-3 | Hash-drift orphans (note edited, ledger stale) | 0 | (none — pipeline in sync) |
| ISS-4 | Audited rows whose declared runner file is missing | 3 | MEDIUM (file recovery / removal) |
| **total** | | **22** | |

## ISS-1 — Orchestrator gap (HIGH severity)

Pipeline fix `860436c2e` landed `helper_runner_paths` in the ledger at **2026-05-17T13:14 UTC**. Three claims were re-audited 8-10 minutes later and STILL cite missing-helper language in their verdict rationale:

| claim | audit_date | helpers in ledger | rationale signal |
|---|---|---:|---|
| `asymmetry_persistence_mass_scaling_note` | 13:22 UTC | 4 | "unprovided helper modules" |
| `dense_prune_guard_seed_note` | 13:24 UTC | 4 | "imported … not provided" |
| `lattice_distance_law_note` | 13:24 UTC | 1 | "imports … from `scripts/lattice_mirror_distance.py` … not in the restricted packet" |

**Diagnosis:** the ledger has the field, but the **external orchestrator that calls Codex is not reading `helper_runner_paths`** when assembling the packet. The pipeline-side fix is complete; the orchestrator-side integration is not.

**Action required:** whoever owns the orchestrator (audit packet assembler) needs to read the new field and bundle helpers in the packet alongside the primary runner.

## ISS-2 — Stale-numerics pattern (16 cases)

The pattern: source-note tables freeze numbers from one runner version; later runner re-runs produce different numbers; auditor flags the mismatch and returns `audited_failed` or `audited_conditional`.

Sample (full list in verifier output):

- `born_lane_comparison_note` — note reports `3.28e-16`, runner reports `4.67e-16`
- `central_band_dense_largen_note` — N=80 collapse gravity is `-0.498±0.072`, note says `-0.576±0.045`
- `edge_deletion_boundary_note` — current sweep shows no sign flip; note claims one
- `distance_law_note` — note claims far-field `α ≈ -1.5`; runner shows different
- ... and 12 more

**Diagnosis:** notes treat runner output as a one-time snapshot. When the runner is re-run (often with helper updates), numbers drift. The note's "frozen rows" become stale.

**Action: per-case mechanical regen.** For each, either (a) update the note's tables from current runner output, or (b) explicitly mark the note's tables as "frozen at <date>" with the runner version pinned. Could be a future tool: `audit_stale_numerics_regenerator.py` that crawls these cases and proposes regen patches.

## ISS-3 — Hash-drift orphans (0 cases)

**Clean.** `seed_audit_ledger.py` is in sync with source notes. No audited row has a `note_hash` that differs from its on-disk file's hash. Good signal that hash-drift is not a current structural issue.

## ISS-4 — Missing runner files (3 cases)

Three audited rows declare a `runner_path` that doesn't exist on disk:

- `gauge_vacuum_plaquette_first_sector_rank_one_factorized_class_boundary_note_2026-04-19` → `scripts/frontier_gauge_vacuum_plaquette_first_sector_rank_one_factorized_class_boundary_2026_04_19.py`
- `gauge_vacuum_plaquette_first_sector_tail_underdetermination_theorem_note_2026-04-19` → `scripts/frontier_gauge_vacuum_plaquette_first_sector_tail_underdetermination_theorem_2026_04_19.py`
- `second_grown_family_note` → `scripts/second_grown_family_battery.py`

All three are `audited_failed`. The audit correctly noted missing runners and failed accordingly.

**Action:** either restore the runner files (recover from git history or rewrite) and re-audit, or mark the rows as `audited_failed` with a stable `repair_class=missing_runner_file`.

## Re-running the verifier

```bash
python3 scripts/audit_structural_issues_verifier.py
```

Re-run anytime to refresh counts. Useful as a periodic check (e.g., nightly with the audit pipeline) to keep structural-issue counts visible.

## What this snapshot does NOT establish

- A new claim or theorem
- An audit verdict (the audit lane decides per-claim)
- A direct fix for any of the 22 surfaced issues — only diagnosis + categorization
- A claim that other structural issues don't exist; only these four patterns were scanned

## Cross-references (non-load-bearing)

- `scripts/audit_structural_issues_verifier.py` (re-runnable diagnostic)
- `logs/runner-cache/audit_structural_issues_verifier.txt` (cached output)
- [PR #1277](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1277) (audit landscape snapshot, earlier)
- [PR #1371](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1371) (script-dep diagnostic + JSON map)
- [PR #1405](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1405) (pipeline integration of `helper_runner_paths`)
