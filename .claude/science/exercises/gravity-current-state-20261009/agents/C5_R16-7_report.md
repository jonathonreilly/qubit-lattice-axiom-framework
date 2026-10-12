# C5 R16-7: does a finite-slot N-type model at strong penalty have an Einstein–Hilbert TT stiffness?

**Worker.** Claude Opus 5.5 (same family as the supervisor and every C5 worker). 2026-10-12, 22:50Z to 23:20Z. **Unrefereed.** I edited no repository file. Scripts and outputs are in `S/scripts/` (s1 and s2; each run is under 2 min on 2 threads). The method statement was written before any run, at 23:08Z: `S/METHOD_preregistered.md`. I downloaded nothing.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`. The R16-7 registration is `TESTS:5259-5285`, with the FIXED readings at `:5282-5284`.
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `N0914` = `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`.
- `R15-5` = `P/agents/C5_R15-5_report.md`. `vR15-5` = the referee verdict, read at `scratchpad/C5/ref_R15-5/REFEREE_VERDICT.md` and archived as `P/agents/C5_R15-5_referee_verdict.md`.
- `R13-2` = `P/agents/C5_R13-2_report.md`.
- `S` = `scratchpad/C5/R16-7/`.

**Labels.**
- proved: a derivation made here (unrefereed);
- checked: numerics run here;
- suggested: an argument, not a proof;
- reading: an interpretation;
- comparator: literature (RECALLED, not fetched).

---

## 0. Plain words

- **The question.** Can a lattice of finite "slots" carrying the gravity-type tensor gauge structure, with all couplings of comparable size, give the metric the stiffness of Einstein–Hilbert gravity? That stiffness means a static TT response ~ 1/k² and an attractive 1/r pull between scalar ("mass") charges.
- **The method.** Simulating the 3D model is out of reach: exact diagonalization would need more than 100 qubits, and Monte Carlo has a sign problem. I used exact operator inequalities instead (sum rules, the Bogoliubov inequality and the diamagnetic inequality). They hold in every ground state at every coupling and need no perturbation theory or system-size extrapolation. Their limit is that they say nothing outside their stated hypotheses.
- **Result 1, the TT channel (proved; checked).** Suppose the microscopic Hamiltonian conserves the vector Gauss law exactly and the metric slots are compact (rotors, or finite quantum-link "slots", which includes qubits). Then the static TT metric susceptibility is **at least c/k⁴ at every coupling**, so the Einstein–Hilbert 1/k² is impossible. The reason is one line. The sum rule for the TT electric field is built only from gauge-invariant metric "hops", and every such hop has a k² symbol (N0914's lemma). So the sum rule is O(k⁴), and Bogoliubov turns that into χ_TT ≥ c/k⁴. The penalty size, the scalar constraint (exact or energetic) and the electric-side energy (including the indefinite N-type form) do not enter.
- **Result 2, the scalar channel (proved).** Suppose the model is sign-free in the electric basis and conserves the scalar ("mass") charge. Then inserting any pattern of scalar charges can never lower the energy below the vacuum. So like charges cannot have an unscreened Newtonian attraction, in any model of this kind. In the sign-free class that also conserves the vector law, the scalar response is contact-type: no 1/k² of either sign. **The sign problem and gravitational attraction are the same obstruction.** This lifts R13-2's product-basis sign lemma to a physical statement.
- **(a) A sign-free basis exists.** It exists for N0914's finite-clock tensor Hamiltonian: the electric (X) basis, at every N, U, J and g (proved by inspection). By Results 1 and 2, however, that is exactly the class that cannot give either registered signature.
- **The dual picture.** Take the metric to be integer-valued and the electric side compact (the "dual rotor"). The Einstein–Hilbert static response is then possible, but it forces a TT excitation with ω ≤ Ck². So the registered static signature does not certify a light-speed graviton. This proves vR15-5's correction non-perturbatively in that class.
- **What is left.** The only window is a microscopic Hamiltonian that **violates the vector Gauss law** (and, for the scalar channel, violates the scalar law or carries the sign problem), with the gauge structure emerging only in the infrared. That is Gu–Wen's lattice N-type and R13-2's 𝒟₀. It is also mod-N clocks at small N, where integer lifting fails. No controlled method reaches it here.
- **Reading.**
  - In the Gauss-law-conserving finite-slot class: **NOT-PRODUCED-EVIDENCE**, pending the referee. The method gives exponent 2 for the U(1) photon control and exactly ≥ 4 for the tensor.
  - For the registered setting as a whole: **INCONCLUSIVE**, because its vector-law-violating part is not reached.

---

## 1. Method and control parameter (stated before running; `S/METHOD_preregistered.md`)

**Method M** (controlled, non-perturbative): exact inequalities in the ground state |0⟩ of the stated class. C is any operator, A any probe, and ω_n = E_n − E_0.
- **(M1) f-sum.** m₁(C) = ⟨[C†,[H,C]]⟩ = Σ_n ω_n(|C_n0|² + |C†_n0|²).
- **(M2) Bogoliubov.** |⟨[C,A]⟩|² ≤ m₁(C)·χ_AA, with χ_AA = Σ_{n≠0}(|A_n0|² + |A†_n0|²)/ω_n (Cauchy–Schwarz). Equality holds for A = [H,C]†, the "current".
- **(M3) Diamagnetic.** If H is stoquastic in a basis, putting phases on its off-diagonal elements cannot lower E₀.
- **(M4) Softness.** ω_min(k)² ≤ m₁(C)/χ_CC, where ω_min is the lowest excitation that C or C† connects to |0⟩.

**Definitions fixed before running.**
- **Metric susceptibility.** χ_TT(k) := χ_AA/|⟨[E_TT(k),A]⟩|² for a gauge-invariant TT probe A, with E_TT(k) = Σ_x e^{ikx} ε_TT(k)·E(x). By (M2), inf_A χ_TT = 1/m₁(E_TT), attained at the current.
  - On every Gaussian rung this equals χ_hh^TT. Checked in s1 (T4): the N-type gives 1/(gq̂²) = 1/m₁ and the L-type gives 1/(gq̂⁴) = 1/m₁, with χ·m₁ = 1.000000 in all directions.
- **Scalar-source response.** W(k) = ∂²E₀(ρ)/∂ρ_k∂ρ_{−k} in the conserved scalar-charge sector ρ. The N-type Gaussian gives W = −g/(4q̂²) (`N0914:290-292`; R15-5 s1(7)).

**Control parameter.**
- Rotors and quantum-link (QLM) truncations: none; the inequalities are exact.
- Z_N clocks: the aliasing and wrap ratio, which sets a k-floor (§8, suggested).
- Numerics: exact lattice symbols at k = 1e-3 to 0.3 along five directions. The k-power is the log-log slope. **Subtraction: none.** Invariant patterns have zero 0th and 1st moments, so m₁ has no constant or k² term to subtract in the tensor case. Checked: m₁/k⁴ tends to a constant.

**Control (c), same method.** A cubic-lattice U(1) link-qubit ice / ring-exchange model (the spin-ice analogue), plus an ED algebra check on a 2D U(1) QLM with a 4×4 torus.

---

## 2. Hypotheses, classes, excluded realizations

**Class 𝒬_E (Theorem B).**
- **Slots.** Each slot carries an integer-valued E: either a rotor (E ∈ Z) or a quantum-link truncation (E in a finite integer window, spin S ≥ ½; spin-½ = qubit). Metric "hops" T_m shift E by an integer pattern m, with [E_a, T_m] = m_a T_m exactly. For rotors, T_m = e^{im·h}; for QLM, T_m is a product of S^±.
- **Hamiltonian.** Every Hermitian H expands as H = Σ_m T_m f_m(E).
- **Hypotheses.**
  - (B1) **Exact vector Gauss law:** [H, (GE)_j] = 0 for all j. Equivalently, G m = 0 over Z for every m present, with G the integer stencil of `N0914:95-97`.
  - (B2) **Quasi-locality:** Σ_m ‖f_m‖ μ₂(m)² < ∞ per site, with μ₂ as in `N0914:239-246`.
  - (B3) Translation invariance, for the k-labels.
- **Not assumed:**
  - the scalar law (it can be exact, energetic or absent);
  - the form of the electric-side energy (any F(E), including the indefinite N-type E:E − ½(trE)², penalties of any size, and scalar-violating X-characters);
  - the coupling regime;
  - stoquasticity.

**Class 𝒟 (Theorem D).**
- Rotors (E ∈ Z, unitary h-characters), or Z_N clocks with discrete twists.
- H stoquastic in the E basis.
- **Exact scalar-charge conservation:** [H, e^{iS_x h}] = 0 for all x.
- The vector law may be violated.

**Class 𝒬_h (dual, §7).** The same as 𝒬_E with the roles of h and E exchanged: h integer-valued, the electric side entering via shifts r, and an exact scalar law (S r = 0 for every shift).

**Excluded realizations.** Nothing negative here covers:
- microscopic violation of the vector law (Gu–Wen's energetic constraints with non-commuting terms; R13-2's 𝒟₀ term (κ_B/2) sin h·B_N·sin h);
- mod-N clocks below the k-floor of §8 (including N = 2 in the Weyl/clock representation);
- non-quasi-local H (infinite μ₂ sums);
- infinite-order emergent gauge structures that are not unitarily dressed (§9);
- fermionic slots;
- nonlinear gravity, Λ, matter.

---

## 3. Prior art (each counted once)

1. **R15-5 and vR15-5.**
   - The ladder, Lemma W and the decisive computation (`R15-5:276-279`).
   - The referee's corrections:
     - Lemma W holds only for orders with N > 36nM; the fixed-N, U ~ J ~ g regime stays open (`vR15-5:33-35`);
     - "a 1/k² static h-susceptibility also occurs on the dual-rotor z = 2 rung, while both compact-h rungs have 1/k⁴, not 1/k⁶" (`vR15-5:45`).
   - I adopt the 1/k⁴ correction. §7 proves the dual-rotor point non-perturbatively.
2. **N0914.**
   - The character/moment lemma: every vector-invariant h-character has an O(k²) symbol, with zero 0th and 1st moments (`N0914:203-207,227-246`).
   - The finite-clock Hamiltonian and its signs (`:151-161`).
   - Integer lifting (`:109-114`) and the source comparators (`:282-295`).
   - Theorem B is the non-perturbative, f-sum form of that lemma. The lemma is the only structural input.
3. **R13-2 and its referee.**
   - X-S: no sign-free product-basis Euclidean form of the N-type (`R13-2:59-71`). The referee narrowed this to "the literal U(1) quadratic comparator is unbounded and the tested Z₄ completion is nonstoquastic under every affine rephasing" (`P/agents/C5_R13-2_referee_verdict.md:23`).
   - Theorem D gives the physical reason, in a different class.
   - X-G and Lemma P (`TESTS:4758-4772`).
4. **The repo's ring-model U(1) photon program (the f-sum for link-qubit ice).**
   - m₁ = 2u s², and ω_min ≤ m₀/m₋₁ ≤ sqrt(m₁/m₋₁) ≤ m₁/m₀ (`docs/RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md:26-32`).
   - On small tori the Feynman photon bound "shows no resolved power"; "neither a few sizes nor an inferred static exponent establishes a photon or phase" (`docs/RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24.md:22,28`).
   - My U(1) control's f-sum is this prior art, counted once. I use it only as the same-method control. That note's negative is also the reason I did not attempt a numerical small-torus fit for the tensor.
5. **Lane R** (`TESTS:685-776`), **R12-5** (`TESTS:4543-4551`) and **R11-2 X1** (`TESTS:4407-4409`).
6. **Comparators (RECALLED, not fetched):**
   - Hermele–Fisher–Balents 2004 (the emergent photon in quantum spin ice, χ ~ 1/k²);
   - QSI quantum Monte Carlo (Shannon et al. 2012; Benton–Sikora–Shannon 2012);
   - Gu–Wen 0907.1203 (the N-type is uncontrolled; `N0914:374-375`);
   - Xu 2006; Pretko 2017;
   - the Bogoliubov inequality and f-sum rule (Pitaevskii–Stringari);
   - the diamagnetic inequality for stoquastic Hamiltonians;
   - the Euclidean conformal-factor problem (Gibbons–Hawking–Perry 1978).

---

## 4. (a) A sign-free basis

**Lemma S0 (proved, by inspection of signs).** N0914's finite-clock Hamiltonian (`N0914:151-157`) is stoquastic in the X-eigenbasis (the E-label basis |n⟩) for every N ≥ 2 and all positive U_v, U_s, J, g.
- Z^m is a permutation matrix with unit entries in this basis. So each term c(1 − Re Z^m) with c > 0 has off-diagonal entries −c/2 ≤ 0, or −c when 2m ≡ 0 mod N. Sums of such terms stay ≤ 0.
- The H0 vector penalty and the J-term are X-characters, which are diagonal.
- Hence a sign-free path-integral QMC exists for this model at every coupling. This is new relative to R13-2's Lemma S, which concerned the N-type quadratic content and not this Hamiltonian.

**Scope.**
- N0914's model is L-type: its symbol is |C(E)|² + |R(h)|² (`N0914:163-165`).
- By Theorem B (§5, in its rotor/QLM form) and Theorem D (§6, exact for clocks), this sign-free class gives neither registered signature.
- For the N-type quadratic content no product basis is sign-free (R13-2 X-S as narrowed). Theorem D shows that this is not an artefact of the basis choice for the scalar channel: in the E basis, sign-freeness plus scalar conservation excludes the attraction itself.

---

## 5. Theorem B: the TT channel (proved; checked)

**Statement.** In 𝒬_E, for every ground state, every coupling and every TT polarization ε = ε_TT(k):

m₁(k) := ⟨[E_TT(k)†,[H,E_TT(k)]]⟩/V = Σ_{[m]} |ε·m̂(k)|² w_m,  with w_m := −⟨T_m f_m(E) + h.c.⟩/V per translation class,

and |ε·m̂(k)| ≤ |k|²μ₂(m)/2, so that m₁(k) ≤ (k⁴/4) Σ_{[m]} 2‖f_m‖μ₂(m)² =: C_H k⁴. Hence, for every probe A,

**χ_TT(k) = χ_AA/|⟨[E_TT,A]⟩|² ≥ 1/m₁(k) ≥ 1/(C_H k⁴),**

with equality in the first step for A = the TT electric current [H, E_TT]†.

**Proof.**
- **(i)** [E_a, T_m f(E)] = m_a T_m f(E) exactly, for rotors and QLM alike. F(E) and every X-character commute with E_TT. So only the hops contribute, each with the factor |Σ_slots e^{ik·x} ε·m|² = |ε·m̂(k)|².
- **(ii)** (B1) means G m = 0 over Z, so N0914's moment lemma gives m̂(k) = O(k²), with the Taylor remainder bound of `N0914:239-242`. The scalar-penalty patterns (S-rows) contribute exactly 0 on TT, because ε_TT : (q̂q̂ᵀ − q̂²I) = 0.
- **(iii)** Apply (M2). ∎

**Checked (s1, five directions, k = 1e-3 to 0.3).**

| Contribution to m₁_TT | Slope |
|---|---|
| R-row characters | 3.998–3.999 |
| Random local invariant patterns (R a + Sᵀb, integer trig-polynomial coefficients) | 3.993–4.000 |
| S-rows | ≤ 4.3e-34 (zero) |
| R13-2's non-invariant 𝒟₀ term sin h·B_N·sin h | 1.999 |

- The Bogoliubov ratio for A = the curvature character is a k-independent constant (0.25–0.5).
- On the Gaussian rungs, χ·m₁ = 1.000000.

**Corollary B2 (proved).** By (M4), ω_min(k)² ≤ m₁/χ_{E_TT E_TT} ≤ C_H k⁴/χ_EE. So if the TT electric susceptibility stays bounded below (χ_EE ≥ c_E > 0, as in the N-type Gaussian, where it equals 1/J), there is a TT excitation with ω ≤ sqrt(C_H/c_E) k²: a z ≥ 2 mode.
- A z = 1 lowest TT branch in 𝒬_E needs χ_EE^TT ≤ O(k²): long-wavelength TT electric fluctuations suppressed like an incompressible fluid. I could not exclude this; the Bogoliubov lower bounds on χ_EE pick up an O(1) incoherent part from compactness (suggested).
- Even then, Theorem B keeps the static metric response at ≥ c/k⁴. That is not Einstein–Hilbert.

**What B does that earlier results did not.**
- X1, the N0914 lemma, DW-q and Lemma W are statements about a regular small-field expansion or a convergent Schrieffer–Wolff series, which vR15-5 limits to N > 36nM orders.
- Theorem B uses neither. It is an exact identity for the bare H in any phase, with penalties of any size (U ~ J ~ g included), and it is insensitive to whether the scalar constraint is exact or energetic.

---

## 6. Theorem D: the scalar channel and the sign problem (proved)

**Statement.** In 𝒟, let E₀(ρ) be the ground energy of the sector e^{iS_x h} = e^{iρ_x}, where ρ_x ∈ [0, 2π) for rotors (neutral, Σρ ≡ 0) and ρ_x ∈ (2π/N)Z for clocks. Then **E₀(ρ) ≥ E₀(0) for every ρ.**

**Proof.**
- e^{iS_x h} shifts E by Sᵀe_x. Sector ρ is the Bloch sector on the orbit graph Z^{slots}/SᵀZ^V. Its Hamiltonian H_ρ([E′],[E]) = Σ_β ⟨E′ + Sᵀβ|H|E⟩e^{iρ·β}.
- Stoquasticity gives |H_ρ| ≤ |H₀| entrywise off the diagonal, and Re diag H_ρ ≥ diag H₀.
- Then (M3): ⟨ψ|H_ρ|ψ⟩ ≥ ⟨|ψ||H₀||ψ|⟩ ≥ E₀(0). ∎

**Corollaries.**
- **D1 (proved).** For rotors, wherever E₀(ρ) is twice differentiable at ρ = 0, the linear-response kernel satisfies W(k) ≥ 0 for every k ≠ 0. A Newtonian form W = c − a/k² with a > 0 is therefore excluded. Any scalar attraction must be screened, with range ≤ sqrt(a/c).
  - The N-type Gaussian has W = −g/(4q̂²) < 0, with no core at all (`N0914:290-292`), so it violates D maximally.
- **D1′ (suggested, for clocks).** A neutral, compensated blob of like charges of radius r costs a core ∝ r³ and gains a Newtonian binding ∝ r⁵. So any unscreened inverse-Laplacian attraction violates D at large r. This assumes the response keeps its linear form at that scale.
- **D2 (proved, in the stoquastic class that also satisfies B1, for rotors).** The upper bound 0 ≤ W(k) ≤ w(k) holds, with w(k) = O(1) analytic.
  - It comes from the trial state e^{iE·h_ρ}|0⟩, minimized over h_ρ with S h_ρ = ρ.
  - The quadratic form B_eff = Σ w_m m̂m̂† is O(k⁴) and PSD (w_m ≥ 0 by Perron–Frobenius), while Ŝ = O(k²). So the minimum is O(|ρ|²). The scalar penalty adds the core U_s(1 − cos ρ_x).
  - The first-order (current) term vanishes for a real Perron ground state.
  - So the scalar response is contact-type, with no 1/k² of either sign.

**Reading.**
- In the E basis, sign-freeness plus scalar conservation forbids gravitational (like-charge, unscreened) attraction.
- This is the lattice, Hamiltonian form of the Euclidean conformal-factor problem (comparator).
- R13-2's X-S located the sign problem in the trace/conformal sector. D shows that the attraction needs it, in this class.

**Checked (s2, an M3/M2/M4 algebra check, not the tensor model).**
- 2D U(1) QLM on a 4×4 torus (2970 Gauss-law states; ground state in the zero-winding sector, dim 990, Perron vector positive). Runs at V = 0 and V = −0.5.
- 20 random plaquette twists: min(E₀(θ) − E₀(0)) = 1.5e-4 > 0, with zero violations.

---

## 7. The dual class 𝒬_h: an Einstein–Hilbert static response forces z ≥ 2 (proved)

**Setting.** h is integer-valued: a rotor in h, or the h-QLM truncation, which includes the dual rotor of `R15-5:166-170`, the nearest miss. The scalar law is exact, so every electric shift r has S r = 0. F(h) is arbitrary and diagonal (for example h:R(h)).

**Statement.**
- Exactly as in §5 with roles exchanged: m₁(h_TT) = Σ|ε·r̂(k)|² w_r = O(k²), because every scalar-invariant E-character is O(k) (`N0914:205-207`).
- By (M4), ω_min(k)² ≤ m₁(h_TT)/χ_{h_TT h_TT}.
- So if the static TT metric response is Einstein–Hilbert (χ_hh ≥ c_h/k²), then for each TT polarization there is an excitation with **ω ≤ C k²**.

**Consequences.**
- An EH static response with exactly two linear TT branches is impossible in 𝒬_h.
- The registered PRODUCED-EVIDENCE signature (χ_TT ~ 1/k² plus a 1/k² scalar response) is met at the Gaussian level by the dual rotor, which has z = 2.
- This makes vR15-5's correction (`vR15-5:45`) non-perturbative in 𝒬_h. The FIXED PRODUCED clause, if it were ever met, would not by itself certify a light-speed graviton (reading).

---

## 8. Z_N (mod-N) clocks (suggested)

- With C = Σ e^{ikx}ε·X, the commutator symbol becomes Σ e^{ikx_a}ε_a(ω^{m_a} − 1) = (2πi/N)ε·m̂(k) + O((2π/N)²·(m²)^(k)). The squared-pattern term is not suppressed at k → 0, and there are cross terms ⟨Z^m X_a†X_b⟩.
- With the E-label operator instead, the wrap adds N·Π_wrap terms.
- Either way, the EH exclusion survives only on a momentum window, roughly k_− ~ 1/N ≪ k ≪ O(1). That window is empty at N = 2 in the Weyl/clock representation.
- So the qubit statement is the **quantum-link** one (§5, exact). Quantum spin ice gets its photon from qubits the same way: integer Gauss law, S^± hops.
- N0914's clock model at small N is not covered by B. It is covered by D (exact for discrete twists).

---

## 9. Control (c), and (b) the k-powers

**Control, same method (checked; the f-sum itself is prior art 3.4).**
- Cubic-lattice U(1) link ice with plaquette characters and an exact div E law: m₁_T(k) slope 1.999–2.000 in all five directions, and m₁/q̂² = 1.000000 at 1e-3.
- So χ_T = 1/m₁ ∝ k⁻², the photon's power (comparator: Hermele–Fisher–Balents).
- Maxwell CCR saturates: χ·m₁ = 1.000000.
- ED algebra check (s2):
  - f-sum identity m₁ = KΣ|μ|²⟨U + U†⟩ to all printed digits (16.935179 = 16.935179 at k = π/2, V = 0);
  - Bogoliubov saturated at the current probe (χ_AA·m₁ = |⟨[C,A]⟩|² = 35.850035);
  - (M4) holds (ω_min² = 3.758 ≤ 3.767);
  - the same at k = π and at V = −0.5.

**On "reproduce".**
- The method yields χ_T = inf_A ratio = 1/m₁ exactly, and its k-dependence is the exact symbol times k-independent ground-state expectation values. In that sense it reproduces exponent 2 for the photon without any fit.
- It does not certify the photon's speed or the deconfinement of the U(1) phase. 2D compact U(1) confines, and the repo's small-torus 3D photon work did not resolve a power (prior art 3.4).
- A referee may judge that a bound-type method cannot "reproduce" the control in the registered sense. I record the control as **passed for the exponent, as an identity, not as a phase measurement** (reading).

**(b) k-power, subtraction named.**
- Tensor class 𝒬_E: χ_TT(k) = 1/m₁(k) ≥ 1/(C_H k⁴), with exponent ≥ 4 (exactly 4 unless the k⁴ coefficient vanishes, in which case it is steeper).
- No subtraction: the 0th and 1st moments of every invariant pattern vanish. Checked: m₁/k⁴ tends to a constant at k = 1e-3, and slope 4.00 ± 0.01.
- No system size enters. These are thermodynamic-limit identities, not fits.
- Scalar response: contact-type in 𝒟 ∩ 𝒬_E (D2). No Newtonian attraction anywhere in 𝒟 (D1).

---

## 10. Where the window now is

R15-5 left the window as "U ~ J ~ g, aliasing, resummation, singular semiclassics" (`vR15-5:47`). After B and D it narrows to:

1. **Microscopic violation of the vector Gauss law** with an EH-type f-sum, as in 𝒟₀'s sin·B_N·sin (slope 2, s1 T3). The gauge structure would then have to emerge only at an IR fixed point.
   - **Suggested:** if the emergence were by a quasi-local unitary dressing to an exactly conserving H, Theorem B would apply in the dressed variables (summable moments are inherited). So the emergence must be RG-accidental, not dressed.
2. For the scalar channel in addition: **the E-basis sign problem** or **scalar-law violation** (D).
3. **Mod-N clocks at small N** (§8). This includes literal qubits in the Weyl representation, where Z₂ tensor gauge theories are generically gapped fracton phases (comparator).
4. **The incompressible z = 1 branch of B2.** It is not Einstein–Hilbert in its static response, so it is not the registered target.

These are exactly Gu–Wen's uncontrolled regime and P-N3″ (`R13-2:172`). R15-5's decisive computation, restricted to Gauss-law-conserving finite slots, is now done analytically. On the remainder, no controlled method fits this machine: it has a sign problem (D, X-S) and needs 3D sizes far beyond ED.

---

## 11. Prices (named, never adopted)

| Price | Axiom touched | Buys |
|---|---|---|
| **P-r16-7a**: an IR fixed point whose vector Gauss law is RG-emergent (not conserved microscopically, and not reachable by quasi-local dressing), with EH stiffness. A sharpening of P-N3″. Unbuilt | none named; a dynamical hypothesis | the only finite-slot route left to χ_TT ~ 1/k² (Theorem B) |
| **P-r16-7b**: accept an E-basis sign problem, i.e. non-stoquastic metric hops, or give up exact scalar-charge conservation | none (a dynamical choice) | the only route to an unscreened Newtonian scalar attraction (Theorem D) |
| P-r15-5a (integer h slot, dual rotor) | Qubit `AX:47` | EH static response, but z ≥ 2 TT modes are then forced (§7) |
| P-N1 (CCR tensor pairs) | Qubit `AX:45-53` | the only class with both the EH response and z = 1 (R15-5 §4) |

---

## 12. Readings against the FIXED clauses (`TESTS:5282-5284`)

- **PRODUCED-EVIDENCE: no.**
  - In 𝒬_E, Theorem B excludes χ_TT ~ 1/k².
  - In 𝒟, Theorem D excludes an unscreened attractive 1/k² scalar response.
  - Nothing was computed in the window of §10.
- **NOT-PRODUCED-EVIDENCE: yes in the Gauss-law-conserving finite-slot class 𝒬_E (worker reading, proved, unrefereed; goes to the referee as a negative).**
  - The same method passes the U(1) control for the exponent (2, saturated by the photon's Gaussian; §9) and gives a steeper power for the tensor: χ_TT ≥ c/k⁴, exponent 4 (§5).
  - The scalar response is contact-type in the stoquastic subclass (D2).
  - "Error bars": none are needed. The exponents are exact symbol identities with relative deviation below 1e-3 from the integers in s1.
- **INCONCLUSIVE: yes for the registered setting as a whole.** Its explicitly vector-law-violating part (Gu–Wen and 𝒟₀ at U_v ~ g) and small-N mod-N clocks are outside every controlled statement here (§8, §10).
- **Expectation check.**
  - The registration expected INCONCLUSIVE from system size. The outcome instead avoids size altogether in the conserving class, and leaves INCONCLUSIVE only for the non-conserving window.
  - The registration called "a sign-free dual basis" durable. What is durable here is instead the converse: in the E basis, sign-free plus conserved scalar charge excludes Newtonian attraction.

---

## 13. Strong-word check and scope

- **"Proved"** is used for:
  - S0 (sign inspection);
  - Theorem B and B2 (operator algebra, N0914's moment lemma, Cauchy–Schwarz);
  - Theorem D and D1 (orbit-graph diamagnetic inequality; D1 needs twice-differentiability at ρ = 0);
  - D2 (variational, needing a real Perron ground state and B1);
  - §7 (the dual of B, plus M4).
  - All are unrefereed.
  - B relies on N0914's lemma. That note is "proposed_retained / conditional-support", independently challenged within the author's work, with audit pending (`N0914:3-9`).
- **"Exactly"** is used for:
  - the identity χ_TT^inf = 1/m₁ (Bogoliubov saturates at the current; checked in s2 to all printed digits);
  - the exponent 4, unless the k⁴ coefficient vanishes, in which case the exponent is steeper.
- **"Suggested"** is used for:
  - §8 (clock windows);
  - D1′ (the blob argument);
  - the dressing transfer in §10.1;
  - "the incompressible branch cannot be excluded".
- **"Checked"** is used for:
  - the s1 symbols (midpoint-symbol model as in R15-5/N0914, not the doubled-position integer stencils; the integer stencil identities are N0914's runner);
  - the s2 2D QLM ED. This is an algebra check of M1–M4 only. 2D compact U(1) confines, so it is not a photon measurement.
- **Not covered:**
  - vector-law-violating microscopic H;
  - small-N clocks;
  - non-quasi-local H;
  - fermions;
  - matter coupling;
  - nonlinear gravity;
  - Λ.

## Files (`S/`)

- `METHOD_preregistered.md`: the method, definitions and control, written 23:08Z, before the runs.
- `scripts/s1_fsum_symbols.py` and `.out`:
  - m₁_TT symbols for R-rows, S-rows, random invariant patterns and the non-invariant 𝒟₀ term;
  - Bogoliubov ratios;
  - Gaussian saturation;
  - the U(1) cubic control.
- `scripts/s2_qlm_ed_inequalities.py`, `s2_qlm_ed_L4_V0.out`, `s2_qlm_ed_L4_Vm0.5.out`: ED of the 2D U(1) QLM on a 4×4 torus, checking the f-sum identity, Bogoliubov (saturated at the current), M4, and the diamagnetic inequality.
