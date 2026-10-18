# Final focused review: mixing-induced vertex

Disposition: PASS for the present scoped native local matched vertex and separate pinned two-channel coefficient scattering statements. No demotion or blocking correction is required. This is not a formal audit. No repository source was modified.

Reviewed native/MIXING_INDUCED_VERTEX_PROOF.md, both executed helpers, docs/NATIVE_MIXING_INDUCED_VERTEX_NOTE_2026-10-18.md and scripts/native_mixing_induced_vertex.py in the scalar-environment worktree.

## Physical and native-coefficient bookkeeping

The anchor-dependent identification addresses the physical heavy plane sector rather than assuming one unchanged background character at every particle position. On flat signs s_xy=a_x b_y, W_j W_i cancels the vertical link sign. A pair away from the anchor commutes with the W_i strings and gives exactly the declared four changed vertical bonds. The proof expressly withholds a global identical-vertex momentum sum for anchor-crossing features.

The leading local matrix element is c times the heavy diagonal difference J lambda V_e. The background-only matrix element -J gamma lambda^L cancels c J Delta lambda^4. Thus the leading retained term is J(gamma/Delta)lambda^(L-3)V_e. Heavy diagonal corrections begin one lambda power later in this expression; direct background-changing heavy paths and occupied-column winding corrections are also later. The cancellation does not pretend to exhaust every order-L heavy term, and the canonical-frame/preparation dependence is explicitly stated.

The local b_e channel is a specified vacuum-rotated pair channel, not by itself the fully projected global bound pole. The proof correctly does not identify the displayed coefficient as a global q=0 pole charge.

## Exact rotation and threshold convention

For the bare constant background matrix [[0,-h],[-h,d_bare]], Q=[[cos(theta),-sin(theta)],[sin(theta),cos(theta)]] with tan(2theta)=2h/d_bare diagonalizes it. Rotating diag(0,V) gives diagonal potentials sin^2(theta)V and cos^2(theta)V and positive off-diagonal sin(theta)cos(theta)V. The off-diagonal coefficient is tied to the diagonal ones; it is not independently adjustable.

The exact gap after this rotation is d_gap=sqrt(d_bare^2+4h^2)=d_bare sqrt(1+4c^2), where c=h/d_bare. Section 5 explicitly reuses d for this diagonalized gap. The scattering helper consistently holds d_gap=.03 fixed while setting theta from c. An equivalent bare realization is d_bare=.03/sqrt(1+4c^2), h=c d_bare. Thus there is no numerical mismatch between the constant rotation and the two free thresholds. This explicit formula clarifies the factor mentioned in the prose.

The exact T matrix W(I+G W)^-1 has the correct sign for G=(L0-E-i0)^-1. Its first-order off-diagonal limit is V(I+G_f^+ V)^-1, with the correct distorted outgoing bra. The first-order-in-c limit is separated from the threshold limit. The statement does not claim uniform all-orders control as c,d,E simultaneously follow native lambda scales.

## Reproduction

I executed both helpers directly; their internal assertions and the runner-level conditions passed. The largest rotation-block error was 3.87e-18. The Duhamel matrix difference was 2.68e-16, and the exact fourth trace difference was -64. The last threshold row had relative error 3.331e-7 against 1/(g_f-g_c). The exact two-channel relative Born errors were 0.00176445, 0.000196515 and 0.0000176911 at c=.03,.01,.003, consistent with the stated O(c^2) behavior at fixed positive channel energies.

These rows test the finite-g formula and the fixed-energy small-c limit. The scaled threshold value at E_f=1e-7 is still approximately 10.767-1.851i rather than its real limiting value 4pi; logarithmic convergence is slow. Neither the runner nor proof incorrectly requires that last row to equal the limiting constant. The infinitesimal regulator is numerical corroboration, not proof of the outgoing boundary limit.

The finite-matrix rotation and Duhamel helper use R=7 as a representation control, not as a physical even-R selected-sector proof. This is harmless for their stated matrix identities; no native plane-sector claim is extracted from that control.

## Scope

The current public note and proof consistently distinguish the native fixed-volume matched coefficient from the separate pinned scattering diagnostic. They retain physical-plane strings, all pair channels, recoil, relaxed preparation and uniform remainder control as open. They do not infer a full microscopic rate, universal charge, cosmological scalar or observed interaction. The analytic native coefficient cancellation depends on the inherited canonical reduction, and is not independently established merely by the small matrix rotation control.
