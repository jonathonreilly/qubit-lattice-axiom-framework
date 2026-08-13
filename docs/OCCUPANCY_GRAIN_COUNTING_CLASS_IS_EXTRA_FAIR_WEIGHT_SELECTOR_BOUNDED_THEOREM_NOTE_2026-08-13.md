---
claim_id: occupancy_grain_counting_class_is_extra_fair_weight_selector_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Within the July 16 declared record-influence class the unique interior stationary 2-cell weight is w=1/2, recomputed and not claimed new; the distinct full-support law w=1/3 is allowed by Admissibility and is not that stationary point; the four axioms do not name the class, so they do not select w=1/2 via it; the unadopted map r=(1-w)/(2w) only displays r=1/2 and r=1; occupancy-grain counting is an extra fair-weight selector."
upstream_dependencies:
  - minimal_axioms
  - acphilambda_occupancy_grain_menu_counting_measure_dynamical_static_correspondence_bounded_theorem_note_2026-07-16
runner: scripts/occupancy_grain_counting_class_is_extra_fair_weight_selector_2026_08_13.py
---

# Occupancy-Grain Counting Class Is An Extra Fair-Weight Selector

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact 2-cell weights `(w, 1-w)` with `0 < w < 1`; July 16
record-influence uniqueness recomputed only; class not adopted; dictionary
not adopted; `r = 1/2` not forced.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/occupancy_grain_counting_class_is_extra_fair_weight_selector_2026_08_13.py`](../scripts/occupancy_grain_counting_class_is_extra_fair_weight_selector_2026_08_13.py)

## Result Up Front

The July 16 occupancy-grain correspondence
[`ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md`](ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md)
is a conditional bounded theorem. Its premise weight is quoted only as a
parent boundary:

Premise weight: conditional. Every claim below is conditional on the declared readings named in this note and on the consumed sources at exactly the live grades listed in Load-bearing dependencies.

Within the declared record-influence class that parent states, verbatim,
that every stationary weight is uniform on its support; in particular, the
unique interior stationary weight on a 2-cell menu is `w = 1/2`. The same
parent states, verbatim:

This note selects no menu, weight, horn, or dial value.

This note recomputes the 2-cell uniqueness and does not claim it is new. It
does not adopt the occupancy-grain class.

The current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is quoted
only as a premise and is not edited. These axioms state only their named
primitive content. The four named axioms are Lattice, Qubit, Admissibility,
and Record.

Admissibility names a nearest-neighbor-conditioned distribution and does
not name its values:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

The same memo states that Admissibility does not supply
transition-probability or weight values, and that update laws together with
the distribution's form and values remain outside axiom content. The
distribution's extensional form and values are not specified by this memo.

Record supplies occurrence, lock, content-only readout, and additivity:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`.

Those sentences do not name a continued-registration profile `f`, a
record-influence map `T_f`, occupancy-grain counting, or the equation
`w = 1/2`.

Five exact statements locate the split.

1. **Class uniqueness, recomputed.** On a 2-cell menu the July 16 update is
   `T_f(w) = f(w)/(f(w)+f(1-w))`. For every executed class profile the unique
   interior stationary weight is `w = 1/2`. This is July 16 T1 at `n = 2`,
   not a new classification.
2. **Value-open second law.** The weight `w = 1/3` is a distinct full-support
   2-cell law and is not that stationary point. Admissibility allows both
   values.
3. **Axioms do not name the class.** The four axioms do not name the
   record-influence / occupancy-grain class. They therefore do not select
   `w = 1/2` via that class.
4. **Unadopted dictionary, display only.** Through `r = (1-w)/(2w)`,
   `w = 1/2` maps to `r = 1/2` and `w = 1/3` maps to `r = 1`. The map is
   displayed. It is not adopted. Universal `r = 1/2` is not forced.
5. **Extra selector.** Occupancy-grain counting is an extra selector for a
   fair 2-cell weight. It is not a theorem of Record additivity or of
   Admissibility values.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "July 16 2-cell uniqueness is recomputed by exact Fraction stationarity of T_f; w=1/3 is a distinct full-support law and is not stationary in the class; the axiom memo does not name T_f or occupancy-grain counting; r=(1-w)/(2w) is displayed and not adopted."
trace_class: negative_route_pruning
target_claim_id: occupancy_grain_counting_selects_fair_two_cell_weight
target_blocker_text: "derive a fair 2-cell weight w=1/2 from the four axioms via occupancy-grain counting"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Occupancy-grain counting remains an extra selector for a fair 2-cell weight. Do not adopt the class. Do not force r=1/2. Do not adopt axiom text."
conditional_surface_status: "exact for 2-cell T_f uniqueness at w=1/2, the w=1/3 rejector, axiom non-naming, and the displayed unadopted dictionary; the class is not installed"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work on a declared 2-cell menu with weights

`(w, 1-w)`, `0 < w < 1`.

Both coordinates are then strictly positive, so every such weight has full
support. The open-interval restriction excludes the singleton-support
vertices `(1, 0)` and `(0, 1)`, which July 16 already classifies as
uniform-on-support boundary points.

The **declared record-influence class**, consumed from July 16 and not
adopted here, is the 2-cell family quoted there:

```text
T_f(q) = f(q) / (f(q)+f(1-q)),

f : [0,1] -> [0,1],
f continuous and strictly increasing,  f(0)=0.
```

July 16 additionally declares the share ratio `g(x) := f(x)/x` strictly
increasing on `(0,1]` (its D1). At `n = 2` that operational content
coincides with the consumed L3 complementary-pair sharpening. Executed
class profiles are the power maps `f(x) = x^2` and `f(x) = x^3`, which
July 16 already uses as membership exemplars. They are witnesses of
non-emptiness, not a choice of record rule.

A weight `w` is **interior stationary** for `f` exactly when
`T_f(w) = w`. The identity-gate update is

```text
T_f(w) = f(w) / (f(w) + f(1-w)).
```

July 16 records that the identity family `f(x) = x` is non-recording
dynamics and is therefore a negative control outside that
recording-update hypothesis. That family is used here only as the class
replacement: it is not installed.

The **unadopted energy dictionary**, displayed by July 16 through the
relocation theorem's explicitly unadopted energy dictionary and not
adopted here, is

```text
r = (1-w)/(2w).
```

The current Admissibility reading note is quoted only as a premise. The
distribution concerns which possibility a forming record locks, conditional
on formation at that site; it does not supply the formation site,
probability, or rate. On a finite menu, available possibilities are exactly
those of nonzero probability.

## Exact Target And Obligation Graph

**Exact target.** Recompute that the July 16 class has unique interior
stationary weight `w = 1/2` on a 2-cell menu; exhibit `w = 1/3` as a
different full-support law that is not that point; record that the four
axioms do not name the class; display the unadopted dictionary on those two
weights; and record that occupancy-grain counting is an extra selector.

| Obligation | Role | Disposition |
|---|---|---|
| quote July 16 unique-interior `w = 1/2` and the selects-none clause | premise | quoted; uniqueness recomputed, not claimed new |
| quote July 16 `T_f` class and identity-family negative control | premise | class displayed; not adopted |
| quote Admissibility distribution, value-openness, and update-law residual | premise | quoted; no edit |
| quote Record lock, content-only, and additivity | premise | quoted; no edit |
| unique interior stationary weight of the class is `w = 1/2` | Theorem 1 | recomputed; not new |
| `w = 1/3` is full-support and not stationary | Theorem 2 | exact `T_f(1/3) = 1/5` for `f = x^2` |
| axioms do not name the class | Theorem 3 | needle scan plus residual quotes |
| display `r = (1-w)/(2w)` at `w = 1/2` and `w = 1/3` | Theorem 4 | display only; not adopted |
| occupancy-grain counting is extra | Theorem 5 | not Record additivity, not Admissibility values |
| adopt the occupancy-grain class | non-claim | not attempted |
| force `r = 1/2` | non-claim | falsified at `w = 1/3` |
| edit an axiom | non-claim | no edit |

## Theorem 1 — Unique Interior Stationary Weight Of The Declared Class

**Claim.** Cite July 16 and recompute only: the uniform point `w = 1/2` is
the unique interior stationary weight of the counting/update class that
note declares. This is not claimed as a new classification.

**Proof.** Write `f(x) = x g(x)` on `(0,1]`. For `0 < w < 1` the exact
identity

```text
f(w)(1-w) - w f(1-w) = w(1-w) [ g(w) - g(1-w) ]
```

holds, because both sides expand to the same difference of products. The
left-hand side is the numerator of `T_f(w) - w` up to the positive
denominator `f(w)+f(1-w)`. Hence `T_f(w) = w` if and only if
`g(w) = g(1-w)`.

July 16 D1 takes `g` strictly increasing on `(0,1]`, so `g` is injective.
Then `g(w) = g(1-w)` if and only if `w = 1-w`, if and only if `w = 1/2`.
The vertices `w = 0` and `w = 1` are stationary because `f(0) = 0`, and
they are not interior.

For the executed power profiles `f(x) = x^k` with `k in {2, 3}` one has
`g(x) = x^{k-1}`, which is strictly increasing on `(0,1]`. Direct
evaluation gives `T_f(1/2) = 1/2`. The same identity therefore confines
the interior fixed set to `{1/2}`.

This is July 16 T1 specialized to a 2-cell menu: every stationary weight
is uniform on its support, so the unique interior point is the counting
measure on two cells.

## Theorem 2 — A Different Full-Support Law Is Not That Point

**Claim.** The 2-cell law `w = 1/3` is a full-support weight and is not
the stationary point of Theorem 1. Admissibility allows both `w = 1/2`
and `w = 1/3` (value-open).

**Proof.** The pairs are

`(1/2, 1/2)` and `(1/3, 2/3)`.

These are unequal as ordered pairs of rationals. Each coordinate is
strictly positive, so each law has support of size two. On a finite menu
the Admissibility reading note identifies available with nonzero
probability; both cells are available under either law.

The governing Admissibility sentence names a distribution determined by
nearest-neighbor conditions. It does not equate `1/2` with `1/3`, and the
memo states that the distribution's extensional form and values are not
specified by this memo. Both pairs are therefore permitted 2-cell laws.

For the class exemplar `f(x) = x^2`,

```text
T_f(1/3) = (1/9) / (1/9 + 4/9) = 1/5 ≠ 1/3.
```

Equivalently `g(1/3) = 1/3` and `g(2/3) = 2/3` are unequal, so Theorem 1
already excludes stationarity. For `f(x) = x^3` the same evaluation is
`T_f(1/3) = 1/9 ≠ 1/3`. Thus `w = 1/3` is a legal full-support weight that
is not the July 16 interior stationary point.

## Theorem 3 — The Four Axioms Do Not Name The Class

**Claim.** The four axioms do not name the record-influence /
occupancy-grain class. Therefore they do not select `w = 1/2` via that
class.

**Proof.** The axiom memo names Lattice, Qubit, Admissibility, and Record,
and states that these axioms state only their named primitive content.
The following class-defining phrases of July 16 are absent from the axiom
memo: `record-influence class`, `occupancy-grain`, `T_f(q)`,
continued-registration, and the D1 share-ratio `g(x) := f(x)/x`.

Independently, the memo lists update laws, together with the
distribution's form and values, among the items that remain outside axiom
content. Admissibility is not a dynamics axiom and does not supply
transition-probability or weight values.

Theorem 1 selects `w = 1/2` only after the class is supplied. A class the
axioms do not name is not a route from those axioms to `w = 1/2`. The
predicate that the axioms force `w = 1/2` therefore fails: Theorem 2
keeps `w = 1/3` as a legal full-support weight.

## Theorem 4 — Unadopted Dictionary, Display Only

**Claim.** Through the unadopted dictionary `r = (1-w)/(2w)`,
`w = 1/2` maps to `r = 1/2` and `w = 1/3` maps to `r = 1`. Display only.
Do not adopt the dictionary. Do not force `r = 1/2`.

**Proof.** Direct substitution:

```text
r(1/2) = (1 - 1/2) / (2 · 1/2) = 1/2,
r(1/3) = (1 - 1/3) / (2 · 1/3) = 1.
```

July 16 already displays those two images through the relocation
theorem's explicitly unadopted energy dictionary and selects no dial
value. The same map is displayed here as coordinate arithmetic on the two
executed weights. It is not installed as axiom content, as a formation
law, or as a physical energy split.

The identity

```text
r(w) - 1/2 = (1 - 2w)/(2w)
```

vanishes if and only if `w = 1/2`. In particular `r(1/3) = 1 ≠ 1/2`. The
predicate that the dictionary forces `r = 1/2` therefore fails.

## Theorem 5 — Occupancy-Grain Counting Is An Extra Selector

**Claim.** Occupancy-grain counting is an extra selector for a fair 2-cell
weight. It is not a theorem of Record additivity or Admissibility values.

**Proof.** Fairness on the declared 2-cell menu is the law `w = 1/2`.
Theorem 1 obtains that value only after the July 16 class is supplied:
stationarity of `T_f` plus injectivity of `g` forces uniformity on the
support. That class is an extra rule. Theorem 3 shows the four axioms do
not name it.

Record additivity supplies a scalar `I` on finite pairwise-disjoint
record collections, with `I(empty)=0`. A scalar sum does not name a
2-cell update `T_f` and does not equate `w = 1/2` with `w = 1/3`.

Admissibility names a nearest-neighbor-conditioned distribution and,
by Theorem 2, leaves the values `w = 1/2` and `w = 1/3` open. The memo
states that it does not supply weight values.

Replacing the July 16 class by the claim that all 2-cell laws are
stationary at `1/2` fails on `w = 1/3`. The identity family `f(x) = x`,
already named by July 16 as a negative control outside the
recording-update hypothesis, has `T(w) = w` at every interior weight, so
`w = 1/3` is stationary for that law. Inside the class,
`T_{x^2}(1/3) = 1/5 ≠ 1/3`. The class restriction is load-bearing. It is
displayed; it is not installed.

## Boundary And Non-Claims

The note does not:

- edit an axiom sentence, or argue that an axiom update is necessary;
- adopt the occupancy-grain / record-influence class;
- adopt the energy dictionary `r = (1-w)/(2w)`, or force `r = 1/2`;
- claim that July 16 2-cell uniqueness is a new theorem;
- select a menu, weight, horn, or dial value;
- identify occupancy-grain counting with physical grain, formation
  weighting, or the count-once / count-twice matter-action fork;
- claim that no later selector for `w = 1/2` exists.

The scope is the exact 2-cell split: class uniqueness recomputed,
value-open `w = 1/3`, axiom non-naming, displayed dictionary, extra
selector.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| July 16 unique interior 2-cell weight `w = 1/2`, selects-none clause, `T_f` class | parent | quoted; uniqueness recomputed only |
| July 16 identity-family negative control | class replacement | quoted; not installed |
| July 16 unadopted dictionary `r = (1-w)/(2w)` | display only | not adopted |
| current Admissibility distribution sentence and value residual | premise | quoted; no edit |
| current Record lock, content-only, and additivity sentences | premise | quoted; no edit |
| 2-cell `T_f` algebra, witnesses `1/5` and `1/9`, dictionary images | Theorems 1--4 | computed here |
| physical occupancy-grain compiler | residual | open |

The exact advance is that the July 16 counting class is an extra
fair-weight selector, not an axiom theorem. Independent audit is required.
This note authors no audit verdict.

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | July 16 states that the unique interior stationary weight on a 2-cell menu is `w = 1/2`, that the claim is conditional, and that the note selects no menu, weight, horn, or dial value. The axiom memo leaves update laws and the distribution's form and values outside axiom content. This note executes the residual that the class is extra. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for occupancy-grain counting as an extra fair-weight selector, axioms forcing `w = 1/2` via the record-influence class, and a fair 2-cell weight from the four axioms. Hits: July 16 proves class-conditional uniqueness and selects no weight; later occupancy-grain notes stay inside that class; flavor `r = 1/2` notes are a different object. No landed extra-selector theorem for this class appears on that commit. |
| V3 | Independently checkable? | Textbook two-point stationarity of `T_f(w) = f(w)/(f(w)+f(1-w))` does not mention Record additivity, Admissibility nearest-neighbor conditions, or occupancy grain. The runner recomputes `T_f` and `r = (1-w)/(2w)` by exact `Fraction` arithmetic. |
| V4 | More than a restatement? | Yes. The witnesses `T_{x^2}(1/3) = 1/5 ≠ 1/3` and `r(1/3) = 1 ≠ 1/2`, and the axiom-memo needle scan that the class is unnamed, are not restatements of July 16 uniqueness. |
| V5 | One-step relabel? | No. July 16 uniqueness is class-conditional. Quoting that uniqueness does not by itself prove that the four axioms name the class or force `w = 1/2`. |

## No-Go Discipline Gate (Theorems 3–5 only)

The negative claims are restricted to these three: the four axioms do not
name the record-influence / occupancy-grain class; the unadopted
dictionary does not force `r = 1/2`; occupancy-grain counting is extra
and is not a theorem of Record additivity or Admissibility values. The
gate does not ship a global non-existence theorem against later
selectors.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| force `w = 1/2` from the four axioms | deduce fairness from Lattice, Qubit, Admissibility, or Record | Theorem 3: the axioms do not name the class; Theorem 2 keeps `w = 1/3` legal | **ATTEMPTED** |
| name the class as axiom content | read `T_f`, D1, or occupancy-grain counting off the axiom memo | Theorem 3: those phrases are absent; update laws are listed as outside axiom content | **ATTEMPTED** |
| Record additivity selects fairness | read `w = 1/2` off additivity of `I` | Theorem 5: `I` is a scalar sum, not a 2-cell update | **ATTEMPTED** |
| Admissibility values select fairness | deduce `w = 1/2` from the distribution sentence | Theorem 2: `w = 1/3` remains a full-support law | **ATTEMPTED** |
| adopt the dictionary and force `r = 1/2` | treat `r = (1-w)/(2w)` as axiom content and require `r = 1/2` | Theorem 4: the map is unadopted; `r(1/3) = 1` | **ATTEMPTED** |
| replace the July 16 class by all 2-cell laws | declare every 2-cell law stationary at `1/2` | fails at `w = 1/3`; the identity family has `T(1/3) = 1/3` | **ATTEMPTED** (mutation) |
| axiom-text edit | replace an axiom sentence by a fairness rule | forbidden; no axiom sentence is edited | **ATTEMPTED** (closed as non-route) |

### N2 — wall independence

Theorem 3 closes only the claim that the four axioms already name the
class or force `w = 1/2` through it. Theorem 4 closes only adoption of
the dictionary and universal `r = 1/2`. Theorem 5 closes only the claim
that occupancy-grain counting is already a theorem of Record additivity
or Admissibility values. A later independently justified selector for
`w = 1/2` remains a different wall.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| 2-cell menu `(w, 1-w)` with `0 < w < 1` | declared finite menu |
| July 16 `T_f` class and D1 | displayed parent class; not adopted |
| power exemplars `f = x^2`, `f = x^3` | membership witnesses, not a record rule |
| identity family `f(x) = x` | parent negative control; class replacement |
| unadopted dictionary `r = (1-w)/(2w)` | display only |
| record formation site and rate | open; not assumed |
| physical grain / matter-action fork | open; not identified |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Admissibility distribution sentence; update laws and distribution form/values outside axiom content; Record lock, content-only, and additivity | quoted as premises only; no edit |
| July 16 occupancy-grain correspondence | unique interior 2-cell weight `w = 1/2`; selects no menu or weight; `T_f` class; unadopted dictionary; identity-family negative control | uniqueness recomputed; extra-selector claim is new |

No citation is used as authority for the `T_f(1/3) = 1/5` witness or the
dictionary images; those are proved here and checked by the runner.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | named weights `1/2` and `1/3`, update values `1/5` and `1/9`, dial images `1/2` and `1` | no classification of every 2-cell map |
| per site | one 2-cell menu | no composite bonded-pair theorem |
| per mode | occupancy-grain `T_f` versus axiom sentences | no spectral-mode exhaustion |
| per block | Theorems 3--5 only in this gate: non-naming, unadopted dictionary, extra selector | no formation dynamics or physical grain |
| lattice-wide | checked and not executed | no lattice-wide fair-weight law or universal `r = 1/2` |

The obstruction is per-site / declared 2-cell menu; it is not lattice-wide.

### N6 — live partial-closure paths

1. A later independently justified selector that forces the 2-cell weight
   to `w = 1/2`.
2. A later derivation of the July 16 class from formation dynamics or
   from some other bridge that is not axiom text.
3. A reason to adopt the energy dictionary, which this note does not
   supply, still without forcing `r = 1/2` at every weight.
4. A different menu geometry, including a 3-cell menu, if and when that
   object is constructed from the axioms.

The quoted axiom sentences already name nearest-neighbor conditions,
lock, content-only readout, and additivity. A fair 2-cell weight remains
an open selector. No axiom sentence is edited here. An axiom-text change
is not required by the present split.

### N7 — hostile steelman

> July 16 already proved that the unique interior stationary weight on a
> 2-cell menu is `w = 1/2`, so the axioms have selected fairness.

**Answer.** July 16 uniqueness is conditional on the declared
record-influence class and is paired with the explicit clause that the
note selects no menu, weight, horn, or dial value. The four axioms do not
name that class. Theorem 2 keeps `w = 1/3` as a legal full-support
Admissibility weight. The discriminating facts remain
`T_{x^2}(1/3) = 1/5 ≠ 1/3` and the axiom-memo absence of `T_f`.

### N8 — cross-cycle echo

July 16 T1 classifies stationary weights inside the declared class as
uniform on support. The present residual is not that classification. It
is the extra-selector fact that the class is not axiom content, so
fairness is not selected by Lattice, Qubit, Admissibility, or Record via
occupancy-grain counting.

**Gate disposition.** PASS for the scoped 2-cell split and the negatives
of Theorems 3--5. FAIL / DO NOT SHIP for "the axioms force `w = 1/2`" or
"the occupancy-grain class is adopted."

## Primary Runner

[`scripts/occupancy_grain_counting_class_is_extra_fair_weight_selector_2026_08_13.py`](../scripts/occupancy_grain_counting_class_is_extra_fair_weight_selector_2026_08_13.py)
recomputes `T_f` on the executed class profiles, the `w = 1/3` rejector,
the unadopted dictionary images, and the axiom-memo non-naming scan in
exact `Fraction` arithmetic. Identity gates call `two_cell_update(f, w)`
and `r_of_w(w) = (1-w)/(2w)`. A predicate that the axioms force `w = 1/2`
must fail, because `w = 1/3` remains a legal weight. Replacing the July
16 class by the claim that all 2-cell laws are stationary at `1/2` must
fail on `w = 1/3`.
