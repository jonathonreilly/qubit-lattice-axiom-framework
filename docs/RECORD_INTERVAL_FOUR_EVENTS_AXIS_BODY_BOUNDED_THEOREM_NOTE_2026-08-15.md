---
claim_id: record_interval_four_events_axis_body_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Interval s^2=t_lock^2-|x|_2^2 on four named recorded events, and axis vs body class, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/record_interval_four_events_axis_body_2026_08_15.py
---

# Record Interval On Four Named Events: Axis Versus Body Class

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact display of `s^2=t_lock^2-|x|_2^2` on one named recorded
set of four events, and the space/null/time class of the axis event versus
the body event. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/record_interval_four_events_axis_body_2026_08_15.py`](../scripts/record_interval_four_events_axis_body_2026_08_15.py)

## Result Up Front

Let the recorded set be

```text
R = {(0,0,0), (1,0,0), (1,1,0), (1,1,1)}.
```

Current Record in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
makes only records readable. The interval below is therefore evaluated only
on `R`. Unread sites are not scored and are not a reverse map.

The named lock order, displayed rather than derived as unique, is

```text
t_lock(0,0,0) = 0,
t_lock(1,0,0) = 1,
t_lock(1,1,0) = 2,
t_lock(1,1,1) = 3.
```

Clock is this lock order. Spatial quadratic is the Euclidean square

```text
Q(x) = x·x = |x|_2^2.
```

This display does not attach L1. No hop-cost is used.

The interval on events in `R` is

```text
s^2(x) = t_lock(x)^2 - Q(x).
```

Sign class: space if `s^2<0`, null if `s^2=0`, time if `s^2>0`.

On this named display the four values are

| event | role | `t_lock` | `Q` | `s^2` | class |
|---|---|---:|---:|---:|---|
| `(0,0,0)` | origin | `0` | `0` | `0` | null |
| `(1,0,0)` | axis | `1` | `1` | `0` | null |
| `(1,1,0)` | face | `2` | `2` | `2` | time |
| `(1,1,1)` | body | `3` | `3` | `6` | time |

The axis event is null. The body event is time. They do not lie in the same
class. That comparison is reported. Displayed, not adopted. The note does not write a metric into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Q and s^2 are exact on the four named recorded events; axis is null and body is time on this displayed lock order. Uniqueness of the order, a physical time metric, and adoption into Admissibility remain outside the claim."
trace_class: upstream_support
target_claim_id: physical_lorentzian_clock_map
target_blocker_text: "construct a physical clock and interval on recorded events without writing a metric into Admissibility"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the interval displayed on the recorded set with lock-order clock and Euclidean square; do not attach L1 or score unread sites."
conditional_surface_status: "exact for the named four-event recorded set and named lock order; not adopted as a metric or uniqueness theorem"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premise Boundary

The current Record axiom supplies formation, one locked admissible
possibility per present record, content-only readout, and unreadability at
absence. It does not supply a scalar collection functional, a value at an
unread site, a uniqueness theorem for lock order, or a spacetime metric.

The current Admissibility axiom supplies one fixed nearest-neighbor
probability rule, covariant under lattice translations and proper cubic
rotations. It does not define a time metric. This display therefore cannot
be written into Admissibility.

The four sites of `R` are ordinary points of `Z^3`. Occupancy of those four
sites by records, and the integers `t_lock`, are named display data. They
are not selected by a formation process, hop length, or shortest-path fill.

## Exact Objects

Let `R` be as above. Let `t_lock:R -> {0,1,2,3}` be the named bijection
displayed in the result section. Define

```text
Q:R -> Z,     Q(x) = x_1^2 + x_2^2 + x_3^2,
s^2:R -> Z,   s^2(x) = t_lock(x)^2 - Q(x).
```

The axis event is `(1,0,0)`. The body event is `(1,1,1)`. The score domain is exactly `R`.

## Theorem 1 — Quadratic And Interval On The Four Events

Direct evaluation of `Q` from coordinates gives

```text
Q(0,0,0) = 0,
Q(1,0,0) = 1,
Q(1,1,0) = 2,
Q(1,1,1) = 3.
```

With the named lock order,

```text
s^2(0,0,0) = 0^2 - 0 = 0,
s^2(1,0,0) = 1^2 - 1 = 0,
s^2(1,1,0) = 2^2 - 2 = 2,
s^2(1,1,1) = 3^2 - 3 = 6.
```

Sign classes are therefore null, null, time, time.

## Theorem 2 — Axis Versus Body Class

The axis event `(1,0,0)` has `s^2=0`, hence null class.

The body event `(1,1,1)` has `s^2=6>0`, hence time class.

## Theorem 3 — Same-Class Comparison

Null is not time. Axis and body therefore do not lie in the same class on
this named display.

The comparison is reported. It is displayed, not adopted. It does not select
a physical metric, write an interval into Admissibility, or claim that every
lock order on `R` yields the same classes.

## Mutations That Stay Outside The Claim

On these four `{0,1}`-coordinate events the coordinate L1 length equals
`Q`. That numerical coincidence is not a license to attach L1. The
definition used here remains the Euclidean square.

A different bijection `R -> {0,1,2,3}` can change classes. The lock order
with `t_lock(1,0,0)=2` and the other three values held fixed makes the axis
event time as well, so uniqueness of lock order is not required and is not
claimed.

The unread site `(2,0,0)` is not in `R`. Current Record assigns it no
readout. It is not scored and is not used as a reverse map.

## Imports And Claim Boundary

| Item | Role | Provenance / status |
|---|---|---|
| Record unreadability at absence | score domain is `R` only | current axiom memo |
| Admissibility does not define a time metric | forbids writing the display into Admissibility | current axiom memo |
| `R` and named `t_lock` | displayed recorded events and clock | named mathematical input |
| `Q=|x|_2^2` | spatial quadratic | declared Euclidean square |
| `s^2=t_lock^2-Q` | interval | declared combination on `R` |
| space/null/time by sign of `s^2` | class labels | declared sign rule |

There are no measured, fitted, literature, or observational inputs. No
physical time metric is selected. No uniqueness theorem is claimed.

## Primary Runner

The paired runner computes `Q` and `s^2` from the named events and lock
order, classifies axis versus body, checks that unread sites are not scored,
checks that a mutated lock order can change the same-class answer, and pins
the current Record/Admissibility boundary together with the displayed-not-adopted
scope of the note.
