# Heavy-background rotation and assisted vertex

Disposition: PASS for the proposed gauge-covariant rotation. The free-outgoing-wave cancellation at rest is not an exact C4 selection rule of the interacting background problem. This does not prove a nonzero physical threshold scattering amplitude.

Let R map lattice sites by a positive quarter turn, and let P_R be its permutation matrix. In the singleton-over-background coordinates, put U_s=diag(s_i). Direct bondwise evaluation gives

 T_(Rs) = P_R U_s T_s U_s P_R^dagger,

where T_s has x-edge amplitude -1 and y-edge amplitude -s_i s_j. An old x edge becomes a new y edge, and conjugation supplies s_i s_j; an old y edge becomes a new x edge, and its two sign factors cancel. This is an exact identity, not a weak-flux approximation.

## Physical phase

Use spin rotation exp(-i pi Z/4) together with the spatial quarter turn. Its phase on a singleton at i relative to its aligned background is exp(i pi s_i/2)=i s_i. Thus the heavy coordinate map is i P_R U_s, times the overall background phase. A different orientation convention conjugates the common i but leaves the relative signs unchanged. For an even-height column pair complemented relative to the uniform background, the background rotation phase relative to the vacuum is exp(i pi L)=1. Hence no extra relative background sign offsets the displayed singleton factor in the present even-L route.

In particular, the physical quarter turn is not the site permutation alone on the final two-flipped-column background. U_s is -1 on those two columns. For compactly supported flips U_s equals identity outside the defect region, so the same covariance carries over to scattering states with correspondingly rotated asymptotic boundary conditions; it changes their values inside the scattering region.

## Vertex covariance

For a hop i to j which also complements those two columns, s'_i=-s_i and s'_j=-s_j. A matrix element transforms with the ratio of final and initial singleton phases s'_j/s_i=-s_i s_j. Therefore the x amplitude -a transforms to the y amplitude +a s_i s_j, exactly the supplied complementary vertex. Both the hopping Hamiltonian and this vertex use the same physical rotation.

For the uniform incoming background and flat heavy wave psi, choose an x-pair outgoing wave phi_x in its actual T_(s_x) problem. The rotated y-pair wave is phi_y=P_R U_(s_x) phi_x, after cancelling the common i phases against the incoming state. At the two flipped endpoints its values are minus the rotated x-wave values. Consequently

 <phi_y,V_y psi> = <phi_x,V_x psi>.

The + sign of the bare y vertex is canceled by the endpoint minus sign of the outgoing wave. The symmetry-even sum of these two correctly transformed channels therefore adds their amplitudes; symmetry does not force their cancellation. This statement concerns a rotated pair of full heavy/background channels, not a factorized choice of the same free heavy wave in every background.

Replacing both outgoing waves by the identical free wave gives the familiar factor cos(K_y)-cos(K_x), which vanishes at K=0. That is a valid matrix element for that specified free prepared final state. It is not the projection onto the actual C4-even scattering channel: the latter includes U_s. Nor is it an invariant conclusion under a change of background-dependent heavy coordinates unless states and vertex are transformed together.

## Remaining boundary

Absence of this symmetry-enforced zero is not proof that the exact scattering amplitude is nonzero. The actual flux scattering solution may suppress endpoint values or produce a dynamical zero. In the infinite two-dimensional lattice, K=0 is a band threshold; one must define the limit of normalized scattering states and examine threshold singularities rather than assume a normalizable free state there. A physical on-shell process also needs energy conservation in the full heavy-plus-environment channel. No relaxed-heavy ground state, emission rate, universal coupling, or full-H outgoing channel is established by this covariance calculation.

Independent R6 matrix check constructed T from physical signed bonds and the two complementary hop matrices. Hamiltonian covariance, vertex covariance, and amplitudes for an arbitrary complex outgoing test wave agree exactly (zero floating discrepancy). Artifacts: /tmp/neutral_heavy_rotation_reviewer.py and /tmp/neutral_heavy_rotation_reviewer.json. Inherited source read: NATIVE_PROBE_LOOP_PROOF.md and ALL_HEIGHT_ASSISTED_HOP_PROOF.md. No repository edits or formal audit.
