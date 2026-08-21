---
claim_id: nnseed_unique_pplus_along_n_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from the unique formdraw letter P_+ along n on the four nnseed probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_unique_pplus_along_n_reverse_face_2026_08_15.py
---

# Unique Formdraw Letter P_+ Along n On Four Nnseed Probes: Reverse And Face

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** unique named rank-1 PVM letter `+` naming `P_+` along the formdraw
occupancy kernel `n` at the formation tick of four probes of the displayed
two-site nnseed process, scored as reverse and face. If `n=0` the letter is
`UNDEFINED`. If `n≠0` the unique letter is `+`; minus is not assigned.
Uniqueness is not required. Displayed, not adopted. This note does not write
PVM letters into Admissibility, does not feed letters into occupancy `n`, and
does not attach the occupancy-kernel formation member.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_unique_pplus_along_n_reverse_face_2026_08_15.py`](../scripts/nnseed_unique_pplus_along_n_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named probes. Incoming lock letters are unit nearest-neighbor
steps. The unique named rank-1 PVM letter is `+`, the name of the projector
`P_+` along occupancy-kernel `n`. Those two alphabets are not identified.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of formdraw occupancy-kernel n and the unique named rank-1 letter + naming P_+ along n on the four nnseed probes, with reverse and face scored as none; uniqueness is not claimed and the letter is not adopted."
trace_class: frontier_discovery
target_claim_id: nnseed_unique_pplus_along_n_reverse_face
target_blocker_text: "display reverse and face from the unique formdraw letter P_+ along n on the four nnseed probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write the unique letter into Admissibility, do not feed letters into n, and do not identify them with incoming steps."
conditional_surface_status: "exact on B_3(0) for unique P_+ along n on the four nnseed probes; displayed, not adopted"
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
kernel and unique PVM letter are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

Lock alphabet of the displayed process: `{±e_1, ±e_2, ±e_3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
perp-consistent locks `L(0)=+e_1` and `L(0,1,0)=+e_2`.

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

## Named occupancy kernel and unique letter P_+ along n

At the formation tick of a probe, occupancy is read from already-recorded
sites only: a neighbor is occupied if and only if it formed strictly earlier.
The probe itself is still unread. Occupancy is in `{0,1}` and does not depend
on any later PVM letter.

The named formdraw occupancy kernel is the triple

```text
n_μ = (o_{+μ} − o_{−μ}) / 3,     μ = 1,2,3.
```

Write `k = |3n|^2`. If `n = 0`, the named construction assigns no letter and
the probe is `UNDEFINED`. If `n ≠ 0`, write `H = a σ_x + b σ_y + c σ_z` with
`(a,b,c) = 3n`. Then `H^2 = k I`, and the named rank-1 pair is

```text
P_± = (√k I ± H) / (2√k).
```

The unique letter is `+`. It names `P_+` along `n`, the `+` member of that
pair. Minus is not assigned. Occupancy of a formed site remains `1` for that
content, so the letter does not feed `n`. This is not a free lettering of the
four probes independent of `n`.

Those projectors live in the live Qubit presentation `M_2(C)`. They are not
unit nearest-neighbor steps. This note reads `n` at each probe's formation
tick as displayed theorem-domain data. It does not attach the occupancy-kernel
formation member: sites form by the nnseed perp-step incoming-lock process,
not by an `n ≠ 0` formation rule.

A process-determined PVM letter at a probe is a value in `{+,−}` assigned by
that named construction from `n`. Incoming `{±e_i}` tags are not that
assignment. Identifying a named sign of an incoming step with a PVM letter
is refused. Uniqueness is not required of incoming locks.

Reverse and face (displayed):

```text
reverse  <=>  L(A)=+ and L(B)=−
face     <=>  L(C)=+ and L(D)=−
```

If a letter needed by a comparison is `UNDEFINED`, that comparison is
`UNDEFINED`. The report is one of `all`, `some`, `none`, or `UNDEFINED`.

Admissibility is not edited. PVM letters are not written into Admissibility.

## Theorem 1 — occupancy kernel and unique letter at each probe

Direct enumeration of the displayed nnseed process on `B_3(0)` forms all four
probes. At each formation tick the occupancy kernel from already-recorded
six-neighbor occupancy is nonzero, so the unique named rank-1 letter is `+`:

```text
n(A) = (−1/3, 1/3, 0),     k(A) = 2,     L(A) = +
n(B) = (−1/3, 0, −1/3),    k(B) = 2,     L(B) = +
n(C) = (−1/3, 0, 0),       k(C) = 1,     L(C) = +
n(D) = (−1/3, 0, 0),       k(D) = 1,     L(D) = +
```

Neighbor occupancies at those formation ticks:

- `A`: already recorded on `−e_1` and `+e_2`;
- `B`: already recorded on `−e_1` and `−e_3`;
- `C`: already recorded on `−e_1`;
- `D`: already recorded on `−e_1`.

Incoming locks exist and need not be unique (`B` has two earliest incoming
steps). That non-uniqueness is not a PVM lettering. The unique letter is not
identified with those incoming steps. Uniqueness is not required.

On the `k=1` probes `C` and `D`, the named traces are `Tr(ρ P_+)=2/3` and
`Tr(ρ P_-)=1/3`. Only `P_+` is named as the unique letter.

## Theorem 2 — reverse report

Reverse is `L(A)=+` and `L(B)=−`. Both probes have unique letter `+`, so the
comparison is defined and `L(B)=−` fails.

Report: `none`.

This is not `all`, not `some`, and not `UNDEFINED`. A named-sign readout of
incoming steps is a different object and is not used.

## Theorem 3 — face report

Face is `L(C)=+` and `L(D)=−`. Both probes have unique letter `+`. Face
fails because `L(D)` is `+`, not `−`.

Report: `none`.

Displayed, not adopted. The letters are not written into Admissibility.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not also assign minus when `n ≠ 0`.
- It does not identify named rank-1 PVM letters with incoming `{±e_i}`.
- It does not feed letters into occupancy `n`.
- It does not attach the occupancy-kernel formation member.
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

This display uses Lattice to name `B_3(0)` and the four probes. It uses Qubit
only as the algebra in which the named projector `P_+` is written. It uses
Record only as a boundary: a present lock is content. It does not rewrite
Admissibility. The nnseed process, the occupancy kernel, the unique letter
`P_+` along `n`, and the reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site seed `+e_1/+e_2` |
| occupancy kernel `n` at each probe formation tick | Theorem 1; all four `n ≠ 0` |
| unique named rank-1 letter `+` naming `P_+` along `n` | Theorem 1; `+` at each probe |
| reverse and face | Theorems 2–3; both `none` |
| unique incoming lock | not required |
| letters fed into occupancy `n` | not executed |
| occupancy-kernel formation member attached | not attached |
| free occupancy lettering independent of `n` | not enumerated |
| PVM letters as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: unique formdraw letter `P_+` along `n` on the four nnseed probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed unique-`P_+`-along-`n` reverse/face report on these four nnseed probes. |
| V3 | Occupancy kernels, the unique named projector, and the `none`/`none` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads `n` at formation and names only `P_+`. |
| V5 | It is not an adopted content rule: the letter remains displayed. |

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
| free occupancy letters on the four probes | ignore `n` and letter independently | different object; not enumerated |
| assign both `{+,−}` whenever `n ≠ 0` | keep minus as a second legal letter | refused; unique letter is `+` only |
| attach occupancy-kernel formation member | form the probes by `n ≠ 0` instead of perp-step | refused; not attached |
| feed letters into `n` | let `+`/`−` change occupancy | refused; occupancy stays `{0,1}` of the already-recorded set |
| adopt letters into Admissibility | rewrite the local rule by `{+,−}` | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; both incoming steps at `B` are kept |

### N2 — wall independence

Missing physical adoption, missing occupancy-kernel formation attachment, and
missing Record identification of the named PVM bit are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `+e_2`, perpendicular step
rule, incoming-step lock, occupancy kernel from already-recorded neighbors,
unique letter `P_+` along `n`, four probes, and reverse/face definitions are
declared. No incoming-lock uniqueness, no occupancy-kernel formation
attachment, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`none` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | the named projector `P_+` along `n` | no continuum alphabet |
| per site | `A,B,C,D` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four unique `+` letters and two `none` comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{+,−}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Once `n ≠ 0` at a forming probe, selecting the unique letter
`P_+` along `n` should make reverse and face hold, or should adopt that
letter as Admissibility content.

**Answer:** The named construction assigns unique letter `+` at every probe
with `n ≠ 0`. Reverse needs `L(B)=−` and face needs `L(D)=−`. Both fail.
The bit remains displayed. Incoming uniqueness is not required.

### N8 — cross-cycle echo

A prior display assigned both named rank-1 letters `{+,−}` whenever `n ≠ 0`
on these four nnseed probes and reported reverse `some` and face `some`.
This note is not that display: it names only `P_+` along `n` and reports
`none` / `none`. A second prior display scored named rank-1 PVM letters on
the one-site perpnn process without reading occupancy-kernel `n`, and
reported `UNDEFINED`. This note reads `n` on the two-site nnseed process.

**Gate disposition:** PASS for the unique-`P_+`-along-`n` reverse/face
reports above. FAIL / DO NOT SHIP for “the PVM letter equals the incoming
step sign,” “letters are Admissibility,” “letters feed `n`,” “minus is also
assigned,” or “reverse/face holds on all combinations.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-site perp-step
incoming-lock process, computes the formdraw occupancy kernel `n` from
already-recorded six-neighbor occupancy at each probe's formation tick,
reconstructs the named rank-1 projector `P_+` as displayed data, reads the
unique process-determined letter `+` at the four probes, and checks Theorems
1--3. It also checks that incoming steps are not PVM letters, that letters
are not fed into occupancy `n`, that minus is not assigned, and that the
occupancy-kernel formation member is not attached. No runner cache is written.
