# Independent two-vacancy clock and coherent-completion reconstruction

For the specified even cycle, every adjacent two-hole start has mean
(K-1)/(2 beta) at every d>0. The uniform mixture has a strictly larger mean,
diverging as r_K/[(K-1)(K-2)d] at small d and as
d(K-2)(K-3)/(48 kappa^2) at large d, where r_K=2 floor(K/4)-1. These are
fixed-K limits. At d=0 there are r_K contact-dark states, and the adjacent
mean is different: (binomial(K,2)-r_K)/(beta K). Thus mean completion time
is discontinuous at zero monitoring even for an initially bright contact.

For arbitrary nonzero complex hopping and a real configuration-diagonal
potential, no contact-free invariant subspace exists with three or more
holes. With two holes a necessary flux condition is
(-1)^K exp(2i Phi)=1. It is not sufficient in general. One monitored site
eliminates every two-hole invariant contact-free subspace, including the
exceptional fluxes. Consequently the specified finite pair-birth process
completes from all even-hole initial states under that one-site monitoring.

All-size arguments are given below. Finite exact ranks corroborate those
arguments; they are not their substitute. No new author clock/completion
source, script, result or seal content has been read before this seal.

## 1. Conventions and required loss hypothesis

The h-hole basis is the set of unordered h-subsets c of a cycle of length
K>=4. Hopping a hole from x to x+1 has matrix element t_x; its reverse has
the conjugate element. No fermionic boundary sign is imported. A real
potential V(c) is diagonal in this basis. Contact means that c contains
two neighboring holes. In Q1, h=2, K is even, t_x=kappa is real and nonzero,
V=0, and Gamma=beta P_contact, beta>0. Let D=binomial(K,2).

For Q2, the required operator statement is

    ker Gamma = span{contact-free configurations}.              (1)

The usual diagonal sum of positive vacant-edge losses satisfies it.
Positive diagonal entries on all contact basis states alone would not
imply (1): Gamma=I+sigma_x has positive diagonal entries but a nonzero
kernel. With H=sigma_x its antisymmetric kernel vector remains dark.
No conclusion here silently substitutes basiswise positivity for (1).

Only the specified Hamiltonian, pair births and stated Hermitian occupation
monitoring are included in completion claims. Arbitrary additional
N,T-preserving dissipators are excluded, consistently with the corrected
prior count theorem and the sealed feedback-jump counterexample.

## 2. Mean operator, sum rule and strict ensemble distinction

In the two-hole sector the trace-decreasing no-formation generator is

    A_d(rho)=-i[H,rho]+d sum_x D_(n_x)(rho)-(1/2){Gamma,rho},
    D_n(rho)=n rho n-(1/2){n,rho}.

Replacing the occupied projector n_x by the hole projector p_x=I-n_x
does not change its dissipator. For d>0 the already checked monitored
completion criterion applies. The positive mean operator is

    M_d=integral_0^infinity exp(t A_d*)I dt,
    -A_d* M_d=I,                  E_rho tau=Tr(M_d rho).          (2)

It is finite and unique. In the configuration basis its exact linear
equation is

    i[H,M]_(c,e)
      -{d[2-|c intersection e|]+(beta/2)(a_c+a_e)} M_(c,e)
      =-delta_(c,e),                                         (3)

where a_c is one on adjacent pairs and zero otherwise. This gives an
explicit finite mean calculation at every K,d,kappa,beta without assuming
a closed population equation.

Taking the ordinary matrix trace of (2), using A_d I=-Gamma, gives

    Tr(Gamma M_d)=D.                                          (4)

Translation covariance and uniqueness make all K contact diagonal entries
equal. Thus each adjacent basis start, and the mixture of them, has

    tau_adj=(K-1)/(2 beta).                                   (5)

This does not state that every coherent superposition of adjacent pairs
has the same mean: its off-diagonal matrix elements can matter.

For the maximally mixed two-hole state,

    tau_mix=Tr M_d/D.

The Hilbert-Schmidt inner product of (2) with M_d yields the exact sum rule

    Tr M_d=Tr(Gamma M_d^2)
             +(d/2) sum_x ||[n_x,M_d]||_HS^2.                 (6)

Weighted Cauchy-Schwarz and (4) imply tau_mix>=tau_adj. The inequality is
strict. Otherwise all occupation commutators would vanish, making M_d
diagonal; its off-diagonal Poisson equations then force it constant along
the connected hopping graph, which cannot solve the diagonal equation at
a contact-free configuration. Thus the uniform spatial mixture and the
contact initial ensemble are not interchangeable.

## 3. The complete d=0 dark space for Q1

Let R translate both holes by one site. H and P_contact commute with R,
so their maximal common loss-free invariant space decomposes into
translation eigenspaces. Consider a nonzero contact-free H eigenvector and
let a>=2 be the smallest cyclic hole separation carrying nonzero amplitude.
The eigen-equation at the zero-amplitude pair {x+1,x+a}, whose separation
is a-1, gives

    psi({x+1,x+a+1})=-psi({x,x+a}).                            (7)

Only the two indicated outward predecessors can have nonzero amplitudes.
Thus a translation eigenvector in the dark space must have eigenvalue -1.
Conversely H annihilates every two-hole vector of translation eigenvalue
-1: its two pairs of allowed predecessor amplitudes cancel. The contact
orbit removes one dimension from this zero-energy translation sector.

An explicit orthonormal dark basis has one vector for each separation
a=2,...,K/2-1,

    u_a=K^(-1/2) sum_(x=0)^(K-1) (-1)^x |{x,x+a}>.

When K/2 is even there is also the opposite-pair vector, summing x over
0,...,K/2-1 with normalization (K/2)^(-1/2). When K/2 is odd that orbit
has odd length and admits no translation eigenvalue -1. Therefore

    r_K=dim dark=K/2-2+1_(4 divides K)=2 floor(K/4)-1.           (8)

Let P_D be its orthogonal projector. Every state with
Tr(P_D rho)>0 has a nonzero asymptotic survival probability at d=0 and an
infinite unconditional mean. On the orthogonal bright corner the
non-Hermitian no-event Hamiltonian is strictly stable. Its mean operator
M_0^B exists and satisfies the restricted Poisson equation with source
I-P_D. The trace argument and translation symmetry now give

    tau_adj(d=0)=(D-r_K)/(beta K).                             (9)

Every contact basis vector is bright. Equations (5) and (9) differ by
r_K/(beta K), despite both being finite. The tempting inference that a
bright initial mean must be continuous at d=0 is false: rare monitoring
excursions into dark states can have order-1 total contribution because
their residence time is order 1/d. Limits at kappa=0 are also outside the
nonzero-hopping statements.

## 4. Fixed-K small-monitoring expansion

All vectors in the dark space transform by the same translation phase.
Consequently P_D p_x P_D is independent of x; since sum_x p_x=2I,

    P_D p_x P_D=(2/K)P_D.

Compressing the unit-strength monitoring generator to dark density matrices
therefore gives

    P_D [sum_x D_(p_x)(rho_D)] P_D
       =(4/K-2)rho_D=-a_K rho_D,
    a_K=2(K-2)/K.                                             (10)

At d=0 the entire dark matrix block has zero generator. The complementary
operator block is invertible: its bright and bright/dark coherences decay
under the stable no-event Hamiltonian. Its zero spectral projection is
exactly rho->P_D rho P_D. A finite-dimensional Schur complement of
A_0+d sum D_(p_x), using (10), yields the operator-norm expansion

    M_d=P_D/(a_K d)+O(1),                 d->0+, fixed K.       (11)

The eliminated complementary block contributes only bounded terms; the
leading dark Schur block is -a_K d times the identity on dark matrices,
with an O(d^2) correction. No large-volume uniformity is implicit here.
In particular

    tau_mix = r_K/[(K-1)(K-2)d]+O(1),
    E_(rho_D) tau = K/[2(K-2)d]+O(1)                           (12)

for every normalized initially dark density rho_D. The leading coefficients
are independent of fixed positive beta and fixed nonzero kappa. Other
initial densities have coefficient Tr(P_D rho)/a_K.

## 5. Fixed-K strong-monitoring expansion

Off-diagonal entries between hopping neighbors decay at rate d, not 2d:
those two configurations share one hole. Eliminating them in (3) produces
an effective configuration jump rate 2 kappa^2/d along each hopping edge.
The contact configurations are absorbing on this slow scale because beta
is fixed and positive.

More explicitly the off-diagonal Schur inverse is O(1/d); its first term
gives the unit-edge-rate two-hole exclusion generator G multiplied by
2 kappa^2/d on the diagonal entries. Splitting the diagonal sector into
contact and noncontact entries then gives the Dirichlet hitting problem.
This finite Dirichlet matrix is invertible, so

    M_d = [d/(2 kappa^2)] diag(g(c))+O(1),                     (13)

in operator norm. The scalar g is the mean hitting time of contact under
G. With an oriented separation r=1,...,K-1,

    g(r)=(r-1)(K-1-r)/4,
    2[g(r+1)+g(r-1)-2g(r)]=-1,
    g(1)=g(K-1)=0.

The uniform unordered pair has the same separation average as a uniform
ordered pair, namely (K-1)^(-1) sum_r. This gives

    tau_mix = d(K-2)(K-3)/(48 kappa^2)+O(1),    d->infinity.    (14)

The adjacent mean remains exactly (5); it has no growing d term. The
limits (11) and (13) concern different singular mechanisms and neither
is a fixed-d thermodynamic law.

As an exact finite check, on K=4 the complete solution gives

    tau_mix = 3/(2 beta) + 1/[3(beta+d)] + 1/[6(beta+2d)]
                    + 1/(6d) + d/(24 kappa^2) + beta/(48 kappa^2). (15)

The checker verifies every entry of the full six-state operator Poisson
equation, not merely this trace formula.

## 6. All-size contact-free argument for h>=3

An H-invariant contact-free subspace exists if and only if it contains a
contact-free eigenvector, since H is finite and Hermitian. Let psi be such
an eigenvector. Initially it vanishes on every configuration with a cyclic
gap one. Inductively suppose it vanishes whenever a gap is less than a,
where a>=2. Choose consecutive holes at x and x+a and fix the other h-2
holes R. Configurations already having a smaller gap need no consideration.

Translate this pair together forward, keeping R fixed, until its right
hole is at distance a-1 from the next fixed hole. This happens before a
collision because R is nonempty. Write

    C_j=R union {x+j,x+j+a},
    Y_j=R union {x+j+1,x+j+a}.

At every intermediate Y_j the selected gap is a-1, so psi(Y_j)=0. Every
one-hop predecessor of Y_j except C_j and C_(j+1) retains a gap below a.
Its eigen-equation is therefore exactly

    t_(x+j) psi(C_j)+conjugate(t_(x+j+a)) psi(C_(j+1))=0.       (16)

The terminal C_j also has a gap a-1 to R. Since every coefficient is
nonzero, (16) propagates its zero backward to the initial configuration.
Inducting through a<=floor(K/h) eliminates every configuration. The real
diagonal potential and eigenvalue multiply zero at Y_j and never enter
the argument. Thus for every h>=3 there is no such subspace, for any
nonzero complex edge amplitudes and any real diagonal potential. When
the contact-free configuration set is empty the conclusion is immediate.

This proves finite almost-sure arrival at the next birth for each such
fixed-h no-event model with loss (1). It does not make an odd number of
holes fully fill: repeated pair births then end at one hole, where contact
loss is absent. Full-completion conclusions below require even hole count.

## 7. Two holes: flux obstruction, positive examples and potential dependence

For h=2 there is no third hole to terminate the translation in (16). At
the smallest nonzero separation a, going once around the cycle instead
gives the necessary condition

    1=(-1)^K product_x t_x/conjugate(t_x)
      =(-1)^K exp(2i Phi),
    exp(i Phi)=product_x t_x/|t_x|.                            (17)

Thus a nonexceptional flux rules out every contact-free eigenvector,
independently of the diagonal potential and magnitudes. On an even cycle
the exceptional fluxes are 0 and pi. This is a necessary condition, not a
universal sufficiency claim at those fluxes.

For equal magnitudes a site gauge puts every t_x at the same phase theta,
K theta=Phi. Set q=-exp(2i theta). At an exceptional flux q^K=1. A vector
on a fixed separation orbit with amplitudes q^x is annihilated by the
hopping Hamiltonian. It is dark whenever the diagonal potential is
constant on that orbit. The opposite-pair orbit on even K additionally
requires q^(K/2)=1. For a distance-dependent potential these vectors give
the full dark space, with dimensions

    K odd:  (K-3)/2,
    K even: K/2-2+1_[(-1)^(K/2) exp(i Phi)=1].                 (18)

To see completeness in this translation-invariant case, decompose an
invariant dark space by translation and use its minimal-separation
recurrence to force q; the listed separation orbits exhaust that sector.
For Q1, Phi=0 and V=0, recovering (8).

Arbitrary diagonal terms or unequal magnitudes can destroy these examples.
For K=4 a nonzero dark vector exists precisely when

    |t_0|=|t_2|, |t_1|=|t_3|, exp(i Phi)=1,
    V({0,2})=V({1,3}).                                       (19)

The contact boundary equations impose the first three requirements and a
nonzero ratio between the two opposite-pair amplitudes; the diagonal
eigen-equation then imposes the last. This supplies explicit failures of
flux sufficiency, including the exceptional pi flux on K=4 itself.

For an arbitrary specified exceptional-flux potential an exact necessary
and sufficient finite criterion is available without a genericity claim.
Let P be the contact-free projector, A=PHP and C=(I-P)HP. The dark space is

    intersection_(j=0)^(dim(P)-1) ker(C A^j).                  (20)

Cayley-Hamilton makes this the maximal A-invariant subspace of ker C.
No simpler universal flux-only answer for arbitrary potentials is asserted.
The controls use exact rational-complex row-space closure, not modular
rank or a tolerance-selected numerical nullspace.

For repeated even-hole formation, (16) handles every stage h>=4. If the
two-hole Hamiltonian has no dark space, by (17), (19), (20) or another
verified condition, the unmonitored finite process completes from every
initial density, with a model-dependent exponential tail and finite mean.
This follows from the absence of any positive stationary nonfull density
and the finite transient CP-semigroup argument already checked earlier.

## 8. A single monitored site suffices

Monitor one occupation n_z with any fixed positive strength. A stationary
nonfull density has zero birth support by the monotone count. Taking its
Hilbert-Schmidt inner product with the remaining Hamiltonian/monitoring
equation forces [rho,n_z]=0 and then [H,rho]=0. Its range S must therefore
be invariant under H and the hole projector p_z, and contact-free. For a
state spanning hole numbers, apply these equations to any nonzero positive
diagonal hole-number block; H, n_z and Gamma preserve each such block.

For h>=3 this is already impossible by (16). For h=2 let S_z=p_z S.
It is invariant under p_z H p_z. Within p_z's range the second hole moves
on the path obtained by removing z from the cycle; the endpoints z-1,z+1
are contact states. The compressed Hamiltonian is a Hermitian tridiagonal
matrix with every off-diagonal path entry nonzero and arbitrary real
diagonal entries. An eigenvector vanishing at an endpoint must vanish
successively along the path. Thus it has no contact-free invariant
subspace, and S_z=0.

Now S is H-invariant and every vector in it vanishes on configurations
containing z. If S were nonzero, choose an H eigenvector in it and its
smallest nonzero two-hole separation. Equation (16) without R propagates
that nonzero amplitude through every translation, since all t_x are
nonzero. In particular some translated configuration contains z, a
contradiction. Hence S=0 for two holes as well. This proof does not depend
on flux, diagonal-potential genericity, or monitoring every site.

The same finite stationary/transient argument gives full occupation with
an exponential survival bound and finite mean for all even-hole initial
densities under the stipulated multistage process. These constants depend
on the finite graph, amplitudes, losses and monitor strength. Zero monitor
strength, a missing hopping edge, and h=1 are outside this conclusion.

## 9. Physical gauge ring and the count identity

For the spin-half zero-Gauss ring, a physical bit word b determines
Q_i=b_i-b_(i-1), n_i=b_i xor b_(i-1), and T complements all bits. Fix the
representative with b_(K-1)=0 for every occupation pattern. In a T sector
tau=+/-1 use (|b>+tau|complement b>)/sqrt(2).

An ordinary hop flipping b_i for i<K-1 preserves the chosen representative
convention. Flipping b_(K-1) changes that convention and contributes tau.
Thus the exact reduced hard-core occupation/hole Hamiltonian has its
ordinary link amplitudes on all edges except the boundary edge, multiplied
there by tau. For real uniform nonzero hopping and even K this gives flux
0 in T=+ and pi in T=-. This sign is derived directly in the physical
basis, not from a Jordan-Wigner convention.

An occupation-preserving H0 commuting with T has a real scalar diagonal
potential in each T sector, even if its physical two-dimensional fiber
block includes a term proportional to T. A single occupation monitor
reduces to the same single-site monitor in both sectors. The scalar birth
loss is positive precisely on contact configurations. Therefore the
one-site completion proof applies to this T-symmetric physical ring. For
arbitrary initial density, absence of nonfull positive diagonal T-sector
blocks also eliminates possible cross-sector support by positivity.

Without monitoring, both exceptional fluxes can carry dark states. For
K>=6, equal hopping and H0=0 give dark states in both sectors; on K=4
only the T=+ sector has one. This refutes arbitrary-state completion for
those unmonitored models, but is not automatically an empty-start trap.
On K=4 every first birth from all vacancies leaves an adjacent pair of
holes, orthogonal to the entire two-hole dark space. Subsequent no-event
Hamiltonian/loss evolution cannot populate that invariant dark space.
The other T sector has no dark state. Thus that special empty preparation
can complete even though another initial density is permanently dark.
No broader empty-start reachability classification is inferred here.

Under the already checked explicit symmetries, a common real chi birth
kernel still conserves chi^((K-N)/2)T. One occupation monitor commutes with
N,T, so it preserves this identity while providing the new completion
argument. For the supplied T-even empty cat, T covariance and the two full
physical states therefore give the same terminal matrix
(I+chi^(K/2)T)/2, with one monitor instead of monitoring every site.
This uses the actual completion proof, not the count invariant alone.
Non-T-invariant H0, different chi on different edges, other added
dissipators, or a non-invariant boundary require a separate calculation.

## 10. Controls, failed inference and numerical failure record

`clock_check.py` independently assembles the two-hole hopping graph and
the complete operator equation. Its K=4 symbolic matrix satisfies every
Poisson entry exactly and yields (15), the small-d dark projector, and the
large-d diagonal hitting operator. For K=4,6,8,10,12 it solves the
dihedral-invariant operator equations at six d values from 10^-5 to 10^5,
reconstructs the complete matrix, and checks Hermiticity, positivity,
all Poisson entries, (4), (6), dark compression and the two asymptotic
coefficients. A separate bright-corner Lyapunov solve verifies (9).
The tested weak-limit ratios are within 0.25% and strong-limit ratios
within 0.047% of their limiting coefficients; these tolerances are finite
evidence, not the analytic proof. Final Poisson residuals are below 1e-10.

The first floating-point run failed the absolute Hermiticity threshold at
K=10,d=10^-5: the residual was about 1.11e-6 despite a small equation
residual. Its script, full stdout/stderr and receipt are preserved under
`failed_attempts/clock`, with a diagnosis. Flagged reduced solves were
then reassembled at 70 decimal digits. No physical parameter, tested grid,
formula or verification threshold changed. The corrected execution passed.
The continuity-at-d=0 inference discussed after (9) is also explicitly
rejected rather than silently imposed.

`dark_space_check.py` passed its first execution. It computes 31 exact
small-cycle cases over Q(i): zero/pi/nonexceptional fluxes, unequal
magnitudes, diagonal detuning, h>=3, one monitored site and the h=1
exception. It verifies 24 exact physical T-sector reductions for K=4,6,8
and all their even-hole levels. These are decisive finite controls of
signs, ranks and hypotheses. They neither prove an all-size rank pattern
nor replace the minimal-gap and path arguments. No author checker was
imported or executed, and no external theorem is imported.

Both complete final result files and all raw run streams/receipts are
preserved. The seal identifies the six permitted prior dependencies,
the independent code/results and the failed attempt. New author clock,
coherent-completion, CQ/cutoff and later frontier artifacts remain unopened.
This packet establishes conditional finite-model mathematics, not native
M2 dynamics, a thermodynamic rate, an empirical parameter, or audit status.
