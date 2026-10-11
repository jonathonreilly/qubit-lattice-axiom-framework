# C4 lane RL2: independent referee verdict

## VERDICT: CONFIRMED WITH CORRECTIONS

The registered outcome remains **INCONCLUSIVE, leaning FAIL**.  The exact
plane-wave reduction, operator normalization, flat targets, bare-ladder
constants, stored numerical outputs, and conditional translation arithmetic
check out.  Two claims must be narrowed.  First, the curved-mean result is an
exact plane-wave result plus a well-supported but not proved Penrose/continuum
transfer; the \(p\to0\) intercept is numerically controlled at about the 1%
level, while the advertised 0.2% level depends on accepting two coarse-grid
points.  Second, the claimed Cauchy--Schwarz/Mecke proof of the proper-time
bound does not close for the actual sprinkled-source observable: its
off-diagonal term contains **two-point Palm** inverses, not the one-point
second moment used in the report.  The physical translation table is therefore
correct arithmetic conditional on the stated rate law and on
\(\tau_{\max}=\sqrt{2Ds+s^2}\), but it is not yet a proved replacement for
RL1's fixed-source variance law.

## Findings

### 1. One-dimensional reduction, density scaling, reruns, and the G--L transfer

**Measure and closure: confirmed, in the stated regular pre-caustic plane-wave
domain.**  Put \(s_i=-2\sigma_i\).  At fixed affine \(u\), the flat-axis
Jacobian is

\[
\left|\frac{\partial(s_1,s_2)}{\partial(v,r^2)}\right|=2\Lambda,
\qquad d^2x_\perp=\pi\,d(r^2),
\]

so \(d^4z=\pi\,du\,ds_1ds_2/(2\Lambda)=
2\pi\,du\,d\sigma_1d\sigma_2/\Lambda\).  In a plane wave the transverse
ellipse contributes \((\det Q)^{-1/2}\); the already-refereed Wronskian
formula for \(\det Q\) gives precisely

\[
d^4z=\frac{2\pi}{\Lambda}
\sqrt{\frac{\Delta(y,x)}{\Delta(y,z)\Delta(z,x)}}
\,du\,d\sigma_1d\sigma_2.
\]

This confirms `RL2_report.md:32-35`.  With
\(S_1=\Lambda s_1/u\), \(S_2=\Lambda s_2/(\Lambda-u)\), the domain is
\(S_1,S_2\ge0\), \(S_1+S_2\le s\).  Laplace transformation supplies the
extra \(1/p\); the two rescaling Jacobians cancel the
\(u(\Lambda-u)/\Lambda^3\) measure, leaving \(\pi/(2\Lambda p)=\pi/(2q)\).
The fixed-\(q=p\Lambda\) Volterra equation in `RL2_report.md:36-43` and its
implementation at `rl2_A_planewave_mean.py:58-74` are therefore correct.
The Palm/Mecke closure is also valid here because consecutive open intervals
of one ordered chain are disjoint.

**Density statement: narrow it.**  The homothety
\((u,v,x_\perp)\mapsto(u,\lambda^2v,\lambda x_\perp)\) scales volume by
\(\lambda^4\) and \(s\) by \(\lambda^2\).  Equivalently, at density \(\rho\)
the dimensionless Laplace argument is \(p/\sqrt\rho\).  Thus a finite-\(p\)
answer is not literally density-independent; the lens/flat ratio is a
universal function of \(p/\sqrt\rho\), and its direct
\(p/\sqrt\rho\to0\) limit, if it exists, is density-independent.  The precise
version at `RL2_report.md:44` is defensible; the unqualified plain-summary
sentence at `RL2_report.md:18` is too strong.

**Numerics: reproduced.**  Direct reruns reproduce `rl2_core.out`,
`rl2_F_measure_check.out`, the mid-lens values at \(p=10^{-2},5\times10^{-3}\),
and the resolved \(p=10^{-3}\) ratios
\(1.01784,1.01729,1.01672\).  The deterministic \(\epsilon=1/8\) Monte Carlo
also reproduces `rl2_B_op0_eps0.125.out` exactly.  An independent calculation
which does not import `rl2_core` evaluates all Gaussian moments in closed form
(`RL2_referee_checks.py:22-57,137-149`) and obtains

| operator | \(c_2\) | \(1/(2\pi c_2)\) | \(I_1\) | \(\sqrt{4\pi I_1}\) |
|---|---:|---:|---:|---:|
| op0 | 0.692179749 | 0.229932966 | 0.643934308 | 2.844629531 |
| op1 | 0.660864714 | 0.240828326 | 0.730330421 | 3.029455848 |
| op2 | 0.631120556 | 0.252178354 | 0.884528356 | 3.333963278 |

This independently confirms `RL2_report.md:49-64,123-130`.

**Intercept sensitivity: confirmed, but it is not an error bar.**  Re-fitting
the same three ansatzes gives 0.99835--0.99846 (mid) and
0.99918--0.99945 (quarter) when the two \(q/10\) tiny-\(p\) points are used,
but 0.98971--0.99058 and 0.99134--0.99214 when only
\(p\ge10^{-3}\) is used (`RL2_referee_checks.py:60-101`).  Replacing the
mid \(p=5\times10^{-4}\) value by its \(q/20\) result moves the fitted means
only to 0.99858--0.99867, consistent with the reported common-mode check.
Nevertheless, `rl2_E_extrapolate_mean.py:24-29` fits three parameters to only
four points and reports half the spread among ansatzes; it propagates neither
quadrature error nor sampling error.  Also, the unrefined
\(p=2.5\times10^{-4}\) point has an absolute flat value wrong by more than
50% (`rl2_A_mid_tinyp.out:6-9`).  The honest numerical statement is therefore:
about **1%** from the resolved points, improving to about **0.2% conditional on
common-mode cancellation** at the two coarse tiny-\(p\) points.  This agrees
with the caveat at `RL2_report.md:82-85,199-201`.

**Penrose transfer: valid as the leading-needle argument, not as the claimed
completed computation on the finite-density conformal lens.**  All chain
points lie in the thin interval, and the Penrose scaling gives the ray's
isotropic plane wave for a conformally flat lens.  This is the correct
candidate for the leading null singularity; the standard local-wave analogue
is explicitly described by Harte and Drivas, who use Penrose limits to recover
the leading singular behavior near a null geodesic
([arXiv:1202.0540](https://arxiv.org/abs/1202.0540)).  But that result is for
local wave equations, not this nonlocal finite-density inverse.  RL2 still
needs a uniform/dominated-convergence statement that suppresses the large
dimensionless-\(s\) tail while the density limit is taken.  The worker also
did not compute finite-\(\ell\) corrections (`RL2_report.md:46-47,99-105`).
Therefore the mean is a legitimate **bounded positive/pass-type result at
plane-wave/needle order**, strongly supported for the G--L lens, but
`RL2_report.md:191` overstates matters when it says the mean is simply
"closed."

### 2. Van Vleck identity

**Confirmed, with a naming correction.**  From the definition

\[
g=\sqrt{\frac{\Delta(0,\Lambda)}
{\Delta(0,u)\Delta(u,\Lambda)}}
\]

one immediately has

\[
g\sqrt{\Delta(0,u)}=
\frac{\sqrt{\Delta(0,\Lambda)}}{\sqrt{\Delta(u,\Lambda)}}.
\]

This is exact wherever the pre-caustic Van Vleck determinants have a consistent
positive branch, and it yields the last-hop factor
\((\Delta\nu)^{-1/2}(u,\Lambda)\) after
\(k(\Lambda)=\sqrt{\Delta(0,\Lambda)}\,\kappa(\Lambda)\), exactly as stated at
`RL2_report.md:87-91`.  It is an algebraic cancellation following from the
definition of \(g\), not an independent multiplicative "chain rule" for
\(\Delta\).  For a short last hop, \(\Delta\nu=1+O(R_{kk}r^2)\), so the factor
tends locally to one.  The accumulation of those local errors through
\(O(1/q)\) renewals and the limit interchange in `RL2_report.md:93` remain an
argument, not a proved consequence of the identity.  `rl2_F_measure_check.py:7-14`
is a useful consistency check, but its \(g\) and \(\nu\) values share the same
`Ray.nu_Delta` implementation and are not a fully independent proof.

### 3. Proper-time scale and the Cauchy--Schwarz/Mecke claim

**Single-pair scale: confirmed.**  For a fixed endpoint pair, Poincare
invariance implies that \(\mathbb E H(x,y)^2\) depends only on the causal
proper time (and the operator scales).  If the source has bounded rest-frame
extent \(s\) and the observer is nearly null-separated by \(D\), then
\(\tau(x,y)^2=O(Ds+s^2)\).  The particular one-sided geometry used in the
translation table gives \(\tau_{\max}^2=2Ds+s^2\).  Other source boxes can
change the coefficient (the worker itself quotes an upper estimate of order
\(6Ds\) at `RL2_report.md:111-113`), so \(\sqrt{2Ds}\) is not a universal exact
maximum.  It is the right parametric scale for each source--observer pair.

**The displayed full-field bound is not proved for the observable actually
simulated.**  For
\(\phi_\eta(x)=\sum_{y\in\eta}J(y)H_\eta(x,y)\), second-order Mecke gives

\[
\begin{aligned}
\mathbb E\phi^2={}&\rho\int J(y)^2
 \mathbb E H_{\eta+\delta_y}(x,y)^2\,dy\\
&+\rho^2\iint J(y)J(y')
 \mathbb E\!\left[H_{\eta+\delta_y+\delta_{y'}}(x,y)
 H_{\eta+\delta_y+\delta_{y'}}(x,y')\right]dy\,dy'.
\end{aligned}
\]

Cauchy--Schwarz bounds the second line by **joint-Palm** second moments
\(\mathbb E H_{\eta+\delta_y+\delta_{y'}}(x,y)^2\), not by the one-point
\(\mathbb E H_{\eta+\delta_y}(x,y)^2\) inserted at
`RL2_report.md:115-117`.  When \(y\prec y'\prec x\), adding \(y'\) changes the
inverse by supplying an extra node and changes the count of every interval
that spans it.  The implementation makes this explicit by building all counts
from the complete sprinkled set before inversion (`rl2_B_smeared_mc.py:39-49`).
Signed weights provide no monotonicity that would justify dropping the extra
Palm point.  A uniform multi-Palm/add-one bound could repair the proof; it is
not present.

There is a second transfer gap.  The Monte Carlo source is an approximately
isotropic Gaussian near the bottom of a **timelike** tip-to-tip diamond
(`RL2_report.md:140-143`; `rl2_B_smeared_mc.py:26-35,48-49`).  A Lorentz
transformation can put one timelike source--observer pair in that frame, but
it does not turn an entire extended, rest-frame astrophysical source into the
same fixed Gaussian for all its points.  The covariance depends on the triple
invariants of \((x,y,y')\).  Consequently `RL2_report.md:203` does not follow
from Poincare invariance alone.

Thus RL1's use of \(D\) as the single-pair timelike exponent is not justified,
and \(\sqrt{Ds}\) is the natural replacement scale, but the report has not
proved that the complete sprinkled-source variance is bounded solely by that
scale.  The claimed factor \(3.5\times10^{10}\) is correct for
\(D/\sqrt{2Ds+s^2}\) in the chosen geometry, not yet a theorem for the full
field variance.

### 4. Ladder constants, Monte Carlo rates, and the \(\sqrt\epsilon\) exponent

**Constants and reruns: confirmed.**  The closed-form calculation above
independently confirms the bare constants \(2.84463,3.02946,3.33396\).  A
fresh run of `rl2_C_ladder_rates.py` reproduces the stored exact roots and the
node-only constants \(2.7315,2.8347,3.2525\)
(`rl2_C_ladder_rates.out:1-18`).  The rate re-fits independently reproduce all
last-four/last-three slopes (`RL2_referee_checks.py:104-120`).  The actual
MC/exact-ladder ratio range in the table is **0.68--0.98**, not literally
0.7--0.9 (`RL2_report.md:145-152`); this is a minor summary correction.

**Structural only for the isolated ladders.**  For the bare rung,
\(r_\epsilon\sim\epsilon^2 f(\epsilon^{1/2}\tau^2)^2\).  Its small-\(z\)
four-dimensional transform contains \(4\pi I_1\epsilon^{3/2}/z^2\), hence
\(z_{\rm var}\ell\sim\sqrt{4\pi I_1}\epsilon^{3/4}\), or
\(z_{\rm var}\ell_k\sim k\sqrt\epsilon\).  The exponent is therefore
structural for that positive bare ladder.  The analogous node ladder has the
same rescaling.  It is **not** yet structural for the full variance: node and
interior insertion amplitudes add before squaring in each nonnegative Poisson
chaos term (`RL2_report.md:133-136`).  A pointwise leading-order cancellation
could change the exponent.  The moderate range \(\epsilon\in[1/8,1]\), small
sample counts, and heavy tails (`RL2_report.md:154-155`) neither prove nor
exclude such an asymptotic cancellation over the remaining 63 decades.

### 5. Translation table and RL1 corrections

**Arithmetic: confirmed conditionally.**  From
\(\epsilon=(\ell_P/\ell_k)^4\) and
\(z_{\rm var}\ell_k=k\sqrt\epsilon\), the standard-deviation exponent is

\[
n=\frac12z_{\rm var}\tau=
\frac{k\ell_P^2\tau}{2\ell_k^3},\qquad
\ell_k(n=1)=\left(\frac{k\ell_P^2\tau}{2}\right)^{1/3}.
\]

Independent evaluation gives, for \(k=2.84\),
\(\tau=(8.7125\times10^{14},1.3607\times10^{16},1.3607\times10^{18})\) m,
\(n=(3.2319\times10^2,5.0473\times10^3,5.0473\times10^5)\), and
\(\ell_k=(6.8625\times10^{-19},1.7154\times10^{-18},7.9620\times10^{-18})\) m
for the three non-RL1 rows (`RL2_referee_checks.py:123-134`).  The other
operators shift these as reported.  At the bar,
\(\epsilon=(\ell_P/10^{-19}{\rm m})^4=6.8240\times10^{-64}\), and suppressing
323 by changing \(\epsilon^{1/2}\) to \(\epsilon^\alpha\) requires
\(\alpha=0.539724\), confirming the rounded 0.54.  The flat targets and the
\(0.9999995\) normalization correction are also confirmed.

These numbers are not an observational exclusion until both the full-variance
small-\(\epsilon\) law and the multi-Palm/null-source transfer in finding 3 are
proved.  The source-shape coefficient in \(\tau_{\max}^2=O(Ds)\) would change
\(\ell_k\) only by a sixth root, but that does not repair the missing theorem.

**Artifact note.**  `rl2_core.py:10-14` ignores the supplied local `.npy` and
loads `../RL1/RL1_F4b_stable_L6.npy`; the two files are byte-identical in this
workspace.  `rl2_C_ladder_rates.py:12-14` similarly imports the parent RL1
Volterra source dynamically.  The results reproduce, but the packet is not
self-contained as written.

### 6. Fixed-reading verdict and status of the mean result

The PASS clause at `TESTS.md:1763-1766` is not met because physical-parameter
noise is not bounded for any operator.  The FAIL clause is also not met:
there is no order-one mean mismatch in the plane-wave/needle calculation, and
unbounded noise at physical \(\epsilon\) still requires a 63-decade
extrapolation plus the missing source-geometry theorem.  `TESTS.md:5-9`
forbids resting the verdict on that extrapolation.  Therefore
**INCONCLUSIVE, leaning FAIL is correct**.  The leaning is supported by two
distinct positive ladders and all accessible fixed-source Monte Carlo rates,
but it has no preregistered decisional force.

The mean result should remain recorded as a positive result with explicit
scope: exact Volterra reduction on regular pre-caustic plane waves, exact
Van Vleck cancellation, and strong numerical evidence for GR-like
\(\sqrt\Delta\) focusing in the leading Penrose/needle limit of the two tested
G--L rays.  It should not be upgraded to an exact finite-density conformal-lens
theorem or an error claim tighter than the grid study supports.

## Strongest correct statement

For the three distinct numerically stable six-layer scalar operators, the mean realization inverse on a regular pre-caustic plane wave admits the claimed exact one-dimensional Volterra reduction, its measure and Van Vleck cancellation are correct, and independent arithmetic plus reruns confirm the operator normalizations, flat targets, and lens/flat ratios; these results strongly support convergence of the leading G--L needle-order magnification to \(\sqrt\Delta\), at about 1% on resolved grids and about 0.2% only if common-mode cancellation in the two coarse tiny-\(p\) runs is accepted, while the Penrose transfer and accumulated \(p\to0\) limit remain unproved.  The bare and node ladders have confirmed constants and structural \(\sqrt\epsilon\) scaling, and accessible fixed-source simulations grow at 0.68--0.98 of the exact bare-ladder rate, but neither ladder bounds the full variance and the proposed Cauchy--Schwarz/Mecke argument omits joint-Palm effects for a sprinkled extended source; hence the physical translation is conditional arithmetic, not a noise theorem.  Under the fixed readings and the ban on long extrapolation, RL2 is therefore **INCONCLUSIVE, leaning FAIL**, with the bounded plane-wave/needle-order mean result retained as a genuine positive result.
