# Local pair form of the compensated Hamiltonian

Root derivation, September 23, 2026. Conditional on the explicit compensated
microscopic law in local_compensation_author. This is an extension of that
frozen candidate, not a change to it. The new locality and first-sector formulas
below are analytic candidates pending selective exact controls and independent
comparison. No thermodynamic dynamics theorem is claimed in this note.

## 1. The finite-graph claim

Let G=(A union B,E) be a finite simple bipartite graph, with maximum degree z.
Use the supplied tensor-product hard-core record algebra, rotor links, physical
Gauss law and all-A-occupied P space. F_a is the unsigned outward hop sum from
A site a. Define S_(ac)=F_c F_a P for unordered distinct A sites a,c. The
outward sums commute, including at shared B destinations where both orders
vanish by hard-core exclusion. The frozen compensated rotor fourth coefficient
has the exact local form

    H4_infinity^C=-2 sum_(unordered a,c with distance(a,c)=2)
                                        S_(ac)^* S_(ac).       (1)

There are no terms for two disjoint stars. Each term is bounded, self-adjoint,
nonpositive and supported on the union of the two overlapping stars. On a
bounded-degree family it is a finite-range interaction with a volume-independent
bound for each local term. This is stronger than merely bounding a fixed-volume
operator polynomial in the global T.

The claim does not say that the full Hamiltonian is nonpositive: its electric
term K D is nonnegative and unbounded. It does not make the total operator
norm independent of volume. It supplies a local decomposition from which a
separate dynamics/volume analysis may start.

## 2. Operator derivation on every P charge and field configuration

The local compensation is

    C_infinity=sum_a F_a^*F_a Q_a,
    Q_a=product_(c!=a, c in A, distance(a,c)=2) n_c.

At rotor order the two diagonal counts in the spin definition cancel.
F_a^*F_a preserves every A occupancy. On the one-vacancy space with missing
site a, the c term is zero if c=a or if c and a have a common B neighbor.
For all other c its gate is one. Thus, with A1=Pi1 T P=-sum_a F_a P,

    A1^* C1 A1
      =sum_(ordered a!=c, distance(a,c)>2)
                                  P F_a^* F_c^* F_c F_a P.     (2)

The notation distance>2 includes disconnected components. Different vacant
A sites give orthogonal intermediate blocks, so there are no terms connecting
the a-vacancy and a'-vacancy blocks in (2). The C1 interaction preserves their
vacancy location exactly.

For Z=Pi2 T Pi1 A1, two outward hops can only vacate two distinct A sites.
Their order does not matter; the two negative T signs cancel. Different
unordered pairs of vacant A sites are orthogonal. Hence

    Z=2 sum_(unordered a<c) S_(ac),
    Z^*Z/2=2 sum_(unordered a<c) S_(ac)^* S_(ac).       (3)

Here the sum for Z is into the direct sum of the pair-vacancy ranges.
The two ordered terms of each distant pair in (2) are equal to twice its
S^*S. Subtracting (3) in the already-derived canonical coefficient
H4_infinity^C=A1^* C1 A1-Z^*Z/2 proves (1). No commutation between different
S^*S terms is assumed. The proof does not select a charge sector or a special
formation output.

For degree z, ||F_a||<=z_a and ||S_(ac)^*S_(ac)||<=z_a^2 z_c^2.
The number of A sites c sharing a B neighbor with a is at most z(z-1).
Thus

    ||H4_infinity^C||<=2 sum_(a<c, distance2) z_a^2 z_c^2
                       <= |A| z^5(z-1).             (4)

This deliberately loose bound is extensive. Local terms near one site are
bounded by a constant depending only on z, not on the number of vertices.
The frozen fixed-graph microscopic approximation still has graph-dependent
constants; (4) alone does not upgrade it to a volume-uniform approximation.

## 3. The initial magnetic dynamics on every such graph

Take q=1_A with all B empty and a divergence-free field. There is only one
P matter word at this minimal record number. For an A pair define
r_ac=|N(a) intersection N(c)|. The two hops in S_ac choose distinct B
destinations, so its diagonal path count is

    z_a z_c-r_ac.                                      (5)

Different destination assignments give the same final occupied B pair only
if they exchange two common neighbors b,d. Their electric shifts differ by
the circulation around the simple four-cycle a-b-c-d-a. Each unordered pair
{b,d} of common neighbors contributes one shift and its adjoint, with unit
coefficient. All other outputs are orthogonal. Consequently (1) reduces to

    H4_initial^C=c_G I-2 sum_(simple unoriented 4-cycles p)
                                            (W_p+W_p^*),       (6)
    c_G=-2 sum_(a<c,r_ac>0)(z_a z_c-r_ac).

Choose either orientation once for every unoriented four-cycle; W_p^* is the
other orientation. This formula includes graphs with multiple common neighbors
and does not assume the geometry is a hypercubic lattice. If there are no
four-cycles, the first-sector magnetic operator is a scalar, as the path
calculation requires. One must not infer a nonzero magnetic field term on a
square-free graph from the general construction.

For comparison, the original unchanged law has on this same initial sector

    H4_initial_original=c_original I
                            -2 sum_p(W_p+W_p^*),
    c_original=sum_(a in A) z_a^2
                         +sum_(b in B) z_b(z_b-1).     (7)

Indeed M=|E| I; use (3) over all pairs, the identity
|E|^2=sum_a z_a^2+2 sum_(a<c)z_a z_c, and
2 sum_(a<c)r_ac=sum_b z_b(z_b-1). Pairs with disjoint stars contribute only
to the scalar. Thus the compensation retains the entire first-sector
magnetic dynamics up to a scalar on every fixed simple bipartite graph,
not only the cube.

The frozen diagonal D on this sector is sum_e E_e^2. Its linear term is
minus sum_(a in A)div E_a, which vanishes by the initial Gauss law. Therefore

    h_initial=K sum_e E_e^2-2delta sum_p(W_p+W_p^*)

up to the scalar delta c_G. The cube has six A pairs, z_a=3 and r_ac=2,
so c_G=-84 and c_original=60. On other graphs the count, and not the local
shift coefficient, changes. This is still a supplied Hamiltonian/gauge model;
it does not derive electromagnetism from minimal record axioms.

## 4. Local formation terms and the remaining volume question

For a birth edge e=(a,b), a in A, the effective resolved jump is

    B_(e,sigma)=P j_(e,sigma) F_a P.                   (8)

Only an old-record hop from that same a can create the needed A vacancy.
Its destination must differ from b. Equation (8) is supported on the A star,
has norm at most z_a-1, preserves Gauss and increases total record number by
two. Coherent edge channels are the specified sums over sigma and remain
local. The spin family has the same support and no larger path weights.
These statements provide finite-range bounded jump terms after the limit.
They do not turn the supplied birth reservoir into an autonomous energy source.

The common diagonal D is a sum of commuting local terms. In the interaction
picture of K D, a bounded interaction or jump initially supported on X is
conjugated only by diagonal terms intersecting X. The other diagonal terms
commute with it and with all those terms, so they cancel exactly. Its support
is enlarged by one fixed interaction neighborhood, while its operator norm
is unchanged. On a bounded-degree graph this is a promising route to a
volume-controlled local dynamics construction.

There are real remaining obligations: strong measurability for rotor operators,
complete positivity and compatible infinite-volume states, physical Gauss
constraints, boundary independence, and a justified locality bound for the
time-dependent interaction-picture generator. Norm continuity on all bounded
rotor operators cannot simply be assumed because electric energies are
unbounded. Nor can finite-graph microscopic error constants be promoted to
volume-independent ones. These are next questions, not conclusions of (1).
