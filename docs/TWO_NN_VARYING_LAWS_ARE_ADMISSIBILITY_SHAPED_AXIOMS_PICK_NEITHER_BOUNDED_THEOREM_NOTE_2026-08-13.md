---
claim_id: two_nn_varying_laws_are_admissibility_shaped_axioms_pick_neither_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On one center site with binary menu {A,B} and occupancy coarse-grain n of the six nearest-neighbor records, two distinct full-support-on-interior laws mu1(A|n) and mu2(A|n) are each functions of nearest-neighbor data and each vary with n. Both therefore fit the current Admissibility shape. The four axioms name neither function, adopt neither as a physical law, and do not force mu(A)=1/2 at every n. The result does not claim that no later selector exists."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_nn_varying_laws_are_admissibility_shaped_axioms_pick_neither_2026_08_13.py
---

# Two NN-Varying Laws Are Admissibility-Shaped; Axioms Pick Neither

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact one-site occupancy coarse-grain of the six nearest-neighbor
conditions; function-selection only.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_nn_varying_laws_are_admissibility_shaped_axioms_pick_neither_2026_08_13.py`](../scripts/two_nn_varying_laws_are_admissibility_shaped_axioms_pick_neither_2026_08_13.py)

## Result Up Front

Admissibility supplies one fixed nearest-neighbor rule and requires that, for
each site, the probability distribution over the possibilities is determined
by, and varies with, the nearest-neighbor conditions. That sentence constrains
the *type* of the law. It does not name the extensional function.

Two explicit occupancy laws on the same window both fit the type and disagree
at a legal interior point. Neither is adopted as a physical law. The uniform
value `mu(A)=1/2` is not forced: `mu1(A|2)=1/3` is a legal value of a
varying nearest-neighbor law. A later selector is not ruled out.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Two explicit occupancy laws are proved to vary with a nearest-neighbor coarse-grain and to disagree, while Admissibility names the type and not the function; adoption as a physical law, a universal half-weight, and nonexistence of a later selector remain outside the claim."
trace_class: negative_route_pruning
target_claim_id: admissibility_nn_rule_extensional_function
target_blocker_text: "determined by and varies with the nearest-neighbor 6-tuple does not select the function"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed occupancy pair and the axiom-type reading; later selectors remain open"
hypothetical_axiom_status: "no edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Fix one center site. The local menu is the two-point set `{A,B}`. The six
nearest-neighbor sites of the cubic lattice are the condition window. Let
`n in {0,1,...,6}` be the number of those neighbor sites locked to a declared
label `A`. This `n` is a coarse-grain of the nearest-neighbor 6-tuple: every
value of `n` is realized by some 6-tuple, and distinct 6-tuples may share a
value of `n`.

A binary occupancy law is a function

`mu(A|n) in [0,1]`, `mu(B|n)=1-mu(A|n)`.

The first displayed law is piecewise

`mu1(A|0)=1/2`, `mu1(A|n)=n/6` for `n=1,...,6`.

So `mu1(A|1)=1/6`, `mu1(A|2)=1/3`, `mu1(A|6)=1`. The `n=0` clause is full
support on `{A,B}`; without it the occupancy fraction would be `0`. At `n=6`
the same occupancy fraction is certain `A`.

The second displayed law is

`mu2(A|n)=(n+1)/8` for `n=0,...,6`.

So `mu2(A|0)=1/8`, `mu2(A|1)=2/8=1/4`, `mu2(A|2)=3/8`, `mu2(A|6)=7/8`. Every
value lies in `{1/8,...,7/8}` and is therefore neither `0` nor `1`.

A discarded alternative `1/(1+n)` also varies with `n`, but at `n=0` it is
certain `A`. It is not used below. The displayed `mu2` is the full-support
replacement.

Neither `mu1` nor `mu2` is adopted as a physical law. They are witnesses that
the Admissibility type is inhabited by more than one function.

## Exact Target And Obligation Graph

**Exact target.** Decide whether the current Admissibility wording, read on
this occupancy coarse-grain, selects one extensional function of `n`.

| Obligation | Role | Disposition |
|---|---|---|
| exhibit one law that varies with `n` | type inhabitance | [Theorem 1](#theorem-1--both-laws-vary-with-n) for `mu1` |
| exhibit a second law that varies with `n` | type inhabitance | [Theorem 1](#theorem-1--both-laws-vary-with-n) for `mu2` |
| show the two laws disagree | non-uniqueness | [Theorem 2](#theorem-2--the-two-laws-disagree) at `n=2` |
| quote the axiom type and observe that it names neither function | axiom reading | [Theorem 3](#theorem-3--admissibility-names-the-type-not-the-function) |
| refuse adoption and refuse a universal half-weight | claim boundary | [Theorem 4](#theorem-4--display-both-adopt-neither-do-not-force-a-universal-half-weight) |
| refuse a nonexistence claim about later selectors | claim boundary | [Theorem 5](#theorem-5--a-later-selector-is-not-ruled-out) |

The occupancy coarse-grain is load-bearing for the witnesses and is not a
claim that Admissibility reduces to a function of `n` alone. A law of the
full 6-tuple remains inside the axiom type. That larger domain still does
not, by itself, name one function.

## Theorem 1 — Both Laws Vary With `n`

Direct evaluation of the displayed formulas gives

`mu1(A|1)=1/6`, `mu1(A|2)=1/3`.

These are unequal, so `mu1` varies with `n`. The same evaluation gives

`mu2(A|1)=2/8=1/4`, `mu2(A|2)=3/8`.

These are unequal, so `mu2` varies with `n`.

Each law is a function of a nearest-neighbor coarse-grain. Combined with
variation, both inhabit the Admissibility type on this window.

## Theorem 2 — The Two Laws Disagree

At the common interior point `n=2`,

`mu1(A|2)=1/3` and `mu2(A|2)=3/8`.

These fractions are unequal: `1/3=8/24` and `3/8=9/24`. Therefore `mu1` and
`mu2` are distinct laws. A predicate that they are the same function fails at
`n=2`.

## Theorem 3 — Admissibility Names The Type, Not The Function

The current Admissibility axiom states that there is one fixed nearest-neighbor
admissibility rule, covariant under lattice translations and proper cubic
rotations, and that for each site the probability distribution over the
possibilities is determined by, and varies with, the nearest-neighbor
conditions.

Both `mu1` and `mu2` are functions of a nearest-neighbor coarse-grain and both
vary with that coarse-grain. The axiom sentence is therefore satisfied by
either witness. The same memo states that the distribution's extensional form
and values are not specified by the axiom text, and that a choice not fixed by
the supplied structure remains a named conditional or open dependency.

The axiom does not name `mu1` versus `mu2`.

## Theorem 4 — Display Both; Adopt Neither; Do Not Force A Universal Half-Weight

The two laws are displayed as type-inhabiting witnesses. This note
does not adopt either as `L_phys`. Neither witness is a physical law.

The note also does not force `mu(A)=1/2` at every `n`. The value
`mu1(A|2)=1/3` is a legal value of a varying nearest-neighbor law. A predicate
that the axioms force `mu(A)=1/2` for all `n` therefore fails at `n=2`.

No ratio dictionary is introduced, and `r=1/2` is not forced.

### N5 — resolution and rhetoric audit (Theorem 4)

Theorem 4 is a display-and-boundary statement, not a selection of values.

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | the two displayed functions of `n`, evaluated at `n=1` and `n=2` | no classification of every function of the full 6-tuple |
| per site | one center site with menu `{A,B}` | no composite, multi-site, or formation-site theorem |
| per mode | occupancy classes `n=0,...,6` as a coarse-grain of the six nearest neighbors | no spectral-mode or harmonic exhaustion |
| per block | function-selection and non-adoption; `mu1(A|2)=1/3` is legal | no adoption of `L_phys`, no universal half-weight, no ratio dictionary |
| lattice-wide | covariance is the axiom's already-named constraint on the *rule*, not a unique value table | no lattice-wide dynamics, gravity, or Laplacian claim |

Rhetoric that "the axioms pick a fair coin," "the axioms pick `mu1`," or "the
axioms pick `mu2`" is outside this resolution. Rhetoric that "no physical law
can ever be selected" is likewise outside this resolution; see Theorem 5.

## Theorem 5 — A Later Selector Is Not Ruled Out

Nothing above claims that no later selector exists. Extra derived structure,
an approved primitive, a finer reading of the 6-tuple, or a later bridge could
still name one function. The present result is only that the current four
axiom sentences, read on this window, do not already do so.

## No-Go Discipline Gate

The negative claims are restricted to: (i) non-uniqueness of the displayed
occupancy pair, (ii) the axiom text not naming that pair, (iii) non-adoption
of either witness as a physical law, and (iv) failure of a universal
half-weight. The gate does not certify that no selector can exist.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Unique-function reading | treat "determined by" as naming one extensional map | Theorems 1--3: two distinct varying maps inhabit the type | **ATTEMPTED** |
| Occupancy-fraction `n/6` | take `mu1` as forced | Theorem 2: `mu2` is another varying law; Theorem 3: the axiom does not name `mu1` | **ATTEMPTED** |
| Universal half-weight | set `mu(A|n)=1/2` for every `n` | fails the vary clause at distinct `n`, and `mu1(A|2)=1/3` remains legal | **ATTEMPTED** |
| Inverse-count `1/(1+n)` | take the discarded alternative as forced | not used; `n=0` is certain `A`, and the axiom still names no values | **ATTEMPTED** |
| Record additivity | lift scalar readout additivity to a unique menu weight | Record names locking and additive readout of disjoint records, not nearest-neighbor values | **ATTEMPTED** |
| Cubic covariance as a value table | treat translation/rotation covariance as selecting `mu(A|n)` | covariance constrains the *rule* to be a nearest-neighbor covariant law; it does not pick `mu1` versus `mu2` | **ATTEMPTED** |
| Later selector | derive or register a function from extra structure | [Theorem 5](#theorem-5--a-later-selector-is-not-ruled-out) keeps the route live | **LIVE** |

The broad statement "the axioms can never select a nearest-neighbor law" is
not shipped.

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| type inhabitance / numerical disagreement | no: many distinct functions can vary | no: disagreement does not by itself quote the axiom | independent |
| type inhabitance / non-adoption | no: displaying a type-fit is not adoption | no: refusing adoption does not prove variation | independent |
| disagreement / universal half-weight | no: `1/3 != 3/8` does not mention `1/2` | no: rejecting a constant `1/2` does not separate `mu1` from `mu2` | independent |
| axiom-type reading / later selector | no: "not named now" is not "unlistable later" | no: a future selector would be extra structure | independent |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| menu `{A,B}` | declared finite possibility menu for the center site |
| occupancy count `n` | coarse-grain of the six nearest-neighbor records; not claimed to be the only legal condition |
| `mu1`, `mu2` | displayed witnesses; not axiom content and not adopted as a physical law |
| `L_phys` | unused adoption slot; neither witness is placed in it |
| `r=1/2` | not introduced and not forced |
| "legal value" | means compatible with the axiom type and with `0<=mu<=1`; not an empirical claim |
| observations or fitted frequencies | none |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | one fixed nearest-neighbor rule; distribution determined by and varying with nearest-neighbor conditions; form and values not specified | exact current wording; no function is borrowed |

No other scientific parent is used. The two occupancy formulas and the
fraction comparison `1/3 != 3/8` are proved here and checked by the runner.

### N6 — live partial-closure paths

1. A later derivation could select one covariant function of the full 6-tuple.
2. A later derivation could select a function of occupancy `n` from extra
   structure not present in the four axiom sentences.
3. An approved primitive could name a specific nearest-neighbor law.
4. A retained bridge from Record formation or from a later kinetic structure
   could constrain values without editing an axiom.

None of these paths is closed here. None is claimed exhausted.

### N7 — hostile steelman

> "Determined by the nearest-neighbor conditions" already means there is one
> physical rule. Displaying two formulas only shows that the English sentence
> is loose. Once covariance and a binary menu are read carefully, a unique
> function will drop out, so the axioms do pick a law.

This steelman is accepted as a *program*, not as a present theorem. Covariance
and a binary menu are already on the table, and they still leave both `mu1`
and `mu2` standing. If a later argument names further structure and derives
one function, that argument is the selector. It is not supplied by the current
axiom text.

### N8 — cross-cycle echo

| Earlier surface | Later movement | Echo here |
|---|---|---|
| Admissibility as availability only | August 5 named a genuine nearest-neighbor-varying distribution | the type is now explicit; the function is still unnamed |
| form and values left unspecified | the current axiom memo keeps that residual | Theorems 3--5 repeat the residual rather than filling it |

**Gate disposition:** PASS for (i) both displayed laws vary with `n`, (ii) they
disagree at `n=2`, (iii) the axiom type does not name either function, and
(iv) neither is adopted and a universal half-weight is not forced.
FAIL / DO NOT SHIP for "an axiom update is necessary," "no later selector exists,"
"the axioms force `mu(A)=1/2` for all `n`," or "either displayed law is the
physical law."

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current four axiom sentences | type baseline | supplied; no edit |
| occupancy coarse-grain `n` | witness domain | constructed here |
| `mu1`, `mu2` | type-inhabiting witnesses | constructed here; not adopted |
| later selector | possible extra structure | open |
| `L_phys` | unused adoption slot | not adopted |
| `r=1/2` | unused dictionary | not introduced and not forced |
| observations or fits | none | not used |

## Review Record

The only scientific parent is the current axiom memo. Independent audit
remains required before any effective status may change.
