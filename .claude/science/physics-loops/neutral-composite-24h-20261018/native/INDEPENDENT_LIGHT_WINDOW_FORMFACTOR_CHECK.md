# Momentum-resolved fixed-box light window: independent check

Disposition: PASS for the momentum extension, using the previously checked fixed-box winding coefficient and ground-mixing construction. Read /tmp/neutral_light_window_root.md. No shared/canonical edits.

For an edge along axis a with center r_e, the two column positions are r_e+/-e_a/2. At Qz=0 each intermediate rung subset changes the original midpoint diagnostic by -2d2(S) per column, so

 Delta C_Q(S)=-4d2(S)exp(-iQ.r_e)cos(Qa/2)/sqrt(V).

Thus the minimal winding derivative equals its uniform-source coefficient multiplied by exp(-iQ.r_e)cos(Qa/2). There is no missing longitudinal phase at Qz=0. One can obtain this complex Fourier coefficient by linear combination of real local-source derivatives, without introducing a non-Hermitian physical perturbation.

The flipped two-column domino has four bad plaquette centers at offsets +/-e_a +/-e_b/2 from r_e. Their Fourier sum is

 4exp(-iQ.r_e)cos(Qa)cos(Qb/2).

Combining this with the original square-source vertex factor cos(Qa/2)cos(Qb/2) gives the static domino excess

 [3Delta4/(Jz sqrt(V))]exp(-iQ.r_e)
 cos(Qa/2)cos(Qa)cos^2(Qb/2).

The offsets +/-1 along the domino and +/-1/2 across it are the reason cos(Qa), rather than another cos(Qa/2), appears in the bracket.

The excited-versus-ground source difference must be subtracted through the leading ground mixing K_edge/Delta4. Therefore the effective transition coefficient is exactly

 -gamma_L/(Jz sqrt(V)) exp(-iQ.r_e)cos(Qa/2)
 [A_L/2-3cos(Qa)cos^2(Qb/2)]

to the stated leading order. The subtraction sign agrees with the previously checked (b-a)K result at zero momentum. Higher source/energy terms alter it by an absolute O(lambda^(L+1)) at fixed R,L.

Different edge images are orthogonal on the entire P0 space: P0 X_edge X_edge' P0 vanishes for distinct edges because their difference flips at most four columns, fewer than the minimum nontrivial P0 pattern weight R. Thus arbitrary complex edge phases introduce no interference terms between edges, even for a coherent exact-ground direction. There are R^2 edges of each orientation. With V=R^2 L,

 W_Q=gamma_L^2/(Jz^2 L) sum_(a=x,y)
 cos^2(Qa/2)[A_L/2-3cos(Qa)cos^2(Qb/2)]^2
 +O(lambda^(2L+1)).

The error is absolute, uniform over the finite allowed momentum mesh at fixed geometry. At Q=0 the sum gives 2(A_L/2-3)^2, reproducing the uniform-source weight. At (pi,pi,0) both leading edge factors vanish; no relative asymptotic is justified there. The quoted absolute error remains safe (and is not intended as a sharp next nonzero order).

For nonzero allowed Qz the low window is exactly dark for sufficiently small lambda: actual ground and the whole low-energy subspace have longitudinal momentum zero by the wall-gap argument. This exact selection rule is stronger than a leading winding cancellation. At Qz=0 the source mean need not be assumed zero in a general ground superposition; centering has no effect on the separated excited spectral window.

These formulas concern the original readout's momentum form factor of a fixed-box spectral-window weight. They do not describe a momentum-dependent energy branch, a propagating scalar mode, an isolated pole, or a uniform growing-L asymptotic. The stated winding/source gauge and fixed-geometry hypotheses remain necessary.
