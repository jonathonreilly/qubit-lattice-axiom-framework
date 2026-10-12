# Independent finite positive scalar approximation

Status: mathematical candidate and check, not an empirical inference or an
adopted gravitational completion. This derivation was written independently
of the parent worker's finite-approximation implementation. Units are
`hbar = c = 1`. No source data or fitted physical parameters enter it.

The supplied measure and readout convention are

\[
 \nu(d\mu)=\frac{\ell^s}{\Gamma(s)}\mu^{s-1}e^{-\ell\mu}d\mu,
 \qquad s,\ell>0,
\]

\[
 j(\omega)=\frac1{4\pi^2}\int_0^\omega
 \sqrt{\omega^2-\mu^2}\,e^{-a^2(\omega^2-\mu^2)}\nu(d\mu).
\]

Here `a >= 0`; for the Gaussian spatial source used previously,
`f_a(x)=(2 pi a^2)^(-3/2) exp[-|x|^2/(2a^2)]`, so that the squared Fourier
smearing is `exp[-a^2 |k|^2]`. The convention is
`W_a(t)=integral_0^infinity j(omega) exp[-i omega t] d omega`.

## A finite local candidate

Put `x=ell mu`, `t=r/ell`, and
`rho_s(dx)=x^(s-1) exp(-x) dx/Gamma(s)`. Let `x_i,w_i`, `1 <= i <= N`, be
the generalized Gauss-Laguerre nodes and weights for this **normalized**
measure. Thus `x_i > 0`, `w_i > 0`, `sum_i w_i = 1`, and moments through
degree `2N-1` are exact. The nodes are the zeros of `L_N^(s-1)`.

The finite theory has canonical fields `phi_i`, masses `mu_i=x_i/ell`,
and a source coupling `J sum_i sqrt(w_i) phi_i`:

\[
 \mathcal L_N=\sum_{i=1}^N\frac12
 [\partial_\alpha\phi_i\partial^\alpha\phi_i-\mu_i^2\phi_i^2]
 +J\sum_{i=1}^N\sqrt{w_i}\phi_i.
\]

For two static charges this gives

\[
 V_N(r)=-\frac{g_Ag_B}{4\pi r}Y_N(t),\qquad
 Y_N(t)=\sum_iw_i e^{-t x_i},
\]

\[
 |F_N(r)|=\frac{g_Ag_B}{4\pi r^2}H_N(t),\qquad
 H_N(t)=\sum_iw_i(1+t x_i)e^{-t x_i}
\]

for like-sign charges, with the attractive radial sign understood. The
continuum responses are exactly

\[
 Y(t)=(1+t)^{-s},\qquad
 H(t)=Y(t)-tY'(t)=(1+t)^{-s}\left(1+\frac{s t}{1+t}\right).
\]

This specifies a local finite quadratic field theory and its linear source
interaction. A dynamical matter sector, its cutoff, radiative stability,
and any nonlinear gravitational identification are additional questions.

## Direct quadrature error, including the force sign

The monic Laguerre polynomial
`p_N(x)=(-1)^N N! L_N^(s-1)(x)` has squared norm

\[
 \int p_N(x)^2\rho_s(dx)=N!(s)_N.
\]

Hermite interpolation of a function and its first derivative at every
quadrature node gives the pointwise remainder
`f^(2N)(xi_x) p_N(x)^2/(2N)!`. Integrating is legitimate here because all
derivatives used below are bounded on `[0,infinity)`, and all polynomial
moments exist. Define

\[
 C_N=\frac{N!(s)_N}{(2N)!},\qquad A_N=\frac{(s)_N}{(N-1)!}.
\]

For `t >= 0`,

\[
 0\le Y(t)-Y_N(t)\le C_Nt^{2N},
 \qquad
 |H(t)-H_N(t)|\le(2N-1)C_Nt^{2N}.
 \tag{1}
\]

The force inequality follows from the explicit derivative

\[
 \frac{d^{2N}}{dx^{2N}}[(1+t x)e^{-t x}]
 =t^{2N}[t x-(2N-1)]e^{-t x},
\]

whose absolute supremum divided by `t^(2N)` is `2N-1`.
**The force error has no fixed sign.** At small positive `t`,

\[
 Y-Y_N=C_Nt^{2N}+O(t^{2N+1}),\qquad
 H-H_N=(1-2N)C_Nt^{2N}+O(t^{2N+1});
\]

at sufficiently large `t`, the finite sum is exponentially smaller than
the algebraic continuum response and `H-H_N > 0`. For `s=N=1`, for
example, `H=(1+2t)/(1+t)^2` and `H_N=(1+t)e^-t`.

Equation (1) is useful on modest radial intervals, but is not a useful
large-`N` certificate for every fixed `T > 2`, because
`C_N ~ sqrt(pi) N^(s-1/2)/(Gamma(s) 4^N)`.

## An error bound on every finite radial interval

A separate representation supplies a bound that converges for every
fixed finite `T`. The normalized Laguerre Jacobi matrix is

\[
 J_{nn}=2n+s,\quad J_{n,n+1}=J_{n+1,n}
 =-\sqrt{(n+1)(n+s)},\qquad n=0,1,\ldots.
\]

It is similar to minus the generator of a nonexplosive birth-death chain
with birth rate `lambda_n=n+s`, death rate `delta_n=n`, and reversible
weights `pi_n=(s)_n/n!`. Explicitly, with `D_nn=sqrt(pi_n)`,
`J=-D L D^(-1)`. Its transition probabilities needed here are

\[
 p_{0n}(u)=\frac{(s)_n}{n!}\frac{u^n}{(1+u)^{n+s}},\qquad
 p_{n0}(u)=\frac{u^n}{(1+u)^{n+s}}.
\]

The first formula follows by solving the probability-generating-function
equation, giving `(1+u(1-z))^-s`; the second follows by reversibility.
The spectral measure of `J` at state zero is `rho_s`, hence
`p_00(t)=Y(t)`. The principal `N` by `N` Jacobi truncation has the
Gauss-Laguerre eigenvalues and weights, hence its exponential's `00`
entry is `Y_N(t)`. In the Markov description this is the chain killed
when it first reaches state `N`.

Let `h_N(u)` be its first hitting-time density. It obeys

\[
 h_N(u)=(N-1+s)p^{\rm kill}_{0,N-1}(u)
 \le A_N\frac{u^{N-1}}{(1+u)^{N-1+s}}.
\]

By the strong Markov property,

\[
 E_Y(t):=Y-Y_N=\int_0^t h_N(u)p_{N0}(t-u)du.
 \tag{2}
\]

Consequently an explicit sharper integral bound is

\[
 E_Y(t)\le A_N\int_0^t
 \frac{u^{N-1}(t-u)^N}
 {(1+u)^{N-1+s}(1+t-u)^{N+s}}du.
 \tag{3}
\]

For `u+v=t`,

\[
 \frac{u}{1+u}\frac{v}{1+v}
 \le\left(\frac{t}{t+2}\right)^2.
\]

Writing `q(t)=t/(t+2)` therefore gives the simple uniform certificates,
valid for all `0 <= t <= T < infinity`:

\[
 0\le E_Y(t)\le A_N T q(T)^{2N-2},
 \tag{4}
\]

\[
 |E_H(t)|\le A_NT[1+T(N+sT)]q(T)^{2N-2}.
 \tag{5}
\]

For `N=1`, the exponent-zero factor is one, including at `T=0`; the
whole bound then vanishes at `T=0`. To obtain (5), differentiate (2),
using `p_N0(0)=0`, and integrate
`h_N(u)[p_N0(v)-t p_N0'(v)]`, where

\[
 p'_{N0}(v)=\frac{v^{N-1}(N-sv)}{(1+v)^{N+s+1}}.
\]

Replacing `h_N` by its upper bound and taking the absolute value of the
bracket also gives a sharper one-dimensional integral certificate.
Both (4) and (5) converge exponentially in `N` for every fixed finite
`T`, since `A_N ~ N^s/Gamma(s)` and `q(T)<1`.

Use the minimum of (1) and (4)/(5). Since `Y` and `H` decrease on
`[0,T]`, division by `Y(T)` and `H(T)`, respectively, gives uniform
relative bounds for the potential and force. In particular,
`H'(t)=-t integral x^2 exp(-t x) rho_s(dx) <= 0`.

These certificates describe the exact algebraically defined nodes and
weights. If an implementation uses rounded positive nodes and weights
`x_tilde,w_tilde`, add

\[
 \sum_i|w_i-\widetilde w_i|+T\sum_iw_i|x_i-\widetilde x_i|
\]

to the absolute potential bound, and

\[
 \sum_i|w_i-\widetilde w_i|+\frac{T}{e}\sum_iw_i|x_i-\widetilde x_i|
\]

to the absolute force bound. These follow from the uniform derivative
bounds `|d_x exp(-tx)| <= T` and
`|d_x[(1+tx)exp(-tx)]| <= T/e`. Binary floating-point scans cannot
confirm a theoretical error smaller than their rounding floor. The CDF
noise bounds below apply directly to any positive normalized rounded
measure, using its actual nodes and weights.

No fixed finite `N` approximates the static algebraic tail with a
nontrivial uniform relative error on an unbounded radial interval:
both `Y_N/Y` and `H_N/H` tend to zero as `t -> infinity`.

## Noise: exact thresholds and the limitation near zero

The same finite fields give

\[
 j_N(\omega)=\frac1{4\pi^2}\sum_{\mu_i<\omega}w_i
 \sqrt{\omega^2-\mu_i^2}\,e^{-a^2(\omega^2-\mu_i^2)}.
 \tag{6}
\]

The continuum has a strictly positive spectrum for every `omega > 0`
and the low-frequency expansion

\[
 j(\omega)\sim
 \frac{\ell^s B(s/2,3/2)}{8\pi^2\Gamma(s)}\omega^{s+1}.
 \tag{7}
\]

This follows by setting `mu=omega z`; the remaining leading integral
is `integral_0^1 z^(s-1) sqrt(1-z^2) dz = B(s/2,3/2)/2`.
But `j_N=0` throughout `0 < omega < mu_min=x_1/ell`. Its relative error
there is **exactly one**, independently of the static accuracy.
Thus no finite `N` achieves uniform relative noise error less than one
on `(0,Omega]`. A necessary condition on a closed measured band
`[omega_lo,Omega]` for such accuracy is strictly
`mu_min < omega_lo`; equality also gives zero at the lower endpoint.

Every finite-mode onset contributes

\[
 \frac{w_i}{4\pi^2}\sqrt{2\mu_i(\omega-\mu_i)}
 [1+O(\omega-\mu_i)].
\]

The threshold integrand as a function of mass is not `2N` times
differentiable. Applying the analytic static Gauss remainder to this
noise integral would be invalid.

The missed integrated power in a low-frequency interval has the much
smaller absolute scale `const * omega_c^(s+2)/(s+2)` as
`omega_c -> 0`. Relative failure alone does not imply a detectable
experimental discrepancy.

## Joint bounds on windows bounded away from zero frequency

Let `F(mu)=P(s,ell mu)` be the gamma CDF and
`F_N(mu)=sum_{mu_i <= mu} w_i`. Their Kolmogorov discrepancy is explicitly

\[
 \delta_N=\max_i\left\{
 \left|F(\mu_i)-\sum_{j<i}w_j\right|,
 \left|F(\mu_i)-\sum_{j\le i}w_j\right|\right\}.
 \tag{8}
\]

There is no optimization over an unknown continuum variable in (8):
between adjacent atoms, the CDF difference is increasing, so extrema
occur at the two sides of jumps. For any continuous function of bounded
variation that vanishes at infinity, integration by parts gives

\[
 \left|\int f\,d(\nu-\nu_N)\right|\le\delta_N\operatorname{Var}(f).
\]

For the noise integrand, the exact total variation in the mass variable is

\[
 V_a(\omega)=
 \begin{cases}
 \omega,&a=0,\\
 \omega e^{-a^2\omega^2},&0<\omega\le1/(\sqrt2a),\\
 2/(a\sqrt{2e})-\omega e^{-a^2\omega^2},&\omega>1/(\sqrt2a).
 \end{cases}
\]

Therefore

\[
 |j-j_N|(\omega)\le\frac{\delta_N V_a(\omega)}{4\pi^2}.
 \tag{9}
\]

`V_a` is nondecreasing, so replacing its argument by `Omega` yields a
uniform absolute bound for `[0,Omega]`. A sharper, computable bound
uses the actual CDF difference rather than its supremum:

\[
 |j-j_N|(\omega)\le\frac1{4\pi^2}\int_0^\omega
 |F(\sqrt{\omega^2-k^2})-F_N(\sqrt{\omega^2-k^2})|
 e^{-a^2k^2}|1-2a^2k^2|\,dk.
 \tag{10}
\]

Without the two absolute-value signs inside the integral, its value is
exactly `j-j_N`. The integral is divided at the known mode thresholds;
this removes square-root endpoint singularities from the measure form.

For `0 < omega_lo <= omega <= Omega`, a simple positive lower bound is

\[
 j(\omega)\ge
 \frac{\sqrt3\,\omega_{\rm lo}}{8\pi^2}
 e^{-a^2\Omega^2}F(\omega_{\rm lo}/2).
 \tag{11}
\]

It follows by keeping only masses up to `omega_lo/2`. Combining (9)
and (11) yields the sufficient uniform relative certificate

\[
 \frac{|j-j_N|}{j}\le
 \frac{2\delta_N V_a(\Omega)e^{a^2\Omega^2}}
 {\sqrt3\,\omega_{\rm lo}F(\omega_{\rm lo}/2)}.
 \tag{12}
\]

This certificate can be conservative, particularly for a wide frequency
band or a very small `omega_lo`. Equation (10), frequency bins, or a
stronger readout-specific lower bound can be much sharper; no claim that
(12) is an efficient way to choose `N` is intended.

For completeness, `delta_N -> 0`. Exact moments give tightness; for any
fixed moment, a higher exact moment supplies uniform integrability.
Every subsequential weak limit consequently has all gamma moments.
These determine the measure: their Carleman sum diverges because
`[(s)_(2n)]^(-1/(2n)) ~ e/(2n)`. The limit CDF is continuous, so weak
convergence implies uniform convergence of CDFs. This proves simultaneous
approximation to arbitrary positive static and noise tolerances on any
fixed finite radial window and any compact frequency band with
`omega_lo > 0`. It does not give relative convergence down to zero.

## What would falsify the chosen finite candidate

* A calibrated positive signal attributable to this coupled vacuum sector
  below its specified `mu_min` contradicts (6), conditional on the source,
  vacuum, linear coupling, and readout premises.
* At a resolved threshold, the finite candidate predicts square-root
  onsets with the stated positive weights. A smooth continuum fit by
  itself does not establish that the thresholds are absent at finer
  resolution.
* Static agreement on a finite interval leaves the low-frequency gap
  unconstrained without a joint readout. Extending measurements to much
  larger distances eventually tests the finite exponential tail.

The relevant experimental alternatives include backgrounds and source or
readout errors. None of these conditional falsifiers is a claim about
gravity in general, nor is an unmeasured gap evidence against the model.

## Reproduction and numerical checks

The independent checker and numerical receipt accompany this note. Its
analytic certificates are (1), (4), (5), (9), and (12). Floating-point
quadrature values and sampled errors are numerical checks, not interval
arithmetic proofs of their last printed digits.

See `RESULTS.md` for concrete windows and the distinction between a
70-digit endpoint calculation and a uniform analytic certificate.
