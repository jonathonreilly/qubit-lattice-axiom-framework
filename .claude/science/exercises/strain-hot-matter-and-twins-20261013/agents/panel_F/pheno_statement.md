# Panel F, precision-phenomenology lens: grid stretching, the grid's extra mass, and the strain-covariant critical-mass rule

- **Lens:** precision phenomenologist and experimentalist. My tools are Lorentz-violation bounds (SME), equivalence-principle tests, clock comparisons, GW propagation, and orders of magnitude.
- **Worker:** Claude Opus 5.5. This is the same model family as the supervisor and every C5 worker, and the statement is unrefereed.
- **Run:** 2026-10-13, 18:25Z to about 19:00Z. No repository file was edited. Web search was used for observational bounds; nothing was downloaded.
- **Scripts:** one script, `pheno/pheno_sizes.py`, with output `pheno_sizes.out`. It is pure arithmetic in under 100 MB. I also ran one read-only call of the repo's `dirac.py` to get the D1 doubler mass.
- **Read:**
  - `docs/MINIMAL_AXIOMS_2026-06-29.md` (AX) in full;
  - the dossier;
  - `P/agents/C5_F2_report.md` in full, with `vF2`;
  - `rF1:1-140, 240-300`, with `vF1`;
  - `rR19-34:130-196`, with `vR19-34`;
  - `rR19-31:1-125` (grep);
  - `rR19-15:120-140`;
  - `TESTS:9322-9379` (F5);
  - `PRICE_NOTE:670-682`;
  - `scripts/C5/R18-5/dirac.py:1-60`;
  - `scripts/C5/R19-34/r1934_sizes.py`.
- **Path conventions:** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `rX` / `vX` = `P/agents/C5_X_report.md` / `_referee_verdict.md`. `out:` = `pheno/pheno_sizes.out`.
- **Labels:** proved / checked / suggested / reading / comparator. RECALLED means from memory. WEB means looked up in this run (sources at the end).

---

## PART 1: plain words

### The bottom line

1. **The size estimates hold up, and the main conflict is conservative.**
   - I re-derived Earth's |m_g| = 3.6e-9 eV and the 1.6e8 exceedance from the inputs.
   - The dependencies are the TT-pole bridge, grid spacing = Planck length, and an SM coupling estimate. To survive, the channel would need to be wrong by 10⁸, not by a factor of 10.
   - The 1.6e8 figure is if anything conservative. Requiring GW170817's lowest frequencies (about 20 Hz) to pass gives a bound up to about 20 times tighter.
2. **A second, independent observation hits the same term from the matter side, at about the same factor.**
   - The extra mass is ~1.5e25 eV × (stretch)² per electron. Pulsar timing sees a nanohertz gravitational-wave background with stretch ~1e-14 at Earth.
   - That background would make the electron's mass, and so the proton-to-electron mass ratio, drift by ~1e-8 per year.
   - Atomic clocks see less than ~4e-17 per year. The exceedance is about 2e8 (suggested).
   - This row does not need the graviton-mass bridge. It needs only "stretch on the grid = gravitational-wave strain" and Planck spacing.
3. **The rule removes nothing that is observed.**
   - In Einstein's theory, a particle's rest mass measured where it sits never depends on gravity. Every precision test agrees:
     - free fall is composition-independent to ~3e-15 (MICROSCOPE);
     - clocks see no mass-ratio change with the Sun's potential at the 1e-7 level, and no drift at the 1e-17/yr level;
     - electron Lorentz-symmetry tests reach ~1e-21.
   - The rule restores exactly that statement for fermion masses.
4. **The rule is incomplete as stated.** By far the largest gap: the Higgs mass² is even more sensitive to the grid (quadratically). The root fixes its counterterm at zero strain too (`rR19-31:62`), and its strain response is unprotected (`rR19-31:113`).
   - Estimate: without a matching rule, the Higgs vacuum value, and with it every particle mass, would shift by ~1e32 × (stretch)².
   - The nanohertz background alone would then move masses by O(1e4). That is excluded beyond any doubt (estimate).
   - The rule has to cover every grid-sensitive mass parameter, not just fermions.
5. **Verdict: sound with conditions.** The conditions are listed in Part 1 §3.

### 1. Jon's questions, answered from my lens

**(a) What is "grid stretching"?**
- The sites do not move. Z³ is fixed by the Lattice axiom (`AX:37-41`).
- "Stretching" is a long-wavelength change in how excitations hop. Under the registered SF rule, each band's momenta are moved by that band's own flow. A wave then travels as if lengths along x were slightly longer and along y slightly shorter (`rR19-15:127-138`). That is an effective metric field, i.e. the graviton, acting on how matter moves.
- The point that matters for experiments: because the grid is fixed, a *uniform* stretch is physically measurable relative to the grid.
  - In Einstein's theory a uniform stretch is just a change of coordinates and has no effect. Diffeomorphism invariance forbids any coupling to the undifferentiated metric.
  - Here nothing forbids it. The program's own continuum check says the protection exists only for a rotation-invariant regulator (the "relabelling Ward identity", `rR19-15:136-137`), and the lattice breaks it (`rF1` §0).
- So stretching is meaningful on Z³, and that is exactly why it is dangerous. Any response to undifferentiated strain is a Lorentz/equivalence-principle violation, which is what precision tests constrain. (reading)

**(b) Why does the grid give fermions extra mass?**
- A fermion placed naively on a grid comes with unwanted copies, called "doublers", at the corners of the momentum zone (Nielsen–Ninomiya: comparator, RECALLED).
- The root removes them with a Wilson-type term W. W is exactly zero for |k| ≤ 0.909/a ("box-exact"). It rises to W(π) = 0.355/a per axis, so the doublers weigh 0.36 to 1.07 times the grid energy, ~4e27 to 1.3e28 eV (checked, `out:B`).
- W multiplies the same matrix as the mass, so it breaks chiral symmetry (`rR19-34:12`). Chiral symmetry is what normally keeps fermion masses small. Without it, quantum (gauge-loop) effects give the light fermion an additive mass:
  - δm = 0.0419 e²/a (refereed, `vR19-34` item 2);
  - electron (e² ≈ 0.1): 4.2e-3 of the grid energy, i.e. 5e25 eV, or 1e20 × m_e;
  - quark (C_F g_s² ≈ 0.4): 1.7e-2 of the grid energy, i.e. 2e26 eV (checked arithmetic, `out:B`).
- **"About the grid's own energy scale" is overstated by 60–240×.** That description fits the doublers. The light fermion's shift is loop-suppressed to 0.4–2% of the grid scale. It is still "huge": the cancellation must be tuned to 1 part in 1e20 for the electron (`out:B`).

**(c) Sizes: grid vs fermion (a = Planck length 1.616e-35 m; checked, `out:A`)**

| object | length | grid sites across |
|---|---|---|
| electron, reduced Compton wavelength | 3.9e-13 m | 2.4e22 |
| u quark, reduced Compton wavelength (2.2 MeV) | 9.0e-14 m | 5.5e21 (but confined inside a proton) |
| proton, charge radius | 0.84 fm | 5.2e19 (6e59 sites inside) |
| top quark, reduced Compton wavelength | 1.1e-18 m | 7e16 |
| electron "size" (point-like to <~1e-18..1e-20 m) | — | still ≥ 6e14 |

- A fermion is an extremely smooth long-wave pattern spread over ~1e20 to 1e22 sites. Grid effects on how it *moves* are suppressed by (mass × spacing)²: ~1e-45 for the electron, invisible.
- The extra mass is different. It comes from quantum fluctuations at *every* wavelength down to the grid spacing, so it is not suppressed at all. That is why a particle 1e22 sites wide can still feel the grid at full Planck strength. (reading; standard power counting, comparator)

**(d) How is a fermion built on this grid?**
- It is supplied, not derived.
- The axioms give one qubit per site (`M_2(C)`, `AX:47`). They say Admissibility does not "assert a Dirac-square carrier" (`AX:120-122`), and they list the staggered-Dirac/Grassmann realization as an open gate outside the axioms (`AX:178`).
- The 4-component structure is a downstream band ansatz: h(k) = Σ c_a γ_a with c = (S_x, S_y, S_z, M) (`dirac.py:4-6`).
- The root places 22.5 Dirac fields on one such edge (`rR18-9:38`). That is the Standard Model's 45 Weyl fermions, put in by hand.
- The per-species couplings used in every size above (e², C_F g_s², nucleon σ-term weight 13) are Standard Model inputs, labelled ESTIMATE in `r1934_sizes.py:1-4`. (reading)

### 2. The pasted explanation: what is right, what is wrong

| phrase | verdict |
|---|---|
| "the grid tries to give them a huge mass, about the grid's own energy scale" | **Half right.** Huge, yes: 1e20 × m_e. "About the grid's scale" is the doublers; the light fermion's shift is 0.4–2% of it. |
| "The root already does this [cancellation] on the ordinary, unstretched grid" | **Right** (critical mass fixed at t = 0; `rF1` §1; `rR19-31:62`). |
| "as a passing gravitational wave or the strain inside the Earth does" | **Partly wrong.** The mechanism needs no strain inside the Earth. Rock is stiff against stretching, and the wave's *own* stretch is resisted. Whether the Earth's static field registers as stretch on the grid is a separate open question (Part 2 §T2, row S). |
| "Every fermion picks up a tiny leftover mass" | **Right but misleading.** Per particle it is tiny for a LIGO wave: 1e-17 eV at a stretch of 1e-21. But the coefficient is Planck-sized, ~1.5e25 eV × stretch² per electron. That coefficient is the problem. |
| "acts like a heavy 'drag' on gravitational waves" | **Wrong word.** Drag means friction and lost energy. This is stiffness, a spring: it gives the graviton a mass inside matter. Below a cutoff frequency the wave cannot travel and dies out within ~54 m (massive sign), or is mostly reflected (other sign; `rF2:65`). LIGO's band is 1e4 below the cutoff in rock (`out:C`). |
| "GW170817 could not have passed through the Earth … yet it did" | **Right** (F2 checked, referee-confirmed for the massive sign, `vF2` item 2). It is conditional on the bridge, Planck spacing and the SM mapping, and robust to factors of 10–100 in any of them. |
| "fermions stay exactly as light as they are, however the grid is stretched" | **Needs three corrections.** (1) It is the rest mass measured locally that stays fixed; motion still responds to the stretch, as gravity requires. (2) It covers only the grid-sized (additive) piece, not the small piece proportional to the fermion's own mass, and not the Higgs. (3) "Exactly" is imposed by the rule, not derived. Observation needs the leftover below ~6e-9 of the computed value, at all orders of perturbation theory. |
| "what Einstein's theory already says" (not in the pasted text; asked by the dossier) | **Right as a statement of the target.** In general relativity plus the Standard Model, a locally measured rest mass does not depend on gravity (the Einstein equivalence principle). GR gets this from a symmetry; the grid lacks that symmetry, so the rule puts it in by hand. |

**Corrected version (plain):**

> On a grid, an electron is a smooth wave spread over about 10²² sites. The grid is far too fine to see directly, but it causes one real problem. A fermion on a grid comes with unwanted copies. The root's law removes the copies by making them very heavy, near the grid's own energy scale, and the price is that the real fermion loses its protection against picking up mass. Quantum effects then give it a mass of about half a percent of the grid scale for an electron, and about 2% for a quark. That is still about 10²⁰ times the electron's actual mass. The law cancels it with a fixed correction, the "critical mass", tuned to one part in 10²⁰ on the unstretched grid.
>
> A gravitational wave here is a pattern in how things hop on the grid: a bit longer in one direction, a bit shorter in another. The sites themselves do not move. In such a region the grid's push on a fermion's mass changes slightly, and the fixed correction no longer cancels it. The leftover is about 10²⁵ eV times the square of the stretch. For a LIGO wave that is unmeasurably small per particle. But because the coefficient is that large, stretching ordinary matter costs a lot of energy: rock becomes stiff against stretching. A gravitational wave cannot travel through stiff material below a cutoff frequency, and LIGO's waves are about 10,000 times below the cutoff in rock. GW170817 reached both LIGO detectors through 9,000–11,000 km of Earth, so this stiffness is ruled out by a factor of about 10⁸. Atomic clocks give a separate exclusion of similar size. The slow background of gravitational waves seen by pulsar timing would make the electron's mass drift about 10⁸ times faster than clocks allow.
>
> The rule: let the correction follow the stretch, so that a fermion's rest mass, measured where it sits, does not change when space is uniformly stretched. Einstein's theory already requires this, and every precision test agrees with it. The grid does not provide it on its own, so the rule imposes it. The same treatment is needed for the Higgs mass, which is even more sensitive to the grid.

### 3. Verdict: **sound with conditions**

The rule removes nothing that is observed. It is needed, because two independent observations each exclude the uncorrected channel by ~1e8. It brings the law back into line with what every equivalence-principle and clock test sees. The conditions:

1. **It must cover the Higgs mass² as well** (and every other mass parameter that depends on the grid). Otherwise the matter-side vev shift is ~1e32 × stretch² (estimate, `out:F`), far beyond any clock bound. As written, the rule (fermion critical mass only) is incomplete.
2. **It must hold at all orders** (as F5 states). Two-loop pieces are only ~α_s/π smaller than one-loop pieces, and observation needs the leftover below ~6e-9 of the one-loop Hessian.
3. **Its vacuum knock-on must be absorbed by (Σ)**, so that the vacuum graviton mass stays below ~2e-23 eV. In grid units that is m_g²a² < 2e-102 (`out:G`). If (Σ) does not absorb it, the rule creates a near-Planck graviton mass in empty space.
4. **The residual "multiplicative" channel (∝ the fermion's own mass) needs a strong-field check.**
   - It passes the Earth row by 5e12.
   - But it is not negligible against gravity itself: it is ~2e-3 of gravitational strength.
   - It sits ~16× above F2's toy binary-pulsar row (suggested; z″ computed under H-cov only, `out:E`).
   - F5's expectation ("suppressed by m_f·a ~1e-22, far below") is right for the Earth row but understates the pulsar row.
5. **Statement form:** "the pole mass vanishes at m_c(h) for every uniform strain" (F5's form, units-free). It should not be read as "the mass in grid units is fixed under a uniform dilation", which would fight the units rescaling in `rR19-34:97`.

### 4. The strongest argument from my tradition, and the steelman against

**For.**
- Whatever the law, it has to reproduce the observed fact that rest masses do not care about gravity. That fact is tested at 1e-15 (free fall), 1e-17/yr (clock drift), 1e-7 (clock vs solar potential) and 1e-21 (electron anisotropy).
- An uncorrected Planck-size strain coefficient fails at least two independent tests (GW propagation through Earth; clocks under the nanohertz background) by about 10⁸ each. It would fail far worse if static fields register as stretch on the grid.
- The rule is the minimal, number-free clause that restores the observed fact for this channel. It removes nothing seen.

**Against (steelman).**
- The rule has no mechanism: it cancels a Planck-size effect exactly, at every strain, at all orders.
- It joins a growing list of clauses that each restore one piece of Einstein's symmetry by hand: (Σ) for the vacuum stiffness, (S_loc), the speed counterterms, now P-R19-34a, and next a scalar version.
- A list like that is evidence that the framework lacks the emergent symmetry (strain covariance, i.e. diffeomorphism invariance at long wavelength) that would make all of them automatic. Under "match observations", each clause is acceptable. Taken together, they reduce the gravity–matter sector to "whatever is observed, impose it", which predicts nothing.
- There is a cleaner-looking alternative: chirally symmetric fermions (staggered or Ginsparg–Wilson). They remove the additive mass, and hence its strain dependence, by symmetry rather than by clause. It is priced as "leaves the root" (`rR19-34` §6).
- F3 also shows the zero is reachable inside the law by a tuned dressing (a* = 0.014). The cancellation may then be a tuned number rather than a clause, with the same lack of explanation.

### 5. What would change my mind, and one next test

- **Toward "unsound":**
  - any observed environment dependence of rest masses (none seen);
  - the vacuum knock-on not absorbable by (Σ) without moving the refereed root rows;
  - no number-free local statement possible beyond O(a·∂h). Observationally, gradient terms are suppressed by (a/L)² ≲ 1e-60 and are harmless.
- **Toward "sound, no conditions":**
  - a computation showing the Higgs mass² is already strain-covariant on the root, or is covered by a registered clause;
  - the SF multiplicative channel passing a strong-field binary-pulsar calculation;
  - best of all, a symmetry derivation showing every mass parameter's strain Hessian vanishes. That would turn the rule from imposed to derived.
- **One next test (F6: the scalar analogue of P-R19-34a), specified in Part 2 §T4.**
  - Compute the Higgs mass²'s strain Hessian on the root's SF law.
  - Convert it to a vev shift per unit stretch².
  - Read it against clocks under the NANOGrav background, with the fermion channel as the control.
  - Pre-registered expectation: SCALAR-HAZARD by ≥1e20, so P-R19-34a must be generalized to all mass parameters.

---

## PART 2: technical

### T1. Do the size estimates hold up? (checked arithmetic, `pheno_sizes.out`)

| claim (dossier) | re-derived here | status |
|---|---|---|
| grid spacing vs fermion | electron 2.4e22 sites; proton radius 5.2e19; m_e·a = 4.2e-23 | checked (`out:A`) |
| δm ~ e²/a | root 0.0419 e²/a: electron 5.1e25 eV (4.2e-3 E_P), quark 2.0e26 eV (1.7e-2 E_P); tuning 1e-20 for the electron. Doublers 0.355–1.066 E_P (W(π) from `dirac.py` D1 at the R18-9 root) | checked; "grid scale" overstated 60–240× for the light mode |
| Earth \|m_g\| ≈ 3.6e-9 eV | 3.627e-9 eV from m_g²a² = 16π·n a³·w_N·c_h/4, with n = 3.3e30 m⁻³, w_N = 5.2, c_h = 4 × 2.42401e-2 | checked; = `vF1` item 3 (3.65e-9) |
| the 1.6e8 exceedance | μ_ρ = 2.39e-21 eV² m³/kg; /1.5e-29 = 1.59e8 | checked |
| physical picture | m_g²/(16πGρ) = 1.65e18 = (w_N c_h/4)·E_P/m_N: each nucleon's *Planck-size* strain Hessian stands where its mass stands in ordinary gravity | proved (algebra of the mapping) |
| robustness of the bound | decay length ħc/m_g = 54 m vs chords ~1e7 m (exponent ~2e5). m_g/ω = 4.4e4 at 20 Hz, 8.8e3 at 100 Hz. Requiring no evanescence at 20 Hz in the core (ρ ≈ 1.1e4) gives μ_ρ < 6e-31, ~25× tighter than F2's SNR-weighted 1.5e-29 | checked; **F2's row is conservative** (the L1 mantle chord gives ~1.6e-30) |
| dependence on a | at fixed G, δm ∝ 1/a, so m_g² ∝ 1/a. Passing the row needs a ≳ 1.6e8 l_P ≈ 3e-27 m, which breaks G = a² (`AX:189-190`, an open gate) | reading |

### T2. Observations the strain-dependent mass would hit (beyond the GW170817 Earth crossing)

The additive channel is one term in the law, ½·δm″·t²·ψ̄ψ. Read from the graviton side it is a medium mass. Read from the matter side it is a rest-mass shift. Per t², with t = GW strain amplitude in grid axes (SF momentum scaling e^{t/2} ↔ 1 − h_GW/2, so |t| = |h_+|; reading):
- δm_e = 1.48e25 eV·t²;
- δm_N = 7.7e26 eV·t²;
- per unit mass: electron 2.9e19, nucleon 8.2e17 (`out:D`).

| # | observation | side | prediction (uncorrected SF channel) | bound | exceedance | label |
|---|---|---|---|---|---|---|
| G1 | GW170817 Earth crossing | graviton | μ_ρ = 2.4e-21 | 1.5e-29 (F2; conservative) | 1.6e8 (to ~4e9) | checked (F2 + `vF2`, massive sign) |
| G2 | detector on the ground | graviton | ~1e-4 suppression of every event | ~1e-29 | ~2e8 | checked (half-space; `vF2` item 3) |
| G3 | binary pulsar | graviton | Ṗ_b cut ~75% | 2e-43 | 1.2e22 | suggested (toy, `vF2` item 4) |
| **M1** | **atomic clocks under the nHz GW background** | matter | t_rms ≈ 1.3–2.0e-14 at Earth (NANOGrav A = 2.4e-15, f ≥ 1–2 nHz); d(t²)/dt ≈ 2–4e-28/yr gives d ln(m_p/m_e)/dt ≈ 6e-9 to 1e-8 /yr | −8(36)e-18 /yr (Lange 2021, WEB) | **~2e8–3e8** | suggested: the GWB is at 3.5–4σ (WEB); drift taken as the rms of 2t·ṫ from modes slower than 1/(5 yr); O(3) |
| M2 | composition-dependent free fall from ∇(t²) | matter | universal strain acceleration ~1e-9 m/s², quasi-static over months, inertially fixed; composition part ~2e-3 of it (binding 2.4e-3 for Be/Ti, electron Z/A 3e-4, in-nucleus σ-terms O(1e-2)?) gives ~2e-12 m/s² | space-fixed Δa < 8.8e-15 m/s² (Eöt-Wash 2008, WEB) | ~2e2 | suggested (composition factor rough) |
| M3 | LIGO-band GWs, matter side | matter | δm_e/m_e ~ 3e-23 at t = 1e-21 | — | invisible | checked arithmetic |
| S | **static fields, if they register as traceless grid strain** | matter | δm_e = m_e already at t = 1.9e-10; Earth's surface potential is 7e-10 and the Sun's at 1 AU 1e-8. Even O(Φ·v²) pieces (t ~ 1e-11, if the grid frame is the CMB frame) would give an annual m_e modulation of ~1e-5 against clock LPI limits of ~1e-16 | MICROSCOPE η(Ti,Pt) = (−1.5 ± 2.3 ± 1.5)e-15; (c²/μ)dμ/dΦ = 7(45)e-8 (WEB) | catastrophic if the registration exists | reading, conditional: static registration is undetermined (`rF2` §3.7) |
| L | SME c_jk-type anisotropic inertia | matter | the additive term is an *isotropic* rest-energy shift at P = 0. Direction-dependent (kinetic) strain terms are only log-sensitive to the grid, O(α t²) with no E_P/m factor, ~1e-31 | electron ~1e-21 (Sanner 2019, WEB) | not binding | suggested (power counting) |

**Answer to "anisotropic mass shifts in SME matter-sector bounds."**
- The channel is not mainly an SME c_jk effect. It is a local-position-invariance / equivalence-principle effect: an isotropic rest mass that tracks the local strain field.
- So the binding matter-side tests are clocks (M1) and free fall (M2), not sidereal anisotropy searches.
- A separate, uncomputed issue: one-loop non-universality of the O(t) kinetic coupling, a species-dependent graviton vertex. It would be SME/EP-relevant only if a static traceless strain exists (row S).

**Answer to "EP violation because ⟨ψ̄ψ⟩ per nucleon differs by composition."**
- On the graviton side, composition hardly matters. μ_ρ is dominated by the nucleon σ-weight (5.2); electrons add ~1% (0.1 × Z/A / 5.2).
- On the matter side, the per-mass coupling is 35× larger for electrons than for nucleons, and material dependence enters through Z/A, nuclear binding and in-nucleus σ-terms. The result is a violation at ~1e-3 of a Planck-amplified strain force (M2).

### T3. The rule against observation

- **What it removes (all unobserved):** G1–G3, M1–M3 and row S for the additive part.
- **Comparator:** in GR + SM the locally measured rest mass is independent of the metric (Einstein equivalence principle). In this program's language, that is the continuum relabelling Ward identity (`rR19-15:136-137`).
- **The observations agree with zero dependence** (WEB):
  - MICROSCOPE: η(Ti,Pt) = (−1.5 ± 2.3 stat ± 1.5 syst)e-15;
  - Eöt-Wash: η(Be,Ti) = (0.3 ± 1.8)e-13 toward Earth; space-fixed Δa < 8.8e-15 m/s²;
  - clocks: d ln μ/dt = −8(36)e-18/yr and (c²/μ)dμ/dΦ = 7(45)e-8;
  - electron Lorentz-violation coefficients ~1e-21.
- **What it leaves untouched:**
  - the O(t) coupling of the graviton to T_ij, which GW detection, light bending and Shapiro delay rely on. The E_g-linear additive term vanishes by cubic symmetry (`vR19-34` item 3);
  - the gravitational redshift, which is the lapse, not spatial strain;
  - vacuum GW propagation, provided (Σ) absorbs the knock-on (condition 3).
- **What it leaves over (needs disposition):**
  - **(i) Multiplicative channel.**
    - Per nucleon Σ m_q⟨N|q̄q|N⟩ ≈ 0.28 GeV (RECALLED); |z″| = 0.0717 e² (H-cov, `r1934_sizes.py:8`).
    - mult/add = 1.3e-21, so μ_ρ = 3.1e-42 eV² m³/kg.
    - Earth row: passes by 5e12. F2's pulsar row: ×16. Against 16πG: 2.1e-3 (`out:E`).
    - It is an O(α_s/π) fraction of gravitational strength, so its natural test is binary-pulsar timing at 1.3e-4. That needs a strong-field calculation (suggested; not under SF).
  - **(ii) Higgs mass² channel.**
    - Lattice scalar QED: ∂²_hΣ(P = 0) = −0.532 e²/a² (`rR19-31:124`). Unprotected (`rR19-31:113`); counterterm fixed at h = 0 (`rR19-31:62`).
    - With g² ≈ 0.4: δm_H² ≈ 4e54–1.6e55 eV²·t², so δv/v ≈ 1e32·t² (`out:F`).
    - Consequences: GWB, O(1e4); LIGO band, ~1e-10 at 2f.
    - ESTIMATE: gauge-group factor and SF vs H-cov units not computed. But a 1e20 margin does not depend on them.
  - **(iii) Vacuum knock-on** (F5(c)): tolerance m_g²a² < 2e-102.
  - **(iv) O(t) kinetic non-universality:** not computed.
- **Tolerances the rule must meet** (leftover as a fraction of F1's Hessian):
  - Earth row: 6e-9;
  - M1: ~4e-9;
  - row S, if it exists: ≲1e-11.
  - Base tuning is already 1e-20, so these add no new kind of fine-tuning. But they rule out a one-loop-only rule (condition 2).

### T4. Next test, specified: F6, the scalar (Higgs) analogue of P-R19-34a

- **Plain question.** Does the root's Higgs mass² respond to uniform strain at grid strength? If so, does any registered clause make it strain-covariant, or must P-R19-34a be generalized to all mass parameters?
- **Setting.**
  - F1's SF law (B1, Psym), U = 1, at the R18-9 root.
  - Scalar mass counterterm fixed at t = 0 (`rR19-31:62`).
  - Compute ∂²_tΣ_H(P = 0; t)·a² at one loop:
    - (1) U(1) gauge loop with F1's strained photon, as a control against `rR19-31:124` in H-cov;
    - (2) the SU(2)×U(1) group factor;
    - (3) the top-Yukawa loop on the D1 edge.
  - Memory: ≤ 96³ grid in k_z slabs, < 1 GB.
- **Conversion.** δv/v per t² = ∂²_tΣ_H/(4·m_H²/2), SM mapping labelled ESTIMATE.
- **Matter-side row M1.**
  - NANOGrav 15-yr spectrum: A = 2.4e-15, γ = 13/3, f_min = 1/(16 yr), with 1/(30 yr) as a branch.
  - Predicted |d ln(m_p/m_e)/dt| against 3.6e-17/yr.
  - Same row for the fermion additive channel as a control. Expected ~2e8 (this statement).
- **FIXED readings.**
  - **SCALAR-COVERED:** a registered clause makes Σ_H strain-covariant (name it, with file:line).
  - **SCALAR-HAZARD:** uncovered, and the predicted rate exceeds the bound.
  - **SCALAR-SAFE:** the Hessian is below the tolerance.
  - **OPEN:** otherwise.
- **Expectation.** SCALAR-HAZARD by ≥1e20. Then the price becomes P-R19-34a′: "every mass parameter of the law (fermion critical masses, scalar mass², vacuum stiffness) is re-set on every uniformly strained law". That is one clause and number-free under the vR19-24 convention.

### Strong words and limits

- **"Checked":** every number in T1, and the arithmetic of M1–M3 and the residual rows (`pheno_sizes.out`).
- **"Proved":** only the algebraic identity m_g²/(16πGρ) = (w c_h/4)E_P/m_N.
- **Suggested:** M1 (GWB at 3.5–4σ; drift model O(3)), M2 (composition factor), the Higgs estimate (group factor, units), and the multiplicative-vs-pulsar row (toy row, H-cov z″).
- **Reading:** row S (static registration undetermined), and t = h_GW.
- **Not claimed:** any F5 result (F5 is running); two-loop sizes; the O(t) vertex non-universality.

### Sources (WEB, this run)

- [Lange et al., PRL 126, 011102 (2021), arXiv:2010.06620](https://arxiv.org/abs/2010.06620): d ln μ/dt = −8(36)e-18/yr; (c²/μ)dμ/dΦ = 7(45)e-8.
- [MICROSCOPE final result, PRL 129, 121102 (2022), arXiv:2209.15487](https://arxiv.org/pdf/2209.15487): η(Ti,Pt) = [−1.5 ± 2.3 (stat) ± 1.5 (syst)]e-15.
- [Schlamminger et al., PRL 100, 041101 (2008), arXiv:0712.0607](https://arxiv.org/abs/0712.0607): η_Earth(Be,Ti) = (0.3 ± 1.8)e-13; space-fixed Δa < 8.8e-15 m/s² (95%). See also [Wagner et al. 2012 review, arXiv:1207.2442](https://arxiv.org/pdf/1207.2442).
- [Sanner et al., Nature 567, 204 (2019), arXiv:1809.10742](https://arxiv.org/pdf/1809.10742): electron Lorentz-violation limits ~1e-21.
- [NANOGrav 15-yr GWB evidence, arXiv:2306.16213](https://arxiv.org/abs/2306.16213): A = 2.4(+0.7/−0.6)e-15 at 1/yr; 3.5–4σ.
- [LVK GWTC-3 tests of GR, arXiv:2112.06861](https://arxiv.org/pdf/2112.06861): vacuum m_g ≲ 1.3–2.4e-23 eV, depending on version. The repo cites GWTC-4.0 at 1.92e-23 (`vR19-21:26`). Used here only as the order for the vacuum tolerance.
- GW170817 geometry and dispersion: from F2's sources (`rF2:274-284`), not re-fetched.
