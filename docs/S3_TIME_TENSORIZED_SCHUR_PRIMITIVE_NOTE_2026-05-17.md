# `S3_TIME_TENSORIZED_SCHUR_PRIMITIVE_NOTE` — Downstream Surgical-Fix Record

**Date:** 2026-05-17
**Claim type:** meta
**Parent under repair:** [`S3_TIME_TENSORIZED_SCHUR_PRIMITIVE_NOTE.md`](S3_TIME_TENSORIZED_SCHUR_PRIMITIVE_NOTE.md)
**Wave:** downstream surgical-fix wave (direct dependent of `anomaly_forces_time_theorem`).
**Status:** branch-local hostile-audit findings; submitted as audit-prep input for the parent's pending audit review.
**Type:** fix-record meta-note (records what was patched; no new science content).
**Status authority:** independent audit lane only.

## 1. Source character

`S3_TIME_TENSORIZED_SCHUR_PRIMITIVE_NOTE.md` is a `bounded_theorem`
that builds a **two-channel boundary completion** around the cited
scalar Schur action:

```
I_TS^(0)(f, a; j) = I_R(f; j) + 1/2 || a - Theta_R^(0)(delta_A1(f)) ||^2
```

with minimal positive-definite tensor kernel `K_TS = I_2`. The
construction itself is unchanged. The hostile-audit-grade issues
patched here are about the **tier qualifier** on the upstream scalar
backbone.

## 2. Findings

### F-A — Over-claim "exact" for scalar backbone

The §Exact scalar backbone block had 5 "exact" bullets for the upstream
composite plus two more "exact" qualifiers in §Atlas-facing
interpretation and §Bottom line:

| Section | Original wording |
|---|---|
| §Exact scalar backbone | "exact `S^3` spatial closure" |
| §Exact scalar backbone | "exact anomaly-forced time with `d_t = 1`" |
| §Exact scalar backbone | "exact background `PL S^3 x R`" |
| §Exact scalar backbone | "exact slice generator `Lambda_R`" |
| §Exact scalar backbone | "exact microscopic Schur boundary action" |
| §Atlas-facing interpretation | "exact scalar Schur boundary action: retained tool" |
| §Bottom line | "exact scalar boundary action `I_R`" |

**Reality (per 2026-05-17 ledger snapshot):**

| Upstream | `audit_status` | `effective_status` |
|---|---|---|
| `s3_boundary_link_theorem_note` | `audited_clean` | `retained_bounded` |
| `s3_cap_uniqueness_note` | `audited_conditional` | `audited_conditional` |
| `anomaly_forces_time_theorem` | `unaudited` | `unaudited` |
| `oh_schur_boundary_action_note` | (per ledger) | `retained_bounded` (on strong-field bridge surface only) |

**None of the upstreams is at `retained_clean`.** The composite
`PL S^3 x R` background is at most `audited_conditional` (via
cap-uniqueness) / `unaudited` (via anomaly-forced time). The Schur
action is `retained_bounded` only on the strong-field bridge surface
(not on the full retained-grade dynamical sector). Calling these
"exact" is tier-loose.

**Fix:**

- §Exact scalar backbone → §Cited scalar backbone (heading renamed);
  bullets corrected to tier-honest wording with explicit qualifiers;
- §Atlas-facing interpretation bullet: "exact scalar Schur boundary
  action: retained tool" → "bounded scalar Schur boundary action:
  `retained_bounded` tool (on the strong-field bridge surface only)";
- §Bottom line bullet: "exact scalar boundary action `I_R`" → "bounded
  scalar boundary action `I_R` (`retained_bounded` on the strong-field
  bridge surface only)".

The tensor-extension content (`I_TS^(0)`, two-channel completion,
`K_TS = I_2` kernel, rank-one obstruction argument, "What it does not
do" list) is unchanged.

### F-B — Admission-inheritance disclosure

The tensorized primitive imports `d_t = 1` from
`ANOMALY_FORCES_TIME_THEOREM`. Per the parent's recent
[F-B framing-fix](ANOMALY_FORCES_TIME_FB_NOTE_2026-05-17.md),
`d_t = 1` decomposes into derived (Step 3) and inherited
(admission (iv)) branches. The tensorized primitive's tensor-extension
content is admission-independent; only the clock-step kinematic
input inherits.

**Fix:** new "Upstream-tier accounting (2026-05-17)" section enumerates
the upstream tiers and records the admission-(iv) inheritance.

## 3. What this fix does NOT do

- Change `I_TS^(0)(f, a; j)` or its block-diagonal form.
- Change `K_TS = I_2` minimal positive-definite kernel.
- Change the source-side comparison-surface numerics
  (`Theta_R^(0)(e0) = (-3.772329e-04, +3.359952e-04)`, etc.).
- Change the rank-one obstruction argument or the `A1`-blind reduction.
- Change the "What it does not do" claim list.
- Promote any upstream companion or alter any retained-tier claim.
- Modify pipeline code or any other source theorem note.
- Set or predict an audit outcome.

## 4. Suggested auditor verdict

`audited_conditional` (bounded_theorem retained; effective tier
inherits from the weakest upstream, currently `unaudited` via
`ANOMALY_FORCES_TIME_THEOREM`).

The corrected note brings the upstream-tier qualifier into line with
the ledger and discloses the admission-inheritance. The tensorized
primitive's construction is unaffected.

## 5. Verification

Paired runner:
`scripts/frontier_s3_time_tensorized_schur_primitive_downstream_fix.py`

Programmatically verifies:

- **F-A:** stale "exact" bullets retired from §Cited scalar backbone
  (heading renamed); §Atlas-facing interpretation and §Bottom line
  bullets corrected to tier-honest wording.
- **F-B:** Upstream-tier accounting section enumerates the upstreams
  with their actual ledger tiers; upstream F-B framing-fix linked;
  admission-(iv) inheritance disclosed.
- **Structural invariants:** `I_TS^(0)` definition preserved;
  `K_TS = I_2` preserved; comparison-surface numerics preserved;
  "What it does not do" list preserved.

Cached output: `logs/runner-cache/frontier_s3_time_tensorized_schur_primitive_downstream_fix.txt`.

## 6. Cross-references (non-load-bearing)

- [`S3_TIME_TENSORIZED_SCHUR_PRIMITIVE_NOTE.md`](S3_TIME_TENSORIZED_SCHUR_PRIMITIVE_NOTE.md) — parent under repair
- [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md) — upstream parent
- [`ANOMALY_FORCES_TIME_FB_NOTE_2026-05-17.md`](ANOMALY_FORCES_TIME_FB_NOTE_2026-05-17.md) — upstream F-B fix
- [PR #1510](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1510) — sibling `s3_time_*` downstream fix
- [PR #1515](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1515) — sibling `s3_time_*` downstream fix
- [PR #1507](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1507) — upstream sibling
