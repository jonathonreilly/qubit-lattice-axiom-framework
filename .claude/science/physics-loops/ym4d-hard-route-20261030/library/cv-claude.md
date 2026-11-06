lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T11:18Z

# CV: reality of the prescribed scalar interaction at independent real current

Queue row 349 (`cv-claude`). Pinned at commit 3c0e25954. Proof attack by Claude (Opus 5.5, max effort), not yet checked by the other model. Research text, not an audit; it grants no status.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the complete account (CA-I, CA-II at `31a47c543775`) and the outline. Tadeusz Balaban for the construction (CMP 99b, 102, 109, 116, 119, 122a/b). The earlier Codex rounds in `library/pd.md` (Lemmas 1-7, attacks 1-9) and the digest `library/prior/cv-claude.md` are reused, not repeated.

Kind of result (FINISH rule 9): proof of steps the account assumes, namely the reality clause of (H_j)(d) and of the family clauses. No correction of their text. No computer-assisted step. No numerics were run.

## 0. Summary

Claim first.

1. **The independent current is not where CV can fail.** Inside V_ω, the free current 𝐉 enters through three routes only: the explicit free-current operators, the old terms read at the tube point ζ itself (rough copies), and the chain layers. Each route preserves reality at real independent pairs, given reality of its inputs (Lemmas R4, R5; Theorem A; Proposition B). Every other member reads ζ only through the configuration 𝐔. For those members, reality at an independent real pair is the same statement as reality at the real configuration (Lemma R3).
2. **The reality clause of (H_j)(d) holds as an implication** (Theorem A). The account assumes it at CA-I 58253-58254 ("They are real at real (𝐔,𝐉)") and in its family clause, CA-I 60651. Here it is proved by an induction that carries reality of every old term as a clause, from the formulas of CMP 119 (3.28)-(3.47) and the account's free-current operators.
3. **The input-family gap of pd.md Attack 8 is closed** for every walk family whose letters are real. Wordwise reflection (Lemma R4) follows from letterwise reflection. The free-current letters, including the branching insertions, are real at real pairs (Lemma R5). The example (29)-(30) of pd.md needs letters that are individually nonreal. Under inputs (L1)-(L2) of Lemma R5, which the account asserts operator by operator for the alphabet (CA-I 47589), no letter of the account is of that kind.
4. **The preparatory stages and the switched chart are real at real points** (Proposition A', Corollary R7). So the stored terms ℂ^{(n)} of the large-field preparation, and every chart the members are read at, add no obstruction either, given the inputs named there.
5. **What stays open** is one precise lemma, (CH-a) ∧ (PT) of §7. (CH-a): each chain layer is a switched-chart fixed point; the account cites this from a statement not found by name in CA-I-III. (PT): four objects that the account takes from CMP 122a/b as printed are real at real data: the source 𝖩_3 of (1.55), the identification of I(U_0), Balaban's ℙ^{(j)}, and the change-of-variables objects. None of these asks for reality at an independent current; all are statements about real data or about the form of an equation.

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

## 2. The real structure and five general lemmas

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

- (L1) *Background operators.* The configuration-only operators D_U, D_U^*, R_b, G_0, G', R, P, Q, Q^*, ℓ (a positive number), 𝔊̃_0, H_0, C^{(2)} of CMP 99b (3.134)-(3.136), the nonlinear map C of CMP 102b (50)-(58) and its derivatives C', C'', and the Wilson Taylor remainder V_0, are holomorphic on connected domains whose real points are the G-valued configurations there, and they map real configurations and real arguments to real values. This is their definition at real backgrounds in CMP 99b, 102b, used by the account at CA-I 13670-13680 and 13980-14012. The account states reality operator by operator for the alphabet of the form assembly (CA-I 47589, "Symmetry and reality hold operator by operator"), and reality of the response chart at independent real 𝐉 (`4.5:prf-chart-covariance`(4), CA-I 15027-15028). By Lemma R1(a) these operators are σ-equivariant.
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

**The branching insertions.** The assembly alphabet adds the vertex operators M_J, Δ^{(2)}[𝔧_0] and 𝒥[𝔧] (CA-I 47537-47567). M_J is linear in J with a configuration-only coefficient; Δ^{(2)}[𝖿] and 𝒥[𝖿] are configuration-only operators linear in the inserted field 𝖿 (CA-I 47340-47371, 47372-47378). Under (L1), which the account asserts for this alphabet at CA-I 47589, each is σ-equivariant for σ-equivariant 𝖿. The inserted fields 𝔧_0 and 𝔧 are images of the current under σ-equivariant operators, of the kind in (iii)-(iv). So Lemma R4 applies to the five stages of the assembly (CA-I 47555-47573). This closes the "termwise reflection with the rule's domain assignments" that pd.md Attack 8 left open, **given (L1)-(L2)**. The fixed rule itself (CA-I 8839-8910) builds each family from cells, words of the inversion rule, and composition of local letters, products, sums and branchings, with the real profile η_q of (F1) and the decompositions (F3). Its interpolation clause (R3) attaches real switch monomials by footprint. Lemma R4 covers each of these.

**Lemma R6 (SU(2): the tubes are σ-invariant).** For W ∈ SL(2,ℂ), |s_G(W) − 1| = |W − 1| in the operator norm and in the Hilbert-Schmidt norm. Hence a set of pairs defined by bounds on |W(p) − 1| for plaquettes and other products of bond variables, on |A'| with 𝐔 = e^{iηA'}U, and on |𝐉|, all with such norms, is σ-invariant when G = SU(2).

*Proof.* With J_2 = [[0,1],[−1,0]], a real orthogonal matrix, every W ∈ SL(2,ℂ) satisfies W^{-1} = J_2W^TJ_2^{-1}. Check it on W = [[a,b],[c,d]]: J_2W^TJ_2^{-1} = [[d,−b],[−c,a]], the adjugate, which is W^{-1} since det W = 1. So W^{-1} − 1 = J_2(W − 1)^TJ_2^{-1}. Conjugation by a unitary and transposition keep both norms. Next, s_G(W) − 1 = (W^{-1})^† − 1 = (W^{-1} − 1)^†, and the adjoint keeps both norms. So |s_G(W) − 1| = |W^{-1} − 1| = |W − 1|. Since s_G is a group homomorphism, it maps the plaquette product of 𝐔 to the plaquette product of s_G𝐔. Finally σ maps e^{iηA'}U to e^{iηA'^†}U, and |A'^†| = |A'|, |𝐉^†| = |𝐉|. ∎

For SU(N) with N ≥ 3 the first identity fails: W = diag(2,2,1/4) has |W − 1| = 1 and |W^{-1} − 1| = 3 in the operator norm. So for N ≥ 3 only the local form of Lemma R1 (on σ-invariant polydiscs) is available. CV in the pointwise form (34) does not need global invariance. Lemma R6 matters only for Attack 12 below.

## 4. Attack 10: carry reality as a clause of the induction

**Idea.** pd.md Attack 9 tried to get the reality of inherited members from the Route's clause (a) at levels j < k, which concerns weight factors only, and stopped there. Attack 10 instead strengthens the induction: it carries reality of every inherited term as a clause and proves that one step preserves it. This is not adding (H_j)(d) as an assumption. It proves the reality part of (H_j)(d), and of the family clause at CA-I 60651, from the step's formulas.

**The clause.** (R_j): for every i ≤ j, every localised term held after step i is real at every real point of its domain. "Real point" means a real pair (𝐔,𝐉) of its tube, with 𝐉 independent of 𝐔, together with real values of its slot, integration and switch variables. The terms are the small-field terms E^{(i)}(X;·) and their pointed terms E^{(i)}(X;·,z), the terms R^{(i)}, B^{(i)}, B''^{(i)}, and the stored and frozen terms ℂ^{(i)}. Base: (R_0) holds, since the Wilson action extended by ½tr(W + W^{-1}) is σ-real (pd.md (24)).

**Theorem A (the whole-lattice step preserves reality).** Fix the constants in the account's order. Let j ≥ 1. Let f = (f_i)_{i<j} be the input family of hypothesis (H_j), CA-I 58232-58240, with all its terms real at real points. Assume (L1), (L2) of Lemma R5. Assume the convergence and analyticity parts of (H_j)(d), and the account's reality of the response chart at real independent 𝐉, real data and real switches (`4.5:prf-chart-covariance`(4) and its switched form, CA-I 15027-15028, 15099-15102, 15324-15333). Then the terms E^{(j),♮}_𝔰(X;·,z), ♮ ∈ {𝔄,ℜ}, of the whole-lattice step j are real at every real pair (𝐔,𝐉) of the domain of CMP 119 (2.27)(ii).

Consequently, by induction on j from (H_1)(d), the clause "They are real at real (𝐔,𝐉)" of (H_j)(d) holds for every j ≤ K as an implication from these inputs. So does the reality part of the family propagation that `4.38:cor-volume-families` takes as its hypothesis (c).

*Proof.* (H_j)(d) defines the step (CA-I 58241-58248): it is the last logarithm in CMP 119 (3.28), with Ω_j = Λ_j the whole torus, pointed as in (3.37)-(3.42) and expanded as in (3.44)-(3.47) under the rule ℛ. Fix a real pair P. Every quantity below is evaluated at P. The fluctuation field A is a real integration variable.

*Step 1 (the integrand).* The integrand of the last logarithm in (3.28) is χ^{(k)}(A)·exp[−½⟨A,𝖠(P)A⟩ + Σ (old terms at the chart point) + (higher-order action terms)], with the parameters s, t of (3.27) and (3.30). Here and below k = j − 1 in Balaban's numbering.
- 𝖠(P) is σ-equivariant (Lemma R5), and is real symmetric at real P (`4.14:prf-form-walk-expansion`(c), CA-I 47274-47276).
- The old terms are read at the response chart, a σ-equivariant map of (P,A) by the cited chart reality. The terms of f are real at real points. So each composite is real at (P,A).
- The higher-order terms are V^J and its derivatives V'_k(tg_k,A,b) of (3.31). They are σ-real by Lemma R5(vii).
- χ^{(k)} and χ^{(k)}_t are characteristic functions of real A. The parameters s, t ∈ [0,1], g_k and ℓ are real.
So at real P the integrand is a real function of real A, and its Gaussian factor is positive.

*Step 2 (expectations and logarithms).* The integral converges at P: the precision is coercive on the admitted domain (the accretivity used in pd.md Lemma 7, CA-I 105232-105254). Its Gaussian normalisation is a positive real number. Each expectation in (3.28), (3.30), (3.32), (3.37) is a ratio of an integral of a real function by a positive real integral, hence real. The t-integrals of (3.30) and (3.37) are over [0,1]. The logarithm of the determinant is written by (3.34)-(3.36) as −½∫_0^∞ tr[(C^*Δ^{(k)}C − λ_0)(C^*Δ^{(k)}C + λ)^{-1}]dλ with real λ_0 > 0. At real P the operators are real, so the integrand is a real trace. This is the branch of pd.md Lemma 7. The constant of (3.33) is real. So (3.38) is real at P.

*Step 3 (pointing).* The functions h_z of (3.40) are products of max{1 − L^{-1}|t|, 0}, real. So the pointed functions E^{(k+1)}_0(Λ,z) of (3.41) are real at P.

*Step 4 (localised expansions).* (3.44)-(3.47) are a cluster expansion of the expectations, a Mayer expansion of the exponential, and generalised random-walk expansions of the operators in the second term of (3.37).
- The activities of the cluster expansion are expectations of products of real functions with real interpolation parameters. By Step 2 they are real.
- The Mayer coefficients are integers (pd.md (19), CA-I 21005-21039). Absolute convergence keeps the sums real.
- The walk expansions are those of the rule ℛ (CA-I 8839-8910). By Lemma R5 and its paragraph on branching insertions, each walk is σ-equivariant with its footprint. By Lemma R4 the masked sums and switch monomials are real at real switches. Each localised trace is a real number at P.
- The split into 𝔄- and ℜ-terms is by a marking of the term's index (CA-I 58248-58250). It does not depend on P.
Each E^{(j),♮}_𝔰(X;·,z) is a convergent real combination of such numbers. So it is real at P.

*Induction.* (H_1)(d) is CMP 119 §3 read at k = 0, which the account identifies with CMP 119 §1 (CA-I 58269-58272). Its input is the Wilson action, real at real points by (R_0). The output family of step j is the input family of step j + 1, by (c^+) of (H_{j+1}). For 4.38, the new family is [log Z^{(k)} − log Z^{(k)}(1)] + 𝖲_{k+1}(g'^{-2},𝐄_f) (CA-I 60688). The first bracket is a function of the block configuration only, a logarithm of a positive normalising integral at real configurations, so it is real there. The second is real by the above. ∎

**What Theorem A settles.** It discharges, as an implication from the named inputs, the reality clause the account assumes in (H_j)(d) and in its family clause. It also covers every inherited small-field term that V_ω reads at an independent real pair. In particular, a rough copy of a pointed term is read at ζ itself (CA-I 97681-97682). Its value at a real independent pair is real whenever the copied term is a term of the whole-lattice family, or is identified with one by `4.4:cor-localised-independence` (CA-I 9615-9669).

**Proposition A' (the preparatory stages preserve reality).** Work at level j, stage n + 1 of the run of CMP 122a as the account writes it (section 4.24). Assume that the stored terms ℂ^{(n)} and the inherited terms 𝔼, ℝ, 𝔹 are real at real points of their domains, and assume (L1)-(L2). Then the stage's new densities ℂ^s_G(X) and ℂ^s_I(X) of `4.24:thm-survivor-block-expansion` (CA-I 104760-104832) are real at every real point of 𝔇^♭_{n+1}(X), and so are the terms f_b of an interrupted change of variables (`4.27:lem-interrupted-terms`, CA-I 137320-137400).

*Proof.* At a real point the stage pair (𝕌,𝕁) is real.
- *The stage form.* K(σ') = C^*Δ^{(j)}(σ')C (CA-I 103680-103683). C is "the holomorphic continuation of Balaban's real map" and C^* = C^T (CA-I 103664-103666), so C is real at real points. Δ^{(j)}(σ') is defined by the form ⟨B,(QG_1Q^*)^{-1}B⟩ − a⟨B,B⟩ − 2⟨H_1D^{(2)}(B),J⟩ (CA-I 103673-103679), decoupled by σ'. This is the operator of Lemma R5(iv) at the current J, with the switch rule of Lemma R4. So K(σ') is real symmetric at real (𝕌,𝕁,σ'). The block 𝒜_ss is a coordinate compression of it, hence real symmetric. It is coercive (`4.24:lem-block-coercivity`), so its Gaussian is a positive measure on the real survivor variables.
- *ℂ^s_G.* The left side of (4.24:eq-survivor-block-expansion-1) is the logarithm of a positive real integral plus the real vacuum constant E_0^{(j)}. Its localisation into bond densities uses the half-line resolvent integral of `4.24:lem-log-resolvent` (pd.md Lemma 7) and the termwise walk expansion of the block resolvent (`4.24:prf-block-walk-expansion`). Both are words with real coefficients in letters that are real at real points, so Lemma R4 makes each density real.
- *ℂ^s_I.* By (ii)(a) of that theorem, Σ_X ℂ^s_I(X) = log⟨χ^s exp Σ_e v_e⟩_s, with ⟨·⟩_s the normalised Gaussian expectation of precision 𝒜_ss. The elements are of three kinds (`4.24:def-survivor-elements`, CA-I 104461-104490): the stage's own and mixed members, which are stored and inherited terms at real arguments; the collar pairs e_a, which are real-parameter integrals of entries of the real kernel 𝒜^w(σ') paired with real 𝖡 (CA-I 103703-103712); and the change-of-variables objects. The last are the terms of `4.27:lem-interrupted-terms`: composites of inherited terms at the map of pairs Φ(b(𝖡))[P] with a real datum b(𝖡) = g_jC𝖡 − h𝐃̃(g_jC𝖡); Balaban's Δ^{(j)} and ℙ^{(j)}; the Wilson-action difference 𝖶 with real weights 𝖼; and f_b, the trace of the logarithm of a real Jacobian near the identity plus real increments. The map of pairs is the switched chart, real at real data by Corollary R7 (§5a). ℙ^{(j)} is Balaban's higher-order term, whose free-current form V^J is real by Lemma R5(vii). So every v_e is real at real points. The characteristic functions χ^s are real. The abstract cluster expansion writes the logarithm as a convergent sum with real combinatorial coefficients of real-parameter integrals of expectations of products of the v_e. So each ℂ^s_I(X) is real. ∎

Two inputs of this proof are read from the account's descriptions, not from formulas: that ℙ^{(j)} is the real-point form of the account's V^J, and the list of change-of-variables objects in clause (c) of the statement that introduces them, which was not located (CA-I 104487 cites it). Proposition A' removes the 𝐁''_k = ℂ^{(n)} terms (CA-I 78469-78471) from the open residue, up to these two readings.

**Exact failure of Attack 10 for CV itself.** The same induction must also cross the large-field half of each step: the preparatory operations of CMP 122a, the operation 𝐑, the operation 𝐓'_k and the operations CMP 122b (1.90)-(1.99). For these the step needs a recipe for each term, and Lemmas R2-R5 then apply term by term. The account reproduces only part of these recipes. Two kinds are taken by statement.
- (a) The chain layers 𝒴(𝗌;b) and their current rider. The layer theorem is cited in `4.21:lem-exempted-set` by its clauses (a)-(f) only (CA-I 72396-72399). The account says that the layer is the unique solution, in the ball of that theorem, of equations built from the decoupled operators K(σ) (CA-I 72510-72514), and that at real points it is Balaban's layer (clause (d)). The layer reads (𝗌,b,𝐔,𝐉) (CA-I 72405-72420). Reality at a real **independent** pair is not stated.
- (b) Balaban's step-k objects that the account takes as printed and that enter V_ω: the source 𝖩_3 of CMP 122b (1.55); the identification of I(U_0) (CMP 122b (1.11), p. 374); Balaban's ℙ^{(j)} at real points; and the change-of-variables objects of the statement cited at CA-I 104487. Given these, Proposition A' covers the 𝐁''_k = ℂ^{(n)} terms.
For (a), Lemma R2 reduces reality to σ-equivariance of the layer equations and σ-invariance of the ball; §5a carries this out for the switched chart (Corollary R7). What is missing is the statement that each chain layer is such a fixed point. For (b) the formulas are in CMP 122a/b, which are not available here (Project Euclid answered with an Incapsula bot page on 2026-11-06; not retried). So the induction step is proved for the small-field half and stops at the first large-field term without a written recipe. This is a missing text, not a failing identity: no term was found that is nonreal at a real pair.

## 5. Attack 11: remove the independent current from V_ω

**Idea.** pd.md Attacks 1, 4 and 5 treated 𝐉 as a variable that every member may read. Attack 11 reads the account's conventions to find which members of V_ω read 𝐉 at all. Lemma R3 then disposes of the members that do not.

**Proposition B (how the tube point enters V_ω).** Let C be a treated component at the operation 𝐑_k, ζ = (𝐔,𝐉) a real pair of 𝔖, and ϖ ∈ supp Π real. Each member of the five families of V^♯(C^♯;ζ;Φ_C,0) (CA-I 95977-96063) is of one of three kinds.
- (B1) *Configuration only.* It reads ζ only through 𝐔, through the block averages M^·(𝐔) and the backgrounds built from them. This covers Balaban's step-k members, since Balaban replaces M^·(U_k), V'' by M^·(𝐔) (CMP 122b p. 375, quoted at CA-I 97745-97750); the smooth far copies, read at ext_v(ζ), the box-minimiser pair of the level-p_v averages of 𝐔 (CA-I 97650-97680); and the members of 𝐂_k (below).
- (B2) *Old terms at ζ itself.* The rough copies and "every other copy" (CA-I 97681-97682; convention (b), CA-I 94133-94151).
- (B3) *Terms read on the chain at ζ* (convention (a)). These are the old terms 𝐄, 𝐑, 𝐁^{(j)} with X ∩ Z ≠ ∅, the 𝐁''_k-terms and the frozen terms of the class 𝒞 (CA-I 73097-73105), read on the carrier pair chain(m).
The members are combined by the vertex formula with real switches and masks, by connected series with integer coefficients, by the real weights w̄_v, by the frame average (2^dd!)^{-1}, by the real partition of unity, and by add-and-subtract with real coefficients. These operations preserve reality at real points (pd.md Lemma 3, (16), (19); Lemma R4).

The list is read off the account's conventions (a)-(e) of `4.23:def-extension-conventions` and the copies definition. It is not a re-derivation of the localisation identity.

**Consequences.**

(i) *(B1) members.* By Lemma R3, such a member is real at the real pair (𝐔,𝐉) iff it is real at the real datum M^·(𝐔). The independent current plays no role.

(ii) *The boundary family 𝔳^𝐂.* The account lists its members (CA-II 15985-16019): (Ca) remainders of the expansions of Wilson actions CMP 122b (1.17), (1.20), (1.24), (1.29), (1.36), (1.46)-(1.48) on Z; (Cb) their counterparts off Z, cut by the real partition of π_k; (Cc) I(U_0). The source part 𝔠_w is removed.
- (Ca), (Cb): Wilson actions with real weights, their Taylor polynomials in real directions, their remainders and their differences between background evaluations are real at real arguments (pd.md Lemma 6). The backgrounds U_0, U^0 are built from 𝖵 = M^k(𝐔)|_{C∖Λ} through the Λ-datum, which is real at real arguments by `4.23:def-lambda-datum`(c) (CA-I 93980-93986). So they are real at real 𝐔. If an expansion's linear term pairs with the free current, the remainder is still real at real (𝐔,𝐉,A) by Lemma R0.
- (Cc): U_0 = U_{k,C}(𝖵, V_Λ(𝖵)) reads 𝐔 only, and is real at real 𝐔. At real U_0, I(U_0) is real **provided** (I0): it is the logarithm of the denominator of CMP 122a (1.100) plus terms real at real U_0, as CMP 122b (1.11) and p. 374 print it (CA-II 15985-15988 describes it this way). The denominator is positive at real exteriors by 4.32(c), proved in pd.md Lemma 1 from the background-domain construction. So the logarithm is real.
So 𝔳^𝐂 is real at every real pair, given (I0) and pd.md Lemma 1's input. This removes the exclusion of I(U_0) and of the other U_0-members that stopped pd.md Attack 7, up to (I0).

(iii) *The quadratic form.* The second kept member does not read 𝐉 (CA-I 94387, "The variable 𝐉 does not enter it") and is at real points the form of CMP 122b (1.71) (clause (q0), CA-I 93890-93893). By Lemma R3 it is real at every real pair.

(iv) *(B2) members.* They are real at real independent pairs by Theorem A and the induction (R_{k−1}).

(v) *(B3) members.* An old term at the chain point is real when the chain point is a real pair: by (R_{k−1}), or by Theorem A for small-field terms.

**Exact failure of Attack 11.** It proves CV for the members of kinds (B1) and (B2) up to two inputs, and reduces (B3) to the reality of the chain. Two statements stay open, and neither involves the independent current through a route not already covered.
- (CH) The carrier pair chain(m) is real at real (ζ,ϖ,𝗌). By Lemma R2, this follows if the layer equations are σ-equivariant and the uniqueness ball is σ-invariant. The account states uniqueness in a ball and builds the equations from the decoupled operators, which are σ-equivariant (Lemmas R4, R5). The remaining ingredients are not written out in what was read (§4, failure (a)).
- (PT) The (B1) members that Balaban prints are real at real data. The account gives their description for 𝐂_k (handled in (ii), up to (I0)) and their identification "at real points" with Balaban's members (CA-I 96028-96030), but not their recipes for the 𝐁''_k-terms. Note that under the filing hypothesis of `4.23:lem-filing-domains` no Y_0-term is filed at C (CA-I 96096-96103). So those are not part of V_ω.

### 5a. The chain, reduced further

**Corollary R7 (the switched chart is real at real parameters).** Let (U,J) be a real pair of the class 𝔖 of `4.5:thm-chart-existence`, B a real block field within the chart radius, and s real decoupling parameters with |s(Δ)| ≤ e^{κ_1}. Then the objects of `4.5:prf-chart-walk-localisation` at s are real: the primitive operators (4.5:eq-chart-walk-localisation-1), the composites, the fixed point 𝒜^J_0(s)(B) of (4.5:eq-chart-walk-localisation-3), and ℋ^J(s)(B), Λ^J(s)(B), 𝔍(s)(B).

*Proof.* Each primitive operator at s is Σ_ω (Π_{Δ meets ω} s(Δ)) K_ω, over walks with their side branches (CA-I 15277-15303). Its walks are σ-equivariant by Lemma R5 and its inputs (L1)-(L2). The switch monomials are real at real s. Lemma R4 gives reality. The composites are built by the formulas of Lemma R5, so they are real. The fixed point is unique in the ball of (K1), which holds at s by clause 2 of that proposition (CA-I 15325-15330). The fixed-point map is real at real arguments, and the ball is defined by a †-invariant norm. Lemma R2 gives reality of the fixed point. The remaining objects are formulas in it. ∎

This is the decoupled form of the account's proved clause `4.5:prf-chart-covariance`(4), "At G-valued U and real J, B and t_□, everything is real" (CA-I 15027), whose proof is the same fixed-point argument (CA-I 15100-15101). The account does not state the decoupled form.

**Consequence for (CH).** The layer 𝒴(𝗌;b) of `4.21:lem-exempted-set` is built from the decoupled operators K(σ) and a datum, is unique in a ball, and at 𝗌 = 𝟏 is "the layer of the undecoupled operators" (CA-I 72405-72414, 72510-72514). If it is the switched chart of Corollary R7 at its determining set and datum, it is real at real (𝗌,b,𝐔,𝐉). The chain layers ℍ_4,…,ℍ_1 are "supplied by the layer holomorphy statement at the determining sets 𝐁''_k, 𝐁''_k, 𝐁_1, 𝐁_k" (CA-I 73556-73561), with the stage-3 field datum 𝔧_3 = G̃_0(σ)𝖩_3 and 𝖩_3 the right-hand bracket of CMP 122b (1.55) (CA-I 73110-73112). No statement named "the layer holomorphy statement" was found in CA-I, CA-II or CA-III at `31a47c543775` (searched by name). Nor was "the clause fixing the members away from the real points" cited at CA-I 96032. So (CH) reduces to two things: that these layers are given by switched-chart fixed-point problems of the form of Corollary R7, which the cited passages describe but which was not located as a statement; and that their data, b and 𝖩_3, are real at real points, which is a (PT)-type statement.

## 6. Attack 12: prescribe the real part

**Idea.** The account says that off the real slice the extension of each term "is a choice made at each use" (CA-I 97738-97740). pd.md (9) noted that ½(v + v^#) is holomorphic and real at real points, and rejected it because it changes the prescribed function. Attack 12 asks whether the account's own freedom of choice lets us prescribe ½(m + m^#) for every member m filed in C^♯, at every level, with every consumer still served. This is a repair by convention. It is not a proof of CV for the literal prescription.

**Proposition C.** Let G = SU(2). Replace each member m filed in C^♯, at each use and at each level, by m_R := ½(m + m^#). Then:
- (a) m_R is defined and holomorphic on the same tube as m, by Lemma R6. sup|m_R| ≤ sup|m|. Every size bound of the account survives with the same constants.
- (b) If a difference bound is stated for all pairs P, P' of the tube with a σ-invariant distance, it survives: |m_R(P) − m_R(P')| ≤ ½|m(P) − m(P')| + ½|m(σP) − m(σP')|. The oscillation seminorm's distances are built from |A'|, |B'|, |𝐉|-type norms, which are †-invariant.
- (c) G-valued gauge invariance survives, since σ commutes with G-valued gauge maps (σ fixes them). Locality survives, since m^# reads the same variables as m.
- (d) Every identity between members that is linear with real coefficients survives: add-and-subtract exactness, the vertex formula, the filing sums.
- (e) V_ω is real at every real pair, by construction, whatever the chain does. So (CH) is not needed for the repaired prescription.
- (f) At a real point P, m_R(P) = Re m(P). So the repair changes no value of m at real points where m is already real.

*Proof.* (a) Lemma R6 makes the tube σ-invariant, so m^# is defined and holomorphic on it, and |m^#(P)| = |m(σP)| ≤ sup|m|. (b) is the triangle inequality. (c) If λ is G-valued then s_G(λ) = λ, so σ(ζ^λ) = (σζ)^λ, and m^#(ζ^λ) = \overline{m(σζ^λ)} = \overline{m((σζ)^λ)} = \overline{m(σζ)} = m^#(ζ). (d) Apply # to the identity; real coefficients are unchanged. (e) A finite sum of σ-real functions is σ-real (Lemma R1(b)). (f) At real P, m^#(P) = \overline{m(P)}. ∎

**Exact failure of Attack 12.** The repair is harmless only where the members are already real at the points where the theory is read. Two obstructions remain.
- *Diagonal points.* At a physical (diagonal) point the repair replaces a member by its real part. The density of a label of CMP 122b (1.72) is unchanged iff the sum of all exponents multiplying in one integrand is real there, because e^{Re a}e^{Re b} = e^{a+b} exactly when a + b is real. So the repair needs reality of label totals at diagonal points, which is a (PT)-type statement. With (PT) and (R_{k−1}) at diagonal points, together with clause (d) of the layer theorem (the chain at real diagonal points is Balaban's real chain), every member is real at diagonal points and the repair changes nothing there.
- *N ≥ 3.* Lemma R6 fails (example after it). Then m_R exists only on 𝔖 ∩ σ𝔖, a tube of smaller radii. The account fixes radii before γ, γ_H, g, m, g_0, K (CA-I 1642-1717), and pd.md §7 forbids shrinking them afterwards. Every bound would have to be re-proved on the smaller tube.
So for SU(2) Attack 12 removes (CH) at the cost of a convention change, but not (PT).

## 7. Result

**Open lemma**

**(CH-a) ∧ (PT): the chain layers are switched-chart fixed points, and four printed objects of CMP 122a/b are real at real data.** Fix the account's constants in its order: N, the Stage-0 data, L, Stages 1-7, then γ, then γ_H, then g, m, g_0, K (CA-I 1642-1717). For every level k ≤ K and every treated component C at the operation 𝐑_k:
- (CH-a) Each chain layer ℍ_4,…,ℍ_1 at the determining sets 𝐁''_k, 𝐁''_k, 𝐁_1, 𝐁_k (CA-I 73556-73561), and the layer 𝒴(𝗌;b) of `4.21:lem-exempted-set`, is the unique fixed point, in a ball defined by a †-invariant norm, of a switched response-chart map of the form (4.5:eq-chart-walk-localisation-3) at its determining set. The account describes the layers this way (CA-I 72405-72432, 72510-72514, 73107-73112) but cites them from "the layer holomorphy statement", which was not found by that name in CA-I, CA-II or CA-III.
- (PT) The following objects, which the account takes from CMP 122a/b by statement, are real at real data:
  - (PT1) the stage-3 source 𝖩_3, the right-hand bracket of CMP 122b (1.55), and the block data b of the layers;
  - (PT2) I(U_0): at real U_0 it is the logarithm of the positive denominator of CMP 122a (1.100) plus terms real at real U_0, as CMP 122b (1.11) and p. 374 print it;
  - (PT3) Balaban's higher-order term ℙ^{(j)} of CMP 122a, read here as the real-point form of the account's V^J;
  - (PT4) the change-of-variables objects of clause (c) of the statement that introduces them (cited at CA-I 104487, not located), which `4.27:lem-interrupted-terms` lists as composites at the map of pairs, Δ^{(j)}, ℙ^{(j)}, a Wilson difference and the Jacobian terms f_b.

Neither part asks for reality off a slice from values on the slice, which is the failure mode of pd.md Attacks 1-2. (PT) concerns real data only. (CH-a) identifies the form of an equation; Corollary R7 and Lemma R2 then give reality.

**Theorem (reduction; proved here, an implication).** Assume (CH-a) ∧ (PT) at every level. Assume also the inputs named above: (L1)-(L2) of Lemma R5; the account's chart reality at independent real 𝐉 (`4.5:prf-chart-covariance`(4)) and its switched form, Corollary R7; the convergence and analyticity parts of (H_j)(d); the background-domain input of pd.md Lemma 1; and the account's conventions and descriptions as quoted in §§4-5. Then:
1. (R_j) holds for every j ≤ K: every inherited term is real at every real point of its domain.
2. In particular the reality clause of (H_j)(d) and the family clause "reality at real points" hold. Theorem A gives these **without** (CH-a) or (PT).
3. CV, pd.md (34), holds: V_ω(X^~;ξ;𝐔,𝐉) ∈ ℝ for every real ξ ∈ S_ω and every real independent pair (𝐔,𝐉) ∈ Reg_k(X), for every level k ≤ K. This includes the zero-current pairs (U,0) at which the island bound reads the operation (CA-I 21330-21345).

*Proof.* Induction on k. (R_0) holds (§4). Assume (R_{k−1}). The whole-lattice step preserves reality (Theorem A). In the large-field half, Proposition B sorts the members of V^♯ into kinds (B1)-(B3). (B1) members are real at real pairs by Lemma R3 together with (PT), and by §5(ii)-(iii) for 𝔳^𝐂 and the form. (B2) members are real by (R_{k−1}) and Theorem A. (B3) members are real by (CH-a), (PT1) and Corollary R7, together with (R_{k−1}). Proposition A' covers the preparatory-stage terms. The operations that combine members preserve reality (§5). So V^♯, and with it V_ω, is real at every real pair. The same sorting applies to every term the step stores, so (R_k) follows. ∎

**For SU(2) (the first target of T0).** By Proposition C, (CH-a) and (PT1) can be dropped if the account's per-use choice of extension is fixed as m ↦ ½(m + m^#). That repair needs only (PT2)-(PT4) and (R_{k−1}) at diagonal points, together with clause (d) of the layer theorem (at real diagonal points the chain is Balaban's real chain). It is a convention change, and it must be recorded as such wherever CV is used.

**What this does and does not show.**
- It does not prove CV for the literal prescription. Two inputs stay open, (CH-a) and (PT). Both need text that the account does not reproduce in the parts read here: the statement it calls "the layer holomorphy statement", and four printed objects of CMP 122a/b.
- It shows that the independent current adds no obstruction of its own. The three routes by which 𝐉 enters V_ω each preserve reality, given reality of their inputs.
- It proves, as an implication, the reality clause the account assumes in (H_j)(d) and in its family clause (Theorem A). A reader of `4.38:cor-volume-families` may drop the reality part of its hypothesis (c) on these inputs.
- No nonreal ingredient and no counterexample to CV or to 4.32 was found.
- Two statements the account cites by description were not found by name in CA-I-III: "the clause fixing the members away from the real points" (CA-I 96032) and "the layer holomorphy statement" (CA-I 73560). This is a locating note for the lead, not a claim that their text is wrong.
- 4.32 needs more than CV: the measure and support identities (c), (d1), (d2), (d5) and the other weight factors stay as in pd.md §§2-3.

**Kinds (FINISH rule 9).** Theorem A is a proof of a step the account assumes. Proposition A' proves reality for the preparation as the account writes it, a property the account does not state. Lemmas R0-R6 and Corollary R7 are new general lemmas; R7 is the decoupled form of the account's proved clause `4.5:prf-chart-covariance`(4). Proposition B is a reading of the account's conventions; it re-derives nothing of theirs. Proposition C is a proposed repair by convention, not a correction of their text.

**Next steps, each tied to the open item.**
1. The other model checks Lemmas R0-R6, Corollary R7, Theorem A, Proposition A' and Propositions B-C line by line. This is the one check FINISH rule 5 asks for.
2. (CH-a): locate the statement the account calls "the layer holomorphy statement" (CA-I 73560), and check (CH-a): that each chain layer is a switched-chart fixed point as in Corollary R7. The account's sentence at CA-I 72510-72514 says the layer equations separate over components and have a unique solution in a ball, which is the shape Lemma R2 needs. Its data are (PT1).
3. (PT1)-(PT4): add them to the hardening tally of `library/t0-tree.md` as theirs-cited Balaban statements (CMP 122a/b), to be checked against the printed formulas when they are obtained. They concern real data only.
4. If the lead prefers the SU(2) repair, record the convention change of Proposition C at the CV node. That removes (CH-a) and (PT1) for SU(2) and leaves (PT2)-(PT4).

Status: complete for this session. Not checked by the other model.
