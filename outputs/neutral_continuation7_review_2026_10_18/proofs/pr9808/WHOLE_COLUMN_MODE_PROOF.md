<!-- Original PR9808 source SHA256 89106a41f6867ede44d13a6f02002ac5c296ffb24d74848dcddc3b80c5212eae. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Native whole-column modes: energy, readout and first winding kinetics

Status: bounded-support. Root derivation in the supplied one-qubit Hamiltonian
H=-J sum[ZZ_z+lambda XX_x+lambda YY_y], J>0, lambda>0. No new interaction,
oscillator, detector coupling or extra site Hilbert space is introduced.
This is exposed model development, not an observed-particle identification.

## 1. Fixed-order inputs and volume family

Use the local, plane- and translation-equivariant native word construction in
MICROSCOPIC_GROUND_WINDOW_PROOF.md and FEATURE_INTERACTION_PROOF.md:

 U_n H U_n^dagger=J(B_n+R_n), B_n=2N+sum_{j<=n}lambda^j D_j,
 [B_n,N]=0, ||R_n||<=C_n V lambda^(n+1).

The omitted scalar vacuum energy is restored whenever absolute energies are
compared. N counts broken vertical bonds. Each fixed-order coefficient is
proper local once all periods exceed its fixed support. The coefficient form
bound is B_n-Evac >= (2-C_n lambda)N+c lambda^4 sum bad plaquettes.
Here Evac is in units J. All constants and small-lambda cutoffs may depend on
fixed n. No convergence of the all-order expansion is assumed.

Take even cubes L=2 ceil(lambda^(-p)/2), fixed 0<p<4, V=L^3. This is a new
volume family, distinct from the earlier p=4 threshold experiments.
On Q0={N=0}, every column is aligned. Proper local N-preserving coefficients
cannot flip an entire column, so B_n is diagonal on Q0. Its ground subspace
P0 consists exactly of signs s_xy=a_x b_y. Plane symmetries equate all these
energies. A bad transverse plaquette repeats on L layers; hence the gap above
P0 is g0>=c lambda^4 L for small lambda. The N>0 gap stays order one.
With r_n=||R_n||, every actual normalized ground vector u in the U_n frame
satisfies |Eg/J-Evac|<=r_n and

 ||(1-P0)u|| <= r_n/(g0-r_n)=O_n(lambda^(n-3-2p)).             (1)

Choose n high enough for all error ratios used below; n=40 suffices for the
explicit displayed examples. No equality of the true-ground and P0 ranks
is needed. An exponentially large P0 rank does not enter (1).

## 2. Genuinely many-spin light features

Choose a nonwrapping rectangle of whole columns with even side widths
asymptotic to L/4, below L/3, and all four corners separated beyond the
fixed coefficient range, including periodic images. Flip every spin in
these columns. This changes Theta(L^3) physical sites and has no vertical
endpoints. Even widths make the string plane neutral.

The fixed-order corner theorem confines every diagonal excess coefficient
to four corner neighborhoods per layer. On a homogeneous background these
contributions do not depend on side widths or position. At fourth order,
the orientation coefficient is -lambda^4 P/128 per plaquette; four bad
plaquettes cost lambda^4/16 per layer. Thus the exact B_n excess is

 Delta_n=J L[lambda^4/16+O_n(lambda^5)]
        ~J lambda^(4-p)/16 ->0.                              (2)

Plane symmetry transfers (2) to any P0 product background. Distinct corner
patterns give orthogonal configurations. Their whole span is an exact B_n
eigenspace, so the dressed physical span has operator residual at most
J r_n, without a factor from its dimension. Any exact-H window centered at
J Evac+Delta_n with halfwidth w, J r_n<<w<<Delta_n, has rank at least this
span's dimension: its spectral projection is injective on the trial span.
Replacing J Evac by actual Eg changes the center by at most J r_n.
No isolated band is asserted.

On the all-up background the transverse translation orbit has no stabilizer,
so Fourier combinations exist at every transverse momentum. Every trial is
in Qz=0, because whole-column states are invariant under z translation and
U_n preserves translation. The common approximate energy does not construct
a unique exact dispersion. Prepared-span evolution obeys

 ||exp(-iHt)Xi-exp[-i(J Evac+Delta_n)t]Xi|| <=J r_n |t|.

At t~1/Delta_n this is O_n(lambda^(n-3-2p)). For each prescribed algebraic
time lambda^-K/J choose sufficiently high fixed n. The trial family can
depend on n. This is not one fixed family proved frozen for all times, an
exponential lifetime, or a convergent normal-form construction.

## 3. Actual low-energy darkness of the original readout

Use precisely the original C_Q=V^-1/2 sum_r exp[-iQ.(r+ez)] Z_r Z_(r+2ez),
and its connected ground vector q=(C_Q-<C_Q>)g. Let C'=U_n C_Q U_n^dagger,
D its polynomial through n. The local expansion gives

 ||C'-D||<=C_n sqrt(V)lambda^(n+1), ||D||<=C_n sqrt(V).

Proper local operators cannot connect distinct aligned-column configurations.
Thus Q0 D Q0 is diagonal, even though D need not preserve N. Plane invariance
and transitivity on P0 imply Q0(D-c_Q)P0=0 for a common complex scalar c_Q.
Writing u=v+e, v=P0u, gives

 (C'-c_Q)u=Qh D v+d, Qh=1-Q0,
 ||d||<=C_n sqrt(V)[r_n/g0+lambda^(n+1)].

Here g0 remains the gap defined in section1. The expectation shift |<C'>-c_Q|
has the same bound, since <v,Qh Dv>=0. This handles centering even at Q=0
and arbitrary exact ground superpositions.

Let P_low be the actual spectral projection H-Eg in [0,J]. In the U frame,
B_n restricted to Qh is >=Evac+1.5, whereas the actual low endpoint is at
most Evac+1+r_n. Ordered-spectrum Sylvester integration gives

 ||P_low U_n^dagger Qh|| <=C r_n.

The forcing is P R_n Qh and the separation is >=0.5-r_n. No gap within the
possibly dense low N0 spectrum is invoked. Combining the last estimates,

 ||P_low q||<=C_n sqrt(V)[r_n+r_n/g0+lambda^(n+1)]
             =O_n(lambda^(n-3-7p/2)).                         (3)

For n40 the positive spectral weight is O(lambda^(74-7p)). For any fixed
power choose a sufficiently high fixed n: the SAME actual response is thus
smaller than every algebraic power along this family. Constants and cutoff
depend on n; n is not optimized as a function of lambda. Uniformity in exact
ground vectors extends to ground mixtures, including their common centering.
This is a positive spectral-weight bound, not an unqualified retarded response.

There is a stronger exact selection rule when Qz!=0. All N0 vectors have
Tz=I; a vector in a nontrivial Tz character lies entirely in N>=1. The
translation-equivariant normal form and its gap then put the entire actual
spectrum in such a character above Eg+J for sufficiently small lambda.
Consequently all exact grounds and low states have Qz=0, and

 P_low C_Q P_ground=0 exactly for every allowed Qz!=0.        (4)

This includes nonzero momenta tending to zero with L. The Qz=0 response is
bounded by (3). Other detector operators and non-ground states remain open.

## 4. First native winding kinetic coefficient at fixed even L

The absence of offdiagonal proper-local coefficients is not exact absence
of kinetics. Hold even L>4 fixed and use the native word-preserving
homological gauge. Any offdiagonal N0 word needs at least L insertions.
Vertical-plane parity requires at least two whole flipped columns, hence
at least 2L sites; each transverse insertion flips only two sites. Equality
forces exactly two adjacent columns, with their connecting edge at every z
inserted once. There are no other sites, repeated edges or mixed directions.
Every proper nonempty subset of those L rungs has vertical walls, so there
is no intermediate return to N0 and no folded contribution to this first
squarefree winding monomial.

For a proper rung subset S on the periodic cycle, let c(S) be its number of
clusters. Each cluster has two endpoints on each of two columns, so its
H0 excitation cost is 8J c(S). The XX numerator has L factors -J lambda;
L-1 denominators are -8J c(S_k). Its matrix element is therefore

 -J lambda^L S_L/8^(L-1),
 S_L=sum_permutations product_{k=1}^{L-1}1/c(S_k).

A short exact combinatorial evaluation closes this coefficient. Set F(empty)=1
and F(S)=sum_{i in S}F(S minus i)/c(S) for proper S. If its cluster lengths
are ell_a, induction gives F(S)=product_a Catalan(ell_a): removing a site
splits one cluster, the Catalan recursion sums its splits, and summing over
clusters cancels c(S). At the last insertion,

 S_L=L Catalan(L-1)=binomial(2L-2,L-1).

For YY the matrix element per rung is +J lambda s_i s_j. Each site is
flipped once; its product over even L is (+J lambda)^L independently of
column signs. The L-1 denominators again give a minus sign. Thus the first
N0 offdiagonal native term is

 -gamma_L sum_<ij>_xy Xbar_i Xbar_j,
 gamma_L=J lambda^L binomial(2L-2,L-1)/8^(L-1),
 Xbar_i=product_z X_(i,z).                                    (5)

This respects every plane symmetry. N0 is the entire wall-free space, not
only the P0 coefficient ground manifold. Equation(5) is specified in the
native word-preserving gauge; an arbitrary externally chosen block rotation
can alter a displayed effective Hamiltonian and is not being admitted.
The first offdiagonal word count prevents lower-order native gauge terms
from changing this minimal coefficient.

The coefficient's large-L asymptotic is
 gamma_L~2J(lambda/2)^L/sqrt[pi(L-1)].
This is an asymptotic of the displayed FIXED-L Taylor coefficient. It does
not prove that it dominates all other terms when L grows as lambda^-p,
provide a resummation, or give a controlled exponentially long propagation
law. The actual growing-volume results(1)-(4) do not use that extrapolation.

## 5. Checks, imports and residual

Exact rational subset recurrence through L16 checks every proper subset and
the cluster-Catalan identity. A two-column rung Hamiltonian
-2J sum tau_z tau_z-J lambda sum tau_x checks the same squarefree coefficient
by finite-L ground splitting/2gamma_L tending to1. This restricted Hamiltonian
is a coefficient control, not a replacement for the full lattice dynamics.
Independent mathematical and physical checks cover the whole-column bounds
and winding combinatorics. No measured data, fitted scale, assumed scalar
coupling or added interaction enters.

The native static shared-corner energy remains -4 kappa L times shared
corner parities, kappa=J lambda^4/128. Together with(5) this supplies actual
microscopic origins of energy dependence and finite-size kinetics, while
(3)-(4) restrict the original detector access. It does not establish a
propagating universal scalar, a cosmological environment, source preparation,
physical units, a particle mass, or finite-density continuum theory.
Subsystem-symmetric corner and collective-tunneling mechanisms are established
prior-art families; this block derives these scoped results for the supplied
Hamiltonian and does not claim invention of those general mechanisms.
