# Independent referee report: Campaign C3, lane G-B

**Referee verdict under the fixed `TESTS.md` reading: INCONCLUSIVE.**

The admixture calculation closes, with qualifications, for the registered
single-observer, rms, source-driven trace-reversed tensor proxy.  The other
mandatory PASS conjunct does not: at finite sprinkling density the exact mean
is \(\bar K_\rho*T\), not the linearized-GR retarded solution \(G_R*T\).
The difference is extremely small at one Gpc for \(\ell=\ell_P\), but the fixed
reading says **exactly**, not "up to negligible finite-density corrections."

This is not a FAIL.  The fixed FAIL arm requires a controlled law putting the
admixture above \(10^{-3}\); the controlled result instead puts it enormously
below that bar.  The applicable fallback is therefore INCONCLUSIVE.

## Exact scope of the surviving result

For a Poisson sprinkling of flat \(3+1\)-dimensional Minkowski spacetime, the
field

\[
 \bar h^{\mu\nu}(x)=\frac{a}{\rho}
 \sum_{y\in\Pi}L_\Pi(x,y)T^{\mu\nu}(y)
\]

is treated as a **trace-reversed potential**, with the same scalar link kernel
on all ten components.  For the smooth conserved superpotential source used
here, and more generally for projected weights whose squared norm is regular
across the cone-normal shell, the E1-prime-b geometry gives a uniform
single-event variance bound.  It controls the rms potential-amplitude ratio at
a specified observer, and detector-smoothed ratios for filters that do not
suppress the mean TT signal.

It does not establish an exact finite-density GR Green function, a physical
curvature-polarization observable, an event-wise or worldline supremum,
generic binary-neutron-star stresses, initial-value propagation, regeneration,
masslessness protection, nonlinear gravity, or the order's strain response.
It remains a test setting and inherits the E1/E1-prime axiom conflicts.

## 1. Load-bearing re-derivation

### 1.1 Vector-weight corollary of E1-prime-b

Let

\[
 F_w(\Pi)=\sum_{y\in\Pi}w(y)L_\Pi(x,y),\qquad w:S\to\mathbb C^k.
\]

Applying the Poisson Poincare inequality to all real and imaginary components
and summing gives, without a dimension-dependent loss,

\[
 \mathbb E\|F_w-\mathbb EF_w\|^2
 \le \rho\int \mathbb E\|D_zF_w\|^2\,dz.
\]

This is exactly the componentwise extension of Last--Penrose theorem 18.7;
the cited theorem has the required scalar inequality for every \(L^2\)
Poisson functional ([official text](https://stoch.math.kit.edu/img/Last/lastpenrose2017.pdf)).

The add-one cost is

\[
 D_zF_w=w(z)L(x,z)-\sum_y w(y)L(x,y){\bf1}_{z\in I(y,x)}.
\]

Using \(\|a-b\|^2\le2\|a\|^2+2\|b\|^2\) produces:

- the new-link term \(2\,\mathrm{Diag}_w\);
- the diagonal killed-link term
  \(2\rho^2\int\|w(y)\|^2V_y e^{-m_y}dy\), equal to
  \(\mathrm{Diag}_w\) at leading shell order because
  \(\langle m\rangle=1/2\);
- the off-diagonal term

  \[
  2\rho^3\iint
  \operatorname{Re}\langle w(y),w(y')\rangle
  |I_y\cap I_{y'}|p_{yy'}\,dy\,dy'.
  \]

Here \(p_{yy'}\le e^{-(m_y+m_{y'})/2}\).  Cauchy--Schwarz followed by
AM--GM bounds the inner product by
\((\|w(y)\|^2+\|w(y')\|^2)/2\).  Symmetry then reduces the inner integral to
the same pointwise needle-overlap integral bounded in the refereed E1-prime-b
argument.  With its corrected unequal-shell bound, the transverse integral is
finite and the off-diagonal contribution is
\(C_S(s/D)\mathrm{Diag}_w\).

The qualification matters.  This is not valid for every merely bounded
vector weight.  Comparing the outer \(e^{-m/2}p(m)\) integral with
\(\mathrm{Diag}_w\), which carries \(e^{-m}\), requires cone-normal
regularity.  The actual weights
\(w=P T\,e^{-i\Omega t}\) satisfy it: their norms are independent of the
harmonic phase and vary only on the macroscopic spatial source scale.  Thus,
for the source actually tested,

\[
 \mathbb E\|\delta F_w\|^2
 \le \left[3+C_S'\frac{s}{D}\right]\mathrm{Diag}_w,
\]

with the E1-prime-b shell and remote-tail corrections absorbed as in its
referee report.  The exact Poincare, add-one, and AM--GM steps plus the
refereed asymptotic geometry make this **controlled**, not EXACT.

I reran the stored direct Poincare check on a fresh small sample
(`s=6,D=20,n=40,seed=991`): `Var/Diag = 1.202 +/- 0.278` and
`RHS/Diag = 2.106 +/- 0.246` for non-TT, with the theorem inequality in the
correct direction.  The stored larger runs and the independent sampler also
agree with the worker's Fano factors.

### 1.2 The 1-Gpc admixture number

For the pure-TT superpotential orientation, independent angular/radial
integration gives

\[
 N_g=0.464212247803167,
 \quad I_1=0.00952230251903932,
 \quad I_2=0.0336081265377859.
\]

At \(s=10^5\,\mathrm m\), \(\lambda=3\times10^6\,\mathrm m\),
\(D=3.0857\times10^{25}\,\mathrm m\), and
\(\ell=1.616255\times10^{-35}\,\mathrm m\), I obtain

\[
 (\Omega s)=0.20943951023932,
 \qquad \widehat g=0.998314121023081,
\]

and

\[
 A_{\rm diag}^2
 =\frac{\sqrt6}{3}\frac{\ell^2D}{s^3}
 \frac{1152I_1(\Omega s)^{-4}+64I_2(\Omega s)^{-2}}
 {N_g^2\widehat g^2}
 =1.76213668823907\times10^{-55}.
\]

Consequently the leading \(F=3\) value is

\[
 \sqrt{3A_{\rm diag}^2}=7.27077029255994\times10^{-28}.
\]

This reproduces the advertised rounded \(7.3\times10^{-28}\).  Strictly, the
proved expression is

\[
 A_{\rm rms}\le
 7.2707703\times10^{-28}
 \sqrt{1+\frac{C_S'}{3}\frac{s}{D}}
\]

plus the stated shell corrections.  Since \(C_S'\) was proved finite but was
not numerically tracked, \(7.3\times10^{-28}\) is a leading-asymptotic bound,
not a literal certified decimal ceiling.  The rounded ceiling would follow
already from the extremely weak \(C_S'<7.46\times10^{18}\).  More importantly,
the fixed \(10^{-3}\) test bar would survive for
\(C_S'<1.75\times10^{69}\).  The constructive overlap proof and the measured
Poincare RHS are nowhere near such values, so this bookkeeping issue does not
threaten the admixture conjunct.

The reruns were:

- the worker's closed-form/quadrature law and translation scripts;
- `work/verify/v_closed.py`, which shares no worker formulas for its numerical
  quadrature path;
- `work/verify/v_mc.py 20 6 400 909`, which returned
  \(F_{\rm nonTT}=1.279\pm0.091\) and \(A_{\rm rms}=9.138\), consistent with
  the worker's \(1.343\pm0.041\) and \(9.36\) at larger statistics;
- `referee_checks.py`, an independent compact recomputation retained with this
  report.

### 1.3 The exact mean

Mecke gives exactly

\[
 \mathbb E\bar h^{\mu\nu}=\bar K_\rho*T^{\mu\nu},\qquad
 \bar K_\rho(z)=\frac{\sqrt\rho}{2\pi\sqrt6}
 e^{-\pi\rho\tau^4/24}{\bf1}_{z\in J^+(0)}.
\]

Translation invariance and source conservation do imply

\[
 \partial_\mu\mathbb E\bar h^{\mu\nu}=0
\]

exactly.  They do **not** imply that \(\bar K_\rho\) is the local retarded
Green function.  Unlike \(G_R\), \(\bar K_\rho\) has support throughout the
timelike interior.  Writing \(u=t^2-r^2>0\) and \(c=\pi\rho/24\), away from
the cone,

\[
 \Box e^{-cu^2}=8cu(2cu^2-3)e^{-cu^2},
\]

which is generically nonzero.  Thus \(\bar K_\rho*T\) does not solve the
linearized local GR wave equation exactly at finite \(\rho\).

The literature states the same distinction: the 3+1-dimensional causal-set
propagator equals the continuum retarded propagator only with the infinite
density limit taken ([Johnston 2008](https://arxiv.org/abs/0806.3083)), while
finite density has explicit correction terms
([Johnston 2015](https://arxiv.org/abs/1411.2614)).

The worker's arrival-delay arithmetic is correct.  The half-Gaussian shell has
\(\langle\sigma\rangle=2\sqrt6\,\ell^2/\pi\), giving
\(\langle\Delta t\rangle=2.20177\times10^{-104}\,\mathrm s\) at one Gpc.
That tiny but nonzero delay is itself evidence that the finite-density kernel
is not exactly \(G_R\).

## 2. Rulings on every adversarial-check issue

1. **"Exactly" clause: sustained and verdict-changing.**  Exact harmonic
   structure is not exact equality to the GR retarded solution.  The
   supervisor's pre-results wording cannot relax the fixed `TESTS.md` word
   "exactly"; commuting derivatives proves transversality, not Green-function
   equality.  This converts the worker/adversarial PASS to INCONCLUSIVE.

2. **Pre-registered Fano-growth trigger: facts sustained; proposed automatic
   INCONCLUSIVE not sustained.**  Growth with \(s/\ell\) is present, and the
   claimed saturation is statistically weak and unnecessary.  But PREREG
   makes the governing condition "the tensor corollary cannot be made
   controlled," with growth given parenthetically as an example.  The analytic
   vector corollary was itself pre-registered and, for the actual weights,
   supplies uniform control independent of a fitted trend.  It therefore
   legitimately answers that diagnostic.  The later \(s=36,48\) saturation
   story must not be used as the reason for control.

3. **Label inflation: sustained.**  The corollary is CONTROLLED.  Its
   functional inequalities are exact, but the shell average, needle geometry,
   tail split, and untracked shape constant are controlled asymptotics.

4. **Face-on BNS factor: sustained.**  The correct
   \(|\Sigma_{TT}|^2_{\rm face}/|\Sigma_{TT}|^2_{\rm edge}\) is 8, so the
   face-on admixtures are the edge-on values divided by \(\sqrt8\), not by 2.
   The corrected low end is about \(1.63\times10^{-28}\) at \(v=0.4\).
   This correction is conservative and does not affect the bar.

5. **BNS stress allowance: sustained.**  Pressure and self-gravity were not
   explicitly modeled.  A factor-two allowance is plausible but not a
   controlled conserved BNS source calculation.  The BNS numbers are ARGUED;
   the smooth superpotential source is the controlled benchmark.

6. **Per-realization versus rms: sustained.**  The theorem controls
   \(\mathbb E A^2\), and Chebyshev controls one specified observer event.  It
   does not give a deterministic bound in every realization or a supremum
   along an entire worldline.  The admissible scope is rms/probabilistic and
   detector-smoothed, as pre-registered.

7. **Smoothing statement: sustained with qualification.**  Minkowski controls
   the smoothed numerator, but the ratio is controlled only for a normalized
   or matched filter whose transfer function does not suppress the mean TT
   signal.  "Every smoothed observable" is too broad.

8. **Phase-correction wording: sustained.**  The static amplitude correction
   is \(O(\ell^2/r^2)\); the quoted phase comes from an arrival delay
   \(O(\Omega\ell^2/r)\).  The number is correct, the label was not.

9. **Mean-check statistics: sustained.**  The 660 z-values are strongly
   correlated and under-dispersed, so "none above 3" is not a standalone
   calibration test.  Exact Mecke integration and the independent sampler are
   the meaningful checks; both agree.

10. **\(h\) versus \(\bar h\): sustained.**  The construction must be read as
    the trace-reversed potential for the de Donder argument.  TT is unchanged,
    but non-TT/gauge components depend on this convention.  The exact scope
    above makes it explicit.

The adversarial check's separately listed sound items are confirmed with the
same qualifications: Mecke and transversality are exact; the add-one formula
and joint-link probability bound are correct; AM--GM/Schur closes for the
actual shell-regular weights; the u-slab decorrelation argument is valid for
the truncated dependence regions; and the shell normalization and 1-Gpc
arithmetic reproduce.

## 3. Fixed-reading decision

| Fixed condition | Referee ruling |
|---|---|
| Controlled admixture below \(10^{-3}\) at 1 Gpc | **Met**, for the stated rms potential-amplitude observable and the controlled superpotential source. |
| Mean exactly the linearized-GR retarded solution | **Not met** at finite density; only exact de Donder transversality plus continuum-limit agreement and finite-density corrections are proved. |
| FAIL condition: controlled admixture above \(10^{-3}\) | **Not met.** |

Therefore the only correct fixed-reading verdict is **INCONCLUSIVE**.

The strongest safe statement is:

> The componentwise scalar link construction has an exactly conserved
> ensemble mean and a uniformly controlled, extremely small rms non-TT
> potential-amplitude noise for the smooth source at one Gpc.  Its mean
> converges to the linearized-GR retarded field and differs from it by
> finite-density corrections; it is not exactly that field at finite
> sprinkling density.
