# deferred-20260924-ledger, first pass: which placements of the walk's momentum current can source block 62's symmetric member

Worker `w-macbookpro9927a-j2f0e` (`claude-opus-5-5`), unit `J-derive-deferred-20260924-ledger-a1`.

- origin/main `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`.
- Landing snapshot `c288aa9cfe`; batch 7 landed in `c3f8c47a58`.
- Status file: [`RECOVERY_STATUS.json`](RECOVERY_STATUS.json). It lists 15 deferred sources, each with its SHA256 re-verified from its frozen head.

**Provenance and independence.**
- **The bundle.** Batch 7 (`probes/work/deferred-science-20260924/batch-07.json`) carries two review findings that apply here:
  - U7-R5 (PR8593, PR8595, PR8596, PR8597): "defer q-only numerical no-go".
  - U7-R4 (PR8590–PR8592): "missing site-to-face transfer explicit".
- **What I read first.** The landed notes of blocks 62, 63, 64 and 65 on origin/main, then the deferred sources of PR8592, PR8593, PR8595 and PR8596:
  - CHECKER and RESULTS for each;
  - the refuter outputs of blocks 62 to 65;
  - block 63's certificate.
- **My plan, formed before reading related attempts.** Both deferred items are one question. Any local transfer, and any q-only divergence symbol, acts on the walker's bilinears at wave vector `q` through a matrix that depends on `q` only. So both items ask whether the stationary states' `q`-parts span enough to force that matrix to vanish.
- **Related attempts inspected.**
  - `a-bond-placed-stress-for-the-walk` a3 (`w-jonathonsmac4f50-j1518`, `claude-opus-5-5`, issue #8636, not yet refereed). It is from the same model family as me. It supplied the site convention for block 62's member and the realisation formalism (`B = Rh`, `ΛR = 1`). Its open item 1 ("Not shown: that every realisation `R` fails") is Theorem C below. This attempt is not a referee of a3.
  - `the-ledgers-force-identity-exactly-on-the-lattice`: a1 is an earlier session on this machine (#8874, confirm #8910), a2 is #8879 (confirm #9017). It concerns the ledger's force identity; no member compatibility is involved.
  - `a-ledger-that-reads-bond-energies`: no delivered attempt on ai/probes.
  - Block 73 (two-step momentum; landed) supplies `P_j` and its current `K`.
- **What is mine.** The reflection states, the spanning lemma, Theorems B, C and D (the transposed law and the φ-realisation), and the exact version of block 63's W3.

## 1. What is attempted

**Setting.** Everything below comes from the landed notes. Nothing is adopted.

- **The walk.**
  - `(T_aψ)(x) = ψ(x + e_a)`, `S_a = (T_a − T_a^{−1})/(2i)`, `C_a = (T_a + T_a^{−1})/2`.
  - `P_j = S_jC_j`, with symbol `½ sin 2k_j` (block 73).
  - `H = Σ_a σ_aS_a`, in the identity frame with uniform rates.
- **Responses.**
  - The site response is `Θ_a^j(x) = Re ψ†(x)σ_a(S_jψ)(x)`. It is the response of block 62's site-placed frame coupling `H_E = ½Σ_j{E^j(x)·σ, S_j}`, `E = 1 + ε`, to `ε_a^j(x)`.
  - The bond currents live on the bond `x → x + e_a`:
    - `J_a^j = ½Re[ψ†(x+e_a)σ_a(S_jψ)(x) + (S_jψ)†(x+e_a)σ_aψ(x)]` (block 63);
    - `K_a^j`, the same with `P_j` in place of `S_j` (block 73).
  - They are the responses of block 64's coupling `H[B] = H + Σσ_a½{C_a[B_a^j], S_j}` and block 73's coupling `H⁽²⁾[B] = H + Σσ_a½{C_a[B_a^j], P_j}` to a nine-component bond strain `B_a^j(x)` (step 7).
- **The member.** Block 62's symmetric six-component member, in a3's site convention. It is a function `F(h)` of a symmetric field `h_ij(x)` with `F(h + Gξ) = F(h)` for the relabelling directions `(Gξ)_ij = −(d_iξ_j + d_jξ_i)`, where `d_af(x) = f(x+e_a) − f(x)`. The symbol is `G(q)ξ̂ = −(D⊗ξ̂ + ξ̂⊗D)`, with `D_a = e^{iq_a} − 1`. Translating `h_ij` by `(e_i+e_j)/2` gives block 62's staggered member with `i(p_iη_j + p_jη_i)`, `p = 2 sin(q/2)` (a3 C1; the phase identity is re-checked in D1).
- **Transfer and realisation.**
  - A *local transfer* or *realisation* is a real, translation-invariant, finite-range linear map from the member's field to the walker's field:
    - the frame strain `ε = Ph` for `H_E`;
    - the bond strain `B = Rh` for `H[B]` or `H⁽²⁾[B]`.
  - Its symbol is a trigonometric polynomial (half-angles allowed for staggered places), so it is continuous at `q = 0`.
  - *Normalisation*: the walker sees the member's uniform field. That means `sym P(0)h = −½h`, so that `h = −(ε + εᵀ)` as in block 62, and `ΛR(0) = 1` with `Λ(B)_ij = −(B_i^j + B_j^i)` (a3).
- **Compatibility.**
  - The condition is `⟨Θ, PGξ⟩ = 0`, `⟨J, RGξ⟩ = 0` or `⟨K, RGξ⟩ = 0` for every finitely supported real `ξ`, where `⟨X, W⟩ = Σ_xΣ_{a,j}X_a^j(x)W_a^j(x)`.
  - It is necessary for the member's static equation `∂F/∂h = −PᵀΘ` (resp. `−RᵀJ`, `−RᵀK`) at first order in the strain, because `F(h + Gξ) = F(h)` gives `⟨∂F/∂h, Gξ⟩ = 0`. Block 64 T1(d) makes the same point.
- **Stationary states.** On `L³` tori these are the eigenvectors of `H`. On `Z³` they are finite superpositions of plane waves of one energy (bounded), paired with finitely supported `ξ`.

**Theorem A (reflection states; spanning).**
- *The states.*
  - Take `θ` with `cos θ ≠ 0 ≠ sin θ` and any `k_2, k_3`.
  - Put `s = (cos θ, sin k_2, sin k_3)` and `E = ±|s|`, and take `χ` with `(s·σ)χ = Eχ`.
  - Let `k = (π/2+θ, k_2, k_3)` and `k' = (π/2−θ, k_2, k_3)`.
- *The responses.* `ψ = χ(e^{ik·x} + e^{ik'·x})` satisfies `Hψ = Eψ`. With `ρ = |ψ|² = |χ|²(2 + 2cos 2θx_1)`:
  - `Θ_a^j = s_as_jρ/E`;
  - `J_1^j = 0`;
  - `J_a^j = s_as_j cos k_a ρ/E` for `a = 2, 3`.
- *Their parts at `q = (2θ,0,0)`.* `Θ̂(q) = |χ|²s⊗s/E` and `Ĵ(q) = |χ|²v⊗s/E`, with `v = (0, s_2 cos k_2, s_3 cos k_3)`.
- *Spanning.* As `(k_2,k_3)` vary:
  - the `Θ̂(q)` span `Sym(3)`;
  - the `Ĵ(q)` span `{v_1 = 0}⊗C³ = U(q)⊗C³`, where `U(q) = {v : Σ_a v_a conj(D_a) = 0}`. This is the whole space in which conserved currents at `q` live.
- *On tori.* The same holds on `L³` tori with `4 | L`, `L ≥ 8`, at `θ = 2πm/L`. The same statements hold for the axes `e_2`, `e_3`.

**Theorem B (the site response).**
- (a) *Exact W3.* No nonzero complex `f` has `Σ_af_aΘ̂_a^j(q) = 0` for every equal-energy pair with difference `q`:
  - at every axis `q`, with rational witnesses at `cos θ = 4/5`;
  - at the generic rational `q` whose half-angle sines are `3/5, 5/13, 8/17`.
- (b) *No transfer.* No local transfer `P` with `sym P(0) = −½` keeps block 62's member compatible on every stationary state of `Z³`. On the `L³` tori with `4 | L`, compatibility can hold only for finitely many `L`.
  - Compatibility on the reflection states at an axis `q` forces `sym(P(q)G(q)ξ̂) = 0` for all `ξ̂`.
  - As `q → 0` it then forces `sym P(0) = 0` on `Sym(3)`: the frame would be blind to every uniform strain of the member.

**Theorem C (the bond current of `S_j`).** No local realisation `R` with `ΛR(0) = 1` keeps the member compatible with block 64's coupling on every stationary state.
- Compatibility at `q = te_c` forces `R(q)G(q)ξ̂ ∈ e_c⊗C³`.
- As `q → 0`, `R(0)` must then annihilate every uniform shear `e_c⊗e_d + e_d⊗e_c` (`c ≠ d`).

**Theorem D (the two-step current).**
- (a) *A transposed law.* On every stationary state, for every site `x` and every `a`:
  `Σ_j Π_{l≠j}C_l[K_a^j(x+e_j) − K_a^j(x−e_j)] = 0`.
- (b) *A compatible realisation.* Take `B_i^j = −½(φ_jh_ij)`, with `φ_j = ½(1 + T_j^{−1})Π_{l≠j}C_l`.
  - `φ_j = 1` on uniform fields.
  - The walker's symmetric strain is `h_ij(φ_i + φ_j)/2`, so `ΛR(0) = 1`.
  - This realisation keeps block 62's member *exactly* compatible with block 73's coupling on every stationary state, torus or `Z³`.
- (c) *Solvability.* Block 62 T5 says the member's static null space at every nonzero symbol momentum is exactly the relabelling directions. So the member's static equation with this source is solvable at every nonzero wave vector. The uniform (`q = 0`) part of the source remains a separate global condition: on a closed lattice it is "not balanced by any curl" (block 64).

**E (boundary).** At an axis `q`, restricted to the species-0 component (pairs with `k̄_1 = 0`):
- block 62's symbol `p` is exact;
- the plain transfer `ε = −h/2` and the plain realisation `B = −h/2` both pass.

B and C therefore rest on mid-zone stationary states (`k_1` near `π/2`).

**In plain terms.** Neither the site-placed frame response nor the canonical bond current of the walk's momentum `S_j` can source block 62's symmetric member: every local way of placing them fails on some stationary state. The two-step momentum `P_j`, which is every species' own wave number, can. Its flux obeys a second, transposed conservation law. A local averaging of the member's field onto the bonds then makes the member's static equations solvable at every nonzero wave vector, whatever the stationary source.

## 2. The steps

1. **PROVED + CHECKED (A1): the reflection states.**
   - `sin(π/2 ± θ) = cos θ`, so `s(k) = s(k')` and `H(k) = H(k')`. So `ψ` is an eigenvector, and `S_jψ = s_jψ`.
   - Hence `Θ_a^j = s_jRe ψ†σ_aψ = s_j(s_a/E)ρ`, using `χ†σχ = (s/E)|χ|²`.
   - Likewise `J_a^j = s_j(s_a/E)|χ|²Re[c̄(x+e_a)c(x)]`, with `c = e^{ik·x} + e^{ik'·x}`:
     - for `a = 2, 3`, `c(x+e_a) = e^{ik_a}c(x)`;
     - for `a = 1`, `e^{ik_1} = ie^{iθ}` and `e^{ik'_1} = ie^{−iθ}` give `c̄(x+e_1)c(x) = −i[2cos θ + 2cos(2θx_1+θ)]`, which is purely imaginary.
   - Checked exactly at all 125 sites of `[−2,2]³` for three states with rational data (`s = (4/5,3/5,0), (4/5,0,3/5), (4/5,0,0)`), for all nine `(a,j)`:
     - `Hψ = Eψ`;
     - the formulas for `Θ` and `J`;
     - `div J = 0`;
     - `div sym J ≠ 0`.

2. **PROVED + CHECKED (A2): spanning.**
   - The `e^{iq·x}` coefficient of `ρ` is `|χ|²`, which gives the stated `q`-parts. The scalar `|χ|²/E ≠ 0` does not change spans.
   - Six rational samples `(k_2,k_3)` give 6×6 determinants in `c = cos θ`:
     - `(298980605952/165695302703125)c²` for the `J`-parts, in the basis `{e_2,e_3}⊗{e_1,e_2,e_3}`;
     - `(−2778946464/75418890625)c⁴` for the `Θ`-parts, in `Sym(3)`.
     - Both are nonzero for every `c ≠ 0`.
   - At `q = (2θ,0,0)`, `U(q) = {v_1 = 0}` because `D_1 = e^{2iθ} − 1 ≠ 0`.
   - *Tori.* `k_1 = π/2 ± θ` lies on the grid when `4 | L` and `θ ∈ 2πZ/L`.
     - The six `J`-functions `c_as_a·(c, s_2, s_3)` (`a = 2,3`) are trigonometric polynomials in `(k_2,k_3)` of degree `≤ 3` with pairwise distinct frequency sets. They are therefore independent on any grid with `L ≥ 7`.
     - The `Θ`-functions have degree `≤ 2`.

3. **PROVED: the Fourier form of compatibility for a two-wave state.**
   - Let `X(x) = X̂_0 + X̂(q)e^{iq·x} + c.c.` and let `W` be real and finitely supported. Then `Σ_xX·W = X̂_0·Ŵ(0) + 2Re[X̂(q)·conj Ŵ(q)]`, with `Ŵ(q) = Σ_xW(x)e^{−iq·x}`.
   - For `W = PGξ` (or `RGξ`), `Ŵ(q) = P(q)G(q)ξ̂(q)` and `G(0) = 0`.
   - `ξ̂(q)` ranges over `C³`: `ξ = vδ_0` gives real `v`, and `ξ = vδ_{e_1}` gives `e^{−2iθ}v` with `e^{−2iθ} ∉ R`.
   - So compatibility on the state is `⟨X̂(q), P(q)G(q)w⟩ = 0` for all `w ∈ C³` (Hermitian pairing).
   - Conservation, `Σ_x J·Dξ = 0` for all `ξ`, reads `Ĵ(q) ∈ U(q)⊗C³`, whose orthogonal complement is `D(q)⊗C³`.

4. **PROVED + CHECKED (B3): Theorem B(b).**
   - By steps 2 and 3, `⟨S, P(q)G(q)w⟩ = 0` for every `S` in the complex span `Sym(3)`. So `sym(P(q)G(q)w) = 0`.
   - `G(te_c)w/t → −i(e_c⊗w + w⊗e_c)` and `P` is continuous. So `sym P(0)(e_c⊗w + w⊗e_c) = 0` for `c = 1,2,3` and every `w`.
   - These matrices span `Sym(3)`, so `sym P(0) = 0`. This contradicts `sym P(0) = −½`.
   - On tori: if compatibility held for infinitely many `L` with `4 | L`, the same argument would run along `q_L = (4π/L)e_c`.
   - Witness: the plain transfer `ε = −h/2`, on the state with `s = (4/5,3/5,0)` and `ξ_1 = δ_0`, gives pairing `−1152/625`.

5. **CHECKED (B1, B2): Theorem B(a), block 63's W3 made exact.**
   - *Axis `q`.* `Θ̂^j_a ∝ s_js_a`. For each `j`, three rational reflection pairs with `s_j ≠ 0` have independent `s` (determinants `36/125, −16/125, 16/125`). These are "two equal-energy pairs with rational data and a common `q`", the object N1.5 of the frozen block 63 asked for (three pairs here).
   - *Generic `q`.* For a pair with `|s| = |s'| = E`, `f·M = 0` holds iff `(E + s'·σ)(f·σ)(E + s·σ) = 0`.
     - Imposing it for both bands (both are equal-energy pairs) gives `X = Y = 0`, where `X = E²(f·σ) + (s'·σ)(f·σ)(s·σ)` and `Y = (s'·σ)(f·σ) + (f·σ)(s·σ)`. This is linear in `f`, with rational coefficients.
     - Over the seven per-component pairs (`k̄_a ∈ {0, π/2}`) with `s + s' ≠ 0`, the system has rank 3.
     - The all-negation pair (`k̄ = 0`) has no site response. It alone accepts `p = 2 sin(q/2)`: block 62's symbol is exact at the species point.

6. **PROVED + CHECKED (C1): Theorem C.**
   - By steps 2 and 3, `R(q)G(q)w ∈ (U(q)⊗C³)^⊥ = D(q)⊗C³ = e_c⊗C³` at `q = te_c`.
   - As `t → 0`, `R(0)(e_c⊗w + w⊗e_c) ∈ e_c⊗C³`.
   - For `c ≠ d`, `R(0)(e_c⊗e_d + e_d⊗e_c) ∈ e_c⊗C³ ∩ e_d⊗C³ = {0}`. But `ΛR(0)(e_c⊗e_d + e_d⊗e_c) = e_c⊗e_d + e_d⊗e_c`.
   - Witness: on the state with `s = (4/5,3/5,0)` and `ξ_2 = δ_0`:
     - `Σ J·(dξ) = 0` (conservation);
     - the realisation `B = −h/2` gives pairing `−1728/3125`, which is a3's transposed divergence;
     - D's φ-realisation also fails for `J`.

7. **PROVED + CHECKED (D0): the responses.**
   - For every state and every bond field `v`, `⟨ψ|σ_a½{C_a[v], M_j}|ψ⟩ = Σ_xv(x)·(current)_a^j(x)`, for `M = S` (current `J`) and `M = P` (current `K`).
   - Proof: `C_a[v]` hops one step along `a`, weighted by `v` on the bond. `M_j` is hermitian and commutes with the shifts. Re-index the backward hop, as in block 63 T2(b) and block 64 T1(b).
   - Checked exactly for random integer `v` on `[−1,1]³`, all `(a,j)`, both `M`.

8. **PROVED + CHECKED (D1, D2): the transposed law.**
   - For `ψ = Σ_kχ_ke^{ik·x}` of energy `E`, expanding the definition gives `K_a^j(x) = Σ_{k,k'}½(P_j(k)+P_j(k'))A_aM_ae^{i(k−k')·x}`, with `A_a = (e^{ik_a}+e^{−ik'_a})/2` and `M_a = χ_{k'}†σ_aχ_k`. (The two terms of `Re` pair `(k,k')` with `(k',k)`.)
   - `Σ_jΠ_{l≠j}C_l(T_j − T_j^{−1})`, acting on `e^{iq·x}`, multiplies by `2iΣ_j sin q_jΠ_{l≠j}cos q_l`.
   - `P_j(k)+P_j(k') = sin(k_j+k'_j)cos q_j`, so `sin q_j(P_j(k)+P_j(k')) = cos q_j(sin²k_j − sin²k'_j)`.
   - Each `(k,k')` term therefore acquires `Π_lcos q_l·(|s(k)|² − |s(k')|²) = Π_lcos q_l·(E² − E²) = 0`.
   - For `J` the analogue fails: `sin k_j + sin k'_j` carries `cos k̄_j`, which no `q`-only weight removes.
   - Checked:
     - the one-variable identity, symbolically;
     - the law at all 27 sites × 3 `a` of an exact energy-1 superposition of five plane waves with rational sines;
     - `div K = 0` there;
     - the same combination of `J` is nonzero at 81 of 81.

9. **PROVED + CHECKED (D3): the φ-realisation is compatible.**
   - For `h = Gξ`, `B = −½φh` gives `W_i^j = ½φ_j(d_iξ_j + d_jξ_i)`.
   - The first half of `⟨K, W⟩` is `½Σ_j⟨K^{·j}, d(φ_jξ_j)⟩`, which is 0 by conservation (`φ_j` commutes with `d_i`, and `φ_jξ_j` is finitely supported).
   - For the second half: `φ_jd_j = ½(1+T_j^{−1})(T_j−1)Π_{l≠j}C_l = ½(T_j − T_j^{−1})Π_{l≠j}C_l`. Its transpose is its negative. So the second half is `−¼Σ_iΣ_xξ_i(x)Σ_jΠ_{l≠j}C_l[K_i^j(x+e_j) − K_i^j(x−e_j)] = 0` by step 8.
   - Checked exactly:
     - zero for three random integer `ξ` on `[−1,1]³` on the superposition, and one each on the three reflection states and the species-0 pair;
     - the plain realisation `B = −h/2` gives nonzero pairings.

10. **PROVED (given block 62 T5) + CHECKED (D4): solvability away from `q = 0`.**
    - At `q ≠ 0` the member's static equation reads `M(q)ĥ = −R(q)†K̂(q)`, plus relabelling-invariant terms such as `uR_1`, whose `h`-gradients are orthogonal to the relabelling directions. It is solvable iff the right side is orthogonal to `ker M(q)`.
    - For `p(q) ≠ 0`, `ker M(q)` is exactly the relabelling directions (block 62 T5). D4 re-checks this in block 62's staggered form at `p = (1,0,0), (1,2,2), (2/5,1/3,−3/7)`: rank 3, with kernel spanned by `p⊗η + η⊗p`.
    - At `q = 0` the member's form vanishes, so the uniform part of the source must vanish separately. That condition is not addressed here.

11. **CHECKED (B3): boundary E.**
    - On the species-0 axis pair `k = (θ, k_2, 0)`, `k' = (−θ, k_2, 0)` (with `Hψ = ψ`), both the plain transfer (`Θ`) and the plain realisation (`J`) pair to 0 for three random `ξ`.
    - Reason: `M_1 = 0`, and the currents sit in the `{2,3}²` block, which the axis relabellings do not reach.

12. **ASSUMED.**
    - The supplied clauses of blocks 54, 62, 63, 64 and 73 as landed.
    - First order in the strain, identity frame, uniform rates.
    - Block 62 T5's three-dimensional static null space at every nonzero symbol momentum; it is re-checked at three `p` only.
    - Nothing is adopted. No physical selection between `S_j` and `P_j` is made.

## 3. Where it stops

- **The first failing step of the near-species strengthening is step 2.**
  - The spanning uses reflection states at axis `q`, with `k_1` near `π/2`.
  - At axis `q`, the species-0 component (`k̄_1 = 0`) gives only currents in the `{2,3}²` block. There the plain transfer and realisation are compatible (step 11).
  - A version of B or C in which compatibility is demanded only near one species point needs non-axis `q` and two-parameter on-shell families. Those carry algebraic, not rational, data.
  - The rational symmetric family `q = (2θ,2θ,0)`, `k̄ = (α,−α,β)` is degenerate. A floating scan, not claimed and not in the check, gives ranks: `M` 2, `J` 4, `sym Θ` 3.
  - Floating scans at generic small `q` near species 0 show full spans (`J` 6, `Θ` 9), which suggests the no-gos persist there. This is not certified.
- **Strict normalisation for the two-step current is open.**
  - The φ-realisation has `ΛR(q)h = h_ij(φ_i+φ_j)/2`, which is not `h` at `q ≠ 0`.
  - A realisation with `ΛR = 1` at every `q` would need a rotation part fixed non-locally by the relabelling, provided the two-step currents span `U(q)⊗(tan q)^⊥` at generic `q`. The floating rank is 4, which equals that dimension, but this is not certified.
- **Scope.**
  - First order in the strain, statics, identity frame, uniform rates.
  - The uniform part of the source and the member's dynamics are not examined.

## 4. What would finish it

1. **A near-species certificate.** For example, the jet of the `J`- and `Θ`-parts at `k̄ = 0` along the on-shell surface, in `Q(i)(E_0)` with `E_0 = |sin(q/2)|`, at a small non-axis rational `q`, together with analyticity in `q`. This would extend B and C to compatibility demanded only near one species.
2. **The exact span of the two-step currents at generic `q`.** This decides whether a local realisation with `ΛR ≡ 1` exists.
3. **Beyond statics.** Whether the φ-realised two-step source drives block 62's two transverse modes consistently, and what happens at nonzero rates (`√w H √w`).
4. **The uniform part of the source on closed lattices.**
5. **The owner's call** on which momentum, `S_j` or `P_j`, the ledger's source uses.
6. **A referee from another model family.** Especially for steps 3, 4 and 6 (the limit arguments) and steps 8 and 9 (the transposed law and the realisation).

## 5. Running it

```
python3 probes/work/derive/deferred-20260924-ledger/w-macbookpro9927a-j2f0e/check.py
```

- It has 12 exact checks (families Q, A, B, C, D), using Gaussian rationals, `fractions` and `sympy`. There are no floats.
- It runs in about 5 seconds.
- Family Q re-verifies:
  - the quotes from origin/main and the frozen head;
  - review findings U7-R5 and U7-R4;
  - the SHA256 of all 15 sources listed in `RECOVERY_STATUS.json`.
