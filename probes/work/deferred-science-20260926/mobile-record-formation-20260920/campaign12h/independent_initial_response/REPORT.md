# Independent initial-response check

2026-09-20. Bounded mathematical check, sealed before access to any new
campaign12h author calculations. This is not an audit or a landing review.

## Model and normalization

Let G be a finite simple z-regular graph with n>=1 vertices. Its six-content
matrix W is strictly positive, symmetric, and has every row sum equal to six.
An empty x acquires a at rate epsilon times

\[
u_{x,a}(s)=\prod_{y\sim x:\,s_y\ne\varnothing}W(a,s_y).
\]

The specified occupied-vacant hops preserve content. All results below use
ordinary physical time and arbitrary epsilon>=0; no mixing or rare-birth
limit is taken. The global identities actually do not need graph regularity.

Let chi be a real, centered content eigenfunction, W chi=theta chi, and put

\[
\sigma_2=\frac16\sum_a\chi_a^2,\qquad
\sigma_3=\frac16\sum_a\chi_a^3.
\]

The independent homogeneous initial law is explicitly parameterized by

\[
P_h(s_x=\varnothing)=1-\rho,
\qquad P_h(s_x=a)=\frac\rho6(1+h\chi_a).
\tag{1}
\]

Here 0<=rho<=1 and h is small enough for nonnegative probabilities. This
choice fixes the perturbation normalization; sigma_2 is not silently set to
one. Write C_a for the total count of a, N=sum C_a, and M=sum chi_a C_a.

## Exact total-content identities, at every configuration

Define H_a(s)=sum_(x empty) u_(x,a)(s), B=sum H_a, J=sum chi_a H_a, and
D=sum chi_a^2 H_a. The row generator L obeys

\[
LC_a=\epsilon H_a,\qquad LN=\epsilon B,\qquad LM=\epsilon J,
\tag{2}
\]
\[
L(C_aC_b)=\epsilon(C_aH_b+C_bH_a+\delta_{ab}H_a),
\qquad LM^2=\epsilon(2MJ+D).
\tag{3}
\]

Proof: hops change none of these observables. Birth of a adds e_a to C and
chi_a to M, so expanding the increments gives (2)--(3). In particular, the
second moment is not obtained by squaring the first-moment equation:

\[
\frac{d}{dt}E M^2=2\epsilon E(MJ)+\epsilon E D,
\qquad
\frac{d}{dt}\operatorname{Var}M
=2\epsilon\operatorname{Cov}(M,J)+\epsilon E D.
\tag{4}
\]

The predictable quadratic-variation rate of the compensated M martingale
is epsilon D. For the count vector it is epsilon diag(H). These are exact
identities, but they are not generally closed equations for count moments.

## Instantaneous response under (1)

Independence, the row sum, and the eigenfunction identity give exactly

\[
E_h[1_{s_x=\varnothing}u_{x,a}]
=(1-\rho)\left(1+\frac{\rho\theta h}{6}\chi_a\right)^z.
\tag{5}
\]

Thus initial derivatives of the expected content per site m_h=E_h M/n and
the expected density r_h=E_h N/n are obtained by summing (5), respectively
with and without chi_a. Define delta m(t)=partial_h m_h(t)|_(h=0). Then

\[
\delta m(0)=\rho\sigma_2,\quad
\delta\dot m(0)=\epsilon z\theta\rho(1-\rho)\sigma_2,
\quad \dot r_0(0)=6\epsilon(1-\rho),\quad
\partial_h\dot r_h(0)|_0=0.
\tag{6}
\]

The instantaneous relative response per site is epsilon z theta (1-rho)
when rho sigma_2>0. Motion contributes zero to the *total* M; no local
transport closure was used to obtain this rate.

For content per record defined as the ratio of expectations
R_h(t)=E_h M(t)/E_h N(t), with rho>0, the denominator also grows. Consequently

\[
\delta R(0)=\sigma_2,\qquad
\delta\dot R(0)
=\epsilon(1-\rho)\sigma_2\left(z\theta-\frac6\rho\right).
\tag{7}
\]

In particular, a positive instantaneous per-site response need not be a
positive per-record response. The sign condition z theta rho>6 concerns
only this initial derivative, not an ordering transition.

The second-moment identities also have a useful independent initial check:

\[
E_h M(0)^2=n\rho\sigma_2+n\rho h\sigma_3+O(h^2),
\]
\[
\left.\frac1n\frac d{dt}E_h M(t)^2\right|_{t=0}
=\epsilon(1-\rho)\left[
\sigma_2(6+2z\rho\theta)
+h\sigma_3\left(3z\rho\theta+
\frac{z(z-1)\rho^2\theta^2}{3}\right)\right]+O(h^2).
\tag{8}
\]

For example, at h=0, E[M J]/n=(1-rho)z rho theta sigma_2 and
E[D]/n=6(1-rho)sigma_2. To get the linear term, separate the occupied
neighbors of a prospective birth from all other sites and use symmetry to
write sum_a chi_a(W chi^2)_a=theta sum_a chi_a^3. Also
E_h[D]/n=(1-rho)[6 sigma_2+h z rho theta sigma_3]+O(h^2).
These formulas allow sigma_3 to be nonzero; a vector-mode symmetry is not
assumed for a general eigenfunction.

## Expectation of a random ratio is different

Define A(s)=M/N for N>0 and A(s)=0 at N=0. This convention must be stated:
M/N is otherwise undefined on an event of positive initial probability.
Hops preserve A, and direct birth increments give

\[
LA=\frac{\epsilon}{N+1}(J-A B).
\tag{9}
\]

At the empty configuration J=n sum chi=0, so (9) is valid there as well.
Let delta a(t)=partial_h E_h A(t)|_0. Initially
delta a(0)=sigma_2[1-(1-rho)^n]. The exact derivative is the following
finite-size expression. For n>=3, let K~Binomial(n-1,rho). Then

\[
\delta\dot a(0)=\epsilon n(1-\rho)\sigma_2
E\left[
\frac{1_{K>0}}{K+1}
\left\{\frac{z\theta K}{n-1}-6-
\frac{\theta^2 z(z-1)(K-1)}{6(n-1)(n-2)}\right\}
\right].
\tag{10}
\]

Derivation: fix an empty birth site x and condition on K=k occupied other
sites, of which ell neighbor x. For k>0, differentiating only the iid
content law in (1) gives

\[
\partial_h E_h\!\left[\sum_a\chi_a u_{x,a}\mid k,\ell\right]_0
=\ell\theta\sigma_2,
\]
\[
\partial_h E_h\!\left[A\sum_a u_{x,a}\mid k,\ell\right]_0
=\sigma_2\left(6+\frac{\theta^2\ell(\ell-1)}{6k}\right).
\]

The second term retains correlations of the old average with the birth
hazard. Conditional ell is hypergeometric, with mean zk/(n-1) and second
factorial moment z(z-1)k(k-1)/[(n-1)(n-2)]. Substitution into (9), multiplied
by the n possible empty birth sites, proves (10). The k=0 term is zero.

For direct evaluation when rho>0, put
U=[1-(1-rho)^n]/(n rho) and p=(1-rho)^(n-1). The bracketed expectation in
(10) equals

\[
\frac{z\theta}{n-1}(1-U)-6(U-p)
-\frac{\theta^2z(z-1)}{6(n-1)(n-2)}(1+p-2U).
\tag{11}
\]

For n=1 the derivative delta dot a is zero. For n=2, z is zero or one and
the result is epsilon rho(1-rho)sigma_2(z theta-6). Formula (10) is zero
at rho=0 and rho=1 by its finite-sum interpretation, without dividing by rho.

One can instead condition on a record being present. Here
P(N(t)>0)=1-(1-rho)^n exp(-6 epsilon n t) exactly, because the empty state
has that exit rate and is never revisited. For rho>0 the conditional
initial response is sigma_2, and its time derivative is

\[
\left.\partial_t\partial_h E_h[A(t)\mid N(t)>0]\right|_{0,0}
=\frac{\delta\dot a(0)-6\epsilon n(1-\rho)^n\sigma_2}
{1-(1-\rho)^n}.
\tag{12}
\]

Neither (10) nor (12) is in general equal to (7).

**A sign-changing normalization falsifier.** Take the four-cycle, rho=3/4,
chi=(1,1,1,-1,-1,-1), and W_(ab)=1+(4/5)chi_a chi_b. This is a positive
symmetric row-six matrix, theta=24/5, sigma_2=1. Exact enumeration gives

\[
\delta\dot R(0)=\frac25\epsilon,\qquad
\delta\dot a(0)=-\frac{27}{128}\epsilon,\qquad
\partial_t\partial_h E_h[A\mid N>0]|_{0,0}
=-\frac{26}{85}\epsilon.
\tag{13}
\]

The two meanings of content per record can even have opposite instantaneous
signs on the same supplied model. Omitting the theta^2 term in (10) also
changes this example: it incorrectly adds 9 epsilon/20.

## Edge cases, scope, and reproduction

At rho=0 the initial law has no perturbation at all: every actual linear
response above is zero, while R(0) and the conditional ratio are undefined.
Equation (7)'s rho-down-to-zero limit is nonuniform and cannot be substituted
at rho=0. Uniform first births nevertheless give a second-moment derivative
6 epsilon n sigma_2. At rho=1 there are no transitions. At epsilon=0 all
global counts, M, M^2 and A are conserved. The zero chi function is trivial
and has no nonzero response to normalize. For theta=0, the per-site initial
response vanishes while (7) still has dilution. In the stronger W=1 control,
LM=0 at every configuration; W chi=0 alone does not imply that identity for
products over multiple neighbors. For instance, chi=(2,-1,-1,0,0,0),
psi=(0,1,-1,0,0,0) and W=1+(1/2)psi psi^T have W chi=0, yet the triangle
state (vacant,1,1) has J=-1/2. This counterexample is checked exactly.

Independence is an initial condition, not a proved invariant family. These
instantaneous derivatives cannot be promoted to closed finite-density ODEs,
exponential amplification laws, a sustained instability, or a physical field
identification. General W need not have a content-permutation symmetry that
keeps the unperturbed ensemble centered at later times. Further-time response
requires control of the evolved correlations. There is no finite-time,
birth-event, equilibrium, or growing-volume ensemble substitution here.

Run `python3 check.py` from this directory. The independent standard-library
runner explicitly enumerates all states and actual birth/hop transitions on
a singleton, edge, triangle and four-cycle. It uses exact rational arithmetic
and no primary runner imports. Positive, negative and zero eigenvalues,
nonzero sigma_3, rho=0 and rho=1, the jump-square term, and the three ratio
normalizations are checked. Results and the complete execution log are in
`RESULTS.json` and `RUN.log`. `SEAL.json` pins this report, the code/results,
and the exact pre-campaign sources below. The executed suite checks 7,945
state cases and 25 initial laws, plus the small construction just given;
all exact checks pass.

## Source identities and independence boundary

Only already-reviewed model sources at commit
`689941783bea870e08458e079ddb208257d0083d` were consulted:

* `docs/MOBILE_RECORDS_RARE_FORMATION_EVENT_LAW_AND_SIX_SITE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-20.md`:
  SHA-256 `8cc06519d7f3acc088b1e450c151f0870ab21d2987ef2b0224d40ba6a5e7e4e2`.
* `docs/MOBILE_RECORDS_FINITE_RATE_CONTROL_AND_SPATIAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-20.md`:
  SHA-256 `423eba32f704e510331bfbb6dba78ea0a35db129854547b155fd76f27248d917`.
* `docs/ai_methodology/SCIENCE_WORKFLOW.md`:
  SHA-256 `d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4`.
* Planning instructions `origin/ai/execution:AGENTS.md` at
  `068e916ca37b004757ad3a3c082857a91dc37215`:
  SHA-256 `b72ba953ee650b464b7987c71de3415de590be5aa42451240525a2b2585312e7`.

These identities were unchanged from the earlier bounded checks. No new
campaign12h author calculation, external theorem, simulator, or draft was
read. No source outside this assigned independent directory was modified.
