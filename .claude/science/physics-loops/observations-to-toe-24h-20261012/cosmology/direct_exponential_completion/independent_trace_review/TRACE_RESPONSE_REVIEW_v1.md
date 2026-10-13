# Independent local trace-response check

The three stated matched-state identities are correct for the supplied regular limit, with tau_g denoting the source-normalized gas trace. No correction is needed. The physical-clock derivative is essential to the coefficient slope. This is a local action/readout check, not a review of the full conditional convergence theorem, a history integration, an observation fit or a formal audit.

## Scope and exact inputs

I froze and read the complete TRACE_RESPONSE_DERIVATION_v1.md, check_trace_response_v1.py, parent freeze, three result rows and execution record. I also read the complete REGULAR_LIMIT_DERIVATION_v1.md to establish the equations and derivative clock; its wider history theorem is being checked separately. The original exponential action note/runner are reused through their exact snapshots in the completed observation review. Their identities and both unchanged observation-review receipts are recorded in REUSED_ACTION_IDENTITIES_v1.json.

The trace note SHA256 is 36a24a90b66bd2882b0faa8617481cd706cff5c1dfcbaf33e921c9797a0395f7. The runner SHA256 isd7cd35fca383f75672cadb7dbf5f70bb998e1be774f949afb550a00cda818b87. The supplied regular-limit note SHA256 isfb5447dbd13fb5015a8f6b06f2ecb92a6e543028176df24e566defa8ef0a2afa. All three parent input hashes match their declared freeze. The parent's actual execution returned three exact symbolic zero residuals, exit 0 and empty stderr in 0.3665s. I did not import or execute that runner as independent evidence.

## Independent action and u-acceleration derivation

Let t=exp(-u), D=1+2(x^2+y^2)/3 and

    g=t diag(1/4,4/(9D),1/(3D)),
    W=3(1-t)^2/2+t^2(x^2/2+y^2/3+nu u^2/2).

At the chosen instant, u=p_u=0, p_x=-3x/2, p_y=-2y, sigma0=x^2+y^2 and B=1+2sigma0/3=D. Define Pi=R0 P_gas. The matter source is tau_total=sigma0-3Pi, while tau_g=y^2-3Pi excludes pressureless dust.

The independent route uses the lowered momentum equation

    (g_i p_i)'=-(3+h)g_i p_i
              +(1/2)sum_j(partial_i g_j)p_j^2
              -[W_i+delta_iu t tau_total/2]/B.

At p_u=0, converting this equation to p_u' gives the same lower connection contribution C_u=Tbar/2, because partial_u g_j=-g_j. Direct substitution yields

    B Tbar=x^2+4y^2/3,
    W_u=-x^2-2y^2/3,
    C_u+[W_u+tau_total/2]/B
       = [B Tbar/2-x^2-2y^2/3+(x^2+y^2-3Pi)/2]/B
       = tau_g/(2B).

Since g_u=1/4 and the friction term is proportional to p_u=0,

    p_u'=-2 tau_g/B.

The dust terms cancel because of this instantaneous matching. They have not been removed from the general matter coupling. The nu term and its first gradient vanish at u=0, so nu does not enter this local result. B>=1 for real x,y, including the zero-field point; no division by x or y is needed.

## Physical coefficient, its energy part and its clock part

The fixed-calibration action expansion is

    K=k g+O(k^2), U=3/2+k W+O(k^2),
    C_B=1+k(1-t)+O(k^2), alpha_B=k t/2+O(k^2),
    sigma=C_B^2 sigma0/(1+k)=sigma0[1+k(1-2t)]+O(k^2).

Expanding the full constraint and physical readout,

    Hhat^2=2(sigma+U)/(3-Kp^2),
    H_J^2/H_v^2=Hhat^2(1+alpha_B p_u)^2/C_B,

gives the supplied coefficient

    C_exp=2[W+sigma0(1-2t)]/(3B)+Tbar/3+t p_u-1+t.

Thus the term t p_u is fixed by the physical metric clock. It is not an adjustable kinetic normalization.

Contracting the regular field equations with velocities gives

    E=W+B Tbar/2,
    E'=-3B Tbar-(t/2)tau_total p_u.

The trace-work term vanishes at the specified instant. Jordan fluid conservation gives sigma0'=-3(sigma0+Pi). Therefore

    Delta=E-sigma0=0,
    Delta'=-3B Tbar+3(sigma0+Pi)=-tau_g.

It is useful to retain the full identity before differentiating:

    C_exp=2Delta/(3B)+4sigma0(1-t)/(3B)+t p_u-1+t.

At u=p_u=Delta=0, derivatives of the second and last terms vanish because t'=-t p_u=0; the denominator derivative multiplying Delta vanishes too. The derivative of t p_u equals p_u'. Consequently,

    C_exp=0,
    C_exp'=2Delta'/(3B)+p_u'=-8 tau_g/(3B).

Omitting the physical-clock term instead gives-2 tau_g/(3B), which is a factor of four smaller when the trace is nonzero. Neither that truncated expression nor the simplified matched-state formula should be applied at arbitrary later states.

## Units and interpretation

All source terms in these equations use the declared dimensionless normalization. x^2=R0 rho_dust and y^2=R0 rho_gas, and Pi=R0 P_gas use pressure and energy density in the same units. Thus

    tau_g=R0(rho_gas-3P_gas).

It is not the raw thermodynamic trace without R0. Written using the raw gas trace, the formulas are p_u'=-2R0(rho_gas-3P_gas)/B and C_exp'=-8R0(rho_gas-3P_gas)/(3B). Prime denotes dimensionless physical e-fold N_J in the limit, not proper time. No omitted H factor or derivative-clock conversion is required in these formulas.

A positive supplied massive-gas trace therefore produces negative initial u acceleration and negative initial physical coefficient slope. The latter affects the physical expansion at order k. A zero trace makes both vanish, consistently with the supplied ideal radiation orbit. These statements neither derive a gas distribution nor prove that the signs persist later. They do not imply finite-k convergence, attractor selection, a new observation or a microscopic origin of matter.

## Independent exact controls and omission sensitivity

The reviewer code uses Fraction arithmetic and forward directional differentiation, not the parent's symbolic matrix construction. It evolves lowered momenta, converts to accelerations and differentiates the complete C_exp as a first-order jet. Seven frozen rational fixtures include vacuum, dust only, ideal radiation, mixed ideal fluids, two positive-trace gases and one explicitly nonphysical negative-trace algebra fixture. Several have nonunit R0.

The first independent execution returned **69 pass, zero fail**, including the source/record identities. All physical identities in the seven fixtures are exact rational equalities. For x=3/5, y=4/5, Pi=1/10 and R0=13/10, tau_g=17/50 while the raw gas trace is 17/65. The independent values are

    p_u'=-51/125,
    C_exp'=-68/125,
    C_exp' without the clock term=-17/125.

The deliberate clock-omission calculation disagrees with the required physical slope in all three nonzero-trace fixtures. It is a reviewer-owned local negative control, not a replay or alteration of the author's runner. The complete exact values and all checks are retained in INDEPENDENT_RESULTS_v1.json. No actual failed reviewer computation occurred in this stage.

The parent serialized forms also agree: p_u'=-6tau_g/(3+2x^2+2y^2) and C_exp'=-8tau_g/(3+2x^2+2y^2). Its simultaneous substitution handles the matching correctly rather than differentiating a prematurely frozen zero-field coefficient.

## Disposition

SOURCE_DISPOSITION_v1.json records the exact six new source/recovery pairs and the reused action identities. FINAL_RECEIPT_v1.json binds this complete derivation/report, independent source, predeclared fixtures, execution, exact results and snapshots. Both observation-review receipts and all 143 evidence files bound by them were reverified unchanged. All writes were confined to independent_trace_review. No parent source, Git state, model setting, external chat or formal audit record was changed.
