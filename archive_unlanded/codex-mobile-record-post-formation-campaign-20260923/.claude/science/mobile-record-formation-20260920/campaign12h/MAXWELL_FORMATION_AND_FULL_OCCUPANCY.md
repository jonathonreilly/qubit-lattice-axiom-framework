# Formation, empty start and a transverse sector that survives full occupancy

Status: primary construction and theorem application; independent check
pending. The exchange model is the supplied fifteen-state construction in
`IMMUTABLE_TRANSVERSE_MAXWELL_CONSTRUCTION.md`. Formation in this note is
uniform, at per-label microscopic rate beta/N, beta>0. It is not the
neighbor-dependent admissibility law. No clock or alphabet is axiom-selected.

## 1. Exact evolving product law

Write v0 for the initial vacancy probability and p_a(0) for the fourteen
occupied probabilities. Because every homogeneous product is exchange
invariant, adding independent vacancy-to-label births gives the exact
finite-volume law, on macroscopic Euler time,

    p0(t)=v0 exp(-14 beta t),
    p_a(t)=p_a(0)+(v0-p0(t))/14.

The product identity holds even if p_a(0)=0 for every occupied label. Every
actual exchange still only swaps unchanged labels, and every birth consumes
a vacancy. Hence finite-site capacity is respected and no occupied record
is deleted or overwritten by this process.

For orbit-isotropic initial products, let rho_A(t),rho_B(t) be the two orbit
masses. Then

    rho_A(t)=rho_A(0)+(3/7)[v0-p0(t)],
    rho_B(t)=rho_B(0)+(4/7)[v0-p0(t)].

The homogeneous vector means remain X=Y=0. The complete first-order reaction
on those vectors is identically zero, since sum_a e(a)=sum_a b(a)=0. Their
time-dependent curl system is

    X_t=(gamma rho_A(t)/3) curl Y,
    Y_t=-gamma rho_B(t) curl X.

Its instantaneous transverse speed is
c(t)=|gamma| sqrt(rho_A(t)rho_B(t)/3). For gamma!=0 and both limiting orbit
masses positive, this approaches a nonzero constant as vacancies disappear.
This differs from the vacancy-dependent acoustic density-wave speed in the
seven-state construction. Atomic exchanges of occupied labels remain active
at full occupancy; their use is an explicit assumption of both models.

## 2. Full-occupancy stationary theorem is a separate finite alphabet

At exactly p0=0 the full-support fifteen-state theorem cannot be cited with
its unchanged entropy coordinates. Instead restrict the same generator to
the invariant fourteen-state occupied alphabet. Uniform births then do
nothing. With rho_A>0,rho_B>0,rho_A+rho_B=1, every remaining label has positive
probability. Product balance, fixed finite range, the positive swap floor,
canonical sector connectivity and the entropy-current identity all survive.

The previously reconstructed finite-alphabet Euler and stationary
fluctuation proofs therefore apply with thirteen independent probabilities.
The linear spectrum for K!=0 and gamma!=0 is

    lambda^9 (lambda^2-c^2 |K|^2)^2,
    c^2=gamma^2 rho_A rho_B/3.

There are four propagating and nine static directions; the missing direction
is the fixed total occupancy. This is a theorem for the restricted model,
not an interchange of a boundary-density limit with the original theorem.
It proves no uniform estimate as a fifteen-state reference approaches p0=0.

## 3. Formation noise is necessary

The finite-alphabet nonstationary fluctuation proof already reconstructed
for uniform births uses the exact product law, a physical backward-energy
estimate, fixed finite canonical blocks and a martingale central limit.
Its argument does not depend on there being exactly six occupied labels.
For fourteen occupied species on any fixed interior interval it gives

    dY_K=[-i A(K,p(t))-beta 1 1^T]Y_K dt
             +sqrt(beta p0(t)) dW_K,

where Y_K now has fourteen species components. Covariances obey the usual
equal-mode rule with complex conjugation and opposite-mode rule without it.
The zero mode is real. Exchange noise vanishes at this scaling; birth noise
survives. This application requires the finite-alphabet hypotheses checked
above and a separate review; no native interacting-birth theorem is imported.

In the X,Y coordinates the birth covariances are

    Q_X=2 beta p0 I,       Q_Y=8 beta p0 I,       Q_XY=0.

Their deterministic drifts are the displayed curl system. The equal-time
covariances are rho_A/3 and rho_B, whose derivatives are precisely Q_X,Q_Y.
The two vector sectors are uncorrelated with the remaining field coordinates
under the orbit-isotropic products. Those other fields are retained in the
full theorem, even when only the vector marginal is displayed.

## 4. Equal per-label probabilities give an explicit phase

Suppose initially every occupied label has probability rho0/14, including
rho0=0 as the empty-start case below. Set v0=1-rho0. Then

    rho(t)=1-v0 exp(-14 beta t),
    rho_A=3rho/7,       rho_B=4rho/7.

Use U=2X and V=Y. Their covariances agree and their drift has a single
time-dependent coefficient:

    U_t=c_signed(t) curl V,       V_t=-c_signed(t) curl U,
    c_signed(t)=2 gamma rho(t)/7,
    Q_U=Q_V=8 beta p0(t) I,       Cov(U)=Cov(V)=4rho(t)/7 I.

For gamma>0 the phase accumulated by a fixed Fourier mode between s and t is

    theta_K(t,s)=(2 gamma |K|/7)
        [(t-s)-v0(exp(-14 beta s)-exp(-14 beta t))/(14 beta)].

The drift matrices at different times commute in this equal-per-label family.
For other initial orbit proportions their ratio generally varies, so a
time-ordered propagator is required; substituting an integrated scalar speed
is not justified for that more general family.

Let C_K w=K cross w, P_L=K K^T/|K|^2 and P_T=I-P_L, K!=0. The finite-time
Gaussian limit therefore has, for t>=s,

    E[U_K(t) U_K(s)^*]=(4rho(s)/7)[P_L+cos(theta_K) P_T],
    E[V_K(t) V_K(s)^*]=(4rho(s)/7)[P_L+cos(theta_K) P_T],
    E[U_K(t) V_K(s)^*]=i(4rho(s)/7) sin(theta_K) C_K/|K|.

The cross covariance follows from U_t=c curl V with the Fourier convention
exp(-i K.x), hence the positive i sign. The limiting process contains new
noise after time s; that noise is independent of fields at s and does not
alter these two-time formulas. Its equal-time covariance increases as new
records form. Static longitudinal drift does not mean noiseless longitudinal
fields during formation.

For gamma<0 use the signed phase in these formulas; for gamma=0 use zero
phase. There is no division by gamma. At beta=0 use the continuous constant
density phase; the main formation statement here assumes beta>0.

## 5. Empty start needs no singular entropy theorem at time zero

For rho0=0 the microscopic initial fluctuation field is identically zero.
At every fixed delta>0 its exact law is already a full-support product.
For any finite list of positive observation times choose delta smaller than
their minimum and apply the interior-interval fluctuation theorem from delta
onward. The product CLT at delta and subsequent birth martingales give a
Gaussian vector with the covariances in Section 4. These are independent of
which such delta was chosen: the covariance identity
C'=B C+C B^*+Q fixes the same covariance at every later time.

The same Gaussian finite-dimensional laws are generated by the displayed
linear SDE starting from zero at t=0, since Q is continuous there and its
covariance is 4rho(t)/7. Appending deterministic time-zero observations gives
the empty-start finite-mode, finite-time limit. This reasoning makes no claim
of a uniform entropy bound down to t=0, path-space tightness, or a theorem
for the neighbor-dependent formation process.

As t grows, c(t) tends to 2|gamma|/7 and the total integrated birth noise is
finite. The accumulated phase grows without bound, so the continuum linear
wave sector persists after formation has nearly saturated. This is an
iterated statement about the continuum equations after the fixed-time
lattice limit. It does not assert undamped propagation for arbitrarily long
times on a fixed finite stochastic lattice.
