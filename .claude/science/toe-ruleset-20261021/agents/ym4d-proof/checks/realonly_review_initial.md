# REALONLY — real estimates at the RG consumer interfaces

**Real estimates suffice for the named downstream quantities and reconstruction
inputs, conditional on the explicit bounds below. Those actual-model bounds
remain OPEN. CHARGE does not close the RG core even on its real section.**
Local reference matching, complete-reader sums and coherent continuation still
need estimates. The existing holomorphic RG norm cannot be certified by
restricting its supremum to real fields; a replacement real-derivative
induction is a different, presently unconstructed contract.

PROVEN denotes a written implication or finite identity with its hypotheses;
ARGUED denotes a proposed application; OPEN denotes an unsupplied actual
Wilson/Decision-4 estimate. REAL-SUFFICES classifies a consumer implication,
not verification of its real hypotheses. COMPLEX-NEEDED means needed by the
explicitly named existing proof/domain, not by every possible RG proof.
There is no new audit status, Yang–Mills existence or mass-gap claim.

Credit: Tadeusz Balaban for the large-field RG organization and Jonathan
Dimock for [Large fields](https://arxiv.org/abs/1212.5562) and
[Convergence](https://arxiv.org/abs/1304.0705). Their primary abstracts concern
scalar theory in dimension three. They supply attribution only. The
elementary replacements used here are rebuilt below; no recalled [m]
assertion carries weight. [REALONLY_LOG.md](REALONLY_LOG.md) records source
identities, read coverage and the independent review.

## 1. Consumer verdicts

The supplied mathematical model is finite periodic SU(N), N>=2, odd L>=3,
probability Haar and the exact normalized soft kernels. These are not
derived physical axioms. Original observable/action sources vary with every
RG kernel and normalizer fixed unless a different differentiation problem
is explicitly specified. Uniformity must cover the consumer's cutoffs,
volumes, levels, histories, supports and real tilt window.

| Consumer | Exact consumed quantity and real replacement | Verdict; actual producer |
|---|---|---|
| H_reg / OS0, E0′ | One all-n triple (s,alpha,beta) controlling distributions on collision-flat tests. Unconditional separated moments (R8), or complete outer-cumulant bounds (R9), give this by §4. | **REAL-SUFFICES — PROVEN implication. OPEN** actual hierarchy. Raw uniform same-test MGFs are not an available shortcut. |
| PL-1L / WITNESS | Real summed second-cumulant matching E11, or the summable per-scale E12, including terminal covariance, correct normalization and running u (WITNESS:505–594). Real degree-two errors suffice. | **REAL-SUFFICES — PROVEN implication. OPEN** actual quantum matching. |
| K4MATCH | All 15 nonempty four-source jets, including triples (K4MATCH:149–183). Its complex 4-SRC-ERR is used to bound a derivative of a small error (:305–360). Real fourth-jet errors or R5–R6 suffice. | **REAL-SUFFICES — PROVEN implication. OPEN** actual four-point matching. |
| H_Euc, flat TQ2 | Extensive real sources for each whole product; NC + PC + COMMON (TQ2:284–390), or its moving-radius version. Real convex secants suffice. | **REAL-SUFFICES — PROVEN implication. OPEN** no-cusp, comparison and hierarchy inputs. |
| H_Euc, sphere N5B | Actual-law real image moments, summed conditional covariance and seam transparency, plus BULK/ALG (N5B:153–214,475–526). | **REAL-SUFFICES — PROVEN implication. OPEN** actual estimates; they are not thereby UV-only. |
| REC / OSLEAF | The same S_n obeying E0′, E1–E3, reality and S0=1 (OSLEAF55:213–248). Its Hilbert/semigroup part needs less regularity. No inverse source partition function is consumed. | **REAL-SUFFICES — PROVEN interface implication. OPEN** YM seed. Complex spacetime continuation remains part of reconstruction. |
| Coupling bracket/tuning | Real curvature Hessian, weighted spatial sum, real remainder bounds and continuity (FLOW:155–171,409–455). Direct real derivative estimates replace Cauchy. | **REAL-SUFFICES — PROVEN implication. OPEN** finite-coupling/LF/volume producers and FI-1. |
| Flow/source response | Real variational derivative bounds with a strict uniform margin replace the scalar Cauchy step of SRCAN SA-F. Spatial source response needs its own local operator bounds. | **REAL-SUFFICES — PROVEN scalar implication; OPEN** spatial response and LOC-e. |
| Literal complex RG contract | RD4/LF-JMBR/STEP55 asks for bounds on nonreal original sources and coarse fields; its contour, holomorphic-log and maximum-principle arguments use those domains. | **COMPLEX-NEEDED for the unchanged contract. OPEN** whether §7's real induction can replace its complete producer. |

Distinguish (i) original/observable sources, (ii) complex coarse group/chart
fields, (iii) bond/decoupling parameters producing spatial locality,
(iv) an auxiliary activity-counting parameter in a graph series, and
(v) complex spacetime in OS continuation. Removing (i) from a consumer
does not establish (ii)/(iii) or remove conclusion (v). Auxiliary (iv)
does not require an estimate at complex physical sources.

## 2. Real exponential moments and denominators

### R-MOM — PROVEN

Let mu be a probability law and X_i real random variables. Assume r>0,
M>=1, p_i>0 and, for each i,

    E exp( r X_i/p_i)<=M,    E exp(-r X_i/p_i)<=M.        (R1)

Put A=2M. Positivity gives E exp(r|X_i|/p_i)<=A. Since
y^n<=n! exp(y) for y>=0, followed by Holder with n equal exponents,

    E|X_i|^n <= A n! (p_i/r)^n,
    E product_(i=1)^n |X_i| <= A n! r^-n product_i p_i. (R2)

For multiplicities alpha_i summing to n the same Holder proof gives
A n! r^-n product p_i^alpha_i. Zero-scale directions can instead be
assumed to have X_i=0 almost surely. Independence is not needed.

The moment-cumulant formula gives

    |kappa_n(X_1,...,X_n)|
      <= n! r^-n product_i p_i
           sum_(k=1)^n [A^k/k] binom(n-1,k-1)
      <= n! A(1+A)^(n-1) r^-n product_i p_i.             (R3)

Indeed the sum of product_B |B|! over unordered k-block partitions is
n! binom(n-1,k-1)/k!: order the blocks, sum positive compositions, then
divide by k!. Multiplication by (k-1)! gives R3. The cumulant formula
itself follows by expanding log(1+w) in the finite ring t_i^2=0;
the coefficient of t_1...t_n needs only finitely many terms. Thus no
complex log branch is used. Real exponential domination identifies
these finite coefficients with derivatives.

The proof applies under each positive real tilted/conditional law if R1
is uniform there. A bound separately at each tilt does not control the
expectation of a supremum over tilts, nor outer products of conditional
cumulants. Those extra inputs remain explicit.

### R-ZERO — PROVEN, a smaller source ball

Real estimates can also derive some complex analyticity. For finitely
many X_i satisfying R1 set a(z)=sum_i |z_i|p_i/r. For 0<a<=1 write
Y=sum_i w_i r|X_i|/p_i with w_i=|z_i|p_i/(ra). Holder gives E exp(Y)<=A.
Convexity gives exp(aY)-1<=a(exp(Y)-1), hence

    |E exp(sum z_i X_i)-1| <= a(z)(A-1).                (R4)

On interior subdomains the same envelope dominates the exponential
series and proves holomorphy. Thus a(z)<1/[2(A-1)] is zero-free and the
normalized complex measure has TV<=2A. The case a=0 is immediate.
At any other real base tilt the hypotheses must hold under that tilted
law. This is an l1-type source ball for this particular normalized MGF,
not a local support expansion or the required fixed coefficient polydisc
and coarse tube. For d directions with p_i=1 the polydisc certified
this way has radius O(1/d). No actual zero is asserted at that radius.

Positivity alone gives much less: a fair variable X=+B or -B has MGF
cosh(Bz), positive on the whole real line but zero at i*pi/(2B). It
lacks uniform R1 as B grows, so this does not contradict R4.

### The clover/contact restriction

SRCCD55 Lemma V (:215–281, corrected remainder :926–927) gives on its
specified even tori and weak-coupling range

    Var O_a(f) >= c g_0^4 a^-4 (||f||_2^2-O_f(a)), c>0.

This diverges along the stipulated logarithmic trajectory. Uniform R1
for O_a(f)-c_a(f) would bound its variance by 2A p(f)^2/r^2, independently
of deterministic centering. It therefore cannot hold in that scope.
A uniform conditional bound for every coarse field with the same
deterministic centering also bounds the unconditional second moment
after integration. This preserves CODEX_REVIEW_SRCAN §1/E8's warning
in real form, without extending it to the sphere or other normalizations.

Local contact counterterms can disappear from separated mixed
derivatives if their range is smaller than the support separation.
However, subtracting a nonlinear source counterterm from log Z does
not generally leave a positive log-MGF. Positivity, Holder and R1 cannot
be applied to that new object without another representation. Centering
does not remove variance; coarse images are not the original variable.

## 3. Finite jets and real-tilt CD

### R-JET — PROVEN

For dmu_t=e^(t.X)dmu/Z(t), real domination in a neighborhood gives

    partial_i E_t G=Cov_t(G,X_i),
    partial_B log Z(0)=kappa(X_i:i in B).

Quotient differentiation proves the first identity; the nilpotent
calculation above proves every finite-order identity. Conditioning before
taking its formal logarithm gives total cumulance and K4MATCH (7).
Thus a degree-four real jet system retains all 15 nonempty subset jets,
including the triple/single, pair/pair and pair/single/single terms.
Their error bounds and outer averages remain necessary.

For a quantitative real replacement of Cauchy, let H be C^(q+1) on
[0,r]^q, q>=1, |H|<=epsilon, and
|partial_j partial_1...partial_q H|<=B for every j throughout the cube.
Repeated fundamental theorem of calculus gives

    h^-q Delta_h^1...Delta_h^q H(0)
      = average_[0,h]^q partial_1...partial_q H,
    |partial_1...partial_q H(0)|
      <=2^q epsilon h^-q+(q/2)Bh,  0<h<=r.              (R5)

The last error is the sum of B times each coordinate's average distance
h/2. If H vanishes on every coordinate face t_i=0, only the all-h
corner survives; replace 2^q by 1. With fixed q,r and uniform B>0,
choose h=(epsilon/B)^(1/(q+1)) once it fits. The derivative is
O(epsilon^(1/(q+1))). If B=0 take h=r; if epsilon=0 let h decrease
to zero. This loses an exponent relative to a Cauchy bound.

For K4MATCH let H=Pi4(L-L_run), with X_r=u lambda^4 O_r as in its §5.1.
A real |H|<=E u^-theta bound and the stated uniform fifth-derivative
bounds give

    |P-P_run| <= C u^(-4-theta/5).                       (R6)

Pi4 vanishes on all coordinate faces, and its mixed derivative is
u^4(P-P_run), with no 4! for distinct labels. A real fourth-jet bound
O(u^-theta) directly retains theta instead. Both actual estimates are
OPEN. The analogous pair argument gives a summed PL-1L error with
theta/3 from a third-derivative bound; it does not create per-scale
E12 envelopes or their summability.

A real value error alone is insufficient even for positive MGFs.
Let mu=N(0,b^2 I_q), 0<epsilon<1/2, and
dnu=(1+epsilon product_j sin(X_j/b))dmu. It is positive and normalized.
Completing the square gives

    log(M_nu(t)/M_mu(t))
      =log(1+epsilon e^(-q/2) product_j sin(b t_j)).     (R7)

To check the Gaussian sine factor using real calculus, integration by
parts gives J'(s)=-sJ(s), J(0)=1 for J(s)=E cos(sZ), Z unit normal.
Thus E sin(m+Z)=e^-1/2 sin(m). The real absolute value in R7 is at most
2epsilon e^(-q/2), but its mixed qth derivative at zero is
epsilon e^(-q/2)b^q. Let b=epsilon^-1, q=2 or 4. Moments and higher
derivatives are not uniform. This refutes only that unsupported
error-to-derivative inference, not a YM estimate.

### Real CD alone does not execute SRCAN SA-S

SRCAN §3.3(A) supplies a complex cross-derivative envelope, (B) a real
tilted covariance bound; SA-TC combines them. Deleting (A) does not prove
its conclusion. A real alternative is to put h=partial_i partial_j Phi
and m=n-2. If |h|<=H and |partial_l partial_I h|<=B_n on a real m-cube,
R5 gives |kappa_n|<=2^m H t^-m+(m/2)B_n t. With H=C exp(-mu_R d)
and uniform B_n, optimization gives fractional decay mu_R/(n-1) in
that pair distance once t fits the window; for n=2 use CD itself.

B_n is an explicit additional real derivative input, not a consequence
of CD or positivity. Its n growth, scale powers and window are needed
before an all-order claim. Outer moments require the corresponding
powers/products of H and B_n under the actual coarse law, or a common
envelope. CODEX_REVIEW_SRCAN §§11–12's fixed-kernel and tilt-supremum
obligations survive. Retuning the kernels to the new bare coupling
changes the generating function.


## 4. The actual H_reg / E0′ replacement

Ordinary factorial moments of one smeared variable do not themselves
supply the collision-flat distribution contract. Rebuild REC_LIB §16:
for centered scalar fields with Z=1, |e_hat_a(x)|<=C_X a^-4, require
for every n>=2, volume and placement with
delta=min_(i<j)|x_i-x_j|>=c_*a,

    |E product_i e_hat_a(x_i)|
      <=A_0^n(n!)^b_0 product_i wbar(delta_i),
    delta_i=min_(j!=i)|x_i-x_j|,
    wbar(r)=min(r,1)^-4[log(2+1/min(r,1))]^q.            (R8)

Here c_*>0, q>=0, b_0>=0 and A_0 are independent of n and cutoff.
These are unconditional expectations under the same actual law.
Assume the common convergent hierarchy required by the consumer;
estimates do not establish convergence or the other axioms.

Use OSLEAF's seminorm
|F|_k=max_(|alpha|<=k) sup_x (1+|x|^2)^(k/2)|partial^alpha F(x)|.
For flat F, Taylor-expand from the closest coincidence plane. For
delta<1 the displacement has l1 size <=2delta and the squared-weight
comparison costs <=2. With M derivatives, reserve 5n weight powers:

    |F(x)| <= (2delta)^M/M! *2^(5n/2)|F|_(M+5n)
                              product_i(1+|x_i|^2)^(-5/2).

Comparison with lattice cubes gives a uniform bound on
a^4 sum_x(1+|x|^2)^(-5/2) for 0<a<=1. If c_*a<=delta<1,
wbar(delta_i)<=C_q delta^-5, so M=5n cancels the singularity.
If 0<delta<c_*a use the crude field bound and M=4n+1:
a^-4n delta^(4n+1)<=c_*^(4n+1)a. Coincident points contribute zero.
For delta>=1 use the integrable weight; if c_*a>1 the lattice spacing
is bounded below and the crude bound suffices. Therefore

    |S_n^a(F)|<=C^n(n!)^b_0 |F|_(10n+1).

Since 10n+1<=11n and C^n<=e^C n!, the common limit has E0′ with
s=11, beta=b_0+1, alpha=e^C, adjusted at n=0,1. Uniform continuity
extends from compact flat tests by density. This has one all-n triple.
For a finite multiplet require R8 uniformly for every label combination;
a crude a^-Q bound instead gives the safe s=max(11,ceil(Q)+6).
No other field is silently assigned the scalar dimension four.

An alternative sufficient real input, with fixed A and p>=0 independent
of n and cutoff, for every partition pi of n labels with r blocks, is

    |kappa_outer(kappa_cond(B):B in pi)|
      <=A^n r! product_(B in pi)(|B|!)^p
                                  product_i wbar(delta_i). (R9)

This includes singleton conditional means and all required outer/LF
products. Total cumulance, product_B |B|!<=n!, and
sum_pi |pi|!<=2^(n-1)n! give unconditional cumulant exponent p+1.
For the count, order blocks and sum the 2^(n-1) positive compositions.
Moment expansion has at most n! partitions, giving R8 with b_0=p+2.
Subset capped weights are bounded by the full-configuration weights.
Thus beta=p+3 suffices. Higher conditional cumulants alone do not
supply R9.

A second usable interface is OSLEAF55:919–940's separated smeared
SP_lambda bound, with explicit lambda^-pn and scaled test-derivative
norms, uniformly down to lambda>=c_SP a. Real conditional distinct-source
jet bounds including singletons, uniform in coarse data, imply its
unconditional product bound by the same partition algebra. Its
tensor/Whitney extension must retain the corrected chart/interior
support and factorial-growth costs; see the full statement in
[the reconstruction inspection](checks/realonly_reconstruction_read.md).
No same-test MGF is substituted for this multilinear bound.

R8/R9 retain small-separation control and the capped large-distance
weight. Convergence on each fixed separated support alone does not
extend to all flat tests: CODEX_REVIEW_SRCAN §10 supplies a shrinking-
annulus counterexample. Shrinking real source windows are allowed only
with their losses included in the uniform distribution estimate.

## 5. Symmetry, reconstruction and flow

**Flat H_Euc.** For each real whole-product observable F, TQ2 uses its
extensive translate-source pressure p_a,F(t), p(0)=0. Positivity gives
convexity since the second derivative of finite-volume log Z is a
variance. Thus -p(-t)/t<=p'(0)<=p(t)/t. Differences of orientation
expectations are bounded by the pressure secant width plus comparison
errors divided by t. PC removes errors at fixed t on a common
volume-first diagonal; NC then removes the secant width as t decreases.
COMMON supplies extraction and extension. This rebuilds the analytic
step of TQ2 without a complex source denominator.

NC is a cutoff-uniform no-cusp condition, not differentiability at
each fixed cutoff. Sources cover every whole product and its translates.
An exponential moment of a linear field does not automatically permit
exponential sources for its products: for a unit Gaussian X, exp(tX^4)
has infinite expectation for t>0 although every polynomial moment
exists, by the large-x exponent tx^4-x^2/2. TQ2's moving-radius version
requires both width and comparison error divided by that radius to
vanish. Source-dependent vacuum scalars cannot be dropped.

**Sphere H_Euc.** Total covariance in the actual positive Markov chain
gives Cov(F,S)=sum_(i<k) E Cov(F_i,S_i|U_(i+1))+Cov(F_k,S_k).
With N5B's Z_a^-q normalization, image L2 bound C(J), seam-image
oscillation tau(a,J), and early sum delta(J), Cauchy–Schwarz gives
delta(J)+C(J)tau(a,J). Fix J so delta is small, then take a->0.
Every product/path and all crossing data are retained, with BULK/ALG
for the radius/OS passage. REVIEW_N5B:28–75 rejects calling this
UV-only: E and D depend on the actual coarse law. Preserve that
dependence or prove the stronger all-data conditional covariance and
image-sup bounds. The identity supplies no physical mass gap.

**REC/OSLEAF.** The real hierarchy, continuity, covariance and RP supply
the form sum S_(n+m)(Theta F_n^* tensor F_m), its Hilbert space and
positive-time semigroup. Complex test coefficients enter through
linearity and conjugation, not exponential source tilts. The reviewed
REC_LIB/REC_CONT implication retains its E0′–E3 seed and complex-
spacetime continuation conclusion. This note replaces none of that
proof. No source partition function is its input, and no mass gap,
unique vacuum, contact extension or different-algebra witness follows.

**Real coupling extraction — PROVEN implication.** In FLOW F-Pi replace
Cauchy by the real local bound
|partial_b partial_b' F(X)(0)|<=H exp(-kappa_p d(X)) in the same
normalized coordinates. There are <=16 possible root M-cubes,
<=80^(2(n-1)) connected n-cube animals, <=4M^4 n second links, and
|z1 z2|<=(Mn)^2. Therefore

    sum_z |z1 z2| |Pi_12(z)|
      <=64 M^6 H sum_(n>=1)n^3(6400e^-kappa_p)^(n-1).

It converges for kappa_p>log 6400. This is the same bound with H
replacing alpha^-2 times the analytic supremum. Gauge/color identities,
the actual action and the infinite-volume convention still have to
match. Differentiation twice must commute with the actual polymer sum;
uniform C^2 convergence on a real neighborhood is a sufficient
justification, while derivative bounds only at the identity are not.
Real higher-loop/LF Hessian estimates give F-rem; telescoping
real increments gives F-flow; continuity and its first-exit
intermediate-value argument give F-tune. Preserve FI-1: each step must
use only the earlier flow along the chain, not its unknown future.

For scalar u_(j+1)=u_j-beta_j(u_j), suppose
|beta_j'(u_j)|<=C u_j^-2<=q_*<1 and S=sum_j C u_j^-2<infinity.
Differentiating yields product_j(1-beta_j'). The elementary logarithm
inequalities log(1-x)>=-x/(1-q_*) and log(1+x)<=x give

    exp[-S/(1-q_*)]<=partial u_K/partial u_0<=exp(S).

A real flow bracket can make S uniformly finite. The strict q_* margin
is indispensable for this lower-bound argument (CODEX_REVIEW_SRCAN §3).
The derivative estimate is an OPEN input, not implied by a real
O(1/u) value error. Spatially varying sources require the actual
weighted variational kernel and inherited dependence; the scalar
formula does not prove LOC-e (review §§5,9).

## 6. Normalized ratios on real fields

Let D=int w>0 with w>=0, dnu=w/D, using the very same reference and
selectors in numerator and denominator. Direct integration gives

    |int w L exp(G)/int w|<=E_nu[|L|exp(|G|)],
    e^-a<=int w exp(G)/int w<=e^a  for real |G|<=a.

TV(nu)=1; unvisited normalized positive cells integrate to one.
Zero-mass histories stay zero summands and are never conditioned on.
This rebuilds RD3 D19/RD4 L2–L4 on the real section.

CHARGE C2's actual all-cut Z_(j,A)(V) is positive for every real V:
its identity-cap subset has positive measure and positive integrand.
Real coefficient tilts preserve this on the same nonempty support.
History references are positive only on their admitted nonzero fibers.
This settles real nonvanishing and TV=1, not uniform bounds on 1/D,
locality of log D, useful ratios to a different reference or derivative
budgets. A mandatory event of mass p becomes 1_E/p after conditioning,
with L1 norm one; its price cannot be earned again.

Connected atoms, inclusion-exclusion, derivatives and counterterm
differences can be signed and still require absolute joint estimates.
Complex contour references require TV=int|w|/|int w|. The two weights
(1,-1+d) and multiplier (e^a,1) give ratio 1+(e^a-1)/d; positivity
on a different real integral gives no bound for this cancellation.
This is a finite diagnostic, not a claimed YM denominator zero.

Moving cut/completion indicators can also destroy real differentiability.
Use fixed measurable sectors, sum selectors before differentiation when
justified, or prove the boundary terms. Positivity supplies no C^r
regularity for an integral with a moving boundary.


## 7. Rebuilt LF-JMBR contract on the real section

D_R keeps the original real source window, real unitary coarse
fields/charts and the same admitted histories, with interior margins
for derivatives. Keep the original reader graph, inactive regions,
exterior and normalizer readers. Define

    ||F||_(mu,R)=sup_x sum_(X contains x)e^(mu|X|)sup_(D_R)|F_X|.

For r derivatives replace each supremum by
sum_(m=0)^r R_jet^m/m! sup ||D^m F_X||, with declared real direction
norms in original units. Leibniz proves the pointwise finite-jet norm
submultiplicative. A fixed r=4 does not imply all-order E0′: supply
explicit r growth or R8/R9 separately. These norms are proposed
replacement spaces, not the already established RG output class.

**REAL-LF — actual instantiation OPEN.** Retain LFPRICE §6 clause 1's
exact paired representation; replace clauses 2–5 as follows.

| Clause | Required real estimate | What is closed here |
|---|---|---|
| 2: charge/reference/boundary | Allocate original fractions once. For every complete mixed group G, bound its coefficient-weighted joint absolute integral, including reference changes, readers and returns under the actual matched positive reference, by exp[-tau m_G+c_ref m_G+b_partial |Bdy_G|]. Use a joint averaged bound if a pointwise one is unavailable. | **PROVEN** positive-reference comparison (§6); CHARGE C9–C11 gives an extensive-family instance. **OPEN** the uniform local mixed bounds. |
| 3: nonzero reference/TV | Actual positive real denominators on admitted fibers, normalized local probabilities and explicit local prefactor logs/real derivative budgets. Retain all normalizers and zero sectors. | **PROVEN** nonvanishing and TV=1 for the stated positive references. **OPEN** local/derivative budgets and a suitable positive cell construction. The original complex clause is not closed. |
| 4: overlaps/full supports | Integrate complete overlaps before logs; exact factorization of disjoint resulting components. For every selected set, its complete coefficient-weighted joint absolute integral is <=product alpha_i, with Q=sup_x sum_(i:x in H_i)e^((mu+2)|H_i|)alpha_i<=1/4. Include all original readers and type multiplicities. For a jet conclusion require the same joint bound in the finite-jet norm, including differentiated measures/prefactors. | **PROVEN** real cluster implication below. **OPEN** actual small weights, matching, factorization and rooted reader sums. Separate scalar history prices are insufficient. |
| 5: returns/failures/next step | Include every success and completion/chart/coherent failure; explicitly extract vacuum and coupling terms. Prove real full-norm continuation/return bounds or a summable creation-and-accumulation envelope, plus invariant nonlinear, derivative and relevant-coefficient recursions. | **PROVEN** window/invariance arithmetic below. **OPEN** actual operators, coherent margin, derivative closure and flow. |

**Real cluster implication — PROVEN conditional statement.** Assume
the exact finite atom representation, local probabilities and joint
bounds in clause 4. Group atoms by intersecting full supports;
disjoint components factor. Put v_i=e^((mu+1)|H_i|)alpha_i and
b_i=e^((mu+2)|H_i|)alpha_i. The rooted-tree recursion
T_i=v_i exp(sum_(j:H_j meets H_i)T_j) has supersolution b_i because
the child sum is <=Q|H_i|. Iteration bounds the integrated gas norm
at mu+1 by Q. For its log, order incompatibility edges and assign
each connected graph its Kruskal spanning tree. Graphs assigned to
one tree form an interval of optional edges, whose alternating
sum has modulus <=1. A second tree sum spends the other unit of
support exponent and bounds the supported log norm at mu by Q.

An auxiliary atom multiplier z has convergence for |z|<2 since
2Q<=1/2; the formal finite-gas identity near zero agrees with the
convergent exponential at z=1. This introduces no complex physical
source bound. With real atoms/coefficients the resulting exponential
is positive and its series is the real logarithm. The same norm
argument applies to finite jets **when the joint jet bounds are
supplied**, not from pointwise alpha_i alone. An empty-support
scalar is separately retained with its nonzero/log budget.
This rebuilds the real version of JMBRB B-JOINT/RENEW R-GROUP.

Precisely, for each selected set I let
A_I(t)=c_I(t) int product_(i in I) a_i(t) dnu_t, with A_empty=1.
For the jet version require these complete integrated coefficients to
be C^r and their finite-jet norms <=product_(i in I)alpha_i, with exact
factorization across disjoint components. Differentiated measures and
selectors are included when constructing A_I. This makes the stronger
hypothesis and the use of submultiplicativity explicit.

For region multiplicity <=A_type^n, full support <=c_s n and
boundary <=c_partial n, RD4 L6 becomes

    nu_R=tau-c_ref-c_partial b_partial,
    r_R=A_type exp[(mu+2)c_s-nu_R],
    e^(h_sf)h_sf+r_R/(1-r_R)<=1/4,   r_R<1.              (R10)

Here h_sf is a compatible matched small-field interaction budget
giving atom budget <=e^(h_sf)h_sf. Complex TV and polar-contour costs
disappear only because the reference and bounds are positive real.
Signed/reference-changing costs stay in the joint alpha_i.
R10 is a sufficient majorant, not evaluated YM constants.

**CHARGE's exact contribution.** Under C10's coupling/cut conditions,
for its original filled flux tube and j>=j_*,

    sup_(real V) R_(E,j)(V)/Z_(j,A)(V)
                       <=exp[-c_delta u_0 n_0/2].

The cap proof pays the actual all-cut denominator. For a filled
ancestor n_0=L^(4R)n_R this beats a fixed B^R bill once the stated
additional support costs are paid. Its local crude C13 bound is
log Q_core<=-tau m+d_j n_j. Deleting complex variation does not
replace the extensive d_j n_j by a local reader cost. Failure of
that majorant supplies no actual local lower bound or impossibility.

**Window arithmetic — PROVEN implication.** If real full-norm
operators have prefix bound B0 for lengths <m, every m-window
norm <=theta<1, and return norm <=D_ret, write r=qm+s. Ordered
products have norm <=B0 theta^q, giving sum <=mB0/(1-theta),
or D_ret times this for first returns. No analyticity is used.
Alternatively a uniform lag envelope
||C_(j+r-1)...C_j A_j||<=a_r with sum_r a_r<infinity bounds
both per-birth lifetimes and past-birth accumulation at a fixed
terminal level. A lifetime sum alone is not the latter bound
(CHARGE C25/C25a).

A real derivative norm also replaces JMBRB B31's limited
maximum-principle example. For C^3 F on a real ball with degree
0–2 jets zero at zero, Taylor's integral formula gives
|F(x)|<=sup||D^3F|| |x|^3/6. For the *ideal* dilation
D_L F(x)=L^4 F(L^-2 x), the third-derivative seminorm satisfies
sup||D^3 D_L F||<=L^-2 sup||D^3F||. It is a norm on the
zero-jet subspace. This is not the actual RG map: its
fluctuation, boundary, gauge, support and extraction operators
still need estimates in the same invariant real norm.

Finally x'<=theta x+C x^2+e is invariant on 0<=x<=M if
theta+CM<1 and e<=(1-theta-CM)M, since Cx^2<=CMx.
The actual coherent no-gap bound is not supplied by this arithmetic.
JMBRB B9 preserves inherited positive mass; RENEW R15's flux
tubes persist with probability tending to one at each fixed
finite horizon as coupling grows. They preclude importing a
uniform plain-forward smoothing margin but leave weighted/
extracted and actual creation-map bounds open. CHARGE's creation
price is not a contraction factor on arbitrary insertions.

## 8. Critical-path effect and scope stress test

**Net effect — ARGUED program change, PROVEN consumer implications.**
The downstream graph can be supplied by real separated distributions,
finite matching jets, real symmetry defects and real flow derivatives.
It need not first receive a complex physical-source polydisc.
Real positivity closes the elementary real part of clause 3;
real joint estimates would support the same cluster/window arithmetic.

Clauses 2, 4 and 5 remain quantitatively OPEN, together with the local
and derivative parts of clause 3. No full original LF-JMBR clause on
D_* is newly certified. AUDIT's coupled full-return/flow block and
actual all-order source seed remain unclosed. The common algebra and
sequence, H_RP, all-product H_Euc and absolute witness estimates also
remain. This changes a possible sufficient interface, not AUDIT's
statuses or the scientific status of its sources.

The next decisive target is a matched real local mixed-group bound
with complete readers and the required jets, then a coherent
continuation or common creation-envelope estimate. FR, KR and TC
remain coordinator inputs only at their exact proven scope; their
all-history extensions are not assumed or rederived here.

### No-Go Discipline Gate — no exhaustion certificate

**N1, routes.** The mechanisms inspected are positive real exponential
moments, direct/finite-difference jets, real convex source pressures,
and positive-reference connected expansion with extracted renewal.
They are live alternatives with missing inputs, not failed routes
proving impossibility. The five-failed-family packet requirement is
not met and no no-go packet PASS is claimed.

**N2, dependencies.** Let J be a joint local expansion, D the required
derivative/distribution estimates, I invariant extracted flow.
A value-bound J alone does not give D (R7); no implication D=>J is
asserted. Neither direction for J/I or D/I is established here.
These pair relations are unresolved, not independent walls.
Derivative-valued J can supply part of D, so they are not counted
as separate independent obstacles.

**N3, hidden conditions.** Probability representations, uniform
windows/constants, fixed selectors or boundary control, outer/LF
bounds, exact factorization, source normalization and invariant
jet norms are explicit. Model identification and a common limiting
algebra are not derived by the elementary estimates.

**N4, residuals.** R7 attacks real error-to-derivative inference
without smoothness; Lemma V attacks uniform raw fine-field growth
on its stated trajectory; RENEW attacks plain uniform forward
smoothing. None refutes a matched weighted/extracted real RG.

**N5, resolution.** R1–R7 concern finite random-variable families;
R8 is a separated-distribution statement; R10/window sums are
conditional full-support estimates. No per-site, per-mode or
lattice-wide impossibility follows. No numerical experiment ran.

**N6, partial closure.** A real jet norm or changed consumer
contract is mathematics, not an additional physical axiom.
Positive real references and scale-dependent windows remain live.
Approved units, kinetic isotropy and realized-state primitives
are not missing walls and supply none of the needed dynamics
or source estimates.

**N7, steelman.** A positive-reference expansion with real
derivative-weighted atoms could provide cumulants, matching
and invariant extraction together. R4 could then recover smaller
complex source domains if needed. That route remains open;
its local mixed estimates, derivative growth and coherent
margin are the concrete obligations.

**N8, earlier mechanisms.** RD3's finite germ, RD4's positive case,
SRCAN's real tilted decay, CHARGE's filled-family charge, TQ2's
real pressure and K4MATCH's jet alternative were inspected and
used at their stated scopes. Neither universal necessity nor
universal dispensability of complex analyticity is asserted.
