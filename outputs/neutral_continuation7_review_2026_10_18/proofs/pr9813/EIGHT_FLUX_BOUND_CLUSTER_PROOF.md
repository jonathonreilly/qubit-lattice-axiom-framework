<!-- Original PR9813 source SHA256 5b9972b6e6293597dc45fefdbef82cd6e4982a1aa4ab011668957311f9beaff1. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Native eight-flux bound cluster and original scalar source

Status: conditional-support. Fixed-height, weak-anisotropy selected-plane-sector result for the supplied one-qubit compass Hamiltonian. All computations are exposed model development. No observed mass, gravitational coupling, fermionic statistics or three-dimensional scalar identification is established.

## Inputs and question

Use the native Hamiltonian and column encoding in [TEN_LAYER_NEUTRAL_BOUND_PROOF.md](TEN_LAYER_NEUTRAL_BOUND_PROOF.md), and the local normal forms in [POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md](POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md). Each encoded column is ten physical qubits, not an additional on-site degree of freedom. Put L=10, Delta=L/16, b=3L/8192, D=8b and gamma=binomial(2L-2,L-1)/8^(L-1). The question is whether native interactions bind an additional neutral feature and whether the original C=(LR²)^(-1/2) sum ZZ_distance2 sees it.

The Q count is the number of negative column plaquettes. D4 costs J L Q lambda4/64. The native D6 interaction is -J b lambda6 sum_nearest PpPq, plus a term linear in Q. Hence its shape-dependent cost is 2J b lambda6 times the perimeter of the negative-plaquette set. No attractive potential is supplied.

## Bound geometry

In Q8 the minimum allowed perimeter is twelve. An eight-cell set with perimeter at most twelve must be connected and fit a box with w+h<=6. The candidates are filled 2×4 or 4×2 rectangles, or a 3×3 box with one missing cell. The latter violates the exact even row/column syndrome constraints. The former correspond to two flipped whole columns separated by two lattice spacings along one axis. They are distinct translations and orientations modulo flat plane backgrounds, not unique raw spin configurations across sectors.

Separated columns have perimeter sixteen, so the cluster binding below that continuum is JD lambda6. The nearest other Q8 shape has perimeter fourteen and gap JD lambda6/2. Adjacent columns have Q4 and must not be included with this denominator. The compact object contains twenty flipped physical spins; its existence does not establish a thermodynamic large-radius particle.

The existing edge winding is -J gamma lambda10 Eedge. Translating a horizontal pair along its axis has one Q8 intermediate of gap JD lambda6; the other ordering passes through Q4 and is later, order lambda16. Perpendicular translation has two Q8 intermediates, each of gap JD lambda6/2. Thus

 t_parallel=gamma²/D, t_perp=4gamma²/D,
 H_A(q)=e(lambda)-2J lambda14[t_parallel cos qx+t_perp cos qy]+later,

with the rotated expression for B. No orientation change occurs in two edge moves. Higher-order mixing is not set to zero. Absolute common energy corrections are left in e(lambda), not discarded as dispersion. The geometry and all two-edge paths are independently enumerated in neutral_eightflux_geometry.py.

## Native environment-dependent winding

The leading scalar source cancels for independent pairs. It is essential to include a native correction to winding at the same order as binding affects that cancellation.

At order L+2 a neighboring-column flip uses one transverse insertion per vertical layer except one layer with three. Bipartite parity excludes two layers with two. The exceptional layer is either a direct edge plus a repeated edge, which has no background plaquette monomial, or a three-edge detour around one of the two adjacent plaquettes. The latter gives

 H_detour=-J d_L lambda^(L+2) sum_edges sum_adjacent_p Pp Eedge.

There is no proper model-space intermediate in a detour word. Scalar order-two folds cannot contribute a plaquette monomial. The subset recurrence in neutral_detour_winding.py sums every ordering, keeping YY signs and each denominator -2JN. At L10 it gives

 d=1076510135/10567230160896.

Introduce h sum ZZ_distance2 only as a derivative device. Its intermediate excitation cost is 2JN-2h D2, so each denominator's logarithmic derivative is D2/(JN). Marking the recurrence gives d'/d=B/J with

 B=1616665793187/110234637824.

Independent coordinate-set permutation sums at L4 and L6 verify the recurrence; the L10 subset sum represents 12! ordered words. This is a native virtual-process calculation, not a new interaction. The background factor is Pp because the two YY edges retain the initial four-column spin product.

## Connected source, including ground and excited mixing

For a fixed horizontal endpoint cluster S there are two intermediate adjacent-column features I1,I2. In the native no-wall frame the local diagonal energies are 0,E,E,F, with

 E=J Delta lambda4+O(lambda6), F=2E+U, U=-3JD lambda6+O(lambda8).

The difference U follows from the perimeter twelve of each intermediate and of S; the terms linear in Q cancel. Write t=J gamma lambda10. Vacuum-to-intermediate hopping is -t1, intermediate-to-S hopping -t2, where

 t1=t+2Jd lambda12+common scalar correction,
 t2=t-2Jd lambda12+the same scalar correction.

Both adjacent plaquettes of the second edge become negative after the first edge. Other scalar winding corrections cancel from the connected coefficient below. The established uniform-source derivatives are E'/E=3/J+O(lambda²), U'/U=5/J+O(lambda²), t'/t=A/(2J), A=432/17. The factor five marks the six-step native rectangle process.

To second order in hopping, direct insertion of the differentiated Hamiltonian between its perturbed eigenvectors gives

 M=2t1t2[F'/(FE)-(t2'/t2)/E+(t1'/t1)/(F-E)-E'/(E(F-E))].

This vanishes identically for F=2E and equal hopping derivative ratios. Expanding the binding and detour terms gives the unnormalized local original-source amplitude

 M=m lambda18+O(lambda20),
 m=3D(gamma/Delta)²(A-8)+(8gamma d/Delta)(B-A/2)
  =1361400132699035/945539748965690376192
  =1.439812693425366e-6.

The binding contribution is 5.140856140783967e-7 and the detour contribution 9.257270793469692e-7. Omitting the detour would therefore miss most of this coefficient. The four-state numerical control verifies the complete eigenvector matrix element, not just the derivative of the binding energy.

The original observable differs from a Hamiltonian derivative in a parameter-dependent no-wall frame by a connection commutator. In a real frame the connection has zero diagonal entries; an adjacent whole-column transition starts at lambda10/J. Multiplication by the lambda4 energy gap and a lambda6 hopping admixture makes its contribution to this S transition lambda20. A direct transition to the two nonadjacent columns requires at least 2L insertions. Thus it cannot change m. A subsequent flux-normal-form rotation must transform the observable as well; its connection is not dropped. Computing in the unreduced no-wall frame avoids that error.

At q0 the two translated orientations each have normalized amplitude m/sqrt(L) lambda18. Their C4-even sum carries weight 2m²/L lambda36. This is a source coefficient for the bound endpoint subspace; actual-state transfer is addressed separately below. It is not an emission rate or universal matter coupling.

## Actual polynomial-grid cluster and positive motion

Use even R~lambda^-p, 1<p<2, fixed L10, and the selected positive plane fibre. The local Q normal form gives volume-independent fixed-Q coefficient norms. Reducing Q8 to its two minimum orientations uses the gap JD lambda6/2. Retain both orientations, never divide by their possibly tiny internal splitting. With centers at integer r, their configurations are r±ex and r±ey. Inversion fixes each orientation, and the real microscopic Hamiltonian permits real, even momentum matrices. The checkerboard Z symmetry excludes odd powers of lambda in this sector. Finite-order paths have uniformly bounded displacement moments. Consequently

 h(q)-h(0)=J t_parallel lambda14 diag(qx²+4qy²,4qx²+qy²)
             +O(Jlambda14|q|4+Jlambda16|q|²).

Unknown common energies and q0 orientation mixing are retained in h(0). The min-max principle bounds the increment of each ordered eigenvalue between J t_parallel lambda14 |q|²[1+o(1)] and 4J t_parallel lambda14 |q|²[1+o(1)]. This does not require an internal orientation gap. For q=2pi n/R with fixed n≠0, an arbitrarily high fixed-order construction with final tail O(JR²lambda40) transfers these positive bounds to the actual microscopic eigenvalues: its relative error is O(lambda^(26-4p)). The first wall-band separation uses lambda4 R²=o(1), as before.

The exact rank-two cluster projector has error O(R²lambda34), using the lambda6 external gap. Multiplication even by the crude original-source norm O(R) gives O(lambda^(34-3p)), smaller than lambda18. Fixed-order centered source coefficients on the vacuum have uniform finite-pattern Gram bounds. Source admixtures from other Q8 shapes cannot change m: two winding operations first reach Q8 at order lambda16, and mixing into the endpoint from other Q8 shapes is at least lambda4. Direct nonadjacent-column processes start at order20. Hence the actual cluster weight is

 2m²/L lambda36[1+o(1)] = 4.146121184297614e-13 lambda36[1+o(1)].

At q0 C4 selects the even orientation atom. Whether it is the upper or lower ordered band depends on the as-yet uncomputed mixing sign; neither a simple two-pole splitting nor an isotropic individual curvature is asserted. The atom may be degenerate with the odd state without invalidating its total spectral weight.

## Verification

Independent checks: INDEPENDENT_Q8_CLUSTER_CHECK.md, INDEPENDENT_DETOUR_WINDING_CHECK.md, INDEPENDENT_Q8_SOURCE_CHECK.md. The exact geometry, marked subset sum and four-state eigenvector controls are separate from full microscopic diagonalization. The actual two-band transfer and positive dispersion bounds are independently checked in INDEPENDENT_Q8_TRANSFER_CHECK.md. No uniform global-ground-sector selection is inferred from the selected-sector calculation.
