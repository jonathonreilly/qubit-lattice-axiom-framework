# C5 R14-5 report: Λ, the P-T creation law with a spatially averaged lapse (P-r13a built)

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. Unrefereed. Run 2026-10-12, 21:14Z to 21:38Z. No repository file was edited.

**Scratch folder.** `S/` = `.../scratchpad/C5/R14-5/`. The scripts and their outputs are in `S/scripts/`. Each runs in under a minute at `OMP_NUM_THREADS=2`.
- `r145_bianchi.py/.out` (sympy): Lemma C, the Bianchi identity with a zero-mode lapse, for a general spherical metric with N(t, r). Also the homogeneous bookkeeping and the drop-out of g in the lapse equation.
- `r145_homog.py/.out`: the homogeneous zero-mode model taken through vacuum steps Δ = 0.01–0.7. It uses a global Prony (P-T) reader and computes Λ̃, λ and g. The control is the unimodular law (g ≡ 0).
- `r145_lapse.py/.out`: the CMC lapse equation in lumpy matter. It covers a 3D periodic lognormal box with contrast up to 1e7, Δ = 200 top-hat clusters and galaxies, a lapse-collapse toy, the Yukawa range, and positivity under DESI-type phantom dark energy.
- `r145_growth.py/.out`: linear dust growth in synchronous-comoving gauge with the CMC E-fluid, for g = 0 and for g = 2X.

**Read.**
- In full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (`AX`); `TESTS.md:2302-2320` (the C5 method); the item `TESTS.md:4872-4886`; `agents/C5_R13-3_report.md`; `C5_R13-3_referee_verdict.md` (`vR13-3`); `C5_R12-2_report.md`; `C5_R12-2_referee_verdict.md` (`vR12-2`).
- The Λ entries: `TESTS.md:2886-2898` and `2985-2993` (R5-3), `:4000-4012` and `4297-4301` (R10-4), `:4157-4188` and `4417-4424` (R11-3), `:4351-4363` and `4509-4517` (R12-2), `:4621-4641` and `4721-4729` (R13-3).
- In part: `C5_R11-3_referee_verdict.md:40-85`; `C5_R11-3_report.md:160-240`; `RN_L3_report.md:230-290`; `RN_L3_referee.md`; `C4_F1_report.md:35-51, 86-99` (khronometric, via grep).
- I also read the R13-3 script header `scripts/C5/R13-3/r133_linear.py:1-40`.

**Path abbreviations.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `TESTS` = `P/TESTS.md`.

**Labels.** proved / checked (sympy or numerics in this run) / suggested / reading / comparator.
- A comparator is **V** if fetched this run: Afshordi 0907.5201; Afshordi–Chung–Geshnizjani hep-th/0609150; Gomes–Guariento 1703.08226 (via a search summary); Afshordi 0807.2639 (abstract); Gomes–Gryb–Koslowski 1010.2481 (abstract); Gerhardt CMP 89 (1983), via a search summary.
- Otherwise it is **RECALLED**.

**Subtraction rule.**
- "Λ̃" is the only vacuum-dependent number that enters local physics. Λ̃ := λ + κρ_v, where λ(t) is the uniform value of E_nn = G_nn − κT_nn^tot. Homogeneously, Λ̃ = 3H² − κρ_nc, which is R12-2's Λ_eff (`C5_R12-2_report.md` subtraction rule).
- "Leak" ε = ρ̂/ρ_nc − 1. Nothing else is subtracted.
- "rel diff" in growth is D_model(1)/D_ref(1) − 1. The reference is named in each row.

---

## 0. Verdict against the FIXED readings (`TESTS:4882-4886`)

**Worker reading: VIABLE within a stated class 𝒵 (continuum completion, H-vac-Λ), with the prices named in §5. It is for the referee. Outside 𝒵 the item stays OPEN.**

**The class 𝒵, stated before the title (§2):**
- a smooth continuum completion;
- fixed proper site density, with sites created at a rate c ≥ 0;
- a shift and a traceless h_ij that are dynamical, so E_ni = 0 and E^TL_ij = 0 are imposed;
- a lapse N(x, t) with the global constraint ⟨N⟩_sites = 1 (one multiplier λ(t));
- a conserved total stress;
- a vacuum that is a w = −1 c-number in the imposed equations (H-vac-Λ);
- a zero-mode expansion law given by the P-T reader applied to the **global** mean density.

**The model (§4.1)** is GR in a CMC (York-time) lattice slicing. The global Hamiltonian constraint, i.e. the Friedmann equation, is replaced by the P-T creation law. Equivalently, it is GR plus a cuscuton-type constraint fluid E. Its two numbers (λ(t), g(t)) are fixed by the creation law, not by a potential.

**Results:**
- **(a) PASS (proved under stated hypotheses; checked).**
  - The CMC lapse obeys −D²N + Q̃N = S(t) with ⟨N⟩ = 1.
  - The maximum principle gives N > 0 wherever Q̃ ≥ 0. This holds for dust, radiation, smooth dark energy with w ≥ −1, and the DESI-type CPL checked in voids.
  - The normals expand at the uniform rate θ(t), so they cannot focus. There is no caustic in any collapsing or virialized region.
  - For a Δ = 200 cluster, N − 1 = Φ_Newton = −1.73e-5, checked.
  - In strong fields the lapse collapses toward 0 but stays positive (toy, checked). In black holes the lattice time freezes (comparator).
- **(b) PASS (proved; checked homogeneously).**
  - The zero mode of the Hamiltonian constraint is released into λ(t). The homogeneous constraint is evaded, and λ absorbs any w = −1 vacuum.
  - Through vacuum steps Δ = 0.01–0.7 the residual is Λ̃/ρ_nc = O(1e-16) after the transient, untuned. The unimodular control gives Λ_eff = −Δ, which is Lemma PT.
- **(c) PASS (proved at linear order; checked).**
  - When g ≡ 0 the model **is** GR with cosmological constant Λ̃ (= 0), nonlinearly. That is the case for an exact reader, no memory and no transition.
  - With g ≠ 0 the correction to growth is O(g/H²·(aH/k)²) inside the horizon (checked).
- **Untuned Λ_eff = 0:** yes, in the homogeneous sector between transitions.
  - In a lumpy universe the residual is Λ̃ = ½⟨R⟩ − ½⟨σ²⟩. That is backreaction-sized, about 1e-5 H₀² (suggested; the magnitude is RECALLED).
- **(d) Prices are named (§5).** The decisive one is new and proved (Lemma C): absorbing a vacuum change in the zero mode **forces** the lattice time to be CMC. That makes an elliptic, instantaneous lapse. A local, finite-speed clock is not available.

**What VIABLE does not cover (scope, stated plainly):**
- There is no Z³ construction. The 3D insertion geometry (S1), the encoder (S3) and ordered phases (S4) are still unbuilt.
- The grid-zero-point branch (H-vac-grid) is not covered. It fails there (suggested, §4.7 K5).
- Inhomogeneous phase transitions: only homogeneous steps were run.
- The P-T reader has transient failures at near-singular Hankel points, so a clamp or a regularized reader is needed (checked; P-r13d carried).
- The observed acceleration still needs w ≠ −1 dark energy or a constant in the creation law (S6 carried). DESI CPL is not reconstructed by a finite Prony reader (R13-3 (e), carried).

**Against the expectation implied by R13-3.** R13-3 named this escape and left it unbuilt (`C5_R13-3_report.md:50,215`; `vR13-3:57`). Building it shows two things:
- It does escape Lemma F and Lemma T.
- Its global price is sharper than "a range limit on `AX:57`". Bianchi forces the slicing to be CMC, and the lapse equation is elliptic, with an instantaneous Yukawa range of 0.4–0.8 c/H.

---

## 1. In plain words

- **What was missing.** In R13-3 the grid's clock ticked at the same rate everywhere. Its "now" then folded over inside every galaxy, because those clocks fall freely. Letting the clock rate vary from site to site fixed that, but it brought back the energy equation, and with it the vacuum energy.
- **The middle road.** Let each site's clock rate vary, but fix the *average* rate over all of space. The energy equation then holds everywhere except for its single "average" component. That component is exactly the one the vacuum energy lives in. The vacuum's energy goes into one leftover number, and the expansion is set by the creation rule, which never sees the vacuum.
- **The surprise: the clock is forced.** For the books to balance when the vacuum changes (at a phase transition), every site must see space expanding at exactly the same rate. Those are "constant-mean-curvature" time slices, a classic construction in relativity, known as York time. Finding the clock rate at each site then means solving an equation that links every site to every other site at the same instant. The influence falls off over about half a Hubble radius. No clock rule built only from neighbours can do this.
- **Galaxies are fine.** With this clock, sites inside a galaxy simply tick slower by the galaxy's gravitational potential, about one part in 100,000 for a cluster. The grid's "now" never folds. Near a black hole the grid's clock slows to a stop: time on the grid freezes there.
- **Structure growth is unchanged.** Whenever the vacuum is not changing and the creation rule reads the content exactly, the model *is* ordinary general relativity with a zero cosmological constant. Galaxies and the CMB then come out exactly as in GR.
- **The bill.**
  - The grid needs one shared, global number at every instant, plus a clock equation that acts instantaneously across space.
  - The creation rule must read the average density of the whole universe, not the local density.
  - A true cosmological constant cannot be seen, so the observed acceleration needs dark energy that changes in time.
  - The universe can never recollapse. Time's direction is the direction in which the number of sites grows.

---

## 2. Hypotheses and classes (stated before titles)

- **H-sites.** The proper site density is fixed. Sites are created at a rate c ≥ 0 per site (H-perm, `C5_R12-2_report.md:77`; `AX:79-80`). Number balance gives c = θ_s, the expansion of the site congruence (`C5_R13-3_report.md:136`, proved there).
- **H-zm (the item's global constraint).** ⟨N⟩ = 1, the average over sites. Because √h is fixed per site, the site average equals the proper-volume average. It is enforced by one multiplier λ(t). The lapse's local part is otherwise free.
- **H-imp.** The imposed equations are:
  - E_ni = 0 (shift);
  - E^TL_ij = 0 (traceless h_ij);
  - E_nn(x) = λ(t), uniform. This is the N-variation under H-zm.
  - The trace E_kk is not imposed, because √h is fixed per site (`vR11-3:49-52`).
- **H-T.** The total stress, matter plus vacuum, is conserved and smooth.
- **H-vac-Λ** (`C5_R13-3_report.md:81`). The vacuum enters as −ρ_v g, with ρ_v spatially uniform between transitions.
- **H-read.** The zero-mode law is H² = (κ/3)ρ̂_nc, where ρ̂ is R12-2's Prony P-T reconstruction (`C5_R12-2_report.md:179-190`). It is applied to the *slice-averaged* density ρ̄_tot(t). It carries no curvature memory X. X is treated only as a variant in §4.5.
- **H-CMC-exist.** A smooth foliation with the required uniform θ exists. In GR this is Gerhardt's theorem, with a compact Cauchy surface, the timelike convergence condition and barriers (V, via search summary). Here it is a hypothesis.
- **Excluded:**
  - the Z³ insertion geometry;
  - H-vac-grid, except §4.7 K5;
  - inhomogeneous bubble dynamics;
  - nonlinear growth beyond the halo lapse;
  - records as a q-charge (R10-4);
  - pairing.

---

## 3. Prior art (each counted once)

1. **R13-3 and its verdict** [ref].
   - Lemma F holds in the smooth N = 1 subclass (`vR13-3:5-12`).
   - Lemma T: the specified F-law is incompatible with V2 and a nonzero vacuum (`vR13-3:14-20`).
   - Lemma N (`vR13-3:22-32`) and Lemma A (`C5_R13-3_report.md:177-181`).
   - The named escape is P-r13a (`C5_R13-3_report.md:50,215,276`).
   - **This run builds P-r13a.**
2. **R12-2 and its verdict** [ref].
   - L-hom: the creation law is the Friedmann equation (`C5_R12-2_report.md:138-146`).
   - Rule P/Prony (`:179-190`), the F-law (`:204-213`), class U = unimodular = Lemma PT (`:158-160`).
   - The B-loc constraint-form obstruction (`:§4.5`).
3. **R11-3 Lemma BR** [ref]. V2 keeps E₀₀ and absorbs the pressure into f(t) (`vR11-3:49-52`).
4. **R5-3 Lemma PT** [ref] (`TESTS:2986-2987`).
   - G1–G3 "leaves out global constraints … dynamical compensators" (`TESTS:2987`). This model is in that escape class.
   - The Kaloper–Padilla global ⟨R⟩ = 0 rule is EXCLUDED, bounded (`TESTS:2988`). It does not apply here: no ⟨R⟩ condition is imposed, and a(t) is left to creation (L-hom).
5. **RN L3** [ref] (`RN_L3_report.md:252-266`). In projectable Hořava (lapse N(t) only) the scalar is a ghost, a tachyon, or strongly coupled.
   - This model is the **opposite** case: the local Hamiltonian constraint is kept for k ≠ 0, and only its zero mode is dropped.
   - So there is no extra local scalar (§4.7 K2). There is also no Mukohyama C(x) dust: P-r13e is no longer needed.
6. **C4 F1 (khronometric / healthy Hořava)** [ref] (`C4_F1_report.md:35-51,86-99`). Its foliation is dynamical with a finite khronon speed c_χ.
   - The cuscuton is the c_χ → ∞ / IR non-projectable Hořava limit (Afshordi 0907.5201, V). Its constant-field slices are CMC.
   - This model is that limit, with (V, μ²) replaced by (λ(t), g(t)) slaved to the creation law (§4.2).
7. **Comparators.**
   - **V:**
     - the cuscuton has infinite sound speed and is argued causal: its perturbations "cannot carry any microscopic information" (hep-th/0609150);
     - Gomes–Guariento: the cuscuton is regular only "as a spatially constant field in a CMC foliation … a single global degree of freedom", with stated conditions for the lapse to stay nonzero (1703.08226);
     - shape dynamics: GR in CMC gauge is dual to a theory with volume-preserving conformal invariance and one global constraint (1010.2481);
     - Afshordi's gravitational aether decouples the vacuum by an incompressible fluid and predicts G_rad/G_matter ≈ 1.33. That is a different model; this one has no such split when g = 0;
     - Gerhardt 1983 (CMC foliation existence).
   - **RECALLED:**
     - Henneaux–Teitelboim unimodular, where Λ is conjugate to cosmic time and Λ̇ = 0;
     - Brill–Cavallo–Isenberg 1980 (K-surfaces in Schwarzschild);
     - Estabrook et al. 1973 and Petrich–Shapiro–Teukolsky 1985 (maximal slicing, collapse of the lapse, limiting surface r = 3M/2);
     - Blas–Sibiryakov (universal horizon);
     - Buchert backreaction of order 1e-5.
8. **Repository grep** for "cuscuton", "constant mean curvature", "York time" and "maximal slicing" in `docs/` and `P/`. There are no hits beyond the khronon rows (C4 F1/F3/W2). No repository treatment of a CMC lattice time was found.

---

## 4. Results

### 4.1 The model (P-r13a made explicit)

**Fields.**
- Lattice time t and sites with fixed proper density.
- The ADM metric relative to t (N, β, h_ij), and matter.
- Lagrange multiplier λ(t).

**Equations:**
1. E_ni = 0, E^TL_ij = 0, E_nn = λ(t) (H-imp). Here E_μν := G_μν − κT^tot_μν.
2. **Zero-mode (creation) law:** θ(t) ≡ ⟨c⟩ = 3H(t), with H² = (κ/3)ρ̂_nc[ρ̄_tot history] (H-read).
3. **Clock (lapse) law, forced by Lemma C, §4.2:** the slicing is CMC, θ_n(x, t) = θ(t). The lapse solves
   −D²N + Q̃N = S(t), with Q̃ := K_ijK^ij + (κ/2)(ρ+3p)_nc − Λ̃(t) and ⟨N⟩ = 1.
   The normalization fixes S(t). Then g(t) = −(2/3)(θ̇ + S) is an output.
4. **Site rule (the simplest consistent choice):** c_s = θ(t) at every site. Sites ride the CMC normals, there is no drift (V = 0), and √h is fixed per site automatically.
5. **E-fluid bookkeeping (from Bianchi):** p_E = g/N − λ, and λ̇ = −g θ.

**The local clock dynamics on the lattice (reading: the direct discretization).** Each site's tick rate N_i satisfies the nearest-neighbour relation

(6 + a²Q̃_i) N_i − Σ_{j~i} N_j = a² S(t),

with one global number S(t) per instant, fixed by Σ_i N_i = N_sites.

**Equivalence.**
- This is GR + matter + a "cuscuton" fluid with velocity n (CMC normals), ρ_E = λ(t), and p_E = g(t)/N − λ(t).
- Compare the cuscuton in unitary gauge: ρ = V(φ(t)), p = μ²φ̇/N − V, with CMC slices (Afshordi 0907.5201, V). Here (V, μ²φ̇) is replaced by (λ, g).

### 4.2 Lemma C: a zero-mode lapse forces a CMC clock whenever the vacuum is absorbed (proved, nonlinear; checked)

**Statement.** Assume H-imp and H-T. Then E = ρ_E nn + p_E h with ρ_E = λ(t), and ∇^μE_μν ≡ 0 gives:
- (Euler) D_i p_E + (λ + p_E) D_i ln N = 0, so (λ + p_E)N = g(t);
- (energy) λ̇ = −g(t) θ_n(x, t).

**Hence, at each instant, one of two cases holds:**
- (A) g = 0. Then λ is constant and E = −λ g_μν. This is exact GR with Λ_eff = λ + κρ_v, i.e. unimodular. A vacuum change Δρ_v then shifts Λ_eff by κΔρ_v, which is Lemma PT (`TESTS:2986`).
- (B) g ≠ 0. Then θ_n is spatially uniform: the slicing is CMC.

**Corollary.** Absorbing a vacuum change requires λ̇ = −κρ̇_v + … ≠ 0, so g ≠ 0, so a CMC slicing during the change.
- Any clock with non-uniform θ_n during a vacuum change violates the k ≠ 0 Hamiltonian constraint at the rate g·(θ_n − θ̄). That includes a finite-speed local driver, harmonic or 1+log slicing, and R13-3's N = 1.
- Otherwise it falls back to (A), i.e. Lemma PT.

**Checks** (`r145_bianchi.out:1-5`). For ds² = −N(t,r)²dt² + A²dr² + B²dΩ², the divergence equals the Euler and energy forms exactly (residual 0). With ρ_E = λ(t) and p_E = g/N − λ, the r-component vanishes identically and N²·(t-component) = λ̇ + gθ_n.

**Homogeneous bookkeeping (checked, `:6-7`).** g = −2Ḣ − κ(ρ+p)_nc: the w = −1 vacuum drops out. The relation λ̇ + 3Hg = 0 holds for any a(t). This is L-hom again: the zero mode is free.

### 4.3 (a) No caustic in collapsing halos

**Lemma P, lapse positivity (proved on compact slices).**
- Integrating the lapse equation gives S = 1/⟨N₁⟩ with −D²N₁ + Q̃N₁ = 1. If Q̃ ≥ 0 and Q̃ is not identically 0 on a compact (toroidal) slice, the strong maximum principle gives N₁ > 0, so N = N₁/⟨N₁⟩ > 0 everywhere.
- On a statistically homogeneous slice of infinite extent the same holds if Q̃ ≥ Q_min > 0. That is the standard positive Yukawa Green's function (proved for bounded Q̃ ≥ Q_min, a standard result).
- **When Q̃ ≥ 0:**
  - Using θ²/3 − Λ̃ = κρ̂_nc (H-read, Λ̃ ≈ 0), Q̃(x) ≥ κρ̄_nc + (κ/2)(ρ+3p)_nc(x).
  - This is ≥ 0 for dust and radiation at any contrast, including voids with ρ_m(x) = 0. For smooth dark energy it is ≥ 0 iff w ≥ −1, i.e. ≥ (3κ/2)(1+w)ρ_DE.
  - The DESI-type CPL (w₀ = −0.75, w_a = −0.86), checked at void floors for a = 1, 0.7, 0.5 and 0.33: Q̃_min = 1.69, 2.60, 6.62 and 24.3 in units of H₀². All positive, because matter dominates whenever w < −1 (`r145_lapse.out`, part D).

**No focusing (proved, given H-CMC-exist and Lemma P).**
- The normals' expansion is θ_n = θ(t) > 0, uniform and finite. A caustic of the foliation needs θ_n → −∞ or N → 0/∞ somewhere. Neither can happen while 0 < N < ∞.
- Raychaudhuri focusing is balanced by the acceleration a = D ln N: the normals "hover" like static observers.
- So R13-3's Lemma F mechanism (geodesic normals, `vR13-3:5-12`) is absent by construction.

**Numbers (checked, `r145_lapse.out`), with c = H = 1, EdS, and σ² ≥ 0 dropped (a lower bound on Q̃):**
- **3D lumpy box** (48³, periodic, lognormal):
  - L = 0.05 c/H with ρ/ρ̄ ∈ [5.5e-6, 165]: N ∈ [0.99869, 1.00017], and N − 1 matches the Poisson potential with correlation 1.0000 and equal rms (1.53e-4).
  - L = 1 c/H with ρ/ρ̄ up to 131: N ∈ [0.719, 1.054]. Still positive, with correlation 0.9989 (Yukawa screening visible).
- **Top-hat, Δ = 200** (relative to critical):
  - cluster R = 1.5 Mpc: N(0) − 1 = −1.7337e-5, against Φ_N(0) = −1.7346e-5;
  - galaxy R = 0.25 Mpc: −4.818e-7, against −4.818e-7.
  - So lattice clocks in halos run slow by the Newtonian potential, as static clocks do.
- **Lapse-collapse toy** (flat 3-metric, fixed mass, R → 0): at compactness Q_inR² = 1, 10 and 100, N(0) = 0.648, 0.0845 and 9.1e-5. It stays positive. This is the expected "collapse of the lapse".
  - For real black holes, CMC/maximal slices approach a limiting surface (r = 3M/2 for K = 0) and never reach the singularity (comparator, RECALLED). Lattice time freezes inside.
  - That is a regular foliation, not a caustic. The toy is not a GR collapse computation.
- **Yukawa range** of the instantaneous lapse response, ℓ = Q̄^{-1/2}: 0.408 c/H (radiation era), 0.471 c/H (matter era), 0.814 c/H today (w = −0.95, Ω_m = 0.3).

**Answer to (a).** No caustic forms in collapsing or virialized halos for any matter contrast, given Q̃ ≥ 0 (proved; checked).
- Inside black holes the lattice time freezes (comparator plus toy).
- The R13-3 registration question "does creation stop inside bound regions?" no longer arises. Creation is uniform (c = θ > 0) and sites stream through halos. Their outward drift relative to the halo matter is H·r, about 100 km/s at 1.5 Mpc (suggested).
- S5 (site freezing) and P-r13c (long memory) are not needed.

### 4.4 (b) The homogeneous Hamiltonian constraint is evaded, and a constant vacuum is invisible without tuning

**Proved (structural).**
- The N-variation under H-zm imposes E_nn − ⟨E_nn⟩ = 0, not E_nn = 0. So the k ≠ 0 Hamiltonian constraint is GR's, while the zero mode λ(t) is free.
- The zero mode of the expansion is set by the creation law (L-hom, now with a dynamical lapse). This is the exact point where R13-3's Lemma T failed: V2 re-imposed 3H² = κρ_tot (`C5_R13-3_report.md:211-215`). Here it does not.
- The vacuum enters only through Λ̃ = λ + κρ_v. Homogeneously Λ̃ = 3H² − κρ_nc = κ(ρ̂ − ρ_nc), which is zero whenever the reader is exact. So λ = −κρ_v is set automatically, whatever ρ_v is.
- With no memory X, a reader error does not persist after the transient. That is the difference from Lemma K's curvature kick (`C5_R12-2_report.md` §4.4).

**Checked** (`r145_homog.out`; κ = 1; u = ln a; latent heat into radiation; global Prony order 2):

| Δ (α) | W | ε(u_T) | Λ̃/ρ_nc at u_T + 10W | Λ̃/ρ_nc at end | λ_end vs −ρ_v,final | unimodular control Λ_eff/ρ_nc at end |
|---|---|---|---|---|---|---|
| 0.01 (0.010) | 0.15 | +7.4e-3 | +1.9e-7 | +6e-16 | −4.9900 = −4.9900 | −3.1e5 (= −Δ) |
| 0.05 (0.049) | 0.3 | +3.3e-2 | +1.6e-5 | +6e-16 | −4.9500 = −4.9500 | −3.9e8 |
| 0.3 (0.28) | 0.3 | +0.20 | +7.7e-5 | +8e-16 | −4.7000 = −4.7000 | −2.3e9 |
| 0.7 (0.59) | 0.3 | +0.48 | +1.4e-4 | −4e-16 | −4.3000 = −4.3000 | −5.2e9 |
| 0.01 (0.010) | 0.02 | +6.1e-2 | +9.5e-7 | −5e-16 | −4.9900 = −4.9900 | −1.9e3 |

- **Untuned:** the same law, with no parameter, for every Δ.
- **The control:** g ≡ 0, the unimodular law tuned to the *initial* vacuum, ends at Λ_eff = −Δ. That is Lemma PT.
- **Reader caveat (checked, same file).**
  - The 2-node Prony reader has near-singular Hankel points, with normalized det down to 4e-6, and complex nodes at 1–79 of 4001 samples.
  - At those points ρ̂ has transient excursions: max|ε| from 1.4 to 4.8e2, and min ρ̂/ρ_nc = −3.4 at Δ = 0.05 and −482 at Δ = 0.3.
  - So a clamp c = max(0, ·), or a regularized reader, is needed during transitions (P-r13d, carried; consistent with `vR13-3` finding 5).
  - The g/H² "peak in step" values, about 1e3, are dominated by these excursions and by finite-difference noise. The pre- and post-step g/H² of about 1e-5 is finite-difference noise; the analytic value is 0.
- **Why the global reader matters.** A per-site reader reproduces Lemma A: collapsed mass is read as "constant" and H comes out about 8–12% low (`C5_R13-3_report.md:177-181`, suggested). With the global ρ̄_tot(t), dust dilutes exactly as a⁻³ by mass conservation, up to virial kinetic corrections of order 1e-6 (suggested). The cost is P-r13b.
- **Lumpy universe (suggested).** Averaging the Hamiltonian constraint on a CMC slice gives Λ̃ = θ²/3 − κρ̄_nc + ½⟨R⟩ − ½⟨σ²⟩. With an exact reader, Λ̃ = ½⟨R⟩ − ½⟨σ²⟩, which is backreaction-sized (of order 1e-5 H₀², RECALLED). It is algebraic, not accumulated.

### 4.5 (c) Linear growth

**Exact GR whenever g = 0 (proved, nonlinear).**
- g = 0 gives E = −λ g_μν with λ constant (Lemma C, case A), so G_μν + Λ̃ g_μν = κT^nc_μν exactly.
- With the exact reader and no memory, Λ̃ = 0. Growth, ISW and lensing are then those of flat GR with the supplied content: wCDM if a constant-w dark energy is present and reconstructed exactly (R12-2 Rule P).
- Between transitions the only departures are reader error and backreaction-sized g.

**With g ≠ 0 (proved, linear; derivation in `r145_growth.py` docstring):**
- In synchronous-comoving gauge for dust, with CMC time T = t + ξ:
  - ξ = δ̇/(k²/a² − 3Ḣ) (the CMC condition; the denominator is > 0);
  - δρ_E = −gθξ;
  - δp_E = (ġ + gθ)ξ + gξ̇;
  - δ̈ + 2Hδ̇ = (κ/2)ρ_mδ + ½[(3ġ + 2gθ)ξ + 3gξ̇].
- Inside the horizon, ξ = O((aH/k)²δ/H), so the correction is O(g/H²·(aH/k)²).
- **Checked** (`r145_growth.out`), with the curvature-like memory variant X ∝ a⁻², g = 2X, compared against GR with the same H(a):

| Ω_X | k = 0.3 | 1 | 3 | 10 | 100 H₀/c |
|---|---|---|---|---|---|
| 3e-3 | +1.4e-3 | +1.3e-3 | +7.5e-4 | +1.8e-4 | +3.4e-6 |
| 0.3 (stress test) | +0.19 | +0.17 | +0.087 | +0.019 | +3.3e-4 |

- With g = 0 the solver returns D(1) = 1.0000000 for EdS, the GR growing mode.
- The X variant also changes the background, by −1.7e-3 in D for Ω_X = 3e-3. **It is not needed:** growth comes from the local GR equations, not from per-site memory. Lemma G (`C5_R12-2_report.md` §4.4) applied to comoving sites only.

**Answer to (c).** GR's linear growth holds exactly when g = 0. Otherwise the departures are O(g/H²), suppressed by (aH/k)² inside the horizon. Today g/H² is of order the backreaction (suggested), or 2Ω_X ≲ 6e-3 if the memory variant is used (DESI DR2 10³Ω_K = 2.3 ± 1.1 as a proxy, `TESTS:2993`).

### 4.6 (d) The price against `AX:57`, and the arrow

**Against `AX:57`** ("one fixed nearest-neighbor admissibility rule, covariant…"):
- The clock relation at each site is nearest-neighbour **in form**: (6 + a²Q̃_i)N_i − ΣN_j = a²S(t). This parallels `AX:60-61`, where each site's distribution is determined by its neighbours' conditions, and a deterministic substrate is a boundary realization (`AX:63-66`; reading).
- **It is not a fixed rule, for three reasons:**
  - (i) It contains a global, time-dependent number S(t), equivalently λ(t) or ⟨N⟩ = 1. That number is one global degree of freedom per instant.
  - (ii) Its solution is simultaneous across the slice. It is elliptic and instantaneous, with Yukawa range 0.4–0.8 c/H, i.e. about 1e61 lattice spacings.
  - (iii) The zero-mode law reads the global ρ̄_tot (P-r13b).
- Lemma C shows that (ii) is **forced** for any zero-mode-lapse theory that absorbs vacuum changes. A finite-speed local clock contradicts the constraint, or else falls back to Lemma PT.
- **Physical instantaneous influence.**
  - With g = 0 the dynamics is exact GR, so the slicing is not observable through the metric. The lattice frame (CMC normals) is then like the CMB frame. Its normals differ from Newtonian-gauge normals by about (aH/k)·Φ·c, i.e. tens of m/s (suggested). The existing LV walls are carried unchanged.
  - With g ≠ 0 there is a genuine instantaneous pressure response δp_E = −gδN.
  - Comparator (V): cuscuton perturbations "cannot carry any microscopic information" (hep-th/0609150). Not proved here.

**Against the arrow** (`AX:186`: the arrow is an open gate):
- c = θ(t) ≥ 0 at every site (H-perm) needs H > 0 forever.
- The P-T law gives H² = κρ̂/3 > 0 for any nonzero content, so **the universe never turns around**, whatever its curvature or content (proved, homogeneous).
- The York time θ(t) is monotone for content satisfying the null energy condition. The arrow of lattice time is therefore the arrow of increasing site count. It is supplied by the creation law's sign, not by the axioms (price).
- Inside black holes, N → 0: the grid's time freezes there. The owner's thought "a sealed box fills until frozen = black hole" (`MEMORY`, a thought, not a rule) has this as a qualitative counterpart (reading only).

### 4.7 Kill round on my own model (each attack stated, with its outcome)

- **K1. Overdetermination** (θ is set by creation, λ by the geometry, ⟨N⟩ = 1).
  - Survives. g(t) = −(2/3)(θ̇ + S) is the free output that absorbs the mismatch, and λ̇ = −gθ is then an identity (Lemma C).
  - Constraint preservation holds: the Euler relation is solved by p_E = g/N − λ, and the energy relation by CMC (proved).
- **K2. An extra local scalar or strong coupling** (RN L3's projectable disease).
  - Survives (suggested). The constraints are the momentum constraints (first class) plus the pair H(x) − ⟨H⟩ and CMC (second class, as in shape dynamics). That leaves 2 local degrees of freedom plus one global pair (volume, York time) driven by the creation law.
  - Consistent with Gomes–Guariento (V): regular in CMC with a single global degree of freedom.
  - There is no C(x) dust, because the k ≠ 0 constraint is imposed.
- **K3. Causality.**
  - Not killed, not cleared. When g ≠ 0 there is an instantaneous influence. It is transient during transitions (pre-BBN for Standard Model ones) and backreaction-sized today (suggested). Named as a price.
- **K4. A local clock instead.** Killed by Lemma C (proved): finite speed means the constraint is violated or Lemma PT returns.
- **K5. H-vac-grid** (the grid zero-point has w ≥ 0 and is at rest in the site frame, `vR11-3:35-41`).
  - Then (ρ + p)_v ≈ 1.4–2.1 a⁻⁴ ≠ 0 enters g ≈ −κ(ρ+p)_v. That gives g/H² of about 1e122 and an instantaneous δp_E = −gδN of Planckian size in every potential well.
  - Separately, Lemma G′ (`C5_R13-3_report.md:217-221`) needs geodesic sites, which conflicts with sites on accelerated CMC normals.
  - **The model fails in this branch (suggested, conditional on the bridge, `AX:187`).** The VIABLE reading is for H-vac-Λ only.
- **K6. Per-site reading.** Lemma A applies (suggested, about 8–12% in H). This requires P-r13b.
- **K7. Phantom dark energy.** Positivity needs Q̃ ≥ 0. Checked for the DESI-type CPL; a strongly NEC-violating dominant component would break it.
- **K8. R5-3's sequestering exclusion.** It does not transfer: no ⟨R⟩ = 0 or global-curvature condition is imposed (L-hom).
- **K9. "This is just GR in CMC gauge".** No. GR in CMC gauge keeps the global Hamiltonian constraint, which is the Friedmann equation, and it sees ρ_v. Here that constraint is replaced by the creation law. The difference from GR is exactly g(t) and Λ̃(t).
- **K10. Henneaux–Teitelboim unimodular.** There λ is conjugate to cosmic time and conserved (case A). Here λ is not conserved (λ̇ = −gθ) because the volume–York pair is driven externally. That is what lets the vacuum change be absorbed.

---

## 5. Prices (named, none adopted)

| # | Price | Axiom text touched | What it buys | Status |
|---|---|---|---|---|
| **P-r14a** (P-r13a built) | **CMC lattice time.** ⟨N⟩ = 1 with one global multiplier λ(t). The lapse solves an elliptic nearest-neighbour-form equation with a global S(t), so it is instantaneous with Yukawa range 0.4–0.8 c/H. The CMC slicing is **forced** by Lemma C | `AX:57` (a fixed nearest-neighbour rule: here a global time-dependent number plus a simultaneous solution); `AX:116-130` (no time metric supplied: lattice time = York time); `AX:37` via S1 | Escapes Lemma F (no caustic, §4.3) and Lemma T (zero mode released, §4.4) | built; proved and checked within 𝒵 |
| P-r13b | **Global reader.** The zero-mode law reads the slice-averaged ρ̄_tot(t) | `AX:57` (range); source/action gate `AX:187` | Escapes Lemma A, P-r13c (orbital memory) and per-site wall passages | needed |
| P-T | Temporal vacuum reference (Prony on time derivatives) | `AX:186-187`; `AX:94-95` (reading) | Untuned Λ̃ = 0 | carried |
| P-r13d | Transition clamp or regularized reader | as P-T | Avoids transient ρ̂ ≤ 0 at near-singular Hankel points (checked) | carried, still needed |
| P-arrow | **No recollapse; the arrow = site count.** c = θ(t) ≥ 0 everywhere, so H > 0 forever | `AX:79-80` (H-perm, reading); `AX:186` (the arrow is an open gate) | Consistency with record permanence; frozen lattice time inside black holes | new, named |
| P-vac | **H-vac-Λ bridge.** The vacuum is a w = −1 c-number in the imposed equations. Under the grid zero-point the model fails (K5) | `AX:187` | Everything above | required |
| S1, S3, S4 | Site creation geometry, encoder, ordered phases. Creation is now uniform at rate θ(t) on CMC normals | `AX:37,40-41`; `AX:60-73,181-184` | Redshift and quiet insertion | carried, unbuilt |
| S6 | Acceleration needs w ≠ −1 dark energy, or a constant Λ_law in the creation law (untouched by vacuum changes) | none (observational) | Today's acceleration | carried |
| dropped | S5 (freezing in bound regions), P-r13c (long memory), P-r13e (C-dust) | — | — | not needed in this model |

---

## 6. Notes for the referee and the record

**Referee items (a VIABLE claim plus one structural no-go, Lemma C's corollary):**
1. **Lemma C:**
   - the perfect-fluid form of E under H-imp;
   - the Euler/energy split with a_i = D_i ln N (sympy-checked in spherical symmetry only; the general case is the standard fluid identity);
   - the dichotomy, and the corollary that a finite-speed clock either violates the k ≠ 0 constraint or returns to Lemma PT.
2. **Lemma P:** the maximum-principle positivity (compact slices; bounded Q̃ ≥ Q_min > 0 on R³), and the sufficient condition Q̃ ≥ κρ̄_nc + (κ/2)(ρ+3p)_nc(x). Existence of the CMC foliation is a hypothesis (H-CMC-exist), not proved in this modified theory.
3. **§4.4:** that the N-variation with ⟨N⟩ = 1 gives E_nn = λ(t) uniform. This needs √h fixed per site, so that the site average equals the volume average. Also the homogeneous runner and its control.
4. **§4.5:** the synchronous-gauge E-fluid perturbations, in particular the sign of the tilt term (∂_i n^i = −∇²ξ/a²) and δN = −ξ̇.
5. **K5:** whether H-vac-grid really kills the model, which is conditional on the bridge.

**Strong-word check.**
- "Forced" (CMC): only under H-imp and H-T, whenever λ̇ ≠ 0.
- "Exact GR": only when g ≡ 0 (case A).
- "No caustic": given H-CMC-exist and Q̃ ≥ 0.
- "Untuned": the homogeneous sector, an exact reader, after transients.
- "Never turns around": the homogeneous P-T law with ρ̂ > 0.
- "VIABLE": the class 𝒵 under H-vac-Λ, at continuum level, as a worker reading.

**What would change the picture:**
- a Z³ realization of the elliptic clock with a global S(t) (for example by relaxation), with its cost;
- a proof or disproof of no-signalling for g ≠ 0;
- the source/action bridge settling H-vac-Λ against H-vac-grid;
- an inhomogeneous first-order transition run in CMC slicing;
- a reader that tracks evolving dark energy (CPL).

## 7. Files

- Report: `S/R14-5_report.md`.
- Scripts and outputs: `S/scripts/r145_bianchi.py/.out`, `r145_homog.py/.out`, `r145_lapse.py/.out`, `r145_growth.py/.out`.
