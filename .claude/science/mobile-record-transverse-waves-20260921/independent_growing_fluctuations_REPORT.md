# Independent growing-product finite-mode fluctuation check

**Result.** The stationary deterministic transport statement does not extend
unchanged: births contribute noise of order one. Its correct extension is a
six-field time-inhomogeneous linear Gaussian diffusion. The extension can be
proved under the supplied hypotheses. The new ingredient is an evolving-law
energy estimate for the current replacement; it follows directly from the
finite-state forward and backward equations and does not assume stationarity
of the growing law.

The exact one-time product trajectory, the current replacement, and the
finite-mode martingale limit are proved below. The result concerns a fixed
full-support initial product, a fixed finite time interval, and finitely many
fixed modes/times. No infinite-dimensional, empty-initial-state, or new
growing-product source has been used or claimed.

## 1. Model, exact trajectory and statement

Let V=N^3 and let eta_t^N denote the process already measured in macroscopic
time, with generator

    G_N=N H_N+beta B_N,        beta>0 fixed.             (1)

H_N is one of the checked conservative context-exchange generators. Its
bounded finite-range rates have a fixed positive floor delta on all
nearest-neighbor exchanges of unequal labels, including two occupied labels.
B_N changes a vacant site to each of the six occupied labels at rate one.
Thus the per-label birth rate in (1) is beta, not N beta. Equivalently, before
accelerating time by N the microscopic birth rate would be beta/N.

The initial law is a homogeneous product with fixed probabilities
p_a(0)>0, a=0,...,6. Exchange annihilates every homogeneous product forward
measure. Independent births alone evolve that product by

    p_0(t)=p_0(0) exp(-6 beta t),
    p_a(t)=p_a(0)+p_0(0)[1-exp(-6 beta t)]/6,
                                             a=1,...,6.              (2)

Let mu_t^N be this product. Its derivative is mu_t^N beta B_N, and
mu_t^N H_N=0 at every t. Hence mu_t^N solves the full finite-state forward
equation for (1). Uniqueness proves that it is the exact law of eta_t^N for
every N. This argument does not assume that the two generator semigroups
commute. Products at distinct times need not be independent, and this is
not a preservation theorem for spatially inhomogeneous products.

For every fixed T, (2) remains uniformly inside the seven-probability
simplex on [0,T]. Write p(t) for its six occupied components and set

    C(t)=diag(p(t))-p(t)p(t)^T,
    A_i(t)=D J_i(p(t)),
    R=-beta 11^T,
    D_K(t)=-i sum_i K_i A_i(t)+R.                       (3)

All physical rate parameters are held fixed in the derivatives. J_i is
the previously checked exact product current of the actual exchange rule.
For example, in the unified notation of those reports,

    s_i(a)=A n(a)+B f_i(a)^2,
    sigma_i=sum_a p_a s_i(a),  g_i=sum_a p_a f_i(a),
    U_i=u+2E sigma_i,       Z_i=u+4E sigma_i,
    J_a^i=p_a[U_i f_i(a)+(2E s_i(a)-Z_i)g_i].           (4)

The old context family has A=1,B=0; the axis-balanced witness has
u=0,E=1/2,A=2,B=-3. Both rate implementations in each family are covered.
The proof only uses their checked product invariance, current polynomial,
entropy symmetry, fixed range, bounded ceiling and positive exchange floor.

For fixed integer m and K=2pi m, define

    Y_N(K,t)=V^(-1/2) sum_x exp(-iK.x/N)[xi_x(eta_t^N)-p(t)],

where xi is the six-component occupied indicator. For any finite list of
fixed nonzero modes and times, these fields converge jointly in law to

    dY_K(t)=D_K(t)Y_K(t)dt+sqrt(beta p_0(t)) dW_K(t).    (5)

The initial field is the product-law Fourier Gaussian with conjugated
covariance C(0). The Brownian fields are independent of it and obey

    E[dW_K dW_L^*]=I_6 1_{m=n}dt,
    E[dW_K dW_L^T]=I_6 1_{m=-n}dt,
    W_{-K}=overline{W_K}.                              (6)

Thus one representative of a nonzero +/- pair is a complex Brownian
motion with independent real and imaginary parts of variance dt/2.
If the zero mode is included, it is real and satisfies (5) with A(0)=0;
its exchange contribution vanishes exactly and needs no current replacement.
This adds no empty-state or infinite-dimensional assertion.

Let Phi_K(t,s) solve

    partial_t Phi_K(t,s)=D_K(t)Phi_K(t,s),
    Phi_K(s,s)=I_6.                                    (7)

In general this is a time-ordered propagator, not exp[D_K(t)(t-s)] or an
unjustified exponential of an integral of noncommuting matrices.

## 2. Correct nonstationary reversal and energy identities

This section makes explicit the step that cannot be copied from the
stationary proof. It also supplies a direct replacement for that step.

### 2.1 The weighted adjoint is not the reversed Markov generator

For a finite chain with row generator G and exact positive law mu_t,
let G^{dagger_t}=diag(mu_t)^(-1) G^T diag(mu_t) denote its formal adjoint
on functions in L2(mu_t). Define the score s_t=partial_t log mu_t. The
forward equation implies

    G^{dagger_t}1=s_t.

The generator of the reversed path, at the corresponding forward time t,
is

    G_t^rev=G^{dagger_t}-diag(s_t).                     (8)

Its off-diagonal rates are G(eta',eta) mu_t(eta')/mu_t(eta), and its rows
sum to zero. In the present model the exchange rates reverse to
N c_e(eta^e), because homogeneous product weights are equal under swaps.
Births reverse to deaths

    a -> 0 at rate beta p_0(t)/p_a(t).                 (9)

The exact score is

    s_t(eta)=sum_x [-6beta 1_{eta_x=0}
               +sum_{a=1}^6 beta p_0(t)/p_a(t) 1_{eta_x=a}].          (10)

It is not zero. The instantaneous generator
`(G_N+G_t^rev)/2` is reversible with respect to mu_t. In contrast,
`(G_N+G_N^{dagger_t})/2` contains the extra diagonal score/2 and is not
a Markov generator. No estimate below drops this correction or bounds
its extensive size by a volume-dependent exponential.

For a function u let

    Gamma_G(u)(eta)=sum_{eta'} G(eta,eta')|u(eta')-u(eta)|^2.

Then

    E_mu Gamma_G(u)=E_mu Gamma_{G^rev}(u),
    (1/2)E_mu Gamma_G(u)
      =-Re<u,G u>_mu+(1/2)E_mu[s_t |u|^2].             (11)

The last term is essential. For example let u be the total count of one
occupied species on a V-site torus. Exchanges preserve u, so under the
growing product

    -E[u G_N u]=-beta V(V-1)p_a(t)p_0(t)<0.            (12)

It cannot serve as a nonnegative stationary Dirichlet form. Equation (11)
restores the nonnegative energy. The proof below uses the equivalent direct
forward-equation identity, so no reversed-path martingale is needed.

### 2.2 Evolving-law additive-functional bound

Consider any finite-state Markov process with generator G_N from (1) and
its exact law mu_t. Let F_t be deterministic time-indexed functions. On
an interval [a,b], solve the finite backward equation

    (partial_t+G_N)u_t=-F_t,      u_b=0.                (13)

Equivalently, u_t(eta)=E[ integral_t^b F_s(eta_s)ds | eta_t=eta ]. This
terminal problem is well-defined without an irreducibility assumption on
the full birth process. For a piecewise continuous F it is solved on each
piece, which also suffices for the deterministic weights used later.

The forward equation for mu_t and the identity
`G|u|^2=2 Re(bar u G u)+Gamma_G(u)` give

    d/dt E_mu_t |u_t|^2
       =2 Re E_mu_t[bar u_t(partial_t+G_N)u_t]
                                      +E_mu_t Gamma_{G_N}(u_t).       (14)

In particular the derivative of the measure has not been omitted.
Integrating (14), and using the terminal condition, gives

    V_F:=||u_a||_{mu_a}^2+integral_a^b E_mu_t Gamma_{G_N}(u_t)dt
        =2 Re integral_a^b <u_t,F_t>_{mu_t}dt.          (15)

Dynkin's martingale satisfies

    integral_a^b F_t(eta_t)dt=u_a(eta_a)+M_b,
    E[M_b | eta_a]=0,
    E|M_b|^2=integral_a^b E Gamma_{G_N}(u_t)dt.

Consequently V_F is exactly the squared L2 norm of the additive functional,
not just a bound that omits a random initial term.

Define the unit-exchange form

    E_{0,t}(h)=(1/2)sum_e E_mu_t |h(eta^e)-h(eta)|^2.

The exchange floor and nonnegative birth bracket give pointwise in time

    E_mu_t Gamma_{G_N}(h)>=2N delta E_{0,t}(h).         (16)

Suppose a deterministic a_t satisfies, for every complex test h,

    |<F_t,h>_{mu_t}|<=a_t sqrt(E_{0,t}(h)).             (17)

By Cauchy-Schwarz in time, (15)-(17) imply

    V_F <= 2 sqrt(integral_a^b a_t^2 dt)
                 sqrt(integral_a^b E_{0,t}(u_t)dt)
        <= 2 sqrt(integral_a^b a_t^2 dt) sqrt(V_F/(2N delta)).

If V_F is nonzero, divide and square; the zero case is immediate. Thus

    E|integral_a^b F_t(eta_t)dt|^2
                  <= (2/(N delta)) integral_a^b a_t^2 dt.             (18)

This is the needed nonstationary estimate. It uses the actual forward law
and actual generator, including births that change the count sector.
There is no assumption that a path remains in a motion sector, no sector
condition on the nonreversible exchange part, and no frozen-time
stationarity approximation.

## 3. Current replacement along the growing product

Fix a scalar component g of an actual local exchange current. Let an odd
cube have side ell, M=ell^3 sites, and be much smaller than the torus.
Average g over all anchors whose complete support lies inside the cube,
normalizing by the number of such anchors. Call this G_ell. Let q^ell be
the six empirical occupied frequencies and set

    Phi_M(q^ell)=E[G_ell | block counts],
    Gtilde_ell=G_ell-Phi_M(q^ell).

At every t the block conditional law given its counts and its exterior is
uniform canonical. In particular Phi_M is independent of p(t), and
Gtilde_ell is conditionally centered at every time. This is a property of
the exact product law; it does not assert that the actual context generator
with a frozen exterior has canonical stationary laws.

The checked unit-swap Poincare inequality on the block is

    Var_canonical h <= P_M E_{0,block}(h),
    P_M=2M^2 7^M.                                    (19)

It follows by sorting a multiset along a nearest-neighbor Hamiltonian
path, using at most M^2 swaps and at most 7^M configurations in a sector.
Every internal unit swap is still controlled by the exchange floor.

For the normalized Fourier residual

    F_{N,ell}=V^(-1/2)sum_x exp(-iK.x/N)
                                      Gtilde_ell(translate_x eta),

conditional centering, (19), and Cauchy-Schwarz give at each t

    |<F_{N,ell},h>_{mu_t}|<=C sqrt(P_M M E_{0,t}(h)).    (20)

Indeed each block contribution is bounded by the square root of its
conditional variance times its local unit-swap form; summing translated
blocks counts every edge at most M times. The bounded current makes C
uniform over t in [0,T]. Combining (18) and (20),

    sup_{t<=T} ||integral_0^t F_{N,ell}(eta_s)ds||_2
                         <= C_T sqrt(M^3 7^M/N).       (21)

The same assertion holds after multiplication by bounded deterministic
time-dependent weights, by applying (18) with the corresponding a_t.

The other replacement terms need only one-time product estimates, which
remain exact here. Sampling a fixed local support with and without
replacement gives uniformly in all block counts

    |Phi_M(q)-J(q)|<=C/M.

Define the time-dependent Taylor residual

    R_{M,t}(q)=Phi_M(q)-J(p(t))-DJ(p(t))(q-p(t)).

The polynomial current has bounded Hessian on the simplex. Multinomial
fourth moments and conditional expectation give, uniformly in t,

    E_mu_t R_{M,t}=0,       E_mu_t |R_{M,t}|^2<=C/M^2. (22)

Disjoint blocks are independent at each time and a block overlaps O(M)
translates. Its normalized Fourier residual therefore has L2 norm at most
C/sqrt(M). Minkowski's inequality gives the same integrated bound times T;
no independence between different times is used.

Finally, spatial averaging is handled at fluctuation scale. If
G_N(K,t)=V^(-1/2)sum_x exp(-iK.x/N)[g(translate_x eta_t)-J(p(t))],
the exact Fourier filters of the anchor average and empirical block density
are scalars a_{N,ell}, b_{N,ell} with

    |a_{N,ell}-1|+|b_{N,ell}-1|<=C_K ell/N.

The normalized current field and Y_N have uniformly bounded one-time
variances under mu_t. For nonzero fixed modes their spatial constants
sum to zero. The exact decomposition is

    G_N-DJ(p(t))Y_N
       =(1-a)G_N+F_{N,ell}+DJ(p(t))(b-1)Y_N
          +V^(-1/2)sum_x exp(-iK.x/N)R_{M,t}(q^ell(x)).

Thus the full, actual current obeys

    sup_{t<=T} ||integral_0^t [G_N(K,s)-DJ(p(s))Y_N(K,s)]ds||_2
       <=C_{T,K}[ell/N+M^(-1/2)+sqrt(M^3 7^M/N)].      (23)

Taking ell tending to infinity with ell^3<=log(N)/(2log7) makes the bound
vanish. This reconstructs the missing nonstationary replacement step.
An equilibrium theorem is not being applied with an unproved adiabatic
substitution. In particular a configuration-uniform spatial averaging
bound would have the wrong central-limit scale and is not used.

## 4. Drift, surviving birth martingale, and L2 approximation

The exchange conservation identity and the negative Fourier convention give

    N H_N Y_N=sum_i N[exp(-iK_i/N)-1]G_{i,N}
             =-i sum_i K_i G_{i,N}+O_K(N^(-1))

in the integrated L2 sense, since current variances are uniformly bounded.
The birth drift is exactly linear after subtracting the trajectory (2):

    birth drift of Y_N=-beta 11^T Y_N=R Y_N.           (24)

This holds also for K=0, where the time derivative of the subtracted
mean cancels the constant birth source.

Split the compensated jump martingale into exchange and birth parts,
M_N^ex and M_N^b. Exchange changes a fixed nonzero Fourier field by
O(1/(N sqrt(V))) and has total rate O(NV). Therefore

    E sup_{t<=T}|M_N^ex(K,t)|^2<=C_{T,K}/N.            (25)

For K=0 the exchange part is identically zero. Births change one component
by exp(-iK.x/N)/sqrt(V), at rate beta if that site is vacant. Their
predictable conjugated brackets are exactly

    d<M_{N,a}^b(K),overline{M_{N,b}^b(L)}>_t
       =delta_ab (beta/V)sum_x exp[-i(K-L).x/N]
                                      1_{eta_t(x)=0}dt.               (26)

The unconjugated bracket uses K+L. Under the exact product mu_t, the
spatial average in (26) has mean p_0(t) times the appropriate Fourier
Kronecker delta and variance at most 1/(4V). Consequently its integrated
fluctuation is O(T/sqrt(V)) in L2. This estimate does not assume temporal
mixing. The surviving bracket is beta p_0(t)I_6, not six times this matrix;
the factor six appears only after summing labels to obtain density noise.

Combining (23)-(25), define the prelimit process

    Z_N(K,t)=Phi_K(t,0)Y_N(K,0)
                   +integral_0^t Phi_K(t,s)dM_N^b(K,s).              (27)

It solves the linear equation with drift D_K(t), the same initial field,
and the actual birth martingale. Subtract its equation from the exact
field martingale identity. Minkowski's inequality and Gronwall's inequality
give

    sup_{t<=T} ||Y_N(K,t)-Z_N(K,t)||_2
       <=C_{T,K}[N^(-1/2)+ell/N+M^(-1/2)
                                  +sqrt(M^3 7^M/N)] -> 0.            (28)

The supremum is outside the L2 norm. No sample-path maximal bound on the
replacement residual has been silently added. Equation (28) directly
suffices at finitely many modes and times.

## 5. Finite-mode Gaussian limit without an unproved noise closure

The initial fields have the joint Fourier central limit law of bounded
independent site variables, with conjugated covariance
`C(0) 1_{m=n}` and unconjugated covariance `C(0) 1_{m=-n}`. For a finite
fixed mode list, accidental finite-torus aliases disappear for large N.

For completeness the birth martingale Gaussian step can be obtained from
an elementary compensated-jump calculation. A real linear combination of
finitely many stochastic integrals appearing in (27) is

    Z_N^test=integral theta(t) dot dM_N^b(t),

with bounded deterministic weights, including the deterministic propagators
in (27) and time cutoffs. Each jump is O(V^(-1/2)); its total predictable
quadratic variation is bounded by a deterministic constant. Equation (26)
and its unconjugated counterpart make that bracket converge in L1 to a
deterministic number sigma^2.

If z denotes a possible real jump of this test martingale, its exponential
compensator is

    K_N=integral sum_{birth channels} rate
                                      [exp(iz)-1-iz]dt.

Taylor's formula gives

    K_N=-(1/2)<Z_N^test>+O(V^(-1/2))

with deterministic control on the remainder, because the integrated third
jump moment is bounded by the largest jump times the quadratic variation.
The compensated exponential `exp(iZ_N^test-K_N)` is a martingale with
initial value one; this follows by the conditional single-jump expansion.
Its modulus is uniformly bounded, since -Re K_N is bounded by half the
quadratic variation. Hence, for any bounded initial-measurable variable g_N,

    E[g_N exp(iZ_N^test)]-exp(-sigma^2/2)E[g_N] -> 0.    (29)

One can see this by replacing exp(K_N) in the martingale expectation by
its deterministic limit; the error tends to zero in L1 with a uniform
bound. Taking g_N to be an initial-field characteristic exponential and
using real linear combinations proves both the joint Gaussian martingale
limit and its independence of the limiting initial fields. The covariance
of those Gaussian noises is exactly (6).

This finite-dimensional characteristic-function argument, (27), and (28)
prove (5) jointly at the requested finite sets of modes and times. It
does not require a statement about tightness in an infinite-dimensional
field space.

## 6. Covariance, failure of deterministic transport, and extra fields

The exact product covariance satisfies

    Cdot=beta p_0[I_6-1p^T-p1^T].

The checked nonlinear entropy identity supplies
`A_i(t)C(t)=C(t)A_i(t)^T` at every interior p(t). Also
`R C+C R^T=-beta p_0(1p^T+p1^T)`. Therefore

    Cdot=D_K C+C D_K^*+beta p_0 I_6.                  (30)

This is the Lyapunov equation of (5). It verifies consistency with the
exact one-time product law and fixes the noise normalization. For t>=s,

    E[Y_K(t)Y_L(s)^*]
       =1_{m=n} Phi_K(t,s)C(s).                       (31)

Unconjugated covariance pairs opposite modes. There is no stationary
time-difference formula: both the background and the propagator vary
with time. At finite N the initial covariance and expected bracket in
(27) already give exactly the covariance generated by (30) for fixed
nonaliased modes. Cauchy-Schwarz and (28) thus also prove convergence of
the actual two-time covariances, without relying on a uniform-integrability
inference from convergence in law alone.

The stationary deterministic conclusion is genuinely false here. For t>0,
the difference from transport of the initial field has limiting covariance

    Q_K(t)=integral_0^t Phi_K(t,s)[beta p_0(s)I_6]
                                         Phi_K(t,s)^* ds.             (32)

This matrix is positive definite: p_0(s)>0 and Phi_K(t,s) is invertible.
Equation (28) and martingale isometry imply

    lim E|Y_N(K,t)-Phi_K(t,0)Y_N(K,0)|^2=trace Q_K(t)>0.

It is therefore incorrect to drop the noise and claim the old L2
deterministic transport law after merely changing A to A(t).

All six fields must be retained. At a balanced initial product in the
fixed axis-balanced witness u=0,E=1/2,A=2,B=-3, let
rho=rho(t), z_j=q_j-rho/3 and use the vector fields g_j=p_{+j}-p_{-j}.
The limiting fluctuation equations include

    dY_rho=[-i 2rho(1-rho) K dot Y_g-6beta Y_rho]dt+dM_rho,
    dY_g=-i(2rho/3)K Y_rho dt+dM_g,
    dY_z=dM_z.                                        (33)

Their instantaneous conjugated birth-noise covariances are

    d<M_rho,overline{M_rho}>=6beta p_0 dt,
    d<M_g,M_g^*>=2beta p_0 I_3 dt,
    d<M_z,M_z^*>=2beta p_0(I_3-11^T/3)dt,

with zero cross covariances between these groups. The two independent z
fields and two vector polarizations transverse to K have zero spatial
characteristic speed but receive birth noise. They are not frozen random
initial amplitudes. The density/longitudinal subsystem has reaction and
time-dependent coefficients, not the previous stationary cosine covariance.

In the old family, fixed u,E tuned at one density generally leave that
tuning as rho grows. The full matrix (3) remains the correct description;
one must not retune parameters while differentiating or suppress the
additional characteristic fields. Equation (33) is only the indicated
balanced-witness specialization of the general six-field theorem.

## 7. Independent complete-generator evidence and failed routes

The independently written checker constructs every one of the 7^4=2,401
states of a four-cycle, all allowed exchanges, and all birth transitions.
It uses acceleration 4, beta=1/3 and a full-support biased initial product
`p_0=1/2, p_a=a/42` for occupied indices a=1,...,6. It checks both rate
implementations for the old context model and the axis-balanced witness,
at three exact points on (2): exp(-6beta t)=1,1/2,1/4. This is a complete
directional finite-generator control of the energy identities; the proof
above, not this small graph, establishes the cubic-torus limit.

The completed run has **108 groups passed, zero failures**:

- 104 algebraic groups check the exact product forward equation, reverse
  birth rates and nonzero adjoint row sums, the score correction,
  evolving-measure energy and exchange-floor inequalities, and all six
  components of the one-time covariance, covariance derivative, drift
  and birth bracket. Integer edge arrays and rational arithmetic perform
  these identities.
- The stationary-energy shortcut fails on the complete generator exactly
  as in (12). At the initial product, `-E[uG u]=-1/21` for the +e1 count,
  whereas its bracket is positive. The time-ordering issue is also
  concrete: at K=2pi(1,2,-1), the drift matrices at survival factors 1
  and 1/2 have nonzero commutators in both checked families.
- A constant-rate context subfamily checks the exact finite-cycle
  Fourier drift `-8 I_6-beta 11^T` and exchange bracket `16 C(t)`.
  Thus finite-N exchange noise has not been declared identically zero;
  only its fixed-mode Euler scaling vanishes as in (25).
- Four numerical groups test the new additive-functional bound itself.
  For the axis-balanced positive-part generator, a nonzero Fourier
  current is centered in every one of the 210 count sectors. Solving
  the symmetric exchange Poisson equation in those sectors gives a
  maximum residual about 1.57e-15. A sparse, complete-state reward
  generator computes the second moment of its integrated current under
  the full growing process. The values at t=0.1,0.4,0.8 are respectively
  approximately 0.001089219, 0.012851571, 0.039490297; the nonstationary
  energy bounds are 0.002733854, 0.018677871, 0.052431896. The norm
  integrals use 24-node Gaussian quadrature. These are numerical
  controls of the proved inequality, not a numerical proof of it.

No calculation run failed. RUN.log preserves one SciPy FutureWarning
about the sparse diagonal's default integer-to-float storage conversion,
followed by the complete JSON results. The exact energy/covariance checks
use integer edge arrays, and all sparse row-sum values are exactly
representable integers. The warning did not change a check or its result.
RESULTS.json is the complete structured suffix of RUN.log, not a
byte-identical copy including that warning. All output is retained.

The unsuccessful mathematical shortcuts are explicit: treating the weighted
adjoint as a Markov reversal without its score correction, treating
`-<u,G u>` as stationary Dirichlet energy, using a frozen equilibrium
replacement without proof, or dropping birth noise. They are not used in
the proof. No primary calculation or outcome was accessed to resolve them.

## 8. Scope and source identities

The theorem is for fixed finite T, a fixed finite mode list, fixed rate
parameters/floor, fixed beta>0 and a fixed full-support homogeneous initial
product. The proof supplies finite-time joint laws and the L2 approximation
(28), whose supremum is outside L2. It makes no infinite-dimensional,
empty-initial-state, growing-time/mode, arbitrary correlated-initial-law,
vanishing-floor, boundary-density, or different birth-scaling assertion.
No microscopic wave, physical-field identification, audit or retention
verdict is attached. There is no unresolved proof gap under these stated
hypotheses.

Only the following unchanged sealed independent scientific sources were
used; the existing Euler report supplies canonical finite-block machinery,
not an inference from a law of large numbers to a fluctuation theorem.

| Relative sibling source | SHA-256 |
|---|---|
| independent_context_exchange/REPORT.md | 277ba40b64842d128a2e46ca7bd468a7efc7c4d401e629648d440588e7784713 |
| independent_context_exchange/PRE_SOURCE_SEAL.json | 7e924cc17d429c64ceb8e1b626f874dc6386ac2618ec7399af2879dce8f4d5f5 |
| independent_context_euler/REPORT.md | 60aaef142f97aea228be967a711880c5272328e5173d6c8df8c033176605a1e3 |
| independent_context_euler/PRE_SOURCE_SEAL.json | 48dda0ccb30539906dd6274bbf8736258727077c0018bb89c604f491164a1fa9 |
| independent_axis_balanced_context/REPORT.md | b9cedcafccb48dfcd2503e5f00569a547288d4dcef0fb7dfca832565aec8f7cf |
| independent_axis_balanced_context/PRE_SOURCE_SEAL.json | 8519e354a43ed16b9c176aa3e7e4672e6b3e6e1101e83af040555323aa3390a2 |
| independent_context_fluctuations/REPORT.md | 772046745ac814c32adcd8f36e3c8415ddf4a3a4b37435e8992441c6c8d5be68 |
| independent_context_fluctuations/PRE_SOURCE_SEAL.json | c729b0f85e0350b834380909001ef62f0db0378fdf114b108f5feef7f6e0e8d1 |

No external literature, primary growing-product source, simulation outcome,
publication draft or new admissibility-formation file was read. The
pre-source seal records every new artifact and the dependency identities.
