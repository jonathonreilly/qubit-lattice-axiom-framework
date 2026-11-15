lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# VC1 on the five-mode laws, pass 1: does a gauged vacuum exist?

Written 2026-11-05 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 of part VC1 on the laws `L5-O` and `L5-U`, under the method of open PR #10138 (Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen).

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks one tiny scratch computation (`/tmp/toe-vc15/check_pairs.py`, 13 s, 27 MB, run after `memory_pressure` showed 60 percent free). A check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local checkout, branch `claude/toe-assembly` (sparse) | `92e03055c` |
| last change of the files below in that checkout | `7d2b20d298` |

No other branch was read.

Files read at that commit, by line. This folder: `TOE_ASSEMBLY.md` lines 1-43 (head, axioms, primitives), 71-95 (section 3 table), 139-145 (PS-7), 169-221 (sections 3.2-3.5, with PS-1c at 180 and PS-7r at 184), 474-486 (VC1); `LW1_5U_DRAFT.md` lines 1-309 (all; Lemma P at 60, Proposition Σ-U at 87, LW1-5U-Σc at 101, Lemma H-U at 140, Theorem F-U at 150, Remarks F.1-F.2 at 159-161); `LW1_5O_DRAFT.md` lines 1-328 (all; Theorem S1 at 185, Lemma S2 at 195, Theorem S3 at 205, Proposition S5 at 224); `LW1.md` lines 1-240 (status, definitions, statement of `L_cube`, A1-B5) and 385-502 (E1-E6, gaps, VC1 at 502); `LW1_5_DRAFT.md` lines 45-62 (one site), 148-262 (Lemma Q, Theorem G, Proposition Σ, Lemma Z, Lemma H, Theorem U), 298-347 (section 8), 349-420 (section 9, with B1-5 at 392, B8b-5 at 404, E2b-5 at 416); `Y2W_DRAFT.md` (format only); `LW1U_DRAFT.md` lines 32, 48, 196-202 (what "factor state" means there), by grep; `CG1_KILL_DRAFT.md`, `CH1_5_DRAFT.md`, `GA2_Y2_DRAFT.md`, by grep for "VC1" only.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The working set is read plainly. The lane's item (iv) needs a reading; section 1.4 states two readings and puts each through the four tests. Nothing is adopted.

**Working set used, by name.** PS-1 read by PS-1c (the symmetry group of item (iii)); PS-5 (fallback text, D1); PS-6 read by PS-6r (finite link registers); PS-7 and PS-7r (only to say what "half filled" asks; section 6); LW1's conjugation reading of local gauge invariance (`LW1.md` line 47). PS-3 read by PS-3c, and the proposed reading PS-3h5 of `LW1_5_DRAFT.md` section 8.2 (not in the working set), only in Corollary O3. PS-2, PS-4, PS-11 are not used. Results used, by name: `LW1.md` A1, A2, E1 (frozen); `LW1_5_DRAFT.md` Theorem G, Theorem U, Lemma H, B1-5, B8b-5(ii) and section 8.1; `LW1_5U_DRAFT.md` Lemma P, Lemma S, Proposition Σ-U; `LW1_5O_DRAFT.md` Lemma S2. Each step used from these is re-derived or quoted at the point of use.

**Inputs from outside the working set.** Standard mathematics, rebuilt in the text: Cauchy-Schwarz for states, purity tested by positive functionals below a state, Schur's lemma for unitary representations, uniqueness of the normalized trace on a full matrix algebra, joint eigenspaces of commuting operators on tensor products. Standard mathematics cited, not rebuilt: existence and invariance of Haar measure on a compact Lie group; existence of weak-* limit points of states (Banach-Alaoglu). One theorem is mentioned and never used as a step: Powers' cluster criterion for factor states (Ann. Math. 1967), credited in `LW1U_DRAFT.md` line 48. Literature context, credited from memory and never load-bearing: Rokhsar-Kivelson states of quantum dimer and ice models; Lieb-Schultz-Mattis type constraints on symmetric states at fractional filling.

---

## 0. The question, quoted

`TOE_ASSEMBLY.md` line 476, VC1(a): "Under `L` and PS-7, there is a translation- and rotation-invariant stationary state `omega_0` of the update (the vacuum) such that (1) it is stable: ... (2) the matter of MT1 is its particle-hole excitations; (3) its energy density ... (4) the record behaviour in `omega_0` is fixed (whether records form there; TM1-i)."

Line 140, PS-7: "The vacuum is the half-filled state of the update's fermion modes." Line 184, PS-7r: "For the gauged law, the vacuum is the state VC1 builds from this sea; PS-7 does not name it by itself."

Line 219 (section 3.5): "Both laws, and `L_cube`: on a periodic box, no pure, locally gauge-invariant, site-transitive state is half filled (`LW1_5U_DRAFT.md` Theorem F-U and Remark F.1). PS-7r already leaves the gauged vacuum to VC1, so this is VC1's question."

`LW1.md` line 47: "Gauge invariance of a state means invariance under these conjugations, not support in the sector \(\mathcal G_x=0\)." Line 502: "E2b proves existence of stationary gauge-invariant half-filled states, not their uniqueness, a sea-continuation property, purity, or a vacuum selection."

`LW1_5U_DRAFT.md` line 101: "(a) Invariance of a pure all-site singlet under the point group `O_{c_0}`. For odd `m` the configuration above depends on link orientation. For even `m` with `α = m/2` the configuration is symmetric, but the action of the site stabilizer on the invariant space is not computed. Open as **LW1-5U-Σc**." Line 304 lists as open: "The infinite-volume form of Theorem F-U and Remark F.1."

`LW1_5O_DRAFT.md` line 224, Proposition S5: on a finite region of one-class `L5-O`, "the density matrix `d_λ^{-1}1_{V_λ} ⊗ |w⟩⟨w|` is gauge invariant in LW1's sense, and its restriction to the gauge-invariant operators is the pure vector state `w`". It is a finite-region statement, and it does not address stationarity.

**The lane's target.** For each of `L5-O` and `L5-U`, prove or refute the existence of a state `ω` of the quasi-local algebra with (i) `ω∘α = ω` for the tick `α`; (ii) `ω` invariant under every local gauge automorphism; (iii) `ω` invariant under the lifts of the cell translations and proper cubic rotations of PS-1c; (iv) `ω` "factor", in a reading to be stated and checked. Say what filling `ω` has. Settle LW1-5U-Σc.

## 0.1 Outcome in one paragraph

**Readings of (iv).** Reading E: `ω` is extremal among the states invariant under the group generated by the tick, the local gauge automorphisms and the lifts of `𝒢`. Reading P: the restriction of `ω` to the gauge-invariant algebra `𝔄^G` is pure. For gauge-invariant states, P is the same as "extremal under the local gauge group alone", and P implies E (Lemma R). Both pass tests 1, 2 and 4; P is conditional on test 3, because on `L5-U` it decides the half-filling question (section 1.4). **`L5-O[S_+]`: yes under both readings, at half filling.** The tracial state meets (i)-(iii) and E (Theorem O1). The gauge average `ω_0` of the empty-matter, rishon-vacuum product state meets (i)-(iii) and P, hence E (Theorem O2). Every locally gauge-invariant state of `L5-O` has filling `5/2` (Lemma H), so both witnesses are half filled. A second P-witness comes from full matter and full rishons, so (i)-(iv) do not single out a state. **`L5-U[m]`.** Under E: yes, at every filling in `[0, 5]` (Theorem U1). Under P: every state that is invariant under the link reversals of `𝒢` and sharp in every Gauss charge `Q_x` has filling `q_x − 3m` with `q_x` an integer (Theorem U2, at infinite volume, with no box and no dynamics). So a P-state of `L5-U` is never half filled, for every `m`, every constant and every plaquette class. The same holds for `L_cube`: filling `0` or `1` (Corollary U2'). This is the infinite-volume form that `LW1_5U_DRAFT.md` left open. For even `m`, P-states with (i)-(iii) exist at fillings `0` and `5` (Theorem U3). For odd `m`, no product state over a nontrivial `𝒢`-invariant partition of the links, with sharp matter numbers, meets (iii) and P (Theorem U4); existence for odd `m` is open after three named attacks (section 4.5). **LW1-5U-Σc.** For even `m`, pure all-site singlets invariant under every lift of `𝒢` exist, with filling `n_m ∈ {4, 3, 2, 1}` for `m = 2, 4, 6, 8` (Theorem Σc(i)). For odd `m`, no state with sharp end numbers on a link is invariant under the reversal of that link, so no singlet of Proposition Σ-U(iii), and no site-product state, is point-group invariant (Theorem Σc(ii)). **Named failing step.** If PS-7 is read as asking the gauged vacuum to be half filled, then `L5-U` (and `L_cube`) fails at Theorem U2 under reading P. Under reading E there is no failing step. `L5-O` has no failing step under either reading. **Scope.** All witnesses are for the base tick `U_0 = W_E M_o M_e`, every value of `ε, μ, τ_E`, and no plaquette class. The P-witnesses are "dark": every hop annihilates them. They are not built from the PS-7r sea.

---

## 1. Setting

### 1.1 The two laws

Notation of `LW1.md` section 1: sites `x ∈ Z^3`, tilings `𝒯_e`, `𝒯_o`, signs `η_i(x)`, angles `a_e = ε − μ/2`, `a_o = ε + μ/2`, and `𝒢 = 2Z^3 ⋊ O_{c_0}`. Both laws are those of `LW1_5_DRAFT.md` section 8.1.

**`L5-O[S_+]`.** Site `x` carries Majoranas `γ_{x,1..10}` and modes `c_{x,j} = (γ_{x,2j−1} + iγ_{x,2j})/2`. Link `ℓ = (x, y)`, `y = x + e_i`, carries ten rishon modes `d^y_k = (η^y_{2k−1} + iη^y_{2k})/2` and `d^x_j = (η^x_{2j−1} + iη^x_{2j})/2`, with `η^y_a = η_a` and `η^x_b = η_{10+b}`. Its register is `S_+`, the `Γ = +1` half of their Fock space, `Γ = i^{10}η_1⋯η_{20}`. Since `iη_{2k−1}η_{2k} = 2n_k − 1 = −(−1)^{n_k}`, `Γ = (−1)^{N_{\rm rishon}}`, so `S_+` is the even-rishon-number half and contains the rishon vacuum `|0⟩_ℓ`. The hop is `h_ℓ = (i/2)Σ_{a,b}γ_{y,a}U^{ab}_ℓγ_{x,b}` with `U^{ab}_ℓ = iη^y_aη^x_b`; the electric layer is `W_E = ∏_ℓ e^{−iτ_EΓ^x_ℓ}`, `Γ^x_ℓ = i^5η^x_1⋯η^x_{10}`. The Gauss generators are `𝒢^{cd}_x = M^{cd}_x + Σ_{ℓ∋x}L^{cd}_{ℓ,x}`. By Theorem G they commute with every gate and give a representation of `K_x = Spin(10)` on site `x` and its six link ends.

**`L5-U[m]`.** Same sites. Link `ℓ = (x, y)` carries rishons `r^{ℓ,x}_k` (source end) and `r^{ℓ,y}_j` (target end), fermionic among themselves, commuting with matter, in the sector of total number `m ∈ {1, …, 9}`. Put `U^{jk}_ℓ = r^{ℓ,y}_jr^{ℓ,x†}_k`, `h^U_ℓ = Σ_{jk}c^†_{y,j}U^{jk}_ℓc_{x,k} + h.c.`, `p_{ℓ,z} = Σ_jr^{ℓ,z†}_jr^{ℓ,z}_j` for an end `z`, and `W_E = ∏_ℓe^{−iτ_E(p_{ℓ,x} − m/2)^2}`. The Gauss generators are `𝒢^T_x = Σc^†_xTc_x + Σ_{ℓ∋x}Σr^{ℓ,x†}Tr^{ℓ,x}`, `T ∈ u(5)`. By Theorem U they commute with every gate and give a representation of `K_x = U(5)`. Write `Q_x = N_x + Σ_{ℓ∋x}p_{ℓ,x}` for the generator of its centre.

**Common.** `H_C = 3^{−1/2}Σ_{ℓ=(x,x+e_i)⊂C}η_i(x)h_ℓ`, `M_e = ∏_{C∈𝒯_e}e^{−ia_eH_C}`, `M_o = ∏_{C∈𝒯_o}e^{ia_oH_C}`, base tick `U_0 = W_EM_oM_e`, tick automorphism `α(A) = U_0^*AU_0` on the quasi-local algebra `𝔄` (`LW1.md` E1; its proof uses only commuting finite gates). The free data are `ε, μ` with `0 ≤ μ < 2ε < π`, `τ_E ∈ R` (zero allowed), and `m`. The plaquette class is open law data (GA1-P-5). Every statement below is for `U_0` unless it says otherwise.

### 1.2 Gauge automorphisms and the gauge average

For a site `x` and `g ∈ K_x`, let `V_x(g) ∈ 𝔄` be the local unitary of Theorem G(iii) or Theorem U, and `α^G_{x,g} = Ad V_x(g)`. Unitaries at different sites commute: they share at most one link, where they act on different ends. Put `𝔄^G = {A ∈ 𝔄 : α^G_{x,g}(A) = A for all x, g}`. For a local `A`, only the finitely many sites `S(A)` at which `A` has matter or a link end can move it. Define
\[
E(A)=\int_{\prod_{x\in S(A)}K_x}\Big(\prod_{x\in S(A)}\alpha^G_{x,g_x}\Big)(A)\,\prod_x dg_x ,
\]
with normalized Haar measures.

**Lemma 1.1 (gauge average).**
(a) `E` extends to a positive, unital, linear contraction `𝔄 → 𝔄^G` with `E(A) = A` on `𝔄^G` and `E(BAC) = BE(A)C` for `B, C ∈ 𝔄^G`.
(b) Local elements of `𝔄^G` are dense in `𝔄^G`.
(c) A state `ω` is gauge invariant exactly when `ω = ω∘E`. Restriction is a bijection from gauge-invariant states of `𝔄` onto states of `𝔄^G`, with inverse `φ ↦ φ∘E`.
(d) `E∘α = α∘E`, and `E∘β_g = β_g∘E` for the lifts `β_g` of Lemma C.

*Proof.* (a) Adding to `S(A)` a site whose unitaries commute with `A` does not change the integral, since the integrand does not depend on that variable. So `E` is well defined on local elements. Each `α^G` is isometric, so `‖E(A)‖ ≤ ‖A‖`, and `E` extends by continuity. Left invariance of Haar measure gives `α^G_{x,h}(E(A)) = E(A)`. The bimodule identity holds because `α^G(BAC) = Bα^G(A)C` for invariant `B, C`. (b) Let `A ∈ 𝔄^G` and local `A_n → A`. Then `E(A_n)` is local and invariant, and `‖E(A_n) − A‖ ≤ sup_g‖α^G_g(A_n − A)‖ = ‖A_n − A‖`. (c) For invariant `ω` and local `A`, `ω(E(A)) = ∫ω(α^G_g(A))dg = ω(A)`: the integral is over a finite product of compact groups and `ω` is continuous. The converse holds since `E∘α^G_{x,h} = E`. Two invariant states that agree on `𝔄^G` agree everywhere, since `ω = ω∘E`. For a state `φ` of `𝔄^G`, `φ∘E` is a state because `E` is positive and unital. (d) Every gate commutes with every Gauss generator (Theorem G(i), Theorem U; `W_E` is a function of end parities or end numbers, which commute with the generators). So `α∘α^G = α^G∘α`, and `E(α(A)) = ∫α(α^G_g(A))dg = α(E(A))`, integrating over the sites relevant to `α(A)`, which contain those relevant to `A`. For `β_g`, Lemma C(iii) gives `β_g∘α^G_{x,h}∘β_g^{-1} = α^G_{gx,h}`, and Haar measure on a finite product does not change when its factors are relabelled. ∎

### 1.3 The symmetry lifts

**Lemma C (cell covariance of both laws).** For every `g ∈ 𝒢` there is an automorphism `β_g` of `𝔄` such that:
(i) `β_g` maps the algebra of site `x` onto that of `gx` and the register of `ℓ` onto that of `gℓ`, and `β_g∘α = α∘β_g`;
(ii) on `L5-U`, `β_g(c_{x,j}) = d_g(gx)c_{gx,j}` and `β_g(r^{ℓ,z}_j) = r^{gℓ,gz}_j` for each end `z` of `ℓ`, with a sign function `d_g`; on `L5-O`, `β_g` is the lift of B1-5;
(iii) `β_g` maps every Gauss generator at `x` to the same generator at `gx`; on `L5-U` it maps `N_x ↦ N_{gx}`, `Q_x ↦ Q_{gx}` and `p_{ℓ,z} ↦ p_{gℓ,gz}`;
(iv) `β_g∘β_{g'} = σ∘β_{gg'}`, where `σ` multiplies each site's odd generators by a sign that depends on the site only, and fixes every register.

*Proof for `L5-U`* (the analogue of B1-5, which `LW1_5U_DRAFT.md` lines 157 and 303 record as not proved). The maps in (ii) permute matter modes with signs and map the ten rishon modes of `ℓ` onto those of `gℓ`, end to end. Each is a Bogoliubov map of a CAR algebra; on a link it preserves the rishon number, so it restricts to the sector `m`. Links are ordinary tensor factors that commute with matter, so these maps define one automorphism. *Hop.* `β_g(h^U_ℓ) = d_g(gx)d_g(gy)Σ_{jk}c^†_{gy,j}r^{gℓ,gy}_jr^{gℓ,gx†}_kc_{gx,k} + h.c.` If `gx` is the source of `gℓ`, the sum is the first term of `h^U_{gℓ}`. If `gx` is its target, write `gℓ = (x', y')` with `x' = gy`. The first term of `h^U_{gℓ}` is `Σc^†_{y',j}r^{y'}_jr^{x'†}_kc_{x',k}`, and its adjoint is `Σc^†_{x',k}r^{x'}_kr^{y'†}_jc_{y',j}`, because rishons commute with matter. That adjoint is the mapped sum. So in both cases `β_g(h^U_ℓ) = d_g(gx)d_g(gy)h^U_{gℓ}`. *Signs.* `LW1.md` A2's proof: "Therefore the ratio on an edge \((x,y)\) is \(d(x)d(y)\). The signed permutation \(D_dP_Q\) consequently fixes both \(R_e,R_o\)". That is the identity `d(gx)d(gy)η_i(x) = η_{i'}(x')` on every cube link, for the image link `(x', x' + e_{i'})`. Even translations need `d = 1`. So `β_g(H_C) = H_{gC}`. `𝒢` preserves each tiling (A2), so `β_g` commutes with `Ad M_e` and `Ad M_o`. *Electric layer.* If `gx` is the target of `gℓ`, `p_{gℓ,gx} = m − p_{gℓ,x'}` on the register, and `(m − p − m/2)^2 = (p − m/2)^2`. So `β_g(W_E) = W_E`, and (i) follows. (iii) Signs cancel in `c^†Tc`, and the six links at `x` go to the six links at `gx`, end to end. (iv) The rishon maps compose exactly, and the matter maps compose up to the product of two sign functions. ∎

*For `L5-O`.* `LW1_5_DRAFT.md` line 392, B1-5: "If it reverses a link, use on that register the lift of the swap `s: η_a ↔ η_{10+a}`. ... A2's sign correction `d(x)` is implemented on matter by `Ad P_x`". (iii): `Ad P_x` fixes the even `M^{cd}_x`, and `s` maps `L_y^{cd} = T_{cd}` to `T_{10+c,10+d} = L_x^{cd}`. (iv) as for `L5-U`; `σ` is a product of `Ad P_x`'s, and a lift of `s` is fixed up to a sign, which `Ad` removes.

Every state below is invariant under every sign automorphism `σ` of (iv), so invariance under one lift of `g` is invariance under all of them.

**Lemma S2′ (reversals, stabilizers, cubes).**
(a) Every link `ℓ = (x, x + e_i)` is mapped onto itself, with its ends exchanged, by some `r_ℓ ∈ 𝒢`. The linear part of `r_ℓ` permutes the coordinate axes by a transposition.
(b) `𝒢` acts transitively on sites. The stabilizer of `x` is cyclic of order 3, generated by the turn `h_x` about the line through `x` and the centre of its even cube. `h_x` permutes the three even-cube links at `x` in one 3-cycle and the three odd-cube links at `x` in another.
(c) The stabilizer in `𝒢` of a cube of either tiling contains the 24 rotations about its centre, and they act transitively on its corners.

*Proof.* (a) `LW1_5O_DRAFT.md` Lemma S2(i), checked here. For `i = 1` and `x_2 ≡ x_3 (mod 2)`, take `Q(y) = (−y_1, y_3, y_2)` (determinant 1) and `t = (x_1, (x_2 − x_3)/2, (x_3 − x_2)/2)`; then `Q(x − c_0) + c_0 + 2t = x + e_1` and `x + e_1 ↦ x`. For `x_2 ≢ x_3`, take `Q(y) = (−y_1, −y_3, −y_2)` and `t = (x_1, (x_2 + x_3 − 1)/2, (x_2 + x_3 − 1)/2)`. Both `Q` swap axes 2 and 3. Other directions follow by conjugating with a cyclic permutation of the axes. (b) `LW1.md` A2: "The action on sites is transitive; a site's stabilizer has three elements", and "its stabilizer consists of the identity and the two turns about that body diagonal." Write `s_i = ±1` for the direction of `x`'s even-cube link along `e_i`. Its even cube has centre `x + s/2` and its odd cube has centre `x − s/2`. Both lie on the turning line, so the turn fixes both cubes and cycles `x`'s three neighbours in each. (c) Rotations about an even centre `b + c_0`, `b ∈ 2Z^3`, are `O_{c_0}` conjugated by a translation in `2Z^3`. About an odd centre, `y ↦ Q(y − c_0 − 1 − b) + c_0 + 1 + b` equals `Q(y − c_0) + c_0 + (1 + b − Q(1 + b))`, and `1 − Q1 ∈ {0, 2}^3` and `b − Qb ∈ 2Z^3`. The quarter turns about the three axes through the centre move any corner to any other. ∎

[check] `check_pairs.py`: on the sampled box every link is reversed by an element of `𝒢`, and the stabilizer of `0` has 3 elements.

### 1.4 Two readings of (iv), and the four tests

**Reading E.** `ω` is an extreme point of the convex set `𝒮_K` of states invariant under the group `K` of automorphisms generated by `α`, all `α^G_{x,g}` and all `β_g`.

**Reading P.** The restriction `ω|𝔄^G` is a pure state of `𝔄^G`.

**Lemma R.** For a gauge-invariant state `ω` the following are equivalent: (a) `ω|𝔄^G` is pure; (b) `ω` is extremal among gauge-invariant states. If they hold and `ω ∈ 𝒮_K`, then `ω` is extremal in `𝒮_K`. So P implies E.

*Proof.* (a) ⇒ (b): if `ω = λω_1 + (1 − λ)ω_2` with gauge-invariant `ω_i` and `0 < λ < 1`, restrict to `𝔄^G`; purity gives `ω_1|𝔄^G = ω|𝔄^G`, and Lemma 1.1(c) gives `ω_1 = ω`. (b) ⇒ (a): if `ω|𝔄^G = λφ_1 + (1 − λ)φ_2`, then `ω = ω∘E = λφ_1∘E + (1 − λ)φ_2∘E` with gauge-invariant terms, so `φ_1∘E = ω` and `φ_1 = ω|𝔄^G`. Last claim: `𝒮_K` lies inside the gauge-invariant states, so a decomposition in `𝒮_K` is one among gauge-invariant states. ∎

So "extremal under the relevant symmetry group" covers both readings. With the local gauge group alone it is P. With the whole group `K` it is E.

**Reading F, for comparison only.** `LW1U_DRAFT.md` and the owner decision "Non-factor states: held" (`TOE_ASSEMBLY.md` section 3.3) use "factor state" in the von Neumann sense: `π_ω(𝔄)''` is a factor. PS-3 selects one transport only at such states. This draft proves nothing under F. Remark 3.1 says what holds for the witnesses.

| Reading | (1) states or fixes a part's target | (2) open-ended | (3) settles a downstream question by premise | (4) adds structure | Result |
|---|---|---|---|---|---|
| E | pass: VC1's text has no extremality clause, and E fixes no state or filling | pass: `K` is generated by the law's own maps | pass: under E the filling of `L5-U` stays free (Theorem U1) | pass: nothing beyond the law | passes; weak: the tracial state meets it and forms no records; it is not F (`LW1U_DRAFT.md` Theorem 4.3 is an ergodic non-factor state) |
| P | pass: it fixes no state | pass | conditional: on `L5-U` and `L_cube` it decides the half-filling reading LW1-5U-PS7 in the negative (Theorem U2); on `L5-O` it decides nothing (Lemma H) | pass: it uses only `LW1.md` line 47 and the law's Gauss law | passes 1, 2, 4; 3 conditional, disclosed |

Neither reading is proposed. Sections 3-5 answer the target under each.

---

## 2. Five general lemmas

A positive functional `φ` on a unital C*-algebra `𝔅` is *below* a state `ψ` if `ψ − φ` is positive. `ψ` is pure exactly when every positive functional below it is a multiple of it. This is the definition used throughout.

**Lemma 2.1 (central elements are sharp in pure states).** Let `ψ` be a pure state of `𝔅` and `z` a self-adjoint element of the centre of `𝔅`. Then `ψ(za) = ψ(z)ψ(a)` for all `a`, and `ψ((z − ψ(z))^2) = 0`.

*Proof.* Rescale so that `0 ≤ z ≤ 1`. The square root `z^{1/2}` lies in the C*-algebra generated by `z`, so it is central. Then `ψ(za^*a) = ψ((az^{1/2})^*(az^{1/2})) ≥ 0`, and likewise with `1 − z`. So `a ↦ ψ(za)` is a positive functional below `ψ`, hence `ψ(za) = tψ(a)` with `t = ψ(z)`. Put `a = z`. ∎

**Lemma 2.2 (purity on invariants from a lowest joint eigenvector).** Let a compact group `K` act unitarily on a finite-dimensional space `W` by `π`. Let `H_1, …, H_r` be self-adjoint operators on `W` that commute with every element of `π(K)' = End(W)^K`; generators of one-parameter subgroups of `π(K)` qualify. Suppose a unit vector `u` spans the joint eigenspace `{w : H_iw = λ_iw for all i}`. Then the vector state `X ↦ ⟨u, Xu⟩` is pure on `End(W)^K`. If `K = ∏_{x∈S}K_x` acts factorwise on `W = ⊗_{x∈S}W_x`, and each `u_x` spans the joint eigenspace of commuting operators `H_{x,i}` on `W_x`, then `u = ⊗_xu_x` spans the joint eigenspace of all `H_{x,i} ⊗ 1`, so the same conclusion holds.

*Proof.* Let `K_u` be the span of `π(K)u`. *Irreducible.* Suppose `K_u = A ⊕ B` with `A, B` orthogonal and invariant. The orthogonal projection `Π_A` onto `A` commutes with `π(K)`, since `A` and `A^⊥` are invariant. So it commutes with every `H_i` and maps the joint eigenspace `Cu` into itself: `Π_Au = cu` with `c ∈ {0, 1}`. If `c = 1`, `u ∈ A`, so `K_u ⊂ A` and `B = 0`. If `c = 0`, `u ∈ K_u ∩ A^⊥ = B`, so `A = 0`. *Schur.* Let `P` be the projection onto `K_u`; it lies in `End(W)^K`. For `X ∈ End(W)^K`, `PXP` restricted to `K_u` commutes with `π(K)`. If it is self-adjoint, its eigenspaces in `K_u` are invariant, so it has one eigenvalue. Splitting into self-adjoint parts, `PXP = c(X)P`. *Purity.* Let `φ` be below the vector state `ω_u` on `End(W)^K`. Then `0 ≤ φ(1 − P) ≤ ω_u(1 − P) = 0`. Cauchy-Schwarz gives `φ(X) = φ(PXP) = c(X)φ(1)`, while `ω_u(X) = ⟨u, PXPu⟩ = c(X)`. So `φ = φ(1)ω_u`. *Products.* Decompose each `W_x` into the joint eigenspaces of the `H_{x,·}`. Then `W = ⊕ ⊗_xW_x^{(λ_x)}`, and the joint eigenspace for the values `(λ_x)_x` is `⊗_xW_x^{(λ_x)} = C⊗_xu_x`. ∎

**Lemma 2.3 (sector lemma: purity at infinite volume).** Let `𝔅 ⊂ 𝔄` be a C*-subalgebra in which local elements are dense, and `Φ` a state of `𝔄`. Suppose that for every local `A ∈ 𝔅` there are a projection `P ∈ 𝔅` with `Φ(P) = 1` and a C*-subalgebra `𝒞 ⊂ 𝔅` with unit `P`, such that `PAP ∈ 𝒞` and `Φ|𝒞` is a pure state of `𝒞`. Then `Φ|𝔅` is pure.

*Proof.* Let `φ` be below `Φ|𝔅`. Fix a local `A ∈ 𝔅` and take `P`, `𝒞`. `0 ≤ φ(1 − P) ≤ Φ(1 − P) = 0`, so Cauchy-Schwarz gives `φ(A) = φ(PAP)`. `φ|𝒞` is below `Φ|𝒞`, which is pure, so `φ|𝒞 = φ(P)Φ|𝒞 = φ(1)Φ|𝒞`. Hence `φ(A) = φ(1)Φ(PAP) = φ(1)Φ(A)`. Both sides are continuous in `A`, and local elements are dense. ∎

**Lemma 2.4 (the tracial state; products are extremal).**
(a) The normalized traces of the finite matter-and-link algebras form one state `τ` of `𝔄`, and `τ∘β = τ` for every automorphism `β` that maps each local algebra into a local algebra.
(b) Call `ω` a *product state* over a partition of the sites and links into blocks of bounded diameter if `ω(AB) = ω(A)ω(B)` whenever `A` and `B` lie in the algebras of disjoint unions of blocks. If `ω` is a product state over a `2Z^3`-invariant partition and `ω` is `2Z^3`-invariant, then `ω` is extremal among `2Z^3`-invariant states. So if moreover `ω ∈ 𝒮_K`, `ω` is extremal in `𝒮_K`.

*Proof.* (a) The traces are consistent under inclusion. For a local algebra `𝔄_F`, `A ↦ τ(β(A))` is a tracial state of the full matrix algebra `𝔄_F`. A tracial functional on `M_n` vanishes on the commutators `E_{ij} = [E_{ik}, E_{kj}]` (`i ≠ j`) and `E_{ii} − E_{jj} = [E_{ij}, E_{ji}]`, so it is a multiple of the trace. So `τ∘β = τ` on `𝔄_F`, and by continuity on `𝔄`. (b) Let `A` be local and `A_n = n^{−3}Σ_{t∈\{0,…,n−1\}^3}τ_{2t}(A)`, with `τ_{2t}` the cell translations. Put `D_n = A_n − ω(A)`. In `ω(D_n^*D_n) = n^{−6}Σ_{s,t}[ω(τ_{2s}(A)^*τ_{2t}(A)) − |ω(A)|^2]`, a term vanishes when the blocks met by `τ_{2s}(A)` and by `τ_{2t}(A)` are disjoint, which holds for all but at most `Cn^3` pairs. Each term is at most `2‖A‖^2`. So `ω(D_n^*D_n) → 0`. Let `ω = λω_1 + (1 − λ)ω_2` with `2Z^3`-invariant states and `0 < λ < 1`. Then `ω_1 ≤ ω/λ`, and `|ω_1(A) − ω(A)|^2 = |ω_1(D_n)|^2 ≤ ω_1(D_n^*D_n) ≤ ω(D_n^*D_n)/λ → 0`. So `ω_1 = ω` on local elements, hence everywhere. The last claim holds because `𝒮_K` lies inside the `2Z^3`-invariant states. ∎

**Lemma 2.5 (a macroscopic two-valued variable rules out purity).** Let `𝔅 ⊂ 𝔄` be a C*-subalgebra in which local elements are dense, and `ω` a state. Suppose there are local projections `P_i ∈ 𝔅`, `i ∈ N`, such that each local `A ∈ 𝔅` commutes with `P_i` for all large `i`, `ω((P_i − P_0)^2) = 0` for all `i`, and `0 < ω(P_0) < 1`. Then `ω|𝔅` is not pure.

*Proof.* `(X + Y)^2 ≤ 2X^2 + 2Y^2` for self-adjoint `X, Y` gives `ω((P_i − P_j)^2) = 0` for all `i, j`. For local `A ∈ 𝔅`, put `φ(A) = ω(P_iA)` with `i` so large that `[P_i, A] = 0`. By Cauchy-Schwarz this does not depend on `i`. `φ(A^*A) = ω((P_iA)^*(P_iA)) ≥ 0` and `ω(A^*A) − φ(A^*A) = ω(((1 − P_i)A)^*((1 − P_i)A)) ≥ 0`. So `φ` extends to a positive functional below `ω|𝔅`, with `φ(1) = ω(P_0)`. But `φ(P_0) = ω(P_iP_0) = ω(P_0)`, while `φ(1)ω(P_0) = ω(P_0)^2 ≠ ω(P_0)`. So `φ` is not a multiple of `ω|𝔅`. ∎

A standard example of the mechanism: the vector states `2^{−1/2}(|0⋯0⟩ + |1⋯1⟩)` of `n` qubits converge locally to the mixture of the two product states, which is not pure by Lemma 2.5. So a weak-* limit of pure states need not be pure. Section 4.5 uses this.

---

## 3. `L5-O[S_+]`: a gauged vacuum exists under both readings

**Theorem O1 (reading E: the tracial state).** The tracial state `τ` of `L5-O[S_+]` is stationary, gauge invariant, invariant under every lift `β_g`, and extremal in `𝒮_K`. Its filling is `τ(N_x) = 5/2`.

*Proof.* `α`, every `α^G_{x,g}` and every `β_g` map local algebras into local algebras, so Lemma 2.4(a) gives invariance. `τ` is a product state over single sites and single links, and it is `2Z^3`-invariant, so Lemma 2.4(b) gives extremality. `τ(n_{x,j}) = 1/2`. ∎

E2b-5 already gives existence of stationary gauge-invariant states (`LW1_5_DRAFT.md` line 416). Theorem O1 adds the extremality of reading E. In `τ` the site parities are independent fair signs, so `τ((1 − P_xP_y)/2) = 1/2` and no record forms under PS-3c, as `LW1.md` line 500 says for `L_cube`'s tracial state.

**Theorem O2 (reading P: the gauge-averaged dark state).** Let `Φ_0` be the product state with the matter Fock vacuum at every site and the rishon vacuum `|0⟩_ℓ ∈ S_+` on every link. Put `ω_0 = Φ_0∘E`. Then `ω_0` is
(i) stationary under the base tick, for every `ε, μ, τ_E` in the window;
(ii) invariant under every local gauge automorphism;
(iii) invariant under every lift `β_g`, `g ∈ 𝒢`;
(iv) pure on `𝔄^G`, hence extremal among gauge-invariant states and extremal in `𝒮_K` (Lemma R).
Its filling is `ω_0(n_{x,j}) = 1/2` for every mode in every frame, so `ω_0(N_x) = 5/2`.

*Proof.* By Lemma 1.1, (i)-(iii) and (iv) for `ω_0` follow from three facts about `Φ_0`: `Φ_0∘α = Φ_0`, `Φ_0∘β_g = Φ_0`, and `Φ_0|𝔄^G` pure. Indeed `ω_0` is gauge invariant by Lemma 1.1(c); `ω_0∘α = Φ_0∘α∘E = ω_0` and `ω_0∘β_g = Φ_0∘β_g∘E = ω_0` by Lemma 1.1(d); and `ω_0|𝔄^G = Φ_0|𝔄^G` since `E` is the identity on `𝔄^G`. The filling is Lemma H (`LW1_5_DRAFT.md` line 246), which needs only gauge invariance at `x`.

*Stationary.* This is B8b-5(ii); here is the computation. `γ_{x,2j−1}|∅⟩ = c^†_{x,j}|∅⟩` and `γ_{x,2j}|∅⟩ = ic^†_{x,j}|∅⟩`. Moving `γ_{y,a}` past `c^†_{x,j}` costs a sign. So
\[
h_\ell\big(|\varnothing\rangle\otimes|0\rangle_\ell\big)=-\tfrac i2\sum_{j,k}c^\dagger_{x,j}c^\dagger_{y,k}|\varnothing\rangle\otimes\mathcal U^{++}_{kj}|0\rangle_\ell,\qquad
\mathcal U^{++}_{kj}=U^{2k-1,2j-1}+iU^{2k-1,2j}+iU^{2k,2j-1}-U^{2k,2j}=4i\,d^y_kd^x_j ,
\]
where the last identity is the expansion of `(η^y_{2k−1} + iη^y_{2k})(η^x_{2j−1} + iη^x_{2j})`. The rishon annihilator `d^x_j` kills `|0⟩_ℓ`. So `H_C` kills every vector with empty matter on `C` and rishon vacuum on `C`'s links, and `e^{iaH_C}` fixes it. `Γ^x_ℓ = ∏_{k}(iη^x_{2k−1}η^x_{2k}) = ∏_k(2n^x_k − 1)` equals `−1` on `|0⟩_ℓ`, so `W_E` multiplies such vectors by a phase. For a local `A`, `α(A) = U_F^*AU_F` with `U_F` a finite product of these gates (`LW1.md` E1). On a finite region that contains their supports, `Φ_0` is the vector state of the local vacuum `ψ`, and `U_Fψ` is a phase times `ψ`. So `Φ_0(α(A)) = Φ_0(A)`.

*Symmetric.* `β_g` maps each `γ_{x,a}` to `±γ_{gx,a}`, so it maps matter vacuum to matter vacuum. On a link it is a relabelling or `Ad V_s`, where `V_s` implements `s: η_a ↔ η_{10+a}`. Then `V_sd^y_kV_s^* = d^x_k` and `V_sd^x_kV_s^* = d^y_k`, so `V_s|0⟩` is killed by every rishon annihilator and is a multiple of `|0⟩`.

*Pure on `𝔄^G`.* Use Lemma 2.3 with `𝔅 = 𝔄^G` (local elements are dense by Lemma 1.1(b)). For a finite site set `S`, let `L(S)` be the links with an end in `S`, and
\[
P_S=\prod_{x\in S}\tfrac12(1+P_x)\prod_{\ell\in L(S)}\tfrac12\big(1+(-1)^{N^{x}_\ell}\big),
\]
with `N^x_ℓ` the rishon number at the source end. On `S_+` the two end parities agree, so the second factor projects onto even parity at both ends. `P_x` commutes with the even `M^{cd}_x`, and `(−1)^{N^x_ℓ} = −Γ^x_ℓ` commutes with both ends' generators (`LW1_5_DRAFT.md` section 8.1, item 6). So `P_S ∈ 𝔄^G`, and `Φ_0(P_S) = 1`. The range of `P_S` is
\[
\mathcal H^{\rm sec}_S=\bigotimes_{x\in S}W_x\otimes\bigotimes_{\text{outer ends}}H_+,\qquad
W_x=H_+(x)\otimes\bigotimes_{\ell\ni x}H^{\ell,x}_+ ,
\]
with `H_+(x)` the even part of the site's Fock space and `H^{ℓ,z}_+` the even part of the Fock space of the five rishon modes at end `z`. With both end parities even, the graded product of the two ends is an ordinary tensor product. `Spin(10)_x`, `x ∈ S`, acts on `𝓗^{sec}_S` through `W_x` only. Let `A ∈ 𝔄^G` be local and take `S` to contain its sites and both ends of each of its links. Then `P_SAP_S = P_S(Y ⊗ 1)P_S` with `Y ∈ End(W_S)`, `W_S = ⊗_{x∈S}W_x`, and `Y` commutes with `∏_{x∈S}Spin(10)_x`. Let `𝒞_S` be the set of all such `P_S(Y ⊗ 1)P_S` with `Y ∈ End(W_S)^{∏Spin(10)_x}`. It is a C*-algebra with unit `P_S`. Its elements are local and commute with every gauge unitary: at `x ∈ S` because `Y` does, and at `x ∉ S` because those act only on outer ends, where the element is `P_S` times the identity. So `𝒞_S ⊂ 𝔄^G`. `Φ_0` restricted to `𝒞_S` is the vector state of `u_S = ⊗_{x∈S}u_x`, `u_x = |∅⟩_x ⊗ ⊗_{ℓ∋x}|0⟩_{ℓ,x}`. Apply Lemma 2.2 with the Cartan generators
\[
H_{x,j}=\mathcal G^{2j-1,2j}_x\big|_{W_x}=\big(n_{x,j}-\tfrac12\big)+\sum_{\ell\ni x}\big(n^{\ell,x}_j-\tfrac12\big),\qquad j=1,\dots,5 ,
\]
which generate one-parameter subgroups of `Spin(10)_x`. The joint eigenvalue `−7/2` for all `j` forces all seven number operators of each flavour at `x` to vanish, so the joint eigenspace is `Cu_x`. So `Φ_0|𝒞_S` is pure, and Lemma 2.3 gives purity of `Φ_0|𝔄^G`. ∎

**Remark O2.1 (a second witness; no uniqueness).** Let `Φ'_0` have full matter at every site and all ten rishon modes occupied on every link (rishon number 10, so the state lies in `S_+`). Then `γ_{x,2j−1}|F⟩ = c_{x,j}|F⟩` and `γ_{x,2j}|F⟩ = −ic_{x,j}|F⟩` for the full vector `|F⟩`, and the same computation gives `h_ℓ|F⟩ = −(i/2)Σc_{x,j}c_{y,k}|F⟩ ⊗ 𝒰^{−−}_{kj}|F⟩_ℓ` with `𝒰^{−−}_{kj} = 4i d^{y†}_kd^{x†}_j`, which kills the full rishon state. `Γ^x_ℓ = +1` there. The proof of Theorem O2 runs with odd parity in place of even in `P_S`, and with the joint eigenvalue `+7/2`. So `ω'_0 = Φ'_0∘E` also meets (i)-(iv) under both readings. In `ω_0` every `P_x = +1`; in `ω'_0` every `P_x = −1`; and `P_x ∈ 𝔄^G`. So `ω_0 ≠ ω'_0`: conditions (i)-(iv) do not select one vacuum on `L5-O`.

**Corollary O3 (records in `ω_0`; under PS-3c and the proposed reading PS-3h5).** In `ω_0` every site parity equals `+1` with probability one at every tick. If actual values are site parities (PS-3h5, `LW1_5_DRAFT.md` section 8.2, not in the working set), then under PS-3c every site's actual value is copied into all six neighbours at tick 1, and a record forms at every site at the end of tick 1, with value `+1`.

*Proof.* `ω_0(P_x) = Φ_0(P_x) = 1` because `P_x ∈ 𝔄^G`, and `ω_0` is stationary. Then `ω_0((1 − P_xP_y)/2) = 0` for every pair, which is PS-3c's "probability one that their actual values agree", read with the joint Born rule of `LW1.md` inferred definition 26. ∎

So for this witness VC1(4) has an answer: records form at once, everywhere, and the record pattern carries no information. This is the opposite of the free sea and of `τ`, where no record forms.

**Remark 3.1 (reading F, not used).** `τ` is a product state over sites and links. `ω_0` and `ω'_0` cluster exactly: if the gauge sites `S(A)` and `S(B)` are disjoint, then `E(AB) = E(A)E(B)`, and `Φ_0` is a product state. By Powers' criterion (credited above, not rebuilt), each would be a factor state, so PS-3's single-transport domain would contain them. Nothing here depends on it.

**Scope of Section 3.** (a) The register is `S_+`. With `S_−` the rishon vacuum is not in the register, and this case is not treated. (b) A plaquette class: `τ` stays stationary under any added local automorphism (Lemma 2.4(a)). `ω_0` need not: a plaquette monomial contains a `U^{ab}` on each of four links, and `U^{ab}|0⟩ ≠ 0`. So with a plaquette class, P-existence on `L5-O` is open. (c) `ω_0` carries the spinor-class Gauss charge `z_x = −1` at every site, as every state of one-class `L5-O` does (`LW1_5O_DRAFT.md` Theorem K); LW1-5-BG is unchanged.

---

## 4. `L5-U[m]`

### 4.1 Link reversal fixes the mean end number

**Lemma 4.0.** Let `ω` be a state of `L5-U[m]` invariant under `β_{r_ℓ}` for a reversal `r_ℓ` of the link `ℓ = (x, y)` (Lemma S2′(a)).
(a) `ω(f(p_{ℓ,x})) = ω(f(m − p_{ℓ,x}))` for every function `f`. In particular `ω(p_{ℓ,x}) = ω(p_{ℓ,y}) = m/2`.
(b) If `m` is odd, `p_{ℓ,x}` is not sharp in `ω`, and `ω((−1)^{p_{ℓ,x}}) = 0`.
(c) If `ω(p_{ℓ,x}p_{ℓ,y}) = ω(p_{ℓ,x})ω(p_{ℓ,y})`, then `p_{ℓ,x}` is sharp. So for odd `m`, no state that factorizes across the two ends of `ℓ` is invariant under `β_{r_ℓ}`.

*Proof.* (a) Lemma C(iii) gives `β_{r_ℓ}(p_{ℓ,x}) = p_{ℓ,y}`, and `p_{ℓ,y} = m − p_{ℓ,x}` on the register. (b) A sharp value is an eigenvalue, an integer `c`, and (a) forces `c = m − c`. Also `(−1)^{m−p} = −(−1)^p` for odd `m`. (c) With `p_{ℓ,y} = m − p_{ℓ,x}`, the hypothesis reads `ω(p(m − p)) = ω(p)(m − ω(p))`, that is `ω(p^2) = ω(p)^2`. Then use (b). ∎

### 4.2 Reading E: every filling

**Theorem U1.** For `t ∈ [−∞, ∞]`, let `ω_t` be the product state with density `e^{−tN_x}/Z_t` on each site (matter vacuum at `t = +∞`, full matter at `t = −∞`) and the normalized trace on each register. Then `ω_t` is stationary under the base tick and under the base tick followed by any finite-depth layer of local link-only gauge-invariant gates. It is gauge invariant, invariant under every `β_g`, and extremal in `𝒮_K`. Its filling is `5/(e^t + 1)`, which takes every value in `[0, 5]`.

*Proof.* On a finite region `F`, `ω_t` has density proportional to `e^{−tN_F} ⊗ 1`. A cube gate commutes with the matter number of its cube, since each hop term moves one particle between two of its sites, and it acts on nothing else; so it commutes with `e^{−tN_F} ⊗ 1` and leaves the density unchanged. `W_E` and link-only gates commute with matter, and the link part is a multiple of the identity. `V_x(g)` acts on the site as `Γ(g)`, which commutes with `N_x`, and on registers by unitaries, which fix traces. `β_g` maps `N_x` to `N_{gx}` and traces to traces. `ω_t` is a `2Z^3`-invariant product over sites and links, so Lemma 2.4(b) gives extremality. `ω_t(n_{x,j}) = e^{−t}/(1 + e^{−t})` for each of the five modes. ∎

### 4.3 Reading P: the filling is an integer

**Theorem U2 (filling of Gauss-sharp symmetric states, infinite volume).** Let `ω` be a state of `L5-U[m]`, for any `m`, any value of the constants and any plaquette class. Suppose `ω` is invariant under `β_{r_ℓ}` for a reversal of each of the six links at `x`, and `ω((Q_x − q_x)^2) = 0`. Then `q_x ∈ Z` and `ω(N_x) = q_x − 3m`. If `ω` is invariant under every `β_g` and sharp in every `Q_x`, then `q_x = q` for all `x`, and `ω(N_x) = q − 3m ∈ {0, 1, …, 5}`. Every gauge-invariant state that is pure on `𝔄^G` is sharp in every `Q_x`. So no state of `L5-U` with (iii) and (iv-P) is half filled.

*Proof.* Lemma 4.0(a) gives `ω(p_{ℓ,x}) = m/2` for each link at `x`, so `ω(Q_x) = ω(N_x) + 3m`. `Q_x` has finite integer spectrum and `(Q_x − q)^2 ≥ dist(q, spec Q_x)^2`, so sharpness gives `q_x ∈ spec Q_x ⊂ Z`. Invariance gives `ω((Q_{gx} − q_x)^2) = ω(β_g((Q_x − q_x)^2)) = 0`, so `q_{gx} = q_x`, and `𝒢` is transitive. Then `0 ≤ ω(N_x) ≤ 5` bounds `q − 3m`. For the last claim: `Q_x` commutes with every gauge unitary (it generates the centre of `U(5)_x`, and at `y ≠ x` the generators act on other modes or on the other end of a shared link), so `Q_x ∈ 𝔄^G`. For `A ∈ 𝔄^G`, `e^{iθQ_x}Ae^{−iθQ_x} = A`, so `[Q_x, A] = 0`, first for local `A` by differentiation and then by continuity. So `Q_x` is central in `𝔄^G`, and Lemma 2.1 applies. ∎

This is the infinite-volume form of Theorem F-U that `LW1_5U_DRAFT.md` line 304 lists as open. The box sum (1.1) there is replaced by Lemma 4.0. No dynamics, no purity on `𝔄` and no box enter.

**Corollary U2′ (`L_cube`).** For `L_cube` with any link spin `S` and any plaquette layer, a state that is invariant under the link reversals of `𝒢` and sharp in every `𝒢_x` has `ω(n_x) ∈ {0, 1}`. So no state of `L_cube` that is invariant under `𝒢` and pure on its gauge-invariant algebra is half filled.

*Proof.* `LW1.md`, gauged covariance B1/B1q: "If it reverses an oriented link, conjugation by the spin rotation \(e^{-i\pi S^x}\) sends \(E\) to \(-E\)". So reversal invariance gives `ω(E_ℓ) = 0` and `ω(𝒢_x) = ω(n_x)`. Each site has three outgoing and three incoming links and `E ∈ S + Z`, so `𝒢_x = n_x + Σ_{out}E − Σ_{in}E` has integer spectrum. Sharpness then gives an integer in `[0, 1]`. `𝒢_x` is central in the gauge-invariant algebra by the argument of Theorem U2, so Lemma 2.1 gives sharpness for pure states. ∎

### 4.4 Reading P for even `m`: dark witnesses at fillings 0 and 5

**Theorem U3.** Let `m = 2k` be even. Let `Φ_m` be the product state with the matter vacuum at every site and, on every link `ℓ = (x, y)`, the register vector
\[
e_\ell=r^{\ell,x\dagger}_1\cdots r^{\ell,x\dagger}_k\,r^{\ell,y\dagger}_1\cdots r^{\ell,y\dagger}_k|0\rangle ,
\]
with flavours `1, …, k` occupied at both ends. Put `ω_m = Φ_m∘E`. Then `ω_m` is (i) stationary under the base tick for every `ε, μ, τ_E`; (ii) gauge invariant; (iii) invariant under every `β_g`; (iv) pure on `𝔄^G`, hence extremal in `𝒮_K`. `Q_x = 3m` is sharp, and the filling is `ω_m(N_x) = 0`. With full matter in place of the vacuum the same holds with `Q_x = 5 + 3m` and filling `5`.

*Proof.* As in Theorem O2, Lemma 1.1 reduces everything to three facts about `Φ_m`. *Stationary.* Each term of `h^U_ℓ` has `c_{x,k}` or `c_{y,j}` on the right: the adjoint term is `c^†_xU^†c_y`. So `H_C` kills every vector with empty matter on `C`, and `e^{iaH_C}` fixes it. On `e_ℓ`, `p_{ℓ,x} = k = m/2`, so `W_E` acts as the identity. For full matter, `c^†_{y,j}` and `c^†_{x,k}` kill full sites instead. Then argue as in Theorem O2. *Symmetric.* `β_g` maps the matter vacuum to itself and maps `e_ℓ` to `±e_{gℓ}`, since it relabels the occupied modes `{1, …, k}` at each end onto the same set at the image ends. *Pure on `𝔄^G`.* Use Lemma 2.3 with
\[
P_S=\prod_{x\in S}\Pi[N_x=0]\prod_{\ell\in L(S)}\Pi[p_{\ell,\rm src}=k],
\]
a product of spectral projections of the gauge-invariant operators `N_x` and `p_{ℓ,z}`; on the register, `p_{ℓ,src} = k` if and only if `p_{ℓ,tgt} = k`. The range of `P_S` is `⊗_{x∈S}W_x ⊗ ⊗_{outer ends}Λ^k`, with `W_x = ⊗_{ℓ∋x}Λ^k(C^5_{ℓ,x})`. With definite parities at both ends, the graded product of the two ends of a register is an ordinary tensor product, up to a fixed sign convention. `U(5)_x` acts through `W_x` only, by the same `Γ(u)` on each of the six factors (`LW1_5U_DRAFT.md` section 1.1: "`e^{i𝒢^T_x}` acts as `Γ(e^{iT})` on the matter at `x` and as the same `Γ(e^{iT})` on each of the six `x`-ends"). Define `𝒞_S` as in Theorem O2. `Φ_m` restricted to `𝒞_S` is the vector state of `⊗_xu_x`, `u_x = ⊗_{ℓ∋x}e_{1…k}`. In Lemma 2.2 take `H_{x,j} = 𝒢^{E_{jj}}_x|_{W_x} = Σ_{ℓ∋x}n^{ℓ,x}_j`. Each end holds exactly `k` rishons, at most one of each flavour. So the joint eigenvalue `6` for every `j ≤ k` forces every end to hold flavours `1, …, k`: the joint eigenspace is `Cu_x`. For full matter use `H_{x,j} = 1 + Σ_{ℓ∋x}n^{ℓ,x}_j`. Finally `N_x` and `Q_x` are gauge invariant, so `ω_m(N_x) = Φ_m(N_x) = 0` and `ω_m((Q_x − 6k)^2) = 0`. ∎

Theorem U2 checks out on these witnesses: `q − 3m = 0` and `q − 3m = 5`.

**Corollary U3′ (records; under PS-3c and the proposed reading PS-3h5).** In `ω_m`, `N_x = 0` with probability one at every site and tick. If actual values are site numbers (PS-3h5 for `L5-U`), a record forms at every site at the end of tick 1, with value `0` (value `5` for the full-matter witness). The proof is that of Corollary O3.


### 4.5 Odd `m`: no product witness

**Theorem U4.** Let `m` be odd. Let `Φ` be a state of `L5-U[m]` that is invariant under every `β_g`, sharp in every `N_x` and in every `Q_x`, and a product state over a `𝒢`-invariant partition `𝒫` of the set of links: `Φ(AB) = Φ(A)Φ(B)` whenever `A` and `B` lie in the register algebras of disjoint unions of blocks. Then either `𝒫` has a single block, or every connected component of every block is a bi-infinite path and `Φ|𝔄^G` is not pure. So no such `Φ` with a nontrivial `𝒫`, and no gauge average `Φ∘E` of one, meets (iii) and (iv-P).

*Proof.* *Step 1 (partial sums are sharp).* For a block `B` and a site `x` put `s_{B,x} = Σ_{ℓ∈B, ℓ∋x}p_{ℓ,x}`. `Q_x − N_x = Σ_Bs_{B,x}` is sharp, since `Var(X + Y) ≤ 2Var X + 2Var Y` for commuting `X, Y`. The summands lie in the algebras of distinct blocks, so they are uncorrelated, and the variance of the sum is the sum of the variances. So each `s_{B,x}` is sharp, with an integer value `σ_{B,x}`.

*Step 2 (what a block looks like at a site).* The turn `h_x` maps `𝒫` to itself and fixes `x`, so it preserves the partition of `x`'s six links by blocks. By Lemma S2′(b) it acts on them with two free orbits: the even-cube links `a_1, a_2, a_3` and the odd-cube links `b_1, b_2, b_3`, labelled by axis. A part fixed by `h_x` is a union of orbits. A part not fixed by `h_x` has three disjoint images, so it has at most two links, at most one from each orbit. So the partition at `x` is one of: (α) one part; (β) the two orbits; (γ) a partition with a singleton; (δ) three pairs `{a_i, b_{i+k}}`, indices mod 3. `𝒢` maps the partition at `x` onto the partition at `gx` and is transitive, so every site is in the same case.

*Step 3 (γ: a leaf).* A block meeting `x` in one link `ℓ` has `s_{B,x} = p_{ℓ,x}` sharp. Lemma 4.0(b) forbids it.

*Step 4 (β: cubes).* At every site, the even-cube links lie in one part and the odd-cube links in another. Let `B` be the block of a link of a cube `C`. It contains all links of `C` at both ends of that link, so all twelve links of `C`, since the cube's edge graph is connected. At a corner of `C` it contains no other link, since the other links there belong to the other tiling and so to the other part. The rotations about `C`'s centre lie in `𝒢` and fix `C`. They map `B` onto a block that contains `C`, so onto `B`, and they act transitively on `C`'s corners (Lemma S2′(c)). So `σ_{B,x}` takes one value `σ` on all eight corners. As operators, `Σ_{x∈C}s_{B,x} = Σ_{ℓ⊂C}(p_{ℓ,\rm src} + p_{ℓ,\rm tgt}) = 12m`. So `8σ = 12m` and `σ = 3m/2 ∉ Z`, a contradiction.

*Step 5 (α: one block).* All six links at every site lie in one block, and the link graph of `Z^3` is connected.

*Step 6 (δ: the components are bi-infinite paths).* Every site meets each of its blocks in two links, so each connected component of a block is a cycle or a bi-infinite path. Let `k(x) ∈ Z/3` be the pairing type at `x`. For a link `ℓ = (x, y)`, `β_{r_ℓ}` maps the pairing at `x` onto the pairing at `y`. The linear part of `r_ℓ` swaps two axes (Lemma S2′(a)), and `r_ℓ` preserves the tilings, so `a_i(x) ↦ a_{π(i)}(y)` and `b_i(x) ↦ b_{π(i)}(y)` with `π` a transposition. For `π = (2 3)`, the pair `(i, i + k)` goes to `(π(i), π(i + k)) = (π(i), π(i) − k)`; the other transpositions are conjugates. So `k(y) = −k(x)` for neighbours `x, y`. Hence either `k ≡ 0`, or `k` takes the values `1` and `2` on the two sublattices `x_1 + x_2 + x_3` even and odd. If `k ≡ 0`, each pair at `x` is the two links of `x` along one axis, and the blocks are straight lines. In the alternating case, follow the component through `0` that leaves along `+e_1`. For `k(0) = 1` it visits `0, (1,0,0), (1,0,−1), (1,1,−1), (2,1,−1), (2,1,−2), (2,2,−2)`, and it enters `(2,2,−2)` through the translate by `T = (2,2,−2)` of the link `{(0,−1,0), 0}` through which it enters `0`. The structure is invariant under `T ∈ 2Z^3`. So `T` maps the block of this component onto the block of the translated link, which is the same block, and maps the component onto the component of that link, which is the same component. So the component is invariant under `T` and is infinite. For `k(0) = 2` the same holds with `0, (1,0,0), (1,−1,0), (1,−1,1), (2,−1,1), (2,−2,1), (2,−2,2)` and `T = (2,−2,2)`. `h_0` permutes the three components through `0`, and `𝒢` is transitive, so every component is an image of this one and is a bi-infinite path.

[check] `check_pairs.py` tests five type functions against all 24 rotations and 27 translations on a box of 125 sites: `k ≡ 0` and both alternating functions are `𝒢`-invariant, `k ≡ 1` and `k ≡ 2` are not. Its traces of the three invariant structures agree with the sequences above.

*Step 7 (paths are not pure on `𝔄^G`).* Let a component `γ` of a block `B` have vertices `x_i` and links `ℓ_i = {x_i, x_{i+1}}`, `i ∈ Z`, and put `u_i = p_{ℓ_i,x_i}`. At `x_i`, `B` contains exactly `ℓ_{i−1}` and `ℓ_i`, so `s_{B,x_i} = (m − u_{i−1}) + u_i` is sharp with value `σ_i`. `r_{ℓ_i}` fixes `ℓ_i`, so it maps `B` onto itself and `γ` onto itself, and it maps `s_{B,x_i}` onto `s_{B,x_{i+1}}`. So `σ_i = σ` for all `i`. Then `Φ(u_i) = Φ(u_0) + i(σ − m)`, and `0 ≤ u_i ≤ 5`, so `σ = m`. Each increment `u_i − u_{i−1}` then has `Φ((u_i − u_{i−1})^2) = 0`, and Minkowski's inequality for `X ↦ Φ(X^*X)^{1/2}` gives `Φ((u_i − u_0)^2) = 0`. Let `P_i` be the spectral projection of `u_i` onto `{u ≤ (m − 1)/2}`. `u_i` and `u_0` commute and agree with probability one in `Φ`, so `Φ((P_i − P_0)^2) = 0`. `β_{r_{ℓ_0}}` maps `u_0` to `m − u_0` and so `P_0` to `1 − P_0`, since `m` is odd; hence `Φ(P_0) = 1/2`. Each `P_i` is a local element of `𝔄^G`, and the `ℓ_i` leave every finite set as `i → ∞`. Lemma 2.5 shows that `Φ|𝔄^G` is not pure. The gauge average has the same restriction to `𝔄^G`. ∎

### 4.6 Odd `m`: what is open

**VC1-5U-odd (OPEN).** For odd `m`, is there a state of `L5-U[m]` with (i), (ii), (iii) and (iv-P)? By Theorem U2 its filling would be an integer. Three attacks failed.
- *Attack 1, site products.* The singlets of Proposition Σ-U(iii), and every state that factorizes across the two ends of each link, have sharp end numbers. This fails at Lemma 4.0(c): reversal forbids sharp end numbers for odd `m`.
- *Attack 2, products over invariant partitions of the links*, in the dark sectors where every `N_x` is sharp (where stationarity is free). This fails at Theorem U4: leaves fail at Lemma 4.0(b), cubes at `σ = 3m/2`, paths at Lemma 2.5.
- *Attack 3, coherent ice superpositions.* With empty matter, the base tick acts only through `W_E`, which is a constant phase on the sector where every end number is `(m ± 1)/2`. There, sharp `Q_x = 3m` means three ends with `(m + 1)/2` and three with `(m − 1)/2` at every site: an ice rule. On a periodic box, take the equal-amplitude superposition, in the Rokhsar-Kivelson manner (credited from memory), of the ice configurations of one `𝒢`-invariant winding sector, for instance zero winding (it contains the configurations with each axis's lines oriented alternately), with highest-weight flavours at each end. Its local weak-* limit points are stationary and `𝒢`-invariant, and their gauge averages are gauge invariant. The attack fails at the step "a limit point is pure on `𝔄^G`". A weak-* limit of pure states need not be pure (section 2, example), and no argument for this one is found here.

The same three attacks apply with (i) dropped, to pure all-site singlets for odd `m`; that residual of LW1-5U-Σc is named **LW1-5U-Σc-odd**. Both items ask for a symmetric state whose end numbers fluctuate coherently around the half-integer `m/2`. Lieb-Schultz-Mattis type reasoning (literature context, not used) suggests such a state, if it exists, cannot be short-range entangled; Theorem U4 proves the product case of that.

---

## 5. LW1-5U-Σc: point-group invariance of the pure all-site singlets

**Theorem Σc.**
(i) Let `m = 2k` be even, and `n = n_m` from the table of Proposition Σ-U (`n = 4, 3, 2, 1` for `m = 2, 4, 6, 8`). There is a pure state of `𝔄` that is invariant under every local gauge automorphism and under every lift `β_g`, `g ∈ 𝒢`, in which `N_x = n` and every end number equals `k`, sharply. Its Gauss charge is `Q_x = n + 3m ∈ 5Z`, and its filling is `n`.
(ii) Let `m` be odd. No state invariant under the reversal of a link has sharp end numbers on that link. So no singlet of Proposition Σ-U(iii), and no state that factorizes across the two ends of every link (a product over sites, in particular), is invariant under `𝒢`.

*Proof of (i).* *The site space.* Fix a site `x_0` and put `W = Λ^n(C^5_{x_0}) ⊗ ⊗_{ℓ∋x_0}Λ^k(C^5_{ℓ,x_0})`, the factor at `x_0` of the sector `{N = n, every end number = k}`. By the table, `n + 6k = n + 3m ≡ 0 (mod 5)`. By Lemma S of `LW1_5U_DRAFT.md` (rebuilt below), `W` has a nonzero subspace `W^{SU(5)}` of `SU(5)`-invariant vectors. `Q_{x_0}` equals `n + 6k` on it. *The stabilizer.* The local implementer of `β_{h_{x_0}}` maps `W` onto itself. It multiplies matter by the sign `d^n`, and it permutes the six end factors. When a source end becomes a target end, reordering the register's modes costs the sign `(−1)^{k·k}`, which is fixed because `k` is. So it commutes with the diagonal `U(5)` action and maps `W^{SU(5)}` into itself. A unitary on a nonzero finite-dimensional space has an eigenvector `v_0`. *Transport.* For each site `x` choose `g_x ∈ 𝒢` with `g_xx_0 = x` (A2), with `g_{x+2t}` equal to translation by `2t` composed with `g_x`. Let `v_x ∈ W_x` be the image of `v_0` under the local implementer of `β_{g_x}`; it is defined up to a phase. Let `Ψ` be the product state of the `v_x` on the sector. Each register lies in its `(k, k)` part, which is the tensor product of its two end factors, so `Ψ` is well defined. The site vectors have definite matter parity, so reordering them changes the global vector only by a sign. *Pure.* Lemma 2.3 with `𝔅 = 𝔄`, `P_S` the sector projection of Theorem U3 with `Π[N_x = n]` in place of `Π[N_x = 0]`, and `𝒞_S` the set of all `P_S(Y ⊗ 1)P_S` with `Y ∈ End(⊗_{x∈S}W_x)` and `1` on the outer ends, a copy of `End(⊗_{x∈S}W_x)`. A local `A` whose sites and link ends lie in `S` has `P_SAP_S ∈ 𝒞_S`, and `Ψ|𝒞_S` is the vector state of `⊗_{x∈S}v_x`. A vector state of a full matrix algebra is pure. *Gauge invariant.* `v_x` is `SU(5)_x`-invariant and a `Q_x`-eigenvector, so every `V_x(g)`, `g ∈ U(5)_x`, multiplies it by a phase (the converse half of Lemma P of `LW1_5U_DRAFT.md`, line 60). *Symmetric.* For `g ∈ 𝒢` and a site `x`, `h = g_{gx}^{-1}gg_x` fixes `x_0`, so `h` is a power of `h_{x_0}`. By Lemma C(iv), `β_g∘β_{g_x} = σ∘β_{g_{gx}}∘β_h` for a sign automorphism `σ`. `β_h` maps `v_0` to a phase times `v_0`, and `σ` multiplies a vector of definite matter number by a phase. So `β_g` maps `v_x` to a phase times `v_{gx}`, and `Ψ∘β_g = Ψ`. The filling is `n` because `N_x = n` on the sector. ∎

*Lemma S, rebuilt (from `LW1_5U_DRAFT.md`, Lemma S and Lemma E).* Let `a_0, …, a_r ∈ {0, …, 5}` with `Σa_i ≡ 0 (mod 5)`, and `V = C^5`. Then `⊗_iΛ^{a_i}V` has a nonzero `SU(5)`-invariant vector. Two maps are used. (E2) For `a + b ≤ 5`, the `(a, b)` component of the coproduct `v ↦ v ⊗ 1 + 1 ⊗ v` of the exterior algebra sends `e_S` to `Σ_{A⊂S,|A|=a}±e_A ⊗ e_{S∖A}`. It is `U(5)`-equivariant. It is injective, because from a basis tensor `e_A ⊗ e_B` in the image one recovers `S = A ∪ B`, so images of distinct basis vectors have disjoint supports. (E3) For `a + b ≥ 5`, let `vol = e_{12345}`, which is `SU(5)`-invariant. The map `w ↦ (id ⊗ ∧)(Δ_{a,5−a}(vol) ⊗ w)` from `Λ^{a+b−5}V` to `Λ^aV ⊗ Λ^bV` sends `e_T` to `Σ_{|A|=a}±e_A ⊗ (e_{A^c} ∧ e_T)`. A term is nonzero exactly when `T ⊂ A`, and such `A` exist since `|T| ≤ a`. From `e_A ⊗ e_{A^c∪T}` one recovers `T`, so the map is injective, and it is `SU(5)`-equivariant. Now merge factors from the left. Given an equivariant injection `Λ^sV → Λ^{a_0}V ⊗ ⋯ ⊗ Λ^{a_{i−1}}V` with `s ≡ a_0 + ⋯ + a_{i−1} (mod 5)`, compose with (E2) or (E3) tensored with the identity to get one for `i + 1` factors. At the end, `Λ^0V` or `Λ^5V` embeds; both are trivial under `SU(5)`. ∎

*Proof of (ii).* Lemma 4.0(b) and (c). The singlets of Proposition Σ-U(iii) have end numbers `α` and `m − α` by construction. ∎

**What this settles.** LW1-5U-Σc asked whether a pure all-site singlet can be point-group invariant, with the site-stabilizer action on the invariant space "not computed" for even `m`. For even `m` the answer is yes, by an eigenvector of the stabilizer and transport along `𝒢`. The singlets of (i) are not claimed stationary: with `n ∈ {1, …, 4}` the hops act on them. For odd `m`, every singlet with sharp end numbers fails; whether a singlet with coherently fluctuating end numbers can be invariant is LW1-5U-Σc-odd (section 4.6).

---

## 6. Named failing steps

PS-7 says "The vacuum is the half-filled state of the update's fermion modes." PS-7r makes "the half-filled sea" the free quasi-free state and leaves the gauged vacuum to VC1. Whether the gauged vacuum must itself be half filled is the owner-level reading LW1-5U-PS7 (`LW1_5U_DRAFT.md` line 163). Call the reading that it must be **PS-7(h)**.

- **`L5-U[m]`, reading P, under PS-7(h): fails at Theorem U2**, for every `m`, every `ε, μ, τ_E` and every plaquette class. The failing step is exact: reversal invariance fixes `ω(p_{ℓ,x}) = m/2`, so a Gauss-sharp state has integer filling `q − 3m`. It does not use stationarity, so no choice of dynamics repairs it.
- **`L_cube`, reading P, under PS-7(h): fails at Corollary U2′**, with filling `0` or `1`.
- **`L5-U[m]`, reading E**: no failing step. `τ = ω_{t=0}` is half filled (Theorem U1).
- **`L5-O[S_+]`**: no failing step under either reading. Lemma H forces filling `5/2`, and Theorems O1 and O2 give witnesses.
- Without PS-7(h), no step fails on either law under reading E. Under reading P, `L5-U` with even `m` has witnesses at fillings `0` and `5`, and odd `m` is VC1-5U-odd.

What (i)-(iv) leave to VC1, in one paragraph. They do not select a state: `L5-O` has `τ`, `ω_0` and `ω'_0`, and `L5-U` has the family `ω_t` and, for even `m`, `ω_m` and its full-matter partner. The P-witnesses are dark: no hop acts on them. They are not continuations of the PS-7r sea, and they bear on VC1(1)-(3) only by showing that (i)-(iv) do not imply them. On VC1(4) the witnesses split: under PS-3h5 the dark witnesses form a record at every site at tick 1 (Corollaries O3 and U3′), and `τ` never forms one. So TM1-i's answer depends on which state VC1 selects.

---

## FINISH

**Proved here (pass 1, not distilled or refereed).**
- Lemma 1.1: the gauge average `E`; gauge-invariant states correspond one to one to states of `𝔄^G`; `E` commutes with the tick and with the lifts.
- Lemma C: cell covariance of `L5-U` (the analogue of B1-5, recorded as not proved in `LW1_5U_DRAFT.md`), and the properties of the lifts on both laws.
- Lemma S2′: link reversals with a transposition as linear part; the site stabilizer `Z_3` with two free orbits on the six links; cube stabilizers transitive on corners.
- Lemma R: for gauge-invariant states, pure on `𝔄^G` is the same as extremal among gauge-invariant states; reading P implies reading E.
- Lemmas 2.1-2.5: central elements are sharp in pure states; purity on invariants from a one-dimensional joint eigenspace; the sector lemma for purity at infinite volume; the tracial state is invariant under every local automorphism, and invariant product states are extremal; a macroscopic two-valued variable rules out purity.
- Theorem O1: on `L5-O[S_+]` the tracial state meets (i)-(iii) and reading E, with filling `5/2`.
- Theorem O2: on `L5-O[S_+]`, `ω_0 = Φ_0∘E` (matter vacuum and rishon vacuum, gauge averaged) meets (i)-(iii) and reading P, hence E, with filling `5/2`. Remark O2.1: a distinct second witness `ω'_0`. Corollary O3: under PS-3c with PS-3h5, `ω_0` forms a record at every site at tick 1.
- Lemma 4.0: on `L5-U`, reversal invariance gives `ω(p_{ℓ,x}) = m/2`, and for odd `m` forbids sharp end numbers and factorization across the link.
- Theorem U1: on `L5-U` the product states `ω_t` meet (i)-(iii) and reading E at every filling in `[0, 5]`.
- Theorem U2: on `L5-U`, a state invariant under the link reversals and sharp in `Q_x` has filling `q_x − 3m ∈ Z`, at infinite volume and for any law data; states meeting (iii) and reading P are never half filled. Corollary U2′: the same for `L_cube`, with filling `0` or `1`.
- Theorem U3: for even `m`, `ω_m` meets (i)-(iii) and reading P at filling `0`, and its full-matter partner at filling `5`. Corollary U3′ on records.
- Theorem U4: for odd `m`, a `𝒢`-invariant state, sharp in every `N_x` and `Q_x`, that is a product over a nontrivial `𝒢`-invariant partition of the links is never pure on `𝔄^G`. The only such partitions with sharp partial sums have bi-infinite paths as components: straight lines, or two families of staircases.
- Theorem Σc: for even `m`, pure, gauge-invariant all-site singlets invariant under every lift of `𝒢` exist, with filling `n_m`; for odd `m`, none has sharp end numbers.

**Counterexamples.**
- To "(i)-(iv) select the vacuum": Remark O2.1 (two distinct P-witnesses on `L5-O`) and Theorem U1 (a one-parameter family of E-witnesses on `L5-U`).
- To "a state of `L5-U` with (iii) and (iv-P) can be half filled", at infinite volume: Theorem U2. For `L_cube`: Corollary U2′.
- To "the singlets of Proposition Σ-U(iii) can be chosen point-group invariant" for odd `m`: Theorem Σc(ii).
- To "products over invariant link partitions give P-witnesses for odd `m`": Theorem U4.

**Open, by name.**
- **VC1-5U-odd**: a state of `L5-U[m]`, `m` odd, with (i)-(iii) and reading P. Attacks failed: site products (Lemma 4.0(c)); products over invariant link partitions (Theorem U4); coherent ice superpositions (fails at purity of the infinite-volume limit).
- **LW1-5U-Σc-odd**: a pure `𝒢`-invariant all-site singlet for odd `m`; the same three attacks apply.
- Reading P with a plaquette class, on both laws: the dark witnesses use the base tick, and plaquette monomials move them.
- Unchanged: LW1-5U-PS7 (owner reading), LW1-5-BG, LW1-5-X, GA1-P-5, LW1-5-RQ (owner).

**What changes downstream.**
- **VC1 on `L5-O`.** The existence part of VC1 holds at half filling under both readings of (iv), for the base tick. Proposition Σ (no pure Gauss singlet with one register class) does not block a vacuum that is pure on the gauge-invariant observables, stationary and symmetric. This extends `LW1_5O_DRAFT.md` Proposition S5 from finite regions to a stationary infinite-volume state.
- **VC1 on `L5-U`.** Under reading P the vacuum is never half filled, at infinite volume as on boxes. Under PS-7(h), `L5-U` fails at Theorem U2; this is a new fact for LW1-5-RQ. Under reading E the filling is free.
- **Section 3.5's shared fact splits by law.** "Both laws, and `L_cube`: on a periodic box, no pure, locally gauge-invariant, site-transitive state is half filled" stays true. On `L5-O`, half filling is forced by gauge invariance and is reached by a stationary symmetric state that is pure on `𝔄^G` (Theorem O2). On `L5-U` and `L_cube`, reading P forbids half filling at infinite volume too (Theorem U2, Corollary U2′).
- **Items of `LW1_5U_DRAFT.md`.** Its line 304 item (infinite-volume form of Theorem F-U and Remark F.1) is closed by Theorem U2 and Corollary U2′. Its line 303 item (covariance of `L5-U`) is closed by Lemma C. LW1-5U-Σc is settled as posed by Theorem Σc, with residual LW1-5U-Σc-odd.
- **TM1-i.** Which state VC1 selects decides whether records form in the vacuum: at once and everywhere for the dark witnesses under PS-3h5, never for `τ`.
