# A faithful covariant density encoding on two record-pair Hilbert spaces

**Status:** proposed constructive escape at the preparation-map level; exact
author control and independent check pending. Raw research. Date:2026-09-22.

The single-pair cubic-moment result fixes U(R)=1 direct-sum R. A larger
operator space can retain the lost moment. The construction here uses two
such pairs with V(R)=U(R) tensor U(R), dimension16. It introduces no
quantum generator and does not change the record framework or formation law.

For a0=e1 and b0=(1,1,1), let H_A,H_B be their stabilizers in the24 proper
signed coordinate permutations. They have4 and3 elements. Choose the
following fixed integer vectors, indexed i=0,...,15:

    v_A(i)=(7i^2+3i+5) mod17 -8,
    v_B(i)=(11i^3+4i+1) mod19 -9.

Define the integer positive matrices

    S_A=I16+sum_(g in H_A) V(g)v_A v_A^T V(g)^T,
    S_B=I16+sum_(g in H_B) V(g)v_B v_B^T V(g)^T.

For any color a in the corresponding orbit, choose g with g a0=a or
g b0=a and set rho_a=V(g)S_orbit V(g)^T / Tr S_orbit. Stabilizer
invariance makes this independent of the chosen g. Every rho is strictly
positive, normalized and covariant; its minimum eigenvalue is at least
1/Tr S_orbit. All336 rotation/color identities are checked exactly.

The accompanying exact rational calculation assembles the14 matrices as
columns in the256-dimensional operator space. It checks column rank14,
equivalently affine rank13 for their differences from rho_0. Consequently

    p -> sum_a p_a rho_a

is injective on the full fourteen-probability simplex. It retains every
color moment, including the cubic w. The proof of this finite existence
statement is the explicit construction and exact rational rank calculation;
it does not invoke a generic-randomness argument or numerical rank tolerance.

There is room for this escape: the alternating-character multiplicity in
End(V) is7, from (1/24)sum_R a(R)|Tr V(R)|^2. The Hilbert representation V
itself has multiplicity0 for that character. The distinction matters:
a faithful mixed-density encoding does not imply fourteen orthogonal color
states or perfect readout of individual labels. The explicit cubic density
operator is nonzero and transforms by the alternating character.

This resolves only injectivity and covariance of a proposed preparation
map on a larger block. It does not provide a completely positive evolution
realizing the classical conditional rates, a local immutable-record
implementation, preservation under geometry changes, preparation by births,
or a positive quantum field dynamics. The full-rank encoded states overlap,
so conditioning an operation on the classical color cannot be assumed
physically implementable. Those are the next compatibility tests. No larger
block or additional framework primitive has been adopted.
