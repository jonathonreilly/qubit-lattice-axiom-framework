# chessboard-repair, attempt 1 (worker w-jonathonsmac4f50-j877a, model claude-opus-5)

## (1) The statement attempted

Objects of block 17 (PR #8151): tori `T_L = (Z/2L)^d`, `d = 2, 3`, `N = (2L)^d`; the static law
`μ_L(v) = Π_bonds φ(v_x, v_y)/Z_L` of the six-axis rule, `φ = p, q, r` on same, antipodal, orthogonal pairs, `m = max(q, r)`;
bad bonds, cells `[x, x+1]^d`, the canonical cell of a bond, the site reflections `θ_{i,k}: x_i ↦ 2k − x_i`, the chessboard
estimate T3 in its general form `μ_L(∩_{c∈S} A_c) ≤ Π_{c∈S} μ_L(A_c^{diss})^{1/N}`, and the chain T4 → corollary → T5 (2D),
T6, T7 (3D). The defect (issue for `J:attack:PR8151`): T3 identifies the disseminated event of "the canonical direction-`i`
bond of the cell is bad" as "every direction-`i` bond is bad"; site reflections preserve the parities of the transverse
coordinates, so it is only one parity class of those bonds.

**Statement.** Assume `p ≥ m`.
- (R1) Under site reflections the disseminated event of "the canonical direction-`i` bond of `c` is bad" is
  `E_i^π`: "every direction-`i` bond whose transverse coordinates have the parities `π` of `c`'s is bad".
- (R2) Every pattern in `E_i^π` has at least `N` bad bonds when `d = 2` and at least `3N/4` when `d = 3`; both are attained.
- (R3, route A: site reflections only) `μ_L(E_i^π)^{1/N} ≤ 6m/p` for `d = 2` and `≤ 6(m/p)^{3/4}` for `d = 3`. Hence block 17's
  T4–T6 hold as stated on `Z²` (threshold `p ≥ 216m`), and T7 holds on `Z³` for `p ≥ 1296m = 6⁴m`.
- (R4) If `p ≥ q` and `p + q ≥ 2r` (`φ` positive semidefinite, block 17's T1 remark), `μ_L` is reflection positive for the
  bond-plane reflections `x_i ↦ 2k + 1 − x_i`. On the four-site ring this holds iff `φ` is positive semidefinite.
- (R5, route B) If `φ` is positive semidefinite and `2L` is a power of two, then for every direction `i` and every set `B_i`
  of direction-`i` bonds, `μ_L(every bond of B_i is bad) ≤ (6m/p)^{|B_i|}`; for a set `B` of `n` bonds in two directions,
  `μ_L(every bond of B is bad) ≤ (6m/p)^{n/2}`.
- (R6) `p ≥ 216 max(q, r)` implies `p ≥ q` and `p + q ≥ 2r`. So block 17's conclusions (long-range order in every coordinate
  plane, and at least two Gibbs states on `Z²` and on `Z³` for `p ≥ 216 max(q, r)`) hold with its constants, through R5.

## (2) Steps

**Step 1 — the disseminated event (PROVED; CHECKED as A).** A cell `[x, x+1]^d` has `2^{d−1}` direction-`i` bonds, at the
transverse corners; its canonical one sits at the corner `x`. For `j ≠ i`, `θ_{j,k}` sends the cell at `x_j` to the cell at
`2k − x_j − 1` and the bond at transverse coordinate `x_j` to `2k − x_j`, which has the parity of `x_j`. `θ_{i,k}` moves the
bond along direction `i` and leaves its transverse coordinates fixed. So in every cell the image of the canonical bond is the
direction-`i` bond of that cell whose transverse coordinates have the parities of `x`. No site reflection fixes a cell,
because `2k − x_j − 1 = x_j` has no integer solution, so the image does not depend on the path. The intersection over all
cells is `E_i^π`. On `(Z/4)², (Z/8)², (Z/4)³, (Z/6)³` the orbit has exactly `N/2^{d−1}` bonds, all of one parity class.

**Step 2 — the one-line lemma (PROVED; CHECKED as B-i).** Let `s`, `a` be cyclic sequences of length `n` with
`a_t ≠ a_{t+1}` for every `t`, `bad(s)` the number of `t` with `s_t ≠ s_{t+1}`, and `bad(s, a)` the number of `t` with
`s_t ≠ a_t`. Then `bad(s) + 2 bad(s, a) ≥ n`.
*Argument.* If `s_t = s_{t+1}` (a good bond of `s`), then since `a_t ≠ a_{t+1}` at least one of `s_t ≠ a_t`, `s_{t+1} ≠ a_{t+1}`
holds. Each position `t` lies in two bonds of `s`, so `bad(s, a) ≥ (n − bad(s))/2`. Checked exhaustively for `n = 4, 6`
(all `s`, all `5^n ± 5` admissible `a`).

**Step 3 — the counting lemmas R2 (PROVED; CHECKED as B-ii, B-iii).**
*d = 2, class of even rows (the other classes follow by translation or rotation).* Every even row has all `2L` horizontal bonds
bad: `L · 2L = N/2` bonds. For an odd row `y`, step 2 with `a` = row `y + 1` and with `a` = row `y − 1` (both even, hence
proper) gives `bad_h(y) + 2U_y ≥ 2L` and `bad_h(y) + 2D_y ≥ 2L`. Adding, `bad_h(y) + U_y + D_y ≥ 2L`, where `U_y, D_y` count
the bad vertical bonds from row `y` up and down. Every vertical bond joins an odd row and an even row, so it is counted in
exactly one odd row's `U` or `D` (for `2L = 2` the two vertical bonds between the rows are distinct bonds). Total:
`≥ N/2 + L · 2L = N`.
*d = 3, class of direction-1 lines with both transverse coordinates even.* Those `L²` lines give `N/4` bad bonds. A line with
transverse parities (odd, even) has its two direction-2 neighbours in the class, so by the argument above
`bad_1 + U_2 + D_2 ≥ 2L`. Likewise a line (even, odd) with its direction-3 neighbours: `bad_1 + U_3 + D_3 ≥ 2L`. These
bonds are distinct from each other and from the class lines' bonds. Total: `≥ N/4 + 2L² · 2L = 3N/4`.
*Sharpness.* Even rows alternating `0, 2` with odd rows constant `0` give exactly `N` bad bonds; class lines alternating
`0, 2` with every other site `0` give exactly `3N/4` (checked on sides 4 and 6). On the `4 × 2` torus all `6⁸` patterns were
enumerated: the minimum over the event is `8 = N`.

**Step 4 — route A (PROVED).** With `p ≥ m`, a pattern with `b` bad bonds weighs at most `m^b p^{dN−b}`, which decreases in
`b`. So `Σ_{v∈E_i^π} Π φ ≤ 6^N m^{b₀} p^{dN−b₀}` with `b₀ = N` (d = 2) or `3N/4` (d = 3), while `Z_L ≥ 6p^{dN}` (the constant
patterns). The `N`-th root gives R3. Block 17's corollary uses only monotonicity: a joint event of a cell is contained in its
single-bond events, and every cell's disseminated single-bond event is one of the `E_i^π`. So the corollary holds with
`ε = 6m/p` in 2D, and with `ε₃ = 6(m/p)^{3/4}` in 3D for the in-plane bound `μ_L(B bad) ≤ ε₃^{n/2}` of T7. T5's counting
needs `ε ≤ 1/36`, i.e. `p ≥ 216m` in 2D and `6(m/p)^{3/4} ≤ 1/36`, i.e. `p/m ≥ 216^{4/3} = 6⁴ = 1296` in 3D (CHECKED as E).
Checked exactly on the `4 × 2` torus at `(216,1,1)` and `(432,1,2)`: `μ(E_1^{even})^{1/N} = 0.00927, 0.00872 ≤ 6m/p = 0.0278`.

**Step 5 — bond-plane reflection positivity R4 (PROVED; CHECKED as C).** Take the reflection `θ: x_i ↦ 1 − x_i` on a torus of
even side. It fixes the two planes `x_i = 1/2` and `x_i = L + 1/2` and has disjoint half-spaces `H^± `. The bonds split into
those inside `H^+` (weight `W^+`), those inside `H^−` (weight `W^−(v) = W^+(θv)`), and the crossing bonds `{x, θx}`. If `φ`
is positive semidefinite, write `φ(a, b) = Σ_k λ_k f_k(a) f_k(b)` with `λ_k ≥ 0` and real `f_k` (spectral theorem for the
real symmetric `6 × 6` matrix; its eigenvalues are block 17's T1). Then
`Π_{crossing} φ(v_x, v_{θx}) = Σ_α c_α g_α(v_{H^+}) g_α(θ^{−1}v_{H^−})` with `c_α ≥ 0`, and for every `F` of `H^+`
`Z_L E[F · F∘θ] = Σ_α c_α (Σ_{v_{H^+}} F W^+ g_α)² ≥ 0`. *Converse on the four-site ring* `0–1–2–3–0` with `H^+ = {1, 2}`:
the form is `Σ F(a)F(b) φ(a₁,a₂)φ(b₁,b₂)φ(a₁,b₁)φ(a₂,b₂) = Gᵀ(φ⊗φ)G` with `G(a) = F(a)φ(a₁,a₂)` arbitrary. `φ⊗φ` has the
eigenvalue `Z₁λ < 0` whenever `φ` has an eigenvalue `λ < 0`, so the law is reflection positive there iff `φ` is positive
semidefinite. Exact witnesses: `Q(F) = −552` at `(5,2,4)` and `−288` at `(1,3,2)`. Random rational `F` are nonnegative at
`(3,1,2)`, `(7,3,5)`, `(216,1,1)`. On the `4 × 2` torus the reflection matrix has smallest eigenvalue about `−1.40` (scaled)
at `(5,2,4)`, with an exact rational witness `Q(F) < 0`, and `≥ −5·10^{−16}` at `(3,1,2)`, `(216,1,1)` (floating point).

**Step 6 — route B chessboard R5 (PROVED, with block 17's T3 iteration ASSUMED as re-proved there).** Fix direction `i`. Use site
reflections `θ_{i,k}` in direction `i` (reflection positive for every `φ`, block 17's T2) and bond-plane reflections in every
direction `j ≠ i` (step 5). T3's proof is an iterated Cauchy–Schwarz, one direction at a time, halving the undisseminated
slab positions each time. It applies verbatim when `2L` is a power of two. In direction `i` the slabs are `{k ≤ x_i ≤ k+1}`,
as in T3; in direction `j ≠ i` they are the single layers `{x_j = b}`. The cells `{k ≤ x_i ≤ k+1} × Π_{j≠i}{x_j = b_j}`
number `N` and each contains exactly one direction-`i` bond. The reflections act on them without fixed cells: a bond-plane
reflection sends layer `b` to `2k + 1 − b ≠ b`. The image of "this cell's bond is bad" is "that cell's bond is bad", so the
disseminated event is "every direction-`i` bond is bad" (checked as A: the orbit is all `N` bonds). Block 17's T4 computation
for that event is correct as written and gives `≤ 6m/p` after the `N`-th root, hence `μ_L(B_i bad) ≤ (6m/p)^{|B_i|}`. For
`B = B₁ ∪ B₂`, `μ_L(B bad) ≤ min_i μ_L(B_i bad) ≤ (μ_L(B₁ bad) μ_L(B₂ bad))^{1/2} ≤ (6m/p)^{n/2}`.

**Step 7 — restoring T5–T7 (PROVED).** T5 uses the bond configuration only through `μ_L(B bad) ≤ ε^{n/2}` for in-plane sets
with `ε = 6m/p ≤ 1/36`, plus the counting (unchanged). T6 uses T5 and standard facts along any sequence of tori with
`L → ∞`; take sides `2L = 2^k ≥ 64`, which satisfies T5's `L ≥ 2L' + 2`, `L' ≥ 10`. T7 uses the in-plane bound on the 3D
torus. Step 6 supplies these bounds when `φ` is positive semidefinite, and `p ≥ 216 max(q, r)` gives `p − q ≥ 215q > 0` and
`p + q − 2r ≥ 214r > 0` (CHECKED as E). So block 17's conclusions hold as stated, in 2D and 3D, for `p ≥ 216 max(q, r)`.

## (3) Where the route could fail

A referee should press step 6: that T3's direction-by-direction halving argument uses nothing but reflection positivity of each
reflection employed and the slab structure, so it transfers to single-layer slabs in the bond-plane directions. Also check
that the cells for different directions `i` may differ, since each direction's bound is proved separately and the directions
are combined only by `min ≤` geometric mean. Step 3's bookkeeping, that each vertical bond is counted once, is the other
point. Route A in 3D (`1296m`) cannot be improved within site reflections alone: the `3N/4` patterns are in the event.

## (4) What would finish it, and what it does not decide

Block 17's chain is repaired with its own constant `216`. Its true optimal threshold is not found: the executed ordering
strength is near `p ≈ 3.6–3.7` (block 28), and moving `216` down needs a sharper contour count or chessboard bound, not
attempted here. Necessity of `φ ⪰ 0` for bond-plane reflection positivity is decided on the four-site ring and numerically on
the `4 × 2` torus, not on every torus; the repair does not need it.
