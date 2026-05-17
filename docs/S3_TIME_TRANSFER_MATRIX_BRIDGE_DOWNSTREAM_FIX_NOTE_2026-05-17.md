# `S3_TIME_TRANSFER_MATRIX_BRIDGE_NOTE` — Downstream Surgical-Fix Record

**Date:** 2026-05-17
**Parent under repair:** [`S3_TIME_TRANSFER_MATRIX_BRIDGE_NOTE.md`](S3_TIME_TRANSFER_MATRIX_BRIDGE_NOTE.md)
**Wave:** downstream surgical-fix wave (direct dependent of `anomaly_forces_time_theorem`).
**Status:** branch-local hostile-audit findings; submitted as audit-prep input for the parent's pending audit review.
**Type:** fix-record meta-note (records what was patched; no new science content).
**Status authority:** independent audit lane only.

## 1. Source character

`S3_TIME_TRANSFER_MATRIX_BRIDGE_NOTE.md` is a `bounded_theorem` that
records a **class-A spectral-calculus construction**: conditional on
the cited `PL S^3` topology, anomaly-forced `d_t = 1`, and the exact
Schur-complement boundary generator `Λ_R`, the one-step Euclidean
transfer operator `T_R := exp(-Λ_R)` is defined and runner-verified to
be a positive self-adjoint contraction.

The bridge construction itself is unchanged. The hostile-audit-grade
issues patched here are about the **tier qualifiers** on the upstream
composite and a stale boundary-link citation tier.

## 2. Findings

### F-A — Over-claim "exact" / "retained" in body

The note's top-of-file "Cited authorities" block correctly tagged
upstreams as `audited_conditional` / `bounded_theorem` /
`retained_bounded`. But the body slipped back to "exact" / "retained"
wording at several sites:

| Section | Original wording |
|---|---|
| §Exact ingredients available — S^3 compactification | "the retained spatial background candidate" |
| §Exact ingredients available — Anomaly-forced time | "the retained temporal background candidate" |
| §Clean bounded bridge candidate (closing line) | "exact spatial slice + exact one-clock time + exact boundary Hamiltonian" |
| §Runnable summary | "`S^3` topology is exact / anomaly-forced time is exact" |

**Reality:** the composite `PL S^3` background inherits the weakest of
the two cited PL companions' tiers, currently `audited_conditional`
(via cap-uniqueness). `ANOMALY_FORCES_TIME_THEOREM` is currently
`unaudited` with named admissions (i)-(iv). Calling either "exact"
overstates the upstream tiers and is internally inconsistent with the
note's own cited-authorities block.

**Fix:** §Exact ingredients block now uses "bounded composite" /
"cited" wording with explicit tier annotations; §Clean bounded bridge
candidate retraction sentence appended; §Runnable summary corrected
inline.

### F-B — Admission-inheritance disclosure

The bridge imports `d_t = 1` as the one-clock Cauchy step. Per the
upstream parent's recent
[F-B framing-fix](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md),
the parent's `d_t = 1` conclusion decomposes into derived part
(Step 3: `d_t ∈ {1, 3, 5, ...}`) and inherited part (admission (iv):
`d_t > 1` excluded).

**Fix:** new "Upstream-tier accounting (2026-05-17)" subsection records
the admission-inheritance and links to the upstream F-B framing-fix.
The bridge's `T_R = exp(-Λ_R)` spectral-calculus construction itself is
unaffected; only the `d_t = 1` kinematic input inherits the parent's
admission structure.

### F-C-like — Stale `s3_boundary_link` citation tier

The cited-authorities block listed:

> `S3_BOUNDARY_LINK_THEOREM_NOTE.md` — `claim_type: positive_theorem`,
> `audit_status: audited_conditional`

The 2026-05-17 ledger has:

| field | value |
|---|---|
| `claim_type` | `bounded_theorem` |
| `audit_status` | `audited_clean` |
| `effective_status` | `retained_bounded` |

This is the same stale citation already fixed upstream in
[PR #1507](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1507)
for `s3_anomaly_spacetime_lift_note`. The cap-uniqueness companion was
cited correctly (`audited_conditional`); only the boundary-link side
was stale.

**Fix:** inline correction of the cited-authorities block entry with
the same explanatory parenthetical used in PR #1507. The composite
`PL S^3` tier inherits from the weaker of the two cited PL companions
(`audited_conditional` via cap-uniqueness), which is now made
explicit.

## 3. What this fix does NOT do

- Change the `T_R = exp(-Λ_R)` definition.
- Change the runner-verified spectral-calculus properties (symmetry,
  positivity, contraction).
- Change the "Sharp blocker" wording about Einstein/Regge dynamics.
- Change the `bounded_theorem` claim type or the "Verdict" wording.
- Promote any upstream companion or alter any retained-tier claim.
- Modify pipeline code or any other source theorem note.
- Set or predict an audit outcome.

## 4. Suggested auditor verdict

`audited_conditional` (bounded_theorem retained; effective tier
inherits from the weakest upstream, currently `unaudited` via
`ANOMALY_FORCES_TIME_THEOREM` and `audited_conditional` via the cited
PL composite).

The corrected note brings the body tier descriptors into line with the
already-honest cited-authorities block, discloses the upstream
admission-inheritance, and refreshes the stale boundary-link citation
tier. The `T_R = exp(-Λ_R)` construction is unaffected.

## 5. Verification

Paired runner:
`scripts/frontier_s3_time_transfer_matrix_bridge_downstream_fix.py`

Programmatically verifies:

- **F-A:** stale "exact"/"retained" wordings retired from §Exact
  ingredients available, §Clean bounded bridge candidate, §Runnable
  summary; replacement "bounded composite" / "cited" wording present;
  retraction sentences present.
- **F-B:** new "Upstream-tier accounting (2026-05-17)" subsection
  enumerates the upstreams with their actual ledger tiers; the
  upstream F-B framing-fix is linked; admission-(iv) inheritance is
  disclosed.
- **F-C-like:** boundary-link companion tier corrected to
  `bounded_theorem` / `audited_clean` / `retained_bounded`; stale
  `positive_theorem` / `audited_conditional` bigram retired from that
  citation line.
- **Structural invariants:** `T_R = exp(-Λ_R)` definition preserved;
  runner-checked properties preserved; verdict and sharp-blocker
  wording preserved; cited-authorities still names the same five
  upstream notes.

Cached output: `logs/runner-cache/frontier_s3_time_transfer_matrix_bridge_downstream_fix.txt`.

## 6. Cross-references (non-load-bearing)

- [`S3_TIME_TRANSFER_MATRIX_BRIDGE_NOTE.md`](S3_TIME_TRANSFER_MATRIX_BRIDGE_NOTE.md) — parent under repair
- [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md) — upstream parent
- [`ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md`](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md) — upstream F-B fix
- [PR #1507](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1507) — sibling fix (same s3_boundary_link tier correction)
- [PR #1509](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1509) — sibling downstream fix
- [PR #1510](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1510) — sibling downstream fix (same `s3_time_*` lineage)
- [PR #1511](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1511) — sibling downstream fix
- [PR #1512](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1512) — sibling downstream fix
- [PR #1513](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1513) — sibling downstream fix
- [PR #1514](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1514) — sibling downstream fix
