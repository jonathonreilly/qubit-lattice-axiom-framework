# Linear constraints and a positive transfer for the Regge tensor sector

Author conditional derivation, 2026-09-13. It depends provisionally on the exact
Block7 Hessian identity and keeps Block8's nonlinear hyperdiagonal condition.
No independent source review, axiom derivation or nonlinear quantum gravity
claim is made. The construction is a reduced quantization of a supplied
quadratic action, with a specified orientation and integer time coordinate.

## 1. Full scalar and vector constraints

At any nonzero real spatial momentum set r=|p_spatial|>0. An orthogonal
spatial frame takes p=(0,0,r,t), t=2sin(k_t/2). The component order is
(1,2,3,0): the time index 0 is the fourth component. Use the same frame on
both sides of the bilinear form. Split the symmetric H as follows:

- H_ab=TT_ab+(tau/2)delta_ab for transverse indices a,b=1,2;
- H_a3=v_a, H_a0=b_a, H_33=sigma, H_30=b_3, H_00=a.

The TT tensor is traceless in its two-dimensional plane, hence has two
independent components. Direct expansion of the Block7 F_p gives

F_TT=(r^2+t^2)tr(TT^2),
F_vector=2 sum_(a=1,2)(t v_a-r b_a)^2,
F_scalar=-(r^2+t^2)tau^2/2
         -2tau(r^2 a+t^2 sigma-2rt b_3).                       (1.1)

The displayed squares stand for the bilinear products of the opposite Fourier
fields, or their absolute squares for real Euclidean momentum. Equation (1.1)
is a full mixed-form identity, not a statement about selected diagonal entries.

The lapse equation is r^2 tau=0, so tau=0. The transverse shift equations give
t v_a-r b_a=0. The remaining scalar equation imposes
r^2 a+t^2 sigma-2rt b_3=0. The longitudinal shift and sigma equations are
then redundant. These conclusions need r>0 but no inverse of t.

Under H -> H+i(pu^T+up^T), the transverse transformations are
v_a -> v_a+i r u_a and b_a -> b_a+i t u_a. Set v_a=0; its shift then vanishes.
Use u_3 to set sigma=0, and then u_0 to set b_3=0. The scalar equation sets
a=0. The combinations in (1.1) are gauge invariant, as direct substitution
checks. Thus every source-free scalar/vector solution is gauge, for every
real frequency and its finite complex continuation at r>0. Exactly two tensor
coordinates remain. This supplies the multiplier/constraint argument missing
from a test of zero lapse/shift diagonal entries.

The four body coordinates are algebraic with constant nonzero block and vanish
in the source-free problem. The hyperdiagonal is an additional zero-action
coordinate at quadratic order, not a vertex gauge transformation. This reduced
model fixes a section for it and considers only the tensor observables.
Block8 excludes pure-hyperdiagonal nonlinear tangents in its specified family;
it does not establish nonlinear continuation of these tensor data. The chosen
linear section is not claimed to solve the nonlinear constraint.

## 2. Finite tensor coordinates and orientation

Choose a finite three-torus with odd side periods at least three and remove
spatial momentum zero. Every remaining momentum has a distinct conjugate
partner, so real cosine/sine coordinates can be chosen without a self-inverse
Nyquist-mode convention. The projector onto spatial transverse traceless tensors is

P_TT,ij,kl = (Pi_ik Pi_jl+Pi_il Pi_jk)/2-Pi_ij Pi_kl/2,
Pi_ij=delta_ij-p_i p_j/r^2.                                   (2.1)

It is an orthogonal rank-two projector. Choose an orthonormal tensor basis
in each conjugate pair, respecting the opposite-phase reality convention of
Block7. No globally smooth polarization basis is required. This gives
2(V-1) real tensor coordinates on a V-site spatial torus.

Choose the action orientation -S_R and a positive overall coefficient, fixed
here to one. The quadratic action is F_TT/8. For each orthonormal amplitude
h=2X and Parseval-normalized spatial Fourier coordinate, it becomes

I_r[X]=1/2 sum_n[(X_(n+1)-X_n)^2+r^2 X_n^2].                 (2.2)

Both the orientation and time normalization are supplied. The opposite action
orientation gives a negative tensor Gaussian and is not selected by this
calculation. Equation (2.2) defines the reduced tensor measure; it is not an
integration over the full unconstrained conformal Regge field.

## 3. Positive transfer, obtained explicitly

On L^2(R,dx) define

K_r(x,y)=(2pi)^(-1/2)
 exp[-(x-y)^2/2-r^2(x^2+y^2)/4].                            (3.1)

Products of these kernels produce precisely (2.2), with its endpoints weighted
by half the local potential. Let M be multiplication by exp(-r^2x^2/4).
Then K=M exp(partial_x^2/2)M. The heat operator is positive self-adjoint
(its Fourier multiplier is exp(-p^2/2)), so K is positive self-adjoint.
Its Gaussian kernel is Hilbert-Schmidt for r>0. The explicit spectrum below
also gives trace class. Positivity here is operator positivity, stronger than
pointwise positivity of the kernel.

Set

A=1+r^2/2=cosh E, a=sqrt(A^2-1)=sinh E,
E=2asinh(r/2)>0, z=exp(-E).                                 (3.2)

The normalized Gaussian psi_0(x)=(a/pi)^(1/4)exp(-a x^2/2)
has eigenvalue exp(-E/2). Gaussian integration of the Hermite generating
function gives

K[exp(-a y^2/2)exp(2sqrt(a)y s-s^2)](x)
 =exp(-E/2)exp(-a x^2/2)exp(2sqrt(a)x z s-z^2 s^2).           (3.3)

Indeed (A+a)^(-1)=z, A-z=a and 2az-1=-z^2. Comparing powers of s shows
that the complete Hermite basis of width a has eigenvalues

lambda_m=exp[-E(m+1/2)], m=0,1,... .                          (3.4)

Their sum is 1/[2sinh(E/2)]=1/r, equal to the integral of K(x,x).
The normalized transfer T=K/lambda_0 is a positive contraction with a simple
vacuum eigenvalue one. Its self-adjoint generator is

H_r=-log T=E N_a,
N_a=(P^2+a^2X^2)/(2a)-1/2.                                  (3.5)

It defines unitary real-parameter evolution exp(-is H_r). This reconstructs
a mathematical time evolution for the supplied reduced model; it does not
identify that parameter with a physical Record clock.

## 4. Reflection positivity and the exact covariance

For finitely many spatial modes use the tensor product of these transfers.
It is positive trace class before vacuum normalization and has the tensor
product Gaussian vacuum. Products of bounded functions of X at ordered
nonnegative integer times define vectors by inserting the appropriate powers
of T between the functions. Reflection of an ordered product reverses its
order and takes adjoints. The site-reflected expectation is the Gram pairing
of those vectors; the link-reflected expectation inserts one positive T.
Both are nonnegative. Finite linear combinations preserve this property.
Gaussian moment bounds extend it to polynomial fields. This is reflection
positivity for the reduced tensor histories, proved by the positive transfer.

Since X psi_0=psi_1/sqrt(2a), the ground-state covariance is

C_r(n)=exp(-E|n|)/(2sinh E).                                 (4.1)

Summing its geometric series gives

sum_(n in Z) C_r(n) exp(-ik_t n)
 =1/[2(cosh E-cos k_t)]
 =1/[r^2+4sin^2(k_t/2)].                                    (4.2)

Consequently the tensor covariance is 4 P_TT times (4.2), in the H=2X
normalization. The two positive spectral weights are 1/(2sinh E) for X.
This gives an actual positive reduced tensor-state construction with the same
dispersion as the algebraic Regge rank drop. It does not turn a small singular
value or an approximate old metric projection into a physical state theorem.

Within the chosen lattice and tick units,

partial E/partial k_i=sin(k_i)/sinh E,
|grad E|^2=[r^2-(1/4)sum_i p_i^4]/[r^2+r^4/4] <=1.            (4.3)

The low-momentum speed tends to one. This is a group-velocity statement;
it does not establish a microscopic causal cone or match the clock/speed of
the separate native matter model. That comparison still needs one physical
coordinate and time map.

## 5. Scope and remaining obligations

The theorem is finite-volume, quadratic, source-free and reduced. It uses odd
spatial periods, nonzero spatial modes, a chosen action orientation and a chosen
hyperdiagonal section. It proves full scalar/vector elimination and a positive
tensor transfer in that domain. It supplies neither an unconstrained conformal
measure nor a nonlinear physical graviton theory.

The strongest remaining connection is a common physical matter/source and time
map, with a conserved source obtained by varying that same matter action.
A finite physical qubit realization, a thermodynamic/continuum limit and nonlinear
constraint propagation remain separate. No axiom, primitive, G or empirical
constant is derived or amended here. This is proposed conditional-support;
same-author checks are complete and independent review remains pending.

## 6. Author verification

The exact checker passes 48 checks. It expands the entire mixed scalar/vector/
tensor form, verifies the gauge transformation that removes constrained entries,
and rejects missing scalar and vector cross terms. The transfer generating
identity is checked symbolically, then a separate Gaussian-moment recurrence
checks the first seven Hermite eigenfunctions at a rational fixture. The
Fourier covariance is checked as a rational identity for arbitrary phase.
Exact site and link Gram matrices for finite polynomial fragments are positive;
an intentionally negative transfer eigenvalue produces a negative link norm.
These finite checks challenge the analytical proof, rather than replacing its
all-mode statements. They provide no independent source review.

The first fixed checker run passed. During author cleanup, a redundant squared
trace predicate was replaced with the signed trace identity using the stated
domain 0<z<1 and r=(1-z)/sqrt(z). The formulas and claim did not change.
