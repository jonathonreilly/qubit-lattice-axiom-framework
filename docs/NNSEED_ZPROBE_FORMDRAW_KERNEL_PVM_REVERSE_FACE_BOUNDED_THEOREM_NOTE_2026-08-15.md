---
claim_id: nnseed_zprobe_formdraw_kernel_pvm_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from formdraw occupancy-kernel PVM letters on the four nnseed z-probes, or UNDEFINED, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_zprobe_formdraw_kernel_pvm_reverse_face_2026_08_15.py
---

# Formdraw Occupancy-Kernel PVM Letters On Four Nnseed Z-Probes: Reverse And Face

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** named rank-1 PVM letters in `{+,−}` read from the formdraw occupancy
kernel `n` at the formation tick of the four nnseed z-probes
`A_z=(0,0,1)`, `B=(1,1,1)`, `C_z=(0,0,2)`, `D_z=(0,1,1)` of the displayed
two-site nnseed process, scored as reverse and face. If `n=0` or the named
construction assigns no letter, the comparison is `UNDEFINED`. Both legal
letters `{+,−}` are kept whenever `n≠0`. Uniqueness is not required. This is
not unique `f(n)` on the x-probes and is not ndot. Displayed, not adopted.
This note does not write PVM letters into Admissibility, does not feed letters
into occupancy `n`, and does not attach the occupancy-kernel formation member.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_zprobe_formdraw_kernel_pvm_reverse_face_2026_08_15.py`](../scripts/nnseed_zprobe_formdraw_kernel_pvm_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. Named rank-1 PVM letters are `{+,−}` names of the projectors `P_±`
read from occupancy-kernel `n`. Those two alphabets are not identified.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of formdraw occupancy-kernel n and named rank-1 P_± letters on the four nnseed z-probes, with reverse and face scored as some; uniqueness is not claimed and the letters are not adopted."
trace_class: frontier_discovery
target_claim_id: nnseed_zprobe_formdraw_kernel_pvm_reverse_face
target_blocker_text: "display reverse and face from formdraw occupancy-kernel PVM letters on the four nnseed z-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write letters into Admissibility, do not feed letters into n, and do not identify them with incoming steps."
conditional_surface_status: "exact on B_3(0) for occupancy-kernel PVM letters on the four nnseed z-probes; displayed, not adopted"
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

No larger host is used. The four z-probes are the only sites whose occupancy
kernel and PVM letters are scored:

```text
A_z = (0,0,1),  B = (1,1,1),  C_z = (0,0,2),  D_z = (0,1,1).
```

These are the nsiso z-probe sites. Formation ticks of those sites locate the
already-recorded six-neighbor set. The ticks are not occupancy kernels and
are not the reverse/face scoring.

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

## Named occupancy kernel and rank-1 PVM letter

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
`(a,b,c) = 3n`. Then `H^2 = k I`, and the two legal lock contents are the
rank-1 projectors

```text
P_± = (√k I ± H) / (2√k).
```

The letter `+` names `P_+`. The letter `−` names `P_-`. Both letters are
legal whenever `n ≠ 0`. Occupancy of a formed site remains `1` for either
content, so the letter does not feed `n`.

Those projectors live in the live Qubit presentation `M_2(C)`. They are not
unit nearest-neighbor steps. This note reads `n` at each z-probe's formation
tick as displayed theorem-domain data. It does not attach the occupancy-kernel
formation member: sites form by the nnseed perp-step incoming-lock process,
not by an `n ≠ 0` formation rule.

A process-determined PVM letter at a probe is a value in `{+,−}` assigned by
that named construction from `n`. Incoming `{±e_i}` tags are not that
assignment. Identifying a named sign of an incoming step with a PVM letter
is refused. If a probe has several process-determined letters, reverse and
face are evaluated on every combination. Uniqueness is not required. Both
`{+,−}` at `n≠0` are the letter set; a 16-letter occupancy census independent
of `n` is not taken.

This display is not unique `f(n)` on the x-probes
`A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`, `D=(1,1,0)`. It does not select one
letter as a function of `n` (along `n`, by `sign(n_1)`, or by a maximal
component). It is not ndot: it does not assign a unique letter by the sign of
a contraction `n·v`.

The equality `n(C)=n(D)` is an x-probe fact of the formdraw occupancy kernel
on those x-probes. It is not an input to these z-probes.

Reverse and face (displayed):

```text
reverse  <=>  L(A_z)=+ and L(B)=−
face     <=>  L(C_z)=+ and L(D_z)=−
```

If a letter needed by a comparison is `UNDEFINED`, that comparison is
`UNDEFINED`. The report is one of `all`, `some`, `none`, or `UNDEFINED`.

Admissibility is not edited. PVM letters are not written into Admissibility.

## Theorem 1 — occupancy kernel and PVM letter at each z-probe

Direct enumeration of the displayed nnseed process on `B_3(0)` forms all four
z-probes. Formation ticks are `t(A_z)=t(0,0,1)=1`, `t(B)=t(1,1,1)=2`,
`t(C_z)=t(0,0,2)=4`, `t(D_z)=t(0,1,1)=1`. Those ticks match the nsiso z-probe
formation order and locate the already-recorded set. They are not the
reverse/face kernel.

At each formation tick the occupancy kernel from already-recorded
six-neighbor occupancy is nonzero, so both named rank-1 letters are assigned:

```text
n(A_z) = (0, 0, −1/3),      k(A_z) = 1,     L(A_z) = {+,−}
n(B)   = (−1/3, 0, −1/3),   k(B) = 2,       L(B) = {+,−}
n(C_z) = (0, −1/3, −1/3),   k(C_z) = 2,     L(C_z) = {+,−}
n(D_z) = (0, 0, −1/3),      k(D_z) = 1,     L(D_z) = {+,−}
```

In particular `n(C_z) ≠ n(D_z)`. The x-probe equality `n(C)=n(D)` is not used.

Neighbor occupancies at those formation ticks:

- `A_z`: already recorded on `−e_3`;
- `B`: already recorded on `−e_1` and `−e_3`;
- `C_z`: already recorded on `+e_1`, `−e_1`, `−e_2`, and `−e_3`;
- `D_z`: already recorded on `−e_3`.

Incoming locks exist and need not be unique (`B` has two earliest incoming
steps; `C_z` has three). That non-uniqueness is not a PVM lettering. The PVM
letters are not identified with those incoming steps. Uniqueness is not
required.

On the `k=1` z-probes `A_z` and `D_z`, the named traces are `Tr(ρ P_+)=2/3`
and `Tr(ρ P_-)=1/3`. Both contents occupy the site.

## Theorem 2 — reverse report

Reverse is `L(A_z)=+` and `L(B)=−`. Both probes have letter set `{+,−}`, so
every combination of the four z-probes is scored. There are 16 combinations.
Reverse holds on exactly 4 of them and fails on the other 12.

Report: `some`.

This is not `all`, not `none`, and not `UNDEFINED`. A unique `f(n)` letter, an
ndot contraction letter, a named-sign readout of incoming steps, and a
formation-tick inequality are different objects and are not used.

## Theorem 3 — face report

Face is `L(C_z)=+` and `L(D_z)=−`. Both probes have letter set `{+,−}`. Face
holds on exactly 4 of the 16 combinations and fails on the other 12.

Report: `some`.

Displayed, not adopted. The letters are not written into Admissibility.

## What this note does not claim

- It does not select a unique incoming lock or a unique PVM letter.
- It is not unique `f(n)` on the x-probes.
- It is not ndot.
- It does not import `n(C)=n(D)` from the x-probes.
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

This display uses Lattice to name `B_3(0)` and the four z-probes. It uses Qubit
only as the algebra in which the named projectors `P_±` are written. It uses
Record only as a boundary: a present lock is content. It does not rewrite
Admissibility. The nnseed process, the occupancy kernel, the named PVM
letters, and the reverse/face predicates are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site seed `+e_1/+e_2` |
| occupancy kernel `n` at each z-probe formation tick | Theorem 1; all four `n ≠ 0`; `n(C_z) ≠ n(D_z)` |
| named rank-1 PVM letters `{+,−}` from `P_±` | Theorem 1; `{+,−}` at each z-probe |
| reverse and face | Theorems 2–3; both `some` |
| unique incoming lock or unique PVM letter | not required |
| unique `f(n)` on the x-probes | not this display |
| ndot contraction letter | not this display |
| `n(C)=n(D)` imported from x-probes | not used |
| letters fed into occupancy `n` | not executed |
| occupancy-kernel formation member attached | not attached |
| free occupancy lettering independent of `n` | not enumerated |
| PVM letters as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: formdraw occupancy-kernel PVM letters on the four nnseed z-probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed occupancy-kernel PVM-letter reverse/face report on these four nnseed z-probes. |
| V3 | Occupancy kernels, named projectors, and the `some`/`some` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads `n` at formation and names `P_±`. |
| V5 | It is not an adopted content rule: the letters remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those letters into
Admissibility, does not identify them with incoming steps, does not feed them
into `n`, does not import `n(C)=n(D)` from the x-probes, and is not unique
`f(n)` or ndot. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| identify PVM letter with named sign of incoming `{±e_i}` | map `+e_i` to `+` and `-e_i` to `−` | refused; different alphabet |
| reverse/face from incoming named signs | reuse the incoming-lock sign readout | different object; not this display |
| reverse/face from formation-tick inequalities | score z-probes by nsiso tick order | different object; ticks locate occupancy only |
| unique `f(n)` on the x-probes | assign one letter as a function of `n` | different object; both `{+,−}` are kept |
| ndot contraction letter | unique letter `sign(n·v)` | different object; not ndot |
| import `n(C)=n(D)` from x-probes | copy the nsfrm x-probe kernel equality | refused; `n(C_z) ≠ n(D_z)` |
| free occupancy letters on the four z-probes | ignore `n` and letter independently | different object; not enumerated |
| attach occupancy-kernel formation member | form the probes by `n ≠ 0` instead of perp-step | refused; not attached |
| feed letters into `n` | let `+`/`−` change occupancy | refused; occupancy stays `{0,1}` of the already-recorded set |
| adopt letters into Admissibility | rewrite the local rule by `{+,−}` | refused; displayed, not adopted |
| unique PVM letter required | demand one letter per probe | uniqueness is not required; both letters are kept |

### N2 — wall independence

Missing physical adoption, missing occupancy-kernel formation attachment, and
missing Record identification of the named PVM bits are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `+e_2`, perpendicular step
rule, incoming-step lock, occupancy kernel from already-recorded neighbors,
named `P_±` letters, four z-probes, and reverse/face definitions are declared.
No uniqueness, no occupancy-kernel formation attachment, no Admissibility
rewrite, no unique `f(n)`, no ndot, and no imported `n(C)=n(D)` are silently
assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`some` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each named projector `P_±` and each occupancy component | no continuum alphabet |
| per site | `A_z,B,C_z,D_z` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four `{+,−}` letter sets and two `some` comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{+,−}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Once `n ≠ 0` at a forming z-probe, the site should lock a unique
letter `+` or `−` by unique `f(n)` or by ndot, reverse and face should hold on
all combinations or be adopted as Admissibility content, occupancy should
track that sign, and `n(C_z)` should equal `n(D_z)` because that held on the
x-probes.

**Answer:** The named construction assigns both `P_+` and `P_-` whenever
`n ≠ 0`. Occupancy stays `{0,1}` of the already-recorded set. Reverse and
face hold on some combinations and fail on others. `n(C_z) ≠ n(D_z)`. The
bits remain displayed. Uniqueness is not required. This is not unique `f(n)`
and is not ndot.

### N8 — cross-cycle echo

A prior display scored named rank-1 PVM letters from occupancy-kernel `n` on
the four nnseed x-probes and reported `some` / `some`, including the x-probe
fact `n(C)=n(D)`. This note is not that display: it reads `n` on the four
z-probes, where `n(C_z) ≠ n(D_z)`. A second prior display scored reverse and
face from formation-tick inequalities on the same z-probes. This note does
not reuse that scoring. Unique `f(n)` letterings on the x-probes reported
`none` / `none`; those selectors are not used here.

**Gate disposition:** PASS for the occupancy-kernel PVM-letter reverse/face
reports on the four nnseed z-probes above. FAIL / DO NOT SHIP for “the PVM
letter equals the incoming step sign,” “letters are Admissibility,” “letters
feed `n`,” “unique `f(n)` on the x-probes,” “ndot,” “`n(C)=n(D)` imported
from the x-probes,” or “reverse/face holds on all combinations.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-site perp-step
incoming-lock process, computes the formdraw occupancy kernel `n` from
already-recorded six-neighbor occupancy at each z-probe's formation tick,
reconstructs the named rank-1 projectors `P_±` as displayed data, reads
process-determined PVM letters at the four z-probes, and checks Theorems 1--3.
It also checks that incoming steps are not PVM letters, that letters are not
fed into occupancy `n`, that the occupancy-kernel formation member is not
attached, that `n(C_z) ≠ n(D_z)`, that the scoring is not unique `f(n)` and
not ndot, and that formation ticks match the nsiso z-probe order. No runner
cache is written.
