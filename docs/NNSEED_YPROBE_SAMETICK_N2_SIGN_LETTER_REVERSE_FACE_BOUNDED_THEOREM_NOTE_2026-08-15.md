---
claim_id: nnseed_yprobe_sametick_n2_sign_letter_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from the unique letter sign(n_2) of the same-tick occupancy kernel on the four nnseed y-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_yprobe_sametick_n2_sign_letter_reverse_face_2026_08_15.py
---

# Unique Letter Sign(n_2) Of Same-Tick Occupancy Kernel On Four Nnseed Y-Probes: Reverse And Face

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** unique letter in `{+,−}` or `UNDEFINED` read as `sign(n_2)` from the
same-tick occupancy kernel `n` at the formation tick of the four nnseed
y-probes `A_y=(0,1,0)`, `B=(1,1,1)`, `C_y=(0,2,0)`, `D_y=(1,1,0)` of the
displayed two-site nnseed process, scored as reverse and face. Occupancy of a
six-neighbor `p` of probe `q` is 1 iff `p` formed at tick `≤ t(q)` and
`p ≠ q`. If `n_2=0`, the unique letter is `UNDEFINED`. Else the unique letter
is `sign(n_2)` in `{+,−}`: `+` iff `n_2>0` and `−` iff `n_2<0`. Uniqueness of
incoming locks is not required. This is not unique `P_+` along `n`, is not
ndot, and is not a sixteen-combination free lettering. Displayed, not
adopted. This note does not write the unique letter into Admissibility, does
not feed letters into occupancy `n`, and does not attach the occupancy-kernel
formation member.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_yprobe_sametick_n2_sign_letter_reverse_face_2026_08_15.py`](../scripts/nnseed_yprobe_sametick_n2_sign_letter_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. The unique letter is a `{+,−}` name of `sign(n_2)`, or `UNDEFINED`.
Those two alphabets are not identified.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of same-tick occupancy-kernel n and unique letter sign(n_2) or UNDEFINED on the four nnseed y-probes, with reverse scored as none and face scored as UNDEFINED; uniqueness of incoming locks is not claimed and the letters are not adopted."
trace_class: frontier_discovery
target_claim_id: nnseed_yprobe_sametick_n2_sign_letter_reverse_face
target_blocker_text: "display reverse and face from unique letter sign(n_2) of the same-tick occupancy kernel on the four nnseed y-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write the unique letter into Admissibility, do not feed letters into n, and do not identify them with incoming steps."
conditional_surface_status: "exact on B_3(0) for unique letter sign(n_2) of the same-tick occupancy kernel on the four nnseed y-probes; displayed, not adopted"
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
kernel and unique letter `sign(n_2)` are scored:

```text
A_y = (0,1,0),  B = (1,1,1),  C_y = (0,2,0),  D_y = (1,1,0).
```

These are the same y-probe sites as the prior occupancy-kernel displays that
kept both `{+,−}` whenever `n≠0`. Formation ticks of those sites locate the
same-tick-inclusive six-neighbor set. The ticks are not occupancy kernels and
are not the reverse/face scoring.

Lock alphabet of the displayed process: `{±e_1, ±e_2, ±e_3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
perp-consistent locks `L(0)=+e_1` and `L(0,1,0)=+e_2`.

`A_y` is the seed site `(0,1,0)`. It is already formed at tick 0. It is not
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

That incoming lock is not occupancy `n` and is not the unique letter
`sign(n_2)`.

## Named same-tick occupancy kernel and unique letter sign(n_2)

At the formation tick of a probe `q`, occupancy of a six-neighbor `p` is 1 if
and only if `p` formed at tick `≤ t(q)` and `p ≠ q`. Same-tick partners count.
The probe itself is excluded. Occupancy is in `{0,1}` and does not depend on
any later unique letter.

`A_y` is a seed. At `t(A_y)=0` the origin is the same-tick partner of `A_y`
and does contribute occupancy.

The named occupancy kernel is the triple

```text
n_μ = (o_{+μ} − o_{−μ}) / 3,     μ = 1,2,3.
```

Write `k = |3n|^2`. If `n_2 = 0`, the named construction assigns no letter and
the probe is `UNDEFINED`. Else the unique letter is `sign(n_2)` in `{+,−}`:
`+` if `n_2 > 0` and `−` if `n_2 < 0`. Occupancy of a formed site remains `1`
for either content, so the letter does not feed `n`.

This note reads `n` at each y-probe's formation tick as displayed
theorem-domain data. It does not attach the occupancy-kernel formation
member: sites form by the nnseed perp-step incoming-lock process, not by an
`n_2 ≠ 0` formation rule.

A process-determined unique letter at a probe is a value in `{+,−}` assigned
by that named construction from `n_2`, or `UNDEFINED`. Incoming `{±e_i}` tags
are not that assignment. Identifying a named sign of an incoming step with
the unique letter is refused. Reverse and face are scored on that unique
letter. They are not scored on a sixteen-combination free lettering of the
four y-probes. Uniqueness of incoming locks is not required.

This display is not unique P_+ along n. A leftover unique letter `P_+`
along `n` is identically `+` at every probe with `n ≠ 0`. Here `n ≠ 0` at all
four y-probes, but `n_2 = 0` at `D_y`, so the unique letter is not identically
`+`. It is not ndot: it does not assign a unique letter by the sign of a
contraction `n·v` for a chosen auxiliary vector.

The prior same-tick occupancy-kernel display on these y-probes kept both legal
letters `{+,−}` whenever `n ≠ 0` and reported reverse/face as `some`. That
both-letter scoring is not reused. The occupancy split on these y-probes is
`n(C_y) ≠ n(D_y)`; the split is n_2 (`−1/3` vs `0`). An x-probe unique-letter
leftover is closed because `n(C)=n(D)` there, so unique `L=f(n)` cannot split
face. These y-probes are not that leftover.

Reverse and face (displayed):

```text
reverse  <=>  L(A_y)=+ and L(B)=−
face     <=>  L(C_y)=+ and L(D_y)=−
```

If a letter needed by a comparison is `UNDEFINED`, that comparison is
`UNDEFINED`. The report is one of `all`, `some`, `none`, or `UNDEFINED`.
Because the unique letter is a single value per probe, the scored comparisons
are not a sixteen-combination free lettering.

Admissibility is not edited. Unique letters are not written into
Admissibility.

## Theorem 1 — occupancy kernel and unique letter at each y-probe

Direct enumeration of the displayed nnseed process on `B_3(0)` forms all four
y-probes. Formation ticks are `t(A_y)=t(0,1,0)=0`, `t(B)=t(1,1,1)=2`,
`t(C_y)=t(0,2,0)=3`, `t(D_y)=t(1,1,0)=1`. Those ticks match the nsiso y-probe
formation order and locate the same-tick-inclusive recorded set. They are not
the reverse/face kernel.

At each formation tick the same-tick occupancy kernel from six-neighbor
occupancy, and the unique letter `sign(n_2)`, are:

```text
n(A_y) = (0, −1/3, 0),         k(A_y) = 1,     L(A_y) = −
n(B)   = (−1/3, −1/3, −1/3),   k(B) = 3,       L(B) = −
n(C_y) = (0, −1/3, 0),         k(C_y) = 1,     L(C_y) = −
n(D_y) = (−1/3, 0, 0),         k(D_y) = 1,     L(D_y) = UNDEFINED
```

In particular `n(C_y) ≠ n(D_y)`. The split is n_2: `n_2(C_y)=−1/3` and
`n_2(D_y)=0` (`−1/3` vs `0`). All four kernels have `n ≠ 0`, so a leftover
unique letter `P_+` along `n` would be identically `+`. That leftover is not
this lettering. Strictly-earlier occupancy at `A_y` is zero; same-tick
occupancy includes the origin partner, so `n(A_y) ≠ 0`.

Neighbor occupancies at those formation ticks:

- `A_y`: same-tick recorded on `−e_2` (the origin partner);
- `B`: same-tick recorded on `−e_1`, `−e_2`, and `−e_3`;
- `C_y`: same-tick recorded on `+e_1`, `−e_1`, `−e_2`, `+e_3`, and `−e_3`;
- `D_y`: same-tick recorded on `−e_1`.

`A_y` carries the seed lock `+e_2`. Incoming locks of the grown sites exist
and need not be unique (`B` has two earliest incoming steps; `C_y` has four).
That non-uniqueness is not a unique-lettering of `sign(n_2)`. The unique
letters are not identified with those incoming steps. Uniqueness is not
required.

## Theorem 2 — reverse report

Reverse is `L(A_y)=+` and `L(B)=−`. The unique letters are `L(A_y)=−` and
`L(B)=−` because `n_2<0` at both probes. Both needed letters are defined. The
predicate fails.

Report: `none`.

This is not `all`, not `some`, and not `UNDEFINED`. Unique `P_+` along `n`
would also score reverse as `none` because every `n ≠ 0` letter is `+`, but
that leftover is identically `+` at all four probes and is not this lettering.
An ndot contraction letter, a named-sign readout of incoming steps, and a
formation-tick inequality are different objects and are not used. A
sixteen-combination free lettering is a different object and is not used.
Strictly-earlier occupancy would leave `n_2(A_y)=0` and score reverse as
`UNDEFINED`. Same-tick occupancy is what makes reverse `none`.

## Theorem 3 — face report

Face is `L(C_y)=+` and `L(D_y)=−`. The unique letters are `L(C_y)=−` and
`L(D_y)=UNDEFINED` because `n_2(D_y)=0`. A needed letter is `UNDEFINED`.

Report: `UNDEFINED`.

This is not `all`, not `some`, and not `none`. Unique `P_+` along `n` would
score face as `none` because every `n ≠ 0` letter is `+`. That leftover does
not split face. Displayed, not adopted. The letters are not written into
Admissibility.

## What this note does not claim

- It does not select a unique incoming lock.
- It is not unique `P_+` along `n`.
- It is not ndot.
- It does not identify unique letters with incoming `{±e_i}`.
- It does not feed letters into occupancy `n`.
- It does not attach the occupancy-kernel formation member.
- It does not census a sixteen-combination free lettering independent of
  `sign(n_2)`.
- It does not import `n(C)=n(D)` from the x-probes.
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
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
nnseed process, the same-tick occupancy kernel, the unique letter `sign(n_2)`,
and the reverse/face predicates are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site seed `+e_1/+e_2` |
| same-tick occupancy kernel `n` at each y-probe formation tick | Theorem 1; all four `n ≠ 0`; `n(C_y) ≠ n(D_y)` |
| unique letter `sign(n_2)` or `UNDEFINED` | Theorem 1; `−`, `−`, `−`, `UNDEFINED` |
| reverse and face | Theorems 2–3; `none` / `UNDEFINED` |
| unique incoming lock | not required |
| unique `P_+` along `n` | not this display |
| ndot contraction letter | not this display |
| letters fed into occupancy `n` | not executed |
| occupancy-kernel formation member attached | not attached |
| sixteen-combination free lettering independent of `sign(n_2)` | not enumerated |
| unique letters as Admissibility content | not adopted |
| `n(C)=n(D)` imported from x-probes | not used |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: unique letter `sign(n_2)` of the same-tick occupancy kernel on the four nnseed y-probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed unique-letter `sign(n_2)` reverse/face report on these four nnseed y-probes with same-tick occupancy. |
| V3 | Occupancy kernels, unique letters, and the `none`/`UNDEFINED` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads `n_2` at formation and names `sign(n_2)`. |
| V5 | It is not an adopted content rule: the letters remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those letters into
Admissibility, does not identify them with incoming steps, does not feed them
into `n`, is not unique `P_+` along `n`, and is not ndot. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| identify unique letter with named sign of incoming `{±e_i}` | map `+e_i` to `+` and `-e_i` to `−` | refused; different alphabet |
| reverse/face from incoming named signs | reuse the incoming-lock sign readout | different object; not this display |
| reverse/face from formation-tick inequalities | score y-probes by formation order | different object; ticks locate occupancy only |
| unique `P_+` along `n` | assign `+` whenever `n ≠ 0` | different object; identically `+` at these four y-probes; face would be `none` |
| ndot contraction letter | unique letter `sign(n·v)` | different object; not ndot |
| unique letter `sign(n_1)` | assign `sign(n_1)` | different object; `n_1(A_y)=0` while `n_2(A_y)≠0` |
| both named occupancy-kernel letters | keep `{+,−}` whenever `n ≠ 0` | different object; both-letter `some` scoring is not reused |
| strictly-earlier occupancy | occupy only neighbors with tick `< t(q)` | different object; that leftover leaves `n(A_y)=0` and reverse `UNDEFINED` |
| sixteen-combination free letters on the four y-probes | ignore `n_2` and letter independently | different object; not enumerated |
| import `n(C)=n(D)` from x-probes | copy the x-probe kernel equality | refused; `n(C_y) ≠ n(D_y)` |
| attach occupancy-kernel formation member | form the probes by `n_2 ≠ 0` instead of perp-step | refused; not attached |
| feed letters into `n` | let `+`/`−` change occupancy | refused; occupancy stays `{0,1}` of the same-tick-inclusive recorded set |
| adopt letters into Admissibility | rewrite the local rule by `{+,−}` | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; both earliest incoming steps at `B` are kept |

### N2 — wall independence

Missing physical adoption, missing occupancy-kernel formation attachment, and
missing Record identification of the unique letter bits are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `+e_2`, perpendicular step
rule, incoming-step lock, occupancy kernel from same-tick-inclusive neighbors
with the probe excluded, unique letter `sign(n_2)`, four y-probes, and
reverse/face definitions are declared. No uniqueness of incoming locks, no
occupancy-kernel formation attachment, no Admissibility rewrite, no unique
`P_+` along `n`, no ndot, and no sixteen-combination free lettering are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`none` and `UNDEFINED` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unique letter `sign(n_2)` | no continuum alphabet |
| per site | `A_y,B,C_y,D_y` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four unique letters and `none`/`UNDEFINED` comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{+,−}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Once `n ≠ 0` at a forming y-probe, the site should lock a unique
letter `+` by unique `P_+` along `n`, reverse and face should hold on all
combinations or be adopted as Admissibility content, occupancy should track
that sign, `n_2=0` should still receive `+` because `n ≠ 0`, and same-tick
occupancy should be refused because a seed partner is not already-recorded.

**Answer:** Same-tick occupancy includes the origin partner, so `n(A_y) ≠ 0`.
The named construction assigns `UNDEFINED` whenever `n_2=0`, even if `n ≠ 0`.
Occupancy stays `{0,1}` of the same-tick-inclusive recorded set. Reverse is
`none`. Face is `UNDEFINED`. The bits remain displayed. Uniqueness of incoming
locks is not required. This is not unique `P_+` along `n` and is not ndot.

### N8 — cross-cycle echo

A prior display scored both named occupancy-kernel letters `{+,−}` on these
four nnseed y-probes from strictly-earlier occupancy and reported reverse
`UNDEFINED` because `n(A_y)=0` with face `some`. A second prior display scored
the same both-letter construction from same-tick occupancy and reported
reverse/face as `some`/`some`, with `n(C_y) ≠ n(D_y)`. This note is not those
displays: it reads the unique letter `sign(n_2)` of the same-tick occupancy
kernel. A leftover unique letter `P_+` along `n` is identically `+` at
`n ≠ 0` and would score reverse/face as `none`/`none`. That leftover is not
used here. An x-probe unique-letter leftover is closed because `n(C)=n(D)`
there, so unique `L=f(n)` cannot split face. These y-probes split: reverse is
`none` and face is `UNDEFINED`.

**Gate disposition:** PASS for the unique-letter `sign(n_2)` reverse/face
reports on the four nnseed y-probes above. FAIL / DO NOT SHIP for “the unique letter equals the incoming step sign,” “letters are Admissibility,” “letters feed `n`,” “unique `P_+` along `n`,” “ndot,” or “reverse/face holds on all combinations.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-site perp-step
incoming-lock process, computes the occupancy kernel `n` from same-tick-
inclusive six-neighbor occupancy at each y-probe's formation tick with the
probe excluded, reads the unique letter `sign(n_2)` at the four y-probes, and
checks Theorems 1--3. It also checks that incoming steps are not unique
letters, that letters are not fed into occupancy `n`, that the occupancy-
kernel formation member is not attached, that `n(C_y) ≠ n(D_y)`, that the
scoring is not unique `P_+` along `n` and not ndot, that same-tick occupancy
includes the seed partner at `A_y`, and that formation ticks match the
displayed y-probe order. No runner cache is written.
