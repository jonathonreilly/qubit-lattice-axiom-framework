# C5 R18-12 report: relic edge quanta. How many can exist, and does the W7 anomaly or anything else bound them?

**Author.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). **Unrefereed.** Ran 2026-10-13 03:36Z to about 04:02Z. No repository file was edited (`git status` clean). No downloads and no web lookups. Every literature number is RECALLED.

**Scratch.** `S/` = `.../scratchpad/C5/R18-12/`. Every script runs in under 35 s at `OMP_NUM_THREADS=2`.
- `S/scripts/r1812_laws.py`: the laws. S(1.4), G(1.4) and D1(1.4, 1/√3) are copied from R14-1; `sublum_copy.py` is byte-identical to `scripts/C5/R14-1/sublum.py`. The photons are R8-5's form, ω² = Σd(q_j)².
- `S/scripts/r1812_kinematics.py` / `.out`: (a) one-photon decay margins; edge-photon decays; corner classes. Grid N = 48.
- `S/scripts/r1812_envelope.py` / `.out`: (a) all channels. These are min-plus lower envelopes on an N = 24 torus grid, covering pairs and multi-body neutral sets.
- `S/scripts/r1812_abundance.py` / `.out`: (0) the proof input for Theorem C′; (b) the relic abundance against T_RH, including T_RH ≥ 1/a; (c) the bounds.
- `S/recheck/`: the archived R18-8 (4), R16-12 (3) and R16-8 (2) runners were copied, their `.out` files moved aside, and each was rerun. All exit 0, and all 9 regenerated `.out` files are byte-identical (`recheck_log.txt`).

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` and `SUMMARY` are in `P/`. `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full. `vX` = `P/agents/C5_X_referee_verdict.md`. `refR18-8` = `scratchpad/C5/ref_R18-8/C5_R18-8_referee_verdict.md`. R18-8's referee verdict appeared during this run: CONFIRMED WITH CORRECTIONS, ANOMALY (`scratchpad/C5/ref_R18-8/REFEREE_VERDICT.md:1-3`).

**Read.**
- `AX`, in full.
- `TESTS`:
  - C5 method (`:2302-2320`);
  - R9-1 and its verdict (`:3600-3636`, `:3839-3847`);
  - R14-1 and its verdict (`:4781-4813`);
  - R16-8 (`:5341-5358`, `:5514-5525`, verdict `:5587-5591`);
  - R16-12 (`:5529-5549`, `:5654-5665`, verdict `:5900-5906`);
  - R17-2 (`:5749-5783`, `:5987-5997`, verdict `:6167-6170`);
  - R18-8 (`:6751-6778`, `:6943-6955`);
  - this item (`:6988-7019`).
- `SUMMARY` §17 (`:355-493`).
- In full: `C5_R18-8_report.md`, `refR18-8`, `vR16-12`, and the R16-12 report's population and prices sections (`:282-330`).
- Also: R14-1 report §6 (`:184-211`), and R8-5 report on the photon and coupling (`:126-147`) and Theorem B (`:44-49`).

**Labels.** proved = complete under stated hypotheses, unrefereed. checked = numerics here. suggested = argued, not proved. reading = interpretation. comparator = literature, RECALLED.

---

## 0. In plain words

1. **Edge quanta cannot all be cleaned up, in any grid law.** On a grid, momentum is only conserved up to a whole turn of the Brillouin zone. The usual name for that is "umklapp". It lets particles trade momentum, but it cannot make momentum vanish.
   - Take the momentum class of a zone corner, say (π,0,0). Some state in that class has the lowest energy, and that state can never decay, under any interaction that respects the grid (proved).
   - So every grid law has one of two things:
     - light copies of particles at the corners. That is the S law's mirror boxes, which R9-1 excludes for charged species (count once);
     - absolutely stable lattice-scale particles at the corners.
   - Umklapp only removes such a particle when it meets a partner carrying the opposite corner momentum.
2. **Which particle is the stable one depends on the law.**
   - **D1 Dirac matter:** the corner states are the Wilson doublers, with mass 0.095n/a (≈ 1.2e18 GeV × n at a = ℓ_P). They carry charge and have no Killing defect (Δ = 0), so they are inert for W7.
   - **G-type matter with R8-5's photon (or the plaquette photon):** the corner states are **zone-corner photons**, with energy 2, 2√2 and 2√3 (units of 1/a). They carry the full W7 defect, Q_D/E = −2 along each corner axis, and they sit at rest (group velocity 0). They are cold, Planckian, stable and W7-active (proved).
3. **Many other edge quanta do decay, quickly.**
   - With physical (tiny) masses and R8-5's photon, every sampled defect-carrying edge quantum of S and G matter has an open one-photon decay (an explicit final state, checked). Its lifetime is of order a/α ≈ 1e-42 s (suggested).
   - Two exceptions:
     - with the fastest allowed subluminal photon (ω = |q|), no state can emit any number of photons (Lemma L, proved);
     - the D1 world keeps about 18% of its matter edge states stable on the grid (1.53/a and up). The G world keeps all its edge photons stable on the grid.
4. **Relics cannot be removed once made.** At every temperature T ≤ 1/a, annihilation and conversion are slower than the expansion: Γ/H ≤ 4e-4 for gauge rates and ≤ 6e-3 for gravitational rates (checked, rate estimates). So whatever is made stays.
5. **How many can exist (bounded by the dark-matter density).** The bound is Ω h² ≤ 0.12, applied to stable corner-class relics:
   - initial abundance Y₀ < 3.8e-28 (doublers) and Y₀ < 1.8e-29 (corner photons);
   - from thermal production after reheating: T_RH ≲ 4–6e16 GeV (doublers) and T_RH ≲ 4–10e17 GeV (corner photons). The production prefactor was varied over 8 decades, and the corner-photon threshold over [2, π]/a (checked).
   - Reheating at T_RH ≥ 1/a overcloses the universe by factors of 1e23–1e27.
   - Standard inflation already caps T_RH below about 6.7e15 GeV (RECALLED, r < 0.036). That leaves relic abundances below e^{−348}. In standard cosmology, nothing is visible.
6. **The W7 anomaly itself bounds nothing.**
   - Even with relics making up all local dark matter, a lab body's far-field mass changes by at most about 3e-30.
   - The relic gas's own mass would be velocity-dependent at about V² ≈ 1.5e-6. No bound for that is computed or recalled here.
   - BBN and CMB energy-injection bounds do not apply: open decays take about 1e-42 s, and the stable states never decay.
7. **P-W7edge0 is not dynamical.** States carrying the W7 defect exist that can never decay (the G-world corner photons, proved), so "physical states carry no edge quanta" cannot follow from the grid dynamics. It is a condition on initial conditions and cosmic history: inflation plus reheating below about 1e16 GeV meets it with enormous margin.
8. **A gap the item's setting hides.** "Standard expansion" is not defined on a fixed grid. Translation-invariant dynamics keep every crystal momentum fixed, so nothing redshifts out of the edge. The usual redshift k → k/R is not even a well-defined map on the Brillouin torus (Lemma X, proved). If expansion did shrink lattice momenta somehow, every edge quantum would enter the box within one e-fold (self-cleaning by redshift). That needs a law the Lattice axiom does not supply.
9. **Worker reading: BOUNDED** (for observable (ii), the dark-matter energy density), conditional on the stated hypotheses (§1) and Lemma X's fixed-grid reading. SELF-CLEANING is not met: Theorem C refutes the expectation's "cannot be stable".

---

## 1. Hypotheses and classes (stated before any title)

- **H-law.**
  - Matter: one-band box laws with b = 1.4. These are S(1.4) and G(1.4) scalars, with whole-zone v_max 0.99270 and 0.99386 at m = 0.3 (`vR16-8` via `C5_R18-8_report.md:39`), and the D1(1.4, 1/√3) Wilson Dirac, with v_max 0.9950 at m = 0.3 (`C5_R14-1_report.md:195-197`).
  - Masses: m = 0.3 (the registered lattice-scale test mass), and m = 0 or 0.01 for physical particles (m·a ≪ 1).
  - Photons (transverse; R8-5's form, `C5_R8-5_report.md:126-131`):
    - R85: d = ρq + (1−ρ)2 sin(q/2), plateau [1, 2];
    - std: d = 2 sin(q/2);
    - max: d = |q|, the pointwise upper envelope of the subluminal nondecreasing class (d′ ∈ [0,1]; kink at π);
    - min1: d = min(|q|, 1), the lower envelope with box |q| ≤ 1.
  - All photon laws are subluminal.
- **H-int.** Peierls coupling (R8-5, `:133-137`). It conserves charge and **crystal momentum mod 2π**; nothing else is conserved. Its vertex is generically nonzero between edge and box states (the Ward identity fixes the longitudinal part to the energy difference). Interactions are weak (α ≈ 1/40 at the lattice scale, RECALLED). Spectra are free, plus perturbative shifts.
- **H-sector.** Dynamics is translation-invariant at all times. That includes a homogeneous gravitational background, entering through the registered linear coupling ½h_ijT^ij with translation-covariant symbols.
- **H-cos.** Standard radiation-era expansion for the bath, with T_RH as a parameter measured against a fixed 1/a, g* = 106.75 and a = ℓ_P (`AX:189-190`: a reading). The tension between this and H-sector is Lemma X.
- **Edge.** Per the item (`TESTS:6997`), a state is "edge" if some |k_i| > b. The W7 source is the subset with Δ ≠ 0 (R18-8 Theorem A, `C5_R18-8_report.md:63-70`).
  - **Correction to the item's premise** (`TESTS:6994`): "Edge quanta are Planckian (≥ 1.4/a)" holds only for the defect-carrying subset (`vR16-12:19`). Under the item's own definition, edge quanta also include:
    - the D1 corner doublers, at m + 0.095n (`C5_R14-1_report.md:203-208`);
    - the S mirror boxes, at mass m (`TESTS:4810`).
    Both have Δ = 0 (checked, `r1812_kinematics.out` (C)).
- **Not covered:**
  - a lattice graviton band (its corner states could be lighter);
  - SM content with many species. Theorem C's dichotomy still holds there, but which species owns each corner class is not computed;
  - confinement (coloured doublers);
  - matrix elements and actual decay widths (only kinematics);
  - strong coupling;
  - translation breaking by records or defects (§3.6);
  - nonlinear gravity.

## 2. Prior art (each counted once)

1. **R18-8 and its referee.**
   - The asymptotic algebra fails by Q_D at degree 2, which meets ANOMALY (`TESTS:6943-6955`; `refR18-8:159-169`).
   - The observable √(E²−P²) is a frame-dependent translation-charge functional, observable only under the ADM/source/readout bridge (`refR18-8:132-157`).
   - P-W7edge0 is an "initial-state/domain condition", not derived (`refR18-8:171-176`). This report supplies the dynamical reason it cannot be derived (Theorem C).
2. **R16-12 and its verdict.** The defect floor is 1.431782/a = 1.748e19 GeV at m = 0.3. Number-conserving matter may keep an arbitrary initial edge population (`vR16-12:19`).
3. **R16-8 and R17-2:** the W7 tail and the dressing (count once; used only through R18-8).
4. **R14-1.** S has seven exact corner valleys. D1 doublers are about 20× lighter than R8-5's (`TESTS:4810-4813`; `C5_R14-1_report.md:203-211`).
5. **R9-1.** The literal law's seven electron corner valleys add about 588 MeV to the Z width, which is EXCLUDED (`TESTS:3840-3841`). Reading: the same applies to the S mirror boxes of any charged species (count once). The G HARMLESS reading was not established, since normalization, cosmology and escapes were open (`TESTS:3842-3846`). Its referee also notes that crystal momentum is conserved in the instantaneous model (`TESTS:3847`). This item closes the population side for corner classes.
6. **R8-5 Theorem B.** Gauge invariance ties the soft photon to every charged mode, including the zone edge (`C5_R8-5_report.md:44-49`). This is the source of the virtual-edge remark in §3.6.
7. **SUMMARY §17** (`:397-413`): a periodic band cannot be relativistic on the whole torus. This is why edge states exist at all (count once).
8. **Comparators (RECALLED).**
   - Crystal momentum and umklapp. Zone-boundary phonon stability under subadditive dispersions: anharmonic decay needs a softer branch.
   - Freeze-in and freeze-out.
   - Griest–Kamionkowski unitarity: thermal relics above about 100 TeV overclose.
   - Planck 2018: Ω_DM h² = 0.12.
   - BICEP/Keck 2021: r < 0.036, so V^{1/4} < 1.6e16 GeV.
   - Local ρ_DM ≈ 0.4 GeV/cm³.
   - MICROSCOPE: η ≲ 1e-15.

---

## 3. Results

### 3.1 Probe (a): number-changing processes

**Symmetry (proved, elementary).** Peierls coupling conserves charge and crystal momentum mod 2π, and nothing else. No selection rule forbids edge → box transitions: the vertex V_j(k+q,k) is nonzero whenever h_j(k_j) ≠ h_j(k_j+q_j). Umklapp, however, only relates momenta that differ by 2π. A single edge quantum at K cannot become a box quantum by itself, because K + 2πn never lies in the box. Every edge → box process must hand K − k′ to other quanta, and that costs energy. **The question is purely kinematic, plus the sector argument below.**

**Theorem C (corner-class ground states; proved).**
- **Hypotheses.** H-sector, with energy conserved. Let K_c ∉ 2πZ³, e.g. a zone corner. Let E_c = inf spec(H) on the sector of total crystal momentum K_c and fixed charges.
- **Statement.** The ground state of that sector cannot decay, under any interactions satisfying the hypotheses. Every lower-energy state has a different crystal momentum or charge.
- **Removal.** Its number can change only through encounters with quanta whose total crystal momentum is ≈ −K_c (mod 2π, up to the box): a second corner-class quantum, or partners carrying lattice-scale momentum. In a bath at T ≪ 1/a, such partners cost energy ≥ (box ratio)·|K_c|_T.
- **Dichotomy.** Either E_c ≈ 0, meaning light corner copies (the S mirror boxes; R9-1 EXCLUDED for charged species), or a Planckian stable state exists in every corner class.

*Proof.* The sector is invariant under H. Its ground state has no lower-energy state with the same quantum numbers, so no transition conserves both energy and crystal momentum. ∎ The content lies in identifying the ground states, below.

**Theorem C′ (which state; proved for the free spectrum; perturbatively stable).**
- **(i) G world.** G(1.4) matter of any m ≥ 0, plus the R85 or std photon. Every quantum obeys E(k) ≥ (2/π)|k|_T:
  - h(k) ≥ 0.7228k (h concave, h(π) = 2.27);
  - d(q) ≥ 2 sin(q/2) ≥ (2/π)q;
  - the bound extends to Euclidean norms componentwise.

  The torus metric obeys the triangle inequality, so **every** multi-quantum state with total K has E ≥ (2/π)|K|_T. The corner photons γ(π,0,0), γ(π,π,0) and γ(π,π,π) have ω = 2, 2√2 and 2√3, which is exactly (2/π)|K_c|_T. They are therefore the sector ground states, and they saturate the bound only at the corners.
  - Their defect: Δ = −2ω on each corner axis, i.e. Q_D/E = −2 (`r1812_abundance.out` (0); checked).
  - Margins (checked): min E/|k|_T is 0.7240 for G (m = 0) and 0.6378 for the photons, against 2/π = 0.6366.
- **(ii) D1 world.** For D1 Dirac matter (m ≥ 0), take φ(k) = √(W² + s²) on an axis. Then:
  - φ ≥ k inside the box;
  - φ ≥ ~1.4 on the slab;
  - φ ≥ W_π on the mirror box.

  So any multi-quantum state with Σk_x ≡ π has E ≥ W_π, and the doubler d(π,0,0) is the ground state. The doublers at (π,0,0), (π,π,0) and (π,π,π) are stable, with masses m + nW_π (0.0953n at m = 0) and Δ = 0 (checked, `r1812_kinematics.out` (C) and `r1812_envelope.out`).
- **(iii) S world.** The corner classes are the light mirror boxes (energy m).

**Lemma L (no photon emission at the fast-photon envelope; proved).**
- **Statement.** Let L = sup|∇ε| be the matter Lipschitz constant on the torus, and suppose every photon has ω(q) ≥ L|q|_T. Then no state of that band can emit any number of photons.
- **Proof.** ε(K) − ε(k′) ≤ L|K − k′|_T ≤ L Σ|q_j|_T ≤ Σω(q_j). ∎
- **Where it applies.** It covers the "max" photon (d = |q|) for every subluminal S, G or D1 band. Pair channels need separate treatment: for S and D1 they open through light corner states, and for G they stay closed at K_c by Theorem C′(i).

**Checked (`r1812_kinematics.out` (A), (A2), (B); N = 48; 580 edge samples).**

| world (m) | photon | one-photon decay open: all edge / defect-carrying | lightest defect-carrying sample with no one-photon decay |
|---|---|---|---|
| S (0) | R85 / std / min1 | 0.67 / **1.00**; 0.995 / **1.00**; 0.71 / **1.00** | none |
| S (0.3) | R85 | 0.00 / 0.00 | 1.452 |
| G (0) | R85 / std / min1 | **1.00 / 1.00** for all three | none |
| G (0.3) | R85 | 0.81 / 0.83 | 1.529 |
| D1 (0) | R85 / std | 0.07 / 0.23; 0.56 / 0.92 | 1.424; 1.629 |
| D1 (0.3) | R85 | 0.00 / 0.00 | 1.442 |
| any (0, 0.3) | max | 0.00 / 0.00 (Lemma L) | 1.42–1.53 |

- **Edge photons** (R85; 170 samples): every one is grid-stable in the G world. Only 13–19% are grid-stable in the S and D1 worlds, where the others decay into light-corner pairs.
- **All channels** (`r1812_envelope.out`; N = 24 min-plus envelopes including pairs and ≥ 3-body neutral sets; m = 0.01):
  - G + R85 and G + std: **0 of 12493** matter edge states are stable, while **13481 of 13481** photon edge states are grid-stable and defect-carrying (lightest ω = 1.047, next to the photon box). The corner photons are the sector ground states.
  - D1 + R85: 2310 grid-stable defect-carrying matter edge states, the lightest 1.531 at K = (−π, −π/2, 0). Also 1854 grid-stable photon edges, and the doublers are the corner ground states.
  - D1 + std: 390 grid-stable defect-carrying matter edge states, from 1.544.
  - S + R85: no stable defect-carrying matter edge state; the corner states are light mirror copies.
- **Scope of "grid-stable".** It is evidence only, since finer final states could open a channel. "Open" is certified by an explicit final state at a grid point.

**Rates (suggested).** An open decay proceeds at Γ ~ α/a (vertex O(e), phase space O(1/a)), giving τ ~ 2e-42 s. Matrix elements are not computed.

### 3.2 Probe (b): relic abundance against T_RH

- **No removal after production** (`r1812_abundance.out` (3); checked as rate estimates).
  - For T ≤ 1/a, with partner density about 0.1T³: annihilation or conversion with σ ~ α²/M² gives Γ/H ≤ 4.0e-4 (doublers) and ≤ 9.1e-7 (corner photons); gravitational σ ~ a² gives Γ/H ≤ 5.8e-3. Each falls ∝ T below that.
  - Diffusion along the energy shell into the box by soft scatterings needs t/t_H ~ 1/(α² aT) ≫ 1 (suggested).
  - So any population present or produced is frozen: no freeze-out dilution, and no chemical equilibrium with the box at T ≤ 1/a.
- **T_RH < 1/a: freeze-in from the bath** (checked; prefactor κ scanned from 1e-6 to 1e2).

| stable class | M | production threshold | T_RH,max (Ωh² = 0.12) | W7 |
|---|---|---|---|---|
| D1 doubler, n = 1 | 0.0953/a = 1.16e18 GeV | pair, 2M | **4.2e16 – 6.3e16 GeV** (2M/T = 37–56) | inert (Δ = 0); charged |
| G-world corner photon (π,0,0) | 2/a = 2.44e19 GeV | single, E_th ∈ [2, π]/a. The lower end is the Theorem C′ bound on any state with K = (π,0,0); the upper end is three box quanta | **4.2e17 – 9.8e17 GeV** (π/a: 6.6–9.8e17; 2/a: 4.2–6.2e17) | Q_D/E = −2 |
| D1-world lightest grid-stable defect matter edge | 1.53/a | between M and 2M | 3.5e17 – 7.1e17 GeV | yes |

  Example at κ = 1: doublers give Ωh² = 7e-13 at T_RH = 3e16 GeV and 8e10 at 1e17 GeV. Corner photons give 2e-33 at 3e17 GeV and 2e5 at 1e18 GeV.
- **T_RH ≥ 1/a** (checked arithmetic; Y₀ is an assumption). Lattice-scale modes are O(1)-populated, Y₀ ∈ [1e-4, 1e-1], and the population is frozen by the Γ/H above. That gives Ωh² = 3e22–3e25 (doublers) or 7e23–7e26 (corner photons). **Excluded by 1e23–1e27.**
- **Standard inflation** (RECALLED). r < 0.036 gives T_RH ≤ 6.7e15 GeV (instant reheating, g* = 106.75). The Boltzmann exponents there are 348 (doublers) and 5735 (corner photons). Gravitational production during inflation is ~exp(−2πM/H_inf) with H_inf ≲ 5e13 GeV, i.e. ≲ e^{−1e5} (comparator, RECALLED).

### 3.3 Probe (c): bounds from observables (i)–(iv)

- **(ii) Dark-matter energy density: the operative bound** (checked). Stable corner-class relics need Y₀ < 3.8e-28 (doublers) or Y₀ < 1.8e-29 (corner photons), equivalent to the T_RH,max values above.
  - Charged doublers face stronger heavy-isotope and charged-relic limits (RECALLED, qualitative, not used).
  - Corner photons are cold (v = 0), stable and Planckian. They are a possible Planck-mass dark-matter component if Y ≈ 1.8e-29, which would need a tuned T_RH (≈ 4–10e17 GeV) or a tuned initial abundance. That is a lead (suggested), not this item's reading.
- **(i) The W7 mass anomaly: no bound.**
  - A lab body sitting in relics at the full local DM density has an edge mass fraction ≤ 1.8e-25. With |Q_D/E| ≤ 20, that gives |δM/M| ≤ 2.7e-30 at the Earth's CMB-frame speed, against η ~ 1e-15 (checked arithmetic). The relics are neutral or lattice-scale-coupled and do not bind into matter (suggested).
  - The relic gas's own far-field mass varies as δM/M = −V² ≈ −1.5e-6 along a corner axis (from R18-8's formula with Q = −2E). Per `refR18-8:132-157`, this is a frame-dependent ADM translation-charge combination, observable only under that bridge. No bound is known here.
- **(iii) Matter-sector LV bounds (RECALLED): no bound on relics.** They constrain box physics, which is exact for free laws. A possible link through virtual edge content is in §3.6.
- **(iv) BBN and CMB energy injection: no bound.**
  - Open decays take about 1e-42 s. Sector ground states never decay. Today's annihilation rate is ∝ n²α²/M², which is negligible (suggested).
  - A slow-decay window (1 s to 1e25 s) would need crystal-momentum violation (§3.6).

### 3.4 Probe (d): is P-W7edge0 dynamical?

- **No (proved for the G world).** The corner photons carry Δ = −2ω and are the ground states of their sectors (Theorem C′(i)). No translation-invariant dynamics can remove them except pairwise.
- In the D1 world the corner classes are W7-inert. Defect-carrying matter edges from 1.53/a and photon edges are grid-stable (evidence, not proof).
- So "physical states carry no edge quanta" is not a consequence of the dynamics. It is an initial-state or history condition, matching `refR18-8:171-176`.
- **What does enforce it (reading):** inflation dilutes any earlier population, and reheating below about 1e16 GeV regenerates at most e^{−348} (doublers) or e^{−5735} (corner photons). P-W7edge0 thus holds in standard cosmology "to all practical purposes". That is a fact about the history, which the four axioms do not supply (`AX:181-185`: formation site and rate are downstream).
- **Defect-carrying matter edges in G and S worlds** (physical masses, R85, std or min1 photons) all have open decays (checked). For those, absence of real quanta at late times is dynamical. The exception is the "max"-photon envelope (Lemma L).

### 3.5 Lemma X: expansion on a fixed grid (proved; scope)

1. **Under H-sector**, a free quantum's crystal momentum is constant in time, whatever the homogeneous background h_ij(t), since [T_a, H(t)] = 0 for every lattice translation T_a. So edge quanta do not redshift out of the edge.
2. **The redshift map k ↦ k/R (R > 1) is not a map on the torus.** It does not commute with k ↦ k + 2πn. Any continuous self-map of T³ whose image lies in the box (a contractible set) has degree 0, so it is not invertible.
3. **Reading.** "Standard expansion" acting on lattice-scale crystal momenta therefore needs a law outside the registered setting: site creation, a non-comoving grid, or a dissipative map. That touches Lattice (`AX:37-41`, fixed Z³ sites) and the open time-metric and dynamics gates (`AX:185-186`).
4. **If such a law existed,** a continuous contraction would bring every edge quantum into the box after expansion by a factor ≤ π/b = 2.24, about 0.8 e-fold. That would be **self-cleaning by redshift**.
5. **This report's choice.** It treats the bath in the standard way, at fixed 1/a, while the edge classes keep their crystal momentum. That is the registered setting's reading. Lemma X shows the setting is not fully specified at the lattice scale.

### 3.6 Escapes and caveats (suggested)

- **Translation breaking.** Records (`AX:77-83`) or lattice defects that break exact translations would let crystal momentum relax by impurity-type scattering. That removes Theorem C's protection and could open slow decays, which would bring (iv) into play. The setting is translation-invariant, so this is outside it.
- **Virtual edge content.** By R8-5 Theorem B, interacting dressed states carry O(α) virtual edge admixture. If that gives ⟨Q_D⟩ ≠ 0 for dressed box particles, it is the e–γ speed-split already priced (F2/R8-5/R13-7/R16-10; count once). Not computed. R18-8's Theorem A is for free matter.
- **Many species.** With SM content, each corner class's ground state is the lightest state across all species in that class. Theorem C still guarantees one per class. Whether it is W7-active depends on the species' corner energies; the gravitons' are unknown.

### 3.7 Probe (e): prices (named, not adopted)

| price | content | axiom touched | buys |
|---|---|---|---|
| **P-r1812a (new): corner dichotomy** | Every grid law pays one of: (α) light corner copies (S mirror boxes; R9-1 EXCLUDED for charged species), or (β) absolutely stable lattice-scale corner relics (D1 doublers, G-world corner photons) | Lattice `AX:37-41` (crystal momentum comes from Z³); Admissibility range `AX:57-61` | — (a necessity, Theorem C) |
| **P-r1812b (new; = P-W7edge0 made concrete)** | Cosmic history keeps stable corner-class relics below Y₀ < 3.8e-28 (doublers) and 1.8e-29 (corner photons), i.e. T_RH ≲ 4e16 GeV (D1 world) or 4e17 GeV (G world); met by inflation + T_RH ≤ 6.7e15 (RECALLED) | none (initial and history condition); formation and dynamics downstream, `AX:181-186` | no overclosure; no W7 relic content |
| **P-r1812c (new; conditional)** | An expansion law that dilates lattice crystal momentum, which would self-clean by redshift | Lattice `AX:37-41` (sites or comoving grid); time and dynamics gates `AX:185-186` | SELF-CLEANING for every T_RH |
| P-W7anom, P-W7edge0 (R18-8) | Unchanged. P-W7edge0 is now shown non-dynamical (§3.4) | as cited | — |
| R14-1's Wilson-gap price | D1 doublers are charged stable relics at 0.095n/a; now with a cosmological bound | count once | — |

---

## 4. Against the FIXED readings (`TESTS:7015-7018`)

- **SELF-CLEANING: not met; the expectation's mechanism is refuted.**
  - Theorem C and C′ (proved) give absolutely stable edge-class states in every law without light corner copies.
  - Γ/H ≪ 1 at all T ≤ 1/a (checked estimate).
  - T_RH ≥ 1/a overcloses by 1e23–1e27 (checked arithmetic).
  - So "below every bound for any T_RH" fails within the registered setting. It would hold only under P-r1812c, an unsupplied expansion law.
- **BOUNDED: worker reading, met as follows (checked).**
  - Observable (ii), the DM energy density. It is violated above:
    - T_RH ≈ 4.2–6.3e16 GeV for D1-world doublers;
    - T_RH ≈ 4.2–9.8e17 GeV for G-world corner photons (the W7-active relics);
    - initial abundances Y₀ = 3.8e-28 and 1.8e-29.
  - Observables (i), (iii) and (iv) give no bound.
  - **Conditional on:** a = ℓ_P; α ≈ 1/40; g* = 106.75; the freeze-in rate form (κ bracket); H-sector; and Lemma X's reading for how the bath cools.
- **If the referee judges Lemma X's unspecified expansion law fatal to "standard expansion",** the fallback is OPEN, with Theorem C/C′, Lemma L and Lemma X as bounded results. The initial-population bound (Y₀) does not depend on T_RH physics and survives either way, given H-sector.
- **Against the expectation** (`TESTS:7019`: "SELF-CLEANING … they cannot be stable. The main risk is a conserved edge number in some sector"):
  - The risk is realized, in every law, as crystal-momentum sector ground states.
  - The expectation holds only for defect-carrying matter edges in S and G worlds at physical masses, which do decay.

## 5. Strong-word and rule check

- **"Proved":**
  - Theorem C: any translation-invariant, energy-conserving dynamics.
  - Theorem C′: free spectra; (i) G any m with R85 or std photons, (ii) D1 with m ≥ 0, (iii) S.
  - Lemma L: Lipschitz matter, ω ≥ L|q|_T, photon channels only.
  - Lemma X: homogeneous translation-invariant H(t); the dilation is not a torus map.
  - "No symmetry forbids edge → box."
- **"Checked":**
  - kinematic margins at grid points, which certify OPEN;
  - grid-stable fractions (evidence only);
  - the lower-bound ratios 0.7240 and 0.6378 against 0.6366;
  - corner energies and Δ;
  - freeze-in integrals and T_RH,max with the κ scan;
  - Γ/H arithmetic;
  - the 9 archived runners rerun, byte-identical.
- **"Absolutely stable"** means only: the ground state of its (charge, crystal-momentum) sector, under H-sector and the free or perturbative spectrum. It is not claimed against translation breaking or a lattice graviton band.
- **"Excluded"** (T_RH ≥ 1/a) is conditional on Y₀ ≥ 1e-4. Any Y₀ > 1.8e-29 is excluded for corner photons.
- **"Suggested":** decay rates of order α/a; diffusion times; that relics do not bind into matter; the virtual-edge link; the slow-decay window.
- **"Reading":** a = ℓ_P sizes; "to all practical purposes"; treating the bath as standard.
- **Round rules.**
  - v_max is stated for every matter law. All photon laws are subluminal (R85 has d′ ∈ [0, 1], checked).
  - No Ward or HDA statement is used beyond R18-8's, which is the standard algebra.
  - Forks: the "corner dichotomy" is exhaustive given H-sector. Its alternatives are E_c ≈ 0 or E_c > 0. It excludes translation breaking and non-Hamiltonian expansion (Lemma X).
- **Not claimed:**
  - widths;
  - SM multi-species corner assignments;
  - a graviton band;
  - charged-relic bounds beyond overclosure;
  - any W7 observational bound;
  - a derivation of inflation.

## 6. For the referee

1. **Theorem C′(i).** Is the triangle-inequality lower bound E ≥ (2/π)|K|_T valid for every multi-quantum state of the G + R85/std world, so that the corner photons are exact sector ground states? Does a perturbative interaction leave this intact?
2. **Lemma X.** Is the reading "bath standard, edge classes conserved" a fair rendering of the registered "standard expansion", or must the item fall back to OPEN?
3. **The κ bracket** for freeze-in, and the corner-photon production threshold bracket [2, π]/a.
4. **Whether BOUNDED via observable (ii) alone** meets "a stated observable is violated", with (i), (iii) and (iv) giving none.

## 7. Files (all in `S/`)

- `scripts/r1812_laws.py`, `scripts/sublum_copy.py` (byte-identical to R14-1's `sublum.py`).
- `scripts/r1812_kinematics.py` / `.out`: (A) one-photon margins, (A2) axis lines, (B) edge photons, (C) corner classes.
- `scripts/r1812_envelope.py` / `.out`: all-channel lower envelopes, N = 24.
- `scripts/r1812_abundance.py` / `.out`: (0) proof inputs, (1) freeze-in and T_RH,max, (2) T_RH ≥ 1/a, (3) Γ/H, (4) observables (i) and (iv).
- `recheck/`: R18-8, R16-12 and R16-8 runners rerun; `recheck_log.txt` shows all 9 identical.
