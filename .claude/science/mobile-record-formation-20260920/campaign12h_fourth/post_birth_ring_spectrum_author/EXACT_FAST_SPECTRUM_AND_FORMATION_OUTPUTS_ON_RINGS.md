# Exact fast spectrum and formation outputs on rings

Personally derived conditional author result, 2026-09-23. Scientific review
standing is recorded separately in the source-bound independent report. This
note does not derive a native quantum law or a three-dimensional field phase.

## 1. Target and supplied model

The previous campaign controlled a fast effective generator containing
`delta epsilon^-2 H2 + delta H4` and finite formation jumps. It identified
the field Hamiltonian before the first formation. The missing next step is
to understand the actual matter state produced by that event. The exact
six-site example previously checked has only one vacancy and cannot form a
second pair. Here the ring size is arbitrary, and rings with at least eight
sites have remaining room for another pair. No later waiting-time law is
inferred solely from having that room.

Fix an integer L>=3 and the oriented ring with vertices 0,...,2L-1 and
links e=(e,e+1 modulo 2L). The A sublattice is even. The supplied matter
alphabet is q=0,+1,-1 with hard-core occupancy. Link fields are integer
rotors, and the supplied Gauss equation is

    E_e-E_(e-1)+1_A(e)-q_e=0.

A charge c hopping forward lowers E_e by c; hopping backward raises it by c.
Every legal hop has amplitude -1. Let T be their sum, W the number of empty
A sites, P=1_(W=0), Pi_1=1_(W=1), and

    H2=-P T Pi_1 T P.                                      (1)

Restrict to total record number N=L+2 and total charge L, the sector after
one pair is added to the all-A-plus, all-B-vacant preparation. There is one
minus record and L+1 plus records. All A sites are occupied; exactly two
B sites are occupied and h=L-2 B sites are vacant. Every such charge word
has integer Gauss solutions. Writing ell=E_(2L-1), all other E are uniquely
fixed by the recurrence, with ell free in Z.

Fourier transformation in ell gives L^2(S^1,dtheta/(2pi)) with a finite
matter fiber of dimension

    D_L=(L+2) binomial(L,2).

An individual theta fiber is not a normalizable physical state. Statements
below about physical band weights refer to direct-integral projections and
normalizable input field densities.

## 2. Exact vacancy and cyclic-word coordinates

Let H be the h-element subset of vacant B positions, with B position j
denoting vertex 2j+1. Starting at occupied vertex A0 and reading clockwise,
list the N nonzero charges. Let r in {0,...,N-1} be the position of the
single minus within that list. Thus (H,r) labels every P charge word once.

Each empty B has two occupied A neighbors. A hop to it followed by the
reverse hop contributes -1 to H2. Consequently the diagonal is -2h.
Every other two-hop return to P fills the temporarily empty A with the
charge from its other B neighbor. It exists precisely when one of the
two B neighbors is vacant and the other occupied. The vacancy then moves
one step around the L-site B ring, with amplitude -1.

If this move does not cross A0, the cyclic charge sequence starting at A0
and ell are unchanged. When the hole moves from B_(L-1) to B_0 across A0,
the first charge c_0 moves through the circulation cut, ell increases by
c_0, and the charge word rotates left. In the r coordinate this is the
unitary

    V(theta)|r> = exp(i c_0(r) theta)|r-1 mod N>,
    c_0(0)=-1,  c_0(r)=+1 for r!=0.                       (2)

The reverse vacancy move applies V(theta)^dagger. Over one complete word
rotation the phase is the total charge, so

    V(theta)^N=exp(i L theta) I.

Its N simple eigenvalues are exp(i alpha_s), where

    alpha_s=(L theta+2pi s)/N,  s=0,...,N-1.                (3)

The modulus of each normalized eigenvector component is 1/sqrt(N): the
eigenvector recurrence has unit-modulus coefficients. In a V eigenbasis,
H2 is exactly the direct sum of hard-core vacancy hopping on the L-site
ring, with h vacancies, boundary twist alpha_s, and constant -2h.
This proves the factorization as an operator identity, including every
boundary phase. It is not a fit of eigenvalues.

## 3. Complete spectrum

For h hard-core particles in one dimension, use increasing coordinate
order to identify the occupation basis with fermionic wedge coordinates.
Interior nearest-neighbor hops have the same matrix element. A hop across
the ring boundary crosses h-1 other occupied coordinates, producing the
sign (-1)^(h-1). Thus the fermion twist is alpha_s+pi(h-1), modulo 2pi.
The one-particle Fourier momenta are

    k_(m,s)=[2pi m+alpha_s+pi(h-1)]/L,  m=0,...,L-1.

Slater determinants diagonalize each wedge sector. The complete fiber
spectrum, with multiplicity, is

    E_(s,I)(theta)=-2h-2 sum_(m in I) cos(k_(m,s)),
    |I|=h.                                               (4)

Because h=L-2, one may equivalently use the two omitted modes. The full
sum of cosines vanishes. Replacing their momenta k by k-pi gives the
two-particle representation

    E_(s,{m,n})(theta)
      =-2h-2cos(p_(m,s))-2cos(p_(n,s)),
    p_(m,s)=[2pi m+alpha_s+pi]/L,  m!=n,                   (5)

up to a permutation of momentum indices. Formula (5) also follows by
complementing the hard-core vacancy occupations. It keeps the physical
two occupied B positions explicit.

The fermionic wedge representation is a spectral tool. It does not
establish that the supplied records have fermionic statistics in other
graphs or in the framework.

For the resolved and coherent first-mark outputs specified in section 5,
the full labeled spectral probabilities in the two-particle representation
(5) are respectively

    p_res(s,m,n)=4 sin^2(pi(m-n)/L)/(N L^2),
    p_coh(s,m,n;theta)=p_res(s,m,n)[1+cos(theta-alpha_s)].   (5a)

At degeneracies sum these weights over equal energies. They follow from
the neighboring-coordinate Slater determinant and the word eigenvector
recurrence proved in section 5. Thus (5) and (5a) specify the complete
formation-output spectral measure, not only its first two moments.

This kind of one-dimensional charge-order factorization is established
machinery. Context includes [Ogata and Shiba, Phys. Rev. B 41, 2326
(1990)](https://doi.org/10.1103/PhysRevB.41.2326) and
[Penc et al., arXiv:cond-mat/9701051](https://arxiv.org/abs/cond-mat/9701051).
Their abstracts were read for prior-art identification; a Hubbard theorem
is not imported into this different staggered record operator. The legal-hop
reduction, twist sign and diagonalization required here are given above.

## 4. Lowest fiber band and its gap

Choose the eigenphase alpha_*(theta) of V closest to zero modulo 2pi.
Except at the finitely many angles L theta=(2j+1)pi modulo 2pi it is
unique and lies between -pi/N and pi/N. The two lowest one-particle
levels in (5) then have momenta (alpha_*+pi)/L and (alpha_*-pi)/L.
Hence the smallest fiber eigenvalue is

    e_0(theta)=-2h-4cos(pi/L)cos(alpha_*(theta)/L).         (6)

To see that another pair does not improve this value, write any sum of
two distinct cosines as 2cos(half-separation)cos(center). The largest
possible absolute separation factor is cos(pi/L), achieved by adjacent
momenta. Among their centers, the phase alpha_* gives the one closest
to zero. More distant momenta have a strictly smaller separation factor.

On |theta|<pi/L the minimizing word branch is s=0, giving

    e_0(theta)=-2h-4cos(pi/L)cos(theta/N),
    e_0''(0)=4cos(pi/L)/N^2.                              (7)

At theta=0 the ground eigenvalue is simple. The next distinct eigenvalue
comes from adjacent momentum pairs in the word branches s=+1 and s=-1:

    gap_L(0)=4cos(pi/L)[1-cos(2pi/(L N))].                 (8)

For nonadjacent pairs the separation factor is at most cos(2pi/L) when
L>=4, while cos(pi/L)cos(2pi/(LN))>=cos(pi/L)^2>cos(2pi/L).
For L=3 every pair is adjacent. This verifies the ordering used in (8).

The gap in (8) is asymptotic to 8pi^2/L^4. At the branch-crossing angles
specified above the two lowest word branches coincide exactly. These are
properties of this explicit spectrum; no uniform rotor or volume gap is
assumed in applying it. The curvature concerns the single global ring
holonomy, not a transverse three-dimensional magnetic mode.

## 5. The actual first formation output

Apply the effective resolved mark on edge (A0,B0) which creates a plus at
0 and a minus at 1. Before that mark can act, the old plus at 0 must hop
to vertex 2L-1. This is the only allowed old-record destination for this
mark on the ring. Thus its normalized matter word is

    q_0=+1, q_1=-1, q_(2L-1)=+1,
    q_a=+1 for other even a, q_b=0 for other odd b.        (9)

The circulation ell increases by one. This contributes a common Fourier
factor exp(i theta), which does not affect a band probability. The two
occupied B positions are neighbors on their L-ring and r=1. For the
opposite charge orientation of the same mark, r=0 with the same B positions
and the same circulation factor. The coherent edge channel is the
unnormalized sum of those two orientations in the existing model, so its
normalized output is their equal, positive superposition.

The lowest two-particle Slater determinant at adjacent B positions has
squared amplitude

    a_L=4 sin^2(pi/L)/L^2.                               (10)

This follows by taking the determinant of the two normalized plane waves
with momentum separation 2pi/L. In the h-vacancy coordinates, the same
absolute value follows by taking the complementary minor of the unitary
L-point Fourier matrix. Boundary gauges only change phases.

Each resolved matter word has word-band probability 1/N. Equations
(2), (6) and (10) therefore give the following exact result, almost
everywhere in theta:

    ||P_low(theta) psi_resolved(theta)||^2
       =w_L=4 sin^2(pi/L)/(L^2 (L+2)).                    (11)

P_low denotes the rank-one lowest-fiber-band projection away from the
crossing angles; choose the full lowest eigenspace at a crossing. These
finitely many exceptional angles have zero measure for every normalizable
rotor density. Since the right side of (11) is independent of theta,
the same probability w_L holds for the direct-integral band measurement
after this resolved mark for ANY normalized pre-event field density.
This last statement uses trace-class normalization and the fact that the
band projection acts fiberwise; it is not a fixed-theta preparation.

For the coherent mark, if u_r is a component of the word eigenbra then
u_1=exp(i(theta-alpha_*))u_0 by (2). Consequently

    w_coh(theta)=w_L[1+cos(theta-alpha_*(theta))].          (12)

For a normalizable input, integrate this function against its angle
probability density. Near theta=0 it approaches 2w_L. A sharp integer-flux
input has uniform angle density and gives w_L: exp(-i alpha_*) has period
2pi/L, so its product with exp(i theta) has zero circle integral for L>=3.
These are different preparations; the single-fiber and normalizable
statements must not be interchanged.

For either instrument and every theta, the first and central second
moments of H2 in its normalized output are

    <H2>=-2h,    Var(H2)=2.                              (13)

Indeed each of the two adjacent occupied-B configurations has exactly
two outward vacancy moves. For the coherent output the two charge words
have disjoint one-step neighbors and no connecting path of at most two
steps returning to the same B occupancy, for L>=3. Applying H2+2h directly
therefore gives norm squared two and vanishing expectation. This also
proves the moments after integrating a normalizable field density.

Examples: L=3 gives w_L=1/15. L=4 gives w_L=1/48 and the theta=0 coherent
weight 1/24. As L grows, w_L is asymptotic to 4pi^2/L^5. These explicit
weights, variance and gap are the information supplied for choosing a
post-formation approximation. A lowest-band preparation is an additional
physical operation, with its locality, energy and occurrence still to be
specified if that route is pursued.

## 6. Relation to the microscopic fast-time regime

The previously checked uniform-spin fixed-graph approximation is in
`../../campaign12h_third/FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md`.
Its exact source is identified in
the accompanying author seal. In its target, set tau=epsilon^2 u/delta.
The H2 term then has unit coefficient, while H4 and the bounded effective
formation dissipator have coefficients O(epsilon^2). At fixed L and
compact u intervals, Duhamel gives an O(epsilon^2) difference from pure
H2 propagation in that target. Combining the parent O(epsilon) microscopic
bound with strong convergence of normalized spin shifts gives the rotor
H2 propagator for normalizable convergent P-supported initial states,
for every joint epsilon->0, S->infinity sequence at fixed L.

This includes the earlier relation epsilon^2 S(S+1)=delta/K, but only
on this compact FAST-time scale. It does not prove convergence of
post-event microscopic conditioned histories, a fixed nonzero laboratory-
time field limit, or a uniform growing-L limit. The specified mark outputs
identify mathematically attainable effective-model initial states; a
finite deterministic microscopic event time is not postulated.

The rate of a later effective formation is bounded at fixed graph. Its
probability over this fast interval is consequently O(epsilon^2). Although
the L>=4 sectors permit a later pair, its ordinary-time waiting law and
field backreaction need a separate calculation. In particular, applying
finite-dimensional secular averaging before the large-spin limit does not
by itself control the small gaps and holonomy crossings displayed here.

## 7. Checks and scientific boundary

The author runner constructs every two-hop Laurent coefficient directly
from legal physical hops, and separately from vacancy/word coordinates.
Equality of the integer coefficient dictionaries checks the operator
factorization for the listed finite rings. Dense Hermitian spectra and
formation overlaps test the analytic formulas at declared angles.
The general proof is the local-hop enumeration and wedge calculation
above; floating agreement does not establish arbitrary L by itself.

The earlier six-site result is recovered by L=3. The complete spectrum
and specified formation-output measure for general L are the new scoped
contribution. The formation generator, quantum carrier, staggered background,
unit-rotor limit, clock and preparation remain supplied. No native selection,
three-dimensional photon phase, finite fuel, empirical matching, or TOE
completion is established here. The immediate next target is the actual
subsequent-formation dynamics with the full field degrees of freedom.
