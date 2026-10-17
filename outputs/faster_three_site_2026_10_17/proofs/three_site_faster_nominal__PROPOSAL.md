# One faster nominal three-site complete-device certificate

Status: new authored conditional composition, requiring a distinct check. This evaluates only lambda=1e-12, g=5e-8, h=4e-6, T=2e13, M=5,000,000. It retains an absolute-background baseline and then applies the newly completed distinct background-IBP and cubic-cancellation checks. Under the exact original supplied physical/calibration and checked matching premises, the complete normalized-target operator error is <.00086 uniformly on [T,2T]. This is a sufficient analytical certificate, not measured error or native implementation.

## Physical construction and literal target

Keep the original calibrated j (in .0027<j<.003), J and shared internal B, with B iota=iota K on source vacuum, K=2I+Z1Z2. Set a1=lambda/sqrt(3), a2=lambda sqrt(8/3), kappa²=3jlambda. Thus kappa²<9e-15 and kappa<9.487e-8. No one-site-emitter restriction kappa<=1e-8 is imported: the emitter-free background and ordered three-site inverse are the applicable interfaces.

The nominal six-block installation is unchanged except these coefficients. The port p=(40,63,1), source s2=(40,64,1), s1=(40,65,1), s0=(40,66,1) have blocks

    j(n2+np)-kappa X_2p;
    a2(n1+n2-X_12); a1(n0+n1-X_01);
    (j-a2)n2; (2j-a1-a2)n1; (2j-a1)n0.

All are positive on the full physical space, all source diagonals equal 2j, and compression onto the old port retains j n_p. Shared B occurs once. There is no new vacuum scalar. These are the compensated nominal blocks, not the later seven-block phase-family reexpression. The exact scalar c_att=c_total+4(sqrt(2)-1)j remains that of the checked device.

The output sites are r_m=(100,3+m,2), m>=0, distinct from gate o=(100,2,2). The connector has hopping sqrt(jg), every slow site has diagonal 2j, and the finite last-site cap g n_last realizes exact principal compression. Geometry and all unchanged head-dependent processor terms are the checked attachment's, with no additional source contacts.

Define delta=-2j cos q=-2g cos k, k_old=2asin(sqrt(j/J)sin(q/2)), and

    q3(delta)=(delta²-lambda²/3)(delta-kappa² m_j(delta+i0))
                                          -(8lambda²/3)delta,
    F3(q)=kappa a1 a2 (2j sin q) zeta
                       exp[i61q+i172k_old]/(sqrt(2pi) j q3(delta)),
    t_f=exp[i(q+k)/2]sqrt(sin q sin k)/sin((q+k)/2),
    F_s(k)=t_f sqrt(g sin k/(j sin q)) F3(q).

The coefficient is restricted to |delta|<=d=2j sin h. Put p=int|F_s|²dk and

    beta_m(t)=1/sqrt(2pi) int F_s(k) exp[ikm-it(2j-2g cos k)]dk,
    r_phys(t)=||beta(t)||_(m>=0).

The complete comparator is

    exp(-it c_att) J_out[(beta(t)/r_phys(t)) tensor exp(-itK) W],
    W=[(9+12i)I+(-16+12i)X1X2]/25.

It has record1, source vacuum and the prescribed other blank registers. The packet is common to all old inputs and passive references, and keeps phase 61.5q+.5k+172k_old and the full complex q3. There is no fitted phase or time-dependent choice of waveform. The finite actual state is embedded in the same infinite output space for comparison; no extra truncation/renormalization of this target is performed. No full-apparatus commutation with K is assumed.

## Inverse, actual outside state and represented source

The exact original calibration gives 2.15e-8<d<2.4e-8 and d/g<.48. Set a0=8e-18, b0=46000/.0053+290/g<5.81e9, s=sqrt(1-3lambda/j). The unchanged full emitter-free kernel obeys ||G-G0||<a0+b0|delta|, G0=m_j(E-c_att-2j-B). Its complete wrong-window complements have the checked gap and inverse bounds. Ordered loading gives

    Theta=(j a0+kappa² b0)/s+6kappa²(a0+b0 d)<5.24e-5,
    c3=(1-Theta)s>.9999475.

Indeed the leading numerator is <2.4e-20+5.229e-5, the complementary term <7.53e-12, and 3lambda/j<1.112e-9. These are full-fiber conditions, on both physical lips, not scalar replacement of the interacting kernel. The actual matching and strict inverse margins provide the in-window seed boundary regularity needed for Stone. All spectral types outside the union of the two physical windows are retained below.

The exact installed sixth central moment is

    mu6=3lambda^6+(8/3)jlambda^5<8.00000001e-63.

The second term is the port-reaching third-hop contribution and cannot be dropped. For the prepared map V and common physical union I of the old-energy 1 and 3 windows,

    epsilon_sp=||E_H(I^c)V||<=sqrt(2mu6)/d³<1.3e-8.

This uses Cauchy-Schwarz over the two input energies, not orthogonality of the omitted outputs. It includes passive references and every outside spectral type. It is charged only once as an actual omitted state.

For the three represented source coordinates retain all three scalar amplitudes, whose rational norm is

    F(z)=exp(-z)sqrt[(1+z+z²/3)²+(z+z²)²/3+2z^4/9].

On z=lambda t>=20, F<7.3e-7: the polynomial norm at 20 is <344 and each polynomial times exp(-z) decreases thereafter; exp(-20)<148^-4<2.1e-9 follows from the finite Taylor lower bound for exp(5). The scalar finite-band density errors (source equation (6)), with eta=lambda/j<3.704e-10, C=6eta+9eta²<2.223e-9 and q=1-3eta, give E0,E1,E2<2.3e-9, hence E_vec<4e-9. Their rational exterior tails remain included.

The exact checked local interface retains

    D_sel=kappa² a1a2/[pi(1-Theta)] *
       [a0*pi/(2s² lambda³)+b0/(s² lambda²)
                            +(6/s)(2a0/lambda²+2b0/lambda)],
    D_wrong=170 kappa² a1a2/[pi(1-Theta)] *
       [(2a0/s)asinh(d/lambda)
        +(2b0/s)(sqrt(d²+lambda²)-lambda)+12a0d+6b0d²].

Using a1a2<.944lambda², pi>3.14, asinh(d/lambda)<14 and sqrt(d²+lambda²)-lambda<d gives D_sel<1.574e-5 and D_wrong<1.4e-34. For the latter the bracket is <280 and the prefactor <4.61e-37. The separate scalar-reference truncation eta_ref<=sqrt(2mu6)/d³<1.3e-8 is not a second actual omitted vector. Thus

    S_I<=F+E_vec+eta_ref+sqrt(2)D_sel+2D_wrong<.0000231.

This retains wrong-window inputs, both lips and all three source coordinates. Orthogonal record/parity sectors add no further factor.

## Absolute complete background and both traveling coefficients

The checked prepared recovery has L0<14000 on its full forcing domain, containing every remaining finite head and all slow closed tails. It excludes the three source sites and the propagating open output, so these components are not duplicated. Both physical windows and lips give the absolute bound

    B_I<=8sqrt(2) kappa L0/(3pi c3)<.0016.

For example sqrt(2)<1.415, pi>3.14, kappa<9.487e-8 and c3>.9999475 give this last inequality directly. This is the dominant term. It grows as sqrt(lambda); it is an estimate, not a residual lower bound. No derivative estimate, oscillatory cancellation or pending background IBP result is used.

For the exact RAW outgoing coefficient, the checked interface yields

    E_sel<=2.1e-13 sqrt(p)
        +[304/(2j cos h)+.302/g]lambda/sqrt(3)
        +1.384 Theta sqrt(p)/(1-Theta),
    B_wrong=170 kappa a1a2[2e-23+461Theta/(1-Theta)],
    E_wrong<=.006 B_wrong sqrt(2h),
    E_raw<=sqrt(2)E_sel+E_wrong.

Using sqrt(p)<=1, 304/(2j cos h)<56300 and 1/sqrt(3)<.578 gives E_sel<7.61e-5, E_wrong<1e-34 and 2E_raw<.000216. The term proportional to lambda uses the exact scalar second moment lambda²/3, while Theta includes the calibration floor and complementary forcing.

The real rectangular two-lip Stone identity gives the other traveling coefficient by fixed conjugation, preserving exp(-itE) at the physical energy. Its ideal old multiplier is W*, whereas outgoing has W. It has the same raw error allowance. Their physical halfline ranges can overlap, so both E_raw terms are paid by triangle, not orthogonal summation. Wrong-window input columns are already in this estimate.

## Separately checked integration-by-parts improvement at this point

The background IBP and nominal cubic-cancellation sources received distinct checks during this task. They are additional premises, fully read with their checks here. The absolute result above remains a valid baseline. We now recompute the general formula rather than scale its former numerical result.

For n=1/(1-Theta), A=3.00002, A_s=2/s+A/s² and Z_g=2e8+17000/g=3.402e11, the checked ordered prepared derivative gives

    D3 <= (c_a/lambda){n A pi/(2s²)
      +(3j n²/s)[A_s(4a0/3+2b0lambda/3)+400a0lambda²
                   +400b0lambda³+Z_g(pi lambda/(2s)+12lambda²)]},
    c_a=2sqrt(2)/3.

It is a per-window/lip supremum, including full prepared wrong-window columns. The cancellation only sharpens the exact selected q0 derivative; it leaves the complementary constants and the actual G derivative obligation intact. Here s>.9999999994, n<1.00005241, A_s<5.001. With pi<22/7 the first bracket term is <4.715; the next three terms are respectively <.019372, <3e-24 and <.53461. Their multiplier is <.009001, giving a correction <.004987. Thus D3<.944*(4.715+.004987)/lambda<4.46e12.

Retain the older checked FULL forcing recovery derivative, not a selected-only replacement:

    M_g=1.00068*(7.29e16+3.31e7/g)+30<7.37e16.

The full two-window, two-lip formula, including the hard-band endpoints, is

    B_IBP(t)=2kappa/(pi|t|) *
      [2c_a lambda²L0/(c3(d²+lambda²)^(3/2))
                                      +2c_a M_g/c3+L0 D3].

Its three bracket terms are <2700, <1.392e17, and <6.244e16, so their sum is <2.017e17. Using pi>3.14 and kappa<9.487e-8 yields, for t>=T,

    B_IBP(t)<[1.8974e-7/(3.14*2e13)]*2.017e17*(T/t)
             <.000610*(T/t).

Consequently the SAME represented-background map obeys min(B_absolute,B_IBP)<.000610 on [T,2T]. This does not differentiate a value bound: it uses the exact ordered product derivative and a Hilbert-valued Stone integration by parts. Each window has a fixed closed-channel projector embedded in the same physical output space; geometric closed tails and their derivatives are square summable. Both lips and both physical windows are paid by triangle and both hard edges remain. The full prepared D3 already includes complementary inputs, so no extra D3_C is added. The recovery-derivative term dominates this evaluated IBP bracket; improving only cubic cancellation does not remove it.

## Weighted reference time and one physical normalization

Use the checked weighted scalar time theorem with the proof cutoff D=g/4=1.25e-8<d. This is not a hardware change or a parameter search. Set

    alpha_D=sin(D/(2g))/(D/(2g)), m_D=s alpha_D³,
    delta_D=2g sin(D/(2g)), P=1/(4g)+102.78/(2j cos h)<5.02e6.

Here D/(2g)=1/8, so alpha_D>1-1/384 and m_D>.9922, delta_D>.997D. The exact old calibration, rather than merely a free choice of j in its interval, supplies k_old'<.24 and hence the stated physical phase ceiling. The weighted comparison retains

    E_c=[3lambda/j+P lambda/sqrt(3)
                     +lambda²(1/(4j²)+11/(8g²))]/m_D,
    E_disp(t)=|t|/(24g²) sqrt(16lambda^5 D/(3pi)),
    U<=sqrt(16/[15pi(1-3lambda/j)])(lambda/delta_D)^(5/2),
    V_D=sqrt(16/(15pi))(lambda/D)^(5/2),
    Z=(8/3)sqrt(16/(15pi))(lambda/(2pi g))^(5/2).

Using the indicated rational lower bounds, sqrt(3)>1.73 and pi>3.14 proves E_c<2.93e-6, E_disp(t)<9.8e-8 for t<=4e13, U<3.4e-11, V_D<3.4e-11 and Z<3e-14. Dispersion uses only the truncated sixth moment of the rational density, not its divergent full sixth moment. The two hard-band tails and lattice aliases are separate charges.

The exact transmitted mass satisfies

    0<=1-p<=mu6/d^6+lambda²/(3g²)<1.334e-10,
    1-sqrt(p)<7e-11.

The first term is scalar truncation; the second is physical reflection loss integrated against the exact second moment. No actual loaded seed density is substituted for this scalar measure. Therefore the normalized scalar comparison is

    E_w=E_c+E_disp+U+V_D+Z+1-sqrt(p)<3.1e-6.

The incoming normalized reference on m>=0 has norm <=E_w, so raw J_I<=sqrt(p)E_w<3.1e-6. On the outgoing side the cubic halfline bound has

    H(z)²=exp(-2z)[(2lambda/(3g))z^4
                     +(2/3)z^4+(4/3)z³+2z²+2z+1].

For 20<=z<=40 it is <(7.3e-7)² (the polynomial at 20 is <344² and its terms decrease after multiplication by exp(-2z)). Hence normalized reference mass on m<=0 has norm <3.9e-6, conservatively including the m=0 summand. Parseval gives

    r_phys>=sqrt(p)sqrt(1-(3.9e-6)²)>0,
    1-r_phys<1e-10.

Only this one physical-halfline normalization is charged in the final synthesis. The 1-sqrt(p) within E_w is the scalar comparison's own normalization, not a second raw traveling-error normalization. None of these finite-interval estimates asserts an all-late-time uniform bound.

## Exact receiver cut and complete sum

All source, old processor, converter and gate sites, including r0, have weight zero. Only output g edges change weight. The weighted imaginary-generator row bound is 2g sinh(a), including every internal fiber and all scalar/load terms. The cap above is exact compression. The one-cut Duhamel comparison consequently gives, uniformly through 2T,

    epsilon_cut<1.2 exp[-M+4gT sinh(1)].

Here 4gT=4,000,000. The elementary sinh(1)<1.176 implies the exponent <-296,000, so epsilon_cut<1e-10. This compares complete actual evolutions and does not project onto successful outputs or assume no returns.

First, the checked complete traveling/local decomposition using only the absolute background gives

    epsilon_complete <= epsilon_sp+S_I+B_I+2E_raw+J_I
                                           +(1-r_phys)+epsilon_cut
      < .000000013+.0000231+.0016+.000216+.0000031
                                      +.0000000001+.0000000001
      = .0018422132 < .00185.

Using the additional checked IBP row replaces only .0016 by .000610 and proves

    epsilon_complete<.0008522132<.00086.

Both bounds hold for every t in [2e13,4e13] in full operator norm, including arbitrary passive references and every apparatus output. The single actual omitted state is outside all represented terms. For the stronger epsilon=.00086 comparator, failure effect is <epsilon² I=7.396e-7 I, hence success >.9999992604. The normalized successful-vector distance is <epsilon+1-sqrt(1-epsilon²)<.000861. Complete channel and successful subnormalized CP-map diamond errors are <2epsilon=.00172; conditioning normalized outputs does not define a linear channel.

## Resources, comparison and limits

The unchanged nominal installation has M+238 heads, M+243 physical qubits, M+239 head edges and 2M+281 unmerged positive blocks: respectively 5,000,238; 5,000,243; 5,000,239; 10,000,281. Compared with the checked lambda=1e-13, T=2e14, M=50,000,000 certificate, the selected onset and receiver length decrease tenfold while this sufficient complete ceiling weakens from .0006 to .00086 (or .00185 if only the absolute-background baseline is used). The weighted reference method differs as well; no claim is made about exact error ordering or the best operating time of either device. Compared with PR9679's earlier .00191 complete certificate at T=1e15 and M=250,000,000, these sufficient onset/receiver counts are fiftyfold lower with the same type of complete metric. This is a different source and waveform, not a same-hardware speed limit or empirical improvement.

Changing lambda preserves lambda*T=20 but does not preserve the total budget: Theta and selected coefficient/local errors scale mainly as lambda, the actual omitted amplitude as lambda^(5/2), background as sqrt(lambda), phase cost as lambda/g, dispersion at fixed lambda*T as (lambda/g)^(3/2), tails as (lambda/g)^(5/2), and transmission deficit as (lambda/g)². Calibration floors remain in the explicit formulas. Positivity, exact supplied correlations, original native interaction and preparation/readout identification, physical time units and scalar phase remain premises. One chosen read in this window is certified; irreversible halt/storage, repeated monitoring, native coefficient generation and arbitrary hardware robustness are not.

## Exposure and verification record

Root supplied this single scaling test, not an error target. I authored scalar/source/time and other ancestors, checked weighted-time and outgoing/traveling components, and authored earlier recovery/derivative work. This composition is author work with shared ancestry, not independent recertification of those premises. The candidate and its distinct check, weighted theorem/check and scalar density argument were fully refreshed; unchanged exact component arguments are reused at their checked scopes from prior complete reads. A distinct review of this new point remains required. The new IBP and cubic-cancellation sources/checks were read in full after their distinct reviews completed; no still-pending improvement was imported. No scientific runner, quadrature, dynamics, sweep, optimization, external search, W/Git/PR/checkpoint/prompt/model change or delegation was used. Only this proposal was created. The source pins below identify evidence, not additional proof checks.

- `three_site_complete_candidate/PROPOSAL.md`: `b64b5a073aeedf47c8d1f3b604763af43edd0ac0d61ac572638a6bfac2ab0e5a`.
- `three_site_complete_candidate_check/REVIEW.md`: `b660546cf354778d99dc08c7277e386069aa62ab9ef9efba5fb44596a19cc821`.
- `three_site_weighted_reference_time/PROPOSAL.md`: `d41e468ffec769a9f5a36a7796999366fddf04ff2b42c1a8083c20e46f243d36`.
- `three_site_weighted_reference_time_check/REVIEW.md`: `809c0e0b452b4d913d5750f3aa184473c4d4b20132de7a73b919e8d0be5415ac`.
- `three_site_product_source/PROPOSAL.md`: `a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823`.
- `three_site_product_source_check/REVIEW.md`: `c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b`.
- `three_site_actual_attachment/PROPOSAL.md`: `4278633f3436008a770088331a2424d3f42dda06d08853dfe18d9b8a6554f006`.
- `three_site_actual_attachment_check/REVIEW.md`: `ede902f9c1bebc768147e459894f98610689f33655f87d01d91d07531cbd157d`.
- `three_site_loaded_inverse/PROPOSAL.md`: `7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672`.
- `three_site_loaded_inverse_check/REVIEW.md`: `8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2`.
- `three_site_local_escape/PROPOSAL.md`: `0340895610d3a5ef709dd8a03c1bc5872c8f34cf00f21053c00adcc3d706468d`.
- `three_site_local_escape_check/REVIEW.md`: `e19767c8092fb856a3c24cb279f621deea38d69d65c41bef4a1aea44bad23074`.
- `three_site_outgoing/PROPOSAL.md`: `af580b44fc2ebfc35eb014ffc63b8bae17464150677ede4a8b8315886f6f36ac`.
- `three_site_outgoing_check/REVIEW.md`: `721a183db3e42527d7cb5bdda697e6c6d81312a94cf047dd7ea15897cb4c2f02`.
- `three_site_traveling_interface/PROPOSAL.md`: `75b1ba68fae3f34e54c15df80b3a39a165240b1759f8fc84eb2b24677cc7f9e3`.
- `three_site_traveling_interface_check/REVIEW.md`: `9cb7655b688a61ce32b950f2d95024762023770380a6e5df8afaa1939744230a`.
- `prepared_core_recovery/PROPOSAL.md`: `cce29994b7141df161ca12f377765fdaf760f7e64fc56043bbf370e2cd437ea9`.
- `prepared_core_dwell_check/REVIEW.md`: `88274b8b49e583bdb9b5f933f7406b1a96a6ca79049e57b83e8030c834d16819`.
- `three_site_reference_time/PROPOSAL.md`: `d21632c8660f92e9478433bb564b357fe623aaa86c465d82537cfb28b77b315f`.
- `three_site_reference_tail/PROPOSAL.md`: `92a14fa12ccb489bfe311278683b6aa12b67b6549449273ba181383f5f779fb1`.
- `three_site_reference_time_check/REVIEW.md`: `0439d990a12b51561257038b1ef14aeb88302adf12bb546de0f00571ac44a553`.
- `output_lead_weight/PROPOSAL.md`: `58f99248986aebe14b4cd87f46237a293ed0c86ab720dd37a497c5b2a64a06cf`.
- `output_lead_weight_check/REVIEW.md`: `1c72e347fed86c96fcc491c550c136d08f3b7720d52ec1534af94066056d59dd`.
- `slow_lead_wide_publication/NOTE.md`: `feec1a7b2d48b758c86d5bdcde4ef0043a3b51ee09fb773024fbd7fd52d5bb38`.

Original canonical endpoint premise: `docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md`, SHA256 `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`; not recalibrated here.
- `prepared_core_composition_check/REVIEW.md`: `52edba6061be49eef40b5c06754a7425b5f7f62671f175cc72a093d4a60de65c`.
- `prepared_background_ibp/PROPOSAL.md`: `90d42e3699496e7694ddda630672af778a506b795865118757ab1e57da4a9c5a`.
- `prepared_background_ibp_check/REVIEW.md`: `5c4c1e2b8930be39195181681c563cd0c150611ad07a201316f3096e5a55ea12`.
- `three_site_cubic_derivative_cancellation/PROPOSAL.md`: `d57ca3702567780319131cdcadd824588364b93d77575e26b56e00565fd292ac`.
- `three_site_cubic_derivative_cancellation_check/REVIEW.md`: `c65696bec16ece9a1080fd24100fb8d7130821f76136f35810d3d148c155d5d4`.
- `three_site_prepared_inverse_derivative/PROPOSAL.md`: `25052bad1d500f52d4e4f4d3913f0bf8a0a57d69801688b7109a549ac3756d84`.
- `three_site_prepared_inverse_derivative_check/REVIEW.md`: `3a76d76895c01dcbd7cf7e5b566f7146ae683ddc4568352df06c19224e59aa1c`.
