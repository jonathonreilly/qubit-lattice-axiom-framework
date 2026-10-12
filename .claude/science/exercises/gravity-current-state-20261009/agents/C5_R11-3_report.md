# C5 R11-3 report: Λ's mean on a fixed grid. The volume mode, the vacuum's tadpoles, and its equation of state (sets C and C-box)

**Worker.** Claude Opus 5.5 (same family as the supervisor, S11 and every C5 worker). Unrefereed. 2026-10-12, 18:36Z to 19:00Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R11-3/`. Scripts and outputs in `S/scripts/` (each runs in under 30 s at `OMP_NUM_THREADS=2`):
- `r113_profiles.py`: the L, G and NN band profiles (copied in form from R9-9's `r99_profiles.py`; R8-2 box B = 2.0, B₂ = 3.1) plus the edge family u_t = (1−t)u_L + t u_G.
- `r113_tadpoles.py/.out`: part (a), the vacuum tadpoles ρ_vac, p_vac, w, the box/edge split, the A-moment identity, the continuum cube comparator, the edge family, the m: 1 → 0.3 step.
- `r113_steps_sizes.py/.out`: small-m step coefficients, V1 finite strain (M coupling), sizes.
- `r113_step_family.py/.out`: step coefficients along the edge family and their A-moment identity.
- `r113_V1_flow_and_numbers.py/.out`: V1 finite strain with the registered U coupling (R9-2's strain flow), the linear cross-check, rapidity budgets and site counts.
- `r113_options.py/.out`: part (b), sympy: the linearized Bianchi identity, and the Fourier mode count of linearized gravity restricted to V1, V2, V3.

**Read.**
- In full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (`AX`); the R11-3 registration (`TESTS.md:4157-4188`); `agents/C5_R5-3_referee_verdict.md`; `agents/C5_R9-2_referee_verdict.md`; `agents/C5_R9-9_referee_verdict.md`; `docs/COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md`; `docs/UNIVERSAL_GR_INDUCED_COSMOLOGICAL_CONSTANT_BOUNDED_THEOREM_NOTE_2026-06-08.md`; the scratch R10-4 referee verdict (`.../C5/ref_R10-4/R10-4_referee_verdict.md`), now recorded at `TESTS.md:4297-4301`.
- In part: `TESTS.md:2302-2420` (method, round 1), `:2875-3009` (R4-5, R5-3), round 6–10 pre-registrations and results (`:3009-4061`), round 10 referee results (`:4268-4307`); `SUMMARY.md:534-636` (§§21–24); `agents/C5_S11_synthesis.md` §§1–6; `agents/C5_R5-3_report.md:1-140`; `agents/C5_R9-2_report.md:195-260`; `agents/C5_R9-9_report.md:1-120`; `agents/C5_O3_report.md` (Λ lines, `:40-104,186`); `agents/RN_L3_report.md:46-50,236-266`; `agents/RN_L3_referee.md:14-15`; R9-2's scratch `r92_shear.py`.
- Not read for content: `C5_R4-5_report.md` beyond its verdict lines in TESTS; R10-5 (worker reading only, `TESTS:4303-4307`, used as a control).

**Labels.** proved / checked (numerics here) / suggested / reading / comparator / RECALLED (from memory, not verified this run).

**Subtraction rule (TESTS:4074).** Every tadpole below is absolute: no channel or counterterm is subtracted. Every "residual" names its subtraction: ρ(e) − ρ(0) is what remains after a constant (Λ√−g) counterterm tuned at strain e = 0. Every "step" is the difference between the vacua at m and m′ of one species, everything else fixed. There are no decay or tail clauses in this item.

---

## 0. Verdicts against the FIXED readings (`TESTS:4180-4184`)

| Option | Reading (worker) | One line |
|---|---|---|
| **V1** (trace dynamical, spacing grows) | **SOURCED** | ρ_vac sources the lapse (the q = 0 Hamiltonian constraint) and p_vac sources the trace (ë = −(κ/6)(ρ + 3p)). Computed: ρ_vac = 1.07–1.56, p_vac = 0.10–0.98 per real scalar in lattice units, w = 0.08–0.91 depending on edge and coupling, **never −1 for any profile** (proved: w ≥ 0). Minkowski needs **two** tadpole conditions at linear order (claimed; to the referee). Over the expansion history the zero-point is a per-site energy function, so a constant counterterm leaves an O(1) Planckian residual after a 10% change of scale (checked) |
| **V2** (√h fixed per site, lapse dynamical) | **EXCLUDED as a fixed-site option** (to the referee). Vacuum coupling inside V2: **SOURCED, ρ only** | No isotropic expansion is possible: volume per site and site count are both fixed, and a homogeneous lapse is a time relabelling. The lost trace equation comes back up to a free f(t), so the homogeneous pressure decouples (proved). ρ̄_vac still enters the q = 0 Hamiltonian constraint (one tuning, not two). Mode count = GR's (checked). With site creation (a Lattice price): OPEN |
| **V3** (√h and lapse fixed) | **DECOUPLED at linear order** (proved), **and EXCLUDED as a fixed-site option** (to the referee) | The lost equations come back as E₀₀ = C(x), static, and E_kk = f(t). The constant vacuum (ρ, p) is absorbed into (C₀, f). A homogeneous step at fixed volume conserves ρ_tot and its Δp goes into f(t). The residual Λ is the integration constant C₀. Prices: an ω = 0 scalar (the projectable strong-coupling point, RN L3), static fields as integration data, and no expansion without site creation. With site creation: OPEN; the tuning relocates to the rule giving C to new sites |

**Against the registered expectations (`TESTS:4185-4188`).** V1: as expected, and sharper: no edge profile gives w = −1 at all, because the vacuum's w ≥ 0. V2: expected SOURCED. Its vacuum coupling is SOURCED (ρ only), but the option itself fails on expansion. V3: as expected (DECOUPLED at linear order, EXCLUDED on expansion as a fixed-site option, OPEN with site creation).

---

## 1. In plain words

- **A grid vacuum is not a cosmological constant.** For empty space's energy to act as Λ, its pressure must be exactly minus its energy density (w = −1). On the axioms' grid with separate time, each mode's zero-point pushes outward, as a gas of half-quanta does. So the vacuum's pressure is positive: w ≥ 0 for every band shape. This holds whatever the box does, because the vacuum sums every momentum on the zone, and even the box part alone is a frame-fixed cutoff (w = 1/3 for massless matter, the textbook momentum-cutoff answer).
- **Exactly how far from −1 is set by the grid's leftover anomaly.** The gap ρ + p equals an energy-weighted average of the same "boost anomaly" A that makes edge quanta fall wrongly (Theorem E). On the torus all of it sits on the edge (proved).
- **So the grid needs two cancellations where a relativistic theory needs one.** With a symmetry that swaps time and space (set B's 4D grid) or Lorentz symmetry (set A), the vacuum's stress points along the metric, and one constant cancels it. With separate time (sets C and C-box) there are two independent vacuum numbers, energy and pressure. Each is about 10¹²³ times the observed Λ, and each must be cancelled.
- **If space grows by stretching the grid (V1),** the vacuum's energy per site changes as the grid stretches. It behaves like a Planck-density fluid, roughly radiation-like, not a constant. A constant counterterm cancels it at one moment only; 10% later, an O(1) Planckian amount is back. The lattice spacing also grows with the universe, so "the grid spacing is the Planck length" can hold at only one epoch.
- **If the volume per site is fixed (V2, V3),** the pressure, and in V3 also the energy density, drop out of gravity: the equations come back with free "integration constants", as in unimodular gravity. The price is that the universe cannot expand at all unless new sites appear. Site creation is a change to the Lattice axiom. It must stretch light (redshift) and keep pace with Friedmann's law. Then the question "does the vacuum gravitate?" moves into the site-creation rule: it is not answered.
- **Exact boson–fermion pairing on identical bands** would remove both vacuum numbers, and the whole stretching function, at once. That is the same structure O3 (refereed) and R10-5 (worker) point to.

---

## 2. Hypotheses and classes (stated before titles)

- **H-mat.** Free Gaussian matter on Z³ × ℝ, with dispersion ε² = m² + Σᵢu(kᵢ). The profiles are L (literal), G (gapped) and NN (control), from R8-2/R9-9 (`C5_R9-9_report.md:35-42`).
  - Zero-point completion: +ε/2 per real scalar mode (R9-2's "(Z)", `C5_R9-2_report.md:229`).
  - Sea: −ε per mode for Clifford-flat fermions with the same band (R9-2's "(S)"). The Wilson/staggered Dirac class, with R10-1's extra a- and mixing-functions (`TESTS:4273-4275`), is outside.
- **H-stress.** Two prescriptions for the spatial stress's forward value:
  - **U** (registered: R8-2's Construction A): F^{ij}(k,k) = ε vᵢvⱼ = pᵢpⱼ/ε, p = ∇(ε²/2), pᵢ = u′(kᵢ)/2;
  - **M** (comparator; R9-9's minimal metric vertex): F^{ij} = δ_ij u(kᵢ)/ε.
  - The vacuum value is half the forward value per mode. That holds for oscillator bilinears (Aπ² + Bφ²). For U it assumes R9-9's field-theory completion of the pair stress, which was assumed there, not built (`vR9-9:3`).
  - Independent cross-check (checked): R9-2's strain-flow definition p = −E′(0)/3, with dk/de = p(k) (`C5_R9-2_report.md:219-224`), reproduces p_U to 1e-4 (`r113_V1_flow_and_numbers.out:1-4` against `r113_tadpoles.out`).
- **H-grav.** R9-9's N-type box graviton, linear: lapse n = −h₀₀/2, shift h₀ᵢ, h_ij, coupled by ½h_μνT^μν, κ = 8πG.
  - Tadpoles live at q = 0, where the box symbol d(q) = q is exact (`C5_R9-9_report.md:38`). So the q → 0 statements are those of linearized GR in ADM form, which is what the 09-14 N-type theory is at λ = 1 (kinetic E:E − ½(trE)², `C5_R9-9_report.md:36`).
  - Mode counts use the continuum symbol. For the box graviton they are exact on the box, and only the symbol changes outside it.
- **Options.**
  - V1: all of h_μν dynamical.
  - V2: h_ii = 0 imposed in the action, with lapse and shift dynamical.
  - V3: h_ii = 0 and h₀₀ = 0 imposed. "Projectable" adds only a homogeneous N(t), which is a time relabelling.
- **Excluded, not addressed:**
  - interactions and loops beyond the zero-point;
  - records as a q-charge (R10-4);
  - nonlinear gravity, except the standard homogeneous Friedmann and Bianchi I identities, which are quoted;
  - edge-SUSY construction (R10-5; used as a control only);
  - the Wilson/staggered Dirac class;
  - q along non-axial directions (irrelevant at q = 0).

---

## 3. Prior art (each counted once)

1. **R5-3 route 1, unimodular Λ** [ref] (`TESTS:2985-2993`; `C5_R5-3_report.md:118-138`).
   - Lemma PT: a c-number vacuum subtraction is undone by Bianchi, leaving Λ_c free; the EW step needs 1 part in 4.7e54.
   - Here: V3's C₀ is the fixed-grid analogue of UG's Λ_c, and V2's f(t) is a new, spatial-trace analogue. Lemma PT's G1 (a full Levi-Civita metric with a free volume) fails in V2/V3, which is why the step can decouple there.
2. **Lane RN L3, "TDiff, unimodular and Hořava are not escapes"** [ref, for the graviton's mass and momentum; `TESTS:809,870`; `RN_L3_report.md:252-262`].
   - The projectable scalar has ω² = −(1 − 2c)Jg k², with no kinetic term at λ = 1, i.e. strong coupling.
   - My V3 mode count (ω² factor, `r113_options.out:10`) is the same point, reached from a different question.
3. **R9-2 free shear** [ref] (`TESTS:3897-3900`).
   - The anisotropic part of the vacuum stress at q = 0 vanishes by cubic symmetry. The shear is a second-order response, R9-2's μ_E (edge-carried; −0.206 L, +0.0080 G). I do not recompute it.
4. **O3** [ref] (`TESTS:2399-2404`; `C5_O3_report.md:98,186`).
   - Untuned cancellation needs matched B/F spectra.
   - Unimodular Λ addresses Λ only (row #6).
   - Imposed rules must be vacuum-referenced (#5/#12).
5. **R4-5** [ref] (`TESTS:2938-2944`). A fixed persistent Z³ allows at most 8.24e184 record events in the stated embedding (`:2941`). It is used in (c).
6. **Repository Λ notes.**
   - `docs/COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md`: spectral-gap Λ = 3/R², with the falsifier "w ≠ −1" at `:106-107`.
   - `docs/UNIVERSAL_GR_INDUCED_COSMOLOGICAL_CONSTANT_BOUNDED_THEOREM_NOTE_2026-06-08.md`: a Euclidean SO(4)-isotropic tadpole, diag 0.8744 (`:22,39`). That is set B's w = −1. Its scope note leaves unimodular and record routes open (`:55-63`).
7. **R10-4** [ref, recorded 18:46Z] (`TESTS:4297-4301`). The minimal conserved-μ q-theory needs μ chosen for the final vacuum. Set A only, so no overlap.
8. **R10-5** [worker, control] (`TESTS:4303-4307`). Theorem Q: an exact free lattice supercharge for the paired content gives zero vacuum energy.
9. **O1 invariant counts** [ref] (`TESTS:2379`). The proper-cubic group has (V, S2) = (1, 2); W(B4) has (0, 1). It is used in (a).
10. **Comparators (RECALLED).**
    - Momentum-cutoff vacuum w = 1/3 (Akhmedov 2002; Koksma–Prokopec 2011).
    - Mukohyama 2009, "dark matter as integration constant" (projectable Hořava).
    - Henneaux–Teitelboim unimodular integration constant.

**Packet and docs grep** (unimodular, volume mode, conformal mode, site creation, p_vac, w = 1/3, Akhmedov, Koksma, spatially unimodular, projectable). Hits: items 1–2 above, `B1_report.md:260` (the conformal mode, a different question), and `C4_F1/F3` (Hořava; graviton sector). No prior computation of the lattice vacuum's pressure or w exists in the packet or `docs/` (the W-native note is Euclidean).

---

## 4. Results

### 4(a) Tadpoles

**Lemma Tad (proved; standard).** For a free scalar field with quadratic Hamiltonian and a bilinear stress of oscillator form, the vacuum expectation is half the forward one-particle value per mode:
- ⟨T⁰⁰⟩ = ⟨ε⟩/2;
- ⟨T^{ij}⟩ = ⟨F^{ij}(k,k)⟩/2.

Here ⟨·⟩ is the zone average (∫d³k/(2π)³, a = 1). Cubic symmetry makes ⟨T^{ij}⟩ = p δ_ij at q = 0, so the anisotropic tadpole vanishes and the shear enters only at second order (R9-2).
- U: p_U = ⟨ε|v|²⟩/6.
- M: p_M = ⟨Σu/ε⟩/6.
- Sea: ρ and p are both −2× the zero-point values, so w is unchanged (reading on normalization). For the gapped edge (the only edge consistent with charged matter, R9-1) at m = 1, per Clifford-flat band: ρ = −3.113, p_U = −0.585, w_U = 0.188 (from the G row below, ×(−2)).

**Identity W (proved; checked to 1e-7 for L/G and 1e-16 for NN, `r113_tadpoles.out`).** For every C² periodic band, with the U stress:

  **ρ_vac + p_vac = −(1/6)⟨ε tr A⟩, A = Hess(ε²/2) − I.**

*Proof.* We have ⟨ε|v|²⟩ = ⟨p·∇ε⟩, since p = ε∇ε. Integrating by parts on the torus gives −⟨ε div p⟩ = −⟨ε(3 + trA)⟩. Then ρ + p = ½⟨ε⟩ + (−3⟨ε⟩ − ⟨ε trA⟩)/6. ∎

Inside the box A = 0, so the right-hand side is edge-supported (box part ≈ 1e-9, quadrature). The departure from w = −1 is an ε-weighted moment of Theorem E's anomaly (`TESTS:3556`), the vacuum counterpart of R9-9's Theorem T and R10-1's photon moments. The m-derivative gives the step version: dρ/dm² + dp_U/dm² = −⟨trA/(12ε)⟩ (checked to ≤ 1e-5, `r113_step_family.out`). For M there is no such identity: p_M − p_U = ⟨(Σu − |p|²)/(6ε)⟩ is edge-supported, since Σu = |p|² in the box.

**Corollary P, positivity (proved).** Pointwise ε/2 + |p|²/(6ε) ≥ ε/2 > 0, and likewise for M. So for every positive band and both couplings:
- ρ_vac + p_vac ≥ ρ_vac > 0, i.e. w ≥ 0;
- ⟨ε tr A⟩ < 0 strictly.

**No edge profile, tuned or not, gives w = −1 for a single species.** Also, no positive vacuum sum over any momentum set (box or not) is boost invariant, because boost invariance needs ⟨T⟩ ∝ η, i.e. p = −ρ < 0. The box makes particles exact, not the vacuum. This is an instance of S11's rule "anything that sums the zone breaks" (`C5_S11_synthesis.md`, §1.3 item 4).

**Table (checked, `r113_tadpoles.out`; per real scalar, lattice units; box = all |kᵢ| ≤ 2).**

| profile | m | ρ (box / edge) | p_U (box / edge) | w_U total (box / edge) | w_M total (edge) | ρ + p_U = −⟨ε trA⟩/6 |
|---|---|---|---|---|---|---|
| L | 1.0 | 1.1938 (0.2876 / 0.9062) | 0.8745 (0.0748 / 0.7996) | 0.732 (0.260 / 0.882) | 0.271 (0.274) | 2.0683 |
| L | 0.3 | 1.0839 (0.2566 / 0.8273) | 0.9661 (0.0833 / 0.8828) | 0.891 (0.325 / 1.067) | 0.326 | 2.0499 |
| L | 0 | 1.0717 | 0.9781 | 0.913 (0.333 / 1.092) | 0.333 | 2.0498 |
| G | 1.0 | 1.5567 (0.2876 / 1.2691) | 0.2925 (0.0748 / 0.2177) | 0.188 (0.260 / 0.172) | 0.296 (0.305) | 1.8492 |
| G | 0.3 | 1.4747 | 0.3107 | 0.211 (0.325 / 0.187) | 0.329 | 1.7854 |
| G | 0 | 1.4661 | 0.3128 | 0.213 (0.333 / 0.188) | 0.333 | 1.7789 |
| NN | 1.0 | 1.3000 | 0.0991 | 0.076 | 0.282 | 1.3991 |

- **Box part = continuum cube cutoff, exactly** (checked): w_box = 0.2602 (m = 1), 0.3246 (m = 0.3) and 1/3 (m = 0), the Akhmedov/Koksma–Prokopec value (comparator, RECALLED).
- **The edge sets the total.** L's edge is stiffer than radiation, and its edge part even has w > 1 at small m (reading: the literal transition region has |v| > 1). G's edge is softer.
- **Edge family (checked).** 1 + w_U runs over 1.14–1.89 and 1 + w_M over 1.27–1.33, for t ∈ [0, 1] and m ∈ {1, 0.3}. There is no zero, as Corollary P requires.

**The step (phase transition: one species' m changes).**
- m: 1 → 0.3, per real scalar (checked):
  - L: Δρ = −0.110, Δp_U = +0.092;
  - G: Δρ = −0.082, Δp_U = +0.018;
  - NN: Δρ = −0.096, Δp_U = +0.010.
- Small-m coefficients (Δρ = c_ρΔm²/a², Δp = c_pΔm²/a²; checked, converged N = 160 → 240):
  - L: c_ρ = 0.1386, c_pU = −0.1400;
  - G: c_ρ = 0.0964, c_pU = −0.0246;
  - NN: c_ρ = 0.1138, c_pU = −0.0144;
  - c_pM/c_ρ = −1/3 exactly for every profile, since Σu/ε³ → 1/ε as m → 0.
- The step is Λ-like (c_p = −c_ρ) only at one edge tuning per species: t* = 0.00117 on the L → G family. L itself is at −1.010 (reading: a near-coincidence of the literal edge).
- **Size (reading; inputs RECALLED).** At a = ℓ_P, the lattice's m²/a² term makes a (100 GeV)² mass step worth Δρ ~ 0.1 Δm² M_Pl² ≈ 1.5e41 GeV⁴ ≈ 6e87 ρ_Λ per real dof. That is 33 decades above Lemma PT's tree-level EW shift (4.7e54 ρ_Λ), because the lattice makes the quadratically divergent piece physical.

**Symmetry count (proved; it is O1's S2 count, `TESTS:2379`).** The number of independent q = 0 stress tadpoles equals the number of invariant symmetric rank-2 tensors of the law's point group on time ⊕ space:
- 2 for proper-cubic × time (sets C and C-box: δ₀₀ and δ_ij);
- 1 for W(B4) (set B: δ_μν) or for Lorentz (set A: η).

So set B's tadpole is forced to w = −1. That is what the Euclidean W-native runner shows (diag 0.8744 × 4, `UNIVERSAL_GR_INDUCED_…:39`). Sets C and C-box have a second tadpole, which is generically nonzero: computed above at O(1/a⁴).

**Two tunings (claim; to the referee, as `TESTS:4182` requires).**
- **Setting.** The linear N-type theory around Minkowski with V1.
- **Two conditions are required.** A static solution requires:
  - ρ̄_tot = 0 (the q = 0 Hamiltonian constraint, whose geometric side tr R(h) vanishes at q = 0);
  - p̄_tot = 0 (the q = 0 trace equation ë = −(κ/6)(ρ̄ + 3p̄)).
- **Both counterterms are allowed (proved).** The two tadpoles c_n∫n and c_h∫h_ii are independent local terms that leave the linear constraint algebra intact:
  - S + c_n is still first class;
  - {S, ∫h_ii} = 0;
  - {G(ξ), ∫h_ii} = 2∫∂ᵢξᵢ = 0 for decaying ξ or on the torus.
- **One covariant counterterm cannot do it (proved for one species; checked for every computed entry).** A single covariant Λ√−g counterterm cancels only the direction ρ = −p. The vacuum vector (ρ_vac, p_vac) is not along it: (ρ + p)/ρ = 1.08 to 1.91 across the nine computed (profile, m) entries. So the bare law needs two tuned coefficients, each to about 1e-123 (ρ_vac ~ 1/a⁴ = 8.8e122 ρ_Λ at a = ℓ_P).
- **Pairing removes both.** With exact boson–fermion pairing on identical bands, the strain acting identically on partners, both supertraces vanish together. That is one structural condition, not a tuning (suggested; consistent with O3 [ref] and R10-5 Theorem Q [worker]).

### 4(b) Decoupling per option in the linear N-type theory

**Lemma BR, Bianchi recovery (proved; the identity is checked symbolically, `r113_options.out:1`).**
- Let E_μν = G_μν[h] − (κ/2)T_μν. Linearized Bianchi plus matter conservation give ∂^μE_μν ≡ 0.
- An option that freezes components of h imposes only the E-components conjugate to the free ones. Bianchi returns the rest, up to integration data:
  - **V1:** all ten E_μν = 0 (GR).
  - **V2** (h_ii frozen): E₀₀, E₀ᵢ and the traceless E_ij are imposed. The ν = j component gives −∂₀E₀ⱼ + ∂ᵢE_ij = ∂ⱼ(E_kk/3) = 0, so **E_kk = f(t)**: a free homogeneous function absorbs the homogeneous pressure.
  - **V3** (h_ii and h₀₀ frozen): additionally, ν = 0 gives ∂₀E₀₀ = ∂ᵢE_i0 = 0, so **E₀₀ = C(x)**, static and arbitrary. This is the fixed-grid form of "dark matter as integration constant" (comparator, RECALLED).

**Mode counts (checked, `r113_options.out:7-10`; Bianchi identity at `:1`).** Reduced determinants of the linearized Einstein–Hilbert form at q ∥ z, with each option's residual gauge removed:
- V1: −16q⁸(ω² − q²)²;
- V2: −16q⁸(ω² − q²)², the same two TT modes as GR, no extra mode;
- V3: −64q⁶ω²(ω² − q²)², an extra root at ω = 0 and no tachyon or ghost at linear order. The root is the static sector: it carries C(x), and the static residual reparametrization ξ₀(x) becomes a null direction there. This is RN L3's projectable λ = 1 point, "no kinetic term … strongly coupled" (`RN_L3_report.md:50,256-262`). Strong coupling is a nonlinear statement, taken from RN L3 and its literature, not checked here.

**Phase-transition step per option (proved at linear order, given Lemma BR).** A homogeneous transition converts vacuum energy into latent heat:
- at fixed volume, Δρ_tot = 0 (energy conservation, no 3H(ρ + p) term);
- the pressure jumps by Δp_tot = Δp_vac − Δρ_vac/3.

| | Constant vacuum (ρ_vac, p_vac) | Homogeneous step | Local bubble (q ≠ 0) |
|---|---|---|---|
| V1 | ρ̄ is a constraint tadpole; p̄ drives ë = −(κ/2)p̄ (at ρ̄ = 0). **Sourced, two coefficients** | Δp_tot ≠ 0 drives the trace: e.g. L, m 1 → 0.3: Δp_tot = +0.092 + 0.037 = +0.128 per real scalar. Expansion and contraction are sourced. After dilution the vacuum difference (Δρ_vac, Δp_vac) remains | Δρ sources curvature through the constraint; Δp gradients through the trace (EP-correct) |
| V2 | ρ̄_tot = 0 is required (q = 0 constraint; nonlinear Bianchi I at fixed volume: ρ̄_tot = −σ²/2κ ≤ 0, comparator). p̄ goes into f(t). **Sourced, ρ only** | Δρ_tot = 0 keeps the constraint; Δp goes into f(t). No homogeneous source | Δρ sources curvature (constraint) |
| V3 | ρ̄ goes into C₀ and p̄ into f(t). **Decoupled** | Nothing sourced | Only ∂ₜρ sources (E₀₀ static), so energy that moves or changes gravitates. Static fields are integration data C(x) |

- **The V2 sign condition (reading, comparator).** Only the homogeneous statement is used: Bianchi I at fixed volume, ρ̄_tot = −σ²/2κ ≤ 0. A pointwise T³ positivity argument would need tr K = 0 pointwise, which a divergent shift evades, so it is not claimed.
- **Not a no-go beyond its class.** The V1 row is linearized GR with a lattice-computed source. It shows SOURCED with computed coefficients; it is not a no-go for other gravity sectors.

### 4(c) Expansion per option

**V1, growing spacing.** This is consistent with the N-type algebra, and the physical spacing is a(t)·a₀. Consequences:
- **The vacuum becomes a fluid** (checked, `r113_V1_flow_and_numbers.out`, `r113_steps_sizes.out`).
  - With a fixed comoving cutoff, the zero-point per site E(V) is a barotropic fluid with running w. Under U: L m = 1 gives w = 0.73 → 0.52 → 0.27 → 0.21 at e = 0, 0.1, 0.5, 1. Under M, w = 1/3 exactly for m = 0, falling toward 0 for m > 0.
  - After a Λ counterterm tuned at e = 0, the residual ρ(e) − ρ(0) is −0.45 at e = 0.1, about 40% of ρ_vac, i.e. about 4e122 ρ_Λ.
  - Cancelling at all epochs needs a whole per-site function f(V) (allowed: ∫Nσf(√h/σ) with fixed site density σ, reading), or pairing.
- **Rapidity budget (reading; inputs RECALLED).**
  - η*_p = asinh(B/(a m_p)) = 45.4 at a = ℓ_P.
  - In V1 it varies as ln(1 + z): 66 at BBN if a = ℓ_P today, and 10.4 after 35 e-folds of the future de Sitter phase.
  - If instead a = ℓ_P at T ~ M_Pl, the spacing today is 5.2e31 ℓ_P ≈ 0.8 mm, with the box edge at about 5e-4 eV. Every collider process would leave the box (excluded, reading).
- **Scale reference (`AX:189-190`).** a/ℓ_P becomes a dynamical variable (the volume mode). "The natural unit equals ℓ_P" can hold at one epoch only. Under the induced-gravity reading (M_P² ∝ J/a²), G ∝ a(t)², i.e. Ġ/G = 2H ≈ 1.4e-10/yr, against lunar-ranging bounds of order 1e-13/yr (RECALLED). That is excluded *if* G is induced; R9-9's M is supplied, so this is conditional.

**V2 and V3, fixed volume per site.**
- **Without site creation (worker reading; referee required).**
  - Physical volume = N_sites × √h a₀³ is constant, so there is no isotropic expansion.
  - A homogeneous lapse is a time relabelling under universal coupling, so it gives no cosmological redshift.
  - Volume-preserving shear gives direction-dependent redshifts with blueshifted directions.
  - Observed isotropic redshift–distance, CMB T(z) ∝ 1 + z and supernova time dilation (RECALLED) exclude this. Both options are **EXCLUDED as fixed-site options**.
  - Also, after any phase transition the latent heat can never dilute, so there is no cooling (reading).
- **With site creation (a Lattice price; the owner's "count rises" tested only as a hypothesis).**
  - **Spacing.** It stays fixed in physical units, so a = ℓ_P at every epoch: the scale reference holds as a constant identity, and the rapidity budget is fixed at 45.4. This is the one structural advantage over V1 (reading).
  - **Counts (reading).** 8.5e184 Planck cells in today's observable universe, comparable to R4-5's cap of 8.24e184 (`TESTS:2941`). The creation rate is 3H₀N ≈ 5.6e167 s⁻¹, or 3.6e-61 per site per Planck time.
  - **What the rule must do (suggested).**
    - stretch field configurations, so that photons redshift and particle numbers are kept (a non-local refinement map);
    - set its rate so that H² = κρ_non-vac/3 holds (BBN/CMB H(z)), which ties the count to non-vacuum energy.
  - **Where V3's decoupling then goes (suggested).** New sites need C-values.
    - A fixed law constant C₀ makes each post-transition vacuum's Δρ gravitate on new sites: Lemma PT's tuning to the final vacuum returns.
    - A vacuum-tracking C is O3's vacuum-referenced rule (#5/#12, P13).

    So the tuning relocates; it is not removed. Reading: OPEN.
  - **The records link (suggested).** With "one record per site, permanent" (`AX:79-80`), a fixed Z³ freezes once every site is recorded (R4-5's cap). Continued formation ("no sealed box") would need site creation. That gives the hypothesis a reason, but the axioms supply no rate law tying it to H (suggested).

### 4(d) Prices (named, not adopted)

- **V1.**
  - (P-V1a) two bare tadpole coefficients, each tuned to about 1e-123, or a full per-site counterterm function over the expansion history, or exact B/F pairing on identical bands;
  - (P-V1b) a/ℓ_P is dynamical: the scale-reference identification holds at one epoch;
  - (P-V1c) if gravity is induced, G varies as a² (excluded); otherwise M_P is a supplied constant.
- **V2.**
  - (P-V2a) fixed √h per site, a reading on the Lattice text (`AX:37-41` fixes sites and adjacency, not a metric);
  - (P-V2b) one tuning, ρ̄_tot ≤ 0 (to the excitation content);
  - (P-V2c) site creation (Lattice) with a redshifting refinement map and a Friedmann-tracking rate.
- **V3.**
  - (P-V3a) as P-V2a, plus a frozen lapse: an ω = 0 scalar, strongly coupled at λ = 1 (RN L3);
  - (P-V3b) static gravitational fields are integration data C(x);
  - (P-V3c) the residual Λ is the integration constant C₀ (named, unexplained);
  - (P-V3d) as P-V2c, plus a rule for new sites' C, either a constant (Lemma PT-type tuning returns) or vacuum-referenced (P13/R₀).
- **No axiom text is changed by this probe.** Site creation would change Lattice ("Physical sites are the points of the cubic lattice Z³", `AX:37`).

---

## 5. Notes for the referee and the record

- **Referee items.**
  - The "two tunings" claim in V1 (§4(a), last part).
  - V2's and V3's EXCLUDED as fixed-site options (§4(c)).
- **Strongest claims and their scope.**
  - Identity W and Corollary P: proved for any C² periodic band with U, and P also for M. Free fields, zero-point or Clifford-flat sea.
  - Lemma BR: proved at linear order.
  - Everything about site creation is suggested or reading.
- **Strong-word check.**
  - "never −1": scoped to a single positive band, both couplings.
  - "decoupled": linear order, V3, constant vacuum and homogeneous steps at fixed volume.
  - "excluded": fixed-site V2 and V3 against observed isotropic expansion, a worker reading.
- **What would change the picture.**
  - A gravity sector whose q = 0 trace coupling is not ½h_ii T^ii.
  - A vacuum completion with negative pressure per mode (not a positive bilinear).
  - A site-creation law derived, not supplied.

---

## 6. Files

- Report: `.../scratchpad/C5/R11-3/R11-3_report.md`.
- Scripts and outputs: `.../scratchpad/C5/R11-3/scripts/`:
  - `r113_profiles.py`;
  - `r113_tadpoles.py/.out`;
  - `r113_steps_sizes.py/.out`;
  - `r113_step_family.py/.out`;
  - `r113_V1_flow_and_numbers.py/.out`;
  - `r113_options.py/.out`.
