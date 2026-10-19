<!-- Original PR9802 source SHA256 183252680d46d693ddfeda501bbbb0add8450851b424c1e8730d9ab9d0c0cddb. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Focused check: vacuum-rotation vertex in pinned coefficient scattering

The proposed distorted-wave Born form factor, order of matrices and threshold coefficient are correct with the specified outgoing-resolvent convention. The result is first order in c for the stated two-channel pinned-background model; it does not transfer by itself to the full native neutral pole or a relaxed on-shell emission process.

## Channel convention and finite-rank form factor

Let H00=L0, Hee=L0+V+d, and H_e0=cV with c real. At conserved total energy E, the outgoing channel's kinetic energy is Ef=E-d>0. Write G_f^+=(L0-Ef-i0)^-1. A final distorted bra with the conventional minus scattering label is

<psi_e^-(k')| = <phi_k'| (I+V G_f^+)^-1.

Indeed its ket uses the conjugate incoming boundary value, and taking its adjoint yields the displayed outgoing Green function. Therefore

M/c = <phi_k'| (I+V G_f^+)^-1 V |phi_k>
    = <phi_k'| V(I+G_f^+ V)^-1 |phi_k>.

The last identity is the finite-rank push-through identity and does not presume that V commutes with G. Only the six defect sites enter this expression. The parent orientation and matrix ordering are correct. Using a plus ket as the final state and then conjugating without adjusting the scattering label would give the conjugate convention instead.

## Threshold limit

For the fixed six-site restriction, G_f^+=g_f 11^T-A+o(1), where g_f=(log(32/Ef))/(4pi)+i/4+o(1). Put C=I-AV and s=1^T V C^-1 1. The exact constant-vector rank-one reduction is

1^T V(C+g_f 1 1^T V)^-1 1
 =s/(1+g_f s)=1/(g_f-g_c),  g_c=-1/s.

Here s=-4(8p-3)/(8p^2-1), p=1/pi. Numerically s=-9.57651142015213 and

g_c=(pi^2-8)/(12pi^2-32pi)=0.1044221591900022.

Consequently

log(1/Ef) (M/c) -> 4pi.

This is not the endpoint source u0+u1 from the previous calculation. It sums V u over all six sites against the final incident wave; its numerator and limiting coefficient therefore differ. In particular it still vanishes logarithmically before multiplication by the logarithm; the value 4pi is not a finite unsuppressed threshold amplitude.

For E and Ef tending to zero with 0<d/E<1 fixed, both incident vectors restricted to these sites approach 1, with corrections O(sqrt(E)) and O(sqrt(Ef)). The full six-site inverse is bounded for large Re g_f, as checked previously. Fixed-distance potential-kernel corrections are O(Ef log(1/Ef)). These yield o(1/log(1/Ef)) corrections to the form factor, so the leading coefficient is unaffected by the two directions or centered phase conventions. Uniformity over a compact subinterval of 0<d/E<1 follows from the same estimates. Endpoint regimes require their own bounds.

## Energy-overlap identity

Formally, the two separate channel eigen-equations imply

<psi_e^-|V|phi_k>=(Ef-E)<psi_e^-|phi_k>.

The bra is an eigenstate of L0+V and the ket of L0, not of one common Hamiltonian. Their overlap is not forced to vanish by orthogonality. These are generalized scattering states; the overlap contains a singular energy-denominator contribution. At nonzero E-Ef=d its off-shell part scales inversely with that difference, so multiplication by -d need not give zero. With wavepacket regularization the same conclusion follows without multiplying ill-defined pointwise distributions. Taking d to zero before handling that singular overlap is invalid.

The full two-channel model conserves total E: the final threshold offset d accounts for the kinetic energy loss. This identity says nothing about the full native recoil, momentum-conserving neutral dispersion or competing connected vertices.

## Limits of the statement

The specified off-diagonal cV is the local rotation-induced vertex in the supplied coefficient model. The analysis computes its first-order distorted-wave transition element; it does not establish a uniform all-orders expansion in c at arbitrarily small energies. If c and d are tied to lambda, the simultaneous-limit error control must still be stated for any claim beyond this leading coefficient. A transition rate additionally needs normalization, channel densities and a physical scattering/preparation model. None is inferred here.
