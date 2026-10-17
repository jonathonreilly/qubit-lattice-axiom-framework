# Three-site product source: complete-input outgoing coefficient

Status: new conditional author derivation, requiring a distinct check. This derives a common normalized scalar outgoing comparator with literal W for the actual three-site source. It concerns the represented outgoing spectral component, not the complete actual state. The installed-geometry dependency is still pending distinct checking at drafting time. No one-site emitter, temporal, finite-cap, success or runtime bound is inherited.

## Domain and exact unchanged row

Assume the installed construction in `three_site_actual_attachment/PROPOSAL.md` at the pin below, including its unchanged background, shared B and scalar c_att. Set

    .0027<j<.003, 0<lambda<=1e-8,
    a1=lambda/sqrt(3), a2=lambda sqrt(8/3), kappa²=3j lambda,
    0<h<=4e-6, d=2j sin h, 0<g<=1e-6, d/g<=1/2.

The windows are I_b=c_att+b+2j+[-d,d], b=1,3. Write delta=−2j cos q=−2g cos k, u=|q−pi/2|<=h, w=exp(iq). All original calibration, physical root, full8 background matching and closed-channel premises remain conditional. For each record-X sector x=±1 and each parity let P select the vacuum old energy open on the window, C=I−P, and omega denote the literal W eigenvalue.

The emitter-free outgoing row from the old endpoint-forcing fiber to the first slow site is t_L L_tilde,x. It is independent of how the source is attached after that fiber. Reuse ONLY section 1 and the physical Fourier/flux identities of the checked wider outgoing source, which give

    rho_att=−i w^40 rho_n, rho_n=zeta exp[i172 k_old(q)],
    j ||L_tilde,x+(x omega rho_att w^21/j)P||
         <= e_N(delta)=2.1e-13+304u+.302|delta|/g,       (1)
    ||L_tilde,x P||<460, ||L_tilde,x C||<2e-23,
    ||L_tilde,x||<461.                                (2)

The two actual feedback margins .999983 and .8709, closed returns, input cap and the 18-site cable are already included here. The full row bound follows by summing the two column-domain bounds; it is not inferred from an endpoint-only inverse. The old outgoing source's kappa<=1e-8 and H>=100 restrictions belonged to its one-site emitter estimates, not this emitter-free row. Their replacement is the full three-site conditioning below. The source attachment explicitly preserves the row's operator and reference planes.

## Ordered source recovery and conditioning

Use D=E−c_att−2j−B, G the actual emitter-free kernel and G0=m_j(D). Put

    P2(D)=D²−a1² I,
    Q=P2(D)(D−kappa²G)−a2²D,
    Q0=P2(D)(D−kappa²G0)−a2²D,
    K_E=kappa² Q0^-1 P2(D)(G−G0).

The checked inverse interface gives Q=Q0(I−K_E), in this order. In particular Q^-1=(I−K_E)^-1 Q0^-1; actual matrices are not commuted. Let r=lambda/j, s0=sqrt(1−3r), a0=8e-18 and b0=46000/.0053+290/g. Define

    theta(delta)=kappa²(a0+b0|delta|)
       [|delta²−lambda²/3|/(s0(delta²+lambda²)^(3/2))+6],
    Theta=(j a0+kappa² b0)/s0+6kappa²(a0+b0 d).      (3)

Assume Theta<1. Then ||K_E||<=theta(delta)<=Theta on either physical lip, separately, with all complementary channels retained. On C, ||Q0^-1 C||<170. Write q3(delta) for the selected scalar value of Q0, using the physical j-chain root, not the Markov cubic:

    q3=(delta²−lambda²/3)(delta−kappa²m_j(delta+i0))
                                                        −(8lambda²/3)delta.

For the source forcing at s0, the last source amplitude is a1 a2 Q^-1 f. The background equation is (E−H_bg)psi_bg=−kappa |p>psi_s2, because the physical hopping is −kappa. Thus the actual preconnector outgoing row is exactly

    A_tilde,x=−kappa a1 a2 L_tilde,x Q^-1.          (4)

This also fixes the source sign: the two internal minus hoppings give positive R20, followed by the negative source-to-background hopping. The comparison row on P is x omega A3 P, where

    A3=kappa a1 a2 rho_att w^21/(j q3).            (5)

There is no new propagation phase for the two added source heads. Their exact amplitude and phase are in a1 a2/q3. Fitting or replacing that complex denominator by its modulus would change the comparator.

For selected forcing f in P, Q0^-1 f=f/q3 and

    ||[(I−K_E)^-1−I]f||<=theta(delta)/(1−Theta)||f||.

Combining (1), (2), (4) and (5) gives the pointwise full-row relative comparison

    ||A_tilde,x P−x omega A3 P||/|A3|
       <= e_N(delta)+1.384 theta(delta)/(1−Theta), (6)

where j*461<1.383<1.384. The error term includes all internal components created by loading. No selected scalar inverse is substituted for a full8 inverse, and no one-source positive-imaginary margin is used.

## Genuine scalar packet, slow Jacobian and normalization

The exact isolated three-source scalar measure is normalized and has no residual spectral mass on the stated domain. Its density is

    rho3(delta)=kappa² sin(q)/j * (a1 a2)²/(pi |q3(delta)|²),
    integral rho3(delta) ddelta=1,
    integral delta² rho3(delta) ddelta=a1²=lambda²/3. (7)

The second moment also follows directly from ||h|s0>||²=a1² and is exact for the finite-band measure. Define on q in (0,pi)

    F3(q)=i E'_q A3(q)/sqrt(2pi)
         =kappa a1 a2 E'_q zeta
             exp[i61q+i172 k_old(q)]/(sqrt(2pi) j q3).

Only its values on the selected q interval are needed; the modulus is defined over the full j band by (7). Since E'_q=2j sin q,

    |F3(q)|² dq=rho3(delta) ddelta.                (8)

The phase is the actual old source/converter phase, with no per-input adjustment. Let J=dq/dk=g sin k/(j sin q). At the first slow site m=0 the exact identity is

    t_L J=t_f sqrt(J),
    t_f=exp[i(q+k)/2]sqrt(sin q sin k)/sin((q+k)/2).

Consequently the reference and actual outgoing Fourier coefficients are

    F_s3(k)=t_f sqrt(J) F3(q(k)),
    F_actual,x(k)=t_f sqrt(J) iE'_q A_tilde,x/sqrt(2pi). (9)

Their measure conversion is exact, including flux, the first-site phase and the half-integer connector phase. The comparator phase is 61.5q+.5k+172 k_old(q), together with the exact phase of 1/q3. It is common to both physical old-energy windows and both record sectors after extracting x omega.

Let p=integral_Ik |F_s3|² dk. Then

    p=integral_Iq |t_f|² |F3|² dq,
    0<p<=1, |t_f|²=1−|r_L|².                    (10)

Strict positivity follows from the nonzero density and transmission on a nonempty central interval; it is not a numerical normalization assumption. Normalize once: F_hat=F_s3/sqrt(p).

For a convenient explicit bound, |r_L|=|sin((q−k)/2)|/|sin((q+k)/2)|. Here sin k>=sqrt(15/16), and |q−pi/2|<=|delta|/(2j cos h), |k−pi/2|<=|delta|/(2g sqrt(15/16)). The denominator is at least sqrt(15/16), since both deviations are at most asin(1/4). Thus

    |r_L|<=|delta|/[4sqrt(15/16)]
               [1/(j cos h)+1/(g sqrt(15/16))]
           <= |delta|/g.                        (11)

The last inequality is conservative on g/j<1e-6/.0027 and h<=4e-6. No narrow-band reflection constant is imported. Using (7), and optionally the exact scalar sixth moment mu6=3lambda^6+(8/3)jlambda^5, gives

    1−p <= Xi := min{1,lambda²/(3d²),mu6/d^6}
                                                    +lambda²/(3g²). (12)

If Xi<1, p>=1−Xi and the normalization cost obeys

    1−sqrt(p)<=1−sqrt(1−Xi)=Xi/[1+sqrt(1−Xi)].      (13)

Without Xi<1 retain the exact positive p and its exact cost. Formula (12) concerns the isolated comparison measure; it does not replace a separate installed-seed omitted-state bound.

## Selected and wrong-window errors

Define Jtheta=integral_Ik theta(delta(k))² |F_s3(k)|² dk. Applying (6), the flux contraction and Minkowski gives a valid selected-column allowance

    Esel=2.1e-13 sqrt(p)
       +[304/(2j cos h)+.302/g]lambda/sqrt(3)
       +1.384 sqrt(Jtheta)/(1−Theta).             (14)

Indeed u<=|delta|/(2j cos h), and both ordinary transmitted energy moments are bounded by the full exact moment lambda²/3. This is the requested gain from the sharper source shape; no old Lorentzian moment estimate is transferred. A simpler fully explicit ceiling is obtained by replacing sqrt(Jtheta) by Theta sqrt(p), or further sqrt(p) by 1.

The other prepared old energy on each output window is in C. It must not be deleted merely because its ideal scalar packet is assigned to the other window. From the ordered factorization,

    Q^-1 C=Q0^-1 C+[(I−K_E)^-1−I]Q0^-1 C.

Since Q0 is a function of D, its first term stays in C. Equations (2)–(4) give the full complementary row bound

    ||A_tilde,x C||<=170 kappa a1 a2
                       [2e-23+461 Theta/(1−Theta)] =: Bwrong. (15)

This deliberately conservative estimate retains resonance mixing through K_E. It remains valid even where a selected-only denominator estimate would be insufficient. The preconnector Fourier multiplier is E'_q/sqrt(2pi)<.003; each q interval has length 2h. Transmission and the exact Jacobian are contractive in L2. Adding the two physical output windows therefore costs at most

    Ewrong=.006 Bwrong sqrt(2h).                  (16)

These terms carry the actual output-window energy c_att+b_window+2j+delta, not a reassigned input energy. They include the opposite prepared vacuum column and all complementary internal directions before restriction to prepared inputs.

## Complete-input, record and normalized comparator contract

The two selected old-energy columns in a parity combine safely by Cauchy–Schwarz, giving sqrt(2)Esel; the cross-window rows add (16). Orthogonal parity blocks combine by maximum. Both record-X sectors obey identical bounds, and record0 embeds them with amplitudes 1/sqrt(2) in orthogonal sector spaces. Thus the unprojected outgoing coefficient comparison, and its record1 projection, have allowance

    Eout,sub=sqrt(2)Esel+Ewrong,
    Eout,norm=Eout,sub+(1−sqrt(p)).                (17)

The normalization cost is paid once at the operator level: the ideal subnormalized common-packet map is sqrt(p) times an isometry, so its difference from the normalized common-packet map has norm 1−sqrt(p), not sqrt(2) times that cost. No actual output is postselected or renormalized in (17).

The ideal sector map is x times the same scalar coefficient times literal W. Recombination maps initial record0 to record1. After paying wrong-window terms, the ideal time-dependent outgoing comparator is the common scalar Fourier packet with carrier exp[−it(c_att+2j)] times iota exp(−itK)W, with first slow coordinate m=0 and the same Fourier convention as the checked outgoing interface. Equivalently absorb exp(−i2jt) into the scalar packet and retain exp(−ic_att t) outside. No overall physical phase is discarded. Arbitrary passive references preserve the operator bound.

Fourier isometry on the full line and restriction to m>=0 carry (17) to the represented outgoing component at every real time under the existing Stone coefficient identification. F_hat has unit full Fourier L2 norm; its restriction to the physical halfline need not have norm one at a given time. Thus (17) is a normalized spectral-packet comparator, not an assertion that the physical outgoing halfline already contains unit probability. Scalar incoming/concentration, actual local/source/core and closed-tail terms, one global installed omitted state, finite output cuts and useful-time normalization remain additional obligations. No full-time or finite-performance conclusion follows here.

## Source exposure and exact pins

Root requested this changed-source interface. I authored the wider outgoing source and earlier scalar/attachment components; I checked the present scalar source but did not author it. This is new author synthesis, not a self-certified independent review. I fully read the new inverse, its distinct check and the new attachment, and refreshed the full wider outgoing source/check. Unchanged component evidence is reused only at its exact stated scope.

| Source relative to renewal directory | SHA256 |
|---|---|
| three_site_loaded_inverse/PROPOSAL.md | 7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672 |
| three_site_loaded_inverse_check/REVIEW.md | 8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2 |
| three_site_actual_attachment/PROPOSAL.md | 4278633f3436008a770088331a2424d3f42dda06d08853dfe18d9b8a6554f006 |
| three_site_product_source/PROPOSAL.md | a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823 |
| three_site_product_source_check/REVIEW.md | c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b |
| slow_lead_wide_outgoing/PROPOSAL.md | 593ed5c43008a40101cfc5a9c8243d7190ea7a3f822becbd9644f30b5f74d606 |
| slow_lead_wide_outgoing_check/REVIEW.md | 55de89b5d0536b0ce8028e4a346feb29bcf073f6012dd9cb9e6c01a5d76ead77 |

The wider outgoing row in turn retains corrected gate `5b667173cd9ee3d8faa285e5856e8a89e8a83ae87f09207664cc5115e247ee57` / check `9c32a1c901300c32cb6d0630cfef19e9aa33b9438274b6ab8dc561ccc2a38b0d` and background endpoint `c4c99408686166ba4d80bc973f5c22afdd1185bbf38e4539512dc26afd5cd5e3` / check `c6cc2ed747956e70bba1a7af3a5d65d3d36a7f708367727cb6f5e8a74386feb5`. Their old one-emitter conclusions are excluded. The nominal calibration and B/K/W remain at canonical pin `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff` through this ancestry.

Distinct checking should particularly test the recovery sign/order, the applicability of the unchanged full row after source replacement, the genuine finite-band normalization and second moment, physical t_L versus flux t_f, and wrong-window estimate (15). No numerical experiment, sweep, scientific runner, new calibration, Git/canonical/checkpoint/prompt/model edit, delegation or publication occurred. Exact correlated coefficients, seed preparation and physical Hamiltonian/output identification remain supplied premises.
