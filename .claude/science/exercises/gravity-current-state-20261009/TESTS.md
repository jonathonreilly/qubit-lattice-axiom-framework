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

### E1 results (2026-10-09; worker Claude Opus 5.5 xhigh; referee codex sol: INCONCLUSIVE, leaning FAIL)

Full texts: `agents/E1_report.md` and `agents/E1_referee.md`. Scripts: `scripts/E1/` (the referee's in `scripts/E1/referee/`).

**Setting, as pre-registered (a test setting only).**
- A Poisson sprinkling of Minkowski space.
- The Benincasa–Dowker/Sorkin smeared d'Alembertian, with ε = (ℓ/ℓ_k)^d.
- The 2D and 4D coefficients were checked against the literature (referee).
- **This setting conflicts with the axioms.** Records as events break Record's "one record per site; permanent", and A36 says records carry no time, so the causal order is supplied.

**What passed (EXACT; confirmed).**
- **(a) Mean shape-blindness.** A constant determinant-one strain maps the order to the Minkowski order with the same Poisson law, so the whole distribution of every order observable is strain-independent, not just its mean. This is the first substrate in this exercise where both mean conditions come from symmetry.
  - **But per realization the order "crackles".** It is piecewise constant in strain and jumps when pairs cross nullness. The rms response goes like s^0.51 (five points; not a universal exponent). There is no smooth stiffness term.
- **(b) One cone in mean.** B̄(p) = F(p², sgn p⁰), so every species shares the real massless cone.
  - **Referee caveat:** the 4D mean operator also has complex zeros, so "one cone" does not mean "one mode" or "stable". Continuum work reports 4D instability that contour or Wheeler prescriptions can project out (Aslanbeigi–Saravani–Sorkin arXiv:1403.1622; BBL arXiv:1411.6513).

**What grows.**
- **Row noise gain (EXACT, L² statement, referee item 8).** Every nonzero retarded 4D kernel that depends only on the interval volume has infinite white-noise gain in an infinite Minkowski past, because each proper-time slice carries an infinite hyperboloid volume. Alternating signs cannot cancel |K|². A finite cosmic past makes it finite but huge.
- **The coefficient (CHECKED).** For the BD weights, A² → 1.6739·ε(T/ℓ_k)² for a diamond of height T, and 4× that, 6.695, for a slab past of depth T (supervisor S1/S1b). The coefficient converges as ε → 0.
- **Exponential instability (CHECKED at ε = 0.2).** The naive retarded evolution is genuinely exponentially unstable: the referee's 12-realization extension to 10.5ℓ_k fits an exponential at rate 0.645, with log-RSS 0.0095 against 0.145 for a power law.
  - At ε = 0.05 the series is too short to tell.
  - The measured rates 0.41, 0.45 and 0.74 compare with renewal predictions 0.33, 0.47 and 0.67.
- **The renewal model is NOT a theorem.** Overlapping intervals give covariance corrections of 5–24% at ε = 0.2 and 15–66% at ε = 0.1, growing as ε falls. Smooth (correlated) errors are protected by the alternating signs; rough errors see Σw².

**Why the verdict is INCONCLUSIVE, leaning FAIL (fixed reading; TESTS.md:8).**
- The claimed exclusion needs the instability rate ∝ √ε/ℓ_k down to ε ≈ 7e-64. Then ℓ_k³ > 1.585ℓ_P²L gives ℓ_k ≳ 2.3e-15 m for 1 Gpc and 3.8e-15 m for c·t₀, far above the 1e-19 m bar.
- That exponent is extrapolated, not established. Keeping the ε = 0.1 calibration, an exponent of about ε^0.71 would already erase the exclusion.
- The scalar-to-GW and swerve translations are conditional: the tensor rate is asserted, the mapping onto the Philpott–Dowker–Sorkin and Kaloper–Mattingly coefficients is not derived, and the lenient swerve rows assume a preferred-frame cutoff.
- Coarse GW phase noise alone passes, as the supervisor's pre-registered power count said.

**Strongest correct statement (referee, condensed).**
- **Established:** the event substrate is exactly shape-blind in law and has one real massless cone in mean. Its 4D one-step noise gain grows like ε(T/ℓ_k)². The standard (BD) evolution is genuinely exponentially unstable at ε = 0.2.
- **Not established:** that the growth rate stays ∝ √ε/ℓ_k down to ε ~ 1e-64, or that the scalar-noise translations are the right GW and swerve observables. Those steps carry the claimed exclusion, so E1 is **INCONCLUSIVE, leaning FAIL**.

## Follow-up 2 at the owner's request (pre-registered 2026-10-09, before any run)

The owner asked: "test the event dynamics with influence passed along links and in parallel reason backward about what the substrate must be to get everything we need for gravity".

This is a **test setting only.** It has the same axiom conflicts as E1: Lattice is replaced, and the causal order is supplied, because records carry no time (A36) and Record says "one record per site; permanent".

### E1′: influence passed along links on records-as-events

**Setting.**
- A Poisson sprinkling of Minkowski M^{1,3} at density ρ = ℓ⁻⁴.
- Influence passes only along **links**: y ⋖ x means y ≺ x with no event between them.
- **Massless:** G₀ = a·L with a = √ρ/(2π√6), Johnston's path-sum propagator.
- **Massive:** G_m = aL(I − abL)⁻¹ = Σ_{n≥0} a^{n+1}bⁿL^{n+1}, with b = −m²/ρ.
- The normalisations must be verified against Johnston (arXiv:0806.3083, 0909.0944).
- The field from a source is φ = G·J, with J a smooth localized source.
- Control: 1+1, with Johnston's 2D causal-matrix form.
- There is no non-locality scale beyond ℓ.

**Questions.**
- **(a) Mean conditions.**
  - Shape-blindness in law (exact, from E1).
  - The mean of G₀ and G_m against the continuum retarded Green functions.
  - One cone in mean: the support of mean G₀ on the light cone, and its width as ρ → ∞.
- **(b) Massless noise (the graviton proxy).**
  - The per-realization relative fluctuation of (G₀J)(x) as a function of distance D, source size s and duration, and ρ.
  - An exact or controlled asymptotic law, including link–link correlations (shared empty intervals), checked numerically over the accessible range.
  - Does the noise grow with the size of the past beyond the source?
  - Compounding: the noise after k successive re-emissions (a relay medium).
- **(c) Massive noise (matter).** The per-realization relative fluctuation of G_m and G_m·J against mτ, at several ρ. Is there exponential growth, and in which variable (mτ, m²ℓτ, m⁴ℓ²τ²)? An exact or controlled law if possible: for example, chain-count variances from Poisson moment formulas.
- **(d) Translation.**
  - GW proxy over 1 Gpc: phase and amplitude noise, scattering loss, arrival-time spread against GW170817 (|c_g − c|/c ≲ 1e-15).
  - The graviton mass, which is massless in mean.
  - Locality: links are near-null, but every event has unboundedly many past links (BHS). Quantify the count over the cosmic past and say what the locality bar means here.

**Readings (fixed now). Two questions, kept separate.**

*The gravity question:*
- **PASS:** (a) holds, and the per-realization noise of massless link propagation meets the GW bounds over 1 Gpc with ℓ ≤ 1e-19 m (natural ℓ = ℓ_P). This must be established by an exact or controlled asymptotic law verified in the tested range, not by a long extrapolation of a fitted trend.
- **FAIL:** (a) fails, or such a law shows the massless noise violates the GW bounds for every ℓ ≤ 1e-19 m.
- **INCONCLUSIVE:** otherwise.

*The matter question:*
- **M-PASS:** the massive path sum's per-realization relative noise stays bounded (no exponential growth), and an exact or controlled law keeps electron and proton propagation coherent over ≥ 1 km at ℓ = ℓ_P.
- **M-FAIL:** by an exact or controlled law, the noise exceeds the mean, so coherence is lost, below 1 km for the electron or the proton at ℓ = ℓ_P.
- **M-INCONCLUSIVE:** otherwise, including any verdict that would need a long extrapolation.

**Supervisor's expectation (written before launch; suggested).**
- **Gravity: PASS likely.**
  - The massless case has no recursion (b = 0), so nothing compounds.
  - The relative noise should go like (ℓ²D/s³)^{1/2}, about 3e-30 for s = 100 km, D = 1 Gpc, ℓ = ℓ_P.
  - The arrival spread should be about ℓ²/D.
  - Links into empty regions (infinite valency) should not matter for a source-driven field.
- **Matter: M-INCONCLUSIVE or M-FAIL.**
  - b < 0 brings back alternating signs, and the mean must build the Bessel oscillation by cancellation.
  - A renewal-type count gives a gain of about 0.06·m⁴ℓ²D², i.e. coherence loss beyond D* ~ 4/(m²ℓ): about 10 km for the proton, 0.3 AU for the electron, about 1 m at 100 GeV.
  - The renewal model was not a theorem in E1, so this is only a guess.

### B: reasoning backward from gravity's requirements to the substrate

**What it is.** A derivation task, not a test. Start from what gravity must deliver:
- observed bounds;
- the classical uniqueness and no-go theorems: Weinberg's soft theorem, Weinberg–Witten, Deser self-coupling, Fierz–Pauli/vDVZ, Rubakov–Tinyakov/Dubovsky, BHS, Collins et al.;
- this packet's results: Lemma R, Lemma P, E1–E3, T1, T2, and the F1a/F1b/F2 kills;
- the candidate pack's results: K3a″, W1, FR1–FR3, G0c, K7a;
- the 09-28/29 probes and exercise.

Then derive what any substrate must be.

**Agents.** Two independent lenses, both Opus 5.5 xhigh:
- **B1, physics-first:** from experiments and theorems.
- **B2, framework-first:** from the four axioms and what the repo has derived or excluded.

The supervisor writes its own thread before either reports.

**Rules.**
- Every necessity claim lists the theorem's hypotheses and where they could fail (headline scope discipline).
- Owner readings are hypotheses, not rules.
- Axiom changes are named only as prices.
- Every no-go or necessity claim that survives into the summary gets the codex sol referee.

### B results (2026-10-09; B1 and B2 Opus 5.5 xhigh plus supervisor thread; referee codex sol: all three CONFIRMED WITH CORRECTIONS)

See SUMMARY.md §8 and `agents/B_referee.md`.
- **The conditional core survives.** In a local, weakly coupled 3+1 EFT with one massless helicity-2 pole, a Lorentz-invariant S-matrix and no compensator or custodial sector, an exact linearized-diffeomorphism Ward identity forbids an h-only mass. Generic physical labels need protection or extreme tuning. The soft-theorem and bootstrap hypotheses then give universality and GR's structure.
- **Not proved:** that the grain must be event-like, fluid, coherent, or of unbounded valency. BHS is narrower: it excludes only an intrinsic finite-valency Lorentz-equivariant map on a Poisson sprinkling.
- **B1 c5** (4D Euclidean random lattice): bounded FAIL for the tested implementation.

### E1′ results (2026-10-09; worker Claude Opus 5.5 xhigh; referee codex sol: gravity INCONCLUSIVE, matter M-INCONCLUSIVE)

Full texts: `agents/E1p_report.md` and `agents/E1p_referee.md`. Scripts: `scripts/E1p/`.

**Confirmed (referee).**
- Johnston's normalisations are right (a = √ρ/(2π√6), b = −m²/ρ, φ = ρ⁻¹KJ).
- The law is shape-blind.
- E[aL] → the massless retarded light-cone kernel, with O(ℓ²/r²) power corrections and no Yukawa factor.
- E[L²] → 3π, in the limit only.
- The massless field's mean and diagonal variance (Mecke) are exact. It depends on nothing outside the source-to-observer intervals. Its Fano factors are 1–2.5 for s/ℓ = 6–24, with κ = 3.5, 4.4 and 4.9.
- Two-stage relays do not compound.
- Neutron-star merger at 1 Gpc: N̄ = 2.2e57, so the noise is 2.1e-29 *if* F stays O(1).

**Gravity: INCONCLUSIVE.** The worker's PASS is not confirmed, because the uniform large-s/ℓ Fano law was argued, not controlled. Taking κ from s/ℓ ≤ 24 to s/ℓ ~ 1e39 is a long extrapolation (TESTS.md:8). The referee also notes the scalar-to-tensor bridge is not derived. Overturning the result would need κ ~ 7e77, i.e. roughly quadratic growth in s/ℓ.

**Matter: M-INCONCLUSIVE.** The worker's M-FAIL is not confirmed.
- **Established for single events.** Event-to-event kernels have a ρ-independent two-link floor, sd ∝ m², which crosses the mean at mτ ≈ 2.88 in the continuum regime. The leading compact-source seed law is (√6/96)(mℓ)²(mτ)³.
- **The mean has a genuine slow growing complex pole.** Re s = (3/(2√6))m³ℓ² = 0.612 m³ℓ²; the referee derived it independently.
- **Not computed: the physical observable**, a wavepacket travelling a given lab distance into a smeared detector, including regeneration along the trip.
- **The 4D renewal growth rate 0.2549·m²ℓ is only an overlap-free model.**

### E1′-b: a uniform bound on the massless Fano factor (supervisor follow-up; pre-registered 2026-10-09 before its referee)

**Why.** The E1′ referee left gravity INCONCLUSIVE only for want of a controlled large-s/ℓ noise law. This follow-up supplies a bound, not a fit.

**Claim (supervisor; proved modulo routine geometry; see `agents/supervisor_E1p_b.md`).** For a source J = 1 on a region that straddles x's past light cone and is thick compared with the link shell:

  Var(Σ_y J(y)L(x,y)) / N̄ ≤ 3 + c·(s/D), with a finite geometric constant c, **uniformly in s/ℓ**.

**How it is proved.**
- The Poisson Poincaré inequality Var F ≤ E∫(D_zF)²ρdz, applied to the add-one cost D_zF = J(z)L(x,z) − Σ_{y: z∈I(y,x)} J(y)L(x,y).
- The needle overlap |I(y,x) ∩ I(y',x)| ≈ min(V, C·ℓ⁸/b⁴) at transverse offset b. This is CHECKED by Monte Carlo in `scripts/E1p/S2_needle_overlap.py`: overlap·b⁴ → about 23ℓ⁸ for b = 8–32ℓ, and the overlap equals V for b ≪ ℓ.
- The overlap is integrable over the transverse plane, and the source depth gives the factor s/D.

**Readings (fixed now):**
- **CONFIRMED:** the referee confirms the bound, with hypotheses stated. The gravity reading's "controlled law" condition is then met, and **E1′ gravity becomes PASS for the scalar link proxy.** At physical parameters F ≤ 3, so the relative noise is ≤ 3.7e-29 at 1 Gpc.
- **NOT CONFIRMED:** the bound fails, for example a divergent overlap integral or a misapplied inequality. E1′ gravity stays INCONCLUSIVE.
- **Scope, unchanged by this follow-up:** the tensor bridge, E1's strain crackle, and source-driven (not initial-value) propagation. The referee is asked to say whether the tensor bridge is a scope caveat (as in E1's scalar proxy) or a PASS condition under the fixed reading.

### E1′-b result (2026-10-09; referee codex sol: CONFIRMED WITH CORRECTIONS)

**E1′ gravity: PASS for the registered scalar, source-driven proxy** (`agents/E1p_b_referee.md`). The bound Var F ≤ (3 + C′_S·s/D)·N̄ holds uniformly in s/ℓ and ρ for regular sources crossing the cone with cone-normal thickness ≫ ℓ²/D. For a neutron-star merger at 1 Gpc this gives relative noise ≲ 3.7e-29.

**Corrections applied** in `agents/supervisor_E1p_b.md`: the shell average is asymptotic, "thick" means cone-normal thickness, the overlap bound depends on the shell depths, and a dimensional typo is fixed.

**Not established, and outside the scope of this PASS:** the tensor/helicity-2 bridge, nonlinear gravity, E1's strain crackle, and initial-value propagation.

**Matter remains M-INCONCLUSIVE.**
