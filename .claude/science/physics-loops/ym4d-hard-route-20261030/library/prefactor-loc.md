lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T02:05Z

# prefactor-loc: the substitution step of rank 9 is exact (queue row 158)

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session, pinned at ef3c72aa2 (branch `claude/ym4d-hard-route`). Same-provider text, not yet checked by the other model; not an audit; grants no status. Sources: `library/prefactor.md` (Codex); the Sussman–Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched once by URL into a private scratch folder (SHA-256 `d7f77d4d…b4d6f`, the same file as `sa-map.md`), not copied here, SA nnnn = its lines (read: R3 at 5631–5651, B3 at 3986–4001, PH1–PH19 at 12890–13300, RF8–RF13 at 20300–20500, the determinant section 21064–21452); `parts/hard-core--mapped.md` Text 3 (P1); `gates/p1-gate-2f2ec0f89.md`; `library/route-compare-2.md` Sections 5.3, 9; Balaban CMP 109 and CMP 119 OCR in `~/ym4d-papers/` (only to confirm prefactor.md's citations). No numeric job was run; no step rests on a computation. No subagent.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for B3, RF8–RF13, PH1–PH19 and the R3 map; the requirement proved in Section 6 below is their RF11a. T. Balaban for the averaging map (CMP 109 (0.12)) and the gauge insertion (CMP 109 (0.14)–(0.16)). Codex for `library/prefactor.md`, whose identities (6), (12), (13) this note reads.

## Result

1. **Check.** `library/prefactor.md` (Codex): checked line by line by Claude, first failing step none. Four non-breaking notes (Section 1).
2. **Theorem S (proved here, by hand).** At the trivial background and at every fixed depth, background substitution preserves the bulk coefficient exactly: π̂^{F∘p_k}(K) = L²π̂^F(K/L) + O(|K|³) for F = Ψ_{k-1}, so b[Ψ_{k-1}∘p_k] = b[Ψ_{k-1}] with zero error. This is the outline's RF11a second formula, proved for the actual R3 average, contour gauge and Wilson action.
3. **Corollary T.** For every k ≥ 1, in the bulk (infinite volume, fixed depth): Σ_{l≤k} b_l^0 = b[Ψ_k] exactly, where b_l^0 is the PH18 coefficient of the step-l Gaussian logarithm Φ_l read at level l. Any localised family N^(l) with (PH5) has b(N^(l)) = b_l^0. The error that row 158 asked to bound is identically zero, so it is summable and uniform in depth and volume. No fall-back to the massive trace route is needed for this step.
4. **Open (not this step).** The value: |b[Ψ_k] − k c_0| ≤ c_2 uniformly in k (RF10 first clause, partial-sum form), by the outline's massive trace route (RF12c, RF13, its mixed energy bounds) or by P1. RF10's second clause and B3's nonlinear parts f_j, q_j are untouched.

## 1. Check of `library/prefactor.md` (Codex, row 151)

Checked line by line by Claude, first failing step none. Verdicts: Section 2 example ADVANCE; Section 3 (normalisations, branch, positivity) ADVANCE; Section 4, (3)–(8) ADVANCE; Section 5, (9)–(13) ADVANCE; Section 6, (14) and the scalar example ADVANCE (it states an open obligation and refutes nothing).

What I redid, in brief.

- Section 2. The critical point is (0,s,0) with multiplier s. Eliminating the delta gives s²/2 + (1−s)x²/2 + x⁴/8 + z²/2. The prefactor 2π(1−s)^{-1/2} and the second derivative 1/2 of −½log(1−s) at s = 0 are correct.
- Section 3. T_yx(U^h) = T_yx(U)h(x)^{-1} when h(y) = 1: the mean of h(y)V_ih(x)^{-1} is h(y)Vh(x)^{-1}, since Ad preserves the defining sum. Haar invariance then gives each factor z_g. The normalised density h_0(sin|a|/|a|)², h_0 = (2π²)^{-1}, integrates to one, since 4π∫_0^π sin²r dr = 2π². The crossing-link field is an exact nonlinear right inverse of (1): internal contours are 1, and the straight paths and U[c] each cross the face once. The positivity chain (zero curl, zero contour sums, constant face values, final average) is correct, including the exclusion of constant torus fields by the gauge term.
- Section 4. (3): differentiate S̃'(u(v)) = DF(u(v))^Tλ(v) and use AR = 1. (4): D²(HF) = A^TH''A + BF'' and λ = B^Tμ. (5): block elimination; det[[D, C^T],[C, 0]] = (−1)^m det C² for square C. The volume factor det(AA^T)^{-1/2} and the cross term n^TT_1Rb = (An)^TS_1''b = 0 give (6). (7) and (8): the powers of g, 2π, h_0 and z_g match, with d_02 = d_01 + d_12.
- Section 5. The straightening D(b) = C(b − hD(b)) gives Ab exactly; the quadratic term is ½b^TT_1b with the sign and factor of (9). (10) is the pivot elimination; RF9's inclusion–exclusion sum is a Möbius inversion. (11) is the substitution β = La + LDα. (12) follows from (8), since all constants cancel in the ratios. (13) follows from DΦ_1(1) = 0, because su(2) has no Ad-invariant vector.
- Citations. In the OCR, CMP 109 (0.12) is the average (1), and (0.14)–(0.16) is the exponential gauge insertion with its normaliser z. (1.4)–(1.5) define Z^(j) with the term −2⟨H hC^(2), J⟩, and (2.10)–(2.14) contain the straightening D^(2) = C^(2) and the split. CMP 119 (3.33) has log z = Σ_c log z(c) − ½ log det(C^*ΔC) + const. The OCR is damaged, but the structure matches prefactor.md's reading.

Notes. None breaks a statement.

- N1 (Section 4, "both integrations converge by fibre positivity"). Add one line: T_02 > 0 on ker BA gives T_1 > 0 on ker A (take a = n) and T_2 > 0 on ker B (take a = Rb, then a^TT_02a = b^TT_2b).
- N2 (Section 3, level-1 insertion). The change of variables for the level-1 gauge must use the block-constant extension h̃(x) = h(y(x)). Then G_01 stays invariant, because T_yx(U^h̃) = h(y)T_yx(U)h(y)^{-1} and w is a class function. The text omits this; the claim is true.
- N3 (Section 3, "three final blocks so each block is contractible"). Blocks are cubes, so they are always contractible. Three blocks per direction are used so that the loops through four adjacent blocks are contractible on the torus.
- N4 ((13) on a torus). There, b_h is a contraction of a finite Hessian and needs a lift convention for displacements. B3 reads the bulk coefficient, and Sections 2–7 below supply it.

## 2. Setting and the bulk coefficient

Everything below is at the trivial background U = 1 and at a fixed depth k. No constant is claimed uniform in k.

**Lattices.** L is odd. The level-j lattice, in level-j units, is Z^4; in level-0 units its sites are L^j Z^4. A bond (x, μ) runs from x to x + e_μ, with midpoint x̃ = x + e_μ/2. Level-j blocks are centred at level-(j+1) sites (the nodes).

**Colour.** At U = 1 every linear map below acts in the same way on each colour component, and every Hessian kernel is δ^{ab} times one kernel (PH6). So colour is suppressed: fields are real or complex valued.

**Linear objects.** Q_j is the linearisation at 1 of the one-step R3 map M_{j-1,j}, from level j−1 to level j; Q_{0,j} := Q_j ⋯ Q_1 and Q_{0,0} := 1. τ_j is the linearised contour mean of R3 at level j: for a level-j site x that is not a node, (τ_j w)(x) is the mean, over the R3 contour family from the node y(x) of its block to x, of the path sums of w. Then D²G_{j,j+1}(1) = τ_j^*τ_j. Put

Δ̃_k := d^*d + Σ_{j=0}^{k-1} Q_{0,j}^* τ_j^* τ_j Q_{0,j},  S_k := [[Δ̃_k, Q_{0,k}^*], [Q_{0,k}, 0]].

Δ̃_k is the Hessian at 1 of S̃_k := S + Σ_{j<k} G_{j,j+1}∘M_{0,j}; S_k is the k-fold saddle operator at 1.

**Branches and responses.** u_{0,k}(z) is the k-fold augmented critical branch (prefactor.md Section 3 with k levels), with R_{0,k} := Du_{0,k}(1). p_k(z) is the level-(k−1) critical field at level-k datum z, with R_k := Dp_k(1), a map from level-k fields to level-(k−1) fields.

**Gaussian logarithms.** On a torus, Ψ_k is the normalised k-fold constrained Gaussian logarithm, log G(T_{0,k}, A_{0,k}) minus its value at 1. Here T_{0,k} is the constrained Hessian of S̃_k at u_{0,k}(z), and A_{0,k} = DM_{0,k} there. Ψ_0 := 0. Φ_l is the step-l Gaussian logarithm read at level l, as in prefactor.md: G(T_l, B_l) normalised at 1, with T_l = S_{l-1}'' + G_{l-1,l}'' − μ·M_{l-1,l}'' at p_l(v).

**The k-step form of (12).** On every torus with N ≥ N_0(k, L) final blocks per direction, near 1,

Ψ_k = Φ_k + Ψ_{k-1}∘p_k,  p_k = M_{0,k-1}∘u_{0,k},  R_k = Q_{0,k-1}R_{0,k}.  (2.1)

Proof. Apply prefactor.md Section 4 with F = M_{0,k-1}, its augmented action S̃_{k-1} and branch u_{0,k-1}, and H = M_{k-1,k} with G_{k-1,k}. Every line of (3)–(8) holds for any two composable maps with critical branches. The composite branch is u_{0,k-1}∘p_k. Indeed, at U = u_{0,k-1}(p_k(z)) we have ∇(S̃_{k-1} + G_{k-1,k}∘F) = A^T(λ + G'_{k-1,k}) = A^T B^T μ, by the envelope identity S_{k-1}' = λ and criticality of p_k(z). Uniqueness of the branch near 1 identifies it with u_{0,k}, and applying F gives p_k = M_{0,k-1}∘u_{0,k}. Fibre positivity: T_{0,k} > 0 on ker A_{0,k} at 1 (Lemma B (iii) on the torus momenta) and nearby by continuity; then note N1. ∎

**Bulk kernel and coefficient.** For a functional F of level-j fields, Lemma D gives a translation-invariant kernel H_F(b, b') = π^F_{μν}(ỹ − x̃), for b = (x, μ) and b' = (y, ν), with Σ_u e^{m|u|}|π^F_{μν}(u)| < ∞. It is the limit of the torus Hessians D²F_N(1). Its symbol is π̂^F(q) := Σ_u π^F(u) e^{iq·u}, analytic for |Im q| < m. Following PH18,

b_{μν}[F] := Σ_u π^F_{μν}(u) u_μ u_ν = −∂_μ∂_ν π̂^F_{μν}(0)  (μ ≠ ν),  b[F] := b_{12}[F].

Under hypercubic covariance (Lemma D (c)), b_{μν} does not depend on the pair (PH16–PH18). **B3's sequence** is b_l^0 := b[Φ_l].

## 3. Lemma B: the fixed-depth inverse

**Lemma B.** Fix k ≥ 1 and L. On the infinite lattice, S_k has a two-sided inverse with |S_k^{-1}(a, a')| ≤ C e^{−m|a − a'|}, for some C, m > 0 that depend on k and L. Here a, a' are level-0 bonds or level-k bonds, placed by their positions in level-0 units. On a torus with N ≥ N_0 final blocks per direction, S_{k,N} = Per S_k is invertible and S_{k,N}^{-1} = Per(S_k^{-1}). In particular R_{0,k}, R_k and the multiplier response have exponentially decaying kernels, covariant under level-k translations, and their torus versions are periodisations.

Proof.

(i) *Bloch fibres.* S_k has finite range and commutes with translations by L^k Z^4 (level-0 units). For θ ∈ R^4 its fibre S_k(θ) acts on θ-Bloch fields: fields with w(b + L^k e) = e^{iθ·e} w(b), on level-0 bonds and on level-k bonds. The fibre is a finite matrix, over one level-k cell. Its entries are trigonometric polynomials in θ.

(ii) *Q_{0,k}(θ) is onto.* Let J_j put a level-j bond value on every level-(j−1) link that crosses the corresponding block face, and zero on all other links. Then Q_j J_j = 1 (prefactor.md Section 3: the internal contours vanish and each straight path crosses the face once). J_j commutes with translations, so Q_{0,k} J_1 ⋯ J_k = 1 on every fibre.

(iii) *Δ̃_k(θ) > 0 on ker Q_{0,k}(θ).* Δ̃_k(θ) = Σ_i B_i(θ)^* B_i(θ), with B_i ∈ {d, τ_j Q_{0,j}}. Suppose ⟨a, Δ̃_k(θ)a⟩ = 0 and Q_{0,k}a = 0. Then da = 0 and τ_j Q_{0,j} a = 0 for all j, on one cell and hence everywhere. A closed bounded 1-form on Z^4 is a gradient, a = dχ, with χ(x) the path sum from 0. For a gradient, every contour mean and every average is a difference of χ: τ_0(dχ)(x) = χ(x) − χ(y(x)), and Q_{0,j}(dχ) = d_j(r_jχ), where r_jχ is χ at the level-j sites. So τ_0 = 0 makes χ constant on each level-1 block. Next τ_1 = 0 makes r_1χ constant on each level-2 block, and so on up to level k. Then Q_{0,k}dχ = d_k(r_kχ) = 0 makes r_kχ constant. Going back down the levels, χ is constant, so a = 0.

(iv) *S_k(θ) is invertible for real θ.* Let (a, λ) be a null vector. Then Q_{0,k}a = 0 and ⟨a, Δ̃_k a⟩ = −⟨Q_{0,k}a, λ⟩ = 0, so a = 0 by (iii). Then Q_{0,k}^*λ = 0, and λ = 0 by (ii).

(v) *Decay.* det S_k(θ) is a trigonometric polynomial with no zero on the compact real torus. So it has no zero on a strip |Im θ| ≤ δ, and ‖S_k(θ)^{-1}‖ ≤ C there. The kernel of S_k^{-1} between level-k cells c, c' is (2π)^{-4} ∫ S_k(θ)^{-1} e^{iθ·(c − c')} dθ. Shift each θ_μ by iδ sgn(c − c')_μ; periodicity in Re θ permits this. Thus |S_k^{-1}(c, c')| ≤ C e^{−δ|c − c'|_1}. The identities S_k S_k^{-1} = S_k^{-1} S_k = 1 hold on each fibre.

(vi) *Torus.* For N above the range of S_k, S_{k,N} = Per S_k. Absolute convergence gives S_{k,N} Per(S_k^{-1}) = Per(S_k S_k^{-1}) = 1, and the same on the other side.

(vii) *Polynomial growth.* If f grows at most polynomially, then w := S_k^{-1} f is defined by absolutely convergent sums and solves S_k w = f (Fubini: finite range against exponential decay). If w grows at most polynomially and S_k w = 0, then w = S_k^{-1}(S_k w) = 0. ∎

## 4. Lemma A: the actual response reproduces affine fields

**Lemma A.** Let ℓ be a level-k affine bond field, ℓ_ν(X̃) = c_ν + Σ_κ C_{νκ} X̃_κ in level-k midpoint coordinates. Let ℓ_f be the level-0 affine field ℓ_{f,μ}(x̃) = L^{−k}c_μ + L^{−2k} Σ_κ C_{μκ} x̃_κ. Then R_{0,k}ℓ = ℓ_f + dψ, with ψ polynomially bounded, and the multiplier response to ℓ is zero. Consequently:

- (R-ii) d(R_k ℓ) is a constant 2-form on the level-(k−1) lattice, equal to L^{−2} times the level-k curl of ℓ.
- (R-i) For a constant field c, the cell average of R_k c is c/L: L^{−4} Σ_{x∈C} (R_k c)_μ(x̃) = c_μ/L, where C is a set of L^4 level-(k−1) sites representing Z^4/LZ^4.

Proof.

(a) *One step.* For a level-(j−1) field w and a level-j bond c = (c_−, μ), linearising (R3) at 1 gives

Q_j w(c) = Q_j^{path} w(c) + Θ_w(c_−) − Θ_w(c_+),  Q_j^{path} w(c) := L^{−4} Σ_{x∈B(c_−)} Σ_{s=0}^{L−1} w_μ(x + s e_μ),

with Θ_w(y) := L^{−4} Σ_{x∈B(y)} τ_y(w)(x). The straight transport U[c] cancels at first order. The contour terms from x' to c_+ sum, over x' ∈ B(c_+) = B(c_−) + L e_μ, to −L^4 Θ_w(c_+). (This is P1 Lemma 3.1, re-derived.) Also Q_j(dχ) = d_j(rχ) for every site function χ, because every path from c_− to c_+ sums dχ to χ(c_+) − χ(c_−).

(b) *Affine to affine.* Let w_μ(x̃) = a_μ + Σ_κ C_{μκ} x̃_κ in level-(j−1) midpoint coordinates. Then Σ_{s<L} w_μ(x + s e_μ + e_μ/2) = L a_μ + L Σ_κ C_{μκ} x_κ + C_{μμ} L²/2. The mean of x over the centred block B(c_−) is c_−, since L is odd. So Q_j^{path} w(c) = L w_μ(c_− + (L/2)e_μ), which is L times w at the midpoint of c. In level-j coordinates, where that midpoint sits at L X̃, this is the level-j affine field with constant L a and slope L² C. Hence Q_j(affine + gradient) = affine + gradient, and by induction Q_{0,j} maps ℓ_f to the level-j affine field with constant L^{j−k}c and slope L^{2(j−k)}C, plus a level-j gradient.

(c) *An affine solution.* By (b) with j = k, Q_{0,k} ℓ_f = ℓ + d_k φ for a polynomially bounded φ. Define a site function χ level by level, from the top down. At level-k sites put χ := −φ. For j = k−1, …, 0, at each level-j site x that is not a level-(j+1) site, put χ(x) := χ(y(x)) − τ_j(Q_{0,j}ℓ_f)(x), where y(x) is the node of its level-j block (already assigned). Put a_1 := ℓ_f + dχ. Since Q_{0,j}(dχ) = d_j(r_jχ) and τ_j(d_j r_jχ)(x) = χ(x) − χ(y(x)), we get Q_{0,k}a_1 = ℓ + d_kφ + d_k(r_kχ) = ℓ, and τ_j Q_{0,j} a_1 = 0 for every j. χ is polynomially bounded, because φ and τ_j(Q_{0,j}ℓ_f) are. Finally da_1 = dℓ_f is a constant 2-form, so d^*da_1 = 0. Thus Δ̃_k a_1 = 0 and S_k(a_1, 0) = (0, ℓ).

(d) *Uniqueness.* S_k^{-1}(0, ℓ) is polynomially bounded and solves the same equation (Lemma B (vii)). So R_{0,k}ℓ = a_1 and the multiplier response is 0.

(e) *(R-ii).* By (2.1), R_k ℓ = Q_{0,k−1} a_1, the level-(k−1) affine field with slope L^{2(k−1)} L^{−2k} C = L^{−2}C, plus a gradient, by (b). Its curl is constant and equals L^{−2} times the curl of ℓ.

(f) *(R-i).* For a constant c, R_k c is L-periodic on the level-(k−1) lattice, by covariance, and Q_k(R_k c) = Q_{0,k} R_{0,k} c = c. For an L-periodic level-(k−1) field w, Θ_w takes the same value at all level-k nodes, so Q_k w = Q_k^{path} w. For fixed transverse coordinates x_⊥, Σ_{s<L} w_μ(x + s e_μ) is the sum over a full period of the line, whatever x_μ is. So Σ_{x∈B} Σ_{s<L} w_μ(x + s e_μ) = L Σ_{x∈C} w_μ(x), and Q_k w = L times the cell average of w_μ. Hence the cell average of R_k c is c/L. ∎

*Remark.* (R-i) fixes the field units ("two form scalings" of RF11a); if it failed with factor α in place of 1/L, b would be multiplied by (αL)². (R-ii) is what removes the aliased modes at second order; a response with a periodic non-gradient part of order |K| would change b.

