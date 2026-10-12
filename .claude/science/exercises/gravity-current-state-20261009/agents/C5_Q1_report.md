# C5 round 1, probe Q1: a coherent (unrecorded) event substrate (worker report)

**Worker:** Claude Opus 5.5 (probe Q1), the same model family as the exercise authors. **Unrefereed.** Worked 10:58–11:40Z on 2026-10-12. OMP_NUM_THREADS=2; every run under 8 minutes (q1_E: 420 s each; the rest under 1 min). No repository file was edited.

**Read in full:** `docs/MINIMAL_AXIOMS_2026-06-29.md`; TESTS.md "Campaign C5" and "C5 Round 1 / Q1" (fixed readings and expectation), "Lane RZ" and "Lane RZ results", "C4 result recorded 21:28Z (Y1)", "C4 result recorded 21:01Z (RL4)", "C4 results recorded 19:41Z" (RL2), "C4 results recorded 20:23Z" (RL3), and the RL, RL2, RL3, RX, RY settings; `C4_RL2_report.md`, `C4_RL2_referee.md`; `C4_RL4_report.md`, `C4_RL4_referee.md`; `C4_Y1_report.md`, `C4_Y1_referee.md`; `RZ_Z1_report.md`, `RZ_referee.md`. **Read in part:** `RZ_Z2_report.md` (lines 1–140); `z2_A_carrier_mc.py`, `z2_C_analyse.py` and its output. **Data reused:** probe Z2's saved sprinkling realizations (`scratchpad/RZ/Z2/z2_A_e*.npz`: op0, a carrier source with a past edge, ε = 1, ½, ¼, ⅛; 3139 / 1637 / 960 / 594 realizations).

**Labels:**
- **PROVED:** complete argument in this report; scope stated.
- **CHECKED:** numerics, with the scripts listed under Files.
- **ARGUED:** a standard step, not written out.
- **SUGGESTED:** a heuristic or estimate.
- **RECALLED:** literature-level, not fetched.

## Verdict (worker)

| item | status | result |
|---|---|---|
| **A. Substrate traced out.** The sprinkling is a quantum label, the light sees a definite sprinkling in each branch, and the substrate amplitude ψ(P) has any phases. | **PROVED**; **CHECKED** | The light's reduced state is exactly the classical mixture ∫dμ U_P ρ₀ U_P†. Every light observable equals the classical ensemble average. ⟨a⟩ = Ψ: the amplitude is averaged and equals the RL2 mean. ⟨a†a⟩ = \|Ψ\|² + V, which is RZ's variance. The phases of ψ cannot be observed. |
| A′. The substrate "returns to its state" by its own dynamics, Lorentz invariant or not | **PROVED** (no-signalling) | Dynamics acting on the substrate alone cannot change the light's reduced state. So this reduces to A. |
| A″. Decoherence-free subspace for the light | **PROVED** | A DFS needs U_P to be P-independent up to a global phase on those modes. RZ's white, carrier-blind in-band noise is not a global phase, so the observed modes are not in a DFS. |
| **B. Kept coherent.** This needs a final-state projection of the substrate, which is non-unitary. | **PROVED** | Projecting onto the initial substrate state gives the Poisson-mean S-matrix E U_P. The success probability is 1 − E‖U_Pχ − EUχ‖². The missing probability is the variance. |
| B1. Coherent-state light, Gaussian per-mode noise | **PROVED** exact; **CHECKED** | E D(Ψ+δ)\|0⟩ = (2/(2+V)) e^{−\|Ψ\|²V/(2+V)²} \|2Ψ/(2+V)⟩, where V is the noise in photons per mode. The recombined light is a pure coherent state, but its amplitude is 2Ψ/(2+V), not Ψ. **The noise returns as extinction of the coherent image.** |
| B1 on the real sprinklings (ε = ⅛) | **CHECKED** | Recombination probabilities match a Gaussian surrogate with the same covariance (0.143 vs 0.140, 0.091 vs 0.077, 0.041 vs 0.036). The amplitude falls below the mean as V_ph grows. |
| B2. Structured complex amplitudes ψ(P) | **PROVED** (one mode) | No amplitude that depends only on the noise magnitude works. A normalizable complex ψ does exist for one mode (an explicit construction, fidelity 1.000000). But it is built from the GR amplitude itself, and its branch weight \|c(λ)\| must vary with the emitted light and fall to 0. Several modes: not settled. |
| **C. The only noise-free quantum substrate** | **PROVED** (kinematics + spectrum condition) | A positive-energy, Poincaré-invariant vacuum cannot scatter on-shell light incoherently, so it gives no noise and no decoherence. **But its density correlations cannot be Poisson (white).** The white spectrum at spacelike momentum transfer is exactly what produces RZ's noise. |
| D. Decoherence by matter (shared ℓ_k) | **SUGGESTED** (robust in direction); per-region sensitivity **CHECKED** | Each matter quantum's own noise grows by 0.36 e-folds per hour of age, and 4×10¹³ for 13.8 Gyr. About 10⁶⁸ CMB photons lie inside the needle of a 1 s, 1 Gpc lensed source. Matter records which sprinkling occurred, so it restores the mixture of A. On Z2's model, resampling about one event near the source edge moves 14–37% of the field's whole noise variance (`q1_E`). |
| Observed lensed light | **CHECKED** arithmetic on refereed RZ numbers | Reading A: coherent fraction ≤ e^{−4.4×10⁴}, with excess flux ≥ e^{4.4×10⁴}. Reading B1: image amplitude × e^{−4.4×10⁴} for any photon occupation from 10⁻¹⁰⁰ to 4×10¹¹. Observation needs a coherent fraction of about 0.1–0.8. |
| Side finding: typical vs mean noise growth | **CHECKED** (accessible ε only) | The typical noise (median, and E ln\|δ\|²) grows at the variance rate to within 3% at every ε. The law moves toward Gaussian as ε falls: kurtosis 103 → 7.8 → 3.4 → 2.4. At accessible ε, RZ's noise is typical, not a rare-tail effect. |

**Worker reading against the FIXED Q1 readings: FAIL (bounded).**
- **Traced-out reading.** Theorem A is an exact identity, so the noise returns at exactly RZ's level, with RZ's controlled (not fully proved) status and its scope:
  - edged emissions;
  - the stable scalar-layer readout;
  - a shared ℓ_k;
  - the scalar-to-photon transfer.
- **Kept-coherent reading, uniform amplitudes.** The noise returns as extinction. This is exact for Gaussian per-mode noise, and Gaussian noise is ARGUED for incoherent sources.
- **Open.** Final-state recombination with general structured complex amplitudes across many modes. For one mode it is possible, at the three prices in §3.4.
- **If the referee requires the whole stated class, structured phases included:** INCONCLUSIVE, leaning FAIL. Every surviving construction needs:
  - a non-unitary final-state law;
  - substrate amplitudes that encode the GR answer;
  - branch weights that depend on the light;
  - and it is undone by decoherence by matter in the shared-ℓ_k setting.

**PASS** is not met. No explicit coherent rule inside the class gives the RL2 mean with negligible noise and negligible decoherence.

**Plain summary.**
- **Making the substrate quantum does not remove the noise. It renames it.** If light crosses a superposition of sprinklings, each sprinkling carries the light differently, so the light becomes entangled with which sprinkling it crossed. Whatever the phases, the light by itself then behaves exactly like the classical average over sprinklings.
  - Its average amplitude is the good RL2 mean (GR lensing).
  - Its brightness carries RZ's huge excess, as incoherent light.
  - Quantum mechanics adds nothing and removes nothing here. This is an identity.
- **The only way to get the "averaged amplitude" as the actual state of the light is to force the substrate back into its starting state at the end.** That step is not ordinary quantum mechanics: it is a final-state projection.
  - Even then, for a beam with more than a tiny fraction of a photon of noise per mode, the recombined beam is dimmed by the noise: amplitude 2Ψ/(2+V).
  - With RZ's numbers the dimming is e^{−44,000}. The lensed image would vanish instead of drowning in noise.
- **One can tune complex substrate amplitudes so that a single light mode comes out exactly right.** But the tuning uses the GR answer as input, and it makes the probability of emitting light depend on how much light is emitted. That is a nonlinear change to quantum mechanics.
- **A quantum substrate in a true vacuum (positive energy, Lorentz invariant) would make no noise at all.** It cannot scatter light, because light-to-light momentum transfer is spacelike and a vacuum cannot absorb spacelike momentum. **But then the substrate's events are not a Poisson sprinkling.** Poisson statistics is white, so it carries spacelike momentum, and that is precisely the noise.
- **Matter makes things worse.** Anything that has existed for more than a few hours, at the shared ℓ_k, carries an exponentially detailed imprint of the sprinkling it lived on. So matter records which sprinkling occurred and destroys any coherence.

## 1. Setting and formulation

**The classical event route** (RL2/RL4/Y1/RZ, refereed). For a sprinkling P with Poisson law μ, the field is φ_P = H_P J, with:
- **mean** Ψ = Eφ_P, giving GR √Δ lensing at leading needle order (RL2);
- **variance** V = Var φ_P, which grows at least as e^{c_low√ε τ/ℓ_k} (RL4);
- **in-band ratio** N_B/S ≥ e^{43,986} for 1 s of emission at 1 Gpc, after every correction (RZ referee). The noise is white, driven by |Ψ|² rather than by the carrier phase.

**Quantum version (the Q1 class).**
- **Substrate.** H_S = L²(Conf, μ), with orthogonal configuration states |P⟩. The substrate state is |Σ⟩ = ∫dμ ψ(P)|P⟩ with ∫|ψ|²dμ = 1.
  - ψ ≡ 1 is "the Poisson measure as path-integral weight". |ψ|² = 1 is "Poisson as amplitude-squared". On the non-atomic configuration space these readings coincide.
  - Random or structured phases: ψ = e^{iθ(P)}.
- **Light.** For a classical source, the per-sprinkling S-matrix on Fock space is the displacement U_P = D(α_P), with α_P the mode amplitudes of H_P J. This is standard for a linear field driven by a c-number source (ARGUED). U_P is unitary for any α_P, so the non-unitarity of H_P as a one-particle map does not enter.
  - Incoherent sources are mixtures over source phases (Glauber P), exactly as in Y1 §2.1.
- **Coupling.** "The substrate is a sprinkling" means that in branch P the light propagates on P: U = ∫^⊕dμ |P⟩⟨P| ⊗ U_P, which is configuration-diagonal.
- **The task's Φ = Σ_C ψ(C)G_C J** is the amplitude-weighted sum. Section 3 shows it is the light's state only after a final-state projection. Without one, the observable field operator is Φ̂ = ∫^⊕ |P⟩⟨P| ⊗ â_P.

## 2. Substrate traced out (PROVED)

**Theorem A.** For any ψ (any phases), the light's reduced state after the coupling is

  ρ_L = Tr_S[U(|Σ⟩⟨Σ| ⊗ ρ₀)U†] = ∫dμ |ψ(P)|² U_P ρ₀ U_P†.

*Proof.* U is block-diagonal in the orthogonal |P⟩. The partial trace in that basis keeps only the diagonal blocks, and the phases enter only through |ψ|². ∎

**Consequences** (all PROVED):
- ⟨â⟩ = Eα_P = Ψ, the RL2 mean. So "amplitude-level averaging" does happen, but as the expectation of a mixture, not as a pure amplitude.
- ⟨â†â⟩ = E|α_P|² = |Ψ|² + V, which is RZ.
- Any observable block-diagonal in P has the classical ensemble value. That includes every observable of observers made of matter that also lives on the events (superselection).
- |EGJ|² could appear only through matrix elements ⟨P|P′⟩ ≠ δ, which orthogonal configurations do not have.

**CHECKED** (`q1_A` §A1). ‖ρ_L − mixture‖ = 5.6×10⁻¹⁷ for three phase sets; purity 0.355 in all three.

**Corollary A′: no-signalling.** A later unitary on the substrate alone, however Lorentz invariant and however it "returns the substrate to |Σ⟩", leaves ρ_L unchanged: Tr_S[(V_S⊗1)X(V_S⊗1)†] = Tr_S X. **CHECKED:** the change is 1–2×10⁻¹⁶. Purifying the light needs either continued joint interaction or a non-unitary step (§3).

**Corollary A″: purity and DFS.**
- ρ_L is pure iff U_Pρ₀U_P† is μ-a.s. constant on supp ψ, i.e. no per-realization noise on the populated modes.
- A decoherence-free subspace is a set of modes on which U_P = e^{iθ_P}U.
- RZ (refereed) found the in-band noise white, decorrelating within about 0.2 ℓ_k, and not following the carrier (Z1 §2.4, Z2 §2.2). That is not a global phase factor, so the observed modes are not in any DFS.

**What observation sees** (CHECKED arithmetic, `q1_C` §1). The in-band first-order coherence of the image with the GR mode is Γ_B = S/(S+N_B):
- ≤ e^{−4.4×10⁴} for 1 s of emission at 1 Gpc;
- e^{−7.7×10⁶} for 8 h;
- e^{−2.5×10⁸} for 1 yr;
- e^{−8.0×10¹¹} for a 10⁷-yr quasar.

**VLBI fringe visibility** is |Ψ₁Ψ₂* + C₁₂|/√((|Ψ₁|²+V₁)(|Ψ₂|²+V₂)).
- If the noise at the two antennas is uncorrelated, as Y1 suggests, the visibility is ≤ Γ_B.
- If it is correlated, the visibility can be large, but the flux excess N_B/S ≥ e^{4.4×10⁴} remains, along with its image-to-image and distance dependence through τ.
- Either way the observed lensing fails. Observation requires visibilities of O(0.1–1) and flux ratios good to 10–20% (RECALLED, as in Y1 §4.1).

**Physical picture.** The light ends up entangled with the sprinkling it crossed. Tracing the sprinkling out is decoherence, and the decohered part is RZ's variance, carried as incoherent light superposed on the GR image. In the quantum version, intensity noise and decoherence are the same thing.

## 3. Kept coherent: final-state projection

### 3.1 What it takes (PROVED)

By A′, interference between different sprinklings in the light's statistics requires projecting the substrate onto a final state ⟨F| = ∫dμ φ_F(P)*⟨P|. This is a two-boundary, or final-state, law: not unitary, and outside standard quantum mechanics.

The light's (unnormalized) state is then ∫dμ φ_F* ψ U_P χ₀.
- **"The substrate returns to its state"** means F = Σ. That gives ∫dμ|ψ|² U_P χ₀ = E U_P χ₀, the Poisson-mean S-matrix.
- **Theorem B** (success probability): ‖E U_Pχ₀‖² = 1 − E‖U_Pχ₀ − EUχ₀‖². The variance is exactly the missing probability. **CHECKED** (`q1_A` §A2): 0.288187 = 0.288187.
- **One-photon sector.** The map is linear, ∫dμ U_P|1_f⟩ = |1_{EG f}⟩, so a single photon comes out mean-propagated, with weight ‖EG f‖².
- **n photons.** The result carries E[(G_P f)^{⊗n}] ≠ (EG f)^{⊗n}, so multi-photon light is not mean-propagated.
- **Random phases.** Take i.i.d. random phases θ(P) in the initial state and project onto a different final state, e.g. the uniform one. The light amplitude is then ∫e^{iθ(P)}U_P dμ, which averages to 0 over a non-atomic configuration space (SUGGESTED, random-walk cancellation). Random phases only remove the light. They cannot restore it.

### 3.2 Theorem C: coherent-state light and Gaussian noise (PROVED exact)

**Statement.** Let α = Ψ + δ, with δ circular complex Gaussian and E|δ|² = V photons per mode. Then

  **E D(α)|0⟩ = (2/(2+V)) · exp(−|Ψ|²V/(2+V)²) · |2Ψ/(2+V)⟩.**

**Proof.**
1. D(Ψ+δ) = D(Ψ)D(δ)e^{−i Im(Ψδ*)}, and D(δ)|0⟩ = e^{−|δ|²/2}Σ δⁿ|n⟩/√n!.
2. Combining e^{−|δ|²/2} with the Gaussian law e^{−|δ|²/V} gives a circular Gaussian with variance V′ = 2V/(2+V) and weight V′/V.
3. The phase factor is e^{aδ + bδ*} with a = Ψ*/2, b = −Ψ/2. Then E′[δⁿ e^{aδ+bδ*}] = (bV′)ⁿ e^{abV′}.
4. Summing gives (V′/V)e^{−|Ψ|²V′/4}e^{|Ψ|²V′²/8} D(Ψ)|−ΨV′/2⟩ = (prefactor) |Ψ(1 − V′/2)⟩, and 1 − V′/2 = 2/(2+V). ∎

**CHECKED** (`q1_A` §A3, Monte Carlo with 4×10⁴ samples in a 120-state Fock basis):

| V | MC norm | closed-form norm | MC ⟨a⟩_rec | 2Ψ/(2+V) |
|---|---|---|---|---|
| 0.1 | 0.93123 | 0.93103 | 0.9507 | 0.9524 |
| 1 | 0.59712 | 0.59656 | 0.6609 | 0.6667 |
| 4 (Ψ = 2) | 0.21041 | 0.21373 | 0.6650 | 0.6667 |
| 20 (Ψ = 1.5) | 0.08312 | 0.08284 | 0.1260 | 0.1364 |

At V = 100 the Monte Carlo is noise-limited.

**Meaning.**
- The recombined light is pure and coherent, so it is "decoherence-free". But the noise has moved into the **amplitude**: it is the mean Ψ shrunk by 2/(2+V).
- Only when V ≪ 1 photon per mode does the recombined state approach |Ψ⟩.

### 3.3 On the actual sprinklings (CHECKED, `q1_B2`)

**Setup.** Probe Z2's realizations at ε = ⅛, carrier ω₀ = 1, at times where the mean is resolved: t = 3.5–5.0, with V/|Ψ|² = 47–91. The amplitudes are scaled so the mean carries n̄ photons per mode.

**Recombination probability:**

| V_ph | Monte Carlo | Gaussian surrogate with the same mean and non-circular covariance (6000 samples) |
|---|---|---|
| 4.66 | 0.1426 | 0.1400 |
| 6.04 | 0.0908 | 0.0773 |
| 8.68 | 0.0406 | 0.0359 |
| 9.08 | 0.0444 | 0.0357 |

**Recombined amplitude |⟨a⟩_rec|/|Ψ|:** 0.45 ± 0.08 against the surrogate's 0.42 at V_ph = 4.7; 0.24 ± 0.13 against 0.22 at V_ph = 8.7. It falls with V_ph as the Gaussian law predicts.

**Circularity.** For one coherent source the noise is not circular: |Eδ²|/V = 0.92, 0.82, 0.64, 0.42 at ε = 1, ½, ¼, ⅛ (`q1_B`). So the circular formula 2/(2+V) is only indicative there (0.30, 0.19).

**For real, incoherent sources** the per-mode in-band noise is a sum over N_e ≫ 1 independently phased emitters, and is therefore circular Gaussian (ARGUED). This needs the weak inter-emitter covariance, which Y1 argued and the referee called heuristic. Theorem C then applies as stated.

**What does not follow from the variance alone.** In general, the recombination weight is at most sup_c E e^{−|α_P − c|²/2}, which is anti-concentration at the one-photon scale (`q1_A` §A4).
- If a finite fraction of realizations were "quiet" (an atom at Ψ), recombination would return Ψ. The toy example gives amplitude 1.000 with probability 0.82.
- A lognormal law, the strong-disorder-like case, gives dimming instead (0.27).
- The realizations show no quiet atom. The law becomes more Gaussian as ε falls (§7).

### 3.4 Structured complex amplitudes (Theorem D, PROVED for one mode; CHECKED)

**Requirement.** For one mode with per-realization amplitude λx_P under a law with a bounded density p_μ, ask that ∫ψ D(λx_P)|0⟩dμ = c(λ)|λΨ₁⟩ for every source strength λ. A law privileges no states, so ψ cannot depend on the source.

**(i) Reduction.** Write g = ψp_μ = Σ_m g_m(r)e^{imθ}. Matching Fock components and using Laplace uniqueness in s = |λ|² forces g_{−n}(r) = Ψ₁ⁿ r^{−n} g₀(r) for every n ≥ 0. Since ψ ∈ L²(μ) gives g ∈ L², g₀ must vanish on r < |Ψ₁|.

**(ii) Amplitudes depending only on the noise magnitude are impossible** (ψ = f(|x − Ψ₁|), Gaussian law).
- The conditions reduce to E[f·|δ|^{2k}] = 0 for k ≥ 1, with E[f] ≠ 0.
- ψ ∈ L²(μ) gives the r-density an exponential moment, so its Laplace transform is analytic.
- That transform is constant near 0, hence constant everywhere, which contradicts its decay. So no normalizable such f exists.

**(iii) General complex ψ: solutions exist.** An explicit one is g(x) = g₀(|x|)·x/(x − Ψ₁)·1[|x| > |Ψ₁|], with g₀(r) = (r − |Ψ₁|)e^{−r²/w}.
- **CHECKED** (`q1_D`): ‖ψ‖²_{L²(μ)} = 3.98, and the fidelity with |λΨ₁⟩ is 1.000000 for λ = 0.3–3.

**Every solution has three costs:**
- **(a) A non-unitary final-state law.**
- **(b) ψ encodes the answer.** ψ(P) = g(x_P)/p_μ(x_P) is built from the GR amplitude Ψ₁ and from the light's own per-realization amplitude for that mode and source geometry. The substrate's state must already contain the GR propagator.
- **(c) The branch weight depends on the light.** |c(λ)| = |∫_{u₀}^∞ e^{−s(u−u₀)}G(u)du| (u = r²/2, u₀ = |Ψ₁|²/2) cannot be constant for an L² function G. It tends to 0 as the photon number grows.
  - **CHECKED:** |c| = 1.13, 0.72, 0.46, 0.21, 0.099, 0.028 for n̄ = 0.09, 0.49, 1, 2.25, 4, 9 (c(0) = 1.27).
  - In the normalized theory, emission probabilities are reweighted by |c(λ)/c(0)|². That is a nonlinear, Born-rule-violating change, the kind Gottesman–Preskill raised for final-state proposals (RECALLED).
  - Narrowing G flattens c(λ) over a larger range only as ψ tends to a non-normalizable amplitude on the circle |x| = |Ψ₁| (SUGGESTED scaling ‖ψ‖ ~ 1/width).

**Several modes.** The product form extends to finitely many independent modes. For a field it needs the event {|x_k| ≥ |Ψ_k| for all k} to have positive μ-measure. **Not settled.**

**Uniform ψ, for comparison:** amplitude 0.33 against a target of 1.0 at n̄ = 1, and 0.16 against 3.0 at n̄ = 9 (Theorem C).

**Phases from a causal-set action** (ψ = e^{iS(P)}, SUGGESTED). If stationary phase concentrates the sum on typical sprinklings, the light sees a single realization's noise, which grows at the variance rate (§7). If it concentrates on regular configurations, Lorentz invariance in law is lost (O1).

## 4. The only noise-free quantum substrate, and why it is not Poisson (PROVED)

**Lemma E (kinematics).** For future null k, k′, q = k − k′ has q² = 2|k||k′|(1 − cos θ) ≥ 0 in the (−,+,+,+) signature. So it is spacelike unless k and k′ are collinear. **CHECKED** (`q1_C` §5: min q² = 5×10⁻⁶ ≥ 0 over 10⁵ draws).

- **Vacuum substrate.** Suppose the substrate's local density n(x) acts in a positive-energy representation with a Poincaré-invariant vacuum. Its spectral support for absorbing momentum lies in V̄₊. Then on-shell light cannot scatter on-shell by giving the substrate momentum q:
  - in Born order: no spacelike support;
  - in every order, for a gapped substrate: k − k′ ∈ V̄₊ forces collinear null q.
- **With a static lens**, which supplies spacelike momentum but no energy, scattering is still forbidden for ω < gap.
- So the substrate produces no incoherent light, no noise, and no decoherence.

**Lemma F (no white vacuum).** In that setting, the Fourier transform of the connected Wightman function ⟨Ω|n(ξ)n(0)|Ω⟩_c is a positive measure supported in V̄₊. The FT of the symmetrized function is supported in V̄₊ ∪ (−V̄₊).
- A Poisson process has connected density correlation ρδ⁴(ξ), whose FT is ρ for every q, spacelike included. So it is excluded.
- A normal translation-invariant state of such a theory is a mixture of vacua, so mixtures do not help (ARGUED, standard).

**Consequence.**
- The Poisson sprinkling is a Lorentz-invariant **classical (mixed) state with white spectral support**. Its spacelike support is what lets a sprinkled event scatter on-shell light into on-shell light. That is Z1's white, |Ψ|²-driven noise, seen as a first-chaos (single-scattering) term.
- A coherent substrate that removes the noise is a positive-energy vacuum. Its events cannot be a white 4D point process, and RL2's √Δ mean, which uses the Poisson Palm structure, does not transfer to it.
- **Named price P-Q1:** replace the classical Poisson sprinkling by a Lorentz-invariant positive-energy quantum vacuum. Discreteness then cannot live in a white point process of events. This fits O2's candidate "discreteness in Hilbert space, not in space". No discrete instance is known to me:
  - lattice ground states break boosts (C3);
  - spin-network and causet configurations are orthogonal, which puts them back in §2 or §3.
- **A distinguishing statistic (SUGGESTED):** the count variance in a region is a volume law for Poisson and sub-Poissonian (boundary-dominated) for a local vacuum.

## 5. Decoherence by matter (task item 2)

**In reading A** this is moot: the light is already mixed.

**In reading B** (final-state recombination), every system whose state depends on the configuration inside the light's needle must be projected too, or else traced, which decoheres.

**Estimates** (`q1_C` §3; SUGGESTED: that matter's own per-realization noise has the RL4 rate at the shared ℓ_k; arithmetic CHECKED):
- **Matter's own noise.** A matter quantum of age T carries γcT variance e-folds of configuration dependence: 0.36 (1 h), 8.6 (1 day), 3.2×10³ (1 yr), 3.2×10¹² (1 Gyr), 4.3×10¹³ (13.8 Gyr). Here γ = 3.33×10⁻¹³ m⁻¹ (c_low, ℓ_k = 7.9×10⁻²⁰ m).
- **Its reach.** Its past diamond has spatial width of about c×age, so it covers the needle of any lensed source.
- **The needle.**
  - For 1 s of emission at 1 Gpc: proper time 1.4×10¹⁷ m, transverse half-width 2.2 pc, about 10⁶⁸ CMB photons and 7×10⁵⁸ IGM baryons.
  - For 1 yr: half-width 12 kpc, about 4×10⁷⁵ CMB photons and 2×10⁶⁶ baryons, plus the lens galaxy.
- **Condition for negligible decoherence.** The summed which-sprinkling infidelity over these N quanta must be ≪ 1, i.e. below about 1/N ~ 10⁻⁶⁸ each. Against exponentially sensitive matter, I expect D(P,P′) ≈ 0 for configurations that differ in the needle. Matter decoherence then restores the mixture of §2.

**How finely a propagated field records a small region** (CHECKED, `q1_E`: Z2's model, op0, carrier ω₀ = 1; 1086 realizations at ε = ½, 702 at ε = ¼).

For each realization, the points inside one small 4-ball R are deleted and resampled at the same density. The sensitivity is

  s_R(t) = E|φ_P − φ_P′|² / (2 Var φ),

which is 1 for a fully independent sprinkling and 0 if the field ignores R.

| region R | 4-volume | points resampled | s_R at ε = ½ | s_R at ε = ¼ |
|---|---|---|---|---|
| near the source's turn-on edge, r = 0.5 | 0.31 ℓ_k⁴ | 0.6–1.3 | 0.18–0.37 | 0.14–0.25 |
| midway between source and observer, r = 0.5 | 0.31 ℓ_k⁴ | 0.6–1.3 | 0.06–0.24 | 0.03–0.19 |
| midway, r = 1.0 | 4.9 ℓ_k⁴ | 10–20 | 0.31–0.82 | 0.33–0.65 |
| off the source–observer axis, r = 0.5 | 0.31 ℓ_k⁴ | 0.6–1.3 | ≤ 0.001 | ≤ 0.001 |

The whole sprinkling region has a 4-volume of about 1000 ℓ_k⁴.

**Reading.**
- Resampling about one event near the source edge or on the source–observer axis changes the observed field by 10–40% of its entire noise variance. Resampling off the axis does nothing.
- So a propagated quantum records, at O(1) of its noise, the configuration in its own sensitive zone, which is dominated by the turn-on edge (RL4 T′).
- For a coherent probe with n̄ photons in its mean mode, |⟨α_P|α_P′⟩| = exp(−|α_P − α_P′|²/2), with E|α_P − α_P′|² = 2n̄ s_R V/|Ψ|². So the typical overlap is about exp(−n̄ s_R V/|Ψ|²).
- At the physical V/|Ψ|² ≥ e^{4.4×10⁴}, any s_R ≳ e^{−4.4×10⁴} gives total which-region decoherence.

**A concrete recorder (SUGGESTED).** Photons emitted in the same emission event but in other directions share the source's turn-on edge, the region the observed light is most sensitive to (s_R ≈ 0.2–0.4). They are absorbed by the source's surroundings and become records, so the near-source configuration is recorded.

**Records alone do not do this.**
- A record pins its event, but recorded events are a tiny fraction of all events: about 1.8×10³⁵ records per m³ per s in air, against c/ℓ_P⁴ = 4.4×10¹⁴⁷ events per m³ per s, a fraction of 4×10⁻¹¹³.
- Classicality comes dynamically: the Record axiom makes permanent the which-sprinkling information carried by configuration-sensitive matter.
- **For O4:** keeping the substrate "unrecorded" requires matter whose dynamics is insensitive to the microstructure at the 1/N level. The event route with a shared ℓ_k does not supply that.

## 6. Map to the FIXED Q1 readings

- **PASS** ("an explicit coherent-substrate rule under which the observed lensing amplitude is the RL2 mean, with residual fluctuations below observational bounds, and decoherence by observed matter shown negligible"): **not met.**
  - A: the amplitude is the RL2 mean, but the fluctuations are RZ's.
  - B1: the image is extinguished.
  - B2: works for one mode only, with the three costs of §3.4.
  - C: noise-free, but not Poisson, and the mean is not established.
  - In every case, decoherence by matter is not negligible at the shared ℓ_k.
- **FAIL** ("a proof that the noise reappears, intensity-level or via decoherence, at RZ's level in the stated class"):
  - **Met for the traced-out subclass, and for every coherent version that uses only unitary dynamics.** Theorem A and A′ are exact identities, so the reappearing noise is RZ's number itself. The status is RZ's controlled level with RZ's scope.
  - **Met, at a different face, for uniform-amplitude recombination with Gaussian per-mode noise.** Theorem C (exact) gives an amplitude factor e^{−4.4×10⁴} (`q1_C` §2, any n̄ from 10⁻¹⁰⁰ to 4×10¹¹; the requirement is V_ph ≤ 0.24). Gaussianity for incoherent sources is ARGUED.
  - **Not met for structured complex final-state amplitudes across many modes.**
- **Worker reading: FAIL (bounded)** to configuration-diagonal coupling (all phases) and to uniform-amplitude recombination with Gaussian noise. If the referee counts the structured-phase final-state subclass as part of the "stated class": **INCONCLUSIVE, leaning FAIL**, with the necessary prices of §3.4 and §5 named.

**Against the supervisor's expectation** ("INCONCLUSIVE; coherent averaging removes noise from amplitudes, intensities pick up a |Ψ|² variance term equal to RZ's; lean FAIL"):
- **Confirmed, and sharper.** The intensity term equals RZ's exactly, as an identity. So the traced-out reading is not inconclusive: it is the classical FAIL itself.
- **The "decoherence-like broadening" alternative appears as extinction.** When coherence is kept by the only available means, a final-state projection, the recombined image is pure but dimmed by 2/(2+V). It is not broadened.

## 7. Side finding: the noise is typical at accessible ε (CHECKED, `q1_B`)

On Z2's realizations (carrier ω₀ = 1, late window):

| ε | median\|δ\|²/V (circular Gaussian 0.693) | E\|δ\|⁴/V² (circular Gaussian 2) | share of V in top 1% / 10% | d/dτ of ln V / ln median\|δ\|² / E ln\|δ\|² |
|---|---|---|---|---|
| 1 | 0.024 | 103 | 0.63 / 0.92 | 4.674 / 4.723 / 4.724 |
| ½ | 0.242 | 7.8 | 0.22 / 0.64 | 2.721 / 2.716 / 2.718 |
| ¼ | 0.480 | 3.4 | 0.11 / 0.47 | 1.469 / 1.473 / 1.472 |
| ⅛ | 0.600 | 2.4 | 0.05 / 0.37 | 0.770 / 0.796 / 0.795 |

**What the table shows.**
- The typical (quenched) growth rate equals the annealed (variance) rate within 3% at every ε.
- The law becomes more Gaussian as ε falls.
- So at accessible ε, the variance growth that RZ uses is not carried by rare realizations. This bears on Y1's referee caveat ("representative rather than rare-tail ensemble behavior").

**Scope.** It does not settle physical ε: no extrapolation is made (TESTS.md:5–9). It also supports the "no quiet atom" premise behind §3.2–3.3.

**Coherent fraction.** At ε = ⅛, Γ = |Eφ|²/E|φ|² = 0.0098 (0.0081 bias-corrected), consistent with V/|Ψ|² ≈ 122.

## 8. Flags for the referee

1. **Theorem A's model.** It assumes configuration-diagonal coupling (the light sees a definite sprinkling per branch) and orthogonal configuration states. These are what "a superposition over sprinklings" means here. A substrate whose density operators do not commute is §4, not §2.
2. **Coherent-state reading of the classical source.** U_P = D(H_P J) is ARGUED as standard. The RL operator is not a unitary one-particle map, so "photon propagation by G_P" is used only in the one-photon remark of §3.1, as linear algebra.
3. **Back-reaction.** Per realization, the radiated energy is e^{4.4×10⁴} times GR's, so the substrate does work on the light. Including back-reaction adds substrate records and only strengthens A.
4. **Theorem C** assumes circular Gaussian per-mode noise. For one coherent source the noise is non-circular (§3.3), and the surrogate with the matching covariance agrees with the Monte Carlo. Circularity for incoherent sources is ARGUED from independent phases.
5. **Theorem D(i)–(iii)** are single-mode statements. The multimode existence question is open. The L² step uses bounded p_μ.
6. **Lemma F** is the standard Wightman spectral-support argument. It needs the substrate density to be a local field in a positive-energy representation, and it is not a statement about classical processes.
7. **§5's matter estimate** assumes matter's per-realization noise has the scalar RL4 rate (shared ℓ_k). This is unproved for massive fields.
8. **Observational allowances** (visibilities, flux ratios) are RECALLED, as in Y1/RZ.
9. **`q1_B` recombination rows at ε = ¼** use an unresolved mean (|mean|²/sem² = 0.8) and are not meaningful. Only the ε = ⅛ rows with a resolved mean are used (`q1_B2`, t ≤ 5.0).

## Files (scratch: `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/Q1/`)

| script | output | content |
|---|---|---|
| `q1_A_toy_theorems.py` | `q1_A_toy_theorems.out` | Theorem A for any phases; no-signalling; final-state projection and the missing probability; Theorem C against Monte Carlo; non-Gaussian anti-concentration toys; linear combinations of unitaries |
| `q1_B_realizations.py` | `q1_B_realizations.out` | Z2 realizations: Γ, distribution shape, typical vs annealed rates, recombination by photon scale |
| `q1_B2_surrogate.py` | `q1_B2_surrogate.out` | ε = ⅛ recombination: Monte Carlo vs same-covariance Gaussian surrogate vs circular formula, with bootstrap |
| `q1_C_physical.py` | `q1_C_physical.out` | physical translation: Γ_B, recombination extinction by source occupation, matter ages, needle contents, records fraction, Lemma E kinematics |
| `q1_D_structured_phase.py` | `q1_D_structured_phase.out` | explicit single-mode structured complex amplitude: normalizability, fidelity, branch weight c(λ) |
| `q1_E_region_sensitivity.py` | `q1_E_eps05.out`, `q1_E_eps025.out` | resample one small 4-ball; the fraction s_R of the noise variance it controls (Z2's model; copies of `rl2_core.py` and `RL1/` from `RZ/Z2`) |
