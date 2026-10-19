<!-- Original PR9784 source SHA256 29e33413840e06ab32dff62349edbcc00975623bbcced33e04eec7ebde19c5ea. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Large neutral feature from a native momentum threshold

Status: bounded-support. Root authored; focused independent mathematical and source checks are preserved alongside this proof. All numerical inputs are exposed model-development controls. No observations have been fitted or independently tested.

## Scope and inherited microscopic construction

Use the supplied one-qubit Hamiltonian
\[
H=-J\sum_r[Z_rZ_{r+e_z}+\lambda X_rX_{r+e_x}+\lambda Y_rY_{r+e_y}].
\]
The selected weak regime, ordered reference, lattice units and momentum remain premises. In the complete compact, layer-even four-wall sector the native first coefficient K1 has the punctured transverse lattice host and two attached interval rays derived in TRANSVERSE_BOUND_STATE_PROOF.md. Fix Qx=Qz=0 and write b=cos(Qy/2) in (0,1]. Host hopping amplitudes are -2 and -2b; ray hopping magnitudes are 2. Their relative sign is gauged along the y ray, without changing its host root. This is the original interaction, with no added potential or scalar field. The normalized original distance-two bond source is lambda(-1,b) in the two orientation roots, to leading dressed order.

This block proves a bound-state threshold and its large spatial extent in K1. It does not assert an isolated eigenstate of the full H. The leading physical excitation energy remains J[8+lambda E], even when the binding gap within K1 tends to zero.

## Exact elimination and critical momentum

The host continuum starts at Eh=-4(1+b), below both ray edges -4. For E<Eh, eliminate the rays with
\[
\sigma(E)=(E+\sqrt{E^2-16})/2<0.
\]
Let g_r(E) be the free lattice resolvent with dispersion -4 cos(kx)-4b cos(ky), using Brillouin measure d²k/(2pi)². In normalized inversion-even roots the origin-Dirichlet resolvent is
\[
G_{xx}=g_0+g_{2x}-2g_x^2/g_0,\quad
G_{yy}=g_0+g_{2y}-2g_y^2/g_0,\quad
G_{xy}=2g_{x+y}-2g_xg_y/g_0.
\]
A bound state is exactly an eigenvalue-one solution of sigma G. No state below Eh can be invisible at both roots: the uncoupled host and rays have no spectrum there.

At the edge define Dx=gx-g0, Dy=gy-g0, Dxy=g(x+y)-g0. Direct integration gives
\[
D_x={\arctan(1/\sqrt b)\over2\pi},\quad
D_y={\arctan\sqrt b\over2\pi b},\quad
D_{xy}={1\over2\pi\sqrt b}.
\]
For example, substituting u=cos(x/2) reduces the relevant integrals to I0=theta and I2=[(1+b)theta-sqrt(b)]/2, theta=atan(1/sqrt(b)). The free recurrence gives
\[
D_{2x}=2(1+b)D_x-2bD_{xy},\quad
D_{2y}=2(1+b)D_y/b-2D_{xy}/b.
\]
Thus Gedge has entries D2x-4Dx, D2y-4Dy and 2Dxy-2Dx-2Dy.

The positive matrix B(b)=sigma(Eh)Gedge has strictly decreasing eigenvalues with b. Indeed, -Gedge is the root compression of the inverse Dirichlet operator 2Lx+2bLy (L=2-S-S*), decreasing in quadratic-form order; |sigma(Eh)| strictly decreases. At b down to zero its smaller eigenvalue tends to 1 and larger diverges; at b=1 the larger is 2-sqrt(3)<1. Consequently exactly one critical bc exists. For fixed b the Birman eigenvalues increase strictly with E from zero to their edge values. There is exactly one simple below-edge bound state for 0<b<bc and none below the edge for b>bc. No assertion about square integrability exactly at threshold is needed.

Closed-form interval arithmetic at 40 decimal digits certifies
\[
0.2347569009270<b_c<0.2347569009271.
\]
The primary runner repeats the certificate. The approximate midpoint root is 0.23475690092702978; its extra digits are not part of the interval certificate.

## Exponentially small binding and divergent extent

Set delta=Eh-Ebound and L=log(1/delta). Uniformly for b near bc,
\[
g_0=-cL+O(1),\quad c=(8\pi\sqrt b)^{-1},\quad
G=G_{edge}+{2DD^T\over cL}+O(L^{-2}),\quad D=(D_x,D_y).
\]
The quadratic host minimum is 2kx²+2bky². Fixed-displacement differences have errors O(delta L); these estimates yield the displayed cavity expansion. Let v be the positive unit eigenvector of B(bc) with eigenvalue one, and m=-mu_edge'(bc)>0. Then
\[
K={2|\sigma_c|(v\cdot D)^2\over c}>0,\qquad
\log(1/\delta)={K/m\over b_c-b}+O(1).
\]
All constants here are derived from the same graph. Numerically K/m=0.95311282744. This is not a fitted exponent or an added selector. Selecting a momentum close to threshold is still an external state choice; the Hamiltonian has not selected it cosmologically.

The normalized host Fourier numerator is
\[
\sqrt2\sigma\{u_x(\cos k_x-1)+u_y(\cos k_y-1)-(u\cdot D)/g_0\}.
\]
On momenta of order sqrt(delta), the constant term dominates. The scaled profile is A_delta/[delta+2kx²+2bky²], with |A_delta|²~delta/c. Parseval then gives the relative-coordinate moments
\[
\langle r_x^2\rangle\sim {2\over3\delta},\qquad
\langle r_y^2\rangle\sim {2b_c\over3\delta}.
\]
These are not merely inferred from L2 convergence: outside a fixed small momentum neighborhood the derivative norm is O(delta L²); inside, numerator gradients and quartic dispersion corrections give o(delta^-1). The continuum integral of px²/(delta+p²)^4 with measure d²p/(2pi)² is 1/(48pi delta²), fixing the constants. Each defect's displacement about their center has one quarter of these second moments.

The ray decay ratio tends to |sigma_c|/2 approximately 0.51045, so the longitudinal interval length stays bounded. The ray probability tends to zero. The large feature is principally two singleton spin flips with a widely spread coherent relative separation. It is not a large number of flipped spins, an extended solid body, or a proven fermion.

## Derived readout weight and its cost

The exact host norm for root vector u is sigma² u*[-G'(E)]u. The ray norm is -sigma'(E)|u|²; the host expression already includes roots. Obtain the derivative by differentiating the exact cavity formula: g0'=-c/delta+O(L) and D'=O(L), hence
\[
-G'(E)={2DD^T\over c\delta L^2}+o((\delta L^2)^{-1}).
\]
One must not differentiate an unspecified big-O remainder alone. Normalization therefore implies
\[
|u|^2\sim {c\delta L^2\over2\sigma_c^2(v\cdot D)^2}.
\]
For the original dressed source lambda(-1,b), the coefficient-model positive weight is
\[
W_C\sim \lambda^2 W_0\delta\log^2(1/\delta),\quad
W_0={c[(-1,b_c)\cdot v]^2\over2\sigma_c^2(v\cdot D)^2}
\simeq0.02574494409835.
\]
The overlap is rigorously nonzero. At the critical matrix with entries (A,B;B,D), vx/vy=B/(1-A). Interval evaluation over the entire critical bracket has B>0, 1-A>0 and
\[
0.5631470858262037<v_x/v_y<0.5631470858279353.
\]
This exceeds bc, proving (-1,bc).v<0. The interval certificate removes a possible cancellation assumption; it does not remove the selected state, Hamiltonian or physical readout identification.

## Controls and limitations

High-precision below-edge resolvent integration independently solves the exact two-root criterion at six b values. At b=.1, delta approximately .0146676815; at b=.2, delta approximately 3.08079397e-11; at b=.22, delta approximately 2.35898872e-27. These are coefficient-model roots, not observations. Finite-graph diagonalization at b=.1 supplies a separate implementation control. The interval bracket and nonzero overlap use elementary formulas, not these quadratures.

Growing spatial extent is paid for by vanishing local source weight and an exponentially fragile binding gap. At fixed lambda, omitted native orders can exceed it. A controlled full-H joint limit needs separate remainder and source comparisons; this block does not supply them. The branch is already known to have a saddle near its anchor, and no isotropic relativistic scalar, universal matter coupling, gravitational range, actual detector response, cosmological background or TOE completion follows. The calculation derives a particular neutral mode and its original-operator overlap from a conditional microscopic model, while preserving those remaining assumptions.
