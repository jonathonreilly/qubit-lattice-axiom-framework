# VERDICT: CONFIRMED WITH CORRECTIONS

The mean-d'Alembertian construction is correct, the supplied raw computation reproduces, and the finite-orbit spectral obstruction survives adversarial checking. The necessary corrections are material to scope but not to the bounded FAIL: the finite frame samples are hyperbolic balls rather than demonstrated Haar samples of the compact quotient; “grows like \(\ell^3\)” must be replaced at theorem level by a positive cubic-normalized **limsup** (with possible faster threshold/exceptional contributions); the \(r=0\) mode has an \(\ell\log\ell\) leading term rather than the rotating \(r>0\) formula; the no-go requires at least one nonzero **off-site** orbit; and the reported count of “23 weight sets” is not the count implemented by the scripts. With those corrections, the second FIXED FAIL disjunct is met in its intended sense—failure of relative suppression—for fixed, finite-orbit, linear retarded scalar kernels in Palm/Haar ensemble rms. If `O(1)` in the FIXED text is read literally as a bounded big-O upper bound, cubic growth is not `O(1)`; the scientifically coherent reading is “order unity or worse / does not tend to zero.”

## 1. Siegel \(C_m\) values and lattice counts

**Confirmed.** The program computes

\[
C_m=\rho\prod_p\alpha_p(Q,-m),\qquad
\alpha_p=\lim_{r\to\infty}p^{-3r}\#\{n\bmod p^r:Q(n)\equiv-m\},
\]

with the good-prime Euler product written as \(1/L(2,\chi_7)\) (`R4-1_report.md:81-87`; `scripts/r41_A_shell_densities.py:25-62`). I recomputed the cyclic congruence counts by exact integer convolution rather than the worker's floating FFT route, and computed \(L(2,\chi_7)\) from Hurwitz zeta values. The result is \(L(2,\chi_7)=1.15192547054449105\); \(C_1,\ldots,C_8\) agree with the supplied array to \(4.1\times10^{-14}\), and the good-prime formulas at \(p=3,5,11\) agree exactly (`referee_runs/referee_independent_checks.py:38-80,180-205`; `referee_runs/referee_independent_checks.out:1-14`).

The packet calls one-class-per-genus an assumption (`R4-1_report.md:89-92`), but it is supplied by the standard square-free-determinant theorem: \(Q=\langle-7,1,1,1\rangle\) is indefinite with square-free determinant \(-7\), so its genus has one class ([Eskin–Rudnick–Sarnak, *A Proof of Siegel's Weight Formula*, p. 1](https://www.math.tau.ac.il/~rudnick/papers/siegelmass.pdf)). Thus the fixed-form density may be identified with the local-density product; this is not merely inferred from the finite counts.

The count rerun at \(T=600\) supports the normalization: ratios are 0.9979–1.0109 for \(m=1,\ldots,16\), apart from the still-sparse high-2-adic shells; \(m=64,96\) remain at 1.1006 and 1.1548 and therefore should not be advertised as high-precision count checks (`referee_runs/A/r41_A_rerun.out:54-77`). The hyperboloid measure used in the denominator is the correct integral of \(\theta(x^0)\delta(x^2+m)\) under the same \(x^0\le\sqrt7T\) cutoff (`scripts/r41_A_shell_densities.py:70-93`).

## 2. Mean-\(\Box\) weights

**Confirmed.** Expanding \(2\pi\sqrt m K_1(K\sqrt m)/K\) gives exactly the moment conditions printed by the worker: \(S_0=S_1=S_2=0\), \(c=-(\pi/2)\sum gm\log m\), and \((\pi/16)\sum gm^2\log m=-1\) (`R4-1_report.md:101-112`; `scripts/r41_C_weights_and_deviation.py:3-6`). For any four distinct positive shells, the barycentric weights annihilate polynomials of degree at most two, while the third divided difference of \(x^2\log x\) is \(f'''(\xi)/3!=1/(3\xi)>0\), so normalization cannot vanish (`R4-1_report.md:114-117`).

My independent \(\{1,2,3,4\}\) result is

\[
g=(6.092462247979,-18.277386743936,18.277386743936,-6.092462247979),
\]
\[
f=(12.185281438619,-24.370562877237,73.111688631711,-16.247041918158),
\qquad c=-1.755620348966.
\]

All three moments vanish at displayed precision and the kinetic normalization is \(-1\) (`referee_runs/referee_independent_checks.out:16-23`). Direct Bessel evaluation gives \(\bar B/(-K^2)=0.9996995,0.9978867,0.9836833,0.9103584\) at \(K=0.01,0.03,0.1,0.3\), reproducing the worker (`referee_runs/referee_independent_checks.out:24-27`; `R4-1_report.md:121-123`). Hence \(\bar B=-K^2+O(K^4\log K)\), equivalently \(\Box[1+O(a^2k^2\log ak)]\), with the usual retarded boundary-value continuation.

## 3. Numerics, frame sampling, and normalization

### Reruns and what they establish

The full \(M=96\), 48-frame, seed-7 enumeration was rerun. All five raw arrays (`S`, `I`, `ells`, `etas`, `C`) are bit-for-bit identical to the supplied NPZ when loaded with `allow_pickle=False`; the run enumerated 11,002,449 vectors and finished all frames (`referee_runs/B/r41_B_rerun.out:1-60`). Re-running the weight analysis reproduces every printed slope in the 18-set `C` script, from +2.23 to +3.23 (`referee_runs/B/r41_C_rerun.out:3-235`). The independent raw-array implementation gives +3.083 relative and +1.083 absolute for the four-shell kernel in the \(\eta\le1\) sample, and +3.377 relative/+1.377 absolute in the independent \(\eta\le0.6\) sample (`referee_runs/referee_independent_checks.out:29-50`). The min-norm 96-shell example is more log-periodic but still gives positive absolute fitted slopes +0.228 and +0.747 over the available windows (`referee_runs/referee_independent_checks.out:51-71`). The \(M=160\) flat-kernel rerun also reproduces the output (`referee_runs/D/r41_D_rerun.out:3-121`).

The truncation reach check is adequate for these runs: the code enforces \(8\ell_{\max}e^{\eta_{\max}}\le R_{\max}\), which is the correct worst-case inverse-boost bound (`scripts/r41_B_shell_sums.py:15-16`), and the Gaussian tail beyond eight widths is negligible. The exact continuum mean is evaluated independently of the frame sample by quadrature (`scripts/r41_B_shell_sums.py:50-54`).

### Corrections to the numerical claim

The frames do **not** numerically estimate Haar rms on \(\Gamma_L\backslash H^3\). The generator samples hyperbolic volume only in the universal-cover ball \(0\le\eta\le\eta_{\max}\) (`scripts/r41_B_shell_sums.py:65-76`); no fundamental domain, reduction map with multiplicity, or quotient covering/equidistribution argument is implemented. Consequently 48 frames at \(\eta\le1\) and 30 at \(\eta\le0.6\) are enough to show robust local direction dependence and to illustrate the log-periodic scaling, but not to measure the quotient-wide ensemble norm. The large nonzero sample means make this visible: for the four-shell kernel at \(\ell=19\), the \(\eta\le1\) sample has rms \(2.87\times10^4\), sd \(1.81\times10^4\), and mean \(2.22\times10^4\); the \(\eta\le0.6\) sample has rms \(5.13\times10^4\), sd \(1.07\times10^4\), and mean \(5.02\times10^4\) (`referee_runs/referee_independent_checks.out:39,49`). The spectral proof, not this sampling, establishes the Haar/Palm statement.

The “23 sets” count is bookkeeping drift. `r41_C_weights_and_deviation.py` actually runs 5 divided-difference + 3 min-norm + 5 smooth-\(f\) + 5 smooth-\(g\) kernels = 18 (`scripts/r41_C_weights_and_deviation.py:80-90`). Adding the six flat families gives 24 named distinct constructions; `r41_D_flat_kernels.py` also reruns three finite-\(M\) exponential families and the duplicate four-shell kernel (`scripts/r41_D_flat_kernels.py:91-97`). This does not affect the sign of any reported fit.

### Is division by \(\Box\phi\) fair?

Yes for the registered effective-law test, with a physical-interpretation qualification. For the fixed-peak Gaussian, \(|\Box\phi(0)|=2/\ell^2\) (`scripts/r41_C_weights_and_deviation.py:7,66-71`). Therefore a relative \(\ell^3\) limsup is an absolute \(\ell\) limsup, not an artefact created solely by a small denominator. In the four-shell raw data the absolute rms rises from 32.4 at \(\ell=6\) to 158.9 at \(\ell=19\), and to 341.6 at \(\ell=24\) in the second sample (`referee_runs/referee_independent_checks.out:35-50`). A local second-order operator acting on this fixed-amplitude, increasingly smooth family should instead vanish like \(\ell^{-2}\); the result therefore obstructs convergence to that effective operator.

This is an operator test, not yet a direct observable. If each Gaussian were rescaled to fixed four-dimensional \(L^2\) norm, its peak would supply an extra \(\ell^{-2}\), and the absolute deviation could fall while the relative error still grows cubically. Nor does an ensemble-rms Gaussian result by itself give a real-momentum dispersion or a statement for every physical solution. Those qualifications do not rescue the FIXED PASS criterion, which is explicitly relative to the target effective law (`TESTS.md:2804-2811`).

## 4. Spectral theorem

### 4.1 Palm/Haar reduction and Parseval

**Confirmed.** Conditioning the stationary affine-lattice process on a lattice point at the evaluation event fixes the torus shift and leaves the orientation with normalized Haar law on \(G/\Gamma_L\). Because the test Gaussian is invariant under the observer's spatial rotation group \(K\), the observable factors through

\[
K\backslash G/\Gamma_L\simeq\Gamma_L\backslash G/K
=\Gamma_L\backslash H^3.
\]

For each shell, decomposition into finitely many \(\Gamma_L\)-orbits gives the usual automorphic point-pair kernel; dividing each orbit representative by its finite stabilizer gives precisely \(\Psi_j(m)=\sum\psi_j(\hat w)/|\Gamma_{\hat w}|\) (`R4-1_report.md:177-191`). With eigenfunctions orthonormal for normalized quotient measure, the constant mode is the Palm ensemble mean and Parseval gives the exact Haar ensemble mean square of the centered observable. The numerical ball sample is not needed for this identity.

### 4.2 Mode asymptotics, including \(r=0\) and exceptional modes

For fixed real \(r>0\), the displayed transform is correct with an **additive** remainder:

\[
\widehat h_{m,\ell}(r)=\frac{\pi}{r}\operatorname{Im}\!\left[
\Gamma\!\left(\tfrac12+\tfrac{ir}{2}\right)
\left(\frac{4\ell^2}{m}\right)^{\frac12+\frac{ir}{2}}
\right]+O(\ell^{-1}).
\]

Writing this as “leading term \(\times[1+O(\beta)]\)” is unsafe at its log-periodic zeros. The supplied quadrature reproduces the additive expansion for \(r=1,3,6\) (`referee_runs/F/r41_F_rerun.out:1-9`). The constant eigenfunction is separate and has \(\pi[K_1(\beta)-K_0(\beta)]\sim\pi/\beta\), as checked (`referee_runs/F/r41_F_rerun.out:10-11`).

The worker's sentence that \(r=0\) is “handled the same way” is not literally correct (`R4-1_report.md:193-200`). The \(\lambda=1\) threshold transform is the \(r\to0\) limit and has

\[
\widehat h(0,\beta)\sim
\frac{\pi\sqrt\pi}{2}\sqrt{\frac2\beta}
\left[\log\frac2\beta+\psi\!\left(\tfrac12\right)\right],
\]

so a threshold mode is \(\ell(A\log\ell+B)\), not a rotating \(\ell e^{ir\log\ell}\) mode. Independent quadrature converges to this formula with ratios 1.0161, 1.00136, 1.00013 (`referee_runs/referee_independent_checks.out:73-76`). PASS still forces its leading coefficient \(A_j=0\) (and then the next threshold coefficient as well), so this correction strengthens rather than breaks the obstruction.

For an exceptional nonconstant eigenvalue \(\lambda=1-t^2\), \(0<t<1\), analytic continuation gives a leading \(\ell^{1+t}\) term, followed by \(\ell^{1-t}\). The worker's “grow faster” statement is correct when the leading exceptional coefficient is nonzero; it is not an unconditional statement for every exceptional mode. A \(t=1/2\) quadrature approaches the predicted \(\beta^{-3/4}\) leading law (`referee_runs/referee_independent_checks.out:77-79`). There are only finitely many exceptional/threshold modes below any fixed spectral cutoff on the compact orbifold.

### 4.3 Infinitely many conditions

**Confirmed, with the threshold correction above.** The FIXED PASS demand is relative \(O(\ell^{-2})\); since \(|\Box\phi|=2/\ell^2\), it requires absolute quotient norm \(O(\ell^{-4})\). Projection onto any fixed real-\(r_j>0\) eigenmode and the additive asymptotic then forces

\[
A_j(f)=\sum_m f_m m^{-1/2-ir_j/2}\Psi_j(m)=0.
\]

Otherwise the sinusoidal leading coefficient has a positive \(\ell^{-1}\)-normalized limsup. At \(r=0\), the \(\ell\log\ell\) coefficient forces the same \(A_j=0\) first. Since the compact quotient has infinitely many tempered eigenmodes and only finitely many exceptional ones, PASS imposes infinitely many spectral cancellations (`R4-1_report.md:187-202`).

### 4.4 Wavefront step and torsion

**Confirmed after making two implicit points explicit.** Define \(A=\sqrt{-\Delta-1}\) on the real tempered spectrum and extend it over the finite-dimensional threshold/exceptional sector by any fixed spectral branch; different low-mode extensions differ by a smoothing finite-rank operator. At high frequency, \(A-\sqrt{-\Delta}\) has order \(-1\), so \(e^{-itA}\) is a half-wave Fourier-integral operator with the usual geodesic canonical relation. For

\[
D=\sum_m f_m m^{-1/2}e^{-\frac i2(\log m)A}\mu_m,
\]

the tempered Fourier coefficients are the \(A_j(f)\). If all vanish, \(D\) is smooth (indeed it lies in the finite non-tempered eigenspace). Applying the inverse half-wave time of one supported orbit isolates its point mass. Every other nonzero-time term has wavefront at that point only along the finitely many cotangent rays belonging to geodesic segments of the prescribed length; discreteness/properness of \(\Gamma_L\) makes the number of lifts at fixed length finite. A delta mass has the entire punctured cotangent fibre, so equality is impossible (`R4-1_report.md:202-212`).

Torsion does not invalidate this comparison. In a local orbifold chart \(\widetilde U/H\), \(H\) is finite. The lifted delta still has the full punctured cotangent fibre, while the finitely many geodesic rays acquire only finitely many \(H\)-images. Stabilizer weights \(1/|H|\) are nonzero scalars and cannot remove the full-fibre singularity. The same local lift also justifies the point-pair spectral expansion at orbifold points.

The theorem must say “at least one nonzero off-site orbit.” A purely on-site operator \(c\phi(x)\) is nonzero but frame-independent and is a counterexample to the worker's literal “not identically zero (any on-site \(c\))” wording (`R4-1_report.md:214-217`). Such an operator cannot have mean \(\Box\), so this wording error does not affect the constructed candidates or the reading.

The proved asymptotic is

\[
\limsup_{\ell\to\infty}\frac{\|\Delta_\ell\|_{L^2(\Gamma\backslash H^3)}}{\ell}>0,
\qquad
\limsup_{\ell\to\infty}R_\ell\left(\frac a\ell\right)^3>0,
\]

where \(R_\ell=\|\Delta_\ell\|/|\Box\phi_\ell|\). It is not a proof that every realization has \(R_\ell\sim C\ell^3\), that the quotient norm is bounded below at every sufficiently large \(\ell\), or that no faster exceptional/threshold growth occurs. The worker itself correctly leaves exceptional individual realization points open (`R4-1_report.md:237-244`).

## 5. Relation to R3-1 and R3-3

This **extends rather than contradicts** both earlier probes.

- R3-1 established genuine direction dependence for a single-shell tube symbol but its referee rejected the fitted IR exponent and nonshrinking absolute limit as unproved, explicitly noting that multi-shell moment cancellations could change them (`C5_R3-1_referee.md:43-51`). R4-1 supplies those mean-\(\Box\) cancellations and proves a finite-support ensemble-rms limsup by spectral/wavefront methods. It therefore closes a narrower question that R3-1 left open; it does not turn the imaginary-momentum diagnostic into a real on-shell observable.
- R3-3 found that a **single positive one-hop response relative to its own mean** falls roughly as \(D^{-1}\) (`C5_R3-3_report.md:137-170`). R4-1 instead forms signed shell combinations whose \(O(\ell^2)\) constant-mode pieces cancel down to \(O(\ell^{-2})\), while at least one nonconstant automorphic mode remains \(O(\ell)\) along a subsequence. The resulting \(\ell^3\) relative obstruction is a different normalization and kernel, not a contradiction.
- R3-3's focusing statement was conditional on a per-realization local second-order law (`C5_R3-3_report.md:178-197`). R4-1 excludes that route for the stated finite-orbit scalar class on the Gaussian test family, but leaves the report's infinite-orbit, nonlinear/tensor/spinor, curved, and ensemble-only alternatives outside the theorem (`R4-1_report.md:225-244`).

## 6. Reading and no-go scope

**FAIL (bounded) is the correct campaign reading**, provided the second FIXED disjunct is read as “the relative deviation fails to vanish (order unity or worse),” which is the only reading consistent with using growth as a stronger failure. The first FAIL disjunct is false because explicit mean-\(\Box\) weights exist. The PASS deviation clause fails because the theorem supplies an unbounded cubic-normalized limsup in Palm/Haar ensemble rms. A literal asymptotic reading of “stays `O(1)`” as “has a bounded upper limit” should be corrected to `not o(1)` or “remains order unity or larger”; \(\ell^3\) is not mathematically `O(1)` (`TESTS.md:2808-2811`; `R4-1_report.md:55-67`).

The negative claim passes a bounded no-go stress test only at this scope:

- **N1 (routes):** mean-moment cancellation, finite-kernel smearing/flatness, quotient-mode cancellation, threshold/exceptional modes, and orbifold/torsion singularity cancellation were separately checked. The first two improve the mean/prefactor but do not remove all automorphic coefficients; the last three are covered by the corrected spectral and wavefront argument.
- **N2:** no independence count is claimed for the outside-domain exits (infinite support, nonlinear/internal representations, curved realizations, individual exceptional points).
- **N3:** the hidden hypotheses are now explicit: Palm/Haar averaging, compact hyperbolic orbifold spectral calculus, fixed isotropic Gaussian family, fixed finite orbit support, scalar linear retardation, and at least one off-site orbit.
- **N4:** R3-1 and R3-3 are context, not substitute witnesses: their residuals are respectively a one-shell tube diagnostic and a positive one-hop response, not this signed mean-\(\Box\) ensemble norm.
- **N5:** the result is per-mode/quotient-ensemble and finite-orbit; it is not lattice-wide pointwise failure for every realization or every law.
- **N6:** no “new axiom required” conclusion follows. Infinite spectral synthesis or a different operator class is a mathematical construction problem.
- **N7:** the strongest counter-route is an infinitely supported fixed kernel engineered to cancel all automorphic coefficients; the finite-sphere wavefront argument does not close it. This route lies outside, and therefore sharply bounds, the theorem.
- **N8:** R3-1's proposed smooth/Bragg suppression is not retired in the infinite-support limit. The finite truncations only show that fixed finite smearing does not evade the theorem.

## Strongest correct statement

For the cocompact \(L_7\) Lorentz-random-lattice ensemble, the exact shell densities are the stated local-density products and four distinct proper-time shells admit explicit retarded weights whose Haar ensemble mean has symbol \(-k^2+O(a^2k^4\log ak)\); however, for any fixed linear retarded scalar kernel with finitely many \(\Gamma_L\)-orbits and at least one nonzero off-site weight, evaluated at a Palm lattice point on the fixed-peak isotropic Gaussian family, the centered response on \(\Gamma_L\backslash H^3\) obeys \(\limsup_{\ell\to\infty}\|B\phi_\ell-\mathbb E B\phi_\ell\|_2/\ell>0\), hence \(\limsup R_\ell(a/\ell)^3>0\) for \(R_\ell=\|B\phi_\ell-\mathbb E B\phi_\ell\|_2/|\Box\phi_\ell|\); fixed finite smearing can reduce sampled coefficients but cannot produce the registered \((a/\ell)^2\) relative falloff. This is an ensemble-rms, finite-orbit no-go on one off-shell test family—not a pointwise theorem for every realization, not a universal exact \(\Theta(\ell^3)\) law, and not a result for infinitely supported, nonlinear, internal-index, curved, or ensemble-only constructions—so the FIXED reading is **FAIL (bounded)** in precisely that class.
