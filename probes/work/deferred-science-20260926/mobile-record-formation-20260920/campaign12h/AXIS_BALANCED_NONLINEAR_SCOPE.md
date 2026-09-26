# Nonlinear closure and the remaining cubic anisotropy

Primary consequence of `AXIS_BALANCED_CONTEXT_EXCHANGE_DERIVATION.md`,
2026-09-21. This concerns that particular supplied generator. It is neither
a restriction on all immutable-record laws nor an exclusion of a TOE.

In three dimensions the exact current laws have an invariant smooth
four-field submanifold

`q_1=q_2=q_3=rho/3`,

with arbitrary interior vector density g. The corresponding occupied
probabilities are p_(+i)=rho/6+g_i/2 and p_(-i)=rho/6-g_i/2, so the
interior condition includes |g_i|<rho/3 and 0<rho<1.

Indeed the axis-occupation currents on this submanifold are exactly
one-third of the number current, for every value of g, not just to first
order. Uniform insertion also adds to each q_i exactly one-third of its
addition to rho. Therefore the ansatz is tangent to the full nonlinear
reaction-conservation equations. Within any smooth solution family whose
uniqueness preserves that ansatz, its closed equations are

`rho_t+2alpha div[rho(1-rho) g]=6beta(1-rho)`,

`g_j,t+alpha partial_j(rho^2/3)`

` +alpha sum_i partial_i{[2(1-rho)-3delta_ij]g_i g_j}=0`.        (1)

The source is beta for each label on macroscopic time; beta=0 is the
conservative case. This algebraic invariant-submanifold calculation is not
a global smooth-existence or uniqueness theorem.

The vector-current tensor on the ansatz is

`P(g,rho)=alpha{(rho^2/3)I+2(1-rho)g g^T-3 diag(g_i^2)}`.       (2)

Its first two terms transform as an isotropic tensor. The last does not.
Take g=(z,0,0), with 0<|z|<rho/3, and a 45-degree rotation R in the xy
plane. The rotated vector is (z/sqrt(2),z/sqrt(2),0); both compositions
remain interior on the q_i=rho/3 ansatz. Directly,

`[P(Rg,rho)-R P(g,rho) R^T]_(xy)=3alpha z^2/2`,                 (3)

and the same residual occurs in the yx entry. Thus the finite-amplitude
four-field current law is cubic covariant but is not SO(3)-covariant for
alpha!=0. The anisotropy first appears at quadratic order in g. Equation
(3) is a counterexample for this model, not a statement about every possible
context feature or any eventual renormalized scaling.

This matters when interpreting the acoustic result. The isotropic
linearized equations, and a possible Euler-scale Gaussian fluctuation
limit, do not establish an isotropic interacting continuum theory. On the
fluctuation scale the retained nonlinear contribution may vanish in the
particular limit being proved; that is different from making (1) invariant
under continuous rotations at finite amplitude. No Lorentz symmetry,
quantum commutator or gravitational dynamics has been derived.

A useful next construction problem is therefore explicit: find local
immutable exchanges that preserve the checked linear sector while
controlling the quadratic tensor term in (2), or establish why a proposed
scaling makes its physical effect negligible. Any new rate must again
satisfy product stationarity, positivity and covariance; a desired continuum
tensor alone does not construct such a microscopic process.
