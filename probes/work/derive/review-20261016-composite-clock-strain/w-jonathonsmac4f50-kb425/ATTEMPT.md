# Attempt: composite and clock coefficient-transfer (J:derive:review-20261016-composite-clock-strain:a1)

Worker: Claude Sonnet 5.5, same model family as the C5 workers and the E1/F6 reports. Same-family and unrefereed. Nothing here is adopted, accepted or audit-passed.

## Plain words

The Higgs mass-squared in the root's law moves with a uniform shear at Planck strength (F6). Against clocks that gives a formal "exceedance" of 2.6e18. A composite Higgs would replace the Planck cutoff by a lower scale. E1 claimed a margin of 5.6e11 for that by simply swapping the cutoff; the referee said a log-response version gives about 5.9e7.

What this attempt shows:
1. Both margins are the same chain: (strain coefficient s of a composite-scale mass-squared) times (an amplification A). The two numbers differ only in which coefficient was borrowed (F6's one-loop edge integral versus a 2D toy's log). Neither is derived for a Higgs. The 5.6e11 is exactly F6's own "(l_P/a)^2" rule with 1/a replaced by the cutoff, so it adds no independent evidence.
2. The clock bound becomes one inequality, s*A <= 6.7e12 (5.0e11 with the loosest slope estimator). That inequality is the real open number.
3. The linearized clock rate for the elementary Higgs is outside its regime (response about 1200). The exact tree-level vacuum map says the observed electroweak vacuum exists only about 4e-4 of the time in the assumed background, and wherever it exists the true rate is at least the linear one. The composite candidates are deep inside the linear regime (response 1e-27 to 1e-23).
4. The 2D toy is reconstructed in closed form. Its log enhancement comes only from the determinant of the stretch and flips away (to -1/4) for a determinant-one response law.

No composite or Standard-Model coefficient is derived. Route stops at step 11.

## Reads and provenance

Read in full: `docs/MINIMAL_AXIOMS_2026-06-29.md` and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (current main checkout `main_wt` at a77a3449c9). Source branch `claude/strain-hot-matter-twins-20261013` at the required commit 6afb06951a13ca861b50f47a8faf5d5c06594109; all 11 source objects fetched with `git show` and sha256 verified (RECOVERY_STATUS.json, `check.py` S0). Read in full: C5_E1_report, C5_E1_referee_verdict, C5_F6_report, C5_F6_referee_verdict, panel_F SYNTHESIS and DOSSIER. The five panel statements were hash-verified but not read line by line; this attempt does not rely on them. No landed current-main correction notes for E1/F6 exist (grep of `.claude` and `docs` on main for SCALAR-HAZARD, MECHANISM-SPLIT, coefficient-transfer found none). No open PR found with `gh pr list --search "strain composite clock"`. The related task `J:derive:review-20261014-flavour-strain-scope:a1` concerns flavour residual symmetries (different source branch) and shares only the word "strain"; no overlap used.

The referee's own derivation of 5.9e7 (`ref_E1/E1_referee_verdict.md:29`, another session's scratch) is not in the frozen source set and was not read. Step 6 is therefore a reconstruction.

## Steps

**1. ASSUMED, what the axioms do and do not supply.** The axioms fix Z^3 sites with nearest-neighbour adjacency (`MINIMAL_AXIOMS_2026-06-29.md:35-41`), a per-site distribution determined by neighbour conditions, and records (`:55-83`). Further structure needs a derivation or registered primitive (`:85-90`), and Admissibility supplies no dynamics, weights or Hamiltonian (`:114-123`). Approved primitives: `scale_reference_primitive` (a^-1 = M_Pl, a units conversion with no dimensionless content, `PRIMITIVE_REGISTRY_CHECK.md:31-56`), `kinetic_isotropy_primitive`, `realized_state_primitive`. Consequently none of the following is axiom content: the strain-to-coupling response law, an E_g Higgs/gauge/Yukawa sector, a strong sector, the Standard Model coupling values, a stochastic gravitational-wave background, the clock bound. All are premises of E1/F6 and stay unadopted here. The scale a = l_P enters only through the registered conversion; a/l_P = 1 is not derived (`:189-190`).

**2. CHECKED, quoted inputs reproduce.** Assembling c_H from F6's three Hessians and the Planck-scale couplings gives 3.681e-3. kappa_H = c_H M_P^2/(2 m_H^2) = 1.753e31 (F6: 1.75e31). The background mean <Q_E> = 7.0e-29 is recomputed from h_c = A (f/yr^-1)^(-2/3), A = 2.4e-15, f_min = 1/16 yr, 1/5 of the power per traceless component. With the referee's conservative slope 7.67e-30 /yr, the bound 3.6e-17 /yr and |d ln(m_p/m_e)/d ln v| = 0.7, the formal exceedance is 2.614e18 (referee: 2.614e18). The slope band gives kappa_clock = 6.7e12 (conservative) to 5.0e11. The numbers 0.7, 3.6e-17, the spectrum, A and the coupling set are quoted ASSUMED inputs, not verified here. (`check.py` S1.)

**3. PROVED (tree level), the exact vev map.** For V = -mu^2|H|^2 + lambda|H|^4 + d|H|^2, with |H|^2 = v^2/2, the broken stationary point is v^2 = (mu^2 - d)/lambda with positive curvature iff d < mu^2. With m_H^2 = 2 mu^2 and x = d/m_H^2: v^2/v0^2 = 1 - 2x exactly. F6's linear formula delta v/v = -x is only its first-order expansion. The Taylor parameter of Sigma_H(strain) is Q_E ~ 1e-28, not x, so the quadratic c_H truncation is not what fails when x ~ 1e3 (premise: higher strain coefficients are not parametrically larger than c_H). (`check.py` S3, sympy.)

**4. PROVED + CHECKED, vacuum edge and rate dichotomy (c_H > 0).** The electroweak vacuum exists iff Q_E < Q_c = 1/(2 kappa_H) = 2.85e-32. Where it exists, d ln v/dt = -kappa Qdot/(1 - 2x), so the exact instantaneous rate exceeds the linear one by 1/(1-2x) > 1 (linear is a lower bound there; instantaneous, not window-averaged). So at every instant either no broken vacuum exists or the rate is at least the linear estimate. Under the ASSUMED stationary, ergodic, isotropic Gaussian background, Q_E = (c1^2 + c2^2)/2 with c_i ~ N(0, sigma^2) is exponential with mean sigma^2 = 7.0e-29, so the fraction of time with a vacuum is 1 - exp(-Q_c/sigma^2) = 4.1e-4. Monte Carlo (2.4e7 draws, independent sampler) gives 4.0e-4 (within statistical error) and the right quantiles. <Q_E>/Q_c = 2443. For c_H < 0 (some dressed branches) there is no vacuum loss but v grows as sqrt(1 + 2|x|), about 49 times at x = 1.2e3. (`check.py` S3.)

**5. CHECKED, regime of the linear clock formula.** Requiring the linear rate to be within 10 percent (x <= 0.05 at <Q_E>) bounds kappa <= 7.2e26, so a formal exceedance is meaningful only up to about 1.1e14. F6's 2.6e18 is 24000 times beyond that. This confirms the task's remark and quantifies it. It does not weaken the failure: it says the elementary Higgs does not have a clock drift to compare, it has no observed vacuum (subject to the same premises). Composite candidates (step 6) have x = 8e-28 and 8e-24, deep in the linear regime, so the linear margin is a legitimate readout there. (`check.py` S3.)

**6. CHECKED (reconstruction), the 5.6e11 and 5.9e7 are one chain.** Write kappa_eff = |d ln v/dQ_E| = s*A with A = Lambda^2/m_H^2 = 6.4e3 (Lambda = 10 TeV) and margin = kappa_clock/kappa_eff.
- Ansatz (E1 3(e)): s = c_H/2 = 1.84e-3 gives margin 5.7e11 (E1: 5.6e11, rounding of the 1.4e-21 requirement).
- Toy log with the same A: s_toy = (1/2) ln(M_P/Lambda) + 0.3664 = 17.7 gives margin 5.92e7. This matches the referee's 5.9e7 to 0.3 percent, which is why I read the referee as using a log-response times Lambda^2/m_H^2. This is an inference, not a copied derivation.
- Toy log with A = 1 (pure multiplicative, v proportional to Lambda): margin 3.8e11.
- The two quoted margins differ by 2 s_toy/c_H = 9.6e3. Nothing about the Higgs fixes either s or A. (`check.py` S2.)

**7. PROVED, the ansatz is F6's scaling.** For margin_ans = kappa_clock/(c_H Lambda^2/(2 m_H^2)) and E = (c_H M_P^2/(2 m_H^2))/kappa_clock, symbolically margin_ans * E = (M_P/Lambda)^2. So 5.6e11 = (M_P/Lambda)^2/E: it restates F6's statement that the rate scales as (l_P/a)^2 with 1/a -> Lambda. It contains no calculation of a composite sector. (`check.py` S2, sympy and numeric.)

**8. CHECKED, the O(N) toy reconstructed in closed form.** The N = infinity lattice gap equation with couplings (J_x, J_y), 1/g^2 = int d^2q/(2 pi)^2 [m^2 + J_x(2-2cos q_x) + J_y(2-2cos q_y)]^-1, reproduces E1's table (1.50, 2.67, 3.82, 4.97, 6.12 for xi0 = 10..1e5; mpmath 1D reduction, cross-checked against an independent numpy 2D grid to 1e-10). High-precision numerics (max error 1.7e-12 over five (J_x, J_y) pairs, 30 digits, small m) give the asymptote I = ln(64 J_x J_y/((J_x+J_y) m^2))/(4 pi sqrt(J_x J_y)). It is CHECKED, not proved; I have no proof. Isotropic limit is the standard (1/4 pi) ln(32/m^2). With L = ln xi0 and the linear law (1+t, 1-t): d ln m/t^2 -> L/2 + (1/4) ln 32 - 1/2 = L/2 + 0.3664, so E1's "0.35" is 0.3664 at large xi0. The sympy series of the closed form gives this coefficient exactly. (`check.py` S5.)

**9. PROVED (given step 8's closed form), response-law dependence.** The L-dependent term comes only from sqrt(J_x J_y) = 1 - t^2/2. For a determinant-one law (e^t, e^-t) the same closed form gives exactly -1/4 at every L, with no log (checked numerically, -0.25000, and symbolically). So the toy's log enhancement and its sign are a property of how the stretch is mapped onto couplings, which the axioms do not supply (step 1). The identification of a physical species' response law is therefore an unresolved input, not a detail.

**10. READING, exponent form.** Define R(Lambda) = kappa_H (Lambda/M_P)^p. The clock bound requires p >= ln(E)/ln(M_P/Lambda) = 1.22 at Lambda = 10 TeV; the ansatz is p = 2; an unsuppressed coefficient (p = 0, E1's tuned toys) fails by 2.6e18. With the s*A form, s must be <= 1.05e9 at 10 TeV, while an unsuppressed coefficient c_H/2 (M_P/Lambda)^2 is 2.7e27. This only reorganises the same inequality; the definition of p is mine and differs from E1's gap-suppression exponent, so I do not map E1's p = 1 onto it.

**11. UNRESOLVED (first unresolved step).** No concrete composite or pseudo-Goldstone Higgs sector is solved, so s and A are not determined. Also undetermined: the response law for the strong sector (step 9), and the species/E_g identification of the strain that this sector sees. A derivation would need a model with the Higgs mass-squared built from a transmuted scale plus elementary-sector couplings that themselves carry lattice-scale strain shifts (E1 notes the Wilson-condensate tadpole and F1's fermion channel are not covered by this route). Nothing here derives a Standard Model or composite-Higgs coefficient.

## What is new relative to the sources

New: step 4 (exact vacuum edge, rate dichotomy, 4.1e-4 time fraction under stated Gaussian premises), step 5 (quantified regime of validity), step 6 (the margin chain A*s and the 9.6e3 factor, inferred reconstruction of 5.9e7), step 7 (identity with F6 scaling), steps 8-9 (closed form of the toy and the law-dependence). Not new: the reproduced Hessians, the E1 table, the 5.6e11 and 5.9e7 values themselves, the E1/F6 referee corrections.

## Not shown

No claim about a real composite Higgs, about the SM coupling values at the cutoff, about the reality of the nHz background, about the nonlinear end state after vacuum loss, about higher-loop terms, or about the unrefereed closed-form asymptote in step 8 beyond 12 digits on five points.
