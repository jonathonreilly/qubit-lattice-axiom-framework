# Check of library/gap-mech-attack-neon.md (FINISH row 1537)

Provenance: Claude Opus 5.5 (configured effort), lane checkout at commit 27ac80562, file under check `library/gap-mech-attack-neon.md` (row 1528, author gemini-4-neon-xhigh via agy). A line-by-line check, not an audit. Overall: CORRECT-NO-ADVANCE.

## Plan

1. Read GOAL.md, FINISH.md 'Rules' and 'Working efficiently'.
2. Read library/gap-mech-attack-neon.md in ranges.
3. Check Theorems 1-5 in the order of the brief, then Theorem 6.
4. Compare COSET-STIFF / COSET-BRIDGE with (PUR-io); bearing on row 1530.
5. Novelty against rows 1011, 1066, 1141, 1244, 1283, 1387, 1442, 1510-1527, registry.
6. RESULT line.

## Progress

Steps 1-9 below, written as each finished.

## Step 1. Theorem 1 (lines 181-215)

**T1(1) bijection and Haar density: HOLDS.** U = [[a,b],[-b̄,ā]]; C(w)A(θ) has a = r e^{iθ}, b = w e^{-iθ}, so w = b a/|a| and θ = arg a are the unique inverse on {a ≠ 0}; the complement {|b| = 1} is a circle, Haar-null. In Hopf coordinates the normalized Haar density is 2 sin α cos α dα dθ/2π dφ/2π; with ρ = sin α, ψ = φ + θ, d(ρ²) dψ/2π = d²w/π. So θ is uniform and independent of w, w is uniform on the disc. Checked by hand.

**T1(2) U(1) covariance (2.2): HOLDS.** g = diag(e^{iχ}, e^{-iχ}) conjugates the (1,2) entry of C(w) by e^{2iχ}; the diagonal parts compose to A(θ + χ_- - χ_+).

**T1(3) plaquette identity (2.4): HOLDS.** Checked every product by hand: A C(w) A^{-1} = C(e^{2iθ}w); C(z1)C(z2) has α12 = r1r2 - z1 z̄2, β12 = r1 z2 + r2 z1; P43^† = [[ᾱ43, -β43],[β̄43, α43]]; (P12 A(θ_p) P43^†)_11 = e^{iθ_p} α12 ᾱ43 + e^{-iθ_p} β12 β̄43; (1/2)tr = Re of the (1,1) entry on SU(2). Orientation U_p = U1 U2 U3^{-1} U4^{-1} matches the stated path.

**T1(4) sixteen masses and P_K: HOLDS AFTER CORRECTION.**
- (2.5) -C(w)A(θ) = C(w)A(θ+π): holds. A centre flip on the slab is θ → θ + π there, w fixed: holds.
- For W ≡ 1 the statement holds, but it is a tautology: the "effective compact U(1) theory" is defined as the θ-marginal of the twisted Wilson measure, so its sixteen partition functions are the Wilson Z^z(v) by the change of variables of T1(1). Its action S_eff^z(θ) = -log ∫ dw exp(β Σ ε_p χ(U_p)) is U(1)-gauge invariant and non-local. Nothing about P_K is learned; proving (PUR-io) for this U(1) theory is proving (PUR-io).
- The extension "for every U(1)-gauge-invariant weight W ≥ 0, π-slab invariant, whose w-integral is identically 1" FAILS as written. First failing line: line 213 ("Consequently, for every ... weight W ... whose w-integral is identically 1"). Inserting W changes Z^z(v) to Z^z(v)·E_z[W], and ∫ W dw = 1 (Haar in w) does not give E_z[W] = 1 under the Wilson law. Counterexample (by hand): fix a plaquette p away from the slab; let c := ∫ sqrt(1-|w|²) d²w/π = 2/3. Averaging the phases of w_1, then w_2 (and w_4, w_3) in (2.4) gives ∫ χ(U_p) Π d²w_k/π = (2/3)^4 cos θ_p, so f := χ(U_p) - (16/81) cos θ_p has w-integral 0 for every θ, is U(1)-gauge invariant and π-slab invariant, and |f| ≤ 97/81. Put W := 1 + f/2 ≥ 0, w-integral 1. Then Z_W^z(v) = Z^z(v)(1 + E_{z,v}[f]/2), and as β → ∞ at fixed lattice χ(U_p) → 1 in law while |cos θ_p| ≤ 1, so E[f] ≥ 65/81 - o(1) > 0. Every Z^z(v) is changed by a factor ≥ 1 + 65/162 - o(1), and P_K = Z_+(2u)/Z_+(u)² changes unless the factors conspire, which a common factor c ≠ 1 already prevents (P_K → P_K/c). Correction: restrict to W ≡ 1, or to weights whose gauge-orbit average is 1 (the Faddeev-Popov form of Theorem 2(1)), not whose w-integral is 1.

## Step 2. Theorem 2 (lines 217-275)

**Definition (2.6): HOLDS AFTER CORRECTION.** (κ/2)|n - Rm|² = κ - κ n·Rm for unit vectors, so the second form of (2.6) has prefactor e^{-κ|E|}, not e^{-2κ|E|}. Same correction in the proof of (3), line 251 ("Z_{O(3)}(U; κ) = e^{-2κ|E|} Z(Ad(U))"). No ratio statement and neither bound of (2.11) uses the prefactor, so nothing downstream changes.

**T2(1) identity (2.7), positivity of the denominator, and (2.8): HOLDS.**
- (1/2)tr(σ3 V σ3 V†) = |a|² - |b|² = 1 - 2|b|² (computed: V σ3 V† = [[1-2|b|², -2ab], [-2āb̄, -(1-2|b|²)]]). With V = g_- U g_+^{-1}, Ad(V)_{33} = (Ad(g_-^{-1}) e3) · Ad(U) (Ad(g_+^{-1}) e3) = n_- · Ad(U) n_+. With |n - Rm|² = 2 - 2 n·Rm this is (2.7).
- g ↦ Ad(g^{-1})e3 pushes Haar to the uniform law on S²; so the gauge average is Z_{O(3)}(U; λ/2) (λ/4 = κ/2). The integrand is strictly positive, so the average is > 0 for every U. Gauge invariance by Haar invariance; centre invariance by Ad(-U) = Ad(U).
- (2.8): insert 1 = (gauge average)/Z_{O(3)}, Tonelli, change U → U^{g^{-1}} (twisted Wilson action, dU and Z_{O(3)} invariant; the seam signs ε_p are gauge invariant), ∫dg = 1, then Theorem 1(1) on the full-measure set U_0^E. Correct and sign-free.
- Prior work: this is the Parrinello-Jona-Lasinio / Zwanziger / Fachin-Parrinello sign-free gauge-fixing construction (gauge-averaged weight normalized by its own orbit integral), here applied to the maximal-abelian-gauge functional. The file credits no one for (2.8). Not new as a method.

**T2(2) gradient (2.10): HOLDS. "Massless w_⊥ at λ → ∞": not proved; relabel ARGUED.**
- Checked by hand: R_13 = -2r Re w, R_23 = 2r Im w (from n_1 - i n_2 = -2ab, ab = rw); R_31 = 2r Re(e^{-2iθ}w), R_32 = -2r Im(e^{-2iθ}w) (from Ad(U)^T = Ad(U†), āb = r e^{-2iθ} w); R_33 = 1 - 2|w|². The first-order expansion of F = (1/2)Σ(1 - n_-^T R n_+) and the sign bookkeeping give (2.10). d*_{2θ} in (2.9) is gauge covariant for charge 2 at e^-. |r - 1| ≤ |w|², so d*_{2θ} w = 0 gives |∇F| ≤ 2d‖w‖³.
- The sentence "the numerator factor e^{-λ‖w_⊥‖²} cancels identically against the leading saddle factor" uses only F_U(e3) = ‖w‖². The denominator is an integral over (S²)^V, not its saddle value: it carries a Hessian determinant, the second minimum n ≡ -e3 (F_U(-n) = F_U(n)), and no statement on when e3 is the global minimizer. So "leaving w_⊥ massless while suppressing longitudinal modes" is a Laplace heuristic. Correction: label that sentence ARGUED.

**T2(3) diamagnetic bound Z_{O(3)}(U; κ) ≤ Z_{O(3)}(I; κ) on even tori with sides ≥ 4: HOLDS.** Checked step by step.
- 3a: gauge fixing of the two crossing sheets (g at x_μ = 1 and x_μ = m; disjoint as m ≥ 2); θ: x_μ ↦ 1 - x_μ maps {1..m} onto {m+1..2m} and each crossing link joins x to θx; the crossing kernel Π_x e^{κ n_x·n'_x} is positive semidefinite (a_ℓ(κ) > 0 by Rodrigues and ℓ integrations by parts; addition theorem; tensor products of PSD kernels are PSD); F_± are real; Cauchy-Schwarz gives (2.14). The reflected configuration has R_e on ν ≠ μ links and R_e^{-1} on μ-links (bond n_{θx}·R n_{θx-μ} = n_{θx-μ}·R^{-1} n_{θx}).
- 3b: both Θ_±R* are maximizers (M² ≤ Z(Θ+)Z(Θ-) ≤ M², M > 0); mirrored interior plaquettes keep flatness; every crossing plaquette becomes I·R·I·R^{-1} = I; the count f(Θ+) + f(Θ-) = 2f(R*) + 2(N_Π - f_Π) ≥ 2f(R*) + 2 is correct. Contradiction stands.
- 3c: a flat SO(3) connection on the torus is gauge equivalent to the one-slice form with commuting holonomies; with the slice at x_1 = 1 inside Λ+, the crossing links are already I, Θ_-R* is flat with H_1' = I and H_j' = H_j (the ν-slice links are copied unchanged), and Z(Θ_-R*) = M. Induct over μ to Z(I) = M.
- The tori of (PUR-io) qualify: n = ℓ b^K with 1024 | ℓ and u = n/512 = 2(ℓ/1024)b^K, so all sides n, u, 2u are even and ≥ 4. Z_{O(3)} ignores the twist (Ad(-U) = Ad(U)).
- The second bound in (2.11), Z_{O(3)}(U; κ) ≤ exp(-(κ/2) λ_min(L_U) |V|), is a pointwise bound on the first form of (2.6): HOLDS.
- (2.12): s ↦ log Z_{O(3)}(A(θ_s)) is smooth with a global maximum at s = 0 (A(θ_0) = I): HOLDS. Reading: the weight 1/Z_{O(3)} favours non-flat fields; in coupling language this lowers stiffness, the anti-screening direction, as stated.
- The name "Brydges-Fröhlich-Seiler" is a loose attribution: their diamagnetic inequality is for scalar (Gaussian/Higgs) fields via Kato; the O(3) bound here is a chessboard (reflection-positivity) argument of the Lieb flux-phase type. Not load-bearing.

**Use of row 1141 (2): HOLDS AFTER CORRECTION.** Row 1141 (2) (`library/gap-crux2-astra62.md` lines 45-51) is a Wilson-probability bound for an R^d cube with **free faces**: with probability ≥ 1 - (2+R)^{-k}, λ_min ≥ c_{d,k}/(1 + b + (log(2+R))^{2/d}). The file only names the combination with (2.11) ("plus Row 1141(2) coercivity bound", lines 233, 433, 494) and never writes it. The correct form: tile the periodic torus by disjoint R-cubes; the torus energy is at least the sum of the free-face cube energies on their internal bonds, so λ_min(L_U^torus) ≥ min over cubes; by a union bound over |V|/R^d cubes, with probability ≥ 1 - (|V|/R^d)(2+R)^{-k},
Z_{O(3)}(U; κ) ≤ exp(-κ c_{d,k} |V| / (2(1 + β + (log(2+R))^{2/d}))). Choose k with (2+R)^k ≫ |V|. As written, the citation applies a free-face cube statement to the torus operator without the tiling and union bound. Also: this gives an upper bound on Z_{O(3)}, so a lower bound on the weight 1/Z_{O(3)}; it is a bound on one factor, not on the effective θ law, and Check 1387 already records that row 1141 (2) also holds in 5D (its line 63). So it carries no selectivity here.

**T2(4) small-λ expansion (2.13): HOLDS AFTER CORRECTION.**
- Leading coefficient checked: 3a_1/a_0 = κ + O(κ³) (Langevin), ∫ n n^T dn = I/3, the oriented cycle gives n_0^T R_1 n_1 n_1^T R_2 n_2 n_2^T R_3^{-1} n_3 n_3^T R_4^{-1} n_0, so the plaquette term is (κ/3)^4 tr(R_p) = κ^4 tr(R_p)/81, and κ = λ/2 gives λ^4/1296. Graph count: ℓ is constant along a cycle (∫P_ℓ P_ℓ' = 0 for ℓ ≠ ℓ'), a vertex of degree one kills the term, and on sides ≥ 5 the only closed graphs with ≤ 5 edges are plaquettes. tr Ad(U) = 4χ(U)² - 1. Correct.
- The text "2-edge double-bond graphs have R_e R_e^{-1} = I" refers to graphs that do not exist on a simple lattice with sides ≥ 5; harmless.
- Gap: O(|V|λ^6) after taking the log needs a convergent cluster expansion with activities uniform in R (true: |P_ℓ| ≤ 1 and a_ℓ/a_0 ≤ κ^ℓ/(2ℓ+1)!!, so Kotecký-Preiss applies at small κ), but no expansion is written. Per the GOAL rules, "standard" is not a step. Correction: write the polymer expansion and its convergence condition, or label the remainder ARGUED. Theorem 5 and §4.2 quote "λ ≤ 1/8" as the convergence range (line 432); no proof of that range is given.
- The coupling β_A: with the Bhanot-Creutz normalization (β_A multiplies tr_A/3), the shift is β_A = -λ^4/432, not -λ^4/1296. The sign (negative) is right. Correction: state the normalization of β_A.

## Step 3. Theorem 3 (lines 279-352)

**T3(1) quadratic split (3.3) and remainder 65/16: HOLDS.** Checked by hand.
- Quadratic part: from (2.4), α12 ᾱ43 = 1 - Σx_k/2 - z1 z̄2 - z̄4 z3 + quartic, β12 β̄43 = (z1+z2)(z̄3+z̄4) + quartic. With ε e^{±iθ_p} = c ± is: the c-part is (1 - c) + (c/2)|(z1+z2) - (z3+z4)|² (expand |S12 - S43|² = Σx + 2Re z1z̄2 + 2Re z3z̄4 - 2Re S12 S̄43); the s-part is -s Im(z1z̄2 + z̄4z3 + S12 S̄43) = -s S_p. No odd terms (the action is even under w → -w, which sends β → -β and keeps α).
- Remainder: δ = 1 - sqrt(1-x) = x/2 + h with 0 ≤ h ≤ x²/2 (equivalent to (x+3)(x-1) ≤ 0 on [0,1]); δ ≤ 5x/8 on x ≤ 1/4; |E12| ≤ x1² + x2²; |a| ≤ (5/4)(x1+x2); α-remainder ≤ (1 + 25/16)Σx² = 41/16 Σx²; S·F cross terms: summing the AM-GM bounds of the eight degree-4 monomials gives (5/32)·8 Σx² = (5/4)Σx²; |F12 F̄43| ≤ (25/64)(x1+x2)(x3+x4)/4 < Σx²/4. Total 65/16.
- "Q_θ is the exact Hessian in w at w = 0 for arbitrary θ": holds; the θ-w mixed second derivatives vanish by w → -w evenness, so Q_θ is the w-block of the full SU(2) Hessian at (θ, 0).

**T3(2) ring identity (3.6): HOLDS.**
- (3.4): θ_p = φ on every (1,2)-plaquette except the corner x1 = x2 = L-1, where θ_p = -φ(L-1) - φL(L-1) = φ - π; with ε_p = -1 there, c_p = cos φ and s_p = sin φ. Other plaquettes: θ_p = 0. Checked.
- Transport: z1 = w_{x,1}, z2 = e^{-2iφx2} w_{x+e1,2}, z3 = e^{2iθ_{x,2}} w_{x+e2,1}, z4 = w_{x,2}. Fourier coefficients g(y), -i e^{-2iφy} g(y) (using 2π/L = 2φL and 2φL² = 2π), g_next(y) in both the bulk and the seam row x2 = L-1 (reindex m = m' - 1), -i g(y). Checked. The two mode expressions (curl and Im S) recomputed by hand and agree. (x2, m) ↦ x2 + mL is a bijection onto Z/L², so ‖w‖² = 2L^{d-1} S_0.
- Off-plane plaquettes: z2 = z4 = 0 and z1 = z3 (not "z1 = z2 = z3 = z4" as line 307 says); curl and S_p vanish either way. Wording slip only.
- GUIDE only: a finite-difference second derivative of the full SU(2) twisted Wilson action along the trial mode on the 2D torus (pure Python, `python3 -I`) agrees with (3.6) to 1e-7 at L = 3, 4, 5, 6; the background action equals L²(1 - cos φ).

**T3(2) bound (3.7) for all L ≥ 3, d ≥ 2: HOLDS AFTER CORRECTION (one slipped constant, conclusion unaffected).**
- (3.8): h1, h2, h3 arguments checked, including h3'' = 1 - e^{-u}(2cos u - 1) and the monotonicity of e^{-u}(1 + sin u) on [0, π].
- Ingredient B: Poisson summation and -Θ' < Θ/(2a) = Θ/(4φ) checked; the Θ'' ratio bound (8/3)·Σ(Xk²)² e^{-Xk²} with X = π²/a ≥ 9π/2 holds (k = 1 term 3.9e-4). Slip: line 331 says 2a n_0 ≥ 20π/9 > 6.98 for all L ≥ 3; for even L ≥ 4, 2a n_0 = 2π < 6.98. Correction: 2a n_0 ≥ 2π, so 1/(1 - e^{-2a n_0}) < 1.002 and Θ - S_0 < 3e^{-17.45} still holds; S_0 ≥ 0.9999 Θ unchanged.
- Ingredient C: Σ sin(2φy) g² = 0 (symmetric R_L for odd L; the one extra point y = L²/2 for even L has sin π = 0); dropping the -(1 - cos)g g_next term and 1 - cos(2φy) ≤ 2φ²y² give (3.9). Checked.
- Ingredient D: the three cases (y ≥ 0 with u = φ(2y+1); y ≤ -1 with k = -y-1, g(y) = e^{-u} g(k), sin(2φy) = -sin(u+φ); wrap y = y_max with g_next = g(y_min)) checked; L = 3 wrap ratio 4e^{-2π}(√2/3)/(π/9)² = 0.0289. Expansion of (φ + φ²(2k+1)²/2)² and each moment bound (Cauchy-Schwarz for odd moments) re-derived; the file's coefficients are upper bounds of the exact ones (e.g. the k³ term has 0.5√3.001, written as √3.001). Evaluated at L = 3 the stated sum is 7.791 < 7.80 (tight but true; all terms increase in φ ≤ π/9). Then Q_kin/(2S_0 L^{d-1}) ≤ 1.9502 φ² cos φ ≤ 1.96 φ sin φ, and Q/‖w‖² ≤ -(1 - 2.2101φ) sin φ. At φ = π/9, 1 - 2.22φ = 0.225 > 1/5.
- GUIDE only: Q/‖w‖² = -0.308 at L = 3 (bound -0.077), -0.183 at L = 4, -0.120 at L = 5, -0.084 at L = 6.
- Meaning: the abelian constant-flux configuration in the n12 = 1 twisted sector is a saddle, not a minimum, of the SU(2) action. This is the lattice form of the known Nielsen-Olesen / 't Hooft-van Baal instability of abelian twisted flux; credit is missing in the file. It is a statement about one classical configuration at w = 0 and carries no information on typical Wilson fields or on P_K.

**T3(3) U(1) contrast and "g = 1 + 1 = 2": HOLDS AFTER CORRECTION (relabel).** The U(1) minimum action βL^4(1 - cos(π/L²)) ≥ 2β is cited from row 1200 Lemma M(b), not re-proved here (not rechecked by me). The g = 1 + 1 = 2 decomposition is a continuum integration by parts with "≈" for the S_p term; it is not a lattice proof, and its numbers are a GUIDE (L = 8 diagonalization). Correction: label (3) ARGUED except the cited U(1) statement.

## Step 4. Theorem 4 (lines 354-381)

**T4(1)-(3) zero-action cube and its monopole charge: HOLDS.** Checked every edge by hand.
- (U_uv)_11 = ψ_u1 ψ̄_v1 + ψ_u2 ψ̄_v2. c+² c-² = 1/6, so vertical edges have (U)_11 = 2c+c- = sqrt(2/3), θ = 0. On CCW horizontal steps q_v = i q_u, so q_u q̄_v = -i; top edges give c+² - i c-² (θ = -arctan(2 - √3) = -π/12), bottom edges c-² - i c+² (θ = -5π/12); c+⁴ + c-⁴ = 2/3 on all twelve edges, so |w|² = 1/3.
- Reversed edge: (U†)_11 = conj(U_11), θ → -θ. Top face -π/3; bottom face (CW from +z) 5π/3 ≡ -π/3; side face x = +1 with boundary (y,z): (-1,-1) → (1,-1) → (1,1) → (-1,1), which is the e_y ∧ e_z = e_x orientation: -5π/12 + 0 + π/12 + 0 = -π/3. The 90° rotation about z multiplies ψ_2 by i at both ends and leaves U_11 unchanged. Q_m = 6(-π/3)/2π = -1.
- Prior work: abelian-projection monopoles of pure-gauge (zero-action) configurations are the known gauge-artifact monopoles of the unfixed abelian projection ('t Hooft 1981; DeGrand-Toussaint counting). The explicit cube is a clean instance. No credit in the file.

**T4(4) flat-plaquette bound |θ_f| ≤ 4πs and the shell bound F_MAG ≥ R/4: HOLDS.** Checked: r1r2r3r4 ≥ 1 - s (Weierstrass), the three cross terms ≤ s/2 + s²/16 ≤ 3s/4, Re A ≥ 9/16 at s ≤ 1/4, |B| ≤ s; the real part of (U_p)_11 = 1 forces cos θ_f > 0, the imaginary part gives |sin θ_f| ≤ 28s/9, hence |θ_f| ≤ 14πs/9. Each edge of a closed shell lies on two of its faces; the shells are edge-disjoint. The hypothesis is that every shell carries charge ±1 and every face is flat (pure gauge).
- The penalty "4λ" is the weight ratio e^{-λ F(U)} relative to the gauge copy U = I; this is right because Z_{O(3)}(U) = Z_{O(3)}(I) for pure gauge U.

**T4(4) "λ = 0 fails (t2) completely": not a theorem; relabel ARGUED.** At λ = 0 the θ-law is the exact Wilson marginal (Theorem 1(4)), in 4D and 5D alike. That zero-action configurations carry abelian monopoles shows that "suppression of abelian monopoles in the unfixed projection" cannot be the selective mechanism. It does not show a test of any stated inequality failing. The aside on 5D at β = ∞ ignores torons (non-trivial flat holonomies on the torus). Correction: label the first and parenthetical sentences of (4) ARGUED.

## Step 5. Theorem 5 (lines 385-422)

**T5(1) all-coupling stiffness identity (4.2): HOLDS (and is generic).** F = -log ∫ e^{-Ψ}, F' = E[∂Ψ], F'' = E[∂²Ψ] - Var(∂Ψ), with Ψ = βS_W + λ‖w‖² + log Z_{O(3)}; everything is smooth on the closed polydisc and Z_{O(3)} ≥ e^{-λ|E|} > 0 (the file writes e^{-2λ|E|}, also a valid lower bound). This is the second-derivative formula for any log-partition function. It holds for any conditional law; nothing about SU(2) enters.
- U(1) bullet: HOLDS AFTER CORRECTION. For a general smooth family, ∂_s² of β Σ(1 - cos θ_p) is β Σ(cos θ_p θ̇_p² + sin θ_p θ̈_p); the file drops the θ̈ term. Correction: state it for linear families (θ̈ = 0), as Theorem 5(2) uses.
- SU(2) bullet: (2.12) is quoted correctly (even torus, sides ≥ 4, at θ = 0 and w = 0). "The pure-flux derivative of the spin term" is -ε cos θ_p θ̇_p S_p for the quadratic part of (3.3) only, at fixed transported z; S_p and R_p also depend on θ through e^{2iθ} in z2, z3. As a definition of which part is meant: holds.

**T5(2) normalization of the one-loop 4D, 5D and U(1) terms: HOLDS AFTER CORRECTION.**
- Gaussian law: with unitary Fourier modes, β Q_0(w) + (β/2)‖d*w‖² = (β/2)Σ k̂² |w_k|² per component, so the stated law is the Feynman-gauge one; Re and Im parts have variance 1/(β(k̂² + M²)), C_k = 2/(β(k̂²+M²)) I. Checked.
- X: w†σ2 w = -2 Im(w1 w̄2) = -1 on the LLL spinor (1, -i)/√2. At k = 0 I recomputed the lattice symbol of Σ_x S_p at θ = 0: the |w_a|² terms are odd in k and the cross term is Im[ζ(1 + e^{-ik1} + e^{ik2}) + ζ̄ e^{i(k1-k2)}] with ζ = w1 w̄2, which is 2 Im ζ = -w†σ2 w at k = 0. So the S_p part is exactly one unit of 2σ2/2 at k = 0, the stated "g_anom = 1". The lattice symbol is k-dependent away from k = 0.
- Variance: complex circular Gaussian modes w_k are independent for all k (no reality constraint); Var(w†Aw) = tr((CA)²); A = 2σ2, tr A² = 8; Var(X) = 32 L^{-4} Σ_k (k̂² + M²)^{-2}. Checked; β cancels.
- 4D: 32 ∫ d⁴k/(2π)⁴ |k|^{-4} over c0/L ≤ |k| ≤ 1 = 32 · 2π²/(16π⁴) · log L = (4/π²) log L. The k = 0 mode gives 32/c0⁴. With β = 4/g² and b_0 = 11/(24π²) for SU(2), β(L) = β - 8b_0 log L = β - (11/(3π²)) log L, and 11/3 = 4 - 1/3 is the Nielsen-Hughes spin/orbital split. So the 4/π² spin normalization is right.
- 5D: L^{-4} Σ_k = L · L^{-5} Σ_k, so 32 L^{-4} Σ = c5 L + O(1); the central cell is O(1/L) in 5D; the mass shift 2m²(k̂²)^{-3} and the cell Taylor error L^{-7}|k|^{-6} each sum to O(L^{-1}). Checked. So (β - c5)L + O_{c0}(1).
- U(1): no w, so zero. SU(N): Σ_{α>0} α(H)² = N tr H² (half the Killing sum 2N tr H²); relative factor N/2 to SU(2). Checked.
- Corrections. (a) (4.3) is exact for the model coupling X with an imposed Feynman-gauge Gaussian law. It is not the conditional law of (4.1) (which has the Soft-MAG factor and the ghost denominator, and no Feynman gauge term), and X is the k = 0 symbol, not the lattice spin coupling; the lattice symbol changes only the O(1) term, not the log coefficient. Title "exact 4D vs 5D vs U(1) separation" should read "one-loop Gaussian model computation". (b) "Combined with the net orbital + ghost screening +1/(3π²) log L" is quoted from Nielsen-Hughes, not computed here; the "exact 100% match" note is the known one-loop coefficient. (c) The 5D statement bounds only the spin piece; the orbital and ghost pieces also give O(L) shifts, so "β > c5" is not the 5D one-loop threshold.
- What it carries: the one-loop asymptotic-freedom coefficient, already on file as row 1244 Proposition 2.3 / Check 1527 §(iv) ("100% Gaussian recovery of the 4D paramagnetic spin bubble"). No non-perturbative content.

## Step 6. The obligations and Theorem 6 (lines 425-460)

**Defect D1, COSET-STIFF as written (line 440): FAILS (not a statement).** "There exist ... a gauge-invariant blocked Abelian stiffness functional x_Ab(k) ... such that x_Ab(k+1) ≤ 2^{d-4} x_Ab(k) - δ_0." The functional is existentially quantified and never defined. With x_Ab free, x_Ab(k) := C - δ_0 k satisfies (4.6) in every model, in every dimension. So COSET-STIFF as written is trivially true and every selectivity or separation claim about it is empty. Neither δ_0 > log 2/4 ≈ 0.173 nor x_E is derived anywhere in the file, and the blocking map is not named. Correction (unproved): fix x_Ab, e.g. x_Ab(k) := 1/(second derivative of F_Ab^(λ_k) of (4.1) along a unit twist on the Q2-blocked torus of side 2^k), fix the blocking map and λ_k, and derive δ_0 and x_E from the consumer. Until then COSET-STIFF is a schema of the K-I carry of row 1386 §4.4, not an obligation.

**T6(1) sufficiency of COSET-BRIDGE: HOLDS AFTER CORRECTION; COSET-STIFF is idle.**
- Consumers named in the file: branch (a) END-K2 (row 1471, checked in row 1473: holds after correction) together with "Fact PUR / Check 1527 §(ii)"; branch (b) (RATE-io) of Check 1516 §(iv).
- Testing the hypotheses. Branch (b): Theorem 2(1) gives E_{SoftMAG}[O] = E_Wilson[O] for every gauge-invariant O (insert O into the derivation of (2.8)). So "exponential decay of local gauge-invariant correlations of the Soft-MAG law at physical rate m_0" is the Wilson statement. To match Check 1516 §(iv), it must hold on an infinite set of least-root cutoffs, on all sufficiently large ordinary periodic cubes, for the gauge-invariant local test class with reflections and arbitrary time translates, with liminf b^K λ_K ≥ m_0; the file's "uniform-in-volume ... at physical rate m_0 at scale R_0" needs these clauses written in. Then (b) is (RATE-io) itself. Branch (a): END-K2 is a statement about a **rule** (a Q2-blocked weight) of weighted norm ≤ ε_E on the sixteen twisted tori with v ≥ v_E(m) (least v = 242 at m = 512v), with the common-lift restriction found in check 1473. The Soft-MAG law (2.8) carries a non-local ghost denominator and is not a rule in that class. Since P_K reads only the sixteen Z^z(v), and these are the Wilson ones, branch (a) has to be stated as: the Q2-blocked Wilson rule at scale R_0 lies in the END-K2 class. That is the end of the Q2 chain, which row 1471 says "has no method" from β ≈ 2.3 to β_E. Check 1527 §(ii) (changed aspect) is not needed for (a).
- Consequence: with these corrections, SOFT-MAG-MIX alone implies the gap; the COSET-STIFF conjunct is never used. Sufficiency holds and is immediate from the consumers on file.

**T6(2) separation of COSET-STIFF from (PUR-io) by a neutral spectator: HOLDS AFTER CORRECTION (conditional, and not new).** The arithmetic holds: P_K ≤ 1 for a commuting centre (Σλ^{2u} ≤ (Σλ^u)²); a decoupled centre-trivial spectator diag(1, 1-η_n) with η_n u → 0 multiplies P_K by (1 + (1-η)^{2u})/(1 + (1-η)^u)² → 1/2, so P_K → ≤ 1/2 < 457/625; derivatives of the abelian free energy are unchanged. But the conclusion "COSET-STIFF does not imply (PUR-io)" needs a model in which COSET-STIFF holds; Wilson ⊗ spectator satisfies it only if Wilson does. Correction: "if COSET-STIFF (with a fixed x_Ab, see D1) holds for Wilson, then Wilson ⊗ spectator satisfies it and fails (PUR-io)". This is the spectator test of row 1025 (FAC) and Check 1527 §(vi), as the file says.

**T6(3) "(PUR-io) holds while COSET-STIFF fails" in the gauge-matter class: FAILS.**
- Model A (line 451): first failing step "with no weak-coupling band and no decrement δ_0, so COSET-STIFF fails". If the stiffness starts below x_E, the clause "throughout the band from the weak-coupling window down to x_E" has no instance, so COSET-STIFF holds vacuously; with D1 it holds trivially anyway. The (PUR-io) half is right in substance: β_0 = 10^{-4} is below the sharp END-K2 entry supremum log(1 + 1/(42e)) ≈ 0.00872 of check 1473 at a suitable strength, and v = u → ∞ ≥ 242. END-K2 gives P_K ≥ 457/625, not P_K → 1 as written.
- Model B (line 452): first failing line "so on large tori P_K → 1 > 457/625 ((PUR-io) holds)". A fundamental Higgs term breaks the centre: under the slab flip U_e → -U_e, χ(φ†Uφ) changes sign and no periodic φ absorbs it, so C_z does not commute with T, the class premise of item 2 ("commuting Z_2^3 centre action") fails, and P_K ≤ 1 is lost. Heuristic counterexample to the stated value (ARGUED, not proved): in the deep Higgs phase the twisted Z^z(v), z ≠ 0, carry a seam cost of order κ n², so Z_+(v) ≈ Z^0(v)/8 and P_K ≈ 8 Z^0(2u)/Z^0(u)² → 8, not 1. Osterwalder-Seiler 1978 gives no statement on P_K. The "COSET-STIFF fails" half is the one-loop heuristic m_W² = κ/β with x_Ab undefined (D1).
- Even if repaired, (3) would show only that (PUR-io) does not imply COSET-BRIDGE in an enlarged class, i.e. that COSET-BRIDGE is not weaker. It does not bear on whether COSET-BRIDGE is easier.

**T6(4) selectivity audit.**
- (t1), (t6) compact and Villain U(1): HOLDS AFTER CORRECTION. With no W-bosons the abelian stiffness of 4D U(1) does not run at weak coupling, consistent with Guth and Fröhlich-Spencer, so any honest x_Ab shows no decrement. The file's reason (w ≡ 0, δ_0 = 0) is one-loop; the non-perturbative fact is the cited literature. With D1 unrepaired the test is empty.
- (t2) 5D SU(2): HOLDS AFTER CORRECTION (relabel GUIDE). The 5D argument is the one-loop Gaussian spin piece (4.5) only (orbital and ghost O(L) shifts omitted), and weak-coupling 5D SU(2) being Coulomb is believed, not proved. Also, (4.6) with 2^{d-4} = 2 is a non-contracting recursion, so COSET-STIFF itself may hold in 5D (the O(1) terms of (4.5) decide x(k+1) - 2x(k)); what fails in 5D is "reaching x_E", i.e. COSET-BRIDGE. The selectivity sits entirely in the hand-inserted factor 2^{d-4} and the assumed gain δ_0, the pairing of Remark PAIR. Nothing in Theorems 1-5 supplies δ_0 beyond one loop.
- (t3) SU(N): FAILS as "passes cleanly" (line 457). The flat-disc Haar density of Theorem 1(1) is a property of SU(2) → S² (the Hopf fibration; Archimedes' area law), which is the kind of N = 2 coincidence (t3) warns against; Theorem 2(3)'s O(3) chessboard proof, (2.13) and Theorem 4 are not given for the flag manifold SU(N)/U(1)^{N-1}. Only the one-loop C_A = N scaling of Theorem 5 is shown. Correction: label ARGUED; the flatness is not load-bearing (any smooth density would do), but the ghost bound must be re-proved.
- (t4) growing β at fixed (n, u): HOLDS as inherited from the consumers. A fixed box allows log_2 n doublings, and the consumers fail there by rows 1143/1144, 1215, 1227 and Check 1387 §6, as the file cites. The mechanism itself contributes nothing to this test.
- (K7): FAILS as a selectivity claim (line 459). K7 is excluded only because SOFT-MAG-MIX assumes unique-phase mixing: the test is passed by hypothesis, as Obstruction (O3) concedes. The remark on β_A = -λ^4/1296 concerns a small-λ shift of the ghost factor, which does not alter the Wilson law at all (Theorem 2(1) is an identity), so it cannot move the Wilson axis toward or away from the K7 line.

## Step 7. COSET-STIFF and COSET-BRIDGE against (PUR-io), under "Equivalent is not progress"

- **COSET-STIFF.** As written (D1) it is trivially true, so it is strictly weaker than everything and carries nothing. With x_Ab fixed as in the D1 correction it is not a sufficient statement (the file says so, and T6(2) shows why conditionally). No implication in either direction with (PUR-io) is proved. It is the K-I carry schema of row 1386 §4.4 specialised to the Soft-MAG abelian law. It is a component, not a reduction, so the rule does not apply to it as a sufficient condition; it moves no open obligation.
- **COSET-BRIDGE.** By T6(1) it is COSET-STIFF ∧ SOFT-MAG-MIX, and SOFT-MAG-MIX alone is sufficient: branch (b) is (RATE-io) of Check 1516 §(iv) verbatim once the clauses are written in, which is the lattice form of the physical mass gap, i.e. equivalent to the open target; branch (a) is the END-K2 entry hypothesis on the Q2-blocked Wilson rule at scale R_0, the open end of the Q2 chain on file (row 1471). So COSET-BRIDGE is **stronger** than an on-file sufficient statement (it adds a conjunct the consumer never uses), and its operative part is equivalent to the target or to an on-file open step. Under the rule: **no progress**. The file's own scope note (inside Wilson it cannot show non-equivalence) is accurate; its class separations do not change this (T6(2) conditional; T6(3) fails).

## Step 8. Bearing of COSET-STIFF on row 1530 (`library/gap-mech-attack-astra62.md`, unchecked)

Row 1530 (lines 20-60, 193-201) tests a Gaussian spin response X(U,h) = (1/2V) Tr(Γ M_h Γ M_h) with Γ = (H + n^{-2})^{-1}, H the adjoint covariant Laplacian of a **typical Wilson background** at β_K, and claims sup_h X ≤ C_k(1 + log(1 + β)) with high probability in 4D (its (2)), via row 1141 (2) coercivity H ≥ c/(1+β) on Neumann cubes (its (3)), so the bare spin response is O(log β_K), not O(log n), and vanishes on a shell at the seed scale.
- Same object, different background. Neon's Theorem 5(2) computes the same g = 2 spin variance (A = 2σ2 against ad h with M_h = -2J ⊗ ad h) about the **flat** background θ = 0, w Gaussian with the free propagator and IR cutoff c_0/L, and gets (4/π²) log L. Row 1530 computes it about the **rough** background, where row 1141 (2) cuts the IR log at L ≈ sqrt(1+β). The two are consistent; neither is the conditional law of (4.1).
- Consequence for COSET-STIFF: Theorem 5(2) cannot supply δ_0 at the bare lattice scale. If row 1530 holds, the bare typical-field spin gain accumulated across the band is O(log β_K) = O(log log n), not order one per doubling across log n doublings. The decrement would have to come from the blocked law at each scale, where the background is smooth at the block scale: that is a K-II step (an RG step at order-one coupling, row 1386 §4.4), the open core. Neon's own use of row 1141 (2) in (2.11) is the same coercivity input that row 1530 uses to kill the bare response.
- This is conditional on row 1530, which no one has checked; I did not check it.

## Step 9. Which of the seven approaches are new relative to the files

- **1 (Cartan-coset / Soft-MAG):** partly new to the files. On file: abelian projection and MAG heuristics (11 and 8 library files, e.g. `library/gap-aligned-frame.md`, `library/gap-measured-assumptions-opus.md`), Nielsen-Olesen (10 files), and the normalized gauge-averaged (Zwanziger / Parrinello-Jona-Lasinio) kernel as C7 of row 1013 (`library/gap-invent-selective-max.md` lines 124, 197, 266, with a different gauge functional). New to the files: the coset coordinates with (2.4), the MAG version (2.7)-(2.8), the O(3) chessboard bound (2.11), the lattice ring proof (3.7), the monopole cube. None is new to the literature (Kronfeld-Schierholz-Wiese MAG; Parrinello-Jona-Lasinio, Zwanziger; Nielsen-Olesen, van Baal; 't Hooft abelian projection), and the file credits none of these for its theorems. The cited "Ding-Huang-Yang arXiv:2611.04908" was not verified by me.
- **2 (gradient flow):** not new. x_fl and Identity FLOW are row 1390 D6 (`library/gap-dim-carry-fable.md` lines 202, 205).
- **3 (Ward-cancelled paramagnetic stiffness):** not new; a repair of row 1526 Approach 1 after Check 1527, of kind K-I (row 1386 §4.4).
- **4 (multiscale Dobrushin-Shlosman / in-law Poincaré to (RATE-io)):** not new; rows 1510, 1511, 1514, 1516.
- **5 (self-dual 2+2 bridge from 2D O(4)):** not new as a direction (row 1139 / row 1141 opening (a), row 1526 Approach 6 refuted by Check 1527 §(vii)(6)); the symmetric two-endpoint path is a new variant, untested.
- **6 (TWO-PER / TR2):** not new; Check 1516 §(v), Check 1521 (52 files mention TWO-PER).
- **7 (blocked x_adj):** not new; row 1390 §4.1 table (x_adj), rows 1141 (2), 1283 (7)-(8), Check 1387.
- Registry: `library/open-registry.md` has no MAG/Soft-MAG entry (grep).

## Summary of verdicts

| Part | Verdict |
|---|---|
| T1(1) bijection, Haar density | HOLDS |
| T1(2) U(1) covariance | HOLDS |
| T1(3) plaquette identity (2.4) | HOLDS |
| T1(4) sixteen masses, P_K | HOLDS AFTER CORRECTION (W ≡ 1 only; tautological; general-W clause FAILS, counterexample given) |
| (2.6) prefactor | HOLDS AFTER CORRECTION (e^{-κ|E|}) |
| T2(1) (2.7), positivity, (2.8) | HOLDS (known PJL/Zwanziger construction) |
| T2(2) gradient (2.10) | HOLDS; "massless w_⊥" ARGUED |
| T2(3) diamagnetic bound and reflection proof, (2.12) | HOLDS |
| T2(3) use of row 1141 (2) | HOLDS AFTER CORRECTION (tiling + union bound; not selective) |
| T2(4) small-λ adjoint shift | HOLDS AFTER CORRECTION (cluster expansion not written; β_A normalization) |
| T3(1) split, remainder 65/16 | HOLDS |
| T3(2) ring identity (3.6) | HOLDS |
| T3(2) Nielsen-Olesen bound (3.7), L ≥ 3, d ≥ 2 | HOLDS AFTER CORRECTION (2a n_0 ≥ 2π slip) |
| T3(3) g = 1 + 1 = 2 | HOLDS AFTER CORRECTION (relabel ARGUED) |
| T4(1)-(3) cube, Q_m = -1 | HOLDS |
| T4(4) penalty bounds | HOLDS; "λ = 0 fails (t2)" ARGUED |
| T5(1) identity (4.2) | HOLDS (generic); U(1) bullet needs θ̈ = 0 |
| T5(2) 4D, 5D, U(1) normalization | HOLDS AFTER CORRECTION (model Gaussian, k = 0 symbol, orbital/ghost cited) |
| COSET-STIFF as stated | FAILS (undefined existential functional; trivially true) |
| T6(1) sufficiency | HOLDS AFTER CORRECTION (SOFT-MAG-MIX alone suffices) |
| T6(2) spectator separation | HOLDS AFTER CORRECTION (conditional; on file) |
| T6(3) Models A, B | FAILS |
| T6(4) (t1)/(t6), (t2), (t4) | HOLDS AFTER CORRECTION / inherited |
| T6(4) (t3) | FAILS as "passes cleanly" |
| T6(4) K7 | FAILS (passed by hypothesis) |

Scope of this check: lines 1-44 (setup), 45-69 and the openings of Approaches 2-7 (lines 70-154, read for novelty only), 175-494 (Theorems 1-6, read line by line). Not checked: the bodies of Approaches 2-7, the comparative table (lines 155-174), the credits list (lines 478-486). Row 1530 was read only at lines 1-60 and 193-201 and was not checked. Python (`python3 -I`, pure, no numerics library) was used only as a GUIDE for (3.6), (3.7) and the 7.80 sum.

RESULT: Theorems 1-5 of row 1528 hold as algebra and analysis after small corrections (W ≡ 1 in T1(4), e^{-κ|E|} in (2.6), the 2a n_0 slip in (3.7), relabelling the heuristic parts ARGUED), and the O(3) reflection-positivity bound and the all-L lattice Nielsen-Olesen bound are correct; but every one of them is an identity or a one-loop or single-configuration statement, COSET-STIFF as written is an undefined existential (trivially true), COSET-BRIDGE is sufficient only through its conjunct SOFT-MAG-MIX, which is (RATE-io) or the END-K2 entry on file, so it is stronger than an on-file sufficient statement and is no progress under "Equivalent is not progress"; the class separation of T6(3) fails (Model A vacuous, Model B breaks the centre symmetry), and the (t3) and K7 audit items fail; (PUR-io) is not moved, and of the seven approaches only Approach 1 is new to the files (not to the literature).
Checked line by line by Claude (Opus 5.5).
