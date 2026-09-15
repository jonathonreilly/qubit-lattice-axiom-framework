# A positive dynamics that keeps the magnetic carrier

Personal derivation, 2026-09-15. Provisional research; no independent review,
full-field limit, native law, or axiom amendment is claimed.

## Exact starting measure

Use the finite free-cube smoothing identity on main
6ad6a2184b7c2067e597528e0964753874493b4a, with D=d1, B=d2,
P the orthogonal projection onto im D, h=2pi sqrt(beta), and
K=(I+tau DD*)^-1. Write A=K^-1. The actual filtered field has law

    pi(dz)=Z^-1 exp[-S(z)] m_C(dz),
    S(z)=z.Az/2 - V_e(z),
    C=im D + h Z^faces.

The measure m_C is counting measure on the discrete quotient of C by im D,
times Euclidean Lebesgue measure on each exact affine fiber. Uniform
normalizing constants cancel. The proven electric extension V_e is real,
even, smooth through order three, and periodic under every z -> z+h n,
n an integer face field. Its real Hessian and third derivative are small
in the stated large fixed-N parameter range. The discrete magnetic
condition Bz in h B Z^faces is retained.

For the specific construction tau=1/64, but the identities below hold
at any fixed tau>0 for which this exact periodic extension is used.
The sign of h Z is immaterial because the integer group is symmetric.

## A candidate reversible generator

For each oriented face p put v_p=h e_p. Define

    c_p^+(z)=exp[-(S(z+v_p)-S(z))/2],
    c_p^-(z)=exp[-(S(z-v_p)-S(z))/2].

Periodicity removes V_e from these differences exactly:

    c_p^+(z)=exp[-v_p.Az/2-v_p.Av_p/4],
    c_p^-(z)=exp[+v_p.Az/2-v_p.Av_p/4].                 (1)

The formal generator on smooth test functions on the fibers is

    L f = tr(P Hess f) - (P grad S).grad f
        + sum_p [c_p^+(z)(f(z+v_p)-f(z))
                 +c_p^-(z)(f(z-v_p)-f(z))].           (2)

All moves preserve C. The diffusion acts only within a magnetic fiber;
the jumps change Bz by +/-h B e_p and connect the magnetic quotient.
This is an auxiliary proof dynamics, not a selected physical clock.

Fiber integration by parts gives the diffusion Dirichlet form. Translation
invariance of m_C and the exact balance identity

    exp[-S(z)]c_p^+(z)=exp[-S(z+v_p)]c_p^-(z+v_p)       (3)

give the jump form. Thus, wherever the integrations are justified,

    -<f,Lg>_pi = E_pi [(P grad f).(P grad g)]
      + (1/2) sum_(p,sigma) E_pi[c_p^sigma
                    (f(z+sigma v_p)-f(z))
                    (g(z+sigma v_p)-g(z))].            (4)

This establishes algebraic reversibility on a test-function core. The
finite conservative realization is supplied below. A volume-uniform
mixing or parameter-response theorem remains open.

## A uniform bound on stationary jump intensity

The original centered clock flux X has E exp(t.X)<=exp(||t||^2/2).
The exact coupling z=K(X+sqrt(beta)D xi), with independent edge Gaussian
xi of covariance s^2 I and tau=beta s^2, gives

    E_pi exp(t.z) <= exp(t.Kt/2).                       (5)

Indeed K^2+tau K DD* K=K. Apply (5) to t=+/-Av_p/2 in (1):

    E_pi c_p^+ , E_pi c_p^- <= exp[-v_p.Av_p/8].        (6)

This is independent of volume and uses the centered law only. On a free
cubic face D has four signed boundary edges, so (DD*)_pp=4, including
boundary faces. Consequently

    E_pi(c_p^+ + c_p^-)
      <= 2 exp[-pi^2 beta(1+4tau)/2].                  (7)

The expected total jump intensity in a finite box is finite, bounded
by its number of faces times (7). This is not a mixing bound.

## Finite-volume nonexplosion, without a uniform response claim

The drift in (2) is globally Lipschitz on each fiber, since Hess V_e is
bounded. The jump rates are locally bounded and smooth. Construct the
diffusion and jump clocks up to exits from bounded sets by the usual
finite-dimensional SDE and thinning construction. For W(z)=1+z.Az,

    L_cont W=2 tr(PA)-2|PAz|^2+2(PAz).(P grad V_e)
             <=2 tr(PA)+|P grad V_e|^2.

The last quantity is bounded by a finite constant proportional to the
number of faces, using the uniform per-coordinate first derivative bound.
For one paired jump direction put x=v.Az and q=v.Av>0. Its contribution is

    2 exp(-q/4)[q cosh(x/2)-2x sinh(x/2)].             (9)

This is bounded above for all real x. Explicitly, if R=max(q,2), then
for |x|>=R one has tanh(|x|/2)>=1/2, so the bracket is nonpositive;
inside that interval it is at most q cosh(R/2). Therefore LW<=C times
the number of faces, with a finite parameter-dependent C. Stopped Dynkin
estimates and W>=1+|z|^2 rule out escape to infinity in finite time.
Inside any bounded set the finite total jump rate rules out accumulation
of jump times. Thus the finite-dimensional construction is conservative.

The integration-by-parts identities, applied first to compactly supported
core functions and then localized, identify the invariant reversible
probability pi. Equivalently its symmetric Dirichlet form has the above
conservative realization. No volume-independent convergence rate follows
from this Lyapunov estimate: its upper constant scales with volume and
can grow rapidly with beta. No infinite-volume process has yet been constructed.

## Diffuse-source jump remainder

For a real face test t, apply the jump part of (2) to exp(i t.z) and
divide by that exponential. Its linear and quadratic terms are

    i sum_p (t.v_p)(c_p^+-c_p^-)
       - (1/2) sum_p (t.v_p)^2(c_p^++c_p^-).

The real-argument Taylor remainder |exp(iu)-1-iu+u^2/2|<=|u|^3/6
and (6) give the expectation bound

    E_pi |R_jump(t,z)|
      <= (h^3/3) exp[-pi^2 beta(1+4tau)/2] ||t||_3^3. (8)

For four-dimensional smooth tests t_a(p)=a^2 f_p(a x),
||t_a||_3^3=O(a^2). Therefore this generator's microscopic jump
Taylor remainder vanishes at macroscopic scaling, with N and beta fixed.
This is a statement about the generator expression, not about the third
cumulant of the stationary field.

## Exact residual and next discriminator

The potential advantage of (2) is that it keeps a positive law and the
actual quantized support, while placing the electric correction in a small
continuous drift perturbation. No mixed electric/magnetic complex weights
have been interpreted as probabilities. The rare jumps remain present.

The stationary equation E_pi L exp(i t.z)=0 still contains nonlinear drift
correlations and the random quadratic jump intensity. Bound (8) does not
control either term, prove ergodicity, or imply a Gaussian stationary law.
In fact the diffusion and jump parts are separately invariant under pi;
their zero stationary expectations cannot be treated as two independent
constraints that by themselves determine pi. Discarding the jumps leaves
every magnetic fiber invariant and loses control of the mixture of fibers.
The missing theorem is a uniform response/homogenization estimate for this
specific hybrid generator (or a different exact reversible dynamics).
As a bare assumption that theorem is comparable to the original target;
the generator is a possible mechanism for proving it, not a completed
reduction that moves the target near closure.

Next examine the mixed diffusion/jump coupling rather than infer contraction
from convexity of S. Even a convex extension does not automatically supply
convexity inequalities for a constrained discrete measure. First verify (1),
(3), (5)-(8) by direct finite source/density calculations, then test a proposed
coupling or Dirichlet estimate on actual magnetic fibers. If it fails, preserve
the concrete failure and try a materially different estimate.

## Finite source challenge

`../evidence/block1_hybrid_generator_check.py` enumerates 32, 243 and 1024
tree-gauge clock configurations on a free three-cube for (N,beta) equal to
(2,.25), (3,.5), (4,.8). It sums image integers separately and uses the exact
Gaussian convolution to compute the filtered complex source. This route
does not evaluate the proposed electric potential or its derivatives.

The carrier translation identity independently predicts

    M(t-Av)=exp[v.Av/2-t.v] M(t),                      (10)

for the actual filtered moment function. Direct source sums verify (10),
the separate stationary jump identity, all six per-face rate bounds and
the integrated absolute Taylor bounds at four source amplitudes. Maximum
relative error in (10) was 1.268e-14; image cutoffs 8 and 10 agreed to
floating precision. The cutoff comparison is not an interval certificate.
These finite parameters challenge algebra and normalization, not the
large-parameter all-volume phase theorem. The analytic potential-existence
hypotheses and the open response bound remain separate.
