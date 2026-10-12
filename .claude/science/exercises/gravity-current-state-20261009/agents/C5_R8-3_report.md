# C5 round 8, probe R8-3: a relativistic completion of R6-4's smeared CQ gravity (worker report)

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every other C5 worker. **Not refereed.** Run 2026-10-12, 15:38Z to 16:01Z. No repository file was edited.

**Scratch folder:** `scratchpad/C5/R8-3/`.
- `scripts/r83_checks.py` and `scripts/r83_checks.out` (sections [1]–[9]) hold every number below.
- SHA-256 of the script: `52638ca8…de8b`. SHA-256 of the output: `43966f30…81ab`.
- No new downloads. The arXiv text of Layton et al. 2307.02557 is read as data from `scratchpad/C5/ref_R6-4/sources_untrusted/source_Layton_2307.02557.clean.txt` (cited as `LAY:`). The OWD 2302.07283 text is read from `scratchpad/C5/R6-4/text/owd2302.txt` (cited as `OWD:`).

**Path abbreviations.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`
- `TESTS` = `P/TESTS.md`

**What I read.**
- In full: `AX` (233 lines); `TESTS:2302-2440` (the C5 method and round 1); `TESTS:3396-3481` (the round 6–7 referee results, the R6-4 entry with its dated correction, and round 8); `P/agents/C5_R6-4_report.md`; `C5_R6-4_referee.md`; `C5_R6-4_referee_verdict.md`; `C5_R3-4_referee.md`; `C5_O4_referee.md`.
- In part: `TESTS:2755-2947` (the round 3–4 results); `C5_R3-4_report.md:200-300` (E2); `C5_R4-4_referee.md:30-66` (Lemma N); `C4_X1_report.md:25-75` (the non-locality bounds).

**Labels.**
- **proved:** a derivation given here, under the stated hypotheses.
- **checked:** a number in `r83_checks.out`.
- **suggested:** argued, not proved.
- **reading:** an interpretation.
- **comparator:** literature. Each comparator is marked web-checked (fetched in this run), local text (from the `ref_R6-4` copies) or recalled.

---

## Reading against the fixed rule (TESTS:3468-3481)

| Scope | Reading | Basis |
|---|---|---|
| **Class 𝒞**: covariant smeared Gaussian CQ gravity with Lorentz- and translation-invariant kernels and a Lorentz-invariant form factor F(□) on the T_μν coupling, in which photons gravitate. 𝒞 contains every construction the item names (e^{ℓ²□}, causal smearing, OWD with field-dependent kernels taken about flat space), plus e^{−ℓ⁴□²} and OWD's own ultra-local kernel. | **EXCLUDED: internally inconsistent.** Worker reading; referee required. | Theorem 3 (§3): three requirements cannot all hold — Newton's law at long range, a finite radiation field, and a finite rate of vacuum excitation |
| The bound tests themselves (γ, Shapiro delay, c_T) | **Every member of 𝒞 passes** at the mean-field level. What fails is internal, not these bounds. | §4 (proved; checked [4] and [6]) |
| R8-3 overall: a relativistic completion | **OPEN** | VIABLE needs an explicit covariant theory. The only route found that passes (§5) has a preferred frame. Its covariant form, with a dynamical frame field, is not constructed. The discrete-jump class and non-Gaussian class lie outside 𝒞. |

**Against the expectation.** Neither covariant option the pre-registration names survives in class 𝒞, and the smearing is not what kills them. Any covariant kernel that couples to the timelike stress spectrum excites the vacuum at an infinite rate per unit 4-volume. Continuity at the light cone forces that coupling.

---

## 0. In plain words

- **The mean field passes every test.** Smear the source of gravity covariantly, so that the classical metric obeys Einstein's equations with a blurred T_μν.
  - Light bending and the Shapiro delay are unchanged except within a few ℓ of a mass. At the Sun the deficit is e^{−10^28}.
  - Gravitational waves travel at exactly c, because nothing in the vacuum wave equation changed.
  - So γ, Shapiro and GW170817 all pass.
- **The vacuum fails.** In classical–quantum gravity, coupling matter to a classical field costs noise, which disturbs the matter: the decoherence–diffusion trade-off.
  - If the noise law is Lorentz-invariant, the empty-space vacuum gets kicked in a Lorentz-invariant way.
  - A Lorentz-invariant spread of kicks has infinite total size, because the set of boosted copies of any kick has infinite volume.
  - So the vacuum is excited at an infinite rate unless the coupling vanishes on every "timelike" momentum (frequency larger than wavenumber).
- **That cannot be arranged.**
  - Newton's law needs the coupling to equal 1 on the spacelike side of the light cone.
  - Gravitational radiation needs the coupling to be continuous across the light cone; otherwise the radiated field is infinite.
  - So the coupling is nonzero just inside the timelike region. Light pairs there, and the vacuum blows up.
  - e^{ℓ²□} is worse still: it grows like e^{ℓ²(ΔE/ħc)²} on timelike momenta. At ℓ = 5 µm even 0.03 eV infrared processes are amplified, and the exponent at a 1 MeV nuclear line is about 10^15.
- **The way out is a preferred frame.** Let the noise and the smearing pick a rest frame, as a lattice does; the mean field stays Einstein's.
  - Then γ, Shapiro and c_T still pass, and the vacuum excitation is finite.
  - The vacuum excitation produces photons of about ħc/ℓ, which pushes the lower end of the window from about 4 Å to about 5–20 nm (order of magnitude).
  - This is not covariant, so it does not meet "VIABLE".

---

## 1. Prior art (each counted once)

1. **R6-4** (refereed, `TESTS:3409-3418`).
   - Smeared Newtonian CQ is VIABLE on 4e-10 to 5e-6 m.
   - Lemmas T and F hold under hypotheses H1–H4 (`C5_R6-4_referee.md:35-55`).
   - Corollary U is narrow: it covers cutoff-free point particles only (`:57-64`).
   - The covariant family is OPEN (`:188-195`).
   - The worker flagged e^{ℓ²□}'s timelike growth as "recalled, not checked" (`C5_R6-4_report.md:194`).
2. **R3-4 E2** (`C5_R3-4_referee.md:27-29`): the OWD diffeomorphism-invariant candidate exists, and its full GR application is "a candidate".
3. **O4 Lemma 1** (`C5_O4_referee.md:5`): V ≤ BC for a perfectly readable classical record.
4. **R4-4 Lemma N** (`C5_R4-4_referee.md:43-49`): a classical channel gives zero concurrence.
5. **C4 X1** (`C4_X1_report.md:49-56`): bounds on non-locality.
   - Matter-sector form factors are collider-bounded at ℓ ≲ 4e-20 m.
   - Gravity-only infinite-derivative gravity is bounded at ℓ ≲ 5e-5 m (G1, search snippet).
   - R8-3's smearing sits on the gravitational coupling only, so the collider bounds do not apply (reading).
6. **Repository grep** for "classical-quantum", "Oppenheim", "CQ gravity" and "postquantum".
   - Hits are confined to the C5 packet (`SUMMARY.md:562-563`; `C5_R2-3_report.md:82,249`; `C5_S5_synthesis.md:331,479-488`; R3-4, R6-4).
   - The other hits are unrelated: Born–Oppenheimer; a "declared classical-quantum domain" in `docs/ADMISSIBILITY_D4_COVARIANT_CONDITIONAL_CAP_PACKET_INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md:153`; and Oppenheim–Margulis in R3-3.
   - No repository derivation of vacuum excitation in covariant CQ exists.
7. **Literature points relevant here.**
   - **OWD's complete-positivity theorem is stated for time-local path integrals** (`OWD:173`). Kernels that are covariant and extended in space "must also have temporal correlations and so they represent non-Markovian dynamics" (`OWD:645-648`, local text).
   - **Layton et al. on non-Markovian kernels.** They call non-Markovian dependence through time integrals of Φ "still guaranteed to be CPTP" (`LAY:1712-1716`). They ask for relativistic corrections below 10⁻¹⁵ m (`LAY:232-234, 1748-1751`) and leave finite-c open.
   - **Relativistic collapse.** White Lorentz-invariant noise excites the vacuum with infinite energy production. Pearle 1999 (quant-ph/9902046) locates the cause in the noise's timelike spectral components (comparator; the content claim is a search snippet, the abstract fetched did not show it).
   - **Carney–Matsumura** (arXiv:2412.04839, abstract web-checked). The simplest OWD-framework CQ gravity, mapped to point-mass 2→2 scattering, conflicts with slingshot observations. Its bearing on smeared kernels is not checked here.

## 2. Hypotheses: class 𝒞 (stated before any title)

- **H1′ (linearized CQ gravity on Minkowski).**
  - The classical metric perturbation obeys the linearized Einstein equation with source 8πG·J_μν, where J = F(ℓ²□)⟨T⟩ + ξ and ξ is zero-mean Gaussian noise with spectrum P_J(p).
  - The coupling is symmetric: matter feels h through the same smeared operator F·T (`OWD:415-418`; this is R6-4's H2).
  - **Asymmetric coupling** (matter feels unsmeared T) is also covered, as noted under Lemma 2.
- **H2′ (covariance).**
  - Every kernel (F, P_J, and the direct decoherence D₀) is translation-invariant and Lorentz-invariant: a function of the invariant s ≡ □-eigenvalue = (p⁰)² − |p|², per spin channel.
  - Markovian or not.
  - Field-dependent kernels are evaluated on the flat background, where they are Lorentz-invariant.
- **H3′ (trade-off and additivity).**
  - At every p with F(p) ≠ 0: P_J(p)·D₀′(p) ≥ ¼ on the smeared operator (Lemma T of R6-4, Fourier-diagonal in 4-momentum).
  - The direct decoherence and the random-metric dephasing add (H4 of R6-4). This is the measurement-and-feedback structure: the cross term there is Hamiltonian, not dephasing (suggested).
  - The same lower bound follows, for a branch pair, from V ≤ BC applied to the metric history (O4 Lemma 1).
- **H4′ (matter).**
  - The vacuum is Poincaré-invariant and unique, with the spectral condition.
  - The electromagnetic T_μν is in the source (universality).
  - Its spin-2 Wightman spectral weight W(s) = a·s²·θ(s), with a > 0, is nonzero for every s > 0 (free Maxwell field; standard).
- **H5′ (form factor).** F has one-sided limits at s = 0 (it is piecewise continuous), and F(−p) = F(p)* (the smeared source is real).
- **Golden-rule order.** Vacuum excitation is computed at second order in the CQ coupling: the rate per unit 4-volume is μ(B) = ∫_B d⁴p/(2π)⁴ K(p)W(p).

**Realizations outside 𝒞.**
- Kernels that select a frame, whether fixed or through a dynamical vector or foliation field (§5).
- Discrete-jump CQ, and non-Gaussian CQ.
- Kernels that are not translation-invariant.
- Theories in which photons do not source gravity: this costs the equivalence principle.

## 3. Lemmas and the theorem

**Lemma 1 (V0: a Lorentz-invariant excitation of the vacuum is zero or infinite).** A nonzero Lorentz-invariant Borel measure μ on V̄₊∖{0} has infinite total mass, and infinite total energy.

*Proof.*
1. By rotation invariance, μ(E) > 0 for some E = {a ≤ p⁰ ≤ b, p_z ≥ 0}.
2. Boosting along +z with rapidity η gives p⁰ ∈ [a cosh η, b e^η] on E.
3. Choosing η_{n+1} with a cosh η_{n+1} > b e^{η_n} makes the images Λ_n E pairwise disjoint, so μ ≥ Σ_n μ(E) = ∞. ∎

[proved; checked [1]: the rapidities 0, 1.32, 2.70, 4.08, … give disjoint copies. The shell measure inside |p| < Λ grows as πΛ², with N/Λ² → 3.14159.]

**Lemma 2 (covariant least-decoherence floor).** Under H1′–H3′, the total matter kernel on T is

  K(p) = D₀ + c_N²|F|²P_J/s², with D₀ = D₀′|F|².

Its lower bound is

  **K(p) ≥ c_N|F(p)|²/|s|**, for timelike and spacelike p alike.

- c_N = O(G/ħ) is fixed by the coupling normalization. At ω = 0 this is exactly R6-4's Lemma F: K ≥ (4πG/ħ)|g̃|²/k².
- The proof is R6-4's argument, with k⁴ replaced by |G̃_R(p)|⁻² = s² off the light cone.
- [proved given H1′–H3′; checked [7]: the minimum of K/floor over 20000 random draws is 1.000025.]
- **Weaker form, without additivity:** K(p) > 0 wherever F(p) ≠ 0. Either P_J > 0 and the classical random metric (a mixture of unitaries) dephases, or P_J = 0 and the trade-off forces D₀ = ∞.
- **Asymmetric coupling.** If matter feels unsmeared T, the same conclusion holds: K > 0 wherever F ≠ 0.

**Lemma 3 (a jump at the light cone makes the radiation field infinite).**
- Take a monochromatic, compactly supported source with T̃(ω₀, |k| = ω₀) ≠ 0 in the spin-2 transverse-traceless channel (any GW emitter).
- Then h = G_R·F·T at any r > 0 has a term (F(0⁻) − F(0⁺))·sin(ω₀r)/(2r)·T̃·ln(1/ε), where ε is the retarded iε.
- So h is finite only if F is continuous at s = 0.
- [proved for the monochromatic point-like source; checked [2]:
  - the projector F = θ(−s) gives a real part growing as +0.07052 per unit of ln(1/ε), equal to the predicted sin(ω₀r)/2·e^{−(ω₀/K)²} = +0.07052;
  - F = 1 converges to −1.55410 + 0.22153i;
  - a continuous F converges to −0.70857 + 0.22153i.]
- Extension to pulsed sources: suggested. The ω-integral of the log coefficient does not vanish for generic sources.

**Lemma 4 (Newton).** Newton's law with the measured G at r ≫ ℓ needs F(s → 0⁻) = g̃(k → 0) = 1. [definition of G]

**Theorem 3 (covariant smeared CQ: the trilemma).** In 𝒞, the following are incompatible:
- (N) Newton's law at long range;
- (R) a finite mean radiation field for compact time-dependent sources;
- (V) a finite vacuum-excitation rate per unit 4-volume.

*Proof.*
1. (N) and (R), with Lemmas 3 and 4, give F(0⁺) = 1.
2. By H5′ there is a δ > 0 with |F| > ½ on (0, δ).
3. Lemma 2 gives K > 0 in the spin-2 channel there, and H4′ gives W > 0 there. So the golden-rule measure μ is nonzero.
4. Lemma 1 then makes μ infinite, contradicting (V). ∎

[proved given H1′–H5′ at golden-rule order. This is a no-go: **referee required.**]

**A second, independent horn (suggested).**
- At s = 0 the trade-off reads P_J(0)·D₀(0) ≥ |F(0)|²/4 = ¼.
- If P_J(0) > 0, a Lorentz-invariant noise spectrum on the null cone pumps the classical gravitational-wave modes. By Lemma 1 applied to the null-cone measure, the pumped energy is infinite.
- If D₀(0) = ∞, matter decoheres without limit at null momentum transfer.

**Corollaries** (each proved from Theorem 3 or directly; referee required):

| Construction | Fate |
|---|---|
| **e^{ℓ²□}** (Gaussian on static momenta) | F = e^{ℓ²s} is unbounded on timelike s. The local operator e^{ℓ²□}T(x) has infinite vacuum norm before any boost integration: ∫ds s² e^{2ℓ²s} = ∞ ([3]). Every timelike process is amplified by e^{2ℓ²(ΔE/ħc)²} ([3]). At ℓ = 4e-10 m the exponent is 8.6e6 at the e⁺e⁻ threshold and 1.1e7 at the Co-60 line. At ℓ = 5e-6 m it exceeds 1 for every ΔE > 0.028 eV, which includes thermal infrared photon pairs. **Excluded across the whole R6-4 window.** |
| **e^{−ℓ²□}** (opposite sign) | Grows on static momenta: anti-smearing, with heating worse than Corollary U. Excluded. |
| **Causal (retarded) smearing**, e.g. F = 1/(1 − ℓ²□)_ret or any kernel supported in the past cone | F is the boundary value of a function analytic in the tube, so it cannot vanish on the open timelike region (standard analyticity/edge-of-the-wedge; comparator). Hence μ = ∞ by Lemmas 1–2. This is consistent with Belenchia–Benincasa–Liberati's continuum of massive modes for the retarded causal-set d'Alembertian (arXiv:1411.6513, abstract web-checked). |
| **Bounded entire choices**, e^{−ℓ⁴□²} and Modesto-type e^{−H(□)} with H even | Continuous at s = 0 with F(0) = 1, so Theorem 3 gives μ = ∞. |
| **Spacelike projector** F = θ(−s)·g̃ (Pearle-style: no timelike spectrum) | Vacuum is safe, but Lemma 3 fails: infinite radiation field. The kernel is also acausal, with power-law tails (suggested). |
| **OWD as written** (ultra-local D₀δ⁴, F ≡ 1) | D₀ is positive on physical local degrees of freedom (`OWD:617-620`). The traceless photon channel is such a degree of freedom, so K ≥ D₀ > 0 on every timelike shell and μ = ∞. The coincident-point ⟨TT⟩ is also UV-divergent: the relativistic-CSL white-noise problem (comparator). [proved at golden-rule order within H1′–H4′; this is a strong claim about a published construction and needs a referee.] |
| **OWD with field-dependent kernels** | About flat space the kernels are Lorentz-invariant, so Theorem 3 applies at linear order. Kernels that vanish on flat space (e.g. D₂ ∝ curvature) force D₀ = ∞ wherever the drift is nonzero, which is worse. Only kernels depending on a non-geometric background vector escape; OWD themselves note that these "introduce a preferred background or must be made dynamical" (`OWD:640-643`). |

## 4. The stated tests within 𝒞 (they are not what fails)

- **γ and Shapiro delay.**
  - The mean field is linearized GR with the conserved source F·T. F commutes with ∂, so ∂·(F·T) = F·(∂·T) = 0 and the Bianchi identity holds.
  - For static dust, h₀₀ and h_ij carry the same smeared Φ, so **γ = 1 identically** (proved).
  - The deflection deficit is exactly e^{−b²/2ℓ²} ([4]: numeric equals closed form to 10 digits at b = 1–8ℓ). At the Sun's limb the exponent is −1.5e36 for ℓ = 4e-10 m and −9.7e27 for ℓ = 5e-6 m, against Cassini's |γ − 1| ≲ 2.3e-5 (comparator, search).
  - The Shapiro excess is 2.8e-7 of the unit GM/c³ at b = 5ℓ and 3.8e-16 at b = 8ℓ ([4]).
- **c_T and GW170817.**
  - The vacuum wave operator is untouched, so classical metric waves move at exactly c with two TT polarizations (proved).
  - The observed bound is −3e-15 ≤ Δc/c ≤ 7e-16 (Abbott et al. 2017, comparator, search). In 𝒞 the emission coupling at null momenta is F(0) = 1.
  - Stochastic phase noise along 40 Mpc is not computed. The R6-4 noise floor suggests it is negligible (suggested).
- **The timelike problems of e^{ℓ²□}:** see the corollary table. The problem is real and fatal for this form factor ([3]).
- **Complete positivity at finite c.**
  - Covariant smearing is non-Markovian (`OWD:645-648`), outside OWD's time-local CP theorem (`OWD:173`). I found no CP proof for covariant non-Markovian kernels.
  - Theorem 3 does not need full CP: it uses only the pointwise trade-off or V ≤ BC. So the CP question is moot for 𝒞.

## 5. The live route: a preferred-frame relativistic completion (outside 𝒞; OPEN)

**Explicit family 𝒫.**
- **Mean field.** Linearized (or full) GR with source F_u·T, where:
  - F_u(ω, k) = e^{−k²ℓ²/2}·(1 − iωτ)^{−n}, with n ≥ 2 and τ = ℓ/c as the minimal choice;
  - ω and k are taken in a rest frame u^μ;
  - the temporal factor is causal (retarded).
- **Noise.** On the trade-off, with the Lorentzian least-decoherence choice D₀ = c_N|F_u|²/(|s| + μ²), where μ is a tiny null-cone regulator.
- **Newtonian limit.** At ω → 0 this is exactly R6-4's least-decoherence kernel, so R6-4's laboratory table carries over (reading).

**Tests.**
- **γ and Shapiro:** as in §4 (proved; [4]).
- **c_T:** exactly c (proved).
- **GW emission.**
  - At 100–1000 Hz, 1 − |F_u| is 1e-30 to 2e-20 ([6]).
  - The causal lag nτ is 3e-18 to 3e-14 s, against GW170817's 1.74 s window ([6]). Passes.
- **Vacuum excitation.**
  - Finite, because F_u decays in the frame.
  - Energy injection Ė ≈ A′·ħc²ℓ_P²/ℓ⁷, in photons of about ħc/ℓ. A′ is uncertain within 1e-4 to 1; it carries the Maxwell spin-2 spectral coefficient. My estimate is A′ ~ 1e-2, using a ≈ N_eff/960 with N_eff = 12 (recalled).
  - Requiring the Hubble-time injection to stay below the whole extragalactic background light (u_EBL ≈ 2.5e-15 J/m³, recalled) gives **ℓ ≳ 4.6e-9 m (A′ = 1e-4), 8.9e-9 m (A′ = 1e-2), 1.7e-8 m (A′ = 1)** ([5]). The photons would be at 11–43 eV.
  - The EBL comparison is deliberately weak; ionizing-background and X-ray bounds would be tighter.
  - For general τ the constraint is on ℓ³τ⁴.
  - [suggested, order of magnitude.] **So the relativistic preferred-frame window is about 1e-8 m ≲ ℓ ≲ 5e-6 m**, narrower than R6-4's Newtonian 4e-10 m.
- **The null cone.**
  - With μ > 0, gravitational-wave pumping stays below an Ω_GW ~ 1e-6 background if 1/μ ≳ 4e9 to 4e15 m ([9]).
  - The price is a logarithmic enhancement of about 80–105 in null-transfer decoherence ([9]).
  - [suggested; coefficients not derived.]
- **Complete positivity.** Can be met by an ancilla, or "pointer-field", realization of the causal temporal smearing, followed by continuous measurement. CP then holds by construction (suggested; Bedingham-type pointer field, recalled).

**Prices (named, not adopted).**
- **(P-r1) A preferred frame** u^μ in the noise kernels and the smearing. It is a fixed background, or a dynamical vector or foliation field; the dynamical version needs its own GW170817 and PPN α₁/α₂ checks and is not constructed here.
- **(P-r2) A temporal smearing scale τ** with causal, non-Markovian memory.
- **(P-r3) R6-4's prices P-i1 to P-i5.**
- **(P-r4) Photons are created from the vacuum** at a rate of about A′ℓ_P²c/(ℓ³(cτ)³) per unit volume per unit time.
- **(P-r5) A null-cone regulator μ.**

**Axiom texts touched (reading).** The frame u^μ is the kind of structure the axioms' Z³ supplies: `AX:37-41` fixes a lattice and therefore a rest frame. But set A replaced Z³ by a continuum. The Qubit, Admissibility and Record prices of R6-4 (iii) stand unchanged (`C5_R6-4_referee.md:231-238`).

## 6. Strong words checked

- "Every", "any" and "all" in §§3–4 mean every member of 𝒞 (H1′–H5′), at golden-rule order.
- "Infinite" means that the invariant measure has infinite mass (Lemma 1), not merely a large regulated number.
- "Proved" is used for Lemmas 1–4, Theorem 3 and the §4 mean-field statements only.
- Everything in §5 is suggested, with order-of-magnitude coefficients.
- The OWD-as-written corollary is a strong claim against a published construction. It rests on `OWD:617-620` (D₀ is positive on physical local degrees of freedom) and on the photon channel being such a degree of freedom. **Referee required.**
- The claim about Pearle's timelike spectral components is a search snippet only.

## 7. What would decide it

1. **A referee of Theorem 3**, especially:
   - Lemma 3 for pulsed sources;
   - the additivity hypothesis H3′;
   - whether a tensor-valued F could evade it in the spin-2 channel (I argue it cannot: GWs and the photon vacuum share that channel).
2. **The covariant form of §5.** Build the dynamical frame field (aether or khronon type), coupling only through the CQ kernels. Then test c_T to 1e-15, PPN α₁ and α₂, and the frame field's own vacuum stability.
3. **An exact value of A′**, from the Maxwell ⟨TT⟩ spectral coefficient, and ionizing-background bounds on the vacuum photons.
4. **The discrete-jump CQ class.** Lemma 1 applies to any Lorentz-invariant excitation, but the jump-class trade-off is not derived here.
5. **Whether Carney–Matsumura's slingshot exclusion persists for smeared kernels.**

**Sources.**
- Web-checked:
  - [Grudka et al., arXiv:2402.17844](https://arxiv.org/abs/2402.17844), abstract: CP "appears to single out the scale invariant" theory.
  - [Carney–Matsumura, arXiv:2412.04839](https://arxiv.org/abs/2412.04839), abstract.
  - [Pearle, quant-ph/9902046](https://arxiv.org/abs/quant-ph/9902046), title and abstract only.
  - [Belenchia–Benincasa–Liberati, arXiv:1411.6513](https://arxiv.org/abs/1411.6513), abstract.
  - [Biswas–Mazumdar–Siegel, hep-th/0508194](https://arxiv.org/abs/hep-th/0508194), abstract: JCAP 0603:009.
  - [GW170817/GRB 170817A, arXiv:1710.05834](https://arxiv.org/pdf/1710.05834), via search.
  - Cassini γ − 1 = (2.1 ± 2.3)e-5, via search.
  - Collapse-model reviews on the infinite energy of relativistic white noise ([arXiv:2310.14969](https://arxiv.org/pdf/2310.14969); [arXiv:1204.4325](https://arxiv.org/pdf/1204.4325)), via search.
- Local text: OWD 2302.07283; Layton et al. 2307.02557.
- Recalled: the EBL energy density; the Ω_GW bound; the Maxwell spectral coefficient; Bedingham's pointer field.
