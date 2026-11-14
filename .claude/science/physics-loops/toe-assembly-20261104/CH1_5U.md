# CH1-5U-i. The twisted family and its mirror

## 0. Status

**FINISH: FROZEN 2026-11-05 after pass 3 (CH1_5U_REFEREE.md); the referee's edits are applied.** Frozen means: the proved results below are not reopened; open statements are worked in their own files and enter by a dated amendment.

**Proved in this item, subject to the stated standard representation theory:** the covering description of the family; vanishing linear and cubic traces; the SU(2) index and Z4 character calculations; the absence of a new-SU(2) structure map over SO(d) for d ≥ 3; the mirror quartic phase calculation; and the one-site commutant. The named anomaly interpretations additionally use the cited anomaly formulas. Pass 3 reviewed these results; its imported referee closures are not themselves refereed.

**GAP:** the draft's claim that all global U(5) anomalies vanish uses an unverified bordism computation and an anomaly-theory input. The draft sketch does not establish the required localization equivalences; R3 supplies a reduction conditional on cited standard results. Its alternative Spin(10) route needs a verified precise anomaly theorem. Absence of the named anomaly tests is not a proof of absence of every anomaly. Spacetime-symmetry anomalies are not analyzed. The draft's implication CH1-5U-i ⇒ CH1-5U-q holds once CH1-5U-q is stated with IR's clause and the same charged-correlator prescription (`CH1_5U_REFEREE.md` R4). The purported failures of the existence attacks have the narrower scope stated below.

**Open by name:** CH1-5U-i; CH1-5U-q[𝒫]; A5-glob; CH1-i; CH1-ii; AM-5; CH1-5O-i; reflection positivity; CG1K-H; LW1-5-X; VC1-5U-odd; GA2's bridge Y2. No law or reading is adopted.

**Provenance.** Pass 2 run (set by the lead from the run log): Codex `gpt-6.1-terra`, reasoning effort high, codex-cli 0.165.0, session `01a1aed1-ebe2-7c72-9dc6-1679cbf694ce`. Pass 2 distillation of `CH1_5U_DRAFT.md`, SHA-256 `91430000d948742a9e833b1855ca02634fdcb7722dc9ae49df3c039a30bc07ae`. Context: `TOE_ASSEMBLY.md`, `LW1.md`, `CH1.md`, `LIT_SMG.md`; checkout HEAD `bf403a16a2bbb3bc0315a71f6cf1d791445cbb7f`. Pass 1 reports source revision `2d0adc0c0`; its other cited draft lemmas are inputs, not independently verified here. Pass 2 session report: requested model `gpt-6.1-terra`; the actual model and reasoning effort were not exposed in that session.

**Pass 3 editing provenance.** Codex `gpt-6.1-terra`, effort high, codex-cli 0.165.0, session `01a1aef7-f492-75a1-bf6d-85a47adc9511`.

## 1. Definitions inferred by the distiller

1. The center `U(1)_N` acts by `e^{iθ}1_5`; a field of charge `q` transforms by `e^{iqθ}`. A bar denotes the complex-conjugate representation. Write `10=Λ²C⁵`, `5bar=(C⁵)*`.
2. Let `u` be odd and `u≡2 mod 5`, `k=(u−2)/5` and `k'=−3k−1`. Thus `k` is odd, `k'` even and `|u|≥3`. Define
   \[R_u=(\Lambda^2\mathbb C^5\otimes\det^k)\oplus((\mathbb C^5)^*\otimes\det^{k'})\oplus\det^u=10_u\oplus\overline5_{-3u}\oplus1_{5u}.\]
   The flipped assignment `B_k` has the same U(5) representation; its Standard Model embedding differs. The left-handed description of the mirror is `R_u*`.
3. Put `Ũ(5)={(g,z)∈U(5)×U(1):z²=det g}`, `−1̃=(1_5,−1)`, and `S=(Λ⁰⊕Λ²⊕Λ⁴)C⁵` with action `(g,z)↦z⁻¹Γ(g)`. The standard identification of this pair with the U(5) preimage and a restricted half-spin 16 of Spin(10) is nomenclature, not an input to the representation proofs.
4. The proposed fermionic structure is `K_d=(Spin(d)×U(5))/⟨(−1,−1_5)⟩`. The draft cites Lemma Z-U for the identification of `−1_5` with fermion parity on local operators. That algebraic identification alone does not prove the continuum theory is defined on every K-manifold. Both K and ordinary `Spin×U(5)` backgrounds are considered conditionally.
5. The perturbative test is `Tr_R X³=Tr_R X=0` for all `X∈u(5)`. A named global-anomaly test is a pullback of the anomaly along the specified structure map. This use of “type” does not classify all possible anomalies. In all pullback statements, connections are pulled back or induced compatibly, and the spinor representations descend.
6. `L5-U`, `G_U`, the hypothesis IR, and PS-8 mean the items in pass 1's quoted sources. CH1-5U-i, as frozen in `CH1.md` line 225: “Find a covariant finite-depth \(L5\text{-U}\)-form gauge update and invariant stationary state whose IR is exactly one left-handed \(10_u\oplus\bar5_{-3u}\oplus1_{5u}\), with \(u=5k+2\), \(k\) odd, or its flipped assignment; keep \(U(5)\) as an operational massless long-distance group and gap the other odd excitations.” This is a proposed dynamical realization, not an established construction.

## 2. Representation and elementary charges

**Theorem 2.1 (Ũ and Φ).** `Ũ(5)` is connected. The map `σ̃(A,w)=(w²A,w⁵)` from `SU(5)×U(1)` is onto, with kernel `{(w⁻²1_5,w):w⁵=1}`. Its scalar circle `C={(w²1_5,w⁵)}` is isomorphic to U(1).

Every continuous homomorphism `ψ:U(5)→Ũ(5)` satisfying `ψ(A)=(A,1)` for `A∈SU(5)` is
\[\psi_{a,b}(g)=(g\det(g)^a,\det(g)^b),\quad 2b=1+5a.\]
Here `a` is odd, `b≡3 mod 5`; the map is onto, with kernel `μ_|b|` of scalar matrices, and
\[\psi_{a,b}^*S\cong10_{-b}\oplus\overline5_{3b}\oplus1_{-5b},\qquad \psi_{a,b}(-1_5)=(1_5,(-1)^b).\]
Thus for `b=−u`, `a=−(2u+1)/5`, `φ_u=ψ_{a,b}` has `φ_u* S≅R_u`, kernel `μ_|u|`, and sends `−1_5` to `−1̃`. The parity-preserving maps of this specified form give exactly the line of `R_u`. None is an isomorphism because `b≡3 mod 5` excludes `b=±1`; in particular no `ψ_{a,b}` gives `u=1`, since `b=−1 ≢ 3 mod 5`; `R_1` is not a `U(5)`-representation since `k=−1/5`. Scalars with `λ^u=1` act trivially on `R_u`.

*Proof.* Given `(g,z)`, choose `λ⁵=det g`, then `w²=λ` and change `w` to `−w` if necessary to obtain `w⁵=z`. Set `A=λ⁻¹g`. This proves surjectivity of σ̃, and its kernel and connectedness follow. The circle is injectively parametrized because `w²=w⁵=1` implies `w=1`.

For the converse, Schur's lemma gives `ψ(λ1_5)=(μ1_5,z)` with `z²=μ⁵`. By R0 below this lies in `C`, so `ψ(λ1)=(λ^{2b}1,λ^{5b})` for integer `b`. Restriction to `μ_5⊂SU(5)` gives `2b≡1 mod 5`. With `a=(2b−1)/5`, decomposition `g=λA` yields the displayed formula. Conversely it defines a homomorphism. Its kernel satisfies `λ^{2b}=λ^{5b}=1`; hence it is `μ_|b|`. Its surjectivity follows directly from R0 below.


**R0 (referee closure, CH1_5U_REFEREE.md) (Theorem 2.1: the scalar step and surjectivity, without Lie theory).** *Scalar step.* Let `ψ(λ1_5) = (μ1_5, z)` with `z^2 = μ^5`. Choose `w` with `w^2 = μ`. Then `(w^5)^2 = μ^5 = z^2`, so `w^5 = ±z`. Replacing `w` by `−w` keeps `w^2` and changes the sign of `w^5`. So `(μ1_5, z) = (w^21_5, w^5) ∈ C`. *Surjectivity.* Let `(g, z) ∈ Ũ(5)`. By the first part of Theorem 2.1, `(g, z) = (w^2A, w^5)` with `A ∈ SU(5)`, `w ∈ U(1)`. Since `b ≠ 0`, choose `λ ∈ U(1)` with `λ^b = w`. Then
\[
\psi_{a,b}(\lambda A)=\big(\lambda^{1+5a}A,\ \lambda^{5b}\big)=\big(\lambda^{2b}A,\ \lambda^{5b}\big)=(w^2A,\ w^5)=(g,z).
\]
∎ This uses only `det(λA) = λ^5` and `1 + 5a = 2b`.

On `Λ^r`, `r=0,2,4`, the pullback has weight `1_T+(ar−b)(1,1,1,1,1)`. The charges are `−5b,−b,3b`; `Λ⁴≅5bar⊗det` gives the indicated types. The parity formula follows by substitution. For odd `b`, `u=−b` is odd and `2 mod 5`, and the converse follows from the same equations. □

Complex conjugation produces the conjugate representation and conjugate embedding. It does not identify `R_u*` with the same unbarred `R_{−u}` convention.

**Theorem 2.2 (Q1 and Q1′, restricted).** Family and mirror charges lie in `{±u,±3u,±5u}` and have modulus at least 3. In a number-conserving quasi-free description, elementary one-particle and one-hole modes have charges `+1` and `−1`; none is a family member.

*Proof.* The first assertion follows from the displayed representation. The one-body space is spanned by creators of charge 1; holes have opposite charge. □

**GAP Q1′:** not every multiparticle excitation has charge ±1; three particles above a quasi-free sea carry charge 3. R2 closes the quasi-free half under its stated hypotheses. The interacting half remains part of CH1-5U-q[𝒫].

**R2 (referee closure, CH1_5U_REFEREE.md) (GAP Q1′: at a quasi-free point, a light field forces a light elementary field).** *Setting.* The matter CAR algebra of the modes `c_{x,j}`, `x ∈ Z^3`, `j = 1, …, 5`, at a c-number background, as in Theorem 2.2. A state `ω` is *number-conserving quasi-free* when, for `b_1, …, b_n ∈ {c_{x,j}, c^†_{x,j}}`, `ω(b_1⋯b_n) = 0` for odd `n` and, for even `n`, `ω(b_1⋯b_n) = Σ_π sgn(π)∏_{(i<j)∈π}ω(b_ib_j)` over the perfect matchings `π` of `{1, …, n}`, with `ω(cc) = ω(c^†c^†) = 0`. Put `G_{xi,yj} = ω(c^†_{x,i}c_{y,j})`.

*(i) Statement.* Let `A = b_1⋯b_{n_A}` have all factors at sites of a finite set `X`, and `B = b_{n_A+1}⋯b_n` all factors at sites of a finite set `Y`, with `X ∩ Y = ∅`. If `|G_{xi,yj}| ≤ Ce^{−μ|x−y|}` for all `x ≠ y`, then
\[
|\omega(AB)-\omega(A)\omega(B)|\le (n-1)!!\;C\,e^{-\mu\,d(X,Y)} .
\]
*Proof.* Expand `ω(AB)` by the matching rule. A matching with no chord between `{1, …, n_A}` and `{n_A + 1, …, n}` is a pair `(π_A, π_B)`, and `sgn π = sgn π_A · sgn π_B`, because no chord inside the first block crosses a chord inside the second. These terms sum to `ω(A)ω(B)`. Every other matching has a chord `(i, j)` with `b_i` at `x ∈ X` and `b_j` at `y ∈ Y`. Since `x ≠ y`, `ω(b_ib_j)` is `0`, `G_{xi,yj}` or `−G_{yj,xi}` (from `ω(c_{x,i}c^†_{y,j}) = −ω(c^†_{y,j}c_{x,i})`). So its modulus is at most `Ce^{−μd(X,Y)}`. Every two-point value has modulus at most 1, since `‖b‖ = 1`. There are `(n − 1)!!` matchings. ∎

*(ii) Statement.* Let `ψ` be fermion odd, of `U(1)_N` charge `q ≠ 0`, and quasi-local in the usual exponential sense (IR fixes no rate): `‖ψ − ψ_R‖ ≤ C'e^{−κR}`, with `ψ_R` in the algebra of the modes within distance `R` of the origin. Let `ψ_x` be its translate. If `G` obeys the bound of (i), then `ω(ψ_xψ_y^†)` decays faster than every power of `|x − y|`.

*Proof.* Replacing `ψ_R` by its charge-`q` part, `(2π)^{−1}∫e^{−iqθ}e^{iθN}ψ_Re^{−iθN}dθ`, keeps it in the same algebra and does not increase `‖ψ − ψ_R‖`. So take `ψ_R` of charge `q`. Then `ω(ψ_{R,x}) = 0`, because a number-conserving quasi-free state is `U(1)_N` invariant. Put `d = |x − y|` and `R = d^{1/4}`, and take `d` so large that `‖ψ_R‖ ≤ 2‖ψ‖`. The truncation changes `ω(ψ_xψ_y^†)` by at most `‖ψ − ψ_R‖(‖ψ‖ + ‖ψ_R‖) ≤ 3‖ψ‖C'e^{−κR}`. `ψ_R` lies in the algebra of `M ≤ 5(2R + 1)^3` modes. The ordered products of `{1, c_k, c^†_k, 2c^†_kc_k − 1}` form a basis of that algebra. It is orthogonal for `⟨X, Y⟩ = 2^{−M}tr(X^†Y)`, with squared norms at least `2^{−M}`: in Majorana form the four factors are `1`, `(γ ± iγ')/2` and `±iγγ'`, and Majorana monomials are orthonormal. So each coefficient of `ψ_R` has modulus at most `2^{M/2}‖ψ_R‖`, since `‖X‖_2 ≤ ‖X‖`. Expanding each `2c^†c − 1` writes `ψ_R` as at most `8^M` products of at most `2M` operators `b`, with coefficients of modulus at most `2^{3M/2}‖ψ_R‖`. By (i), applied to each pair of products, whose supports lie at distance at least `d − 2R`,
\[
|\omega(\psi_{R,x}\psi_{R,y}^\dagger)|\le 64^M\,2^{3M}\,(2\|\psi\|)^2\,(4M-1)!!\;C\,e^{-\mu(d-2R)}=\exp\!\big(O(d^{3/4}\log d)-\mu d\big).
\]
Both contributions decay faster than every power of `d`. ∎

*(iii) Consequences.* The equal-time two-point function of a free Weyl field decays as a power of the separation. So, at a number-conserving quasi-free point:
- if `G` decays exponentially, no quasi-local fermion-odd operator of any charge has free-Weyl large-separation correlations;
- hence, if some field of charge `|q| ≥ 3` has free-Weyl correlations there, `G` does not decay exponentially. Then the elementary field of charge `±1` is not gapped, and the light content is never exactly `R_u ⊕ R_u^*`. This is the step Attack 4 (§4) needs, now with composites included.

*A reading, used only here.* CH1-5U-i asks that "every other fermion-odd excitation" be gapped. At a quasi-free point, read this to include the elementary `c_{x,j}`: their connected correlations decay exponentially, as IR's clause "all other connected correlations decaying exponentially" (`CH1_5_DRAFT.md` line 49) says for operators outside the family fields. Under this reading, (iii) shows that no number-conserving quasi-free state at a c-number background has the light content CH1-5U-i asks for. Four-test check. (1) It fixes no part's target; it reads a clause of CH1-5U-i as worded. (2) It is closed: one clause, one class of operators. (3) It settles nothing by premise: the quasi-free conclusion is derived, and frozen Lemma V (`CH1.md` line 113) already excludes the free route by another argument. (4) It adds no structure or constant. Pass. Not adopted.

*What R2 does not reach.* An interacting law can have light composites of charge `|q| ≥ 3` without a light elementary field. That case is CH1-5U-q.

## 3. Anomaly calculations

**Theorem 3.1 (N, naturality).** For a structure homomorphism `f:K'→K` over `SO(d)` and a compatible representation `R`, induced associated bundles obey `P'×_{K'} f*R ≅ (P'×_f K)×_K R`. With compatible connections the associated Dirac operators and their indices and η-invariants agree. A vanishing anomaly therefore pulls back to a vanishing anomaly. In particular, `F_u:K_d→Spin(d)×_{Z₂}Ũ(5)`, `[s,g]↦[s,φ_u(g)]`, is well defined and pulls the anomaly of S back to that of `R_u`.

*Proof.* The map `[p', v] ↦ [[p', 1], v]` is well defined: `(p'k', v)` and `(p', f(k')v)` both map to `[[p', f(k')], v] = [[p', 1], f(k')v]`. It is a linear bijection on each fibre and intertwines the induced connections and Clifford actions, which come from the same frame bundle. Theorem 2.1 gives `φ_u(−1_5)=−1̃` and `φ_u*S=R_u`, which establish the special map and pullback. □

**Theorem 3.2 (A1, perturbative traces).** For every `X∈u(5)`, `Tr_{R_u}X=Tr_{R_u}X³=0`. The same holds for `R_u*`. Under the standard four-dimensional Weyl anomaly polynomial, all perturbative gauge and mixed gauge-gravitational anomalies vanish.

*Proof.* Diagonalize `dφ_u(X)`. On `S`, its 16 weights have the form `(1/2)∑ ε_i x_i` with an even number of plus signs. For any linear or cubic monomial, some variable has odd exponent and at least one of the five variables is absent. Flip both corresponding signs. This preserves the parity of plus signs and cancels the coefficient. The trace identities follow on S and hence on `R_u`. Conjugation reverses odd traces. Expanding in the central and traceless parts gives the `SU(5)^3`, `U(1)SU(5)^2`, `U(1)^2SU(5)`, `U(1)^3` and mixed gravitational terms. □

The draft's second derivation uses the cited `SU(5)^3` indices `A(10)=1`, `A(5bar)=−1`, the line `u(1,−3,5)`, and vanishing traces of traceless generators. It agrees with the proof above but is not an independent verification of those cited indices here.

**Theorem 3.3 (A2).** For every continuous `σ:SU(2)→U(5)`, with `n(W)=2Tr_W J_3²`,
\[n(\sigma^*R_u)=4n(\sigma^*5)\in4\mathbb Z.\]
Under the standard instanton-index and Witten-anomaly formulas, its Witten-type anomaly and that of the mirror vanish for these maps.

*Proof.* `det∘σ` is trivial because `su(2)` is perfect and SU(2) connected. If the eigenvalues of `J_3` on 5 are `y_i` with sum zero, then `∑_{i<j}(y_i+y_j)²=3∑y_i²`. The dual adds `∑y_i²` and the singlet adds zero. The SU(2) representation on 5 decomposes into spins of dimensions at most 5, whose indices are integers. The map `(s,h)↦[s,σ(h)]` gives the stated pullback. □

**Theorem 3.4 (A3).** If `g∈U(5)` and `g²=−1_5`, let `ν(g)` be the number of `+i` eigenvalues minus the number of `−i` eigenvalues on `R_u`. Then `ν∈{16,0,−16}`. At `g=i1_5`, it is `±16`; without the singlet it is `±15`. Under the cited mod-16 formula these tests vanish for the full family and mirror, and not for the 15 alone.

*Proof.* Conjugate `g` to `i diag(s_i)` with `r` negative signs. All three charges are `u mod 4`. Put `t=5−2r` and `ε=i^{u−1}=±1`. Then `ν=ε χ_{R_u}(diag(s_i))`, and, since `k,u` are odd and `k'` even,
\[\chi=(-1)^r\frac{t^2-3}{2}+t=(16,0,0,0,0,-16)_{r=0}^5.\]
Conjugation reverses ν. The center acts uniformly by `i^u`; removing the singlet removes one equal eigenvalue. □

**Theorem 3.5 (A4 and A5(i)).** For `d ≥ 3`, no continuous homomorphism `Spin(d)×_{Z₂}SU(2) → K_d` exists over `SO(d)` (R1, referee closure, CH1_5U_REFEREE.md). Also
\[K_d\cong(Spin^c(d)\times SU(5))/\mu_5,\]
where `ζ∈μ_5` acts by `(ζ⁻¹,ζ1_5)` on the central U(1) and SU(5).

*Proof.* For the first statement, see R1 below. In the special case of a map `σ:SU(2)→U(5)`, every σ has determinant 1, whereas `det(−1_5)=−1`. For the second statement, write `U(5)=(SU(5)×U(1))/μ_5` via `(A,λ)↦λA`. First divide `Spin×SU(5)×U(1)` by `(-1,1,-1)` and then by `(1,ζ1,ζ⁻¹)`. □

**GAP A4:** the first clause is closed by R1; the question of every realization of the new-SU(2) anomaly is part of A5-glob.

**R1 (referee closure, CH1_5U_REFEREE.md) (GAP A4: no structure map at all).** *Statement.* Let `d ≥ 3`. No continuous homomorphism `f: Spin(d) ×_{Z_2} SU(2) → K_d` satisfies `π_K∘f = π'`, where `π'[s, h] = π(s)` and `π_K[s, g] = π(s)` are the maps to `SO(d)`.

*Proof.* (1) `ker π_K = {[1, g] : g ∈ U(5)}`, because `[−1, g] = [1, −g]`. The map `j: g ↦ [1, g]` is an injective continuous homomorphism onto it: `[1, g] = [1, g']` forces `(1, g') = (1, g)`, since `(1, g') = (−1, −g)` is impossible. As `U(5)` is compact, `j` is a homeomorphism onto `ker π_K`. (2) `f[1, h]` lies in `ker π_K`, so `σ := j^{−1}∘f∘(h ↦ [1, h])` is a continuous homomorphism `SU(2) → U(5)`. (3) For `s ∈ Spin(d)`, `π_K(f[s, 1]) = π(s)`, so `f[s, 1] = [s', g]` with `s' = ±s`. As `[−s, g] = [s, −g]`, write `f[s, 1] = [s, τ(s)]`, with `τ(s)` unique, since `[s, g] = [s, g']` forces `g = g'`. `τ` is a homomorphism: `[ss', τ(ss')] = f[ss', 1] = [s, τ(s)][s', τ(s')] = [ss', τ(s)τ(s')]`. It is continuous, because `[1, τ(s)] = [s, 1]^{−1}f[s, 1]`. (4) In `Spin(d) ×_{Z_2} SU(2)`, `[−1, 1] = [1, −1]`. Applying `f`: `[−1, τ(−1)] = [1, σ(−1)]`, that is `[1, −τ(−1)] = [1, σ(−1)]`, so `σ(−1) = −τ(−1)`. (5) `det∘σ` and `det∘τ` are continuous characters of connected groups whose Lie algebras `su(2)` and `so(d)` are perfect for `d ≥ 3`. Their differentials vanish on `[𝔤, 𝔤] = 𝔤`, so both characters are trivial. Hence `1 = det σ(−1) = det(−τ(−1)) = (−1)^5 det τ(−1) = −1`, a contradiction. ∎

So no pullback test of the new-`SU(2)` type exists for `K_d`, with or without a spin component in the map. This is the proof of Theorem 3.5 with the Lorentz part allowed to twist.

**Conditional proposition 3.6 (A5(ii–iv)).** If `Ω₅^{Spin×_{Z₂}U(5)}=0` and, after local anomaly cancellation, the anomaly defines a homomorphism from this bordism group to U(1), then the full global anomaly of `R_u` and its mirror vanishes on K backgrounds and hence on ordinary spin U(5) backgrounds.

*Proof.* Theorem 3.2 gives the stipulated local cancellation. A homomorphism from the zero group is trivial; apply Theorem 3.1. □

**GAP A5:** neither hypothesis is established by the draft. The proposed AHSS sketch asserts, without proving the maps of Thom spectra, that quotienting by `μ_5` has the required 2-local effect and that odd-local K-bordism is oriented bordism of `BU(5)`. The displayed zero E² terms would suffice only after these identifications are justified. The alternative pullback from the Spin(10) 16 requires a precise checked theorem on its anomaly on `Spin×_{Z₂}Spin(10)`, not a list of reported anomaly types. The draft's unconditional lines 37 (“its anomaly, is decided: absent”) and 278 (“anomaly obstruction absent”) are therefore not proved. Its line 173 states the conclusion only “With the cited bordism fact”. A nonzero perturbative anomaly off the line follows within the one-family classification R-M, by frozen `CH1.md` Theorems U-M (line 143) and U-A (line 165).

**A5-glob (open, conditional).** Every anomaly of `R_u` and `R_u*` on `K_d`-manifolds, and hence on `Spin(d)×U(5)`-manifolds, vanishes, given the cited standard theorems S1-S9 and the η-invariant framework. R3 derives `Ω₅^K=0` from S1-S9, which are cited, not rebuilt; the anomaly framework remains an additional input.

**R3 (referee closure, CH1_5U_REFEREE.md) (GAP A5: `Ω_5^{K} = 0` from named standard theorems).** Write `K` for the stable form of `K_d`. The inputs S1-S9, cited and not rebuilt, are: S1 Pontryagin-Thom (Thom 1954); S2 the Thom isomorphism; S3 the Serre spectral sequence (Serre 1951); S4 the Hurewicz theorem modulo a Serre class (Serre 1953); S5 the Atiyah-Hirzebruch spectral sequence (Atiyah and Hirzebruch 1961); S6 `Ω^{Spin^c}_1 = Ω^{Spin^c}_5 = 0` (Stong 1968; Bahri and Gilkey 1987); S7 `Ω^{SO}_1 = Ω^{SO}_2 = Ω^{SO}_3 = 0`, `Ω^{SO}_5 = Z_2` (Thom 1954; Wall 1960); S8 `H^*(BU(5); Z) = Z[c_1, …, c_5]` and `H^*(BSU(5); Z) = Z[c_2, …, c_5]` (Borel 1953); S9 finite generation of `Ω_n` for a compact structure group; Wu's formula `w_3 = Sq^1w_2` on oriented manifolds. R3 completes pass 1's sketch (`CH1_5U_DRAFT.md` line 167).

*(a) At the prime 2.* The homomorphism `q: Spin^c(d) × SU(5) → K_d`, `([s, λ], A) ↦ [s, λA]`, is well defined (`([−s, −λ], A) ↦ [−s, −λA] = [s, λA]`), lies over `SO(d)`, is onto, and has kernel `{([1, ζ], ζ^{−1}1_5) : ζ^5 = 1} ≅ Z_5`. That is Theorem 3.5's isomorphism. `Bq` is a fibration with fibre `BZ_5`, over the simply connected `BK` (`K` is connected). The reduced homology of `BZ_5` with `Z_{(2)}` coefficients vanishes, so the Serre spectral sequence (S3) makes `Bq` a `Z_{(2)}`-homology isomorphism. Both Thom spectra are built from the same oriented bundle pulled back from `BSO`. The Thom isomorphism (S2) and S4 then give `Ω_5^K ⊗ Z_{(2)} ≅ Ω_5^{Spin^c × SU(5)} ⊗ Z_{(2)} = Ω_5^{Spin^c}(BSU(5)) ⊗ Z_{(2)}`, by S1. In the AHSS (S5), `E^2_{p,5−p} = H_p(BSU(5); Ω^{Spin^c}_{5−p})`. `SU(5)` is 2-connected, so `BSU(5)` is 3-connected and `H_p(BSU(5); A) = 0` for `p = 1, 2, 3` and every `A`. `H_5(BSU(5); Z) = 0` by S8 and universal coefficients (`H^5 = 0`, and `H^6 = Z c_3` is torsion free). The two remaining entries carry `Ω^{Spin^c}_1 = 0` (at `p = 4`) and `Ω^{Spin^c}_5 = 0` (at `p = 0`), by S6. So the whole line `p + q = 5` vanishes at `E^2`, and `Ω_5^K ⊗ Z_{(2)} = 0`.

*(b) At an odd prime p.* Put `P = U(5)/{±1_5}`. The maps `K_d → SO(d) × P`, `[s, g] ↦ (π(s), [g])`, and `SO(d) × U(5) → SO(d) × P` are onto, lie over `SO(d)`, and have kernel `Z_2`. Their fibres `BZ_2` have vanishing reduced `Z_{(p)}`-homology, and the base is simply connected. So, as in (a), `Ω_5^K ⊗ Z_{(p)} ≅ Ω_5^{SO}(BU(5)) ⊗ Z_{(p)}`. In its AHSS, `H_{odd}(BU(5); A) = 0` for every `A` by S8 (cohomology free and in even degrees), so the entries at `p' = 1, 3, 5` vanish. The entries at `p' = 4, 2` carry `Ω^{SO}_1 = 0` and `Ω^{SO}_3 = 0`, and the entry at `p' = 0` is `Ω^{SO}_5 ⊗ Z_{(p)} = Z_2 ⊗ Z_{(p)} = 0` (S7). So `Ω_5^K ⊗ Z_{(p)} = 0`.

*(c) Conclusion.* `Ω_5^K` is finitely generated (S9). A finitely generated abelian group that vanishes after tensoring with `Z_{(p)}` for every prime `p` is zero. So `Ω_5^K = 0`, given S1-S9.

*(d) Why the `Spin(10)` class does not reach `K`.* `LIT_SMG.md` line 92 records Wan and Wang: "Table 25 gives `Z2`, detected by `w2 w3`, for `Spin ×_{Z2} Spin(10)`." The homomorphism `K_d → Spin^c(d)`, `[s, g] ↦ [s, det g]`, is well defined, since `det(−1_5) = −1`. So every `K`-manifold is `Spin^c`: `w_2` is the reduction of an integral class, `W_3 = 0`, and `w_3 = Sq^1w_2 = 0` on an oriented manifold (Wu). Hence `w_2w_3 = 0` on every `K`-manifold. Any anomaly of the 16 on that `Z_2` pulls back along `F_u` (composed with `Ũ(5) ⊂ Spin(10)`) to zero. This agrees with (c). The vanishing of `w_2w_3` on `K`-manifolds does not depend on Wan and Wang.

*(e) What stays conditional.* Proposition 3.6 also needs its second hypothesis: once the degree-6 polynomial vanishes, the anomaly of a `K`-Weyl content is a homomorphism `Ω_5^K → U(1)`. Under the η-invariant definition of the anomaly, this follows from the Atiyah-Patodi-Singer theorem: on `Y = ∂Z`, `exp(2πiη(Y)) = exp(2πi∫_ZI_6) = 1`. That framework is cited. So A5-glob holds given S1-S9 and the framework, and neither is rebuilt here.

## 4. Mirror interactions and attempted routes

**Theorem 4.1 (K).** Let left-handed Weyl fields `A_{jk}=−A_{kj}`, `B^j`, `C` transform in `10bar_{−u}`, `5_{3u}`, `1_{−5u}`. Write `(χη)=ε^{αβ}χ_αη_β`. The unitary linear transformations commuting with U(5) are `U(1)^3`. The nonzero Lorentz- and U(5)-invariant quartics
\[O_2=\sum_{j,k}(A_{jk}B^k)(B^jC),\quad O_3=\sum\epsilon^{ijklm}(A_{jk}A_{lm})(\bar B_i\bar C)\]
are fixed exactly by the image of the gauged center: phases `(e^{iα},e^{-3iα},e^{5iα})`.

*Proof.* The three irreducible SU(5) types are distinct, so Schur's lemma gives the phase group. Both contractions are SU(5)-invariant and their U(1) charges are `−u+3u+3u−5u=0` and `−2u−3u+5u=0`. In `O_3`, for `i=1` the eight orderings of index pairs `(23),(45)` give the same nonzero contribution. In `O_2` the monomial `A_{12;1}B^2_{;2}B^1_{;1}C_{;2}` has nonzero coefficient; the reversed index term has different spinor components. Fixing the quartics imposes `α+2β+γ=0` and `2α−β−γ=0` modulo `2π`. These give `β=−3α`, `γ=5α`, including finite components. The gauged center supplies the full circle because `u≠0`. □

This excludes additional commuting **linear unitary flavor phases** common to these two interactions. It does not classify antiunitary, spacetime, nonlinear, higher-form, or microscopic symmetries, nor prove the interactions are realizable with the needed independent composite lattice fields. The draft's stronger “no surviving symmetry has an anomaly” is a GAP.

**R5 (referee closure, CH1_5U_REFEREE.md) (GAP on line 94: the restricted statement that is proved).** Let `Φ` be a unitary linear map of the mirror's left-handed fields `(A, B, C)` that commutes with `U(5)` and fixes `O_2` and `O_3`. By Theorem 4.1, `Φ` lies in the image of `U(1)_N ⊂ U(5)`. On that image, every perturbative anomaly vanishes (Theorem 3.2), the Witten and mod-16 tests vanish (Theorems 3.3, 3.4), and no new-`SU(2)` test exists (R1). So no symmetry of this class carries an anomaly of these types; with A5-glob, none of any type. Antiunitary, spacetime, nonlinear and higher-form symmetries stay outside, as the scope remark above says.

**Attack 1**, free; **Attack 2**, PS-8 on elementary content; and **Attack 3**, the one-site carriers `c`, `ccc`, `c^5`: pass 1 reports failures at Lemma V, K1-5/K2-5 with AM-5, and U-A(iii) with AM-5, respectively. Frozen `CH1.md` line 225 states: “A free construction fails V; an elementary chiral \(5\) fails K1 at its endpoints and, conditionally, AM-5; the one-site family fails the U-A ledger under AM-5.” Corollary U-T″ (`CH1.md` lines 197–201) carries an anomaly-free line family at one site exactly when `2 ≤ m ≤ 8`.

**Attack 4**, import a Spin(10) mirror-gapping flow: Theorem 2.1 pulls back any invariant interaction of S to an invariant interaction of `R_u`. The elementary quasi-free starting point does not have the required charge sectors (Theorem 2.2); R2 gives the quasi-free conclusion including composite fields under its stated hypotheses. This does not rule out another interacting starting point. The proposed gapping flow and a lattice realization of its continuum composite operators remain unproved. A proposed additional strongly coupled gauge group changes the stipulated law; it is not adopted.

**Attack 5**, overlap pullback: frozen W2 (`GA2_Y2.md` line 88, Theorem 3.4) gives `(U^{jk})²=0`; any state multiplicative on these operators gives `ω(U^{jk})²=0`, so its matrix of values is zero and not unitary. Thus this specific evaluation cannot supply the c-number unitary links used in the proposed overlap construction. This does not exclude operator-valued, coarse-grained, or approximate alternatives. A Euclidean overlap kernel also needs a separate derivation of the requested tick; the one-site composite CAR obstruction is frozen as Lemma C2-5 (`CH1.md` line 109). Replacing the finite registers with c-number links changes the law and is not adopted.

**Attack 6**, protected mirror flavor symmetry or elementary propagator: Theorem 4.1 defeats a universal obstruction based solely on a commuting linear unitary flavor phase that must survive *both* quartics, subject to their microscopic admissibility. The elementary charged field lies in a different global-charge sector from the family (Theorem 2.2), so an elementary one-particle pole theorem alone does not establish a constraint on the composite family. For a gauge-dressed correlator, endpoints, the Wilson line, Gauss constraints, and the definition of global charge must be specified before the draft's intermediate-state selection rule can be applied. Neither observation proves a general no-go theorem inapplicable.

## 5. Open subproblem and proposed readings

**R4 (referee closure, CH1_5U_REFEREE.md) (the implication CH1-5U-i ⇒ CH1-5U-q).** *Statement of CH1-5U-q.* Fix a charged-correlator prescription `𝒫` in the sense of `CH1.md` line 26. CH1-5U-q[`𝒫`]: there exist (a) an update `U` of `L5-U` form as in CH1-5U-i (a), covariant under `G_U`, and (b) a state `ω`, stationary under `U` and invariant under `G_U` and gauge transformations, such that hypothesis IR, with prescription `𝒫`, holds for at least one quasi-local fermion-odd operator `ψ` of definite `U(1)_N` charge `q`, `|q| ≥ 3`: its large-separation correlations in `ω` agree with those of a free Weyl field.

*Claim.* For every `𝒫`, CH1-5U-i[`𝒫`] implies CH1-5U-q[`𝒫`].

*Proof.* CH1-5U-i[`𝒫`] supplies `U` and `ω` with clauses (a) and (b), and IR fields spanning the `10_u`. Each component has fermion parity odd and `U(1)_N` charge `u`, with `|u| ≥ 3` (Theorem 2.2). Its correlations are free-Weyl under `𝒫`. ∎ So a proof of ¬CH1-5U-q[`𝒫`] refutes CH1-5U-i[`𝒫`].

*Four-test check.* (1) It fixes no part's target: it is a consequence of CH1-5U-i, posed as an open question. (2) It is closed: every clause is quoted from CH1-5U-i and IR, and `𝒫` is a parameter left open, not filled. (3) No downstream question is assumed. (4) It removes clauses and adds none. Pass. Not adopted.

The implication GAP in the earlier statement is closed by R4. CH1-5U-q[𝒫] remains open for interacting laws. The family also has charge magnitudes at least 9 and 15 in its other sectors. A theorem excluding all light charged excitations of modulus at least 3 would refute the target directly. The question is dynamical and is not settled by local carrier representations.

**Theorem 5.1 (Q3).** An operator on one site's `Λ(C⁵)` commutes with every `Γ(g)`, `g∈U(5)`, exactly when it is a function of the site number `N_x`.

*Proof.* The `Λ^k C⁵`, `0≤k≤5`, are irreducible and pairwise inequivalent: the center acts with distinct charges k. Schur's lemma makes the commutant the span of their projectors, which are polynomials in `N_x`. □

For a proposed on-site interaction `V(N_x)`, changing occupation from `n` to `n+q` changes that term's energy by `V(n+q)−V(n)`. The proposed 1+1-dimensional five-mode chain test was not run. The draft's assertion that it would merely print its input, or that four sites cannot distinguish a light composite from a finite-size level, is not established: hopping, gauge dynamics and finite-size scaling affect the spectrum. Such a test would be a guide, not a proof of 3+1-dimensional CH1-5U-q.

**Proposed four-test readings, with pass-1 results.** No item is adopted. (a) K as continuum structure: pass 1 says pass on tests 1–4 and calls it forced; the microscopic parity identity supports compatibility but does not itself establish all K backgrounds. (b) “global-anomaly type” as pullback: pass 1 says pass on all four; it is a definition, and completeness remains open. (c) an added strongly coupled gauge group: pass 1 records fail, fail unless specified, fail, fail; the claimed automatic settlement of CH1-i by adding it is not proved, though it changes the law. (d) c-number links replacing registers: pass 1 records fail, pass, fail, fail; the replacement changes PS-6r, while the claimed automatic settlement of bridge Y2 is not proved. (e) CH1-5U-q: pass 1 says pass on all four as an open question; R4 proves the implication from CH1-5U-i for each shared prescription 𝒫. The tests concern target fit, openness, whether a downstream question is settled by premise, and unneeded added structure, respectively.

## 6. Check record and limits

Pass 1 reports scratch checks, not proofs: (1) matching 16 weights for eight line values `|u|≤40`; (2) linear and cubic traces at 30 random integer points for each; (3) characters `16,0,0,0,0,−16` for `u=−33,−23,−13`; (4),(8) the quadratic index identity at random traceless points and the seven SU(2) partitions of 5, with index set `{20,10,5,4,2,1,0}`; and (6) phase solutions modulo `n=2,…,30`. The scratch code and output are not included in the supplied source and were not rerun here. The general proofs above do not rely on those checks.

The anomaly interpretations rely on standard results attributed in the draft to Atiyah–Singer, Witten, Tachikawa–Yonekura, García-Etxebarria–Montero, Hsieh, and the η-invariant anomaly framework. The exact outside hypotheses were not independently verified in this pass. A targeted literature lookup found [Davighi and Lohitsiri, Anomaly interplay in U(2) gauge theories](https://www.repository.cam.ac.uk/items/330c9a0f-f3c6-4e9d-9c33-efa03b0f8eb0), which concerns a different group and does not establish A5, and [Debray et al., What Bordism-Theoretic Anomaly Cancellation Can Do for U](https://doi.org/10.1007/s00220-024-04937-4), which illustrates the bordism/anomaly distinction but does not verify the claimed K computation. Pass 3 reviewed the chapter; the referee closures are not themselves refereed, and A5-glob remains conditional on the cited inputs.
