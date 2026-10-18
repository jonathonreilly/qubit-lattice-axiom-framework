# Derived neutral feature motion and readout form factor

Status: bounded-support. This explains a finite-slab mechanism from the native
four-layer coefficient model, not a three-dimensional scalar identification.
FOUR_LAYER_COLLECTIVE_PROOF.md derives K=-5E-4P and its original source.
For analysis introduce K(u)=-gE-huP with g=5,h=4. The physical coefficient
model is u=1. This is a mathematical expansion variable, not an independently
adjustable native interaction or a parameter fitted to data. A small-u theorem
does not by itself control u=1. The microscopic lambda expansion is separate.

## The neutral feature subspace

In the X basis a flipped set S above the uniform vacuum costs 2g b(S), where
b counts boundary edges. Restrict to even parity in every row and column.
A 2 by 2 square A has four flipped logical columns and b(A)=8, hence energy
16g. Each column contains four physical qubits, so this feature involves
sixteen physical spins. It is not a growing-size particle.

On a sufficiently large periodic square (R>=9 is a conservative no-wrap
choice), the cost-16g subspace consists of elementary squares and, when
allowed by even R, their global complements. To see this, winding boundaries
would need at least 2R edges. Two planar components of total perimeter eight
would be isolated sites and fail row/column parity. A connected component has
bounding widths w,h and perimeter at least 2(w+h). Parity requires w,h>=2,
forcing w=h=2 and all four sites occupied. Holes cannot fit the perimeter
budget. Complement copies do not mix through two local plaquette flips.

## Motion through the existing interaction

There is no first-order matrix element between distinct square features.
Two native plaquette flips connect A to B through the vacuum and A xor B.
Both channels must be retained. The second-order matrix element is

 t_AB=(h^2 u^2/g)[1/16+1/(16-2b(A xor B))].

Exact boundary counting yields -h^2 u^2/(16g) for cardinal displacements
one or two lattice spacings, and -h^2 u^2/(48g) for the eight knight
displacements (plus/minus 2,plus/minus 1) and its transpose. Other distinct
positions cancel: a vacuum-mediated term cancels the disconnected two-feature
intermediate. This cancellation is why a naive vacuum-only approximation
would incorrectly produce infinite-range hopping.

Subtracting the corrected vacuum energy gives the diagonal shift
(h^2u^2/g)[1/8-8/16-8/48]=-13h^2u^2/(24g). Fourier transformation gives

 Delta(k)=16g-(h^2u^2/g)[13/24
  +(cos kx+cos ky+cos 2kx+cos 2ky)/8
  +(cos 2kx cos ky+cos kx cos 2ky)/12]+O_R(u^3).

Thus Delta(0)=16g-29h^2u^2/(24g)+O_R(u^3), and its quadratic curvature is
25h^2u^2/(48g) in each transverse direction. This is a derived two-dimensional
hopping band at small u. It is not a relativistic dispersion or a proof that
the branch remains isolated at u=1. The physical energy scale multiplies all
these coefficient energies by J lambda^4/128.

## Original readout, including ground mixing

Let Ck=cos(kx/2)cos(ky/2). The source continuation used for analysis is the
native coefficient O_k(u)=-12u Ck sum_p exp(-ik center_p)P_p
-18 sum_edges_a cos(ka/2)exp(-ik center_edge)E_edge. At u=1 it is exactly the
previously derived original-readout coefficient, not an assigned coupling.
The ground has admixture hu/(16g) sum_A |A>+O_R(u^2). On feature A, the
weighted diagonal edge sum differs from the vacuum by
-8 Ck(cos kx+cos ky) exp(-ik center_A).
After centering and accounting for ground/excited mixing, the source amplitude
per square is therefore

 u Ck[(36/5)(cos kx+cos ky)-12] exp(-ik center_A)+O_R(u^2).

Its leading norm squared is R^2u^2 Ck^2[(36/5)(cos kx+cos ky)-12]^2.
At k=0 this is (144/25)R^2u^2. The coefficient comes from the same native
paths and state mixing as the Hamiltonian; no free scalar coupling was used.
Restoring the microscopic readout adds lambda^8/(128^2 V) to weights.
At zeros of the displayed form factor no relative error is claimed.

## Numerical challenge, not an uncontrolled promotion

A fixed periodic R5 coefficient calculation at u=.05,.1,.2,.4,.7,1 tests the
series. R5 lies outside the conservative no-wrap theorem statement; its
second-order coefficients can nevertheless be independently checked by its
finite geometry, and its shorter periodic relations allow additional higher
orders. The gap discrepancies at .05 and .1 are about .0002413 and .0019390,
consistent with an O(u^3) remainder. At physical u=1 the second-order k0 gap
76.13333 differs from R5's 74.26777 and R6's 75.44676. The leading total source
weight per area 5.76 compares with 5.89780 (R5) and 5.83068 (R6). These are
unfitted development comparisons, not rigorous u=1 error bars or experiments.
The earlier exact finite-slab positivity theorem at u=1 does not rely on
this truncated expansion.

## Remaining obstacle

The band is an extended superposition of sixteen-spin local features across
a large slab. Its transverse motion and original diagnostic vertex are
constructive, but its thin longitudinal support is supplied. A larger grid
alone does not establish a large particle, a three-dimensional light scalar,
universal source/detector coupling, or a cosmological background. Extending
this mechanism while retaining controlled mobility and a measurable vertex
is the next physical test, rather than identifying this band with a scalar
by naming it.
