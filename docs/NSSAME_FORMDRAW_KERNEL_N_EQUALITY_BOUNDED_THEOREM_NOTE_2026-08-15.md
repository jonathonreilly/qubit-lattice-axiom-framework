---
claim_id: nssame_formdraw_kernel_n_equality_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Formdraw occupancy kernels on the four nssame probes, and whether n(C)=n(D), are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nssame_formdraw_kernel_n_equality_2026_08_15.py
---

# Formdraw Occupancy Kernels On Four Nssame Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** formdraw occupancy kernels `n` at the formation tick of four probes
of the displayed two-site same-lock nssame process. Whether `n(C)=n(D)`, and
whether the four-`n` tuple equals the mixed-lock formdraw occupancy-kernel
display on the same probes, are reported. Uniqueness is not required. No unique
`{+,−}` letter is assigned. Displayed, not adopted. This note does not write
the occupancy kernel into Admissibility and does not attach the occupancy-kernel
formation member.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nssame_formdraw_kernel_n_equality_2026_08_15.py`](../scripts/nssame_formdraw_kernel_n_equality_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Host Euclidean `B_3(0)`. Seed at tick 0: the origin is recorded with lock
`+e_1`, and `(0,1,0)` is recorded with the same lock `+e_1`. Growth is the
perp-step incoming-lock rule. At the formation tick of each probe, occupancy
kernel `n` is read from already-recorded six-neighbor occupancy. The four
kernels are

```text
n(A) = (−1/3, −1/3, 0)
n(B) = (−1/3, 0, 0)
n(C) = (−1/3, 0, 0)
n(D) = (−1/3, 1/3, 0)
```

So `n(C) ≠ n(D)`. The four-`n` tuple is not the mixed-lock formdraw occupancy
kernel on the same probes. The unique `f(n)` leftover closed there because
`n(C)=n(D)` does not transfer. No unique letter is assigned here.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact formdraw occupancy kernels on the four nssame probes, with n(C)=n(D) reported false and the mixed-lock four-n tuple reported unequal."
trace_class: frontier_discovery
target_claim_id: nssame_formdraw_kernel_n_equality
target_blocker_text: "display formdraw occupancy kernels on the four nssame probes and whether n(C)=n(D)"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded occupancy-kernel report"
conditional_surface_status: "exact on B_3(0) for occupancy kernels on the four nssame probes; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Displayed process

Write `e_1=(1,0,0)`, `e_2=(0,1,0)`, and `e_3=(0,0,1)`. The six nearest-neighbor
steps are

```text
NN = {+e_1,-e_1,+e_2,-e_2,+e_3,-e_3}.
```

The finite host is the closed Euclidean ball of radius 3 centered at the
origin,

```text
B_3(0) = { n in Z^3 : n·n <= 9 }.
```

No larger host is used. The four probes are the only sites whose occupancy
kernel is scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

Seed, at tick 0:

```text
t(0) = 0,     L(0) = +e_1,
t(0,1,0) = 0, L(0,1,0) = +e_1.
```

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept as a
possible lock. Uniqueness is not required. A later parent does not re-form
`q`.

That incoming lock is not occupancy `n`. This same-lock seed is outside the
proper cubic orbit of the mixed-lock two-site seed with letters `+e_1` and
`+e_2`.

## Named occupancy kernel

At the formation tick of a probe, occupancy is read from already-recorded
sites only: a neighbor is occupied if and only if it formed strictly earlier.
The probe itself is still unread. Occupancy is in `{0,1}`.

The named formdraw occupancy kernel is the triple

```text
n_μ = (o_{+μ} − o_{−μ}) / 3,     μ = 1,2,3.
```

This note reads `n` at each probe's formation tick as displayed theorem-domain
data. It does not attach the occupancy-kernel formation member: sites form by
the nssame perp-step incoming-lock process, not by an `n ≠ 0` formation rule.
No unique `{+,−}` letter is assigned from `n`.

The occupancy kernel is displayed, not adopted. It is not written into
Admissibility.

## Theorem 1 — occupancy kernel at each probe

Direct enumeration of the displayed nssame process on `B_3(0)` forms all four
probes. At each formation tick the occupancy kernel from already-recorded
six-neighbor occupancy is

```text
n(A) = (−1/3, −1/3, 0)
n(B) = (−1/3, 0, 0)
n(C) = (−1/3, 0, 0)
n(D) = (−1/3, 1/3, 0)
```

Neighbor occupancies at those formation ticks:

- `A`: already recorded on `−e_1`, `−e_2`, `+e_3`, and `−e_3`;
- `B`: already recorded on `−e_1`;
- `C`: already recorded on `−e_1`;
- `D`: already recorded on `−e_1`, `+e_2`, `+e_3`, and `−e_3`.

Incoming locks exist and need not be unique. That non-uniqueness is not a
lettering. Uniqueness is not required.

## Theorem 2 — `n(C)` and `n(D)`

The kernels of Theorem 1 give `n(C) = (−1/3, 0, 0)` and
`n(D) = (−1/3, 1/3, 0)`. Componentwise comparison yields `n(C) ≠ n(D)`.

## Theorem 3 — mixed-lock formdraw four-`n` tuple

The mixed-lock two-site process with `L(0)=+e_1` and `L(0,1,0)=+e_2`, on the
same host and the same four probes, with the same formdraw occupancy kernel,
displays

```text
n(A) = (−1/3, 1/3, 0)
n(B) = (−1/3, 0, −1/3)
n(C) = (−1/3, 0, 0)
n(D) = (−1/3, 0, 0)
```

That four-`n` tuple is not the nssame tuple of Theorem 1. On the mixed-lock
display, `n(C)=n(D)`, which closed a unique `f(n)` leftover. That leftover
does not transfer: here `n(C) ≠ n(D)`. No unique `f(n)` is constructed.

The mixed-lock display is a contrast, not a parent theorem.

## Inputs And Import Boundary

- **Framework dependency:** Lattice supplies the cubic nearest-neighbor
  geometry of `Z^3`. Record supplies permanence and single-site locking
  vocabulary. Both are quoted without rewrite.
- **Explicit theorem-domain condition:** the host is the Euclidean ball
  `B_3(0)={n∈Z^3:n·n≤9}` only. The same-lock seed, the perp-step incoming-lock
  rule, the formdraw occupancy kernel, and the four probes are supplied data
  for this display.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** adopting occupancy `n` as an Admissibility
  constraint or a formation law remains a separate obligation. This note does
  not attach that bridge.

## What This Does Not Claim

- No unique `{+,−}` letter is assigned from `n`.
- Occupancy-kernel letters are not written into Admissibility.
- The display is not written into Admissibility.
- The occupancy-kernel formation member is not attached.
- Incoming-step uniqueness is not required and is not proved.
- The mixed-lock four-`n` tuple is a contrast, not a parent.
- No continuum limit and no comparison beyond the four probes on this host
  is claimed.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site.

> When present, a record locks exactly one admissible local possibility.

> A site with no record cannot be read.

Their dependency role is limited to cubic nearest-neighbor geometry and
lock/permanence vocabulary. This theorem separately supplies the Euclidean
host, the two-site same-lock seed, the perp-step protocol, and the formdraw
occupancy kernel. Readout of unrecorded sites remains outside the target: the
four probes are recorded before `n` is read at neighboring unread sites.

## Runner Contract

The companion runner enumerates `B_3(0)` by `n·n≤9`, grows by simultaneous
tick under the perp-step incoming-lock rule, and computes the formdraw
occupancy kernel `n` from already-recorded six-neighbor occupancy at each
probe's formation tick. It reports the four kernels, checks `n(C)≠n(D)`, and
compares the four-`n` tuple to the mixed-lock formdraw kernels on the same
probes. It pins the declared review inputs to this note and the axiom memo
only. No runner cache is written.
