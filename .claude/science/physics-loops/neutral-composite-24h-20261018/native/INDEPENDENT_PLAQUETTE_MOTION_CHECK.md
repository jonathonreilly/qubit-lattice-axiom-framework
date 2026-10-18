# Plaquette-defect motion in the auxiliary coefficient-model expansion

Checked K(u)=-g E-hu P with g=5,h=4, where E is the nearest-neighbor Ising sum in the rotated X basis and P is the sum of four-spin plaquette flips. The parameter u is a mathematical expansion device; the native leading coefficient model is at u=1. This calculation supplies no error estimate at u=1.

## Degenerate subspace

A flipped-spin set S above the all-plus X vacuum has excitation cost 2g b(S), where b is its nearest-neighbor edge boundary. A single 2x2 plaquette has b=8 and cost 16g. Row/column-even constraints are essential: without them the cost-16g subspace contains other shapes.

For a sufficiently large periodic square, boundary eight cannot include noncontractible domain walls: noncontractible components of the boundary must have total trivial homology and require at least two winding contours, of total length at least 2R. Choosing R>=9 is a conservative sufficient regime in which the following planar argument is unambiguous. Up to global complementation, the minority domains are planar finite components. Two components with total boundary eight must be two isolated sites; they cannot satisfy both even row and even column parity. A single component of boundary eight has bounding widths w,h with 2(w+h)<=8. Even row/column parity requires at least two occupied rows and two occupied columns. Thus w=h=2, and parity then requires all four sites of that elementary square. A hole would itself cost at least four boundary edges and cannot coexist with a parity-compatible exterior within this budget.

Accordingly the relevant degenerate subspace is precisely the translates of one plaquette, plus their global complements when R is even and the complement obeys the selected row/column constraints. The two background copies cannot mix at second order on a sufficiently large square. For smaller periodic geometries one should check wrapping separately instead of using the planar classification.

## Second-order matrix element

Let A and B be distinct plaquette flip masks. To connect |A> to |B> in two perturbations, the intermediate masks are empty and A xor B. There is no additional local two-plaquette decomposition of the same mask. A nontrivial short periodic plaquette relation would need separate treatment, avoided in the stated large-R regime. There is no first-order matrix element within the single-plaquette subspace.

The two denominators are 16g and g[16-2b(A xor B)], and the numerator from the two -hu flips is positive. Hence

    t_AB=(h²u²/g) [1/16+1/(16-2b(A xor B))].

An independent exact-rational boundary enumeration yields:

- cardinal displacements (±1,0),(±2,0),(0,±1),(0,±2): -1/16;
- knight displacements (±2,±1),(±1,±2): -1/48;
- all other nonzero displacements: zero.

The cancellation to zero for sufficiently separated plaquettes is the vacuum-mediated contribution cancelling the disconnected two-defect intermediate; it should not be dropped by retaining only one intermediate channel.

## Diagonal subtraction and dispersion

Subtract the second-order vacuum energy. The perturbation at A contributes 1/16+1/16=1/8. Every other plaquette contributes the same bracket as t_AB above. Thus the diagonal relative coefficient is

    1/8 + 8(-1/16)+8(-1/48)=-13/24.

Fourier transformation gives exactly

    Delta(k)=16g-(h²u²/g) [13/24
       +(cos kx+cos ky+cos 2kx+cos 2ky)/8
       +(cos 2kx cos ky+cos kx cos 2ky)/12]+O(u³).

In particular Delta(0)=16g-29h²u²/(24g)+O(u³), and the coefficient multiplying either kx² or ky² is 25h²u²/(48g). An exact-rational recomputation reproduced -13/24, -29/24 and 25/48. A separate finite planar enumeration of all <=4-spin subsets in a 4x4 box found only its nine elementary squares satisfying boundary eight and row/column parity; the all-size exclusion rests on the perimeter argument above, not this finite enumeration.

## Scope

This is a complete second-order small-u dispersion for the identified finite-box degenerate coefficient-model subspace, in the no-wrap regime. The even-R global-complement copy must be retained where present, but does not alter the local coefficient. Positivity of the curvature near u=0 does not prove the same branch or dispersion at native u=1. The original microscopic lambda expansion and this auxiliary u expansion are distinct; neither a stable physical particle nor a propagating scalar follows merely by inserting u=1 into the truncated series.
