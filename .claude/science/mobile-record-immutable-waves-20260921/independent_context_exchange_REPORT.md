# Independent check of the context-exchange generator

## Result and scope

Both supplied rate implementations are strictly positive, bounded, jointly
cubic-covariant local exchange rules. Every homogeneous product distribution
is stationary for the exchange process. They have the same exact homogeneous
mean currents, although their symmetric traffic differs. For an interior
balanced density 0<rho<1, the current Jacobian has a nonzero
direction-independent propagation speed **if and only if**

\[
u+2E\rho=0,\qquad E\ne0.
\]

There is then one pair of speeds and four zero modes:

\[
\lambda=\pm c_*|\nu|,\ 0,0,0,0,
\qquad c_*^2=\frac{4E^2\rho^2(1-\rho)}3.
\tag{1}
\]

These are eigenvalues of a homogeneous-current Jacobian. This calculation
does not establish a microscopic wave, a hydrodynamic limit, or a closed
inhomogeneous first-moment equation. Independent births preserve an exact
time-dependent homogeneous product family, but its density changes and
therefore leaves any fixed interior tuning. Filling does not in general stop
this exchange process, which also exchanges unequal occupied labels.

The input is reproduced in `INPUT.md`. No primary calculation was accessed.
All evidence in this directory was independently written from that input.

## 1. Rate bounds, covariance, and stationary products

Write f=f_i, Delta f=f(a)-f(b), Delta n=n(a)-n(b), and

\[
C=\Delta f\,[n(l)+n(r)]+\Delta n\,[f(l)+f(r)].
\]

The alphabet constraints imply |Delta f|<=2 and |C|<=4. If both endpoints are
occupied, Delta n=0; if precisely one is occupied, each of the two outer
contributions is at most 2 in absolute value; if both are vacant, C=0.
Consequently

\[
|h|\le2|u|+4|E|,\qquad
K+h/2\ge K-|u|-2|E|>0.
\tag{2}
\]

The positive-part implementation is at least kappa0. The bounds are uniform
and the dependence range is finite, giving the ordinary local graphical
construction on Z^3. A backward query at one site encounters at most six
incident dominating clocks and branches to at most four sites at an event.
The finite-time dependency cluster is therefore dominated by a finite-rate
branching process and is finite almost surely; acceptance uniforms then
construct the local trajectory.

Rotate or reflect both sites and occupied vectors by a signed coordinate
permutation R. If R e_i=+e_j, the four states remain in the same order and
f_j(Rs)=f_i(s). If R e_i=-e_j, positive-j orientation puts them in the order
(Rr,Rb,Ra,Rl), while f_j(Rs)=-f_i(s). Both Delta f and C are unchanged in
this reversed representation. Thus the rate rule is covariant under all 48
signed coordinate permutations, in particular the 24 proper cubic rotations.
This is joint space/content covariance. On a rectangular torus a permutation
of unequal periods maps to the correspondingly permuted torus; it is an
automorphism of that same finite graph only when it respects the periods.

For either implementation, exchange of the central endpoints sends h to -h
and obeys

\[
c(\eta)-c(\eta^{x,x+e_i})=h_i(\eta).
\tag{3}
\]

The four positions are distinct under the stipulated period bound. A
homogeneous product measure mu_p assigns the same mass to configurations
related by an exchange. Its finite-torus forward balance is therefore

\[
(\mu_p H)(\eta)=-\mu_p(\eta)\sum_{x,i}h_i(\eta).
\]

The sum vanishes pointwise. The u term telescopes. For the context term,
put S(y,z)=f_y n_z+n_y f_z on a periodic coordinate line. Its sum is

\[
\sum_x\{S(x,x-1)+S(x,x+2)-S(x+1,x-1)-S(x+1,x+2)\}=0,
\tag{4}
\]

by index shifts and symmetry of S. This proves stationarity for every p,
including zero-probability labels. Bounded finite-range local convergence of
expanding tori proves the same assertion on Z^3. This balance is not generally
detailed balance: a nonzero h is an exchange asymmetry.

The cross term is essential to this argument. On the four-cycle in direction
1, the state sequence (+e_1,0,0,+e_2) has sum
Delta f[n(l)+n(r)]=1, while the omitted cross term sums to -1. Deleting that
term destroys product stationarity when E is nonzero. This is a control for
the supplied construction, not a counterexample to the complete rate.

## 2. Exact homogeneous currents

Let p_a denote each occupied-label probability, p_0=1-rho,
rho=sum_a p_a, m_i=sum_a p_a f_i(a), and
q_i=p_{+e_i}+p_{-e_i}. Define the oriented species current by

\[
J_a^i=\mathbb E_{\mu_p}
[(\mathbf1_{s_x=a}-\mathbf1_{s_{x+e_i}=a})c_i].
\]

The endpoint-symmetric part of c makes zero contribution, so (3) gives
J_a^i=(1/2)E[Delta 1_a h_i]. Independence gives outer means 2rho and 2m_i,
and

\[
\mathbb E[\Delta1_a\Delta f]=2p_a(f_i(a)-m_i),\qquad
\mathbb E[\Delta1_a\Delta n]=2p_a(1-\rho)
\]

for occupied a. Set

\[
A=u+2E\rho,\qquad B=2E-u-4E\rho.
\]

Then both implementations have exactly

\[
\boxed{J_a^i=p_a[A f_i(a)+B m_i]},\qquad
J_0^i=-(1-\rho)(u+4E\rho)m_i.
\tag{5}
\]

The sum over all seven species is zero. In particular,

\[
J_\rho^i=(1-\rho)(u+4E\rho)m_i,\quad
J_{q_j}^i=A\delta_{ij}m_j+Bq_jm_i,\quad
J_{m_j}^i=A\delta_{ij}q_i+Bm_im_j.
\tag{6}
\]

Neither K nor kappa0 appears in these means; changing them still changes
microscopic activity and can change fluctuation and relaxation behavior.

## 3. Six-variable Jacobian and directional spectrum

At p_a=rho/6, m=0, with 0<rho<1, the independent variables are the six
occupied probabilities; changing them also changes p_0. **The physical
parameters u,E remain fixed during differentiation.** For occupied a,b,

\[
(\mathcal A_i)_{ab}
= A f_i(a)\delta_{ab}
 +\frac{\rho}{6}[2E f_i(a)+B f_i(b)].
\tag{7}
\]

For an arbitrary real direction nu, let t_a=nu dot v_a. Equivalently,

\[
\mathcal A(\nu)=\sum_i\nu_i\mathcal A_i
=A\,\mathrm{diag}(t)
 +\frac{\rho}{6}(2E\,t\mathbf1^T+B\mathbf1t^T).
\tag{8}
\]

In the invertible coordinates (delta q,delta m), write D=diag(nu),
b=rho B/3, c=2E rho/3, and J=11^T (a 3 by 3 matrix). Then

\[
\mathcal A(\nu)\sim
\begin{pmatrix}0&M\\N&0\end{pmatrix},\quad
M=(AI+bJ)D,\quad N=D(AI+cJ).
\tag{9}
\]

By the identity det(mu I-XY)=det(mu I-YX), the squared-speed polynomial is
the characteristic polynomial of

\[
\mathrm{diag}(\nu_1^2,\nu_2^2,\nu_3^2)(A^2I+gJ),
\quad g=A(b+c)+3bc.
\]

Define Q=(1-rho)(u+4E rho)^2. Directly,

\[
A^2+3g=(A+3b)(A+3c)=Q\ge0.
\tag{10}
\]

Thus the squared speeds are nonnegative: A^2I+gJ is positive semidefinite,
and its product with diag(nu_i^2) has the characteristic polynomial of the
corresponding symmetric positive semidefinite sandwich. This statement does
not assert diagonalizability in every degenerate parameter case.

For |nu|=1, put S_2=sum_{i<j}nu_i^2 nu_j^2 and S_3=nu_1^2 nu_2^2 nu_3^2.
The six-speed polynomial is obtained by substituting mu=lambda^2 into

\[
\mu^3-(A^2+g)\mu^2
 +A^2(A^2+2g)S_2\mu
 -A^4(A^2+3g)S_3.
\tag{11}
\]

In an axis direction the only potentially nonzero squared speed is
(2A^2+Q)/3; the other two squared speeds are zero. In a body-diagonal
direction they are A^2/3, A^2/3, Q/3. A nonzero speed common to *all*
directions must occur in both of these sets. Equality with Q/3 requires
A=0. Equality with A^2/3 requires A^2+Q=0 and therefore gives no nonzero
speed. This proves the necessity of A=0. For A=0, (9) has one nonzero pair
given by (1), a four-dimensional kernel, and is diagonalizable for
E!=0, 0<rho<1, nu!=0. This proves sufficiency as well.

A valid explicit witness is rho=1/2, E=1, u=-1, K=4 (or kappa0=1), giving
c_*^2=1/6. For comparison, u=E=1, rho=1/2, K=4 gives axis speed squared
25/6, versus diagonal squared speeds 4/3,4/3,3/2: generic cubic covariance
does not imply isotropy. At rho=0 or rho=1 the tuned nonzero pair disappears;
the six-variable derivative also needs a boundary-tangent interpretation
because the probability simplex is not open there. E=u=0 has zero mean
current Jacobian.

At the tuning, the density and vector-current part of the *formal*
local-product Euler linearization reads

\[
\partial_t\delta\rho+2E\rho(1-\rho)\nabla\cdot\delta m=0,\qquad
\partial_t\delta m+\frac{2E\rho}{3}\nabla\delta\rho=0.
\tag{12}
\]

It algebraically yields a wave operator with coefficient c_*^2. For an
inhomogeneous stochastic law, however, the generator expectation involves
joint local probabilities, not just p_a(x). Product stationarity at constant
p does not establish preservation of spatially varying products, local
equilibrium, or a hydrodynamic limit. Equations (7)-(12) are not the spectrum
of the microscopic Markov generator, nor an exact finite-wavevector lattice
dispersion relation. Establishing those stronger statements needs an
additional argument.

## 4. Adding independent births

Let every vacant site receive each occupied label at rate epsilon>0. The
birth source for first moments is exactly

\[
\dot p_a\big|_{\rm birth}=\epsilon p_0,\quad
\dot\rho\big|_{\rm birth}=6\epsilon(1-\rho),\quad
\dot m_i\big|_{\rm birth}=0,\quad
\dot q_i\big|_{\rm birth}=2\epsilon(1-\rho).
\tag{13}
\]

For any translation-invariant initial law, exchange contributes zero to each
one-site species mean by the current-divergence identity. Thus these mean
equations are exact in that class. For a homogeneous product initial law,
there is a stronger exact solution: products remain products, with

\[
p_0(t)=p_0(0)e^{-6\epsilon t},\qquad
p_a(t)=p_a(0)+\frac{p_0(0)}6(1-e^{-6\epsilon t}).
\tag{14}
\]

Indeed, the derivative of this product measure is its independent-birth
forward generator, while its exchange forward generator is zero at every
time by (4). Uniqueness gives the claim, first on tori and then locally on
Z^3. Product preservation here is a homogeneous statement, not a closure for
spatially varying products. Mean polarization stays constant, but births do
not conserve realized total polarization or the six realized label counts.

For a balanced initial product with rho(0)<1, rho(t) increases strictly.
Fixed u,E can satisfy u+2E rho(t)=0 at at most one interior time when E!=0;
the stationary exchange family and its isotropic current pair do not become
a stationary growing family. The birth-source Jacobian is
-epsilon 11^T on the six probabilities, with density eigenvalue -6epsilon
and zero eigenvalues on label-difference directions. Treating a tuned
background as fixed would therefore already omit a reaction term, besides
omitting the actual drift of that background.

With births, a stationary homogeneous product must have rho=1. At full
occupancy the context rate reduces to h_i=(u+2E)(f_i(a)-f_i(b)), and
unequal occupied labels can continue to exchange. A filled single-label
configuration is unchanged by exchanges. Under a balanced full product, the
linear implementation has expected actual unequal-label exchanges per edge
per unit time 5K/6; the positive-part implementation has at least
5kappa0/6. Thus vacancy-only fixation arguments cannot be transferred to
this new generator. This activity statement is not an unproved assertion
about almost-sure lifetime hops of every infinite-volume tagged record.

## 5. Independent executable evidence and limits

Run `python3 independent_check.py > RUN.log 2>&1` in this directory. The
final run passed 46 grouped exact checks using Python 3.13.5 and SymPy 1.14.0.
The full stdout is `RUN.log`, identical byte-for-byte to `RESULTS.json`.
The checks include:

- All 7^4 local state tuples, all three axes, and all 48 signed coordinate
  permutations (345,744 local covariance cases), with exact coefficient
  bounds and endpoint-swap identities.
- Pointwise periodic-line balance on all 2,401 four-cycle configurations,
  and the explicit missing-cross-term failure above.
- Direct four-site product summation for all seven mean currents under a
  biased product and a balanced product, for both rate implementations.
- Direct derivatives of those product expectations in all six independent
  probabilities, at fixed u,E, for tuned and generic parameters. For example,
  the tuned derivative d J_{+e1}^1 / d p_{+e2}=1/6; differentiating u along
  the tuning relation would incorrectly give zero.
- The exact symbolic squared-speed polynomial and direct six-by-six
  characteristic polynomials along four unit directions. The tuned result
  is lambda^4(lambda^2-1/6) in all four directions; (9)-(11), not that finite
  direction sample, prove the all-direction statement.
- A direct 2,401-state forward-generator calculation on a four-cycle, with
  biased product probabilities: both the exchange stationarity residual and
  the exchange-plus-birth product-flow residual are exactly zero, for both
  rate implementations. This is a finite directional control; (4) proves
  the full cubic-torus result.
- Exact full-occupancy activity at the tuned parameters: 10/3 per edge for
  the linear implementation and 10/9 for the positive-part implementation.

An initial execution found a missing brace in a checker f-string before
any computation; `INITIAL_SYNTAX_FAILURE.log` preserves that failure. The
brace was corrected and the complete final run then succeeded. No theorem
or model was changed to obtain the successful run.

The proof establishes the algebraic and stationary statements above and
supplies explicit positive witnesses and anisotropy controls. No microscopic
wave, mixing, diffusion coefficient, hydrodynamic limit, or physical field
identification has been checked or claimed. `PRE_SOURCE_SEAL.json` records
complete hashes of the task input, report, checker, outputs, and checkpoint;
no author-source result was used to produce them.
