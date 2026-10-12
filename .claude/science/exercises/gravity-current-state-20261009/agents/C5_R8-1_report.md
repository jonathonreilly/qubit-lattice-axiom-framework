# C5 R8-1 report: repair and extend R7-1's interacting two-body box sector (P2)

**Author.** Claude Opus 5.5 probe (same family as the supervisor, R7-1's worker and every C5 worker). Unrefereed. 2026-10-12, 15:38Z to about 16:25Z. No repository file edited.
**Scratch.** `S/` = `.../scratchpad/C5/R8-1/`. Scripts and outputs are in `S/scripts/`:
- `r81_common.py`: the box law and the exact smooth BT kernel; `r81_kernel_check.{py,out}` checks the kernel;
- `r81_fock_norm.{py,out}`: the quartic prefactor;
- `r81_d1_ring.{py}` with `_L512.out`, `_L1024.out`, `_L2048.out`: the d = 1 lattice ring, K built and commutators checked;
- `r81_d2_chart_algebra.{py,out}`: the d = 2 chart identity and all 12 relations;
- `r81_d2_lattice_mass.py` with `_L64.out`, `_L128.out`, `_L192.out`: the d = 2 lattice spectrum;
- `r81_d2_lattice_algebra.py` with `_L*_NP*.out`: the d = 2 direct lattice run, which is resolution-limited;
- `r81_leak.{py,out}` and `r81_leak_NP960.out`: finite interacting boosts.

**Read.** `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full. `TESTS.md:2302-2440` (C5 method and round 1), `:3009-3100` and `:3240-3481` (rounds 6–8, the R7-1 referee results, R8-1). `agents/C5_R7-1_report.md`, in full. `agents/C5_R7-1_referee_verdict.md`, in full; only the verdict file exists, with no separate `C5_R7-1_referee*.md`. `scripts/C5/R7-1/r71_bt_twobody.{py,out}` and `r71_box_poincare_free.py`, plus the referee's `ref_R7-1/scripts/r71_referee_checks.{py,out}`. R7-6's in-progress scratch (`C5/R7-6/scripts/r76_threebody_naive.py`, the three-body problem) was skimmed for overlap only.
**Literature.** Keister–Polyzou arXiv:1109.6575: verified by web fetch that its abstract states that BT dynamics is Poincaré invariant but fails cluster separability for N ≥ 3. Bakamjian–Thomas 1953 and the BT canonical form H = √(M² + P²) are cited by the referee from Polyzou's notes, eqs. (136)–(140); I did not re-fetch these (RECALLED/cited). The spin-term form below is **derived here**, not taken from the literature.
**Labels.** proved / checked (numerics here) / suggested / reading / comparator / RECALLED.

---

## 0. In plain words

- **The repair works in d = 1 and d = 2.**
  - Of the referee's three defects, the boost sign is real and repaired, and the global symmetry gap is real and repaired.
  - The "¼ prefactor" is **not** a defect. It is a convention mismatch. With the ordered-pair kernel that the runner and BT actually use, ½ is right. ¼ is right only if the kernel is normalised on unordered pairs. Decided by exact spectra (`r81_fock_norm.out`).
- **The boost is built and checked, d = 1.** It is the global, symmetric lattice operator K = ½{H, X_P}, with X_P = Σ_i ½{ε_i/H₀, X_i} the lattice centre-of-energy position. On the lattice ring the relations [K, P] = iH, [K, H] = iP, [H, P] = 0 close to 1e-11–3e-8 at L = 2048. The residual falls about 1000× per doubling of L. The comparators (R7-1's printed sign; the free boost) fail at O(1).
- **The boost is built and checked, d = 2 with rotations.**
  - Channel: a p-wave doublet, g_a(q) = q_a b(|q|²). It is odd, so fermionic, and rotation invariant, so it commutes with the pair's internal spin S.
  - The repaired boost is K_a = ½{H, X_NW,a} + ε_ab P_b S/(M + H). The spin term's coefficient is fixed by [K_x, K_y] = −iJ (proved).
  - All 12 relations close to ≤ 6e-13 in the canonical chart.
  - The lattice free generators equal the BT free generators in that chart to 1e-14.
  - On the lattice the bound doublet's invariant mass is the same at every P, magnitude and direction, to 1.2e-8 at L = 192, converging. The Galilean comparator drifts by 9e-2.
  - Without the spin term, or with R7-1's single rank-one channel, the algebra fails at O(0.1–1).
- **Interacting leakage: proved, checked.**
  - Statement: ‖e^{−iηK}ψ − U_BT(η)ψ‖ ≤ 2‖(1 − E)ψ‖. Here E = 1_I(P) 1_Σ(M) is built from the total momentum and the pair's internal-mass spectrum. The BT orbits of I × Σ over [0, η] must stay on the plateau.
  - A compactly supported bound-state packet shows zero leakage (to the 5e-8 discretisation floor) until the predicted η*, then leaks.
  - A mixed packet obeys the optimised bound at every η.
- **What is not shown:**
  - N ≥ 3 (R7-6's item);
  - d = 3 (suggested: the same construction with a p-wave triplet);
  - interacting stress tensors and Ward identities (W1–W4);
  - universal coupling (R8-2);
  - loops (R7-5);
  - the ungraded ⊗M₂ version.

  In d = 2 a direct lattice-native run of all 12 relations was attempted but is resolution-limited at feasible sizes (§4.6).

---

## 1. Hypotheses and classes (stated before any title)

- **H-lat (as R7-1).**
  - One complex fermion mode per site of Z^d, d = 1, 2, with the graded tensor product. One-site algebra M₂(C) (`AX:48`); cross-site composition graded, as R7-1's PASS clause allows (`TESTS:3254`).
  - Continuous time: the Hamiltonian is on Z^d × ℝ.
  - One-body box law: s(k) = k and ε̃ = √(m² + |k|²) on |k_i| ≤ B = 2.6, extended smoothly and periodically (R7-1 §3).
- **H-2.** The interacting statements concern the **two-particle sector**. The second-quantized law acts in every N-sector pairwise. N ≥ 3 closure is not claimed (R7-6).
- **H-int.**
  - BT mass operator M = M₀ + V, with V = λ Σ_a |g_a⟩⟨g_a| in the canonical relative momentum q.
    - d = 1: g(q) = (q/κ) sstep(1 − q²/κ²), with κ = 0.4.
    - d = 2: g_a = q_a b(|q|²), with b = sstep(1 − |q|²/κ²)/κ and κ = 0.8.
    - λ is tuned to M_b = 0.85, with m = 0.5.
  - Plateau: c(|P|) = 1 for |P| ≤ Π₁, and 0 for |P| ≥ Π₂.
    - d = 1: Π₁ = 0.6, Π₂ = 1.2.
    - d = 2 spectrum run: (0.6, 1.2). d = 2 direct run: (1.0, 1.4).
  - Interaction legs are inside |k_i| < 2.0 (2.4 in the direct run) < B, with no umklapp.
- **H-gen.** "Exact algebra" means operator identities on the common invariant domain 𝒟₂: antisymmetric C_c^∞ two-particle wavefunctions supported in R′ = {|P| < Π₁, legs in the box, no umklapp}. As in R7-1, integrability to a unitary representation on the box is **not** claimed (B1 Theorem U; referee §1).
- **Excluded realizations (not addressed):**
  - N ≥ 3;
  - d = 3 (suggested only);
  - pair creation and loops;
  - gauge fields;
  - the local-lapse algebra;
  - set B (Euclidean Z⁴);
  - LRL;
  - ungraded qubit realizations.

## 2. Prior art (each counted once)

- **R7-1 P2.**
  - The law: `C5_R7-1_report.md:73-81`.
  - The printed boost: `:146-147`.
  - N ≥ 3 open: `:163-167`.
- **R7-1 referee.**
  - Sign defect: `C5_R7-1_referee_verdict.md:108-113`.
  - ¼ prefactor: `:114-122`.
  - Unsymmetrised cutoff: `:124-129`.
  - d ≥ 2 needs a rotational multiplet: `:100-104`.
  - Interacting leakage "asserted but not proved": `:168-171`.
  - The runner never builds K: `:139-146`.
  - Independent checks: `ref_R7-1/scripts/r71_referee_checks.out:1-6`.
- **R7-1 P1** (free, every N; CONFIRMED) and the free leakage bound 2‖1_E ψ‖ (`TESTS:3398-3403`): used as the free half here.
- **R7-6** (in progress, unrefereed): three-body closure of the pairwise BT law. Not overlapping.
- **Keister–Polyzou** (web-verified abstract): BT is Poincaré invariant with a broken N ≥ 3 cluster property. Consistent with H-2.

---

## 3. The repaired law

### 3.1 d = 1

- **H.** H = H₀ + W.
  - H₀ = ε̃(k₁) + ε̃(k₂).
  - W(P) = c(P)[√(M² + P²) − √(M₀² + P²)] in the half-density chart (P, q).
  - q = m sinh((θ₁ − θ₂)/2) and M₀ = 2√(m² + q²).
  - On the lattice: W(P; k₁′, k₁) = c(P) w(P; q′, q) √(q_k′ q_k).
- **The kernel w is exact and smooth (proved, algebraic).** By Woodbury,
  - √A − √A₀ = (1/π)∫₀^∞ t^{1/2} R_t U (C⁻¹ + UᵀR_tU)⁻¹ Uᵀ R_t dt;
  - with U = [g, M₀g], C = [[λ²‖g‖², λ], [λ, 0]] and R_t = (M₀² + P² + t)⁻¹.

  So w = g(q′)g(q) Ω(P; q′, q), with Ω smooth and supp w ⊂ supp g × supp g. Checked against Nyström diagonalisation to 7e-15 absolute, 1e-11 relative (`r81_kernel_check.out`).
- **The boost** (built here, global, symmetric):
  - **K = ½{H, X_P}**, with **X_P = Σ_i ½{ε̃_i/H₀, X_i}** and X_i the lattice site positions.
  - Equivalently K = K₀ + ½{W, X_P}, because K₀ = Σ_i ½{ε̃_i, X_i} = ½{H₀, X_P} exactly. That is an anticommutator identity for commuting multiplication operators (proved).
  - In the chart, X_P = i∂_P|_q. Reason: X_P is i × (the Lie derivative on half-densities) along u = (ε₁∂₁ + ε₂∂₂)/H₀, which is the free-boost field divided by H₀, i.e. ∂_P|_q (proved).
- **Second quantization** (product-basis kernels, §4.1):
  - H_int = ½ Σ_{P,k₁′,k₁} W(P; k₁′, k₁) a†_{k₁′} a†_{P−k₁′} a_{P−k₁} a_{k₁};
  - K_W = ½ Σ ⟨k₁′k₂′|½{W, X_P}|k₁k₂⟩ a†_{k₁′} a†_{k₂′} a_{k₂} a_{k₁};
  - in real space, K_W is the first moment of a quasi-local two-body density.

### 3.2 d = 2

- **Canonical chart.** q = k₁ + P[(P·k₁)/(M₀(H₀+M₀)) − ε₁/M₀], with Jacobian |∂(k₁,k₂)/∂(P,q)| = ε₁ε₂M₀/(ω²H₀). The Jacobian and the round trip check to 9e-11 (`r81_d2_chart_algebra.out`, line 1).
- **Repaired generators**, in R7-1's measured conventions [K_x, K_y] = −iJ and [J, P_x] = +iP_y (`r71_box_poincare_free.out` (C)):
  - **H = √(M² + P²)**;
  - **J = X_NW × P + S**, with S = −i∂_{φ_q};
  - **K_a = ½{H, X_NW,a} + ε_ab P_b S/(M + H)**, with ε_xy = +1.
- **Why the spin coefficient is +1 (proved).** Take K_a = ½{H, X_a} + α ε_ab P_b S f, with f = 1/(M + H). The cross terms give −iαS(2Hf − P²f²). Since P² = (H − M)(H + M), this equals −iαS. So [K_x, K_y] = −i(X × P) − iαS, and α = 1.
- **R7-1's printed form** (−½{H, X} − (S × P)/(M+H) = −½{H, X} + εPS/(M+H) in d = 2) has the right spin term and the wrong first-term sign.
- **d = 3 (suggested, not checked):** K = ½{H, X} + (P × S)/(M + H).
- **Lattice-native forms** (proved by algebra on the chart region):
  - K₀ = ½{H₀, X_E}, with X_E = Σ_i ½{ε̃_i/H₀, X_i};
  - S = (H₀/M₀)(J₀ − X_E × P);
  - X_NW = X_E − ε P S/(H₀(M₀ + H₀));
  - F := f(M) − f(M₀) = (W₁ − V)/P².

  Then **K = K₀ + ½{cW, X_NW} + ε P ½{S, cF}** and **J = J₀**. J is kinematic in BT.
- **Fermionic.** Exchange is q → −q. The g_a are odd and M₀ is even, so W, F and K preserve the odd sector.

### 3.3 Self-adjointness of the global K (proved, sketch)

- **K = ½{H, X_E} + B.** B is bounded and symmetric: it is built from S composed with operators of smooth kernel supported in supp g. In d = 1, B = 0.
- **H is bounded below by a positive constant.**
  - Off the chart, H = H₀ ≥ 2m.
  - On the chart, H = (1 − c)√(M₀² + P²) + c√(M² + P²) ≥ min(2m, M_b) > 0.
  - H is bounded on the torus.
- **The commutators are bounded.** [X_E, H] is bounded: it is a smooth multiplication, plus the derivative along u of a smooth P-family of smooth kernels. So [X_E, H^{1/2}] is bounded, via the resolvent integral.
- **Conclusion.** K = H^{1/2} X_E H^{1/2} + (bounded). It is self-adjoint by Kato–Rellich. X_E is self-adjoint because it generates a smooth complete flow on the compact torus.
- **The referee's symmetry gap is closed.** "c(P) × (K_BT − K₀)" is not symmetric; ½{cW, X_NW} is. Checked: 1e-14 against 0.39 (`r81_d1_ring_L2048.out`).

---

## 4. Results

### 4.1 The quartic prefactor: referee defect 2 is a convention mismatch, NOT CONFIRMED (checked, exact)

`r81_fock_norm.out`. 7 modes, P = 0, exact CAR enumeration:

| quantity | value |
|---|---|
| runner-style first-quantized odd spectrum (W on ordered pairs, as in `r71_bt_twobody.py:79-95`) | 2.307, 3.697, 14.356 |
| Fock, prefactor ½ | same spectrum, max difference 7.1e-15 |
| Fock, prefactor ¼ | max difference 5.1 |
| generic exchange-symmetric non-P-conserving kernel (boost-type), ½ vs first-quantized | 5e-16 |
| the same, ¼ | 1.3 |

- **Why the referee saw a ratio of 2.** Their ratio 2 (`r71_referee_checks.out:3-6`) compares ⟨pair k′|·|pair k⟩ with W(k′, k). But for a kernel odd in each argument, the first-quantized normalised-pair element is ⟨A′|W|A⟩ = ½[4W(k′, k)] = 2W(k′, k). The Fock ½ form reproduces exactly that (`r81_fock_norm.out`, (A), rows 4–6).
- **What changes.** "¼" is correct only for the normalised-pair kernel W_A = 2W. ¼ Σ W_A equals ½ Σ W. R7-1's printed ½ law is consistent with its runner.

### 4.2 The boost-sign defect: CONFIRMED and repaired (checked)

- With X = i∂, K = −½{H, X} gives [K, P] = −iH.
- The repaired operator is +½{H, X}.
- On the d = 1 ring the printed sign gives residual 2.00 in both [K,P] − iH and [K,H] − iP (`r81_d1_ring_L2048.out`).
- In the d = 2 chart it gives 2.0 and 1.6 (`r81_d2_chart_algebra.out`, (b)(c1)).

### 4.3 Theorem P2′ (d = 1, interacting two-body, lattice ring): proved; checked

- **Proof.**
  - 𝒟₂ is invariant: H₀ and P are multiplications, X_P is differential, and W outputs supp g at the same P.
  - On R′: c = 1, ε̃ is relativistic, P = k₁ + k₂ as real numbers, and X_P = i∂_P|_q.
  - So K = ½{√(M² + P²), i∂_P}, with M independent of P. Since [X_P, P] = i: [K, P] = iH and [K, H] = iP. [H, P] = 0 because W conserves P.
- **Check.** All operators are lattice operators on an L × L two-particle ring: FFT for the symbols, diagonal site positions, sampled smooth W. Packets are antisymmetric and Gaussian in P (σ = 0.05–0.06), inside the plateau: a bound state, a bound + scattering mix, and a scattering-only packet.

| L | [K,P] − iH (rel.) | [K,H] − iP (rel.) | [H,P] | comparator: printed sign | comparator: free K₀ with interacting H |
|---|---|---|---|---|---|
| 512 | 5.7e-6 – 6.2e-5 | 1.2e-4 – 2.7e-4 | ≤ 7e-16 | 2.00 / 2.00 | 0.23–0.26 / 0.38–0.58 |
| 1024 | 2.5e-8 – 2.4e-7 | 6.1e-7 – 1.1e-6 | ≤ 8e-16 | 2.00 / 2.00 | same |
| 2048 | 1.1e-11 – 9.5e-11 | 5.4e-10 – 3.1e-8 | ≤ 8e-16 | 2.00 / 2.00 | same |

- The convergence is finite-L aliasing of W's super-polynomial but sub-exponential real-space tail.
- |Wψ|/|Hψ| = 0.23–0.26, so the interaction is not perturbatively small.
- **Rep-independent check on the ring.** The bound state's √(E² − P²) is constant on the plateau to 1.0e-9 (L = 512), 1.4e-13 (1024) and 3.1e-14 (2048). In the transition shell it is 0.9715 at c = 0.43.
- At |P| = 1.84 and 2.21 the lowest odd pair state has E < |P| (printed as nan in `r81_d1_ring_L512.out`). These are zone-edge pairs, outside the box: R8-2's edge sector.

### 4.4 Theorem P2″ (d = 2 with rotations): proved; checked in the chart; lattice spectrum checked

**Proof.**
- (a) **Chart identity.** On box functions the lattice free generators are the BT free generators with M₀. J₀ = X_NW × P + S holds by rotation covariance of the canonical boost. K₀ = ½{H₀, X_E} = ½{H₀, X_NW} + εPS f₀ follows from §3.2.
- (b) **Interacting algebra.** Replace M₀ → M. M commutes with P, with X_NW (it is P-independent in the chart) and with S (rotation-invariant V). Then [K_a, P_b] = iδ_ab H, [K_a, H] = iP_a, [K_x, K_y] = −iJ (by §3.2's computation), the vector rules for J, and [J, H] = [P, H] = 0. H, F and the plateau c depend on P only through |P|.
- (c) **Domain.** 𝒟₂ is invariant: W and F output |q| < κ at the same P, and S preserves |q|.

**Checks.**
- **Chart identity** (`r81_d2_chart_algebra.out`, (a); 8th-order finite differences, 12 random points, a complex test function with l = 0, ±1, ±2):

| quantity | max relative difference |
|---|---|
| K₀,x vs BT | 1.1e-14 |
| K₀,y vs BT | 1.4e-14 |
| J₀ vs BT | 9.0e-15 |
| H₀ vs BT | 4.7e-17 |
| printed sign (comparator) | 1.84 |
| spin term dropped (comparator) | 3.0e-3 (small P) |

- **All 12 relations, interacting** (spectral P-grid 64², polar q-grid 40 × 16, packet = bound doublet + scattering):

| case | residual |
|---|---|
| repaired | every relation ≤ 6.0e-13; [S, M] = 5.5e-15 |
| (c1) printed sign | 2.0 ([K,P], [K,H]); 1.6 ([K_x,K_y] + iJ) |
| (c2) spin term dropped | 0.78 ([K_x,K_y] + iJ) |
| (c3) R7-1's single rank-one g_x channel | [S,M] 0.38; [J,H] 0.42; [J,K_x] − iK_y 0.42; [K_y,H] − iP_y 0.26 |

  Case (c3) confirms the referee's point that d ≥ 2 needs a rotational multiplet (`referee:100-104`).
- **On the lattice: invariant mass and doublet degeneracy** (`r81_d2_lattice_mass_L*.out`). Exact eigenvalues of the lattice H at fixed lattice P; the supp-W block decouples exactly because H₀ is diagonal in k₁. Eleven P vectors, |P| up to 0.56, directions 0° to 158°:

| L | BT: spread of √(E² − P²) | BT: max doublet split | Galilean comparator: spread | Galilean: doublet split |
|---|---|---|---|---|
| 64 | 9.1e-5 | 5e-5 | 0.100 | up to 3.7e-2 |
| 128 | 6.3e-7 | 3.6e-7 | 0.089 | — |
| 192 | 1.2e-8 | 1.2e-8 | 0.089 | up to 3.5e-2 |

### 4.5 Theorem L (interacting leakage): proved; checked

- **Statement.** Let ψ be a two-particle lattice state, η a rapidity along n, I an open set of total momenta and Σ a Borel set of the spectrum of M. Suppose that for all μ ∈ Σ, P ∈ I and s ∈ [0, η]:
  - the mass-μ orbit Φ^μ_s(P) stays in |P| < Π₁ (along n: P_∥ ↦ m_⊥ sinh(asinh(P_∥/m_⊥) − s), with m_⊥ = √(μ² + P_⊥²));
  - the legs of (Φ^μ_s(P), q) stay in the box for all q ∈ Q_Σ := {M₀(q) ∈ Σ} ∪ supp g.

  Then **‖e^{−iηK}ψ − ι U_BT(η) ψ‖ ≤ 2‖(1 − E)ψ‖**, with **E = 1_I(P) 1_Σ(M)**. Here ι is the embedding of box-supported functions, and U_BT is the continuum BT group (c ≡ 1).
- **Proof.**
  1. **E commutes with M and P,** and [K_BT, M] = 0. So U_BT(s) maps Ran E into Ran 1_{Φ_s(I)}(P) 1_Σ(M).
  2. **q-support is controlled.** For any Borel f, f(M) − f(M₀) has kernel in supp g × supp g. That follows from the resolvent: (M − z)⁻¹ − (M₀ − z)⁻¹ = −(M₀ − z)⁻¹ V (M − z)⁻¹, with (M − z)⁻¹ g ∝ (M₀ − z)⁻¹ g, extended by Helffer–Sjöstrand or a limit. So Ran 1_Σ(M) has q-support in Q_Σ. U_BT changes q only through the spin rotation, which preserves |q|.
  3. **The good part is exact.** φ(s) := U_BT(s)Eψ is therefore supported where K_lat = K_BT, by Lemma L, the chart identity and c = 1. So φ solves the lattice equation, and by self-adjointness (§3.3) φ(s) = e^{−isK}Eψ.
  4. **The rest is bounded by unitarity:** ‖(U_lat − ιU_BT)(1 − E)ψ‖ ≤ 2‖(1 − E)ψ‖. ∎

  Steps 2–3 for non-smooth Eψ use a standard density argument (sketch). The theorem uses internal-mass spectral support, as the registration asks.
- **Check** (`r81_leak.out`, `r81_leak_NP960.out`). The d = 1 lattice law in the chart is ½{H_c(P), i∂_P}, with H_c = (1 − c)√(M₀² + P²) + c√(M² + P²). Both it and the c ≡ 1 BT law are integrated with RK4.
  - **(i) Bound-state packet with C^∞ compact P-support |P| < 0.25.** Predicted η* = asinh(Π₁/M_b) − asinh(0.25/M_b) = 0.367.

    | η | ‖U_lat ψ − U_BT ψ‖, NP = 640 | NP = 960 | bound 2‖(1 − E)ψ‖ |
    |---|---|---|---|
    | 0.1 – 0.37 (≤ η*) | 1.1e-6 – 1.6e-6 | 4.8e-8 – 6.9e-8 | 0 |
    | 0.45 | 2.0e-6 | 1.0e-7 | 0.21 |
    | 0.6 | 2.35e-3 | 2.35e-3 | 1.18 |
    | 0.8 | 4.95e-2 | 4.95e-2 | 1.89 |
    | 1.0 | 0.133 | 0.133 | 2.0 |

    Before η* the difference is discretisation: it falls 20× from NP = 640 to 960, and the BT integrator's error against analytic transport is 1e-5 → 3e-6. That is consistent with the theorem's "exactly zero".
  - **(ii) Bound + continuum mix** (Gaussian in P). The leakage stays below the bound optimised over Σ = spec ∩ [0, μ_max] at all eight η. For example: 6.7e-6 against 0.16 at η = 0.3, and 0.104 against 2.0 at η = 1.0.

### 4.6 d = 2 direct lattice-native run: resolution-limited, not a precision check (checked; reported as such)

- **Setup** (`r81_d2_lattice_algebra.py`). Every generator is built from lattice operators. The relative momentum k₁ is on an L × L torus; P is on a spectral window; S, X_NW and F are in the lattice-native forms of §3.2; all 12 relations are evaluated.
- **Results:**

| run (file `r81_d2_lattice_algebra_...out`) | [K_x,H] − iP_x | other relations |
|---|---|---|
| repaired, L = 64, NP = 20 (`L64_NP20_doublet`) | 1.0 | 1e-2 to 0.8 |
| repaired, L = 96, NP = 20 (`L96_NP20_doublet`) | 0.35 | 7e-3 to 0.3 |
| free-only comparator (K₀ with interacting H), L = 64 → 96 | 3.8 → 3.5 | — |
| representation floor: free law alone, same packet, L = 64 → 96 (`_FREE`) | 0.65 → 0.22 | the other relations track the interacting run |
| floor with a Gaussian-only packet, L = 64, NP = 20 → 28 (`_FREE_GAUSS`); L = 96, NP = 20 gives the same as L = 64, NP = 20 | 5.3e-3 → 3.4e-5 | the other relations fall to 1e-6 – 7e-5 |

- The file `..._L48_NP24_doublet.out` is from a first version: κ = 0.8, window ±0.9, Π₁ = 0.85. It is superseded and not used.
- **Reading.** The relative-momentum torus cannot resolve the sstep shoulder of the d = 2 form factor at feasible L. The interacting residuals track the free-law floor. So this run is consistent with, but does not independently confirm, §4.4 at high precision. The precise d = 2 evidence is §4.4: the chart algebra, the chart identity of the lattice free generators, and the lattice spectrum.

---

## 5. Scope, and what is not shown

- **N ≥ 3.** The law acts pairwise in every sector. The pairwise K does not close (BT cluster problem; Keister–Polyzou). This is R7-6's item, open here.
- **d = 3.** The p-wave triplet and K = ½{H, X} + (P × S)/(M + H) are suggested by the same algebra; not checked.
- **Ward identities.** No interacting stress tensor is built, so the referee's W1–W4 narrowing stands. Universal coupling and the edge sector belong to R8-2. Loops and pair creation belong to R7-5. There are no gauge fields.
- **Not a reducing sector.** The domain is a common invariant Lie-algebra domain, not an exponentiating box sector (B1 Theorem U untouched). Finite boosts are exact only up to the orbit condition of Theorem L.
- **Graded fermions.** R6-1's ⊗M₂ caveat stands.

## 6. Reading against the FIXED readings (`TESTS:3450-3453`)

- **PASS: worker reading, referee required.**
  - (i) The repaired interacting two-body box sector has an exact Poincaré algebra in d = 2 with rotations (Theorem P2″). It is proved. It is checked in the chart (≤ 6e-13), with the lattice free generators identified to 1e-14, and with the rep-independent lattice spectrum test at 1.2e-8 (L = 192, converging).
  - In d = 1 the algebra is checked directly on the lattice ring (≤ 3e-8 at L = 2048, converging).
  - (ii) The interacting leakage bound, using internal-mass spectral support, is proved (Theorem L) and checked.
- **The caveat that travels with it.** "Verify every commutator numerically on the lattice" is met literally in d = 1. In d = 2 it is met in the canonical chart, plus the lattice-generator identification and the lattice spectrum. The direct lattice-native d = 2 run is resolution-limited (§4.6). If the referee requires a direct high-precision lattice run in d = 2, the strongest reading is INCONCLUSIVE, with P2′ (d = 1), P2″ (chart) and L as bounded positive results.
- **FAIL is not available.** P2″ is an explicit counterexample to an obstruction in d = 2.

## 7. Strong-word check

- "Exact" means an operator identity on 𝒟₂ in infinite volume. The numerics are finite-L or finite-grid, and converging.
- "Every commutator" means the Poincaré relations of 2+1 dimensions (12 listed) and of 1+1 (3).
- "Proved" for P2″ rests on algebra done here, BT's structure (cited), and Lemma L (R7-1, confirmed). The spin coefficient is derived here, not quoted.
- "Defect 2 not confirmed" is a convention statement, checked by exact enumeration. It changes no number in R7-1's runner.
- Theorem L is a sketch at the density step.
- Nothing here bears on the gravitational wall (referee §5); there is no Ward identity and no universal coupling.

## 8. Price (named, not adopted)

Unchanged from R7-1 (`C5_R7-1_report.md:274`):
- non-quasi-analytic band and kernel functions;
- a frame-fixed box;
- an inert edge sector;
- form-factor interactions.

Added detail:
- the interaction and the boost's two-body part are defined through the pair's invariant mass. They are non-local in the relative coordinate at scale 1/κ, with super-polynomial tails.
- K_W is a first moment: T_a K T_a⁻¹ = K + aH (proved, since X_E → X_E + a).

No axiom text changes. Admissibility does not fix the dynamics (`AX:116`).

## 9. For the referee

Check, in order:
1. §4.1's convention argument. The ½ spectra match the runner (`r81_fock_norm.out`).
2. The spin coefficient α = +1 (§3.2), and the chart identity (§4.4 (a)).
3. The lattice-native identities K₀ = ½{H₀, X_E}, S = (H₀/M₀)(J₀ − X_E × P), X_NW = X_E − εPS/(H₀(M₀+H₀)).
4. Self-adjointness (§3.3).
5. Theorem L, step 2 (q-support of 1_Σ(M)) and the density step.
6. Whether §6's d = 2 evidence meets "verify every commutator numerically on the lattice".

Runtimes with OMP_NUM_THREADS=2:
- d = 1 ring: L = 2048 about 3 min.
- d = 2 chart: 25 s.
- d = 2 lattice spectrum: L = 192 about 1 min.
- Leakage: 2–4 min.
- d = 2 direct run: L = 96 about 3 min.
