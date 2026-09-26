# Preparing a finite-mode Gauss sector without changing the exchange rule

2026-09-21. Primary conditional extension; separate check pending.
This note uses the stationary finite-mode fluctuation theorem for the
supplied immutable transverse generator. It establishes a possible
preparation of its source-free vector sector, not a dynamical selection
principle, microscopic gauge constraint, or derivation of electromagnetism.
All limits below keep a fixed finite set of Fourier modes and times.

## 1. Interior stationary background and the unconditioned limit

Let the fifteen-state orbit-isotropic product have positive vacancy and
orbit masses rho_A,rho_B. Define a=rho_A/3, b=rho_B and use normalized
vector fluctuations

    E_K=X_K/sqrt(a),   B_K=Y_K/sqrt(b),
    c=gamma sqrt(a b).

For a nonzero wave vector K define C_K w=K cross w and
P_L=K K^T/|K|^2, P_T=I-P_L. The stationary finite-mode theorem supplies

    (E_K(t),B_K(t))=P_K(t)(E_K(0),B_K(0)) in the limit,

where each diagonal block of P_K is P_L+cos(c|K|t)P_T, its upper-right
block is i sin(c|K|t) C_K/|K| and its lower-left is the negative of that
block. The complex Fourier convention is exp(-i K.x). Initial E and B
have covariance I and are independent at a given nonzero mode; their real
and imaginary parts have covariance I/2. Choose one member of each pair
{K,-K}; opposite modes are conjugates, not independent observations.
For fixed nonzero integer torus frequencies and N sufficiently large,
there is no accidental self-conjugate lattice frequency.

The two longitudinal projections remain constant in time. Their initial
variances are positive under the product ensemble. Thus the product
ensemble alone does not impose K.E_K=K.B_K=0.

## 2. A bounded initial conditioning transfers the limit theorem

Choose finitely many distinct nonzero wave vectors, modulo conjugation.
Let Z_N be the real vector containing the real and imaginary parts of
K.E_K(0)/|K| and K.B_K(0)/|K| for those modes. Define

    A_(N,epsilon)={every coordinate of Z_N lies in [-epsilon,epsilon]},
    mu_(N,epsilon)=pi_N conditioned on A_(N,epsilon),

for a fixed epsilon>0. The finite-dimensional product CLT implies

    pi_N(A_(N,epsilon))->p_epsilon>0,

since the limiting Z is a nondegenerate finite Gaussian vector and the
box boundary has zero Gaussian probability. The conditional path law
with unchanged exchange dynamics has Radon-Nikodym derivative
1_A/pi_N(A) against the original stationary path law. Therefore for every
nonnegative path observable F,

    E_(mu_(N,epsilon)) F <= E_(pi_N)F/pi_N(A_(N,epsilon)). (1)

Apply (1) to the squared field-propagation remainder in the stationary
theorem. Its supremum of expectations still tends to zero at fixed epsilon.
No stationarity of the conditional law is assumed. The original theorem's
error estimate is simply transferred through its bounded initial density.

For any bounded continuous initial-field test function, the conditional
CLT follows from the unconditional joint CLT and the box boundary having
zero probability. The limit at fixed epsilon is the original Gaussian
initial vector conditioned on its longitudinal coordinates lying in that
box, propagated by P_K. It is generally not Gaussian at this intermediate
step, and no Gaussian assertion is made there.

Now take epsilon down to zero **after** N tends to infinity. In an isotropic
Gaussian vector, longitudinal and transverse projections are independent.
The conditioned longitudinal coordinates converge to zero, while every
transverse coordinate keeps its original law. Thus the iterated finite-mode,
finite-time limit is Gaussian with

    Cov(E_K(0))=Cov(B_K(0))=P_T,
    Cov(E_K(0),B_K(0))=0.                                 (2)

Its two-time vector covariances are

    E[E_K(t) E_K(s)^*]=cos(c|K|(t-s)) P_T,
    E[B_K(t) B_K(s)^*]=cos(c|K|(t-s)) P_T,
    E[E_K(t) B_K(s)^*]=i sin(c|K|(t-s)) C_K/|K|.           (3)

The longitudinal Gauss constraints now hold for the selected modes at all
observation times. The remaining species-moment fields are still present.
At an interior fifteen-state background there are eight additional static
directions after the two longitudinal directions have been removed. This
is a restriction of the vector marginal, not a deletion of those fields.

The entropy cost of the preparation is exactly
H(mu_(N,epsilon)|pi_N)=-log pi_N(A_(N,epsilon)); for fixed epsilon it stays
bounded as N grows. This fact is compatible with the smooth-profile Euler
hypothesis but does not select the preparation. The argument does not give
a quantitative error uniform as epsilon decreases. A simultaneous choice
epsilon_N->0 requires additional control; no such rate is asserted.
Conditioning all lattice Fourier modes is a different, extensive constraint
and is not covered by this finite-mode proof.

At exact full occupancy, repeat the same argument for the separately
restricted fourteen-label product with positive orbit masses. Its
thirteen-dimensional stationary theorem has seven other static directions
after removing the two longitudinal ones. No boundary-density interchange
is required.

## 3. Uniform formation supplies new longitudinal noise

Take the equal-per-label formation trajectory of
`MAXWELL_FORMATION_AND_FULL_OCCUPANCY.md`, with U=2X,V=Y. Its vector drift
has zero longitudinal part, but each sector receives independent isotropic
noise of covariance8 beta p0(t) I per unit time. Suppose a finite-mode
Gauss preparation is imposed at a fixed s where the reference is interior.
The same bounded-conditioning argument applies to the known growing-product
fluctuation limit, followed by epsilon->0. For t>=s,

    Var(K.U_K(t)/|K|)=Var(K.V_K(t)/|K|)
        =integral_s^t 8 beta p0(u) du
        =(4/7)[rho(t)-rho(s)].                            (4)

This is a positive variance when new records form. In terms of the
unscaled divergences, multiply (4) by |K|^2. Longitudinal drift being zero
therefore does not preserve a noise-free Gauss preparation during these
uniform births. Equation (4) is an explicit property of this supplied
formation rule. It does not classify other formation rules, charge sectors,
or a possible microscopic constrained model.

One constructive next question is whether a local vacancy-consuming birth
mechanism can have a transverse projected noise at the relevant scale,
while retaining immutability, capacity and a tractable local equilibrium.
The present mechanism already gives a controlled comparison: a freely
prepared source-free sector after formation versus longitudinal noise
while births continue. No additional constraint has been silently imposed
on the original product ensemble.
