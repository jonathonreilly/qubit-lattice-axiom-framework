---
claim_id: opposite_lock_yprobe_sametick_formdraw_kernel_split_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-tick-inclusive formdraw occupancy kernel n on the four opposite-lock y-probes, equality of n(C) and n(D), and reverse/face from the unique splitting-component letter when they disagree (else UNDEFINED), are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_yprobe_sametick_formdraw_kernel_split_reverse_face_2026_08_15.py
---

# Same-Tick Formdraw Occupancy Kernel On Opposite-Lock Y-Probes: Splitting-Component Letter, Reverse, And Face

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** same-tick-inclusive formdraw occupancy kernel `n` at the formation
tick of the four opposite-lock y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)` of the displayed opposite-lock two-site process. Occupancy of a
six-neighbor `p` of probe `q` is 1 iff `p` formed at tick ≤ `t(q)` and
`p≠q`; the same-tick partner counts and the probe itself is excluded.
`A` is a seed. Whether `n(C)=n(D)` is reported. If they disagree, `μ*` is
the first axis in `(e_1,e_2,e_3)` with `n(C)_{μ*} ≠ n(D)_{μ*}`, and the
unique letter at probe `q` is `sign(n(q)_{μ*})` in `{+,−}` when that
component is nonzero, else `UNDEFINED`. Reverse holds iff `L(A)=+` and
`L(B)=−`. Face holds iff `L(C)=+` and `L(D)=−`. If `n(C)=n(D)`, that unique
letter is not assigned and reverse and face are `UNDEFINED`; the report
would stop after Theorem 1. Uniqueness of incoming locks is not required.
This is not unique `P_+`. This is not nscodot. This is not leftover of the
strictly-earlier occupancy kernel on these same four opposite-lock
y-probes. This is not leftover of the strictly-earlier formdraw
occupancy-kernel split on these same y-probes. This is not leftover of
already-recorded six-neighbor lock lists. This is not leftover of the four
y-probe neighbor-lock lists on this seed. This is not the x-probe
same-tick formdraw occupancy-kernel split on this same process. Displayed,
not adopted. This note does not write the kernel or the letter into
Admissibility, does not feed a letter into occupancy `n`, and does not
attach the occupancy-kernel formation member.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_yprobe_sametick_formdraw_kernel_split_reverse_face_2026_08_15.py`](../scripts/opposite_lock_yprobe_sametick_formdraw_kernel_split_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. The unique splitting-component letter, when assigned, is a sign in
`{+,−}`. Those two alphabets are not identified.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of same-tick-inclusive formdraw occupancy-kernel n on the four opposite-lock y-probes, with n(C)≠n(D), unique splitting-component letters UNDEFINED, −, UNDEFINED, −, and reverse/face UNDEFINED; uniqueness is not claimed and the kernel is not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_yprobe_sametick_formdraw_kernel_split_reverse_face
target_blocker_text: "display same-tick-inclusive formdraw occupancy kernel n on the four opposite-lock y-probes, whether n(C)=n(D), and reverse/face from the unique splitting-component letter or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep n, the disagreement n(C)≠n(D), the unique splitting-component letters, and UNDEFINED reverse/face displayed; do not write the kernel into Admissibility, do not pick a unique P_+, and do not attach the occupancy-kernel formation member."
conditional_surface_status: "exact on B_3(0) for same-tick-inclusive occupancy-kernel n on the four opposite-lock y-probes; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose occupancy
kernel is scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`,
`C=(0,0,2)`, `D=(0,1,1)`. `A` is a seed.

Formation ticks of those y-probe sites locate the formed-at-or-before
six-neighbor set. The ticks are not occupancy kernels and are not the
reverse/face scoring.

Lock alphabet of the displayed process: `{±e_1, ±e_2, ±e_3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_1` and `L(0,1,0)=−e_1`.

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

That incoming lock is not occupancy `n` and is not the unique splitting-component
letter.

Both seed locks lie on the `e_1` axis, so the allowed-step plane at each seed
site is the span of `{e_2,e_3}`. Formation ticks of the four y-probes are
`t(A)=0` and `t(B)=2`, with `t(C)=1` and `t(D)=3`. Reverse and face are not
scored from those ticks.

The opposite pair `+e_1/−e_1` is not a proper cubic image of the perp pair
`+e_1/+e_2`. This display is not the cubic orbit of that perp two-site seed.

## Named occupancy kernel and unique splitting-component letter

At the formation tick of a y-probe `q`, occupancy of a six-neighbor `p` is 1
iff `p` formed at tick ≤ t(q) and p≠q. The same-tick partner counts. The
probe itself is excluded even though it is formed. Occupancy is in `{0,1}`
and does not depend on any later letter. Occupancy at a seed tick is
formed-at-or-before: the same-tick partner at the origin is occupied.

This is not the strictly-earlier leftover: a neighbor formed at the same tick
as `q` is occupied here and is empty under strictly-earlier occupancy.

The named formdraw occupancy kernel is the triple

```text
n_μ = (o_{+μ} − o_{−μ}) / 3,     μ = 1,2,3.
```

If `n(C)=n(D)`, there is no splitting component. The unique letter is not
assigned. Reverse and face are `UNDEFINED`. The report stops after Theorem 1:
no axis `μ*` is selected.

If `n(C)≠n(D)`, let `μ*` be the first axis in `(e_1,e_2,e_3)` with
`n(C)_{μ*} ≠ n(D)_{μ*}`. The unique letter at probe `q` is

```text
+  iff  n(q)_{μ*} > 0,
−  iff  n(q)_{μ*} < 0,
UNDEFINED  iff  n(q)_{μ*} = 0.
```

Reverse and face (displayed, only when the unique letter is assigned):

```text
reverse  <=>  L(A)=+ and L(B)=−
face     <=>  L(C)=+ and L(D)=−
```

If a letter needed by a comparison is `UNDEFINED`, that comparison is
`UNDEFINED`. If both letters are defined and the predicate holds, the
comparison is `hold`. If both letters are defined and the predicate fails,
the comparison is `fail`. The report is one of `hold`, `fail`, or
`UNDEFINED`.

This is not unique `P_+`: it does not assign `+` whenever `n≠0`. This is not
nscodot: it does not assign a unique letter by an occupancy-kernel inner
product. This is not leftover of the strictly-earlier occupancy kernel on
these same four opposite-lock y-probes: that leftover reports a different
four-tuple of kernels. This is not leftover of the strictly-earlier formdraw
occupancy-kernel split on these same y-probes. This is not leftover of
already-recorded six-neighbor lock lists: the unique letter is not the
singleton lock vector of those neighbors. This is not leftover of the four
y-probe neighbor-lock lists on this seed. This is not the x-probe same-tick
formdraw occupancy-kernel split on this same process: those x-probes are
`A=(1,0,0)` and `C=(2,0,0)`, and their first splitting axis is `e_2`.

The letter, when assigned, does not feed `n`. Occupancy of a formed site
remains `1` for either content. This note reads `n` at each y-probe's
formation tick as displayed theorem-domain data. It does not attach the
occupancy-kernel formation member: sites form by the opposite-lock perp-step
incoming-lock process, not by an `n ≠ 0` formation rule.

Incoming `{±e_i}` tags are not that assignment. Identifying a named sign of
an incoming step with the unique letter is refused.

Admissibility is not edited. The kernel and the letter are not written into
Admissibility.

## Theorem 1 — occupancy kernel at each y-probe, and equality of n(C) and n(D)

Direct enumeration of the displayed opposite-lock process on `B_3(0)` forms
all four y-probes. Formation ticks are `t(A)=t(0,1,0)=0`, `t(B)=t(1,1,1)=2`,
`t(C)=t(0,2,0)=1`, `t(D)=t(1,1,0)=3`. Those ticks locate the
formed-at-or-before set. They are not the reverse/face kernel.

At each formation tick the same-tick-inclusive occupancy kernel is

```text
n(A) = (0, −1/3, 0)
n(B) = (−1/3, −1/3, 0)
n(C) = (0, −1/3, 0)
n(D) = (−1/3, 0, 0)
```

Componentwise comparison yields `n(C)≠n(D)`. The first disagreeing axis is
`μ* = e_1`: `n(C)_1 = 0` and `n(D)_1 = −1/3`. The `e_2` components also
disagree, but they are not first. The unique splitting-component letter at
each probe is therefore the sign of the `e_1` component:

```text
L(A) = UNDEFINED
L(B) = −
L(C) = UNDEFINED
L(D) = −
```

`L(A)` and `L(C)` are `UNDEFINED` because those `e_1` components vanish, not
because `n(C)=n(D)`. `A` is a seed: its same-tick six-neighbor set occupies
the origin partner, so `n(A)=(0, −1/3, 0)`.

The strictly-earlier leftover on these same four opposite-lock y-probes
displays `n(A)=(0, 0, 0)`, `n(B)=(−1/3, 0, 0)`, `n(C)=(0, −1/3, 0)`, and
`n(D)=(−1/3, 1/3, 0)`. Same-tick partners change the kernels at `A`, `B`,
and `D`. Probe `C` has no same-tick six-neighbor, so that leftover agrees
with `n(C)` by accident; the named kernel remains same-tick-inclusive. That
leftover is not this kernel.

Neighbor occupancies at those formation ticks:

- `A`: occupied on `−e_2` only, the same-tick seed partner at the origin;
- `B`: occupied on `−e_1` and `−e_2`, including the same-tick neighbor
  `(1,0,1)`;
- `C`: occupied on `−e_2` only (the seed `A`); no same-tick six-neighbor;
- `D`: occupied on `−e_1`, `+e_2`, and `−e_2`; the same-tick neighbor
  `(1,0,0)` cancels `+e_2`; `+e_3` and `−e_3` cancel.

Incoming locks exist and need not be unique (`D` keeps three earliest
incoming steps). That non-uniqueness is not a splitting-component lettering.
Uniqueness is not required.

This four-tuple of kernels is not leftover of the four x-probe same-tick
kernels on the same seed. Shared sites `B` and `D` do not make the y-probe
display a reprint: `n(A)` and `n(C)` differ from those x-probe kernels, and
`μ*` is `e_1` here rather than `e_2`.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if `L(A)=+` and `L(B)=−`. The unique letters are
`L(A)=UNDEFINED` and `L(B)=−`. A needed letter is `UNDEFINED`. Reverse is
`UNDEFINED`.

Reverse: UNDEFINED

This is not `hold` and not `fail`. Unique `P_+` along `n` would score reverse
as fail because every `n ≠ 0` letter is `+`. An nscodot inner product, a
strictly-earlier leftover occupancy kernel, a leftover of already-recorded
six-neighbor lock lists, a leftover of the four y-probe neighbor-lock lists,
a named-sign readout of incoming steps, the x-probe same-tick formdraw
occupancy-kernel split, and a formation-tick inequality are different objects
and are not used.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if `L(C)=+` and `L(D)=−`. The unique letters are
`L(C)=UNDEFINED` and `L(D)=−`. A needed letter is `UNDEFINED`. Face is
`UNDEFINED`.

Face: UNDEFINED

Displayed, not adopted. The letters are not written into Admissibility.

This is not `hold` and not `fail`. Unique `P_+` would score face as fail
because both nonzero kernels would be lettered `+`. Face remains
`UNDEFINED` from `C` alone. Leftover of the four y-probe neighbor-lock lists
on this seed assigned `L(C)=−e_1` as a unique lock vector; that leftover
is not this letter. The x-probe same-tick formdraw occupancy-kernel split on
this same process selected `μ*=e_2` and lettered `C` as `+` and `D` as
`UNDEFINED`. Those are not these y-probes.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not assign a unique splitting-component letter when `n(C)=n(D)`.
- It is not unique `P_+` along `n`.
- It is not nscodot.
- It is not leftover of the strictly-earlier occupancy kernel on these same
  four opposite-lock y-probes.
- It is not leftover of the strictly-earlier formdraw occupancy-kernel split
  on these same y-probes.
- It is not leftover of already-recorded six-neighbor lock lists.
- It is not leftover of the four y-probe neighbor-lock lists on this seed.
- It is not the x-probe same-tick formdraw occupancy-kernel split on this
  same process.
- It does not identify a letter with incoming `{±e_i}`.
- It does not feed a letter into occupancy `n`.
- It does not attach the occupancy-kernel formation member.
- It does not census a sixteen-combination free lettering independent of `n`.
- It does not enlarge the host beyond `B_3(0)`.
- It does not treat the opposite-lock seed as a proper cubic image of the
  perp two-site seed.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not supply a physical rate or a continuum kernel.

## Current premise boundary

The Lattice, Qubit, Admissibility, and Record premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Records form.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

The Admissibility reading note says the distribution concerns which possibility
a forming record locks, conditional on formation at that site; it does not
supply the formation site, probability, or rate.

This display uses Lattice to name `B_3(0)` and the four y-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
opposite-lock two-site process, the same-tick-inclusive occupancy kernel, the
disagreement `n(C)≠n(D)`, the unique splitting-component letter, and the
reverse/face predicates are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; opposite-lock two-site seed `+e_1/−e_1` |
| same-tick-inclusive occupancy kernel `n` at each y-probe | Theorem 1 |
| whether `n(C)=n(D)` | Theorem 1; `n(C)≠n(D)` |
| unique splitting-component letter | Theorem 1; `μ*=e_1`; `UNDEFINED`, `−`, `UNDEFINED`, `−` |
| reverse and face | Theorems 2–3; both `UNDEFINED` |
| unique incoming lock | not required |
| unique `P_+` along `n` | not used |
| nscodot inner product | not used |
| leftover of the strictly-earlier occupancy kernel | not used; same-tick neighbors count |
| leftover of already-recorded six-neighbor lock lists | not used |
| leftover of the four y-probe neighbor-lock lists | not used |
| x-probe same-tick formdraw occupancy-kernel split | different object; not reused |
| letters fed into occupancy `n` | not executed |
| occupancy-kernel formation member attached | not attached |
| kernel or letter as Admissibility content | not adopted |
| cubic orbit of the perp two-site seed | not this seed |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: same-tick-inclusive formdraw occupancy kernel `n` on the four opposite-lock y-probes, whether `n(C)=n(D)`, and reverse/face from the unique splitting-component letter or `UNDEFINED`. |
| V2 | Current main has no landed same-tick-inclusive occupancy-kernel splitting-component reverse/face report on these four opposite-lock y-probes. |
| V3 | Occupancy kernels, the disagreement `n(C)≠n(D)`, the four letters, and the two `UNDEFINED` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads same-tick-inclusive `n` at formation and tests a unique splitting-component letter. |
| V5 | It is not an adopted content rule: the kernel remains displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write the kernel into
Admissibility, does not pick unique `P_+`, and does not score reverse or
face from a vanishing splitting component as hold or fail. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique `P_+` along `n` | assign `+` whenever `n≠0` | refused; different object; would report reverse fail and face fail |
| nscodot inner product | assign a letter from `n·n'` | refused; different object |
| leftover of the strictly-earlier occupancy kernel | occupy only tick `< t(q)` | different kernel at `A`, `B`, and `D`; leftover Theorem 1 reports `n(A)=(0, 0, 0)`, `n(B)=(−1/3, 0, 0)`, `n(C)=(0, −1/3, 0)`, `n(D)=(−1/3, 1/3, 0)` |
| leftover of the strictly-earlier formdraw occupancy-kernel split | copy that leftover four-tuple | refused; same-tick partners change three kernels |
| leftover of already-recorded six-neighbor lock lists | unique lock vector at already-recorded neighbors | refused; that leftover letters `B` as `+e_3` and `C` as `−e_1` |
| leftover of the four y-probe neighbor-lock lists | copy `UNDEFINED`, `+e_3`, `−e_1`, `UNDEFINED` | refused; the splitting-component letters are `UNDEFINED`, `−`, `UNDEFINED`, `−` |
| x-probe same-tick formdraw occupancy-kernel split | copy `μ*=e_2` and letters `UNDEFINED`, `−`, `+`, `UNDEFINED` | refused; these are the y-probes `A=(0,1,0)`, `C=(0,2,0)`; `μ*=e_1` |
| identify letter with named sign of incoming `{±e_i}` | map `+e_i` to `+` | refused; different alphabet |
| reverse/face from formation-tick inequalities | score `t(A)=0` against `t(B)=2` | different object; ticks are not scored |
| free occupancy letters on the four probes | ignore `n` and letter independently | different object; not enumerated |
| attach occupancy-kernel formation member | form the probes by `n ≠ 0` instead of perp-step | refused; not attached |
| feed letters into `n` | let `+`/`−` change occupancy | refused; occupancy stays `{0,1}` of the formed-at-or-before set |
| adopt the kernel into Admissibility | rewrite the local rule by `n` | refused; displayed, not adopted |
| treat this seed as a cubic image of `+e_1/+e_2` | rotate the perp two-site seed onto `+e_1/−e_1` | refused; no proper cubic rotation does so |

Honesty marker for each row: `ATTEMPTED`.

### N2 — wall independence

Missing physical adoption, missing occupancy-kernel formation attachment, and
missing Record identification of a splitting letter are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, opposite-lock two-site seed `+e_1` and `−e_1`,
perpendicular step rule, incoming-step lock, same-tick-inclusive occupancy
kernel, four y-probes, seed `A` at tick 0, equality test `n(C)=n(D)`, unique
splitting-component letter, and reverse/face definitions are declared. No
uniqueness, no occupancy-kernel formation attachment, and no Admissibility
rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`UNDEFINED` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each occupancy component of `n` and the splitting-component letter | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four kernels, one equality test, two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a seed or host on which the splitting component is
nonzero at every needed probe. None is taken here.

### N7 — hostile steelman

**Steelman:** Opposite seed locks should force reverse to hold, same-tick
partners should restore `n(C)=n(D)` as on the leftover perp two-site seed,
unique `P_+` should be used because every kernel is nonzero, leftover of the
four y-probe neighbor-lock lists should be imported, the x-probe same-tick
formdraw split should be reused, or the strictly-earlier leftover occupancy
kernel should be reused because the unique letters happen to match.

**Answer:** Direct enumeration gives `n(C)≠n(D)` with `μ*=e_1`. The unique
letters are `UNDEFINED`, `−`, `UNDEFINED`, `−`. Reverse and face are
`UNDEFINED` because `L(A)` and `L(C)` vanish on that axis. Unique `P_+` is a
different object and is not used. The strictly-earlier leftover occupancy
kernel is a different object even when its unique letters coincide. Leftover
of already-recorded six-neighbor lock lists is a different object. The
x-probe same-tick formdraw occupancy-kernel split is a different object. The
kernel remains displayed.

### N8 — cross-cycle echo

A leftover-closed occupancy kernel on the perp two-site seed reports
`n(C)=n(D)=(−1/3, 0, 0)` and closes a unique occupancy face there. That is
not this display: the seed here is `+e_1/−e_1`, occupancy is
same-tick-inclusive, the y-probes are `A=(0,1,0)` and `C=(0,2,0)`, and
`n(C)≠n(D)`. Strictly-earlier occupancy on these same four opposite-lock
y-probes reports leftover Theorem 1 kernels `n(A)=(0, 0, 0)`,
`n(B)=(−1/3, 0, 0)`, `n(C)=(0, −1/3, 0)`, `n(D)=(−1/3, 1/3, 0)`. Same-tick
partners change the kernels at `A`, `B`, and `D`. A unique-vector
already-recorded neighbor-lock readout on these same y-probes letters `A`
as `UNDEFINED`, `B` as `+e_3`, `C` as `−e_1`, and `D` as `UNDEFINED`. The
x-probe same-tick formdraw occupancy-kernel split on this same opposite-lock
process reports `μ*=e_2` and letters `UNDEFINED`, `−`, `+`, `UNDEFINED`.
This note does not reuse those scorings.

**Gate disposition:** PASS for the same-tick-inclusive occupancy-kernel
disagreement and `UNDEFINED` reverse/face reports above. FAIL / DO NOT SHIP
for “unique `P_+` is this letter,” “letters are Admissibility,” “letters feed
`n`,” “the letter is leftover of the strictly-earlier occupancy kernel,”
“this is leftover of the four y-probe neighbor-lock lists,” “this is the
x-probe same-tick formdraw occupancy-kernel split,” or “reverse holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the opposite-lock two-site
perp-step incoming-lock process, computes the same-tick-inclusive formdraw
occupancy kernel `n` from formed-at-or-before six-neighbor occupancy at each
y-probe's formation tick, tests whether `n(C)=n(D)`, reads the unique
splitting-component letter, and checks Theorems 1--3. It also checks that
unique `P_+`, nscodot, leftover of the strictly-earlier occupancy kernel,
leftover of already-recorded six-neighbor lock lists, leftover of the four
y-probe neighbor-lock lists, and the x-probe same-tick formdraw
occupancy-kernel split are not this lettering, that a letter is not fed into
occupancy `n`, and that the occupancy-kernel formation member is not attached.
No runner cache is written.
