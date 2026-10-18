# Physical original-source coefficient for the first winding process

Focused check of the source extension to `/tmp/neutral_whole_column_root.md` and recurrence in `/tmp/neutral_winding_source_probe.py`. The result below concerns a formal fixed-even-L coefficient, in the same native word-derived canonical gauge as the winding Hamiltonian.

## Denominator derivative and sign

For an intermediate flipped-rung subset S in the two columns, c(S) cyclic clusters cost 8J c(S). Let d2(S)=sum_z [1_S(z) xor 1_S(z+2)], counting the actual periodic distance-two bonds. In either column each mismatch changes ZZ by -2. There are two columns, so the original normalized source changes by -4 d2(S)/sqrt(V). Thus under the derivative device H+hC,

    Delta_S(h)=8J c(S)-4h d2(S)/sqrt(V).

The tunneling magnitude is the sum of positive path weights times product_(proper intermediate S) 1/Delta_S(h). Differentiating at h=0 gives

    gamma_L'(0)=gamma_L A_L/(2J sqrt(V)),

where A_L is the normalized weighted average over insertion orders of sum_S d2(S)/c(S). Since the Hamiltonian matrix element is -gamma_L, its derivative is negative:

    C_eff,offdiag^(L)=-gamma_L A_L/(2J sqrt(V)).

This has the correct units: gamma/J is dimensionless and C itself is dimensionless. No h-dependent perturbation is being retained physically; h is solely a derivative parameter for the existing observable at h=0.

## Recurrence

Writing F(S) for the denominator path sum and T(S) for its sum weighted by all previous d2/c insertions gives

    F(S)=sum_i F(S\i)/c(S),
    T(S)=sum_i T(S\i)/c(S)+(d2(S)/c(S))F(S).

There is no denominator for the final full subset. Dividing sum_i T(full\i) by the previous exact total path sum binom(2L-2,L-1) therefore gives A_L. The root script implements this correctly. A limited exact-rational replay gave A4=36/5, A6=40/3, A8=252/13, A10=432/17, A12=220/7. No all-L closed form is inferred from those values here. For L>4 the distance-two bond convention has no small-ring duplication issue; L4 is still a useful explicitly counted control.

## Effective-source connection

For a real canonical block diagonalization H_eff=P UHU†P and A=(partial_h U)U†,

    partial_h H_eff=C_eff+P[A,UHU†]P.

Once the Hamiltonian is block diagonal, the last term is [PAP,H_eff]. It must not generally be omitted. Here the native H and C are real matrices in the spin basis, including YY bonds, so the canonical unitary can be taken real orthogonal and PAP is real antisymmetric.

Every coefficient of PAP below order L in transverse insertions is diagonal within N=0 by the same whole-column flip count. A real antisymmetric diagonal matrix vanishes. Its first possible off-diagonal contribution is consequently order L. The zeroth-order N=0 Hamiltonian and the order-two correction are scalar; the first nonconstant diagonal contribution is order four. Hence the connection commutator cannot change the order-L off-diagonal source coefficient (its first potential contribution of this type is order L+4).

This is a formal word/local canonical-gauge statement at fixed L. An independently chosen nonlocal, h-dependent block rotation would invalidate the vanishing-connection argument as stated. The physical operator must then be transformed consistently; one cannot retain just its Hamiltonian derivative in such an arbitrary gauge.

## Independent virtual-dressing control

I additionally diagonalized the selected two-column winding subproblem, mapped to L logical rung spins:

    H_sub=-2J sum_z Z_z Z_(z+1)-J lambda sum_z X_z,
    C_sub=(2/sqrt(V))sum_z Z_z Z_(z+2).

This is a control of the minimal-path coefficient, not a replacement full native Hamiltonian. The even/odd global-X eigenstates give the real localized-basis source off-diagonal entry (C_even-C_odd)/2. It approaches the predicted coefficient directly from dressed eigenvectors:

- L4, lambda=.15,.10,.05: ratios .997179, .998748, .999687.
- L6, lambda=.15,.10,.05: ratios .997532, .998905, .999720.

Control files: `/private/tmp/neutral_winding_source_matrix_control.py` and `.json`. An initial scratch run used an integer Hamiltonian array and truncated the hopping; that operational mistake was fixed by casting to float before diagonalization. Only the corrected results above support the check.

## Scope

The nonzero coefficient is an off-diagonal observable matrix element in the aligned-column basis, not automatically an inelastic transition between eigenstates. In a pure isolated pair-tunneling doublet this source term is parallel to the tunneling Hamiltonian and is diagonal in its parity eigenbasis. Other diagonal energies and couplings matter for a spectral transition.

The derivative and virtual dressing therefore agree at the leading fixed-L winding order. They do not establish a uniformly dominant observable coefficient as L grows with lambda^(-p), a physical readout rate, or an exponentially long kinetic timescale.
