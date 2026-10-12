# C5 R13-3 report: Λ, the P-T creation law in a lumpy universe (inhomogeneous completion, bound regions, phase transitions)

**Worker.** Claude Opus 5.5 (same family as the supervisor, S14 and every C5 worker). Unrefereed. 2026-10-12, 20:13Z to 20:41Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R13-3/`. Scripts and outputs in `S/scripts/` (each runs in under 5 s at `OMP_NUM_THREADS=2`):
- `r133_linear.py/.out`: sympy. Linear scalar perturbations of V3 + creation in the unit-lapse (synchronous) slicing: which Einstein equations are implied, how the Hamiltonian-constraint violation C propagates, and how a creation-law memory feeds it.
- `r133_bound.py/.out`: exact EdS virial-radius orbital period vs collapse time; ΛCDM spherical collapse; the unit-lapse normals in a top-hat; Raychaudhuri focusing in a halo; the filter-error floor.
- `r133_transition.py/.out`: Prony leakage at a phase transition with two specified transition sectors; Prony orders N = 2, 3; widths from percolation scale to a single wall passage.
- `r133_de_encoder.py/.out`: the creation-clock mean with the stationary age density (fixes the R12-2 referee's 5.56%), and Prony visibility of constant-w and CPL dark energy.

**Read.** In full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (`AX`); `TESTS.md:2302-2320` (C5 method) and `:4560-4656` (round 13, my item `:4621-4641`); `agents/C5_S14_synthesis.md`; `SUMMARY.md:534-675` (§§21–25); `agents/C5_R12-2_report.md`; `C5_R12-2_referee_verdict.md` and the scratch referee checks (`ref_R12-2/scripts/referee_r122_checks.py/.out`, `r122_frw_rules.py`); `C5_R11-3_report.md`; `C5_R11-3_referee_verdict.md`; `C5_R10-4_referee_verdict.md`; `C5_R5-3_referee_verdict.md`; `TESTS.md:2985-2993`. In part: `C5_R10-4_report.md:1-60`; `RN_L3_report.md:252-266`; `RN_L3_referee.md:14-15`. Results of rounds 6–12 were read through S14 §§1–3 and SUMMARY §§23–25, not line by line.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `vR12-2` = `P/agents/C5_R12-2_referee_verdict.md` (similarly vR11-3, vR10-4, vR5-3). `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.

**Labels.** proved / checked (numerics or sympy here) / suggested / reading / comparator. Comparators are RECALLED (from memory) unless stated; none was fetched this run.

**Subtraction rule (R9-3 rule, `TESTS.md:4566`).** Every leak, residual or decay clause names its subtraction before the run:
- "ε" (transition leak) = ρ̂/ρ_nc − 1, where ρ_nc is the exact non-vacuum density at the site (radiation + dust + released latent heat). Nothing else is subtracted. "Decays" means |ε| < 1e-6 at u ≥ u_T + 10W (printed; it holds to ≤ 3e-5 in every row, see §4(d)).
- "C" = the Hamiltonian-constraint violation E_00 of the non-vacuum stress (G_00 − κT^nc_00). With a w = −1 vacuum, the vacuum enters only as −ρ_v g, whose divergence vanishes in every metric.
- "δH²/H²" (averaging) = the mean creation rate squared over the Friedmann value for the full mean density, (⟨c⟩/3)²/((κ/3)ρ̄_tot,nc) − 1.
- Δ_vir is relative to the background matter density at collapse (EdS) or to the critical density (ΛCDM), as labelled.

**New-rule note (`TESTS.md:4566`).** No PASS/VIABLE clause is claimed, so no perturbative-order statement is owed. Every "proved" below says whether it is linear or nonlinear.

---

## 0. Verdict against the FIXED readings (`TESTS.md:4636-4639`)

**Worker reading: EXCLUDED in a bounded class 𝒱3, for the referee. OPEN outside it.**

**𝒱3 (stated before the title).** This is the registered setting (`TESTS.md:4625`):
- V3: unit lapse at every site (N = 1, nonlinearly; §4(c) states the scope) and fixed proper volume per site;
- site creation by **any** local law with finitely many memory variables per site;
- conserved non-vacuum matter obeying the strong energy condition inside bound matter;
- a vacuum that is either w = −1 or absent from the imposed equations (H-vac-Λ, §2);
- adiabatic initial conditions.

**The inconsistency (Lemma F, §4(c); proved, nonlinear, via Raychaudhuri).**
- A unit lapse makes V3's preferred time slicing a *geodesic* slicing. Its normals form a cold, irrotational geodesic flow.
- In every collapsing region those normals focus to a caustic:
  - at exactly t_coll in a top-hat (checked: θ·t_coll = −1.2e4 at η = 1.999π);
  - for normals entering a virialized Δ = 200 halo with θ = +3H, after 0.17/H, which is less than one crossing (checked).
- So the lattice's global time cannot be continued through any virialized region. **This does not depend on the creation law.**
- The question "is the creation rate zero inside without a clamp?" therefore has no V3 setting in which to be asked.
- Prior art: RN L3 lists "caustics" for projectable Hořava as literature (`RN_L3_report.md:264`). Izumi–Mukohyama 2009 found a "dynamical stellar centre" in projectable Hořava (RECALLED). Neither was applied to V3 or to P-T before.

**Why the obvious escapes do not rescue P-T inside the class family.**
- **Stiffen the projectable foliation.** RN L3, refereed: the projectable scalar is a ghost or a tachyon for λ ≠ 1 and has no kinetic term at λ = 1 (`RN_L3_report.md:256-259`; `RN_L3_referee.md:14`).
- **Make the lapse dynamical (V2 + creation).** This re-imposes the homogeneous Hamiltonian constraint 3H² = κρ_tot (`vR11-3:51,80`). P-T's H² = (κ/3)ρ̂_nc then agrees with it only if ρ_v = 0 (Lemma T, §4(c); proved, homogeneous). That is Lemma PT again.
- **The one named escape** is a lapse whose local part is dynamical but whose spatial zero mode is fixed. It imposes the Hamiltonian constraint for k ≠ 0 only, which is a global, non-local condition (price P-r13a). That class is **OPEN**: nothing here excludes it, and I did not build it.

**Not VIABLE, on every probe.**
- (b) passes in form: growth and ISW are GR's (Lemma N), with C acting as dust. It needs (e).
- (c) fails in 𝒱3 (Lemma F).
- (d) passes for Standard-Model transitions (transient leakage, all before BBN). It needs a pre-filter or clamp at wall passages.
- (e) passes only for dark energy made of a finite constant-w mixture. DESI-type CPL is not reconstructed at N ≤ 5.
- A per-site P-T reading also undercounts the collapsed mass in the mean expansion (Lemma A, suggested).

**Against the expectation (`TESTS.md:4640`).**
- (c): the expectation was "memory ≥ the longest bound-orbit period". This is confirmed and made exact: at the virial radius T_orb = t_coll in EdS. But it is pre-empted by Lemma F.
- (d): "leaks at roughly the latent-heat fraction" is confirmed only for slow transitions (W ≳ 0.15). Sharp transitions leak ∝ α/W, and the leak goes negative when α/W ≳ 10.
- (b): "C(x) acts as dust with unexplained initial data" is confirmed, with a refinement. The zero-mean part decays relative to the growing mode. A clustering mean C needs a dust-like creation memory.

---

## 1. In plain words

- **Most of the creation pattern is invisible.** On this grid the gravity equations that are kept already fix how lumps of matter grow, exactly as in general relativity. They also leave one extra ingredient: a frozen-in "dust" that comes from the dropped energy equation. Where new sites appear decides only where the grid points sit. It does not decide how galaxies form. The creation law matters through one number per moment: its average, which is the expansion rate.
- **The frozen dust (C).** The extra ingredient behaves exactly like cold dust that falls freely, and its amount is whatever it was at the start. If the creation law carries a dust-like memory, this dust clusters exactly like cold dark matter ("dark matter as integration constant"). Its amount is then a free number, not explained.
- **Galaxies break the grid's clock.** On this grid, every site's clock ticks at the same proper rate (the "fixed lapse"). The surfaces of equal grid time are then traced out by freely falling observers. Where matter collapses into a galaxy, those observers fall in, cross one another, and the grid's "now" folds over itself. This happens in every galaxy, within about one crossing time, and nothing in the creation law can stop it.
- **The cures cost the thing P-T was for.** Giving the grid's clock some stiffness makes the extra scalar a ghost or a tachyon (an earlier, refereed result). Letting the clock rate vary from site to site brings back the energy equation, and the vacuum energy gravitates again. What is left is a clock whose *average* rate is fixed while its local rate varies. That is a global rule, not a nearest-neighbour one.
- **"Ignore what is constant" also ignores galaxies.** A galaxy's matter, sitting at a site, is as constant in time as the vacuum. A per-site rule that ignores constants also ignores galaxies, so it undercounts the matter that drives the average expansion. That is roughly 10% in H at late times (estimate). Avoiding this needs memory carried by the matter, or reading over very large regions.
- **Phase transitions are fine for known physics.** The electroweak and QCD transitions disturb the reading only while they happen, long before nucleosynthesis. A sharp wall passing a site gives a nonsense (negative) reading for a moment, so the rule needs a smoothing filter or a clamp there.
- **Dark energy must be "simple".** The rule sees dark energy only if its w differs from −1. It reconstructs it exactly only if it is a few components with constant w. The evolving dark energy DESI hints at is reconstructed wrongly, by factors of order one.

---

## 2. Hypotheses and classes (before titles)

- **H-V3c** (`C5_R12-2_report.md:73-75`): unit lapse; fixed proper volume per site; shift and traceless h_ij dynamical. The imposed equations are E_0i = 0 and E_ij^TL = 0 (`vR11-3:51`). Sites are created at local rate c ≥ 0 (H-perm, `C5_R12-2_report.md:77`).
- **H-vac-Λ.** The vacuum entering the *imposed* equations is a w = −1 c-number, or is absent. This is what R12-2's B-loc used (`C5_R12-2_report.md:216`).
  - **H-vac-grid** (alternative, §4(c) Lemma G′): R11-3's refereed w ≥ 0 grid zero-point (`vR11-3:35-41`), carried in the lattice rest frame with inertia ρ_v + p_v ~ a⁻⁴.
  - Which one holds is a source/action bridge (`AX:187`). I keep both.
- **H-matter.** Non-vacuum matter is conserved and obeys the strong energy condition inside bound matter. Latent heat goes into a specified sector (§4(d)).
- **H-adi.** Adiabatic growing-mode initial conditions.
- **H-read** (as R12-2). The creation law reads local stress and its derivatives along the site worldline, plus finitely many per-site memories.
- **Excluded:** records as a q-charge (R10-4); pairing; bubble-wall dynamics beyond a tanh release profile; Prony orders above 5; nonlinear claims beyond those labelled.
- **Excluded outside realizations, not covered by any claim:**
  - a continuation of the slicing through caustics as kinks or shocks;
  - negative C-dust comparable to the matter density inside halos;
  - a lattice-scale completion in which the unit-lapse slicing is not a continuum geodesic slicing;
  - non-metric redshift mechanisms.

---

## 3. Prior art (each counted once)

1. **R12-2 and its verdict** [ref].
   - L-CR (mean c̄ = 3H) and L-hom (`vR12-2:5`).
   - The F-law. Transitions leak: m₂ = 16ρ_r + 9ρ_m − 4Δs′, with 0.9% and 2.2% errors (`vR12-2:7`).
   - Lemma G is only for density-only, comoving, memoryless laws (`vR12-2:9`).
   - The clock mean is 5.56% high (`vR12-2:11`).
   - P-T is a zero-frequency projector (`vR12-2:13`).
   - The open items are bound regions and the inhomogeneous completion (`vR12-2:15`).
   - The worker flagged "matter flows through sites: OPEN" (`C5_R12-2_report.md:196`). Lemma N below closes that case at linear order.
2. **R11-3 and its verdict** [ref].
   - Lemma BR. V3 has E_00 = C(x) and E_kk = f(t) (`vR11-3:51`).
   - The ω = 0 null is a static gauge/integration sector, not a proved physical scalar (`vR11-3:53`).
   - The transition sector must be specified (`vR11-3:55`).
   - Fixed-site V3 is EXCLUDED; site creation is OPEN (`vR11-3:57,81`).
   - The worker cited Mukohyama 2009 as a comparator (`C5_R11-3_report.md:97,185`).
3. **R10-4** [ref] (`vR10-4:27`). A different set (set A, q-charge), so no overlap. Counted once, as the registration asks.
4. **R5-3 Lemma PT** [ref] (`TESTS.md:2986-2987`; `vR5-3:5-7`). It is what Lemma T reproduces.
5. **RN L3** [ref] (`RN_L3_report.md:252-266`; `RN_L3_referee.md:14`). The projectable scalar: ω² = −(1 − 2c)Jg k², which is a ghost, a tachyon, or has no kinetic term at λ = 1. It lists "caustics" (Blas–Pujolas–Sibiryakov) as literature. **This is the nearest prior art to Lemma F.** RN L3 did not connect it to V3's preferred slicing, to bound regions, or to P-T.
6. **O3 P13 / #5, #12** (`C5_O3_report.md:87,97,104`, via R12-2 §3). A vacuum-referenced rule. P-T replaces it.
7. **Grep of the packet and `docs/`** (mimetic, Izumi, caustic, Painlevé, geodesic slicing, projectable, integration constant). No V3/foliation-caustic, mimetic or Painlevé–Gullstrand treatment was found. The hits are items 2 and 5, the unimodular rows (`TESTS.md:2889`, `C5_R4-5_report.md:227`), and unrelated optical caustics (C3 G-L).
8. **Comparators (RECALLED):**
   - Mukohyama 0905.3563 (dark matter as integration constant; projectable Hořava);
   - Chamseddine–Mukhanov 2013 and Chamseddine–Mukhanov–Vikman 2014 (mimetic dust = CDM at linear order);
   - Izumi–Mukohyama 0911.1814 (stellar centre is dynamical in projectable HL);
   - mimetic caustics (Barvinsky 2014; Babichev–Ramazanov 2017);
   - Hamilton–Lisle river model (Painlevé–Gullstrand: unit lapse, flat slices);
   - Buchert averaging;
   - Press–Schechter collapsed fractions;
   - EDE bounds (f_EDE ≲ 0.07–0.1 near z_c ~ 3500);
   - ΔN_eff ≲ 0.3 (BBN/CMB);
   - DESI DR2 CPL w₀ ≈ −0.75, w_a ≈ −0.86.

---

## 4. Results

### 4(a) The local 3D rule, the encoder and c̄ = 3H

**Pointwise number balance (proved; exact, nonlinear).**
- Fixed proper site density n plus creation c per site gives ∇_μ(n u_s^μ) = n c, so **c = θ_s**, the expansion of the site congruence.
- Relative to the unit-lapse normals, c = θ_n + D·V, where V is the site drift relative to the normals. This is R12-2's c = 3H + ∂_iV^i made pointwise.
- **Mean (proved, as L-CR):** under statistical homogeneity, ⟨D·V⟩_vol = 0, so ⟨c⟩_vol = ⟨θ_n⟩_vol ≡ 3H.

**The rule, stated per site s.** These are the registered F-law ingredients made explicit.
- **Reading.** Prony-order-N moments m_k = (−d/du)^k ρ̃_s, k = 1…2N, of a pre-filtered local stress ρ̃_s. The pre-filter is first order, time constant τ (§4(d)). Here u is the site's own creation count: d/du = (3/c)d/dt.
- **Output.** ρ̂_s = Σ w_i/x_i.
- **Memory.** X_s, with Ẋ_s = −2H_sX_s (curvature-like) or −3H_sX_s (dust-like, §4(b)).
- **Rate.** c_s = 3H_s, with H_s² = (κ/3)ρ̂_s + X_s.
- **Encoder.** The S4 integrate-and-fire clock with an axis cycle (`C5_R12-2_report.md:245-253`). The 3D dislocation geometry is still **not built** (price S1 unchanged).

**Encoder mean, corrected (proved; checked).**
- The referee's 5.56% excess (`vR12-2:11`) is an artefact of *uniform* initial phases.
- With the stationary age density of an exponentially growing population, p(φ) = 2 ln2 · 2^{−φ}, the mean count is exactly 2^Φ for every Φ. Exact rationals: 1.000000000000 at Φ = 3.3, 6.6 and 0.5, against 1.0559, 1.0556 and 1.0607 for uniform phases.
- The quasi-periodic version, φ_i = −log₂(1 − frac(iγ)/2), keeps both the exact mean and the O(log N) noise. Window std is 6.6 and 62.9 at Φ = 3.3 and 6.6, against 451 and 4409 for random stationary phases (`r133_de_encoder.out:1-7`).
- The price remains an ordered initial phase field (S4).

### 4(b) Linear perturbations: growth, ISW, and what C(x) is

**Lemma N (proved at linear order around flat FRW, under H-vac-Λ; checked in sympy, `r133_linear.out`).**
- V3's slicing is the unit-lapse (synchronous) slicing. Work in Ma–Bertschinger variables (h, η) for one barotropic fluid with any w and c_s².
  1. **(T) is implied.** (S) − (T) − (6/k²)[(M)′ + 2ℋ(M)] = 0 identically, given the fluid equations (`r133_linear.out:2`). So for k ≠ 0 the unimposed spatial-trace equation (T) follows from the imposed momentum (M) and traceless (S) equations. This is the ν = j Bianchi component.
  2. **The unimposed Hamiltonian equation (H) obeys (H)′ + ℋ(H) = (χ/2) h′,** where χ = X a² is the F-law's curvature-like memory (`r133_linear.out:3-4`).
     - With χ = 0: (H) ∝ 1/a, i.e. δE⁰₀ ∝ a⁻³ at fixed synchronous coordinates. **C is a pressureless dust with zero sound speed, at rest on the geodesic normals.**
  3. **So for k ≠ 0, V3 + creation is GR's synchronous evolution system plus that dust.** The creation law does not appear in (M), (S), (T) or the fluid equations. Its k ≠ 0 part fixes only the map between synchronous and site coordinates, i.e. the site drift (V, E).
- **Consequence:** R12-2's open case is settled at linear order (`C5_R12-2_report.md:196`; `vR12-2:9`). When sites may drift relative to matter, **any** creation law gives GR growth. Lemma G's δ ∝ a^{−3/2} needs sites forced to comove with matter.

**Growth D(a) and ISW (proved, linear, from Lemma N).** Both are GR's, for:
- the background H(a) set by the mean creation rate (L-hom, `vR12-2:5`);
- the clustering content: baryons, CDM, and C if it has a mean.

So (b) passes the growth and ISW comparators exactly as wCDM does. The condition is that (e) supplies a wCDM-like H(a) (reading).

**C(x): defect or feature?**
- **Zero-mean C** (C-data with no homogeneous part; proved, linear). δρ_C = C(x)/a³ is static in comoving coordinates. It does not grow, because its background is zero. Relative to the matter growing mode (δρ_m ∝ a⁻²) it decays as a⁻¹. Its amplitude is pure initial data.
- **Dust-like creation memory** (H² = (κ/3)(ρ̂ + ρ_d), with ρ_d ∝ a⁻³ a per-site memory, not in T; proved, linear). The coefficient becomes 2πG a² ρ_d h′, i.e. (a³δρ_C)′ = −(a³ρ_d/2)h′ (`r133_linear.out:6`). **C clusters exactly like synchronous-gauge CDM** with mean ρ_d. This is Mukohyama's "dark matter as integration constant" in V3 form (comparator, RECALLED).
  - *Feature:* it could be all of the dark matter at linear order.
  - *Defect:* its amount Ω_d h² ≈ 0.12 is a free integration constant of the creation memory. It rides the same normals as Lemma F, so it fails at the first shell crossing unless completed.
- **Curvature-like memory** (the registered F-law). It acts as a w = −1/3 fluid at rest on the normals with ρ_X = 3X/κ (`r133_linear.out:5`). Its source for C is ∝ Ω_X δ, which is small while |Ω_K|-type memory ≲ 3e-3 (DESI DR2 10³Ω_K = 2.3 ± 1.1, `TESTS.md:2993`).
- **What sets C's amplitude:** nothing in the law. Creation does not touch C, because C is a property of the slicing, not of the sites. C is the slicing's initial data plus whatever dust-like memory the creation law carries. Reading: "unexplained initial data", as expected.

**Lemma A, the averaging condition (proved: H = ⟨c⟩_vol/3; the size is suggested).**
- Under P-T, a site inside a virialized region sees time-constant stress, so ρ̂_s = 0 there. **A per-site P-T reading cannot tell a galaxy from a cosmological constant.**
- A memoryless local rule then gives H² ≲ (κ/3)[ρ̄_DE + (1 − f_coll)ρ̄_m], by Jensen's inequality, if unbound sites read ρ̂_s ≤ ρ_s (assumption, not proved). So δH²/H² ≈ −f_coll(z)Ω_m(z).
- With f_coll ≈ 0.5 at z = 0 (RECALLED, Press–Schechter-type), H₀ comes out about 8% low. Near z ≈ 1, using an assumed f_coll of about 0.3 (my guess, not a recalled number) and Ω_m(1) = 0.78, H(z) is about 12% low. BAO and SN measure H(z) to about 1–2% (RECALLED), so this is excluded *if* the estimate holds.
- In GR, voids out-expand the mean and compensate. The F-law can do the same only if its memory X is the separate-universe curvature of the matter now at the site. Lemma N lets sites drift, so the memory must be **Lagrangian (carried by matter)**, or the reading must be coarse-grained over the homogeneity scale (~100 Mpc). Price P-r13b.

### 4(c) Bound regions

**Lemma VO, the virial-radius orbit (proved, exact; checked).**
- For an EdS top-hat with Δ_vir = 18π² relative to the background at t_coll, the circular period at r_vir is **T_orb(r_vir) = t_coll**, exactly (`r133_bound.out:1`). Equivalently T_orb · H(t_coll) = 2/3.
- For Δ_c relative to critical, T_orb H = 2π√(2/Δ_c), which is 0.63 for Δ_c = 200.
- ΛCDM (Ω_m = 0.3) collapse today (numerical, r_vir = R_max/2): Δ_vir = 92.7 relative to critical (Bryan–Norman RECALLED: 101), T_orb(r_vir) H₀ = 0.923, **T_orb/t₀ = 0.957**.
- **Consequence (checked).** A P-T pre-filter must pass the cosmic dilution signal (rate H) and reject orbital-period variation. At r_vir no time constant does both: the least achievable max(lag Hτ, ripple (T/2πτ)ⁿ) is 0.22 (n = 2) and 0.14 (n = 8) in EdS, and 0.28 and 0.18 in ΛCDM (`r133_bound.out`, rows (5)). Deeper in, at T H = 0.2, it is 0.10 and 0.05.
- So the expectation's "memory ≥ longest bound-orbit period" is right and sharp: **memory ≳ t_coll ~ the Hubble time at collapse.** This makes the rule non-local in time (price P-r13c).

**Lemma F, the foliation caustic (proved, nonlinear, for class 𝒱3; numbers checked).**
- *Setup.* The unit lapse gives zero acceleration of the normals (a_μ = D_μ ln N = 0, standard ADM), so the normals are geodesic. They are hypersurface-orthogonal, so ω = 0. Raychaudhuri (a geometric identity) reads θ̇_n = −θ_n²/3 − σ_n² − R_nn.
- *The V3 equations give R_nn.* R_nn = ½(G_nn + h^{ij}G_ij) = (κ/2)(ρ + 3p)_nc + ½(E_nn + E^k_k).
  - Under H-vac-Λ the w = −1 vacuum contributes zero net (P-T's E = κρ_v δ^μ_ν cancels −κρ_v g).
  - E_nn is the C-dust.
  - E^k_k is homogeneous: proved at linear order (Lemma N.1); suggested nonlinearly, from the ν = j identity with a_j = 0.
  - Today the homogeneous term equals −3ä/a ≈ −1.5H₀² (RECALLED q₀ ≈ −0.5). The matter term inside a Δ = 200 halo is (κ/2)ρ_vir ≈ 300 H₀². So R_nn > 0 inside bound matter, unless C is negative and comparable to the matter density (excluded realization).
- *Top-hat.* Under H-adi the normals' velocity relative to CDM decays as 1/a (MB synchronous θ_c′ = −ℋθ_c). The normals are then the closed-FRW comoving observers of the interior. **θ_n → −∞ at t_coll**: θ·t_coll = −1.19e2, −1.2e3, −1.2e4 at η/π = 1.9, 1.99, 1.999 (`r133_bound.out`, row (3)). This is a point caustic of the unit-lapse slicing.
- *Normals entering a virialized halo* (Δ_c = 200, θ_entry = +3H, using only R_nn ≥ 4πGρ_vir and σ² ≥ 0):
  - θ turns negative after 0.010/H;
  - it reaches −1e6 H at 0.167/H (`r133_bound.out`, row (4));
  - a diameter crossing is ≈ T_orb/2 = 0.31/H, so the caustic forms within one crossing.
  - This does not need comoving normals. Normals at rest inside a well would be accelerated, so normals there must fall.
- **Statement.** In 𝒱3 the preferred slicing (the lattice's global time) develops a caustic in every collapsing or virialized region, by t_coll for a top-hat and within one crossing time for a halo. **The creation law plays no role.** V3 cannot be continued through the observed galaxies and clusters. This is the inconsistency I give the referee (§0).
- **Scope of "fixed lapse" (stated).** Lemma F uses the literal nonlinear reading **N = 1** (the lapse is fixed; R12-2's H-V3c, `C5_R12-2_report.md:73`). At linear order it coincides with R11-3's "h₀₀ frozen" (`C5_R11-3_report.md:183-185`).
  - An alternative nonlinear reading is g₀₀ = −1 along site worldlines: site clocks tick at the global rate, so N² = 1 + β². Under it the normals are accelerated, and Lemma F does **not** apply as stated.
  - **For that reading I show only (suggested):** sites at rest in a static well desynchronize. Their t = const slices become null after t ≈ c/g: about 1 yr at the Earth's surface, about 13 days at the solar surface, and about 1e11 yr in galactic potentials (g ~ 1e-10 m/s²). Sites inside stars and planets must therefore move. Whether accelerated, synchronized site flows exist without crossing is not computed.
  - **So the referee's class is 𝒱3 with N = 1.**

**Lemma T, the lapse trade-off (proved, homogeneous).**
- **V2** (dynamical lapse, fixed volume per site) imposes the homogeneous Hamiltonian constraint (`vR11-3:51,80`). With creation it reads 3H² = κρ_tot.
- P-T sets H² = (κ/3)ρ̂_nc. Both hold only if ρ_v = 0 (a tuning to the final vacuum), i.e. Lemma PT-s class A (`C5_R12-2_report.md:150-156`).
- **Stiffening the projectable lapse** (λ ≠ 1) gives a ghost or a tachyon; λ = 1 gives no kinetic term (RN L3 [ref], `RN_L3_report.md:256-259`).
- **So** the only escape named here is a lapse with a dynamical local part and a fixed spatial zero mode: the Hamiltonian constraint imposed for k ≠ 0 only. On a physically infinite lattice "the spatial mean" is a global object, a range price on `AX:57` (P-r13a). That class is **OPEN**: I did not build its local equations or check its bound regions.

**Lemma G′, the grid-vacuum branch (suggested; it depends on a source/action bridge, `AX:187`).**
- Under H-vac-grid, the w ≥ 0 zero-point (`vR11-3:35-41`) is a perfect fluid at rest in the site frame, with uniform pressure and Planckian inertia (ρ + p)_v ≈ 1.4–2.1 a⁻⁴ per real scalar (`C5_R11-3_report.md:133-141`).
- Creation injects energy isotropically and no momentum. The fluid's Euler equation then makes **the sites geodesic**. The momentum constraint ties any site drift to Planckian momentum density.
- Raychaudhuri for the site congruence then gives c = θ_s < 0 after turnaround in any region whose sites start comoving with matter (H-adi). That is site destruction, which Record permanence forbids (`AX:80`).
- In this branch, **every** local creation law in V3 violates c ≥ 0 at the first turnaround. This is the registration's own EXCLUDED example (`TESTS.md:4638`), but it is conditional on the bridge, so I do not claim it.

**Answer to (c) as registered.** "Is the creation rate zero inside without a clamp?"
- In 𝒱3 the question is pre-empted by Lemma F under H-vac-Λ, and by Lemma G′ under H-vac-grid.
- If an escape class (P-r13a) supplies a regular slicing, Lemma N makes the *physical* size of bound systems GR's, whatever the creation rate inside them. Creation inside only drifts sites outward, at |V| ~ cR ≪ 1. Then c ≥ 0 is the only condition; c = 0 is not needed.
- A per-site P-T rule there still needs memory ≳ t_coll (Lemma VO). It also misses the collapsed mass in the mean (Lemma A).

### 4(d) Phase transition with a specified transition sector

**Sectors (stated).**
- **S1:** a bag model. Latent heat goes into radiation (w = 1/3) at once.
- **S2:** a condensate. Latent heat goes into a pressureless coherent field (w = 0).
- **Release profile:** s(u) = (1 + tanh(u/W))/2. W is the width in ln a: from percolation (W ~ H/β) down to a single site's wall passage (W ~ H × wall thickness / v_w).
- **Fraction:** α = Δ/ρ_r(u_T).
- Local energy is exactly conserved at fixed site volume, so m₁ is exact. The leak enters from m₂ on (`vR12-2:7`).

**Results (checked, `r133_transition.out`; N = Prony order).**

| sector | α | W | ε(u_T), N = 2 / N = 3 | peak \|ε\|, N = 3 | integrated ∫(√(1+ε) − 1)du, N = 3 | ρ̂ ≤ 0 somewhere (clamp needed) |
|---|---|---|---|---|---|---|
| S1 | 0.01 | 0.15 | **+0.0090** / +0.0061 | 6.3e-3 | +3.5e-4 | no |
| S1 | 0.01 | 0.005 | +0.33 / +0.23 | 0.23 | +5.4e-4 | N = 2 yes, N = 3 no |
| S1 | 0.10 | 0.3 | +0.070 / +0.044 | 0.052 | +1.5e-2 | no (N = 3) |
| S1 | 0.10 | 0.005 | −1.73 / −2.29 | 58 | +4.6e-3 | **yes** |
| S1 | 0.50 | 0.05 | −58 / +3.2 | 3.2 | +4.3e-2 | N = 2 yes |
| S2 | 0.10 | 0.3 | +0.066 / +0.037 | 0.045 | +1.2e-2 | no (N = 3) |
| S2 | 0.50 | 0.005 | −1.14 / −1.19 | 20 | +2.1e-3 | **yes** |

- **Reproduction.** S1, α = 0.01, W = 0.15, N = 2 gives ε(u_T) = +0.0090. This matches the referee's 1.009003 (`ref_R12-2/scripts/referee_r122_checks.out:2`).
- **Scaling (checked).** The peak leak grows like α/W. For α/W ≳ 10 the order-2 or order-3 estimator returns ρ̂ ≤ 0 at some u. Then H² ≤ 0 and **a clamp or a pre-filter is required.** A single wall passage (W ~ 1e-16 at the EW scale; inputs RECALLED) is deep in that regime.
- **Pre-filter cure (reading).** Pre-filter the stress with τ such that Hτ ≳ α/few. For the EW step, α = 5.1e-3 (`C5_R12-2_report.md:201`), so Hτ ~ 1e-3 suffices.
- **Transient (checked).** |ε| ≤ 3e-5 by u_T + 10W in every row. The integrated extra creation is O(0.1α) and positive or negative. That changes only t(a) near the transition. ρ(a) relations are fixed by local conservation and the encoder, not by H (reading).
- **Comparators** (RECALLED; the bounds used are stated):
  - ΔN_eff ≲ 0.3 at BBN/CMB, i.e. |δH²/H²| ≲ 0.04 *at T ~ 1 MeV and at recombination*. EW (α ≈ 5e-3) and QCD (α ~ 0.1–0.5, W ~ 0.3, so peak ε ≈ 0.05–0.24 at N = 3) are both over long before BBN. **They pass, as transients.**
  - EDE: f_EDE ≲ 0.07–0.1 near z_c ~ 3500. A *hypothetical* dark-sector transition there with α ≳ 0.1 and W ≲ 0.3 (peak ε ≳ 0.05) would be constrained. The Standard Model has none.
- **Inhomogeneous transitions.** By Lemma N, a spatially varying creation error moves only sites. This removes the worry that bubbles imprint curvature through creation. B-loc (`C5_R12-2_report.md:214-222`) concerns a constraint-form law and does not apply to the F-law (`vR12-2:7`).

### 4(e) Acceleration

- **A true Λ is invisible** (exact, at N = 1 for a matter + Λ universe; `r133_de_encoder.out`). So today's acceleration must come from a w ≠ −1 sector, which is visible through m₁ ∝ 3(1 + w)ρ_DE.
- **Constant w** (checked): w = −0.95 and w = −0.99 are reconstructed exactly at N ≥ 2. That is wCDM, a DESI-allowed fit (comparator).
- **CPL** (checked, N = 1…5):
  - **DESI-type phantom-crossing** w₀ = −0.75, w_a = −0.86: ρ̂/ρ_nc = 1.50, 5.44, 0.65, −0.19, 0.48. **No convergence, and a negative value at N = 4.** The x-measure has a sign change at the phantom crossing, so Prony is not a valid quadrature.
  - **Non-phantom** w₀ = −0.85, w_a = +0.10: 0.49, 0.51, 0.72, 0.83, 0.89. It converges slowly and is still 11% low at N = 5.
- **Reading.** The F-law makes acceleration visible only through w ≠ −1. It reconstructs it accurately only for a finite constant-w mixture.
  - If the DESI w₀w_a preference is real, a finite-N local P-T reading cannot track it (checked for N ≤ 5; not a no-go for other reconstructions).
  - The output is discontinuous in the content: w = −1 + ε counts fully, w = −1 counts zero.
  - The meV scale and the coincidence stay unexplained (S6).

---

## 5. Prices (named, none adopted)

| # | Price | Axiom text touched | What it buys |
|---|---|---|---|
| P-r13a | **A zero-mode lapse.** The lapse's local part is dynamical, its spatial zero mode fixed: the Hamiltonian constraint is imposed for k ≠ 0 only. It replaces V3's unit lapse | Admissibility "one fixed nearest-neighbor admissibility rule" (`AX:57`) as a range limit (a global condition); "Physical sites are the points of the cubic lattice Z³" (`AX:37`), via S1 | Escapes Lemma F (no geodesic preferred slicing) and Lemma T (the homogeneous constraint is still absent). Unbuilt: OPEN |
| P-r13b | **Lagrangian or coarse-grained reading.** The P-T memory is carried by matter elements, not sites, or the stress is read over ≳ 100 Mpc | `AX:57` (range); source/action gate (`AX:187`) | Escapes Lemma A (collapsed mass undercounted, about 8–12% in H, suggested) |
| P-r13c | **Long memory.** Pre-filter time τ ≳ t_coll ~ (2/3)/H at the virial radius | Formation-rate gate (`AX:182-184`); dynamics not supplied (`AX:116-130`) | Separates orbital variation from dilution. The floor is 14–28% at r_vir for filter orders 2–8 |
| P-r13d | **Wall pre-filter or clamp.** Hτ ≳ α/few, or c = max(0, ·) | As P-r13c | Keeps ρ̂ > 0 when bubble walls pass |
| P-r13e | **C-dust amount.** If C is the dark matter, Ω_d h² ≈ 0.12 is an integration constant of a dust-like creation memory, and the slicing needs a caustic completion | "A law privileges no states" (`AX:94`): the datum is a state choice (reading) | Dark matter as a linear-order CDM equivalent (proved, linear) |
| P-r13f | **Simple dark energy.** A finite constant-w mixture with w ≠ −1 | none (observational, refines S6) | Exact visibility under P-T (checked) |
| (carried) | S1–S6, P-T, P52, P53 (`C5_R12-2_report.md:280-286`; `C5_S14_synthesis.md:183-184`) | as recorded | — |

---

## 6. Notes for the referee and the record

**Referee items (FAIL/EXCLUDED-type, bounded).**
1. **Lemma F in 𝒱3 (the EXCLUDED candidate).** Please check:
   - unit lapse ⇒ geodesic, irrotational normals;
   - R_nn > 0 inside bound matter under the V3 equations (homogeneous E^k_k; the C sign);
   - the top-hat point caustic under H-adi;
   - the Δ = 200 entry integration;
   - whether a kink or shock continuation of the slicing could be admissible (listed as an excluded realization).
2. **Lemma T.** V2 + creation + P-T forces ρ_v = 0. Projectable stiffening is excluded by RN L3.
3. **Lemma N.** The sympy identity (S) − (T) = (6/k²)[(M)′ + 2ℋ(M)], and (H)′ + ℋ(H) = (χ/2)h′. Also the claim that the creation law's k ≠ 0 part fixes only site coordinates (H-vac-Λ).
4. **Lemma A.** Suggested only. The Jensen step assumes ρ̂_s ≤ ρ_s on unbound sites, and f_coll is RECALLED.
5. **Lemma G′.** Suggested; conditional on the grid-vacuum bridge.

**Strong-word check.**
- "Exact": Lemma VO (EdS, Δ = 18π²); the encoder mean (stationary age density); the top-hat caustic at t_coll (pressureless, under H-adi).
- "Invisible": a true Λ and any time-constant stress at a site, including bound matter, under per-site P-T.
- "Every collapsing region": for 𝒱3, with R_nn > 0 inside bound matter.
- "EXCLUDED": only 𝒱3, and only as a worker reading pending the referee.
- "GR's growth": linear order, H-vac-Λ.

**What would change the picture.**
- A local construction of P-r13a, a lapse with a fixed zero mode, with its bound-region behaviour computed.
- A proof that kink or shock slicings are admissible lattice times.
- A Lagrangian-memory F-law with ⟨c⟩ = 3H̄ to Buchert accuracy.
- A source/action bridge settling H-vac-Λ against H-vac-grid.

## 7. Files

- Report: `S/R13-3_report.md`.
- Scripts and outputs: `S/scripts/`, namely `r133_linear.py/.out`, `r133_bound.py/.out`, `r133_transition.py/.out` and `r133_de_encoder.py/.out`.
