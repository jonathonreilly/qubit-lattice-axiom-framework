# B1 (physics-first backward reasoning): agent report (Claude Opus 5.5, xhigh; 2026-10-09)

Verbatim. Same-family, not refereed; necessity claims go to the codex sol referee before entering the summary. Scripts in `scripts/B1/` (c5 imports `scripts/E23/e23_core.py`).

# B1 report: reasoning backward from what gravity must deliver to what the substrate must be

**Lens.** B1, physics-first. **Agent:** Claude Opus 5.5 at xhigh. This is the same model family as the supervisor and B2, and nothing here is refereed.

**What I read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` (all 233 lines) and `PRIMITIVE_REGISTRY_CHECK.md`.
- The packet files: SUMMARY, WALL, ASSUMPTIONS, ROUTES, APPROACH_REGISTRY, OUTSIDE_VIEW and TESTS.
- The agent reports: E1 and E23 with their referees, R3, R4, and the F1a, F1b and F2 kills with their referees.
- The candidate pack's TEST_LOG (K7a, K3a, K3a′, K3a″, G0c, W1, W2, FR1, FR3), the KILL_SHEET and the DECISION_MATRIX.
- From the viability branch: the 09-29 exercise SUMMARY and the viability map, including its gravity panels and the 09-29 owner-decision section.

**What I did not read.** I left `agents/supervisor_thread.md` unread to keep this lens independent. I took Lemma P from the referee's corrected statement.

**Labels.**
- **proved:** an exact derivation given here.
- **checked:** computed here.
- **suggested:** an argument.
- **reading:** an interpretation.
- **comparator:** literature. Every number marked (M) is quoted from memory and was not re-fetched in this run.

**Scripts.** All are in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/ex_grav/B1/`, each with a `.out` file beside it:
- `B1_c1_tt_bound.py`;
- `B1_c2_mass_invariants.py`;
- `B1_c3_noise_thresholds.py`;
- `B1_c4_records_arith.py`;
- `B1_c5_euclid4d_noise.py` and `B1_c5b_euclid4d_noise_more.py`.

c5 imports the packet's `scripts/E23/e23_core.py` read-only. No repository file was edited.

---

## 0. The answer in five lines (reading, assembled from the sections below)

1. **The core requirement.** Data and theorems together require the long-distance theory to have a **gauge redundancy acting on the graviton (linearized diffeomorphisms)**, and to have **one light cone**. On a discrete substrate the redundancy must hold **in each realization, not only on average**. That is what forbids a graviton mass, makes the substrate's own noise harmless, and (with the light cone) makes coupling universal and the nonlinear theory unique.
2. **What this means in plain terms.** The substrate's discreteness must not act as a **physical coordinate system**. Its elements must not carry persistent, readable positions that resist being sheared.
3. **The three known ways to have discreteness without physical coordinates:**
   - a Lorentz-invariant random set of spacetime events with unboundedly many links (causal-set-like);
   - discreteness that is itself a gauge choice, summed over;
   - discreteness only in the spectra of a gauge-invariant quantum geometry.

   None is a finished construction.
4. **Where the framework stands.** Z³ with readable sites and cubic covariance is a physical coordinate system: the "gravitational Higgs phase". Keeping it costs tuned numbers: two shear numbers to about 1e-104 of Planck⁴, and possibly speed tunings (Test 2).
5. **The owner's thoughts.** They help exactly to the extent that "records" are read as **spacetime events** (counted, causally ordered, not persisting at sites). They hurt under the reading of records as **persisting located objects**.

---

## 1. Requirements table (comparator; numbers M unless computed)

| # | Requirement | Observational bound | Source |
|---|---|---|---|
| R1 | Massless helicity-±2 mode | m_g ≤ 1.27e-23 eV (90%); ephemerides about 3e-23 eV | GWTC-3, arXiv:2112.06861; Bernus et al. 2019 |
| R2 | GW speed equals light speed | −3e-15 ≤ (v_g − c)/c ≤ +7e-16 | GW170817 + GRB170817A, ApJL 848, L13 |
| R3 | Two tensor polarizations; no extra gapless mode at gravitational strength | Pure-tensor polarization favoured over pure vector/scalar (Bayes factors about 200 and 1000). Double-pulsar orbital decay matches GR's quadrupole to 1.3e-4. Brans–Dicke ω > 4e4 | GW170814 PRL 119, 141101; Kramer et al., PRX 11, 041050 (2021); Cassini |
| R4 | One light cone for all species | Dimension-4 speed differences 1e-15 to 1e-27 by sector; photon vs matter about 1e-18 (resonators). Dimension-5 photon: E_QG,1 > 1.2 E_Pl (Fermi GRB 090510), about 10 E_Pl (LHAASO GRB 221009A) | Kostelecký–Russell, arXiv:0801.0287 |
| R5 | Universal coupling / equivalence principle | η ≤ about 1e-15 (MICROSCOPE final, PRL 129, 121102); η(Be,Ti) ≲ 2e-13 (Eöt-Wash). Strong form: LLR Nordtvedt η_N ≲ 1e-4; triple pulsar \|Δ\| < 2e-6 | Touboul 2022; Schlamminger 2008; Archibald 2018; Voisin 2020 |
| R6 | Newtonian 1/r and post-Newtonian GR | Yukawa \|α\| = 1 excluded for λ ≳ 40–50 μm. γ − 1 = (2.1 ± 2.3)e-5. \|β − 1\| ≲ 1e-4. Pulsar timing; ringdowns consistent with GR | Lee et al. PRL 124, 101101; Bertotti 2003 |
| R7 | Stable, coherent propagation over Gpc | GW phase coherence over about 1 Gpc (matched filtering, dispersion tests). Sharp optical-to-γ images and timing of Gpc sources. 10 TeV photons over about 0.75 Gpc | LVK tests; Perlman et al. 2015 (spacetime foam); LHAASO |
| R8 | Locality | ≲ 1e-19 m (the packet's bar; LHC contact scales Λ ≳ 20–40 TeV) | ATLAS/CMS |
| R9 | No swerves, momentum diffusion or anomalous heating | CMB photon swerve k₁ < 7e-97 (Planck units); relic-neutrino bound; collapse-model heating bounds (Ge X-rays, LISA Pathfinder) | Philpott–Dowker–Sorkin 0810.5591; Kaloper–Mattingly astro-ph/0607485; Donadi 2021 |
| R10 | Small cosmological constant | ρ_Λ = 2.51e-11 eV⁴ = (2.24 meV)⁴ = 1.1e-123 M_Pl⁴ (**checked**, c1) | Planck 2018 |
| R11 | Quantum consistency | Unitarity (no ghosts; positive transfer on physical states); loophole-free Bell violation; stable records; no signalling | Hensen 2015 et al. |
| R12 | Black-hole thermodynamics (consistency, not data) | Area theorem consistent with GW150914 ringdown (97%); S = A/4 is theoretical | Isi et al., PRL 127, 011103 |

---

## 2. From each requirement to the substrate property it forces

For each theorem I list its hypotheses (H) and say what would have to fail for the necessity to fail.

### 2.1 Only a gauge redundancy forbids a graviton mass (R1)

- **proved / checked (c2).** A local mass term M(h,h) is never forbidden by a point group or by Lorentz symmetry. tr h² is invariant under every orthogonal group.
  - **Counts of independent mass invariants (checked):**

    | Group | On Sym²(R³) | On traceless (TT-type) |
    |---|---|---|
    | SO(3) | 2 | 1 |
    | proper cubic O (24) | 3 | 2 (separate E_g and T_2g) |
    | icosahedral (60) | 2 | 1 |

    On Sym²(R⁴): SO(4) has 2, the hypercubic W(B4) (384) has 3, and SO(3,1) has 2.
  - **Gauge invariance does forbid it (proved).** The gauge directions q⊗ξ + ξ⊗q span all of Sym² (rank 10 of 10, checked), so M(h, δh) = 0 for all h and δh forces M = 0. Linearized gauge invariance δh = ∂ξ + ∂ξ forbids every local mass form; nothing else does.
- **Fierz–Pauli/vDVZ and the Lorentz-violating case (comparator).**
  - Lorentz invariance allows the Fierz–Pauli mass. vDVZ gives γ = ½ at linear order unless Vainshtein screening acts.
  - In the Lorentz-violating "m₀ = 0" phase (Rubakov–Tinyakov), which is the framework's phase (F1b's K1 found m₀ = m₁ = m₄ = 0), there is no vDVZ jump. The binding bound is then the GW dispersion bound, R1.
- **Not natural (comparator; reading).** h² is a dimension-2, relevant operator, so no IR attractor helps. It is technically natural only if m → 0 restores a symmetry. On a substrate whose labels are physical, it restores none (Dubovsky).
- **(H)** A local symmetric-tensor EFT at long distance, and "mass" meaning a local non-derivative quadratic term.
- **Fails if:**
  - the "mass" is non-local, e.g. μ·P_TT(q) with q_iq_j/q², which gapless sectors can generate;
  - there is no EFT (strong coupling);
  - there are infinite towers of fields.

### 2.2 With universal coupling, the vacuum's shear modulus is the graviton mass (R1 + R5)

- **suggested.** If h couples to all energy-momentum, including the vacuum's (R5 plus §2.5), then a constant volume-preserving strain changes the vacuum energy by ½μh². That is a graviton mass term, with m_g² = 4μ/M² in GR normalization (reduced M; same as the F1a referee).
- **checked (c1).** R1 requires μ ≤ 2.4e8 eV⁴ = (124 eV)⁴ = **1.1e-104 M_Pl⁴** per Planck cell. That is 9.5e18 × ρ_Λ: the shear bar is 19 decades looser than the CC bar.
  - **Required suppression relative to the natural size:**

    | Cutoff | Allowed μ/Λ_c⁴ |
    |---|---|
    | 2 TeV (the 1e-19 m bar) | 1.6e-41 |
    | 1e16 GeV | 2.4e-92 |
    | M_Pl | 1.1e-104 |
  - **An unprotected substrate** with μ = c·a⁻⁴ needs a⁻¹ ≤ 668 eV for K3a″'s c = 1.2e-3, and 173 eV for the free natural-coupling c = 0.27. That is excluded by everything above about 1 keV. At a = l_P it gives m_g ≈ 4e27 eV, 3e50 times the bound.
- **(H)** Universality includes the vacuum stress; a stationary flat background (no tadpole); an analytic q → 0 response.
- **Fails if:**
  - **(i) The vacuum stress does not gravitate.** The known sequestering and self-tuning mechanisms act on the trace only (Volovik/Klinkhamer: first derivative; Kaloper–Padilla: trace). None is known for shear. **comparator.**
  - **(ii) The response is non-analytic.** E1's "crackling" order has no Hessian per realization.
  - **(iii) The graviton is emergent and its 1PI TT mass differs from the vacuum Hessian** (the K3a″ referee's caveat).
- **Property V: the vacuum must be a fluid.** Its energy must depend on the metric only through det g.
  - **proved (c2c):** d²/dt² f(det e^{th}) = 0 for tr h = 0. A cubic solid Σg_ii² gives 8 (E_g) and 4 (T_2g); an isotropic solid tr g² gives 8 and 8.
  - A Lorentz-invariant vacuum (⟨T_μν⟩ ∝ g_μν) is a special case. Then Λ is the only vacuum number (§2.11).

### 2.3 Physical labels put the substrate in the "gravitational Higgs phase" (R1)

- **comparator.** Coupling a metric to fields φ^I that define comoving coordinates is the gravitational Higgs mechanism ('t Hooft arXiv:0708.3184; Chamseddine–Mukhanov 2010; Dubovsky hep-th/0409124; Rubakov–Tinyakov 0802.4379). The graviton's TT mass m₂ is set by the medium's shear modulus. m₂ = 0 is protected only by:
  - (a) no spatial labels (ghost condensate, Hořava: spatial diffeomorphisms unbroken);
  - (b) labels with a continuous, volume-preserving relabelling symmetry (a fluid, F(det B));
  - (c) no medium, i.e. exact diffeomorphism gauge.
- **suggested: a trichotomy for substrates.**

  | Substrate | Graviton | Extra modes |
  |---|---|---|
  | Explicit fixed labels (Z³) | massive | no phonons |
  | Spontaneous labels (a crystal of mobile sites) | massive | plus 3 phonons |
  | No labels, or a relabelling-invariant state and law | massless | — |

  A fixed-connectivity network with mobile positions is a rubber. Rubber has a nonzero (entropic or zero-point) shear modulus (comparator, rubber elasticity; consistent with W1 and with R3's see-or-stiff result). So **the neighbour relation must be able to rearrange**, not just the positions.
- **Lemma R** (packet, R4; narrowed by the T2 referee to ordinary, local, additively momentum-conserving interacting laws). Z³ with discrete translations admits no continuous relabelling, so the framework is in the explicit-label class.
- **(H)** A low-energy EFT of smooth label fields coupled covariantly; labels are the only diffeomorphism breakers.
- **Fails if:** strong coupling beyond the EFT, or labels that are themselves gauge (a sum over discretizations).
- **Property L: no physical coordinates at long distances.**

### 2.4 Weinberg–Witten: the graviton must be a gauge mode (R1 with R2/R4)

- **comparator** (PLB 96, 59, 1980).
- **(H)**
  1. Poincaré-covariant one-particle states;
  2. a conserved, Lorentz-covariant T^μν;
  3. ∫T^{0μ} = P^μ on those states;
  4. forward-limit continuity.
- **Conclusion:** no massless |h| > 1 particle carries energy-momentum.
- **Consequence.** The data force a Lorentz-invariant IR (R2, R4) and a massless helicity-2 mode (R1). So (H2) must fail in the IR: **Property G is that a (linearized) diffeomorphism redundancy acts on h.** A symmetric-tensor composite of Lorentz-invariant matter is excluded. The finite-slot "composite graviton" exit (c) of 09-29 must carry such a redundancy.
- **Corollary (comparator, Marolf PRL 114, 031104).** With diffeomorphisms as gauge there are no strictly local gauge-invariant positions. Readable locations must be relational.
- **Fails if:** the graviton lives in another spacetime (holography); the IR is Lorentz-violating beyond the R2/R4 bounds; the stress is non-local.

### 2.5 Weinberg's soft theorem: universality comes free in a Lorentz-invariant IR (R5)

- **comparator** (Phys. Rev. 135, B1049).
- **(H)** A Lorentz-invariant S-matrix; a massless helicity-2 with a nonzero soft coupling; pole factorization; asymptotic states.
- **Conclusion:** all soft couplings are equal, so coupling to energy is universal (the equivalence principle).
- **Consequence (suggested).** G plus a Lorentz-invariant IR makes universality automatic. A Lorentz-violating IR makes universality a separate construction burden ("one geometry for all sectors", as in W1).
- **Lattice note (suggested).** Newtonian Eötvös universality uses the energy density. On a Hamiltonian lattice the energy density is exactly locally conserved. The lattice's defect is the **momentum and stress** (K3a), which enter m_g and c_g rather than the Newtonian equivalence principle.
- **Fails if:** there is no S-matrix (cosmology), the IR is Lorentz-violating, or factorization fails.

### 2.6 Deser/Wald: nonlinear GR comes free (R6, strong equivalence)

- **comparator** (Deser GRG 1, 9; Wald PRD 33, 3613; Boulware–Deser 1975).
- **(H)**
  1. a massless spin-2 field with linearized gauge invariance;
  2. Lorentz invariance;
  3. a local two-derivative leading action;
  4. a source equal to the total stress, including the field's own;
  5. d = 4.
- **Conclusion:** the unique consistent completion is GR, plus Λ and higher-derivative terms.
- **Consequence (suggested).** A substrate needs to deliver only G, a Lorentz-invariant IR and universality. The failure of lattice relabelling brackets to close (block 150) is a symptom of missing G, not an extra requirement.
- **Fails if:** scalar–tensor extras (bounded by Cassini), Lorentz violation, non-locality, or towers of fields.

### 2.7 Collins et al.: one light cone (R2, R4)

- **comparator** (PRL 93, 191301; reproduced in the packet: T1(a2) gives Δ = −0.696; F1b's K2 gives Ξ ≥ 1, refereed).
- **(H)** A regulator with a preferred frame; dimensionless couplings; no symmetry relating the species' kinetic terms; cutoff ≫ IR.
- **Conclusion:** speed differences of order g²/16π², independent of the cutoff scale and dependent on its shape.
- **Property C.** The law must be Lorentz invariant (at least in law), or it must have a symmetry forbidding every dimension-4 Lorentz-violating operator in every sector. Candidates:
  - **Euclidean hypercubic, with time as a lattice direction.** T1 shows this is sufficient (Z⁴ residual 2e-9). **For the graviton it works only with exact lattice gauge invariance**: K7a's count goes from 9 forms to 1 only if the interacting stress is exactly conserved, and K3a says no conserved stress exists in the tested class.
  - SUSY (Groot Nibbelink–Pospelov hep-ph/0404271).
  - Gravitational confinement or scale separation (Pujolas–Sibiryakov 1109.4495). This needs matter that is Lorentz invariant on its own.
- **Fails if:** Lorentz-invariant UV structure, special cancellations, or a strong RG attraction. Chadha–Nielsen's attraction is only logarithmic (Belenchia–Gambassi–Liberati 1601.06700).

### 2.8 Bombelli–Henson–Sorkin: Lorentz invariance in law plus a point grain means unbounded valency (R4, R8)

- **comparator** (gr-qc/0605006).
- **(H)** A Lorentz-invariant-in-law (Poisson) point process in Minkowski space, and a measurable, equivariant rule picking finitely many neighbours (or a direction) per point.
- **Conclusion:** no such rule exists. The root is that the Lorentz group is non-compact, so there is no invariant probability measure on the hyperboloid of frames. **suggested:** the same argument covers any point process that is Lorentz invariant in law.
- **Consequence.** If C is met by Lorentz invariance in law with a point grain, then "neighbours" must be causal links, unboundedly many. Locality becomes causal locality. The 1e-19 m bar applies to the non-locality scale ℓ_k (E1).
- **Loopholes:**
  - **Euclidean random lattices** (Christ–Friedberg–Lee; O(4) in law, finite valency). **I tested this one (c5): it fails on per-realization noise. See §2.9.**
  - Hypercubic Z⁴ (finite valency; dimension-4 isotropy by symmetry; not Lorentz invariant in law).
  - Discreteness in spectra (Rovelli–Speziale gr-qc/0205108).
  - A superposition over discretizations.

### 2.9 Per-realization noise: the requirement every "in law" construction failed (R7, R9)

- **Packet evidence (refereed with corrections).** Wherever the law protects the mean it is zero, but the noise is white or growing:
  - F1a: frozen Poisson sets;
  - E2/E3: dilution, quasicrystal, hyperuniform and growing sets;
  - E1: spacetime events.

  **Lemma P (corrected):** SL- or AN-law protection and an ensemble-hyperuniform density exclude each other.
- **checked (c5), new: the 4D Euclidean random lattice.**
  - **Setup.** A Poisson set in 4D, O(4)/SL(4)-invariant in law, finite valency, with R3/K1's proper-distance kernel (R = 1.8), boson zero-point energy, exact eigen-perturbation.
  - **Mean:** consistent with 0, for example +0.0001 ± 0.0003 at N = 255.
  - **Noise:** the per-site TT stiffness has sd·√N = 0.051–0.069 (m² = 1) and 0.059–0.079 (m² = 0.04). It is **flat over N = 255 → 4087 (16×)**, so the noise is white with S(0) > 0, and of the same size as F1a's 3D values (0.064–0.084). The TT tadpole is also white (sd·√N about 0.06).
  - **Scope.** Bounded to one kernel and a free scalar. Per the E23 referee, the sd·√N estimator is strong evidence for S(0) > 0, not a rigorous bound.
- **proved (dimensional analysis): how per-realization white noise scales.** Write δ_λ ∝ (ℓ/λ)^p for the fractional change of the wave operator over a wavelength cell.

  | Where the noise enters | Frozen 3D | White in 4D |
  |---|---|---|
  | Mass-type term (δm²) | p = −½ (relevant; F1a) | p = 0 (marginal; E1 and c5) |
  | Dimensionless kinetic coefficient | p = 3/2 | p = 2 |
- **checked arithmetic in a suggested random-phase toy (c3).** The model is φ_rms = 2πA(ℓ/λ)^p (D/λ)^{1/2} < 1.
  - **Required p (A = 1, ℓ = l_P):**

    | Probe | Required p |
    |---|---|
    | LIGO, 1 Gpc | 0.25 |
    | Optical quasars, 3 Gpc | 0.59 |
    | 31 GeV to 10 TeV photons over about 1 Gpc | 1.2–1.45 |
    | Electron or proton Compton phase over 1 km | 0.35–0.49 |
  - **Kinetic-type noise passes every probe at l_P.** Mass-type noise fails every probe, by 8 to 31 decades.
  - **Marginal mass-type noise** would need A ≲ 5e-11 to pass LIGO. c5's amplitude is about 0.06 per site, so it fails by about 9 decades.
  - **At ℓ = 1e-19 m,** even kinetic-type noise fails the γ-ray probes unless A ≪ 1.
  - **E1-type volume kernels** have a gain A = (6.7ε)^{1/2}(T/ℓ_k), which is about 9e13 at ℓ_k = 1e-19 m.
- **Property N.** Per realization, substrate noise may couple to each massless field only through operators of dimension ≥ 4, with a gain that does not grow with the size of the past.
  - For photons and gravitons this is per-realization gauge invariance; for fermions, chiral symmetry.
  - **For the graviton, N requires G per realization.** A per-realization random TT stiffness is mass-type noise (F1a, c5). So symmetry in law (Lemma A/L) cannot suffice.
- **(H)** Weak-scattering random phases; independent cells; an analytic per-realization response.
- **Fails if:**
  - a realization-wise coboundary identity holds (the F1a/E23 referees' double-curl stress gives S ∝ q⁴). That is itself a per-realization gauge-type identity;
  - the response is non-analytic and order-based (E1's crackling);
  - the substrate is annealed (§2.10).

### 2.10 Quenched versus annealed: the noise is not inevitable (R7, R9)

- **suggested, from comparators** (the Landau criterion; no vacuum Cherenkov radiation in a Lorentz-invariant vacuum).
  - A probe in a translation- and Lorentz-invariant **state** conserves energy-momentum. A massless on-shell probe can neither scatter elastically nor excite the vacuum, apart from collinear emission.
  - Substrate fluctuations then appear only as a Lorentz-invariant self-energy, which gauge invariance suppresses as p⁴.
  - A single quenched realization breaks momentum conservation and scatters. Swerves are the Lorentz-invariant-in-law version.
- **Consequence.** The discreteness must be either:
  - (i) a quenched, Lorentz-invariant-in-law grain that meets N per realization; or
  - (ii) held in the state: a superposition or sum over discretizations, or discreteness in spectra.
- **Caveat (reading).** Records quench. Once records form that depend on the configuration, each branch is a quenched realization.

### 2.11 The cosmological constant (R10)

- **proved.** In a fluid or Lorentz-invariant vacuum, shear is tied to the trace (§2.2): one vacuum number. On a cubic substrate there are three: the trace plus E_g and T_2g (Schur; R3/R4 in the packet). The data then need one number at 1e-123 and two at about 1e-104: three tunings instead of one.
- **proved (standard mapping theorem).** A Poisson process with intensity ρ·vol is invariant in law under **every** volume-preserving map of spacetime (SDiff(4), which contains Poincaré). It is a "spacetime fluid in law".
- **comparator.** If the element count is the 4-volume, the result is unimodular gravity:
  - Λ is conjugate to the volume, so the constant vacuum energy does not gravitate;
  - Poisson fluctuations give the "everpresent Λ", about 1/√V ≈ H²M_P², the observed order (Sorkin; Ahmed–Dodelson–Greene–Sorkin astro-ph/0209274);
  - E1 found the count TT-blind at fixed det, exactly.
- **Property V′ (helps, optional):** count = volume.

### 2.12 Quantum consistency and records (R9, R11, R12)

- **Positivity.** There must be a positive transfer on physical, constraint-reduced states. K7a's unreduced Euclidean form is indefinite (the conformal mode); whether a positive physical transfer exists is open.
- **checked (c4).** At Planck event density there are 4.4e147 events per m³ per s, i.e. 1.1e103 per nucleon volume per second.
  - If geometry-bearing events were records that lock matter possibilities, any disturbance probability above about 3e-135 per event would exceed the viability map's quoted heating bound.
  - **suggested:** locks of non-conserved matter observables at that rate Zeno-freeze matter (an effective rate of about J²/Γ).
- **Property Q.** Geometry-bearing records must not lock non-conserved matter possibilities. Geometry must be readable **relationally** from records. **comparator:** order plus number suffice. Hawking–King–McCarthy 1976 and Malament 1977 show that causal order fixes the conformal metric for past- and future-distinguishing spacetimes of dimension ≥ 3, and counting fixes the volume.
- **R12, checked (c4).** One record per Planck cell inside a solar-mass hole is 2.6e115, against S_BH = 1.0e77, a ratio of 2.4e38. A volume-law "frozen box" cannot be the Bekenstein–Hawking entropy (consistency, not data).

---

## 3. The intersection

**The necessary set.** Each property is conditional on the hypotheses above.

| Property | Content |
|---|---|
| **G** (per realization) | linearized diffeomorphism redundancy acting on h and on matter's regulator |
| **L** | no physical coordinates at long distance |
| **V** | vacuum energy depends on volume only |
| **C** | one cone, by Lorentz invariance in law or by a symmetry forbidding all dimension-4 Lorentz violation, with exact gauge invariance in every sector |
| **N** | noise only through dimension ≥ 4 operators, with bounded gain, or an annealed substrate |
| **B** | if C comes from a Lorentz-invariant-in-law point grain: unbounded valency and causal locality |
| **Q** | unitarity and record compatibility |

**How they relate (suggested).**
- G per realization implies L, V (locally) and N for the graviton.
- G plus a Lorentz-invariant IR implies universality (Weinberg), which with locality implies GR (Deser/Wald).
- **So the hard core is G per realization together with C.**

**Is the intersection nonempty?**
- **At the EFT and continuum level, yes.** GR plus the Standard Model meets every row except the naturalness of Λ, so the requirements are mutually consistent (reading).
- **For discrete substrates, no known construction meets them all.**

| Class | Example(s) | G (per realization) | C | N | V | Graviton derived? | What it lacks |
|---|---|---|---|---|---|---|---|
| I. Explicit fixed labels | the framework's Z³ (+ Z_τ, K7a) | ✗ (Lemma R; K3a″, W1; T2 floors) | ✓ for matter (T1); graviton only with an exact interacting stress (K3a open) | ✓ (a perfect crystal has no noise) | ✗ (3 numbers) | partial (K7a action; positivity open) | two tunings at about 1e-104, plus possible speed tunings (Test 2) |
| II. Lorentz-invariant-in-law events | causal sets | L in law ✓; per realization "crackling", no Hessian (E1) | ✓ in mean (exact) | open or ✗ (E1: volume-kernel gain diverges; links untested) | ✓ (unimodular, everpresent Λ) | ✗ (no derived spin-2; growth dynamics give non-manifold orders) | noise law, dynamics, graviton |
| III. Discretization as a summed gauge | spin foams (EPRL), CDT, perfect-action Regge, GFT | ✓ in principle (W2: the vacuum Regge gauge modes are exact; matter breaks them at fixed combinatorics, W1) | spin foams Lorentz covariant ✓?; CDT foliated ✗ | ✓ (annealed) | open | spin-foam graviton propagator at leading order (large spins) | continuum limit, matter universality; locality of perfect actions |
| IV. Discreteness in spectra | canonical LQG | ✓ | ✓ (Rovelli–Speziale) | ✓ | open | ✗ | dynamics (Hamiltonian constraint), low-energy limit |
| V. No spatial labels, foliated | Hořava, khronometric, Einstein-aether | spatial ✓ | ✗ (GW170817 forces c_T to 1e-15; Collins for matter unless gravitationally confined with matter Lorentz invariant on its own) | ✓ | ✓ | ✓ (with an extra scalar) | Lorentz-invariance naturalness |
| VI. Fluid of mobile sites | F1b | ✓ for the TT mass | ✗ (rest frame) | ✓ | ✓ | ✗ (the displacement is a vector) | degenerate at flat space (w = 0) |
| VII. Holographic | lattice-regularized boundary field theory | ✓ in the bulk | boundary lattice Lorentz violation | ✓ | AdS | ✓ in the bulk | our de Sitter 3+1 world; dimension count |
| VIII. Condensed-matter emergent | Gu–Wen, rank-2 spin liquids, fractons | partial (an emergent rank-2 constraint) | ✗ (ω ∝ k² or k³) | — | — | partial | Lorentz invariance, linear dispersion, partner modes (09-29) |
| — | string theory | ✓ | ✓ | ✓ | landscape | ✓ | no discrete qubit substrate; Λ |
| — | 4D Euclidean random lattice | in law only | ✓ in law | **✗ (c5: white, about 0.06 per site, marginal)** | in law | ✗ | closed by c5 (bounded) |

**Structural conclusion (reading).** The discreteness must not be a physical coordinate system. The three known ways for a discrete theory to avoid that are classes II, III and IV. The framework's Z³ is a physical coordinate system: sites are given, readable and covariant only under a finite group.

---

## 4. Confronting the framework (prices only; nothing adopted)

| Axiom clause | What it blocks | Through | Minimal change, stated as a price |
|---|---|---|---|
| **Lattice:** "points of Z³ … standard translations, proper cubic rotations" | R1 (G, L, V) | Lemma R; Rubakov–Tinyakov/Dubovsky; Schur (3 numbers); K3a″, W1; T2 | (a) Keep it and tune two shear numbers to about 1e-104 per Planck cell (c1), plus speed tunings if Test 2 fails. (b) Replace the site set with a Lorentz-invariant-in-law event set ("sites are where records form"; covariance becomes Poincaré/SDiff in law). (c) Make the site set a gauge choice that is summed over |
| **Lattice/Admissibility:** "nearest-neighbour" | C when it is met by Lorentz invariance in law | BHS | "Neighbours" become causal links (unbounded valency); locality becomes causal; the 1e-19 m bar moves to ℓ_k |
| **Admissibility:** covariance under translations and proper cubic rotations, with no boosts | C for the graviton | Collins; K7a | Within (a): the kinetic-isotropy primitive helps, but the graviton cone also needs an exactly conserved interacting stress, which is unknown (K3a; suggested: generic non-integrable lattice theories lack a local conserved momentum density with p ≈ k, cf. Shiraishi-type results) |
| **Admissibility:** "not a dynamics axiom" | R1–R3 need a propagating mode | — | A gap, not a block. Every class needs a supplied dynamics clause (one premise) |
| **Qubit:** M₂(C), finite | Only the mobile-site fluid (needs canonical commutation relations) and the local-slot graviton (09-29) | landed 05-02 no-go; probes 10–21 | Not a block for classes II and III, where the qubit is matter content (G0c: one qubit per site carries covariant fermions) and geometry is order (suggested) |
| **Record:** "one record per site; permanent" | Under the object reading (persisting located records): L, C, N | E2/E3; Collins (the record gas's rest frame); FR1/FR3 (records carry scalars and vectors, not the mediator) | Event reading: a record is a spacetime event, permanence means it stays a fact, the site is the event. Price: a supplied causal order (A36 says records carry no time) and sites created by records (a Lattice change) |
| **Record:** "only records are readable" | G (no local gauge-invariant positions) under the fixed-site reading | Marolf | Under the event reading, geometry is read relationally from order plus count (HKMM/Malament). This **helps** |
| **Realized-state primitive:** one realized configuration | Makes any record-borne geometry quenched (N must then hold per realization) | §2.9–2.10 | Or carry geometry in the pre-record (annealed) state. In practice that means classes III/IV, not records |

**The owner's thoughts, tested against the requirements.**

1. **"Records are reality's grain."**
   - **Helps** if the grain is counted spacetime events: V′ (unimodular Λ of the right order), C in law, relational readability.
   - **Hurts** if the grain is persisting located objects: labels give a massive graviton, the records' rest frame splits speeds (Collins), and quenched noise follows.
   - **Required either way (c4):** geometry-bearing records cannot be matter-disturbing locks.
2. **"Records can move between neighbouring sites."**
   - **Neutral to harmful.** On a fixed site set this is a fluid in a fixed (Eulerian) frame on a fixed regulator.
   - Lemma R, T0, R4's dilute-gas check (shear/interaction = 0.030) and FR3 (no tensor waves) all apply.
   - A moving record gas also defines a rest frame.
3. **"The record count rises until a region freezes."**
   - **Compatible as "the count measures elapsed 4-volume"** (sequential growth; Rideout–Sorkin gr-qc/9904062).
   - **Harmful as "a frozen region holds one record per site".** That is a perfect solid (maximal labels), and its volume law exceeds S_BH by 2.4e38 for a solar-mass hole (c4).
4. **"The sites are just the substrate; the neighbourhood can move across it, including the qubits."**
   - **Reading (a): a geometric site set with a moving pattern.** The regulator stays fixed, so it fails R1 without tuning.
   - **Reading (b): sites are an abstract set and geometry is the rearranging neighbourhood relation, with a law blind to site identity.** This meets L, and rearrangement is what a fluid needs (rubber point, §2.3).
   - But a Hamiltonian graph dynamics has a preferred time and fails C, unless the relation is spacetime-causal. Then it becomes class II.
   - **Helps exactly to the extent that it becomes "records as causally linked events".**

---

## 5. The cheapest decisive tests (readings fixed here, before any run)

### Test 1 (class II, about 1 day): an exact noise law for link-only propagation, evaluated at physical parameters

This is E1′(b) done analytically, with a two-species reading.

- **Setting.** E1′'s massless link propagator G₀ = aL on a 3+1 Poisson sprinkling (ρ = ℓ⁻⁴), with a smooth compact source J of size s and a field point at distance D.
- **Method.** Derive Var[(G₀J)(x)] from the Poisson moment (Mecke/Slivnyak) formulas: a one-point term plus the shared-emptiness two-point term. Get a closed form or a controlled asymptotic in s/ℓ and D/s, and check it by Monte Carlo up to s/ℓ of about 10.
- **Evaluate the law, not a fit,** at two points:
  - (ℓ_P; s = 3e6 m; D = 1 Gpc), the GW;
  - (ℓ_P; s = 1.2e-19 m; D = 0.75 Gpc), a 10 TeV photon proxy on the same substrate.

| Reading | Condition |
|---|---|
| **PASS** | Relative rms fluctuation < 0.1 at both points, and no dependence on the past beyond the source's causal past |
| **FAIL** | By the exact law, relative rms ≥ 1 at either point, or the variance diverges with the depth of the past |
| **INCONCLUSIVE** | No exact or controlled law |

**Decides:** whether class II survives N for gravity and light with one reading.

### Test 2 (class I, a few days): does the hypercubic tick keep one graviton speed under interactions?

- **Setting.** K7a's staggered h on Z⁴, coupled to lattice QED through the best available stress (K3a's optimized range-R stress).
- **Compute.** The O(e²) induced graviton quadratic action at O(q²), decomposed into the 9 W(B4) two-derivative forms. Report the 5 forms that are not gauge invariant, relative to the gauge-invariant one, converged in L. This extends K3a″'s machinery to non-uniform h.

| Reading | Condition |
|---|---|
| **PASS** | All 5 vanish at O(e²) (< 1e-6 relative). Keeping the grid still costs only the two shear tunings |
| **FAIL** | Any of them ≥ 1e-4 relative. Keeping the grid also costs graviton-speed tuning to the GW170817 level, so the price is ≥ 3 independent tunings, worse than "a second CC problem" |
| **INCONCLUSIVE** | Otherwise |

### Test 3 (finite-valency loophole of BHS): run here as check c5, bounded FAIL, unrefereed

- **Readings fixed for the extension:**

  | Reading | Condition |
  |---|---|
  | **PASS** | sd·√N of the per-site TT stiffness falls with N (S(0) = 0), or is ≤ 5e-11 |
  | **FAIL** | Flat in N and ≥ 1e-3 |
- **Result.** For the scalar with the proper-distance kernel it is flat over 16× in N, at about 0.06: **FAIL**.
- **Cheap remaining step (hours):** a frame-sensitive fermion sea and a second kernel, plus the codex referee. A confirmed FAIL removes "finite valency with symmetry only in law" as a class. The survivors would then be I (pay), II (unbounded valency) and III/IV (gauge or spectral discreteness).

---

## 6. Plain summary

**In one sentence:** for gravity to work, the "atoms" of space must not act like a fixed coordinate grid. They must be either a random scatter of events in space and time with no favoured frame, or something whose grid is itself a matter of description rather than a physical fact.

- **What the data force.** Gravity's waves are massless to one part in about 1e51 of the Planck mass, travel at light speed to 1e-15, and pull on everything equally to 1e-15. The known theorems turn those facts into one demand: the long-distance theory must have the gauge symmetry of Einstein's theory, plus one shared light speed.
- **A grid with fixed, readable positions is a crystal.** A crystal resists being sheared, and that resistance is a graviton mass. No rotation symmetry, however large, can forbid it; only the gauge symmetry can. The allowed resistance is below (124 eV)⁴, about 1e-104 of its Planck-scale size, so keeping the grid means fine-tuning two numbers that far.
- **"Symmetric on average" is not enough.** Every random or patternless grid tested is unstiff on average but carries a random stiffness in each actual arrangement. That includes a 4D random lattice I checked here: about 0.06 per site, white noise. It would scramble light and gravitational waves from distant sources.
- **What would work.** Noise must reach waves only through gradient-type couplings, or the grain must exist only in quantum superposition, where momentum is conserved and nothing scatters.
- **One light speed needs space-time symmetry.** Without it, quantum effects split the speeds of different particles at about 1e-3. With Lorentz symmetry in a random grain, each grain point must connect to unboundedly many others.
- **Records as events help.** Read as events in spacetime, counted and ordered in time, records fit: the count measures volume, which naturally gives a cosmological constant of the right size, and order plus count is enough to read off geometry. Read as permanent objects sitting at sites, records hurt: they become a frozen grid with a rest frame.
- **No constraint on matter from records-as-events.** Those records cannot be "locks" on matter's state. At Planck density that would freeze or heat matter by more than 100 orders of magnitude.
- **Next tests.** The decisive next steps are:
  - an exact noise law for the event substrate (Test 1);
  - whether keeping the grid costs only two tunings or also a light-speed tuning (Test 2);
  - a referee on the closed 4D-random-lattice loophole (Test 3).