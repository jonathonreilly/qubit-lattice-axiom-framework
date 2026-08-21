---
claim_id: perpnn_pvm_letter_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from named rank-1 PVM letters on the four perpnn probes, or UNDEFINED if the process determines no such letter, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/perpnn_pvm_letter_reverse_face_2026_08_15.py
---

# Named Rank-1 PVM Letters On Four Perpnn Probes: Reverse And Face

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** named rank-1 PVM letters in `{+,−}` on four probes of the
displayed perpnn process, scored as reverse and face. If the process
determines no such letter at a needed probe, the comparison is
`UNDEFINED`. Uniqueness is not required. Displayed, not adopted. This note
does not write PVM letters into Admissibility, does not feed letters into
occupancy `n`, and does not attach the occupancy-kernel member.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/perpnn_pvm_letter_reverse_face_2026_08_15.py`](../scripts/perpnn_pvm_letter_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named probes. Incoming lock letters are unit nearest-neighbor
steps. Named rank-1 PVM letters are `{+,−}` names of the projectors `P_±`
below. Those two alphabets are not identified.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report that the displayed perpnn process determines no named rank-1 PVM letter at the four probes, so reverse and face are UNDEFINED; uniqueness is not claimed and the letters are not adopted."
trace_class: frontier_discovery
target_claim_id: perpnn_pvm_letter_reverse_face
target_blocker_text: "display reverse and face from named rank-1 PVM letters on the four perpnn probes, or UNDEFINED if the process determines no such letter"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed as UNDEFINED when no PVM letter is process-determined; do not write letters into Admissibility and do not identify them with incoming steps."
conditional_surface_status: "exact on B_3(0) for named rank-1 PVM letters on the four probes; displayed, not adopted"
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

No larger host is used. The four probes are the only sites whose PVM letters
are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

Lock alphabet of the displayed process: `{±e_1, ±e_2, ±e_3}`.

Seed: the origin is recorded first with lock letter `+e_1`.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s` (the unit vector from `p` to `q`).
If several allowed parents reach `q` at the same earliest formation, each such
incoming step is kept as a possible lock. Uniqueness is not required. A later
parent does not re-form `q`.

That incoming lock is not occupancy `n` and is not a named rank-1 PVM letter.

## Named rank-1 PVM letter

The named construction, copied as displayed data from the formation PVM draw
and from the two-cube occupancy-label display, is as follows.

At an unread site with occupancy kernel `n ≠ 0`, write `k = |3n|^2` and
`H = a σ_x + b σ_y + c σ_z`. The two legal lock contents are the rank-1
projectors

```text
P_± = (√k I ± H) / (2√k).
```

The letter `+` names `P_+`. The letter `−` names `P_-`. Occupancy of a formed
site remains `1` for either content, so the letter does not feed `n`.

Those projectors live in the live Qubit presentation `M_2(C)`. They are not
unit nearest-neighbor steps. This note does not attach the occupancy-kernel
member as process law, does not run that occupancy step on the four probes,
and does not feed any letter into `n`.

A process-determined PVM letter at a probe is a value in `{+,−}` assigned by
that named construction from the displayed perpnn process. Incoming
`{±e_i}` tags are not that assignment. If the named construction assigns no
PVM letter at a probe, the letter is `UNDEFINED`. If a probe has several
process-determined letters, reverse and face are evaluated on every
combination. Uniqueness is not required.

Reverse and face (displayed):

```text
reverse  <=>  L(A)=+ and L(B)=−
face     <=>  L(C)=+ and L(D)=−
```

If a letter needed by a comparison is `UNDEFINED`, that comparison is
`UNDEFINED`. The report is one of `hold-on-all`, `some`, `none`, or
`UNDEFINED`.

Admissibility is not edited. PVM letters are not written into Admissibility.

## Theorem 1 — process-determined PVM letter at each probe

Direct enumeration of the displayed perpnn process on `B_3(0)` yields
incoming locks in `NN` at every formed site, including the four probes.
Those locks are unit steps. They are not the named projectors `P_±` and they
are not the letters `{+,−}`.

The named PVM construction assigns a letter only from occupancy-kernel `n`
at an unread site. The displayed process does not compute that kernel and
does not draw `P_±`. Identifying a named sign of an incoming step with a PVM
letter is refused.

Therefore no process-determined PVM letter exists at any of the four probes:

```text
L(A) = UNDEFINED
L(B) = UNDEFINED
L(C) = UNDEFINED
L(D) = UNDEFINED
```

Incoming lock sets exist and need not be unique. That non-uniqueness is not
a PVM lettering. Uniqueness is not required.

## Theorem 2 — reverse report

Reverse is `L(A)=+` and `L(B)=−`. Both `L(A)` and `L(B)` are `UNDEFINED`.
The comparison is therefore `UNDEFINED`.

Report: `UNDEFINED`.

This is not `hold-on-all`, not `some`, and not `none`. A named-sign readout
of incoming steps is a different object and is not used.

## Theorem 3 — face report

Face is `L(C)=+` and `L(D)=−`. Both `L(C)` and `L(D)` are `UNDEFINED`.
The comparison is therefore `UNDEFINED`.

Report: `UNDEFINED`.

Displayed, not adopted. The letters are not written into Admissibility.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify named rank-1 PVM letters with incoming `{±e_i}`.
- It does not feed letters into occupancy `n`.
- It does not attach the occupancy-kernel member.
- It does not census free occupancy letterings of the four probes.
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

This display uses Lattice to name `B_3(0)` and the four probes. It uses Qubit
only as the algebra in which the named projectors `P_±` are written. It uses
Record only as a boundary: a present lock is content. It does not rewrite
Admissibility. The perpnn process, the named PVM letters, and the
reverse/face predicates are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; seed lock `+e_1` |
| named rank-1 PVM letters `{+,−}` from `P_±` | declared; not incoming tags |
| process-determined letter at `A,B,C,D` | Theorem 1; all `UNDEFINED` |
| reverse and face | Theorems 2–3; both `UNDEFINED` |
| unique incoming lock | not required |
| letters fed into occupancy `n` | not executed |
| occupancy-kernel member attached | not attached |
| free occupancy lettering of the four probes | not enumerated |
| PVM letters as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: named rank-1 PVM letters on the four perpnn probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed PVM-letter reverse/face report on these four perpnn probes. |
| V3 | Incoming locks, the named projectors, and the `UNDEFINED` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it asks whether a displayed projector letter is process-determined. |
| V5 | It is not an adopted content rule: the letters remain displayed, and here they are `UNDEFINED`. |

## No-go discipline gate

The negative content is narrow: the displayed perpnn process does not assign
the named rank-1 PVM letters, does not write those letters into Admissibility,
and does not identify them with incoming steps. No global impossibility is
claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| identify PVM letter with named sign of incoming `{±e_i}` | map `+e_i` to `+` and `-e_i` to `−` | refused; different alphabet |
| reverse/face from incoming named signs | reuse the incoming-lock sign readout | different object; not this display |
| free occupancy letters on the four probes | ignore the process and letter independently | different object; not enumerated |
| attach occupancy-kernel member | form the probes by `n ≠ 0` and draw `P_±` | refused; not attached |
| feed letters into `n` | let `+`/`−` change occupancy | refused; occupancy stays `{0,1}` of the locked set |
| adopt letters into Admissibility | rewrite the local rule by `{+,−}` | refused; displayed, not adopted |
| unique PVM letter required | demand one letter per probe | uniqueness is not required; here none is determined |

### N2 — wall independence

Missing physical adoption, missing occupancy-kernel attachment, and missing
Record identification of the named PVM bits are distinct open premises. This
note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, seed lock `+e_1`, perpendicular step rule, incoming-step
lock, named `P_±` letters, four probes, and reverse/face definitions are
declared. No uniqueness, no occupancy-kernel attachment, and no Admissibility
rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`UNDEFINED` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each named projector `P_±` and each incoming step | no continuum alphabet |
| per site | `A,B,C,D` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four `UNDEFINED` letters and two `UNDEFINED` comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later occupancy-kernel attachment that actually draws
`P_±`, a separate Record content map for reverse/face, and a formation-rate
rule. None is taken here.

### N7 — hostile steelman

**Steelman:** Once the four probes form, each should carry a rank-1 PVM
letter `+` or `−` from the named projectors, reverse and face should hold or
fail as bits, and those bits should be adopted as Admissibility content.

**Answer:** The displayed process locks incoming nearest-neighbor steps, not
`P_±`. The named construction assigns letters from occupancy-kernel `n`,
which this process does not compute. Incoming `{±e_i}` are not those letters.
All four probes are `UNDEFINED`, so reverse and face are `UNDEFINED`. The
bits remain displayed. Uniqueness is not required.

### N8 — cross-cycle echo

A prior display scored reverse and face from named signs of incoming locks
on the same four probes. This note does not reuse that scoring: it asks for
named rank-1 PVM letters and reports `UNDEFINED` / `UNDEFINED`. The two
displays are distinct objects.

**Gate disposition:** PASS for the named rank-1 PVM-letter reverse/face
reports above. FAIL / DO NOT SHIP for “the PVM letter equals the incoming
step sign,” “letters are Admissibility,” or “reverse/face holds on all
combinations.”

## Primary runner

The paired runner builds `B_3(0)`, runs the perp-step incoming-lock process
from the seed, reconstructs the named rank-1 projectors `P_±` as displayed
data, reads process-determined PVM letters at the four probes, and checks
Theorems 1--3. It also checks that incoming steps are not PVM letters, that
letters are not fed into occupancy `n`, and that occupancy-kernel attachment
is not performed. No runner cache is written.
