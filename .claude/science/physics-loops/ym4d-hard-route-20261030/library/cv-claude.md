lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T11:18Z

# CV: reality of the prescribed scalar interaction at independent real current

Queue row 349 (`cv-claude`). Pinned at commit 3c0e25954. Proof attack by Claude (Opus 5.5, max effort), not yet checked by the other model. Research text, not an audit; it grants no status.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the complete account (CA-I, CA-II at `31a47c543775`) and the outline. Tadeusz Balaban for the construction (CMP 99b, 102, 109, 116, 119, 122a/b). The earlier Codex rounds in `library/pd.md` (Lemmas 1-7, attacks 1-9) and the digest `library/prior/cv-claude.md` are reused, not repeated.

Kind of result (FINISH rule 9): proof of steps the account assumes, namely the reality clause of (H_j)(d) and of the family clauses. No correction of their text. No computer-assisted step. No numerics were run.

## 0. Summary

Claim first.

1. **The independent current is not where CV can fail.** Inside V_ω, the free current 𝐉 enters through three routes only: the explicit free-current operators, the old terms read at the tube point ζ itself (rough copies), and the chain layers. Each route preserves reality at real independent pairs, given reality of its inputs (Lemmas R4, R5; Theorem A; Proposition B). Every other member reads ζ only through the configuration 𝐔. For those members, reality at an independent real pair is the same statement as reality at the real configuration (Lemma R3).
2. **The reality clause of (H_j)(d) holds as an implication** (Theorem A). The account assumes it at CA-I 58252 ("They are real at real (𝐔,𝐉)") and in its family clause, CA-I 60651. Here it is proved by an induction that carries reality of every old term as a clause, from the formulas of CMP 119 (3.28)-(3.47) and the account's free-current operators.
3. **The input-family gap of pd.md Attack 8 is closed** for every walk family whose letters are real. Wordwise reflection (Lemma R4) follows from letterwise reflection. The free-current letters, including the branching insertions, are real at real pairs (Lemma R5). The example (29)-(30) of pd.md needs letters that are individually nonreal. No letter of the account is of that kind.
4. **What stays open** is one precise lemma, (CH) ∧ (PT) of §8. (CH): the chain layers are real at real independent pairs. (PT): the step-k terms that the account takes from CMP 122a/b as printed are real at real configurations. Neither has an independent-current difficulty that the lemmas here do not remove. Both need text (the layer theorem's construction, Balaban's printed formulas) that the account does not reproduce in full.

Result kind: **Open lemma**, a strict reduction of pd.md (34).

## 1. Sources read

The account was fetched at `31a47c543775` into a scratch folder. These ranges were read.

| Source | Content used |
|---|---|
| CA-I 156837-156998 | 4.32 and its Route. The third Route step says Balaban only assumes analyticity of E^{(j)}(X,…,U,J). |
| CA-I 20440-20530; 21325-21410 | The island exponent; the island bound reads the operation at (U,0) (CMP 122b (1.73)-(1.75)). |
| CA-I 58200-58275 | (H_j)(d): "They are real at real (𝐔,𝐉)", an assumption. |
| CA-I 60630-60705 | The family clauses ("reality at real points") and 4.38:cor-volume-families, whose hypothesis (c) assumes their propagation. |
| CA-I 93510-93660; 93990-94200 | The source tube, the boundary family 𝔳^𝐂 (printed without proof), the extension conventions (a)-(e). |
| CA-I 94370-94400 | The second kept member: "The variable 𝐉 does not enter it." |
| CA-I 95890-96070 | The five families of the resummed density V^♯. |
| CA-I 97640-97752 | The copies reading: smooth far copies at ext_v(ζ), rough copies at ζ. "Off the real slice, the extension of each term is a choice made at each use." Balaban reads 𝐔 through M^·(𝐔) (CMP 122b p. 375). |
| CA-I 13670-13800; 13980-14060; 14155-14210 | The free-current operators (J1)-(J8), the fixed point D^J, the map 𝔏^J, the functional V^J. |
| CA-I 47250-47610 | The form walk expansion, its alphabet, the branching insertions Δ^{(2)}[𝔧_0] and 𝒥[𝔧]. |
| CA-I 5100-5160; 5500-5570; 8839-8912 | The interpolation rule, the form-walk hypothesis, the fixed walk rule (R1)-(R3). |
| CA-I 71085-71145; 72370-72420; 72988-73120; 73540-73640; 124189-124380 | Complex covariance, the decoupled layer 𝒴(𝗌;b) (it reads (𝗌,b,𝐔,𝐉)), the class 𝒞 of terms read on the chain, the carriers, the source image. |
| CA-II 15979-16060 | 5.2:lem-wilson-remainders: the members of 𝐂_k are remainders of Wilson-action expansions and I(U_0). |
| CMP 109 pp. 260-264 (local scan) | J replaces the current functions (1.8); explicit terms extend "by the same formulas"; E^{(j)}(X,g,U,J) is assumed analytic. |
| CMP 119 pp. 261, 270-275 (local scan) | Tube conditions (2.34)-(2.39); the step (3.26)-(3.42). |

CMP 122a/b were not available (pd.md §8 records a Project Euclid bot check; it was not retried). No claim below rests on their text. Where the account quotes or describes their formulas, the account is the source.

## 2. The real structure and four general lemmas

**Conventions.** The account uses the Hermitian convention: 𝔤 is the Hermitian traceless matrices, and U = e^{iηA} with A ∈ 𝔤 is unitary. On G^ℂ put s_G(W) = (W^†)^{-1}. On 𝔤^ℂ put s_H(X) = X^†. A tube point is ζ = (𝐔,𝐉) with 𝐔 G^ℂ-valued and 𝐉 𝔤^ℂ-valued on bonds. Put σ(𝐔,𝐉) = (s_G𝐔, s_H𝐉) bondwise. Its fixed points, the **real pairs**, have 𝐔 G-valued and 𝐉 Hermitian, with no relation between them. The **diagonal** is the set of real pairs (U, J(U)), with J(U) the current of U. Real integration variables (B, V'', ϖ, t, λ) are fixed by σ. A complex switch parameter s goes to s̄.

For a map F between spaces with real structures put F^#(P) := σ'(F(σP)). Call F **σ-equivariant** if F^# = F where both sides are defined. For a scalar function σ' is complex conjugation. For an operator between coordinate spaces with real bases, σ' conjugates its matrix entries in those bases. This is **not** the adjoint. It keeps the order of products.

The bilinear pairing of the account is ⟨X,Y⟩ = Σ_b tr(X(b)Y(b)), with no conjugation (CA-I 94375-94378, "no complex conjugation is taken in it").

**Lemma R0 (pairing).** ⟨s_H X, s_H Y⟩ = \overline{⟨X,Y⟩} for all X, Y. Hence the bilinear transpose K^T of a σ-equivariant operator K is σ-equivariant.

*Proof.* \overline{tr(XY)} = tr((XY)^†) = tr(Y^†X^†) = tr(X^†Y^†), by cyclicity. Sum over b. For the transpose, σ-equivariance of K(P) means s_H(K(P)X) = K(σP)(s_H X). For all X and Y,
\overline{⟨X, K(P)^T Y⟩} = \overline{⟨K(P)X, Y⟩} = ⟨s_H(K(P)X), s_H Y⟩ = ⟨K(σP)s_H X, s_H Y⟩ = ⟨s_H X, K(σP)^T s_H Y⟩.
By the first identity the left side is also ⟨s_H X, s_H(K(P)^T Y)⟩. Since s_H is a bijection, s_H X runs over the whole space. Nondegeneracy gives s_H(K(P)^T Y) = K(σP)^T(s_H Y). ∎

In a basis of 𝔤 (Hermitian matrices), s_H is conjugation of the coordinates. So "real basis" below means a basis of 𝔤, and σ' on operators is conjugation of their matrix entries in such bases.

**Lemma R1 (reality at real points and reflection).** Let D be a connected open set with σD = D, whose real points form a nonempty set. Let F be holomorphic on D with values in a space with a real structure.
(a) If F maps every real point of D to a real point, then F^# = F on D.
(b) If F^# = F, then F maps real points to real points.

*Proof.* (b) At a real P, σP = P, so σ'F(P) = F^#(P) = F(P). (a) F^# is holomorphic: conjugate the coefficients of the local power series of F in real-centred coordinates. F^# and F agree on the real points of D. These form an open subset of the fixed set of σ, a totally real submanifold of maximal dimension. Two holomorphic maps that agree on such a set agree near it (expand in real-centred coordinates; all real derivatives agree, so all complex derivatives agree). The identity theorem on the connected set D gives F^# = F. ∎

This is pd.md §4, stated for maps. Pointwise reality at real pairs, the form (34) of CV, needs only (b) and no σ-invariance of the whole tube.

**Lemma R2 (uniqueness transfers reflection).** Let Φ(d,x) be σ-equivariant in both variables, and let S be a σ-invariant set of x. Suppose that for each d in a set D there is exactly one x(d) ∈ S with Φ(d,x(d)) = 0, a real point. Then x(σd) = σx(d) whenever d, σd ∈ D. In particular x(d) is real at real d.

*Proof.* Φ(σd, σx(d)) = σ'Φ(d,x(d)) = σ'0 = 0, and σx(d) ∈ S. Uniqueness at σd gives x(σd) = σx(d). At real d this reads x(d) = σx(d). ∎

Uses below: inverses (Φ(M,X) = MX − 1), unique fixed points of σ-equivariant maps on σ-invariant balls, principal logarithms and roots fixed by their spectra, and the background minimisers (unique critical points in a σ-invariant regular class of a σ-real functional). For a ball S = {|x| < r}, σ-invariance holds when the norm satisfies |x^†| = |x| pointwise. The operator and Hilbert-Schmidt norms do.

**Lemma R3 (members that do not read the current).** Let f be defined on a set of pairs, and suppose f(𝐔,𝐉) = g(π(𝐔)) for a map π of the configuration alone (for example the block averages M^·(𝐔)) and a function g. Suppose π maps G-valued configurations to real data. Then f is real at a real pair (𝐔,𝐉) if and only if g is real at the real datum π(𝐔). The value does not depend on 𝐉. In particular, if (𝐔, J(𝐔)) is also in the domain, f(𝐔,𝐉) = f(𝐔,J(𝐔)).

*Proof.* f(𝐔,𝐉) = g(π(𝐔)) for every admissible 𝐉. ∎

So for a member that reads only the configuration, reality at independent real pairs is exactly reality on the diagonal. The failure mode of pd.md (5), iεh(P)^r with h vanishing on two slices, reads 𝐉. It cannot occur in such a member.

**Lemma R4 (wordwise reflection).** Let 𝔏 be a set of letters. Each letter a is an operator L_a(P) between coordinate spaces with real bases, depending holomorphically on a point P, with a footprint [a] that does not depend on P. Suppose each L_a is σ-equivariant. A word w = (a_1,…,a_n) with a real coefficient c_w gives K_w(P) = c_w L_{a_1}(P)⋯L_{a_n}(P), with a footprint [w] fixed by the letters, for example ∪_i[a_i] together with listed side branches. Then:
(a) each K_w is σ-equivariant, and K_w^# has the footprint [w];
(b) for any family 𝒲 of words with Σ_w ‖K_w(P)‖ locally uniformly finite, and any coefficient m(w,s) that depends on w only through its footprint and is real at real s, the operator K(s;P) = Σ_w m(w,s)K_w(P) satisfies K(s̄;σP) = σ'K(s;P) whenever m(w,s̄) = \overline{m(w,s)};
(c) this holds for the masks 1{[w] ⊂ W}, for the switch monomials Π_{Δ meets [w]} s(Δ) of the interpolation rule (CA-I 5130-5153), and for the decoupling monomials of CA-I 72384-72387;
(d) words formed from such words by concatenation with real coefficients (products, sums, Neumann series, the words of an inversion series) are again words in 𝔏 with real coefficients.

*Proof.* (a) Entrywise conjugation in real bases is multiplicative and keeps the order of factors: \overline{L_1 L_2} = \overline{L_1}\,\overline{L_2}. So σ'K_w(P) = c_w σ'L_{a_1}(P)⋯σ'L_{a_n}(P) = c_w L_{a_1}(σP)⋯L_{a_n}(σP) = K_w(σP). The footprint is a property of the word, not of P. (b) Conjugation commutes with absolutely convergent sums. Each term transforms as in (a), and its coefficient is conjugated. (c) A mask is 0 or 1. A switch monomial is a product of the s(Δ) over a set fixed by the footprint, so its conjugate is the same monomial at s̄. (d) is the definition of these operations. ∎

**Consequence for the vertex formula.** The account's vertex formula (pd.md (16); CA-I 5218-5269) writes the localised member as f_σ(P) = Σ_{τ⊆σ} (−1)^{|σ∖τ|} f(1_τ;P), where f(1_τ;P) evaluates one fixed functional with each operator K replaced by its masked sum K^{W(τ)} (CA-I 5271-5287). If the functional is σ-real in its operator arguments and the walk families satisfy R4, each f(1_τ;·) is σ-real, hence so is f_σ. This is the "fixed input walk family" identity that pd.md Attack 8 lacked. It holds as soon as every letter is σ-equivariant. Example (29)-(30) of pd.md uses letters ±ih that are not σ-equivariant one by one. Lemma R5 shows no letter of the account is of that kind.

## 3. The free-current letters are real at real pairs

**Lemma R5 (letters).** Assume the following inputs (L1)-(L2). Then every operator and map in the list (J1)-(J8) of `4.5:lem-free-current-operators` (CA-I 13706-13799), the maps of `4.5:lem-nonlinear-correction` (CA-I 13980-14012) and the functionals of `4.5:def-higher-order-functional` (CA-I 14155-14186) is σ-equivariant. Each walk of their concatenated-walk expansions (J8) is σ-equivariant with the same footprint.

- (L1) *Background operators.* The configuration-only operators D_U, D_U^*, R_b, G_0, G', R, P, Q, Q^*, ℓ (a positive number), 𝔊̃_0, H_0, C^{(2)} of CMP 99b (3.134)-(3.136), the nonlinear map C of CMP 102b (50)-(58) and its derivatives C', C'', and the Wilson Taylor remainder V_0, are holomorphic on connected domains whose real points are the G-valued configurations there, and they map real configurations and real arguments to real values. This is their definition at real backgrounds in CMP 99b, 102b, used by the account at CA-I 13670-13680 and 13980-14012. The account states reality operator by operator for the alphabet of the form assembly (CA-I 47577, "Symmetry and reality hold operator by operator"), and reality of the response chart at independent real 𝐉 (`4.5:prf-chart-covariance`(4), CA-I 15027-15028). By Lemma R1(a) these operators are σ-equivariant.
- (L2) *Elementary walks.* Each elementary walk of G', G_0, T' and of the products DG', G'D^*, D^*G_0, G_0D (the elementary-sheet lemma, CA-I 47294-47313, from CMP 99b Theorems 3.4, 3.7, 3.9, 3.10) is a product of real local operators at real configurations. pd.md Attack 8 read this off CMP 99b (3.87)-(3.90), pp. 409-410: real partitions of unity, local propagators, commutator errors. These walks read 𝐔 only, so Lemma R1(a) makes each σ-equivariant.

*Proof.* Write s for s_H on 𝔤^ℂ-valued fields and gauge parameters. All base points move from P to σP; this is not repeated.

(i) *Commutators.* For X, Y ∈ 𝔤^ℂ, [X,Y]^† = [Y^†,X^†] = −[X^†,Y^†]. Hence (i[X,Y])^† = −i·(−[X^†,Y^†]) = i[X^†,Y^†], and ((2i)^{-1}[X,Y])^† = (2i)^{-1}[X^†,Y^†]. So both bilinear maps (X,Y) ↦ (i/2)[X,Y] and (X,Y) ↦ (2i)^{-1}[X,Y] are σ-equivariant.

(ii) *c^{(1)}, c^{(2)}.* CA-I 13690-13700 gives c^{(1)}(A,λ)(b) = (i/2)[λ(b_-) + R_bλ(b_+), A(b)] and c^{(2)}(λ,λ)(b) = (2i)^{-1}[λ(b_-), (D_Uλ)(b)]. By (i) and (L1) both are σ-equivariant. So is the polarisation c^{(2)}(λ_1,λ_2), a real combination.

(iii) *𝔧_J, 𝔨_J, 𝔪_J.* They are defined by ⟨λ,𝔧_J(A)⟩ = ⟨A,𝔨_J(λ)⟩ := ⟨c^{(1)}(A,λ),J⟩ and ⟨λ_1,𝔪_J(λ_2)⟩ := 2⟨c^{(2)}(λ_1,λ_2),J⟩. By Lemma R0 and (ii),
\overline{⟨λ,𝔧_J(A)⟩} = \overline{⟨c^{(1)}(A,λ),J⟩} = ⟨c^{(1)}(sA,sλ),sJ⟩ = ⟨sλ, 𝔧_{sJ}(sA)⟩,
with the right sides at σP. The left side is ⟨sλ, s(𝔧_J(A))⟩ by Lemma R0. Since sλ is arbitrary, s(𝔧_J(A)) = 𝔧_{sJ}(sA). The same argument gives 𝔨 and 𝔪.

(iv) *Θ'_J, G^J_π, 𝗊_J, H^J, Θ_J, G̃^J, G^J_1, H^J_1.* Θ'_J = 𝔨_JΛ + Λ^T𝔧_J + Λ^T𝔪_JΛ with Λ = G'RD^*_U is a sum of products of σ-equivariant operators and bilinear transposes of such (Lemma R0). G^J_π = Σ_n G_0(Θ'_JG_0)^n converges absolutely (J2); conjugation commutes with the sum. 𝗊_J = (QG^J_πQ^*)^{-1} is σ-equivariant by Lemma R2 with Φ(M,X) = MX − 1. H^J = G^J_πQ^*𝗊_Jℓ^{-1} is a product. Θ_J is the symmetric operator of the quadratic form 2⟨H^JC^{(2)}(ℓA),J⟩, a polarisation with real coefficients of a σ-real form (Lemma R0). G̃^J = (I − 𝔊̃_0Θ_J)^{-1}𝔊̃_0, G^J_1 = Σ_n G_0((Θ'_J + Π^TΘ_JΠ)G_0)^n with Π = I − D_UΛ, and H^J_1 = G^J_1Q^*(QG^J_1Q^*)^{-1}ℓ^{-1} follow in the same way.

(v) *Walks.* By (J8) the series for G^J_π, 𝗊_J, G̃^J, G^J_1 are expanded into concatenated walks: pieces of walks of G_0 joined by the local insertions Θ'_J, Π^TΘ_JΠ and Q(G^J_π − G_0)Q^*, each with its side branch (the walk of H^{J,T}J inside Θ_J; the walks of Λ and of RG' inside Θ'_J), the side branches counted among the domains (CA-I 13793-13799). These are words with real coefficients in letters that are σ-equivariant by (L1), (L2) and (iii). Lemma R4 applies.

(vi) *D^J, 𝔏^J, 𝔇^J, 𝔗^J.* D^J(A') is the unique fixed point of X ↦ C(ℓA' − ℓH^JX) in S = {X: X = 0 on Λ_0, |X| < ε_3/B_0} (CA-I 13998-14001). This map is σ-equivariant by (L1) and (iv). S is σ-invariant, since the support condition is real and the norm satisfies |X^†| = |X| pointwise. Lemma R2 with Φ(d,X) = X − C(ℓA' − ℓH^JX) gives D^{sJ}(sA') = sD^J(A'). Then 𝔏^J = A' − H^JD^J is σ-equivariant. Derivatives in real directions of σ-equivariant maps are σ-equivariant (pd.md Lemma 3), so C'(ℓ𝔏^JA') is. Then 𝔇^J = (I + ℜ^J)^{-1}C'(ℓ𝔏^JA')ℓ and 𝔗^J = I − H^J𝔇^J are σ-equivariant.

(vii) *V^{J,disp}, W^J, V^J, 𝕍'^J.* Each is a real linear combination of pairings of σ-equivariant objects, plus V_0(𝔏^JA';U) (CA-I 14170-14186). Lemma R0 and (L1) make each σ-real. This agrees with the port of V^J in pd.md Attack 5; here it comes with the operators, not only the scalar. ∎

**The branching insertions.** The assembly alphabet adds the vertex operators M_J, Δ^{(2)}[𝔧_0] and 𝒥[𝔧] (CA-I 47537-47567). M_J is linear in J with a configuration-only coefficient; Δ^{(2)}[𝖿] and 𝒥[𝖿] are configuration-only operators linear in the inserted field 𝖿 (CA-I 47340-47371, 47372-47378). Under (L1), which the account asserts for this alphabet at CA-I 47577, each is σ-equivariant for σ-equivariant 𝖿. The inserted fields 𝔧_0 and 𝔧 are images of the current under σ-equivariant operators, of the kind in (iii)-(iv). So Lemma R4 applies to the five stages of the assembly (CA-I 47555-47573). This closes the "termwise reflection with the rule's domain assignments" that pd.md Attack 8 left open, **given (L1)-(L2)**. The fixed rule itself (CA-I 8839-8910) builds each family from cells, words of the inversion rule, and composition of local letters, products, sums and branchings, with the real profile η_q of (F1) and the decompositions (F3). Its interpolation clause (R3) attaches real switch monomials by footprint. Lemma R4 covers each of these.

**Lemma R6 (SU(2): the tubes are σ-invariant).** For W ∈ SL(2,ℂ), |s_G(W) − 1| = |W − 1| in the operator norm and in the Hilbert-Schmidt norm. Hence a set of pairs defined by bounds on |W(p) − 1| for plaquettes and other products of bond variables, on |A'| with 𝐔 = e^{iηA'}U, and on |𝐉|, all with such norms, is σ-invariant when G = SU(2).

*Proof.* With J_2 = [[0,1],[−1,0]], a real orthogonal matrix, every W ∈ SL(2,ℂ) satisfies W^{-1} = J_2W^TJ_2^{-1}. Check it on W = [[a,b],[c,d]]: J_2W^TJ_2^{-1} = [[d,−b],[−c,a]], the adjugate, which is W^{-1} since det W = 1. So W^{-1} − 1 = J_2(W − 1)^TJ_2^{-1}. Conjugation by a unitary and transposition keep both norms. Next, s_G(W) − 1 = (W^{-1})^† − 1 = (W^{-1} − 1)^†, and the adjoint keeps both norms. So |s_G(W) − 1| = |W^{-1} − 1| = |W − 1|. Since s_G is a group homomorphism, it maps the plaquette product of 𝐔 to the plaquette product of s_G𝐔. Finally σ maps e^{iηA'}U to e^{iηA'^†}U, and |A'^†| = |A'|, |𝐉^†| = |𝐉|. ∎

For SU(N) with N ≥ 3 the first identity fails: W = diag(2,2,1/4) has |W − 1| = 1 and |W^{-1} − 1| = 3 in the operator norm. So for N ≥ 3 only the local form of Lemma R1 (on σ-invariant polydiscs) is available. CV in the pointwise form (34) does not need global invariance. Lemma R6 matters only for Attack 12 below.

Status: §§0-3 written; §4 (Attack 10) follows.
