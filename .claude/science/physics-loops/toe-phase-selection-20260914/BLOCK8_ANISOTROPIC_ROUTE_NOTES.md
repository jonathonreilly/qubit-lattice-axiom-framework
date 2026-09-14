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

## Exact N=3 principal-Wilson comparison and current conservation

For N=3, temporal gauge a_0=0 identifies the principal temporal plaquette
value with k_l=principal(a'_l-a_l) in {-1,0,1}. The temporal cube charge is
m_p=(b'_p-b_p-(F k)_p)/3, up to the harmless common orientation convention.
The anisotropic principal-Wilson action has temporal factor

 K_pr(q,mu)(a',a)=(1+2q)^(-E) q^(||k||^2) exp[-mu||m||^2],
 q=exp(-3 beta_t^W/2),

and spatial half factors from beta_s^W=epsilon K and
mu_s=epsilon lambda. Choose beta_t^W=(2/3)log[1/(epsilon t)], mu_t=mu.
This is the anisotropic version of the N=3 principal-monopole action (4)
in Giansiracusa--Lanners--Sulejmanpasic, arXiv:2505.00079v2, not the full
integer-plaquette Villain action of Nguyen--Sulejmanpasic--Unsal.
The former paper supplies numerical phase evidence for its isotropic model;
it does not prove a uniform phase bound along this singular anisotropic path.

The full periodized kernel splits EXACTLY as

 K_per = alpha K_pr + R,
 alpha=[(1+2q)/Theta(q)]^E,
 R=the sum over lifts with at least one |k_l|>=2.

Both K_pr and R are symmetric with nonnegative entries. Their operator norms
are bounded by 1 and 1-alpha respectively, by their row sums. Thus

 ||K_per-K_pr|| <=2(1-alpha)
                 <=2E[Theta(q)-1-2q]/Theta(q) <=6E q^4  (q<=1/8).

Consequently both transfer families have the SAME finite-volume target
Hamiltonian and semigroup limit. This estimate does not identify their
finite-step spectra or prove reflection positivity of K_pr. In particular,
positive matrix entries and a symmetric kernel alone do not imply a positive
operator. A full-link single-square numerical check finds negative eigenvalues
for K_pr at q=.638, mu=1, but its GAUGE-INVARIANT three-state restriction
is positive in that check. The nonphysical negative mode is not a counterexample
to positivity of the physical transfer; do not use it as one.

The lift representation is local in spacetime. With b_j principal spatial
flux, Q_j=D b_j/3 and temporal integer m_j=(b_(j+1)-b_j-F k_j)/3,

 D m_j = Q_(j+1)-Q_j

holds identically. This is the exact integer continuity equation for the
principal defects, including finite penalties. The action is a sum of
[-log q]||k_j||^2, mu||m_j||^2 and epsilon V(b_j), with the global clock
realizability and holonomy conditions retained. This is a local auxiliary
summation representation of a supplied Hamiltonian, not a new axiom.

For the cubic N=3 target a single original-link move changes at most four
plaquettes and at most four cube charges. Since each charge is an integer
in {-2,-1,0,1,2}, |Delta V|<=6K+16lambda. Hence
||[H_E,V]||<=2tE(6K+16lambda) by the symmetric absolute row bound, and one
may take C<=32E^2t^2+tE(6K+16lambda) in the preceding finite-volume estimate.
This is conservative; it is not a volume-uniform local-observable estimate.

## New local Poisson coupling: extensive one-step error

The previous E^2 estimate can be improved for the actual cubic N=3 model.
Let J be the number of unordered pairs of distinct original links sharing a
spatial plaquette. A cubic link meets at most 12 other links this way, so
J<=6E (assume a standard cubical box or torus without degenerate short-cell
identifications). Weighted elementary jump operators A_(l,+/-) have entries
exp[-mu||m||^2] times their clock shifts, and A=sum_l,s A_(l,s).

The exact matrix exp[-epsilon H_E], H_E=t(2E I-A), has the following
Poisson representation. Each original link has independent +/- Poisson
clocks of rate t. Follow the time-ordered jump history in [0,epsilon], and
multiply exp[-mu||m_event||^2] at each event. The resulting subprobability
transition matrix is exactly the exponential, as follows by its Dyson
series. Every history weight is in [0,1]. The event law is independent of the
starting configuration. This representation retains the fixed 2tE diagonal.

Condition on every link having at most one event. The probability of this
condition is
alpha_P=[exp(-2q)(1+2q)]^E, q=epsilon t.
Conditional on it, each link is inactive with probability 1/(1+2q) or has
one signed event with probabilities q/(1+2q). Times are independent uniform
variables. Let K_cond denote the weighted conditional-history matrix.
Time reversal shows it is symmetric; its entries are nonnegative and its
row sums are <=1. The unconditioned remainder R_P has row sums <=1-alpha_P.
Therefore

 ||K_cond-exp(-epsilon H_E)||<=2(1-alpha_P)<=4E q^2,

using the union bound and P[Poisson(2q)>=2]<=2q^2.

The endpoint law of the conditional process is exactly the unpenalized
principal-clock step. If no two active links share a plaquette, all changed
principal-face supports are disjoint. Their mismatch vectors have disjoint
support, each elementary weight is unchanged by the other jumps, and
exp[-mu||m_total||^2] equals the product of elementary weights. Hence K_pr
and K_cond agree on these histories. On a bad history their two weights both
lie in [0,1], so the absolute difference is <=1. The bad-history probability
is at most

 J [2q/(1+2q)]^2 <=4J q^2.

This is an absolute ROW-SUM bound on the difference kernel, uniformly in its
initial configuration. Both kernels are symmetric, so it also bounds the
operator norm. The full-integer-lift correction proved above is <=6E q^4.
Consequently

 ||K_per-exp(-epsilon H_E)||
     <=4(E+J)q^2+6E q^4 <=29E q^2,   q<=1/8.

Combining with the symmetric spatial half-factor estimate gives

 ||T_epsilon-exp(-epsilon H)||<=epsilon^2 C_ext,
 C_ext=29Et^2+||[H_E,V]||/2
      <=E[29t^2+t(6K+16lambda)].

At epsilon=tau/m, telescoping contractions yields
||T_epsilon^m-exp(-tau H)||<=tau epsilon C_ext.
This estimate is extensive, not a thermodynamic local-state or phase bound:
its right side still grows with E. It does, however, avoid charging every
pair of spatially separated elementary events as an error. The proof is
uniform in finite mu>=0 and depends on locality through J.

A related fixed-volume expansion identifies the FIRST generator correction
as local. Let A_l=A_(l,+)+A_(l,-) and let B_lr be the sum of four simultaneous
signed lifts on distinct links l,r, with the total principal mismatch weight.
Then

 log K_per=q(A-2E I)+q^2 C_K+O(q^3),
 C_K=sum_l[2I-A_l^2/2]
       +sum_(l<r sharing a face)[B_lr-(A_l A_r+A_r A_l)/2].

The pair terms vanish identically for links without a common plaquette.
The single-link term has norm <=4, the pair term <=8, hence
||C_K||<=4E+8J<=52E. The symmetric potential insertion has no order-epsilon^2
commutator term in its logarithm, so at fixed volume

 -epsilon^(-1)log T_epsilon = H-epsilon t^2 C_K+O(epsilon^2).

This coefficient locality is not an all-orders logarithm-locality theorem.
Its signs and normalization will be checked independently in the cube matrix.

## Exact physical principal-kernel counterexample, with narrow scope

A three-square spatial strip has 10 links and 3 independent principal fluxes.
With free spatial boundary its gauge-invariant Hilbert space is 27-dimensional.
Use the face-edge incidence with columns e1,-e1+e2,-e2+e3,-e3,
+e1,-e1,+e2,-e2,+e3,-e3. At q=9/10 and exp(-mu)=1/2, define

 w(b1,b2,b3)=g(b2) A(b1,b3),
 g=(-1,0,1)->(1,-2,1),
 A=[[0,1,-1],[-1,0,1],[1,-1,0]],

where rows/columns use principal flux order -1,0,1. Its squared norm is 36.
The exact quadratic form of the PHYSICAL K_pr is

 w^T K_pr w = -901886967/55267035185152 <0.

Two author implementations agree by exact rational arithmetic: direct
enumeration of all 3^10 principal link lifts, and an independent Laurent
polynomial convolution

 g_q(z1)^3 g_q(z2)^2 g_q(z3)^3 g_q(z2/z1)g_q(z3/z2),
 g_q(z)=1+q(z+z^-1).

For r=exp(-mu)=1/2, the unnormalized quadratic form is
(q-1)/64 times

 13659q^9-7097q^8-56738q^7+126672q^6-124012q^5+54056q^4
 +9504q^3-24800q^2+12352q-2304,

and the normalization is (1+2q)^10. This polynomial can be checked directly
from the displayed finite generating function, without accepting a floating
point eigenvalue. At r=1 the same calculation gives the positive expression
36(1-q)^9(1+2q), an unpenalized normalization check.

Thus a one-step positive-operator claim for ALL principal temporal kernels
with arbitrary finite positive parameters is false, already in a physical
gauge sector of a free strip. Spatial half factors are positive invertible
congruences and cannot remove the negative direction. This is NOT a statement
about the periodic 4D simulated parameters, absence of a photon phase, or the
continuous-time Hamiltonian. Nor does it exclude two-step transfer positivity:
a symmetric transfer always has positive square. The full periodized Gaussian
completion remains positive for every admitted q and has the same target H.

An exploratory full cube calculation also found small negative physical
principal-kernel eigenvalues at q=.9, mu=1 and mu=10, while q=.638,mu=1 was
positive. Those floating-point results motivated the simpler exact strip
certificate; only the latter is used as the decisive counterexample.

## Gauge projection in the spacetime identification

K commutes with simultaneous spatial gauge transformations; it is not an
independently gauge-invariant kernel at its two endpoints before temporal
links are summed. Let P_G be the finite group average over spatial gauge
transformations. The physical transfer is the restriction of K (and D K D)
to im P_G, equivalently P_G T P_G there. For a periodic Euclidean time
partition function the correct trace is Tr(P_G T^M), with the temporal
holonomy/gauge projection retained; Tr(T^M) on all link coordinates alone is
not the physical gauge partition function. Gauge-invariant boundary vectors
likewise supply the physical free-cylinder amplitudes. The exact strip
counterexample is already computed after this gauge reduction.
