# Occupancy-Grain Sharpening-Import Decomposition: Reflection-Asymmetry and Orientation Dichotomy over the Declared Record-Influence Class: Bounded Theorem

claim id: `acphilambda_occupancy_grain_sharpening_import_decomposition_reflection_asymmetry_orientation_dichotomy_bounded_theorem_note_2026-07-16`

**Date:** 2026-07-16
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Premise weight:** conditional. Every claim below is conditional on the declared readings named in this note and on the consumed sources at exactly the live grades listed in Load-bearing dependencies. Nothing consumed is upgraded here, and no derivation obligation is discharged here.
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:** [`scripts/acphilambda_sharpening_import_decomposition_2026_07_16.py`](../scripts/acphilambda_sharpening_import_decomposition_2026_07_16.py)
**Cache:** [`logs/runner-cache/acphilambda_sharpening_import_decomposition_2026_07_16.txt`](../logs/runner-cache/acphilambda_sharpening_import_decomposition_2026_07_16.txt)

## Purpose

The occupancy-grain rule-class universality note consumes one strict-sharpening
import at its L3: the majority-amplification hypothesis
`T_f(q) < q for 0<q<1/2, T_f(q) > q for 1/2<q<1`. This note takes that single
import apart over the same declared 2-cell record-influence class and proves,
exactly, that it carries two logically separate contents:

1. a **reflection-asymmetry** content — the per-weight influence profile
   (declared `g` in D1) must be reflection-asymmetric on the interior (a
   note-local class written `A` below), which is what keeps the durable
   weight set on the closed cell equal to `{0, 1/2, 1}` — interior durable
   weight exactly `{1/2}` — and blocks any extra off-center durable weight; and
2. an **orientation** content — among reflection-asymmetric profiles, the
   majority-amplifying orientation (a note-local subclass written `A+`) versus
   the majority-attenuating orientation (`A-`) is a separate binary that the
   fixed-point set alone does not fix; it fixes only the stability/selection
   mode near the interior weight.

The reflection-asymmetry content is stated as an exact characterization of the
interior fixed set (T1 with T5(i)); the orientation content is a disjoint
dichotomy `A = A+ ⊔ A-` on top of it (T2, T5(ii)). Two exact
piecewise-linear witnesses make the separation load-bearing: an amplifying
member with a non-monotone per-weight influence profile that sits in `A+` but
not in the monotone-profile subclass `M`, and a reflection-symmetry-broken
boundary member outside `A` that carries an extra reflected pair of off-center
fixed points at `q = 5/22` and `q = 17/22`. The identity member `f(q) = q` is
the non-recording control with `T_f = q` identically.

The four framework axioms (Lattice, Qubit, Admissibility, Record) supply
neither content: a choice not fixed by the supplied structure remains a named
conditional or open dependency. This note quantifies over the declared class;
it selects no profile, no weight, and no dial value, and it discharges no part
of the open grain derivation obligation.

Record ontology throughout: a supplied registered weight is called durable
exactly when the declared continued-registration update leaves it stationary,
as in the consumed note's permanence-to-stationarity reading. No formation,
occurrence, convergence, or pre-record readout is inferred.

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

   with `T_f` extended to the endpoints by its limits `T_f(0) = 0`,
   `T_f(1) = 1`. This note calls the set of all such `f` the family `F`.

2. **The strict-sharpening meaning consumed at that note's L3.** The consumed
   note frames it, verbatim:

   > For this lemma, **strict sharpening** has its majority-amplification meaning:

   followed verbatim by

   ```text
   T_f(q) < q  for 0<q<1/2,
   T_f(q) > q  for 1/2<q<1.
   ```

   This is the single import decomposed below.

3. **The consumed scope boundary** of that note, verbatim:

   > L3 uses off-center majority amplification as strict sharpening. Bare monotonicity of the influence odds is insufficient, as N2 shows.

   The parent's "influence odds" is its own object, defined there verbatim:

   > with input odds `O(q)=q/(1-q)` and influence odds `F(q)=f(q)/f(1-q)`

   (the parent's symbols; this note's family symbol `F` is unrelated, and the
   parent's `O`, `F(q)` are not used below).

   The present decomposition sharpens exactly this sentence: it separates the
   reflection-asymmetry content that governs the interior fixed set from the
   orientation content, and it re-exhibits the N2 identity member as the
   non-recording control.

4. **The consumed Record clauses**, from the framework axiom memo (a `meta`
   axiom note; depending on an axiom confers no bounded status). Verbatim:

   > When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent.

   and

   > Only records are readable. A readout value is determined by record content alone.

   The permanence-to-stationarity reading — a durably registered interior
   weight must be a fixed point of every admissible continued-registration
   update — is consumed as a declared reading exactly as in the parent note's
   L1; it is not re-derived here.

5. **The consumed qualification clause**, from the same axiom memo, verbatim:

   > A choice not fixed by the supplied structure remains a named conditional or open dependency.

   This is the exact sense in which the two decomposed contents are named
   conditionals, not axiom consequences (T5).

6. **The weight-to-dial translation**, consumed from the parent note's L3,
   verbatim in its own derivation:

   ```text
   p_d = P_d/(P_s+P_d)
       = 2|b|^2/(a^2+2|b|^2)
       = 2r/(1+2r).
   ```

   Through this supplied translation the central interior weight `q = 1/2`
   corresponds to the dial setting `r = 1/2`. The translation is supplied
   context only; nothing here forces, derives, or prefers that dial setting.

## Declared symbols D1

The following are note-local symbols for the declared class, in the same
declared-reading discipline as the parent note's L2/L3 — plain descriptors for
this note, not proposed framework vocabulary or registry coinages.

> **D1.** On `(0,1]` write the per-weight influence profile `g(x) := f(x)/x`,
> so that `f(x) = x g(x)` and `g` is continuous with `g > 0`. This is a
> note-local object, distinct from the parent note's influence odds (the ratio
> `f(q)/f(1-q)`, quoted in Supplied objects item 3); no claim below is a claim
> about that ratio. Write the **reflection asymmetry**
> `h(q) := g(q) - g(1-q)` on `(0,1)` (the sign convention is note-local); it
> is reflection-odd, `h(1-q) = -h(q)`, so `h(1/2) = 0`. Over the family `F`
> declare the note-local classes
>
> ```text
> A  := { f in F : h != 0 on (0,1) except at q = 1/2 },        (reflection-asymmetric)
> A+ := { f in A : h > 0 on (1/2,1) },                         (majority-amplifying)
> A- := { f in A : h < 0 on (1/2,1) },                         (majority-attenuating)
> M  := { f in F : g strictly increasing on (0,1] }.           (monotone per-weight influence)
> ```

Three honesty facts about D1; the runner re-proves the identities and witness
separations exactly, and fact 3's forward inclusions are one-line consequences
of D1 shown in place:

1. **The reflection asymmetry `h` is exactly the interior fixed-point control.**
   With `f(x) = x g(x)`, the exact identity of T1 makes the numerator of
   `T_f(q) - q` equal `q(1-q) h(q)`, so an interior weight is fixed if and only
   if `h` vanishes there. `A`-membership is precisely the condition that `h` has
   no interior zero other than `q = 1/2`.

2. **Orientation is a second, separate binary.** Among `A` members, the sign of
   `h` on `(1/2,1)` splits `A` into `A+` and `A-` disjointly (T2). The fixed
   set on the closed cell is `{0, 1/2, 1}` for both orientations; the
   orientation changes only the stability/selection mode near `q = 1/2`, not
   the fixed set.

3. **The ladder is strict.** `M ( A+ ( A ( F`. The forward inclusions are
   one-line consequences of D1: if `g` is strictly increasing, then for
   `q in (1/2,1)` one has `q > 1-q`, so `h(q) = g(q) - g(1-q) > 0`, and by
   reflection-oddness `h < 0` on `(0,1/2)`; hence `h` has no interior zero off
   the center, giving `M => A+` (`A`-membership and the `+` orientation
   together). `A+ ( A ( F` are restrictions by definition. Each inclusion is
   proper, separated by an exact witness (T4); the runner additionally gates
   the affine-subfamily mechanism identity `h(q) = c1(2q - 1)` exactly.

## T1 (reflection-asymmetry fixed-point identity)

> **T1.** For every `f in F`, the exact identity
>
> ```text
> f(q)(1-q) - q f(1-q) = q(1-q) [ g(q) - g(1-q) ] = q(1-q) h(q)
> ```
>
> holds, and it is the numerator of `T_f(q) - q`. Hence on `(0,1)` the
> interior fixed points of `T_f` are exactly the interior zeros of `h`. The
> interior fixed set is `{1/2}` — equivalently `Fix(T_f) = {0, 1/2, 1}` on the
> closed cell — if and only if `f in A`. This interior-fixed-set equivalence is
> the exact-characterization content isolated in T5(i).

*Reading.* The endpoints `0` and `1` are fixed for every `f in F` by
`f(0) = 0` and strict increase, exactly as in the parent note. The interior
story is governed entirely by `h`: a reflection-asymmetric profile keeps a
single interior fixed weight at the center, while any interior zero of `h` off
the center is an extra off-center durable weight (N1).

Runner: block `T1_FIXED_POINT` proves the identity symbolically for a generic
profile, checks that the numerator of `T_f(q) - q` equals `f(q)(1-q) - q f(1-q)`,
solves the interior fixed condition exactly for the power members `f = q^2` and
`f = q^3` (interior fixed set `{1/2}` in each case), and confirms the endpoint
limit extensions `T_f(0) = 0`, `T_f(1) = 1`.

## T2 (sign bridge and orientation dichotomy)

> **T2.** For every `f in F` and interior `q`,
>
> ```text
> T_f(q) - q = q(1-q) h(q) / ( f(q) + f(1-q) ),
> ```
>
> and since `f(0) = 0` with strict increase gives `f > 0` on `(0,1]`, the
> factor `q(1-q)/(f(q)+f(1-q))` is strictly positive on the interior, giving
> the sign bridge
> `sign(T_f(q) - q) = sign(h(q))`. Consequently `A = A+ ⊔ A-` disjointly:
> a reflection-asymmetric profile is either majority-amplifying (`T_f(q) > q`
> for `q > 1/2`) or majority-attenuating (`T_f(q) < q` for `q > 1/2`), never
> both. Every member also satisfies the exchange symmetry
> `T_f(1-q) = 1 - T_f(q)`. If `f` is differentiable at `q = 1/2`, then
> `T_f'(1/2) = f'(1/2) / (2 f(1/2))`; for the differentiable-at-center power
> member `f = q^k` the central slope is exactly `k`.

*Reading.* The sign bridge is what turns the parent note's L3 inequality into a
statement about `h`. Majority amplification (the L3 orientation) is exactly
`h > 0` on `(1/2,1)`, i.e. membership in `A+`. Attenuation is `A-`. Both keep
the interior fixed set at the center; the orientation is a genuinely separate
choice, invisible to the fixed-point count and fixed only by the mode content
of the L3 import.

Runner: block `T2_SIGN_BRIDGE` proves the full-quotient identity symbolically,
checks strict positivity of the denominator at a rational sample for two
members (the class-level positivity is the one-line `f > 0` fact in the box),
proves the exchange symmetry and, under the stated differentiability condition,
the central-slope formula symbolically, and confirms the central slope equals
`k` for `k = 1/2`, `k = 2`, and symbolic `k > 0`.

## T3 (off-center orientation horn) and orbit behaviour

> **T3.** For `f in A+`, off-center amplification holds strictly:
> `T_f(q) > q` on `(1/2,1)` and `T_f(q) < q` on `(0,1/2)`. The abstract
> continued-registration orbit `q_{n+1} = T_f(q_n)` from any `q_0 in (1/2,1)`
> is strictly increasing, stays in `(1/2,1)`, and converges upward with limit
> `1`. For `f in A-` the strict inequalities reverse and the orbit from
> `q_0 in (1/2,1)` is strictly decreasing, stays in `(1/2,1)`, and converges
> downward with limit `1/2`.

*Derivation of the orbit statements.* Confinement: since `f` is strictly
increasing, `T_f(q) - 1/2 = (f(q) - f(1-q)) / (2(f(q) + f(1-q)))` has the sign
of `q - 1/2`, so `(1/2,1)` maps into `(1/2,1)` (and `T_f(q) < 1` because
`f(1-q) > 0` for `q < 1`). A monotone orbit confined to a bounded interval
converges; on `[1/2,1]` the denominator satisfies
`f(q) + f(1-q) >= f(1/2) > 0`, so `T_f` is continuous there and the limit is a
fixed point of `T_f` in `[1/2,1]`, which by T1 lies in `{1/2, 1}`. An `A+`
orbit is strictly increasing from `q_0 > 1/2`, so its limit is `1`; an `A-`
orbit is strictly decreasing and stays above `1/2`, so its limit is `1/2`.

*Reading.* Orientation is what selects which side of the central weight the
recording update pushes toward. This is the stability/selection-mode content of
the L3 import; the interior fixed set is the same `{0, 1/2, 1}` in both
orientations. Durability throughout is fixed-point stationarity under the
declared update, not attraction: the horn statements describe the one-step and
iterated direction and its limit. This is distinct from stationarity of an
entropy or balance functional.

Runner: block `T3_HORN` checks off-center amplification `T_f(q) > q` at
`q = 3/5` for four `A+` members (`q^2`, `q^3`, `q^4`, `(q + q^2)/2`) and the mirror
minority attenuation `T_f(2/5) < 2/5` for `q^2`. Block `ORBITS` iterates the
`A+` exemplar `f = q^2` from `q_0 = 3/5` (six exact-rational steps, strictly
increasing, staying in `(1/2,1)`, closing gap to `1` below `1/1000`) and the
`A-` exemplar `f = sqrt(q)` from `q_0 = 3/4` (six exact-radical steps, strictly
decreasing, staying above `1/2`, closing gap to `1/2` below `1/100`), with all
radicals kept exact, and solves the `A-` exemplar's interior fixed set exactly
(`{1/2}` on `(0,1)`).

## T4 (strict ladder `M ( A+ ( A ( F`)

> **T4.** The note-local classes form a strict ladder
> `M ( A+ ( A ( F`. Each inclusion is proper, witnessed exactly:
> the amplifying witness of N0 lies in `A+` but not in `M` (its per-weight
> influence profile `g` is non-monotone); the member `f = sqrt(q)` lies in
> `A-`, hence in `A` but not in `A+` and not in `M`; and the identity member
> `f = q` lies in `F` but not in `A` (its `h` is identically zero), as does
> the sign-mixed witness `B` of N1.

Runner: block `LADDER` checks the affine-subfamily mechanism identity
`h(q) = c1 (2q - 1)` symbolically; the non-monotone per-weight profile of the
N0 witness (`g(1/2) < g(1/4)`) together with `h > 0` at interior samples of
`(1/2,1)`; the exact derivative `g'(x) = -x^(-3/2)/2 < 0` for `f = sqrt(q)`
(not in `M`) with an exact conjugate certificate that `h < 0` on `(1/2,1)`
(in `A-`); the identically-zero `h` of the identity member (in `F`, not in
`A`); and witness `B`'s exact reflected off-center zeros
`h(5/22) = h(17/22) = 0` (in `F`, not in `A`).

## T5 (sharpening-import decomposition)

> **T5.** Over the declared family `F`, the single strict-sharpening import of
> the parent note's L3 decomposes into two logically separate contents:
>
> - **(i) reflection asymmetry** — `f in A`. By T1 this is `necessary and
>   sufficient` for the interior durable weight set to be exactly `{1/2}`
>   (no off-center durable weight). Sufficiency and necessity are the two
>   directions of the T1 zero-of-`h` identity.
> - **(ii) orientation** — `f in A+` rather than `A-`. By T2 this is a separate
>   disjoint binary on top of (i); it does not change the interior fixed set and
>   fixes only the stability/selection mode near `q = 1/2`.
>
> The parent note's L3 imports (i) and (ii) together. The four framework axioms
> supply neither: a choice not fixed by the supplied structure remains a named
> conditional or open dependency.

The two contents are made load-bearing by exact witnesses in the following
sections (N0–N2): the N0 member exhibits `A+` without `M`, a sign-mixed
boundary member outside `A` (N1) shows (i) is load-bearing (an extra reflected
pair of off-center fixed points appears), and the amplifying/attenuating split shows
(ii) is not implied by (i).

## N0 (amplifying witness, in `A+` but not in `M`)

Define `g` piecewise linear on `[0,1]` with node values

```text
g(0) = 1/2,  g(1/4) = 3/5,  g(1/2) = 11/20,  g(3/4) = 4/5,  g(1) = 9/10,
```

on the pieces `[0,1/4]`, `[1/4,1/2]`, `[1/2,3/4]`, `[3/4,1]` (linear on each),
and set `f(x) = x g(x)`. The runner names this member `WITNESS_A`; the letter
names the witness, not the class `A`. Exact facts, all re-proven by runner
block `WITNESS_A`:

- **The witness is in the family `F`.** `f` is continuous with `f(0) = 0` and
  `f(1) = 9/10 <= 1`, and strictly increasing: on each linear piece
  `g = a + b x` the derivative `f' = a + 2 b x` is positive at both piece
  endpoints, so positive throughout.
- **The witness is in `A+`.** Exactly and on both pieces of `(1/2,1)` the same
  affine formula holds,

  ```text
  h(q) = 4q/5 - 2/5   on (1/2, 1),
  ```

  which is strictly positive there (e.g. `h(7/8) = 3/10`) and vanishes only at
  the center, so `h` has no interior zero off `q = 1/2` and is positive on the
  majority side.
- **The witness is not in `M`.** `g(1/4) = 3/5 > 11/20 = g(1/2)`, so the
  per-weight influence profile is non-monotone while the member still
  amplifies the majority. This is the exact separation `M ( A+` used in T4.

Reading: orientation (content (ii)) does not require a monotone per-weight
profile. Amplification is controlled by the reflection asymmetry `h` alone,
which compares `g` across the reflection `q <-> 1-q` and is insensitive to
`g`'s behaviour within a side.

## N1 (sign-mixed boundary witness `B`, extra fixed-point pair `{5/22, 17/22}`)

Define `g` piecewise linear on `[0,1]` with node values

```text
g(0) = 1/2,  g(1/4) = 7/10,  g(1/2) = 3/5,  g(3/4) = 13/20,  g(1) = 1,
```

on the pieces `[0,1/4]`, `[1/4,1/2]`, `[1/2,3/4]`, `[3/4,1]` (linear on each),
and set `f(x) = x g(x)`. Exact facts, all re-proven by runner block
`WITNESS_B`:

- **`B` is in the family `F`.** `f` is continuous with `f(0) = 0` and
  `f(1) = 1`, and strictly increasing: on each linear piece `g = a + b x` the
  derivative `f' = a + 2 b x` is positive at both piece endpoints, so positive
  throughout.
- **`B` is reflection-symmetry-broken but sign-mixed, so `B` is NOT in `A`.**
  Exactly and piece by piece,

  ```text
  h(q) = 1/10 - q/5      on (1/2, 3/4),
  h(q) = 11q/5 - 17/10   on (3/4, 1),
  ```

  so `h(3/4) = -1/20 < 0` while `h(21/22) = 2/5 > 0`: `h` changes sign on
  `(1/2,1)`, hence has an interior zero there, so `B` is outside `A`.
- **The extra off-center fixed points are the reflected pair
  `{5/22, 17/22}`.** Solving `h(q) = 0` on `(3/4,1)` gives exactly
  `q = 17/22`; reflection oddness gives the paired zero `q = 5/22`.
  Back-substitution gives both fixed points exactly:
  `g(17/22) = g(5/22) = 15/22`,
  `f(17/22) = 255/484`, `f(5/22) = 75/484`, and hence
  `T_B(17/22) = 255/330 = 17/22` while
  `T_B(5/22) = 75/330 = 5/22`. Thus the closed-cell fixed set of `B` is
  `{0, 5/22, 1/2, 17/22, 1}`. Below the upper point
  `T_B(7/10) < 7/10` and above it `T_B(9/10) > 9/10`, so `q = 17/22`
  sits between an attenuation region and an amplification region.

Reading: reflection asymmetry (`A`-membership) is exactly what forbids an
off-center durable weight. Drop it — keep only continuity, strict increase, and
`f(0) = 0` — and an extra reflected pair of off-center fixed points appears.
This witness plays the
same load-bearing negative-control role for content (i) that the parent note's
N1/N2 controls play for its L2/L3.

## N2 (identity member `f = q`, non-recording control)

For `f(q) = q`, `g(x) = 1` is constant, `h` is identically zero, and

```text
T_f(q) = q / ( q + (1-q) ) = q
```

for every `q`. Every weight is fixed: the identity member is non-recording, it
lies in `F` but not in `A`, and it selects nothing. This is exactly the parent
note's N2 control. The parent's scope-boundary sentence speaks of its own
influence odds `f(q)/f(1-q)` (Supplied objects, item 3); for the identity
member that ratio is `q/(1-q)`, strictly increasing on `(0,1)`, yet the member
lies outside `A` — that is the parent's sense in which bare influence-odds
monotonicity is insufficient. In this note's decomposition the same member
shows the finer fact: its per-weight influence profile `g` is constant, `h`
vanishes identically, and it imports neither content (i) nor content (ii).

Runner block `IDENTITY` proves `T_f = q` identically, checks a set of rational
samples are all fixed, and confirms `h` is identically zero.

## Bounded consequence

Over the declared 2-cell record-influence family `F` and the consumed
permanence-to-stationarity reading, the strict-sharpening import consumed at the
parent note's L3 is exactly the conjunction of two separate contents:
reflection asymmetry (`A`-membership), which by T1 is exactly the condition for
the interior durable weight to be the single central weight `q = 1/2`; and the
amplifying orientation (`A+`), a disjoint binary that fixes the direction and
limit of the declared abstract iteration. Through the parent note's supplied translation
`p_d = 2r/(1+2r)`, the central weight `q = 1/2` corresponds to the dial setting
`r = 1/2`; this note forces, derives, and prefers no dial setting. The
translation supplies no physical lane assignment.

The grain derivation obligation's closure criterion is, verbatim:

```text
A closing theorem must derive the physical matter action and its measure, then
distinguish the count-once `det_C`/holomorphic realization from the
count-twice `|det_C|^2`/realified realization without inserting the desired
charged-lepton value or readout dictionary.
```

This note engages no part of that criterion. It derives no physical matter
action or measure and identifies its abstract class decomposition with no
physical realization fork. No part of the obligation is weakened, localized,
replaced, or discharged; the obligation stands at its live grade. Nothing is
claimed outside the declared class: non-symmetric families, non-multiplicative
influence forms, and non-stationarity selection modes are out of scope.

## Honest auditor read / Boundary

- **This note decomposes an import; it derives no new physics.** T1–T5 restate
  the content of the parent note's L3 import as two separate conditions over
  the same declared class. No occupancy weight, horn, orientation, or dial value
  is selected. The decomposition is a statement about the class, not a
  selection within it.
- **Everything is class-scoped.** All theorems quantify over the declared
  2-cell record-influence family `F` and the note-local classes `A`, `A+`,
  `A-`, `M` built from it. Non-symmetric families, non-multiplicative influence
  forms, and non-stationarity selection modes are outside scope, exactly as in
  the parent note's own scope boundary. Membership witnesses are non-emptiness
  exhibits, not a choice of record rule.
- **The two contents are genuinely separate, and each is load-bearing.** Content
  (i) is load-bearing by witness `B`: a member of `F` outside `A` acquires an
  extra reflected pair of off-center durable weights at `q = 5/22` and
  `q = 17/22`. Content (ii) is not implied by
  (i): `A = A+ ⊔ A-` is a disjoint dichotomy, and the attenuating member
  `f = sqrt(q)` sits in `A-`, sharing the interior fixed set `{0, 1/2, 1}` with
  every `A+` member while pushing orbits the other way. The amplifying witness
  (N0) sits in `A+` but not `M`, so the monotone-profile condition `M` is
  strictly stronger than the amplifying orientation.
- **The axioms supply neither content.** By the consumed qualification clause, a
  choice not fixed by the supplied structure remains a named conditional or open
  dependency. The framework axiom memo is a `meta` note and confers no bounded
  status; depending on Record here is only the consumed permanence-to-
  stationarity reading, declared, not a source of bounded status. Both contents
  (i) and (ii) are named conditionals in exactly this sense.
- **Durability is fixed-point stationarity under the declared update, not
  attraction.** The horn and orbit statements
  describe the direction and limit of the abstract continued-registration
  iteration. This is distinct from stationarity of an entropy or balance
  functional. No attractor or convergence claim about a physical state is made.
- **Conditional premises at live grades.** The consumed sources enter at exactly
  the grades listed in Load-bearing dependencies: one unaudited `bounded_theorem`
  parent, one `meta` axiom memo, and one open obligation shown at `open_gate`
  with its ledger row `audited_renaming`. Every
  claim here is conditional on them at those grades; none is upgraded by
  consumption.

## Non-claims

This note selects no horn, no grain, no orientation, no `r` value, no `Q`
value, no mass, no mixing angle, no probability rule, no species map, and no
sector weight. The decomposition in T5 is an exact statement about the declared
class, not a selection among its members. Nothing here forces or prefers any
dial setting.
The note adds no axiom, no primitive, no literature comparator, and no supplied
physical binding, and it coins no framework vocabulary: `A`, `A+`, `A-`, `M`,
`g`, and `h` are note-local descriptors declared in D1 and proposed for no
registry. It explicitly consumes the parent declared readings, the Record
clauses, and the other graded inputs listed below; it changes no audit verdict
and predicts none; it does not assert that the physical charged-lepton matter
action registers either content; and it does not derive record formation,
occurrence, or the physical matter action and measure named by the grain
obligation's closure criterion.

## Relation to prior notes

The counting-measure correspondence note
`ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md`
works over the same declared class at the level of the menu cardinality and the
uniform-on-support fixed weights. The present note is independent of it: it
consumes none of its content, seeds no citation edge to it, and shares only the
parent record-influence family. It is named here for orientation only.

## Load-bearing dependencies

| Dependency | Live grade (cited at exactly this grade) | Consumed content |
|---|---|---|
| [`ACPHILAMBDA_OCCUPANCY_GRAIN_RULE_CLASS_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-07-11.md`](ACPHILAMBDA_OCCUPANCY_GRAIN_RULE_CLASS_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-07-11.md) | unaudited `bounded_theorem` | The declared 2-cell record-influence family `T_f` (L2); the strict-sharpening majority-amplification meaning decomposed here (L3); the scope-boundary sentence that bare influence-odds monotonicity is insufficient; the influence-odds definition itself (the parent's own object, distinguished from this note's per-weight profile); the `p_d = 2r/(1+2r)` weight-to-dial translation; the N1/N2 negative-control pattern. Verbatim clauses are quoted above and gated in runner block `SOURCE_GATES`. |
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | `meta` (doc-header type; framework axiom memo; confers no bounded status; not a graded ledger row) | The verbatim Record clauses (permanence, record-only readability) read as the permanence-to-stationarity discipline, and the qualification clause that an unfixed choice remains a named conditional or open dependency. Depending on the Record axiom is not treated as a source of bounded status. Quoted above and gated in `SOURCE_GATES`. |
| [`AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`](AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md) | `open_gate` (ledger row: `audited_renaming`) | The open grain derivation obligation. Its closure criterion is quoted verbatim in Bounded consequence and gated in runner block `SOURCE_GATES`. This note uses it only to state the boundary and engages no physical-action step. |

## Runner verification map

| Block | Content | Result |
|---|---|---|
| `TEXT_INTEGRITY` | Paired note exists; claim id present; each of the three load-bearing dependency filenames appears in the note | PASS=5 FAIL=0 |
| `T1_FIXED_POINT` | Reflection-asymmetry fixed-point identity, numerator match, exact interior solves for `q^2` and `q^3`, endpoint-limit extensions, reflection-oddness of `h` | PASS=7 FAIL=0 |
| `T2_SIGN_BRIDGE` | Full-quotient sign-bridge identity, denominator positivity, exchange symmetry, differentiability-qualified central-slope formula, power-member central slopes including symbolic `k` | PASS=9 FAIL=0 |
| `T3_HORN` | Declared-family gate for the normalized polynomial member, off-center amplification `T_f(3/5) > 3/5` for four `A+` members, and the mirror attenuation `T_f(2/5) < 2/5` | PASS=6 FAIL=0 |
| `ORBITS` | `A+` orbit rising toward `1` (exact rationals); `A-` orbit falling toward `1/2` (exact radicals); monotone, in-band, and gap certificates; exact interior fixed-set solve for the `A-` exemplar | PASS=7 FAIL=0 |
| `WITNESS_A` | `A+` witness of N0: node table gated in note text, continuity, `f(0)=0`/`f(1)<=1`, strict increase, `h` values and the affine side formula `h = 4q/5 - 2/5` with collinearity and slope certificates, non-monotone per-weight profile, one-step amplification | PASS=13 FAIL=0 |
| `WITNESS_B` | Sign-mixed boundary witness of N1: node table gated in note text, continuity, `f(0)=0`/`f(1)=1`, strict increase, sign-mixed `h`, symbolic side formulas, exact upper-half solve `h=0 -> q=17/22`, reflected pair `{5/22,17/22}`, back-substituted fixed points, complete closed-cell fixed set, below/above sign check | PASS=14 FAIL=0 |
| `IDENTITY` | N2 identity member: `T_f = q` identically, all rational samples fixed, `h` identically zero | PASS=3 FAIL=0 |
| `LADDER` | Strict ladder `M ( A+ ( A ( F`: affine mechanism identity, N0 witness in `A+` not `M`, `sqrt` in `A-` not `M` with conjugate certificate, identity member in `F` not `A`, witness `B` off-center zero | PASS=7 FAIL=0 |
| `SOURCE_GATES` | Verbatim quote gates: each consumed clause present in its source note AND in this note (flattened substring), including the parent's influence-odds definition | PASS=10 FAIL=0 |
| `NOTE_HYGIENE` | No prose decimals outside code fences, pinned closing/enumeration phrases absent, claim-type line, required sections, the T5 exact-characterization phrase used exactly once | PASS=5 FAIL=0 |

Run:

```bash
python3 scripts/acphilambda_sharpening_import_decomposition_2026_07_16.py
```

Cached run result:

```text
TOTAL: PASS=86 FAIL=0
```

**No check passes by literal stipulation.**
