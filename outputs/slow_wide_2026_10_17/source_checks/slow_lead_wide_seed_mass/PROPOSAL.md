# Wider slow receiver: paired density and full prepared seed mass

Status: new authored conditional derivation requiring a distinct check. The dominant slow-interface correction can be paired on the symmetric physical energy windows without taking its pointwise resolvent norm first. The cancellation is proved for an arbitrary fixed complex source phase; no actual selfenergy is assumed odd. Positivity then assigns each prepared diagonal its own physical window, while the complete prepared off-diagonal matrix is charged explicitly.

At the supplied candidate g=5e-8, kappa=1e-8, h=4e-6, the resulting proposed actual full-seed bounds are

    M_actual(R outside I) <1.558e-6 I_4,
    ||E_actual(R outside I)V_seed|| <.00125.          (A)

This is not an emitter-output amplitude estimate. Every outside spectral type, including possible atoms, is charged through exact seed normalization. No runtime, finite success or full-state temporal theorem follows here.

## Domain, source exposure and conditional premises

Keep the exact original source/calibration, two converters, capped input, record gate, cable and same-center slow connector. Use .0027<j<.003, 0<kappa<=1e-8, 0<g<=1e-6, 0<h<=4e-6, d=2j sin h, gamma=kappa^2/j, H=d/gamma>=100, d/g<=.5 and L=g/gamma>=2H>=200. Both record-X sectors use the identical physical union

    I=I_1 union I_3,
    I_b=[c_att+b+2j-d,c_att+b+2j+d], b=1,3.

On I_b let delta=Lambda-c_att-b-2j=-2j cos q, u=|q-pi/2|, w=exp(iq), and delta=-2g cos k. In each parity P is the selected B direction and C its full seven-dimensional complement. The other prepared vacuum direction lies in C. Nothing projects the input domain onto P.

Root suggested that a full resolvent L1 comparison may overpay an energy-dependent selfenergy. That was a hypothesis, not evidence. I authored narrower emitter/reference/mass work and checked the wider gate, endpoint, scalar and outgoing compositions. This is new exposed author work, not an independent check of itself. I read the complete wider endpoint and gate sources in the immediately preceding coherent checks, and refreshed the original endpoint source and exact outgoing-row identities for this derivation. Existing local absolute continuity and full complementary bounds are conditional inputs, not newly recertified original source physics.

The following checked wider endpoint facts are used:

    Gref=-Q/j, ||G_x||<550,
    ||G_PC||,||G_CP||<1e-23, ||Dcc^-1||<6,
    g_x=G_PP+kappa^2 G_PC Dcc^-1 G_CP,
    D_x=delta-kappa^2 g_x, Dref=delta+gamma w,
    |D_x|>.9955 r, |Dref|>.9999 r,
    r=sqrt(delta^2+gamma^2),
    |g_x+w/j|<a+b|delta|,
    a=8e-18, b=46000/.0053+290/g.                    (B)

The full actual prepared seed measure is absolutely continuous on both closed windows, including their endpoints. This follows from the already checked complete finite matching inverses and local root branches. Outside I no spectral-type restriction is imposed. The genuine comparison consists of a j chain for every B eigenvalue, compressed to the four prepared vacuum directions; its exact common window mass is p0, not the transmitted scalar mass p_s.

## 1. Isolate the exact leading slow reflection

Write r_L for the scalar connector reflection, r_x for the actual gate/cable return at v0, and rho_R=-i w^22. The checked gate data are

    |r_L|<.128, |r_L|<=.261|delta|/g,
    |r_p,x|,|r_o,x|<=33u,
    |t_x-x rho_R|<=33u, |t_x|<=1,
    |1-r_o,x r_L|>.999983.

Exact two-port composition gives

    r_x=w^36[r_p,x+t_x^2 r_L/(1-r_o,x r_L)].

Since rho_R^2=-w^44, define s=-w^80 r_L. Direct subtraction, before any source feedback, yields

    |r_x-s|
      <=[33+66*.128+33*.128^2/.999983]u <=43u.       (1)

Thus |r_x|<=|r_L|+43u, and, using u<=4e-6,

    |r_x|^2<=|r_L|^2+(86*.128+1849*4e-6)u
              <=|r_L|^2+11.016u.                   (2)

The leading s is common to the two record sectors; no cancellation of actual sector errors is assumed.

Let ell=(B_e)_PP be the scalar selected component of the unchanged unloaded forcing row. Its exact source relation and calibrated comparison give

    ell=-(t_new/j)w^21/(1+R_new w^42)+(E_L)_PP,
    |E_L|<1e-23, |R_new|<1e-20+12u,
    |t_new-rho_n omega|<1.76e-13+1e-20+181u,
    |t_new|<=1,
    rho_n=zeta exp[i172k_old(q)],
    k_old(q)=2asin(sqrt(j/J)sin(q/2)), sqrt(j/J)<1/3,
    |k_old'(q)|<.25.

Here omega is the literal fixed W eigenvalue for the parity, and zeta is the fixed supplied unimodular phase. Define

    ell0(q)=-rho_n(q)omega w^21/j.

The denominator 1-|R_new|>.9999519 proves

    |ell-ell0|<(1.8e-13+194u)/j,
    |ell|<1.00005/j, |ell0|=1/j.                   (3)

The full endpoint feedback is G=Gfree+K_eff f B_eff+F_c, f=r_x/(1-S_eff r_x). Let A_x=(K_eff)_PP(B_eff)_PP. The exact transpose identity K_e=B_e^T A_source^-1 and A_source^-1 P=2ij sin q P imply the unloaded selected product is 2ij sin q ell^2. The closed corrections are below the previously checked allowances 3e-47, 2e-48 and 4e-49. Consequently

    |A_x|<961,
    |A_x-2ij sin q ell0(q)^2|
       <(4.001/j)(1.8e-13+194u)+1e-43.             (4)

No reality assumption on ell or omega is made. The noncommuting full matrices have only been reduced to their actual selected scalar component after the closed elimination.

Define a fixed complex coefficient for this parity/window,

    C(q)=-2ij sin q ell0(q)^2 w^80,
    C0=C(pi/2), |C0|=2/j.

Its varying phase is 122q+344k_old(q) plus a constant. Since its derivative in q is at most 208 and sin q varies by at most u, a safe bound is

    |C(q)-C0|<=418u/j.                              (5)

This estimates only the explicit ideal phase. No derivative of an unknown actual scattering error is inferred from a value bound.

## 2. A structured actual selfenergy remainder

Use the exact identity

    A_x r_x/(1-S_eff r_x)
       =A_x r_x+A_x S_eff r_x^2/(1-S_eff r_x).

The second term is below 1104|r_x|^2, because |S_eff|<1+8e-47 and its denominator exceeds .8709. The first term differs from C0 r_L by three terms: A_x(r_x-s), (A_x-2ij sin q ell0^2)s, and (C(q)-C0)r_L. Equations (1)–(5) and the unchanged free-endpoint error therefore give the ACTUAL selected effective selfenergy decomposition

    g_x(delta)+w/j=C0 r_L(delta)+E_x(delta),
    |E_x(delta)|<=a_E+b_E|delta|+76 delta^2/g^2,
    a_E=4e-11, b_E=120000/.0053.                   (6)

For transparent coefficient accounting, before converting u to |delta|/.0053, the u terms are bounded by

    961*43
      +(.128/j)(4.001*194+418)
      +1104*11.016+8904 <120000.

The constant from (3)–(4), even using |r_L|<.128, is below .128*(4.001/.0027)*1.8e-13<3.415e-11. The original calibration contribution 7.42e-18, tiny closed corrections and selected quadratic Schur term <6e-46 kappa^2 fit in the 4e-11 ceiling. The nonlinear reflected term has coefficient 1104*.261^2<76. These are relaxed comparison allowances, not a change in the original calibration or an assertion that its nonzero floor vanishes. The original sharper envelope (B) is retained for the resolvent remainder below.

## 3. Pairing the first resolvent correction

Put T0=1/Dref, T_x=1/D_x and Delta g=g_x+w/j. Exact scalar resolvent algebra gives

    T_x-T0=kappa^2 Delta g T0^2
                  +kappa^4 (Delta g)^2 T0^2 T_x.  (7)

The actual selected seed density is -Im T_x/pi. Only the leading C0 r_L term in (6) is paired; the remaining terms are bounded absolutely.

Write q=pi/2+asin(delta/(2j)) and k=pi/2+asin(delta/(2g)). The exact interface reflection has the form

    r_L=w a_r(delta),
    a_r=sin((q-k)/2)/sin((q+k)/2).

The real a_r is odd, whereas sin q is even. Thus

    r_L(-delta)=conjugate(r_L(delta)),
    Dref(-delta)=-conjugate(Dref(delta)),
    [T0^2 r_L](-delta)=conjugate([T0^2 r_L](delta)).

Its symmetric integral is real. This is the proved symmetry; Delta g itself need not be odd, and C0 need not be real or imaginary. In particular

    |Im integral_-d^d C0 T0^2 r_L ddelta|
       <=|C0| integral_-d^d |Re(T0^2 r_L)| ddelta. (8)

With beta=1-gamma/(2j) and s_q=sin q,

    Dref=beta delta+i gamma s_q,
    |Re r_L|<=.1305 delta^2/(jg),
    |Im r_L|<=.261|delta|/g,
    |Re T0^2|<=1.0003/r^2,
    |Im T0^2|<=2.001 gamma |delta|/r^4.

Using integral delta^2/r^2<=2d and integral_R delta^2/r^4=pi/(2gamma), equation (8), multiplied by kappa^2/pi, is bounded by

    .5224/L +(.5222/pi)*(d/j)/L <.523/L,           (9)

since d/j=2sin h<8e-6. This removes the logarithmic absolute-norm cost of the dominant slow-reflection term. The smaller explicit source/gate remainder is not assigned this symmetry.

## 4. Per-diagonal mass loss with explicit error terms

The reference mass on the selected window is p0. Explicitly, with A0=2j-gamma, alpha=gamma/A0 and y=tan h,

    p0=4kappa^2/[pi A0^2(1-alpha^2)]
                        *[atan(y/alpha)/alpha-h].

This follows from the normalized genuine j-chain measure, not from a transmitted packet. Equations (6)–(9) imply

    integral_Ib rho_x,jj >=p0-eta_diag,
    eta_diag=.523/L+eta_E+eta_2,                   (10)

where convenient entirely explicit ceilings are

    eta_E=(1.0003 kappa^2/pi)*[
       2a_E atan(H)/gamma+b_E log(1+H^2)
                  +(152/g^2)(d-gamma atan(H))],

    eta_2=(1.006 kappa^4/pi)*[
       2a^2/gamma^2+4ab/gamma+2b^2 asinh(H)].       (11)

For eta_E, bound the first-order E_x contribution with |T0|^2<=1.0003/r^2. For eta_2 use the ORIGINAL (B) envelope, |T0|^2|T_x|<1.006/r^3, and

    integral 1/r^3<=2/gamma^2,
    integral |delta|/r^3<=2/gamma,
    integral delta^2/r^3
        =2[asinh(H)-H/sqrt(1+H^2)]<=2asinh(H).

These are bounds on signed integrated density differences, not claims of pointwise ordering of the selected density. No atom or singular component is omitted inside I because the checked endpoint argument already supplies local absolute continuity there.

## 5. Full prepared matrix and both physical windows

On I_b, compress the actual positive density to the two prepared vacuum directions in a parity. Its CC prepared diagonal is nonnegative. Its off-diagonal density block has norm at most

    (||T_PC||+||T_CP||)/(2pi)
       <7e-23 kappa^2/(pi r),

by the checked full Schur bounds. Therefore this two-by-two matrix is bounded below in Loewner order by its selected diagonal times P_b, minus this cross-block norm times the identity. This uses positivity only for the complementary diagonal; it does not delete the complementary prepared input or its coupling.

Integrating both physical windows charges the complete off-diagonal matrix by

    eta_cross=28e-23 kappa^2 asinh(H)/pi.            (12)

The two selected diagonal deficits act on the orthogonal prepared projections P_1 and P_3. Since each is at most eta_diag, their sum is bounded by eta_diag I, not 2eta_diag I. The nonnegative wrong-window diagonal densities may be discarded for a LOWER bound; the wrong-window OFF-DIAGONALS have just been paid explicitly. Thus in each parity and record sector,

    M_x(I)>= (p0-eta_diag-eta_cross) I,
    0<=M_x(R outside I)
       <=min{1,1-p0+eta_diag+eta_cross} I.          (13)

Orthogonal parities combine by maximum, giving the full four-input statement. Both record-X sectors use the same union and scalar c_att. Record0 initialization averages squared omitted norms in orthogonal sector ranges, preserving the same ceiling; arbitrary passive references preserve the operator bound. The omitted seed embedding norm is the square root of (13), not its mass. This controls the complete evolved omitted state and all outside spectral types, not merely its return to prepared emitter rows.

## 6. One fixed candidate, without a parameter search

At g=5e-8, kappa=1e-8, h=4e-6 and the original supplied j interval, d/g<.48, L>1.35e6, H<720000, d<2.4e-8, log(1+H^2)<28 and asinh H<15. The exact normalized reference tail bound gives 1-p0<1.1e-6. For example 4kappa^2/[pi(2j-gamma)^2 tan h], j>.0027 and pi>3.14 prove that relaxed ceiling directly.

The separate terms obey

    .523/L <3.875e-7,
    eta_E constant term <1.201e-13,
    eta_E linear term <2.12e-8,
    eta_E quadratic term <4.87e-8,
    eta_2 <3.5e-12,
    eta_cross <2e-37.

For eta_2, b<5.81e9 and pi>3 suffice; its a terms are negligible within the displayed slack but are retained in (11). These elementary ceilings imply eta_diag+eta_cross<4.58e-7. Equation (13) therefore gives (A), because .00125^2=1.5625e-6>1.558e-6. This is a proposed improvement of the actual seed-mass certificate at the single requested candidate, not an optimized value or a new performance target.

The surviving logarithm in eta_E multiplies the much smaller source/gate slope b_E. The dominant 290/g term has been treated through its actual interface structure and a quadratic resolvent remainder, rather than simply being erased from the original norm estimate. The exact phase C0 remains arbitrary throughout.

## Scope and required distinct check

The result is conditional on the exact source/row identities, gate and endpoint margins, local absolute continuity and supplied physical identification already stated. A distinct checker must inspect the selected product transpose, 43u gate remainder, coefficient accounting in (6), reflection symmetry and complex C0 pairing in (8), full prepared off-diagonal Loewner bound and both-window aggregation. No review status of an ancestor independently verifies this new derivation.

There is no actual outgoing/incoming waveform or runtime conclusion here, and no statement that the whole actual emitter output has error equal to this mass. Exact total seed normalization is what charges all outside atoms and other singular mass. All original physical/native preparation, calibration and record-identification gaps remain. No parameter sweep, numerical dynamics, scientific runner, delegation, model change, W/Git/PR edit, publication, checkpoint or editable prompt change occurred.

## Exact source identities

- Wider gate: `slow_lead_wider_receiver_band/PROPOSAL.md` `5b667173cd9ee3d8faa285e5856e8a89e8a83ae87f09207664cc5115e247ee57`; check `9c32a1c901300c32cb6d0630cfef19e9aa33b9438274b6ab8dc561ccc2a38b0d`.
- Wider endpoint: `slow_lead_wide_endpoint/PROPOSAL.md` `c4c99408686166ba4d80bc973f5c22afdd1185bbf38e4539512dc26afd5cd5e3`; check `c6cc2ed747956e70bba1a7af3a5d65d3d36a7f708367727cb6f5e8a74386feb5`.
- Exact outgoing row: `slow_lead_wide_outgoing/PROPOSAL.md` `593ed5c43008a40101cfc5a9c8243d7190ea7a3f822becbd9644f30b5f74d606`; check `55de89b5d0536b0ce8028e4a346feb29bcf073f6012dd9cb9e6c01a5d76ead77`.
- Original endpoint identities: `record_attached_emitter_bound/PROPOSAL.md` `2b2161aabb84d533ac884d4199a72d6c4ff6745cd00599a20abe547b9c9caea9`.
- Exact reference measure: `bandcenter_reference_measure_check/REVIEW.md` `1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae`.
- Wider scalar identities: `slow_lead_wide_reference/PROPOSAL.md` `c2d7a0cbc06e2669b6e42fca50f3c902dc889b5fb02bc891aaf7d94ab6eff4fd`; check `61f1796d3f192301a4b88483bf496b2a84304a424dd5b70b4d8df4f2c0e9cced`.
- Original canonical source/calibration: `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`.
