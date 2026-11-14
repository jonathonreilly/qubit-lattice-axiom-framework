# Y2-W: a small-coupling window for L5-U, pass 1

Written 2026-11-05 by a Claude Opus 5.5 subagent, as a pass-1 lane of the TOE assembly (part GA2, item Y2-W of `GA2_Y2_DRAFT.md`). Method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation (`check_y2w.py`, output `out.txt`, in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-yalow-de8f06/bd9fd3c1-9024-4004-87d2-e8917bcfe6a3/scratchpad/y2w/`; about 2 s, a few MB, floating point, largest space `10^4`). A check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local branch `toe-assembly-local` (the commit the lane brief names for `claude/toe-assembly`) | `7d2b20d298` |
| `origin/claude/ym4d-hard-route` (read with `git show` only, after `git fetch -q origin`) | `86b3c42f2e` |

Files read at those commits, by line. This folder: `GA2_Y2_DRAFT.md` lines 1-215 (all); `TOE_ASSEMBLY.md` lines 13-23 (axioms), 95-220 (section 3, with 3.4 and 3.5), 369-396 (GA1, GA2), 538-562 (section 6, Y1-Y5); `LW1_5_DRAFT.md` lines 1-22, 45-62 (one five-mode site), 148-200 (Lemma Q, Theorem G), 252-264 (Theorem U), 280-348 (section 7, section 8), 378, 424, 464; `LW1.md` lines 14-24 (free data), 30-70 (matter, links, ticks), 136-171 (statement of `L_cube`), 389-463 (E1-E6), 476 (GA1-P). YM branch, `.claude/science/physics-loops/ym4d-hard-route-20261030/parts/upper-chain.md` (last changed `4d58aa4f7f`): lines 220-224 (model) and 276-284 (Theorem 2), found by grep for "small field" and "large field" (hits at lines 36, 171, 999 read in passing).

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". PS-6r, PS-5 and the law `L5-U` are read plainly. One possible change of law data is recorded (section 5.3) and not proposed.

**Working set used, by name.** PS-5 (five modes per site), PS-6 and PS-6r (finite link registers), through the two five-mode laws of `LW1_5_DRAFT.md` section 8.1. PS-7r only through its sentence "the vacuum is the state VC1 builds". Results used, cited by name: Theorem U, Lemma Q and section 8.1 of `LW1_5_DRAFT.md`; Theorem E1 of `LW1.md` (only to say that states of the law are states of the quasi-local algebra); Theorem N, Corollary N3', Corollary N5, T0-start and T0-rate of `GA2_Y2_DRAFT.md`.

**Inputs from outside the working set.** Standard mathematics, rebuilt in the text: the spectral theorem in finite dimension, Cauchy-Schwarz, Jordan-Wigner, the fact that pairwise anticommuting Hermitian involutions `A_i` satisfy `Σ_i ω(A_i)^2 ≤ 1`. Standard mathematics cited, not rebuilt (remarks only): the dimensions of `Gr(5, 10)` (50) and `SO(20)/U(10)` (90). One YM-branch result is quoted as a guide and never used as a proof step: upper-chain Theorem 2, "Also <s_p> <= C_5/beta". Literature context, credited from memory and never load-bearing: Kogut-Susskind Hamiltonian lattice gauge theory; quantum link models (Horn; Orland-Rohrlich; Chandrasekharan-Wiese, Nucl. Phys. B 492 (1997)); D-theory (Brower-Chandrasekharan-Wiese, Phys. Rev. D 60 (1999); Brower-Chandrasekharan-Riederer-Wiese, Nucl. Phys. B 693 (2004)); coherent states of compact groups and their classical limits (Perelomov; Berezin; Lieb).

---

## 0. The question, quoted

`GA2_Y2_DRAFT.md` line 195: "**Y2-W** (`L5-U` first): whether the law's free constants give a small coupling at some scale, so that GA2(a)'s window `a << r << Λ^{-1}` is non-empty, with a register of fixed dimension `C(10, m)`."

`TOE_ASSEMBLY.md` line 387, GA2(a): "For each simple factor `G_i` with negative one-loop beta coefficient, the framework's gauge sector at scales `a << r << Lambda_i^{-1}` agrees with continuum `G_i` Yang-Mills with the matter of CG1, at the running coupling `g_i(r)`, up to errors `O((a/r)^p) + O(g_i(r)^4)`". The same line: "For the abelian factor, the corresponding statement holds as an effective lattice theory at scales above `a`, with no `a -> 0` limit required".

`LW1_5_DRAFT.md` line 318, the law: "**The variant `L5-U`.** Items 1, 4, 5, 8, 10, 11 unchanged; items 2-3 replaced by the rishon register of Theorem U (free datum `m`, `1 ≤ m ≤ 9`) and the hop `h^U_ℓ`; item 6 by `W_E = ∏_ℓ e^{−iτ_E(n^ℓ_{x\text{-end}} − m/2)^2}`". Line 254, Theorem U: "ten complex rishon modes `r^{ℓ,y}_j`, `r^{ℓ,x}_k` (`j, k = 1, …, 5`), fermionic among themselves, in an ordinary tensor factor that commutes with matter, restricted to a sector of fixed total rishon number `m`, `1 ≤ m ≤ 9`. Put `U_ℓ^{jk} = r^{ℓ,y}_j r^{ℓ,x†}_k`". Line 316, free data: "`ε, μ` with `0 ≤ μ < 2ε < π`; the register `R`; `τ_E` (zero allowed); the plaquette class (open); `ω_0`." Line 310: "**Plaquette class.** OPEN as law data".

`TOE_ASSEMBLY.md` line 214 (section 3.5): "The owner chose: **keep both live.** MT1, GA1 and CG1 are developed on both laws until one fails at a named step."

## 0.1 Outcome in one paragraph

**Open, after three named attacks.** Neither (A) nor (B) is proved. **The definition GA2 needs** is a correlator statement: at some block scale `r = a_{k0}`, the framework's gauge-invariant block-loop correlators, in the state VC1 supplies, equal those of a measure in T0-start's class at coupling `g ≤ g_*`, up to `δ` (Definition SC, section 1). It passes the four tests when its parameters (state, block map, loop list, the YM class) are pinned and it is used as a question, not as a premise. A law-internal necessary condition follows from it: Wilson-type plaquette loops must be nearly a nonzero scalar in the state (Definition SC-loop, Lemma 0). **Proved, for every value of the free constants, every plaquette class and every state** (these are kinematic facts of the register): (i) the flux floor (Lemma F, Theorem W1): every `L5-U` loop that raises the bounded `U(1)` flux of a link obeys `D ≥ 2/K_m^2 ≥ 1/18`, so the fine scale of `L5-U` is never `U(5)` Wilson at small coupling; through a surface crossed by `n` links the floor is `2/(n(K_m − 1) + 1)^2`, so it decays as the scale grows; (ii) the coherence gap (Theorem W2): one `L5-U` link has coherence `κ ≤ 1/2` in every state; `L5-O[S_±]` has `κ ≤ 1/10`, and this is attained. **What fails.** Attack 1 (the flux floor as a no-go) fails for `SU(5)`: loops that see `SU(5)` but not the `U(1)` phase raise no bounded grading. Attack 2 (the bare corner `τ_E → 0` with a plaquette class) fails at the step "the corner is classical": the floors above do not depend on the constants. Attack 3 (the zoom as a register knob) fails at the step "the block state is a product of aligned coherent states", which is the small-coupling statement itself. **Smallest exact sub-lemma:** Y2-W-L (section 4): whether `U(1)`-blind block loops of `L5-U` meet SC-loop at some scale; its failure for all constants proves (A). **`L5-O`.** Its free datum `R` contains `S_+^{⊗k}`, with coherence `≥ k/(k+9)` at a state on the `SO(10)`-valued locus. So option (a1) answers the fine-scale classicality question there (to `O(1/k)`), and leaves the coupling question as a standard bare-coupling question plus T0-start for `SO(10)`. **No named failing step for either law.**

---

## 1. The question made exact

### 1.1 Notation

`L5-U` as in section 0. On each link `ℓ = (x, y)`, `y = x + e_i`, write `N^x_ℓ = Σ_k r^{ℓ,x†}_k r^{ℓ,x}_k` and `N^y_ℓ` likewise, so `N^x_ℓ + N^y_ℓ = m`. `𝐔_ℓ = Σ_{jk} E_{jk} ⊗ U_ℓ^{jk}` is the `5 × 5` link matrix (conventions of `GA2_Y2_DRAFT.md` section 1). For a closed lattice loop `C`, `W_C` is the trace of the ordered product of `𝐔_ℓ` (or `𝐔_ℓ^†` where `C` runs against `ℓ`), with indices contracted at the sites of `C`. For a plaquette `p`, `W_p`. For an operator `X`, `|X|^2 := X^†X`. For a state `ω` and an operator `Y` put

\[
D_\omega(Y):=\omega\big((Y-1)^\dagger(Y-1)\big)+\omega\big((Y-1)(Y-1)^\dagger\big)\ \ge 0. \tag{1.1}
\]

For a commuting variable `w`, `D(w) = 2E|w − 1|^2`. `D_ω(Y)` is small exactly when `Y` and `Y^†` both act on the state almost as `1`.

### 1.2 What GA2 needs

GA2(a) asks agreement "at the running coupling" over the window `a << r << Λ_i^{-1}`. `GA2_Y2_DRAFT.md` Corollary N5 fixes the form: link operators are never Wilson's, so agreement can only be about gauge-invariant correlators. T0-start (quoted there, FINISH block) starts the hard core "at every `k_0`" from "every gauge-invariant, reflection-positive probability measure `μ` on `G`-valued links of `a_{k_0}Z^4`, with Haar reference measure and density in `𝒜_{k_0}(g)` for some `g ≤ g_*`".

**Definition SC (small coupling at scale `r`, the form GA2 needs).** Data: the law with its constants; a state `ω` of the law; a simple factor `G_i` (`SU(5)` for `L5-U`); a block scale `r = a_{k0} = L^{k0}a` of ZM1; a fixed finite list `Λ_r` of gauge-invariant block-loop observables at scale `r`, with an identification `ι` of each with a Wilson-loop function on `G_i`-valued links of `rZ^4` (ZM1-G's identification, normalisations included); `δ > 0`. **SC(r; δ)** holds if there is `μ` in T0-start's class at step `k0` with `g ≤ g_*` such that `|ω(O) − E_μ(ι O)| ≤ δ` for every product `O` of at most two observables of `Λ_r` and their adjoints, both orders mapped to the same commuting product.

**Y2-W, exact.** For `L5-U`, `G_i = SU(5)`, and `ω` the state VC1 supplies: are there constants, a plaquette class and `k0` with SC(`a_{k0}`; `δ`) for a `δ` inside the hard core's error budget? If yes, T0-start and T0-rate give GA2(a) on the window `a_{k0} << r << Λ_i^{-1}`, with `(a/r)^p` replaced by `(a_{k0}/r)^p`. That costs only the fixed factor `(a_{k0}/a)^p`.

The reading "the Euclidean form of the gauge sector at scale `r` lies in T0-start's class" is the case `δ = 0` with `μ` the framework's own Euclidean measure. `GA2_Y2_DRAFT.md` section 4.2 shows such a measure has a band-limited kernel, not a Haar density in a small-field class. GA2 does not need `δ = 0`. So Definition SC, not the Euclidean-form reading, is what GA2 needs.

**Definition SC-loop (law-internal necessary condition).** Fix a class `𝒲_r` of block plaquette observables at scale `r` (for `r = a`, the `W_p`). **SC-loop(r; η)** holds in `ω` if there is `c ∈ C∖{0}` with `D_ω(cW) ≤ η` for every `W ∈ 𝒲_r`.

**Lemma 0 (SC gives SC-loop).** Suppose `Λ_r` contains `Ŵ = cW` with `ι(Ŵ) = w_p := N^{-1} tr U_p`, and `μ` satisfies `E_μ(1 − Re w_p) ≤ ε_μ` for that plaquette. If SC(r; δ) holds with this `μ`, then `D_ω(Ŵ) ≤ 8ε_μ + 6δ`.

*Proof.* `D_ω(Ŵ) = ω(Ŵ^†Ŵ) + ω(ŴŴ^†) − 2ω(Ŵ) − 2ω(Ŵ^†) + 2`. The `μ`-side value is `2E|w|^2 − 4Re E w + 2 = 2E|w − 1|^2`. The two differ by at most `2δ + 4δ`. Since `|w| ≤ 1`: `(Im w)^2 ≤ (1 − Re w)(1 + Re w) ≤ 2(1 − Re w)` and `(1 − Re w)^2 ≤ 2(1 − Re w)`, so `E|w − 1|^2 ≤ 4ε_μ`. ∎

The hypothesis on `μ` is what "small coupling" means at the plaquette level. For Wilson `SU(2)` at the bare level, the branch proves it: upper-chain line 282, "Also <s_p> <= C_5/beta", with line 222, "s_p = 1 - (1/2) Tr U_p". So `ε_μ = C_5/β` there. For the inductive class `𝒜_k(g)` and for `SU(N)` it is a property to confirm on the branch; it is not used as a proof step here.

### 1.3 Four-test check

Tests (`LW1_5_DRAFT.md` line 328): "(1) states or fixes a part's target; (2) open-ended; (3) settles a downstream physics question by premise; (4) adds structure or constants its own reasons do not need."

| Definition | (1) | (2) | (3) | (4) | Result |
|---|---|---|---|---|---|
| SC | pass as a question: it names GA2's input (ZM1-G's hypothesis with T0-start's class) and adopts nothing. As a premise it would fail (1) and (3) | pass once `Λ_r`, `ι`, `δ` and the branch commit of `𝒜_k` are pinned; fails if `Λ_r` may grow to fit a result | pass only with `ω` the state VC1 supplies. "There is a state" would choose the vacuum by premise and fail | pass: block map, loop list and class are each needed by GA2 | passes as a question with its parameters pinned |
| SC-loop | pass: a necessary condition, not GA2's statement | pass: one inequality per observable, `c` quantified, `𝒲_r` fixed | pass. The no-go results below hold for every `ω`, so they need no VC1 input | pass | passes; a no-go from it reaches SC only through Lemma 0 |
| Euclidean-form reading | fails (3) in part: it requires the operator identification that Corollary N5 excludes | | | | not used |

## 2. Exact facts about the `L5-U` registers

### 2.1 The flux floor

**Lemma F (bounded flux floor).** Let `H` be finite-dimensional, `E` Hermitian on `H` with spectrum in the integer interval `{e_0, e_0 + 1, …, e_0 + K − 1}`, and `Y` an operator with `[E, Y] = Y`. Then for every state `ω` on `B(H)` and every `z ∈ C`,

\[
\omega\big((Y-z)^\dagger(Y-z)\big)+\omega\big((Y-z)(Y-z)^\dagger\big)\ \ge\ \frac{2|z|^2}{K^2}. \tag{2.1}
\]

*Proof.* The left side is affine in `ω`, so take `ω` pure, `ψ` a unit vector. Let `P_e` project onto the `e`-eigenspace of `E` (zero for `e` outside the interval). `[E, Y] = Y` gives `YP_e = P_{e+1}YP_e =: B_e`. Put `u_e = P_eψ`, `p_e = ‖u_e‖^2`, so `Σ_e p_e = 1`. Decompose by eigenspace: `‖(Y − z)ψ‖^2 = Σ_f ‖B_{f−1}u_{f−1} − zu_f‖^2` and `‖(Y − z)^†ψ‖^2 = Σ_f ‖B_f^†u_{f+1} − z̄u_f‖^2`. Group the terms by the edge `(e, e+1)`, for `e = e_0 − 1, …, e_0 + K − 1`, with `u = 0` outside the interval. The edge gets `‖B_eu_e − zu_{e+1}‖^2 + ‖B_e^†u_{e+1} − z̄u_e‖^2`. Put `α = ⟨u_{e+1}, B_eu_e⟩`; then `⟨u_e, B_e^†u_{e+1}⟩ = ᾱ`. Projecting each vector on `u_{e+1}` and on `u_e`, the edge term is at least `|α − zp_{e+1}|^2/p_{e+1} + |α − zp_e|^2/p_e` when both `p` are positive. Minimised over `α ∈ C` (at `α = 2zp_ep_{e+1}/(p_e + p_{e+1})`) this is `|z|^2(p_{e+1} − p_e)^2/(p_e + p_{e+1})`. If one `p` vanishes the edge term is `|z|^2` times the other `p`, which is the same formula. So the left side of (2.1) is at least `|z|^2Φ`, `Φ = Σ_e (p_{e+1} − p_e)^2/(p_e + p_{e+1})`, over edges with `p_e + p_{e+1} > 0`. By Cauchy-Schwarz, `(Σ_e|p_{e+1} − p_e|)^2 ≤ Φ · Σ_e(p_e + p_{e+1}) = 2Φ`. The path `p` starts and ends at zero, so `Σ_e|p_{e+1} − p_e| ≥ 2 max_e p_e ≥ 2/K`. Hence `Φ ≥ 2/K^2`. ∎

Every step is finite linear algebra. Lemma F is the state-level form of `GA2_Y2_DRAFT.md` Theorem N: there, a bounded generator forbids an invertible covariant link; here, it forbids any state in which a flux-raising operator acts almost as a nonzero scalar. For an unbounded flux (Kogut-Susskind `U(1)`, `K = ∞`) the floor is zero. [check] (1): for `K = 2, …, 6` the infimum over states of (2.1) at `z = 1` is `1.00, 0.63, 0.44, 0.33, 0.25` for optimised weighted shifts, above `2/K^2`; random raising operators give larger values.

**Theorem W1 (the flux floor of `L5-U`).** Fix `m`, and put `K_m = min(m, 10 − m) + 1 ≤ 6`. For every value of the free constants, every plaquette class, every state `ω` of the law and every `c ∈ C∖{0}`:
(i) for every closed loop `C` that runs through some link `ℓ` exactly once, `D_ω(cW_C) ≥ 2/K_m^2`;
(ii) let `S` be a finite set of `n_S` links with signs `σ_ℓ`, put `Φ_S = Σ_{ℓ∈S} σ_ℓN^x_ℓ`, and let `O` be any operator on finitely many links with `[Φ_S, O] = O` (for example a sum of loops each of net crossing number `+1` through `S`). Then `D_ω(cO) ≥ 2/(n_S(K_m − 1) + 1)^2`.

*Proof.* (i) `[N^x_ℓ, U_ℓ^{jk}] = [N^x_ℓ, r^y_jr^{x†}_k] = U_ℓ^{jk}`, and operators of other links commute with `N^x_ℓ` (ordinary tensor factors, Theorem U). `W_C` contains `𝐔_ℓ` or `𝐔_ℓ^†` once, so `[±N^x_ℓ, W_C] = W_C`. In sector `m`, `N^x_ℓ` takes the values `max(0, m − 5), …, min(5, m)`: `K_m` consecutive integers. The restriction of `ω` to the finite algebra of the links of `C` is a density matrix. Apply Lemma F with `Y = cW_C`, `z = 1`. (ii) `Φ_S` has integer spectrum in an interval of `n_S(K_m − 1) + 1` integers. Apply Lemma F. ∎

The theorem uses no gate of the law. It holds for every plaquette class whatsoever, so no closed class needs to be stated. [check] (2): `K_m = min(m, 10 − m) + 1` for `m = 1, …, 9`. [check] (3): at `m = 1` (four links, dimension `10^4`) the lowest eigenvalue of the operator in (1.1) for `cW_p` is `1.00` on a grid of `c`, above the bound `0.5`.

**Corollary W1' (the fine scale is not `U(5)` Wilson at small coupling).** Let `μ` be any measure on `U(5)`-valued links with `E_μ(1 − Re w_p) ≤ ε_μ` for every plaquette, `w_p = (1/5)tr U_p`. If the single-plaquette correlators of `ω` (those in Lemma 0, with `ι(cW_p) = w_p`) match `μ`'s within `δ`, then `2/K_m^2 ≤ 8ε_μ + 6δ`. At `m = 5`, `2/K_m^2 = 1/18`; at `m = 1` or `9` it is `1/2`.

*Proof.* Lemma 0 and Theorem W1(i). ∎

**What W1 reaches, and what it does not.** In `U(5)` Wilson with the `SU(5)` part at small coupling, `w_p ≈ e^{iθ_p}` with `θ_p` the `U(1)` plaquette angle. So W1 is a statement about the abelian factor of `U(5)`: at the lattice scale it is never weakly coupled. GA2 asks no small coupling of the abelian factor at scale `a` (line 387). Through a surface crossed by `n_S ~ (r/a)^2` links the floor decays like `(a/r)^4`, inside GA2's `O((a/r)^p)` budget. So W1 is consistent with GA2 and does not decide Y2-W.

### 2.2 The coherence gap

**Definition.** For one link register and a state `ω`, put `M = Σ_{jk}(U^{jk†}U^{jk} + U^{jk}U^{jk†})` and `κ(ω) = 2Σ_{jk}|ω(U^{jk})|^2 / ω(M)`. By Cauchy-Schwarz `κ ≤ 1`. For a commuting unitary link in a sharp configuration `κ = 1`. `κ` is not gauge invariant. It measures how classical the link variables can be in any description, gauge-fixed or not.

**Theorem W2 (coherence gap).**
(i) On the `L5-U` register in sector `m`: `(U^{jk})^2 = 0` for all `j, k`; `M = 5m − 2N^xN^y ≥ m(10 − m)/2 > 0`; and `κ(ω) ≤ 1/2` for every state.
(ii) At `m = 5`, the Slater state of the five orbitals `(r^{y†}_j + Σ_k V_{kj} r^{x†}_k)/√2`, `V ∈ U(5)`, has `ω(𝐔) = ±V/2` (all singular values `1/2`) and `κ = 1/6`.
(iii) On the `L5-O` registers `S_±` (Lemma Q, `U^{ab} = iη^y_aη^x_b`, Hermitian), with `κ := Σ_{ab}ω(U^{ab})^2 / Σ_{ab}ω((U^{ab})^2)`: `(U^{ab})^2 = 1`, and `κ ≤ 1/10` for every state. The bound is attained by a state `φ` with `ω(U^{ab}) = ε_aδ_{ab}`, `ε_a = ±1`, and `ω(L_x^{cd}) = ω(L_y^{cd}) = 0`.

*Proof.* (i) `(r^y_jr^{x†}_k)^2 = −r^y_jr^y_jr^{x†}_kr^{x†}_k = 0`. `U^{jk†}U^{jk} = r^x_kr^{y†}_jr^y_jr^{x†}_k = n^y_j(1 − n^x_k)` and `U^{jk}U^{jk†} = n^x_k(1 − n^y_j)`; sum over `j, k` to get `5N^y + 5N^x − 2N^xN^y = 5m − 2N^xN^y`, and `N^xN^y ≤ m^2/4`. For `X` with `X^2 = 0`: let `Q` project onto `ran X`; then `XQ = 0` (since `ran X ⊂ ker X`) and `X = QX`. For a unit `ψ`, `⟨ψ, Xψ⟩ = ⟨Qψ, Xψ⟩ = ⟨X^†ψ, (1 − Q)ψ⟩`. So with `q = ‖Qψ‖^2`, `|⟨ψ, Xψ⟩|^2 ≤ min(q‖Xψ‖^2, (1 − q)‖X^†ψ‖^2) ≤ ‖Xψ‖^2‖X^†ψ‖^2/(‖Xψ‖^2 + ‖X^†ψ‖^2) ≤ (‖Xψ‖^2 + ‖X^†ψ‖^2)/4`. Mixed states follow by convexity of `|·|^2`. Sum over `j, k`: `2Σ|ω(U^{jk})|^2 ≤ ω(M)/2`.
(ii) The one-body density matrix `γ` of this state is the projection onto the span of the orbitals, with blocks `A = B = 1/2` and off-diagonal block `V/2` (up to the sign fixed by ordering). `ω(U^{jk}) = ω(r^y_jr^{x†}_k)` is that off-diagonal block. So `2Σ|ω(U)|^2 = 2 · 5/4`. `N^x` is a sum of five independent fair coins, so `ω(N^xN^y) = ω(N^x(5 − N^x)) = 25/2 − 15/2 = 5` and `ω(M) = 25 − 10 = 15`. `κ = (5/2)/15`.
(iii) `(iη_aη_b)^2 = 1` for `a ≠ b`. For fixed `a`, the ten `U^{ab}` (`b = 1, …, 10`) anticommute pairwise: `η^y_aη^x_bη^y_aη^x_d = −η^x_bη^x_d = −η^y_aη^x_dη^y_aη^x_b`. For anticommuting Hermitian involutions, `(Σ_b β_bU^{ab})^2 = Σβ_b^2`, so `Σ_bβ_bω(U^{ab}) ≤ ‖β‖`, hence `Σ_bω(U^{ab})^2 ≤ 1`. Summing over ten rows gives `Σ_{ab}ω(U^{ab})^2 ≤ 10`, against `Σ ω((U^{ab})^2) = 100`. The ten `U^{aa}` commute; take `φ` a joint eigenvector, eigenvalues `ε_a`. Their product is a multiple of the chirality, so `φ` lies in `S_+` or `S_−`, and `Π_aε_a` is fixed by which. Row bounds force `ω(U^{ab}) = 0` for `b ≠ a`. Each `η^x_cη^x_d` (`c ≠ d`) anticommutes with `U^{cc}`, so its expectation in an eigenvector of `U^{cc}` vanishes; likewise at the `y`-end. ∎

[check] (2): for `m = 1, …, 9`, `(U^{jk})^2 = 0` and `M = 5m − 2N^xN^y` to machine precision; the lowest eigenvalue of `M` is at least `m(10 − m)/2`; random states give `κ ≤ 0.10`. The state of (ii) gives `κ = 0.1667` and singular values `0.5`. [check] (4): on `C^{1024}` the joint eigenvector with all `ε_a = +1` has chirality `−1` in the script's convention, `κ = 0.1000`; random `S_+` states give `κ ≤ 0.003`.

**Remark (where the classical locus sits; cited dimensions, not used).** The state of (ii) is a coherent state of `u(10)` on `Λ^5(C^{10})`, at a point where `ω(𝐔)` is half a unitary and the end generators have scalar expectations. The orbit of such points is `Gr(5, 10)`, of dimension 50, the dimension of `T^*U(5)`. Only `m = 5` has such a point: `ω(𝐔) = V/2` with `V` unitary forces `A = B = 1/2`, so `m = tr γ = 5`. The state `φ` of (iii) lies on the `SO(10)`-valued locus with zero electric field. Its orbit is `SO(20)/U(10)`, of dimension 90, the dimension of `T^*SO(10)`. So both registers are the first member of a family whose classical limit contains the Kogut-Susskind phase space near zero electric field. `L5-U` fixes that member. `L5-O` does not (section 5).

### 2.3 Averaging restores coherence

**Lemma W4.** Let `X` act on one register, and let `X̄ = (1/n)Σ_{i=1}^n X_{(i)}` on `n` copies. In the product state `φ^{⊗n}` with `x = ω_φ(X)`: `ω(X̄) = x` and `ω(X̄^†X̄) = |x|^2 + (ω_φ(X^†X) − |x|^2)/n`. The same holds for `X̄X̄^†`. So the coherence of the averaged variables is `κ_n = nκ_1/(1 + (n − 1)κ_1) → 1`, and `‖[X̄, Ȳ]‖ ≤ ‖[X, Y]‖/n`.

*Proof.* Cross terms factorise in a product state: `ω(X_{(i)}^†X_{(j)}) = |x|^2` for `i ≠ j`. Commutators of different copies vanish. ∎

The same formula applies with `X̄` replaced by the sum `Σ_iX_{(i)}`, which is the Lie-algebra action on the tensor-power register. With `κ_1 = 1/6` (Theorem W2(ii)) it gives `κ_k = k/(k + 5)`; with `κ_1 = 1/10` (W2(iii)) it gives `κ_k = k/(k + 9)`.

## 3. Three attacks

### Attack 1, toward (A): the flux floor as a no-go

*Idea.* Theorem N's boundedness, carried to states, is Lemma F. If every `SU(5)`-sensitive loop raised a bounded grading, Lemma F would give a floor at every scale. With Lemma 0 that would be (A).

*What it proves.* Theorem W1 and Corollary W1': the `U(1)`-sensitive loops of `L5-U` have the floor `2/K_m^2` at the lattice scale and `2/(n_S(K_m − 1) + 1)^2` through `n_S` links.

*Named failing step: "every loop that sees `SU(5)` raises a bounded grading".* It is false. In `U(5)` Wilson, `Θ = Π_{f ∈ ∂c} w_f` over the six oriented faces of a cube `c` is blind to the `U(1)` angles (each edge appears in two faces with opposite orientation), and it tends to 1 at small `SU(5)` coupling. The framework's `Θ_c = Π_f W_f` contains, on each of the twelve edges, one `𝐔_ℓ` and one `𝐔_ℓ^†`. So `[N^x_ℓ, Θ_c] = 0` for every `ℓ`, and Lemma F has nothing to act on. The only bounded grading that loops raise is the center flux `N^x`; the center of `SU(5)` is `Z_5`, cyclic, and a cyclic shift has eigenvalue 1. Second failing point: even for `U(1)`-sensitive loops the floor decays as `n_S^{-2}`, so it cannot exclude a window at large `r`.

### Attack 2, toward (B): the bare corner

*Idea.* In Kogut-Susskind form, small bare coupling is the corner where the electric angle is small against the magnetic one, `τ_E/τ_B → 0`, at small angles. PS-6r allows a plaquette class with its own constant (`TOE_ASSEMBLY.md` line 183: "each gate class carries its own named free constant"). Take the single-plaquette class `W_B = Π_p e^{−iτ_B(W_p + W_p^†)}` (ordering as GA1-P), and drive `τ_E/τ_B → 0`.

*Named failing step: "the corner is classical".* In Kogut-Susskind form the plaquette terms commute, the flux is unbounded (`K = ∞`) and link coherence can reach 1, so the corner has a sharp classical vacuum. In `L5-U` the plaquette terms do not commute (`LW1.md` line 162 records "noncommuting shared-link plaquette terms" for quantum links). More decisively, Theorems W1 and W2 are kinematic. They hold in every state of every corner, with constants that do not depend on `ε, μ, τ_E, τ_B`. So no value of the constants brings the fine scale to the Kogut-Susskind small-coupling regime: `D ≥ 2/K_m^2` for the `U(5)` plaquette and `κ ≤ 1/2` per link, at every corner. This refutes the route, not Y2-W. A window with `k0 ≥ 1` stays possible.

### Attack 3, toward (B): the zoom as a register knob

*Idea.* `L5-U` has no register datum, but the zoom has one. The `n ~ (r/a)^2` fine links that cross a block face carry `(Λ^m)^{⊗n}`, which contains large representations of `u(10)`. Lemma W4 shows that averaged link variables in an aligned product of coherent states have coherence `→ 1` and commutators `O(1/n)`. So at scale `r` the block variables could be as classical as the links of a large register (option (a1), supplied by ZM1). D-theory works this way, as recalled: the classical 4D fields are collective variables over an extra direction.

*Named failing step: "the block state is close to a product of aligned coherent states across each block".* Lemma W4 needs that alignment. Alignment across a block, in some gauge, is long-range order of the link field over the block, which is the small-coupling statement at scale `r` itself. A block link of a block-spin RG is also not a register sum over parallel fine links; it is a path-ordered average. So the attack reduces Y2-W to Y2-W-L below and does not prove it. The D-theory form of the attack fails at a counting step. D-theory reduces a quantum link model by one direction. `L5-U` has three spatial directions and the tick, so a reduction along any one of them leaves three Euclidean directions, not T0's four.

**Remark (not used).** GA2(a) covers factors with negative one-loop beta coefficient, where the coupling grows toward the infrared. Attack 2 shows the bare coupling is not small in the Kogut-Susskind sense. So a window at `k0 ≥ 1` would need a stretch of scales between `a` and `a_{k0}` over which the effective `SU(5)` coupling decreases toward the infrared. D-theory has such a stretch (its extra direction). For `L5-U` it would have to come from the 3+1 dynamics alone. This is the content of Y2-W-L.

## 4. The smallest exact sub-lemma

**Y2-W-L (block loop window for `L5-U`).** Fix ZM1's block map and the class `𝒲_r` of `U(1)`-blind block cube products `Θ^{(r)}_c` at scale `r` (Attack 1). Let `ω` be the state VC1 supplies. Is there a choice of constants (`m`, `ε`, `μ`, `τ_E`, a plaquette class with its constant) and a scale `r = a_{k0}` such that SC-loop(`r`; `η_*`) holds for `𝒲_r`, with `η_* = 8ε_μ(g_*) + 6δ`?

- If Y2-W-L fails for every choice, then (A) holds: no window, by Lemma 0, given `ε_μ(g)` for T0-start's class (to be confirmed on the branch) and ZM1-G's identification of `Θ^{(r)}` with `Θ`.
- If it holds, the plaquette-level necessary condition holds, and (B) then needs ZM1-G in full (all of `Λ_r`, not just one family).
- Its first case is `k0 = 0`. **Y2-W-L0** is finite-dimensional and kinematic: is `inf_ω inf_c D_ω(cΘ_c) > η_*` on the twelve links of one cube? It is open. If true, a window must start at `k0 ≥ 1`.

## 5. `L5-O` and option (a1)

### 5.1 The analogous question

**Y2-W[`L5-O`].** Are there a register `R` (free datum, `LW1_5_DRAFT.md` section 8.1 item 2: "a finite-dimensional unitary representation of `𝔨 = so(20)` ... Free datum"), constants, a plaquette class and `k0` with SC(`a_{k0}`; `δ`) for `G_i = SO(10)` (or `Spin(10)`) in the state VC1 supplies?

### 5.2 What (a1) answers

- Theorem W1 has no analogue. `SO(10)` has no `U(1)` center, and on `S_±` the `U^{ab}` are Hermitian involutions, not flux-raising operators.
- The proposed register `S_+` is as far from classical as `L5-U`'s: `κ ≤ 1/10`, attained (W2(iii)).
- (a1) is inside the free data. `R = S_+^{⊗k}` (or its irreducible top component) is a finite-dimensional unitary representation of `so(20)`. In `φ^{⊗k}`, with `φ` the state of W2(iii) taken in `S_+`, the link variables `Σ_iU^{ab}_{(i)}` have coherence `k/(k + 9)` (Lemma W4), expectation `k·diag(ε)` on the `O(10)`-valued locus (sign of `det` fixed by chirality), and zero electric field. [check] (4): `k/(k + 9) = 0.1, 0.18, 0.25, 0.31` for `k = 1, …, 4`.

So (a1) answers the fine-scale classicality part of Y2-W[`L5-O`]: the links can be classical to `O(1/k)`. With large `k`, Attack 2's corner becomes available, because the kinematic obstructions shrink like `1/k`. Y2-W[`L5-O`] then becomes the standard bare-coupling question for a tick law with near-classical `SO(10)` links, plus Y1 and Y3. Two limits stay, as in `GA2_Y2_DRAFT.md` (a1): convergence is never in norm (Corollary N3'), and one law has one register, so GA2 holds only with an error `O(9/k)` that must fit its budget. T0-start for `SO(10)` is outside the branch's planned `SU(N)` path. (a1) does not answer the coupling question itself.

### 5.3 The matching datum for `L5-U` (recorded, not proposed)

**L5-U[ρ].** Replace the rishon register by any finite-dimensional unitary representation `ρ` of `u(10)`, with `U^{jk} := ρ(` the off-diagonal generator `)` and end generators `ρ(` the diagonal blocks `)`. Theorem U's commutation proof uses only the Lie-algebra relations, so the Gauss law holds for every `ρ`. With `ρ = (Λ^5)^{⊗k}`, the flux `N^x` takes `5k + 1` values, so W1's floor becomes `2/(5k + 1)^2`, and the coherence reaches `k/(k + 5)`. Four tests: (1) conditional: it fails if its reason is T0 alone; a second reason is parity with `L5-O`'s item 2 and `LW1.md`'s spin `S`; (2) passes for a named `ρ`, fails for "large"; (3) passes; (4) passes if the parity reason is accepted. Results proved for rishon registers (for example `LW1_5U_DRAFT.md` Proposition Σ-U) would need re-checking. This is the owner's call.

---

## FINISH

**Proved here (pass 1, not distilled or refereed).**
- Definition SC (what GA2 needs) and Definition SC-loop, with the four-test check; Lemma 0: SC with a small-field `μ` gives SC-loop with `η = 8ε_μ + 6δ`.
- Lemma F: a flux-raising operator `Y` with `K` flux values obeys `ω(|Y − z|^2) + ω(|(Y − z)^†|^2) ≥ 2|z|^2/K^2` in every state.
- Theorem W1: on `L5-U`, for every value of the constants, every plaquette class and every state, `D_ω(cW_C) ≥ 2/K_m^2` (`K_m = min(m, 10 − m) + 1`) for every loop through a link once, and `≥ 2/(n_S(K_m − 1) + 1)^2` for operators of net flux 1 through `n_S` links. Corollary W1': the lattice scale of `L5-U` is never `U(5)` Wilson at small coupling (`2/K_m^2 ≤ 8ε_μ + 6δ` is forced).
- Theorem W2: `L5-U` links have `(U^{jk})^2 = 0`, `M = 5m − 2N^xN^y`, coherence `κ ≤ 1/2` in every state, and `κ = 1/6` at the graph-plane state (`m = 5`). `L5-O[S_±]` links have `κ ≤ 1/10`, attained on the `O(10)`-valued locus with zero electric field.
- Lemma W4: averaging over `n` aligned copies gives coherence `nκ_1/(1 + (n − 1)κ_1)`; hence `k/(k + 5)` and `k/(k + 9)` for tensor-power registers.

**Counterexamples.** None to a stated claim. The bare-corner route (Attack 2) is refuted as a route: no constants bring the fine scale of `L5-U` to the Kogut-Susskind small-coupling regime.

**Open, by name.**
- **Y2-W** for `L5-U`: open after three named attacks (section 3). Attack 1 fails at "every loop that sees `SU(5)` raises a bounded grading". Attack 2 fails at "the corner is classical". Attack 3 fails at "the block state is close to a product of aligned coherent states", and its D-theory form at the direction count.
- **Y2-W-L** (section 4), the smallest exact sub-lemma; its failure for all constants proves (A). Its kinematic first case is **Y2-W-L0** on one cube.
- **Y2-W[`L5-O`]**: (a1) settles its fine-scale classicality part; the coupling part is open as a bare-coupling question with Y1, Y3 and T0-start for `SO(10)`.

**Named failing step for `L5-U` or `L5-O`.** None. Neither law fails at a named step here. Both stay live under section 3.5. The fixed register of `L5-U` costs a lattice-scale start: a window, if it exists, must begin at `k0 ≥ 1` for the `U(1)`-sensitive loops (Corollary W1'), and for every loop if Y2-W-L0 holds.

**What GA2 needs next.**
1. From the YM programme, inside T0-start: the plaquette bound `E_μ(1 − Re w_p) ≤ ε_μ(g)` for every `μ` in `𝒜_k(g)`, for `SU(N)`. The branch has it for bare Wilson `SU(2)` (upper-chain Theorem 2).
2. From ZM1: a fixed block map and a fixed class of block loops at scale `r`, with ZM1-G's identification `ι`.
3. From VC1: the state `ω`. Definition SC is stated for that state only.
4. On the TOE side: attack Y2-W-L0, then Y2-W-L.
5. Owner decision, if wanted: whether `L5-U` should carry a register datum (L5-U[ρ], section 5.3). Recorded, not proposed.
