# State of attack

- **Discharged:** an explicit separated near/far pair for the convolution in
  Lemma FB, with a positive lower bound proved below by Taylor's formula.
- **Discharged:** a uniform finite-regulator bound `2^53 L^-4` on the fibre
  correction, by enlarging the conditioning space to all coarse links.
- **Discharged:** the joint finite-regulator limit at fixed `L`, and
  `a_L>=a_0>0` for all sufficiently large admissible odd `L`, for (B-1)'s
  Gaussian fibre over closed coarse currents. Explicit constants are below.
- **Implication only:** Corollary NT1-F still needs its nonlinear producer,
  support, reconstruction, and scale hypotheses. None is supplied here.

Author work at `39189b75b33ade215b3b379c467674b4973d17ff`, 2026-11-01.
This is a neutral mathematical calculation for the explicit linear map
(B-1), not a review, audit, or claim about the nonlinear Wilson measure.
No numerical or symbolic-computation job was run. The numerical tables supply
no premise. Only this file is an output.

## 1. Scope and first attempts to refute the proposed argument

**Discharged (source check).** The inputs are section 4 and Corollary NT1-F
of `nt2-flat-fibre-criterion.md`, (B-1)--(B-5) of
`witness-blocked-tree-limit.md`, and Corollary 4.2 of `parts/witness.md`
(lines 668--672 at this revision). Corollary 4.2 evaluates the *point*
Maxwell kernel at `(d,d,2d,2d)` and `(d,d,2d,3d)`; it assumes the required
accuracy for the actual correlators. Its later qualification at lines
1153--1156 explicitly leaves the blocked far-field approximation open.
It therefore does not already bound the convolution remainder.

**Discharged (hand kill tests).** A cheap way to refute the proposed
geometry would be to find that its far point is not a zero of `M`, or
that its offsets do not differ solely in positive time. For

    z_n = (2d,2d,2d,d),       z_f = (2d,2d,2d,2d),

both tests pass: `z_f-z_n=d e_4`, and `|z_f|^2=2(z_f,1^2+z_f,2^2)`.
Another possible failure is a divergent alias sum in the proposed
full-link conditioning bound. That test is addressed explicitly below;
positive semidefiniteness alone would give no decay in `L`.

**Implication (model boundary).** Throughout, `P` is the normalized free
covariance with the factor `4` stripped off, as in (B-3). The conditioning
space for `P^fib` is the closed span of pulled-back *closed coarse currents*,
exactly the space specified in section 4 of the criterion note. Identification
of this Gaussian fibre with the nonlinear chart in (FT) remains that
corollary's separate hypothesis.

## 2. Explicit convolution estimate

**Discharged (mass, support, moments).** Write `b=1_[-1/2,1/2]`,
`T_k=b^(*k)`, and

    R(w)=T_4(w_1)T_4(w_2)T_2(w_3)T_2(w_4).

Iterating the convolution integral shows that each `T_k` is a nonnegative
unit-mass density, supported in `[-k/2,k/2]`, with mean zero. Also
`int t^2 b(t)dt=1/12`. Expanding the square of a sum in each convolution
and using the zero means gives `int t^2 T_k(t)dt=k/12`. Consequently

    int R=1,     int w R(w)dw=0,
    supp R subset [-2,2]^2 x [-1,1]^2,
    |w|<=sqrt(10)<4 on supp R,     int |w|^2 R(w)dw=1.       (H1)

**Discharged (derivative bound).** Let
`A=diag(-1,-1,1,1)`, `r=|x|`, and `t=x^T A x`. The kernel of Lemma FB is

    M(x)=t/(pi^2 r^6).

Since `|t|<=r^2` and `|Ax|=r`, direct differentiation gives

    pi^2 Hess M
      =2 A r^-6 -12[(Ax)x^T+x(Ax)^T]r^-8
        -6t I r^-8 +48t xx^T r^-10.

Each outer product `uv^T` has operator norm `|u||v|`: this follows by
applying Cauchy--Schwarz to `uv^T h`, with equality when `h` is parallel
to `v`. Thus

    ||Hess M(x)|| <= (2+24+6+48)/(pi^2 r^6)
                  =80/(pi^2 r^6).                         (H2)

For `|z|>4`, apply twice the fundamental theorem of calculus to
`s -> M(z-sw)`. Its integral remainder is
`int_0^1 (1-s) w^T Hess M(z-sw) w ds`. Integrating against `R`, the
linear term vanishes by (H1), and therefore

    |P_infinity(z)-M(z)| <= 40/[pi^2 (|z|-4)^6].            (H3)

This argument never evaluates the singular kernel at zero.

**Discharged (strict difference).** Fix an integer `d>=64`. At the above
two offsets,

    M(z_n)=-mu,    M(z_f)=0,
    mu:=3/(13^3 pi^2 d^4)>0.                              (H4)

Indeed `|z_n|^2=13d^2` and `t(z_n)=-3d^2`. Both offsets have norm at
least `3d`, so `|z|-4>=2d` for `d>=4`. Formula (H3) is then at most
`5/(8 pi^2 d^6)`. This is at most `mu/4`, because

    5*13^3 = 10985 < 24576 = 6*64^2 <= 6d^2.

Hence

    |P_infinity(z_n)| >= 3mu/4,
    |P_infinity(z_f)| <= mu/4,
    |P_infinity(z_n)|^2-|P_infinity(z_f)|^2 >= mu^2/2.      (H5)

Every constant here is independent of `L`. The density and kernel in the
question are the only premises of this calculation.

## 3. The finite-regulator fibre estimate

**Discharged (projection comparison).** Work first in the finite Gaussian
of (B-3). Its covariance defines an inner product on linear functionals
after null vectors are quotiented out. Let `H_cl` be the span of the
pulled-back closed coarse currents, and `H_all` the span of all pulled-back
coarse links, with orthogonal projections `Pi_cl` and `Pi_all`. Then
`H_cl subset H_all`. Decomposing a vector first along `H_all` and then
along `H_cl` proves

    ||Pi_cl f||^2 <= ||Pi_all f||^2.

The Schur correction specified in the question is
`delta_pq=<Pi_cl f_p,Pi_cl f_q>`. Therefore

    |delta_pq| <= sqrt(delta_pp delta_qq),
    delta_pp <= ||Pi_all f_p||^2.                         (H6)

Here Cauchy--Schwarz follows by expanding
`||u-t v||^2>=0` and minimizing over the complex scalar `t` (the zero
vector case is immediate). Thus no lower bound on the *closed-current*
Gram matrix is needed for the decay estimate.

**Discharged (alias formulas).** Take positive odd `n,L`, fine torus side `nLU`,
level-j torus side `S=LU`, and coarse torus side `U`, an integer. Set
`N=nL`. To fix every normalization, the multipliers of (B-2) are

    s_n(u)=sin(u/2)/[n sin(u/(2n))],
    a_(n,mu)(p)=exp[-i(1-1/n)p_mu/2] s_n(p_mu) prod_nu s_n(p_nu),
    lambda_n(p)=4n^2 sum_nu sin^2(p_nu/(2n)).

Continuous values are used at zero. The limiting multipliers replace
`s_n(u)` by `s(u)=2sin(u/2)/u`, and the phase by `exp(-ip_mu/2)`.
For a unit plaquette at
`x`, write `j_(n,x,mu)(p)=a_(n,mu)(p) Jhat_(x,mu)(p)`.
Only `mu=1,2` occur. The nonzero components of `Jhat_x` are, up to signs
and translation phase, `1-exp(-ip_2)` and `1-exp(-ip_1)`. Since
`1-exp(-it)=int_0^t i exp(-is)ds`, (B-5) gives

    |j_(n,x,mu)(p)| <= |p|                               (H7)

on the scaled fine zone, uniformly in `x` and `n`.

Here the bounds (B-5) can themselves be checked by hand: for odd `n`,
`s_n(u)=n^-1 sum_(r=-(n-1)/2)^((n-1)/2) exp(iru/n)`, so its modulus is
at most one. The sine chord inequality on `[0,pi/2]` gives
`n|sin(u/(2n))|>=|u|/pi` on `|u|<=pi n`; bounding the numerator by one
gives `|s_n(u)|<=pi/|u|`. Squaring that same chord inequality in the
four terms of `lambda_n` gives `lambda_n(p)>=(4/pi^2)|p|^2`.

Put `theta in [-pi,pi)^4`, `k_m=theta+2pi m`. In the finite formula retain
only the aliases with `k_m in [-pi N,pi N)^4`. Exact composition of (B-1)
gives the coarse-link pullback multiplier `L a_(N,mu)(Lp)`, in the
level-j momentum variable `p`. This also follows directly: its fine
multiplier is `nL a_(nL,mu)(nL k)`, and (B-3) factors out `n`.
Moreover

    lambda_n(k_m/L)=L^-2 lambda_N(k_m).

The alias decomposition `Lp=theta+2pi m` of the fine momentum grid has
`theta in (2pi/U) Z^4`. Its normalized counting measure is
`L^-4 U^-4` before summing aliases: the total covariance in (B-3) is
`(LU)^-4 sum_(p!=0) sum_mu conj(j_p,mu) j_q,mu/lambda_n(p)`.
Consequently the full-link Gram matrix
is diagonal, with entries

    G_(N,mu)(theta)=sum_m |a_(N,mu)(k_m)|^2/lambda_N(k_m),
    h_(n,L,x,mu)(theta)
      =L^-1 sum_m conj(a_(N,mu)(k_m))
                        j_(n,x,mu)(k_m/L)/lambda_N(k_m).  (H8)

For example the coarse-coarse product contributes `L^2` from its two
currents and `L^2` from the inverse Laplacian, canceling `L^-4`; the
coarse-fine product contributes just `L`, leaving `L^-1` after the
inverse Laplacian. Pairing a coarse Fourier coefficient `v(theta)` with
the fine plaquette gives `U^-4 sum_theta v(theta)^* h_x(theta)`.
Minimizing its squared residual separately in each component yields

    ||Pi_all f_x||^2
      =U^-4 sum_(theta!=0) sum_mu |h_(n,L,x,mu)(theta)|^2
                                               /G_(N,mu)(theta). (H9)

At `theta=0`, every nonzero alias has a vanishing sinc factor; the zero
alias is the removed fine zero mode. Thus `G=h=0` there, and its
contribution is defined to be zero. This is also why no harmonic
coarse-link ambiguity affects (H9).

**Discharged (inverse bound).** The zero alias at `theta!=0` gives

    G_(N,mu)(theta) >= (2/pi)^10 |theta|^-2
                    >= 2^-10 |theta|^-2.                 (H10)

To verify this without a numerical constant: on `|u|<=pi`, concavity
of sine on `[0,pi/2]` gives `s(u)>=2/pi`, and
`N sin(|u|/(2N))<=|u|/2` gives `s_N(u)>=s(u)`.
There are five sinc factors in `a_(N,mu)`. Also
`lambda_N(theta)<=|theta|^2`. The inequalities `2<pi<4` follow, for
example, from `pi=4 int_0^1 (1+t^2)^-1 dt` by bounding its integrand
between `1/2` and `1`.

**Discharged (the summable alias bound).** Define
`u(0)=1`, `u(m)=1/|m|` for nonzero integers. For a retained alias,
`|theta_nu+2pi m_nu|>=pi |m_nu|` if `m_nu!=0`.
Thus (B-5) gives

    |a_(N,mu)(k_m)| <= u(m_mu)^2 prod_(nu!=mu) u(m_nu).

For `m!=0`, also `|k_m|>=max_nu |m_nu|`. The following bound therefore
holds uniformly in `N` and `theta!=0`:

    sum_m |a_(N,mu)(k_m)|/|k_m|
       <= |theta|^-1 + 2^15.                             (H11)

Here are the summation details. On the shell
`2^j<=max|m_nu|<2^(j+1)`, replace `1/|k_m|` by `2^-j` and enlarge the
remaining sum to the coordinate cube of radius `2^(j+1)`. Integral
comparison of the decreasing functions `t^-2` and `t^-1` gives

    sum_(|m|<=M) u(m)^2 <= 1+2(1+int_1^infinity t^-2 dt)=5,
    sum_(|m|<=2^(j+1)) u(m)
       <= 1+2[1+(j+1)log 2] <= 5(j+1).

The shell is at most `625 (j+1)^3 2^-j`. To check its sum by hand, put
`S_r=sum_(j>=0) j^r 2^-j` for `r=0,1,2,3` (with `0^0=1` in `S_0`).
The geometric sum gives `S_0=2`; shifting the index gives
`S_1=2`, `S_2=6`, `S_3=26`. Indeed the three equations are
`S_1=(S_1+S_0)/2`, `S_2=(S_2+2S_1+S_0)/2`, and
`S_3=(S_3+3S_2+3S_1+S_0)/2`.
Thus `sum (j+1)^3 2^-j=26+18+6+2=52`, and the nonzero aliases sum to
at most `625*52=32500<32768=2^15`. Convergence needed in these index
shifts can itself be checked by
`(j+1)^3<=6 binom(j+3,3)` and
`sum binom(j+3,3)2^-j=(sum 2^-j)^4=16`, obtained by multiplying four
nonnegative geometric series. This is a written bound, not enumeration.

**Discharged (uniform fibre correction).** By (B-5),
`lambda_N(k)^-1 <= (pi^2/4)|k|^-2 <=4|k|^-2`.
Using (H7) in (H8), then (H11), gives

    |h_(n,L,x,mu)(theta)|
       <=4 L^-2 (|theta|^-1+2^15).

Since `|theta|<=2pi<8`,
`|theta| |h_mu| <=4 L^-2(1+2^18)<2^21 L^-2`.
By (H10), each nonzero component contributes at most `2^52 L^-4`
to (H9). There are only two such components, and `U^-4` times the
number of coarse momenta is one. Equations (H6)--(H9) prove

    0 <= delta_xx <= C L^-4,
    |P^inf_(n,LU)(p,q)-P^fib_(n,LU;L)(p,q)| <= C L^-4,
    C:=2^53.                                             (H12)

This holds for every position of a unit `(1,2)` plaquette and all the
finite regulators just specified. In particular it includes block faces
and corners. There is no edge logarithm in this upper bound. It proves
the requested exponent `kappa=2` for this Gaussian map; it proves no
nonlinear lift estimate.

## 4. The limit previously labelled unchecked

**Discharged (closed-current matrix).** Put
`r_mu(theta)=1-exp(-i theta_mu)`, treating `r` as a row. A closed current
has Fourier vector `v` with `r v=0`. For `theta!=0` these vectors are
exactly the span of the plaquette vectors
`r_nu e_mu-r_mu e_nu`: choose an index `nu` with `r_nu!=0` and write
`v=sum_(mu!=nu) (v_mu/r_nu)(r_nu e_mu-r_mu e_nu)`.
On a finite torus, one can choose the coefficients independently at
each momentum: the geometric-sum identity
`U^-1 sum_(y=0)^(U-1) exp(2pi i k y/U)=1_(k=0 mod U)`, multiplied in
four coordinates, verifies Fourier inversion directly. Thus the
closed-current correction is

    delta_(n,U;L)(p,q)=U^-4 sum_(theta!=0) h_p(theta)^*
                                           K_N(theta) h_q(theta),
    K_N=G_N^-1-G_N^-1 r^* (r G_N^-1 r^*)^-1 r G_N^-1,     (H13)

where `G_N` is the diagonal matrix in (H8). To derive the formula, set
`y=G_N^(1/2) v`. The constraint becomes orthogonality of `y` to
`G_N^(-1/2) r^*`. Subtract the projection onto this one-dimensional
vector from the identity, and conjugate by `G_N^(-1/2)`.
This proves both (H13) and

    0 <= K_N <= G_N^-1,       K_N G_N K_N=K_N.             (H14)

The denominator in (H13) is strictly positive for `theta!=0` by
positivity of `G_N`. No unquantified spectral assertion about a
three-by-three matrix is being used.

**Discharged (normalization check at `L=1`).** In this case
`Jhat_x(theta+2pi m)=Jhat_x(theta)` and (H8) gives
`h_x=G_n Jhat_x`. Since `r Jhat_x=0`, formula (H13) gives
`K_n h_x=Jhat_x`. Thus `delta=P^inf` and `P^fib=0`, as required when
the supposedly coarse currents already include every observed plaquette.
This is an algebraic check, not a numerical test.

**Discharged (convergence away from zero).** Define continuum aliases by
replacing `a_N` by `a`, `lambda_N(k)` by `|k|^2`, and
`j_(n,x)` by `j_x=a Jhat_x` in (H8), and summing all `m in Z^4`.
Call the resulting quantities `G`, `h_(L,x)`, and `K`. On any compact
subset of the theta torus excluding zero, these sums converge uniformly,
as do their finite-regulator versions as `n -> infinity` at fixed `L`.
These are periodic theta functions: relabel the aliases after a shift
by `2pi` in a coordinate. At a finite-zone boundary, the multipliers
have period `2pi N` (respectively `2pi n` for the fine current), since
`s_N(u+2pi N)=s_N(u)` and the phase gains
`exp[-i pi(N-1)]=1` for odd `N`. Thus this relabelling is valid there
as well as for the infinite sums.
Here is the required tail argument, in addition to (B-5):

1. For `h`, the absolute tail is bounded by the tail of the convergent
   shell sum used in (H11), multiplied by `4L^-2`. This is uniform in
   `theta` and `n` for all nonzero aliases.
2. For `G`, each nonzero-alias term is at most
   `4 prod_nu u(m_nu)^2`, since `|k_m|>=1` and
   `u(m_mu)^4<=u(m_mu)^2`. The product sum is at most `4*5^4`.
   Its tail outside a coordinate cube tends to zero: split into four
   coordinate tails, and use
   `sum_(|m|>M) u(m)^2 <= 2/M` and `sum u(m)^2<=5`.
3. On a finite alias set, `s_N(u)->s(u)`, the phases converge,
   `lambda_N(u)->|u|^2`, and `j_(n,x)(u/L)->j_x(u/L)` uniformly on
   the compact set. For example `sin t/t->1` follows by integrating
   `cos t` between `cos |t|` and `1`. Denominators there stay away
   from zero. Every fixed alias is retained once `n` is large.

The zero-alias lower bound (H10) passes to `G`. Inversion of a diagonal
matrix is continuous when its entries are positive. The scalar
`r G^-1 r^*` is positive away from zero, so compactness also bounds it
away from zero on each of these compact sets. Formula (H13) therefore
converges uniformly there. The summand is bounded everywhere by

    |h_p^* K_N h_q| <= C L^-4,                            (H15)

by (H9)--(H12), (H14), and Cauchy--Schwarz for a positive matrix.
The same bound holds for its limit.

**Discharged (joint momentum-grid limit).** Write
`dtheta=(2pi)^-4 d^4 theta`. Outside the cube
`max|theta_mu|<epsilon`, the uniform convergence just proved, followed
by the Riemann-sum limit of a continuous periodic function, gives
convergence as `n,U -> infinity` independently. For completeness, on a
compact set uniform continuity bounds the oscillation in each grid cell
by its modulus of continuity at cell diameter `4pi/U`; summing cell
volumes proves that Riemann limit. Cells meeting the boundary of the
removed cube have total volume tending to zero and a bounded integrand.
Inside the cube, (H15) bounds the integral by
`C L^-4 (epsilon/pi)^4`. The grid has at most
`(1+epsilon U/pi)^4` points there, so its normalized contribution is
at most `C L^-4 (1/U+epsilon/pi)^4`. First let `n,U -> infinity`,
then `epsilon ->0`. This proves

    delta_(n,U;L)(p,q) -> delta_L(p,q)
       := int h_(L,p)^* K h_(L,q) dtheta,
    |delta_L(p,q)| <= C L^-4.                             (H16)

All limits in this paragraph are at fixed odd `L` and fixed plaquettes.
The proof handles a joint limit, not only an iterated one.

**Discharged (identification with the infinite closed span).** The
continuum covariance inner product is
`<f,g>=int_(R^4) sum_mu conj(f_mu(p))g_mu(p) |p|^-2 dp/(2pi)^4`.
Alias decomposition for coarse currents gives exactly `G,h` above.
The pointwise projected coefficient is `c=K h_x`; it satisfies `r c=0`
and `c^*G c=h_x^*K h_x`, whose integral is finite by (H15).
To check that it lies in the closure of *finite* closed coarse currents,
first multiply by a continuous periodic cutoff `chi` vanishing near
zero. Then

    chi c = sum_(mu<nu) b_(mu,nu)(r_nu e_mu-r_mu e_nu),
    b_(mu,nu)
      =chi (conj(r_nu)c_mu-conj(r_mu)c_nu)/sum_alpha |r_alpha|^2.

The identity follows by taking component `mu` and using `r c=0`.
Each `b` is continuous on the torus, extended by zero near zero.
It can be uniformly approximated by trigonometric polynomials as
follows. In one coordinate the kernel
`F_m(t)=|sum_(j=0)^m exp(ijt)|^2/(m+1)` is nonnegative and has normalized
integral one, by integrating its finite Fourier expansion. For
`eta<=|t|<=pi` it is at most
`[(m+1)sin^2(eta/2)]^-1`, by summing the geometric series.
Convolution with the product of these four kernels is a trigonometric
polynomial. Its uniform approximation error tends to zero: uniform
continuity controls translations smaller than `eta`, and the union
bound in four coordinates makes the remaining kernel mass tend to zero.

The coefficient approximations converge in the `G` norm as well.
Indeed the tail bound above gives
`G_mu(theta)<=4|theta|^-2+4*5^4`. This is integrable in four dimensions:
on the shells `2^(-j-1)<max|theta_mu|<=2^-j`, its singular part has
integral bounded by a constant times `2^(-2j)`, a geometric series.
The plaquette vectors are bounded, so uniform coefficient error tends
to zero in this norm. The approximants are Fourier transforms of finite
linear combinations of translated plaquettes. Finally remove the cutoff;
the squared norm removed is at most `C L^-4` times the volume near zero,
by (H15). This proves the claimed closed-span membership. The residual
is orthogonal to it: the formula for `K` makes `h_x-G c` proportional
to `r^*`, which pairs to zero with every vector satisfying `r v=0`.
Thus (H16) is also the infinite-space Gaussian projection correction.

**Discharged (fibre limit).** Combine (H16) with the total covariance
limit (B-4), taking `S=LU`. Alternatively its proof applies directly:
the integrand is bounded at zero by (H7) and (B-5); outside a fixed
cube it is bounded by an integrable product
`C prod_nu (1+|p_nu|)^-2`; the integral and grid tails tend to zero by
one-dimensional integral comparison; and on the intervening compact
annulus the multipliers converge uniformly. A small cube at zero has
contribution bounded by a constant times `(epsilon+2pi/S)^4`.
These are precisely the tail, compact, and small-cube estimates needed
for the joint `n,S -> infinity` limit, with no computed values. Hence

    P^fib_(n,LU;L)(p,q) -> P^fib_(infinity;L)(p,q)
       =P_infinity(q-p)-delta_L(p,q).                     (H17)

This discharges the previously unchecked limit for the explicit map,
regulator, and conditioning space stated here. It does not identify a
different regulator or a nonlinear gauge chart with this one.

## 5. Positive free value and the order of constants

**Discharged (free lower bound).** With `mu` from (H4), set

    a_0:=3mu^2/16,
    L_split:=(8*2^53/mu)^(1/4).                           (H18)

For every admissible odd `L>=L_split`, (H16) gives
`|delta_L(p,q)|<=mu/8`. Combining with (H5), at either pair of
plaquettes with the chosen offsets,

    |P^fib_(infinity;L)(p,q_n)| >= 5mu/8,
    |P^fib_(infinity;L)(p,q_f)| <= 3mu/8.

Their squared difference is at least
`(25-9)mu^2/64=mu^2/4`, and therefore

    a_L=(3/2)|(P^fib_near)^2-(P^fib_far)^2|
        >=3mu^2/8=2a_0>0.                               (H19)

There is also slack for the original finite regulators. At each fixed
such `L`, (B-4) eventually makes the two total covariances accurate to
`mu/16`, while (H12) already bounds each fibre correction by `mu/8`.
The corresponding near and far absolute values are then at least
`9mu/16` and at most `7mu/16`. Their squared difference is at least
`(81-49)mu^2/256=mu^2/8`, so their `a_(n,U;L)` is at least `a_0`.
No rate in `n,U` or in the coupling is needed for this conclusion.

**Discharged (fixed geometry for B-1).** One can take

    p=(-d,-d,-d,-d),   q_n=(d,d,d,0),   q_f=(d,d,d,d),

all in the `(1,2)` plane orientation. They remain fixed while `L` grows.
In the explicit linear map, a blocked plaquette is supported in the
coordinate box extending by at most two level-j cells from its base.
To verify this also before the continuum limit, (B-1) has transverse
fine displacement at most `(n-1)/2`, and longitudinal displacement at
most `(n-1)/2+n`, including the last link endpoint. Divide by `n` and
include the other unit edge of the plaquette: the resulting box is
`[-1/2,3/2]^2 x [-1/2,1/2]^2`, translated to its base (or a smaller
box at finite `n`). Composition is `Q_n Q_L=Q_(nL)`, so no extra range
accumulates. The box has coordinate radius at most two and sum of
coordinate radii at most four; use the safe radius `w=4`, independent
of `L`, also if the support radius uses Euclidean or edge distance.

**Implication (geometry for the consumer's actual observables).** If the
nonlinear observables have the corollary's support radius `w`, free of
`L`, first choose an integer

    d >= max(64, 2w+2),    N_D=4(d+w+1).

The supports of each pair are then strictly ordered on every axis.
The symbol `N_D` is the *window* radius called `n` in NT1-F; it is
distinct from the fine blocking ratio `n` in (B-2). Both pairs fit in
that fixed window. If `n_L=L/C_win` is the window allowance in the
criterion, take any odd `L_0` at least

    max{L_split, C_win N_D, 8(d+w+1)+1}.                  (H20)

The last bound also puts the whole window of plaquettes and their
supports in the central coarse block with ample clearance. All offsets,
`w`, `N_D`, `mu`, `a_0`, and the coefficient `2^53` were chosen before
`L`; none grows with it. For the explicit linear calculation, `w=4`
and `d=64` suffice. A support statement for a complete nonlinear map
does not follow merely from its first jet being (B-1).

**Implication (clipping, then smoothing, then weak coupling).** The
smaller free constant may make the required `L` very large; it creates
no circular choice. Fix geometry and (H18) first. If the clipping
constant in (F-3) is bounded uniformly by `A`, choose
`b>=max(1,(8A/a_0)^(1/r))`. Then `2 tau_b<=a_0/4`.
Choose `L>=L_0` large enough for the smoothing error, and finally choose
`X` for the (FT), omega, and eta errors as in NT1-F.

There is one precision needed in the printed order: when the clipping
bound is only `C_(N_D,r)(L)<=A(1+log L)^alpha`, a single value of `b`
cannot be justified *before* all `L` from that bound alone. Instead fix
the clipping rule

    b(L)=max{1,(8A/a_0)^(1/r)(1+log L)^(alpha/r)}          (H21)

before choosing `L`. This is the power-of-log interpretation already
used in NT1-F's explanation. With its stated power-of-log bounds on
`C_(N_D)`, fixed `C_s`, positive `kappa_lift`, and the stated eventual
`L`-independent bound on `Mbar_1`, the smoothing error is bounded by
`B(1+log L)^gamma L^(-2 kappa_lift)` for fixed `B,gamma`.
At fixed `L`, take weak coupling small enough that `omega_L<=1` when
bounding `bold-C_(N_D)`. To check existence of the choice of `L`, put
`t=log L` and choose an integer `m>gamma`. The positive exponential
series gives `exp(2 kappa_lift t)>=(2 kappa_lift t)^m/m!`;
thus the error is at most a constant times `t^(gamma-m)`, which tends
to zero. After this `L` is fixed, `b=b(L)` is fixed, and `X` is chosen
last. These are implications of the producer bounds, not proofs of
them. The Gaussian exponent `kappa=2` in (H12) is not substituted for
the producer's `kappa_lift`.

**Discharged (read boundary).** Read GOAL and FINISH's Rules; the
criterion note; bounded ranges of `witness-blocked-tree-limit.md`,
`witness-two-separation.md` (NF-5), `witness-interface-moments.md` (M-2),
`parts/witness.md`, and `parts/upper-chain.md` containing the cited
definitions and consumers. No hard-core attempt part file or gate on an
attempt was read. No numerical scripts were read or run, and no checks
directory was created.

## Endpoint

**Discharged:** the written estimate (H5) replaces the numerical near/far
table; (H12) replaces the trend with an explicit `L^-4` bound, uniform
even at block edges; (H17) proves the joint regulator limit for the
specified fibre; and (H18)--(H20) give `a_L>=a_0>0` for every admissible
odd `L>=L_0`. All are statements about the explicit free map (B-1).

**Implication:** NT1-F can use this free input, with the clipping order
made precise by (H21) if its constants are only logarithmically bounded.
It still assumes H-NET, the fixed-scale part of H-SCALE, the clauses
listed in section 2 of the criterion, (FT), and a support radius free
of `L` for the actual nonlinear observables.

**Gap / outside this calculation:** those nonlinear and reconstruction
clauses, and any identification of another gauge/torus regulator with
the one in (B-3). No assertion about Wilson or either hard-core attempt
is discharged here. No mathematical clause of the requested *explicit
free-value problem* is left unchecked in this note; this is an author
proof without independent review or formal verification.
