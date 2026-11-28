lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T10:27Z

# B2: the pointed quadratic cancellation (20) and the potential bound (19)

Queue row 194, `b2-extract`. Pinned at commit 13424f9e2 on branch `claude/ym4d-hard-route`.
Written by Claude (Opus 5.5, max effort) on the Mac mini worker, 2026-11-03. Research-stage working state; no status.

**Summary.**
- *Check.* `b4-step.md` Section 10 (Codex) was checked line by line by Claude; first failing step none (Section 1).
- *Theorem P (Section 3).* The outline's B2 rebuilt, proved by Claude and not yet checked by the other model. (20) holds at a base point z exactly when the prescribed coefficient equals the pointed second moment b_z. Gauge invariance, absolute moments, the hypercube about z and the affine response suffice. b_z equals the bulk extractor for every z under unit-translation covariance.
- *Inputs.* The actual class supplies every input at fixed j (Section 4) except (R14): covariance of each old member's pointed totals under the hypercube about every base point and under unit translations. That is the first failing input. Examples 1-3 show it cannot be dropped (Section 5). Lemma R reduces it to (TI), invariance of the member's total (Section 6).
- *(19).* (19) follows from (20) and further inputs (Proposition W, Section 7). Besides (20), its first open input is (ER8u) = (ER7), which also stops D1.

Credit: the pointed Hessian argument rebuilt below is the outline's (Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text), `YM4_sketch_500.tex` at `31a47c543775`, Section "The Hessian of a pointed member and its own action counterterm" (SA 12889-13424, PH1-PH23), and Requirement B2 (SA 3936-3981). The underlying mechanism is Balaban's, CMP 109 (1987) Section 4, pp. 281-285: gauge-invariance (Ward-Takahashi) identities (4.7)-(4.15), which remove the linear term (4.14) and constrain the quadratic one; the exponential smallness of terms localised away from the cube (4.5); and the Hölder bound on the local derivative expansion (4.16)-(4.18). (3.34)-(3.36) give the analyticity domain. I read those pages in `~/ym4d-papers/cmp109.txt`.

## 1. Check of `b4-step.md` Section 10 (Codex): B1 for the intrinsic gas

Provenance: Claude Opus 5.5, max effort, commit 13424f9e2. One line-by-line reading by one other model; not an audit.

**Verdict: (15)-(18) and Section 10.1 ADVANCE as implications. Checked line by line by Claude, first failing step none.** The inputs are (6) uniformly on the discs abs(s_Delta) < R_s, the intrinsic UM1 bound (14), the full-hull locality and heredity premises with [RT], the identity r(1) r(1)^T = A^{-1} of the adopted symmetric root, and the order of choice of `um-envelope.md` Section 5.

What I redid, step by step, against SA UM12-UM30 (SA 14448-14765):

- *Type budget.* (14) has no constant term, so it is dominated by the UM1 form with a_Y = K_GA delta(t) and lambda_V <= kappa-bar - 2. Section 9 gives kappa-bar >= lambda + 2, and `um-envelope.md` (8) chooses lambda = lambda_V. So the intrinsic type meets UM1 at the common rate.
- *(13)-type sum.* On abs(zeta_Y) < R_Y, abs(zeta_Y V(Y)) <= W_0 e^{-lambda_0 d_f(Y)} (1 + M^{-4} sum_{b in Y} abs(B(b))^2). Every selected Y has Y^sharp in Z_0^sharp, a subset of Z. The constant part is at most c_f L^4 S_{lambda_0} N (UM10); the quadratic part is summed at each bond first. This needs lambda_0 > kappa_f, which is imposed.
- *(15).* abs(e^w - 1) <= 2 e^{abs(w)} gives the factor 2^r. On the support of the failed-bond factor, abs(b)^2 >= v b-frak^2, because failed bonds are distinct coordinates. So the integrand is at most 2^r e^{C_p W_0 L^4 N} e^{-gamma v b-frak^2 / 2} e^{(rho + gamma/2) abs(b)^2} with rho = C_p W_0 M^{-4}. Then (7) at rho + gamma/2 <= rho_0(K_G), with m <= c_m (LM)^4 N, gives (15) exactly. The two constants agree with `um-envelope.md` (1).
- *(16).* The integral is holomorphic in (zeta, s) by Gaussian domination. It vanishes on each hyperplane zeta_Y = 0, so f / prod zeta_Y is holomorphic. The maximum principle at zeta = 1 on polydiscs of radii tending to R_Y >= 2 gives the factor prod_Y (a/W_0) e^{-(lambda_V - lambda_0) d_f(Y)}. One Cauchy estimate per cube of Z \ Z_0^sharp, on circles of radius tending to R_s - 1 about points of [0, 1], gives (R_s - 1)^{-h}. No factorial occurs, since each parameter is differentiated once.
- *Collar and (17).* Z_0^sharp is in the union of the Y^sharp and the failed-bond collars, because the collar preserves unions. This and UM7 give N <= C_h [r + L^{-1} sum d_f + v + h]. Paying e^{(C_0 + K_*) N} with it leaves prod_Y (2a/W_0) e^Theta e^{-sigma_0 d_f(Y)} times (p e^Theta)^v, since ((R_s - 1)^{-1} e^Theta)^h <= 1. The sum over nonempty selections with collars in Z is at most e^{tau N} - 1, by UM10 and UM11. Then e^x - 1 <= x e^x, N <= e^N and tau <= 1 give tau e^{-(K_* - 2) N} <= tau e^{-Lambda l(Z)}, because (K_* - 2) N = c_l Lambda N >= Lambda l(Z).
- *Tree step and (18).* Fix an edge order. Toggle the smallest edge of the incompatibility graph whose endpoints are joined in G by a path of smaller edges. That edge stays the smallest one with this property, because neither it nor any larger edge occurs in the paths that test the smaller edges. Removing it keeps G connected. So this is a sign-reversing involution, and its fixed points are trees. Hence abs(phi) <= the number of spanning trees. With B_* < 1/(2 c_adj) and w_Z <= tau e^{-(Lambda - mu) l(Z)}, the Kotecky-Preiss criterion holds with root weight #Z and room #Z/2. The depth recursion gives T_Z <= e^{#Z}. A marked cube q, UM28 and this bound give e^{mu l(X)} abs(E(X)) <= tau B_*, which is (18). Scaling the activities by abs(lambda) < 2 keeps the criterion. So exp(sum E) = Xi holds as an identity of analytic functions on that disc, which includes lambda = 1. This proves Xi is not zero.
- *10.1.* Block-diagonal factors with respect to one partition multiply to a block-diagonal matrix. So chi A(s) chi, C, Gamma Gamma^T and D split if A(s) and r(s) do. That is the full-hull premise, and it needs the hull to contain its neighbour layer, so that a corner contact between coarse cubes also meets the zero cubes around that corner. At s = 1, Gamma Gamma^T = A_IO (A^{-1})_OO A_OI = A_IO S^{-1} A_OI, and the block-inverse formula gives D = (A^{-1})_II. The cutoff expansion prod_{b not in Y_0} chi_b = sum_{P_0} (-1)^{abs(P_0)} prod_{b in P_0} (1 - chi_b) is UM2. On a wall component of Z that misses Z_0^sharp, the integrand does not depend on the coordinates there, so the s-derivatives of J[1] = 1 vanish. This is why only connected polymers that contain the selections survive.

Not shown by this check: the premises themselves, the other potential types, and the older-origin bound (19) (Section 11 there). The order of choice needs delta(t) -> 0 and t delta(t)^2 -> infinity together. `um1.md` uses the first; I did not find a line that states the second for the chain's delta(t). It is a condition on that choice, not a defect of Section 10.

## 2. The statement (20) and its inputs

Fix the old level j. Work in level-j (coarse) units on ℤ⁴. The member is the infinite-lattice companion of one old regular member, with no stored colour spectators (SA 5883-5888). Torus terms agree with it on non-wrapping lifts (`h-walk-fix.md` §5 item 6). So the torus version differs only by wrapping domains, whose weight e^{−κ d_j(X)} has d_j(X) of order the torus side.

- A bond b = (x, μ) has midpoint x̃ = x + e_μ/2. The bare spacing is η = L^{−j}.
- B is a finitely supported su(2)-valued coarse bond field. The colour basis t_a is orthonormal for ⟨A, C⟩ = ½ Tr(AC). Complexification is bilinear.
- P_j(B) = (U_j(B), J(U_j(B))) is the actual critical background pair of the datum e^{iB}, with P_j(0) = (1, 0). Its first response is hB = DP_j(0)B = (HB, D_1^*D_1 HB) (SA PH3).
- G is the member. Its pointed total is G_z(P) = Σ_{X∋z} G(X, P, z), and F_z := G_z ∘ P_j.
- K_z^{μν;ab}(x, y) := Σ_{X∋z} D²G(X, (1,0), z)[hδ^a_{x,μ}, hδ^b_{y,ν}] (SA PH4).
- A_z(U) := Σ_{μ<ν} Σ_{p ∈ P_{μν}} h_z(p) A_p(U) is the tent action, with h_z(p) = Π_r (1 − |p_r − z_r|)_+ at the barycentre p of a bare plaquette. A_p is normalised by A(e^{itB}) = (t²/2) Σ_p |∂B(p)|² + O(t³), where ∂B(p) is the oriented sum of B over the boundary of p (SA PH1).
- ℓ is an affine coarse field ℓ_μ(x̃) = a_μ + Σ_κ C_{μκ}(x̃ − z)_κ, with constant curl F_{μν} = C_{νμ} − C_{μν}. The axial choice ℓ_μ(x̃) = Σ_{κ<μ} (x̃ − z)_κ F_{κμ} has curl F. Every D²(·)(0)[ℓ, ℓ] below is the extended Hessian Σ_{x,y} K(x, y) ℓ(x) ℓ(y), which converges absolutely by (Mo). It is not a value of a nonlinear function at an unbounded field.

The statement to prove is (20) of `b4-step.md`:

  D²(F_z − b (A_z ∘ P_j))(0)[ℓ_F, ℓ_F] = 0 for every constant F, with b = b_j(G) the member's prescribed coefficient.

**Inputs, named once.** Each is a property of the actual objects at fixed j, not a convention.

- (D) *Derivatives.* For each X, DG(X, (1,0), z) and D²G(X, (1,0), z) exist. The sums over X ∋ z of the first and second derivatives along hδ_x converge absolutely and normally near 0. For finitely supported B, C, the composite F_z has D²F_z(0)[B, C] = Σ_{x,y} K_z(x, y) B(x) C(y).
- (C) *Colour.* Each G(X, ·, z) is invariant under constant gauge maps, and P_j(Ad_g B) = P_j(B)^g for constant g ∈ SU(2).
- (G) *Gauge.* For finitely supported coarse χ and g_t = e^{itχ}, F_z(B^{g_t}) = F_z(B) for B near 0 and |t| small. Here (U^g)(x, μ) = g(x)^{−1} U(x, μ) g(x + e_μ), and B^g is the coarse logarithm of (e^{iB})^g. It suffices that P_j(B^g) = P_j(B)^{g̃} for a bare gauge map g̃ under which every G(X, ·, z) is invariant.
- (Mo) *Moments.* For some m > 0, C_m(z) := Σ_{μ,ν,a,b} Σ_{x,y} e^{m(|x−z|+|y−z|)} |K_z^{μν;ab}(x, y)| < ∞ (SA PH5).
- (H_z) *Hypercube at z.* F_z(w_z B) = F_z(B) for every signed permutation w, w e_μ = s_μ e_{σ(μ)}, acting about z on bond fields as one-forms: (w_z B)_{σ(μ)}(z + w(x̃ − z)) = s_μ B_μ(x̃).
- (AR) *Affine response.* For each bare bond b in the support of h_z, Σ_x |(Hδ_x)(b)| (1 + |x − z|)² < ∞. The extended response Hℓ := Σ_x (Hδ_x) ℓ(x) of an affine ℓ is, at those bonds, the bare affine potential with the same coefficients plus a bare gradient: (Hℓ)_b = a_μ + Σ_κ C_{μκ}(b̃ − z)_κ + (dψ)_b, in the chart U_b = e^{iηA_b}.
- (Tr) *Translations.* F_{z+e}(τ_e B) = F_z(B) for every unit e, where (τ_e B)(x̃) = B(x̃ − e).

(H_z) for every z together with (Tr) is the outline's (R14) (SA 5889-5898) for this member: covariance of pointed totals under every lattice isometry, including unit translations. SA 7581 makes it "part of the definition of renormalised".

## 3. Theorem P: the pointed cancellation

**Theorem P.** Assume (D), (C), (G), (Mo) and (H_z) at one base point z. Write K_z^{μν}(x, y) := ⅓ Σ_a K_z^{μν;aa}(x, y), and for μ ≠ ν put

  b_z := Σ_{x,y} K_z^{μν}(x, y) (ỹ − x̃)_μ (ỹ − x̃)_ν.

Then:
- (a) b_z does not depend on the pair μ ≠ ν, and (1/2) D²F_z(0)[ℓ, ℓ] = (b_z/2) Σ_{μ<ν} ⟨F_{μν}, F_{μν}⟩ for every affine ℓ with curl F.
- (b) If (AR) holds, (1/2) D²(A_z ∘ P_j)(0)[ℓ, ℓ] = (1/2) Σ_{μ<ν} ⟨F_{μν}, F_{μν}⟩.
- (c) Hence D²(F_z − b (A_z ∘ P_j))(0)[ℓ, ℓ] = (b_z − b) Σ_{μ<ν} ⟨F_{μν}, F_{μν}⟩. So (20) holds at z for every F if and only if b = b_z.
- (d) If (H_z) holds at every z and (Tr) holds, then b_z = b[G] := Σ_u π_{μν}(u) u_μ u_ν for every z, with π_{μν}(u) := Σ_x K_0^{μν}(x̃, x̃ + u). This is the outline's bulk extractor (SA PH13, PH18).

Translation covariance enters only in (d). The outline's proof uses it to name the coefficient through the bulk sum. At one base point, (a)-(c) need only the hypercube about that point. Part (b) uses no symmetry of P_j. This is the outline's argument (SA PH1-PH23), rebuilt with the base point kept fixed. Credit: Sussman-Alpoge; mechanism after Balaban, CMP 109, (3.34)-(3.36).

*Proof.* All rearrangements below are of absolutely convergent sums, by (Mo): every polynomial of degree at most 4 in x − z and y − z is dominated by C e^{m(|x−z|+|y−z|)}.

*Step 1 (first derivative and the kernel).* Fix X. By (C), G(X, (U, J)^g, z) = G(X, (U, J), z) for constant g, and (1, 0)^g = (1, 0). Differentiate at (1, 0) along (Ad_g A, Ad_g J). The linear form DG(X, (1,0), z) is invariant under Ad_g on every local coordinate. Each coordinate carries the adjoint representation of SO(3) on ℂ³, which has no non-zero invariant vector. So DG(X, (1,0), z) = 0. In the chain rule for D²F_z(0), the term Σ_X DG(X, (1,0), z)[D²P_j(0)[B, C]] therefore vanishes, and (D) gives the kernel formula.

*Step 2 (colour).* By (C), D²F_z(0)[Ad_g B, Ad_g C] = D²F_z(0)[B, C]. Fix x, y, μ, ν, and let M_{ab} = K_z^{μν;ab}(x, y). Then R^T M R = M for every R ∈ SO(3), because the adjoint map of SU(2) is onto SO(3). With R = diag(1, −1, −1), M_{12} = M_{13} = M_{21} = M_{31} = 0; the other axis rotations by π remove M_{23}, M_{32}. The cyclic permutation of axes is in SO(3), so M_{11} = M_{22} = M_{33}. Hence K_z^{μν;ab} = δ_{ab} K_z^{μν}. Mixed derivatives commute, so K_z^{μν}(x, y) = K_z^{νμ}(y, x).

*Step 3 (compact Ward identity).* Let Φ(t, B) := B^{g_t}. By (G), F_z(Φ(t, B)) = F_z(B). Differentiate once in t at t = 0 and once in B at 0 along C. This gives D²F_z(0)[∂_tΦ(0, 0), C] + DF_z(0)[∂_B ∂_t Φ(0, 0)[C]] = 0. By Step 1, DF_z(0) = 0. Also ∂_tΦ(0, 0) = dχ, with (dχ)_μ(x) = χ(x + e_μ) − χ(x), because g_t(x)^{−1} g_t(x + e_μ) = 1 + it(dχ)_μ(x) + O(t²). Hence D²F_z(0)[dχ, C] = 0 for finitely supported χ and C.

*Step 4 (polynomial Ward identity).* Let χ be a polynomial of degree q, put χ_R(x) = χ(x) ϑ((x − z)/R) with a fixed smooth ϑ of compact support that equals 1 near 0, and let R ≥ 1. Then dχ_R → dχ pointwise. Moreover |dχ_R(x)| ≤ C_χ (1 + |x − z|)^{max(q−1, 0)}: write dχ_R as [χ(x + e) − χ(x)] ϑ((x + e − z)/R) + χ(x)[ϑ((x + e − z)/R) − ϑ((x − z)/R)]. The second bracket is at most ‖∇ϑ‖_∞/R, and it is non-zero only where |x − z| is comparable with R. Apply Step 3 with C = δ_{y,ν}. Dominated convergence, with (Mo), gives Σ_{x,μ} K_z^{μν}(x, y)(dχ)_μ(x) = 0 for every y, ν. Summing against any polynomial second argument is then legitimate.

*Step 5 (zeroth moments).* Take χ(x) = (x − z)_κ. Then (dχ)_μ = δ_{μκ}, so Step 4 gives Σ_x K_z^{κν}(x, y) = 0 for every κ, y, ν. Step 2 gives Σ_y K_z^{μν}(x, y) = 0. Both hold for each fixed remaining bond and pair of directions.

*Step 6 (the moment tensor at z and its two antisymmetries).* Put T_{μν,κλ} := Σ_{x,y} K_z^{μν}(x, y)(x̃ − z)_κ (ỹ − z)_λ, in midpoint coordinates relative to z. For a symmetric matrix S, let χ(x) = ½ Σ_{α,β} S_{αβ}(x − z)_α (x − z)_β. On a μ-bond, (dχ)_μ(x) = Σ_κ S_{μκ}(x − z)_κ + ½ S_{μμ} = Σ_κ S_{μκ}(x̃ − z)_κ, exactly, because x̃ = x + e_μ/2. Apply Step 4 with the second argument C_ν(y) = (ỹ − z)_λ on ν-bonds only. This gives Σ_{μ,κ} S_{μκ} T_{μν,κλ} = 0 for every symmetric S. Hence T_{μν,κλ} = −T_{κν,μλ}, and in particular T_{μν,μλ} = 0. Step 2 gives T_{μν,κλ} = T_{νμ,λκ}. Combining the two gives T_{μν,κλ} = −T_{μλ,κν}.

*Step 7 (classification at z).* Under w_z, midpoint coordinates relative to z transform linearly, and the midpoint set of direction μ maps onto that of direction σ(μ), since ℤ − ½ = ℤ + ½. By (H_z), K_z^{σ(μ)σ(ν)}(z + w(x̃ − z), z + w(ỹ − z)) s_μ s_ν = K_z^{μν}(x̃, ỹ). So T_{σμ σν, σκ σλ} = s_μ s_ν s_κ s_λ T_{μν,κλ}. A reflection of one coordinate shows that each label occurs an even number of times in a non-zero entry. By Step 6, T = 0 when μ = κ or ν = λ. So the only non-zero entries are T_{μμ,κκ} and T_{μκ,κμ} with μ ≠ κ. Permutations make every T_{μμ,κκ} (μ ≠ κ) equal to one number b'. Step 6 gives T_{μκ,κμ} = −T_{μμ,κκ} = −b'. Hence T_{μν,κλ} = b'(δ_{μν}δ_{κλ} − δ_{μλ}δ_{κν}), for all indices. Full reflections are needed: a proper rotation leaves the alternating tensor ε_{μνκλ}, which satisfies both antisymmetries of Step 6.

*Step 8 (affine jet and the coefficient).* Write ℓ = a + C(x̃ − z). The terms containing a vanish by Step 5. So D²F_z(0)[ℓ, ℓ] = Σ C_{μκ} C_{νλ} T_{μν,κλ}, with the bilinear colour pairing, which is b' Σ_{μ,κ} (⟨C_{μκ}, C_{μκ}⟩ − ⟨C_{μκ}, C_{κμ}⟩) = b' Σ_{μ<ν} ⟨F_{μν}, F_{μν}⟩. Next, (ỹ − x̃) = (ỹ − z) − (x̃ − z). The pure terms vanish by Step 5, so Σ_{x,y} K_z^{μν}(x, y)(ỹ − x̃)_κ (ỹ − x̃)_λ = −T_{μν,κλ} − T_{μν,λκ}. At (κ, λ) = (μ, ν), μ ≠ ν, this is −0 − (−b') = b'. So b' = b_z, which is (a).

*Step 9 (the tent action).* Each A_p has DA_p(1) = 0, so D²(A_z ∘ P_j)(0)[δ_x, δ_y] = D²A_z(1)[Hδ_x, Hδ_y]. By the normalisation of A_p in the chart U_b = e^{iηA_b}, D²A_z(1)[A, A'] = Σ_{μ<ν} Σ_{p∈P_{μν}} h_z(p) η² ⟨∂A(p), ∂A'(p)⟩. The plaquette sum is finite, because h_z has compact support. By the decay clause of (AR), the extended Hessian at ℓ equals Σ_p h_z(p) η² ⟨∂(Hℓ)(p), ∂(Hℓ)(p)⟩. By (AR), Hℓ is affine plus a gradient near z, and ∂(dψ) = 0. For an affine bare potential, the oriented sum over a plaquette of side η in plane μν is exactly η(C_{νμ} − C_{μν}) = ηF_{μν}. So the extended Hessian is Σ_{μ<ν} ⟨F_{μν}, F_{μν}⟩ η⁴ Σ_{p∈P_{μν}} h_z(p).

*Quadrature (SA PH21).* For η = 1/N_0 and each orientation μν, η⁴ Σ_{p∈P_{μν}} h_z(p) = 1. The barycentres of μν-plaquettes have half-mesh shifts in directions μ, ν and none in the other two directions. The factor of h_z in an unshifted direction sums to N_0^{−1}[1 + 2 Σ_{r=1}^{N_0−1}(1 − r/N_0)] = N_0^{−1}[1 + (N_0 − 1)] = 1. In a shifted direction, it sums to 2 N_0^{−1} Σ_{r=0}^{N_0−1} (1 − (r + ½)/N_0) = 2 N_0^{−1}(N_0 − N_0/2) = 1. The product of the four factors is 1. This proves (b), and (c) follows from (a) and (b).

*Step 10 (the bulk, under (Tr)).* (Tr) gives K_z(x̃, ỹ) = K_0(x̃ − z, ỹ − z). So the sum defining b_z is the same at every z. Now Σ_x K_0^{μν}(x̃, x̃ + u) = π_{μν}(u) converges absolutely, and Σ_u e^{m|u|} |π_{μν}(u)| ≤ C_m(0). Reindex the double sum by u = ỹ − x̃; this gives b_0 = Σ_u π_{μν}(u) u_μ u_ν = b[G]. ∎

*Remarks.* (i) The identity concerns the full pointed total Σ_{X∋z}, before any domain restriction. The window sum of WF13a keeps only X ⊂ □^{~2}. Its kernel differs from K_z by the long domains, whose weighted moment is at most C g e^{−c/σ} times a fixed polynomial (SA 15868-15876). So the window member satisfies (20) up to that tail. (ii) The midpoint convention matters only in Step 7; Steps 5 and 6 make lower-start and midpoint moments equal (SA 13193-13203). (iii) Nothing above uses positivity, reality or a bound uniform in j. The identity holds at each fixed j once C_m(z) < ∞.

## 4. The inputs for the actual class, at fixed j

Read "the actual critical background pair" as the j-fold augmented critical branch u_{0,j} of `prefactor-loc.md` Section 2: the R3 average (SA 5631-5651 = CMP 109 (0.12)) with the contour gauge insertion (CMP 109 (0.14)-(0.16)), and J the current of that configuration. Call this reading (Id). A different gauge representative changes nothing below if it differs by a bare map constant on level-j blocks.

| Input | State for the actual class | Source |
|---|---|---|
| (C) | holds | Constant maps are block-constant. `prefactor-loc.md` Lemma D (c): the branch is covariant by uniqueness near 1. |
| (G) | holds, given (Id) | `prefactor-loc.md` Lemma D (c) proves u_{0,j}(v^h) = u_{0,j}(v)^{h̃}, with h̃(x) = h(Y(x)) constant on level-j blocks (checked by Codex, row 166). The members are invariant under such maps: `carrier-adopt.md` Lemma L (c) and `h-walk-fix.md` Theorem IC give covariance of every term under the block-constant subgroup, and a member is a trace or logarithm of such terms. That subgroup is exactly what (G) reads. |
| (D), (Mo) | hold at each fixed j, with constants that depend on j | The background is holomorphic near 0 (A1, `a1-balaban.md` (9.2), checked). The near-zero core holds with a j-dependent radius r_j > 0 (`d1-floor.md` 4c, from (9.2)). The member bound is g_j e^{−κ d_j(X)} on that core (class norm, SA (OSF2)). The response decays exponentially at fixed depth (`prefactor-loc.md` Lemma B, checked). The rooted count is C_D e^{κ_D q} with κ > κ_D. Then SA's (PH5a), redone with these inputs, gives C_m(z) ≤ C g_j r_j^{−2} < ∞, and normal convergence gives (D). |
| (AR) | holds, given (Id) | `prefactor-loc.md` Lemma A (checked, row 166): R_{0,j}ℓ = ℓ_f + dψ, with multiplier response 0. In the chart U_b = e^{iηA_b}, η = L^{−j}, the field ℓ_f = L^{−j}c + L^{−2j}C x̃ (level-0 units) is A_b = c + C X̃ in level-j units, so it has the same coefficients. The decay clause is Lemma B. |
| (H_z) | **not supplied** | Single terms are covariant only under isometries that preserve the M_1-grid (`h-walk-fix.md` Theorems W' (d'), IC; SA 10340). A-terms are covariant only under 𝒢_ax, given (I4b). The pointed total at z inherits these, and nothing more. Hence (H_z) is available at most at the base points that the grid point group fixes, and not under permutations outside 𝒢_ax. |
| (Tr) | **not supplied** | The same sources: only translations by the grid are supplied. `carrier-adopt.md` lists "covariance of pointed totals under all isometries (B2)" as open, three times. |

The P_j side of (H_z) and (Tr) holds. `prefactor-loc.md` Lemma B gives covariance under level-j translations. Lemma D (c) gives covariance under the hypercube about a block centre, that is, about a level-j site, since L is odd and the R3 contour family is symmetric. So the gap is on the member side alone.

**First failing input for (20): (R14) for the actual old regular member**, that is, (H_z) at every base point together with (Tr). By Theorem P (c), (20) holds at z exactly when the prescribed coefficient equals b_z. Without (H_z), D²F_z(0)[ℓ_F, ℓ_F] is a general quadratic form in F, and no single coefficient cancels it (Section 5). Everything else that (20) reads is supplied at fixed j by checked notes, under the reading (Id).

The quantitative versions are different inputs, and they are needed only for (19): r_j ≍ α_j uniformly in j, which is (ER8) and reduces to (ER7) (`d1-floor.md` 4c-4d), and response decay uniform in j (SA 13323-13345). See Section 7.

## 5. (R14) cannot be dropped, and the total does not replace it

Each example below is a local, real, gauge-invariant member with finite moments. Each satisfies (D), (C), (G), (Mo) and (AR) (use any P_j with (AR)). Let X_z be the closed coarse cube of side 2 centred at z; it carries the support of h_z. Every computation is Step 9 of Section 3, done orientation by orientation.

**Example 1 (fails only permutations in (H_z)).** Take real c_{μν} = c_{νμ}, not all equal, and put G^{(1)}(X_z, (U, J), z) := Σ_{μ<ν} c_{μν} Σ_{p∈P_{μν}} h_z(p) A_p(U), with zero on other domains. It satisfies (Tr) and reflections about z, but not permutations. Then (1/2) D²F_z(0)[ℓ, ℓ] = (1/2) Σ_{μ<ν} c_{μν} ⟨F_{μν}, F_{μν}⟩. So D²(F_z − b A_z ∘ P_j)(0)[ℓ, ℓ] = Σ_{μ<ν} (c_{μν} − b) ⟨F_{μν}, F_{μν}⟩. For every b, take F with one non-zero component F_{μν}, where c_{μν} ≠ b: the left side is not zero. The second moment P_{μν,μν} = c_{μν} depends on the pair, so no extractor exists.

**Example 2 (fails (Tr); the total is unchanged).** Let G satisfy all inputs with b_z ≡ b. Take θ: ℤ⁴ → ℝ bounded and not constant. File at base point z the two extra domains X_z and X_{z−e_1}: G'_z := G_z + θ(z) A_z − θ(z − e_1) A_{z−e_1}. On a torus, Σ_z G'_z = Σ_z G_z, by telescoping. So the total and its Hessian are unchanged. By Theorem P (b), at base points z and z − e_1, b'_z = b + θ(z) − θ(z − e_1). The jets stay isotropic, by the Ward identity of Step 8, but (20) with one coefficient fails wherever θ(z) ≠ θ(z − e_1). So a pointed coefficient is not determined by the total.

**Example 3 (fails only reflections in (H_z)).** Let q(x) := ε_{μνκλ} tr(Q_{μν}(x) Q_{κλ}(x)), where Im W := (W − W^{−1})/(2i) and Q_{μν}(x) is the mean of Im W over the four μν-plaquette holonomies W based at the bare site x (the clover). Both holonomies in the trace are based at x, so q is gauge invariant. Put G^{(3)}_z := θ Σ_x h_z(x) q(x), summed over bare sites. It satisfies (Tr) and every proper signed permutation, but is odd under a reflection. Its jet at ℓ is θ' Σ ε_{μνκλ} ⟨F_{μν}, F_{κλ}⟩, with θ' = 2θ, by the unshifted quadrature η⁴ Σ_x h_z(x) = 1. Its second moment is zero, because ε_{μνμν} = ε_{μννμ} = 0. So the bulk extractor is 0, and yet (20) with b = 0 fails at F_{12} = F_{34} = 1. This is the alternating tensor left open by proper rotations in Step 7. The outline's remark at SA 13240-13242 ("full reflections are used here") is correct and necessary.

**Why a residual matters for (19).** WF8 bounds each base point separately, and WF9, WF14 add the bounds absolutely. A pointed residual of size g_j(ρ_jσ_j²)² per base point therefore adds C_Mσ_j^{−4} g_j ρ_j² σ_j⁴ = C g_j ρ_j² to (19), with no factor L^{−α_H(k−j)}. Then ω_n is not summable. Example 3's residual is a lattice total derivative in the bulk, but within one window it is a boundary term of the same order: σ^{−3}·(α_kσ)(α_kσ²) = α_k², the same as the marginal term σ^{−4}(α_kσ²)². Example 2 with bounded θ is a discrete divergence in z, so a summation by parts inside a window would gain one factor σ. The window-first rule does not do that summation.

## 6. Lemma R: re-pointing reduces (R14) to invariance of the total

**Lemma R.** Let T_N be a level-j torus that is symmetric about a level-j site. Let 𝔊_N be the finite group generated by its unit translations and the signed permutations about that site. Let G be a pointed family on T_N, defined on a 𝔊_N-invariant core, and gauge invariant under level-j block-constant maps. Assume P_j is 𝔊_N-covariant, with the reversed-bond twist (`prefactor-loc.md` Lemmas B, D (c)). For g ∈ 𝔊_N write g·P for the transformed pair, and define

  Ḡ(X, P, z) := |𝔊_N|^{−1} Σ_{g∈𝔊_N} G(g^{−1}X, g^{−1}·P, g^{−1}z),

where G is zero on sets that are not among its domains. Then:
- (i) Ḡ satisfies (R14): Σ_{X∋hz} Ḡ(X, h·P, hz) = Σ_{X∋z} Ḡ(X, P, z) for every h ∈ 𝔊_N. So (H_z) holds at every z, and (Tr) holds.
- (ii) ‖Ḡ‖_{j,κ} ≤ ‖G‖_{j,κ}, because d_j(gX) = d_j(X).
- (iii) Each Ḡ(X, ·, z) reads the pair on X only. Gauge invariance, reality and holomorphy carry over.
- (iv) If G's domains are unions of cubes of one M-grid, with the symmetry site on that grid and M dividing N, then Ḡ's domains are unions of cubes of the M⁴ offset grids. So the rooted count gains at most the factor M⁴.
- (v) Σ_{X,z} Ḡ(X, P, z) = |𝔊_N|^{−1} Σ_g Tot_G(g^{−1}·P), where Tot_G := Σ_{X,z} G. This equals Tot_G(P) for all P exactly when (TI) holds: Tot_G(g·P) = Tot_G(P) for every g ∈ 𝔊_N.

*Proof.* (i): substitute g = hg' and X = hX'; the sum over g' ∈ 𝔊_N is unchanged. (ii)-(iii): Ḡ is an average of |𝔊_N| terms, each bounded by ‖G‖ e^{−κd_j(X)} and reading only g^{−1}X. Block-constant maps are conjugated to block-constant maps by every g ∈ 𝔊_N. (iv): the hypercube about a grid point preserves the grid, so 𝔊_N maps the M-grid to its translates, and there are M⁴ of those. (v): exchange the finite sums. ∎

**Consequence.** Assume (TI) for an old regular member G of level j. Use Ḡ in place of G as the supplied localisation rule; the outline allows this, since it states that the rule is "supplied once, for every torus and list" (SA 6229-6231). The effective action is unchanged, and so are the other inputs of Theorem P. (Mo) holds with sup_z C_m(z). Theorem P then gives (20) at every base point, with the single coefficient b = b[Ḡ]. That coefficient is the bulk coefficient of the Hessian of Tot_G, so it is fixed by the total. The non-wrapping terms of Ḡ agree across tori with room, because each g maps non-wrapping domains to non-wrapping domains. So Ḡ has a companion on ℤ⁴. With grid covariance of G, the average over translations is an average over the M⁴ grid offsets.

So **(R14) reduces to (TI)**, invariance of the member's total under unit translations and the hypercube about a site. That is a statement about an unpointed functional, and it is weaker than (R14), by Examples 2 and 3. For the remainders the outline already requires invariant totals (SA 7581, 20636). (TI) is not proved here, and it is the second reduction of this item. What (TI) would read:
- The step functional E^{(j)}[θ; x; S] (SA 6211-6226) is invariant once its kernel T^{sf}_{j−1}, its non-pivot bond coordinates, its sharp box, the background U_j and the previous list S are covariant. The pivots are covariant (SA 10340).
- The operator sums of the step are covariant under every isometry that preserves T^{(k)} and the regions (SA 10340). These are the cited inputs (I4-tr), (I4a), (I4b), not yet checked here (`h-walk-fix.md` "Open").
- One risk to name: a sharp box in gauge-fixed coordinates is not gauge invariant. If the coordinates used an oriented axial tree, the total could depend on the orientation through the failed-test terms. SA's non-pivot coordinates avoid this only if the pivot rule is isometry-covariant, as SA 10340 states. That should be checked where the kernel is rebuilt.

## 7. Then (19): what it reads besides (20)

Notation is that of SA (WF1): σ = σ_j = L^{−(k−j)}, ρ = ρ_j = max(1, α_k/α_j), s_k = δ_k/α_k, and r_{B,j} is the datum radius with α_j/r_{B,j} ≤ C. G̃ := G − b_j 𝖠_{j,z} is the member with its own counterterm filed at z (WF13a).

**Proposition W (regular part of (19)).** Fix k, x = t, and one old regular member G of level j < k with norm g_j. Assume:
- (P20) (20) for the full pointed total of G at every base point, with one coefficient b_j. This holds by Theorem P under (R14), or under (TI) by Lemma R.
- (ER8u) The near-zero core inclusion with radius r_j ≥ c α_j, with c independent of j (SA (ER8), L6586-6600).
- (BX) The box package (SA 15821-15826; the pointed window remainder, SA 13427 onward). On the ν-disc (WF6), the datum of the critical box pair at a base point z is ℓ_z + E_z near z, in an axial gauge about z and in level-j units. Here ℓ_z is affine with slope at most Cα_kσ². The error E_z has Hölder part at most Cα_kσ^{2+α_H}|x − z|^{1+α_H} and nonlinear part at most C r_{B,j}^{−1} α_k² σ⁴ (1 + |x − z|)². The box Hessian at 0 differs from the infinite-volume one by a kernel with moments at most C g_j α_j^{−2} e^{−cM/σ}.
- (UR) The moment bound C_m(z) ≤ C g_j α_j^{−2}, uniformly in j. Given (ER8u), this follows from SA (PH5a) once the response decay is uniform in j (SA 13323-13345).
- (YA) The whole-core bound for G and for its own tent action, for domains whose Cauchy-size parameter T_X := ρσ² D_X is at least 1 (D_X = 2 + diam_j X), and at the finitely many young ages (SA 15827-15835, 16038-16044).
- The inputs already checked or proved: WF room (WF5)-(WF7) (`wf-room-2.md`, checked); the complementary, long-domain and removed bounds (`wf7-bf.md` (3)-(6), checked in `cond-c.md` §1); the brackets and rate allocation (WF13)-(WF13d) (`wf7-bf.md` §4); the age bound ρ_j² ≤ C(1 + k − j) (WF1).

Then, at one base point, the inner window value after the vacuum and own-counterterm subtraction is at most

  C g_j [ρ²σ^{4+α_H} + ρ³σ⁶]          (WF8)

and the regular part of (19) holds with ω_n = C(1 + n)^{3/2} L^{−α_H(n−1)}.

*Proof.* Split the domains X ∋ z at T_X = 1.
1. *Small domains (T_X < 1).* By (ER8u), the pair on X stays in the near-zero ball of radius cα_j/2. Taylor-expand each G̃(X, P_j^box(·), z) at 0. The linear terms vanish domain by domain (Theorem P, Step 1).
2. *The quadratic terms at ℓ_z.* By (P20), they sum to zero over all X ∋ z. So the small-domain sum equals minus the large-domain sum. Each large-domain term is at most C g_j α_j^{−2}(α_kσ²D_X)² e^{−κd_j(X)} = C g_j T_X² e^{−κd_j(X)}, which is at most C g_j T_X³ e^{−κd_j(X)}.
3. *Cross and error terms.* By (UR) and the polynomial growth of ℓ_z and E_z, |D²F̃_z(0)[ℓ_z, E_z]| ≤ C g_j α_j^{−2} · α_kσ² · (α_kσ^{2+α_H} + r_{B,j}^{−1}α_k²σ⁴). This is at most C g_j(ρ²σ^{4+α_H} + ρ³σ⁶), since α_k/r_{B,j} ≤ Cρ. The E–E term is smaller by one more factor σ^{α_H}, given ρσ ≤ C_age (WF2).
4. *Cubic terms.* Cauchy on the ball of radius cα_j bounds the remainder on X by C g_j T_X³ e^{−κd_j(X)} = C g_j ρ³σ⁶ D_X³ e^{−κd_j(X)}.
5. *Large domains.* (YA) gives at most C g_j (1 + T_X²) e^{−κd_j(X)} ≤ C g_j T_X³ e^{−κd_j(X)}, since 1 + T² ≤ 2T³ for T ≥ 1.
6. *Sums.* The rooted count C_D e^{κ_D q} with κ_sum > κ_D sums every fixed polynomial in D_X; with Lemma R this count gains the factor M⁴. This proves (WF8).
7. *Base points and ages.* There are C_M σ^{−4} base points in a window, so the window value is at most C g_j(ρ²σ^{α_H} + ρ³σ²) ≤ C g_j ρ³ σ^{α_H} (WF9), because ρ ≥ 1, σ ≤ 1 and α_H ≤ 1. Then (WF1) gives ρ³σ^{α_H} ≤ ω_{k+1−j}. Cauchy on |ν| < c_ν/s_k gives exactly one factor s_k. The brackets cost (e^{κ̄} − 1)^{−|K|} with no factorial. (WF13c)-(WF13d) give the output decay. The box-versus-infinite Hessian difference in (BX) adds C g_j ρ² e^{−cM/σ}, which (WF12)'s argument absorbs into ρ³σ^{α_H}. ∎

The defect and aged-remainder terms of (19), C s_k Σ ρ_j²(d_j + r_j), need no counterterm (WF10). They read (ER8u) and (YA), and not (20).

**First failing input for (19).** (19) reads (20), and through it (R14), which reduces to (TI). Besides (20), the first input of Proposition W that is not supplied is (ER8u), the uniform near-zero core inclusion. It reduces to the uniform complex tower estimate (ER7) (`d1-floor.md` 4c-4d). The checked A1 (9.2) gives a radius that shrinks with depth like L^{−(p−n)}. This is the same input that stops D1's (P3). (BX) is also open: `cond-c.md` 6.2 reads it and does not prove it. (UR) and (YA) are cited, not rebuilt here.

## 8. Result

**Check (Section 1).** `b4-step.md` Section 10 (Codex), B1 for the intrinsic gas: checked line by line by Claude, first failing step none. (15)-(18) and 10.1 ADVANCE as implications from (6), (14), the full-hull and heredity premises with [RT], and the order of `um-envelope.md` Section 5.

**Proved here by Claude, not yet checked by the other model:**
- **Theorem P.** The outline's B2 cancellation (SA PH1-PH23), rebuilt with the base point fixed. Under (D), (C), (G), (Mo) and (H_z), the pointed affine jet is (b_z/2) Σ_{μ<ν} ⟨F_{μν}, F_{μν}⟩. Under (AR), the own tent action's jet is (1/2) Σ ⟨F, F⟩. So (20) holds at z exactly when b = b_z. Under (Tr), b_z = b[G], the bulk extractor. All exchanges rest on the absolute moments (Mo), before any domain restriction. I found no error in the outline's PH6-PH23 as an implication. Translation covariance is needed only to make the coefficient common to all base points.
- **The inputs at fixed j (Section 4).** (C), (G), (D), (Mo) and (AR) hold for the actual class at each fixed j, under the reading (Id) of the background as the augmented R3 branch. The sources are checked notes: `prefactor-loc.md` Lemmas A, B, D (c); `a1-balaban.md` (9.2) with `d1-floor.md` 4c; `carrier-adopt.md` Lemma L (c); `h-walk-fix.md` Theorem IC.
- **Examples 1-3 (Section 5).** (H_z) and (Tr) cannot be dropped. The total does not fix a pointed coefficient (Example 2). The bulk extractor does not see the alternating jet (Example 3), so full reflections are necessary, as the outline says.
- **Lemma R (Section 6).** Averaging over the finite symmetry group of a symmetric torus gives (R14) with the same norm, locality and gauge invariance. The rooted count gains a factor M⁴. The total is preserved exactly when (TI) holds.
- **Proposition W (Section 7).** (19) for the regular members follows from (20), (ER8u), (BX), (UR), (YA) and the inputs already checked.

**First failing input.**
- For (20): (R14) for the actual old regular member, that is, covariance of its pointed totals under the hypercube about every base point and under unit translations (SA 5889-5898, 7581). Our chain supplies only grid isometries for single terms. Lemma R reduces (R14) to (TI), invariance of the member's unpointed total. (TI) is open; this is the second reduction, so the item stops here.
- For (19), besides (20): (ER8u) = (ER7), the uniform complex tower estimate, which also stops D1's (P3). (BX) is also open.

**What would change.** If (TI) holds, adopt Lemma R's re-pointing as the localisation rule. Then (20) holds for every old regular member, with the coefficient fixed by the total, and B4's (19) and WF7's retained premise reduce to (ER7) and (BX). If (TI) fails, the failure is a non-invariant part of the total. It would have to be filed as a scale-small non-covariant defect (SA 4007-4010) with its own bound, or (19) loses its age decay (Section 5).

**Evidence for other owners (not edited here).**
- `b4-step.md` Section 11: (20) is Theorem P plus (R14). The "extractor-to-tent identification" is Theorem P (b)-(d).
- `wf7-bf.md` §3 and `cond-c.md` §6.1-6.2: their retained "pointed Hessian cancellation" is Theorem P under (R14).
- `t0-skeleton.md` row B2: from "cited" to "implication proved (Theorem P, Claude, not yet checked); open: (R14) ⇐ (TI)".
- `sa-ledger.md` rows PH17, PH18, PH23: rebuilt here; PH17 and PH23 need (H_z), and PH18's bulk form needs (Tr).
- `h-walk-fix.md` §5 item 8 (i)-(ii): Lemma R is a mean over the torus symmetry group. Given (TI), it supplies both the unit translations and the non-axial isometries. The cost is a factor M⁴ in the domain count.

**Numerics.** None were run. Every step is by hand.
