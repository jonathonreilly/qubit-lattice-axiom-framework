lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T02:05Z

# prefactor-loc: the substitution step of rank 9 is exact (queue row 158)

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session, pinned at ef3c72aa2 (branch `claude/ym4d-hard-route`). Same-provider text, not yet checked by the other model; not an audit; grants no status. Sources: `library/prefactor.md` (Codex); the Sussman–Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched once by URL into a private scratch folder (SHA-256 `d7f77d4d…b4d6f`, the same file as `sa-map.md`), not copied here, SA nnnn = its lines (read: R3 at 5631–5651, B3 at 3986–4001, PH1–PH19 at 12890–13300, RF8–RF13 at 20300–20500, the determinant section 21064–21452); `parts/hard-core--mapped.md` Text 3 (P1); `gates/p1-gate-2f2ec0f89.md`; `library/route-compare-2.md` Sections 5.3, 9; Balaban CMP 109 and CMP 119 OCR in `~/ym4d-papers/` (only to confirm prefactor.md's citations). No numeric job was run; no step rests on a computation. No subagent.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for B3, RF8–RF13, PH1–PH19 and the R3 map; the requirement proved in Section 6 below is their RF11a. T. Balaban for the averaging map (CMP 109 (0.12)) and the gauge insertion (CMP 109 (0.14)–(0.16)). Codex for `library/prefactor.md`, whose identities (6), (12), (13) this note reads.

## Result

1. **Check.** `library/prefactor.md` (Codex): checked line by line by Claude, first failing step none. Four non-breaking notes (Section 1).
2. **Theorem S (proved by Claude, by hand; not yet checked by the other model).** At the trivial background and at every fixed depth, background substitution preserves the bulk coefficient exactly: π̂^{F∘p_k}(K) = L²π̂^F(K/L) + O(|K|³) for F = Ψ_{k-1}, so b[Ψ_{k-1}∘p_k] = b[Ψ_{k-1}] with zero error. This is the outline's RF11a second formula, proved for the actual R3 average, contour gauge and Wilson action.
3. **Corollary T.** For every k ≥ 1, in the bulk (infinite volume, fixed depth): Σ_{l≤k} b_l^0 = b[Ψ_k] exactly, where b_l^0 is the PH18 coefficient of the step-l Gaussian logarithm Φ_l read at level l. Any localised family N^(l) as in RF8 (with its decay, (PH5) and a companion) has b(N^(l)) = b_l^0. The error that row 158 asked to bound is identically zero, so it is summable and uniform in depth and volume. No fall-back to the massive trace route is needed for this step.
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
- N3 (Section 3, "three final blocks so each block is contractible"). Wording only. Blocks are cubes, so contractibility of a block is not the operative reason. The argument needs the blocks, and the loops through adjacent blocks that it uses, not to wrap the torus; three blocks per direction ensure this.
- N4 ((13) on a torus). There, b_h is a contraction of a finite Hessian and needs a lift convention for displacements. B3 reads the bulk coefficient, and Sections 2–7 below supply it.

## 2. Setting and the bulk coefficient

Everything below is at the trivial background U = 1 and at a fixed depth k. No constant is claimed uniform in k.

**Lattices.** L is odd. The level-j lattice, in level-j units, is Z^4; in level-0 units its sites are L^j Z^4. A bond (x, μ) runs from x to x + e_μ, with midpoint x̃ = x + e_μ/2. Level-j blocks are centred at level-(j+1) sites (the nodes).

**Colour.** At U = 1 every linear map below acts in the same way on each colour component, and every Hessian kernel is δ^{ab} times one kernel (PH6). So colour is suppressed: fields are real or complex valued.

**Linear objects.** Q_j is the linearisation at 1 of the one-step R3 map M_{j-1,j}, from level j−1 to level j; Q_{0,j} := Q_j ⋯ Q_1 and Q_{0,0} := 1. τ_j is the linearised contour mean of R3 at level j: for a level-j site x that is not a node, (τ_j w)(x) is the mean, over the R3 contour family from the node y(x) of its block to x, of the path sums of w. Then D²G_{j,j+1}(1) = τ_j^*τ_j. Put

Δ̃_k := d^*d + Σ_{j=0}^{k-1} Q_{0,j}^* τ_j^* τ_j Q_{0,j},  S_k := [[Δ̃_k, Q_{0,k}^*], [Q_{0,k}, 0]].

Δ̃_k is the Hessian at 1 of S̃_k := S + Σ_{j<k} G_{j,j+1}∘M_{0,j}; S_k is the k-fold saddle operator at 1.

**Branches and responses.** u_{0,k}(z) is the k-fold augmented critical branch (prefactor.md Section 3 with k levels), with R_{0,k} := Du_{0,k}(1). p_k(z) is the level-(k−1) critical field at level-k datum z, with R_k := Dp_k(1), a map from level-k fields to level-(k−1) fields.

**Gaussian logarithms.** On a torus, Ψ_k is the normalised k-fold constrained Gaussian logarithm, log G(T_{0,k}, A_{0,k}) minus its value at 1. Here T_{0,k} is the constrained Hessian of S̃_k at u_{0,k}(z), and A_{0,k} = DM_{0,k} there. Ψ_0 := 0. Φ_l is the step-l Gaussian logarithm read at level l, as in prefactor.md: log G(T_l, B_l) normalised at 1, with T_l = S_{l-1}'' + G_{l-1,l}'' − μ·M_{l-1,l}'' at p_l(v).

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
- (R-i) For a constant field c, the cell average of R_k c is c/L: L^{−4} Σ_{x∈Λ_L} (R_k c)_μ(x̃) = c_μ/L, where Λ_L := {0, …, L−1}^4 is a set of level-(k−1) sites representing Z^4/LZ^4.

Proof.

(a) *One step.* For a level-(j−1) field w and a level-j bond c = (c_−, μ), linearising (R3) at 1 gives

Q_j w(c) = Q_j^{path} w(c) + Θ_w(c_−) − Θ_w(c_+),  Q_j^{path} w(c) := L^{−4} Σ_{x∈B(c_−)} Σ_{s=0}^{L−1} w_μ(x + s e_μ),

with Θ_w(y) := L^{−4} Σ_{x∈B(y)} τ_y(w)(x). The straight transport U[c] cancels at first order. The contour terms from x' to c_+ sum, over x' ∈ B(c_+) = B(c_−) + L e_μ, to −L^4 Θ_w(c_+). (This is P1 Lemma 3.1, re-derived.) Also Q_j(dχ) = d_j(rχ) for every site function χ, because every path from c_− to c_+ sums dχ to χ(c_+) − χ(c_−).

(b) *Affine to affine.* Let w_μ(x̃) = a_μ + Σ_κ C_{μκ} x̃_κ in level-(j−1) midpoint coordinates. Then Σ_{s<L} w_μ(x + s e_μ + e_μ/2) = L a_μ + L Σ_κ C_{μκ} x_κ + C_{μμ} L²/2. The mean of x over the centred block B(c_−) is c_−, since L is odd. So Q_j^{path} w(c) = L w_μ(c_− + (L/2)e_μ), which is L times w at the midpoint of c. In level-j coordinates, where that midpoint sits at L X̃, this is the level-j affine field with constant L a and slope L² C. Hence Q_j(affine + gradient) = affine + gradient, and by induction Q_{0,j} maps ℓ_f to the level-j affine field with constant L^{j−k}c and slope L^{2(j−k)}C, plus a level-j gradient.

(c) *An affine solution.* By (b) with j = k, Q_{0,k} ℓ_f = ℓ + d_k φ for a polynomially bounded φ. Define a site function χ level by level, from the top down. At level-k sites put χ := −φ. For j = k−1, …, 0, at each level-j site x that is not a level-(j+1) site, put χ(x) := χ(y(x)) − τ_j(Q_{0,j}ℓ_f)(x), where y(x) is the node of its level-j block (already assigned). Put a_1 := ℓ_f + dχ. Since Q_{0,j}(dχ) = d_j(r_jχ) and τ_j(d_j r_jχ)(x) = χ(x) − χ(y(x)), we get Q_{0,k}a_1 = ℓ + d_kφ + d_k(r_kχ) = ℓ, and τ_j Q_{0,j} a_1 = 0 for every j. χ is polynomially bounded, because φ and τ_j(Q_{0,j}ℓ_f) are. Finally da_1 = dℓ_f is a constant 2-form, so d^*da_1 = 0. Thus Δ̃_k a_1 = 0 and S_k(a_1, 0) = (0, ℓ).

(d) *Uniqueness.* S_k^{-1}(0, ℓ) is polynomially bounded and solves the same equation (Lemma B (vii)). So R_{0,k}ℓ = a_1 and the multiplier response is 0.

(e) *(R-ii).* By (2.1), R_k ℓ = Q_{0,k−1} a_1, the level-(k−1) affine field with slope L^{2(k−1)} L^{−2k} C = L^{−2}C, plus a gradient, by (b). Its curl is constant and equals L^{−2} times the curl of ℓ.

(f) *(R-i).* For a constant c, R_k c is L-periodic on the level-(k−1) lattice, by covariance, and Q_k(R_k c) = Q_{0,k} R_{0,k} c = c. For an L-periodic level-(k−1) field w, Θ_w takes the same value at all level-k nodes, so Q_k w = Q_k^{path} w. For fixed transverse coordinates x_⊥, Σ_{s<L} w_μ(x + s e_μ) is the sum over a full period of the line, whatever x_μ is. So Σ_{x∈B} Σ_{s<L} w_μ(x + s e_μ) = L Σ_{x∈Λ_L} w_μ(x), and Q_k w = L times the cell average of w_μ. Hence the cell average of R_k c is c/L. ∎

*Remark.* (R-i) fixes the field units ("two form scalings" of RF11a); if it failed with factor α in place of 1/L, b would be multiplied by (αL)². (R-ii) is what removes the aliased modes at second order; a response with a periodic non-gradient part of order |K| would change b.

## 5. Lemma D: bulk Hessian kernels at fixed depth

**Lemma D.** Fix l ≥ 1 and L.

- (a) DΨ_{l,N}(1) = 0 on every admissible torus.
- (b) There is a kernel H_l on level-l bonds, invariant under level-l translations, with |H_l(b, b')| ≤ C e^{−m|b̃ − b̃'|}, such that D²Ψ_{l,N}(1)(b, b') = H_l(b, b') + O(e^{−mN}) for fixed lifts b, b' as N → ∞.
- (c) H_l is symmetric. It annihilates gradients of polynomially bounded site functions: Σ_{b'} H_l(b, b')(dχ)(b') = 0. It is covariant under the hypercubic group, reflections included, fixing a site.
- (d) The same holds for Ψ_{l−1}∘p_l, with kernel R_l^T H_{l−1} R_l, and for Φ_l, with kernel H_{Φ_l} := H_l − R_l^T H_{l−1} R_l (H_0 := 0).

The constants C, m depend on l and L. Nothing below needs them uniform in l.

Proof.

(a) Ψ(g v g^{−1}) = Ψ(v) for constant g, and su(2) has no Ad-invariant vector (as for (13)).

(b) Write K(v) := 𝕊(T_{0,l}(v), A_{0,l}(v)) in right-trivialised coordinates, so Ψ_{l,N} = −½ log|det K| + const. The entries of K(v) are analytic functions of the branch (u_{0,l}(v), λ(v)) and of v near 1. Each entry depends only on these fields within a distance r(l, L) of its two bonds, because S, each G_{j,j+1}∘M_{0,j} and M_{0,l} have finite range at fixed depth. Also K(1) = S_{l,N}. Polarising (14) of prefactor.md,

D²Ψ_{l,N}(1)[δ_b, δ_{b'}] = −½ Tr(K^{−1}K_{bb'}) + ½ Tr(K^{−1}K_b K^{−1}K_{b'}),  (5.1)

with K_b := ∂_b K(1) and K_{bb'} := ∂_b∂_{b'} K(1). The branch derivatives solve S_l(Du, Dλ)[δ_b] = (0, δ_b) and S_l(D²u, D²λ)[δ_b, δ_{b'}] = s_{bb'}, where s_{bb'} is a finite-range quadratic vertex applied to the first derivatives. By Lemma B, |Du[δ_b](a)| ≤ C e^{−m|a−b|}. Hence |s_{bb'}(a)| ≤ C e^{−m(|a−b| + |a−b'|)}. Convolving with S_l^{−1} and using |a−c| + |c−b| + |c−b'| ≥ ¼(|a−b| + |b−b'|) + ½|a−c| gives |D²u[δ_b, δ_{b'}](a)| ≤ C e^{−(m/4)(|a−b| + |b−b'|)}. So, for some m' > 0,

|K_b(a, a')| ≤ C e^{−m'(|a−b| + |a'−b|)},  |K_{bb'}(a, a')| ≤ C e^{−m'(|a−b| + |a'−b| + |b−b'|)}.

Use Σ_a e^{−m(|x−a| + |a−y|)} ≤ C_m e^{−m|x−y|/2}. Then both traces in (5.1) converge absolutely on the infinite lattice and are O(e^{−m''|b−b'|}). In the second trace the chain b → a → a' → b' has length at least |b − b'|. Define H_l(b, b') by (5.1) on the infinite lattice. On the torus each factor is the periodisation of its infinite-volume version, up to terms in which some factor joins points at torus distance at least N/2 (Lemma B (vi)). These terms are O(e^{−mN}).

(c) *Symmetry:* mixed derivatives commute.

*Gradients.* Ψ_{l,N} is invariant under level-l gauge transformations h near 1. Let h̃(x) := h(Y(x)), with Y(x) the level-l node of the level-l block that contains the fine site x. Then:
- S is invariant.
- Each M_{0,j}, j ≤ l, is covariant: M_{0,j}(U^{h̃}) = M_{0,j}(U)^{h̃_j}, where h̃_j is h̃ at the level-j sites.
- Each G_{j,j+1}∘M_{0,j}, j < l, is invariant: both ends of each contour mean lie in one level-l block, where h̃ is constant, and w is a class function.
- The constraint datum becomes v^h.

By uniqueness near 1, u_{0,l}(v^h) = u_{0,l}(v)^{h̃}. In right-trivialised coordinates (e^{ia}U)^{h̃} = e^{i Ad_{h̃(b_−)} a} U^{h̃} on each bond b. So T_{0,l} and A_{0,l} are conjugated by orthogonal maps, and |det K| is unchanged. Differentiate Ψ(v^{e^{itχ}}) = Ψ(v) once in t and once in a field direction, and use (a). This gives D²Ψ_{l,N}(1)[dχ, ·] = 0 (PH8, re-derived). In the limit, H_l annihilates dχ for finitely supported χ, and then for polynomially bounded χ by exponential decay (PH9).

*Hypercubic covariance.* The R3 contour family (shortest paths in every coordinate order) is invariant under the hypercubic group fixing a block centre. The blocks are centred, because L is odd. The Wilson action and the gauge terms are invariant. Finally (R3) satisfies M(U)(c̄) = M(U)(c)^{−1} for the reversed bond c̄. Proof: put W_x := U(c_−, x)U([x, x'])U(x', c_+). Reindex the start block B(c_+) of c̄ by x ↦ x − L e_μ. Then the formula for c̄ is exp{L^{−4} Σ_x log(W_x^{−1}U[c])} U[c]^{−1}. Also log(W_x^{−1}U[c]) = −Ad_{U[c]^{−1}} log(W_x U[c]^{−1}). So the formula equals U[c]^{−1} exp{−L^{−4} Σ_x log(W_x U[c]^{−1})} = M(U)(c)^{−1}. Hence a symmetry g of a torus symmetric about a level-l site maps the augmented problem at datum v to the problem at g·v, and Ψ_{l,N}(g·v) = Ψ_{l,N}(v).

(d) *Ψ_{l−1}∘p_l.* By (a) for Ψ_{l−1}, its torus Hessian at 1 is R_{l,N}^T D²Ψ_{l−1,N}(1) R_{l,N}, with R_{l,N} = Per R_l. The limit is R_l^T H_{l−1} R_l, with exponential decay by Lemma B and (b). Gauge invariance and covariance follow from those of Ψ_{l−1}, and from p_l(z^h) = p_l(z)^{h̃_{l−1}}, which is proved as in (c).

*Φ_l.* By (2.1), Φ_l = Ψ_l − Ψ_{l−1}∘p_l. ∎

## 6. Theorem S: substitution preserves the coefficient exactly

**Theorem S.** Let π be a bulk kernel on level-(k−1) bonds with exponential moments. Assume:

- (W) π̂(q) ĝ(q) = 0 on its strip, where ĝ_ν(q) := 2i sin(q_ν/2) is the symbol of the gradient;
- (Sy) π_{μν}(u) = π_{νμ}(−u);
- (Re) covariance under the reflection of one coordinate about a site.

Let R map level-k bond fields to level-(k−1) bond fields, with a kernel that is covariant under level-k translations and decays exponentially, and that satisfies (R-i) and (R-ii) of Lemma A. Let π^c be the bulk kernel of R^T Π R on level-k bonds. Then

π̂^c(K) = L² π̂(K/L) + O(|K|³)  as K → 0.  (6.1)

Hence π^c and π have the same second moments, Σ_U π^c_{μν}(U) U_κ U_λ = Σ_u π_{μν}(u) u_κ u_λ, and in particular b_{μν}[π^c] = b_{μν}[π] for every pair μ ≠ ν.

Proof. Work in level-(k−1) units. Level-k sites sit at L Z^4, and the level-k bond (X, ν) has its midpoint at L(X + e_ν/2).

*Step 1: π̂(q) = O(|q|²).* Differentiate (W) at q = 0, using ĝ(0) = 0, ∂_κ ĝ_ν(0) = i δ_{κν} and ∂_κ∂_λ ĝ(0) = 0. Once: i π̂_{μκ}(0) = 0, so π̂(0) = 0. Twice: ∂_κ π̂_{μλ}(0) + ∂_λ π̂_{μκ}(0) = 0. So the first moment M_{μν,κ} := Σ_u π_{μν}(u) u_κ is antisymmetric in (ν, κ). By (Sy) it is antisymmetric in (μ, ν). So it is totally antisymmetric. Under the reflection of coordinate ρ, a bond field transforms by B_μ(x̃) ↦ s_μ B_μ(r x̃), with s_ρ = −1 and s_μ = 1 otherwise. (Re) gives M_{μν,κ} = s_μ s_ν s_κ M_{μν,κ}. For distinct μ, ν, κ take ρ = κ: then M = −M. So M = 0 and ∇π̂(0) = 0.

*Step 2: the composite symbol.* Fix ν and K in a small complex ball. Let w^{K,ν} := R(e_ν e^{iK·X̃}), the image of the level-k plane wave in direction ν. By covariance, w^{K,ν}(x̃ + L e) = e^{iK·e} w^{K,ν}(x̃) for e ∈ Z^4. Put N := {−(L−1)/2, …, (L−1)/2}^4, k_n := (K + 2πn)/L and C := {0, …, L−1}^4. Then

w^{K,ν}_μ(x̃) = Σ_{n∈N} ρ_{μν}(K, n) e^{i k_n·x̃},  ρ_{μν}(K, n) = L^{−4} Σ_{x∈C} w^{K,ν}_μ(x̃) e^{−i k_n·x̃}.

The ρ are analytic in K, by the exponential decay of R. Put τ(q) := Σ_x R(x̃; 0) e^{iq·x̃}, the kernel to the level-k bonds at X = 0. Covariance, R(x̃ + L X; X) = R(x̃; 0), gives two facts. First, ρ(K, n) = L^{−4} τ(−k_n) Ph(K), with Ph(K) := diag(e^{iK_ν/2}). Second, R^T maps a fine plane wave α e^{i k_n·x̃} to e^{iK·X} τ(k_n)^T α, since e^{i k_n·L X} = e^{iK·X}. Apply R^T Π R to the plane wave and compare with π̂^c(K) e^{iK·X̃}. Since −k_n(K) = k_{−n}(−K), we have τ(k_n)^T = L^4 Ph(K) ρ(−K, −n)^T, and the phases cancel:

π̂^c(K) = L^4 Σ_{n∈N} ρ(−K, −n)^T π̂(k_n) ρ(K, n).  (6.2)

For real K, ρ(−K, −n)^T = ρ(K, n)^†.

*Step 3: the term n = 0.* ρ_{μν}(0, 0) is the cell average of (R e_ν)_μ, which is δ_{μν}/L by (R-i). So ρ(±K, 0) = L^{−1} + O(|K|). By Step 1, π̂(K/L) = O(|K|²). So the n = 0 term of (6.2) is L^4 · L^{−2} π̂(K/L) + O(|K|³).

*Step 4: the terms n ≠ 0.* For a fine plane wave α e^{iq·x̃}, the curl on the plaquette (x; μ, λ), with centre p̃ = x + (e_μ + e_λ)/2, is

(ĝ_μ(q) α_λ − ĝ_λ(q) α_μ) e^{iq·p̃} =: (ĝ(q) ∧ α)_{μλ} e^{iq·p̃}.

So the curl Ω^K := d w^{K,ν} has modes ĝ(k_n) ∧ ρ_{·ν}(K, n), and ĝ(k_n) ∧ ρ_{·ν}(K, n) = L^{−4} Σ_{x∈C} Ω^K(p̃) e^{−i k_n·p̃}. Expand in K at fixed p, uniformly over the bounded set p ∈ C:

Ω^K = d(R e_ν) + i Σ_κ K_κ d(R(X̃_κ e_ν)) + O(|K|²).

Here ∂_{K_κ} w^{K,ν} = i R(X̃_κ e_ν) at K = 0, by differentiation under the absolutely convergent sum. By (R-ii) both curls are constant 2-forms, ω_0 and ω_κ. Moreover ω_0 = 0: R e_ν is L-periodic, and the sum of the curl of a periodic field over a period cell telescopes to zero. Hence

ĝ(k_n) ∧ ρ_{·ν}(K, n) = i Σ_κ K_κ ω_κ · L^{−4} Σ_{x∈C} e^{−i k_n·p̃} + O(|K|²).

For n ≠ 0 the last sum is zero at K = 0 (a nontrivial character of Z^4/LZ^4, times a constant phase) and analytic, so it is O(|K|). Therefore ĝ(k_n) ∧ ρ_{·ν}(K, n) = O(|K|²).

Now pick α with n_α ≠ 0. Then |π n_α / L| ∈ [π/L, π/2), so ĝ_α(k_n) = 2i sin((K_α + 2π n_α)/(2L)) is analytic and nonzero near K = 0. Put φ(K) := ρ_{αν}(K, n)/ĝ_α(k_n). For each λ, ρ_{λν} − ĝ_λ φ = (ĝ ∧ ρ)_{αλ}/ĝ_α = O(|K|²). So ρ_{·ν}(K, n) = ĝ(k_n) φ(K) + O(|K|²). The same holds for ρ(−K, −n), with ĝ(k_{−n}(−K)) = −ĝ(k_n(K)). By (W) at −q and (Sy), π̂(q)^T = π̂(−q) and ĝ(q)^T π̂(q) = 0. So the gradient parts drop out on both sides, and the n-th term of (6.2) is O(|K|²) · π̂(k_n) · O(|K|²) = O(|K|⁴).

*Step 5.* Adding the terms, π̂^c(K) = L² π̂(K/L) + O(|K|³). The second-order Taylor polynomial of L² π̂(K/L) at 0 is that of π̂, evaluated at K. ∎

## 7. Corollary T: B3's bulk coefficient sequence telescopes exactly

**Corollary T.** For every k ≥ 1,

Σ_{l=1}^{k} b_l^0 = b[Ψ_k]  and  b_l^0 = b[Ψ_l] − b[Ψ_{l−1}],

exactly. The same holds for every pair μ ≠ ν and for the whole second-moment tensor.

Proof. Fix l ≥ 1. By (2.1) and Lemma D (a), on each torus D²Ψ_{l,N}(1) = D²Φ_{l,N}(1) + R_{l,N}^T D²Ψ_{l−1,N}(1) R_{l,N}. In the limit, H_l = H_{Φ_l} + R_l^T H_{l−1} R_l (Lemma D (d)). The coefficient b is linear in the kernel. Apply Theorem S with π = H_{l−1} and R = R_l. Its hypotheses (W), (Sy), (Re) hold by Lemma D (c); covariance and decay of R_l hold by Lemma B; (R-i) and (R-ii) hold by Lemma A with k = l. (For l = 1, H_0 = 0 and there is nothing to prove.) So b[R_l^T H_{l−1} R_l] = b[Ψ_{l−1}], and b_l^0 = b[H_{Φ_l}] = b[Ψ_l] − b[Ψ_{l−1}]. Sum over l ≤ k, with Ψ_0 = 0. ∎

**Remarks.**

1. *The localised family.* RF8 defines b_l^0 as b(N^{(l)}) for its localised family. Suppose N^{(l)} sums to Φ_l on every admissible torus, agrees with a companion family on Z^4 for nonwrapping polymers, and has RF8's decay and (PH5) with constants independent of the torus. Then the sum over base points of its pointed Hessians is D²Φ_{l,N}(1) on each torus, and the wrapping and torus–companion differences at fixed b, b' tend to zero. So its PH13 bulk kernel is H_{Φ_l}, and b(N^{(l)}) = b_l^0. B3's sequence therefore does not depend on the localisation. Corollary T itself does not use RF8.
2. *Why the requested error is zero.* prefactor.md Section 6 asked for a summable bound on the substitution error b[R_k^T H_{k−1} R_k] − b[H_{k−1}]. Theorem S shows that this error is zero for every k. Only fixed-depth decay is used (Lemmas B, D), with rates that may degenerate as k grows; they are never summed over k. The ε + t² example of prefactor.md (14) concerns uniform derivative bounds, and these do not enter.
3. *RF11a.* (6.1) with F = Ψ_{k−1} is RF11a's second formula. The coefficient needs no "uniform analytic control of the aliased modes": Step 4 shows the aliased terms are O(|K|⁴) at each fixed depth. A version of the O(|K|³) remainder uniform in k is not proved here.
4. *Units.* (R-i) carries RF11a's two form scalings L^{−1}L^{−1}, and the volume ratio L^4 is the prefactor in (6.2).

## 8. Scope, and what stays open

**Proved here, by hand, not yet checked by the other model.** Lemmas B, A, D, Theorem S and Corollary T, as implications from these inputs only: the Wilson action; the R3 average (SA 5631–5651 = CMP 109 (0.12)); the contour gauge insertion (CMP 109 (0.14)–(0.16)); prefactor.md (5), (6), (12), (14), checked in Section 1; and the outline's definition of b as the PH18 second moment. The (2.1) induction re-uses prefactor.md Section 4 verbatim. No literature lemma is cited without its proof here.

**What this does not show.**

- *The value.* Corollary T reduces B3's Gaussian part to one number per depth: b[Ψ_k], the coefficient of the k-fold constrained Gaussian logarithm. The bound |b[Ψ_k] − k c_0| ≤ c_2, uniform in k, is open. By Corollary T it is equivalent to the partial-sum form of RF10's first clause, which B3 accepts as a "stated summable substitute". It is the target of the outline's massive trace route: the change to the covariant background gauge (SA 21095–21111), the current cancellation RF12b–RF12c (SA 21162–21322), and the mass comparison RF13 (SA 21325–21452). That comparison has two named open checks: the mixed energy bounds for the actual average and constraint jets (SA 21325–21356), and the matching of the vector numerators to the grouped magnetic remainder (SA 21378–21430). P1's constant-flux route is the alternative; the P1 gate found its bound (E) WRONG and its uniform symbol and alias bounds open. Either route must compute b of the same Ψ_k: the contour-gauge Gaussian here, or RF12's covariant-gauge form with the gauge change proved along the branch.
- *Geometric convergence.* RF10's second clause, |b_{l+1}^0 − b_l^0| ≤ C_α L^{−αl} (the RF14 route), is not touched. It is needed only for B3's strong form |b_j^0 − c_0| ≤ C L^{−σj}, not for the partial-sum substitute.
- *Nonlinear parts and localisation.* B3's f_j and q_j, and RF8's uniform localisation of N^{(l)}, are not touched. Remark 1 of Section 7 shows that RF8 is not needed for the coefficient identity.
- *Uniformity.* The constants of Lemmas B and D depend on the depth. The identity is exact, so this costs nothing. A torus coefficient, if a consumer reads one, differs from the bulk coefficient by O(e^{−m_k N}), with m_k not uniform in k; B3 reads the bulk coefficient.

**For the lead.** Row 158 is closed in the stronger form: the substitution and localisation error is zero, uniformly in depth and volume, so the hybrid coefficient lane of `library/route-compare-2.md` Section 9 item 1 is real. Rank 9 now stops at the value b[Ψ_k] = k c_0 + O(1). Its first statement for a lane is RF13's comparison for this Ψ_k. Start from Lemma B's Bloch fibres and the bounded-conjugation strip, and prove the mixed energy bounds of SA 21325–21356 for the actual R3 jets, uniformly in k. Check RF12c in the same lane; like Theorem S, it is exact at fixed k and uses only Lemma D's fixed-depth moments. A failure there would send rank 9 back to P1's constant-flux route, with its gate's repairs.

RESULT: prefactor.md (Codex) checked line by line by Claude, first failing step none (four non-breaking notes). Proved by Claude, not yet checked: Theorem S, π̂^{Ψ_{k−1}∘p_k}(K) = L²π̂^{Ψ_{k−1}}(K/L) + O(|K|³) at every fixed depth for the actual R3 average, contour gauge and Wilson action (RF11a's second formula), hence Corollary T, Σ_{l≤k} b_l^0 = b[Ψ_k] exactly, so the substitution error that row 158 asked to bound is zero, uniformly in depth and volume, and any RF8 localisation gives the same b_l^0. Open: the value |b[Ψ_k] − k c_0| ≤ c_2 uniformly in k (massive trace route RF12c/RF13 with its mixed energy bounds, or P1), RF10's second clause, and B3's nonlinear parts.
