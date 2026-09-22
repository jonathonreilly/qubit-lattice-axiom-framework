# the-fall-from-the-ledgers-consistency, attempt 2 of 2: on the lattice a ledger of curls forbids the fall; the walk falls with weight × cos k

Worker `w-jonathonsmac4f50-j5024` (`claude-opus-5-5`), unit `J-derive-the-fall-from-the-ledgers-consistency:a2`.

**Provenance.**
- Attempt a1 left nothing on `ai/probes`.
- I read blocks 62–65 (PRs #8592–#8596) for an earlier unit in this session, and made my plan for (a)–(c) before reading
  anything further. The plan: the commutator `[S_j, √wH√w]`, and the field's relabelling identity with the rates carried along.
- Then I read three later blocks of the same campaign, all by my model family, unrefereed, and not named in the task:
  - block 66 (PR #8597): the exact lattice content law (T3), the continuum field identity (T1), and the leading-order agreement
    (T4);
  - block 72 (PR #8605): which of the walk's eight species fall;
  - block 68 (PR #8599): the species.
- This attempt re-checks block 66 T3 exactly for every state (not only stationary). It adds three exact lattice statements that
  block 66 lists as not claimed. The main import from block 66 is its continuum identity T1, used only as the comparator for (c).

## 1. What is claimed

**Setting.**
- `H_w = φHφ`, with `φ = √w`, `u = log w` and `H = Σ_a σ_a S_a`. The momentum density is `π_j = Re ψ†S_jψ`.
- `J_a^j[χ]` is block 63's bond current of a state `χ`, and `C_j[v]` the symmetric hop along `j` weighted by `v`.
- `e_x = Re ψ†(x)(H_wψ)(x)`.
- The ledger is `F = Σ_x w_x D_x`, with `D_x` a function of the plaquette curls `F_ab^j = d_aB_b^j − d_bB_a^j` at `x` (blocks 60 and
  64).

> **(a) Momentum balance (exact, every state; block 66 T3 re-derived).**
> `∂_t π_j + Σ_a back_a J_a^j[φψ] = −f_j`, with `f_j = Re[(C_j[d_jφ]ψ)† Hφψ + ψ† C_j[d_jφ] Hφψ]`. Behind it lies
> `i[φ, S_j] = −C_j[d_jφ]`.
>
> **At first order in the rate gradient**, for every plane wave `ψ = χe^{ik·x}` with `Hψ = Eψ`:
> `f_j(x) = e · ½(u(x+e_j) − u(x−e_j)) · cos k_j`, exactly. The force is the weight (energy × the centred difference of `u` at
> the site) times `cos k_j`:
> - full for a smooth amplitude;
> - zero at `k_j = π/2`;
> - reversed for a species reflected along `j` (`cos k_j = −1`, block 72).
>
> **(b) The field's side on the lattice.**
> - For `F = Σ_x w_x D_x(curls)`, the identity `Σ_a back_a ∂F/∂B_a^j = 0` holds exactly **for every rate field**. A relabelling of
>   the strains leaves the curls unchanged and does not move site rates, so nothing replaces "divergence-free".
> - With the strains' equations `J[φψ] = −∂F/∂B`, the static system demands `div J[φψ] = 0`. By (a) that is `f = 0`. **This ledger
>   has no static solution for a content that feels a force: on the lattice it forbids the fall.**
> - More generally, take any ledger whose identity sees the content through `e` and `J`, with coefficients independent of the
>   content. At first order in the gradient, no such ledger reproduces the factor `cos k_j` (an exact linear system with no
>   solution).
>
> **(c) The answer.**
> - The fall is owed by the ledger's consistency **only at leading order in the wave number**. There the continuum ledger of
>   block 66 T1/T2 requires `div J = e∇u`, and the walk gives `e (centred du) cos k_j = e (centred du)(1 + O(k²))`. The energy
>   density sits on the site, with the centred difference of `u` on the same site.
> - The relative mismatch is `cos k_j − 1`, and `−2` for reflected species.
> - At the lattice level the fall is an **independent clause** for the ledgers considered here: block 64's curls with site rates
>   forbid it, and no content-blind `(e, J)` ledger owes the walk's exact law.

## 2. The steps

1. **PROVED + CHECKED (A1).**
   - `(S_j(φψ))(x) = (φ(x+e_j)ψ(x+e_j) − φ(x−e_j)ψ(x−e_j))/(2i)`, so `i(φS_j − S_jφ)ψ = −C_j[d_jφ]ψ` by collecting the two
     shifts.
   - Then `i[H_w, G_ξ] = φ(i[H, G_ξ])φ − (ΛHφ + φHΛ)` with `Λ = ½Σ_j{ξ_j, C_j[d_jφ]}`.
   - Take expectations: the first term is `Σ(d_aξ_j) J_a^j[φψ]` (block 63 T2 applied to `φψ`), and the second is `−Σ ξ_j f_j`.
     Also `⟨G_ξ⟩ = Σ ξ_j π_j`. Summation by parts gives the local law.
   - Checked exactly at all 60 sites of a 3×4×5 torus, for random rational `φ` and a random Gaussian-integer (non-stationary)
     state, `j = 1, 2, 3`, together with the commutator.
2. **PROVED + CHECKED (A2): first order.**
   - For `φ = 1 + εφ₁`: `d_jφ = ε d_jφ₁` exactly, and `Hφψ = Eψ + εHφ₁ψ`. So `f_j = 2εE Re[ψ†C_j[d_jφ₁]ψ] + O(ε²)`.
   - For a plane wave, `(C_j[v]ψ)(x) = ½[v(x)e^{ik_j} + v(x−e_j)e^{−ik_j}]ψ(x)`. Hence
     `f_j = εE|χ|² cos k_j (φ₁(x+e_j) − φ₁(x−e_j))`.
   - With `e = E|χ|² + O(ε)` and `u = 2εφ₁ + O(ε²)`, this is the stated form.
   - Checked exactly for all 24 energy-1 plane waves of the 4³ torus (exact Gaussian-integer coins), in all three directions, with
     `cos k_j ∈ {1, 0, −1}` all occurring.
3. **PROVED + CHECKED (B1): the lattice identity.**
   - `F(B + Dξ) = F(B)` for every `ξ`, because the curls of `Dξ` vanish (block 64 T1) and the weights `w_x` do not move. So
     `⟨∂F/∂B, Dξ⟩ = 0`, and summation by parts gives `div ∂F/∂B = 0`.
   - On shell, `J[φψ] = −∂F/∂B`, so `div J[φψ] = 0`. Step 1 then requires `f = 0` at every site.
   - Checked exactly on the 3³ torus for random rational rates and strains, with `D = curl² + curl³/3`. The gradient is taken
     symbolically, and the divergence is zero at all 27 sites while the gradient is not zero.
4. **PROVED + CHECKED (B2): no content-blind `(e, J)` ledger.**
   - At first order a single plane wave has uniform `e = E|χ|²` and `J_a^i = cos k_a s_a s_i |χ|²/E`.
   - A field identity linear in `e` and `J`, with coefficients independent of the content, needs
     `E² cos k_j c_j = A_j E² + Σ_{a,i} B_jai cos k_a s_i s_a` for all `k`.
   - Over 127 wave vectors with rational sines and cosines (Pythagorean triples) the exact system has
     `rank M = 7 < rank [M | b] = 8`. So there is no solution.
   - Directly: `k = (k₁, 0, 0)` forces `B₁₁₁ = 1` and `A₁ = 0`. Then `k = (0, k₂, 0)` leaves `s₂² = B₁₂₂ cos k₂ s₂²` for all `k₂`,
     which is impossible.
5. **PROVED (C1): leading order.** `cos k_j = 1 − k_j²/2 + …`. For a smooth amplitude the walk's force is block 66 T2's
   requirement, with the placement of step 2.

## 3. Where this stops

- **The route (b) as posed fails on the lattice**, at its first step: a relabelling of block 64's strains does not carry the
  rates. The ledger's identity stays "divergence-free" and forbids the fall.
- Block 66's continuum identity T1 carries the rates through the member's full frame dependence and the transport terms. Those
  are not in block 64's lattice variables. A lattice member that transports the rates, so that the relabelling identity acquires
  a `U d u` term, is not constructed here.
- Step 4 covers identities linear in `e` and `J` with content-independent coefficients. A ledger that also sees other content
  quantities is not covered: bond energies, the coin torque of block 65, or block 72's reach-three current `K`.
- Block 72 T1 finds that the reach-three relabelling gives the right leading-order force for all eight species, with lattice
  factor `cos 2q`. The exact first-order form for reach three (the analog of step 2) is not done here.

## 4. What would finish it

1. A lattice member that is blind under the **combined** relabelling, of the strains and of the rates (the rates carried by a
   lattice transport). Then work out whether its identity reproduces step 2's force exactly, at first order in the gradient, for
   every `k`. Step 4 shows it must see more of the content than `e` and `J`.
2. The reach-three analog of step 2: the exact first-order force for `P_j = S_jC_j`, and whether it equals `e du` times a factor
   independent of `k`.
3. A referee from another model family, especially for step 3 (the claim that this ledger forbids the fall) and step 4.

## 5. Running it

```
python3 probes/work/derive/the-fall-from-the-ledgers-consistency/w-jonathonsmac4f50-j5024/check.py
```

- It has 5 exact checks, using Fractions, Gaussian rationals and sympy. There are no floats.
- It runs in about 40 seconds, most of it the symbolic gradient of the 3³ ledger.
- `gauss_lattice.py` beside it is the exact lattice machinery, copied from this session's `a-bond-placed-stress-for-the-walk`
  unit.
