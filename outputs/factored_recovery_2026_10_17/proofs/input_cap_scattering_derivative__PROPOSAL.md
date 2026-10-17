# Physical scattering derivatives for the factored input cap

Status: new conditional author derivation requiring a distinct check. On the original nominal calibration and both physical windows |q-pi/2|<=4e-6, the uncapped two-converter input-input scattering block satisfies

    s1=||P S' P||<39000, swide=||S'||<5e22,

where primes are PHYSICAL E derivatives at fixed hardware. Consequently the checked cap forcing obeys ||alpha'||<2e7, ||C alpha||<1.72e-35 and ||C alpha'||<8.6e-31. These are full endpoint-forcing operator bounds, not a full recovery Lprime or runtime theorem. The complementary finite old recovery derivative remains a separate obligation.

## 1. Exact conventions and retained premises

Use fixed B projectors on each window, both physical lips, the original two old-J ports with origins m=0, converter planes m=40 and the first-new-site j-port origins. Shared internal coordinates are not duplicated. Set L=Q_old^40. For the old generalized source S_o=T_old A_old^-1, the two-converter full physical-amplitude matrix is exactly

    S_new=R_n+V L S_o F L U,
    F=(I-R_o L² S_o)^-1.                              (1)

U,V,R_o,R_n are diagonal channel converter matrices on the two ports; S_o is generally noncommuting. Its physical derivation is A=R_o B+U alpha, beta=R_n alpha+V B at the outer planes, followed by the old source propagation. No closed flux normalization is introduced. The requested S is the input-input block of S_new. All estimates below for the whole two-port matrix also bound this block.

The checked enlarged-band and converter derivative arguments supply

    ||S_o||<1.000001, ||S_o'||<4e22,
    ||L||=1, ||L'||<1600,
    ||R_o||<.2, ||R_o'||<230,
    ||U||<.49, ||U'||<300, ||V||<2.5,
    ||R_o L²||<4.881e-6, ||F||<1.000005.              (2)

The full S_o' bound uses the actual old-k analytic disks of radius1e-12, complex finite-matching bound ||S_o||<1e9 and |dk/dE|<40. It is not a derivative of a small real scattering value. Its full-fiber scope includes all closed blocks. The sharper selected derivative will be obtained separately.

For L', the selected phase derivative is40|dk/dE|<1600; closed powers give40*7^-39*5, smaller than this. The R_o L² bound uses open |r_o|<4.88e-6 and closed .2*7^-80; taking the diagonal-channel maximum gives <4.881e-6. Combining with the sharper inherited source norm 1+2(5.2e-12)+5.2e-32 proves the stated F margin. A crude product .2||L||² would lose this physical propagation structure unnecessarily.

## 2. Complete converter coefficients and their real derivatives

For signed closed roots a,w, the exact interface equations give

    H=epsilon-J-j+Ja+(tau²/j)w,
    U=-tau(1-w²)/H,
    V=(tau/j)w(1+R_o),
    R_n=-w²+(tau/j)w U.                              (3)

On open channels the last two identities hold as well, with w=exp(iq), R_o=r_o and U=eta_c=t_c sqrt(v_new/v_old). These are physical site amplitudes at the first-new-site plane. In particular the exp(iq) phase is not removed. The checked open coefficient calculation gives |U'|<300 and |r_o'|<230 by direct quotient and velocity-factor differentiation.

For closed channels the checked H bounds are |H|>.1797, |H'|<1.157, |w|<1/60, |w'|<.104, |a'|<5, tau<.007 and tau/j<2.4. Differentiating U, rather than its value ceiling, gives

    |U'|<=tau[2|w w'|/|H|+(1+|w|²)|H'|/|H|²]<1.

Thus the full U' bound300 in(2) covers both types. Differentiating V and R_n in(3) gives on open channels

    |V'|<2.4[189(1+4.88e-6)+230]<1010,
    |R_n'|<2*189+2.4[189*.49+300]<1400.               (4)

The closed versions obey |V'|<2.4[.104*1.2+3/60]<1 and
|R_n'|<2*.104/60+2.4[.104*.04+1/60]<1. Therefore ||V'||<1010 and ||R_n'||<1400 on the full fiber. Both signs of all closed roots are covered. No equality of unnormalized forward and reverse transmissions is assumed.

## 3. Differentiate the FULL ordered matrix

Let K_c=R_o L² S_o. Exact differentiation gives

    K_c'=R_o' L² S_o+R_o (L²)' S_o+R_o L² S_o',
    F'=F K_c' F,
    S_new'=R_n'+V' L S_o F L U+V L' S_o F L U
       +V L S_o' F L U+V L S_o F' L U
       +V L S_o F L' U+V L S_o F L U'.               (5)

The order is retained in every term. Since ||(L²)'||<=3200,

    ||K_c'||<230*1.000001+.2*3200*1.000001
                                  +(4.881e-6)(4e22)<1.953e17,
    ||F'||<(1.000005)²(1.953e17)<1.954e17.

The dominant direct S_o' term in(5) is bounded by

    2.5*(4e22)*1.000005*.49<4.900025e22.

The F' term is <2.5*1.000001*(1.954e17)*.49<2.4e17. All other terms together are <10000. Thus ||S_new'||<5e22, and hence swide<5e22 for its input-input block. This intentionally coarse bound is justified by a genuine analytic old-source premise and direct real converter derivatives; no complex converter domain is presumed.

## 4. Sharper SELECTED derivative without a full-matrix loss

Eliminate only closed old returns exactly as in the checked converter proof. At the outer planes let B=S_tilde,B=z^80 S_tilde, where the closed feedback is retained. That proof and its distinct check give ||B||=1 and ||B'||<36001. In particular the small closed-feedback VALUE was not differentiated: its derivative used S_o'<4e22 and decaying80-step powers. The actual inverse N and incoming amplitude used to prove its closed outgoing value obey N<1.000001 and ||u||<.490003, supplying b_C<3e-12; the inadequate coarser N<2,u<.5 product is not used.

The complete selected two-new-port scattering is exactly

    S_open=r_n I+t_c² B F_o,
    F_o=(I-r_o B)^-1.                               (6)

All phases and velocity conversions have already been retained; the two velocity factors cancel in this selected scattering matrix only. The physical flux coefficient is

    t_c=exp(iq) w0(1+r_o),
    w0=sqrt(S0 sin q/sin k).

Here w0<1.000003. Its logarithmic derivative is

    w0'/w0=(cot(q)q'-cot(k)k')/2,

so |w0'|<51 using |cot q|<5e-6, q'<189, |cot k|<2.5 and k'<40. Directly differentiating t_c gives

    |t_c'|<189*1.000003*(1+4.88e-6)
                    +51*(1+4.88e-6)+1.000003*230<500.

Flux conservation gives |t_c|<=1. Differentiating F_o with its true order yields

    F_o'=F_o(r_o' B+r_o B')F_o,
    ||F_o'||<(1.000005)²(230+4.88e-6*36001)<231.

Using(4), the derivative of(6) is bounded by

    ||S_open'||<1400+1000*1.000005
                              +36001*1.000005+231<39000. (7)

The desired P S' P is a subblock of this full selected two-port derivative, so s1<39000. Closed induced responses are incorporated in B; equation(7) does not identify the selected block with a source having its closed channels deleted.

## 5. Numerical consequence for the full input cap

Use the separately checked exact cap identity at ell=20, D=Q_new^21:

    Fcap=(I+D S D)^-1, alpha=-D Fcap/j.

Here S is the uncapped input-input block, not an already gate-loaded matrix. Fixed-projector bounds from its checked factorization are

    q=1/60, r0=4.81e-5, s0=1.3, N=21,
    rho=r0+s0(2q^N+q^(2N)), f=(1-rho)^-1<1.000049,
    d1=N/.0053<3963, c1=1/[.0027(60²-1)]<.104,
    K=2d1s0+s1+(2q^N+q^(2N))swide<49400.

For example 60^10>6e17 gives q^20<1/(3.6e35) and q^21<1/(2.16e37), so the swide contribution is <5e-15. The large generalized derivative is suppressed by actual cap powers, not assumed small. Thus

    ||alpha||<=f/j<371,
    ||alpha'||<=(d1 f+f² K)/j<2e7,
    ||C alpha||<=q^21 f/j<1.72e-35,
    ||C alpha'||<=[21q^20 c1 f+q^21 f² K]/j<8.6e-31. (8)

For the last ceiling, the numerator is <6.068e-36+2.288e-33 and j>.0027. These estimates apply to every endpoint-forcing coordinate, not merely selected input. For all input sites0<=n<=20, the exact canceled expression Q^-n alpha=-Q^(21-n)Fcap/j and its derivative remain available; no growing power is applied to the tiny unstructured C alpha bound. Outgoing products use beta=S alpha with beta'=S'alpha+S alpha' and can be bounded with the same fixed-projector decomposition as needed.

All statements hold separately on both physical old-energy windows and each conserved record/parity sector. The lower lip follows by fixed real conjugation or its own identical algebra. Passive references do not change operator norms. Hardware parameters and input vectors are held fixed when differentiating physical E.

## Scope and remaining derivative obligation

The selected old finite response derivative ||(Phi_old P)'||<5.1e11 is already separately checked, but its complementary-input counterpart is not established by that selected statement. The exact forced-old derivative still includes

    (Phi_old P)'Palpha+Phi_old P Palpha'
      +(Phi_old C)'Calpha+Phi_old C Calpha'.

Equation(8) makes its complementary coefficients explicit and small. It does not supply a value for ||(Phi_old C)'||, and multiplying an unproved derivative by a small coefficient would not close the proof. The old H_C' bound from the prepared converter source concerns complementary OLD-port incidence, not automatically complementary NEW-port incidence through both converters. A separate full propagation/product calculation is still required for that map. Output return, gate and cable derivatives are also separate. No full Lprime, background improvement, complete operating point, source robustness or native implementation follows from this note alone.

## Exposure and exact sources

I authored the prepared converter derivative and reviewed the new cap factorization; neither is independently recertified here. The cap factorization was root-authored and has my explicit distinct review. The prepared converter proof has a separate completed check, including its sharper b_C value clarification. Root requested the present numerical scattering derivatives without imposing a desired constant. I read the complete converter derivative source/check and complete two-converter composition, and reused the fully refreshed endpoint/wider-domain arguments from the immediately preceding cap check. This is new author derivation requiring a distinct check of(3)--(8), not a reviewed result by its author. Original physical source/filter and canonical analytic-disk premises remain conditional.

No scientific runner, numerical inverse, quadrature, dynamics, parameter sweep, Git/canonical/publication/checkpoint/prompt/model change or delegation occurred. Only this proposal was written.

- `input_cap_factored_forcing/PROPOSAL.md`: `95755c3a08b6434a7ec7f86897a80f975c7575be747d1a9f09cdf34c9cce4376`.
- `input_cap_factored_forcing_check/REVIEW.md`: `85ad12b8df4b15a4abeeded5b28e84d1413f9ab848122ca0e45e0e09eece66d3`.
- `prepared_converter_direct_derivative/PROPOSAL.md`: `a444e105c88fcfad8fcae59b7f72d9dd9247e2b83ada73edeb7b97a849b33653`.
- `prepared_converter_direct_derivative_check/REVIEW.md`: `283494e3a50b12b77bf9d4be184452b49b582627fac20c802087e00e4d69e11d`.
- `bandcenter_converter_composition/PROPOSAL.md`: `1cc6fec524a8184f844711a4fa6d72fcc7cd13a4c8b413cbc064cd4b2201df78`.
- `bandcenter_bandwidth_extension/PROPOSAL.md`: `d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2`.
- `bandcenter_converter_endpoint/PROPOSAL.md`: `22e7b4a9363a0c010ebce59f3235891708fd40eb5a5fa18f91b1a8878fe99c5a`.

Original canonical endpoint note: SHA256 `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`, including its finite analytic-disk premises; no recalibration performed.
