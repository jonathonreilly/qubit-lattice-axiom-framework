# C5 probe O4: what records may lock (worker report)

**Worker:** Claude Opus 5.5 (same family as the supervisor). Not refereed.
**Run:** 2026-10-12, 10:58Z to about 11:15Z.
**Scratch:** `scratchpad/C5/O4/`. It holds `o4_numbers.py` and `.out` (all arithmetic) and `o4_coarse_check.py` and `.out` (the coarse-graining factor). Nothing was downloaded. No repository file was edited.
**Readings used:** DERIVED, SUGGESTED, REFUTED (C5 fixed readings, `TESTS.md:2314-2318`).

## Verdict in plain words

- **DERIVED (Lemma 1).** A record that is permanent and readable acts as a classical which-way detector on anything its content depends on. Interference between two branches can be no larger than the overlap of the record distributions in those branches.
- So every observed interference experiment is a bound on records. Molecules above 25 kDa, clusters above 170 kDa, atoms coherent for 70 s, ions coherent for an hour, and Bell tests over km are all bounds of this kind.

Three results follow.

1. **Records cannot lock spacetime microstructure that responds to matter (DERIVED, under the count = volume hypothesis H3).**
   - Suppose the events are records at Planck density, and their count tracks the matter-sourced volume element.
   - Then a mass m held in two places a distance d apart loses coherence by −ln V ≥ (2π/3)(d/λ_C)², even with one record count for the whole experiment. Here λ_C = ħ/mc. G cancels.
   - This is about 10²⁷ e-folds for 25 kDa molecules and about 10²⁴ for the 70 s cesium interferometer.
   - Microstructure that does *not* respond to matter, but does steer propagation, gives per-realization noise instead. That is lane RZ's controlled FAIL.
   - Microstructure that does neither carries no geometry.
   - **So the geometry's microstructure must be unrecorded** (it must be a possibility, not a record), except as a copy of matter that is already recorded.
2. **"Gauge-invariant" and "conserved" are not enough (DERIVED / SUGGESTED).**
   - Records of a local gauge-invariant field strength, taken at the field's own quantum resolution, decohere a charge at a rate that does not depend on record density. This rate is the difference-field energy over ħ: the Diósi–Penrose structure.
   - For gravity this near zone is excluded by the underground X-ray bound. For electron interference it is about αcT/(4d), which is ≫ 1 for the illustrative biprism parameters (reading).
   - Records of local conserved quantities (energy, spin) inject no heat. They still kill observed energy and spin superpositions: clocks, and ion qubits coherent beyond an hour.
3. **What may be locked.**
   - (a) Data whose alternatives the environment has already decohered ("records copy, never measure"). This costs no heat and no visible decoherence, at any rate (DERIVED).
   - (b) Superselection labels of regions that enclose every coherent branch, such as the total charge read from the Gauss flux (DERIVED).
   - (c) Matter-independent occurrence that does not steer any amplitude (DERIVED, but it carries no physics).
   - (d) At most a small budget of fresh position records on matter, GRW-flash-like. They must be coarse (resolution a ≳ 0.1 µm) and rare: at most about 5×10⁻¹¹ s⁻¹ per nucleon at a = 0.1 µm from Earth heat flow alone. That is at most about 3×10¹⁹ m⁻³ s⁻¹ in water, a fraction of about 10⁻¹²⁸ of Planck-density events (DERIVED arithmetic; the model is a Gaussian lock).
4. **Bell (DERIVED, Bell's theorem plus loophole-free data).**
   - Records cannot be drawn independently, site by site, from any local data, including local reduced quantum states.
   - The joint law of space-like separated records must be non-factorizable (and no-signalling).
   - This is a constraint on Admissibility's distribution clause as read with Record. It is flagged for O5.

**Minimal rewrite, named as a price (not adopted):**
- **P4′ "Records copy, never measure":** a record locks a possibility only of alternatives that are already distinguishable outside the site.
- **Corollary P4-g:** which events exist and neighbour which is a possibility, not a record.
- **Variant P4′-f:** "rare coarse flashes", with the quantitative budget of item 3(d).

**Against the registered expectation** (`TESTS.md:2366-2369`). The expectation was "DERIVED: records cannot lock the spacetime microstructure … restricted to coarse, gauge-invariant or conserved data."
- **Confirmed** for the microstructure, with a sharper and G-independent mechanism.
- **Corrected** on "gauge-invariant or conserved": local gauge-invariant fields and local conserved densities are excluded too. Only superselection labels of enclosing regions, already-decohered pointer data and a bounded flash budget survive.
- **Corrected on mechanism for lensed light:** matter-independent records do not decohere it. They noise it (RZ).
- **Coarse counts:** coarse-graining helps only as (d/λ_C)²(cT)²/(ℓ_c·cτ_c). The count cells must be at least about 10 kpc (25 kDa) or about 2 Mpc (Cs, 70 s) across.

---

## 0. Hypotheses

- **H0 (reading of Record).**
  - "Permanent" means a record is never erased.
  - "Readable, readout determined by record content alone" means distinct record contents are perfectly distinguishable in principle. Formally, record states for distinct contents are orthogonal (classical).
  - This is a reading of `MINIMAL_AXIOMS_2026-06-29.md:79-83`, not axiom text.
- **H1.** Unrecorded degrees of freedom obey ordinary quantum mechanics: amplitudes, the Born rule, unitary evolution between record formations. This is the scope in which the observed visibilities are interpreted.
- **H2.** Observed visibilities agree with environment-only predictions within a tolerance δ. Fein et al. report about 90% of the expected visibility. Collisional and thermal-emission decoherence were measured quantitatively. I use δ ≈ 0.1–1 e-fold as the allowed extra loss.
- **H3 (count = volume; used only in section 3).**
  - Records are events at density ρ = ℓ_P⁻⁴ per 4-volume (x⁰ = ct).
  - The count in a cell defined independently of the superposed mass (for example, by decohered laboratory or astronomical matter) is Poisson, with mean ρ × (the matter-sourced 4-volume).
  - The weak-field Newtonian-gauge volume element is √−g = 1 − 2Φ/c².
  - This is the B2 candidate wording "their number: one per unit of spacetime volume" (`B2_report.md:190`). It is also what C3 G-L sprinkles: "a fixed curved metric, using that metric's true causal order" (`C3_G-L_report.md:136`).
- **H4.** Heating budget: Earth's total heat flow, 47 TW / 5.97×10²⁴ kg = 7.9×10⁻¹² W kg⁻¹, which is 1.3×10⁻³⁸ W per nucleon. This is generous, since the radiogenic part is not subtracted. B used about 7×10⁻¹² W kg⁻¹ (`B_referee.md:101-103`).
- **H5 (Bell).** Measurement independence, single recorded outcomes, no retrocausality.

## 1. Observations used

Two labels mark the source: "checked" means confirmed by a web search this run; "recall" means from memory.

| Observation | Numbers | Source | Use |
|---|---|---|---|
| Molecule interferometry, Fein et al. 2019 (Arndt group, LUMI) | about 2000 atoms, > 25 kDa, de Broglie wavelength down to 53 fm, > 7 ms in superposition, about 90% of expected visibility, macroscopicity μ = 14.1; grating period 266 nm (recall), used as d | checked: Nature Phys. 15, 1242 (2019) | §3, §4 |
| Nanoparticle interferometry, Pedalino et al. (MUSCLE) | Na clusters of > 7000 atoms, > 170 kDa, μ = 15.5 | checked: Nature 649, 866 (2026), doi 10.1038/s41586-025-09917-9. d and T not verified; only (d/λ_C)² is used | §3 |
| Lattice atom interferometer, Panda et al. 2024 | Cs-133 spatial superposition held 70 s | checked: Nat. Phys. 20, 1234 (2024), arXiv:2210.07289. d is taken as 1 µm, a guess I could not verify | §3, §4. **Note:** C3 M-D calls this "Rb-87 at 70 s" (`C3_M-D_report.md:7`); the atom is cesium |
| Kovachy et al. 2015 | Rb-87, 54 cm, 2T ≈ 2.08 s (T recall) | checked: Nature 528, 530. The superposition reading is disputed (Stamper-Kurn et al., arXiv:1607.01454) | §3, shown but not load-bearing |
| Ion qubit | coherence > 1 h (¹⁷¹Yb⁺) | recall: Wang et al., Nat. Commun. 12, 233 (2021) | §4 (conserved-lock bound) |
| Loophole-free Bell | NV centres 1.3 km (Hensen 2015); photons (Giustina 2015, Shalm 2015); atoms 398 m (Rosenfeld 2017); superconducting 30 m (Storz 2023) | recall | §6 |
| Environmental decoherence measured | C₇₀ collisional (Hornberger 2003) and thermal-emission (Hackermüller 2004) decoherence match theory | recall | H2 |
| Collapse and heating bounds | Diósi–Penrose with the parameter-free R₀ excluded; R₀ ≳ 0.54 Å (Donadi et al., Nat. Phys. 17, 74). Majorana Demonstrator X-ray limit on white CSL (PRL 129, 080401, 2022; numeric λ not retrieved). Oppenheim et al. 2023 decoherence–diffusion trade-off for classical gravity (Nat. Commun. 14, 7910) | checked (the 0.54 Å figure is from a secondary source) | §4, §5 |
| Lensed and VLBI light | refereed in-packet: lane RZ FAIL at the controlled level for the event route with stable layer readouts and shared ℓ_k; about 44,000 e-folds of margin | `TESTS.md:2125-2154`, `RZ_referee.md` | §5 |

## 2. Lemma 1: a record is a classical which-way detector (DERIVED, exact under H0 and H1)

**Setting.** A system is in a superposition α|A⟩ + β|B⟩. While it is coherent, records form whose joint content r has distribution p_A(r) in branch A and p_B(r) in branch B.

By H0, the record states |r⟩ are orthonormal. The joint state is

α|A⟩Σ_r c_A(r)|r⟩ + β|B⟩Σ_r c_B(r)|r⟩, with |c_X(r)|² = p_X(r).

The system's coherence is αβ*Σ_r c_A c_B*. Its modulus is at most |αβ*| · BC(p_A, p_B), where BC = Σ_r √(p_A p_B) is the Bhattacharyya overlap.

Permanence forbids later erasure. So every later recombination has

**V ≤ V_env · BC(p_A, p_B).**

Special cases:
- **Poisson record counts with intensities λ_A(x), λ_B(x):** −ln BC = ½∫(√λ_A − √λ_B)² d⁴x. This is exact.
- **Independent weak records**, each with a shift s_r between branches in units of its spread: −ln BC ≈ Σ_r s_r²/8.

**Observation link (N1).** Every observed coherent superposition with visibility at the environment-predicted value (H2) bounds the records formed during it: −ln BC ≤ δ. Records may differ between branches only by an amount whose BC is within e^{−δ} of 1.

## 3. Theorem C: recorded geometry that responds to matter is a which-way detector (DERIVED under H3)

**Step 1.** Under H3, λ_X = ρ(1 − 2Φ_X/c²). So (√λ_A − √λ_B)² = ρ(ΔΦ/c²)².

**Step 2.** For a point mass displaced by d:

∫(ΔΦ)² d³x = G²m² ∫(1/|x−a| − 1/|x−b|)² d³x = 4πG²m²d.

- Fourier form: 16π²·2(1 − cos k·d)/k⁴, integrated over d³k/(2π)³.
- It uses ∫₀^∞(1 − sin u/u)/u² du = π/4. Numerically 0.78457 against 0.78540; `o4_numbers.out`.

**Step 3.** With ρ = c⁶/(ħ²G²), the fine-grained form is

**−ln V ≥ 2π (mc²/ħ)² (d/c) T = 2π (d/λ_C)² (cT/d).**

**G cancels.** The weak signal per record, of order Gm/(c²r), is paid for exactly by the Planck density.

**Coarse-graining.** Suppose only counts in cells of size ℓ_c ≫ d and duration τ_c ≥ T are recorded. The far-field dipole sum gives

−ln V ≈ k_near · (2π/3) (d/λ_C)² (cT)²/(ℓ_c · cτ_c).

The near-cell factor k_near was checked numerically at 1.27–3.14, depending on where the pair sits in its cell; it is ≥ 1 in every case run (`o4_coarse_check.out`). The minimal case is one count over a cell the size of the experiment (ℓ_c = cτ_c = cT): −ln V ≥ (2π/3)(d/λ_C)².

| Experiment | λ_C (m) | (2π/3)(d/λ_C)², one cell | Fine-grained −ln V | Cell size ℓ_c = cτ_c needed for −ln V ≤ 0.1 |
|---|---|---|---|---|
| 25 kDa molecule (d = 266 nm, T = 7 ms) | 8.5e-21 | 2.1e27 | 4.9e40 | 3.0e20 m (about 10 kpc) |
| > 170 kDa cluster (d about 133 nm) | 1.3e-21 | 2.4e28 | — (T not verified) | — |
| Cs, 70 s (d = 1 µm, guessed) | 1.6e-18 | 8.3e23 | 5.2e40 | 6.0e22 m (about 2 Mpc) |
| Neutron crystal interferometer (d about 1 cm, T = 25 µs) | 2.1e-16 | 4.8e27 | 1.1e34 | 1.6e18 m (about 50 pc) |
| Rb, 54 cm (disputed) | 2.4e-18 | 1.0e35 | 3.6e44 | 6.3e26 m (more than the Hubble radius) |
| Electron (illustrative: d = 10 µm, T = 0.6 ns) | 3.9e-13 | 1.4e15 | 7.6e19 | 2.1e7 m |

**Scope and what is not proved.**
- The H3 cell is defined independently of the superposed mass.
- A fully relational version (counts of causal intervals between events on decohered apparatus, or proper-measure grids) reaches the matter only through the spatial curvature inside the region: linearized static ³R = 16πGρ_m/c², the "excess radius". A Cauchy–Schwarz estimate gives the same scaling (d/λ_C)²·(cT/R)·O(1) at best. **SUGGESTED:** the O(1) factor of the relational version was not computed.
- A causal order that is *also* recorded can only add information (data processing), so it cannot weaken the bound.

**Plain reading.** A Planck-density count, made permanent, measures the position of any mass to within its Compton wavelength in one experiment-sized cell. Observed interference has d/λ_C up to about 10¹⁴. So recorded count = volume geometry is excluded by 23 to 28 decades in the exponent, at every coarse-graining below kpc to Mpc cells.

## 4. Lemma 2: heat, and which locks are free (DERIVED)

**2a. Translation-covariant records on a free particle.**
- Records that decohere x-superpositions with function Γ(u) per unit time are a random-kick channel. The kick distribution is the Fourier transform of e^{−Γ(u)}.
- So dE/dt = (ħ²/2m)∇²Γ|₀ exactly.
- A Gaussian lock of resolution a gives ΔE = 3ħ²/(8ma²) per lock and decoherence 1 − e^{−d²/8a²} per lock.

Decoherence and heat are tied. Fine locks are hot; coarse locks are cool but only decohere separations ≳ a.

| a | ΔE per lock | Maximum locks per nucleon per s (H4) | Maximum fraction of the Planck events in a nucleon volume (1.1e103 s⁻¹) |
|---|---|---|---|
| ℓ_P | 9.5e27 J (unphysical) | 1.4e-66 | 1.3e-169 |
| 1e-19 m | 1.6e9 MeV | 5.3e-35 | 4.8e-138 |
| 1 fm | 15.6 MeV | 5.3e-27 | 4.8e-130 |
| 1 Å | 1.6 meV | 5.3e-17 | 4.8e-120 |
| 0.1 µm | 1.6e-9 eV | 5.3e-11 | 4.8e-114 |
| 1 µm | 1.6e-11 eV | 5.3e-9 | 4.8e-112 |

- Cross-check: in the CSL convention at r_C = 0.1 µm this is λ ≤ 2.6×10⁻¹¹ s⁻¹.
- X-ray limits on charged-particle kicks (Majorana 2022) are stronger. The numeric value was not retrieved.
- B's matched figure of about 4×10⁻¹⁵¹ per event (`B_referee.md:103`) uses a different per-event energy model (a viability-map birth energy). Both say "essentially none".

Converting to "records touching matter per volume per time" (water, 6×10²⁹ nucleons m⁻³):
- at most about 3×10¹⁹ m⁻³ s⁻¹ at a = 0.1 µm;
- at most about 3×10¹³ m⁻³ s⁻¹ at 1 Å;
- at most about 3×10³ m⁻³ s⁻¹ at 1 fm (5.3e-27 × 6e29).

All of these must also obey the coherence bounds below, and the CSL-type limits on mass-proportional amplification for large objects.

**2b. Locks of a conserved quantity (DERIVED).**
- A lock of an observable that commutes with H injects no energy.
- It still decoheres superpositions of different values (Lemma 1).
- Observed: hyperfine-qubit coherence > 1 h, so at most about 3×10⁻⁴ s⁻¹ per ion on that qubit. Clock superpositions of energy eigenstates are seconds long or more.
- **So "conserved" is not a free pass.** A local conserved density is a which-way variable for energy and spin superpositions.

**2c. Locks of already-decohered alternatives (DERIVED).**
- If the environment has already made the branch states orthogonal (decoherence factor ≤ ε), a record of that pointer variable leaves the reduced state unchanged. It adds no heat and at most ε extra visibility loss.
- Records of this kind may form at any rate.
- This is the only unbounded class.

**2d. Records of a local gauge-invariant field at its quantum resolution (DERIVED in scaling, SUGGESTED in O(1)).**
- Suppose records of cell-averaged E (or ∇Φ) are made at vacuum-limited resolution, with ⟨E_ℓ²⟩ = κ′ħc/(ε₀ℓ⁴), at density ℓ⁻⁴.
- Then ρ_r/σ² = ε₀/(κ′ħc), **independent of ℓ**. So −ln V ≈ (T/8κ′ħ)·ε₀∫ΔE² d³x, which is the difference-field energy × T/ħ.
- **Charge, far zone:** about αcT/(4κ′d), which is 5 to 330 for the illustrative biprism parameters.
- **Gravity, far zone:** Gm²T/(4ħd), which is ≤ 10⁻¹⁷ (negligible).
- **Gravity, near zone:** Diósi–Penrose with R₀ = cell size. At R₀ = ℓ_P this gives about 10⁵ s⁻¹ per nucleon, with the matching heating. The parameter-free DP limit is excluded; R₀ ≳ 0.54 Å.
- **So gauge-invariant local fields may not be recorded at fine resolution either.**

## 5. The geometry trilemma, with RZ (DERIVED, within RZ's scope)

Any recorded spacetime microstructure is one of four kinds:
- **(I) Independent of matter, and steers propagation.** Per-realization noise follows. Lane RZ: controlled FAIL for lensed optical and radio light at 1 Gpc, with a margin of about 44,000 e-folds. C3 M-A and M-D give the matter analogue (M-INCONCLUSIVE, with conditional tension against 70 s, 2.3 s and qBounce).
- **(II) Depends on matter.** Theorem C excludes it, by 10²³ to 10²⁸ e-folds for atoms, neutrons, molecules and clusters, and by about 10¹⁵ for an illustrative electron.
- **(III) Independent of matter, and steers nothing.** It is harmless and carries no geometry ("occurrence and relations only", B's reconciliation (a), `B_referee.md:187`).
- **(IV) Depends on matter only through already-recorded matter (pointer) data.** It is harmless by Lemma 2c.
  - But then the gravity of an *unrecorded* superposed mass is not encoded per branch.
  - This is semiclassical-like for coherent sources. Gravity-mediated-entanglement (BMV-type) experiments would refute it if they succeed.
  - It is also bound by the Oppenheim et al. decoherence–diffusion trade-off whenever classical geometry couples to coherent matter.

**Necessity (N2).** Geometry-bearing microstructure must be a possibility, not a record. Only (III) and (IV) records of it are allowed. This is B2's fallback C wording (`B2_report.md:205`), now with numbers. It is also the premise of Q1, the coherent substrate. If Q1 FAILs, no recorded or unrecorded event microstructure in this class survives.

## 6. Bell constraint on how records form (DERIVED: Bell's theorem plus loophole-free data)

**Claim.** Suppose each record's content is drawn from a distribution fixed by data local to its site, independently of distant records given that data. Then the joint record statistics have the form P(a,b|x,y) = ∫P(a|x,λ)P(b|y,λ)dμ(λ), with λ the full local data. This holds even when the local data includes the unrecorded local reduced state. So they obey CHSH ≤ 2.

**Observed:** loophole-free violations.

**Necessary (N3).** The joint law of record formation at space-like separation must not factorize given local data. It must be a global (Born-type, no-signalling) law, as in relativistic GRW flash models, or the single-outcome premise must go.

**Consequence.** This conflicts with reading Admissibility's "for each site … determined by … the nearest-neighbor conditions" as the full conditional law of record formation. It is consistent only if that clause gives a marginal. This connects to P3, P7 and lane F's "Bell-causal" scope (`PRICE_NOTE.md:166-178`). Flag for O5.

## 7. Necessity statement

**N (DERIVED, under H0–H2, plus H3 for the geometry clause and H4 for the rates).** Records may lock only:
- **Y1:** possibilities whose alternatives are already decohered outside the site (pointer data; records copy, never measure), at any rate;
- **Y2:** superselection labels of regions that enclose every coherent branch (the Gauss-flux charge, baryon number);
- **Y3:** matter-independent occurrence data that enters no amplitude;
- **Y4:** at most a bounded budget of fresh matter-position records. The budget is per nucleon Γ(a)·3ħ²/(8m_N a²) ≤ 1.3×10⁻³⁸ W, plus Γ(d)·T ≤ δ for every observed (d, T), plus X-ray and CSL-type limits. In practice a ≳ 0.1 µm and Γ ≲ 10⁻¹¹ s⁻¹ per nucleon (fraction ≲ 10⁻¹¹³ of Planck events).

Records may **never** lock:
- the spacetime microstructure that tracks matter (−ln V ≥ (2π/3)(d/λ_C)² ≈ 10²³–10²⁸ for observed atoms, neutrons, molecules and clusters);
- matter-independent microstructure that steers propagation (RZ);
- local gauge-invariant field values at quantum resolution (difference-field energy × T/ħ);
- local conserved densities of coherent systems (ions > 1 h, clocks);
- individual matter phases, positions or spins at resolution finer than observed separations.

Their joint formation law must violate Bell factorization (N3).

**What is not proved:**
- the relational O(1) factor in §3;
- κ′ and the near-zone treatment in §4 2d;
- d for Panda et al. (a guess) and T for Pedalino et al. (not used);
- the numeric X-ray limits;
- RZ's own open items (edgeless sources, the scalar-to-photon transfer).

## 8. Minimal rewrite of Record, named as a price (not adopted; owner decision)

The current text is: "Records form. When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent." (`MINIMAL_AXIOMS_2026-06-29.md:77-80`)

**P4′ "Records copy, never measure" (SUGGESTED wording; the necessity behind it is DERIVED).**
> Records form. When present, a record locks exactly one admissible local possibility, **and only among alternatives that are already distinguishable outside the site; forming a record changes no unrecorded interference.** A site never carries more than one record; records are permanent. **Which sites exist and which neighbour which is a possibility, not a record.**

**Variant P4′-f "rare coarse flashes".** Replace the bold first clause with:
> records of matter possibilities form rarely and coarsely, at rates and resolutions below the bounds of §4

This gives a GRW-flash ontology. Definite outcomes then come from records themselves, rather than from a decoherence notion.

**What either variant costs:**
- P4′ needs a notion of "already distinguishable" (decoherence) inside the axioms. Today decoherence mechanisms are an open gate outside them (`MINIMAL_AXIOMS_2026-06-29.md:182-183`).
- With the B2 qualification, "a state is records **plus the wave over unrecorded possibilities**", the geometry clause makes the microstructure part of the wave. That is Q1's coherent substrate.
- N3 requires Admissibility's per-site distribution to be a marginal of a non-factorizing joint formation law. That is an Admissibility price, separate from this one.
- It replaces P4 "Records as events". Records-as-events at Planck density is excluded:
  - by Theorem C, if the event count tracks the curved, matter-sourced metric;
  - by RZ, if it does not and the events steer propagation.
- Under (III) and (IV), events may still exist as unrecorded possibilities.
- Consistent with B1 c4: the volume-law record entropy is 2.4e38 × S_BH (`B_referee.md:105`). Copy-only records are sparse.

**Referee targets:**
- Lemma 1 (H0's orthogonality reading);
- Theorem C's H3 and its relational version;
- Lemma 2d's scaling;
- N3's application to the Admissibility clause.

Sources: [Fein et al. 2019 (univie)](https://ucrisportal.univie.ac.at/en/publications/quantum-superposition-of-molecules-beyond-25-kda/), [Arndt group: Nature 2026 nanoparticles](https://arndt.univie.ac.at/detailview-news/news/publication-in-nature-1/), [Panda et al. arXiv:2210.07289](https://arxiv.org/abs/2210.07289v3), [Kovachy 2015 dispute arXiv:1607.01454](https://arxiv.org/pdf/1607.01454), [Donadi et al. arXiv:2111.13490](https://www.arxiv.org/pdf/2111.13490), [Majorana PRL 129, 080401 / arXiv:2202.01343](https://arxiv.org/abs/2202.01343), [Oppenheim et al. 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10696068/).
