---
claim_id: perpnn_tick_interval_vs_recint_four_events_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Interval s^2 under perpnn formation-ticks on four named recorded events, versus recint axis/body classes, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/perpnn_tick_interval_vs_recint_four_events_2026_08_15.py
---

# Perpnn Formation-Tick Interval Versus Recint Classes On Four Events

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact display of `s^2=t^2-|x|_2^2` on one named recorded set of
four events under displayed perpnn formation-ticks, and the axis versus body
space/null/time class compared with the displayed recint classes. Displayed,
not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/perpnn_tick_interval_vs_recint_four_events_2026_08_15.py`](../scripts/perpnn_tick_interval_vs_recint_four_events_2026_08_15.py)

## Result Up Front

Let the recorded set be

```text
R = {(0,0,0), (1,0,0), (1,1,0), (1,1,1)}.
```

Current Record in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
makes only records readable. The interval below is therefore evaluated only
on `R`. Unread sites are not scored.

The perpnn formation-ticks on these four events are displayed, not recomputed by path dump:

```text
t(0,0,0) = 0,
t(1,0,0) = 3,
t(1,1,0) = 2,
t(1,1,1) = 3.
```

Spatial quadratic is the Euclidean square

```text
Q(x) = |x|_2^2.
```

This display does not attach L1. It is not a second occupancy lock-order
table.

The interval on events in `R` is

```text
s^2(x) = t(x)^2 - Q(x).
```

Sign class: space if `s^2<0`, null if `s^2=0`, time if `s^2>0`.

On this named display the four values are

| event | role | `t` | `Q` | `s^2` | class |
|---|---|---:|---:|---:|---|
| `(0,0,0)` | origin | `0` | `0` | `0` | null |
| `(1,0,0)` | axis | `3` | `1` | `8` | time |
| `(1,1,0)` | face | `2` | `2` | `2` | time |
| `(1,1,1)` | body | `3` | `3` | `6` | time |

The axis event is time. The body event is time.

The displayed recint classes on the same four events are axis null and body
time. Axis therefore disagrees with recint. Body agrees with recint. The
axis/body class pair does not agree with recint. That comparison is reported.
Displayed, not adopted. The note does not write a metric into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Q and s^2 are exact on the four named recorded events under displayed perpnn ticks; axis is time and body is time. Recint reports axis null and body time. Uniqueness of the ticks, a physical time metric, and adoption into Admissibility remain outside the claim."
trace_class: upstream_support
target_claim_id: physical_lorentzian_clock_map
target_blocker_text: "construct a physical clock and interval on recorded events without writing a metric into Admissibility"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the interval displayed on the recorded set with displayed perpnn formation-ticks and Euclidean square; do not attach L1, do not reprint occupancy lock-order, and do not recompute ticks by path dump."
conditional_surface_status: "exact for the named four-event recorded set and named perpnn ticks versus displayed recint classes; not adopted as a metric or uniqueness theorem"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premise Boundary

The current Record axiom supplies formation, one locked admissible
possibility per present record, content-only readout, and unreadability at
absence. It does not supply a scalar collection functional, a uniqueness
theorem for formation ticks, or a spacetime metric.

The current Admissibility axiom supplies one fixed nearest-neighbor
probability rule, covariant under lattice translations and proper cubic
rotations. It does not define a time metric. This display therefore cannot
be written into Admissibility.

The four sites of `R` are ordinary points of `Z^3`. The integers `t` are
named display data. They are not recomputed here by path dump.

## Exact Objects

Let `R` be as above. Let `t:R -> {0,2,3}` be the named map displayed in the
result section. Define

```text
Q:R -> Z,     Q(x) = x_1^2 + x_2^2 + x_3^2,
s^2:R -> Z,   s^2(x) = t(x)^2 - Q(x).
```

The axis event is `(1,0,0)`. The body event is `(1,1,1)`. The score domain is exactly `R`.

The displayed recint classes used for comparison, and not recomputed here, are

```text
recint axis class = null,
recint body class = time.
```

Those two labels are the comparison target. This note does not reprint the
occupancy lock-order table that produced them.

## Theorem 1 — Quadratic And Interval Under Perpnn Ticks

Direct evaluation of `Q` from coordinates gives

```text
Q(0,0,0) = 0,
Q(1,0,0) = 1,
Q(1,1,0) = 2,
Q(1,1,1) = 3.
```

With the named perpnn ticks,

```text
s^2(0,0,0) = 0^2 - 0 = 0,
s^2(1,0,0) = 3^2 - 1 = 8,
s^2(1,1,0) = 2^2 - 2 = 2,
s^2(1,1,1) = 3^2 - 3 = 6.
```

Sign classes are therefore null, time, time, time.

## Theorem 2 — Axis Versus Body Class

The axis event `(1,0,0)` has `s^2=8>0`, hence time class.

The body event `(1,1,1)` has `s^2=6>0`, hence time class.

## Theorem 3 — Comparison With Recint Classes

Recint reports axis null and body time.

Time is not null, so the axis class under perpnn ticks disagrees with recint.

Both reports assign time to the body event, so the body class agrees with
recint.

The axis/body class pair therefore does not agree with recint.

The comparison is reported. It is displayed, not adopted. It does not select
a physical metric, write an interval into Admissibility, claim uniqueness of
the ticks, or reprint occupancy lock-order.

## Mutations That Stay Outside The Claim

On these four `{0,1}`-coordinate events the coordinate L1 length equals
`Q`. That numerical coincidence is not a license to attach L1. The
definition used here remains the Euclidean square.

A different assignment of ticks on `R` can change classes. Replacing only
`t(1,0,0)` by `1` makes the axis event null, matching the recint axis class.
Uniqueness of the displayed ticks is not required and is not claimed.

The four events are the whole score. No further site is scored.

## Imports And Claim Boundary

| Item | Role | Provenance / status |
|---|---|---|
| Record unreadability at absence | score domain is `R` only | current axiom memo |
| Admissibility does not define a time metric | forbids writing the display into Admissibility | current axiom memo |
| `R` and named perpnn ticks | displayed recorded events and clock | named mathematical input |
| recint axis null, body time | comparison labels | named displayed classes |
| `Q=|x|_2^2` | spatial quadratic | declared Euclidean square |
| `s^2=t^2-Q` | interval | declared combination on `R` |
| space/null/time by sign of `s^2` | class labels | declared sign rule |

There are no measured, fitted, literature, or observational inputs. No
physical time metric is selected. No uniqueness theorem is claimed.

## Primary Runner

The paired runner computes `Q` and `s^2` from the named events and displayed
perpnn ticks, classifies axis versus body, compares those classes with the
displayed recint labels, checks that L1 is not attached, checks that a mutated
tick can change the axis class, and pins the current Record/Admissibility
boundary together with the displayed-not-adopted scope of the note.
