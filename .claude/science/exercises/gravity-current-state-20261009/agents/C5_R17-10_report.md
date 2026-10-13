# C5 R17-10 report: certify or break the graviton-cone / K₆ conflict (and the μ_E conflict) on one subluminal scalar edge, U vertex, E1

**Author.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. 2026-10-13, 01:10Z to 01:44Z. No repository file was edited. No downloads, no web lookups. Only installed packages (numpy 2.4.1, scipy 1.17.0, mpmath 1.3.0; no SDP/conic solver is installed, checked with `pip list`). `OMP_NUM_THREADS=2`; every run under 10 min (per-cell `alarm` guards).

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `S/` = `.../scratchpad/C5/R17-10/`. Scripts and `.out` files in `S/scripts/`.

**Read.** `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (`AX`). `P/TESTS.md`: C5 method and readings (`:2302-2320`); R14-3 (`:4830-4843`) and verdict (`:4915-4922`); R16-3 (`:5087-5105`) and verdicts (`:5359-5369`, `:5427-5432`); R16-9 (`:5373-5400`), worker (`:5550-5562`) and verdict (`:5668-5682`); R17-4 (`:5816-5845`), worker (`:5940-5953`) and verdict (`:6171-6178`); my item (`:6208-6228`). `P/agents/C5_R16-9_report.md` and `C5_R16-9_referee.md` (`vR16-9`); `C5_R17-4_report.md`, `C5_R17-4_referee.md`, `C5_R17-4_referee_verdict.md` (`vR17-4`).

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

---

## Certification method and tolerance (stated before any certification attempt)

Written to `S/METHOD.md` at 01:21Z. Honest timing: before that file I had run only the archived-runner rechecks (§3.1), the identity check of §3.2, and two exploratory (non-certified) cells of the relaxation in §3.3. No certification step preceded it.

- **Target, per condition.** On the relaxation superset, U vertex, E1, m ∈ [0.01, 0.1], continuous b, lo, hi, s_min:
  - K₆: sup of −⟨K₆/ε⁷⟩/128 subject to Ξ_Eg = Ξ_T2g = 0. The stronger form is sup Ξ_face1 subject to Ξ_Eg ≥ 0, Ξ_T2g ≥ 0.
  - μ_E: inf μ_E subject to the axis zeros.
- **Certified method.** Interval branch-and-bound with outward rounding (mpmath.iv), or a verified moment-SOS certificate with rational data. SOS is unavailable because no SDP solver is installed. As it turned out, the certificate actually produced (§3.5) is an exact rational polynomial Lagrange certificate plus one interval-enclosed constant.
- **Tolerance: zero for a certificate.** Every inequality must be exact (rational arithmetic) or enclosed by outward-rounded intervals, with the strict sign after enclosure. Local optimizers, node-placed level bins and non-enclosed quadrature count as "checked" numerics, never as certificates.
- **Gap test first, not a certificate.** Multistart SLSQP on the node-placed relaxation (700 log-t nodes, as R16-9). Its quadrature error was checked at ≤ 8e-18 (`slack.out`).

---

## 0. In plain words

1. **The problem collapses to three numbers per moment in time (proved; checked to all printed digits).** Write W = t·f² and use the tilted one-dimensional zone measure. With its first three moments x, y, z, the four U-vertex rows are single time integrals:
   - Ξ_T2g ∝ ∫ x²(2x − 1);
   - Ξ_Eg ∝ ∫ (2x − 1)(y − x²);
   - ⟨K₆/ε⁷⟩ ∝ ∫ (z − 15xy + 30x³).

   In the box (continuum) x = ½ and z − 15xy + 30x³ = 0, so all three vanish.
2. **On the "fast-only" slice the K₆ conflict is now a theorem (Theorem F, proved, with an exact certificate).** "Fast-only" means every edge state has |σ′| = 1. That is the sharp-turn limit of R16-3's zigzags. It is also where the best "ge" optima of the relaxation sit (P/M = 1.000 in the best cells). The exact-axis-zero optima do not sit there (item 3).
   - On this slice, two integrations by parts turn every row into the integral of a cubic polynomial in one function, x(t).
   - A fixed pair of multipliers makes Ξ_face1 − α Ξ_Eg − β Ξ_T2g the integral of x·P(x, m²t), with P < 0 everywhere the trajectory can go. The multipliers are α = 536/625 and β = −16/125.
   - So at every axis zero ⟨K₆/ε⁷⟩ > 0, for every m > 0, provided b ≥ 2.994 m and s_min ≥ 1.377 m. This needs no coarea, no σ ≤ k and no mass constraint.
3. **It does not yet reach the whole relaxation (checked).**
   - The same multipliers give a positive Lagrangian, up to +1.1e-4, on flat-heavy measures (per-level slope² average 0.05–0.14). There Ξ_Eg is very negative.
   - Numerically it stays negative when every level has mean slope² ≥ 0.5: max −1.2e-4 (local search).
   - The general relaxation's best exact-axis-zero points carry slow mass (aggregate P/M 0.25–0.6). So the slice theorem does not cover them.
4. **The general relaxation keeps the sign, but no certificate exists for it (checked).**
   - With R16-9's Lemma R_U extended by the sixth slope moment: the best face1 found at Ξ_Eg, Ξ_T2g ≥ 0 is −9.4e-5 (m = 0.01; −6.3e-5 with the path constraints removed). The best −⟨K₆/ε⁷⟩/128 at exact axis zeros is −1.8e-4.
   - So the relaxation gap is smaller than the margin. That was the expectation's condition (`TESTS:6227`).
   - Certification still fails for three reasons:
     - the node-placed bins are not an outward superset: the termwise enclosure slack at 50 levels is 6.6e-3 to 9.2e-3, about 70–80× the margin;
     - the problem is nonconvex: local maxima are not monotone across nested problems;
     - no SDP solver is installed.
5. **μ_E: nothing certified (checked rechecks only).** R16-9's U value +1.32177e-4 reproduces exactly. Theorem F's pointwise trick does not carry over: the shear row has an extra 1/t weight, which makes its small-t integrand strictly negative while the cone integrands vanish. Any μ_E certificate must use trajectory (path) information.

**Against the FIXED readings (`TESTS:6223-6225`); worker reading, referee required.**
- **K₆: OPEN** as a class reading on the relaxation superset of 𝒮.
  - Inside it: **CERTIFIED-CONFLICT on the stated fast-only slice** (Theorem F; exact rational certificate plus one interval constant; unrefereed).
  - That slice is not a superset of 𝒮. Laws in 𝒮 always have |σ′| < 1 near k = π, because σσ′(π) = 0 with σ(π) ≥ s_min. So the fixed clause is met only on the slice.
- **μ_E: OPEN.**
- **JOINT: not met.** No law or relaxation point with the axis zeros and K₆ ≤ 0 or μ_E ≤ 0 was found.

---

## 1. Setting, hypotheses, excluded realizations (stated before titles)

- **Laws.**
  - R14-3/R16-3's separable class 𝒮: ε² = m² + Σᵢ σ(kᵢ)², σ ∈ C², σ(0) = 0, σσ′(π) = 0, |σ′| ≤ 1.
  - Box σ = k on [0, b]. Edge σ ≥ s_min > 0 (no doubler) (`C5_R16-9_report.md:38`).
  - f = σσ′, u = σ′² ∈ [0, 1], f² = u·h² at level h = σ.
- **Rows.**
  - R17-4's U+E1 five-moment forms (`C5_R17-4_report.md:133-137`), refereed exactly (`C5_R17-4_referee.md:9-16`).
  - R9-9's prescription, with standard W1 assumed, not built.
  - Supplied scalar zero-point vacuum; in the empty Fock vacuum all rows vanish.
  - Bare-cone shift only.
- **Excluded (item, `TESTS:6214`):**
  - the M vertex (non-local, Lemma M);
  - fermion loops;
  - pairing; deformed W2; non-separable laws;
  - the E2 extension (rows differ off-axis, `vR17-4` item 4).
- **Relaxation (§3.3).** R16-9's Lemma R_U (`C5_R16-9_report.md:115-121`, inequalities confirmed `vR16-9:7`), extended by R = ∫s⁶dk per level. K₆ needs ⟨f⁶⟩. Constraints:
  - the truncated-Hausdorff conditions for (M, P, Q, R) as moments of u ∈ [0, 1];
  - coarea + Cauchy–Schwarz (M·P ≥ |A|²);
  - the σ ≤ k tail;
  - total edge mass π − b.
- **Fast-only slice 𝓕 (§3.5).** The level measure is the box plus any positive edge measure on [s_min, π], with u ≡ 1 (|σ′| = 1 a.e.).
  - **This is the sharp-turn limit of zigzag skeletons, not a subset of 𝒮.**
- **Masses.** m ∈ [0.01, 0.1]. Theorem F holds for every m > 0 under its b and s_min conditions.
- **Head rules.**
  - v_max: no new law is proposed. Laws used are R16-3's, with v_max in `C5_R17-4_report.md:216-219`.
  - Ward: standard W1, assumed.
  - No frame-tied kernel, no readout bridge, no initial-state claim. Forks are not offered as exhaustive.

## 2. Prior art (each counted once)

- **R17-4** (`vR17-4`, COUNTED-ROWS for U+E1):
  - face2 ≡ T2g;
  - face1 = (3Eg + T2g)/4 − ⟨K₆/ε⁷⟩/128 (`C5_R17-4_report.md:20,135`);
  - searches max face1 −1.12e-4 (inner, not certified) (`:178-181`);
  - (f) OPEN (`:240-249`).
- **R16-9** (`vR16-9`, OPEN):
  - Lemma R_U;
  - the fast-state identity, confirmed (`vR16-9:11`), with R16-9's a = 2x here;
  - U shear margin +1.3e-4 (`C5_R16-9_report.md:188`);
  - the referee's three gaps: grid not a superset, local optima, sampled parameters (`vR16-9:5-9`). §3.4 measures the first two.
- **R16-3** (Z1, IBP identity; U zeros) and **R14-3** (μ_E = −(5/72)⟨K₄/ε³⟩; analyticity in m²).
- **Grep.** I searched the packet for "Lagrange certificate", "sixth moment", "fast-only", "x(5x". The only hit is R16-9's fast-state identity, which Theorem F extends to face1 and Eg (counted once).

---

## 3. Results

### 3.1 Rechecks of archived runners (checked)

- **R17-4 `evalzeros.py`, copied unmodified.** Output identical to the archive except runtime (`evalzeros_recheck.out`; `diff` empty). U zeros give face1 = −8.93992e-4 / −8.95970e-4 / −8.96115e-4 at m = 0.1 / 0.03 / 0.01.
- **R16-9 `relaxed_UV.py U 0.01 0.15 8 1 0.3 0.5`, unmodified.** MIN μ_E = **+1.32177e-04** at b = 0.3, hi = 0.8. This is identical to `P/scripts/C5/R16-9/relaxed_UV_U_m0.01_batch.out:3` (`recheck_relaxed_UV_U_m0.01_b0.3.out`).
- **R17-4 `fastU.py`** is used as the reference evaluator in §3.2.

### 3.2 (a) The polynomial formulation (proved; checked)

**Compact form.** For any separable law (any slopes), Laplace factorization of R17-4's five moments gives the following. Let the tilted 1D measure be e^{−tg}dk/E0. Set W = t f², x = E[W], y = E[W²], z = E[W³], dλ = t^{−1/2}e^{−tm²}E0(t)³dt and c7 = 1/Γ(7/2). Then:

- Ξ_T2g = (5c7/16) ∫dλ x²(2x − 1)
- Ξ_Eg = (5c7/32) ∫dλ (2x − 1)(y − x²)
- ⟨K₆/ε⁷⟩ = c7 ∫dλ (z − 15xy + 30x³),  Ξ_face1 = (c7/128) ∫dλ (−z + 45xy − 40x³ − 15y + 5x²)
- μ_E = (1/(12Γ(3/2))) ∫ t^{−3/2}e^{−tm²}E0³ (3x² − y) dt

**Proof.** a6 = c7∫t^{5/2}e^{−tm²}F6E0², …, b22 = c5∫t^{3/2}e^{−tm²}F2²E0 (R17-4's Laplace forms), and c5 = (5/2)c7. Substitute F_{2k} = E0·E[W^k]/t^k. ∎

**Consequences (proved).**
- At the axis zeros, Ξ_T2g = 0 ⟺ b22 = 5a222 and Ξ_Eg = 0 ⟺ b4 = 5a42. So K = a6 − 3b4 + 6b22 there.
- Box control: a Gaussian W gives x = ½, y = ¾, z = 15/8, and all integrands vanish.

**Check (`xyz_check.out`).** Agreement with `fastU.rowsU` to all 7 printed digits for Eg, T2g, face1, the K₆ row and μ_E. Tested on G(1.0), C2, C and R16-3's U zero, at m = 0.1 and 0.01.

**(a) proper.**
- The K₆ problem is a polynomial optimization over the relaxation: maximize ∫dλ(−z + …) subject to ∫dλ x²(2x−1) = 0 and ∫dλ(2x−1)(y−x²) = 0.
- (x, y, z)(t) are ratios of linear functionals of the per-level (M, P, Q, R). The objective is cubic in those variables after clearing E0.
- The μ_E problem is the same with the weight dλ/t and integrand 3x² − y.
- The new ingredient over Lemma R_U is the sixth slope moment R. Its necessary conditions are [[P,Q],[Q,R]] ⪰ 0 and [[M−P, P−Q],[P−Q, Q−R]] ⪰ 0 (truncated Hausdorff on u ∈ [0,1]).
- Adding R does not change the μ_E problem (reading: R is free once (M, P, Q) is degree-2 Hausdorff-feasible; recalled).

### 3.3 (b, c) The general relaxation: gap test (checked, not certified; `relaxK6.py`)

**Method.** Two-phase multistart SLSQP with exact gradients (gradient check ≤ 5e-9 relative). 50 node-placed levels on [0.15, π], 6 starts per cell. Cells: b ∈ {0.2, …, 1.4}, hi = b + {0, …, 1.5}. Cells with b < s_min are invalid and are discarded.

| problem (U, E1) | m | best value found | cell | structure |
|---|---|---|---|---|
| max face1, Ξ_Eg, Ξ_T2g ≥ 0, full relaxation | 0.01 | **−9.36e-5** | b = 0.3, hi = 0.8 | all fast (u = 1) |
| same | 0.1 | −1.35e-4 | b = 0.2, hi = 0.95 | all fast |
| same, path constraints removed (no coarea, no σ ≤ k) | 0.01 | **−6.28e-5** | b = 0.3, hi = 0.8 (`polish_nopath.out`) | all fast, level gap |
| max −⟨K₆/ε⁷⟩/128 at exact Ξ_Eg = Ξ_T2g = 0 | 0.01 | **−1.83e-4** | b = 0.2, hi = 0.95 | aggregate P/M 0.38, slow climbs |
| R17-4 inner (slope-resolved) search, comparator | 0.01 | −1.12e-4 (80 lev.) / −1.33e-4 (40 lev., b = 0.3, hi = 0.8) | `C5_R17-4_report.md:180` | |

Files: `relaxK6_{ge,eq}_m0.01_s0.15.out`, `relaxK6_ge_m0.1_s0.15.out`, `nopath_ge_m0.01.out`, `polish_*.out`.

**Readings from the table.**
- The relaxation's best points look like realizable laws (reading, from `structure.out`). They combine fast zigzag passes (u = 1, up to 30 passes per level bin) with gentle slow climbs (M·P = |A|², uniform slope ≈ 0.13, which a real climb can realize). So the outer–inner gap is ≈ 2–4e-5 with the path constraints and ≈ 5–7e-5 without them, while the margin is ≈ 1e-4.
- **The margin beats the relaxation gap numerically.** This was the expectation's condition, but it is local-search evidence only.
- The path constraints matter only weakly here:
  - removing them raises the best ge value from −9.4e-5 to −6.3e-5, and the sign stays;
  - warm-started NOCOAREA alone stays at −9.36e-5 (`ablate_nocoarea_polish_b0.3.out`);
  - NOSK alone gives −1.18e-4 (`ablate_nosk_b0.3.out`).

### 3.4 Why the general relaxation is not certified (checked)

1. **The node-placed bins are not an outward superset**, as R16-9's referee noted (`vR16-9:5,7`). `slack.py` bounds each term over every placement of each bin's mass inside its bin, using the per-bin max or min of each kernel by coefficient sign (sampled, so this is an estimate). Results:
   - b = 0.3/hi = 0.8: face1 upper bound +6.50e-3 against node value −9.36e-5, slack 6.6e-3;
   - b = 0.6/hi = 0.65: slack 9.2e-3.

   That is 70–80× the margin (`slack.out`). The cause is that face1 is a difference of terms ~1e-2. The slack is O(Δh), so termwise enclosure needs ≳ 4000 levels. A first-order (in-bin moment) scheme would need ≳ 450, with 8 variables per bin. Neither is followed by a global certificate for the resulting nonconvex program.
2. **The problem is nonconvex, and local maxima are not reliable.**
   - Nested problems violate the required order: ge ⊇ eq must give max_ge ≥ max_eq. Yet at b = 0.2, hi = 0.45 the first ge run gave −3.96e-4 against eq's −2.00e-4. Warm-starting ge from the eq point gives −2.00e-4 (`polish` test).
   - Polishing from stored optima also moved b = 0.3, hi = 0.8 to a different local optimum (−1.26e-4; `polish_full.out`).
   - So every tabulated value is a lower bound on the relaxation's sup, nothing more.
3. **Solver fragility.** SLSQP failed to converge in some cells:
   - "no feasible point found" although phase 1 was feasible; later runs re-check and fall back to the phase-1 point;
   - in the whole `mu` mode (`mu_crosscheck_b0.3_m0.01.out`; nonlinear-constraint violations up to 3.6e-2, `DBG` output);
   - in the 100-level refinement (`refine_L100_b0.3.out`).

   These failures are reported, not used.
4. **No SDP solver is installed,** so a moment-SOS relaxation cannot be run. Interval branch-and-bound over ~200 variables is not feasible in this budget.

### 3.5 Theorem F: the K₆ conflict on the fast-only slice (proved; exact certificate)

**Setting.** 𝓕 is the box σ = k on [0, b] plus any positive edge level measure η on [s_min, π], with u = 1 everywhere. Then F2 = −Φ′, F4 = Φ″, F6 = −Φ‴ with Φ = E0. Define x = −tΦ′/Φ (= a/2 in R16-9's notation), V = y − x² = t²(ln Φ)″ = x − t x′ ≥ 0, and C3 = −t³(ln Φ)‴ = 2V − tV′. Set s := m²t.

**Step 1 — one-function forms (proved; checked).** Start from §3.2 with z = x³ + 3xV + C3:
- face1 integrand: −z + 45xy − 40x³ − 15y + 5x² = 4x³ − 10x² + 42xV − 15V − C3.

Integrate by parts in t with w = t^{1/2}e^{−tm²}Φ³. Then w′ = (dλ/dt)(½ − s − 3x), and boundary terms vanish because t^{1/2}x → 0 at 0 and e^{−tm²} → 0 at ∞, for m > 0.
- ∫dλ tV′ = ∫dλ V(3x − ½ + s).
- ∫dλ (45x − 35/2 + s)(−t x′) = ∫dλ[(45x²/2 − 35x/2)(½ − s − 3x) + s x(3/2 − s − 3x)].

This gives, exactly:

- **Ξ_face1 = (c7/128) ∫dλ [−63.5x³ + 98.75x² − 26.25x + s(20x − 25.5x²) − s²x]**
- **Ξ_Eg = (5c7/32) ∫dλ [−3x³ + 5.5x² − 1.5x − s(x² − x)]** (one IBP of (2x − 1)(−tx′))
- **Ξ_T2g = (5c7/16) ∫dλ (2x³ − x²)** (no IBP)

The μ_E analogue is μ_E = (1/(12Γ(3/2)))∫(dλ/t) x(5x − ½ + s). That is R16-9's confirmed fast-state identity (`vR16-9:11`), a consistency check. It is checked here to ≤ 7e-11 on 4 random fast measures (`mufast_check.out`). That form has a t^{−1/2} integrable singularity at t → 0, so its grid must start at e^{−44}; cut at e^{−16}, the dropped tail is ~1e-4. The face1 and Eg forms are regular there (integrand ~ t^{1/2}).

Checked against the five-moment forms (`fastcert.out`, `fastform_check.out`): differences ≤ 5.5e-12 on 9 all-fast measures. These were 3 relaxation optima and 6 random measures, with m ∈ {0.01, 0.03, 0.1} and b ∈ [0.2, 1.2].

**Step 2 — the certificate (proved; exact rationals, `fastcert_exact.out`).** Take A = 67/500, B = −1/25, so α = 32A/5 = 536/625 and β = 16B/5 = −16/125. Then:

  Ξ_face1 − α Ξ_Eg − β Ξ_T2g = c7 ∫dλ x·P(x, s),
  P(x, s) = c2x² + c1x + c0 + s(k1 − k2x) − s²/128,

with c2 = −451/32000, c1 = −353/64000, c0 = −261/64000, k1 = 89/4000 and k2 = 2087/32000.
- **Region 1, s ≤ s* = 9/50:** P ≤ c0 + s*k1 = −117/1600000 < 0. This uses c1, c2 < 0 and the fact that the s·x and s² terms are ≤ 0.
- **Region 2, x ≥ x* = k1/k2 = 712/2087 ≈ 0.34116:** the s-linear term is ≤ 0, so P ≤ q(x) ≤ c0 < 0.

**Step 3 — the trajectory stays in Region 1 ∪ Region 2 (proved; one interval constant).**
- x(t) is the tilted mean of W = th² over box states and edge states. So x(t) ≥ min(x_box(t), t s_min²), because every edge state has W ≥ t s_min².
- x_box(t) = (1 − R(z))/2 with z = b√t and R(z) = 2ze^{−z²}/(√π erf z).
- For z ≥ z0 ≥ 1/√2, R(z) ≤ R(z0), because 2ze^{−z²} decreases and erf increases.
- With z0 = 1.27, R(z0) ≤ 0.3079868 is outward-enclosed: a rigorous right-endpoint Riemann lower bound of ∫₀^{z0}e^{−v²}, N = 4000, in mpmath.iv. So x_box ≥ 0.346007 > x*.
- Hence for t ≥ s*/m², x(t) ≥ x*, whenever **b ≥ 1.27 m/√(9/50) = 2.9935 m and s_min ≥ m√(x*/s*) = 1.3768 m**.
- For t < s*/m² the trajectory is in Region 1 whatever x is.

**Conclusion (Theorem F).** For every m > 0 and every law in 𝓕 with b ≥ 2.9935m and s_min ≥ 1.3768m:

  Ξ_face1 < (536/625) Ξ_Eg − (16/125) Ξ_T2g  (strict, since x(t) > 0 for t > 0).

So **Ξ_Eg = Ξ_T2g = 0 ⇒ Ξ_face1 < 0 ⇒ ⟨K₆/ε⁷⟩ > 0**. ∎
- No coarea, no σ ≤ k, no total-mass constraint and no hi bound is used.
- It covers m ∈ [0.01, 0.1] whenever b ≥ 0.3 at m = 0.1 (b ≥ 0.03 at m = 0.01) and s_min ≥ 0.138 at m = 0.1 (0.0138 at m = 0.01). R16-9's s_min = 0.15 qualifies.

**Adversarial consistency check (checked; `lag_fastonly_adversarial.out`).** I maximized Λ by local search over the path-free fast-only relaxation (UMIN = 1, no coarea, no σ ≤ k), with b ∈ {0.3, 0.6, 1.0}, m ∈ {0.01, 0.1} and hi up to 3.08.
- Every converged cell gave Λ < 0. The largest was −6.1e-4.
- Three cells did not converge (degenerate equality-like constraints at UMIN = 1). They are reported as "none".

**Scope (strong-word check).**
- 𝓕 ∩ 𝒮 = ∅. A C² law with σ(π) ≥ s_min needs σ′(π) = 0.
- So Theorem F proves the conflict for the sharp-turn limits of P-Z zigzag skeletons and for the u ≡ 1 face of the relaxation, not for any law in 𝒮.
- It does **not** prove anything with Ξ_Eg, Ξ_T2g ≥ 0 (α > 0 permits face1 → 0 at large Ξ_Eg). Consistently, the ge optima of §3.3 have Ξ_Eg ≈ +1.2e-3 and face1 ≈ −9e-5, which obeys the bound.

**Reading.** On the fast slice the cone needs x > ½ somewhere (fast low-lying pair states, R16-9's a > 1). Those same states make P's cubic part dominate, so K₆ > 0 is forced pointwise once the cone constraints are added with these weights.

### 3.6 Does the certificate reach slow slopes? (checked; `lag_*.out`)

Maximize the fixed Lagrangian Λ = face1 − (536/625)Eg + (16/125)T2g over the **general** relaxation, with no cone constraint (local search):
- **Full constraints:** max Λ = **+1.12e-4** at m = 0.01 and +1.02e-4 at m = 0.1 (b = 0.2, hi = 0.45).
  - These are flat-heavy edges (aggregate u ≈ 0.05–0.14) with Ξ_Eg ≈ −4.5e-3. Far from the axis zeros, the −αΞ_Eg term wins.
  - Some flat-heavy points have K₆ < 0 (positive K₆ row), the terrace mechanism of R17-4.
- **With per-level mean u ≥ u0 (`lag_nearfast.out`):**
  - u0 = 0.9: max Λ = −3.6e-4;
  - u0 = 0.7: −2.5e-4;
  - u0 = 0.5: −1.2e-4.

  So numerically (not proved) Theorem F's multipliers also work when every level's mean slope² is ≥ ½. That covers zigzag laws with finite turn widths like R16-3's (suggested).
- **The gap that remains.** The general relaxation's best exact-axis-zero points (§3.3) combine fast levels with slow climbs (per-level u down to ~0.02). This is the region neither Theorem F nor the near-fast evidence covers. A general certificate needs either different (non-constant, or more) multipliers or the path constraints. With constant multipliers, the window that my simple sufficient sign pattern (c1, c2 ≤ 0, c0 < 0) allows on the fast slice is narrow (A ∈ [0.1309, 0.1367]). Other windows, using the discriminant route or sharper trajectory bounds, were not explored. The flat-heavy points push A the other way (reading). Side observation (checked): μ_E itself can be negative on fast-only measures without cone constraints (−5.33e-3, `mufast_check.out`), so any μ_E conflict must come from the cone constraints.

### 3.7 μ_E (checked rechecks; reading)

- R16-9's U relaxation minimum +1.32177e-4 (m = 0.01, b = 0.3, hi = 0.8) reproduces exactly (§3.1). My independent `mu` mode failed to converge and is not used (§3.4).
- **Why Theorem F's method does not transfer (proved, elementary).** On 𝓕, μ_E = C∫(dλ/t) x(5x − ½ + s). As t → 0, x/t → ⟨g⟩₀ > 0, so the integrand tends to −C⟨g⟩₀/2 < 0 per dλ. Meanwhile the cone integrands vanish like x. So no constant-multiplier pointwise certificate gives μ_E > 0 at the axis zeros, even on 𝓕.
- A μ_E certificate must use trajectory information: how much small-t (UV) weight can coexist with x > ½ at intermediate t. That is the role R16-9 found for the path constraints (`C5_R16-9_report.md:162-167`).
- **Reading: OPEN**, as expected (`TESTS:6228`).

### 3.8 (d) Prices and the bill

- **Bill: unchanged as conditional bookkeeping.** 8 + CC per class / 12 + CC per species for U+E1 (`vR17-4` item 6).
- What changes is the K₆ row's status:
  - on the sharp-turn (fast) slice it is **proved** not shape-tunable together with the axis zeros. There it needs a non-shape knob: a q²-dependent TT seagull (Ward-defect counterterm) or the vertex-extension datum (`C5_R17-4_report.md:229`);
  - on 𝒮 itself it stays OPEN.
- **P-K6′ (new, sharpens P-K6).** The P-Z route cannot pay for the K₆ row in its sharp-turn limit. A shape solution, if one exists, must rest on finite slow-slope structure: turns, terraces or slow climbs that carry a finite fraction of the level occupation (per §3.6, below mean slope² ½ on some levels). Axiom cost: none; downstream dynamics (`AX:114-130`). Vertex and vacuum remain source/action gates (`AX:187`).
- **Inherited:** P-K6, P-TTV₂, P-LocM, P-Tad (R17-4); P-R16-9a (shear knob, still uncertified); P-Z; assumed W1; supplied vacuum.
- **No axiom text changes.**

---

## 4. Against the FIXED readings (`TESTS:6223-6225`)

**Worker reading; referee required.**
- **K₆ row: OPEN on the relaxation superset of 𝒮.**
  - Contained in it: **CERTIFIED-CONFLICT on the fast-only slice 𝓕 (Theorem F)**. The certificate is exact rational plus one outward-enclosed constant, valid for all m > 0 with b ≥ 2.9935m and s_min ≥ 1.3768m.
  - The fixed clause needs the superset of 𝒮, and 𝓕 ∩ 𝒮 = ∅. So the clause is met on a stated subclass only, not class-wide.
  - Numerically the general relaxation keeps the sign: best −9.4e-5 (ge), −1.8e-4 (exact zeros), −6.3e-5 without path constraints. These are local searches, not certified.
- **μ_E: OPEN.** No certificate. Theorem F's pointwise method provably cannot give one (§3.7).
- **JOINT: not met** for either condition.
- **Expectation check (`TESTS:6226-6228`).**
  - "CERTIFIED-CONFLICT for K₆ at m = 0.01 if the margins beat the relaxation gap": the margin does beat the gap numerically. The certificate came for every m, but only on the fast slice. The general relaxation failed on enclosure and nonconvexity, not on the gap.
  - "OPEN for μ_E": met.

## 5. Strong-word check

- **"Proved"** is used for:
  - the compact (x, y, z) form;
  - the fast-slice one-function forms (IBP, with boundary terms shown to vanish);
  - the rational certificate inequalities;
  - x ≥ min(x_box, t s_min²);
  - the R(z) monotone bound;
  - Theorem F;
  - the μ_E non-transfer remark.

  The IBP algebra is additionally checked to ≤ 5.5e-12. The only non-rational constant (R(1.27)) is outward-enclosed.
- **"Every / for all"** appears only in Theorem F (all laws in 𝓕 under its b, s_min conditions, all m > 0).
- **"Cannot"** appears only for "Theorem F's pointwise method cannot certify μ_E".
- **"Best found"** values are local-search lower bounds of a sup (§3.4 item 2).
- **Not claimed:**
  - any certificate on 𝒮 or on the general relaxation;
  - anything with Ξ_Eg, Ξ_T2g ≥ 0 (as opposed to = 0);
  - M or E2 vertices; Dirac/photon/gluon loops; non-separable laws; dressed poles; W2.

## 6. For the referee

1. **The compact form (§3.2):** c5 = (5/2)c7 and the W-moment substitution. Agreement to all digits with `fastU` (`xyz_check.out`).
2. **The fast-slice IBPs (§3.5 Step 1):** w′ = (dλ/dt)(½ − s − 3x), and the boundary terms at t → 0 (t^{1/2}x, t^{1/2}V → 0) and t → ∞ (m > 0). The checks are in `fastcert.out`.
3. **The certificate arithmetic (`fastcert_exact.py`):** exact Fractions. The Region-1 margin −117/1600000 is thin but exact.
4. **Step 3:** that the tilted mean over box ∪ edge is a convex combination with edge W ≥ t s_min², and the R(z) bound for z ≥ 1/√2 with the Riemann-sum enclosure.
5. **Scope:** 𝓕 ∩ 𝒮 = ∅. Is "sharp-turn limit" the right description? And is a continuity extension to near-fast laws in 𝒮 provable? §3.6 suggests a margin, but no uniform bound is given.
6. **Whether a general-u certificate is plausible** given §3.6's positive Lagrangian on flat-heavy measures. Non-constant or additional multipliers, or the use of path constraints, seem necessary.

## 7. Files (`S/scripts/`)

- **Copied unmodified:** from `P/scripts/C5/R17-4/`: `zz.py`, `laws.py`, `floor_scan.py`, `offaxis.py`, `fastU.py`, `evalzeros.py`, `relaxTT.py`, `simul2.py`; from `R16-9/`: `relaxed_UV.py`.
- **Rechecks:** `evalzeros_recheck.out`; `recheck_relaxed_UV_U_m0.01_b0.3.out`.
- **(a):** `xyz_check.{py,out}`.
- **Relaxation:**
  - `relaxK6.py` (modes ge/eq/free/mu/lag; env NOCOAREA, NOSK, RLEV, UMIN, TAG), `run_batch.sh`, `run_nopath.sh`, `run_lag.sh`;
  - outputs `relaxK6_{ge,eq}_m0.01_s0.15.out`, `relaxK6_ge_m0.1_s0.15.out`, `nopath_ge_m0.01.out`, `ablate_*.out`, `refine_L100_b0.3.out` (failed to converge), `mu_crosscheck_b0.3_m0.01.out` (failed);
  - `polish.py`, `run_polish*.sh` → `polish_full.out`, `polish_nopath.out` (the two runs could overwrite the same `polish_*.npy`; the `.npy` files are not used for any result);
  - stored optima `relaxK6_*.npy`.
- **Enclosure slack:** `slack.{py,out}`. Optimum structure: `structure.{py,out}`.
- **Theorem F adversarial check:** `lag_fastonly_adversarial.out`.
- **Theorem F:** `fastform_check.{py,out}`, `fastcert.{py,out}`, `fastcert_exact.{py,out}`; shear fast form `mufast_check.{py,out}`.
- **§3.6:** `lag_full_m0.01.out`, `lag_full_m0.1.out`, `lag_nopath_m0.01.out` (partial; stopped), `lag_nearfast.out`.
- `../METHOD.md` (method statement, 01:21Z).
