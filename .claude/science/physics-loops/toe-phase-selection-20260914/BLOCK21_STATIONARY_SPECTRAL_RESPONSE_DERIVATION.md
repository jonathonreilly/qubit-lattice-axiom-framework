# A stationary spectral response lemma for small contrast

Personal derivation, 2026-09-15, subject to independent review. This is a
conditional analytic lemma with a complete proposed operator argument.
It does not assume that its response is the covariance of the gauge model;
that identification belongs to BLOCK21_THERMODYNAMIC_MATCHING_DERIVATION.md.
Standard spectral decomposition and a convergent resolvent expansion are
used without a novelty claim for those mathematical tools.

## 1. Explicit Hilbert-space hypotheses

Let (Omega,P) carry commuting measure-preserving spatial translations
tau_x, x in Z^d, and a strongly continuous group of time translations
sigma_t commuting with them. Write U_x f=f composed with tau_x and
S_t f=f composed with sigma_t. The spatial action is ergodic. Let

 H=L2(Omega;C^n), P0 f=E f, Q0=I-P0.

Thus the joint spectral projection of all U_x at frequency0 is exactly
P0, acting componentwise. Time translations preserve P0 and Q0.

Let K be a deterministic self-adjoint convolution on ell2(Z^d;C^n), with
matrix multiplier m on the frequency torus. Suppose m is continuous away
from0, ||m(k)||<=1, and for every p!=0,

 m(a p) -> m0(p) as a decreases to0.                       (1)

Assume m0 is a matrix-valued degree-zero homogeneous function and a
projection. Set m(0)=0. This choice at a Lebesgue-null point does not
change K on deterministic ell2, but specifies its action on invariant
vectors in the environment spectral calculus.

Let A(omega) be a covariant random operator on ell2 lattice fields,

 (A F)_i(x)=sum_(j,z) a_ij(z,tau_x omega) F_j(x+z).

Suppose deterministic nonnegative t_ij(z) dominate |a_ij(z,omega)| and
have both row and column sums at most delta<1. All sums here include z.
Require their spatial tails to tend to0 uniformly in the finite indices.
This hypothesis implies absolute operator convergence of range cutoffs
and ||A||<=delta. Self-adjointness may hold in applications, but the
resolvent calculation below does not require it.

Define the bounded time-averaged operator on lattice/path fields

 B=integral_0^infinity exp(-s) S_(-s) A ds, ||B||<=delta.

The order S_(-s) A is part of the definition; multiplication by the
environment and time translation need not commute. Define the annealed
deterministic response T by its bilinear form

 (g,T h)=E (g,(I-KB)^(-1)K h),                         (2)

initially for finitely supported deterministic sources. The inverse
exists by the norm-convergent Neumann series and ||T||<=1/(1-delta).
Translation covariance makes T a deterministic convolution. Positivity
and symmetry are additional facts when(2) is a genuine Gibbs covariance.

## 2. Exact spatial fiber convention

On lattice/path fields introduce the unitary change of variables

 (V F)_x(omega)=F_x(tau_(-x)omega).

Then a direct substitution gives

 (V A V^(-1)G)_i(x)
 =sum_(j,z) a_ij(z,omega) U_z G_j(x+z).

With Fourier convention Ghat(k)=sum_x exp(-i k.x)G_x, the fiber operator
is therefore

 A(k)_ij=sum_z exp(i k.z) M_(a_ij(z)) U_z,              (3)

where M denotes multiplication. The operator-valued Schur estimate,
using unitary U_z and the deterministic t bound, gives ||A(k)||<=delta
for every k. The same estimate with factors |exp(i k.z)-1| proves

 ||A(k)-A(0)|| ->0 as k->0.                            (4)

Indeed first truncate z, where convergence is uniform, then use the row
and column tails. No mixing rate or summable environment covariance is
used in(4).

The same conjugation sends deterministic K to

 K(k)=integral_(frequency torus) m(k+theta) dE(theta),   (5)

where E is the joint spectral measure of the spatial unitaries on H.
One can justify(5) without summing a nonsummable kernel: approximate the
bounded multiplier m by its Fejer trigonometric approximants (whose
operator norms stay at most1), use the exact
identity for each polynomial, and take the direct-integral limit. The
joint product of Lebesgue measure in k and any finite spectral measure
in theta makes almost-everywhere convergence and bounded domination
valid after translation. Alternatively
use bounded smooth mass regularizations and their strong direct-integral
limits. Equation(5) specifies a measurable representative for every k.

Since V commutes with time shifts,

 B(k)=integral_0^infinity exp(-s) S_(-s) A(k) ds,
 ||B(k)-B(0)|| ->0.                                   (6)

Deterministic sources become constant environment vectors under V. Thus
the Fourier multiplier of(2) is

 That(k)=P0(I-K(k)B(k))^(-1)K(k)P0,                   (7)

identified as an n-by-n matrix on the constant subspace.

## 3. Strong low-frequency limit

For fixed p!=0 and any f in H, the matrix spectral calculus and bounded
convergence give

 K(a p)f -> [Kenv Q0+m0(p)P0]f,
 Kenv=integral m(theta)dE(theta), Kenv P0=0.           (8)

For theta!=0, continuity gives m(ap+theta)->m(theta); at theta=0 use(1).
All multipliers have norm at most1. The only exceptional frequency is0,
whose spectral projection was separated explicitly. The environment may
have singular continuous spectrum or other atoms; these do not spoil
pointwise convergence away from0. Spatial ergodicity is what makes the
invariant projection consist of constant vectors only.

Let Kp=Kenv Q0+m0(p)P0 and B0=B(0). Equations(6),(8), uniform boundedness,
and induction show convergence of every term in the resolvent series.
Its norm tail is at most delta^(N+1)/(1-delta), independently of a. Hence

 That(a p) -> P0(I-Kp B0)^(-1)Kp P0.                  (9)

This convergence is in ordinary matrix norm because the constant source
and target spaces have finite dimension n. It is a directional limit of
the full response, not just a covariance bound or a guessed tensor.

## 4. Finite effective matrix from the environment fluctuations

Solve v=(I-Kp B0)^(-1)Kp h with constant h, and write v=bar_v+tilde_v
according to P0,Q0. The fluctuation equation is

 tilde_v=Kenv Q0 B0 P0 bar_v+Kenv Q0 B0 Q0 tilde_v.

Its inverse has norm at most1/(1-delta). Eliminating tilde_v gives

 bar_v=m0(p)[h+B_eff bar_v],

 B_eff=P0 B0 P0
   +P0 B0 Q0(I-Kenv Q0 B0 Q0)^(-1)Kenv Q0 B0 P0.      (10)

This n-by-n matrix is independent of p, and ||B_eff||<=delta/(1-delta).
For delta<1/2 this bound directly guarantees invertibility in

 T0(p)=(I-m0(p)B_eff)^(-1)m0(p).                     (11)

For larger delta<1 the original Schur-complement inverse in(9) still
exists, but no larger regime is needed here. The second term in(10)
must be retained; replacing B_eff by E A discards environmental response
and also ignores the time ordering inside B0.

## 5. Four-dimensional form symmetry

In the intended application n=7: six two-form components and one four-form
component. The potential depends only on the first six coordinates, so
A and B have zero seventh row and column. Formula(10) has the same zero
row and column. The zero-frequency Hodge projection is block diagonal,
with first block R_cont(p)=d*Delta^(-1)d and last block1. The off-diagonal
blocks vanish by d squared=0.

Assume the joint state and extended potential are invariant under all
signed permutations of four coordinate axes. The lattice action includes
the orientation-dependent basepoint translations of reflected cells.
Those translations act trivially on constant environment vectors, so
B_eff's first block commutes with the usual action on Lambda^2(R^4).

For distinct oriented pairs I,J there is a coordinate axis belonging to
exactly one pair. Reflection of that coordinate has opposite eigenvalues
on I and J, and forces the corresponding off-diagonal matrix entry to0.
Permutations act transitively on the six pairs and force all diagonal
entries equal. This applies to a general matrix, without assuming it
symmetric. Therefore B_eff=b I on the first block. Equation(11) gives

 T0,first(p)=kappa R_cont(p), kappa=1/(1-b).           (12)

In this application all underlying lattice and time-shift operators
preserve real fields, so B_eff and b are real. The complex Fourier fibers
do not introduce a complex physical covariance coefficient.

The environment can be symmetrized only in a way that preserves its
spatial ergodicity and the physical extension. Randomly selecting a global
anisotropic orientation and averaging it is not a substitute: that label
is translation invariant. Instead symmetrize the potential itself over
the finite group before constructing its unique noise-factor state.

## 6. Continuum covariance and physical qualifications

For smooth compactly supported sources h_a(x)=a^(d/2)f(ax), the Fourier
sum converges after k=ap to the ordinary continuum transform. Uniform
boundedness of That and smooth-source Fourier tails justify passing(9)
inside the bilinear integral. One elementary tail bound uses repeated
finite differences of f: their ell2 norms are O(a^r), which controls the
rescaled Fourier mass outside |p|<=R uniformly as R grows. On a bounded
p region, the rescaled Fourier sums converge by Riemann sums. The point
p=0 has zero Lebesgue measure. Cell averages and orientation-basepoint
shifts have the same limit. Thus(9)-(12) identify the continuum covariance.

If T is the matched auxiliary Gibbs covariance, the finite inequalities

 K_L(I+delta K_L)^(-1)<=Cov(omega_L)<=K_L

give 1/(1+delta)<=kappa<=1 after the bulk and scaling limits. The left
inequality is the score/Cramer-Rao lower bound using the upper Hessian
K_L^(-1)+delta on its compatible range; the right is the exact positive
theta MGF domination, not a generic consequence of small contrast.

The uniform third-cumulant remainder is still needed to turn covariance
convergence into Gaussian convergence. The exact physical full-flux map,
the score/image conditional law, and any reflection-positive state match
are additional steps. This operator lemma does not by itself supply them.

## 7. Author challenges actually run

block21_environment_response_check.py constructs actual four-dimensional
cochain Bloch matrices for a two-site layered quadratic environment. A
direct Gaussian precision inversion on the compatible subspace agrees
with the response to7.22e-14. The spatial fiber convention agrees to
4.01e-11. Across three directions and six meshes the covariance approaches
the Schur-complement limit; the mean-Hessian shortcut has a persistent
matrix discrepancy. The same runner solves the general36-entry symmetry
commutant exactly and obtains dimension1.

A mixture of four rotated layered Gaussian comparisons has fourth
cumulant1.98e-5 for a selected component, despite symmetry of its averaged
law. This checks why the invariant environment sector must be retained.
It is not a counterexample to the actual Villain carrier hypotheses.
These finite challenges do not certify the infinite spectral theorem or
the nonlinear thermodynamic matching. Independent review remains pending.
