# Independent native-formation Euler extension

Date: 2026-09-21. This report was derived before access to primary
native-formation arguments, checkers, simulations or results. It uses only
the supplied generator and the three named sealed independent context,
Euler and axis-balanced reports. It is a bounded mathematical check, not
an audit, physical identification or publication-source review.

**Result.** The smooth-profile relative-entropy theorem extends to the
specified neighbor-dependent births. The reaction is

\[
 r_a(p)=\beta p_0\left[p_0+\sum_{b=1}^6W(a,b)p_b\right]^6.                 \tag{1}
\]

The given full-support profile must solve the corresponding reaction
conservation law; smoothness alone is insufficient. The source-adjoint
constant and linear terms cancel after local equilibrium, not pointwise.
No invariance of the actual growing homogeneous law is needed, and that
law is generally not product. For the j-family, density, vector and
quadrupole reactions are explicit. The full linearized nonautonomous
response has a rigorous finite-time energy bound and an exactly bounded
transverse amplification factor. Frozen eigenvalues are not its evolution
operator.

## 1. Hypotheses, product reaction and precise theorem

Use the cubic torus Lambda_N=(Z/NZ)^3, N>=4, with seven states: vacancy 0
and six immutable occupied labels +/-e_i. The conservative generator L_N
is the already checked axis-balanced context exchange, with fixed finite
range, fixed bounded rates and a fixed positive floor delta for every
unequal-label adjacent transposition. Its homogeneous product current J
and nonlinear entropy identities are those proved in the allowed sources.
The new macroscopic generator is

\[
 G_N=N L_N+R_N,\qquad
 R_NF=\beta\sum_{x,a}{\bf1}_{\eta_x=0}
       \prod_{y\sim x}W(a,\eta_y)
       [F(\eta^{x,a})-F(\eta)].                                      \tag{2}
\]

Beta is fixed and nonnegative; the growing case has beta>0. The matrix
entries are fixed, strictly positive and bounded, with W(a,0)=1. Neither
symmetry, row normalization nor cubic covariance of general W is required
for the theorem. Arbitrary W can break the model's rotational symmetry;
that does not obstruct the entropy estimate. The birth rate is the supplied
unnormalized product, not a conditional outcome probability divided by
the sum over labels. On the original microscopic clock it is beta/N times
that product.

Write p=(p_1,...,p_6), p_0=1-sum_a p_a, and

\[
 \ell_a(p)=p_0+\sum_b W(a,b)p_b
           =1+\sum_b[W(a,b)-1]p_b.
\]

The center and its six distinct neighbors are independent under a product
law, so the mean birth drift is (1). Under an inhomogeneous product its
exact mean at x is beta p_0(x) product_{y~x} ell_a(p(y)); the continuum
local-equilibrium source is (1). This is a polynomial of degree at most
seven in the occupied probabilities, with bounded derivatives on the
closed simplex. Positivity of W is part of the supplied model; the entropy
extension actually needs only bounded nonnegative insertion rates of this
form and the conservative positive floor.

Fix T<infinity. Suppose the **given** C^2 periodic profile satisfies

\[
 \partial_t p+\sum_{i=1}^3\partial_i J^i(p)=r(p),\qquad
 \min_{t\le T,X,a=0,...,6}p_a(t,X)\ge\eta_*>0.                        \tag{3}
\]

Let nu_t^N be the inhomogeneous product with these marginals. If
H(mu_0^N|nu_0^N)=o(V), V=N^3, then

\[
 \sup_{t\le T}V^{-1}H(\mu_t^N\mid\nu_t^N)\longrightarrow0.            \tag{4}
\]

Empirical occupied-species profiles converge in probability to p at fixed
times against continuous test functions, and uniformly on [0,T] against
fixed smooth tests. This is conditional on the smooth interior solution.
There is no new global smooth-solution, shock, boundary-density, fluctuation
or finite-N product-preservation claim.

The solution condition in (3) is necessary. For instance W=1, beta>0 and a
constant interior profile in time are already incompatible: starting in
that product, mean vacancy decays exponentially and the limiting density
changes. Initial entropy zero and C^2 positivity alone cannot justify a
different stationary target profile.

## 2. New source-adjoint identity and entropy closure

Let pi_N be the uniform seven-state product and f_t=dmu_t^N/dpi_N. Put

\[
 D_N(f)=\sum_e E_{\pi_N}(\sqrt{f^e}-\sqrt f)^2,
 \qquad W_* = \max_{1\le a\le6,\ 0\le b\le6}W(a,b),
\]

where a ranges over occupied insertion labels and W(a,0)=1. The harmless
notation b=0,...,6 includes vacancy; W_*>=1. At an occupied site a,
R_N^*1 contributes beta product_{y~x}W(a,eta_y); at a vacancy it contributes
-beta sum_a product_{y~x}W(a,eta_y). Therefore R_N^*1<=beta W_*^6 V.
The original exchange entropy argument gives

\[
 \int_0^T D_N(f_t)\,dt
 \le {V[\log7+\beta W_*^6T]\over N\delta}.                         \tag{5}
\]

This budget holds for the actual evolving law, without spatial independence
or a product assumption.

Set theta_a=log(p_a/p_0), H(p)=diag(1/p_a)+p_0^{-1}11^T and
psi_t=dnu_t^N/dpi_N. Because a birth at x changes only its center, leaving
the neighboring rate arguments unchanged, its exact source-adjoint term is

\[
 {R_N^*\psi_t\over\psi_t}
   =\sum_x B_{p_x}(\tau_x\eta),
 \quad
 B_p(\eta)=\beta\sum_a\prod_{y\sim0}W(a,\eta_y)
       \left[{p_0\over p_a}{\bf1}_{\eta_0=a}
                         -{\bf1}_{\eta_0=0}\right].                \tag{6}
\]

For a homogeneous product with probabilities q, its expectation is

\[
 F(p,q)=E_{\pi_q}B_p
 =\beta\sum_a\ell_a(q)^6\left[{p_0\over p_a}q_a-q_0\right].          \tag{7}
\]

Here p is the frozen reference parameter, not the actual local count
vector. The decisive two identities are

\[
 F(p,p)=0,\qquad D_qF(p,p)=H(p)r(p).                                \tag{8}
\]

To check the derivative in occupied coordinates, the central bracket
(p_0/p_a)q_a-q_0 is zero at q=p, so every derivative of ell_a(q)^6 drops
out. For coordinate b the remaining derivative is

\[
 \beta\left[{p_0\over p_b}\ell_b(p)^6+\sum_a\ell_a(p)^6\right]
   ={r_b(p)\over p_b}+{\sum_a r_a(p)\over p_0}.
\]

Thus neither a derivative of the birth response nor a factor of six is
missing from the entropy cancellation: the appropriate derivative here
is D_qF, not D r. On the compact interior set of reference p, the second
q-derivatives of F are uniformly bounded all the way to boundary q. Hence

\[
 |F(p,q)-[H(p)r(p)]\cdot(q-p)|\le C|q-p|^2.                         \tag{9}
\]

The source is not equal configuration by configuration to
[H(p)r(p)].(xi_0-p). Unlike uniform births, it still depends on the
neighbor contents. Replacement is the new required step.

Here are the load-bearing replacement details. Take open cubes of side
ell and M=ell^3 sites, containing all seven sites of a birth footprint and
all four sites of a current footprint. The old unit-swap canonical
Poincare bound M^2 7^M is unchanged: all internal adjacent swaps still
have the conservative positive floor. It does not require that the
actual finite-context dynamics with exterior frozen be canonical-stationary.
Marginalizing a density contracts the swap energy, and each edge lies in
at most M translated blocks.

The new observables are just the finitely many bounded local functions

    1_(eta_0=a) product_{y~0} W(a,eta_y),
    1_(eta_0=0) product_{y~0} W(a,eta_y).

Their coefficients beta p_0/p_a are uniformly bounded and Lipschitz for
p_a>=eta_*. For a count-conditioned block law, sampling a seven-site
footprint without replacement differs from product sampling at the block
frequencies q by O(1/M). For two disjoint footprints, the same estimate
on at most 14 positions bounds covariance by O(1/M); only O(M) anchor
pairs overlap. Thus an interior block average has canonical variance
O(1/M) and mean F(p,q)+O(1/M), with an additional O(1/ell) boundary
error if normalized by M, as in the original proof. Sectorwise Hellinger
comparison and (5) give the integrated replacement error per volume

\[
 C_T\left[\ell^{-1}
       +\sqrt{M^3 7^M/N}\right].                                  \tag{10}
\]

All omitted constants are fixed by W, beta, delta, T and the profile.
Shifting smooth coefficients to block centers costs O(ell/N) per volume.
This proves replacement for (6), rather than supposing that nu_t^N is an
exactly evolving product. The same exchange-current replacement is already
proved by the allowed Euler report.

For completeness, using its forward-current entropy route and the birth
jump entropy inequality gives

\[
 {d\over dt}H(\mu_t^N\mid\nu_t^N)
 \le -N\delta D_N(f_t)
     -\sum_{x,i}E_\mu j_i(x)\cdot N\Delta_i\theta_x
     +\sum_xE_\mu B_{p_x}
     -\sum_xE_\mu(\xi_x-p_x)\cdot\partial_t\theta_x.                \tag{11}
\]

The exchange entropy identities in the sealed axis-balanced report give

\[
 \partial_t\theta= -\sum_i A_i^T\partial_i\theta+H(p)r(p),
 \qquad \partial_i\theta\cdot J^i=\partial_i\Psi_i.
\]

After replacement, the exchange constant term integrates to zero by
periodicity and its linear term cancels as before. For the source, (8)
cancels its constant and linear terms against the reaction part of the
last term of (11). Both remainders are bounded by C sum_x|q_ell(x)-p_x|^2.
The same product Hoeffding estimate, overlap coloring and entropy inequality
as in the sealed proof yield

\[
 E_\mu\sum_x|q_\ell(x)-p_x|^2
    \le C H(\mu\mid\nu)+C V/M+C V(\ell/N)^2.
\]

Gronwall therefore gives, with fixed C_T,

\[
 \sup_{t\le T}{H(\mu_t^N\mid\nu_t^N)\over V}
 \le C_T\left[{H(\mu_0^N\mid\nu_0^N)\over V}
    +\ell^{-1}+M^{-1}+\ell/N+(\ell/N)^2
    +\sqrt{M^3 7^M/N}\right].                                    \tag{12}
\]

Taking ell to infinity slowly, for example odd ell with
ell^3<=log N/(2 log7), proves (4). Zero probabilities of mu can be handled
by the original finite-state regularization; only the references must be
strictly positive. For the empirical consequence, source jumps change a
test average by O(1/V) and have total rate O(V), so their bracket is
O(T/V). Exchange contributes O(T/(NV)). The bounded smooth-test drift,
Doob inequality and a finite time grid give uniform-time convergence for
smooth tests. No central-limit-scale consequence is being inferred.

## 3. The complete j-family reaction and product-law counterexample

Now W(a,b)=1+j v_a.v_b, |j|<1. Put rho=sum p_a, v=1-rho,
g_i=p_(+i)-p_(-i), q_i=p_(+i)+p_(-i), r_i=q_i-rho/3, sum_i r_i=0.
Then ell_(+/-i)=1+/-j g_i, so the six species sources are exactly

\[
 r_{+i}(p)=\beta v(1+jg_i)^6,\qquad
 r_{-i}(p)=\beta v(1-jg_i)^6.                                     \tag{13}
\]

Define E(z)=1+15z^2+15z^4+z^6 and O(z)=6z+20z^3+6z^5. The complete
six-field reaction, in three q and three g fields or equivalently one
density, three vector and two quadrupole fields, is

\[
 R_{q_i}=2\beta v E(jg_i),\qquad R_{g_i}=2\beta v O(jg_i),
\]
\[
 R_\rho=2\beta v\sum_i E(jg_i)
 =6\beta v+30\beta v j^2|g|^2
              +30\beta v j^4\sum_i g_i^4+2\beta v j^6\sum_i g_i^6,
\]
\[
 R_{r_i}=2\beta v\left[E(jg_i)-{1\over3}\sum_k E(jg_k)\right].       \tag{14}
\]

These sources are independent of the quadrupole *state* except through
rho, but they can generate a nonzero quadrupole from a polarized vector,
beginning at quadratic order. They are not generally rotationally invariant
nonlinear functions. The six-field PDE includes the unchanged nonlinear
currents, for the sealed fixed witness u=0,E=1/2,A=2,B=-3:

\[
 S_k=2\rho-3q_k,\qquad J_\rho^k=2vS_k g_k,
\]
\[
 J_{g_i}^k=\delta_{ik}S_kq_k+(2-3\delta_{ik}-2S_k)g_k g_i,
 \quad J_{q_i}^k=g_k[\delta_{ik}S_k+(2-3\delta_{ik}-2S_k)q_i],         \tag{15}
\]

and J_(r_i)^k=J_(q_i)^k-J_rho^k/3. Equations (14)-(15) retain all six
fields; they do not replace quadrupoles by an imposed isotropic constraint.

For homogeneous isotropic initial data g=0,q_i=rho/3, the **Euler reference
solution** is

\[
 v(t)=v_0e^{-6\beta t},\quad \rho(t)=1-v(t),\quad
 p_a(t)=\rho(t)/6.                                                \tag{16}
\]

This does not say that the actual finite stochastic law remains product.
There is a direct counterexample within the given model. Start the finite
cubic torus in an isotropic product at 0<rho<1. For adjacent x,y and any
coordinate i, both initial vector means vanish, and

\[
 \left.{d\over dt}\operatorname{Cov}
   (v_i(\eta_x(t)),v_i(\eta_y(t)))\right|_{t=0}
       ={4\beta j\rho(1-\rho)\over3}.                             \tag{17}
\]

Exchange contributes zero because the initial product is invariant under
that generator, even after its N acceleration. In the birth-at-x term,
the five other neighbors have mean weight one; the distinguished neighbor
has E[W(a,eta_y)v_i(eta_y)]=j rho v_(a,i)/3. Summing v_(a,i)^2 over the
six labels gives 2, and the birth-at-y term supplies the other equal
contribution. For beta=1/3, j=1/2, rho=1/2 the derivative is exactly 1/18.
A product evolving along (16) would keep this connected covariance zero.
The exact local generator check below reproduces 1/18. Rapid conservative
relaxation and (4) are consistent with this finite-N non-product fact.

## 4. Six-field linearization and honest amplification bounds

Linearize the PDE, not the finite-N stochastic law, around (16). Let
lambda=6beta, mu(t)=12beta j v(t), a(t)=2rho(t)v(t) and b(t)=2rho(t)/3.
For each fixed Fourier wave vector K, the full system is

\[
 \dot{\delta\rho}=-\lambda\delta\rho-i a(t)K\cdot\delta g,
 \quad
 \dot{\delta g}=\mu(t)\delta g-i b(t)K\delta\rho,
 \quad \dot{\delta r_i}=0.                                       \tag{18}
\]

At the species level the reaction derivative is

\[
 D r=-\beta11^T+6\beta j v\,VV^T,
\]

where the six rows of V are the occupied label vectors. Thus it has the
density eigenvalue -6beta, three vector eigenvalues 12beta j v, and two
zero quadrupole eigenvalues. The exchange part is exactly the previously
proved rank-two acoustic block. If the separately supplied conservative
family is multiplied by a fixed drive amplitude alpha, the a and b in
(18) are both multiplied by alpha; the source and energy conclusions below
are unchanged. The executed control uses the sealed witness alpha=1.

For K!=0 there are two transverse vector components. They satisfy the
**exact nonautonomous** formula

\[
 \delta g_\perp(t)
   =\exp\{2j[\rho(t)-\rho(0)]\}\delta g_\perp(0).                  \tag{19}
\]

For j>0 this is finite amplification, bounded by exp(2j v_0), and not an
indefinite exponential growth rate. For j<0 it is finite attenuation with
a generally nonzero limiting factor. At K=0 all three vector components
have (19), density decays by exp(-lambda t), and quadrupoles are constant.

Freezing time gives two longitudinal roots of

\[
 (z+\lambda)(z-\mu(t))+c(t)^2|K|^2=0,
 \quad c(t)^2={4\rho(t)^2v(t)\over3},
\]

namely

\[
 z_\pm(t)={\mu(t)-\lambda\over2}
     \mathbin{\pm}\sqrt{{[\lambda+\mu(t)]^2\over4}-c(t)^2|K|^2}.    \tag{20}
\]

The other frozen eigenvalues are two copies of mu(t) and two zeros.
Equation (20) describes only the instantaneous matrix. Matrices at
different times generally do not commute, and neither exp[t M(0)] nor an
integral of its eigenvalues is the propagator of (18).

There is a direct bound for the *whole* nonautonomous system. For complex
Fourier amplitudes define the instantaneous product-entropy energy

\[
 \mathcal E(t)={|\delta\rho|^2\over\rho v}
   +{3\over\rho}\left(|\delta g|^2+\sum_i|\delta r_i|^2\right),
 \qquad \sum_i\delta r_i=0.                                      \tag{21}
\]

Let its three nonnegative contributions be E_rho,E_g,E_r. Differentiating
the time-dependent weights, using rho'=lambda v, and cancelling the
skew transport terms gives the exact identity

\[
 \dot{\mathcal E}
   =-{\lambda\over\rho}E_\rho
     +\left(2\mu-{\lambda v\over\rho}\right)E_g
     -{\lambda v\over\rho}E_r.                                  \tag{22}
\]

The vector coefficient is 6beta v(4j-1/rho). Consequently

\[
 \mathcal E(t)\le \mathcal E(0)
  \exp\left\{\int_{\rho_0}^{\rho(t)}[4j-1/s]_+\,ds\right\}
 \le \mathcal E(0)e^{4j_+v_0}.                                   \tag{23}
\]

For j<=1/4 the energy is nonincreasing. For j>1/4 the integral is zero
until rho(t)>rho_*=max(rho_0,1/(4j)); afterwards it equals
4j[rho(t)-rho_*]-log[rho(t)/rho_*]. This is uniform in the Fourier
direction and magnitude for the linearized PDE. The time-dependent norm
matters: a transverse vector can grow in physical amplitude for any j>0
even when (21) decreases. Equation (23) is a bound, not a formula for the
exact longitudinal maximum. It allows finite transient transfer between
density and the longitudinal vector.

The bound is even uniform in time for this particular linear ODE and fixed
interior rho_0: (21) bounds the ordinary field norm from below uniformly.
It does not establish an infinite-time hydrodynamic limit, nonlinear
stability, or a stationary native-formation fluctuation theorem. Nor does
it force all perturbations to decay, since quadrupoles stay constant and
vector amplitudes can retain nonzero values. Beta=0 recovers conservative
linear transport; j=0 recovers the uniform-birth reaction derivative.
Empty or full initial densities are not covered by this entropy metric
or by the initial full-support theorem.

## 5. Independent controls, failed routes and provenance

`independent_check.py` does not import primary code or read any author
result. Its local birth generator has six frozen neighbor labels and all
seven center states. Permutation invariance of the product rate in the
six neighbors gives an exact lumping into 924 count orbits, representing
all 7^7=823,543 star states. Each orbit has the complete seven-state
center generator: six rates out of vacancy, their negative row sum, and
zero occupied rows. These local calculations are exact components of the
specified cubic generator, not an enumeration of its full 7^(N^3) state
space or a replacement of it by a star model.

The checks use a strictly positive nonsymmetric W with nonconstant row
sums and unequal product weights, an off-reference product q!=p, and a
uniform-weight control. Exact summation verifies (1), the full expectation
(7), the zero constant term and all six derivatives in (8), as well as the
uniform-reference source bound in (5). The derivative is computed through
the categorical score on **all seven sites**, rather than differentiating
the proposed closed formula. The balanced j-case independently gives the
non-product covariance derivative 1/18.

Symbolic controls differentiate the six species reactions before changing
coordinates. They verify all six linear source and transport fields, the
full nonlinear reactions (14), the quadrupole independence of the source
state, the complete time-dependent metric identity (22), and the frozen
longitudinal polynomial. The two constrained r fields use the metric
(3/rho)[[2,1],[1,2]], so the third quadrupole component is not discarded.

A separate numerical control integrates the full six-by-six nonautonomous
fundamental matrix at rho_0=0.1, beta=1/3, j=0.9, K=(2pi,4pi,0), T=2.
The weighted operator norm respects (23) on the 101 sampled times; the
transverse gain is 4.905360883851552, below its exact all-time bound
5.053090316563868. The frozen-at-zero matrix instead predicts transverse
gain 651.9709462711725. The fundamental matrices differ in Frobenius norm
by about 966.20. This numerical comparison illustrates the invalid frozen
substitution; formulas (19) and (22)-(23), not numerical sampling, prove
the stated gain and bound.

The following tempting routes are explicitly rejected:

1. **Exact growing product:** false in general by (17); the entropy proof
   does not require it.
2. **Pointwise source cancellation:** false with neighbor-dependent
   weights; (7)-(10) provide the missing local-equilibrium argument.
3. **Normalized birth odds:** not the supplied generator and would give
   a different reaction.
4. **Frozen eigenvalues as growth exponents:** not valid for (18);
   (19) and (22) control its actual time dependence.
5. **Arbitrary positive profile as target:** (3) must be imposed. Fixed
   positive microscopic formation under N acceleration would also be a
   different scaling and is not covered by this proof.

There were two development executions, both with no assertion failures.
The first completed 14 controls. Inspection found that its general biased
product output mislabeled a raw pair-moment derivative as a connected
covariance derivative; the balanced 1/18 witness was unaffected. The
second script explicitly subtracts 2 times the vector mean times its
source derivative, reports both quantities, and adds the uniform-weight
control. The original script and complete first output are preserved as
`independent_check_attempt_01.py` and `RUN_attempt_01.log`. The final run
completed 15 controls: 11 exact finite/symbolic or combinatorial controls
and four numerical propagation/solver controls. `RUN_attempt_02.log` is
byte-identical to final `RESULTS.json`. `ATTEMPTS.json` records the correction
and both source identities; no attempt was suppressed.

Reproduce from this directory with:

    OPENBLAS_NUM_THREADS=1 python3 independent_check.py

Python, NumPy, SymPy and SciPy versions are in the raw results. No primary
source, native simulation, external theorem or literature was imported.
The only mathematical dependency reports are:

| Dependency | SHA-256 |
|---|---|
| `independent_context_exchange/REPORT.md` | `277ba40b64842d128a2e46ca7bd468a7efc7c4d401e629648d440588e7784713` |
| `independent_context_euler/REPORT.md` | `60aaef142f97aea228be967a711880c5272328e5173d6c8df8c033176605a1e3` |
| `independent_axis_balanced_context/REPORT.md` | `b9cedcafccb48dfcd2503e5f00569a547288d4dcef0fb7dfca832565aec8f7cf` |

Their seals and checker identities are included in `DEPENDENCIES.json`.
The adjacent `PRE_SOURCE_SEAL.json` identifies every artifact and dependency
before any primary-source comparison. No production, publication, Git, PR,
audit, prompt or unrelated campaign file was changed.
