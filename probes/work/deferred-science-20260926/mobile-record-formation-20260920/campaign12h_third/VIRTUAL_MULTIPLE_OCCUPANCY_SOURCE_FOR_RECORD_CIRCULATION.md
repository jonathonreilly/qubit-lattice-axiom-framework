# A virtual multiple-occupancy source for one record-circulation matrix element

Date: 2026-09-22. Status: author exact perturbative coefficient in an explicitly
enlarged finite model; independent check pending. This does not satisfy the
original exact one-record-per-site microscopic premise.

## Construction and its premise cost

The previous note supplied a four-record circulation term and showed that it
releases a particular gauge trap. A familiar way for collective circulation
to arise from simpler motion is virtual hopping through energetically costly
multiple occupancy. Fourth-order ring exchange is established Hubbard-model
physics. For context, the fourth-order expansion and convention-dependent
spin coefficient in section I.A of
[Larsen et al., arXiv:1812.04277v1](https://arxiv.org/abs/1812.04277v1)
were checked; no phase or numerical coupling is imported from that fermionic
spin model into the construction below.

Here use four distinguishable bosonic payload species, one permanent particle
of each, on a four-vertex cycle. Their charges are (+,+,+,-). Each may occupy
any vertex, including vertices already holding another species. Interactions
cost

    H_0 = U sum_x n_x(n_x-1)/2, U>0.

Every particle hops to its two neighboring vertices with amplitude t and
with the same spin-half gauge-link shift required by its charge. The total
number of each species is conserved. Allowing virtual multiple occupancy
is essential: replacing this space by an exact hard-core one-record space
removes these intermediate states and this derivation.

Let reference signs along the cycle be s=(+,+,-,-), and use a field bit b_i
with E_i=b_i-1/2. Start with particle positions (0,1,2,3) and field bits
(1,1,0,1). The target has positions (1,2,3,0) and bits (0,0,1,0). This is
exactly the labeled four-cycle transport for that charge word. Both states
have one particle per vertex and the same local Gauss values, with twice
the generators equal to (0,-2,-2,0). Untouched external links can supply the
corresponding boundary charges if this plaquette is embedded in a larger
zero-Gauss lattice.

The total labeled Hilbert space has dimension4^4*2^4=4096. The selected Gauss
sector has dimension158. Its one-particle-per-site subspace P has dimension12;
all other states Q have H_0 energy at least U. The exact checker enumerates
this sector, checks every allowed elementary hop and its reverse, and verifies
Gauss conservation. The hopping adjacency T has maximal row degree eight,
so ||T||<=8. We write the complete Hamiltonian as H_0+tT.

## Selected fourth-order coefficient

There are24 time orderings in which each particle makes its designated
clockwise hop exactly once. Every one obeys the link-capacity restriction:
the four links are distinct, and their initially eligible shifts do not
depend on the order of the other three hops. None of the three intermediate
states lies in P.

The first and third intermediate states each cost U. If the first two hops
are adjacent edges, the middle state costs U; if they are opposite edges,
it has two doublons and costs2U. Sixteen orders have energy sequence
(U,U,U), and eight have (U,2U,U). Their denominator sum is

    16/U^3 + 8/(2U^3) = 20/U^3.

At zero reference energy the Feshbach operator is

    H_F(0) = -t^2 P T Q (Q H_0 Q + t Q T Q)^(-1) Q T P.

Expanding its inverse, the selected fourth-order matrix element is therefore

    <target|H_F(0)|initial> = -20 t^4/U^3 + O(t^6/U^5).

The checker obtains20 both by summing all actual intermediate-Q paths in
the full selected sector and by enumerating the24 designated hop orders.
The sign is the three negative energy denominators; it differs from the
positive g convention used to state the earlier supplied Hamiltonian. The
nonzero renewal probability there depends on the squared amplitude and is
unaffected by giving every circulation term the same opposite sign.

Lower orders cannot take all four distinct payloads to their target sites.
Odd total hop orders between one-particle-per-site states vanish on the
bipartite cycle. Paths returning to P after two hops also cannot connect
this particular target after two additional hops: each two-hop P return is
an identity or a two-particle transposition, whereas a four-cycle is an odd
permutation. The checker verifies that the complete number of such folded
two-plus-two paths to this target is zero. Thus usual fourth-order folded
terms do not alter this selected labeled circulation coefficient. This is
not a derivation of every term of an energy-independent effective Hamiltonian.

For a conservative explicit remainder at zero reference energy, put
r=8|t|/U<1. The resolvent Neumann series converges, and the selected remainder
after the fourth-order term obeys

    |R| <= 8^6 |t|^6 / [U^5 (1-r)].

This follows by bounding all terms with at least six total hopping factors;
the fifth-order entry is zero by bipartite parity. The bound is deliberately
loose and is not an accurate finite-coupling error estimate. For |t|<U/16,
Weyl's bound also separates the low cluster from the remaining spectrum by
at least U-16|t|. This is a controlled finite auxiliary model, not a claimed
many-body or continuum expansion with a volume-independent bound.

## What the calculation does not supply

Second-order diagonal and same-charge exchange terms are present, as are
other fourth-order processes. The cyclic term is not the entire effective
Hamiltonian. Distinguishable payloads identify the requested permutation
matrix element; when payloads are identified or traced out, distinct
permutations can contribute to the same charge-only matrix element. The
number20 cannot simply be inserted as the complete bare-qutrit dynamics.

Most importantly, virtual multiple occupancy enlarges the microscopic record
space and replaces exact occupancy exclusion by an energy penalty. This
does not establish a native implementation of a framework in which a site
can participate in only one permanent record at all times. A construction
using additional intermediate sites would be another model and would need
its own locality, preparation and formation checks.

No irreversible birth generator has been derived in this elimination. Naive
birth rules acting on virtual vacancies could create additional permanent
records during the excursion, so appending the earlier birth jumps to this
larger Hamiltonian would require a new analysis. The calculation supplies a
specific coherent interaction and exposes its premise cost; it does not
close the native carrier or open-system formation obligations.

