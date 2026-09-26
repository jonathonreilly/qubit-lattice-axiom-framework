# From the context-exchange generator to a smooth Euler profile

Primary derivation, 2026-09-21. A separate proof completed before access to
this source reaches the same smooth-profile conclusion and the same narrow
birth extension. Its full report and checker have been read, and all nine
sealed artifacts and four prior dependencies verified. See
`independent_context_euler/REPORT.md`, SHA
`60aaef142f97aea228be967a711880c5272328e5173d6c8df8c033176605a1e3`.
That proof uses a forward-current entropy calculation and an explicit crude
block Poincare constant; the primary derivation below uses the reverse-current
adjoint inequality. This is separate mathematical corroboration, not a formal
audit, retained-status decision or physical identification.

## 1. Precise target

Let V_N=(Z/NZ)^3, N>=4, with seven states 0,+/-e_1,+/-e_2,+/-e_3 and six
occupied indicator variables xi_a. On each positive-i nearest-neighbor edge,
exchange the two endpoint states at the context rate specified in
`CONTEXT_EXCHANGE_ACOUSTIC_DERIVATION.md`. Fix u,E and either

`c=K+h/2`, K>|u|+2|E|,

or `c=kappa0+max(h,0)`, kappa0>0.

The read footprint contains the four collinear sites x-e_i,x,x+e_i,x+2e_i.
Write 0<c_*<=c<=c^* for fixed uniform bounds. All parameters are independent
of N. Let L_N be the conservative generator at these microscopic rates;
the macroscopic-time process has generator N L_N. Its homogeneous product
stationarity and exact flux are already derived directly:

`J_a^i(p)=p_a[F(rho) v_(a,i)+G(rho) g_i]`,

`rho=sum_a p_a`, `p_0=1-rho`, `g=sum_a p_a v_a`,

`F=u+2E rho`, `G=(1-rho)F'-F`.

Assume p(t,X), X in the unit continuous three-torus, is a given C^2 periodic
solution on [0,T] of

`partial_t p_a + sum_i partial_i J_a^i(p)=0`,                     (1)

and every one of its seven probabilities is at least a fixed eta>0.
Define the inhomogeneous product reference nu_t^N with marginals p(t,x/N).
If the initial law mu_0^N obeys

`H(mu_0^N | nu_0^N)=o(N^3)`,                                    (2)

the target conclusion is

`sup_(0<=t<=T) H(mu_t^N | nu_t^N)=o(N^3)`.                       (3)

This implies convergence in probability of each empirical occupied-label
profile against a fixed continuous test function, at every fixed t in [0,T].
The theorem is about smooth profiles before a shock or loss of the assumed
interior bound. It does not assert global smooth solutions, shock selection,
or convergence of equilibrium fluctuation fields.

The argument below supplies the local-equilibrium step for this finite-range,
strictly positive exchange generator. It does not invoke an endpoint-only
hydrodynamic theorem as though its hypotheses already covered these rates.

## 2. A uniform reference and entropy dissipation

Let pi_N be the product with each of the seven labels equally likely. It is
stationary because the pointwise sum of the exchange-rate asymmetry h is
zero. For f_t=d mu_t^N/d pi_N, define the unweighted swap energy

`D_N(f)=sum_edges E_pi[(sqrt(f(eta^edge))-sqrt(f(eta)))^2]`.

The elementary inequality

`a log(b/a) <= 2 sqrt(a)(sqrt(b)-sqrt(a))`

and stationarity give

`d H(mu_t^N|pi_N)/dt <= -N c_* D_N(f_t)`.                        (4)

Indeed the right side before applying the rate floor is
`-N sum_edges E_pi[c(eta)(sqrt(f^edge)-sqrt(f))^2]` plus
`N sum_edges E_pi[c(eta)(f^edge-f)]`; the latter vanishes by stationarity.
The usual limiting convention handles zero f. Since the finite state space
has 7^(N^3) configurations, H(mu_0^N|pi_N)<=N^3 log 7 and H>=0. Thus

`integral_0^T D_N(f_t) dt <= N^3 log(7)/(N c_*)`.                (5)

No quantitative large-block spectral-gap theorem is needed in the order of
limits used below: first N tends to infinity at a fixed block size, then the
block size grows.

## 3. The finite-block mixing step

Take a cube B_l={-l,...,l}^3 with M=(2l+1)^3 sites, l>=4, and N>4l.
Let g_B be the density of a block marginal with respect to the uniform
seven-category product pi_B. Condition pi_B on its seven label counts.
Each such conditional law is uniform on all arrangements with those counts.

Internal nearest-neighbor swaps connect every arrangement in a fixed-count
sector: adjacent transpositions on a connected finite graph generate all
permutations. There are finitely many sectors for fixed l. Consequently a
finite constant A_l exists, uniform over those sectors, with

`E_pi_B Var(sqrt(g_B) | counts) <= A_l D_B(g_B)`.                 (6)

D_B sums the unweighted square-root swap differences on internal block
edges. One-point sectors contribute zero. This is the elementary positive
gap of a finite connected symmetric chain in each sector, followed by a
maximum over the finitely many sectors; no bound on A_l as l grows is used.

Let tilde mu_B have the same count distribution as mu_B and be uniform
within each count sector. Its density is h=E_pi_B[g_B|counts]. The squared
Hellinger distance satisfies

`E_pi_B[(sqrt(g_B)-sqrt(h))^2]`

` <= 2 E_pi_B Var(sqrt(g_B)|counts) <= 2 A_l D_B(g_B)`.

The first inequality follows, sector by sector, from 1-z<=1-z^2 for
z=E[sqrt(g_B/h)|counts] in [0,1]. Cauchy-Schwarz then bounds the L1
distance of the two block probability laws by

`||mu_B-tilde mu_B||_1 <= 2 sqrt(2 A_l D_B(g_B))`.                (7)

For a global density f, marginalization contracts this swap energy:

`D_B(g_B) <= sum_(edges inside B) E_pi_N[(sqrt(f^edge)-sqrt(f))^2]`.

For each internal edge this is the reverse triangle inequality for the
L2 norms of sqrt(f) and sqrt(f^edge) over outside configurations, with the
inside configuration fixed. Thus averaging over translated blocks counts
each global edge at most M times.

## 4. Canonical block averages and one-block replacement

For a positive-i edge put

`j_i^rev(eta)=c_i(eta^edge)[xi(eta_x)-xi(eta_(x+e_i))]`,

a bounded six-vector depending on four distinct sites. Its product mean is
`-J_i(p)`, by swapping the endpoints in the product expectation. Average
this local variable over centers in B_(l-2), so its complete read footprint
lies in B_l. Denote the average by bar j_(i,l), and let bar xi_l be the
occupied count vector divided by M.

Under a uniform fixed-count block law with empirical probabilities q, any
r fixed distinct positions are a sample without replacement from that
multiset. Couple this to sampling with replacement: the probability that
the r sampled indices repeat is at most r(r-1)/(2M). Hence the expectation
of any bounded r-site function differs from its product expectation at q
by O(1/M), uniformly even at the boundary of the probability simplex.

Apply this with r=4 and r<=8. Pairs of translated read footprints overlap
for only O(M) pairs of centers. For disjoint footprints, the without-
replacement coupling bounds their covariance by O(1/M). The variance of
the block average is therefore O(1/M), uniformly in the counts. Since the
number of inner centers is comparable to M for l>=4, this proves

`E_canonical |bar j_(i,l)+J_i(bar xi_l)| <= C/sqrt(M)`.           (8)

Combining (7)-(8), applying Cauchy-Schwarz over time and block translations,
and using (5), gives

`(1/N^3) integral_0^T sum_x`

` E_mu_t |tau_x bar j_(i,l)+J_i(tau_x bar xi_l)| dt`

` <= C T/sqrt(M) + C sqrt(A_l T M log(7)/(N c_*))`.              (9)

C depends on the bounded local current and finite footprint, not on l,N or
the count values. Thus the left side tends to zero as N tends to infinity
and then l tends to infinity. This is an actual local-equilibrium estimate
for the process law; spatially varying products have not been assumed to
remain products. The energy estimate uses the uniform swap floor to avoid
any separate assumption about the original context rates on a block boundary.

## 5. Relative-entropy expansion and its cancellation

Write chemical coordinates theta_a=log(p_a/p_0), C=diag(p)-p p^T,
H=C^(-1), and A_i=partial J_i/partial p. Direct differentiation of

`Psi_i(theta)=F(rho(theta)) g_i(theta)`

gives `partial Psi_i/partial theta_a=J_a^i`. Consequently `A_i C` is
symmetric, equivalently `H A_i=A_i^T H`. For the smooth solution (1),

`partial_t theta = -sum_i A_i^T partial_i theta`.                (10)

Let psi_t=d nu_t^N/d pi_N and H_N(t)=H(mu_t^N|nu_t^N). The logarithmic
inequality log z<=z-1, applied to the Markov relative-entropy derivative,
gives

`H_N'(t) <= E_mu_t [N L_N^* psi_t/psi_t - partial_t log psi_t]`.  (11)

The adjoint is with respect to pi_N. For an endpoint swap e=(x,x+e_i),

`psi(eta^e)/psi(eta)`

` = exp{[theta(t,(x+e_i)/N)-theta(t,x/N)]`

`             dot [xi(eta_x)-xi(eta_(x+e_i))]}`.

The zero-order adjoint term is `sum_e[c(eta^e)-c(eta)]=0` pointwise.
Taylor expansion of the exponential and of the smooth chemical coordinate
therefore yields, uniformly in the configuration and t in [0,T],

`N L_N^*psi/psi = sum_(x,i) partial_i theta(t,x/N) dot j_i^rev(tau_x eta)`

`                  + O(N^3/N)`.                                (12)

The local read context changes c(eta^e), but does not change the product
Radon-Nikodym ratio. Also, exactly,

`partial_t log psi = sum_x partial_t theta(t,x/N)`

`                              dot [xi(eta_x)-p(t,x/N)]`.        (13)

Replace the currents in (12) and densities in (13) by their block averages.
Moving their smooth coefficients over O(l) sites costs O(l N^3/N).
Use (9) in the time integral. The resulting expression has, up to an error
whose integral is o(N^3) in the stated successive limits,

`sum_x { -sum_i partial_i theta dot J_i(bar xi_l)`

`         -partial_t theta dot [bar xi_l-p] }`.                  (14)

Expand J_i at p. The deterministic term
`-sum_(x,i) partial_i theta dot J_i(p)=-sum_(x,i) partial_i Psi_i(theta)`
has spatial integral zero on the continuous torus; its discrete Riemann sum
is O(N^3/N). The terms linear in bar xi_l-p cancel by (10). The flux J is
a polynomial with bounded second derivatives on the closed probability
simplex, so the remaining expression is bounded above by

`C sum_x |tau_x bar xi_l-p(t,x/N)|^2`.                           (15)

## 6. The quadratic-block entropy estimate

Under nu_t^N the sites are independent, though their marginals vary. The
block's actual mean differs from p(t,x/N) by O(l/N). For a bounded
categorical sample, Hoeffding's inequality and a union bound over six
coordinates imply, for a sufficiently small fixed b>0,

`E_nu exp{b M |bar xi_l-E_nu bar xi_l|^2} <= C_b`,                (16)

uniformly in M, the site probabilities and t. For completeness, the tail of
M times the squared six-vector norm is bounded by 12 exp(-z/3), using that
one coordinate must exceed sqrt(z/(6M)); integrate this tail against
b exp(bz) with b<1/3.

The translated cubes can be colored into at most a constant times M classes
of disjoint cubes: their overlap graph has degree O(M). Use a fixed such
number of colors, allowing empty classes, and apply Holder's inequality
over classes. Independence within a class and (16), with a sufficiently
small fixed a>0, then give

`log E_nu exp{a sum_x |tau_x bar xi_l-p(t,x/N)|^2}`

` <= C N^3/M + C N^3 l^2/N^2`.                                 (17)

This coloring argument covers arbitrary sufficiently large N; divisibility
of N by the block side is unnecessary. The entropy inequality now yields

`E_mu sum_x |tau_x bar xi_l-p(t,x/N)|^2`

` <= a^(-1) H_N(t)+C N^3/M+C N^3 l^2/N^2`.                     (18)

Combine (9), (11)-(18) and integrate. For each fixed block radius l,

`H_N(t)/N^3 <= H_N(0)/N^3 + C integral_0^t H_N(s)/N^3 ds`

`                  + C_T/sqrt(M)+C_T/M+o_N(1)`,                 (19)

uniformly in t<=T. The Gronwall coefficient C does not grow with l: the
entropy-exponential parameter in (17) is fixed. The block gap A_l appears
only in o_N(1). Gronwall, first N to infinity and then l to infinity,
proves (3).

Under the reference product, bounded empirical test averages have
exponentially small deviation probabilities, with exponent proportional
to N^3, and their means are Riemann sums of the prescribed p profile.
The binary-event entropy inequality transfers these bounds to mu_t^N
because H_N(t)=o(N^3). Continuous test functions follow by uniform smooth
approximation. This proves the stated empirical-profile consequence.

## 7. Narrow reaction extension and its scaling

Now add a birth of each occupied label at each vacant site at *microscopic*
rate epsilon/N, with fixed epsilon>=0. At macroscopic time the generator is
`N L_N + R_N`, where R_N gives each label rate epsilon. The target equation is

`partial_t p_a+sum_i partial_i J_a^i(p)=epsilon p_0`.             (20)

The proof changes in two explicit places. First, the absolute-reference
entropy derivative for the birth part is at most `E_mu R_N^*1<=epsilon N^3`:
the local adjoint applied to one is epsilon at an occupied state and
-6epsilon at vacancy. Thus (5) holds with log7 replaced by log7+epsilon T.
The one-block replacement is unchanged.

Second, for the inhomogeneous product reference, `R_N^*psi/psi` is exactly
the portion of `partial_t log psi` generated by the independent birth
equations. Locally it is epsilon p_0/p_a at occupied label a and -6epsilon
at vacancy. Those contributions cancel pointwise in (11). The transport
part of (10) and the remainder of the proof apply to the smooth interior
solution of (20). This proves the same relative-entropy conclusion for
this particular reaction scaling.

A fixed positive microscopic epsilon is a different limit. On time Nt,
its homogeneous vacancy fraction is `p_0(0) exp(-6epsilon Nt)` and vanishes
for every fixed positive macroscopic t. Such a sequence cannot be described
by (20) with finite epsilon. In particular, continuing fixed-rate insertion
cannot silently be treated as a stationary interior acoustic background.

## 8. What the tuned acoustic statement would then mean

For epsilon=0 and an interior rho_*, choose u=-2E rho_*, E!=0. The proved
current linearization about p_a=rho_*/6 is

`partial_t delta rho+2E rho_*(1-rho_*) div delta g=0`,

`partial_t delta g+(2E rho_*/3) grad delta rho=0`,

`partial_t delta Q_traceless=0`.

It gives `partial_t^2 delta rho=c_s^2 Laplacian delta rho`,
`c_s^2=4E^2 rho_*^2(1-rho_*)/3`. Given a smooth interior nonlinear solution
family differentiable in an initial perturbation parameter, (3) followed
by that derivative identifies an iterated macroscopic-profile / small-
amplitude wave limit. For an initial density cosine and zero vector and
quadrupole perturbations, the linear density profile is the same spatial
cosine times cos(c_s |k|t).

This is a smooth-profile assertion with ordered limits. It does not prove
the equilibrium fluctuation spectrum, the damping coefficient fitted from
finite simulations, a relativistic field, an axiom-selected speed, or a
mechanism keeping the growing system at its tuned density. The premises are
the supplied context rate, the fixed positive swap floor, and the specified
scaling and profile regularity. Independent scrutiny must check the argument
before this candidate is promoted to a publication theorem.

## 9. Method and source boundary

The proof uses the established relative-entropy method. Toth and Valko's
[primary paper, arXiv:math/0210426v2](https://arxiv.org/abs/math/0210426v2)
provides the relevant multi-conservation-law context and emphasizes the
current-susceptibility symmetry. Its displayed microscopic rates depend on
the two updated sites; that theorem is not directly applied here. The
four-site block argument, all dimension-three bookkeeping, and the exact
birth cancellation are written above for this generator. No novelty claim
is made for the general method or for hydrodynamic limit theory.
