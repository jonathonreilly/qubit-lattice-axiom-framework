# C5 R7-1 report: box-confined Poincaré (does R6-1's non-analytic trick also break the boost wall?)

**Author.** Claude Opus 5.5 probe (same family as the supervisor, R6-1's worker and every C5 worker). Unrefereed. 2026-10-12, 14:44Z to about 15:50Z. No repository file edited.
**Scratch.** `S/` = `.../scratchpad/C5/R7-1/`. Scripts and outputs: `S/scripts/r71_box_poincare_free.{py,out}` (d = 2, free, real-space lattice check), `S/scripts/r71_bt_twobody.{py,out}` (d = 1 numerics, interacting two-body box law).
**Read.** `docs/MINIMAL_AXIOMS_2026-06-29.md` in full; `TESTS.md:2302-2440` (C5 method and round 1), `:3009-3256` (round 6 and R7-1); `SUMMARY.md:322-567` (§§14-22, incl. §17 boost wall); `TESTS.md:1162-1244` (lane RC, C1/C3), `:1853-1960` (RB, B1), `:2263-2300` (RFW), `:2740-2752` (R2-1); `agents/C4_B1_referee.md`, `agents/C4_I1_referee.md`, `agents/RG_G1G2_referee.md`, `agents/C5_R2-1_referee_verdict.md`; the R6-1 report and its scripts (`.../C5/R6-1/R6-1_report.md`, unrefereed).
**Labels.** proved / checked (numerics here) / suggested / reading / comparator / RECALLED (literature from memory, not verified here).

---

## 0. In plain words

- **Yes, in a stated sector.** Take R6-1's trick and apply it to the energy: make each particle's energy exactly √(m² + k²) for every momentum inside a box |k_i| ≤ B (any B < π), and let it bend back smoothly to a periodic band outside. The boost is then the ordinary first moment of the energy density, as B1 showed it must be. On every state whose momenta sit inside the box, momentum, energy, boosts and rotations obey the exact Poincaré rules. The grid's cos k factor is replaced by exactly 1 inside the box.
- **Interactions can be included, for pairs.** A Bakamjian–Thomas pair interaction, switched off smoothly before either particle leaves the box, gives an exact Poincaré algebra on the two-particle box sector, with real scattering and a bound state. The bound state's energy obeys E² − P² = M_b² exactly, at every total momentum on the plateau. Checked to 1e-10 against 8% drift for the naive pair potential.
- **Boosts are exact up to a rapidity budget.** A state stays exact under a boost until some particle's momentum reaches the box edge. For a Planck-spacing grid that budget is about 45 units of rapidity for a proton at rest and 53 for an electron. The fastest cosmic rays use about 27. A packet whose momenta are strictly inside the box leaks nothing until then. A packet with tails leaks at most twice the weight of its tail that crosses the edge (proved; checked).
- **Why the boost wall does not stop it.** Every refereed boost no-go assumes one of three things: closure on all momenta (C3, I2, B1 Theorems R and D); boosts that can be applied without limit, so the algebra integrates (I1 Theorem 1, B1 Theorem U); or analytic band functions (C1 Theorem B1, R2-1, RFW F1). The box sector violates each by design. The zone-averaged anomaly of −1 per mode is still there (checked), parked entirely outside the box. This is the "patchwise" escape the B1 referee left open.
- **The price.** The same as R6-1's:
  - band and interaction functions are smooth but not analytic, so couplings fall off faster than any power but slower than exponentially;
  - a frame-fixed momentum box, the lattice frame, beyond which Lorentz symmetry fails;
  - a decoupled, non-gravitating sector of zone-edge modes that carries the whole lattice anomaly.
- **What is not shown.**
  - An interacting law with exact boosts for three or more particles and a local boost.
  - Closure of the full local constraint algebra (local lapse, not just the global Poincaré part).
  - Gauge fields.
  - Quantum field theory with pair creation, whose loops would normally reintroduce speed differences at a box cutoff.
- **Against the FIXED readings:** PASS (worker reading), in the scope of §6. A FAIL is impossible in the registered sense: the free and two-body laws are explicit counterexamples to "the box sector cannot carry exact boosts even with a rapidity cutoff".

---

## 1. Hypotheses and classes (stated before any title)

- **H-lat.** One complex fermion mode per site of Z^d (d = 1, 2, 3), so local dimension 2, with a graded tensor product as in R6-1. Translation-invariant, number-conserving Hamiltonians, with time continuous (Z^d × ℝ; a set-C-type law in C5's labels, `TESTS:2424-2428`).
- **H-box.** B = [−b, b]^d, with 0 < b < π. "Box states" are finite-particle vectors whose momentum wavefunctions are C^∞ with compact support in int(B)^N (and in a stated subregion for the interacting law, §4.3).
- **H-gen.** The generators are self-adjoint operators on the whole Fock space. On the box domain they are required to satisfy the Poincaré relations exactly (as operator identities on a common invariant domain). They are **not** required to integrate to a unitary Poincaré representation on the box sector, which is impossible (B1 Theorem U, `C4_B1_referee.md:7`).
- **H-K.** The boost is a first moment of the Hamiltonian density, K = ½{H, X} in one-body form. That is the form B1 Theorem S forces (`C4_B1_referee.md:9`), so nothing is gained by changing the generator.
- **Excluded outside realizations, not addressed:**
  - Euclidean Z⁴ / set B (R6-1 §6 argues reflection positivity plus W(B4) closes the non-analytic door there; suggested, not rechecked);
  - LRL;
  - gauge fields;
  - QFT with pair creation and loops (§5.4);
  - interacting sectors with N ≥ 3 particles (§4.3);
  - the local (non-affine lapse) hypersurface-deformation algebra;
  - the graviton's own nonlinear self-coupling;
  - qubit (⊗M₂, ungraded) realizations beyond R6-1's suggested bosonization.

## 2. Prior art (each counted once)

- **C3 (lane RC):** closure in the constant-shift, linear-lapse and rotational sectors "needs Hess(ω²/2) to be constant. A periodic function with constant Hessian is constant" (`TESTS:1213`).
- **C1 Theorem A** (full-support normal collisions force E² = m₀² + β|k|², `TESTS:1173`). **C1 Theorem B1:** "No finite-component periodic real-analytic one-body matrix has an exact SLAC band on any open set" (`TESTS:1177`).
- **I1/I2/I3:** zone-averaged anomaly −β per mode (`SUMMARY:403`). Exact closure with an *integrated* representation needs a complete tower (`C4_I1_referee.md:7`, Theorem 1, Nelson integrability assumed). Patches within one tower cannot be decoupled "while preserving boost covariance" (`C4_I1_referee.md:13`).
- **M1:** every *globally isolated* composite band has averaged anomaly −βI (`TESTS:1654`; `SUMMARY:405`).
- **B1 (lane RB):** Theorem S (first moment forced), Theorem U (no closure on a bounded K-invariant exponentiating sector), Theorem R (no global smooth action on the BZ), Theorem D (cubic Morse). The referee: "patchwise DSR remains possible, exactly as in Bisio–D'Ariano–Perinotti" (`C4_B1_referee.md:7-11`; `TESTS:1935-1946`; `SUMMARY:394,480`). **This report builds the patchwise, undeformed case.**
- **K2:** Z⁴ e(4) closure fails at O(κ²) (`SUMMARY:406`). Not addressed here (set B excluded).
- **RFW F1:** "Tangency plus closure would force the shell into a complex quadric. That is incompatible with a nonzero finite Fourier kinetic symbol" (`TESTS:2289`). The symbol here has infinite Fourier support.
- **R2-1 Theorem T:** needs globally analytic periodic H₁(k) (`C5_R2-1_referee_verdict.md:3`).
- **RG G3:** sourcing the shift needs an exactly SLAC dispersion (`TESTS:1066`). **RD:** exact SLAC at finite Z needs a 1/r² tail (`SUMMARY:385`). Both concern the *whole zone*.
- **R6-1 (unrefereed):** exact additive Q with box-supported interactions, a = 0.49π (`R6-1_report.md:87-118`). Its last strong-word item says boosts cannot work "as built" because boosts move momenta out of the box (`R6-1_report.md:191`). This report answers that item: true for the full group, false for the local algebra on box states.
- **Comparators, RECALLED:** Bakamjian–Thomas (1953) instant-form construction; Coester–Polyzou / Sokolov on N ≥ 3 cluster separability; Collins–Perez–Sudarsky–Urrutia–Vucetich (2004) on loops carrying Planck-scale Lorentz violation to low energy; Denjoy–Carleman / Beurling (as in R6-1 Prop. N).

---

## 3. The law

**Free part (d arbitrary; numerics in d = 2 and d = 1).**
- s(k) = ρ(k)·k + (1 − ρ(k))·sin k, where ρ is an even C^∞ Gevrey-2 plateau with ρ = 1 on |k| ≤ b and ρ = 0 on |k| ≥ b₂ < π. Then s is C^∞, odd and 2π-periodic, and s(k) = k on |k| ≤ b.
- ε̃(k) = √(m² + Σ_i s(k_i)²), C^∞ and periodic, with ε̃ = √(m² + |k|²) on B.
- H₀ = Σ_k ε̃(k) n_k.
- Momentum: P_j = Σ s(k_j) n_k. This is a smooth version; R6-1's sawtooth Q equals it on box states, and e^{iQ_j} = T_j.
- Position: X_j = Σ_x x_j n_x.
- Boost: K_j = dΓ(½{ε̃, X_j}). In real space, K_j = Σ_{x,y} ½(x_j + y_j) ĥ(x−y) c†_x c_y, the first moment of the Hamiltonian density, with ĥ the Fourier coefficients of ε̃.
- Rotations: J_ab = dΓ(½({X_a, j_b} − {X_b, j_a})), with j = ∇(ε̃²/2) = (s s′)(k_i). In the box j = k.
- Numerics: b = 2.0, b₂ = 3.1, m = 0.3 (script 1); b = 2.6, b₂ = 3.0 (script 2).

**Interaction (two-body Bakamjian–Thomas box law).**
- At total lattice momentum P and on the box region, define:
  - q(P, k₁) = the CM-frame momentum of particle 1;
  - M₀ = 2√(m² + q²);
  - M = M₀ + λ|g⟩⟨g|, with g odd, C^∞, supported in |q| < κ (antisymmetric, so fermion-compatible);
  - W(P) = c(P)·[√(M² + P²) − √(M₀² + P²)], with c a C^∞ plateau (c = 1 for |P| ≤ Π₁, c = 0 for |P| ≥ Π₂).
- Second-quantized: H = H₀ + ½ Σ_P Σ W(P; k₁′, k₁) a†_{k₁′} a†_{P−k₁′} a_{P−k₁} a_{k₁}.
- Numerics: d = 1, a = 0.45π, κ = 0.25, Π₁ = 0.7, Π₂ = 1.0, λ = −2 (bound) and +2.
- The parameters are chosen so that every leg in supp W has |k_i| ≤ 0.49 < a < π/2, with no umklapp (checked, `r71_bt_twobody.out`, (ii)).

---

## 4. Results

### 4.1 Lemma L (box locality) — proved, elementary

- **Setting.** Every one-body generator above is a differential operator of order ≤ 1 on T^d with C^∞ periodic coefficients:
  - H and P are multiplications;
  - K and J are symmetrized first-order operators, with X = i∂_k.
- **Claim.** On int(B) the coefficients equal the continuum ones: √(m² + k²), k, ½{√(m²+k²), i∂}, and k × i∂.
- **Proof.** Differential operators do not enlarge supports. So C_c^∞(int B) is invariant under each generator, and on it each generator acts as its continuum counterpart.
- **Consequence.** Any polynomial identity among the continuum generators that holds on C^∞(ℝ^d) holds for the lattice generators on C_c^∞(int B).

### 4.2 Theorem P1 (free matter, every particle number) — proved; checked

- **Claim.** On the box domain 𝒟_B (finite-particle vectors with C_c^∞(int B^N) wavefunctions), H, P, K, J satisfy the Poincaré relations exactly:
  - [K_a, P_b] = iδ_ab H;
  - [K_a, H] = iP_a;
  - [K_a, K_b] = −iJ_ab;
  - [J, K], [J, P] rotate as vectors;
  - [P, H] = [J, H] = 0.
- **Proof.** Lemma L, the continuum identities, and the fact that dΓ is a Lie homomorphism on finite-particle vectors over an invariant one-body domain.
- **Self-adjointness and the local group.**
  - Each generator is globally self-adjoint: a symmetrized first-order operator with smooth real coefficients on the compact torus generates the unitary flow of a complete smooth vector field (standard).
  - So e^{−iηK} exists for every η. For box states whose orbit stays in int(B), it equals the continuum boost.
  - This gives a *local* Poincaré group action, exact, on box states.
- **The conventions were measured, not assumed** (`r71_box_poincare_free.out`, (C)): [K_x, K_y] = −iJ, [J, K_x] = +iK_y, [J, P_x] = +iP_y.

**Real-space lattice check** (checked, `r71_box_poincare_free.out` (C)). L = 512 torus; every operator is applied in real space by FFT; X is the centred coordinate.

| packet (Gaussian in k) | box law: worst Poincaré residual | NN Klein–Gordon comparator, P = sin k: [K_x,P_x] − iH |
|---|---|---|
| inside, k₀ = (0.4, −0.3), σ = 0.12 | 1.7e-12 ([K_x,K_y] + iJ); others ≤ 6e-12 | 5.6e-2; [J,K_x] − iK_y = 0.33 |
| inside, fast k₀ = (1.4, 0.3), σ = 0.08 | 1.3e-11 | 1.1; [J,K_x] − iK_y = 10 |
| straddles the edge, k₀ = (2.0, 0) | [K_x,P_x] − iH = 0.12 (73% of weight outside) | 2.4 |
| zone edge, k₀ = (2.9, 2.9) | O(1) failures | O(1) |

- The comparator's [K, H] = iP and [K_x, K_y] = −iJ hold exactly, because j = sin k = P. Its failures are exactly the cos k factor in [K, P] and in the rotation relations. In the box law that factor is s′(k) = 1, exactly (`(A)`: max|s′ − 1| = 0 on the box).
- The residual floor of 1e-12 is set by the X² scale and the seam (packet weight near the seam ≤ 9e-16).

**The anomaly is still there, outside the box** (checked, (A)).
- The anomaly (Hess(ε̃²/2) − I)_xx = (s s′)′ − 1 is zero on the box (1.8e-7, from finite differencing) and ranges over −33 … +20 outside.
- Its zone mean is −1.000000, as I2/C3 require.
- So no refereed periodic-Hessian theorem is contradicted; the anomaly is localized, not removed.

**Locality** (checked, (B); proved in class).
- The hopping kernel of ε̃ falls as 1.4e-1, 2.0e-5, 1.9e-9, 1.2e-12 at r = 1, 32, 128, 256 on the axis, and to 6e-18 at (128, 128).
- Non-analyticity is *necessary* (proved, elementary). If ε̃² were real-analytic on ℝ^d, then ε̃² − m² − |k|² would vanish identically, contradicting periodicity.
- With Denjoy–Carleman (RECALLED), ε̃² must lie outside every quasi-analytic class. Hence no e^{−w(r)} hopping decay with ∫w/r² = ∞ (exponential excluded). This is the same price, and the same class, as R6-1's Prop. N.

### 4.3 Theorem P2 (interacting, two-particle box sector) — proved (BT RECALLED + Lemma L + Lemma Sm); checked

- **Domain.** 𝒟₂ = antisymmetric two-particle wavefunctions, C^∞ with compact support in the open set R′ = {(P, q): |P| < Π₁, both legs in int(B) ∩ (−a, a)^d}. The parameters are chosen so that {|P| ≤ Π₁, |q| ≤ κ} ⊂ R′.
- **Invariance.** 𝒟₂ is invariant under H:
  - √(M₀² + P²) is a multiplication;
  - W(P) is an integral operator in q at fixed P, with kernel supported in supp g × supp g (shown below), so W maps into {|q| < κ} ⊂ R′.
  - 𝒟₂ is also invariant under the BT boost (differential in P at fixed q, plus H) and under the BT rotations.
- **Coincidence with BT.** On R′:
  - c(P) = 1;
  - ε̃ is relativistic;
  - P = k₁ + k₂ as real vectors (no umklapp);
  - the lattice K₀ and J₀ are the continuum free generators (Lemma L).

  So the lattice two-body operators on 𝒟₂ are exactly the BT operators: H = √(M² + P²), K = −½{H, X_NW} − (S × P)/(M + H) in d ≥ 2 (no spin term in d = 1), and J = X_NW × P + S. BT closure follows from [X_NW, P] = i, with M commuting with P, X_NW and S (RECALLED; algebraic).
- **The boost.** Define the interacting lattice boost as K₀ + K_W, with K_W the two-body operator K_BT − K₀ cut off by c(P). Then the Poincaré relations hold exactly on 𝒟₂.
- **Lemma Sm (smoothness of W) — proved.**
  - √· is analytic on a neighbourhood of spec(M² + P²) ⊂ [M_b² + P², ∞), which needs M_b > 0 (here M_b = 0.557).
  - So W = (1/π)∫₀^∞ t^{1/2}(A + t)^{-1}(A − A₀)(A₀ + t)^{-1} dt, with A = M² + P² and A₀ = M₀² + P².
  - A − A₀ = M₀v + vM₀ + v² is finite-rank with C^∞ compactly supported kernels. The resolvents are taken at real negative spectral parameter, away from the spectrum, so no threshold singularity enters.
  - Hence W(P; q′, q) is C^∞ in (P, q′, q), supported in supp g × supp g, and its real-space kernel decays faster than any power.
  - Threshold singularities live only in on-shell boundary values, never in the operator kernel.
- **Checks (`r71_bt_twobody.out`):**
  - (ii) W vanishes outside supp g × supp g (0.0); all legs lie in the interaction box; the real total momentum is conserved (no umklapp, max|k₁ + k₂ − P| = 0).
  - (i) Bound state below threshold 2m = 0.6, with √(E² − P²) = M_b = 0.5573391 at six plateau momenta 0 ≤ P ≤ 0.69. The spread is 6.7e-9 at L = 600, falling to 1.2e-10 at L = 800 (finite-L only).
  - (i) **Comparator** (same g as a Galilean pair potential in lattice relative momentum): the invariant mass drifts 0.557 → 0.481 over the same range (spread 7.6e-2).
  - (i) In the transition region c < 1, invariance fails (0.590 at c = 0.58). At c = 0 the bound state is gone (0.600024 ≈ threshold).
  - (iv) The on-shell internal t-matrix is nonzero: |t| = 0.02–0.14 at q = 0.05–0.20, for λ = ±2. It is P-independent by construction.
  - (iii) The real-space kernel of W falls from 5.5e-6 to 3.9e-8 by separation 79 at L = 160. Its range is set by 1/κ and 1/(Π₂ − Π₁). Only two decades are resolved; super-polynomial decay is the proved statement, not this number.
- **M1 is not contradicted.** The composite band exists only on the P-plateau; it is not globally isolated, which is M1's hypothesis (`TESTS:1654`).

**N ≥ 3 — not established.**
- The second-quantized law acts pairwise in the N-particle sector, H_N = H₀ + Σ W_ij.
- With a pairwise boost K₀ + ΣK_W,ij, cross terms such as [K_W,12, W₂₃] do not cancel. Instant-form relativistic N-body dynamics needs many-body terms (Coester–Polyzou, Sokolov packing operators; RECALLED).
- An exact but non-local K = Ω₊K₀Ω₊* always exists given complete wave operators. That is the trivial intertwiner algebra and is not claimed.
- So exact Poincaré for the interacting law with a quasi-local, cluster-separable K is **OPEN** for N ≥ 3. Box confinement neither helps nor hurts this problem.

### 4.4 Rapidity range and leakage — proved; checked

- **Exact range.** For a box state with momentum support C ⊂ int(B) and boost direction n: e^{−iηK_n}ψ = U^c_η ψ exactly for |η| < η*(C, n) = sup{η : the continuum orbits Φ_t(C), |t| ≤ η, stay in int(B)}.
  - For an axis boost of a leg with transverse mass m_⊥ and rapidity θ: η* = asinh(b/m_⊥) − |θ|.
  - For N legs, take the minimum over legs.
  - For the interacting two-body law, use the orbit of the total momentum and require |P(η)| < Π₁ as well.
- **Leakage bound.** For any ψ: ‖e^{−iηK}ψ − U^c_ηψ‖ ≤ 2‖1_{E_η}ψ‖, where E_η is the set of momenta whose continuum orbit over [0, η] leaves the box. (The two flows and their Jacobians agree off E_η.)
  - Checked for a Gaussian packet at rest, σ_k = 0.25, m = 0.3, b = 2.0 (`(D)`):

| η | actual leakage | bound 2‖1_E ψ‖ |
|---|---|---|
| 0.5 | 1.3e-5 | 1.9e-3 |
| 1.0 | 5.8e-3 | 0.11 |
| 1.5 | 9.4e-2 | 0.55 |
| 2.0 | 0.35 | 1.09 |

- **Physical budgets (reading).** Assume a Planck-spacing grid with box edge b = 2.0/ℓ_P:
  - reach at rest: electron 52.9, proton 45.4, top 40.2;
  - a 3e20 eV proton has lattice-frame rapidity 27.2, leaving 18.2;
  - every observed process sits deep inside the exact region.
  - For box-sector processes the dispersion and two-body S-matrix are exactly Lorentz invariant. So dimension-n LIV coefficients of *every* n vanish identically, and time-of-flight or threshold bounds are met trivially.
  - This ignores §5.4.

### 4.5 Ward identity for a linearized graviton coupled to the box sector

- **(W1) O(h) conservation — proved.**
  - Take T^{μν}(q) = Σ_k χ(k+q)χ(k) F^{μν}(k+q, k) a†_{k+q}a_k, with:
    - F^{μν}(k′, k) = [k′^μk^ν + k^μk′^ν − η^{μν}(k′·k − m²)]/(2√(ε′ε)), the one-particle matrix element of the free-scalar continuum T;
    - χ a C^∞ box plateau inside (−a, a)^d, with 2a ≤ b.
  - Give the graviton the spatial difference symbol ŝ(q) = s(q), equal to q for |q_i| ≤ b.
  - Then ŝ_μT^{μν} = 0 holds as an operator identity, every matrix element:
    - the continuum on-shell identity q_μF^{μν} = 0 is algebraic (shown in-line: (q·k)k′^ν + (q·k′)k^ν − q^ν(k′·k − m²) = 0);
    - multiplying by the scalar cutoff χχ preserves it;
    - on the support of χχ, q = k′ − k is real with |q_i| ≤ 2a ≤ b.
  - T is symmetric, ∫T^{00} = H and ∫T^{0i} = P on box states, and the linearized EH action with ŝ is gauge invariant for any symbol (algebraic).
- **(W2) Soft / constant-ξ Ward identity — proved, in the box.** The coupling at q → 0 is p^μp^ν/E with p = (ε̃, k) on box legs. Q is exact and additive (R6-1; the interaction here is also box-supported, so the R6-1 two-line argument applies), and energy is conserved. The charge has R2-1's form τ = aω + b·k (`TESTS:2750`) with b ≠ 0, realized by a *non-analytic* one-body symbol, which is outside R2-1's hypothesis.
- **(W3) Affine-ξ sector of the O(h²) closure, C3's sectors — proved, in scope.**
  - C3's constant-shift, linear-lapse and rotational sectors are the global Poincaré algebra (`TESTS:1211-1213`).
  - P1 closes them exactly on box states, for free matter at every N.
  - P2 closes them for the interacting two-body box sector.
  - The edge modes carry the anomaly and are excluded from T by χ.
- **(W4) Local lapse (non-affine ξ) at O(h²) — not addressed. OPEN.**
  - It needs the commutator algebra of the box densities themselves.
  - For positive-energy number-conserving bilinears, the continuum free field closes the local Dirac algebra only with its pair (aa, a†a†) terms (suggested; not computed).
  - So this item is not claimed.

---

## 5. What fails at the box edge (quantified)

1. **States near the edge** (checked). Poincaré residuals are O(1) on packets straddling or outside the box ((C), rows 3–4). The anomaly there takes values up to 33 ((A)).
2. **Finite boosts.** The exact range is η*(state) (§4.4). Beyond it, leakage is bounded by 2‖1_E ψ‖. Leakage is zero for compactly supported packets until η*.
3. **The edge sector.** Modes with some |k_i| > b are free (interactions are box-supported) and non-gravitating (χ = 0). They carry the full zone-averaged anomaly −1 per mode, and they are never produced from box states:
   - the box sector is dynamically closed: H₀ conserves each k, and W maps box pairs to box pairs (proved);
   - the graviton coupling is also box-to-box.

   Reading: an inert, sterile sector. The equivalence principle fails only for quanta with Planck-scale lattice-frame momenta, and in the transition shell where χ < 1.
4. **Comparison with lane RC's "whole-zone SLAC" requirement** (C1/RG G3/RD). Those require SLAC across the zone because the graviton couples to all modes. Restricting the gravitating sector to the box reduces the requirement to "SLAC on the box". C∞ non-analytic bands meet that with super-polynomial tails, not 1/r² tails. RD's 1/r² statement is about exact SLAC at the zone face, which is not needed here.
5. **Loops and pair creation (suggested; the main open physics risk).** The construction keeps the box sector closed because interactions are number-conserving with compact support in relative and total momentum. A local QFT with point vertices has loop momenta up to the cutoff. With a frame-fixed box this regulator is Lorentz-violating and, by the Collins et al. mechanism (RECALLED), feeds dimension-4 speed differences into the infrared. The in-repo comparator is F2's 8.55e-3 QED split (`SUMMARY:423`).
   - A Lorentz-invariant escape would need every vertex to carry a form factor with compact support in *invariant* masses or relative momenta, as BT's g(q) does. Then virtual states reached from low-momentum states stay deep inside the box.
   - That is a non-local (form-factor) dynamics at the form-factor scale. Not constructed for pair-creating theories.
6. **Gauge fields (suggested).** Lattice minimal coupling links every charged mode, edge modes included. A box-supported gauge coupling is not lattice-gauge-invariant. Not addressed.

---

## 6. Reading against the FIXED readings (`TESTS:3252-3255`)

- **PASS — worker reading, referee required.** All clauses are met:
  - **(a)** an explicit finite-per-site law: one fermion mode per site, graded tensor product, as R6-1;
  - **(b)** an exact Poincaré algebra on a stated box sector:
    - free matter, every particle number, on 𝒟_B (Theorem P1);
    - the interacting two-body BT box law on 𝒟₂ (Theorem P2), with nonzero scattering and a bound state;
  - **(c)** a stated rapidity range η*(state), ≥ asinh(b/m_⊥) − θ_max per leg;
  - **(d)** the leakage bound 2‖1_E ψ‖, proved and checked;
  - the algebra itself is checked in real space on the lattice to 1e-11 (inside the box).
- **Scope of the PASS (must travel with it).**
  - Fermionic graded composition; the ⊗M₂ qubit version only via R6-1's suggested flux-free bosonization.
  - Couplings and hoppings with super-polynomial but sub-exponential tails (necessary, §4.2).
  - The interacting statement holds for N ≤ 2 only. N ≥ 3 with a quasi-local, cluster-separable boost is OPEN (§4.3).
  - Ward identity: O(h) conservation, soft identity and the affine (C3) sector only. The local-lapse algebra is OPEN.
  - No gauge fields and no pair-creating QFT (§5.4–5.6).
  - Continuous time (Z^d × ℝ); set B is excluded.
- **FAIL is not available in the registered sense.** P1 and P2 are explicit counterexamples to "the box sector cannot carry exact boosts even with a rapidity cutoff".
- **Against the round's question** ("is 'approximately local in rapidity' good enough to evade C3/I1?").
  - It is not approximate: it is exact up to η*.
  - It evades C3, I1–I3, M1, B1 (Theorems U, R, D), C1-B1, R2-1 and RFW-F1 by violating their stated hypotheses, not their conclusions:
    - closure on all momenta;
    - integrated or exponentiating representations;
    - a globally isolated band;
    - analytic or finite-Fourier symbols.
  - B1 Theorem S is satisfied: K is the first moment of H.
  - The zone-averaged anomaly −1 survives outside the box (checked), exactly as I2 requires.

## 7. Strong-word check

- "Exact" means an operator identity on the stated domain (𝒟_B, 𝒟₂), not on the full Fock space; on the full space the relations fail at the edge.
- "Every particle number" applies to free matter only.
- "Proved" for P2 rests on the BT theorem (RECALLED, standard) plus Lemmas L and Sm, both proved here.
- "Lorentz invariant S-matrix" is two-body only, on the P-plateau.
- "No LIV at any order" is a reading. It covers box-sector processes of number-conserving, form-factor dynamics, and ignores §5.4.
- Nothing here gives an exact graviton on a grid. It shows that the global-Poincaré part of the boost wall has a patchwise exit at R6-1's locality price.
- It does not touch the one-cone question across species. In the box each species has c = 1 exactly, so speeds agree by construction for free and BT-interacting matter. Whether loops of gauge interactions keep that is §5.5–5.6.

## 8. Price (named, not adopted)

"Band functions and interaction kernels that are C^∞ but outside every quasi-analytic class (super-polynomial, sub-exponential tails); a frame-fixed momentum box in the lattice frame, with exact Lorentz covariance only for states whose orbits stay inside it; an inert non-interacting, non-gravitating zone-edge sector that carries the whole lattice anomaly; and form-factor (not point-local) interactions". This extends R6-1's named price (`R6-1_report.md:196`) from momentum to the global Poincaré sector. It adds no new axiom text beyond R6-1's question on graded composition (`R6-1_report.md:195`; `AX:45-53`). Admissibility does not fix the dynamics (`AX:114-125`).

## 9. For the referee

Check, in order:
1. Lemma L, and that 𝒟_B and 𝒟₂ are invariant under all generators, including H's two-body part.
2. Lemma Sm: the smoothness of √(M² + P²) − √(M₀² + P²) with finite-rank smooth v and M_b > 0.
3. That the BT algebra applies verbatim on R′ (no umklapp; c = 1; Jacobians).
4. The leakage bound's two-flow argument.
5. Whether PASS's "stated box sector" may be the free all-N sector plus the interacting N ≤ 2 sector, or must be an interacting all-N sector. If the latter, the strongest reading is INCONCLUSIVE, with P1 and P2 as the bounded positive results and N ≥ 3 open.
6. The W1 identity with the lattice symbol ŝ and 2a ≤ b.

Scripts reproduce in a few minutes each (`OMP_NUM_THREADS=2`).
