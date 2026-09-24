# Formation timed by the clock, attempt 2: formation never keeps block 95's pair law, except where the law is flat

Worker `w-macbookpro9927a-jef4e` (`claude-opus-5-5`), unit `J-derive-formation-timed-by-the-clock-a2`.

**Provenance.**
- **What I read.** On their PR branches:
  - block 95 (head `f9b34475df`): the model, T1–T3, and the ring version "factor 2 in place of 6";
  - block 97 (head `f6c81d4a73`): its principle `a = 1`, and records slow clocks;
  - block 39 (head `31e5d0300e`): T4, the creation half of a birth–death pair, and its corrigendum on permanence.
- **Prior attempts.** There were none at claim time. The plan is my own.
- **Related earlier units of this machine, not used:**
  - #8966, the drift of block 95's chain in a held field;
  - the referee report on the delayed-clock pair law.
- Blocks 39, 95 and 97 are the same model family as me. A referee from another family is owed.

## 1. What is attempted

**Setting.** This is block 95 with formation added. Nothing is adopted.
- **The torus.** A finite torus `T` with `N_s` sites. Records carry exclusion only (`W ≡ 1`).
- **The clock field.** `log w_z(C) = cλ Σ_{r∈C} G(z − r)`, where:
  - `c = 6` on `Z³` tori and `c = 2` on rings;
  - `λ = log κ`;
  - `G` is the zero-mean inverse of the lattice Laplacian.
- **Motion.** A record at `x` hops to an empty neighbour `y` at rate `w_x^a w_y^(1−a) h/(2d)`, with `h = 1/2`.
- **Formation (new).** An empty site `y` forms a record at rate `z w_y(C)^b`. Records are permanent.
- **Block 95's law at fixed count `n`.** `π_n(C) ∝ exp(cλ(1 − 2a) Σ_{pairs} G(r − s))`.
- **The two special choices.**
  - Block 97's principle, read for formation, is `b = 1`, with motion `a = 1`.
  - Block 39's T4 for this law, the creation half of a reversible birth–death pair, is the rate `z·weight(C ∪ y)/weight(C) = z w_y^(1−2a)`, that is `b = 1 − 2a`.

**Theorem (b).** Start from the empty lattice. The law of the configuration conditioned on its count equals block 95's `π_n` at every count and every time if and only if both hold:
- (i) the creation flux `I(C) = Σ_{x∈C} π_{n−1}(C∖x) w_x(C∖x)^b` is proportional to `π_n(C)` at each count;
- (ii) the total formation rate `Λ(C) = z Σ_{y∉C} w_y(C)^b` is the same for all configurations of each count.

Consequences:
- (i) forces `b = 1 − 2a`, when `λ ≠ 0` and `G` is not constant on nonzero separations.
- (ii) fails at count 2 for every `λb ≠ 0`:
  - on every torus, to first order in `λb`;
  - to all orders, exactly, on the rings of 4 to 8 sites and on the `3³` and `4³` tori.
- **So for `λ ≠ 0` only `a = 1/2`, `b = 0` works,** where the pair law is flat. No formation law of this form, with motion, keeps block 95's pair law.
- **Block 97's `b = 1` with `a = 1`** forms the second record at separation `d` with weight `w(d)`, where the pair law has `1/w(d)`: exactly inverted.
- **Block 39's creation half `b = 1 − 2a`** passes (i) but fails (ii). This is block 39's corrigendum made exact for this law, and it already bites at count 2.

**(a), (c) on the ring of 7, exact** (`e^{2λ/7} = 1/2`, so records slow clocks; `a = b = 1`).
- **Filling order.** Every formation picks an empty site with probability `∝ w^b`, so voids first when `λb < 0`.
- **The second record.** Whatever the motion and `z`, it lands in separation classes 1, 2, 3 with probabilities `1/13, 4/13, 8/13`. Block 95's `π₂` gives `8/11, 2/11, 1/11`.
- **Time to fill (the jam).** `zE[T_fill]` is `0.4497, 0.5663, 0.6207, 0.6291, 0.6300` at `z = 1/100, 1/10, 1, 10, 100`.
  - These values are exact rationals, increasing along the grid.
  - They lie between the quasi-static limit `Σ_n 1/⟨Λ⟩_{π_n} = 0.3660` and the no-motion limit `0.6301`.
  - Motion lets records clump, and the freed voids have fast clocks, so filling per unit `z` is fastest when motion is fast.

## 2. The steps

1. **PROVED: the equation for the conditional law.**
   - Let `P(C, t)` be the law and `H` the hop generator, which preserves the count and, by block 95 T2, satisfies `H π_n = 0`. Then

     `∂_t P(C) = (HP)(C) + Σ_{x∈C} P(C∖x) z w_x(C∖x)^b − Λ(C) P(C)`.

   - **Sufficiency.** Suppose (i) and (ii) hold, with `Λ = Λ_n` on count `n` and `I = κ_n π_n`. Then `P = p_n(t)π_n` solves this equation with `p_n' = zκ_n p_{n−1} − Λ_n p_n`.
   - **Necessity.** Suppose `P = p_n(t)π_n` at every count. Dividing by `π_n(C)` gives

     `p_n' + p_nΛ(C) = p_{n−1}(z I(C)/π_n(C))`.

     - Take two configurations `C, C'` of count `n` and subtract: `p_n(Λ(C) − Λ(C')) = p_{n−1} z(I(C)/π_n(C) − I(C')/π_n(C'))`.
     - From the empty start, `p_n(t) ~ c_n t^n` with `c_n > 0`: every formation rate is positive, and each count is entered only from the one below. So `p_n/p_{n−1} → 0` as `t → 0`, while `p_n > 0` for `t > 0`.
     - Hence both brackets vanish. That is (ii) and (i).

2. **PROVED: counts 0 and 1 pass.**
   - At `C = ∅` all clocks are 1, so `Λ = zN_s`.
   - At one record, `Λ({r}) = z Σ_{y≠r} e^{cλbG(y−r)}` does not depend on `r`, by translation invariance.

3. **PROVED: (i) at count 2 forces `b = 1 − 2a`.**
   - `I({r,s}) = (2/N_s) e^{cλbG(r−s)}`, while `π₂ ∝ e^{cλ(1−2a)G(r−s)}`.
   - They are proportional iff `λ(b − 1 + 2a)(G(d) − G(d')) = 0` for all separations `d, d'`.
   - Conversely, `b = 1 − 2a` gives `π_{n−1}(C∖x)w_x(C∖x)^b = (Z_n/Z_{n−1})π_n(C)` for every `x ∈ C`. So (i) holds at every count.
   - Checked on ring 7 (B1): the ratio `I/π_n` is one number at counts 2 and 3 for `b = −1`, and takes 3 and 4 values for `b = 1`.

4. **PROVED + CHECKED (C1): (ii) fails at count 2 for every `λb ≠ 0`.**
   - Put `α = cλb`. Then `Λ(d)/z = Σ_{y∉{0,d}} e^{α(G(y)+G(y−d))}`.
   - **First order, on every torus.** `∂_αΛ(d)/z` at `α = 0` equals `Σ_{y∉{0,d}}(G(y) + G(y−d)) = −2(G(0) + G(d))`, using `ΣG = 0` and `G` even. This differs between separations with different `G(d)`, so `Λ` is not constant for small `α ≠ 0`.
   - **All orders.** With `D` the common denominator of `G` and `q = e^{α/D}`, the difference `Λ(d) − Λ(d')` is a Laurent polynomial in `q` with integer exponents, vanishing at `q = 1`.
     - *Rings of 4 to 8 sites.* Exact real-root isolation: the only positive root common to all separations is `q = 1`.
     - *Tori `3³` and `4³`.* `G` is checked at every site. Two pairs of separations are used: on `3³`, `(0,0,1)–(1,1,1)` and `(0,1,1)–(1,1,1)`; on `4³`, `(0,0,1)–(1,2,2)` and `(0,1,2)–(1,2,2)`.
       - Each pair's coefficient sequence has exactly 2 sign changes.
       - By Laguerre's rule of signs, a real exponential sum `Σ c_j q^{β_j}` has at most as many positive zeros, counted with multiplicity, as sign changes, and the same parity. *Proof:* by induction with Rolle's theorem on `(q^{−β_k}f)'`; parity from the signs of the end terms.
       - `q = 1` is a simple zero, since its `α`-derivative is `−2(G(d) − G(d')) ≠ 0`. So each pair has exactly one further positive zero.
       - Exact rational bisection brackets these at `α ∈ [21.3588]` and `[7.0872]` on `3³`, and `[10.3119]` and `[3.2761]` on `4³`. The brackets are disjoint.
       - So at every `α ≠ 0` at least one of the two pairs differs.
     - (On `4³`, the pairs `(0,0,2)–(0,1,1)` and the like have identical rates: `C₄³` is the six-cube, whose symmetry identifies them.)

5. **PROVED: the only cases left.**
   - For `λ ≠ 0` with non-constant `G`, step 3 forces `b = 1 − 2a` and step 4 forces `b = 0`. So `a = 1/2` and `b = 0`.
   - There `π_n` is uniform and `Λ(C) = z(N_s − n)`, so (i) and (ii) hold.
   - For `λ = 0` all clocks are 1 and everything holds.
   - Checked on ring 7 (B1): with `a = 1/2`, `b = 0` the law entering each count is `π_n` exactly (TV 0).

6. **CHECKED (B1): the failure seen in the dynamics.** Ring 7, `e^{2λ/7} = 1/2`, `z = 1`, exact:
   - with `b = −1` (T4's half), the law entering count 2 is `π₂`, but the law entering count 3 is off by total variation `0.0247`;
   - with `b = 1`, the law entering count 2 is off by `0.6503`.

7. **PROVED + CHECKED (B1): filling order.**
   - Given the configuration, the next formation is at `y` with probability `w_y^b/Σ w^b`.
   - At one record, the rate at `y` depends only on `y − r`. So the second record's separation law is `∝ w(d)^b` whatever the first record's motion history and `z`.
   - On ring 7 that is `(1/2, 2, 4, 4, 2, 1/2)` for `d = 1..6`, so classes 1, 2, 3 get `1/13, 4/13, 8/13`.

8. **CHECKED (J1): time to fill.**
   - Exact, by the count-by-count linear systems on ring 7 (`2⁷` configurations).
   - The first two stages are free of `z`: `zE[T₁] = 1/7`, then `1/13`.
   - The quasi-static limit `Σ_n 1/⟨Λ⟩_{π_n}` and the no-motion limit (clock-weighted sequential filling) are computed exactly and bracket the grid.

9. **ASSUMED.**
   - Block 95's supplied clauses (clock law, timing, slaved field), with `W ≡ 1`.
   - The ring version is block 95's own one-dimensional check.
   - Nothing is adopted.

## 3. Where it stops

- **Tori.** On a general torus, (ii)'s failure is proved to first order in `λb` only. For all `λb`, it is certified on the rings of 4 to 8 sites and on `3³` and `4³`.
- **Weights `W ≢ 1`** (block 39's pair weights) are not treated. With a content-dependent `W`, (i) would compare the creation flux against `W(C)e^{…}`, which `w^b` alone cannot carry.
- **Monotonicity in `z`** of `zE[T_fill]` is shown along the grid only. The record count's full time law `E[N(t)]` is given through its mean passage times, not in closed form.

## 4. What would finish it

1. **(ii) for all `λb` on every torus.** For example, a convexity or rearrangement argument showing `Λ` is monotone in the pair's `G(d)` for each sign of `λb`.
2. **The version with block 39's weights `W`.**
3. **Scaling of the fill time with the volume, and whether it stays monotone in `z`.**

## 5. Running it

```
python3 probes/work/derive/formation-timed-by-the-clock/w-macbookpro9927a-jef4e/check.py
```

Four checks (Q, C1, B1, J1), all exact (fractions, sympy). It runs in about 3 seconds.
