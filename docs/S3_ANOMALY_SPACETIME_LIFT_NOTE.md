# `S^3` + Anomaly-Forced Time: Axiom-First Spacetime Lift

**Status:** open route survey — kinematic background candidate with explicitly
named missing dynamics theorem. **Not** a full-GR closure.
**Date:** 2026-04-14 (audit-narrowing refresh: 2026-05-10)
**Branch:** `codex/review-active`
**Purpose:** route-2 assessment from
[`FULL_GR_AXIOM_FIRST_PATHS_NOTE.md`](FULL_GR_AXIOM_FIRST_PATHS_NOTE.md)
**Type:** open_gate (route-survey)
**Status authority:** independent audit lane only.
**Authority role:** identifies, but does not close, a candidate axiom-first
GR-lift architecture. Names the missing dynamics-bridge primitive as the
single open theorem target for this route.
**Primary runner:** [`scripts/frontier_s3_anomaly_spacetime_lift.py`](../scripts/frontier_s3_anomaly_spacetime_lift.py)
checks the route-2 source boundary against the current bounded/conditional
upstream tiers and verifies that the dynamics bridge remains explicitly open.

## Audit boundary

This note is an open-route survey. It does two things:

1. **Records the kinematic background candidate** `PL S^3 x R` as the unique
   target obtained by composing two existing upstream authorities:
   - the `PL S^3` compactification family (cited; not closed in this note);
   - the anomaly-forced time-direction theorem (cited; not closed in this
     note).
   The composition `PL S^3 x R` itself is a kinematic statement at the level
   of background topology, not a dynamics derivation.
2. **Names the missing dynamics bridge** as the single open theorem target
   needed to lift this route to a full-GR closure. No such bridge is
   constructed inside this note.

Under the rubric, this row is therefore an `open_gate` route survey, not a
positive- or bounded-theorem closure. It is **not** a GR closure on `main`
and it does **not** propose retained or positive-theorem promotion.

**Cited authorities (one-hop deps; cited but not closed in this note):**

- [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md)
  (`claim_type: bounded_theorem`) — anomaly-forced single-time-direction
  result. This note imports its `d_t = 1` conclusion as a kinematic input
  to the background candidate.
- [`S3_BOUNDARY_LINK_THEOREM_NOTE.md`](S3_BOUNDARY_LINK_THEOREM_NOTE.md)
  (`claim_type: bounded_theorem`, `audit_status: audited_clean`,
  `effective_status: retained_bounded`) —
  PL boundary-link disk theorem on `B_R`, supports the `PL S^3` compactification
  family. (Tier corrected 2026-05-17: prior wording said
  `positive_theorem` / `audited_conditional`; ledger has it at
  `audited_clean` / `retained_bounded` as of the current snapshot. See
  fix-record note linked below.)
- [`S3_CAP_UNIQUENESS_NOTE.md`](S3_CAP_UNIQUENESS_NOTE.md)
  (`claim_type: bounded_theorem`, `audit_status: audited_conditional`) —
  PL cap-uniqueness, supports the `PL S^3` compactification family.

**Admission inheritance from `ANOMALY_FORCES_TIME_THEOREM` (2026-05-17):**

Because this note imports the `d_t = 1` conclusion from
[`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md) as a
single kinematic input, it inherits the full upstream admission structure
on which that conclusion rests:

- **Admissions (ii), (iii), (iv)** are routed to internal companion notes
  on `main`; their final closure is conditional on the audit pipeline's
  independent re-evaluation of those companions.
- **Admission (i)** (ABJ anomaly-to-inconsistency on the lattice) remains
  a bare external admission to the standard ABJ result on current `main`.

Per the recent `F-B` framing-fix on the upstream parent
([`ANOMALY_FORCES_TIME_FB_NOTE_2026-05-17.md`](ANOMALY_FORCES_TIME_FB_NOTE_2026-05-17.md)),
the upstream `d_t = 1` conclusion decomposes as:

- **Derived (Step 3 of the parent):** `d_t` lies in the set of odd
  positives, i.e. `d_t ∈ {1, 3, 5, ...}`.
- **Inherited (admission (iv)):** `d_t > 1` is excluded, collapsing the
  derived set to the single value `d_t = 1`.

This note treats `d_t = 1` as a black-box kinematic input but does not
absorb either upstream substep into itself. Any future sharpening or
revision of admission (iv) propagates directly into the route-2 kinematic
background here and is **not** insulated by this row.

**Admitted-context derivation gap (real, not import-redirect):**

This note explicitly admits there is no in-atlas theorem that turns the
kinematic background `PL S^3 x R` into tensor/metric dynamics. The route is
blocked by the absence of any one of:

1. an exact spacetime-lift observable from the `S^3` + anomaly stack;
2. an exact action whose Euler-Lagrange equations give the GR field law on
   the lifted background;
3. a uniqueness theorem saying the only compatible dynamical lift is the GR
   one.

This is a **real derivation gap**, not a dependency-citation issue. No
retained, bounded, or proposed theorem on the current atlas closes any of
(1)-(3) for this route.

## Verdict (scope-bounded)

**Kinematically clean, dynamically unclosed.**

The current atlas supports a clean axiom-first kinematic background candidate:

- `S^3` topology is supported by the cited PL boundary-link /
  cap-uniqueness theorems. The boundary-link is `audited_clean` (effective
  `retained_bounded`); the cap-uniqueness is `audited_conditional` (not
  retained-grade). The composite `S^3` support inherits the weaker of the
  two tiers (`audited_conditional`);
- anomaly-forced time is supported by the cited `ANOMALY_FORCES_TIME_THEOREM`
  (bounded_theorem).

Their composition gives the kinematic background candidate

    PL S^3 x R.

The atlas does **not** contain an exact theorem that turns that background
into tensor/metric dynamics. In particular:

- no exact `S^3`-to-curvature law is present;
- no exact anomaly-to-Einstein-field-equation derivation is present;
- no exact discrete variational action is present for this route.

So route 2 is not a full-GR proof path yet. It is a clean kinematic
background candidate with a precise, named, currently-open dynamics theorem.

## What the route would need

The route becomes theorem-grade only if one can derive at least one of:

1. an exact spacetime-lift observable from the `S^3` + anomaly stack
2. an exact action whose Euler-Lagrange equations give the GR field law on
   the lifted background
3. a uniqueness theorem saying the only compatible dynamical lift is the GR
   one

Without one of those, the route remains a background theorem, not a full
gravity closure theorem.

## Route 2 in context

The current `FULL_GR_AXIOM_FIRST_PATHS_NOTE.md` survey treats this as one of
the top three alternatives because it uses only retained topology and
chirality/time tools. That is still correct.

But the route is now sharper than the survey wording alone suggests:

- `S^3` is `retained_bounded` (boundary-link) and `audited_conditional`
  (cap-uniqueness); reusable at the weaker (`audited_conditional`) tier of
  the composite.
- anomaly-forced time is `bounded_theorem` with named admissions
  (i)-(iv) (see "Admission inheritance" remark above); reusable at the
  bounded tier modulo those admissions, not as an unconditional exact
  result.
- the combined lift `PL S^3 x R` is the right kinematic target at the
  bounded tier inherited from its upstream authorities, not at an "exact"
  tier.
- the missing piece is a genuine dynamical bridge.

(Phrasing corrected 2026-05-17: the earlier wording "`S^3` is exact and
reusable / anomaly-forced time is exact and reusable" overstated the
upstream tier of both citations and was inconsistent with the
audit-boundary section above. See fix-record note linked below.)

## Full 10-route survey

Against the current atlas and axioms, the 10 candidate architectures are:

1. Exact support-side tensor observable on `A1 x {E_x, T1x}`.
2. Exact support-side Schur / Dirichlet tensor action.
3. Axiom-first spacetime lift from `S^3` and anomaly-forced time.
4. Observable-principle effective-action route.
5. Gauge-matter-first backreaction route.
6. Exact finite-rank source-to-metric theorem.
7. Direct lattice Green / resolvent route to the full metric.
8. Discrete 4D variational action route.
9. Geometric RG / projective-shape flow route.
10. Obstruction-first theorem with a minimal new primitive.

The current ranking still stands:

1. support-side tensor observable
2. `S^3` + anomaly-forced-time spacetime lift
3. exact finite-rank source-to-metric theorem

## Runner result

Primary runner:
[`scripts/frontier_s3_anomaly_spacetime_lift.py`](../scripts/frontier_s3_anomaly_spacetime_lift.py)
(`PASS=8 FAIL=0` after the 2026-06-20 open-gate verifier repair).
The runner does not attempt a GR closure. It checks that this note is still
scoped as a kinematic `open_gate` route survey, verifies the cited
topology/time ingredients and their current bounded/conditional source tiers,
preserves the upstream `S^3` non-overclaim and anomaly-admission inheritance,
and confirms that the missing dynamics bridge remains explicitly open.

The route ingredients live on the cited upstream authorities and are
individually audited there:

- PL `S^3` compactification — cited from
  [`S3_BOUNDARY_LINK_THEOREM_NOTE.md`](S3_BOUNDARY_LINK_THEOREM_NOTE.md)
  (`audited_clean`, effective `retained_bounded`) and
  [`S3_CAP_UNIQUENESS_NOTE.md`](S3_CAP_UNIQUENESS_NOTE.md)
  (`audited_conditional`).
- Anomaly-forced time — cited from
  [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md)
  (`bounded_theorem`).
- The atlas does not yet contain an exact dynamics bridge for this route;
  this is the sharp, currently-open blocker.

## Bottom line

Route 2 is **not** a GR closure on `main`. It is a clean axiom-first
**kinematic** background candidate with a precise, currently-open dynamics
theorem. This row is `open_gate` and remains so until one of the named
dynamics-bridge primitives is constructed and audited on a separate row.

## Fix record (2026-05-17, downstream surgical-fix wave)

Three hostile-audit-grade issues were patched on this note:

- **F-A (stale tier citation):** `S3_BOUNDARY_LINK_THEOREM_NOTE.md` was
  cited as `audited_conditional` / `positive_theorem`; the ledger has it
  at `audited_clean` / `retained_bounded` / `bounded_theorem`. Corrected
  inline above.
- **F-B (over-claim of "exact"):** the "Route 2 in context" bullets
  previously asserted `S^3` and anomaly-forced time were "exact and
  reusable", which over-stated the upstream tiers (`audited_conditional`
  composite for `S^3`; `bounded_theorem` with admissions (i)-(iv) for
  anomaly-forced time) and was inconsistent with the audit-boundary
  section. Corrected inline above.
- **F-C (missing admission-inheritance disclosure):** the note imports
  the `d_t = 1` conclusion as a kinematic input without acknowledging
  that the upstream parent's `F-B` framing-fix decomposes that
  conclusion into a derived part (`d_t ∈ {1, 3, 5, ...}` from Step 3 of
  the parent) and an inherited part (admission (iv): `d_t > 1`
  excluded). Now explicit in the "Admission inheritance" remark above.

See companion fix-record:
`S3_ANOMALY_SPACETIME_LIFT_NOTE_2026-05-17.md`.

Paired verifier:
`scripts/frontier_s3_anomaly_spacetime_lift_downstream_fix.py`.

None of these edits change the open-route survey character or the
`open_gate` claim type. They make the upstream-tier accounting honest and
disclose the inherited admission structure to downstream readers.
