# Step 8: tests (pre-registered before running)

**Budget.** The default 2 hours; the owner asked for the exercise without a different budget.

**Rules (skill PR #9472):**
- Readings are fixed before the run and never changed after it; a follow-up gets a dated new entry.
- Searches state their class.
- No verdict rests on long extrapolation.
- Every FAIL or no-go gets the other-vendor referee (codex gpt-5.6-sol xhigh) before it is reported.

## T0: the IR-cone cutoff identity (step 3 "shrink"; run 2026-10-09)

- **Script:** `scripts/S0_ir_cone_cutoff_identity.py`, with its output.
- **Result (EXACT):** a fixed label-space window gives a TT second derivative of K₀⁴/(120π²) per bosonic mode and −K₀⁴/(60π²) per Weyl sea, the same for every shear direction. A proper-space window gives 0.
- **Effect on the wall:** none. This is the smallest object in which the wall bites. R3's surface-term lemma generalizes it to any covariant integrand and any window (`agents/R3_price.md`).

## T1: the one-light-cone test for the surviving shape-blind regulators (pre-registered 2026-10-09)

**Why.** Every surviving way to remove the TT stiffness changes the regulator so that it no longer has the hypercubic Z³ × Z_τ symmetry. That symmetry is what K7a and the kinetic-isotropy primitive used to protect one light cone. Without it, loops generically split the speeds of different species at O(g²/16π²), whatever the cutoff scale. That is the Collins–Perez–Sudarsky–Urrutia–Vucetich mechanism (COMPARATOR). Both R1 and R2 propose this test and predict FAIL.

**Method.**
- **Theory.** A Yukawa theory g·ψ̄ψφ: one Dirac or Weyl fermion ψ and one real scalar φ, both massless at tree level, with equal bare speeds.
- **Time.** Continuous. Space is regulated in two ways:
  - **(a) Fixed Z³ with a smooth proper-distance kernel of width σ** (route F2). Run σ = 1, 2, 3 in lattice units, or as far as converged.
  - **(b) A 3D Poisson–Delaunay spatial lattice** (route F1a), with circumcentric (Voronoi-dual) weights. Use the law average plus the per-configuration spread. If (b) cannot be completed within the budget, report it as INCONCLUSIVE and say why.
- **Quantity.** The one-loop renormalized low-momentum speeds, δc_ψ and δc_φ, and their split Δ ≡ (δc_ψ − δc_φ)/(g²/16π²). Tree-level speeds are equalized before the loop.

**Readings (fixed now):**
- **(a)**
  - **PASS:** |Δ| falls by at least 10× from σ = 1 to σ = 3, trending to zero.
  - **FAIL:** |Δ| ≥ 0.1 and σ-independent within 20%.
  - **INCONCLUSIVE:** otherwise.
- **(b)**
  - **PASS:** |⟨Δ⟩| < 0.01, with per-configuration spread < 0.01.
  - **FAIL:** |⟨Δ⟩| ≥ 0.1, or per-configuration spread ≥ 0.1.
  - **INCONCLUSIVE:** otherwise.

**What a FAIL means.** That regulator cannot have both a protected light cone and zero shear stiffness without tuning. This is one corner of R2's regulator trilemma.

### T1 results (2026-10-09; worker Claude Opus 5.5 xhigh; referee: codex sol, CONFIRMED WITH CORRECTIONS)

**Method.**
- Euclidean self-energies, with the q₀ integral done in closed form.
- δc_ψ = B − A and δc_φ = (b − a)/2 from the coefficients of the time-derivative and space-derivative terms.
- A twisted IR mass iγ5·m, with m → 0; an ordinary mass drifts.
- Comparator: Collins et al.'s formula reproduced (16π²δc_φ = 1.3304 vs 4/3, CHECKED).

**Δ ≡ (δc_ψ − δc_φ)/(g²/16π²), at m → 0.**

| σ | (a1) literal R2 kernel | (a2) shape-fixed (Gaussian propagator factor, as in Collins) |
|---|---|---|
| 1 | −8.3 | −0.692 |
| 1.5 | −31.1 | −0.692 |
| 2 | −75.4 | −0.692 |
| 2.5 | −148.6 | — |
| 3 | −258 | −0.697 (L-limited; continuum −0.692) |

**Controls.**
- Nearest-neighbour Z³ with continuous time: Δ = −2.50 ± 0.03.
- **Euclidean hypercubic Z⁴ (time on the lattice): Δ = −2×10⁻⁹**, zero by symmetry.

**Verdicts against the fixed readings.**
- **(a1): INCONCLUSIVE.** |Δ| grows about 31× (roughly ∝ σ³; a flat-band formula matches within 1–15%), so it neither falls (PASS) nor stays flat (FAIL). It is the opposite of a pass.
  - **Reading (worker):** R2's Gaussian kernel leaves most of the Brillouin zone as a flat band, and those cutoff-scale modes renormalize only the fermion's time-derivative term.
  - **The flatness that makes the TT stiffness vanish is what breaks the single light cone.**
  - The reading is not changed after the fact. A growth reading would need a new, dated test.
- **(a2): FAIL.** |Δ| = 0.69 ≥ 0.1, σ-independent to 1e-4.
  - The value depends on shape (r = 0.5 gives +0.62, r = 1 gives −0.69, r = 2 gives −1.55). A tuned r zeroes it for one pair of species only: tuning, not protection (Collins).
  - **Other-vendor referee: confirmed** (see below).
- **(b): INCONCLUSIVE.** Only the tree level was checked: the DEC identities, and tree speed exactly 1 per configuration for the scalar and for Wilson–Dirac. The one-loop run needs supercell Bloch sampling, about a day of compute plus validation. Collins' argument predicts ⟨Δ⟩ = O(1) (ARGUED).

**Scripts:** `scripts/T1/`.

### T1 referee (codex gpt-5.6-sol xhigh): CONFIRMED WITH CORRECTIONS

The verdict is in `scripts/T1/referee/REFEREE_VERDICT.md`, with an independent unexpanded 4D integration in `referee_direct4d.py`.

- **(a2) FAIL is confirmed.** The split is "a finite, cutoff-scale-independent and regulator-shape-dependent O(g²/16π²) fermion–scalar speed split".
  - The independent integration gives a massless value of **Δ ≈ −0.696**, not exactly −0.692: the worker's finite-difference step contaminated its smallest-m rows.
  - The shape dependence is confirmed: Δ = +0.6135, −0.6954, −1.5468 at r = 0.5, 1, 2.
- **(a1) INCONCLUSIVE is confirmed.** The σ³ growth is real for the specified operator, but it is dominated by a flat band that depends on how the fermion was built. It is not a universal Collins coefficient.
- **The controls are confirmed.** Collins' 4/3 is reproduced. The Z⁴ residual of 2e-9 is roundoff, forced to zero by hypercubic symmetry. The nearest-neighbour value of −2.50 is robustly order one.
- **(b) INCONCLUSIVE is confirmed.** The DEC identities give unit speed per configuration as p → 0. No one-loop value was computed.
- **Artifact notes.** `t1a_scan.out` is stale; use `t1a_scan_twisted.out`. The radial decomposition in `t1_diag_mdrift.py` is invalid at large m; the totals are unaffected.
- **Scope (the referee's strongest statement).** "T1 establishes the **sufficiency** of hypercubic time–space symmetry and the failure of the tested (a2) regulator, but it does **not** establish that a time lattice is necessary or that every smooth spatial regulator with continuous time lacks a protected light cone."

## T2: does reflection positivity plus hypercubic symmetry force a TT stiffness floor? (pre-registered 2026-10-09, after the F2 referee)

**Why.** The F2 referee left one keep-the-grid route open: a 4D hypercubic, reflection-positive regulator with smooth or perfect-action kernels. T1 shows that hypercubic time–space symmetry suffices for one light cone, so this route keeps that protection. Lemma N (`agents/kill_F2.md`, corrected by the referee) bounds the zone-face curvature of every reflection-positive kernel along an axis. Whether that implies a floor on the **TT vacuum stiffness** is the open lemma. This is the cheapest decisive test of the route, and of R2's regulator trilemma at the free level.

**Method.**
- **Field.** A free real scalar on Z⁴ (Euclidean, time on the lattice, a_t = a_s).
- **Kernel family.** The general hypercubically symmetric, reflection-positive kernel. Per axis, the inverse propagator is D(cos q_μ), in the Nevanlinna class of Lemma N; for example, sums over μ of single-pole or several-pole forms, or the known perfect-action (fixed-point) free kernel.
- **Coupling to the metric.** Through proper distance, as in R2 Route 3, applied to every axis treated alike. Say exactly how.
- **Stiffness.** The TT vacuum stiffness is the second derivative of −½ log det under a constant volume-preserving spatial shear. Compute it in both TT channels.
- **The question.** Minimise the stiffness over the family at fixed kernel range (a "width" parameter), and report how the minimum scales with the width.
- **Check.** Reflection positivity, both per axis (the Hankel test) and for the full kernel.

**Readings (fixed now).**
- **PASS (the route lives):** some reflection-positive hypercubic kernel family has a TT stiffness that falls faster than any power of the width (for example exponentially), or reaches ≤ 1e-10 at a width of ≤ 10 lattice units, with no tuning of the TT channels.
- **FAIL:** every reflection-positive hypercubic family tested has a stiffness ≥ c·width^(−p), a power-law floor. Report p and c, and say which family attains the floor.
- **INCONCLUSIVE:** otherwise.

### T2 results (2026-10-09; worker Claude Opus 5.5 xhigh; referee: codex sol, CONFIRMED WITH CORRECTIONS)

**Verdict against the fixed readings: FAIL, bounded to the families searched.** Every reflection-positive hypercubic family coupled through proper distance has |κ| ≥ c·σ_N^(−p).

| Family (coupling) | κ_E / κ_T at σ_N ≈ 10 | Decay |
|---|---|---|
| A: F(S_G), complete Bernstein F, metric-coupled nearest-neighbour Laplacian | 4.3e-4 / 6.5e-4 | p = 2 (c = 2\|W''\|, Watson integral, matched to 0.5%) |
| B: proper-distance weights J(\|G^{1/2}n\|), positive sums of 4D propagators | 1.0e-3 / −2.4e-4 | p = 2 |
| C: Bietenholz–Wiese perfect action, blocked over label cells | 1.1e-4 / 1.2e-4 | p → 2 |
| C′: perfect action blocked over a fixed **physical** hypercube | 1.5e-6 / −1.7e-7 | **p = 4** (the σ⁻² term is exactly 0 by unfolding) |
| D: per-axis sums with a frame coupling | −3.4e-3 / 0.16 | no decay |

- **The minimiser** at fixed width is a single pole or mass in every family (log-convexity, ARGUED).
- **Reflection positivity:** A, B and D pass the site, link and Hausdorff Hankel tests everywhere. C and C′ are link-RP exactly; their site-RP fails for s² ≤ 1/3.
- **Best case:** about 1.5e-6 at width 10. Reaching about 1e-102 with p = 4 would need widths of about 1e25 sites (supervisor arithmetic).

**The open lemma ("face floor ⇒ TT stiffness floor") is disproved as stated (EXACT + CHECKED).** A momentum-space relabelling coupling, D₁(q₀, Φ_ε(k)) with Φ_ε a volume-preserving flow, has these properties:
- **κ ≡ 0;**
- it keeps time-RP;
- it is IR-covariant;
- its couplings decay exponentially.

That is R4's free-level escape. Lemma R excludes it for interacting laws, because Φ_ε is not additive, so it cannot act consistently at vertices. **So the floor comes from the coupling rule, not from RP plus hypercubic symmetry.** With interactions, every admissible coupling tested gives a power-law floor.

**Scripts:** `scripts/T2/`.

### T2 referee (codex gpt-5.6-sol xhigh): CONFIRMED WITH CORRECTIONS

The verdict is in `scripts/T2/referee/REFEREE_VERDICT.md`.

- **The bounded FAIL survives.**
- **The relabelling coupling is outside T2's proper-distance contract.** If it were admitted, it would be an exact free-level PASS. Under the registered contract it is out of scope.
- **The stiffness calculations are substantially correct.** A and B robustly give p = 2. C trends to p = 2. C′'s σ⁻² term is exactly eliminated, with about σ⁻⁴ as numerical evidence.
- **Major RP correction: C and C′ do not have a positive one-step transfer matrix at any finite s².** The alias weights decay polynomially while cosh E grows, so the Hausdorff mass diverges. Their finite Hankel passes are false assurance, and they have only link-RP. **So C′'s σ⁻⁴ is not in the RP class.**
- **The best RP-confirmed performer** is family A's single pole: max|κ| ≈ 0.0647·σ_N⁻², i.e. 6.45e-4 at σ_N = 10.
- **The minimiser claims are narrowed.** Only A's large-width leading coefficient is proved minimal for a single effective pole.
- **Lemma R is narrowed.** It excludes ordinary local, additively momentum-conserving interacting extensions, not every conceivable interacting law.
- **Strongest statement:** "On the fixed Z⁴ grid, every tested proper-distance or minimal-metric family that also has the required positive one-step transfer property (A, B and D) misses the PASS bar and retains a power-law or non-decaying TT response … This is a bounded experimental FAIL, not a theorem that RP plus hypercubic symmetry forces such a floor."

## Follow-up tests at the owner's request (pre-registered 2026-10-09)

The owner asked: "test the spacetime-event substrate with records as events, and test what happens if we give up the fixed repeating pattern. maybe the grid does not have all sites present? or there is no fixed pattern? or??"

These are **test settings only.** The Lattice axiom is not changed by running them.

**What every substrate must meet:**
- **(A) No TT stiffness on average:** the shape-blind mean.
- **(B) No TT stiffness noise at long wavelength in each realization:** S(0) = 0, or noise suppressed enough. F1a died here.
- **(C) One protected light cone:** T1 found hypercubic time–space symmetry sufficient. A preferred frame splits speeds (Collins).
- **(D) Locality enough to fit current tests.**

**Supervisor power count (suggested, to be checked by E1).**
- **Static (frozen-in-space) white disorder** in a random mass² is *relevant* in 3D: its strength relative to k² grows like (λ/a)^½. This is F1a's failure.
- **Spacetime white disorder** (events scattered in 3+1) is *marginal*: the ratio is constant in λ.
- **So** records-as-events could escape F1a's failure if the per-event noise σ is small, or is smeared over a modest scale ℓ.
- **Known literature (COMPARATOR):** causal sets predict a fluctuating cosmological constant of the observed order ("everpresent Λ", Sorkin). They also need a non-locality scale to tame the fluctuations of the discrete d'Alembertian (Sorkin 2007; Benincasa–Dowker).

### E1: records as spacetime events (a causal-set-like substrate)

**Setting.**
- The substrate is the set of record-formation events, a Poisson process in Minkowski spacetime (Lorentz-invariant in law).
- Fields live on events, and their dynamics uses only the events' causal order. Take the Benincasa–Dowker discrete d'Alembertian in a local form and in a form smeared at non-locality scale ℓ.
- Work in 1+1 and in 3+1 sprinklings.

**Questions.**
- **(a)** Is the mean response of the vacuum (or of the discrete d'Alembertian's action) to a constant volume-preserving deformation zero? Expected: yes, exactly, by invariance of the law.
- **(b)** Is the mean low-energy propagation the same for two species, i.e. one cone in mean?
- **(c) The decisive question: per-realization noise.**
  - How does the fluctuation of the effective mass² felt by a long-wavelength mode, and of the TT response, scale with the averaging size λ and with ℓ?
  - Compare with F1a's static case.
  - Translate the result into: (i) gravitational-wave propagation over 1 Gpc without significant scattering or phase noise, together with the graviton-mass bound; (ii) observational bounds on "swerves", the Lorentz-invariant momentum diffusion of Dowker–Henson–Sorkin.
- **(d)** What ℓ is required, and is it below the scales where locality is tested?
  - Use about 1e-19 m (the LHC) as the locality bar.
  - State any Lorentz-violation bounds used.

**Readings (fixed now):**
- **PASS:** some ℓ (or none needed) satisfies the gravitational-wave and graviton-mass bounds *and* the swerve bounds, with ℓ ≤ 1e-19 m. Mean shape-blindness and one mean cone must also hold.
- **FAIL:** no ℓ satisfies both the noise bounds and the locality bar, or the mean conditions fail.
- **INCONCLUSIVE:** otherwise, for example if a needed scaling exponent cannot be established.

### E2: a grid with not all sites present (dilution)

**Setting.**
- Z³, with each site present independently with probability p.
- Fields live on the present sites. Run two couplings: (i) nearest-neighbour among present sites; (ii) proper-distance couplings (as in R2/R3).
- Variants: (a) frozen dilution; (b) growing dilution, where sites appear over time as records form and never disappear.

**Compute.** The mean TT stiffness (both channels) against p, and the per-realization noise S(0), for a free scalar (and a fermion sea, if cheap).

**Readings:**
- **PASS:** at some p, the mean TT stiffness vanishes in both channels without tuning, and S(0) = 0.
- **FAIL:** the mean stays nonzero for every p, since the law keeps only Z³'s finite symmetry, or S(0) > 0.
- **INCONCLUSIVE:** otherwise.

### E3: other "no fixed pattern" substrates

**Setting.** Three substrates:
- aperiodic order: a quasicrystal (a 3D icosahedral or Penrose-type construction, or a 2D analogue if 3D is too costly);
- a hyperuniform disordered set (for example "stealthy");
- a Poisson set that keeps growing (sites appear and are never removed).

**Compute.** The mean TT stiffness and the per-realization noise, as in E2.

**Readings:**
- **PASS:** zero mean TT stiffness and S(0) = 0 at long wavelength, without tuning.
- **FAIL:** otherwise, with the reason stated.

### E2 and E3 results (2026-10-09; worker Claude Opus 5.5 xhigh; referee codex sol: CONFIRMED WITH CORRECTIONS for both)

Full texts: `agents/E23_report.md` and `agents/E23_referee.md`. Scripts: `scripts/E23/`.

**Field and quantity.**
- A free scalar on the present points, with metric g = e^{th}, h traceless.
- E″ per present site, in the channels E_g and T_2g.
- Couplings: nn (unit Z³ bonds among present sites, weight 1/d_g²) and pd (R3's kernel, R = 1.8).
- Bosons at m² = 1 and 0.04, plus a secondary smeared fermion sea.
- Noise: sd·√N per direction against box size.
- Validation reproduced by the referee: crystal pd 0.0473827 / 0.0140046; exact small-p slopes.

**E2, diluted Z³ (frozen and growing): FAIL (bounded).**
- **Mean:** nonzero in both channels at every p searched, p ∈ {1, .9, .7, .5, .3116, .3, .2, .1}.
  - **Referee strengthening (analytic):** the nn T_2g mean is strictly negative for **every** p > 0, not just the sampled ones.
  - The light pd boson crosses zero in E_g only, at a p that depends on the mass, while T_2g stays positive.
- **Noise:** sd·√N is flat, so the noise is white, for every p < 1.
  - The 24 extended fits lie at −0.60 to −0.38 against −0.5.
  - **Referee correction:** those fits cover only p = 0.1, 0.3116 and 0.5. Some three-box fits at other p (for example nn at p = 0.9) are finite-size inconclusive, but none points to suppression.
  - **Referee correction:** the fixed-N periodic-box estimator is not a rigorous lower bound on S(k → 0). The N^(−½) scaling is strong evidence of extensive fluctuations, not a proof.
- **Growing dilution:** Theorem A (landed) gives Bernoulli(p(t)) at each time. The stage means equal the frozen ones. The instantaneous-vacuum reading is a fair equilibrium setting; it does not test state preparation or any dynamical cancellation.

**E3: FAIL for all three substrates.**
- **(a) Icosahedral cut-and-project set, spherical window, density 1 (construction checked).**
  - The mean is isotropic, exactly so for the hull mean, and it is not zero without choosing the coupling range.
    - Full functional: −0.0002 ± 0.0001 at R = 1.8; +0.0454 at R = 2.2.
    - Pair level, confirmed by the referee's independent covariogram calculation: −0.067 (R 1.2), +0.003 (1.8), +0.198 (2.2), −0.092 (3.0).
  - **Referee correction:**
    - the quoted errors are phason-patch scatter, not controlled thermodynamic errors;
    - "R = 1.8 is the crossing" is too precise;
    - **full-functional S(0) = 0 is NOT established**: the 35× suppression is for the pair functional only;
    - the polyhedral (Ammann–Kramer) window is untested.
- **(b) Stealthy hyperuniform (χ = 0.30) and perturbed Z³.**
  - The mean is +0.024 (real; robust through L = 12).
  - The stiffness noise is white (q = −0.41 ± 0.08 and −0.50 ± 0.08) even though the density is hyperuniform.
  - Perturbed Z³ at s ≥ 1.2 is unresolved, which does not affect the verdict.
- **(c) Growing Poisson.** The mean is 0, as Lemma A predicts, and the noise is white at every stage.

**Lemma P (supervisor; `agents/supervisor_thread.md`): CONFIRMED WITH CORRECTIONS.**
- **Corrected statement.** A stationary simple point process in R^d (d ≥ 2) with finite local second moments and an SL(d)- or AN-invariant law has reduced second moment measure ρc·dx with c ≥ 1, so Var N(W) = ρ|W| + ρ²(c − 1)|W|².
  - c = 1 holds iff density averages converge in L². Translation ergodicity is sufficient but not necessary; a Haar-random unimodular lattice has c = 1.
  - When c > 1, the spectrum is white at k ≠ 0 plus a zero-frequency atom.
- **AN proof gap closed by the referee.** A contraction argument kills singular mass on x_d = 0, and pair exchange (not parity) equates the two half-space constants. "Smallest group" is not justified.
- **What survives:** the narrow corollary, that SL- or AN-law protection of the mean and an ensemble-hyperuniform density exclude each other.
- **What is withdrawn as too strong:** "density noise ⇒ stiffness noise", and "no symmetry protection ⇒ nonzero response".

**Strongest correct statement (referee).** In every tested free-field construction, giving up the repeating pattern, or leaving some sites absent, is not enough:
- iid dilution keeps a cubic shear response and extensive disorder fluctuations;
- icosahedral order makes the five TT directions equal but does not make them zero;
- a hyperuniform density does not make a nonlinear stiffness functional hyperuniform;
- Poisson law symmetry protects only the ensemble mean.

A frozen spatial law whose shape-blind mean is protected only by SL(d) or AN symmetry cannot also have hyperuniform ensemble density. **This is not a theorem that every frozen substrate fails, or that sites must move.** Still open: an exact realization-wise coboundary or conservation identity, another structural cancellation, a quenched or non-ergodic mechanism, or a spacetime construction (E1). The defensible instruction is to give up *ensemble-symmetry-only protection on a frozen spatial substrate*.
