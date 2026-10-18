# Exact collision-sensitive original-readout identity

The identity and the proposed native collision matrix element are correct, with an explicit physical-boundary qualification.

Because all longitudinal Z operators commute, let w_z=(1-Z_z Z_(z+1))/2. Then the exact operator identity on each distance-two bond is

Z_z Z_(z+2)-1=(1-2w_z)(1-2w_(z+1))-1
             =-2w_z-2w_(z+1)+4w_z w_(z+1).

Summing over complete longitudinal bonds on the infinite lattice with finitely many flipped spins, or on a periodic lattice with the corresponding sums, gives

C_excess=-4N+4A,
N=sum_(c,z) w_(c,z), A=sum_(c,z) w_(c,z)w_(c,z+1).

This is an operator identity in the computational basis algebra, not an expectation-value approximation. A direct enumeration of all 256 eight-spin finite-flip configurations with up exterior verifies it exactly.

For a finite open column with spins1,...,L and only internal distance-two readout bonds, the two edge wall variables occur once rather than twice. The exact formula is instead

C_excess=-4N+4A+2(w_1+w_(L-1))

per column, with N summed over its L-1 internal nearest bonds and A over consecutive such bonds. The simpler formula therefore requires up exterior included in the readout, periodic sums, or no walls on these physical boundary bonds. This is unrelated to a feature's internal endpoint: internal endpoints are already counted exactly by N and A.

## Meaning of A and the collision example

A counts adjacent longitudinal wall pairs. Such a pair is an isolated spin relative to its two neighbors: it can be a singleton down domain in up background or a singleton up gap between down domains. It is not restricted to one of those cases.

Four separated finite intervals each contribute two walls, so N=8. When all four have length at least two and no one-site intervening gaps, A=0 and C_excess=-32. Four singleton down spins in separate columns have A=4, so C_excess=-16.

Start with four down intervals and take two neighboring columns whose final two down layers coincide. Flip the two spins at one common endpoint, shortening each interval from length two to one. Each column still has two walls, hence total N=8 is unchanged. Each new singleton adds one adjacent-wall pair: Delta A=2 and Delta C=8. The remaining two columns may remain long.

The native transverse XX bond contributes -Jx to this transition. For a y bond the two flipped spins are both down, so YY acting on them has product phase -1 and the Hamiltonian -Jy YY contributes +Jy. Both are nonzero when their coupling is nonzero. The reverse extension has the same Hamiltonian amplitude and opposite Delta C. Thus this is an explicit nonzero wall-preserving first-order matrix element in the full collision sector, not a hypothetical source term.

## Commutator and scope

Within a fixed-N coefficient sector, [N,K1]=0, so the identity reduces the source commutator to

[C_excess,K1]=4[A,K1].

For the displayed transition, <f|[C,K1]|i>=8<f|K1|i>. This proves the original bare uniform readout is not constant on the full collision sector and is sensitive to adjacent-wall contacts. It corrects any extension of the long-height-space darkness statement beyond its stated interval-length domain.

For the full microscopic Hamiltonian, [N,H] need not vanish; the exact identity instead gives [C,H]=-4[N,H]+4[A,H], with boundary terms if present. One must not silently use the projected commutator identity for unrestricted H.

A nonzero commutator demonstrates nonconservation and the existence of off-diagonal matrix elements in some energy basis; it does not specify which states are occupied, prove a particular spectral line, determine a residue, or show that a candidate bound channel is visible. Those require the collision-sector eigenstates and the original readout matrix elements in them. No added coupling, scattering theorem, detector identification, or cosmological implication is asserted.
