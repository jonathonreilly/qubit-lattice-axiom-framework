---
claim_id: opposite_lock_yprobe_pvm_letter_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from named rank-1 PVM letters on the four nsopp y-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_yprobe_pvm_letter_reverse_face_2026_08_15.py
---

# Named Rank-1 PVM Letters On Four Opposite-Lock Y-Probes: Reverse And Face

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** named rank-1 PVM letters in `{+,−}` as constructed in the formation
PVM draw and the two-cube occupancy-label display, read from occupancy-kernel
`n` at the formation of the four y-probes `A=(0,1,0)`, `B=(1,1,1)`,
`C=(0,2,0)`, `D=(1,1,0)` of the displayed opposite-lock two-site seed,
scored as reverse and face. `A` is a seed. Occupancy at a seed formation is
already-recorded strictly earlier; the same-tick partner is not
already-recorded. If `n=0` or the named construction assigns no letter, the
comparison is `UNDEFINED`. Both legal letters `{+,−}` are kept whenever
`n≠0`. Uniqueness is not required. Incoming `{±e_i}` tags are not the letter.
Occupancy `n` is not the letter. Displayed, not adopted. This note does not
write PVM letters into Admissibility, does not feed letters into occupancy
`n`, and does not attach the occupancy-kernel formation member.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_yprobe_pvm_letter_reverse_face_2026_08_15.py`](../scripts/opposite_lock_yprobe_pvm_letter_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. Named rank-1 PVM letters are `{+,−}` names of the projectors `P_±`
read from occupancy-kernel `n`. Those two alphabets are not identified.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of named rank-1 PVM letters from occupancy-kernel n on the four opposite-lock y-probes, with reverse UNDEFINED because n(A)=0 and face scored as some; uniqueness is not claimed and the letters are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_yprobe_pvm_letter_reverse_face
target_blocker_text: "display reverse and face from named rank-1 PVM letters on the four opposite-lock y-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write letters into Admissibility, do not feed letters into n, do not identify them with incoming steps, and do not attach the occupancy-kernel formation member."
conditional_surface_status: "exact on B_3(0) for named rank-1 PVM letters on the four opposite-lock y-probes; displayed, not adopted"
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
kernel and PVM letters are scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

Lock alphabet of the displayed process: `{±e_1, ±e_2, ±e_3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded first with opposite locks
`L(0)=+e_1` and `L(0,1,0)=−e_1`.

`A` is the seed site `(0,1,0)`. It is already formed with the seed. It is not
re-formed by a later incoming step.

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
`q`. A seed site is already formed, so it is not re-formed.

That incoming lock is not occupancy `n` and is not a named rank-1 PVM letter.

## Named occupancy kernel and rank-1 PVM letter

At the formation of a probe, occupancy is read from already-recorded sites
only: a neighbor is occupied if and only if it formed strictly earlier. The
probe itself is still unread. Occupancy is in `{0,1}` and does not depend on
any later PVM letter.

Occupancy at a seed formation is already-recorded strictly earlier. The
same-tick partner is not already-recorded. In particular, at the seed
formation of `A` the origin is the same-tick partner of `A` and does not
contribute occupancy.

The named occupancy kernel, copied as displayed data from the formation PVM
draw and from the two-cube occupancy-label display, is the triple

```text
n_μ = (o_{+μ} − o_{−μ}) / 3,     μ = 1,2,3.
```

Write `k = |3n|^2`. If `n = 0`, the named construction assigns no letter and
the probe is `UNDEFINED`. If `n ≠ 0`, write `H = a σ_x + b σ_y + c σ_z` with
`(a,b,c) = 3n`. Then `H^2 = k I`, and the two legal lock contents are the
rank-1 projectors

```text
P_± = (√k I ± H) / (2√k).
```

The letter `+` names `P_+`. The letter `−` names `P_-`. Both letters are
legal whenever `n ≠ 0`. Occupancy of a formed site remains `1` for either
content, so the letter does not feed `n`.

Those projectors live in the live Qubit presentation `M_2(C)`. Occupancy
exist-opposite does not use that presentation. The projectors are not unit
nearest-neighbor steps. This note reads `n` at each y-probe's formation as
displayed theorem-domain data. It does not attach the occupancy-kernel
formation member: sites form by the opposite-lock perp-step incoming-lock
process, not by an `n ≠ 0` formation rule.

A process-determined PVM letter at a probe is a value in `{+,−}` assigned by
that named construction from `n`. Incoming `{±e_i}` tags are not that
assignment. Identifying a named sign of an incoming step with a PVM letter
is refused. If a probe has several process-determined letters, reverse and
face are evaluated on every combination. Uniqueness is not required. Both
`{+,−}` at `n≠0` are the letter set. Unique `P_+` is not used.

This display is not unique `f(n)`. It does not select one letter as a function
of `n`. It is not ndot: it does not assign a unique letter by the sign of a
contraction `n·v`. It is not a leftover of already-recorded six-neighbor lock
vectors. It is not a scoring of formation order.

Reverse and face (displayed):

```text
reverse  <=>  L(A)=+ and L(B)=−
face     <=>  L(C)=+ and L(D)=−
```

If a letter needed by a comparison is `UNDEFINED`, that comparison is
`UNDEFINED`. The report is one of `all`, `some`, `none`, or `UNDEFINED`.

Admissibility is not edited. PVM letters are not written into Admissibility.

## Theorem 1 — PVM letter or UNDEFINED at A, B, C, D

Direct enumeration of the displayed opposite-lock process on `B_3(0)` forms
all four y-probes. At the seed formation of `A` the occupancy kernel from
already-recorded six-neighbor occupancy is zero, so no named rank-1 letter is
assigned. At the formation of `B`, `C`, and `D` the occupancy kernel is
nonzero, so both named rank-1 letters are assigned:

```text
n(A) = (0, 0, 0),       k(A) = 0,     L(A) = UNDEFINED
n(B) = (−1/3, 0, 0),    k(B) = 1,     L(B) = {+,−}
n(C) = (0, −1/3, 0),    k(C) = 1,     L(C) = {+,−}
n(D) = (−1/3, 1/3, 0),  k(D) = 2,     L(D) = {+,−}
```

Neighbor occupancies at those formations:

- `A`: no already-recorded six-neighbor; the origin is the same-tick partner
  and is not already-recorded;
- `B`: already recorded on `−e_1`;
- `C`: already recorded on `−e_2`;
- `D`: already recorded on `−e_1`, `+e_2`, `+e_3`, and `−e_3`.

`A` carries the seed lock `−e_1`. Incoming locks of the grown sites exist and
need not be unique (`D` has three earliest incoming steps). That
non-uniqueness is not a PVM lettering. The PVM letters are not identified
with those incoming steps. Uniqueness is not required.

On the `k=1` y-probes `B` and `C`, the named traces are `Tr(ρ P_+)=2/3` and
`Tr(ρ P_-)=1/3`. Both contents occupy the site. On the `k=2` y-probe `D`,
`H^2 = 2 I` and both named letters remain legal.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse is `L(A)=+` and `L(B)=−`. `L(A)` is `UNDEFINED` because `n(A)=0`. A
letter needed by the comparison is `UNDEFINED`.

Report: `UNDEFINED`.

This is not `all`, not `some`, and not `none`. A named-sign readout of
incoming steps, a unique lock-vector leftover, a unique `f(n)` letter, an
ndot contraction letter, and a formation-order inequality are different
objects and are not used.

## Theorem 3 — face hold / fail / UNDEFINED

Face is `L(C)=+` and `L(D)=−`. Both probes have letter set `{+,−}`, so every
combination of those two letter sets is scored. There are four combinations.
Face holds on exactly one of them and fails on the other three.

Report: `some`.

This is not `all`, not `none`, and not `UNDEFINED`. Displayed, not adopted.
The letters are not written into Admissibility.

## What this note does not claim

- It does not select a unique incoming lock or a unique PVM letter.
- It is not unique `f(n)`.
- It is not ndot.
- It does not identify named rank-1 PVM letters with incoming `{±e_i}`.
- It does not feed letters into occupancy `n`.
- It does not attach the occupancy-kernel formation member.
- It does not treat the same-tick seed partner as already-recorded.
- It does not score reverse or face from formation order.
- It does not census free occupancy letterings independent of `n`.
- It does not enlarge the host beyond `B_3(0)`.
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
only as the algebra in which the named projectors `P_±` are written. It uses
Record only as a boundary: a present lock is content. It does not rewrite
Admissibility. The opposite-lock process, the occupancy kernel, the named PVM
letters, and the reverse/face predicates are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site seed `+e_1/−e_1` |
| occupancy kernel `n` at each y-probe formation | Theorem 1; `n(A)=0`; `n(B),n(C),n(D) ≠ 0` |
| named rank-1 PVM letters `{+,−}` from `P_±` | Theorem 1; `UNDEFINED` at `A`; `{+,−}` at `B,C,D` |
| reverse and face | Theorems 2–3; `UNDEFINED` / `some` |
| unique incoming lock or unique PVM letter | not required |
| unique `f(n)` | not this display |
| ndot contraction letter | not this display |
| incoming `{±e_i}` identified with the letter | refused |
| letters fed into occupancy `n` | not executed |
| occupancy-kernel formation member attached | not attached |
| same-tick seed partner counted as occupancy | not executed |
| PVM letters as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: named rank-1 PVM letters on the four opposite-lock y-probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed occupancy-kernel PVM-letter reverse/face report on these four opposite-lock y-probes. |
| V3 | Occupancy kernels, named projectors, and the `UNDEFINED`/`some` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads `n` at formation and names `P_±` in `M_2(C)`. |
| V5 | It is not an adopted content rule: the letters remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those letters into
Admissibility, does not identify them with incoming steps, does not feed them
into `n`, does not count the same-tick seed partner as occupancy, and is not
unique `f(n)` or ndot. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| identify PVM letter with named sign of incoming `{±e_i}` | map `+e_i` to `+` and `-e_i` to `−` | refused; different alphabet |
| reverse/face from incoming named signs | reuse the incoming-lock sign readout | different object; not this display |
| reverse/face from formation-order inequalities | score y-probes by formation order | different object; formation locates occupancy only |
| unique `f(n)` | assign one letter as a function of `n` | different object; both `{+,−}` are kept at `n≠0` |
| unique `P_+` | keep only `P_+` when `n≠0` | refused; both letters are legal |
| ndot contraction letter | unique letter `sign(n·v)` | different object; not ndot |
| leftover unique lock vector of already-recorded neighbors | singleton `{v}` in `{±e_i}` | different alphabet; not this letter |
| count same-tick seed partner as occupancy | occupy the origin at the seed formation of `A` | refused; already-recorded is strictly earlier |
| attach occupancy-kernel formation member | form the probes by `n ≠ 0` instead of perp-step | refused; not attached; `A` forms with `n=0` |
| feed letters into `n` | let `+`/`−` change occupancy | refused; occupancy stays `{0,1}` of the already-recorded set |
| adopt letters into Admissibility | rewrite the local rule by `{+,−}` | refused; displayed, not adopted |
| unique PVM letter required | demand one letter per probe | uniqueness is not required; both letters are kept at `n≠0` |

### N2 — wall independence

Missing physical adoption, missing occupancy-kernel formation attachment, and
missing Record identification of the named PVM bits are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, occupancy kernel from already-recorded neighbors,
seed occupancy excluding the same-tick partner, named `P_±` letters, four
y-probes, and reverse/face definitions are declared. No uniqueness, no
occupancy-kernel formation attachment, no Admissibility rewrite, no unique
`f(n)`, and no ndot are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`UNDEFINED` and `some` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each named projector `P_±` and each occupancy component | no continuum alphabet |
| per site | `A,B,C,D` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four letter sets and `UNDEFINED`/`some` comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{+,−}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** `A` is a seed, so occupancy should include the origin partner,
`n(A)` should be nonzero, the site should lock a unique letter `+` or `−` by
unique `f(n)` or by the named sign of its incoming lock `−e_1`, reverse should
fail, and face should hold on all combinations or be adopted as Admissibility
content.

**Answer:** Already-recorded occupancy is strictly earlier than formation. The
same-tick partner is not occupied, so `n(A)=0` and reverse is `UNDEFINED`.
The named construction assigns both `P_+` and `P_-` whenever `n ≠ 0`. Face
holds on some combinations of `C` and `D` and fails on others. Incoming
`{±e_i}` tags are not PVM letters. The bits remain displayed. Uniqueness is
not required. This is not unique `f(n)` and is not ndot.

### N8 — cross-cycle echo

A prior display scored named rank-1 PVM letters on a one-site perp-step
process without reading occupancy-kernel `n`, and reported `UNDEFINED`. This
note is not that display: it reads `n` on the opposite-lock two-site y-probes.
A second prior display scored the same occupancy-kernel letters on nnseed
y-probes with seed locks `+e_1/+e_2`; those kernels at `B` and `D` are not
the kernels here. A third prior display scored reverse and face from incoming
`{±e_i}` tags on opposite-lock y-probes; that alphabet is not this letter.
This note does not reuse those scorings.

**Gate disposition:** PASS for the named rank-1 PVM-letter reverse/face
reports on the four opposite-lock y-probes above. FAIL / DO NOT SHIP for “the
PVM letter equals the incoming step sign,” “letters are Admissibility,”
“letters feed `n`,” “unique `f(n)`,” “ndot,” “same-tick seed partner occupies
`A`,” or “reverse/face holds on all combinations.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the opposite-lock two-site
perp-step incoming-lock process, computes the occupancy kernel `n` from
already-recorded six-neighbor occupancy at each y-probe's formation,
reconstructs the named rank-1 projectors `P_±` as displayed data, reads
process-determined PVM letters at the four y-probes, and checks Theorems 1--3.
It also checks that incoming steps are not PVM letters, that letters are not
fed into occupancy `n`, that the occupancy-kernel formation member is not
attached, that the same-tick seed partner is not already-recorded, and that
the scoring is not unique `f(n)` and not ndot. No runner cache is written.
