# Uniform finite-coupling remainder of the normalized SU(N) kernel

Author unit, requested Astra/max, pending fresh independent review. This
proves a finite, uniform estimate for one actual normalized compact-group
kernel and its local field derivatives. It supplies an analytic
`O(u^-1)` correction after its tree exponent and full Gaussian normalizer
have been extracted. It does not estimate an interacting fluctuation
integral, a returned denominator, or a nonlinear RG coupling map. Full
four-dimensional continuum existence and a positive physical continuum
mass gap remain open.

## 1. Exact target and previously available results

Fix N>=2, D=N^2-1. Lie-algebra coordinates are orthonormal for
`<X,Y>_HS=-Re tr(XY)` on su(N); matrix HS norms below use the corresponding
complex Euclidean norm. Every group integral uses probability Haar. Put

    phi(W;M_plus,M_minus)
        =[tr(W^-1 M_plus)+tr(M_minus W)]/(2N),
    Z_t(M_plus,M_minus)=int_SU(N) exp[t phi(W;M_plus,M_minus)] dW,
    k_t(V;M_plus,M_minus)=exp[t phi(V;M_plus,M_minus)]/Z_t.       (FK1)

The matrices M_plus and M_minus are INDEPENDENT complex matrices. On real
data M_minus=M_plus*. For actual complexified fine links they are the
mean of the path matrices and the mean of their inverses, respectively.
In general M_minus is neither M_plus^-1 nor M_plus*. The original
uncentered normalizer in CB1 is `N_t=e^-t Z_t`; that factor cancels
exactly in the normalized kernel, without a change of stiffness.

The novelty is narrower than zero-freeness. STEP55 §§4.1–4.3, with its
S5–S7 corrections and CODEX_REVIEW_STEP R6, already prove complex Haar
invariance, local SL recentering, and fixed-field-width zero-freeness of
one normalizer for ALL real t>0, with an O(1) centered logarithm and its
derivatives. CB9–CB15 use that result. NODEA55 A.3 is a fixed-volume
Laplace/price comparison, not the estimate here. BFT_A §1.1 explicitly
uses the normalized TREE exponent; BFT_B's selected §§41.5–42.3 discuss
composite background/source estimates, not a finite-t normalizer
remainder. CJ1 and the reviewed UL theorem concern the tree jets and
Gaussian coefficient. No conclusion about the rest of those large BFT
files is inferred from the selected read.

Here the sharper result is

    Z_t=e^(t phi_star) t^(-D/2) A(M_plus,M_minus) exp E_t,
    |partial_parameter^alpha partial_t^m E_t|
                         <= C_(alpha,m) t^(-1-m),           (FK2)

on a fixed smaller complex parameter neighborhood, for real t>=2t_0
(and a surrounding sector used in its proof). Constants depend on N and
the chosen neighborhood, not t, lattice volume or scale. The amplitude
A includes probability Haar and the FULL D-colour Hessian determinant.

## 2. A uniform SL saddle, including the scalar SU constraint

Fix ANY real G in SU(N), and write

    A0=G^-1 M_plus, B0=M_minus G,
    eta=max(||A0-I||_HS,||B0-I||_HS),
    C_odd=16 N^3,
    eta_N=min{1/64, 1/[8(4+2 C_odd)]}.                     (FK3)

The theorem initially holds throughout eta<eta_N. The letters A0,B0
are matrix parameters; the scalar amplitude in FK2 is denoted A below.
Let P0 X=X-(tr X/N)I. In complex HS norm P0 has norm one. For Y in
sl(N,C), set

    F(Y)=P0(e^-Y A0-B0 e^Y),
    R(Y)=F(Y)-P0(A0-B0)+2Y,
    T(Y)=P0(A0-B0)/2+R(Y)/2.                              (FK4)

For ||Y||_HS<=r,

    ||R(Y)||_HS <= e^r r^3/3+2 eta(e^r-1),
    ||D R(Y)|| <= e^r r^2+2 eta e^r.                     (FK5)

To obtain these bounds, separate `e^-Y-e^Y+2Y`, whose series starts at
degree three, from `(e^-Y-I)(A0-I)-(B0-I)(e^Y-I)`; differentiate each
matrix power by inserting the variation at every position. Matrix HS
norm is submultiplicative and bounds operator norm. At r=2 eta, T maps
the closed r-ball into itself and has Lipschitz constant less than 1/4
for eta<=1/64. Consequently its iterates from zero converge uniformly
on compact parameter sets to a holomorphic Y, with ||Y||<=2 eta and
F(Y)=0. These same derivative bounds give uniqueness among solutions
with ||Y||<=8 eta_N. This is a uniform contraction, not an implicit
function theorem with an untracked neighborhood.

Define

    W_star=G e^Y, E=e^-Y A0, F=B0 e^Y,
    S=(E+F)/2, (E-F)/2=lambda I, phi_star=tr S/N.          (FK6)

Then `||E-I||_HS,||F-I||_HS<=4 eta`, hence
`||S-I||op<=4 eta` and `|lambda|<=4 eta`. Right variation of W_star by
exp X gives derivative `tr[(F-E)X]/(2N)=0` for EVERY traceless X.
Thus W_star is the actual SL(N,C) critical point. The scalar lambda is
retained. Setting lambda=0 would solve the wrong U(N) problem.

On the physical subspace B0=A0*, T preserves su(N), so W_star is
unitary. Section 4 proves that it is the unique global SU(N) maximizer.
The local construction is uniform in G. If two such G-neighborhoods
overlap, both candidate saddles lie in the uniqueness ball in one
chart (the logarithm of the product has norm less than 8 eta_N), so the
branches agree. All assertions can alternatively be used in a single
fixed G chart, without a global logarithm of G.

## 3. Translate the entire compact integration cycle

Choose an oriented real HS-orthonormal basis T_a of su(N), and its
complex-linear extension as a basis of sl(N,C). There is a left-invariant
holomorphic D-form Omega on SL(N,C), specified at the identity by
`Omega(T_1,...,T_D)=h_N`, where h_N is the density at zero of probability
Haar in exponential HS coordinates. Its restriction to SU(N) is exactly
probability Haar: both are left invariant, with the same normalization.
Every holomorphic top form on a complex D-manifold is closed. The form
`exp(t phi) Omega` is therefore closed; inversion is holomorphic on SL.

The smooth homotopy `(s,U) -> G exp(sY) U`, 0<=s<=1, is a compact
(D+1)-chain whose boundary is the two full group cycles. SU(N) has no
boundary. Stokes' theorem and left invariance of Omega give the EXACT
identity, for every complex t,

    Z_t=e^(t phi_star) int_SU(N) exp[-t f(U)] dU,
    f(U)=phi_star-phi(W_star U;M_plus,M_minus)
        =tr[S(I-(U+U^-1)/2)]/N
                       -lambda tr(U^-1-U)/(2N).           (FK7)

No chart is moved separately; there are no discarded faces. This rebuilds
STEP55 INV for the present phase and supplies its geometric justification.
The real integration variables after translation are still U in SU(N).

## 4. Global real-part drop and the full Hessian

For U unitary let H_U=I-(U+U*)/2>=0 and s(U)=tr H_U/N. The SU condition
implies the elementary global estimate

    |tr(U^-1-U)| <= C_odd tr H_U.                          (FK8)

Here is a complete bound. If ||I-U||op<1/(2N), all principal eigenangles
have absolute value less than 1/N. Their sum, a multiple of 2pi, is zero.
Subtract their sum from the sum of their sines, use
`|sin theta-theta|<=|theta|^3/6` and
`theta^2<=(pi^2/2)(1-cos theta)`. This gives a constant smaller than
C_odd. On the complementary set, tr H_U>=1/(8N^2), while the left side
is at most 2N, proving FK8 with 16N^3. This argument is full SU(N),
including center elements; it does not assume every global principal
logarithm is traceless.

Since `|tr[(S-I)H_U]|<=||S-I||op tr H_U`, FK3–FK8 imply

    |f(U)-s(U)| <= (4+2 C_odd) eta s(U) <= s(U)/8.
    Re[t f(U)] >= |t| s(U)/2       if |arg t|<=pi/6.       (FK9)

In particular for physical parameters f is real, zero only at I. This
proves the asserted global maximum. It also controls the complete
translated cycle, including points outside every local chart.

In the fixed real basis write X=sum x_a T_a. Expansion at U=exp X gives

    f(exp X)=q(x)+f3(x)+f4(x)+O_N(|x|^5),
    q=x^T H x/2, H_ab=-tr[S(T_a T_b+T_b T_a)]/(2N),
    f3=lambda tr X^3/(6N), f4=-tr(S X^4)/(24N),
    ||N H-I_D|| <=4 eta.                                 (FK10)

The last bound follows from `|tr(S-I)XY|<=||S-I||op ||X||_HS||Y||_HS`
and polarization in the displayed symmetric bilinear form. In particular
`Re(t q(x))>=|t| |x|^2/(4N)` on the sector for real x.
The square root is fixed without an eigenvalue-ordering convention:

    (det H)^(-1/2)=N^(D/2) exp[-Tr log(NH)/2],
    log(NH)=sum_(j>=1) (-1)^(j+1)(NH-I)^j/j.              (FK11)

It is holomorphic and positive at A0=B0=I. For N=2, tr X^3=0;
for N>=3 the cubic term generally survives. Its cancellation in the
integral below is parity, not a claim that it is identically zero.

## 5. Haar amplitude and an actual uniform error estimate

The exponential differential, in left coordinates, is
`(1-e^(-ad X))/(ad X)=int_0^1 e^(-s ad X) ds`. Taking its determinant
and using `Tr_ad ad X=0` proves

    dHaar(exp X)=h_N j_N(X) dx,
    j_N(X)=det_sl [sinh(ad X/2)/(ad X/2)],
    j_N(-X)=j_N(X), j_N(0)=1,
    j_N(X)=1+(N/12)tr X^2+O_N(|X|^4).                    (FK12)

For the last identity, on all matrices ad X is `X tensor I-I tensor X^T`;
its square has trace `2N tr X^2-2(tr X)^2`. The scalar matrix contributes
zero, so this is also its trace on sl. The power series of log(sinh z/z)
starts at z^2/6. This proves the coefficient including all colours.
For real X with eigenvalues i theta_j, FK12 is the positive product
`prod_(i<j) [sin((theta_i-theta_j)/2)/((theta_i-theta_j)/2)]^2`.
On a sufficiently small ball it is nonzero. h_N is not set to one.

Here are explicit prescriptions for all constants in the error estimate;
their numerical optimization is unnecessary. Take r_bar=min(1/8,1/(8N)).
On the compact closure eta<=eta_N and |x|<=r_bar, define C3,C4,J,J2 as
upper bounds for

    |f(exp X)-q|/|x|^3,
    |f(exp X)-q-f3|/|x|^4,
    |j_N(X)|, |j_N(X)-1|/|x|^2,                           (FK13)

respectively, with values at zero filled by their Taylor bounds. The
explicit matrix exponential series and FK5 bound every derivative on
this compact set; thus these constants are finite and depend only on N.
Choose `r=min(r_bar,1/[16N max(1,C3)])`, c=1/(8N), and tau=|t|>=1.
For |x|<=r, put b=f-q. The elementary exponential remainder gives

    |exp(-t b)-1+t f3|
       <= tau C4 |x|^4+(tau^2 C3^2/2)|x|^6 exp(tau C3|x|^3).

The integrand `exp(-t q) j_N f3` is odd on the symmetric real ball, so
its integral is EXACTLY zero, also for complex parameters and t.
After the FK10 Gaussian factor is included, the difference between the
local integral and `h_N int_(|x|<=r) exp(-t q) dx` is bounded by

    h_N int_R^D e^(-c tau |x|^2)
        [J2 |x|^2+J C4 tau |x|^4+(J C3^2/2)tau^2 |x|^6] dx
            = C_local tau^(-D/2-1).                       (FK14)

For example each coefficient is evaluated with
`M_j(c)=pi^(D/2)c^(-(D+j)/2) Gamma((D+j)/2)/Gamma(D/2)`.
The choice of r ensures the exponential in the preceding remainder is
absorbed into the Gaussian. Thus FK14 is a finite inequality, not a
termwise integration of an unbounded formal series.

Outside exp{|x|<r}, the principal eigenangles obey sum theta_j^2>=r^2:
otherwise their sum is zero and their HS logarithm belongs to that ball.
Therefore `s(U)>=2r^2/(N pi^2)`. FK9 bounds the remaining compact-group
integral by `exp[-tau r^2/(N pi^2)]`. The discarded Gaussian tail is
bounded by a fixed multiple of
`tau^(-D/2) exp[-tau r^2/(8N)]`. Both are bounded by
`C_tail tau^(-D/2-1)` for tau>=1. A computable choice follows from
`sup_(tau>=1) tau^a exp(-b tau) <= max(e^-b,(a/(be))^a)`.
No group boundary or gauge volume is lost in this split.

Finally

    int_R^D exp(-t x^T H x/2) dx
                       =(2pi)^(D/2) t^(-D/2)(det H)^(-1/2).

For positive real H,t this follows by orthogonal diagonalization and
the one-dimensional Gaussian integral. Both sides are holomorphic on
`Re(tH)>0`; analytic continuation from real positive matrices proves
the identity on the connected neighborhood used here. The branch is
FK11 and the principal t logarithm. In particular the factor is
`(2pi)^(D/2)`, with the stated HS Lebesgue convention.

Set

    A=h_N(2pi)^(D/2)(det H)^(-1/2),
    r_t=t^(D/2) exp(-t phi_star) Z_t/A-1.

Since `|A|>=h_N(2pi N)^(D/2)(1+4 eta_N)^(-D/2)>0`, FK14 and the tails
prove, uniformly for eta<eta_N and |arg t|<=pi/6,

    |r_t|<=C_N^Lap/|t|,  |t|>=1.                         (FK15)

All constants have been prescribed independently of t. For
`|t|>=t_0=max(1,2 C_N^Lap)`, define the single holomorphic branch
`E_t=log(1+r_t)` by its convergent series. It obeys
`|E_t|<=2 C_N^Lap/|t|`; Z_t is nonzero throughout this domain.
This proves FK2's value estimate and the full finite-u factorization.
It makes no claim about a normalizer at small complex t.

## 6. Derivatives, inverse charts and exact kernel action

For eta<=eta_N/2 the parameter margin is fixed. In an orthonormal
complex matrix-entry coordinate system there are 2N^2 independent
coordinates. A simultaneous polydisc of radius
`r_par=eta_N/(4 sqrt(2N^2))` remains in eta<eta_N. Cauchy's formula
applied to E_t bounds any multi-index alpha by
`alpha! r_par^(-|alpha|) 2 C_N^Lap/|t|`. At real t>=2t_0 the t-disc
of radius t/4 lies inside the sector and has modulus at least 3t/4.
The joint Cauchy formula proves

    |partial_parameter^alpha partial_t^m E_t|
       <= (8 C_N^Lap/3) alpha! m! r_par^(-|alpha|)
                                              4^m t^(-m-1). (FK16)

This includes arbitrary mixed independent-plus/minus derivatives. No
complex derivative is taken by conjugating its argument. On a smaller
joint neighborhood, V^-1 W_star has an analytic traceless logarithm:
the logarithm series converges near I, and det=1 forces its trace to be
the locally constant value zero. This is the actual inverse mismatch
chart. The exact action is

    -log k_t(V)=t psi(V)-D/2 log t+log A+E_t,
    psi(V)=phi_star-phi(V).                               (FK17)

The logarithm in FK17 is specified by this equality; only the exponential
is globally meaningful without a branch convention. On real physical
data it is the ordinary real negative logdensity. The exact SU saddle
defines psi; an unconstrained U(N) polar factor cannot replace it.
Both the phase and A are covariant under endpoint SU(N) gauges; for A,
the right tangent basis changes by an orthogonal adjoint matrix with
determinant one. Local complex covariance follows by holomorphic
continuation. E_t inherits the same symmetries from FK1/FK15.

At the unit pair, differentiating in t gives the sharpened identity-tilt
estimate (the derivative is justified by FK16):

    c_N(t)=d_t log Z_t(I,I)=1-D/(2t)+d_t E_t(I,I),
    1-c_N(t)=D/(2t)+O_N(t^-2).                            (FK18)

Thus the ACTUAL spread term in F9/CB8 satisfies, at t=kappa u,

    kappa(1-c_N(kappa u)) B
                      =[D/(2u)+O_(N,kappa_-)(u^-2)] B.   (FK19)

The Haar precision N^2/(6u)I from F9 remains separate. FK19 neither
sets the positive finite-u spread to zero nor redefines the tree phase.

## 7. Actual S4-prime fields, sources and local counting

Fix odd L>=3, d=4, coarse torus side T>=2,
0<kappa_-<=kappa<=kappa_+, and a real coarse field V0, with arbitrary
holonomies. Use CB2's brick lift: internal fine links
are I and every crossing face link is the corresponding coarse V0.
Every actual contour for c is exactly G=V0_c: the same axial permutation
at the two endpoints, centered offsets -h,...,h, length-L straight leg,
divisor 24L^4. A contour has length <=p_L=5L-4 and lies in the two
endpoint blocks and their joining edges.
Throughout this section take `u>=max(1,2t_0/kappa_-)`, so all mixed
stiffness derivative estimates are on FK16's stated domain.

In complex left coordinates U_e=exp(x_e)U0_e, inverse edges use the
EXACT inverse `U0_e^-1 exp(-x_e)`. Moving the unitary baseline factors
through the word gives

    ||G^-1 T_tau(U)-I||_HS,
    ||T_tau(U)^-1 G-I||_HS
                      <=sqrt(N)(exp(p_L a)-1)
           if max_e ||x_e||_HS<=a.                        (FK20)

The same holds for the two arithmetic means. For example choose
`a=log(1+eta_N/(4sqrt(N)))/(p_L+1)`. Then both means are strictly
inside eta_N/2, on a u-independent complex field neighborhood. This
proves that the actual path averages lie in the theorem's domain in
this chart. It does not put arbitrary large-field means there: at
M_plus=M_minus=0, Z_t=1 and the nondegenerate Laplace form fails.
Coarse output V=exp(v)G can vary independently on ||v||<a. FK17 and
its inverse chart then apply on a smaller fixed joint neighborhood.

Let `E0(t)=E_t(I,I)`. The EXACT field-dependent normalizer remainder is

    R_c(u,x)=E_(kappa u)(M_c^+(x),M_c^-(x))-E0(kappa u).

In each joint field polydisc of radius `r_link=a/(4sqrt(D))` per colour
coordinate, centered at fine/coarse HS sup norms at most a/4, Cauchy gives

    |partial_x^alpha partial_u^m R_c|
          <=C_(N,L,kappa_-,kappa_+,alpha,m) u^(-1-m).      (FK21)

The u-disc is obtained by t=kappa u, with kappa fixed. Derivatives in
the output V at fixed fine U are identically zero for R_c: all output
dependence in FK17 is in psi. Joint fine/coarse charts or composed
backgrounds may have indirect dependence and use the joint Cauchy
bound instead. No stiffness/source convention is changed.

For clarity there is an actual joint coarse chart behind that statement:
replace each coarse baseline link by exp(v_c)V0_c, form its SAME brick
lift, and then multiply its fine links by exp(x_e). If both HS sup norms
are <=a/2, each contour contains at most p_L fine displacement factors
and p_L coarse displacement factors. The proof of FK20, with their
sum <=p_L a, still applies about the fixed real G=V0_c. This proves FK21
for the indirect coarse derivatives in this concrete chart as well;
there are at most eight additional coarse-link slots per local term.

At the exact brick lift, R_c=0 and its first fine-field derivative is
zero. Indeed the first doubled mean variation is (G Z,-Z G^-1) for
one traceless Z, tangent to the common-path pair
`(G exp(sZ),exp(-sZ)G^-1)`. Complex Haar translation makes phi_star,
A and E_t constant on this pair. Thus, on a smaller ball,
`|R_c|<=C u^-1 (max_e||x_e||_HS)^2`. Its higher derivatives obey FK21.

One coarse term reads at most n_c=8L^4 distinct fine links (a safe
overcount of the two blocks and face edges). A fine link is read by at
most eight coarse means. Consequently the sum R=sum_c R_c has, for
q>=1, an absolute q-derivative tensor row sum bounded by

    8 (D n_c)^(q-1) q! C r_link^(-q)/u.                  (FK22)

The same anchored-column estimate follows by symmetry of the mixed
derivative tensor. Entries vanish if their links do not belong to one
common contour reader. A fixed exponential of coarse-block diameter
costs only a constant (diameter<=2 for this safe support). Periodic
identifications can only reduce the reader set. These are own-level
counting norms, with the original 24L^4 average retained; no ell^4
density factor or all-depth summation has been silently dropped.
The unsubtracted vacuum contributes `#coarse_links E0(kappa u)`, which
is extensive and is retained in FK17. There is no volume-uniform bound
on the absolute total vacuum.

Original sources are `u sum_p epsilon_p s(U_p)` with
`s^C(P)=1-[tr P+tr P^-1]/(2N)`; they do not enter FK1. At fixed fine
field all direct epsilon derivatives of R_c are zero. More generally,
if an already constructed holomorphic field map x(epsilon,v) sends a
source polydisc of FIXED radius rho into the above smaller field ball,
then the composition has bounds
`|partial_epsilon^beta R_c(x(epsilon,v))|<=C beta!(2/rho)^|beta|/u`
on a concentric half polydisc, by Cauchy. This is a precise composition lemma,
not a construction of such a map. CB14 provides a local one-step
critical branch on its stated curvature/source domain; its image and
the new, potentially smaller FK20 chart must BOTH be imposed before
using this lemma. A fixed-n stationary germ or SA's source radius
shrinking with p does not meet this condition by assertion. No
source-history integral or hard-cut deformation was used.

There is a nonempty, explicitly matched application to the actual CB14
one-step source branch. Retain its R,G,delta_star,rho_star and original
source convention, and restrict

    delta_V<=min(delta_star,a/(16RG)),
    u>=max(1,2t_0/kappa_-), ||epsilon||infinity<rho_star.  (FK23)

CB14's proved bound `||a_(u,epsilon)||_(infinity,HS)<=4RG delta_V`
places that complex critical branch inside the a/4 ball here. Therefore
for every fixed real V in FK23, and every source multi-index beta,

    |partial_epsilon^beta R_c(u,a_(u,epsilon))|
       <=(C/u) beta! (2/rho_star)^|beta|
             for ||epsilon||infinity<=rho_star/2.

The source radius is fixed as u grows. This corollary uses the actual
CB14 construction at its stated one-step scope; the standalone scalar
theorem FK2 does not depend on CB. It does not assert the source map is
finite range: FK22's tensor-support bound is BEFORE this composition.
No sum over arbitrarily many source labels, weighted source-reader norm,
source-history integral or integrated partition-function logarithm is
bounded by this pointwise Cauchy estimate.

In the original unscaled action, the new local error is O(u^-1).
In CB's `F=(N/u) S_eff` it is O(u^-2). In FLOW coordinates
`x_HS=sqrt(N)x_FLOW`, q-th derivatives gain N^(q/2), while the separate
tree-action convention in UL9 divides its energy by N. These factors
are not absorbed into u or kappa. The log A term in FK17 is the
leading, field-dependent normalizer determinant already retained by
UL10: `log A=constant-(1/2)log det H`, equivalently the positive half-log
of the covariance determinant H^-1. Adding it again to UL's Gaussian
coefficient would double count.

There is also an exact quadratic identification of this error. At an
aligned contour family, let theta_tau be its transported first variation,
`q=average theta_tau`, `z_tau=theta_tau-q`, and let B_sp have quadratic
form `sum_c average_tau ||z_tau||_HS^2`, as in F4. Rebuilding F6–F7:
`Re tr M''=-average||theta_tau||^2`, while differentiation of log Z
gives that trace multiplied by t c_N/N plus a variance. Haar invariance
of `Z_t(exp(sq),exp(-sq))` makes the variance equal to
`(t/N)c_N ||q||^2`. Thus the exact kernel Hessian is
`(t/N)[||q||^2+(1-c_N)average||z_tau||^2]`. Differentiating the
stationary equation gives W_star'=q; hence the tree Hessian of t psi is
`(t/N)||q||^2`. FK16 makes the E_t Hessian tend to zero. Taking the
limit t->infinity in the difference, using FK18, therefore proves

    Hess sum_c log A_c = D/(2N) B_sp,
    Hess R = [t(1-c_N(t))-D/2] B_sp/N = O_N(t^-1) B_sp.    (FK24)

These are derivatives in actual unscaled HS link coordinates at the
aligned family, with the covariantly transported B_sp at a brick lift.
They verify exactly which finite-u quadratic correction is supplied.
They do not identify the marginal projection after the interacting
fine-field integral or after an all-depth stationary pullback.

## 8. Literature, evidence and the next interface

The compact saddle/recentering mechanism reuses STEP55's actual
normalized-kernel construction; the uniform remainder is proved above.
[Pemantle–Wilson, arXiv:0903.3585v1](https://arxiv.org/abs/0903.3585)
discuss complex analytic saddle integrals and contour deformation.
Their Theorem 2.3, local Theorem 4.1 and Stokes passage provide the
comparison; no asymptotic theorem or normalization constant is imported.
FK7 and FK10–FK16 rebuild the needed whole-cycle, parameter-uniform
finite estimate explicitly. In particular the Gaussian constant is
derived in the present Haar/HS convention.

The multiscale small/large-field architecture is due to Bałaban; see
[his four-dimensional small-field effective-action paper](https://doi.org/10.1007/BF01215223)
and [Dimock's exposition, arXiv:1108.1335](https://arxiv.org/abs/1108.1335).
The latter treats scalar phi^4 in d=3. These are attribution and scope
comparisons, not imports of a d=4 SU(N) finite-u interacting estimate.
The read manifest records the exact primary sections inspected.

Numerical criteria were written first in
[the criteria file](checks/finite_coupling_kernel_criteria.md). The proof,
not a finite check, establishes the theorem. The evidence receipt records
every run and failure without reclassifying post-hoc diagnostics.

FK17–FK24 give a volume-uniform LOCAL analytic correction to the
preintegration action, and FK19 sharpens one actual quadratic term.
They do not control the connected logarithm of the integral of the
remaining cubic and higher fluctuation terms, its marginal projection,
or the hard complement. Product errors need not remain small as the
number of links grows. Likewise a collection of individually nonzero
kernels does not make an integrated complex-source denominator nonzero.
To upgrade UL's reviewed every-increment Gaussian bracket to a finite-u
coupling map, an interacting/source-local estimate for that connected
remainder, with the actual support-size norm and normalization, remains
necessary. HINT2_55 R2.3 separately names SF-g, RLF-delta, SF-cont and
SF-infinity; this scalar theorem does not discharge them. Neither
continuum existence nor a physical mass gap follows from FK2.

## 9. Normalizations tested by the finite controls

For SU(2), write a matrix as `m0 I+i sum m_a sigma_a`, with complex
quaternion coordinates. Direct multiplication in FK1 gives
`phi(W)=h dot w`, where `h0=(m0_plus+m0_minus)/2` and
`h_a=(m_a_plus-m_a_minus)/2`. Probability Haar is uniform S^3.
Its even monomial moments give
`Z_t=sum_(k>=0) [t^2(h dot h)/4]^k/[k!(k+1)!]`, the entire function
`2 I_1(t sqrt(h dot h))/(t sqrt(h dot h))`. The dot is bilinear; there
is no conjugation. This also rebuilds the corrected dual-quaternion
convention rather than repeating STEP55's rejected plus-sign formula.
The HS sphere radius is sqrt(2), so
`h_2=1/(4sqrt(2)pi^2)` and FK15's identity prefactor is sqrt(2/pi).

The identity first correction can be found without a Bessel citation.
Evenize the local integrand in X, rescale real X by t^-1/2, and apply
the polynomial-times-Gaussian majorant of FK14. Dominated convergence
identifies the first coefficient as the Gaussian expectation of
`j2-f4+f3^2/2`. The same evenized estimates on a smaller complex t sector
give a uniform remainder little-o(t^-1), so Cauchy also differentiates
this first-coefficient statement. At the identity f3=0.
With q=|x|^2/4, the Gaussian has covariance 2I_3. FK12 contributes
`-E|x|^2/6=-1`, and `-f4=|x|^4/96` contributes 5/8, giving -3/8.
The exact Bessel formula independently checks this coefficient and
the coefficient -3/8 of t^-2 in 1-c_2(t) at the sampled t values.

For SU(3) scalar S and lambda the integrand is a class function. Exact
probability Weyl integration uses the two angles theta_1,theta_2,
theta_3=-theta_1-theta_2, with density
`prod_(i<j)|exp(i theta_i)-exp(i theta_j)|^2/[6(2pi)^2]`.
To rebuild this measure factor, diagonalize a regular unitary matrix.
Each off-diagonal conjugation direction is multiplied by
`exp(i theta_i)-exp(i theta_j)`; its two real coordinates contribute
the squared modulus. The diagonal angle metric contributes only a
constant. Normalization fixes that constant: expand the squared
Vandermonde determinant into its two permutation sums. With
theta_3=-theta_1-theta_2, a term has zero torus character only when
the two exponent permutations agree (their component differences sum
to zero and cannot be a nonzero constant vector). There are six such
terms. The singular eigenvalue set has Haar measure zero, and continuity
extends the formula to these integrands. Thus no six colour directions
have been replaced by an unweighted two-angle law.
This is still the full eight-dimensional Haar integral; the six root
directions are in its Vandermonde. At S=I, the leading rescaled quadratic
is `(y1^2+y1 y2+y2^2)/3`. Its covariance is
`[[2,-1],[-1,2]]`, determinant factor 2pi sqrt(3), and the Gaussian
moment of `(y1-y2)^2(2y1+y2)^2(y1+2y2)^2` is 324 (Wick pairing).
Thus the prefactor is `27sqrt(3)/pi`. In all eight HS coordinates,
the Haar quadratic contribution is -6 and the quartic phase contribution
is +5, giving first correction -1. The latter follows by pairing the
four matrix entries with
`sum_a (T_a)ij(T_a)kl=-(delta_il delta_jk-delta_ij delta_kl/N)`:
at covariance N I_D, `E tr X^4=N^2(2N^3-5N+3/N)=360` for N=3,
and 360/(24N)=5. This check would detect dropping the Haar factor.

The constructed noncommuting SU(3) pair separately tests all eight
Hessian directions and the nonzero scalar odd term. The actual L=3
paired contour family tests the path count, inverse continuation and
arbitrary-holonomy brick center. Larger algebra probes are labelled as
such; they do not enlarge the conservative analytic radius in FK3.
Nor are the sampled stiffnesses certified to exceed the conservative
t_0 prescribed in FK15: they test the exact normalization, signs and
observed approach, not a numerical value of the uniform theorem constant.

The first launch was resource-only: 49% free memory failed the required
50% gate, so no numerical child ran. The next gate passed at 54%; the
single actual numerical run produced **35/35**, including five detected
intentional mutations, in 0.775 seconds with sampled peak RSS 136304 KiB.
The full SU(2) original/translated integrals agreed with the exact
formula within 3.0e-15. The SU(3) grid comparison agreed within 2.5e-15;
its identity tE values were -1.05839, -1.02809 and -1.01379. The full
eight-colour Hessian difference was 5.73e-9. Actual S4-prime enumeration
gave 1944 paths, length at most 11 and 459 distinct reader links.

One criterion's subleading sign was corrected analytically BEFORE any
numerical execution: since `E_t=-3/(8t)+...`, the t^-2 coefficient in
`1-c_2(t)=3/(2t)-E_t'` is -3/8. The tolerance was unchanged. The
[pre-execution amendment](checks/finite_coupling_kernel_preexecution_amendment.json)
preserves the original criteria text, old/new hashes, exact code-condition
change and its time, after the resource-only failure and before the run.
This is not a retroactive passing result. The
[complete results](checks/finite_coupling_kernel_01_results.json), raw
stdout/stderr, resource gates and runner are bound by the
[freeze receipt](checks/finite_coupling_kernel_receipt.json). The
[read manifest](checks/finite_coupling_kernel_read_manifest.json) records
complete and selected source reads separately. No new numerical replay
is needed merely for a prose change outside the numerical claims.
