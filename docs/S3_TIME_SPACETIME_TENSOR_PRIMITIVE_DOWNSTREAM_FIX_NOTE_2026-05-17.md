# `S3_TIME_SPACETIME_TENSOR_PRIMITIVE_NOTE` — Downstream Surgical-Fix Record

**Date:** 2026-05-17
**Parent under repair:** [`S3_TIME_SPACETIME_TENSOR_PRIMITIVE_NOTE.md`](S3_TIME_SPACETIME_TENSOR_PRIMITIVE_NOTE.md)
**Wave:** downstream surgical-fix wave (direct dependent of `anomaly_forces_time_theorem`).
**Status:** branch-local hostile-audit findings; submitted as audit-prep input for the parent's pending audit review.
**Type:** fix-record meta-note (records what was patched; no new science content).
**Status authority:** independent audit lane only. This note does not set or predict the parent's audit outcome.

## 1. Source character

`S3_TIME_SPACETIME_TENSOR_PRIMITIVE_NOTE.md` defines a **bounded
spacetime tensor primitive candidate**

```
Xi_R^(0)(t; q) := Theta_R^(0)(q) ⊗ V_R(t),    V_R(t) := exp(-t Λ_R) u_*
```

on the composite route-2 background `PL S^3 x R`. The note is honest
about `Xi_R^(0)` itself being **bounded, not exact** ("bounded
spacetime primitive candidate rather than a theorem-grade
Einstein/Regge dynamics law").

The two hostile-audit-grade issues fixed here are about how the note
described the **upstream background**, not about the candidate
`Xi_R^(0)` itself. The candidate's bounded character is unchanged.

## 2. Findings

### F-A — Over-claim of "exact background"

**Symptom:** at three sites the note called `PL S^3 x R` an "exact"
background:

| site | original wording |
|---|---|
| Verdict bullet | "exact background `PL S^3 x R`" |
| "Background" block | "The route-2 background remains exact:" |
| "Bottom line" bullet | "exact background: `PL S^3 x R`" |

**Reality (per 2026-05-17 ledger snapshot):**

| Upstream | `claim_type` | `audit_status` | `effective_status` |
|---|---|---|---|
| `S3_BOUNDARY_LINK_THEOREM_NOTE` | `bounded_theorem` | `audited_clean` | `retained_bounded` |
| `S3_CAP_UNIQUENESS_NOTE` | `bounded_theorem` | `audited_conditional` | `audited_conditional` |
| `ANOMALY_FORCES_TIME_THEOREM` | `bounded_theorem` | `unaudited` | `unaudited` |

Composite `PL S^3 x R` inherits at best the **weakest** tier in the
composition. With `ANOMALY_FORCES_TIME_THEOREM` currently `unaudited`,
the composite tier is also `unaudited` — and will rise no higher than
the worst of the audited components once that audit lands.

**Fix:** all three sites now read "bounded composite background" /
"bounded composite". A new "Upstream-tier accounting" section spells
out the composite tier explicitly with a table. A retraction sentence
is appended in the "Background" block.

### F-B — Missing admission-inheritance from upstream parent

**Symptom:** the note imported `PL S^3 x R` as a black-box background
without disclosing:

- the upstream parent's named admissions (i)-(iv);
- the parent's recent
  [F-B framing-fix](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md),
  which decomposes the parent's `d_t = 1` conclusion into a derived
  part (Step 3: `d_t ∈ {1, 3, 5, ...}`) and an inherited part
  (admission (iv): `d_t > 1` excluded).

A downstream reader could not see that any future revision of
admission (iv) propagates directly into the route-2 background here.

**Fix:** the new "Upstream-tier accounting" section enumerates
admissions (i)-(iv), records their routing status (internal companions
for (ii)-(iv); bare external admission for (i)), and gives the derived
vs inherited decomposition of `d_t = 1` from the parent's `F-B` fix.
The note explicitly states that it treats `PL S^3 x R` as a black-box
bounded composite input and does **not** insulate `Xi_R^(0)` from
upstream admission revisions.

## 3. What this fix does NOT do

- Change the `Xi_R^(0)` candidate definition (`Theta_R^(0)(q) ⊗ V_R(t)`).
- Change the candidate's bounded-not-exact character.
- Change the sharp blocker ("no exact tensor-valued support observable
  on `A1 x {E_x, T1x}` in the current retained support-side machinery").
- Change the runnable-sanity-conditions list or any runner expectation.
- Promote any companion theorem or propose any retained-tier status.
- Modify any pipeline code or any other source theorem note.
- Set or predict an audit outcome.

## 4. Suggested auditor verdict

`audited_conditional` (bounded candidate retained; effective tier
inherits the weakest of the upstream composite, currently `unaudited`
via `ANOMALY_FORCES_TIME_THEOREM`).

The corrected note:

- gives honest tier labels for the upstream composite;
- enumerates the inherited admission structure explicitly;
- preserves the candidate's bounded character and the sharp blocker;
- does not over-claim either the route's status or the candidate's tier.

Once the upstream `ANOMALY_FORCES_TIME_THEOREM` audits through, the
composite background's tier rises automatically without further
surgical edits on this row.

## 5. Verification

Paired runner:
`scripts/frontier_s3_time_spacetime_tensor_primitive_downstream_fix.py`

Programmatically verifies:

- **F-A:** stale "exact background" wording retired at all three sites
  (Verdict bullet, Background block, Bottom line); "bounded composite"
  / "bounded composite background" wording present; "Upstream-tier
  accounting" section present with the three-row tier table.
- **F-B:** admissions (i)-(iv) named; derived vs inherited
  decomposition of `d_t = 1` recorded; the upstream `F-B` framing-fix
  note is linked.
- **Structural invariants:** `Xi_R^(0)` definition unchanged; "bounded,
  not exact" character of the candidate preserved; sharp-blocker
  wording preserved; the candidate is **not** promoted to exact.

Cached output: `logs/runner-cache/frontier_s3_time_spacetime_tensor_primitive_downstream_fix.txt`.

## 6. Cross-references (non-load-bearing)

- [`S3_TIME_SPACETIME_TENSOR_PRIMITIVE_NOTE.md`](S3_TIME_SPACETIME_TENSOR_PRIMITIVE_NOTE.md) — parent under repair
- [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md) — upstream parent
- [`ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md`](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md) — upstream `F-B` fix
- [`S3_BOUNDARY_LINK_THEOREM_NOTE.md`](S3_BOUNDARY_LINK_THEOREM_NOTE.md) — cited upstream
- [`S3_CAP_UNIQUENESS_NOTE.md`](S3_CAP_UNIQUENESS_NOTE.md) — cited upstream
- [PR #1500](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1500) — upstream `F-C` PR
- [PR #1502](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1502) — upstream `F-B` PR
- [PR #1507](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1507) — sibling downstream fix (`s3_anomaly_spacetime_lift_note`)
- [PR #1509](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1509) — sibling downstream fix (`dt1_time_dimension_proof_walk`)
