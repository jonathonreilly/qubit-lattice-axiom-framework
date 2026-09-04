# Occupancy Grain-Menu Counting-Measure Correspondence over the Declared Record-Influence Class: Bounded Theorem

**Date:** 2026-07-16
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Premise weight:** conditional. Every claim below is conditional on the declared readings named in this note and on the consumed sources at exactly the live grades listed in Load-bearing dependencies. Nothing consumed is upgraded here, and no derivation obligation is discharged here.
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:** [`scripts/acphilambda_occupancy_grain_menu_counting_correspondence_2026_07_16.py`](../scripts/acphilambda_occupancy_grain_menu_counting_correspondence_2026_07_16.py)
**Cache:** [`logs/runner-cache/acphilambda_occupancy_grain_menu_counting_correspondence_2026_07_16.txt`](../logs/runner-cache/acphilambda_occupancy_grain_menu_counting_correspondence_2026_07_16.txt)

## Purpose

This note proves a bounded fixed-point classification over the declared
record-influence class. Within that class, every stationary weight is uniform
on its support; in particular, the unique interior stationary weight on a
2-cell menu is `w = 1/2`, while the unique interior stationary weight on a
3-cell menu is uniform on 3 cells and has singlet weight `w = 1/3`. On the
swap-symmetric 3-cell surface this is the exact aggregated fixed point
`q = 2/3`. The associated dial coordinates, through the explicitly
unadopted energy dictionary, are `r = 1/2` and `r = 1`.

The resulting numerical set `{1/3, 1/2}` equals the static classification's
licensed weight set. That equality is a SET-LEVEL ARITHMETIC CORRESPONDENCE
between independent conditional constructions. The static classification
operates on one fixed singlet/doublet quotient: carrier/orbit multiplicities
give `w = 1/3`, while quotient-atom counting gives `w = 1/2`. It is not a
classification of the dynamical 2-cell and 3-cell menus. No identification of
measure granularity, formation weighting, and dynamical menu is made here;
such an identification is the missing binding theorem preserved by the
formation-gate relocation source. This note selects no menu, weight, horn, or
dial value.

Record ontology throughout: a supplied initialized weight is called durable
exactly when the declared continued-registration update leaves it stationary.
No formation, occurrence, convergence, or pre-record readout is inferred.

## Supplied objects and consumed readings

1. **The declared record-influence class (2-cell form)**, consumed from the
   occupancy-grain rule-class universality note (unaudited `bounded_theorem`).
   That note's declared reading states, verbatim, that

   > "the normalized record influence of a continued-registration rule in that class has the form"

   ```text
   T_f(q) = f(q) / (f(q)+f(1-q)),

   f : [0,1] -> [0,1],
   f continuous and strictly increasing,  f(0)=0.
   ```

   with the recording/non-recording distinction, verbatim: "an admissible
   **continued-registration** rule is a recording update: its off-center
   action strictly amplifies the majority sector in the sense stated in L3.
   The identity family in N2 is non-recording dynamics and is therefore a
   negative control outside that recording-update hypothesis"; the
   symmetric-family reading (that note's L2), verbatim: "Under this declared
   reading, the same
   `f` acts on both sectors. An asymmetric pair `f_s != f_d` lies outside the
   declared symmetric family and is tested in N1 as a load-bearing negative
   control"; and the strict-sharpening meaning (that note's L3), verbatim:

   ```text
   T_f(q) < q  for 0<q<1/2,
   T_f(q) > q  for 1/2<q<1.
   ```

2. **The 3-cell sector menu** `{s, w, wbar}` with the swap-symmetric
   (orbit-constant) surface `p = (1-q, q/2, q/2)`. This surface is exactly
   the aggregation image `E(p_s, p_d) = (p_s, p_d/2, p_d/2)` of the
   KCPT-orbit-constant protocol-class note (unaudited `bounded_theorem`) and
   the dial shape `diag(p_s, p_d/2, p_d/2)` of the dial-shape qualification
   note (`audited_conditional`).

3. **The weight-to-dial coordinate map**, from the formation-gate relocation
   note (unaudited `bounded_theorem`) as consumed by the expressibility
   classification. The map is supplied only through the relocation theorem's
   explicitly unadopted energy dictionary (its Residual Atom 2, declared
   there as that note's own modeling element, not adopted); the
   expressibility classification introduces it, verbatim, as "Using the
   relocation theorem's explicitly unadopted energy dictionary (Residual
   Atom 2), the coordinate map is", followed verbatim by:

   ```text
   cell probabilities = (w, 1-w) = (singlet, doublet),
   r = (1-w)/(2w).
   ```

4. **The licensed static formation-weight set and its classification
   convention** from the expressibility classification note (unaudited
   `bounded_theorem`), verbatim:

   ```text
   W_expr = {1/3, 1/2}.
   ```

   This set is conditional on the source note's Supplied-Object
   Canonical-Measure Licensing Criterion (SOCMLC), which the source explicitly
   calls "a classification convention, not a theorem derived from the minimal
   axioms." Both values concern the same fixed singlet/doublet quotient:
   "carrier/orbit counting gives singlet weight `w = 1/3`, while counting or
   left-regular/Hilbert-Schmidt weighting of the **licensed commutative
   quotient** gives `w = 1/2`." The source expressly says it is "Not a
   classification for a different carrier, a refined menu, a menu with
   different orbit sizes, or a three-cell registration."

5. **The independence boundary** of the formation-gate relocation note
   (unaudited `bounded_theorem`). It states that "an independent formation rule
   supplies any normalized weight `(w, 1-w)`" and does NOT claim "an
   identification of measure granularity with formation weighting." It also
   states: "Not an inference that the tied measure's count-twice analytic grain
   is itself the formation law. That inference is the missing binding theorem
   isolated in T4." This boundary is load-bearing for the limited meaning of
   the correspondence proved below.

## Declared reading D1 (per-cell pairwise strict sharpening)

This note adds the following COMPOSITE declared class boundary — declared in
the same sense as the consumed note's L2/L3 declared-reading discipline, not
derived. Its independent components are the normalized common-profile
`n`-cell update, strict monotonicity of `g = f/x`, and the extension of
durability-as-stationarity to the finite menu:

> **D1.** On a finite registered cell menu with `n >= 2` cells, continued
> registration acts per cell through the same profile `f`:
> `T(p)_i = f(p_i) / sum_j f(p_j)`, with the share ratio
> `g(x) := f(x)/x` strictly increasing on all of `(0,1]`. In consequence,
> for any two cells with `0 < p_i < p_j` the update strictly amplifies the
> larger cell's share: `T(p)_i / T(p)_j < p_i / p_j` — exactly the
> statement `f(p_i)/p_i < f(p_j)/p_j`, i.e. `g(p_i) < g(p_j)`. The declared
> condition is deliberately the profile form, not the per-cell form: cells
> of one weight vector only realize pairs with `p_i + p_j <= 1`, so the
> per-cell amplification statements alone constrain `g` only on such
> realizable pairs; D1 declares monotonicity on all of `(0,1]`, which is
> exactly what the runner's profile-membership gates check. D1 also carries
> the consumed permanence-to-stationarity reading (L1) to the `n`-cell menu:
> "durable weight" in this note means exactly "stationary point of `T` on
> the probability simplex" — stationarity is the entire operational content
> of durability here, as in the consumed note's L1.

Three honesty facts about D1, each re-proven exactly by the runner:

1. **At `n = 2`, D1's operational content coincides exactly with the consumed
   L3.** The only realized pairs are complementary `(q, 1-q)`, and with
   `f(x) = x g(x)` the exact identity

   ```text
   f(q)(1-q) - q f(1-q) = q(1-q) [ g(q) - g(1-q) ]
   ```

   makes `g(q) < g(1-q)` for `0 < q < 1/2` algebraically equivalent to
   `f(q)(1-q) < q f(1-q)`, i.e. to the influence-odds-versus-input-odds form
   of L3 (runner block `TWO_CELL`).

2. **As a condition on the profile `f`, D1 is strictly stronger than 2-cell
   L3.** L3 constrains `g` only at complementary pairs `x + y = 1`; D1
   constrains `g` on all of `(0,1]`. The T5 witness separates the two
   conditions exactly.
   D1 is load-bearing at `n >= 3` and operationally invisible at `n = 2`.

3. **The Lueders exemplar family satisfies D1**: `f_k(q) = q^k` with `k > 1`
   gives `g(x) = x^(k-1)`, strictly increasing on `(0,1]` (runner blocks
   `POWER_PROFILES` and `NONPOWER_PROFILES` check the membership `g' > 0` on
   `(0,1]` exactly for the power and non-power exemplars).

## T1 (uniform-on-support classification of durable weights)

> **T1.** Under D1, for every `n >= 2`: `T(p) = p` on the probability
> simplex if and only if `p` is the uniform distribution on its support.
> The fixed set is exactly the `2^n - 1` uniform-on-support distributions.

*Proof.* Cells outside the support stay at `0` because `f(0) = 0`. On the
support, `T(p)_i = p_i` iff `f(p_i) = p_i * S` with `S = sum_j f(p_j)`, iff
`g(p_i) = S` is constant over the support. Since `g` is strictly increasing
it is injective, so all nonzero `p_i` are equal; conversely the uniform
distribution on a support of size `k` has
`T(p)_i = f(1/k) / (k f(1/k)) = 1/k`. QED

Reading (record ontology): within the class, every stationary weight is the
normalized counting measure on ITS SUPPORT. The unique interior stationary
weight is the normalized counting measure on the full registered menu.

Runner: block `UNIFORM_SUPPORT` solves `T(p) = p` exactly at `n = 3` for
`f = x^2` and `f = x^3`; the simplex fixed set is exactly the `7`
uniform-on-support points (three vertices, three edge midpoints, barycenter).

## T2 (aggregation identity and 3-cell-menu universality `q = 2/3`)

Restrict the 3-cell map with common `f` to the swap-symmetric surface
`(1-q, q/2, q/2)` and track the aggregated doublet weight `q`. The surface is
invariant (runner block `SWAP_DYNAMICS`), and the aggregated 2-cell dynamics is

```text
q -> 2 f(q/2) / (2 f(q/2) + f(1-q)),
```

i.e. the profile pair `f_s = f`, `f_d(q) = 2 f(q/2)`. Under D1 this pair is
strictly asymmetric: with `f(x) = x g(x)`,

```text
f_d(q) - f_s(q) = 2 f(q/2) - f(q) = q [ g(q/2) - g(q) ] < 0
```

for `0 < q <= 1`, since `q/2 < q` and `g` is strictly increasing. Runner block
`SWAP_DYNAMICS` proves the displayed identity symbolically and checks the
exemplar `f = x^2`
(`f_d(q) = q^2/2 != q^2`); the identity profile `f = x` has constant `g`, so
it sits outside D1 and gives `f_d = f` exactly — the contrast case. An
asymmetric pair is exactly a member of the family the consumed note's N1
treats as a load-bearing negative control — but here it is DERIVED as the
aggregated shadow of the symmetric 3-cell rule on the invariant surface, not
chosen as a family extension.

> **T2.** Interior fixed points of the aggregated dynamics satisfy
> `2 f(q/2)(1-q) = q f(1-q)`, and with `f(x) = x g(x)` the exact identity
>
> ```text
> 2 f(q/2) (1-q) - q f(1-q) = q (1-q) [ g(q/2) - g(1-q) ]
> ```
>
> holds. Hence under D1 the unique interior fixed point is `q/2 = 1-q`,
> i.e. `q = 2/3`, for EVERY admissible profile.

This is the exact 3-cell-menu mirror of the consumed note's universal
2-cell-menu interior fixed point `q = 1/2`. Aggregated `q = 2/3` means
`(p_s, p_d) = (1/3, 2/3)`: singlet weight `w = 1/3`, dial `r = 1` — the
counting measure on 3 cells, seen in aggregated coordinates.

Runner: block `AGGREGATION` proves the identity symbolically; blocks
`POWER_PROFILES` and `NONPOWER_PROFILES` solve the power family
`k in {2, 3, 5/2, 4}` and the non-power members `f = x e^(x-1)` and
`f = (x^2 + x^3)/2` exactly (aggregated interior fixed set `{2/3}`,
2-cell fixed set `{0, 1/2, 1}` in each case). Both non-power members
satisfy the class codomain `f : [0,1] -> [0,1]` with `f(0) = 0` and
`f(1) = 1`, gated in `NONPOWER_PROFILES`; a positive rescaling of `f` changes
neither `T_f` nor either stationarity condition, so the codomain gate costs
nothing.

## T3 (set-level arithmetic correspondence)

> **T3.** Within the declared record-influence class (D1 together with the
> consumed L1/L2/L3 readings), the set of singlet weights at the two unique
> interior stationary points is
>
> ```text
> W_dyn = {1/2, 1/3}.
> ```
>
> The 2-cell construction supplies `w = 1/2`; the 3-cell construction,
> aggregated on the swap-symmetric surface, supplies `w = 1/3`. Therefore
> `W_dyn = W_expr` as unordered numerical sets. Through
> `r = (1-w)/(2w)` — a coordinate supplied only through the relocation
> theorem's explicitly unadopted energy dictionary (Residual Atom 2) — both
> sets have dial image `{1/2, 1}`.

This equality does NOT identify the objects or mechanisms producing the two
sets. The dynamical values arise from normalized counting on two different
cell menus. The static values arise on one fixed singlet/doublet quotient:
carrier/orbit multiplicities `(1,2)` produce `w = 1/3`, while quotient-atom
counting `(1,1)` produces `w = 1/2`, conditional on SOCMLC. The expressibility
source excludes a three-cell registration from its classification. The
relocation source independently supplies the formation weight and explicitly
leaves measure-granularity/formation-weight identification as a missing
binding theorem. Accordingly T3 is support-only arithmetic, not a bijection
of physical grains, formation rules, or supplied objects.

Runner block `MENU_ARITHMETIC` checks the arithmetic
(`w = 1/2 -> r = 1/2`, `w = 1/3 -> r = 1`), the exact numerical set
equalities with `W_expr` as weights and `{1/2, 1}` as dials, and a
counterfactual 4-cell menu (`w = 1/4 -> r = 3/2`, outside both sets). It tests
only the advertised set-level correspondence; it does not test or assert a
physical identification.

## T4 (K-consistency exhibit)

Both menu dynamics are swap-equivariant, and the swap-symmetric
(orbit-constant) surface `p_w = p_wbar` is invariant under the 3-cell map
with common `f` (symbolic, runner block `SWAP_DYNAMICS`). The transverse
swap-odd mode at the 3-cell uniform point `(1/3, 1/3, 1/3)` for the exemplar
`f = x^2` has
exact multiplier `2` — but exciting it requires swap-odd (K-odd) initial
data, which is non-derivable inside the protocol class per the
KCPT-orbit-constant note's L-K2: "a nonzero K-odd initial datum therefore
remains a named conditional or open dependency; it is not derivable." This is
one K-odd perturbation exhibit only. It does not exclude K-even discriminants;
indeed, the same source gives a jointly K-even doublet-resolving observable.

Honesty: the interior uniform fixed points on BOTH menus are unstable under
iteration — the exemplar `f = x^2` has exact multiplier `2` at the
2-cell fixed point `q = 1/2`, at the aggregated 3-cell fixed
point `q = 2/3`, and on the transverse swap-odd mode (runner block
`MULTIPLIERS`). The value
`2` matches the exact multiplier of the records-flow separatrix exemplar
`r -> 2 r^2` at `r = 1/2` (consumed unaudited). The selection mode
throughout is stationarity/durability — a distinguished stationary point,
exactly as in the consumed occupancy-grain note and in the
stationary-point-not-forced anchor (`retained_bounded`) — not attraction
under iteration. No attractor claim is made.

## T5 (load-bearing negative control: the D1 witness)

D1 is a strictly stronger profile condition than 2-cell L3, and it is
load-bearing at `n = 3`. Exact piecewise-linear-`g` witness: define `g` on
`[0,1]` piecewise linear with node values

```text
g(0) = 2/5,   g(1/6) = 1/2,   g(1/3) = 9/20,
g(2/3) = 1/2, g(5/6) = 3/5,   g(1) = 7/10,
```

on the pieces `[0,1/6]`, `[1/6,1/3]`, `[1/3,2/3]`, `[2/3,1]` (linear on
each), and set `f(x) = x g(x)`. Exact facts, all re-proven by runner block
`D1_WITNESS`:

- **(a) The witness IS in the consumed note's literal 2-cell class.** `f` is
  continuous with `f(0) = 0` and `f(1) = 7/10 <= 1`, and strictly
  increasing: on each linear piece `g = a + b x`, the derivative
  `f' = a + 2 b x` is linear, so its minimum over the piece sits at a piece
  endpoint; the exact per-piece endpoint minima are `2/5 > 0` on `[0,1/6]`
  and `7/20 > 0` on `[1/6,1/3]` (where `f' = 11/20 - (3/5) x`), while on
  `[1/3,2/3]` one has `f' = 2/5 + (3/10) x >= 2/5 > 0` and on `[2/3,1]` the
  slope is positive with positive left-endpoint derivative.
- **(b) 2-cell L3 holds strictly — the witness leaves the consumed
  2-cell conclusion untouched.** `h(q) = g(1-q) - g(q)` is piecewise
  linear with breakpoints on `(0,1/2)` only at `q = 1/6` and `q = 1/3`, and

  ```text
  h(0) = 3/10,  h(1/6) = 1/10,  h(1/3) = 1/20,  h(1/2) = 0.
  ```

  All breakpoint values on `[0,1/3]` are positive and the final piece
  decreases linearly from `1/20` to the endpoint zero at `q = 1/2`, so
  `h > 0` on `(0,1/2)`; by antisymmetry `h(1-q) = -h(q)`, `h < 0` on
  `(1/2,1)`. By the `TWO_CELL` identity,
  `f(q)(1-q) < q f(1-q)` on `(0,1/2)` and
  the reverse on `(1/2,1)`: L3 holds strictly and the witness's 2-cell
  interior fixed set is exactly `{1/2}`.
- **(c) D1 fails.** `g(1/6) = g(2/3) = 1/2` while `g(1/3) = 9/20 < 1/2`
  with `1/6 < 1/3`: `g` is not strictly increasing (not even injective).
- **(d) At `n = 3` the counting menu is NOT reproduced — durability
  collapses to a CONTINUUM.** `p = (2/3, 1/6, 1/6)` is a NON-uniform 3-cell
  fixed point: `f(2/3) = 1/3`, `f(1/6) = 1/12`, so `S = 1/2` and
  `T(p) = (2/3, 1/6, 1/6)` exactly. And this fixed point is not isolated.
  Write `phi(q) = g(q/2) - g(1-q)` for the aggregated stationarity gap of
  T2. For the witness, exactly and piece by piece,

  ```text
  phi(q) = 9q/10 - 3/10    on [0, 1/3]    (unique zero  q = 1/3),
  phi(q) = 0  identically  on [1/3, 2/3],
  phi(q) = 3/20 - 9q/40    on [2/3, 5/6]  (unique zero  q = 2/3),
  phi(q) = 27q/40 - 3/5    on [5/6, 1]    (unique zero  q = 8/9),
  ```

  because on `[1/3, 2/3]` the two compositions `g(q/2)` and `g(1-q)` are the
  SAME linear polynomial `11/20 - (3/20) q`. The aggregated interior fixed
  set is therefore exactly the segment `[1/3, 2/3]` together with the
  isolated point `q = 8/9`, and on the swap-symmetric surface every point of
  `{(1-q, q/2, q/2) : q in [1/3, 2/3]}` is exactly fixed for the full 3-cell
  map (`g` takes one common value across the realized cell values there —
  exactly T1's stationarity mechanism, available at non-uniform profiles
  because the witness's `g` is non-injective). In dial coordinates the
  witness's durable weights sweep `r in [1/4, 1]` continuously and add the
  isolated value `r = 4` (`q = 8/9`, singlet weight `w = 1/9`). Exact
  exemplars, each verified by `D1_WITNESS`: the endpoint `q = 1/3`
  (`2 f(1/6) (2/3) = 1/9 = (1/3) f(2/3)`; weight `w = 2/3`, dial `r = 1/4`,
  outside the licensed menu both as a weight and as a dial); the midpoint
  `q = 1/2`, i.e. `p = (1/2, 1/4, 1/4)` (`g(1/4) = g(1/2) = 19/40`,
  `f(1/2) = 19/80`, `f(1/4) = 19/160`, `S = 19/40`) — a NON-counting durable
  profile that registers the LICENSED dial `r = 1/2`; the endpoint
  `q = 2/3` — the counting point survives, but as one endpoint of a fixed
  segment rather than as the unique interior durable weight; and `q = 8/9`
  (`g(4/9) = g(1/9) = 7/15`; both sides of the fixed-point condition equal
  `56/1215`).

Reading: D1 is exactly what confines the durable weights of the class to
counting measures. Without it the failure is not one stray extra point but a
collapse of selection: durability admits a CONTINUUM of weights, the dial
sweeps `r in [1/4, 1]` and also takes `r = 4`, and even the licensed dial
values lose their counting pedigree — the witness registers `r = 1/2` from
the non-counting profile `(1/2, 1/4, 1/4)`, and the counting point `r = 1`
survives merely as one endpoint of the fixed segment. This witness plays the
same role for D1 that the consumed note's N1/N2 controls play for its
L2/L3 — a load-bearing negative control, not a defect; in the consumed
note's own words, "N3 is an exact contrast, not a competing derivation."

## Bounded consequence

Within the declared record-influence class (D1 together with the consumed
L1/L2/L3 readings), T1 classifies every stationary point as uniform on its
support, and T2 fixes the unique interior point on the swap-symmetric 3-cell
surface at `q = 2/3`. For the 2-cell and 3-cell interior constructions, the
resulting singlet-weight set is numerically `{1/2, 1/3}`. Conditional on the
expressibility source and its SOCMLC convention, that set equals `W_expr`.
No object-level or physical identity follows from the equality.

The grain derivation obligation's closure criterion is two-part; verbatim:

```text
A closing theorem must derive the physical matter action and its measure,
then distinguish the count-once `det_C`/holomorphic realization from the
count-twice `|det_C|^2`/realified realization without inserting the desired
charged-lepton value or readout dictionary.
```

This note does not engage EITHER part of that criterion. It does not derive
the physical matter action or measure, and it does not identify its abstract
2-cell/3-cell menu arithmetic with the physical count-once/count-twice fork.
The formation-gate relocation source says the latter identification is a
missing binding theorem. No part of the obligation is weakened, localized,
replaced, or discharged. The obligation separately lists three notes as
"Relevant current route maps" (the measure-binary no-go, the
determinant-power split support note, the record-outcome orbit non-supply
no-go); this note adds no new map and does not assert that list is complete.
Nothing is claimed outside the declared class: non-symmetric families,
non-multiplicative influence forms, and non-stationarity selection modes are
all out of scope.

## Honest auditor read / Boundary

- **This note does NOT identify or decide the physical grain.** The dynamical
  2-cell/3-cell menu choice, the static carrier/quotient counting convention,
  and the physical count-once/count-twice action-and-measure fork remain
  distinct constructions. T3 proves only equality between the dynamical and
  static numerical weight sets; it supplies no map to the physical fork. The
  missing binding theorem is not supplied, and the grain derivation obligation
  stays fully open.
- **Everything is class-scoped.** All theorems quantify over the declared
  record-influence class only: the common-`f` symmetric family (consumed L2)
  together with the D1 per-cell strict sharpening. Non-symmetric families,
  non-multiplicative influence forms, and non-stationarity selection modes
  are outside scope, exactly as in the consumed note's own scope boundary.
  Membership exemplars are witnesses of non-emptiness, not a choice of
  record rule.
- **D1 is a declared reading, strictly stronger than the consumed 2-cell
  L3.** The T5 witness proves the strictness exactly: a profile inside the
  literal 2-cell class that satisfies L3 strictly, fails D1, and at `n = 3`
  admits a CONTINUUM of durable weights — the full aggregated interior fixed
  set is the segment `[1/3, 2/3]` together with the isolated point
  `q = 8/9`, sweeping dials `r in [1/4, 1]` plus `r = 4` and including a
  non-counting profile at the licensed dial `r = 1/2`. D1 is load-bearing at
  `n >= 3` and operationally invisible at `n = 2` (runner block `TWO_CELL`).
  A derivation of D1 from the record clauses is not attempted here.
- **Durability is stationarity, not attraction.** The interior uniform fixed
  points on both menus are unstable under iteration (exact exemplar
  multiplier `2` at `q = 1/2`, at aggregated `q = 2/3`, and on the
  transverse swap-odd mode). The selection mode is a distinguished
  stationary point, matching the stationary-point-not-forced anchor
  (`retained_bounded`) and the records-flow separatrix multiplier
  (unaudited); no attractor or convergence claim is made.
- **Conditional premises at live grades.** The consumed sources enter at
  exactly the grades listed in Load-bearing dependencies: five unaudited
  `bounded_theorem` notes, one `audited_conditional` note, one
  `retained_bounded` note, and one `open_gate` obligation. Every claim here
  is conditional on them at those grades; none is upgraded by consumption.
- **The aggregated asymmetric pair is a shadow, not a family extension.**
  T2's `f_s = f`, `f_d(q) = 2 f(q/2)` is derived by aggregating the
  symmetric 3-cell rule on the invariant surface; it does not enlarge the
  consumed note's declared symmetric family, whose N1 negative-control
  language is quoted above and preserved.

## Non-claims

This note selects no horn, no grain, no `r` value, no `Q` value, no mass, no
mixing angle, no probability rule, no species map, and no sector weight. The
two-point correspondence in T3 is exact set arithmetic across distinct
conditional constructions, not a selection among them (the counterfactual
4-cell row in runner block `MENU_ARITHMETIC` shows the arithmetic tracks menu
cardinality). The dial settings `r = 0`,
`r = 1/2`, and `r = 1` remain distinguished settings of a dial, per the
stationary-point-not-forced anchor; nothing here forces or prefers any of
them. The note adds no axiom, no primitive, no literature comparator, and no
supplied physical binding. It explicitly consumes D1, the parent declared
readings, the SOCMLC classification convention, and the other graded inputs
listed below; it changes no audit verdict and predicts none; it does not assert that the
physical charged-lepton matter action registers either grain; and it does
not derive record formation, occurrence, or the physical matter action and
measure named by the grain obligation's closure criterion.

## Load-bearing dependencies

| Dependency | Live grade (cited at exactly this grade) | Consumed content |
|---|---|---|
| [`ACPHILAMBDA_OCCUPANCY_GRAIN_RULE_CLASS_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-07-11.md`](ACPHILAMBDA_OCCUPANCY_GRAIN_RULE_CLASS_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-07-11.md) | unaudited `bounded_theorem` | The declared record-influence class; the permanence-to-stationarity reading (L1), the symmetric-family reading (L2), the strict-sharpening meaning (L3); the universal orbit-menu interior fixed point `q = 1/2`; the N1/N2/N3 negative-control pattern. Verbatim clauses are quoted above and gated in runner block `SOURCE_GATES`. |
| [`KOIDE_FORMATION_WEIGHT_LAW_EXPRESSIBILITY_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md`](KOIDE_FORMATION_WEIGHT_LAW_EXPRESSIBILITY_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md) | unaudited `bounded_theorem` | The static weight set `W_expr = {1/3, 1/2}`, conditional on that note's SOCMLC classification convention; `w = 1/3` from carrier/orbit multiplicities and `w = 1/2` from quotient-atom counting on one fixed two-cell quotient; the explicit exclusion of three-cell registration; and the coordinate hedge. These boundaries are quoted above and gated in runner block `SOURCE_GATES`. T3 consumes only the numerical set for support-only comparison. |
| [`KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md`](KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md) | unaudited `bounded_theorem` | Source of the `(w, 1-w) = (singlet, doublet)` per-cell coordinate and the dial map `r = (1-w)/(2w)` used in T3 and `MENU_ARITHMETIC` — supplied only through its explicitly unadopted energy dictionary (Residual Atom 2), declared in that note as its own modeling element, not adopted here. Also supplies the load-bearing independence boundary: formation weight is independent of measure granularity unless a missing binding theorem is proved. |
| [`KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md`](KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md) | unaudited `bounded_theorem` | The aggregation image `E(p_s, p_d) = (p_s, p_d/2, p_d/2)`; orbit-constancy of the swap-symmetric surface; L-K2 (swap-odd data non-derivable inside the protocol class), consumed in T4. |
| [`FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md`](FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md) | `retained_bounded` | The stationary-point-not-forced framing (distinguished dial settings, lanes not competing answers), consumed in T4 and Non-claims. |
| [`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md) | unaudited `bounded_theorem` | The records-flow separatrix exemplar `r -> 2 r^2`, whose exact multiplier `2` at `r = 1/2` is matched in runner block `MULTIPLIERS`. |
| [`KOIDE_GENERATION_WEIGHT_DIAL_SHAPE_FORCED_VALUE_UNFIXED_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md`](KOIDE_GENERATION_WEIGHT_DIAL_SHAPE_FORCED_VALUE_UNFIXED_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md) | `audited_conditional` | The dial shape `diag(p_s, p_d/2, p_d/2)` read on the swap-symmetric surface (shape forced, value unfixed). |
| [`AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`](AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md) | `open_gate` (ledger row: `audited_renaming`) | The open grain derivation obligation. Its two-part closure criterion is quoted verbatim in Bounded consequence and gated in runner block `SOURCE_GATES`. This note uses it only to state the boundary and does not engage either physical-action step. |

## Runner verification map

| Block | Content | Result |
|---|---|---|
| `AGGREGATION` | Aggregation identity `2 f(q/2)(1-q) - q f(1-q) = q(1-q)[g(q/2) - g(1-q)]` and the odds form of the aggregated fixed-point condition (symbolic) | PASS=3 FAIL=0 |
| `TWO_CELL` | `n = 2` equivalence identity (D1 content = L3 at complementary pairs) | PASS=2 FAIL=0 |
| `POWER_PROFILES` | Power family `k in {2, 3, 5/2, 4}`: D1 membership, aggregated interior fixed set exactly `{2/3}`, 2-cell fixed set exactly `{0, 1/2, 1}` | PASS=12 FAIL=0 |
| `NONPOWER_PROFILES` | Non-power members `f = x e^(x-1)` and `f = (x^2 + x^3)/2`: class-codomain gates (`f(0) = 0`, `f(1) = 1`), strict increase, D1 membership, and the same exact fixed sets | PASS=12 FAIL=0 |
| `UNIFORM_SUPPORT` | T1 at `n = 3` for `f = x^2`, `f = x^3`: simplex fixed set = exactly the `7` uniform-on-support points | PASS=3 FAIL=0 |
| `MENU_ARITHMETIC` | Weight-to-dial arithmetic `w = 1/2 -> r = 1/2`, `w = 1/3 -> r = 1`; numerical set equalities with `W_expr` and `{1/2, 1}`; counterfactual 4-cell menu | PASS=5 FAIL=0 |
| `SWAP_DYNAMICS` | Swap equivariance, surface invariance, aggregated-shadow formula, exemplar asymmetry `f_d != f_s`, identity-profile contrast, the strict-asymmetry identity | PASS=6 FAIL=0 |
| `MULTIPLIERS` | Exact multipliers: transverse swap-odd mode, 2-cell menu, aggregated 3-cell menu, separatrix match (all `= 2`) | PASS=5 FAIL=0 |
| `D1_WITNESS` | T5 witness: class membership, strict L3, D1 failure, the full aggregated interior fixed set `[1/3, 2/3]` together with `{8/9}` (piecewise certificate: piece mapping, per-piece formulas, identically-zero segment, unique zeros, assembly), the fixed-segment mechanism, spot identities, the non-counting profile at the licensed numerical dial `r = 1/2`, endpoint and isolated dials, dial sweep | PASS=28 FAIL=0 |
| `SOURCE_GATES` | Verbatim quote gates: each consumed clause present in its source note AND in this note (flattened substring), including SOCMLC, fixed-quotient provenance, three-cell exclusion, measure/formation independence, K-odd non-derivability, the energy-dictionary hedge, and the obligation criterion | PASS=15 FAIL=0 |
| `NOTE_HYGIENE` | Note hygiene: no prose decimals outside code fences, pinned closing phrases absent, claim-type line, required sections | PASS=4 FAIL=0 |

Run:

```bash
python3 scripts/acphilambda_occupancy_grain_menu_counting_correspondence_2026_07_16.py
```

Cached run result:

```text
TOTAL: PASS=95 FAIL=0
```

**No check passes by literal stipulation.**
