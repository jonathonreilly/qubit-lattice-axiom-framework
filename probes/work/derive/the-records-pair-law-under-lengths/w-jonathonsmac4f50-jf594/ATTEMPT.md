# Do block 60's lengths change the records' pair law? — attempt 1

Worker `w-jonathonsmac4f50-jf594`, model `claude-opus-5-5`. Blocks 59, 60 and 95–98 were written by the campaign supervisor, who is from the same model family (Claude), so a referee from another family is needed. No prior attempt was printed at claim time.

## 1. Statement

**Setting.**
- Records hop from `x` to an empty neighbour `y` at rate `w_x · s(l_b) · h/6`.
- The hop is timed by the occupied site `x` (block 97, `a = 1`).
- It crosses the bond at a factor `s` of the bond's length `l_b = χ_xχ_y`. Block 60 crosses bonds at `√(w_xw_y)/(χ_xχ_y)`, and block 59 defines `l_b = √(w_xw_y)/c_b`.
- The natural `c_b`-type choice is `s = 1/l_b`, but `s` may be any positive function of `l_b`.
- `h = W(C')/(W(C) + W(C'))`, as in block 95.

**(a) Stationary laws.**
- In any held field `(w, l)`: the stationary law is `π(C) ∝ W(C) Π_{z∈C} 1/w_z` for any number of records. The lengths drop out completely.
- In the field slaved to the records at first order (block 60 T4's one-body field, superposed): the chain is reversible with the pair law `π(C) ∝ W(C) Π_{pairs} exp(−log w_1(r − s))`. Again there is no trace of the lengths.

**(b) The wave's turn.**
- Under block 60, at first order: `log w_1 = −2Qg`, `log l_1 = +2Qg`, and `β = 1`.
- So the wave's turn is `δ(b) = 4 log g(b)`, where `g` is the pair excess per site.
- For general `β` it is `δ = 2(1 + β) log g`.
- This confirms the conditional sentence in block 98's corrigendum.

**Contrast.**
- If a hop reads its own site's length (rate `w_x/l_x`), the pair law picks up `log l_1`, and `δ = 2 log g`.
- If the excess is referred to physical volume `l³` per site, `log g_vol = −4Qg = −δ/2`.

## 2. Steps

**A1 (PROVED, CHECKED): held field.**

*Detailed balance.*
- Let `D = C∖{x}`.
- Then `π(C) · rate(C → C') = W(C)Π_D(1/w) · (1/w_x) · w_x s(χ_xχ_y) · W'/(6(W + W'))`.
- This equals `Π_D(1/w) · s(χ_xχ_y) · WW'/(6(W + W'))`, which is symmetric under `(C, x) ↔ (C', y)`.

*Checked* on a ring of five, with all five rates and all five lengths symbolic and `s` an undefined function:
- one record;
- two and three records, with exclusion and pair weights on occupied bonds.

*Kinetics.* Per own tick the hop rate is `s(l_b)`. So the lengths change the kinetics, including the direction odds, which favour short bonds, but they do not change the stationary law.

*Control.* With the occupied site's own length, rate `w_x/l_x`, the law is `l/w`, and `1/w` is not stationary.

**A2 (PROVED, CHECKED): slaved field at first order.**

*The first-order field.* Block 60 T4 gives `χ = 1 + ΣQ_i g_i` and `N = 1 − ΣP_i g_i`, with `P_i = Q_i w_i = Q + O(Q²)`. To first order the logarithms superpose:
- `log w_z(C) = Σ_r ω(z − r)` with `ω = −2Qg`;
- `log χ_z(C) = Σ_r λ(z − r)` with `λ = Qg`;
- both one-body functions are even.

*The bond length cancels.*
- The record moves from `x` to `y`, and the others form `D`.
- Before the move, `log(χ_xχ_y)(C) = λ(0) + λ(x − y) + Λ_D(x) + Λ_D(y)`.
- After the move it is the same, because `λ` is even.

*The pair law.*
- The rate ratio reduces to block 95 T2's: `log w_x(C) − log w_y(C') = Ω_D(x) − Ω_D(y)`.
- The pair sum `Σ ω` changes by the opposite amount.
- So `π ∝ W Π_{pairs} e^{−ω}`.

*Checked exactly* on the 3³ torus with generic even rational one-body factors: 4050 moves of two records, and 6870 of three.

*Controls.*
- A symmetric but non-product bond factor `1/(χ_x + χ_y)` breaks reversibility of this pair law. So the product form of block 60's bond length matters.
- Counting pairs twice (the held-field law evaluated in the slaved field) is not stationary.

**A3 (CHECKED): the variant that reads its own site's length.** With rate `w_x/l_x(C)`, the slaved pair law is `Π_{pairs} e^{log l_1 − log w_1}`.

**B1 (CHECKED).** This is block 98 T2: the transverse gradient of `1/(4πr)` integrated along the line at impact parameter `b` gives `−2/(4πb)`.

**B2 (CHECKED): block 60 T4 at first order.**
- `log w_1 = −2Qg(b)`.
- `log l_1 = log χ² = +2Qg(b)`.
- Hence `l = 1/w` to this order, i.e. `β = 1`, consistent with block 60 T3.

**B3 (PROVED, CHECKED): the turn.**

*The wave's side.*
- A wave of the walk crosses bonds at `c_b = √(w_xw_y)/l_b` (block 59).
- At long wavelength `log c = log w − log l = −4Qg`.
- Block 59 T4: a ray crossing the gradient bends at `−c²∇ log c`.
- Along a straight passage, B1 gives `δ(b) = 2|log c_1(b)| = 8Qg(b)`.

*The records' side.* From A2, `log g_pair(b) = −log w_1(b) = 2Qg(b)`.

*Result.*
- `δ = 4 log g`.
- For general lengths `l = (w̄/w)^β`, `δ = 2(1 + β) log g`: this is 2 for block 54's product form (`β = 0`) and 4 for the curvature member.

**B4 (CHECKED): the variant.** With A3, `log g = 4Qg` and `δ = 2 log g`.

The number is fixed by how a record's hop sees a length:
- as a symmetric factor of the bond crossed, the relation is `4 log g`;
- as its own site's length, it is `2 log g`.

The task's `c_b`-type crossing is the first.

**B5 (CHECKED): a remark on the measure.**
- The excess above is per site.
- Per physical volume `l³` it is `log g_vol = log g − 3 log l_1 = −4Qg = −δ/2`.
- In that measure a second record is less likely near the first, even though it is more likely per site.

## 3. First failing step

None.

## 4. Not claimed, and what would finish it

1. **Beyond first order.** Block 60 T4's exact slaved field is nonlinear:
   - the `Q_i` solve `Q_iχ(x_i) = m/(8K)`;
   - `P_i = Q_i w_i`;
   - so the bond length need not be the same before and after a move.

   Reversibility at second order is open.
2. **The strong-field far-field ratio.** Block 60 T4's far-field bending over fall is `1 + (1 + 2Qg₀)/(1 + Qg₀)`, which would give `δ/log g = 2(1 + 2/(1 + w₀))` if the pair law kept its first-order form there. This is not worked.
3. **Which reading is supplied.** Two choices are left to the owner:
   - whether a record's hop sees the bond's length or its own site's length, or none (block 97's principle extended to lengths gives rate `w_x`, and then the lengths trivially do not enter);
   - whether "found at that distance" counts sites or physical volume.

ASSUMED: nothing beyond the named notes' definitions.
