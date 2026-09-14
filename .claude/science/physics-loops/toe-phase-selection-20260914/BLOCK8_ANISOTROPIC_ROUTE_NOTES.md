# Next leverage: actual finite-clock Hamiltonian and the time limit

Personal scratch derivation, 2026-09-14. This records the next candidate
route while block7 is still under author review. No phase conclusion is
asserted here.

## A scaling distinction that must be checked

For fixed N>=3, the temporal Villain kernel on clock angles is the sampled
circle heat kernel phi_beta_t. The ratio of an elementary nonzero jump to
the zero-angle weight is, for large beta_t,

  phi_beta_t(2pi/N)/phi_beta_t(0)
       ~exp[-2pi^2 beta_t/N^2].

To obtain a finite nearest-clock-jump rate h in a time step epsilon, choose

  beta_t(epsilon)=N^2/(2pi^2) log[1/(epsilon h)].

After normalization the temporal kernel should approach
I+epsilon h(X+X^dagger-2I)+o(epsilon), with care for N=2, opposite jumps
and periodic images. For N>=3 the two nearest jumps are distinct; at N=3
the longer image contributes at fourth rather than first order in epsilon.

For the spatial Villain factor at SMALL beta_s, its Fourier expansion is
1+2exp[-1/(2beta_s)] cos(theta)+higher modes. To obtain exp[epsilon K cos
(theta)] to first order, choose

  beta_s(epsilon)=1/[2 log(2/(epsilon K))].

Thus beta_s beta_t tends to N^2/(4pi^2) at fixed h,K, but beta_s tends to
zero. The block7 all-couplings-large proof is not uniform on this path.
The continuous-U(1) kinetic scaling beta_t proportional to 1/epsilon would
freeze fixed-N clock jumps exponentially faster than epsilon instead.
These statements need exact finite-N transfer tests and error estimates.

The resulting pure-clock Hamiltonian is expected to be, up to a scalar,

  H=h sum_links(2I-X-X^dagger)+K sum_plaquettes(1-cos theta_p)

on the physical gauge subspace. The actual repository penalty Hamiltonian
also contains configuration-dependent wrap suppression and a spatial
principal-monopole penalty. Its transfer action must be derived explicitly;
it is not identified merely by a matching clock alphabet.

## Primary literature route, not yet a proof input

Borsten--Kim, arXiv:2507.10459v2 (27 Apr 2026), section IV, studies a modified
Villain formulation with integer plaquette field m and an independent
monopole suppression. Their exact-suppression construction uses a Lagrange
multiplier enforcing dm=0 and dualizes to a U(1) model with monopoles in
N-unit charges. Their finite monopole-mass extension in equation (60) is
presented as an expected phase picture, not a proved uniform covariance
estimate. This is a useful construction to compare with the actual penalty
Hamiltonian, not authority for its phase.

Primary PDF: https://arxiv.org/pdf/2507.10459v2
Local PDF SHA256: 3a25df2f0ed23835c2f9726cce4cc219ec2eb194dadbbc4a24805b4a964a9326.
Read sections I, parts of II, and IV in full; sections II remainder and III
have not been fully read. The direct predecessor is Nguyen--Sulejmanpasic--
Unsal, arXiv:2401.04800, PRL134,141902(2025), not yet read in this block.

Next terminal obligations: derive the exact finite-time kernel and its
operator-norm generator limit; identify the repository's wrap and monopole
terms without changing its law; then seek a uniform actual-state estimate
for the resulting anisotropic family. A failed estimate on this path would
be a method limitation, not an axiom-update certificate.

## Periodized Gaussian kernel for the actual wrap penalty: new proof route

Take a finite spatial link-coordinate state a in (Z/NZ)^E and let
b(a)=principal(Fa mod N) in the face representatives. For N=3 these are
{-1,0,1}; use odd N if reflection-covariant principal representatives matter.
Let D F=0 and Q(a)=D b(a)/N. The target Hamiltonian has a link jump k=+/-e_l,
with b'=b(a+k), mismatch m=(b'-b-Fk)/N and rate t exp[-mu||m||^2].
Its diagonal is 2t per link, plus K sum_p[1-cos(2pi b_p/N)] and
lambda||Q||^2. For N=3 the spatial cosine is (3K/2)sum b_p^2.

A candidate EXACT temporal kernel, normalized before the monopole penalty,
is

 K_(q,mu)(a',a)=Theta(q)^(-|E|)
   sum_(k in Z^E : k=a'-a mod N)
      q^(||k||^2) exp[-mu/N^2 ||b(a')-b(a)-F k||^2],
 Theta(q)=sum_(j in Z) q^(j^2), q=epsilon t.

At mu=0 this is the normalized sampled Villain heat kernel on every link.
At small epsilon, k=0 supplies the diagonal, k=+/-e_l supplies exactly the
specified hopping, and all other k have norm squared at least two (apart
from coincident N=2 nearest jumps, which are counted with multiplicity).
Theta(q)^(-|E|)=1-2|E|q+O(q^2), giving the fixed diagonal 2t|E|. Do NOT
renormalize each penalized row: that would replace the diagonal by the
configuration-dependent escape rate and change the intended Hamiltonian.

There is a promising all-volume positivity proof. The function of real
increments (x,y),

 f(x,y)=exp[-c||x||^2-(mu/N^2)||y-Fx||^2], c=-log q>0,

is a positive-definite Gaussian kernel (strict for mu>0). Periodize only x
by N Z^E, leaving y real. Its Fourier representation has a positive spectral
measure on the discrete x frequencies and continuous y frequencies, so it
is positive definite on (R/NZ)^E x R^P. Restrict to the nonlinear finite
embedding a -> (a,b(a)). The restricted kernel is exactly K above, up to its
positive scalar normalization, hence positive semidefinite. For mu>0,
strict positivity should follow from continuity in y frequency and the
complete x characters; mu=0 is the strictly positive circle-heat case.
This avoids assuming that an arbitrary state-dependent hopping kernel is
reflection positive. Write the Fourier proof and test it before use.

The spatial potential V=K sum(1-cos)+lambda||Q||^2 can be inserted as
D_epsilon=exp[-epsilon V/2], giving
T_epsilon=D_epsilon K_(epsilon t,mu) D_epsilon.
If the kernel proof is sound, T_epsilon is positive and self-adjoint at every
finite volume and admitted epsilon. Its first-order generator is precisely
the target H, up to an explicitly controlled finite-volume O(epsilon) error.
Gauge transformations permute a, leave b fixed, and preserve the summed
integer-lift differences; the physical gauge subspace should therefore be
invariant. Global holonomies and realizable flux restrictions must remain.

This is a candidate matched transfer/continuous-time construction. It does
not prove the actual H is massless. The terminal phase obligation is a
uniform actual-state estimate for this anisotropic, principal-flux kernel.
The all-couplings-large block7 theorem is not uniform on this time-limit
path. A failure of that particular bound is not an axiom-update certificate.

## Positivity and a conservative finite-volume error derivation

For mu>0 the Gaussian quadratic form in (x,y) is strictly positive definite:
c||x||^2+(mu/N^2)||y-Fx||^2 is a sum of positive squares under an invertible
triangular change of variables. Its Fourier density is everywhere positive.
Periodizing x on N Z^E restricts the x frequencies to the dual lattice while
leaving positive densities in the real y frequencies. For a nonzero vector
of coefficients c_a on the finite principal-flux graph, at y frequency zero
some complete finite x character has nonzero sum c_a exp(2pi i n.a/N).
Continuity gives a positive-measure neighborhood with nonzero modulus, so
the restricted Gram matrix is STRICTLY positive. At mu=0 it is the strictly
positive product clock heat matrix, independent of y.

Symmetry follows by swapping endpoints and k -> -k. Every entry is positive
for finite mu. Every row sum is <=1 because the penalty is <=1 and each k
selects one endpoint a'. Thus K is a positive self-adjoint contraction; with
V>=0, D K D is also a positive self-adjoint contraction. Gauge transformations
at both endpoints leave b unchanged and reindex integer lifts of the same
modular increment. The physical subspace is invariant.

For E=number of links>=1, q<=1/8, set Theta(q)=1+s, with
s=2q+tail and tail<=2q^4/(1-q^5)<=3q^4, hence s<=3q. Write
K=p0 I+q p0 A+R, p0=(1+s)^(-E), where A is the sum of the 2E weighted
unit-hop permutations, ||A||<=2E, and R contains all other integer k.
Its nonnegative symmetric entries have row sum at most
1-p0(1+2Eq), so its norm is bounded by that number.

Taylor's bound for (1+s)^(-E) gives
|p0-1+2Eq|<=(9/2)E(E+1)q^2+3E q^4.
Also q|p0-1| ||A||<=6E^2 q^2 and
||R||<=E*tail+2Eq(1-p0)<=3E q^4+6E^2q^2.
Consequently the deliberately loose bound

 ||K-I-q(A-2E I)||<=24 E^2 q^2

holds, uniformly in the nonnegative mu and in F (the penalty was only bounded
by one). With q=epsilon t, H_E=t(2E I-A)>=0 and ||H_E||<=4tE. The scalar
spectral bound for exp(-epsilon H_E) gives

 ||K-exp(-epsilon H_E)||<=32 E^2 t^2 epsilon^2.

For V>=0 use two contraction Lie-product estimates to obtain

 ||exp(-epsilon V/2)exp(-epsilon H_E)exp(-epsilon V/2)
          -exp[-epsilon(H_E+V)]||
    <=(epsilon^2/2)||[H_E,V]||.

This is a conservative SECOND-order estimate; it does not claim the sharper
Strang third-order constant. Combining the bounds gives
||T_epsilon-exp(-epsilon H)||<=epsilon^2 C,
C=32E^2t^2+||[H_E,V]||/2. Telescoping m contractions at epsilon=T/m yields
||T_epsilon^m-exp(-T H)||<=T epsilon C.
These are finite-volume estimates; E^2 is explicit. No volume-uniform phase
or thermodynamic exchange follows from them. The Gaussian representation and
all numerical constants are pending the forthcoming finite checks and final
adversarial reread.

The full periodization includes integer temporal lifts beyond the principal
clock difference. A classical action retaining only a principal temporal
representative is a different finite-time measure, even if its first-order
Hamiltonian agrees. This distinction must be retained in the literature
comparison; it may be precisely what makes finite-time positivity transparent.
