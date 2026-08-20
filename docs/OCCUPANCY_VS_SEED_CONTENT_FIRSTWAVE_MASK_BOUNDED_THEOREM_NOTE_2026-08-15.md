---
claim_id: occupancy_vs_seed_content_firstwave_mask_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "First-wave 6-masks and k=1 reverse/face under occupancy vs seed-content formation-tick on B_3(0) are compared. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/occupancy_vs_seed_content_firstwave_mask_2026_08_15.py
---

# Occupancy Versus Seed-Content First-Wave Masks On The Six-Neighbor Star

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** first-wave 6-masks on the origin-plus-six-NN host, and k=1
reverse/face bits of formation-tick on `B_3(0)`, compared under occupancy
versus a named seed-content nearest-neighbor rule.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/occupancy_vs_seed_content_firstwave_mask_2026_08_15.py`](../scripts/occupancy_vs_seed_content_firstwave_mask_2026_08_15.py)

Displayed, not adopted. Do not attach L1. Do not write into Admissibility.
Uniqueness not required.

## Result up front

The scoring register is formation-tick, not a hop-cost table. A site forms at
the first tick its displayed rule allows from already-formed 6-NN sites.
Synchronous wavefront only; no Dijkstra.

Seed: the origin is occupied and locked with the named rank-1 letter `+`.
That letter is displayed as the outward axis `+e1`. It is not fed into the
occupancy count `n`.

Occupancy (displayed L1 rule, as in the l1chi occupancy form): `n=d/3` with
`d` the number of already-formed nearest neighbors, and a vacant site forms
iff `n≠0`.

Content-NN (displayed, not adopted): the occupancy gate, and in addition the
seed letter `+` must match the outward step from some already-formed neighbor.

**Theorem 1.** On the seven-site host `{0} ∪ {±e1,±e2,±e3}`, ordered
`(+e1,-e1,+e2,-e2,+e3,-e3)`, the tick-1 masks are

```text
occupancy 6-mask = (1, 1, 1, 1, 1, 1)
content 6-mask   = (1, 0, 0, 0, 0, 0)
```

They do not agree.

**Theorem 2.** Under occupancy formation-tick on `B_3(0)={x in Z^3 : |x|_1 ≤ 3}`:

```text
t(0)=0,  t(1,0,0)=1,  t(1,1,1)=3,  t(2,0,0)=2,  t(1,1,0)=2
3 t(1,0,0)^2 > t(1,1,1)^2   is false
t(2,0,0)^2 > 2 t(1,1,0)^2   is false
```

**Theorem 3.** Under content formation-tick on the same `B_3(0)`:

```text
t(0)=0,  t(1,0,0)=1,  t(2,0,0)=2
t(1,1,1) and t(1,1,0) are unformed
```

Both reverse and face bits are undefined. They do not agree with the occupancy
pair `(false, false)`.

claim_scope: First-wave 6-masks and k=1 reverse/face under occupancy vs
seed-content formation-tick on B_3(0) are compared. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite masks and formation-tick bits on a declared seven-site star and on B_3(0); the two rules are displayed comparison objects, not adopted formation laws."
trace_class: frontier_discovery
target_claim_id: occupancy_vs_seed_content_firstwave_mask
target_blocker_text: "compare occupancy n≠0 first-wave 6-masks against a named seed-content NN under formation-tick, without attaching L1"
source_of_blocker_text: handoff
reachability_to_target: compares
artifact_role: theorem
next_trace_action: "keep the comparison displayed; do not attach L1 or write the content-NN rule into Admissibility"
conditional_surface_status: "exact only for the displayed occupancy and seed-content rules on the seven-site mask host and B_3(0)"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premise boundary

[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
`Z^3` with nearest-neighbor adjacency, one covariant Admissibility rule for
the local possibility distribution, and Record occurrence:

```text
Records form.

When present, a record locks exactly one admissible local possibility.
```

Admissibility types a distribution over possibilities, conditional on
formation at a site, and does not supply the formation site, probability, or
rate. The occupancy `n=d/3` rule and the seed-content outward-axis gate are
therefore displayed comparison rules. They are not Admissibility clauses and
are not attached as L1.

The seed letter `+` is a named locked content at the origin. Occupancy `d`
counts formed neighbors and does not read that letter.

## Exact objects

Let `NN = (+e1,-e1,+e2,-e2,+e3,-e3)`. The mask host is the origin plus those
six neighbors (seven sites). `B_3(0)` is the integer L1 ball of radius 3.
Formation-tick is scored only on that ball.

At tick 0 the origin is formed. At later ticks, every vacant site in the host
is tested against already-formed sites only. All currently allowed sites form
together.

Occupancy allows a vacant site iff `n=d/3 ≠ 0`, i.e. iff at least one neighbor
is already formed. Content-NN allows it iff occupancy allows it and some
already-formed neighbor `y` satisfies `x-y = +e1`.

k=1 reverse uses `(1,0,0)` and `(1,1,1)`. k=1 face uses `(2,0,0)` and
`(1,1,0)`. A bit is undefined when a required site never forms.

## Negative scope

The comparison does not select a physical formation law, clock, or content
rule. It does not attach L1 occupancy to Admissibility, does not promote the
named `+` axis, and does not claim uniqueness of either mask. It is not a
hop-cost table and does not dump paths. No axiom edit is proposed.
