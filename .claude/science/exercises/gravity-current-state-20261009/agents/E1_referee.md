# E1 and S1: referee verdict (codex gpt-5.6-sol, xhigh; other vendor; 2026-10-09)

Paths below point to the referee's scratch copy; the worker's files are in `scripts/E1/`, the referee's own scripts in `scripts/E1/referee/`.

**Supervisor response on S1 (CHECKED, `scripts/E1/S1b_slab_vs_diamond.py`):** the factor 4 is not a Jacobian error. S1 integrates over a time slab of depth T (cosh η ≤ T/τ) and gets 6.695; the worker's diamond of height T (cosh η ≤ (T²+τ²)/2Tτ) gives 1.674. Direct integration at T = 20, 40, 80 gives slab 6.558, 6.655, 6.684 and diamond 1.581, 1.644, 1.665, so both conventions converge to their own limit. The physical past of an observer is slab-like, so the physical gain is four times the diamond value. That raises the conditional bound on ℓ_k by about 2^(1/3) ≈ 1.26 and does not change the verdict.

# Referee verdict

**E1: INCONCLUSIVE — leaning FAIL.**

The worker’s **FAIL (bounded)** is not confirmed under the fixed protocol. The mean conditions pass and the ε = 0.2 recurrence is genuinely exponentially unstable, but the decisive bound extrapolates a Lyapunov law from ε = 0.05–0.2 to ε ≈ 7×10⁻⁶⁴. Neither S1 nor the simulations establish that dynamical exponent. `TESTS.md:8,179-182` therefore requires INCONCLUSIVE.

**S1: CONFIRMED WITH CORRECTIONS.**

S1 correctly establishes a finite nonzero limit and correctly computes all finite-ε convergence ratios. Its absolute coefficient is wrong by exactly four:

\[
\frac{A^2}{\epsilon T^2}\longrightarrow 1.673867577,
\]

not 6.695470309. The missing factor is the \(1/4\) Jacobian in \(\tau\,d\tau\to m^{-1/2}dm\); S1 and the worker use the same weights, so this is not a normalization convention.

The complete referee report is [REFEREE_VERDICT.md:1](<REFEREE_VERDICT.md:1>).

## Findings

1. **Operators — correct, with a truncation caveat.**  
   The 2D and 4D coefficients, smearing polynomials, and prefactors agree with the supplied literature and `bd_core.py:17-37,165-184`. Poisson factorial moments independently reproduce the 4D continuum polynomial. `SMAX=24` omits only \(2.12\times10^{-14}\) of the squared gain, but its signed mean truncation error grows as \(-1.32\times10^{-7}T^2\); it is safe for the reported \(T\le16\), not for direct evolution to \(T\sim\epsilon^{-1/2}\). `E1_2_4d_validate.out` is not useful validation because empty target sets cause its NaNs. [Report:20-52](<REFEREE_VERDICT.md:20>)

2. **Mean shape-blindness — exact in the stated test.**  
   A constant determinant-one map carries the \(g\)-order to the Minkowski order while preserving the Poisson law. Indeed the whole distribution of a covariantly defined order observable is invariant, not merely its mean. Per realization, however, the finite causal order is piecewise constant in strain with jumps when pairs cross nullness. The five-point rms fit is \(s^{0.507}\), not evidence for a universal 0.53 exponent. Physically this is zero mean TT stiffness accompanied by realization-wise “crackling” noise. `E1_6b_strain.py:81-103`; `E1_6b_strain.out:1-5`. [Report:54-76](<REFEREE_VERDICT.md:54>)

3. **One cone in mean — exact, narrowly interpreted.**  
   Translation and Lorentz invariance plus retarded support imply \(\bar B(p)=F(p^2,\operatorname{sgn}p^0)\), hence a common real massless cone. The two-species 1+1 calculation confirms rapidity invariance, but neither probes null momentum nor proves identical off-shell dispersion. The 4D mean operator also has complex zeros, so “one cone” does not mean “one mode” or “stable.” `E1_1_2d_mean_and_noise.py:48-89`; `lit_bbl2015/bbl2015.txt:225-264,697-700`. [Report:78-93](<REFEREE_VERDICT.md:78>)

4. **Noise scalings — partly established.**  
   The analytic row-gain integrals give logarithmic 2D growth and \(1.673867577\,T^2\) in 4D. The element-variance data are consistent with \(\tau^2\), with a late-bin fit \(2.175\), but the ε→0 behavior of \(\kappa\) remains unknown. The 4D window exponents refit to −1.55, −1.31, and −2.33; windows only reach \(2.2\ell_k\), with eight realizations at the endpoint. Thus \(\lambda^{-2.0\pm0.3}\) and marginality are plausible power counting, not established asymptotics. [Report:95-120](<REFEREE_VERDICT.md:95>)

5. **Instability — real at ε = 0.2, but renewal is not a theorem.**  
   An independent 12-realization extension through \(10.5\ell_k\) strongly favors an exponential over a power law: rate 0.645, log-RSS 0.0095 versus 0.145. The ε = 0.05 series is too short and is actually fit better by a power law over its three points. Nominal measured rates 0.407, 0.454, 0.735 compare with renewal predictions 0.333, 0.471, 0.666. Overlapping intervals invalidate literal independence; measured covariance corrections are about 5–24% at ε = 0.2 and 15–66% at ε = 0.1. Alternating signs protect smooth correlated errors, whereas rough errors see \(\sum w^2\). Therefore “every ε>0 gives \(\gamma\propto\sqrt\epsilon\)” is an argument, not a theorem. [Report:122-157](<REFEREE_VERDICT.md:122>) Published continuum work likewise reports numerical 4D instability, while contour/Wheeler prescriptions can project out the complex modes: [Generalized Causal Set d’Alembertians](https://arxiv.org/abs/1403.1622), [Nonlocal Scalar QFT from Causal Sets](https://arxiv.org/abs/1411.6513).

6. **Extrapolation — S1 proves row gain, not the rate exponent.**  
   S1’s exact finite-ε ratios survive the factor-four correction. Still extrapolated are the joint-error/renewal closure in the double-scaling regime \(T\sim\epsilon^{-1/2}\), \(\kappa(\epsilon\to0)\), treatment of complex modes, and the scalar-to-GW bridge. The physical verdict is sensitive to this: retaining the ε = 0.1 calibration, an exponent about \(\epsilon^{0.711}\)—not necessarily \(\epsilon^1\)—would already erase the claimed exclusion. [Report:159-180](<REFEREE_VERDICT.md:159>)

7. **Translation — arithmetic correct, physical mappings conditional.**  
   Conditional on the renewal law,
   \[
   \ell_k^3>1.585\,\ell_P^2L
   \]
   and the quoted \(2.34\times10^{-15}\) m and \(3.78\times10^{-15}\) m bounds are correct. The wavetrain calculation similarly gives \(2.61\times10^{-18}\) m, but its tensor rate is asserted rather than derived. The swerve unit conversions are correct; mapping \(Q\) onto the Philpott–Dowker–Sorkin photon coefficients or Kaloper–Mattingly worldline diffusion is not derived. The lenient rows rely on a preferred-frame cutoff. [Report:182-218](<REFEREE_VERDICT.md:182>) See [Philpott–Dowker–Sorkin](https://arxiv.org/abs/0810.5591) and [Kaloper–Mattingly](https://arxiv.org/abs/astro-ph/0607485). The newer [GWTC-4.0](https://dcc.ligo.org/LIGO-P2500066/public) graviton-mass result changes only an order-one comparator and is not load-bearing. An FRW past makes the gain finite but does not parametrically remove the conditional 1 Gpc bound.

8. **General kernel claim — exact as an \(L^2\) statement only.**  
   Every nonzero measurable retarded 4D kernel \(K=h(V)\) has infinite white-noise gain in an infinite Minkowski past because each nonzero proper-time slice contains an infinite hyperboloid-volume factor. Alternating signs cannot cancel \(|K|^2\). A finite cosmic past makes the norm finite. This proves divergent row noise, not exponential dynamical instability; correlations, angular dependence, cutoffs, or another solution prescription can alter the latter. [Report:220-239](<REFEREE_VERDICT.md:220>)

9. **Fixed-reading verdict.**  
   Since the verdict-changing ε exponent is not established and `TESTS.md:8` forbids resting a verdict on long extrapolation, the prescribed reading is **INCONCLUSIVE**, although the finite-ε evidence gives a serious and technically credible lean toward FAIL.

## Strongest correct statement

For the Poisson/Minkowski test, constant volume-preserving strain is exactly shape-blind in law and the ensemble-mean retarded operator has one common real massless cone. The 4D one-step gain has the analytic asymptotic \(A^2\sim1.6738676\,\epsilon(T/\ell_k)^2\), and an independent extension confirms genuine exponential growth of the naive recurrence at ε = 0.2 beyond \(9\ell_k\). What has not been established is that its Lyapunov exponent remains proportional to \(\sqrt\epsilon/\ell_k\) down to ε≈10⁻⁶⁴, or that the proposed scalar-noise translations are the relevant GW and swerve observables. Those missing steps generate the claimed \(\ell_k\gtrsim2\times10^{-15}\) m exclusion, so under the fixed no-long-extrapolation rule E1 is **INCONCLUSIVE, leaning FAIL**, not a confirmed bounded FAIL.