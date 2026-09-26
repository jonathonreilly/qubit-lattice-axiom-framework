# Prepared-state refinement: independent derivation before author checks

2026-09-21. The complete supplied note and the three pinned first-campaign
inputs have been read. Their identities are in READ_BOUNDARY.json. The
stationary propagator is an imported checked hypothesis; its replacement
proof is not being redone. The prepared-state author checker/results remain
unopened. This check concerns the new smooth reweighting, covariance/entropy,
local statistics and finite-volume nonstationarity examples. It is not a new
preparation/propagation bridge, a local preparation mechanism or an audit.

## 1. Hypotheses and the Gaussian calculation

Keep the full-support isotropic fifteen-label product, fixed positive
rho_A,rho_B and vacancy density, fixed bounded exchange rates with positive
floor, no births, a fixed finite set M of nonzero torus modes modulo conjugacy,
fixed lambda>=0 and a fixed finite time interval. At sufficiently large N,
the selected modes have no aliases or self-conjugacy. The normalized one-site
vector (e/sqrt(rho_A/3), b/sqrt(rho_B)) has mean zero and covariance I_6.
Its cross covariance with the other eight stated moments is zero. Product
Fourier CLT therefore gives independent proper complex CN(0,I_6) vectors at
the selected representatives. It does not assert finite-N Gaussianity.

There are two complex longitudinal coordinates per selected mode. Let
d=2|M| be their total complex dimension. For one CN(0,1) coordinate, |z|^2
is exponential of mean one, and

    E exp(-lambda |z|^2)=1/(1+lambda),
    E[|z|^2 exp(-lambda |z|^2)]=1/(1+lambda)^2.

Thus Z_N -> (1+lambda)^(-d), and the limiting covariance of each selected
six-vector is diag(Sigma,Sigma), with

    Sigma=P_T+(1+lambda)^(-1)P_L.

This is a bounded-continuous weighted CLT. The transverse coordinates and
the spectator fields remain independent of the tilted longitudinal ones in
the limiting Gaussian. At finite N they need not have those independences.
Uniform fourth moments of bounded independent site sums, together with
g_N/Z_N<=1/Z_N and a positive limiting Z_N, give the needed uniform
integrability for second-moment convergence.

The exact finite-N entropy identity is

    H(mu_N|nu_N)=-log Z_N-lambda E_mu Q_N.

For lambda>0, Q exp(-lambda Q) is bounded, so weighted CLT gives
E_mu Q_N -> d/(1+lambda) directly. For lambda=0, H=0 exactly. Hence

    H(mu_N|nu_N) -> d[log(1+lambda)-lambda/(1+lambda)].

This expression is the exact finite-lambda *limiting* entropy, not an exact
Gaussian formula at finite volume. Entropy density tends to zero at fixed
lambda and M. Neither the density bound nor these arguments are uniform as
lambda or the number of selected modes grows.

## 2. Transfer and time covariance

The unchanged conditional path kernel gives the exact path density
g_N(eta_0)/Z_N. For every nonnegative path variable F,

    E_mu F <= Z_N^(-1) E_nu F.

Apply this to the squared remainder in the pinned stationary propagator,
with the supremum outside expectation. This transfers its fixed-T result
without requiring microscopic stationarity of mu_N. The same elementary
bounded-path-density transfer was already established for the earlier box
conditioning; the smooth tilt refines its initial distribution.

Write Cw=K cross w, r=|K|, and retain the signed c. Since C^T=-C,

    G=i c [[0,C],[-C,0]]

is anti-Hermitian. Also C P_L=0 and C^2=-r^2 P_T. Therefore exp(Gt) has
diagonal blocks P_L+cos(crt)P_T, upper block i sin(crt)C/r, and the negative
lower block. The tilted covariance commutes with G, so the limiting Gaussian
process is stationary. The displayed auto- and cross-covariances follow,
including the sign of c in the cross block. If c=0 all six vector modes are
static. The other eight conserved modes have not been removed.

The ordered N->infinity, then lambda->infinity limit suppresses the selected
longitudinal coordinates. It does not justify a joint lambda_N limit, all-mode
conditioning, microscopic path convergence or continuing births. A finite
list of observation times follows from the imported L2 errors; no new
path-space topology is asserted.

## 3. A quantitative local-marginal estimate and charge variance

Regard the finite Fourier vector as a real Euclidean vector Y, and let P
project onto all selected longitudinal coordinates. The function
g(Y)=exp(-lambda ||PY||^2) has global Lipschitz constant

    L_lambda=sqrt(2 lambda/e),

with L_0=0. This follows by maximizing 2 lambda r exp(-lambda r^2).
For a fixed local set A, remove its summands from Y_N. The remaining vector
Y_out is independent of all variables in A under the product measure, and

    ||Y_N-Y_out|| <= |A| sqrt(m) M_0/sqrt(V),
    M_0=max(sqrt(3/rho_A),sqrt(3/rho_B)).

For any local event F, subtract E_nu F inside its covariance with g_N.
Independence from g(Y_out) then yields

    |mu_N(F)-nu_N(F)|
      <= L_lambda |A| sqrt(m) M_0 / [Z_N sqrt(V)].

This proves the claimed fixed-site-set total-variation estimate. It needs
joint local marginals, not an unjustified assumption of finite-N independence.
The constant can grow with lambda,m or the local set and is bounded in N
only after fixing those parameters. At lambda=0 the two laws coincide exactly.

The centered divergence at one site involves six distinct neighbors for the
allowed side lengths. Product means vanish, each e_j has variance rho_A/3,
and each b_j has variance rho_B. The limiting divergence variances are
therefore 6(rho_A/3)/4=rho_A/2 and 6 rho_B/4=3 rho_B/2. The fixed six-site
TV estimate transfers them to mu_N, since the observables are bounded.
Global A-sign and global B-sign symmetries give zero initial means exactly.
No microscopic charge elimination follows from this finite-mode tilt.

## 4. Microscopic nonstationarity and one witness-scope counterexample

The positive floor connects all arrangements within a fixed content multiset.
Product invariance, conditioned on these conserved counts, supplies the uniform
stationary law of that sector, unique by irreducibility. A nonconstant tilt
on such a sector is therefore not invariant.

For M consisting of the first axis shell, the proposed two-identical-+x-record
example works. Independently enumerating the entire N=4 sector gives 2016
arrangements. On this sector b=0 everywhere, so the context drive vanishes
and the process is exactly symmetric nearest-neighbor stirring with its
positive floor. Take rho_A=3/8 and lambda=4 log 2. The three possible Q values
are 0,1/4,1/2, with multiplicities 512,1024,480. The conditional normalizer is
143/252. For the configuration with records at 000 and 100,

    (mu L)(configuration)=1/1144 > 0

for unit unaccelerated exchange floor. Euler acceleration multiplies this by
N and does not change the nonstationarity. The entropy derivative in this
sector is -(188/143) log 2. Thus the finite-chain countercontrol is exact.

**Narrow finding:** the note then says that for a symmetry-closed set
*containing* the first axis shell, the other modes do not remove the
distance-one versus distance-two difference. Read as a statement for arbitrary
larger such M at the stated finite N>=4, this is false.

Take N=5 and

    M/(2 pi)={e_x,e_y,e_z,2e_x,2e_y,2e_z}.

This is cubic closed up to conjugacy and has neither aliases nor self-conjugate
modes. For two +x records separated by d e_x,

    Q(d)=[4+2 cos(2 pi d/5)+2 cos(4 pi d/5)]/[V(rho_A/3)].

At d=1 and d=2 the two cosine contributions interchange, so Q(1)=Q(2).
For rho_A=3/8 both equal 24/125. A separation by e_y instead gives 64/125,
so the sector is still nonstationary; only the stated general witness fails.
The checker verifies these values exactly and all mode-set symmetry/alias
conditions. A narrow correction is “For the first-axis-shell choice of M”.
Alternatively the distance-one/two argument holds for any fixed larger M
once N is sufficiently large: each summand in its difference is a nonnegative
multiple of cos(theta)-cos(2theta), positive for 0<|theta|<2 pi/3; taking
N>3 max_K |K_x/(2 pi)| suffices and the first x mode makes the sum strict.
The Gaussian limit, entropy, local estimate and bounded transfer are unaffected.

## 5. Exact full-product finite-volume control

A separate control uses the actual 15-label N=4 product law, not just a
fixed-count sector. Put rho_A=3/8, rho_B=1/4, M={2 pi e_x}, lambda=16 log 2.
The real and imaginary projected Fourier sums come from disjoint groups of
32 independent sites. After absorbing the +/- phases by sign symmetry,
one site's sufficient statistic (e_x,b_x) has integer weights

    (0,0):10; (+1,0):1; (-1,0):1; (0,+1):2; (0,-1):2,

with common denominator 16. The exact 32-site distribution is given by
the coefficients of [10+x+x^-1+2y+2y^-1]^32/16^32. It has 2113 states.
For a group sum (a,b), its Q contribution is (2a^2+b^2)/16, and its tilt is
exactly 2^[-(2a^2+b^2)]. Rational convolution therefore evaluates Z_N,
E_mu Q_N, one-site marginals and marked two-site moments without sampling.
Removing one or two factors computes the local and opposite-neighbor marks.

The exact rational outputs, converted here only for readability, are:

    Z_N = 0.00709888423536531,
    E_mu Q_N = 0.161614476673960,
    H(mu_N|nu_N) = 3.15545575572514,
    one-site TV(mu_N,nu_N) = 0.0188103504166393,
    E_mu |D e|^2 = 0.183808585888066,
    E_mu |D b|^2 = 0.360551556183041.

At the same lambda the Gaussian-limit normalizer is 0.00684103641446995
and entropy is 3.15023715236121. This decisively distinguishes the valid
limiting formulas from false finite-volume Gaussian equalities. Both charge
variances are positive, and both one-site vector means vanish exactly.
All underlying rationals are retained in INDEPENDENT_RESULTS.json.

## Preliminary disposition

The new limiting covariance/entropy and local-marginal/charge claims check.
There is one narrow finite-volume witness-scope correction above. Pinned
propagation remains an explicit dependency, and preparation remains nonlocal.
The independent script passed on its first execution; full stdout, stderr,
receipt and exact results are retained, with no failed attempt to discard.
The pre-comparison seal will freeze these bytes before author-checker access.
