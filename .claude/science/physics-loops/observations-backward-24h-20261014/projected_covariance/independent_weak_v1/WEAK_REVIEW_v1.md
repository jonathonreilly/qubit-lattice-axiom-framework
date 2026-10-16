# Independent projected weak-form check

The primary compact-interior-support weak kernels are correct under the supplied geometry and differentiable signal premises. The original finite-regularity alternative needed a boundary qualification: vanishing through radial derivative six does not remove the time flux at moving radial limits. An exact counterexample confirms this. The complete v1-to-v2 change now restricts that alternative to a fixed interior rectangle and explicitly retains or removes the moving-boundary flux separately. That repair is sufficient and changes no kernel or source equation.

This is a focused independent mathematical/implementation check, not an empirical test, formal audit or full validation of the projected-covariance construction. Root remains the author. No author CHECK source or output has been opened. All writes are confined to `projected_covariance/independent_weak_v1`.

## Read versions and independence

I read both complete author arguments and the needed M14 source equations. Exact identities are:

| Source | SHA256 |
|---|---|
| WORKING_v1.md | `641a730694795f2e18af4b57e3083f82bd62f4a89902ac0dbc25aab1dd33d92d` |
| WEAK_FORM_v1.md | `5b7f5e9ede7e845067dc5f90b4fdca629fb912520fce29a5ca74b884ca30a381` |
| M14 canonical note | `592df22cbc7421da970842b42157129ba65e8f0c71d6928ca90fa189474702ce` |
| WEAK_FORM_v2.md | `30a62389ff52fcc0ddbf48f096a448d12219b32d892677bf1e59e7724a841b76` |

The author mathematical notes were intentionally exposed before the check; the independent claim concerns rederivation and separate implementation, not blind discovery of the proposed formula. `PRECHECK_v1.md` and the control implementation were frozen before execution. Results were frozen before opening the changed WEAK_FORM_v2 text. The result freeze SHA256 is `4fa99dbeaef06dbf1e700186e65d8aaf2f65f284bd6cc86c64a2946f621a3325`. The complete v2 diff changes only the finite-boundary paragraph; every kernel, geometric identity, error-bound equation and empirical qualification is unchanged.

## Derivation and separate control

With measure dN dr and fixed-r time derivatives, the M14 covariance residual is

    R=.5 f_N−y j_N+.5 y² l_N−a0 f−(c0−a0y)j+c0y l,

where f=C_SS, j=C_SV and l=C_VV. Coefficients depend only on N. The independent radial integration gives D*w=−(w/r)_r, K*w=−K w−w and E*w=−alpha r w_r−(alpha+1)w. Order reverses, so L*=E*E*P* and Q*=D*L*. The operator Q has radial order seven.

Differentiating U=E D l first gives E²D l_N=E U_N−g(E+1)U. Time integration therefore yields precisely the three stated kernels. The observation multipliers 2aHchi/r² and a²H² stay outside those time derivatives because the differentiated variables were d and U. The y-history derivative and the explicit geometry correction are necessary. P and E cannot be commuted.

My implementation builds Q by a generic Leibniz coefficient-composition rule and computes its adjoint from the resulting coefficients. It separately evaluates the proposed factored adjoints and raw cross/radial-velocity Hessian map. It then exactly integrates the full forward and weak residuals, rather than evaluating author check code.

The frozen fixture uses chi=3/(1+N), a=exp(N), H=exp(−N)(1+N)²/3, and nonconstant x,y,m. The geometry obeys chi_N=−1/(aH); h and g also vary. The fixed domain is 0≤N≤1, 1≤r≤2, strictly inside 0<r<2chi. Its weight is N²(1−N)²(1+N)²r²(r−1)^8(2−r)^8. Polynomial arguments with radial degrees above the annihilator's null modes make the identity nonvacuous. Forward and weak integrals equal exactly

    −1890902253015923142474461377159 / 3541262891210765725958553600000.

All 25 exact controls pass. Negative controls give nonzero defects when the geometry correction or coefficient-history derivatives are omitted, when adjoint ordering is swapped, or when a fixed-angle derivative replaces the fixed-separation derivative. A direct angular-coordinate chain-rule control confirms the stated conversion. A separate time-endpoint control verifies the omitted endpoint term and shows it need not vanish for a noncompact time weight. These are algebraic test functions, not claimed PSD physical covariance ensembles, full background solutions or measured inputs.

## Boundary finding and repair

On moving bounds, the extra time flux is minus the upper-bound speed times

    .5 Q*w C_SS−y L*w d+.5 y² E*P*w U,

plus the corresponding lower-bound term. Vanishing w and its first six radial derivatives kills the seventh-order radial boundary terms but can leave Q*w nonzero in this flux.

For rlo=1, rhi=2+N/10 and w=N²(1−N)²(r−1)^7(rhi−r)^7, all six required radial derivatives vanish and the time endpoints vanish. Yet at the upper boundary

    Q*w = 7! N²(1−N)²(rhi−1)^7 rhi^9/(16chi^4)>0.

Choose C_SS=1 and d=U=0. The projected pointwise residual is zero because Q kills constants. The boundary-free weak expression instead equals the positive exact flux

    4989883216143779891748313 / 137241000000000000000000.

The independent direct integration agrees exactly with that flux. This is a real domain counterexample to an unrestricted moving-boundary interpretation of the v1 alternative, not a defect in the primary smooth compact-support theorem. The v2 fixed-rectangle restriction removes it; for moving bounds the separately required full flux condition or stronger derivative-seven vanishing is sufficient. No boundary condition on the physical potential is added.

## Preserved implementation failure and empirical limits

The first independent implementation stopped before writing a result because its ordinary-polynomial antiderivative could not accept the r^-2 term in the moving-boundary adjoint. Original source, empty stdout and full stderr are preserved. Version 2 extends only that integrator to exact Laurent monomials down to r^-2, refusing unexpected logarithmic terms. No fixture, weight, coefficient, identity or expected zero/nonzero condition changed. The successful result is `INDEPENDENT_WEAK_RESULTS_v2.json`; this is not a relabeled v1 pass.

A weak adjoint does not supply the continuum source-distance shear inversion, the two-source covariance's equal-epoch limit, homogeneous/isotropic signal separation, calibrated velocity/distance fields, masking corrections or an error model. For finite windows the target functional must be represented by their span on the admitted signal space, or further justified restrictions must remove its null space. The simple exact mean-bin example has zero response to N−1/2 but the N-weighted target sees 1/12, illustrating why interpolation alone is insufficient. The supplied |delta C_i| envelopes would imply the stated integral absolute-kernel error bound, but this check supplies neither those envelopes nor stability. High derivatives can amplify errors substantially.

I have not independently established nonzero-rank physical ensembles for the entire new projected construction, run full rolling projected trajectories, checked any survey likelihood or examined the author's CHECK implementation. Those are distinct obligations. The action, realized history, absolute scale and measurement supplier remain conditional. No further mathematical discrepancy was found within the stated weak-form scope after the v2 boundary repair.
