lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# LW1-5-X: the frame bound at exceptional angles of the cube gate, both five-mode laws, pass 1

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini, as a pass-1 lane of the TOE assembly (item LW1-5-X of `LW1_5_DRAFT.md` section 11). Method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation in `/tmp/toe-lw15x/`. A check guides and never proves. Nothing here is a verdict.

**Source revisions read.** Branch `claude/toe-assembly` at `92e03055c` (this checkout). Files read at that commit, by line: `LW1_5_DRAFT.md` lines 1-510 (all; Theorem M at 124-132, Corollary M.1 at 134-136, the single-link [check] at 144, Lemma Q at 152-168, Theorem G at 190-198, Theorem R at 206-221, Theorem U at 254-262, section 8.1 at 300-318, section 11 at 446-466); `LW1_5U_DRAFT.md` lines 1-56 (head, law), 167-193 (section 5: Proposition X2, Lemma X1, three attacks, [check]); `LW1_5U_DRAFT.md` line 270 (section 9 table row); `B5B_DRAFT.md` lines 1-12, 37-39 (outcome), 92-176 (Lemmas G1-G3, Lemma T, Theorem B5b), 292-300 (Lemma T'). No other branch was read. Scratch: `/tmp/toe-lw15x/check_n.py` and `out_n.txt` (one [check], section 3).

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The laws `L5-U` and `L5-O[S_+]` are read as `LW1_5_DRAFT.md` section 8.1 states them. No reading, specification or definition is proposed here, so no four-test check is needed (section 7 says why).

**Working set used, by name.** PS-5 and PS-6r only through the two laws of `LW1_5_DRAFT.md` section 8.1. From `LW1_5_DRAFT.md`: Definition F1, Definition R1, compatibility (section 1.2), Theorem C, Lemma C1, Lemma C2, Theorem M, Corollary M.1, Theorem U, Lemma Q, Theorem G. From `LW1_5U_DRAFT.md`: Lemma X1 and Proposition X2. From `B5B_DRAFT.md`: Lemmas G1-G3 and the block method of Lemma T. PS-1, PS-2, PS-3, PS-4 and PS-7 are not used.

**Plan.** Section 0 quotes the target. Section 1 fixes notation. Sections 2-4 prove the target for `L5-U` with one rishon per link (`m = 1`). Section 5 treats `L5-U` with `2 ≤ m ≤ 9`. Section 6 treats `L5-O[S_+]`. Section 7 is the four-test note. The FINISH block closes.

---

## 0. The target, quoted

`LW1_5_DRAFT.md` line 448: "**LW1-5-X (OPEN, first).** For `L5-O[R]` (and `L5-U`), at angles `a ∈ 𝔈(H_C)` in the window, is every frame compatible with the cube gate `e^{iaH_C}` still Bogoliubov (resp. in `U(5)`)?"

`LW1_5U_DRAFT.md` line 173 (Proposition X2): "Outside a finite set of points `(ε, μ)` with `0 ≤ μ < 2ε < π`, every frame at `x` that is gate-wise compatible with `W_e` and `W_o` is `Ad Γ(u)` with `u ∈ U(5)`." At the finitely many remaining points it was open after three attacks (lines 185-187: charge commutant, probe products, spectral).

`LW1_5_DRAFT.md` line 70 (compatibility): "`φ` is *compatible with the gate `e^{iaH}`* if `(φ∘Ad L)(e^{iaH}) = e^{iaH}` for some such `L`", where line 68 says "A register change is `Ad L` with `L` a unitary on finitely many links."

Line 308 (the layers): "`M_e = ∏_{C∈𝒯_e}e^{−ia_eH_C}`, `M_o = ∏_{C∈𝒯_o}e^{ia_oH_C}`", with `a_e = ε − μ/2`, `a_o = ε + μ/2` and `0 ≤ μ < 2ε < π` (line 316). So the even angle obeys `0 < a_e ≤ ε < π/2`, and the odd angle obeys `0 < a_o < π`.

## 0.1 Outcome in one paragraph

**For `L5-U` with one rishon per link (`m = 1`), LW1-5-X is proved at every point of the window, with the even gate alone (Theorem X).** The proof has three steps. (A) At every angle `a ≠ 0`, the only elements of the site algebra `𝒜_x` that commute with a cube gate are the scalars (Lemma A). Two-site and three-site blocks, in the manner of B5B's Lemma T, give `Dc_{x,j} = c_{x,j}D` for such a `D`; the irrationality of `√((k+1)/k)` covers every angle. With `LW1_5U`'s Lemma X1, every compatible frame then keeps `N_x` (Corollary A.1). (B) On the one-particle sector of the cube the generator has norm at most `√3` (Lemma N). So for `|a| < π/√3` the gate determines the generator there, and a register change that commutes with the gate on that sector is trivial on the cube links (Lemma B). The even angle lies below `π/2 < π/√3` at every point of the window. (C) After one exact `U(5)` frame, the frame is the identity on `Λ^0 ⊕ Λ^1`, its register change is trivial, and Lemma A makes it trivial. So the compatible frames are exactly `U(5)`, and Proposition X2's finite set of possible bad points is empty. **For `2 ≤ m ≤ 9`:** a particle-hole duality maps `L5-U[m]` to `L5-U[10−m]` (Lemma D), so `m = 9` is proved too. For `2 ≤ m ≤ 8` the site commutant is trivial at every angle `0 < |a| < π√(3/5)`, so at every even angle of the window (Lemma A_m, by a centre argument with `U(5)`), and LW1-5-X holds at every point with `a_e < π/(√3ν'_m)` and at every point where `a_e` is not an exceptional angle of the one-particle (or, by duality, one-hole) sector (Theorem X_m). The remaining points lie in Proposition X2's finite set; the smallest open statement is **LW1-5-X-B_m**, the one-particle register commutant, after three failed attacks. **For `L5-O[S_+]`:** the site-commutant step carries over under an amplitude condition (Lemma A_O). The step that removes the register change does not: the Majorana hop conserves no matter number, so there is no analogue of Lemma X1 or of the one-particle sector. LW1-5-X for `L5-O[S_+]` stays open at Proposition X2's finitely many points as **LW1-5-X-O**, after three failed attacks. No counterexample is found for either law.

---

## 1. Setting

### 1.1 One cube of `L5-U`

Fix a site `x` and a cube `C ∋ x` of either tiling. Put `𝔐 = C ∖ {x}`. The cube has 40 matter modes `c_{z,j}` (`z ∈ C`, `j = 1, …, 5`) and twelve links. For a link `ℓ` with ends `s, t` write `r^{ℓ,s}_j` for the rishon modes at the `s`-end. The register of `ℓ` is the sector of total rishon number `m` of the ten modes `r^{ℓ,s}_j, r^{ℓ,t}_j`. Write `p_{ℓ,s} = Σ_j r^{ℓ,s†}_j r^{ℓ,s}_j`. `LW1_5_DRAFT.md` line 254 gives the hop for `ℓ = (s, t)`, `t = s + e_i`:
\[
h_\ell=\sum_{j,k}c_{t,j}^\dagger\,r^{\ell,t}_j r^{\ell,s\dagger}_k\,c_{s,k}+\text{h.c.}
\]
The cube generator is `H = 3^{-1/2} Σ_{ℓ⊂C} η_ℓ h_ℓ` with `η_ℓ = ±1` (line 307), and the gate is `W = e^{iaH}` with `a = −a_e` or `a = a_o`.

**Hop rule.** The term `c^†_{t,j} r^{ℓ,t}_j r^{ℓ,s†}_k c_{s,k}` moves a particle from `s` (colour `k`) to `t` (colour `j`) and a rishon from the `t`-end (colour `j`) to the `s`-end (colour `k`). Its adjoint does the reverse. So in both orientations: *a hop of a particle away from a site `u` along `ℓ` removes a rishon at the far end of `ℓ` and creates one at the `u`-end; the particle takes the colour of the removed rishon, and the created rishon takes the particle's old colour.*

**One rishon per link (`m = 1`).** Then each link's register is `C^{10}`, with basis `|s;k⟩ = r^{ℓ,s†}_k|0⟩` and `|t;j⟩`. Call a link state *blocking at `u`* if its rishon sits at the `u`-end, and *open at `u`* if it sits at the far end. By the hop rule, no particle can leave `u` along a link that is blocking at `u`.

**Conserved quantities used.** Every hop conserves the matter number of the cube. So `W` commutes with `N_x + N_𝔐`. Theorem U (`LW1_5_DRAFT.md` line 254) gives the Gauss generators `𝒢^T_x = Σ_{jk} c^†_{x,j}T_{jk}c_{x,k} + Σ_{ℓ∋x} Σ_{jk} r^{ℓ,x†}_j T_{jk} r^{ℓ,x}_k`, and line 258: "every `h^U_ℓ` commutes with every `𝒢^T_z`". So `W` commutes with every `𝒢^T_x`.

### 1.2 What a compatible frame is, as an operator

Let `φ` be a frame at `x` and `L` a unitary on finitely many links with `ψ := φ∘Ad L` and `ψ(W) = W`. By Theorem C(i) (line 87), `φ` acts on `𝒜_x = M_32(C)` as `Ad V` with `V` homogeneous. Order the modes of `x` first in a Jordan-Wigner map, as in Lemma M0 (line 116). Then `𝒜_x` acts as `M_32(C) ⊗ 1`, and an element `b` of parity `q` built from the matter of `𝔐` and links acts as `P_x^q ⊗ b̂`.

**Lemma 1.1.** If `V` is even, then `ψ = Ad(V ⊗ L)` on the algebra generated by `𝒜_x`, the matter of `𝔐` and all links. Here `V ⊗ L` acts as `V` on the modes of `x` and as `L` on the links.

*Proof.* On `a ∈ 𝒜_x`, `Ad(V ⊗ L)(a ⊗ 1) = VaV^* ⊗ 1 = φ(a)`. On `b` of parity `q`, `Ad(V ⊗ L)(P_x^q ⊗ b̂) = VP_x^qV^* ⊗ L b̂ L^* = P_x^q ⊗ Lb̂L^*`, because an even `V` commutes with `P_x`. This is `ψ(b) = Ad L(b)`, since `φ` fixes `b` and `L` fixes matter. ∎

---

## 2. The site commutant of a cube gate is trivial (`m = 1`)

For `ξ ∈ Λ^k(C^5)` write `|ξ; 0⟩` for the cube matter state with `x` in state `ξ` and `𝔐` empty. For a link `ℓ` with ends `u, v` put `T^ℓ_{u→v} = Σ_{j,k} c^†_{v,j} r^{ℓ,v}_j r^{ℓ,u†}_k c_{u,k}`. In both orientations `h_ℓ = T^ℓ_{u→v} + T^ℓ_{v→u}` and `T^ℓ_{v→u} = (T^ℓ_{u→v})^†` (for `ℓ = (u, v)` this is the definition; for `ℓ = (v, u)` the h.c. term of `h_ℓ` is `T^ℓ_{u→v}`).

**Lemma A (`m = 1`).** Let `C ∋ x` be a cube of either tiling, `W = e^{iaH}` its gate, and `a ∈ R`, `a ≠ 0`. If `D ∈ 𝒜_x` and `DW = WD`, then `D ∈ C·1`.

*Proof.* Let `𝒟` be the set of such `D`. It is a unital `*`-subalgebra of `𝒜_x`: if `DW = WD` then `W^*D = DW^*`, and the adjoint gives `D^*W = WD^*`.

*Step 1 (charges).* `e^{iθ𝒢^1_x}` commutes with `W` (section 1.1). Its link factor commutes with `𝒜_x`, so `Ad e^{iθ𝒢^1_x}(D) = e^{iθN_x}De^{−iθN_x}`. Hence `D_q := (2π)^{-1}∫_0^{2π} e^{−iqθ} e^{iθN_x}De^{−iθN_x}dθ` lies in `𝒟` for every integer `q`. `D_q` maps `Λ^k` into `Λ^{k+q}`, and `D = Σ_{q=−5}^{5} D_q`.

*Step 2 (two-site block).* Fix `k ∈ {1, …, 5}`, a neighbour `y` of `x` in `C`, the link `ℓ_1 = {x, y}` and a colour `j'`. Let `λ_0` be a basis state of the twelve registers in which `ℓ_1` has its rishon at the `y`-end in colour `j'` (open at `x`), the two other links of `C` at `x` are blocking at `x`, the two other links of `C` at `y` are blocking at `y`, and the other seven links are in any fixed basis state. The cube has no triangles, so these five links are distinct. Put `A_ξ = |ξ; 0⟩ ⊗ λ_0` and `B_ξ = T^{ℓ_1}_{x→y} A_ξ`. Only the term `j = j'` acts, so
\[
B_\xi=\sum_{k'}c^\dagger_{y,j'}c_{x,k'}|\xi;0\rangle\otimes\lambda_{k'},\qquad \lambda_{k'}:=r^{\ell_1,y}_{j'}r^{\ell_1,x\dagger}_{k'}\lambda_0 .
\]
In `λ_{k'}` the rishon of `ℓ_1` sits at the `x`-end in colour `k'`, so the `λ_{k'}` are orthonormal up to one common sign. Hence `‖B_ξ‖^2 = Σ_{k'}‖c_{x,k'}ξ‖^2 = k‖ξ‖^2`.

Which hops act. On `A_ξ`: only `x` holds particles, and of its links only `ℓ_1` is open at `x`. So `HA_ξ = sB_ξ` with `s = 3^{-1/2}η_{ℓ_1}`. On `B_ξ`: the particles at `x` cannot leave (`ℓ_1` now blocks at `x`, the others still do); the particle at `y` can leave only along `ℓ_1` (the other links at `y` block at `y`); all other sites are empty. So `HB_ξ = sT^{ℓ_1}_{y→x}B_ξ`. A direct computation in the one-rishon register gives `r^{ℓ_1,x}_{k''}r^{ℓ_1,y†}_{j'}λ_{k'} = δ_{k''k'}λ_0`, and `c^†_{x,k''}c_{y,j'}c^†_{y,j'}c_{x,k'}|ξ;0⟩ = c^†_{x,k''}c_{x,k'}|ξ;0⟩` because `y` is empty. So
\[
HB_\xi=s\sum_{k'}n_{x,k'}|\xi;0\rangle\otimes\lambda_0=s\,k\,A_\xi .
\]
On `span{A_ξ, B_ξ}` therefore `H^2 = β^2` with `β = √(k/3)`, and
\[
WA_\xi=\cos(a\beta)\,A_\xi+i\,s\,\frac{\sin(a\beta)}{\beta}\,B_\xi . \tag{2.1}
\]

*Step 3 (three-site block).* Keep `y` and `ℓ_1`. Pick a neighbour `z ≠ x` of `y` in `C`, the link `ℓ_2 = {y, z}` and a colour `j''`. Let `λ'_0` put `ℓ_1` open at `x` (rishon at the `y`-end, colour `j'`), `ℓ_2` open at `y` (rishon at the `z`-end, colour `j''`), the two other links at `x` blocking at `x`, the third link at `y` blocking at `y`, the two other links at `z` blocking at `z`, and the rest in fixed basis states. `x` and `z` are at distance two, so these seven links are distinct. Put `A_ξ = |ξ;0⟩ ⊗ λ'_0`, `B_ξ = T^{ℓ_1}_{x→y}A_ξ`, `C_ξ = T^{ℓ_2}_{y→z}B_ξ`. As in Step 2, `HA_ξ = sB_ξ`. On `B_ξ` two hops act: `y → x` along `ℓ_1` and `y → z` along `ℓ_2`; so `HB_ξ = skA_ξ + tC_ξ` with `t = 3^{-1/2}η_{ℓ_2}`. On `C_ξ` the only hop is `z → y` along `ℓ_2` (the rishon of `ℓ_2` now sits at the `y`-end; the other links at `z` block at `z`; `x` is still blocked; `y` is empty). The same one-rishon computation gives `T^{ℓ_2}_{z→y}C_ξ = B_ξ`, so `HC_ξ = tB_ξ`, and `‖C_ξ‖ = ‖B_ξ‖`. Then `H^2A_ξ = s^2kA_ξ + stC_ξ`, `H^2B_ξ = ω^2B_ξ` and `H^3 = ω^2H` on the span, with `ω^2 = s^2k + t^2 = (k+1)/3`. So
\[
e^{iaH}=1+i\frac{\sin a\omega}{\omega}H+\frac{\cos a\omega-1}{\omega^2}H^2
\]
there, and the `B`-part of `WA_ξ` is `i s (sin(aω)/ω) B_ξ`.

*Step 4 (one block has a nonzero `B`-part).* If `sin(aβ) = 0` and `sin(aω) = 0`, then `a√(k/3) = pπ` and `a√((k+1)/3) = p'π` with nonzero integers `p, p'` (`a ≠ 0`). Then `(k+1)/k = (p'/p)^2`, so `k(k+1)` is the square of the rational `kp'/p`, hence of an integer. But `k^2 < k(k+1) < (k+1)^2`. So for each `k` one of the two blocks gives `WA_ξ = αA_ξ + γ_kB_ξ + (\text{a }C\text{-part})` with `γ_k ≠ 0`, where `α, γ_k` depend on `k` and `a` only, not on `ξ`.

*Step 5 (charge zero).* Let `D ∈ 𝒟` with `D = D_0`. Then `D` is even and keeps each `Λ^k`. `D` commutes with `c^†_{y,j'}` and with every link operator. So `(D⊗1)A_ξ = A_{Dξ}`, and `(D⊗1)B_ξ = Σ_{k'} c^†_{y,j'}|Dc_{x,k'}ξ;0⟩ ⊗ λ_{k'}`. The span of the `B`-type vectors `c^†_{y,j'}|η;0⟩ ⊗ λ_{k'}` (`η ∈ Λ^{k−1}`) is orthogonal to the `A`- and `C`-type vectors (different matter at `𝔐` or different link states), and `D ⊗ 1` keeps all three types. Take the `B`-parts of `(D⊗1)WA_ξ = W(D⊗1)A_ξ = WA_{Dξ}`:
\[
\gamma_k\sum_{k'}c^\dagger_{y,j'}\big|(Dc_{x,k'}-c_{x,k'}D)\xi;0\big\rangle\otimes\lambda_{k'}=0 .
\]
The `λ_{k'}` are orthonormal and `c^†_{y,j'}` is injective on states with `y` empty. So `Dc_{x,k'} = c_{x,k'}D` on `Λ^k`, for every `k ≥ 1` and every colour `k'`. Apply this to `D^* ∈ 𝒟` (also of charge zero) and take adjoints: `c^†_{x,k'}D = Dc^†_{x,k'}` on all of `Λ(C^5)`. `D` keeps the line `Λ^0`, so `D|0⟩ = d|0⟩`, and then `D c^†_{x,k_1}⋯c^†_{x,k_r}|0⟩ = d\,c^†_{x,k_1}⋯c^†_{x,k_r}|0⟩`. So `D = d·1`.

*Step 6 (charge `q ≠ 0`).* `D_q^*D_q ∈ 𝒟` has charge zero, so it equals `c·1` by Step 5. If `q > 0`, `D_q` kills `Λ^5`; if `q < 0`, it kills `Λ^0`. So `c = 0` and `D_q = 0`. Hence `D = D_0 ∈ C·1`. ∎

*Remark.* Lemma A needs no window and no exceptional-set condition. It is the five-mode form of B5B's Lemma T (line 114), with `x` holding `k` particles instead of one; the ratio `√((k+1)/k)` replaces B5B's `√2`.

**Corollary A.1 (`N_x` is kept).** Let `φ` be compatible with the gate of a cube `C ∋ x`, at any `a ≠ 0`. Then `φ(N_x) = N_x`, `φ` acts on `𝒜_x` as `Ad V` with `V` even, and `V` keeps every `Λ^k`.

*Proof.* `LW1_5U_DRAFT.md` line 179, Lemma X1: "`D = φ(N_x) − N_x` is an even element of `𝒜_x` that commutes with `W`. If the only even elements of `𝒜_x` commuting with `W` are scalars, then `φ` preserves `N_x`." Its proof (line 181) uses only that `ψ` fixes `N_𝔐` and that `W` commutes with `N_x + N_𝔐`, both true here. Lemma A supplies the hypothesis. Then `VN_xV^* = N_x`, so `V` keeps each `Λ^k`. Each `Λ^k` lies in `H_+` or `H_−`, so `V` keeps `H_±`, and a homogeneous `V` that keeps `H_±` is even. ∎

---

## 3. On the one-particle sector the gate fixes the register change (`m = 1`)

Let `ℋ_1` be the space where the cube holds exactly one matter particle, tensored with the twelve cube registers. It has the orthonormal basis `|z, j⟩ ⊗ ρ`, with `|z, j⟩ = c^†_{z,j}|Ω⟩` (`Ω` the empty cube) and `ρ` a basis state of the registers. `H` maps `ℋ_1` into itself.

**Lemma N (one-particle norm).** For `m = 1`, `‖H|_{ℋ_1}‖ ≤ √3`.

*Proof.* Write `H = 3^{-1/2}(H^{(1)} + H^{(2)} + H^{(3)})`, with `H^{(i)}` the sum of `η_ℓh_ℓ` over the four links of `C` in direction `i`. These four links are disjoint and cover the eight sites. So `ℋ_1 = ⊕_ℓ ℋ_1^ℓ` over them, with `ℋ_1^ℓ` spanned by the states whose particle sits at an end of `ℓ`. `h_ℓ` keeps `ℋ_1^ℓ`, and the other three hops of direction `i` kill it (they need a particle at one of their ends). So `‖H^{(i)}|_{ℋ_1}‖ = max_ℓ ‖h_ℓ|_{ℋ_1^ℓ}‖`. Let `ℓ` have ends `u, v` and put `T = T^ℓ_{u→v}`. For one particle there are no fermion signs, and the one-rishon computation of section 2 gives
\[
T\big(|u,k\rangle\otimes|v;j\rangle_\ell\otimes\rho'\big)=-\,|v,j\rangle\otimes|u;k\rangle_\ell\otimes\rho',
\]
while `T` kills the basis states with the particle at `v` or the rishon of `ℓ` at the `u`-end. So `T` maps one set of basis vectors bijectively onto a disjoint set and kills the rest. Hence `T^*T` and `TT^*` are projections onto orthogonal subspaces, `T^2 = 0`, and `(T + T^*)^2 = T^*T + TT^* ≤ 1`. So `‖h_ℓ|_{ℋ_1^ℓ}‖ ≤ 1`, each `‖H^{(i)}|_{ℋ_1}‖ ≤ 1`, and `‖H|_{ℋ_1}‖ ≤ 3^{-1/2}·3 = √3`. ∎

[check] `/tmp/toe-lw15x/check_n.py`, output `out_n.txt` (a few seconds, under 100 MB): the one-mode analogue (one colour, one rishon per link, the cube `{0,1}^3` with signs `η = (1, (−1)^{x_1}, (−1)^{x_1+x_2})`), one-particle sector of dimension `8·2^{12} = 32768`. The largest eigenvalue is `1.3481`, below `√3 ≈ 1.7321`. This guides only; it is not the five-mode sector.

**Lemma B (`m = 1`).** Let `0 < |a| < π/√3`. Let `𝓛_C` be the twelve cube registers and `𝓛'` the registers of finitely many other links. Let `L` be a unitary on `𝓛_C ⊗ 𝓛'` such that `1 ⊗ L` commutes with `W` on `ℋ_1 ⊗ 𝓛'`. Then `L = 1_{𝓛_C} ⊗ L'` for a unitary `L'` on `𝓛'`.

*Proof.* `ℋ_1 ⊗ 𝓛'` is invariant under `H` and under `1 ⊗ L`. By Lemma N the spectrum of `H` there lies in `[−√3, √3]`. If `e^{iaλ} = e^{iaλ'}` for two eigenvalues, then `a(λ − λ') ∈ 2πZ` and `|a(λ − λ')| ≤ 2√3|a| < 2π`, so `λ = λ'`. So `t ↦ e^{iat}` is injective on the spectrum, and Lagrange interpolation gives a polynomial `f` with `f(W) = H` on `ℋ_1 ⊗ 𝓛'` (Corollary M.1's argument, `LW1_5_DRAFT.md` line 138). Hence `1 ⊗ L` commutes with `H` there. It also commutes with the matter matrix units `|z', j'⟩⟨z, j| ⊗ 1`. For a cube link `ℓ` with ends `u, v`, the display above gives the matrix entry
\[
\langle v,j|\,H\,|u,k\rangle=3^{-1/2}\eta_\ell\,r^{\ell,v}_j\,r^{\ell,u\dagger}_k\quad(\text{an operator on the registers}).
\]
So `L` commutes with `r^{ℓ,v}_j r^{ℓ,u†}_k ⊗ 1` for every cube link, both orders of its ends, and all colours. On the register `C^{10}` of `ℓ` these operators are, up to sign, the matrix units `|u;k⟩⟨v;j|` and `|v;j⟩⟨u;k|`; their products give `|u;k⟩⟨u;k'|` and `|v;j⟩⟨v;j'|`. So `L` commutes with `End(C^{10}_ℓ) ⊗ 1` for each of the twelve cube links. By the commutant statement of B5B's Lemma G3 (line 110: "The commutant of `M_n ⊗ 1` in `M_n ⊗ M_k` is `1 ⊗ M_k`"), applied link by link, `L = 1_{𝓛_C} ⊗ L'`. ∎

---

## 4. Theorem X: LW1-5-X for `L5-U` with `m = 1`

**Theorem X.** Take `L5-U` with `m = 1`. Let `C ∋ x` be a cube of either tiling and `0 < |a| < π/√3`. A frame `φ` at `x` is compatible with the gate `e^{iaH_C}` if and only if `φ` acts on `𝒜_x` as `Ad Γ(u)` with `u ∈ U(5)`. In particular, at every point `(ε, μ)` with `0 ≤ μ < 2ε < π`, every frame compatible with the even gate at `x` (angle `a_e = ε − μ/2 ∈ (0, π/2)`) is in `U(5)`. So LW1-5-X holds for `L5-U` with `m = 1` at every point of the window, and Proposition X2's finite set of possible bad points is empty.

*Proof.* "If": Theorem U (`LW1_5_DRAFT.md` lines 254-260) shows that `Γ(u)` with a register change on the six links at `x` leaves every gate unchanged at every angle.

"Only if". Let `ψ = φ∘Ad L` fix `W = e^{iaH_C}`. By Corollary A.1, `φ = Ad V` on `𝒜_x` with `V` even and keeping each `Λ^k`. Fix the phase of `V` so that `V|_{Λ^0} = 1`, and put `u = V|_{Λ^1} ∈ U(5)`. By Theorem U there is a unitary `R_u` on the six links at `x` such that `Ad(Γ(u) ⊗ R_u)` fixes `W` (line 260: "Each `e^{i𝒢^T_x}` is `Γ(e^{iT})` at `x` times rishon unitaries on the six links"). Put `V' = Γ(u)^*V` and `L' = R_u^*L`. By Lemma 1.1, `ψ = Ad(V ⊗ L)`, so `Ad(V' ⊗ L') = Ad((Γ(u) ⊗ R_u)^*)∘ψ` fixes `W`. `V'` is even, keeps each `Λ^k`, and is the identity on `Λ^0 ⊕ Λ^1`.

The one-particle space `ℋ_1 ⊗ 𝓛'` is invariant under `V' ⊗ L'` (`V'` keeps `N_x`, `L'` fixes matter). On it the state of `x` lies in `Λ^0 ⊕ Λ^1`, so `V' ⊗ L'` acts there as `1 ⊗ L'`. So `1 ⊗ L'` commutes with `W` on `ℋ_1 ⊗ 𝓛'`. Lemma B gives `L' = 1 ⊗ L''` with `L''` on links outside `C`, and `L''` commutes with `W`. So `Ad(V' ⊗ 1)` fixes `W`: `V'W = WV'` with `V' ∈ 𝒜_x`. Lemma A gives `V' ∈ C·1`, and `V'|_{Λ^0} = 1` gives `V' = 1`. So `V = Γ(u)` and `φ = Ad Γ(u)` on `𝒜_x`.

For the window: `0 < a_e = ε − μ/2 ≤ ε < π/2 < π/√3`. ∎

*Remarks.* (1) The odd gate is not needed. At the odd angle the same proof works when `a_o < π/√3`. (2) The proof does not use Theorem M or Corollary M.1 for the bound; it reproves the generator statement on the way. (3) The decisive spectral facts are two: the blocks of Lemma A, whose frequencies `√(k/3)` and `√((k+1)/3)` are never both resonant, and the one-particle bandwidth `2√3` of Lemma N, which keeps every exceptional coincidence of the one-particle sector out of `|a| < π/√3`. (4) `LW1_5U_DRAFT.md` records a single-link counterexample at `(n, m) = (2, 2)`, `a = π/√2`. It does not contradict Theorem X: it is a single-link gate, two modes, `m = 2`, and an angle above `π/√3`.

---

## 5. `L5-U` with `2 ≤ m ≤ 9`

### 5.1 Particle-hole duality `m ↔ 10 − m`

**Lemma D (duality).** Let `Θ` be the automorphism of the matter and rishon algebras with `Θ(c_{z,j}) = c^†_{z,j}` for every matter mode and `Θ(r^{ℓ,s}_j) = r^{ℓ,s†}_j` for every rishon mode. Then `Θ(T^ℓ_{u→v}) = T^ℓ_{v→u}`, so `Θ(h_ℓ) = h_ℓ` and `Θ(H_C) = H_C` for every cube. `Θ` maps the register sector `m` onto the sector `10 − m`, maps `𝒜_x` onto itself, fixes `𝒪_x` setwise, maps `N_x` to `5 − N_x`, and conjugates `Ad Γ(u)` to `Ad Γ(ū)`. Hence a frame `φ` is compatible with a gate of `L5-U[m]` at angle `a` if and only if `ΘφΘ^{-1}` is compatible with the same gate of `L5-U[10−m]`, and `φ ∈ U(5)` if and only if `ΘφΘ^{-1} ∈ U(5)`.

*Proof.* Rishons commute with matter. So
\[
\Theta\big(c^\dagger_{v,j}r^{v}_jr^{u\dagger}_kc_{u,k}\big)=c_{v,j}r^{v\dagger}_jr^{u}_kc^\dagger_{u,k}
=-\,r^{v\dagger}_jr^{u}_k\,c^\dagger_{u,k}c_{v,j}
=c^\dagger_{u,k}\,r^{u}_kr^{v\dagger}_j\,c_{v,j},
\]
using `c_{v,j}c^†_{u,k} = −c^†_{u,k}c_{v,j}` (`u ≠ v`) and `r^{v†}_jr^u_k = −r^u_kr^{v†}_j`. Summing over `j, k` gives `T^ℓ_{v→u}`. `Θ` maps the number `p_{ℓ,s}` to `5 − p_{ℓ,s}`, so it maps total rishon number `m` to `10 − m`. On a finite set of modes `Θ` is a Bogoliubov map and is implemented by a unitary; it is a product of one map per site and one per link, so it maps `𝒜_x` onto itself and `𝒪_x` onto itself. If `ψ = φ∘Ad L` fixes `W`, then `ΘψΘ^{-1} = (ΘφΘ^{-1})∘Ad(Θ L Θ^{-1})` fixes `Θ(W) = W`; `ΘφΘ^{-1}` fixes `𝒪_x` pointwise, so it is a frame at `x`; `ΘLΘ^{-1}` is a register unitary. Finally `Ad Γ(u)(c^†_j) = Σ_k u_{kj}c^†_k` becomes `c_j ↦ Σ_k u_{kj}c_k`, which is `Ad Γ(ū)`. ∎

So it suffices to treat `m ≤ 5`, and any statement proved on the one-particle sector of `L5-U[m]` holds on the one-hole sector of `L5-U[10−m]`.

### 5.2 The one-particle sector for general `m`

**Lemma N_m.** `‖H|_{ℋ_1}‖ ≤ √3 ν_m`, where `ν_m^2 = max{(m − p)(p + 1) : max(0, m − 5) ≤ p ≤ min(4, m − 1)}`. The values of `ν_m^2` for `m = 1, …, 9` are `1, 2, 4, 6, 9, 12, 16, 20, 25`.

*Proof.* As in Lemma N, it suffices to bound `‖h_ℓ|_{ℋ_1^ℓ}‖ = ‖T‖` for `T = T^ℓ_{u→v}` (again `T^2 = 0` and `T^*T`, `TT^*` live on the orthogonal spaces "particle at `u`" and "particle at `v`"). On "particle at `u`",
\[
T^*T=\sum_{k,k'}|u,k'\rangle\langle u,k|\otimes r^{u}_{k'}\,p_{\ell,v}\,r^{u\dagger}_k=(1\otimes p_{\ell,v})\,Z^*Z,
\]
with `Z(e_k ⊗ ρ) = r^{ℓ,u†}_kρ`; `p_{ℓ,v}` commutes with every `r^{ℓ,u}_k`. `Z^*Z` keeps the end numbers. On register states with `p_{ℓ,u} = p` it has norm at most `‖ZZ^*‖` on `p_{ℓ,u} = p + 1`, and `ZZ^* = Σ_k r^{ℓ,u†}_kr^{ℓ,u}_k = p_{ℓ,u}`, which is `p + 1` there. There `p_{ℓ,v} = m − p`. A hop needs `p ≤ 4` and `m − p ≥ 1`, and the register needs `m − p ≤ 5`. ∎

**Lemma B_m.** Lemma B holds for `L5-U[m]` with `π/√3` replaced by `π/(√3ν_m)`. More generally it holds at every `a` such that `t ↦ e^{iat}` is injective on the spectrum of `H|_{ℋ_1}`.

*Proof.* The functional-calculus step is as in Lemma B, with Lemma N_m. It remains to show that an operator `X` on `Λ^m(C^{10})` that commutes with every `r^{v}_j r^{u†}_k` and `r^{u}_k r^{v†}_j` (one link, ends `u, v`) is a scalar. Products give `(r^u_kr^{v†}_j)(r^v_jr^{u†}_k) = n^v_j(1 − n^u_k)` and `n^u_k(1 − n^v_j)`, with `n^s_j = r^{s†}_jr^s_j`. So `X` commutes with these. They are diagonal in the basis `e_S` (`S` an `m`-subset of the ten rishon modes) and separate it: if `v_j ∈ S ∖ S'`, then `n^v_j(1−n^u_k)` separates `e_S` from `e_{S'}` for any `u_k ∉ S`, and `n^u_k(1−n^v_j)` does for any `u_k ∈ S'`; if neither exists, `S` holds all five `u`-modes and `v_j`, and `S'` holds no `u`-mode and not `v_j`, so `|S| ≥ 6 > 4 ≥ |S'|`, impossible. (The case `u_k ∈ S ∖ S'` is the same with the ends exchanged.) So `X` is diagonal, `Xe_S = x_Se_S`. The operator `r^v_jr^{u†}_k` maps `e_S` to `±e_{S − v_j + u_k}` when `v_j ∈ S`, `u_k ∉ S`. So `x_S = x_{S'}` whenever `S'` arises from `S` by one *trade*: drop a `v`-mode and add a `u`-mode, or the reverse. Any two `m`-subsets are joined by trades. (i) To replace `v_j ∈ S` by `v_{j'} ∉ S`: if some `u_k ∉ S`, trade `v_j → u_k`, then `u_k → v_{j'}`; if all `u_k ∈ S`, trade `u_1 → v_{j'}`, then `v_j → u_1`. The same works inside the `u`-block. (ii) If `|S ∩ v| > |S' ∩ v|`, then `|S ∩ u| < |S' ∩ u| ≤ 5`, so some `u_k ∉ S`, and one trade `v_j → u_k` lowers `|S ∩ v|` by one. By (ii) reach the block counts of `S'`, then by (i) reach `S'`. So `x_S` is constant. ∎

### 5.3 The site commutant for general `m`

**Lemma A_m.** Let `1 ≤ m ≤ 5`, `C ∋ x` a cube, and `0 < |a| < π√(3/5)`. If `D ∈ 𝒜_x` and `DW = WD`, then `D ∈ C·1`. By Lemma D the same holds for `5 ≤ m ≤ 9`.

*Proof.* Let `𝒟` be as in Lemma A. Step 1 of Lemma A applies unchanged: the charge parts `D_q` lie in `𝒟`. Let `𝒟_0` be the charge-zero part, a unital `*`-subalgebra of `⊕_k End(Λ^k)`.

*Step 1 (`U(5)`-invariance).* For Hermitian `T`, `e^{i𝒢^T_x}` commutes with `W`, its link factor commutes with `𝒜_x`, and it acts on `𝒜_x` as `Ad Γ(e^{iT})`. So `Ad Γ(u)` maps `𝒟_0` onto itself for every `u ∈ U(5)`.

*Step 2 (invariants).* If `Y` on `Λ(C^5)` commutes with every `Γ(u)`, then `Y ∈ span{Π_0, …, Π_5}`. Indeed, `Y` commutes with `Γ(e^{iθ}1) = e^{iθN_x}`, so it keeps each `Λ^k`. Differentiating `Γ(e^{itE})` gives that `Y` commutes with every `c^†_ic_j`. The `n_i = c^†_ic_i` separate the basis vectors `e_S` (`|S| = k`), so `Y` is diagonal, `Ye_S = y_Se_S`. `c^†_ic_j` maps `e_S` to `±e_{S−j+i}` for `j ∈ S`, `i ∉ S`, and single swaps join any two `k`-subsets. So `y_S` is constant on `Λ^k`.

*Step 3 (the centre).* The centre `𝒵_0` of `𝒟_0` is a commutative finite-dimensional `*`-algebra, so it is spanned by its minimal projections `e_1, …, e_s` (simultaneous diagonalization). Each `Ad Γ(u)` is an automorphism of `𝒟_0`, so it permutes them. For each `i`, `u ↦ Ad Γ(u)(e_i)` is continuous with values in the finite set `{e_1, …, e_s}`, whose distinct elements are at norm distance one. `U(5)` is connected, so the map is constant: `Ad Γ(u)(e_i) = e_i`. By Step 2, `e_i ∈ 𝒟_0 ∩ span{Π_k}`.

*Step 4 (no function of `N_x` commutes with `W`).* Let `f(N_x) ∈ 𝒟`. Then `(f(k−1) − f(k))Π^x_{k−1}WΠ^x_k = 0`. It suffices to show `Π^x_{k−1}WΠ^x_k ≠ 0` for `k = 1, …, 5`. Take a neighbour `y` of `x`, `ℓ_1 = {x, y}`, a Fock state of `x` with occupied colour set `F` (`|F| = k`), and `𝔐` empty. Put all `m` rishons of every other link at `x` at its `x`-end, and all `m` rishons of every other link at `y` at its `y`-end (possible since `m ≤ 5`); then no particle can leave `x` or `y` along those links. Choose the `x`-end colours `S` and `y`-end colours `T` of `ℓ_1` as follows.
- If `k ≥ m`: `S ⊂ F` with `|S| = m − 1`, and `T = {j'}`.
- If `k ≤ m`: `S = F ∖ {k_0}` for one `k_0 ∈ F`, and `|T| = m − k + 1` (between 1 and 5).

By the hop rule a particle of colour `c` leaves `x` along `ℓ_1` only if `c ∈ F ∖ S` and `T ≠ ∅`; it then takes a colour `j ∈ T`, and the `x`-end gains colour `c`. In both cases, after one departure no second one is possible (first case: `T` is used up; second case: the new `x`-end set is `F`, which covers every remaining particle). The particle at `y` can return only into an `x`-colour that the `x`-end holds and `x` lacks; that set is `(S ∩ F^c) ∪ {c} = {c}`, because `S ⊂ F`. So it returns to the starting state. Hence the starting state `A` and the `n` one-departure states `B_1, …, B_n` span an invariant space, with `n = k − m + 1` in the first case and `n = m − k + 1` in the second, and `1 ≤ n ≤ 5`. On it `HA = s Σ_i σ_iB_i`, `HB_i = sσ_iA` with `s = 3^{-1/2}η_{ℓ_1}`, `σ_i = ±1`. So `H^2A = (n/3)A`, and `WA = cos(aβ)A + i(sin(aβ)/β)HA` with `β = √(n/3)`. `HA ≠ 0` has `N_x = k − 1`. Since `0 < |a|β < π√(3/5)·√(5/3) = π`, `sin(aβ) ≠ 0`. So `Π^x_{k−1}WA ≠ 0`.

*Step 5 (`𝒟_0 = C`).* By Steps 3-4 each `e_i` is a scalar projection, so `𝒵_0 = C·1`. Let `ρ_0: 𝒟_0 → End(Λ^0) = C` be restriction to the line `Λ^0`; it is a unital `*`-homomorphism, and its kernel `J` is a `*`-ideal. If `J ≠ 0`, let `h = Σ_i x_i^*x_i` over a basis `x_i` of `J`, and let `e` be the support projection of `h`, a polynomial in `h` without constant term, so `e ∈ J`. For `x = Σα_ix_i ∈ J`, `x^*x ≤ (Σ|α_i|^2)h` (Cauchy-Schwarz), so `x = xe`, and likewise `x = ex`. For `y ∈ 𝒟_0`, `ye, ey ∈ J`, so `ye = e(ye) = (ey)e = ey`. So `e` is a central projection, `e ≠ 0`, and `ρ_0(e) = 0 ≠ 1`, against `𝒵_0 = C·1`. So `J = 0`, `ρ_0` is injective, and `𝒟_0 = C·1`.

*Step 6.* The charges `q ≠ 0` vanish as in Step 6 of Lemma A. ∎

### 5.4 Theorem X_m and what stays open

**Theorem X_m.** Take `L5-U[m]`, `1 ≤ m ≤ 9`. Put `ν'_m = min(ν_m, ν_{10−m})`, so `ν'^2_m = 1, 2, 4, 6, 9, 6, 4, 2, 1` for `m = 1, …, 9`. Let `C ∋ x` be a cube and `0 < |a| < π/(√3ν'_m)`. Then the frames at `x` compatible with `e^{iaH_C}` are exactly the `Ad Γ(u)`, `u ∈ U(5)`. For `m ≤ 5` the same holds at every `a` with `0 < |a| < π√(3/5)` at which `t ↦ e^{iat}` is injective on the spectrum of `H_C|_{ℋ_1}`.

*Proof.* For `m ≤ 5`, `ν'_m = ν_m` and `π/(√3ν_m) ≤ π/√3 < π√(3/5)`. Repeat the proof of Theorem X with Lemma A_m for Lemma A and Lemma B_m for Lemma B. For `m ≥ 6`, apply Lemma D: the statement for `m` is the statement for `10 − m`. ∎

**Corollary X_m.1 (the window).** For `m = 1` and `m = 9`, LW1-5-X holds at every point of the window (the even gate suffices). For `2 ≤ m ≤ 8` it holds at every point with `a_e < π/(√3ν'_m)`, and at every point where `a_e` (for `m ≤ 5`) is not an exceptional angle of the one-particle sector. Numerically the sub-windows are `a_e < π/√6 ≈ 1.28` (`m = 2, 8`), `π/(2√3) ≈ 0.91` (`m = 3, 7`), `π/√18 ≈ 0.74` (`m = 4, 6`), `π/(3√3) ≈ 0.60` (`m = 5`).

For `2 ≤ m ≤ 8` the remaining points lie in Proposition X2's finite set, since an exceptional angle of `H_C|_{ℋ_1}` is an exceptional angle of `H_C`. The step that fails there is Lemma B_m. Stated as the smallest exact open statement:

**LW1-5-X-B_m (OPEN, `2 ≤ m ≤ 5`; `m ≥ 6` by Lemma D on the one-hole sector).** Let `a` be an exceptional angle of `H_C|_{ℋ_1}` with `π/(√3ν_m) ≤ |a| < π/2`. If a unitary `L` on the registers is such that `1 ⊗ L` commutes with `e^{iaH_C}` on `ℋ_1`, then `L` acts as a scalar on the twelve cube registers. (By the proof of Theorem X, LW1-5-X-B_m at `a = −a_e` gives LW1-5-X for `L5-U[m]` at `(ε, μ)`.)

Three attacks failed.
- *Attack 1 (functional calculus).* This is Lemma B_m's route. It needs `t ↦ e^{iat}` injective on the one-particle spectrum. Lemma N_m bounds the bandwidth by `2√3ν_m ≥ 2√6`, and `2√6·π/2 > 2π`, so coincidences in `|a| < π/2` are not excluded; at an exceptional angle of `H_C|_{ℋ_1}` the route has nothing left.
- *Attack 2 (gauge covariance and the centre).* The algebra `𝒵 = {L : [1⊗L, W] = 0 on ℋ_1}` is invariant under the link parts of the gauge transformations of all eight sites, a connected group. As in Step 3 of Lemma A_m its centre lies in the functions of the end numbers `p_{ℓ,s}`; blocks like Step 4 can make the centre trivial. The last step fails: Step 5 of Lemma A_m used a line (`Λ^0`) that `𝒟_0` keeps. `𝒵` is not known to keep any joint eigenspace of the end numbers, and for `2 ≤ m ≤ 4` none of them is a line anyway. So `𝒵` may be a large factor.
- *Attack 3 (blocks).* Blocks fix register basis states. `L` may map them to superpositions, so commutation on a block constrains only some matrix elements of `L`. Lemma A's blocks worked because there the unknown `D` acts on `x` only and the register state is left alone.

No counterexample is found. A frame outside `U(5)` at such a point would need, by Theorem X_m's proof, a register unitary `L` that is not a scalar and commutes with the one-particle gate.

---

## 6. `L5-O[S_+]`

### 6.1 What carries over

`LW1_5_DRAFT.md` line 188, Theorem G(ii): "for every `g` in the group generated by the `e^{iθ𝒢_x^{cd}}`, `Ad g` is a frame at `x` composed with a register change on the six links at `x`, made link by link; it leaves every gate of the update unchanged; its action on `𝒜_x` is the Bogoliubov frame of an element of `SO(10)`, and every element of `SO(10)` occurs". Its `U(5)` subgroup includes `e^{iθΣ_j𝒢^{2j−1,2j}_x}`, which acts on `𝒜_x` as `Ad e^{iθ(N_x − 5/2)}` (since `n_{x,j} − 1/2 = M^{2j−1,2j}_x`, line 51 and line 248). So the charge decomposition and Steps 1-3, 5, 6 of Lemma A_m run unchanged for `L5-O[S_+]`, with `Γ(u)` for `u ∈ U(5) ⊂ SO(10)`. Only Step 4 used the law. This gives:

**Lemma A_O (reduction).** Let `W` be a cube gate of `L5-O[S_+]` at angle `a`. Suppose the nonzero blocks `Π^x_{k'}WΠ^x_k` connect `{0, 1, …, 5}` (as edges `{k, k'}`, `k ≠ k'`). Then every `D ∈ 𝒜_x` with `DW = WD` is a scalar.

*Proof.* If `f(N_x)` commutes with `W`, then `(f(k') − f(k))Π^x_{k'}WΠ^x_k = 0`, so `f` is constant on connected sets. The rest is Lemma A_m's proof. ∎

The hypothesis holds for all small `|a|`, since `Π^x_{k±1}HΠ^x_k ≠ 0` (each Majorana `γ_{x,b}` changes `N_x` by one, and Theorem M(i)'s inflow is faithful). At a given angle of the window it is an amplitude condition. It is not checked here.

### 6.2 What does not carry over

The proof of Theorem X used two more facts. (i) Lemma X1: `W` commutes with `N_x + N_𝔐`, a charge with no link part, so `φ(N_x) − N_x` commutes with `W`. (ii) The one-particle sector `ℋ_1`, on which a normalized frame acts trivially and the gate determines the generator. Both rest on matter-number conservation. The Majorana hop (4.1) of `LW1_5_DRAFT.md` contains pairing terms `c_yc_x` times link operators (line 318: "its hop also contains pairing terms"). The only conserved charges are the Gauss generators `𝒢^{cd}_z`, and every one of them has a link part, which `Ad L` moves. So neither (i) nor (ii) is available.

**LW1-5-X-O (OPEN).** For `L5-O[S_+]`, at the finitely many points of Proposition X2 (both `a_e` and `a_o` exceptional for `H_C`): is every frame compatible with the even and the odd gate Bogoliubov? The smallest open statement this lane isolates is the analogue of (i) and (ii) together: *a ψ-fixed subspace of the cube on which, after an exact `SO(10)` frame, `φ` acts trivially and the gate determines the generator.* With such a subspace, the proof of Theorem X runs (Lemma B's commutant step needs only that the `U^{ab}_ℓ` generate `End(S_+)`; by Lemma Q3 this is the irreducibility of `S_+` under `so(20)`, standard and not rebuilt here).

Three attacks failed.
- *Attack 1 (the `L5-U` route).* Lemma X1 needs a conserved charge `Q_x + Q_𝔐` with `Q_x ∈ 𝒜_x` not scalar and no link part. For `L5-O` the only matter-only conserved quantity is the parity `P_xP_𝔐`, and `φ(P_x) = ±P_x` holds for every frame. So Lemma X1 gives nothing, and the sector `ℋ_1` has no analogue: the matter vacuum is not invariant under the Majorana hop.
- *Attack 2 (parity slices).* `ψ` fixes `P_𝔐`, so it fixes the part of `W` odd in `𝔐`. Its `x`-slices are odd elements of `𝒜_x`. At a finite angle they include Majorana products of degree 3, 5, 7 and 9, so the slice space can be all of the odd part (512 dimensions), and preserving it is automatic for every frame (Lemma G1). This is `LW1_5_DRAFT.md` line 450's Attack 1 in the gate form; the matter projections of `𝔐` do not cut the degree down, because no matter number constrains the `x`-degree.
- *Attack 3 (Lie algebra of the compatible group).* The compatible group `K_W` is compact and contains `SO(10)`. Its Lie algebra is an `SO(10)`-submodule of the even part of `𝒜_x` modulo scalars, `45 ⊕ 45 ⊕ 210 ⊕ 210 ⊕ 1` (the even Clifford degrees `2, 8, 4, 6, 10`). So only finitely many candidate algebras exist. But excluding each one needs the spectral projections of the gate on the sectors that candidate mixes, which this attack does not supply; and the component group of `K_W` is not controlled by its Lie algebra at all.

No counterexample is found.

---

## 7. Four-test note

This file proposes no reading, specification or definition. The objects it introduces (`𝒟`, `ℋ_1`, `ν_m`, the duality `Θ`, blocks) are tools inside proofs; they fix no part's target, are closed, settle no downstream question and add no structure to any law. Lemma D is a symmetry of the stated law, not a change to it. So the four-test check has nothing to test.

---

## FINISH

**Proved here (pass 1, not refereed).**
- Lemma 1.1: a compatible frame with even implementer acts on one cube as `Ad(V ⊗ L)`.
- Lemma A (`L5-U`, `m = 1`): at every angle `a ≠ 0`, the only elements of `𝒜_x` commuting with a cube gate are scalars. Corollary A.1: every compatible frame keeps `N_x` and has an even implementer.
- Lemma N and Lemma B (`m = 1`): the one-particle norm of `H_C` is at most `√3`; for `0 < |a| < π/√3` a register unitary that commutes with the gate on the one-particle sector is trivial on the twelve cube registers.
- **Theorem X (`L5-U`, `m = 1`): for every cube gate at `0 < |a| < π/√3`, the compatible frames at `x` are exactly `Ad Γ(u)`, `u ∈ U(5)`. Hence LW1-5-X holds at every point `0 ≤ μ < 2ε < π`, by the even gate alone, and Proposition X2's finite set of possible bad points is empty.**
- Lemma D: the particle-hole map `Θ` carries `L5-U[m]` to `L5-U[10−m]`, compatible frames to compatible frames, and `U(5)` to `U(5)`. Hence Theorem X holds for `m = 9`.
- Lemma N_m, Lemma B_m, Lemma A_m (`m ≤ 5` at `0 < |a| < π√(3/5)`; `m ≥ 5` by Lemma D), Theorem X_m and Corollary X_m.1: for `2 ≤ m ≤ 8`, LW1-5-X holds at every point with `a_e < π/(√3ν'_m)` (`ν'^2_m = 2, 4, 6, 9, 6, 4, 2`) and at every point where `a_e` is not an exceptional angle of the one-particle (`m ≤ 5`) or one-hole (`m ≥ 6`) sector.
- Lemma A_O (`L5-O[S_+]`, reduction): the site commutant of a cube gate is trivial whenever the nonzero blocks `Π^x_{k'}WΠ^x_k` connect `{0, …, 5}`.

**Counterexamples.** None. Remark (4) of section 4 records why the single-link counterexample of `LW1_5U_DRAFT.md` (`(n, m) = (2, 2)`, `a = π/√2`) does not transfer to Theorem X.

**Open, by name.**
- **LW1-5-X-B_m** (`2 ≤ m ≤ 8`): at an exceptional angle of the one-particle sector with `π/(√3ν_m) ≤ |a| < π/2`, a register unitary that commutes with the gate on that sector is a scalar on the cube registers. It implies LW1-5-X for `L5-U[m]`. Three attacks failed: functional calculus, gauge covariance and the centre, blocks (section 5.4). The open points lie inside Proposition X2's finite set.
- **LW1-5-X-O** (`L5-O[S_+]`): at Proposition X2's finitely many points, LW1-5-X is open. The missing object is a ψ-fixed sector on which a normalized frame acts trivially and the gate determines the generator; the Majorana hop conserves no matter number, so the `L5-U` sector does not exist. Three attacks failed: the `L5-U` route, parity slices, the Lie algebra of the compatible group (section 6.2). The amplitude hypothesis of Lemma A_O at the window's angles is unchecked.

**What changes downstream.**
- `LW1_5_DRAFT.md` section 11, LW1-5-X: closed for `L5-U` with `m = 1` and `m = 9`; reduced to LW1-5-X-B_m for `2 ≤ m ≤ 8`; still open for `L5-O[S_+]` as LW1-5-X-O. Section 7's table: the `L5-U` row's upper bound `U(5)` holds gate-wise at every angle of the window for `m ∈ {1, 9}`.
- `LW1_5U_DRAFT.md` section 9 (the comparison table for LW1-5-RQ), row "Frame bound at exceptional angles": for `L5-U` with `m = 1` the entry becomes "closed (Theorem X)"; the `L5-O` entry is unchanged. This adds one point on the `L5-U` side of the owner decision LW1-5-RQ; it decides nothing.
- GA1-i: under `L5-U[m=1]` the exact frame group `U(5)` now holds for gate-wise compatibility at every parameter point, not only outside a finite set.
- The register datum `m`: the proof is complete at the smallest register (`m = 1`, dimension 10) and its dual (`m = 9`). This is a fact about the proof, not a reason to choose `m`.
- The odd gate is not needed for the frame bound of `L5-U[m = 1]`. B5B's one-mode result (`B5B_DRAFT.md` line 39: "no exceptional angle enlarges the mode image") is the one-mode case of the same block method.

**Inputs from outside the working set.** `LW1_5_DRAFT.md`'s Theorems C, G, U, Lemma M0, Corollary M.1's interpolation argument; `LW1_5U_DRAFT.md`'s Lemma X1 and Proposition X2; `B5B_DRAFT.md`'s Lemmas G1 and G3 and its block method (Lemma T). Standard mathematics, rebuilt in the text: Jordan-Wigner ordering, Lagrange interpolation, simultaneous diagonalization of commuting normal matrices, the operator Cauchy-Schwarz inequality, irreducibility of `Λ^k(C^5)` under `U(5)` (as a commutant computation), connectivity of subsets under single swaps, irrationality of `√(k(k+1))`. Standard mathematics cited, not rebuilt: connectedness of `U(5)`; irreducibility of `S_+` under `so(20)` (only in a remark on a route that does not exist yet). Literature context, credited from memory and never load-bearing: quantum link models and rishons (Horn; Orland-Rohrlich; Chandrasekharan-Wiese; Brower-Chandrasekharan-Wiese), as credited in `LW1_5_DRAFT.md`.
