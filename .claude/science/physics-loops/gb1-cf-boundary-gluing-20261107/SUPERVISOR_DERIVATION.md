# Supervisor derivation before worker comparison

This is the supervisor's analytic route, recorded before reading the new
primary or checker results. Values below are proposed exact derivations to
be compared, not audit verdicts. The raw finite model is in GOAL.md.

## Link subdivision

Let P project onto the full matrix-coefficient sectors j=0,1/2 in L2(SU2).
For S f(g1,g2)=f(g2 g1), Haar invariance gives S* S=I. In the normalized
Peter-Weyl basis phi^j_mn=sqrt(d_j) D^j_mn,

S phi^j_mn = d_j^(-1/2) sum_k phi^j_kn(g1) phi^j_mk(g2).

Thus S(R) is contained in R tensor R. At the new vertex, the endpoint factors
are dual, and invariants exist only for equal representation labels. There is
one contracted intermediate index per (j,m,n), so the invariant image has
dimension 1+4=5. S is onto this image. This is an isometry into a constrained
25-dimensional space, not cloning the link into independent descriptions.

For Q=P tensor P, Q S = S P on the full Haar domain, because S preserves the
representation label on both factors. Let M_g denote color-matrix
multiplication. Then (U2 U1) S = Q M_(g2g1) S = Q S M_g = S U.
The same identity holds for adjoints. This is a full unprojected image
intertwining identity, not only S* (U2 U1) S=U. Iterating the cut is associative
because both routes give f(g3 g2 g1) with the same Haar norm.

Both segment Casimirs intertwine the original Casimir individually:
E1^2 S=E2^2 S=S E^2. Their unweighted sum is twice the original electric term.
Representing one original edge by two segments therefore needs segment weights
whose sum is one. Refining a representation is distinct from adding a new
physical electric contribution.

## Boundary representations and gluing

Fix a finite global graph and a chosen set V0 of vertices at which Gauss law
is to be imposed. For a region edge set A, impose P_v only where v belongs to
V0 and all incident global edges lie in A. Other incident vertices retain
their SU(2) action. Regional edge tensor factors can be regrouped without
duplication for disjoint A,B. On union A+B, impose only the newly internal
Gauss projectors. They commute with earlier projectors, because distinct
vertex actions commute. All parenthesizations therefore apply the same final
projector to the same tensor product, provided constraints at vertices still
touching a third region are delayed. At such a vertex fuse the boundary
representations; do not prematurely choose total spin zero.

For a final two-region seam, write H_A=direct_sum_J M_A(J) tensor V_J and
H_B=direct_sum_J M_B(J) tensor V_J*. The glued invariant space is the sum of
M_A(J) tensor M_B(J), with a normalized contracted vector in V_J tensor V_J*.
Its dimension is sum_J m_A(J)m_B(J), not merely the J=0 term. All labels and
multiplicities are finite at fixed link register and bounded graph degree.

Operators which commute with all the applied constraints descend to the
glued space. Gauge-covariant open operators require matching boundary actions;
one cannot treat every regional operator as a standalone physical observable.
Overlapping edge charts instead embed into one common edge tensor algebra:
each physical edge occurs once, and the two charts agree on its operator.
Their overlapping operators need not commute. This constructs compatible
observables and generators; it does not identify different products of patch
exponentials or provide a fixed-depth nearest-neighbor native update.

## Four-plaquette hand calculation

Take the 3x3 vertex square with all 12 oriented edges. A owns the two left
vertical columns and the three left horizontal edges; B owns the right
vertical column and three right horizontal edges. The interface vertices
are (1,0),(1,1),(1,2). All outer vertices are constrained for this closed test.

Let x,y,z be the fundamental characters at the three interface vertices.
The five-edge tree on either outside column has regional character
T=1+xy+yz+xz: its possible occupied configurations are the empty one and
the three paths pairing two interface ends. Its regional dimension is 13.
The two middle vertical links have boundary character C=(1+xy)(1+yz).
Thus chi_A=T C, chi_B=T, and dim H_A=13*5^2=325.

Using chi_half^2=1+chi_1 and chi_half^3=2 chi_half+chi_(3/2), the A
multiplicities that match B's four labels (2j0,2j1,2j2) are

| label | m_A | m_B | contribution |
|---|---:|---:|---:|
| (0,0,0) | 4 | 1 | 4 |
| (1,1,0) | 5 | 1 | 5 |
| (0,1,1) | 5 | 1 | 5 |
| (1,0,1) | 4 | 1 | 4 |

The predicted glued dimension is 18. Other A labels do not match B and
therefore contribute no final singlet, though they belong to the open region.

An independent hand count uses the binary cycle space: its dimension is
12-9+1=4, hence 16 even occupied subgraphs. All vertices except the center
have degree at most three and therefore a unique singlet when their occupied
degree is even. The center has four occupied ends for the two alternating
plaquette-bit configurations. Four spin-halves have two singlets. Those two
sectors therefore each contribute two states, and the other 14 contribute one:
14+2*2=18. Setting every regional boundary representation to zero keeps only
4 states; replacing every nonempty invariant multiplicity by one gives 16.
Both are proposed concrete error witnesses, not universal no-go claims.

For the open square impose Gauss law only at the center. Its four incident
links contribute singlet rank
sum_(n even) binom(4,n) mult_singlet(n) 2^n = 1+24+32=57;
the eight nonincident links are free. The predicted dimension is
57*5^8=22,265,625. This retains boundary flux rather than closing the patch.

## Scope and literature

The link-splitting/edge-state method is established machinery. Donnelly,
arXiv:1109.0036, section II, equations (8)-(14), was inspected as primary
literature; it supplies context for the normalized embedding. Here the full
finite-irrep closure, compressed transporter identity and graph calculation
are proved from the explicitly supplied model. We consistently use g2 g1
according to our stated path convention. No literature priority is claimed.

Current main also has SU3 Peter-Weyl compression and finite 2D character-gluing
notes. Their setup/scope was inspected, not imported as authority. The one-site
SU2-QCA note has additional dynamics and symmetry premises; its theorem is
not assumed here. A 230-filename bounded prior-art inventory is saved separately.
An open-PR search for gluing returned no matches; this is not an exhaustive
novelty search. The framework's native spatial law, Record realization, state,
continuum and mass-gap bridges remain open.
