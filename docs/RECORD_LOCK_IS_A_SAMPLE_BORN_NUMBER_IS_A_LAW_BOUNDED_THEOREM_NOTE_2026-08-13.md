---
claim_id: record_lock_is_a_sample_born_number_is_a_law_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "At one site with finite menu {A,B}, a single Record lock of A is a realized sample: content A and I=1. Two full-support laws mu1(A)=1/3 and mu2(A)=3/5 both admit that same lock and the same pair (content, I). The Born numbers 1/3 and 3/5 are law-level and are not functions of the lock. Quoting 3/5 as the readout of the lock violates the realized-state primitive. The note displays the mismatch; it does not adopt mu as a readout, force r=1/2, or adopt L_phys."
upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
runner: scripts/record_lock_is_a_sample_born_number_is_a_law_2026_08_13.py
---

# A Record Lock Is A Sample; A Born Number Is A Law

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** one site, finite menu `{A,B}`, two full-support laws, one realized
lock of `A`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/record_lock_is_a_sample_born_number_is_a_law_2026_08_13.py`](../scripts/record_lock_is_a_sample_born_number_is_a_law_2026_08_13.py)

Parents, both on `origin/main`:

- [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
- [`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)

## Result Up Front

A Record lock is a sample. A Born number is a law.

Fix one site and the finite menu `{A,B}`. Let `mu1` and `mu2` be the two
full-support laws with

`mu1(A)=1/3`, `mu1(B)=2/3`

and

`mu2(A)=3/5`, `mu2(B)=2/5`.

Let `h` be the history that locks `A`. Record content of `h` is `A`. Scalar
readout is `I(h)=1`.

Both laws admit `h`. The pair `(content, I)` is the same under both. The
law-level numbers `1/3` and `3/5` differ, so they are not functions of `h`.
Quoting `3/5` as the readout of `h` treats a law number as if it were
record content and therefore violates the realized-state primitive. The
mismatch is displayed. The note does not adopt `mu` as a readout, does not
force `r=1/2`, and does not adopt `L_phys`. It does not claim that no later
compiler exists.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The one-site lock is admissible for two distinct full-support laws, the pair (content, I) is the same, and the Born numbers 1/3 and 3/5 are not functions of that lock. Adoption of mu as a readout, a later compiler, r=1/2, and L_phys remain open."
trace_class: negative_route_pruning
target_claim_id: single_lock_carries_born_number
target_blocker_text: "identify a single Record lock with the Born number mu of the locked possibility"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
conditional_surface_status: "exact for the displayed two-law lock; a later compiler from an ensemble or extra dictionary remains open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

One site. Finite local menu

`M={A,B}`.

A **law** on `M` is a probability vector `mu` with `mu(A)+mu(B)=1` and
`mu>=0`. Its **support** is `{X in M: mu(X)>0}`. On a finite menu the
current Admissibility reading takes the admissible possibilities to be
exactly the support.

The two laws used here are the odds-normalized vectors

`mu1 = law_from_odds(1,2)`, so `mu1(A)=1/3`,

`mu2 = law_from_odds(3,2)`, so `mu2(A)=3/5`.

Both have full support on `{A,B}`.

A **history** `h` at the site is a single Record lock of one menu entry.
Write `lock_content(h)` for the locked possibility and `I(h)` for the
additive scalar readout of that finite record collection. The Record axiom
gives `I(empty)=0` and, for one unit lock, `I(h)=1`. Only records are
readable. A readout value is determined by record content alone.

The realized history of this note is the lock of `A`:

`lock_content(h)=A`, `I(h)=1`.

A **Born number** in this note is a law-level value `mu(X)` for a
possibility `X`. It is not a Record readout.

## Exact Target And Obligation Graph

**Exact target.** Decide whether the pair `(lock_content(h), I(h))` of one
realized lock determines the Born number of the locked possibility. If it
does not, display the mismatch and refuse to adopt `mu` as a readout of `h`.

| Obligation | Role | Disposition |
|---|---|---|
| both laws have full support, so `A` is admissible for both | Theorem 1 | proved |
| `(lock_content, I)` is independent of which of the two laws is used | Theorem 1 | proved |
| `1/3 != 3/5`, so the Born number is not a function of `h` | Theorem 2 | proved |
| quoting `3/5` as the readout of `h` is not pointwise evaluation of `h` | Theorem 3 | proved from the realized-state primitive |
| do not adopt `mu` as a readout; do not claim no later compiler exists | Theorem 4 | scoped residual |
| do not force `r=1/2`; do not adopt `L_phys` | Theorem 5 | firewall |

## Theorem 1 — The Same Lock Is Admissible For Both Laws

The current Record wording is: when present, a record locks exactly one
admissible local possibility. On the finite menu `{A,B}`, admissibility is
the support of the law.

Both coordinates of `mu1` and of `mu2` are strictly positive, so both laws
have full support. The lock of `A` is therefore admissible for `mu1` and
for `mu2`.

The Record readout depends on record content alone. The content of `h` is
`A` under either law. Additivity with `I(empty)=0` gives `I(h)=1` under
either law. The pair

`(lock_content(h), I(h)) = (A, 1)`

is therefore the same for both laws.

This is the current axioms' split: the law supplies the odds; the realized
state supplies the pick. One pick of `A` does not name which odds were
used.

## Theorem 2 — The Law-Level Numbers Differ And Are Not Functions Of `h`

Directly from the odds construction,

`mu1(A)=1/3`, `mu2(A)=3/5`,

and

`1/3 != 3/5`.

A function of `h` would assign one number to the pair `(A, 1)`. The two
laws assign two different Born numbers to that same pair. Therefore the
Born number of the locked possibility is not a function of `h`.

The predicate “lock `A` determines `mu(A)`” fails on this pair of laws.

## Theorem 3 — Quoting `3/5` As The Readout Of `h` Violates The Primitive

The realized-state primitive licenses one operation: evaluate pointwise at
the realized state. Nothing more is supplied: no averaging over
alternatives, no typical or generic claim, and no quoting a number that
would differ had another law-admissible state been realized.

The pointwise readout of `h` is the pair `(A, 1)`. That pair does not
include `3/5`.

A Born number depends on the law, not on the single lock. The same lock
`h` is law-admissible under `mu1`, where the Born number of `A` is `1/3`,
and under `mu2`, where it is `3/5`. Quoting `3/5` as the readout of `h`
therefore quotes a number that is not determined by the realized state and
that would differ under another law for which this same state is
admissible. That is not pointwise evaluation of `h`. It violates the
primitive.

The primitive's complementary clause is the same split: a value that would
change under a different law-admissible realized state is registered data,
not derivation output. Here the change is even earlier: the quoted number
already changes when the law changes and the realized lock is held fixed.
It is law data, not a readout of `h`.

## Theorem 4 — Display The Mismatch; Do Not Adopt `mu` As A Readout

The displayed mismatch is exact:

| Object | Value on `h` |
|---|---|
| `lock_content(h)` | `A` |
| `I(h)` | `1` |
| `mu1(A)` | `1/3` |
| `mu2(A)` | `3/5` |

Record content and `I` are the readout. The two Born numbers are not.
This note does not adopt `mu` as a readout of a single lock.

The note does not claim that no later compiler exists. A later construction
might relate an ensemble of locks, or a separately derived dictionary, to a
Born number. That construction would be extra. It is not supplied by one
lock of `A`.

## Theorem 5 — Do Not Force `r=1/2`; Do Not Adopt `L_phys`

The realized-state primitive already records that dial settings
`r=0, 1/2, 1` are sector data, never forced. Nothing in the two-law lock
selects `r=1/2`. Do not force `r=1/2`.

The note does not adopt `L_phys`. It does not adopt a Born axiom. It does
not edit the four named axioms.

## No-Go Discipline Gate

The negative claims are restricted to the identification of one Record lock
with a Born number. The gate does not certify that no compiler from extra
structure can exist.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Read `mu(A)` off one lock of `A` | use `h` alone | Theorems 1–2: the same `(A,1)` sits under `1/3` and under `3/5` | **ATTEMPTED** |
| Quote `3/5` as the readout of `h` | treat the Born number as content or as `I` | Theorem 3: readout is `(A,1)`; `3/5` is law data | **ATTEMPTED** |
| Average the two laws at the lock | replace pointwise evaluation by a mean | the primitive supplies no averaging | **ATTEMPTED** |
| Force `r=1/2` from the sample | read a sector dial off `h` | Theorem 5: the lock does not select `r` | **ATTEMPTED** |
| Adopt `L_phys` or a Born axiom | promote the mismatch to new axiom text | Theorem 4–5: display only; no adoption | **ATTEMPTED** |
| Later ensemble or dictionary compiler | many locks, or an extra map from locks to a law | not tested; remains live | live |

The broad statement “no later compiler exists” is not shipped.

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| lock content / Born number | no: content `A` sits under two laws | no: a law number does not lock a site | independent |
| `I` / Born number | no: `I=1` for any unit lock | no: `3/5` is not a cardinality | independent |
| full-support admissibility / readout pair | no: support only permits the lock | no: `(A,1)` does not name the support weights | independent |
| realized-state evaluation / law data | no: pointwise evaluation of `h` yields `(A,1)` | no: `mu` is not a state functional of `h` | independent |

The sufficient later extra, if any, is a compiler that takes more than one
lock, or a separately derived dictionary. That extra is not counted as a
wall closed here.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| one site, menu `{A,B}` | explicit finite witness |
| `mu1`, `mu2` | two explicit full-support laws; not a classification of all laws |
| `h` | one unit lock of `A` |
| `I` | Record additivity on a one-record collection |
| Born number | law-level `mu(X)`, not a Record readout |
| averaging, typicality, generic sample | excluded by the primitive; not used |
| ensemble of locks | not used; live later route |
| `r=1/2` | firewall only; not derived |
| `L_phys` | named only to refuse adoption |
| observations or empirical frequencies | none |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | one admissible lock; content-only readout; `I` additive with `I(empty)=0`; the law supplies the odds and the realized state supplies the pick; finite-menu support is the nonzero probabilities | exact current wording; no Born readout borrowed |
| [`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) | pointwise evaluation; no averaging; do not quote a number that would differ had another law-admissible state been realized; `r` dials are never forced | used as the evaluation license and the `r` firewall; not as a selector |

No unmerged pull request is cited. The arithmetic `1/3 != 3/5` is proved
here and checked by the runner.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | two menu entries `{A,B}` and two law values at `A` | no classification of every law |
| per site | one site, one lock | no lattice composite |
| per mode | not used | no spectral claim |
| per block | lock-versus-law type split only | no Born-form derivation |
| lattice-wide | not executed | no global history or frequency theorem |

### N6 — live partial-closure paths

1. A later compiler may take an ensemble of locks and a separately derived
   law-identification theorem.
2. A later dictionary may relate Record content to a menu kernel after the
   kernel is itself derived.
3. The two laws may be distinguished by further neighbor data, which this
   one-site lock does not include.

None of those paths is closed here. None is claimed impossible.

### N7 — hostile steelman

> One lock of `A` already tells an observer that `A` occurred, and under a
> known law the Born number of `A` is then known. So the lock carries
> `mu(A)`.

The steelman assumes the law is already known. That is extra input. The
witness is exactly that the same lock is admissible for two different laws.
Once the law is supplied, `mu(A)` is a function of the law, not of the
lock. The lock remains a sample.

### N8 — cross-cycle echo

The current Admissibility wording already separates the distribution (law)
from the realized lock (state). The realized-state primitive already
separates pointwise evaluation from law-level or counterfactual numbers.
This note applies those two separations to the tempting identification of
one lock with a Born number. It does not reopen either parent.

**Gate disposition:** PASS for (i) one lock of `A` is admissible for both
displayed laws, (ii) `1/3 != 3/5` so the Born number is not a function of
the lock, and (iii) quoting `3/5` as the readout of `h` is not licensed.
FAIL / DO NOT SHIP for “no later compiler exists,” “an axiom update is
necessary,” “Born is false,” “force `r=1/2`,” or “adopt `L_phys`.”

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current four axiom sentences | lock, content-only readout, `I`, law-versus-pick | supplied; no edit |
| realized-state primitive | pointwise evaluation license and `r` firewall | supplied; no edit |
| two odds-normalized laws | Theorem 1–2 witness | constructed here |
| one unit lock of `A` | sample | constructed here |
| later compiler, `L_phys`, Born axiom | extras | not adopted |
| observed frequencies | none | not used |

## Review Record

Independent audit remains required before any effective status may change.
No `review-loop` was invoked in producing this artifact.
