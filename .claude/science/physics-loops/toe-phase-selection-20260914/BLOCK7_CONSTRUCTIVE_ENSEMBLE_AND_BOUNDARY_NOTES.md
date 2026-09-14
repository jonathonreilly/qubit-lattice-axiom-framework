# Constructive ensemble proof and boundary audit for the clock route

Personal working notes, 2026-09-14 approximately 18:53 UTC. These are proposed
proof details, not a completed phase theorem. Keep the boundary audit open.

## Exact finite identities already checked

block7_dual_covariance_check.py and BLOCK7_DUAL_COVARIANCE_CHECK.json compare
primal residue sums with dual character filters for the six-face cube lattice
at N=2,3,4,5,8. Both the partition normalizations and
Cov(n)/beta+Cov(m)/beta_dual=I agree, with beta_dual=N^2/(4pi^2 beta).

On a (5,2,2,2) four-dimensional box with 92 edges, 78 plaquettes and curl
rank 53, two separated loop currents check the selected-link Gaussian
integration against a separate character expansion. The correct coefficient
is beta/2 times sum rho_e^2/n_e. Replacing it by beta times that sum gives
an error .02579986470; replacing the ORIGINAL external phase current by the
renormalized frequency gives an error .02009913352. Both mistakes are rejected.
Positive phase-integral curvature checks pass for 1,3,5 current factors.
A positive function built with a negative mixture coefficient violates the
proposed componentwise log-sum bound, confirming why mixture positivity is
load-bearing. Shifted one-dimensional closed-current cosets approach their
Gaussian covariance uniformly in the sampled shift as beta grows; these
finite observations do not establish the general uniform bound.

## A direct finite positive-ensemble construction

The FS cosine identity can be re-derived algebraically:

 (1+A cos x)(1+B cos y)
 = (1+3A cos x)/3 + (1+3B cos y)/3
   + (1+3AB cos(x-y))/6 + (1+3AB cos(x+y))/6.

Start with at most one occupied oscillator per edge, with frequency
rho_e=2pi k_e. Repeatedly choose two currents whose edge supports are within
Euclidean distance <=1 and apply the identity. Each resulting branch replaces
two currents by one, so the recursion terminates. All mixture coefficients
are positive and sum to one. Supports remain disjoint inside a branch, so
frequency addition/subtraction never cancels an occupied edge. Every final
current support is connected using edge-to-edge distance <=1.

A final current with support S and L edges has amplitude at most

    K(rho) <= 3^(N_1(S)) product_(e in S) z_(|k_e|),

where N_1 counts canonical edges at distance <=1 from S. To justify the
exponent, its merge ancestry contributes at most L-1 operations. Every
retention that drops a neighboring current can be assigned a distinct
initial edge outside S within distance <=1 from an intermediate subset of
S. Dropped initial edges never return in that branch, so these witnesses are
distinct and there are at most N_1(S)-L of them. This count needs a careful
formal reread but does not appeal to the numerical size of the expression.

Use Fejer kernels instead of a formal Dirac comb. With z_k=4 k^2,

 Fejer_h(x)=1+2 sum_(k=1)^h (1-k/(h+1)) cos(2pi k x)

is a positive mixture of the constant 1 and the factors 1+z_k cos(2pi k x):
the latter coefficient is 2(1-k/(h+1))/z_k. The residual constant coefficient
is positive because sum_(k>=1) 2/z_k <1 (the elementary integral bound
sum k^-2 <2 suffices). Products of these mixtures preserve positivity of
all mixture weights. Individual initial factors need not be positive; after
the Gaussian damping they will be.

A canonical edge in Z^4 has exactly 107 canonical edges within Euclidean
distance <=1, counting itself. Proposed hand count: 23 parallel edges and
28 edges of each of three perpendicular orientations. This finite geometric
count must be independently enumerated. Therefore N_1(S)<=107 L. Also
log(4 k^2)<=k^2 log 4 for k>=1. Set

    beta_1=(107 log 3+log 4)/(4pi^2).

Then K(rho)<=exp[beta_1 ||rho||^2]. This is a deliberately conservative
constant, not a claim about a physical critical coupling.

## Exact damping without ambiguous contour factors

Let Q=d^T d on one-form potentials, V=Q^+ on its positive range. For
coclosed currents rho in that range, Gaussian characteristic functions are
exp[-beta rho^T V rho/2]. Choose mutually plaquette-nonadjacent selected
edges B. With u_e=rho_e/Q_ee on B and zero elsewhere,

    rho_tilde=rho-Q u,
    rho^T V rho-rho_tilde^T V rho_tilde=sum_(e in B) rho_e^2/Q_ee.

The selected components of rho_tilde vanish and delta rho_tilde=0. This is
an exact quadratic identity, avoiding the preprint's convention ambiguity.
For a separated ensemble, all selected sets can be combined: cross terms
vanish because supports are disjoint and selected edges share no plaquette.
The identity therefore holds termwise after expanding the entire cosine
product, for arbitrary EXTERNAL phases rho(a).

A concrete 32-coloring uses edge orientation (four choices) and the three
transverse coordinate parities (eight choices). Each color has no two edges
in a plaquette. Choosing the color with largest squared-current weight gives
sum_B rho_e^2>=||rho||^2/32. Since Q_ee<=6 in four dimensions,

    z(rho)<=exp[-a ||rho||^2], a=beta/384-beta_1.

For a>0 every final factor 1+z cos is positive. A 19-coloring of the
maximum-degree-18 conflict graph could improve the constant to 1/228;
that optimization is not needed for existence and is not used yet.

## Gauge averaging and Fejer convergence

For a FREE potential graph, average the Fejer product over vertex gauge
rotations modulo one. This is nonnegative. In Fourier form it removes
noncoclosed currents. After the separated-ensemble expansion, disjoint
vertex neighborhoods ensure a signed sum of currents is coclosed only
when each nonzero participating current is coclosed. Thus noncoclosed
factors can be deleted under gauge averaging while keeping positive mixture
coefficients. On a contractible box, coclosed one-forms are in range Q.
The remaining finite Gaussian integral has exactly the desired positive
phase representation.

For a fixed finite graph, the Fejer Fourier coefficients are bounded by one
and tend to one. The coclosed Gaussian Fourier series and all phase
 derivatives converge absolutely, so the partition approaches the theta
function for a shifted integer-curl lattice. Equivalently, the supported
physical field is dA in da+d Z^E. Gauge-volume factors cancel in ratios.
This argument must be written with a precise lattice quotient before it is
used as a universal boundary statement.

## Prospective local surface and packing estimate

For a nonzero coclosed current rho whose connected support has L edges,
its bounding box has side at most 3L. A coordinate-path contraction to a
corner fills each edge difference with at most 3R plaquettes when the box
side is R. Summing over a closed current cancels the paths, producing a
2-form mu with delta mu=rho and

    ||mu||_1 <= 9 L ||rho||_1 <= 9 L^(3/2) ||rho||_2.

Hence |rho(w)|^2 <=81 L^3 ||rho||^2 max_(p in box) |dw(p)|^2.
This proposed homotopy bound needs an explicit chain formula and tests.
In one separated ensemble, supports are disjoint. For fixed L and a
plaquette p lying in a current's box, the whole support lies inside a cube
of side <=9L about p; there are at most 4(9L)^4 edges there. Therefore at
most 26244 L^3 such currents can be assigned to p.

Taking z/(1-z)<=2z once z<=1/2, using ||rho||^2>=(2pi)^2 L, and splitting
exp[-a||rho||^2] into two factors gives the candidate uniform bound

 c(beta) <= (4*81*26244/(a*e))
            sum_(L>=1) L^6 exp[-a (2pi)^2 L/2].

The estimate uses t exp(-a t/2)<=2/(a e). It is intentionally loose and
still decays exponentially as beta grows. It would imply a uniform
phase curvature bound -c(beta)||dw||^2. Neither the geometric constants nor
boundary applicability have been certified in the current source yet.

## Boundary and topology audit: do not skip

The free-potential integer-curl model d Z^E is straightforward. Its dual
partner ker(delta) intersect Z^P on a FREE primal box is represented by
potentials on a relative or wired dual complex. Boundary currents can then
look like open paths ending on the wired boundary. They must not silently
be treated as compactly supported closed currents in Z^4. A local filling
and gauge-averaging argument valid for free potentials does not automatically
cover that relative boundary problem. This is currently unresolved.

A potentially cleaner route is a periodic four-torus. Isotropic periodic
cube measures have translation/cubic symmetry and reflection positivity
before any subsequential limit, removing the need for a finite-Z_N
Ginibre limit argument. Both integer-curl sublattices exist with periodic
potential graphs. Harmonic modes, however, must be retained explicitly.
Condition on electric currents AND harmonic flux to leave a coset of the
integer coexact lattice delta Z^C. On the dual side condition to leave a
coset of the exact lattice d Z^E. Their real projections sum to I-P_harm,
not I. P_harm has finite rank six and fixed local entries tend to zero as
the four-torus volume grows.

Small contractible currents admit the local filling bound. Winding or
large-diameter currents have support length at least order the torus side.
On coexact potential directions, a global Poincare estimate costs only a
power of that side, while their activities decay exponentially in length.
This may give a vanishing correction or a uniform small bound. Harmonic
Gaussian integration can couple winding currents, so they cannot simply be
deleted factor-by-factor; integrate the positive renormalized product over
harmonic angles, and keep its source curvature estimate valid. Precise
periodic integer lattices, flux cosets, large-current packing and limiting
projectors are the next load-bearing tasks.

An isotropic periodic-limit OS phase would still not automatically identify
the selected anisotropic continuous-time clock Hamiltonian or prove finite
spatial transfer gaps converge without a state-limit argument. Keep those
claims separate. No public block-6 or block-7 PR has been opened.


## Periodic harmonic resolution under development, 19:00 UTC

For a torus, use the connected compact subtorus
H=(ker d + Z^E)/Z^E of flat potential shifts. Its character annihilator is
Z^E intersect range(Q). Averaging a shifted Fejer product over H therefore
produces the theta representation of the integer-curl lattice d Z^E.
One may first average vertex gauge rotations to remove noncoclosed currents
factorwise using support separation, then keep the harmonic average of the
remaining positive product. Individual winding currents MUST remain.

For a term surviving the harmonic average, the TOTAL signed current R lies
in range Q. The selected-link identity applies to R and the total selected
u. Disjoint supports and mutually nonadjacent selected links make all cross
terms vanish. Thus the whole product renormalizes with the same independent
factors z_rho and unchanged external phases even when individual rho has a
harmonic component. Terms with nonzero total winding vanish on both sides.
After renormalization the product is positive, so Gaussian AND harmonic
integration preserve the phase-curvature bound by the log-expectation
variance identity. This needs an explicit finite torus check.

The source direction w=Q^+ mu is in range Q and has no harmonic component.
Split currents at r=L/8 for an equal-side torus of side L. A connected support
with r<L/8 should have a consistent contractible lift with bounding box
side <=3r. Prove this using a spanning tree of unit edges and distance-one
gaps; a possible winding cycle would have length at least L. The local
surface/packing estimate applies to these small currents.

For r>=L/8, use the global coexact Poincare bound
||w||^2<=L^2 ||dw||^2/16, since the first nonzero torus Laplacian eigenvalue
4 sin^2(pi/L)>=16/L^2. There are at most 4L^4/r disjoint currents of a
given size r. The same activity split therefore gives a total large-current
curvature contribution bounded by

    L^6/(a e) sum_(r>=L/8) r^-1 exp[-b r]
    <= 8^6/(a e) sum_(r>=1) r^5 exp[-b r],
    b=2pi^2 a.

Combined with the small-current term, a prospective uniform constant is

    c(beta) <= [8503056 S_6(exp(-b)) + 262144 S_5(exp(-b))]/(a e),
    S_j(q)=sum_(r>=1) r^j q^r.

This is a proposed conservative constant pending verification of the lift
and packing counts. It decays exponentially and beta*c(beta) decreases once
a=beta/384-beta_1>0. Very large finite beta and N suffice; optimizing the
threshold is irrelevant to proving existence.

For the full torus Fourier lattice L_N, partition into cosets of delta Z^C;
for its scaled dual M_N, partition into cosets of d Z^E. No informal
conditioning on a noninteger harmonic coordinate is necessary. Each affine
coset is a shifted discrete Gaussian in the relevant real subspace. The law
of total covariance gives the lower bounds on the coexact and exact
projectors. These sum to I-P_harm. The finite-rank harmonic projection is
kept; its fixed local matrix elements vanish as the volume grows. The
infinite Fourier projector diagonal for a plaquette ij is
P_exact,ij=(|d_i(k)|^2+|d_j(k)|^2)/|d(k)|^2, with P_coexact=1-P_exact.

Periodic isotropic clock measures have compact local subsequential limits,
translation/cubic symmetry, charge conjugation and both reflection
positivities. Uniform covariance bounds could pass to any such limit;
the harmonic term vanishes and the multiplier bounds imply clustering plus
a directional discontinuity of the bounded-score spectrum. The block-6 OS
argument would then establish a gapless reconstructed state. This does not
yet justify the finite-cylinder gap convergence statement for the clock
model, nor the selected anisotropic continuous-time Hamiltonian.


## Further exact conventions to carry into the proof

Use equal EVEN torus side L>=4 for the concrete transverse-parity coloring
and for convenient reflection planes. The 32-coloring is not a valid
periodic coloring at odd L. An alternative finite greedy coloring of the
maximum-degree-18 plaquette conflict graph works with 19 colors at any
sufficiently nondegenerate side; it would still imply the weaker 1/32 bound,
but that alternative has not yet been implemented.

The 107-neighbor count was independently enumerated and agrees with the
hand count. With the proposed constants, beta_1=3.0127299032238786. At
beta=2000 the candidate a=2.1956034301094545 and candidate beta*c(beta)
is 4.424343075e-10. N=16384 gives beta_dual=3399.774766686335. These numbers
only evaluate the proposed bound; they do NOT certify the phase while the
proof obligations remain open. A much larger conservative threshold is
acceptable if a geometric count needs loosening.

The local chain homotopy can be made explicit. Let b be the coordinatewise
minimum corner and P(x) the path from b to x in coordinate order. For a
positive edge e=(x,j), define K_1(e) as MINUS the sum of jk plaquettes for
all k>j along the k-coordinate segment b_k,...,x_k-1. In that strip,
coordinates below k are fixed at x, coordinates above k at b, and coordinate
k varies. Then

    boundary K_1(e)=P(x)+e-P(x+e_j).

Summing against a closed current cancels the vertex paths and gives a
filling. Each strip has at most R plaquettes and there are at most three,
so ||K_1 rho||_1<=3R||rho||_1. Verify the sign and chain equation on explicit
integer cochains before using the general bound.

For the theta-function quotient, let S=im d and K=d Z^E. The dual lattice
K^* consists of y in S with d^T y in Z^E. The bijection
rho=2pi d^T y identifies K^* with 2pi Z^E intersect range Q, with

    y=d Q^+ rho/(2pi), ||y||^2=rho^T Q^+ rho/(4pi^2).

Poisson summation thus gives the Gaussian Fourier series used by the
Fejer/harmonic-average construction, up to a positive a-independent factor.
For a field source f, use potential shift w=Q^+ d^T f. Then
dw=P_S f and ||dw||^2=||P_S f||^2. The completed-square MGF therefore
turns the phase curvature bound into Cov_a(field)>=beta(1-beta c)P_S.
This applies to every affine coset, with its perpendicular part held fixed.

For the full-rank dual-lattice identity at COMPOSITE N, use the perfect
character pairing on (Z/NZ)^P. The annihilator of ker(delta mod N) is
im(d mod N). Inclusion is immediate; equality follows because a matrix
and its transpose have the same image cardinality modulo N, for example
by integer Smith normal form. No vector-space argument over Z/NZ is used.
Thus L_N^*=Z^P+(1/N)d Z^E exactly for all positive integers N.

On the four-torus, rank(im d_1)=rank(im delta_2)=3(L^4-1), and the harmonic
two-form space has rank six. The integer coexact lattice is carried to an
integer exact lattice on the translated dual torus by the signed Hodge
map. Its norm and the positive-ensemble proof constants are unchanged.
These finite cochain ranks, Hodge signs and projector identities still need
explicit checks in the runner.

The next finite torus test should use two separated winding loops with
opposite winding. Individually their harmonic averages vanish, but their
product has a nonzero zero-winding term. Dropping winding factors would
incorrectly replace that term by one. The selected-link renormalization
must agree with the original character expansion AFTER harmonic averaging,
with the original external phase and the corrected half-factor damping.


## Small-current lift proof and completed finite torus checks

Connect the r occupied unit edges by at most r-1 extra unit edges, using a
spanning tree in the distance-one proximity graph. Nearest points of two
coordinate unit edges with integer endpoints can be chosen as endpoints;
if their distance is <=1, they either coincide or are joined by one lattice
edge. The auxiliary connected graph therefore has at most 2r-1 edges.
If r<L/8, it has fewer than L edges. Every nonzero-winding simple cycle on
the torus needs at least L edges, so this graph has no such cycle. Its lift
to Z^4 is consistent. A spanning-tree path between any two lifted vertices
has length at most 2r-1, so the coordinate bounding side is <=2r-1, safely
within the previously used 3r bound. Closed-current divergence lifts unchanged.
This supplies the intended general lifting argument, subject to final review.

The new block7_torus_geometry_check.py passes on an even four-torus L=4:
256 vertices, 1024 edges, 1536 plaquettes, 1024 cubes, 256 four-cells.
It checks every chain-composition zero, the componentwise two-form Laplacian,
the six harmonic two-forms, and the signed translated Hodge identity
star_2 delta_3 = - d_1 star_3. The two opposite winding loops give a
nontrivial harmonic-averaged partition 0.9697240333076211 before AND after
selected-link renormalization. Dropping winding factors incorrectly gives
one, an error .03027596669238. A separate Fourier potential inverse matches
the sparse cochain operator on every surviving current. Finally 2000 exact
edge-chain homotopy identities in a four-dimensional box pass, with maximum
filling area 12 at side four. See BLOCK7_TORUS_GEOMETRY_CHECK.json.

For the full phase proof, the finite-volume covariance bounds should read

 beta(1-delta_beta) P_coexact <= Cov_L_N(n)
   <= beta P_coexact + beta delta_dual P_exact + beta P_harm,

with delta_beta=beta c(beta) and delta_dual=beta_dual c(beta_dual).
The harmonic term is not omitted at finite volume. The separate exact
Poisson identity also yields Cov_L_N(n)<=beta I, ensuring uniform second
moments and an absolutely continuous bounded spectral density in a local
translation-invariant limit. The clock score contact identity then transfers
clustering and the angular discontinuity to a bounded physical plaquette
observable. The remaining author work is to write and adversarially review
the complete positive-ensemble/Fejer/coset proof, fix constants conservatively,
and test the full finite combinatorial expansion. No phase claim has yet
been promoted or publicly shipped.
