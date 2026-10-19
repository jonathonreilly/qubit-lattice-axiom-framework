# A local dressed witness for the actual mediated product seed

Status: new ROOT conditional author calculation, requiring independent checking. This bounds outside-window mass in the attached apparatus without assuming a global spectral gap or transferring an isolated-cell spectral projector. It does not prove represented propagation, a pulse shape, a complete-output theorem or permanent halt.

Assume the three-mediator stationary proposal2972451d with the required corrected port convention: remove the existing positive j n_p cap from H_bg, install the new path and occupations, and thereby restore exactly that cap on compression. The uncorrected literal addition to H_bg is not a premise. Assume further its shared B acts identically on every mediator/source coordinate and the prepared old input subspaces satisfy B iota_e=e iota_e for e=1,3. No unexpected source/internal contact acts on the witness below. These are supplied installation and preparation hypotheses.

Let V_e place the head at s0 with the prescribed otherwise blank/record0 apparatus and old input iota_e. Write E_e=c_att+2j+e, and A1 for the positive-weight adjacency of ONLY the first 2n1 mediator sites between s0 and s1. C_L embeds into its first internal endpoint. Define the physical linear map into these actual internal coordinates

    X_e=-gamma1 A1^-1 C_L iota_e,
    Y_e=V_e+X_e,
    c1=gamma1^2 d_(n1),
    d_n=J^-2 sum_(l=0)^(n-1)(q/J)^(2l).

The inverse exists because J>q. The bipartite inverse identities imply

    X_e^* X_e=c1 I_e, V_e^*X_e=0,
    (H-E_e)Y_e=t1 |s1> iota_e,
    t1=(-1)^(n1-1)gamma1^2 q^(n1-1)/J^n1.

The second equality is a full physical-vector identity, not a stationary effective equation. To check it, the internal rows are -gamma1 C_L iota_e-A1 X_e=0; the s0 row receives gamma1^2 (A1^-1)_(1,1)=0; the s1 row receives the opposite-end entry t1. Every other head amplitude is zero. In particular chain2, chain3 and the attached processor do not act on this witness because s1,s2,p and all their adjacent occupied-head inputs vanish. The unchanged shared B cancels E_e on both components. The port-cap correction is still required for the apparatus definition, even though this witness has zero amplitude there.

Thus W_e=Y_e/sqrt(1+c1) is an isometry on the old input sector and

    ||(H-E_e)W_e||=|t1|/sqrt(1+c1),
    ||V_e-W_e||=delta_p,
    delta_p=sqrt(2[1-1/sqrt(1+c1)]) <= sqrt(c1).

Different e sectors and passive reference inputs preserve the scalar Gram identities, since A1 acts only on head coordinates and the prepared internal vectors are orthogonal. Therefore W=sum_e W_e is an isometry and ||V-W||=delta_p; the difference cost needs no sqrt(2).

Let I be the union of the two physical intervals centered at E_1,E_3, each of halfwidth d>0, and E_H(I^c) the ACTUAL full-H spectral projection. For each e, every energy in I^c has distance at least d from E_e. The spectral theorem yields

    ||E_H(I^c) W_e|| <= |t1|/[d sqrt(1+c1)].

No assumption of orthogonality of the two omitted output images is made. Cauchy-Schwarz over the two orthogonal INPUT sectors gives

    ||E_H(I^c) V||
       <= delta_p + sqrt(2)|t1|/[d sqrt(1+c1)]
       <= sqrt(c1) + sqrt(2)|t1|/d.                 (1)

This includes all omitted spectral types, trapped modes and passive references. It uses no claim that [H,B]=0 globally, and no gap in the attached background. The head graph may be finite or infinite provided the displayed local vectors are in the self-adjoint H domain; finite-support vectors suffice for the supplied bounded finite-range installation.

For n1=2m-1 and the nominal bandcenter definition lambda_m=sqrt(3)t1, (1) reads delta_p+sqrt(2/3)lambda_m/[d sqrt(1+c1)]. With fixed gamma1,J,q, c1 increases to gamma1^2/(J^2-q^2). Thus this particular preparation certificate retains a nonzero upper allowance controlled by the supplied ratio gamma1/sqrt(J^2-q^2), even as lambda_m decreases. A nonzero upper allowance is not a lower bound or an impossibility result. It does not show the actual omitted mass is that large.

The witness W is only a proof device. The actual initial condition stays the product seed V; no correlated preparation protocol or free dressed input is assumed. Its difference from V is charged once before spectral projection. This bound does not establish mass or regularity inside I, the altered source pulse, absence of loaded poles, physical phase, mediator vacancy at output or receiver convergence. Those remain separate load-bearing steps. The old sixth-moment formula is neither used nor claimed applicable.

Exposure: ROOT derived this local witness after reading the stationary mediator source2972451d and isolated-cell source836caee, and after receiving the distinct review's port-cap correction. ROOT also proposed the prior integer-length ratios. This is not an independent check of those premises. No scientific execution, numerical spectrum, solver, parameter optimization, canonical publication or editable prompt/axiom change occurred.
