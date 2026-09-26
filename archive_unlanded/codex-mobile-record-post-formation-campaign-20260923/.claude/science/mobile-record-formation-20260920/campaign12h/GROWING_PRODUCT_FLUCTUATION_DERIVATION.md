# Formation noise and the growing-product Euler fluctuation limit

Primary proof, 2026-09-21. The separate pre-source reconstruction agrees. This is a
new nonstationary argument, not a consequence of the smooth-profile theorem
or an unchecked extension of the stationary fluctuation statement.

## 1. Model and intended conclusion

On the N^3 periodic lattice, use a fixed bounded finite-range immutable
nearest-neighbor exchange generator L_N with a fixed positive swap floor.
Every homogeneous seven-state product is invariant for its conservative
part. Its six occupied-species mean currents J_i(p) are C^2 on the closed
probability simplex and satisfy A_i C=C A_i^T, where A_i=D J_i and
C=diag(p)-p p^T. The checked four-site constructions satisfy these premises.
The polynomial realization is a further candidate, pending its own check.

On macroscopic time use generator N L_N+R_N, with R_N giving each of the
six birth labels rate beta>0 at a vacant site. Thus its microscopic birth
rate is beta/N. Start with an independent homogeneous full-support product.
Its law is exactly product at every time, with

`p_0(t)=p_0(0) exp(-6 beta t)`,
`p_a(t)=p_a(0)+[p_0(0)-p_0(t)]/6` for a=1,...,6.                (1)

Fix T<infinity. All seven probabilities have a positive lower bound on
[0,T]. Let V=N^3, K=2 pi m for a fixed integer mode, and

`Y_N(K,t)=V^(-1/2) sum_x exp(-i K.x/N)[xi_x(t)-p(t)]`.

The proposed finite-dimensional limit is the Gaussian linear equation

`dY(K,t)=B_K(t) Y(K,t) dt+dW(K,t)`,                            (2)
`B_K(t)=-i sum_i K_i A_i(p(t))-beta 11^T`,

where the real-space birth noise has species covariance

`Q(t)=beta p_0(t) I_6`.                                       (3)

For nonzero distinct fixed modes, Fourier orthogonality gives
`E[dW(K)dW(K')^*]=delta_(K,K') Q(t)dt`; without conjugation use
`delta_(K,-K')`. Opposite modes are complex conjugates. At K=0 the field is
real. The initial Gaussian field has covariance C(0), and the limiting
noise is independent of it. If M_K(t,s) is the propagator of B_K, then

`E[Y(K,t)Y(K,s)^*]=M_K(t,s) C(s)`, t>=s.                       (4)

The result is for any finite collection of fixed modes and times. It does
not yet claim tightness in a field-valued path topology, a finite-size error
rate, fixed microscopic formation rate as N grows, or an empty initial law.

## 2. A nonstationary forward/backward energy identity

Let a finite-state chain have forward generator G_t and strictly positive
law nu_t solving the forward equation. Its physical reverse generator at
the same forward time has off-diagonal rates

`G_t^rev(x,y)=nu_t(y) G_t(y,x)/nu_t(x)`.

It is a Markov generator, with diagonal set by its off-diagonal row sum.
It is not simply the L2(nu_t) adjoint: the latter has the additional
multiplication operator `(d nu_t/dt)/nu_t`. This distinction is essential.

The operator S_t=(G_t+G_t^rev)/2 IS a reversible Markov generator under
nu_t: its edge conductances are the average of the two directed fluxes.
For a smooth centered family F_t, solve `-S_t u_t=F_t` in the orthogonal
complement of its kernel. In the application beta>0 and full support make
S_t irreducible; finite-dimensional smooth dependence gives a smooth u_t.

The forward martingale uses `(partial_t+G_t)u_t`. Over a reversed path its
terminal backward martingale uses `(-partial_t+G_t^rev)u_t`. Their sum is
exactly

`M_t+Mhat_t=2 integral_0^t F_s(eta_s) ds`.

The endpoint terms and both time derivatives cancel. Moreover, reversing
the two indices in the edge sum shows

`E_nu_s Gamma_(G_s)(u_s)=E_nu_s Gamma_(G_s^rev)(u_s)`
`                         =2 <u_s,-S_s u_s>_nu_s`.

The elementary square bound on M+Mhat therefore gives

`E |integral_0^t F_s(eta_s)ds|^2`
` <=2 integral_0^t ||F_s||_(-1,S_s)^2 ds`.                      (5)

This is a finite-state identity and bound. Stationarity was not assumed;
using the uncorrected adjoint in the reversed path would be an error.
Real and imaginary parts can be handled separately.

## 3. Why fast exchange still gives current replacement

For G=N L_N+R_N under (1), reverse exchanges have rate c(eta^edge), because
all homogeneous product configuration weights are invariant under swaps.
The reverse of birth 0->a is death a->0 at rate beta p_0(t)/p_a(t).
Consequently

`S_t=N S_exchange+[R_N+R_N^rev(t)]/2`,

and its Dirichlet form dominates the N-accelerated exchange form. Its
exchange part has the same positive floor and fixed-count block comparison
as in the stationary proof.

For a fixed block of M=(2l+1)^3 sites containing a current's footprint,
let hat j_l be the conditional current average given its seven counts.
This function does not depend on t or p: a product conditioned on counts
is the same uniform arrangement law. Put h_l=j-hat j_l. Its conditional
mean given the outside and the block counts is zero at every time.

For bounded deterministic coefficients a_x(s), the finite-sector Poincare
comparison and block-overlap counting give, uniformly for s<=T,

`||V^(-1/2) sum_x a_x(s) tau_x h_l||_(-1,S_s)^2`
` <=C A_l M/(N c_*)`,                                         (6)

where A_l<infinity is a block comparison constant and c_*>0 the fixed floor.
Adding the birth Dirichlet form only decreases this variational norm.
Apply (5) to (6), first for smooth coefficients; the Fourier and propagator
weights used below are smooth. This controls the time integral in L2.

Uniform finite-population sampling gives hat j_l=J(q)+O(1/M), with q the
block occupied frequencies. Taylor expansion at the evolving p(s) leaves

`W_l(s)=hat j_l-J(p(s))-A(p(s))[q-p(s)]`.

At EACH time, its mean is zero and its variance is O(1/M^2), because the
actual law is product. Disjoint blocks are independent at that time;
translated-block overlap gives variance O(1/M) for the normalized spatial
sum. Cauchy-Schwarz in time then gives an O(T^2/M) integrated bound. No
independence between different times is used.

Replacing block-averaged indicator fields by their Fourier mode adds
O(T^2 l^2/N^2), since their instantaneous variances are bounded. Thus the
stationary replacement estimate extends, now with A evaluated at p(s):

`sup_(t<=T) E |integral_0^t [Z_i,N(K,s)-A_i(p(s))Y_N(K,s)]ds|^2`
` <=C_T [A_l M/(N c_*)+1/M+l^2/N^2]`.                          (7)

For K=0 subtract the constant current from Z; its spatial divergence is
zero anyway. First let N grow at fixed l, then let l grow. Smooth bounded
matrix-valued propagator weights are also allowed directly in (5)-(6),
or by integration by parts on (7).

## 4. Birth fluctuations remain after exchange noise vanishes

The exact Fourier martingale equation has exchange coefficient
b_i,N=N(exp(-i K_i/N)-1), the exactly linear birth drift -beta 11^T Y_N,
and a martingale decomposed into exchange and birth jumps.

Each exchange jump is O(1/(N sqrt(V))) and its accelerated total intensity
is O(NV). Its expected bracket on [0,T] is therefore O(1/N), so it vanishes
in L2. A birth of species a contributes `exp(-iK.x/N)e_a/sqrt(V)`. Its
predictable cross-mode bracket is exactly

`d<M_a(K),overline(M_b(K'))>_t`
` =delta_ab beta V^(-1) sum_x exp[-i(K-K').x/N] 1_(eta_x=0) dt`.

At each time, product independence makes the centered spatial average have
variance at most 1/V. Time integration preserves convergence in L2. The
bracket therefore converges to (3) with the stated mode Kronecker deltas.
The maximum birth jump tends to zero as V^(-1/2).

For completeness, the required finite-dimensional martingale central limit
step can be obtained by expanding the conditional exponential at each jump:
for any finite real linear combination of real/imaginary modes, the
third-order Taylor remainder is at most C V^(-3/2) per jump, while total
birth intensity is O(V). Its integrated expectation is O(V^(-1/2)). The
quadratic term is the bracket above, whose compensator converges to a
deterministic time integral in L2. Applying the exponential martingale
identity successively on finitely many time intervals identifies centered
Gaussian increments with that covariance. A bounded function of the initial
configuration can be retained as a multiplier throughout, giving stable
independence of these increments from the limiting initial Gaussian field.
The initial independent bounded triangular-array Fourier sums satisfy the
ordinary Lindeberg CLT.

Variation of constants with
B_N(t)=sum_i b_i,N A_i(p(t))-beta 11^T and the weighted version of (7)
removes the nonlinear current remainder. B_N converges uniformly on [0,T]
to B_K; its propagators and derivatives are uniformly bounded. The birth
martingale with deterministic propagator weights obeys the same bracket
and Taylor argument. This proves the finite-dimensional assertion (2),
provided the preceding energy/replacement steps survive separate scrutiny.

## 5. A consistency identity that catches a missing source noise

From (1),

`C'(t)=beta p_0 I-beta p_0(1 p^T+p 1^T)`.

Since 1^T C=p_0 p^T and A_i C=C A_i^T,

`B_K C+C B_K^*+Q=C'`.                                         (8)

Thus the covariance of (2) is exactly the instantaneous product covariance
C(t). Omitting Q would contradict the known microscopic one-time law.
Equation (4) follows by propagating between s and t and using independent
future Gaussian increments. In particular, two-time response M C(s) can
be compared with simulations without pretending the growing process is
stationary or fitting a stationary sound speed.

For the axis-balanced rule, along an isotropic evolving product the density
and longitudinal vector response close at every time:

`d delta rho/dt=-6 beta delta rho-i |K| 2alpha rho p_0 delta g_L`,
`d delta g_L/dt=-i |K| (2alpha rho/3) delta rho`.

Birth noise projected onto these fields has
Q_rho,rho=6 beta p_0, Q_g_i,g_j=2 beta p_0 delta_ij, and Q_rho,g_i=0.
Four additional zero-speed exchange modes remain and also acquire their
appropriate formation noise. They have not been discarded from (2).

## 6. Scope and next checks

This mechanism allows new records to form while microscopic density
correlations have a controlled transient wave limit, if this proof is
confirmed. It does not give permanent waves at a fixed nonzero microscopic
birth clock: then beta=N epsilon diverges in this scaling, outside the
fixed-T, fixed-beta argument. Full occupancy is approached as t grows, and
this rule's sound coefficient tends to zero.

A completely empty start is outside the full-support proof at t=0. At any
strictly positive macroscopic time its exact homogeneous law is interior,
so the same argument can start there for correlations between later times.
A theorem covering the initial boundary layer needs separate treatment.
The clock, polynomial current potential and parameters remain supplied,
and this classical fluctuation theorem would not establish quantum,
relativistic or gravitational dynamics.


## Separately reconstructed proof and a simpler energy route

The complete independent report and checker in
`independent_growing_fluctuations/` were read, and all nine artifacts and
all eight dependencies were hash-verified. Report SHA
`168ae65623d124f2aa10a0c215c75e8767950f7fb1c50fc5a3fc287f1667b1dc`;
seal SHA `c86eba9af78a19fbeb92782f521bb9ed43553f078adf638c4ca846e6b9ee6286`.
It reconstructs the same stochastic limit before seeing this primary proof,
using complete2401-state controls and a different energy argument. This is
not a publication-source review, audit or retained-status verdict.

The following alternative is reconstructed from that report after its seal.
It can replace the reversed-path Poisson step above. For an exact evolving
finite-state law mu_t and generator G, solve the terminal backward equation
(partial_t+G)u_t=-F_t, u_b=0. The derivative of E_mu_t|u_t|^2 is
2Re E[bar u_t(partial_t+G)u_t]+E Gamma_G(u_t), with the measure derivative
already included through the forward equation. Dynkin's martingale gives
integral_a^b F_t(eta_t)dt=u_a(eta_a)+M_b, E[M_b|eta_a]=0. Consequently

    E|integral_a^b F_t(eta_t)dt|^2
      =E|u_a|^2+integral_a^b E Gamma_G(u_t)dt
      =2Re integral_a^b <u_t,F_t>_mu_t dt.

If |<F_t,h>_mu_t|<=a_t sqrt(E_0,t(h)) for every h, and the exchange floor
implies E Gamma_G(h)>=2N c_* E_0,t(h), Cauchy-Schwarz followed by division
by the square root of the left side gives the explicit bound

    E|integral_a^b F_t(eta_t)dt|^2
           <=2/(N c_*) integral_a^b a_t^2 dt.

The zero case needs no division. This route includes the initial random
term and does not require irreducibility of the birth generator. For the
current residual, exact instantaneous product laws give the needed canonical
centering and Poincare bound with a_t^2<=C A_l M. The remainder of the
current replacement and the surviving birth-martingale argument are unchanged.
This alternative does not supply the same centering for neighbor-dependent
births, whose law is not an exact product; that extension remains separate.
