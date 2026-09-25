# Facet growth from two-move paths, attempt 1: exact departure rates of the (111) and (110) facets, and (111) turns last

Worker `w-macbookpro9927a-jf7c6` (Claude Opus 5.5, `claude-opus-5-5`). The checks are in `check.py` in this directory. They run in about a minute with a peak of about 70 MB.

The families are:
- Q: pinned sources.
- A: facet departure rates.
- B: the growth law per facet.
- C: clusters and turning sizes.
- N: `[float]` scans.

Families A to C are exact: rational arithmetic, exact linear solves, and sympy with `√17` and `√(x²+2)`. Family N is floating point and is marked so.

## Sources, provenance and route

**Sources.**
- **Block 39**, as landed on main (pinned at `60c5f194`).
  - Pair-weight transit: "a bond with exactly one occupied end is visited …; it moves with probability `w_y/(w_x + w_y)`".
  - The neutral scale `c₀ = 6/(p+q+4r)`.
  - Formation at rate `zZ_x`.
- **Block 127**, PR #9184 at head `2cc2429c`.
  - Its rate convention: "Every bond is visited at rate `1`".
  - Its accounting: "`E` counts moves to an isolated site; the departed record has left the cluster" and "Formation at the touching sites gives `G = 6zcA₁L²`".
  - T4's first hops: "On `(111)` … a hop of probability `1/(1+x)` …; On `(110)` that hop has probability `1/(1+x³)`".
  - Its open item: "a growth law from two-move paths".
- **The task text**, from `probes/TASKS.json` at `61392c88`.

Family Q checks the hashes and the quotes verbatim.

**Provenance.**
- The claim printed no prior attempts on this problem.
- The related problem `moving-jammed-clusters` has three attempts:
  - a2 (#8680), by the same model family on another machine, is what block 127 harvests;
  - a3 (#8992), mine: a census of the arrangements a box reaches in T moves, with no rates and no tied facets;
  - a1.
- Block 127 lists my a3 as unrefereed and does not use it. Neither do I.
- I use block 127's definitions and T3/T4 facts, and I re-derive every number I use from block 39's clause.

**Route.**
1. Extend block 127's instantaneous accounting of the ideal shape to two-move paths, by following the moved record until it first reaches an isolated site.
2. Solve that first-passage problem exactly for each facet. It has one state for (111) and a half-infinite line for (110).
3. Check every rate against a direct lattice computation.
4. Add formation for the growth law.
5. Do the same for finite clusters bounded by each facet type, which gives turning sizes.

## Definitions

**The model.**
- Records are aligned, and `x = cp` is the weight of a bond between two records. A bond with an empty end weighs `1`.
- Every bond with exactly one occupied end is visited at rate `1`.
- The record at `s` moves to the empty end `t` with probability `x^{k_t}/(x^{k_s} + x^{k_t})`. Here `k_s` counts the recorded neighbours of `s` other than `t`, and `k_t` those of `t` other than `s`. This is block 39's `w_t/(w_s + w_t)`, since `w = x^k`.
- An empty site with no recorded neighbour is *isolated*.

**Held-shape first passage.**
- After a first hop `s → t`, the moved record keeps moving under the same clause while the rest of the shape is held. That is, `s` stays empty and no other record moves.
- It moves until it reaches an isolated site, which is a *departure*, or re-enters `s`, which is a *return*.
- `E_F` is the departure rate per surface record of the ideal facet `F`: `E_F = Σ_t (first-hop rate s → t) · P_t(departure before return)`. The departure rate per unit area is `E_F/|n|`, with `|n| = 1, √2, √3` for (100), (110) and (111).
- This is block 127's accounting, "a record that moves to an isolated site has left", followed beyond one move. For (111) every departure takes exactly two moves. For (110) a departure is a first hop followed by a walk along a groove.

**Formation.** Formation happens at rate `zZ_x`, with `Z_x = c^jA_j`, `A_j = p^j + q^j + 4r^j`, at an empty site with `j` aligned recorded neighbours. As in block 127, all contents are counted.

## (1) The statement attempted

**(A) Departure rates per surface record.** These hold for every `x > 0`.

| Facet | `E_F` | Mechanism |
|---|---|---|
| (100) | `1/(1+x⁵)` | one move |
| (111) | `9/(x³ + 4x + 3)` | exactly two moves |
| (110) | `4(σ + x² + 2x) / ((x⁴ + 3x³ + 2)σ + 3x⁵ + 5x⁴ + 2x² + 4x)`, with `σ = √(x²+2)` | a first hop, then a walk along the groove |

More on (110):
- Its part from paths of exactly two moves is `4/((x+1)(3x³+2))`.
- At `x = 1`, `E(110) = 2√3/(1+2√3)`.
- At `x = 3/2`, `E(110) = (2402 − 162√17)/5575`.

As `x → ∞`, `E(111) ≈ 9x^{−3}`, `E(110) ≈ x^{−3}` and `E(100) ≈ x^{−5}`. Every departure path satisfies forward/backward `= x^{−k_s}`.

**(B) The growth law per facet.**
- Each surface record has exactly one touching site, which has `j = 1, 2, 3` recorded neighbours on (100), (110) and (111).
- The net rate per surface record is `n_F = z c^jA_j − E_F`, and the normal velocity is `n_F/|n|`.
- So facet `F` advances iff `z > z_c(F) = E_F/(c^jA_j)`.
- At `(3,1,2)`, where `c = 1/2` and `x = 3/2`:
  - `z_c(100) = 16/825`, block 127's value;
  - `z_c(110) = 4(1201 − 81√17)/72475 ≈ 0.04785`;
  - `z_c(111) = 16/165`.

**(C) Clusters.** At `x = 3/2` with `(3,1,2)`:

*The octahedron `|v|₁ ≤ R`.*
- `E(R) = 4(R−1)(R−2)e₃ + 12(R−1)e₂ + 6e₁`, with
  - `e₃ = 9/(x³+4x+3)`;
  - `e₂ = 8/((1+x)(4+x)) + 6/(7+x²)`;
  - `e₁ = 1/(1+x) + 16/(9+x)`.
- `G(R)/z = 4R(R−1)Z₃ + 12R Z₂ + 6Z₁`.
- Both hold for every `R ≥ 1`.

*Size-dependent critical rates `E/G`.*
- The octahedron's rate is the highest at every size computed. The rhombic dodecahedron comes second, then block 127's box.
- At `z = 1/10` the octahedron shrinks for `R ≤ 12` and grows from `R = 13` on. The box and the dodecahedron grow at every size computed from `L, R = 2`. At `R = 1` both polyhedra are the same seven-site cluster.
- At `z = 1/20` the octahedron shrinks at every size.

So the (111) facet has the largest turning size.

*Under the kinetic Wulff construction (ASSUMED).*
- (111) facets bound the growing cluster at every `z`.
- It is a regular octahedron for `16/165 < z < 112/275`.
- (100) facets appear at `z₁ = 112/275`, and (110) facets at `z₂ = 8/11 − E(110) ≈ 0.4162`.

## (2) Steps

**Step 1 (PROVED): the rules.**
- A bond visited at rate `1` moves the record with the probability above.
- The one-record chain of the held shape is reversible for the weight `x^{#record bonds}`: each move has forward/backward `= x^{k_t−k_s}`, block 39's balance.
- The first-passage probabilities are the harmonic solutions with value `1` at isolated sites and `0` at `s`.

**Step 2 (PROVED): (100) departs in one move.** A surface record of `{v₃ ≤ 0}` has `k_s = 5` and one empty neighbour, `s + e₃`, which is isolated. So `E(100) = 1/(1+x⁵)`, block 127's face term.

**Step 3 (PROVED): (111).** Take the facet `{v₁+v₂+v₃ ≤ 0}` and its surface layer `Σ = 0`.
- A surface record has `k_s = 3` (below) and three empty neighbours `t = s + e_i`.
- Each `t` has `k_t = 2`: its three lower neighbours, less `s`.
- The empty neighbours of `t` are `s` and the three sites `t + e_j` at `Σ = 2`. Those are isolated, because their other neighbours lie at `Σ = 1` and are empty.
- The sites at `Σ = 1` are never adjacent to one another. So from `t` the record either returns, at rate `x³/(x²+x³) = x/(1+x)`, or departs, at rate `3/(1+x²)`.

Hence `E(111) = 3 · (1/(1+x)) · (3/(1+x²)) / (3/(1+x²) + x/(1+x)) = 9/(x³+4x+3)`. Every departure takes exactly two moves.

**Step 4 (PROVED): (110).** Take the facet `{v₁+v₂ ≤ 0}`.

*The first hop.*
- A surface record has `k_s = 4`: two in its row along `e₃` and two below.
- It has two empty neighbours, `s + e₁` and `s + e₂`, each with `k = 1`. The first hop is `1/(1+x³)` to each.
- The touching sites `Σ = 1` form lines along `e₃` (grooves). The two first-hop sites lie on different grooves, and the only link between the grooves is through `s` or through isolated sites.

*Along one groove, `g_n = s + e₁ + n e₃`.*
- `g_0` has `k = 1`, and every `g_n` with `n ≠ 0` has `k = 2`.
- Each `g_n` has two isolated neighbours, `g_n + e₁` and `g_n + e₂`.
- `g_0` also neighbours `s`.
- The rates:
  - `g_0 → s`: `x³/(1+x³)`;
  - `g_0 →` isolated: `1/(1+x)` each;
  - `g_0 → g_{±1}`: `x/(1+x)` each;
  - `g_n → g_{n±1}`, with `n, n±1 ≠ 0`: `1/2` each;
  - `g_{±1} → g_0`: `1/(1+x)`;
  - `g_n →` isolated, `n ≠ 0`: `1/(1+x²)` each.

*The walk.*
1. Let `ρ_n = P(reach g_0 before departing | g_n)` for `n ≥ 1`.
2. For `n ≥ 2`, `ρ_n = Cμⁿ` with `μ² − 2(1 + 2/(1+x²))μ + 1 = 0`, whose root below `1` is `μ = (σ−1)/(σ+1)`. This uses `x² + 1 = (σ−1)(σ+1)`.
3. The equation at `n = 1` gives `ρ₁ = (σ−1)/(σ+x)`.
4. So a record stepping into the groove departs before coming back to `g_0` with probability `h = (x+1)/(σ+x)`.
5. From `g_0`, with `Φ = 1 + xh`, the probability of departing before returning is `f₀ = 2Φ/(1+x) / (x³/(1+x³) + 2Φ/(1+x))`.
6. So `E(110) = 2f₀/(1+x³)`, which simplifies to the closed form in (A).
7. The closed form decreases in `σ`, since `C − aB = −x⁴(x+1)²`. This makes rational interval checks one-sided.

*The strict two-move part.* This counts only departures at the second move, with the groove moves counted as non-departures. It is `2 · (1/(1+x³)) · (2/(1+x)) / (2 + x³/(1+x³)) = 4/((x+1)(3x³+2))`.

The groove more than doubles it at `x = 3/2`: 0.311 against 0.132.

**Step 5 (CHECKED): family A, the lattice.**
- The check solves the first passage on the actual lattice. The occupied set is `{n·v ≤ 0}` minus `s`, the neighbour counts are computed and the harmonic system is solved exactly.
- (100) and (111) equal the closed forms at `x ∈ {1/3, 1/2, 1, 3/2, 2, 3, 5}`.
- For (110), chains capped at sup-distance 8, 16 and 32, with the cap made absorbing as a return or as a departure, bracket the infinite groove. The closed form, with `σ` bounded by rationals to `10⁻⁴⁰`, lies inside every bracket at `x ∈ {1/2, 1, 3/2, 2, 3}`, and the widths shrink to at most `10⁻¹⁰`.
- The groove solution and its assembly are checked symbolically.
- The strict two-move part holds at seven points.

**Step 6 (PROVED, CHECKED): balance, and dependence on the acceptance.**
- For every two-move departure path `s → t → u`, forward/backward is `[x^{k_t−k_s}]·[x^{0−k_t}] = x^{−k_s}`: `x^{−3}` on (111) and `x^{−4}` on (110). All 39 paths are checked.
- Block 39 also allows any acceptance with the same ratio. With Metropolis, `min(1, w_t/w_s)`, `E(111) = 9/(x(x²+3))` for `x ≥ 1` (checked).
- So the balance ratios are universal, but the rates belong to the heat-bath clause that block 127 uses.

**Step 7 (PROVED, CHECKED): the growth law (B).**
- `v ↦ v + e`, with `e` along a positive normal component, maps surface records one-to-one onto touching sites.
- Their recorded neighbours number `j = |n|₁ = 1, 2, 3`. No other empty site touches the facet.
- Formation adds `z c^jA_j` per surface record, and the net rate and velocity follow.
- At `(3,1,2)`, `Z₁ = 6`, `Z₂ = 13/2` and `Z₃ = 15/2`, which gives the critical rates in (B). They are compared exactly, with `√17`.

**Step 8 (PROVED, CHECKED): the octahedron.** Its surface records fall into three classes.

*Face records* (three non-zero coordinates; `4(R−1)(R−2)` of them). These are as in Step 3, which gives `e₃`.

*Edge records* (one zero coordinate; `12(R−1)` of them). Each has `k_s = 2`.
- Two in-plane first hops, each `1/(1+x)`, go to a site with `k = 1`. From there there are four isolated neighbours at `1/(1+x)` each, and the return is `x/(1+x)`, so `P = 4/(4+x)`.
- Two out-of-plane first hops, each `1/2`, go to a site with `k = 2`. From there there are three isolated neighbours at `1/(1+x²)` each, and the return is `1/2`, so `P = 6/(7+x²)`.
- Together these give `e₂`.

*Tips* (6 of them). Each has `k_s = 1`.
- One one-move departure, at `1/(1+x)`.
- Four first hops, each `1/2`, go to a site with `k = 1`. From there there are four isolated neighbours at `1/(1+x)` each, and the return is `1/2`, so `P = 8/(9+x)`.
- Together these give `e₁`.

*Formation.*
- Touching sites lie at `|v|₁ = R+1`, and `j` equals the number of non-zero coordinates.
- There are `4R(R−1)`, `12R` and `6` sites with `j = 3, 2, 1`.

*Checked.* Both closed forms equal the lattice first passage at `x = 3/2` for `R ≤ 8`, and at `x = 2/3` and `5/2` for `R ≤ 5`.

**Step 9 (CHECKED): the comparison of clusters.**
- **The box.** Block 127's box `E(L)` equals the lattice first passage for `L = 2..6`. All of its departures are single moves.
- **The rhombic dodecahedron.** It is computed exactly for `R ≤ 10`. It has finite grooves, and so no closed form here.
- **The critical rates `E/G` at `(3,1,2)`:**
  - octahedron: 0.1013, 0.1044, 0.1042, … → 16/165;
  - dodecahedron: 0.1013, 0.0604, 0.0603, … → 0.0479;
  - box: 0.0381, 0.0313, … → 16/825.
- **At `z = 1/10`.**
  - The octahedron's quadratic `zG − E` has a positive leading coefficient `4(zZ₃ − e₃) = 1/11`. It is negative up to `R = 12` and positive from `R = 13` to `200`, so the turning size lies between 12 and 13.
  - The box grows for `L = 2..199`, and the dodecahedron for `R = 2..10`. At `R = 1` the dodecahedron is the octahedron's seven-site cluster, which shrinks at this `z`.
- **At `z = 1/20`.**
  - The octahedron's leading coefficient is negative, and it is negative at every `R`.
  - The dodecahedron first grows at `R = 10`.
  - The box grows at every size.
- The octahedron lies above at every size computed. The (111) facet has the largest turning size.

**Step 10 (ASSUMED construction; PROVED algebra): the kinetic Wulff shape.**
- *Assumed.* A growing convex cluster is the inner envelope of the facet planes, each moving at `n_F/|n|`. This is the kinetic Wulff construction, a continuum statement not derived here.
- *The presence rules.* Facet F is present iff its central point `n_F n/|n|²` satisfies the other planes:
  - (100) iff `n₁₀₀ ≤ n₁₁₀` and `n₁₀₀ ≤ n₁₁₁`;
  - (110) iff `n₁₁₀ ≤ 2n₁₀₀` and `n₁₁₀ ≤ n₁₁₁`;
  - (111) iff `n₁₁₁ ≤ 3n₁₀₀` and `n₁₁₁ ≤ (3/2)n₁₁₀`.
- *At `(3,1,2)`.*
  - (111) is present at every `z`: `3n₁₀₀ − n₁₁₁ = (21/2)z + (e₁₁₁ − 3e₁₀₀)` and `(3/2)n₁₁₀ − n₁₁₁ = (9/4)z + (e₁₁₁ − (3/2)e₁₁₀)`, with both constants positive.
  - The first (110) condition holds at every `z`: `2n₁₀₀ − n₁₁₀ = (11/2)z + (e₁₁₀ − 2e₁₀₀)`, with the constant positive.
  - (100) appears at `z₁ = (e₁₁₁ − e₁₀₀)/(Z₃ − Z₁) = 112/275`.
  - (110) appears at `z₂ = e₁₁₁ − e₁₁₀ ≈ 0.4162`.
- *So the growth shape* is an octahedron for `16/165 < z < 112/275`, and then a (100)- and (110)-truncated octahedron.

**Step 11 (`[float]`, family N): scans.**
- `E(111) > E(110) > E(100)` for `x ∈ [0.05, 20]`.
- Along `(p, 1, 2)` at the neutral scale, `z_c(100) < z_c(110) < z_c(111)` for `p ∈ [1.5, 20]`.

## Answer to (c), and how it compares with the box

**The largest turning size.** The facet whose turning size is largest is (111). Its critical formation rate is the highest of the three facets, 16/165 at (3,1,2), five times the box's 16/825. The octahedron's size-dependent critical rate stays above the other shapes' at every size computed. At `z = 1/10` its turning size lies between 12 and 13, while the box and the dodecahedron grow at every computed size from `L, R = 2`.

**The shape of a growing aligned cluster**, under Step 10's construction:
- (111) facets are never outgrown.
- The cluster is a regular octahedron up to `z = 112/275`.
- (100) facets appear at the tips above that, and (110) facets along the edges above `0.4162`.

**Comparison with the box.** Block 127's box is bounded by (100) facets, which the construction removes below `z₁`. The box grows above its own turning size from `z > 16/825`. The (111) orientations exposed at its corners have negative net rate for all `z < 16/165`, and that box accounting holds the corners fixed.

This comparison is a consequence of the per-facet laws inside block 127's accounting, not a result about the many-body dynamics. See the next section.

## (3) Where the route stops

1. **Held shape.** `E_F` follows the moved record with everything else held. In the full dynamics other records move meanwhile. On (111), for example, the vacancy at `s` is refilled from below at total rate `3/(1+x²)`, the same order as the moved record's departure rate `3/(1+x²)`.

   So `E_F` is the exact rate of block 127's accounting extended by first passage. It is not the evaporation rate of the many-body dynamics, whose leading power `x^{−3}` can agree while its prefactor differs.
2. **Formation counted as growth.** A formed record is counted as growth at once, as in block 127. A record formed on (100) has one bond and would usually leave again, which slows real (100) growth into a nucleation-limited process. A record formed on (111) leaves in one move at `3/(1+x³)`.

   The growth-shape conclusion depends on this convention and could reverse under a law that follows formed records.
3. **The Wulff construction.** Step 10 is an assumed continuum construction.
4. **The dodecahedron** is exact only per size, for `R ≤ 10` at `x = 3/2`.
5. **The acceptance.** The rates belong to the heat-bath acceptance (Step 6).

## (4) What would finish it

1. A growth law that follows formed records and the vacancy's own moves. It would include the adatom populations on each facet and the two-dimensional nucleation rate on (100).
2. The full many-body departure rate of an ideal facet, at least its large-`x` prefactor.
3. Clusters with mixed contents.
