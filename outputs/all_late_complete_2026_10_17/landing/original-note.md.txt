# Three-site complete output at all sufficiently late times on an infinite receiver

Claim type: bounded_theorem. Status: conditional mathematical note prepared for review. The scalar all-late lemma and complete composition have completed distinct ROOT checks; publication integration is recorded separately. No retained audit status is conferred.

Under the unchanged supplied physical/calibration and preparation premises, the actual nominal three-site apparatus with an **infinite passive receiver** has a complete normalized-output error bound for **every t>=T**. Equations (8)-(9) give an explicit sufficient onset for any allowance above the stated comparison budget. No numerical onset or new hardware point is selected. The result does not extend finite storage to all future times.

The [factored-recovery parent](FACTORED_RECOVERY_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md) proves a finite receiver certificate on a finite interval. Here the new ingredient is direct integration of the exact scalar dispersion on its positive-velocity hard band, with both cutoff edges and the integer halfline paid explicitly. This replaces the time-growing dispersion-comparison error for the present infinite-receiver purpose; it does not strengthen the parent into a finite permanent-halt theorem.

The new [scalar proof](../outputs/all_late_complete_2026_10_17/proofs/three_site_all_late_reference__PROPOSAL.md) and [distinct check](../outputs/all_late_complete_2026_10_17/proofs/three_site_all_late_reference_check__REVIEW.md), followed by the [actual complete composition](../outputs/all_late_complete_2026_10_17/proofs/three_site_all_late_complete__PROPOSAL.md) and its [distinct check](../outputs/all_late_complete_2026_10_17/proofs/three_site_all_late_complete_check__REVIEW.md), provide the new proof packet.

## Physical scope and target

Keep the nominal six-block three-source installation of the [spectral parent](CRITICAL_PRODUCT_SOURCE_SPECTRAL_BOUNDED_THEOREM_NOTE_2026-10-17.md) and [temporal parent](THREE_SITE_PRODUCT_SOURCE_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md), original calibrated processor/converters, compensated slow connector, record gate, source-vacuum product preparation V and common scalar c_att. The source coefficients are a1=lambda/sqrt(3), a2=lambda sqrt(8/3), kappa^2=3jlambda. Shared B occurs once and B iota=iota K on the prepared vacuum, with literal K=2I+Z1Z2 and W=[(9+12i)I+(-16+12i)X1X2]/25. No commutation of actual H with K is assumed. No offset, source tolerance, mediator replacement or seven-block phase variant is included. In the source coordinates s0,s1,s2,p the positive blocks are j(n_s2+n_p)-kappa X_s2,p, Q_a2(s1,s2), Q_a1(s0,s1), (j-a2)n_s2, (2j-a1-a2)n_s1 and (2j-a1)n_s0, with Q_a=a(n_u+n_v-X_uv). Source diagonals equal2j and compression leaves the single j n_p load. No new vacuum scalar is added. The literal common scalar remains c_att=2nu+2beta+4gamma_J+4gamma_c+4(sqrt(2)-1)j. The slow connector has magnitude sqrt(jg), with the inherited positive occupations preserving every slow one-head diagonal2j. The head starts at s0 with computational record0 and all prescribed other blank registers.

Keep J=.030021107107032 and the original calibrated relation j=J(1-C0); j is not a freely retuned point in its enclosure. Assume the checked nominal domain

    .0027<j<.003, 0<lambda<=1e-8,
    0<g<=1e-6, 0<h<=4e-6, d=2j sin h, d/g<=1/2,
    eta=lambda/j, s=sqrt(1-3eta)>0,
    a0=8e-18, b0=46000/.0053+290/g,
    Theta=(j a0+kappa^2 b0)/s+6kappa^2(a0+b0d)<1,
    c=(1-Theta)s, n=1/(1-Theta), c_a=2sqrt(2)/3.

All original finite matching, calibration, real structure and full-fiber inverse premises remain required. In particular both physical windows I_b=c_att+2j+b+[-d,d], b=1,3, have the actual seed regularity needed for Stone, including their hard endpoints. The Hamiltonian is the bounded self-adjoint INFINITE apparatus with its passive semi-infinite slow output; outside spectral types are not excluded.

Use the exact scalar F_s3 and physical dispersion of the checked all-late source, without a fitted phase. In detail delta=-2g cos k=-2j cos q, k_old=2asin(sqrt(j/J)sin(q/2)), and the coefficient phase is 61.5q+.5k+172k_old plus the fixed zeta and the complex phase of 1/q3. The flux transmission and sqrt(dq/dk) are retained. For clarity the exact scalar functions are

    m_j(delta+i0)=delta/(2j^2)-i sqrt(1-delta^2/(4j^2))/j,
    q3=(delta^2-lambda^2/3)(delta-kappa^2 m_j)
                                         -(8lambda^2/3)delta,
    t_f=exp[i(q+k)/2]sqrt(sin q sin k)/sin((q+k)/2),
    F3(q)=kappa a1a2(2j sin q) zeta exp[i61q+i172k_old]
                                         /[sqrt(2pi)j q3],
    F_s3(k)=t_f sqrt(g sin k/(j sin q)) F3(q(k)).

The integration band is I_k=[pi/2-alpha,pi/2+alpha], alpha=asin(d/(2g)); the coefficient is zero elsewhere in one 2pi Fourier cell. Put

    p=int_I_k |F_s3(k)|^2 dk, 0<p<=1,
    beta_m(t)=(2pi)^(-1/2) int_I_k F_s3(k)
                                 exp[imk-it delta(k)] dk,
    r(t)=||1_{m>=0}beta(t)||.

The exact normalized COMPLETE target is

    T_norm(t)=exp[-it(c_att+2j)]
          J_out[(beta_+(t)/r(t)) tensor exp(-itK)W],       (1)

whenever r(t)>0. J_out includes record1, the source vacuum, every other prescribed blank register, and the physical slow sites m>=0. Site m=0 is the first slow site, distinct from the old gate port. The comparator is common to all old inputs and passive references. It is normalized by the actual scalar physical-halfline norm, not a fitted normalization of the actual state.

## Fixed actual allowances

Let mu6=3lambda^6+(8/3)jlambda^5. A safe SINGLE global omitted-state allowance is

    eps_sp=min{1,sqrt(2mu6)/d^3}.

It bounds ||E_H(I^c)V|| for the union I=I_1 union I_3, retaining possible atoms and singular mass outside. The independent scalar-reference truncation allowance is eta_ref=min{1,sqrt(2mu6)/d^3}. Its equal numerical expression does not make it another actual omitted charge.

For completeness define q_eta=1-3eta and C_eta=6eta+9eta^2, and the checked scalar local-vector errors

    E0=(C_eta+eta^2/12)/q_eta^2+eta^5/(30pi),
    E1=[4sqrt(3)C_eta/(3pi)+sqrt(3)eta^2/(3pi)]/q_eta^2
                                      +sqrt(3)eta^4/(12pi),
    E2=[C_eta/sqrt(2)+5eta^2/(12sqrt(2))]/q_eta^2
                +eta^3/(3pi sqrt(2))+eta^5/(60pi sqrt(2)),
    Evec=sqrt(E0^2+E1^2+E2^2).

The [actual all-three-source local subtraction](../outputs/three_site_temporal_2026_10_17/proofs/three_site_local_escape__PROPOSAL.md) gives

    Dsel=kappa^2 a1a2/[pi(1-Theta)] *
      [a0*pi/(2s^2 lambda^3)+b0/(s^2 lambda^2)
                              +(6/s)(2a0/lambda^2+2b0/lambda)],
    Dwrong=170 kappa^2 a1a2/[pi(1-Theta)] *
      [(2a0/s)asinh(d/lambda)
       +(2b0/s)(sqrt(d^2+lambda^2)-lambda)+12a0d+6b0d^2],
    S_floor=Evec+eta_ref+sqrt(2)Dsel+2Dwrong.

Then the represented source amplitude, including all three sites and every internal component, obeys

    S_I(t)<=F_loc(lambda t)+S_floor,
    F_loc(z)=exp(-z)sqrt[(1+z+z^2/3)^2+(z+z^2)^2/3+2z^4/9]
             <=9exp(-z/2), z>=0.                       (2)

The last ceiling is the already checked elementary bound. The two selected old-energy errors are combined by Cauchy-Schwarz, while wrong-window errors are retained separately. These are bounds on full prepared-input maps, not a return amplitude on s0 alone.

The [full-input outgoing interface](../outputs/three_site_temporal_2026_10_17/proofs/three_site_outgoing__PROPOSAL.md) supplies the fully explicit RAW outgoing allowance

    Esel=2.1e-13 sqrt(p)
       +[304/(2j cos h)+.302/g]lambda/sqrt(3)
       +1.384 Theta sqrt(p)/(1-Theta),
    Bwrong=170 kappa a1a2[2e-23+461Theta/(1-Theta)],
    Ewrong=.006 Bwrong sqrt(2h),
    Eraw=sqrt(2)Esel+Ewrong.                            (3)

This is a conservative version of the checked energy-resolved outgoing estimate. Both wrong-window prepared columns are included. The [exact real two-lip Stone conjugation](../outputs/three_site_temporal_2026_10_17/proofs/three_site_traveling_interface__PROPOSAL.md) gives the SAME raw allowance for incoming, with W-star and the same physical time, not W and not negative time. Hence both discrepancies cost 2Eraw; their physical halfline outputs are not presumed orthogonal.

## Background decay constant

Retain L0=14000 and a checked full-forcing recovery derivative bound M. One available improved choice is

    M=1.00068[1.21e16+1.28e6/g]+30,

from the separately checked [factored derivative](../outputs/factored_recovery_2026_10_17/proofs/prepared_full_recovery_factored_derivative__PROPOSAL.md). This note retains that envelope; the parent’s later load-action refinement is not needed for the existence of the all-late onset. The older M=1.00068[7.29e16+3.31e7/g]+30 is also valid and requires no new interpretation. Neither is a selected-only derivative. They include every 235 finite background head and all closed slow tails, excluding the three source sites and open stationary ray.

For an explicit full prepared inverse-derivative bound one may conservatively use A=6.01, A_s=2/s+A/s^2 and Z_g=2e8+17000/g, and set

    D3bar=(c_a/lambda){n A pi/(2s^2)
      +(3j n^2/s)[A_s(4a0/3+2b0lambda/3)+400a0lambda^2
                   +400b0lambda^3+Z_g(pi lambda/(2s)+12lambda^2)]}.

This is the [checked ordered full-fiber derivative integral](../outputs/faster_three_site_2026_10_17/proofs/three_site_prepared_inverse_derivative__PROPOSAL.md), already including complementary prepared inputs. A separately checked sharper nominal A may replace 6.01 only in its own stated domain; that replacement is not needed here. Define the finite constant

    H_bg=2kappa/pi * [2c_a lambda^2 L0/(c(d^2+lambda^2)^(3/2))
                                      +2c_a M/c+L0 D3bar].

The checked [Hilbert-valued Stone integration by parts](../outputs/faster_three_site_2026_10_17/proofs/prepared_background_ibp__PROPOSAL.md) then yields

    B_I(t)<=H_bg/t, t>0.                               (4)

Both lips, both physical windows, their nonzero hard endpoints and the full spatial closed-tail derivative are already paid in H_bg. The windows' closed projectors differ but each is fixed on its own interval, and both maps are embedded in the physical Hilbert space. There is no extra complementary D3 charge, no actual-source complex-strip assumption and no second omitted-state charge inside (4).

## Exact all-late scalar constants

Here are the explicit constants from the newly checked exact-dispersion lemma. They are reproduced to make the sufficient onset evaluable without a finite-time comparison. Set

    alpha=asin(d/(2g)), v_*=2g cos alpha,
    Q1=g/(j cos h), P_phi=.5+102.78Q1,
    P_N=tan(h)Q1+tan(alpha)+.5tan((h+alpha)/2)(Q1+1),
    A_ref=3+9eta/(2cos h), C_ref=sqrt(8lambda^5/(3pi)),
    K_ref=sqrt(2g)C_ref,
    I0=2K_ref/(s v_* lambda^2),
    I1=(P_phi+P_N)I0+K_ref A_ref pi/(2s^2 lambda^3),
    E_edge=2K_ref/[s(d^2+lambda^2)^(3/2)],
    B_ref=E_edge+I1+(d/v_*)I0.

For every positive t, with the EXACT phase and dispersion,

    J(t)=B_ref/sqrt(2pi)*sqrt((v_*t)^(-2)+(v_*t)^(-1)),
    C_left(t)^2=B_ref^2/(2pi v_*t),
    ||incoming_raw(t)||<=min{sqrt(p),J(t)},
    ||1_{m<0}beta(t)||<=min{sqrt(p),C_left(t)}.          (5)

To see the all-late mechanism, write F_s3=zeta exp(i phi)K_ref N/q3, where N=sin q sin k/sin((q+k)/2). The actual bounds are |phi'|<=P_phi, 0<N<=1, |N'|<=P_N, |q3|>=s(delta^2+lambda^2)^(3/2), and |dq3/d delta|<=A_ref(delta^2+lambda^2). They follow from the exact phase/map, logarithmic derivative of N and differentiated physical Weyl function, rather than from differentiation of value inequalities. Consequently the coefficient has L1 norm<=I0, interior derivative L1 norm<=I1 and sum of its two endpoint magnitudes<=E_edge.

For incoming m=n>=0 or excluded outgoing m=-n,n>=1, the physical phase is -nk-t delta(k), with derivative magnitude at least n+v_*t and |delta''|<=d. Integration by parts on the closed band therefore bounds each Fourier coefficient by B_ref/[sqrt(2pi)(n+v_*t)]. The two edge terms are nonzero and included. The exact sums satisfy sum_(n>=0)(z+n)^(-2)<=z^(-2)+1/z and sum_(n>=1)(z+n)^(-2)<=1/z. These prove (5), including the incoming m=0 term. There is no dispersion error growing with time, no sampling/alias approximation and no continuity argument from the old finite window. Since ||beta||^2=p, if C_left(t)^2<p then

    r(t)>=sqrt(p-C_left(t)^2)>0,
    1-r(t)<=1-sqrt(p-C_left(t)^2).                     (6)

The scalar mass can remain its exact positive integral. If a fully elementary lower bound is preferred and Xi<1, the checked scalar formula supplies

    p>=p_*=1-Xi>0,
    Xi=min{1,lambda^2/(3d^2),mu6/d^6}+lambda^2/(3g^2).

One may replace p by p_* in all lower-norm and onset denominators, use sqrt(p)<=1 in (3), and charge 1-sqrt(p_*) in the constant budget. This is conservative and uses no density of the actual loaded source.

## Complete actual evolution and explicit onset

The actual represented spatial decomposition consists of all three source sites, the remaining finite/closed background and the two traveling terms. The omitted actual spectral vector is added globally once. Using (2)-(6) gives, whenever C_left(t)^2<p,

    ||exp(-itH)V-T_norm(t)||
      <= eps_sp+S_floor+F_loc(lambda t)+H_bg/t+2Eraw
                          +J(t)+1-sqrt(p-C_left(t)^2). (7)

All norms are complete unprojected operator norms, stable under arbitrary passive-reference extension. The target contains record1; the actual vector is not postselected. Orthogonal conserved record-X and parity sectors combine by maximum after their normalized initial record weights are retained. Old-energy error images are not assumed orthogonal. The checked local/outgoing/background estimates already pay their respective old-energy and wrong-window factors.

Define the time-independent sufficient certificate

    e_floor=eps_sp+S_floor+2Eraw+1-sqrt(p).             (8)

It is an upper allowance, NOT an actual error lower bound or a proof of irreducible leakage. For any desired e>e_floor let Delta=e-e_floor>0. The following completely explicit sufficient onset works:

    T=max{1/v_*,
          (2/lambda)max{0,log(36/Delta)},
          4H_bg/Delta,
          16B_ref^2/(pi v_* Delta^2),
          B_ref^2/(pi v_* p),
          2B_ref^2/(pi v_* sqrt(p) Delta)}.            (9)

Then for EVERY t>=T,

    r(t)>0,  ||exp(-itH)V-T_norm(t)||<=e.              (10)

To verify (9), the second term and (2) give F_loc<=Delta/4. The third bounds H_bg/t by Delta/4. Since v_*t>=1, J(t)^2<=B_ref^2/(pi v_*t), and the fourth term gives J<=Delta/4. The fifth ensures C_left^2<=p/2 and hence r>0. Finally

    sqrt(p)-sqrt(p-C_left^2)
       =C_left^2/[sqrt(p)+sqrt(p-C_left^2)]
       <=C_left^2/sqrt(p)<=Delta/4

by the sixth term. Summing the four decaying allowances above (8) proves (10). No interchange of a t limit and actual finite-system evolution is made. The exact curve (7) is often preferable to the crude four-way sufficient split in (9).

In particular the construction proves the qualified infinite-apparatus limit statement

    limsup_{t->infinity} ||exp(-itH)V-T_norm(t)||<=e_floor.

It does not assert that the true limit is e_floor or that the error has a limit. The packet is time-dependent through its prescribed exact physical evolution and normalization, not selected separately to fit the actual state. If the displayed floor exceeds a requested allowance, these bounds do not certify that request; this is not a physical obstruction claim.

For 0<e<1, the complete bound also implies at any single chosen t>=T failure effect <=e^2 I and success >=1-e^2 for the specified record read. Normalized successful-vector distance is at most e+1-sqrt(1-e^2), and complete-channel and subnormalized success-map diamond errors are at most 2e. A normalized conditional output rule is not a linear channel. These are single-read consequences of unmeasured evolution, not simultaneous assertions about a sequence of measurements.

## Infinite output and remaining physical obligations

This result concerns the actual INFINITE passive lead. At every late time the target is on its physical positive halfline, but its position distribution continues to evolve. There is no claim of concentration in one fixed finite interval for all late times. A fixed finite cap permits returns and recurrence; its finite-cut error is not uniformly small as t tends to infinity. Thus neither (9) nor the limsup statement proves finite permanent storage, a halt, repeated polling safety or an irreversible latch.

No numerical onset or new hardware point is selected. The previously checked PR 9685 finite-window point and its bounds are unchanged. This all-late sufficient onset may be far more conservative: the new scalar J is only an algebraic t^(-1/2) certificate, unlike a resonant finite-window approximation. A practical evaluated all-late time would require substituting the same fixed parameters in every constant and separately reviewing that arithmetic. No finite-window scalar dispersion bound is extrapolated beyond its interval.

All source preparation, physical Hamiltonian identification, calibration, exact compensated coefficients, record readout and physical time-unit premises remain supplied. No native supplier, common-mode/tolerance family or mediator source theorem is imported. This composition uses the actual loaded source only through its checked full-input interfaces and actual spectral moment, not through a scalar substitute for its inverse.

## Evidence, review exposure and publication boundary

The scalar and complete proofs have both received source-exposed checks distinct from their author. ROOT reconstructed the new exact-coefficient derivative, hard-edge integration, integer sums and physical normalization, then independently checked the complete accounting and every sufficient-onset threshold. Those checks support the stated conditional scope, not the underlying supplied calibration as a newly audited physical result.

I authored both new proofs and the weighted-reference, traveling and background-IBP ancestors, and checked several other components. ROOT authored the local-source ancestor and other shared interfaces. This is same-model collaborative proof development with disclosed ancestry, not blind or model-diverse validation. The completed ROOT composition review was read in full for this note. No unchanged ancestry is recertified by repeating its result here.

New packet identities:

| New source or review | SHA256 |
|---|---|
| three_site_all_late_reference/PROPOSAL.md | 7044e77bcf2d944a3f1b4286b885691fd9f88e733a6ab49514111af5acbc5966 |
| three_site_all_late_reference_check/REVIEW.md | 4ba80afbbc2301fbb4e23aafe59f85b3a85ebdab160101f970774d0383139247 |
| three_site_all_late_complete/PROPOSAL.md | 053d8bd41ee8e16884b303b2b6bc2c8073fd840e7d4087205faa0279d4ddc693 |
| three_site_all_late_complete_check/REVIEW.md | cf275f3fa8598a2d9705ca6493a76d6ec23f3af7f44f93c6e260614342ee7f49 |

The scalar finite-band density and moment formulas are retained in the existing [critical-source packet](../outputs/critical_source_2026_10_17/source_checks/three_site_product_source/PROPOSAL.md). The full inherited proof/check identities are listed in the new composition source and their existing parent packets. No duplicate unchanged proof packet is proposed here. The original canonical physical premise remains SHA25671c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff.

Final publication integration and installed copy/link/graph evidence are recorded separately. This drafting created only this note; it used no scientific runner, numerical inverse, quadrature, dynamics, parameter sweep, new operating point, delegation, canonical/W/Git/PR/checkpoint/prompt/model change or audit process. No editable prompt files changed.
