# Fixed-law image noise, current-sector scope and physical reconstruction

Personal proof draft, 2026-09-14. No independent review or formal audit.
Fixed-law Gaussian photons remain open. The claims below identify actual
model observables and a conditional scaling mechanism, not a selected
native probability law or an axiom contradiction.

## 1. Positive lift and actual score at fixed parameters

Fix beta>0 and finite N>=2 on the oriented nearest-neighbor four-lattice
Z^4 or its periodic four-tori. The link angles theta_e are2pi a_e/N with
a_e in Z/NZ. Define phi_beta(u)=sum_k exp[-beta(u-2pi k)^2/2] and the
finite-periodic probability law proportional to product_p phi_beta((dtheta)_p).
Here d is the oriented cochain coboundary and positive plaquette orientations
are the six ordered pairs mu<nu. Its positive image representation has,
conditional on all angles theta, independent plaquette labels k_p with

 P(k_p=k|theta) proportional to exp[-2pi^2 beta(k-t_p)^2],
 t_p=(dtheta)_p/(2pi).

Put X_p=sqrt(beta)((dtheta)_p-2pi k_p) and
Y_p=E[X_p|theta]=-phi_beta'((dtheta)_p)/(sqrt(beta)phi_beta((dtheta)_p)).
Thus Y is an actual bounded local clock observable; X is an auxiliary
real lift. Let xi_p=X_p-Y_p and v_p(theta)=E[xi_p^2|theta].
This conditional kernel is periodic in the plaquette angle, so choosing a
different representative of dtheta changes k labels but not the X law.

For completeness, the centered lattice representation on a finite torus
requires no phase theorem. Write theta=2pi a/N and z=da-Nk. Its image is
M=d Z^E+N Z^P, a full-rank lattice since it contains N Z^P. The finite
group homomorphism d:(Z/NZ)^E->(Z/NZ)^P has constant fiber size on its
image. Thus every z in M has the same number of clock preimages, and the
marginal weight of z is proportional to exp(-|z|^2/(2sigma)), with
sigma=N^2/(4pi^2 beta). Completing the square gives the real MGF as
exp(||h||^2/2) times a shifted theta divided by its centered value.
Poisson summation has positive Fourier coefficients and bounds that ratio
by one. This proves the finite-volume domination used below.

## 2. Strict conditional variance and uniform image moments

Write c=2pi^2 beta. Choose a nearest integer k0 to t and r=t-k0 in[-1/2,1/2].
Relative weights satisfy

 w(k0+n)/w(k0)=exp[-c(n^2-2nr)] <= exp[-c(n^2-|n|)].

The sum of all relative weights is at most

 D_beta = 3+2exp(-2c)/(1-exp(-4c)),                     (2.1)

because the n=0,+/-1 terms are at most3 in total, and for n>=2 the
successive n(n-1) exponents grow by at least4. One neighboring integer
in the direction of r has weight at least exp(-c) times the mode weight.
Consequently p(k0)>=1/D_beta and p(k0+s)>=exp(-c)/D_beta for one s=+/-1.
Using Var(K)=1/2 sum_{k,l}p_kp_l(k-l)^2,

 v_p(theta) >= v_min(beta)
 :=4pi^2 beta exp(-2pi^2 beta)/D_beta^2 >0.             (2.2)

This is a deliberately loose uniform lower bound, independent of N and
the volume. Its state average can also be read from the local action
curvature. For A(u)=-log phi_beta(u), differentiating the conditional mean
gives Y'(u)=sqrt(beta)(1-v(u)), hence

 v(u)=1-A''(u)/beta.                                  (2.2a)

The variance average is therefore1-E[A'']/beta in each orientation or
invariant sector. This identity is a single-plaquette derivative of the
specified image kernel; it uses no integration by parts over clock angles.

The same relative-weight estimate bounds all conditional
moments of X and xi uniformly over theta at each fixed beta: a polynomial
in |n| times exp[-c(n^2-|n|)] is summable. These bounds also yield a
uniform analytic neighborhood of the conditional characteristic function.

For every real finite-support h, conditional independence therefore gives

 E|<h,X>|^2 = E|<h,Y>|^2+E sum_p h_p^2 v_p(theta)
             >= v_min(beta)||h||^2.                   (2.3)

The equality includes any possible nonzero mean in its raw second moments;
E[xi|theta]=0 removes the cross term. The corresponding covariance matrix
identity is Cov(X)=Cov(Y)+E diag(v_p).

For centered periodic laws the lattice-Gaussian completion-of-square bound
is E exp(<h,X>)<=exp(||h||^2/2), and Jensen gives the same bound for Y.
These inequalities pass to any subsequential infinite-volume limit of the
periodic clock laws by continuity of the conditional image moment kernel
and its uniform finite-beta tails. They are not asserted for every
arbitrary-boundary Gibbs state without this hypothesis.

It follows that a fixed-beta periodic-limit X field, normalized by a^-2
under macroscopic smearing, cannot converge to a pure closed Maxwell
Euclidean field with covariance alpha P_e. Choose a nonzero compact
coexact test f=d^*eta. Then P_e f=0, whereas cell-average sources satisfy
||J_a f||^2->||f||^2 and(2.3) gives a positive limiting lower second-moment
bound. Gaussian domination gives uniform integrability, so convergence in
distribution to zero would contradict that lower bound.

This is a statement about the auxiliary lift. It neither disproves
Maxwell scaling of Y nor rules out a photon in the physical OS quotient.
The varying-beta constructions avoid it because v_min(beta) tends to zero.

## 3. A conditional white-noise limit

Let mu be a translation-invariant infinite-volume clock law at these fixed
parameters. For the bounds above and tightness conclusions, take mu to be
a periodic-limit state; the conditional-noise calculation itself only
needs translation invariance and the specified image kernel.

For smooth compactly supported real two-form tests f, define
(J_a f)_{x,I}=a^-2 integral_{C_{x,I}} f_I, where for each orientation I,
C_{x,I} are disjoint side-a four-cells centered at the corresponding
plaquette midpoints and tiling R4. Thus ||J_a f||<=||f||_2. Write h=J_a f,
with h_p of order a^2, ||h||=O(1), and
max_p|h_p|=O(a^2). For a fixed finite linear combination of such tests,
the uniform image moments yield, when max|h| is sufficiently small,

 log E[exp(i<h,xi>)|theta]
 =-1/2 sum_p h_p^2 v_p(theta)+R_a(theta),
 |R_a(theta)|<=C_beta sum_p|h_p|^3
              <=C_beta max|h| ||h||^2 ->0.            (3.1)

A logarithm branch exists uniformly near one for each single-site factor.
The centered third-order remainder follows from Taylor's formula and a
uniform third absolute moment, then the analytic log expansion. More
explicitly, for a centered single-site noise with variance v and third
absolute moment m3, put zeta=v u^2/2. When zeta<1,

 |log E exp(iu xi)+v u^2/2|
 <=m3 |u|^3/6+zeta^2/[2(1-zeta)].                     (3.1a)

Here |E exp(iu xi)-1|<=zeta, and the second term bounds the remainder
of log(1+z). Uniform fixed-beta moment bounds make this uniform in theta.
Summing factor logarithms is valid by conditional independence. It is not an
assumption that the conditional field is Gaussian at finite a.

For each positive orientation I, let V_I=E_mu[v_{0,I}|I_inv], where I_inv
is the sigma-algebra invariant under lattice translations. Weighted
mean-ergodic averaging gives

 sum_x (J_a f)_{x,I}(J_a g)_{x,I} v_{x,I}
 -> V_I integral_R4 f_I(x)g_I(x)dx                     (3.2)

in L2(mu). To verify the weighted form, first take a compactly supported
step weight on finitely many rectangles, then apply the L2 mean ergodic
theorem to their expanding rectangular lattice sums. Translated rectangles
have the same error norm because the translations are unitary and commute
with the invariant projection. Uniform boundedness of v and Riemann sums
control continuous-weight approximation. Finally replacing h by a^2 times
sampled smooth f has vanishing l2 error, and Cauchy-Schwarz transfers(3.2).

If mu is translation ergodic, V_I are constants. If it is also invariant
under the supplied four-dimensional cubic symmetries, all six constants
coincide, v_bar. No assertion is made that a given periodic-limit state is
ergodic. Without ergodicity the V_I may be random, and independence must
be conditioned on that invariant data.

For any bounded theta-measurable variable B_a, (3.1)–(3.2) imply

 E[B_a exp(i< J_a f,xi>)]
 -E[B_a exp(-1/2 sum_I V_I||f_I||_2^2)] ->0,           (3.3)

provided sup_a||B_a||_infinity<infinity. This is a stable characteristic
identity, not merely convergence of the noise marginal.

In particular, along any subsequence on which the actual score field Y_a
and V=(V_I) have a joint distributional limit(F,V), the joint lift limit is

 (Y_a,X_a,V) -> (F,F+W_V,V),                           (3.4)

where W_V is conditionally centered Gaussian two-form white noise,
Cov(W_V(f),W_V(g)|F,V)=sum_I V_I<f_I,g_I>, and is conditionally independent
of F given V. Under ergodicity, this is ordinary independent white noise.
The finite-dimensional assertion follows from(3.3) with
B_a=exp(i<Y_a,g>+i t dot V); Cramer-Wold then identifies every joint law.

For periodic-limit mu, the inherited uniform L2 test bounds make both X_a
and Y_a tight in local H^-s for s>2. Indeed, after multiplication by a
compact cutoff, an orthonormal Dirichlet Laplacian basis in a bounded
four-dimensional domain gives E||T_a||_{H^-t}^2 bounded by a constant times
sum_j(1+lambda_j)^(-t), finite for t>2. Choose2<t<s and use the compact
embedding H^-t->H^-s, then exhaust space by countably many bounded domains.
The test variance bound applies to cell-integral projections of all L2
functions, so its constant is uniform in a. The white-noise limit has that
regularity too. Hence(3.4) can be promoted to joint local-distribution
convergence along subsequences, with the explicit assumption that Y_a has
the named limit. No Gaussianity of F is inferred.

## 4. Independent white noise and the strict positive-time OS space

Let F be any real random two-form distribution whose law is reflection
invariant and reflection positive with the tensor reflection: electric
components change sign,
magnetic components do not. Assume time-translation invariance and the
usual OS time-translation action exists. Let W be an independent white
two-form noise of constant nonnegative diagonal orientation covariance
which respects the reflection, and set X=F+W.

Use bounded cylinder functions with all test supports strictly in t>0.
For a cylinder function A define TA(F)=E_W[A(F+W)|F]. White-noise
restrictions to t>0 and t<0 are independent. Covariance invariance under
reflection, including the tensor signs, implies

 <Theta A(X) B(X)> = <Theta TA(F) TB(F)> .             (4.1)

Thus X is reflection positive on this algebra, and T is an isometry of
the corresponding pre-Hilbert quotient into that of F. For exponential
cylinders A_f(X)=exp(iX(f)),

 TA_f(F)=exp(-1/2 sum_I v_I||f_I||_2^2) exp(iF(f)).    (4.2)

The scalar is strictly positive for every test f, so the range contains
all finite linear combinations of exponential cylinders of F. Their
span is dense in the cylinder L2 space: if a finite-measure signed density
annihilates all characters, uniqueness of finite-dimensional Fourier
transforms makes it zero, then conditional expectations over cylinders
are dense. Passing to the OS completion gives a unitary onto the physical
Hilbert space of F. The vacuum is preserved.

Because white covariance is time-translation invariant, T commutes with
positive-time translations. It therefore intertwines the reconstructed
contraction semigroups and their nonnegative generators. Independent
white contact noise changes Euclidean coincidence correlations but adds
no physical states or energies in this strict positive-time reconstruction.
This conclusion is conditional on the limiting law and RP/semigroup
hypotheses; it does not prove a lattice continuum limit or a mass gap.

A random invariant-sector noise variance does NOT automatically give the
same isometry by replacing v with its average. The conditional mixture
must retain V as part of the state or supply additional factorization.
This is the same distinction already visible in(3.3).

## 5. What the current sector can and cannot establish

Let W be standard two-form white noise on R4 and let F=P_e W be the
Gaussian Maxwell field, with Fourier P_e(p)=d(p)d(p)^*/|p|^2 away p=0.
For every compact smooth closed two-form h=dj,

 F(h)=W(P_e h)=W(h).

Consequently W and F have identical joint laws on all such tests, and
identical current laws d*W=d*F. The first field has no Bianchi constraint;
the second is closed. Their full covariances are I and P_e, respectively.
For F the current covariance is the differential contact operator d*d,
so strict positive-time current-only cross-reflection covariances vanish.
Wick's theorem makes every centered current Wick polynomial a null OS
vector. The current-only Gaussian OS Hilbert space is the vacuum line.
The full Maxwell field instead has a nonzero physical vector already
from a magnetic component F_12. At spatial momentum p with p_1^2+p_2^2>0,
its strict positive-time covariance kernel is

 (p_1^2+p_2^2)/(2|p|) exp[-|p|(t+s)].                 (5.1)

This follows by Fourier integration of
(p_1^2+p_2^2)/(p_0^2+|p|^2). A smooth spatial Fourier test supported where
the prefactor is positive and a nonzero positive-time Laplace transform
has strictly positive OS norm. Thus the full field is not the vacuum
current-only theory. No full mode-count theorem is needed for this control.
Knowing only the current-sector limit cannot identify the full physical
space or its propagating modes.

Driver1987 proves the explicitly restricted current-sector statement for
continuous U(1) under its specified Gibbs-state hypotheses. Nothing here
claims an error in that theorem. The finite-clock sum is not the continuous
Haar integral required in its integration-by-parts identity, and a full
field phase statement needs additional information even when that identity
is available.

The finite-clock score itself supplies a separate observable-scope control.
For N=2 every plaquette angle is0 or pi modulo2pi. Evenness and periodicity
of phi imply phi'(0)=phi'(pi)=0, so Y is identically zero at every beta.
The image noise still has the strictly positive variance(2.2). This is an
exact statement about the chosen score field, not about every observable
or phase of the N=2 clock theory. At N=3, beta=1 and angle2pi/3 the score
is nonzero; no universal score-vanishing conclusion is drawn.

## 6. Next obligation: actual-score connected correlations

A fixed-law Gaussian photon theorem should control the actual score field
on general two-form tests, including its nonlocal covariance and higher
connected correlations. A contact part may be harmless for the physical
OS space if Gaussianity and independence are established; merely naming
it contact noise is not a proof of either property.

Next derive a quantitative cumulant criterion and identify whether the
positive current expansion supplies it. Uniform covariance sandwiching,
centered Gaussian MGF domination, and a small but fixed covariance error
do not themselves force every higher cumulant to vanish. Any unclosed
connected-correlation estimate must remain an explicit proof obligation.
