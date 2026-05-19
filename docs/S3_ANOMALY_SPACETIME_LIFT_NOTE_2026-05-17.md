# `S3_ANOMALY_SPACETIME_LIFT_NOTE` — Downstream Surgical-Fix Record

**Date:** 2026-05-17
**Claim type:** meta
**Parent under repair:** [`S3_ANOMALY_SPACETIME_LIFT_NOTE.md`](S3_ANOMALY_SPACETIME_LIFT_NOTE.md)
**Wave:** downstream surgical-fix wave (direct dependent of `anomaly_forces_time_theorem`).
**Status:** branch-local hostile-audit findings; submitted as audit-prep input for the parent's pending audit review.
**Type:** fix-record meta-note (records what was patched; no new science content).
**Status authority:** independent audit lane only. This note does not set or predict the parent's audit outcome.

## 1. Source character

`S3_ANOMALY_SPACETIME_LIFT_NOTE.md` is an **`open_gate` route-survey** for
route-2 of the axiom-first GR-lift paths catalogued in
`FULL_GR_AXIOM_FIRST_PATHS_NOTE.md`. It is **not** a GR closure and not a
positive- or bounded-theorem promotion candidate. Its job is to record the
kinematic background `PL S^3 x R` as a composition of two cited upstream
authorities and to name the missing dynamics-bridge theorem as the single
currently-open blocker.

This downstream fix-record does **not** change that character. It only:

1. corrects a stale upstream-tier citation,
2. retracts an "exact and reusable" over-claim, and
3. discloses the admission-inheritance from the parent
   `ANOMALY_FORCES_TIME_THEOREM` (per its recent `F-B` framing-fix in
   [PR #1502](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1502)).

## 2. Findings

### F-A — Stale tier citation for `S3_BOUNDARY_LINK_THEOREM_NOTE.md`

**Symptom:** the original note cited the boundary-link companion as

> `claim_type: positive_theorem`, `audit_status: audited_conditional`

(and elsewhere said both `S^3` companions were `audited_conditional`).

**Reality (per the ledger snapshot):**

| field | value |
|---|---|
| `claim_id` | `s3_boundary_link_theorem_note` |
| `claim_type` | `bounded_theorem` |
| `audit_status` | `audited_clean` |
| `effective_status` | `retained_bounded` |

The cited tier was therefore **under-stated** — the ledger has the
boundary-link companion at `audited_clean` / `retained_bounded` rather
than `audited_conditional`. The cap-uniqueness companion is correctly
cited as `audited_conditional` / `bounded_theorem`; only the boundary-link
side was stale.

**Fix:** inline tier correction in the "Cited authorities" block and the
"Runner result" block; explicit composite-tier accounting in the
"Verdict" block (the composite inherits the weaker of the two tiers,
i.e. `audited_conditional`).

### F-B — Over-claim of "exact"

**Symptom:** the "Route 2 in context" block previously contained the
bullets

> - `S^3` is exact and reusable
> - anomaly-forced time is exact and reusable

These were inconsistent with the rest of the note, which correctly
describes the cap-uniqueness companion as `audited_conditional` and the
anomaly-forced-time theorem as `bounded_theorem` (with admissions
(i)-(iv)). "Exact" is a stronger claim than either upstream authority
actually carries.

**Fix:** the two bullets are replaced with tier-accurate wording:

- `S^3` is `retained_bounded` (boundary-link) and `audited_conditional`
  (cap-uniqueness); reusable at the weaker tier of the composite.
- anomaly-forced time is `bounded_theorem` with named admissions
  (i)-(iv); reusable at the bounded tier modulo those admissions.
- the combined lift `PL S^3 x R` is the right kinematic target at the
  bounded tier inherited from its upstream authorities, not at an
  "exact" tier.

A retraction sentence is appended in the same block. No claim in the
audit-boundary, verdict, or open-gate sections changes.

### F-C — Missing admission-inheritance disclosure

**Symptom:** the note imports the `d_t = 1` conclusion from
`ANOMALY_FORCES_TIME_THEOREM.md` as a single kinematic input without
acknowledging:

- the upstream parent's admission structure (admissions (i)-(iv)), which
  conditions the `d_t = 1` conclusion; and
- the recent `F-B` framing-fix on the parent
  ([`ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md`](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md)),
  which makes the derived-vs-inherited decomposition of `d_t = 1`
  explicit upstream.

A downstream consumer reading the survey alone could not see that any
future revision of admission (iv) would propagate directly into the
route-2 kinematic background here.

**Fix:** a new subsection "Admission inheritance from
`ANOMALY_FORCES_TIME_THEOREM`" is added immediately after the
"Cited authorities" list. It:

- enumerates admissions (i)-(iv) and their routing status on the parent;
- records the derived-vs-inherited decomposition of `d_t = 1` from the
  parent's `F-B` fix:
  - **Derived (Step 3):** `d_t ∈ {1, 3, 5, ...}`,
  - **Inherited (admission (iv)):** `d_t > 1` excluded → `d_t = 1`;
- states explicitly that this note treats `d_t = 1` as a black-box
  kinematic input and does **not** insulate downstream consumers from
  future revisions of admission (iv).

## 3. What this fix does NOT do

- It does **not** close the dynamics-bridge gap (the named
  open-route blocker).
- It does **not** change the route-survey verdict, the route-ranking, or
  the 10-route enumeration.
- It does **not** promote the row beyond `open_gate`.
- It does **not** set or predict an audit outcome; the audit lane decides
  whether the corrected wording is sufficient or whether further
  sharpening is required.
- It does **not** modify any pipeline code, any other source theorem
  note, or any retained-tier claim.

## 4. Suggested auditor verdict

`audited_conditional` (open_gate retained as route-survey). The corrected
wording brings the in-note tier accounting into line with the ledger and
makes the upstream admission-inheritance explicit. The row's character is
unchanged: kinematically clean, dynamically unclosed, awaiting one of the
three named dynamics-bridge primitives.

If the audit lane judges the open-gate framing already adequate even with
the prior wording, that judgement is undisturbed by these edits — they
are all clarifications, not new claims.

## 5. Verification

Paired runner:
`scripts/frontier_s3_anomaly_spacetime_lift_downstream_fix.py`

Programmatically verifies:

- F-A: the corrected tier strings appear and the stale strings do not;
- F-B: the retraction sentence is present and the "exact and reusable"
  bullets are gone;
- F-C: the "Admission inheritance" subsection is present and references
  the parent's `F-B` fix-record note;
- structural invariants: `open_gate` claim type unchanged; route-survey
  verdict unchanged; cited-authorities block still names the same three
  upstream authorities; no retained-tier promotion implied.

Cached output: `logs/runner-cache/frontier_s3_anomaly_spacetime_lift_downstream_fix.txt`.

## 6. Cross-references (non-load-bearing)

- [`S3_ANOMALY_SPACETIME_LIFT_NOTE.md`](S3_ANOMALY_SPACETIME_LIFT_NOTE.md) — parent under repair
- [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md) — upstream parent
- [`ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md`](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md) — upstream `F-B` fix
- [`ANOMALY_FORCES_TIME_ADMISSION_III_ROUTING_CORRECTION_NOTE_2026-05-17.md`](ANOMALY_FORCES_TIME_ADMISSION_III_ROUTING_CORRECTION_NOTE_2026-05-17.md) — upstream `F-C` fix
- [`S3_BOUNDARY_LINK_THEOREM_NOTE.md`](S3_BOUNDARY_LINK_THEOREM_NOTE.md) — cited authority (corrected tier)
- [`S3_CAP_UNIQUENESS_NOTE.md`](S3_CAP_UNIQUENESS_NOTE.md) — cited authority
- [PR #1500](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1500) — upstream `F-C` PR
- [PR #1502](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1502) — upstream `F-B` PR
