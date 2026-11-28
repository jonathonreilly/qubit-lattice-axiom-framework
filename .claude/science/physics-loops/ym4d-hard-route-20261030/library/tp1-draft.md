# TP1 (with AG1): the two-point law, the running normalisation and TU10 — pass 1, long draft

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-04, one session, written for the lead under `library/process-review-2026-11-04.md` §4 item 2 (Claude generates at length; Codex distils; a fresh session then reads line by line). Research text. It is not an audit, it grants no status, and no other model has read it. No step rests on a computation; every argument below is meant to be Lean-formalisable (finite sums, Cauchy integrals on polydiscs, Isserlis' formula, elementary inequalities).

Credit. The short-distance architecture is that of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text): the outline `YM4_sketch_500.tex` (SA), its Section 7 (SA L25966ff), the obligations F2, F3, D3 (SA L4289–4415, L4165–4176), and their complete account (CA-I/II/III). Their three-dimensional manuscript `YM3/YM3_I.tex` (Y3) supplies the complex plaquette coefficient, the small-torus law and the vector orthogonal to the vacuum, which are ported here. Tadeusz Balaban's papers (CMP 95, 96, 109, 116, 119, 122a, 122b) are the source of the renormalisation-group (RG) method and of the free decomposition used in §6; Jonathan Dimock's expositions (arXiv 1108.1335, 1212.5562, 1304.0705) are the readable versions. Our own notes `library/tu10.md` (Codex), `library/ref-73.md` (Codex) and `library/ym4-assembly.md` (Claude) are the starting point; their results are re-proved where they are used.

Line references: **SA L** = `scratchpad/sa/ym4.tex`; **CA-III L** = `scratchpad/sa/ca_III.tex`; **Y3 L** = `scratchpad/sa/YM3_I.tex` (3,646,452 bytes, 89,144 lines, commit `31a47c543775`; I read it myself in this session at the lines cited). Every claim about these texts below quotes the line range I read.

Status words, used inline: **[proved]** = proved in this file by hand, from the stated imports; **[imported: X]** = a statement of another submanuscript X of `ym4-assembly.md`, used as stated there, with its own status; **[TP-input: NAME]** = a statement TP1 needs from the hard core that the assembly does not yet list in that form; **[outstanding]** = TP1's own statement, not proved here.

---

## 0. Summary

**What TP1 must prove** (assembly §5, TP1(a), L391–397): the reference two-point law F2 with |r| ≤ ½ for every periodic Gibbs state, the running normalisation F3, TU10, and the law on R⁴ for every continuum limit and component; AG1 (assembly L351) is the rarity input inside it.

**Route chosen (§5).** I keep SA's two-level skeleton but change three things.

1. *Gaussian extraction by Cauchy estimates in a complex plaquette coefficient* (ported from Y3 L745–747: the complex-source construction "extends these measures to a complex plaquette coefficient"), done at one coarse level k₁ only. The interacting comparison is then a sup bound on a coupling-sized complex disc, differentiated by Cauchy's formula. No integration by parts in field directions occurs, so the complete-force term (GCB52) of SA L28196–28221 never appears. SA L28219–28221 says: "No such convexity, symmetry or force bound is asserted for the resummed interacting conditional density." Our route needs none.
2. *Transfer through an infinite-volume reference and the common cell normaliser*, so the finite reference torus and the companion criteria (ET8)–(ET10) of SA L26872–26931 are not needed (SA's own F2 text, L4345–4348, says an infinite reference "needs no finite-volume vacuum comparison").
3. *NT1 by a vector orthogonal to the vacuum* (Y3 L88901–88917, Lemma IV-69-33) plus the unique vacuum of PH1(5). This needs only one strictly positive reflected two-point value, not the ratio argument of Lemma W.

**Proved here [proved], from the named imports.**

- §3: the exact Wilson facts (sources are local inverse-coupling changes; mixed derivatives; dilation; the Wick identity for half-squares; Cauchy lemmas; kernel bounds on the shape class).
- §3.6: *the four-dimensional obstruction*, as arithmetic: the creation-rarity union bound that closes Y3's short-distance law diverges in four dimensions (Lemma 3.9). This is the precise reason AG1 exists in 4D and not in 3D.
- §4: F3 from OL1(2), OL1(3), OL1(5) and the slope bound of SC1. The one-loop increment law OL1(4) ⟦OL-incr⟧ is **not** needed: only the telescoped sum enters.
- §6: the reference law RL on every compatible torus, uniformly in the side, as an implication from the five TP-inputs of §2.2 and (AG-k₁) (summation, Gaussian template, free comparison, all error terms).
- §7: transfer to every periodic Gibbs state with error D d² (the arithmetic of `tu10.md` (8), re-proved, and fed by an infinite reference).
- §8: TU10, the law on R⁴ with ε̄ = ½ for every volume-first limit and every component.
- §9: NT1 in every component.
- §10.2: AG1 is needed, for TP1, only as one weighted live-age tail at a single level and for the unsourced law, (AG-k₁); and (AG-k₁) follows from a stagewise rarity product (Lemma 10.1, [proved]) once two per-level statements (H), (SR) hold.

**First outstanding statement (TP1's own).** Lemma AG-k₁ (§10.1): at the coarse level k₁, the weighted live-age tail Σ_a L^{8a} sup_c P(a live lineage of age ≥ a meets the cell c) is at most C(log x)^C e^{−c p₀(g_{k₁})}, uniformly in the volume, the cutoff and the position, for the *unsourced* positive history law. Three attacks are in §10.3. (A) The Y3 union bound over creations: fails by Lemma 3.9 (linear running in 4D). (B) A stagewise product (Lemma 10.1, proved) reduces it to a healing dichotomy (H) and a stagewise rarity (SR); chessboard reduces (SR) to a periodic constrained free-energy bound (CF); it stops at (H), which is SA's healing/exit property (CA-III lists "the exit bound" as proof outstanding, L111192–111193), and at (CF), which needs the same constrained-versus-free comparison (SEP) at which `rarity-fresh-x.md` stopped. (C) Closing large-field regions off at creation removes ages but needs ⟦LF-mass⟧ (LF1(3)) and still needs (H). The common core is stated at the end of §10.3.

**TP-inputs (§2.2) that the hard core must supply**, beyond the assembly's own lists: (TP-cx) the regular energies on coupling-sized complex discs (an extension of NL1(3)/SC1 from the ordinary source ball; `tu10.md` §3 shows the ordinary ball cannot suffice); (TP-pres) the exact sourced presentation at level k₁ (SC1's exact mass identity; = ref-73 (4)); (TP-slope) the constant-source slopes; (TP-live) the live amplitude bound. None of these is attacked here beyond stating it exactly and showing where it is used; each belongs to NL1, SC1 or LF1.

---

## 1. Statements

### 1.1 Notation

As in `ym4-assembly.md` §0. G = SU(2), N = 2, d = 4 dimensions, L odd and large, a_K = L^{−K}, a_p(U) = 1 − ½ Re tr U_p ∈ [0, 2], O_K(f) = Σ_p f(x(p)) a_p(U). Compatible tori T_ℓ, ℓ = 2L^m, m ≥ m₀.

Levels. An RG run on a_K Z⁴ has steps j = 1, …, K from fine to coarse; after j steps the cells have side a_{(j)} := L^j a_K = a_{K−j}. The running inverse coupling is x₀ = β, x_j = x_{j−1} − b_j. (SA writes x_{k}, k = K − s; the same here.)

Shape class 𝔗(d; ϑ) (SA L26020–26030 as read; assembly §0): f, h ≥ 0 nonzero Lipschitz, supp f ⊂ B(x_f, d), supp h ⊂ B(x_h, d), d ≤ dist(supp f, supp h) ≤ 6d, ∫f ≥ ϑ‖f‖_∞ d⁴, Lip f ≤ ‖f‖_∞/(ϑd), the same for h. ϑ_* = 1/12000. K_free(f,h) = ∬ f(x)h(y)|x − y|^{−8} dx dy. C_G = 3(N² − 1)/π⁴.

Witness depth (SA L26062–26070; Y3 L87778–87800 in its 3D form). Fix 𝔭₀ (the large-field exponent of the assembly's order, p₀(g) = (log g^{−2})^{𝔭₀}), put x̄_s := g^{−2} + B_♯(s + 1), C_W(s) := C_{W,0} p₀(x̄_s^{−1/2})² = C_{W,0}(log x̄_s)^{2𝔭₀}, and

s(d) := min{s ≥ 0 : L^s d ≥ C_W(s)},   d̂ := L^{s(d)} d ∈ [C_W(s), L C_W(s)).

The bracket holds by minimality and monotonicity of C_W (if s ≥ 1: L^{s−1}d < C_W(s − 1) ≤ C_W(s)). Since log C_W(s) = O(log log s) = o(s), s(d) log L = log(1/d) + O(log log(1/d)).

The witness level is k₀ := K − s(d), with cells of side a_{(k₀)} = a_{s(d)} = d/d̂, so the pair is d̂ ∈ [C_W, LC_W) cells apart. The coarse level is k₁ := k₀ + n with n := ⌈2 log_L x̄_{s(d)}⌉, so L^n ≥ x̄² and cells of level k₁ have side ≥ x̄² d/(LC_W) ≫ d. We require K − s(d) ≥ n₀ and n ≤ s(d) (so k₁ ≤ K), which hold for d ≤ d₀(g) and K − s(d) ≥ n₀. We write

x := x_{k₀} = g(d)^{−2},   ζ := ζ'_{k₀}.

### 1.2 Theorem TP1 (our form)

**Theorem TP1.** Fix L and the constants of the assembly's order (§3 there). There are a ceiling γ_W > 0, an integer n₀ and, for each 0 < g ≤ γ_W, a threshold d₀(g) ∈ (0, 1/10) such that for every first-passage datum (K, β) at g, every d ≤ d₀ with K − s(d) ≥ n₀ and every C¹ pair (f, h) ∈ 𝔗(d; ϑ_*):

1. *(F2, all states.)* For every periodic Wilson Gibbs state ρ ∈ 𝒢_{a_K,β},
   S^T_2[ρ](f,h) := ρ(O(f)O(h)) − ρ(O(f))ρ(O(h)) = C_G ζ² g(d)⁴ K_free(f,h)(1 + r),  |r| ≤ ½,
   and |r| ≤ ε̄(d) with ε̄ non-decreasing, ε̄(d) → 0, independent of K, β, ρ and the position of the pair.
2. *(F3.)* g(d)^{−2} = c_* log(1/d)(1 + η₁(d)), c_* = 11N²/(12π²), and |ζ − 1| ≤ η₂(d), with η₁, η₂ → 0 uniformly in (K, β).
3. *(TU10.)* 0 ≤ S^T_2[ρ](f,h) ≤ u(d)‖f‖_∞‖h‖_∞, u(d) = C′[log(1/d)]^{−2}.
4. *(Law on R⁴.)* Every volume-first limit S of CL1 and every component σ_ξ of PH1 satisfies, on C¹ pairs of 𝔗(d; ϑ_*), S_2^T(f,h) = C_G g_c(d)⁴ K_free(f,h)(1 + η), (1 − ½)(1 − η̄)⁴ ≤ 1 + η ≤ (1 + ½)(1 + η̄)⁴, where g_c(d)^{−2} := c_* log(1/d) and η̄(d) → 0. (This is T0(5)'s law, assembly L57.)
5. *(NT1.)* For every component σ_ξ, H_{σ_ξ} ≠ 0 on Ω^⊥.

**Theorem AG1 (our form).** Statement (AG-k₁) of §10.1. It is the only rarity statement TP1 reads.

**Status.** TP1(1)–(5) [proved] from the imports of §2.1, the TP-inputs of §2.2 and (AG-k₁). (AG-k₁) [outstanding]; reduced in §10.2 to (H) and (SR).

---

## 2. Imports

### 2.1 Imports from other submanuscripts (used as stated in `ym4-assembly.md`)

- **LG1(2), LG1(5)** [imported: LG1, [C]]: periodic limits of torus measures are DLR states; 𝒢_{a,β} is compact convex; every periodic Wilson DLR state is invariant under all unit lattice translations and the signed permutation group, and reflection positive at coordinate and diagonal mirrors.
- **IN1(3), IN1(4)** [imported: IN1, [O]]: the flow exists to first passage, g^{−2} < x_K ≤ g^{−2} + B_♯, b_i ≤ B_♯; the increments are independent of the torus and of unused finer cutoff.
- **OL1(2), OL1(3), OL1(5)** [imported: OL1; (2) [C], (3) [P], (5) [O] = ⟦OL-nl⟧]: b_j = b_j⁰ + f_j + q_j with b_k⁰ = A_k − A_{k−1}, A_k = b[Ψ_k] (exact substitution at the trivial background), |A_k − k c₀| ≤ c₂(L), c₀ = 11N² log L/(12π²); |f_j| ≤ C x_{j−1}^{−1/2}(log x_{j−1})^{𝔭}, |q_j| ≤ C x_{j−1}^{−(κ₀−4)/2}, κ₀ > 6.
  (I use κ₀ > 6 rather than the assembly's κ₀ > 4 only in §4.3, for the normalisation slope; SA L26075–26084 uses the same exponent κ₀ − 6.)
- **FC1** [imported: FC1, [SP]] (SA F1, L4252–4288): for the standard Gaussian on ran d₁ (covariance P_ex) on T_ℓ at spacing a, with r = |x(p) − x(q)|, |a^{−4}P_ex(p_P, q_Q) − K_{P,Q}(x(p) − x(q))| ≤ C r^{−4}[(a/r)^{1/2} + (r/ℓ)⁴] for a ≤ r/10, r ≤ ℓ/10; 𝕂(u) = π^{−2}|u|^{−4}Λ²𝖨(û), tr 𝕂(u)² = 6π^{−4}|u|^{−8} (SA L26038ff).
- **The free orthogonal decomposition** [imported: FC1 with SA (7a)–(7b)(c), [SS]] (SA L26038–26060 and L26133–26160, the latter citing Balaban CMP 95 (1.103), (1.110)): P_ex = Σ_{j=1}^{K} G_j with G_j the covariances of mutually independent pieces of the free curvature (the RG slices at U = 1), and
  |G_j(p, q)| ≤ C_s (a_K/a_{(j)})⁴ e^{−δ_s |x(p) − x(q)|/a_{(j)}}   (2.1)
  as 6 × 6 matrices in the plaquette orientations. (SA's display at L26133ff gives |𝒞_{(j)}(p,q)| ≤ Cη_{j−1}⁴ e^{−δ|x(p)−x(q)|/a_{K−j+1}}; (2.1) is that bound with η_j⁴ = (a_K/a_{(j)})⁴ written out.)
- **SR1, common cell normaliser** [imported: SR1, [C] as an implication from D1] (SA L23833ff, "Holomorphic cell normalizers from the ordinary hypothesis"): for a cell C of side l and sources supported in radius-R balls at distance > b from ∂C, there are a holomorphic E_C(z) and constants Q, r₀ such that for every periodic Gibbs state ω at the same datum, h_ω(z) := e^{−E_C(z)} ω(exp Σ_i z_i O(F_i)) satisfies h_ω(0) = 1 and |h_ω| ≤ Q on Σ_i |z_i|‖F_i‖_♯ < r₀, with Q, r₀ independent of K, ℓ, ω and of the positions.
- **CL1(1)–(3), PH1(3), PH1(5)** [imported: CL1, PH1, [C] as implications]: volume-first limits on separated tuples; RP at x₄ = 0; the OS space; the canonical decomposition, each σ_ξ realised by periodic Gibbs states (all-state realisation, SA L4380–4412 "all-state phase realizations"); ker H_{σ_ξ} = CΩ.

### 2.2 The representation at level k₁ (from SC1 and LF1)

Fix the datum, the torus T_ℓ and the pair. Write w = z₁f₁ + z₂f₂ (f₁ = f, f₂ = h). I use the sourced construction of SA (4a)–(4b) (SA L22345–23385, as summarised at SA L26085–26117) run to level k₁, with the history classes [h] and the retained variables y = ([h], V, ξ) of `ref-73.md` §2.

**(TP-pres)** [TP-input; SC1, ⟦TP-7.6⟧ first step] There is a positive measure P^{(k₁)} on the retained variables and a sourced exponent Φ(z; y), holomorphic in z on a polydisc 𝔻₀ ∋ 0, with Φ(0; y) = 0 and

Z(z)/Z(0) = E_P e^{Φ(z;y)}   (2.2)

with differentiation under E_P allowed, where Φ is the *formed* exponent of SA 4.6 with its regular, pointed and live parts:

Φ = Φ^{pt} + Φ^{reg} + Φ^{live} + Φ^{far}.   (2.3)

`ref-73.md` §2 proves the identity (2.2) by hand for *some* logarithm (its (3)), and §3 there shows that the identification with the formed exponent is exactly its (4). I do not re-prove that; I use the finite identity (2.2) in §6 only through the formula (6.1) below, which ref-73 proves for any such representation. The *decomposition* (2.3) with the bounds below is the input.

**Pointed part.** Φ^{pt}(z; y) = Σ_p φ_p(w(x_p); y) is a sum of functions each depending on one value of w (SA L26103–26105: "the running shift at a plaquette is a finite sum of functions of this kind"). Hence, since f₁f₂ = 0 pointwise, ∂_{z₁}∂_{z₂}Φ^{pt} = 0. [This consequence is proved: a function of w(x_p) alone, with f₁(x_p)f₂(x_p) = 0, depends on only one of z₁, z₂.]

**Marginal part.** Off live components, ∂_{z_i}Φ at 0 contains ζ'_{k₁} X_i, X_i(V) = Σ_p f̃_i(p) χ(□(p)) a_p(U_{k₁,□(p)}(V)) (SA L26117–26132, there at level k₀; the same formula at k₁).

**(TP-cx)** [TP-input; NL1(3) and SC1 on coupling-sized discs] For every level j ≤ k₁ and every localisation domain X ∈ 𝒟_j of the regular part, the regular energy e_j(X; z, V) is holomorphic in z on the *coupling-sized polydisc*

𝔻_j(X) := {z : |z_i| ‖f_i‖_∞ < r x_j for every i with X^+ ∩ supp f_i ≠ ∅}

(e_j(X) does not depend on z_i when X^+ misses supp f_i, so no condition is imposed on that z_i), for every real regular V in the small-field domain near X, with

|e_j(X; z, V)| ≤ C e^{−κ m_j(X)},   e_j(X; ·, V) = e_j^G(X; ·, 𝟙) + ρ_j(X; ·, V),   |ρ_j| ≤ C x_j^{−1/2}(log x_j)^{q} e^{−κ m_j(X)} on 𝔻_j(X),   (2.4)

where 𝟙 is the trivial block field, e_j^G(X; ·, 𝟙) are the localised pieces of the exact Gaussian computation of the free running model of §6.2 with the actual source transport (§6.2, (S1)–(S2)), κ exceeds the rooted entropy rate ϵ of the level-j domains, and m_j(X) is the tree size of X in level-j cells. (The remainder ρ_j contains both the non-Gaussian part at V and the change of the Gaussian part from 𝟙 to V; in the small-field domain the background curvature in level-j units is ≤ C p₀(g_j) g_j, which is why the same factor x_j^{−1/2} up to logarithms bounds both.) Also the oscillation bound: for V in the small-field domain on the O(1) cells of level k₁ near the supports,

|∂_{z_i}(Φ^{pt} + Φ^{reg})(0; V) − c_i| ≤ C x^{−1}(log x)^{C} (d̂ L^{−n})² ‖f_i‖_∞,   (2.5)

with c_i a constant (independent of y), and on every history the crude bound |∂_{z_i}(Φ^{pt} + Φ^{reg})(0; y) − c_i| ≤ C x^{−1}(log x)^C‖f_i‖_∞.

*The sup-norm radius at coarse levels.* At levels j > k₀ the test is rough on the cell scale, and SA's sharp norm ‖f‖_{♯,K−j} can exceed ‖f‖_∞ by L^{j−k₀} (SA's Strategy paragraph for Proposition 7.3, L26085–26101). (TP-cx) asks for holomorphy on the sup-norm disc of radius r x_j even so. The reason it is plausible: a source of sup-size < r x_j changes the local inverse coupling by a relative amount < r on its support, whatever its roughness, and the step stays coercive (Re(1 − ε) ≥ 1 − r); roughness enters SA's estimates through the localisation of the pointed (running-shift) part, which has no mixed derivative. If only the sharp-norm radius r x_j L^{−(j−k₀)} were available, the Cauchy factor at level j would grow like L^{2(j−k₀)}, and the sum over the n = O(log x) coarse levels in §6.4 would carry L^{2n} ≥ x̄⁴, which x^{−1/2} cannot pay. Then the coarse levels would have to be treated by SA's exact one-step recursion at the flat background (SA (c3), L26162–26176) instead. This is the one place where the route depends on the exact form of the disc.

*Why this is the right input.* `tu10.md` §3 (Codex) builds a bounded source model that satisfies every displayed D1 clause on the *ordinary* source ball (fixed radius r) and every E1 flow bound, yet has a short-distance covariance bounded below by c_*² > 0 at arbitrarily small d. So no argument from the fixed-radius D1 alone can give the factor x^{−2}. The scaling of the source disc with x_j is the Wilson-specific link: the source is a change of the local inverse coupling (Lemma 3.1), and the step is holomorphic in the coupling on a disc of relative radius r < 1 (the Gaussian part is a complex Gaussian with Re(1 − ε) ≥ 1 − r; the Wilson factor e^{−(β−w)a_p} keeps modulus ≤ e^{−(1−r)βa_p}). Y3 does exactly this in three dimensions ("extends these measures to a complex plaquette coefficient", Y3 L745–747). SA F3 (L4375–4378) names "coupling-sized independent complex polydiscs" as the domain of its own slope proof.

**(TP-live)** [TP-input; LF1 and SC1] (SA L26103–26117.) Let a(y) be the largest lineage age of a live component meeting the CMŘ-neighbourhood of supp f₁ ∪ supp f₂ at level k₁ (a(y) = −∞ if none). Then Φ^{live} vanishes when a(y) = −∞, and otherwise, on the coupling-sized disc,

|∂_{z_i}Φ^{live}(0)| ≤ C x^{−1}(log x)^{C} L^{4a} ‖f_i‖_∞,   |∂_{z₁}∂_{z₂}Φ^{live}(0)| ≤ C x^{−2}(log x)^{C} L^{8a} ‖f₁‖_∞‖f₂‖_∞.   (2.6)

and on such histories the regular part keeps its bound |e_j| ≤ C e^{−κm_j(X)} on 𝔻_j(X) and the crude bound after (2.5). (SA states the amplitude growth with age: "The growth of the amplitude and the decay of the series are governed by one and the same age, namely the age of the lineage", L26103–26117.)

**(TP-far)** [TP-input; SC1] |∂Φ^{far}| ≤ C e^{−c d̂}‖f‖_∞ x^{−1} and the same for the mixed derivative with x^{−2} (SA L26117–26132, "(far)": exponentially small in the localisation radius).

**(TP-slope)** [TP-input; SC1, SA (3c)/(4b)] A constant source w ≡ t acts as a shift of β with all auxiliary choices frozen; the increment b_{j+1}(t) is holomorphic for |t| < 2ϱ and |b'_{j+1}(0)| ≤ C[g_j³ (log x_j)^{𝔭₀} + ϱ^{−1} g_j^{κ₀−4}] (SA L26075–26084, Lemma 7.2's proof, as read). ζ'_k := 1 + Σ_{j≤k} b'_j(0) (SA L26075ff).

### 2.3 Summary of what TP1 reads

| Input | Owner | Status in the assembly | Used in |
|---|---|---|---|
| LG1(2),(5) | LG1 | [C] | §7, §8 |
| IN1(3),(4) | IN1 | [O] | §4, §6 |
| OL1(2),(3),(5) | OL1 | [C], [P], [O] | §4 |
| FC1, free decomposition (2.1) | FC1 | [SP]/[SS] | §6 |
| common cell normaliser | SR1 | [C] from D1 | §7 |
| CL1, PH1 | CL1, PH1 | [C] | §8, §9 |
| TP-pres, TP-cx, TP-live, TP-far, TP-slope | SC1, NL1, LF1 | not listed in this form | §4, §6 |
| AG-k₁ | AG1 (TP1's own) | [outstanding] | §6.5 |

Not read: OL1(4) ⟦OL-incr⟧; the finite reference torus and (ET8)–(ET10); the interacting force term (GCB52); Lemma W; CA-III's Lemma 7.3 (non-convergence of first-passage offsets, CA-III L111241–111242), since only g^{−2} < x_K ≤ g^{−2} + B_♯ is used.

---

## 3. Exact facts [all proved]

### 3.1 Sources are local inverse-coupling changes

**Lemma 3.1.** On a finite torus, for complex z₁, z₂ and real bounded f₁, f₂,
Z(z) := ∫ e^{z₁O(f₁) + z₂O(f₂)} e^{−βΣ_p a_p(U)} dU = ∫ exp(−Σ_p (β − w(x(p))) a_p(U)) dU, w = z₁f₁ + z₂f₂.
Z is entire in (z₁, z₂), Z(z) > 0 for real z, and S^T_2(f₁,f₂) = ∂_{z₁}∂_{z₂} log Z(0).

*Proof.* The first identity is the definition of O. The integrand is a finite product of entire functions of z with modulus ≤ e^{2(|z₁|‖f₁‖₁' + |z₂|‖f₂‖₁')}, where ‖f‖₁' := Σ_p|f(x(p))| < ∞ is a finite sum; Haar measure is finite, so Z is entire by differentiation under the integral (dominated convergence on compact z-sets). For real z the integrand is positive. Near 0, Z ≠ 0, log Z is holomorphic, ∂_{z_i} log Z = Z^{−1}∂_iZ and ∂₁∂₂ log Z = Z^{−1}∂₁∂₂Z − Z^{−2}∂₁Z ∂₂Z; at z = 0 this is ⟨O(f₁)O(f₂)⟩ − ⟨O(f₁)⟩⟨O(f₂)⟩. ∎

So a source of size |z|‖f‖_∞ changes the inverse coupling by at most that amount; relative to the running coupling x_j at the level where the source lives, it is a relative change of size |z|‖f‖_∞/x_j. This is the reason the natural source disc has radius proportional to x_j (TP-cx).

### 3.2 Dilation

**Lemma 3.2** (SA's "Cutoffs off first passage" remark in (7a), L26038ff; it is a relabelling). For b ∈ Z and f^{[b]}(x) := f(L^{−b}x), ⟨O(f); O(h)⟩_{K,ℓ,β} = ⟨O(f^{[b]}); O(h^{[b]})⟩_{K−b, L^bℓ, β}.

*Proof.* The map x ↦ L^b x carries a_K Z⁴ ∩ T_ℓ = L^{−K}Z⁴ ∩ T_ℓ bijectively onto L^{b−K}Z⁴ ∩ T_{L^bℓ} = a_{K−b}Z⁴ ∩ T_{L^bℓ}. It carries bonds to bonds, plaquettes to plaquettes and barycentres to barycentres; product Haar measure and every a_p are invariant, and f(x(p)) = f^{[b]}(L^b x(p)). Both sides are therefore the same finite integral after relabelling. K_free(f^{[b]}, h^{[b]}) = L^{8b−8b}K_free(f,h) = K_free(f,h), since dx dy scales by L^{8b} and |x−y|^{−8} by L^{−8b}; 𝔗(d;ϑ) maps to 𝔗(L^b d; ϑ). ∎

(TP1 does not need Lemma 3.2; it is recorded because SA's two-variants remark uses it, and because it shows S^T_2 depends on (K, d) only through the lattice separation d/a_K and β.)

### 3.3 Half-squares of Gaussians

**Lemma 3.3** (Isserlis). Let φ be a centred Gaussian vector in R^m with covariance Σ, and P, Q real symmetric m × m matrices. Then Cov(½⟨φ, Pφ⟩, ½⟨φ, Qφ⟩) = ½ tr(PΣQΣ). In particular, if φ = (X, Y) with Cov(X_a, Y_b) = C_{ab}, then Cov(½|X|², ½|Y|²) = ½ Σ_{a,b} C_{ab}².

*Proof.* Isserlis: E φ_iφ_jφ_kφ_l = Σ_{ij}Σ_{kl} + Σ_{ik}Σ_{jl} + Σ_{il}Σ_{jk}. Hence E[½⟨φ,Pφ⟩ ½⟨φ,Qφ⟩] − E[½⟨φ,Pφ⟩]E[½⟨φ,Qφ⟩] = ¼ Σ P_{ij}Q_{kl}(Σ_{ik}Σ_{jl} + Σ_{il}Σ_{jk}) = ¼(tr(PΣQΣ) + tr(PΣQΣ)) by symmetry of P, Q, Σ. For the special case take P = diag(I, 0), Q = diag(0, I): tr(PΣQΣ) = Σ_{a,b} C_{ab}C_{ab}. ∎

*Use.* With a_p ≈ ½ a_K⁴|F_U(p)|² (SA L6852) and N² − 1 independent colours of the free curvature, each with covariance x^{−1}P_ex at inverse coupling x, Lemma 3.3 gives Cov(Σ_p u(p)½|F_p|², Σ_q v(q)½|F_q|²) = ((N²−1)/2) x^{−2} Σ_{p,q} u(p)v(q) tr[P_ex(p,q)P_ex(q,p)], the trace over the six orientations. With FC1, a_K^{−8}tr P_ex(p,q)² → tr 𝕂(x−y)² = 6π^{−4}|x−y|^{−8}, and Σ_{p,q} ↔ a_K^{−8}∬ (one plaquette of each of the six orientations per site), so the free value is ((N²−1)/2)(6/π⁴) x^{−2} K_free = C_G x^{−2}K_free. This is SA's constant (SA L26038–26040: "(N²−1)/2 · 6/π⁴ = 3(N²−1)/π⁴").

### 3.4 Cauchy lemmas

**Lemma 3.4.** Let Ψ be holomorphic on a neighbourhood of the closed bidisc |z₁| ≤ ρ₁, |z₂| ≤ ρ₂, with |Ψ| ≤ A there. Then |∂_{z_i}Ψ(0)| ≤ A/ρ_i and |∂_{z₁}∂_{z₂}Ψ(0)| ≤ A/(ρ₁ρ₂). If Ψ does not depend on z₂, ∂₁∂₂Ψ = 0.

*Proof.* Cauchy's formula on the distinguished boundary: ∂₁∂₂Ψ(0) = (2πi)^{−2}∮_{|z₁|=ρ₁}∮_{|z₂|=ρ₂} Ψ(z) z₁^{−2}z₂^{−2} dz₁dz₂, and the length of each circle is 2πρ_i. The first derivative is the one-variable case. ∎

**Lemma 3.5** (Schwarz along rays; `tu10.md` §4, re-proved). Let h be holomorphic on {Σ_i |z_i|t_i < r₀} with h(0) = 1 and |h| ≤ Q. On the polydisc |z_i| ≤ r₀/(4(Q+1)t_i), |h − 1| ≤ ½ and |log h| ≤ log 2.

*Proof.* Fix z in the polydisc and let s := Σ|z_i|t_i ≤ 2·r₀/(4(Q+1)) = r₀/(2(Q+1)). The function φ(λ) := (h(λz) − 1)/(Q + 1) is holomorphic on |λ| < r₀/s, |φ| ≤ 1, φ(0) = 0; Schwarz's lemma gives |φ(1)| ≤ s/r₀ ≤ 1/(2(Q+1)), so |h(z) − 1| ≤ ½. Then log h = Σ_{n≥1}(−1)^{n+1}(h−1)^n/n has |log h| ≤ Σ 2^{−n}/n = log 2. ∎

### 3.5 The shape class

**Lemma 3.6.** For (f,h) ∈ 𝔗(d; ϑ), 10^{−8}ϑ² ‖f‖_∞‖h‖_∞ ≤ K_free(f,h) ≤ v₄²‖f‖_∞‖h‖_∞, v₄ = π²/2.

*Proof.* For x ∈ supp f, y ∈ supp h: |x − y| ≥ d, and |x − y| ≤ dist(supp f, supp h) + diam(supp f) + diam(supp h) ≤ 6d + 2d + 2d = 10d. Hence (10d)^{−8}∫f∫h ≤ K_free ≤ d^{−8}∫f∫h, and ϑ‖f‖_∞d⁴ ≤ ∫f ≤ v₄d⁴‖f‖_∞. ∎

**Lemma 3.7** (lattice kernel sums). Let u, v be supported in radius-2d balls whose distance is ≥ d/2, and let a ≤ d/20. Then Σ_{p,q} |u(x(p))||v(x(q))| a⁸ |x(p) − x(q)|^{−8} ≤ C₇ ‖u‖_∞‖v‖_∞, with C₇ absolute (six orientations per site counted).

*Proof.* A ball of radius 2d contains at most (4d/a + 1)⁴ ≤ (5d/a)⁴ sites (as d/a ≥ 1), so at most N_d := 6(5d/a)⁴ plaquette barycentres (six orientations per site, barycentres displaced by a/2·(e_μ + e_ν), which only enlarges the ball by a ≤ d/20 — absorbed by using radius 2d + a ≤ 2.05d and 4.1d/a + 1 ≤ 5d/a). Each pair has |x(p) − x(q)| ≥ d/2, so the sum is ≤ N_d² a⁸ (d/2)^{−8}‖u‖‖v‖ = 36·5⁸·2⁸ ‖u‖_∞‖v‖_∞ =: C₇‖u‖_∞‖v‖_∞. ∎

### 3.6 The four-dimensional arithmetic

**Lemma 3.8** (summability of large-field costs along one lineage). Let p > 1, c > 0, λ > 0, X ≥ e. Then Σ_{m≥0} exp[−c(log(X + λm))^p] ≤ (1 + λ^{−1}) X^{−1} exp[−(c/2)(log X)^p] when (c/2)(log X)^{p−1} ≥ 2.

*Proof.* Put t_m := log(X + λm) ≥ log X. Since p > 1 and t_m ≥ log X, c t_m^p ≥ (c/2)(log X)^p + (c/2)t_m^{p−1}t_m ≥ (c/2)(log X)^p + 2 t_m. So each term is ≤ e^{−(c/2)(log X)^p}(X + λm)^{−2}, and Σ_m (X + λm)^{−2} ≤ X^{−2} + ∫₀^∞(X + λu)^{−2}du = X^{−2} + (λX)^{−1} ≤ (1 + λ^{−1})X^{−1}. ∎

**Lemma 3.9** (the 4D union bound diverges; the 3D one converges). Let 𝔭 > 1, c > 0.

(a) (4D, marginal coupling.) If x_j = x + λ(k − j) + O(1) for j ≤ k (linear growth, IN1(3)), then for every k and every cell c of level k, Σ_{m ≥ 0} L^{4m} exp[−c(log x_{k−m})^{𝔭}] = +∞ as k → ∞ along any sequence with x fixed; precisely, the partial sum up to m ≤ k is ≥ exp[4k log L − c(log(x + λk + O(1)))^{𝔭}] → ∞.

(b) (3D, super-renormalisable coupling.) If x_j ≥ x L^{(k−j)} (Y3 L87778–87785: x̄_s = L^{s+1}(g^{−2} + B̄)), then Σ_{m≥0} L^{3m}exp[−c(log x_{k−m})^{𝔭}] ≤ C(c, 𝔭, L) exp[−c(log x)^{𝔭}].

*Proof.* (a) The m = k term alone is L^{4k}exp[−c(log(x + λk + O(1)))^𝔭], and 4k log L − c(log(x+λk+O(1)))^𝔭 → ∞ because (log k)^𝔭 = o(k). (b) log x_{k−m} ≥ log x + m log L. By superadditivity (a + b)^𝔭 ≥ a^𝔭 + b^𝔭 for a, b ≥ 0, 𝔭 ≥ 1: c(log x + m log L)^𝔭 ≥ c(log x)^𝔭 + c(m log L)^𝔭 ≥ c(log x)^𝔭 + 4m log L for m ≥ m₁(c, 𝔭, L), and for m < m₁ use c(log x + m log L)^𝔭 ≥ c(log x)^𝔭 and absorb L^{3m₁} into C. Then Σ L^{3m}e^{−c(log x_{k−m})^𝔭} ≤ e^{−c(log x)^𝔭}[C(m₁) + Σ_m L^{−m}]. ∎

**What Lemma 3.9 means.** The number of positions at level k − m inside one level-k cell is L^{4m} (L^{3m} in 3D), and the rarity of a newly created large-field region at level j is at best exp[−c p₀(g_j)] = exp[−c(log x_j)^{𝔭₀}] (LF1(3)). In 3D the coupling x_j grows exponentially in the number of finer levels, so (b) shows that the union over all creation levels and positions is small: no history persistence needs to be controlled. This is exactly how Y3 controls "the remaining history" by "the rarity of early large-field regions" (Y3 L791–797), and why its Corollary IV-68-44 has a "volume-dependent tail" x_k²t_T controlled by the small-torus condition (Y3 L87712–87750). In 4D the coupling grows only linearly (asymptotic freedom with a marginal coupling), so (a) shows that creation rarity alone cannot pay for the positions: almost every coarse cell contains *some* fine-level large-field creation. What saves the two-point function is that a fine-level region matters only if it persists (or grows) to the scale of the pair. That persistence is AG1 (SA D3, L4165–4176: "A rarity estimate for one newly created component is insufficient for this persistence assertion"). Lemma 3.9(a) is the arithmetic content of that sentence.

---

## 4. F3: the running normalisation [proved from OL1(2),(3),(5), IN1(3),(4) and TP-slope]

### 4.1 A lower flow bound without the increment law

**Lemma 4.1.** Assume OL1(2), OL1(3), OL1(5) and let g ≤ γ₄ with γ₄ small. Then for all 0 ≤ i ≤ k up to first passage,
(c₀/2)(k − i) − 2c₂ ≤ x_i − x_k ≤ (c₀ + 1)(k − i) + 2c₂.   (4.1)

*Proof.* First, x_j > g^{−2} for all j ≤ K. Indeed x₀ = β ≥ g^{−2} + B_♯ (IN1(4)), and if j < K then x_j lies outside the window (g^{−2}, g^{−2} + B_♯] because K is the first passage; if x_j > g^{−2} + B_♯ then x_{j+1} = x_j − b_{j+1} ≥ x_j − B_♯ > g^{−2} (IN1(3): b ≤ B_♯), so x_{j+1} is either in the window (then j + 1 = K) or again above it. Induction gives x_j > g^{−2} + B_♯ for j < K and x_K > g^{−2}.
Next, x_i − x_k = Σ_{j=i+1}^{k} b_j = (A_k − A_i) + Σ_{j=i+1}^k (f_j + q_j), by OL1(2) (telescoping b_j⁰ = A_j − A_{j−1}). By OL1(3), |A_k − A_i − c₀(k − i)| ≤ 2c₂. Since t ↦ t^{−1/2}(log t)^𝔭 and t ↦ t^{−(κ₀−4)/2} decrease for t ≥ e^{2𝔭}, and x_{j−1} > g^{−2}, OL1(5) gives |f_j| + |q_j| ≤ C g(log g^{−2})^𝔭 + C g^{κ₀−4} ≤ min{c₀/2, 1} for g ≤ γ₄. Summing over k − i terms gives (4.1). ∎

So E1's lower bound holds with λ = c₀/2 and C = 2c₂, and its upper bound with B_♯ := c₀ + 1 + 2c₂, **without OL1(4)**. (`rf10-incr.md` showed OL1(3) does not give the increment law; F3 does not need it.)

### 4.2 The coupling at the witness scale

**Proposition 4.2.** Under the hypotheses of Lemma 4.1, uniformly in first-passage data (K, β) at g,
g(d)^{−2} = x_{K−s(d)} = c₀ s(d) + θ₁ with |θ₁| ≤ g^{−2} + B_♯ + 2c₂ + C s(d)^{1/2}(log(g^{−2} + s(d)))^𝔭 + C,
and hence g(d)^{−2}/log(1/d) → c₀/log L = 11N²/(12π²) = c_* as d → 0, uniformly in (K, β).

*Proof.* With k = K, i = K − s: x_{K−s} − x_K = (A_K − A_{K−s}) + Σ_{j=K−s+1}^{K}(f_j + q_j). The first bracket is c₀s + O(2c₂). For the sum, x_{j−1} ≥ x_K + (c₀/2)(K − j + 1) − 2c₂ ≥ g^{−2} + (c₀/2)(K − j + 1) − 2c₂ by (4.1); so Σ_j |f_j| ≤ C Σ_{m=1}^{s} (g^{−2} + (c₀/2)m − 2c₂)^{−1/2}(log(·))^𝔭 ≤ C s^{1/2}(log(g^{−2}+s))^𝔭 and Σ_j |q_j| ≤ C Σ_m (g^{−2} + c₀m/2 − 2c₂)^{−(κ₀−4)/2} ≤ C (κ₀ > 6). Finally g^{−2} < x_K ≤ g^{−2} + B_♯ (IN1(4)). For the ratio: s(d) log L = log(1/d) + θ₂ with 0 ≤ θ₂ ≤ log(LC_W(s)) = O(log log(1/d)) (§1.1), so g(d)^{−2}/log(1/d) = (c₀ s + θ₁)/(s log L − θ₂) → c₀/log L, with an error depending only on g and d. And c₀/log L = 11N²/(12π²) by OL1's value of c₀. ∎

### 4.3 The normalisation ζ

**Proposition 4.3.** Assume TP-slope and (4.1). For g ≤ γ₄ and every k ≤ K, ζ'_k ∈ [2/3, 4/3] and
|ζ'_k − 1| ≤ C[g_k (log x_k)^{𝔭₀} + ϱ^{−1} g_k^{κ₀−6}],  g_k := x_k^{−1/2}.
In particular ζ = ζ'_{k₀} = 1 + O(g(d)(log g(d)^{−2})^{𝔭₀}) → 1 uniformly, and |ζ'_j − ζ'_{k₀}| ≤ C g(d)³(log x)^{𝔭₀}·n + C ϱ^{−1}g(d)^{κ₀−4}·n for k₀ ≤ j ≤ k₁.

*Proof.* ζ'_k − 1 = Σ_{j≤k} b'_j(0). By TP-slope and (4.1), x_j ≥ x_k + (c₀/2)(k − j) − 2c₂, so Σ_{j≤k} g_j³(log x_j)^{𝔭₀} ≤ C Σ_{m≥0}(x_k + c₀m/2 − 2c₂)^{−3/2}(log(x_k + c₀ m))^{𝔭₀} ≤ C x_k^{−1/2}(log x_k)^{𝔭₀}, and Σ_j g_j^{κ₀−4} ≤ C x_k^{−(κ₀−6)/2} since (κ₀ − 4)/2 > 1. For g small the total is ≤ 1/3. The last claim sums n terms with x_j ≥ x_{k₁} ≥ x − B_♯ n ≥ x/2. ∎

*Remark (what F3 asks).* SA F3 (L4360–4373) asks that "A derivative of a running coupling with respect to a constant source must be shown to equal this normalization". In our route ζ enters only through the marginal part of the sourced exponent (§2.2), whose coefficient is ζ'_{k} by its definition in SA (b) (L26117–26132); Proposition 4.3 bounds it. Nothing else is chosen.

---

## 5. The route, and why

### 5.1 SA's route, as read

SA §7 (L25966–26200) proves the reference law on one small torus T_{ℓ_⋆(g)} (Proposition 7.3, L26085) through the exact identity at two levels (L26094–26101):

⟨O(f₁); O(f₂)⟩ = Cov_{P^{(k)}}(Φ_1^{(k)}, Φ_2^{(k)}) + E_{P^{(k)}} Φ_{12}^{(k)},  1 ≤ k ≤ k₁.   (5.1)

At k = k₀ the covariance term is the main term; at k = k₁ the mean of the mixed derivative is (L26097–26101). Its ingredients are (a) locality and the age series 4.14 "taken with rate b ≥ 8", used "twice" at k₀ and "once" at k₁ (L26103–26117); (b) the marginal part and ζ (L26117–26132); (c) Gaussian extraction with a single-step recursion at the flat background whose "two inequalities on a single fluctuation integral" are needed (L26133–26176); (d) wild histories at k₁ with weight ≤ C(MŘ_{k₁})⁴e^{−cp₀(g_{k₁})} "and no union over the levels is taken" (L26178). The transfer to Gibbs states goes through the reference torus, ET5 and (ET8)–(ET10) (SA L26765–27085). The Gaussian comparison is where SA's own conditional law analysis meets the complete-force term (GCB52) (SA L28196–28221), for which no bound is asserted.

### 5.2 Our route

1. *One level only.* We use (5.1) at k = k₁ only (§6). There both first derivatives are small, except on live histories, and the main term is E_P Φ_{12}.
2. *Gaussian extraction by Cauchy in the complex plaquette coefficient.* E_P Φ_{12} is a sum of mixed source derivatives of regular energies. Each is the derivative at 0 of a function holomorphic on a coupling-sized disc (TP-cx). We split it into its exact Gaussian part and a remainder bounded *in sup norm* by C x_j^{−1/2}(log x_j)^q on that disc, and Cauchy's formula turns the sup bound into a derivative bound with the factor x^{−2}. This replaces both SA's single-step recursion (c3) and every force estimate: we never differentiate the density in a field direction, so the non-log-concavity of the resummed interacting density (SA L28212–28221) is irrelevant. The price is (TP-cx): the step must be holomorphic in the local coupling on a disc of relative radius r, uniformly. That is the form Y3 uses in 3D (L745–747), and the form SA F3 itself names for its slope proof (L4375–4378).
3. *Infinite-volume reference.* RL is proved on every compatible torus with thresholds independent of ℓ (§6), so its periodic limits are reference *Gibbs states*, and the common cell normaliser of SR1 transfers it to every periodic Gibbs state (§7). No finite reference torus, no ET8–ET10.
4. *NT1 by one positive reflected value* (§9), ported from Y3 IV-69-33.
5. *AG1 at one level.* Our route reads rarity only at k₁, in the weighted form (AG-k₁) of §10.1. It is used twice, both at k₁: for the mean of the live mixed derivative (weight L^{8a}) and for the live part of the covariance (weight L^{4a}·L^{4a}).

Where 4D changes the Y3 argument: (i) x_j grows linearly, so error factors are powers of x and of log x, not of L^{−s}; every Y3 smallness factor of the form x_T^{−1/2} still works because the polylogarithmic losses (log x)^C are beaten by x^{−1/2} (Y3's Corollary IV-68-44, L87712–87750, has the factor y^{15p}s_T with s_T ≥ x_T^{−1/2}, y = log x; in 4D y^{15p}x^{−1/2} → 0 still holds); (ii) the separation room C_W(s) is polylogarithmic in both, but the room d̂ ≥ C_W beats x only through e^{−c d̂} vs. x² — in 4D, x² e^{−c C_{W,0}(log x)^{2𝔭₀}} → 0 since 2𝔭₀ > 1; (iii) the coupling runs across the levels k₀..k₁, so x_j ≈ x needs B_♯ n ≪ x, true since n = O(log x); (iv) the normalisation ζ appears (Y3's label b is a fixed dimensionful constant; in 4D the source renormalises with the coupling); (v) the union bound over early large-field creations, which Y3 uses, fails (Lemma 3.9), and AG1 takes its place.

---

## 6. The reference law on every compatible torus

**Proposition RL.** Assume the imports of §2.1, the TP-inputs of §2.2 and (AG-k₁). There are γ_W, n₀ and d₀(g) such that for g ≤ γ_W, every first-passage datum (K, β) at g, every compatible torus T_ℓ (ℓ = 2L^m, m ≥ m₀, any m), every d ≤ d₀ with K − s(d) ≥ n₀ and every (f, h) ∈ 𝔗(d; ϑ_*) placed anywhere on T_ℓ,

⟨O(f); O(h)⟩_{K,ℓ,β} = ζ² C_G g(d)⁴ K_free(f,h)(1 + R),   |R| ≤ ε_RL(d) ≤ ¼,   (6.0)

with ε_RL non-decreasing, ε_RL(d) → 0 as d → 0, independent of K, β, ℓ and the position of the pair.

Status: [proved] from the stated inputs. The proof occupies §6.1–6.7. Throughout, f₁ = f, f₂ = h, x = x_{k₀} = g(d)^{−2}, ζ = ζ'_{k₀}, and "o(x^{−2})" means a quantity bounded by ε(d) x^{−2}‖f‖_∞‖h‖_∞ with ε(d) → 0 depending only on g, ϑ_* and the fixed constants.

### 6.1 The exact identity at level k₁

**Lemma 6.1** (ref-73 (3); SA L26094–26101). Under (TP-pres), with Φ_i := ∂_{z_i}Φ(0; y) and Φ_{12} := ∂_{z₁}∂_{z₂}Φ(0; y),

⟨O(f₁); O(f₂)⟩ = Cov_P(Φ_1, Φ_2) + E_P Φ_{12}.   (6.1)

*Proof.* By Lemma 3.1, ⟨O(f₁);O(f₂)⟩ = ∂₁∂₂ log(Z(z)/Z(0))|₀. By (2.2), Z(z)/Z(0) = E_P e^{Φ(z;y)} with differentiation under E_P. So ∂_i(Z/Z₀) = E_P[Φ_i(z)e^{Φ}] and ∂₁∂₂(Z/Z₀) = E_P[(Φ_{12}(z) + Φ_1(z)Φ_2(z))e^{Φ}]. At z = 0, Φ = 0 and Z/Z₀ = 1, so ∂₁∂₂ log(Z/Z₀)|₀ = E_P[Φ_{12} + Φ_1Φ_2] − E_PΦ_1 E_PΦ_2. ∎

### 6.2 The free running model and its template

Slices. Let P_ex = Σ_{j=1}^K G_j be the free orthogonal decomposition (§2.1, (2.1)). For each colour α = 1, …, N² − 1 let φ_j^{(α)} be independent centred Gaussian fields on plaquettes with covariance G_j, independent over j and α. The *free running model* at level k₁ is the Gaussian field F^{(α)} := Σ_{j ≤ k₁} x_j^{−1/2} φ_j^{(α)}, with covariance

C_{≤k₁} := Σ_{j≤k₁} x_j^{−1} G_j.

Source transport (SA (b), L26117–26132; this is how the sourced construction carries a source as a local coupling change):
- (S1) the bare vertex: the source couples to Σ_p w(x(p)) ½|F_p|² (all slices);
- (S2) the counterterm vertices: at each level j the counterterm of step j carries the source as b'_j(0) Σ_y h_y^{(j)}(p) w(x(p_y)) times the level-j action density; it couples only to the slices i > j (it is a term of the level-j effective action, a function of the level-j field). The tents h_y^{(j)} ≥ 0 have range C M a_{(j)} and Σ_y h_y^{(j)} = 1.

Define the *template*, for u, v supported in radius-2d balls at distance ≥ d/2,

T(u, v) := ((N² − 1)/2) Σ_{p,q} u(x(p)) v(x(q)) tr[C_{≤k₁}(p,q) C_{≤k₁}(q,p)].

By Lemma 3.3 (applied to the joint Gaussian vector of all F_p^{(α)}), T(u,v) is the covariance of Σ_p u ½|F_p|² and Σ_q v ½|F_q|² in the free running model. The Gaussian parts e_j^G(X; ·, 𝟙) of (TP-cx) are, by their definition there, the localised pieces of the free running model's sourced log-partition function with transport (S1)–(S2); their mixed derivatives therefore sum exactly to the mixed derivative of that Gaussian sourced exponent. By Lemma 3.3 applied vertex by vertex (each vertex is a quadratic form in the Gaussian field), that mixed derivative is

Γ₁₂ := T_{11}(f, h) + Σ_{j ≤ k₁} b'_j(0)[T_{j1}(f^{(j)}, h) + T_{1j}(f, h^{(j)})] + Σ_{j,j'} b'_j(0)b'_{j'}(0) T_{jj'}(f^{(j)}, h^{(j')}),   (6.2)

where f^{(j)}(p) := Σ_y h_y^{(j)}(p) f(x(p_y)), and T_{jj'} is T with C_{≤k₁} replaced by C_{(j∨j',k₁]} := Σ_{j∨j' < i ≤ k₁} x_i^{−1}G_i in both legs (both legs of a pairing between a vertex coupling to slices > j and one coupling to slices > j' run through slices > max(j, j')); index 1 means "all slices" (j = 0).

### 6.3 Kernel bounds

**Lemma 6.2.** For plaquettes p, q at distance r := |x(p) − x(q)| ≥ a_K and every 0 ≤ j₀ < j₁ ≤ k₁:
(a) |C_{(j₀,j₁]}(p,q)| ≤ 2C_s c_δ x^{−1} (a_K/r)⁴, with c_δ := sup_{t>0} Σ_{i∈Z} (tL^i)⁴e^{−δ_s tL^i} < ∞;
(b) Σ_{j ≤ k₀}|G_j(p,q)| ≤ C_s c'_δ (a_K/r)⁴ (r a_{(k₀)}^{−1})⁴ e^{−δ_s r/(2a_{(k₀)})} when r ≥ a_{(k₀)};
(c) Σ_{j > k₁}|G_j(p,q)| ≤ C_s (1 − L^{−4})^{−1} (a_K/a_{(k₁)})⁴.

*Proof.* (a) By (2.1), |G_i(p,q)| ≤ C_s(a_K/r)⁴ t_i⁴ e^{−δ_s t_i} with t_i := r/a_{(i)} = (r/a_K)L^{−i}, a geometric sequence; the sum over i is ≤ c_δ, finite since t⁴e^{−δt} is summable over a geometric sequence in both directions (≤ Σ_{i: t_i ≤ 1} t_i⁴ + Σ_{i: t_i > 1} C_δ t_i^{−1}). For i ≤ k₁, x_i ≥ x_{k₁} ≥ x − B_♯ n ≥ x/2 by (4.1) and n = O(log x), so x_i^{−1} ≤ 2x^{−1}. (b) For j ≤ k₀, t_j = r/a_{(j)} = t₀L^{k₀−j} with t₀ := r/a_{(k₀)} ≥ 1. Then Σ_{j≤k₀} t_j⁴e^{−δ_s t_j} = t₀⁴e^{−δ_s t₀/2} Σ_{i≥0} L^{4i} e^{−δ_s t₀(L^i − ½)} ≤ t₀⁴e^{−δ_s t₀/2} Σ_{i≥0}L^{4i}e^{−δ_s(L^i − ½)} =: c'_δ t₀⁴e^{−δ_s t₀/2}, using t₀ ≥ 1; multiply by C_s(a_K/r)⁴. (c) |G_j(p,q)| ≤ C_s(a_K/a_{(j)})⁴ = C_s(a_K/a_{(k₁)})⁴ L^{−4(j−k₁)}; sum the geometric series. ∎

Consequences, for p ∈ supp f-neighbourhood and q ∈ supp h-neighbourhood (r ∈ [d/2, 11d]):
- r/a_{(k₀)} ≥ d̂/2 ≥ C_W/2;
- (a_K/a_{(k₁)})⁴ = (a_K/r)⁴ (r/a_{(k₁)})⁴ ≤ (a_K/r)⁴ (11 d̂ L^{−n})⁴ ≤ (a_K/r)⁴ (11 L C_W x̄^{−2})⁴, since a_{(k₁)} = L^n a_{(k₀)} = L^n d/d̂ and L^n ≥ x̄².

### 6.4 The template equals the free law

**Lemma 6.3.** Γ₁₂ = ζ² C_G x^{−2} K_free(f,h) + o(x^{−2}).

*Proof.* Step 1 (counterterms of levels j ≤ k₀ give ζ). For j ≤ k₀ the tents have range CMa_{(j)} ≤ CMd/d̂ ≤ d/8 (d ≤ d₀ makes d̂ ≥ C_W ≥ 8CM), so f^{(j)} is supported in the d/8-neighbourhood of supp f and |f^{(j)}| ≤ ‖f‖_∞. In T_{j1}, both legs run through slices > j. Split C_{≤k₁} = C_{≤k₀} + C_{(k₀,k₁]}. Every pairing in which some leg uses a slice ≤ k₀ is bounded by C x^{−2} d̂⁴ e^{−δ_s d̂/4}‖f‖‖h‖ = o(x^{−2}): that leg is ≤ C_s c'_δ x^{−1}(a_K/r)⁴ t₀⁴e^{−δ_s t₀/2} by Lemma 6.2(b) (with x_j ≥ x for j ≤ k₀), the other leg is ≤ 2C_s c_δ x^{−1}(a_K/r)⁴ by Lemma 6.2(a), r ∈ [d/2, 11d] gives t₀ ∈ [d̂/2, 11d̂] and t₀⁴e^{−δ_s t₀/2} ≤ 11⁴d̂⁴e^{−δ_s d̂/4}, and Σ_{p,q}|u||v|(a_K/r)⁸ ≤ C₇‖u‖‖v‖ by Lemma 3.7. Removing these pairings from T_{11}, T_{j1}, T_{1j}, T_{jj'} (j, j' ≤ k₀) leaves the same kernel C_{(k₀,k₁]} in every term, so by bilinearity the j, j' ≤ k₀ part of (6.2) equals

T_dom(f + Σ_{j≤k₀} b'_j f^{(j)}, h + Σ_{j≤k₀} b'_j h^{(j)}) + o(x^{−2}) = ζ² T_dom(f̃, h̃) + o(x^{−2}),

where T_dom is T with kernel C_{(k₀,k₁]} and ζ f̃ := f + Σ_{j≤k₀} b'_j(0) f^{(j)} is SA's definition (L26117–26132: ∂_{z_i}ζ_{k₀}(p;w)|₀ =: ζ'_{k₀} f̃_i(p)).

Step 2 (counterterms of levels j ∈ (k₀, k₁] are small). For such j, ‖f^{(j)}‖_{L¹} ≤ ‖f‖_{L¹} ≤ v₄ d⁴‖f‖_∞ (the tents sum to 1), and both legs run through slices > j, with |C_{(j,k₁]}(p,q)| ≤ 2C_s(1 − L^{−4})^{−1} x^{−1}(a_K/a_{(j)})⁴ by (2.1) summed geometrically. Therefore |T_{j1}(f^{(j)}, h)| ≤ C x^{−2} (a_K/a_{(j)})⁸ (Σ_p|f^{(j)}(x(p))|)(Σ_q|h(x(q))|) ≤ C x^{−2} a_{(j)}^{−8} ‖f‖_{L¹}‖h‖_{L¹} ≤ C x^{−2} (d/a_{(j)})⁸ ‖f‖_∞‖h‖_∞ (lattice sums Σ_p|u(x(p))| ≤ 6 a_K^{−4}(‖u‖_{L¹} + C a_K Lip-terms), absorbed). With d/a_{(j)} = d̂ L^{−(j−k₀)} and |b'_j(0)| ≤ C x^{−3/2}(log x)^{𝔭₀} + Cϱ^{−1}x^{−(κ₀−4)/2} (TP-slope; x_j ≥ x/2), Σ_{k₀<j≤k₁}|b'_j||T_{j1}| ≤ C x^{−2} d̂⁸ [x^{−3/2}(log x)^{𝔭₀} + x^{−(κ₀−4)/2}] ‖f‖‖h‖ = o(x^{−2}), since d̂ ≤ LC_W = O((log x)^{2𝔭₀}). The same bound holds for T_{1j} and, with an extra factor Σ|b'|, for the T_{jj'} terms with j or j' > k₀.

Step 3 (f̃ → f). By SA (L26117–26132), |f̃ − f| ≤ (CM/(ϑ d̂)) Σ_j|b'_j(0)| ‖f‖_∞ ≤ C(ϑ C_W)^{−1} ‖f‖_∞, with supports in the d/8-neighbourhood. By Lemma 6.2(a) and Lemma 3.7 (radius-2d balls at distance ≥ d/2), |T_dom(u,v)| ≤ C x^{−2}‖u‖_∞‖v‖_∞ for such u, v. Bilinearity gives |T_dom(f̃,h̃) − T_dom(f,h)| ≤ C x^{−2}(ϑC_W)^{−1}‖f‖‖h‖ = o(x^{−2}).

Step 4 (running coupling → x). C_{(k₀,k₁]} − x^{−1}P_ex = Σ_{k₀<j≤k₁}(x_j^{−1} − x^{−1})G_j − x^{−1}Σ_{j≤k₀}G_j − x^{−1}Σ_{j>k₁}G_j. For k₀ < j ≤ k₁, 0 ≤ x − x_j ≤ (c₀ + 1)n + 2c₂ by (4.1), so |x_j^{−1} − x^{−1}| ≤ 2((c₀+1)n + 2c₂)x^{−2}. With Lemma 6.2:
|C_{(k₀,k₁]}(p,q) − x^{−1}P_ex(p,q)| ≤ C x^{−1}(a_K/r)⁴ ε₃,  ε₃ := n/x + d̂⁴e^{−δ_s d̂/4} + (11LC_W x̄^{−2})⁴.
Since |tr(AA') − tr(BB')| ≤ 6(|A − B|(|A'| + |B'|) + ...) entrywise for 6 × 6 matrices, and |P_ex(p,q)| ≤ C(a_K/r)⁴ (FC1 with r ≥ d ≥ 10a_K), |tr C_{(k₀,k₁]}(p,q)C_{(k₀,k₁]}(q,p) − x^{−2}tr P_ex(p,q)P_ex(q,p)| ≤ C x^{−2}(a_K/r)⁸ ε₃. Summing with Lemma 3.7: |T_dom(f,h) − x^{−2}((N²−1)/2)Σ_{p,q} f h tr P_ex(p,q)²| ≤ C x^{−2}ε₃‖f‖‖h‖ = o(x^{−2}).

Step 5 (free comparison, FC1). For r = |x(p) − x(q)| ∈ [d, 10d], a_K ≤ r/10 and r ≤ ℓ/10 (ℓ ≥ 2L^{m₀} ≥ 10 and r ≤ 10d₀ < 1), FC1 gives |a_K^{−4}P_ex(p_P,q_Q) − K_{P,Q}(x(p) − x(q))| ≤ C r^{−4}[(a_K/r)^{1/2} + (r/ℓ)⁴]. Hence |a_K^{−8}tr P_ex(p,q)P_ex(q,p) − Σ_{P,Q}K_{PQ}(u)²| ≤ C r^{−8}[(a_K/d)^{1/2} + (10d/ℓ)⁴] with u = x(p) − x(q). Summing over plaquettes with weight a_K⁸ and Lemma 3.7, the error is ≤ C[(a_K/d)^{1/2} + d⁴]‖f‖‖h‖, since ℓ ≥ 10 gives (10d/ℓ)⁴ ≤ d⁴. The remaining Riemann sum Σ_{p,q} a_K⁸ f(x(p))h(x(q)) Σ_{P,Q}K_{PQ}(x(p) − x(q))² over sites and orientations converges to ∬ f h tr𝕂(x − y)² = 6π^{−4}K_free(f,h) with error ≤ C(a_K/(ϑ d))‖f‖‖h‖: the summand's gradient in either variable is ≤ (Lip f/‖f‖ + Lip h/‖h‖ + 8/r)‖f‖‖h‖ C r^{−8} ≤ C(ϑd)^{−1}‖f‖‖h‖ d^{−8}, the cells have side a_K, the orientation offsets are ≤ a_K, and the integration region has volume ≤ (v₄(2d)⁴)². Since a_K/d = (d̂L^{k₀})^{−1} ≤ L^{−n₀}C_W^{−1}, all these errors are o(1)‖f‖‖h‖.

Step 6 (assembly). Combining Steps 1–5: Γ₁₂ = ζ²·x^{−2}·((N²−1)/2)·6π^{−4}K_free(f,h) + o(x^{−2}) = ζ²C_G x^{−2}K_free + o(x^{−2}), using ζ² ≤ 16/9 (Proposition 4.3) to keep the errors multiplied by ζ² of the same form. ∎

### 6.5 The regular remainder

**Lemma 6.4.** On every history y whose V is in the small-field domain on the O(1) cells of level k₁ near the supports and which has no live component there,

|Φ_{12}^{reg}(y) − Γ₁₂| ≤ C x^{−5/2}(log x)^{q+C} n d̂⁴ ‖f‖‖h‖ = o(x^{−2}),

and Φ_{12}^{pt} = 0, Φ_{12}^{live} = 0, |Φ_{12}^{far}| ≤ C x^{−2}e^{−cd̂}‖f‖‖h‖.

*Proof.* Φ^{pt}: §2.2 (each piece depends on one value of w and f₁f₂ = 0). Φ^{live} = 0 by (TP-live) (no live component). Φ^{far}: (TP-far). For Φ^{reg} = Σ_{j≤k₁}Σ_{X∈𝒟_j} e_j(X; z, V): only domains whose X^+ meets both supports have a nonzero mixed derivative (Lemma 3.4). By (2.4), e_j(X) − e_j^G(X;·,𝟙) = ρ_j(X;·,V) is holomorphic on 𝔻_j(X) ⊃ {|z_i| ≤ ½ r x_j/‖f_i‖_∞} with |ρ_j| ≤ C x_j^{−1/2}(log x_j)^q e^{−κm_j(X)}; Lemma 3.4 gives |∂₁∂₂ρ_j(X)| ≤ 4 C r^{−2} x_j^{−5/2}(log x_j)^q e^{−κm_j(X)}‖f‖‖h‖. The Gaussian parts sum to Γ₁₂ (§6.2). It remains to count.

Counting. Let D_j := dist(supp f, supp h)/(M' a_{(j)}) − 1 ≥ d/(M'a_{(j)}) − 1, where M' is the number of cell diameters per tree edge (a fixed multiple of M by the dependence-layer convention of D1: E_X depends on w only on a fixed number of neighbouring cube layers). A domain whose enlargement meets both supports has m_j(X) ≥ D_j. The number of level-j cells within the enlargement-distance of supp f is ≤ C(d/a_{(j)} + 1)⁴. The number of domains X containing a given cell with m_j(X) = m is ≤ C e^{ϵm} (rooted entropy, κ > ϵ). Hence

Σ_{X: X^+ meets both} e^{−κ m_j(X)} ≤ C(d/a_{(j)} + 1)⁴ Σ_{m ≥ max(D_j,0)} e^{−(κ−ϵ)m} ≤ C'(d/a_{(j)} + 1)⁴ e^{−(κ−ϵ)max(D_j,0)}.

For j ≤ k₀: d/a_{(j)} = d̂L^{k₀−j}, D_j ≥ d̂L^{k₀−j}/M' − 1, and Σ_{j≤k₀} (2d̂L^{k₀−j})⁴e^{−(κ−ϵ)(d̂L^{k₀−j}/M' − 1)} ≤ C d̂⁴ e^{−(κ−ϵ)d̂/M'}·C'' (geometric). For k₀ < j ≤ k₁: the bound is ≤ C(d̂ + 1)⁴ for each of the n levels. With x_j ≥ x/2 for j ≤ k₁ and x_j ≥ x for j ≤ k₀,

|Φ^{reg}_{12} − Γ₁₂| ≤ C x^{−5/2}(log x)^q [d̂⁴e^{−cd̂} + n(d̂ + 1)⁴]‖f‖‖h‖.

With n = O(log x) and d̂ ≤ LC_W = O((log x)^{2𝔭₀}), this is ≤ C x^{−5/2}(log x)^{q + 8𝔭₀ + 1}‖f‖‖h‖ = o(x^{−2}). ∎

### 6.6 Live histories and the covariance term

Let Λ := {y : some live component meets the CMŘ-neighbourhood of supp f ∪ supp h at level k₁}. By the definition of the large-field regions, every history whose V fails the small-field condition on the cells near the supports is in Λ (a cell failing the small-field test at level k₁ is a large-field region of level k₁, i.e. live with age 0). Define the weighted live tail at level k₁ near the pair

𝔄 := E_P[L^{8a(y)} 𝟙_Λ(y)],  (a(y) as in TP-live).

By (AG-k₁) (§10.1) and the fact that O(1)·(CMŘ_{k₁})⁴ cells of level k₁ meet the neighbourhood (SA (d), L26178: "(MŘ_{k₁})⁴ counts the sites of level k₁ in one cell of that level, and O(1) cells touch the supports"),

𝔄 ≤ C (MŘ_{k₁})⁴ Σ_{a≥0} L^{8a} sup_c P(live lineage of age ≥ a meets c) ≤ C (log x)^{C} e^{−c p₀(g_{k₁})}.   (6.3)

**Lemma 6.5** (mean of the mixed derivative). E_P Φ_{12} = Γ₁₂ + o(x^{−2}).

*Proof.* Split E_P Φ_{12} = E_P[Φ_{12}𝟙_{Λ^c}] + E_P[Φ_{12}𝟙_Λ]. On Λ^c, Lemma 6.4 gives Φ_{12} = Γ₁₂ + o(x^{−2}), so E_P[Φ_{12}𝟙_{Λ^c}] = Γ₁₂ P(Λ^c) + o(x^{−2}). On Λ: |Φ^{live}_{12}| ≤ C x^{−2}(log x)^C L^{8a}‖f‖‖h‖ (TP-live); |Φ^{reg}_{12}| ≤ C x^{−2}[d̂⁴ + n(d̂+1)⁴]‖f‖‖h‖ by the same counting as Lemma 6.4 applied to |e_j| ≤ Ce^{−κm} (Cauchy on 𝔻_j); Φ^{pt}_{12} = 0; Φ^{far} as before. So |E_P[Φ_{12}𝟙_Λ]| ≤ C x^{−2}(log x)^C(𝔄 + P(Λ))‖f‖‖h‖ ≤ C x^{−2}(log x)^C𝔄 ‖f‖‖h‖, since P(Λ) ≤ 𝔄. By (6.3) and 𝔭₀ large (p₀(g_{k₁}) = (log x_{k₁})^{𝔭₀} ≥ (log(x/2))^{𝔭₀}), (log x)^{2C}e^{−cp₀(g_{k₁})} → 0. Finally |Γ₁₂|P(Λ) ≤ C x^{−2}𝔄‖f‖‖h‖ by Lemma 6.3 and Lemma 3.6. ∎

**Lemma 6.6** (the covariance term). |Cov_P(Φ_1, Φ_2)| = o(x^{−2}).

*Proof.* Write Φ_i − c_i = A_i + B_i + D_i with A_i := ∂_i(Φ^{pt} + Φ^{reg}) − c_i, B_i := ∂_iΦ^{far}, D_i := ∂_iΦ^{live}. Covariance is bilinear and |Cov(X, Y)| ≤ ‖X‖_{L²(P)}‖Y‖_{L²(P)}, so |Cov_P(Φ_1,Φ_2)| ≤ (‖A_1‖ + ‖B_1‖ + ‖D_1‖)(‖A_2‖ + ‖B_2‖ + ‖D_2‖). Bounds:
- ‖A_i‖² ≤ [C x^{−1}(log x)^C(d̂L^{−n})²]²‖f_i‖² + [C x^{−1}(log x)^C]²‖f_i‖² P(Λ), by (2.5) off Λ and the crude bound on Λ. Since d̂L^{−n} ≤ LC_W x̄^{−2}, ‖A_i‖ ≤ C x^{−1}[(log x)^C x^{−4} + (log x)^C 𝔄^{1/2}]‖f_i‖.
- ‖B_i‖ ≤ C x^{−1}e^{−cd̂}‖f_i‖ (TP-far).
- ‖D_i‖² ≤ C x^{−2}(log x)^{2C}E_P[L^{8a}𝟙_Λ]‖f_i‖² = C x^{−2}(log x)^{2C}𝔄‖f_i‖² (TP-live: |D_i| ≤ Cx^{−1}(log x)^C L^{4a}‖f_i‖, squared gives L^{8a}).
Hence |Cov_P(Φ_1,Φ_2)| ≤ C x^{−2}[(log x)^C x^{−4} + e^{−cd̂} + (log x)^C𝔄^{1/2}]²‖f‖‖h‖ = o(x^{−2}) by (6.3). ∎

This is where the weight L^{8a} enters twice, as SA says (L26103–26117): once in the mean (Lemma 6.5) and once in the product of two live first derivatives, L^{4a}·L^{4a} (Lemma 6.6). In our route both uses are at the single level k₁.

### 6.7 Proof of Proposition RL

By Lemma 6.1, ⟨O(f);O(h)⟩ = Cov_P(Φ_1,Φ_2) + E_PΦ_{12}. By Lemmas 6.5, 6.6 and 6.3, this equals ζ²C_G x^{−2}K_free(f,h) + E with |E| ≤ ε(d)x^{−2}‖f‖‖h‖, ε(d) → 0 depending only on g, ϑ_* and the fixed constants. By Lemma 3.6, K_free ≥ 10^{−8}ϑ_*²‖f‖‖h‖, and ζ² ≥ 4/9 (Proposition 4.3). So R := E/(ζ²C_Gx^{−2}K_free) satisfies |R| ≤ ε(d)·(9/4)·10⁸ϑ_*^{−2}C_G^{−1} =: ε_RL(d). Replace ε_RL by its non-decreasing majorant sup_{d'≤d}; it still tends to 0. Choose d₀(g) with ε_RL(d₀) ≤ ¼. Nothing in the bounds depends on ℓ (FC1's (r/ℓ)⁴ term was bounded using ℓ ≥ 10 only), K, β, or the position. ∎

*Note on the threshold.* d₀ depends on g through x̄_s, C_W(s) and the requirement that d̂ ≥ C_W be large; ε_RL(d) → 0 as d → 0 at fixed g, because x = g(d)^{−2} → ∞ (Proposition 4.2) and every error is a negative power of x times a power of log x, or e^{−c d̂}, or e^{−cp₀(g_{k₁})}·(log x)^C.

---

## 7. Transfer to every periodic Gibbs state

### 7.1 Two periodic states differ by O(d²)

**Proposition 7.1.** Assume the common cell normaliser of SR1 and LG1(5). For any two periodic Gibbs states ρ, ν ∈ 𝒢_{a_K,β} at a first-passage datum, every d ≤ d₀ with a_K ≤ d/40, and every (f,h) ∈ 𝔗(d; ϑ),

|S^T_2[ρ](f,h) − S^T_2[ν](f,h)| ≤ D_ϑ d² ‖f‖_∞‖h‖_∞,  D_ϑ := C_N ϑ^{−2},

with C_N depending only on Q, r₀, c_M and the cell geometry. [proved]

*Proof.* (This is the arithmetic of `tu10.md` (8), re-proved with the infinite-volume normaliser in place of ET5.)

Step 1 (a signed packing). Fix a cell C of side l and a ball B_R ⊂ C of radius R = 1 at distance > b from ∂C, as in the normaliser statement. Choose lattice vectors v₁, …, v_N ∈ a_K Z⁴ with 20d ≤ |v_k − v_{k'}| ≤ 40d for nearest pairs, forming a grid, such that every translate B(x_f + v_k, d) ∪ B(x_h + v_k, d) lies in B_R (after translating the pair to the centre of B_R; translation does not change S^T by LG1(5)). A grid of spacing between 20d and 40d inside a ball of radius ½ gives N ≥ c₈ d^{−4} with c₈ absolute, for d ≤ d₀. For signs σ ∈ {±1}^N put F₁^σ := Σ_k σ_k f(· − v_k), F₂^σ := Σ_k σ_k h(· − v_k). For k ≠ k', |(x_f + v_k) − (x_h + v_{k'})| ≥ 20d − |x_f − x_h| ≥ 20d − 8d, so the supports of distinct translates are ≥ 8d apart; also f(·−v_k) and h(·−v_k) are the original pair.

Step 2 (norms). The translates have disjoint supports, so ‖F_i^σ‖_∞ = ‖f_i‖_∞. Each translate vanishes outside its support; for x, y in different supports the segment [x, y] leaves both, so |F(x) − F(y)| ≤ Lip(f_i)(dist(x, ∂) + dist(y, ∂)) ≤ Lip(f_i)|x − y|; hence Lip F_i^σ ≤ Lip f_i ≤ ‖f_i‖_∞/(ϑd). So ‖F_i^σ‖_♯ = max(‖F‖_∞, c_M Lip F) ≤ (1 + c_M/(ϑd))‖f_i‖_∞ ≤ 2c_M(ϑd)^{−1}‖f_i‖_∞ for d ≤ c_M ϑ.

Step 3 (Cauchy through the normaliser). For a periodic Gibbs state ω, z ↦ ω(exp(z₁O(F₁) + z₂O(F₂))) is entire (O(F_i) is a finite sum of bounded continuous local functions) and equals e^{E_C(z)}h_ω(z). On the polydisc |z_i| ≤ ρ_i := r₀/(4(Q + 1)‖F_i‖_♯), Lemma 3.5 gives |log h_ω| ≤ log 2, so log ω(e^{z·O}) = E_C(z) + log h_ω(z) there, and S^T[ω](F₁,F₂) = ∂₁∂₂E_C(0) + ∂₁∂₂ log h_ω(0) (Lemma 3.1's computation for the state ω). The term ∂₁∂₂E_C(0) is the same for ρ and ν. By Lemma 3.4, |∂₁∂₂ log h_ω(0)| ≤ log 2/(ρ₁ρ₂). Hence

|D(F₁^σ, F₂^σ)| ≤ 2 log 2 · 16 (Q+1)² r₀^{−2} ‖F₁^σ‖_♯‖F₂^σ‖_♯ ≤ 128 log 2 (Q+1)² r₀^{−2} c_M² (ϑd)^{−2} ‖f‖_∞‖h‖_∞,

where D(u,v) := S^T[ρ](u,v) − S^T[ν](u,v).

Step 4 (sign average). D is bilinear. Averaging over independent uniform signs, E_σ D(F₁^σ, F₂^σ) = Σ_{k,k'}E[σ_kσ_{k'}] D(f(·−v_k), h(·−v_{k'})) = Σ_k D(f(·−v_k), h(·−v_k)). Both states are invariant under all lattice translations (LG1(5): unit translations, hence all of a_K Z⁴), so each summand equals D(f, h). Therefore N|D(f,h)| ≤ sup_σ |D(F₁^σ,F₂^σ)|, and |D(f,h)| ≤ c₈^{−1}d⁴ · 128 log 2 (Q+1)² r₀^{−2}c_M²ϑ^{−2}d^{−2}‖f‖‖h‖ = D_ϑ d²‖f‖‖h‖. ∎

The sign average is a finite algebraic identity, not an enumeration.

### 7.2 An infinite-volume reference

**Lemma 7.2.** For each first-passage datum there is a periodic Gibbs state ν_* ∈ 𝒢_{a_K,β} (a periodic limit of the torus measures μ_{K,ℓ_m,β}, ℓ_m → ∞ compatible) which satisfies (6.0) with the same ζ, g(d) and |R| ≤ ε_RL(d), for every pair and position. [proved from Proposition RL and LG1(2)]

*Proof.* By LG1(2), a subsequence of the torus measures converges, in the sense of expectations of bounded continuous local functions, to a DLR state ν_*; it is invariant under all lattice translations, being a limit of translation-invariant measures. For a fixed pair at a fixed position, O(f), O(h) and O(f)O(h) are finite sums of bounded continuous functions of finitely many links, the same on every torus large enough to contain the supports without wrapping, so S^T[μ_{K,ℓ_m}](f,h) → S^T[ν_*](f,h). By Proposition RL, each S^T[μ_{K,ℓ_m}](f,h) lies in the closed interval ζ²C_G g(d)⁴K_free[1 − ε_RL(d), 1 + ε_RL(d)], whose ends do not depend on ℓ_m (ζ and g(d) are run quantities, independent of the torus by IN1(3)). Closed intervals pass to limits. ∎

### 7.3 F2 for every periodic state

**Theorem 7.3** (TP1(1)). For every periodic Gibbs state ρ ∈ 𝒢_{a_K,β}, S^T_2[ρ](f,h) = ζ²C_G g(d)⁴K_free(f,h)(1 + r) with |r| ≤ ε̄(d) := ε_RL(d) + C₉ d²(log(1/d))² ≤ ½ for d ≤ d₀. [proved]

*Proof.* By Proposition 7.1 with ν = ν_* of Lemma 7.2, S^T[ρ] = S^T[ν_*] + θD_ϑ d²‖f‖‖h‖ with |θ| ≤ 1. Divide by the main term: by Lemma 3.6, K_free ≥ 10^{−8}ϑ_*²‖f‖‖h‖; ζ² ≥ 4/9; g(d)⁴ = x^{−2} ≥ (2c_* log(1/d))^{−2} for d ≤ d₀ (Proposition 4.2). So the relative change is ≤ D_{ϑ_*}d²·(9/4)·10⁸ϑ_*^{−2}C_G^{−1}·4c_*²(log 1/d)² =: C₉d²(log 1/d)². Hence 1 + r = (1 + R)(1 + θ'C₉d²(log 1/d)²/(1 + R)) and |r| ≤ ε_RL + 2C₉d²(log 1/d)², renamed. Shrink d₀ so that ε̄(d₀) ≤ ½. ∎

*Remark.* The all-state constants are those of RL plus D_ϑ; nothing depends on the state, the torus period of ρ, or the position. This answers the uniformity requirement SA states for F2 (L4302–4309: "At fixed d its eventual cutoff threshold and constants must be uniform in those states and support positions").

---

## 8. TU10, the law on R⁴ and components

**Corollary 8.1** (TU10, TP1(3)). For every periodic Gibbs state ρ, 0 ≤ S^T_2[ρ](f,h) ≤ u(d)‖f‖_∞‖h‖_∞ with u(d) := (3/2)(16/9)C_G v₄²(c_*/2)^{−2}[log(1/d)]^{−2}. These closed inequalities pass to every volume-first limit and to every component (Theorem 8.2). [proved]

*Proof.* By Theorem 7.3, 0 ≤ ½ζ²C_G x^{−2}K_free ≤ S^T ≤ (3/2)ζ²C_Gx^{−2}K_free. Use ζ² ≤ 16/9, K_free ≤ v₄²‖f‖‖h‖ (Lemma 3.6), and x ≥ (c_*/2) log(1/d) for d ≤ d₀ (Proposition 4.2). ∎

This is TU10 exactly as RO1 reads it (assembly TP1(4), L396; SA L4380–4412 deduce TU10 from F2–F3 by the same two lines, and say "This deduction does not verify the state-uniform extraction or running normalization required in F2–F3"; here those are Theorems 7.3 and §4).

**Theorem 8.2** (TP1(4)). Let S be a volume-first limit along first-passage data (K_j, β_j), K_j → ∞, with centering states ν_j (CL1(1)), and let σ_ξ be any component of its canonical decomposition (PH1(3)). Put g_c(d)^{−2} := c_* log(1/d) and η̄(d) := sup |ζ^{1/2}g(d)/g_c(d) − 1|, the supremum over all first-passage data at g with K − s(d) ≥ n₀. Then η̄(d) → 0, and for C¹ pairs (f, h) ∈ 𝔗(d; ϑ_*) with d ≤ d₀,

S_2^T(f,h) = C_G g_c(d)⁴ K_free(f,h)(1 + η),  (1 − ½)(1 − η̄)⁴ ≤ 1 + η ≤ (1 + ½)(1 + η̄)⁴,

and the same for σ_ξ. [proved from CL1(1) and the all-state realisation of PH1]

*Proof.* η̄ → 0: by Proposition 4.2, g(d)^{−2}/g_c(d)^{−2} → 1 and by Proposition 4.3, ζ → 1, both uniformly over the data; so ζ^{1/2}g(d)/g_c(d) → 1 uniformly. For each j, with K_j − s(d) ≥ n₀ for j large, Theorem 7.3 gives S^T[ν_j](f,h) = C_G g_c(d)⁴K_free·(ζ_j^{1/2}g_j(d)/g_c(d))⁴(1 + r_j), with (ζ_j^{1/2}g_j/g_c)⁴ ∈ [(1 − η̄)⁴, (1 + η̄)⁴] and |r_j| ≤ ½. CL1(1) gives S_2^T(f,h) = lim_j ν_j[(O(f) − ν_j O(f))(O(h) − ν_j O(h))] = lim_j S^T[ν_j](f,h) (the connected function is the centred second moment). The interval is closed and independent of j, so the limit lies in it. For a component σ_ξ: by the all-state realisation (§2.1, PH1), σ_ξ's separated moments are limits along the defining subsequence of centred moments of periodic Gibbs states ρ_j^ξ ∈ 𝒢_{a_{K_j},β_j}, and S^T is unchanged by centering at any constants; Theorem 7.3 applies to every ρ_j^ξ with the same interval. ∎

*Caveat on the component import.* I use the all-state realisation as the assembly states it for RO1 ("a canonical component of PH1 with its all-state realisation", L407) and as SA states it for TU10 ("pass to every limit and to the all-state phase realizations", L4409–4411). The connected two-point function of a mixture is not the mixture of the components' connected functions (S_2^T[S] = ∫S_2^T[σ_ξ]dλ + ∫𝔠_ξ²dλ ∫f∫h), so the law for S alone would not give it for σ_ξ; the realisation is needed and is not re-proved here.

---

## 9. NT1 in every component

**Lemma 9.1** (Y3 L88901–88917, Lemma IV-69-33, ported to x₄). Let σ be a normalised real functional on separated tuples, invariant under θ(x₁,x₂,x₃,x₄) = (x₁,x₂,x₃,−x₄) and reflection positive at x₄ = 0, with OS space ℋ(σ) and Ω = [1]. If f ∈ C_c¹({x₄ > 0}) and S_2^σ(θf, f) > 0, then ℋ(σ) contains a unit vector orthogonal to Ω. [proved]

*Proof.* The OS form is ⟨A, B⟩ = σ(θĀ·B). Let c := σ(O(f)); c is real since σ is real and f is real, and σ(O(θf)) = c by θ-invariance. Put v := [O(f)] − cΩ. Then ⟨Ω, v⟩ = σ(O(f)) − c = 0, and ‖v‖² = σ(O(θf)O(f)) − cσ(O(θf)) − cσ(O(f)) + c² = σ(O(θf)O(f)) − c² = S_2^σ(θf, f) > 0. Normalise. ∎

**Theorem 9.2** (TP1(5), NT1). For every component σ_ξ of every volume-first limit at g ≤ γ_W, H_{σ_ξ} ≠ 0 on Ω^⊥. [proved from Theorem 8.2, CL1(2)–(3), PH1(3), PH1(5)]

*Proof.* Let φ(u) := (1 − |u|²)² for |u| ≤ 1 and 0 otherwise; φ is C¹ (∇φ = −4u(1 − |u|²) vanishes on |u| = 1), 0 ≤ φ ≤ 1 = φ(0), ∫φ = 2π²∫₀¹r³(1−r²)²dr = π²∫₀¹t(1−t)²dt = π²/12, and Lip φ = max_{0≤ρ≤1}4ρ(1 − ρ²) = 8/(3√3) < 2. Fix d ≤ d₀ and put f(x) := φ((x − c)/d), c := (0, 0, 0, 3d/2). Then supp f = B(c, d) ⊂ {x₄ ≥ d/2}, supp θf = B(θc, d), dist(supp θf, supp f) = 3d − 2d = d ∈ [d, 6d], ∫f = (π²/12)d⁴ ≥ ϑ_*‖f‖_∞d⁴, Lip f < 2/d ≤ ‖f‖_∞/(ϑ_*d). So (θf, f) ∈ 𝔗(d; ϑ_*) is a C¹ pair. Theorem 8.2 gives S_2^{σ_ξ}(θf, f) ≥ ½(1 − η̄)⁴C_G g_c(d)⁴K_free(θf, f) > 0 (η̄ < 1 for d ≤ d₀; K_free > 0 by Lemma 3.6). σ_ξ is real, θ-invariant and reflection positive at x₄ = 0 (PH1(3): each σ_ξ has the invariances and positivity of S; CL1(2)). Lemma 9.1 gives a unit v ⊥ Ω. By PH1(5), ker H_{σ_ξ} = CΩ, so Hv ≠ 0. ∎

*Comparison with WT1(1).* Lemma W (`t0-skeleton.md` §3.10) needs the law at two times with a ratio margin (> 7·10⁴ against 48). Theorem 9.2 needs one positive reflected value and the unique vacuum, which PH1 already supplies. Lemma W is no longer on T0's path for NT1; it remains a valid alternative (it does not use PH1(5)).

---

## 10. AG1: ages and the rarity of old live regions

### 10.1 The statement TP1 reads

Let P = P^{(k)} be the positive (unsourced, z = 0) law of the retained variables at level k (LF1(1): for real inputs every weight is nonnegative and the moves preserve total mass; `ref-73.md` §2 builds it as the image of the Wilson measure under a mass-one kernel). For a cell c of level k and a ≥ 0 let 𝔏_k^{≥a}(c) be the event that some live component at level k meeting c has lineage age ≥ a (created at level ≤ k − a and never healed since, in SA's sense: "The age recorded in the label restarts wherever 𝐑 leaves a component standing as an island", L26103–26117).

**Lemma AG-k₁** [outstanding]. There are C, c > 0 such that for g ≤ γ_W, every first-passage datum, every compatible torus, every level k with x_k ≥ g^{−2} and every cell c of level k,

Σ_{a≥0} L^{8a} P(𝔏_k^{≥a}(c)) ≤ C (log x_k)^{C} e^{−c p₀(g_k)}.   (10.1)

TP1 uses it only at k = k₁, in (6.3).

*Relation to AG1 and to SA.* (10.1) is AG1 (assembly L351) with the moment L^{8m} that TP1 uses and with r(m) := sup_c P(𝔏_k^{≥m}(c)); it is SA's display Σ_a L^{8a}max_𝔠 ν̃(𝔩𝔳_{k}^{≥a}(𝔠)) ≤ … e^{−cp₀(g(d))} in (a) of Proposition 7.3 (L26103–26117), there at k₀, here at k₁. It is CA-III's Proposition 8.12, "uniform rarity of never-healed old large-field regions", which CA-III lists under "Proof outstanding: statements for which no complete argument is known" (CA-III L111189–111192).

*What our route does not need from AG1.* AG1 as the assembly states it also asks that "witness selection, reflection replication and pattern counting preserve the insertion and source weights" (SA D3, L4167–4170). Our route evaluates the live law at z = 0 (in (6.1) all source dependence sits in the derivatives Φ_i, Φ_{12}, bounded pointwise by (TP-live)). So (10.1) is a statement about the *unsourced* positive law only; no source-weight preservation is read.

### 10.2 A reduction: the stagewise product [proved]

Two per-level statements.

**(H) Healing dichotomy.** There is C_H such that: if a live component Y at level i − 1 has a descendant live component at level i, then the level-i small-field test fails on some cell of level i within C_H cells of the image of Y. (Survival from one level to the next requires a fresh large-field event at the next level near the lineage; otherwise the component is healed.)

**(SR) Stagewise rarity.** For every a ≥ 0 and every chain of cells c_{k−a}, …, c_k (c_i of level i, c_{i} within C_H cells of the parent of c_{i−1}), P(the small-field test fails at level i on c_i for every i = k − a, …, k) ≤ (C_R)^{a+1} Π_{i=k−a}^{k} e^{−c p₀(g_i)}.

**Lemma 10.1** (product). (H) and (SR) imply (10.1).

*Proof.* If 𝔏_k^{≥a}(c) occurs, there is a lineage alive from some level k − a' (a' ≥ a) to level k with its level-k component meeting c. By (H), at each level i ∈ [k − a', k] the small-field test fails on a cell c_i within C_H cells of the lineage's image; at the creation level k − a' it fails by definition. The cells form a chain as in (SR), ending within C_H + diam cells of c. The number of chains of length a' + 1 ending near c is ≤ (C_c L⁴)^{a'} (at each step down one level, (2C_H + 1)⁴ choices of the neighbouring parent times L⁴ choices of the sub-cell), times a constant for the end. By (SR) and the union bound,

P(𝔏_k^{≥a}(c)) ≤ Σ_{a'≥a} C (C_cL⁴C_R)^{a'} C_R Π_{i=k−a'}^{k}e^{−cp₀(g_i)} ≤ C C_R e^{−cp₀(g_k)} Σ_{a'≥a} (C_cC_R L⁴ e^{−cp₀(g_k)})^{a'},

using p₀(g_i) ≥ ½p₀(g_k) for i ≤ k (by (4.1), x_i ≥ x_k − 2c₂, and (log(x_k − 2c₂))^{𝔭₀} ≥ ½(log x_k)^{𝔭₀} for x_k large) and renaming c/2 as c. Put θ := C_cC_RL⁴e^{−cp₀(g_k)}. Then Σ_a L^{8a}P(𝔏^{≥a}) ≤ C C_R e^{−cp₀(g_k)} Σ_a L^{8a}θ^a/(1 − θ) ≤ 4 C C_R e^{−cp₀(g_k)} once L⁸θ ≤ ½, which holds for g ≤ γ_W because p₀(g_k) = (log x_k)^{𝔭₀} ≥ (log g^{−2})^{𝔭₀} → ∞. ∎

So the geometric decay that AG1 needs comes from paying the large-field cost *at every level of survival*, and Lemma 3.8/3.9 explain why paying only at creation is not enough in 4D. The rate L^{8a} is beaten because each surviving level costs e^{−cp₀}, which is eventually smaller than any fixed power of L.

### 10.3 Attacks on (10.1)

**Attack A — the three-dimensional union bound (Y3's route).** *Idea.* Bound P(𝔏_k^{≥0}(c)) by the probability that a large-field region is created at some level ≤ k anywhere in the region that can influence c, summing creation rarity over levels and positions (Y3 L791–797; Y3 Corollary IV-68-44, L87712–87750, "the volume-dependent tail"). *Result.* Fails in 4D. *Exact reason.* Lemma 3.9(a): the number of creation positions at level k − m inside a level-k cell is L^{4m}, while the creation cost is e^{−c(log x_{k−m})^{𝔭₀}} with x_{k−m} = x_k + O(m) (linear running, (4.1)); Σ_m L^{4m}e^{−c(log(x_k + c₀m))^{𝔭₀}} diverges. With an additional age weight L^{8a} it diverges faster. In 3D, x_{k−m} ≥ x_kL^m and the same sum converges (Lemma 3.9(b)). The failure is structural (marginal coupling), not a lost constant.

**Attack B — the stagewise product (Lemma 10.1), then (SR) by chessboard.** *Idea.* Prove (H) from the healing rule and (SR) for the Wilson measure, then apply Lemma 10.1. For (SR): each "test fails at level i on c_i" is an event of the level-i block field near c_i; with Balaban's averaging that block field is a local gauge-covariant function of the bare links in the block of c_i and a fixed collar (plus the independent auxiliary gauge draws of the history moves, which are product over cells). So the chain event E is a local event of the bare field on the level-k cell of c_k with its collar. The chessboard estimate (LG1(3), SA (ST1)–(ST4) as summarised in the assembly) gives P(E) ≤ P(E^{diss})^{1/𝒩}, where E^{diss} imposes the reflected copies of E in every level-k cell of the torus and 𝒩 is the number of cells. Then P(E^{diss}) = Z_{E^{diss}}/Z is a ratio of a *periodic constrained* partition function to the unconstrained one, and (SR) follows if

(CF) log Z_{E^{diss}} − log Z ≤ 𝒩·[(a + 1) log C_R − c Σ_{i=k−a}^{k} p₀(g_i)].

*Result.* (H) is not proved here: it is a property of SA's healing operation 𝐑, and CA-III lists "the exit bound" and the arrest theorem among statements without complete proof (CA-III L111189–111194 list, items (1)–(3); L111393 "the arrest theorem", as cited in the assembly LF1(c)). (CF) is not proved either. *Exact reason for (CF).* (CF) is a lower bound on the free-energy cost per level-k cell of a periodic pattern of nested large-field events at a + 1 consecutive levels. The action part is plausible and additive over disjoint scale shells (a field large at level i on c_i and at level i + 1 on its parent must have curvature of natural size ≥ p(g_i)g_i at both scales; a smooth profile that is large at level i + 1 has natural size only L^{−2} times that at level i, so each level needs its own excess). But the measure statement needs the excess *net of fluctuation entropy* at every level, uniformly in the coarser data: the constrained partition function at level i must be compared with the unconstrained one with the same coarse data. That is exactly the separation (SEP) at which `library/rarity-fresh-x.md` stopped ("The first failed proof step is the extension from admitted class coercivity to (SEP) for the full marked sector at the same top/data", its §3, checked in `gates/rarity-fresh-x-0e8a5a4e7.md`: "First step that fails: (SEP)"). Chessboard removes the dependence on the exterior and on the position, but leaves the constrained-versus-free comparison at each level intact.

**Attack C — remove old regions by redesign: close off large-field regions at creation.** *Idea.* Change the representation (a design freedom of the hard core, not of TP1 alone): when a large-field region is created at level i, integrate its interior variables at once with the crude Wilson bound, conditionally on its exterior collar, so that it becomes an ordinary polymer activity of level i, holomorphic in the collar data on the small-field domain, of mass ≤ e^{−cp₀(g_i) − κ|X|_i}. Then there are no old live regions; ages are 0; (10.1) reduces to a single-level statement; and the effect of all fine-level closed-off polymers on a coarse cell is renormalisable: their vacuum parts are constants and their marginal parts shift the coupling by Σ_m e^{−cp₀(g_{k−m})}, which converges by Lemma 3.8 (p > 1). *Result.* Fails as a proof here. *Exact reason.* The closed-off activity is "the internal integral with the supremum over external complex data inside, including the Wilson factor, stored Jacobians, gauge factors and insertion weights" — exactly the C3 mass bound ⟦LF-mass⟧ of LF1(3) (assembly L296), which is open. In addition, integrating the interior at creation removes the level-i block averages over the region, so the level-(i+1) block field is undefined on the region unless the averages are kept and integrated later; keeping them reintroduces a region whose block field may stay large at level i + 1 — an old region again, unless (H) holds. So Attack C does not avoid (H); it trades the age series for ⟦LF-mass⟧ plus (H), and it changes the representation that NL1, LF1 and SC1 are built on.

**Where the three attacks meet.** Each attack stops at a per-level statement: A at the absence of any per-level cost after creation; B at (H) and the constrained comparison (CF)/(SEP); C at ⟦LF-mass⟧ and (H). The common core is:

> **(H) + per-level conditional rarity.** A lineage survives a level only by a fresh large-field event near it, and that event costs e^{−cp₀(g_i)} relative to the same coarse data.

With both, Lemma 10.1 proves (10.1) and TP1 closes from its TP-inputs.

### 10.4 Is there a counterexample?

I looked for a mechanism that would make (10.1) false for the Wilson measure, and found none. Two candidates fail:
- *Scale-invariant profiles* (curvature ∝ |x − x₀|^{−2}, natural size constant across scales) are large at every level around x₀, but their action is additive over scale shells (∫_{shell}|F|² ≈ const per shell), so a lineage of age a costs ≈ a·p₀ — consistent with (SR).
- *Thin or thick centre vortices* make nested plaquettes have holonomy −1 at all levels between the vortex thickness and its size R; their cost is an area law ∝ R², far above a·p₀.
These are heuristics, not proofs; they explain why (SR) is expected, not that it holds.

---

## 11. Status of every statement

| Statement | Where | Status |
|---|---|---|
| Lemma 3.1 (sources = local inverse coupling; S^T as mixed derivative) | §3.1 | [proved] |
| Lemma 3.2 (dilation) | §3.2 | [proved] (not used) |
| Lemma 3.3 (Isserlis; C_G) | §3.3 | [proved]; normalisation a_p ≈ ½|F|² from SA L6852 |
| Lemmas 3.4, 3.5 (Cauchy; Schwarz along rays) | §3.4 | [proved] |
| Lemmas 3.6, 3.7 (shape class; kernel sums) | §3.5 | [proved] |
| Lemmas 3.8, 3.9 (4D arithmetic; union bound diverges in 4D, converges in 3D) | §3.6 | [proved] |
| Lemma 4.1 (flow bounds without OL-incr) | §4.1 | [proved] from OL1(2),(3),(5), IN1 |
| Proposition 4.2 (g(d)^{−2} ~ c_* log 1/d) | §4.2 | [proved] from the same |
| Proposition 4.3 (ζ → 1) | §4.3 | [proved] from TP-slope |
| Lemma 6.1 (exact identity at k₁) | §6.1 | [proved] from TP-pres |
| Lemma 6.2 (kernel bounds) | §6.3 | [proved] from (2.1) |
| Lemma 6.3 (template = free law) | §6.4 | [proved] from (2.1), FC1, TP-slope, SA's running-shift formula |
| Lemma 6.4 (regular remainder) | §6.5 | [proved] from TP-cx, TP-far |
| Lemmas 6.5, 6.6 (mean; covariance) | §6.6 | [proved] from TP-live, TP-cx, AG-k₁ |
| Proposition RL | §6.7 | [proved] from the above |
| Proposition 7.1 (two states differ by O(d²)) | §7.1 | [proved] from SR1's normaliser, LG1(5) |
| Lemma 7.2, Theorem 7.3 (F2 for all states) | §7.2–7.3 | [proved] |
| Corollary 8.1 (TU10) | §8 | [proved] |
| Theorem 8.2 (law on R⁴, components) | §8 | [proved] from CL1(1), PH1 all-state realisation |
| Lemma 9.1, Theorem 9.2 (NT1 per component) | §9 | [proved] from PH1(5) |
| Lemma 10.1 (stagewise product) | §10.2 | [proved] |
| Lemma AG-k₁ (10.1) | §10.1 | **[outstanding]**: three attacks, §10.3 |
| (H), (SR)/(CF) | §10.2–10.3 | [outstanding]; the per-level core |
| TP-pres, TP-cx, TP-live, TP-far, TP-slope | §2.2 | TP-inputs for SC1, NL1, LF1; not attacked here |

**What TP1 now is.** TP1(1)–(5) hold as an implication from: the assembly's imports (LG1, IN1(3)–(4), OL1(2),(3),(5), FC1, SR1's normaliser, CL1, PH1), five TP-inputs which belong to the hard core (SC1, NL1, LF1), and one TP1-owned rarity statement (10.1), itself reduced to (H) and (SR).

**What changed relative to the assembly's TP1 entry.**
- ⟦TP-F3⟧ is closed as an implication (§4), with OL1(4) ⟦OL-incr⟧ no longer an input to F3.
- ⟦TP-7.6⟧: the transfer half is closed (§7, infinite reference, no ET8–ET10); the identification half is (TP-pres), SC1's exact sourced presentation.
- ⟦TP-F2⟧: closed as an implication from the TP-inputs and (10.1) (§6–7); the complete-force term (GCB52) is not read.
- NT1 moves from Lemma W to Theorem 9.2.
- AG1 is needed in the form (10.1), unsourced, at one level, with the moment L^{8a}.

## 12. Departures from SA's Section 7, and why

1. **One level (k₁), not two.** SA uses both k₀ and k₁ and matches them (L26097–26101). We need only k₁, because the template there is a Gaussian covariance that we evaluate exactly (Lemma 6.3); we never need the law of the level-k₀ block field.
2. **Cauchy in the complex plaquette coefficient instead of a one-step recursion with force terms.** SA's (c3) needs "two inequalities on a single fluctuation integral" per step (L26162–26176), and its conditional law meets the complete-force term (GCB52), for which "No such convexity, symmetry or force bound is asserted" (L28219–28221). We need sup bounds of the non-Gaussian remainder on coupling-sized discs (TP-cx) instead; Cauchy's formula supplies the derivatives. This is Y3's complex plaquette coefficient (L745–747) carried to 4D.
3. **Infinite-volume reference.** SA uses one small torus and the companion criteria (ET8)–(ET10) (L26872–26931). We prove RL uniformly in the torus and pass to a periodic Gibbs state, which SA's own F2 text allows (L4345–4348).
4. **NT1 from one positive reflected value** (Y3 IV-69-33) and PH1's unique vacuum, instead of a two-time ratio.
5. **F3 without the increment law.** The sum Σ b_j⁰ telescopes to A_K − A_{K−s} (OL1(2)); OL1(3) then gives c₀s + O(1).
6. **AG1 unsourced and at one level**, with the reduction of §10.2 naming the per-level core.

Credit again: the architecture (two-level identity, running shift, ζ, witness depth, age series, transfer by a common normaliser) is Sussman and Alpoge's (with Claude and Codex as authors of their text); the complex plaquette coefficient and the nontriviality lemma are from their YM3_I; the free decomposition and the background-field method are Balaban's; Dimock's expositions are the readable source for the latter.
