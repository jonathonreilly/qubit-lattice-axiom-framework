# YM4 existence via the Balaban RG: lemma ledger (sessions 1-2, 2026-10-26)

**Session-2 header.** REVIEW_S1.md (independent hostile review of the session-1 snapshot) has been applied: every fix
is marked **[R1-fix]** in place. Session-2 additions are marked **[S2]**. Two general caveats from the review apply to
the whole file:
- **Checks test instances, not uniformity.** Each check in checks/ verifies a stated identity or inequality on finitely
  many configurations and sizes. Uniformity in n, k, K, M or the background rests on the written proofs alone.
- **The citation upgrades** marked [v-R1] were confirmed by the reviewer's web search, not by me.

**Goal (owner).** Derive, independently, the existence of 4D pure SU(N) Yang-Mills as a continuum limit of lattice gauge
theory satisfying the Osterwalder-Schrader (OS) axioms. No mass gap is claimed.

Probe document only. No PR, no CL edit, no axiom edit. The lemma DAG follows
`../openai-balaban-review/review.md` section 6 (L1-L10, F1-F4, C1-C4), refined below.

## Status legend
- **PROVEN-HERE**: the complete argument is written in this file.
- **IMPORTED-AND-REVERIFIED**: exact citation and statement; hypotheses checked on our setting; the load-bearing step
  re-derived here, or checked exactly or numerically (named check).
- **IMPORTED-NOT-YET-REVERIFIED**: a named obligation. It never supports a PROVEN claim.
- **OPEN**: the missing estimate is stated.

## Citation key
- **[v]**: title, journal, volume and pages confirmed by web search this session (bibliographic data only; the paper
  bodies are paywalled and were NOT read).
- **[v-abs]**: the abstract or introduction was read.
- **[m]**: from memory, not confirmed.
- **[unverified-citation]**: the attribution is plausible, but the exact reference was not confirmed.

**Global caveat.** Every statement attributed to Balaban below paraphrases the *structure* of his programme. The exact
theorem statements (norms, constants, hypotheses) were not read. Each is therefore `[unverified-exact-statement]`, and
re-verifying it is part of the obligation.

---

## 0. Target, and how it decomposes

**T_fin (finite volume).** On the torus T^4_M (side L^M in resolution-0 units), the lattice measures along a tuned
sequence of bare couplings converge, as the lattice spacing L^-K → 0, to a limit state on a gauge-invariant observable
algebra. The limit is non-trivial and reflection positive, with the torus symmetries.

**T_OS (the owner's target).** There is a state on an E(4)-covariant algebra of gauge-invariant observables on R^4. It
arises as such a limit, satisfies OS0-OS3 (OS4 clustering is listed separately in L9d), and is not a free theory.

Structural findings of this session:
1. **Existence of limit points of block laws is cheap; existence of the theory is not.** At every fixed resolution the
   RG variables live in a compact space, so limit points of the *block laws* exist by compactness alone: L7a and L8a,
   proven here, at finite and at infinite volume, with no infrared control. [R1-fix] These limit points are not yet a
   theory: without E8 the per-resolution limits need not be consistent (A_* ν_{m+1} ≠ ν_m is possible), mass may sit on
   the arbitrary off-D extension, and non-triviality has the L7.0 gap. The content of the theorem lies elsewhere:
   - (a) the limit is non-trivial and consistent across resolutions (needs Balaban's local large-field suppression, L6loc);
   - (b) uniqueness, i.e. convergence of the whole sequence (estimate E7);
   - (c) Euclidean invariance and OS0 regularity on a *local* field algebra (L9b, L9c).
2. **The infrared strong coupling is not an obstruction to the existence of limit points of block laws** (section L8).
   [R1-fix: the session-1 wording "not an obstruction to existence" was overstated.] It obstructs uniqueness of the
   infinite-volume state, clustering and the mass gap. Through uniqueness it also obstructs route γ1 to OS1 on R^4, so
   it may well obstruct existence of the OS theory itself.
3. **Euclidean invariance is the hard core.** On T^4 it is false: the torus breaks O(4). On R^4 it cannot be obtained
   by averaging over rotations, because averaging destroys reflection positivity (remark R9.1). It needs either
   universality (orientation independence, which rests on E7-type estimates) or a second, rotation-covariant observable
   family identified with the block family.

---

## 1. Setting (fixed for the whole document)

- **S1 Lattice.** Fix an integer L ≥ 3, odd. Balaban takes L sufficiently large [m]. The resolution-j lattice is
  Λ_{j,M} = (L^-j Z / L^M Z)^4, in physical units with the resolution-0 spacing equal to 1. The UV cutoff is the
  resolution K, with spacing ε_K = L^-K.
- **S2 Group.** G = SU(N), N ≥ 2. The links are U_b ∈ G on oriented bonds, with U_{-b} = U_b^dag.
- **S3 Wilson action.** S_K(U) = β_K Σ_p (1 - N^-1 Re tr U_p), with β_K = 2N/g_K^2. The measure is
  dμ_K = Z_K^-1 e^{-S_K} Π_b dU_b, with Haar measure dU_b.
- **S4 Averaging (L1).** Fine blocks B(X) have side L in lattice units, and their roots are the block centres c_X (L is
  odd).
  - Paths: T_y = P(c_X → y) · [L straight steps from y in direction μ] · P(c_Y → y + L e_μ)^dag, where P is the
    complete-axial transporter (move in coordinate 1, then 2, 3, 4).
  - Coarse link: U'(X, X + e_μ) = T_{c_X} exp(L^-4 Σ_{y∈B(X)} log(T_{c_X}^-1 T_y)), with the principal logarithm.
  - The map is defined on the small-field domain D = {||T_{c_X}^-1 T_y - 1|| < 1 for all y}.
  - The iterate A^{K-m} gives the resolution-m field V^(m). [Balaban-type; whether it equals the CMP 98 definition is
    unverified.]
- **S5 Renormalisation condition (RC).** Fix w* ∈ (0, 1). Tune β_K so that
  E_K[1 - N^-1 Re tr V^(0)_p] = w* for a resolution-0 plaquette p. Weak coupling at resolution 0 corresponds to w*
  small (L7.0).
- **S6 Observables.** O_m(X) is the set of continuous, gauge-invariant f(V^(m)|_X) for X a finite union of
  resolution-m blocks, extended measurably off D. The algebra is O = ∪_m O_m.
- **S7 OS axioms (target).**
  - OS0: regularity / temperedness.
  - OS1: E(4) invariance.
  - OS2: reflection positivity.
  - OS3: permutation symmetry (automatic for these bosonic observables).
  - OS4: clustering.

---

## 2. Lemma ledger

### L0. Locality and consistency of the averaged fields: PROVEN-HERE
**Statement.**
- (i) V^(m)(X, X + e_μ) depends only on the fine links inside B^(m)(X) ∪ B^(m)(X + e_μ), the two resolution-m blocks.
- (ii) Under a fine gauge transformation g, V^(m)(X, Y) → g(c^(m)_X) V^(m)(X, Y) g(c^(m)_Y)^dag. Here c^(m) are the
  iterated roots: the centre of a block of side L^{K-m} is a fine site, because L is odd.
- (iii) A(V^(m+1)) = V^(m) holds identically on D (D_N for N ≥ 7, see L1b) (definition of the iterate).
- (iv) Every f ∈ O_m(X) is gauge invariant, bounded, and measurable with respect to the links in X.

**Proof.**
- (i) For one step: the axial paths P stay inside their own block. The straight leg runs from y ∈ B(X) to
  y + L e_μ ∈ B(X + e_μ), and its μ-coordinate stays in [X_μ L, X_μ L + 2L - 1], so it passes only through the two
  blocks. Induct on the number of steps; at each step the two coarse blocks contain the fine blocks used.
- (ii) Every T_y has the endpoints c_X and c_Y, so T_y → g(c_X) T_y g(c_Y)^dag. The rest is L1a, applied
  inductively, with the coarse gauge transformation g|_roots.
- (iii) By definition.
- (iv) f is a gauge-invariant function of the coarse field, which by (ii) transforms covariantly; locality is (i). ∎

### L1. Gauge-covariant averaging
- **L1a. Covariance: PROVEN-HERE.** U'[g·U] = g(c_X) U'[U] g(c_Y)^dag, and D is gauge invariant.
  - Proof: T_{c_X}^-1 T_y → g(c_Y) (T_{c_X}^-1 T_y) g(c_Y)^dag. The principal log commutes with unitary conjugation,
    the norm is conjugation-invariant (so D is invariant), and the exp of the averaged log is conjugated by g(c_Y).
    Multiply by T_{c_X} → g(c_X) T_{c_X} g(c_Y)^dag. ∎
  - Check c1(a): error 6e-16 for SU(2) and 6e-15 for SU(3), with random g on all fine sites.
- **L1b. SU(N)-valued; pure gauge goes to pure gauge: PROVEN-HERE.**
  - **Domain.** Take D_N = {||T_{c_X}^-1 T_y - 1|| < 2 sin(π/N) for all y}. For N ≤ 6 the bound 1 of S4 suffices
    (2 sin(π/6) = 1); for N ≥ 7 use D_N. [R1-fix: session 1 wrote "N ≤ 5" here and "fails for N ≥ 7" in LOG; the
    correct threshold is N ≤ 6.] D_N shrinks like 1/N, so any claim uniform in N must track it.
  - **Proof.** Each Z_y = T_{c_X}^-1 T_y ∈ SU(N) has eigenvalues e^{iθ_j}. The domain condition gives |θ_j| < 2π/N
    (for N ≤ 6, the bound 1 gives |θ_j| < π/3 ≤ 2π/N).
    - So the principal log is i·diag(θ_j) in the eigenbasis, anti-Hermitian, with trace iΣθ_j.
    - det Z_y = 1 gives Σθ_j ∈ 2πZ, and |Σθ_j| < 2π, so Σθ_j = 0.
    - The average of traceless anti-Hermitian matrices is traceless anti-Hermitian, its exponential lies in SU(N), and
      T_{c_X} ∈ SU(N).
  - Pure gauge: U_b = g_x g_y^-1 gives T_y = g(c_X) g(c_Y)^-1 for all y, all the logs vanish, and
    U' = g(c_X) g(c_Y)^-1. ∎
  - Check c1(b, c) for SU(2) and SU(3).
- **L1c. Linearisation: PROVEN-HERE.**
  - If U_b = exp(i t a_b) with ||a_b|| ≤ 1, then log U' = i t L^-4 Σ_y (Σ_{b∈Γ_y} a_b) + O(t^2), where Γ_y is the
    path of T_y. This is Balaban's abelian averaging Q applied to the line integrals.
  - Proof: BCH gives log T_y = i t Σ_{Γ_y} a_b + O(t^2) and log(T_{c_X}^-1 T_y) = log T_y - log T_{c_X} + O(t^2).
    Average, and add log T_{c_X} back at order t. ∎
  - [R1-fix] Check c1(d) compares log U' with avg_y log T_y, **not** with the averaged line integrals stated above. Those
    two differ at O(t^2) (the second-order BCH commutators cancel in the first, so log U' = avg log T_y + O(t^3)), which
    is why the halving ratio is about 4. The session-1 reading "second order, better than the claim" was a misreading of
    which identity was tested. The lemma itself stands on the BCH proof; the line-integral form is untested by c1(d).
  - The O(t^2) constant depends on L through the path lengths; no uniformity in L is claimed.
- **L1d. Regularity on Balaban's spaces of regular configurations: IMPORTED-NOT-YET-REVERIFIED.**
  - Content: analyticity of A on D; derivative bounds; the coarse small-field condition implied by the fine one with
    L-dependent constants; the composition of k steps controlled uniformly in k.
  - Sources: Balaban, "Averaging operations for lattice gauge theories", CMP 98 (1985) 17-51 [v]; "Spaces of regular
    gauge field configurations on a lattice and gauge fixing conditions", CMP 99 (1985) 75-102 [v-R1].
  - [S2] The k-uniform *sup-curvature* part of this obligation is now proven for L ≥ 9 (d = 4): see **L1e** below.
    Analyticity, derivative and Hölder bounds remain imported.
  - Finite diagnostic c1(e): one coarse plaquette has F_coarse ≈ 0.14-0.2 F_fine,max for smooth SU(2) and SU(3) fields.
  - Obligation: a k-uniform version with explicit constants.

- **L1e. [S2] Iterated averaging stays uniformly close to straight fine transport: PROVEN-HERE.**
  - **Setting.** Fine spacing ε = L^-k in physical units, so unit blocks have side 1. Put V^(k) = U and
    V^(j) = A(V^(j+1)) (S4 applied on the resolution-(j+1) lattice), with s_j = L^-j.
    - For a resolution-j link b = (X, X + e_μ), let S_b be the fine straight transporter between the fine roots c^(j)_X
      and c^(j)_X + s_j e_μ. These roots are fine sites; the iterated root offset is (L^{k-j} - 1)/2.
    - F := max over fine plaquettes p in the region of ||1 - U_p|| / ε^2.
    - Define δ_j := max_b ||V^(j)_b - S_b|| / s_j^2, so that δ_k = 0.
    - Constants: c := 4 arcsin(1/4) = 1.0107, C_A := (d-1)/2, and ρ := (1 + c(d+2)) / L.
  - **Claim (recursion), for every odd L.** If every Z_y used at level j obeys ||Z_y - 1|| ≤ 1/2, then
    δ_j ≤ ρ δ_{j+1} + c C_A F.
  - **Corollary (uniform in k).** Let L > 1 + c(d+2) (= 7.07 in d = 4, so L ≥ 9), and put C_δ := c C_A / (1 - ρ). If
    F ≤ F_0 := 1 / (2(C_A + (d+2) C_δ / L)), then for all k and all j ≤ k:
    - (a) the domain hypothesis holds at every level, and δ_j ≤ C_δ F;
    - (b) coarse curvature: ||1 - V^(j)_p|| ≤ s_j^2 (1 + 4 C_δ) F, so F_j ≤ (1 + 4C_δ) F uniformly in k;
    - (c) every V^(j) lies in D (indeed ||Z_y - 1|| ≤ 1/2 < 1). For SU(N) membership via L1b we also need
      1/2 < 2 sin(π/N), i.e. N ≤ 12. For N ≥ 13, replace 1/2 by τ_N/2 throughout, which shrinks F_0 by a factor ~ 1/N.
    - The proof uses only unitarity and the spectral log, so it holds for every SU(N), with c computed at the threshold
      used.
  - **Proof of the recursion.**
    - Write V = V^(j)_b = T_c exp(X̄), where X̄ = avg_y log Z_y and Z_y = T_c^-1 T_y are products of resolution-(j+1)
      links. Let T^S and Z^S be the same products with every V^(j+1) link replaced by its S.
    - T_c is the straight product of L links, and T^S_c = S_b. For unitaries, ||Π A_i - Π B_i|| ≤ Σ ||A_i - B_i||.
      Hence ||T_c - S_b|| ≤ L δ_{j+1} s_{j+1}^2 = δ_{j+1} s_j^2 / L.
    - Z_y contains at most 2L + d(L-1) ≤ (d+2)L links: two axial legs of at most d(L-1)/2 links each, and two straight
      legs. Hence ||Z_y - Z^S_y|| ≤ (d+2) δ_{j+1} s_j^2 / L.
    - **Ribbon bound: ||Z^S_y - 1|| ≤ C_A s_j^2 F.**
      - Z^S_y is the fine holonomy of γ σ_y (γ + s_j e_μ)^-1 σ_c^-1. Here γ is the fine realisation of the
        resolution-(j+1) axial path c_X → y, σ is the straight μ-leg of length s_j, and γ + s_j e_μ is the axial path
        c_Y → y + s_j e_μ, because axial paths are translation covariant.
      - Insert σ_p σ_p^-1 at each corner p of γ. The loop becomes a product of conjugated rectangle loops, one per
        segment γ_ν.
      - For ν = μ the rectangle is degenerate and collinear, so its holonomy is exactly 1.
      - For ν ≠ μ it is a planar |γ_ν| × s_j grid. Its boundary holonomy is a product of conjugated plaquettes (row by
        row: each row is a ladder, as in L3s(i)), so its norm is ≤ |γ_ν| s_j F.
      - Finally |γ_ν| ≤ ((L-1)/2) s_j / L < s_j / 2. Summing over ν ≠ μ gives ≤ (d-1) s_j^2 F / 2.
    - **Log and exp bounds.**
      - If ||Z - 1|| ≤ 1/2, then ||log Z|| ≤ c ||Z - 1||. Z is normal, |e^{iθ} - 1| = 2 sin(|θ|/2), and
        2 arcsin(x/2)/x is increasing, with value c at x = 1/2.
      - For anti-Hermitian X, ||e^X - 1|| ≤ ||X||, and ||X̄|| ≤ max_y ||log Z_y||.
    - **Combine.** ||V - S_b|| ≤ ||T_c - S_b|| + ||e^{X̄} - 1||
      ≤ s_j^2 [δ_{j+1}/L + c(C_A F + (d+2) δ_{j+1}/L)]. Divide by s_j^2. ∎
  - **Proof of the corollary.** Induct downward from δ_k = 0.
    - If δ_{j+1} ≤ C_δ F, then ||Z_y - 1|| ≤ s_j^2 (C_A + (d+2) C_δ / L) F ≤ 1/2, using s_j ≤ 1 and F ≤ F_0. So the
      recursion applies, and δ_j ≤ ρ C_δ F + c C_A F = C_δ F.
    - (b): S_p is the fine holonomy of a planar s_j × s_j square, so ||1 - S_p|| ≤ s_j^2 F. Add the four link errors.
    - (c) is the domain bound. ∎
  - **Check c5** (SU(2); d = 2, 3, 4; L = 3, 5, 7, 9; k = 2-3). The recursion and the domain hold in every small-field
    case.
    - Measured δ_j/F lies in 0.01-0.08, far below the bound c C_A ≈ 1.5 (d = 4).
    - In the L = 3 cases (ρ > 1, not covered by the corollary) the measured δ_j grows roughly additively in the number of
      levels: 0.028, 0.057, 0.083 in d = 3 with k = 3. So uniformity in k at small L is genuinely not shown.
    - These are instances, not uniformity tests.
  - **What remains of L1d:** analyticity in U, derivative and Hölder bounds, and the large-field side.

### L2. Background field (constrained minimiser): IMPORTED-NOT-YET-REVERIFIED
- **Statement (paraphrase).** For V in the coarse small-field domain, the Wilson action restricted to {U : A(U) = V}
  has a unique minimiser U(V) near the identity in a suitable axial/Landau gauge. U(V) is analytic in V and
  exponentially localised.
- **Source.** Balaban, "The variational problem and background fields in renormalization group method for lattice gauge
  theories", CMP 102 (1985) 277-309 [v-R1].
- **Obligation.** An SU(2) Newton/continuation check of uniqueness on an 8^4 torus, plus a written contraction argument.

### L3. Fluctuation propagators uniform in small-field backgrounds

#### L3s. Scalar multi-scale covariance in SU(N) backgrounds: PROVEN-HERE (a strictly weaker analogue of Balaban's bound)
[R1-fix] This is a scalar, weaker analogue of Balaban's propagator bounds. Its constants are uniform in n = 1/ε. Scope:
- (a) Session 1 proved it for the *direct* axial average only. [S2] Corollary L3s' below extends it to both forms of the
  iterated average, which closes R3.1.
- (b) It covers scalar 0-forms only: no gauge fixing, any unitary representation. The gauge-field (1-form) analogue is
  L3g, which is OPEN, and session 2 found an obstruction there (L3g-ob).
- (c) It gives only L^2 operator-norm bounds on block-localised pieces. The pointwise kernel bound that follows,
  |G(x,y)| ≤ (2/m) ε^-4 e^{-μρ}, is not uniform. No derivative or Hölder bounds are proved.
- (d) The hypothesis "F small" holds for smooth backgrounds such as the minimisers U(V) of L2, not for typical Wilson
  configurations, where F ~ g/ε^2. *Applying* L3s therefore needs L2 and L1d (imported).
- (e) It is quantitative: for a = 1 it needs F < 1/3.

**Setting.**
- d = 4 and n ≥ 1, with spacing ε = 1/n. The torus is Λ = (εZ/TZ)^4, partitioned into unit cubes B, each with n^d
  sites.
- φ ∈ ℓ^2(Λ, C^N), with ⟨φ, ψ⟩ = ε^4 Σ_x φ_x^dag ψ_x. The proof uses only unitarity, so any unitary representation
  works.
- Root: c_B has offsets r_0 = ⌊(n-1)/2⌋, and r = ⌈(n-1)/2⌉ ≤ n/2 is the largest coordinate distance from the root.
  P(c → y) is the complete-axial transporter inside B.
- ⟨φ, -Δ_A φ⟩ = ε^2 Σ_{bonds b=(x,y)} |φ_x - U_b φ_y|^2.
- (Q_A φ)(B) = ε^4 Σ_{y∈B} P(c_B → y) φ_y, with ||Qφ||^2 = Σ_B |(Qφ)(B)|^2.
- H_A = -Δ_A + a Q_A^dag Q_A, with a > 0.
- F := max over plaquettes p inside the blocks of ||1 - U_p|| / ε^2 (operator norm).
- A_max := max over intra-block bonds of ||1 - U_b^ax|| / ε, where U^ax is the field in the complete axial gauge of
  each block.

**Claims.** Every constant is independent of n, T, N and of the background.
- (i) A_max ≤ (d-1) r ε F ≤ (d-1) F / 2.
- (ii) H_A ≥ m := min(2, a) - d A_max^2 ≥ min(2, a) - d (d-1)^2 F^2 / 4, which is min(2, a) - 9 F^2 in d = 4.
- (iii) Suppose m > 0 and μ ∈ (0, 1/ε] satisfies (CT) (1 - η) m - 1.55 d μ^2 - a (η + η^2) ≥ m/2, with
  η = e^μ - 1. Then for all subsets Δ, Δ' ⊂ Λ,
  ||1_Δ H_A^-1 1_Δ'|| ≤ (2/m) exp(-μ ρ_∞(Δ, Δ')),
  where ρ_∞ is the ℓ^∞ torus distance in physical units.

**Proof of (i).**
- Gauge transform by g(x) = P(c_B → x) on each block. The blocks partition Λ, so this is one gauge transformation. It
  makes every tree link equal to 1 and sends the non-tree link b = (x, x + e_μ) to the holonomy of the loop
  P(c → x) b P(c → x + e_μ)^dag.
- The two axial paths agree in coordinates 1, ..., μ-1. They differ by one step in coordinate μ, then run in parallel
  through coordinates μ+1, ..., d.
- So the loop bounds a ladder of Σ_{ν>μ} |x_ν - c_ν| ≤ (d-1) r plaquettes, each entering as a lasso (a conjugated
  plaquette).
- For unitaries, ||Π V_i - 1|| ≤ Σ ||V_i - 1||, and conjugation preserves the norm. Hence
  ||U_b^ax - 1|| ≤ (d-1) r ε^2 F. Divide by ε and use r ε ≤ 1/2. Bonds in the last direction μ = d are tree bonds. ∎

**Proof of (ii).**
- In the gauge of (i), H_A is unitarily equivalent to the operator with U → U^ax. Because P^ax = 1, Q_A becomes the
  plain block average Q_0. Dropping the inter-block bonds (each term ≥ 0):
  ⟨φ, H φ⟩ ≥ Σ_B [ ||∂_A φ||_B^2 + a |Q_0 φ(B)|^2 ], with ||∂_A φ||_B^2 = ε^2 Σ_{b⊂B} |φ_x - U_b^ax φ_y|^2.
- **Step 1.** Split (φ_x - U φ_y)/ε = (φ_x - φ_y)/ε - (U - 1) φ_y / ε. The triangle inequality in ℓ^2(bonds) gives
  ||∂_A φ||_B ≥ ||∂φ||_B - A_max √d ||φ||_B, since each site is the forward end of at most d intra-block bonds.
  Then (x - y)^2 ≥ x^2/2 - y^2 (or the right side is negative) gives
  ||∂_A φ||_B^2 ≥ (1/2) ||∂φ||_B^2 - d A_max^2 ||φ||_B^2.
- **Step 2 (Poincaré, eq. P).** ||φ||_B^2 ≤ (1/4) ||∂φ||_B^2 + |Q_0 φ(B)|^2.
  - The Neumann grid Laplacian on {0, ..., n-1}^d with spacing ε has eigenvalues Σ_i (4/ε^2) sin^2(π k_i / (2n)),
    with cosine eigenvectors.
  - For k ≠ 0 the eigenvalue is at least (4/ε^2) sin^2(π/(2n)) ≥ (4/ε^2)(1/n)^2 = 4, using sin x ≥ 2x/π on [0, π/2].
  - Decompose φ = φ̄ + φ^⊥ with φ̄ the block mean, which equals Q_0 φ(B) because the block volume is 1. Then
    ||φ̄||_B^2 = |Q_0 φ|^2 and ||φ^⊥||^2 ≤ (1/4) ⟨φ^⊥, -Δ_N φ^⊥⟩ = (1/4) ||∂φ||_B^2. The cross terms vanish.
- **Step 3.** (1/2) x + a y ≥ min(2, a) (x/4 + y) ≥ min(2, a) ||φ||_B^2. Subtract d A_max^2 ||φ||_B^2 and sum over B. ∎

**Proof of (iii) (Combes-Thomas, in the form uniform in ε).**
- Let f(x) = ρ_∞(x, Δ'), which is 1-Lipschitz, and H_μ = e^{μf} H e^{-μf}.
- **Kinetic part.** For a bond, with z = φ_x^dag U φ_y and t = μ(f_x - f_y), |t| ≤ με ≤ 1, the off-diagonal terms give
  real part -2 cosh(t) Re z. Compared with t = 0, the change is ≥ -2 (cosh t - 1) |z| ≥ -(cosh t - 1)(|φ_x|^2 + |φ_y|^2).
  Summing over the 2d bonds at each site, the kinetic real part is
  ≥ ⟨φ, -Δ_A φ⟩ - 2d (cosh(με) - 1) ε^-2 ||φ||^2 ≥ ⟨φ, -Δ_A φ⟩ - d cosh(1) μ^2 ||φ||^2.
- **Block part.** In block B, write e^{±μ f(y)} = e^{±μ f(c_B)} (1 + s_±(y)), with |s_±| ≤ e^{μ/2} - 1 ≤ η. Let
  w = Q_A φ(B) and r_± = ε^4 Σ_y P s_± φ_y. Then |r_±| ≤ η ||φ||_B (Cauchy-Schwarz, block volume 1), and
  ⟨Q e^{μf} φ, Q e^{-μf} φ⟩_B = ⟨w + r_+, w + r_-⟩. Its real part is
  ≥ |w|^2 - 2η |w| ||φ||_B - η^2 ||φ||_B^2 ≥ (1 - η) |w|^2 - (η + η^2) ||φ||_B^2.
- **Combine.** Re ⟨φ, H_μ φ⟩ ≥ (1 - η) ⟨φ, H φ⟩ - [1.55 d μ^2 + a (η + η^2)] ||φ||^2 ≥ (m/2) ||φ||^2 under (CT).
  The numerical range then gives ||H_μ^-1|| ≤ 2/m.
- Finally 1_Δ H^-1 1_Δ' = (1_Δ e^{-μf}) H_μ^-1 (e^{μf} 1_Δ'), with ||1_Δ e^{-μf}|| ≤ e^{-μ ρ_∞(Δ, Δ')} and
  e^{μf} 1_Δ' = 1_Δ'. ∎

**Check c3.**
- n = 1, 2, 3, i.e. ε = 1, 1/2, 1/3, with smooth and rough SU(2) backgrounds at F = 0.1-0.3 and a large rough field.
  (i) and (ii) hold in every case.
- The free gap is exactly 1 = min(2, a) for a = 1: (P) is sharp on constants.
- The spectrum is gauge invariant.
- (iii) on n = 2, T = 4, F = 0.2: m_lb = 0.931, proven μ = 0.147. The block-block norms are ≤ 0.038 × the bound. The
  measured decay rate is 1.78 per unit length.

**Remark R3.1 (perturbed transports): PROVEN-HERE.** Suppose Q' uses unitary transports V'_y with
||V'_y - P(c → y)|| ≤ θ for all y.
- Then |Q' φ| ≥ |Q_A φ| - θ ||φ||_B, by Cauchy-Schwarz with block volume 1. So a|Q'φ|^2 ≥ (a/2)|Q_A φ|^2 - a θ^2 ||φ||_B^2.
- Step 3 with a/2 gives H' ≥ m' := min(2, a/2) - d A_max^2 - a θ^2.
- (iii) holds verbatim with m' in place of m. The block part used only unitarity of the transports and Cauchy-Schwarz.

**Corollary L3s'. [S2] Iterated scalar averaging: PROVEN-HERE (closes the session-1 C_path obligation).**
The iterated scalar average is Q_k φ(B) = ε^d Σ_y W_y φ_y. Each y has a unique ancestor chain
c_B = c^(0) → c^(1)(y) → ... → c^(k)(y) = y, and W_y is the product of stage transports along it. Stage i is a
resolution-i axial path inside the level-(i-1) block. Two versions:
- **(I) Stage paths realised by fine links: θ_I ≤ C_path F, with C_path = d(d-1)/4 (= 3 in d = 4), for every L and k.**
  - Proof: in the unit-block axial gauge of L3s(i), ||W_y - P(c → y)|| = ||W^ax_y - 1||.
  - The composite path has physical length < d/2: per coordinate and per stage at most ((L-1)/2) L^-i, and summing over
    i gives < 1/2.
  - So it has < d/(2ε) fine bonds, each with ||U^ax_b - 1|| ≤ (d-1) ε F / 2 by L3s(i). Multiply. ∎
- **(II) Stage transports by the averaged fields V^(i) (Balaban's natural choice): θ_II ≤ [d(d-1)/4 + d C_δ/(2(L+1))] F.**
  - This holds under the hypotheses of L1e (L ≥ 9 in d = 4, F ≤ F_0).
  - Proof: compare with (I) link by link. Stage i has ≤ d(L-1)/2 links, each within C_δ s_i^2 F of its S, by L1e.
    Then Σ_{i≥1} d((L-1)/2) C_δ L^-2i = d C_δ / (2(L+1)). ∎
- **Consequence.** H' = -Δ_A + a Q_k^† Q_k ≥ min(2, a/2) - 9F^2 - a C_path'^2 F^2 in d = 4, and (iii) holds with this
  gap. Both are uniform in k.
- **Check c5(P).** Measured θ_I/F and θ_II/F are 0.01-0.08, against the bounds 0.5 (d = 2), 1.5 (d = 3) and 3 (d = 4).

**Scope.** L3s is scalar and has no gauge fixing. Balaban's operator acts on 1-forms. See L3g.

#### L3g. Gauge-field fluctuation operator: IMPORTED-NOT-YET-REVERIFIED
- **Statement (paraphrase).** The covariance (Δ_k,A + a Q_k^dag Q_k)^-1 on Lie-algebra-valued 1-forms, in the
  background L2 with Balaban's gauge fixing, has uniform exponential decay and uniform Hölder/derivative bounds. It has
  a random-walk expansion analytic in the background.
- **Sources.** CMP 95 (1984) 17-40 [v]; CMP 96 (1984) 223-250 [v]; CMP 99 (1985) 389-434 [v].
- **Re-verification route (the L3s method).**
  - (a) A Hodge-Poincaré inequality on unit blocks:
    ||A||_B^2 ≤ C_H (||dA||_B^2 + ||d^* A||_B^2) + |Q_0 A|^2, uniform in ε. This is a discrete de Rham/Poincaré
    statement on a cube, a finite matrix problem for each n, and needs a uniform-in-n proof.
  - (b) The Weitzenböck curvature term ad F is bounded by F under the small-field condition, so it shifts the gap by
    O(F).
  - (c) Combes-Thomas exactly as in (iii).
  - (d) Derivative bounds, which do not follow from (iii) and need a separate local-regularity argument.
- (a) and (d) are the open sub-estimates.

**L3g(a)-block. [S2] Block Hodge-Poincaré inequality, absolute boundary conditions: PROVEN-HERE.**
- **Statement.** On the bonds of a unit block {0, ..., n-1}^d with spacing ε = 1/n, let d_B be the block-restricted
  exterior derivative and d_B^* its adjoint (Neumann, i.e. absolute). For R- or Lie-algebra-valued 1-forms A:
  ||A||_B^2 ≤ (1/λ_n) (||d_B A||_B^2 + ||d_B^* A||_B^2), with λ_n = 4n^2 sin^2(π/(2n)) ∈ [4, π^2).
  No averaging term is needed.
- **Proof.**
  - The block's cubical cochain complex is the graded tensor product of d copies of the 1D path complex
    C^0 = R^n → C^1 = R^{n-1}, with the derivative scaled by 1/ε and uniform weights.
  - For graded tensor products, the mixed terms d_i d_j^* + d_j^* d_i (i ≠ j) vanish. So the Hodge Laplacian is
    Δ = Σ_i 1 ⊗ ... ⊗ Δ^(i) ⊗ ... ⊗ 1, each factor acting in its own degree.
  - A 1-form component in direction μ lies in C^1_μ ⊗ (⊗_{ν≠μ} C^0_ν). Its spectrum is λ^(1)_{k_μ} + Σ_{ν≠μ} λ^(0)_{k_ν}.
  - In 1D, the nonzero spectra of d d^* (on C^1) and d^* d (on C^0) coincide: (4/ε^2) sin^2(πk/(2n)), for k = 1, ..., n-1
    on C^1 and k = 0, ..., n-1 on C^0.
  - So the minimum is (4/ε^2) sin^2(π/(2n)) = λ_n ≥ 4, by sin x ≥ 2x/π. ∎
- **Check c6(A).** λ_min equals the formula to 1e-8 for d = 2, 3, 4 and n ≤ 8.
- **Why this does not close L3g.** Unlike ||dφ||^2, the global ||d^* A||^2 is a sum over *sites* of combinations that
  include inter-block bonds. It does not split as Σ_B ||d_B^* A_B||^2, so the L3s block-dropping step fails for the
  gauge-fixing term. The global gap must be obtained another way.

**L3g-ob. [S2] Obstruction for S4's complete-axial contours: OPEN (heuristic argument plus numerical confirmation; not
proven).**
- **Mechanism.** The linearised S4 average (L1c) is (QA)(X, μ) = n^-d Σ_y ∫_{Γ_y} A. All the axial legs out of the root
  c_X start along the coordinate-1 line through c_X. After averaging over y, Q contains a line functional
  ℓ_X(A_1) = ∫ w(x_1) A_1(x_1, c_2, ..., c_d) dx_1 with w = O(1). It enters as f(X) - f(X + e_μ), with f(X) = ℓ_X(A_1).
- **Size.** A line has zero H^1-capacity in d = 4 (codimension 3). So ||ℓ||^2_{H^-1} ~ n: a tube test function of
  radius ε has H^1 energy ~ 4πε and line integral O(1). In d = 3 it is ~ log n; in d = 2 it is bounded.
  - c6(B') measures ||Q_row||^2_{H^-1} = 0.196, 0.261, 0.334 at n = 3, 5, 7 (d = 4). The excess over the straight-leg
    part is 0.097, 0.167, 0.242, about 0.034 n, so linear.
  - The same quantity is 0.214 → 0.236 (d = 3, n = 3 to 15, log-like) and constant at 0.307 (d = 2). The straight-leg
    part alone is bounded in every d.
- **Heuristic consequence (not proven).** In Feynman gauge, M = d^*d + dd^* + aQ^†Q has no gap uniform in (n, T) in
  d = 4.
  - Trial A = dφ + σ, with φ of wave number k and σ = Σ_X φ(c_X) τ_X. Here τ_X are cheap tube profiles with
    ℓ_X(τ_X) = 1, which cancel the coarse gradient in QA.
  - The Rayleigh quotient is ≈ k^2 + C/(n k^2), so inf_T λ_min ≲ 2 (C/n)^{1/2}. This needs T ≳ n^{1/4}.
  - On the T = 2 torus of c6 the only low modes are the constants, which are exact eigenvectors with eigenvalue a
    (c6(B)). Their coarse "gradient" cannot be cancelled on a torus, so the effect is invisible at T = 2.
  - The cross-term estimates are not written out. Status: heuristic.
- **Gauge artifact, recorded so that it is not misread.** c6(C) restricts to the complete-axial gauge inside blocks
  without fixing the residual coarse gauge. Then λ_min ≈ 0.95 a/n even in d = 2. This comes from coarse pure-gauge modes
  on the inter-block faces (||A||^2 ~ n, |QA|^2 ~ 1, dA = 0), not from a coercivity failure.
- **What it means.** The scalar L3s is unaffected: its transports are unitary multipliers, not linearised line
  integrals. For the gauge field, a uniform L^2 gap needs one of:
  - contours spread so that each averaging functional is uniformly in H^-1 (the root funnel is the only problem, since
    the straight-leg part is fine);
  - a gauge fixing under which the funnel terms vanish *together with* a coarse gauge fixing;
  - Balaban's own construction, whose exact contour and gauge choices remain [unverified-exact-statement].
- **Caveat on spreading (heuristic).** Spreading cannot fully cure this. Any root-based covariant average has a
  linearised current J with div J = δ_{c_X} - δ_{c_Y}. Its gradient part has |Ĵ|^2/k^2 ~ k^-4 at large k, so
  ||J||^2_{H^-1} ≥ c log n in d = 4, whatever the contours. Equivalently, on pure gauge A = dφ, QA evaluates φ at points,
  and in d = 4 point evaluation is log-unbounded on H^2.
  - So a uniform Feynman-gauge L^2 gap needs a gauge fixing adapted to Q, one that absorbs the point-source part.
  - My unverified guess is that this is Balaban's choice [unverified-exact-statement]. The line part (~n) can be removed
    by spreading; the log part needs the gauge.
- **[S2] Literature cross-check: Dimock, "Covariant axial gauge", arXiv:1410.2798 [v-abs + body via a summarising fetch;
  data only].** This is an abelian treatment following Balaban.
  - The block average sums A along paths Γ_{x, x+L e_μ} for x in the block, weight L^-4, with no block-centre legs.
    The fetch could only infer that these are straight paths.
  - Covariance is Q ∂λ = ∂ Q λ with the *averaged* scalar gauge function, not a root value.
  - The gauge fixing is a δ-function on a permutation-averaged tree average τA (averaged over the d! coordinate orders),
    with constraints Q_k λ = 0 in the Landau and Feynman steps. Balaban is reported to have "averaged over various trees
    to regain the covariance" and to have used exponential gauge fixing in the YM papers.
  - Consistency with L3g-ob: the straight-leg, averaged-gauge form is precisely the part c6 found uniformly H^-1
    bounded, and the Q_k λ = 0 constraint is a Q-adapted gauge fixing of the kind L3g-ob says is needed.
  - Order averaging is also the repair for L8b.
  - So the obstruction is specific to S4's root-based nonabelian definition. **S4 should be revised** toward Balaban's
    construction (CMP 98; exact nonabelian form still [unverified-exact-statement]).
- **Revised L3g(a) target.** Prove the gap for M_Q = d^*d + (gauge term adapted to Q) + aQ^†Q, with spread contours,
  where the gauge term fixes the components of A that Q sees as point sources. The S4 contours plus the plain Feynman
  term are probably not the right object in d = 4.

### L4. Small-field effective actions and the coupling flow
- **L4a. Structure: IMPORTED-NOT-YET-REVERIFIED.**
  - After k steps, on the small-field region the density is exp(-(1/g_k^2) S_W(V) - Σ_X E_k(X, V)), with polymer
    activities obeying |E_k(X)| ≤ C g_k^{?} e^{-κ d_X}. [The exponent and the norms are unverified.]
  - The coupling recursion, indexed by **resolution** j (finer = larger j), is 1/g_{j+1}^2 = 1/g_j^2 + β_j, with
    β_j → 2 b0 ln L. The coupling grows toward the IR, i.e. as j decreases. [R1-fix: session 1 indexed this by "steps" k,
    which gives the wrong sign if k counts coarse-graining steps.]
  - Sources: CMP 109 (1987) 249-301 [v]; CMP 116 (1988) 1-22 [v]; CMP 119 (1988) 243-285 [v].
- **L4b. One-loop coefficient b0 = 11N/(48π^2): IMPORTED-AND-REVERIFIED.**
  - **Hypotheses (imported).**
    - The Seeley-DeWitt coefficient a2 = tr[(1/12) Ω_{μν} Ω_{μν} + (1/2) E^2] for -(D^2 + E) in 4D (Vassilevich,
      Phys. Rept. 388 (2003) 279-360 [v]).
    - The background-field Feynman-gauge fluctuation operator -D^2 δ_{μν} + 2i ad F_{μν}, with adjoint ghosts -D^2
      [v-R1: Abbott, NPB 185 (1981) 189-203].
  - **Derivation (here).**
    - (1/2) a2_vec - a2_gh = [(1/2)(4·(1/12)·(-C_A) + (1/2)·4 C_A) + (1/12) C_A] F^a F^a = (11/12) C_A F^a F^a.
    - With UV proper-time cutoff Λ and IR scale μ: Γ ⊃ -(16π^2)^-1 ln(Λ^2/μ^2)(11/12) C_A ∫ F^a F^a.
    - Against S = (4g^2)^-1 ∫ F^a F^a this gives 1/g^2(μ) = 1/g_0^2 - (11/3) C_A (16π^2)^-1 ln(Λ^2/μ^2), so
      d(1/g^2)/d ln μ = 2 b0 with b0 = 11 C_A/(48π^2) and C_A = N.
    - The sign gives infrared growth (asymptotic freedom).
  - **Check c2(A).** Exact to 1e-12 for SU(2), SU(3) and SU(4).
  - **Lattice universality of the two log coefficients that enter (c2(B)):**
    - E^2: the slope of ∫_BZ (ω + m^2)^-2 against ln(1/m^2) is 1.0056 → 1.0017 times 1/(16π^2).
    - Ω^2: unit-charge lattice scalar in constant flux on a 64^2 torus; the slope is 0.94-1.10 times 1/(96π^2). This
      is a finite diagnostic, finite-size limited.
  - **Not covered.** That Balaban's lattice β_k → 2 b0 ln L is part of L4a, not reverified.
- **L4c. AF recursion arithmetic: PROVEN-HERE.**
  - Statement: let 1/g_{j+1}^2 = 1/g_j^2 + β_j, with |β_j - β| ≤ C g_j^2, β = 2 b0 ln L > 0, and C g_0^2 ≤ β/2. Then:
    - (a) 1/g_0^2 + jβ/2 ≤ 1/g_j^2 ≤ 1/g_0^2 + 3jβ/2;
    - (b) Σ_j g_j^{2+δ} < ∞ for every δ > 0;
    - (c) Σ_j g_j^2 = ∞.
  - Proof: by induction, g_j ≤ g_0, so β/2 ≤ β_j ≤ 3β/2; sum to get (a). (b) and (c) follow by comparison with
    Σ j^{-1-δ/2} and Σ j^-1. ∎
  - **Consequence used in L7b (heuristic, [R1-fix] softened):** per-scale error *bounds* of order g_j^2 are not
    summable. So a convergence proof by summing absolute per-scale bounds needs geometric decay L^{-κ(j-m)}, or
    O(g_j^{2+δ}). O(g^2) errors could still telescope or cancel; this is not excluded.

### L5. Large-field R-operation: IMPORTED-NOT-YET-REVERIFIED
- **Sources.** CMP 122 (1989) 175-202 [v-abs: "the basic step of the R operation"]; CMP 122 (1989) 355-392 [v].
- **Content (paraphrase).** Large-field regions are suppressed by exp(-c p(g_k)^2 / g_k^2) per unit block, with
  p(g) = (-log g)^p, and are localised and exponentiated.

### L6. UV stability: IMPORTED-NOT-YET-REVERIFIED
- **Statement (paraphrase).** exp(-E_- |T|) ≤ Z_K / Z_K^ref ≤ exp(E_+ |T|), uniformly in K, with bulk dependence on
  the torus size.
- **Dimock's scalar analogue [v-abs, introduction read]:** torus (L^-N Z / L^M Z)^3, bounds "uniform in the ultraviolet
  cutoff N and with bulk dependence on the volume parameter M" (Dimock, arXiv:1212.5562; see also 1108.1335 and
  1304.0705; part III proves "convergence of the expansion" for the stability bound, not of correlations).
- **Correction to review.md §1.** "Small physical volume" is probably a misreading. The restriction is that the
  coupling be small at the stopping scale; the torus side in stopping-scale units is arbitrary (M is arbitrary). Status:
  pending the Balaban primary text.

### L6loc. Local, volume-uniform large-field suppression: OPEN
- **Estimate E8.** There is δ(g) → 0 as g → 0 such that, for every K ≥ m, every M, and every resolution-m block B,
  μ_{K,M}(some averaging step K → m leaves D inside B) ≤ δ(g).
- **Plausible route (not verified).** Ratios of constrained to unconstrained partition functions. In Balaban's polymer
  representation these differ only by polymers touching B. The number of scales is controlled by
  Σ_j L^{4j} e^{-c p(g_j)^2 / g_j^2} < ∞ (L4c(a) with p(g) = (-log g)^p, p > 1/2).
- **What it buys.** It makes the limits in L7a and L8a consistent across resolutions (A_* ν_{m+1} = ν_m, because A is
  continuous on D and D^c has small mass) and non-degenerate. Together with E7.0 it also supplies a K-uniform tuning.
- **[S2] Literature status of E8** (Dimock II, arXiv:1212.5562, full-text HTML read via a summarising fetch: data only,
  paraphrased; scalar φ^4 in 3D, not gauge).
  - Large-field regions are defined by characteristic functions χ, ζ with thresholds p_k = (-log λ_k)^p (§1, eq. 10).
  - Each large-field cube contributes e^{-O(1) p_0^2}, so a region Ω^c carries e^{-O(1) p_0^2 |Ω^c|_M}.
  - The result is a sum over decreasing regions Ω_1 ⊃ Ω_2 ⊃ ..., with exponentially decaying polymer activities.
  - **No local, volume-uniform probability bound of E8 type is stated** in the part read (the first 100k of 159k
    characters).
  - So E8 is NOT already in Dimock I-II as a stated result. The structure (a *local density-level* suppression, plus
    local polymers) is exactly what the E8 route needs: a ratio Z(B forced large)/Z ≤ e^{-c p^2} × (polymer
    correction). Whether Balaban's gauge papers state it is unknown [unverified-exact-statement]; their bodies were not
    read.

### L7. The continuum limit on T^4_M
- **L7.0. Tuning at each fixed K: PROVEN-HERE. Tuning to a K-independent w*: GAP (OPEN, estimate E7.0).**
  [R1-fix: session 1 claimed a fixed w* for all K; that does not follow.]
  - **Definitions.** RC is read with the continuous cut-off observable w̃ = ζ · (1 - N^-1 Re tr V^(0)_p). Here
    ζ ∈ [0, 1] is a continuous gauge-invariant function. It equals 1 when every averaging step inside the four
    resolution-0 blocks of p satisfies ||Z_y - 1|| ≤ τ_N/2, and 0 when some step has ||Z_y - 1|| ≥ 3τ_N/4.
    - τ_N := min(1, 2 sin(π/N)). [R1-fix] For N ≥ 13 the session-1 thresholds 1/2 and 3/4 did not imply D_N.
  - **Statement (per K).** For each K, β ↦ E_{K,β}[w̃] is continuous on [0, ∞) and tends to 0 as β → ∞. Its value
    w̃_0(K) at β = 0 is > 0. Hence every w* ∈ (0, w̃_0(K)) is attained at that K.
  - **The gap.** At β = 0 the links are i.i.d. Haar. ζ = 1 needs about L^{4K} of the Z_y, many with disjoint supports, to
    lie in a fixed ball. So w̃_0(K) → 0 super-exponentially in K, and even sup_β E_{K,β}[w̃] ≥ c > 0 uniformly in K is
    unproven.
  - **Estimate E7.0 (OPEN).** There are c > 0 and β-ranges such that sup_β E_{K,β}[w̃] ≥ c for all K. Its content is a
    large-field suppression statement, of L6/E8 type: with high probability all averaging steps stay in the domain.
    The RC, L7c and LOG decision 1 all need E7.0.
  - **Proof.**
    - Continuity: dominated convergence on the compact configuration space (the integrand is continuous and bounded,
      and the density is continuous in β).
    - w̃_0 > 0: w̃ is continuous, non-negative, and positive on a non-empty open set.
    - β → ∞: by Laplace's principle on the compact space, μ_β concentrates on the flat set {U_p = 1 for all p}.
      - On a flat configuration every Z_y is the holonomy of a null-homotopic loop (zero winding on the torus), so
        Z_y = 1, ζ = 1, and U' = T_{c_X}.
      - Every coarse plaquette is the holonomy of a null-homotopic loop, so it equals 1 and w̃ = 0. This includes flat
        configurations with non-trivial torus holonomy.
      - [R1-fix] Session 1 wrote "contractible union of blocks". That fails when the coarse torus has side ≤ 2; zero
        winding is the correct reason.
    - w̃ is continuous, so E_β[w̃] → 0. Conclude by the intermediate value theorem. ∎
  - That the tuned β_K lies in Balaban's regime for small w* is part of L4a and L6 (imported).
- **L7a. Subsequential limits at every resolution: PROVEN-HERE (content-free alone).**
  - Statement: for any sequence β_K, there is a subsequence along which, for every m, the law ν_{K,m} of V^(m) (a
    probability measure on the compact space C_m = G^{links of Λ_{m,M}}) converges weakly.
  - Proof: Prokhorov on a compact metric space, then a diagonal argument over m ∈ N. ∎
- **L7b. Convergence of the whole sequence: OPEN. The first open estimate of the DAG is E7.**
  - **E7 (trajectory Cauchy estimate).** Assume RC with w* ≤ w_*(N, L). There are κ > 0 and C < ∞ such that for all
    K ≥ m ≥ 0, M ≥ 0, every union X of resolution-m blocks, and every gauge-invariant f : C_m(X) → C with
    ||f||_∞ ≤ 1:
    |E_{K+1}[f(V^(m))] - E_K[f(V^(m))]| ≤ C |X|_m L^{-κ(K-m)},
    where |X|_m is the number of resolution-m blocks in X.
  - E7 is summable in K, so it gives convergence of all of O, with cutoff effects O(ε^κ). It is stated for the
    observable expectations so that it does not depend on Balaban's internal norms.
  - **Sub-estimates (all OPEN).**
    - **E7.1 (one-step comparison).** The (K+1)-theory after one step equals a Wilson action at the tuned coupling plus
      an irrelevant remainder R. R must be measured in Balaban's polymer norm, with size O(g^{2+δ}) or carrying
      L^{-κ}. L4c shows that O(g^2) is not enough.
    - **E7.2 (contraction).** The linearised RG map on Balaban's space of effective actions contracts the irrelevant
      directions by L^{-κ} per step, uniformly for g ≤ g_*, including across the large-field/small-field interface. The
      marginal direction is fixed by RC.
    - **E7.3 (tuning stability).** The tuned β_{K+1} and β_K differ by an amount the marginal flow absorbs, with error
      O(L^{-κK}).
    - **E7.4 (from norms to observables).** A polymer-norm difference of the effective densities on X gives an L^1
      difference of the X-marginals. This is a cluster-expansion ratio bound that uses L6loc.
  - **Note.** In the Dimock/Balaban scalar expositions only the stability bound is proved. No correlation-function
    convergence was found in the abstracts read.
  - **[S2] Toy test of E7 / E7.2: Migdal-Kadanoff SU(2), d = 4, b = 2 (check c7). FINITE DIAGNOSTIC, toy only.**
    - **Map.** Bond moving w → w^{b^2}, then decimation a_n → a_n^{b^2} on the character coefficients. This is an exact
      block map of a hierarchical model [m; exactness for gauge models unverified], and an uncontrolled approximation of
      the real 4D RG.
    - **E7 analogue holds.** Tune a_1 = a* after K steps; the tuned resolution-0 weights converge geometrically in K.
      - The per-step ratio of D_K is 0.067 at a* = 0.6 and 0.0636 at a* = 0.9, tending to b^-4 = 1/16 at weak coupling.
      - Four bare families converge to the same limit with the same rate: Wilson, Wilson + adjoint, a large-field bump
        (factor 3 at θ > 2.2), and heat kernel.
      - The tuned β_K grows linearly in K (asymptotic-freedom-like). The implied MK coefficient 0.0457 is close to
        11·2/(48π^2) = 0.0464. This is not claimed as anything.
    - **Rate explained (derived here at leading order in small t; heuristic, since the re-expansion step is not controlled).**
      - Near a heat kernel K_t, a quartic-Casimir deviation u enters log w as (u/t^2) f(θ/√t).
      - Bond moving multiplies log w by p = b^{d-2} and maps t → t/p. Re-expanded on the new width, it gives
        u → u/p^3.
      - Decimation multiplies both t and u by b^2.
      - In d = 4 (p = b^2): t is marginal and u → u b^-4. The measured 1/16 matches.
      - In the real 4D RG the leading irrelevant (dimension-6) operators contract only like L^-2. So the MK rate is
        faster than the expected true κ = 2 (up to logs).
    - **Large fields in the toy.** The bump's effect falls from 7.6e-5 (K = 1) to 2.2e-9 (K = 3) at a* = 0.6. The power
      w^{b^2} suppresses large θ super-exponentially.
    - **Limits of the toy.** MK has no spatial large-field regions, no small-field/large-field interface, and no
      polymer tails. So it confirms only that the E7 *structure* (RC fixes the marginal direction; everything else
      contracts geometrically; the bare large-field shape is irrelevant) is consistent in an exact block map. It is NOT
      evidence for E7.2 in 4D Wilson theory, and in particular not across the interface.
- **L7c. Non-triviality at resolution 0: CONDITIONAL on E7.0 (moved from PROVEN-HERE). [R1-fix]**
  - w̃ is a function of the fine field, not of V^(0). What holds is E_K[w(V^(0)_p)] ≥ E_K[w̃] = w*, since w ≥ w̃ ≥ 0
    on D. The session-1 "= w*" was wrong.
  - The inequality passes to the limit because w is continuous.
  - So, given a K-uniform w* (E7.0), the limit is not concentrated on pure gauge. This is weak; the meaningful version
    is L10.

### L8. Infinite volume
- **L8a. Subsequential limits as M → ∞: PROVEN-HERE.** The laws of V^(m) restricted to any fixed bounded region form a
  tight family on a compact space. By Tychonoff the product over all links of Λ_{m,∞} is compact, so a diagonal
  subsequence (M_i, K_i) converges for every m. ∎
- **L8b. Invariance: PROVEN-HERE in a narrowed form. [R1-fix: the session-1 statement was WRONG]**
  - The limits are invariant under resolution-m lattice translations (period L^-m), and under coordinate reflections
    through block-aligned hyperplanes (by L9a'), for every m along the subsequence.
  - Proof: weak limits of invariant measures are invariant. The torus measures are invariant, and the block map
    commutes with these operations: translations preserve every finer grid, and reflections are covered by L9a'. ∎
  - **Axis permutations are NOT symmetries of the block laws.** S4 fixes the path order 1, 2, 3, 4, so for a
    permutation R, V^(m)[RU] ≠ R V^(m)[U] in general.
  - Repair option (not done): symmetrise S4 by averaging the logs over all 24 orders. L1a and L1b survive, since an
    average of traceless anti-Hermitian logs is traceless anti-Hermitian, but L1e and L3s' would need re-checking.
- **L8c. RP is preserved: PROVEN-HERE, given L9a (incl. the mixed reflection L9a-m) and L9a'.**
  - For continuous f supported in a positive half-space union of blocks, ⟨θ(f)^* f⟩ ≥ 0 holds at every (K, M) and is a
    closed condition under weak limits. ∎
  - [R1-fix (a)] The fine torus side L^{K+M} is odd. A reflection through a block-boundary link plane therefore fixes the
    antipodal *site* plane: it is a mixed reflection, and L9a-m covers it.
  - [R1-fix (b)] The measurable extension of the block map off D must be chosen θ-covariant. Set every coarse link whose
    averaging step leaves D to 1. This works because:
    - 1^-1 = 1;
    - D is θ-invariant (L9a');
    - so V^(m)[θU] = θ V^(m)[U] holds everywhere.
    Gauge covariance of this extension is not needed for RP.
- **L8d. Uniformity: OPEN.** Non-triviality and consistency in infinite volume need E8 (L6loc) uniform in M.
- **The obstruction, stated exactly.**
  - The RG stops at resolution 0, where g is small. What remains is a lattice gauge theory with compact variables,
    strongly coupled at large distances.
  - Existence of limit points needs no infrared control: L8a is pure compactness.
  - The infrared coupling growth blocks:
    - (1) uniqueness of the infinite-volume state, i.e. independence of the subsequence and of the boundary conditions;
    - (2) clustering (OS4);
    - (3) the mass gap;
    - (4) through (1), the universality route to rotation invariance (L9b-β).
- **What the OpenAI claim must have done (inference, not fact).** Either:
  - (A) stay on T^4. Then OS1 fails, so "OS axioms" would have to be read as torus axioms. Or
  - (B) take infinite-volume limit points by compactness, as here, and solve L9b without uniqueness. Or
  - (C) prove uniqueness on R^4, which seems to require IR control comparable to a mass gap, which is not claimed.
  - (B) is the most consistent with "existence, no mass gap".

### L9. The OS axioms
- **L9a. RP of the Wilson action, link reflection and site reflection: IMPORTED-AND-REVERIFIED.**
  - **Source.** Osterwalder-Seiler, "Gauge field theories on a lattice", Ann. Phys. 110 (1978) 440 [v-R1, via a citing
    paper].
  - **L9a-m. [S2, R1-fix] Mixed reflection on an odd torus: PROVEN-HERE (re-derived).**
    - Setting: θ fixes one link plane Π_l and, antipodally, one site plane Π_s. Assume side ≥ 3, so the two are distinct.
    - Gauge-fix the crossing links at Π_l to 1, by a gauge transformation on the positive-half sites adjacent to Π_l.
      It does not touch Π_s.
    - The links inside Π_s (call them W) are θ-fixed. Links from Π_s into either half belong to that half. Plaquettes
      inside Π_s are functions of W alone.
    - Then e^{-S} = h(W) e^{A_+(U_+, W)} θ(e^{A_+}) Π_{crossing p at Π_l} exp((β/N) Re tr(G_p θ(G_p)^†)), with A_+ real.
    - Expanding the crossing factors as in L9a and using Haar product structure, for every W:
      ∫ θ(F) F̄ e^{-S} dμ(·|W) = h(W) Σ_α c_α |∫ F Ḡ_α e^{A_+} dμ_+(·|W)|^2 ≥ 0, with c_α ≥ 0.
    - The equality uses that θ preserves the measure and fixes W, and that A_+ is real. Integrating over W ≥ 0 gives
      RP. ∎
    - Not separately checked numerically: c4 covers only pure link and pure site reflections.
  - **Proof re-derived (link reflection θ: t → 1 - t, on T^4 or Z^4).**
    - The links crossing the reflection plane(s) are pairwise disjoint edges and contain no loop. A gauge
      transformation supported on the positive half sets them to 1; it leaves gauge-invariant positive observables and
      the measure unchanged.
    - Then e^{-S} = e^{A_+} θ(e^{A_+}) Π_{crossing p} exp((β/N) Re tr(W_p θ(W_p)^dag)), where A_+ is positive-half
      measurable and W_p is a positive-half link.
    - Re tr(W θ(W)^dag) = Σ_{ab} Re(W_ab conj(θW_ab)) is a sum of terms G θ(Ḡ) + c.c.
    - Expanding the exponential gives a non-negative combination of products G_α θ(Ḡ_α). The Haar measure factorises
      as dμ_+ dμ_-, and θ is measure preserving.
    - So ⟨θ(F) F̄⟩ = Σ_α c_α |∫ F G_α e^{A_+} dμ_+|^2 ≥ 0, with c_α ≥ 0 when β ≥ 0. ∎
    - Site reflection is analogous. The plane variables are shared, and the plaquettes in the plane belong to both
      halves; split their weight symmetrically.
  - **Check c4.**
    - Exact enumeration for Z2 on 4×2: the RP matrix is PSD, minimum eigenvalue ≥ -2e-17, for both reflections. The
      non-RP control has minimum eigenvalue -1.5e-2 (link) and -1.7e-3 (site).
    - The SU(2) and SU(3) kernels exp(β Re tr W V^dag) are PSD for β ≥ 0 and not PSD for β = -1.
  - **Note.** β < 0 is *not* a usable negative control for Z2 (observed PSD; presumably a π-flux relabelling, not
    proven).
- **L9a'. Block observables are reflection covariant: PROVEN-HERE.**
  - Statement: for a reflection through a resolution-m block-boundary hyperplane, θ maps O_m(X) to O_m(θX), and
    V^(m)[θU] = θ(V^(m)[U]), with link orientation reversed in the reflected direction.
  - Proof: the complete-axial path between two sites is determined by its endpoints and the fixed order of directions.
    A coordinate reflection preserves that order and maps monotone segments to monotone segments, so it maps
    complete-axial paths to complete-axial paths.
  - For L odd the block centres map to block centres when the plane is a block boundary. Straight legs map to straight
    legs (reversed when the reflected coordinate is μ).
  - Directions other than the reflected one: the path set maps bijectively onto the path set of the reflected link,
    the reference maps to the reference, and the identity is exact.
  - **Reversal (reflected direction μ).** Let the reflected link run from X' to X' + e_μ.
    - Its paths are the images of the original reversed paths T̃_{y} = T_{y-Le_μ}^-1, for y ∈ B(X + e_μ).
    - Its reference is T̃_{c_Y} = T_{c_Y - Le_μ}^-1 = T_{c_X}^-1, because c_Y = c_X + L e_μ.
    - Write Z_y = T_{c_X}^-1 T_y. Then T_{c_X} T_y^-1 = T_{c_X} Z_y^-1 T_{c_X}^-1, and the reversed average is
      T_{c_X}^-1 exp(avg log(T_{c_X} Z_y^-1 T_{c_X}^-1)) = T_{c_X}^-1 T_{c_X} exp(-avg log Z_y) T_{c_X}^-1 = U'^-1.
    - This uses log(W Z W^-1) = W log(Z) W^-1 and log(Z^-1) = -log Z (principal branch on D). ∎
  - **Check c1(f).** Exact to 1e-15 for SU(2) and SU(3), for both the reflected and an unreflected direction.
  - A draft of this lemma wrongly flagged a reference asymmetry; the computation above removes it, see LOG.
- **L9b. Euclidean invariance (OS1): OPEN. This is the hard core.**
  - (α) On T^4 it is false by geometry.
  - (β) Continuum translations. Only translations by multiples of L^-K are exact symmetries. Translation by a general
    vector needs grids offset by fine-lattice vectors. **Estimate E9.1:** for f ∈ O_m(X) with Lipschitz constant 1,
    |E_K[f(V^(m)_{grid+a})] - E_K[f(V^(m)_{grid})]| ≤ C |X|_m (L^m |a|)^γ, uniformly in K, for some γ > 0. E9.1 plus
    L8b gives exact R^4 translation invariance of the limit.
  - (γ) Rotations. There is no lattice rotation beyond the hypercubic group.
    - **Remark R9.1:** averaging the limit over SO(4) gives invariance but destroys RP. A convex combination of
      measures that are RP with respect to different planes is not RP with respect to a fixed plane in general. This is
      not a proof of impossibility, only of the failure of the naive route.
    - **Route γ1 (universality).** The limit on a common continuum state space is independent of the lattice
      orientation. This needs E7 plus discretisation independence, and in infinite volume probably uniqueness (blocked,
      see L8).
    - **Route γ2 (two families).** A rotation-covariant family, e.g. gradient-flow observables at flow time t > 0
      [m: Lüscher, JHEP 08 (2010) 071; reviewer: consistent, not web-confirmed], provides OS1. The block family provides OS2. One must prove that both generate the same
      limit state, i.e. a 4D state space à la Cao-Chatterjee (3D: arXiv:2111.12813 [v], CMP 2024). Flowed observables
      are not exactly local, so they cannot carry RP themselves.
- **L9c. OS0 regularity: OPEN.** The block observables are bounded, so their Schwinger "functions" are bounded, but
  they are not distributions in local fields. OS reconstruction needs a local field algebra with E(4) action. This is
  tied to γ2. E9.1 and E7 are the needed uniform estimates.
- **L9d. Clustering (OS4): OPEN.** Whether RP survives the ergodic decomposition of a translation-invariant RP state is
  [unverified]. Without a gap or uniqueness this is not available.

### L10. Non-triviality (not a free theory): OPEN
The target is a short-distance statement: for example, a connected 4-point function of resolution-m linearised fields,
or the β-function seen in O, differs from the free value at order g_m^4. It needs E7-level control.

### QCD and the GUT (carried from review.md; not attacked)
- **F1.** RP for Wilson fermions: IMPORTED-NOT-YET-REVERIFIED (Osterwalder-Seiler 1978 [unverified-citation]).
- **F2-F4:** OPEN.
- **C1-C4:** OPEN.

---

## 3. Tally (after session 2, with REVIEW_S1 applied)
- **PROVEN-HERE: 17.**
  - Twelve survive from session 1: L0, L1a, L1b, L1c, L3s (weaker analogue), L4c, L7.0 (per-K only), L7a, L8a,
    L8b (narrowed), L8c, L9a'.
  - Five are new in session 2: L1e, R3.1, L3s', L3g(a)-block and L9a-m.
  - L7a and L8a-c are soft statements, content-free without E7, E8 and E9.
  - The substantive ones are L3s/L3s' (scalar, k-uniform, iterated) and L1e (k-uniform sup-curvature control of the
    iterated average, for L ≥ 9).
- **IMPORTED-AND-REVERIFIED: 2.** L4b (b0) and L9a (Wilson RP, pure link and site reflections).
- **IMPORTED-NOT-YET-REVERIFIED: 7.** L1d (reduced by L1e), L2, L3g, L4a, L5, L6, F1.
- **OPEN: 17.** E8 (L6loc), E7.0 (new), L7b (E7, E7.1-E7.4), L7c (conditional on E7.0), L3g-ob (heuristic
  obstruction), L8d, L9b (E9.1, γ), L9c, L9d, L10, F2, F3, F4, C1, C2, C3, C4.
- **Moved by the review:** L7.0 split (its uniform part is now E7.0); L7c to conditional; L8b narrowed.

**First open estimate: E8** (local, volume- and K-uniform large-field suppression). Since REVIEW_S1 it sits upstream of
everything else:
- E7.0, the K-uniform tuning, is an E8-type statement;
- L7c and the cross-resolution consistency of the limit points need it;
- E7.4 needs it.

E7 (convergence; core E7.2) is next. Separately, the gauge-field propagator lane (L3g) is blocked on *revising S4*:
the root-based complete-axial average gives non-H^-1-bounded linearised functionals in d = 4 (L3g-ob).

## 4. Next session
1. **Revise S4** toward Balaban's/Dimock's form: average over the coordinate orders (this also repairs L8b), and use a
   linearisation with straight legs and averaged gauge functions. Then:
   - re-check L1a, L1b, L1e, L3s' and L9a';
   - re-run c6(B') to confirm uniform H^-1 bounds;
   - attempt the L3g(a) gap with a Q-adapted gauge fixing (Q_k λ = 0).
2. **E8 attack.** Prove a one-step local ratio bound, Z(block B forced large-field)/Z ≤ e^{-c p(g)^2} × (1 + polymer
   correction), first in a model where the polymer expansion is explicit (Dimock's scalar setting, then abelian), and
   check it numerically on a small 2D U(1) lattice. Read the rest of Dimock II (characters 100k-159k) and Dimock III
   for any local statement.
3. **E7.2 beyond MK.** Build a hierarchical toy *with spatial structure* (two-site or Dyson-type hierarchical
   U(1)/SU(2), with explicit large-field regions) to test contraction across a small-field/large-field interface. MK
   cannot test this.
4. The Balaban primary texts (CMP 98, 109, 116, 119 and 122) remain unread: paywalled, and no exposition found for the
   nonabelian averaging.
