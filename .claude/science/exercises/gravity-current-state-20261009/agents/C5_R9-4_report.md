# C5 round 9, probe R9-4: covariant CQ gravity outside the R8-3 subclass (worker report)

**Worker.** Claude Opus 5.5, the same family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-12, 16:38Z to about 17:30Z. No repository file was edited.

**Scratch folder:** `scratchpad/C5/R9-4/`.
- `scripts/r94_checks.py` and `scripts/r94_checks.out` (sections [1]–[7]) hold every number below. Runtime about 6 s.
- SHA-256 of the script: `52b1cad3…8347`. SHA-256 of the output: `6851c3ff…fafa`.
- No new downloads. The OWD text is read as data from `scratchpad/C5/R6-4/text/owd2302.txt` (cited as `OWD:`). Layton et al. is read as data from `scratchpad/C5/ref_R6-4/sources_untrusted/source_Layton_2307.02557.clean.txt` (cited as `LAY:`).

**Path abbreviations.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; bare `C5_*` files are in `P/agents/`.

**What I read.**
- In full: `AX`; `TESTS:2302-2440` (the C5 method and round 1); the round 4–8 results, `TESTS:2900-3008` and `:3285-3573`; the round 9 block, `TESTS:3575-3791`, with R9-4 at `:3707-3738`; `C5_R8-3_report.md`; `C5_R8-3_referee.md`; `C5_R8-3_referee_verdict.md`; `C5_R6-4_report.md`; `C5_R6-4_referee_verdict.md`; `C5_R6-4_referee.md:1-140`; `SUMMARY.md:534-606` (§§21–23).
- In part: `C5_S8_synthesis.md:1-60,105-135,280-320` and its R9-4 draft at `:446-475`; the R8-3 worker and referee check outputs; `OWD:600-660`; `LAY:155-165,590-598,1700-1720`.

**Labels.**
- **proved:** derived here under the stated hypotheses.
- **checked:** a number in `r94_checks.out`.
- **suggested:** argued, not proved.
- **reading:** an interpretation.
- **comparator:** literature, marked web-checked (fetched in this run), local text, or RECALLED.

---

## Reading against the fixed rule (`TESTS:3730-3733`)

| Variant | Reading (worker; referee required for each EXCLUDED) | Basis |
|---|---|---|
| **(i) spacelike-supported noise kernels** | **EXCLUDED** in class 𝒯 (defined below). Outside 𝒯, the timelike region is no longer classically mediated. | Lemma S1 plus Lemma L (§3): Newton forces a jump in F at the light cone. The jump gives a far field growing as ln r, which no light-cone counterterm removes ([1]). |
| **(ii) spin-separated** (spin-2 GR-normalized; scalar carries the noise) | **EXCLUDED** in 𝒯. As literally posed it is not CP. Repairing it puts it inside R8-3's refereed subclass. | Lemma S2 ([2]); R8-3 repaired theorem (`C5_R8-3_referee_verdict.md:11,19`); Cassini bound on any scalar drift, and γ = −1 for a trace-only drift ([3]) |
| **(iii) non-Markovian, non-additive** | **OPEN**, with a sharpened conditional no-go | (a) OWD's own spacetime-correlated class (Eq. 27) is automatically additive, so R8-3 applies there ([4]). (b) A finite vacuum outside it needs perfect emission-side anticorrelation, so matter no longer feels the classical record ([6]). Sub-floor decoherence needs a joint meter, which entangles ([5]). |
| **(iv) preferred frame** | **OPEN**. The window is computed under named conditions. | The μ-ansatz excess is reproduced. An exact least-decoherence kernel needs no μ. **Correction: n ≥ 3, not n ≥ 2.** The near-cone classical-GW content gives a conditional lower end of about 1.5–3.4e-7 m ([7]). |

**Overall.** No VIABLE variant. Against the expectation (`TESTS:3734-3738`):
- (i) and (ii) come out EXCLUDED in a stated class, where OPEN was expected.
- (iii) is OPEN, as expected.
- (iv) is OPEN with a computed window, as expected, but narrower than R8-3's target.

**Class 𝒯 (stated before any title).**
- Linearized CQ gravity on Minkowski space.
- Translation-invariant, stationary Gaussian statistics, with Lorentz invariance in (i)–(iii).
- The classical field is h = G_R·(F·T + ξ), with the standard massless retarded G_R and a light-cone form factor F that has one-sided limits at s = 0.
- Matter feels the classical h. A direct backaction B may also act.
- **The pointwise product trade-off (H-T).** At every 4-momentum p, and in every spin channel, the block matrix [[P_J, F/2], [F*/2, D₀′]] ≥ 0.
- Golden-rule order wherever a vacuum rate is computed.

**Why (H-T) is the right class for non-Markovian kernels (proved under stated hypotheses; comparator).**
1. For translation-invariant kernels in space and time, an operator inequality on L²(ℝ⁴) is exactly a pointwise inequality in 4-momentum.
2. **Gaussian dilation.** Realize the classical record as the output of a linear quantum detector (a meter field) in a stationary state. The record J commutes with itself, and the detector has no reverse gain (the commutator [J(x), B(0)] is retarded). Positivity of the 2×2 unsymmetrized spectral matrix of (B, J), together with Cauchy–Schwarz on the commutator spectral weight, then gives S_JJ(p)·S̄_BB(p) ≥ |F(p)|²/4 at every p. This is the stationary quantum-noise constraint of Clerk et al., RMP 82, 1155 (2010), Eq. (90) (comparator; equation web-checked on ar5iv; the per-frequency reading is mine).
3. So (H-T) holds for temporally correlated kernels too. Layton et al.'s remark that non-Markovian D₀, D₂ "need not" obey the instantaneous trade-off (`LAY:160`) concerns the time-local form, not this frequency-resolved one.
4. What (H-T) does **not** fix is additivity, meaning whether B and the fed-back record noise are correlated. Variant (iii) lives there.

---

## 0. In plain words

- **(i) Noise only at spacelike momenta.** Static gravity is at spacelike momentum, so this looked promising. But classical gravity pays for its pull with noise, at every momentum where matter pulls on the field. Newton fixes that pull at 1 just outside the light cone. If there is no noise inside the cone, the pull must drop to 0 there, so it jumps at the cone. A jump makes the field of any radiating source fall like (ln r)/r instead of 1/r. Then there is no radiation zone, and the radiated power grows without limit with distance. No fix placed on the light cone can cancel a ln r.
- **(ii) Separate spin channels.** Noise in the scalar channel cannot pay for the pull in the spin-2 channel; the positivity condition holds channel by channel. So spin-2 needs its own noise, and that is exactly R8-3's refereed no-go. Any scalar pull is limited by Cassini to about 5e-5 of the spin-2 pull. A trace-only kernel cannot pay for spin-2 at all, so photons would not bend (γ = −1).
- **(iii) Correlated noise.** The only way to keep the vacuum quiet is to have the quantum backaction exactly cancel the classical noise for every emission the vacuum could make. Matter then never feels the classical metric's fluctuations there; what it feels is quantum. A two-qubit check makes this concrete. Pushing decoherence below the classical floor needs a joint meter, and the joint meter entangles the two qubits. Separate local meters cannot do it, and never entangle. So this escape works by making gravity quantum where it matters.
- **(iv) Preferred frame.** This still works, with three corrections:
  - an exact least-decoherence kernel removes R8-3's regulator μ;
  - the time smearing needs power n ≥ 3, not 2, or the vacuum photon energy diverges;
  - the noise near the light cone fills the classical metric with gravitational waves of energy about ħc/(π³ℓ⁴) per unit volume, many orders above the dark-energy density.

  Suppressing that raises the vacuum photon output, and the window's lower end moves up to about 2e-7 m (order of magnitude, conditional).

---

## 1. Prior art (each counted once)

1. **R6-4** (`TESTS:3409-3418`; `C5_R6-4_referee_verdict.md:5-25`).
   - Newtonian least-decoherence floor K ≥ (4πG/ħ)|g̃|²/k²; VIABLE subwindow 4e-10 to 5e-6 m (true lower end about 1e-10 m).
   - Corollary U (no cutoff-free point particles).
   - The OSSW "32 decades" falls.
2. **R8-3** (`TESTS:3559-3573`; `C5_R8-3_referee_verdict.md:5-19`).
   - Lemma 1: a Lorentz-invariant excitation measure is zero or infinite (confirmed).
   - Lemma 3: a light-cone jump gives a ln(1/ε) (confirmed with pulses; light-cone counterterms open).
   - The repaired theorem for a common scalar or GR-normalized spin-2 F, with additive pointwise kernels.
   - The μ-regulated ansatz is non-minimal near the cone (`C5_R8-3_referee.md:219-225`).
3. **R4-4 Lemma N** (`TESTS:2935`): a classical channel generates no entanglement, so a positive BMV-type result excludes every CQ variant.
4. **Bedingham and Tumulka** (`C5_R8-3_referee_verdict.md:5`).
   - They change the dynamics (a mediating pointer field; fixed-N flashes) and do not refute Lemma 1.
   - Pearle's spacelike ("tachyonic") noise is the collapse-model analogue of variant (i) (`C5_R8-3_referee.md:51-55`). Collapse models have no drift F, so the continuity requirement used in §3 does not arise for them (reading).
5. **OWD's trace-only kernel** (`C5_R8-3_referee_verdict.md:13`; `C5_R8-3_referee.md:181-190`).
   - Also from OWD: Eq. 26 (Wheeler–DeWitt-type kernel, `OWD:604-610`); positivity "on physical, local degrees of freedom" (`OWD:617-620`); non-geometric kernels "introduce a preferred background or must be made dynamical" (`OWD:624-628`).
   - The spacetime-correlated kernels of Eq. 27, which "represent non-Markovian dynamics" (`OWD:629-648`), and OWD's LOCC no-entanglement argument (`OWD:650-655`).
6. **Repository grep** for tachyonic or spacelike-supported noise, Wiseman–Milburn, quantum-noise constraint, and Kafri. The only matches are this item's own text (`TESTS:3707-3711`, S8) and an unrelated raw prompt mentioning Kafri–Taylor–Milburn (`docs/ai_methodology/raw/prompts_session_049708ba_jonreilly.md:7444`). Neither is a derivation.

---

## 2. Tests common to all variants: what each variant must meet (`TESTS:3720-3727`)

- complete positivity at finite c;
- γ = 1 and the Shapiro delay;
- c_T and finite radiation (the light-cone log);
- a finite vacuum-excitation rate;
- decoherence and diffusion within R6-4's bounds;
- a Newtonian limit inside R6-4's window.

Under (H-T), the mean field is R8-3 §4: γ = 1, Shapiro and c_T pass whenever F(0⁻) = 1 and the spin-2 channel is GR-normalized (`C5_R8-3_report.md:181-196`, not the failing part per the referee). So the variants are decided by **positivity, radiation and the vacuum**.

---

## 3. Variant (i): spacelike-supported noise kernels — EXCLUDED in 𝒯

**Lemma S1 (spacelike support forces F = 0 on the timelike region).** Assume (H-T), and that both P_J(p) and D₀′(p) vanish for timelike p. Then F(p) = 0 for timelike p.
- *Proof.* A 2×2 positive-semidefinite matrix with zero diagonal has a zero off-diagonal entry. ∎
- [proved; checked [2]: non-PSD in 20000/20000 draws with F ≠ 0]

**Lemma 4 (R8-3; definition of G).** Newton at long range needs F(s → 0⁻) = 1, since static exchange has q⁰ = 0.

**So F jumps from 1 to 0 at s = 0.** R8-3's Lemma 3 (referee-confirmed, including pulses) gives a ln(1/ε) radiation field. The referee left one escape: a light-cone finite part (`C5_R8-3_referee.md:117-123`).

**Lemma L (the jump defeats every light-cone counterterm).** Take a monochromatic point source and F = θ(−s)·g, and define the ε → 0 limit by any Hadamard finite part. Then

  2π²·r·h(r) = −g(ω)·sin(ωr)·ln r + (terms bounded in r).

- *Proof.* Near k = ω the integrand is g(ω)·sin(kr)/(k − ω). Splitting sin(kr) = sin(ωr)cos(ur) + cos(ωr)sin(ur) with u = k − ω gives Pf∫₀¹ cos(ur)/u du = Ci(r) − γ_E − ln r, while every other piece is bounded. ∎
- **checked [1]:** A(r) + g₀ ln r = −0.28843 (constant to 5 digits) at r = 190, 1887, 18851 and 188497, with g₀ = 0.49969. For comparison, F = 1 gives the bounded (π/2)e^{iωr}.
- **Counterterms.** A counterterm supported on the cone is a finite sum of c_j δ^{(j)}(k² − ω²). Its far field is a polynomial in r times sin(ωr)/r or cos(ωr)/r, and ln r is not such a polynomial. So no light-cone-supported counterterm cancels it (proved for finite-order counterterms).
- **Consequence.** There is no radiation zone: the flux through a sphere grows as (ln r)², so the radiated power is not defined. This fails "finite radiation" (`TESTS:3723`).

**Reading for (i): EXCLUDED** within 𝒯 with Newton and the standard retarded G_R, for every spacelike-supported noise pair. It needs neither additivity nor Lemma 1.

**Outside 𝒯.** Variant (i) can keep F ≠ 0 inside the cone only by dropping (H-T) there. Then, in the Gaussian-dilation picture, the timelike channel is a noiseless coherent coupling (§5, Lemma E).

---

## 4. Variant (ii): spin-separated kernels — EXCLUDED in 𝒯

**Lemma S2 (no cross-channel payment).** The Barnes–Rivers projectors P², P⁰ are orthogonal and commute with every Lorentz-invariant kernel, so (H-T) splits by channel. If the decoherence D₀ has no spin-2 component while the drift F₂ ≠ 0, the block matrix is not positive semidefinite.
- [proved; checked [2]: 20000/20000 draws non-PSD]
- So "the scalar kernel carries the decoherence and diffusion" is **not CP** as posed.
- Adding the minimal spin-2 noise puts the model exactly in R8-3's refereed subclass: a GR-normalized spin-2 F at the light cone, which forces infinite photon-pair vacuum excitation (`C5_R8-3_referee_verdict.md:11`, "spin separation does not help", `C5_R8-3_referee.md:151-153`).

**The scalar channel's own pull (asked for in the expectation, `TESTS:3736`).**
- Static source: the contractions are P² = 2/3 and P⁰ = 1/3. GR = P² − ½P⁰ = 1/2. Photons see only P².
- An extra scalar drift c₀P⁰ changes the static G but not the bending, so

  γ = (1 − 2c₀/3)/(1 + 2c₀/3).

- Cassini, γ − 1 = (2.1 ± 2.3)e-5 (comparator, web-checked in R8-3), gives **c₀ ∈ [−5.0e-5, 1.9e-5]** at 2σ ([3]).
- The scalar channel is therefore phenomenologically almost decoupled. A scalar channel with zero drift may carry any extra noise, but it pays for nothing.

**OWD's trace-only kernel (Eq. 25 type).**
- With a trace-only D₀, (H-T) forces the traceless drift to zero, so photons are not deflected (conformally flat), giving γ = −1. That is 8.7e4 Cassini σ away ([3]).
- Otherwise the traceless metric has unbounded diffusion.
- **Excluded as a model of light bending.** This covers trace-only *payment*. OWD's trace-only D₀ as an *extra* decoherence term is harmless and irrelevant.

**Reading for (ii): EXCLUDED** within 𝒯 (refereed core: R8-3's repaired theorem). The spin-separated form as posed fails CP; the repaired form is the refereed subclass.

---

## 5. Variant (iii): non-Markovian, non-additive kernels — OPEN, with a sharpened conditional no-go

**(a) OWD's own non-Markovian class is additive.**
- In Eq. 27 (`OWD:629-640`) the Gaussian exponent is −½ΔD₀Δ − ½W̄D₂⁻¹W̄. Integrating out the classical field gives matter noise D₀ + |G|²D₂ and response G·F, with no cross term.
- [proved; checked [4]: three Gaussian integrals match exp(iΔb/a − Δ²N/2a²) to 8 digits.]
- With (H-T), this is R8-3's additive subclass, so **OWD Eq. 27 with Lorentz-invariant kernels is EXCLUDED** at golden-rule order whenever the spin-2 F is GR-normalized at the cone. The refereed theorem applies; only the containment is new here.
- OWD's hope that correlated kernels suppress "heating and diffusion" (`OWD:647-648`) does not reach the boost-orbit infinity of Lemma 1.

**(b) Beyond additivity: correlated backaction.**
- **The Wiseman–Milburn identity** for measurement plus feedback: the unconditional generator equals D[c − iF] − i[(Fc + c†F)/2, ·].
  - [checked [5]: error 5.3e-15 over 200 random draws.]
  - With c = √κ(1 + iμ)A and F = λA, the total dephasing is κ + (√κμ − λ)² at coupling g = 2√κλ.
  - Choosing λ = √κμ gives dephasing g/(2μ). At μ = 100 that is 0.005 of the AM–GM floor.
  - **[checked [5]] The floor is not a theorem without additivity.** This confirms the referee's caution (`C5_R8-3_referee.md:90-96`).
- **The cost: classicality (checked [5]).** Two qubits, with target coupling g Z₁Z₂.
  - A **joint** meter on Z₁ + Z₂ with correlated feedback: negativity 0.081 (μ = 0), 0.159 (1), 0.322 (10), 0.350 (100). The coherent limit is 0.354.
  - **Local** meters, each record fed to the other qubit (LOCC): the same Z₁Z₂ Hamiltonian coefficient, 1.000, but negativity 0 for every μ.
  - So a sub-floor total kernel between separated bodies needs a non-LOCC mediator, and that mediator entangles. This is R4-4 Lemma N in reverse: such a model is BMV-positive-capable, which is not a classical metric in the campaign's sense (reading).

**Lemma E (emission side).** Setting: stationary, Lorentz-invariant (B, J) statistics; a classical record J, so S_JJ(p) = S_JJ(−p); felt field f = B + G_R J.
1. The golden-rule vacuum rate is ∫S_ff(−p)W(p) over the future cone, where S_ff(−p) = [1, G]S(−p)[1, G]†.
2. If B and J are uncorrelated on the emission side (the additive case), then S_ff(−p) ≥ |G|²S_JJ(p).
   - (H-T) with finite S̄_BB gives S_JJ > 0 wherever F ≠ 0.
   - By continuity F ≠ 0 just inside the cone, so Lemma 1 makes the rate infinite.
   - [proved; checked [6]: 0/20000 violations.]
3. **A finite vacuum therefore forces S(−p) to be rank one with null vector [1, G]** at every timelike p where F ≠ 0. That is perfect anticorrelation, B = −G J on the emission side.
4. Then the commutator bound forces **absorption** S_ff(p) ≥ |F(p)|²/S_JJ(p) > 0. Matter states with timelike T-transfer (photon pairs, excited atoms) decay into the hidden meter.
   - [proved; checked [6]: min absorption·S_JJ/|C|² = 1.000008 over 20000 emission-silent draws.]
   - These are finite rates for given states, with no boost-orbit integral.
   - Its size has not been computed against light-by-light or metastable-state bounds.
5. In this corner, matter does not feel the classical record's noise at timelike transfers. It feels the quantum combination B + GJ: a zero-temperature quantum bath, i.e. quantum-mediated gravity there.

**Reading for (iii): OPEN.**
- *Excluded (worker reading; referee required):* Lorentz-invariant Gaussian CQ in which matter feels the record noise additively on the emission side. That covers OWD Eq. 27 and every uncorrelated non-Markovian kernel. It does **not** require pointwise additivity of the symmetrized decoherence; it requires only emission-side uncorrelatedness plus (H-T).
- *Survives:* emission-cancelled hybrids that are classical at spacelike (Newtonian, lensing) transfers and quantum-cancelled at timelike ones. No such model is constructed.
- *Still open for the surviving corner:*
  - the null cone itself: P_J(0) > 0 pumps classical GWs with a Lorentz-invariant, hence infinite, null-cone measure (R8-3 second horn, `C5_R8-3_report.md:164-168`);
  - the absorption rates;
  - BMV status.
- *Price (named, not adopted):* **P-r9a.** The gravitational field felt at timelike transfers is a quantum bath, not the record. "Records are the metric" then holds only for spacelike components.

---

## 6. Variant (iv): preferred frame — OPEN, with a computed, conditional window

1. **D₀'s excess near the null cone.** R8-3's ansatz at saturation has K/floor = x/(x+1) + (x+1)/(4x), with x = |s|/μ².
   - Values: 25.26 at x = 1e-2, 2500.25 at 1e-4, 2.5e5 at 1e-6. These reproduce the referee's numbers. Away from the cone the ratio tends to **1.25, not 1** ([7]).
   - Near the cone the excess K ≈ cμ²/(4s²) is the resonant pumping of on-shell GWs seen from the matter side. It is the same physics R8-3 bounded through μ.
2. **The exact pointwise least-decoherence kernel needs no μ.** Take D₀′ = c/(2|s|) and P_J = |s|/(2c), so K equals the floor exactly.
   - P_J(0) = 0, so there is no linear-in-time pumping. What remains near the cone is logarithmic.
   - Matter transitions at exactly null transfer then pick up ln(ωT). For a 10 eV atomic dipole line the rate is about 1e-27 s⁻¹ before the log (suggested arithmetic, not in `.out`), which is harmless.
3. **Correction to R8-3 §5.** With K at the floor and Maxwell W ∝ s², the vacuum energy injection ∫p⁰KW grows as ω^{3−2n}.
   - n = 2 diverges logarithmically: [7] gives 7.86, 20.59, 33.41, 44.10 at cutoffs 1e1 to 1e4.
   - n = 3 converges to 0.6741.
   - **R8-3's "n ≥ 2" (`C5_R8-3_report.md:201`) must read n ≥ 3.** The R8-3 scaling ħc²ℓ_P²/ℓ⁷ holds only for n ≥ 3. [proved; checked]
4. **Near-cone classical-GW content (suggested; O(1) normalization).** With P_J = ε|s|/(2c) near the cone and a frame cutoff at k ~ 1/ℓ:
   - ρ_GW ≈ ε·L·ħc/(π³ℓ⁴), with L a logarithm of order 10.
   - At ε = 1 this is 1.2e15 ρ_crit at ℓ = 1e-8 m and 1.9e4 ρ_crit at 5e-6 m ([7]).
   - This content is propagating classical radiation, so it gravitates (Isaacson; a reading, the same kind of premise as R6-4's H-cosmo, which the referee did not accept as proved, `C5_R6-4_referee_verdict.md:17`).
   - If so, it needs ε ≲ 6e-16 to 4e-5.
   - Suppressing P_J broadband near the cone raises D₀ there by 1/ε, and so raises R8-3's vacuum photon injection by 1/ε. The EBL lower end then scales as ε^{−1/7}.
   - **Solved jointly, the conditional lower end is about 1.5e-7 m (A′ = 1e-4), 2.3e-7 m (A′ = 1e-2), 3.4e-7 m (A′ = 1)** ([7]).
   - The upper end stays R6-4's 5e-6 m.
   - The suppression is applied only where ω ≳ |k|, so the ω → 0 Newtonian kernel, and with it R6-4's laboratory table, is unchanged (reading).
5. **The remaining tests.**
   - γ, Shapiro and c_T pass as in R8-3.
   - GW emission at 100–1000 Hz is unaffected (R8-3 [6]).
   - Cs-133 (70 s), LPF as a γ = 1 prediction, and the corrected torsion formula σ_a² = (48π/5)G²D₂/(RT): all are ω → 0 statements, so R6-4's margins carry over (reading).
   - CP: suggested only, via a pointer-field dilation (as R8-3).
   - The dynamical frame field and its PPN α₁/α₂ checks are not built.

**Reading for (iv): OPEN.**
- The search target is narrowed, conditionally, to about [2e-7, 5e-6] m.
- Unconditionally, it remains R8-3's [1e-8, 5e-6] m with n ≥ 3.
- **Prices (named):** R8-3's P-r1 to P-r5. P-r5 (μ) is replaced by **P-r9b**: a near-cone noise suppression ε(ℓ), with its 1/ε decoherence excess near the cone.

---

## 7. Strong words checked

- "EXCLUDED" for (i) and (ii) means within 𝒯: (H-T), Lorentz invariance, Gaussian, the standard retarded massless G_R, and Newton. Golden-rule order is used only where the R8-3 theorem is invoked.
- "Every counterterm" in Lemma L means a finite-order distribution supported on the cone.
- (H-T) for non-Markovian kernels rests on the Gaussian-dilation derivation (no reverse gain; a self-commuting record). OWD/Layton CP for general history functionals is not proved here to imply (H-T).
- Lemma E's hypotheses are a stationary Lorentz-invariant meter, a classical J, and finite S̄_BB. Infinite S̄_BB is not treated.
- All of §6 items 4–5 is suggested and order-of-magnitude.
- A′ is still R8-3's bracket. "Gravitates" is a reading.
- The two-qubit checks are illustrations of the mechanism, not a field-theory proof.

## 8. What would decide it

1. **A referee of Lemmas S1, L, S2 and E**, and of the Gaussian-dilation derivation of (H-T) for colored kernels.
2. **For (iii):** an explicit emission-cancelled hybrid. Compute its null-cone pumping, its absorption rates against light-by-light and metastable-state bounds, and its BMV prediction.
3. **For (iv):**
   - the dynamical frame field;
   - A′ from the Maxwell ⟨TT⟩ coefficient;
   - an honest Isaacson/backreaction treatment of the near-cone classical-GW content, which decides whether the [2e-7, 5e-6] m narrowing is real.

**Sources.**
- Web-checked this run: Clerk, Devoret, Girvin, Marquardt, Schoelkopf, [arXiv:0810.4729](https://ar5iv.labs.arxiv.org/html/0810.4729), Eq. (90). A search confirming Markovian scope only for the CQ trade-off literature: [arXiv:2307.02557](https://arxiv.org/html/2307.02557v1).
- Local text: OWD 2302.07283; Layton et al. 2307.02557.
- Via R8-3 or R6-4: Cassini; GW170817; the EBL.
- RECALLED: Isaacson; ρ_Λ = 5.9e-10 J/m³; ρ_crit = 8.5e-10 J/m³.
