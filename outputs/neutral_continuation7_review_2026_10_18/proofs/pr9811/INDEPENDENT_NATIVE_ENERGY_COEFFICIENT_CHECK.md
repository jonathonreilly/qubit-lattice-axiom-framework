<!-- Original PR9811 source SHA256 3a79a46fa7720adc3bf8e58590aa88ad694f569e48b575277ca7ce6cb9bb1c4f. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Addendum: original bond-energy readout into the L10 Q4 pole

This is a separate zero-temperature native-source calculation from the earlier infinite-temperature results above. Disposition: PASS for the leading coefficient and its symmetry-controlled small-q cancellation; actual-grid errors require the uniform estimates stated below.

## Source definition and coefficient differentiation

Use H_q=V^(-1/2) sum_b exp(-i q.center(b)) h_b, q_z=0. Differentiating all native bond couplings by their Fourier mark is an algebraic way of inserting this existing operator. It does not adopt an added interaction. For nonzero complex Fourier mode, do the differentiation first for real cosine/sine variations and then combine linearly. H_-q=H_q^dagger.

For the elementary four-edge plaquette process, the four transverse numerator marks, relative to the plaquette center, sum to

    2 cos(qx/2)+2 cos(qy/2).

Only the longitudinal broken bonds enter its leading denominators. At q_z=0 their marks equal those of their transverse columns. The sum of the three inverse-denominator logarithmic derivatives is minus three under a uniform rescaling. By the square symmetry of the fully summed plaquette coefficient, this is distributed equally over the four vertices. Their Fourier average is cos(qx/2)cos(qy/2). Consequently

    F4(q)=2 cos(qx/2)+2 cos(qy/2)-3 cos(qx/2)cos(qy/2).

F4(0)=1, as required because the effective energy coefficient itself has degree one in a common rescaling of all bond couplings. This derivation refers to the complete symmetry-summed coefficient, not to equal weights in each individual virtual path.

For a horizontal winding process, all L transverse numerator bonds have the same transverse midpoint. Each virtual denominator is supported on the two participating columns. Equal column weights follow by exchanging the columns, and the total denominator derivative is -(L-1). Thus

    Fx(q)=L-(L-1) cos(qx/2),
    Fy(q)=L-(L-1) cos(qy/2).

Again both equal one at q=0. No longitudinal phase survives because q_z=0.

## Vacuum rotation and normalization

The four bad plaquettes of a horizontal adjacent-column pair have centers, relative to the edge midpoint, (plus/minus 1, plus/minus 1/2). Its diagonal excitation-energy insertion is therefore

    J Delta lambda^4 F4(q) cos(qx) cos(qy/2).

The leading virtual pair amplitude in the ground state is t/(J Delta lambda^4), t=J gamma lambda^L. Combining the diagonal insertion on this component with the direct winding insertion -t Fx gives the horizontal orientation amplitude

    A_x(q)= t/sqrt(L) [F4(q) cos(qx) cos(qy/2)-Fx(q)].

Here the normalized Bloch sum supplies R, while the original source normalization sqrt(V)=R sqrt(L), leaving 1/sqrt(L). The vertical formula follows by exchanging x and y. There is no extra factor of two from treating the ground and excited admixtures separately: they enter as the difference between the pair and vacuum diagonal source values, as in ordinary first-order eigenvector perturbation theory.

Expansion gives

    F4=1+(qx^2+qy^2)/8+O(|q|^4),
    F4 cos(qx) cos(qy/2)-Fx=-(L+2) qx^2/8+O(|q|^4).

Thus the two orientation amplitudes are respectively proportional to -qx^2 and -qy^2. For the lower symmetric Q4 orientation mode in |q| << lambda,

    A_low(q)=-J gamma (L+2)/(8 sqrt(2L)) lambda^L |q|^2 [1+o(1)],
    weight=J^2 gamma^2 (L+2)^2/(128L) lambda^(2L) |q|^4 [1+o(1)].

The energy convention and the chosen phases of the low branch fix the displayed amplitude sign; the weight is convention independent. The expression is transverse-isotropic to this order. It is not a statement about propagation in the longitudinal direction.

## Conservation, gauge connection, and uniform errors

H_0=H/sqrt(V) has exactly zero transition matrix element between different exact-energy eigenstates. Both leading coefficient kernels satisfy this cancellation individually after the correct ground rotation. This is a strong normalization/sign control.

For an off-diagonal canonical high-wall SW transformation, differentiating its source-dependent gauge produces a within-N0 connection. Real perturbations give a real antisymmetric connection, so its diagonal part vanishes. A nontrivial two-column matrix element first requires L physical insertions. Its commutator with the first nonconstant column energy (order lambda^4) therefore contributes no earlier than lambda^(L+4), not at the displayed order lambda^L. If a second, source-dependent flux-sector rotation is used, its connection must be kept or, equivalently, the source and eigenvectors must both be transformed consistently. The above calculation works in the unreduced N0 column basis with the explicit vacuum mixing.

An error merely stated as O(lambda^(L+2)) is NOT uniform relative to lambda^L q^2 on a growing box. To claim the asymptotic weight for q shrinking with lambda one needs:

1. The exact zero-q identity for the fully matched energy source, including higher-order ground rotations and gauge terms.
2. Inversion symmetry and smooth, bounded displacement moments of the effective source kernel in the local orientation basis. These make its even, vanishing-at-zero correction O(q^2), rather than using energy conservation alone, which would not forbid an odd linear term in a generic channel.
3. The low-branch eigenvector correction is controlled in |q| << lambda. Its orientation mixing error is O(q^2/lambda^2), giving a relative contribution of this order; direct analytic kernel corrections are relative O(lambda^2)+O(q^2) at fixed L.
4. The actual-H/projector/source remainder is o(J lambda^L q^2), after all volume and denominator losses. One may choose sufficiently high fixed normal-form order after choosing a fixed polynomial box exponent, but this comparison must be made explicitly. A uniform gap approximation alone is insufficient to establish the very small q^4 source weight.

The translation eigenstate/fibre convention must also be the same as in the established pole theorem. Allowed momenta permit unwrapped local centers across periodic bonds: shifting the local cluster by a full period changes the total phase by one. Choosing wrapped centers inconsistently within a bond or plaquette would introduce spurious signs.

This is a derived native energy-density matrix element, not a derived gravitational coupling. Its exact uniform-energy darkness and q^2 amplitude are part of the result, rather than evidence of a constant universal scalar charge.
