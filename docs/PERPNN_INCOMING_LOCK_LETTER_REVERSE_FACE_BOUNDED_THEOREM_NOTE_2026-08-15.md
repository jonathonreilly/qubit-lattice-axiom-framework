---
claim_id: perpnn_incoming_lock_letter_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face content-bits from perpnn earliest incoming locks on four probes are reported as all/some/none. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/perpnn_incoming_lock_letter_reverse_face_2026_08_15.py
---

# Incoming-Lock Named Signs: Reverse And Face Hold Reports

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** named signs of earliest incoming locks on four probes inside
`B_3(0)`, scored as reverse and face content-bits. The report is
`hold-on-all` / `some` / `none`. Uniqueness is not required. Displayed, not
adopted. This note does not write locks into Admissibility and does not treat
the bits as a free lettering space.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/perpnn_incoming_lock_letter_reverse_face_2026_08_15.py`](../scripts/perpnn_incoming_lock_letter_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, and the Record
  sentences that records form and that a present record locks exactly one
  admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named probes. Lock letters are unit nearest-neighbor steps. Named
signs are `{+,−}` labels of those steps. They are not a new axiom alphabet.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite incoming-lock sets on four probes, named signs, and reverse/face hold-on-all/some/none reports; uniqueness is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: perpnn_incoming_lock_letter_reverse_face
target_blocker_text: "display reverse and face as named-sign content-bits of earliest incoming locks without adopting them or requiring unique locks"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed as all/some/none; do not write locks into Admissibility and do not require unique incoming locks."
conditional_surface_status: "exact on B_3(0) for named signs of earliest incoming locks on the four probes; displayed, not adopted"
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

No larger host is used. The four probes are the only sites whose incoming
locks are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

Lock alphabet: `{±e_1, ±e_2, ±e_3}`.

Seed: the origin is recorded first with lock letter `+e_1`.

From a recorded site `p` with lock `L(p)=±e_i`, a six-neighbor step `s in NN`
to `q=p+s` is allowed if and only if `s` is perpendicular to `e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s` (the unit vector from `p` to `q`).
If several allowed parents reach `q` at the same earliest formation, each such
incoming step is kept as a possible lock. Uniqueness is not required. A later
parent does not re-form `q`.

Named sign of an incoming lock:

```text
sign(s) = +  if s in {+e_1,+e_2,+e_3},
sign(s) = −  otherwise.
```

If a probe has several earliest incoming locks, reverse and face are evaluated
on every combination of those earliest locks. The report is one of
`hold-on-all`, `some`, or `none`. The bits are not scored from a clock
parameter and are not scored on a free lettering space.

Reverse and face (displayed, as in the four-site letter bits):

```text
reverse  <=>  L(A)=+ and L(B)=−
face     <=>  L(C)=+ and L(D)=−
```

Admissibility is not edited. The process is a displayed Record-like lock on
the six-letter step alphabet, then a named-sign readout of those letters.

## Theorem 1 — earliest incoming locks at the four probes

Direct enumeration of the displayed process on `B_3(0)` yields

```text
locks(A) = {+e_2,-e_2,+e_3,-e_3}
locks(B) = {+e_1,+e_2,+e_3}
locks(C) = {+e_1}
locks(D) = {+e_1}
```

Witness parents (not claimed unique):

- `A` is reached from `(1,1,0)` by `-e_2`, from `(1,-1,0)` by `+e_2`, from
  `(1,0,1)` by `-e_3`, and from `(1,0,-1)` by `+e_3`.
- `B` is reached from `(1,1,0)` by `+e_3`, from `(1,0,1)` by `+e_2`, and from
  `(0,1,1)` by `+e_1`.
- `C` is reached from `A` by `+e_1`. Every earliest lock at `A` is
  perpendicular to `e_1`, so the incoming lock at `C` is `+e_1` in every
  earliest case.
- `D` is reached from `(0,1,0)` by `+e_1`.

Named signs of those lock sets:

```text
sign(locks(A)) = {+,−}
sign(locks(B)) = {+}
sign(locks(C)) = {+}
sign(locks(D)) = {+}
```

The cartesian product of earliest lock sets has

```text
|locks(A)| · |locks(B)| · |locks(C)| · |locks(D)| = 4 · 3 · 1 · 1 = 12
```

combinations. Incoming lock at `A` is not unique. Incoming lock at `B` is not
unique. Uniqueness is not required.

## Theorem 2 — reverse hold report

Reverse is `L(A)=+` and `L(B)=−`. Every earliest lock at `B` lies in
`{+e_1,+e_2,+e_3}`, so `L(B)=+` on every combination. The second conjunct
never holds. Therefore reverse is true on `0` of the `12` combinations.

Report: `none`.

This is not `hold-on-all` and not `some`. Two of the four locks at `A` have
named sign `+`, but reverse still fails because `B` never supplies `−`.

## Theorem 3 — face hold report

Face is `L(C)=+` and `L(D)=−`. The unique earliest lock at `C` is `+e_1`, so
`L(C)=+` on every combination. The unique earliest lock at `D` is `+e_1`, so
`L(D)=+` on every combination. The second conjunct never holds. Therefore
face is true on `0` of the `12` combinations.

Report: `none`.

Displayed, not adopted. The bits are not written into Admissibility.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not score reverse or face from a clock parameter.
- It does not enumerate a free lettering space of the four probes.
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

This display uses Lattice to name `B_3(0)` and the four probes. It uses Record
only as a boundary: a present lock is content. It does not rewrite
Admissibility. The lock alphabet, named signs, and reverse/face predicates
are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; seed lock `+e_1` |
| earliest incoming locks at `A,B,C,D` | Theorem 1 |
| named signs `{+,−}` | declared from `{±e_i}` |
| reverse and face on every earliest combination | Theorems 2–3; both `none` |
| unique incoming lock | not required; `A` has four |
| free lettering space of the four probes | not enumerated |
| locks as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: named signs of earliest incoming locks, reverse/face as `hold-on-all` / `some` / `none`. |
| V2 | Current main has no landed named-sign reverse/face hold report on these four probes. |
| V3 | The lock sets, the twelve combinations, and the two hold reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads a displayed sign of incoming steps on named probes. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the named-sign bits do not force a unique
incoming lock, do not write locks into Admissibility, and do not replace
reverse/face by a clock comparison. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique incoming lock at `A` | require one lock | fails; four earliest incoming steps |
| reverse as `L(A)=+` only | drop the `L(B)=−` conjunct | would be `some` (six of twelve), not `none` |
| face as `L(C)=+` only | drop the `L(D)=−` conjunct | would be `hold-on-all`, not `none` |
| free independent letters on the four probes | ignore the incoming-lock sets | different object; not this display |
| clock comparison | score reverse/face from formation order | different display; not used here |
| adopt locks into Admissibility | rewrite the local rule by `{+,−}` | refused; displayed, not adopted |
| formation mask | let bits choose which sites form | not executed; probes are declared |

### N2 — wall independence

Missing physical adoption, missing unique-lock selector, and missing Record
identification of the named bits are distinct open premises. This note claims
no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, seed lock `+e_1`, perpendicular step rule, incoming-step
lock, named-sign map, four probes, and reverse/face definitions are declared.
No uniqueness and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, content-conditional-on-formation,
and unreadable absence. The residual that formation site, probability, and
rate remain unsupplied is unchanged. The hold reports do not close that
residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each earliest incoming step and its named sign | no continuum alphabet |
| per site | `A,B,C,D` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | twelve combinations and two hold reports | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later unique-lock selector, a separate formation-rate
rule, and a Record content map for reverse/face. None is taken here.

### N7 — hostile steelman

**Steelman:** Earliest incoming locks on four formed probes should pick one
reverse letter and one face letter, and those bits should be adopted as
Admissibility content.

**Answer:** `A` has four earliest incoming locks and `B` has three, so the
display is a combination report, not a unique lettering. Reverse needs
`L(B)=−`, which never occurs among earliest locks at `B`. Face needs
`L(D)=−`, which never occurs. The bits remain displayed. Uniqueness is not
required.

### N8 — cross-cycle echo

A prior formation-order display scored reverse and face as tick comparisons
on the same four probes. This note does not reuse that scoring: it reads
named signs of incoming locks and reports `none` / `none`. The two displays
are distinct objects.

**Gate disposition:** PASS for the incoming-lock named-sign reverse/face hold
reports above. FAIL / DO NOT SHIP for “the incoming lock is unique,” “letters
are Admissibility,” or “reverse/face holds on all combinations.”

## Primary runner

The paired runner builds `B_3(0)`, runs the perp-step incoming-lock process
from the seed, lists earliest incoming locks at the four probes, maps them to
named signs, evaluates reverse and face on every earliest combination, and
checks Theorems 1--3. It also checks that dropping the `L(B)=−` conjunct
changes reverse from `none` to `some`, that uniqueness is not required at
`A`, and that a free lettering space is not enumerated. No runner cache is
written.
