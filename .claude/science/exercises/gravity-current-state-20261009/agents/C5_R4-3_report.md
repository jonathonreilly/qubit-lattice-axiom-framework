# C5 R4-3: observational size of LRL per-realization Lorentz violation and Bragg resonances

**Worker.** Claude Opus 5.5 (probe R4-3), the same model family as R2-2, R3-1, R3-3 and the supervisor. **Not refereed.** Run 2026-10-12, 13:09Z to about 13:45Z. No repository file was edited.

**Scratch.** `scratchpad/C5/R4-3/`: this report, plus `scripts/`:
- `r43_moment_lv.py` → `.out`: per-shell LV, moment-conditioned shell combinations, LV-minimising weights, out-of-sample check;
- `r43_moment_lv2_compute.py` → `.out` and `r43_S_arrays.npz`: the same 12 shells, adding κ = 0.035, with the arrays saved;
- `r43_moment_lv2_analyse.py` → `.out`: empirical shell densities, sign test, pattern correlations;
- `r43_tube_zero.py` → `.out`: bisection for zeros of the symbol in the forward tube;
- `r43_zero_robust.py` → `.out`: how far errors in the shell densities can move those zeros;
- `r43_obs_table.py` → `.out`: arithmetic in physical units, the in-band margins and conditional bound tables.

**Read in full.** `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS.md:2302-2851`, i.e. the C5 method, rounds 1–3, their results, and round 4 (R4-3 is at `:2815-2825`); `agents/C5_R3-1_report.md` and every script and `.out` in `scripts/C5/R3-1`; `agents/C5_R3-3_report.md`; `scratchpad/C5/R2-2/R2-2_report.md` (§§4–7); `ref_R2-2/REFEREE_VERDICT.md` and `R2-2_referee.md:150-200`; `RZ_referee.md`.

**Read in part.**
- `C5_O5_synthesis.md`: §0, the F1 block, `:100-135`.
- `SUMMARY.md` §§15–22.
- `PRICE_NOTE.md`: v6 delta headers only.
- `C5_O1_report.md:33-62`.
- `C5_O1_referee.md:70-90`.
- The RL1 report and referee, for stability prior art.

The R3-1 referee was still running (`ref_R3-1/runner.out` was empty). R3-1's numbers are therefore treated as worker claims. The ones used here are rechecked in §5.

**Labels.**
- *proved*: a complete argument written here (same family, unrefereed).
- *proved mod RECALLED*: complete except for a named standard theorem.
- *checked*: a computation in the scratch files.
- *suggested*: argued only.
- *reading*: an interpretation.
- *comparator*: an outside bound or result, either web-checked (W) or from memory (M).

---

## 0. In plain words

- **The plain question.** On the Lorentz-random lattice (LRL), each copy of the universe is a crystal with a discrete set of boosts. Do its copy-specific direction effects, and its Bragg resonances, show up in gamma-ray-burst timing, cosmic-ray thresholds, polarization twisting, or atomic clocks?
- **What can be said without the missing law:**
  - **At the Planck spacing, every observed collision sits far below the crystal's "Bragg gap".** The margin is 27–44 decades in the collision's invariant mass², so direct one-to-one Bragg scattering is exactly absent (kinematics; the gap itself is refereed). At 10⁻¹⁹ m spacing, LHC collisions and the highest-energy cosmic-ray air showers are above the gap.
  - **Massless particles cannot carry smooth copy-specific direction effects at all.** The crystal's boost group scrambles every light-like and space-like momentum densely. Any smooth function of such a momentum that respects the crystal's symmetry is therefore a function of p² alone, i.e. Lorentz-invariant. So, if light has a regular dispersion law in each copy, there is exactly no energy-dependent arrival delay, no birefringence and no photon decay from this source (proved mod RECALLED).
  - **Massive particles can carry such effects**, but only as a mass that depends slightly and periodically on the particle's velocity relative to the crystal. That mass stays bounded, so the effect does not grow with energy. Cosmic-ray and TeV thresholds are insensitive to it. Atomic clocks and comagnetometers are the sensitive tests: about 10⁻²⁹ of the mass for neutrons and about 10⁻²¹ for electrons (mapping suggested).
- **What breaks.** The only explicit per-copy laws available are kernels built from a few hyperbolic shells, tuned so that their average is a wave operator. In those laws the copy-specific part does not shrink at long wavelength. It grows relative to the wave operator, roughly as (wavelength/a)^{2.3–3.2} in the forward tube (checked).
  - Its sign also varies, so the law's symbol has zeros in the forward tube. Those are exponentially growing modes with an e-folding time of about 2 lattice times (checked, robust to the density inputs).
  - So these laws are unstable at the Planck rate. They are not merely Lorentz-violating.
  - Trying hard to cancel the effect with 12 shells reduces it about 100-fold, but it still exceeds the wave operator at long wavelength, out of sample (checked).
- **What might work (suggested, unchecked).** Kernels smeared over a mesoscale ℓ_k ≫ a in proper time might suppress the copy-specific long-wavelength term faster than any power of a/ℓ_k (the Bragg gap, or cusp-form, argument). Because that term grows at long wavelength, surviving a Hubble time without an instability needs its coefficient below about 10⁻¹⁸³ at a = ℓ_P. That would require ℓ_k of roughly 420a/c, where c is the unknown suppression constant.
- **Reading: INCONCLUSIVE.** No bound is shown to be violated at a = ℓ_P by a law that exists. The only explicit laws fail on stability first, which is a theory-level failure, not an observational one. Every remaining estimate needs the unbuilt effective law, and the FIXED reading sends that case to INCONCLUSIVE (`TESTS.md:2825`).

---

## 1. Against the FIXED readings (`TESTS.md:2822-2825`)

| Reading | Status |
|---|---|
| **PASS**: "every effect is below current bounds at a = ℓ_P with no tuning" | **Not met.** Pieces that pass:<br>• the in-band kinematic margin (§3.1);<br>• the regular massless sector, where time-of-flight (ToF), birefringence and the photon-decay and vacuum-Cherenkov κ̃ terms are exactly zero by symmetry (§3.2);<br>• threshold insensitivity of the massive sector (§3.3).<br>But the massive automorphic amplitude, the Bragg-cone singular sector, and the existence of a stable per-realization law are not established. The one explicit class is unstable (§4.1), and the escape needs a hierarchy ℓ_k/a ≳ 10²–10³ that is unchecked (§4.2) |
| **FAIL**: "a bound is violated at a = ℓ_P" | **Not met.**<br>• Naive transfers of R3-1's tube numbers would violate LHAASO photon decay by ~10³ and birefringence by ~5e13. But §3.2 shows that transfer is invalid for massless species.<br>• For neutrons the naive transfer exceeds Hughes–Drever by ~2e7. That is a transfer, not a computed law, so it is suggested only.<br>• The finite-shell laws fail by instability, not by an observational bound |
| **INCONCLUSIVE**: otherwise, "including when an estimate needs the unbuilt effective law" | **Returned** |

**Against the round-4 framing** (`TESTS.md:2792-2793`: "How large are the per-realization anisotropy and the Bragg-resonance effects at physical energies?"):
- Bragg: zero for 1→1 in band (refereed narrow form). The singular cones' size is unbuilt.
- Anisotropy: zero for regular massless dispersions (proved mod RECALLED). Massive amplitude unbuilt.
- New: the explicit finite-shell laws are unstable (checked).

---

## 2. Setting, hypotheses, scope (stated before titles)

- **(S1) The process.** One realization X = g(L₇ + u), with L₇ = diag(√7,1,1,1)ℤ⁴. Exact symmetry Γ_L ⋉ L₇, where Γ_L = SO⁺(Q₇,ℤ) is cocompact (refereed, `ref_R2-2/REFEREE_VERDICT.md:9`).
  - The Bragg gap is |G²| ≥ (2π)²/(7a²) on the reciprocal lattice, with no null G (refereed, `:11-16`).
- **(S2) Per-realization laws.** These are Γ_L ⋉ L₇-invariant (R3-1 S3, `C5_R3-1_report.md:48-51`). The explicit ones are retarded orbit sums that converge in the forward tube (R3-1 Prop. R, `:117-128`).
- **(S3) Regular in-band effective dispersion.** For §3.2–3.3 only, assume this hypothesis (H_reg): the in-band on-shell structure of each species is described by a Γ_L-invariant function Φ_s(p), continuous on a Γ_L-invariant region containing the punctured null cone, with on-shell set {Φ_s = 0}.
  - R3-1's Lemma M forbids this as a function on the momentum *torus* (`:75-86`). H_reg is therefore a hypothesis about the **unbuilt effective law**, not about the lattice symbol.
- **(S4) Observational inputs** (refereed in the packet unless marked):
  - LHAASO GRB 221009A: E_QG,1 > 10 E_Pl and E_QG,2 > 6e-8 E_Pl;
  - LHAASO 1.4 PeV photon survival: c_γ − c_e < 2.66e-19;
  - LHAASO superluminal decay: E_LV,1 ≳ 1e5 E_Pl;
  - Auger/HESS: 6e-20, iron-based and indicative;
  - Ne-Rb-K neutron c_jk ~ 1e-29;
  - GW170817 (`C5_O1_report.md:41-49`; `C5_O1_referee.md:76-86`).

  Web-checked comparators (W, this run):
  - GRB 140206A polarization, ξ < 1e-16 (Götz et al. 2014);
  - Yb⁺ clock electron c_jk ~ 1e-21 (Sanner et al., Nature 567, 204 (2019); improved by Dreissen et al. 2022).

  From memory (M): optical-cavity isotropy of c at about 1e-18; the Fermi GRB 090510 linear bound of order E_Pl.
- **Outside scope:**
  - laws covariant only in law;
  - continuum fields coupled to the point set (RL-type; there k → k − G is a real transition);
  - curved spacetime (R3-3);
  - gauge structure (no lattice photon law on LRL exists);
  - gravity.

---

## 3. Law-independent results

### 3.1 In-band kinematic margins (checked arithmetic on refereed kinematics; `r43_obs_table.out:3-24`)

In-band means every pair invariant of the process lies below |G²|min = 5.64/a² (R2-2 §4.2; narrow refereed form, `R2-2_referee.md:151-164`).

| Process | a = ℓ_P: log₁₀(gap/s) | a = 1e-19 m: log₁₀(gap/s) |
|---|---|---|
| 1.4 PeV γ × CMB | 44.2 | 12.6 |
| 13 TeV GRB γ × EBL | 43.2 | 11.6 |
| GZK p × CMB (1e20 eV) | 38.8 | 7.2 |
| 3e20 eV primary × air nucleon | 27.2 | **−4.4 (out of band)** |
| LHC pp, √s = 13.6 TeV | 30.7 | **−0.9 (out of band)** |
| 1.4 PeV γ × detector nucleon | 32.5 | 0.9 |

**At a = ℓ_P** every observed process is ≥ 27 decades inside the gap.
- Ideal 1→1 (and 0→2) in-band Bragg mixing is exactly absent (refereed narrow form).
- The far-umklapp channels k → k − G need |G|_E ≳ |G²|/(4ω), i.e. trans-Planckian partners (R2-2 `:179-181`; R3-3 `:135`).
- For a massive particle at rest, the Bragg resonance shell sits at |G|_E ≈ |G²|/(2m) ≈ 3.7e19 E_Pl for a nucleon and 6.7e22 E_Pl for an electron (`r43_obs_table.out:11-12`).
- For lattice fields these are not transitions; they are singular cones of the symbol (R3-1 `:216-219`). Their observable size is law-dependent (§4.4).

**At a = 1e-19 m** LHC collisions (√s > 4.69 TeV) and UHECR air showers are out of band, so umklapp channels are kinematically open there.
- Their size is law-dependent.
- Reading: this sits at or beyond the collider bar that X1 recorded as unrefereed (≈ 4e-20 m, `SUMMARY.md:492`). So a = 1e-19 m is at best marginal on collider grounds alone.

### 3.2 Lemma Z: null and spacelike rigidity (proved mod RECALLED)

**Statement.** Let Φ be a continuous Γ_L-invariant function on Ω = {p ∈ ℝ⁴ ∖ 0 : p² ≥ 0} (the spacelike vectors plus the punctured null cone). Then Φ(p) depends on p² alone. For measurable Φ the same holds almost everywhere.

**Proof.**
1. *Null cone.* C⁺ ∖ 0 ≅ G/MN, with N the horospherical subgroup, G = SO⁺(1,3) and Γ_L cocompact. N-orbits on Γ\G are dense: minimality of horospherical flows on compact quotients (Hedlund for SL₂; Veech and Dani in general; RECALLED). Hence every Γ_L-orbit in G/N, and so in G/MN, is dense. A continuous invariant function is constant on a dense set, hence constant on C⁺. The same holds on C⁻.
2. *Each spacelike hyperboloid* p² = μ² > 0 is ≅ G/SO(1,2). By Ratner's orbit-closure theorem (Shah for SO(1,2) ⊂ SO(1,3); RECALLED), every SO(1,2)-orbit closure in Γ\G is either closed (countably many) or all of Γ\G. So a dense set of points of the hyperboloid have dense Γ_L-orbits, and continuity again gives a constant.
3. *Measurable version.* Moore's ergodicity theorem, since MN and SO(1,2) are non-compact (RECALLED). □

**Prior art (count once).** R3-3 noted that measurable Γ_L-invariant functions of a null *direction* are a.e. constant, and that "the leading on-shell anisotropy may vanish" (suggested, `C5_R3-3_report.md:173`). New here:
- the momentum version (direction and scale);
- the spacelike hyperboloids;
- the dispersion consequences below.

**Consequences under H_reg (proved, given H_reg and Lemma Z).**
- **(Z1) The massless sector.** On Ω, every species' on-shell set is a union of whole level sets {p² = const}. A massless branch is exactly the light cone. A superluminal branch can only be a full tachyonic hyperboloid, which is Lorentz-invariant.
  - So the regular sector has no ToF delay of any order, no energy-dependent phase, and no helicity splitting.
  - It also has no isotropic κ̃_tr: that would need a non-cone branch on Ω.
  - Hence GRB 221009A ToF, GRB polarization (ξ), LHAASO photon survival and superluminal decay, Auger/HESS vacuum Cherenkov via κ̃_tr, and cavity isotropy all receive **exactly zero** contribution from the regular per-realization LV. The same holds for gravitons and GW170817's c_T, given the same hypothesis for the graviton.
- **(Z2) Correction to the R3-3 arithmetic note.** A per-realization dispersion term (aω)^δ (`C5_R3-3_report.md:171-172, 337-340`) cannot enter a regular massless dispersion at any δ. The 5e4 rad example is therefore excluded by symmetry under H_reg, not by data.
- **(Z3) Where LV can live, in the subluminal timelike region.** On timelike hyperboloids Γ_L\H³ is compact, and Φ can be any automorphic function there.
  - A near-massless species can only carry an automorphic mass-like deformation: on-shell p² = −m²(v) with v ∈ Γ_L\H³.
  - Its effect in a lab frame is ω ≈ |k| + m(v)²/(2|k|), which falls with energy. It is bounded by photon-mass limits (M: ~1e-18 eV), not by LIV ToF bounds.
- **(Z4) Outside H_reg.** For an actual lattice field, R3-1's Lemma M says the symbol has no regular version. Any physical photon LV must then sit in the **singular** sector: boundary values on the Bragg cones (R3-1 §4.2, §4.4). Lemma Z says nothing about its size.

### 3.3 Massive species: bounded automorphic mass, no high-energy amplification (proved arithmetic under H_reg; mapping suggested)

- Write m_s(v) = m_s(1 + ε_s ψ_s(v)), with ψ_s continuous on the compact Γ_L\H³, so bounded (proved).
- **Maximal attainable speed.** Group-velocity corrections are O(ε_s m²/E²) → 0, so every species' maximal attainable speed is exactly c (suggested arithmetic).
- **Thresholds.**
  - GZK, γγ → e⁺e⁻ (TeV transparency) and γ → e⁺e⁻ shift only by a relative O(ε_s).
  - The photon branch is the cone (Z1), so γ → e⁺e⁻ stays forbidden.
  - **UHECR and TeV-γ thresholds are insensitive** to the regular sector at any ε_s ≪ 1. This contrasts with preferred-frame LV, which enters as E²δc.
- **Velocity-lowering emission.** e(v) → e(v′) + γ is kinematically allowed whenever m(v′) < m(v), with no threshold (proved kinematics: m(v)² − m(v′)² = −2p′·k ≥ 0).
  - The photon energy in the electron frame is ~ ε_e m_e. The rate is about α ε_e m_e/ħ (suggested), e.g. ~1e-6 s⁻¹ at ε_e ~ 1e-24.
  - That is observationally negligible unless ε_e is far larger than the clock bound allows.
- **Clock and Hughes–Drever mapping (suggested).** Expanding ψ about the lab velocity gives δE ⊃ ε_s ∂_i∂_jψ p_i p_j/(2m), i.e. SME c_jk ≈ −(ε_s/2)(∂∂ψ)_traceless. So:
  - ε_n |∂∂ψ_n| ≲ 1e-29 (Ne-Rb-K comagnetometer, refereed number; projection factors not computed);
  - ε_e |∂∂ψ_e| ≲ 1e-21 (Yb⁺ clocks, W comparator).
- **Natural size of ε_s.** Not determinable without the law (§4).

---

## 4. Law-dependent results: the explicit kernels, the escape, conditional numbers

### 4.1 Finite-shell d'Alembertian kernels are dominated by per-realization LV and are unstable (checked)

**Object.**
- S_N(u, κ) = Σ_{x ∈ L₇, x² = N, x₀ > 0} e^{−κ w(u,x)}: the single-shell symbol at p = iκu in the forward tube (R3-1 §4.3).
- The exact Lorentz-invariant (LI) part is ν_N·4πK₁(κτ_N)/(κτ_N).
- Weights w_N impose four LI moment conditions, which kill 1/κ², ln κ, the constant and κ² ln κ, plus a normalization. The LI part of Σ w_N S_N is then (π/4)κ² + O(κ⁴ ln κ): a d'Alembertian. This is the LRL analogue of R3-3's four conditions (`C5_R3-3_report.md:111`).

**Set-up.**
- Shells N = −1…−12, with n₀ ≤ 520. The truncation margin is ≥ 24 e-folds at κ = 0.035 and ≥ 270 at κ ≥ 0.4.
- 32 directions of rapidity ≤ 0.7, and κ from 0.8 to 0.035.
- The ν_N come from the small-κ direction mean. They agree with R3-1's counting estimator to ≤ 0.8% (`r43_moment_lv2_analyse.out:1-13`).

**Results** (`r43_moment_lv2_analyse.out`):

| Weights | rel LV = std_u/LI at κ = 0.2 / 0.1 / 0.05 / 0.035 | log-slope of rel LV (κ ≤ 0.2) | Directions with a sign change |
|---|---|---|---|
| 5 shells {−1,−2,−3,−5,−7} | 90 / 1.1e3 / 4.0e3 / 1.5e4 | −2.78 | 32/32 |
| 5 shells {−2,−3,−5,−6,−7} | 1.0e3 / 1.2e4 / 3.1e4 / 3.1e5 | −3.20 | 32/32 |
| 5 shells {−3,−5,−7,−10,−11} | 3.3e2 / 3.3e3 / 5.2e3 / 7.4e4 | −2.98 | 32/32 |
| 5 shells {−1,−4,−6,−9,−12} | 55 / 3.7e2 / 9.2e2 / 2.8e3 | −2.27 | 32/32 |
| min-norm over all 12 shells | 28 / 2.6e2 / 2.3e2 / 4.7e3 | −2.69 | 32/32 |
| LV-minimising over 12 shells (in sample) | 1.9 / 6.3 / 2.2 / 8.6 | −0.55 | 32/32 |
| LV-minimising, fitted on κ ≥ 0.1 only | 0.14 / 0.60 / **51 / 305** (test) | −4.70 | 13/32 |

The v1 run gives the out-of-sample check (16 fresh directions) for the in-sample LV-minimising weights: rel LV 0.29 / 3.6 / 2.5 at κ = 0.4 / 0.1 / 0.05 (`r43_moment_lv.out`, end).

**Per-shell absolute LV.** κ·std_u(S_N) stays between 2e-4 and 5e-2, oscillating, over κ = 0.8 → 0.035 for every shell (`r43_moment_lv2_analyse.out`, "per-shell" block). So absolute LV goes as ~1/κ (log-periodic), and against a κ² d'Alembertian the relative LV goes as ~κ^{−3}. The fitted slopes are −2.3 to −3.2.
- This reproduces R3-1's single-shell scaling (§5) and the spectral reading of `C5_R3-1_report.md:189-194`.
- It **confirms (checked) R3-1's open suggestion** "that the 1/κ absolute growth survives the Lorentz-invariant moment conditions" (`:291`).

**Zeros in the forward tube, i.e. instability.**
- K̂(iκu) is real and continuous in κ, so a sign change implies a zero κ* by the intermediate value theorem.
- A zero at p* = iκ*u with κ*u ∈ V₊ gives the homogeneous solution e^{ip*·x} = e^{−κ* u·x}. It grows toward the future at rate κ*/a.
- This is the same stability criterion as for causal-set d'Alembertians: RL1 found the BD retarded inverse unstable (`C4_RL1_report.md:23,108`; referee agreement with Aslanbeigi–Saravani–Sorkin, `C4_RL1_referee.md:9-14`). Count once.
- Bisection for the {−1,−2,−3,−5,−7} kernel (`r43_tube_zero.out`) gives κ* = 0.499, 0.501, 0.488, 0.456 (first zeros) and 0.177, 0.180, 0.177, 0.165 (second zeros) in four directions. The e-folding time is **≈ 2 lattice times** (2 t_P at a = ℓ_P).
- **Robustness** (`r43_zero_robust.out`).
  - A density error |δν/ν| ≤ 1e-3 shifts K by ≤ 0.87 at κ = 0.584 and ≤ 1.82 at κ = 0.438. The bracketing values are |K| = 6.9 at both points, so the first zero is robust.
  - The second zero is robust only if |δν/ν| ≲ 5e-4. The empirical ν are expected to be good to ~3e-4, so that holds, but it is not shown.
- The truncation error is negligible at κ ≥ 0.4.

**Reading.** In the forward tube, every tested finite-shell, moment-conditioned per-realization LRL kernel:
- has its automorphic (Γ_L-periodic) part dominating its d'Alembertian at every κ ≲ 0.5/a;
- has forward-tube zeros, i.e. Planck-rate growing modes.

Checked for the listed weights only. It is not a class theorem.

**Why the LV-minimising attempt cannot win (suggested).** Each tempered automorphic eigenvalue contributes a term ∝ κ^{−1±ir_j}ψ_j(u)·Σ_N w_N c_{N,j}τ_N^{−1∓ir_j} (spectral reading, RECALLED Selberg/Harish-Chandra transform). Cancelling it at all κ costs two real conditions per eigenfunction, and Weyl's law gives infinitely many eigenfunctions. Twelve shells minus five constraints leave seven parameters. The fit removes the dominant pattern (×~100 in absolute LV) but not the rest out of sample.

### 4.2 The general mechanism and the escape (suggested)

**Mechanism.**
- Suppose the residual automorphic coefficient is ε_B ≠ 0. On the compact quotient this term has zero mean, so it is negative in some directions.
- Along those directions K̂ ≈ (π/4)κ² − |ε_B|/κ changes sign at κ* ≈ (4|ε_B|/π)^{1/3}. **Any** nonzero residual therefore gives a forward-tube zero, i.e. an instability at rate ≈ κ*/a.
- Required for no growth within a Hubble time: ε_B ≲ (π/4)(H₀a)³ ≈ **1.3e-183** at a = ℓ_P, and ≈ 3e-136 at a = 1e-19 m (arithmetic, `r43_obs_table.out`, last two lines).
- Keeping relative LV below 1e-18 down to κ = 1 m⁻¹ needs ε_B < 3.3e-123 at a = ℓ_P. That is weaker than the stability requirement.

**Escape (suggested, unchecked).** Use smooth kernels with weights f(τ²) supported away from τ = 0 and varying on a proper-time mesoscale ℓ_k ≫ a. Two arguments say the automorphic coefficients are then suppressed faster than any power:
- (i) Poisson summation plus the Bragg gap (R3-1's suggestion, `:198`);
- (ii) the generating functions Σ_N c_{N,j}q^N of the shell periods are theta lifts with no constant term (cusp-type; RECALLED theta correspondence). Smooth bump sums of their coefficients decay faster than any power of ℓ_k², with an exp(−c·ℓ_k/a) form plausible.

If the suppression is exp(−c ℓ_k/a), stability over a Hubble time needs ℓ_k ≳ 421a/c at a = ℓ_P (312a/c at a = 1e-19 m). With c ~ 2π/√7 that is about 180 ℓ_P. That is a hierarchy, not a fine tuning, but:
- R3-1's runs reached only Δτ ≈ 1, where no clean suppression is seen (`r31_multishell2.out:2-5`);
- mine reached shells up to τ = √12;
- so the ℓ_k ≫ a regime is **untested**.

### 4.3 Conditional numbers in physical units (`r43_obs_table.out`, part 3)

Parametrize δv/c = ε(Ea)^n A(direction). The largest ε each bound allows at a = ℓ_P:

| Bound (at energy) | n = +1 | n = +2 | n = −3 |
|---|---|---|---|
| GRB 221009A ToF, linear (13 TeV) | 0.10 | 9e13 | 1.3e-61 |
| 1.4 PeV γ survival | 2.3e-6 | 2e7 | 4e-58 |
| LHAASO superluminal decay | 1e-5 | 1.2e8 | 4.5e-58 |
| GRB polarization ξ < 1e-16 (W) | 2e-16 | 8e6 | 7e-107 |
| Neutron Hughes–Drever c_jk 1e-29 | 4.9e-10 | 2.4e10 | 8.6e-89 |
| Electron clock c_jk 1e-21 (W) | 2.4e3 | 6e27 | 6.9e-95 |
| Cavity isotropy 1e-18 (M) | 1.2e10 | 1.5e38 | 5.5e-103 |

**Naive n = +1 transfer** of R3-1's single-shell tube numbers (ε ≈ C·τ ≈ 1e-2; `r31_lv_scaling.out:16,33`):
- It would pass ToF by ×10 (a 0.64 s delay at 13 TeV).
- It would violate photon survival by 4e3, superluminal decay by 1e3, birefringence by 5e13 and neutron Hughes–Drever by 2e7.
- **This transfer is invalid for photons** (Lemma Z: no regular null LV), and it is unbacked for nucleons (the finite-shell laws it comes from are unstable, §4.1).
- It is reported only to show what the ν and tube numbers would mean if transferred. These are not results.

**At a = 1e-19 m** every row is violated by the naive transfer, by 1e3 to 1e29, and the n = −3 requirements are 1e-11 to 1e-59. Together with §3.1, a = 1e-19 m is disfavoured on every count shown (suggested).

### 4.4 Bragg-cone singular sector (not computed; needs the law)

- For real momenta the per-realization symbol is a boundary value with singular cones (p − G)² = 0 accumulating at p = 0. For null k the resonance count grows ∝ T/ω per dyadic shell (R3-1 `:206-213`, not rechecked here beyond reading the script and its output).
- Their strength is set by the kernel's singular moments C₁, C₂, …. By Müntz–Szász, finitely many conditions leave logarithmic terms (R3-1 `:164-166`).
- Lemma Z puts every observable massless LV in this sector. Its size for photons (phase noise, dispersion, birefringence) needs an explicit stable law, which does not exist (§4.1). **Not computed.**

---

## 5. Rechecks of R3-1 numbers used, and one correction

**Single-shell LV reproduced.** My shells, with 32 different directions and n₀ ≤ 520, give the following (`r43_moment_lv.out:2-13`):
- N = −3: relative LV 6.3e-3 at κ = 0.8, and κ·std of 4e-3 to 1.4e-2 over κ = 0.8 → 0.035;
- N = −7: 2.4e-2 at κ = 0.8.

R3-1 has 8.8e-3 and 3.5e-2 with κ·std of 1e-3 to 2e-2. They agree within the direction-sample variation. The densities agree too: ν(−3) = 0.3746 (empirical) against R3-1's 0.3759.

**Correction (checked).** R3-1 states "pairwise pattern correlations are −0.01 to −0.04" (`C5_R3-1_report.md:196`). The script prints the **mean** pairwise correlation (`r31_multishell.py`; `r31_multishell.out:27-29`).
- The individual correlations are mostly |c| > 0.9: at κ = 0.1, 55 of the 66 pairs among shells −1…−12.
- Eight pairs hold |c| > 0.9 at every κ (`r43_moment_lv2_analyse.out`, final blocks).
- So over rapidity ≤ 0.7 the LV is dominated by **one common direction pattern**, with shell- and κ-dependent log-periodic sign. A single low automorphic eigenfunction is suggested.
- R3-1's ×0.028 suppression of the equal-weight 24-shell sum at κ = 0.05 is therefore sign cancellation of a common pattern, not averaging of independent ones. It does not persist: the same table gives ×0.21 at κ = 0.2 and ×0.11 at κ = 0.1.

---

## 6. Prior art (counted once)

- **R3-1:** Lemma M, Prop. R, the tube LV scaling, resonance counts.
- **R3-3:** null-direction ergodicity remark `:173`; four moment conditions `:111`; the (aω)^δ example `:171-172`.
- **R2-2 and its referee:** the gap, the narrow Bloch silence, the open per-realization O1 bounds (`R2-2_referee.md:179-189`).
- **RL1 and its referee:** retarded-operator instability, Aslanbeigi–Saravani–Sorkin.
- **O1 and its referee:** the bound numbers.
- **X1:** the collider bar (`SUMMARY.md:492`).
- **No repository hits** for "Ratner", "horospherical" or "Hedlund" (grep not exhaustive across `docs/`). Lemma Z's momentum and spacelike form is new here as far as checked.

---

## 7. Scope, hypotheses, strong words

**Proved:**
- the §3.1 kinematics (given the refereed gap);
- the §3.3 boundedness and emission kinematics;
- Lemma Z mod RECALLED (horospherical minimality, Ratner/Shah, Moore);
- Z1–Z3 given H_reg.

**Checked:**
- the §4.1 tables, zeros and robustness;
- the §5 rechecks and the correlation correction.

**Suggested:**
- the §3.3 c_jk mapping and emission rate;
- the §4.1 spectral reading;
- all of §4.2 (the mechanism for general kernels, and the mesoscale escape);
- the a = 1e-19 m disfavouring.

**Excluded realizations:**
- laws without exact per-realization Γ_L covariance;
- RL-type continuum couplings;
- curved LRL;
- defect sectors;
- any explicit gauge or photon law;
- other arithmetic forms than L₇;
- kernels with unbounded shell support, except through the §4.2 suggestion.

**Strong words.**
- "Exactly zero" is used only for (a) ideal in-band 1→1 Bragg mixing (refereed narrow form) and (b) regular massless LV under H_reg (Lemma Z).
- "Unstable" is used only for the checked weight sets, by the forward-tube-zero criterion. It is not used for the LRL class.

---

## 8. Price implications (named, none adopted)

- **For candidate E′/B′ (LRL)**, beyond R3-1 §8:
  - (i) A per-realization law must be stable. Finite-shell retarded kernels with LI moment conditions are not (checked instances). A **mesoscale kernel** with ℓ_k ≳ 10²–10³ a/c is then needed, i.e. a non-locality hierarchy in the Admissibility rule, plus a proof that the automorphic IR coefficients are suppressed to ≲ 1e-183.
  - (ii) Under any regular effective law, LRL's observable LV is confined to massive species as a bounded velocity-periodic mass (clock/comagnetometer bar ~1e-29). For massless species it lives in the singular Bragg-cone sector.
- **Good news, conditional on H_reg:** the high-energy LIV bounds (GRB ToF, polarization, LHAASO, UHECR thresholds) are satisfied by symmetry, not by tuning.

## 9. Needs codex referee

- Lemma Z (the density inputs, and its use on dispersion surfaces).
- The §4.1 instability claim and its robustness, i.e. the tube-zero criterion for these retarded lattice laws.
- The §5 correction to R3-1's correlation statement.
- The suggestion in §4.2 that any nonzero automorphic IR coefficient gives a forward-tube zero.

**Sources (web, this run):**
- [Götz et al., GRB 140206A (arXiv:1408.4121)](https://ar5iv.arxiv.org/html/1408.4121)
- [Götz et al., GRB 061122 (arXiv:1303.4186)](https://arxiv.org/pdf/1303.4186)
- [Sanner et al., optical clock comparison for Lorentz symmetry testing (arXiv:1809.10742)](https://arxiv.org/abs/1809.10742v1)
- [PTB/ScienceDaily summary](https://www.sciencedaily.com/releases/2019/03/190313143300.htm)
- [Dreissen et al. 2022, Nat. Commun.](https://ideas.repec.org/a/nat/natcom/v13y2022i1d10.1038_s41467-022-34818-0.html)
