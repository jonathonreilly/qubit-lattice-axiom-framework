<!-- Original PR9795 source SHA256 fc686f0b4a98bd723b3f0a147453381bf29ee066380ee0d6d414298eb19ada3d. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Native four-layer neutral collective response

Status: bounded-support. The physical Hilbert space remains one qubit per
site. Fix a transverse R by R square (R>=3), open or periodic, and exactly
four longitudinal layers. Take lambda->0 at this fixed geometry. The native
Hamiltonian is -J sum ZZ_z - J lambda(sum XX_x + sum YY_y), J>0.
The state is the actual ground state. Neither the geometry, weak anisotropy,
nor ground-state preparation is derived from observations.

## Native coefficients, with no added interaction

Use the analytic wall-free block reduction and real native-word gauge of
WHOLE_COLUMN_MODE_PROOF.md and COLUMN_READOUT_PROOF.md. A logical column
operator Xbar flips all four physical spins; Zbar labels the two aligned
column states. This is a derived subspace, not an added qubit at a site.
Write P=sum transverse plaquettes Zbar Zbar Zbar Zbar and
E=sum transverse edges Xbar Xbar. For periodic longitudinal boundaries,

 H_eff = scalar + J lambda^4 K/128 + O_R(J lambda^5),
 C_eff = scalar + lambda^4 O/(128 sqrt(V)) + O_R(lambda^5),
 K=-4P-5E, O=-12P-18E=3K-3E, V=4R^2.

C is the original normalized distance-two ZZ diagnostic. At height four its
periodic sum counts each opposite pair twice; this convention is retained.
The diagonal square coefficient is four layers times -1/128. The winding
coefficient is c4=binomial(6,3)/8^3=5/128. The marked denominator coefficient
is A4=36/5, giving c4 A4/2=18/128 for C. Square differentiation gives 12/128.
A source parameter is used only for differentiation at zero; the physical
Hamiltonian is unchanged. The block connection cannot contribute at order
four: all earlier energy coefficients are scalar, and the first offdiagonal
connection is at least order four.

Completeness uses the native word classification: nonconstant diagonal
returns first occur as a transverse square. Repeated-edge returns are
orientation independent. A distinct wall-free configuration requires whole
columns flipped. Four insertions can flip at most eight distinct spins;
thus the first offdiagonal word flips exactly two adjacent columns, once at
each of four layers. All lower block/source coefficients are scalar on the
entire wall-free block. No assumed scalar field or independent coupling is
inserted. Both terms have the same order, so a plaquette-dominant expansion
would be invalid here.

## Ground sector and exact positive response

In the logical Z basis K is stoquastic. Edge pair flips on a connected grid
connect every configuration of a given global Z parity. Perron-Frobenius
therefore gives one strictly positive ground vector in each parity sector.
Row and column X products commute with K. For even R they preserve parity
and fix these positive vectors. Both would therefore belong to the all-plus
row/column-X block. In the X basis this block is connected by plaquette
flips and has a unique positive lowest vector. Consequently the global
ground is unique. For odd R, row/column X exchange the two parity sectors,
so their positive grounds are degenerate. Their sum and difference occupy
all-plus and all-minus row/column-X sectors. Global Z interchanges these
and commutes with K and O; their response is identical.

In the all-plus X basis the dimension is 2^((R-1)^2). Free bits at (i,j)
expand to four corners (i,j),(i,R-1),(R-1,j),(R-1,R-1). Plaquette flips span
this row/column-even space. Every amplitude of its ground g is positive.
E is diagonal and nonconstant for R>=3: the uniform pattern and a flipped
2 by 2 plaquette have different boundary-edge products. Thus

 q_O=(O-<O>)g=-3(E-<E>)g,
 ||q_O||^2=9 Var_g(E)>0.

This is exact finite-dimensional positivity, independent of numerical pole
identification. R=2 is excluded because E can be constant in this block.
The positive vector lies orthogonal to the ground within its sector, hence
has weight at positive coefficient excitation energies.

## Transfer to the original microscopic response

Fix a smooth compactly supported F whose support excludes zero. Let q_C be
the centered original C acting on any actual microscopic ground. Analytic
finite-box reduction, the coefficient ground gap, and smooth functional
calculus give

 <q_C,F(128(H-Eg)/(J lambda^4))q_C> / [lambda^8/(128^2 V)]
 = <q_O,F(K-e0)q_O> + O_R(lambda).

The wall-excited spectrum remains order J and is excluded from this scaled
window. For odd R, exact physical plane symmetries continue the coefficient
ground doublet as an irreducible doublet; the original diagnostic commutes
with them, so every ground has the same response. Even R has a unique
continued ground. Constants are not uniform in R. The error is absolute;
no relative estimate is asserted at a zero limiting weight. Choosing a
nonnegative F equal to one on the finite positive source spectrum proves
positive actual low-energy response for sufficiently small lambda.

## Boundary challenge: open longitudinal layers

Keep only the original open distance-two pairs (0,2),(1,3). End spin flips
cost 2J, interior flips 4J; each site now occurs in one diagnostic pair.
The same native word classification gives

 K_open=-18P-16E,
 O_open=-51P-48E=(17/6)K_open-(8/3)E.

Two end squares have eight times the periodic per-layer energy coefficient,
and the two interior squares have the ordinary coefficient: 2*8+2=18.
Their source factors give 2*24+2*1.5=51. For a proper rung subset S, let
b(S) count open nearest-neighbor mismatches and d2(S) open distance-two
mismatches. The energy cost is 4J b(S), source change -4d2(S)/sqrt(V).
Exact enumeration of all 24 orders gives sum product 1/b=8 and its weighted
mean sum d2/b=3. Thus the energy winding coefficient is 1/8=16/128 and
source coefficient 3/8=48/128. The same PF argument yields positive variance,
with factor (8/3)^2. This boundary change preserves the mechanism but changes
its numbers. It does not derive a preferred physical boundary condition.

## Momentum source on the transverse torus

For allowed Q=(2pi mx/R,2pi my/R), Qz=0, the leading original source is

 O_Q=-12 cos(Qx/2)cos(Qy/2) sum_p exp(-iQ center_p) P_p
     -18 sum_edges_a cos(Qa/2) exp(-iQ center_edge) E_edge.

Each plaquette vertex has local coefficient -3; each edge endpoint -9.
Use unit-edge/unit-square lifted centers across the periodic seam, never
averages of wrapped coordinate labels. O_Q dagger=O_-Q. At zero momentum
this reduces to O above. At (pi,pi) on even R the leading source vanishes;
this is not an all-orders selection rule.

## Scope

This derives a neutral finite-slab response and its original-readout vertex
from the existing interaction. Numerical spectra are coefficient-model
controls, not full microscopic diagonalizations or observed data. A positive
finite response does not establish a stable propagating scalar particle,
three-dimensional bulk limit, Lorentz invariance, universal matter coupling,
cosmological field, or measurement/environment identification. The supplied
thin geometry and weak-coupling regime remain assumptions to challenge.
