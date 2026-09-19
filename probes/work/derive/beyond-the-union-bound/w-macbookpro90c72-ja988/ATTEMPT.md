# beyond-the-union-bound, attempt 2 (worker w-macbookpro90c72-ja988, model grok-4.6)

Plan, locked before using the prior attempts sitting in this worktree: candidate (ii),
a two-scale / local-statistic closure for the two-level automaton `η'` of block 30.
The 4/27 ceiling is a one-generation branching radius; the eroder of 3-input majority
kills every finite island in two steps when `ε₁ = ε₂ = 0`, so a pair-regeneration
kernel of order `ε₂` should replace `x = 4/27` if collisions can be closed.

Route taken: close a pair of statistics `(q, r)` — `q = P(η'_z = 1)`, `r = P` both
sites of a specified fork-adjacent pair are `1` — by one-step majority arithmetic and
the isolated-pair offspring table. The isolated kernel is exact. The closure is not:
every atom-sum upper bound that charges a configuration by `r` whenever it contains a
fork pair has `r`-coefficient `> 1` at every `p`. That is the first failing step.

## (1) The statement attempted

Objects as in block 30 (PR #8174) and block 25 (PR #8168): six-axis formation law in
level time from the all-`a` plane; `ξ ≤ η'` (T1); `ε₁ = d_1`, `ε₂ = max(d₂, d₃)`;
forks are the six displacements `e_i − e_j`.

On `(p, 1, 2)` the closed forms (block 30) are
`d₁ = 33/(p³+33)`, `d₂ = (p+32)/(p(p+1)+32)`, `d₃ = (2p+11)/(p²+2p+11)`.

**A (isolated-pair kernel, exact).** Let `(u, v)` be a fork pair at level `n` with
`v = u + e_i − e_j`, and suppose no other site at level `n` is `1`. Then the next
level contains exactly one majority child `w = u + e_i = v + e_j`, exactly four
`N = 1` children (amplification slots), and seven descendant fork-pairs. Each of the
four amplification children is fork-adjacent to `w`. Given the parent pair,
```
P(at least one descendant fork-pair is both 1) = 1 − (1 − ε₂)⁴ ,
E[# descendant fork-pairs] = 4 ε₂ + 3 ε₂² .
```
The mean is `< 1` iff `ε₂ < (−2 + √7)/3`. On `(p, 1, 2)`, `ε₂ = max(d₂, d₃)` first
drops below that threshold at the integer `p = 13` (`d₂(12) > (−2+√7)/3 > d₂(13)`,
and `d₂ ≥ d₃` for every integer `p ≤ 21`).

**B (2-step eroder, exact on cones).** If `ε₁ = ε₂ = 0`, an isolated fork-pair at the
base of a depth-2 cone produces a singleton at mid-level and `0` at the top. Exhausted
on every depth-2 base pair and every depth-3 configuration with `ε = 0`.

**C (candidate closure, fails).** The one-step bounds `q' ≤ ε₁ + 3 ε₂ q + 3 r` and
`P(N ≥ 2) ≤ 3 r` are valid. The candidate lemma "`r' ≤ ε₁² + c_q q + c_r r` with
`c_r < 1`, obtained by summing `f(N_u) f(N_v)` over the 32 configurations of the
5-predecessor neighbourhood and charging each atom by `r` whenever it contains a fork
pair" is false: that sum's `r`-coefficient is `> 10` at every `p ≥ 11`. The same
atom-sum on the depth-2 cone's 64 base-masks has `r`-coefficient `> 33`. No
super-solution of this linear map exists, so this form of two-scale does not move
the threshold.

## (2) Steps

**Step 1: two predecessors of a site are a fork pair (PROVED; CHECKED as A1).**
The predecessors of `x` are `x − e_a`, `x − e_b`. Their difference is `e_b − e_a`,
one of the six forks. Hence `P(N ≥ 2) ≤ 3 r` and
`q' ≤ ε₁ + 3 ε₂ q + (1 − ε₂) · 3 r ≤ ε₁ + 3 ε₂ q + 3 r`.

**Step 2: isolated-pair geometry (PROVED; CHECKED as B1).**
Place `u` at the origin and `v = u + e_1 − e_2`. Successors of `u`: `u+e_1, u+e_2, u+e_3`.
Successors of `v`: `v+e_1, v+e_2, v+e_3`. The unique common successor is
`w = u+e_1 = v+e_2`. The other four successors have exactly one parent in `{u, v}`.
Fork-adjacency among `{w} ∪ {the four}`: all four `w`–amp edges are forks; three of
the six amp–amp edges are forks. Total seven descendant fork-pairs.

**Step 3: regeneration probabilities (PROVED; CHECKED as B2, B3).**
Given the isolated pair, `w` is `1` with probability `1`. Each of the four amp
children is independently `1` with probability `ε₂`. A descendant fork-pair involving
`w` occurs iff at least one amp child is `1`, so
`P(at least one descendant pair) = 1 − (1 − ε₂)⁴`.
The three amp–amp fork-pairs are occupied only when two amps are `1`, which already
occupies two `w`–amp pairs; they do not change the "at least one" event. By linearity,
`E[# descendant pairs] = 4 ε₂ + 3 ε₂²`.

**Step 4: the mean-1 threshold (PROVED; CHECKED as C1, C2).**
`3 ε² + 4 ε − 1 = 3 (ε − (−2+√7)/3) (ε − (−2−√7)/3)`. For `ε > 0` the mean is `< 1`
iff `ε < (−2+√7)/3`. On `(p, 1, 2)`, `d₂ − d₃ = p²(21−p)/[(p²+p+32)(p²+2p+11)]`,
so `ε₂ = d₂` for integer `p ≤ 21` and `ε₂ = d₃` for `p ≥ 21`. Comparing `d₂(p)` to
`(−2+√7)/3`: `d₂(12) = 55/235 > (−2+√7)/3 > d₂(13) = 45/214`.

**Step 5: atom-sum closure of `r'` (FAILS; CHECKED as D1, D2).**
The 5 predecessors of a specified child fork-pair `(u, v)` are `A, B, C` for `u` and
`B, D, E` for `v` (`B` shared). The 32 configurations partition the past. For each
config `c`, `P(c) ≤ r` if the 1-set of `c` contains a fork pair, `≤ q` if it is a
nonempty isolated set, and `≤ 1` if empty. Then
`r' = Σ f(N_u(c)) f(N_v(c)) P(c) ≤ A₀ + A_q q + A_r r`.
`A_r` equals the sum of `f(N_u) f(N_v)` over the configs that contain a fork pair.
That sum is `> 10` at `p = 200` already (`ε₂ ≈ 1/100`) and `> 12` at `p = 11`.
The same method on the 64 base-masks of the depth-2 cone gives `A_r > 33` at every
tested `p`. Because `A_r > 1`, the linear map on `(q, r)` has no finite super-solution.

The overcount is mechanical: packed majority configs have `f f = 1` and contain a
fork pair, so each is charged `r`; many such configs exist, and the charges add.
This is not a statement that pairs branch in the automaton (Step 3 says an *isolated*
pair has mean `< 1` for `p ≥ 13`). It is a statement that this bounding technique
cannot see that.

## (3) Where the route stops

Step 5 is the first failing step of the closure. Steps 1–4 stand. The route does not
produce a super-solution for `P(η'_x = 1)` and does not move block 30's `p ≥ 4165`
or the history-count certificates of the other attempt on this problem.

## (4) What would finish it

1. A *covering* of `{u = v = 1}` by `O(1)` events, not a 32-atom partition: "this
   isolated pair regenerated" (weight `1−(1−ε₂)⁴` times `r`) plus "two lineages
   met" (a quadratic in `q` or a triple with its own `ε₂`-contracting bound).
2. A history count for the *pair* (two roots joined by one fork), keeping block 30's
   distinctness of seeds, so that `r ≤ ε₁² W_pair` with `W_pair` finite past `27 ε₂ = 1`.
3. Value-aware amplification (`d₂` vs `d₃`) — at `p = 11`, `d₂ = 43/164` still has
   isolated-pair mean `> 1`, so even the dilute pair-BP survives on the antipodal
   slot; a value-aware `η'` is required to reach the located strength.

Imports: block 30 T1 (domination `ξ ≤ η'`) is ASSUMED if anyone turns A into a bound
on the formation law; A–C as stated are about `η'` only. No other import.
