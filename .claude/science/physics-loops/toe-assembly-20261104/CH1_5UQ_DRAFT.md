lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CH1-5U-q on `L5-U`, pass 1: what "light" can mean, a pinned-charge lemma, exact charge-3 zero modes, and the coherence condition

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 of the open sub-lemma CH1-5U-q of `CH1_5U_DRAFT.md` section 5, under the method of open PR #10138 (Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen).

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks one tiny scratch computation (`/tmp/toe-ch15uq/check_ch15uq.py`, output `out.txt`; floating point on one link with its two end sites, largest space `2^{20}`; 10 s, 0.90 GB peak, run after `memory_pressure` showed 64 percent free). A check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local checkout, branch `claude/toe-assembly` (sparse) | `4b65c608f` |

No other branch was read. Files read at that commit, by line, with the commit of their last change. This folder: `CH1_5U_DRAFT.md` (`ecb2036d9`) lines 1-290 (all; Theorem Φ at 82, Lemma Q1 at 100, Lemma Q1′ at 183, Attack 4 at 198-204, CH1-5U-q at 230-234, Lemma Q3 at 236); `CH1.md` (`5ff19240c`) lines 1-229 (all; inferred definitions 1, 6, 8 at 19, 24, 26; Lemma S1-5 at 105; Lemma B at 137; Lemma U-T′ at 179-195; Corollary U-T″ at 197-203; AM-5 at 207); `LIT_SMG.md` (`5d1409d92`) lines 1-216 (all); `VC1_5_DRAFT.md` (`2d0adc0c0`) lines 1-352 (all; Lemma 1.1 at 70, Lemma C at 80, Lemmas 2.2-2.4 at 132-144, Theorem U1 at 222, Theorem U2 at 228, Theorem U3 at 240, VC1-5U-odd at 279); `LW1_5.md` (`4b65c608f`) lines 1-350 (all; inferred definition 4 at 40, the law `L5-U` at 85-91, Theorem U at 134, Z-U at 231); `Y2W_DRAFT.md` (`92e03055c`) lines 1-30 (format) and 96-128 (Theorem W2); `CH1_DRAFT.md` (`b913d2d2e`) lines 301-303 (Lemma AM, hypothesis IR) and 340-400 (Lemma C3, CH1-C1); `CH1_5_DRAFT.md` (`a8a208fdf`) lines 40-60 (hypothesis IR at 49), 205, 239, 250, by grep; `TOE_ASSEMBLY.md` (`7d2b20d29`) lines 140-160 (PS-8) and 395-415 (CH1). `CH1_5U_REFEREE.md` (untracked, no commit; it appeared in the checkout while this lane ran) was read only by grep for "CH1-5U-q", "dress" and "light" (lines 19, 36, 80, 99, 138-140, 159, 177-181, 195-199, 260, 293-302).

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The law `L5-U` is read plainly. One word of CH1-5U-q needs a meaning: "light". Section 1.3 states three readings, sections 2-6 decide or attack CH1-5U-q under each, and section 7 puts each through the four tests. Nothing is adopted.

**Working set used, by name.** PS-5, PS-6 and PS-6r, only through the law `L5-U` of `LW1_5.md` section 2. PS-1c, only through the cell-group lifts of `VC1_5_DRAFT.md` Lemma C. PS-8, only as the kind of added gate that CH1-5U-i (a) allows; no proof below uses an added gate. Results used, quoted at the point of use: from `LW1_5.md`, the statement of `L5-U`, inferred definition 4, Theorem U and Z-U; from `VC1_5_DRAFT.md`, Lemma 1.1, Lemma C, Lemmas 2.2-2.4, Theorems U1-U3; from `CH1.md`, inferred definitions 1, 6, 8, the gauge action in the proof of Lemma U-T′, Corollary U-T″; from `CH1_5U_DRAFT.md`, the statement of CH1-5U-q and Lemma Q1′; from `Y2W_DRAFT.md`, Theorem W2; from `CH1_DRAFT.md`, hypothesis IR of Lemma AM. PS-2, PS-3, PS-4, PS-7, PS-9 to PS-11 are not used.

**Inputs from outside the working set.** *Standard mathematics, rebuilt in the text:* characters of a finite torus acting on a finite-dimensional space; the GNS construction and the unitary that implements a state-preserving automorphism; Cauchy-Schwarz; Hölder's inequality for the trace norm of `5 × 5` matrices; the numerical radius of an operator of square zero; Schur's lemma; complete reducibility of finite-dimensional unitary representations of compact groups (cited, not rebuilt). *Physics cited, never load-bearing:* the equal-time two-point function of a free massless Weyl field, whose modulus is a constant times `|r|^{-3}`; Elitzur's theorem (1975) on vanishing gauge-variant expectations; Dirac's dressing of charged fields (1955) and the charged-sector literature (Buchholz; Fröhlich, Morchio and Strocchi), for the remark that string dressings decay by a perimeter law; Lieb and Robinson (1972), only as the name of the light-cone idea. *Literature map:* `LIT_SMG.md` sections 6, 8, 9 and 15 (Wang-You; Golterman-Shamir 2025 and 2026; Fidkowski-Kitaev), used as the map says, as context.

---

## 0. The question, quoted

`CH1_5U_DRAFT.md` line 230, **Lemma CH1-5U-q (open).** "There exist an update `U` of `L5-U` form (as in CH1-5U-i (a)), a state `ω` stationary under `U` and invariant under `G_U` and gauge transformations, and a quasi-local fermion-odd operator `ψ` of `U(1)_N` charge `q` with `|q| ≥ 3`, whose large-separation correlations in `ω` agree with those of a free Weyl field."

Line 232: "CH1-5U-i implies CH1-5U-q: its hypothesis IR supplies a light field in `10_u`, of charge `u` with `|u| ≥ 3` (Lemma Q1). So a proof that every light fermion of such a state has charge `±1` refutes CH1-5U-i."

`CH1.md` line 26, inferred definition 8: "**IR** is the drafts' hypothesis of quasi-local odd operators with large-separation Weyl correlations and no other long-range connected correlations. Charged correlators require a gauge-covariant dressing or a charge-sector prescription."

`CH1_5_DRAFT.md` line 250: "False: a theorem that every light fermion of an invariant stationary state of an `L5-U` law has `|U(1)_N| ≤ 5`, or is carried at one site".

**The lane's target.** Can a stationary, gauge-invariant, cell-symmetric state of an `L5-U` law have a light fermion-odd excitation of `U(1)_N` charge `|q| ≥ 3`? A no-go is a named failing step for `L5-U`'s CH1 route; a construction keeps it alive. State what "light" means and check that definition.

## 0.1 Outcome in one paragraph

**Three readings of "light"** (section 1.3). L1 is the text's own: correlations of an undressed field. L2 is spectral, as the brief suggests: the excitation `ψΩ` lies within `δ` of quasi-energy 0. L3 is dressed: a gauge-invariant bilocal `ψ_x^* D α^n(ψ_y)`, with a norm-bounded dressing `D` that moves no matter, has correlations no smaller than `c|x − y|^{-3}`. **L1: false for every charge.** Every update of `L5-U` form conserves each local charge `Q_z`, so a gauge-invariant state kills every correlation between separated charged operators, at every time (Lemma G). Hence no fermion-odd field of any charge, `±1` included, has Weyl correlations (Corollary G1). This decides CH1-5U-q as written, but through the reading: the same proof kills the literal hypothesis IR on `L5-O` and `L_cube`, and it is the theorem behind CH1's inferred definition 8. L1 fails test 3. **L2: true.** At a site whose matter and six link ends hold the same flavours, every hop on its links vanishes, and the base tick conserves this "frozen" property for every `m` and every constant (Lemma F1, Theorem Z0). For `3 ≤ m ≤ 7` (any `τ_E` for odd `m`, `τ_E = 0` for even `m`) this gives a local fermion-odd operator `Ψ` of `U(1)_N` charge 3 with `α(Ψ) = Ψ` exactly; in the tracial state, `ΨΩ` is an exact quasi-energy-0 eigenvector (Theorem Z). So CH1-5U-q holds under L2, and no charge-weighted spectral bound can fail `L5-U` (Corollary Z1). But the excitation is pinned and frozen: L2 is met by a static defect, and it carries none of IR. **L3: open, and charge-blind as far as the tools reach.** A dressed correlation across a distance needs matter-number coherence between distant sites. Every gauge-invariant state that is diagonal in the link end numbers kills it, for every charge (Lemma E), and every stationary invariant state on file is such a state. For string dressings, every state that is a product over the links of the string gives at most `5·2^{-L}` for charge 1 (Corollary W2′.1, from Theorem W2 of `Y2W_DRAFT.md`). **The proposed no-go tools fail at exact steps:** the light cone does not see charge (section 5.1); the register carries a triple across one link exactly when `3 ≤ m ≤ 7` (Lemma T); the spectral bound is refuted by Theorem Z; the pinned charge decides only L1. **No named failing step for `L5-U`.** CH1-5U-q under L3 stays open after three failed attacks each way. What it needs, for charge 1 as much as for charge 3, is a stationary invariant state with electric coherence that is entangled across links: a gauge-sector question (VC1, GA2's bridge Y2). By-product for VC1: for even `m`, the all-frozen state is a stationary, invariant state, pure on the gauge-invariant algebra, at filling `m/2` (Corollary F2).

---

## 1. Setting

### 1.1 The law, its charges and its states

`CH1.md` line 177 restates the register: "Each link carries ten rishon modes, fermionic among themselves, in an ordinary tensor factor that commutes with matter and with other links. The register is `Λ^m(C^{10})`, so `p_{ℓ,x} + p_{ℓ,y} = m`." `LW1_5.md` line 85: "Put \(U_\ell^{jk}=r^{y}_jr^{x\dagger}_k\),", and line 87, displayed: "h^U_\ell=\sum_{jk}c^\dagger_{y,j}U_\ell^{jk}c_{x,k}+\mathrm{h.c.}", with `x` the source of `ℓ = (x, y)`, cube generators `H_C = 3^{−1/2}Σ_{ℓ⊂C}η_ℓh_ℓ`, cube layers `M_e`, `M_o`, electric layer `W_E = ∏_ℓe^{−iτ_E(p_{ℓ,x}−m/2)^2}` and base tick `U_0 = W_EM_oM_e`. Write `N_z` for the matter number at `z`, `p_{ℓ,z}` for the rishon number at the `z`-end of `ℓ`, and `Q_z = N_z + Σ_{ℓ∋z}p_{ℓ,z}`, the generator of the centre of `U(5)_z`. `LW1_5.md` line 134, Theorem U: "every \(\mathcal G_x^T\) commutes with every hop and electric gate."

An *update of `L5-U` form* is `U_0` together with finitely many layers of gauge-invariant site or cell gates (CH1-5U-i (a)); a gate is gauge invariant when it commutes with every `𝒢^T_z`. Its *tick automorphism* is `α(A) = U^*AU` on the quasi-local algebra `𝔄`; for local `A`, `α(A) = U_F^*AU_F` with `U_F` a finite product of gates (`LW1.md` E1, as used in `VC1_5_DRAFT.md` section 1.1). A state `ω` is *stationary* if `ω∘α = ω`, *gauge invariant* if `ω∘Ad V_z(g) = ω` for every site `z` and `g ∈ U(5)` (`V_z(g)` as in `VC1_5_DRAFT.md` section 1.2), and *cell symmetric* if `ω∘β_g = ω` for the lifts of `VC1_5_DRAFT.md` Lemma C, whose part (iii) reads: "`β_g` maps every Gauss generator at `x` to the same generator at `gx`; on `L5-U` it maps `N_x ↦ N_{gx}`, `Q_x ↦ Q_{gx}` and `p_{ℓ,z} ↦ p_{gℓ,gz}`".

*GNS.* For a stationary `ω` with GNS triple `(H, π, Ω)`, put `Ũπ(A)Ω := π(α(A))Ω`. This is well defined and isometric, because `ω(α(A)^*α(A)) = ω(α(A^*A)) = ω(A^*A)`. Its range is dense, because `α` is onto. So `Ũ` extends to a unitary with `ŨΩ = Ω`. Quasi-energy `w` means eigenvalue `e^{−iw}` of `Ũ`.

### 1.2 Local charge vectors

For a local `A`, let `S(A)` be the set of sites where `A` has matter, together with both ends of every link in its support (as in `VC1_5_DRAFT.md` section 1.2), and `M(A)` the set of sites where it has matter. `A` is *homogeneous* with *charge vector* `(q_z)` if `Ad e^{iθQ_z}(A) = e^{iθq_z}A` for all `z` and `θ` (`CH1_5_DRAFT.md` line 41). Its *total charge* is `Σ_zq_z`; this is the "`U(1)_N` charge" of CH1-5U-q (`CH1.md` inferred definition 6).

**Lemma 1.2 (components; charges are static).**
(a) The `Q_z` commute pairwise and have integer spectra. Every local `A` is a finite sum `A = Σ_qA_{(q)}` of local homogeneous operators whose charge vectors vanish off `S(A)`. If `A` is fermion odd, every `A_{(q)}` is fermion odd and has odd, hence nonzero, total charge.
(b) Likewise every local `A` is a finite sum of components with definite changes `(δN_z, δp_{ℓ,z})` of all matter and end numbers, with `δN` vanishing off `M(A)`. If `A` has total charge `q`, every component has total matter change `Σ_zδN_z = q`.
(c) For every update of `L5-U` form and every `n ∈ Z`, `α^n(A_{(q)})` is homogeneous with the same charge vector `q`.

*Proof.* (a) `Q_z` is a sum of commuting number operators (matter at `z`, the six ends at `z`), so its spectrum is integral. `Q_z` and `Q_{z'}` meet only through a shared link `ℓ = (z, z')`, where `p_{ℓ,z}` and `p_{ℓ,z'}` count disjoint modes and commute. Let `𝔄_F` be a finite local algebra that contains `A`, the matter at every site of `S(A)` and the registers of all links at those sites. Then `θ ↦ Ad(∏_{z∈S(A)}e^{iθ_zQ_z})` is a representation of the torus `T^{S(A)}` on the finite-dimensional space `𝔄_F`, with integer weights. Put `A_{(q)} = (2π)^{−|S(A)|}∫e^{−iq·θ}Ad(∏_ze^{iθ_zQ_z})(A)dθ`. A trigonometric polynomial equals its Fourier series, so `A = Σ_qA_{(q)}`, a finite sum. For `z ∉ S(A)`, `e^{iθQ_z}` commutes with `A`: a link at `z` in the support of `A` would put `z` in `S(A)`. Conjugation by `e^{iθQ_z}` preserves fermion parity. `LW1_5.md` line 231, Z-U: "A local operator with definite \(Q_x\) charges has total charge equal to its matter-number change, and its matter parity is \((-1)^{\sum q_x}\)." So an odd component has odd total charge.
(b) The `N_z` and `p_{ℓ,z}` are commuting number operators; the same projection argument applies, and `e^{iθN_z}` commutes with `A` for `z ∉ M(A)`. These components refine those of (a). For each component, `Σ_zδQ_z = Σ_zδN_z + Σ_ℓ(δp_{ℓ,x} + δp_{ℓ,y}) = Σ_zδN_z`, because `p_{ℓ,x} + p_{ℓ,y} = m` on every register.
(c) Every gate commutes with every `𝒢^T_z`, in particular with `Q_z`. So `α` commutes with `Ad e^{iθQ_z}`, and `Ad e^{iθQ_z}(α^n(A_{(q)})) = α^n(e^{iθq_z}A_{(q)})`. ∎

Part (c) is Gauss's law in operator form. The matter of an excitation can move, since `α^n(A)` has a growing matter support. Its local charges cannot: matter that leaves `z` is replaced in `Q_z` by rishons at the ends of `z`'s links.

### 1.3 Three readings of "light"

Fix a stationary, gauge-invariant `ω`, a local fermion-odd `ψ` of total charge `q`, and translates `ψ_x := β_g(ψ)`, `g ∈ 𝒢`, of a base point to `x`.

- **L1 (undressed; the reading of the text).** `ψ` is light if its two-point function agrees at large separation with that of a free Weyl field; at least, `|ω(ψ_y^*α^n(ψ_x))| ≥ c|x − y|^{−3}` for some `n`, some `c > 0` and pairs with `|x − y| → ∞`. This is hypothesis IR of `CH1_DRAFT.md` line 301, "the correlations of `omega` at large separations agree with those of free Weyl fields", and of CH1-5U-q.
- **L2(δ) (spectral, at a stated scale `δ ≥ 0`).** `ω(ψ^*ψ) = 1` and `ω((α(ψ) − ψ)^*(α(ψ) − ψ)) ≤ δ^2`; that is, `‖(Ũ − 1)π(ψ)Ω‖ ≤ δ`. The excitation lies within `δ` of quasi-energy 0. *Gapless* means L2(δ) for every `δ > 0`.
- **L3 (dressed).** There are pairs `(x_i, y_i)` with `|x_i − y_i| → ∞`, a fixed `n`, local *dressings* `D_i` with `‖D_i‖ ≤ 1` and `[D_i, N_z] = 0` for every `z`, such that `ψ_{x_i}^*D_iα^n(ψ_{y_i})` is gauge invariant and `|ω(ψ_{x_i}^*D_iα^n(ψ_{y_i}))| ≥ c|x_i − y_i|^{−3}` for some `c > 0`. "Agrees with a free Weyl field" adds the tensor structure; L3 is its necessary part.

Why each clause of L3. The bilocal must be gauge invariant, or Lemma G below kills it. The bound `‖D‖ ≤ 1` stops a decaying correlation from being rescaled. The condition `[D, N_z] = 0` excludes dressings that move matter: `D = ψ_xα^n(ψ_y)^*` would turn the bilocal into a product of two local densities. Every link-only operator is allowed, in particular every string of `U_ℓ` and `U_ℓ^†`.

*Relation to the pass-3 referee of CH1-5U-i.* `CH1_5U_REFEREE.md` line 195 restates the sub-lemma with a prescription: "Fix a charged-correlator prescription `𝒫` in the sense of `CH1.md` line 26." Line 197: "For every `𝒫`, CH1-5U-i[`𝒫`] implies CH1-5U-q[`𝒫`]." L3 is one such prescription. L1 is the empty one, and Corollary G1 below proves that it cannot serve. That referee's R2 (line 293) treats quasi-free points at c-number backgrounds; attack P1 of section 6 agrees with it.

*CH1-5U-q(L)* denotes line 230 with "whose large-separation correlations in `ω` agree with those of a free Weyl field" replaced by "light in the sense L", and with `ω` also cell symmetric, as the brief asks. Section 7 checks each reading against the four tests.

---

## 2. L1: the pinned charge kills every undressed correlation

**Lemma G (pinned charge).** Let `α` be the tick automorphism of an update of `L5-U` form, and `ω` a state with `ω∘Ad e^{iθQ_z} = ω` for every site `z` and every `θ` (every gauge-invariant state qualifies). Let `A, B` be local, with components `A_{(q)}`, `B_{(q′)}` as in Lemma 1.2(a). Then for every `n ∈ Z`,
\[
\omega\big(B^*\alpha^n(A)\big)=\sum_q\omega\big(B_{(q)}^*\,\alpha^n(A_{(q)})\big).
\]
In particular, if `S(A) ∩ S(B) = ∅` and every component of `A` has nonzero total charge (for example, `A` fermion odd), then `ω(B^*α^n(A)) = 0` for every `n`.

*Proof.* `Ad e^{iθQ_z}(B_{(q′)}^*) = (Ad e^{iθQ_z}(B_{(q′)}))^* = e^{−iθq′_z}B_{(q′)}^*`. With Lemma 1.2(c), `Y = B_{(q′)}^*α^n(A_{(q)})` is homogeneous with charge vector `q − q′`. Invariance gives `ω(Y) = e^{iθ(q_z−q′_z)}ω(Y)` for all `θ`, so `ω(Y) = 0` unless `q = q′`. Expanding `B^*α^n(A)` gives the formula. If `S(A) ∩ S(B) = ∅`, then `q` vanishes off `S(A)` and `q′` off `S(B)`, so `q = q′` forces `q = 0`, which no component of `A` has. ∎

This is the lattice form of Elitzur's theorem (credited, not used), with one addition: `n` is arbitrary. Under every update of `L5-U` form the charge created at `z` stays at `z`, so no amount of waiting carries it to `y`.

**Corollary G1 (L1 fails for every charge).** Let `ω` be gauge invariant and stationary under an update of `L5-U` form. Let `ψ` be quasi-local and fermion odd in this sense: `ψ = lim_Rψ_R` in norm, with `ψ_R` local, fermion odd, `S(ψ_R)` inside the ball of radius `R` about a base point, and `f(R) := ‖ψ − ψ_R‖`. Put `ψ_x = β_g(ψ)` and `ψ_{x,R} = β_g(ψ_R)`. If `|x − y| > 2R`, then for every `n`,
\[
|\omega(\psi_y^*\alpha^n(\psi_x))|\le(2\|\psi\|+f(R))\,f(R).
\]
So if `f(R) = o(R^{−3})`, the two-point function is `o(|x − y|^{−3})`, uniformly in `n`, and `ψ` is not light in the sense L1. This holds for every total charge, `±1` included.

*Proof.* `β_g` maps sites and links geometrically (Lemma C(i)) by an isometry of `Z^3`, so `S(ψ_{x,R})` and `S(ψ_{y,R})` lie in disjoint balls. Each `ψ_R` is fermion odd, so by Lemma 1.2(a) all its components have odd total charge, and Lemma G gives `ω(ψ_{y,R}^*α^n(ψ_{x,R})) = 0`. Write `ψ_y^*α^n(ψ_x) − ψ_{y,R}^*α^n(ψ_{x,R}) = (ψ_y − ψ_{y,R})^*α^n(ψ_x) + ψ_{y,R}^*α^n(ψ_x − ψ_{x,R})`. Automorphisms of a C*-algebra are isometric, so the norm is at most `f(R)‖ψ‖ + (‖ψ‖ + f(R))f(R)`. ∎

**What Corollary G1 decides.**
- CH1-5U-q(L1) is false: for every update of `L5-U` form, every gauge-invariant stationary state (cell symmetric or not) and every fermion-odd `ψ` with tails `o(R^{−3})`. The modulus of a free Weyl two-point function at equal times is a constant times `|r|^{−3}` (credited), so the failure holds for every reading of "agree" that keeps the leading power.
- For the same reason CH1-5U-i is false under L1: its light fields are fermion odd. So line 232's "a proof that every light fermion of such a state has charge `±1` refutes CH1-5U-i" is true under L1, but vacuously: under L1 there is no light fermion of any charge.
- It is not a failing step of `L5-U`. The proof uses two facts only: gauge-invariant gates conserve each local central charge, and a fermion-odd operator carries a nonzero local charge somewhere. Both hold on `L_cube` (`CH1.md` Lemma S1: "an odd local field has odd charge"). On `L5-O`, with the local centre elements in place of `e^{iθQ_z}`, the second holds under the hypotheses of `LW1_5.md` line 199: "\(-1_{10}\) at every site of \(\Lambda\) acts as fermion parity on operators supported with all their links in \(\Lambda\)". So L1 fails CH1 on every law with exact local gauge invariance, before any dynamics. That is the content of `CH1.md` inferred definition 8, "Charged correlators require a gauge-covariant dressing or a charge-sector prescription", now as a theorem. L1 fails test 3 (section 7).

---

## 3. L2: frozen stars give exact zero modes of charge 3

### 3.1 Frozen stars

All operators below act on the Fock space `𝓕` of the matter and rishon modes of a finite region; the law's Hilbert space `H_Λ` (every register in `Λ^m`) is a subspace of `𝓕`. For a site `x` and a link `ℓ ∋ x` with other end `y`, put
\[
\varphi_{\ell,x}=\sum_{k=1}^5 r^{\ell,x\dagger}_k\,c_{x,k}.
\]
It raises the rishon number of `ℓ` by one, so it leaves `H_Λ`; the products below return to it. Put `G_{ℓ,x} = {v ∈ H_Λ : φ_{ℓ,x}v = 0 = φ_{ℓ,x}^†v}` and `F_x = ∩_{ℓ∋x}G_{ℓ,x}`, the *frozen subspace* of the star of `x` (the site and its six links), with projection `P_x`. A basis vector is *flavour-locked at `x`* if `n^{ℓ,x}_k = n_{x,k}` for every flavour `k` and every `ℓ ∋ x`: each end at `x` holds exactly the flavours of the matter at `x`.

**Lemma F1 (frozen stars).**
(a) `K_x = Σ_{ℓ∋x}(φ_{ℓ,x}^†φ_{ℓ,x} + φ_{ℓ,x}φ_{ℓ,x}^†)` is a local, even, gauge-invariant operator of the law, acting on the matter at `x` and the `x`-ends of its six registers, and commuting with `N_x` and every `p_{ℓ,x}`. `K_x ≥ 0` and `ker K_x = F_x`. So `P_x` is a local, even, gauge-invariant element that commutes with `N_x` and every `p_{ℓ,x}`, and it does not depend on `Λ`.
(b) For `ℓ = (x, y)` of either orientation, `h_ℓ = φ_{ℓ,y}^†φ_{ℓ,x} + φ_{ℓ,x}^†φ_{ℓ,y}`, and `φ_{ℓ,y}` commutes with `φ_{ℓ,x}` and with `φ_{ℓ,x}^†`.
(c) `h_ℓv = 0` for every `v ∈ G_{ℓ,x}`. Hence `h_ℓP_x = P_xh_ℓ = 0` for every `ℓ ∋ x`.
(d) Every basis vector flavour-locked at `x` lies in `F_x`.

*Proof.* (a) Rishons commute with matter, so `φ_{ℓ,x}^†φ_{ℓ,x} = Σ_{jk}(c_{x,j}^†c_{x,k}) ⊗ (r^{ℓ,x}_jr^{ℓ,x†}_k)` and `φ_{ℓ,x}φ_{ℓ,x}^† = Σ_{jk}(c_{x,k}c_{x,j}^†) ⊗ (r^{ℓ,x†}_kr^{ℓ,x}_j)`. The rishon factors conserve both end numbers, so they act on the register; the matter factors conserve `N_x`; all factors are even. For gauge invariance, the proof of `CH1.md` Lemma U-T′(i) computes at a site `x_i`: "`c_{x_i,k} ↦ Σ_{k'} \bar v_{k'k} c_{x_i,k'}` and `r^{ℓ_i,x_i†}_k ↦ Σ_{k''} v_{k''k} r^{ℓ_i,x_i†}_{k''}`. So `A_i ↦ Σ_{k',k''} (vv^*)_{k''k'} c_{x_i,k'} r^{ℓ_i,x_i†}_{k''} = A_i`". There `A_i = Σ_kc_{x_i,k}r^{ℓ_i,x_i†}_k`, which is `φ_{ℓ_i,x_i}` because `c` and `r` commute. So `φ_{ℓ,x}` is invariant under `U(5)_x`; the groups of other sites do not act on it; the same holds for its adjoint and for `K_x`. `K_x` is a sum of terms `T^*T` and `TT^*`, so `K_x ≥ 0`, and `K_xv = 0` exactly when every `φ_{ℓ,x}v` and `φ_{ℓ,x}^†v` vanishes.
(b) If `x` is the source, `Σ_{jk}c_{y,j}^†r^{ℓ,y}_jr^{ℓ,x†}_kc_{x,k} = (Σ_jc_{y,j}^†r^{ℓ,y}_j)(Σ_kr^{ℓ,x†}_kc_{x,k}) = φ_{ℓ,y}^†φ_{ℓ,x}`, and its adjoint is `φ_{ℓ,x}^†φ_{ℓ,y}`; if `x` is the target, exchange the names. Moving matter past rishons, `φ_{ℓ,y}φ_{ℓ,x} = Σr^{ℓ,y†}_jr^{ℓ,x†}_kc_{y,j}c_{x,k}`. Reversing the rishon pair and the matter pair costs two signs, since distinct modes anticommute, so this equals `φ_{ℓ,x}φ_{ℓ,y}`. The same two exchanges give `φ_{ℓ,y}φ_{ℓ,x}^† = φ_{ℓ,x}^†φ_{ℓ,y}`. [check] (1), (2): both identities hold exactly in the matrices.
(c) By (b), `h_ℓv = φ_{ℓ,y}^†(φ_{ℓ,x}v) + φ_{ℓ,y}(φ_{ℓ,x}^†v) = 0`. `F_x ⊆ G_{ℓ,x}` gives `h_ℓP_x = 0`, and `P_xh_ℓ = (h_ℓP_x)^* = 0`. [check] for `m = 1, …, 9`, `h_ℓ` annihilates every null vector of the one-link `K` found in 3000 sampled blocks.
(d) The `k`-th term of `φ_{ℓ,x}` is nonzero on a basis vector only if `n_{x,k} = 1` and `n^{ℓ,x}_k = 0`; the `k`-th term of `φ_{ℓ,x}^†` only if `n^{ℓ,x}_k = 1` and `n_{x,k} = 0`. Locking excludes both. ∎

**Theorem Z0 (frozen stars are conserved and inert).** Let `α` be the base tick of `L5-U[m]`, for any `m`, `ε`, `μ`, `τ_E`, with no plaquette class.
(i) `α(P_x) = P_x`.
(ii) Every hop on a link at `x` annihilates the range of `P_x`.
(iii) Let `Y` act only on the matter at `x` and the registers of the six links at `x`, with `Y = P_xYP_x` and `[Y, e^{−iτ_E(p_{ℓ,x}−m/2)^2}] = 0` for these six links. Then `α(Y) = Y`.

*Proof.* Write `H_C = H_C^x + H′_C`, with `H_C^x` the terms on links at `x`. By Lemma F1(c), `H_C^xP_x = P_xH_C^x = 0`. `H′_C` acts on matter at sites other than `x` and on registers of links not at `x`, which are disjoint from the support of `P_x`; both are even, so `[H′_C, P_x] = 0`. Hence `[H_C, P_x] = 0` and `H_CP_x = H′_CP_x`; by induction `H_C^kP_x = H′^k_CP_x`, so `e^{−iaH_C}P_x = e^{−iaH′_C}P_x`. The electric factors commute with `P_x` by F1(a). For a local `A`, let `U_F` be the finite product of gates with `α(A) = U_F^*AU_F` (E1), and `U′_F` the same product with each `H_C` replaced by `H′_C`. Then `U_F` commutes with `P_x`, which gives (i); and `U_FP_x = U′_FP_x`, with `U′_F` commuting with `P_x`. (ii) is F1(c). (iii) `U_FY = U_FP_xY = U′_FY`, and `YU_F = YP_xU_F = YU_FP_x = YU′_FP_x = YP_xU′_F = YU′_F`. Each factor of `U′_F` commutes with `Y`: the `H′_C` act on supports disjoint from that of `Y` and are even; the electric factors of other links are disjoint and even; those of the six links commute with `Y` by hypothesis. So `U_FY = YU_F` and `α(Y) = Y`. ∎

A plaquette gate through a link at `x` acts on that register by other operators than `φ`, so Theorem Z0 is stated for the base tick only, as are the dark witnesses of `VC1_5_DRAFT.md` (its section 6: "All witnesses are for the base tick").

### 3.2 Exact zero modes of charge 3

**Theorem Z.** Let `m ∈ {3, 4, 5, 6, 7}`. Put `n_0 = (m − 3)/2` for odd `m` and `n_0 = max(0, m − 5)` for even `m`. Let `S ⊆ {4, 5}` with `|S| = n_0`, and `T = {1, 2, 3}`. Let `x` be a site, `ℓ_1, …, ℓ_6` its links and `y_s` the other end of `ℓ_s`. Put
\[
X=c^\dagger_{x,1}c^\dagger_{x,2}c^\dagger_{x,3}\prod_{s=1}^{6}r^{\ell_s,x\dagger}_1r^{\ell_s,x\dagger}_2r^{\ell_s,x\dagger}_3\,r^{\ell_s,y_s}_3r^{\ell_s,y_s}_2r^{\ell_s,y_s}_1,\qquad
\Pi=\prod_{s=1}^6\Pi[p_{\ell_s,x}=n_0],\qquad
\Psi=P_x\,X\,\Pi\,P_x .
\]
(i) `Ψ` is local, fermion odd and homogeneous, with charge `21` at `x`, `−3` at each `y_s`, and total `U(1)_N` charge `3`.
(ii) `Ψ ≠ 0`.
(iii) `α(Ψ) = Ψ` for the base tick, for every `ε, μ`, and for every `τ_E` if `m` is odd, `τ_E = 0` if `m` is even.
(iv) The tracial state `τ` is stationary under every update, gauge invariant and cell symmetric; `τ(Ψ^*Ψ) > 0`; and `Ũπ(Ψ)Ω = π(Ψ)Ω`. So `ψ = Ψ/τ(Ψ^*Ψ)^{1/2}` meets L2(0): an excitation of charge 3 at quasi-energy exactly 0. `Ψ^*` gives charge `−3`.
(v) Every gauge transform `Ad V_z(g)(Ψ)` and every lift `β_g(Ψ)` is conserved too. The span of the orbit of `Ψ` under the gauge groups at `x, y_1, …, y_6` is a finite-dimensional space of conserved fermion-odd operators of total charge 3, and it contains an irreducible multiplet of these groups.

*Proof.* (i) `c_{x,k}^†` has charge `+1` at `x`; `r^{ℓ,x†}_k` raises `p_{ℓ,x}`, so it has charge `+1` at `x`; `r^{ℓ,y}_k` lowers `p_{ℓ,y}`, so it has charge `−1` at `y`. So `X` has charge `3 + 6·3 = 21` at `x` and `−3` at each `y_s`. `P_x` and `Π` are gauge invariant (F1(a); end numbers commute with every `Q_z`). The total `21 − 18 = 3` is the matter change, as Z-U requires. Each link factor creates three rishons and destroys three, so `X` acts on the registers. The three matter creators make `X` odd, and every other factor is even.
(ii) Let `v` be a basis vector with matter `S` at `x`, and on each `ℓ_s` the `x`-end `S` and a `y_s`-end `Y_s ⊇ T` with `|Y_s| = m − n_0`; anything elsewhere. This exists: `T ∩ S = ∅`, and `m − n_0` is `3, 4, 4, 5, 5` for `m = 3, …, 7`. `v` is flavour-locked at `x`, so `v ∈ F_x` (F1(d)), and `Πv = v`. `Xv = ±v′`, where `v′` has matter `S ∪ T` at `x`, `x`-ends `S ∪ T` and `y_s`-ends `Y_s ∖ T`. `v′` is flavour-locked at `x`, so `v′ ∈ F_x` and `Ψv = P_xXv = ±v′ ≠ 0`. [check] on one link, the move maps a locked vector to a nonzero locked vector, with `p_x` going `0→3, 0→3, 1→4, 1→4, 2→5` for `m = 3, …, 7`.
(iii) `Ψ = P_xΨP_x`, and `Ψ` acts on the matter at `x` and the six registers at `x`. `X` raises each `p_{ℓ_s,x}` by 3, and `Π` fixes the input value `n_0`. With `f(p) = e^{−iτ_E(p−m/2)^2}`, `f(p_{ℓ_s,x})Ψ = f(n_0 + 3)Ψ` and `Ψf(p_{ℓ_s,x}) = f(n_0)Ψ`. These agree if `τ_E = 0`, or if `n_0 + 3 = m − n_0`, which is the choice `n_0 = (m − 3)/2` for odd `m`. The electric factor of `ℓ_s` uses its source end; if `x` is the target, it is a function of `m − p_{ℓ_s,x}`, and `(m − p − m/2)^2 = (p − m/2)^2`. Theorem Z0(iii) applies.
(iv) `VC1_5_DRAFT.md` Lemma 2.4(a): "`τ∘β = τ` for every automorphism `β` that maps each local algebra into a local algebra". The tick, the gauge automorphisms and the lifts do. `τ(Ψ^*Ψ)` is the normalized trace of a nonzero positive operator. `Ũπ(Ψ)Ω = π(α(Ψ))Ω = π(Ψ)Ω`, so `τ((α(ψ) − ψ)^*(α(ψ) − ψ)) = 0`.
(v) Every gate is gauge invariant, so `α` commutes with each `Ad V_z(g)`; `α` commutes with each `β_g` (Lemma C(i)). The orbit lies in the finite-dimensional local algebra of the star of `x`, so its span carries a finite-dimensional unitary representation of the product of the seven groups. The local `U(1)` characters are those of `Ψ`, so total charge 3 and oddness persist, and `α` is the identity on the span. Complete reducibility (cited) gives an irreducible summand. ∎

**Corollary Z1 (no charge-weighted spectral no-go).** CH1-5U-q(L2(δ)) holds for every `δ ≥ 0`: take `m ∈ {3, …, 7}`, the base tick, the tracial state and `ψ` of Theorem Z. So every statement of the form "for some `|q| ≥ 3` and some `δ_q > 0`, no stationary, gauge-invariant, cell-symmetric state of an `L5-U` law has a local fermion-odd `ψ` of charge `q` with `ω(ψ^*ψ) = 1` and `ω((α(ψ) − ψ)^*(α(ψ) − ψ)) < δ_q^2`" is false for `q = ±3`. The same construction with all five flavours at `m = 5`, `n_0 = 0`, refutes it for `q = ±5` (`f(0) = f(5)`).

*Remarks.* (1) With one flavour, moving `p_{ℓ,x}` from `n_0` to `n_0 + 1`, the same proof gives exact zero modes of charge 1 for every `m`: with any `τ_E` and `n_0 = (m − 1)/2` for odd `m`, and with `τ_E = 0` for even `m`. (2) For `m ∈ {1, 2, 8, 9}`, `p_{ℓ,x}` takes at most three values, so no star absorbs a locked move of charge 3. A product of three separated charge-1 zero modes is a conserved operator of charge 3, but it is three objects. (3) *Where it stops.* The excitation does not move. Lemma G gives `ω(Ψ_y^*α^n(Ψ_x)) = 0` for disjoint stars, and Theorem Z0(ii) admits no hop at a frozen star. `LIT_SMG.md` section 9 warns: "Existence of an operator with the right charge does not establish a particle pole, residue or mass." Here the operator even has an exact quasi-energy, and it is still not a particle. So L2 is met by a static defect, and CH1-5U-q(L2) says nothing about CH1-5U-i. (4) The frozen stars are an exact block result of the kind `LIT_SMG.md` section 15 holds up as the standard for "what a rigorous SMG block proof should look like", with one difference: they are conserved by the law's own tick.

**Corollary F2 (all-frozen witnesses for VC1, even `m`).** Let `m = 2n`, `n ∈ {1, 2, 3, 4}`. Choose sets `A_x ⊆ {1, …, 5}` with `|A_x| = n`, and let `v` be the product basis vector with matter `A_x` at each site `x` and, on each link `ℓ = (x, y)`, `x`-end `A_x` and `y`-end `A_y`. Let `Φ` be its state and `ω_F = Φ∘E`. Then `ω_F` is stationary under the base tick (any `ε, μ, τ_E`), gauge invariant, cell symmetric and pure on `𝔄^G`. Its filling is `n = m/2` and `Q_x = 7n`. It does not depend on the sets `A_x`.

*Proof.* Every site is flavour-locked with its six ends, so every hop annihilates the finite restrictions of `v` (F1(c), (d)), and `W_E` multiplies them by a phase. As in the proof of `VC1_5_DRAFT.md` Theorem U3, `Φ∘α = Φ`, and Lemma 1.1(c), (d) there make `ω_F` stationary and gauge invariant. Two choices of sets differ by a flavour permutation `π_x` at each site. `V_x(π_x)` acts by the same permutation on the matter at `x` and on each of its six `x`-ends, so it maps one locked vector to `±` the other. If `v′ = Vv` with `V = ∏_xV_x(π_x)`, then `Φ′∘E = Φ∘Ad V^*∘E = Φ∘E`, because every gauge unitary fixes every `E(A)` (Lemma 1.1(a)). `β_g` maps `v` to `±` a locked vector of the same kind (Lemma C(ii) keeps flavours), so `ω_F∘β_g = Φ∘β_g∘E = ω_F` by Lemma 1.1(d) and the independence just shown. Purity on `𝔄^G` follows as in Theorem U3's proof, with `P_S = ∏_{x∈S}Π[N_x = n]∏_{ℓ∈L(S)}Π[p_{ℓ,src} = n]`, `W_x = Λ^n(C^5_x) ⊗ ⊗_{ℓ∋x}Λ^n(C^5_{ℓ,x})` and `H_{x,j} = n_{x,j} + Σ_{ℓ∋x}n^{ℓ,x}_j`: the joint eigenvalues `7` for `j ∈ A_x` and `0` otherwise force all seven factors at `x` to hold exactly `A_x`, so the joint eigenspace is one-dimensional, and Lemmas 2.2 and 2.3 of `VC1_5_DRAFT.md` apply. `N_x = n` is gauge invariant and sharp in `Φ`. ∎

This agrees with `VC1_5_DRAFT.md` Theorem U2: `q − 3m = 7n − 6n = n`. Theorem U3 gave reading-P witnesses at fillings 0 and 5 only; Corollary F2 adds filling `m/2` for every even `m`.

---

## 4. L3: dressed correlations need electric coherence

**Lemma E (number coherence is necessary).** Let `ω` be gauge invariant and *electrically diagonal*: `ω∘Ad e^{iθp_{ℓ,z}} = ω` for every link end. Then `ω∘Ad e^{iθN_z} = ω` for every site `z`. Let `ψ` be local and fermion odd, `D` local with `[D, N_z] = 0` for every `z`, and `n ∈ Z`, and suppose `M(ψ_x) ∩ M(α^n(ψ_y)) = ∅` (at fixed `n` this holds once `|x − y|` is large, by the light cone of section 5.1). Then `ω(ψ_x^*Dα^n(ψ_y)) = 0`. So in an electrically diagonal state no fermion-odd field of any charge is light in the sense L3.

*Proof.* `e^{iθN_z} = e^{iθQ_z}∏_{ℓ∋z}e^{−iθp_{ℓ,z}}`, a product of commuting unitaries, each of whose adjoint actions fixes `ω`. Decompose `ψ_x^*`, `D` and `α^n(ψ_y)` into components with definite matter changes (Lemma 1.2(b)). `D` has `δN = 0`. Every component of `ψ_x` has total matter change equal to the total charge of `ψ`, which is odd (Lemma 1.2(a), (b)); its `δN` vanishes off `M(ψ_x)`. The components of `α^n(ψ_y)` have `δN` vanishing off `M(α^n(ψ_y))`, which is disjoint from `M(ψ_x)`. So on `M(ψ_x)` each component of the product has the `δN` of a component of `ψ_x^*`, whose sum is `−q ≠ 0`. A component `Y` with `δN_z ≠ 0` has `ω(Y) = e^{iθδN_z}ω(Y)` for all `θ`, so `ω(Y) = 0`. ∎

**Corollary E1 (no stationary state on file carries a dressed light fermion).** The tracial state `τ`, the states `ω_t` of `VC1_5_DRAFT.md` Theorem U1, the states `ω_m` of Theorem U3 and their full-matter partners, and `ω_F` of Corollary F2 are electrically diagonal. So in none of them is any fermion-odd field, of any charge, light in the sense L3.

*Proof.* `τ` and `ω_t` restrict to the normalized trace on every register, which every register unitary fixes. `Φ_m` and `Φ` of Corollary F2 are vector states of basis vectors with sharp end numbers, so `Ad e^{iθp}` fixes them. Each `p_{ℓ,z}` is gauge invariant, so `Ad e^{iθp}` commutes with every `Ad V_z(g)` and with the gauge average `E`; hence `Φ∘E∘Ad e^{iθp} = Φ∘Ad e^{iθp}∘E = Φ∘E`. ∎

The next lemma is the operator-norm form of the coherence gap of `Y2W_DRAFT.md` Theorem W2, which reads: "On the `L5-U` register in sector `m`: `(U^{jk})^2 = 0` for all `j, k`; ... and `κ(ω) ≤ 1/2` for every state", with equality of all singular values in W2(ii): "`ω(𝐔) = ±V/2` (all singular values `1/2`)".

**Lemma W2′ (no link state is more than half a unitary).** For every state `λ` of one `L5-U` register, in any sector `m`, the matrices `u(λ)_{jk} = λ(U^{jk})` and `u^†(λ)_{jk} = λ(U^{jk†})` have operator norm at most `1/2`. At `m = 5` the bound is attained (Theorem W2(ii)).

*Proof.* (Square zero; rebuilt.) Let `X` act on a finite-dimensional space with `X^2 = 0`, and `ψ` be a unit vector. Write `ψ = a + b` with `a ∈ ker X` and `b ⊥ ker X`. Then `Xψ = Xb ∈ ran X ⊆ ker X`, which is orthogonal to `b`, so `⟨ψ, Xψ⟩ = ⟨a, Xb⟩` and `|⟨ψ, Xψ⟩| ≤ ‖X‖‖a‖‖b‖ ≤ ‖X‖/2`. Density matrices follow by convexity. Now take unit `α, β ∈ C^5` and put `X = r^y(ᾱ)r^{x†}(β)`, with `r^y(ᾱ) = Σ_jᾱ_jr^y_j` and `r^{x†}(β) = Σ_kβ_kr^{x†}_k`. Then `⟨α, u(λ)β⟩ = λ(X)`. `X` conserves the rishon number, so it acts on the register. The two factors anticommute and `r^y(ᾱ)^2 = 0`, so `X^2 = −r^y(ᾱ)^2r^{x†}(β)^2 = 0`. Each factor is a single-mode operator of a unit mode, so `‖X‖ ≤ 1`. Hence `|⟨α, u(λ)β⟩| ≤ 1/2`. The same holds for `X^†`. ∎ [check] (7): for `m = 1, 3, 5, 7, 9` and random `α, β`, the numerical radius of `X` equals `‖X‖/2` and `X^2 = 0`.

**Corollary W2′.1 (product link states give exponentially small string correlations).** Let `γ` be a lattice path `y = z_0, z_1, …, z_L = x` with links `ℓ_i = {z_{i−1}, z_i}`. Let `T_i` be the transport matrix of `ℓ_i` from `z_{i−1}` to `z_i`: `T_i^{jk} = U^{jk}_{ℓ_i}` if `z_{i−1}` is the source, and `T_i^{jk} = (U^{kj}_{ℓ_i})^†` if it is the target, so that `c^†_{z_i}T_ic_{z_{i−1}}` is a term of `h_{ℓ_i}`. Put `B_γ = Σ_{jk}c^†_{x,j}(T_L⋯T_1)^{jk}c_{y,k}`, which is gauge invariant. If `ω` restricted to the matter at `x, y` and the registers of `γ` is a product `μ ⊗ λ_1 ⊗ ⋯ ⊗ λ_L`, then `|ω(B_γ)| ≤ 5·2^{−L}`.

*Proof.* The operators of distinct registers commute and commute with matter, so `ω(B_γ) = Σ_{jk}M_{jk}(t_L⋯t_1)_{jk}`, with `M_{jk} = μ(c^†_{x,j}c_{y,k})` and `t_i = λ_i(T_i)`. For unit `a, b`, `Σa_jb_kM_{jk} = μ(c^†_x(a)c_y(b))` has modulus at most 1, so `‖M‖ ≤ 1` and its trace norm is at most 5. Hölder's inequality and Lemma W2′ give `|ω(B_γ)| ≤ 5∏‖t_i‖ ≤ 5·2^{−L}`. ∎

So a charge-1 field dressed by strings is never light in the sense L3 in a state that is a product over the links of the strings, whatever the matter state. This is the "perimeter law" of string dressings in its sharpest lattice form, forced by the finite register; it does not depend on the charge's sign or on `m`. Lemma E and Corollary W2′.1 say the same thing from two sides: a dressed light charged fermion needs a stationary state whose link sector is electrically coherent and entangled along long strings.

---

## 5. The proposed no-go tools, tested

The brief names three tools for a no-go: locality and light cones, the finite register, and a charge-weighted spectral bound. A fourth one is on file: the pinned charge.

**5.1 The light cone does not see charge.** For an update of `L5-U` form, E1 gives a radius `r_U` (two cube layers, the electric layer and the added layers) such that `α(A)` is supported within distance `r_U` of the support of `A`, for every local `A`. So `α^n(A)` lies within `|n|r_U`, whatever the charge of `A`. *Exact failing step* of a light-cone no-go for `|q| ≥ 3`: the cone constrains supports, not quasi-energies or correlation strengths. Under L2 it is refuted outright: the charge-3 `Ψ` of Theorem Z satisfies the cone trivially (`α(Ψ) = Ψ`) and sits at quasi-energy 0. Under L3 the cone gives the same constraint for charge 1 as for charge 3, so any no-go from the cone alone would remove every light charged fermion, of every charge, and would be a statement about CH1 as a whole on `L5-U`, not about `|q| ≥ 3`.

**Lemma T (the register carries a triple across one link exactly when `3 ≤ m ≤ 7`).** For a link `ℓ = (x, y)`, put `A_ℓ = φ_{ℓ,y}^†φ_{ℓ,x}` (the first term of `h_ℓ`, Lemma F1(b)) and `T_ℓ = A_ℓ^3`. Then `T_ℓ = (φ_{ℓ,y}^†)^3(φ_{ℓ,x})^3` is gauge invariant, moves three matter units from `x` to `y` and three rishons from the `y`-end to the `x`-end, and `T_ℓ ≠ 0` exactly when `3 ≤ m ≤ 7`.

*Proof.* `φ_{ℓ,y}^†` commutes with `φ_{ℓ,x}` (adjoint of F1(b)), which gives the factorization; gauge invariance is F1(a). *Nonzero for `3 ≤ m ≤ 7`.* Take a basis vector with matter `{1, 2, 3}` at `x`, no matter at `y`, `x`-end `S′ ⊆ {4, 5}` with `|S′| = max(0, m − 5)` and `y`-end `Y ⊇ {1, 2, 3}` with `|Y| = min(m, 5)`; then `|S′| + |Y| = m`. Since `r` and `c` commute, `(φ_{ℓ,x})^3 = Σ_{k_1k_2k_3}r^{x†}_{k_1}r^{x†}_{k_2}r^{x†}_{k_3}c_{x,k_1}c_{x,k_2}c_{x,k_3}`. On this vector only the six orderings of `{1, 2, 3}` survive, and each equals `r^{x†}_1r^{x†}_2r^{x†}_3c_{x,1}c_{x,2}c_{x,3}`, because reordering both triples by the same permutation costs its sign twice. That operator is nonzero here: the `x`-end lacks `1, 2, 3` and has room, `|S′| + 3 ≤ 5`. Likewise `(φ_{ℓ,y}^†)^3 = Σc^†_{y,j_1}c^†_{y,j_2}c^†_{y,j_3}r^y_{j_1}r^y_{j_2}r^y_{j_3}`, and on the image each 3-subset `J ⊆ Y` contributes `6c^†_{y,J}r^y_J`; distinct `J` give orthogonal nonzero vectors. *Zero otherwise.* `T_ℓ` raises `p_{ℓ,x}` by 3, and `p_{ℓ,x}` ranges over `K_m = min(m, 10 − m) + 1` consecutive integers (`Y2W_DRAFT.md` proof of Theorem W1: "In sector `m`, `N^x_ℓ` takes the values `max(0, m − 5), …, min(5, m)`: `K_m` consecutive integers"), so `T_ℓ = 0` when `K_m ≤ 3`, that is `m ∈ {1, 2, 8, 9}`. ∎ [check] `max|T_ℓ| = 36` for `m = 3, …, 7` and `0` otherwise.

**5.2 The register does not stop charge 3.** `CH1.md` Corollary U-T″: "an anomaly-free `U(5)` family is carried at one site exactly when `2 ≤ m ≤ 8`." Lemma T: a charge-3 composite crosses one link when `3 ≤ m ≤ 7`, by the part of `h_ℓ^3` that moves three matter units. CH1-5U-q quantifies over `m`. *Exact failing step* of a register no-go: "a link cannot carry the flux of a charge-3 composite" is false for `3 ≤ m ≤ 7`. (For `m ∈ {1, 9}` the bound of Lemma U-T, width 11 at one site, is real, but it concerns the line family's charge 15 at one site, and `m` is free.)

**5.3 A charge-weighted spectral bound is false.** Corollary Z1.

**5.4 The pinned charge decides only L1.** Lemma G kills undressed correlations for every charge. Under L3 the bilocal is gauge invariant, its charge vector is zero, and Lemma G gives nothing.

**Verdict.** None of the four tools gives a no-go for `|q| ≥ 3` that is not also a no-go for `|q| = 1`. **No named failing step for `L5-U`.**

---

## 6. CH1-5U-q under L3: open after three failed attacks each way

**Lemma CH1-5U-q(L3) (open).** There exist an update of `L5-U` form, a stationary, gauge-invariant, cell-symmetric state `ω`, and a local fermion-odd `ψ` of total charge `q` with `|q| ≥ 3` that is light in the sense L3, with dressed correlations of free-Weyl form.

*Relation to CH1-5U-i.* CH1-5U-i with hypothesis IR read through L3 implies it, since the `10_u` has charge `u` with `|u| ≥ 3` (`CH1_5U_DRAFT.md` Lemma Q1). So its negation would refute CH1-5U-i under L3.

*Attacks that try to prove it.*
- **P1, quasi-free import** (`CH1_5U_DRAFT.md` Attack 4). It fails twice. Lemma Q1′ there: "Its light excitations are one-body modes near the cuts ... particles, created by combinations of the `c^†_{x,j}` (charge `+1`), and holes", so only charge `±1`. And `LW1_5.md` inferred definition 4: "A free tick is an auxiliary c-number replacement of link operators; it is not the interacting tick or its vacuum." Lemma W2′ adds that every link state gives `‖λ(𝐔)‖ ≤ 1/2`, half the norm of that replacement.
- **P2, frozen zero modes** (Theorem Z). Exact charge-3 excitations at quasi-energy 0 exist, but they are static: a frozen star admits no hop (Theorem Z0(ii)), the charge is pinned (Lemma G), and the state that carries them, `τ`, is electrically diagonal. It fails at Lemma E.
- **P3, the stationary invariant states on file, and product link states.** `τ`, `ω_t`, `ω_m` and its partner, and `ω_F` are electrically diagonal (Corollary E1), so they fail at Lemma E, for every charge. In every state that is a product over the links of the strings, string-dressed charge-1 correlations are at most `5·2^{−L}` (Corollary W2′.1).

*Attacks that try to refute it.*
- **R1, the light cone** (section 5.1). It fails at the step "a support bound limits quasi-energies or correlation strength"; the bound is the same for every charge.
- **R2, the finite register** (section 5.2). It fails at Lemma T and Corollary U-T″: charge-3 composites sit at one site for `2 ≤ m ≤ 8` and cross one link for `3 ≤ m ≤ 7`.
- **R3, a charge-weighted spectral bound** (section 5.3). It fails at Theorem Z.
The pinned charge (section 5.4) decides L1 only.

*What any proof needs.* A stationary, gauge-invariant, cell-symmetric state that is not site-number diagonal (Lemma E) and, for string dressings, not a product over the links of long strings (Corollary W2′.1). Both requirements are word for word the same for charge 1. So, as far as these tools reach, the clause `|q| ≥ 3` adds nothing to what every light charged fermion of `L5-U` already needs. The deciding question is the gauge sector's: does any `L5-U` law have a stationary invariant state with long-range electric coherence? That is VC1's state question and GA2's bridge Y2, where Theorem W2 of `Y2W_DRAFT.md` is the per-link form of the same obstruction.

---

## 7. Four-test check

Tests: (1) states or fixes a part's target; (2) open-ended, so a part can add to it; (3) settles a downstream physics question by premise; (4) adds structure or constants its own reasons do not need. Nothing is adopted.

| Item | (1) | (2) | (3) | (4) | Result |
|---|---|---|---|---|---|
| a. L1, undressed correlations (the text's reading) | pass: CH1's own wording | pass | fails: by Corollary G1 it settles CH1 negatively on every law with exact local gauge invariance, before any dynamics | pass | not usable; recorded |
| b. L2(δ), spectral, as the brief suggests | pass: fixes no state and no charge | pass: one inequality, `δ` stated | pass | pass: uses only `ω`, `α` and the GNS space | passes; CH1-5U-q(L2) is proved (Theorem Z), and it implies nothing for CH1-5U-i, since a static defect meets it |
| c. L3, dressed, with `‖D‖ ≤ 1` and `[D, N_z] = 0` | pass | pass: one fixed class of dressings, quantified existentially | conditional: norm-bounded local dressings may rate charged fermions in a phase with a massless gauge field as not light (string dressings decay by a perimeter law, exponentially in link-product states by Corollary W2′.1), so it may settle that case by premise | pass: the dressing is forced by Lemma G, the norm bound by rescaling, the number clause by the cancelling dressing of section 1.3 | passes 1, 2, 4; 3 conditional, disclosed; the working reading of sections 4 and 6, not proposed |
| d. The frozen subspace `F_x` | pass: defined by the law's own operators | pass | pass | pass | a definition; used |
| e. CH1-5U-q(L3) as an open lemma | pass: a consequence of CH1-5U-i under L3, posed as a question | pass: one statement | pass: not a premise of any part | pass | recorded as open |

No change to `L5-U`, to CH1-5U-i or to any working-set entry is proposed.

---

## FINISH

**Proved here (pass 1, not distilled or refereed).**
- Lemma 1.2: local charge vectors and components; under every update of `L5-U` form the charge vector of an operator is static.
- Lemma G and Corollary G1: in a gauge-invariant state every correlation between separated charged operators vanishes, at every time. So no fermion-odd field of any charge, `±1` included, has undressed Weyl correlations (tails `o(R^{−3})`). CH1-5U-q and CH1-5U-i are false under the literal reading L1, for the same reason on every law with exact local gauge invariance.
- Lemma F1 and Theorem Z0: frozen stars. Every hop at a frozen star vanishes; the base tick conserves `P_x` for every `m` and every constant; every operator inside a frozen star that respects the electric layer is conserved.
- Theorem Z and Corollary Z1: for `3 ≤ m ≤ 7`, an exactly conserved local fermion-odd operator of `U(1)_N` charge 3, and an irreducible multiplet of them; in the tracial state an excitation at quasi-energy exactly 0. CH1-5U-q(L2(δ)) holds for every `δ ≥ 0`, and no charge-weighted spectral bound fails `L5-U` (also charge 5 at `m = 5`).
- Corollary F2: for even `m`, a stationary, gauge-invariant, cell-symmetric state, pure on `𝔄^G`, at filling `m/2`.
- Lemma E and Corollary E1: dressed correlations vanish in electrically diagonal states, and every stationary invariant state on file is one.
- Lemma W2′ and Corollary W2′.1: every state of one register has `‖λ(𝐔)‖ ≤ 1/2`; in states that are products over the links of a string, string-dressed charge-1 correlations are at most `5·2^{−L}`.
- Lemma T: the register carries a triple across one link exactly when `3 ≤ m ≤ 7`.

**Counterexamples.**
- To "a charge-weighted spectral bound forbids light fermion-odd excitations with `|q| ≥ 3` on `L5-U`": Theorem Z (`q = ±3`, `3 ≤ m ≤ 7`) and its five-flavour form (`q = ±5`, `m = 5`).
- To "the finite register stops charge-3 composites from moving": Lemma T.
- Refuted as a route, not as a stated claim: a light-cone argument that separates `|q| ≥ 3` from `|q| = 1` (section 5.1); the cone does not see charge, and Theorem Z sits inside it at quasi-energy 0.

**Open, by name.**
- **CH1-5U-q(L3)** (section 6). Attacks to prove it failed: quasi-free import (Lemma Q1′; inferred definition 4), frozen zero modes (Lemma E), the states on file and link-product states (Lemma E, Corollary W2′.1). Attacks to refute it failed: light cone, register (Lemma T), spectral bound (Theorem Z).
- **The reading of "light" in hypothesis IR** (owner question). L1 is unusable on every gauge law (test 3); L2 is met by static defects; L3 passes with test 3 conditional. A Dirac-type dressing is built from group-valued link variables, which no state of an `L5-U` link approximates (Lemma W2′); a charge-sector prescription is not attempted here.
- Inherited, unchanged: CH1-5U-i, AM-5, CH1-ii, CH1-5O-i, VC1-5U-odd, LW1-5U-PS7, Y2-W.

**What changes downstream.**
- `CH1_5U_DRAFT.md` section 5: CH1-5U-q as written is false for every charge (Corollary G1), and so is CH1-5U-i under the same reading. Line 232's "a proof that every light fermion of such a state has charge `±1` refutes CH1-5U-i" holds there only vacuously. Any use of CH1-5U-q needs a dressed reading; this file states L3.
- `CH1.md` inferred definition 8 is now a theorem (Lemma G): on every law with exact local gauge invariance, undressed charged correlators vanish at all times, so hypothesis IR must be dressed on `L5-U`, `L5-O` and `L_cube` alike.
- **No named failing step for `L5-U`** from CH1-5U-q. The tools the brief names do not separate `|q| ≥ 3` from `|q| = 1` (section 5), and the spectral reading holds at charge 3 exactly (Theorem Z). The law stays live under `TOE_ASSEMBLY.md` section 3.5.
- The asymmetry "charge 1 is light at quasi-free points, charge `≥ 3` is not" (`CH1_5U_DRAFT.md` Lemma Q1′, Attack 4) lives in the auxiliary free tick. In the law itself no state on file carries a dressed light fermion of any charge (Corollary E1), and every link state gives `‖λ(𝐔)‖ ≤ 1/2`, half the norm of a c-number link (Lemma W2′). For CH1 on `L5-U` the next question is the gauge sector's: a stationary invariant state with long-range electric coherence. This ties CH1-5U-i to VC1 and to GA2's bridge Y2.
- VC1: frozen stars are local conserved projectors of the base tick for every `m` and every constant (Theorem Z0). For even `m` they give a reading-P witness at filling `m/2` (Corollary F2), beside Theorem U3's fillings 0 and 5. Like those it is dark and electrically diagonal; by the proof of Corollary U3′, under PS-3h5 its sharp `N_x = m/2` forms a record at every site at tick 1.
- GA2 and Y2: Lemma W2′ is Theorem W2 in operator-norm form, `‖λ(𝐔)‖ ≤ 1/2` for every state of one register, attained at `m = 5`; Corollary W2′.1 turns it into a perimeter bound `5·2^{−L}` for string observables in link-product states.
