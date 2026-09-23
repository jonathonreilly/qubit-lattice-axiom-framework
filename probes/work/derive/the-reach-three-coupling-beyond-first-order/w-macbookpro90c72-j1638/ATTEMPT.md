# J:derive:the-reach-three-coupling-beyond-first-order:a3 — worker w-macbookpro90c72-j1638

**Model:** claude-opus-5-5.

**Check:** `python3 probes/work/derive/the-reach-three-coupling-beyond-first-order/w-macbookpro90c72-j1638/check.py`
- About 5 s.
- The vector identities use exact Gaussian-rational arithmetic, via `gq.py` and `ops.py` next to it. R3 is symbolic. R4 is floating point.

**Provenance.**
- My plan was formed before I read attempt a1 (`w-jonathonsmac4f50-j5453`, same model family, another machine):
  - species-blindness from hop parity, for any bond field;
  - the dependence on the completion through the first variation of the sea's energy;
  - the exact momentum balance at finite strain.
- a1 found the first two, and it lists the third as not done: "the second-order terms of block 66's rate-dependent force density `fP` at finite strain are not derived".
- **What this attempt adds:**
  - that third part (S5, S6), with an exact check on 5³;
  - an exact reason why the relabelling's exponential cannot serve (S2);
  - independent confirmations of a1's first two parts (S1, S3, S4). a1's stiffness numbers (0.0004 → 0.0068) are a1's; I do not recompute them.
- **Overlap with my own units:**
  - #8716 (the sea's clock stiffness, block 76's `κ`);
  - the unit on couplings that are not a local relabelling's deformation, today; it covered block 69's coupling at first order.
  Nothing is reused beyond the definitions.
- Blocks 66–76, a1 and this attempt are all from the Claude family. This needs a referee of another family.
- Definitions come from the notes of blocks 66, 69, 70, 72 and 76 on their PR branches (#8597, #8601, #8602, #8605, #8611).

## 1. The statements attempted

**Objects.**
- The walk `H = Σ_a σ_a S_a` and the two-step momentum `P_l = S_lC_l`, where `(P_lψ)(x) = (ψ(x+2e_l) − ψ(x−2e_l))/(4i)`.
- `V[b] = Σ_{a,l} σ_a ½{C_a[b_a^l], P_l}` for a bond field `b`, and `H3[b] = H + V[b]` (block 69).
- The relabelling `G = ½Σ_j {ξ_j, P_j}`.
- The clocked walk `φH3[b]φ`.

**(a) Completions exist, so the task's HIT condition fails.**
- Every `H3[f(B)]`, with `f(B) = B + O(B²)` applied bond by bond, is hermitian, translation- and rotation-covariant, and species-blind exactly.
- The reason is the hop parity: each term is `σ_a` times a hop `m ≡ e_a` (mod 2).
- The linear `H3[B]` is one such completion.
- **The natural one, by analogy with `φHφ`**, is the log-strain completion `b = e^{−Λ} − 1`: the two-step momentum weighted by `e^{−Λ}`. A uniform strain then shows all eight species `e^{−Λᵀ}e^{−Λ}` exactly.
- **Exponentiating the relabelling is no alternative.** Its second-order term depends on `ξ`, not only on `dξ`.

**(b) Where the completion enters the sea.**
- It enters `E_sea''` only through `2 tr(P_sea V[b₂])`.
- For completions local to each bond this is a shift independent of `q`: `κ_aa = −0.10761` per bond on 8³.

**(c) The exact momentum balance at finite strain.** For every state, rate field `φ > 0`, displacement `ξ` and bond field `b`:

```
d⟨G⟩/dt = Σ_{a,j,x} (d_aξ_j) K_a^j[φψ] + ⟨T1 + T2⟩_{φψ} − Σ_{j,x} ξ_j (f^P_j[b] + f^B_j[b]).
```

- **The strain flux** `T1 + T2` pairs with differences of `ξ`.
- **A new force from strain gradients**, `f^B`, comes from `i[C_a[b], P_j]`, i.e. from two-step differences of `b`.
- `f^P_j[b]` is block 72's rate force with `H3[b]` in place of `H`.
- **Consequences.**
  - On stationary states, the divergence of the total flux equals `−(f^P + f^B)` site by site.
  - Block 72's leading-order requirement is unchanged.
  - The completion first enters at second order in `B`, through `b = f(B)` in all three terms.

## 2. Steps

**S1. Species-blindness of every completion. PROVED; R1 exact.**
- Block 70's maps are `V_n = R_nU_n`, with `U_n = (−1)^{n·x}` and `R_n` the coin's half turn for `ρ_n = s_nD_n`.
- **The sign of a term.** A term `σ_a · w(y)|y+m⟩⟨y|` (any position-dependent weight `w`) picks up `(−1)^{n·m}` from `U_n` and `ρ_{n,aa} = s_nD_a` from `R_n`. For the term to pick up `s_n` we need `(−1)^{n·m} = D_a` for all `n`, i.e. `m ≡ e_a` (mod 2).
- **The parities in `V[b]`.** `C_a[·]` moves one step along `a`, and `P_l` zero or two steps along `l`. So every term of `V[b]` has parity `e_a`, and so does `H`.
- **Conclusion.** `V_n H3[b] V_n⁻¹ = s_n H3[b]` for every bond field `b`: for `H3[B]`, for any `H3[f(B)]`, and for any placement of the weights.
- **Other properties.** Hermiticity holds because `C_a[·]` and `P_l` are hermitian for real weights. Covariance holds by construction.
- R1 checks the relation exactly on 6³ for random rational `b`, all seven `n`.

**S2. The relabelling's exponential is not a strain coupling. PROVED; R2 exact.**
- `[P_j, H] = 0` gives `[G + cP, [G + cP, H]] = [G, [G, H]] + c[[P, G], H]`.
- R2 finds `[[P_j, G], H] ≠ 0` for a random rational `ξ`. So the second-order term of `e^{iG}He^{−iG}` changes under `ξ → ξ + c`: it is not a function of the strain `dξ`.
- This is the reason a completion must be supplied.

**S3. The log-strain completion. PROVED; R3 exact.**
- Block 69 T4's computation, `s_a + c_a(Bq)_a = D_a[(1 + B)q]_a`, is exact in `B` for a uniform strain.
- So `b = e^{−Λ} − 1` gives every species `(1 + b)ᵀ(1 + b) = e^{−Λᵀ}e^{−Λ}` exactly. R3 checks this symbolically to second order in `Λ`, for all eight `n`.
- It is "the two-step momentum weighted by `e^{−Λ}`", the analogue of `φHφ`'s `√(w_xw_y)`.

**S4. The completion in the sea. PROVED; R4 floating point.**
- **The formula.** For `H(ε) = H + εV[b₁] + ε²V[b₂]`, first-order perturbation of the negative eigenvalues gives `E_sea''(0) = 2 tr(P_sea V[b₂]) + (terms in b₁ only)`. The zero modes of even tori contribute nothing at this order.
- **Bond-local completions.** For `b₂ = c b₁²` and a mode `b₁ = b cos(q·x)`, `tr(P_sea V[b₂])` sees only the uniform part `b²/2`. The shift is then independent of `q`: it changes the local part of the stiffness, not its gradient part.
- **The coefficient.** Per unit uniform strain, `κ_aa = −(1/N) Σ_k sin²k_a cos²k_a/|s(k)|`. That is `−0.10761` on 8³ and `−0.10881` on 16³; the off-diagonal part vanishes.
- This agrees with a1's −0.10761, computed here independently.
- A completion that mixes sites changes the gradient part; a1 computes that case.

**S5. The finite-strain law in operator form. PROVED; R5 exact.**
1. **The rate hop.** `i[φ, P_j] = −½C2_j[d2_jφ]` (block 72 T1(a)).
2. **The bare relabelling.** `i[H, G] = V[dξ]` (block 69 T3(a)).
3. **The strain term, by the Leibniz rule** `[{A,P}, Z] = {A, [P,Z]} + {[A,Z], P}` and `[P_l, P_j] = 0`: `i[V[b], G] = Σ_{a,l,j} σ_a (T1 + T2 + T3)`, where
   - `T1 = ¼{C_a[b_a^l], {½C2_l[d2_lξ_j], P_j}}`, using `i[P_l, ξ_j] = ½C2_l[d2_lξ_j]`;
   - `T2 = ¼{{−S_a[b_a^l d_aξ_j], P_j}, P_l}`, using `i[C_a[β], ξ] = −S_a[β d_aξ]` with `S_a[w]` the antisymmetric weighted hop;
   - `T3 = ¼{{ξ_j, i[C_a[b_a^l], P_j]}, P_l}`.
4. **The clocked law.** `i[φXφ, G] = φ(i[X, G])φ − (ΛXφ + φXΛ)`, with `Λ = Σ_j ½{ξ_j, ½C2_j[d2_jφ]}` and `X = H3[b]`.
- All four are checked as exact vector identities on 5³, with random rational `φ > 0`, `ξ`, `b`, `ψ`.

**S6. The momentum balance. PROVED; R6 exact.** Take expectations in `ψ` and write `χ = φψ`.
- `⟨φV[dξ]φ⟩ = Σ(d_aξ_j) K_a^j[χ]` (block 69 T3(c)).
- `⟨φ(T1 + T2)φ⟩ = ⟨T1 + T2⟩_χ`. This is linear in the differences `d_aξ` and `d2_lξ`: the strain's correction to the momentum flux.
- `⟨φT3φ⟩ = −Σ ξ_j f^B_j[b]`, with
  `f^B_j(x) = −Σ_{a,l} ¼ · 2Re[χ†(σ_aX_{alj}P_lχ) + (σ_aX_{alj}χ)†(P_lχ)](x)` and `X_{alj} = i[C_a[b_a^l], P_j]`,
  which involves only `b(x ± 2e_j) − b(x)` (from `[b, P_j]`).
- `⟨ΛH3φ + φH3Λ⟩ = Σ ξ_j f^P_j[b]`, with `f^P_j[b](x) = Re[(Q_jψ)†(H3[b]χ) + ψ†(Q_jH3[b]χ)](x)` and `Q_j = ½C2_j[d2_jφ]`.
- **The total.** R6 checks the resulting identity exactly (value 39431/36864 on the sample).
- **Uniform `ξ`.** The flux terms vanish, and the total two-step momentum changes at minus the total force, rates plus strain gradients.
- **Stationary states.** `d⟨G⟩/dt = 0` gives the site-by-site law `div(K + strain flux) = −(f^P + f^B)`.

**S7. Leading-order reading (the same approximation as block 72 T3).**
- For smooth `b`, `i[C_a[b], P_j] ≈ −(∂_jb) C_aC2_j`. So `f^B_j ≈ Σ_{a,l} (∂_j b_a^l) · 𝔗_a^l`, where `𝔗_a^l = ⟨σ_a C_a C2_j P_l⟩` per site is the stress that couples to `b`: stress times strain gradient.
- Near every zero `C_a → D_a` and `C2_j P_l → q_l`, so `σ_a D_a q_l` has the same sign for all eight species. The strain force is species-blind at leading order, as the coupling is.
- This reading is not checked in `check.py`. It is marked here as the leading-order statement.

**S8. Block 72's requirement and the completion.**
- Block 72's leading-order requirement is evaluated at `b = 0`, and every completion has `f(B) = B + O(B²)`. So neither it nor the first-order terms in `B` of S6 depend on the completion.
- The completion first appears at second order in `B`, through `b = f(B)` in `T1 + T2`, in `f^B` and in `f^P[b]`.
- **Block 66's exact law.** Its force density at finite strain is `f^P[b] + f^B[b]`, with the extra flux. The "second-order terms" the task asks for:
  - `Δf^P_j = Re[(Q_jψ)†(V[b]χ) + ψ†(Q_jV[b]χ)]`: the rate gradient times the strain;
  - `f^B`: the strain gradient;
  - `⟨T1 + T2⟩`: the strain flux.
  - For `b = f(B)` the completion's `f₂(B)` enters each of these linearly.

**ASSUMED:** nothing beyond block 69 T3 and block 72 T1(a), which are restated and re-checked here, and first-order perturbation theory for eigenvalues (S4).

## 3. Where it stops

- The task's HIT condition (no completion exists) is refuted by S1, so no HIT line is printed.
- **Not done here:**
  - the full recomputation of block 76's stiffnesses for a completion that mixes sites (a1 has it);
  - a check of S7's leading-order reading against a packet;
  - a choice among completions. The framework supplies none. S2 shows that the relabelling's exponential cannot decide it, and S4 shows that bond-local completions leave the gradient stiffness unchanged.

## 4. What would finish it

1. **A principle that selects the completion.** For example, the ledger's exact force identity at second order: does some `f₂` make `f^P + f^B` equal the energy density times `d log w` plus the strain force of a field energy that is blind to relabellings? The terms of S6 are what that question needs.
2. **The strain force against a packet,** at leading order (S7).
3. **A referee of another model family** for S5 and S6.
