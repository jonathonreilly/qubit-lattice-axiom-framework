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
