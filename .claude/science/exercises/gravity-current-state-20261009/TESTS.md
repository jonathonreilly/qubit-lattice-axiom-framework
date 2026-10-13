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

## Campaign C3 (owner, 2026-10-10 00:47Z, 3 hours): pre-registered before any run

**Owner.**
- "test the graviton on links and in parallel test matter coherence. Run a 3 hour campaign, use multiple opus 5.5 sub agents on ultra all out on all the remaining options - exercise when we hit walls, keep iterating and working towards closing all lanes. make PRs as needed."
- Then: "run all 4 next options in parallel, spin up more opus 55 ultra workers on any lane or task that furthers our push here".

**Rules.**
- Workers are Opus 5.5 at max effort.
- Any FAIL or no-go gets the codex sol referee before it is recorded.
- A lane that hits a refereed wall gets a compressed exercise: wall, routes, kills, a new pre-registered test.
- Every setting is a test setting only. The axiom conflicts of E1/E1′ apply to the event lanes.

### Lane G: the graviton on links

**G-A: the order itself as the graviton.**
- **Setting.**
  - Sprinkle once in coordinates.
  - Recompute the causal order and links under g = η + ε·e(k)cos(k·x), where e is TT polarisation.
  - Evaluate order-only functionals: link counts, and the 4D BD action, local and smeared.
- **Measure:**
  - the mean ΔS(ε,k), which should be quadratic in ε;
  - its k → 0 limit, the mass term;
  - its helicity structure (TT against pure-gauge and trace perturbations);
  - the per-realization response: analytic in ε, or E1's crackle (sd ∝ |ε|^½).
- **PASS:** by an exact or controlled law, the mean has no mass term, pure gauge gives zero, the TT kinetic term goes like k², and the per-realization response is analytic, or its noise is subdominant to the mean quadratic action for LIGO-amplitude waves (h ~ 1e-21) over a wavelength cell at Planck density.
- **FAIL:** a mean mass term, or a controlled law showing crackle noise dominating the quadratic action at physical h.
- **INCONCLUSIVE:** otherwise.

**G-B: a tensor field propagated along links.**
- **Setting.** h_μν(x) = ρ⁻¹Σ_y G₀(x,y)·T_μν(y), from a conserved quadrupole source, with G₀ = aL.
- **Measure:**
  - per realization, the non-TT admixture (helicity 0 and ±1) relative to TT;
  - the violation of the harmonic-gauge condition at distance D.
- **PASS:** by a controlled law, the admixture at 1 Gpc stays below 1e-3 of the TT amplitude (conservative against polarisation tests), and the mean is exactly the linearized-GR retarded solution.
- **FAIL:** a controlled law showing the admixture above that.
- **INCONCLUSIVE:** otherwise.
- **Scope.** This tests a linearized graviton carried on links, not its protection.

**G-C: protection.**
- **Question.** Does any order-only or link-only dynamics carry an exact per-realization identity (diffeomorphism-type, coboundary or conservation) that forbids a TT mass in each realization? Or does a quantum sum over orders supply it?
- **PASS:** an identity or mechanism exhibited with proof.
- **FAIL:** a no-go proved under stated hypotheses (sent to the referee).
- **INCONCLUSIVE:** otherwise.

### Lane M: matter coherence

**M-A: Johnston's massive path sum, packet plus detector.**
- **Measure.** Var/mean² of the amplitude received by a smeared detector of size σ_d, from a Gaussian packet of width σ and lab momentum p sent from a source, after lab distance L. Include regeneration along the trip.
- **Method.** An exact or controlled law (Mecke, Poincaré, resolvent bounds), checked by simulation. Evaluate the electron and the proton at laboratory momenta.
- **Readings (the E1′ M-readings, fixed):**
  - **M-PASS:** a controlled law gives Var/mean² < 0.1 at L ≥ 1 km for both particles;
  - **M-FAIL:** a controlled law gives ≥ 1 below 1 km for either;
  - **M-INCONCLUSIVE:** otherwise.

**M-B: unitary matter on links.**
- **Setting.** A norm-preserving matter rule along links: Feynman-checkerboard or chiral hopping with a mass-flip amplitude ∝ i·m·ℓ, or any unitary link walk.
- **Questions.**
  - Is it definable on a Poisson sprinkling, with unbounded valency and no frame?
  - Its mean dispersion: massive, with one cone.
  - Per-realization coherence over 1 km.
- **PASS:** a definable, Lorentz-invariant-in-law, norm-preserving rule with a massive one-cone mean, and packets coherent over 1 km by a controlled law.
- **FAIL:** a no-go under stated hypotheses (referee).
- **INCONCLUSIVE:** otherwise.

### Lane K: the cost of keeping the grid (B1 Test 2, with the referee's corrections)

**Setting.** K7a's staggered h on Z⁴, coupled to lattice QED through the best available stress (K3a's optimized range-R stress).

**Compute.** The O(e²) induced quadratic action at O(q²), decomposed into the W(B4) two-derivative forms.

**Readings:**
- **PASS:** the 5 non-gauge-invariant forms vanish by an exact identity, or go systematically to 0 under size and precision improvement. Keeping the grid then costs only the two shear tunings.
- **FAIL:** any of them converged at ≥ 1e-4 relative to the gauge-invariant form. Keeping the grid then also costs a graviton-speed tuning.
- **INCONCLUSIVE:** otherwise.

### Lane P: the price note

Not a test. A written, plain-first note assembling the refereed results into one owner-level statement of what massless gravity costs on each substrate. It is drafted by a worker, checked against the packet's referee verdicts, and refereed before any PR to main.

### Lane X: extensions (the referee's ranked tests 3–5)

**X1: random-lattice extension.** Direct nonzero-k spectra, a second kernel, and a fermion sea.
- **PASS:** S_TT(k → 0) → 0, or ≤ 5e-11.
- **FAIL:** flat and ≥ 1e-3 in the direct k-spectra, for both kernels and for the fermion.
- **INCONCLUSIVE:** otherwise.

**X2: response of a classical record gas.** S(ω) and G_T(ω) separately, using FDT only after checking that its conditions hold.
- **PASS:** some model has Re G_T(0) = 0, with S and Im G_T both vanishing as ω^n, n ≥ 3, untuned.
- **FAIL:** every model tested has Re G_T(0) ≠ 0 or n ≤ 1.
- **INCONCLUSIVE:** otherwise.

### Campaign C3, added lanes (pre-registered 2026-10-10 ~01:05Z, before any run)

**Lane F: can records forming produce the event set themselves?**
- **Setting.** A label-free growth rule: each new event's relations are decided from the existing order only, with no coordinates and no supplied causal order. Examples are sequential-growth or record-formation rules.
- **Measure:**
  - interval abundances;
  - the Myrheim–Meyer dimension;
  - link statistics against a 4D Poisson sprinkling.
- **PASS:** a rule whose orders match 4D Poisson-sprinkling statistics within controlled error at accessible sizes, with an exact or controlled argument for large N.
- **FAIL:** a no-go under stated hypotheses (referee). For example, Markovian label-invariant growth gives non-manifold orders.
- **INCONCLUSIVE:** otherwise.

**Lane D: spin-½ matter on links.**
- **Setting.** An order-only or link-only spin-½ propagator.
- **Measure:**
  - its mean against the massless (then massive) Dirac retarded propagator: one cone, chirality;
  - a controlled per-realization noise law;
  - whether G0c's one-qubit-per-site fermions have an analogue on events.
- **PASS:** a construction with the correct mean and a controlled noise law meeting the E1′ coherence bars.
- **FAIL:** a no-go, e.g. no spinor structure from order alone without a frame (referee).
- **INCONCLUSIVE:** otherwise.

**C3 end time (owner, 2026-10-10 00:54Z):** "End the work exactly at midnight eastern please". The campaign therefore stops at **04:00Z** (00:00 EDT). Any lane not finished by then is recorded as "not completed (stopped at midnight)".

### C3 progress log (01:52Z)

**Lanes returned**, all pending the codex sol referee:
- **F (formation):** the worker says FAIL, a bounded no-go; the adversarial check supports it, with a narrower scope.
- **D (fermions):** the worker says FAIL; the check says not supported, so INCONCLUSIVE. Exact no-gos within their scope: no spinor kernel from order alone, order is parity-even, and no frame has an invariant law.
- **M-A:** the worker says M-PASS on its grid; the check says M-INCONCLUSIVE because of a missing overlap factor.
- **M-B:** the worker and the check both say INCONCLUSIVE.
- **M-C:** the worker says FAIL. The core is confirmed: no all-positive rule has the massive mean.

Reports: `agents/C3_*_report.md`.

**Exercises started on two walls.** They are conditional on the referees, and moot if a wall is overturned:
- formation (`F_formation`);
- massive matter (`M_massive_matter`).

Each exercise uses the compressed form: 3 lenses, a kill round, and a next test pre-registered by its worker.

- **M-C referee (codex sol):** CONFIRMED WITH CORRECTIONS. The formal FAIL survives. Exact: no all-nonnegative linear source-to-readout rule has the exact massive retarded KG kernel as its mean, in any dimension (zero-mode proof sin(mt)/m). Lemma D holds only for Fourier-mode descent. The block-122 analogy is scoped. Not excluded: positive massive transport with an added carrier, and nonlinear observables. See `agents/C3_M-C_referee.md`.

- **M-B referee (codex sol):** CONFIRMED WITH CORRECTIONS. The lane is INCONCLUSIVE. Theorem A: no jointly Poincare-equivariant isometry with finite event fibers can move amplitude between events. Theorem B: the sprinkling cannot select an antichain. Neither excludes supplied-slice dynamics or link (arc) states. The swerve result holds only for the greedy chain, typically about 9.75 Planck times. An arc unitary, a massive mean and 1 km coherence are all open. See `agents/C3_M-B_referee.md`.

- **D referee (codex sol):** NOT CONFIRMED. The lane is INCONCLUSIVE. Exact narrow no-gos: order alone gives no per-event spinor or frame mark, no handedness, and no gamma.Delta mean of a fixed-fiber kernel. But scalar link propagation plus apparatus differentiation, and the order-only Kahler-Dirac cochain dG, reproduce the massless Dirac response in mean. Chiral matter needs an orientation and spin-transport primitive, as a price. See `agents/C3_D_referee.md`.

- **F referee (codex sol):** CONFIRMED WITH CORRECTIONS. This is a bounded FAIL, not a universal no-go. Three classes cannot reproduce 4D sprinkling: exchangeable generating-subset growth (link means), frontier-only growth (L <= N-1), and every classical DGC+Bell dynamics including VR towers (asymptotically, since 2+2 and 3+1 densities vanish). A surviving rule must use the order non-exchangeably, or leave the Markovian, classical or Bell-causal scope. See `agents/C3_F_referee.md`.

- **M-A referee (codex sol):** CONFIRMED WITH CORRECTIONS. The worker's M-PASS is not confirmed; the reading is M-INCONCLUSIVE. Exact: the add-one identity, the chaos and Poincare bounds, and the shared-link renewal exponent 0.2549 m^2 l. Not established: the full variance exponent (E2, cross-terms, end factors). Within the unproved closure the 1 MeV/c proton margin fails, and if the chain law were applied to a composite's centre of mass (a mapping not derived) there would be conditional tension with qBounce neutrons (42.5 ms) and Rb-87 interferometry (2.3 s to 70 s). See `agents/C3_M-A_referee.md`.

### C3 lane M-D: composite centre-of-mass coherence on links (pre-registered 2026-10-10 01:58Z, before any run)

**Why.** The M-A referee notes the following conditional result. If Johnston's chain law were applied to a composite's centre of mass using its total mass, it would conflict with:
- qBounce: ultracold-neutron states kept coherent for 42.5 ms;
- Rb-87 atom interferometry: 2.3 s, and spatial coherence for up to 70 s.

But that mapping has not been derived.

**Setting.** A bound state of N light constituents (a toy: two or three massive Johnston scalars bound by a short-range attraction carried along links, or the most tractable equivalent), on the E1′ substrate.

**Question.** Does the per-realization noise of the centre-of-mass amplitude scale with:
- (a) the total mass M, as an elementary Johnston scalar of mass M would;
- (b) the constituent masses;
- (c) something else?

**Deliverables.** Derive the scaling by an exact or controlled argument, check it in a toy, then evaluate at ℓ = ℓ_P.

**Readings (fixed now):**
- **PASS:** a controlled law gives coherence times longer than 70 s for an Rb-87-like composite and longer than 42.5 ms for a neutron-like composite, at ℓ = ℓ_P.
- **FAIL:** a controlled law gives decoherence below either observed time. The event substrate with Johnston matter is then excluded by experiment.
- **INCONCLUSIVE:** otherwise.

**Interferometric visibility depends on the covariance between the two arms. The worker must use that observable,** not the variance of a single amplitude.

- **G-A referee (codex sol):** FAIL, narrowly scoped to the fixed-coordinate coupling (picture I) and ensemble-RMS noise. The second-chaos bound and the Rosen causal order check out. The local BD action alone triggers FAIL, so the imported 1e-19 m bar is not needed. See `agents/C3_G-A_referee.md`.

- **G-B referee (codex sol):** INCONCLUSIVE. The admixture conjunct is controlled: A_rms = 7.27e-28 at 1 Gpc, far below 1e-3, as an asymptotic ceiling. The PASS clause 'mean exactly the linearized-GR retarded solution' fails only at finite density (the mean is K_rho*T, which equals G_R*T only as density goes to infinity). FAIL is inapplicable. See `agents/C3_G-B_referee.md`.

- **G-C referee (codex sol):** INCONCLUSIVE. The narrow no-go is confirmed only for frozen picture-I, fixed-point, point-marked order functionals with uniform per-realization invariance and an EH ensemble mean. It does not cover independent link fields, picture II, other couplings or a background-free quantum sum. The law-level Ward identity is exact but does not establish the physical quantum-sum branch. See `agents/C3_G-C_referee.md`.

- **M-D (composite coherence): INCONCLUSIVE** (worker; the adversarial check supports it with corrections). No codex referee is needed for a non-FAIL; see `agents/C3_M-D_report.md`.
  - In the pure shared-link sector, the exponentially growing noise is per constituent: rate k0·m_i·m_j·ℓ per pair channel, never k0·M²·ℓ. The total-mass mapping that drove the M-A tension is therefore not what the substrate gives (EXACT within that sector; ARGUED beyond it).
  - Conditional on the uncontrolled M-A chain law, the outcome depends on what carries Johnston mass vertices:
    - nucleons or 313 MeV constituent quarks: Rb-87 decoheres in about 10–90 ms, against the observed 2.3 s and 70 s;
    - current quarks and electrons with massless binding: about 440 s, which passes.
  - Equivalently, the 70 s experiment would require every Johnston mass-vertex scale in an atom to be below about 12 MeV.
  - **Checker corrections.**
    - The 1+1 toy exceeds the composite law by a factor that grows with time (1.1–1.6), so channel additivity is not checked.
    - The 1+1 visibility check is circular by construction.
    - Cross-species non-growth is ARGUED for 4D, not CHECKED.

- **Exercise on the formation wall (F_formation): all 9 routes killed** (same family; `agents/C3_exercise_F_formation.md`).
  - **Herm(2)/Löwner order.** It needs one global identification of every record's algebra: boosts do not preserve the Jordan product, and 40–42% of relations are lost under per-record automorphisms. That amounts to a supplied flat arena.
  - **Local bulk-nucleation rules cluster.** Fano64 is 6.6 → 34.6 from N = 500 to 2000.
  - **Real-weight action sums:** an entropy bound, and the action changes sign across d = 4.
  - **Lorentzian sums:** no coupling window.
  - **BD-tilted growth:** kill reading met in 74/75 settings.
  - **Next test (pre-registered by the worker, run).** The only known rule that reproduces 4D statistics (Lemma G: the sprinkling read in random birth order) is TELEOLOGICAL. Its early stages are less ordered than small diamonds (10–19 SE), so it needs the final size in advance.
  - **The price, stated (reading, not refereed):** either a supplied event set, or a whole-region formation law that knows its final size. Admissibility's nearest-neighbour locality is given up for formation.

- **Exercise on the graviton wall (G_graviton_on_events): all 9 routes killed** (same family; `agents/C3_exercise_G_graviton.md`).
  - **Route 1 (misframing).** G-A's FAIL ratio holds even with no wave present: it measures the sampling noise of the flat BD action (proved corollary, checked). The route is blocked-equivalent, because masslessness then needs a covariant growth law with Einstein histories (lane F's wall).
  - **Route 2 (an unrecorded, coherent sum over orders).** Dead under the exact interval volume. The variance functional's TT response tends to I0(h)^{1/2}−1, does not depend on ω, and grows like L².
  - **Route 3 (spin-ice / Cayley–Menger).** Blocked-equivalent to K3a/F6, with a per-realization Hessian and tadpole.
  - **N1 (worker test, pre-registered, run).** The exact needle volume in the Rosen wave tends to ρ·I0(h). Both "kill collapses" and "kill as computed" are excluded; the corrected coefficient is about 2× smaller.
  - **The price, stated (suggested, not refereed).** A massless, smooth graviton on events needs:
    - a covariant growth law with Einstein histories (lane F);
    - amplitudes not weighted by e^{iS} of interval-count actions;
    - link-only readouts that reproduce Van Vleck focusing on curved backgrounds (open).

### C3 lane G-L: link-only lensing (pre-registered 2026-10-10 02:46Z, before any run)

**Why.** The graviton exercise's open check. A one-hop link-sum mean through a curved background scales near the cone as ν^{−1/2}·Δ⁻¹, against GR's Δ^{−1/2}, where Δ is the Van Vleck determinant. With O(1) lensing this could be an O(1) mismatch.

**Setting.** A Poisson sprinkling of a curved background: a thin lens, or a weak-field Schwarzschild or focusing plane-wave region. Massless link propagation G₀ = aL, on the true causal order of that metric.

**Measure.** The mean link-sum amplitude (magnification) behind the lens, against GR's Van Vleck magnification √Δ, as ρ → ∞.

**Readings (fixed now):**
- **PASS:** by an exact or controlled argument checked numerically, the link mean reproduces GR's √Δ magnification to O(ℓ²/r²) for O(1) focusing.
- **FAIL:** a controlled law shows a density-independent O(1) mismatch, e.g. Δ⁻¹ against Δ^{−1/2}, so link-only readout mis-lenses.
- **INCONCLUSIVE:** otherwise.

- **Exercise on the massive-matter wall (M_massive_matter): all 9 routes killed as written** (same family; `agents/C3_exercise_M_massive_matter.md`).
  - **Dead:** positive smeared hops (a growing mode in the mean, e^(1.7e4) for Rb at 2.3 s), SJ/Wightman readout, and extinction scoring.
  - **Wounded:**
    - compositeness with soft binding. Single-event binding misses Rb at 2.3 s by 15–25×; it passes only with ≥ 15–81 soft re-emitters per nucleon;
    - a coherent quantum substrate (the textbook kinematic lemma, but the substrate dynamics is open research).
  - **Lemma L (proved, same family, unrefereed).** For hop weights that depend only on the two events, the variance is exactly a sum of positive ladders with rung ρb²·G_m². So the variance always grows exponentially, at rate κ_F.
  - **Pre-registered test S0** (signed hop, first moment zero, smeared at ℓ_k): **FAIL.** The 25 kDa molecule bar has an empty ℓ_k window (the molecule treated as an elementary scalar).
  - **Post hoc, not pre-registered, a lead only:** profiles whose first two moments vanish (Z2) clear every bar at ℓ_k of about 1e-28 to 1e-25 m.
  - **Price (suggested):** a non-locality scale ℓ_k plus a signed hop profile with cancelling moments.

- **K referee (codex sol):** lane K is **INCONCLUSIVE**. The registered setting was neither computed nor defined well enough to compute. K-num is rejected as a lane FAIL; it stands only as a bounded side result for a substitute model. K-ana is partially supported. Strongest statement: "Two shear tunings alone are not established; additional speed-sector protection/tuning remains an open, generically expected cost." See `agents/C3_K_referee.md`.

- **X1 referee (codex sol):** CONFIRMED WITH CORRECTIONS, bounded FAIL. Every ensemble-averaged nonzero-q TT stiffness spectrum (two kernels, scalar and fermion functionals) is flat with power S >= 2.07e-3, in finite periodic Poisson ensembles. Not an asymptotic no-go for random lattices. See `agents/C3_X1_referee.md`.

- **X2 referee (codex sol):** CONFIRMED WITH CORRECTIONS, bounded FAIL. The FR3 gases have a metric-independent stationary law (G_T = 0) but white stress noise (n_S = 0). Activity stresses have contact responses, and frozen dilution has a positive static shear. Every preregistered model fails; not a theorem about all classical gases. See `agents/C3_X2_referee.md`.

- **Lemma L referee (codex sol): CONFIRMED WITH CORRECTIONS.**
  - **Established:** for a deterministic, strictly causal, square-integrable pair kernel on a Poisson process, the covariance of the path-resolvent amplitude is exactly a sum of nonnegative ladders with rung ρb²|G_m|². There are no Johnston-type emptiness overlaps or signed cross terms.
  - **The exponential conclusion needs more:** translation and Lorentz invariance, a nonzero light-cone normalization and nonzero ends.
  - **It does not validate the M-A packet prefactor used in S0.** See `agents/C3_LemmaL_referee.md`.
- **Price note v4 referee (codex sol): APPROVE WITH CORRECTIONS** (8 scope and bookkeeping corrections; the numerical audit is clean). See `agents/C3_P_referee.md`.
- **G-L (link-only lensing):** the worker says FAIL; the adversarial check supports it with corrections. Link/GR = (νΔ)^{−1/2} is a density-independent O(1) mismatch: the link mean de-magnifies where GR magnifies. The codex referee is running.

- **G-L referee (codex sol):** CONFIRMED WITH CORRECTIONS: FAIL for the mean of the unweighted massless one-hop link kernel aL on a fixed curved Poisson sprinkling. Link/GR = (nu Delta)^(-1/2), a density-independent O(1) mismatch (pre-caustic, regular null tubes). It does not extend automatically to G-B (still INCONCLUSIVE), to E1' (flat PASS unchanged), or to weighted links, multi-hop, BD inversion, metric-aware density or other readouts. See `agents/C3_G-L_referee.md`.

### C3 closed (03:20Z; owner's stop: midnight Eastern, 04:00Z)

Every pre-registered lane returned and was recorded. Every FAIL or contested claim was refereed by codex sol:
- G-A, G-B, G-C, G-L;
- M-A, M-B, M-C;
- D, F, K, X1, X2;
- Lemma L and the price note.

M-D and the three exercises are same-family only, and labelled so. No new work was started after 03:20Z, so nothing is "not completed".

## Lane R: gauge redundancy as the primitive (owner, 2026-10-10)

**Owner request:** "run probes on option 3" (option 3 of the status reply: make a gauge redundancy among records the primitive and test whether a massless, protected spin-2 mode comes out). Test settings only; nothing here is recorded in the axiom memo. Any redundancy found is named as a price.

**The question.** Is there a local redundancy on the framework's records or qubits (on Z³, or on events) under which a massless helicity-±2 mode exists *and* is protected, so that no local term allowed by the redundancy gives it a mass?

**Probes** (Claude Opus 5.5, xhigh, run in parallel; same family):
- **R0, prior art.** The repo (UNIVERSAL_GR_*, GRAVITON_MASS_*, the 09-28 Gu–Wen/Pretko lead, the viability campaign) and the literature (Gu–Wen, Xu, Pretko, Rasmussen–You–Xu, emergent-photon analogues).
- **R1, framework-native.** Which transformations of record or qubit states leave every physical readout unchanged, and can any of them be local, giving a tensor Gauss law?
- **R2, lattice computation.** A rank-2 symmetric-tensor model on Z³:
  - its spectrum and gapless helicities;
  - its dispersion;
  - protection against every local term that respects the redundancy, and against the label-dependent shear terms of the stiffness wall;
  - speed and universality of its coupling to matter.
- **R3, events.** A quantum sum over event orders, with relabelling of events as the redundancy (G-C's open item).

**Fixed readings** (for each probe, and for the lane overall):
- **PASS:** an explicit local redundancy, stated as a price, under which a model satisfies all four of:
  - (i) it has a gapless helicity-±2 mode, with linear dispersion;
  - (ii) the mode stays gapless under every local term that respects the redundancy (checked against a complete term list to the order stated);
  - (iii) it couples to matter's energy and momentum universally at linear order;
  - (iv) it needs no more hand tunings than P0, with one-speed tunings counted too.
- **FAIL:** for each candidate class, one of the following is shown:
  - no gapless helicity-2 mode;
  - protection needs tuning comparable to P0;
  - the dispersion is not linear without tuning;
  - universal coupling is impossible.

  Bounded to the classes examined.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation (registered before any probe returns).**
- Gu–Wen-type models give gapless helicity-±2 modes protected by an emergent gauge structure, as spin ice protects its emergent photon. So (i) and (ii) are expected to pass.
- (iii) is expected to fail or stay open. The emergent "graviton" sources a conserved vector or fracton charge, not matter's energy and momentum, and Weinberg–Witten-type limits apply once the low-energy theory is Lorentz invariant.
- (iv) is expected to need at least one speed tuning, a Collins-type split between the graviton and matter.
- The spatial-only constraint ∂_i E_ij = 0 lacks a Hamiltonian constraint, so the mode content may differ from linearized GR.
- **Expected lane reading:** INCONCLUSIVE, leaning FAIL on (iii).

**Rules.** Every FAIL is refereed by codex gpt-5.6-sol at xhigh before it is recorded. These readings are not changed after the runs.

### Lane R results (2026-10-10, 10:28Z to about 11:40Z)

**Who ran it.** Probes R0–R3: Claude Opus 5.5 at xhigh (same family). Referees for R1, R2 and R3: codex gpt-5.6-sol at xhigh. R0 is a prior-art survey and has no verdict. Reports are in `agents/R{0..3}_report.md`, referee reports in `agents/R{1,2,3}_referee.md`, scripts in `scripts/laneR/`.

**Prior-art miss.** Lane R is not new. It was already run as the "tensor / constraint route":
- the 09-14 note `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_…_2026-09-14.md` on main;
- probes 10–21 on PR #9363;
- the 09-29 wall exercise.

R0 found these. The supervisor's "option 3 untested" was wrong.

- **R1 (framework-native).** Worker: FAIL bounded to 4 classes. **Referee: NOT CONFIRMED, so INCONCLUSIVE.** Narrow negatives:
  - V gives ω ∝ k² and VS gives ω ∝ k³, in the regular analytic compact class.
  - Traceful scalar charge cannot couple directly to a generic conserved stress.
  - Integer gauge parameters allow periodic masses.
  - The axioms supply no tensor redundancy.

  Corrections:
  - Lemma D is argued, not proved.
  - "Compact ⇒ k² or k³" is too broad.
  - R1-d (non-compact slots) is wrong for effective fields, since a noncompact infrared field can emerge from qubits.
  - c = ½ comes from constraint preservation within the ansatz, not from closure.

  Open: Gu–Wen N-type at strong coupling; an emergent noncompact VS + Einstein–Hilbert sector; matter as tensor defects.
- **R2 (rank-2 models on Z³).** Worker: FAIL. **Referee: NOT CONFIRMED, so INCONCLUSIVE.**

  Confirmed:
  - In the strong class, S, S-tl, V and V-tl have 5, 4, 3 and 2 modes, with dispersions k, k, k² and k³.
  - Scalar charge gives linear TT modes only together with gapless partners, and its charge cannot be mobile energy.
  - Strong V/VS theories are too soft, and pure V has no minimal Newtonian source.
  - Gauge invariance removes A-only TT masses.
  - Breaking the redundancy brings back exactly P0's μ_E and μ_T2.
  - The speed tunings are 3, or 4 without P/T, as a local codimension. (iv) is INCONCLUSIVE.

  Open, and the strongest counter-route: **exact-constraint weak VS/N-type**. It has two positive linear TT modes and an attractive 1/r response to a supplied source; what remains open is the exact lattice stress/source bridge and a compact realization. Also open: mixed charges, defect matter, and nonlinear or nonperturbative phases.
- **R3 (sum over event orders, on top of P1–P4).** Worker: INCONCLUSIVE leaning FAIL. **Referee: CONFIRMED WITH CORRECTIONS.**
  - The class-A FAIL is not supported; class A is INCONCLUSIVE. A2 and A3 are unsupported, and the variance-to-TT-damping bridge is missing.
  - Class B (positive fixed-coefficient interval-count weights) is a bounded FAIL: the bilayer sector is not suppressed.
  - Relabelling is an exact discrete quotient with no local gauge generators.
  - The orbit-volume T⁶ lemma holds only for short-range timelike kernels.
  - Prices: R3-a and R3-c stand. R3-b conflicts with P4. R3-d is only a candidate escape.

**Lane R verdict: INCONCLUSIVE.** No PASS. Every refereed negative is class-bounded. The one live construction is the exact-constraint weak (N-type) VS theory, but nothing derives its coupling to matter's energy-momentum on the lattice, or its realization in qubits.

**Against the registered expectation:**
- (i) holds in the strong class only for scalar charge, and then with partners. It was expected to pass generally.
- (ii) passes, scoped to local analytic terms.
- (iii) is unresolved, not failed.
- (iv) is INCONCLUSIVE, as expected.

**Decisive next test.** Couple a lattice matter field to the exact-constraint VS/N-type theory through lapse and shift. Can its stress satisfy the Gauss identities exactly, the K3a/Lemma R question, without regenerating μ_E and μ_T2?

## Lane RN: matter coupled to the exact-constraint VS (N-type) theory through lapse and shift (owner, 2026-10-10)

**Owner request:** "run the lapse/shift matter coupling test". This is lane R's decisive next test. It is a test setting only, and nothing here is recorded in the axiom memo.

**Prior art (read first; this lane must go beyond it):**
- **K3a and its referees** (`candidates/candidate-law-20261008/TEST_LOG.md:236-262`, `checks/referee_K3a*/`):
  - Free 3D Maxwell has an EXACT stress of radius ½ (207 coefficients).
  - In staggered QED at O(e), genuine lattice-scale umklapp resonances obstruct every conserved momentum in the tested bounded class: one-body, electron range ≤ 4, scalar photon weight.
  - The referee left open larger, quasi-local, polarization-matrix, higher-body and engineered stresses.
- **K3a2:** an O(e²) TT contact term of about 1e-2·e² per cell on the fixed grid.
- **The landed 09-14 note:** H_N gives linear TT modes and a 1/r response to a supplied source.
- **Lane R referees:** `agents/R1_referee.md`, `agents/R2_referee.md`.

**Setting.**
- **Gravity:** the linearized exact-constraint weak VS theory on Z³ (H_N of the 09-14 note), with canonical (h_ij, π_ij).
- **Coupling:** H = H_N + H_m + N·(C_s − T₀₀) + N_i·(C_i − T₀ᵢ) + ½h_ij·T_ij, with lattice difference operators. Here N and N_i are the lapse and shift multipliers.
- **Matter:** local lattice laws with a finite local Hilbert space or a bosonic stand-in, free and interacting.
- **Consistency requirement:** the constraints stay first class. This requires the lattice identities ∂_t T₀₀ + ∇·J = 0 and ∂_t T₀ᵢ + ∇_j T_ij = 0 to hold exactly, using the same T_ij that couples to h.

**Probes** (Claude Opus 5.5 at xhigh, in parallel, same family):
- **L1, free matter.**
  - For each of a free lattice scalar, a staggered fermion and Maxwell: find the exact local stress (pseudo-momentum) and verify that the constraints are first class.
  - Show that the TT modes are gapless with no tuning.
  - Universality: two species with different masses get the same G.
  - Newtonian 1/r.
  - PPN γ from massless matter, i.e. light bending.
- **L2, interacting matter.** Onsite φ⁴, two-species contact, and Hubbard-type staggered interactions.
  - Do an exact linear-algebra search for a stress satisfying the identities. Extend the class beyond K3a: longer range, higher-body, matrix-valued, quasi-local with fitted decay.
  - If there is none, compute what the violation does in the exact-constraint theory: constraints turn second class, giving an extra mode or a TT mass. Compute the induced μ_E and μ_T2 at the first nonvanishing order and compare with natural size.
- **L3, escapes and literature.**
  - Lapse-only coupling (no shift): γ, light bending, Shapiro delay.
  - Matter as defects of the tensor field: vector charges are momentum by construction. Are they mobile, or lineons?
  - Transverse-diffeomorphism and unimodular variants, and the Hořava projectable case.
  - Literature: lattice energy-momentum tensors (Caracciolo et al., Suzuki), and Gu–Wen's matter coupling.

**Fixed readings.**
- **F-PASS / F-FAIL (free matter).** F-PASS: every free law tested has an exact local stress, the constraints stay first class, the TT modes stay gapless untuned, the coupling is universal, the pull is Newtonian 1/r, and γ = 1 at leading order. F-FAIL otherwise, with the failing item named.
- **PASS.** Some interacting local matter law (stated: Hilbert space, range, interaction) has a local or exponentially quasi-local stress that obeys the identities exactly to the order computed, and with it:
  - the constraints stay first class;
  - μ_E = μ_T2 = 0 with no tuning;
  - G is the same for at least 2 species;
  - γ = 1 at leading order.
- **FAIL.** For the interacting classes tested (ranges, body orders and laws stated), no such stress exists, and at least one of the following holds:
  - the violation makes the constraints second class, with an induced TT mass or extra mode of natural size × (coupling)², untuned;
  - the escapes tested in L3 fail an observational bar (γ, Shapiro delay, or mobility).

  Bounded to the classes examined.
- **INCONCLUSIVE.** Otherwise.

**Supervisor expectation (registered before any probe returns).**
- **L1:** F-PASS. Free lattice fields have exact local pseudo-momentum, and the K3a Maxwell result shows this.
- **L2:** no finite-range or quasi-local stress for generic interactions. The cause is umklapp: lattice interactions have trigonometric-polynomial kernels with momentum transfer across the zone. The constraints turn second class, and μ comes out of order λ² × natural. That is a bounded FAIL, whose price is a non-local (momentum-space cutoff) interaction.
- **L3:**
  - Lapse-only coupling gives γ ≠ 1, failing Cassini (|γ − 1| < 2.3e-5).
  - Defect matter is restricted in mobility.
- **Expected lane reading:** FAIL (bounded), with the price "non-local interactions or an exact lattice momentum not in the axioms".

**Rules.** Every FAIL is refereed by codex gpt-5.6-sol at xhigh before it is recorded. These readings are not changed after the runs.

### Lane RN results (2026-10-10, 11:15Z to about 12:50Z)

**Who and where.**
- Probes L1–L3: Claude Opus 5.5 at xhigh (same family).
- Referees: codex gpt-5.6-sol at xhigh, one per probe.
- Files: probe reports in `agents/RN_L{1,2,3}_report.md`, referee reports in `agents/RN_L{1,2,3}_referee.md`, scripts in `scripts/laneRN/`. The referees' own checks are included there.

**L1, free matter. Worker: F-FAIL (item 3 named). Referee: CONFIRMED WITH CORRECTIONS. Recorded as F-FAIL by the fixed binary; scientifically INCONCLUSIVE, since nothing failed and items were left incomplete.**
- **Free scalar:**
  - It has an exact local symmetric lattice stress (exact in rational arithmetic).
  - The lapse/shift coupling is first class at linear order.
  - The pull is Newtonian 1/r, with the same G for different masses.
  - γ = c_m²/c_g². Setting γ = 1 is the speed match R2 already counted.
  - The cubic correction is −Σk⁴/(4k²).
  - The sign of the h coupling is −½h_ijT_ij in lower-index conventions.
- **Referee correction:** a unitary seagull H_sg = −½[K_h,[K_h,H_m]], with K_h = ½h_ij Σ X_j P_i, cancels the linear-only TT susceptibilities (−0.0037 and −0.0118) exactly at uniform strain. It is finite-range, and its coefficients are fixed by H_m and P, not tuned. No physical TT mass from free matter is demonstrated.
- **Open:**
  - extending the seagull to non-constant h, with a full first-class algebra at O(κ). The matter-only bracket {P,P} lies outside the flat P, T00 span, but the metric-dependent completion was not searched;
  - the symmetric stresses for the fermion and Maxwell.

**L2, interacting matter. Worker: bounded FAIL. Referee: NOT CONFIRMED, so INCONCLUSIVE.**
- **Established:** for d ≥ 2, massive nearest-neighbour lattice KG and scalar tight-binding bands have no nonzero odd periodic C¹ collision invariant (consistent with Spohn: only aω + c). So no local or exponentially quasi-local higher-body dressing can give a conserved momentum with a nonzero scalar one-particle action. This holds exactly in contact U, and at O(λ) for analytic onsite φ⁴.
- **Not established:**
  - a forced natural-size TT mass. μ_E = −1.009e-6·λ² and μ_T2 = +1.61e-8·λ² per cell are reproduced, but they depend on the coupling design, and the off-shell dressing loophole is real;
  - "second class" (no bracket-rank computation);
  - the 5-DOF count, which is wrong.
- **Open:** matrix-valued (staggered taste) charges; gauge-mediated scattering; non-perturbative effects; zero-scattering laws; alternative coupling completions. XXZ is a valid 1D control only.

**L3, escapes. Referee: CONFIRMED WITH CORRECTIONS.**
- **Lapse-only coupling: FAIL** for the classes studied:
  - as a direct multiplier, SK = −DG freezes T00 pointwise (mobility);
  - as a natural fixed potential, γ = 0 and the Shapiro delay is half of GR's.
- **The "conserved energy current ⇒ ballistic heat" upgrade of K3a is not established.** It needs a lattice-cohomology lemma, and the φ⁴ numerics were averaged wrongly. The corrected numbers are C(50)/C(0) = 0.05 ± 0.07 and −0.07 ± 0.06.
- **Defect matter: INCONCLUSIVE.** The kinematics are correct, but universality does not follow from a topological charge, and binding, inertia and stability are not shown.
- **TDiff, unimodular and Hořava are not escapes.** The projectable scalar has ω² = −(1−2c)Jg k².
- **Kato–Sakamoto–So** gives the local Leibniz obstruction, but not a blanket theorem that no lattice momentum exists.

**Lane RN verdict: INCONCLUSIVE.**
- Under the fixed FAIL reading, the "no stress" leg is met only for the scalar single-band interacting classes.
- The second leg is not met: the mass is not forced, and one L3 escape (defect matter) does not fail a bar.
- No PASS.

**Strongest combined statement.**
- Ordinary single-band interacting lattice matter in d ≥ 2 cannot feed the exact-constraint VS shift constraint through a local momentum. So the live N-type route needs one of:
  - matrix-band (staggered) matter whose tastes supply extra collision invariants;
  - gauge-mediated interactions;
  - defect matter with universality still to be shown;
  - a non-local momentum (price).
- Free matter couples consistently at linear order, and its uniform-strain TT response is cancelled by a determined seagull.

**Against the registered expectation.**
- L1 was expected to be F-PASS; it is F-FAIL by the binary, because items are incomplete.
- L2 was expected to be a bounded FAIL with an O(λ²) natural mass; the mass is reproduced but not forced, so INCONCLUSIVE.
- L3's lapse-only FAIL was as expected. Defect matter was expected to fail on mobility; it is INCONCLUSIVE instead.
- The expected lane reading was FAIL; the result is INCONCLUSIVE.

**Next decisive tests:**
1. Interacting staggered fermions, the framework's own matter: do matrix-valued taste charges give an exact local momentum (a K3a/L2 extension)?
2. The seagull for non-constant h, with full O(κ) closure, for the free scalar.

## Lane RS: interacting staggered fermions as the source of an exact lattice momentum (owner, 2026-10-10)

**Owner request:** "run the staggered fermion test". This is lane RN's decisive next test. It is a test setting only, and nothing in it is recorded in the axiom memo.

**The question.** Lane RN's L2 refereed result covers only scalar single-band matter: in d ≥ 2 its collisions conserve no momentum. Can the framework's own matter, staggered fermions, do better? Staggered fermions carry one component per site, have 2^d taste corners, and their dispersion has period π. Do their taste and matrix structure supply an exactly conserved local, or exponentially quasi-local, momentum density once they interact? Such a density would let them feed the exact-constraint VS shift constraint.

**Prior art to extend, not repeat:**
- K3a: staggered QED at O(e), with a one-body symbol and a scalar photon weight. Its referees left matrix-valued charges open.
- RN L2 and its referee: the two-body collision reduction (a necessary condition), and Spohn's result that only aω + c survives.
- RN L1: the free staggered fermion's energy current is exact, and P_j = ½{J_j, h} commutes with h.

**Probes** (Claude Opus 5.5 at xhigh, run in parallel; same model family as the supervisor):
- **S1 (contact interactions).** Staggered fermions in d = 2 and 3, with a nearest-neighbour density–density interaction (the natural interaction at one per site), plus a taste-invariant four-fermion contact.
  - Analytic: a collision-invariant analysis with matrix-valued charges (taste and sublattice symbols, the reduced zone).
  - Numeric: exact null spaces on the on-shell 2↔2 manifold, plus an exact operator check of [H, P] on finite clusters for any candidate.
- **S2 (gauge-mediated interactions).** Staggered QED at O(e²), with the photon included as a species (Møller and Compton channels), and any further gauge-mediated class that is feasible.
  - If either probe finds a passer, follow it through: build its symmetric stress, check first class at linear order, check that G is the same for every taste, and check γ.

**Fixed readings.**
- **PASS.** An interacting staggered law, with d, interaction and range stated, has an exactly conserved local or exponentially quasi-local momentum. Its one-particle action must have a nonzero, taste-universal slope at every taste corner. Both checks must hold: the collision null space and the exact cluster operator check. Its stress must feed the constraints first class at linear order.
- **FAIL.** For each stated interaction class, there is no odd collision invariant with nonzero slope at the taste corners. This is proved, or checked with order-one singular gaps, matrix-valued charges included. Bounded to those classes.
  - This lane's FAIL concerns the momentum only. Whether the failure forces a graviton mass is lane RN's open question, and it is not re-asked here.
- **INCONCLUSIVE.** Otherwise.

**Supervisor expectation (registered before any probe returns).**
- The period-π dispersion gives taste-shift structure: k_i → π − k_i maps the band to itself. That yields discrete Z2 taste charges, not an additive momentum.
- Matrix charges add invariants only on resonant, degenerate submanifolds.
- So both S1 and S2 are expected to FAIL (bounded).
- The price then stays "non-local momentum, or an exact lattice momentum not in the axioms".

**Rules.** Every FAIL is refereed by codex gpt-5.6-sol at xhigh before it is recorded. These readings are not changed after the run.

### Lane RS results (2026-10-10, 19:50Z to about 21:30Z)

**Who and where.**
- Probes S1 and S2: Claude Opus 5.5 at xhigh (same family as the supervisor).
- Referees: codex gpt-5.6-sol at xhigh, one per probe.
- Reports are in `agents/RS_S{1,2}_report.md` and `agents/RS_S{1,2}_referee*.md`; scripts, including the referees' checks, are in `scripts/laneRS/`.

**S1 (nearest-neighbour density–density V, and a hypercube-summed taste-invariant contact U).** Worker: FAIL (bounded). **Referee: CONFIRMED WITH CORRECTIONS, bounded FAIL (momentum only).**
- **Analytic result.** A regular, coupling-analytic, local or exponentially quasi-local conserved charge with a nonzero taste-universal slope has to satisfy the Born collision intertwiner. Shift averaging, sector sewing on the double cover, and Spohn applied to the exact KG map ε_stag(k) = ½ω_KG(2k; 2m) together exclude it in d = 2 at every mass and in d = 3 at m = 0.
- **d = 3, m = 0.5.** Numerical only. No odd invariant appears in the matrix spaces through R = 4, and the gaps are order one. There is no all-range theorem.
- **Corrections:**
  - at m = 0 and k = 0 the eigenvalue 0 has multiplicity 2^d;
  - the normalization of the U kernel is off by a factor of 2, which changes no result;
  - the massless gradient has a cusp, and C¹ locality removes it;
  - the averaging excludes the required universal slope, not every odd invariant.
- **Cluster exact diagonalization (6×6, N = 2):** on-shell norm 0.204, distance to the commutant 0.677. This is reproduced, but it is a limited reading.

**S2 (noncompact staggered QED, Born sector at O(e²)).** Worker: FAIL (bounded). **Referee: CONFIRMED WITH CORRECTIONS, bounded FAIL (momentum only).**
- **Result.** For d = 2 and 3 and m = 0 and 0.5, a perturbatively analytic conserved local or quasi-local charge cannot have a nonzero taste-universal fermion slope.
- **Why.**
  - A regular Møller patch is invertible.
  - The trace of the charge then obeys the scalar staggered collision equation.
  - The KG map plus analytic periodicity removes the odd slope.
  - Spohn's theorem also covers m = 0.
- **Corrections:**
  - the light-cone inequality holds only for equal-sign bands; opposite-sign bands keep pair resonances;
  - the O(e) pair resonances add constraints and do not relax any;
  - the trace lemma constrains only the normalized trace. Traceless equal-magnitude slopes are not excluded analytically, but they are not taste-universal;
  - the zero photon slope is strongly checked but conditional, because there is no connectivity theorem;
  - the Z2 reduction is not confirmed.

**Lane RS verdict: FAIL (bounded, momentum only). Both probes are refereed, CONFIRMED WITH CORRECTIONS.**
- The framework's own matter, staggered fermions, interacting through contact or perturbative QED, supplies no exactly conserved local or quasi-local momentum with a taste-universal slope.
- So it cannot feed the exact-constraint VS shift constraint.
- Open:
  - strong or non-analytic coupling;
  - power-law-tailed charges;
  - d = 3, m > 0 beyond R = 4;
  - number-nonconserving or higher-body leading interactions;
  - compact confinement;
  - Z2 gauge fields;
  - traceless taste sectors, which are not taste-universal.

**Against the registered expectation.** The FAIL in both probes is as expected, but the mechanism is different. Taste structure adds nothing: invertible amplitudes collapse matrix charges onto their trace, and the staggered band is lattice KG at (2k, 2m). No degenerate resonant submanifold rescues anything.

**Price, unchanged:** a non-local momentum, i.e. interactions not nearest-neighbour (against Admissibility), or an exact additive lattice momentum that the axioms do not supply.

### Correction to the lane RS price wording (owner, 2026-10-10)

The owner asked: "we don't have an only-nearest-neighbour rule, right? You can influence through networks of nodes."

**That is correct.** Admissibility (`MINIMAL_AXIOMS_2026-06-29.md:57-61,116-125`) fixes only the local rule: each site's odds are set by its nearest neighbours. It explicitly chooses no Hamiltonian, transfer operator or dynamics. Influence can therefore reach any distance through chains of sites.

The phrase "interactions not nearest-neighbour (against Admissibility)" in the RS entry, and the matching line in SUMMARY §13, overstate what the axiom forbids. The phrase is withdrawn as a statement about the axiom. The RS and RN results themselves are unchanged.

**What the refereed results actually exclude** is defined by the conserved charge's reach, not by how the interactions arose:
- **Covered:** charges whose momentum density has a summable first moment, i.e. finite range or exponential tails (RN L2, RS S1/S2). Any effective interaction a network of nearest-neighbour steps produces through *gapped* intermediate nodes falls in this class.
- **Covered:** a gapless photon network at the Born level (S2).
- **Not covered, and the open form of the owner's idea:** a *gapless* network that produces power-law-tailed charges and interactions. The one candidate momentum that survives ordinary collisions is the sawtooth f = k, whose density has 1/r tails (RN L2). It fails only on umklapp, i.e. scattering across the zone boundary. So the open question is whether a nearest-neighbour rule acting through a gapless network can give matter interactions with no umklapp, and with them an exactly conserved sawtooth momentum.

**Corrected price wording:** "a momentum density with power-law tails, together with matter interactions with no umklapp (whether a nearest-neighbour rule can produce this through gapless networks is untested), or an exact additive lattice momentum that the axioms do not supply."

## Lane RG: gapless networks and umklapp (owner, 2026-10-10)

**Owner request:** "run the gapless network umklapp test". This follows the owner's correction that influence can travel through networks of nodes. It is a test setting only, and nothing here is recorded in the axiom memo.

**The question.** Take a nearest-neighbour rule that acts through a network of nodes: a finite number of fields per site, covariant under translations and proper cubic rotations, with any depth and with gapless mediators allowed.
- Can it give matter interactions that vanish exactly on every umklapp configuration, i.e. collisions whose momenta wrap across the zone edge, while staying nonzero on normal ones?
- If so, the sawtooth momentum f = k, whose density has 1/r tails, is an exact collision invariant (RN L2) and could feed the VS shift constraint.

**Prior art.**
- RN L2 and its referee: the sawtooth momentum survives ordinary collisions and fails only on umklapp.
- RS S1 and S2 and their referees: summable-first-moment charges are excluded. A gapless photon at the Born level is covered.
- The Correction entry above.

**Probes** (Claude Opus 5.5 at xhigh, run in parallel; same model family as the supervisor):
- **G1, theorem and loopholes.**
  - Prove or refute: if the 2↔2 amplitude, and every matter–mediator amplitude, is real-analytic on the connected on-shell torus, then vanishing on the umklapp set (which has an interior) forces it to vanish identically. Gapless propagators are meromorphic and singular only at isolated points, so they fall in this class.
  - Enumerate the sources of non-analyticity a local network can produce: cone points, Fermi surfaces (Kohn anomalies), critical points, the infinite-depth or thermodynamic limit. For each, decide whether it can give an amplitude that vanishes on an open umklapp set but not everywhere.
- **G2, constructions and the quantitative readout Q.** Build explicit networks:
  - (a) vertex form factors that vanish at the zone edge, such as (1 + cos k)^n;
  - (b) a mediator with a Fermi sea (a Lindhard kernel);
  - (c) deep networks that approximate a smooth momentum-space cutoff.

  Measure the relative umklapp amplitude ε_U against network depth or size n, and fit its decay law.
- **G3, sourcing and consequence.**
  - Can a momentum density with 1/r tails, built or carried through the network, source the VS shift constraint consistently at linear order?
  - If momentum is conserved only up to a residual ε_U, how does the induced TT response scale with ε_U (RN L2's μ)?
  - Translate this into the network depth or interaction range needed to meet the observational graviton-mass bound.

**Fixed readings.**
- **PASS.** An explicit network law, with fields, rule and mediator stated, meets all of the following at the order computed:
  - its effective matter 2↔2 amplitude, and its matter–mediator amplitudes, vanish exactly on all umklapp configurations and are nonzero on normal ones;
  - so a momentum with a taste-universal slope is an exact collision invariant;
  - that momentum sources the VS shift constraint consistently at linear order.
- **FAIL.** For the stated class (finite fields per site, finite-range rule, any network depth), it is shown, proved or checked, that an umklapp-free amplitude must vanish identically: for analytic amplitudes, and for each non-analytic source examined. Bounded to that class.
- **INCONCLUSIVE.** Otherwise.
- **Readout Q (recorded as a number; not a pass/fail item).** The best ε_U(n) decay law, and the depth or range n* needed for the induced TT response to meet the bound.

**Supervisor expectation (registered before any probe returns).**
- **G1:** the identity theorem excludes every analytic class, so exact umklapp-free interactions with local networks are impossible. Fermi-surface and cone non-analyticities live on sets of measure zero and cannot create an open zero set, so FAIL (bounded) in the classes examined.
- **G2:** ε_U(n) falls exponentially with depth, at best e^{−cn}.
- **G3:** a 1/r-tailed density can source the constraint only non-locally. The induced TT response is about ε_U² times natural, so n* is of order 10² to 10³ sites.
- **Expected lane reading:** FAIL (bounded) for exact conservation. Q would reframe the price as "an interaction range of hundreds of grid steps" rather than true non-locality. Whether an approximate constraint is acceptable is a separate question that this lane does not decide.

**Rules.** Every FAIL is refereed by codex gpt-5.6-sol at xhigh before it is recorded. These readings are not changed after the run.

### Lane RG results (2026-10-11, 00:53Z to about 02:40Z)

**Who and where.**
- Probes G1–G3: Claude Opus 5.5 at xhigh (same family as the supervisor).
- Referees: codex gpt-5.6-sol at xhigh. One refereed G1 together with G2's constructions; the other refereed G3.
- Files: `agents/RG_G{1,2,3}_report.md`, `agents/RG_G1G2_referee.md`, `agents/RG_G3_referee*.md`. Scripts, including the referees' checks, are in `scripts/laneRG/`.

**G1, the theorem. Worker: FAIL (bounded). Referee: NOT CONFIRMED → INCONCLUSIVE.**
- **Confirmed:**
  - Consider an exact conserved charge that acts additively and diagonally on asymptotic particles, with any integrable lift of crystal momentum. It forces the total 2↔2 amplitude to vanish almost everywhere on an umklapp set of positive measure. For piecewise-smooth domains that set is open.
  - Any globally meromorphic amplitude on a connected M_reg must then vanish identically. The TB connectivity proof is confirmed; KG connectivity is conditional (checked plus argued).
  - This rigorously covers:
    - finite-depth tree exchange;
    - finite-component quadratic-network resolvents;
    - nonzero rank-one contact scattering.
  - Coupling-analytic Born families and factorized positive-spectral-weight exchange are covered only with additional hypotheses.
  - G1's correction to the supervisor's premise stands: a codimension-1 wall can bound an open zero set.
- **Not closed, and inside the registered class:**
  - dressed vertices at fixed strong coupling;
  - general interfering spectral exchange;
  - nonperturbative non-contact finite-range potentials. G1-B′ could reduce to fixed-energy inverse scattering, but the step that carries a partial zero patch over to full scattering data is missing.
- Pauli complementarity is argued at tree level only. Edge-of-the-wedge closure is not available.

**G2, the constructions. Referee: main checks pass, with one correction.**
- The binomial filter gives an exact on-shell supremum of 16^(−r), nonzero at finite depth.
- The static Lindhard kernel does not help.
- **Correction:** the fixed-window and Chebyshev "2↔2 sup" rates did not impose energy conservation. They are certified momentum-space upper bounds, not optimal on-shell rates.
- These filters are low-pass: they suppress lattice-scale normal scattering as well as umklapp, and do not isolate umklapp.

**G3, sourcing and consequence. Referee: CONFIRMED WITH CORRECTIONS.**
- **Confirmed:**
  - With the fixed 09-14 constraints and regular kernels, a matter-only sawtooth shift source requires an exactly SLAC scalar dispersion. Nearest-neighbour KG gives sin k instead.
  - The SLAC stress satisfies the linear first-class identities, but it is power-law non-local: P ~ R⁻², T is log-corrected R⁻², and neither is absolutely summable.
  - The E-channel sawtooth dilation has no self-adjoint generator on the fixed-zone space.
- **Not confirmed:**
  - The "+1.7 floor" depends on the completion chosen.
  - The O(λ²) sawtooth coefficients do not converge in L. At L = 127 they are (0.93, −0.44)e-6, and continuum-first integration gives about (0.80, −0.70)e-6.
  - No vacuum term is forced, because of the dressing loophole.
- **Not excluded:** network-carried or singular conserved additions, matrix bands, and modified constraint completions.

**Readout Q (conditional).**
- **Amplitude suppression to 1e-100:** about 83 binomial steps, or 5–9e2 fixed-window steps; roughly 1e-33 to 1e-32 m at Planck spacing.
- **Depth to meet the induced-TT bound:** n* ≈ 113/c for a quadratic law, doubled for a linear one. This holds only if a design-dependent floor is removed. "No finite n*" applies only if a nonzero floor stays uncancelled.

**Lane RG verdict: INCONCLUSIVE.**
- An exact umklapp-free interaction is impossible for every analytic or meromorphic class: finite networks, quadratic networks of any depth, contact interactions at any strength, and weak-coupling families.
- What remains open is non-analytic:
  - strongly coupled dressed walls;
  - nonperturbative finite-range potentials.
- Even with umklapp removed, regular nearest-neighbour matter cannot source the constraint through the sawtooth. That would need SLAC (1/r²-hopping) matter, or a demonstrated network carrier.
- Approximate suppression is exponential in depth, about 10² steps for 1e-100.

**Against the registered expectation.**
- G1's FAIL was not confirmed; the open strong-coupling routes are inside the class.
- The measure-zero premise was wrong for codimension-1 walls.
- G2 is as expected: exponential suppression, c of order 1.
- G3 adds a requirement that was not foreseen: the momentum that feeds the shift must equal the energy current, which forces SLAC matter.

## Lane RC: carrying the energy current (owner, 2026-10-11)

**Owner request:** "continue with the next tests". This lane follows lane RG's open items. It is a test setting only, and nothing here is recorded in the axiom memo.

### What lane RG left
The shift source must equal the energy current. Two refereed results set this up:
- G3: div P_shift = div J_E.
- The RN L3 referee: the equality holds only up to divergence-free improvements.

So feeding the shift needs a conserved total energy current whose one-particle symbol is E∇E, i.e. ballistic energy transport. If that momentum is the sawtooth, the dispersion must be exactly SLAC, and the interactions must be free of umklapp.

### Probes
All three run in parallel on Claude Opus 5.5 at xhigh (same model family as the supervisor).

**C1. Reduction and emergent SLAC bands.**
- (a) Prove or refute the reduction: (shift-source closure) + (odd collision invariant on an umklapp-free law) ⇒ f is linear on the lifted zone ⇒ E² = c²|k|² + const exactly.
- (b) Can a nearest-neighbour network of finitely many fields per site produce an exact SLAC band as an emergent quasiparticle band? Examples: a polaron, or a band dressed by gapless mediators. Candidate obstruction: k is transcendental over the field of trigonometric polynomials, so no eigenvalue branch of a finite trig-polynomial matrix equals √(m² + c²k²) on an open set.
- (c) Readout Q1: the best approximation error to the SLAC band as a function of network depth n.

**C2. Strong-coupling candidates.** The aim is the open corner of lane RG. Survey exactly solvable or strongly coupled lattice models in d ≥ 2 and ask whether any has an exactly conserved total energy current, i.e. ballistic thermal transport at T > 0 in the thermodynamic limit. Candidates:
- the Kitaev honeycomb model (free Majoranas in a static Z2 flux);
- toric-code-type and fracton models;
- free-fermion-like models with interactions;
- models with extensively many local conserved quantities.

For each candidate:
- compute [H, J_E] exactly, by operator algebra or exact diagonalization on clusters;
- search linear spaces of local improvements for a conserved current;
- estimate the Drude weight with finite-size scaling.

Restricting conservation to one sector does not count as exact.

**C3. Gravity-side closure for free matter** (lane RN L1's open item).
- Search for a metric-dependent local completion that makes the full O(κ) constraint algebra of the free scalar close with non-constant h: a seagull plus h-dependent corrections to the constraints, within a stated ansatz of range and polynomial order.
- Prior art: Bahr and Dittrich showed that discretization breaks diffeomorphism symmetry on curved backgrounds, which turns constraints second class. Compare with the RN L1 referee's unitary seagull.

### Fixed readings
**C1**
- **PASS:** a finite network gives an exact SLAC band.
- **FAIL:** the reduction holds, and the impossibility is proved for the stated class (finite-component quadratic networks, plus any further class stated).
- **INCONCLUSIVE:** otherwise.
- **Q1 is recorded as a number.**

**C2**
- **PASS:** an interacting nearest-neighbour model in d ≥ 2, stated explicitly, has an exactly conserved local or quasi-local total energy current in all sectors. This must be shown by an exact operator identity plus a Drude weight that stays nonzero under finite-size scaling.
- **FAIL:** every candidate examined has [H, J_E] ≠ 0, and no improved local current is conserved within the searched spaces. Bounded to the candidates examined.
- **INCONCLUSIVE:** otherwise.

**C3**
- **C-PASS:** a local completion within the stated ansatz closes the O(κ) algebra for non-constant h.
- **C-FAIL:** it is proved impossible within the ansatz.
- **INCONCLUSIVE:** otherwise.

### Lane verdict
- **PASS** needs both C1 or C2 PASS and C3 C-PASS.
- **FAIL** needs either:
  - C1 FAIL and C2 FAIL (refereed), or
  - C3 C-FAIL (refereed) on a class that free matter cannot avoid.
- **INCONCLUSIVE:** otherwise.

### Supervisor expectation (registered before any probe returns)
- **C1:** the reduction holds, and the transcendence obstruction makes exact SLAC bands impossible for finite networks. FAIL, with the approximation error exponential in depth.
- **C2:** the Kitaev honeycomb conserves the current only within flux sectors, and at T > 0 flux scattering spoils it. No candidate passes. FAIL (bounded), or INCONCLUSIVE if the survey is thin.
- **C3:** following Bahr–Dittrich, a fixed lattice cannot close the hypersurface-deformation algebra beyond uniform strain. C-FAIL within the ansatz, or INCONCLUSIVE.
- **Lane:** FAIL (bounded).

### Rules
Every FAIL is refereed by codex gpt-5.6-sol at xhigh before it is recorded. These readings are not changed after the run.

### Lane RC results (2026-10-11, 15:43Z to about 17:30Z)

**Who and where.** Probes C1–C3 were run by Claude Opus 5.5 at xhigh (same family). Each was refereed by codex gpt-5.6-sol at xhigh. Files: `agents/RC_C{1,2,3}_report.md` and `agents/RC_C{1,2,3}_referee*.md`; scripts, including the referees' checks, are in `scripts/laneRC/`.

#### C1: reduction and emergent SLAC

Worker: FAIL (bounded). **Referee: CONFIRMED WITH CORRECTIONS. C1 FAIL, bounded to finite-component analytic quadratic networks and the analytic simple-root dressed subclass.**

What the referee confirmed:
- **Lemma C (Koszul).** A finite-range, divergence-free improvement is a local curl plus a constant. This resolves the RN L3 referee's caveat. The transverse-projector improvement, with R^-d tails, remains a formal non-regular loophole.
- **Lemma R.** In d ≥ 2, the C¹ invariants of normal collisions on the lifted zone are λE + b·k + c.
- **Theorem A.** Under transfer-regular improvements, exact additive conservation and full-support normal collisions:
  - closure forces E² = m₀² + β|k|²;
  - closure forbids umklapp;
  - mutually scattering self-scatterers share β.
- **Theorem B1, rigorous in every d.** No finite-component periodic real-analytic one-body matrix has an exact SLAC band on any open set.
- **Theorem B2.** No simple, jointly analytic dressed root can carry the face cusp. A positive-spectral-weight self-energy is therefore excluded wherever its continuum stays gapped. Gapless continua remain open.
- **Readout Q1.**
  - A single smooth band has whole-zone error Θ(1/n) and closure floor πc².
  - The window rates are 3.23, 1.76 and 0.81.
  - A two-band construction touching at the face converges super-algebraically, but is inexact at every finite n, and its partner-band interaction obstruction is unresolved.

Corrections from the referee:
- β need not be c² > 0 without a minimum at k = 0.
- The extension holds through smooth taste degeneracies but not through isolated crossings.
- "Every scattering mediator" is too broad.
- The defect value 2.44 is a sample maximum.

#### C2: strong-coupling survey

Worker: FAIL (bounded). **Referee: NOT CONFIRMED, so INCONCLUSIVE.**

What survives:
- **F1 lemmas.** Hilbert–Schmidt orthogonality, and [H,[H,B]] = 0 ⇒ [H,B] = 0. Exact N-independence also needs alias-free embedding, so N = 8–12 does not exclude every improvement of about 3×3.
- Commuting-term models are immobile, with J_E ≡ 0. They are vacuous non-PASS cases, not FAIL witnesses.
- Theorems exclude local conserved currents for TFIM, XX/XYZ and compass (Chiba; Shiraishi–Tasaki; Futami–Tasaki). The reflection reduction is sound.
- **Kitaev.**
  - The current matrix is −½[A²,X].
  - The zero-flux symbol E∇E and the chiral lemma hold for nondegenerate sectors.
  - The 1e-29 result is machine zero from typical sectors only. Full gauge-orbit sums give r = 0.375 at L = 2 and 0.067 at L = 3.
  - D(T > 0) = 0 is not proved.
- Stacked XXZ is real but violates cubic covariance.

No axiom-admissible PASS was found.

#### C3: gravity-side closure for free matter

Worker: C-FAIL. **Referee: CONFIRMED WITH CORRECTIONS. C3 = C-FAIL within the regular local single-band scalar ansatz.**

What the referee confirmed:
- In the constant-shift, linear-lapse and rotational (global Poincaré) sectors, every regular local gravity-dependent completion vanishes exactly. This holds because GᵀΞ = 0, Gᵀη = 0, and SᵀN = 0 for affine N.
- Closure then needs Hess(ω²/2) to be constant. A periodic function with constant Hessian is constant, which leaves only a dispersionless Carroll contraction, not GR.
- Local improvements of T00 or P cannot remove the obstruction.
- **Mechanism:** P_tot generates central differences factor by factor, not exact translations. Kato–Sakamoto–So is a correct analogy, not the proof.

Corrections from the referee:
- The exact A(π) sequence is −2, −8/3, −16/5, −128/35, −256/63.
- The printed IR residual came from an all-momentum fit.
- Loll proves closure in the continuum limit, not impossibility at finite spacing.

What C3 does not establish:
- Its class is not shown to be unavoidable for free matter. Non-local, multi-band, infinite-band or network, singular-structure-function, altered-generator and non-GR escapes all remain.
- So C3 alone does not meet the lane-FAIL clause.

#### Lane RC verdict: INCONCLUSIVE

- C1 FAIL and C3 C-FAIL are refereed. C2 is INCONCLUSIVE.
- The lane-FAIL clause needs either C1 and C2 both FAIL, or a C3 class that free matter cannot avoid. Neither is met.

**Strongest combined statement.**
- On a fixed lattice, regular local single-band matter cannot carry a closing hypersurface-deformation algebra, not even free matter (C3). Its momentum generates central differences, not translations, so boosts do not close with it.
- Feeding the shift needs an exact SLAC band with no umklapp (C1). No finite-component analytic network produces one.
- The surviving escapes all go beyond regular, local, finite-band matter:
  - SLAC or other non-local matter;
  - infinite-band or network matter, including face-touching multi-band constructions;
  - gapless-dressed bands;
  - giving up GR's constraint algebra (a preferred foliation).

**Against the registered expectation.**
- C1 FAIL, as expected.
- C2 INCONCLUSIVE rather than FAIL; the survey was thin on Kitaev all-sectors and T > 0.
- C3 C-FAIL, as expected but for a different reason: a global Poincaré obstruction at any h, not a breakdown "beyond uniform strain".

## Campaign C4 (owner, 2026-10-11, 16:21Z to 22:21Z, 6 hours)

**Owner request:** "run the infinite-band network test - push this campaign for the next 6 hours".
- **End:** 22:21Z (18:21 EDT). Unfinished lanes are marked "not completed (stopped at end)".
- **Agents:** Opus 5.5 at xhigh.
- **Referee:** every FAIL is refereed by codex gpt-5.6-sol at xhigh before it is recorded.
- **Readings:** fixed before each run and not changed afterward.
- All settings are test settings; any axiom change is named as a price only.

**Lanes opened now, in parallel:**
- **RI:** infinite-band networks (the owner's named test).
- **RF:** preferred foliation. Escape (4) of lane RC: use the grid's own time slicing and give up GR's full constraint algebra.
- **RD:** gapless-dressed bands. Escape (3) of lane RC: can a gapless continuum carry the exact SLAC face cusp?

### Lane RI: infinite-band networks

**Question.** Lane RC's escapes need matter that is not regular local single-band matter. Can a network with unboundedly many bands per cell supply all three of the following at once?
- an exact SLAC band (C1);
- no umklapp;
- a closing global Poincaré sector (C3).

Can the partner bands be decoupled? What does it cost the axioms?

**Probes:**
- **I1, theorem.** Is exact closure (C1 + C3) equivalent to the folded-continuum ("empty-lattice") tower E_n(k) = √(m² + |k + 2πn|²)? That tower is equivalent to an exact continuous translation generator, and so to infinitely many degrees of freedom per cell.
  - Prove or refute this.
  - Treat the partner-band problem: does Theorem A force each scattering partner to be SLAC with the same β?
  - Identify the axiom cost against `MINIMAL_AXIOMS_2026-06-29.md`.
- **I2, truncation.** Use N bands per cell, for example the empty-lattice tower truncated, or a coarse cell of the Z³ qubit lattice holding N sites.
  - Measure the C3 Poincaré defect and the C1 closure residual as functions of N.
  - Measure interband scattering at the truncation edge.
  - Decide whether N-band truncation is equivalent to a finer lattice with spacing a/N.
- **I3, realization within the axioms.** Can Z³ itself supply the tower, with matter living on coarse cells of L³ qubits and the fine grid as its internal bands?
  - Compute how the C3 anomaly and the induced TT response from lattice-scale loop modes scale with L.
  - Compare with P0's bound.

**Fixed readings:**
- **PASS:** an explicit network realizable under the four axioms (Z³, qubits, a nearest-neighbour rule; networks allowed) gives exact closure of C1 + C3 for free matter, with interacting matter free of umklapp. Any further cost is stated.
- **FAIL:** exact closure is proved to require infinitely many degrees of freedom per cell (a Qubit or Lattice price), with every finite-N truncation inexact, AND the coarse-cell route (I3) leaves a lattice-scale anomaly or TT response that does not fall with L. Bounded to the stated classes.
- **INCONCLUSIVE:** otherwise.
- **Readout Q-RI:** the scaling of the defect with N or L, and the N* or L* needed for the P0-level bound.

**Supervisor expectation:**
- **I1:** exact closure ⇔ the empty-lattice tower ⇔ continuous translations; this costs Qubit/Lattice (infinite local dimension).
- **I2:** for low-energy modes the defect falls like (ka/N)^p, but at the truncation edge it stays order one.
- **I3:** the coarse-cell route is the ordinary continuum limit. Low-energy matter is fine, but lattice-scale modes in loops still carry an order-one zone-averaged anomaly, so the induced TT response does not fall with L.
- **Lane:** FAIL (bounded), with the price "infinite local dimension per cell".

### Lane RF: preferred foliation (the grid's slicing)

**Question.** Give up GR's full constraint algebra. Keep spatial diffeomorphisms, or only the lattice's own symmetries, plus a preferred time slicing, as in khronometric / Hořava–Blas–Pujolas–Sibiryakov (BPS) or Einstein-aether gravity. The C3 boost obstruction then no longer applies. Does the resulting theory, coupled to lattice matter, pass every observational bound?
- the speed of gravitational waves: GW170817, |c_T − 1| ≲ 1e-15;
- PPN α1 and α2;
- binary-pulsar radiation, including dipole radiation;
- the scalar (khronon) mode's stability and strong coupling;
- the Lorentz-violating matter couplings induced by lattice loops (the Collins et al. naturalness problem).

**Probes:**
- **F1, gravity sector.** The healthy-extension Hořava / khronometric parameter space after GW170817. Which region survives (literature, verified), and can the lattice's VS/N-type structure from lane R realize it?
- **F2, matter sector.** In the preferred-foliation theory, does a lattice-scale loop of matter percolate Lorentz violation into the low-energy matter sector, and at what size? This is the Collins–Perez–Sudarsky–Urrutia–Vucetich problem. Count the tunings needed against the bounds, and compare with P0.

**Fixed readings:**
- **PASS:** an explicit preferred-foliation theory, realizable on the lattice, that passes every listed bound with no more tunings than P0 and no unstable or strongly coupled scalar at observed scales.
- **FAIL:** every examined realization violates a listed bound or needs more tunings than P0. Bounded.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation:** GW170817 plus the PPN bounds leave a narrow khronometric window. The matter sector's Lorentz violation from lattice loops needs tunings comparable to P0 (Collins et al.). FAIL on tunings (bounded), or INCONCLUSIVE.

### Lane RD: gapless-dressed bands

**Question.** Lane RC's C1 (B2) left open whether a band dressed by a gapless continuum, a soft-emission threshold, can carry SLAC's exact face cusp, giving E² = m² + β|k|² exactly on the lifted zone.

**Probes:**
- **D1, analysis.** Treat a single band coupled to a gapless mediator: lattice photon, phonon, or Fermi sea.
  - Is the dressed dispersion exactly SLAC anywhere?
  - Can a threshold-touching cusp have exactly the SLAC form?
  - What happens to the quasiparticle residue at the face (the infrared catastrophe)?
- **D2, numerics.** Self-consistent one-loop and ladder self-energies in 1D and 2D toy models. Measure the face cusp shape and how far it deviates from SLAC.

**Fixed readings:**
- **PASS:** an explicit dressed band, under a nearest-neighbour rule with gapless mediators, that equals SLAC exactly on an open set including the face, with a finite residue.
- **FAIL:** proved or checked that the dressed face cusp differs from SLAC, or that the residue vanishes there, for the stated classes. Bounded.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation:** the soft-emission threshold gives a cusp of the wrong form, a branch-point power law set by the coupling, or a vanishing residue (the infrared catastrophe). FAIL (bounded).

### C4 second wave (16:55Z): lanes RW and RE

**Where the first wave leaves things.** All of the following are same-family results; their referees are running.
- **RI.** Exact closure needs the folded-continuum tower, which means unbounded local generators. Every finite N is a finer lattice. Coarse cells move the anomaly to a different place; they never remove it.
- **RF.** The preferred slicing leaves C3's rotation sector in place. Matter speeds then need 1–9 tunings.
- **RD.** Dressing scales a kink by Z and never creates one.

Every route therefore ends in one of two places:
- the lattice as a readout of a continuum;
- an anomaly at the lattice scale, whose effect on low-energy physics is a question of naturalness.

Two big open questions remain, and the second wave takes each one on directly.

#### Lane RW: does the refereed C3 anomaly force a graviton mass?

**Question.** C3 (refereed) shows that the constraint algebra cannot close for regular local lattice matter. "Not forbidden" is not the same as "generated". Several referees flagged a dressing loophole: an O(λ) off-shell dressing might cancel the induced vacuum TT terms. This lane settles that loophole and the consistency of the theory once the algebra is broken.

- **W1 (cancellation by dressing).** Take the free part completed by the RN L1 unitary seagull, so that μ = 0 for free matter. Add interacting onsite φ⁴. Write the most general local O(λ) dressing of T00, P and T_ij, up to a stated range and polynomial order. Then solve as a linear system: can the dressing cancel μ_E and μ_T2 at O(λ²) exactly?
  - If it can: is the dressing fixed by the matter law, or is it a free tuning?
  - Does the cancellation survive at the next order, or for a second interaction?
- **W2 (consistency of the broken-algebra theory).** Run the Dirac analysis of linearized gravity coupled to matter whose constraint algebra fails at O(κ) as C3 shows. Determine:
  - which constraints turn second class;
  - the count of propagating modes;
  - whether the extra modes are ghosts (Boulware–Deser-like), tachyons or healthy;
  - their masses in terms of the anomaly.

  Compare with Lorentz-violating massive gravity (Dubovsky; Rubakov–Tinyakov) and Hořava's extra mode.

**Fixed readings.**
- **W1:**
  - **PASS:** a dressing fixed by the matter law (no free parameter tuned) cancels μ at O(λ²) and at the next order checked.
  - **FAIL:** no dressing in the stated ansatz cancels it, or cancellation requires tuning a free parameter.
  - **INCONCLUSIVE:** otherwise.
- **W2:**
  - **PASS:** the broken theory has exactly the 2 TT modes and no ghost or tachyon to the order computed.
  - **FAIL:** an extra ghost or tachyon appears, or an extra mode with a mass set by the anomaly that violates bounds.
  - **INCONCLUSIVE:** otherwise.
- **Lane:**
  - **PASS:** W1 and W2 both PASS.
  - **FAIL:** W1 or W2 FAIL, refereed.
  - **INCONCLUSIVE:** otherwise.

**Supervisor expectation.**
- W1: the dressing can cancel μ at O(λ²) only by tuning one parameter per channel, so FAIL (a tuning).
- W2: the broken algebra brings in extra modes, either a Boulware–Deser-type ghost or the khronon. FAIL, unless the anomaly-induced mass is Planckian and the extra mode decouples, in which case INCONCLUSIVE.

#### Lane RE: emergent Lorentz invariance from strong dynamics

**Question.** Some theories make Lorentz violation irrelevant in the infrared: it decays as a power law at a strongly coupled fixed point (Bednik–Pujolàs–Sibiryakov 2013 holographic examples; Anber–Donoghue; Kostelecký–Samuel; Lorentz symmetry emerging in Dirac and Weyl materials). Could the framework's matter flow to such a point, and does the flow also cure the graviton mass?

- **E1 (theory and literature).** Which Lorentz-violating operators can become irrelevant at a strongly coupled fixed point?
  - Speed differences can.
  - Can the TT stiffness, a graviton mass, which is a relevant dimension-2 operator?
  - Can C3's algebra anomaly become irrelevant?
  - What does strong dynamics require of the lattice matter, and does it conflict with the axioms or with known physics (the Standard Model is weakly coupled)?
- **E2 (computation).** Take a lattice model that flows to a Lorentz-invariant fixed point, such as lattice QED3 or a Gross–Neveu–Yukawa model with velocity anisotropy, at large N or by RG. Compute the decay law of the speed anisotropy and of the C3-type anomaly with scale. From that, estimate the suppression available between the Planck scale and 1 TeV.

**Fixed readings.**
- **PASS:** an explicit mechanism, realizable from a nearest-neighbour rule, that drives every dimension ≤ 4 Lorentz-violating matter coefficient and the TT stiffness below bounds without tuning, with the Standard Model emerging at low energy.
- **FAIL:** for the classes examined, the TT stiffness, or some Lorentz-violating coefficient that bounds require, cannot be made irrelevant, or the needed running is too slow over the available range.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation.**
- Matter speed differences can decay as a power law at a strongly coupled fixed point. Over 15 decades that could be enough.
- The graviton mass is a relevant operator in the gravity sector, so the matter fixed point cannot make it irrelevant.
- Reading: E1 FAIL for the graviton mass, with a partial win for matter speeds. Lane INCONCLUSIVE, leaning FAIL.

### C4 first-wave results (recorded 17:10Z)

All probes were run by Opus 5.5 at xhigh (same model family). Each was refereed by codex gpt-5.6-sol at xhigh. Reports are in `agents/C4_{I1,I2,I3,F1,F2,D1,D2}_report.md`; referee reports in `agents/C4_*_referee*.md`; scripts in `scripts/C4/`.

**Lane RI (infinite-band networks): FAIL (bounded)**, for regular positive-energy free one-particle Bloch theories and finite-band periodic quadratic networks.
- **I1 — CONFIRMED WITH CORRECTIONS.**
  - Under first-moment boosts and currents, local closure forces Hess(E_α²/2) = βI on every band.
  - The periodic trace sum and determinant winding prevent closure at any finite N.
  - With an integrated positive-energy Poincaré representation, or with band-gluing assumptions, each component unfolds into a complete reciprocal-lattice tower.
  - So exact closure needs an infinite-dimensional, unbounded one-particle fibre. This holds at the one-particle level only: it does not prove an infinite microscopic site space for interacting composite qubit matter.
  - The index argument does not give a many-body contradiction.
  - Separate Poincaré sectors may decouple.
  - Nelson integrability is assumed, not proved.
- **I2 — CONFIRMED WITH CORRECTIONS.**
  - The band- and zone-averaged anomaly is exactly −β per mode for every finite-dimensional periodic C² Bloch matrix.
  - The C1 face residual summed over branches is ≥ π|β|N.
  - A uniform L³-site supercell is exactly a fine lattice with spacing a/L. In 3D that takes L³ bands, not L.
  - The 1D two-band C1 model is the folded a/2 chain.
  - Arbitrary finite networks are not shown to be fine lattices, and the universal Z_N claim is not shown.
- **I3 — CONFIRMED WITH CORRECTIONS.**
  - The anomaly leg is proved: the band-and-zone-averaged anomaly is −1 at every L, the registered quantity.
  - It is not a proof of a non-decaying physical TT mass:
    - the linear-only response falls as L⁻⁴;
    - the unitary completion cancels it;
    - one φ⁴ calculation gives a speed shift of about 2e-5·λ² through L = 16, with the L → ∞ limit not established.
  - The identity ⟨E_c − H⟩_vac = −(ρ + p_c) is confirmed for one band.
- **Lane reading.** Both FAIL legs are met in their stated scopes, so the lane is FAIL, bounded as above. Open: interacting or composite qubit matter, and decoupled separate Poincaré sectors.

**Lane RF (preferred foliation): INCONCLUSIVE.**
- **F1 — NOT CONFIRMED, so INCONCLUSIVE.**
  - Established:
    - the projectable model fails;
    - the stated single-band, fixed-generator realization fails;
    - the non-projectable lattice matches GSS;
    - cubic-only theories allow six mass invariants, which need relations beyond P0.
  - Not established:
    - non-realizability for all finite-band matter;
    - "≥ 5 P0 tunings";
    - a second anisotropy tuning at 1e-15;
    - exclusion of a separate gravitational UV scale.
- **F2 — NOT CONFIRMED, so INCONCLUSIVE.**
  - The one-loop QED numbers are confirmed: δc_f = −16.06, δc_γ = −0.671 per taste, Δ = −14.72, i.e. c_e − c_γ = −8.55e-3. That needs one counterterm tuned to about 3e-17. ξ = 1 (hypercubic) removes the splittings; ξ = 2 gives −10.26.
  - The worker's dimension-3 claim needs a correction. Proper cubic rotations do allow b₀ and (k_AF)₀, but C, T and shift symmetries do not forbid them, contrary to the worker's report. Only the parity of the chosen action does.
  - Not a FAIL: realization C is open, P0's total count is unknown, and the Z⁴-matter / RF-gravity route is open.

**Lane RD (gapless-dressed bands): FAIL (bounded).**
- **D1 — CONFIRMED WITH CORRECTIONS.**
  - Lemma K holds for a single scalar band with a finite-range bare dispersion and a stable, uniformly subsonic rainbow/SCBA self-energy satisfying UI: the face jump obeys J_E = Z·J_ε0. So no SLAC cusp at finite residue.
  - The marginal case and the gapped-touch case have Z = 0 and non-SLAC singularities.
  - Exact SLAC forces a non-local bare 1/r² tail of size 1/Z.
  - Open: general Herglotz self-energies, the all-orders 1D Fermi sea, sonic vertices, and two-band crossings.
- **D2 — CONFIRMED WITH CORRECTIONS.**
  - In the computed classes and orders, no finite-residue SLAC face appears.
  - The Cherenkov branch exchange has an exact cusp of non-SLAC form, with Z, ℓ ∝ g⁴.
  - Fermi faces have nonzero linewidth.

### C4 third wave (17:15Z): lanes RM, RK2, RF3

#### Lane RM: can composites and multi-particle continua evade the sum rule?

**Question.** RI's theorems (I1, I2) cover finite-dimensional one-particle Bloch matrices. Interacting qubit matter differs in two ways:
- its composites are extended objects;
- at fixed total momentum K, its multi-particle sector has infinitely many states (a continuum of relative motion).

Do composites' centre-of-mass bands and multi-particle continua obey the same periodic trace sum rule, which forces a band- and zone-averaged anomaly of −β? Or can an infinite internal space supply the tower, as I1 says only infinitely many bands can? This is the open item left by the I1 referee.

**Probe M1.**
- Exact two-body and few-body calculations on Z^d for bound states and their continua, giving the C3 boost anomaly of the composite as a function of binding and size.
- Whether the full two-particle sector can close C3 exactly.
- Whether a composite's centre-of-mass dispersion can approach a complete tower.
- Whether the GNVW index obstructs many-body realizations.

**Fixed readings.**
- **PASS:** an explicit interacting law, nearest-neighbour on qubits, whose physical low-energy particles (composites) close C1 + C3 exactly.
- **FAIL:** proved or checked that composites' bands obey the sum rule with averaged anomaly −β, or an equivalent obstruction, for the stated classes. Bounded.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation.**
- A composite's centre-of-mass band is periodic in K and finite-dimensional per internal level, so the sum rule applies to each bound level.
- The scattering continuum is not one particle; its boost anomaly averages the constituents'.
- So FAIL (bounded) is expected. The index question is likely INCONCLUSIVE.

#### Lane RK2: lane K re-registered in an implementable form (the hypercubic Z⁴ block)

**Question.** The lane K referee asked for exactly this: an interacting W(B4)-covariant stress on Z⁴ (time as a grid direction with the same step as space, ξ = 1), and whether the 5 non-gauge-invariant forms vanish. F2 shows matter speeds are protected at ξ = 1. What exactly does P0 cost on Z⁴? This needs two counts:
- the TT and graviton-sector counterterm count;
- the speed count.

Separately, does C3's continuous-time constraint-algebra obstruction have a discrete-time analogue on Z⁴?

**Probes.**
- **K1, the count.** Enumerate the W(B4)-invariant quadratic forms for a symmetric tensor h_μν on Z⁴: mass terms at O(q⁰), and two-derivative forms at O(q²). Compute the one-loop induced coefficients from interacting matter, staggered fermions plus a U(1) gauge field, on Z⁴ with ξ = 1. From these, derive the number of independent tunings P0 needs on Z⁴: masses plus non-gauge-invariant kinetic forms.
- **K2, discrete-time algebra.** On Z⁴, the hypersurface-deformation algebra is replaced by lattice discrete-time evolution. Is there a discrete analogue of C3's global-Poincaré obstruction? Hypercubic symmetry contains no boosts, only discrete 90° rotations in time–space planes, which are Euclidean. Determine:
  - what protects one light cone;
  - whether a graviton's gauge symmetry, linearized diffeomorphisms on Z⁴, can be exact for the free Euclidean lattice action (Rocek–Williams style);
  - which reflection-positivity issues arise (K7a: leapfrog unstable at the hypercubic tick).

**Fixed readings.**
- **K1:** record the count, N_tune(Z⁴), as a number. Lane K's question ("two shear tunings alone?") is answered YES if N_tune = 2 and NO if N_tune > 2.
- **K2:**
  - **PASS:** an exact linearized lattice diffeomorphism gauge symmetry for free matter plus graviton on Z⁴, with reflection positivity (a positive transfer matrix) at ξ = 1.
  - **FAIL:** proved impossible in the stated class.
  - **INCONCLUSIVE:** otherwise.

**Supervisor expectation.**
- **K1:** N_tune > 2 at the O(q²) level. The 5 non-gauge-invariant W(B4) forms are generated by loops.
- **K2:** exact linearized lattice diffeomorphisms hold for the free Euclidean graviton on a flat lattice (Rocek–Williams, with Bahr–Dittrich's flat-background result). Matter coupling breaks them, by the discrete analogue of the Leibniz failure. Reflection positivity fails at ξ = 1 (K7a). So INCONCLUSIVE or FAIL.

#### Lane RF3: Z⁴ matter with foliated gravity at a separate UV scale (the F2 referee's open route)

**Question.** Matter on Z⁴ at ξ = 1 has protected speeds. Can gravity carry its own preferred foliation at a separate, lower UV scale M_*? Check:
- the khronometric window;
- Pospelov–Shang's bound M_* < 1.5e10 GeV;
- whether the hierarchy between M_* and the matter lattice scale can arise without a tuning;
- whether the setup is consistent with a single Z³ (or Z⁴) grid under the axioms, i.e. one lattice for both sectors.

**Probe F3.** Analysis and literature.

**Fixed readings.**
- **PASS:** a realization on one grid, under the axioms, that passes every RF bound with no more tunings than P0.
- **FAIL:** every examined realization violates a bound, or needs a hierarchy or tuning beyond P0.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation.** A separate M_* needs the gravity sector to see a coarser effective lattice than matter, roughly 1e9 times coarser. On one grid that is a hierarchy, i.e. a tuning, so FAIL or INCONCLUSIVE.

### Lane RE results (recorded 17:25Z): FAIL (bounded)

E1 and E2 are both CONFIRMED WITH CORRECTIONS by codex gpt-5.6-sol at xhigh. Reports are `agents/C4_E{1,2}_*`.

**E1.** Consider a unitary 4D matter flow to a Lorentz-invariant fixed point, with:
- a unique stress tensor;
- no allowed vector deformation with 3 ≤ Δ ≤ 4;
- a spectator graviton coupled only through irrelevant gravity.

Then:
- The common matter speed is redundant, and the relative speeds of interacting matter sectors are irrelevant.
- Matter RG does not make the local TT vacuum response irrelevant.
- Matter RG does not pull the graviton speed onto the matter cone.
- Without a separate gravitational Ward identity, sum rule or UV matching, the P0 TT problem remains, and matching the graviton and matter speeds is an independent cost.
- Standard Model logarithmic running is far too slow.

This is a FAIL bounded to that class, not a no-go against every strong-dynamics or emergent-gravity construction.

**E2.**
- For F2's realization, the verified one-loop flow only takes the split from 8.55e-3 at the cutoff to 7.34e-3 at 1.4 PeV. Photon survival needs ≤ 2.66e-19, so the flow misses by 2.76e16. This is FIXED reading "running too slow": FAIL (bounded).
- Corrections:
  - the SM factor 0.911 depends on the norm used;
  - S ~ 1e-2 comes from an elementary-species scan, not a universal bound;
  - the graviton claims are conditional estimates.

### C4 fourth wave (17:35Z): lanes RV and RL

#### Lane RV: W1's open route, a dressed momentum that annihilates the vacuum

**Question.** The W1 worker named one principled way the dressing could be fixed rather than tuned. Choose the interacting dressed momentum P_λ so that it annihilates the interacting vacuum. Its quartic correction is V·Σf/Σω, which is analytic because Σω ≥ 4m. The metric then enters through the unitary flow generated by K built from P_λ.

**Probe V1.** Construct P_λ to O(λ), and to O(λ²) where feasible. Compute its strain flow, the induced μ_E and μ_T2 at O(λ²), and whether they vanish with no free parameter. Check locality: is the 0↔4 sector exponentially local? Determine where the 2↔2 obstruction (power-law tails, RN L2) enters, and at what order.

**Fixed readings:**
- **PASS:** μ_E = μ_T2 = 0 at O(λ²), with no free parameter, and the flow exponentially local.
- **FAIL:** μ ≠ 0, or the construction needs a free parameter, or it is non-local (power-law) already at the order where μ is computed.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation.** Annihilating the vacuum fixes the 0↔4 part, and μ at O(λ²) comes from vacuum fluctuations. So μ may vanish at O(λ²); this would be a vacuum-level version of the seagull. The 2↔2 obstruction enters at O(λ³), or in excited states, and there it is non-local. Reading: INCONCLUSIVE, leaning to a partial PASS at O(λ²) that does not survive the next order.

#### Lane RL: the event route again, with weighted and multi-hop link readouts (G-L's open item)

**Why now.** Every lattice lane in C4 ends at the boost obstruction (C3, I1/I2, M1). The events substrate, a Poisson sprinkling, is Lorentz invariant in law, so C3 does not apply to it. Its refereed walls:
- G-L: the unweighted one-hop link mean lenses as (νΔ)^{-1/2}, not √Δ. Weighted and multi-hop readouts were left open.
- G-B: INCONCLUSIVE.

The price list P1–P4 is unchanged.

**Probe L1.** On a curved Poisson sprinkling (weak-field lens, as in G-L), test readouts that reproduce Van Vleck focusing, √Δ, in the mean:
- weighted links: weights from interval volumes or local density;
- multi-hop sums: the Johnston path sum including longer chains;
- the BD d'Alembertian inverse.

Is there a readout whose mean is link/GR → 1, up to corrections O(ℓ²/r²), with noise bounded as in E1′-b?

**Fixed readings:**
- **PASS:** an explicit, order-only readout with mean → √Δ magnification (density-independent mismatch → 0) and noise bounded at physical parameters.
- **FAIL:** every tested readout class has a density-independent O(1) mismatch, or the noise is unbounded. Bounded to the classes tested.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation.** The multi-hop Johnston sum (the full massless propagator) and the BD inverse reproduce the continuum retarded Green function in the mean. In curved spacetime that Green function carries √Δ, so these should PASS in the mean. The unweighted one-hop case fails because one hop lacks the transport factor. Noise for multi-hop sums at physical parameters is the open risk. Reading: PASS in the mean, INCONCLUSIVE on noise.

### Lane RF3 result (recorded 17:41Z): INCONCLUSIVE

F3 was refereed by codex sol: NOT CONFIRMED, so the result is INCONCLUSIVE. Files: `agents/C4_F3_*`.

**What the referee confirmed.** On one grid, an explicit Pospelov–Shang-type Hořava crossover must soften every graviton component that contributes. That brings in large dimensionless separations:
- M_* of a few 1e9 GeV;
- L of a few 1e9;
- a TT k⁶ coefficient of 1e38–1e39.

An explicitly coarse graviton cell writes L into the law. These are legitimate hierarchies beyond P0, though not automatically precision tunings. Minimal, weak hidden-sector loops cannot bend a Planck-stiff graviton without an enormous central charge.

**What stays open.**
- No all-orders result excludes other dimensional-transmutation mechanisms.
- A dynamical khronon remains an RF preferred-foliation theory. This corrects the worker's R4 classification.

The hierarchy is established for the explicit R1 and R2 subcases, not for every one-grid realization.

### Lane RW, W2 (recorded 17:41Z): INCONCLUSIVE

Refereed by codex sol: NOT CONFIRMED, so the result is INCONCLUSIVE. Files: `agents/C4_W2_*`.

**What the referee confirmed.** C3 leaves a nonzero Killing-sector obstruction in the 09-14 / L1 single-band construction. Suppose that obstruction is replaced by a homogeneous background coefficient and every gauge-invariant addition is set to zero. Then the minimal λ = 1 Wess–Zumino theory has one extra scalar:
- dispersion ω² = a k²/(3a − 2M_P²k²);
- a ghost for the physical sign a < 0;
- the α term alone does not cure it.

**Why it is not a FAIL.** The anomaly does not uniquely determine that action or its spectrum.

#### Lane RW follow-up W3 (17:43Z): is there a ghost-free completion?

**Question.** The W2 referee found that the anomaly does not uniquely determine the Stückelberg/Wess–Zumino action. So the question becomes: does the most general quadratic action, consistent with the C3 anomaly plus every gauge-invariant addition (λ ≠ 1, α, β, higher-derivative terms), allow a choice that has all of the following?
- only the 2 TT modes propagating, or the extra scalar healthy (no ghost, no tachyon);
- consistency with the khronometric window (F1);
- no tuning beyond P0.

**Fixed readings.**
- **PASS:** an explicit region of parameter space that is ghost-free and tachyon-free, inside the observational window, reached without tuning beyond P0.
- **FAIL:** every completion within the stated class (quadratic, up to stated derivative order) has a ghost or tachyon, or needs tuning beyond P0.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation.** A healthy region exists at λ ≠ 1, as in healthy Hořava, where the khronon is healthy for an appropriate sign of (λ − 1). It requires α and λ − 1 in the khronometric window. The question is whether the anomaly forces a sign incompatible with that region. Reading: INCONCLUSIVE, leaning PASS-for-health but FAIL-for-tuning, since the khronometric tunings (F1) come on top of P0.

### C4 results recorded 18:15Z (W1, M1, K1, K2, V1)

All five were refereed by codex gpt-5.6-sol at xhigh. Files: `agents/C4_{W1,M1,K1,K2,V1}_*`.

**Lane RW, W1: FAIL bounded to the h-linear reflection-even quartic dressing ansatz (CONFIRMED WITH CORRECTIONS). The unrestricted question is INCONCLUSIVE.**
- Inside that ansatz the E and T2 cancellation loci are codimension-1 spheres, so cancelling requires tuning.
- Corrections:
  - Quadratic dressings were omitted.
  - The reported dimensions need reflection symmetry.
  - The "50×" figure is not generic.
  - v_R is a determined completion built from the state, not a tuning.
  - Strained normal ordering cancels the bond O(λ′) term with fixed seagulls.
- The P₄ route was not computed.

**Lane RV, V1: INCONCLUSIVE (NOT CONFIRMED as PASS).**
- Established:
  - For massive onsite φ⁴, the vacuum-annihilating dressing fixes an exponentially quasi-local 0↔4 kernel.
  - The 1↔3 block is gapped.
  - The 2↔2 block stays obstructed.
  - Given Rule R, the dressed vertex and the seagull cancel exactly at O(λ²), so μ_E = μ_T2 = 0 with no tunable coefficient.
- Why this is not a PASS:
  - R is a vacuum-referenced coupling convention. It is not derived and not basis-free.
  - It leaves an O(λε) scattering Ward-identity defect, a physical stress defect. That defect conflicts with universal coupling under the usual massless spin-2 assumptions.
  - The "all orders" claim needs an exact W that was never constructed.
- **Reading:** a conditional mechanism that works for the vacuum only, and the most promising lead of C4.

**Lane RM, M1: FAIL (bounded) (CONFIRMED WITH CORRECTIONS).**
- Assume a first-moment boost and strong conservation of the energy current. Then every globally isolated positive-energy composite band has current ∇(E²/2). C3 closure would require Hess = βI, but periodicity forces the averaged anomaly to be −βI. This holds whatever the binding, size, fibre dimension or Chern twist.
- For finite-range, number-conserving models over an empty vacuum, every finite-N sector is excluded by the bounded-sector theorem.
- Not excluded:
  - non-first-moment generators;
  - non-number-conserving embedded sectors in d ≥ 2;
  - irrational centres;
  - massless sectors;
  - unbounded continuum sectors.

**Lane RK2, K1: N_tune(Z⁴) = 11 = 3 + 8 (CONFIRMED WITH CORRECTIONS). Lane K's question is answered NO.**
- This is an exact operator-codimension count under the registered definition, after a separate tuning for the cosmological tadpole.
- It is corroborated by a one-loop example in which every coefficient is nonzero.
- It is not a universal theorem for every W(B4)-covariant stress.
- 5 is the rank of the Euclidean TT restriction. It is not a proved physical floor for two helicities.

**Lane RK2, K2: INCONCLUSIVE (CONFIRMED WITH CORRECTIONS).**
- The free lattice Fierz–Pauli action has an exact linearized gauge identity and 10 affine Killing parameters.
- The scalar and the naive/staggered fermion have local symmetric stresses, giving exact coupled invariance through O(κ).
- Their Killing transformations provably fail e(4) closure at O(κ²), and a seagull cannot repair it.
- The general no-go needs hypotheses that are not established for every reflection-positive theory: compact smooth shells, a Wick-real translation symbol, and a complete boost flow.
- The free scalar and reduced TT graviton transfer matrices are positive; 9.899 is a leapfrog instability only.
- Coupled reflection positivity is unproved.

### C4 fifth wave (18:17Z): following up V1's conditional vacuum mechanism

V1 (refereed INCONCLUSIVE) is the campaign's strongest lead. The referee raised three objections:
- (i) Rule R is a vacuum-referenced convention: it is not basis-free and not derived.
- (ii) It leaves an O(λε) scattering Ward-identity defect, which conflicts with universal coupling.
- (iii) "All orders" needs an exact W that has not been constructed.

#### Lane RV2: can R be made canonical, and does the defect matter?

**Probe V2.**
- (a) Look for a basis-free, canonical form of R, one that is derived rather than chosen. Candidates:
  - Kato adiabatic transport of the interacting vacuum;
  - Gell-Mann–Low dressing;
  - a variational principle, such as minimal norm of the explicit-position part;
  - the requirement that the local coupling be a unitary flow of H within the space of local Hamiltonians.

  Show whether any of these selects R uniquely and agrees with V1.
- (b) Size the scattering-sector Ward defect and its consequences:
  - universality, i.e. whether a composite's binding energy gravitates with the same G, giving an Eötvös-type violation as a function of (ka);
  - whether the defect feeds back into the vacuum TT response at higher order (V1 says it never does under R; check);
  - whether, given (ii), the defect is phenomenologically negligible at physical energies: relative defect O((ka)²) ~ (E/M_Pl)².

**Fixed readings.**
- **PASS:**
  - a canonical (basis-free, derived) R that reproduces V1's μ = 0; and
  - a scattering defect whose effect on universality is below observational bounds at physical energies, with no feedback into μ at the order checked.
- **FAIL:** either of these:
  - no candidate principle selects R, and every candidate gives μ ≠ 0;
  - the defect feeds back into μ at natural size, or violates universality above bounds.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation.**
- Kato transport or Gell-Mann–Low is likely to select V1's sector split up to terms that do not move μ, so R would be canonical (PASS on (a), probable).
- The universality defect is about (E/M_Pl)², which is negligible.
- Feedback into μ is possible at O(λ³) through loops of lattice-scale scattering states. This is the real risk.
- **Reading:** INCONCLUSIVE leaning PASS, with the O(λ³) feedback as the decider.

#### Lane RV3: the V1 mechanism for the framework's own matter

**Probe V3.** Extend V1 to staggered fermions on Z³:
- with a contact interaction (S1's classes);
- or with lattice QED at O(e²), where the photon brings a gapless continuum.

Does the vacuum-annihilating dressing exist and stay local? For massless photons the gap Σω ≥ 4m fails and kernels become power-law, so is it local at all? Does the O(λ²)/O(e²) vacuum TT cancellation work, given that rule R is adapted to fermions?

**Fixed readings.**
- **PASS:** μ = 0 at the first nontrivial order with a local or exponentially quasi-local dressing, for the stated fermion class.
- **FAIL:** no local dressing exists (e.g. power-law kernels at the order needed), or μ ≠ 0.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation.**
- Massive staggered fermions with contact interactions: works as for φ⁴, so PASS (conditional on R).
- Massless photon: the 0↔4 analogue, e⁺e⁻γ production from the vacuum, has a denominator ≥ 2m, so it stays gapped. But photon-only channels such as light-by-light are gapless, so power-law kernels appear at O(e⁴). At O(e²) the mechanism may survive.
- **Reading:** PASS at O(e²) for massive fermions with photons, conditional on R.

### C4 results recorded 18:47Z (RL1, W3)

**Lane RL, RL1: INCONCLUSIVE, leaning FAIL.** The codex sol referee did NOT CONFIRM the bounded FAIL. Files are in `agents/C4_RL1_*`.

What the referee confirmed, for regular pre-caustic scalar propagation:
- The massless 4D Johnston sum is exactly the one-hop link kernel.
- Extra hops add tails, but no direct-cone delta.
- Normalizable one-hop kernels that depend only on ρV keep the wrong ν^{-1/2} coefficient.
- The Palm-kernel mean-inverse identity is exact.
- The 4D BD mean has an unstable pair at 0.375598 ± 5.052239i.
- No scalar density repairs a thin, net-focusing Ricci lens at first order.

Still open:
- Three distinct L = 6 operators remain stable to the scanned resolution.
- Their curved-space mean and their physical fixed-source variance are unresolved.

**Lane RW, W3: INCONCLUSIVE.** The referee CONFIRMED WITH CORRECTIONS, with bounded FAILs for two subclasses: the khronometric one and the exactly repaired window-side one. Files are in `agents/C4_W3_*`. Conditional on the homogeneous continuum anomaly representative:
- The anomaly is represented by a metric-nonlocal F. Its coefficient is fixed only modulo invariant additions.
- In the pure khronometric completion, every nonzero-momentum scalar is pathological for physical a < 0.
- The unique repair m₄ = −a/2 restores the lapse. It still leaves the λ > 1 branch unstable below k*, and it costs one exact extra relation.
- General quadratic actions that break spatial diffeomorphisms give healthy full spectra in a numerical search. On a dense grid there are 9 scalar-sector candidates and 4 candidates across all sectors. All are far from GR.
- No region compatible with the observational window has been exhibited, and no no-go theorem excludes one.

### C4 sixth wave (18:48Z): lane RL2, the stable layer operators of the event route

**Question.** The RL1 referee left three distinct stable L = 6 layer operators. Their curved-space mean and their physical fixed-source variance are unresolved. For these operators:
- Does the per-sprinkling inverse reproduce Van Vleck √Δ focusing in the mean on the G-L lens?
- Is the variance for a fixed source at physical ε (smearing) bounded?

**Probe RL2.** Compute both, using the RL1 scripts and the G-L lens.

**Fixed readings:**
- **PASS:** at least one stable operator has mean magnification → √Δ, with a density-independent mismatch → 0, and noise bounded at physical parameters (ℓ_k ≤ 1e-19 m over 1 Gpc).
- **FAIL:** each of the three operators fails at least one of the following: its mean has an O(1) mismatch, or its noise is unbounded at physical parameters.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation:**
- The mean passes, because a local stable operator inverts to the curved Green function.
- The noise fails at ℓ_k = 1e-19 m, consistent with the renewal growth of E1 and RL1.
- So FAIL on noise, or INCONCLUSIVE if the small-ε variance cannot be controlled.

### C4 results recorded 18:57Z (V2, V3): a correction to earlier records

**Lane RV3, V3. CONFIRMED WITH CORRECTIONS (codex sol): (a) FAIL, (b) FAIL (bounded).** Files: `agents/C4_V3_*`.

**Central result (free matter).** Take the uniform-strain coupling as a translation-covariant, finite-range local operator: the bulk commutators of the first-moment flow, periodized onto the torus. Then:
- the thermodynamic vacuum energy carries the Jacobian of the flow;
- the T2 flow is divergence-free, so μ_T2 = 0;
- the E flow gives μ_E = +1.97038864e-3 for the RN-L1 scalar at m = 1, and the corresponding negative value for staggered fermions.

**Why the earlier argument missed this.**
- Exact unitary isospectrality holds only if the boundary/seam part of the ill-defined torus first moment is kept.
- The f-sum substitution keeps that extensive boundary piece without saying so, so it never actually evaluated the local seagull.
- For a fixed, local, translation-covariant probe, the bulk-local construction is the physical one. The formal torus unitary has a privileged seam, so it is not a uniform local strain.
- The axioms do not uniquely fix this nonlinear coupling; that choice belongs to downstream structure.

**What the surviving response is.** It is an E_g shear coefficient, not a cosmological constant. Removing it requires one of:
- an added E_g counterterm;
- a selected momentum symbol (a tuning);
- the vacuum-referenced subtraction R₀, which holds by definition.

**Verdicts.**
- **(a) Contact fermions: FAIL.** The dressing is exponentially quasi-local, and the interaction pieces cancel under R. But the total has μ_E ≠ 0 at O(λ⁰).
- **(b) QED: FAIL, bounded** to the analytic Coulomb-gauge A,E ansatz. The photon-leg tails are non-analytic, and for m < √3 there is no exponential repair.

**CORRECTION to earlier records.** These were recorded with an exact uniform-strain cancellation; the correction is dated here, not edited into them:
- **RN L1 referee:** "the unitary seagull cancels the uniform-strain TT response exactly." True only for T2, or with the boundary/seam retained. False in E for the local coupling.
- **C4 I3:** "μ = 0 with the seagull at every L." The same correction applies.
- **C4 V1:** "W|0_h⟩ exact eigenstate". Holds only with R₀.

So free regular local lattice matter already generates one of P0's two shear numbers (E_g). T_2g stays protected (Liouville).

**Lane RV2, V2. NOT CONFIRMED (codex sol). Result: INCONCLUSIVE, leaning FAIL.** Files: `agents/C4_V2_*`.
- The referee sides with V3: V2's "μ ≡ 0" needs R₀.
- Survives:
  - the narrow O(λ²) cancellation between the Kato interaction and the seagull;
  - the conditional O(λ³) formula;
  - the defect identity ΔP = 2 sin(Q/2)(cos κ − cos κ′), with (ka)² scaling.
- Kato does not fix the split or R₀.
- Gell-Mann–Low is non-local.
- The η figure is not an Eötvös observable, because the lapse coupling was not tested.
- PASS is excluded. Under the literal rubric the result is INCONCLUSIVE, leaning FAIL.

**Lane RV (V1 to V3) overall.** The vacuum-annihilating dressing cancels the interaction part of the TT response at O(λ²), with no tunable number. But even free matter's local coupling leaves the E_g shear mass. So the mechanism works for interactions, not for the free Jacobian, and the lead closes in this form.

**Supervisor's own thread (same family; written before reading the referees).** The supervisor's reasoning agreed with V3:
- A uniform-strain flow along the lattice momentum symbol is not translation-invariant.
- Forcing it into translation-invariant local form reweights the zero-point sum by the Jacobian.
- This is C3's Hessian anomaly appearing in the vacuum.

### C4 seventh wave (19:00Z): lane RP, species sum rules for the E_g shear mass

**Question.** V3 (refereed) found that free local matter generates an E_g shear mass:
- scalar: +1.97e-3 at m = 1;
- staggered fermion: negative, equal to −½ × scalar(2m).

I3 found that Bose–Fermi pairing cancels the vacuum quantities exactly, for any dispersion.

So can the matter content cancel μ_E species by species? This would be a "Pauli sum rule" for the shear mass, the analogue of Pauli's vacuum-energy sum rules. Expand each species' μ_E(m) in powers of (ma). Cancelling to the P0 level (~1e-99 per cell) at physical masses (ma ≲ 1e-17) then needs a sum rule at each order up to some n. What does each order demand of the content: degree-of-freedom counts, Σm², Σm⁴log m, and so on? Can Standard-Model-like content satisfy the leading rule? What do interactions do?

**Probe P1.**
- Compute μ_E(m) and the expansion coefficients for:
  - a real scalar;
  - a staggered fermion;
  - a U(1) gauge field (K1 found the photon tadpole is zero by Weyl invariance; what is its μ_E?);
  - optionally a naive fermion.
- Derive the sum rules order by order.
- Count the resulting conditions against P0.
- Estimate the one-loop interaction corrections (g²/16π²) that break the cancellation.

**Fixed readings:**
- **PASS:** the leading-order rule is satisfiable by a natural degree-of-freedom count, all higher-order rules up to the P0 level hold without mass relations, and interactions preserve them (a symmetry reason).
- **FAIL:** the sum rules need mass relations (tunings) or interaction-stable cancellation is impossible without a symmetry the lattice lacks. Bounded to the species examined.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation:**
- The leading rule is a degree-of-freedom count (bosons against fermions, weighted). That is satisfiable, but not by the SM as it stands.
- The (ma)² and (ma)⁴ rules need mass relations, as Pauli's sum rules do.
- Interactions break the cancellation at g²/16π², because lattice SUSY is obstructed (Kato–Sakamoto–So).
- FAIL (bounded). This turns P0's E_g tuning into a Pauli-type sum-rule problem: the same naturalness problem as the cosmological constant.

### C4 eighth wave (19:18Z): lane RB, boost generators that are not first moments

**Question.** Every obstruction in C3, I1/I2, M1 and K2 assumes the boost generator is the first moment of a local energy density, K = Σ x·h(x) + improvements. The M1 and C3 referees both left non-first-moment generators open. Could some other exact symmetry generator close the global algebra with the lattice H and P? Candidates:
- generators with higher moments, K = Σ (x·h + x²·q + …);
- generators that are not local densities but are still quasi-local;
- deformed (DSR-like) boosts whose algebra closes non-linearly onto H and P.

For each: does it close with H and P, and would gravity's hypersurface-deformation algebra accept it? In GR, the generator must arise from the lapse smearing N = x, so it has to be a first moment. Is that requirement forced?

**Probe B1.**
- For free lattice matter (one band, finite bands), classify the exact symmetry generators of H that act like boosts at low energy.
- Check whether any closes an algebra with H and P (exactly, or deformed).
- Check whether such a generator can arise from a local constraint smearing.
- Comparator: I1's umbilic argument against deformed boosts in d = 3.

**Fixed readings.**
- **PASS:** an explicit exact generator that, together with H, P and the rotations, closes an algebra reducing to Poincaré in the infrared, and that arises from a local constraint structure gravity can use.
- **FAIL:** for the stated classes, no such generator exists (proved), or none can arise from a local smearing.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation.**
- Deformed boosts can close for a single band in 1D. Doubly special relativity is known to give lattice-like dispersions with deformed Lorentz symmetry: E(k) with a maximal momentum.
- In d ≥ 2 with cubic symmetry, the umbilic obstruction (I1) kills smooth deformations.
- Gravity's constraint algebra needs first moments, from the lapse smearing.
- Expected reading: FAIL (bounded), with 1D DSR as a curiosity.

### C4 ninth wave (19:20Z): lane RL3, the noise exponent theorem for the event route

**Question.** RL2 (worker, unrefereed; referee running) finds two things:
- The mean of the stable 6-layer inverses gives GR's √Δ lensing.
- The noise grows like exp(k√ε·τ/ℓ_k) in proper time τ ≈ √(2Ds). At the locality bar this misses by only 0.8–1.9 decades in ℓ_k.

A PASS would need the true small-ε rate exponent to be α ≥ 0.54 rather than ½. Only a theorem can settle this. Extrapolating across 63 decades is forbidden (TESTS.md:5–9).

**Probe RL3.** Prove a small-ε asymptotic result for the variance growth rate of the inverse of a stable layer operator on a Poisson sprinkling:
- a lower bound or an upper bound, or the exact exponent, from the Wiener–Itô chaos expansion keeping both node and interior insertion amplitudes;
- alternatively, an exact renewal/ladder argument with controlled error.

Determine α, and the constant where possible.

**Fixed readings.**
- **PASS:** a proof that the rate exponent is > ½ (e.g. α ≥ 0.54), or that the constant is small enough, so that ℓ_k ≤ 1e-19 m bounds the noise over 1 Gpc for a 10 km source.
- **FAIL:** a proof that the rate is at least c√ε/ℓ_k with c large enough that the bar fails.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation.** The ladder (renewal) structure gives rate ∝ √(Σ w² ε) by the same argument as E1's S1 (where A² ∝ εT² with a convergent coefficient). The exponent is ½ exactly, with constant ≈ ladder, so a provable lower bound gives FAIL by about 1 decade. Reading: FAIL if the lower bound closes, otherwise INCONCLUSIVE.

### C4 results recorded 19:41Z (P1, RL2)

**Lane RP, P1: FAIL** (bounded). Codex sol: CONFIRMED WITH CORRECTIONS. Files: `agents/C4_P1_*`.

The shear responses in the RN-L1 bulk-flow coupling:
- free KG scalar: F(M);
- staggered fermion: −½F(2m);
- naive taste-singlet fermion: −2F(2m).

Key values: F(1) = 1.970388642e-3, and F(M) = c₀ + c₂M² + c₄M⁴ + M⁶[(384π²)⁻¹ln M + c₆] + ….

Consequences:
- Cancelling to the P0 level at physical masses needs the count rule R0 plus the mass relations R2, R4 and R6.
- The SM proxy misses R0 by +22F(0).
- Exactly matched spectra would cancel to all orders. Generic interactions are expected to spoil the cancellation, but this was not computed.
- The renormalized O(λ) scalar residual vanishes.
- Photon option B gives exactly 0.71172125. Photon option A and the O(g²) coefficient are argued, not computed.
- The FAIL is bounded to the analyzed free dispersions and couplings. It is not a universal lattice-SUSY or interaction no-go.

**Lane RL2: INCONCLUSIVE, leaning FAIL.** Codex sol: CONFIRMED WITH CORRECTIONS. The scoped positive result on the mean stays on record. Files: `agents/C4_RL2_*`.
- **Mean (positive).** For all three stable six-layer operators, GR-like √Δ focusing at leading needle order is strongly supported. The support is the exact plane-wave Volterra reduction plus the Van Vleck cancellation, with independently checked normalizations and rerun numerics.
- **Variance (unresolved).** The accessible data favor exponential growth at rates close to the ladder estimate. Neither the physical small-ε exponent nor the extended-source proper-time bound is proved.

**Lane RW, lane-level line (supervisor, recording the fixed lane clause).** The fixed clause gives FAIL if W1 or W2 FAILs, refereed.
- W1 is a FAIL bounded to its h-linear reflection-even quartic dressing ansatz.
- W2 is INCONCLUSIVE.
- W3 is INCONCLUSIVE, with FAILs in two subclasses.
- **Reading:** lane RW is FAIL, bounded to W1's ansatz. The unrestricted question ("does the anomaly force a graviton mass, and is the broken theory healthy?") is INCONCLUSIVE.

### C4 results recorded 20:23Z (B1, RL3, RL3b)

All three were refereed by codex sol.

**Lane RB, B1: FAIL (bounded), CONFIRMED WITH CORRECTIONS.** Files: `agents/C4_B1_*`. Scope: free matter on a smooth isolated simple Bloch band, in d = 2 and 3.
- **Smearing forces a first moment.** A regular affine-lapse Hamiltonian smearing necessarily generates a first-moment boost.
- **No (H, P)-closure.** If u = ω²/2 is cubic-invariant and Morse, [K_a, P_b] cannot close as a single-valued function of (H, P) alone. The obstruction is cubic Hessian invariance plus Morse theory.
- **No undeformed Poincaré closure.** Exact undeformed positive-β closure is impossible on any bounded K-invariant sector whose commutators exponentiate.
- **No global undeformed Lorentz action.** A global smooth undeformed Lorentz action with the usual fixed rest point cannot act on the whole Brillouin torus.

Left open:
- patchwise or singular DSR;
- fully deformed non-first-moment algebras with extra constraints;
- non-Morse or touching bands;
- interacting matter;
- unbounded sectors.

**Lane RL3: INCONCLUSIVE, leaning FAIL.**
- **RL3 (worker reported FAIL):** NOT CONFIRMED.
  - The exact Poisson-chaos variance expansion is sound: Var_ε = Σ_k ε^k a_k, with fixed a_k ≥ 0. So no extrapolation in ε is needed at that stage.
  - Candidate constants: c_low = 0.717–1.521 and c* = 2.732–3.253.
  - Not proved:
    - the uniform comparison across many insertions;
    - the step from the capped renewal pole to a pointwise lower bound;
    - a nonzero end factor for the extended source.
- **RL3b (independent method): CONFIRMED WITH CORRECTIONS, INCONCLUSIVE leaning FAIL.**
  - The Palm second moment has an exact formal renewal equation.
  - Its shared-node part has small-ε rate k_h√ε, with k_h = 2.7348, 2.8353, 3.2539 confirmed independently.
  - A displaced pair loses the z⁻² enhancement, but the bound is not uniform.
  - The exclusion of 281–334 e-folds is a compelling conditional consequence, not yet a proved FAIL.
- **The two methods agree:** exponent ½, node-ladder constant about 2.7–3.3, and a miss at the 1e-19 m bar of about 0.8 decades in ℓ_k. The open items are named lemmas: a uniform irreducible-kernel bound, and pole-to-source transfer.

### Wrap-up stance (supervisor, 20:25Z)

No new probes are launched after this point. Every probe has returned and every referee verdict is recorded.

### C4 tenth wave (20:27Z). Correction to the stance above.

The line "No new probes after this point" was premature: there are still about 90 minutes before the 21:55Z wrap-up. Two closing probes are launched on the named open lemmas. Each must return by 21:50Z.

#### Lane RL4: close RL3's two lemmas

**Probe RL4.** Prove the two missing lemmas:
- **Lemma U:** a uniform bound on the irreducible kernel. RL3b needs only |Λ_c| ≤ 7.9e4 at z₀ = 0.0098√ε; power counting gives about 1e-59.
- **Lemma T:** transfer of the shared-node pole to the extended-source observable, with a nonzero end factor. This is RL3's step from the pole to a pointwise bound plus the end factor.

**Fixed readings.**
- **PASS:** not applicable. The lane cannot pass by closing lemmas.
- **FAIL:** both lemmas are proved, so the RL3 lower bound holds and the 1e-19 m bar fails. Lane RL3 then becomes FAIL.
- **INCONCLUSIVE:** otherwise.

#### Lane RN2: interacting matter that does not conserve particle number, in d ≥ 2 (the M1/B1 open item)

**Probe N1.** For lattice matter on Z^d (d = 2, 3) whose interactions change particle number (e.g. φ³ or Yukawa with pair creation, over an interacting vacuum), ask two questions:
- Can exact global Poincaré closure (C3's Killing sector) hold for the full interacting theory?
- Can it hold in a sector that sits inside the continuum? Here M1's bounded-sector theorem does not apply, because each sector is unbounded.

Use:
- the Haag–Ruelle / asymptotic-completeness route (single-particle bands of the interacting theory are isolated bands, so T1 of M1 applies to them);
- the cluster-decomposition argument.

**Fixed readings.**
- **PASS:** an explicit interacting lattice theory with exact Poincaré closure in d ≥ 2.
- **FAIL:** proved impossible for the stated class, e.g. via the asymptotic single-particle bands plus M1's T1.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation.**
- **RL4:** Lemma U is likely provable, given 60 decades of slack. Lemma T is harder. Expected reading: INCONCLUSIVE, or FAIL if both lemmas close.
- **N1:** with asymptotic completeness and a mass gap, the theory's one-particle bands are isolated Bloch bands, so M1's T1 sum rule applies to them, and the S-matrix inherits the obstruction. Expected reading: FAIL (bounded, assuming a gap and asymptotic completeness).

### C4 result recorded 20:51Z (N1)

**Lane RN2, N1: INCONCLUSIVE, leaning FAIL.** Referee: CONFIRMED WITH CORRECTIONS (codex sol). The regular-band subclass has a rigorous bounded FAIL. Files: `agents/C4_N1_*`.

**What is established, assuming** exact commutators integrate to a positive-energy Poincaré representation and obey first-moment lattice covariance:
- The gapped vacuum is invariant.
- Every fixed-mass spectral subspace is invariant under boosts and lattice translations.
- Each irreducible component folds into a complete reciprocal-lattice tower, without using particle-number conservation.

**A separate result:** exact closure is impossible if the theory contains a nonzero global joint (T,H) eigenband with all of the following:
- a C¹ projector;
- E²/2 ∈ W^{2,1}(T^d);
- the required commutators in the strong/weak-domain sense.

**What remains open:**
- A gap plus asymptotic completeness does not supply that global-band hypothesis.
- The d ≥ 2 index extension lacks its dimension-uniform approximate tube lemma.

### C4 result recorded 21:01Z (RL4): lane RL3 becomes FAIL (bounded)

**RL4: CONFIRMED WITH CORRECTIONS** (codex sol), FAIL (bounded). Files: `agents/C4_RL4_*`.
- **The bound.** For all three stable six-layer operators, the windowed rapid-turn chaos kernel obeys |F_k| ≥ (1−2δ)^k |F_k^nn| uniformly in k, with floating-point δ < 0.047.
- **The rate.** At fixed physical ε, the alternating-cap renewal gives lim inf τ⁻¹ log V_ε(τ) ≥ c_low √ε, with c_low = 0.628–0.712. That is far above the 0.00975 at which the bar fails.
- **Scope.** The rate transfers to finite sources that have a spacelike past edge and a nonzero regular turn-on patch.
- **Still open.** Gaussian or edgeless histories, and the actual prefactor for a finite source at 1 Gpc.

**Lane RL3 / event-route noise: FAIL (bounded).** This follows the fixed RL4 reading: both lemmas are proved within the stated scope. The event substrate with stable layer readouts gets GR's √Δ lensing in the mean (RL2, positive). Its noise, however, grows at least as exp(0.63√ε·τ/ℓ_k). At the 1e-19 m locality bar this fails for edged sources over 1 Gpc. The required ℓ_k is about 7e-19 m, a miss of less than one decade.

### C4 last probe (21:08Z): lane RX, is the 1e-19 m locality bar the right bar?

**Why this matters.** The event-route noise fails at ℓ_k = 1e-19 m by less than one decade; it needs about 7e-19 m (RL4, refereed). That bar came from E1's pre-registration. Two questions follow:
- What do current observations actually bound for a causal-set or Benincasa–Dowker non-locality scale ℓ_k?
- Where did the 1e-19 m figure come from?

**Probe X1.** Sources:
- the packet's own origin for the bar (grep TESTS.md and supervisor_thread);
- the literature: Belenchia–Benincasa–Liberati–Marin and others on non-local d'Alembertians; LHC and collider effective-field-theory bounds on non-locality; optomechanical bounds; Saravani–Aslanbeigy–Kempf.

Report the strongest bound on ℓ_k with its source, and whether ℓ_k ≈ 7e-19 m is excluded.

**Fixed readings for X1.**
- **Bar too strict:** the strongest observational bound is weaker than 7e-19 m. The noise result then passes observationally, but the E1-registered bar is not changed. A follow-up test would need a new dated pre-registration.
- **Bar justified:** some bound excludes 7e-19 m.
- **Unclear:** otherwise.

No PASS or FAIL is recorded for any lane on the basis of X1. E1's fixed readings stand.

### C4 result recorded 21:14Z (X1): worker reading, not refereed (none required; no lane verdict depends on it)

**X1 reading: the bar is justified, provided ℓ_k is shared with matter.** This is E1's setting, where all fields live on events. File: `agents/C4_X1_report.md`.

**Where the 1e-19 m bar comes from.** It is Belenchia et al. PRL 116, 161303 (2016), quoting Biswas–Okada's LHC Drell–Yan bound of 2.5–3 TeV.

**Current collider bounds**, each on an exponential form factor; they translate to the BD kernel only at order-of-magnitude level, and no BD-specific collider analysis exists:
- LEP: ℓ < 1.9e-19 m;
- LHC Drell–Yan: ℓ < 7.9e-20 m;
- CMS dijets: ℓ < 4.2e-20 m.

**Consequence for the event-route noise.** Its requirement, ℓ_k ≈ 4–7e-19 m, is excluded by factors of about 2–17 if ℓ_k is shared with matter.

**A gravity-only ℓ_k is not bounded at this level.** But lensing is observed mostly with light, and the photon's ℓ_k is collider-bounded. Whether light-lensing noise is acceptable then turns on the effective source extent for incoherent light. At atomic scale it is about 3 e-folds; at 10 km it is about 570. That step is open.

**E1's fixed readings stand.**

### C4 final probe (21:12Z): lane RY, readout noise for lensed light

**Question.** Assume the photon's non-locality scale ℓ_k is at most 7.9e-20 m (the collider bound, X1). What is the stable-readout noise (RL2/RL4) for the light we actually see lensed? The variance grows in proper time τ ≈ √(2Ds), where s is the source's coherent extent. So the probe must settle what s is for incoherent thermal or atomic emission: the atomic or coherence scale, or the macroscopic source.

**Probe Y1.**
- Derive the effective s for a fixed-source variance, for incoherent sources made of many independent emitters. Is the variance of a sum of independent emitter fields controlled by each emitter's own s?
- Evaluate the noise in e-folds for strong-lensing observations, at D of about Gpc and optical/radio frequencies.
- Compare with what observations require: image flux stability, and VLBI phase coherence.

**Fixed readings.**
- **PASS:** for realistic incoherent sources, the noise is below 1 e-fold, i.e. negligible, at ℓ_k ≤ 7.9e-20 m. The derivation of s is controlled.
- **FAIL:** the noise exceeds what observed lensing allows, with s derived.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation.**
- For independent emitters, the variances add, and each grows with that emitter's own τ ≈ √(2D·s_atom), where s_atom is about 1e-10 m to 1 m (coherence length).
- For s ≈ 1 m and D = 1 Gpc: τ ≈ 2.5e13 m, and the e-folds come to about 0.63·√ε·τ/ℓ_k. The probe must compute ε from ℓ_k: ε = (ℓ/ℓ_k)⁴.
- Expected reading: borderline. The answer depends on the coherence length, so INCONCLUSIVE.

### C4 result recorded 21:28Z (Y1)

**Lane RY, Y1: INCONCLUSIVE, strongly leaning FAIL.** The codex sol referee did NOT CONFIRM the worker's FAIL. Files: `agents/C4_Y1_*`.

**What the referee confirmed.** Within the stable scalar layer-readout model, take any single finite emission current that has a spacelike past edge and a regular nonzero turn-on patch.
- Its all-frequency ensemble field-variance rate is set by its full timelike separation from the observer, not by its coherence length. This non-Huygens mechanism is confirmed.
- For emission Δt before the retarded time, the separation is τ ≈ √(2D·cΔt).
- Independent phase averaging makes the unfiltered mean noise powers add.
- At ℓ_k = 7.9e-20 m, the asymptotic exponent budget is already 4.5e4 for one second at 1 Gpc.

**Why it is not yet a FAIL.** There is no finite-distance normalization, and no positive lower bound on the optical/radio band fraction. So this is strong evidence of an instability, but not yet an observational lensing FAIL. Nor is it a no-go for every long-lived source.

### Campaign C4 closed (21:30Z; owner's end 22:21Z)

- Every pre-registered probe returned, and every result is recorded with its referee verdict. No lane is left unfinished.
- Synthesis: SUMMARY §17 and the PRICE_NOTE v6 delta (with wrap-up additions). X1 and Y1, added after §17 was written, are summarized in the closing entry below.
- **Closing state of the event route:**
  - Lensing in the mean: positive (RL2).
  - Noise at the bar: FAIL, bounded (RL4).
  - The bar itself is justified if ℓ_k is shared (X1, unrefereed).
  - Noise for lensed light: INCONCLUSIVE, strongly leaning FAIL (Y1). The decisive missing piece is the band fraction and finite-distance normalization.

## Lane RZ: the in-band fraction of the event-route noise (owner, 2026-10-11)

**Owner request:** "run the in-band noise fraction test". This is the decisive item that Y1's referee left open. It is a test setting only.

**The question.** RL4 (refereed) and Y1 (referee: INCONCLUSIVE, strongly leaning FAIL) give an all-frequency variance growth rate of at least c_low·√ε·τ/ℓ_k, with τ ≈ √(2D·cΔt). Two things are missing for an observational verdict:
- **(a)** a positive lower bound on the fraction of that noise power that lands in the observing band, for optical or radio light;
- **(b)** a finite-distance normalization, i.e. the prefactor at physical D, not only the asymptotic rate.

**Probes.** Both run on Claude Opus 5.5 at xhigh (same family).
- **Z1 (analytic).** Derive the frequency spectrum of the readout noise. Use the variance kernel, or the two-time covariance of (GJ)(x,t) for a monochromatic source at ω₀. Is the noise concentrated near ω₀ (multiplicative, "phase or amplitude noise" on the carrier), or spread to ~1/ℓ_k frequencies? Prove a lower bound on the in-band fraction, or show it is exponentially small.
- **Z2 (numerical and normalization).** Compute the noise power spectral density from the ladder/renewal structure (RL2–RL4 code) at accessible ε, with a carrier source. Measure the band fraction and how it scales. Obtain the finite-τ prefactor. Then translate to physical cases: lensed quasars and radio sources at 1 Gpc, and a 1 h lab lamp.

**Fixed readings.**
- **FAIL:** a proved (or controlled) positive lower bound on the in-band fraction, times the finite-distance variance, exceeds what observed lensing or interferometry allows (≳ 1 in relative variance) for at least one real observation class. With RL4 and Y1, the event route with shared ℓ_k is then an observational FAIL.
- **PASS:** the in-band fraction is shown to be small enough (e.g. exponentially suppressed by more than the e-fold budget) that observed lensing survives at ℓ_k ≤ 7.9e-20 m.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation.** The noise is multiplicative on the carrier: each extra chain node rescales the wave's amplitude and phase. So its spectrum sits near ω₀, broadened by the inverse correlation time of the multiplier, and the in-band fraction is O(1). Expected reading: FAIL, if the multiplicative structure is proved.

**Rules.** Every FAIL is refereed by codex gpt-5.6-sol at xhigh before it is recorded. These readings are not changed after the run.

### Lane RZ results (2026-10-11, 21:38Z to 22:31Z)

**Who and where.** Probes Z1 (analytic) and Z2 (numerical) were run by Claude Opus 5.5 at xhigh (same model family). They were refereed together by codex gpt-5.6-sol at xhigh. Files: `agents/RZ_Z{1,2}_report.md`, `agents/RZ_referee.md`; scripts in `scripts/RZ/`.

**Referee verdict: CONFIRMED WITH CORRECTIONS. Lane RZ: FAIL, at the controlled (not fully proved) level, bounded.**

**What the referee confirmed.** Within the stable scalar-layer readout, take finite emissions that are independently phased, have a spacelike past edge, and have a regular turn-on patch. For these:
- The ladder covariance is driven by |Ψ|², not by the carrier's phase. It has a nonzero white low-frequency level.
- Including the real-field mirror band and the observer boost, the optical and radio band penalty is only 122–147 e-folds, at 1 s of emission and 1 Gpc.
- A restricted-shell Fourier bound and a uniformly rescaled RL4 cap-walk local limit theorem control the remaining full-model and finite-distance factors. Both sit well within the 45,258 proved rate e-folds.
- About 44,000 e-folds remain even after a 1000-e-fold allowance.

So a real lensed optical or radio observation meets the FIXED FAIL condition, at the controlled level.

**Still open:**
- edgeless sources;
- a theorem-level transfer from the scalar readout to the photon, including whether ℓ_k is shared.

**Referee corrections:**
- The τ^{-3/2} power is not measured by the Monte Carlo fit. It follows from RL4's four-dimensional local limit theorem.
- Lemma F (the filtered U′ step) is controlled by a far-field-shell restriction.
- **Z1's side claim about RL4's GW gloss.** It is correct only at the old 1e-19 m bar: −23.5 e-folds with c_low, or +409 with the node rate. At the photon value 7.9e-20 m it is +109. RL4's rate is unaffected.

**Against the registered expectation.** The FAIL came out as expected, but by a different mechanism. The noise is not multiplicative on the carrier with an O(1) in-band share. It is white, and its in-band share is about e^{-110} to e^{-147}. The growth budget overwhelms that share.

**Event route, closing state.**
- Lensing in the mean: positive (RL2).
- Noise at the locality bar: FAIL, bounded (RL4).
- Observed lensed light at the collider-bounded photon ℓ_k: FAIL at the controlled level (RZ), with Y1's mechanism confirmed.
- **Reading:** the event substrate with stable layer readouts and a shared ℓ_k is excluded observationally, at the controlled level, within the stated scope.

## Lane RV4: can a principle remove the free shear term? (owner, 2026-10-11)

**Owner request:** "run the vacuum-referenced dressing follow-up on the free shear term". Test setting only.

**The problem.** V3 (refereed) showed three things:
- The local, translation-covariant uniform-strain coupling of free lattice matter leaves an E_g shear mass, μ_E = +1.97e-3 (scalar, m = 1).
- This comes from the Jacobian of the momentum flow.
- The T_2g channel is protected because its flow is divergence-free (Liouville).

Removing μ_E currently takes one of these:
- an E_g counterterm (tuning);
- a selected momentum symbol (tuning);
- R₀ (a definition);
- exactly matched Bose–Fermi spectra (P1; mass relations).

**The question.** Is there a principle, not a tuning and not a definition, that fixes the free-matter strain coupling so that μ_E = μ_T2 = 0? Candidates:
- **(a) Non-separable momentum symbols / flows.** The flow v = (sin k_x cos k_y, −cos k_x sin k_y) is divergence-free and ≈ (k_x, −k_y) at small k. Can a single momentum symbol p(k) make every traceless strain flow v = h·p divergence-free? Or at least make every channel's μ vanish?
- **(b) Covariant measure prescriptions.**
  - Half-density / √J-weighted couplings.
  - A Weyl-type volume-form coupling.
  - Requiring the coupling to equal the formal unitary on the bulk, density of states included.
- **(c) A conservation or Ward principle** that forces the Jacobian term to cancel, e.g. requiring the vacuum to stay an eigenstate of the strained Hamiltonian with the same energy density, built into the flow.
- **(d) R₀ restated as a principle,** e.g. "uniform strain is a relabelling, so the vacuum energy density is strain-invariant." Is this derivable from anything in the axioms, or only an imposed rule?

**Probes** (Claude Opus 5.5 at xhigh; same family):
- **S1 (theorem):** classify (a)–(d).
  - Conjecture to prove or refute: a strain coupling whose flow is divergence-free in every shear channel exists iff the momentum symbol is linear (SLAC).
  - For local periodic symbols, find the minimal achievable (μ_E, μ_T2) and whether any principle selects a point with both zero.
  - Map (b)–(d) to principle, tuning, or definition.
- **S2 (numerics):**
  - Scan local momentum symbols and flows, separable and non-separable, range r ≤ 4, in d = 2 and 3, using V3/P1's Jacobian formula. Record μ_E, μ_T2 and the trace channel.
  - Find the trade-off surface: can both shear channels vanish simultaneously with a local symbol, and at what cost elsewhere (one-cone speed, the C3 anomaly)?
  - Evaluate the half-density prescription explicitly.

**Fixed readings.**
- **PASS:** a principle (stated, not tuned or defined) fixes a local free-matter strain coupling with μ_E = μ_T2 = 0. It must keep the free-matter properties established in RN L1 (exact stress, linear first class, 1/r with universal G).
- **FAIL:** proved that μ_E = μ_T2 = 0 with a local coupling needs a non-local (SLAC) symbol, a tuning, a definition (R₀), or matched spectra. Bounded to the classes examined.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation.**
- Requiring div(h·p) = 0 for all traceless h forces ∂_i p_j = λ δ_ij, so p is linear: SLAC. That is the C3 obstruction again.
- Non-separable symbols can zero E at the cost of T2.
- Half-density prescriptions reproduce the formal unitary only with non-local seams.
- R₀ is not derivable from the axioms.
- **Expected:** FAIL (bounded).

**Rules.** Every FAIL is refereed by codex gpt-5.6-sol at xhigh before it is recorded. These readings are not changed after the run.

### Lane RV4 results (2026-10-11, 22:44Z to 23:36Z)

**Who ran it.** S1 (theorem) and S2 (numerics) were run on Claude Opus 5.5 at xhigh (same family). Both were refereed by codex gpt-5.6-sol at xhigh and CONFIRMED WITH CORRECTIONS. Files: `agents/RV4_S{1,2}_*`, scripts in `scripts/RV4/`.

**Lane RV4: FAIL (bounded).**

**S1.** Scope: gapped, single-band, free quadratic matter, with RN-L1 energy-current momentum p = ∇(ω²/2).
- The bulk-flow coupling has the stated Jacobian response.
- No periodic momentum field makes every shear flow divergence-free (the conformal Killing obstruction).
  - Axis hopping protects only T_2g.
  - Body-diagonal hopping protects only E_g.
- Canonical SLAC leaves μ_E(1) = 1.4832833e-2.
- The density prescriptions examined reduce to one of three things: a violation of the exact stress, a tuned coefficient, or R₀.
- A finite-range non-separable symbol can zero both channels at one chosen mass, but the zero drifts with mass.
- Cancelling over a range of masses is excluded for single-minimum analytic separable symbols, and for Morse symbols without cancellation at coincident critical levels.
- Compact Ward covariance would enforce μ_E = μ_T2, but it is incompatible with the field-independent e^{−iP[ξ]} bulk response.

**S2.** S2 found a genuine object: a finite-range, mass-independent O(h²) operator seagull for the nearest-neighbour free KG scalar.
- It cancels the uniform-strain DOS Hessian in both shear channels.
- It leaves intact RN-L1's linear stress, the linear first-class algebra, 1/r, and universal G.

But it is only a homogeneous O(h²) completion that preserves the DOS. Its selection condition imposes the spectral invariance directly, it is not unique, and it is not derived from the axioms. So it sits in the definition/R₀-type disjunct, and it does not warrant PASS.

**Open:**
- field-dependent, non-uniform Ward completions;
- degenerate or coincident-level non-separable bands;
- multi-band and Berry structures;
- interactions.

**Against the registered expectation.** FAIL, as expected. Two corrections to my expectation:
- The obstruction is the conformal Killing condition, which excludes every periodic symbol. I had stated it as linearity.
- SLAC does not help: its E-flow has a zone-face sink and source.

## Lane RFW: field-dependent Ward completion (owner, 2026-10-11)

**Owner request:** "run the field-dependent Ward completion test". This is the open item from RV4, S1 and C3: field-dependent gauge generators, i.e. RN L1's unsearched second-order completion. Test setting only.

**The question.** C3 (refereed) and K2 found the same obstruction. With field-independent generators, the matter Killing transformations fail to close at O(κ) Hamiltonian / O(κ²) Euclidean: [L_ω, D_ρ] = −ω S_ρ D_ν, an extra cos k factor. Every metric-dependent correction vanishes in that sector. RV4 S1 showed that a compact Ward identity would force μ_E = μ_T2 (the cosmological-constant value), but that identity is incompatible with field-independent generators.

So: can a gauge algebra with field-dependent generators remove the Killing-sector obstruction? This would be an open or soft algebra: structure functions depending on h and on matter, gauge parameters that are operator-valued or field-dependent, and nonlinear (GR-like Lie-derivative) transformations of h. The completion must be local, with finite field content. Would the resulting Ward identity fix the E_g shear mass?

**Probes** (Claude Opus 5.5 at xhigh, same family):
- **F1, cohomology and theory.** Use the BRST/BV framework for local consistent deformations (Barnich–Brandt–Henneaux; the uniqueness of Einstein–Hilbert as a deformation of Fierz–Pauli; Boulware–Deser–Wald) on the lattice. Is C3's Killing-sector anomaly a nontrivial class in the local lattice BRST cohomology at second order? A nontrivial class cannot be removed by field redefinitions or field-dependent generators. W3 found the anomaly functional F is non-local in h. Also: do differential-operator-valued gauge parameters, which absorb the cos k factor, force an infinite tower of generalized symmetries (higher-spin-like; B1)?
- **F2, constructive search.** Run the Noether procedure on Z⁴ (K2's Euclidean setting: free scalar plus lattice Fierz–Pauli, exact through O(κ)) at O(κ²). Allow corrections to the gauge transformations of h and φ that are linear and quadratic in fields, range ≤ r, together with seagull and vertex corrections to the action. Solve the invariance conditions, including the Killing sector, as a linear system for r = 1, 2, 3. Report the solution space, or the rank obstruction, and how it changes with r.

**Fixed readings.**
- **PASS:** an explicit local completion (finite field content, finite range) with field-dependent gauge transformations that makes the coupled action invariant through O(κ²) for non-uniform ξ, including the Killing sector, with a resulting Ward identity fixing μ_E = μ_T2.
- **FAIL:** proved that no such completion exists in the stated class (range, polynomial order, finite field content), or that one exists only with infinite field content.
- **INCONCLUSIVE:** otherwise.

**Supervisor expectation.**
- The Killing-sector anomaly is a nontrivial local BRST class, the lattice analogue of an anomaly that cannot be removed by counterterms.
- Field-dependent generators cannot remove it, because at flat background its field-dependent parts vanish (C3 lemma).
- Operator-valued parameters need an infinite tower.
- F2's linear system has no solution for r ≤ 3.
- Expected reading: FAIL (bounded).

**Rules.** Every FAIL is refereed by codex gpt-5.6-sol at xhigh before it is recorded. These readings are not changed after the run.

### Lane RFW results (2026-10-12, 01:48Z to 02:36Z)

**Provenance.** Probes F1 (cohomology) and F2 (constructive) ran on Claude Opus 5.5 at xhigh (same model family). Both were refereed by codex gpt-5.6-sol at xhigh. Files: `agents/RFW_F{1,2}_*`; scripts in `scripts/RFW/`.

**F2: CONFIRMED WITH CORRECTIONS. Bounded FAIL.**
- **Setting.** K2's nearest-neighbour scalar on Z⁴. Its O(κ) pseudo-translation and symmetric stress are held fixed, up to local improvements and on-shell-trivial symmetries.
- **Result.** No translation-covariant completion makes the action gauge invariant through O(κ²) using only h and φ. This holds at every finite range, and more generally for any completion that is C¹ at q = 0.
- **How.** The constant-translation h·φ²·ξ coefficient already gives an impossible first-jet identity, for every finite range and every m² ≥ 0.
- **Open:**
  - altered leading generators;
  - odd-field extensions;
  - fermions;
  - auxiliary or multiband matter;
  - infinite towers;
  - singular, non-local or quasi-local completions.

**F1: NOT CONFIRMED as stated.** A narrow fixed-field/graded FAIL is established; the broad claim is INCONCLUSIVE.
- **Hypotheses.**
  - A fixed gravity–matter BV complex with a block-diagonal Killing action that preserves matter number and parity.
  - A regular irreducible scalar/simple shell.
  - A nonzero scalar translation symbol.
  - A local, IR-normalized gauge map.
  - The continuum e(4) bracket with c = 1.
- **Established under these hypotheses.**
  - The affine-Killing projection is invariant under diagonal field-dependent generators, open-algebra terms, field redefinitions, counterterms and seagulls.
  - Locality fixes the orbital part of the rotation to the first moment of the translation.
  - Tangency plus closure would force the shell into a complex quadric. That is incompatible with a nonzero finite Fourier kinetic symbol.
  - Confirmed: the exact K2 scalar and fermion defects, the SLAC interior control, and the Hamiltonian tower.
  - Stückelberg fields trivialize the class without fixing either shear coefficient.
- **Not established.** The claimed FAIL for all local finite-field BV completions. That broader question stays INCONCLUSIVE.

**Lane RFW: FAIL (bounded).** It is bounded to two things:
- F2's fixed-O(κ)-data class for the K2 scalar;
- F1's fixed-field, graded class.

Still INCONCLUSIVE: altered leading generators, non-block-diagonal BV completions, multiband or auxiliary matter, and quasi-local tower actions.

**Against the registered expectation:** FAIL (bounded), as expected. The obstruction sits entirely in the cos k factor (F2's Leibniz diagnostic). A clean theorem (F1's T1, quadric) holds under the narrowed hypotheses.

## Campaign C5: reverse-engineering the rules from observations (owner, 2026-10-12 10:57Z to 2026-10-13 10:57Z, 24 h)

**Owner request:** "keep reverse engineering observations into the underlying rules of our TOE for 24 hours".

**How C5 runs.**
- **Method.** Each round goes forward from one or more observations to necessary properties of the substrate's rules (a necessity derivation, with its hypotheses stated). Candidate rule sets are then built to satisfy those properties, and the candidates are tested against the refereed walls of this packet.
- **Agents.** Probes run on Opus 5.5 at xhigh.
- **Referee.** Every FAIL or no-go goes to codex gpt-5.6-sol at xhigh before it is recorded.
- **Readings.** Readings are fixed before each run.
- **Axioms.** Every axiom change is named as a price, never adopted.
- **End.** 2026-10-13 10:57Z. Unfinished items are marked "not completed (stopped at end)".
- **Driver.** A recurring cron checks progress about every 40 minutes. It records results and launches the next round's pre-registered tests.

**Readings used for derivation probes, fixed for all rounds.**
- **DERIVED:** the necessity is proved from the stated observations plus explicitly stated hypotheses, with the bound given.
- **SUGGESTED:** argued, not proved.
- **REFUTED:** the claimed necessity is false (a counterexample exists).
- Test probes carry their own PASS/FAIL/INCONCLUSIVE readings.

### C5 Round 1 (10:57Z)

**Where we start.** The refereed state: SUMMARY §§10–20 and PRICE_NOTE v5 plus the v6 delta.
- On a fixed grid, local matter has no boost that closes with its momentum. The cause is the cos k factor (C3/K2/RB/RFW).
- A fixed random event set has the right mean lensing (RL2) but per-realization noise that observation excludes (RL4, RZ).
- Free local matter generates the E_g shear mass (V3); removing it costs a tuning or an imposed rule (RV4).

**Round 1 probes:**

- **O1: Lorentz invariance.**
  - Observations: matter Lorentz invariance to about 1e-20 (photon decay, UHECR, LHAASO); GW170817 c_T to 1e-15.
  - Combined with the refereed boost theorems, derive what the substrate's spacetime-symmetry structure must be.
  - The candidates to sort: exact Lorentz invariance in law (events, or a continuum fibre); an emergent mechanism; a preferred frame with tuning.
  - Expected: DERIVED, either Lorentz invariance in law or tuning at about 1e-20 per species. Only Lorentz-invariant-in-law substrates avoid tuning.

- **O2: universality.**
  - Observations: the equivalence principle (MICROSCOPE, 1e-15) and a massless spin-2 field with universal coupling (Weinberg soft theorem).
  - Derive the necessary structure of the substrate's translation and stress: an exactly conserved, universal local T coupled to h.
  - Then reverse-engineer the minimal rule that supplies an exact continuous translation while keeping discreteness somewhere. Candidates:
    - discreteness in count, not position (events);
    - discreteness in Hilbert space or records, not in space;
    - a continuum fibre per cell (I1).
  - Expected: DERIVED: an exact continuous translation symmetry is necessary. Discreteness must live off the translation group.

- **Q1: a coherent (unrecorded) event substrate, the key test.**
  - Idea: RL2's mean lensing passes; RL4/RZ's failure is per-realization noise. Suppose the event microstructure is quantum, a coherent superposition over sprinklings that is not recorded. Then observed amplitudes may be ensemble means, and the noise becomes something else.
  - Compute two things:
    - (a) the observable for a coherent sum over sprinklings (amplitude-level averaging versus intensity-level mixing);
    - (b) whether matter decoheres the substrate (which-sprinkling information leaking into records), which would bring the classical noise back.
  - **Fixed readings:**
    - **PASS:** an explicit coherent-substrate rule under which the observed lensing amplitude is the RL2 mean, with residual fluctuations below observational bounds, and decoherence by observed matter is shown to be negligible.
    - **FAIL:** a proof that the noise reappears (intensity-level or via decoherence) at RZ's level in the stated class.
    - **INCONCLUSIVE:** otherwise.
  - Expected: INCONCLUSIVE. Coherent averaging removes the noise from amplitudes, but intensities pick up a |Ψ|² variance term equal to RZ's. The decisive question is whether that variance term is observable as noise (it is, per-shot) or appears as a decoherence-like broadening. Lean FAIL.

- **O3: vacuum energy and shear.**
  - Observations: the measured cosmological constant (tiny), plus the refereed RP and RV4 results (E_g shear needs Pauli-type sum rules or an imposed rule).
  - Derive what the matter content and substrate must do: exact boson–fermion pairing at the cell scale, or an imposed spectral-invariance rule.
  - Test whether a qubit site (M₂(C)) naturally pairs a bosonic and a fermionic mode, e.g. via Jordan–Wigner / hard-core boson ⇔ fermion duality, so the pairing sum rules (R0–R6) hold by structure.
  - **Fixed readings for the qubit-pairing test:**
    - **PASS:** an explicit qubit rule whose excitations come in exactly paired bosonic and fermionic bands, satisfying R0–R6 without tuning.
    - **FAIL:** proved impossible for qubit sites in the stated class.
    - **INCONCLUSIVE:** otherwise.
  - Expected: FAIL. Hard-core boson/fermion duality is one excitation viewed two ways, not a pair, and interactions break pairing.

- **O4: records.**
  - Observations: quantum mechanics as observed (interference of massive molecules, Bell violations, decoherence rates) and the classicality of records.
  - Together with Q1's and RZ's lesson, derive what the Record axiom must and must not lock: which degrees of freedom can be recorded without destroying interference (molecule interferometry at 25 kDa) or lensing coherence.
  - Expected: DERIVED: records cannot lock the spacetime microstructure, or lensed and interfering amplitudes decohere. So Record must be restricted to coarse, gauge-invariant or conserved data. This is a sharpened P4.

- **O5: synthesis.** From O1–O4, plus the refereed walls, state the minimal set of rule changes to the four axioms consistent with every observation used. Name each as a price. Design the decisive tests for round 2.

### C5 Round 1 results (recorded 12:00Z)

All round-1 probes were refereed by codex gpt-5.6-sol at xhigh. Files: `agents/C5_{O1,O2,O3,O4,Q1}_*`; synthesis in `agents/C5_O5_synthesis.md` (same family, unrefereed).

**O1 (Lorentz invariance) — NOT CONFIRMED as a necessity theorem.**
- **Established.** Under the geometric-EFT hypotheses, having no invariant traceless rank-2 tensor (V₂^tl = 0) is *sufficient* to forbid dimension-4 speed operators, and it implies there is no invariant vector (V₁ = 0).
- **Invariant counts.** The axioms' proper-cubic group has (V, S2) = (1, 2). B4⁺ and W(B4) have (0, 1). So a truly hypercubic whole matter law protects dimension-4 matter kinetic terms without continuous Lorentz symmetry.
- **F2's e–γ split** of 8.55e-3 needs a counterterm of about 3.1e-17; ξ = 1 removes it. This is regulator-specific.
- **Not established:**
  - a universal necessity theorem;
  - one tuning per pair of species;
  - a counterexample to the full claim covering matter and gravity together.

**O2 (universality) — CONFIRMED WITH CORRECTIONS.** Assuming exact soft spin-2 gauge redundancy and the pole Ward identity:
- The soft residue is an additive collision invariant.
- Its time component is energy, provided a further Noether bridge holds.
- Regular spatial invariants are excluded only in the cited bounded classes.
- The grid's tree-level defect is C(pa)², about 2e-41 at nucleon momenta, so tree-level precision cannot force exactness.
- Under a supplied weak energy coupling, a band-bottom wavepacket falls as −β_B∇Φ. MICROSCOPE constrains only differences in effective β between compositions.
- Exact geometric translations are rigorously incompatible with:
  - (i) finite one-particle fibres uniformly tied to sites (Lemma S);
  - (ii) strictly local continuous interpolation of the qubit-chain shift (Lemma G, 1D);
  - (iii) finite-dimensional local algebras in positive-energy relativistic nets (Reeh–Schlieder).
- Open: unbounded or non-geometric positions; quasi-local or asymptotic actions; infinite-transverse many-body systems.
- The proposed rule (a continuum with records) is SUGGESTED, not derived.

**O3 (vacuum and shear) — CONFIRMED WITH CORRECTIONS.**
- **Free species.** For finitely many free lattice species, exact cancellation on an open mass interval forces the signed aggregate density-of-states measures to be equal (Theorem 1a). The precision arithmetic is correct.
- **Nilpotent Q** with H = {Q, Q†} and nonzero superdimension gives exactly zero ground energy, plus paired levels under any deformation that preserves Q.
- **Qubit sites.** A two-state site cannot hold independent exact CCR and CAR modes, and the dualities do not duplicate the spectrum. So the on-site/free subclass is a bounded FAIL.
- **FS M1 lattice SUSY** is a genuine interacting escape. It needs an added Hamiltonian, a grading and a coupling rule that goes through Q. It establishes neither the physical E_g coupling nor visible partners.
- **Qubit-pairing test overall:** INCONCLUSIVE.

**O4 (records) — NOT CONFIRMED in its broad claims.**
- **Established:**
  - A permanent, perfectly distinguishable record channel that gains branch information obeys V ≤ BC(p_A, p_B), with the exact Poisson affinity formula.
  - Under the narrow H3 model (fixed-cell Poisson at ℓ_P⁻⁴√−g in weak branchwise Newtonian metrics), −ln BC = 2πm²c³dT/ħ², with G cancelling. This is catastrophically large for matter waves.
  - The 0.1 µm localization bound is about 5.3e-11 s⁻¹ per nucleon.
  - Bell data exclude independently factorized local joint outcome laws.
- **Not proved:** that every matter-responsive microgeometry must be unrecorded; that Y1–Y4 exhaust what records may lock; that "records copy, never measure" is necessary. P4′ remains a sufficient policy.
- **Correction:** the 70 s experiment used Cs-133 at d = 1.9 µm.

**Q1 (coherent event substrate) — CONFIRMED WITH CORRECTIONS.**
- **Proved FAIL** for orthogonal sprinkling labels with configuration-diagonal coupling and fixed Poisson Born weights. Tracing out the substrate, or applying any later trace-preserving operation acting only on the substrate, gives the Poisson random-unitary channel. The intensity is then |Ψ|² + V, which inherits RZ's controlled exclusion: ln(N_B/S) ≥ 43986.
- **Two exact results:**
  - Projecting back onto the initial substrate succeeds with probability 1 − variance.
  - A single circular-Gaussian mode gives amplitude 2Ψ/(2+V).
- **Campaign-wide:** INCONCLUSIVE, leaning FAIL. Open: structured multimode amplitudes, tuned joint-unitary erasure, other spectral mechanisms, and decoherence induced by matter.

### C5 Round 2 (pre-registered 12:02Z from the O5 synthesis; launched now)

The O5 synthesis left three candidate sets of axiom changes. They are mutually exclusive; each change is named as a price, none is adopted.
- **A** — continuum base with discreteness only in records.
- **B** — Euclidean Z⁴ with a hypercubic whole law and the arrow in the state.
- **C** — keep Z³ and tune.

None of the three produces the graviton, and none explains Λ.

Round 2 tests what decides between them. The full pre-registration text follows verbatim from `O5_round2_prereg.md`.

### C5 Round 2 (pre-registration draft by O5; readings fixed before any run)

**Where we start.** Round 1 (O1–O4 and Q1) and its codex verdicts:
- O1: NOT CONFIRMED.
- O2: CONFIRMED WITH CORRECTIONS (CWC).
- O3: CWC.
- O4: NOT CONFIRMED.
- Q1: CWC. FAIL is proved for fixed Poisson Born weights with the substrate traced out; the full class is INCONCLUSIVE, leaning FAIL.

O5's synthesis leaves three mutually incompatible minimal sets:
- **A:** a continuum base, with discreteness only in sparse records.
- **B:** a Euclidean Z⁴ at ξ = 1, with the whole law B4⁺-covariant and the arrow in the state.
- **C:** keep Z³ and tune.

Two other routes are near-closed: random events (E), and a quantum vacuum substrate with discrete events (A′). Round 2 targets the open problems that decide which set survives.

**Rules for every probe.**
- Agents: Opus 5.5 at xhigh.
- Every FAIL, REFUTED or no-go goes to the codex gpt-5.6-sol (xhigh) referee before it is recorded.
- Every axiom change is named as a price, never adopted.
- Before deriving, each probe greps the repository and the packet for prior art and counts any match once.
- Each probe states its hypotheses before giving a title, and lists the outside realizations its scope excludes.

**Readings for derivation probes** (as in round 1):
- **DERIVED:** proved from the stated observations plus explicitly stated hypotheses, with the bound given.
- **SUGGESTED:** argued, not proved.
- **REFUTED:** the claimed necessity is false; a counterexample exists.

Test probes carry their own PASS / FAIL / INCONCLUSIVE readings, given below.

---

**R2-1: class II gravity. Can a Z⁴ grid have an exact gauge identity without secretly being a continuum?** (decides B)

- **Plain question.** On a 4D grid with equal steps, matter light speeds are protected by the grid's symmetry. The graviton still needs an exact gauge identity, or 11 hand-set numbers (K1, refereed). Every identity tried has failed:
  - K2 fails at second order;
  - RFW is a bounded FAIL;
  - T2's perfect-action kernels leave a p = 4 stiffness floor under proper-distance coupling.

  Can a quasi-local law do better? Lattice chiral symmetry survives in the modified Ginsparg–Wilson form; can a modified identity of that kind exist for gravity, from a perfect (RG-blocked) or Ginsparg–Wilson-type action? Or does exactness need the whole blocked continuum, so that B is set A in lattice clothing?
- **Setting.** Euclidean Z⁴, ξ = 1. A W(B4)-covariant law with finitely many fields per site, and couplings that decay at least exponentially (quasi-local). The matter is a free scalar and then a φ⁴ or Yukawa-interacting scalar, coupled to a linearized graviton h_μν. Prior art to count once:
  - T2 (`TESTS.md:86-126`, families C and C′ and the κ ≡ 0 relabelling);
  - K1 and K2 (`C4_K1_referee.md`, `C4_K2_referee.md`);
  - RFW (`SUMMARY.md` §20);
  - Lemma R (`T2-REF:21`).
- **Probes.**
  - **(a) Construction.** Block continuum linearized gravity plus the scalar with a W(B4)-covariant Gaussian blocking kernel, and write the resulting lattice Ward identity in Ginsparg–Wilson form (δS equal to terms in the blocking kernel).
  - **(b) Counting.** Decide which of K1's 11 gauge-restoration directions (3 mass forms + 8 kinetic forms) the identity fixes.
  - **(c) Closure.** Repeat K2's Killing-closure test at O(κ²) with the modified (remnant) symmetry.
  - **(d) Locality.** Give the decay length of the couplings, and say whether the symbol is analytic in a strip.
  - **(e) Field content.** Does the identity hold with the lattice fields alone, or does it need auxiliary fields, a tower of blocked modes per cell (P10), or the blocked continuum supplied as data?
  - **(f) Interactions.** Does the identity survive a φ⁴ or Yukawa vertex with additive lattice momentum? Lemma R (refereed, narrowed) excludes ordinary local laws of that kind for the relabelling escape.
- **FIXED readings.**
  - **PASS:** an explicit quasi-local, W(B4)-covariant law with finitely many fields per site whose (possibly Ginsparg–Wilson-modified) linearized-diffeomorphism identity holds through O(κ²) for gravity plus interacting matter, and fixes all 11 K1 directions with no tuning.
  - **COLLAPSES-TO-A:** such an identity exists only with an infinite per-cell tower, or with the blocked continuum supplied as data. Record this as "set B reduces to set A in lattice coordinates".
  - **FAIL:** a proof that every quasi-local W(B4) law with finitely many fields per site fails the identity at O(κ²). This extends K2 beyond regular nearest-neighbour laws.
  - **INCONCLUSIVE:** otherwise.
- **Expectation.** INCONCLUSIVE, leaning COLLAPSES-TO-A.
  - A Ginsparg–Wilson-type relation can protect the linear identity at O(κ).
  - The O(κ²) closure needs the full nonlinear algebra. A blocked action carries that only through the continuum it was blocked from.

---

**R2-2: Lorentz-invariant discreteness, quantum and classical** (decides whether routes E and A′ are closed in general)

- **Plain question.** Random events that steer light make shot-by-shot noise (RZ, refereed). A plain quantum superposition of them does not help (Q1, refereed for fixed Poisson weights; the full class is INCONCLUSIVE, leaning FAIL). Is that true of **every** Lorentz-invariant discreteness of spacetime events? Two lemmas would settle it:
  - **N-Q:** a positive-energy quantum vacuum cannot contain countable events at all.
  - **P-L:** a classical Lorentz-invariant point process always has weight at spacelike momentum transfer, so it always scatters on-shell light.
- **Hypotheses for N-Q, as drafted in O5 §2.6:**
  - **(N1)** Unitary translations, with spectrum in V̄₊ and a unique invariant vector Ω.
  - **(N2)** Locality, with Ω separating for every bounded-region algebra.
  - **(N3)** Each bounded 4D region O has a count N(O) affiliated with A(O), with spectrum in {0, 1, 2, …}.
  - **(N4)** Additivity over finite disjoint unions, at every separation, timelike included.
  - **(N5)** Fine-scale simplicity: any finite family of regions has a common refinement into regions on which N is a projection.
  - **(N6)** Covariance, with ⟨N(O)⟩ = ρ·vol(O) and ρ > 0.
- **Hypotheses for P-L.** A stationary, simple point process in R^{1,3} whose law is invariant under the Lorentz group, with finite local second moments. Its structure factor S(q) is the Fourier transform of ρδ⁴ + ρ²(g − 1), a positive Lorentz-invariant measure.
- **Probes.**
  - **(a) Check N-Q's sketch.** The steps to check:
    - the Halmos two-projection step (commutation of disjoint fine counts);
    - the extension to all regions through N5;
    - the symmetric two-point function with support in V̄₊ ∩ (−V̄₊) = {0};
    - Ω separating, which makes the count a constant ρ·vol(O)·1.

    Then find the weakest form of N4 and N5 that still works.
  - **(b) Prior art.** Compare with Malament (1996), Halvorson–Clifton (2002) and Hegerfeldt. Say what, if anything, is new: the 4D event version, with additivity across timelike separation.
  - **(c) Escapes.** List and classify them: non-additive counts; counts additive only across spacelike separation (slice counts, which need a foliation); non-local counts; a non-unique vacuum; approximate simplicity.
  - **(d) P-L.** Attempt a proof, modelled on the refereed corrected Lemma P (`E23_referee.md:90-112`): the δ⁴ self-term contributes ρ at every spacelike q, and positivity plus Lorentz invariance must then fail to cancel it. Alternatively, construct a counterexample with S(q) = 0 for all spacelike q.
  - **(e) Survivors.** For any surviving construction, compute the incoherent on-shell scattering rate at RL coupling strength and compare it with RZ's bar.
  - **(f) Reuse.** Reuse O5's check that a forward-cone-only spectral measure gives volume-law count variance (`o5_checks.out`), so that variance is not used as the criterion.
- **FIXED readings** (derivation):
  - **DERIVED:** both lemmas proved under the stated hypotheses. Then every Lorentz-invariant discrete event structure that steers propagation either makes noise (classical) or cannot exist as local counts (quantum vacuum).
  - **SUGGESTED:** argued only, for either lemma. Record which one.
  - **REFUTED:** an explicit counterexample: a covariant integer-count net in a positive-energy vacuum, or a Lorentz-invariant point process with zero spacelike structure factor.
- **Expectation.**
  - N-Q: DERIVED. It sits close to the Malament and Halvorson–Clifton theorems.
  - P-L: SUGGESTED. Classical Lorentz-invariant processes are poorly characterized.
  - Lean: route E and A′'s discrete events are both closed, with discreteness left to sets A (records), B (grid), C (grid) or D (deformed coordinates).

---

**R2-3: rare record flashes on a continuum, against the gravity walls** (decides whether set A is consistent)

- **Plain question.** In set A, the only discreteness is rare record "flashes" on a continuum, as in relativistic GRW (Tumulka's rGRWf). Each flash kicks matter, so energy-momentum is not exactly conserved. Do such flashes, at rates allowed by interference and heat bounds, clash with a massless graviton, Λ, or the gravity walls? And can they be dense enough to give definite outcomes?
- **Setting.** A continuum QFT (a free massive scalar or Dirac field) plus a covariant-in-law flash law, coupled to a supplied linearized graviton. The rates and resolutions must sit inside the refereed O4 budget:
  - ≤ 5.3e-11 s⁻¹ per nucleon at 0.1 µm (Earth heat);
  - Lemma 1's V ≤ BC for 25 kDa molecules;
  - Cs-133 at 1.9 µm for 70 s;
  - ions coherent for more than 1 h;
  - X-ray and CSL-type limits as published.

  Prior art to count once:
  - PRICE_NOTE P4 and B referee line 103 (4e-151 per event);
  - X2 (white stress noise in FR3 gases, a bounded FAIL);
  - O2's flash row and the Josset–Perez–Sudarsky unimodular argument.
- **Probes.**
  - **(a) Source.** Compute the flash-induced stochastic source J^ν = ∂_μT^{μν} and its spectrum.
  - **(b) Bianchi.** Check compatibility with the Bianchi identity: GR tolerates only a gradient source, so the setting is unimodular. Compute the implied Λ(t) drift over the Hubble time.
  - **(c) TT noise.** Compute the TT stress-noise spectrum S_TT(q → 0). Compare it with P0's μ = 2.39e8 eV⁴ (graviton-mass channel) and with GW strain-noise and pulsar-timing levels.
  - **(d) Heating.** Check heating against neutron stars and the intergalactic medium.
  - **(e) Bell.** Check that the joint flash law is non-factorizing and no-signalling, as F8 requires.
  - **(f) Density.** Find the maximal flash density compatible with (a)–(e), as a fraction of Planck-density events.
  - **(g) Definite outcomes.** Find the minimal density that gives definite outcomes. Example: a 1 µm pointer of 1e10 nucleons localized within 1 ms.
- **FIXED readings.**
  - **PASS:** an explicit covariant flash law satisfying (b)–(e) with stated numbers, at a density that gives definite outcomes (g).
  - **FAIL:** a proof that every covariant flash law dense enough for (g) violates one of (b)–(e).
  - **INCONCLUSIVE:** otherwise.
- **Expectation.** PASS at GRW-type rates, with every gravitational effect many orders below the bounds. The mandatory reading attached to that PASS: the flashes are then gravitationally inert, so set A's discreteness plays no role in gravity, and the graviton and Λ stay unexplained.

---

**R2-4: set B's weight. Is Admissibility's probability clause satisfiable on Z⁴?** (decides set B's extra Admissibility price)

- **Plain question.** In set B, Admissibility's "probability distribution … determined by the nearest-neighbor conditions" becomes the conditional of a Euclidean Gibbs weight on Z⁴. Physical probabilities exist only after the Osterwalder–Schrader reconstruction. Is that weight a positive, normalizable, reflection-positive probability when the content includes the following?
  - (i) Chiral fermions, as in the Standard Model's weak sector.
  - (ii) A graviton or metric sector.

  If not, what is the smallest change to Admissibility, and does that change bring back a preferred tensor (Lemma C) or a law-level arrow (Lemma E)?
- **Setting.** Z⁴ at ξ = 1, a W(B4)-covariant law, nearest-neighbour and then quasi-local. Prior art to count once:
  - K7a's 4 tastes;
  - K2's open coupled reflection positivity;
  - the registered `kinetic_isotropy_primitive`;
  - Nielsen–Ninomiya, Ginsparg–Wilson/overlap, Lüscher's chiral-gauge construction;
  - the Gibbons–Hawking–Perry conformal factor;
  - dynamical triangulations and CDT. CDT's causal restriction uses a foliation, which puts it in class I.
- **Probes.**
  - **(a) Chiral fermions.** State Nielsen–Ninomiya's hypotheses and check whether nearest-neighbour couplings plus W(B4) force doublers or tastes. Then give the locality class of the overlap/Ginsparg–Wilson operator (exponential, not nearest-neighbour), and say when the phase of the chiral determinant can be made positive.
  - **(b) Gravity.** Check whether the lattice Euclidean Einstein–Hilbert (Regge) weight is bounded below, and how the known lattice-gravity phases avoid the conformal mode.
  - **(c) Reflection positivity.** Check reflection positivity for (a) and (b) together.
  - **(d) Wording.** State the resulting price against the exact Admissibility text (`MINIMAL_AXIOMS_2026-06-29.md:57-73`).
- **FIXED readings** (derivation):
  - **DERIVED:** a proof, under stated hypotheses, that no positive, normalizable, reflection-positive, W(B4)-covariant nearest-neighbour Gibbs weight on Z⁴ carries (i), and/or (ii). Then name the price: "probability distribution" becomes "weight", and/or "nearest-neighbour" becomes "quasi-local".
  - **SUGGESTED:** argued from the known results without a proof in the stated class.
  - **REFUTED:** an explicit positive, reflection-positive, W(B4) weight carrying (i) and (ii).
- **Expectation.**
  - (i): DERIVED for nearest-neighbour couplings (Nielsen–Ninomiya plus tastes); the chiral phase is SUGGESTED.
  - (ii): SUGGESTED (the conformal factor).
  - Net: set B pays an extra Admissibility price.

---

**R2-5: the arrow of time in the state** (decides whether set B is compatible with Record)

- **Plain question.** A finite-symmetry law that keeps an arrow of time has a preferred frame (Lemma E, refereed with a convex cone). So in set B the arrow cannot be in the law. Can "Records form … records are permanent" (`MINIMAL_AXIOMS_2026-06-29.md:77-80`) then hold as a property of the state or a boundary condition?
- **The conditions.** Under a time-reflection-symmetric, whole-law B4⁺ rule, can the following hold together?
  - (i) The record count does not decrease toward one time direction, with probability ≥ 1 − δ over cosmological spans.
  - (ii) Records, once formed, never un-form.
  - (iii) The state induces matter-sector Lorentz violation of size at most (state energy density)/M_Pl⁴, with no natural-size u^μ operator in the law.

  And does "permanent", read in a block (4D) sense, impose a law-level arrow?
- **Probes.**
  - **(a) Text.** List every time-oriented word in the four axioms and the Qualification: "form", "permanent", "locks", "when present", "a state is a configuration of records". Give a time-symmetric block reading of each, or show that none exists.
  - **(b) Toy.** Build a 1+1 Euclidean, time-reflection-symmetric Gibbs model with an absorbing "locked" value, a low-record boundary at t = 0 and no future boundary. Measure monotonicity of the record count, permanence, and whether conditioning on the boundary reproduces a forward arrow without any oriented coupling.
  - **(c) Induced Lorentz violation.** Estimate the Lorentz-violating coefficients induced by a state that carries an arrow, i.e. a thermal or cosmological state. Compare them with the F1 bounds.
  - **(d) Prior art.** Compare with the Past-Hypothesis literature, and with repo notes on the arrow and on record formation (count once).
- **FIXED readings** (derivation):
  - **DERIVED:** under stated hypotheses, the arrow can sit in the state, with (i)–(iii) bounded.
  - **SUGGESTED:** argued only.
  - **REFUTED:** a proof that Record's formation or permanence clause forces a law-level time orientation, for example because "form" needs an oriented transfer step. Lemma E would then put set B back in class I. Record that as "B is incompatible with Record as written".
- **Expectation.** SUGGESTED for the block reading, with a real risk of REFUTED if "records form" is irreducibly dynamical.

---

**R2-6: Snyder coordinates, discrete space with exact Lorentz symmetry** (decides whether a fourth set D exists)

- **Plain question.** In Snyder's 1947 algebra, the spatial coordinates have discrete spectra (step a) while exact Lorentz symmetry is kept. The price is deformed translations: a curved (de Sitter) momentum space, and a non-additive, non-associative composition of momenta. It is the only known way to have discrete space and exact Lorentz symmetry together. Does it survive the round-1 observations?
- **Prior art.** There are no repo hits. Count O2's SUGGESTED Snyder row once, and RB's torus-only scope.
- **Probes.**
  - **(a) Spectrum.** Confirm the spectrum of x_i and its covariance, and state what "discrete" means for a moving observer.
  - **(b) Dispersion.** Find the one-particle dispersion and the dimension-5 and dimension-6 terms at a = ℓ_P. Compare them with LHAASO: E_QG,1 > 10 E_Pl and E_QG,2 > 6e-8 E_Pl.
  - **(c) Composition.** Take the composition law (the Battisti–Meljanac coproduct) and find its N-body scaling for macroscopic bodies, i.e. the soccer-ball problem. Find the equivalence-principle violation for the MICROSCOPE test masses (1e-15) and for Earth and Moon (LLR, 1e-13).
  - **(d) Soft theorem.** Run Lemma W with non-additive composition: does a consistent massless spin-2 soft theorem exist?
  - **(e) Boost wall.** Does RB or C3's obstruction apply on a de Sitter momentum space?
  - **(f) Finite fibre.** Can Snyder's structure sit on an M₂(C)-per-site fibre at all, given Lemmas S and G and Reeh–Schlieder?
- **FIXED readings.**
  - **PASS:** an explicit Snyder-type rule with a = ℓ_P that meets (b) and (c) numerically, has a consistent soft spin-2 coupling (d), and resolves the soccer-ball problem by a local rule.
  - **FAIL:** a proof that the deformed composition violates MICROSCOPE or LLR at a = ℓ_P for macroscopic bodies, or that no consistent soft spin-2 coupling exists.
  - **INCONCLUSIVE:** otherwise, including a resolution that needs a deformation scale depending on N (a non-local rule).
- **Expectation.** FAIL for composition per constituent. INCONCLUSIVE if the deformation scale is allowed to scale with body size.

---

**Priority order** (most decisive first): R2-1, R2-2, R2-3, R2-4, R2-5, R2-6.

**Dependencies.**
- R2-2 uses Q1's Lemma E and Lemma F only as motivation. Its N-Q proof stands on its own hypotheses.
- R2-4 and R2-5 matter only if R2-1 does not return COLLAPSES-TO-A or FAIL. They can run in parallel with it.

**Deferred:**
- edgeless sources for route E (R2-2 covers E in general);
- the RG stability of set C's tuning count;
- the FS supercharge rule as a gravity coupling.

### C5 Round 3 (pre-registered 12:30Z; launched now)

**Why this round.** Round 2's R2-2 worker built a candidate: the Lorentz-random lattice (LRL). Its referee is still running. LRL is X = g(L₇ + u), with g Haar-random in SO⁺(1,3)/Γ_L and L₇ = diag(√7,1,1,1)ℤ⁴.
- It is Lorentz-invariant in law.
- Each realization is a crystal whose reciprocal vectors satisfy |G²| ≥ c > 0, with no null reciprocal vectors.
- So in-band scattering vanishes exactly, for couplings that are covariant functionals.
- Each realization is invariant under the infinite integral Lorentz group Γ_L, which is Zariski-dense in SO(1,3).

**The supervisor's own thread (worker-unchecked, same family).**
1. Zariski density means every polynomial invariant tensor of Γ_L is Lorentz-invariant. So a Γ_L-covariant law has no Lorentz-violating operator at any polynomial order, in each single realization. This would beat set B's dimension ≤ 4 protection.
2. By O1's Lemma C′, a summable Γ_L-covariant law does not exist. Orbit counting in H³, however, suggests that power-law couplings ~|x|_E^{-s} with s > 2 give convergent Γ_L-invariant (Poincaré-series) laws. If so, the price is quasi-locality with power-law tails, not full non-locality.
3. Per-realization momentum is conserved modulo the dual lattice. In-band (low-energy) processes therefore conserve exact momentum, and the C3/RB defects can only live at Planck-scale momenta.

Each of these is tested below. Round 3 runs whatever the R2-2 referee rules on LRL. If the referee rejects LRL's basic claims, the affected items are reported as conditional.

**R3-1. Γ_L-covariant laws on L₇: existence, locality, per-realization EFT.**
- (a) Construct Γ_L-invariant quadratic and interacting matter laws on L₇ realizations as Poincaré-type orbit sums. Prove or refute convergence for kernels with power-law decay s > s_c, and find s_c. Check numerically with orbit counting.
- (b) Is every per-realization effective operator Lorentz-invariant at every polynomial order (Zariski density)? Exactly what survives, including non-polynomial and umklapp effects at |G²| ≥ c?
- (c) Per-realization momentum conservation mod dual lattice. Is the low-energy S-matrix exactly Poincaré-covariant below the Bragg gap? Do the C3/RB/RFW obstructions apply, given only discrete boosts with continuous boosts emergent?

Readings:
- **PASS:** an explicit convergent Γ_L-covariant law with power-law (or better) couplings whose per-realization low-energy physics is Lorentz-invariant at all polynomial orders, proved.
- **FAIL:** proved non-convergent for every decay class, or per-realization Lorentz violation at dimension ≤ 4.
- **INCONCLUSIVE:** otherwise.

Expectation: PASS for (a) at s > 2, and for (b) at polynomial order. Non-analytic and umklapp terms are suppressed below the gap. INCONCLUSIVE on (c).

**R3-2. Gravity on LRL.**
- Do the obstructions that killed the grid (C3 Hessian anomaly, K1 11 forms, V3 E_g shear) survive on a Γ_L-covariant substrate?
- Count Γ_L-invariant quadratic forms for a symmetric tensor h_μν. Expectation: only the Lorentz-invariant ones (Fierz–Pauli mass forms, the EH kinetic term and the non-gauge-invariant Lorentz-invariant kinetic forms). That would drop K1's 11 to the Lorentz count.
- Is there an exact linearized gauge identity for matter on L₇ with Γ_L-covariant couplings (the R2-1 Theorem T analogue)? Note: per realization, translations are discrete, so does Theorem T's tower argument bite?
- Does the free E_g shear distinction collapse because Γ_L has no cubic E/T2 split?

Readings:
- **PASS:** a Γ_L-covariant matter + graviton law with an exact linearized gauge identity, or with a tuning count ≤ the Lorentz-invariant count (graviton mass + cosmological constant only).
- **FAIL:** the R2-1-type tower is forced, or the count does not improve.
- **INCONCLUSIVE:** otherwise.

Expectation: the count collapses to the Lorentz count (an improvement: no speed or anisotropy tunings). The exact gauge identity still hits a Theorem-T analogue, since per-realization translations are discrete. INCONCLUSIVE, leaning a partial PASS.

**R3-3. LRL propagation, lensing and curved spacetime.**
- (a) The mean link or propagator kernel on LRL, compared with RL2's √Δ result for Poisson.
- (b) Is there a natural curved-spacetime version, e.g. a locally arithmetic lattice in a frame field, or a quotient/orbifold construction? Do curvature defects bring noise back, and at what size (a/L_curv)²?

Readings:
- **PASS:** the mean propagation reproduces GR focusing, and curvature-induced noise is below RZ's bar for physical lenses.
- **FAIL:** an O(1) mismatch, or curvature noise above the bar.
- **INCONCLUSIVE:** otherwise.

Expectation: INCONCLUSIVE. Curved space is the main obstacle.

**R3-4. Set A's gravity escape: which of E1–E4 is cheapest and still viable?** (From R2-3: worker FAIL (bounded); its referee is still running.)
- Compare against observations: metric jumps on state-chosen surfaces (Juárez-Aubry–Kay–Sudarsky), classical-quantum gravity (Oppenheim et al.; decoherence/diffusion trade-off bounds), Bell-type beables with a guidance foliation, and Kraus operators dressed to infinity.

Readings, per escape:
- **VIABLE:** passes current bounds with stated prices.
- **EXCLUDED:** violates a stated bound.
- **OPEN:** otherwise.

Expectation: CQ gravity is constrained but viable in a window. Metric jumps are viable but need a foliation. Beables are viable with a foliation (a preferred frame in the guidance law only).

### C5 Round 2 results (recorded 12:52Z)

All verdicts are from codex gpt-5.6-sol at xhigh. Files: `agents/C5_R2-*`. The R2-1 referee died on a stream error and was relaunched; it is pending.

**R2-2 (Lorentz-invariant discreteness) — CONFIRMED WITH CORRECTIONS. N-Q′ and P-L′ are DERIVED; LRL is a genuine in-band gap.**
- **N-Q′.** Take positive energy, an invariant vector, and covariant nonnegative integer counts with finite vacuum second moments, vacuum-level commutativity and temporal-halving additivity. Then every count annihilates the vacuum.
- **P-L′.** Every stationary integer-valued random measure with ρ > 0 and finite second moments has Bartlett weight in every cone about every hyperplane, so it has spacelike weight. Neither result places that weight in a prescribed band.
- **The cocompact arithmetic L₇ ensemble (LRL)** has three properties:
  - it is Poincaré-invariant in law;
  - it has a uniform hard core;
  - it has no Bragg support for 0 < |q²| < (2π)²/7, or on the nonzero null cone.

  This is a genuine in-band spectral gap and ideal one-to-one Bloch silence.
- **Not established:** an all-orders observational pass of the RZ bar, or a viable event route. Still open are steering, finite-source and curved propagation, inelastic sectors, convergent effective dynamics, and the per-realization O1 bounds.

**R2-3 (record flashes vs gravity) — NOT CONFIRMED as FAIL, so INCONCLUSIVE.**
- **Proved for one collapse surface.** A spatially decaying stress jump confined to one non-compact collapse surface gives a non-integrable non-conservation current. So neither semiclassical Einstein gravity nor its unimodular form admits it as a global distributional solution without a compensator or a metric-reset rule.
- **Heating formulas are exact.** At the Earth-heat limit, an isolated pointer is limited to about 20 s⁻¹. Environmental amplification can exceed 10³ s⁻¹.
- **GW signals:** negligible.
- **Bounded FAILs** hold for bare, independently flashing position laws.
- **Not excluded:** non-local gravitationally dressed operations, relativistic collective or coloured laws, and other compensators.

**R2-4 (set B weight) — CONFIRMED WITH CORRECTIONS. DERIVED, through gravity.**
- **Assumptions W1–W3:** a positive source-tilted measure, real local source functionals, and an isotropic unscreened 1/p² response.
- **Result.** The trace projector forces a ≤ 1/3, i.e. γ ≤ 1/2. GR needs a = 1/2, so GR cannot arise from a positive local Gibbs realization.
- **Escapes:** non-real or non-local bridges.
- **No class-wide chiral no-go:**
  - Nielsen–Ninomiya covers only the free exact-chiral class.
  - Positivity forbids CKM CP only if the reconstructed antiunitary symmetry is unbroken and acts within the ordinary SM sector.
  - The Hammersley–Clifford pair-only reading needs a strictly positive Markov field. It does not follow from the literal wording.

**R2-5 (arrow in the state) — CONFIRMED WITH CORRECTIONS. SUGGESTED.**
- **Proved, for classical non-negative nearest-neighbour slice transfer laws** with a bond-reflection-positive twisted kernel and a θ-equivariant record map. Strict support-level permanence then forbids every formation step that has a reachable predecessor and a forward-continuable target. Only boundary-only formation survives.
- **Not a universal incompatibility between B and Record.** Outside the theorem: non-RP tagged laws, probabilistic permanence, non-commuting quantum slices, non-nearest-neighbour laws, and OS-reconstructed real-time records.

**R2-6 (Snyder) — CONFIRMED WITH CORRECTIONS. FAIL (bounded).**
- **Assumptions:** the canonical Snyder transvection product; a standard unitary Lorentz-invariant S-matrix with a massless helicity-2 particle; generic support; leg-local soft poles; the exact Ward-residue identity.
- **Result.** The Snyder total does not factor through an additive charge, so the coupling vanishes. Set D does not exist in this class.
- **Open:** braided or non-leg-local soft structures, extended momentum spaces with an abelian quotient, and non-particle gravity.

### C5 Round 2 addendum: R2-1 referee (recorded 13:07Z)

**R2-1 (multi-band / perfect action on Z⁴) — CONFIRMED WITH CORRECTIONS. COLLAPSES-TO-A, bounded, in the one-particle/spectral sense only.**
- **Hypotheses.** A quasi-local Z⁴ law with an unbroken additive asymptotic charge on the same interacting simple scalar band. Near-threshold dispersion that is nondegenerate and analytic, d ≥ 2. One-particle charge and Hamiltonian matrices that are globally periodic, real-analytic and finite-dimensional, or scalar W(B4) parity removing the energy admixture. The referee added these last premises; the report used them without stating them.
- **Result.** Under these hypotheses, the constant-ξ Ward identity forces τ = aω + b·k + e with b ≠ 0. Analytic continuation then gives a fixed finite matrix infinitely many characteristic roots. So a finite one-particle fibre is impossible.
- **Not proved.** That the site ontology must itself be a continuum, or that the exact pure-point ladder is universal.
- **Perfect-action numerics** reproduce, but the Gaussian time-blocked covariance fails OS reflection positivity: two minors are negative, −2.25e-3 and −1.83e-4. So its poles are Euclidean poles, not established physical states.
- **Whitney blocking** is exact for arbitrary regular ξ at κ⁰.

### C5 Round 3 results (recorded 13:07Z; R3-1 referee pending)

**R3-2 (gravity on LRL) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE; neither fixed disjunct is met.**
- **The count drops from 11 to 5,** given a Γ-covariant quadratic graviton action with a symmetry-preserving expansion through q². There are 2 mass forms and 4 kinetic forms, with one gauge-invariant combination.
- **The cubic E/T2 shear split disappears.** μ_E = μ_T2 leaves one spin-2 masslessness coefficient. It is tuned, not symmetry-enforced.
- **A tuned massless TT pole** has the background cone, with no independent speed coefficient.
- **Theorem T_Γ.** A nonzero four-vector gauge charge cannot be bounded under a unitary Γ action, even for free matter. But this does not force a tower: singular finite-fibre multipliers remain open. Hypothesis (C) is natural, not implied.
- **Lemma A.** Invariant nonzero scalar couplings repeat without decay along unbounded orbits. That refutes uniform power-law tails. The discrete-shell 1/q² claim is unproved.
- **Scalar sector.** c₂/c₁ = −(a+b)/(4a+3b), so GR generically needs b = −2a: one more matching condition.

**R3-3 (LRL propagation and curvature) — worker INCONCLUSIVE; not refereed (no FAIL or no-go claimed).**
- **The mean link kernel** is the massless retarded kernel at long range, with corrections of order (a/r)².
- **BD weights fail on LRL**: the 1/k² term survives. RL2's √Δ proof uses a Poisson-only property, so it does not transfer.
- **A single realization** differs from the mean by 30–40% of Poisson scatter. The difference is smooth, in band, and frame-dependent: a deterministic anisotropy.
- **Focusing.** If an action-derived second-order effective law exists with density equal to volume, it is □_g + V, which focuses like GR per realization (proved given the law).
- **Curved spacetime.**
  - An exact de Sitter/AdS LRL exists, but integer forms have null pairs; avoiding them needs ℤ[√2].
  - Generic curvature needs dislocation defects. Under an assumed defect model, the disorder fraction is about 4e-62 (galaxy) to 3e-40 (neutron star). That is ≥ 30 decades below RZ's bar (suggested).

**R3-4 (set A gravity escapes) — NOT CONFIRMED as stated. Refereed per-escape readings:**
- **E1** (metric jumps, JKMS): OPEN.
- **E2** (CQ gravity): OPEN. Ultra-local continuous Newtonian CQ is EXCLUDED by the 32-decade empty window. A diffeomorphism-invariant CQ-GR candidate exists.
- **E3** (fixed-foliation equilibrium beables): VIABLE in explicit preferred-foliation scope only. Its interacting-QFT completion is OPEN.
- **E4** (dressed Kraus operators): OPEN.
- **E5** (reservoirs): OPEN. The 2.4 eV emission bound is wrong: it uses rms spread for |Δ⟨P⟩|.
- **Lemma P** holds under compact-spacetime-support and finite-momentum premises. It does not establish those premises for persistent rGRWf changes.
- **Lemma F** (a reservoir rest frame) is not proved.
- E3 is not shown to be uniquely cheapest.

**R3-1 (laws on one LRL realization) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE.** Referee verdict recorded 13:33Z.
- **Lemma M holds.** Invariant L² scalar torus symbols are constant. Vector and tensor fields also hold, by the second-moment argument. Spinors need a specified Spin lift. So nonzero invariant hopping kernels are non-summable and do not decay along their infinite orbits.
- **Prop. P:** s_c = 2 is correct, but the convergent Poincaré series defines a finite orbit weight, not a convergent hopping operator. "Power-law quasi-locality" is refuted.
- **Prop. R.** A nonzero past-timelike, polynomially bounded kernel converges absolutely exactly in the forward tube. Spacelike and time-symmetric kernels have no ordinary Fourier series; distributional forms remain possible. Retardation gives an arrow without a rest-frame vector.
- **Polynomial invariants** have degrees 1–6 with counts 0, 1, 0, 1, 0, 1. There are two mass structures.
- **"No Taylor expansion at p = 0"** is too broad. Only global L² regularity and full-cone analyticity are excluded.
- **Per-realization direction dependence at imaginary momentum is genuine** continuous-Lorentz breaking of the tube symbol. But the fitted exponent is unstable (slopes 0.61–2.28), so neither κ^1.3 nor a non-shrinking absolute LV is established. It is a diagnostic, not yet observable LV.
- **Momentum.** Resonance counts reproduce. Exact in-band momentum conservation is false: multiparticle umklapp can use low individual momenta whose total transfer is reciprocal. The gap protects 1→1 processes and processes whose total transfer stays in the gap. The boost-wall theorems do not apply as quoted, and they are not refuted.

### C5 Round 4 (pre-registered 13:08Z; launched now)

**Why this round.** Round 3 left LRL as the live candidate for set B′: a Lorentz-invariant-in-law substrate.
- Its graviton count improves conditionally from 11 to 5.
- It is blocked on three open points:
  1. Does a per-realization long-wavelength effective law exist (R3-1, R3-3)?
  2. Do singular finite-fibre multipliers allow an exact gauge identity (R3-2)?
  3. How large are the per-realization anisotropy and the Bragg-resonance effects at physical energies?
- On set A, E3 (beables) is the one explicit VIABLE route, and its interacting completion is OPEN.
- Λ has not been tested in any set.

Five probes; the R3-1 referee may narrow R4-1 and R4-3. **R4-1. An LRL-specific d'Alembertian and the per-realization effective law.**
- Build non-local weights on L₇ realizations: layer weights over the seven proper-time shells and beyond, analogous to BD for Poisson. Their ensemble mean should give □ + O(a²□²) with no 1/k² remnant.
- Then measure the per-realization deviation from the mean as a function of the smearing scale ℓ ≫ a. Is the anisotropy suppressed by a power of a/ℓ, exponentially by the Bragg gap, or not at all?

Readings:
- **PASS:** explicit weights whose mean is □ to O(a²) and whose per-realization deviation falls at least as (a/ℓ)², checked.
- **FAIL:** no weights cancel the remnant, or the per-realization deviation stays O(1) relative as ℓ grows.
- **INCONCLUSIVE:** otherwise.

**R4-2. Singular finite-fibre multipliers (from the R3-2 referee).**
- Can a finite-fibre matter representation on an LRL realization carry an unbounded, non-zero four-vector Γ-charge through singular multipliers? If so, construct the exact linearized gauge identity, giving a massless graviton without the R2-1 tower.
- If not, prove the no-go in a stated class.

Readings:
- **PASS:** an explicit finite-fibre example with an exact gauge identity.
- **FAIL:** a no-go that covers singular multipliers in a stated class (refereed).
- **INCONCLUSIVE:** otherwise.

**R4-3. Observational size of LRL per-realization Lorentz violation and Bragg resonances.**
- Use R3-1's per-realization numbers and the Bragg cones at |G²| ≥ (2π)²/7. Compute the leading effects at a = ℓ_P (and at a = 10⁻¹⁹ m) on:
  - GRB photon time delays (Fermi/LHAASO);
  - UHECR and TeV-γ thresholds;
  - vacuum birefringence;
  - Hughes–Drever and clock bounds.

Readings:
- **PASS:** every effect is below current bounds at a = ℓ_P with no tuning.
- **FAIL:** a bound is violated at a = ℓ_P.
- **INCONCLUSIVE:** otherwise, including when an estimate needs the unbuilt effective law.

**R4-4. Set A's E3 completion: an equilibrium beable theory sourcing gravity.**
- Build the most explicit interacting beable model available: Bell-type QFT, Dürr et al. (2004), with records as beable configurations; the stadium picture is a related thought, not a rule. Source a classical metric with the actual beable stress, not ⟨T⟩.
- Check:
  - Page–Geilker;
  - Cavendish-type tests in superposition (BMV and its classical analogues);
  - energy-momentum conservation;
  - whether the foliation can be wave-function-selected rather than fixed.

Readings:
- **PASS:** a stated model consistent with those tests, with the price named.
- **FAIL:** a test excludes the model class.
- **INCONCLUSIVE:** otherwise.

**R4-5. Λ from the record count (everpresent Λ).**
- The record count rises (owner's thought, tested only as a hypothesis). In unimodular form, Λ is conjugate to 4-volume, i.e. to the count.
- Derive the fluctuation δΛ ~ N^(−1/2) for each set (A: records only; B/LRL: lattice sites; C: 3D grid with ticks).
- Confront the result with current data: Sorkin's model and the fits of Zwane–Afshordi–Sorkin, from memory or a verified source.
- Does any set give the observed magnitude without tuning and survive the data?

Readings:
- **PASS:** a set gives |Λ| of the observed order without tuning and is consistent with the CMB/BAO constraints as stated.
- **FAIL:** every set gives the wrong order or is excluded by data.
- **INCONCLUSIVE:** otherwise.

Prior-art note: everpresent Λ appears in this packet only as a comparator or suggestion (`TESTS.md:159`, `agents/supervisor_thread.md:53,149`, `agents/C5_O3_report.md:99`). It has never been tested. The repository's `docs/COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md` and the docs on the cosmological constant must be read first.

### C5 Round 5, first item (pre-registered 13:34Z; launched now)

**R5-1. Composite particles on an LRL realization (the escape left by R4-2, whose referee is pending).**
- R4-2 (worker) finds that states made by finite-variance on-site operators carry no covariant charge and do not propagate. So any particle on LRL must be a composite that only multi-site operators create, or must live in a state that breaks Γ.
- Construct a candidate:
  - a multi-site (link, plaquette or orbit-smeared) operator family on L₇, or a Γ-breaking state with a restored-in-law symmetry;
  - its two-point function;
  - whether it has a decaying correlation with a dispersion relation and a covariant momentum.
- Prove a no-go in a stated class if none exists.

Readings:
- **PASS:** an explicit composite (or symmetry-broken-state) excitation with a dispersion and a covariant charge, checked.
- **FAIL:** a no-go for multi-site operators of bounded support, or for every Γ-breaking state, in a stated class (refereed).
- **INCONCLUSIVE:** otherwise.

### C5 Round 5, items 2–3 (pre-registered 13:40Z; launched now)

**R5-2. Infinite-orbit kernels on LRL: can a per-realization effective law exist at all?**
- The R4-1 worker (unrefereed) finds a ban: for retarded kernels supported on finitely many Γ_L orbits, the per-realization deviation grows as (ℓ/a)³ relative to □φ. The open escape is kernels on infinitely many orbits, with weights tending to zero along the shell index m.
- Construct such a kernel. One option is to choose f_m so that the infinitely many mode conditions A_j(f) = 0 hold, e.g. via Hecke operators or a theta lift with no cusp/Maass components. Or prove that none converges in the forward tube.

Readings:
- **PASS:** an explicit infinite-orbit retarded kernel whose mean is □ to O(a²) and whose per-realization rms deviation falls at least as (a/ℓ)², checked.
- **FAIL:** a no-go covering every infinite-orbit kernel with convergent tube symbol (refereed).
- **INCONCLUSIVE:** otherwise.

**R5-3. The mean of Λ: can any set make ⟨Λ⟩ = 0 without tuning?**
- R4-5's worker (unrefereed) finds that ⟨Λ⟩ = 0 is a premise in every set. That is the old cosmological-constant problem.
- Take the routes that touch the axioms:
  - unimodular gravity with Λ as an integration constant fixed by a boundary or record condition;
  - Baum–Hawking/Coleman probability peaking at Λ → 0;
  - a self-tuning or sequestering mechanism (Kaloper–Padilla), with the count as the global variable;
  - a record-formation equilibrium that sets the vacuum stress to zero (owner's thought "count rises until frozen", tested as a hypothesis).
- For each, derive what the axioms supply and what must be added, and check it against observation: w(z), and the effect of DESI DR2 hints, verified or labelled from memory.

Readings, per route:
- **VIABLE:** gives ⟨Λ⟩ = 0 (or the observed value) with named prices and no fine tuning, consistent with stated bounds.
- **EXCLUDED:** violates a stated bound or is internally inconsistent.
- **OPEN:** otherwise.

### C5 Round 4 results (recorded 14:05Z)

All five were refereed by codex gpt-5.6-sol at xhigh. Files: `agents/C5_R4-*`.

**R4-1 (LRL d'Alembertian) — CONFIRMED WITH CORRECTIONS. FAIL (bounded).**
- **Weights.** Four-shell retarded weights exist whose Haar mean is −k² + O(a²k⁴ log ak). The Siegel densities are confirmed independently, with class number one proved by the square-free-determinant theorem.
- **No per-realization law from finitely many orbits.** Every fixed linear retarded scalar kernel on finitely many Γ_L orbits with a nonzero off-site weight obeys, on isotropic Gaussians at a Palm point, limsup_ℓ ‖Bφ_ℓ − E Bφ_ℓ‖₂/ℓ > 0. Hence limsup R_ℓ(a/ℓ)³ > 0: the per-realization deviation does not vanish relative to □φ. The absolute deviation grows too, so this is not a normalization artefact.
- **Scope.** It is an ensemble-rms obstruction, not pointwise for every realization. It does not cover infinite-support, nonlinear, curved or internal-index operators.
- **Corrections:**
  - the frame sampling covers a local ball, not Haar on the quotient;
  - there are 18 + 6 kernels, not 23;
  - the r = 0 mode grows as ℓ log ℓ;
  - the clause "stays O(1)" must be read as "does not vanish".

**R4-2 (singular finite-fibre multipliers) — CONFIRMED WITH CORRECTIONS. FAIL (bounded) for the conservative class; INCONCLUSIVE for propagating dissipative matter.**
- **The conservative class.** Take a unitary Γ⋉L₇ one-particle representation with finite spectral multiplicity, closed decomposable charges forming a finite rational multiplet, and spectral support conservative for the three coordinate boosts. Then every nontrivial Lorentz component of every measurable finite-fibre charge vanishes.
- **On-site operators stay in that class.** Strictly on-site bounded operators acting on an invariant vacuum generate it. Its two-point measure is ultralocal Haar plus uniformly almost-periodic, so there is no continuous dispersive branch.
- **The dissipative escape (Example E).** The folded continuum hyperboloid gives a covariant, unbounded, multiplicity-one charge, but no lattice law and no local gauge identity.
- **Corrections:**
  - S′ needs a Lie-algebra argument over the three coordinate boosts;
  - Qubit makes variance automatic only for represented on-site M₂ elements;
  - "no propagation" should read "no continuous dispersive branch".

**R4-3 (observational LV on LRL) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE.**
- **Margins.** At a = ℓ_P, every listed process is 27.2–44.2 decades below the gap. At a = 1e-19 m, LHC and UHECR-air invariants lie above it, which opens umklapp channels but does not size them.
- **Lemma Z, confirmed in its continuous form.** Γ_L orbits on the punctured null cone are dense in direction and scale. So scalar invariants on the spacelike-plus-null domain depend only on p², and regular null/spacelike per-realization LV is excluded. Bounded timelike mass-like branches and singular Bragg-cone sectors stay open.
- **Not confirmed:** thresholdless emission. Exact kinematics need d_H(v,v′) = |log m(v)/m(v′)|.
- **The instability of the representative five-shell kernel is genuine.** It has a forward-tube zero at κ ≈ 0.46–0.50, with an e-folding time of about 2 lattice times. The second zero, the optimized families and the universal exponent are not robust.
- **The correction to R3-1 is confirmed.** 55 of 66 shell pairs have |c| > 0.9.

**R4-4 (beables sourcing gravity) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE.**
- **Literal C0 is ruled out.** Bare localized beable stress cannot source linearized Einstein or trace-free gravity when the Bohmian momentum changes. Lemma K needs o(r⁻²) fall-off.
- **Naive CQ is ruled out.** Adding the realized quantum-potential energy does not restore run-wise conservation for generic states.
- **CG is an incomplete proposal, still open.** The ghost has not been derived from an action, and signalling is shown only in the ideal 1D toy (TV 0.794 reproduced).
- **The LLR seven-decade exclusion is not established.** Pauli/Dirac currents make the 1s state circulate, which cuts the deficit to −4.5 eV in the same bookkeeping. No many-electron calculation was done.
- **Lemma N confirmed.** A classical c-number channel gives zero entanglement; the quantum value is concurrence 0.156.
- **R is viable, outside beable-sourced gravity.** It is a non-back-reacting E3 comparator: gravity quantum, beable metric inert. DGNSZ gives a covariant foliation only for timelike total momentum (not the vacuum, not null states).

**R4-5 (everpresent Λ) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE.**
- **The observed order arises under three conditions:** unimodular conjugacy, a count-volume bridge, and a Poisson-like 4D count at Planck density. The past cone of 6.389e242 ℓ_P⁴ then gives 1.389 Λ_obs, with a convention range of 0.695–34.9. Neither the coefficient nor the zero mean is derived.
- **Set A:** matter-following GRW flashes are vastly too sparse. Even the report's generous scenario gives about 3.3e-72 Λ_obs, and this is not a class-wide bound.
- **The axioms' Z³ (set C):** a fixed persistent Z³ allows at most 8.24e184 record events in the stated embedding. The 4e-28 figure needs extra assumptions.
- **A crystal's count variance depends on the frame** (confirmed).
- **LRL:** sub-volume-like through T = 108, compatible with the gap and P-L′. The asymptotic law is unsettled; Lemma V is open.
- **Data and consistency:** a Bianchi-completion problem (a 17-decade gap) and CMB problems. Neither excludes the whole class.
- **No contradiction with the Λ = 3/R² note.** That note is conditional.

### C5 Round 5, item 4 and mid-campaign synthesis (pre-registered 14:07Z; launched now)

**R5-4. A law on timelike-link cells that generates a mass shell (the class R5-1's worker leaves open; its referee is pending).**
- Put finite-dimensional degrees of freedom on timelike links (or Lorentzian simplices) of an L₇ realization, with non-commuting timelike structure. Give them a Γ⋉L₇-covariant law: quasilocal on links where possible.
- Does any such law have a one-particle mass shell with a decaying two-point function and a covariant positive-energy momentum, without supplying a continuum field as data?
- Candidates:
  - a quantum walk or transfer matrix on the link graph;
  - a Gaussian (free) link field with covariant link-link couplings;
  - a link "spin foam" amplitude.

Readings:
- **PASS:** an explicit link law, not continuum-supplied, with a mass shell and a covariant charge, checked.
- **FAIL:** a no-go covering quasilocal covariant link laws in a stated class (refereed).
- **INCONCLUSIVE:** otherwise.

**S5. Mid-campaign synthesis** (same family; it gives no verdicts).
- Read all C5 results through round 4, plus round 5 as available.
- State what is now forced, what is dead, and what is open for sets A, B, B′ (LRL) and C.
- Rank the next decisive tests, with the big open problems first-class.
- Draft round-6 pre-registrations with fixed readings.

### C5 Round 5 results, part 1 (recorded 14:18Z)

**R5-1 (composites on LRL) — CONFIRMED WITH CORRECTIONS. FAIL, bounded to the corrected stated classes.**
- **Supports with infinite stabilizers carry nothing.** On L₇, take any finite-dimensional covariant operator family whose support has an infinite pointwise stabilizer: qubit operators on a point, a spacelike line or a spacelike plane (Lemma K). Such a family:
  - has no massive or massless shell component;
  - has Haar-a.c. correlations confined to the stabilizer-fixed spacelike sublattice; the singular part is uncontrolled;
  - gives zero to any decomposable covariant positive-energy four-charge.
- **Theorem Q.** Continuous full-Γ event rules, past-cone rules included, are condition-independent, and full DLR versions are products.
  - An arbitrary retarded kernel need not give a product joint law.
  - Q does not directly refute Admissibility as written: the axiom concerns Z³ with nearest neighbours, not L₇. An explicit bridge would be needed.
- **Proposition L.** Strict locality excludes fixed-mass content only under (SC_m), a strong extra hypothesis that Bragg relifts evade.
- **Lemma H.** A measurable frame-picking state cannot be restored by invariant averaging.
- **Example D (reproduced).** A continuum field smeared on timelike links is consistent but imports set A.
- **Open:** finite-stabilizer link cells with non-commuting timelike structure, under a genuinely LRL-generated law. R5-4 is running on this.

**R5-2 (infinite-orbit kernels):** worker INCONCLUSIVE; referee running (launched 14:16Z).

**R5-3 (the mean of Λ) — CONFIRMED WITH CORRECTIONS. All four routes OPEN; no untuned, observationally viable derivation of ⟨Λ⟩ = 0 exists in the campaign.** Referee recorded 14:33Z.
- **Lemma PT holds within G1–G3:** a Levi-Civita metric theory with conserved true matter stress. There, a prescribed c-number vacuum subtraction cannot protect the geometry across phase transitions. The electroweak shift alone needs cancellation to about 1 part in 4.7e54.
  - G1–G3 is not complete. It leaves out global constraints, four-form fluxes, dynamical compensators, symmetries, modified gravity and exchanging sectors.
- **Route 3 (sequestering).** The original global Kaloper–Padilla ⟨R⟩ = 0 rule is EXCLUDED, bounded to its class: global, homogeneous, finite endpoints, no extreme loitering. Lemma S gives |Ω_k0| ≥ 0.917 for a ΛCDM-like past; 241.6 a0/H0 of loitering would be needed. This does not extend to local or Gauss–Bonnet sequestering.
- **Route 2 (Baum–Hawking/Coleman).** The weight e^{3π/GΛ} is non-normalizable, so it is a formal weight, not a probability. Polchinski's phase reverses its sign.
  - R2-4 excludes a positive full W1–W3 measure, but not a marginal prior on a global constant.
  - The fixed-count "saddle" Λ* = √(24π²/V) is not a controlled saddle.
- **Route 4 (records forming until frozen).** The Gibbs–Duhem objection is confirmed. Forming records leave an additive constant unfixed, and formation may stop before the minimum. Coupling gravity to ε − μn needs an extra q-type source rule.
- **Curvature data.** DESI DR2 gives 10³Ω_K = 2.3 ± 1.1. The 0.002 figure is a benchmark, not the DESI interval.

### C5 Round 5, item 5 (pre-registered 14:19Z; launched now)

**R5-5. The ensemble-only LRL law: a superposition over lattice frames (price (iv) in R5-2's worker report).**
- R4-1 (refereed) and R5-2 (worker) find that a single LRL realization has no long-wavelength □ from finite-orbit kernels, and none from the natural infinite ones. The ensemble mean does have □.
- Suppose the substrate frame g ∈ SO⁺(1,3)/Γ_L is itself a quantum degree of freedom in superposition, so that only the frame-averaged law is physical.
- Does matter propagation **decohere** the frame, selecting a realization, so that per-realization physics returns? Or does the frame stay coherent, so the mean law is what is observed?
- Compute the frame-which-path information that a propagating particle writes, as a function of ℓ and the time of flight. Use the refereed per-realization deviations (R4-1) as the coupling.
- Relate this to Q1, the traced-out substrate (FAIL for the plain Poisson version), and to O4's visibility bound V ≤ BC.

Readings:
- **PASS:** the frame stays coherent for all observed propagation (decoherence rate below stated bounds), so the ensemble □ is the observed law, with prices named.
- **FAIL:** propagation decoheres the frame within observed scales, so per-realization physics, and the R4-1 obstruction, return.
- **INCONCLUSIVE:** otherwise.

### C5 Round 6 (pre-registered 14:19Z from the S5 synthesis, agents/C5_S5_synthesis.md; readings fixed as drafted below)

Launch order: R6-1, R6-2, R6-3 and R6-5 now; R6-4 when a slot frees; R6-6 only on its stated condition. Draft text verbatim from S5 §5:


**Rules (as for rounds 2–5).**
- Probes: Opus 5.5 at xhigh.
- Every FAIL, REFUTED, EXCLUDED or no-go goes to the codex gpt-5.6-sol (xhigh) referee before it is recorded.
- Prices are named, never adopted.
- Each probe greps the repository and packet for prior art first and counts each match once.
- Hypotheses are stated before titles; excluded outside realizations are listed.
- Derivation readings: DERIVED / SUGGESTED / REFUTED, as at `TESTS:2315-2318`.

**Overlap check against R5-1..R5-4.**
- R6-1 excludes LRL (covered by R5-1/R5-4).
- R6-3 concerns count fluctuations, not ⟨Λ⟩ (R5-3).
- R6-6 is conditional on R5-2 and tests stability only.

**Priority:** R6-1, R6-2, R6-3, R6-4, R6-5; R6-6 conditional.

---

**R6-1. Exact additive momentum from finite-per-site interacting laws (sets B and C; the continuum-from-qubits problem)**

- **Plain question.** Every exact-graviton route on a grid needs momentum that adds up exactly in collisions. The known obstructions are piecemeal:
  - a 1D qubit chain's shift cannot be interpolated continuously by strictly local maps (Lemma G);
  - a finite one-particle fibre cannot carry the Z⁴ Ward identity (R2-1);
  - umklapp-free interactions are impossible in analytic and meromorphic classes (RG).

  Does the obstruction hold for interacting qubit lattices in d ≥ 2? Or is there a door: a momentum defined only on scattering states, or an internal symmetry V carrying the shift's index (T = UV)?
- **Setting.** Quasi-local spin systems on ⊗_{Z^d} M₂(C), d = 2, 3, with:
  - (i) strict-range QCA paths;
  - (ii) approximately local automorphism groups with Lieb–Robinson tails;
  - (iii) Heisenberg dynamics of quasi-local Hamiltonians with nontrivial 2→2 scattering (Haag–Ruelle on the lattice).

  Euclidean B enters through the OS-reconstructed transfer matrix on Z³ × Z_τ. LRL is excluded.
- **Prior art (count once).**
  - O2 Lemmas S and G (`TESTS:2392-2394`; `C5_O2_referee_full.md:195,333`);
  - I1 referee on T = UV and GNVW/RWW conventions (`C4_I1_referee.md:15`);
  - RN2 (`SUMMARY:395`; `C4_N1_referee.md`);
  - R2-1 Theorem T (`TESTS:2748-2751`);
  - RG G1 umklapp-free classes (`TESTS:1023-1028,1080`);
  - RS (`PRICE_NOTE:323`).
- **Probes.**
  - (a) **Index in d ≥ 2.** Prove or refute that no continuous path, and no strongly continuous one-parameter group α_s with α_1 = the unit lattice shift, exists among:
    - strict-range QCAs, using flow per unit cut length;
    - approximately local automorphisms, extending RWW from 1D; state exactly which d ≥ 2 index theorem is used, or prove the needed one.
  - (b) **T = UV.** Under what conditions can an on-site-generated internal symmetry V carrying the inverse shift index commute with an interacting dynamics with nonzero scattering? Does V force an infinite on-site or one-particle structure (P10)?
  - (c) **Asymptotic-only charge.** Assume a lattice S-matrix that conserves quasi-momentum modulo the reciprocal lattice. Prove or refute: an additive ℝ^d-valued charge extending quasi-momentum on asymptotic states exists only if every umklapp amplitude vanishes. Then search outside RG's classes for a nonzero-scattering umklapp-free qubit law: integrable, kinematically constrained, or non-analytic.
  - (d) **Transfer to Z⁴.** Carry (a)–(c) to the OS-reconstructed Euclidean Z⁴ transfer matrix; state what reflection positivity adds.
- **FIXED readings** (derivation):
  - **DERIVED:** (a) and (c) proved in a stated class covering interacting finite-per-site laws in d ≥ 2. In that class, an exact graviton Ward identity on any grid set then requires the continuum. Record: "grid sets pay tuning or import the continuum (class …)".
  - **SUGGESTED:** argued only, for (a) or (c); record which.
  - **REFUTED:** an explicit finite-per-site interacting law in d ≥ 2 with nonzero 2→2 scattering and an exact additive ℝ^d asymptotic momentum, checked numerically on scattering data.
- **Expectation.**
  - (a) DERIVED for strict-range paths, SUGGESTED for approximately local ones.
  - (c) SUGGESTED.
  - Overall SUGGESTED. There is a real REFUTED risk from integrable umklapp-free sectors.

---

**R6-2. Can any set produce the graviton? A Weinberg–Witten sorting with the B′ specifics**

- **Plain question.** In every set the graviton is put in by hand. The Weinberg–Witten theorem says a Lorentz-invariant theory with a Lorentz-covariant conserved stress tensor has no massless spin-2 particle. So an emergent graviton needs one of the theorem's assumptions to fail:
  - Lorentz invariance;
  - a covariant T;
  - a particle pole;
  - locality or holography.

  Which sets can produce, rather than supply, a graviton that couples universally to matter's energy-momentum?
- **Setting.** The four sets as defined (`TESTS:2424-2428,2647-2651`). Matter: the minimal content each set's refereed results allow. Graviton: any emergent massless helicity-±2 mode.
- **Prior art (count once).**
  - `B_referee.md:47,175` (WW hypotheses and exits);
  - `OUTSIDE_VIEW.md:39`;
  - lane R on Z³: Gu–Wen and rank-2 models, the exact-constraint N-type theory live, its coupling to matter's T open (`TESTS:714-767`);
  - O2 Lemma W (`TESTS:2386-2389`);
  - R2-6 (non-additive momentum kills the soft coupling).
- **Probes.**
  - (a) Per set, state WW's hypotheses and check each against the set's refereed low-energy content: an IR Lorentz-covariant conserved T^{μν} with nonzero forward one-particle matrix elements, and particle poles.
  - (b) **B′ specifics.**
    - A realization has only Γ_L. Does WW's small-angle helicity argument go through with Γ_L alone, using Zariski density and Lemma Z (`TESTS:2925`)?
    - Does multiparticle umklapp (`TESTS:2791`) spoil the covariance of the forward matrix element?
  - (c) **B specifics.** WW concerns IR matrix elements. Does dimension-4 Lorentz protection with dimension-6 breaking (`C5_O5_synthesis.md:132`) suffice for its hypotheses?
  - (d) **C specifics.** Can the lane-R N-type graviton couple universally to matter's energy-momentum? State the minimal speed tunings: the graviton–matter Collins split (`TESTS:719`).
  - (e) **Exits.** For each exit (holography, non-particle gravity, non-covariant T as in GR's pseudotensor), say which set's axioms could host it and at what price.
- **FIXED readings, per set:**
  - **PRODUCIBLE:** a stated mechanism evades WW in that set, with universal coupling to matter's energy-momentum and the prices named.
  - **SUPPLIED-FORCED:** WW's hypotheses are shown to hold in that set's low-energy content, so the graviton must be an elementary gauge field (supplied). Referee required.
  - **OPEN:** otherwise.
- **Expectation.**
  - A: SUPPLIED-FORCED.
  - B: SUPPLIED-FORCED at the IR level, or OPEN.
  - B′: OPEN, leaning SUPPLIED-FORCED via Lemma Z.
  - C: OPEN; WW is evaded by Lorentz violation, and universal coupling is the barrier.

---

**R6-3. Lemma V: does the Lorentz-random lattice's count fluctuate like a volume? Does lensing silence exclude Poisson-size Λ fluctuations?**

- **Plain question.** Everpresent Λ gets its size from the number of events in our past fluctuating like a Poisson count. Poisson events are excluded by lensing. The Lorentz-random grid passes lensing, but its counts looked sub-Poisson through T = 108.
  - Does its count in a causal diamond or past cone of size T fluctuate as T⁴, slower, or faster?
  - Is there a general trade-off between lensing silence and Poisson-size count fluctuation?
- **Setting.**
  - The cocompact L₇ LRL ensemble, with the Haar measure on ISO⁺(1,3)/(L ⋊ Γ_L) (`C5_R2-2_referee.md:9`).
  - Windows: causal diamonds D_T and truncated past cones, each sharp and smoothed.
  - Comparators: Poisson at equal density, and Z⁴ in two frames.
- **Prior art (count once).**
  - R4-5 numerics and Lemma V (`TESTS:2943`; `C5_R4-5_referee_verdict.md:13,15`);
  - P-L′ (`TESTS:2712`);
  - O5 remark 1, quantum forward-cone volume law (`C5_O5_synthesis.md:447-453`);
  - E2/E3 frozen hyperuniform sets, spatial (`TESTS:243-263`);
  - Siegel densities (`TESTS:2905`).
- **Probes.**
  - (a) **Variance formula.** Write Var N(W) = ∫ S(q)|Ŵ(q)|², with S = the Haar average of the Bragg combs, i.e. a sum over shells Q(n) of the Siegel mass times the invariant measure on q² = (2π)²Q(n)/7. State convergence.
  - (b) **Shell asymptotics.** Find the asymptotics in T of ∫_{q²=c}|Ŵ_T|² dμ for sharp diamonds and past cones. Null boundaries make Ŵ decay slowly along null directions, where the hyperboloids accumulate. Find the exponent and the shell-sum convergence.
  - (c) **Numerics.** Extend R4-5 to larger T with sampling that is genuinely Haar on the quotient (R4-1's sampling correction, `TESTS:2909`). Fit with and without a T⁴ term.
  - (d) **Trade-off lemma.** For a Lorentz-invariant classical stationary point process with no structure-factor support for 0 < |q²| < c, prove or refute o(T⁴) count variance in diamonds.
    - Smooth windows: expected easy, since there is no support in the Euclidean ball of radius √c.
    - Sharp windows: the real case.
  - (e) **Λ size.** Translate the result into δΛ/Λ_obs under R4-5's three premises (`TESTS:2939`).
- **FIXED readings.**
  - For the LRL count:
    - **VOLUME:** Var ∝ T⁴ with a computed F > 0; state the resulting δΛ/Λ_obs.
    - **SUB-VOLUME:** o(T⁴) proved for sharp diamonds and past cones; record "everpresent-Λ magnitude excluded on LRL under the three premises" (referee required).
    - **DIVERGENT:** the shell sum diverges for sharp windows; report the regularization dependence.
    - **OPEN:** otherwise.
  - For (d) (derivation): **DERIVED / SUGGESTED / REFUTED.**
- **Expectation.**
  - Smooth windows: SUB-VOLUME (DERIVED).
  - Sharp windows: OPEN, leaning SUB-VOLUME with boundary-dominated growth.
  - (d): SUGGESTED.

---

**R6-4. Set A: can the records be the classical metric? (covariant classical–quantum gravity against the decoherence–diffusion bounds)**

- **Plain question.** In set A the records either do nothing for gravity or need a preferred slicing. In classical–quantum (CQ) gravity, the metric is classical: it is a record of where the mass is. It must then diffuse enough to keep quantum mechanics consistent, and lab experiments bound both the diffusion and the decoherence it causes. The simplest version is excluded by 32 decades. Does any version survive?
  - a smeared one;
  - the diffeomorphism-invariant one.

  And would its metric record satisfy "one record per site, permanent"?
- **Setting.** The variants:
  - (i) Newtonian CQ with a smearing length ℓ_s (non-ultralocal);
  - (ii) the diffeomorphism-invariant CQ-GR candidate cited in R3-4 (Oppenheim–Weller-Davies);
  - (iii) the Record reading: the metric history as the record set.

  Bounds:
  - Cs-133 at 1.9 µm for 70 s; 25 kDa molecules; ion coherence (`TESTS:2538-2541`);
  - torsion-balance and Cavendish mass-precision diffusion bounds, as published, verified or labelled from memory.
- **Prior art (count once).**
  - R3-4 E2 (`TESTS:2776`; `C5_R3-4_referee_verdict.md:13`);
  - R4-4 Lemma N: a classical channel gives zero entanglement (`TESTS:2935`), so a BMV-type positive result would exclude every variant; state that as a falsifier;
  - R2-3 Bianchi lemmas (`TESTS:2722`);
  - O4 Lemma 1 (`TESTS:2408`).
- **Probes.**
  - (a) Derive the decoherence–diffusion trade-off for (i) as a function of ℓ_s, and find the allowed window in ℓ_s.
  - (b) For (ii), state whether the covariant theory has a computed weak-field trade-off. If it does, apply the bounds; if not, say what is missing.
  - (c) Energy-momentum: does CQ diffusion source a Λ-like drift? Compare with R4-5's 17-decade Bianchi gap (`TESTS:2944`).
  - (d) Record reading:
    - Is a diffusing classical metric a set of permanent, one-per-site records in a block sense?
    - Which axiom text changes? Name the price.
- **FIXED readings, per variant:**
  - **VIABLE:** passes the stated bounds with named prices.
  - **EXCLUDED:** violates a stated bound for every parameter in the variant (referee required).
  - **OPEN:** otherwise.
- **Expectation.**
  - (i): a narrow VIABLE window at macroscopic ℓ_s, or EXCLUDED.
  - (ii): OPEN.
  - (iii): a reading with a Record price.

---

**R6-5. Set C's dimension-3 price: CPT-odd terms the axioms' proper-only rotations allow**

- **Plain question.** The axioms name only proper cubic rotations (`AX:37-41,57-58`). That allows two CPT-odd terms of dimension 3 (`TESTS:1440`):
  - an axial chemical potential b₀ for fermions;
  - a photon Chern–Simons term (k_AF)₀.

  Their natural size on a Planck lattice would be near the cutoff, while observation bounds (k_AF) to about 6e-43 GeV (`C5_O1_report.md:49`, partially verified). Are they generated? How large are they? Is the cheapest fix a tuning, or a symmetry added to the law?
- **Setting.**
  - Z³ × ℝ, with a gauge-invariant local Hamiltonian lattice law covariant under translations and proper cubic rotations only: no inversion and no antiunitary symmetry.
  - Matter: naive/staggered or Wilson-type fermions with compact U(1); then chiral content as R2-4 allows.
  - Sets B and B′ are excluded: V = 0 and Zariski density forbid invariant vectors (`TESTS:2379`; `TESTS:2788`).
- **Prior art (count once).**
  - F2 referee (`TESTS:1440`);
  - O1's counts and dimension-3 note (`C5_O1_report.md:82,104,242-245`);
  - the R2-4 chirality and CP scope (`C5_R2-4_referee.md:44-63`).
- **Probes.**
  - (a) An explicit local law in the class with b₀ ≠ 0 at natural size: a Weyl-node energy offset.
  - (b) Is (k_AF)₀ induced? Points to settle:
    - compact lattice U(1) admits no local A·B term;
    - the equilibrium chiral-magnetic response vanishes on lattices (Vazifeh–Franz, RECALLED; verify);
    - so state whether k_AF is PROTECTED, or induced through non-equilibrium or non-compact sectors.
  - (c) Observational bounds on b₀ for electron, proton and neutron (torsion pendulum, comagnetometer, boost-suppressed timelike components) and on k_AF (CMB). Verify or label from memory. Give the tuning in decades.
  - (d) The cheapest symmetry price: law-level CPT, i.e. CRT with spatial inversion, added to Lattice/Admissibility covariance. Is it compatible with chiral SM content and doublers/tastes on the lattice? Name the axiom text it touches.
- **FIXED readings.**
  - **TUNING-PRICED:** an explicit law in the class generates the term(s) at a computed natural size; state the tuning in decades against the stated bounds.
  - **SYMMETRY-PRICED:** a stated symmetry forbids them, is compatible with chiral content, and the axiom text it touches is named.
  - **PROTECTED:** proved forbidden by gauge invariance, locality, hermiticity and the axioms as written; C's price does not grow.
  - **INCONCLUSIVE:** otherwise.
  - More than one reading may apply, one per operator.
- **Expectation.**
  - b₀: TUNING-PRICED, by tens of decades.
  - (k_AF)₀: PROTECTED or suppressed in equilibrium (OPEN risk).
  - SYMMETRY-PRICED is available through law-level CPT, at a Lattice-text cost.

---

**R6-6 (conditional: run only if R5-2 returns PASS or INCONCLUSIVE with an explicit kernel). Stability of an LRL d'Alembertian**

- **Plain question.** R4-3 found that the representative five-shell kernel has a growing mode that e-folds in about two lattice times. Does any Γ_L-invariant retarded kernel whose mean is □ have no such mode? That includes R5-2's infinite-orbit kernel, if it exists.
- **Setting.**
  - Retarded Γ_L-invariant kernels on L₇, finite-shell and infinite-orbit, with Haar mean □ + O(a²).
  - Symbols in the forward tube (Prop. R, `TESTS:2787`).
- **Prior art (count once).**
  - R4-3's tube zeros (`TESTS:2927`; `C5_R4-3_referee_verdict.md:15`);
  - R4-1's weights (`TESTS:2905`);
  - Aslanbeigi–Saravani–Sorkin on stability of causal-set d'Alembertians (comparator, `C5_R4-3_referee_verdict.md:15`).
- **Probes.**
  - (a) An argument-principle certificate for forward-tube zeros of the mean symbol over a stated domain.
  - (b) Construct a moment-cancelled family with no tube zero, or prove that every family in a stated class has one.
  - (c) Apply (a) to R5-2's kernel.
- **FIXED readings.**
  - **PASS:** an explicit kernel with mean □ + O(a²) and a certified zero-free forward-tube symbol.
  - **FAIL:** a proof that every kernel in a stated class has a forward-tube zero (referee required).
  - **INCONCLUSIVE:** otherwise.
- **Expectation.** INCONCLUSIVE. Stable families are known for causal-set d'Alembertians in some dimensions (comparator, RECALLED); whether moment cancellation on LRL shells allows one is open.

---


### C5 Round 7, item 1 (pre-registered 14:46Z; launched now; conditional on R6-1, whose referee is running)

**R7-1. Box-confined Poincaré: does R6-1's non-analytic trick also break the boost wall?**
- R6-1's worker (unrefereed) builds an exactly additive real momentum on Z² fermions. The interactions are switched off smoothly outside a box |k_i| < a < π/2, with C^∞ non-quasi-analytic form factors and sub-exponential tails.
- The boost wall (C3/I1/RB/RFW, refereed) comes from the lattice momentum's cos k factor and from the analytic, periodic structure.
- Take the same non-analytic freedom in the dispersion: ε(k) = √(m² + k²) exactly inside the box, extended smoothly and periodically outside. Take interactions supported in the box.
- Does there exist:
  - a boost generator K on the box-supported sector, closing [K, P], [K, H] and [K, K] exactly on states whose momenta stay in the box under the boosts considered, i.e. a local Poincaré algebra with a rapidity cutoff;
  - an exact Ward identity for a linearized graviton coupled to the box sector?

  Quantify what fails at the box edge: leakage under finite boosts, and whether "approximately local in rapidity" is good enough to evade C3/I1.

Readings:
- **PASS:** an explicit finite-per-site law (fermionic allowed, as for R6-1) with an exact Poincaré algebra on a stated box sector and a stated rapidity range, plus the leakage bound, checked.
- **FAIL:** a no-go showing the box sector cannot carry exact boosts even with a rapidity cutoff (refereed).
- **INCONCLUSIVE:** otherwise.

### C5 Round 6 worker results awaiting referees (recorded 14:50Z; worker readings only, nothing here is recorded as a verdict)

- **R5-2:** INCONCLUSIVE. Referee relaunched after a codex capacity error.
- **R5-4:** INCONCLUSIVE. Referee running.
- **R5-5:** FAIL (bounded). Referee running.
- **R6-1:** REFUTED. Witness W: spinless fermions on Z² with a C^∞ box-supported p-wave pair form factor, giving exactly additive ℝ² momentum with nonzero 2→2 scattering and sub-exponential tails. Theorems A1/A2 extend Lemma G to d ≥ 2 for strict-range translation-invariant QCAs. Referee running.
- **R6-2:** A SUPPLIED-FORCED; B, B′ and C OPEN. Referee running.
- **R6-5:** worker readings (no FAIL, so no referee required; one may be added if codex capacity allows):
  - b₀: TUNING-PRICED, 43–49 decades with ≥ 3 joint conditions.
  - (k_AF)₀: PROTECTED by vacuum stability plus Bloch/Watanabe, not by symmetry.
  - The dimension-5 CPT-odd photon term is not protected: about 10 decades, suggested.
  - Law-level CPT: SYMMETRY-PRICED, conditional. It needs inversion in Lattice and Admissibility, a reversible law (the arrow in the state), and a chiral lattice construction that has not been built.

### C5 Round 7, item 2 (pre-registered 14:52Z; launched now)

**R7-2. Set E: a holographic or lower-dimensional substrate. Does it escape the walls that bind A, B, B′ and C?**
- The S5 synthesis notes that holographic, relational and non-commutative routes are unexamined (`agents/C5_S5_synthesis.md`, §6). R6-2's worker (unrefereed) says WW is evaded by holography only through a lower-dimensional substrate and an AdS bulk, which runs against the observed Λ > 0.
- Test the cheapest qubit-lattice versions:
  - (a) a tensor-network or holographic code on a 3D qubit lattice whose emergent bulk has 4D gravity (HaPPY, random tensor networks; the bulk is AdS);
  - (b) dS proposals: dS/CFT, static-patch holography, Susskind's double-scaled SYK, TT̄+Λ₂ flows;
  - (c) what each supplies against observations: Λ > 0 and its size, one light cone, GW170817 speed, universal coupling, record formation (the arrow).
- Name the prices against the axiom text: Lattice dimension, Qubit, Admissibility locality.

Readings, per route:
- **VIABLE:** gives 4D gravity with Λ > 0, matter on one cone and universal coupling, with prices named.
- **EXCLUDED:** violates a stated bound or is internally inconsistent (refereed).
- **OPEN:** otherwise.

### C5 Rounds 5–6 referee results (recorded 15:07Z)

**R5-2 (infinite-orbit kernels) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE.**
- **The exact reduction holds.** For shell-constant weights f_m = O(m^−A), A > 5, Haar-rms relative error O((a/ℓ)²) is equivalent to all of the following:
  - three cancellations per tempered mode;
  - double zeros for each threshold (r = 0) mode;
  - both real-branch cancellations for each exceptional mode;
  - the four mean-□ conditions.
- **Families that fail:**
  - nonzero finite-orbit kernels fail at leading order;
  - the 1+1 unweighted retarded family fails in every non-constant mode (Hecke step and the Jacquet–Shalika transfer confirmed);
  - sampled 3+1 families drift locally. This is checked only on local frame balls.
- **Full-lattice sums** give a delta comb whose central term is P(−□)δ(k), not the multiplier −k².
- **Open:** orbit-dependent and engineered infinite sequences.

**R5-4 (link-cell laws) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE.**
- **Lemma N** (finite covariant link neighbourhoods) is confirmed.
- **Lemma F, corrected:** multiplicity-one shells factor into a.e. ℓ² kernel fibres. Multiplicity r > 1 needs a generally non-splitting U(r) cocycle.
- **Theorem Δ:** every uniformly banded covariant linear law has a kernel set that is Haar-null or Haar-conull.
  - The conull case admits almost every mass.
  - The null case allows shell components only at a Lebesgue-null set of masses.
- **The 1+1 two-term scalar class has a genuine no-shell theorem.** The coined-walk evidence is finite truncation only.
- **Open:** no generated L₇ shell, and no exclusion at every mass.

**R5-5 (frame superposition) — NOT CONFIRMED as FAIL, so INCONCLUSIVE.**
- **Narrow exclusion.** Take a stipulated direct-integral model with a decomposable matter/record observable algebra. There every statistic is the |ψ|² mixture of branch statistics. That excludes an exact ensemble-mean unitary law, but under imposed superselection; it does not prove decoherence.
- **Lemma P0:** P^μ = 0 on the bare orientation sector.
- **Lemma AE holds** for the corrected finite-orbit class (Haar-a.e. limsup, off-shell).
- **The three four-shell mean symbols have unstable zeros.**
- **Which-frame numbers rejected.** A frame-dependent overall phase carries no which-frame information. Propagation-induced decoherence on observed scales is unproved.

**R6-1 (exact additive momentum) — NOT CONFIRMED as REFUTED, so SUGGESTED, with derived parts.**
- **Witness W is sound, but in the graded CAR category, not the fixed ⊗M₂ spin class.** One fermion mode per site admits an explicit super-polynomially quasi-local (non-exponential) d = 2 interaction with:
  - exact sawtooth momentum;
  - exact many-body conservation;
  - genuinely non-forward, umklapp-free 2→2 scattering. The referee found an explicit on-shell non-forward process.
- **Why it is outside the class.** 2D Jordan–Wigner gives long strings, and local bosonization needs gauge qubits and constraints.
- **Prop. N** (rank-one separable class: non-quasi-analytic form factor forced) is confirmed after narrowing.
- **DERIVED:** cylinder wrapping plus the GNVW index excludes H-TI uniformly range-bounded strict-QCA paths, and strict-range roots of the shift, in every dimension.
- **Not supplied:**
  - a ⊗M₂ witness;
  - a boost-compatible or SLAC energy current;
  - a stress tensor or Ward identity;
  - one-cone protection;
  - a graviton.

**R6-2 (Weinberg–Witten sorting) — NOT CONFIRMED. A, B, B′ and C are all OPEN.**
- **A is not SUPPLIED-FORCED.** W1–W3 are not established, and WW forbids elementary and composite spin-2 under its premises alike; it does not force "supplied".
- **Confirmed:**
  - the order lemma: per-copy WW phase argument empty on Γ_L;
  - proper action on momentum pairs;
  - the form counts 3 + 9 against 2 + 4;
  - Z₂ dimensions 43 = 31 + 15 − 3.
- **Lemma A is false as stated.** Global averaging need not preserve uniform locality. It survives for support-preserving direct-product gauge actions.
- **Zariski density** constrains polynomial coefficients but supplies no exact translations or conserved stress. Umklapp obstructs W3.
- **No PRODUCIBLE mechanism exists in the packet, as an absence of demonstration, not a no-go.** Still open:
  - the weak N-type stress bridge;
  - non-regular strong-coupling emergence;
  - non-local/holographic mechanisms.

### C5 Round 7, items 3–4 (pre-registered 15:08Z; launched now)

**R7-3. Spin-algebra version of R6-1's witness: exact additive momentum with scattering on ⊗M₂(C).**
- The R6-1 referee confirms W in the graded CAR category but not in the fixed ⊗_{Z^d} M₂ spin class.
- Build a qubit (spin) law on Z² or Z³ with exact additive ℝ^d momentum on scattering states and genuine non-forward 2→2 scattering. Candidates:
  - hard-core bosons with a box-supported C^∞ pair form factor;
  - multi-qubit unit cells with an encoded (gauge-constrained) fermion, counting the constraint sector honestly;
  - spin-wave (magnon) two-body scattering above a ferromagnet with a box form factor.
- Or show why spin composition forbids it, in a stated class. The R6-1 worker's suggestion was that hard-core versions fail.

Readings:
- **REFUTED-class (positive):** an explicit ⊗M₂ quasi-local law (tails stated) with exact additive momentum and checked non-forward scattering.
- **DERIVED (no-go):** a proof that a stated spin class forbids it (refereed).
- **SUGGESTED:** otherwise.

**R7-4. The weak N-type stress bridge: can the exact-constraint VS/N-type graviton on Z³ couple universally to matter's energy-momentum?**
- Lane R left this as the strongest live counter-route (`TESTS.md` lane R verdict). R6-2's referee keeps "the exact weak N-type stress-bridge route" open.
- Construct the lattice matter–graviton coupling: a local matter stress tensor sourcing the N-type constraint so that the combined system keeps the exact constraint algebra. Test:
  - universality across two matter species with different dispersions;
  - the Newtonian limit and the light-bending factor (γ);
  - the speed tuning needed against GW170817.
- Use R6-1/R7-3's exact-momentum constructions if helpful.

Readings:
- **PASS:** an explicit lattice coupling preserving the exact constraint, with universal coupling and γ = 1 at linear order, checked, with the tunings named.
- **FAIL:** a no-go that the constraint algebra cannot close with a matter stress source in a stated class (refereed).
- **INCONCLUSIVE:** otherwise.

### C5 Round 7, items 5–6 (pre-registered 15:17Z; launched now; conditional on R7-1, whose referee is running)

**R7-5. Loops in box-confined Poincaré: does a pair-creating box field theory feed Lorentz violation into the infrared?**
- R7-1's worker (unrefereed, reading PASS) flags its main physics risk. A frame-fixed momentum box in a pair-creating, point-vertex field theory is a Lorentz-violating regulator. By the Collins–Perez–Sudarsky–Urrutia–Vucetich mechanism it would generate O(1) dimension-4 speed differences (comparator F2: an 8.55e-3 QED split, `SUMMARY.md:423`).
- Build the cheapest box-confined interacting field theory with pair creation. Examples:
  - a Yukawa or φ⁴ vertex with box-supported, smooth form factors on Z³ × ℝ, Lorentz-exact inside the box;
  - form factors that are functions of invariant masses only, with compact support.
- Compute the one-loop self-energy's IR Lorentz violation: the coefficient of the dimension-4 operator (c² − 1)k². Is it O(1)·g², suppressed by a power of (box scale / cutoff), or zero?

Readings:
- **PASS:** an explicit box field theory whose one-loop IR dimension-4 LV vanishes, or is suppressed below current bounds without tuning, checked.
- **FAIL:** an O(g²) unsuppressed dimension-4 LV in a stated class (refereed).
- **INCONCLUSIVE:** otherwise.

**R7-6. Three and more particles in box-confined Poincaré: can the interacting algebra close beyond two bodies on a lattice?**
- R7-1's P2 closes the algebra for two interacting particles (unrefereed). Pairwise Bakamjian–Thomas boosts do not close for three or more bodies; the continuum fix is Sokolov packing or Coester–Polyzou many-body terms, with macrocausality/cluster separability.
- On the box sector of R7-1's lattice law, construct a three-body law (box-supported, smooth, faster-than-power tails) with an exact Poincaré algebra and cluster separability. Check numerically in d = 1.

Readings:
- **PASS:** an explicit three-body box law with an exact algebra and cluster separability, checked.
- **FAIL:** a no-go for box-supported quasi-local three-body closure with cluster separability, in a stated class (refereed).
- **INCONCLUSIVE:** otherwise.

### C5 Round 6–7 referee results (recorded 15:31Z)

**R7-1 (box-confined Poincaré) — CONFIRMED WITH CORRECTIONS. PASS WITH SCOPE.** This is the campaign's first PASS.
- **What holds.** A graded-CAR, continuous-time lattice law with smooth non-analytic, super-polynomially quasi-local hopping carries the exact, undeformed Poincaré Lie algebra on compactly supported finite-particle wavefunctions inside an open momentum box. Its finite free boosts agree with continuum boosts up to the stated rapidity boundary, with the leakage bound 2‖1_E ψ‖.
- **Why it is not overturned.** It is a genuine local-domain counterexample lying outside the global, integrated and analytic boost no-gos (C3, I1–I3, B1, M1, C1, R2-1, RFW). It avoids their hypotheses rather than overturning their conclusions. I3 bites only if integrated boost covariance is claimed.
- **Not established:**
  - **No invariant Poincaré sector.** The domain is infinitesimally invariant but not closed under finite boosts.
  - **P2 (two-body Bakamjian–Thomas) is defective as written.** The boost sign is wrong, the quartic prefactor must be ¼ *(withdrawn 2026-10-12 by the R8-1 referee: ½ is correct for the ordered kernel)*, and the boost is never constructed in the runner. After repair, standard BT applies on the 1D plateau. A rotationally invariant channel is still needed for d ≥ 2.
  - **Interacting leakage** is unproved.
  - **Ward identities.** W1 holds only for free matter where χ = 1; W2 is not established for interacting matter; W3 holds only as P1's free affine algebra; W4 (local lapse) is open.
  - **Universal coupling fails.** Energetic edge modes that do not gravitate violate it.
- **What meets the fixed clause.** The PASS clause is met through P1 (free, every particle number) alone, with the graded fermionic composition the clause expressly allows.

**R6-4 (records as the classical metric) — CONFIRMED WITH CORRECTIONS.**
- **(i) Smeared Newtonian CQ: VIABLE**, on a conservative demonstrated subwindow of 4e-10 m ≲ ℓ_s ≲ 5e-6 m.
  - The class is homogeneous Markovian Gaussian continuous CQ Newtonian gravity with additive dephasing.
  - The DP floor has an 8π normalization mismatch, so the true lower end is about 1e-10 m.
  - The LISA Pathfinder floor is a γ = 1 prediction.
  - The 10 µm ISL endpoint is unsupported.
- **(ii) OPEN overall.** Layton et al.'s unregulated point-particle Newtonian limit is EXCLUDED: Corollary U gives cubic UV heating. The covariant or UV-completed family is open.
- **(iii) A reading with prices** on Lattice, Qubit, Admissibility and Record, plus a source/readout/permanence bridge.
- **H-cosmo is conditional** and does not exclude (i).
- **Dated correction to R3-4/R2-3 (2026-10-12).** The R3-4 referee's "32-decade empty window" excluding ultra-local Newtonian CQ gravity **falls**. OSSW's published torsion-balance reduction (F8–F10) is invalid. It replaces the spatially falling total-body field with a nuclear interior-field estimate. Direct integration gives σ_a² = (48π/5)G²D₂/(RT) and D₂ ≲ 3.7e5, a 9.45e44 discrepancy. What survives is only the narrower cutoff-free point-particle no-go (Corollary U).

**R6-3 (Lemma V, LRL count variance) — CONFIRMED WITH CORRECTIONS.**
- **Count: SUB-VOLUME.**
  - Diamond counts: Var N(D_T) = O(T² log T).
  - Past cones: O(T³). The proof is repairable, and the T³ mean and variance are dominated by rare near-rest frames.
  - The coefficients 0.1665 and 0.4847 are numerical, not exact. The advertised constant K is wrong (about 2.0e4), but the bound holds.
- **Literal Lemma V (d): REFUTED.** Lorentz-random affine Z⁴ has null reciprocal vectors and a positive T⁶ contribution of about 0.042.
- **Null-inclusive V′: DERIVED, with repairs.** Finite local second moments plus a reciprocal gap that excludes the null cone force sub-volume laws.
- **Strict lensing silence: OPEN.**
- **Cosmology.** Under H1/H2/H4, sub-volume variance makes Λ fluctuations too large: about 1.4e30 for the cone and 1.4e59 for the diamond. So everpresent-Λ size is excluded on LRL sites under those heuristic premises. This holds for homothetic flat regions; the epoch comparison assumes power-law FRW.

**R7-2 (set E: holographic substrates) — CONFIRMED WITH CORRECTIONS.**
- **Pure AdS: EXCLUDED** only when identified with our cosmological bulk and dark energy is a constant Λ < 0.
- **AHS higher-spin dS/CFT: EXCLUDED**, narrowly.
- **All other routes: OPEN.**
- **D ≤ 3 gives no local graviton.** This holds for the explicit HaPPY/AdS₃, DSSYK and TT̄ realizations, but not for the random-tensor-network class, which admits higher-dimensional bulks.
- **The {5,3,4} lattice is Planck-curved:** a/R = 1.0613, a 10^62.3 curvature mismatch.
- **Qubit AME states exist only for n = 2, 3, 5, 6** (confirmed).
- **dS/CFT keeps three spatial dimensions,** but not the literal Z³. Adding Z³ breaks conformal symmetry.
- **N-bound.** 4.78e122 qubits. The overcount is of order 1e61; the fm-scale minimum spacing is 3.4–4.6 fm, depending on the slicing.
- **Rule C** gives log₂N = |V| − |C| on open sets, 3L² − 3L + 1 for a box. The torus rank differs, but the nullity is the same.

### C5 Round 8 (pre-registered 15:39Z; launched now)

These follow up the two survivors: R7-1 (PASS WITH SCOPE) and R6-4 (VIABLE).

**R8-1. Repair and extend R7-1's interacting sector (P2).**
- The R7-1 referee found P2 defective as written: wrong boost sign; the quartic prefactor must be ¼; the boost was never constructed or tested.
- Repair the two-body Bakamjian–Thomas box law. Construct K for the interacting two-particle box sector, and verify every Poincaré commutator numerically on the lattice, in d = 1 and then d = 2 with a rotationally invariant channel.
- Prove the interacting leakage bound, using internal-mass spectral support.

Readings:
- **PASS:** the repaired interacting two-body box sector has an exact Poincaré algebra (d = 2 with rotations), and the interacting leakage bound is proved, checked.
- **FAIL:** an obstruction to the interacting algebra on the box sector in d ≥ 2 (refereed).
- **INCONCLUSIVE:** otherwise.

**R8-2. The edge-mode universality problem in box-confined Poincaré.**
- In R7-1's law, the zone-edge modes outside the box carry energy and the whole lattice anomaly. The referee notes that excluding them from gravity violates universal coupling.
- Can the edge sector be:
  - (a) made to gravitate with a lattice symbol, with the Ward identities closing on box ⊕ edge;
  - (b) gapped to the Planck scale so it is never produced and its coupling is irrelevant below a bound;
  - (c) removed by a non-periodic momentum space (a price on Lattice)?
- Quantify the equivalence-principle violation (Eötvös η) from edge modes for each option.

Readings:
- **PASS:** an option with universal coupling at linear order (box plus edge) and Eötvös η below 1e-15, with prices named, checked.
- **FAIL:** a no-go showing universal coupling cannot hold with an exact box sector, in a stated class (refereed).
- **INCONCLUSIVE:** otherwise.

**R8-3. Relativistic completion of R6-4's smeared CQ gravity.**
- R6-4 (refereed): smeared Newtonian CQ is VIABLE on 4e-10 to 5e-6 m. Its covariant completion is OPEN.
- Construct the cheapest relativistic smeared CQ theory: covariant smearing of the stress-tensor coupling (e^{ℓ²□} or a causal smearing), or Oppenheim–Weller-Davies with field-dependent kernels.
- Test:
  - light bending (γ);
  - GW170817 (c_T), given that classical gravity has no graviton but metric waves exist classically;
  - Shapiro delay;
  - the timelike-momentum problems of e^{ℓ²□};
  - positivity (complete positivity) at finite c.

Readings:
- **VIABLE:** an explicit covariant smeared CQ theory passing the stated bounds, with prices named.
- **EXCLUDED:** violates a stated bound or is internally inconsistent (refereed).
- **OPEN:** otherwise.

### C5 Round 7 referee results, part 2 (recorded 16:05Z)

**R7-4 (N-type stress bridge) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE.**
- **Two decoupled species.** For the 09-14 weak N-type constraint pair, two decoupled nearest-neighbour scalar species admit an exact linear-order lapse/shift bridge with:
  - J_E = c_s²P;
  - symmetric stress;
  - c′_s = −κa_s c_s²/J;
  - a lattice 1/r limit;
  - γ_s = c_s²/c_g².
- **Universality and γ = 1 come only from imposing them:** equal couplings and a common matter–graviton cone. Energy-exchanging scattering forces both only under the regular collision-invariant hypotheses.
- **Corrections:**
  - 0.69 is a normalized differential acceleration; the symmetric Eötvös parameter is 0.513.
  - T4 is not a compulsory tuning: RN L1's seagull cancels the uniform-strain part.
- **Constraint preservation gives the formal i[H,D] = J and [H,J] = 0,** but not a self-adjoint, globally exponentiating D.
- **The conditional box exclusion.** With those extra global assumptions, every proper box-supported scattering amplitude is excluded. So the R6-1/R7-1 box interaction cannot be a global exact stress bridge. R7-1 evades this by asserting only a local algebra up to a rapidity budget.
- **The "only forward or exchange" theorem is not proved at theorem scope.**

**R7-5 (loops in box field theory) — NOT CONFIRMED as PASS. Bounded FAIL for classes P and FF.**
- **The bounded FAIL.** Point Yukawa and frame-fixed smooth vertices on the continuous-time Z³ box dispersion generate unsuppressed one-loop scalar speed terms: XI_P ≈ 1.7–1.94 and XI_FF ≈ 10.9. This is O(g²/16π²) dimension-4 LV.
- **INV: a conditional spectral lemma only.** If continuum on-shell legs stay in the box and both pole orderings carry the same compact invariant-mass weight, the scalar and Dirac self-energies are exactly Lorentz-invariant spectral functions inside the momentum budget. But no explicit stable finite-per-site lattice field Hamiltonian realizing this was built.
- **BT is a finite-sector mass-operator model, not a field theory.** "Every order" means only within the truncated sector.
- **Invariant-mass vertices are an imposed functional custodial condition.** They are not derived and not shown to be radiatively closed.

**R7-6 (three-body box Poincaré) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE.**
- **The pair-sum drift is real.** The d = 1 three-fermion pair-BT trimer's invariant-mass drift is robust. With the corrected ¼ prefactor it shrinks from δ ≈ 0.074 to about 0.019.
- **So H needs a connected three-body term.** Given P = Q and a locally integrable self-adjoint boost, no boost completes the pair-sum H.
- **P = Q is an extra physical identification**, not a consequence of the Lattice axiom.
- **Sokolov packing is a formal route only.** The full lattice operator, its domain and its faster-than-power tails were not shown. The exp(−0.8√r) fit is only three points, and a power fit is better.


### C5 Round 8, items 4–5 (pre-registered 16:06Z; launched now)

**R8-4. An explicit lattice field Hamiltonian for invariant-mass vertices (the INV gap named by the R7-5 referee).**
- Build an explicit, stable (bounded-below), self-adjoint, finite-per-site lattice Hamiltonian on Z³ × ℝ (fermionic allowed). Its pair-creation vertices must be compact smooth functions of the created pair's invariant mass, with every time ordering present, so that R7-5's INV spectral lemma applies.
- Check:
  - boundedness below (the vacuum-triple term);
  - quasi-locality (tails);
  - the one-loop self-energy is Lorentz-invariant inside the box, computed from the Hamiltonian itself, not from inserted Feynman expressions;
  - radiative closure at two loops, at least in a toy: does the invariant-mass structure survive?

Readings:
- **PASS:** an explicit Hamiltonian meeting all four checks at one loop, with two-loop closure in a stated toy.
- **FAIL:** a no-go: invariant-mass vertices with all time orderings are incompatible with a bounded-below finite-per-site Hamiltonian, in a stated class (refereed).
- **INCONCLUSIVE:** otherwise.

**R8-5. Gauge fields in box-confined Poincaré.**
- QED's one-cone split (F2: 8.55e-3) is the decisive open item for the box route.
- Can a lattice U(1) gauge theory on Z³ × ℝ have:
  - a photon with exact dispersion ω = |k| in the box (non-analytic, as in R7-1);
  - a matter coupling that is gauge-invariant and either box-confined or invariant-mass-structured;
  - an exact Ward identity (charge conservation and gauge invariance)?
- Compute whether the one-loop vacuum polarization and the electron self-energy keep a common light cone. Identify the obstruction if gauge invariance forbids box-supported vertices (minimal coupling via Peierls phases is point-local).

Readings:
- **PASS:** an explicit gauge-invariant box law with an exact Ward identity whose one-loop photon and electron cones agree to below 1e-15 without tuning, checked.
- **FAIL:** a no-go that gauge invariance plus box confinement of the vertex is impossible in a stated class, or a computed unsuppressed one-loop cone split (refereed).
- **INCONCLUSIVE:** otherwise.

### C5 Round 7–8 referee results, part 3 (recorded 16:25Z)

**R7-3 (exact momentum on ⊗M₂) — CONFIRMED WITH CORRECTIONS. SUGGESTED, with derived parts.**
- **Route A (Kitaev).** On the flux-free invariant sector of a one-qubit-per-site Kitaev brick-wall model, a spin-string image of the CAR witness has exact additive cell momentum at every quasiparticle number. It also has reproducibly non-forward, umklapp-free 2→2 scattering. Super-polynomial locality is plausible but not norm-certified. The vison-pair defect scatters non-forwardly.
- **Lemma S** rigorously excludes bounded additive lifts for a translation-covariant scalar flat-band defect with a nonzero non-forward kernel.
- **Lemmas I and L** (the hard-core Fredholm deficit, and the continuity obstruction) hold under their hypotheses.
- **Route B** keeps the two-body S-matrix under its rank-one dressing. Full-spin quasi-locality and N ≥ 3 are open.
- **No all-sector ⊗M₂ witness, and no general fermion-encoding no-go.**

**R8-2 (edge-mode universality) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE** against the physical PASS criterion.
- **Confirmed:**
  - R7-1's literal band has exactly 2^d − 1 extra mass-m corner valleys.
  - A monotone edge can remove them, but the edge threshold is at most √(m² + b²)/a.
  - For free number-conserving matter there is a smooth, quasi-local, symmetric, Hermitian box-plus-edge stress with an exact linear Ward identity. Its energy integral is H, and its first moment is R7-1's boost on box states.
  - Lemma U: continuity forces box–edge matrix elements.
  - **Theorem E:** under a uniform lapse, Ṗ_i = −g_j[δ_ij H + dΓ(ε A_ij)], with A = Hess(ε²/2) − I and a zone mean of −I. So every finite periodic band has states that fall non-universally.
- **η = 0 holds only as a proxy** for free box packets at linear order. No universally coupled interacting stress or bound-body Eötvös observable was built.

**R8-3 (covariant smeared CQ) — NOT CONFIRMED as class-wide EXCLUDED, so OPEN, with a conditional no-go.**
- **The conditional no-go.** At golden-rule order, consider a translation- and Lorentz-invariant linearized Gaussian CQ model with:
  - a common scalar stress form factor (or a nonzero GR-normalized spin-2 one);
  - a retarded propagator;
  - a pointwise decoherence–diffusion bound;
  - additive decoherence.

  Such a model cannot simultaneously keep the light-cone coupling, give finite radiation, and have a finite vacuum-excitation rate.
- **What this excludes:** e^{ℓ²□}, continuous bounded scalar factors in that subclass, and (conditionally) ultra-local OWD kernels with positive spin-2 weight.
- **Not excluded:**
  - general non-Markovian or correlated Gaussian histories;
  - OWD as a framework;
  - trace-only or spin-separated kernels;
  - light-cone-renormalized distributions;
  - jump, non-Gaussian or mediator constructions.

### C5 Round 9 (pre-registered 16:38Z from the S8 synthesis, agents/C5_S8_synthesis.md; readings fixed as drafted below)

Launch: R9-1, R9-2, R9-4 and R9-5 now; R9-3 when a slot frees; R9-6 only on its condition. Draft text verbatim from S8 §5:


**Rules (as for rounds 2–8).**
- Probes: Opus 5.5 at xhigh.
- Every FAIL, EXCLUDED or no-go goes to the codex gpt-5.6-sol (xhigh) referee before it is recorded.
- Prices are named, never adopted.
- Each probe greps the repository and packet for prior art first, and counts each match once.
- Hypotheses are stated before titles; excluded outside realizations are listed.
- Numbers from memory are labelled RECALLED unless verified.

**Overlap check against R8-1, R8-4 and R8-5.**
- R8-1 builds the two-body algebra and leakage in d = 1 and d = 2, and excludes W1–W4, N ≥ 3 and d = 3 (`C5_R8-1_report.md:34-44`).
  - R9-2 uses R8-1's law for the stress tensor only.
  - R9-3 is N = 3.
  - R9-6 is d = 3, conditional on R8-1's referee.
- R8-4 builds the INV Hamiltonian. No R9 item builds pair-creating vertices.
- R8-5 covers gauge fields. R9-1 conditions on R8-5's coupling form but builds no gauge field.

**Priority.** R9-2, R9-1, R9-3, R9-4, R9-5; R9-6 conditional.

---

**R9-1. Edge-sector population: are the wrong-falling edge quanta harmless, observable, or dark-matter-like?**

- **Plain question.** Theorem E says every finite periodic band has states that fall the wrong way. In C-box they live outside the box, in the edge. The literal law also has 2^d − 1 copies of each particle at the zone corners, with the same mass m. These fall correctly at rest and feel no box-supported interaction, only gravity. Does anything put particles in the edge? If so, what would we see: a violation in lab free-fall tests, a cosmic relic, or something that behaves like dark matter?
- **Setting.**
  - R7-1/R8-2's free law in d = 3, with two edge profiles:
    - (L) literal, with doublers;
    - (G) gapped, edge threshold E_e ≤ √(m² + b²)/a.
  - Gravity: R8-2's universal box⊕edge stress at linear order, with the first-moment lapse.
  - Interactions: box-supported and number-conserving (R7-1/R8-1).
  - Lattice spacing a is a parameter; a = ℓ_P is a reading.
  - Excluded: pair-creating vertices (R8-4). Gauge couplings are treated conditionally: (G-in) gauge vertices box-supported; (G-out) point-local Peierls coupling that reaches the corners. Take the form from R8-5 if it has reported.
- **Prior art (count once).**
  - R8-2 (`TESTS:3550-3557`; `C5_R8-2_report.md:64-70,130-131,152,177-178`);
  - the referee's leakage correction (states near the face couple with small q; `C5_R8-2_referee_verdict.md:29`);
  - Theorem E scope (`:47`);
  - O2 Lemma F (`C5_O2_report.md:118`);
  - R7-1 leakage (`TESTS:3399`);
  - the I2 zone average (`SUMMARY:403-405`);
  - MICROSCOPE, as cited at `C5_R8-2_referee_verdict.md:66`.
- **Probes.**
  - (a) **Production.** Compute the rate of edge population by:
    - (i) gravitational box→edge transitions through Lemma U matrix elements, for matter near the face and for a thermal gas at temperature T;
    - (ii) thermal equilibrium at an early-universe temperature T_max (a parameter);
    - (iii) gravitational particle production in an expanding background (comparator literature RECALLED unless verified);
    - (iv) under G-out, ordinary gauge production of corner copies.
  - (b) **Fall and clustering.** For each populated edge state, give the A(k) tensor of Theorem E and the energy-weighted means. Then:
    - (1) the admixture η in test bodies against 1e-15;
    - (2) a relic gas's density, equation of state, and whether it clusters like cold dark matter or falls up or anisotropically;
    - (3) for doublers under G-in: a gravitationally-only interacting mass-m copy of every species. State the dark-matter equivalence-principle bound used (verify or label RECALLED).
  - (c) **Momentum balance.** Theorem E's Ṗ contains dΓ(εA). Identify where momentum goes in a uniform field (into the field, or not conserved), i.e. active versus passive mass.
  - (d) Name the price for each outcome.
- **FIXED readings, per profile (L, G) and gauge case:**
  - **HARMLESS:** computed edge population, for every T_max up to a stated bound, stays below every stated observational bound (η < 1e-15; relic Ω_edge below a stated limit), checked.
  - **EXCLUDED:** a computed population violates a stated bound for every parameter in the profile class (refereed).
  - **DARK-CANDIDATE:** a computed relic abundance can equal Ω_DM in a stated parameter range without violating the stated bounds, including a dark-matter EP bound. Recorded as a lead, not adopted.
  - **OPEN:** otherwise.
- **Expectation.**
  - G: HARMLESS for T_max well below E_e (Boltzmann suppression; E_e is Planckian for b of order one); OPEN near Planckian T_max.
  - L under G-out: EXCLUDED (charged mass-m copies of the electron).
  - L under G-in: OPEN, leaning HARMLESS (purely gravitational production), with a DARK-CANDIDATE risk worth computing.

---

**R9-2. The interacting stress tensor on the box, and the fall of bound bodies (plus the free shear mass)**

- **Plain question.** Gravity must pull on binding energy exactly as on rest mass. MICROSCOPE tests this to about 1e-15 for bodies whose binding fractions differ. R8-2 built a universal stress only for free particles. Is there an exactly conserved stress for the *interacting* box law whose bound states fall with weight one? Separately, does R8-2's free box⊕edge stress bring back the E_g shear mass that free lattice matter generates (V3)?
- **Setting.**
  - The law: R8-1's repaired two-body law (d = 1, d = 2), conditional on R8-1's referee. If R8-1 is not confirmed, use the d = 1 BT law as repaired per the R7-1 referee (`C5_R7-1_referee_verdict.md:93-104`).
  - The free stress: R8-2's Construction A.
  - Gravity: first-moment lapse coupling.
  - Test bodies: two bound states with different binding fractions (vary λ or κ), at rest and moving within the budget.
  - Excluded: pair creation (R8-4), gauge fields (R8-5), N ≥ 3 (R9-3).
- **Prior art (count once).**
  - R8-2 (`TESTS:3554-3557`);
  - R7-1 W2/W4 (`C5_R7-1_referee_verdict.md:237-250`);
  - R7-4 Lemma 1 and the conditional exclusion (`TESTS:3496-3497`; `C5_R7-4_referee_verdict.md:35-55,75`);
  - R7-6 instant form and P = Q (`TESTS:3508-3509`);
  - V3 μ_E = 1.97038864e-3 per cell (`PRICE_NOTE:290-295`);
  - the RN L1 seagull correction (`PRICE_NOTE:341-352`);
  - O2 Lemma F.
- **Probes.**
  - (a) **Free shear.** Compute the uniform-strain (E_g, T_2g) susceptibility of R8-2's box⊕edge stress for profiles L and G, against V3's μ_E. Does the edge carry it?
  - (b) **Interacting stress.** Construct T_int^{μν} for the two-body law with these properties:
    - symmetric, Hermitian, quasi-local (tails stated);
    - an exact linear Ward identity on the two-body box sector;
    - ∫T⁰⁰ = H;
    - first energy moment = the interacting K.
  - (c) **Bound-body fall.** Compute the operator identity for Ṗ in a uniform lapse (Theorem E plus the interaction term), the acceleration of each bound state, and η between two binding fractions, at rest and in motion.
  - (d) **R7-4's hypotheses.** Identify which of R7-4's global hypotheses the construction violates (self-adjoint exponentiating D; Møller intertwining). State the rapidity range on which (b) is exact.
- **FIXED readings.**
  - **PASS:** (b) and (c) met, with computed η between two binding fractions below 1e-15 at linear order (or exactly zero), checked.
  - **FAIL:** a refereed no-go that no stress with (b)'s properties exists for box-supported two-body interactions in a stated class; or a computed bound-body η > 1e-15 that no choice in the class removes.
  - **INCONCLUSIVE:** otherwise.
  - (a) is reported as **SHEAR-PRESENT / SHEAR-ABSENT / OPEN**, with the number.
- **Expectation.**
  - (a) SHEAR-PRESENT [S8 reading: Theorem E moves the anomaly to the edge; the zone average still feeds the uniform-strain response].
  - (b)–(c): INCONCLUSIVE, leaning PASS in d = 1. BT bound states have H = √(M² + P²), so a stress built as the mass-operator density should give weight one at rest. The risk is the locality of that density, and a global-exponentiation requirement sneaking back in.

---

**R9-3. Sokolov-packed three-body box law, built and checked on the lattice (d = 1)**

- **Plain question.** For three bodies, adding up pair interactions breaks relativity (R7-6). The textbook cure, Sokolov packing, adds connected three-body terms so the algebra closes and far-apart particles stop affecting each other. Does the cure work on the lattice, with tails that still fall faster than any power?
- **Setting.**
  - d = 1, three spinless fermions on a ring.
  - The pair law: R8-1's (or the R7-1-referee-repaired) pair law, with R7-6's plateau and box.
  - The packed H_S and K_S are built as explicit operators, not formally.
  - Excluded: d ≥ 2, pair creation, gravity.
- **Prior art (count once).**
  - R7-6 (`TESTS:3506-3510`; `C5_R7-6_referee_verdict.md:52-67,93-137`);
  - Keister–Polyzou, Coester–Polyzou, Reichelt–Schweiger–Klink, as cited there;
  - R7-1 Lemma Sm (`C5_R7-1_referee_verdict.md:131-137`).
- **Probes.**
  - (a) Construct H_S, K_S on the three-body box sector.
  - (b) Check [K,P] = iH, [K,H] = iP and [H,P] = 0 on rings of at least three sizes.
  - (c) **Cluster separability.** Translate one particle by r over at least 1.5 decades. Measure ‖(H_S − H_{12} ⊗ 1 − 1 ⊗ h₃)ψ_r‖ and the same for K.
    - Pre-registered model comparison: an information criterion on log residuals over the full range, super-polynomial (e.g. exp(−c r^β)) against a power law.
  - (d) Measure the real-space tails of H_S − H_BT and of the packing unitary.
  - (e) Check the trimer invariant mass at P = 0, ±P₁, ±P₂.
- **FIXED readings.**
  - **PASS:** (b) residuals → 0 with L; (e) drift at the discretisation floor; (c) and (d) super-polynomial by the pre-registered comparison; checked.
  - **FAIL:** a refereed proof that, in a stated class (box-supported pair interactions, smooth plateau), the connected term or the packing unitary has power-law or slower tails, or that cluster separability fails.
  - **INCONCLUSIVE:** otherwise.
- **Expectation.** INCONCLUSIVE. The algebra should close by construction; the tails are the real risk, since the R7-6 referee found a power law fits better over 40–320 (`C5_R7-6_referee_verdict.md:125-128`).

---

**R9-4. Covariant CQ gravity outside the R8-3 subclass: spacelike-supported, spin-separated and non-Markovian kernels (set A)**

- **Plain question.** Smeared classical gravity works at Newtonian level (R6-4). Its simplest relativistic forms cannot keep light bending, finite radiation and a quiet vacuum all at once (R8-3). The no-go lists what it does not cover. Test the cheapest member of each uncovered class.
- **Setting.** Linearized, translation-invariant Gaussian CQ models; variants:
  - (i) **Spacelike-supported kernels** [S8 suggestion]. Noise kernels Lorentz-invariant and supported on spacelike transfer q² > 0 only.
    - Reason: R8-3's vacuum divergence (Lemma 1) lives on the future timelike cone, where pair creation needs q. Static Newtonian exchange is at q⁰ = 0, which is spacelike.
    - The question is the null cone, where radiation and lensing live.
  - (ii) **Spin-separated.** Spin-2 is GR-normalized at the light cone; a separate scalar kernel carries the decoherence and diffusion.
  - (iii) **Non-Markovian.** Temporally correlated kernels that violate the pointwise additivity H3′ while keeping complete positivity.
  - (iv) **Preferred frame.** R8-3's search target 1e-8 to 5e-6 m, with D₀'s excess near the null cone computed.
- **Prior art (count once).**
  - R6-4 (`TESTS:3409-3418`; `C5_R6-4_referee_verdict.md:5-25`);
  - R8-3 (`TESTS:3559-3573`; `C5_R8-3_referee_verdict.md:5-19`);
  - R4-4 Lemma N (a BMV-type positive result excludes every variant; `TESTS:2935`);
  - Bedingham and Tumulka (as cited in `C5_R8-3_referee_verdict.md:5`);
  - OWD's trace-only kernel (`:13`).
- **Tests.**
  - complete positivity at finite c;
  - γ = 1 and Shapiro delay;
  - c_T (GW170817), and finite radiation (Lemma 3's light-cone log);
  - a finite vacuum-excitation rate (Lemma 1);
  - decoherence and diffusion against R6-4's bounds: Cs-133 for 70 s; LPF as a γ = 1 prediction; torsion with the corrected integration σ_a² = (48π/5)G²D₂/(RT);
  - the Newtonian limit must land in R6-4's window.
- **FIXED readings, per variant:**
  - **VIABLE:** passes all stated tests with named prices.
  - **EXCLUDED:** violates a stated bound or is inconsistent, for every parameter in the variant (refereed).
  - **OPEN:** otherwise.
- **Expectation.**
  - (i) OPEN. The risk is at q² = 0: radiation and lensing sit on the support's boundary, and Lemma 3's log may return.
  - (ii) OPEN; the scalar channel's lensing contribution needs a computed bound.
  - (iii) OPEN.
  - (iv) OPEN, with a computed window, or EXCLUDED.

---

**R9-5. Box-confined Poincaré on a qubit lattice (⊗M₂), with honest sector accounting**

- **Plain question.** Every box PASS uses fermion modes, which compose across sites with signs. The campaign's reading of Qubit is one qubit per site with the plain tensor product. Can the free box law live on qubits? R7-3 put R6-1's witness into the flux-free sector of a Kitaev spin model. Does the same work for R7-1's box law? What lives in the other sectors, at what energy, and what does it cost?
- **Setting.**
  - ⊗_{Z^d} M₂(C), d = 2 (d = 3 if cheap). Two routes:
    - (A) a Kitaev honeycomb or brick-wall model whose matter Majoranas carry the box dispersion in the flux-free sector. Massive box dispersion needs a gap-opening term; state which.
    - (B) a gauge-constrained fermion encoding (Bravyi–Kitaev superfast or Chen–Kapustin–Radičević), with the constraint sector counted.
  - Excluded: interactions beyond R7-1's free law; gravity.
- **Prior art (count once).**
  - R7-3 (`TESTS:3543-3548`; `C5_R7-3_referee_verdict.md:5-35`);
  - R6-1 (`TESTS:3316-3329`; `C5_R6-1_referee_verdict.md:17`);
  - R7-1 (`TESTS:3398-3407`);
  - R8-2 doublers and edge (`TESTS:3552-3553`).
- **Probes.**
  - (a) The explicit spin Hamiltonian, with norm-certified super-polynomial tails (the gap the R7-3 referee named).
  - (b) R7-1's free box algebra on the invariant sector at every particle number, checked.
  - (c) The complementary sectors: vison and defect energies and dispersions; whether they form a non-Poincaré, edge-like sector; and whether sector-connecting local operators (a single σ^z flips two fluxes) are generated by the dynamics.
  - (d) Name the price: sector restriction, a constraint, and the Qubit-text question in P26(c).
- **FIXED readings.**
  - **PASS:** an explicit quasi-local ⊗M₂ law (tails certified) whose stated invariant sector carries the exact free box Poincaré algebra at every particle number, with the complementary sectors' gap and dynamics computed and the price named, checked.
  - **FAIL:** a refereed no-go for ⊗M₂ quasi-local laws carrying the free box algebra on a stated class of sectors.
  - **INCONCLUSIVE:** otherwise.
- **Expectation.** INCONCLUSIVE overall. The flux-free algebra is likely: the Kitaev map is exact there, and the law is free. The risks are certifying the tails and a vison sector whose gap sets a new, possibly low, edge-like threshold.
- **Context [S8 reading].** `AX:47` fixes the one-site algebra and states no cross-site composition. Whether graded composition is a price on the axiom text, or only on the campaign's ⊗M₂ reading (`TESTS:3039`), is an owner question this probe does not settle.

---

**R9-6 (conditional: run only if R8-1's referee confirms the d = 2 construction, with or without corrections). The d = 3 rotation-multiplet box law**

- **Plain question.** R8-1 (pending) builds the interacting two-body box law in d = 2 with a p-wave doublet and a spin term. In d = 3 the channel becomes a p-wave triplet, and the spin term becomes (P × S)/(M + H) (suggested, `C5_R8-1_report.md:127`). Separately, the box is a cube, and finite rotations push corner states out of a cube. Does the full ten-generator algebra close in d = 3? What is the rotation budget?
- **Setting.**
  - d = 3, with g_a(q) = q_a b(|q|²) for a = 1..3.
  - The exact region is taken in two forms: (i) the cube |k_i| < b; (ii) the inscribed ball |k| < b.
- **Prior art (count once).**
  - R8-1 (pending; `C5_R8-1_report.md:22-44,127,258,279`);
  - R7-1 (`TESTS:3398-3407`);
  - the R7-1 referee's d ≥ 2 channel requirement (`C5_R7-1_referee_verdict.md:99-104`).
- **Probes.**
  - (a) All 45 commutators of {H, P_i, J_i, K_i} in the canonical chart, with the spin term.
  - (b) Lattice spectrum: the bound triplet's invariant mass against |P| and direction, at three L.
  - (c) Finite-rotation and finite-boost leakage for the cube and for the ball. Give the rotation-angle budget, and prove a 2‖1_E ψ‖-type bound for rotations.
  - (d) The cubic anisotropy of the bound state where only the cube, not the ball, is exact.
- **FIXED readings.**
  - **PASS:** (a) closes to a stated tolerance; (b) the mass is P-independent to converging precision; (c) leakage bounds proved and checked for rotations and boosts.
  - **FAIL:** a refereed obstruction to the d = 3 interacting algebra on the box sector.
  - **INCONCLUSIVE:** otherwise.
- **Expectation.** PASS in the canonical chart. Lattice-native checks are likely resolution-limited, as in d = 2 (`C5_R8-1_report.md:258`), so INCONCLUSIVE overall is likely. [S8 reading, elementary] On the ball, finite rotations preserve |k|, so the rotation budget is unlimited. Only boosts leak.

---


### C5 Round 8 referee results (recorded 16:42Z)

**R8-1 (repair of R7-1's interacting two-body box sector) — CONFIRMED WITH CORRECTIONS. PASS WITH SCOPE.**
- **The ½ vs ¼ prefactor: the worker is right.** The R7-1 referee's "¼" correction was wrong: that referee compared the Fock element with a single ordered kernel entry. The ½ lift equals the restriction of W to ∧²ℋ. The exact spectra agree to 7.1e-15 with ½ and miss by 5.1 with ¼.
  - **Dated correction (2026-10-12)** to the R7-1 entry above: "the quartic prefactor must be ¼" is withdrawn. The ½ prefactor of R7-1's runner is correct for its ordered kernel. This also covers R7-6's use of "the corrected ¼ prefactor (δ ≈ 0.019)". The drift R7-6 found at ½ (δ ≈ 0.074) is the correct-normalization value, and the referee's δ ≈ 0.019 comes from a mis-normalized kernel.
- **The boost-sign repair is confirmed.**
- **d = 1: confirmed on the lattice ring.** Reruns at L = 1024 reproduce, and the L = 2048 residuals are 1.1e-11 to 3.1e-8.
- **d = 2: confirmed in the chart.**
  - The p-wave doublet and the spin term with α = +1 (forced by [K_x,K_y] = −iJ) are right.
  - The chart round trip holds to 9e-11, and the lattice free generators match to 1e-14.
  - The direct lattice-native run is not a precision check: its residuals are 7e-3 to 0.35. So "every d = 2 commutator verified numerically on the lattice" is not met literally. The FIXED PASS reading (an exact algebra in d = 2 with rotations, and a proved, checked leakage bound) is met.
- **Self-adjointness is correct, with a missing lemma supplied** (bounded-invertible congruence).
- **The interacting leakage theorem is valid** after sharpening step 2 to f(M) − f(M₀) = Q_G[f(M) − f(M₀)]Q_G and spelling out the density step.

**R8-5 (gauge fields in the box) — CONFIRMED WITH CORRECTIONS. FAIL (bounded).**
- **The Ward-identity no-go.** Take conventional Hamiltonian U(1) theories with finite-component, bilinear, translation-covariant, ℓ¹-quasi-local gauge generators. In them the nonzero charge spectrum has constant multiplicity over the Brillouin torus (Lemma C, with an added closedness step). So the complete gauge vertex cannot vanish whenever a fermion leg leaves a proper momentum box.
- **The computed split.** In explicit non-compact Peierls-coupled box QED, the in-box one-loop rules and the Ward identity are exact. Yet the independently checked electron–photon cone split is unsuppressed:
  - Δ ≈ −11 to −71 across nine shapes (in e²/16π² units);
  - −21.8 ± 0.15 as m → 0;
  - about −713 at Wilson edge mass r = 32.
- **Open:** non-minimal transverse couplings, invariant-mass kernels, non-bilinear or power-law generators, Z⁴, and tuning.

**R8-4 (an explicit invariant-mass vertex Hamiltonian) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE.**
- **Model S.** Conditional on a supplied block of four CAR modes per site, model S is a finite-volume, Hermitian, extensively stable, super-polynomially quasi-local quartic Hamiltonian.
- **One loop works, with a fermion factor.** Its on-shell O(g²) dispersion is Lorentz-invariant within the strict spectator and cutoff plateau, after imposing the frame-dependent fermionic factor h = (3W − E)/(W + E). R7-5's lemma fails as written for fermions.
- **Two loops fail in the toy.** For the ordering-truncated toy N, the O(g_o²g_i²) correction depends on momentum: about −6.2% (fermions) and −0.60% (bosons) already at p = m/3. This survives independent Fock, quadrature, Sobol and scaling checks, so radiative closure fails for toy N.
- **Open:** the completed crossing set.
- **Status against the fixed readings.** The two-loop PASS is not met, and the incompatibility FAIL is not proved.

### C5 Round 9, item 7 (pre-registered 17:00Z; launched now)

**R9-7. Two-loop closure with the complete crossing set (the R8-4 open item).**
- The R8-4 referee confirms that the ordering-truncated toy N fails radiative closure at two loops: −6.2% fermion and −0.6% boson at p = m/3. A completed crossing set (2↔2 crossings, reverse decays) is the open restoration route. Its vertex functions are not fixed by the invariant-mass prescription.
- Complete toy N with every time ordering a local relativistic theory would have, giving each new vertex the invariant-mass plateau of the pair or pairs it creates. Recompute the two-loop E² − p².
- Also run the local-limit control: the plateaus are made wide, so the theory approaches a local Lorentz-invariant field theory with a covariant regulator. Does E² − p² become p-independent there?
- If closure fails with the complete set, prove or argue why invariant-mass plateaus cannot be radiatively closed at two loops in a stated class.

Readings:
- **PASS:** with the complete crossing set, the two-loop E² − p² is p-independent to the quadrature floor inside the budget, checked, with fermion and boson both stated.
- **FAIL:** non-closure persists with the complete crossing set for every vertex-function choice in a stated class (refereed).
- **INCONCLUSIVE:** otherwise.

Expectation: INCONCLUSIVE, leaning FAIL. A product of plateaus is not a covariant regulator of a two-loop graph's subdivergences.

### C5 Round 9 referee results, part 1 (recorded 17:08Z)

**R9-1 (edge-sector population) — NOT CONFIRMED as a whole. Only the L / G-out classification survives as recorded: L under G-out is EXCLUDED.**
- **L under G-out: EXCLUDED.** The literal law with a Dirac sea has seven electron corner valleys. Those alone add about 588 MeV to the Z width, for any lattice parameters.
- **G-in is inconsistent, not equivalent to G-out.** For R8-2's free scalar stress kernel, exact conservation of a momentum-diagonal global charge in an arbitrary lapse forces the charge to be constant across the connected Brillouin torus. So a box-supported, Ward-consistent gauge vertex is incompatible with a charged edge. That makes G-in inconsistent within this added class.
- **Not established:**
  - the L dark-matter window;
  - the global G HARMLESS reading.

  The contact ansatz gives Γ/H ∝ (T/M_P)⁷, but its normalization, the broken-phase species composition, the cosmological evolution and the gauge-inert escape are not closed.
- **Momentum.** Crystal momentum is conserved in the instantaneous model, and the A term is the anomalous conversion from canonical momentum to energy current. Claims about total field momentum or the energy centroid are open.

### C5 Round 9, items 8–9 (pre-registered 17:09Z; launched now)

**R9-8. Non-minimal gauge-invariant couplings in box QED (the escape left by R8-5).**
- R8-5 (refereed, FAIL bounded) excludes protection through minimal Peierls coupling: the cone split is unsuppressed. It leaves open transverse non-minimal and invariant-mass gauge-invariant kernels, for example Wilson-line-dressed (Terning-type) non-local vertices with invariant-mass form factors on the charged pair.
- Construct the cheapest gauge-invariant box QED in which the full photon vertex, including its longitudinal part forced by the Ward identity, has an invariant-mass structure, as far as Lemma C allows.
- Compute the one-loop electron and photon speed shifts.
- Identify whether the Ward-forced longitudinal part alone regenerates the split.

Readings:
- **PASS:** an explicit gauge-invariant law with an exact Ward identity whose one-loop cones agree to below 1e-15 relative without tuning, checked.
- **FAIL:** a refereed proof that every gauge-invariant vertex in a stated non-minimal class carries an O(e²/16π²) cone split, or a computed unsuppressed split for the cheapest construction plus a stated-class argument.
- **INCONCLUSIVE:** otherwise.

**R9-9. A box-confined graviton: does the TT mass stay zero under box-matter loops?**
- Give the linearized graviton the box treatment: dispersion ω = |k| in a box, with non-analytic periodic extension and a lattice gauge structure (R8-2's generalized forward-difference divergence, or the 09-14 N-type constraints).
- Couple it to R8-2's universal free box-plus-edge stress.
- Compute the one-loop TT self-energy from box matter (free, number-conserving; then a pair-creating INV variant if feasible):
  - does it keep the TT mass zero (gauge protection) and the TT speed equal to the matter speed;
  - do the E_g and T_2g shear masses (V3: μ_E = 1.97e-3) reappear through the edge?

Readings:
- **PASS:** an explicit box graviton coupled to universal box matter whose one-loop TT mass is zero and whose TT speed matches matter to below 1e-15, without tuning, checked.
- **FAIL:** a computed nonzero one-loop TT mass or speed split that no choice in a stated class removes (refereed).
- **INCONCLUSIVE:** otherwise.

### C5 Round 9, item 10 (pre-registered 17:16Z; launched now; conditional on R9-2, whose referee is running)

**R9-10. The interacting box stress in d = 2: a symmetric (Belinfante) tensor, and the fall of bound bodies with spin.**
- R9-2's worker (unrefereed) builds the d = 1 interacting stress tensor, a Weyl-midpoint density of W, and proves η = 0 for bound bodies on the box sector. In d = 1 symmetry tests nothing.
- In d = 2, take R8-1's refereed two-body law: a p-wave doublet with the spin term in K.
- Construct T^{μν} that is symmetric (a Belinfante improvement for the spin term), Hermitian, quasi-local, exactly conserved with an exact Ward identity on the box sector, has ∫T⁰⁰ = H, and has first moments equal to K_a and J.
- Check the fall of bound doublet states, including spin, between two binding fractions, at rest and moving within the budget. Check the gravitomagnetic (spin–orbit) coupling against the GR value.

Readings:
- **PASS:** all properties are met in d = 2, with bound-body η exactly zero or below 1e-15 at linear order, and the spin coupling equal to GR's, checked.
- **FAIL:** a refereed no-go for a symmetric, conserved stress with first moment K on the d = 2 box sector in a stated class.
- **INCONCLUSIVE:** otherwise.

### C5 Round 9 referee results, part 2 (recorded 17:31Z)

**R9-2 (interacting box stress; bound-body fall; free shear) — CONFIRMED WITH CORRECTIONS. PASS WITH SCOPE in d = 1. (a) is SHEAR-ABSENT in the empty vacuum and SHEAR-PRESENT under a supplied zero-point completion.**
- **The stress tensor.** Take R8-1's repaired graded-CAR two-particle BT law in d = 1, and correct the inverse-Fourier sign. The Weyl-midpoint density then gives a Hermitian, quasi-local stress with:
  - ∫T⁰⁰ = H;
  - energy dipole K;
  - an exact global energy Ward identity;
  - a momentum Ward identity after projection between plateau states, with a transition-shell source outside that scope.
- **Bound bodies fall universally.** On the common invariant box domain this proves Ẍ_E = −g(1 − 2V²). So the linear-order Eötvös violation between equal-velocity bodies of different binding is exactly zero. The operator and real-time checks reproduce.
- **Not established:** d = 2, or a globally source-free interacting stress.
- **Free shear.** It is absent in R8-2's actual empty vacuum. A supplied scalar zero-point completion gives an edge-carried μ_E:
  - −0.20565108 (literal edge) or +0.0079760558 (gapped edge), at m = 1;
  - μ_T2 = 0;
  - a profile-family zero at t* = 0.287922, i.e. an edge tuning.

**R9-3 (Sokolov three-body) — CONFIRMED WITH CORRECTIONS. Literal reading FAIL, as a registration artefact. The physical question is INCONCLUSIVE.**
- **The registration conflict.** Cluster separability necessarily leaves nonzero, un-subtracted spectator-channel limits for B − I and H_S − H_BT. So FIXED clauses (c) and (d) are incompatible as worded, and the literal reading is FAIL. This exposes a defect in the pre-registration, not in the physics.
- **The physical question (subtracted tails, assembled operators) remains INCONCLUSIVE.**
  - The tested B_b − I and B_c − I track smooth compact form-factor Fourier proxies, but no uniform super-polynomial operator bound follows.
  - B, H_S and K_S were not assembled.
  - Finite rings at P ≠ 0 need a discretization prescription.

**R9-4 (covariant CQ escapes) — CONFIRMED WITH CORRECTIONS. All variants OPEN, with narrow EXCLUDED subclasses.**
- **What is excluded.** Take translation- and Lorentz-invariant linearized Gaussian CQ models that admit a stationary linear-meter dilation (the condition under which (H-T) follows frequency by frequency), with a standard retarded G_R and one-sided cone limits:
  - **(i) Spacelike-only noise** forces a response jump whose generic radiation contains (ln r)/r. EXCLUDED in that class.
  - **(ii)** Scalar noise cannot pay for a GR-normalized spin-2 response, and additive repairs inherit R8-3. So literal and additive (ii) are EXCLUDED.
- **(H-T) is not proved for general CP Gaussian CQ histories.**
- **(iii):** OWD Eq. (27) is additive. Correlated, emission-cancelled histories remain open.
- **(iv):** preferred-frame UV convergence needs integer n ≥ 3. This correction to R8-3 is confirmed. The near-cone kernel and cosmological inputs do not establish an allowed window.

**R9-5 (box law on ⊗M₂) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE.** The complementary sectors' global gap was not computed or bounded.
- **The construction.** In d = 2 there is an explicit one-qubit-per-site brick-wall Pauli-string Hamiltonian with super-polynomially quasi-local interaction. Its simply connected flux-free invariant direct sum is exactly unitarily equivalent to R7-1's free Fock law, up to gauge-edge multiplicity and a constant.
- **Consequence.** The undeformed Poincaré Lie algebra holds on the box domain at every finite particle number: even N in the vacuum representation, odd N in the ε representation.
- **Visons.** Flux variables are exactly conserved, so vison configurations are static, and local spin operators can leave the flux-free subspace.
- **The plaquette threshold.** Δ_v = 0 does not select the flux-free vacuum. The tested threshold is about 3.81e-3, but no bound covers every flux configuration.
- **Evidential status.** The tail constants are numerical estimates. The non-forward T-matrix is strong but uncontrolled evidence for Lemma S's hypothesis.
- **Reading.** A genuine sector-qualified qubit realization, not a PASS under the fixed clause.

**R9-7 (two-loop complete crossings) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE.**
- **The crossings and signs are right.** For the selected O(g_o²g_i²) topology, the complete set has 24 orderings, and the finite-Fock formula and fermion signs are correct.
- **Completing the crossings removes the local ordering artefact.** In the 1+1D continuum-dispersion extension, the 10-ordering residual tends to −0.54%, whereas the full local bosonic sum is covariant.
- **The registered completion P1 still leaves residuals:**
  - bosons: +4.76e-4;
  - fermions: −1.35% to −3.62% (tested sign choices).
- **P2 closes exactly for bosons,** but is not box-confining and fails for the tested fermions.
- **The mass-insertion mechanism** is strong finite-family evidence, not a class no-go.
- **The actual completed fixed-box Hamiltonian is untested,** because P1, P4 and P2swap leak outside the box.
- The 24 orderings remove most of toy N's failure.
- The registered completion P1 still fails: +4.8e-4 for bosons, −1.3e-2 to −3.6e-2 for fermions.
- P2 closes exactly for bosons, but keeps no leg in the box.
- The residual falls steeply with m/Λ in 1+1D.

**R9-9 (box graviton) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE.** The class-wide FAIL is not established; it holds only for a narrow prescribed coupling.
- **The tree level is exact.** The N-type graviton with the smooth non-analytic symbol d(q) gives:
  - an exact linear constraint algebra;
  - two TT modes with ω = |q| in the box;
  - no graviton doubler;
  - an exact midpoint-phase Ward coupling to R8-2's number-conserving stress.
- **Theorem T (confirmed).** For pair-creating scalar TT vertices independent of k_z and q, the one-loop paramagnetic coefficient obeys Ξ = ⟨|V|²[Hess_zz(ε²/2) − 1]/ε⁵⟩/32. It is negative for the gapped edge and positive (numerically) for the literal edge. This is a robust graviton-sector speed anomaly carried by Theorem E's edge anomaly.
- **The narrow FAIL.** The fixed minimal-metric coupling and seagull give a nonzero E_g − T_2g mass split throughout the tested L → G edge family.
- **Why it is not class-wide:**
  - the pair-creating stress is not completed to Ward-exact universal coupling;
  - the seagull is not fixed by a second-order Ward identity, and general ultralocal polarization-dependent seagulls can cancel the mass split;
  - the dressed matter speed was not computed.

### C5 Round 10, items 1–2 (pre-registered 17:52Z; launched now)

**R10-1. Is the edge anomaly unremovable? A one-loop "anomaly-inflow" no-go for box-confined lattice field theories.**
- Three results point to one mechanism: the zone-averaged boost anomaly. Over any periodic band, Hess(ε²/2) − 1 averages to −I.
  - R8-2 Theorem E (refereed): edge quanta fall wrongly.
  - R8-5 (refereed FAIL, bounded): the box-QED cone split is unsuppressed.
  - R9-9 (worker FAIL): c_T² − 1 is an average of A_zz.
- Question: in a stated class, is every one-loop Lorentz-violating coefficient a zone integral of A = Hess(ε²/2) − I weighted by a coupling-dependent positive or signed measure? If so, can the weights be chosen to cancel it for every observable at once, with no tuning per species and per observable?
- Probes:
  - (a) Generalize R9-9's Theorem T and Lemma N to Dirac (sea) matter and to the photon (R8-5's split).
  - (b) Find the minimal set of independent "anomaly moments" that every one-loop LV coefficient depends on.
  - (c) Count the tunings needed to null them all, against set C's count.
- The class must allow non-analytic bands, box-supported or invariant-mass vertices, and Ward-forced couplings.

Readings:
- **DERIVED (no-go):** in the stated class, a proof that the one-loop LV coefficients are moments of A that no untuned choice nulls simultaneously (refereed). Recorded as: the box route needs tunings or a non-periodic momentum space.
- **REFUTED:** an explicit untuned choice nulling every one-loop LV coefficient, checked.
- **SUGGESTED:** otherwise.

**R10-2. Set B with box symbols: does a Euclidean Z⁴ law with box-exact O(4) symbols reduce set B's graviton tunings (11)?**
- Set B's hypercubic Z⁴ protects dimension-4 matter operators but needs 11 graviton tunings (K1; R6-2 form counts 3 + 9 against 2 + 4).
- Apply the box trick in Euclidean 4-momentum: symbols that are exactly O(4)-covariant on a 4D box and periodic outside, for matter and for the graviton. Count the remaining graviton tunings at tree level and one loop.
- Does reflection positivity (OS) survive non-analytic box symbols?
- Do the R2-1 (Theorem T, tower) and R2-4 (γ ≤ ½) results bind?

Readings:
- **PASS:** a reflection-positive Euclidean Z⁴ law with box-exact symbols whose graviton needs ≤ 2 tunings (mass plus Λ) at one loop, checked.
- **FAIL:** a refereed no-go: OS positivity fails for box symbols in a stated class, or the tuning count does not fall.
- **INCONCLUSIVE:** otherwise.

### C5 Round 10, items 3–4 (pre-registered 18:01Z; launched now)

**R10-3. Set A: an emission-cancelled classical–quantum hybrid (the R9-4 (iii) open route).**
- R9-4 (refereed) leaves open correlated, emission-cancelled Gaussian histories: classical at spacelike transfers, quantum-cancelled at timelike ones.
- Build the simplest explicit model: linearized, a stationary meter dilation with correlated measurement and feedback, cancelling backaction on the timelike cone.
- Compute:
  - the Newtonian limit (inside R6-4's window);
  - γ and c_T;
  - the null-cone pumping (R8-3's second horn);
  - the vacuum-excitation rate;
  - the absorption rate of timelike-transfer matter states into the meter;
  - the BMV prediction (entanglement or none).

Readings:
- **VIABLE:** an explicit model passing all stated tests with named prices, with its BMV prediction stated.
- **EXCLUDED:** a refereed inconsistency or bound violation for the model class.
- **OPEN:** otherwise.

**R10-4. Λ's mean in set A via a conserved record charge with free volume (q-theory, refining R5-3 route 4).**
- R5-3 (refereed) shows that zero vacuum stress needs a conserved count, a free volume, and gravity coupled to ε − μn (Gibbs–Duhem, Klinkhamer–Volovik q-theory). Set A has a continuum base, so volume is free.
- Can set A's records supply a conserved q-type charge? For example: a 3-form or 4-form record density, records as permanent marks whose density is a conserved current, or the record count per comoving volume.
- Then test:
  - does equilibrium give ⟨Λ⟩ = 0 without tuning, and survive phase transitions (Lemma PT's escape class "dynamical compensators")?
  - what sets today's small Λ (relaxation, or a residual from non-equilibrium formation)?
  - observational checks: w(z), DESI DR2, BBN and CMB constraints on a q-field.
- The owner's "count rises until frozen" is tested as a hypothesis only.

Readings:
- **VIABLE:** a model with records as the q-charge giving ⟨Λ⟩ = 0 across phase transitions without tuning, consistent with the stated bounds, with prices named.
- **EXCLUDED:** a refereed inconsistency, e.g. records cannot be a conserved q-charge under the Record axiom, or a bound is violated.
- **OPEN:** otherwise.

### C5 Round 9–10 referee results (recorded 18:14Z)

**R9-6 (d = 3 rotation-multiplet box law) — CONFIRMED WITH CORRECTIONS. PASS WITH SCOPE.**
- **The algebra.** Conditional on the graded-CAR, continuous-time, number-conserving two-body BT law (not derived from the axioms), the rotationally scalar d = 3 p-wave triplet with K = ½{H, X_NW} + (P × S)/(M + H) has α = 1 forced. It satisfies the exact undeformed Poincaré Lie algebra on the plateau domain.
  - The 45 chart commutators converge from 5.5e-7 (NP = 28) to 1.5e-10 (NP = 40).
  - The lattice triplet mass converges to independence of direction and P.
- **Rotations and leakage.** The interaction support is in |k| < 1.548 < B, so:
  - the ball sector carries exact E(3);
  - the whole-torus Hamiltonian commutes with every deformed rotation flow, though those flows do not form SO(3) off the cube;
  - the rotation and boost leakage theorems hold.
- **Scope:** a two-particle common-domain Lie algebra. It is not an exponentiating sector, and it covers neither N ≥ 3, pair creation, loops, gauge fields, Ward identities nor gravity.

**R9-8 (non-minimal box QED) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE.**
- **Proved for the smooth BQ-W FW-frame family with symmetrized-staircase Wilson lines:**
  - gauge invariance fixes the zero-transfer charge and velocity vertex;
  - a regular Hamiltonian vertex has a nonzero four-transverse part;
  - an invariant-energy profile cannot multiply the full forward pair current except at F = 0 or 1.
- **Numbers, checked independently:**
  - Δ = −33.5860 e²/16π² at (0.5, 1.9);
  - all 15 quasi-local staircase cases have |Δ| ≥ 12.9;
  - path changes move the photon coefficient by −5.5 to −69.3.
- **Scope.** This strongly rejects protection in the cheapest construction, but it is not a stated-class no-go.

**R9-10 (d = 2 Belinfante box stress) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE.** The fixed GR-spin clause is unmet.
- **The stress.** Conditional on R8-1's d = 2 law and the first-moment lapse bridge, the Weyl-midpoint density has total H and dipole K, spin term included. A valid KB/Belinfante division gives a symmetric, Hermitian, Gevrey-quasi-local stress with:
  - exact global energy conservation;
  - box-to-box momentum conservation, with off-box shell and torque sources;
  - J_T = J box-to-box.
- **Existence only.** This is an analytic existence result. The checked closed-form chart realization is not the global quasi-local flux.
- **Bodies fall universally.** On the box domain, Ẍ_E = −g + 2(g·V)V. So the linear-order Eötvös violation between bodies of different binding or spin is exactly zero.
- **Spin.** The checks establish the special-relativistic uniform-acceleration term and unit rigid-rotation coupling. They do not establish GR's curved-field geodetic or spin-curvature coupling.

### C5 Round 10, item 5 (pre-registered 18:13Z; launched now; conditional on R10-1, whose referee is running)

**R10-5. An edge supertrace: does boson–fermion pairing on the box edge cancel every one-loop Lorentz-violating coefficient (photon, electron, graviton)? And does it touch the vacuum energy?**
- R10-1's worker (unrefereed) proves Theorem P: Clifford-flat fermions plus two matched complex scalars cancel the photon's one-loop speed shift for every edge shape (a supertrace). The electron's own shift (−11 to −18) and the graviton sector are not paired.
- O3 (refereed) found that untuned vacuum-energy cancellation needs matched boson and fermion spectra. A qubit site cannot hold both, and lattice supersymmetry (Fendley–Schoutens) is a costly escape.
- Build the minimal "edge-SUSY" box law: superpartner loops (a selectron and photino analogue, with a Yukawa vertex fixed by a lattice supercharge) such that the electron self-energy is supertrace-paired too. Compute:
  - the residual one-loop c_e − c_γ;
  - Theorem T's graviton speed moment with superpartners;
  - the one-loop vacuum energy.
- Test whether one exact lattice supercharge Q with Q² = H (or a Nicolai-type map) can be imposed on the box law at all, and with what per-site content.

Readings:
- **PASS:** an explicit law with a stated lattice supersymmetry whose one-loop c_e − c_γ and graviton TT speed shift vanish for every edge shape (mass-split residuals stated), checked, with per-site content and prices named.
- **FAIL:** a refereed no-go: no lattice supercharge compatible with box symbols and Ward-forced gauge coupling exists in a stated class, or the pairing provably cannot cancel the electron self-energy.
- **INCONCLUSIVE:** otherwise.

### C5 Round 11 (pre-registered 18:35Z from the S11 synthesis, agents/C5_S11_synthesis.md; readings fixed as drafted below)

Launch: R11-2 through R11-6 now; R11-1 after the R10-1 referee. Draft text verbatim from S11 §6:


**Rules (as rounds 2–10).**
- Probes: Opus 5.5 at xhigh.
- Every FAIL, EXCLUDED or no-go goes to codex gpt-5.6-sol (xhigh) before it is recorded.
- Prices are named, never adopted.
- Each probe greps the repository and packet for prior art first and counts each match once.
- Hypotheses are stated before titles; excluded outside realizations are listed.
- Numbers from memory are labelled RECALLED unless verified.
- **New rule (from R9-3's defect).** Every tail or decay clause names its subtraction (which channel limit is subtracted) before any run.

**Overlap check.**
- R10-3 is emission-cancelled CQ (variant iii). R11-5 is variant (iv) only.
- R10-4 is set A (free volume, records as q-charge). R11-3 is sets C and C-box (fixed grid). It does not test records as a q-charge.
- R10-5 builds the edge-SUSY law and computes c_e − c_γ, the graviton TT speed with partners, and the one-loop vacuum energy. R11-1 asks the converse (is pairing *necessary*?) and computes the matter self-energy from graviton loops, which R10-5 does not.
- R11-2, R11-4 and R11-6 overlap nothing running.

**Priority.** R11-1 (after R10-1's referee), R11-2, R11-3, R11-4, R11-5; R11-6 when a slot frees.

---

**R11-1. Is an edge supertrace necessary? And the dressed matter speed under graviton loops.**
*(Launch after R10-1's referee. If Theorems T′, P or Lemma N(m) are not confirmed, use only refereed Theorem T and prove T′ inside the probe.)*

- **Plain question.** The box route's one-loop light-speed shifts all live on the edge. R10-1's worker found one way to cancel one of them: bosons and fermions contributing with opposite signs. Is that the *only* untuned way, or can some edge shape or vertex choice do it without pairing? Separately, R9-9 computed the graviton's speed shift but not the matter's shift from graviton loops. Without it, "graviton and matter on different cones" is not yet a computed fact.
- **Setting (class 𝒞_A).**
  - Z³ × ℝ, continuous time, Gaussian matter species s with C² periodic bands, box-exact on an open box (H-box, `C5_R10-1_report.md:67-96`).
  - Gauge and graviton vertices are Ward-forced onto the whole zone (Lemma C `TESTS:3808`; Lemma Q `TESTS:3841`).
  - Species are complex scalars or Clifford-flat fermions, the subclass in which each one-loop coefficient is a signed A-moment.
  - "Untuned" means: band shapes and vertices are fixed per statistics and do not depend on the observable or the mass.
  - Excluded: the Dirac class (D) with non-zero a- and mixing-moments (stated as outside); interactions beyond one loop; set C's own discretization.
- **Prior art (count once).**
  - R8-2 Theorem E (`TESTS:3556`);
  - R9-9 Theorem T and Lemma N with its richness caveat (`vR9-9:12-14`);
  - R10-1 Theorems T′, D, P and Lemma N(m) (pending, `C5_R10-1_report.md:137-260`);
  - O3 Theorem 1a, equal signed DOS (`TESTS:2400`);
  - R10-5 (running; do not duplicate its construction);
  - Nielsen–Ninomiya (RECALLED).
- **Probes.**
  - (a) **Necessity.** Suppose C_O(m) = 0 for every m² in an interval and every O in {photon speed, graviton TT speed}, with no per-O tuning. Prove or refute: the species' band pushforward measures must pair across statistics, observable by observable. A counterexample must be explicit and checked.
  - (b) **Dressed matter speed.** Compute the one-loop matter (scalar) self-energy from R9-9's tree-level box graviton, on the L and G edges, at m = 1 and 0.3. Give c_matter − c_T at one loop, including R9-9's Ξ, in units of κ_lat²/(16π²a²). State the size at a = ℓ_P (a reading on `AX:189-190`).
  - (c) Restate the one-loop count with and without pairing. Note any change from R10-1's referee.
- **FIXED readings.**
  - (a) uses the derivation readings (`TESTS:2314-2318`):
    - **DERIVED:** pairing is necessary in 𝒞_A, proved (refereed);
    - **REFUTED:** an explicit unpaired untuned choice nulls both coefficients for all m² in an interval, checked;
    - **SUGGESTED:** otherwise.
  - (b) is reported as:
    - **SPLIT-PRESENT:** c_matter − c_T ≠ 0 computed for both edges, with the number;
    - **SPLIT-ABSENT:** it vanishes identically, with the reason;
    - **OPEN:** otherwise.
    - A SPLIT-PRESENT claimed as class-wide goes to the referee.
- **Expectation.**
  - (a) DERIVED in 𝒞_A. The mass-independence plus Laplace uniqueness argument of Lemma N(m) should force equality of signed measures, as O3's Theorem 1a does for vacuum energy. SUGGESTED beyond 𝒞_A.
  - (b) SPLIT-PRESENT, sign-definite on the gapped edge (A_zz ≤ 0 there, `vR9-9:12`), unsuppressed at a = ℓ_P.

---

**R11-2. Producing the graviton: a qubit realization of the weak N-type box graviton, and Weinberg–Witten on box domains.**

- **Plain question.** In every set the graviton is put in by hand. Lane R found one gauge structure on Z³, the weak N-type (Gu–Wen "weak" type), with two light-like graviton modes and a 1/r pull. R9-9 gave it a box law that is exact at tree level and couples exactly to box matter. The decisive test named in `SUMMARY:290` was never run: can one qubit per site, with local terms only, *produce* that field as its low-energy sector, the way R9-5 produced box matter? And does Weinberg–Witten, which forbids composite gravitons, apply when boosts are exact only inside a budget?
- **Setting.**
  - ⊗_{Z³} M₂(C), local or super-polynomially quasi-local terms.
  - The constraints are enforced energetically (stabilizer- or ice-type) or as invariant sectors (R9-5 style). At linear order the N-type constraints commute, as linearized diffeomorphisms are abelian (RECALLED; verify in the probe).
  - The target is R9-9's tree-level box graviton: an exact linear constraint algebra, 2 TT modes with ω = |q| in the box (or ω ∝ |q| at low q), no doubler (`TESTS:3940-3944`).
  - Matter: R9-5's flux-free fermion sector, or constraint violations (defects).
  - Excluded: nonlinear gravity; pair-creating matter; Λ.
- **Prior art (count once).**
  - lane R, `TESTS:685-776`, notably R1 and R2 at `:740-760`: "V gives k², VS gives k³ in the regular analytic compact class"; "a noncompact IR field can emerge from qubits"; strong-class mode counts 5/4/3/2;
  - the 09-14 note (`docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`);
  - PR #9363 probes 10–21;
  - R6-2 (`TESTS:3331-3343`);
  - R9-9 (`TESTS:3939-3950`); R9-5 (`TESTS:3917-3923`);
  - `OUTSIDE_VIEW.md:46,49` (Gu–Wen, Xu, Pretko);
  - Gu–Wen 2009 helicity-±2 model, Xu 2006, Pretko 2017 (RECALLED).
  - Read every section naming "N-type" or "weak VS" before building.
- **Probes.**
  - (a) **WW on box domains.** Does the Weinberg–Witten proof go through when finite boosts act exactly only on a budget-limited domain? This covers (i) a composite spin-2 state made of box matter and (ii) a gauge graviton without a gauge-invariant stress. State which step uses unbounded boosts.
  - (b) **Construction.** Build the cheapest ⊗M₂ Hamiltonian whose constraint-satisfying low-energy sector carries the N-type gauge structure. Compute its emergent dispersion (perturbative ring exchange or exact sector map), its mode count, and any extra helicity-1 or 0 modes.
  - (c) **Box symbol.** Can the box trick (R9-9's d(q)) be applied to the emergent field's effective symbol? Or is the emergent dispersion fixed by the constraint structure (k² or k³, as lane R found)?
  - (d) **Source.** Do matter excitations source the emergent field through their energy-momentum (universal, Ward-exact) or through an emergent charge (lane R's failure mode)?
  - (e) Name the prices.
- **FIXED readings.**
  - **PRODUCED:** an explicit ⊗M₂ quasi-local model whose stated low-energy sector contains exactly two TT modes, light-like in a box (or at low q), with the N-type constraint algebra, no extra gapless modes, and matter coupling through a Ward-exact universal stress, checked.
  - **EXCLUDED:** a refereed no-go that, in a stated class of ⊗M₂ constraint models on Z³, the emergent tensor field is never light-like or never couples to energy-momentum.
  - **OPEN:** otherwise. Report (a) separately as DERIVED / REFUTED / SUGGESTED.
- **Expectation.**
  - (a) SUGGESTED: WW binds composite TT states built from box matter inside the budget; it does not bind a gauge graviton, as in GR.
  - (b)–(d) OPEN. Most likely an emergent field with k² or k³ dispersion, or one sourced by an emergent vector or fracton charge rather than by energy. A light-like N-type sector from qubits would be the campaign's first produced graviton.

---

**R11-3. Λ's mean on a fixed grid: the volume mode, the vacuum's tadpoles, and its equation of state (sets C and C-box).**

- **Plain question.** On a continuum (set A), space can expand freely. On the axioms' Z³ the sites are fixed. So what is the universe's expansion on a grid? Either the proper spacing grows, making the volume a field, or new sites appear, a price on Lattice. Does the vacuum energy push on that volume mode? If space's volume per site were fixed, the vacuum's energy might stop gravitating, as in unimodular gravity. Separately, a grid vacuum need not have pressure equal to minus its energy (w = −1). If it doesn't, it is not a cosmological constant at all, and cancelling it costs two numbers, not one.
- **Setting.**
  - R9-9's N-type box graviton (lapse N, shift N_i, h_ij) on Z³ × ℝ, coupled to R8-2's stress with R9-2's supplied scalar zero-point completion, on the L and G edges. Add a Dirac sea if feasible, gapped edge only (P38).
  - Three options for the volume mode:
    - (V1) the trace h_ii is dynamical (spacing grows);
    - (V2) √h is fixed per site (a "spatially unimodular" grid), lapse dynamical;
    - (V3) the lapse is also fixed (a projectable, preferred-time grid).
  - Excluded: records as a q-charge (R10-4); edge-SUSY (R10-5; use its vacuum result only as a control if it has reported).
- **Prior art (count once).**
  - R5-3 route 1 (unimodular with Λ an integration constant; `TESTS:2888-2889`, result `:2985-2993`);
  - lane RN's "TDiff, unimodular, Hořava are not escapes" (for the graviton's mass, `TESTS:809,870`; a different question, counted once);
  - R9-2 free shear (`TESTS:3897-3900`);
  - O3 (`TESTS:2399-2404`);
  - R4-5 everpresent-Λ unimodular conjugacy (`TESTS:2939`);
  - `docs/COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md` and every repo doc on the cosmological constant;
  - comparator: momentum-cutoff vacuum w = 1/3 (Akhmedov; Koksma–Prokopec; RECALLED).
- **Probes.**
  - (a) **Tadpoles.** Compute ⟨T⁰⁰⟩_vac and ⟨T^ij⟩_vac (isotropic p_vac; anisotropic part = R9-2's shear), split into box and edge contributions, for L and G. Give w = p_vac/ρ_vac for each part, and test whether any edge profile gives w = −1 without tuning. State any zone-integral identity relating ρ_vac + p_vac to A-moments.
  - (b) **Decoupling.** For each of V1–V3, does a step change in ρ_vac (a phase transition: change one species' m) source curvature or expansion? Derive it in the linear N-type theory.
  - (c) **Expansion.** For each option, state how a FRW-like expansion is realized: growing spacing, site creation, or none. Give the consequence for the rapidity budget in physical units and for the scale reference (`AX:189-190`).
  - (d) Name the prices per option.
- **FIXED readings (per option V1, V2, V3).**
  - **DECOUPLED:** vacuum-energy shifts, including a phase-transition step, provably do not source curvature or expansion; the residual Λ is named as an integration constant, and prices are named.
  - **SOURCED:** the vacuum sources the volume or lapse mode with computed coefficients (ρ_vac, p_vac, w stated). The mean remains a tuning. If w ≠ −1 is claimed to cost two tunings, that goes to the referee.
  - **EXCLUDED:** the option is inconsistent with observed expansion or with the N-type constraint algebra (refereed).
  - **OPEN:** otherwise.
- **Expectation.**
  - V1: SOURCED, with the edge part's w ≠ −1, so two tunings (ρ and p) instead of one.
  - V2: SOURCED through the lapse, since ρ_vac√h still enters the Hamiltonian constraint.
  - V3: DECOUPLED at linear order, but EXCLUDED or OPEN on expansion: a fixed grid with fixed lapse cannot expand without site creation, a Lattice price, which links to the owner's "count rises" thought, tested only as a hypothesis.

---

**R11-4. Box bodies in a curved field: the space–space coupling (γ), von Laue, geodetic precession and the spin–curvature force (d = 3).**

- **Plain question.** Every gravity test of box bodies so far used a uniform field coupled to the energy's first moment. Light bending, Shapiro delay and the precession of a spinning gyroscope test the rest of the coupling: how a body's internal pressure and momentum flow respond to curved space. A bound body at rest has zero total internal stress (von Laue's condition) only if its momentum is exactly conserved. In the box law momentum is conserved only box-to-box. Does the condition still hold, and does a spinning bound body precess at GR's rate?
- **Setting.**
  - R9-6's d = 3 two-body triplet law (`TESTS:4016-4024`).
  - A d = 3 symmetric stress built as in R9-10 (Weyl midpoint plus KB/Belinfante division).
  - Linear coupling ½h_μν T^μν to prescribed static fields: (i) uniform lapse (control); (ii) isotropic linearized Schwarzschild, h₀₀ = −2Φ, h_ij = −2γΦδ_ij with γ = 1; (iii) a pure tidal field; (iv) gravitomagnetic h₀ᵢ.
  - Fallback if the d = 3 stress is not constructible in time: d = 2 for von Laue and tidal only, with that stated.
  - Excluded: pair creation; N ≥ 3; nonlinear gravity.
- **Prior art (count once).**
  - R9-2 (`TESTS:3889-3900`); R9-10 (`TESTS:4037-4044`, the unmet GR-spin clause `vR9-10:21-22`); R9-6;
  - R8-2's stress (`TESTS:3554`); R7-4's conditional exclusion (`TESTS:3496-3497`; `vR9-2:17`);
  - comparators: Gravity Probe B geodetic precession (3/2, about 0.3%), Cassini γ, Mathisson–Papapetrou–Dixon force, von Laue's theorem (RECALLED unless verified).
- **Probes.**
  - (a) Construct the d = 3 stress: symmetric, Hermitian, quasi-local, ∫T⁰⁰ = H, first moments K and J, box-to-box momentum conservation, sources stated.
  - (b) **Von Laue.** Is ∫T^ij = 0 for bound states at rest, exactly on the box domain? Compute any shell-source contribution as a function of binding.
  - (c) The passive coupling to (ii): the acceleration and the effective γ of bound bodies of two binding fractions, at rest and moving within the budget.
  - (d) The geodetic precession of the triplet's spin in (ii), against 3/2; the MPD force in (iii); the frame-dragging response to (iv).
- **FIXED readings.**
  - **PASS:** (a) met; von Laue exact on the box domain; the effective γ is binding-independent and equal to 1 at linear order; geodetic 3/2 and the MPD force reproduced, checked.
  - **FAIL:** a computed binding-dependent γ or a precession ≠ 3/2 at linear order that no choice in a stated class removes (refereed).
  - **INCONCLUSIVE:** otherwise.
- **Expectation.** PASS on the box domain. Von Laue follows from box-to-box momentum conservation for stationary bound states, and 3/2 follows from ½h_μνT^μν with a symmetric von-Laue stress (S11 expectation). The risks: the second moments (x² weights) needed for tidal and MPD terms may reach the shell sources, and the d = 3 global quasi-local flux may again be existence-only. INCONCLUSIVE overall is likely.

---

**R11-5. Set A: a regulated preferred-frame CQ kernel and its window (R9-4 variant iv).**

- **Plain question.** The simplest relativistic forms of "the records are the classical metric" are excluded. One open form keeps a preferred frame, with noise tied to it. That needs a UV power n ≥ 3 and a regulator at the light cone. Build one, then ask whether any smearing length survives every bound, including effects of Earth's motion through the frame.
- **Setting.**
  - Linearized Gaussian CQ gravity with mean GR coupling and noise kernel D(ω, k) defined in a preferred frame u^μ (taken as the CMB frame).
  - Integer n ≥ 3 UV falloff. An explicit regulator or restricted domain at the cone, making D′₀ a locally finite positive measure.
  - Spatial smearing ℓ_s.
  - Excluded: correlated emission-cancelled histories (R10-3); trace-only kernels already excluded (`TESTS:3911-3912`).
- **Prior art (count once).**
  - R6-4 (`TESTS:3409-3418`); R8-3 (`TESTS:3559-3573`); R9-4 (`TESTS:3909-3915`; `vR9-4:11`);
  - R4-4 Lemma N (a BMV-type positive result excludes every variant, `TESTS:2935`);
  - PPN preferred-frame bounds α₁, α₂ (RECALLED; verify).
- **Probes.**
  - (a) Construct the regulated kernel. Prove complete positivity and the mean-field limit.
  - (b) Compute γ, c_T, the vacuum-excitation rate in the frame, and the heating and diffusion rates for matter moving at v ≈ 370 km/s through the frame, including their annual modulation.
  - (c) Compare against:
    - R6-4's decoherence and diffusion bounds (Cs-133 for 70 s; LISA Pathfinder; corrected torsion σ_a² = (48π/5)G²D₂/(RT));
    - Cassini;
    - GW170817;
    - PPN α₁, α₂, if the noise feeds the mean metric at any order.
  - (d) Give the allowed ℓ_s interval, or none.
- **FIXED readings.**
  - **VIABLE:** an explicit regulated kernel passing every stated test, with an allowed ℓ_s interval and named prices.
  - **EXCLUDED:** every regulated kernel in a stated class violates a stated bound for every ℓ_s (refereed).
  - **OPEN:** otherwise.
- **Expectation.** OPEN, leaning VIABLE on a narrow interval inside 2e-7 to 5e-6 m. The new risk is the velocity-dependent heating and its annual modulation, which no earlier probe computed.

---

**R11-6 (when a slot frees). Assembled Sokolov three-body box law with subtracted channel tails (R9-3 re-registered, d = 1).**

- **Plain question.** For three bodies, summing pair forces breaks relativity, and the textbook cure (Sokolov packing) was never assembled on the lattice. R9-3's registration also asked for the impossible. Assemble the operators and measure the right tails.
- **Setting.**
  - d = 1; three spinless fermions; R8-1's pair law with R7-6's plateau; the normalization ½ (`TESTS:3797`).
  - A stated interpolation or discretization prescription for P ≠ 0 rings (`vR9-3:110`).
- **Prior art (count once).** R7-6 (`TESTS:3506-3510`); R9-3 (`TESTS:3902-3907`; `vR9-3:3,26,43,110`); Keister–Polyzou, Coester–Polyzou (as cited there).
- **Probes.**
  - (a) Assemble B, H_S = B H_BT B†, K_S on the three-body box sector, on at least three ring sizes.
  - (b) Check [K, P] = iH, [K, H] = iP, [H, P] = 0.
  - (c) **Subtracted tails (fixed now).** For the spectator channel a = (12)(3), measure ‖(B − B_a)ψ_r‖ and ‖(H_S − H_a ⊗ 1 − 1 ⊗ h₃)ψ_r‖ against separation r over at least 1.5 decades. Use a pre-registered information-criterion comparison of exp(−c r^β) against a power law, over the full range.
  - (d) The trimer invariant mass at P = 0, ±P₁, ±P₂.
- **FIXED readings.**
  - **PASS:** (b) residuals → 0 with L; (d) flat to the discretization floor; (c) super-polynomial by the pre-registered comparison; checked.
  - **FAIL:** a refereed proof that the *subtracted* channel deviations decay no faster than a power, in a stated class.
  - **INCONCLUSIVE:** otherwise.
- **Expectation.** INCONCLUSIVE. The algebra closes by construction; the subtracted tails should track the form-factor proxies (`vR9-3:43`), but a uniform operator bound is unlikely within one run.

---


### C5 Round 10 referee results (recorded 18:46Z)

**R10-1 (edge-anomaly inflow) — CONFIRMED WITH CORRECTIONS. SUGGESTED, with derived parts.**
- **Derived identities.** In free, separable Z³ × ℝ Peierls-coupled box theories:
  - the scalar-QED photon-speed correction is exactly a positively weighted moment of A;
  - the box-QED Dirac correction is exactly a moment of (a, A, c₁, c₂).

  So the registered "A-only" premise is false.
- **Theorem P.** For Clifford-flat unit-speed bands and matched masses, one fermion contribution per four components plus two matched complex-scalar contributions cancel the photon coefficient pointwise, for every edge shape. The actual 8-component realization needs four scalars.
- **What pairing leaves.** The paired electron speed remains δc_e·16π² ≈ −10.66 to −17.96. The scalar speeds, the graviton sector, the Dirac TT sector and higher loops are open.
- **Neither direction proved.** The box anomaly is not proved unremovable, and no counterexample cancels every one-loop coefficient. The claimed total of six tunings is not established.

**R10-2 (Euclidean box symbols, set B) — CONFIRMED WITH CORRECTIONS. FAIL (bounded) on the OS-positivity clause, in the stated class.**
- **Smooth box symbols fail RP.** Take translation-invariant Euclidean lattice laws whose time-local bosonic two-point functions have the standard OS transfer-contraction representation. Their fixed-spatial-momentum slices are real-analytic away from k₄ = 0, π. So the smooth-box Gaussian covariances, and small correlator-continuous perturbations of them, fail both site and link RP.
- **No smooth law is exactly O(4) on a box.** A nonconstant smooth periodic continuum-O(4) two-point function cannot be exact on an open box.
- **The one exception.** Whole-zone scalar SLAC is a sharp link-RP exception. But its positive measure contains negative transfer spectrum approaching −1, which gives time-alternating energies down to zero.
- **Without RP** (and with the full loop integrand confined to an O(4) ball), the codimension falls from 11 to 5 + Λ, not to 2.
- **Other walls.** R2-4 remains conditional on its source and response premises. R2-1 is not re-derived.

**R10-3 (emission-cancelled CQ hybrid) — NOT CONFIRMED as conditional VIABLE. EXCLUDED in class T_E.**
- **The class T_E** (all conditions together):
  - a translation- and Lorentz-invariant stationary Gaussian linear-meter CQ model;
  - a self-commuting, locally finite record and zero reverse gain;
  - standard massless retarded propagation and continuous nonzero cone gain;
  - positive spectral measures, finite vacuum excitation and finite static response.
- **The exclusion.** In this class, exact emission cancellation makes the matter influence field obey zero-temperature quantum-bath detailed balance. But it necessarily makes the classical metric-record covariance non-locally-finite at the light cone, so the finite-time on-shell record energy is unbounded (Cesàro mean/limsup). No record-metric realization exists in T_E.
- **Scope.** The result is channelwise. It does not establish the claimed tensor γ or the spin-2/spin-0 tower.
- **Still open:** emission-cancelled hybrids outside T_E.

**R10-4 (records as a q-charge for Λ) — CONFIRMED WITH CORRECTIONS. OPEN.**
- **What is derived, conditionally.** Supply an additional metric-independent, additive record-history 3-current A, with formation form F = dA. Then the local action ε(*F) yields the Gibbs–Duhem stress.
- **Why the minimal version fails.** Its shift-symmetric equation conserves μ. On a regular branch with a q-independent vacuum jump, Minkowski space afterwards needs μ chosen for the final vacuum, to about 2.1e-55 at the electroweak step. That excludes the minimal conserved-μ realization.
- **Not excluded:** membrane-sourced, dissipative, global, count-dependent, q-coupled-matter and multi-flux completions.
- **No untuned, observationally viable completion was produced.**

**R10-5 (edge supertrace) — CONFIRMED WITH CORRECTIONS. FAIL (bounded), clause 1, to class 𝒮.**
- **The class 𝒮:** the canonical C¹, translation-invariant SUSY-QM/Nicolai class without quadratic gauge–scalar mixing.
- **What holds.** The Clifford-flat matter multiplet has an exact free supercharge and zero matched vacuum energy.
  - The superpotential sign needs correcting.
  - 2⟨1/E⟩Δm² is only the leading small-splitting term.
- **The no-go.** The three-component gauge Hessian must carry helicity Chern number ±2. That forces an extra transverse zero, so a doubler-free box photon is excluded.
- **The graviton.** The stipulated TT pairing cancels the one-loop TT response for matched unit-speed curves. Coupling "through Q" remains Lorentz-violating.
- **The electron.** The tested partner loops enlarge the electron–photon split, but this does not prove a general electron no-go.

### C5 Round 11 worker readings awaiting referees (recorded 18:59Z)

- **R11-2 (producing the graviton):** OPEN overall; (a) SUGGESTED. Candidate no-gos to the referee:
  - X1: exact commuting finite-slot constraints give ω_TT = O(k³), with dressing law ω ∝ k^{3−n};
  - X2: exact linear constraints sourced by matter densities freeze mobile matter (Lemma F).
- **R11-3 (Λ on a fixed grid):**
  - V1 SOURCED: two tadpoles, and w ≥ 0 for every positive band, with ρ + p = −(1/6)⟨ε tr A⟩.
  - V2 EXCLUDED as a fixed-site option.
  - V3 DECOUPLED at linear order, and EXCLUDED as a fixed-site option.
- **R11-4 (box bodies in a curved field):** PASS WITH SCOPE.
  - Theorem PD: on the bound-triplet sector, the moments equal the flat Dixon pole–dipole stress.
  - Von Laue is exact, the effective γ equals the field's γ, the geodetic coefficient is 3/2, and frame dragging matches Schiff.
  - The quadrupole is not fixed (price P-Q).
- **R11-5 (preferred-frame CQ):** VIABLE, conditional on a law with a start time. Lemma C: no stationary version exists. The window is about 5e-7 to 5e-6 m.
- **R11-6 (assembled three-body box law):** INCONCLUSIVE (worker; no FAIL claimed, so no referee is required).
  - B, H_S and K_S were assembled as matrices in a stated free-chart prescription.
  - The algebra and the trimer-mass flatness are exact by conjugation.
  - The registered subtracted-tail measurement is resolution-limited: the spline aliases beyond r ≈ L/6.
  - Matrix-free large-r ingredients favour super-polynomial decay (ΔAICc +4 to +31, β ≈ 0.3–0.45) but are not the registered observable.
  - A dense-grid s_min collapse is traced to an antipodal aliasing artefact.

### C5 Round 12, items 1–2 (pre-registered 19:07Z; launched now)

**R12-1. Graviton production beyond the linear constraint: a lattice hypersurface-deformation (non-abelian) constraint algebra with finite-site matter.**
- R11-2's worker (unrefereed; referee running) argues two things:
  - exact linear constraints sourced by energy freeze mobile matter (X2);
  - the escape is a non-abelian constraint algebra at O(κ²), i.e. nonlinear gravity.
- The continuum hypersurface-deformation (Dirac) algebra has structure functions. Lattice versions are known to be anomalous: LQG's anomaly problem, Bahr–Dittrich perfect discretizations.
- Test:
  - (a) Can a lattice constraint system with finite-site (or box) matter close a deformed algebra {C, C} ~ C to O(κ²), with mobile matter in the physical sector?
  - (b) What fails: anomaly terms, the lattice spacing, structure functions?
  - (c) Do R7-1's box tricks (non-analytic symbols, exact on a box) help the algebra close on box states?
- Prior art: the boost wall (SUMMARY.md §17), lane RN L3, R7-4 (N-type bridge), RFW (field-dependent Ward completion).

Readings:
- **PASS:** an explicit lattice constraint system closing a deformed algebra to O(κ²) with mobile matter in the physical sector, on a stated domain, checked.
- **FAIL:** a refereed no-go for closure at O(κ²) with mobile finite-site matter, in a stated class.
- **INCONCLUSIVE:** otherwise.

**R12-2. Site creation and Λ: can a local rule that creates sites track the expansion and fix the vacuum value without tuning?**
- R11-3's worker (unrefereed) finds that fixed-site options V2 and V3 can expand only by creating sites. The vacuum question then moves into the value C assigned to new sites: a fixed constant brings back Lemma PT, and a vacuum-tracking value is O3's P13.
- The owner's thought "count rises" (a hypothesis, not a rule) suggests that records forming on new sites drive the expansion.
- Construct a local site-creation rule on Z³ (refinement or insertion) and test:
  - (a) Can it track Friedmann's law using only local, non-vacuum data?
  - (b) What C do new sites get, and is ⟨Λ⟩ = 0 untuned across a phase transition?
  - (c) Do redshift, the rapidity budget, and the Lattice axiom's "no site is privileged" survive?
  - (d) Observational checks: w(z), and isotropy, where insertion is anisotropic on a cubic grid.

Readings:
- **VIABLE:** an explicit local rule giving Friedmann expansion and ⟨Λ⟩ = 0 untuned, passing the stated checks, with prices named.
- **EXCLUDED:** a refereed inconsistency, or a violated stated bound.
- **OPEN:** otherwise.
- **R11-1 (pairing necessity; dressed matter speed):** worker readings below. Referee running (19:08Z).
  - **(a) DERIVED** in 𝒞_A:
    - Theorem N*: interval vanishing forces boson–fermion cancellation of A-weighted measures, so neither statistics alone suffices;
    - Theorem S: in a subclass, minimal pairing is forced.
  - **(b) SPLIT-PRESENT** in prescription dD-M only:
    - the matter shift is O(κm²) (Lemma M);
    - so for light matter c_m − c_T → −κΞ, unsuppressed;
    - the sign on the gapped edge is not definite.

### C5 Round 12, item 3 (pre-registered 19:10Z; launched now)

**R12-3. Twisted lattice supersymmetry outside class 𝒮: does a doubler-free gauge multiplet exist, and does Groot Nibbelink–Pospelov protection (no dimension-4 LV in SUSY theories) remove the electron–photon split?**
- R10-5 (refereed, FAIL bounded to 𝒮): in the canonical SUSY-QM/Nicolai class without gauge–scalar mixing, the photino carries Chern ±2, which forces photon doublers. Its named escapes are twisted N=2 equivariant constructions with the scalar a, KKU-type orbifolds with A–scalar mixing, light-cone supercharges, and non-C¹ symbols.
- The comparator (Groot Nibbelink–Pospelov, hep-ph/0404271, recalled) says SUSY forbids dimension-4 Lorentz-violating operators. With SUSY, LV starts at dimension 5, so it is Planck-suppressed.
- The electron–photon split is the one coefficient nothing has removed so far:
  - R8-5 (refereed) and R9-8: unsuppressed;
  - R10-1 and R10-5: pairing leaves it.
- Construct the cheapest Hamiltonian lattice gauge multiplet (twisted N=2 or orbifold, with A–scalar mixing) on Z³ × ℝ with box symbols, coupled to the Clifford-flat matter multiplet. Then:
  - (a) Is the photon doubler-free? What is the Chern bookkeeping once the scalar mixes?
  - (b) Is one supercharge exact with the Ward identity?
  - (c) Compute the one-loop c_e − c_γ. Does it vanish, or is it suppressed to dimension 5?
  - (d) Name the per-site content and prices.

Readings:
- **PASS:** an explicit lattice gauge-plus-matter law with an exact supercharge and Ward identity, a doubler-free photon, and a one-loop c_e − c_γ vanishing (or dimension-5-suppressed) for every edge shape, checked.
- **FAIL:** a refereed no-go extending R10-5's Chern obstruction to the twisted or orbifold class.
- **INCONCLUSIVE:** otherwise.

### C5 Round 11 referee results (recorded 19:31Z)

**R11-1 (pairing necessity; dressed matter speed) — CONFIRMED WITH CORRECTIONS.**
- **(a) DERIVED in the stated class.**
  - **The class.** Finitely many species in 𝒞_A, with affine mass-squared families and nonnegative, longitudinally independent, nonvanishing weights.
  - **The result.** Cancellation on an open mass interval forces the aggregate rescaled A-weighted boson and fermion measures to cancel separately for each observable. So both statistics are necessary, though pairwise species matching is not forced in general. The analyticity domain is M > M₀.
  - **The subclass result.** In the one-curve, monotone, no-doubler, c_γ = 1 subclass, with the anomaly-onset and parity hypotheses made explicit:
    - Titchmarsh plus ODE uniqueness forces u = v;
    - the TT condition forces w = 2√(N_F/N_B)S², i.e. w = S² for the four-scalar / eight-component unit.
- **(b) SPLIT-PRESENT in prescription dD-M only.**
  - The on-shell scalar matter correction is c_m² − 1 = 4κm²J₂.
  - The m = 1 and 0.3 splits are nonzero on both edges and both polarizations, with no fixed sign on the gapped edge.
  - For light matter the split tends to −κΞ.
  - This depends on the gauge, the Ward completion and the square-root prescription; it is not a class-wide physical prediction.

**R11-2 (producing the graviton) — CONFIRMED WITH CORRECTIONS. EXCLUDED in the X1 class; (a) SUGGESTED.**
- **The X1 class:** an exact, locally finite, pairwise-commuting finite-slot realization of the N-type constraints, whose averaged sector Hamiltonian has the regular lifted compact-character expansion and a nonsingular smooth canonical linearization.
- **X1 holds.** In that class, local Haar averaging is support-preserving, and the 09-14 derivative-order theorem forces every small-field frequency to be O(k³). So no light-like TT branch exists in that qubit class.
- **The dressing law (ω ∝ k^{3−n}) holds formally.** But the rotor-side A and B models lack a demonstrated normalizable exact sector.
- **(a) SUGGESTED.**
  - The brick-wall WW boost stays inside a momentum ball, so a box edge alone is no escape.
  - WW applies to a composite only when all its premises hold.
  - Lemma A_c does not manufacture those premises for a gauge graviton.
- **X2 is not supported as stated.** Exact commuting sourced constraints do force matter-density commutators to annihilate physical states, and they exclude a one-particle state for the free-hopping density. But they do not prohibit constraint-preserving dressed transport, nor prove empty/full-only matter in general.

**R11-3 (Λ on a fixed grid) — CONFIRMED WITH CORRECTIONS.**
- **The tadpole identity.** Conditional on the supplied free bands, stress vertices, conserved source and linear N-type coupling, the full-zone U tadpole obeys the exact edge-anomaly identity and has w ≥ 0. For the minimal-metric coupling M, positivity holds only for nonnegative kinetic bands.
- **V1: SOURCED,** with two independent linear tadpole conditions.
- **V2:** keeps the energy constraint and releases the homogeneous pressure.
- **V3:** absorbs energy and pressure into C(x) and f(t) at linear order.
- **V2 and V3 on fixed sites cannot realize metric FRW expansion.** Site creation is an open additional law.
- **Correction.** The reported edge tuning is only an infinitesimal small-mass result, not a property of the finite phase-transition step.

**R11-4 (box bodies in a curved field, d = 3) — CONFIRMED WITH CORRECTIONS. PASS WITH SCOPE.**
- **The stress.** Conditional on the refereed d = 3 two-body BT box law and the supplied minimal coupling to prescribed weak metric fields, the constructed symmetric, Hermitian, Gevrey-quasi-local stress has:
  - exact global energy conservation;
  - box-to-box momentum conservation, with disclosed off-box sources;
  - total H, dipole K, and J_T = J.
- **Uniqueness on the triplet bundle.** On the plateau bound-triplet bundle these data uniquely fix every projected pole–dipole moment to the Newton–Wigner stress at linear spin. This is a projection, not the full stress.
- **Consequences:**
  - von Laue holds exactly;
  - the effective γ is binding-independent;
  - for γ = 1, precession and the spin–curvature force carry the GR coefficient (2Γ+1)/(Γ+1) → 3/2;
  - frame dragging is unit (Schiff).
- **Excluded from the PASS:** global-flux numerics, self-consistent gravity, off-sector dynamics, nonlinear gravity, and any fixed quadrupole.

**R11-5 (preferred-frame CQ) — NOT CONFIRMED as VIABLE, so OPEN.**
- **Lemma C holds.** In the stationary pointwise-spectral class T_u, the conditions (H-T), a standard massless retarded pole, and continuous nonzero cone gain imply D′₀ + a²P_J/s² ≥ a|F|/|s|. So matter decoherence and stationary metric-record covariance cannot both be locally finite.
- **The meter chain checks out.** The driven four-stage QND chain is confirmed to be quantum-limited, finite-time CP under causal feedback, self-commuting and zero-reverse-gain, with ω⁻⁸ backaction.
- **What is missing:**
  - an explicit causal finite-start dilation for the full 𝒦_ε;
  - closure of the nonlinear, noise-fed PPN test;
  - the cosmological and absorption coefficients, which are still assumed.
- **A finite frame age is allowed as a named price.** But the submission is a promising conditional construction, not VIABLE.

### C5 Round 12, items 4–5 (pre-registered 19:32Z; launched now)

**R12-4. Set A: one no-go for classical metric records across the CQ classes?**
- Three refereed results all fail the same way, at the light cone:
  - R8-3, conditional covariant no-go (Lemma 3/Theorem 3 trilemma);
  - R10-3, EXCLUDED in T_E (record non-locally-finite at the cone);
  - R11-5, Lemma C in T_u (D′₀ + a²P_J/s² ≥ a|F|/|s|).
- Is there one theorem covering every stationary Gaussian CQ model (Lorentz-invariant or frame-tied, Markovian or not, any meter dilation with positive spectral measures) with Newton plus finite radiation? Its content would be that "matter decoherence finite" and "classical metric record finite near the cone" are incompatible.
- What exactly is left: finite-time (start-time) processes, non-Gaussian or jump models, mediator models, non-stationary frames?
- Name the minimal price for set A's "records are the metric".

Readings:
- **DERIVED:** a unified no-go in a stated class containing T_E, T_u and R8-3's subclass (refereed).
- **REFUTED:** an explicit stationary model in that class with both finite, checked.
- **SUGGESTED:** otherwise.

**R12-5. Graviton production outside X1: non-regular or strong-coupling phases of qubit N-type constraint models.**
- R11-2 (refereed): in the regular lifted finite-slot class X1, every small-field frequency is O(k³), so no light-like TT branch. The open escapes are:
  - non-regular or strong-coupling phases (Gu–Wen N-type);
  - emergent (energetically imposed) constraints;
  - normalizable rotor sectors.
- Test:
  - (a) Which X1 hypothesis does a strong-coupling phase violate (regular lifted expansion, smooth linearization)?
  - (b) Small-scale numerics on the smallest qubit N-type or rank-2 toric-code-like model with an energetic constraint term. Look for a linear TT mode, and compare its dispersion exponent with k³.
  - (c) Literature: Xu, Gu–Wen, Pretko, "emergent graviton" lattice models. Has any qubit model shown a linear gapless spin-2 mode numerically?

Readings:
- **PRODUCED:** a qubit model with a numerically demonstrated linear gapless TT mode (two polarizations, no partners), checked.
- **EXCLUDED:** a refereed no-go extending X1 to the stated strong-coupling or emergent class.
- **OPEN:** otherwise.
- **R12-1 (deformation algebra) — NOT CONFIRMED (Theorem K's global sufficiency). INCONCLUSIVE.**
  - **Necessity holds.** For free number-conserving box fermions on a smooth, compactly supported finite-particle core, exact Poincaré closure is necessary for degree-2 matter-bracket closure: every regular scalar-curvature/Killing-gate completion vanishes on Killing smearings.
  - **Local statements hold.**
    - Near zero smearing momentum in d ≥ 2, the SS defect admits a local Hadamard decomposition.
    - Within the fixed completion ansatz, an off-box O(q) Killing defect needs a 1/|q| singularity, i.e. a 1/r^{d−1} tail.
  - **Not established:** an explicit global quasi-local lattice HDA, an undeformed common structure function, W4 closure, or a mobile physical sector.
- **R12-3 (twisted lattice SUSY) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE, not bounded FAIL.**
  - **BF is a genuine doubler-free multiplet.** On Z³ × ℝ the BF construction is a gauge-quotient multiplet with C² = ΔP_phys, c₁ = 0, nilpotent Q and the stated Ward identity.
  - **But it is incomplete.** Its charged quotient Hamiltonian is Coulomb-nonlocal. No local equivariant completion, and no complete one-loop electron–photon split, was constructed.
  - **PD₁ fails at its written scope.** An A₂ ⊕ T₂ odd-signature block carries c₁ = +2.
  - **The odd-signature c₁ = ±2 obstruction** applies only with conserved fermion number, not merely with a ghost U(1)_R.
  - **Theorem U** excludes untwistable spin-½ photinos only in the narrow SO(3)-linear Nicolai class.
  - **Exact scalar Q alone does not enforce c_γ = c_e.** Groot Nibbelink–Pospelov rely on the full standard supercharge–translation setting.

### C5 Round 12, item 6 (pre-registered 19:37Z; launched now; conditional on R12-3, whose referee is running)

**R12-6. The twisted N=4 Kähler–Dirac gauge multiplet on Z³ × ℝ with charged box matter: the one lattice-SUSY route R12-3's worker leaves open.**
- R12-3's worker (unrefereed) finds:
  - the BF gauge multiplet is doubler-free but has integer-spin photinos;
  - Theorem U blocks spin-½ in Nicolai form;
  - completing with a complex scalar σ and a site fermion η gives a Kähler–Dirac photino that is doubler-free (K² = Δ) and untwistable, i.e. Catterall-like N=4 content.
- Build its Hamiltonian on Z³ × ℝ with box symbols. Couple it to charged Clifford-flat box matter (Lemma J content) with an exact supercharge and Ward identity. Then:
  - (a) Is H = {Q, Q†} local and bounded below?
  - (b) Is the photino spin-½ after untwisting, with no doublers?
  - (c) Compute the one-loop c_e − c_γ, including the dressing terms R12-3 omitted.
  - (d) Do the 6 massless neutral scalars conflict with fifth-force bounds, and does giving them mass break the protection?
  - (e) Theorem L says no lattice supercharge fixes c_γ/c_e. Does N=4's extended algebra change that?

Readings:
- **PASS:** an explicit local Hamiltonian law with an exact supercharge, Ward identity, doubler-free spin-½ photino, and a one-loop c_e − c_γ that vanishes or is protected, checked.
- **FAIL:** a refereed no-go in the N=4 Kähler–Dirac class (locality, spin, or the split).
- **INCONCLUSIVE:** otherwise.
- **R12-2 (site creation and Λ) — CONFIRMED WITH CORRECTIONS. OPEN.**
  - **Setting:** V3, fixed proper site density, flat FRW cosmic slicing, timelike site worldlines, statistical homogeneity.
  - **Creation is forced.** Number balance gives mean creation c̄ = 3H, and the V3 equations leave homogeneous expansion to the creation law.
  - **The conditional homogeneous construction.** For exact, separately conserved finite constant-w mixtures away from interactions, a derivative (Prony) rule can reconstruct all w ≠ −1 density while annihilating every constant contribution. That gives untuned late Λ_eff = 0, and makes a true Λ non-gravitating.
  - **What limits it:**
    - transitions contaminate the higher moments;
    - the F runner hard-codes its memory evolution;
    - the local 3D encoder, bound structures, inhomogeneous completion, source bridge and dark-energy sector are all absent.
  - **No candidate is VIABLE and no general inconsistency is proved.**
- **R12-4 (unified CQ no-go) — CONFIRMED WITH CORRECTIONS. DERIVED.**
  - **The class.** Every translation-stationary, spatially homogeneous, linearized record-metric CQ theory at second order whose:
    - record obeys the stated non-demolition Kubo or additive product bound;
    - metric response keeps an undamped massless 1/s pole;
    - gain is bounded away from zero on a one-sided regular cone patch.
  - **The no-go.** State-independent spectral positivity gives σ̄M ≥ κg²f₀²/s². So matter noise and classical metric-record covariance cannot both be locally finite, in any nonsingular frame.
  - **The class contains** T_E, T_u and R8-3's retained subclass.
  - **Narrowed claims.** Specified regulators keep a regulator-dependent log-squared trade. E2 (GW friction) is an uncompleted spectral construction. No universal "preferred frame plus one regulator" minimal price is proved.

### C5 Round 12, item 7 (pre-registered 19:48Z; launched now; conditional on R12-4, whose referee is running)

**R12-7. Set A, route E2: classical metric records with frame friction on gravitational waves, G = g/(s + iγω).**
- R12-4's worker (unrefereed) finds that, outside the unified no-go class 𝒰, a stationary CQ model with damped classical TT waves has both matter decoherence and the metric record locally finite. At γ ≈ H₀ the GW amplitude loss is 0.45% at 40 Mpc, inside LIGO's 6.75e-4 Mpc⁻¹ bound.
- Construct E2 explicitly:
  - (a) a stationary non-demolition meter dilation with frame friction, and where the damped wave energy goes (an energy sink);
  - (b) causality and positivity;
  - (c) GW170817's speed (c_T), the binary-pulsar orbital decay (Hulse–Taylor: radiated power at the source), and LIGO amplitude–distance consistency against standard sirens;
  - (d) whether friction changes the Newtonian static limit or R6-4's lab window;
  - (e) the PPN preferred-frame α₁ and α₂;
  - (f) the price list against the axiom texts.

Readings:
- **VIABLE:** an explicit stationary E2 model passing every stated test on a stated (γ, ℓ_s) region, with prices named.
- **EXCLUDED:** a refereed inconsistency, or a violated stated bound for every γ.
- **OPEN:** otherwise.
- **R12-5 (strong-coupling graviton) — CONFIRMED WITH CORRECTIONS. OPEN.**
  - **What holds:**
    - DW-q exactly removes non-invariant Weyl characters at first order in a sharp constraint sector;
    - the specified finite-penalty Gaussian is unstable;
    - the two supplied one-exact reductions keep k² TT modes.
  - **This is a genuine weakness in Gu–Wen's uncontrolled freeze/spin-wave argument.** It does not control higher-order returning words, all one-exact Hamiltonians, or non-Gaussian strong-coupling phases.
  - **ADHH** gives at most conditional prethermal support.
  - **Neither fixed reading is met:** no model satisfies PRODUCED, and no valid argument establishes EXCLUDED.
- **R12-7 (GW friction CQ route) — CONFIRMED WITH CORRECTIONS. OPEN.**
  - **What holds:**
    - For each fixed preferred-frame scalar mode, the positive finite bank has bounded H-T excess and realizes the regulated near-cone slopes.
    - The retarded telegraph propagator is causal, boost-stable and exactly Newtonian at zero frequency.
    - A classical outgoing Lamb string realizes noiseless Ohmic friction for a toy mode.
    - Spatial-TT-only friction is generically acausal at O(γ).
  - **No current comparator excludes γ ≲ H₀:** speed, binary pulsars, static/lab and coarse sirens all pass. Lu et al.'s 2.98 H₀ is only a fixed-distance benchmark, and PPN is unclosed.
  - **The budget problem returns, conditionally.** Given R11-5's spectral normalization, gravitating near-cone content and a dust-like gravitating sink, the dark-energy budget again needs extreme suppression.
  - **Missing:** a full spin-2 CQ dilation, a conserved gravitating bath, and a nonlinear preferred-frame completion.

### C5 Round 13 (pre-registered 20:13Z from the S14 synthesis, agents/C5_S14_synthesis.md; readings fixed as drafted below)

Launch: R13-1, R13-3, R13-5 and R13-6 now; R13-2 after the R12-5 referee; R13-4 after R12-6. Draft text verbatim from S14 §5:


**Rules (as rounds 2–12).** Probes: Opus 5.5 at xhigh. Every FAIL, EXCLUDED or no-go goes to codex gpt-5.6-sol (xhigh) before it is recorded. Prices are named, never adopted. Each probe greps the repository and packet for prior art first and counts each match once. Hypotheses before titles; excluded outside realizations listed. Numbers from memory labelled RECALLED. Every tail or decay clause names its subtraction before any run (R9-3 rule). **New rule (from R11-2's registration):** a PRODUCED or PASS clause names the perturbative order at which each exactness condition is required.

**Overlap check.**
- R12-6 builds the twisted N=4 Kähler–Dirac multiplet with a nilpotent scalar Q and computes c_e − c_γ there. R13-1 uses *untwisted spinor* supercharges whose square contains momentum; it excludes twisted and nilpotent-scalar classes. R13-4(i) asks about BF *without* σ, η; launch part (i) after R12-6(a) reports, and drop it if R12-6 supplies a local completion.
- R12-7 builds set A's GW-friction route (E2). R13-6 builds the start-time route (E1), so the owner has both sides of question 1. No overlap.
- R12-5 is the strong-coupling graviton argument. R13-2 is a numerical Euclidean test of the same window; launch after R12-5's referee.
- R13-3 and R13-5 overlap nothing running.

**Priority.** R13-1, R13-2 (after R12-5's referee), R13-3, R13-4, R13-5, R13-6 (pair with R12-7's result).

---

**R13-1. The electron–photon split: momentum in the superalgebra on the box.**

- **Plain question.** The theorem that supersymmetry forbids dimension-4 Lorentz violation (Groot Nibbelink–Pospelov) needs supercharges whose square is the momentum. On a lattice no local difference operator obeys the product rule (Kato–Sakamoto–So), so lattice superalgebras leave momentum out, and then nothing ties the electron's speed to the photon's (`vR12-3:9`). But the box symbol is exactly linear inside the box, so the product rule holds whenever all momenta, and their sums, stay in the box. Can a supercharge with {Q, Q̄} = 2σ·P exist on box states, and does it force c_e = c_γ at one loop, even though loops reach the edge?
- **Setting.**
  - Z³ × ℝ, Hamiltonian. A free chiral multiplet and an abelian vector multiplet with untwisted spinor supercharges Q_α. Box symbols p_i(k) = k_i on the open box B, smooth and periodic outside; Ward-forced gauge coupling on the whole zone (Lemma C).
  - Two domains: (D1) the box-additive domain (all external and internal momenta and their sums in B); (D2) the full zone with a periodic p(k).
  - Excluded: twisted or nilpotent-scalar-Q constructions (R12-3, R12-6); class 𝒮 (R10-5); interactions beyond one loop.
- **Prior art (count once).** C4 F2's "SUSY fails (suggested)" and its referee correction that Kato–Sakamoto–So has infinite-flavour/non-local escapes (`agents/C4_F2_referee.md:46`); C4 P1 referee on KSS and FS models; R10-5 Lemma J (`vR10-5:9`); R12-3 Theorem L and its scope (`vR12-3:9`); R11-1 Theorem N\*; R8-2/R9-2 box-to-box momentum conservation; KSS 0803.3121, 0810.2360; GNP hep-ph/0404271; Dondi–Nicolai 1977; Bergner et al. on SLAC-derivative SUSY (RECALLED).
- **Probes.**
  - (a) **Free level.** Construct Q_α with {Q_α, Q̄_β} = 2σ^μ_{αβ}P_μ on D2. Prove or refute: the algebra forces one common p(k) for every multiplet coupled to the same P (one cone at tree level by algebra, not by tuning).
  - (b) **Interacting.** Add the gauge and Yukawa vertices. State on which domain the superalgebra closes. Give the defect operator off D1 explicitly.
  - (c) **One loop.** Compute c_e − c_γ in minimal box SQED (electron, selectron, photon, photino) with matched masses, on the literal and gapped edges. Is it zero, or an edge moment of the product-rule defect? Give the number in e²/16π² units and the residual under a mass split O(Δm²a²).
  - (d) **Doublers.** Does the vector multiplet have a doubler (R10-5's Chern ±2 argument is for 𝒮)?
  - (e) Per-site content and prices.
- **FIXED readings.**
  - **PASS:** an explicit law with spinor Q, {Q, Q̄} = 2σ·P exact on a stated domain, a Ward identity, a doubler-free photon, and one-loop c_e − c_γ = 0 for every edge shape at matched masses (residual O(Δm²a²) stated), checked.
  - **FAIL:** a refereed no-go: in a stated class containing box-symbol spinor SUSY, either a photon doubler is forced, or the one-loop c_e − c_γ equals a nonzero edge moment of the product-rule defect that no untuned choice removes.
  - **INCONCLUSIVE:** otherwise.
- **Expectation.** (a) a common p(k) is forced at the free level. (b)–(c) the product-rule defect lives exactly where the edge anomaly lives, so supersymmetry fails in the loop and the split becomes a defect moment: INCONCLUSIVE leaning FAIL. The upside, if the defect moment cancels by N\*'s structure, would be the campaign's first untuned removal of the electron–photon split.

---

**R13-2. Producing the graviton: the compact non-Gaussian window, by Euclidean Monte Carlo.**
*(Launch after R12-5's referee. Use whatever of Lemma DW-q, X1-E and the Gaussian-instability statement is confirmed; otherwise state them as hypotheses.)*

- **Plain question.** Exact qubit constraints give gravitons with ω = O(k³) (X1). The R12-5 worker says one exact constraint caps them at k², the soft Gaussian version is unstable, and the only window left is a compact, strongly coupled phase where both constraints are energetic. Exact diagonalization cannot reach it. But a Euclidean path integral of a compact (Villain-type) model is a classical 4D statistical model. If its weights are positive, Monte Carlo can measure the tensor correlator directly and read off how frequency scales with momentum. Is there a phase with light-like (z = 1) gravitons, two polarizations and nothing else gapless?
- **Setting.**
  - A rank-2 symmetric-tensor U(1) or Z_N gauge field with integer conjugates on Z³, both N-type constraints imposed energetically; Euclidean Z³ × Z_τ by Trotter/Villain; L from 6 up to the largest feasible (target ≥ 12), at least three sizes.
  - Excluded: matter, nonlinear gravity, Λ.
- **Prior art (count once).** R11-2 and verdict (X1, Lemma A_c, dressing law; `vR11-2:7-9`); R12-5 (pending; `TESTS:4543-4551`); N0914 (Gaussian instability); lane R (`TESTS:685-776`); Gu–Wen 0907.1203 (they call the linear N-type result unreliable; `vR11-2:9`); Xu 2006; Pretko 2017; published Monte Carlo of rank-2 U(1) Coulomb phases (RECALLED; verify before use).
- **Probes.**
  - (a) Write the Euclidean Villain form. Prove positivity of the weights, or locate the sign problem (expected in the trace/conformal sector).
  - (b) If positive: sample a coupling grid that includes U ~ J ~ g. Measure the TT, vector and scalar correlators G(ω_n, k); extract z from a pre-registered collapse fit; count gapless polarizations; detect confinement.
  - (c) If not positive: give the cheapest sign-free deformation and state which constraint or which polarization content it changes.
  - (d) Prices.
- **FIXED readings.**
  - **PRODUCED:** a phase with z = 1 ± 0.1 by the pre-registered collapse fit on ≥ 3 sizes, exactly two gapless TT polarizations, no gapless vector or scalar partners, checked.
  - **EXCLUDED:** a refereed no-go in a stated class (for example, positivity forces confinement, or z ≥ 2, or gapless partners).
  - **OPEN:** otherwise, including an unresolved sign problem.
- **Expectation.** OPEN. Most likely a sign problem in the trace sector; if sign-free, a confined phase at strong coupling and a weak-coupling phase with k² or k³ modes or gapless partners. A clean z = 1 two-polarization phase is not expected; a definite numerical answer either way would still close or open the last unpriced window.

---

**R13-3. Λ: the P-T creation law in a lumpy universe (inhomogeneous completion, bound regions, phase transitions).**

- **Plain question.** R12-2 found a homogeneous rule that creates sites at mean rate 3H and reads only *changes* in the local stress, so constant vacuum energy cannot drive expansion. It has never been written for a universe with galaxies, sound waves and phase transitions. Do bound systems stay unexpanded without a clamp? Does a phase transition leak a visible energy density? And in V3 the static field is an integration datum C(x), which behaves like extra dust (Mukohyama's "dark matter as integration constant"): is that a defect or a feature?
- **Setting.**
  - V3 (fixed √h per site, fixed lapse) with site creation obeying a local 3D F-law (P53): creation density c(x, t) a functional of time derivatives of local stress along site worldlines, plus finitely many per-site memory variables, with a stated local encoder.
  - Linear perturbations about FRW; a top-hat collapse to a virialized region; a first-order phase transition **with a specified transition sector** (the ingredient missing in R11-3, `vR11-3:55`).
  - Excluded: records as a q-charge (R10-4); the pairing route.
- **Prior art (count once).** R12-2 and verdict (`vR12-2:5-17`); R11-3 and verdict (`vR11-3:51,57`); R10-4 Q1–Q5; R5-3 Lemma PT (`TESTS:2985-2993`); O3 P13; Mukohyama 2009 (cited `C5_R11-3_report.md:97,185`; RECALLED); RN L3 (projectable Hořava strong coupling); Perlman et al. 1411.7262 on foam (`vR12-2:11`); DESI DR2 w₀w_a (comparator).
- **Probes.**
  - (a) Write the local 3D rule and encoder. Show c̄ = 3H is recovered on average.
  - (b) **Linear perturbations.** Growth D(a) and the ISW source. Does C(x) behave as pressureless dust with zero sound speed? What sets its amplitude?
  - (c) **Bound regions.** In a virialized top-hat, is the creation rate zero inside without a clamp? What memory time does that need relative to orbital periods?
  - (d) **Phase transition.** Compute the leakage into higher Prony moments with the specified transition sector. Compare with ΔN_eff and early-dark-energy bounds (state the bounds used).
  - (e) **Acceleration.** A true Λ is invisible. State which sector produces today's acceleration, and whether the F-law makes it visible only through w ≠ −1.
  - (f) Prices.
- **FIXED readings.**
  - **VIABLE:** an explicit local 3D rule with (b)–(e) passing their stated comparators, bound regions non-expanding without a clamp, prices named, checked.
  - **EXCLUDED:** a refereed inconsistency in a stated class (for example, every local rule of memory order N creates sites inside virialized regions, or leaks more than the stated bound for every N).
  - **OPEN:** otherwise.
- **Expectation.** OPEN. Most likely: (c) forces a memory time at least the longest bound-orbit period, which makes the rule non-local in time; (d) leaks at roughly the latent-heat fraction (R12-2's 1–2%), dangerous only for late transitions; (b) C(x) acts as dust with unexplained initial data.

---

**R13-4. Tails: are the Coulomb-type tails of the BF photon multiplet and of the off-box gravity completion physical, or constraint-solving as in Coulomb-gauge QED?**
*(Part (i) launches after R12-6(a) reports; drop it if R12-6 supplies a local completion.)*

- **Plain question.** Two routes stopped at the same kind of term. The doubler-free BF photon multiplet has an inverse-Laplacian (Coulomb-type) piece in its charged Hamiltonian (`vR12-3:5`). The off-box gravity completion needs a 1/r^{d−1} tail (`vR12-1:15`). Ordinary QED in Coulomb gauge also has an instantaneous 1/r term, yet it is a local theory: the term only solves Gauss's law, and gauge-invariant observables respect the light cone. Are these two tails of that harmless kind, or do they act on physical observables at a distance? And, as a control, how big is the box law's own super-polynomial leakage outside the light cone?
- **Setting.**
  - (i) R12-3's BF quotient Hamiltonian with charged box matter.
  - (ii) R12-1's completion ansatz for the off-box Killing defect.
  - (iii) Control: R7-1's free box law and R9-5's qubit realization.
  - "Constraint-solving" means: there is a local Hamiltonian on an extended space with local constraints whose reduced dynamics equals the given one, so the tail appears only in gauge-dependent quantities.
  - Excluded: N=4 KD content (R12-6); interacting gravity beyond degree 2.
- **Prior art (count once).** R12-3 and verdict; R12-1 and verdict (`vR12-1:5,15`); R11-2 on Marolf's kinematic non-locality (`vR11-2:5`); C5_R12-1 P12-2 (`C5_R12-1_report.md:272`); R7-1 and R9-5 tail constants (`vR9-5:9,12`); R11-6's large-r fits (`TESTS:4330`); Coulomb-gauge QED and Lieb–Robinson bounds for quasi-local Hamiltonians (RECALLED).
- **Probes.**
  - (a) For (i) and (ii): construct a local extended formulation, or prove none exists in a stated class. Compute the equal-time commutator of gauge-invariant local observables at separation r and its decay.
  - (b) For (iii): the maximal group velocity over the whole zone, and the commutator leakage outside the cone versus distance from it, with constants, at a = ℓ_P (a reading on `AX:189-190`).
  - (c) Prices, against `AX:57` and `AX:116-130`.
- **FIXED readings (per object (i), (ii)).**
  - **LOCAL-EQUIVALENT:** an explicit local extended formulation, with gauge-invariant commutators decaying at least super-polynomially outside the cone, checked.
  - **PHYSICALLY NON-LOCAL:** a refereed proof that a gauge-invariant commutator decays no faster than a power, in a stated class.
  - **OPEN:** otherwise.
  - (iii) is reported as numbers with constants (no verdict).
- **Expectation.** (i) LOCAL-EQUIVALENT for the bosonic part, as in Coulomb-gauge QED; the photino/ghost sector may need the equivariant completion. (ii) OPEN. (iii) group velocity ≤ 1 achievable on the whole zone; leakage negligible at a = ℓ_P.

---

**R13-5. The graviton–matter split, gauge-invariantly: Ward-complete the pair-creating stress, then compute the pole positions.**

- **Plain question.** R11-1(b) found the matter and graviton cones split, but only in one prescription; the pair-creating stress was never Ward-completed (`vR9-9:5`; `vR11-3:31`; `vR11-1:19`). GW170817 says gravitons and light arrive together to about 1e-15. A prescription-independent number needs the missing piece: a Ward-complete pair stress. With it, compute the shift of the physical poles (which is gauge-invariant), with and without the TT pairing w = S².
- **Setting.** R9-9's N-type box graviton; R8-2's stress plus a pair-creating completion satisfying the second-order Ward identity; complex scalars and Clifford-flat fermions on the literal and gapped edges; m = 1 and 0.3; the paired unit of Theorem S as a variant.
- **Prior art (count once).** R9-9 and verdict (`vR9-9:5,23`); R10-5 Theorem PT (`vR10-5:5`); R11-1 (`vR11-1:9,17-19`); R11-3's U/M vertices (`vR11-3:31`); RFW (field-dependent Ward completion); GW170817 (comparator).
- **Probes.** (a) Construct the Ward-complete pair stress (or prove none exists in a stated class). (b) Compute the one-loop pole shifts of the TT graviton (both polarizations) and of scalar matter; give c_m − c_T in κ_lat units and its size at a = ℓ_P. (c) Repeat with the paired unit. (d) State which seagull terms the Ward identity fixes.
- **FIXED readings.**
  - **SPLIT-PRESENT:** a nonzero pole-position split for every Ward-complete stress in a stated class (refereed if claimed class-wide), with numbers.
  - **SPLIT-ABSENT:** the pole split vanishes identically for the Ward-complete stress (with or without pairing, stated), with the reason, checked.
  - **OPEN:** otherwise.
- **Expectation.** SPLIT-PRESENT without pairing (birefringence alone forces one polarization off the matter cone, `vR11-1:19`); with pairing, SPLIT-ABSENT for TT at matched unit-speed curves, with the scalar matter self-energy unpaired.

---

**R13-6. Set A, route E1: an explicit start-time CQ dilation (R11-5's missing piece).**

- **Plain question.** R12-4 proved that a stationary record-metric model cannot keep both matter noise and the metric record finite at the light cone. One escape is a law with a start time. R11-5 built the meter chain but not the full causal finite-start construction (`vR11-5:9,22`). Build it, so that the owner can compare "a start time" (this item) with "leaky gravitational waves" (R12-7) on equal terms.
- **Setting.** Linearized Gaussian CQ gravity with mean GR coupling, R11-5's regulated kernel family 𝒦_ε, a finite start t₀, a preferred frame (CMB), integer n ≥ 3. Excluded: GW friction (R12-7); non-Gaussian and jump models.
- **Prior art (count once).** R6-4; R8-3; R9-4; R10-3; R11-5 and verdict (`vR11-5:6-22`); R12-4 and verdict (`vR12-4:5-19`); `C5_R12-4_report.md:162` (E1 row).
- **Probes.** (a) Construct a positive synthesis measure, a causal spectral factor, the finite-start state and covariance, and the exact map from the meter bank to the displayed spectra; prove complete positivity. (b) Record growth (ε ln t, or linear with a finite regulator) and its size at t_H. (c) Re-run R11-5's tests, adding the nonlinear noise-fed PPN term. (d) The allowed ℓ_s interval, or none. (e) Prices.
- **FIXED readings.**
  - **VIABLE:** an explicit finite-start model passing every stated test on a stated ℓ_s interval, with prices named, checked.
  - **EXCLUDED:** a refereed inconsistency or bound violation for every ℓ_s in the class.
  - **OPEN:** otherwise.
- **Expectation.** OPEN, leaning VIABLE on a narrow interval near 4e-7 to 5e-6 m; the noise-fed PPN term is the likeliest failure point.

---

- **R12-6 (twisted N=4 box QED) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE.** It gives a sharp 𝒦₀ obstruction, not the class-wide no-go FAIL requires.
  - **What holds.** On Z³ × ℝ, the equivariant (σ, η) completion gives:
    - Q² = iσL and H ≥ 0;
    - finite-range locality for cochain symbols, and quasi-locality for box symbols;
    - a free doubler-free Kähler–Dirac photino with K² = Δ.
  - **The obstruction.** In the minimal-Hessian class 𝒦₀, the photon and matched-electron logarithms have coefficients −8 and −2 (units e²/16π²). So c_e − c_γ contains +6 ln(1/m): neither protected nor identically zero.
  - **The B repair** removes the photon logarithm but leaves an electron logarithm, shown only numerically.
  - **Still open:** τ-coupled, non-Hessian and full extended-N=4 completions.

### C5 Round 13 worker readings (recorded as they arrive)

- **R13-5 (graviton–matter split) — CONFIRMED WITH CORRECTIONS. OPEN both without and with pairing.** The fixed test needs a second-order Ward-complete stress and gauge-invariant physical poles.
  - **What W1 does.** For a fixed massive free scalar and a smooth spatial pair kernel, W1 uniquely supplies smooth time components, and the conjugate annihilation channel restores Hermiticity.
  - **What blocks W2.** Under the standard undeformed Dirac–Schwinger/HDA meaning of W2, the pair terms vanish from H, P and K. The periodic-band boost anomaly is left as a bounded obstruction to second-order closure.
  - **The W1-only class 𝒲_V:**
    - the G edge has a strictly negative TT floor, hence a large, prescription-scoped light-scalar dD-M split;
    - light L doublers destroy that floor;
    - birefringence is removable by a one-mass edge tuning.
  - **With pairing.** Matched pairing cancels the stipulated TT response and leaves 2κm²J₂.
- **R13-1 (momentum in the superalgebra) — CONFIRMED WITH CORRECTIONS. INCONCLUSIVE.** It has a sharp bounded Theorem B and a confirmed model-specific obstruction.
  - **The free level.** Abstract modewise N=1 representations exist on the free zone when the multiplet multiplicities and E ≥ |p| hold. But the algebra neither identifies p with lattice momentum nor bounds a massive particle's IR speed by 1 − m²/b² (corrected). A field-level vector-multiplet charge is unconstructed.
  - **Theorem B is rigorous** in the interacting class with C¹ periodic one-body band-scalar momentum and a whole-zone Peierls vertex. There, Jacobi plus the nonvanishing transverse vertex forbids an exact D2 supercharge algebra.
  - **The one-loop split.** For the chosen off-D1 completion of minimal box SQED, it is negative in all 24 sampled laws.
  - **The literal-edge photon coefficient** is a sign-indefinite moment of the product-rule defect.
  - **Untuned class-wide non-removability is not proved.**
- **R13-3 (P-T in a lumpy universe) — NOT CONFIRMED as EXCLUDED. OPEN.** Only the smooth synchronous-continuum subclass is conditionally excluded.
  - **The conditional exclusion.** Take a literal smooth continuum V3 completion with ADM lapse N = 1, conserved stress, adiabatic synchronous initial data, and no negative C-density or non-smooth/discrete reset. Then the slice normals are hypersurface-orthogonal geodesics, and Raychaudhuri focuses them in a collapsing top-hat (conditionally on a halo timescale). A scalar creation rule does not remove this.
  - **Not excluded:** kinked, lattice-scale or alternative nonlinear completions.
  - **V2** restores the homogeneous Hamiltonian constraint. So the decaying-memory F-law is incompatible with a nonzero constant vacuum unless a tuned compensator is added.
  - **At linear k ≠ 0** the system matches GR plus an effective dust component.
  - **Confirmed:** T_orb = t_coll in EdS, and the stationary-age encoder mean is exact.
  - **Not confirmed:** the filter floors are model-specific, and the transition runner misclassifies complex Prony roots.
- **R13-6 (start-time CQ dilation) — CONFIRMED WITH CORRECTIONS. EXCLUDED for the literal class; OPEN once the gain is repaired.**
  - **Lemma D, confirmed.** Within the linearized, preferred-CMB-frame E1 model with R11-5's literal causal gain e^{−k²ℓ²/2}(1 − iωℓ/c)^{−n}, n ≥ 3, a compact body necessarily acquires a self-drag −(4πG/3)(nℓ/c)(∫ρ²)v. Double-pulsar timing then needs ℓ ≲ 4e-21 m, excluding every ℓ_s in the class by at least 11 orders of magnitude.
  - **Not covered:** R6-4's instantaneous kernel, and arbitrary Lorentz-covariant or reciprocal CQ completions.
  - **The repair.** A signed zero-first-moment gain removes the leading drag and passes the strict τ = ℓ/c test. But it is a changed, still-OPEN model, whose exact finite-start regularity/CP and spin-2 completion are unresolved.
  - **Dated correction (2026-10-12) to R11-5:** R11-5's literal kernel 𝒦_ε is excluded by Lemma D (double-pulsar drag). The R11-5 "OPEN" reading applies only to its repaired, zero-first-moment-gain version.

### C5 Round 13, items 7–8 (pre-registered 20:49Z; launched now)

**R13-7. Is the electron–photon split a theorem? A mass-interval no-go for c_e − c_γ in Ward-forced lattice QED with periodic bands.**
- Four refereed or worker routes leave c_e − c_γ nonzero: R8-5, R10-1/R10-5, R12-6 (log), R13-1.
- R11-1 (refereed, DERIVED) proved that interval vanishing of A-moment coefficients forces boson–fermion cancellation, but for the photon and graviton-TT coefficients only. The electron's own shift involves the Dirac a-, c₁- and c₂-moments (R10-1 Theorem D), which have no bosonic counterpart.
- Question: in a stated class, can c_e(m) − c_γ(m) vanish on an open mass interval? The class: Ward-forced Peierls (or any ℓ¹ bilinear gauge generator, Lemma C), periodic C² bands, box or not, any finite set of species, paired or not, one loop.
- Use a Laplace/Lerch argument on the m-dependence, as in N*, plus the sign structure of the electron self-energy moments.

Readings:
- **DERIVED:** a refereed proof that c_e − c_γ cannot vanish on a mass interval in the stated class. The split then needs a per-mass (counterterm) tuning.
- **REFUTED:** an explicit untuned law in the class with c_e − c_γ ≡ 0 on an interval, checked.
- **SUGGESTED:** otherwise.

**R13-8. Set C's actual one-loop tuning count (Z³ × ℝ, nearest-neighbour or box, QED plus graviton).**
- The claim "≥ 6 tunings" for set C is a reading. R10-1's "six" is not established (`vR10-1:15`).
- Count the independent one-loop Lorentz-violating coefficients that must be tuned, for:
  - one charged Dirac species plus the photon plus the N-type graviton on Z³ × ℝ with cubic symmetry (the axioms' proper rotations only);
  - then per extra species.
- List each coefficient: speeds, birefringence, TT masses, tadpoles, CPT-odd b₀ and k_AF (R6-5).
- Give the scaling with the number of species N_s, against observational precision.

Readings:
- **COUNTED:** an explicit count, with each coefficient shown to be generated (nonzero) at one loop and independent, checked.
- **OPEN:** otherwise.
- **R13-2 (graviton Monte Carlo) — CONFIRMED WITH CORRECTIONS. EXCLUDED (bounded, X-G).**
  - **The exclusion.** Take a real, local, C⁴, cubic-covariant PSD Gaussian Hamiltonian of exactly the six symmetric-tensor canonical pairs.
    - Two gapless axial TT modes force two vector partners and one scalar zero-frequency partner at k = 0.
    - If the vector partners are instead flat through a one-sided transverse gauge kernel valid for all nearby directions, positivity forces ω_TT = O(k²).
  - **Still open:**
    - mixed h–E kernels;
    - auxiliary irreps;
    - axis-only flatness;
    - non-local symbols;
    - non-product sign cures;
    - the strongly coupled indefinite non-Gaussian window.
  - **The Monte Carlo** gives finite-volume evidence of ordering in one sign-free deformation. It neither excludes a linear branch nor establishes a thermodynamic gapped crystal.
  - **Corrections:** Z₄ normalization, auxiliary-field scope, LP certification, harmonic frequencies.
- **R13-4 (tails) — CONFIRMED WITH CORRECTIONS.**
  - **(i) PHYSICALLY NON-LOCAL in class 𝓔.**
    - For the charged BF quotient law with the inherited flat/group-averaged measure, horizontal reduction necessarily produces a four-fermion neutral-pair transfer with a Coulomb 1/r kernel, detected by a bounded local gauge-invariant observable. So no finite-range or super-polynomially quasi-local extension in 𝓔 can keep the same physical content and locality.
    - The zero-fermion sector is constraint-solving.
    - R12-6 localizes the interaction only by adding physical modes.
  - **(ii) R12-1's gravity tail: OPEN.**
  - **(iii) Box speed.** The box profiles actually used are superluminal at lattice scale, with power-law leakage. A derivative-controlled b < π/2 Gevrey box is subluminal and preserves the earlier scoped box constructions on a narrower plateau, but needs fresh edge numerics.

### C5 Round 14, item 1 (pre-registered 20:54Z; launched now; conditional on R13-4, whose referee is running)

**R14-1. Do the box-route PASS results survive with a subluminal box (b < b*(m) ≤ π/2)?**
- R13-4's worker (unrefereed) proves Lemma V: every one-band box law with b > b*(m) has v_max > 1 on the zone. The laws behind the box-route PASS results are all superluminal at lattice scale:
  - R7-1 and R9-5 (b = 2, 2.6);
  - R8-1 and R9-6 (b = 2.6);
  - R8-5 Dirac.
- The worker exhibits a subluminal b = 1.4 law.
- Re-run the load-bearing checks with a subluminal box (b ≤ 1.4, Gevrey step):
  - R7-1 P1 (free algebra);
  - R8-1 (two-body d = 1/2 algebra, leakage);
  - R9-2 (bound-body fall, d = 1);
  - R9-6 (d = 3 triplet, mass flatness);
  - R11-4 (pole–dipole moments).
- Then check:
  - Does each conclusion carry over unchanged?
  - Which numbers move (rapidity budget, interaction plateau sizes, leakage)?
  - Does the subluminal step create new problems: doublers, a smaller box for interactions, or Theorem E's edge share?
  - Is a subluminal Wilson-box Dirac possible?

Readings:
- **PASS:** every listed result holds with a subluminal box, with the changed numbers stated, checked.
- **FAIL:** a listed result fails for every subluminal box (refereed).
- **INCONCLUSIVE:** otherwise.
- **R13-8 (set C tuning count) — CONFIRMED WITH CORRECTIONS. OPEN, not COUNTED.**
  - **TT ranks.** In the local quadratic, first-order-on-shell-TT EFT through two derivatives, set C has TT ranks (2, 2, 5) under proper cubic rotations, and (2, 0, 4) with P and T.
  - **The gauge kernel.** Exact linearized diffeomorphism invariance leaves a two-dimensional degree-2 kernel whose TT image is the single graviton-speed direction. The other TT structures are Ward-defect candidates.
  - **The P,T-even count.** A valid candidate bookkeeping count is N_s + 7: eight LV conditions plus the CC for one Dirac species. It is not an established one-loop tuning count, because the witnesses are not Ward-complete and no single law generates every coefficient.
  - **The generic count** 3N_s + 8 assumes removal of two degree-1 graviton terms. Without that assumption it is 3N_s + 10.
- **R14-1 (subluminal box recheck) — CONFIRMED WITH CORRECTIONS. PASS.**
  - **The subluminal completion.** A smooth, Gevrey, whole-zone subluminal b = 1.4 odd-symbol completion preserves every listed box/plateau result within its inherited scope, once the d = 2, 3 transition support shrinks to Π₂ < 0.992. Global edge stresses and shell quantities must be recomputed.
  - **Its doublers.** It has seven exact d = 3 corner valleys with componentwise sign-flipped boosts.
  - **Lemma V re-scoped.** A separate even gapped completion is subluminal for every b < π with no light corners. This disproves only TESTS' overbroad paraphrase of Lemma V.
  - **The sign of Ξ and the shear.** For the specific S/G families, A ≤ 0 and the R9-9 vertex gives Ξ < 0. But neither this sign nor a nonzero conditional shear is universal across subluminal bands. The shear-cancelling profile is superluminal (d = 3 v_max = 1.734).
  - **The Wilson construction** is rigorously subluminal for r ≤ 1/√d, with light doublers.

### C5 Round 14, items 2–3 (pre-registered 21:15Z; launched now)

**R14-2. Set A, start time (E1) against GW friction (E2), with the drag fixed: the comparison for the owner's question 1.**
- R13-6 (refereed): Lemma D excludes R11-5's literal causal gain by double-pulsar self-drag. A zero-first-moment gain repairs it (still OPEN).
- The same drag mechanism, applied to R12-7's E2-h friction law (`C5_R12-7_report.md:145`), suggests γ ≲ 0.03 H₀ (R13-6 worker, suggested only).
- Compute:
  - (a) the E2-h self-drag on each star's orbital velocity and the double-pulsar bound on γ. Can E2's drag be removed the same way, and at what cost?
  - (b) for both E1 (repaired) and E2 (repaired if needed), the full set of stated observational tests and the near-cone energy budget on equal terms;
  - (c) the price lists side by side, against the axiom text.

Readings, per route:
- **VIABLE:** an explicit repaired model passing every stated test (including double-pulsar drag) on a stated parameter region, with prices named.
- **EXCLUDED:** a refereed bound violation for every parameter.
- **OPEN:** otherwise.

**R14-3. Subluminal edges: does any subluminal box law cancel the free shear mass μ_E or the graviton-cone shift Ξ?**
- R14-1's worker (unrefereed) finds:
  - in subluminal families A ≤ 0 everywhere, so Ξ < 0 for every edge vertex (graviton slower);
  - every subluminal edge tried gives μ_E > 0;
  - R9-2's shear-cancelling t* used a superluminal edge (v_max 1.6).
- Prove or refute, in a stated class of subluminal one-band (even or odd, gapped) laws:
  - (a) μ_E > 0 for every subluminal edge with a supplied zero-point vacuum;
  - (b) Ξ < 0 for every vertex.
- If both hold, the box route's graviton and shear sectors need tuning, or a superluminal edge. That is a choice between causality at the lattice scale and tuning.

Readings:
- **DERIVED:** (a) and (b) proved in the stated subluminal class (refereed).
- **REFUTED:** an explicit subluminal law with μ_E = 0 or Ξ ≥ 0, checked.
- **SUGGESTED:** otherwise.
- **R13-7 (is the e–γ split a theorem?) — CONFIRMED WITH CORRECTIONS. SUGGESTED overall, with a DERIVED regulated literal-edge subclass.**
  - **The subclass.** At one loop and fixed λ > 0, take a literal-edge Peierls-coupled Dirac electron with:
    - S odd and periodic, with S(q) = q in its box;
    - t = d² even and periodic;
    - |S| ≤ |q|;
    - the heavy-limit weight convex on the electron edge.
  - **The result there:**
    - Δ_λ(m) = c_e − c_γ is real-analytic for m > 0;
    - δc_γ = O(m⁻³);
    - δc_e → ¼⟨A(W² − d_x²)/(d_x²W³)⟩ < 0, a lattice 4/3 problem.

    So Δ_λ cannot vanish on any open mass interval.
  - **Extension:** to finitely many extra charged species, only along real-analytic heavy-mass trajectories where their photon contributions decouple.
  - **Not covered:** Wilson edges, general ℓ¹ generators, partners, arbitrary photon shapes, or λ = 0.
  - **Outside H2:** the heavy constant changes sign and can be tuned to zero. The next tested coefficient remains nonzero, and no interval-zero law is known.

### C5 Round 14, items 4–5 (pre-registered 21:15Z; launched now)

**R14-4. Graviton production: the mixed h–E kernel escape from X-G.**
- R13-2 (refereed, EXCLUDED bounded X-G): in a real, local, C⁴, cubic-covariant PSD Gaussian Hamiltonian of the six symmetric-tensor canonical pairs:
  - gapless axial TT forces vector and scalar partners;
  - one-sided transverse gauge flatness forces ω_TT = O(k²).
- Its named open escapes: mixed h–E kernels, auxiliary irreps, axis-only flatness, non-local symbols, and non-product sign cures.
- Take the cheapest: mixed h–E (off-diagonal) kernels in the Gaussian Hamiltonian, i.e. symplectic mixing. Can a PSD local cubic Gaussian with h–E mixing give linear TT with two polarizations and no gapless partners?
- If yes, can it be realized as a qubit or finite-slot model, which is X1's regime?
- If no, extend X-G's no-go to the mixed class.

Readings:
- **PRODUCED:** an explicit PSD local Gaussian (and, separately, a finite-slot realization) with linear two-polarization TT and no gapless partners, checked.
- **EXCLUDED:** a refereed no-go extending X-G to mixed kernels.
- **OPEN:** otherwise.

**R14-5. Λ: the P-T creation law with a spatially averaged lapse (P-r13a), the escape R13-3 left open.**
- R13-3 (refereed, OPEN):
  - V3's unit lapse caustics in smooth continuum completions;
  - V2 restores the Hamiltonian constraint (Lemma T).
- The worker named the escape: a lapse that varies locally but whose spatial average is fixed. It is global, not nearest-neighbour.
- Build it. Specify the global constraint ⟨N⟩_space = 1, or an equivalent, and the local clock dynamics. Then test:
  - (a) no caustic in collapsing halos;
  - (b) is the homogeneous Hamiltonian constraint still evaded, so that a constant vacuum is invisible without tuning?
  - (c) linear growth;
  - (d) the price against `AX:57` (non-local constraint) and the arrow.

Readings:
- **VIABLE:** an explicit model passing (a)–(c), with untuned Λ_eff = 0 and the prices named.
- **EXCLUDED:** a refereed inconsistency.
- **OPEN:** otherwise.
- **R14-2 (E1 vs E2) — CONFIRMED WITH CORRECTIONS. Both OPEN, and observationally tied.**
  - **E2's self-drag is confirmed.** Γ_i = 2γ|U_i|/(3M_ic²) and Ṗ_b/P_b = −3Γ_eff. That bounds γ to 0.032–0.047 H₀ (conservative envelope), or 0.016–0.024 H₀ from the signed timing measurement.
  - **Consequence for stationarity.** Genuine stationarity of E2 needs a history of many tens of Hubble times (more than 80 under the signed likelihood).
  - **The repair.** A causal passive high-pass friction kernel allows faster damping. It costs a cutoff, frequency-dependent GW damping, and a larger sink budget.
  - **E1's window.** The CMB velocity tightens E1's repaired-gain window (τ_c correction).
  - **Equal footing.** The E1/E2 content equivalence and the ≤ 8% budget difference hold asymptotically, under shared premises.
  - **Which is cheaper.** E1 is cheaper only under the report's price-counting convention.
- **R14-4 (mixed h–E graviton) — CONFIRMED WITH CORRECTIONS. EXCLUDED, as an extension of X-G in its class.**
  - **The class.** A translation-invariant real PSD Gaussian Hamiltonian with exactly six symmetric-tensor pairs per cell, a C² symbol at k = 0, proper-cubic covariance, and arbitrary h–E mixing.
  - **The result.** If both axial TT polarizations are linear, some direction has at least three positive linear branches, so a linear partner is always present.
  - **Outside the class:** auxiliary irreps, non-C² or non-local kernels, indefinite exact-constraint theories, and non-Gaussian phases.
  - **Corrections:** the gyroscopic wording, the soft limit and the Williamson step.
- **R14-5 (averaged-lapse P-T) — NOT CONFIRMED as VIABLE. OPEN.** It is a credible conditional zero-mode degravitation mechanism, with a correct CMC necessity lemma.
  - **The setting.** A smooth continuum theory imposing E_ni = 0, E^TL_ij = 0, a spatially uniform E_nn = λ(t), conserved stress, and a supplied global zero-frequency expansion law.
  - **What is proved there.** Bianchi exactly gives N(λ + p_E) = g(t) and λ̇ = −gθ_n.
    - Active vacuum compensation forces CMC slicing.
    - g ≡ 0 reduces to GR with a constant effective cosmological term.
  - **What the reader does.** An exact finite-rank Prony reader removes a constant w = −1 vacuum from a homogeneous constant-w mixture without tuning λ's value.
  - **Not established:**
    - a globally existing positive-lapse CMC foliation through collapse (assumed, not shown);
    - the positivity bound, which drops inhomogeneous curvature terms;
    - real, regular evolution through the tested phase transitions (the Prony law goes non-physical);
    - exact Λ̃ = 0 in a lumpy universe;
    - causal and Hamiltonian-stable g ≠ 0 dynamics.
- **R14-3 (subluminal edges) — CONFIRMED WITH CORRECTIONS. REFUTED.**
  - **Subluminality.** In the separable periodic one-band class, |σ′| ≤ 1 certifies whole-zone subluminality.
  - **(a) refuted: the shear can be cancelled subluminally.** The smooth gapped G_w(1.4) family has an exact conditional shear zero at each fixed mass. One common massless-limit setting suppresses (not exactly cancels) the shear of all light common-edge species, by O((ma)²).
  - **(b) refuted outside 𝒰₀.**
    - Theorem B: Ξ < 0 for every nonnegative nonzero transverse vertex independent of k_z, on the no-gapped-valley class 𝒰₀.
    - Outside 𝒰₀, the subluminal W08/W14 bands give positive E_g shifts, hence an E_g zero by interpolation.
  - **Not established:** a nonnegative T_2g witness, or a dressed graviton–matter cancellation.
  - **The empty Fock vacuum** remains the separate trivial-zero case.

### C5 Round 15, items 1–3 (pre-registered 21:41Z; launched now)

**R15-1. The CMC lattice-time model (R14-5): causality, stability and strong coupling of the constraint sector, and the vacuum it needs.** Conditional on R14-5, whose referee is running.
- R14-5's worker builds GR on CMC (York-time) slices, with the Friedmann zero-mode replaced by a P-T creation law. That is a cuscuton-type constraint fluid with an instantaneous elliptic lapse.
- Test:
  - (a) Is there superluminal information transfer through the instantaneous lapse when g ≠ 0? (The cuscuton literature argues no.)
  - (b) Ghosts, gradient instabilities or strong coupling of the extra scalar around FRW and around a static star. Compare with the projectable/non-projectable Hořava pathologies (RN L3).
  - (c) Does the CMC foliation exist through collapse to black holes?
  - (d) Can it coexist with the box route's grid zero-point vacuum (w ≥ 0, R11-3)? R14-5 says the model needs a w = −1 vacuum. Is there a pairing or partition that makes the vacuum w = −1?

Readings:
- **PASS:** (a)–(c) clean (no signalling, no ghost or gradient instability, foliation exists through collapse) and (d) resolved or priced, checked.
- **FAIL:** a refereed pathology (signalling, ghost, instability) in the stated class.
- **INCONCLUSIVE:** otherwise.

**R15-2. Set A E1: the spin-2 conserved-noise assembly for the repaired zero-first-moment gain.**
- R13-6 and R14-2 (worker): E1 with a zero-first-moment gain passes every stated test, but the spin-2 conserved-noise assembly is missing, along with exact finite-start CP and ḣ regularity.
- Build the spin-2 (TT plus gauge) noise kernel with transverse conserved noise, the zero-first-moment gain, and a finite start. Check:
  - CP;
  - Bianchi compatibility (conserved noise source);
  - TT weights vs the assumed O(1);
  - the PPN α₁/α₂ at second order;
  - the budget.

Readings:
- **VIABLE:** an explicit spin-2 E1 model passing every stated test, checked.
- **EXCLUDED:** a refereed inconsistency (e.g. conserved spin-2 noise is impossible with the repaired gain).
- **OPEN:** otherwise.

**R15-3. Graviton production: the auxiliary-irrep escape from X-G / G-mix.**
- R13-2 (X-G, refereed) and R14-4 (G-mix, worker) cover Gaussians on exactly the six symmetric-tensor pairs. The named open escape is extra canonical pairs (auxiliary irreps), which could absorb the partners.
- With extra local fields (vectors or scalars, or a second tensor) under the proper cubic group, can a PSD local Gaussian have exactly two linear TT branches and no other gapless branch?
- If so, is it finite-slot realizable?

Readings:
- **PRODUCED:** an explicit PSD local Gaussian with auxiliary fields and only the two TT branches gapless and linear, checked.
- **EXCLUDED:** a refereed no-go covering a stated auxiliary class.
- **OPEN:** otherwise.
- **R15-3 (auxiliary-irrep graviton):** worker reading OPEN; EXCLUDED if confirmed.
  - Theorem C, in class 𝒜: any finite auxiliary content, PSD, O-covariant, symbol continuous at k = 0. By characters at C4 (axis) and C2′ (face diagonal), two gapless TT branches force at least 4 gapless branches, or at least 5 with an h coupling.
  - TT along axes alone needs only 2 (A2 pseudo-scalars), but they are not TT off-axis.
  - The non-local k²P_TT symbol leaves flat partners; only a discontinuous symbol gives exactly 2.

  Referee running.

### C5 Round 15, item 4 (pre-registered 22:05Z; launched now)

**R15-4. A regular P-T reader: removing a constant vacuum through phase transitions and in a lumpy universe (the R14-5 gaps).**
- R14-5 (refereed, OPEN) supplies a credible conditional zero-mode degravitation mechanism, but two of its gaps are:
  - the finite-rank Prony reader goes non-physical (complex or singular) through phase transitions;
  - exact Λ̃ = 0 in a lumpy universe is not shown.
- Construct a regularized reader with these properties:
  - a causal linear filter on the slice-averaged density history, or a constrained fit, that annihilates exactly constant contributions;
  - real and regular for all histories with finite energy-density derivatives;
  - convergent to the w ≠ −1 content.
- Test it:
  - (a) through EW- and QCD-like transitions (S1/S2 sectors of R13-3);
  - (b) on a lumpy universe via the slice average (backreaction terms);
  - (c) on DESI-like evolving w;
  - (d) the residual Λ̃ and its tuning, if any.

Readings:
- **PASS:** an explicit regular reader giving Λ̃ = 0 to stated precision through (a)–(c) without tuning, checked.
- **FAIL:** a refereed no-go: no causal regular reader annihilates constants while tracking the stated content, in a stated class.
- **INCONCLUSIVE:** otherwise.
- **R15-2 (spin-2 E1 assembly):** worker reading OPEN.
  - Conserved spin-2 noise is built exactly from a finite start; this needs f(0) = f′(0) = 0, which the repaired gain has.
  - Lemma A: the theorem-U/Lemma-C walls bind only TT; the scalar and vector channels are instantaneous and finite.
  - Lemma B: a plain finite start violates Bianchi; a B term repairs it, and decays only with a zero-first-moment gain.
  - The TT weight is ¼ of the prior normalization; CP holds in the exact limit.
  - New budget term: constraint-channel record-noise energy, ~ρ_Λ × (1.2–2e12) if non-radiative noise gravitates (premise iii).

  Referee running.
- **R15-1 (CMC sector pathologies):** worker reading **FAIL on (a)**, pending the referee.
  - **(a) Signalling.** Lemma S: when g ≠ 0, a local impulse moves the gauge-invariant comoving density rate everywhere at once through a Yukawa kernel of range ~½ Hubble. Lemma C forces g ≠ 0 during every absorbed vacuum change. This influence is ordered by the global CMC time, so it cannot form a causal loop. If such influence does not count as "signalling", the reading becomes INCONCLUSIVE.
  - **(b) Ghosts, gradients, strong coupling.** One scalar, with sound speed → 1. A ghost appears for g > 6H² and a tachyon for g ≳ 1–5H². R14-5's unregularized reader enters the bad region. Cubic order is OPEN.
  - **(c) Collapse.** Lemma F′ gives a lapse floor N ≳ 1.5(mH₀)², so time does not freeze inside black holes (this corrects R14-5). Global CMC existence remains a hypothesis.
  - **(d) Grid vacuum.** Lemma V: an isotropic site-frame vacuum of any w is absorbed. This corrects R14-5's K5 "g ~ 1e122 H²". The outcome turns on the AX source/action bridge:
    - (d-i) resolved if the vacuum has no separate conservation law;
    - (d-ii) priced at one tuning or exact pairing if it does.
  - **Prices**, renamed to avoid a clash with R15-2: P-r15-1a (instantaneous g-influence), P-r15-1b (the reader keeps g ≲ 1–6H²), P-r15-1c (CMC foliation existence), P-vac′.

  Referee running. The R14-5 referee verdict is archived.

### C5 Round 15, items 5–6 (pre-registered 22:12Z, before launch; S17 still drafting round 16)

**R15-5. Producing the graviton at strong coupling: does a Gu–Wen-type qubit model escape the Gaussian exclusions?**
- X1, X-G and G-mix are EXCLUDED, and R15-3 (worker) says ≥4 or ≥5 gapless branches. All of these cover Gaussian or quadratic classes.
- The open route is a non-Gaussian, strong-coupling phase: Gu–Wen's helicity-±2 qubit model and Xu's rank-2 spin liquids, where projection or energetics may gap the helicity-0/±1 modes.
- **Setting:**
  - Prior art first: the repo's lane R (`TESTS:692-767`), R9-9 and R13-2, and Gu–Wen / Xu / Pretko / Rasmussen–You–Xu, which may be downloaded as untrusted text.
  - Then:
    - (a) state precisely which assumption of Lemma P / Theorem G / Theorem C the model violates, if any;
    - (b) count the gapless branches it claims and their helicities, and check by a small computation where feasible (a perturbative effective Hamiltonian, or a classical/large-S spectrum);
    - (c) does matter couple to the h-modes through a conserved T with a 1/r pull (the Weinberg–Witten status)?

Readings:
- **PASS:** a stated qubit model, local terms only, whose low-energy sector has exactly the two helicity-±2 gapless modes plus a universal 1/r coupling, checked at the level the literature or the probe supports, and naming the Gaussian assumption it breaks.
- **FAIL:** a refereed no-go extending Theorem C to the stated non-Gaussian class.
- **INCONCLUSIVE:** otherwise, with the decisive missing computation named.

**R15-6. Can the lattice-time reader keep the CMC sector healthy? A sign theorem for g.**
- R15-1 (worker) finds ghosts or tachyons for g ≳ 1–6H², health for g ≤ 0, and signalling ∝ g.
- **Question:**
  - (a) Is there a reader rule within R14-5's class (causal, regular, annihilates constants) whose g is ≤ 0, or ≤ cH² with c below the tachyon threshold, for all physically allowed histories: phase transitions, lumpy late times, DESI-like w?
  - (b) Is there a rule that keeps |g| small enough that the R15-1 Lemma S influence is below current bounds? State the bound used, for example pulsar timing or lunar laser ranging on instantaneous Yukawa couplings.
  - (c) Or is g's sign forced by the null energy condition (NEC) and Lemma C?

Readings:
- **PASS:** an explicit reader rule with a proved sign or size bound on g in a stated class of histories, and the influence below a stated bound.
- **FAIL:** a refereed proof that every allowed reader gives g above threshold, or above a bound, on some allowed history.
- **INCONCLUSIVE:** otherwise.

### C5 Round 16, items 1–5 (pre-registered 22:20Z from S17 §5, text fixed before any run; R16-1/R16-2 launched now, R16-4 next, R16-3/R16-5 as slots free)

New rules from S17: every law states its whole-zone v_max; every frame-tied kernel states its self-force on a moving compact body; every Ward requirement says standard or deformed.

**R16-1. Is the electron–photon split a theorem on the edges physics would actually use? The interval no-go for Wilson edges, including the subluminal D1(r).**

- **Plain question.** R13-7 proved that the split cannot vanish over any mass range, but only for the literal edge. That edge has seven same-mass electron copies and is already excluded by the Z width (R9-1). Usable Dirac edges are Wilson edges, and R14-1's subluminal Dirac is one. On those, R13-7's control saw the split grow linearly in mass with a shape-dependent sign. Does the no-go hold where it matters?
- **Setting.**
  - Class 𝒬_W: R8-5's BQ electron with a Wilson term W even, periodic and C², including R8-5's r = 1 box and R14-1's D1(r) with r ≤ 1/√d (b = 1.4, 1.2, 1.0).
  - R13-7's photon class: t = d² even and periodic, H2′ shapes.
  - Peierls coupling, Feynman gauge, fixed λ > 0, one loop, on-shell c_e.
  - Variant 𝒬_W^P: add two complex selectrons with R13-1's gauging.
  - Excluded: λ = 0; non-Peierls vertices; two loops; N=4 content.
- **Prior art (count once).** R13-7 and verdict (`vR13-7:3-30`; Wilson control `C5_R13-7_report.md:48,144-148,202`); R8-5 (`vR8-5:7`, non-decoupling under r); R14-1 D1(r) (`C5_R14-1_report.md:184-211`); R9-1 (`TESTS:3840`); R10-1 Theorem D; R13-1 partner gauging.
- **Probes.**
  - (a) Extend Lemma A (real-analyticity for m > 0) to 𝒬_W.
  - (b) The large-m expansion. Identify the linear-in-m coefficient (worker suggestion: a zero-mean W″-moment). Prove a sign or nonvanishing on a stated subclass containing D1(r ≤ 1/√d), or show it can vanish. If it vanishes, carry on to the next coefficient.
  - (c) Numerics on D1 at b = 1.4, r = 1/√3: Δ_λ(m) for m ∈ [0.01, 3] and Δ_λ(0⁺), at three resolutions.
  - (d) Repeat (b)–(c) for 𝒬_W^P.
  - (e) Prices.
- **FIXED readings.**
  - **DERIVED:** a refereed proof that Δ_λ cannot vanish on an open mass interval in a stated Wilson class containing D1(r ≤ 1/√d) at fixed λ > 0.
  - **REFUTED:** an explicit untuned law in 𝒬_W (or 𝒬_W^P, stated) with Δ_λ ≡ 0 on an interval, checked.
  - **SUGGESTED:** otherwise.
- **Expectation.** SUGGESTED. The linear coefficient's sign already varies across shapes, so a class-wide sign is unlikely. A DERIVED subclass on D1 is possible if r ≤ 1/√d fixes the W″-moment's sign. REFUTED is not expected: isolated zeros (m ≈ 3.3 in R13-7's Wilson S1) are not interval zeros.

---

**R16-2. How many tunings put every light charged particle and the photon on one cone? (The matter-speed rows of the count.)**

- **Plain question.** R13-8's bookkeeping charges one tuning per matter species (the N_s in N_s + 7). The R13-7 worker argues the opposite: the split is analytic in mass, and physical masses are ~1e-17 to 1e-23 in Planck units, so one tuning at zero mass fixes every light species. The referee called that a plausible reading, not a theorem: it is not uniform in λ, band shape, species or counterterm structure. Charges differ, spins differ, and the photon's own shift sums over every species. So is the number of tunings 1, 2, one per spin class, or N_s?
- **Setting.**
  - One-loop QED on Z³ × ℝ with N_s charged species: charges q_i ∈ {1, 2/3, 1/3}, spins 0 and ½, masses m_i a ∈ [1e-23, 1.5e-17] (the SM charged range at a = ℓ_P, a reading on `AX:189-190`).
  - Every species on one common edge family per spin: literal and D1(r) for Dirac, G(b) for scalars. Peierls coupling.
  - Allowed tunings: edge-shape parameters, a photon-kinetic counterterm, matter-kinetic counterterms. Each one counts.
  - Excluded: non-abelian sectors, W±, two loops.
- **Prior art (count once).** R13-7 (`C5_R13-7_report.md:50,211`; `vR13-7:28`); R13-8 (`vR13-8:15-22`); R14-3's common-setting result (`vR14-3:18`, the shear analogue); R8-5's comparators (`C5_R8-5_report.md:261`, 2.66e-19); F2's 3.1e-17 (`TESTS:2380`); R10-1 Lemma N(m).
- **Probes.**
  - (a) The small-m expansion δc_i(m) = q_i²[F_s(0⁺) + F_s′·(ma) + O((ma)² ln ma)] and δc_γ = Σ_j q_j² G_s(m_j), with constants, at fixed λ > 0 and as λ → 0 (state the IR treatment).
  - (b) The minimal set of tunings that makes |c_i − c_γ| below the stated comparators for every SM charged species. Show that one fewer does not suffice in the stated class.
  - (c) Can one shape condition null F_{1/2}(0⁺) and F_0(0⁺) together, or does each spin class need its own?
  - (d) The residual after tuning, for the heaviest species (top-like m a ≈ 1.4e-17).
  - (e) Map the result onto R13-8's N_s rows.
- **FIXED readings.**
  - **COUNTED:** an explicit number n_t, with a refereed proof that n_t tunings suffice for every species in the setting, to the stated comparators, and that n_t − 1 do not, in a stated class.
  - **OPEN:** otherwise.
- **Expectation.** COUNTED with n_t independent of N_s, most likely 2 or 3: one photon-side condition plus one shape or counterterm condition per spin class. Residuals scale with (ma) and fall far below comparators except possibly for the heaviest species. A λ → 0 obstruction (IR logs) is the likeliest reason for OPEN.

---

**R16-3. The second graviton polarization: can any slower-than-light edge put T₂g on the matter cone?**

- **Plain question.** On slower-than-light edges without extra valleys, the graviton is always slower than matter (R14-3 Theorem B). With heavy valleys one polarization (E_g) can be zeroed, but the other (T₂g) stayed negative in every test. If T₂g is negative for every allowed edge, then the box route's graviton cone needs pairing or a per-polarization counterterm, and edge shaping cannot do it.
- **Setting.**
  - R14-3's separable periodic one-band class with |σ′| ≤ 1, gapped valleys allowed (outside 𝒰₀).
  - R9-9's TT vertex with its assumed Ward completion. This is prescription-scoped; state it in every claim.
  - Nonnegative nonzero transverse vertices; m ∈ {1, 0.3, 0.1}.
  - Excluded: pairing; deformed W2 (R16-5); matter's own graviton-loop shift (R11-1(b)).
- **Prior art (count once).** R14-3 and verdict (`vR14-3:14-22`; W08/W14); R14-1 (`vR14-1:13`); R13-5 (`vR13-5:9-13`; T₂g weight tuning on L-U); R11-1(b) (`vR11-1:17-19`); R9-9 Theorem T.
- **Probes.**
  - (a) Prove Ξ_T2g < 0 for every nonnegative nonzero vertex in a stated class strictly larger than 𝒰₀, including W08/W14-type gapped valleys. Or exhibit a subluminal law with Ξ_T2g ≥ 0.
  - (b) If (a) finds a zero, find one law with Ξ_Eg = Ξ_T2g = 0 at a common mass, and count the tunings, with and without P62's shear condition.
  - (c) Prices.
- **FIXED readings.**
  - **DERIVED:** a refereed proof of Ξ_T2g < 0 in a stated class containing 𝒰₀ and gapped-valley laws.
  - **REFUTED:** an explicit subluminal law with Ξ_T2g ≥ 0, checked. Report separately whether a simultaneous E_g/T₂g zero was found.
  - **SUGGESTED:** otherwise.
- **Expectation.** SUGGESTED leaning DERIVED for T₂g, because every tested shift is negative and T₂g weights mixed derivatives that the valley trick does not reach. A simultaneous zero is not expected.

---

**R16-4. Set A, E1: does anything observable remember the start? (Initial-state dependence, for `AX:94`.)**

- **Plain question.** E1's start time comes with a fixed initial state: meters in their vacuum, h = ḣ = 0. The worker's price count favours E1 unless that state counts as a "privileged state" under `AX:94` (`C5_R14-2_report.md:273`). The J₀ channel has a memory as long as the age, and Var h grows like ln T. Do late-time observables depend on the initial state, or does any reasonable start give the same universe?
- **Setting.**
  - R13-6's linearized preferred-frame E1 model with the repaired gain (P-r13b) and its finite-start covariance (`vR13-6:27-31`), with a stated bandwidth regulator for ḣ. Use R15-2's spin-2 kernel if it has been refereed.
  - Initial-state class: Gaussian meter and metric states with finite energy per mode (thermal, squeezed, displaced), up to a stated bound.
  - Observables: R11-5/R13-6's test list (lab decoherence, near-cone budget, PPN-type, double-pulsar drag, record growth) evaluated at t − t₀ ≥ t_H.
  - Excluded: E2; non-Gaussian initial states.
- **Prior art (count once).** R13-6 and verdict; R14-2 and verdict (`vR14-2:11`); R11-5; R12-4 (`vR12-4:15`, a temporal boundary is not a privileged site); Lemma S (`vR13-6:25`).
- **Probes.**
  - (a) For each listed observable, the difference between the vacuum start and the worst state in the class at t − t₀ = t_H, with constants.
  - (b) Whether an attractor exists, and its rate (J₀ tails, t^{−1/2}).
  - (c) Which quantity, if any, keeps an O(1) memory of the start at every time.
  - (d) Prices.
- **FIXED readings.**
  - **WASHED-OUT:** every listed observable at t − t₀ ≥ t_H differs between any two states in the class by less than its observational comparator, with proof, checked.
  - **STATE-DEPENDENT:** a refereed demonstration that some listed observable differs beyond its comparator between two states in the class.
  - **OPEN:** otherwise.
- **Expectation.** WASHED-OUT for every listed observable. The J₀ channel's exact memory should leave an unobservable logarithmic dependence. The owner question then becomes whether an unobservable initial datum counts as a privileged state.

---

**R16-5. GW170817 on the grid: a preferred-frame second-order Ward identity, and the graviton–matter poles under it.** *(Launch only if time allows.)*

- **Plain question.** R13-5 found that the standard second-order Ward identity cannot hold on any periodic band: the pair-creating stress drops out of H, P and K, and the lattice's boost anomaly blocks closure. So the gauge-invariant comparison of graviton and matter cones, which is what GW170817 tests, had nothing to compute in. On a grid with a preferred frame, the natural gauge group is the foliation-preserving one, as in khronometric or Hořava gravity. Is there a deformed W2 with that group that admits the pair stress? If so, what are the physical pole positions, and what does the extra scalar mode do?
- **Setting.**
  - R9-9's N-type box graviton. R8-2's stress plus R13-5's W1 pair kernel.
  - W2_pf: the second-order identity for foliation-preserving deformations (lapse a function of time only, shifts arbitrary).
  - Complex scalars and Clifford-flat fermions on G(b) and literal edges; m = 1 and 0.3; with and without P46 pairing.
  - Excluded: standard W2 (R13-5 covers it); nonlinear gravity.
- **Prior art (count once).** R13-5 and verdict (`vR13-5:7,13`); R13-8's gauge kernel (`vR13-8:11`); RN L3 (projectable Hořava strong coupling); R14-5's CMC discussion (`vR14-5:86-88`, cuscuton, Bhattacharyya et al.); RFW.
- **Probes.**
  - (a) Write W2_pf. Construct a pair stress satisfying it, or prove none exists in a stated class.
  - (b) Show that the TT and matter pole positions are W2_pf-gauge-invariant.
  - (c) Compute c_m − c_T for both polarizations, in κ_lat units and at a = ℓ_P, with and without pairing.
  - (d) The extra scalar graviton mode: its dispersion and whether it is strongly coupled.
  - (e) Prices.
- **FIXED readings.**
  - **SPLIT-PRESENT:** a nonzero W2_pf-invariant pole split for every W2_pf-complete stress in a stated class (refereed if class-wide), with numbers.
  - **SPLIT-ABSENT:** the split vanishes identically for the W2_pf-complete stress (pairing stated), with the reason, checked.
  - **OPEN:** otherwise, including no W2_pf-complete stress constructed.
- **Expectation.** A W2_pf-complete stress exists, since boosts are no longer gauge. SPLIT-PRESENT without pairing, at the edge-anomaly size. SPLIT-ABSENT for TT with matched pairing (residual 2κm²J₂). The likeliest failure is a strongly coupled extra scalar, as in projectable Hořava.

---

- **R15-5 (strong-coupling graviton):** worker reading **INCONCLUSIVE**.
  - **(a)** The exact-constraint N-type escapes by breaking positive semi-definiteness. Its physical projector jumps at k = 0, which is the same as Theorem C's discontinuous-symbol edge.
  - **(b)** With CCR fields there are exactly two branches, helicity ±2, with ω = |k| and a 1/r pull.
  - **Lemma L, the compactness ladder:** z = 1 needs a noncompact h and E. Qubit/qubit is z = 3 with contact only, and rotor rungs are z = 2.
  - **Lemma W:** strong-penalty perturbation theory to all finite orders gives O(k³).
  - **Lemma T:** the sourced constraints are kept only if matter has T⁰ⁱ = Tⁱ⁰ as an exact collision invariant. T′: periodic bands fail this, so the boost wall reappears.
  - **Decisive missing computation:** a non-perturbative TT stiffness (static χ_TT ~ 1/k²) at penalties comparable to the couplings.
  - **Prices:** P-r15-5a/b/c.

  Referee running.

#### C5 Round 15 referee verdicts (recorded 22:40Z; codex gpt-5.6-sol, xhigh)

- **R15-1 referee: CONFIRMED WITH CORRECTIONS. Reading FAIL** (`agents/C5_R15-1_referee_verdict.md`).
  - **Lemma S is confirmed.** A smooth, compact, conserved source gives the same instantaneous exterior response.
  - **It counts as signalling.** It is superluminal information transfer under the fixed reading. Preferred-time ordering prevents only backward-in-time messages, so the INCONCLUSIVE fallback does not apply.
  - **Signalling is unavoidable during active vacuum compensation.**
  - **Scope of the other parts:**
    - S_E represents the linear k ≠ 0 sector only.
    - A(k) and the g > 6H² ghost band are exact. The 1–5H² tachyon thresholds are frozen-background diagnostics, not bounds.
    - Lemma F′ is a floor on each slice (exact constant 1.51875(mH₀)²), not a theorem about collapse continuing.
    - Global CMC existence is open.
    - Lemma V (d-i) needs the source bridge changed to allow momentum exchange. Under (d-ii), ρ_v + p_v = 0 is required.
  - **Dated consequence for R14-5** (OPEN, conditional zero-mode degravitation): in its smooth continuum form, the mechanism signals superluminally whenever it is active. This is recorded as a refereed FAIL of the R14-5/CMC model on causality; R14-5's other findings stand.
- **R15-2 referee: CONFIRMED WITH CORRECTIONS. Reading OPEN** (`agents/C5_R15-2_referee_verdict.md`).
  - Lemma A is confirmed for k ≠ 0. A finite switch-on still needs Lemma B's constraint data.
  - Lemma CU is not universal; it holds only within the channel-diagonal common-profile ansatz.
  - The f(0) = f′(0) = 0 condition is necessary and sufficient for the finite-variance construction without singular boundary terms.
  - The B term and the TT weight ¼ are confirmed. A dropped derivative invalidates the finite constant and the exact budget endpoints, but not the ¼.
  - Exact full-instrument CP is not proved.
  - The |u₁| formula is confirmed (I_F = 21/32). Premise (iii) is not established, so the overshoot is conditional, not an exclusion.
- **R15-3 referee: CONFIRMED WITH CORRECTIONS. Reading EXCLUDED** in the finite, continuous, PSD, cubic-covariant Gaussian auxiliary class (`agents/C5_R15-3_referee_verdict.md`).
  - Two genuine TT branches on an axis and a face diagonal force dim G ≥ 8, hence ≥ 4 gapless branches.
  - The ≥ 5 bound with an h coupling needs a rank-2 TT residue.
  - The C4+C2′ minimizer list omitted 4A₁+4A₂.
  - Lemma N is conditional, not a theorem.
  - Discontinuity is necessary only within the finite PSD class.
- **R15-6 (reader sign theorem): worker reading PASS on class H1 only; INCONCLUSIVE for all histories.**
  - The running-minimum reader MR gives Λ̃ ≡ 0 and g ≤ 0 on H1.
  - Theorem L: no linear fading-memory reader that is exact on dust and radiation is sign-safe. This hits R15-4's class.
  - Lemmas L and U: uniform caps fail on fast changes with α > c/4.
  - Local tests do not bound g. Hubble-scale data give |g| ≲ 0.05H₀² (suggested).
  - This does not undo R15-1's FAIL: g ≠ 0 remains during every absorbed drop.

  Referee running.
- **R15-4 (regular P-T reader): worker reading FAIL**, limited to test (c) and to class 𝓡⁺. Tests (a) and (b) PASS within that class.
  - **The reader:** a causal linear two-register reader fed by E = −dρ_tot/du. It annihilates constants exactly. κE = 2S, so there is no new non-locality. Lemma P2: ρ̂ ≥ 0 on 𝓗₄, so the clamp is not needed.
  - **(a) Transitions.** Bounded error for any release width. EW and QCD are fine. e⁺e⁻ annihilation gives a ΔN_eff equivalent of +0.43 (D1) and +0.16 (R*), from RECALLED comparators; no BBN network was run.
  - **(b) Lumpy universe.** Local reader identities hold, and the lapse positivity gap closes, given the SEC and no recollapse. Residuals are ~1e-7 Λ_obs.
  - **(c) DESI-like w.**
    - Lemma N+: every causal, linear, time-invariant reader that is exact on dust and never negative after reheating has G ≤ x(4−x)/3, and G ≤ 0 for phantom content.
    - Lemma N0: a dead band at w ≈ −1.
    - The DR2 fits are phantom at z ≳ 0.4, so the H(z) errors are 24–43%.
  - **The escape:** a non-phantom true dark energy whose reading equals the DESI curve. Its cost is g/H² ~ −0.3 to −1.1 today, so the R15-1 signalling is active now.
  - **(d)** The vacuum's contribution to Λ̃ is exactly zero, with no tuning.

  Referee running.
- **R16-2 (tuning count): worker reading OPEN.** The count is neither 1 nor one per spin class.
  - **Lemma Q (proved).** The species shift is q_i²F_s(m_i), and the photon shift is one number that does not depend on λ. So one light-mass tuning aligns different charges only if F_s(0⁺) = 0. This is the gap in R13-7's single-species reading.
  - **Lemma T′ (proved).** Tadpole and seagull bounds hold for any non-rising band with a nondecreasing photon symbol.
  - **Lemma F (checked, not proved).** F_{1/2}(0⁺) ∈ [−16.1, −4.5] and F_0(0⁺) ∈ [−3.6, −1.6] on the stated edges. An overshooting edge has a zero, but it is superluminal along an axis.
  - **Proposition C, given Lemma F.** One-loop e, u and d cones sit about 1e-3 apart. Each tuning is set to about 1e-16.
    - one counterterm per species: N_s − n_max + 1 = **7** of the 9 SM charged fermions;
    - one counterterm per (spin, |q|) class: **3**;
    - with a superluminal over-rising edge: 2.
  - **κ_γ is required.** No IR log was seen. Residuals are at least 36× below the comparator.
  - **Prices:** P73 is refined to one tuning per (spin, |q|) class.

  Referee running.

### C5 Round 16, item 6 (pre-registered 22:50Z, before launch)

**R16-6. After R15-1's FAIL: can Λ be removed without signalling, i.e. with g ≡ 0?**
- **Plain question.** R15-1 (refereed FAIL) shows the CMC mechanism signals faster than light whenever g ≠ 0. Lemma C says g ≠ 0 whenever a vacuum *change* is actively absorbed. R15-6 (worker) suggests a reader built from the content's equilibrium equation of state gives g ≡ 0 through equilibrium crossovers and mass thresholds. In that case the "vacuum change" is part of the content's own EoS, so it is never absorbed. Does that remove Λ with no signalling at all?
- **Setting.**
  - R14-5's model with Lemma C.
  - Readers in two classes: (i) R15-6's P-EoS class, where the creation law carries ρ_EoS(T(h)); (ii) any reader with g ≡ 0 identically.
  - Histories:
    - the SM electroweak and QCD crossovers (RECALLED lattice EoS is acceptable, labelled);
    - e⁺e⁻ annihilation;
    - a first-order transition with supercooling, as a control;
    - inflation followed by reheating;
    - DESI-like dark energy.
- **Probes.**
  - (a) Characterize every history and reader for which g ≡ 0 while the observed Λ̃ = 0. Does this coincide with "the constant is a pure c-number in the EoS"?
  - (b) Can g ≡ 0 handle a supercooled or inflationary vacuum drop, or is a drop out of equilibrium necessarily absorbed (g ≠ 0)?
  - (c) What does the observed late-time acceleration have to be under g ≡ 0? Is it a true w ≠ −1 content, with a constant Λ unobservable?
  - (d) Prices, including whether "the creation law knows the EoS" is a new axiom text.
- **FIXED readings.**
  - **PASS:** a stated reader class with g ≡ 0 that removes a constant vacuum (Λ̃ = 0) through the stated SM history including inflation/reheating, checked, with its prices named.
  - **FAIL:** a refereed proof that any history containing an out-of-equilibrium vacuum drop (inflation's end or supercooling) forces g ≠ 0 for every reader giving Λ̃ = 0. That would make R15-1's signalling unavoidable for every universe with inflation.
  - **INCONCLUSIVE:** otherwise.
- **Expectation.** FAIL for inflation's end by Lemma C, unless reheating counts as "equilibrium". In that case the result is PASS with the EoS price. The likely sticking point is whether the inflaton potential is "content" or "vacuum".
- **R16-1 (Wilson-edge interval no-go): worker reading DERIVED**, pending the referee. The class is a stated Wilson class containing D1(r ≤ 1/√3) at b = 1.4, 1.2 and 1.0, with fixed λ > 0.
  - **Theorem W:** on Wilson edges δc_e = L·m + O(1), with a closed-form L; the photon is O(m⁻²).
  - **Lemmas K and K′:** Ω is convex in the photon momentum, so L > 0 under (H0) W ≥ 0 and either (H3) or (H3′) with b ≥ 0.505.
  - **So** Δ_λ → +∞, and by analyticity there is no interval zero.
  - **Probe (c):** Δ(0⁺) = −10.877 e²/16π² on D1(1.4, 1/√3), with one isolated zero at m ≈ 24.
  - **Outside the class:** L takes both signs, and a tuned L = 0 law has c₀ ≈ −2.15.
  - **𝒬_W^P:** DERIVED-level with selectrons, SUGGESTED with the photino loop.
  - **v_max:** D1(r = 1/√3) has v_max ≤ 1, and the R8-5 Wilson boxes are superluminal.
  - **What it closes:** S17's gap that the derived subclass was only the Z-width-excluded literal edge.
  - **No new price;** P73 still applies.

  Referee running.

### C5 Round 16, item 7 (pre-registered 22:52Z, before launch)

**R16-7. R15-5's decisive computation: does a finite-slot N-type model at strong penalty have an Einstein–Hilbert TT stiffness?**
- **Plain question.** R15-5 (worker) shows:
  - real-valued fields give exactly two graviton modes;
  - qubits give k³ at every finite order of perturbation theory.

  What is left is the non-perturbative regime, where the penalties are comparable to the other couplings. The signature of a light-speed graviton there is a static TT susceptibility χ_TT(k) ~ 1/k², rather than 1/k⁴ or 1/k⁶.
- **Setting.**
  - A Z_N clock / finite-slot version of the N-type (R15-5 §1; N0914), with penalties U comparable to the couplings J and g.
  - Any controlled non-perturbative method that fits the machine. The method and its control parameter are stated before running. Candidates:
    - exact diagonalization on the smallest cluster with ≥ 2 nonzero k;
    - sign-free QMC in a dual basis, if one exists;
    - a variational/tensor ansatz with an error bar;
    - large-N clock or self-consistent harmonic approximation, labelled uncontrolled if so.
  - Excluded: claims from uncontrolled methods counted as PASS.
- **Prior art (count once):** R15-5 and its referee (when back), R13-2's X-S sign problem, R12-5, R11-2, Gu–Wen, Xu, and the Hermele–Fisher–Balents spin-ice emergent photon (a comparator for the U(1) analogue).
- **Probes.**
  - (a) Prove or find a sign-free basis.
  - (b) Compute χ_TT(k) and the scalar-source static response on the largest feasible system. Fit the k-power, with its subtraction named.
  - (c) Run a U(1) spin-ice analogue control with the same method: it must reproduce χ ~ 1/k² for the emergent photon.
  - (d) Prices.
- **FIXED readings.**
  - **PRODUCED-EVIDENCE:** a controlled method that passes the control (c) and gives χ_TT ~ 1/k² with the scalar response 1/k², with error bars.
  - **NOT-PRODUCED-EVIDENCE:** the same method passes the control and gives a steeper power.
  - **INCONCLUSIVE:** the control fails, the method is uncontrolled, or the sizes are too small to fit a power.
- **Expectation.** INCONCLUSIVE, because of system size. A sign-free dual basis would itself be a durable result.
- **R16-4 (E1 start memory): worker reading STATE-DEPENDENT** for 𝒢(1, 1/ℓ); OPEN for small classes. A referee is required.
  - **What remembers the start.** Free TT wave data at t₀ are kept exactly forever (Lemma T: no attractor). One quantum per mode up to 1/ℓ gives Δρ = ħc/(4π²ℓ⁴), which is 2.4e3 to 5.9e19 ρ_Λ.
  - **What forgets it:**
    - record-current perturbations decay as t^{−1/2};
    - meter modes stay within a Λ(n_b)×vacuum bound (Lemma M);
    - B is gone in ~40τ.
  - **What does not depend on it:** drag; first-order PPN.
  - **The log memory** belongs to the start time, not the start state.
  - **New price, P-r16a:** the law supplies the initial TT datum h = ḣ = 0, which makes the AX:94 owner question physical.
  - **E1 against E2:** E2 keeps 96–99% of the initial TT energy too, so the start question does not separate the two routes.

  Referee running. Its key question: whether this is E1-specific or just GR's free data.

#### C5 Round 15 referee verdicts, part 2 (recorded 22:57Z; codex gpt-5.6-sol, xhigh)

- **R15-4 referee: CONFIRMED WITH CORRECTIONS. Bounded FAIL in 𝓡⁺** (`agents/C5_R15-4_referee_verdict.md`).
  - **The readers.** D1 and R* are causal, finite-state, linear readers. They ignore constants exactly, read dust and radiation exactly, stay ≥ 0 on 𝓗₄, and replace Prony's singularities with bounded transients.
  - **Corrections and scope.**
    - The lumpy identity is −d𝓔/du = 2S, not κ(−dρ_tot/du) = 2S.
    - The lumpy residual is a recalled-input linear estimate.
  - **Lemma N+ is confirmed:** no reader in 𝓡⁺ tracks DESI DR2 CPL, whose early asymptotes are phantom.
  - **The escape (inverse reading) is confirmed.** It leaves g/H₀² = O(1) today.
  - **Relation to R15-1.** R15-4 is consistent with R15-1's causality FAIL and subordinate to it. It does not rehabilitate the CMC model.
- **R15-5 referee: CONFIRMED WITH CORRECTIONS. Reading INCONCLUSIVE** (`agents/C5_R15-5_referee_verdict.md`).
  - **The exact noncompact N-type works but is unreduced-indefinite.** It has:
    - a positive two-pair TT quotient with ω² = Jg|q̂|², helicity-±2 characters and an attractive 1/r;
    - an indefinite energy before reduction;
    - a TT projector that cannot be continuous at k = 0. The identification with X2 is not literal.
  - **Compact characters cannot make a linear mode.** Regular lifted compact-character Hamiltonians, and each liftable finite Schrieffer–Wolff order, give ω = O(k³). This does not control fixed-N aliasing, high orders, resummation or genuine strong coupling.
  - **The GR source would need symmetric, locally conserved matter stress.** Generic periodic bands fail this under T′'s hypotheses.
  - **No PASS and no FAIL.**
- **R15-6 referee: NOT CONFIRMED (the PASS). Reading INCONCLUSIVE** (`agents/C5_R15-6_referee_verdict.md`).
  - **Confirmed:**
    - Identity I (for R > 0) and Lemma B. Vacuum transfers stay indirectly visible through the receiving sector's enthalpy.
    - MR gives exact cancellation and g ≤ 0 on H1 after a quiet start.
    - No linear fading-memory reader that is exact on dust and radiation keeps g ≤ 0 after sharp releases (Theorem L).
    - Fast-change caps trade against tracking or expansion.
  - **Why it is not a PASS:** no uniform influence bound is proved on H1.
  - **Why it is not a FAIL:** the negative results do not cover all allowed readers.
- **R16-5 (preferred-frame W2): worker reading OPEN, with a no-go for the referee.** This contradicts the registered expectation that the stress exists.
  - **Theorem T_pf.** The zeroth moment of W2_pf under constant shifts requires the momentum symbol g to be affine with a common slope wherever the vertex is nonzero. With continuity and cubic rotations, this forces g ≡ 0 and θ ≡ 0, standard or deformed.
  - **The trivial solution is excluded by observation:** with g ≡ 0, light would not redshift.
  - **The wall moves from boosts to translations;** it does not go away.
  - **The pair channel** enters the strain moments but cannot repair the identity.
  - **Escapes:**
    - a discontinuous momentum symbol, with 1/r tails and vertices that never cross the face (P-pf1);
    - the band tower (P64).
    - Smooth edge decoupling fails.
  - **Carried over:** R13-5's TT floor of 4.4–5.5e-3 per species at a = ℓ_P.
  - **Bearing on R15-1:** the projectable scalar has no Lemma-S local channel.

  Referee running.

### C5 Round 16, item 8 (pre-registered 23:06Z, before launch)

**R16-8. Wall W7: is the off-box gravity tail physical? Build the gravity sector and the physical domain of R12-1's completion.**
- **Plain question.** R12-1's completion of the off-box Killing defect needs a 1/r^{d−1} tail. R13-4(ii) left it OPEN: the completion is only a local germ, the gravity sector and physical domain are unbuilt, and the gauge generator may be non-local. R16-5 (worker) finds that the same zone-mean anomaly blocks preferred-frame translations unless the momentum symbol is discontinuous, i.e. has 1/r tails. Is W7's tail the same object as R16-5's P-pf1? Is it constraint-solving (harmless) or physical?
- **Setting.**
  - R12-1's ansatz, the R13-4(ii) germ, R9-9's graviton, and the R14-1 subluminal box (b = 1.4).
  - Linear order in κ; d = 3; box matter.
  - Excluded: nonlinear gravity, pairing.
- **Prior art (count once):** R12-1 and its verdict (`vR12-1:15`), R13-4 and its verdict (`vR13-4:18`), R16-5 (worker, unrefereed), R14-1, R9-9, Coulomb-gauge QED, and the RFW F2 first-jet obstruction.
- **Probes.**
  - (a) Complete the germ: write the gravity-sector generator and the physical (gauge-invariant) domain, or prove no local completion exists in a stated class.
  - (b) Test the R13-4 criterion: does a bounded gauge-invariant observable at distance r respond instantaneously, at size ∝ r^{−(d−1)}?
  - (c) Relate the result to R16-5's T_pf, the sawtooth symbol and P-pf1. Are they the same price?
  - (d) Prices.
- **Rules.** Every tail clause names its subtraction. Every law states its whole-zone v_max. Every Ward statement says standard or deformed.
- **FIXED readings.**
  - **LOCAL-EQUIVALENT:** a constructed completion whose tail acts on no bounded gauge-invariant observable outside the light cone, checked.
  - **PHYSICALLY NON-LOCAL:** a refereed demonstration of a bounded gauge-invariant observable responding instantaneously through the tail.
  - **OPEN:** otherwise.
- **Expectation.** OPEN or PHYSICALLY NON-LOCAL, with the same price as P-pf1.
- **R16-3 (T₂g on the matter cone): worker reading REFUTED.** This is contrary to the expectation. All claims are within R9-9's vertex, the assumed W1 and the supplied vacuum; in the Fock vacuum Ξ ≡ 0.
  - **Witness Z1.** A zigzag subluminal edge (max|σ′| = 1, v_max < 1, valleys at ~0.36/a) has Ξ_T2g = +3.9e-4 and +2.8e-4 (M and U) at m = 0.3. Three evaluators agree, and a smoother-turn control is negative.
  - **IBP identity:** Ξ = (1/32)⟨|V|²(5v_z² − 1)/ε⁵⟩.
  - **Lemma V:** the every-vertex form already fails on W08 and W14.
  - **Theorem B″ (DERIVED-type subclass).** If every flank ending at a gapped valley has |σ′| ≤ 1/√5, then Ξ < 0 for every vertex.
  - **(b) Simultaneous E_g = T₂g = 0** from convex mixes at m = 0.1, 0.03 and 0.01, for M and U separately. The count is two edge tunings per edge per vertex, holding to O((ma)²).
  - **With P62:** no common zero was found.
  - **Price P-Z:** a zigzag edge with longer-range hopping tails, and each tuning held to ~1e-13.
  - **Proposed corrections, if refereed:** S17's "T₂g never zeroed" and P63(i).

  Referee running.

### C5 Round 16, item 9 (pre-registered 23:10Z, before launch)

**R16-9. One law, every cone: can one subluminal edge family meet the photon, the electron and the graviton cones together, and the shear condition? What is the total bill?**
- **Plain question.** Round 16 so far gives:
  - one tuning per (spin, |q|) class for charged matter against the photon (R16-2, worker);
  - two edge tunings per edge for the graviton's E_g and T₂g on a zigzag edge (R16-3, worker);
  - one shape condition for the shear (R14-3; P62).

  These were each found on different edges. Do they fit on one law? Or do the conditions conflict? R16-3 finds no common zero with P62, and the zigzag raises μ_E.
- **Setting.**
  - One subluminal edge family per spin (Dirac D1/zigzag hybrids, and G(b)/zigzag for scalars), with |σ′| ≤ 1 and whole-zone v_max stated.
  - Peierls photon; R9-9's graviton vertex with the assumed W1; zero-point vacuum supplied.
  - One loop; m ≤ 0.3; light-mass limit.
  - Counterterms counted as in R16-2.
- **Prior art (count once):** R16-1, R16-2 and R16-3 (workers or referees as available), R14-3 (P62), R13-5, R13-8, S17's P61–P73.
- **Probes.**
  - (a) Within the stated family, find the minimal number of continuous knobs that zero, at a common light mass:
    - E_g and T₂g (both vertices, or state which);
    - μ_E;
    - the charged-matter Δ(0⁺) per class.

    Otherwise show that a pair of conditions is incompatible in the family (checked, with a scan).
  - (b) The total count of tunings for SM content, in R13-8's rows.
  - (c) The whole-zone v_max and the hopping tails of the resulting law.
  - (d) Prices.
- **FIXED readings.**
  - **JOINT:** an explicit law with every listed condition met at a common light mass to stated precision, checked, with the count.
  - **CONFLICT:** a demonstration, refereed if class-wide, that two listed conditions cannot both hold in the stated family.
  - **OPEN:** otherwise.
- **Expectation.** JOINT without P62 and with a count of about 5–6. CONFLICT or OPEN with P62.
- **R16-7 (strong-coupling TT stiffness): worker reading NOT-PRODUCED-EVIDENCE in 𝒬_E** (the vector Gauss law conserved exactly); **INCONCLUSIVE overall**. The method was pre-stated in `agents/C5_R16-7_method.md`: exact operator inequalities (f-sum, Bogoliubov, diamagnetic).
  - **Theorem B (proved).** In 𝒬_E (integer E: rotors or quantum links, qubits included; any penalty size or sign structure), m₁(E_TT) ≤ Ck⁴. So χ_TT ≥ 1/(Ck⁴) at every coupling, and the Einstein–Hilbert 1/k² is excluded non-perturbatively.
  - **Theorem D (proved).** A stoquastic H in the E basis with conserved scalar charge gives W(k) ≥ 0, so Newtonian attraction needs an E-basis sign problem.
  - **N0914's model is stoquastic,** so it is sign-free but L-type.
  - **Dual rotor:** Einstein–Hilbert static response is possible, but it forces z ≤ 2 modes.
  - **U(1) control:** k⁻² is reproduced as an identity, not as a phase measurement.
  - **What remains:**
    - microscopic violation of the vector Gauss law, with gauge structure emerging only under RG (P-r16-7a);
    - a sign problem or scalar-law violation (P-r16-7b);
    - small-N clocks.

  Referee running.

#### C5 Round 16 referee verdicts, items 1–5 (recorded 23:22Z; codex gpt-5.6-sol, xhigh)

- **R16-1 referee: CONFIRMED WITH CORRECTIONS. Reading DERIVED.**
  - **Correction:** the uniform heavy expansion closes with a ≥ λ/2 denominator bound for large m near p = 0.
  - **Statement.** At one loop, in Feynman gauge with Peierls coupling and fixed λ > 0: every box-exact Wilson law with nonnegative, nonzero W, an H2′ photon, and (H3) or (H3′) has δc_e = Lm + O(1) with L > 0, while the photon is O(m⁻²). So there is no interval zero.
  - **Covers:** D1 (0 < r ≤ 1/√3) at b = 1.4, 1.2 and 1.0, and the selectron-only P-a variant.
  - **Does not cover:** P-b, λ = 0, photon transitions on the Wilson edge, or the uniqueness of the zero near m ≈ 24.
  - **Effect:** this closes S17's gap that the DERIVED subclass was only the literal edge already excluded by the Z width.
- **R16-2 referee: CONFIRMED WITH CORRECTIONS. Reading OPEN.**
  - **Confirmed:** the q²F_s factorization; that the photon shift is independent of λ and of the internal photon symbol; the scalar runner; Lemma T′.
  - **Conditional:** the count of 7 per species or 3 per charge class depends on F_s(0⁺) ≠ 0 class-wide, uniform mass control, and the additive-counterterm conventions.
  - **Not proved:** class-wide F_s(0⁺) ≠ 0, the λ → 0 bound, the literal-corner accounting, convention-independent minimality.
  - **Correction:** κ_γ is replaceable, not required.
- **R16-3 referee: CONFIRMED WITH CORRECTIONS. Reading REFUTED** (universal T₂g negativity), within R9-9's prescription.
  - **Z1 confirmed independently:** Ξ_M = +3.9047e-4, Ξ_U = +2.8101e-4 at m = 0.3.
  - **Simultaneous zero:** a convex two-parameter mix gives a common E_g/T₂g zero for a chosen vertex.
  - **B″ proved:** strict negativity for every admissible weight when |σ′| ≤ 1/√5 on stretches incident to a positive valley.
  - **Not supplied from the axioms:** the Ward completion, the dressed matter pole, or the vacuum.
  - **Dated correction:** S17's "T₂g never zeroed" (`C5_S17_synthesis.md:95,179`) and P63(i)'s "T₂g not reached" are superseded within the prescription.
- **R16-4 referee: CONFIRMED WITH CORRECTIONS. Reading STATE-DEPENDENT** for 𝒢(1, 1/ℓ).
  - Free TT data keep their initial energy, which exceeds the listed ρ_Λ budget by 2.4e3 to 5.9e19.
  - **This is generic free-wave memory (as in GR), not a special mechanism of the E1 start.** The J₀ perturbation decays as t^{−1/2}.
  - **Consequence:** E1 must either record nonzero initial TT data or impose zero TT data (P-r16a). That makes the AX:94 privilege question consequential, but leaves it unresolved.
- **R16-5 referee: CONFIRMED WITH CORRECTIONS. Reading OPEN.**
  - **Confirmed:** for massive free single-band matter on T³, standard W2_pf has no physically nontrivial pair-stress completion: θ = 0, then g = 0. Pair terms cannot repair this because the identity separates by particle-number grade.
  - **Not established:**
    - the finite-band no-go;
    - the redshift (observational) exclusion.
  - **Live counter-routes:** C₂-exchanged bands, general 3D component mixing, singular or non-local generators.
  - **Consequences:**
    - no W2_pf-invariant pole split is available;
    - the TT one-loop matter part is gauge-parameter-free;
    - the matter pole is unprotected;
    - R13-5's numbers stay W1- and prescription-scoped.

### C5 Round 16, item 10 (pre-registered 23:24Z, before launch)

**R16-10. Close R16-2: prove F_s(0⁺) ≠ 0 class-wide, and the λ → 0 limit, so the tuning count becomes a theorem.**
- **Plain question.** R16-2 (refereed OPEN) gives 7 per species or 3 per charge class, but only if the light-mass speed shift per unit charge², F_s(0⁺), is nonzero on every allowed edge. The referee also asks for:
  - uniform mass control;
  - the physical λ → 0 bound;
  - convention-independent minimality;
  - and notes that κ_γ is replaceable.

  Can these be proved?
- **Setting.** R16-2's stated class:
  - non-rising matter symbols (S ≤ q for Dirac, u′/2 ≤ q for scalars);
  - nondecreasing photon symbol;
  - D1, literal and G(b) families plus their admissible deformations;
  - one loop, Peierls coupling, Feynman gauge.

  The counterterm conventions are fixed as in the R16-2 verdict.
- **Prior art (count once):** R16-2 and its verdict (Lemmas Q and T′; the leftover is ≤ 0.27 of the bound for Dirac and ≤ 0.73 for scalars), R13-7's Theorem Sgn, R16-1's Theorem W/K, R10-1.
- **Probes.**
  - (a) Bound the non-tadpole leftover by proof, so that F_s(0⁺) < 0 on the class, or find a law in the class with F_s(0⁺) = 0.
  - (b) λ → 0: prove that the limit exists uniformly, or exhibit a log.
  - (c) State minimality in a convention-independent form: a tuning is any continuous parameter of the law or counterterms.
  - (d) The literal-corner accounting.
- **FIXED readings.**
  - **COUNTED:** a refereed proof that F_s(0⁺) ≠ 0 on the class and that the count is minimal, with the n_t stated.
  - **REFUTED-ZERO:** an explicit law in the class with F_s(0⁺) = 0, checked.
  - **OPEN:** otherwise.
- **Expectation.** COUNTED for scalars (simpler), OPEN for Dirac.
- **R16-6 (non-signalling Λ): worker reading PASS, scoped.**
  - **The class:** readers whose zero is the late vacuum, supplied by the law. Members: IE (read the EoS once, then integrate) and G0.
  - **What IE gives:** g ≡ 0 and Λ̃_late = 0 through supercooling, inflation (65.2 e-folds), reheating, e⁺e⁻ annihilation, QCD and DESI. There is no signalling and no CMC clock.
  - **Theorem Z:** g ≡ 0 and Λ̃_late = 0 together hold if and only if R ≡ ρ_tot − ρ_v,late.
  - **Theorem NA:** landscape branching between late vacua is excluded.
  - **The worker's own caveat, which the referee must decide:** with g ≡ 0 the model is exactly GR with a fixed cosmological term of −V_late. That is Lemma PT's c-number subtraction, with the number supplied by the law's T = 0 normalization. Is that a tuning?
  - **Prices:**
    - P-r166a: the creation law's zero is the T = 0 vacuum. This is in tension with AX:94.
    - P-r166b: late-vacuum stability.
    - P-r166c: no late branching.
    - P-r166d: a first exact reading.
  - **Consequence:** DESI's phantom crossing would then have to be real dark energy.

  Referee running.

### C5 Round 16, item 11 (pre-registered 23:25Z, before launch)

**R16-11. Does R16-7's Theorem B survive an emergent Gauss law? The dressing transfer.**
- **Plain question.** R16-7 (worker; referee running) proves χ_TT ≥ 1/(Ck⁴) for every finite-slot model whose Hamiltonian conserves the vector Gauss law exactly. Spin ice gets its photon from qubits whose Hamiltonian does not conserve Gauss's law exactly; the law emerges at low energy. Suppose a microscopic finite-slot H violates the vector law but flows to a phase where the law is emergent. If the emergent phase is related to an exactly conserving model by a quasi-local unitary dressing (quasi-adiabatic continuation, Schrieffer–Wolff to all orders), does Theorem B transfer? If it does, the last finite-slot window (P-r16-7a) closes for every phase connected to a gapped-constraint limit.
- **Setting.**
  - Finite-slot (qubit or Z_N) H on Z³ with a tensor gauge structure:
    - H = U·Σ(vector-law penalty) + V, where V violates the law;
    - large but finite U;
    - phases adiabatically connected to U = ∞.
  - Quasi-local dressing W with Lieb–Robinson / quasi-adiabatic tails (stretched-exponential decay).
  - Observables: dressed E_TT and h_TT.
- **Prior art (count once):** R16-7 (Theorem B, Theorem D, N0914's moment lemma), R15-5 Lemma W (all finite SW orders O(k³)), its verdict, Hastings quasi-adiabatic continuation, Bravyi–Hastings–Michalakis, and Hermele–Fisher–Balents spin ice as the U(1) comparator where the photon does emerge.
- **Probes.**
  - (a) Does the f-sum bound m₁(Ẽ_TT) ≤ Ck⁴ hold for the dressed operator Ẽ = W†EW, with the dressing's tails accounted for (state which tail decay suffices)?
  - (b) Reconcile with spin ice: why does the U(1) photon emerge there? Its m₁ ~ k² is allowed. Is the tensor obstruction specifically the k⁴ moment structure, which dressing preserves?
  - (c) What remains: gapless intermediate phases, non-quasi-local dressing, first-order transitions out of the constrained limit.
  - (d) Prices.
- **FIXED readings.**
  - **TRANSFERS:** a proof, refereed if a no-go, that Theorem B's bound holds for dressed operators in every phase connected to the constrained limit by a quasi-local dressing with stated tails.
  - **FAILS-TO-TRANSFER:** an explicit dressing class or model where the dressed m₁ is O(k²), checked.
  - **OPEN:** otherwise.
- **Expectation.** TRANSFERS for stretched-exponential tails, since dressing cannot change the k-power of a conserved-charge moment. This would leave only phases not connected to the constrained limit.
- **R16-8 (W7 off-box tail): worker reading OPEN.**
  - **The tail:** B = s·D/|s|², falling as 1/r^{d−1}. Its gauge-invariant curvature falls as 1/r^{d+1} and is fixed by Bianchi. Its source is the defect charge Q_D, carried by edge quanta only.
  - **Lemmas P, S and F:**
    - the singular terms can be confined to the spatial-diffeomorphism constraint;
    - the tail is inert on box states;
    - it acts through a shell at infinity.
  - **Lemma A:** there is no local formulation with non-dynamical auxiliary fields unless the defect is static.
  - **Lemma D (suggested):** closing in time needs either (α) non-local dynamics or (β) a second singular momentum-constraint term. Deciding between them needs the degree-3 algebra.
  - **Relation to R16-5:** the same root as P-pf1, but a different object. Sawtooth (SLAC) matter pays W7 at degree 2.
  - **Prices:** P50 refined, P-W7α, P-W7aux.

  Referee running.

### C5 Round 16, item 12 (pre-registered 23:29Z, before launch)

**R16-12. W7's fork: does the degree-3 constraint algebra force non-local dynamics (α), or allow a quasi-local fix (β)?**
- **Plain question.** R16-8 (worker) reduces W7 to one fork. Keeping the momentum constraint true in time produces a non-local term κ³∫ξE·(B∗Ȯ_D). It must be cancelled either by:
  - **(α)** a non-local Hamiltonian-constraint term, so the dynamics acts at a distance at ~κ²|E||Q_D|/(8πr²) per edge quantum; or
  - **(β)** a second singular term inside the momentum constraint, so the dynamics stays quasi-local.

  Which one does the degree-3 algebra allow?
- **Setting.**
  - R12-1's completion with R16-8's Lemma-P placement (P = ∂(ε²/2)) and the R14-1 subluminal S(1.4) or G(1.4) box.
  - d = 3, linear in matter bilinears, through κ³. Standard (undeformed) algebra.
  - Excluded: pairing, the SLAC/P-pf1 matter.
- **Prior art (count once):** R16-8, R12-1 and its verdict, R13-4, R16-5's grading lemma (the identity splits by particle-number grade), RFW's first-jet obstruction.
- **Probes.**
  - (a) Write the degree-3 brackets {H,H}, {H,D} and {D,D} at O(κ³) with the completion. Find all terms carrying B.
  - (b) Try (β): is there a quasi-local-dynamics completion? Construct it, or prove it inconsistent in a stated class.
  - (c) If (α) is forced, exhibit a bounded gauge-invariant observable responding at a distance, which is the R13-4 criterion. State its size at a = ℓ_P for a realistic density of edge quanta (thermal at T_CMB, or a gas at a stated temperature).
  - (d) Prices.
- **FIXED readings.**
  - **QUASI-LOCAL (β):** a constructed degree-3 completion with quasi-local dynamics, checked through κ³.
  - **NON-LOCAL (α):** a refereed proof that (β) is inconsistent in a stated class, with the size of the distant response.
  - **OPEN:** otherwise.
- **Expectation.** NON-LOCAL in the class, with an effect suppressed by the edge-quanta population, which is negligible at low temperature. The physical verdict then depends on that population.
- **R16-9 (one law, every cone): worker reading CONFLICT**, needing a referee because it is class-wide; otherwise OPEN.
  - **Block split (proved):** the charge cones depend on the Dirac and photon edges and the counterterms; the graviton and shear conditions depend on the scalar edge only.
  - **The conflict:** over a provable superset of the subluminal scalar class (Lemmas R and R_U), the scans find no point with E_g/T₂g ≥ 0 and μ_E ≤ 0.
    - M vertex: smallest μ_E +1.25e-3.
    - U vertex: smallest μ_E +1.3e-4, a thin margin.
  - **So the shear needs a non-shape knob:** a counterterm, pairing, the Fock vacuum, or giving up subluminality.
  - **Counts:**
    - the listed conditions: 6 per class or 10 per species;
    - SM rows: 9 + CC per class or 13 + CC per species, against R13-8's 16 + CC.
  - **Biggest open item:** Dirac, photon and gluon zero-point loops have no TT or shear vertex yet, and could cancel μ_E.
  - **Prices:** P-R16-9a (P62 and P-Z cannot share one subluminal scalar edge); P-R16-9b (named gap).

  Referee running.
- **R16-10 (Lemma F and λ → 0): worker reading Dirac REFUTED-ZERO; scalar OPEN; COUNTED not met.**
  - **Theorem L (proved):** the λ → 0 limit exists jointly with m → 0 and has no log; F_s(0⁺) = K_s + Λ_s, with K_0 = −1/3 (closed form) and K_½ = +2/3 (checked).
  - **The Dirac zero:** D1(1.4, 1/√3) with a stiffened R8-5 photon (nondecreasing for G ≥ π/2) gives F_½(0⁺) = 0 at G* ≈ 3.126. The unmodified R13-7 runner converges toward it.
    - **Caveat:** the photon's whole-zone v_max is 7.35, i.e. superluminal at the grid scale. If that is outside the class, Dirac is OPEN.
  - **Subluminal photons:** proved tadpole ≤ −2.02; about 92 samples give F_½ ≤ −3.8.
  - **Scalars:** F_0 < −1/3 in every resolved sample.
  - **(c) Convention-independent minimum:** n_t = 2 (G* plus κ_γ) with a superluminal photon tuned to ~1e-15; 7/3 survives only on the subluminal-photon subclass.
  - **Price:** P-r16-10a.

  Referee running.

#### C5 Round 16 referee verdicts, items 6–8 (recorded 23:50Z; codex gpt-5.6-sol, xhigh)

- **R16-6 referee: NOT CONFIRMED (the PASS). Reading INCONCLUSIVE.**
  - **What holds.** g = (κ/3)(ρ_tot − R)′, so g ≡ 0 is exactly GR with one constant subtraction, R = ρ_tot − C. Choosing C = ρ_v,late avoids R15-1's signalling and reproduces the checked histories.
  - **Theorem NA holds:** no causal reader handles branches with unequal late vacua.
  - **Why it is not a PASS.** C = ρ_v,late is obtained only by stipulating the law's T = 0 gravitational zero, and IE imposes its integration constant exactly. Without a derived symmetry, constraint or mechanism, these are the same late-vacuum counterterm and precision cancellation as Lemma PT, i.e. a tuning.
  - **Why it is not a FAIL.** The tuned g ≡ 0 counterexample defeats the universal FAIL clause.
  - **Consequence:** the R15-1 signalling is not forced by inflation, but Λ removal without tuning and without signalling is not shown.
- **R16-7 referee: CONFIRMED WITH CORRECTIONS. Reading INCONCLUSIVE.** The narrower NOT-PRODUCED-EVIDENCE is not permitted, because the physical U(1) control did not pass.
  - **Theorem B holds after correction.** With consistent V^{−1/2} normalization, the TT-electric f-sum is O(k⁴) for quasi-local rotor or quantum-link H with an exact integer vector Gauss law. So the normalized probes obey the Bogoliubov bound, and a nonvanishing TT-electric susceptibility forces an E_TT-connected excitation with ω ≤ Ck².
  - **What it does not do:** it does not identify the optimized probe ratio with the physical metric susceptibility.
  - **Theorem D holds in Hessian/PSD form.**
  - **Not reached:** the non-lifted, microscopically constraint-violating N-type at U ~ J ~ g.
- **R16-8 referee: CONFIRMED WITH CORRECTIONS. Reading OPEN.**
  - **The tail.** The 1/r² kernel and the Bianchi-fixed non-TT 1/r⁴ linear curvature tail are confirmed, as is the box-inertness under a smooth placement.
  - **Not physical non-locality.** The curvature transforms under the completed momentum constraint. No closed degree-3 system or invariant physical domain exists, and no bounded gauge-invariant instantaneous responder has been built.
  - **Lemma A and the (α)/(β) fork do not close.**
  - **P-pf1** shares the zone-mean root but relocates the cost to a discontinuous 1/n matter generator.

### C5 Round 16, item 13 (pre-registered 23:53Z, before launch)

**R16-13. Fermion and photon zero-point loops in the graviton cone and the shear: does their sign lift R16-9's conflict?**
- **Plain question.** R16-9 (worker, CONFLICT pending referee) finds that on one subluminal scalar edge the graviton-cone zero always leaves μ_E > 0. Its biggest open item is that no TT or shear vertex exists for Dirac, photon or gluon loops. Fermion zero-point energy has the opposite sign to the boson one. With a TT vertex written for Dirac matter on D1 or zigzag Dirac edges, does the fermion contribution to Ξ (E_g, T₂g) and μ_E have the opposite sign? Can it cancel the scalar's μ_E at the graviton-cone zero without pairing?
- **Setting.**
  - The R9-9 / R13-5 vertex prescription extended to Dirac fermions: the Belinfante-symmetrized lattice stress with the assumed W1 completion. State it explicitly and stipulate where needed.
  - D1(1.4, r) and subluminal zigzag Dirac edges. The photon is optional (Peierls Maxwell stress on the R14-1 photon edge).
  - Zero-point vacuum supplied, one loop, m ≤ 0.3.
  - Excluded: exact pairing (P46). That is the comparison, not the target.
- **Prior art (count once):** R16-9, R16-3 (Z1, IBP identity), R14-3 (μ_E, Theorem B), R13-5 (stipulated vertex, Lemma B2, pairing gives 2κm²J₂), R11-1 (N*: pairing necessary for untuned cancellation), R9-9.
- **Probes.**
  - (a) Write the Dirac TT and shear vertex and its IBP identity, analogous to R16-3's Ξ = (1/32)⟨|V|²(5v_z² − 1)/ε⁵⟩.
  - (b) Compute the signs and sizes of Ξ_E_g, Ξ_T2g and μ_E for D1 and zigzag Dirac edges.
  - (c) For SM-like content (scalar edge plus N_f Dirac edges, with or without the photon), find the knob count that zeroes E_g, T₂g and μ_E together, or show the conflict persists.
  - (d) Relate the result to R11-1's N*. Does an untuned cancellation re-enter by the back door?
  - (e) Prices.
- **FIXED readings.**
  - **LIFTED:** an explicit mixed-species content, all edges subluminal, with E_g = T₂g = μ_E = 0 at a common light mass, checked, with the count.
  - **PERSISTS:** a demonstration (refereed if class-wide) that the fermion and photon loops cannot cancel μ_E at the graviton-cone zero in the stated class.
  - **OPEN:** otherwise.
- **Expectation.** Fermion μ_E has the opposite sign, so the conflict is LIFTED with one more tuning (the species ratio is not a knob, so an edge parameter is needed).
- **R16-11 (dressing transfer): worker reading TRANSFERS** (a no-go, so it needs the referee).
  - **Theorem B′.** Assume a quasi-local unitary dressing of the ground state into the exact vector-law sector, with dressed H second moments finite (tails Σr¹³Φ < ∞). Then m₁(Ẽ_TT) ≤ 2S²K₂k⁴ for any penalty U and any law-violating V. A floor version covers approximate dressings.
  - **Corollary B-inv.** The local gauge-invariant curvature readout has its susceptibility bounded below by a constant. This excludes Einstein–Hilbert for any local invariant readout with a nonzero vertex, and narrows R16-7's gap 1.
  - **Spin ice is consistent:** for U(1) only 6 of 9 linear fields are pure gauge, against 18 of 18 for the tensor, so Maxwell is allowed.
  - **The smallest exactly invariant qubit hop flips 20 slots.**
  - **What remains:**
    - non-dressable phases (criticality, first-order transitions, U ~ J);
    - mod-N clocks and rotors;
    - non-local or zero-vertex readouts;
    - the scalar channel.
  - **Prices:** P-r16-11a, b and c.

  Referee running.

### C5 Round 16, item 14 (pre-registered 23:55Z, before launch)

**R16-14. Set A: close the noise-fed PPN test for E1 and E2.**
- **Plain question.** Both covariant exits of set A are OPEN and tied (R14-2). R15-2 and R16-4 refine E1. The PPN test has been "unclosed" on both routes since R12-7, and R13-6 and R16-4 give power counting only. Two things are in question:
  - the second-order, noise-fed corrections to the post-Newtonian metric;
  - the preferred-frame parameters α₁ and α₂, since both routes live in the CMB frame.

  Do they pass Solar System and binary-pulsar bounds (RECALLED values labelled), and does either route lose?
- **Setting.**
  - **E1:** R13-6's repaired gain (P-r13b) with R15-2's refereed channel split and the TT weight ¼, plus the R16-4 initial datum h_TT = 0.
  - **E2:** R12-7's friction on all of h̄ with γ in the drag-allowed range 0.016–0.047 H₀ (R14-2).
  - Both on a Minkowski background in the CMB frame, with v_⊙ ≈ 370 km/s.
  - Order: O(G²) and O(noise²), with every subtraction named.
- **Prior art (count once):** R12-7 and its verdict, R13-6, R14-2, R15-2, R16-4, R11-5, R6-4 (Newtonian VIABLE), Will's PPN bounds (RECALLED), and Foster–Jacobson α₁/α₂ for khronometric theories (comparator).
- **Probes.**
  - (a) α₁, α₂ and the γ_PPN, β_PPN shifts for each route, with constants.
  - (b) The noise-fed stochastic metric's contribution to perihelion advance and to timing residuals.
  - (c) Compare against the bounds: |α₁| ≲ 1e-5, |α₂| ≲ 2e-9 (RECALLED), and |γ−1| ≲ 2.3e-5 (Cassini, RECALLED).
  - (d) Prices, and whether the tie breaks.
- **FIXED readings.**
  - **PASS (a route):** every listed PPN quantity is computed with constants, below its bound across the route's allowed parameter window. Checked.
  - **EXCLUDED (a route):** a refereed demonstration that some listed quantity exceeds its bound over the whole allowed window.
  - **OPEN:** otherwise.
- **Expectation.**
  - α₁ and α₂ vanish at linear order for both routes, which are instantaneous and Newtonian at zero frequency, and are suppressed at second order.
  - Both PASS. The likeliest failure is α₂ for E2's frame-tied friction.
- **R16-12 (W7 at degree 3): worker reading OPEN.** All results are at leading order in the Killing sector of class 𝒞.
  - **Theorem T3, translation sector.** (β) works: an h-linear singular momentum-constraint term cancels R16-8's term, with its helicity-0 condition fixed by the W1 stress. Lemma J3: this is the JJ repair.
    - Closure is weak only, with 1/r² structure functions.
    - Lemma C: every defect-carrying mode must be subluminal. S/G pass and L-box fails.
  - **Lemma W.** Φ_c = {P⁰_c, W}, so whether a term counts as (α) or (β) depends on the variables chosen.
  - **Theorem B3, boost sector (no-go in 𝒞).** The standard {K, H} = P^tot forces a world-line Coulomb kernel X_T ∝ 1/(q·v), which is unbounded. So (β) fails in 𝒞.
  - **Escapes outside 𝒞:** a non-local H, boost world-line kernels, degree-4 shells, canonical relocations, auxiliary fields.
  - **Population.** Defect quanta carry ≥ 1.7e19 GeV, so their thermal occupation is negligible below ~1e19 GeV.
  - **Prices:** P-W7K, P-W7sf, P-W7v.

  Referee running.

#### C5 Round 16 referee verdict, item 9 (recorded 00:07Z; codex gpt-5.6-sol, xhigh)

- **R16-9 referee: NOT CONFIRMED (the CONFLICT). Reading OPEN** (`agents/C5_R16-9_referee_verdict.md`, full record `agents/C5_R16-9_referee.md`).
  - **Confirmed:**
    - Lemma R, as a continuous relaxation at fixed exact parameters;
    - Lemma R_U's necessary inequalities;
    - the fast-state identity;
    - the tadpole monotonicity;
    - one M cell, independently: μ_E = +1.255274e-3.
  - **Why it is not a CONFLICT:**
    - the scanned grids are not proved supersets;
    - local optima are only upper bounds;
    - the parameters were sampled, not exhausted;
    - the thin U margin needs a certified enclosure.
  - **Scope of the remaining claims:**
    - The block split holds only for the truncated scalar-loop prescription.
    - The 9/13 + CC bill is conditional bookkeeping, not an established minimal bill, and μ_T2 = 0 is coupling-specific.
  - **Referee's summary:** credible search evidence for tension.

### C5 Round 17 (pre-registered 00:07Z from S20 §7 (agents/C5_S20_synthesis.md), text fixed before any run; R17-1, R17-3, R17-4 launched now; R17-2 after R16-12's referee; R17-5 if time allows)


**Rules (as rounds 2–16).**
- Probes run on Opus 5.5 at xhigh. Every FAIL, EXCLUDED or no-go goes to codex gpt-5.6-sol (xhigh) before it is recorded.
- Prices are named, never adopted.
- Each probe greps the repository and packet for prior art first and counts each match once.
- Hypotheses come before titles, and excluded outside realizations are listed. Numbers from memory are labelled RECALLED.
- Every tail or decay clause names its subtraction before any run. A PRODUCED or PASS clause names the perturbative order of each exactness condition.
- **Round-16 head rules (`TESTS:5039`):**
  - every law states its whole-zone v_max;
  - every frame-tied kernel states its self-force on a moving compact body;
  - every Ward requirement says standard or deformed.
- **New rules (from round-16 verdicts):**
  - **Gauge fields too.** The v_max rule applies to photon, gluon and graviton symbols, not only matter (R16-10's v_max 7.35 photon).
  - **Counting conventions.** Every tuning count states its counterterm basis: per species, per (spin, |q|) class, or q²-correlated (`vR16-2:13`).
  - **Enforced or stipulated.** Every Λ mechanism states whether any number it needs is enforced (by a symmetry, constraint or theorem) or stipulated, and checks radiative stability (`vR16-6:26`).
  - **Physical controls.** A "control" must measure the same physical observable in a model known to have the target phase. An operator identity is not a control (`vR16-7:13`).
  - **Readout bridges.** Every finite-slot susceptibility or stiffness claim names its readout (observable) bridge (`vR16-7:5`; `AX:85-90`).
  - **Forks.** Every dichotomy offered as exhaustive lists the alternatives it excludes and why (`vR16-8:9`).
  - **Generic GR comparison.** Every initial-state or memory claim says whether the effect is generic GR behaviour or specific to the model (`vR16-4:13`).
  - **Changed hypotheses.** Every expectation names which hypothesis of the governing prior no-go the new setting removes (§6).

**Overlap check.**
- R16-13 covers fermion/photon TT and shear vertices; no R17 item repeats it.
- R16-14 covers set A's noise-fed PPN; no R17 item is on set A.
- R16-11 covers quasi-local dressing; R17-1 covers only small-N clocks and readouts, which R16-11 leaves open (`C5_R16-11_report.md:288,290`).
- R16-12 covers the (α)/(β) fork in class 𝒞. R17-2 covers the boost-sector escapes it leaves undecided (`C5_R16-12_report.md:263-276`) and the constraint-invariant observables.
- R16-10 covers Lemma F; R17-4 covers only the three uncomputed bill rows and R16-9's missing enclosure.

**Priority.**
1. R17-1 (graviton, axiom-level) and R17-3 (Λ), in parallel.
2. R17-4 (bill rows, owner Q3). Its probe (f) only if R16-13 does not return LIFTED.
3. R17-2 (W7), preferably after R16-12's referee.
4. R17-5 (W15) only if time allows.

---

**R17-1. Literal qubits: does the k⁴ obstruction survive on Z₂ and Z₃ clocks, where integer lifting fails?**

- **Plain question.** R16-7 (refereed) proves that finite slots with an exact *integer* vector Gauss law cannot give Einstein–Hilbert TT stiffness through the electric f-sum. R16-11 (worker) extends this to every phase reachable by a quasi-local dressing. Both leave out mod-N clocks at small N. There "divergence-free" holds only mod N, so the moment lemma's integer lift fails. The axioms' one-site algebra is M₂(C), so a qubit metric slot in the Weyl presentation is a Z₂ clock. Is the qubit case inside the obstruction, or is it the window?
- **Setting.**
  - Z_N clock tensor model on Z³ (N0914's slot positions and stencil), N ∈ {2, 3, 4}.
  - Exact mod-N vector Gauss law, plus any local Hamiltonian, bounded below and quasi-local.
  - Probes: TT-component clock operators (state the operator used for E_TT at N = 2, e.g. the Hermitian part of the clock Z^{ε}) and gauge-invariant curvature probes (R16-11's B-inv form).
  - A stated readout bridge for "metric susceptibility".
  - Excluded: rotors; integer-law QLMs (R16-7, R16-11 cover them); non-local hops.
- **Prior art (count once).** R16-7 and its verdict (`vR16-7:5-7`; `C5_R16-7_report.md:224-230`, its suggested §8 on mod-N); R16-11 Lemma S (`C5_R16-11_report.md:94-135,288`); N0914's moment lemma and lifting bound (`N0914:109-129,218-250`); R15-5 Lemma W's N > 36nM (`vR15-5:33`); X-cube/Z_N rank-2 fracton literature (comparator, RECALLED: gapped at large penalty).
- **Hypothesis that changes from the prior no-go.** Integer lifting (removed). Kept: finite slots, exact law, quasi-locality.
- **Probes.**
  - (a) Enumerate the minimal gauge-invariant hops at N = 2, 3, 4 up to a stated support size. For each, compute its zeroth and first moments as integers of a minimal lift. Identify every invariant hop with no lift of vanishing moments.
  - (b) Compute m₁(k) for the TT probe with those hops present. Is it still ≤ Ck⁴, or does a k² or k⁰ term appear? Give exact symbols.
  - (c) If the bound fails, state what the failure buys. A k⁰ f-sum gives no exclusion and no production; say which. Check one explicit qubit model's static TT response by exact diagonalization on the largest feasible cluster, labelled with its size limit.
  - (d) The readout bridge: which record-readable quantity is "the metric" at N = 2 (`AX:82-83`)?
  - (e) Physical control: the 3D Z₂ vector gauge theory (toric code). The method must not report a gapless photon there (comparator, RECALLED: gapped deconfined phase).
  - (f) Prices.
- **FIXED readings.**
  - **EXTENDS:** a refereed proof that m₁(E_TT) ≤ Ck⁴ (or the B-inv curvature bound) holds at N = 2 (and stated N) in the stated class, with the readout bridge named.
  - **WINDOW:** an explicit qubit (N = 2) model in the class with an invariant hop giving m₁ ≥ ck² (or k⁰) for the TT probe, checked. This is a window, not a production claim.
  - **OPEN:** otherwise.
- **Expectation.** WINDOW at the f-sum level. At N = 2 every shift is its own inverse, so invariant patterns need not lift to moment-free integer patterns. But no gapless TT phase follows from that, and every known Z₂ tensor phase is gapped (comparator). If so, the obstruction moves from "the f-sum" to "whether any gapless Z₂ tensor phase exists", which no method here decides.

---

**R17-2. W7 in the boost bracket: does any escape outside class 𝒞 close degree 3, and is anything physical left?** *(Preferably launched after R16-12's referee. The readings are fixed now.)*

- **Plain question.** R16-8 (refereed OPEN) gives the off-box tail as a 1/r² kernel with a 1/r⁴ curvature, inert on box states but not shown physical or harmless. R16-12 (worker OPEN) finds three things:
  - the translation part is repaired by (β), with weak closure only;
  - the boost bracket {H[x_b], H[1]} = D[e_b] forces a world-line Coulomb kernel X_T ∝ 1/(q·v), unbounded on q ⊥ v. So in class 𝒞 (homogeneous kernels bounded on the sphere) there is no quasi-local completion;
  - by Lemma W, whether this reads as "(α) non-local" or "(β) quasi-local" depends on the canonical variables. Only constraint-invariant observables can decide.

  Two questions remain: does an escape outside 𝒞 close the boost bracket with quasi-local dynamics, and does any constraint-invariant observable respond at a distance?
- **Setting.**
  - R12-1's completion with R16-8's Lemma-P placement and R16-12's Theorem T3 translation repair.
  - The R14-1 S(1.4) or G(1.4) box (whole-zone v_max 0.99270 or 0.99386; R16-12's Lemma C needs |v| < 1).
  - d = 3; linear in matter bilinears; through κ³, plus degree-4 shell terms where an escape needs them.
  - Standard hypersurface algebra, unless the deformation is the escape under test, in which case it is stated (standard or deformed, per rule).
  - Excluded: pairing; P90 matter; nonlinear gravity beyond the stated degree.
- **Prior art (count once).**
  - R16-8 and its verdict (`vR16-8:5-17`);
  - R16-12 and its referee when back (`C5_R16-12_report.md:230-313`; Theorem B3, Lemma W, escapes 1–7 at `:263-276`);
  - R12-1 and its verdict; R13-4's criterion (`vR13-4:18`);
  - R16-5's grading lemma (`vR16-5:19`), which already excludes pair channels;
  - SUMMARY §17's boost wall;
  - RFW F2's first-jet obstruction;
  - the hypersurface-deformation literature with field-dependent structure functions (comparator, RECALLED).
- **Hypothesis that changes from the prior no-go.** Theorem B3 assumes homogeneous kernels bounded on the sphere and a fixed presentation. This item allows world-line (non-homogeneous) boost kernels, degree-4 shell terms, constrained auxiliaries (`vR16-8:7`) and canonical relocations.
- **Probes.**
  - (a) Escapes 2, 3 and 5 of `C5_R16-12_report.md:269-274`. For each, close {P_c, K_b} = δ_bc H and {K_a, K_b} = J at degree 3, or prove inconsistency in a stated class.
  - (b) For any closed system, build at least one bounded observable invariant under the completed constraints, at distance r from a defect-carrying quantum. Test R13-4's criterion: an instantaneous response, and its r-dependence.
  - (c) If a response exists, state its size at a = ℓ_P per edge quantum and for thermal populations at T_CMB and 1e16 GeV, with the subtraction named. R16-12's ≥ 1.41/a quantum energy is the input.
  - (d) Settle Lemma W's question: is the non-locality removable by a canonical map on the physical (invariant) domain, or only relocated?
  - (e) Prices.
- **FIXED readings.**
  - **LOCAL-EQUIVALENT:** a closed degree-3 completion with an invariant physical domain on which no bounded invariant observable responds outside the light cone, checked through the stated degree.
  - **PHYSICALLY NON-LOCAL:** a refereed demonstration of a bounded constraint-invariant observable responding instantaneously through the tail, in a class containing escapes 2, 3 and 5, with its size.
  - **OPEN:** otherwise.
- **Expectation.** PHYSICALLY NON-LOCAL in principle and unobservable in practice, or OPEN. Theorem B3's kernel is the Coulomb field along the defect's world-line, which is the hallmark of a constraint carrying non-local charge (as in Coulomb-gauge QED). Its invariant content is likely real but tied to Planckian edge quanta, whose thermal occupation is 10^(−3.3e31) at T_CMB. The likeliest failure is that no invariant observable can be built at this degree, which would give OPEN.

---

**R17-3. Λ after R16-6: can anything in the four axioms force the gravitating zero, or is it necessarily a tuning?**

- **Plain question.** R16-6 (refereed INCONCLUSIVE) shows that the only non-signalling route is GR with one constant: the law's late (T = 0) vacuum. Choosing that constant is Lemma PT's counterterm unless something forces it. Theorem NA suggests why a causal law cannot do better [S20 reading]: it cannot know the final vacuum before reaching it, so that energy must be a law constant. Three candidates might force it:
  - (i) **Record sourcing.** "Only records are readable; a site with no record cannot be read" (`AX:82-83`). Read as a source bridge, gravity sees only recorded content, so the unrecorded ground state never weighs.
  - (ii) **A global constraint** that fixes the constant from the whole history's average (sequestering-type; RECALLED).
  - (iii) **The vacuum-shift symmetry** ρ_v → ρ_v + C, λ → λ − κC of R14-5 (`vR14-5:29-35`), extended to the creation law.

  Does any of these force C = ρ_v,late without a tuned number, keep inflation, and stay causal?
- **Setting.**
  - R16-6's homogeneous equations (Theorem Z, `vR16-6:5-14`), plus the R15-1 linear k ≠ 0 sector for causality.
  - Histories: SM crossovers, supercooling control, m²φ² inflation + reheating (65 e-folds), DESI-like CPL, as in R16-6.
  - Radiative stability: one-loop SM shifts of ρ_v,late (RECALLED sizes).
  - The source bridge for (i) is stated as a hypothesis on `AX:187`, not as axiom content. The owner's "records are mass" picture is a thought, not a rule (`owner-readings-are-thoughts`); it is tested here as a hypothesis.
  - Excluded: active compensation (R15-1 covers it); readers in 𝓡⁺ (R15-4 covers them).
- **Prior art (count once).** R16-6 and its verdict; R5-3 Lemma PT (`TESTS:2985-2988`); R14-5 vacuum-shift symmetry (`vR14-5:29-35`); R15-1 Lemma V and the (d-i)/(d-ii) bridge (`vR15-1:15`); R10-4 q-charge (`TESTS` R10-4 entry); R11-3 (grid zero-point w ≥ 0); the stadium/records-are-mass thread (owner thought; memory); sequestering (comparator, RECALLED).
- **Hypothesis that changes from the prior no-go.** R16-6 stipulated C. Here C must follow from a stated law structure.
- **Probes.**
  - (a) Under (i), what gravitates during inflation? Is a homogeneous false vacuum "recorded"? If it is, why is the late vacuum not? If it is not, does inflation fail (R16-6 §4.2)?
  - (b) Under (ii), state the global constraint, check that it fixes C = ρ_v,late, and test causality: does a late vacuum change alter early-time gravity?
  - (c) Under (iii), find whether the symmetry plus any creation-law structure selects C, or leaves it a free datum (`vR14-5:35`).
  - (d) Radiative stability of whichever mechanism survives (a)–(c).
  - (e) Prices.
- **FIXED readings.**
  - **ENFORCED:** a stated law structure, in class (i), (ii) or (iii), that forces C = ρ_v,late with no independent number, keeps 60+ e-folds of inflation, has no R15-1-type signalling, and is radiatively stable, checked.
  - **TUNING:** a refereed proof that in a stated class containing (i)–(iii), every law with g ≡ 0 and Λ̃_late = 0 needs an independent exact number, or an acausal (final-state) input.
  - **OPEN:** otherwise.
- **Expectation.** TUNING for (i) and (iii). Under (i), inflation needs the false vacuum to gravitate; any rule that lets it, but not the true vacuum, must single out the true vacuum's energy, which is the counterterm again. (ii) can force C only with a whole-history (final-state) input, which is the acausal price. The likeliest outcome is a refereed "tuning or acausal" theorem. This would turn owner Q1(b) into a plain choice between a tuning and a final-state law.

---

**R17-4. The cone bill's three uncomputed rows (off-axis graviton speeds, LV tadpole), and a certified answer for the shear row.**

- **Plain question.** R16-9's bill is 9 + CC (per class) or 13 + CC (per species). The referee confirmed the arithmetic but called it conditional bookkeeping (`vR16-9:19`). Three of its rows were never computed:
  - the two off-axis TT speed anisotropies (R16-3 zeroed only the axis speeds);
  - the LV tadpole.

  Do the zigzag laws that zero E_g and T₂g on the axis also zero the off-axis speeds? Or does each cost a further edge shape, with longer tails? Is the tadpole a separate tuning?
- **Setting.**
  - R13-8's P,T-even degree-2 TT basis (graviton speed + 3 anisotropies; `vR13-8:15-18`).
  - R9-9's M and U vertices extended to q along a face diagonal and a body diagonal. State the extension and the assumed standard W1.
  - Scalar edges in 𝒮: R16-3's checked zero law and R16-9's M-best/U-best laws, with v_max and raw tails stated. Masses m = 0.1 and 0.01. Supplied zero-point vacuum.
  - Excluded: Dirac/photon/gluon vertices (R16-13); pairing; deformed W2 (R16-5).
- **Prior art (count once).** R16-3 and its verdict (Z1, IBP identity Ξ = (1/32)⟨|V|²(5v_z² − 1)/ε⁵⟩, `C5_R16-3_report.md`); R16-9 and its verdict (`C5_R16-9_report.md:216-235`; Lemma R and R_U and the fast-state identity confirmed in continuous form, `vR16-9:5-11`); R13-8 (`vR13-8:11-22`); R9-9 Theorem T; R14-3 analyticity in m² (`vR14-3:18`).
- **Hypothesis that changes from the prior no-go.** R16-3 restricted q to an axis. Here q is off-axis.
- **Probes.**
  - (a) The off-axis generalization of the IBP identity, giving the four degree-2 TT speed parameters in closed form.
  - (b) Evaluate them on the axis-zero laws. Count how many further shape conditions are needed, and find one law with all four zero at a common light mass, or show that two conditions conflict in the family. A conflict needs a certified enclosure, since R16-9's scans did not meet that clause (`vR16-9:9`).
  - (c) The LV tadpole row on the same laws: is it a separate condition, or fixed by the others?
  - (d) The resulting v_max and raw tails.
  - (e) The total in R13-8's rows.
  - (f) *Only if R16-13 does not return LIFTED.* A certified answer to R16-9's shear row. Run an outward-rounded, interval-enclosed version of Lemma R_U's continuous relaxation, covering continuous b, lo, hi, s_min and m ∈ [0.01, 0.1], first for the U vertex, whose margin is thinner. It should either prove μ_E > 0 at every graviton-cone zero in 𝒮, or return a certified feasible point with μ_E ≤ 0 (`vR16-9:5-9`).
- **FIXED readings.**
  - **COUNTED-ROWS:** an explicit law with every TT speed parameter and the tadpole zero at a common light mass, checked, with the number of shape conditions. Or a proof that some rows vanish identically given the axis zeros.
  - **For (f) separately: CERTIFIED-CONFLICT** (an enclosure proof, refereed) **or JOINT** (a certified law with Ξ_Eg = Ξ_T2g = μ_E = 0).
  - **CONFLICT:** a demonstration, refereed if class-wide, that the off-axis rows cannot be zeroed together with the axis rows in 𝒮.
  - **OPEN:** otherwise.
- **Expectation.**
  - COUNTED-ROWS with two further shape conditions. That would confirm 9 + CC per class as a count, with tails growing beyond R16-3's 3.67e-5 at r = 128.
  - The main alternative is a CONFLICT inside separable 𝒮, since off-axis zeros need more zigzag structure than a single-axis separable law may have. That would push the off-axis rows to non-separable laws.
  - For (f): CERTIFIED-CONFLICT for M. The U vertex is likelier to yield a JOINT point if one exists, because its margin is ~10× thinner.

---

**R17-5. GW170817 on the grid, second attempt: a multi-band W2_pf completion.** *(Launch only if time allows.)*

- **Plain question.** R16-5 (refereed OPEN) proves that single-band matter admits no nontrivial pair stress under the preferred-frame second-order identity. The referee exhibited a six-band signed-axis construction (Π_j = diag(v_j), v ∈ {±e_x, ±e_y, ±e_z}) that satisfies the zeroth moment with θ = 0 (`vR16-5:13`). Can it, or a C₂-exchanged band family, be completed into full W2_pf matter whose momentum generator carries physical (redshifting) momentum? If so, what is the gauge-invariant graviton–matter pole split?
- **Setting.**
  - Six-band and C₂-exchanged band families with proper cubic covariance; continuous quasi-local kernels; finite pair channels; projectable lapse.
  - R9-9's N-type graviton.
  - The redshift test needs a stated source/observable bridge (`vR16-5:19`).
  - Excluded: single-band (covered), discontinuous symbols (P90), tower matter (P64).
- **Prior art (count once).** R16-5 and its verdict (`vR16-5:5-25`); R13-5 (`vR13-5:7,13`); R16-8's relation of P-pf1 to W7 (`vR16-8:13`); RN L3 (projectable Hořava); RFW F1.
- **Hypothesis that changes from the prior no-go.** Single-band (removed). Kept: continuity, quasi-locality, multiplier-generated shifts.
- **Probes.**
  - (a) Complete the six-band construction to a W2_pf-complete stress, or prove none exists in a stated multi-band class.
  - (b) Does its P_j generate physical translations? Test whether a homogeneous strain shifts its one-particle energies (the redshift bridge, stated).
  - (c) If (a) and (b) succeed, compute c_m − c_T for both polarizations, gauge-invariant, at a = ℓ_P.
  - (d) Prices.
- **FIXED readings.**
  - **SPLIT-PRESENT / SPLIT-ABSENT:** as R16-5 (`TESTS:5145-5148`), with a W2_pf-complete multi-band stress that passes (b).
  - **EXCLUDED-MB:** a refereed no-go for W2_pf-complete stresses with physical momentum in a stated multi-band class containing the six-band and C₂-exchanged families.
  - **OPEN:** otherwise.
- **Expectation.** EXCLUDED-MB or OPEN. The signed-axis Π_j has k-independent spectra, so it labels bands rather than carrying kinetic momentum. It is likely to fail (b) for the same reason T_pf forces g ≡ 0. A physical multi-band completion would be the first gauge-invariant GW170817 test on a grid and would change W15.

---


#### C5 Round 16/17 worker readings (recorded as they arrive)

- **R16-14 (set A PPN): worker reading OPEN for bare E1/E2; PASS for both with completion N; literal linear class EXCLUDED.** A referee is required.
  - **α₁, α₂ and γ** are fixed at O(G): α₁ = α₂ = 0 and γ = 1 exactly in PPN form for both routes. The non-PPN terms pass by at least 3.5 decades; the tightest is the gain's α̂₂,eff = 6.9e-13 against the 2e-9 bound. E2's frame dipole exerts no α₂ torque.
  - **Lemma L:**
    - a metric linear in matter records, with geodesic matter, gives β = 0, so Mercury is 57.5″/cy;
    - R13-6's literal ½hT coupling gives β = ½, so Mercury is 50.3″/cy;
    - both fail by ≥ 3.4 decades.
  - **Completion N** (the record source is gravity's total stress-energy) gives β = 1. It suggests the noise's field energy must gravitate, which makes premise (iii) non-optional.
  - **Noise-fed terms** are negligible.
  - **The tie holds:** both routes need N.
  - **New price:** P-r16-14a (completion N). Owner choice: N, or the mean-field alternative, which conflicts with AX:82-83.

  Referee running.

#### C5 Round 16 referee verdicts, items 10–12 (recorded 00:19Z; codex gpt-5.6-sol, xhigh)

- **R16-10 referee: CONFIRMED WITH CORRECTIONS. Reading: Dirac REFUTED-ZERO under the literal registered class; scalar OPEN; COUNTED not met.**
  - **Theorem L is confirmed** for the named box-exact families with integrable valleys. It gives a finite, path-independent (m, λ) → (0, 0) limit with K_0 = −1/3 and K_½ = 2/3, and no divergent IR log. λ = 0 is understood as a boundary value, and vanishing corrections such as m² log m are not excluded.
  - **The Dirac zero.** The stiffened R8-5 photon gives a checked Dirac zero near G = 3.1264. If admissibility also requires a whole-zone subluminal photon, that witness is excluded and Dirac is OPEN.
  - **The two-condition SM construction** is a checked upper bound, not a minimality theorem.
- **R16-11 referee: CONFIRMED WITH CORRECTIONS. Reading TRANSFERS.**
  - **The statement.** Take a volume-uniform quasi-local unitary that maps the chosen ground state into an exact Gauss sector, with the transformed H having finite K₂ (Σr¹³Φ < ∞ suffices for finite-range bounded-density H). Then the dressed, V^{−1/2}-normalized TT-electric m₁ ≤ 2S²K₂k⁴. The Bogoliubov bound and the ω ≤ Ck² corollary follow.
  - **Overstated:**
    - the curvature consequence. A local invariant probe with a nonzero vertex has an O(1) lower bound on its total susceptibility, but that is not identified with physical curvature, and it does not exclude an Einstein–Hilbert IR pole without a readout and spectral-isolation bridge;
    - the approximate floor;
    - the global 20-slot minimum. An 8³ MILP also gives 20.
- **R16-12 referee: CONFIRMED WITH CORRECTIONS. Reading OPEN.**
  - **Confirmed:** T3 and J3 at leading order in the weak Killing sector, and the S/G Cherenkov avoidance.
  - **B3 is narrowed.** Under the standard HDA, within the linear-bilinear bounded-angular ansatz, X_T ∝ 1/(q·v) is forced. This is only a presentation-dependent obstruction.
    - The translation closure is weak or deformed.
    - The full degree-3 and boost brackets are unbuilt.
    - Strict subluminality is not necessary at the luminal boundary.
    - There is no bounded Dirac observable with an instantaneous distant response.
- **R17-3 (Λ enforced or tuning?): worker reading TUNING.** The referee must decide whether (S) counts as an "independent exact number"; if it does not, the reading is OPEN.
  - **Theorem T (trichotomy), in 𝒦** (g ≡ 0, Λ̃_late = 0, H-blind, H-an). C = ρ_v,late needs exactly one of:
    - **(A)** final-state input;
    - **(N)** an independent exact number, which is radiatively unstable (one-loop terms 1.7e31 to 6.7e53 ρ_Λ);
    - **(S)** the number-free rule "the law's lowest state weighs nothing" (= P92). It is stipulated, and stable except when the ordering of minima flips.
  - **Lemma U:** (S) is exactly the shift-covariant, nonnegative-weight reference.
  - **Nothing in the four texts enforces (S):** they name no Hamiltonian, energy or ground state.
  - **Record sourcing ("records are mass", tested as a hypothesis):**
    - the literal form makes inflation-then-reheating impossible at g ≡ 0;
    - Lemma M: fixed nonnegative record weights give w_eff ≤ 0, so there is no radiation era;
    - the record map on file records the vacuum.
  - **Global constraint:** a final-state rule is ill-posed when the vacuum pick is gravity-sensitive, and a causal average signals.
  - **Vacuum-shift symmetry** leaves C a free modulus. Reflections fix the midpoint, not the bottom.
  - **Prices:** P-r173a (= P92), P-r173b, P-r173c, P-r173d.

  Referee running.
- **R17-1 (literal qubits as Z₂ clocks): worker reading WINDOW.** It refutes EXTENDS in the class, which needs the referee.
  - **Why the bound fails.** A mod-N law allows jumps with Gδ = Nγ. Their zeroth moment is M₀ = −N·D(γ):
    - a zero dipole gives k²;
    - a TT dipole gives k⁰;
    - integer-invariant hops give k⁴ (R16-7).
  - **Minimal hops.** Every Z₂-invariant hop of weight < 20 has no integer lift. N0914's own Hamiltonian at N = 2 is in the k⁰ class.
  - **Explicit qubit models:**
    - **k⁰ (cube moves).** Plus an electric term, this is exactly the 3D transverse-field Ising model on the dual lattice: a scalar Ising model, not a graviton.
    - **k²** (neighbour hop; slope 2.000). Probably a helicity-0 sound mode.
  - **Readout bridge.**
    - On a Z₂ clock the face labels carry A₁+E, not T₂, under the natural action.
    - Every invariant move is Hermitian, so the sine-curvature probe vanishes.
  - **Control.** The 3D toric code gives a gapped k⁰ f-sum, a negative control only.
  - **The question moves to:** does any mod-2 model have exactly two helicity-±2 gapless branches, gapped V/S channels and a metric readout?
  - **Prices:** P-r17-1a to P-r17-1d.

  Referee running.
- **R17-4 (the bill's rows): worker reading COUNTED-ROWS in part (U + E1). Second off-axis row OPEN; (f) OPEN.**
  - **(a) Off-axis formula:** Ξ(n, e) = (1/32)⟨W_e A_nn/ε⁵⟩ − (1/192)⟨(n·∇)²W_e/ε³⟩. Grid-checked; the rank-4 TT space confirms R13-8.
  - **U identities (proved):**
    - Ξ_face2 ≡ Ξ_T2g;
    - Ξ_face1 = (3Ξ_Eg + Ξ_T2g)/4 − (1/128)⟨K₆/ε⁷⟩.
    - So the off-axis rows cost one new condition, a sixth cumulant, not two.
  - **(b) Search:** Ξ_face1 ≈ −9e-4 on R16-3's U zeros, and it stayed negative wherever both axis rows are ≥ 0 (not certified).
  - **Lemma M (proved).** Any C₂ᵧ-covariant T₂g amplitude must vanish at k_x = π. R9-9's M vertex does not, so M has no summable kernel on doubler-free laws.
    - **Consequence:** the M numbers of R16-3 and R16-9 are integrals of a non-local vertex. U is unaffected.
  - **E1 vs E2:** the off-axis rows depend on how the vertex is extended (P-TTV₂).
  - **(c) LV tadpole:** ρ + p > 0 for every law in 𝒮, so it needs a trace counterterm (P-Tad).
  - **(e) Totals (conditional):** 8 + CC per class or 12 + CC per species under U + E1; 9/13 + CC under E2.
  - **Prices:** P-K6, P-TTV₂, P-LocM, P-Tad.

  Referee running.

### C5 Round 17, item 6 (pre-registered 00:46Z, before launch)

**R17-6. The moved question: is there a qubit (Z₂-clock) model with exactly two gapless helicity-±2 branches?**
- **Plain question.** R17-1 (worker; referee running) finds that the k⁴ obstruction fails for qubits read as Z₂ clocks. It exhibits:
  - a k⁰ model, which is the 3D transverse-field Ising model (a scalar);
  - a k² model, probably a helicity-0 sound mode.

  It also finds that under the natural rotation action, on-site Z₂ face labels carry A₁+E and not T₂. Is there any local Z₂-clock model on Z³ whose low-energy spectrum has:
  - exactly two gapless helicity-±2 branches with ω ∝ k (or at least a definite power);
  - gapped vector and scalar channels;
  - a stated metric readout?
- **Setting.**
  - Local, translation-invariant, cubic-covariant qubit Hamiltonians on Z³ with a mod-2 tensor Gauss law. Slots can sit on faces, links or sites, with a block encoding into site qubits stated.
  - Rotation action: natural, or a shift implementation (P-r17-1c), stated.
  - Excluded: integer-law lifts (R16-7/R16-11), rotors, power-law hops.
- **Prior art (count once):**
  - R17-1 and its referee (when back);
  - R16-7 and R16-11 with their verdicts;
  - R15-3 (≥ 4 branches in finite PSD Gaussians), R15-5, R13-2, R12-5;
  - the X-cube/fracton literature (gapped; RECALLED) and the Gu–Wen helicity-±2 claim.
- **Removed hypothesis:** integer lifting, together with the Gaussian/PSD class of R15-3 (Z₂ models are not Gaussian).
- **Probes.**
  - (a) The representation theory. Which slot placements and rotation actions allow a T₂ (or T₂g) on-site or few-site label? Is the A₁+E obstruction general for the natural action?
  - (b) Construct the best candidate. Compute its excitation spectrum by ED on the largest feasible cluster and by spin-wave or large-N where controlled. Identify the helicity content of the gapless modes, with the method stated in advance.
  - (c) Does R15-3's partner theorem have a Z₂ analogue, e.g. via an f-sum or the Goldstone-type counting of R16-11?
  - (d) Prices.
- **FIXED readings.**
  - **CANDIDATE:** an explicit qubit model with checked evidence of exactly two helicity-±2 gapless branches and gapped V/S, with its readout stated. Evidence, not production; production would need a referee.
  - **OBSTRUCTED:** a refereed no-go for a stated Z₂ class, e.g. "no natural-action Z₂ model has a T₂ gapless branch".
  - **OPEN:** otherwise.
- **Expectation.** OPEN. Most likely a representation obstruction for the natural action, plus an unresolved shift-action class. A CANDIDATE would be a major result and needs the most careful check.
- **R17-2 (W7 boost bracket): worker reading OPEN.**
  - **Lemma D (proved and checked; bulk, leading order).** R16-12's generator W is exactly GR's own dressing (ratio −1 to 6.4e-8). So the W7 tail is an edge quantum's own GR field, moved by a lattice momentum that is not a true translation.
  - **Lemma H (proved and checked).** {W, H₀} = −H_int plus constraint terms. So the undressed H′ ≈ H₀ is non-local only through gauge multipliers, which is the Coulomb-gauge pattern. This corrects R16-12's "non-local H′".
  - **B3's world-line kernel** can be traded for non-local multipliers (suggested).
  - **Escape 2:** a 1/r world-line kernel. Any Jacobi failure is confined to the q·v = 0 shell, which was not evaluated.
  - **The dressed curvature O_F** is bulk-invariant. R13-4's criterion also flags GR's own dressed operators, so it is not a valid gravity control.
  - **Direction (suggested):** removable from the bulk physics, with what is lattice-specific relocated to the global (boundary) Poincaré charges.
  - **Prices:** P-W7mult, P-W7bdy, P-W7ro.

  Referee running.

#### C5 referee verdicts R16-14, R17-3 (recorded 00:47Z; codex gpt-5.6-sol, xhigh)

- **R16-14 referee: CONFIRMED WITH CORRECTIONS. Reading: E1 and E2 OPEN and observationally tied; only the literal linear completions (L0, L1/2) EXCLUDED.**
  - **E1** has the GR long-range α₁ = α₂ = 0 and γ = 1 at linear order. Its correction starts at 6(ωτ)² and gives 1/r³ terms.
  - **E2** has the same near-zone projection plus tiny non-PPN friction terms. Calling it "exactly PPN" globally is too strong.
  - **Confirmed:** the factor 45(cτ/R)² = 6.94e-13, and that E2's dipole exerts no leading torque on an inversion-symmetric body.
  - **β is not fixed by either bare route.**
    - A metric linear in matter T gives β = 0 with geodesic matter, or β_eff = ½ with the literal coupling. Mercury excludes both.
    - Completion N (Landau–Lifshitz total-stress source) formally restores β = 1. But it is a new, uncompleted nonlinear source/action bridge, especially for E2, and it does not establish premise (iii).
- **R17-3 referee: NOT CONFIRMED (the TUNING). Reading OPEN.**
  - **Theorem T is not proved as stated:** H-an makes V analytic, but not Γ.
  - **The sound bounded obstruction:**
    - g ≡ 0 forces GR with one constant, C = ρ_v,late, and a fixed independent value is radiatively unstable;
    - without an informative pre-branch label, no causal common rule cancels histories that end in unequal vacua;
    - fixed nonnegative record weights cannot source radiation;
    - the causal average signals;
    - vacuum-shift symmetry does not select the zero.
  - **The number-free rule C = E₀[H]** tracks radiative corrections by definition. It is an added source/action principle, not forced by the four axioms, and not "an independent exact number". So the result is OPEN, not TUNING.
  - **Consequence for owner Q1:** "the lowest state of the law weighs nothing" is a genuine, consistent, number-free principle that would have to be added. It is not a disguised tuning (this narrows vR16-6). It is still unforced by the axiom texts.

### C5 Round 17, item 7 (pre-registered 00:49Z, before launch)

**R17-7. If "the law's lowest state weighs nothing" (C = E₀[H]) is added as a principle, what does it predict, and does it survive?**
- **Plain question.** R17-3's referee rules that C = E₀[H] is a consistent, number-free source/action principle. It tracks radiative shifts by definition. It is not forced by the four axiom texts, and it is not a disguised tuning. If Jon were to add it:
  - What does it predict for today's acceleration? Under it, a constant Λ is zero, so the observed acceleration must be content above the ground state.
  - Does it survive the grid's own zero-point (P70: w ≥ 0 on the fixed grid; R11-3)?
  - Does it survive SM vacuum metastability (P93)?
  - Does it survive the record/permanence structure (AX:79-83)?
  - Is it covariant beyond homogeneity (R13-3, R15-1)?
- **Setting.**
  - R16-6/R17-3's homogeneous equations, plus linear perturbations.
  - The grid zero-point per R11-3.
  - The SM effective potential (RECALLED, labelled).
  - DESI DR2 (fetched, untrusted, or RECALLED).
  - Excluded: active compensation (R15-1 FAIL); 𝓡⁺ readers.
- **Prior art (count once):** R17-3 and its verdict, R16-6 and its verdict (Theorem Z, NA), R11-3, R13-3, R15-1, R15-4 (DESI phantom), Lemma PT, and the owner's records-are-mass thought (as a hypothesis only).
- **Probes.**
  - (a) Late universe. If E₀ weighs nothing, what must the dark energy be (w(z), and whether it is phantom)? Compare with DESI DR2. Name any prediction that distinguishes this from ΛCDM.
  - (b) Grid zero-point. Does E₀ include the lattice zero-point (w ≥ 0 per R11-3)? If so, is the residual exactly zero, or w ≥ 0 matter-like?
  - (c) Metastability. If our vacuum is not E₀, what is Λ̃ = κ(V_EW − E₀)? Is there a version, "lowest state of the current sector", that avoids it without branching (P94) or acausality?
  - (d) Inhomogeneous and covariant form. Write C = E₀ as a local covariant statement, or show it requires a global quantity. Then check it against R15-1's signalling criterion.
  - (e) Prices.
- **FIXED readings.**
  - **VIABLE-PRINCIPLE:** (a)–(d) are all consistent with observation, with a covariant, non-signalling form, checked.
  - **EXCLUDED-PRINCIPLE:** a refereed demonstration that the principle contradicts an observation, or forces signalling or acausality in every covariant form.
  - **OPEN:** otherwise.
- **Expectation.** OPEN, leaning towards three conditions:
  - (b) needs E₀ to include the grid zero-point exactly;
  - (c) is a real problem unless the SM is stabilized;
  - (d) needs a global quantity, though possibly a non-signalling one (a constant).
- **R17-5 (multi-band W2_pf): worker reading EXCLUDED-MB.** A referee is required.
  - **Theorem MB-A.** For any finite N and any degeneracy, the zeroth moment gives θ ≡ 0 and a k-independent Π spectrum. This closes the C₂-exchanged gap.
  - **Corollary S.** Standard W2_pf fails for any nonzero momentum density.
  - **Theorem MB-B.** W1_pf makes every band either momentum-free or an "axis mover" whose energy depends only on ĉ·k. The referee's six-band construction is six species of axis movers.
  - **Physical momentum fails under every bridge:**
    - standard θ;
    - lattice translation (winding 0);
    - redshift. By Lemma RB, the strain response tracks velocity, giving 1/k of the physical redshift and a blueshift for counter-movers.
  - **Lemma R.** Standard rotations force Π ≡ 0.
  - **The only finite-band local route left:** P-r175a, mixing or altered generators, which is untested. P64 (tower) and P90 (discontinuous) are unchanged.

  Referee running.

### C5 Round 17, item 8 (pre-registered 00:52Z, before launch)

**R17-8. W15's last finite-band local route: can constant shifts be generated by a component-mixing, field-dependent or altered generator (P-r175a)?**
- **Plain question.** R16-5 (refereed) and R17-5 (worker) exclude multiplier-generated shifts for finite-band local matter. The remaining routes are:
  - generators that mix stress components (e.g. T^{0j} with T^{jk} or T^{00});
  - field-dependent generators;
  - altered leading generators (RFW F2's item).

  Is there a finite-band, quasi-local, cubic-covariant matter law whose constant-shift generator lies in one of these classes, satisfies W2_pf with a nonzero physical momentum (one that redshifts correctly), and keeps W1_pf?
- **Setting.**
  - Free matter with finite N.
  - Generators G_j = ∫(T^{0j} + Σ a·T^{μν} + field-dependent terms), quasi-local.
  - R9-9's N-type graviton, projectable lapse.
  - The redshift bridge as in R17-5 (a hypothesis on AX:187).
  - Excluded: P64, P90, and the single-band case.
- **Prior art (count once):** R16-5 (T_pf, its verdict, the 1D mixing result), R17-5 (MB-A, MB-B, RB, R), RFW F2 (`TESTS:2268-2280`), I1/I2, C4 F1.
- **Removed hypothesis:** shifts acting by a multiplier.
- **Probes.**
  - (a) The general zeroth-moment identity for mixing generators. Is θ still forced to 0? Does the momentum-symbol argument survive?
  - (b) Field-dependent generators at linear order in the fields.
  - (c) If a solution exists, run R17-5's redshift and translation tests on it.
  - (d) Prices.
- **FIXED readings.**
  - **ESCAPE:** an explicit finite-band local law with W2_pf, nonzero physical momentum and correct redshift. Checked.
  - **EXCLUDED-MIX:** a refereed no-go covering mixing and linear field-dependent generators.
  - **OPEN:** otherwise.
- **Expectation.** EXCLUDED-MIX. The zone-mean anomaly of a periodic symbol is topological (winding), and mixing cannot change a winding. That would leave only P64, P90, or giving up W2_pf.
- **R16-13 (fermion loops): worker reading LIFTED on the letter of the clause; SM-like content OPEN.** A referee is required.
  - **Theorem DT:** the Dirac cone shift, computed under two stipulations:
    - a vielbein TT vertex with the Wilson mass not coupled;
    - R9-2's strain flow for the Dirac sea.
  - **Signs:** opposite to the scalar for Ξ_T2g, Ξ_Eg and μ_E.
  - **Lemma V1:** s′² + 3W′² ≤ 1 implies v_max ≤ 1.
  - **New row:** a Wilson-Dirac T₂g shear mass, so R16-9's "μ_T2 = 0" fails with fermions.
  - **Joint zero:** E_g = T₂g = μ_E = 0 at m = 0.01 and 0.001.
    - Content: 2 scalars on G(2.5647), 2 on G_w(1.7406, 0.7413), and 1 Dirac on D1(1.3133, r = 0.5731), all subluminal.
    - Cost: 3 tunings.
  - **Caveats:**
    - μ_T2 ≠ 0 at the root;
    - it needs two scalar edge families, and one Higgs edge stalls;
    - SM counts (4 scalars + 22.5 Dirac) are not reached, because Dirac birefringence dominates;
    - r sits 0.7% below the cap;
    - there are no photon or gluon loops.
  - **Prices:** P-R16-13a, b and c.

  Referee running.

### C5 Round 17, item 9 (pre-registered 00:55Z, before launch)

**R17-9. SM content on one graviton cone: do the gauge-boson loops offset the Dirac birefringence?**
- **Plain question.** R16-13 (worker; referee running) zeroes E_g, T₂g and μ_E with toy content (4 scalars on two edges + 1 Dirac field). With SM counts (one Higgs edge, 22.5 Dirac fields) it stalls: Dirac birefringence (Ξ_T2g − Ξ_Eg ≥ +2.6e-3 per field) dominates. Photon and gluon loops are missing because no vector TT vertex exists. With 12 gauge bosons (vectors, each with two polarizations), can the vector loops offset the Dirac birefringence? Is SM content then placeable on one cone, and with how many tunings?
- **Setting.**
  - Build a vector TT vertex for a compact or non-compact U(1)/SU(N) lattice gauge field. Use the Peierls/Maxwell stress on the R14-1 subluminal photon edge, plus R13-5's prescription; state the stipulations.
  - Content: SM counts in the free-field limit — 12 vectors, 22.5 Dirac fields (D1 family), 4 real scalars on one edge family.
  - One loop, zero-point vacuum supplied, light masses (m ≤ 0.01). Every whole-zone v_max is stated.
- **Prior art (count once):** R16-13 (Theorem DT, Lemma V1), R16-3 and R16-9, R17-4 (Lemma M; use the U-type or a local vertex), R13-5, R10-5 (photino control), R8-5's photon edges, R16-10's photon stiffening (superluminal at 7.35; excluded here).
- **Removed hypothesis:** scalar and Dirac loops only.
- **Probes.**
  - (a) The vector TT vertex and its IBP identity, with sign checks against the continuum (zero).
  - (b) Signs and sizes per vector field of Ξ_Eg, Ξ_T2g, μ_E and μ_T2 on subluminal photon edges.
  - (c) The SM-count solve: the minimal number of edge tunings for E_g = T₂g = μ_E (= μ_T2 if possible) = 0, with one scalar edge. Or a demonstration of conflict in the stated families.
  - (d) The bill update.
  - (e) Prices.
- **FIXED readings.**
  - **SM-LIFTED:** an explicit SM-count content, all edges subluminal and one Higgs edge, with E_g = T₂g = μ_E = 0 at a common light mass. Checked, with the count.
  - **SM-CONFLICT:** a demonstration (refereed if class-wide) that no tuning of the stated families achieves it.
  - **OPEN:** otherwise.
- **Expectation.** OPEN. The vector sign is likely boson-like (the same sign as the scalar), so the vectors add to the scalar side. That could offset the Dirac birefringence at SM ratios, but the margins are unknown.
- **R17-7 (the E₀ principle): worker reading OPEN.** The principle is consistent only under named conditions.
  - **(a) Late universe.** Λ̃_late ≥ 0 always, and equals 0 with P93. So today's acceleration must be temporary, rolling dark energy, which predicts eventual deceleration.
    - A BAO-only DESI proxy: thawing scalars recover 54–62% of the ΛCDM-to-CPL gap.
    - DESI's phantom side cannot be reproduced.
  - **(b) Grid zero-point.** The energy cancels by definition, but the pressure residual ρ₀+p₀ ≈ 1e123 ρ_Λ per scalar remains.
    - Invisible under bridge (d-i).
    - Under (d-ii) it needs pairing, or one tuning per order per species.
  - **(c) Metastability.** SM-only running gives Λ̃ ≈ 1e112–1e120 ρ_Λ, so the principle predicts a stabilized EW vacuum (P93).
    - Causal alternative: (S′-start), the bottom of the starting basin (P-r177a).
    - (S′-current) breaks Bianchi in every local form, a no-go.
  - **(d) Covariant form.** G + Λ_* g = κT with Λ_* = −κe₀, a law constant. It is local and non-signalling.
  - **Records (Lemma X).** Dense site-projection records cost ~1e123 ρ_Λ per field. That is P4's heating, not the principle's. Under (S) the records-are-mass thought follows as a consequence.

  Referee running.

#### C5 referee verdicts R16-13, R17-1, R17-2, R17-4, R17-5 (recorded 01:11Z; codex gpt-5.6-sol, xhigh)

- **R16-13 referee: NOT CONFIRMED (the LIFTED). Reading OPEN.**
  - **Confirmed, conditionally:** under an ultralocal-seagull assumption and the stipulated V0 (Dirac TT) and SF (strain) responses, these reproduce:
    - Theorem DT (to 2.7e-9);
    - the opposite-sign D1 example;
    - Lemma V1;
    - the Wilson T₂g shear mechanism;
    - a subluminal codimension-3 axial zero at separately tuned light masses.
  - **Not lifted in the registered local-stress setting:**
    - the only root uses the non-local scalar M amplitude (R17-4 Lemma M);
    - μ_T2 remains nonzero;
    - neither one-Higgs-edge nor SM-count content is reached.
- **R17-1 referee: CONFIRMED WITH CORRECTIONS. Reading WINDOW; EXTENDS refuted at the f-sum level.**
  - **Why:** modular Gauss invariance gives Gδ = Nγ and M₀ = −N·D(γ), so the integer-law O(k⁴) bound is not universal.
  - **The explicit models:**
    - an N = 2 cube+μ₈ qubit stabilizer model has an exact positive k-independent TT-label f-sum;
    - a moving-cube model has m₁ ≥ c·k² for generic coupled directions;
    - integer lifts recover O(k⁴).
  - **Not established:** a physical metric susceptibility, or a graviton.
    - The k⁰ model is the even sector of a scalar 3D TFIM.
    - The k² construction gives only a scalar-density/rank-one TT signal.
    - Still open: the one-site encoding, the readout, the two-helicity spectrum, the S/V gaps, and the reciprocal coupling.
- **R17-2 referee: CONFIRMED WITH CORRECTIONS. Reading OPEN.**
  - **Lemma D is confirmed** (ratios −1 to 1.1e-14). W is the inverse of one particular linearized-GR Coulomb/comoving dressing, not a unique one.
  - **At leading bulk order** for free subluminal S/G matter, W7's forced translation term is canonically equivalent to that dressing. Its matter coupling can be moved into non-local constraint multipliers, so no instantaneous physical bulk interaction is demonstrated.
  - **Still open:** degree 3 does not close. Missing are the global boundary algebra, the zero-frequency shell, the remaining boost brackets, exact lower-order closure, and a completed Dirac observable.
- **R17-4 referee: CONFIRMED WITH CORRECTIONS. Reading COUNTED-ROWS for U+E1; the K₆ row and the shear certificate OPEN.**
  - **Confirmed:**
    - the off-axis formula, checked independently to 6.7e-16; the D²W form needs W ∈ C² or a weak derivative;
    - U reduces the two off-axis rows to one sixth-cumulant condition. Searches strongly but non-certifiably suggest it conflicts with the axis zeros;
    - the LV tadpole is strictly positive and separately payable;
    - E2 shows that off-axis values depend on the vertex extension.
  - **Lemma M is confirmed** under the stated single-amplitude covariance hypotheses: M has no absolutely summable doubler-free realization. U preserves R16-3's refutation.
  - **Dated consequence:** the M-vertex numbers in R16-3, R16-9 and R16-13 belong to a non-local vertex. R16-3's REFUTED stands via U.
- **R17-5 referee: CONFIRMED WITH CORRECTIONS. Reading EXCLUDED-MB.**
  - **The class:** finite-N free quadratic matter on the BZ torus with:
    - continuous quasi-local kernels and W1 regularity;
    - symmetric stress;
    - a projectable lapse;
    - multiplier-generated constant shifts.
  - **What fails in that class:**
    - standard W2_pf is impossible for nonzero momentum density;
    - nonzero-label sectors are restricted to 1D axis motion;
    - no continuous finite-dimensional generator exponentiates to a lattice translation;
    - conditional on H-RB, the strain response is velocity × label, not p·v.
  - **Coverage:** the six-band and C₂-exchanged families are included.
  - **Still open:** altered or component-mixing generators (R17-8 running).
- **R17-6 (Z₂ helicity-2 search): worker reading OPEN**, with subclass OBSTRUCTED results offered to the referee. The method was pre-stated in `agents/C5_R17-6_method.md`.
  - **The representation obstruction is not general.**
    - Proposition F: T₂ multiplicity equals the site group's fixed-vector count.
    - N0914's slots carry A₁+E+T₂ at the zone corner.
    - Proposition S: the shift action is the natural action conjugated by a staggered flip, so it only relocates the readout to R.
    - Two-slot product labels carry T₂ at zero momentum.
  - **Theorem G (Goldstone):** if the TT modes are Goldstone modes, there are at least 4 gapless branches.
  - **Theorem Z (f-sum).** A vanishing TT f-sum with a finite static response forces either vector/scalar weight at zero energy or a pinch point. Z′ covers the divergent case. A k⁰ f-sum with finite response is not covered.
  - **Lemma R:** equal-weight (CSS/RK) Z₂ states have no pinch points.
  - **Best candidate.** It needs bound γ-charges at U ~ K, the same window as P-r16-7a. ED is infeasible (2³¹ states).
  - **Prices:** P-r17-6a to P-r17-6d.

  Referee running.

### C5 Round 17, items 10–11 (pre-registered 01:12Z, before launch)

**R17-10. Certify or break the graviton-cone/K₆ conflict on one subluminal scalar edge (U vertex, E1).**
- **Plain question.** R17-4 (refereed COUNTED-ROWS for U+E1) leaves one new off-axis condition, a weighted sixth cumulant K₆. Searches strongly but non-certifiably suggest it conflicts with the axis zeros (E_g = T₂g = 0). R16-9's shear conflict (μ_E) is likewise uncertified (`vR16-9:9`). Can a certified enclosure settle either conflict for the local U vertex?
- **Setting.**
  - R16-9/R17-4's relaxation: per-level moments of the occupation measure, with Lemma R_U's necessary inequalities.
  - U vertex, E1 extension, m ∈ [0.01, 0.1], subluminal separable 𝒮.
  - Method stated in advance: interval branch-and-bound with outward rounding, or a verified moment-SOS relaxation with rational certificates. Exactness and tolerance stated.
  - Excluded: the M vertex (non-local, Lemma M), fermion loops.
- **Prior art (count once):** R16-9 and `vR16-9:5-11`, R17-4 and its verdict, R16-3 (Z1, IBP), R14-3.
- **Removed hypothesis:** sampling (certification).
- **Probes.**
  - (a) Formulate the K₆ and μ_E joint problems as polynomial optimization over the relaxation.
  - (b) Run the certified method on the smallest problem first: U, K₆ with the axis zeros, m = 0.01.
  - (c) Report certified bounds, or a feasible point.
  - (d) Prices and the bill update.
- **FIXED readings.**
  - **CERTIFIED-CONFLICT** (per condition): a certified proof that the stated condition cannot hold together with the axis zeros on the relaxation superset, refereed.
  - **JOINT:** an explicit subluminal law meeting it, checked.
  - **OPEN:** otherwise.
- **Expectation.**
  - CERTIFIED-CONFLICT for K₆ at m = 0.01, if the margins (≈ 1e-4) beat the relaxation gap.
  - OPEN for μ_E on U, whose margin is thin (1.3e-4).

**R17-11. The E₀ principle's pressure residual: is bridge (d-i) — vacuum exchanging energy and momentum with the expansion sector — consistent and covariant?**
- **Plain question.** R17-7 (worker; referee running) finds that under C = E₀[H] the grid zero-point's energy cancels, but its pressure ρ₀+p₀ ≈ 1e123 ρ_Λ per scalar remains. It is invisible only under bridge (d-i), where the vacuum has no separate conservation law and exchanges with the sector that drives expansion. Otherwise pairing, or one tuning per order, is needed.
  - Is (d-i) consistent with local covariance and Bianchi beyond homogeneity?
  - Does it reintroduce R15-1's signalling (a g ≠ 0 channel) or a new instantaneous channel?
  - What does it predict?
- **Setting.**
  - R14-5/R15-1's E-sector equations, linear perturbations, with C = E₀ and the grid zero-point stress of R11-3.
  - Bridge (d-i) written as a covariant exchange current Q^μ.
  - Excluded: active compensation of vacuum changes (R15-1 FAIL).
- **Prior art (count once):** R17-7, R17-3, R15-1 (Lemmas S, V) and its verdict (`vR15-1:15`), R14-5, R11-3, R13-3 (Lemma G′), and interacting-vacuum (Q-coupled) literature (RECALLED).
- **Removed hypothesis:** separate vacuum conservation.
- **Probes.**
  - (a) A covariant form of (d-i). Which Q^μ absorbs ρ₀+p₀ exactly at all times?
  - (b) Bianchi and causality at linear order: is there an instantaneous response (Lemma S test)?
  - (c) Observable consequences, e.g. a coupling of the vacuum to matter flows.
  - (d) Prices.
- **FIXED readings.**
  - **CONSISTENT:** a covariant, non-signalling (d-i) that absorbs the pressure exactly, checked at linear order.
  - **SIGNALS / INCONSISTENT:** a refereed demonstration that every (d-i) form in a stated class signals or breaks Bianchi.
  - **OPEN:** otherwise.
- **Expectation.** SIGNALS. Absorbing a uniform pressure exactly at all times is the CMC/g ≠ 0 pattern again, unless the pressure residual is itself constant, in which case (d-i) may be trivial.
- **R17-8 (mixing, field-dependent and altered generators): worker reading OPEN.** The no-gos cover each generator kind separately, not jointly.
  - **Lemma N (Noether lock).** W1_pf forces the shift generator to be ∫T^{0j} on shell. This closes RFW F2's altered-generator item in the canonical class.
  - **MIX-1 (single band).** Finitely many shift eigenvalues cannot track a continuous symbol, so g ≡ 0.
  - **MIX-2 (multi-band).** The k-independent Π spectrum is proved for one small shift and for analytic symbols. The generalized RB then fails the redshift test.
  - **Lemma FD.** Field-dependent generators enforce W2_pf only on shell, up to O(q²).
  - **Theorem W (winding).** The redshift bridge needs rank-3 windings, but a T³ band's Reeb graph allows rank ≤ 1, so π ≡ 0 for isolated analytic bands.
  - **Not covered:**
    - mixing and field-dependent generators used together;
    - continuous-only symbols with several shifts;
    - crossing bands.
  - **Prices:**
    - P-r178a: a non-canonical shift action;
    - P64 and P90 unchanged.
  - **Archive fix (01:30Z):** the committed R17-5 runner imported a profile file from a path that was not archived. The file was copied beside it and the path corrected. The rerun matches the stored output (reported by R17-8).

  Referee running.
- **R17-9 (vector loops, SM on one cone): worker reading OPEN.**
  - **The vector TT vertex VU:** the Maxwell stress of site-averaged fields at R9-9's placement. It is local, and it reduces to the continuum helicity-2 amplitude.
  - **The Maxwell vector pushes the cone outward, like Dirac (not boson-like).** This comes from E–B interference. So the expectation's sign premise fails.
  - **Under VU, no SM-count zero.** Two conditions are incompatible on all sampled laws:
    - the T₂g row needs Ξ_γ,T2g ≤ 6e-4;
    - the Dirac birefringence needs Ξ_γ,Eg − Ξ_γ,T2g ≥ 4.46e-3.
  - **Under VM (magnetic part off R9-9's placement), an explicit SM-count zero exists:**
    - content: 4 scalars + 22.5 Dirac fields + 12 vectors;
    - cost: 3 edge tunings, every edge subluminal;
    - Ξ_T2g = Ξ_Eg = μ_E = 0 at m = 0.01 and 0.001;
    - μ_T2 = +0.106 is left over, from the Wilson-Dirac fields.
  - **Whether VM is in-setting decides between OPEN and SM-LIFTED.** The placement is a law datum (P-R17-9b).
  - **Bill:** 9 + CC per class or 13 + CC per species. The gravity–charge block split ends.

  Referee running.

#### C5 referee verdicts R17-6, R17-7, R17-8 (recorded 01:38Z; codex gpt-5.6-sol, xhigh)

- **R17-6 referee: CONFIRMED WITH CORRECTIONS. Reading OPEN.**
  - No qubit model with exactly two helicity-±2 gapless branches and strict V/S gaps is established, and no universal qubit no-go is proved.
  - **No representation obstruction under the natural action.** T₂ appears at R, in low-symmetry slot orbits, and in pair labels at Γ.
  - **Bounded results:**
    - **Internal-Goldstone subclass:** at least four gapless branches, rigorously.
    - **Unique symmetric quasi-local class** where both axial TT f-sums vanish, both TT responses stay nonzero, and the full response has a finite, direction-independent limit: strict V/S gaps are impossible without a pinch point.
  - **Still open:**
    - pinch-point phases;
    - finite-response k⁰ f-sums;
    - non-strict V/S continua;
    - degenerate or symmetry-broken ground states;
    - other readouts.
- **R17-7 referee: CONFIRMED WITH CORRECTIONS. Reading OPEN.**
  - **Corrections:**
    - Dark energy above e₀ need not be temporary.
    - "One tuning per order" is proved only through m⁴.
    - Bianchi excludes (S′-current) only without a local carrier.
  - **Strongest statement.** C = e₀, if stipulated, is a fixed, non-signalling constant, and the residual κ(ρ_v − e₀) is ≥ 0. Its viability has these conditions:
    - The DESI proxy recovers 54–62% of one synthetic gap and cannot realize w < −1.
    - The grid enthalpy needs bridge (d-i) or structural cancellations.
    - P93 is a severe stabilization condition.
    - R-projection records give P4 heating; R-label records give nothing.
  - **Status:** not excluded, and conditionally viable.
- **R17-8 referee: CONFIRMED WITH CORRECTIONS. Reading OPEN.**
  - **Confirmed, as scoped no-gos:**
    - **Lemma N:** canonical, local-in-time; it locks the generator to T^{0j}.
    - **MIX-1:** single band.
    - **MIX-2:** one small eigenvalue; finitely many under analyticity.
    - **FD:** the equal-energy O(q) tangential identity is unaltered.
    - **Theorem W:** conditional on H-RB, with analytic continuation and tame Reeb topology.
  - **Still open:**
    - continuous non-analytic multi-shift mixing;
    - crossing bands;
    - joint mixing with field-dependent generators.
- **R17-11 (E₀ principle, pressure bridge (d-i)): worker reading CONSISTENT in 𝒟.** The expectation was SIGNALS.
  - **Class 𝒟:** R14-5's E-sector, with √h fixed per site so the spatial trace is not imposed, sites riding the normals, and C = E₀.
  - **The bridge:**
    - The grid vacuum's enthalpy W is absorbed by the unique exchange current Q_ν = ∇^μ(W h_μν).
    - Generalized Lemma V: W never enters λ̇.
    - Under (S), g′ ≡ 0 and the site frame drops out of the field equations.
  - **Linear order:** the dust equation has no W terms, the tilt is absent at g′ = 0, and there is no instantaneous channel (Lemma S jump = F).
  - **Observables:** nothing beyond (S). The anisotropic and TT walls are unchanged.
  - **Other receivers excluded:**
    - unimodular Λ(x), which drifts by about 1e123 ρ_Λ;
    - matter;
    - an ultralocal khronon;
    - (d-ii) still needs W = 0.
  - **Bill:** R17-4's LV tadpole equals P70's uniform part, which is paid by P-vac′ with no numbers, so the bill drops by one.
  - **Prices:** P-r1711a, b and c.

  Referee running.

### C5 Round 17, items 12–13 (pre-registered 01:39Z, before launch)

**R17-12. Which vector-vertex placement does consistency force: VU (R9-9's placement) or VM?**
- **Plain question.** R17-9 (worker; referee running) finds that the choice decides everything. Under VU, the Maxwell stress at R9-9's 09-14 placement, no SM-count zero exists. Under VM, where the magnetic product is moved to z + ½, there is an explicit SM-count zero with 3 tunings. Is the placement free, or is it fixed by something we already require?
  - (i) The vector W1 Ward identity, i.e. a conserved lattice stress for the photon coupled to the stated graviton.
  - (ii) Gauge invariance of the pair vertex.
  - (iii) R9-9's own graviton placement and its Killing identities.
  - (iv) Locality (Lemma M-type covariance).
- **Setting.**
  - The R14-1 subluminal photon edge, compact or non-compact U(1).
  - R9-9's graviton and placement.
  - The Maxwell stress family, with E and B products placed at any half-integer offsets.
  - One loop, axial q.
  - Excluded: superluminal photons, pairing.
- **Prior art (count once):** R17-9, R9-9 (placement at `C5_R9-9_report.md:100`), R13-5 (W1, B2), R17-4 (Lemma M, P-TTV₂), R16-13 (V0 stipulation, `vR16-13:5`), R8-5, and the lattice Maxwell stress tensor literature (RECALLED).
- **Removed hypothesis:** the vertex as a free datum.
- **Probes.**
  - (a) Write the vector W1 identity on the lattice for each placement. Which placements satisfy it, exactly or to O(q)?
  - (b) Gauge invariance and C₂ covariance of each placement (Lemma M test).
  - (c) If several placements survive, state the residual freedom as a law datum. If exactly one survives, recompute R17-9's sign for it.
  - (d) Prices.
- **FIXED readings.**
  - **FORCED-VU:** a refereed proof that consistency selects VU, or excludes VM, in the stated class.
  - **FORCED-VM:** the same for VM.
  - **FREE:** both satisfy every stated requirement (checked). The placement is then a law datum.
  - **OPEN:** otherwise.
- **Expectation.** FREE at O(q). W1 constrains only the divergence, and the placement is an O(q²) datum.

**R17-13. The Wilson-Dirac T₂g shear row μ_T2: can it be zeroed with SM content, and at what cost?**
- **Plain question.** R16-13 (refereed) found a nonzero Wilson-Dirac T₂g shear mass. R17-9's VM root leaves μ_T2 = +0.106, all from 22.5 Wilson-Dirac fields, and a 4-row solve stalled at the parameter bounds. Is μ_T2 = 0 reachable by edge shape on subluminal Dirac edges? Or is it sign-definite on D1-type Wilson edges, making it a separate non-shape knob?
- **Setting.**
  - The Dirac edges: D1(b, r) and Wilson families with r ≤ 1/√3 or s′² + 3W′² ≤ 1 (Lemma V1).
  - The SF strain flow, as R16-13 stipulated.
  - One loop, m ∈ [0.001, 0.01].
  - Excluded: superluminal edges, pairing.
- **Prior art (count once):** R16-13 (mechanism) and its verdict, R17-9, R16-1 (Theorem W/K: convexity sign arguments), R14-3 (μ_E Theorem B), R17-4.
- **Removed hypothesis:** μ_T2 = 0 at one loop (R16-9).
- **Probes.**
  - (a) A closed form or IBP identity for μ_T2^F.
  - (b) A sign theorem on the subluminal Wilson class (convexity as in R16-1/K), or a zero.
  - (c) If a zero exists, add it to R17-9's VM root (4 rows, 4 knobs).
  - (d) Prices and the bill.
- **FIXED readings.**
  - **SIGN-DEFINITE:** a refereed proof that μ_T2^F has a fixed sign in a stated subluminal Wilson class.
  - **ZEROED:** an explicit subluminal law with μ_T2 = 0, checked. If (c) succeeds, also report the full 4-row root.
  - **OPEN:** otherwise.
- **Expectation.** SIGN-DEFINITE on D1 (positive), via the Wilson mass coupling directions, which would make μ_T2 a separate knob.
- **R17-10 (certification): worker reading K₆ OPEN on the relaxation superset, with CERTIFIED-CONFLICT on the fast-only slice 𝓕 (the sharp-turn limit, disjoint from 𝒮); μ_E OPEN.** The method is pre-stated in `agents/C5_R17-10_method.md`.
  - **Theorem F.** On 𝓕, an exact rational certificate shows that the axis zeros (Ξ_Eg = Ξ_T2g = 0) force ⟨K₆/ε⁷⟩ > 0 for every m. It uses multipliers 536/625 and −16/125 and a margin of −117/1600000.
  - **The general relaxation** keeps the sign in local searches (best −6.3e-5), but it is not certified: bin slack is 70–80× the margin, and no SDP solver is installed.
  - **μ_E:** no constant-multiplier pointwise certificate can exist.
  - **P-K6′:** any shape solution of the K₆ row needs a finite fraction of slow-slope structure.

  Referee running.

### C5 Round 18 (pre-registered 01:52Z from S23 §7 (agents/C5_S23_synthesis.md), text fixed before any run; R18-1, R18-2 launched now; R18-3 after R17-12's worker reading (dropped if FORCED-VM); R18-4 if time allows)


**Rules (as rounds 2–17, `TESTS:5688-5706`).**
- Probes on Opus 5.5 at xhigh. Every FAIL, EXCLUDED, OBSTRUCTED or no-go goes to codex gpt-5.6-sol (xhigh) before it is recorded.
- Prices are named, never adopted. Prior art is grepped first and counted once. Hypotheses come before titles. Numbers from memory are labelled RECALLED.
- Every law states its whole-zone v_max, gauge fields included.
- Every count states its counterterm basis.
- Every Λ mechanism says what is enforced and what is stipulated.
- Controls must measure the same observable. Every finite-slot claim names its readout bridge. Forks list their exclusions. Memory claims say generic-GR or model-specific. Expectations name the removed hypothesis.
- **New (from round-17 verdicts):**
  - **Locality of vertices.** Every TT or stress vertex states whether it satisfies the C₂-covariance zero of Lemma M (`vR17-4:7`), or is labelled non-local.
  - **Number-free ≠ forced.** A Λ result distinguishes "no number" from "forced by the four texts" (`vR17-3:17`).
  - **Bounded classes for spectra.** "Gapped" means a uniform spectral gap, multiparticle continua included (`vR17-6:13`).
  - **Certificates.** Any CONFLICT claimed from a relaxation states its enclosure method in advance, as R17-10 did (`SP/R17-10/METHOD.md`).

**Timing.** Each item is sized for about 75 minutes of worker time. The campaign starts no new probes after 09:57Z and ends at 10:57Z.

**Overlap check.**
- R17-9 covers the vector TT vertex and the SM-count solve.
- R17-12 covers the vector placement (VU vs VM), including vector Lemma-M covariance.
- R17-13 covers the Wilson-Dirac μ_T2 row.
- **No R18 item drafts R17-12's or R17-13's questions.**
- R18-3 covers only two things those items leave out: the Dirac TT vertex's own locality (a Lemma-M test for V0), and a certificate for R17-9's VU conflict. It launches only if R17-12 does not return FORCED-VM.
- R17-10 covers the K₆ and μ_E certificates for scalars on U; no R18 item repeats them.
- R17-11 covers bridge (d-i). R18-2 covers P93 (vacuum stability), a different condition of (S).
- R17-6 covers representation theory and Theorems G/Z. R18-1 covers the static pinch-point test and Theorem Z's k⁰ gap, both left open by `vR17-6:19`.

**Priority.**
1. R18-1 (graviton) and R18-2 (Λ), in parallel.
2. R18-3 (SM content on one cone), after R17-12's worker reading.
3. R18-4 (W15) only if time allows, after nothing else is pending.

---

**R18-1. The Z₂ window's signature: does any local Z₂ tensor ensemble with suppressed γ-charges show a pinch point, and does Theorem Z's k⁰ gap close?**

- **Plain question.**
  - R17-1 (refereed WINDOW): reading the qubit as a Z₂ clock escapes the k⁴ f-sum bound.
  - R17-6 (refereed OPEN; OBSTRUCTED in two bounded classes): two gapless helicity-±2 branches with strict V/S gaps need a pinch point in the readout's static response, unless the f-sum is in the k⁰ finite-response gap.
  - Identity V says the pinch point needs the mod-2 law's even γ-charges (Gn = 2γ) suppressed at long wavelength faster than k². Lemma R says states uniform over the full coset have white-noise labels (`vR17-6:15`).
  - Two questions:
    1. Does any local, cubic-covariant Z₂ ensemble that penalizes γ-charges have a pinch point at nonzero γ-density, or only in the exact integer-law limit (which R16-7/R16-11 already cap)?
    2. Can Theorem Z be extended to a k⁰ f-sum with a finite TT response?
- **Setting.**
  - N0914's slots, mod-2 law.
  - Rokhsar–Kivelson-type states with amplitude ∝ exp(−βU Σ_x |γ(x)|²/2). Their equal-time correlations equal a classical ensemble. This is an RK identity, stated as the readout bridge for "static response" here, not a general one.
  - Moves: R17-1's minimal Z₂-invariant cube patterns, which preserve Gn mod 2. Metropolis on L = 6–12 periodic, plus L = 16 if time allows.
  - Observables: the E⊕T₂ structure factors S_TT, S_V, S_S, and the γ structure factor, along the axis, face and body directions.
  - βU ∈ {0, 0.5, 1, 2, 4} plus the βU = ∞ sector (Gn = 0, 0/1 occupations).
  - Excluded: spectra and dynamics; integer-law lifts; non-local moves; degenerate or symmetry-broken grounds (`vR17-6:19`).
- **Prior art (count once):**
  - R17-6 and vR17-6 (Theorems G, Z, Z′ corrected; Identity V; Lemma R narrowed);
  - R17-1 and vR17-1;
  - R16-11 and vR16-11 (the dressing cap);
  - R16-7; N0914's stencil;
  - classical Coulomb-phase pinch points with charge fugacity (Henley; Castelnovo–Moessner–Sondhi; comparators, RECALLED);
  - rank-2 U(1) four-fold pinch points (Prem–Vijay–Chamon; Pretko; comparators, RECALLED).
- **Removed hypothesis.** Lemma R's uniform (full-coset) weight. Kept: locality, finite fugacity, the mod-2 law.
- **Probes.**
  - (a) Build the cube-flip MC. Check detailed balance, and ergodicity within the mod-2 sector, by exact enumeration at L = 2–3 where feasible.
  - (b) At each βU, measure the three readout structure factors and S_γ.
    - A pinch point means the k → 0 limit depends on direction, with the width set by finite size.
    - Report the fitted width ξ⁻¹(βU) and its scaling with L.
  - (c) Is ξ(βU) finite at every finite βU (screening by γ-charges), or is there a βU_c beyond which ξ = ∞ at nonzero γ-density?
  - (d) Analytic. Extend Theorem Z to the k⁰ f-sum class with a finite TT response (e.g. through m₃ or the Goldstone counting), or exhibit the obstruction to extension.
  - (e) Prices.
- **FIXED readings.**
  - For (a)–(c):
    - **PINCH-PRESENT:** a finite-βU ensemble with nonzero γ-density whose readout has a pinch point, consistent with ξ = ∞ under finite-size scaling to the largest L run. Checked. This is evidence for the window at the static level, not production.
    - **SCREENED:** at every finite βU tested, ξ(βU) is finite and fitted; only βU = ∞ is sharp. Checked. This is evidence that the static window needs exact emergence, which is P96 at a phase boundary.
    - **OPEN:** otherwise.
  - For (d):
    - **GAP-CLOSED:** a refereed extension of Theorem Z to the stated k⁰ finite-response class;
    - **OPEN:** otherwise.
- **Expectation.** SCREENED, and (d) OPEN.
  - Classical charge fugacity screens Coulomb-phase pinch points into Lorentzians of width ~ (γ-density)^{1/2} (comparator, RECALLED).
  - The removed hypothesis is uniform weighting, but finite fugacity keeps charges at nonzero density.
  - If SCREENED holds, the Z₂ window narrows to an exact-emergence critical point or a first-order boundary.
  - The likeliest failure is an MC ergodicity problem in the βU = ∞ sector.

---

**R18-2. (S)'s sharpest prediction: must the electroweak vacuum be the true minimum, and is that consistent with the measured inputs?**

- **Plain question.**
  - vR17-3 rules that (S), "the law's lowest state weighs nothing", is a consistent number-free principle.
  - vR17-7 finds it conditionally viable, but only with P93: our vacuum must be the global minimum. SM-only extrapolation would leave 1e112–3e120 ρ_Λ (`vR17-7:37-40`). That turns (S) into a test of particle physics.
  - Within the SM, with measured m_t, m_h and α_s (RECALLED, labelled), is the electroweak vacuum absolutely stable within stated uncertainties?
  - If not, can the lattice at a = ℓ_P stabilize it?
  - If not, what minimal content stabilizes it, and is that a tuning under rule `TESTS:5700` or a content choice?
- **Setting.**
  - Two-loop SM RGEs for λ, y_t and g₁₋₃ (three-loop results as RECALLED comparators). MS-bar matching at m_t with stated threshold corrections (RECALLED, labelled).
  - Effective potential at the stated loop order; instability scale and λ_min.
  - Lattice terms: Planck-suppressed φ⁶/Λ² with Λ = 1/a = M_P, and the box law's dispersion near k ~ 1/a.
  - One stabilizer family: a real singlet with a Higgs portal (tree-level threshold mechanism; RECALLED).
  - (S′-start) as the comparison.
  - Excluded: anthropic selection; landscape branching (P94); active compensation.
- **Prior art (count once):**
  - R17-7 and vR17-7; R17-3 and vR17-3; P93 and P125;
  - Buttazzo et al. 2013 and Degrassi et al. 2012 (comparators, RECALLED; cited in `vR17-7:40`);
  - the singlet-threshold stabilization literature (comparator, RECALLED).
- **Removed hypothesis.** R17-7's SM-only content.
- **Probes.**
  - (a) Reproduce λ(μ), the instability scale and the absolute-stability bound on m_t at the stated order. Compare with the RECALLED published bounds.
  - (b) With the RECALLED m_t average and uncertainty, including a labelled pole-mass ambiguity, state the tension in σ.
  - (c) Can φ⁶/M_P² or the lattice's own dispersion make the electroweak vacuum the global minimum? State the field values involved, against the instability scale.
  - (d) The minimal singlet window (m_S, λ_HS, λ_S) that gives absolute stability up to 1/a, while keeping (S)'s Λ̃ ≥ 0 and no deeper minimum. Say whether any parameter must be held to better than O(1) (a tuning) or not (a content choice).
  - (e) Prices and counting convention.
- **FIXED readings.**
  - **SM-STABLE:** SM-only absolute stability within 2σ of the stated inputs. Checked. (S) then adds no particle-physics price.
  - **NEEDS-STABILIZER:** SM-only metastability beyond 2σ, plus an explicit stabilizer, content stated, that makes the electroweak vacuum the global minimum below 1/a. Checked.
  - **LATTICE-STABILIZES:** a lattice-scale term at a = ℓ_P alone suffices. Checked.
  - **OPEN:** otherwise. An EXCLUDED-for-(S) reading would need a refereed proof that no stabilizer in a stated class works.
- **Expectation.** NEEDS-STABILIZER.
  - SM-only metastability is a 2–3σ tension (RECALLED).
  - Lattice-scale operators cannot act at the 1e10–1e11 GeV instability scale.
  - A singlet threshold stabilizes over an O(1) window, so it is content, not a tuning.
  - The likeliest failure is that RECALLED inputs make (b) inconclusive at 2σ, which gives OPEN.

---

**R18-3. SM content on one cone under the local placement: is the Dirac TT vertex local, and can R17-9's VU conflict be certified?** *(Launch after R17-12's worker reading, and only if it is not FORCED-VM. The readings are fixed now.)*

- **Plain question.**
  - R17-9 [worker] finds the outcome turns on the vector placement. At R9-9's placement (VU), two conditions are incompatible on every sampled law:
    - the T₂g row needs Ξ_γ,T2g ≤ 6e-4 per vector;
    - offsetting the Dirac birefringence (≥ +2.6e-3 per field, `rR16-13:200`) needs Ξ_γ,Eg − Ξ_γ,T2g ≥ 4.46e-3 (`TESTS:6270-6272`).
  - R17-12 asks whether consistency forces VU. If it does, or if the placement is free, the in-setting answer at VU rests on samples. Two questions are left that neither R17-12 nor R17-13 asks:
    1. Is R16-13's V0 Dirac TT amplitude itself local in Lemma M's sense? Every Dirac number since R16-13 uses it.
    2. Can the VU conflict be certified by class bounds — a lower bound B_min on the Dirac birefringence over subluminal Wilson-Dirac edges, and an upper bound on the VU vector's Ξ_γ,Eg − Ξ_γ,T2g over subluminal photon edges — so that 22.5·B_min exceeds what 12 vectors and one Higgs edge can supply?
- **Setting.**
  - Dirac: separable Wilson-Dirac edges with Lemma V1 subluminality, the V0 vertex, SF strain and an ultralocal seagull.
  - Vectors: R17-9's VU vertex (P126) on subluminal photon edges in R17-9's family, with stated regularity.
  - Scalars: one Higgs edge on the U vertex (R17-4's class).
  - Axial q, m ≤ 0.01, one loop, the supplied zero-point vacuum. SM counts: 4 + 22.5 + 12.
  - Excluded: VM (R17-12's subject); μ_T2 (R17-13's subject); the M vertex; pairing; superluminal edges.
- **Prior art (count once):**
  - R17-9 (worker; its referee, when back);
  - R16-13 and vR16-13 (Theorem DT, Lemma V1, V0 as a stipulation);
  - R17-4's Lemma M and `vR17-4:7`;
  - R16-3's IBP identity;
  - R17-10's certification method (`SP/R17-10/METHOD.md`), as the template for any enclosure.
- **Removed hypothesis.** Sampling: class bounds replace sampled laws. Kept: the VU placement, V0, SF.
- **Probes.**
  - (a) The Lemma-M test for V0. Does the Dirac T₂g pair amplitude vanish where proper C₂ᵧ covariance and periodicity require it on doubler-free Wilson edges? A proof either way.
  - (b) A closed form for the Dirac birefringence B through Theorem DT's IBP, and a lower bound B_min on the class, or a law with B ≤ B_crit (the value that would let VU close).
  - (c) An upper bound on the VU vector's Ξ_γ,Eg − Ξ_γ,T2g over the stated photon class, with the T₂g row's constraint imposed.
  - (d) The certified inequality at SM counts, or an explicit point that breaks it.
  - (e) Prices.
- **FIXED readings.**
  - **V0-NONLOCAL:** a proof that V0 violates the covariance zero, so the local Dirac class needs a different vertex. Checked, then refereed.
  - **VU-CERTIFIED-CONFLICT:** a refereed certificate, with the method stated in advance, that no content in the stated class meets Ξ_Eg = Ξ_T2g = μ_E = 0 at SM counts under VU.
  - **VU-ZERO:** an explicit SM-count law under VU, all edges subluminal and local, with Ξ_Eg = Ξ_T2g = μ_E = 0 at a common light mass. Checked.
  - **OPEN:** otherwise.
- **Expectation.**
  - (a) Undecided, with a lean to V0-NONLOCAL.
    - The Wilson part enters through W′, which vanishes at k = π for (1 − cos k)-type terms.
    - The kinetic part's derivative s′ need not vanish there: for sin-type edges s′(π) = −1.
    - Whether V0's T₂g amplitude obeys the covariance zero depends on how V0 combines them. A second Lemma M is a live outcome.
  - (b)–(d) OPEN or VU-CERTIFIED-CONFLICT for the birefringence row. The sign mechanism (H_xy = W′_xW′_y, `vR16-13:17`) is fixed, but a certified vector bound over a continuous photon family may not fit in 75 minutes.
  - Removed hypothesis: sampling only. Kept: the vertex stipulations, which (a) tests.

---

**R18-4. W15's last free finite-band holes: crossing bands and merely continuous multi-shift mixing.** *(Launch only if time allows.)*

- **Plain question.** vR17-8 confirms scoped no-gos for finite mixing (analytic symbols), canonical altered generators, and regular linear field-dependent generators on isolated analytic bands. It names its steelman as "an analytic crossing-band or joint mixing/field-dependent completion" (`vR17-8:35`). Does a symmetry-protected band crossing let a field-dependent generator carry rank-3 C, so that the Reeb rank bound ≤ 1 fails?
- **Setting.**
  - Two-band analytic Bloch Hamiltonians on T³ with a symmetry-protected crossing surface or line.
  - Free quadratic matter, symmetric stress, projectable lapse, R9-9's N-type graviton.
  - Field-dependent canonical generators as in R17-8, with H-RB as the redshift bridge.
  - Excluded: interactions; non-symmetric couplings; non-projectable lapse; P64; P90.
- **Prior art (count once):** R17-8 and vR17-8 (Lemma N, MIX-1/2, FD, Theorem W repaired); R17-5 and vR17-5; R16-5; the tame Reeb-graph facts as cited in `vR17-8:29`.
- **Removed hypothesis.** Isolated bands.
- **Probes.**
  - (a) The equal-energy identity across a crossing: does the analytic-continuation step of `vR17-8:25-29` survive along the crossing branches?
  - (b) Construct the best crossing-band candidate and test rank C, then the redshift test.
  - (c) Prices.
- **FIXED readings.**
  - **ESCAPE:** an explicit crossing-band law with W2_pf, nonzero physical momentum and correct redshift. Checked.
  - **EXCLUDED-CROSS:** a refereed no-go for the stated crossing-band class.
  - **OPEN:** otherwise.
- **Expectation.** EXCLUDED-CROSS for symmetry-protected crossings. The union of analytic branches still lives on T³, and the winding obstruction is topological. The main alternative is OPEN, if the branch continuation fails at the crossing set.

---


#### C5 referee verdicts R17-9, R17-10, R17-11 and the R17-12 worker reading (recorded 02:16Z)

- **R17-9 referee: CONFIRMED WITH CORRECTIONS. Reading OPEN with the imported placement; SM-LIFTED only if VM and its G_w photon are admitted as extra stipulations.**
  - **VU:** confirmed representative-invariant with the correct continuum Maxwell amplitude. It is absolutely summable and quasi-local, not finite-range. Its positive cone shifts come from E–B interference.
  - **VM:** a genuine subluminal rank-3 SM-count zero exists after a small high-resolution retuning, leaving μ_T2 = 0.10619 unpaid.
  - **No enclosure excludes a VU solution.**
- **R17-10 referee: CONFIRMED WITH CORRECTIONS. Readings: K₆ OPEN, μ_E OPEN, JOINT not met.**
  - **Theorem F is valid** on the conditioned fast relaxation face (u = 1, b ≥ 2.9935m, s_min ≥ 1.3768m). It persists locally around each realizable sharp-turn skeleton.
  - **It does not meet CERTIFIED-CONFLICT,** because it covers neither the full relaxation nor any class-wide portion of 𝒮.
  - **The μ_E remark** rules out only constant-multiplier pointwise certificates, not certificates built along trajectories.
- **R17-11 referee: CONFIRMED WITH CORRECTIONS. Central result survives (CONSISTENT in the stipulated class).**
  - **The class:** the smooth hypersurface-orthogonal E-sector with the spatial trace equation omitted, sites riding the normals, and λ = −κe₀.
  - **The result:**
    - Q_ν = ∇^μ(W h_μν) cancels W exactly.
    - The Lemma-S parameter is zero on expanding intervals.
    - The equations reduce to GR with residual V − e₀.
    - There is no instantaneous gravitational channel at linear order.
  - **Limits:** this is an on-shell, one-point covariant embedding, not derived from the axioms or from a completed action. The Planckian vacuum inertia is hidden in an exactly tracking sector, and moving-body and anisotropic responses lie outside the class.
  - **Corrections:**
    - the universal (d-ii) no-go fails;
    - the one-row bill reduction is conditional bookkeeping: it replaces a trace counterterm with the stipulated P-vac′ bridge.
- **R17-12 (vector placement): worker reading OPEN.** Substantively, neither placement survives.
  - **VU fails W1 at O(q).**
    - Lemma F: W1 plus a symmetric stress fixes the forward stress, F = ω v_i v_j δ.
    - F1: VU's z-averaged B legs mix polarizations, giving a violation of 0.25–0.87 against a required scale of 0.01–0.06.
  - **VM breaks C₂ covariance** (Lemma C, a defect of 15–29% at q = 0.3). Its E_g row also fails Lemma F. Correction to R17-9: VM is local but non-covariant.
  - **What survives: the family VW** (per-leg σ′σ′ averaging, symmetric, trace kept).
    - Lemma X: the T₂g q = 0 vertex is fixed and equals VM's.
    - Lemma I: the O(q²) stencils are FREE law data.
  - **Under VW0,** the VM root does not carry over, and no SM zero was found in sampled solves.
  - **Prices:** P-R17-12a, b and c.

  Referee running.
- **R18-3 dropped (02:16Z).** Its premise was a certificate for the VU conflict, and VU is now excluded by W1 (R17-12, worker; referee running). Its part (a), V0 locality, is folded into R18-5 below.
- **R18-2 (EW vacuum stability under (S)): worker reading NEEDS-STABILIZER on the primary inputs. The σ condition is fragile.** Inputs RECALLED; method pre-stated in `agents/C5_R18-2_prereg.md`.
  - **SM-only running (two-loop):**
    - λ_eff crosses zero at 1.8e11 GeV;
    - M_t,crit = 170.88 GeV;
    - the tension is 2.28σ on the primary row; it ranges over 1.5–3.1σ across rows and drops below 2σ at an ambiguity of 0.64 GeV.
  - **The lattice cannot stabilize** (by a factor of at least 4e15; bounded EFT no-go, referee needed). Λ̃ ≥ 2.6e108 ρ_Λ, whatever the lattice.
  - **Stabilizers:**
    - **Higgs-portal singlet:** O(1) coupling windows, but m_S ≤ 1.5e-8/a, so one scalar-mass tuning per species unless the mass is protected.
    - **Vector-like 5-plets (n5 ≥ 2):** chirally protected, so no precision tuning. They face collider and relic costs (RECALLED).
  - **(S) prediction:** with SM content alone, (S) requires M_t(pole) ≤ 170.9 GeV.
  - **Prices:** P93 sharpened; P-r182a (singlet); P-r182b (5-plets).
  - **Archive fix (02:17Z):** the committed R17-7 runner `r177_enthalpy_orders.py` imported from a path that is not archived. It now imports from `scripts/C5/R11-3`, and its rerun matches the stored output. Reported by R18-2.

  Referee running.

### C5 Round 18, item 5 (pre-registered 02:18Z, before launch; replaces dropped R18-3)

**R18-5. Do the Dirac vertex V0 and the surviving vector family VW pass the forward test, and can SM content sit on one cone under them?**
- **Plain question.**
  - R17-12 (worker; referee running) shows that W1 plus a symmetric stress fixes the forward stress (Lemma F). That test excludes VU, and C₂ covariance excludes VM. Only the per-leg-averaged family VW survives, with free O(q²) stencils (Lemma I).
  - Every Dirac number since R16-13 uses the stipulated V0 vertex, which leaves the Wilson mass uncoupled. That includes R17-9's SM root and R17-13's μ_T2.
  - Does V0 pass Lemma F and the Lemma-M covariance zero? If not, what is the conserved Dirac vertex?
  - With conserved vertices (U scalar, a conserved Dirac vertex, VW vector), is there an SM-count zero Ξ_Eg = Ξ_T2g = μ_E = 0? The VW stencils may be used as law data, and must be stated.
- **Setting.** Wilson-Dirac D1-type edges (Lemma V1 subluminal), the U scalar vertex on one Higgs edge, VW vectors on subluminal photon edges. SM counts 4 + 22.5 + 12. Axial q, m ≤ 0.01, one loop, supplied zero-point vacuum, ultralocal seagull.
- **Excluded:** VU, VM, the M vertex, pairing, superluminal edges.
- **Prior art (count once):**
  - R17-12 (Lemmas F, C, X, I; VW) and its referee when back;
  - R17-9 and its verdict; R16-13 and its verdict (V0 and SF as stipulations);
  - R17-4 (Lemma M); R13-5 (W1 hypotheses); R17-13 (running; μ_T2).
- **Removed hypothesis:** V0 taken as a stipulation (it is now tested against Lemma F and Lemma M).
- **Probes.**
  - (a) The Lemma-F forward test and the Lemma-M covariance zero for V0. If V0 fails, construct the Dirac vertex fixed by Lemma F, including the Wilson-mass coupling.
  - (b) Signs and sizes of the conserved Dirac Ξ_T2g, Ξ_Eg and μ_E on D1, compared with V0's.
  - (c) The SM-count solve under (U, conserved Dirac, VW), with the VW stencils as declared extra knobs. Count the knobs and say which are law data.
  - (d) Prices and the bill.
- **FIXED readings.**
  - **SM-LIFTED-CONSERVED:** an explicit SM-count content with conserved, covariant, local vertices, every edge subluminal and one Higgs edge, with Ξ_Eg = Ξ_T2g = μ_E = 0 at a common light mass. Checked, with knobs counted.
  - **V0-FAILS:** a demonstration (referee required) that V0 violates Lemma F or Lemma M, with the replacement vertex stated. This can be recorded together with either of the other readings.
  - **OPEN:** otherwise.
- **Expectation.** V0-FAILS: the Wilson mass must couple to the stress, which changes the Dirac signs. The SM solve then stays OPEN.
- **R17-13 (Wilson-Dirac μ_T2): worker reading ZEROED on the letter of the clause; the 4-row SM root was not found; SIGN-DEFINITE is false.**
  - **The sign is not fixed.** μ_T2 takes both signs on D1. The Wilson piece (positive) competes with the kinetic–Wilson interference (negative).
  - **Lemma S:** for the mirror-symmetric class, μ_T2 = r⁴C₄ + O(r⁵) with C₄ < 0.
  - **Closed forms:** P and I.
  - **The zero.** D1(0.916719, 0.559627) at m = 0.01 gives μ_T2 = 0. It costs one Dirac-edge shape tuning, and the zero carries over to m = 0.001.
  - **Vertex independence.** μ_T2 depends only on the band and on SF, so the result holds whatever the vector or Dirac TT vertex placement.
  - **No SM root.** On the zero curve the Dirac μ_E is too negative at SM counts: the shortfall is 2.5–6× on the sampled ranges. A non-shape shear knob, or wider families, would be needed (P-R17-13b).
  - **Prices:** P-R17-13a (one shape tuning per Wilson-Dirac edge) and P-R17-13b.

  Referee running.
- **R18-1 (Z₂ pinch point): worker reading SCREENED for (a)–(c); (d) Theorem Z₀ offered as GAP-CLOSED.** A referee is required. The method is pre-stated in `agents/C5_R18-1_method.md`.
  - **The ensemble.** The RK ensemble exp(−βU Σγ²) is shift-action covariant (it needs P112). Detailed balance holds, and the L = 2 enumeration agrees. The registered chain is frozen at βU = ∞ (proved).
  - **The measurement.** Pinch ratio ρ = S_xz(k∥z)/S_xz(k∥y); the Gaussian control passes.
  - **The result.** ξ(βU) is finite and independent of L:

    | βU | ξ (lattice units) |
    |---|---|
    | 0.5 | ≈ 0.3 |
    | 2 | ≈ 1.2 |
    | 4 | ≈ 4 (L = 6–10) |

    This is Debye screening by γ-charges; S_γ/q² stays finite.
  - **Theorem Z₀.** Assume Lieb–Robinson bounds, a unique symmetric ground state, an E⊕T₂ readout and a strict vector gap. Then the pinch-point jump equals the static T₂ weight below the gap, in every f-sum class. So gapless TT branches visible to the readout, plus strict V/S gaps, force a pinch point.
  - **Consequence.** Finite fugacity screens. The static window needs exact emergence, at a critical point or phase boundary, or an ensemble outside the RK family. This sharpens P96.
  - **New price:** P-r18-1a.

  Referee running.

### C5 Round 18, items 6–7 (pre-registered 02:45Z, before launch)

**R18-6. One source bridge for everything? Are (S), (d-i) and completion N jointly consistent?**
- **Plain question.** S23 reads every remaining unpriced item as a question about the source/observable bridge that the axioms leave open (`AX:85-90,187`). The separately refereed candidate pieces are:
  - (S): C = E₀, "the lowest state weighs nothing" (R17-3, R17-7);
  - (d-i): the vacuum enthalpy is exchanged with site creation (R17-11);
  - completion N: the metric record is sourced by total stress, gravity's own included (R16-14).

  Written as one bridge — what gravitates, and how the metric is read from records — are they consistent together? In particular:
  - (S) subtracts e₀ while N adds gravity's own energy. Does N's gravitational-energy source include a vacuum part that (S) must also subtract?
  - (d-i) needs √h fixed per site with site creation, while set A (where N was posed) is a continuum.
- **Setting.**
  - Two arenas:
    - set C-box with site creation (P52) and the R14-5 E-sector;
    - set A (continuum, records-as-metric).
  - State the bridge as equations: the source T_eff, the metric readout, the exchange current.
  - Linear plus second order (enough for β and for the Lemma-S test).
  - Excluded: active compensation; superluminal edges.
- **Prior art (count once):** R16-14 and its verdict; R17-3, R17-7 and R17-11 with their verdicts; R13-6 and R15-2 (set A); R14-5 and R15-1; S23 §§1.0, 4.
- **Removed hypothesis:** the bridge pieces were each tested alone.
- **Probes.**
  - (a) Write the combined bridge in each arena, or show that a piece cannot be posed there (e.g. (d-i) in set A).
  - (b) Check Bianchi consistency at second order, β = 1, Λ̃ = 0 under P93, and no Lemma-S channel.
  - (c) Count the independent stipulated sentences and numbers.
  - (d) Prices.
- **FIXED readings.**
  - **JOINT-CONSISTENT:** an explicit combined bridge in a stated arena satisfying (b), with its sentence count. Checked.
  - **JOINT-CONFLICT:** a refereed demonstration that two of the pieces cannot hold together in a stated arena.
  - **OPEN:** otherwise.
- **Expectation.** JOINT-CONSISTENT in C-box with site creation (N's gravitational-energy source is Λ-free once e₀ is subtracted). (d-i) cannot be posed in set A, so set A needs pairing or a tuning for the enthalpy.

**R18-7. Set A's completion N as a construction: a well-posed, CP, records-as-metric law with β = 1?**
- **Plain question.** R16-14 (refereed) shows that a metric linear in matter records fails Mercury. Completion N (a total-stress, Landau–Lifshitz-type source) formally restores β = 1, but it is "a new, uncompleted nonlinear source/action bridge", and E2 lacks a sink action. Can set A's E1 route be completed with:
  - a nonlinear record readout that is well-posed as an initial-value problem at O(G²);
  - complete positivity (CP) of the record/measurement map;
  - consistency with the R16-4 initial-TT datum (P88);
  - β = 1 and γ = 1, with the R13-6/R15-2 noise kernel intact?
- **Setting.**
  - The E1 model (R13-6 repaired gain, R15-2 channels, P88 zero datum).
  - Post-Newtonian order O(G²).
  - The record source is total stress (matter + Landau–Lifshitz pseudotensor, or an equivalent, gauge stated).
  - Excluded: E2; strong field.
- **Prior art (count once):** R16-14 and its verdict, R16-4, R15-2, R13-6, R12-4, R6-4; Landau–Lifshitz and the post-Minkowskian iteration (RECALLED).
- **Removed hypothesis:** a metric linear in records.
- **Probes.**
  - (a) The O(G²) iteration with recorded sources: does it close? Is the readout a well-defined functional of records plus P88?
  - (b) CP of the composite (nonlinear) measurement map, at least at Gaussian order.
  - (c) β, γ, and the noise-fed corrections at O(G²).
  - (d) Does premise (iii) (non-radiative noise gravitates) become forced?
  - (e) Prices.
- **FIXED readings.**
  - **CONSTRUCTED:** an explicit E1 + N law at O(G²) with a well-posed readout, CP at Gaussian order, and β = γ = 1. Checked.
  - **OBSTRUCTED:** a refereed demonstration that no records-as-metric readout in a stated class gives β = 1 with CP.
  - **OPEN:** otherwise.
- **Expectation.** CONSTRUCTED at O(G²) with the gauge-dependence of the LL source as the main caveat, and premise (iii) forced. That would make R15-2's constraint-energy overshoot live again.
- **R18-4 (W15 crossing bands): worker reading EXCLUDED-CROSS** for every two-band analytic crossing law, including unprotected Weyl points. Continuous multi-shift mixing is OPEN. A referee is required.
  - **Lemma S0:** momentum is continuous through conical tips.
  - **Theorem WX:** the continuation runs on the orientation double cover (again a T³), giving rank C ≤ 1.
  - **Lemma RB-X:** H-RB forces rank C = 3 at any positive homogeneous extremum, including massless cones.
  - **Corollary:** no redshifting momentum.
  - **Lemmas X1/X2:** analytic laws have no odd orientation monodromy.
  - **RECALLED facts** (to be accepted or replaced): tame Reeb, half-branch evenness, stratification.
  - **No new price;** P64, P90 and P124 are unchanged.
  - **Archive fix (02:47Z):** the committed R17-8 runner imported from the non-archived `recheck/R16-5`. It now points at `scripts/C5/R16-5`, and its rerun is byte-identical. Reported by R18-4. An audit of every archived runner's sys.path inserts found no other missing directory.

  Referee running.

### C5 Round 18, item 8 (pre-registered 02:49Z, before launch)

**R18-8. W7 at infinity: does the off-box tail survive in the global Poincaré charges, and is that observable?**
- **Plain question.**
  - R17-2 (refereed OPEN) shows that, in the bulk at leading order, W7's forced translation term is the inverse of a linearized-GR Coulomb dressing.
  - Its matter coupling can be moved into non-local constraint multipliers, so no instantaneous bulk interaction is demonstrated.
  - What is lattice-specific is relocated to the global boundary algebra and the q·v = 0 shell, and nobody has computed it.
  - Do the asymptotic (ADM) Poincaré charges of a system containing edge quanta satisfy the Poincaré algebra? If not, the defect is a boundary-charge anomaly. Is it observable, e.g. as a frame-dependent total momentum or a mass–energy mismatch for bound systems with edge content?
- **Setting.**
  - R16-8/R16-12/R17-2's completion with S(1.4)/G(1.4) matter (v_max stated).
  - Linearized gravity with asymptotically flat falloff.
  - ADM charges (E, P, J, K) as surface integrals; standard algebra assumed for the gravitational part.
  - Degree 3 in the Killing sector.
  - Excluded: nonlinear gravity, pairing, P90.
- **Prior art (count once):**
  - R17-2 and its verdict (escapes 2, 3 and 5; Lemmas D and H);
  - R16-12 and its verdict (B3, presentation-dependent);
  - R16-8 and its verdict (the shell at infinity, Lemma F);
  - Regge–Teitelboim boundary terms and Beig–Ó Murchadha asymptotic Poincaré charges (RECALLED).
- **Removed hypothesis:** bulk-only (compact smearings).
- **Probes.**
  - (a) The surface terms of R17-2's dressing W, and their contribution to {K, H}, {K, P} and {K, K} at degree 3.
  - (b) Does the asymptotic algebra close? If not, give the anomaly in terms of Q_D (the defect charge of edge quanta).
  - (c) An observable form of the anomaly, and its size for a body with edge content at a stated population (thermal at T, or a primordial relic).
  - (d) Prices.
- **FIXED readings.**
  - **CLOSES:** an explicit degree-3 asymptotic algebra that closes with the surface terms. Checked.
  - **ANOMALY:** a refereed demonstration that the asymptotic algebra fails by a term ∝ Q_D, with an observable form.
  - **OPEN:** otherwise.
- **Expectation.** ANOMALY ∝ Q_D in {K, P}. That would be an edge-quantum Lorentz violation at infinity, unobservable for any thermal population below ~1e19 GeV. That makes W7 a priced, practically invisible defect.
- **R18-5 (V0 and VW; SM on one cone): worker readings V0-FAILS and SM-LIFTED-CONSERVED (met on the letter).** A referee is required for both.
  - **V0 fails Lemma F.** Its forward stress is s_is_j/E instead of p_ip_j/E. Off the box the mismatch is O(1), and the mirror boxes even get the wrong sign. V0 is spin-½ covariant: Lemma M′ shows spinors permit a face amplitude.
  - **Replacement UD = ½(p_j∂_ih + p_i∂_jh).** It is the unique Lemma-F vertex in the one-vector family. It couples the Wilson mass and equals V0 inside the box.
  - **Correction (P-R18-5a):** every Dirac Ξ number since R16-13 used a non-conserved vertex. R16-13's birefringence obstruction belongs to V0; under UD the birefringence spans −5.2e-4 to +2.4e-3. R17-13's μ_T2 result is unaffected.
  - **The SM-count root** under U + UD + VW needs a signed VW stencil (λ = 0.0045 < ¼):
    - content: 4 scalars + 22.5 Dirac + 12 vectors, one Higgs edge, every edge subluminal;
    - Ξ_Eg = Ξ_T2g = μ_E = 0 at m = 0.01 (residual ~8e-6 at N = 192), and also at m = 0.001;
    - 3 tunings: two edge shapes plus one placement datum;
    - μ_T2 = +0.091 is left unpaid.
  - **Nonnegative stencils** stall.
  - **Prices:** P-R18-5a, b and c.

  Referee running.

#### C5 referee verdicts R17-12, R17-13, R18-2, R18-4 (recorded 03:00Z; codex gpt-5.6-sol, xhigh)

- **R17-12 referee: CONFIRMED WITH CORRECTIONS. Reading: both FORCED labels are recorded through their exclusion disjuncts; substantively NEITHER.**
  - **Neither placement passes.**
    - VU violates the necessary forward Ward value (Lemma F).
    - VM's E_g row violates it too, and VM's one-sided placement breaks C₂ covariance.
  - **What consistency fixes.** W1 fixes the q = 0 T₂g vertex to VM's value. Covariance replaces VM's one-sided placement with a symmetric VW-type stencil.
  - **What stays free.** Normalized symmetric stencils differ by identically conserved superpotentials, so their O(q²) placement is free.
  - **Scope.** This is a necessary-order, class-scoped result. Exact W1 completion and general E_g uniqueness remain open. The numerical ranges and the scope of VW uniqueness are corrected.
- **R17-13 referee: CONFIRMED WITH CORRECTIONS. Reading ZEROED; the four-row SM problem is OPEN; SIGN-DEFINITE is false.**
  - **Confirmed:** Forms P and I are exact under SF. Lemma S holds with the added nonzero-overlap hypothesis, giving C₄(0) < 0. D1 takes both signs.
  - **The zero.** D1(0.916719266558, 0.55962727) at m = 0.01 has a transversal μ_T2 = 0. That costs one continuous edge-shape tuning.
  - **Not enclosed.** The μ_E deficit (2.5–6×) is not enclosed.
- **R18-2 referee: NOT CONFIRMED (the NEEDS-STABILIZER). Reading OPEN.**
  - **Confirmed:** M_t,crit = 170.8776 GeV, λ_min = −0.01129, and λ_eff = 0 near 1.81e11 GeV, reproduced independently.
  - **Why OPEN:** the recalled inputs favour SM metastability but do not establish a robust > 2σ conflict.
  - **Stabilizers:**
    - Ordinary Planck-suppressed terms and the two tested lattice dispersions fail.
    - A singlet stabilizes, with one unprotected scalar-mass tuning.
    - Chirally protected vector-like 5-plets also stabilize.
  - **The conditional.** If (S) is stipulated, the electroweak vacuum must be global to dark-energy accuracy. None of this makes (S) axiomatic.
- **R18-4 referee: CONFIRMED WITH CORRECTIONS. Reading EXCLUDED-CROSS.**
  - **The class:** nontrivial two-band real-analytic Bloch Hamiltonians on T³ under the stated hypotheses.
  - **The mechanism:**
    - momentum eigenvalues extend continuously through conical crossings;
    - on the orientation double cover, every nonflat branch carrying momentum has rank C ≤ 1;
    - H-RB needs rank C = 3.
  - **Coverage:** smooth swaps, folded bands, protected nodal crossings, mixed crossings and Weyl points.
  - **Still OPEN:**
    - continuous multi-shift mixing;
    - N > 2 braiding;
    - joint mixing with field dependence;
    - the other excluded classes.
- **R18-6 (joint bridge): worker reading JOINT-CONSISTENT in C-box-E; set A OPEN.**
  - **The bridge (C-box-E):** λ = −κe₀[H] (that is, (S)); Q = ∇(W h) (that is, (d-i)); and N stated on the gravitating stress.
  - **Checks in C-box-E:**
    - Bianchi gives g = 0 on every slice that expands somewhere, so the equations reduce exactly to GR on T_m − (V − e₀)g.
    - A static star is exactly TOV.
    - β = γ = 1.
    - Λ̃ = 0 under P93.
    - There is no Lemma-S channel.
  - **Count:** 3 sentences, 0 numbers.
  - **J1 (wording versus conflict).** N read literally ("total stress", vacuum included) forces W = 0, so it must be stated on the gravitating stress. The referee rules whether this is a wording fix or a conflict.
  - **J2.** The graviton must be GR's self-coupled field. If gravity is quantum, its zero-point sector lies inside H, and (S) together with (d-i) removes it with no number.
  - **Set A:**
    - (d-i) cannot be posed there.
    - Matter's vacuum has W = 0 by Poincaré invariance.
    - N's source includes the record noise (up to 1e12–1e19 ρ_Λ), which no scalar rule removes. That makes premise (iii) and R15-2's budget the live constraint.
  - **Prices:** P-r186a (N on the gravitating stress), P-r186b (J2), P-r186c (set A meter stress).

  Referee running.

### C5 Round 18, items 9–10 (pre-registered 03:01Z, before launch)

**R18-9. All four cone/shear rows with SM content under conserved vertices: E_g = T₂g = μ_E = μ_T2 = 0?**
- **Plain question.**
  - R18-5 (worker; referee running) finds a conserved-vertex SM-count root (U + UD + VW, signed stencil) that zeroes three rows and leaves μ_T2 = +0.091.
  - R17-13 (refereed ZEROED) shows μ_T2 can be zeroed by one Dirac-edge shape tuning on D1. At SM counts the μ_E budget fought it under V0/VM.
  - With UD's different Dirac Ξ and the signed VW stencil as an extra knob, can all four rows be zeroed at SM counts? How many knobs does that take?
- **Setting.**
  - The R18-5 content and vertices: 4 scalars U, 22.5 Dirac UD, 12 vectors VW with a signed stencil.
  - One Higgs edge; all edges subluminal.
  - m = 0.01 and 0.001.
  - Knobs: edge shapes plus stencil, declared.
  - Excluded: VU, VM, V0, the M vertex, pairing.
- **Prior art (count once):** R18-5 (worker) and its referee when back, R17-13 and its verdict, R17-12 and its verdict, R16-9, R17-4 and R14-3.
- **Removed hypothesis:** μ_T2 left unpaid.
- **Probes.**
  - (a) Four-row solve with 4 declared knobs (scalar edge, Dirac b, Dirac r, stencil); with 5 if needed (photon edge).
  - (b) Transversality, subluminality and resolution checks.
  - (c) Off-axis rows (R17-4's K₆ for scalars; face2 ≡ T₂g check for UD and VW) at the root, if time allows.
  - (d) The bill.
- **FIXED readings.**
  - **FOUR-ROW-ZERO:** an explicit SM-count content with conserved vertices, all subluminal, all four rows zero at a common light mass. Checked, with the knob count.
  - **FOUR-ROW-CONFLICT:** a demonstration (refereed if class-wide) that the four rows cannot be zeroed together in the stated families.
  - **OPEN:** otherwise.
- **Expectation.** FOUR-ROW-ZERO with 4 knobs. UD's smaller Dirac μ_E pull plus the signed stencil should relax R17-13's budget shortfall.

**R18-10. A Z₂ ensemble with dipole-hyperuniform charges: does conserving the γ-dipole produce the pinch point that finite fugacity screens?**
- **Plain question.**
  - R18-1 (worker; referee running) finds that the RK Z₂ ensemble with finite charge fugacity is screened (Debye).
  - Identity V says a pinch point needs S_γ = o(k²): the charges must be dipole-hyperuniform.
  - If the dynamics conserves the total γ-dipole (fracton-like mobility restrictions, a local constraint not a global one), can the static readout develop a pinch point at finite fugacity?
  - That would be a static window outside R18-1's RK family that does not need exact emergence.
- **Setting.**
  - N0914's slots with the mod-2 law and the shift action (P112).
  - An RK ensemble whose move set conserves Σ x γ(x) (dipole) in addition to Gn mod 2, with weight exp(−βU Σγ²).
  - L = 6–12.
  - Observables as in R18-1 (ρ, ξ², S_γ/q², S_γ/q⁴).
  - Excluded: spectra; integer lifts.
- **Prior art (count once):**
  - R18-1 (and its referee); R17-6 and its verdict (Identity V, Theorem Z; R18-1's Z₀);
  - R17-1; N0914;
  - fracton dipole conservation and pinch points (Pretko; Prem–Vijay–Chamon; RECALLED).
- **Removed hypothesis:** charge moves without dipole conservation.
- **Probes.**
  - (a) Construct a local dipole-conserving move set within the mod-2 sector, and check detailed balance and ergodicity at small L.
  - (b) Measure ξ²(βU, L) and S_γ/q², S_γ/q⁴.
  - (c) If a pinch point appears, check the readout's helicity content: is it T₂ (tensor) and not scalar?
  - (d) Prices: a dipole-conservation law as a new conserved structure (`AX:57-61`).
- **FIXED readings.**
  - **PINCH-PRESENT:** finite βU with ξ growing as L (finite-size scaling), S_γ = o(k²), and a T₂ readout. Checked.
  - **SCREENED:** ξ finite at every finite βU tested. Checked.
  - **OPEN:** otherwise, including non-ergodic moves.
- **Expectation.** PINCH-PRESENT. Dipole conservation makes the charges hyperuniform (S_γ ∝ k²) at any fugacity. It costs a new conservation law, and the result is a static window only.
- **R18-7 (set A completion N): worker reading CONSTRUCTED** in a stated scope: static and quasi-static, O(G²), harmonic gauge.
  - **The law E1 + N_c:**
    - The record is unchanged.
    - The source is (−g)J + Λ[h], where Λ is the LL pseudotensor plus the harmonic-gauge term.
    - A causal conserving projection Π is added.
    - The readout is □h = −16πG τ_rec.
  - **What it gives:**
    - G = 8πG T_eff exactly.
    - The readout is well-posed: each order is a flat retarded wave equation.
    - CP holds: the instrument is R13-6's plus record-controlled classical feedback.
    - β = γ = 1 (point mass: g₀₀ = −1 + 2M/r − 2M²/r²).
  - **Corrections to R16-14:**
    - N as written does not close at O(G²): the gain does not commute with the gravitational force, so Π is required.
    - N̄ (mean-metric feedback) is not CP, which drops it from owner Q2.
  - **Premise (iii):** the static active density is (2a − 8)|u₁|, which vanishes only at insertion weight a = 4.
  - **Caveat:** harmonic gauge conflicts with P-r15b. The pure-gauge S/V noise grows secularly, so the time-dependent noise terms are not gauge-invariant yet.
  - **Prices:** P-r18-7a (Π), P-r18-7b (readout gauge), P-r18-7c (weight a); P88 extended.

  Referee running.

### C5 Round 18, item 11 (pre-registered 03:10Z, before launch)

**R18-11. Set A's E1 + N in Poisson gauge: does the time-dependent noise behave gauge-invariantly at O(G²), and is premise (iii) live?**
- **Plain question.** R18-7 (worker; referee running) constructs E1 + N_c at O(G²) in harmonic gauge. Static and quasi-static: β = γ = 1, CP, well-posed. But in harmonic gauge the realised scalar/vector noise carries secularly growing pure-gauge parts. These conflict with R15-2's Poisson-gauge record (P-r15b), and the time-dependent noise-fed O(G²) terms were not computed gauge-invariantly. In Poisson gauge, or gauge-invariantly:
  - Is the O(G²) law well-posed and CP?
  - What is the active gravitating density of the noise for each insertion weight a?
  - Does R15-2's constraint-energy overshoot (|u₁| up to ~1e12 ρ_Λ) return?
- **Setting.**
  - E1 (R13-6 repaired gain, R15-2 channels, P76, P88), with N_c's conserving projection Π.
  - Poisson-gauge readout, or Bardeen-type gauge invariants.
  - O(G²); the static, quasi-static, and stationary-noise sectors.
  - Excluded: E2; strong field; FRW, unless time allows.
- **Prior art (count once):** R18-7 (worker), R18-6 (set A part, worker), R16-14 and its verdict, R15-2 and its verdict (premise (iii), |u₁|), R16-4, R13-6.
- **Removed hypothesis:** harmonic gauge.
- **Probes.**
  - (a) The construction in Poisson gauge, or a gauge-invariant reformulation, at O(G²).
  - (b) The noise's active density, ⟨T_eff⁰⁰ + 3p⟩, as a function of a. Is it gauge-invariant? Which a makes it vanish, and is that value natural?
  - (c) The budget against ρ_Λ over R15-2's window.
  - (d) CP and well-posedness.
  - (e) Prices.
- **FIXED readings.**
  - **NOISE-SAFE:** a gauge-invariant O(G²) result in which the noise's active density is below ρ_Λ over a stated window for a natural, stated a, with CP. Checked.
  - **NOISE-OVERSHOOT:** a refereed demonstration that for every a in a stated class, the gauge-invariant active density exceeds ρ_Λ over the whole window.
  - **OPEN:** otherwise.
- **Expectation.** OPEN. The a = 4 cancellation is a harmonic-gauge statement, and the gauge-invariant density is likely a different combination. The main risk is that no natural a works, which would revive R15-2's overshoot as a set A wall.
- **R18-8 (W7 at infinity): worker reading ANOMALY, pending the referee.**
  - **Theorem A (degree 2).** The asymptotic Poincaré algebra fails by the defect charge: {K_b, P_c} = δ_bc H + Q_D,cb. This holds for every completion whose added terms have degree ≥ 3. Checked by symbolic algebra and by a 2048-site lattice operator identity.
  - **Lemma S∞.** One shell term cancels the defect in the bulk constraints and reproduces it in the boost charge, so these are the same statement. Correction: R16-8 Lemma F's "Consequence" applies only to the weakly-zero generator.
  - **Lemma T.** The tail of a point defect is a mass dipole (M·a = −Δ) plus gauge. Corollaries N and N′: no boundary functional and no matter-moment redefinition repairs the algebra.
  - **Theorem A3 (degree 3).** The anomaly is F(Q_D) in the dressed presentation, conditional on F's boundary terms. This corrects R17-2's Jacobi lemma.
  - **Observable.** A body with edge content has a direction- and velocity-dependent far-field mass. Thermal populations are invisible below ~1e18 GeV. Relic populations are not bounded.
  - **Prices:**
    - P-W7anom: accept the anomaly.
    - P-W7edge0: physical states carry no edge quanta.
    - R17-2's P-W7bdy reduces to P-W7anom.

  Referee running.

#### C5 referee verdicts R18-1, R18-5, R18-6 (recorded 03:17Z; codex gpt-5.6-sol, xhigh)

- **R18-1 referee: CONFIRMED WITH CORRECTIONS. (a)–(c) demoted to OPEN; (d) GAP-CLOSED for the strengthened, uniformly Lieb–Robinson-local class.**
  - **What was observed:** no finite-size-sharp pinch point through βU = 4. Data for βU ≤ 3.5 are consistent with screened finite widths.
  - **Why OPEN:** the βU = 4 runs mix too slowly and are not seed-stable enough to certify a fitted ξ. βU = ∞ is exactly sharp but frozen.
  - **Theorem Z₀ is confirmed** for uniformly LR-local, cubic-covariant families with a unique symmetric ground state, a local E⊕T₂ readout and a strict vector gap. In that class, a statically visible gapless T₂ branch forces a directional contrast in every f-sum class.
    - The contrast is bracketed by nested cutoff weights rather than equal to one "weight below the gap".
    - It does not close the broader quasi-local H1 class.
- **R18-5 referee: CONFIRMED WITH CORRECTIONS. V0-FAILS confirmed; SM-LIFTED-CONSERVED holds if signed VW stencils are admitted, which the referee reads the unqualified setting as indicating; otherwise OPEN.**
  - **V0 fails the forward Ward value.** At an independent check point it gives +0.2654 where −0.2654 is required. VW passes the forward test to 1.7e-16.
  - **UD** is the unique forward-correct Dirac vertex within the stipulated strain-flow family 𝔇, and it couples the Wilson mass. Neither the family restriction, the pair block, the O(q²) placement nor exact W1 completion is derived.
  - **The SM-count three-row axial zero** at m = 0.01 is well resolved. It costs 3 tunings.
  - **Unpaid:** μ_T2 ≈ 0.0911, off-axis closure, and exact conservation.
- **R18-6 referee: NOT CONFIRMED (the JOINT-CONSISTENT). Literal reading JOINT-CONFLICT** (expanding arena, W ≠ 0).
  - **Literal N conflicts with (d-i).** Literal N is sourced by the total matter-plus-vacuum stress plus gravitational self-stress. Bianchi then requires Q = 0, which forces W = 0 on any connected expanding slice.
  - **N_red is a new completion, not a wording fix.** Redefining N to include the E/creation receiver, or to use only the net gravitating stress, gives a consistent bridge. In that modified net-source bridge:
    - each connected slice component that expands somewhere reduces to exact classical GR (TOV without W);
    - β = γ = 1;
    - Λ̃ = 0 under P93;
    - there is no Lemma-S channel;
    - it takes three clauses and zero fitted numbers.
  - **Still open:** the quantum J2 step, full quantum-gravity completion, and set A noise completion.
- **R18-10 (dipole-conserving Z₂ ensemble): worker reading OPEN.** No pinch point was found anywhere. SCREENED is checked for βU ≤ 2.5, but βU = 3–3.5 is not seed-stable and the registered moves are non-ergodic. The method is pre-stated in `agents/C5_R18-10_method.md`.
  - **Dipole = labels.** The γ-dipole equals −½ × the six slot-label totals. So dipole conservation is six global numbers and imposes no local Gauss law.
  - **The fixed sector is screened,** with R18-1's ξ.
  - **The registered moves fragment:** they conserve 3L planar counts.
  - **Diagnostic correction.** Planar conservation laws fake an axis pinch (ρ = 0 on the axes) while the off-axis channels stay screened. Every pinch claim must check face and body directions too.
  - **The expectation's mechanism fails.** S_γ ∝ k² already holds in screened ensembles; a pinch needs o(k²).
  - **Prices:** P-r18-10a, b and c. P96 sharpened: move conservation laws cannot replace exact charge suppression.

  Referee running.

### C5 Round 18, item 12 (pre-registered 03:37Z, before launch)

**R18-12. Relic edge quanta: how many can exist, and does the W7 anomaly or anything else bound them?**
- **Plain question.**
  - R18-8 (worker; referee running) finds the W7 tail survives as an asymptotic Poincaré anomaly ∝ Q_D: a direction- and velocity-dependent far-field mass for bodies with edge content.
  - Thermal populations are invisible below ~1e18 GeV. But number-conserving matter can keep any initial edge population (`vR16-12:19`), and no relic population has been bounded.
  - Edge quanta are Planckian (≥ 1.4/a ≈ 1.7e19 GeV) and carry lattice Lorentz violation.
  - What populations survive from a hot early universe or reheating? Do they decay, annihilate or redshift away? What observational bounds apply?
- **Setting.**
  - Box-law matter with subluminal edges (S/G(1.4), D1): edge quanta are states with |k_i| > b/a.
  - Interactions:
    - gauge (Peierls), giving an annihilation and scattering cross-section into box quanta;
    - gravity.
  - Cosmology: reheating temperature T_RH as a parameter, with standard expansion.
  - Observables:
    - (i) R18-8's mass anomaly (a gravitational test, e.g. a frame-dependent equivalence-principle signal);
    - (ii) the edge quanta's own energy density as dark matter;
    - (iii) the matter-sector Lorentz-violation bounds (RECALLED);
    - (iv) BBN and CMB energy-injection bounds.
- **Prior art (count once):** R18-8, R16-12 and its verdict (population), R16-8, R17-2, SUMMARY §17 (the root obstruction), R9-1, and the relic-abundance literature (RECALLED; e.g. Planckian relics, freeze-out).
- **Removed hypothesis:** thermal populations only.
- **Probes.**
  - (a) Number-changing processes for edge quanta: decay to box quanta (is it allowed kinematically and by symmetry?), annihilation, and scattering out of the edge.
  - (b) The relic abundance as a function of T_RH, including a T_RH ≥ 1/a case.
  - (c) The bounds on that population from (i)–(iv).
  - (d) Whether P-W7edge0 ("physical states carry no edge quanta") is a dynamical consequence or a stipulation.
  - (e) Prices.
- **FIXED readings.**
  - **SELF-CLEANING:** edge quanta decay or annihilate efficiently, so the relic population is below every bound for any T_RH. Checked.
  - **BOUNDED:** a stated maximum T_RH, or initial population, above which a stated observable is violated. Checked.
  - **OPEN:** otherwise.
- **Expectation.** SELF-CLEANING. Edge quanta can scatter into box states by Peierls vertices (umklapp), so they cannot be stable. The main risk is a conserved edge number in some sector.
- **R18-7 referee: CONFIRMED WITH CORRECTIONS. CONSTRUCTED, only in the stated weak-field harmonic static/quasi-static scope** (recorded 03:37Z).
  - **What holds:** the retarded Π gives a causal, conserved, order-by-order records-to-metric law through O(G²). h₁ is E1. The record-conditioned instrument is CP. Static spherical β = γ = 1 after mass renormalization.
  - **R16-14's unprojected completion is genuinely non-conserving.** The worker gave the wrong exact commutator and coefficient for it.
  - **Limits:**
    - the a = 4 cancellation holds only for the homogeneous static scalar channel;
    - the canonical Π is non-local;
    - the old Poisson-gauge kernel is not preserved;
    - no gauge-invariant, time-dependent O(G²) noise result exists yet.
- **R18-11 (E1+N, gauge-invariant noise): worker reading OPEN.** A NOISE-OVERSHOOT candidate is offered for 𝒜₂ (a = 2).
  - **Theorem G:** the readout gauge is physical in set A. Only a = 2 (the record √−g T^{μν}) gives a gauge-independent mean source.
  - **Lemma P:** the noise's mean energy density is pinned at zero for E1's zero start. This gives readings (P) and (U).
  - **Active density at a = 2:**
    - −4u₁ under (U);
    - ≤ −(1 + ⟨x²⟩)u₁ under (P).
    - It is repulsive, with |ρ_act| ≥ 1.17–4.68 ρ_Λ across R15-2's window.
    - Mercury excludes ℓ ≲ 2.5e-8 m (strict).
  - **Zeros need tunings:** a ≠ 2 (gauge-dependent), a tuned T_⊥ fraction, or a spectrum-tuned a*.
  - **Consequences:**
    - R18-7's a = 4 zero does not survive a gauge-proper treatment;
    - R15-2's overshoot returns as a set A wall;
    - an FRW corner window at ℓ ≳ 4.6e-6 m is suggested only.
  - **Prices:** P-r1811a (a = 2), P-r1811b (noise energy history); P-r15c is now necessary.

  Referee running.
- **R18-9 (four rows at SM counts): worker reading FOUR-ROW-ZERO on the letter of the clause.** A referee is required.
  - **The root (m = 0.01):**
    - 4 scalars on G_w(2.526151), U vertex;
    - 22.5 Dirac fields on D1(0.909103, 0.555604), UD vertex;
    - 12 vectors on γG_w(2.9435, 0.198093), VW vertex with signed stencil a = −0.176095.
    - Ξ_T2g = Ξ_Eg = μ_E = μ_T2 = 0 to ≤ 7e-11 at N = 224. Every edge is subluminal. The root holds at m = 0.001.
  - **Cost:** 4 tunings (b_s, b_f, r, a), plus a narrow photon window b_γ ≈ 2.936–2.947. The window may count as a fifth tuning.
  - **Mechanism:**
    - μ_T2 comes from the Dirac fields only, so the Dirac edge must sit on R17-13's zero curve.
    - The signed stencil decouples the photon's Ξ from its μ_E.
    - The expectation's UD-μ_E mechanism was wrong: μ_E is vertex-independent.
  - **Off-axis:** face2 ≡ T₂g holds for scalars but fails for UD Dirac (~7e-5). VW was not computed. So the off-axis rows remain unpaid.
  - **Still unpaid:** the off-axis rows, the LV tadpole (paid by (d-i) in 𝒟), the CC, and exact W1.
  - **Prices:** P-R18-9a (photon window), P-R18-9b (UD off-axis).

  Referee running.

### C5 Round 18, item 13 (pre-registered 03:40Z, before launch)

**R18-13. The off-axis graviton rows at the SM root: how many more conditions, and can shape or placement pay them?**
- **Plain question.**
  - R18-9 (worker; referee running) zeroes the four axial rows at SM counts with conserved vertices (U, UD, VW with a signed stencil).
  - The off-axis rows are unpaid:
    - for scalars, face2 ≡ T₂g and face1 adds K₆ (R17-4);
    - for UD Dirac, face2 ≠ T₂g (~7e-5);
    - VW is defined only for q ∥ z (R17-12), so its off-axis extension is a further law datum.
  - At the SM root:
    - How many independent off-axis conditions are there (face1, face2, body)?
    - Can the remaining freedom pay them: the Dirac pair block, the off-axis VW stencils and UD's O(q²) placement (P-R18-5b/c)?
    - Or do they need non-shape knobs?
- **Setting.**
  - R18-9's root content and vertices.
  - VW extended off-axis covariantly (stencils per symmetry type, stated).
  - UD with its O(q²) placement data.
  - Off-axis directions: face (110) and body (111), m = 0.01, one loop.
  - Excluded: pairing; superluminal edges; M; V0.
- **Prior art (count once):** R17-4 (off-axis formula; U identities; K₆), R17-10 (Theorem F), R18-9, R18-5, R17-12 (Lemma I, stencils free), R13-8 (rank-4 TT space).
- **Removed hypothesis:** axial q only.
- **Probes.**
  - (a) An off-axis extension of VW and UD that keeps covariance and the forward test.
  - (b) The face1, face2 and body rows at the R18-9 root, per species and in total.
  - (c) The count of independent extra conditions, and a solve using the off-axis placement data (declared knobs) together with the axial rows.
  - (d) The bill.
- **FIXED readings.**
  - **ALL-ROWS-ZERO:** an explicit SM-count law with conserved covariant vertices, all subluminal, and the axial and off-axis rows all zero at a common light mass. Checked, with the knob count.
  - **OFF-AXIS-COUNTED:** the number of extra conditions is established (proved or checked), with a stated payment route, but no joint root is found.
  - **OPEN:** otherwise.
- **Expectation.** OFF-AXIS-COUNTED with two extra conditions (face1 and face2), payable by off-axis stencil data. The bill then becomes ~6 tunings for the SM gravity block, plus the charge block.

#### C5 referee verdicts R18-8, R18-10 (recorded 03:52Z; codex gpt-5.6-sol, xhigh)

- **R18-8 referee: CONFIRMED WITH CORRECTIONS. Reading ANOMALY.**
  - **The anomaly.** In the standard Regge–Teitelboim asymptotically flat phase space with free current-aligned S/G matter, the improved Killing generators have vanishing degree-1 pieces. So the degree-2 algebra contains {K_b, P_c} = δ_bc H + Q_D,cb, with defect moments in the rotation sector. {K,H}, {K,K} and {P,P} close.
  - **No completion removes it** if the completion starts at degree 3.
  - **Corrections:**
    - Lemma T survives, but the surface-sign explanation is reversed.
    - The no-repair corollaries are narrow.
    - F(Q_D) stays conditional on the dressing's boundary domain.
    - The observable is a frame-dependent combination of the ADM translation charges, not an invariant mass. Its thermal suppression rests on the stated population and scale assumptions.
- **R18-10 referee: CONFIRMED WITH CORRECTIONS. Reading OPEN.**
  - **Confirmed:**
    - γ-dipole conservation by local XOR moves is exactly the conservation of six global label totals.
    - The fixed-N half-filled sector through βU ≤ 2.5 is consistent with R18-1's screened width; no pinch point was found.
    - M1 is rigorously fragmented.
  - **Limits:**
    - M2 is proven sector-ergodic only at L = 2.
    - Higher couplings are mixing-limited.
    - Subsystem conservation can manufacture exact axial zeros, so off-axis checks are required.
  - **Not shown:** that all dipole-conserving Z₂ ensembles are screened.

### C5 Round 19 (pre-registered 03:53Z from S26 §7 (agents/C5_S26_synthesis.md), text fixed before any run; R19-1..3 launched now)


**Rules (as rounds 2–18, `TESTS:5688-5706`, `TESTS:6395-6406`).**
- Probes on Opus 5.5 at xhigh. Every FAIL, EXCLUDED, OBSTRUCTED, CONFLICT or no-go goes to codex gpt-5.6-sol (xhigh) before it is recorded.
- Prices are named, never adopted. Prior art is grepped first and counted once. Hypotheses come before titles. Numbers from memory are labelled RECALLED.
- Every law states its whole-zone v_max, gauge fields included. Every count states its counterterm basis. Every Λ mechanism says what is enforced and what is stipulated.
- Round-18 rules kept: locality of vertices (Lemma M, with Lemma M′ for spinors); number-free ≠ forced; bounded classes for spectra; certificates stated in advance.
- **New (from round-18 verdicts):**
  - **Exhaustive forks.** Every fork of the form FORCED-X / FORCED-Y has an explicit NEITHER branch (`vR17-12:17`).
  - **Literal first.** A registered piece is tested as written. A restatement is reported as a new completion and priced (`vR18-6:5`).
  - **Signs of law data.** Each registration says whether law-data weights may be signed (`vR18-5:16-20`).
  - **Equilibration stated in advance.** Any MC reading states its equilibration criterion (round trips, seed stability, ladder) before the run (`vR18-1:9`).
  - **Same-component controls.** A control measures the same component and normalization as the observable (`vR18-1:7`).
  - **Off-axis pinch checks.** Any pinch claim reports the face and body channels, not the axes only (R18-10's correction to R18-1's diagnostic, `TESTS:6982`; `vR18-10:11`).
  - **Thresholds recomputed.** A printed window or threshold is recomputed in exact or interval arithmetic before it is quoted (`vR18-2:11`).
  - **Invariance, not covariance.** Isotropy claims cite the invariance of the state (`vR18-6:7`).
  - **Vertex conservation.** Every TT or stress vertex passes the Lemma-F forward test, or is labelled non-conserved (`vR17-12:5`; `vR18-5:3`).

**Timing.** Each item is sized for about 75 minutes of worker time. No new probe starts after 09:57Z; the campaign ends at 10:57Z. At about 03:30Z that leaves room for about five more rounds.

**Overlap check (running items are not duplicated).**
- R18-9 (worker FOUR-ROW-ZERO) covered the four axial rows at SM counts. **R18-13 (running) covers the off-axis rows at the SM root. No round-19 item drafts either; S26's earlier R19-4 is withdrawn.**
- R18-10 (refereed OPEN) covered static dipole-conserving ensembles. R19-1 covers dynamics (the dispersion of the tensor branch), on R18-1's ensemble.
- R18-11 (worker OPEN; referee running) covers set A on a Minkowski background in Poisson gauge. R19-2 covers only the FRW step its report names as decisive (`rR18-11:271`).
- R18-8 (refereed ANOMALY) covers W7's algebra, and **R18-12 (running) covers the relic population, its bounds and whether P-W7edge0 holds dynamically. No round-19 item drafts either.** (An earlier S26 draft of a W7 relic item was withdrawn when R18-12 was registered.)
- R18-6 covers the classical bridge. R19-3 covers only the quantum J2 step that `vR18-6:7` leaves open.

**Priority.**
1. R19-1 (graviton dynamics) and R19-3 (J2), in parallel, now.
2. R19-2 (set A in FRW), after R18-11's referee confirms Theorem G and Lemma P, or now with its readings conditional on them.
3. (R19-4 withdrawn: R18-13 covers it.)

---

**R19-1. Graviton production from the Z₂ window: can a tensor branch be light-like at or near the RK point?**

- **Plain question.**
  - Z₀ (refereed, bounded) says a statically visible gapless tensor branch with a strict vector gap forces a pinch point. R18-1 (refereed OPEN) and R18-10 (refereed OPEN) found no such static window yet.
  - A static pinch point is necessary, not sufficient. Production needs a light-like branch, ω = ck.
  - At a Rokhsar–Kivelson (RK) point the quantum dynamics is similar to the classical Markov generator of the same ensemble. The single-mode (Bijl–Feynman) bound gives ω(k) ≤ f(k)/S(k), where f is the f-sum (R17-1: k⁰ or k² for the Z₂ models) and S the static structure factor.
  - With S finite at a pinch point, f ∝ k² gives z = 2 and f ∝ k⁰ gives a gap. A light-like branch needs S_TT ∝ |k|, a quantum (non-RK) Coulomb-type phase.
  - Question: in the RK family on N0914's slots, can any tensor branch be light-like? If not, what exactly must the non-RK deformation supply?
- **Setting.**
  - N0914's slots, mod-2 law, the shift action (P112), the E⊕T₂ readout of R18-1.
  - RK Hamiltonians H = Σ_moves [−t·flip + v·(potential)], at t = v, for R18-1's ensemble. (R18-10's fixed-dipole sector has the same ξ [ref, `vR18-10:7`], so it adds nothing.)
  - Observables: the RK-point f-sum f_TT(k) as an exact classical average; S_TT(k) from MC (R18-1's data and runners, rerun first); the SMA bound along axis, face and body directions; the spectral gap of the Markov generator restricted to the TT channel, on small L by exact diagonalization where feasible.
  - Excluded: integer-law lifts; non-local moves; degenerate grounds; the t ≠ v quantum phase beyond leading order.
- **Prior art (count once):**
  - R18-1 and vR18-1 (Z₀; the ensemble; frozen βU = ∞); R18-10 and vR18-10 (OPEN: the dipole is six label totals; planar laws fake axis pinches); R17-6 and vR17-6 (Theorems G, Z); R17-1 and vR17-1 (f-sum orders, k⁰/k² models); R15-5 (worker: qubits give k³ at every finite order at strong coupling);
  - RK-point dynamics of classical Coulomb phases has z = 2 (Henley; Moessner–Sondhi; comparators, RECALLED);
  - quantum Coulomb phase away from the RK point has ω ∝ k (Hermele–Fisher–Balents; comparator, RECALLED);
  - rank-2 and lattice-graviton qubit models (Xu; Gu–Wen; Pretko; comparators, RECALLED).
- **Removed hypothesis.** Statics only.
- **Probes.**
  - (a) The RK-point f_TT(k): its leading k-order in the registered ensemble, as an exact classical expression.
  - (b) The SMA bound ω_SMA(k) = f/S along axis, face and body directions (R18-10's diagnostic correction), at βU ≤ 3.5, where vR18-1 accepts the data.
  - (c) Analytic. For local RK generators with the mod-2 law, prove z ≥ 2 (or a gap) for every T₂ branch, or exhibit a counterexample. State the needed hypotheses (detailed balance, locality, the conserved structure).
  - (d) What a light-like branch needs (S_TT ∝ |k|), and the leading t ≠ v correction to S_TT, if it fits in time.
  - (e) Prices.
- **FIXED readings.**
  - **RK-Z2:** a refereed proof that, in the stated RK class, every T₂ branch is gapped or has z ≥ 2. Light-like production then needs a non-RK phase.
  - **LIGHT-LIKE-SMA:** an explicit ensemble in the stated class whose SMA bound is linear in k in the TT channel, with checked strict V/S gaps. Checked.
  - **NEITHER:** both fail; for example, the bound is z = 2 on samples but no proof covers the class.
  - **OPEN:** otherwise.
- **Expectation.** RK-Z2.
  - Removed hypothesis: statics. RK dynamics is a symmetric Markov generator, and conserved local structure gives diffusive (z = 2) relaxation (comparator).
  - The likeliest failure is a k⁰ f-sum (R17-1's face-only model) making the SMA bound uninformative (a gap). That gives NEITHER or OPEN.
  - If RK-Z2 holds, the graviton window becomes "a non-RK quantum phase with S_TT ∝ |k|", which is P96 stated as a measurable target for quantum MC.

---

**R19-2. Set A's record noise in an expanding universe: does the a = 2 noise settle into a positive cosmological constant, and can it be the observed dark energy?** *(Launch after R18-11's referee confirms Theorem G and Lemma P, or now with the readings conditional on them. If the referee rejects either, the item is moot. This replaces an earlier S26 draft on W7 relics, which R18-12 now covers.)*

- **Plain question.**
  - R18-7 (refereed, in scope) builds set A's E1 + N_c at O(G²) in harmonic gauge.
  - R18-11 (worker; referee running) finds that only the insertion a = 2, the record as √−g T^{μν}, makes the averaged noise source independent of the readout gauge (Theorem G). On Minkowski, Lemma P pins the noise's mean energy at its zero start, so only its pressure acts. At a = 2 the active density is negative and |ρ_act| > ρ_Λ over all of R15-2's window (×1.17 to ×1e19): a NOISE-OVERSHOOT candidate.
  - R18-11 also suggests, without building it, that in FRW the switched-on noise settles to w = −1 with ρ ≈ (1 + ⟨x²⟩ + 2r + u_V/u₁)u₁/3 > 0. That equals ρ_Λ at ℓ ≈ 3.65 µm at the τ_c ceiling (`rR18-11:211-216`). Its report names this as one of the deciding computations (`rR18-11:271`).
  - Question: with an FRW version of Π, does the a = 2 noise become an exact w = −1 component? If so, is its size a prediction (one relation between ℓ and τ) inside R15-2's window and R6-4's lab bounds, or does it overshoot everywhere?
- **Setting.**
  - E1 + N_c at a = 2 (P145); R15-2's channels (ρ, T_⊥, V, TT) at the least-decoherence split; P76; P88 (extended to TT only, as R18-11 states for Poisson gauge).
  - A spatially flat FRW background with matter and radiation; the O(G·noise²) mean source; a noise spectrum stationary in comoving units.
  - An FRW version of Π: a causal conserving completion with zero homogeneous data before t₀. Any homogeneous-pressure freedom is stated as a price, not used to cancel.
  - Both energy histories, (P) and (U) (P146).
  - Excluded: E2; strong field; a ≠ 2; the γ-trade (P-r15c) except as a stated price.
- **Prior art (count once):** R18-11 (worker; its referee when back); R18-7 and vR18-7 (Π, the CP instrument, the scoped a = 4 zero); R18-6 and vR18-6 (set A: (S) cannot remove a non-vacuum stress); R15-2 and vR15-2 (u₁, the window, premise (iii)); R14-2 (the τ_c ceiling, suggested); R6-4 (the window's endpoint); R16-14 and vR16-14 (the Mercury bound); averaged backreaction (Isaacson; Green–Wald; comparators, RECALLED).
- **Removed hypothesis.** The Minkowski background of R18-11's Lemma P.
- **Probes.**
  - (a) The FRW Π and the homogeneous mode: prove or refute ρ̇_K + 3Hρ_K = −3H(ρ_s + p_s) and the w → −1 attractor; state the decaying remainder.
  - (b) The late-time ρ_noise in all channels (r, u_V, ⟨x²⟩ from R15-2's spectrum), as a function of (ℓ, τ).
  - (c) Where ρ_noise = ρ_Λ, and whether that point lies inside R15-2's window and R6-4's bounds; the local Mercury bound at that point (R18-11's a = 2 exclusion of ℓ ≲ 2.5e-8 m).
  - (d) Prediction or tuning: state the precision any match requires.
  - (e) Prices.
- **FIXED readings.**
  - **NOISE-IS-Λ:** an explicit FRW construction in which the a = 2 noise tends to w = −1 with ρ_noise = ρ_Λ at a stated (ℓ, τ) inside the window, consistent with Mercury and R6-4's bounds, with the required precision stated. Checked.
  - **NOISE-OVERSHOOT-FRW:** a refereed demonstration that in the stated class the late-time |ρ_act| exceeds ρ_Λ at every (ℓ, τ) in the window.
  - **NEITHER:** the attractor exists, but its size cannot match ρ_Λ anywhere in the window without the γ-trade or a tuning (state which).
  - **OPEN:** otherwise.
- **Expectation.** NEITHER, leaning NOISE-IS-Λ only at the window's top corner.
  - R18-11's suggested match needs the τ_c ceiling (itself suggested, R14-2) and small r and u_V. The T_⊥ and V channels add positive terms (2r, u_V/u₁) that push the match toward or past the window's edge.
  - Removed hypothesis: the Minkowski background. Kept: a = 2; E1's zero-energy start.
  - If NOISE-IS-Λ holds, set A would produce dark energy from its own record noise, with (S) setting the vacuum part to zero. That would be the campaign's first number that comes out rather than being tuned. It would also make P-r15c unnecessary at that point.

---

**R19-3. (S) as a quantum statement (J2): is the graviton's own zero-point stress absorbed by (S) and (d-i) in every gauge?**

- **Plain question.**
  - vR18-6 confirms the classical bridge (S) + (d-i) + N_red. It leaves the quantum step J2 OPEN (`vR18-6:7`):
    - isotropy needs the vacuum to be cubic-*invariant*;
    - the virial identification of ⟨t_LL⟩₀'s energy with the Hamiltonian zero-point covers only free, gauge-fixed TT modes;
    - constraints, ghosts, interactions and the gauge-dependent LL pseudotensor are not covered.
  - For linearized gravity on the box regulator, is the one-loop gravitational vacuum stress of the absorbable form −e_g g + W_g h[n] in every gauge, with e_g the TT zero-point energy density? If yes, (S) with the gravity sector inside H, plus (d-i), removes it with no number. If a non-absorbable part depends on the gauge or on the pseudotensor, J2 needs a named observable bridge.
- **Setting.**
  - R9-9's N-type box graviton (whole-zone v_max stated), lattice frame, Fierz–Pauli quadratic action.
  - Three treatments: reduced phase space (TT only); harmonic gauge with Faddeev–Popov ghosts; Coulomb/Poisson gauge.
  - The one-point stress via (A) ⟨t_LL⟩, (B) the second-order Einstein tensor ⟨G^(2)⟩ (Isaacson-type), and (C) the Hamiltonian zero-point. One loop.
  - Check cubic invariance of each vacuum, not just covariance.
  - Excluded: graviton self-interaction beyond one loop; matter; backreaction.
- **Prior art (count once):** R18-6 and vR18-6/refR18-6 (J2); R17-11 and vR17-11 (the exchange current); R17-7 (the enthalpy residual); R11-3 (zero-point stress of lattice fields); R9-9 (graviton symbol); the Isaacson effective stress and the gauge independence of the on-shell one-loop effective action (comparators, RECALLED).
- **Removed hypothesis.** Free TT-only, gauge-fixed modes.
- **Probes.**
  - (a) ⟨G^(2)_μν⟩ and ⟨t_LL⟩ in each of the three treatments, on the box regulator.
  - (b) Decompose each into −e g + W h[n] plus a remainder; check cubic invariance; compare e with the TT zero-point.
  - (c) Does the remainder vanish, and is it gauge-independent?
  - (d) Under (S) with the gravity sector inside H, plus (d-i): is the gravitational vacuum removed with no number?
  - (e) Prices.
- **FIXED readings.**
  - **J2-ABSORBED:** in all three treatments, the one-loop gravitational vacuum stress has the form −e_g g + W_g h[n], with e_g equal to the TT zero-point energy density and no remainder. Checked.
  - **J2-GAUGE-BRIDGE:** a refereed demonstration that the non-absorbable part depends on the gauge or the pseudotensor choice, so J2 needs a named observable bridge.
  - **NEITHER:** a gauge-independent non-absorbable remainder (J2 fails outright in the stated class). Refereed.
  - **OPEN:** otherwise.
- **Expectation.** J2-ABSORBED for (B) and (C); (A) may differ.
  - On shell, the one-loop effective action is gauge-independent (comparator), and ghosts cancel the unphysical polarizations, leaving the two TT modes.
  - In the lattice frame the vacuum is cubic-invariant, so its one-point stress is isotropic.
  - The likeliest failure is ⟨t_LL⟩'s off-shell gauge dependence, which would make (A) disagree and give J2-GAUGE-BRIDGE for the pseudotensor reading only.
  - Removed hypothesis: free TT-only modes. Kept: one loop, box regulator.

---

**R19-4 (withdrawn at 03:42Z).** Its question, the off-axis rows for UD and VW at the SM root, is now R18-13 (pre-registered 03:40Z, running; `TESTS:7061-7091`). R18-9 [worker] already found face2 ≠ T₂g for UD (`TESTS:7055`). So round 19 has three items.

**Queued for round 20 (stubs only; register after the named reading).**
- W7: if R18-12 returns BOUNDED or OPEN, the observational test of √(E² − P²) under the ADM readout bridge that P141 names.
- The bill's off-axis fallback (P122 as a non-shape knob, or a q²-dependent seagull), if R18-13 returns OPEN or its count exceeds the placement data.
- Quantum MC of the t ≠ v Z₂ model for S_TT ∝ |k|, if R19-1 returns RK-Z2.
- W15's continuous multi-shift mixing (`vR18-4:3`), if time allows.

---

- **R18-12 (relic edge quanta): worker reading BOUNDED** through the dark-matter density only. SELF-CLEANING is not met.
  - **Theorem C (corner dichotomy).** Umklapp conserves crystal momentum mod 2π. So every grid law has either light corner copies or absolutely stable Planckian corner states.
  - **Theorem C′ (which corner state is stable):**
    - **D1 world:** the Wilson doublers (0.095n/a, charged, W7-inert).
    - **G world:** the corner photons (2–2√3 /a, at rest, W7-active).
  - **Unstable defect states.** Many defect-carrying edge states decay in ~1e-42 s. Nothing removes the stable ones once made (Γ/H ≤ 6e-3).
  - **Bounds from Ωh² ≤ 0.12:**
    - doublers: T_RH ≤ 4–6e16 GeV;
    - corner photons: T_RH ≤ 4–10e17 GeV;
    - T_RH ≥ 1/a is excluded (overclosure by 1e23–1e27);
    - standard inflation (T_RH ≲ 7e15 GeV) is safe by enormous margins.
  - **No other observable bites:** the W7 mass anomaly in the lab is ≤ 3e-30.
  - **P-W7edge0 cannot follow from dynamics;** it is a history condition.
  - **Lemma X.** Translation-invariant dynamics never redshift crystal momentum, so "standard expansion" is undefined at the lattice scale. A momentum-dilating law would self-clean (P-r1812c).
  - **Prices:** P-r1812a (corner dichotomy), P-r1812b (history bound), P-r1812c.

  Referee running.

#### C5 referee verdicts R18-9, R18-11 and the R18-13 worker reading (recorded 04:12Z)

- **R18-9 referee: CONFIRMED WITH CORRECTIONS. FOUR-ROW-ZERO in the campaign's necessary-O(q) conservation convention.**
  - **What holds:**
    - SM content 4 + 22.5 + 12 has a transversal, independently reproduced, all-subluminal four-row axial zero at m = 0.01.
    - It uses **five** continuous knobs: four equality tunings plus a constrained photon-edge selection.
    - A separately retuned m = 0.001 root also exists.
  - **Corrections:** Ξ(a) is quadratic at finite grid but affine in the continuum q² coefficient. The "a-blind combination" was restated.
  - **Not established:**
    - exact Ward-completed conservation;
    - one law valid at both masses;
    - an enclosed photon window;
    - off-axis closure;
    - radiative stability;
    - the tadpole and CC rows;
    - two loops.
- **R18-11 referee: CONFIRMED WITH CORRECTIONS. Reading OPEN** (neither NOISE-SAFE nor NOISE-OVERSHOOT).
  - **Theorem G:** within the contravariant power-density family, gauge independence of the coarse-grained mean selects a = 2.
  - **The two readings at a = 2:**
    - (U) gives −4u₁;
    - (P) gives −(1 + ⟨x²⟩)u₁ + 2⟨q⟩u₁ − u_V.
  - **Why (P) does not establish an overshoot:** it overshoots only after imposing modewise q ≤ 0, u_V ≥ 0 and zero homogeneous pressure. These are not established for the strict spectrum.
  - **Other limits:** (U) is not a closed zero-start solution, and FRW remains suggested.
- **R18-13 (off-axis rows at the SM root): worker reading ALL-ROWS-ZERO on the letter, in the O(q) convention. It falls back to OFF-AXIS-COUNTED under exact W1.**
  - **Exactly two extra conditions:** face1 and face2. Body is then fixed (rank 4).
  - **Values at the root:** vectors dominate (face1 ≈ +2.65, face2 ≈ +1.36). UD Dirac breaks face2 ≡ T₂g.
  - **Lemma O:** own-direction smearings (w_d, w_o) move only the face rows, with nonzero Jacobian.
  - **Corollary N:** nonnegative weights cannot pay, so signed weights are needed.
  - **Lemma S:** no exactly conserved improvement moves the face rows. So this route conserves only at O(q).
  - **Joint root:** w_d ≈ −1.17, w_o ≈ −0.196. All axial and off-axis rows are zero to ~2e-6, at m = 0.01 and 0.001.
  - **Bill:** the SM gravity block costs 6 equality tunings plus 1 window selection.
  - **Prices:** P-R18-13a (signed own-direction placement), P-R18-13b (vector off-axis extension), P-R18-13c (if exact W1 is required).

  Referee running.

### C5 Round 19, item 5 (pre-registered 04:13Z, before launch)

**R19-5. Exact W1: do the surviving vertices (U, UD, VW) have exact Ward completions, and do these allow the signed placement data that pay the SM cone rows?**
- **Plain question.**
  - Every SM cone result so far holds only in the necessary-O(q) conservation convention. The vertices pass the forward test, but no vertex has an exact W1 completion (`vR18-9`, `vR18-5`).
  - R18-13 (worker) shows two things:
    - the off-axis rows are paid by signed own-direction placements;
    - by its Lemma S, no exactly conserved improvement moves those rows.
  - R17-12's Lemma I says axial stencils differ by identically conserved superpotentials.
  - If exact W1 is required:
    - (i) do exact completions of U, UD and VW exist (e.g. by Noether from a lattice action coupled to h)?
    - (ii) which of the placement data (the axial signed stencil a; the off-axis w_d and w_o) survive?
    - (iii) does the SM root survive, or which rows become unpayable by shape and placement?
- **Setting.**
  - Lattice actions for scalar, Wilson-Dirac and Maxwell fields on the subluminal edges, coupled to a lattice metric perturbation h at linear order.
  - The stress is defined as δS/δh (the Noether/Hilbert stress), and is exactly conserved under the lattice diffeomorphism generated by the stated graviton.
  - Compare with U, UD and VW.
  - One loop; axial and off-axis TT rows.
  - Excluded: M, V0, VU, VM; pairing.
- **Prior art (count once):** R17-12 (Lemmas F, I, X), R18-5 (Lemma D, UD), R18-9, R18-13 (Lemmas O, S), R13-5 (W1 hypotheses), R9-9 (graviton and placement), R16-5 (Ward wall W15), and lattice energy-momentum tensors (Caracciolo et al., RECALLED).
- **Removed hypothesis:** conservation only at O(q).
- **Probes.**
  - (a) Construct δS/δh for each field on the stated edges, or prove that no exactly conserved stress exists. Connect this to W15 (T_pf), which forbids exact translation Ward identities for single bands.
  - (b) Compare with U, UD and VW at O(q) and O(q²).
  - (c) Classify the placement data under exactness.
  - (d) Determine the fate of the R18-9/13 root.
  - (e) Prices.
- **FIXED readings.**
  - **EXACT-SURVIVES:** exact completions exist, and the SM all-rows root survives with exact vertices. Checked.
  - **EXACT-KILLS:** a refereed demonstration that exact conservation removes the placement freedom needed for the root, with the unpayable rows named.
  - **EXACT-IMPOSSIBLE:** a refereed proof that no exactly conserved lattice stress exists in the stated class. This would be W15 again.
  - **OPEN:** otherwise.
- **Expectation.** EXACT-IMPOSSIBLE for the translation part (T_pf / W15 already forbids an exact Ward identity for periodic bands). So "exact W1" is not available on any grid set. The O(q) convention is then the best attainable, and it is itself a price.
- **R19-2 (set A noise in FRW): worker reading OPEN.**
  - **The overshoot candidate is refuted** for the registered four-channel set. NOISE-IS-Λ is not met. A NEITHER candidate is offered for τ_c only.
  - **Theorem I₀ (main correction).** R18-11 and its referee omitted the quasi-static TT stress. With all four channels at the complete least-decoherence split and a = 2:
    - the averaged noise source vanishes on every spacelike mode;
    - reading (U) gives zero active density.
    - So the large noise does not gravitate; only a small remainder from near the cone does, and its sign depends on how that band is recorded (P-r192c).
  - **Lemma F0.** The FRW lift of the conserving projection is law data:
    - Lift A gives w → −1;
    - Lift B gives w = −1.23 and a de Sitter growing mode.
  - **Matches with ρ_Λ:**
    - complete split with the floor up to the cone: cτ = 23 µm for any ℓ, which lies outside R15-2's window;
    - otherwise a match needs a fit or a tuning.
  - **Corrections to R18-11:**
    - its flat (P) value and Mercury cut belong only to the TT-omitted set;
    - the 3.65 µm match assumed u_V ≈ 0;
    - its ρ_GW factor.
  - **Prices:** P-r192a (FRW lift), P-r192b (complete split), P-r192c (near-cone recording).

  Referee running.
- **R19-3 ((S) as quantum J2): worker reading J2-GAUGE-BRIDGE.** J2-ABSORBED is not met literally.
  - **The vacuum stress per mode** is c·k̃k̃/ω. The value of c depends on how gravity's stress is defined and in which gauge:
    - TT and Coulomb gauges: c = 1 for every definition.
    - Harmonic gauge: LL gives c = 2, G^(2) gives c = 4, and the Hamiltonian count with ghosts gives c = 1.
    - Other gauge conditions: c is 7/4, 3 or ½ for LL, and 17/4, 3 or 11/2 for G^(2).
  - **The remainder.** In harmonic gauge the LL and G^(2) readings leave a gauge-dependent Λ̃ ~ 2–6e123 ρ_Λ, which (S) and (d-i) do not remove.
  - **Literal N** (R16-14/R18-7's source) double-counts the graviton zero point.
  - **Lemma D (proved, checked symbolically).** Only weight-1 stress densities are free of pure-gauge vacuum contributions. The weight-1 object (A′) = −⟨[√−g G^{μν}]^(2)⟩/8πG gives c = 1 in every gauge, consistent with the background-field total (EH 1 + gauge-fixing 4 + ghosts −4).
  - **Probe (d):** with the weight-1 source, (S) and (d-i) remove the graviton vacuum with no number.
  - **Prices:**
    - P-r193a: the quantum source is the weight-1 density. One clause; possibly the same as R18-11's a = 2 price.
    - P-r193b: the lattice cubic vertex.

  Referee running.
- **R19-1 (Z₂ graviton at the RK point): worker reading NEITHER.** RK-Z2 and LIGHT-LIKE-SMA are both unmet. The method is pre-stated in `agents/C5_R19-1_method.md`.
  - **Lemma 1:** the RK Hamiltonian is the Markov generator, so its spectral measures equal the classical relaxation measures.
  - **Lemma 2:** at βU = 0 there are flat gapped bands.
  - **Lemma 3:** at every finite βU, the f-sum is k⁰ (bounded below uniformly), so the SMA gives a flat gap, never a cone.
  - **Proposition 4:** a linear SMA needs an odd-power S_TT matched to the f-class. Neither screened nor pinch-point ensembles supply one.
  - **Theorem 5:** under exponential clustering, every finite-mode Rayleigh–Ritz branch is gapped or O(k²), because relaxation rates have even-order zeros.
  - **Theorem 6:** in a bounded class, no isolated light-like T₂ branch.
  - **Conclusion:** a light-like branch would need a phase transition away from the RK point (P96 restated dynamically). Under P143 the T₂ mode is at best diffusive (z = 2).
  - **Prices:** P-r19-1a (RK tuning v = t); P96 sharpened.

  Referee running.

### C5 Round 19, items 6–8 (pre-registered 04:21Z, before launch; supervisor-drafted, no synthesis since S26)

**R19-6. One weight-1 source clause for both arenas?**
- **Plain question.** Three results each single out the weight-1 density as the gravitating source:
  - R18-11's Theorem G (refereed): a = 2, i.e. the record is √−g T^{μν}, for set A's record noise;
  - R19-3's Lemma D (worker): only weight-1 stress densities give gauge-independent vacuum stress, which is what J2 needs on the grid;
  - R19-2's Theorem I₀ (worker): at a = 2 the four-channel noise source vanishes on spacelike modes.

  Is there one clause, "the gravitating one-point source is the weight-1 density", that does all three jobs? Does it fix:
  - set A's insertion (a = 2);
  - the quantum graviton's vacuum source (A′);
  - N_red's readout?

  Does it conflict with any refereed result: (d-i), P88, R18-7's harmonic construction, or the R18-6 bridge?
- **Setting.** Both arenas, C-box-E with site creation and set A E1+N_c; one loop; O(G²).
  - Write the clause as an equation for the source of each arena's metric readout.
  - Check its gauge independence, its Bianchi consistency, and what it predicts for matter (β, γ), for the noise (R19-2) and for the graviton vacuum (R19-3).
- **Prior art (count once):** R18-11 and its verdict; R19-2 and R19-3 (workers; referees running); R18-6 and its verdict (N_red); R18-7 and its verdict; R16-14; R15-2.
- **Removed hypothesis:** separate source clauses per arena.
- **Probes.**
  - (a) The unified clause.
  - (b) A consistency check in each arena.
  - (c) The sentence count of the full bridge: (S), (d-i), N_red and weight-1.
  - (d) Prices.
- **FIXED readings.**
  - **UNIFIED:** one clause covers all three, consistent with every refereed result in both arenas. Checked.
  - **SPLIT:** a demonstration (refereed if a no-go) that the arenas need different source weights or clauses.
  - **OPEN:** otherwise.
- **Expectation.** UNIFIED. All three are the same statement: Lie-derivative covariance of the one-point source. The full classical-plus-quantum bridge is then four clauses and zero numbers.

**R19-7. Away from the RK point: is there a sign-free quantum Z₂ tensor model whose T₂ dynamical structure factor shows a linear mode?**
- **Plain question.**
  - R19-1 (worker) finds that at the RK point the T₂ spectrum is gapped or diffusive. A light-like branch needs a phase transition away from RK (P96).
  - The RK Hamiltonian is stoquastic, and so is H(v) = Σ[−t X^{p} + v·(diagonal)] for v ≠ t.
  - Using sign-free methods (continuous-time QMC, or exact ED on the smallest cluster), compute the T₂ dynamical structure factor S_TT(k, ω) at v/t < 1 (towards the Coulomb-like side) and at v/t > 1. Does a sharp, linearly dispersing T₂ peak appear anywhere?
- **Setting.**
  - R18-1/R19-1's slots and moves (cube, μ8; shift action), with H(v, βU) as stated.
  - Small L (2–4 for ED, or QMC up to 6) with imaginary-time correlators. Use a maximum-entropy-free diagnostic: the first frequency moment and the SMA ω(k), plus the imaginary-time decay rate per k.
  - Excluded: integer lifts; non-local moves.
- **Prior art (count once):**
  - R19-1, R18-1 and R18-10 (with verdicts as available); R17-6 (Theorem Z, Z₀); R16-7 (Theorem D: stoquastic means no Newtonian attraction);
  - quantum spin ice and RK-point literature (Hermele–Fisher–Balents, Moessner–Sondhi; RECALLED): the U(1) photon appears on the v < t side.
- **Removed hypothesis:** the RK point v = t.
- **Probes.**
  - (a) A method statement before running.
  - (b) ω(k) and the SMA along the axis, face and body directions for several v/t, with the TT, V and S channels separated.
  - (c) Off-axis checks (R18-10 rule).
  - (d) Is there a regime with ω ∝ |k| in T₂ and gapped V/S, at the system sizes run?
  - (e) Prices.
- **FIXED readings.**
  - **LINEAR-T2-EVIDENCE:** at stated sizes, a T₂ channel with ω(k) linear over ≥ 3 k-points, gapped V/S, consistent across two sizes. Checked. This is evidence only.
  - **NO-LINEAR:** gapped or quadratic T₂ in every v/t regime tested, consistent across sizes. Checked.
  - **OPEN:** otherwise.
- **Expectation.** NO-LINEAR at the accessible sizes, with v < t giving a soft but quadratic T₂. The expectation names its removed hypothesis: RK fine-tuning. It keeps stoquasticity, which by Theorem D already forbids Newtonian attraction.

**R19-8. Set A's leak route E2 under the same source analysis: does E2 tie with E1, or break the tie?**
- **Plain question.**
  - E1 and E2 are tied observationally (R14-2, R16-14).
  - R18-7, R18-11 and R19-2 built E1 + N_c at O(G²) and analyzed its noise source: Theorem G gives a = 2, and Theorem I₀ gives a vanishing spacelike source.
  - E2 (friction on all of h̄ plus a noiseless outgoing sink) lacks a sink action (R16-14 verdict).
  - Can E2 be completed the same way (records sourced with a = 2, conserving projection), with CP and a well-posed readout? Does its noise or sink stress gravitate differently from E1's?
- **Setting.** E2 as in R12-7/R14-2 (γ in the drag-allowed range). Completion as in R18-7 (Π, a = 2). O(G²), static and quasi-static plus the stationary noise. Excluded: strong field.
- **Prior art (count once):** R12-7, R14-2, R16-14 and R18-7 with their verdicts; R18-11 and its verdict; R19-2 (worker); R16-4 (E2 keeps initial TT energy).
- **Removed hypothesis:** E1 only.
- **Probes.**
  - (a) The E2 + N construction, including a sink action, or proof that none exists in a stated class.
  - (b) CP.
  - (c) β, γ.
  - (d) The noise and sink active density.
  - (e) Prices, and a tie-break statement.
- **FIXED readings.**
  - **E2-CONSTRUCTED:** an explicit E2 + N law at O(G²), CP, with β = γ = 1. Checked, with its noise and sink budget.
  - **E2-OBSTRUCTED:** a refereed demonstration that no E2 completion in a stated class is CP with a conserved source.
  - **OPEN:** otherwise.
- **Expectation.** E2-OBSTRUCTED, or OPEN. The noiseless outgoing sink has no CP + conserving completion, because a sink that absorbs TT energy without noise violates the fluctuation–dissipation balance. If so, the tie breaks in favour of E1.
- **R19-5 (exact W1): worker reading OPEN.**
  - **What the readings come to:**
    - EXACT-IMPOSSIBLE is refuted for the massive species.
    - EXACT-KILLS is not supported.
    - EXACT-SURVIVES is met for scalar and Dirac, and only partly for the photon.
  - **Exact W1 is not W2.** W15/T_pf forbids the translation Ward identity (W2), not exact conservation (W1). U already had an exact completion via R8-2 and R13-5 Lemma P1; earlier verdicts missed this.
  - **For massive species, exact W1 constrains nothing in the cone rows.**
  - **New exact Wilson-Dirac stress** (Lemma Div):
    - it uses UD's pair block on R18-9's edge;
    - W1 holds to 2.4e-15;
    - the own-direction smearings also complete exactly.
  - **P-R18-13c is class-scoped:** it applies only to channel-tied stresses.
  - **The photon** needs a continuum Maxwell kernel at the soft corner, at a row cost of O(r⁴) (~1e-6 at r = 0.1). This is an outline only.
  - **The SM root survives** exact W1 for scalar and Dirac (proved), and for the photon (suggested). The bill is unchanged: 7 knobs.
  - **Prices:**
    - P-R19-5a: a channel-decoupled stress;
    - P-R19-5b: the photon soft-corner clause.

  Referee running.

#### C5 referee verdicts R18-12, R18-13, R19-1, R19-2, R19-3 (recorded 04:42Z; codex gpt-5.6-sol, xhigh)

- **R18-12 referee: CONFIRMED WITH CORRECTIONS. Reading BOUNDED** (narrowly, through observable (ii)).
  - **Confirmed:**
    - for free S/G/D1 bands, crystal momentum is conserved mod 2π;
    - G + R85 gives free-sector corner photons at 2, 2√2, 2√3 /a with zero group velocity and Q_D/E = −2;
    - the D1 corner modes are m + nW_π, charged, with Δ = 0;
    - any surviving conserved relic is bounded by the dark-matter density: Y ≤ 3.76e-28 (doubler) or Y ≤ 1.79e-29 (corner photon).
  - **Not confirmed:**
    - the universal corner dichotomy;
    - the universal Γ/H ceiling;
    - the quoted T_RH brackets;
    - strict Lemma L;
    - "translation invariance invalidates standard expansion".
  - **Scope:** decay widths and interacting stability are not certified.
- **R18-13 referee: CONFIRMED WITH CORRECTIONS. ALL-ROWS-ZERO in the O(q) convention.**
  - **Confirmed:**
    - rank four, and the body relation;
    - face1 and face2 are the two independent extra conditions;
    - signed own-direction weights near (−1.172, −0.195) give a checked, all-subluminal joint zero at m = 0.01, plus a separately tuned m = 0.001 solution;
    - the cost is six equality tunings plus one photon-window selection.
  - **Not established:**
    - exact W1 (R19-5 worker addresses this);
    - a unique VW extension;
    - one law at both masses;
    - the tadpole and CC rows;
    - radiative stability.
- **R19-1 referee: CONFIRMED WITH CORRECTIONS. Reading NEITHER.**
  - **Confirmed:**
    - Lemma 1: frustration-free, and unitarily equivalent to the reversible Markov generator;
    - Lemma 2: flat 8t and 12t label modes at βU = 0;
    - a volume-independent positive k⁰ f-sum at every finite βU (L ≥ 3);
    - uniform exponential clustering would exclude linear finite-mode Rayleigh–Ritz branches, and isolated light-like branches with analytic complementary moments.
  - **Open:**
    - continuum-mixed branches;
    - finite-βU clustering;
    - a uniform gap.
- **R19-2 referee: NOT CONFIRMED (the w → −1 claim). Reading OPEN.**
  - **Theorem I₀ is confirmed off the cone.** At a = 2, with the newly stipulated complete split, the four-channel source cancels exactly on every spacelike mode. The FRW lift is genuine law data.
  - **But the worker changed the registered assumption,** from comoving-stationary noise to proper-stationary. Consequences:
    - the registered comoving spectrum is asymptotically dust-like under lift A, not w = −1;
    - the 23.24 µm result belongs to a new, out-of-window completion;
    - free r and the γ-trade are fits;
    - the near-cone contribution is incomplete.
  - **Result:** set A is not shown to become a positive cosmological constant.
- **R19-3 referee: CONFIRMED WITH CORRECTIONS. Reading J2-GAUGE-BRIDGE** (J2-ABSORBED not met).
  - **Reproduced independently:**
    - harmonic gauge: c_A = 2, c_B = 4, c_C = 1 with ghosts;
    - background field: 1 + 4 − 4 = 1;
    - literal N gives (2 + ξ)e_g, which is exactly double only as ξ → 0.
  - **Conditional result.** At free one loop, conditional on H-V3, P136(ii), P-r193a and the class-𝒟 receiver, (S) removes the physical graviton zero point and (d-i) compensates its isotropic enthalpy. No fitted number is needed.
  - **Why a bridge is needed:** the LL and G^(2) composites are gauge-dependent, so a named observable bridge is necessary.
  - **Not covered:** arbitrary gauges, interactions, higher loops.

### C5 Round 19, item 9 (pre-registered 04:44Z, before launch)

**R19-9. Close the photon at EXACT-SURVIVES: build the exact W1 completion of VW numerically and re-solve the SM root.**
- **Plain question.** R19-5 (worker; referee running) finds:
  - exact W1 exists for scalars and Dirac, and the SM rows are unchanged;
  - for the photon only an outline exists: Sylvester inversion, plus division on the scattering shell, plus the continuum Maxwell kernel in a soft-corner cube of radius r, with row cost O(r⁴).

  Build it, check W1 to machine precision, and re-solve the 6-knob SM root at r ≈ 0.05–0.1.
- **Setting.**
  - R18-9/R18-13's SM root (U, UD, VW with signed own-direction stencils) on its stated edges.
  - The photon on γG_w(2.9435, 0.198093); the graviton as R9-9.
  - Exact W1 means machine precision over the torus.
  - Single soft legs: write the Gauss-law bookkeeping.
- **Prior art (count once):** R19-5 (worker), R8-2 Construction A, R13-5 Lemma P1, R17-12, R18-9 and R18-13 with their verdicts.
- **Removed hypothesis:** conservation only at O(q), for the photon.
- **Probes.**
  - (a) The exact photon stress and its W1 check.
  - (b) Its corner cost.
  - (c) Re-solve the root: all axial and off-axis rows, with knob shifts.
  - (d) Prices.
- **FIXED readings.**
  - **PHOTON-EXACT:** the exact photon completion is checked to ≤ 1e-12 and the SM root is re-solved with all rows zero. Checked.
  - **PHOTON-OBSTRUCTED:** a demonstration (refereed) that no exact completion exists in a stated class (e.g. a single-soft-leg Gauss-law obstruction).
  - **OPEN:** otherwise.
- **Expectation.** PHOTON-EXACT with knob shifts ~1e-6.
- **R19-6 (one weight-1 source clause): worker reading UNIFIED.**
  - **The clause W1:** "the gravitating one-point source is the weight-1 density √−g T^{μν}; records and expectations are of it; gravity's own stress enters as −[√−g G]^{(≥2)}/8πG".
  - **Lemma L.** ⟨L_ξ𝔜⟩ = (w − 1)⟨(∂·ξ)𝔜⟩ for any flat-conserved weight-w density, so only w = 1 gives gauge-blind averages. It covers both R18-11's Theorem G and R19-3's Lemma D.
  - **Proposition U.** At a = 2, set A's noise gravitates through the same functional A′ as the graviton vacuum. Gauge dependence at a ≠ 2 carries the factor (a − 2).
  - **Graviton vacuum.** In Feynman–de Donder gauge c = w. Only w = 1 matches the TT value in every gauge.
  - **No conflict found** with (d-i), P88, R18-6 or R18-11. R18-7's a = 4 is replaced by a = 2, which keeps CP and β = γ = 1 and loses only the static a = 4 zero.
  - **The full bridge** is 4 clauses with 0 numbers: (S), (d-i), N_red and W1. W1 merges P145 and P-r193a.
  - **What W1 does not fix:** the noise's remaining gravitating size, which still depends on P-r192a/b/c and P146.
  - **Archive fix (04:43Z).** `scripts/C5/R19-3/r193_lattice.py` imported from the non-archived `../recheck/R9-9`. It now points to `../R9-9`, and the rerun output is identical. (Reported by R19-6.)

  Referee running.

### C5 Round 19, item 10 (pre-registered 04:45Z, before launch)

**R19-10. Is "the law's lowest state" well defined when the lattice creates sites? e₀ for a growing lattice.**
- **Plain question.**
  - (S) sets C = e₀[H]: the ground-state energy density of the law's Hamiltonian (R17-3, R17-7).
  - In C-box-E, the arena where (S), (d-i), N_red and W1 form a consistent bridge (R18-6, R19-6), sites are created at rate 3H (P52).
  - The Hilbert space and H then change with time. Is "the lowest state" defined, and is e₀ a time-independent intensive constant?
  - Concrete issues:
    - (i) Is e₀ = lim E₀/V the same for every volume, with no 1/V or boundary terms that would make Λ̃ drift as sites are added?
    - (ii) Does site creation inject energy relative to the instantaneous ground state, i.e. excitations? The creation law must place new sites in some state (AX:37, AX:92-94).
    - (iii) Does the answer depend on whether new sites are created in their local ground state or in a fixed product state?
- **Setting.**
  - Free lattice fields (scalar, Wilson-Dirac, photon) on growing boxes L → L + 1, plus a local site-insertion rule. Candidates: insert in a product state, or insert adiabatically.
  - FRW-like slow growth (H ≪ 1/a).
  - Measures:
    - e₀(L) and its finite-size corrections;
    - the energy above the instantaneous ground state after insertions, per unit volume per e-fold.
  - Excluded: interacting matter; gravity backreaction beyond the (S) bookkeeping.
- **Prior art (count once):** R17-3 and its verdict (Lemma U, Theorem T), R17-7 and its verdict (Lemma X: records cost energy above E₀), R17-11, R18-6, R12-2 (site creation forced at 3H), R13-3, P52/P53, and adiabatic theorems (RECALLED).
- **Removed hypothesis:** a fixed Hilbert space.
- **Probes.**
  - (a) e₀(L) convergence and its corrections, for each field.
  - (b) Excitation energy per inserted site for each insertion rule, and the resulting energy density injected per e-fold, against ρ_Λ at a = ℓ_P.
  - (c) Whether any local insertion rule injects less than ρ_Λ per Hubble time, or the result is a new Λ-like or dust-like term.
  - (d) Prices.
- **FIXED readings.**
  - **WELL-DEFINED:** e₀ is intensive with corrections that vanish, and some stated local insertion rule injects energy below ρ_Λ per Hubble time at a = ℓ_P. Checked.
  - **INJECTS:** a refereed demonstration that every local insertion rule in a stated class injects energy above ρ_Λ per Hubble time.
  - **OPEN:** otherwise.
- **Expectation.** INJECTS for product-state insertion: each inserted site costs about the local zero-point gap, ~1/a. Adiabatic insertion is plausibly WELL-DEFINED, but it needs a rate slower than the gap, which a = ℓ_P, H ≪ 1/a satisfies. The question is whether adiabatic insertion is local.
- **R19-8 (set A's E2 route): worker reading E2-CONSTRUCTED in a stated scope.** The expectation (OBSTRUCTED or OPEN) was refuted.
  - **The law.** E2 + N_c is R18-7's law with damped readout □ − γu·∂, a = 2, and the same Π.
    - The friction stress is flat-conserved.
    - CP holds: the sink is classical, deterministic and sits inside Π.
    - β = γ = 1.
  - **Noise.** Per mode, E2 = |R| × E1, with |R| ≤ 1 and different only in bands |1 − x| ≲ 1e-28. Theorem I₀ carries over. a = 2 is forced by inertness.
  - **Sink.** It absorbs exactly the noise's work and is pressureless at k = 0. It needs memory (Lemma S2: no instantaneous local sink stress).
  - **The FDT objection does not bind** a classical zero-temperature sink in set A.
  - **Caveats:**
    - a near-cone cap (P-r198c) under P-r14b;
    - the FRW friction lift (P-r198a);
    - there is no local sink action.
  - **The tie with E1 holds.** No observation decides between them; the differences are law data.
  - **Prices:** P-r198a, P-r198b ("the sink is Π"; retires P-r12b) and P-r198c.

  Referee running.

### C5 Round 19, item 11 (pre-registered 04:49Z, before launch)

**R19-11. One law for every SM mass: does the SM cone root have a massless limit valid for all species at once?**
- **Plain question.**
  - R18-9 and R18-13 (refereed in the O(q) convention) zero every cone row at m = 0.01, and separately at m = 0.001. The verdicts note that "one law at both masses" is not shown.
  - At a = ℓ_P every SM mass is m·a ≲ 1.4e-17. So the physically relevant law is the m → 0⁺ limit root, with corrections from each species' own mass.
  - Do the rows have a finite massless limit? Are they analytic in m², or do they carry m log m terms (cf. R16-10's Theorem L)?
  - Does the m → 0⁺ root exist, and how large are the residual rows for the heaviest SM species (top, m·a ≈ 1.4e-17)?
- **Setting.**
  - R18-9/R18-13's content and vertices (U, UD, VW with signed and own-direction stencils) and edges.
  - All six rows (E_g, T₂g, μ_E, μ_T2, face1, face2).
  - Masses: a common m → 0⁺, then per-species SM masses as perturbations.
- **Prior art (count once):** R18-9, R18-13 and R16-10 (Theorem L) with their verdicts; R16-2 (per-species residuals ≤ 1e-21); R14-3 (μ_E analytic in m²); R16-3 (Ξ analytic in m²).
- **Removed hypothesis:** fixed finite m.
- **Probes.**
  - (a) The m → 0⁺ limits of each row and their leading corrections (power or log), per species.
  - (b) The root at m = 0⁺ (knob values), or a proof that some row diverges.
  - (c) Residual rows with SM masses at a = ℓ_P, against GW170817 (|c_g − c|/c ≲ 1e-15, RECALLED).
  - (d) Prices.
- **FIXED readings.**
  - **ONE-LAW:** a massless-limit root exists. The residuals at the SM masses are below the GW170817 comparator and below the R16-2 photon comparator. Checked.
  - **MASS-OBSTRUCTED:** some row diverges or is non-analytic as m → 0, so that no single law serves all SM masses (refereed).
  - **OPEN:** otherwise.
- **Expectation.** ONE-LAW. The rows are analytic in m² for gapped valleys, so the corrections are ~(m·a)² ≲ 1e-34. The main risk is IR logs in the Dirac or photon μ rows.
- **R19-7 (off-RK Z₂ tensor dynamics): worker reading OPEN.** NO-LINEAR holds in some regimes; LINEAR-T2-EVIDENCE is not met. The method is pre-stated in `agents/C5_R19-7_method.md`. The family is sign-free for every v.
  - **Feasibility.** Exact diagonalization is limited to ≤ 8-site clusters, which are all distorted by wrap-around. The "≥ 3 k-points" condition cannot be reached by ED here.
  - **No linear T₂ anywhere.** The T₂ pole is either flat in k or has its minimum at finite wavevector. S_TT never grows toward k = 0.
    - On the v < t side it is a gapped flat paramagnet (exact at v = 0).
    - The RK point is a sharp avoided crossing.
    - On the v > t side the system collapses onto a degenerate γ = 0 manifold: soft, but flat, not propagating.
  - **Lemma B:** off RK the TT f-sum stays k⁰.
  - **Proposition C:** a linear T₂ branch in the k⁰ class forces S_TT ≳ 1/|k|.
  - **Lemma G:** the registered moves obey a local F₂ relation per 3³ block, so any pair-insertion QMC is non-ergodic.
  - **Prices:** P-r19-7a (v/t); P96 sharpened.
  - Not a no-go, so a referee is optional.
- **R19-6 referee: NOT CONFIRMED (the UNIFIED). Reading OPEN** (recorded 04:52Z). W1 replaces R18-7's registered a = 4 law instead of staying consistent with it; under the "literal first" rule that makes the reading OPEN, not SPLIT.
  - **Confirmed, within the stated contravariant density families and perturbative domains:**
    - Lemma L, with both of its instances;
    - weight one unifies the conserved-record and linearized-Einstein gauge identities;
    - it makes set A's a = 2 mean source equal to the same Einstein–Hilbert functional A′ used for the graviton vacuum;
    - with the complete split, the spacelike off-cone noise mean cancels;
    - the TT and Feynman–de Donder vacuum coefficient is 1.
  - **The new a = 2 law** is past-record-adaptive and causally completed. It keeps CP and static spherical β = γ = 1, but loses R18-7's pure-scalar cancellation.
  - **Net:** this is a coherent, number-free common-source completion, but not strictly UNIFIED.

### C5 Round 19, item 12 (pre-registered 04:54Z, before launch)

**R19-12. The whole SM cone bill on one set of edges: the charge block on the gravity root's edges.**
- **Plain question.**
  - The gravity block's SM root (R18-9 and R18-13, refereed in the O(q) convention) fixes particular edges:
    - Dirac on D1(0.909, 0.556);
    - a nearly linear photon γG_w(2.9435, 0.198);
    - scalars on G_w(2.526).
  - The charge block (R16-1, R16-2, R16-10) was computed on other edges.
  - On the gravity root's own edges, recompute:
    - the electron–photon split Δ(0⁺) for each charge class;
    - the photon shift Σ;
    - the minimal number of charge tunings, counted on the counterterm basis.
  - Does one law then carry both blocks, and what is the total bill for SM content?
  - Does the photon window (b_γ ≈ 2.94) help or hurt the charge rows? Note that R16-10's stiffened-photon zero needed v_max 7.35, while this photon is subluminal.
- **Setting.**
  - R16-2's one-loop runner and R16-10's split evaluator (Theorem L), at the R18-9/13 root edges.
  - SM charges, counted per class and per species.
  - m → 0⁺.
- **Prior art (count once):** R16-1, R16-2 and R16-10 with their verdicts (Lemma Q: the photon shift is independent of the internal photon symbol; Theorem L); R18-9 and R18-13 with their verdicts; R19-11 (running).
- **Removed hypothesis:** the charge and gravity blocks on separate edges.
- **Probes.**
  - (a) F_s(0⁺) for D1(0.909, 0.556) and G_w(2.526) with the root photon.
  - (b) The charge tunings needed, and whether any gravity knob can double as a charge knob.
  - (c) The total bill on one law, with every row listed.
  - (d) Prices.
- **FIXED readings.**
  - **ONE-LAW-BILL:** an explicit total count on the root's edges, with every row's payment named. Checked.
  - **CONFLICT:** a demonstration that the charge rows cannot be paid on the root's edges without breaking a gravity row, in the stated knob class.
  - **OPEN:** otherwise.
- **Expectation.** ONE-LAW-BILL, with 3 charge counterterms per class. The total is about 6 + 1 + 3 + tadpole + CC, so roughly 11 + CC, or fewer if the tadpole is paid by (d-i).
- **R19-10 (e₀ with site creation): worker reading INJECTS in class 𝒞_Γ.** A referee is required. WELL-DEFINED is not met.
  - **Static lattice: e₀ is intensive** (L⁻⁴ Casimir terms, about 1e-121 ρ_Λ at Hubble size). Adding a plane adds exactly e₀ per site.
  - **Product insertion** costs 0.04–0.06 (scalar) and 0.7–1.0 (Wilson-Dirac) per site, which injects 1e122–3e123 ρ_Λ per Hubble time.
  - **Lemma S-ins:** bounded local insertion (rate ≤ Γ) leaves a standing excess ρ_ins = 3H·A/a³ ≥ 5.5e59/Γ ρ_Λ.
    - Slow ramps trade leftover excitation for in-progress energy; the total is ≥ 6.7e60 ρ_Λ for any ramp time T.
    - Dislocation climb gives ~3.4e61/v ρ_Λ.
  - **This is a new H-tracking Λ term.** Under (S) + N_red it gravitates. If e₀ is defined from the instantaneous law instead, it drifts and brings back the signalling channel.
  - **Escapes:** super-Planckian Γ, a per-species 1e-62 tuning plus Hubble-time insertions, acausal born-entangled sites, a new principle, or no site creation.
  - **Consequence (worker reading):** P93 cannot hold exactly on a lattice that grows by local insertion. C-box-E's "zero numbers" bridge holds only for a static or perfect site set.
  - **Prices:** P-r1910a (insertion energy), P-r1910b (dislocation cores).

  Referee running.

### C5 Round 19, item 13 (pre-registered 05:11Z, before launch)

**R19-13. Can a site be born already entangled? Insertion cost against isometry radius.**
- **Plain question.** R19-10 (worker; referee running) finds that every product-born insertion with bounded extraction rate Γ leaves a standing excess ρ_ins ≥ 5.5e59/Γ ρ_Λ. Its escape E3 is to insert a site through a local isometry of radius R, which entangles the new site with its neighbours on arrival. That escape was not computed.
  - How does the best radius-R isometric insertion's excess energy ΔE(R) scale? Expect a power law for gapless fields and exponential decay for gapped ones.
  - What R makes 3H·ΔE(R)·τ_ins/a³ < ρ_Λ?
  - Is such an R local (R ~ a few a) or effectively acausal?
- **Setting.**
  - Free scalar (m = 0 and m > 0), Wilson-Dirac and photon (transverse) on Z³.
  - Plane insertion as in R19-10.
  - The best Gaussian isometry supported on a ball or slab of radius R around the new site, found by optimizing the Gaussian state on the support.
  - Stated insertion time τ_ins.
- **Prior art (count once):**
  - R19-10 (worker): Lemma S-ins and the product costs;
  - R17-7 Lemma X;
  - entanglement area laws and the decay of ground-state correlations (RECALLED; e.g. Hastings, Brandão–Horodecki).
- **Removed hypothesis:** product-born sites.
- **Probes.**
  - (a) ΔE(R) for R = 1..R_max on each field. Fit and extrapolate.
  - (b) The R needed for ρ_ins < ρ_Λ at a = ℓ_P.
  - (c) Whether the isometry is realizable by a finite-depth local circuit within τ_ins (Lieb–Robinson).
  - (d) Prices.
- **FIXED readings.**
  - **ENTANGLED-ESCAPE:** a stated local isometry rule with R ≤ 10a and circuit depth ≤ τ_ins/a that brings ρ_ins below ρ_Λ. Checked.
  - **NO-LOCAL-ESCAPE:** a demonstration (refereed) that the required R exceeds a stated bound, e.g. R ≳ 1e30 a for gapless fields.
  - **OPEN:** otherwise.
- **Expectation.** For gapped fields, R ≈ ln(1e122)/m: local for m ~ 1/a, non-local for SM masses (m·a ~ 1e-17). For gapless fields (photon, graviton), R ~ (1e122)^{1/4} ~ 1e30 a. So NO-LOCAL-ESCAPE for the photon, which makes the R19-10 injection unavoidable for massless fields.

#### C5 referee verdicts R19-5, R19-8 and the R19-9 worker reading (recorded 05:19Z)

- **R19-5 referee: CONFIRMED WITH CORRECTIONS. Reading OPEN.**
  - **W1 and W2 are distinct.** W15/T_pf addresses W2 and does not prohibit exact W1.
  - **Exact completions exist for the massive species.** U has an exact quasi-local completion. Every admissible smooth massive Wilson-Dirac pair kernel has one in the channel-decoupled class, including UD and its signed own-direction smearings.
  - **The scalar and Dirac rows are unchanged** under these completions.
  - **Lemma S** removes the placement route only in the channel-tied class.
  - **Open for the photon:** VW had only a plausible soft-corner construction (R19-9 now addresses this).
- **R19-8 referee: NOT CONFIRMED (the E2-CONSTRUCTED). Reading OPEN.**
  - **What can be stipulated.** In the weak-field, finite-rational, Gaussian, real-Ohmic, off-cone scope, a causal non-local E2 + N_c records-to-metric law can be stipulated. It propagates harmonic gauge and is CP. Its static sector keeps β = γ = 1, and its per-mode noise source is exactly |R| times E1's.
  - **Also confirmed:** Lemma S2 (the sink needs memory), and classical zero-temperature FDT does not force added noise.
  - **Not constructed:**
    - a physical sink action or stress with a unique homogeneous budget;
    - a record-finite stationary cone prescription;
    - the FRW lift.
  - **The tie with E1** survives formally at the noise level.
- **R19-9 (exact photon completion): worker reading PHOTON-EXACT.**
  - **The construction:** a glued exact W1 photon stress made of three pieces:
    - the continuum Maxwell stress on the corner ball;
    - an inverted soft-leg block;
    - in the hard-hard region, VW pair blocks plus R8-2's dust scattering kernel with a fibre identification.
  - **W1** holds on the physical (Gauss-law) block to ≤ 6.5e-14.
  - **No obstruction at a single soft leg.**
  - **Proposition K:** the corner cost is exactly C_e r⁴.
  - **The SM root re-solves:** all six rows ≤ 3.3e-11, with knob shifts ≤ 2.9e-6 at r = 0.1. The bill is unchanged at 6 + 1.

  Referee running.

### C5 Round 19, item 14 (pre-registered 05:21Z, before launch)

**R19-14. If site creation injects energy (R19-10), does any other way of growing space keep (S) number-free?**
- **Plain question.** R19-10 (worker; referee running) finds that local site insertion leaves a standing excess energy of at least ~1e60 ρ_Λ above e₀, which tracks H. (S) plus N_red then gives Λ̃ ≠ 0. Two alternatives remain:
  - V1, where the lattice spacing grows with a fixed number of sites (R11-3, R12-2);
  - a grid that does not expand at all, with expansion carried by records or the metric.

  Under each:
  - (i) is e₀ constant? For example, in V1 the physical e₀ ∝ 1/a(t)⁴ is not constant.
  - (ii) Is there a standing excitation?
  - (iii) Can (S) + (d-i) + N_red + W1 stay number-free and non-signalling?
- **Setting.**
  - V1: the R11-3 fixed-site grid with a growing a(t), where a/ℓ_P drifts.
  - V0: the grid fixed in physical units, with no growth, as in set A-like or records-carry-expansion pictures.
  - Excluded: active compensation; site creation (R19-10's subject).
- **Prior art (count once):**
  - R11-3 and its verdict (two tadpoles; w ≥ 0; a/ℓ_P drift);
  - R12-2 and its verdict (fixed-site grids cannot expand; site creation is forced at 3H);
  - R17-7, R17-11, R18-6 and R19-6 with their verdicts;
  - R19-10 (worker);
  - SUMMARY §25.
- **Removed hypothesis:** site creation as the growth mechanism.
- **Probes.**
  - (a) e₀ and the excitations under V1. Is the evolution adiabatic? What is the drift of e₀·a⁴?
  - (b) Under V1, (S) with a time-dependent e₀: Bianchi, a carrier, and signalling.
  - (c) R12-2's no-go for fixed sites: does it still bind with (S) in place?
  - (d) V0 options.
  - (e) Prices.
- **FIXED readings.**
  - **ALT-GROWTH-OK:** a stated growth mode under which (S) and the bridge stay number-free, non-signalling and consistent with observation (no a/ℓ_P drift beyond bounds). Checked.
  - **NO-NUMBER-FREE-GROWTH:** a refereed demonstration that every growth mode in a stated class (site creation, V1, fixed grid) costs a number or a signalling channel under (S).
  - **OPEN:** otherwise.
- **Expectation.** NO-NUMBER-FREE-GROWTH:
  - V1 makes e₀ time-dependent, which brings back the Bianchi carrier and signalling;
  - a fixed grid cannot expand (R12-2);
  - site creation injects energy (R19-10).

  If so, (S) is number-free only on a static universe, and Λ goes back to a tuning or a new principle.
- **R19-11 (one law for every SM mass): worker reading OPEN.**
  - **Massless limit.** Every row has a finite limit as m → 0⁺.
    - Scalar and vector rows are analytic in m².
    - Wilson-Dirac rows have linear-in-m terms (Lemma A: the Wilson mass breaks m → −m).
  - **The m → 0⁺ root exists:** (2.590035, 0.915439, 0.568281, −0.176177), with off-axis (−1.1717, −0.1956). It is subluminal and transversal.
  - **Residuals with SM masses at a = ℓ_P** (top-dominated, O(ma) ≈ 1e-17):
    - speed rows: Δc ≈ 0.2–2.4e-18. Below GW170817, but 6–9× above R16-2's photon comparator.
    - shear rows: μ ≈ 1–5e-19 per cell. Read as a graviton mass (~6e10 GeV), that is ~1e79 above the GW170817-level bound.
  - **A spectrum-tuned law exists** (implicit-function theorem). It zeroes all six rows, but its knobs encode the SM mass sums to ~1e-98, and electroweak-transition changes detune it.
  - **Twisted-mass Dirac** (P-R19-11c) brings the speed residuals to ~1e-35. The shear residual stays ~1e62 too large.
  - **A mass-blind law** needs ~14–17 more conditions.
  - **Prices:** P-R19-11a, b and c.

  Referee running.

### C5 Round 19, item 15 (pre-registered 05:24Z, before launch)

**R19-15. The shear rows as a graviton mass: does any part of the bridge — exact W1, (S), (d-i), W1-weight — remove them, or are they a ~1e-98 tuning?**
- **Plain question.**
  - The shear rows μ_E and μ_T2 are the supplied zero-point vacuum's response to a static TT strain.
  - R19-11 (worker; referee running) reads them as a graviton mass. At SM masses, an untwisted law leaves μ ~ 1e-19 per cell, ~1e79 above the GW170817-level bound. A spectrum-tuned law zeroes them only by encoding mass sums to ~1e-98 (P0-level).
  - Does any refereed piece of the bridge force μ = 0 structurally?
    - Exact W1 (R19-5/R19-9): a conserved stress.
    - (S): e₀ removed.
    - (d-i): it absorbs the isotropic enthalpy W h[n] only (R17-11 says the anisotropic part is not absorbed).
    - The weight-1 source (R19-6).
  - Or is a separate principle needed? For example: "the vacuum's static strain response does not gravitate", or "the gravitating source is the strain-subtracted stress".
  - Is any such principle number-free and non-signalling?
- **Setting.**
  - The C-box-E bridge with the exact W1 stresses.
  - The supplied zero-point vacuum; one loop; the TT static response at q → 0.
  - Compare with continuum GR with Lorentz-invariant regularization, where μ = 0 by Lorentz invariance of the vacuum (comparator).
- **Prior art (count once):**
  - R14-3 (μ_E), R16-9, R16-13 (μ_T2), R17-11, R17-13, R18-6, R19-5, R19-6, R19-9 and R19-11, with their verdicts;
  - PRICE_NOTE P0;
  - the R9-9 vertex.
- **Removed hypothesis:** shear rows paid by tuning only.
- **Probes.**
  - (a) Identify μ as a vacuum strain response. Is it ⟨T_ij⟩'s derivative with respect to a uniform TT strain, minus the contact term?
  - (b) Check each bridge piece for whether it cancels μ.
  - (c) If none does, the minimal principle that does, and its cost: Bianchi, signalling, numbers.
  - (d) Radiative stability of μ = 0 under each option.
  - (e) Prices.
- **FIXED readings.**
  - **STRUCTURAL-ZERO:** a stated principle (existing or new, number-free, non-signalling) forces μ_E = μ_T2 = 0 for every species at every mass. Checked.
  - **TUNING-ONLY:** a refereed demonstration that within the stated bridge class μ = 0 requires tuning at the ~1e-98 level and is radiatively unstable.
  - **OPEN:** otherwise.
- **Expectation.** TUNING-ONLY within the current bridge. A new principle ("only the strain-subtracted vacuum stress gravitates") could give STRUCTURAL-ZERO, but it would be a fifth clause, and likely the lattice analogue of requiring a Lorentz-invariant vacuum, which the lattice lacks.

#### C5 referee verdicts R19-9, R19-10 and worker readings R19-12, R19-14 (recorded 05:42Z)

- **R19-9 referee: NOT CONFIRMED (the PHOTON-EXACT). Reading OPEN.**
  - **What holds:**
    - the analytic strategy (continuum / Sylvester / dust) is a valid blueprint;
    - the fibre identification gives the correct face continuity;
    - there is no single-soft-leg Gauss-law obstruction;
    - Proposition K's C_e r⁴ costs are confirmed independently;
    - the six-knob SM root re-solves at r = 0.05–0.1, with direct N = 224 residuals < 4e-12.
  - **Why it is not yet exact torus-wide:**
    - the finite-width divided-difference fallback creates an internal discontinuity, with a residual > 1e-12 at a seam;
    - exact-zero soft legs return NaN.
  - **What is needed:** two implementation repairs and a renewed targeted check.
- **R19-10 referee: NOT CONFIRMED (the INJECTS). Reading OPEN.**
  - **Confirmed:**
    - the completed-law e₀ exists, with L⁻⁴ (gapless) or exponential (gapped) finite-size corrections;
    - the product-insertion costs: 0.04–0.06 per scalar site and 0.68–0.98 per Wilson-Dirac site;
    - Lemma S-ins, under completed-law energy accounting with bounded extraction power Γ.
  - **Why it does not establish INJECTS:** for a genuinely growing law, the axioms do not select the Hilbert-space embedding, the instantaneous Hamiltonian, the energy comparator, the insertion map, the interaction norms or event additivity.
  - **What it does establish:** a strong conditional creation-energy obstruction, and a missing condition in the C-box-E realization. It does not show that every local growing lattice violates P93.
- **R19-12 (charge block on the gravity root's edges): worker reading ONE-LAW-BILL.**
  - **Charge rows on the root edges:** F_½ = −5.24 and Σ = +0.92 to +1.04.
  - **Lemma A:** on one law the neutral species sit exactly on the tree cone, so the photon needs its own row (R16-9 missed this). The charge block is then 4 per class.
  - **Shared knobs:** the gravity stencils never enter the charge rows. The window's free direction can pay Σ = 0, because Σ and μ_T2 are both Dirac-only; roots bracket Σ = 0 near b_γ ≈ 2.93605.
  - **Bill** for SM content on one law, per (spin, |q|) class:
    - **(A):** 11 equalities + photon window + CC.
    - **(B):** at the Σ = 0 root, 11 + CC with no open selection.
    - **With (d-i):** 10 + CC.
    - **Per species:** 17 + CC.
  - **R16-10's superluminal-photon route** is incompatible with the gravity root (v_max 8.05).
  - **Prices:** P-R19-12a (photon-to-neutral row), P73 refined.

  Referee running.
- **R19-14 (other growth modes under (S)): worker reading OPEN.**
  - **Lemma G0:** on fixed sites with a uniform law, light keeps its lattice wavenumber. So a fixed grid gives no redshift (excluded), and "records carry the expansion" is V1 (growing spacing) in another frame.
  - **V1 needs no lattice-native scale:** Ġ/G = 2H is excluded by lunar ranging, and ℓ/ℓ_P drifts by ≥ 1e50.
  - **V1 under (S).**
    - e₀ ∝ a⁻⁴. A literal fixed C drifts; (d-i) cannot be posed there.
    - (S_V), which subtracts the instantaneous lowest-state stress, closes Bianchi with no signalling.
    - It leaves a second-order adiabatic lag of 0.954(1−s)²(ℓ_P/ℓ)² ρ_crit per field. That is non-negative and depends on the field-variable choice s. At s = 0 it excludes inflation unless ℓ > 100 m.
    - (S_ad), "the adiabatic lowest state weighs nothing", removes the lag with no number.
  - **Result:** V1 + (S_ad) + N_red + W1 is a homogeneous-only, 0-number candidate.
  - **Prices:** P-r1914a (S_ad), P-r1914b (tune s), P-r1914c (no lattice-native scale), P-r1914d (lattice-frame motion).

### C5 Round 19, items 16–17 (pre-registered 05:44Z, before launch)

**R19-16. Repair R19-9's photon kernel: remove the divided-difference seam and the exact-zero soft-leg NaN, then re-check exactness torus-wide.**
- **Plain question.** R19-9's referee (NOT CONFIRMED → OPEN) accepts the analytic blueprint, Proposition K and the root re-solve. Two implementation defects block PHOTON-EXACT:
  - (i) the finite-width divided-difference fallback creates an internal discontinuity with W1 residual > 1e-12;
  - (ii) exact-zero soft legs return NaN.

  Repair both. For (i), use an analytic divided difference (e.g. a Taylor or complex-step form valid uniformly). For (ii), use the analytic limit at k = 0. Then rerun the targeted and dense W1 checks, including the referee's seam and zero-leg cases, and confirm that the root re-solve is unchanged.
- **Setting:** R19-9's construction and root (U, UD, VW-exact; r = 0.05, 0.1).
- **Prior art (count once):** R19-9 and its verdict (the seam location and NaN cases), R19-5 and its verdict.
- **Removed hypothesis:** finite-width numerical fallback.
- **FIXED readings:**
  - **PHOTON-EXACT** (as in R19-9's item): W1 ≤ 1e-12 torus-wide, including the referee's seam and zero-leg cases, and the SM root re-solved with all rows zero. Checked.
  - **OPEN:** otherwise.
- **Expectation:** PHOTON-EXACT.

**R19-17. V1 + (S_ad) beyond homogeneity: is the adiabatic-lowest-state rule local, covariant and non-signalling for lumps?**
- **Plain question.** R19-14 (worker) finds that a growing-spacing lattice V1 with (S_ad), "the adiabatic lowest state weighs nothing", plus N_red and W1, is number-free in the homogeneous universe. Its price is that the lattice sets no physical scale (ℓ/ℓ_P free). Open questions:
  - Is "adiabatic lowest state" definable locally when the expansion is inhomogeneous (lumps, local strain rates)?
  - Does subtracting its stress keep Bianchi without a CMC-type global carrier (which would mean Lemma S signalling)?
  - What frame does the lattice move with (P-r1914d)?
- **Setting.**
  - V1 with a local scale factor a(x,t) (the lattice spacing follows local volume expansion θ).
  - Free fields; adiabatic expansion of the vacuum stress to second order in gradients and θ.
  - Linear perturbations of FRW with dust.
  - Excluded: site creation.
- **Prior art (count once):** R19-14 (worker), R19-10 and its verdict, R17-11 and its verdict (class 𝒟; Lemma V), R15-1 and its verdict (Lemma S), R13-3, R11-3, R12-2; adiabatic regularization and the local Hadamard / adiabatic vacuum (Parker–Fulling, RECALLED).
- **Removed hypothesis:** homogeneity.
- **Probes.**
  - (a) A local covariant form of ⟨T⟩_ad, to the stated adiabatic order.
  - (b) Bianchi and the linear signalling test (the Lemma S jump).
  - (c) The lattice-frame rule.
  - (d) Observables, including any frame dependence.
  - (e) Prices.
- **FIXED readings:**
  - **LOCAL-OK:** a local covariant (S_ad) for lumps, Bianchi-consistent with no instantaneous channel at linear order. Checked.
  - **NONLOCAL:** a refereed demonstration that (S_ad) beyond homogeneity needs a global or instantaneous carrier.
  - **OPEN:** otherwise.
- **Expectation:** LOCAL-OK to second adiabatic order. The adiabatic subtraction is the standard local Hadamard/adiabatic counterterm structure, which is covariant. The price moves to "which state is adiabatic", i.e. the frame.
- **R19-13 (entangled-born sites): worker reading NO-LOCAL-ESCAPE.** A referee is required. ENTANGLED-ESCAPE (R ≤ 10a) is excluded for every field.
  - **Best insertion cost against slab radius.** It falls as R⁻⁵ for massless fields, and as e^{−4κR} (κ = arccosh(1 + m²/2)) for massive ones.
  - **Lower bound (proved).** Fidelity and trace-distance with fixed bounding planes, which the slab cannot re-space. It holds for any slab operation.
  - **Required radius:**
    - lattice-proved: R > 256a (massless scalar and photon), 512a (Dirac), 12–16a (m ~ 1/a);
    - continuum-asymptotic: R > 1.7e23 a for massless fields.
  - **Consequences.** Ball-shaped insertions would overlap, so creation becomes collective rather than a series of local events. An entangled birth is not local.
  - **Price:** P-r1913a.

  Referee running.

### C5 Round 19, item 18 (pre-registered 05:47Z, before launch)

**R19-18. Breaking the E1/E2 tie by observation: does E2's friction, lifted to FRW, change the expansion history or structure growth measurably?**
- **Plain question.**
  - E1 (start time) and E2 (leaky waves) stay observationally tied (R14-2, R16-14, R19-8 verdict: OPEN, formal tie at the noise level).
  - R19-8 (worker) names the FRW lift of E2's friction as law data (P-r198a). If the friction also acts on the background expansion, the expansion law changes at O(γ/H) ≈ 2–5% (suggested).
  - For the friction lifts that are consistent (stated), compute the change to:
    - H(z) and distance measures;
    - growth fσ8(z);
    - the ISW effect;
    - the GW luminosity distance (friction damps the GW amplitude: d_L^GW ≠ d_L^EM).
  - Compare with data (RECALLED: DESI BAO, Planck, GW170817's d_L^GW / d_L^EM). Can these break the tie, or bound γ below R14-2's drag bound (0.016–0.047 H₀)?
- **Setting.**
  - E2 with γ in the drag-allowed range.
  - The friction lifts: (L0) acts only on perturbations relative to the FRW background in the cosmic frame; (L1) also acts on the background (state the form).
  - Linear perturbation theory.
  - The GW propagation equation h'' + (2 + ν)ℋh' + k²h = 0 with ν from γ.
- **Prior art (count once):**
  - R12-7, R14-2, R16-14, R19-8 and their verdicts (Lu et al. 2.98 H₀ benchmark; EM-counterpart scale ~62 H₀);
  - modified GW propagation and Ξ-parametrisation literature (Belgacem et al., RECALLED);
  - DESI DR2 (RECALLED).
- **Removed hypothesis:** perturbation-only friction (for L1).
- **Probes.**
  - (a) Background and growth under L1.
  - (b) d_L^GW / d_L^EM under both lifts, against GW170817 and forecast LISA/ET sirens (RECALLED).
  - (c) Bounds on γ.
  - (d) Is the tie broken: does E2 predict a signal that E1 does not?
- **FIXED readings.**
  - **TIE-BROKEN:** a stated E2 lift predicts a signal E1 does not, which is either excluded or detectable by stated (RECALLED) data or forecasts. Checked.
  - **TIE-HOLDS:** every consistent lift's signal is below current and forecast sensitivity. Checked.
  - **OPEN:** otherwise.
- **Expectation.** TIE-BROKEN under L1 by forecast sirens: d_L^GW/d_L^EM − 1 ≈ γ/(2H₀) × O(1) ~ 1–2% at z ~ 1, within ET/LISA reach. Under L0 the GW damping alone gives a similar siren signal, since E1 has none.
- **R19-11 referee: CONFIRMED WITH CORRECTIONS. Reading OPEN** (recorded 05:46Z).
  - **Confirmed:**
    - Lemma A: Wilson-Dirac rows are analytic in m, with nonzero linear terms.
    - Lemma B: scalar and vector rows are analytic in m².
    - The transversal, subluminal m → 0⁺ root.
    - SM speed residuals of 1.9e-19 to 2.4e-18, so three rows miss R16-2's comparator.
    - Shear residuals of O(1e-19). These are catastrophic only if they are identified with a canonically normalized physical graviton mass.
  - **Conditional:** the spectrum-tuned root follows from the implicit-function theorem only once a C¹ massive-vector completion is supplied.
  - **Twisted mass** leaves the conditional shear about 1e62 above the 100 Hz target.
- **R19-15 (the shear rows as a graviton mass): worker reading STRUCTURAL-ZERO on the letter, via the new clause (S\*). TUNING-ONLY content holds within the registered bridge.**
  - **Lemma H:** μ is the full Hessian of the strained zero-point energy (checked to 8e-11). The lattice vacuum is an elastic solid with cubic shear moduli.
  - **No bridge piece removes the anisotropy A = μ_E − μ_T2.** Every rotation-invariant clause ((S), (d-i), N_red, weight-1) shifts both rows equally, and exact W1 leaves the rows unchanged. At SM masses A ≈ 1e79 above the bound.
  - **Radiative instability:** O(λ²) basketball diagrams give μ_T2 ≈ 4e-9λ², which no quadratic counterterm absorbs. So a tuned zero is radiatively unstable.
  - **(S\*):** "in every uniform static background the law's lowest state contributes nothing to the gravitating source".
    - It is number-free, non-signalling at linear order and can replace (S).
    - It pays both shear rows at every mass and order for the lowest state.
    - It is a definition-type clause; the referee must rule whether that is a "principle".
  - **The matter-side version fails at two loops.**
  - **Prices:** P-R19-15a ((S\*)), P-R19-15b (whole linear response, non-local).

  Referee running.

### C5 Round 19, item 19 (pre-registered 05:48Z, before launch)

**R19-19. Extend (S\*) to O(q²): can one local, number-free source clause remove every graviton-cone row, and what does it cost?**
- **Plain question.**
  - R19-15 (worker; referee running) finds that (S\*), "the lowest state's response to uniform static deformation does not gravitate", removes the shear rows (q⁰) with no numbers.
  - The remaining graviton-cone rows (Ξ_Eg, Ξ_T2g, face1, face2) are the O(q²) coefficients of the vacuum's TT self-energy.
  - Consider (S\*\*): "the lowest state's TT response through O(q²) contributes only its Lorentz-invariant (continuum) form to the gravitating source." This is a local subtraction, since it is a Taylor polynomial in q.
  - Does (S\*\*):
    - zero every graviton-cone row for every species at every mass, with no tuning;
    - stay local, covariant and non-signalling;
    - leave only the charge block (R16-2/R19-12) plus the CC?
  - What does it cost? Is it radiatively stable? Does it conflict with the refereed W1 / weight-1 results?
  - Does it also affect matter's own cone rows? (It should not: those come from the matter self-energy, not the graviton's.)
- **Setting.**
  - The SM root (R18-9/R18-13/R19-9/R19-11) and its vertices.
  - Graviton TT self-energy Π_TT(q) from the vacuum loops.
  - (S\*\*) defined as subtracting Π_TT's Taylor coefficients at q⁰ and q² minus their continuum Lorentz-invariant values.
  - One loop, plus the R19-15 two-loop model for the radiative check.
- **Prior art (count once):**
  - R19-15 (worker) and its referee when back;
  - R17-3 (S accepted as a principle);
  - C4 V3's R₀ (called tautological);
  - R16-3 (IBP identity: the Ξ rows as q² coefficients);
  - R17-4 (off-axis);
  - R19-12 (the bill);
  - R9-9 (vertex prescription).
- **Removed hypothesis:** the cone rows paid by tunings.
- **Probes.**
  - (a) The clause as an equation.
  - (b) Its effect on each of the six rows.
  - (c) Locality, Bianchi and signalling.
  - (d) What remains at O(q⁴) and beyond. The O(q⁴) remainder gives dispersion such as ω² = k² + αk⁴a²; check it against GW170817 and Fermi-LAT-type bounds at a = ℓ_P (RECALLED).
  - (e) The two-loop check.
  - (f) The new bill.
- **FIXED readings.**
  - **CONE-PRINCIPLE:** a stated local, number-free, non-signalling clause zeroes all six graviton-cone rows for every species and mass, with O(q⁴) remainders below bounds. Checked.
  - **TAUTOLOGY-OR-CONFLICT:** a demonstration (refereed) that the clause either conflicts with a refereed result (W1, weight-1, Bianchi) or is equivalent to assuming the answer in a way that makes it non-predictive.
  - **OPEN:** otherwise.
- **Expectation.** CONE-PRINCIPLE on the letter, with the honest caveat that the clause is a renormalization condition dressed as a principle. The bill drops to the charge block plus the CC. The referee's judgement on tautology decides.
- **R19-18 (E1/E2 observational tie-break): worker reading OPEN.**
  - **FRW lifts of E2's friction:**
    - L0 (perturbations only) is consistent.
    - L1-H and L1-S (gothic, local) are consistent, but give a negative-energy w = −1/2 sink.
    - L1-M (fixed global reference) is not consistent.
  - **The GW equation** is h'' + (2 + γ/H)ℋh' + k²h = 0 in every lift.
  - **The unique E2 signal:** d_L^GW/d_L^EM = exp(γt_lb/2). At z = 1 it is 0.44–1.30% at the drag ceilings, while E1 predicts exactly 1.
  - **Current data cannot see it:** GWTC-3 gives γ < 1.35 H₀, and GW170817 ≤ 2.3e-4.
  - **Forecasts:** ET reaches ≥ 3σ only for γ ≈ 0.039–0.047 H₀ (toy, optimistic). L1 background and growth changes are ~1–2%, not excluded by DESI DR2 + CMB (compressed, RECALLED).
  - **The tie holds** at and below the signed drag ceiling (0.024 H₀). E2 can be confirmed only if γ is near its ceiling, and can never be excluded as a class. A significant Ξ₀ < 1 would exclude both routes.
  - **Correction to R19-8:** the 2–5% was the sink's density parameter, not the change in H.
  - **Prices:** P-r1918a (lift L0), P-r1918b (L1-H).
  - Not a no-go; a referee is optional.

### C5 Round 19, item 20 (pre-registered 06:05Z, before launch)

**R19-20. Audit: do the source clauses — (S) or (S\*), (d-i) or (S_ad), N_red, W1, (S\*\*) — reduce to one statement, "the vacuum gravitates only through its Lorentz-invariant renormalized form"? If so, is the grid then predicting anything about gravity, or only stipulating GR?**
- **Plain question.** C5's source-side results move each grid defect of the vacuum into a number-free clause about what gravitates:
  - the constant (S);
  - the enthalpy ((d-i), or (S_ad) on V1);
  - the gauge-dependent zero point (W1);
  - the shear (S\*);
  - possibly the O(q²) rows (S\*\*, R19-19, running).

  Is there one clause that implies them all? A candidate: "the gravitating source is ⟨T⟩ minus the lowest state's response through O(q²), replaced by its Lorentz-invariant form."

  If so:
  - (i) Is that clause stating that the vacuum's gravitational effect is exactly GR's, i.e. imposing relativity at the source rather than deriving it?
  - (ii) What observable content, if any, distinguishes "grid + clause" from "GR + SM with a Lorentz-invariant regulator"? Candidates: O(q⁴) dispersion, the charge-block counterterms, the W7 anomaly, relic corner states, the E1/E2 noise.
  - (iii) What is the minimal honest statement for the owner?
- **Setting.**
  - The refereed and worker records from R16 to R19.
  - S26 §4 and the price ledger.
  - The axiom texts (AX:85-90, 116-130, 182-190).
- **Prior art (count once):**
  - all R17-3 … R19-19 source-side items and their verdicts;
  - SUMMARY §17 (the root obstruction);
  - C4 V3 (tautology precedent);
  - R16-6 / Lemma PT (counterterm precedent).
- **Removed hypothesis:** clauses judged one at a time.
- **Probes.**
  - (a) Write the single clause, and prove or disprove that it implies each existing clause.
  - (b) List every observable the grid still predicts beyond GR + SM with the clause, with sizes at a = ℓ_P.
  - (c) The owner-facing statement.
- **FIXED readings.**
  - **ONE-CLAUSE:** a single stated clause implies all the listed source clauses, checked. Report its remaining predictions.
  - **IRREDUCIBLE:** a demonstration that at least two of the clauses are logically independent, with the reason stated.
  - **OPEN:** otherwise.
- **Expectation.** ONE-CLAUSE. The clause is "renormalize the vacuum's gravitational response to its Lorentz-invariant form through O(q²)". The grid's gravitational predictions then reduce to the residual list in (b): charge-block tunings, W7 edge anomalies, relics, O(q⁴) dispersion and set A noise. That is an honest finding the owner needs.

#### C5 referee verdicts R19-12, R19-13 and the R19-17 worker reading (recorded 06:06Z)

- **R19-12 referee: CONFIRMED WITH CORRECTIONS. Reading: ONE-LAW-BILL for route A.**
  - **Charge values on the root's edges:** F_½ = −5.2444, F_0 = −1.1674, G_½ = 0.11484, Σ = 0.9187.
  - **Neutral classes** are exactly unshifted within the QED truncation.
  - **Charge-block cost** at minimum: 4 per class, 10 per species, or 2 q²-correlated payments.
  - **Route A:** a checked bill of 11 equalities, plus one photon-window selection, plus the CC. Under conditional (d-i) it is 10 plus the window plus the CC.
  - **Route B:** 11 + CC with no open selection. The numerics bracket it strongly, but it is conditional on gravity-branch continuity and on off-axis closure at the 0⁺ root.
  - **Not covered:**
    - exact W1;
    - W± and the non-Abelian sectors;
    - matter graviton-loop speeds;
    - mixed O(Ge²);
    - radiative stability.
- **R19-13 referee: CONFIRMED WITH CORRECTIONS. Reading NO-LOCAL-ESCAPE.**
  - **Scope:** the nearest-neighbour free scalar under plane insertion.
  - **The bound holds for every deterministic CPTP slab operation**, including ones with local ancillas.
  - **The proved radius is R > 256a.** The referee evaluated ΔE_min(256) ≥ 2.28e-18 independently. This holds under either accounting, so R ≤ 10a is excluded.
  - **1.7e23 a is an estimate, not a bound:** a credible asymptotic estimate only.
  - **Not established:** no universal photon, interacting-law or arbitrary-growth no-go follows.
- **R19-17 (V1 + (S_ad) beyond homogeneity): worker reading LOCAL-OK** in class 𝒱 (V1 with comoving lattice-frame fields, H-cov).
  - **(S_ad) is local and covariant through adiabatic order 2.**
    - Order 0 is an elastic cubic solid.
    - Order 2 gradient terms are fitted locally to within 1–2%.
    - The lag formula holds pointwise with the local H.
  - **Lemma N:** ∇T_grav = F_I∇X^I, with F_I the excitations' force on the lattice. There is no global carrier. With c = 1 for dust, F = O(ε³), so Bianchi holds at linear order and there is no Lemma-S channel. The vacuum response is causal.
  - **Lattice-frame law:** W (weightless, an elastic test medium) or A (absent). This is new completion data.
  - **The order-2 terms are the induced G,** so (S_ad) must subtract them and G is fully supplied.
  - **Prices:** P-r1917a, b and c.
  - A referee is optional.
- **R19-15 referee: CONFIRMED WITH CORRECTIONS. Reading: STRUCTURAL-ZERO on the literal wording, by stipulation** (recorded 06:10Z).
  - **Lemma H is confirmed.** The shear rows are the complete uniform-strain Hessian of the lowest-state energy, seagull included. Separable T₂g flow is Liouville-invariant.
  - **The registered clauses do not touch the cubic anisotropy.** The isotropic source/receiver clauses leave it unchanged, and so does exact W1.
  - **The registered route needs tuning.** Conditional on the dynamical graviton bridge, it requires a radiatively unstable ~1e-98 tuning, with explicit two-loop detuning in the NN λφ⁴ model.
  - **(S\*) meets the wording but is not a mechanism.** It is a stipulated renormalization/source definition, not a derived Ward mechanism.
  - **Not established:** a nonlinear Bianchi completion, and a universal matter-side two-loop no-go.
- **R19-19 ((S\*\*) at O(q²)): worker reading CONE-PRINCIPLE on the letter.** The tautology question goes to the referee.
  - **The clause (S\*\*₀):** the lowest state contributes nothing to the gravitating source through second order in metric derivatives, at linear order in h. It is local and number-free, and it zeroes all six graviton-cone rows for every species, mass and loop order by construction.
  - **Lemma G (exact linear algebra).** Under the full linearized-diffeo Ward identity, only an isotropic speed shift is allowed. So 5 of the 6 rows are the vacuum response's own Ward violations, and only the isotropic graviton speed is a gauge-invariant LV coefficient.
  - **Lemma E.** The clause is 31–32 linear conditions. At O(p²) it cannot fail any cone observation; that is the "assumes the answer" half.
  - **O(q⁴) remainder:** |δc/c| ~ 1e-84 at 100 Hz.
  - **Bill under (S\*\*):** 4 per class + CC, i.e. charge counterterms only. The gravity block costs 0 numbers.
  - **Main risk (state-tied subtraction).** Before the electroweak crossover the subtracted lowest state differs from the actual state. The shear mismatch is then tachyonic (|m_g| ~ 6e10 GeV, or ~170 GeV with twisted mass), which would be catastrophic if μ is a canonical graviton mass.
  - **Prices:** P-R19-19a ((S\*\*₀)), b (Z) and c (nonlinear extension, non-lowest states).

  Referee running.

### C5 Round 19, item 21 (pre-registered 06:12Z, before launch)

**R19-21. The state-tied subtraction: do (S\*) and (S\*\*) survive cosmic history (the electroweak crossover, a thermal plasma), or does a mismatch in the shear and cone rows ruin the early universe?**
- **Plain question.**
  - (S\*) and (S\*\*) subtract the lowest state's strain response (R19-15 refereed: a stipulated source definition; R19-19 worker).
  - The real universe was not in today's lowest state. Before the electroweak crossover the fermions were nearly massless, and the plasma was thermal.
  - R19-19 (worker) estimates a tachyonic shear mismatch Δμ ≈ −5e-19 per cell before the crossover, |m_g| ~ 6e10 GeV, if μ acts as a canonical graviton mass.
  - Questions:
    - (i) Is the thermal or pre-crossover strain response's shear part, at the relevant temperatures and masses, actually of that size and sign?
    - (ii) Does a thermal plasma's own (non-vacuum) shear response, which is physical, dominate?
    - (iii) Is there a state-tracking version that keeps Bianchi? For example, "the instantaneous law's lowest state", or the local equilibrium state. R17-7 says a varying algebraic C needs a local carrier, and R19-17 suggests the lattice frame X could carry it.
    - (iv) What does each version predict for primordial tensor modes and for growth before the crossover?
- **Setting.**
  - The SM root edges (R19-11's 0⁺ root).
  - Thermal states at T between 1 GeV and 1e16 GeV (a·T ≪ 1).
  - The shear rows μ_E and μ_T2 of (a) the vacuum at the pre-crossover masses and (b) the thermal state.
  - The canonical graviton-mass reading (with vR19-11's conditional) and the alternative "μ is not a mass" readings.
- **Prior art (count once):** R19-15 and its verdict, R19-19 (worker), R19-11 and its verdict, R17-7 (S′ variants; Bianchi and carrier), R19-17 (Lemma N; frame carrier), R18-2 (EW vacuum), solid-inflation and massive-graviton cosmology (RECALLED).
- **Removed hypothesis:** the universe always in today's lowest state.
- **Probes.**
  - (a) The size and sign of Δμ_vac, and the thermal μ_th(T), on the root edges.
  - (b) Which dominates, and the resulting graviton mass² history.
  - (c) The state-tracking variant's Bianchi and carrier.
  - (d) The observational consequences: tensor modes, BBN expansion rate, GW background.
  - (e) Prices.
- **FIXED readings.**
  - **HISTORY-SAFE:** a stated version, either (S\*\*) or a state-tracking variant, keeps every pre-crossover effect below the stated observational bounds without a new number. Checked.
  - **HISTORY-CONFLICT:** a refereed demonstration that every stated version yields an excluded early-universe effect (e.g. a tachyonic instability faster than H, or erased tensor modes conflicting with data), or needs a ~1e-67 tuning.
  - **OPEN:** otherwise.
- **Expectation.** HISTORY-CONFLICT for fixed (S\*\*) under the canonical-mass reading, since |m_g| ≫ H. A state-tracking variant could be HISTORY-SAFE if the frame field carries the drift (R19-17). The thermal μ_th is likely the dominant physical piece, and in a plasma it is a genuine, observable effect.

### C5 Round 19, item 22 (pre-registered 06:14Z, before launch)

**R19-22. Pricing the supplied graviton: how large a finite site space reproduces the CCR N-type graviton to observational accuracy?**
- **Plain question.**
  - Every refereed route to producing the graviton from qubits fails or stays open:
    - integer-law k⁴ (R16-7, R16-11);
    - the Z₂ window with no light-like branch (R17-1, R17-6, R18-1, R19-1, R19-7).
  - The only working source is P-N1: supplied CCR (noncompact) tensor pairs, R15-5's exact N-type with ω = |k|. That violates "one M₂(C) per site" (AX:47).
  - How expensive is P-N1, made finite? Truncate each CCR pair to a spin-S or clock-N representation, e.g. Holstein–Primakoff / large-S, or a Z_N clock with N → ∞.
    - At what S or N does the graviton branch stay light-like, with z = 1 and the 1/r pull, to the accuracy GW170817 (|c_g − c| ≲ 1e-15) and Newtonian tests need, at the accessible energies?
    - Is the error ∝ 1/S, or exponentially small?
    - How many qubits per site does that mean (log₂(2S+1) per slot)?
- **Setting.**
  - R15-5's exact N-type theory with CCR replaced by spin-S (Holstein–Primakoff) or a Z_N clock with a large-N rotor limit.
  - The R16-7 and R17-1 machinery: f-sum classes, compactness ladder.
  - Linear response at k ≪ 1/a, with occupation ≪ S.
- **Prior art (count once):**
  - R15-5 and its verdict (the compactness ladder, Lemma L: qubit/qubit gives z = 3, rotor rungs give z = 2);
  - R16-7, R16-11, R17-1 and R17-6 with their verdicts;
  - the quantum-link / large-S approach to U(1) photons (RECALLED; e.g. Banerjee et al., quantum link models; Wiese).
- **Removed hypothesis:** exactly CCR or exactly qubit, as opposed to finite S.
- **Probes.**
  - (a) The dispersion and static response of the spin-S N-type graviton at k ≪ 1/a: how the z = 1 branch is recovered as S → ∞, and its error scaling.
  - (b) Whether the compactness ladder (k³ / k² rungs) moves with S: does the crossover scale k_c(S) → 0?
  - (c) The S needed for GW170817 at a = ℓ_P for LIGO-band k, and for the 1/r pull.
  - (d) Qubits per site, and the AX:47 price.
- **FIXED readings.**
  - **FINITE-PRICE:** a stated S (or N) and qubit count per site that reproduces the graviton to the stated bounds at the relevant k. Checked, with the scaling law.
  - **NO-FINITE:** a demonstration (refereed) that no finite S reproduces z = 1 at any k, e.g. compactness forces k³ for every finite S.
  - **OPEN:** otherwise.
- **Expectation.** FINITE-PRICE. The truncation error is controlled by occupation/S, and the z = 1 branch holds for k ≫ k_c(S) ~ 1/(aS^p). Modest S (tens of qubits per site) suffices at LIGO wavelengths, because the relevant occupations are tiny. That would give an honest price for "supply the graviton": a larger site space, not an extra field.
- **R19-16 (repair of the photon kernel): worker reading PHOTON-EXACT.**
  - **The two defects reproduced** exactly with the R19-9 referee's script.
  - **Three repairs:**
    - R1: a Hadamard-integral divided difference, uniform over the torus.
    - R2: an analytic soft-leg series, finite at exact zero.
    - R0: an analytic photon law. The archived table was piecewise linear and caused a 5e-4 kink at every node; that kink is the source of the referee's 1.49e-5 jump.
  - **W1** now holds to ≤ 2.3e-15 everywhere tested, including the seam and exact zero legs.
  - **The root re-solves:**
    - photon-bearing rows ≤ 1.4e-12;
    - μ_E at the scalar/Dirac evaluator floor of ~5e-11;
    - knob shifts ≤ 4e-8.
  - **Evaluator fact on record:** the archived tabulated photon law used by R18-9, R18-13 and R19-9 differs from the stated law by up to 1.9e-9 in c.

  Referee running.

### C5 Round 19, item 23 (pre-registered 06:13Z, before launch)

**R19-23. Are the five Ward-violating cone rows physical observables or prescription artefacts?**
- **Plain question.**
  - R19-19 (worker; referee running) shows by exact linear algebra (Lemma G) that, under the full linearized-diffeo Ward identity, only an isotropic graviton speed shift is allowed. The other five rows (E_g − T₂g birefringence, face1's K₆ part, face2 − T₂g, μ_E and μ_T2) are Ward violations of the vacuum response.
  - Two readings follow:
    - (i) the rows are real, gauge-invariant effects of a grid that breaks the graviton's gauge symmetry, and observable, e.g. as GW birefringence or a graviton mass;
    - (ii) the rows are artefacts of a matter–graviton coupling that is not consistently gauge-completed at second order (W2 is excluded on the lattice by W15).
  - If (ii) holds, the physical bill drops to one row: the isotropic speed. If (i) holds, these rows signal extra propagating graviton polarizations or gauge-symmetry breaking, which is constrained independently.
- **Setting.**
  - R9-9's N-type graviton (state whether its gauge group is full or spatial-only).
  - The SM root's vacuum response Π.
  - Gauge-invariant observables: GW phase velocity per polarization from the full quadratic action (graviton kinetic term plus Π); the number of propagating modes (does Ward violation add scalar or vector modes?); the static potential between sources.
  - Linear order, one loop.
- **Prior art (count once):**
  - R19-19 (Lemma G, worker), R19-15 and its verdict, R19-5 and its verdict (W1 exact, W2 not);
  - R16-5, R17-5 and R17-8 (W15);
  - R13-5;
  - Fierz–Pauli / vDVZ and massive-gravity mode counting (RECALLED).
- **Removed hypothesis:** the rows read directly as observables.
- **Probes.**
  - (a) The quadratic action graviton plus Π, its propagating modes and their dispersion for each polarization.
  - (b) Which rows change a gauge-invariant observable, and which are removable by field redefinition or gauge choice.
  - (c) The extra modes, if any, and their coupling to matter.
  - (d) Bill consequences.
- **FIXED readings.**
  - **PHYSICAL:** a demonstration that the five rows change gauge-invariant observables (polarization-dependent speeds, masses, or extra modes). Checked, and refereed if class-wide.
  - **ARTEFACT:** a demonstration that the five rows are removable, or do not enter any gauge-invariant observable at linear order. Checked, and refereed.
  - **OPEN:** otherwise.
- **Expectation.** PHYSICAL. Ward violations in a graviton self-energy generically give mass terms and extra polarizations (Fierz–Pauli logic), so the rows are observable and the bill stands. The extra modes may themselves be a new wall: a vDVZ-type discontinuity or a ghost.
- **R19-20 (source-clause audit): worker reading IRREDUCIBLE.**
  - **The vacuum clauses collapse into one.** (S), (S\*) and (S\*\*) are truncations of one rule, (Σ): "the lowest state's gravitational effect through two derivatives is replaced by its Lorentz-invariant form with zero CC".
  - **The full set does not.** W1-weight and N are logically independent of (S\*), with explicit models. The carrier is separate.
  - **Minimal bridge:** (Σ) + W1-weight (including gravity's own stress) + a carrier. That is 3 clauses and 0 numbers.
  - **The count** (checked; it reproduces R19-19's Lemma G). The local vacuum response through two derivatives has 34 numbers; a Lorentz/diff-invariant vacuum has 2. (Σ) sets:
    - 30 by Ward identities;
    - 2 by Lorentz conditions;
    - 1 by Λ = 0;
    - 1 by convention.
  - **Reading: gravity is GR by stipulation**, for the lowest state, through two derivatives, at linear order. The grid adds nothing measurable for today's vacuum.
  - **Grid-specific residuals:**
    - the pre-crossover shear mismatch (tachyonic, conditional);
    - a pre-crossover enthalpy mismatch, ~7e106 ρ_Λ for the top quark (illustration). (d-i) absorbs it; (S\*), (S\*\*) and (S_ad) do not;
    - site-creation injection;
    - the W7 anomaly;
    - relics;
    - the charge-block tunings.
  - **The top-mass test** (M_t ≤ 170.9) comes from Λ = 0 and is not specific to the grid.
  - **Registration collision:** ONE-CLAUSE and IRREDUCIBLE are not mutually exclusive. IRREDUCIBLE is reported under the literal-first rule.

  Referee running.

### C5 Round 19, item 24 (pre-registered 06:32Z, before launch)

**R19-24. Can the charge block be paid the same way? Is there a number-free clause for the matter and photon light cones, or must they stay counterterms?**
- **Plain question.**
  - R19-20 (worker; referee running) reads the gravity sector as GR by stipulation via (Σ). (Σ) is a source clause: it changes what gravitates, not how matter moves.
  - The charge block (4 per class, 10 per species; R19-12 refereed) consists of matter and photon propagation speeds, which are dynamics. A source clause cannot touch them.
  - Is there a number-free dynamical clause, for example "the law's quadratic effective action for every species is Lorentz-invariant through two derivatives at one loop", that zeroes the charge rows?
    - (i) Is such a clause a law-level statement, or does it require counterterms, i.e. numbers, in the law?
    - (ii) Is it consistent with gauge invariance (Peierls coupling, the Ward identity) and locality?
    - (iii) Is it radiatively stable?
    - (iv) If it requires numbers, how many, and how precisely tuned? This is P73, restated.
  - Contrast with (Σ): why can a source clause be number-free while a dynamics clause cannot? Or can it?
- **Setting.**
  - One-loop QED on the SM root's edges (R19-12).
  - The counterterm basis (rule `TESTS:5700`).
  - Candidate clauses:
    - (D1) "the law includes whatever local quadratic terms make each species' one-loop dispersion Lorentz-invariant to O(q²)", i.e. the law depends on its own loop corrections;
    - (D2) a symmetry that forces it;
    - (D3) RG fixed-point arguments (RECALLED: Collins et al. on Lorentz violation in loops).
- **Prior art (count once):**
  - R16-1, R16-2, R16-10 and R19-12, with their verdicts;
  - R13-7 (no structural zero);
  - R10-1 and R11-1 (pairing is necessary for an untuned cancellation);
  - R19-15, R19-19 and R19-20 (the source clauses);
  - Collins–Perez–Sudarsky–Urrutia–Vucetich (RECALLED).
- **Removed hypothesis:** counterterms as the only route.
- **Probes.**
  - (a) Classify D1–D3.
  - (b) For D1: is "a law that contains its own one-loop counterterm" self-consistent, and is it number-free? What happens at two loops?
  - (c) The source-versus-dynamics asymmetry.
  - (d) Prices.
- **FIXED readings.**
  - **DYNAMIC-CLAUSE:** a stated number-free, local, gauge-invariant clause that zeroes the charge rows at one loop and stays zero at two loops. Checked.
  - **COUNTERTERMS-NEEDED:** a refereed demonstration that every clause in a stated class amounts to tuned counterterms (numbers) that must be re-set at each loop order.
  - **OPEN:** otherwise.
- **Expectation.** COUNTERTERMS-NEEDED. A dynamics clause that refers to its own loop corrections is a renormalization condition whose coefficients are numbers fixed order by order, which is P73. The asymmetry with (Σ) is that (Σ) subtracts the result after the fact, from the source, and never feeds back into propagation.
- **R19-22 (finite-site supplied graviton): worker reading OPEN.** FINITE-PRICE is not met, and neither is NO-FINITE. The expectation of tens of qubits per site fails structurally.
  - **Truncating the modes is cheap.** Single-mode truncation error is 1/S for spins and e^(−1.45N) for clocks. The helicity-±2 modes stay light-like under every local completion.
  - **Exact constraints are impossible on finite slots.** The N-type graviton needs two exact gauge constraints, and those need [h, E] = i·1, which is impossible in finite dimensions (trace argument). The constraints are what remove the partners, and the conformal sector carries the 1/r pull.
  - **Theorem B holds for any finite spectrum.** The TT f-sum is O(k⁴) at every S.
  - **Lemma J.** With spin-S fields, the constraints stop commuting and the only joint solution is the zero state.
  - **Proposition C.** With penalty constraints, the graviton sector sits ≥ (3/4)JS above the ground state. Every local repair fails: a Jordan chain, a tachyon, or six gapless branches.
  - **Exact clocks** spread labels uniformly across the wrap.
  - **Conditional on an unbuilt protection mechanism,** ~30–2000 qubits per cell would suffice.
  - **The irreducible price** is noncompact exact gauge (P-N1 + P-r15-5b), not a larger site.
  - **Prices:** P-r19-22a (a larger site algebra), b (an unbuilt protection) and c (a metastable sector).

  Referee running.

### C5 Round 19, item 25 (pre-registered 06:39Z, before launch)

**R19-25. The finite-site graviton with weakly imposed (Gupta–Bleuler / BRST-type) constraints: does it escape Lemma J and Proposition C?**
- **Plain question.**
  - R19-22 (worker; referee running) finds that exact gauge constraints are impossible on finite slots, by the trace argument; that Lemma J kills the joint constraint space; and that penalties leave the graviton sector at least (3/4)JS above the ground.
  - Its open windows include weakly imposed constraints. In those, physical states satisfy ⟨G⟩ = 0, or only the positive-frequency half annihilates them, rather than G|ψ⟩ = 0.
  - On spin-S or clock slots, does a weak (Gupta–Bleuler-like) or BRST-cohomology definition of the physical space give:
    - exactly two helicity-±2 light-like branches;
    - a positive physical norm;
    - the conformal 1/r pull;
    - with errors decaying in S?
  - What does it cost: ghosts, an indefinite metric, a non-local projector?
- **Setting.**
  - R15-5's N-type on spin-S (Holstein–Primakoff) or Z_N slots.
  - The physical space defined by:
    - (a) Gupta–Bleuler, G⁽⁺⁾|ψ⟩ = 0 with an indefinite metric;
    - (b) BRST cohomology, with fermionic ghost slots added per cell;
    - (c) a local projector, if one exists.
  - Linear response, k ≪ 1/a.
- **Prior art (count once):** R19-22 (worker) and its referee when back; R15-5 and its verdict; R16-7 and R16-11; quantum link models and BRST on the lattice (RECALLED).
- **Removed hypothesis:** strong (exact) constraints.
- **Probes.**
  - (a) Check the construction is consistent at finite S: is the weak condition preserved in time, and does the BRST operator square to zero?
  - (b) Physical spectrum and norm.
  - (c) The 1/r pull.
  - (d) The S needed, and the ghost-slot price.
  - (e) Prices against AX:47.
- **FIXED readings.**
  - **WEAK-ESCAPE:** a finite-S construction with positive-norm physical space, exactly two light-like helicity-±2 branches and a 1/r pull to stated accuracy. Checked.
  - **WEAK-OBSTRUCTED:** a refereed demonstration that every weak or BRST definition in a stated class fails at finite S, e.g. Q² ≠ 0, or the weak condition is not preserved, or the norm turns negative.
  - **OPEN:** otherwise.
- **Expectation.** WEAK-OBSTRUCTED. The finite-S constraints do not close (Lemma J), so the BRST charge does not square to zero and the Gupta–Bleuler condition is not preserved, both at O(1/S). An O(1/S) approximate version may hold, with a 1/S leak into unphysical states.

#### C5 referee verdicts R19-14, R19-16, R19-17, R19-18, R19-19 and the R19-23 worker reading (recorded 06:38Z)

- **R19-14 referee: CONFIRMED WITH CORRECTIONS. Reading OPEN.**
  - Lemma G0 does not follow from translation covariance for interacting or general time-dependent laws.
  - The s = 1 comparator has no instantaneous ground state for massless modes with ω ≤ H, so (S_ad) is not a checked global homogeneous completion.
  - The ℓ/ℓ_P drift at 10 MeV reheating is 4.86e36, not ≥ 1e50.
  - The lag coefficient and the conditional inflation arithmetic reproduce.
- **R19-16 referee: NOT CONFIRMED (the PHOTON-EXACT). Reading OPEN.**
  - **Repaired:**
    - the original 1e-7 seam and the exact-zero NaN;
    - R0 restores the analytic law;
    - R2 installs finite soft-leg limits;
    - W1 holds to machine precision at every tested point;
    - the six-row root re-solves at the numerical floor.
  - **Still broken:** R1 is not analytic on the whole torus. At the wrapped-transfer cut q_j = ±π it has opposite divided-difference limits, which gives an O(1) physically projected kernel jump. So the object is not yet a smooth, quasi-local class-𝒢 exact completion.
- **R19-17 referee: CONFIRMED WITH CORRECTIONS. Conditional LOCAL-OK** for the planar NN-scalar, constant-mass cold-dust class.
  - It is a newly priced W/A completion.
  - The full order-2/T₂g sector and other fields are uncomputed, and complete 3D hyperbolicity is not established.
  - The strict lattice light-cone claim is false; only rapid suppression outside the cone is shown.
  - The induced-G and "no standing memory" wording is too strong.
- **R19-18 referee: NOT CONFIRMED (the OPEN). Literal reading TIE-BROKEN.**
  - Under L0, E2 predicts d_L^GW/d_L^EM = exp(γt_lb/2), a 0.44–1.30% excess at z = 1.
  - The worker's optimistic ET-like case reaches 3.0–3.7σ for 0.039 ≤ γ/H₀ ≤ 0.047, which satisfies the literal TIE-BROKEN branch.
  - Arbitrarily small γ remains observationally degenerate.
  - The L1 arithmetic is a separately stipulated completion.
- **R19-19 referee: CONFIRMED WITH CORRECTIONS. Reading TAUTOLOGY-OR-CONFLICT.**
  - **Confirmed:**
    - the 32-dimensional classification and its full and spatial Ward images are exact;
    - (S\*\*₀) locally and number-freely removes all six lowest-state cone rows wherever the Taylor jet exists;
    - the bill falls to the charge block.
  - **Why the reading is TAUTOLOGY-OR-CONFLICT:** the gravity zero is imposed rather than predicted.
  - **Not closed:**
    - universal remainder bounds;
    - massless logs;
    - nonlinear causality;
    - exact Bianchi completion.
  - **The pre-electroweak instability** remains conditional.
- **R19-23 (are the Ward-violating rows physical?): worker reading PHYSICAL.**
  - **The gauge group** of R9-9's graviton is the full linearized-diffeo group.
  - **Lemma I:** E_g (B₁), T₂g (B₂) and face2 (A₂) are isolated irreps with no gauge directions. So μ_E, μ_T2, Ξ_Eg − Ξ_T2g and face2 − Ξ_T2g are exact invariant poles for any covariant response.
  - **face1:** its pole is a Schur complement over the A₁ gauge directions. It differs from the row by 9–65%. The face1 payments in R18-13 and R19-12 are therefore conditional on the uncomputed A₁ block (P-R19-23a).
  - **Shear rows are canonical TT pole masses.** They give 2 propagating branches with no vDVZ jump: the Lorentz-violating m₀ = 0 massive-gravity phase. This supplies the zero-temperature part of vR19-11's missing bridge.
  - **Speed-row Ward violations** add a time-diffeo Goldstone π⁰ whose stability depends on the sample. This is a candidate new wall (P-R19-23b).

  Referee running.

### C5 Round 19, item 26 (pre-registered 06:40Z, before launch)

**R19-26. Close the photon kernel at the wrapped-transfer cut q_j = ±π.**
- **Plain question.** R19-16's referee (NOT CONFIRMED → OPEN) finds that R1, the Hadamard divided difference, has opposite limits at the wrapped-transfer cut q_j = ±π. That gives an O(1) physically projected kernel jump, so the photon completion is not yet smooth or quasi-local.
  - Is the cut intrinsic? For example, does a periodic σ² imply that its divided difference must jump where the transfer momentum wraps?
  - Or can it be removed? Candidates:
    - a fibre identification I that is twisted at the cut;
    - a choice of transfer representative tied to the stress placement;
    - using R8-2's continuous dust kernel variant.
  - If it is intrinsic, is it a physical defect (the photon stress is non-local at the zone face), or a removable coordinate artefact?
- **Setting.** R19-9/R19-16's kernel at the root; the referee's cut-check script at scratchpad/C5/ref_R19-16.
- **Prior art (count once):** R19-9 and R19-16 with their verdicts; R8-2 Construction A; R16-5 (W15 face issues); R18-12 (corner and face states).
- **Removed hypothesis:** an untwisted, transfer-cut divided difference.
- **FIXED readings.**
  - **PHOTON-EXACT:** a W1-exact (≤ 1e-12), smooth, quasi-local photon completion with no O(1) jump anywhere on the torus, including the q = ±π cut. The root is re-solved. Checked.
  - **CUT-INTRINSIC:** a refereed demonstration that no smooth exact completion exists in the stated class because of the wrap, with the cut named as a photon-sector face defect.
  - **OPEN:** otherwise.
- **Expectation.** PHOTON-EXACT via a twisted fibre identification. The cut is a branch-choice artefact, like the face continuity R19-9 already repaired with I.
- **R19-21 (the state-tied subtraction across history): worker reading HISTORY-SAFE on the letter, narrowly, via a new clause (S_loc) plus (d-i), in C-box-E.**
  - **Every fixed lowest-state version is excluded under the canonical-mass reading.** This covers (S\*), (S\*\*), the instantaneous law and (S_ad). The Higgs-vev and thermal channels re-mass the lattice-scale sea and keep |m_g| ≫ H, tachyonic over most of history, from 1e15 GeV to BBN.
  - **The mass-even part flips sign near 0.5 TeV.** So it is tachyonic on one side of that temperature whatever the sign.
  - **Today's matter closes the massive-sign escape.** Intergalactic matter shifts the Higgs vev, giving |m_g| ≈ 1.4e-9 eV, about 1e14 above the LVK bound.
  - **The plasma's own shear is small,** about (Ta)⁶.
  - **(S_loc):** the LV part of the lowest state's strain response, re-evaluated at the actual state's local IR mean fields, does not gravitate.
    - It leaves only a T⁶ residue.
    - Bianchi reduces to R19-17's frame condition (automatic under reading A).
    - The isotropic enthalpy needs (d-i).
    - Beyond O(λ) it needs a UV/IR split with an unestimated ambiguity.
  - **Enthalpy on the D1 root.** The symmetric-phase ΔW ≈ 2.7e106 ρ_Λ, which (d-i) absorbs and nothing else registered does. On V1 nothing absorbs it.
  - **Prices:**
    - P-R19-21a: (S_loc), with zero numbers but state-dependent;
    - P-R19-21b: a mass-blind law, which is a tuning.

  Referee running.

### C5 Round 19, item 27 (pre-registered 06:42Z, before launch)

**R19-27. V1's enthalpy gap: does a growing-spacing lattice have any receiver for the vacuum enthalpy mismatch, or is V1 excluded by history?**
- **Plain question.**
  - On V1 (growing spacing, fixed sites), (S_ad) with N_red and W1 is number-free and LOCAL-OK in a stated class (R19-14, R19-17; refereed with corrections).
  - R19-20 and R19-21 (workers) find a vacuum enthalpy mismatch in non-lowest states (pre-crossover, BBN, today's matter): ΔW ~ 1e106 ρ_Λ in the symmetric phase.
  - (d-i) absorbs that mismatch only where the spatial trace equation is unimposed (C-box-E with site creation). (d-i) cannot be posed on V1 (R17-11, R19-14).
  - Does V1 admit any receiver, e.g. through R19-17's lattice frame (readings W and A), or through V1's spacing dynamics?
  - Or does the enthalpy mismatch exclude V1 under N_red?
- **Setting.**
  - V1 with comoving frame fields X^I (R19-17's class 𝒱).
  - (S_ad) or (S_loc).
  - The enthalpy mismatch ΔW(T) from R19-21 (D1 root edges).
  - Linear perturbations plus the homogeneous history.
- **Prior art (count once):** R17-11 and its verdict, R19-14, R19-17 and R19-21 with their verdicts or worker reports, R19-20, R12-2, R11-3.
- **Removed hypothesis:** site creation as the only receiver.
- **Probes.**
  - (a) Can the lattice frame (W or A) or the spacing evolution absorb an isotropic enthalpy, and at what cost (signalling, a number)?
  - (b) If none can, the size of the gravitational effect at BBN and today against the bounds.
  - (c) Prices.
- **FIXED readings.**
  - **V1-RECEIVER:** a stated V1 mechanism absorbs the enthalpy mismatch with no number and no signalling. Checked.
  - **V1-EXCLUDED:** a refereed demonstration that every V1 completion in a stated class leaves an enthalpy mismatch violating a stated bound.
  - **OPEN:** otherwise.
- **Expectation.** V1-RECEIVER under reading A: the frame's zero-inertia constraint becomes a carrier, which is (d-i)'s analogue with the spatial trace freed by X. Otherwise V1-EXCLUDED.

#### C5 referee verdicts R19-20, R19-22 and the R19-24 worker reading (recorded 06:51Z)

- **R19-20 referee: CONFIRMED WITH CORRECTIONS. Reading IRREDUCIBLE** (established by D1 and D2).
  - **What (Σ) is.** Under O_h × T, analyticity and a specified source/Hamiltonian identification, one number-free renormalization rule packages three things: the lowest-state constant, the uniform-strain response, and the linear response through two derivatives.
  - **It imposes rather than derives** the Lorentz- and diff-invariant vacuum form.
  - **What it does not entail:** the weight-1 choice, gravitational self-coupling, or a Bianchi-compatible growth or frame completion.
  - **Not established:** D3 and the claimed three-clause minimality.
  - **Confirmed in scope:** the 34 → 2 count, and the Wilson 6.6e106 ρ_Λ illustration.
  - **No robust new gravity prediction follows.**
    - The present-vacuum O(p⁴) correction is negligible.
    - The early-state shear, enthalpy, creation, anomaly and relic effects are hazards conditional on the model, the history or the bridge.
    - The top-mass condition belongs to the stipulated Λ = 0 rule and is not evidence for the grid.
- **R19-22 referee: CONFIRMED WITH CORRECTIONS. Reading OPEN.**
  - **What holds:**
    - For the literal linear Holstein–Primakoff replacement, every finite S destroys the first-class pair and leaves no nonzero joint-kernel state.
    - With fixed penalty couplings, the ground energy is ≤ −3JS/4 + O(1) per cell relative to fixed-occupation states.
    - Exact non-modular finite-spectrum vector-law models have a k⁴ TT f-sum at each fixed S. Uniformity in S needs another hypothesis.
  - **Scope of the impossibility.** Finite dimension forbids the noncompact CCR realization, not every exact finite constraint or every emergent finite-slot mechanism.
  - **No model realizes the graviton** to observational accuracy, and no universal finite-slot no-go is proved.
- **R19-24 (can the charge block be number-free?): worker reading COUNTERTERMS-NEEDED in class 𝒦′,** with an OPEN remainder and a registration collision.
  - **The registered one-loop clause D1 fails at two loops.** In the toy λφ⁴ on Z³ × ℝ, the one-loop speed row is exactly zero, yet the two-loop sunset gives δc² ≈ −0.09 to −0.38 (λ/16π²)². The Z⁴ control is zero.
  - **D1∞ (all orders)** is the on-shell renormalization condition: the R19-12 counterterms (4 per class), re-set at every order.
  - **Lemma S.** The axioms' symmetry group acts block-diagonally on (t, x), so no symmetry fixes the speed. Only time–space mixing does, via set B's Z⁴ (refereed T1, F2, O1) or set A.
  - **Lemma E (key).** A state-independent linear source subtraction equals a kinetic counterterm. So (Σ) is, at linear order, the graviton's kinetic counterterm.
    - The asymmetry is "bridge (supplied sector) vs law", not "source vs dynamics".
    - (Σ_γ) equals κ_γ.
    - Consistency demand: either exempt law-level clauses from the count, or count (Σ) as 33 conditions.
  - **Prices:** P-R19-24a (D1∞, which is P73 restated), P-R19-24b ((Σ_γ) = κ_γ).

  Referee running.
- **R19-27 (V1 enthalpy gap): worker reading V1-RECEIVER, in class 𝒱_ct.**
  - **Why the mismatch arose.** It assumed Higgs-sector counterterms fixed in physical units, which is inadmissible on V1: the vev would drift by ~1e51 per e-fold.
  - **The receiver: per-site counterterms.** These are lattice-unit counterterms on a line of constant physics. Each carries exactly the opposite pressure to the piece of the sea it cancels (Lemma E: W_k = ((4−k)/3)ρ_k). So the mismatch is cancelled to O(φ⁵ℓ) (Theorem R).
  - **The lattice frame cannot take the energy leg** (Lemma X0).
  - **Checked** on D1 root edges (residual ~5e-7 relative, scaling as m^{3.2}, CW-log) and in the NN thermal channel.
  - **No lattice force and no signalling.**
  - **Price:** P-R19-27a (per-site Higgs-sector counterterms plus the LCP; no new numbers).
  - **Suggested:** R19-21's C-box-E enthalpy claims also depend on the counterterm scheme.
  - **Archive fix (07:02Z):** `scripts/C5/R19-21/r1921_enthalpy.py` imported from the non-archived `../arch/R18-5`. It now uses `../R18-5`, and its rerun output is identical. (Reported by R19-27.)

  Referee running.

### C5 Round 19, item 28 (pre-registered 07:04Z, before launch)

**R19-28. Set B with (Σ): if time is on the grid too (Z⁴), the charge block vanishes by symmetry (R19-24, worker). Do set B's refereed walls survive once (Σ) handles the gravitating source? What is set B's total bill?**
- **Plain question.**
  - R19-24 (worker; referee running) finds that with continuous time no symmetry fixes the particle speeds, so the charge block stays as counterterms.
  - On hypercubic Z⁴ with a_t = a_s, the 90° time–space rotation zeroes every dimension-4 speed row at all orders. This is refereed prior art: T1, F2, O1.
  - Set B was set aside earlier for other walls:
    - R2-4, R2-5 and R2-1 (`TESTS:2728-2760`);
    - RK2 (`TESTS:1663`);
    - reflection positivity (RP) with box symbols, R10-2.
  - With (Σ), the vacuum-gravity source rule, now available, are those walls about the gravitating source, which (Σ) would address? Or are they about matter, records or unitarity, which it would not?
  - Is set B + (Σ) a package with zero tuned numbers, apart from the CC, which (S) handles?
- **Setting.**
  - Set B as registered earlier: Euclidean Z⁴ with a transfer matrix, records via RP, and box symbols per R10-2.
  - Together with (Σ), W1-weight and a carrier (R19-20).
  - Re-read each refereed set-B wall and classify it as source-side, matter-side, or record/unitarity-side.
- **Prior art (count once):** set B's walls and verdicts (T1, F2, O1, RK2, R2-1, R2-4, R2-5, R10-2, R5-x as applicable), R19-20 and R19-24, and the C1-C4 lanes on Z⁴.
- **Removed hypothesis:** set B judged without (Σ).
- **Probes.**
  - (a) A table of set-B walls, each classified, citing its verdict.
  - (b) For each source-side wall, whether (Σ) removes it.
  - (c) The total bill for set B + (Σ).
  - (d) Prices, including the Lattice axiom change (time on the grid) and the RP and record issues.
- **FIXED readings.**
  - **B-PACKAGE:** set B + (Σ) has every refereed set-B wall either removed by (Σ) or priced, with a stated total bill lower than C-box's. Checked against the verdicts.
  - **B-STILL-WALLED:** a set-B wall that (Σ) does not touch and no stated price passes (cite it).
  - **OPEN:** otherwise.
- **Expectation.** B-STILL-WALLED. Set B's main walls are RP and record ones (R10-2: box symbols lose RP; R2-x), which concern matter and records, not the gravitating source. (Σ) cannot touch them.
- **R19-26 (photon kernel wrap cut): worker reading PHOTON-EXACT.**
  - **Lemma P.** With R9-9's placement, a local stress's wrapped-q kernel must flip sign at q = ±π. So R1's opposite limits are required, not a defect.
  - **The real defect** was VW's site-placed off-diagonal stress used as plaquette-centred: a non-local half-shift that gave the O(1) jump.
  - **The repair:** a local 4-point re-placement F(q_i)F(q_j), with F = 1 + O(q⁴). It leaves every row unchanged and keeps W1 exact to ≤ 2e-15.
  - **Checks:**
    - the placement-corrected jump vanishes like ε;
    - the referee's script gives 3.3e-11;
    - the kernel's Fourier coefficients decay faster than any power (before the repair they decayed like 1/n).
  - **The root re-solves:** face totals ~1e-12.
  - **Correction:** R17-12's co-location claim held only along the axis.
  - **Price:** P-R19-26a (re-placement law data, zero numbers).
  - **Flag:** R19-5's U/UD exact completions should get the same placement and Fourier test.

  Referee running.

- **Referee records, 2026-10-13 ~07:08Z.** Codex gpt-5.6-sol at xhigh.
  - **R19-21: NOT CONFIRMED. Recorded reading: OPEN** (the worker's reading was HISTORY-SAFE).
    - Confirmed:
      - the NN O(λ) mechanism, within its model;
      - the sign flip at T = 563 GeV, in the Higgs mean-field channel;
      - today's matter channel, |m_g| ≈ 1.4e-9 eV. With GWTC-4.0's 1.92e-23 eV bound the ratio is 7.4e13 (not 1.1e14), which does not change the conclusion;
      - the D1 enthalpy, 2.68e106 ρ_Λ.
    - Not established:
      - (S_loc) is shown only at O(λ) in one NN scalar model;
      - gauge/Yukawa thermal masses of order g²T² are not excluded, so "Higgs-only, T⁶ residue" does not hold;
      - the cone-row thermal analogues, the all-orders UV/IR definition, and the hot-frame dynamics are uncomputed;
      - (d-i)'s C-box-E is not checked jointly with V1.
  - **R19-23: CONFIRMED WITH CORRECTIONS. PHYSICAL is met.**
    - E_g, T_2g and face2 are gauge-free TT pole shifts. "A_1 + E" is a typo for "4A_1 + B_1 + B_2 + 2E".
    - face1 enters a physical pole only through the first-order A_1 Schur complement, which is uncomputed. So R18-13 and R19-12's face1 zero and payment are CONDITIONAL; face2 stands.
    - Solid kernel: two positive-residue TT branches; the correct phase specification is m_0 = m_1 = m_4 = 0. There is no vDVZ jump at fixed q, but this is not derived for the actual vacuum.
    - **Correction to the worker's overclaim:** a degree-2 Ward-violating speed kernel need not propagate π⁰. The π⁰ spectrum and the candidate wall stay OPEN.
  - **R19-24: NOT CONFIRMED** (the worker's reading was COUNTERTERMS-NEEDED).
    - Confirmed:
      - the toy: an exact one-loop zero gets a nonzero two-loop speed row, and Z⁴ removes it. This is not a computation of the QED residual. The values at m = 0.2 are −0.3617 and −0.0908;
      - Lemma S, within G;
      - Lemma E is exactly algebraic, with residual kernel K − Z E_EH. It establishes 33 imposed conditions, not necessarily 33 selected numbers.
    - Under the campaign's law-functional precedent, D1_∞ is number-free and meets DYNAMIC-CLAUSE by construction. Under law-level counting it is OPEN.
    - D1_∞ and linear Σ are the same inverse-kernel renormalization move. Both impose Lorentz invariance; neither predicts it.
    - No class-wide counterterm no-go is proved.
