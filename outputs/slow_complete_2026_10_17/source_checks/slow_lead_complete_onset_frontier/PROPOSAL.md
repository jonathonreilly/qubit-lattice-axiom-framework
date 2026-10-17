# Quantitative complete-state onset: emitter closure and a background derivative frontier

Status: authored conditional derivation requiring a distinct check. A concrete quantitative bound is proved below for the represented IN-BAND full emitter component. For the other finite coordinates and closed tails, a real-energy integration-by-parts formula reduces the missing quantitative onset to an explicit background inverse/forced-column derivative certificate. That certificate has not been numerically or analytically bounded by a supplied number here. Consequently this proposal does NOT claim a new actual-device complete-state onset, even though it specifies sufficient inequalities and a useful conditional scale. No parameter choice or requested accuracy is optimized.

## Sources, exposure and scope

The current fixed device has kappa=1e-8, g=1e-6 and h=4e-6. Family statements use the positive domain of uniform composition, with gamma=kappa^2/j, d=2j sin h, H=d/gamma>=100, L=g/gamma and H/L<=.024. Here H denotes the dimensionless band ratio when it is a scalar, and H_device the physical Hamiltonian. The old source, correlated calibration and .0027<j<.003 are fixed. Firstslow m=0 and the old finite gate port are distinct. Literal c_att, K and W and all prepared old/reference directions remain as in the pinned synthesis.

Read/reused complete fixed synthesis ab552c4002af8388d5e223cf81390cdcbaa74685affda5c263048cbea73cdb2a/checkc6d82eaf1e4789f6b4f6b6f5c0fe97a0201fce1dbe7e99b294995d76e516a628; uniform synthesis8cd26edcb7941d8254494480455d17c137652ec779e37e78901de5a04e71ac9e/checkb873ac37d8a327f27491f36e80dfe5e8aeef7eb0d7b405bba6b70a6ffb9e71a7; fixed emitter53916c906eda8cd5a1c8c6228c54002f4f74fe7986bee301d3162124d40544c0/check23c228886a96e29071beabf5e3ae1f6c9caee8544eee4e5b5ddc38f854fda707; recoveryf0f39510b65133d8399720c53ce2822bfe60a378ab2e50e1773a3dc8d0fe880f/check488d0a9e8871f77f40d44803ee9bfe7fda25388c66b367944eea3376f51f5195; uniform endpointc8d2b7681f2059ec986bc3e41bf0a3eea8fefbc43c86addc17539b2f258bb887/checkf3e449109bc4bac6b4e4692d0db5f40c4d282d663b32f3b89a7ff1065ded28e0; uniform reference5f2026dc3f63a757f13cf58bc468f05de10cfca9f04fda9c6615b816c9b94907/check338e554834f994741982842c555589db5e62dba9ad121233989ce60068f26c93. These are sibling PROPOSAL.md and corresponding _check/REVIEW.md paths. Fixed scalar referencee6a9706d497d7c6abb5590d2baae0940efdf628e81101f5f4cfd91885e93ea8e/rootcheck6fb89d66d0a79e5c66c6dabd00c030ddb603308485f60c857b95f0e791b1a5f5 and general resources84b76d1ec9b1e45811b74ecd2594a0622dfb01ef69d1acadf98931c0ed3f9967/checkdd944d8803da24fdfbccfd010e2fd865196aa08ac244605303093a605fef22fe retain their previously read scope.

I authored the fixed emitter, fixed scalar reference and fixed synthesis, and checked uniform reference/composition; this is not an independent check of those ancestors. Root exposed the missing oscillatory cancellation, separately suggested a finite-background inverse route and emphasized the full emitter/output distinction. Their suggestions are disclosed, not substituted for proof. No solver, sweep, scientific runner, delegation, W/Git/PR/checkpoint, model or prompt change occurred. The sole deliverable is this proposal. Original complete inverse/calibration premises remain conditional.

## 1. Decomposition and the single omitted state

Use the same physical union I=I_1 union I_3 for EVERY input and both record-X sectors, I_b=c_att+b+2j+[-d,d]. The represented evolution is U_I(t)=exp(-itH_device)E(I)V. The full four-input seed theorem gives

    ||U(t)-U_I(t)||<=epsilon_sp,
    epsilon_sp=sqrt(min(1,1-p0+2eta)).                   (1)

At the fixed parameters epsilon_sp<.00129 and eta<2.8e-7 per window. This omitted STATE amplitude is charged once at the end. In particular, the small emitter estimate below is for U_I, not the entire actual full8 emitter output. A prepared-emitter compression may have an outside mass estimate, but that cannot silently replace the square-root outside bound for complementary full8 output rows.

The represented unprojected state splits into full emitter output, other finite coordinates plus complete closed tails, outgoing open rays and incoming open rays. In each parity the emitter output has eight internal coordinates while prepared input has two; neither is compressed away. Both record sectors are retained. Finite coordinates are orthogonal to one another, but closed/open projections vary between physical windows, so window errors are added. The ideal comparator remains T1(t)=exp(-it c_att)Jout[beta_t tensor exp(-itK)W], with raw norm r(t). None of the following estimates commutes K through the interacting source.

## 2. A quantitative full-emitter bound without an actual-source derivative

Let T_s(E) be the actual full8 emitter inverse in a record sector and Tref(E) the full8 reference inverse with one j-chain per B eigenvalue. Its prepared-vacuum columns only have literal old-energy shifts b=1,3; the six excited-source directions per parity are mathematical comparison channels. The existing pointwise matrix bound and both-lip Stone jump imply a norm-integrated full emitter density error<=eta per window, including all complementary output rows. Two physical windows therefore cost2eta. This does not rely merely on the prepared-to-prepared density compression: the antecedent resolvent comparison was a full8 matrix bound.

The exact scalar reference emitter density, with delta measured from its own center2j, is

    rho_ref(delta)=gamma sqrt(1-delta^2/(4j^2)) /
       [pi((1-gamma/j)delta^2+gamma^2)], |delta|<2j,

and zero outside. Set a=1-gamma/j>0 and ell(delta)=gamma/[pi(delta^2+gamma^2)] on the entire real line. With s=sqrt(1-delta^2/(4j^2)),

    |rho_ref-ell|
      <=ell[(1-s)/a+(gamma/j)/a], |delta|<2j.

This follows by separating the numerator change from the denominator ratio; the latter is at most1/a. Also1-s<=delta^2/(4j^2), and

    integral_(|delta|<2j) delta^2 ell(delta) ddelta
                               <=4j gamma/pi,
    integral_(|delta|>=2j) ell(delta) ddelta<=gamma/(pi j).

Thus the FULL-LINE L1 distance is at most

    (gamma/j)[(1+1/pi)/a+1/pi]<2gamma/j.                 (2)

The last relaxed inequality holds throughout the supplied domain gamma/j<1.4e-11. Since the Fourier transform of ell is exp(-gamma|t|), the full reference return amplitude is bounded by exp(-gamma t)+2gamma/j for t>=0. Removing its own hard-band complement adds at most1-p0 in amplitude, because this is a positive scalar spectral measure. Orthogonal ideal old channels combine by maximum, not by summing four copies.

Consequently the represented full emitter component obeys

    E_I(t):=||P_em U_I(t)||
       <=exp(-gamma t)+2gamma/j+(1-p0)+2eta.            (3)

At the fixed parameters and t>=1e15, gamma t>100/3,1-p0<1.1e-6,2eta<5.6e-7 and2gamma/j<2.8e-11. Hence E_I(t)<1.661e-6. This is a concrete quantitative represented-emitter result, not a claim that the complete emitter amplitude lacks an omitted-state contribution. No source complex strip or derivative was used. The common energy shifts multiply the scalar return by phases of unit modulus.

## 3. Remove the actual emitter denominator before differentiating recovery

Let L_s(E) recover every nonemitter finite coordinate and every closed slow tail from endpoint forcing, with the actual slow load already included. The checked absolute bound is ||L_s||<L0=4e5 on both lips. Its full background seed column is -kappa L_s T_s. Replace only T_s by the exact Tref while keeping L_s ACTUAL:

    -kappa L_s T_s=-kappa L_s Tref
                            -kappa L_s(T_s-Tref).

The same full8 resolvent comparison and both lips bound the represented replacement error by

    B_replace<=2 kappa L0 eta.                         (4)

At the fixed point this is<2.24e-9. This is an in-band background-column comparison, not an extra omitted seed charge. All complementary reference denominators and wrong-window prepared columns remain present. No smallness of L_s itself beyond L0 is assumed.

Suppose, as an explicit additional quantitative certificate, that the actual Hilbert-space-valued recovery is continuously differentiable on each CLOSED energy window and both lips, with

    sup ||dL_s/dE||<=M1.                               (5)

The known local analytic inverse/root continuations ensure such a finite supremum exists for each fixed positive triple, but existing notes give no numerical M1. Its value is therefore an open obligation, not an established constant in this proposal.

For Tref, the direct scalar branch formulas give ||Tref||<=1.01/r_delta and the safe bound ||Tref'||<=2/r_delta^2, r_delta=sqrt(delta^2+gamma^2). For the selected entry, Dref'=1+gamma i exp(iq)/(2j sin q), |Dref|>.9999r_delta, so this derivative ceiling has ample slack. For every complementary reference channel, its continuum is separated by the inherited gap>.162; its surface Green derivative is bounded by1/.162^2, its emitter inverse by6, and differentiation gives an O(37) ceiling, far below2/r_delta^2 on these windows. This pays the full8 extension, not only its resonant diagonal.

Integrate EACH boundary column L_s Tref by parts in REAL energy. With r_d=sqrt(d^2+gamma^2), two endpoint terms, the derivative product and BOTH Stone lips give, after adding both windows,

    B_I(t)<=2 kappa L0 eta
      +2kappa/(pi t) [2.02L0/r_d
                 +2.02M1 asinh(H)+4L0 atan(H)/gamma],
    t>0.                                               (6)

The factor1/pi per window is from two lips of an unprojected sector, not the record1 half-difference. Different sectors combine by the norm of their orthogonal direct sum with seed weights1/sqrt2, preserving the same ceiling. Equation(6) includes the hard energy-cutoff boundary terms; smoothing them away would change the problem. It is a quantitative statement conditional on(5), not qualitative Riemann–Lebesgue presented as a rate.

A coarse direct L1 background bound remains available without(5): per window it is2*1.03*kappa L0 asinh(H)/pi, hence twice that on the union. One can take the minimum of this and(6) when M1 is certified. It does not control the emitter by itself, which is why(3) is separate.

## 4. Exact finite-background matrix obligation and closed-tail derivative

There is a concrete matrix whose certificate would settle(5). In one record-X sector and old parity, remove the emitter and eliminate only the infinite slow ray. The remaining finite background has235 heads times the full8 internal fiber. Let

    M_s(E)=E I-H_finite,s-Sigma_s(E),
    R_s(E)=M_s(E)^-1,
    F_s(E)=R_s(E)V_endpoint.

Physical scalar shifts can be retained in E or removed consistently. Sigma acts only on the old gate output port and equals -j times the diagonal slow-root matrix there. This finite background is NOT the emitter Schur inverse T_s and does not contain its gamma resonance denominator. F_s recovers the finite part of L_s; its norm is already<L0. The complete finite matching arguments imply invertibility on the chosen windows, but a numerical norm for the ENTIRE R_s, on arbitrary forcing at every head, is not supplied by the endpoint column bound.

Define Bstar=sup_(s,b,E in I_b)||R_s(E)||. For the open root v=exp(ik), |dv/dE|=1/(2g sin k)<=1/(1.99g). Closed roots give smaller derivatives by the fixed gap. Therefore

    ||M_s'(E)||<=S1:=1+j/(1.99g),
    F_s'=-R_s M_s' F_s,
    ||F_s'||<=Bstar S1 L0.                            (7)

This forced-column estimate is stronger than blindly using Bstar^2 S1: it retains the already proved L0 bound on the actual endpoint-forcing column. A direct certificate for R_s M_s' F_s would improve it further. The slow energy derivative1/g is explicit, not omitted.

The infinite closed-tail lift also has an explicit derivative. For a closed root v with |v|<r_c=1/160000 and gap Delta_c>.162, its tail from the gate-port amplitude has entries sqrt(j/g)v^(m+1), m>=0. Differentiating the root equation yields

    |v'|=|v|^2/[g(1-|v|^2)],
    ||tail'||<=sqrt(j/g)|v'| sqrt(1+|v|^2)
                                      /(1-|v|^2)^(3/2).

Using |v|<=2g/.162 bounds this by

    4sqrt(jg)/.162^2 *sqrt(1+r_c^2)/(1-r_c^2)^(5/2)<.009.

Its undifferentiated norm is<.00068. These are diagonal B-channel blocks, so seven closed channels combine by maximum, not seven times the constant. Their spectral projectors are fixed in each window. Applying the product rule to the gate-port column and combining finite and closed-tail ranges by a safe triangle bound gives the sufficient certificate

    M1 <=1.00068 Bstar S1 L0+.009 L0.                   (8)

This proves that the closed infinite range itself is not an unspecified differentiation obstacle. The remaining task is a NUMBER for Bstar or for the smaller forced derivative. Existing selected/open scattering margins, endpoint Green norm and ||L_s|| do not by themselves bound the entire inverse: other forcing directions can be large. Nor does a real-band value bound imply a derivative bound. One must inspect the full finite matching inverse or an exact factorization for this derivative, including the original source and converter blocks.

At the fixed g, S1<1510, so (8) gives M1<6.05e8 Bstar+3600. The illustrative sufficient inequality M1<=1e17 would follow, for example, from a suitably verified Bstar<=1.65e8. Neither inequality is asserted to hold. Larger certified inverse constants would still give a finite but potentially enormous onset through(6); no practical time claim follows from mere finiteness.

## 5. Actual incoming wave: what is quantitative now and what a decay rate needs

The actual incoming coefficient matrices differ from the ideal incoming reference by the same complete-input Eout as the outgoing matrices, including wrong-window columns. Therefore, without any derivative obligation,

    ||incoming_actual(t)||<=Iin+Eout, t>=0.             (9)

At the fixed point Iin<.0016 and Eout<.000041, so the actual incoming contribution is<.001641 for EVERY nonnegative time. This is an actual two-lip coefficient consequence, not a scalar estimate silently substituted for the physical wave. It is not a decay-to-zero rate.

An explicit real-momentum derivative route is available but may be very loose near the narrow resonance. On one physical window write the full incoming matrix coefficient A(k) (including its actual phase and all input columns). Let v=min E_s'(k)>0, a=max|E_s''(k)|, and define

    C_A=[||A(k_-)||+||A(k_+)||
                 +integral||A'||dk+(a/v)integral||A||dk]/sqrt(2pi).

Integration by parts for phase -km-tE_s(k), whose derivative magnitude is m+tE_s'(k), gives amplitude norm<=C_A/(m+vt). For m>=0 and t>0, summing yields

    ||incoming_window(t)||
        <=C_A sqrt((vt)^-2+(vt)^-1).                   (10)

Add the two window bounds, take the maximum over parity, and preserve orthogonal record-sector averaging. The endpoints are paid and m=0 is included. The formula remains an operator bound after passive-reference tensoring. Its hypotheses require an explicit integrable derivative bound for the ACTUAL coefficient A, not the scalar contour alone. Such a certificate has not been extracted here. Even a valid bound can be poor when it differentiates the resonance without cancellation; it should be compared with(9), not advertised as automatically useful at the fixed onset.

To approach the sharper asymptotic ceiling at a controlled time, one needs a sharper incoming bound that actually decays, such as a proved actual-source contour or a derivative/factorization estimate avoiding the large resonant variation. The known auxiliary scalar contour is legitimate only for its scalar coefficient and cannot establish an interacting-source strip. The existing qualitative L2 propagation argument proves no quantitative constant in(10).

## 6. Complete-state consequence and useful conditional scale

Combine the SAME one omitted state, emitter, background, outgoing error and incoming estimate. For the unnormalized complete comparator,

    ||U(t)-T1(t)||
       <=epsilon_sp+E_I(t)+B_I(t)+Eout+J_actual(t),     (11)

where J_actual may be (9), or any independently certified improved bound such as the full aggregated(10). For a normalized comparator add1-r(t), provided r(t)>0. The scalar outgoing concentration curve supplies an explicit r(t) lower bound and is used ONLY for that reference normalization. To transfer to a finite device through absolute horizon2T, add the existing exact full-state cut error D_M(T); no square root of a branch error is taken.

For orientation only, retain the current fixed parameters and assume the still-UNVERIFIED derivative certificate M1<=1e17. At t>=1e15, use asinh H<15, gamma>1/(3e13), d>2.15e-8, pi>3.14 and atan H<pi/2 in(6). The resonant derivative term is<.000480, the cutoff term<2.4e-10, the M1 term<.0000193 and the replacement error<2.24e-9. A safe conditional ceiling is B_I<.000501. With(3),(9), epsilon_sp<.00129 and Eout<.000041,

    complete raw error <.00129+.000001661+.000501
                                      +.000041+.001641 <.003475.

For the fixed scalar onset,1-r(t)<1.6e-6, so normalized complete error would be<.003477. At M=5e9 and t in[1e15,2e15], adding the proved finite-transfer allowance<1e-6 would give<.003478. These are IMPLICATIONS of the additional derivative certificate, not new actual-device conclusions. They illustrate why replacing T before differentiating L could remove the loose .083 square-root branch cost without needing the sharper .001332 asymptotic ceiling at the same time.

No new target has been selected and no bound on M1 or Bstar was fabricated. The unconditional new quantitative progress is the represented full-emitter estimate(3), the actual incoming ceiling(9), the small replacement error(4), and exact sufficient derivative/onset inequalities(6)–(11). The unresolved load-bearing number is the full background inverse or forced derivative in(7)–(8); a sharper incoming rate is additionally needed to approach the asymptotic floor. These are explicit finite-matrix/column tasks, not a claim that quantitative complete onset is impossible.

## Limits

All claims concern the exact supplied static Hamiltonian and seeded one-head sector with arbitrary old/reference input. The actual omitted amplitude is never paid as a small mass on unrestricted complementary output rows. Both record sectors, both physical windows, literal common phase and old aging, wrong-window inputs and every finite/closed output are retained. Native preparation, coefficient supply/tolerance, readout and physical units remain premises. No repeated-measurement, permanent halt, reset/reuse, new actual runtime or publication claim is made. The new Lorentzian comparison and derivative interface require a distinct check before composition into a theorem.
