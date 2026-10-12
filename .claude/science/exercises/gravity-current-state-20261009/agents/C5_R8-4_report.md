# C5 R8-4 report: an explicit lattice field Hamiltonian for invariant-mass vertices (the INV gap)

**Author.** Claude Opus 5.5 probe. Same model family as the supervisor and as every C5 worker. Unrefereed. Run 2026-10-12, 16:03Z to about 16:50Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R8-4/`. Scripts and outputs are in `S/scripts/`. Every run took under 4 min with `OMP_NUM_THREADS=2`.
- `r84_d3_oneloop.py` → `_m0.05.out`, `_m0.05_fine.out`, `_m0.15.out`. Infinite-volume one-loop dressed dispersion of model S on Z³, with comparators.
- `r84_fock.py` → `r84_fock_part1.out`. A sparse fermionic (and bosonic) Fock engine. It applies H's explicit monomials, with CAR signs, to basis states. RS2 from H is compared with the closed form.
- `r84_toyN_fock.py` → `_F.out`, `_B.out`. Two-loop toy N: brute-force RS4 mixed coefficient from H, compared with the Goldstone linked closed form.
- `r84_toyN_cont.py` → `_F.out`, `_B.out`; `r84_toyN_cont_cuts.py` → `.out`; `r84_toyN_scaling.py` → `.out`. Toy N in infinite volume (1+1D), with a cutoff-inactivity check and a mass-scaling check.
- `r84_tails.py` → `.out`. Real-space kernel tails and ℓ¹ norms (stability constants), for d = 1.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full.
- `TESTS.md`:
  - `:1-86` (T0, T1);
  - `:2302-2440` (C5 method, round 1);
  - `:3396-3542` (round 6–7 referee results, round 8, R7 referee part 2, and R8-4 itself at `:3515-3526`).
- `agents/C5_R7-5_report.md` (all of it) and `agents/C5_R7-5_referee_verdict.md` (all of it).
- `agents/C5_R7-1_report.md:1-140` (the box law).
- `scripts/C5/R7-5/r75_oneloop.py` (conventions).

**Labels.** proved / checked (numerics here) / suggested / reading / comparator. A comparator marked **V** was verified on the web this session by a literature sub-agent reading arXiv abstract or ar5iv pages; its quotes passed through a summarizer. **R** means recalled, not verified.

---

## 0. In plain words

- **The missing object now exists, at one loop.** Model S is an explicit, finite-per-site, stable, Hermitian, quasi-local fermion Hamiltonian on Z³ × ℝ.
  - Every pair-creating vertex is a compact smooth function of the created pairs' invariant masses.
  - Every species has both orderings that R7-5's INV lemma needs: decay into the cluster, and creation of the cluster together with the particle from the vacuum.
  - The one-loop dressed dispersion, computed from the Hamiltonian's own matrix elements, is exactly relativistic inside a stated momentum and rapidity budget.
- **Stability is automatic once everything is a fermion.** Each term is a product of four fermion operators, so it has norm at most 1. Summable kernels then give H ≥ −c·(number of sites). The vacuum-triple instability the R7-5 referee named belongs to bosonic cubic couplings and does not arise here.
- **Two things had to be added that R7-5 did not have.**
  - (a) A fermion's "Z-graph" is a vacuum fluctuation that the external particle Pauli-blocks. Its sign is opposite to the boson case, so R7-5's lemma does not carry over as written: with plain relativistic normalization the dispersion is off by O(1) (checked). A kinematic factor h = (3W − E)/(W + E) on the decay vertex restores exactness (proved).
  - (b) R7-5 used a product vacuum vertex but never checked it. It works only while the "spectator" pair masses, which involve the external particle, stay on the form-factor plateau. That sets the rapidity budget. Leaving it gives a few-percent violation (checked).
- **Two loops: the invariant-mass structure does not survive in the stated toy.** Toy N nests one quartet's loop inside another's. It contains exactly the orderings the INV lemma needs, for both the external particle and the internal line.
  - Its O(g_o²g_i²) dressed dispersion has a Lorentz-violating p² term of order one relative to the two-loop mass shift. This holds for fermions (−6% at p = m/3, growing to −135% at p = 2m) and for bosons, which is R7-5's own INV class (−0.6% at p = m/3, growing to −18% at p = 2m). It persists when the masses are lowered 4× at fixed form-factor scale.
  - This is computed from the Hamiltonian. A closed form is checked against brute-force fourth-order perturbation theory on the Fock space to 1e-16, then evaluated in infinite volume.
- **What the toy leaves open.** A quartic vertex also has 2↔2 crossings (for example X + Y → A + B) and the Y ↔ XAB ordering. In a local theory those orderings are needed for Feynman covariance. Toy N omits them, as R7-5's pair-creation class does. Whether a complete crossing set with invariant-mass vertex functions closes at two loops is untested. The invariant-mass prescription does not fix their vertex functions.
- **Against the FIXED readings: INCONCLUSIVE** (worker reading).
  - PASS needs two-loop closure in a stated toy, and the stated toy fails it.
  - FAIL needs an incompatibility no-go, and model S is an explicit counterexample to that no-go.

---

## 1. Hypotheses and classes (stated before any title)

**H-lat.**
- Z³ × ℝ, continuous time.
- Four spinless complex fermion species s ∈ {A, B, C, D} per site, giving local dimension 16 with a graded tensor product. This is R7-1's H-lat (`C5_R7-1_report.md:31`) with four species.
- Box dispersion ε̃_s(k) = √(m_s² + Σ_i w₁(k_i)), where:
  - w₁ = ρk² + (1 − ρ)(π²/2)(1 − cos k);
  - ρ is a Gevrey-2 plateau equal to 1 on |k| ≤ b₁;
  - so ε̃ = √(m² + |k|²) in the box and ε̃ ≥ √(m² + b₁²) outside it (no doubler).

**H-pert.**
- "One loop" means the O(g²) Rayleigh–Schrödinger (RS) shift of a one-particle energy relative to the Fock vacuum.
- "Two loops (toy)" means the O(g_o²g_i²) RS4 shift.
- "Lorentz-invariant self-energy" means the on-shell dressed dispersion obeys E(p)² − p² = constant at that order. An instant-form Hamiltonian has no off-shell covariant Σ(z, p); the R7-5 referee's "computed from the Hamiltonian itself" is met by this on-shell object.

**Classes.**
- **S (model S).** Pair creation through even four-fermion monomials: 0 → ABCD, and X → (the other three) for each X, each with its h.c.
- **N (toy N).** An outer quartet (X, Y, A, B) and an inner quartet (Y, U, C, D). Terms:
  - X → YAB and 0 → XYAB, the vacuum vertex depending on (Y, A, B) only;
  - Y → UCD and 0 → YUCD, the vacuum vertex depending on (U, C, D) only;
  - each with its h.c.
  - Fermionic version F (with h) and bosonic version B (R7-5's INV class, h = 1).

**Excluded, not addressed:**
- 2↔2 crossings (number-conserving rearrangements);
- gauge fields (R8-5);
- microcausality and cluster separability;
- gravity and Ward identities;
- Z⁴;
- non-perturbative ground-state structure beyond existence.

## 2. Prior art (each counted once)

- **R7-5 (referee: NOT CONFIRMED as PASS).** INV is "a conditional spectral lemma only … no explicit stable finite-per-site lattice field Hamiltonian realizing this was built" (`TESTS.md:3502`). The vertices are "an imposed functional custodial condition … not shown to be radiatively closed" (`TESTS.md:3504`).
  - The referee's specific gaps: no Hamiltonian or enumeration of orderings; the product vacuum vertex unchecked; vacuum-triple cubic terms "generically unbounded below"; the canonical Fock space is not finite per site (`C5_R7-5_referee_verdict.md:20-22`).
  - The worker's own expectation: two loops "plausibly fails unless the dynamics is reorganised in BT form" (`C5_R7-5_report.md:274`).
- **R7-5 INV-s.** Π = g²∫dM² ρ₂F²/(M² − s) with both orderings (`C5_R7-5_report.md:172-178`). Below I extend it to three-body clusters and to the fermionic Pauli sign.
- **R7-1 (PASS WITH SCOPE).** Box law and Lemma L, under which on C_c^∞(int B) the lattice generators equal the continuum ones (`C5_R7-1_report.md`, §4.1).
- **Axioms.** Admissibility "does not choose a Hamiltonian or transfer operator" (`MINIMAL_AXIOMS_2026-06-29.md:116-121`). The one-site domain is M₂(C) (`:47`). So every dynamics here is supplied content.
- **Literature (comparators).**
  - **Collins–Perez–Sudarsky–Urrutia–Vucetich, gr-qc/0403053 (V).** ξ = g²/(6π²)[1 + 2∫x f′²], of order g² independently of Λ. This is in the appendix; the abstract says "percent level" unless fine-tuned.
  - **Polyzou, nucl-th/0302023 (V).** Poincaré-invariant relativistic quantum mechanics with particle production, satisfying cluster properties and the spectral condition, for "a bounded number of bare-particle degrees of freedom". The relativistic Lee model is used there to illustrate the charge structure.
  - **Lee model (V via Bender et al., hep-th/0411064, citing Källén–Pauli 1955).** Above a critical renormalized coupling a negative-norm ghost appears.
  - **Efimov nonlocal QFT (partly V).**
    - Form factors are entire functions decreasing in Euclidean space (Guskov–Ivanov–Ogarkov, 1711.08829).
    - Unitarity and macrocausality hold order by order (JINR PEPAN 1970 abstract).
    - Nonlocal Lagrangians generically inherit Ostrogradsky/higher-derivative instabilities in Hamiltonian form (Kleppe–Woodard, hep-th/9203016 §5; Barnaby, 1005.2945).
    - Model S avoids that route: H is given directly as a bounded-per-site operator, not obtained from a nonlocal Lagrangian. The price is that there is no Feynman-covariant structure to inherit beyond one loop (§3.5).
  - **Bru–de Siqueira Pedra, arXiv:1702.08869, Thm 4.8 (V).** For even fermionic interactions with finite W-norm, with F(r) = (1+r)^{−(d+ε)} allowed, the finite-volume dynamics converge to a C₀-group of *-automorphisms.
  - **Keister–Polyzou, 1109.6575 (V).** Bakamjian–Thomas (BT) fails cluster separability for N ≥ 3; Sokolov packing restores it.

## 3. Results

### 3.1 The Hamiltonian (model S): explicit

On a periodic L³ torus, N = L³, with the infinite-volume limit taken as usual:

  H = Σ_s Σ_k ε̃_s(k) n_{s,k} + g(V₀ + Σ_X V_X) + h.c.

**Vacuum term.**
- V₀ = Σ_{k_A+k_B+k_C+k_D=0} N⁻¹ K₀ a†_{A,k_A} a†_{B,k_B} a†_{C,k_C} a†_{D,k_D}
- K₀ = Π_{i<j} F(s_ij) · Π_i χ(k_i) / √(Π_i 2ε̃_i), with the product over all six pairs.

**Decay term for each species X** (Y, Z, W are the other three species):
- V_X = Σ N⁻¹ K_X a†_{Y,k₁} a†_{Z,k₂} a†_{W,k₃} a_{X,p}, with p = k₁ + k₂ + k₃.
- K_X = Π_{pairs ⊂ YZW} F(s_ij) · √h(ε̃_X(p), W) · Π_i χ(k_i) · c(p) / √(2ε̃_X(p) Π_i 2ε̃_i).

**Ingredients.**
- s_ij = (ε̃_i + ε̃_j)² − |k_i + k_j|², the on-shell pair invariant mass², exact on the support. W = Σ_i ε̃_i.
- F(s) = 1 − σ((√s − Λ₁)/(Λ₂ − Λ₁)), where σ is the e^{−1/x} smooth step (Gevrey-2). F is compact and C^∞.
- h = (W(1 + 2C) − E)/(W + E), with C = 1 here.
- χ is a per-component leg plateau (A₁ → A₂, inside the box) and c is a total-momentum plateau (C₁ → C₂). Both are frame-fixed and **inactive on every configuration used below** (checked: maximum leg component on the support 0.87–1.11 against A₁ = 1.7, from `r84_d3_oneloop_m*.out`, column "maxleg").
- Every kernel is a C^∞ function on the torus with compact support inside the box.

### 3.2 Stability, self-adjointness, finite per site

- **Finite per site (proved).** Local dimension 16, four fermion modes per site.
- **Hermitian at finite volume (proved).** Each monomial enters with its adjoint (`r84_fock.py`, `Ham.add`).
- **Extensive lower bound (proved).**
  - Each CAR monomial has norm ≤ 1, and H₀ ≥ 0.
  - Translation invariance gives ‖V₀‖ ≤ N‖κ₀‖₁, and likewise for each V_X, where κ is the real-space coefficient: the inverse DFT of K over the independent momenta.
  - So H_Λ ≥ −2g|Λ|(‖κ₀‖₁ + Σ_X‖κ_X‖₁).
  - ‖κ‖₁ < ∞ because K is C^∞ on T^{3d}, so its Fourier coefficients decay faster than any power (proved, standard).
- **The constant (checked, d = 1 only).** ‖κ₀‖₁ = 8.708 and ‖κ_X‖₁ = 10.980 (L = 192; 8.65 and 10.92 at L = 128), so H_Λ ≥ −105 g|Λ| (`r84_tails.out`). The d = 3 constant is finite (proved) but was not computed.
- **R7-5's vacuum-triple instability does not arise.** That mechanism needs bosonic amplitudes growing as amplitude² against amplitude³ (`C5_R7-5_referee_verdict.md:22`). Fermionic monomials are bounded.
- **Side remark (proved, elementary; not used).** A bosonic φ coupled linearly to bounded fermion bilinears, φB + h.c., is also bounded below by completing the square: H ≥ −‖Σ_k B_k†B_k/ω_k‖, which is extensive for massive φ. But that φ is not finite per site.
- **Infinite volume (comparator V).**
  - The coefficients are super-polynomial, so the W-norm with F(r) = (1+r)^{−(d+ε)} is finite. Bru–de Siqueira Pedra Thm 4.8 then gives a strongly continuous automorphism group.
  - Ground states exist (weak-* compactness), and the GNS generator is self-adjoint and ≥ 0 (R).

### 3.3 Quasi-locality (tails)

- **Super-polynomial (proved).** Each kernel is C^∞ on the torus.
- **Exponential decay is impossible (proved, elementary).** An exponentially decaying kernel has a real-analytic symbol on the torus. A real-analytic function that vanishes on an open set (outside the compact support of F) vanishes identically. This is the same price class as R7-1 / R6-1 Prop. N.
- **Gevrey-2 inputs give tails of roughly exp(−c√r)** (R, Gevrey–Fourier).
- **Checked (d = 1).** The maximum |κ| on shells of radius R falls 1.0e-2 → 6.9e-4 → 4.0e-5 → 4.0e-6 at R = 0, 8, 24, 64 (vacuum term), and similarly for the decay term (`r84_tails.out`). That fits c ≈ 1 in exp(−c√r), with oscillations.

### 3.4 One loop, from the Hamiltonian

**(a) Enumeration of orderings (checked; this closes the referee's "no enumeration" gap).**
- `r84_fock.py` builds every monomial of model S on the finite lattice. It applies V to |X_p⟩ and to |0⟩ with explicit CAR signs, and forms RS2 = Σ_n |V_{nψ}|²/(E_ψ − E_n) for each.
- Their difference matches the closed form "decay sum Σ|K_X/N|²/(E − W) + Pauli-blocked vacuum sum Σ|K₀/N|²/(E + W)" to:
  - ≤ 1.1e-16 for all four species at four momenta, in d = 1 with L = 6 (periodic) and L = 8 (A, B antiperiodic);
  - ≤ 1.4e-17 in d = 3, L = 3; 0 and 1e-27 in d = 3, L = 4 (`r84_fock_part1.out`).
- The Z ordering of a fermion is the vacuum fluctuation that the external particle Pauli-blocks, with sign +.
- Outside the budget the c(p) cutoff switches the decay vertex off. Only the Z part then survives (positive shifts at k = 2.09: +1.46e-4), which is frame-fixed by design.

**(b) Lemma INV-3F (proved).**
- Let Ψ be any Lorentz-scalar weight on an n-body on-shell cluster, here Π F(s_ij)².
- Then ∫Π d³k_i/(2E_i) δ³(Σk − p) Ψ² G(W) = ∫dM² ρ_Ψ(M²) G(√(M² + p²)) / (2√(M² + p²)), provided the support is untruncated. Proof: insert ∫dP⁰ δ(P⁰ − W); ρ_Ψ(P²) is Lorentz-invariant.
- On shell, h/(E − W) + 1/(E + W) = 2CW/(E² − W²). Hence 2E_p δE(p) = g²(2π)⁻⁶ ∫dM² ρ_Ψ(M²) · C/(m² − M²), which is p-independent.
- With h = 1 instead (boson normalization, fermion sign), the bracket is 2E/(E² − W²) and 2E_p δE carries E_p/W: Lorentz violation (proved).
- C is free. C = 0 gives zero one-loop mass shift.

**(c) Spectator budget for the product vacuum vertex (proved, elementary).**
- On X's Z configuration (X at p, rest cluster at −p), Ψ₆ = Ψ(rest) × Π_Y F(s_XY).
- Here s_XY ≤ 2m² + 2E_Y(E_p + |p|). The spectators sit on the plateau while that is ≤ Λ₁².
- This gives a rapidity budget y ≲ ln(Λ₁²/(2 m E_Y,max)): large for m ≪ Λ (as in R7-5's estimate), small in numerics.

**(d) Infinite-volume d = 3 check (checked; `r84_d3_oneloop_m*.out`).**
- Setup: Λ₁ = 1, Λ₂ = 1.3, four equal masses m.
- Quadrature: axial Gauss in k₁, a trapezoid cube in k₂, three resolutions.
- Rotations: p along z and along (1,1,1)/√3 give identical numbers. That is so by construction, because the evaluation frame is rotated with p and the only cubic-frame ingredients, the cutoffs, are inactive. It is not an independent test of rotations.

Relative deviation [m²_eff(p) − m²_eff(0)]/|m²_eff(0)|, with m²_eff = 2E_p δE:

| m | p | INV (as built) | h = 1 | no Z ordering | frame-fixed FF |
|---|---|---|---|---|---|
| 0.05 | 0.1 | −2.3e-5 → −4.7e-5 → **−2.5e-6** (refining) | −1.21 | +2.2e-2 | +1.5e-2 |
| 0.05 | 0.2 | −1.3e-4 → −1.1e-4 → **−1.6e-5** | −2.96 | +5.4e-2 | +5.9e-2 |
| 0.15 | 0.1 | +9.6e-5 → **−1.2e-5** | −0.20 | +9.0e-3 | +1.7e-2 |
| 0.15 | 0.2 | +9.9e-5 → **−2.2e-5** | −0.64 | +2.9e-2 | +6.5e-2 |
| 0.15 | 0.3 | −1.9e-4 → **−2.8e-5** | −1.15 | +5.2e-2 | +0.14 |
| 0.05 / 0.15 | 0.45 (outside the spectator budget: √s_spect up to 1.43–1.45 > Λ₁) | **−2.8e-2 / −4.2e-2**; with spectators dropped, −1.7e-4 / −4.5e-6 | | | |

- m²_eff(0) = −3.78e-5 g² (m = 0.05) and −2.23e-5 g² (m = 0.15), lattice units.
- Inside the budget the residual is at quadrature level and shrinks under refinement. Each comparator is 10² to 10⁵ times larger.
- By the A–B–C–D symmetry of model S (equal masses), all four species have the same self-energy; (a) checks that at finite L.

### 3.5 Two loops in a stated toy (toy N): the structure is not radiatively closed — checked

**(a) From the Hamiltonian (checked).**
- `r84_toyN_fock.py` builds toy N's monomials (masses 0.29–0.43, d = 1, L = 5, 6, 7, with twists).
- It computes RS4 = ⟨VRVRVRV⟩ − E₂⟨VR²V⟩ for X_p minus the vacuum, at (g_o, g_i) = (1,1), (1,0), (0,1). The mixed coefficient is b = E₄(1,1) − E₄(1,0) − E₄(0,1).
- It also finds E₃ = 0 exactly (each move flips every species-count parity) and E₄(0,1) = 0.
- The Goldstone linked closed form reproduces b to ≤ 9e-17 (fermions) and ≤ 3e-16 (bosons), in `_F.out` and `_B.out`:

  mixed = Σ_outer-decay |o|² 𝒩(E_p − W_o, k_Y) + Σ_outer-vac (∓|o_v|²) 𝒩(−(E_p + W_o), k_Y)

  𝒩(α, k_Y) = Σ_inner-decay |i|²/(α²(α − c)) ∓ Σ_inner-vac |i_v|²(α − b)/(α²b²)

  where c = W_in − E_Y and b = E_Y + W_in.
- The ∓ sign is upper for fermions (Pauli/exchange sign) and lower for bosons.
- The Z-type inner insertion is the sum of four relative orderings, (α − b)/(α²b²). That is only the first-order Taylor expansion of the covariant 1/(b + α).

**(b) Infinite volume (checked; `r84_toyN_cont_{F,B}.out`, `_cuts.out`, `_scaling.out`).**
- Controls on the same grid:
  - the one-loop m²₁(p) of X is p-independent to 2e-8;
  - the inner Y one-loop is p-independent to 2e-8.
- The mixed coefficient 2E_p·mixed(p), relative deviation from p = 0 (masses ×1):

| p (m_X = 0.3) | 0.1 | 0.2 | 0.3 | 0.4 | 0.6 |
|---|---|---|---|---|---|
| fermion (m²_mix(0) = −6.295e-4) | −6.20e-2 | −0.230 | −0.468 | −0.746 | −1.35 |
| boson, R7-5's INV class (m²_mix(0) = −2.653e-3) | −5.98e-3 | −2.36e-2 | −5.17e-2 | −8.90e-2 | −0.184 |

- **Grid stability.** G = 121 and 161 agree to < 1e-6 relative.
- **Cutoffs.** Inactive: max |k_Y| ≤ 1.08 < C₁ = 1.2; max leg ≤ 1.39 < A₁ = 2.0. Widening every cutoff leaves the numbers unchanged to 1e-8.
- **Mass scaling at fixed (Λ₁, Λ₂).** Define c ≡ [Δm²_mix/|m²_mix(0)|]/(p/m_X)² at p = 0.1, where Δm²_mix = m²_mix(p) − m²_mix(0). c < 0 means the negative two-loop m² term grows in magnitude with p. For masses × (1, 0.5, 0.25):
  - fermion: c = −0.56, −0.43, −0.29;
  - boson: c = −0.054, −0.049, −0.046.
  - The scale 0.5 and 0.25 points use one grid each; the one-loop control on the same grids is at 1e-8.
- **Reading.** At O(g_o²g_i²) the dressed mass² picks up c·(p/m)² times the size of the two-loop mass shift. That is a dimension-4 speed term of the size of the two-loop correction. It is not suppressed in the tested window of m/Λ (boson: nearly flat; fermion: slowly falling). The asymptotic m/Λ → 0 behaviour is not established.

**(c) Mechanism (suggested).**
- The outer vertex functions and normalizations are evaluated at the bare on-shell kinematics of the Y line. The Y line carries an off-shell insertion.
- The inner Z-insertion's off-shell continuation is (b − α)/b², not the covariant 1/(b + α).
- Neither error is cancelled by any ordering present in toy N.

**(d) Scope (strong words).**
- Toy N contains the orderings the INV lemma requires: decay and vacuum for X and for Y.
- It omits the 2↔2 crossings (X + Y → A + B, and so on) and the Y ↔ XAB ordering of the outer quartet. A Feynman-type covariant sum needs those even for constant (local) vertices, so toy N's failure may be partly a missing-orderings effect (suggested; the local-limit control was not run).
- The invariant-mass prescription does not determine the vertex functions of those crossings.

## 4. Answer to the registered question

| check | result | label |
|---|---|---|
| explicit, finite-per-site, Hermitian H on Z³ × ℝ with compact invariant-mass pair-creation vertices and the INV orderings for every species | model S (§3.1) | proved (construction) |
| boundedness below (the vacuum-triple term) | H_Λ ≥ −2g\|Λ\|Σ‖κ‖₁; −105 g\|Λ\| in d = 1 | proved; constant checked in d = 1 |
| quasi-locality | faster than any power, never exponential; about exp(−√r) in d = 1 | proved; checked in d = 1 |
| one-loop self-energy Lorentz-invariant, from H | Fock RS2 = closed form to 1e-16 (d = 1, 3); d = 3 dispersion flat to ≤ 3e-5 and shrinking, against comparators at 1e-2 to 1; budget mapped | checked; Lemma INV-3F proved |
| two-loop closure in a toy | **fails in toy N**, O(1) relative to the two-loop term, both statistics | checked (Hamiltonian-verified closed form) |

## 5. Strong-word check

- **"Exact" (one loop).**
  - The on-shell O(g²) dressed dispersion, in infinite volume.
  - p inside the spectator budget and the inactive-cutoff region.
  - The numerics are at quadrature level: 2.5e-6 to 3e-5.
  - For fermions it holds only with the h factor.
- **"Stable."** An extensive lower bound H_Λ ≥ −c|Λ| (thermodynamic stability), not H ≥ 0. The d = 3 constant was not computed.
- **"Self-adjoint."**
  - At finite volume: by construction.
  - In infinite volume: by the comparator theorem (V) plus standard GNS (R).
- **"From the Hamiltonian itself."**
  - The small-L identities are exact algebraic checks.
  - The large-L, d = 3 and infinite-volume numbers use those verified closed forms, not inserted Feynman integrands.
  - The Goldstone form is derived (Goldstone linked-cluster theorem, R) and verified only at L = 5–7, where the support is sparse (7–16 monomials per family).
- **"Fails at two loops."**
  - Toy N only (1+1D; distinct species; no 2↔2 or Y ↔ XAB orderings).
  - Masses 0.3, 0.15, 0.075 at Λ₁ = 1, Λ₂ = 1.4.
  - **Not** a theorem about every completion.
- **"Not suppressed."** Only in the tested factor-4 window of m/Λ. The fermion coefficient is falling slowly.

## 6. Against the FIXED readings (`TESTS.md:3523-3526`)

**INCONCLUSIVE.** Worker reading, same model family, unrefereed.

- **PASS: not met.**
  - The four one-loop checks are met by model S: explicit, stable, quasi-local, and Lorentz-invariant at one loop from the Hamiltonian.
  - But the clause also asks for "two-loop closure in a stated toy". In the stated toy the invariant-mass structure is **not** radiatively closed (§3.5).
- **FAIL: not met, and refuted in the stated class.**
  - Model S is an explicit counterexample to "invariant-mass vertices with all time orderings are incompatible with a bounded-below finite-per-site Hamiltonian".
  - More strongly (proved): in the finite-per-site fermionic class, *any* finite family of even monomials with summable kernels is extensively bounded below. That includes adding the 2↔2 crossings. So no incompatibility no-go exists in that class.
- **The negative result that does stand** (§3.5) is a radiative-closure failure, not the registered FAIL. If it is recorded, it needs the other-vendor referee.

## 7. Price (named, not adopted)

- **Supplied dynamics.** Admissibility does not choose a Hamiltonian (`MINIMAL_AXIOMS_2026-06-29.md:116-121`).
- **Four fermion species per site.** That is local dimension 16 against the axioms' single M₂(C) per site (`:47`): a species or block bridge.
- **Vertex functions.** Compact Gevrey invariant-mass plateaus on every created pair, plus the frame-dependent kinematic factor h on every decay vertex, which fermionic statistics force.
- **Frame-fixed leg and total-momentum cutoffs.** Inactive inside a rapidity budget y ≲ ln(Λ₁²/(2 m E_max)), which is set by the vacuum vertex's spectator plateaus.
- **Locality.** Tails that are sub-exponential by necessity.
- **Not shown.** Microcausality and cluster separability.
- **One loop only.** In toy N the structure fails at O(g⁴). Keeping one light cone beyond one loop would need either an order-by-order redesign of the vertex functions (more custodial functional conditions), or a BT-type mass-operator reorganization. Per Polyzou (V) and Keister–Polyzou (V), BT loses vacuum fluctuations, or cluster separability beyond bounded particle number, and is not quasi-local.

## 8. For the referee

1. Rebuild model S from `r84_fock.py:build_S`. Check the CAR sign convention in `apply_ops`, and the RS2 identity in `r84_fock_part1.out`.
2. Check Lemma INV-3F and the identity h/(E − W) + 1/(E + W) = 2CW/(E² − W²) for h = (W(1 + 2C) − E)/(W + E). Confirm that h = 1 gives E_p/W Lorentz violation.
3. Check the spectator bound s_XY ≤ 2m² + 2E_Y(E_p + |p|) and the budget, against the p = 0.45 rows.
4. Check the toy N Goldstone form, especially the four-ordering inner-Z factor (α − b)/(α²b²) and the exchange signs. Rerun `r84_toyN_fock.py F` and `B`.
5. **Decisive open item.** Add the 2↔2 and Y ↔ XAB crossings to toy N with a stated vertex prescription. As a local-limit control, test whether the toy-N ordering subset is non-covariant even for Ψ ≡ 1 (expected, since Feynman covariance needs all orderings).
6. Check whether the two-loop coefficient c tends to zero as m/Λ → 0 (dimension-6) or to a constant (dimension-4). The window tested here is only a factor of 4.
