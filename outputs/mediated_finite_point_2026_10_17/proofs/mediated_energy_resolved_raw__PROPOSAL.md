# Energy-resolved L2 loading for the mediated raw packet

Status: new conditional author refinement requiring a distinct check. This gives an alternative explicit selected-input raw coefficient bound, preserving the exact reference phase and physical seed mass of the checked raw interface26392923. It changes no hardware or reference packet and proves no improved runtime or operating point. It is separate from the pending milestone and does not modify the checked raw source.

## 1. Unchanged domain and notation

Retain every corrected installation, mass-tuned family, physical matching and strict finite gate of loaded5f909e1e/checkf6303bb3 and raw26392923/check111aaeff. In particular lambda>0, rho<=min(d_bg,a/2), rho/g<=1/2, eta<1, k_C>0 and zeta<1 on both physical lips and both old-energy windows. Fixed supplied coefficients and physical mass factors Z0,Z1,Z2 are unchanged. Let

    R=sqrt(delta²+lambda²), s=sqrt(1-3lambda/j),
    kappa=sqrt(3jlambda), c_a=2sqrt(2)/3,
    H=6/[s(1-zeta)], tau=gamma3²/b_gap,
    b_mix=kappa(1+theta3)e_tilde tau,
    K_p=(I-S_p G)^(-1), S_p=s3(D).

All quantities below are nonnegative ceilings evaluated for that SAME finite m and rho. The original reference is

    v20=(S_crit^-1)_20=c_a lambda²/q_crit,
    z_ref=(-1)^(m-1)kappa v20 P/sqrt(Z0),
    |q_crit|>=s R³.                                      (1)

No stronger actual determinant estimate is assumed. Actual forcing remains z=K_p t3(D)psi_s2 in that order. The physical selected hopping is (-1)^(m-1)sqrt(Z2)kappa r3(delta), so its sqrt(Z2) cancels the physical left source2 mass only. The right seed factor1/sqrt(Z0) remains.

## 2. Explicit pointwise numerator

Import the checked pulse-bridge2ad7f593/checkb7b8697b ENERGY-RESOLVED numerator, not its integrated local bound. For self-contained evaluation its constants are

    A_err=1/[(1-eta0)(1-eta)],
    B_err=A_err² tau²/k_C,
    nu=gamma3²/[a(a-rho)], sigma=max(nu rho,tau),
    D_3=Gamma2/[a³(a-rho)], Gamma2=sum_l gamma_l²,
    H12=(2m-1)/a² * (1-rho²/a²)^(-2m),
    H3=m/a² * (1-rho²/a²)^(-m-1),
    H_hop=sqrt(3)H12+3(2+theta3)H3,
    Jfac=3j(1+theta3)²,
    C0=A_err a0+B_err a0²,
    C1=nu/[j²(1-nu rho/j)]+A_err b0+2B_err a0 b0,
    C2=B_err b0².

Here a0=8e-18 and b0=46000/.0053+290/g are retained, not set to zero. Define

    d0=lambda Jfac C0,
    d1=delta_m+lambda Jfac C1,
    d2=lambda H_hop+lambda Jfac C2,
    d3=D_3,
    Dpol(x)=d0+d1 x+d2 x²+d3 x³.

The checked ordered port/complement reduction gives

    ||DeltaF(delta)||<=Dpol(|delta|),
    ||F^-1-S_crit^-1||
             <=36 Dpol(|delta|)/[s²(1-zeta)R²].          (2)

The direct complementary source feedback is included in B_err. Formula(2) is an inverse-subtraction estimate, not a claim that the full physical source inverse commutes with D. Its restriction to the selected source2 row cannot increase the norm.

## 3. Ordered port action and selected forcing

The exact decomposition is

    z-z_ref=K_p[t3 psi_s2-z_ref]+(K_p-I)z_ref.          (3)

For selected prepared input, split its pre-port selected difference into r3 times the inverse difference and (r3−1) times the reference v20. The quadratic mean-value bound gives

    0<=r3−1<=H3 delta², r3<=1+theta3.

The complementary physical source2 output remains bounded by H b_mix/[k_C sqrt(Z0)R]. It is multiplied by tau, not by kappa. The selected action of the port perturbation is bounded pointwise by

    ||S_p G P||<=nu|delta|/j+sigma(a0+b0|delta|),
    ||(K_p-I)P||<=[nu|delta|/j+sigma(a0+b0|delta|)]/(1-eta).

This follows from G0P=m_j(delta)P, |m_j|=1/j and K_p-I=K_p S_p G. No factor is reversed or commuted.

Set

    A_F=36(1+theta3)/[s²(1-zeta)],
    e0=sigma a0, e1=nu/j+sigma b0,
    C_C=H(1+theta3)e_tilde tau²/k_C.

Substituting these into(3), and keeping the exact reference v20 where it matters, gives

    ||z-z_ref|| <= kappa/[sqrt(Z0)(1-eta)] * {
       A_F Dpol(|delta|)/R²
       +(e0+e1|delta|+H3 delta²)|v20|
       +C_C/R }.                                      (4)

The complementary term follows because tau H b_mix/(k_C kappa)=C_C. It retains the same coarse full complementary response as the checked raw theorem. Equation(4) applies on each physical lip separately. It neither assumes a zero complementary jump nor substitutes an adjoint for a rectangular boundary column.

## 4. Explicit L2 integral and replacement loading bound

All the following integrals are on[-rho,rho]. Define positive scalar moments

    I_n=int delta^(2n)/(delta²+lambda²)² ddelta, n=0,1,2,3,
    J_n=int delta^(2n)/(delta²+lambda²)³ ddelta, n=0,1,2,
    K=int 1/(delta²+lambda²) ddelta.

Minkowski, |v20|<=c_a lambda²/(sR³), and(4) give the usable bound

    E_load,ER =461 sqrt(j/pi) kappa/[sqrt(Z0)(1-eta)] * {
       A_F sum_(n=0)^3 d_n sqrt(I_n)
       +(c_a lambda²/s)[e0 sqrt(J_0)+e1 sqrt(J_1)+H3 sqrt(J_2)]
       +C_C sqrt(K) }.                                (5)

This is already a finite explicit expression; the following closed elementary ceilings eliminate quadrature entirely:

    I_0<=pi/(2lambda³), I_1<=pi/(2lambda),
    I_2<=2rho, I_3<=2rho³/3,
    J_0<=3pi/(8lambda^5), J_1<=pi/(8lambda³),
    J_2<=3pi/(8lambda), K<=pi/lambda.                  (6)

The first two I and all J bounds follow by extending their nonnegative integrands to the full line and scaling delta=lambda u. The rational full-line integrals are respectively pi/2,pi/2,3pi/8,pi/8,3pi/8. For I2 and I3, delta^4/R^4<=1 and delta^6/R^4<=delta² give the displayed finite-interval bounds. Extending those last two to the full line would diverge; the retained rho dependence is essential.

For a tighter finite-interval evaluation, put Atn=atan(rho/lambda), D=rho²+lambda². Exact formulas are

    K=2Atn/lambda,
    I0=rho/(lambda² D)+Atn/lambda³,
    I1=Atn/lambda-rho/D,
    I2=2rho-3lambda Atn+lambda²rho/D,
    I3=2rho³/3-4lambda²rho+5lambda³Atn-lambda^4 rho/D,
    J0=rho/(2lambda² D²)+3I0/(4lambda²),
    J1=I0-lambda² J0,
    J2=K-2lambda² I0+lambda^4 J0.                    (7)

These follow from the integral of R^-2, the standard differentiated recurrence for R^-4,R^-6, and polynomial division. The integral definitions ensure nonnegativity even if subtractive formulas are inconvenient for numerical arithmetic. Either(6) or(7) suffices; no numerical evaluation or sweep is part of this proposal.

The factor461 is the actual full-fiber preconnector row ceiling, applied to z-z_ref BEFORE Fourier conversion. The exact flux/Jacobian identity is

    int ||F_A(k)||² dk
       =int |t_f|² E'_q ||A(delta)||² ddelta/(2pi)
       <=(j/pi)int ||A(delta)||² ddelta.

This supplies the prefactor in(5); no leftover slow group-velocity factor is missing. The reference critical measure is used only for the separate row mismatch, never as the actual mediated seed measure. No term in(5) comes from a local Stone L1 bound masquerading as an outgoing L2 estimate.

## 5. Full raw interface, unchanged errors and precise scope

Keep the checked row term

    E_row=[2.1e-13 sqrt(p_rho)
       +(304/(2j cos h)+.302/g)lambda/sqrt(3)]/sqrt(Z0).

For a replacement selected allowance use E_sel,ER=E_load,ER+E_row. Because(5) and the old E_load bound have the same target and domain, one may instead take their minimum. This avoids claiming that a Minkowski refinement is numerically better at every finite tuple.

Complementary PREPARED inputs remain governed by the checked formulas

    U=tau/[k_C(1-eta)],
    V=H/(1-eta)*(b_mix/k_C)
                  [kappa(1+theta3)+tau b_mix/k_C],
    E_wrong,one=461 sqrt(j/pi)
                  [U sqrt(2rho)+V sqrt(pi/lambda)].

The direct U term is retained. This proposal makes no new cancellation or jump claim for K_C. Therefore a complete-input raw outgoing allowance is

    E_raw,ER=sqrt(2)E_sel,ER+2E_wrong,one.              (8)

The two selected input errors are combined by Cauchy-Schwarz and the two wrong-window errors by triangle. Conserved parity and record-X sectors combine with the existing normalized input weights; arbitrary passive references preserve the norms. Under the actual real assembled matching/regularity, the same bound applies to the incoming coefficient, with W-star at the same positive time. A later complete synthesis still pays BOTH raw discrepancies, hence2E_raw,ER.

The raw reference remains(-1)^m F_rho/sqrt(Z0), with its exact phase61.5q+.5k+172k_old and complex critical denominator. Its full-line norm is sqrt(p_rho/Z0), not one. There is no changed packet, fitted phase or divided-away physical seed mass. Physical-halfline normalization, actual outside state, source/mediator/background recovery and time-onset estimates are unchanged separate obligations when composing a complete statement. This source selects no such time or resource count.

## 6. Structural behavior, not an operating certificate

For fixed suppliers, gap and background with eventual rho=sqrt(a lambda), the strict margins stay bounded and H_hop,H3=O(m). The terms of(5) have transparent sufficient scalings using(6):

- d0 yields an O(C0) loading allowance, retaining the calibration floor.
- d1 yields O(delta_m+lambda C1), which decreases at fixed supplier.
- d2 yields O(lambda^(3/2) sqrt(rho) [H_hop+Jfac C2]).
- d3 yields O(sqrt(lambda) rho^(3/2) D_3).
- Sharp reference port terms yield O(e0), O(lambda e1) and O(lambda² H3), respectively.
- The retained complementary term yields O(C_C), which need not vanish with the inherited a0 ceiling.

Fixed j,Z0 and inverse-margin factors are suppressed only in this paragraph's asymptotic notation, not in(5). With rho=sqrt(a lambda), the d2 and d3 contributions vanish as O(lambda^(7/4)m) and O(lambda^(5/4)) at fixed gap. The mass discrepancy is O(lambda). These statements identify what is gained by retaining the actual energy numerator and exact v20 instead of a uniform zeta/R envelope. They do not eliminate all calibration allowances or prove a desired finite-m improvement. If the gap, g or supplier tuple varies with m, these scalings require new uniform bounds.

No stronger determinant conditioning, actual source regularity, source-time pulse or practical runtime has been derived here. A numerical complete certificate would require explicit finite-gate checks, this new lemma's distinct review, and re-evaluation of ALL other unchanged terms. It cannot be inferred from one smaller loading term or from asymptotic notation. This work is not part of the preceding frozen milestone packet.

## 7. Exposure and exact premises

The exact raw source and its full-input/phase proof were refreshed, as was the complete pointwise numerator portion of the checked pulse bridge. Their full proofs and checks were read in the immediately preceding coherent tasks. Exact unchanged pins:

- `mediated_raw_traveling/PROPOSAL.md`:263929233b06c4466535452e95f3a05ecfd6ab1a1046938bbac57322c2870f97; check111aaeff2a9839c028d2cf203c4cb5d324cca3ffcec2b0d7f127be9bc8732186.
- `mediated_pulse_bridge_plan/PROPOSAL.md`:2ad7f5936ab6044d180fe16ddf96f954a077f81f9d3e760df64ee373689b9e36; own checkb7b8697bbda3746ba98373562cbb9648bb8bc65d378887bcd4b56fe16d4f13cc.
- `mediated_loaded_inverse_interface/PROPOSAL.md`:5f909e1ea897e9aaef31dd362e42fc60d5ba0b5f595d28bd12f1d000d8552a22; own checkf6303bb308a56b0db39cf66b673e40174be775e7a32a71f28a6e489beb3990c3.

Root suggested retaining this numerator in L2 and using the exact prepared reference column for the port and hopping-variation terms. These were proposed routes, not accepted constants. I authored recovery/geometry/scalar ancestors and checked the local pulse bridge and loaded inverse; this is new source-exposed author derivation requiring distinct checking. No checked raw file, W/Git/PR/checkpoint/prompt/model setting was changed, no numerical integration, dynamics, parameter point or sweep was executed, and no delegation occurred. Only this proposal was written.
