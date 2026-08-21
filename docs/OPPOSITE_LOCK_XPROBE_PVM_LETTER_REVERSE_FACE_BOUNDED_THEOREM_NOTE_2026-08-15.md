---
claim_id: opposite_lock_xprobe_pvm_letter_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from named rank-1 PVM letters on the four nsopp x-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_xprobe_pvm_letter_reverse_face_2026_08_15.py
---

# Named Rank-1 PVM Letters On Four Opposite-Lock X-Probes: Reverse And Face

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** named rank-1 PVM letters in `{+,−}` read from the formdraw occupancy
kernel `n` at the formation of four x-probes of the displayed opposite-lock
two-site process, scored as reverse and face. If `n=0` or the named
construction assigns no letter, the comparison is `UNDEFINED`. Uniqueness is
not required. Displayed, not adopted. This note does not write PVM letters
into Admissibility, does not feed letters into occupancy `n`, and does not
attach the occupancy-kernel formation member. This is the same Qubit
register as the y-probe display, read on the four x-probes. It is not leftover
of a one-site perpnn PVM-letter report that assigned no letter.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_xprobe_pvm_letter_reverse_face_2026_08_15.py`](../scripts/opposite_lock_xprobe_pvm_letter_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. Named rank-1 PVM letters are `{+,−}` names of the projectors `P_±`
read from occupancy-kernel `n`. Those two alphabets are not identified.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of formdraw occupancy-kernel n and named rank-1 P_± letters on the four nsopp x-probes, with reverse hold and face hold; uniqueness is not claimed and the letters are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_xprobe_pvm_letter_reverse_face
target_blocker_text: "display reverse and face from named rank-1 PVM letters on the four nsopp x-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write letters into Admissibility, do not feed letters into n, and do not identify them with incoming steps."
conditional_surface_status: "exact on B_3(0) for occupancy-kernel PVM letters on the four nsopp x-probes; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose occupancy
kernel and PVM letters are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

Lock alphabet of the displayed process: `{±e_1, ±e_2, ±e_3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded first with opposite locks
`L(0)=+e_1` and `L(0,1,0)=−e_1`.

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

That incoming lock is not occupancy `n` and is not a named rank-1 PVM letter.

Formation ticks are not scored. Reverse and face are not tick inequalities.

## Named occupancy kernel and rank-1 PVM letter

At the formation of a probe, occupancy is read from already-recorded sites
only: a neighbor is occupied if and only if it formed strictly earlier. The
probe itself is still unread. Occupancy is in `{0,1}` and does not depend on
any later PVM letter.

The named formdraw occupancy kernel is the triple

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

Those projectors live in the live Qubit presentation `M_2(C)`. They are not
unit nearest-neighbor steps. This note reads `n` at each probe's formation as
displayed theorem-domain data. It does not attach the occupancy-kernel
formation member: sites form by the opposite-lock perp-step incoming-lock
process, not by an `n ≠ 0` formation rule. It does not attach the two-cube
first-wave occupancy-label display.

A process-determined PVM letter at a probe is a value in `{+,−}` assigned by
that named construction from `n`. Incoming `{±e_i}` tags are not that
assignment. Identifying a named sign of an incoming step with a PVM letter
is refused. Uniqueness is not required: both letters are kept whenever
`n ≠ 0`. Four-probe lettering combinations are not enumerated.

Reverse and face (displayed):

```text
reverse  <=>  L(A)=+ and L(B)=−
face     <=>  L(C)=+ and L(D)=−
```

If a letter needed by a comparison is `UNDEFINED`, that comparison is
`UNDEFINED`. If both needed probes have process-determined letters and the
required letters are among them, the comparison is `hold`. If both needed
probes have process-determined letters and a required letter is missing, the
comparison is `fail`. The report is one of `hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. PVM letters are not written into Admissibility.

## Theorem 1 — occupancy kernel and PVM letter at each probe

Direct enumeration of the displayed opposite-lock process on `B_3(0)` forms
all four x-probes. At each formation the occupancy kernel from
already-recorded six-neighbor occupancy is nonzero, so both named rank-1
letters are assigned:

```text
n(A) = (−1/3, −1/3, 0),     k(A) = 2,     L(A) = {+,−}
n(B) = (−1/3, 0, 0),        k(B) = 1,     L(B) = {+,−}
n(C) = (−1/3, 0, 0),        k(C) = 1,     L(C) = {+,−}
n(D) = (−1/3, 1/3, 0),      k(D) = 2,     L(D) = {+,−}
```

Neighbor occupancies at those formations:

- `A`: already recorded on `−e_1`, `−e_2`, `+e_3`, and `−e_3`;
- `B`: already recorded on `−e_1`;
- `C`: already recorded on `−e_1`;
- `D`: already recorded on `−e_1`, `+e_2`, `+e_3`, and `−e_3`.

Incoming locks exist and need not be unique (`A` keeps three earliest
incoming steps). That non-uniqueness is not a PVM lettering. The PVM letters
are not identified with those incoming steps. Uniqueness is not required.

On the `k=1` probes `B` and `C`, the named traces are `Tr(ρ P_+)=2/3` and
`Tr(ρ P_-)=1/3`. Both contents occupy the site.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if `L(A)=+` and `L(B)=−`. Both probes have letter
set `{+,−}`, so `+` is process-determined at `A` and `−` is process-determined
at `B`. Reverse holds.

Reverse: hold

This is not `fail` and not `UNDEFINED`. A named-sign readout of incoming
steps is a different object and is not used. Formation ticks are not the
reverse predicate.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if `L(C)=+` and `L(D)=−`. Both probes have letter set
`{+,−}`, so `+` is process-determined at `C` and `−` is process-determined at
`D`. Face holds.

Face: hold

Displayed, not adopted. The letters are not written into Admissibility.

This is not `fail` and not `UNDEFINED`.

## What this note does not claim

- It does not select a unique incoming lock or a unique PVM letter.
- It does not identify named rank-1 PVM letters with incoming `{±e_i}`.
- It does not feed letters into occupancy `n`.
- It does not attach the occupancy-kernel formation member.
- It does not attach the two-cube first-wave occupancy-label display.
- It does not census free occupancy letterings independent of `n`.
- It does not enlarge the host beyond `B_3(0)`.
- It does not score reverse or face from formation-tick inequalities.
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

This display uses Lattice to name `B_3(0)` and the four x-probes. It uses
Qubit only as the algebra in which the named projectors `P_±` are written. It
uses Record only as a boundary: a present lock is content. It does not rewrite
Admissibility. The opposite-lock process, the occupancy kernel, the named PVM
letters, and the reverse/face predicates are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; opposite-lock two-site seed `+e_1/−e_1` |
| occupancy kernel `n` at each x-probe formation | Theorem 1; all four `n ≠ 0` |
| named rank-1 PVM letters `{+,−}` from `P_±` | Theorem 1; `{+,−}` at each x-probe |
| reverse and face | Theorems 2–3; both `hold` |
| unique incoming lock or unique PVM letter | not required |
| letters fed into occupancy `n` | not executed |
| occupancy-kernel formation member attached | not attached |
| two-cube first-wave occupancy-label display attached | not attached |
| free occupancy lettering independent of `n` | not enumerated |
| PVM letters as Admissibility content | not adopted |
| formation-tick reverse/face | not scored |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: named rank-1 PVM letters on the four nsopp x-probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed occupancy-kernel PVM-letter reverse/face report on these four nsopp x-probes. |
| V3 | Occupancy kernels, named projectors, and the `hold`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads `n` at formation and names `P_±`. |
| V5 | It is not an adopted content rule: the letters remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those letters into
Admissibility, does not identify them with incoming steps, and does not feed
them into `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| identify PVM letter with named sign of incoming `{±e_i}` | map `+e_i` to `+` and `-e_i` to `−` | refused; different alphabet |
| reverse/face from incoming named signs | reuse the incoming-lock sign readout | different object; not this display |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; not this display |
| unique already-recorded 6-NN lock vector | demand a singleton neighbor-lock vector | different object; occupancy `n` is the kernel here |
| free occupancy letters on the four probes | ignore `n` and letter independently | different object; not enumerated |
| attach occupancy-kernel formation member | form the probes by `n ≠ 0` instead of perp-step | refused; not attached |
| attach two-cube first-wave occupancy-label display | import that first-wave labeling as process law | refused; not attached |
| feed letters into `n` | let `+`/`−` change occupancy | refused; occupancy stays `{0,1}` of the already-recorded set |
| adopt letters into Admissibility | rewrite the local rule by `{+,−}` | refused; displayed, not adopted |
| unique PVM letter required | demand one letter per probe | uniqueness is not required; both letters are kept |
| leftover of one-site perpnn PVM letters | reuse a report that assigned no letter | refused; this process reads `n` on the opposite-lock two-site seed |
| leftover of the y-probe Qubit register | score `A=(0,1,0)` as the seed | refused; this display scores the four x-probes |

Honesty marker for each row: `ATTEMPTED`.

### N2 — wall independence

Missing physical adoption, missing occupancy-kernel formation attachment, and
missing Record identification of the named PVM bits are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, opposite-lock two-site seed `+e_1` and `−e_1`,
perpendicular step rule, incoming-step lock, occupancy kernel from
already-recorded neighbors, named `P_±` letters, four x-probes, and
reverse/face as presence of `+` then `−` are declared. No uniqueness, no
occupancy-kernel formation attachment, no first-wave occupancy-label
attachment, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each named projector `P_±` and each occupancy component | no continuum alphabet |
| per site | `A,B,C,D` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four `{+,−}` letter sets and two `hold` comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{+,−}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Once `n ≠ 0` at a forming x-probe, the site should lock a unique
letter `+` or `−`, reverse and face should fail unless that unique pair is
exactly `+/−`, occupancy should track that sign, and the y-probe seed letter
should be reused.

**Answer:** The named construction assigns both `P_+` and `P_-` whenever
`n ≠ 0`. Occupancy stays `{0,1}` of the already-recorded set. Reverse and
face hold because the required letters are among the process-determined
letters. Uniqueness is not required. The y-probe seed is not scored here.
The bits remain displayed.

### N8 — cross-cycle echo

A prior display scored named rank-1 PVM letters on the one-site perpnn
process without reading occupancy-kernel `n`, and reported `UNDEFINED`. This
note is not that display: it reads `n` on the opposite-lock two-site process
and reports `hold` / `hold`. The same named construction on the four nsopp
y-probes assigns no letter at the seed `A=(0,1,0)`, so reverse there is
`UNDEFINED`. This note scores the four x-probes. A unique already-recorded
six-neighbor lock-vector readout on this same process reports reverse fail
and face `UNDEFINED`. This note does not reuse that scoring.

**Gate disposition:** PASS for the occupancy-kernel PVM-letter reverse/face
reports above. FAIL / DO NOT SHIP for “the PVM letter equals the incoming
step sign,” “letters are Admissibility,” “letters feed `n`,” “reverse fails,”
or “face fails.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the opposite-lock two-site
perp-step incoming-lock process, computes the formdraw occupancy kernel `n`
from already-recorded six-neighbor occupancy at each x-probe's formation,
reconstructs the named rank-1 projectors `P_±` as displayed data, reads
process-determined PVM letters at the four x-probes, and checks Theorems 1--3.
It also checks that incoming steps are not PVM letters, that letters are not
fed into occupancy `n`, that the occupancy-kernel formation member is not
attached, and that this is not leftover of the y-probe seed letter. No runner
cache is written.
