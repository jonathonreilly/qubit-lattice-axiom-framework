# The Kappa Flow Class Is the Formation Weight in Flow Coordinates (Bounded Theorem)

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note adopts no
premise and sets no audit outcome.
**Primary runner:**
[`scripts/frontier_kappa_formation_weight_2026_07_12.py`](../scripts/frontier_kappa_formation_weight_2026_07_12.py)
**Runner cache:**
[`logs/runner-cache/frontier_kappa_formation_weight_2026_07_12.txt`](../logs/runner-cache/frontier_kappa_formation_weight_2026_07_12.txt)

> **VERDICT (bounded):** On the positive interior fixed-point surface, the
> relocation coordinate
> `r = (1-w)/(2w)` and the flow-class coordinate `r_* = 1/kappa` give the exact
> bijection `kappa = 2w/(1-w)`, equivalently `w = kappa/(2+kappa)`. Thus the
> kappa bookkeeping residual and the formation/equipartition residual are one
> scalar object in two coordinates. This does not select that object. Moreover,
> direct agreement-conditioned i.i.d. composition of the *same* formation
> weights `(w,1-w)` induces only `r -> 2r^2`; a general-kappa flow requires the
> separate odds identification `(1-q)/q = kappa r`. The independent-composition
> statistics atom is named, not derived.

## Scope and supplied surfaces

This note intersects two conditional coordinate surfaces and one conditional
menu classification. The
[`kappa flow-class theorem`](KOIDE_KAPPA_BOOKKEEPING_FLOW_CLASS_FIXED_POINT_INVERSION_AND_LANE_SCOPING_BOUNDED_THEOREM_NOTE_2026-07-11.md)
supplies, at its own declared bounded grade, the supplied
agreement-conditioned mechanism, the T1 odds map `x -> x^2` with
`x = kappa r`, the T2 `kappa=1,2` coefficient evaluations, and the T3
conditional positive-fixed-point inversion `r_* = 1/kappa`; its comparators
remain report-only. The
[`formation-gate relocation theorem`](KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md)
supplies, at its own declared Residual Atom 2 grade, the energy dictionary

```text
r = (1-w)/(2w),        0 < w < 1,
```

on the two-cell registrable menu, with `w` the singlet-cell formation weight.
The
[`formation-weight classification theorem`](KOIDE_FORMATION_WEIGHT_LAW_EXPRESSIBILITY_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md)
classifies `{1/3,1/2}` only conditionally on its note-owned Supplied-Object
Canonical-Measure Licensing Criterion (SOCMLC), at its declared bounded grade.
The Record axiom says that records form; the minimal axioms expressly leave the
formation rule, including its weight, outside axiom content. Nothing here
derives a formation law, a value of `w`, a bookkeeping convention, or a
persistence dynamics.

## T1 — exact coordinate identity and the discrete image

### Statement

On the positive interior fixed-point surface,

```text
r = (1-w)/(2w),        r = r_* = 1/kappa
```

imply exactly

```text
kappa = 2w/(1-w),      w = kappa/(2+kappa).
```

Consequently the image of the SOCMLC-conditional classified menu is

```text
w = 1/2  <->  kappa = 2  <->  r_* = 1/2,
w = 1/3  <->  kappa = 1  <->  r_* = 1.
```

This is a coordinate image of the classification theorem's conditional menu,
not an independent proof of its completeness or a selection of either cell.

### Exact proof

For `0 < w < 1`, the relocation coordinate is positive. Substitution into the
nonzero fixed-point identity gives

```text
kappa = 1/r = 1 / ((1-w)/(2w)) = 2w/(1-w).
```

Solving the last equality for `w` gives `w = kappa/(2+kappa)`. Both maps are
well-defined and inverse on the positive domains.

The runner derives the two menu weights from their defining equal-share laws,
not from endpoint literals. Counting on the two registrable cells solves
`w = 1-w`. Restriction of carrier-direction counting, with one singlet
direction and two doublet directions, solves `w/1 = (1-w)/2`. Substitution of
those symbolic solves into the coordinate maps yields the displayed triples.

The kappa companion's fixed-point arithmetic is also reproduced rather than
assumed: solving `kappa r^2 = r` on the positive branch gives `r_* = 1/kappa`,
substitution gives `kappa r_*^2 = r_*`, and differentiation gives multiplier
`2`. The endpoint triples above therefore compose with that companion's own
fixed-point calculation at its declared grade.

## T2 — one residual object, with the remaining atoms exposed

Under the two named identifications—Residual Atom 2's energy dictionary and
the positive interior fixed-point relation—the formation weight is a complete
coordinate for all three quantities:

```text
w  <->  r = (1-w)/(2w)  <->  kappa = 2w/(1-w).
```

Therefore “equipartition/dial residual” and “kappa bookkeeping residual” do not
name two independently adjustable scalars on this intersection. They name the
single formation weight `w`. This is residual compression only: changing
coordinates neither supplies nor prefers its value.

The lane ledger compresses as follows:

| item | disposition at this note's scope |
|---|---|
| K-tied measure branch | supplied by the records-only reconstruction at its declared grade, as reported by the relocation theorem |
| measure/formation grain separation | relocated by the formation-gate companion |
| conditional classified menu | consumed from the formation-weight classification theorem only at its bounded SOCMLC-conditional grade; not reproved here |
| kappa bookkeeping scalar | identified here as the flow coordinate of `w` on the fixed-point surface |
| remaining residue | the selection conditionals, plus the independent-composition statistics atom needed to interpret the flow as repeated registrations |

The first four rows do not discharge either remaining item. In particular,
knowing the conditional menu would still not choose a member, and a static coordinate
identity would still not prove the statistics of repeated formation events.

## T3 — the exact agreement-conditioned bridge

### The named premise

The **independent-composition statistics atom** is:

> Two registrations compose as independent draws of the same formation law,
> after which one conditions on agreement.

This is the kappa theorem's own agreement-conditioned double-registration
scope. This note names it locally as the irreducible statistics residual. It
is not a consequence of the Record axiom and is not discharged here.

### What direct composition actually gives

Let the per-registration cell probabilities be literally the formation state
`(p_s,p_d) = (w,1-w)`. For two i.i.d. draws conditioned on agreement,

```text
D    = w^2 + (1-w)^2,
p_s' = w^2/D,
p_d' = (1-w)^2/D.
```

Writing the cell odds as `y = p_d/p_s = (1-w)/w`, normalization cancels and
`y' = p_d'/p_s' = y^2`. The relocation energy dictionary is exactly
`r = y/2`, so applying the same dictionary after composition gives

```text
r' = y'/2 = y^2/2 = 2r^2.
```

Thus i.i.d. composition of the same formation law reproduces the kappa flow
only for `kappa = 2`. It does **not** produce the variable coefficient
`kappa = 2w/(1-w)` for arbitrary `w`.

### What a general-kappa composition requires

For a general member of the kappa class, let `(q,1-q)` be the probabilities
used by the registration composition. Exact reproduction requires the
identification

```text
(1-q)/q = kappa r,
```

and conversion back with `r = ((1-q)/q)/kappa`. Agreement conditioning then
squares those odds and gives

```text
r' = (kappa r)^2/kappa = kappa r^2.
```

If one additionally identifies `q = w` and simultaneously keeps the relocation
dictionary, then `(1-w)/w = 2r`; comparison with `(1-q)/q = kappa r` forces
`kappa = 2` on the positive domain. The fixed-point coordinate formula
`kappa = 2w/(1-w)` agrees with that direct same-weight coefficient only at the
symbolically derived equal-cell point. That intersection is a compatibility
statement, not a derivation or selection of the point.

Equivalently, on the general kappa fixed graph the registration law above has
`q = 1/2` for every positive `kappa`, whereas the relocation coordinate has
`w = kappa/(2+kappa)`. The two weights coincide only at that same derived
intersection; calling them identical away from it would force the bridge.

The exact surviving bridge is therefore:

> The independence atom plus the relocation dictionary sends direct i.i.d.
> composition of the formation state to the `kappa = 2` flow. The full kappa
> family follows from the same odds-squaring mechanism only after separately
> supplying `(1-q)/q = kappa r`. Meanwhile
> `kappa = 2w/(1-w)` is the exact static coordinate identification on the
> positive interior fixed-point surface, not the generic coefficient generated
> by composing `(w,1-w)`.

This also locates the other conditional-menu image honestly: its `kappa = 1` label
is correct on the fixed-point coordinate graph, but direct composition of its
formation weights through the relocation dictionary still belongs to the
`kappa = 2` dynamical member. Reaching the `kappa = 1` flow therefore requires
the distinct count-once odds identification; independence alone does not
supply it.

## T4 — inherited quark-lane scoping

The kappa theorem's T3 comparators are inherited unchanged as report-only
scope. This note does not rederive, import into a derivation, consume, compare,
or threshold any numerical quark-lane kappa value. No quark comparator supports
the coordinate theorem, the residual compression, or the composition bridge.

## Honesty boundary

- No value of `kappa`, `w`, or `r` is derived, selected, preferred, or adopted.
- The menu is classified only conditionally on SOCMLC at the classification
  theorem's bounded grade; this note computes only its exact coordinate image.
- The energy dictionary is consumed only at the relocation companion's
  declared Residual Atom 2 grade.
- The independent-composition statistics atom is named and localized, not
  discharged.
- Labeled comparators are never thresholded and are not proof inputs.
- The direct-composition/fixed-point distinction may not be collapsed: the
  former fixes the coefficient from the odds dictionary, while the latter
  changes coordinates on the stationary surface.
- No status authority, premise adoption, registry action, or lane selection is
  asserted by this note.

## Source ledger

Load-bearing, each consumed only at its own declared grade:

- [Kappa flow-class theorem](KOIDE_KAPPA_BOOKKEEPING_FLOW_CLASS_FIXED_POINT_INVERSION_AND_LANE_SCOPING_BOUNDED_THEOREM_NOTE_2026-07-11.md)
  — T1 supplies the agreement-conditioned odds square, `x = kappa r`, and
  `r -> kappa r^2`; T2 supplies only the `kappa=1,2` coefficient evaluations;
  T3 supplies conditional fixed-point inversion with report-only comparators.
  The agreement mechanism and physical bookkeeping remain supplied
  conditions at that note's bounded grade.
- [Formation-gate relocation theorem](KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md)
  — source of the two-cell formation state and the Residual Atom 2 energy
  dictionary, with both Residual Atoms preserved without renumbering and
  consumed only at their declared source grades.
- [Formation-weight classification theorem](KOIDE_FORMATION_WEIGHT_LAW_EXPRESSIBILITY_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md)
  — source only for the conditional `{1/3,1/2}` menu under its note-owned
  SOCMLC and fixed-menu scope; it supplies no member selection.
- [Minimal framework axioms](MINIMAL_AXIOMS_2026-06-29.md) — source only for
  the Record boundary and the explicit formation-rule open gate.

## Verification

Run:

```bash
python3 scripts/frontier_kappa_formation_weight_2026_07_12.py
```

The runner uses exact SymPy algebra only. It derives both menu weights from
their share laws, derives every endpoint image by substitution, verifies the
kappa companion's fixed-point arithmetic, distinguishes direct same-weight
composition from the general-kappa odds identification, prints numbered
`[PASS]`/`[FAIL]` checks and `TOTAL`, and exits zero exactly when `FAIL=0`.
