# Perturbed actual three-source and background amplitude interface

Status: new conditional author derivation requiring a distinct check. The perturbed attachment/inverse/moment dependency has now received a distinct conditional check, read completely before freezing this artifact. This derives represented local-source and complete background absolute-integral bounds. It selects no tolerance, operating point, outgoing waveform, runtime or complete performance claim.

## 1. Domain and explicit premises

Use the exact construction and parameter domain of `three_site_perturbed_attachment/PROPOSAL.md` at f32b28aba669d09933c9c22052b2abce4d68339f43faa5beac8f3dc4d8ee978d. In particular the same positive six-block source at s0,s1,s2 has real identity detunings d_i, positive negative-hopping amplitudes

    a1^2=(lambda^2/3)(1+e1), a2^2=(8lambda^2/3)(1+e2),
    kappa^2=3jlambda(1+e3), |e_i|<=epsilon, |d_i|<=epsilon lambda.

Retain .0027<j<.003, 0<lambda<=1e-8, eta=lambda/j<=1/16, 0<h<=4e-6, 0<g<=1e-6, d=2j sin h, d/g<=1/2. The original nominal calibration, common B, its vacuum restriction K, scalar c_att, installed edges and complete background matching are unchanged. Detunings are not input-dependent phases. The two physical windows remain I_b=c_att+2j+b+[-d,d], b=1,3.

Define

    B_eps=20epsilon+16epsilon^2+4epsilon^3,
    m=1-3eta-B_eps>0,
    A_eps=(1+epsilon)^2+(1+epsilon)/3,
    a0=8e-18, b0=46000/.0053+290/g,
    Theta=kappa^2[(A_eps/m)(a0/lambda+b0)+6(a0+b0d)]<1,
    c=(1-Theta)m.

These are the sufficient conditions of the checked attachment. They imply epsilon<.05; they are not necessary conditions for emission. Here a0,b0 denote background error coefficients, distinct from the source bond labels.

On a window set D=(E-c_att-2j)I-B, A_i=D-d_i I, P_eps=A_0 A_1-a1^2 I, v=delta^2+lambda^2. Let G be the actual unchanged emitter-free background and G_ref=m_j(D). The exact reference and loaded denominators are

    Q_ref=P_eps(A_2-kappa^2 G_ref)-a2^2 A_0,
    Q=P_eps(A_2-kappa^2 G)-a2^2 A_0.

Retain the attachment's separately derived full complementary margin |q_ref(x)|>.99|x|^3 for |x|>=.185, and its selected |q_ref(delta)|>=m v^(3/2). Its ordered factorization gives

    ||Q^-1 P||<=1/[c v^(3/2)],
    ||Q^-1 C||<170/(1-Theta),
    ||Q^-1||<=1/[c v^(3/2)],
    ||G-G_ref||<=a0+b0|delta|.                            (1)

All statements are required on each physical lip separately. P is the selected open channel on the current window, C its full complement. The reference is the direct sum of genuine scalar uniform-j chains over the full B spectrum, not a Markov bath applied to closed channels.

## 2. Joint reference last-source column, including complements

Let R_ref be the inverse of the three-source reference Schur matrix, and E_2 its last-source injection. Cofactors, or direct substitution, give the ordered reference column

    R_ref E_2=(a1a2,-a2 A_0,P_eps)^T Q_ref^-1.             (2)

Only reference factors commute as functions of D. For the nominal bonds a=lambda/sqrt(3), b=lambda sqrt(8/3), the numerator vector (ab,-b delta,delta^2-a^2) has exact squared norm v^2. We bound its perturbation, instead of assuming that identity survives detuning.

Put

    r_eps=1-sqrt(1-epsilon),
    c0=(2sqrt(2)/3)epsilon,
    c1=sqrt(8/3)[r_eps/2+epsilon sqrt(1+epsilon)],
    c2=(4/3)epsilon+epsilon^2,
    C_eps=1+sqrt(c0^2+c1^2+c2^2).                         (3)

The first component changes by at most epsilon ab<=c0 v, since sqrt((1+e1)(1+e2)) lies between 1-epsilon and 1+epsilon. The second changes by at most

    b[r_eps |delta|+sqrt(1+epsilon)epsilon lambda]<=c1 v,

using lambda|delta|<=v/2 and lambda^2<=v. The third changes by

    -delta(d0+d1)+d0d1-a^2 e1,

whose modulus is at most c2 v. Consequently the entire perturbed numerator has norm at most C_eps v. In particular C_eps tends to one with epsilon; a joint norm is used rather than a seed-return-only numerator.

For complementary |x|>=.185 put t=lambda/|x|<6e-8. The attachment bounds |P_eps(x)|<1.000001|x|^2. Also

    |a2(x-d0)|<=sqrt(8/3)*sqrt(1.05)*t(1+.05t)|x|^2,
    |a1a2|<.944*1.05*t^2 |x|^2.

The sum of these three component magnitudes is below 1.000002|x|^2. Dividing by .99|x|^3 gives a norm less than 6. Thus the closed-column value 6 is justified for this JOINT perturbed column, not merely inherited from the bound for P_eps/Q_ref. It holds for both signs of the closed root and all complementary channels. Combining the selected and complementary estimates safely gives

    ||R_ref E_2||<=C_eps/(m sqrt(v))+6.                   (4)

The bound is a sum over orthogonal spectral domains and needs no channel-count factor.

## 3. Exact actual/reference subtraction and two Stone allowances

Let R be the inverse of the actual three-source Schur matrix, with E_0 the seed injection. Since S=S_ref-kappa^2 E_2(G-G_ref)E_2*, the resolvent identity in the useful order is

    (R-R_ref)E_0=kappa^2 (R_ref E_2)(G-G_ref) R20,
    R20=a1a2 Q^-1.                                      (5)

No actual G is commuted through D or a source polynomial. Combining (1),(4),(5) gives selected and complementary full-output bounds

    ||(R-R_ref)E_0 P||
      <= kappa^2 a1a2(a0+b0|delta|)/(1-Theta)
         [C_eps/(m^2 v^2)+6/(m v^(3/2))],
    ||(R-R_ref)E_0 C||
      <=170 kappa^2 a1a2(a0+b0|delta|)/(1-Theta)
                       [C_eps/(m sqrt(v))+6].            (6)

Every source output coordinate is included. A wrong-window prepared input lies in C and is not deleted. Its reference jump is zero on that window, because the reference roots there are real and the complementary source determinant has no pole.

Actual spectral synthesis requires the attachment's full matching/root regularity, not just (6). Under those premises the seed/source cross measures are absolutely continuous on neighborhoods of the two closed windows. Apply the rectangular Stone jump (R_down-R_up)/(2pi i) on each window. Equal majorants on the two lips give the following per-window errors, uniform in real time:

    Dsel_eps=kappa^2 a1a2/[pi(1-Theta)] *
      [(C_eps/m^2)(a0*pi/(2lambda^3)+b0/lambda^2)
                         +(6/m)(2a0/lambda^2+2b0/lambda)], (7)

    Dwrong_eps=170 kappa^2 a1a2/[pi(1-Theta)] *
      [(C_eps/m)(2a0 asinh(d/lambda)
                   +2b0(sqrt(d^2+lambda^2)-lambda))
                                      +12a0d+6b0d^2].     (8)

For (7) use the full real-line nonnegative integrals of v^-2, |delta|v^-2, v^-3/2 and |delta|v^-3/2, respectively pi/(2lambda^3), 1/lambda^2, 2/lambda^2 and 2/lambda. For (8) integrate only [-d,d]. Extending majorants in (7) does not extend the actual device's spectral domain. No source-energy derivative is used.

The two selected old-input projections cost at most sqrt(2)Dsel_eps by triangle/Cauchy–Schwarz, and both wrong-window pieces cost at most 2Dwrong_eps. Their actual error images are not assumed orthogonal. Orthogonal parity and record-X sectors combine by maximum, with the initial normalized record0 superposition retained. Passive references preserve these operator bounds. The lower denominator is treated in its own physical ordering; it need not be the adjoint of the upper Q.

## 4. Perturbed scalar reference and represented local-source estimate

Use the separately checked scalar local stability source b36ef900 and its distinct review 3db96616. Let E_local(epsilon) be its explicit polynomial/density-ratio allowance. The exact perturbed isolated scalar three-source vector satisfies, for t>=0,

    ||v_ref,eps(t)||<=min{1,F(lambda t)+Evec+E_local},       (9)

where F and Evec are the checked nominal finite-band scalar expressions. This retains all three sites and the actual perturbed scalar density, without assuming the split poles remain a triple pole. This is a fixed nominal comparison bound, not a fitted detuning-dependent time phase.

For clarity the moment needed for truncating this perturbed reference can be obtained directly from its physical prefix. Center at the original carrier. The third-power head coefficients are

    c_0=d0^3+a1^2(2d0+d1),
    c_1=-a1(d0^2+d0d1+d1^2+a1^2+a2^2),
    c_2=a1a2(d0+d1+d2), c_p=-a1a2 kappa.

They have orthogonal head supports, so its exact sixth moment is

    mu6_eps=c_0^2+c_1^2+c_2^2+(a1a2 kappa)^2.             (10)

The genuine uniform-ray reference has no omitted bound component outside its normalized scalar measure, by the scalar robustness premise. Equation (10) and the spectral theorem give the conservative two-old-energy common-union truncation allowance

    eta_ref,eps=min{1,sqrt(2mu6_eps)/d^3}.                 (11)

The perturbed attachment has the SAME local moment for the actual installed seed because the third power first reaches the old port and has not yet acted through its downstream contacts. This actual claim has its separate attachment check; it is not inferred from the reference's absence of atoms.

Let Q_src project onto all three actual source heads and I be the common physical union. Combining the represented subtraction with (9)–(11) gives

    ||Q_src exp(-itH) E_H(I) V||
      <= min{1,F(lambda t)+Evec+E_local+eta_ref,eps
                             +sqrt(2)Dsel_eps+2Dwrong_eps}, t>=0. (12)

The minimum one is allowed because this is a projection of unitary evolution of the projected seed map. Equation (12) excludes the actual omitted state. Its reference truncation charge is necessary even though a separate actual moment is available. A bound on the untruncated actual local source may add eta_actual,eps; a later complete-output argument must instead charge that actual omitted vector once globally.

## 5. Full background absolute-integral bound

The source replacement, including scalar identity detunings, leaves the emitter-free background G and recovery L exactly unchanged. The checked prepared-core derivation and its two complementary selective reviews supply

    ||L(E)||<L0=14000

on both physical windows and lips. L covers every non-source finite coordinate and the complete slow closed tails; the stationary open ray is excluded. The endpoint forcing domain is the full eight-coordinate fiber, not just its selected entry.

The actual background seed column remains exactly

    -kappa L a1a2 Q^-1.                                (13)

Using the FULL inverse from (1), the two lip norms and two-window triangle inequality gives, uniformly in real time,

    B_I,eps <=4 kappa a1a2 L0/[pi c lambda^2]
             <=8sqrt(2)(1+epsilon) kappa L0/(3pi c).      (14)

For one window the factor is (1/pi) times integral v^-3/2<=2/lambda^2; paying two windows gives 4/pi. The perturbed numerator is explicitly retained through a1a2<= (2sqrt(2)/3)(1+epsilon)lambda^2. This does not silently reuse the nominal numerator or c3. No derivative estimate or actual long-time escape assertion is needed for this absolute bound.

The background and three source coordinate ranges are disjoint. Their represented norms can be added conservatively in a future synthesis. Closed tails must remain in the background allowance; open traveling components require separate proofs. Neither (12) nor (14) charges the global actual outside state. When that state is needed, its proposed full-input bound is eta_actual,eps<=min{1,sqrt(2mu6_eps)/d^3}, including all spectral types, to be paid once rather than once per spatial range.

## 6. Limits and source exposure

The sufficient parameters m>0 and Theta<1 may lose sharpness relative to nominal conditioning even at epsilon=0; this is an honest conservative extension, not evidence of a physical instability. The bounds give local/source and background interfaces only. They do not certify useful numerical tolerance, normalized output, actual outgoing/incoming stability, temporal onset, finite receiver performance, repeated measurement, permanent halt or native coefficient preparation. Complete phase, literal W/old aging and common scalar remain owed in a subsequent output target.

I authored the original scalar robustness/reference and several recovery ancestors, and checked the new perturbed scalar-local lemma and the prepared-core dwell argument. I did not author the perturbed attachment or root's new scalar-local lemma. Root requested this source/background extension. This is new exposed author synthesis requiring a distinct check, not independent revalidation of my own ancestors. The attachment and its newly received distinct review 0fd4a54559c48af641f9c90baa326e78a7bcc51f9428d0384ab6c7cc0252447d were read completely; the review conditionally supports its physical, inverse and moment claims. This new local/core extension still needs its own check. The nominal actual-local and complete prepared-core arguments and checks were fully read in the preceding coherent task, with unchanged identities reused below.

Required source pins:

- Perturbed attachment `three_site_perturbed_attachment/PROPOSAL.md`: f32b28aba669d09933c9c22052b2abce4d68339f43faa5beac8f3dc4d8ee978d ; distinct check `three_site_perturbed_attachment_check/REVIEW.md`: 0fd4a54559c48af641f9c90baa326e78a7bcc51f9428d0384ab6c7cc0252447d.
- Perturbed scalar local `three_site_perturbed_local_reference/PROPOSAL.md`: b36ef9001996fd031bfabd8541776be27831050cac6b67fee1016cf10f04b504; check 3db966162b1c49a28041a8c0a04eaa9c5bebb7613718894d43227b3e65cd18c7.
- Scalar robustness `three_site_source_robustness/PROPOSAL.md`: 32456b0b5c99ad1acfcdc9a770d022ffcc14069dee157981c715177cfa6a7eb6; check ba06cef2ddf0aae45eeaf5f5c8740258babe21d2a8206fbf6c1eb7b3b33f97ad.
- Nominal actual local `three_site_local_escape/PROPOSAL.md`: 0340895610d3a5ef709dd8a03c1bc5872c8f34cf00f21053c00adcc3d706468d; check e19767c8092fb856a3c24cb279f621deea38d69d65c41bef4a1aea44bad23074.
- Prepared core `prepared_core_recovery/PROPOSAL.md`: cce29994b7141df161ca12f377765fdaf760f7e64fc56043bbf370e2cd437ea9; dwell check 88274b8b49e583bdb9b5f933f7406b1a96a6ca79049e57b83e8030c834d16819; composition check 52edba6061be49eef40b5c06754a7425b5f7f62671f175cc72a093d4a60de65c.
- Nominal scalar `three_site_product_source/PROPOSAL.md`: a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823; check c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b.

A distinct reader should test the joint perturbed numerator, the independent closed-column bound 6, full inverse ordering, both-lip integrals, scalar-versus-actual truncation and the factor 4/pi in (14). No scientific computation, integration, parameter sweep, operating-point selection, W/Git/PR/checkpoint/prompt/model edit or delegation occurred. Only this proposal was created.
