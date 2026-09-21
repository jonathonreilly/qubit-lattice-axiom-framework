# Independent axis-balanced context-exchange check

## Result

Both supplied exchange implementations preserve every homogeneous product
law. Their exact homogeneous currents agree and admit the usual strictly
convex product entropy throughout the seven-probability interior.

For fixed parameters, a nonzero direction-independent pair in the full
six-field current Jacobian exists at **every** density 0<rho<1 exactly when

\[
\boxed{u=0,\qquad B=-\frac32 A,\qquad EA\ne0.}
\tag{1}
\]

The other four eigenvalues are zero, and the speed is density dependent:

\[
\lambda=\pm c(\rho)|\nu|,\ 0,0,0,0,
\qquad c(\rho)^2=\frac{4E^2A^2\rho^2(1-\rho)}3.
\tag{2}
\]

In particular, the proposed fixed witness u=0,E=1/2,A=2,B=-3 satisfies (1)
and has c(rho)=2rho sqrt((1-rho)/3). Uniform births keep a balanced homogeneous
background on this family of isotropic current Jacobians; they still change
its speed and add a reaction term. They do not turn the growing background
into a stationary one.

The earlier smooth-profile Euler argument applies after the rate bound,
current, and entropy potential are changed as explicitly checked below. This
is a conditional smooth-solution hydrodynamic theorem, not an exact
microscopic wave or a fluctuation theorem. No new primary source was read.

## 1. Rate bounds, covariance, and product stationarity

Write the context coefficient as C_s=A C_n+B C_q, with

\[
C_n=\Delta f[n(l)+n(r)]+\Delta n[f(l)+f(r)],\qquad
C_q=\Delta f[q(l)+q(r)]+\Delta q[f(l)+f(r)].
\]

The exact convex hull of the attainable (C_n,C_q) pairs is

\[
(-4,-4),\ (-2,-4),\ (4,0),\ (4,4),\ (2,4),\ (-4,0).
\]

Thus the sharp context-only bound is

\[
M(A,B):=\max|C_s|
=\max\{4|A|,\ 4|A+B|,\ 2|A+2B|\}.
\tag{3}
\]

This also follows by classifying a site as vacant, axial +, axial -, or
occupied transverse to i. Opposite axial endpoints give the extreme forms
4A and 4(A+B); an axial/transverse endpoint pair gives 2A+4B. The remaining
cases lie in their symmetric convex hull. Since |Delta f|<=2,

\[
|h_i|\le2|u|+|E|M(A,B).
\]

Therefore kappa0+max(h,0) is bounded below by kappa0 and above by
kappa0+2|u|+|E|M. The sufficient fixed choice

\[
K>|u|+\frac{|E|}{2}M(A,B)
\tag{4}
\]

makes K+h/2 strictly positive. The bound in (4) need not be the sharp combined
u,E bound. For the witness, M=8 and |h|<=4 is attained. K=3 and kappa0=1 give
rate ranges [1,5] for the respective implementations.

Under a signed coordinate permutation R, when R e_i=+e_j the transformed
four-site string retains its order and f_j(Ra)=f_i(a), s_j(Ra)=s_i(a).
When R e_i=-e_j its positive-j representation is (Rr,Rb,Ra,Rl), with
f_j(Ra)=-f_i(a) and s_j(Ra)=s_i(a). Both terms in h are unchanged in this
representation. This proves covariance under all 48 joint signed-coordinate
transformations, including the 24 proper cubic rotations. It is joint
space/content covariance. A permutation of unequal torus periods maps to
the correspondingly permuted torus, and is a symmetry of the same finite
torus only when it preserves those periods.

Swapping only the central endpoints sends h to -h, so either rate satisfies
c(eta)-c(eta^e)=h_e(eta). Every homogeneous product mu_p is invariant under
endpoint exchange. Its finite-torus master-balance residual is consequently

\[
(\mu_p H)(\eta)=-\mu_p(\eta)\sum_e h_e(\eta)=0.
\tag{5}
\]

For completeness, the u sum telescopes, and the context sum along a periodic
coordinate line is

\[
\sum_x\{T(x,x-1)+T(x,x+2)-T(x+1,x-1)-T(x+1,x+2)\}=0,
\]

where T(y,z)=f_y s_z+s_y f_z is symmetric. This proof works for arbitrary
signed A,B and for zero-probability labels as well. The four sites are
distinct under the period restriction. Bounded finite-range rates give the
ordinary local graphical construction on Z^3 and the corresponding
stationarity by expanding-torus local limits. Detailed balance is not
generally implied.

## 2. Exact nonlinear currents and entropy compatibility

Let p_a be the six occupied probabilities, p_0=1-rho, and distinguish the
one-site function q_i(a)=f_i(a)^2 from its mean

\[
q_i=p_{+e_i}+p_{-e_i},\quad m_i=\sum_a p_a f_i(a),\quad
\sigma_i=\sum_a p_a s_i(a)=A\rho+Bq_i.
\]

Put U_i=u+2E sigma_i and Z_i=u+4E sigma_i. For oriented current
j_a^i=c_i[1_{s_x=a}-1_{s_{x+e_i}=a}], endpoint antisymmetry eliminates the
swap-symmetric part of the rate. Independence of the outer sites gives,
for all seven labels including vacancy,

\[
\boxed{J_a^i(p)=\mathbb E_{\mu_p}j_a^i
=p_a\{U_i f_i(a)+[2E s_i(a)-Z_i]m_i\}.}
\tag{6}
\]

One direct derivation uses outer means 2sigma_i,2m_i and
E[Delta 1_a Delta f]=2p_a(f_i(a)-m_i),
E[Delta 1_a Delta s]=2p_a(s_i(a)-sigma_i).
In particular,

\[
J_0^i=-p_0 Z_i m_i,\quad J_\rho^i=p_0 Z_i m_i,\quad
\sum_{a=0}^6J_a^i=0.
\]

If R_i=2EA-u-4E sigma_i, the six equivalent q,m currents are

\[
J_{q_j}^i=m_i\{(U_i+2EBq_i)\delta_{ij}+R_iq_j\},
\]
\[
J_{m_j}^i=U_i\delta_{ij}q_i+R_i m_i m_j+2EB\delta_{ij}m_i^2.
\tag{7}
\]

These are homogeneous product expectations. A spatially varying stochastic
law is not asserted to have a closed microscopic first-moment equation.

Let s(p)=sum_{a=0}^6 p_a log p_a, lambda_a=log(p_a/p_0), and

\[
S=D^2s=\operatorname{diag}(1/p_a)+p_0^{-1}\mathbf1\mathbf1^T.
\]

At every interior p, not just balanced p,

\[
S J^i=U_i f_i+2E m_i s_i
=\nabla_p G_i,\qquad G_i(p)=(u+2E\sigma_i)m_i.
\tag{8}
\]

Here f_i and s_i in vector expressions are their six occupied-label values.
An explicit check of the required nonlinear symmetry is

\[
(S D J^i)_{ab}
=\frac{\delta_{ab}}{p_a}
\{U_i f_i(a)+[2E s_i(a)-Z_i]m_i\}
 +2E[f_i(a)s_i(b)+s_i(a)f_i(b)]
 -\frac{Z_i m_i}{p_0}.
\tag{9}
\]

Thus S D J^i is symmetric and S is positive definite. The thermodynamic
entropy flux is lambda dot J^i-G_i. Every directional interior current
Jacobian is similar to a real symmetric matrix and is diagonalizable with
real eigenvalues. The new s dependence has not spoiled entropy compatibility.

## 3. Complete balanced six-field linearization

Fix u,E,A,B when differentiating the six occupied probabilities, with vacancy
probability determined by their sum. At p_a=rho/6, q_i=rho/3 and m=0. Write

\[
C=A+B/3,\quad U=u+2E\rho C,\quad Z=u+4E\rho C.
\]

The six by six Cartesian current Jacobians are exactly

\[
(\mathcal A_i)_{ab}
=U f_i(a)\delta_{ab}
 +\frac{\rho}{6}\{2E f_i(a)s_i(b)
                  +[2E s_i(a)-Z]f_i(b)\}.
\tag{10}
\]

To expose every mode, use the invertible variables
delta q_i=delta p_{+i}+delta p_{-i},
delta m_i=delta p_{+i}-delta p_{-i}. Define

\[
\alpha=u+2E\rho(A+2B/3),\quad
\beta=\frac{\rho}{3}(2EA-u-4E\rho C),\quad
\gamma=\frac{2EA\rho}{3}.
\]

For a real direction nu, D=diag(nu_1,nu_2,nu_3), the full directional
Jacobian has block form

\[
\mathcal A(\nu)\sim
\begin{pmatrix}0&M\\N&0\end{pmatrix},\qquad
M=(\alpha I+\beta\mathbf1\mathbf1^T)D,\quad
N=D(\alpha I+\gamma\mathbf1\mathbf1^T).
\tag{11}
\]

This follows directly by differentiating (7); in particular the B term
contributes to both off-diagonal blocks and changes U to alpha. Omitting
that contribution would produce the wrong density tuning.

Let

\[
g=\alpha(\beta+\gamma)+3\beta\gamma,\qquad
Q=(1-\rho)Z^2.
\]

Then

\[
\alpha+3\beta=(1-\rho)Z,\quad
\alpha+3\gamma=Z,\quad \alpha^2+3g=Q.
\tag{12}
\]

The three squared speeds are the eigenvalues of
diag(nu_i^2)[alpha^2 I+g 11^T]. Consequently the complete characteristic
polynomial is

\[
\lambda^6-(\alpha^2+g)|\nu|^2\lambda^4
 +\alpha^2(\alpha^2+2g)
    \left(\sum_{i<j}\nu_i^2\nu_j^2\right)\lambda^2
 -\alpha^4 Q\nu_1^2\nu_2^2\nu_3^2.
\tag{13}
\]

No extra fields or extra eigenvalues have been discarded. The rank-one
reduction follows from det(mu I-XY)=det(mu I-YX) applied to MN. The matrix
alpha^2 I+g 11^T has eigenvalues alpha^2,alpha^2,Q>=0, consistent with (9).

For a unit axis direction the squared speeds are
(2alpha^2+Q)/3,0,0. For a unit body diagonal they are
alpha^2/3,alpha^2/3,Q/3. A nonzero speed common to all directions must appear
in both lists. Equality with Q/3 forces alpha=0; equality with alpha^2/3
would force alpha^2+Q=0 and gives no nonzero speed. Thus at a fixed interior
density, a nonzero direction-independent pair exists exactly when
alpha(rho)=0 and EA!=0. With alpha=0, Z=2EA rho and the pair is (2).

Requiring this at every interior rho makes the affine function
u+2E rho(A+2B/3) vanish identically. Excluding the zero-speed case gives
precisely (1). This proves necessity and sufficiency, not just a witness at
sampled densities.

## 4. The proposed fixed witness and its extra modes

For u=0,E=1/2,A=2,B=-3,

\[
s_i=2n-3q_i(a),\quad\sigma_i=2\rho-3q_i,
\quad G_i=(2\rho-3q_i)m_i.
\]

At every balanced interior density, U=rho, alpha=0,
beta=2rho(1-rho)/3, gamma=2rho/3. For nu!=0 the Jacobian has rank two, a
four-dimensional kernel, and the diagonalizable spectrum (2). The zero
modes are precisely the two independent axis-population imbalances
sum_i delta q_i=0 and the two vector polarizations transverse to nu. The
longitudinal equations in the linearized Euler system are

\[
\partial_t\delta\rho+2\rho(1-\rho)\nabla\cdot\delta m=0,
\qquad
\partial_t\delta m+\frac{2\rho}{3}\nabla\delta\rho=0.
\tag{14}
\]

The axis-population modes still enter the nonlinear currents (7), so (14)
does not eliminate them from nonlinear Euler dynamics.

For example, c^2 is 1/16,1/6,3/16 at rho=1/4,1/2,3/4 respectively.
The general untuned family is not direction independent: the exact control
u=1/3,E=2/5,A=3/2,B=-2,rho=1/2 has axis speed squared 41/150, while its
diagonal squared speeds are 4/75,4/75,1/6.

The endpoints rho=0,1 are excluded from the interior theorem, and c tends
to zero there. At rho=1 the formal six-variable balanced Jacobian in (11)
has M=0 and N=(2EA/3)nu 1^T under (1); it can be nonzero nilpotent despite
having only zero eigenvalues. Its restriction to the fixed-full-occupancy
tangent sum delta q=0 is zero. Interior diagonalizability and the positive
vacancy entropy metric must not be extended to that boundary without a
separate argument. At rho=0 the tuned Jacobian is zero. At nu=0 all six
spatial eigenvalues are zero.

These statements concern the entire current Jacobian and its Euler
linearization. Four zero characteristic modes do not mean that four
microscopic degrees of freedom stop exchanging, nor is an exact finite-N
wave dispersion or fluctuation limit supplied by this spectrum. Isotropy
of this linear pair also does not establish continuous rotational symmetry
of the nonlinear flux or the finite lattice dynamics.

## 5. Uniform births: preserved tuning, reaction, and scaling

Add births of each label at a vacant site at rate epsilon. Exchange alone
annihilates every homogeneous product measure, while the birth generator
acts independently at sites. Hence the exact homogeneous product evolution
for the unscaled process is

\[
p_0(t)=p_0(0)e^{-6\epsilon t},\qquad
p_a(t)=p_a(0)+\frac{p_0(0)}6(1-e^{-6\epsilon t}).
\tag{15}
\]

In particular, m_i is constant and q_i-rho/3 is constant. A balanced
homogeneous product remains balanced. Under (1), unlike a tuning at a
single density, its instantaneous current Jacobian stays isotropic at every
interior time. Its speed c(rho(t)) changes and eventually tends to zero as
rho(t) tends to one. There is no claim of isotropy about an arbitrary biased
product: the balanced-background premise still matters.

For the Euler generator N H_N+epsilon B_N, the birth source is
r_a=epsilon(1-rho). Linearizing this PDE about a spatially homogeneous
balanced growing background in the witness gives

\[
\partial_t\delta\rho
+2\rho(t)(1-\rho(t))\nabla\cdot\delta m=-6\epsilon\delta\rho,
\qquad
\partial_t\delta m+\frac{2\rho(t)}3\nabla\delta\rho=0.
\tag{16}
\]

The two axis-population differences and two transverse Fourier components
remain zero modes of this linearized system. If its coefficients are
*frozen* at one density and wavevector k, the other temporal eigenvalues
obey

\[
z^2+6\epsilon z+c(\rho)^2|k|^2=0.
\tag{17}
\]

Thus even the frozen reaction system is not an undamped acoustic pair for
all wavelengths. The actual growing background has time-dependent
coefficients, so (17) is not a global time-translation-invariant dispersion
law for (16).

In Euler time, the finite reaction term above requires each-label
*microscopic* birth rate epsilon/N. Fixed microscopic epsilon under the
same acceleration instead gives N H_N+N epsilon B_N and the exact
homogeneous vacancy law p_0^N(t)=p_0(0)e^{-6N epsilon t}. It fills on a
vanishing Euler-time scale and does not meet a fixed positive-vacancy
interior premise at positive times. All-density isotropic tuning does not
repair this distinct scaling issue.

For the finite-reaction scaling N H_N+epsilon B_N, a completely empty initial
product is also outside the interior entropy proof at time zero. Its
homogeneous evolution is known exactly from (15). In that scaling the
interior theorem can be started at any positive time before a fixed finite
endpoint, with this exact product law supplying the new initial law.

With births a stationary homogeneous product must be full. Full occupancy
does not generally stop exchanges: under a balanced full product, expected
unequal-label activity is 5K/6 per edge for the linear implementation and
at least 5kappa0/6 for the positive-part implementation. A filled single-label
configuration remains an exception with no state-changing exchanges.

## 6. Applicability of the previously sealed Euler proof

The earlier independent Euler report is used as a proved argument with
specific hypotheses, not as a status label. Each load-bearing hypothesis is
verified for the new generator:

1. **Uniform rates and local support.** Equations (3)-(4) give a positive
   N-independent floor and a finite ceiling. The rate still reads just four
   sites. All nearest-neighbor endpoint exchanges, including exchanges of
   different occupied labels, have that floor.
2. **Reference invariance and entropy budget.** Equation (5) makes the
   uniform seven-state product pi_N invariant. The same jump entropy
   inequality therefore gives, for f_t=d mu_t/d pi_N and the unit-swap
   Dirichlet expression D_N,
   integral_0^T D_N(f_t) dt <= N^3(log 7+epsilon T)/(delta N) for
   N H_N+epsilon B_N. Only the value of delta changes.
3. **Block equilibration.** The floor still controls every internal unit
   adjacent transposition. The seven-count-vector sectors, their sorting
   proof of connectivity, and the bound C_P(m)=m^2 7^m are unchanged. The
   marginal Dirichlet comparison and canonical sampling argument apply to
   the new bounded four-site current (6). Canonical block-current variance
   remains O(1/m), and its mean converges to the new J. No frozen-exterior
   context generator is assumed to be canonical-stationary.
4. **Nonlinear closure identities.** The old entropy potential must be
   replaced by (8), and the current by (6). Equations (8)-(9) verify both
   S D J^i symmetry and partial_i lambda dot J^i=partial_i G_i. These give
   the linear cancellation and periodic constant-term cancellation in the
   relative-entropy argument. The new J is still a polynomial with bounded
   second derivatives on the closed probability simplex.
5. **Reaction term.** The alphabet, product entropy, and independent birth
   operator are unchanged. Thus the exact identity
   epsilon B_N^*nu/nu=sum_x(eta_x-p_x) dot S(p_x)r(p_x) holds as before,
   with r_a=epsilon p_0. The reaction-reference cancellation is unaffected.

It follows that, for a given periodic C^2 solution of

\[
\partial_t p+\sum_i\partial_iJ^i(p)=\epsilon p_0\mathbf1
\]

with all seven probabilities uniformly positive on [0,T], and initial
H(mu_0^N|nu_0^N)=o(N^3), both implementations satisfy

\[
\sup_{t\le T}H(\mu_t^N\mid\nu_t^N)/N^3\longrightarrow0,
\tag{18}
\]

and empirical profiles converge in probability uniformly in time against
smooth test functions. For example the old error estimate with m=ell^3 is
still valid with new fixed constants:

\[
\sup_{t\le T}\frac{H(\mu_t^N\mid\nu_t^N)}{N^3}
\le C_T\left[\frac{H(\mu_0^N\mid\nu_0^N)}{N^3}
+\ell^{-1}+m^{-1}+\ell/N+(\ell/N)^2
+\sqrt{m^3 7^m/N}\right].
\]

Taking odd ell tending slowly to infinity with ell^3<=log N/(2 log 7)
proves (18). The changes are therefore explicit in the rate constants,
local current, and entropy potential. Smooth-solution existence on the
chosen interval is still an assumption; no post-shock, boundary-density,
microscopic fluctuation, or tagged-record theorem is inherited.

## 7. Independent checks and source identities

`independent_check.py` was written here without importing an earlier checker
or author file. It exhausts all 7^4 local tuples and all 48 signed cubic
transformations, computes the exact coefficient hull in (3), and checks
each coefficient of the pointwise periodic balance. Direct four-site
product summation computes all seven currents and all six probability
derivatives, including the vacancy derivative, for both rate implementations
at three witness densities and at balanced and biased untuned controls.
All parameters are held fixed in those derivatives.

The controls also check nonlinear entropy symmetry, the exact six-field
block representation, complete characteristic polynomials and four-dimensional
kernels in four directions, the generic anisotropy example, and the frozen
birth polynomial (17). A direct 2,401-state four-cycle forward equation
checks exchange product stationarity and the homogeneous exchange-plus-birth
product flow. The four-cycle is a directional finite control, not a substitute
for the three-dimensional pointwise balance proof. `RUN.log` contains the
complete final output, `RESULTS.json` its byte-identical structured copy,
and `PROGRESS.log` records completed check groups. All 66 grouped exact
checks passed with Python 3.13.5 and SymPy 1.14.0. At the witness rates above,
the computed balanced full-occupancy activity is 5/2 per edge for the linear
implementation and 35/27 for the positive-part implementation. The analytic
identities, rather than the finite density/direction sample, establish the
all-density conclusion.

The only reused mathematical evidence is the earlier independent work:

| Source | SHA-256 |
|---|---|
| `../independent_context_exchange/REPORT.md` | `277ba40b64842d128a2e46ca7bd468a7efc7c4d401e629648d440588e7784713` |
| `../independent_context_exchange/PRE_SOURCE_SEAL.json` | `7e924cc17d429c64ceb8e1b626f874dc6386ac2618ec7399af2879dce8f4d5f5` |
| `../independent_context_euler/REPORT.md` | `60aaef142f97aea228be967a711880c5272328e5173d6c8df8c033176605a1e3` |
| `../independent_context_euler/independent_check.py` | `5ebc1ce0750c658649447e0a0d8da146b2ab64bd4fd83d232329281d1df4b3d4` |
| `../independent_context_euler/PRE_SOURCE_SEAL.json` | `48dda0ccb30539906dd6274bbf8736258727077c0018bb89c604f491164a1fa9` |

These identities were verified before this derivation and are rechecked by
the seal script. No new primary context, axis-balanced, fluctuation, Euler,
or simulation source was read. No external literature was imported. The
new source/output identities are in `PRE_SOURCE_SEAL.json`. This is a bounded
independent scientific derivation, not an audit or retained-status verdict.
