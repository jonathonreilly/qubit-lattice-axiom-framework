# beyond-the-union-bound, attempt 4 (worker w-macbookpro90c72-j5968, model grok-4.6)

Definitions are those of block 25 (PR #8168) and block 30 (PR #8174), fetched from
`origin/physics-loop/admissibility-induced-law-block25-formation-law-ordered-phase-toom-stability-level-automaton-20260916`
and
`origin/physics-loop/admissibility-induced-law-block30-six-axis-threshold-two-level-domination-amplified-nodes-20260916`.
The two-level automaton `η'`, the extended explanation family `𝓔`, the typed regular
tree `𝕋`, and the slot-product recursion

```
D = (1+xU)^2 (1+3xD) (1+yF)^6,
U = (1+xU)^3 (1+yF)^6,
F = (1+xU)^3 (1+3xD) (1+yF)^5,
R = (1+xU)^3 (1+3xD) (1+yF)^6
```

are block 30's T1–T3, restated. At `y = 0` the `U`-equation is `U = (1+xU)^3`, whose
positive solutions exist if and only if `x ≤ 4/27` (block 30 T5). The t-trick of T3
then needs `ε₂ < max_t t²(4/27 − t) = 256/531441`, which on `(p, 1, 2)` fails for
every `p ≤ 4150`. The executed threshold is `p ∈ (10.5, 11)` (block 28, evidence
address only).

The plan, formed before looking at other attempts: (i) thin the *lift* to `𝕋` by
forbidding the first lattice identification (the commutative diamond `e_i + e_j`),
which still upper-bounds the G-tree sum; (ii) separately try a past-cluster *set*
count with the 3-type product `A = ε₁ + 3ε₂ A + 3A² + A³`. Route (ii) is recorded
as a no-go. Route (i) gives a new exact domain point.

## (1) The statement attempted

**A (tree count, diamond-free lift).** Let `𝕋^{DF}` be the admissible subtrees of
`𝕋` in which no vertex has both of the two up-grandchildren that close a diamond:
if a vertex occupies up-children in directions `i` and `j`, it does not occupy both
the further up-`j` child of `i` and the further up-`i` child of `j`. Every lift of
a subtree of `G` lies in `𝕋^{DF}` (a G-tree is simple). At `y = 0` the occupancy
generating function of a U-node in `𝕋^{DF}` obeys the 4-type system of Step 3, and
the rational triple `(a₁, a₂, a₃) = (12/25, 1/5, 2/25)` is a super-solution at
`x = 3/20 > 4/27`, with `U = 78/25`. The companion D-node bound `D̄ = 72` and the
slot-product `R̄ = (1 + xU)³(1 + 3x D̄) = 8254954121/78125000` are super-solutions
of the remaining `y = 0` equations. Hence the lifted sum over `𝓔` with arrow-weight
`x` and fork-weight `0` is finite at `x = 3/20`. The t-trick of T3 then needs only
`ε₂ < max_t t²(3/20 − t) = 1/2000` (attained at `t = 1/10`). On `(p, 1, 2)`,
`max(d₂, d₃) < 1/2000` first holds at the integer `p = 4004` (fails at `p = 4003`).
At that coupling, `t = 1/10` gives `t + ε₂/t² < 3/20` and `ε₁ R̄ < 10^{-7}`.

This is a strictly smaller *tree* count than T5's slot-product (the domain of `U`
grows); it is not a set count, and it does not remove the t-trick's `t²` from the
bad-pair budget. It does not locate the true strength.

**B (set count, no-go).** The candidate lemma "`A = ε₁ + 3ε₂ A + 3A² + A³`
dominates `Σ_S ε₁^{n₀(S)} ε₂^{n₁(S)}` over past directed animals `S` containing the
root, because `w(S) ≤ w_root ∏ w(S_i)`" is false. On
`S = {0, −e₁, −e₂, −e₁−e₂}` one has `w(S) = ε₁ ε₂² > (ε₁ ε₂)² = w(S₁)w(S₂)`
whenever `ε₁ < 1`. Exact values at `p = 14` on `(p, 1, 2)`:
`1587/3696187 > 4761/933119209`. The overlapping-cone product is the first failing
step of this set-route. (Existence of a super-solution of the product map is not
the obstruction: `(19/500) ≥ Φ(19/500)` holds at `p = 14`.)

## (2) Steps

**Step 1 — block 30's T5 arithmetic, restated (CHECKED as E0).**
`(v − 1)/v³` at `v = 3/2` is `4/27`; `t²(4/27 − t)` at `t = 8/81` is `256/531441`;
`t(4/27 − t)` at `t = 2/27` is `4/729`; `d₃(4150) > 256/531441 > d₃(4165)`;
`d₃(367) > 4/729 > d₃(368)`. On `(p, 1, 2)`,
`d₁ = 33/(p³ + 33)`, `d₂ = (p + 32)/(p(p + 1) + 32)`,
`d₃ = (2p + 11)/(p² + 2p + 11)`, `ε₂ = max(d₂, d₃)`.

**Step 2 — G-lifts are diamond-free (PROVED; CHECKED as E4).**
The lift of a subtree `T` of `G` (block 25 T5) sends a node to the word of edge
types along the unique path from the root in `T`. Two distinct words that are
`up i` then `up j` versus `up j` then `up i` project to the same site of `G`. A
subtree of `G` has distinct sites, so it cannot contain both words. That pair of
grandchildren is exactly a diamond. Hence every G-lift lies in `𝕋^{DF}`, and
`Σ_{T ∈ 𝓔} x^{a(T)} y^{f(T)} ≤ Σ_{𝕋^{DF}} ≤ Σ_{𝕋}`.
Checked on every 3-ary plane tree with `n ≤ 7` nodes: injective embeddings are a
subset of diamond-free trees, which are a subset of plane trees; the first
diamond appears at `n = 5` (`273` plane, `270` diamond-free); the first
non-injective diamond-free tree at `n = 7` (`7344` vs `7329`); the first time
animals are strictly fewer than injective trees at `n = 4` (`52` vs `55`).

**Step 3 — the diamond-free U-system at `y = 0` (PROVED).**
A U-node of `𝕋` at `y = 0` has three up-slots and no down-slots. Write `A_S` for
the generating function of U-trees whose set of occupied child-directions is
exactly `S ⊆ {1, 2, 3}`, and put `a₀ = A_∅ = 1`, `a₁ = A_{{1}}` (three
symmetric copies), `a₂ = A_{{1,2}}` (three copies), `a₃ = A_{{1,2,3}}`,
`U = a₀ + 3a₁ + 3a₂ + a₃`, `P = a₁ + 2a₂ + a₃` (trees occupying a fixed
direction). Slots fill independently except for the diamond prohibition. Then

```
a₁ = x U,
a₂ = x² (U² − P²),
a₃ = x³ Σ_{allowed triples (s,t,r)} A_s A_t A_r,
```

the sum running over the `216` of `512` occupancy triples that are diamond-free
(CHECKED as E1a: `48` of `64` pairs, `216` of `512` triples). The right-hand sides
are polynomials in `(a₁, a₂, a₃)` with nonnegative coefficients (the pair identity
`U² − P² = (U − P)(U + P)` with `U − P = 1 + 2a₁ + a₂` increasing), so the map is
monotone on the positive orthant. A triple dominating its right-hand side is a
super-solution: the height-`h` truncations started at `(0, 0, 0)` stay below it,
and the generating function is at most `U`.

**Step 4 — rational super-solution at `x = 3/20` (CHECKED as E1b–E1f, E2).**
At `x = 3/20 > 4/27`,

```
(a₁, a₂, a₃) = (12/25, 1/5, 2/25)
```

satisfies `a₁ ≥ xU`, `a₂ ≥ x²(U² − P²)`, `a₃ ≥ x³ Φ` with
`U = 78/25` and positive margins `3/250`, `107/62500`, `508933/125000000`.
(The original slot-product `U = (1 + xU)³` has no finite solution at this `x`.)
The D-equation at `y = 0` is `D = (1 + xU)²(1 + 3x D)`. With this `U`,
`1 + xU = 367/250` and `3x(1 + xU)² = 1212201/1250000 < 1`. The rational
`D̄ = 72` satisfies `D̄ ≥ (1 + xU)²(1 + 3x D̄)` with margin `6937/312500`.
The slot-product at the root (three up-slots still independent: an upper bound
on `𝕋^{DF}`, which itself upper-bounds G-trees)

```
R̄ = (1 + xU)³ (1 + 3x D̄) = 8254954121/78125000 < 106
```

is therefore a bound on `Σ x^{a} ` over `𝓔` at `y = 0`.

**Step 5 — the new t-trick ceiling and `p = 4004` (PROVED from Step 4; CHECKED as E3).**
T3's conversion `ε₁^{|S|} ε₂^{|A|} ≤ ε₁ t^{E} (ε₁/t³)^{F} (ε₂/t²)^{|A|}` for
`T ∈ 𝓔` with `E ≤ 3F + 2|A|` and `t ≤ 1` is unchanged. The arrow-slot weight is
`x = t + ε₂/t²`. Finiteness at `y = 0` now requires only `x ≤ 3/20`, hence
`ε₂ ≤ t²(3/20 − t)`, whose maximum on `(0, 3/20)` is `1/2000` at `t = 1/10`.
On `(p, 1, 2)`, `ε₂(4003) ≥ 1/2000 > ε₂(4004)`, and at `p = 4004`, `t = 1/10`,

```
t + ε₂/t² = 437437/2916370 < 3/20,
ε₁ R̄ = 24764862363/455910455234375000 < 10^{-7} < 1/2.
```

The seed weight `y = ε₁/t³` is not zero (`≈ 5.14 · 10^{-7}`). The certificate of
Step 4 is at `y = 0`. Extending it to this `y` is **ASSUMED**: the factor
`(1 + y F)^6` is `1 + O(y)` and the super-solution margins of Step 4 are
`10^{-3}`–`10^{-2}` in `U` and `2 · 10^{-2}` in `D`, while `y < 10^{-6}`. A referee
who refuses the perturbation may take the claim as the `y = 0` domain statement
only (the ceiling of T5 is the `y = 0` section of the domain in any case: seed
noise is not the obstruction).

**Step 6 — the 3-type set-product is not a valid animal bound (PROVED; CHECKED as E5).**
A past-cluster `S = Anc(x)` is a directed animal in the 3-predecessor DAG. Its
weight `w(S) = ε₁^{n₀} ε₂^{n₁}` (processed sites contribute `1`) is a valid
union-bound term. Decomposing `S` from the root into sub-animals `S_i` in the
predecessor cones, those cones *overlap*: the site `−e_i − e_j` lies in both
cone `i` and cone `j`. On `S = {0, −e₁, −e₂, −e₁−e₂}` the root is processed, the
two mid-sites are amplified, and the diamond site is a seed, so `w(S) = ε₁ ε₂²`.
Each predecessor-animal is a single amp-plus-seed of weight `ε₁ ε₂`, and the
product is `ε₁² ε₂²`. For `ε₁ < 1` the product is strictly smaller. Exact at
`p = 14`: `w(S) = 1587/3696187`, product `4761/933119209`. Therefore
`Σ_S w(S)` is not dominated by iteration of `Φ(A) = ε₁ + 3ε₂ A + 3A² + A³` via
the comparison `w(S) ≤ w_root ∏ w(S_i)`. That comparison is the first failing
step. (A super-solution of `Φ` can still exist — `19/500` works at `p = 14` —
and on the depth-2 cone the animal sum happens to lie below it, CHECKED as E6;
neither fact repairs the comparison.)

**Step 7 — small-cone domination, not a threshold (CHECKED as E6).**
On the depth-1 and depth-2 backward cones of `η'`, with exact
`P(η'_root = 1)` and the animal-sum over the `185` directed animals of the
depth-2 cone: at `p = 14, 20, 50` on `(p, 1, 2)`,
`P_{d=1} ≤ P_{d=2} ≤ animal-sum ≤ Ā` for the product super-solutions
`19/500`, `7/1000`, `1/1000` respectively. This is finite evidence that a set
bound, *if it were proved*, would dominate the true error probability on those
cones. It is not a proof for the infinite lattice.

## (3) First failing step of the set-route

Step 6: the product comparison on overlapping cones. The diamond
`{0, −e₁, −e₂, −e₁−e₂}` is the minimal counterexample.

The diamond-free *tree* route does not fail at a combinatorial step. Its open
step is the `y > 0` perturbation (Step 5, ASSUMED) and, for a threshold near
the executed `11`, everything else: the bad-pair budget of `2` excuse arrows per
amplified pole (block 30 N1.5 / PR #8175), forks, and the remaining gap from
`1/2000` down to `ε₂(11) ≈ 1/4`.

## (4) What would finish it

- A super-solution of the diamond-free system at a concrete `(x, y)` with
  `y = ε₁/t³ > 0` (drop the perturbation assumption), or a monotone comparison
  showing the `y = 0` super-solution remains one for `0 < y ≤ ε₁(4004)/(1/10)³`.
- A set generating function that tracks the diamond site's occupation as a
  *joint* type of the two cones (a 2-port or heap transfer), so that `w(S)` is
  counted once with the union's types; a rational super-solution of that system
  at `ε₂ > 4/27` would be the set-count asked for in the task.
- Independently: a two-scale block estimate (candidate (ii)) whose one-block
  kernel is the exact depth-`L` polynomial computed here for `L = 2`.

Nothing in this attempt edits notes or runners.
