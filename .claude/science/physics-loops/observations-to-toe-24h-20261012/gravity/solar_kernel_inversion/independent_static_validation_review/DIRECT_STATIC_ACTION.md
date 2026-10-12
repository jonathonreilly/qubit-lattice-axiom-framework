# Static action behind the reconstructed response family

2026-10-12. Direct derivation by this chat. The field equation is the supplied
[QUMOND construction](https://arxiv.org/abs/0911.5464v2); its variational form
is not a novelty claim. The purpose here is to make the currently proposed
finite response family and its differential condition mathematically explicit.
No fitted response has yet been accepted as empirical physics.

Let A=|grad Phi_N| and s=A^2, in consistent physical units. For the frozen
dimensionless response N(A), define the acceleration-squared primitive

    F(s)=integral_0^s N(sqrt(u)) du.

Use the static functional, with prescribed baryonic density rho,

    S_static[Phi,Phi_N;rho]
      = 1/(8 pi G) integral [-2 grad Phi . grad Phi_N + F(|grad Phi_N|^2)] d^3x
        - integral rho Phi d^3x.

For compactly supported variations (or fixed boundary variations), varying
Phi gives laplacian Phi_N=4 pi G rho. Varying Phi_N gives

    laplacian Phi = div[N(|grad Phi_N|) grad Phi_N].

The ordinary Newtonian case N=1 has F(s)=s. The source term supplies a
universal Newtonian mass-density coupling as a premise. Point masses and
thin layers require their distributional/weak interpretation; divergent
global energy constants do not alter the local compact-variation equations.
The proposed finite basis returns to N=1 at sufficiently large A, and its
low-A enhancement is bounded. Its isolated far field therefore ultimately
falls as r^-2, unlike a permanently deep-MOND asymptote. This distinction is
already part of the frozen family, not a consequence deduced from data.

## Exact primitive for one log-ramp column

For 0<L<H, d=log(H/L), the basis b(A) is one below L, log(H/A)/d between
L and H, and zero above H. Its primitive B(s)=integral_0^s b(sqrt(u))du is

    B(s) = s,                                             0<=s<=L^2,
         = [s log(H/sqrt(s))+(s-L^2)/2]/d,                 L^2<s<H^2,
         = (H^2-L^2)/(2d),                                s>=H^2.

B and B' agree at both boundaries. B'(s)=b(sqrt(s)) almost everywhere and
continuously at the knots, so the finite-knot functional has the required
first variation without new surface delta terms at a response knot.
For the20-column reconstruction,

    F(s)=s+sum_j w_j B_j(s).

This is an explicit static field model for every nonnegative fitted weight
vector, not just a curve-prediction recipe. Choosing that functional form
and matter coupling is additional theory; the observations have not uniquely
selected them over other dynamics with the same limited observables.

## What the D-family condition actually establishes

For a vector U and A=|U|>0,

    partial_U F(|U|^2)=2 N(A) U,
    Hessian_U F=2 N(A) I + 2 N'(A) U U^T/A.

The transverse eigenvalues are2N(A)>0. The longitudinal eigenvalue is
2[N(A)+A N'(A)]. On one ramp interval j, let d_j=log(A_(j+1)/A_j).
Higher-index ramps are still equal to one, lower-index ramps have vanished,
and only ramp j is changing. Thus

    N(A)+A N'(A)
      = 1+sum_(k>j) w_k + w_j log(A_(j+1)/A)/d_j - w_j/d_j.

Its infimum in the interval is the upper-edge value. Nonnegativity is
equivalent to the frozen linear inequality

    w_j/d_j <= 1+sum_(k>j) w_k.

Consequently D makes the function U -> F(|U|^2) convex, including the
continuous joins. At U=0 the low-A branch is quadratic, so no singular
exception is needed. A strict version makes the local longitudinal
Jacobian positive. Family M only guarantees positive, nonincreasing N;
it can have a negative differential radial response on a steep interval.

This result concerns one static constitutive term. It does **not** establish
positivity of a time-dependent Hamiltonian, absence of relativistic ghosts,
causal propagation, a quantum vacuum, or a covariant metric completion.
The mixed-potential static action cannot supply those conclusions by itself.
Likewise it does not identify these weights with the positive scalar
mass/noise measure in the earlier campaign theorem; that is a different
conditional model whose force kernel and state assumptions would have to
be matched explicitly.

The useful reverse-inference statement is narrower: an observed-force
compatibility problem can select or rule out members of this explicitly
supplied static family, subject to the circular-speed and source assumptions.
Testing the same member in solar dynamics probes a shared function rather
than adding an independent solar fit parameter. The ephemeris constraint is
an input when used in the combined inverse fit, so passing it there is not
an independent empirical prediction.
