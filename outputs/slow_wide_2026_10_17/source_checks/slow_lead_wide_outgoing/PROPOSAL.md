# Wider receiver: complete-input actual outgoing coefficient

Status: new conditional real-band coefficient derivation requiring a distinct check. With the corrected wider gate and checked wider endpoint/emitter, the actual outgoing coefficient differs from the exact transmitted scalar reference by the parameter-dependent complete-input Eout in(12) below. No scalar contour constant, actual-source continuation, runtime, finite success or publication result is claimed.

## Domain, exposure and exact reference planes

Keep the supplied source/calibration, original converters, input cap, cable, gate, diagonal2j emitter and same-center slow connector. Assume .0027<j<.003, 0<kappa<=1e-8, 0<g<=1e-6, 0<h<=4e-6, d=2j sin h, gamma=kappa^2/j, H=d/gamma>=100 and d/g<=.5. Thus L=g/gamma>=200. On each physical window I_b=c_att+b+2j+[-d,d], b=1,3, define delta=-2j cos q, u=|q-pi/2|<=h and slow k by delta=-2g cos k. The same two-window union is used for every prepared input and both record sectors.

The corrected gate source5b667173 and its completed distinct check9c32a1c9, and endpoint sourcec4c99408 with completed distinct checkc6cc2ed7, are the new conditional inputs. I authored those two sources, not their checks; I read both checks completely. I refreshed the complete older outgoing argument only for its exact row/Schur/normalization identities. Its narrow constants are not transferred. Root requested this changed interface. This is exposed author derivation, not independent checking or original source recalibration. The wide scalar sourcec2d7a0cb is under separate check; this argument uses only the explicit measure identities reproduced below, not its temporal conclusions.

No sweep, numerical integration, scientific execution, model change, delegation, W/Git/PR/checkpoint, prompt or frozen-source edit occurred. Exact identities appear at the end. All original coefficient, source-inverse and physical identification premises remain conditional.

## 1. Actual complete output row

Write x=+1,-1 for record-X sectors. The original equal-j gate entries are t_x,r_o,x; the scalar slow interface coefficients at the SAME old output port are r_L and PHYSICAL t_L. Let

    d_gate,x=1-r_o,x r_L,
    d_src,x=1-S_eff,x r_x,
    rho_R=-i w^22, rho_att=w^18 rho_R rho_n=-i w^40 rho_n,
    w=exp(iq), rho_n=zeta exp[i172k_old(q)].

The physical first slow site is distinct from the old gate port. The exact selected output row for the full endpoint-forcing fiber is

    L_phys,x=t_L L_tilde,x,
    L_tilde,x=w^18(t_x/d_gate,x)d_src,x^-1 B_eff,x.    (1)

Every shown gate/source denominator is a scalar on the selected outgoing row; upstream matrix order is otherwise retained. Closed backreaction is already inside S_eff and B_eff. No extra cable phase belongs inside the gate-interface feedback.

The checked new margins are |d_gate|>.999983, |d_src|>.8709 and

    |t_x/d_gate-x rho_R|<=38u,
    |r_x|<.129, |r_x|<=33u+.262|delta|/g,
    |S_eff-S_PP|<8e-47, |S_PP|=1.

The unchanged upstream row is

    P B_e=-(t_new/j)w^21/(1+R_new w^42) P+E_L,
    ||E_L||<1e-23, ||B_eff-P B_e||<2e-48,
    |R_new|<r0=1e-20+12u<4.81e-5,
    |t_new-rho_n omega|<1.76e-13+1e-20+181u,
    |t_new|<=1.

Here omega is the literal W eigenvalue. It is not fitted to the changed lead. The gate numerator error38u and source transmission181u add before denominator division. The combined source/input denominator has modulus>.8709*(1-r0)>.8708. Its difference from1 is at most

    r0+(1+r0)(1+8e-47)|r_x|.

Therefore the numerator slope is at most219+12+33*1.000049<264.002 in u and .262*1.000049<.262013 in |delta|/g. Division by.8708 gives the safe complete row comparison

    j||L_tilde,x+(x rho_att omega/j)w^21 P||
       <e_N:=2.1e-13+304u+.302|delta|/g.             (2)

The positive floor1.76e-13 and the source reflection floor1e-20 are both paid; the E_L and closed corrections fit in the displayed2.1e-13 ceiling. The38u gate estimate already includes d_gate, so it is not divided by that denominator again in the scalar comparison.

For complementary rows and absolute forcing use both actual denominators in(1). Their product is>.999983*.8709. The unchanged complementary numerator E_L plus the closed correction then gives

    ||L_tilde,C||<2e-23,
    ||L_tilde,j||<460.                              (3)

These are full complementary-row norms, including the opposite prepared vacuum input.

## 2. Emitter correction with energy-resolved conditioning

Use the checked new full8 emitter blocks. In particular

    ||Dcc^-1||<6, ||G_PC||,||G_CP||<1e-23,
    Im D_x>189kappa^2,
    |D_x|>.9955r_delta, r_delta=sqrt(delta^2+gamma^2),
    |D_x-Dref|<kappa^2(a+b(g)|delta|),
    a=8e-18, b(g)=46000/.0053+290/g,
    Dref=delta+gamma w.

The8e-18 floor is the checked original calibration/source allowance, not an adjustable phase. The full modulus bound uses H>=100, hence L>=200; the weaker imaginary margin remains separately necessary below.

The exact selected output coefficient before the final physical connector is

    A_tilde,x=-kappa[L_tilde,j
                  +kappa^2 L_tilde,C Dcc^-1 G_Cj]/D_x,
    A_ref=kappa rho_att w^21/(jDref).                (4)

The complementary numerator costs less than j*kappa^2*(2e-23)*6*(1e-23)<1e-60 relative to the unit reference numerator. It is retained explicitly. Since

    |Dref|^2=(1-kappa^2/j^2)delta^2+gamma^2<=r_delta^2,

combining(2)–(4) gives the pointwise selected relative error

    |A_tilde,x/A_ref-x omega|
       <[e_N+1e-60+kappa^2(a+b(g)|delta|)/r_delta]
                                                          /.9955. (5)

This uses energy-resolved emitter modulus conditioning. Replacing the denominator error by its worst-band ratio to the imaginary part would lose useful information. Conversely the modulus estimate is not being used as a substitute for the positive imaginary margin in the wrong-window estimate below.

## 3. Exact physical flux and first-site scalar coefficient

Let J_k=dq/dk=g sin k/(j sin q). The actual first-slow-site physical coefficient is A_phys=t_L A_tilde. Its energy-to-Fourier factor is i E'_k/sqrt(2pi), not i E'_q/sqrt(2pi). Since E'_k=J_k E'_q and t_L J_k=t_f sqrt(J_k),

    F_actual,x(k)=t_f sqrt(J_k)
                           [iE'_q A_tilde,x(q)/sqrt(2pi)],
    F_s(k)=t_f sqrt(J_k)[iE'_q A_ref(q)/sqrt(2pi)].     (6)

Here

    t_f=exp[i(q+k)/2]sqrt(sin q sin k)/sin((q+k)/2),
    F_ref(q)=iE'_q A_ref/sqrt(2pi)
       =kappa E'_q zeta exp[i61q+i172k_old(q)]
                                      /[sqrt(2pi)jDref].

Thus F_s has the exact phase61.5q+.5k+172k_old(q), and firstslowm0 is the reference origin. The physical t_L is not replaced by a unit transmission. Its possibly large sqrt(j/g) is canceled only through the actual flux/Jacobian identity.

The identity |t_f|^2=1-|r_L|^2<=1 gives

    p_s=integral_Ik|F_s|^2dk
       =integral_Iq |t_f|^2|F_ref|^2dq=p0-R,
    R=integral_Iq |r_L|^2|F_ref|^2dq.                 (7)

The genuine j-chain scalar reference has total mass one. These exact identities and positivity do not require any contour theorem. In particular p_s<=1. The wide scalar proof separately supplies its new lower bound and concentration curves; neither is silently assumed here for an actual device.

## 4. Parameter-dependent selected coefficient error

Define exact UNNORMALIZED reference moments on I_q:

    M_q2=integral u^2 |F_ref|^2 dq,
    M_E2=integral delta^2 |F_ref|^2 dq.

Define the exact transmitted resonance-weighted moments on I_k:

    J0=integral |F_s|^2/r_delta^2 dk,
    J1=integral delta^2 |F_s|^2/r_delta^2 dk.

They are finite for each positive kappa. No numerical moment from a fixed earlier device is inserted. Minkowski's inequality applied to(5)–(6), followed by flux contraction on the two ordinary moments, gives

    Esel={ (2.1e-13+1e-60)sqrt(p_s)
             +304sqrt(M_q2)+(.302/g)sqrt(M_E2)
             +kappa^2[a sqrt(J0)+b(g)sqrt(J1)] }/.9955,
    ||F_actual,selected-x omega F_s||_2<=Esel.         (8)

This statement is for a subnormalized packet. There is no division by sqrt(p_s) in(8). For simple completely explicit evaluation,

    J0<=p_s/gamma^2, J1<=p_s,
    kappa^2[a sqrt(J0)+b(g)sqrt(J1)]
       <=theta sqrt(p_s), theta=j a+kappa^2 b(g)<.004351. (9)

The exact weighted moments in(8) may be sharper than(9). Ordinary moments may be bounded directly from the genuine reference density, with A=2j-gamma, by

    M_q2<=4kappa^2 h/(pi A^2)*(h/sin h)^2,
    M_E2<=16kappa^2 j^2 h/(pi A^2).                  (10)

These follow from its explicit cotangent density; they are algebraic measure bounds rather than a transfer of narrow contour constants. The nonzero calibration floor and all parameter dependence remain visible.

## 5. Complementary prepared inputs on each physical window

The other prepared vacuum input belongs to C on the selected window. The exact outgoing row on the complementary domain is

    A_tilde,C=-kappa[L_C Dcc^-1
       +(L_j+kappa^2 L_C Dcc^-1 G_Cj)
                           D_x^-1 kappa^2 G_jC Dcc^-1].

Equations(3)–(4) give effective |L_j+...|<461. Using the independently established Im D_x>189kappa^2, rather than a selected-only density approximation, yields

    ||A_tilde,C||
       <kappa[12e-23+461*(6e-23)/189]<2.7e-22 kappa.

Since E'_q/sqrt(2pi)<.003, its preconnector Fourier coefficient is<8.1e-25 kappa. Its q-band L2 norm is therefore<8.1e-25 kappa sqrt(2h). Transmission and the physical variable change multiply its squared norm by |t_f|^2<=1, so the same ceiling holds in slow k. Both physical windows together cost less than

    Ewrong=1.7e-24 kappa sqrt(2h).                   (11)

The complementary response is not deleted because its mathematical reference density vanishes there. It evolves with ACTUAL output-window phase c_att+b_window+E(q), not with a silently reassigned input energy.

## 6. Complete input and record-sector contract

There are two selected old-energy columns in each parity. Using the safe Cauchy–Schwarz column aggregation, without requiring their error ranges to be orthogonal, and then adding(11), gives the complete-input outgoing coefficient allowance

    Eout=sqrt(2) Esel+1.7e-24 kappa sqrt(2h).          (12)

Orthogonal parity blocks combine by maximum. Each record-X sector obeys the same bound. Initial record0 supplies weights1/sqrt2 in orthogonal sector ranges; an unprojected outgoing comparison therefore retains Eout, and final record1 half-difference also costs at most Eout. There is no extra factor two from record recombination.

The ideal sector coefficient is x times the literal W eigenvalue times the SAME scalar F_s. Only after charging the wrong-window terms can the ideal diagonal target factor the common scalar exp(-it c_att) and literal old aging exp(-itK)W. No commutation of K with actual source contacts, per-column phase fitting, waveform translation or postselected target normalization occurs. Tensoring arbitrary passive references preserves these operator norms.

Fourier isometry and restriction to the physical slow halfline make(12) a coefficient-to-outgoing-wave error bound at any real time once the existing physical Stone identification is used on the selected windows. That statement concerns the represented outgoing component only, not the whole actual state. Full synthesis must also retain the actual conjugate incoming term, finite/core coordinates, all closed tails and one global omitted seed amplitude. The scalar wide-reference contour is an independent input for later incoming/outgoing concentration; no actual coefficient is analytically continued here.

## Limits and check targets

The new result is a real-band complete-input coefficient interface parameterized by exact scalar moments, with changed gate/source margins, energy-resolved emitter conditioning and explicit wrong-window columns. It does not choose an operating point or promise a useful Eout at every admissible triple. Any normalized target or actual success/runtime statement needs additional mass, local temporal, scalar concentration and finite-cap composition.

Distinct checking should reconstruct the row slopes304 and.302, the positive2.1e-13 floor, the denominator comparison(5), the physical flux identity(6), the exact moment weighting, and the complementary prepared-input estimate(11). The completed gate and endpoint checks qualify their premises; they do not independently check this new outgoing composition. No retained/audit or native supply claim is made.

## Exact source identities

- `slow_lead_wider_receiver_band/PROPOSAL.md`: `5b667173cd9ee3d8faa285e5856e8a89e8a83ae87f09207664cc5115e247ee57`.
- `slow_lead_wider_receiver_band_check/REVIEW.md`: `9c32a1c901300c32cb6d0630cfef19e9aa33b9438274b6ab8dc561ccc2a38b0d`.
- `slow_lead_wide_endpoint/PROPOSAL.md`: `c4c99408686166ba4d80bc973f5c22afdd1185bbf38e4539512dc26afd5cd5e3`.
- `slow_lead_wide_endpoint_check/REVIEW.md`: `c6cc2ed747956e70bba1a7af3a5d65d3d36a7f708367727cb6f5e8a74386feb5`.
- `slow_lead_outgoing_profile/PROPOSAL.md`: `6f9ebabb3405b124e52582c313c342889c9146e0040306d0ec7b72e8e8371b17`.
- `slow_lead_outgoing_profile_check/REVIEW.md`: `aeb147ff7d430562ff27ab7cbfc276e8066b48199ed6c9a163ee281357ecf528`.
- `slow_lead_wide_reference/PROPOSAL.md`: `c2d7a0cbc06e2669b6e42fca50f3c902dc889b5fb02bc891aaf7d94ab6eff4fd`.
- `bandcenter_reference_measure_check/REVIEW.md`: `1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae`.

The original exact source/calibration pin and upstream row ancestry are preserved in the checked gate/endpoint sources. The scalar-wide source is context for its explicit coefficient; its pending contour check is not claimed as evidence here. Hashes identify evidence, not proof.
