# Pre-control derivation

Let C=S(S+1), Q=1+sum_links |E|. Use zero-extended normalized spin shifts
on the full rotor word space. Each difference U_S^sign-U^sign has coefficient
at most E(E+sign)/C in magnitude for integer E, including the cutoff exterior.
Thus its weighted norm against Q^-2 is at most2/C. A product of two actual
hops differs by at most10 Q-squared/C because one hop changes Q by at most1.

The exact one-hole block formula for Hbar_S=H2_S-Delta_S has diagonal row
budget684 and offdiagonal budget60. Block Schur with Q commuting with the
hole projectors should give ||(Hbar_S-H_rot)Q^-2||<=7440/C. The diagonal
Delta_S is positive and at most2Q-squared/C, since each oriented A-B link
occurs once and its occupancy gate is at most1. This retains its extensive
operator norm; it is only relatively small on the weighted input domain.
Use the harmless larger constant10000/C for the full H difference.
Actual marked-map and loss differences should obey
||(J_S-J_rot)Q^-2||<=8/C and ||(G_S-G_rot)Q^-2||<=24/C,
with J the original direct sum, separately for resolved/coherent instruments.
These constants and the common-space extension need proof and controls.

The rotor weighted bound is already checked:
||Q² Z_rot(t)psi||<=C_k exp(-gamma_k t)R2(t)||Q²psi||,
R2=1+8bt+4b²t², b=5C_k delta M. Its L1 and L2 time norms are finite with
constants independent of volume in the stated fixed-k rotor domain.

Set A_S=-i delta H2_S-kappa G_S/2 and K_S=sqrt(kappa)J_S. Each no-event
semigroup is contractive, including the potentially unbounded diagonal
Delta_S, and its terminal-survival plus first-event amplitude map V_S,T
is an isometry. Duhamel expresses the no-event difference as an integral
of spin propagations driven by (A_S-A_rot)Z_rot(s)psi. The same injected
vector propagated from s to T has total terminal-plus-output norm at most
its input norm by the loss identity. Minkowski therefore bounds the whole
instrument-amplitude difference by

 integral_0^T ||(A_S-A_rot)Z_rot(s)psi|| ds
 + [integral_0^T ||(K_S-K_rot)Z_rot(s)psi||² ds]^(1/2).

The first term includes terminal survival and every original future mark;
the second is the direct output-map change. An integral of the perturbed
survival tail itself is not needed. Weighted rotor decay makes this bound
O(C^-1)||Q²psi|| uniformly over T. The resulting cq output trace distance
is at most twice the amplitude difference, extends with ancillas by the
same operator estimates, and with mixed states by a purification and
sqrt(Tr Q^4 rho). Dephasing time/marks or finite bins is contractive.

If correct, spin survival limsup at infinite time is at most the square
of this O(C^-1) amplitude error, since rotor survival vanishes. This is
source-weighted approximate absorption, not a positive unweighted spin
gap or a waiting-time moment. Arbitrarily long tails with small mass are
not ruled out. For moving input families, require Tr Q^4 rho=o(C²) for
convergence, or a fixed weighted bound for the stated O(S^-2) rate.

On infinite Z3 the diagonal Delta_S is defined as a nonnegative multiplication
operator; D(Q²) is contained in its domain. Hbar_S is bounded self-adjoint,
so the sum and bounded loss define the contractive semigroup. Duhamel on
rotor graph-domain vectors is justified by Q² continuity and the relative
bound, then density. The physical spin box is invariant. These are proposed
proof steps, not yet independently checked new results.
