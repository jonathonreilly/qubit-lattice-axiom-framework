# C5 R2-2: Lorentz-invariant discreteness, quantum (Lemma N-Q) and classical (Lemma P-L)

**Worker.** Claude Opus 5.5 (probe R2-2), the same model family as O1–O5, Q1 and the supervisor. **Not refereed.** Run 2026-10-12, 11:53Z to 12:24Z. No repository file was edited.
**Scratch.** `scratchpad/C5/R2-2/`: `r22_checks.py` → `r22_checks.out`; `r22_lorentz_mc.py` → `r22_lorentz_mc.out`; this report.
**Read in full.** `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS.md` "Campaign C5", "C5 Round 1 results" and "C5 Round 2" (`TESTS.md:2302-2643`, R2-2 at `:2496-2529`); `agents/C5_O5_synthesis.md`; `SUMMARY.md` §§15–21; `PRICE_NOTE.md` (v5 and the v6 delta); `C5_Q1_referee.md`, `C5_Q1_referee_full.md` §§4–6, `C5_Q1_report.md` §4; `RZ_referee.md`; `C4_RL2_referee.md`; `C4_RL4_referee.md`; `B_referee.md` (BHS at `:52`, Landau kinematics at `:82-90`, Lemma Q at `:123-131`); `E23_referee.md` §6 (Lemma P, `:88-117`).
**Labels.** *proved* = a complete proof written here (same family, unrefereed). *checked* = a numerical or symbolic check in the scratch files. *suggested* = argued only. *reading* = an interpretation. *comparator* = an outside result used for comparison. *RECALLED* = a literature fact from memory, not re-derived here.

---

## 0. In plain words

- **Quantum (N-Q).** A quantum vacuum cannot contain events that you could count like marbles.
  - The proof is short. The only things it needs are positive energy, a state that does not change in time, and event counts that commute and are whole numbers.
  - It does not need relativity, locality or a unique vacuum. A single positive Hamiltonian is enough.
  - This is the same reason an inertial detector in the vacuum never clicks.
  - **N-Q holds, in a stronger form than registered.**
- **Classical, the lemma as worded (P-L).** Any random scatter of points in spacetime, Lorentz-invariant or not, has some density fluctuation at spacelike wave-vectors. The cause is whole-number counting.
  - Take a long, thin needle of spacetime that holds on average half an event. Its count is 0, 1, 2, …, so it must fluctuate by at least ½.
  - A long thin timelike needle only "sees" spacelike wave-vectors.
  - **P-L holds as worded, in a stronger form than registered.**
- **But the conclusion route E needed does not follow.** That spacelike weight can sit entirely at Planck-size wave-vectors.
  - Explicit counterexample: a **Lorentz-random lattice**. Take a lattice whose own symmetry group is an infinite group of exact boosts (an arithmetic lattice). Give it a uniformly random "frame" drawn from a finite invariant measure, and a uniformly random shift.
  - The ensemble is then exactly Poincaré-invariant in law. Every realization is a crystal.
  - Its structure factor is exactly zero in a whole Lorentz-invariant band around the light cone: 0 < |q²| < c ~ (2π/a)².
  - Ordinary (sub-Planckian) light therefore cannot scatter off it into any other in-band direction or frequency, at any order. No in-band noise.
- **Effect on the routes.**
  - **A′ (a quantum vacuum substrate with countable events) is closed** for commuting event counts.
  - **Route E (classical random events) is closed only for white, Poisson-like processes**, which RZ and Q1 cover. It is **not** closed for Lorentz-invariant discreteness in general.
  - The surviving class has its own untested costs:
    - no known version in curved spacetime;
    - the same infinite-neighbour non-locality as causal sets;
    - an unknown mean lensing law.

---

## 1. Results against the FIXED readings (`TESTS.md:2522-2525`)

| Item | FIXED reading | What was found |
|---|---|---|
| **N-Q** | **DERIVED** | Proved under weaker hypotheses than N1–N6 (§2). O5's sketch is correct in every step. One phrasing in step 1 is loose, and steps 3–4 need fewer hypotheses than stated |
| **P-L, as worded** ("always has weight at spacelike momentum transfer") | **DERIVED** | Proved for every stationary integer-valued random measure with finite local second moments and ρ > 0. Lorentz invariance and simplicity are not needed (§3, Theorem P-L′) |
| **P-L's gloss** ("so it always scatters on-shell light") and **the DERIVED clause's consequence** ("every Lorentz-invariant discrete event structure that steers propagation either makes noise …") | not a fixed reading of its own | **False as a general statement.** The explicit Lorentz-random lattice (LRL, §4) is a stationary, simple, Lorentz-invariant point process with finite moments. Its Bartlett spectrum vanishes on {0 < \|q²\| < c} and, in the anisotropic version, on the null cone. In-band on-shell light has no non-forward channel. The REFUTED reading is *not* met as worded: LRL's spacelike structure factor is not zero everywhere, and Theorem P-L′ shows it cannot be |

**Net reading: DERIVED (both lemmas), with a mandatory scope correction.**
- The pre-registered lean ("route E and A′'s discrete events are both closed", `TESTS.md:2529`) holds for **A′** (commuting counts).
- For **route E** it holds only for processes with in-band spacelike weight, Poisson included (RZ/Q1).
- The O5 escape "Non-Poisson classical Lorentz-invariant processes: open" (`C5_O5_synthesis.md:268`) is now populated by an explicit member (LRL). It is **not** shown to steer propagation.

---

## 2. Lemma N-Q

### 2.1 Hypotheses (stated before the title)

The pre-registered N1–N6 are at `TESTS.md:2501-2507` and `C5_O5_synthesis.md:457-463`. The weakest set that works, found here:
- **(Q1)** A strongly continuous unitary group U(τ) = e^{iHτ} along one direction e, with **H ≥ 0**, and a unit vector Ω with U(τ)Ω = Ω. Ω does not have to be unique.
  - Under N1 this holds for every timelike e, since p·e ≥ 0 on V̄₊.
- **(Q2)** For every box B in a family closed under e-translation and halving along e: a self-adjoint N(B) ≥ 0 with spectrum in {0, 1, 2, …} and Ω ∈ D(N(B)), i.e. a finite vacuum second moment.
- **(Q3)** Covariance: U(τ)N(B)U(τ)* = N(B + τe).
- **(Q4)** Commutativity at vacuum level: Im⟨N(B)Ω, N(B+τe)Ω⟩ = 0 for a dense set of τ. This is implied by strong commutativity of N(B) and N(B+τe).
- **(Q5)** Additivity on the vacuum only: N(B)Ω = N(B₁)Ω + N(B₂)Ω, where B₁ and B₂ are the two halves of B along e.
- **(Q6)** ⟨Ω, N(B)Ω⟩ > 0 for some B.

**Not used:**
- locality (affiliation with A(O));
- Ω separating (N2);
- uniqueness of the vacuum;
- Lorentz covariance;
- the full 4D spectral cone.

### 2.2 Theorem N-Q′ (proved, same family)

**(Q1)–(Q5) imply N(B)Ω = 0 for every box B. So (Q6) fails: the vacuum carries no events.**

*Proof.*
1. **The count vector is time-invariant.** Let ψ = N(B)Ω and F(τ) = ⟨N(B)Ω, N(B+τe)Ω⟩ = ⟨ψ, U(τ)ψ⟩ = ∫e^{iEτ}dμ_ψ(E), using (Q3) and U(τ)*Ω = Ω. Here μ_ψ is a finite positive measure on [0, ∞) by (Q1). By (Q4) and continuity, F is real. Then μ_ψ equals its reflection E ↦ −E, so it is supported in [0, ∞) ∩ (−∞, 0] = {0}. Hence Hψ = 0 and U(τ)ψ = ψ.
2. **All translates give the same vector.** N(B+τe)Ω = U(τ)N(B)U(τ)*Ω = U(τ)ψ = ψ = N(B)Ω for every τ.
3. **Halving.** By (Q5) and step 2, N(B)Ω = 2N(B′)Ω, where B′ is either half. Iterating gives N(B)Ω = 2ⁿN(B⁽ⁿ⁾)Ω.
4. **Whole numbers.** On spectrum in ℤ≥0, λ² ≥ λ, so ⟨N²⟩ ≥ ⟨N⟩. Therefore ‖N(B)Ω‖² = 4ⁿ‖N(B⁽ⁿ⁾)Ω‖² ≥ 4ⁿ⟨N(B⁽ⁿ⁾)⟩ = 2ⁿ⟨N(B)⟩.
5. **Conclusion.** The left side of step 4 is finite by (Q2), so ⟨N(B)⟩ = 0. Then N(B)^{1/2}Ω = 0, so N(B)Ω = 0. ∎

**The registered N-Q follows (proved):**
- N3 + N4 + N5 give (Q4) and (Q5) by the two-projection step (§2.3).
- N5 makes every count a finite sum of projections, so it is bounded and (Q2) holds.
- N1 gives (Q1) and N6 gives (Q6).

**Corollary (proved).** Under N1 the conclusion holds for every timelike e. Under the 4D pointed-cone version, the spectral measure of ψ is supported in V̄₊ ∩ (−V̄₊) = {0}, and ψ is invariant under all translations.

### 2.3 (a) Check of O5's sketch (`C5_O5_synthesis.md:465-469`)

- **Step 1 (two projections): correct; one sentence is loose.**
  - "The generic part of P+Q has spectrum 1 ± cos θ … never an integer" is loose. Points of continuous spectrum can approach integers as θ → 0 or π/2. The conclusion is still right.
  - A cleaner proof (checked, `r22_checks.out` §1, symbolic):
    - For projections P and Q, (P+Q)(P+Q−1)(P+Q−2) = PQP + QPQ − PQ − QP.
    - If spec(P+Q) ⊂ {0,1,2}, multiplying by P on both sides gives (PQP)² = PQP.
    - Then ‖QP − PQP‖² = PQP − (PQP)² = 0, so QP = PQP = PQ.
- **Step 2 (all counts commute via N5): correct.**
  - Every count is a finite sum of fine-cell projections.
  - Disjoint cells commute by step 1, and identical cells commute trivially.
- **Step 3 (symmetric two-point function, support {0}): correct.**
  - Precisely: commutation makes F real, and reality makes the spectral measure reflection-symmetric.
- **Step 4 (Ω separating, so N = ρ·vol·1, contradiction): correct but more than needed.**
  - The halving argument of §2.2 needs neither the separating property nor a choice of O with non-integer ρ·vol(O).

**Weakest forms of N4 and N5 (proved or checked):**
- **N4** can be reduced to (Q5): additivity on Ω only, for halvings along one time direction.
- **N5** is needed **only** to derive commutativity. If commutativity (Q4) is assumed directly, N5 can be dropped.
- **Without N5 and without (Q4), the two-projection route fails.** Counterexample (checked, `r22_checks.out` §1): A = 2P and B = 2Q at angle π/3.
  - spec A = spec B = {0, 2} and spec(A+B) = {1, 3}, all integers.
  - ‖[A,B]‖ = 2.449.
  - Whether a full covariant positive-energy net with non-simple, non-commuting integer counts exists is **open** (§2.5, row 5).

### 2.4 (b) Prior art (count once)

- **Malament (1996) and Halvorson–Clifton (2002)** (RECALLED; no repository copy).
  - Setting: spatial localization or number operators on the hyperplanes of a frame.
  - Hypotheses: microcausality across hyperplanes, positive energy, translation covariance; Malament adds localizability. These yield commutation through a Borchers-type lemma.
  - Conclusion: the operators are trivial.
- **Hegerfeldt** (RECALLED): positive energy forces instantaneous spreading. The repository already uses Hegerfeldt's 1998 positivity theorem for an "exact permanent capture" obstruction under semibounded unitary evolution (`docs/NATIVE_HALFLINE_CLOCK_COMPLETION_FINITE_HORIZONS_AND_PERMANENCE_BOUNDED_THEOREM_NOTE_2026-09-14.md:16-19`, proposed_retained, review pending). That is the closest repository prior art. Count once.
- **Federbush–Johnson / Streater–Wightman** (RECALLED): a field whose vacuum commutator vanishes everywhere annihilates the vacuum up to its expectation. That is step 1 of §2.2.
- **Unruh–DeWitt** (comparator): an inertial detector in the vacuum has zero excitation rate. An accelerated one clicks, because the boost generator is not positive. Both agree with Theorem N-Q′ and with its escape (i) below.
- **What is new here.** Counts of 4D events with additivity across timelike separation. Whole numbers enter through ⟨N²⟩ ≥ ⟨N⟩ under repeated halving. The result is a one-direction version needing no locality, no Lorentz covariance and no unique or separating vacuum. The mathematical novelty is modest; the content is an application of the commuting-plus-positive-energy triviality.

### 2.5 (c) Escapes, classified

| # | Escape | Status |
|---|---|---|
| 1 | Non-additive "counts" | Escapes. They are no longer counts of events (definitional) |
| 2 | Counts additive only across spacelike separation (slice counts) | These are particle-number-type operators on hyperplanes, the Malament/H–C setting (RECALLED: excluded if microcausal with positive energy). Otherwise they need a foliation plus non-locality (P11-type). Not 4D events |
| 3 | Non-local counts | **Not an escape.** Locality is never used |
| 4 | Non-unique vacuum | **Not an escape.** Any invariant Ω with a finite second moment works |
| 5 | Approximate simplicity | If the counts still commute at timelike and null separation: **not an escape**. If they are non-simple **and** non-commuting: **open**. The 2P/2Q example shows the algebra allows it at matrix level; no covariant net is constructed |
| 6 | Infinite vacuum second moment | Closed again if Ω is separating (N2) and N5 holds (O5's route) |
| (i) | **State not invariant or not a ground state** (thermal, excited, cosmological; KMS GNS has a two-sided Liouvillean) | Escapes. Events need a non-vacuum state |
| (ii) | **Dynamics not a positive-energy unitary group** (collapse or flash dynamics that heats, GRW-type) | Escapes. This is R2-3's setting |
| (iii) | POVM or instrument outcomes (`C5_Q1_referee_full.md:176-180`) | Escapes. They are records of an apparatus (set A). Once realized they form a classical process, and §3 applies |
| (iv) | Euclidean lattice (set B) and classical stochastic substrates (route E) | N-Q does not apply: the sites are not real-time operators (B), or the Koopman spectrum is two-sided (E). For E, P-L is the relevant lemma |

**Reading (record formation).** "Records form … records are permanent" (`MINIMAL_AXIOMS_2026-06-29.md:77-80`), modelled as commuting, time-covariant whole-number counts in a positive-energy invariant state, gives formation rate zero. A stationary positive formation rate needs escape (i), (ii) or (iii). This agrees with the 09-14 permanence obstruction and bears on R2-3 (flashes heat) and R2-5 (an arrow in the state). It is a reading, not a derivation about the axioms: the axioms fix no Hilbert-space representation.

---

## 3. Lemma P-L

### 3.1 Hypotheses (stated before the title)

- ξ is a stationary random measure on ℝ^{1+d}, d ≥ 1, whose realizations are integer-valued (counting) measures.
- It has finite local second moments and mean intensity ρ > 0.
- Its Bartlett spectrum Γ̂ is the positive, positive-definite, translation-bounded measure with Var ξ(f) = ∫|f̂|²dΓ̂. It includes the self-term ρ (RECALLED standard: Daley–Vere-Jones vol. I §8.6). Translation-boundedness follows from Var ξ(g e^{iq·x}) ≤ E[ξ(|g|)²] for one fixed g with |ĝ| ≥ c > 0 on B₁.
- **Not assumed:**
  - Lorentz invariance;
  - simplicity;
  - absolute continuity of g₂ (the E23 referee's caution, `E23_referee.md:114`, is fully allowed).

### 3.2 Theorem P-L′, the needle theorem (proved, same family)

**Statement.** For every unit vector n and every c > 0, Γ̂ charges the set {q ≠ 0 : |q·n| < c|q_⊥|}. In particular, for timelike n it charges the open spacelike region {q² > 0}.

*Proof, ergodic case.*
1. **The integer variance bound.** If X is integer-valued with mean m and θ = frac(m), then E[(X−⌊m⌋)(X−⌈m⌉)] ≥ 0. This gives Var X ≥ θ(1−θ) (checked, `r22_checks.out` §2).
2. **The needle.** Take W_T = [−T/2, T/2]·n × (cube of side w), with Tw^d = V and ρV = ½. Then Var ξ(W_T) ≥ ¼.
3. **Suppose the claim fails.** Then Γ̂ off the origin lives in the closed cone K = {|q·n| ≥ c|q_⊥|}, where |1̂_W|² = V²·sinc²(q·nT/2)·∏sinc²(q_i w/2). Split K into three regions:
   - **(i) |q·n| < δ.** This lies inside B_{δ(1+1/c)} minus the origin. The contribution is at most V²·Γ̂(B_{δ(1+1/c)}∖0), which tends to 0 as δ → 0, because the ergodic Γ̂ has no atom at 0.
   - **(ii) δ ≤ |q·n| < 1.** Use sinc² ≤ 4/(q·n T)² and Γ̂(bounded set) ≤ K′. The contribution is O(V²/(δ²T²)).
   - **(iii) |q·n| ≥ 1.** Sum over unit cells using the translation bound. The cross-section holds about min(|q·n|/c, 1/w)^d cells, so the contribution is O(V²/T²·w^{−(d−1)}) (log-corrected for d = 1). That is O(T^{−2+(d−1)/d}) → 0.
4. **Contradiction.** With δ = T^{−1/2}, Var ξ(W_T) → 0, which contradicts step 2.

*Non-ergodic case.* Use the ergodic decomposition (RECALLED standard). Off the origin, Γ̂ is the average of the components' Γ̂_I, and the atom at 0 is Var(ρ_I). If Γ̂ vanishes on the open set, almost every Γ̂_I does too. Applying the ergodic case to a component with ρ_I > 0 gives the contradiction. ∎

**Where whole numbers enter.** The bound in step 1 is the whole of the "discreteness" input. A non-integer stationary random measure (e.g. ρ·Leb) has Γ̂ = 0, so the theorem is false without it.

**Check** (`r22_checks.out` §4, on the 1+1 LRL of §4).
- Needle variance: MC gives exactly 0.482 ≥ ¼ at T = 16.
- The share of the needle variance carried by timelike Bragg peaks falls as 0.19, 2.5e-2, 2.4e-3, 2.2e-4, 5.3e-5 for T = 1, 4, 16, 64, 256. This is the mechanism of the proof.
- The truncated spectral sums underestimate the variance at large T: at T = 256 they give 0.34, against the MC value of 0.48 at T = 16. They are lower estimates only.

**What Lorentz invariance adds (proved, kinematics).**
- The spacelike part of Γ̂ is a nonzero invariant measure on spacelike hyperboloids q² = κ².
- For a photon k, q = k − k′ with k′ null and future-pointing has q² = 2ωω′(1 − cos θ) ≤ 4ωω′. This is Q1's Lemma E (`C5_Q1_report.md:204`).
- Every spacelike hyperboloid meets this set, so on-shell scattering is kinematically open in the ensemble for every photon. But the final frequency is ω′ ≥ κ²/(4ω).
- If the spacelike weight starts at κ ~ 1/a, an in-band photon (ω, ω′ ≪ 1/a) has no non-forward channel.
- **P-L′ therefore does not imply in-band noise.** §4 shows the gap is realized.

**Comparison with Lemma P (`E23_referee.md:88-117`).**
- SL(d) or AN law invariance forces a white reduced second moment (c ≥ 1), hence white Γ̂, hence spacelike weight everywhere, including in band.
- The Lorentz group is too small to force that. Its invariant pair measures can be singular on hyperboloids, as the E23 referee warned at `:114`. LRL realizes exactly this.
- The SL(4) Haar-random affine lattice (`E23_referee.md:101`) is Lorentz-invariant too and has Poisson second moments (c = 1, white). It therefore makes in-band noise like Poisson.

---

## 4. The Lorentz-random lattice (LRL): a Lorentz-invariant point process silent in band

### 4.1 Construction

- Let L ⊂ ℝ^{1,3} be a lattice on which the Minkowski form is rational. Let Γ_L = {γ ∈ SO⁺(1,3) : γL = L}.
- If Γ_L is a lattice in SO⁺(1,3) (finite covolume), let μ be the invariant probability on SO⁺(1,3)/Γ_L.
- Draw gΓ_L ~ μ and an independent u, uniform on the torus ℝ⁴/L. Set X = g(L + u). This is well defined on the coset because γ(L + u) = L + γu and γ preserves Haar measure on the torus.

**Proposition (proved here from RECALLED inputs).**
- **(a) Invariance.** X is stationary and SO⁺(1,3)-invariant in law. The proof:
  - for a boost h, hgΓ_L ~ μ by left-invariance;
  - for a translation a, X + a = g(L + u + g⁻¹a) with u + g⁻¹a uniform.

  Adding diag(±1) ∈ O(Q)(ℤ) gives the full O(1,3). The law is ergodic under Poincaré, since G acts transitively on G/Γ_L. It is not ergodic under translations alone: the shape is invariant.
- **(b) Simple, intensity ρ = 1/covol(L).** All realizations have the same density, so Γ̂ has no atom at 0.
- **(c) Per-realization spectrum.** Each realization's Bartlett spectrum is the Bragg comb ρ²(2π)⁴Σ_{G∈gL*∖0}δ_G. Since G² is Lorentz-invariant, every nonzero Bragg vector has G² in the value set of the dual form, scaled by (2π)².
- **(d) Moments.**
  - In the isotropic case (L = ℤ⁴ with −x₀² + x₁² + x₂² + x₃²), Γ_ℤ is non-cocompact (it has a cusp).
  - The reduced Palm measure is Σ_orbits c·λ_{hyperboloid}, plus a null-cone part c·Σ_k k⁻²·d³x/|x|. This is locally finite, so second moments are finite.
  - The third moment diverges logarithmically from the cusp (suggested scaling).

**RECALLED inputs:**
- Borel–Harish-Chandra: arithmetic subgroups of semisimple ℚ-groups are lattices.
- Godement: such a subgroup is cocompact iff it contains no non-trivial unipotent elements; for SO(Q), iff Q is anisotropic over ℚ.
- Finiteness of the orbits of arithmetic groups on integral vectors of given norm.

In 1+1 dimensions everything above is elementary; see §4.3.

### 4.2 The anisotropic version (all elementary once Γ_L is a lattice)

Take L₇ = diag(√7, 1, 1, 1)ℤ⁴, so x² = Q₇(n) = −7n₀² + n₁² + n₂² + n₃².

- **Q₇ is anisotropic over ℚ.**
  - Proved: 7n₀² = n₁² + n₂² + n₃² has no nonzero solution (Legendre's three-square theorem plus 2-adic descent).
  - Checked: no solutions for |n_i| ≤ 25, and none for the dual form.
- **So:**
  - no nonzero lattice vector is null, and |x²| ≥ 1 on L₇∖0;
  - **|x|_E² ≥ |x²| ≥ 1 in every frame**, so every realization is uniformly discrete with a hard core;
  - every realization is relatively dense, by Minkowski's second theorem;
  - all moments are finite.
- **Bragg gap.** |G²| ≥ (2π)²/7 on gL₇*∖0. Checked: no dual null vectors.
- **Γ_{L₇} is infinite.** The reflections in r = (0,1,0,0) and r = (1,3,0,0) (Q₇ = 1 and 2) are integral. Their product γ has the (n₀, n₁) block [[8, 3], [21, 8]], preserves Q₇, has det = 1 and is orthochronous, with cosh(rapidity) = 8. Its powers have cosh(rapidity) = 127, 2024, 32257 (checked, `r22_checks.out` §5).
- **Γ_{L₇} is cocompact** (Godement, RECALLED).

**Consequences.**
- **Spectral gap.** The ensemble Γ̂ vanishes on the Lorentz-invariant open set {0 < |q²| < (2π)²/7}, in units with covol(L₇) = √7, **and** on the null cone minus the origin.
- **In-band silence (proved, kinematics plus per-realization covariance).** Assume the light–event coupling is a covariant functional of the realized point set, as RL's link readouts are. Then every amplitude of a single realization conserves 4-momentum modulo gL₇*, at every order.
  - An in-band transition k → k′ ≠ k needs q = k − k′ with 0 ≤ q² ≤ 4ω_max².
  - No Bragg vector lies there when 2ω_max < 2π/√7 (lattice units), i.e. for every sub-Planckian band if a is near the Planck length.
  - **So in-band incoherent mixing is exactly zero in every realization**, and RZ's |Ψ|²-driven white term does not arise.
- **The isotropic ℤ⁴ version** also has null Bragg peaks, so a collinear, frequency-shifting channel exists.
  - An in-band null Bragg vector (|G₀| ≤ ω) requires a cusp realization. The probability is ≲ C·(ωa)² by the Siegel-type count E#{null x ∈ gℤ⁴ : |x| < ε} ∝ ε² (suggested; constant not computed).
  - The channel also needs exact collinearity.

### 4.3 The 1+1 version (fully elementary, checked)

- **The lattice.** L = {(u, v) = s(a + b√2, a − b√2)}, with u = t + x, v = t − x, s = 2^{−1/4} and density 1. Then x² = −uv = −s²(a² − 2b²) ≠ 0.
- **Its boost symmetry.** The boost (u, v) → (e^{η₀}u, e^{−η₀}v), with η₀ = ln(3 + 2√2), maps L to itself through the integer matrix [[3, 4], [2, 3]] (checked). So Γ_L ⊇ ℤ, and G/Γ_L is a circle.
- **LRL in 1+1.** Draw η uniform on [0, η₀) and a uniform shift.
- **Checks:**
  - **Hard core.** The Euclidean minimum distance over η ∈ [−6, 6] is 0.8409, equal to the bound √|x²|min = 2^{−1/4} (checked).
  - **Bragg gap.** min |q²| = (2π)²/√2 = 27.915 (checked).
  - **Invariance in law, Monte Carlo** (30,000 samples each, `r22_lorentz_mc.out`). Counts in the unit square and in squares boosted by χ = 0, 0.7 and 2.5 give P(N=0) = 0.1189, 0.1152 and 0.1174 (SE 0.0019). The means are 0.999, 1.002 and 1.005. The timelike-pair covariances are +0.010, +0.012 and +0.011. All agree within MC error, as they must exactly.

### 4.4 What LRL does *not* establish (open or suggested)

- **Steering.** RL2's √Δ mean (`C4_RL2_referee.md:15-17`) used the Poisson Palm structure. LRL's mean link kernel is a sum over integer shells plus (for ℤ⁴) a null-cone part; it is not computed.
- **Curved spacetime.** The construction needs the global affine Minkowski structure. No curved-spacetime version is known. Local frames would bring curvature-induced defects (suggested), and those could reintroduce noise.
  - If the defect density scales with curvature times a², their white contribution would be suppressed by about (a/L_curv)² relative to Poisson. That is unquantified and suggested only.
  - **This is the main obstacle to LRL as a gravity substrate.**
- **Forward (coherent) dispersion in one realization.** Γ_L is Zariski-dense (Borel density, RECALLED; already noted for ℤ⁴ at `C4_F2_report.md:98` and `C5_O1_report.md:138,193`). Every polynomial Γ_L-invariant tensor is therefore Lorentz-invariant. But covariant couplings are constant on infinite Γ_L-orbits, so the needed sums are not shown to converge or to be analytic. Open.
- **Locality (proved, trivial).** No finite set of neighbours of a point is Γ_L-invariant, because the orbits are infinite. No equivariant frame map exists, because Γ_L fixes no point of H³. LRL therefore pays the same unbounded-valency price as Poisson sprinkling (P2; BHS analogue, `B_referee.md:52`).
  - This answers PRICE_NOTE's open item "Beyond Poisson. BHS does not cover other point processes" (`PRICE_NOTE.md:208`) for this class.
- **Formation, matter and the graviton:** untouched.

**Prior art (count once).**
- The integral Lorentz group of ℤ⁴, its Zariski density and its infinite orbits: `C4_F2_report.md:98`, `C5_O1_report.md:138,193`, Schild 1948 (RECALLED), arXiv hep-lat/0204027.
- Discrete-boost-invariant 1+1 lattices: P. Wang, arXiv:1708.00924.
- Lorentzian cut-and-project quasicrystals: Boyle–Mygdalas, arXiv:2601.07769.
- The SL(d) Haar-random lattice: `E23_referee.md:101`.
- Causal-set statements that regular lattices are not Lorentz invariant, and the BHS theorem: Dowker–Henson–Sorkin, gr-qc/0311055; BHS, gr-qc/0605006.
- **Not found** in the repository or in two web searches: the **Haar-random coset over a finite-covolume Γ_L** used to make a lattice ensemble exactly Lorentz-invariant in law, and its use against P-L. It may exist in the homogeneous-dynamics literature (Siegel / Eskin–Margulis–Mozes random lattices for SO(Q)).
- **Correction to a common claim (suggested).** "A regular lattice looks lopsided after a boost" holds for isotropic lattices such as ℤ⁴, which have short null vectors in boosted frames. It fails for anisotropic arithmetic lattices such as L₇: in every frame |x|_E ≥ 1.

---

## 5. (e) Survivors against RZ's bar, and (f) reuse

**(e) RZ's bar.** RZ's FAIL is ln(N_B/S) ≥ 43,986 at 1 s and 1 Gpc (`RZ_referee.md:17`). It is driven by the white |Ψ|² first-chaos term, which Q1 ties to spacelike spectral support (`C5_Q1_report.md:217`).
- **Anisotropic LRL:** the in-band incoherent rate is exactly 0 at all orders, in every realization (§4.2). It passes trivially, whatever the RL coupling strength. The RL coupling never enters, because the zero is kinematic.
- **Isotropic ℤ⁴-LRL:** only the collinear null channel exists. Its realization probability is ≲ C(ωa)² (about 1e-56 at optical ω with a Planck-length a, constant not computed), and it also needs exact alignment. Suggested pass.
- **Not computed:** the realization-dependent forward phase (§4.4).

**(f) Reuse of O5 remark 1** (`C5_O5_synthesis.md:447-453`, `o5_checks.out` §2).
- Neither lemma uses count variance as a criterion. N-Q uses integrality plus spectral symmetry. P-L′ uses integrality plus spectral support.
- LRL strengthens O5's point. A Lorentz-invariant process can even be hyperuniform: every realization is a lattice with surface-law variance. So variance scaling cannot separate "Lorentz-invariant" from "not".

---

## 6. Scope and outside realizations

**N-Q′ excludes:**
- non-invariant or excited states;
- non-unitary or heating dynamics;
- POVM outcomes (records);
- non-commuting non-simple counts (open);
- Euclidean or OS-only lattices;
- classical substrates.

**P-L′ covers** every stationary integer-valued random measure with finite second moments on ℝ^{1+d}. **It excludes:**
- non-stationary processes (e.g. cosmological growth with a start);
- marked processes whose coupling weights can be negative or complex — the coupling may then not see ξ's Bartlett spectrum;
- processes with infinite local second moments.

**The in-band silence of LRL is conditional on:**
- per-realization covariance of the light–event coupling;
- flat spacetime.

It is not a lensing PASS.

**Strong words checked.**
- "Proved" is used only for the arguments written in full here (§2.2, §3.2, the 1+1 and anisotropic properties in §4.2–4.3). Their external inputs are RECALLED and named.
- "Exactly zero in band" relies on 4-momentum conservation modulo the dual lattice in each realization.

**Needs codex referee** (no-go or counterexample claims): Theorem N-Q′, Theorem P-L′, and the LRL proposition (invariance in law, the Bragg gap, and the in-band silence argument).

---

## 7. Price implications (named, none adopted)

- **A′ (P-Q1 with discrete events).** In a positive-energy vacuum, discreteness cannot be commuting event counts. That leaves non-commuting non-simple counts (open), or records formed by a non-unitary or heating process, or in a non-vacuum state. This is set A's A4 / R2-3.
- **Route E, generalized: a candidate "E′, arithmetic random lattice".** Its prices:
  - **Lattice:** sites become a Haar-random-frame arithmetic lattice in Minkowski space. This touches `MINIMAL_AXIOMS_2026-06-29.md:37-38`, and "proper cubic rotations" becomes the infinite integral Lorentz group;
  - **Admissibility:** unbounded valency (as P2);
  - **a supplied flat affine background**, with no curved version known;
  - **P3** (supplied order) and **P4** (records as events), unchanged.

  It removes the in-band noise wall. It does not supply lensing, a graviton or formation. Whether it is worth a test lane is an owner or supervisor decision. The decisive next test would be the mean link kernel on LRL and its curved-spacetime definition.
