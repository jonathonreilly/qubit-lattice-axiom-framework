# C5 round 2, probe R2-3: rare record flashes on a continuum, against the gravity walls (worker report)

**Worker.** Claude Opus 5.5 (same family as the supervisor and the round-1 probes). **Not refereed.** Run 2026-10-12, 11:53Z to about 12:40Z. No repository file was edited.
**Scratch.** `scratchpad/C5/R2-3/`:
- `r23_lemmas_check.py` / `.out`: numerical sanity checks of Lemmas B, T and H (below);
- `r23_numbers.py` / `.out`: all arithmetic for (a)–(g).

**Read in full.** `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS.md` "Campaign C5" (2302–2643) including R2-3 (2533–2559); `agents/C5_O5_synthesis.md`; `SUMMARY.md` §§15–21; `PRICE_NOTE.md` §§1, 2, 5, 6 and the v6 delta with wrap-up additions; `C5_O4_referee.md` and `C5_O4_report.md`; `C5_O2_referee.md`, the flash and unimodular rows of `C5_O2_report.md` and `C5_O2_referee_full.md` §7; `C5_O3_referee.md`; `C4_V3_referee.md`; `RV4_S1_referee.md`; `C3_X2_referee.md`; `B_referee.md` items 2, 9, 16.

**Prior art (each counted once).**
- PRICE_NOTE P4 (`PRICE_NOTE.md:166`); `B_referee.md:103` (4e-151 per Planck event); `B_referee.md:185-190` (the ways to reconcile records with heating).
- X2: white stress noise in the FR3 gases, bounded FAIL (`C3_X2_referee.md:5,32`).
- O2's flash row, which states that the Bianchi identity tolerates kicks "only as a gradient (unimodular; Josset–Perez–Sudarsky 2017)" (`C5_O2_report.md:225`). Its referee: flash models are legitimate covariant-in-law candidates, but "their gravity, energy-conservation, and record bridges remain open" (`C5_O2_referee_full.md:283-285`). The TDiff row is at `C5_O2_report.md:163`.
- The refereed O4 numbers: the 0.1 µm heat bound (`C5_O4_referee.md:30`), the ion bound (`:28`) and Bell (`:36`).
- Candidate-law records fork F, a CSL window "1e-16 ≲ λ ≲ 5e-15 s⁻¹" quoted from Majorana, and "a site-local hit heats the vacuum" (`.claude/science/candidates/candidate-law-20261008/DECISION_MATRIX.md:23,82`).
- The rGRWf description in `archive/notes/docs/work_history/repo/review_feedback/BARE_METAL_RECORD_ACTUALIZATION_PRIMARY_SOURCE_AUDIT_2026-07-14.md:174-185`.

The repository has no prior computation of the flash source against the Bianchi identity, the TT channel or definiteness.

**Labels.**
- **proved:** a proof is given here.
- **checked:** arithmetic or a numerical check, in the scratch files.
- **suggested:** argued, not proved.
- **reading:** an interpretation.
- **comparator / RECALLED:** literature from memory, not re-derived.
- **web-checked:** confirmed by a search during this run.

---

## 0. Verdict in plain words

- **The flashes are gravitationally inert in size** (checked). At any rate that the heat bounds allow, every gravitational effect of the flashes sits many orders of magnitude below its bound:
  - the TT channel against P0's μ, at the densities and frequencies that matter;
  - the stochastic GW background;
  - force noise in LIGO and LISA Pathfinder;
  - the late-time drift of Λ;
  - neutron-star and IGM heating.

  The registered expectation is right on sizes.
- **They are not consistent with Einstein's equations, even in unimodular form** (proved, bounded). A flash changes matter's energy-momentum at one place and one instant (or on one hyperboloid). The source J^ν = ∂_μT^{μν} that this creates is never a gradient, so unimodular gravity cannot absorb it per realization (Lemma B).
  - If gravity is sourced by the collapsed state (semiclassical), any flash that gives a definite outcome breaks the identity, because the pointer's mass moves without a current.
  - If gravity is quantum (A5's supplied gauge graviton) and the flash acts on matter, every flash law of the GRW/rGRWf type breaks the gravitational constraints. Such a law must heat (Lemma H), and a local change of total energy-momentum cannot be squared with Gauss-type constraints and causality (Lemma Q).
  - **Josset–Perez–Sudarsky's unimodular repair works only for the spatially uniform part of the average heating.** For inhomogeneous matter, such as the Earth against empty space, even the averaged source is not a gradient (Lemma B′).
  - The defect is tiny: about (ℓ_P/r_C)² ≈ 3e-56 per flash per nucleon, as a gauge-defect strength (estimate). But it breaks an exact identity, and the registered test (b) asks for exact compatibility.
- **Definite outcomes against heat** (proved, bounded). For laws in which each particle flashes independently (rGRWf-type), a general inequality bounds the localization rate of a pointer of N nucleons spread over d by the heat each nucleon may receive: Γ ≤ N m d² P/ħ².
  - For the registered pointer (1e10 nucleons, 1 µm, 1 ms), the refereed Earth-heat allowance gives at most about 20 s⁻¹. The neutron-star allowance gives at most about 290 s⁻¹. Both are short of the 1000 s⁻¹ needed.
  - The same pointer in air becomes definite in about 0.5 ms at λ ≈ 2.6e-11 s⁻¹, through the air molecules that record it. That rate is inside the Earth-heat budget but above the X-ray bound quoted in the repository for r_C = 0.1 µm.
  - Collective laws (CSL-type) escape the inequality. But no covariant collective flash law is known that leaves the vacuum unexcited (Lemma V).
- **Against the FIXED readings:**
  - **Not PASS.** No explicit covariant flash law satisfies (b).
  - **FAIL (bounded).** Within the class stated in §1, every flash law at any nonzero density violates (b), and per-particle laws violate (d) at the registered isolated pointer.
  - **Not a FAIL for "every covariant flash law".** Three realizations outside the class remain (§7): metric jumps on a state-chosen hypersurface; non-Einstein (classical-stochastic or Newtonian) gravity; and records that do not act back on the quantum state (Bell-type beables, which are not collapse flashes).

  If the referee reads "every covariant flash law" as including those three, the verdict is **INCONCLUSIVE, with bounded FAILs on (b) and on (d)+(g)**.
- **Mandatory reading** (as registered, `TESTS.md:2559`), confirmed in size:
  - the flashes are gravitationally inert, so set A's discreteness does nothing in gravity;
  - the graviton and Λ stay unexplained.

  **Added price for set A** (suggested): set A also has to pay a gravity-coupling price at the flashes. Its options are listed in §7.

---

## 1. Hypotheses (stated before the title) and the class

- **H-flash.** The flash law is covariant in law and translation-covariant. Each flash is a local or quasi-local quantum operation: Kraus operators in the bounded-region algebra, or its norm closure, near the flash.
  - **Class Π_pos (rGRWf/GRW type):** the Kraus operators are multiplication by a real envelope f(x_k − X) of one particle's position (on a slice or a hyperboloid), at flash rate λ per particle (mass-proportional when stated).
  - Between flashes matter evolves by a local Hamiltonian with a conserved T^{μν} (operator conservation).
- **H-grav.** The supplied linearized metric (A5) obeys the linearized Einstein equation, or its trace-free unimodular version, as a global solution across the flashes. It is coupled in one of two ways:
  - **(S)** classically, to a per-realization stress, either ⟨T^{μν}⟩ in the conditional (collapsed) state or a stress built from the flashes; or
  - **(Q)** quantum-mechanically, with physical states annihilated by the linearized constraints C_ν(x) = G^lin_{0ν}[h](x) − 8πG T_{0ν}(x), and with flashes acting on the joint state.
- **H-net** (Q only). Matter is a translation-covariant local quantum field theory in an irreducible representation. The constraints' surface charges at spatial infinity are the total P^μ.
- **H-loc.** The matter is spatially localized (its fields decay at spatial infinity on the collapse surface).
- **The budget** is the one registered (`TESTS.md:2536-2541`):
  - Earth heat: 1.32e-38 W per nucleon (O4 H4), refereed as an allowance (`C5_O4_referee.md:30`);
  - Lemma 1's V ≤ BC;
  - Cs-133 at 1.9 µm for 70 s;
  - ions coherent for more than 1 h;
  - X-ray limits as published.

**Outside realizations this scope excludes:**
- metric jumps on a chosen Cauchy surface, i.e. the semiclassical self-consistent-configuration approach (Diez-Tejedor–Sudarsky; Juárez-Aubry–Kay–Sudarsky; RECALLED);
- classical-stochastic or classical-quantum gravity (Oppenheim et al.; RECALLED), and Newtonian "massive flashes" (Tilloy 2018; RECALLED), where no Bianchi identity applies;
- Kraus operators dressed non-locally to spatial infinity;
- non-collapse records (Bell-type beables);
- collective (CSL-type) flash laws, for (g) only.

---

## 2. Probe (a): the flash source J^ν and its spectrum

- **Per flash** (Π_pos, Gaussian envelope of width r_C on the amplitude). These are standard GRW numbers (checked: `r23_numbers.out` [a]; Lemma H check).
  - The mean energy gain is ΔE = 3ħ²/(4 m r_C²) = 4.99e-28 J = 3.1 neV per nucleon at r_C = 0.1 µm. It is the same for every state.
  - The momentum kick has zero mean and variance ħ²/(2r_C²) per axis (rms 7.5e-28 kg m s⁻¹).
- **Per realization (proved form).**
  - In (S): J^ν(x) = δ_Σ(x) n_μ Δ⟨T^{μν}(x)⟩, supported on the collapse surface Σ (a slice, or rGRWf's hyperboloid). Δ⟨T⟩ is spread over the wavefunction on Σ. Its integral is the change of the expected 4-momentum. For a pointer that becomes definite it contains the mass-density jump |β|²(ρ_L − ρ_R), so it is non-zero even with no heating.
  - In (Q): the constraint defect −8πG[T_{0ν}(x), K_X] has the kick structure above.
- **Spectrum.**
  - The force-density noise is white: ⟨J_iJ_j⟩ = δ_ij n λ ħ²/(2r_C²) δ⁴(x−y) for independent per-particle flashes.
  - The mean is J_0 = −n λ ΔE in signature (−+++), with J_i = 0.
  - The TT stress noise driven by the kicks is shot noise filtered by stress relaxation: S_TT(ω) ≈ n λ ⟨Δτ²⟩ τ_r²/(1 + ω²τ_r²), where ⟨Δτ²⟩ = kT ħ²/(m r_C²) (estimate; §4).

## 3. Probe (b): the Bianchi identity, unimodular gravity and the Λ drift

**Lemma B (jump-type sources are never gradients). Proved.**
- *Statement.* Let J = δ_Σ α, with Σ a smooth spacelike hypersurface and α a 1-form density on Σ that decays along Σ. Then dJ = 0 implies J = 0.
- *Proof.*
  - dJ = δ′_Σ dσ∧α + δ_Σ dα. Since δ′ and δ are independent distributions, both terms vanish.
  - The first term vanishing forces α = c dσ. The second then forces dc∧dσ = 0 on Σ, so c is constant along Σ.
  - Decay gives c = 0. ∎
- *Extension.* The same holds for any finite set of flashes on distinct surfaces.
- *Check.* Discrete version on a 9×9×T lattice with compact support: one temporal layer gives nullity 0. Two or three layers (δ′-type, "inject then withdraw") give nullity 9 and 18. `r23_lemmas_check.out` L-B.
- *Consequence.* Unimodular gravity requires ∂_νΛ = 8πG J_ν, i.e. J closed. **No flash that changes the energy-momentum density of localized matter is compatible with it, per realization.**
- *Correction.* The registered premise "GR tolerates only a gradient source, so the setting is unimodular" (`TESTS.md:2549`), and O2's flash row (`C5_O2_report.md:225`), read as if unimodular gravity accommodated the kicks. It does not, per event.

**Lemma B′ (continuous or averaged sources). Proved.**
- *Statement.* If J is closed, then J_i(t,x) = ∂_i ∫^t J_0(t′,x) dt′.
- *Application.* For the ensemble (Lindblad) source of Π_pos, J_i = 0 by isotropy and J_0 = −λΔE·n(x). So closedness ⇔ ∇n = 0.
- *Consequence.* **The Josset–Perez–Sudarsky repair holds only for spatially homogeneous matter.** Earth against vacuum already violates it.
- *Scope.* Whether JPS state this: RECALLED, not checked.

**(S) semiclassical sourcing. Proved.**
- *Statement.* For any Kraus form, a flash that makes a superposed position pointer definite changes ⟨T_00⟩ on Σ by |β|²(ρ_L − ρ_R) ≠ 0. By Lemma B (or B′ for continuous collapse) this is not closed. So the linearized (unimodular) Einstein equation sourced by the conditional state has no solution across the flash.
- This holds at any flash density. It needs no heating.
- A stress built from the flashes themselves (massive flashes) is not conserved either: u·∂δ⁴ dipoles, or the Δp kinks of segment worldlines. It is not closed.

**(Q) quantum metric. Proved under H-net.**
- **Lemma H (state-independent heating).** For a translation-covariant Kraus family {f(x−X)} with ∫f² = 1, d⟨H⟩/dt = λ(ħ²/2m)∫|∇f|² > 0 for every non-constant f and every state. The double commutator with Σp²/2m + V(x) is a c-number; the f-sum rule applies.
  - *Check:* 0.2490, 0.2498 and 0.2499 for three different states, against 0.25 (`r23_lemmas_check.out` L-H).
  - So every flash law in Π_pos changes the matter energy in some realizations, for every state.
- **Lemma Q (local, constraint-preserving Kraus operators are trivial).**
  - *Statement.* If K is in the quasi-local algebra and maps every physical state to a physical state, then [P^μ, K] = 0, and therefore K ∝ 1.
  - *Proof, step 1.* Integrate [C_ν(x), K]Ψ = 0 over Σ. At linear order ∫_Σ G^lin_{0ν} is a surface charge at infinity, which commutes with a quasi-local K. So [P^ν_matter, K]Ψ = 0 for all physical Ψ. With gravitons included the same holds for the total P.
  - *Proof, step 2.* A quasi-local, translation-invariant K commutes asymptotically, and hence exactly, with every local operator. So K is central, i.e. a scalar. ∎
  - *Meaning.* This is the gravitational form of "charge non-conservation contradicts Gauss's law plus causality". A local flash that changes total energy-momentum would have to change the surface charge at spatial infinity at once.
  - rGRWf's hyperboloids reach null infinity, not spatial infinity, so they cannot carry such a dressing. A dressing to spatial infinity has to pick a Cauchy surface.
- **Conclusion for (Q).** Every flash law in Π_pos violates the constraints with positive probability per flash, for every state. Every non-trivial local Kraus family violates them on some physical states.
- **Size of the defect** (estimate, `r23_numbers.out` [b′]). The gauge-defect strength per flash per nucleon is (Δp/M_Pl c)² = (ℓ_P/r_C)² = 2.6e-56 at r_C = 0.1 µm. Numerically negligible; an exact-identity failure all the same.

**Λ drift** (checked, `r23_numbers.out` [b]; homogeneous mean only, which Lemma B′ allows).
- **Sign.** ∂_tρ_Λ = J_0 = −ρ̇_heat in signature (−+++). Flash heating drains the unimodular Λ, so w_eff > −1. JPS's positive-Λ reading would need the opposite flow (RECALLED, not checked).
- **Today.** |d ln ρ_Λ/d ln a| = n_b λΔE/(H₀ρ_Λ):
  - 1.1e-17 at GRW (λ = 1e-16);
  - 5.5e-16 at the quoted X-ray limit (5e-15);
  - 2.9e-12 at the Earth-heat maximum (2.6e-11).

  This is |w + 1| ≤ 1e-12. Negligible.
- **Integrated injection.** ∫ρ̇_heat dt from z_max, in units of ρ_Λ:

  | λ | z_max = 1 | z_max = 1e9 | z_max = 1e12 |
  |---|---|---|---|
  | GRW | 1.8e-17 | 1.1e-6 | 1.1e-3 |
  | X-ray quoted | 9.1e-16 | 5.7e-5 | 5.7e-2 |
  | Earth-heat max | 4.8e-12 | 0.30 | 300 |

  In unimodular gravity this is absorbed into the integration constant. It changes nothing observable after the early universe, but it is not an explanation of Λ (reading). Λ stays unexplained, as registered.

**(b) result. FAIL (bounded).** Exact compatibility fails per realization:
- for every flash law that gives definite outcomes, in (S);
- for every Π_pos law, in (Q);
- in GR and in unimodular gravity alike.

Only the homogeneous mean source is unimodular-compatible. Its drift is negligible.

## 4. Probe (c): TT noise, the graviton-mass channel, GW strain and pulsar timing

- **No mass from additive noise** (proved, trivial).
  - If the flash law does not depend on h, the noise adds to the symmetrized correlator only. The retarded TT response, and hence Π_TT(0), is the unitary theory's. So the flashes add nothing to P0's μ channel.
  - If the law is metric-covariant (proper rates and lengths), the induced response is secular. It is bounded by ρ̇_heat/ω (estimate). At the cosmic mean baryon density, where m_g is constrained by propagation, at LIGO frequencies, this is 1e-48 eV⁴ (GRW) to 3e-43 eV⁴ (Earth-heat maximum), against μ = 2.39e8 eV⁴.
  - At terrestrial density and Hubble frequency the bound reaches 1e9 eV⁴. That is not a propagation mass: it is a secular heating anisotropy (reading).
- **The additive stress noise S_TT(0)** (estimate; white, n_S = 0, the same spectral form as X2's).
  - IGM, with Spitzer relaxation τ_r ≈ 2e12 s: 4e-6 eV⁴ (GRW) to 1.1 eV⁴ (Earth-heat maximum).
  - Earth solid: ≤ 1e-19 eV⁴.
  - It is not a mass (above). Unlike X2, it lives in a supplied matter source, not in the graviton's carrier.
- **Stochastic GW background** from flash stress steps (estimate; O(1) prefactor omitted; ωτ_r ≫ 1):
  - Ω_gw ≈ 1e-117 to 2e-112 in the PTA band, against the measured signal of about 1e-9;
  - Ω_gw ≈ 1e-98 to 2e-93 in the LIGO band.
- **Direct kicks on detectors** (checked):
  - LIGO test mass: strain 2.6e-32 to 1.3e-29 /√Hz at 100 Hz, against about 4e-24.
  - LISA Pathfinder: 1.9e-22 to 9.5e-20 m s⁻² /√Hz, against about 1.7e-15 (RECALLED).
- **(c) result.** Inert by 4 decades (LISA Pathfinder, at the Earth-heat maximum) to more than 80 decades (GW background), depending on the channel (checked; the estimates are labelled as such).

## 5. Probe (d): heating

All figures are per nucleon, at r_C = 0.1 µm, mass-proportional. Checked, `r23_numbers.out` [d].
- **Neutron stars.** Heating does not depend on the state (Tilloy–Stace form; web-checked as stated in their abstract). At the GRW rate the equilibrium surface temperature is 948 K.
  - The coldest known neutron star, PSR J2144−3933, has T < 42,000 K (Guillot et al. 2019, HST; web-checked).
  - That gives λ ≤ 3.8e-10 s⁻¹ (redshift ignored).
- **IGM.** The GRW rate heats each baryon by 1e-3 K over a Hubble time. A loose ≲ 1e4 K allowance gives λ ≲ 1e-9.
- **Earth.** λ ≤ 2.6e-11 (refereed O4 figure, reproduced).
- **X-rays.** The repository's quoted figure is ≲ 5e-15 at r_C = 1e-7 (`DECISION_MATRIX.md:82`).
  - Web check: the Majorana PRL is confirmed to bound white CSL at r_C ≲ 1e-7, but its exact λ was **not re-verified**.
  - Its applicability to independent per-particle flashes (coherent nuclear emission) is conditional.
- **(d) result.** GRW-rate flashes pass every heating bound.

## 6. Probes (e), (f) and (g)

**(e) Bell.** Comparator, RECALLED (Tumulka 2006, J. Stat. Phys. 125:821).
- rGRWf's joint flash law is Lorentz-invariant in law, non-factorizing, and no-signalling, and reproduces the quantum-mechanical EPR–Bell statistics (in its non-interacting, distinguishable-particle domain).
- It meets the refereed O4 Bell requirement (`C5_O4_referee.md:36`) under the marginal reading of Admissibility.
- Not recomputed here. A repair of (b) by a hypersurface choice (§7, E1) has not been checked for no-signalling.

**(f) Maximum flash density.** Checked.
- **With (b) read exactly: zero.** Any nonzero density of a Π_pos law violates it in (Q), and any outcome-giving density violates it in (S).
- **With (b) set aside (heat only):**

  | Medium | Earth-heat maximum | X-ray quoted | GRW |
  |---|---|---|---|
  | Earth mean | 2.0e-128 | 3.8e-132 | 7.5e-134 |
  | Water | 3.6e-129 | 6.8e-133 | 1.4e-134 |
  | Cosmic mean | 1.5e-159 | 2.9e-163 | 5.7e-165 |

  All as fractions of Planck-density events (4.39e147 m⁻³ s⁻¹). This is consistent with O4's ~1e-128 to 1e-113 and B's 4e-151.

**(g) Definite outcomes.**
- **Lemma T (decoherence/heat trade-off). Proved.**
  - *Statement.* For a normalized envelope, 1 − C(d) = ½∫(f(y+d)−f(y))² ≤ ½d²∫|d̂·∇f|² (Cauchy–Schwarz along the segment), and the heating per flash is (ħ²/2m)∫|∇f|².
  - *Consequence.* For N independently flashing particles, each displaced by d, Γ_loc ≤ N m d² P/ħ², and ≤ N m d² P/(3ħ²) for an isotropic f. Here P is the heating power per particle.
  - *Check.* The maximum ratio is 0.999 (Gaussian), 0.993 (flat-top) and 0.992 (ring), all ≤ 1 (`r23_lemmas_check.out` L-T).
- **The registered isolated pointer (N = 1e10, d = 1 µm, 1 ms):**
  - the Earth-heat allowance gives Γ ≤ 19.8 s⁻¹ (any envelope), short by a factor of 50;
  - the neutron-star allowance gives Γ ≤ 288 s⁻¹, short by 3.5;
  - the loose IGM allowance gives Γ ≤ 715 s⁻¹, short by 1.4;
  - the quoted X-ray limit gives Γ ≤ 4e-3 s⁻¹.

  These bounds hold for every r_C and every envelope. At Earth heat the smallest isolated pointer that can become definite in 1 ms has N ≥ 5e11 nucleons. **(d)+(g) result: FAIL (bounded) for Π_pos at the registered isolated pointer.**
- **With environmental amplification** (checked; standard GRW lore).
  - A 1 µm pointer in air at 1 atm is recorded by about 2.6e17 nucleons per second (air molecules).
  - Becoming definite within 1 ms needs λ ≥ 7.6e-12 s⁻¹. That is inside Earth heat (2.6e-11) and neutron-star heat.
  - It is above the X-ray-quoted 5e-15 at r_C = 0.1 µm (definite in 39 ms there; 276 ms at GRW).
  - If the X-ray limit scales like heating, as λ/r_C² (RECALLED), then r_C ≳ 4 µm reopens the window. That is suggested, not checked against the large-r_C bounds for per-particle laws.
- **Collective laws.** CSL-type mass-density collapse gains a factor of about n r_C³ (4π)^{3/2}, about 1e10 in solids, so it escapes Lemma T. But:
  - **Lemma V. Proved, elementary; comparator Pearle and Ghirardi–Grassi–Pearle 1990, RECALLED.** A finite Lorentz-invariant measure on ℝ⁴ is c·δ₀, because every non-zero orbit carries an infinite invariant measure. So stationary covariant noise with finite variance at a point is constant. A non-trivial covariant noise coupled to a local operator with vacuum spectral weight excites the vacuum at an infinite rate per unit volume.
  - Non-relativistic CSL's mass-density operator is not covariant.
  - **Result:** no covariant collective flash law that leaves the vacuum unexcited is established here. The lattice analogue is DECISION_MATRIX's "site-local hit heats the vacuum".
- **Lensing (F6), not asked.** Mass-proportional flashes do not act on photons, so they produce no RZ-type lensing noise (suggested).

---

## 7. What would work, and the prices (suggested; none adopted)

Exact (b) together with definite outcomes needs one of the following.

- **E1. Metric jumps on a state-chosen Cauchy surface.** At each flash the gravitational initial data are re-solved, with the constraints holding on both sides (semiclassical self-consistent configurations, Juárez-Aubry–Kay–Sudarsky; RECALLED).
  - Price: the metric obeys Einstein's equations only between flashes.
  - It needs a foliation, which can be covariant in law if the state chooses it, as in Ψ-determined Bohm–Dirac foliations (RECALLED).
  - It has non-causal Coulomb-field jumps.
  - Its no-signalling has not been checked.
- **E2. Non-Einstein gravity.**
  - Classical-stochastic or classical-quantum gravity (Oppenheim et al.): a covariant version is known only for Nordström scalar gravity (RECALLED). It pays the decoherence–diffusion trade-off cited in O4.
  - Or Newtonian massive flashes (Tilloy).
  - Price: conflicts with A5 (the graviton as an exact diffeomorphism gauge field).
- **E3. Records that do not act back on Ψ.** These are Bell-type beables or guided flashes. Ψ evolves unitarily and T is conserved as an operator, so (Q) holds exactly.
  - Price: a beable layer with relativistic guidance, which needs a preferred or Ψ-determined foliation.
  - It is not a collapse flash law, so it lies outside R2-3. It equals records fork B in `DECISION_MATRIX.md:23` (count once).
  - This is the only route found that keeps exact (b) with local dynamics in Ψ (suggested).
- **E4. Kraus operators dressed non-locally to spatial infinity.** This is the operator version of E1 and has the same surface-choice cost.

**Reading for set A** (O5 §2.1, `C5_O5_synthesis.md:318-346`).
- A4, "flash-like records", is consistent in size with every gravitational bound.
- But A5, a supplied exact gauge graviton, together with A4 as collapse flashes, is inconsistent per realization.
- So set A must add either E1/E4 (a state-chosen foliation for metric jumps) or E3 (records as non-collapse beables, with a foliation). The alternative is to give up A5 for E2.
- **Either way a foliation, or a non-gauge graviton, returns.** That bears on set A's motive, exact Lorentz invariance in law. The cost is surface or guidance structure, not a speed tuning (suggested).

## 8. Against the registered expectation (`TESTS.md:2559`)

- **"PASS at GRW-type rates, with every gravitational effect many orders below the bounds."**
  - Confirmed on sizes: (c), (d), the Λ drift, and (f) when (b) is set aside.
  - Not confirmed on (b): unimodular gravity does not absorb per-event or inhomogeneous sources (Lemmas B and B′), and quantum-constraint coupling fails as well (Lemmas H and Q).
  - Not confirmed on (g) for the isolated registered pointer under independent per-particle flashes (Lemma T). It holds with environmental amplification, inside the Earth-heat budget.
- **The mandatory reading** (flashes gravitationally inert; graviton and Λ unexplained): confirmed. Added: set A owes a gravity-coupling price at the flashes (§7).

## 9. For the referee

- Lemma B and B′: the distributional step; the decay hypothesis on Σ.
- Lemma Q: the integrated-constraint step at linear order; the quasi-local commutation with surface charges; irreducibility.
- Lemma T: the Cauchy–Schwarz bound and its use with the refereed Earth-heat allowance.
- The Λ sign convention.
- Whether "every covariant flash law" in the FIXED FAIL reading includes E1 to E4. That decides between FAIL (bounded) and INCONCLUSIVE.
- Numbers not re-verified: the exact Majorana λ; the LISA Pathfinder floor; Tumulka's no-signalling and Bell results.

Sources (web-checked this run): [Majorana PRL 129, 080401 / arXiv:2202.01343](https://arxiv.org/pdf/2202.01343); [Tilloy & Stace, arXiv:1901.05477](https://arxiv.org/pdf/1901.05477); [Guillot et al., PSR J2144−3933, arXiv:1901.07998](https://arxiv.org/pdf/1901.07998).
