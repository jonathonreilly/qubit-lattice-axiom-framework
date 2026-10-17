# One complete nominal point using the checked factored recovery derivative

Status: new authored conditional composition requiring a distinct check. Evaluate ONLY

    lambda=2e-12, g=5e-8, h=4e-6,
    T=1e13, M=2,500,000, Delta=0.

Under the original supplied physical/calibration, preparation and checked matching premises, the complete finite-device normalized-target operator error is <.00076 uniformly on [T,2T]. No desired error was assumed. The checked full recovery/action sources replace the former coarse Lprime in the background integral; every other lambda-dependent budget is recomputed below. No sweep, optimization or publication is performed.

## 1. Actual hardware, carrier and common comparator

Keep the ORIGINAL calibrated j in .0027<j<.003 and J=.030021107107032, not a newly chosen value in that interval. Install a1=lambda/sqrt(3), a2=lambda sqrt(8/3), kappa²=3jlambda. Thus kappa²<1.8e-14 and kappa<1.342e-7. The old one-site emitter restriction kappa<=1e-8 does not apply to this three-site source or its emitter-free background.

Use the same compensated six-block source at p=(40,63,1), s2=(40,64,1), s1=(40,65,1), s0=(40,66,1):

    j(n_s2+n_p)-kappa X_s2,p;
    Q_a2(s1,s2), Q_a1(s0,s1);
    (j-a2)n_s2, (2j-a1-a2)n_s1, (2j-a1)n_s0,
    Q_a(u,v)=a(n_u+n_v-X_uv).

All coefficients of the occupations are positive. The first block has eigenvalues0,j-kappa,j+kappa,2j and is PSD; the Q blocks are PSD. Source diagonals remain2j and compression off the three source heads leaves exactly the preexisting j n_p load. No second port cap, new vacuum scalar or replicated shared source is added. The head begins at s0, with source vacuum, computational record0 and otherwise prescribed blank apparatus, and arbitrary old/reference input. Shared B is included once and satisfies B iota=iota K on that preparation. The interacting full H need not commute with K.

Retain the slow connector sqrt(jg), the occupations preserving diagonal2j, and output sites r_m=(100,3+m,2), m>=0, beyond distinct gate o=(100,2,2). Retaining M sites with cap g n_r(M-1) gives exact principal compression. All original source/filter/converter/gate terms and selective installation remain premises. This is the nominal six-block family, not a later tolerance/mediator or seven-block reexpression.

The target keeps literally

    K=2I+Z1Z2, W=[(9+12i)I+(-16+12i)X1X2]/25,
    c_att=2nu+2beta+4gamma_J+4gamma_c+4(sqrt(2)-1)j.

Let d=2j sin h, delta=-2j cos q=-2g cos k and k_old(q)=2asin(sqrt(j/J)sin(q/2)). On the selected hard band |delta|<=d define

    q3(delta)=(delta²-lambda²/3)(delta-kappa²m_j(delta+i0))
                                                -(8lambda²/3)delta,
    F3(q)=kappa a1a2(2j sin q) zeta exp[i61q+i172k_old(q)]
                                            /[sqrt(2pi)j q3(delta)],
    t_f=exp[i(q+k)/2]sqrt(sin q sin k)/sin((q+k)/2),
    F_s(k)=t_f sqrt(g sin k/(j sin q)) F3(q(k)),
    p=int |F_s|²dk,
    beta_m(t)=1/sqrt(2pi) int F_s(k)exp[ikm-it(2j-2g cos k)]dk,
    r(t)=||beta(t)||_(m>=0).

The common comparator is exp(-it c_att) Jout[(beta/r) tensor exp(-itK)W], with source vacuum, record1 and all prescribed other registers. The physical phase61.5q+.5k+172k_old, complex q3, first slow site m=0, flux factor and Jacobian are unchanged in definition but evaluated at this lambda. No fitted phase or per-input waveform is allowed. The finite actual state is embedded into the same infinite comparison space; no extra truncation or normalization of the target tail is performed. Positivity of r is proved below.

## 2. Changed full inverse and actual omitted state

Here 2.15e-8<d<2.4e-8, d/g<.48, lambda/j<7.408e-10<1/16. Keep a0=8e-18 and b0=46000/.0053+290/g<5.81e9. The checked emitter-free full kernel has ||G-m_j(D_old)||<a0+b0|delta|, D_old=E-c_att-2j-B, including its complementary channels. For s=sqrt(1-3lambda/j), the ordered three-site loading criterion gives

    Theta=(j a0+kappa²b0)/s+6kappa²(a0+b0d)<1.048e-4,
    s>.9999999988, n=(1-Theta)^-1<1.00010482,
    c3=(1-Theta)s>.9998951.                         (1)

The leading numerator is <2.4e-20+1.0458e-4 and the complementary term <1.507e-11. The actual denominator Q=(D_old²-a1²)(D_old-kappa²G)-a2²D_old retains its noncommuting order. Its inverse is bounded by1/[c3(delta²+lambda²)^(3/2)]. Both lips, wrong-window input and closed inverse columns remain. Matching/root continuation and nonzero finite inverses supply in-window seed regularity; a matrix value bound alone would not eliminate singular seed measure.

The installed, not scalar-surrogate, sixth moment is

    mu6=3lambda^6+(8/3)jlambda^5<2.56000001e-61.

Its port-reaching term is retained. For the common union of the physical windows centered at c_att+2j+1 and c_att+2j+3, the full prepared map V obeys

    epsilon_sp=||E_H(I^c)V||<=sqrt(2mu6)/d³<7.3e-8.   (2)

For example2mu6<5.12000002e-61 while(7.3e-8)²(2.15e-8)^6 exceeds5.2e-61. This pays every outside spectral type, including atoms and trapped modes. The two omitted images are not assumed orthogonal; sqrt(2) is the input Cauchy-Schwarz cost. It is charged ONCE as an actual outside vector, including passive references.

## 3. All three represented source coordinates

The scalar reference's weighted-density formulas, with eta=lambda/j and C=6eta+9eta²<4.445e-9, give E0,E1,E2<4.6e-9, hence E_vec<8e-9. These formulas include finite-band and rational exterior errors; no exact Markov replacement occurs. For z=lambda t>=20, the same joint three-source rational norm

    F(z)=exp(-z)sqrt[(1+z+z²/3)²+(z+z²)²/3+2z^4/9]

is <7.3e-7. Its polynomial norm at20 is<344 and each term times the exponential decreases; exp(5)>148 supplies an elementary exponential witness.

The exact checked local Stone allowances are

    D_sel=kappa²a1a2/[pi(1-Theta)] *
      [a0*pi/(2s²lambda³)+b0/(s²lambda²)
                               +(6/s)(2a0/lambda²+2b0/lambda)],
    D_wrong=170kappa²a1a2/[pi(1-Theta)] *
      [(2a0/s)asinh(d/lambda)
       +(2b0/s)(sqrt(d²+lambda²)-lambda)+12a0d+6b0d²].

Using a1a2<.944lambda², pi>3.14, asinh(d/lambda)<14 and sqrt(d²+lambda²)-lambda<d gives

    D_sel<3.149e-5, D_wrong<1.1e-33.

For D_sel its dominant term is bounded by1.8e-14*.944*5.81e9/[3.14(1-1.048e-4)s²], with all other terms retained inside the displayed margin. For D_wrong the bracket is<280 and prefactor<3.69e-36. The scalar reference truncation eta_ref<=sqrt(2mu6)/d³<7.3e-8 is distinct from the single actual omitted state. Thus, using sqrt(2)<1.415,

    S_I<=F+E_vec+eta_ref+sqrt(2)D_sel+2D_wrong<.000046. (3)

Both physical lips and full wrong-window inputs are included; orthogonal record/parity sectors add no extra multiplier. This controls all three source heads, not only seed return.

## 4. Recomputed D3 and complete background IBP

The full recovery derivative is now supported by the completed factored-recovery and gate-action reviews:

    M_g=1.00068[2.9e14+1.28e6/g]+30<3.159e14.         (4)

This includes all235 finite heads and complete slow closed tails on the full forcing domain. The gate's B invariance is local; no source commutation is imported. All input-cap, gate and closed-root derivatives were paid in its proof. The former selected-only derivative and the contextual unchecked53f571b6 result are not numerical substitutes.

Retain L0=14000, c_a=2sqrt(2)/3<.944 and the checked nominal cancellation A=3.00002. Put A_s=2/s+A/s²<5.001 and Z_g=2e8+17000/g=3.402e11. The full prepared inverse derivative still has the explicit envelope

    D3 <= (c_a/lambda){n A pi/(2s²)
      +(3j n²/s)[A_s(4a0/3+2b0lambda/3)+400a0lambda²
                   +400b0lambda³+Z_g(pi lambda/(2s)+12lambda²)]}.

This includes wrong-window induced selected output and all complementary forcing. No separate D3_C is added. The physical G derivative premise Z_g is unchanged, not derived from the improved Lprime by circular reasoning. With pi<22/7, the leading bracket term is<4.716; the three interior terms are respectively<.038744,<2e-23,<1.06922; the multiplier is<.009002. Their product is<.00998. Consequently

    D3<.944*(4.716+.00998)/(2e-12)<2.24e12.           (5)

The exact lip background column is -kappa a1a2 L Q^-1 V_seed. Hilbert-valued integration by parts keeps both hard endpoints, both physical windows and both lips:

    B_IBP(t)<=2kappa/(pi|t|) *
      [2c_a lambda²L0/(c3(d²+lambda²)^(3/2))
                                      +2c_a M_g/c3+L0D3].

The bracket terms are<10700,<5.965e14 and<3.136e16, so the sum is<3.196e16. Therefore for t>=T,

    B_IBP(t)<[2.684e-7/(3.14e13)]*(3.196e16)*(T/t)
              <.000274*(T/t).                       (6)

The absolute alternative remains8sqrt(2)kappa L0/(3pi c3)<.00227, but(6) is used. The full inverse-derivative term L0D3 now dominates the IBP bracket. Finite core and closed slow tails occupy fixed per-window physical subspaces, with differentiable square-summable lifts. Their ranges are embedded in the common output space before adding the windows. There is no unproved vector Riemann-Lebesgue step, moving basis or presumed source strip. The actual outside vector is not appended inside(6).

## 5. Both raw traveling errors

The exact outgoing coefficient interface supplies

    E_sel<=2.1e-13 sqrt(p)
      +[304/(2j cos h)+.302/g]lambda/sqrt(3)
      +1.384Theta sqrt(p)/(1-Theta),
    B_wrong=170kappa a1a2[2e-23+461Theta/(1-Theta)],
    E_wrong<=.006B_wrong sqrt(2h),
    E_raw<=sqrt(2)E_sel+E_wrong.

Using sqrt(p)<=1,304/(2j cos h)<56300 and1/sqrt(3)<.578 gives E_sel<1.523e-4 and E_wrong<1e-33. Therefore

    2E_raw<.000432.                                 (7)

The second-moment term uses the exact lambda²/3, not an unchanged prior numerical moment. Real physical rectangular Stone columns give the incoming coefficient by fixed conjugation while preserving exp(-itE) on each physical window. Its ideal old multiplier is W*, not W. Wrong-window columns remain in both allowances; the two traveling errors can overlap on the physical halfline, so they cost2E_raw by triangle. These are RAW errors, without another spectral normalization charge.

## 6. Weighted reference, exact hard tails and physical normalization

Choose the same proof cutoff D=g/4=1.25e-8<d; this is not a new hardware control or a sweep. With alpha_D=sinc(D/(2g)), delta_D=2g sin(D/(2g)), m_D=s alpha_D³, one has alpha_D>383/384, delta_D>.997D and m_D>.9922. The original calibrated phase map gives

    P_safe=1/(4g)+102.78/(2j cos h)<5.02e6.

This bounds the derivative of61.5q+.5k+172k_old in x=2g(k-pi/2), preserving its actual phase. The checked weighted comparison uses

    E_c=[3lambda/j+P_safe lambda/sqrt(3)
                   +lambda²(1/(4j²)+11/(8g²))]/m_D,
    E_disp(t)=|t|/(24g²)*sqrt(16lambda^5D/(3pi)),
    U<=sqrt(16/[15pi(1-3lambda/j)])(lambda/delta_D)^(5/2),
    V_D=sqrt(16/(15pi))(lambda/D)^(5/2),
    Z_alias=(8/3)sqrt(16/(15pi))(lambda/(2pi g))^(5/2).

Direct elementary substitution, with pi>3.14, gives

    E_c<5.86e-6, E_disp(t)<2.78e-7 for t<=2e13,
    U<2e-10, V_D<2e-10, Z_alias<1.7e-13.

Dispersion uses the TRUNCATED sixth moment16lambda^5D/(3pi) of the cubic density; its divergent full sixth moment is never used. The physical raw tail threshold is delta_D, the rational tail threshold is D, and the integer-lattice aliases have period4pi g. None is omitted or identified with the actual seed's outside state.

Scalar transmission loss and truncation give

    1-p<=mu6/d^6+lambda²/(3g²)<5.335e-10,
    1-sqrt(p)<2.7e-10.

Consequently the normalized scalar comparison E_w=E_c+E_disp+U+V_D+Z_alias+1-sqrt(p) is<6.2e-6. The conjugate cubic sequence vanishes on m>=0 at positive time; hence the RAW scalar incoming norm is sqrt(p)E_w<6.2e-6.

The outgoing negative-halfline comparison has

    H(z)²=exp(-2z)[(2lambda/(3g))z^4
                   +(2/3)z^4+(4/3)z³+2z²+2z+1].

At20<=z=lambda t<=40 the polynomial at20 is still<344², and each term times exp(-2z) decreases. Thus H<7.3e-7 and the stronger excluded set m<=0 has norm<H+E_w<7e-6. Parseval yields

    r(t)>=sqrt(p)sqrt(1-(7e-6)²)>0,
    1-r(t)<2.7e-10+(7e-6)²/[1+sqrt(1-(7e-6)²)]<3e-10. (8)

This is the one physical target normalization used in the complete map. The1-sqrt(p) inside E_w is part of its scalar comparison proof, not another normalized outgoing-error summand. No actual output is normalized, and no uniform all-late-time scalar claim is inferred from this finite-horizon estimate.

## 7. Exact finite cut and complete conclusion

Use zero position weight on all upstream/source/gate heads and r0, with weight m on r_m. Only receiver g bonds change weight. The imaginary weighted-generator bound2g sinh(a), exact cap compression and one retained-to-omitted cut give

    epsilon_cut<1.2exp[-M+4gT sinh(1)], 0<=t<=2T.

Here4gT=2,000,000 and sinh(1)<1.176, so the exponent is<-148,000 and epsilon_cut<1e-10. Every spectral component, internal channel and return is included; no absorbing boundary or successful-branch projection is used.

The full complete comparison is therefore

    ||J_M exp(-itH_M)V_M-Tnorm(t)||
       <=epsilon_sp+S_I+B_IBP+2E_raw+J_raw+(1-r)+epsilon_cut
       < .000000073+.000046+.000274+.000432+.0000062
                                     +.0000000003+.0000000001
       =.0007582734 <.00076,
                         every t in [1e13,2e13].     (9)

Both old-energy inputs, all physical outputs and arbitrary passive references are retained. The single actual omitted state is charged once globally. Upper time endpoints are used in dispersion and cut; lower endpoints in source escape and IBP. Thus(9) is an interval theorem, not an estimate at only one time.

For epsilon=.00076, the ideal comparator lies entirely in record1. Complete norm error gives failure effect<epsilon²I=5.776e-7 I and success>.9999994224. Normalized successful-vector distance is<epsilon+1-sqrt(1-epsilon²)<.000761. Complete-channel and successful SUBNORMALIZED CP-map diamond errors are<2epsilon=.00152. Normalized conditioning is nonlinear and is not assigned a linear-channel diamond claim.

## 8. Inventory, comparison and explicit limits

The same nominal graph has M+238 heads, M+243 physical qubits, M+239 head edges and2M+281 unmerged positive blocks. At this point these are2,500,238;2,500,243;2,500,239;5,000,281. Shared old/source/record qubits are counted once; passive references are excluded.

The PR9685 nominal certificate used lambda=1e-12, T=2e13, M=5,000,000 and complete ceiling.00086. This proposed point halves its onset scale and receiver sites and has the smaller sufficient ceiling.00076, using the newly checked structural derivative improvement. Total qubit ratios include their fixed offsets. The Hamiltonian source coefficients and exact packet change; these are not equal-hardware measurements, an optimum, a lower bound on the prior device's time, or proof of actual error ordering. No other point was evaluated.

Holding lambda*T=20 does not make the estimates invariant. Relative to9685, actual moment amplitude grows roughly lambda^(5/2), selected load/local/coefficient costs roughly lambda, the weighted phase cost lambda/g, dispersion at fixed lambda*T roughly(lambda/g)^(3/2), and transmission deficit(lambda/g)². Absolute background scales as sqrt(lambda), whereas IBP splits into kappa M_g/T and kappa L0D3/T. Both terms were reevaluated; the new M_g follows from checked physical derivative identities, not numerical scaling of an old allowance. Nonzero calibration floors remain in a0 and the coefficient formulas.

Original exact calibration, correlated supplier coefficients, local selective interactions, source-vacuum/product/record preparation, native Hamiltonian/Record identification and physical time units remain premises. No tolerance/common-offset/mediator result, arbitrary noise model, native supplier, irreversible storage, permanent halt, repeated monitoring or reset/reuse is imported. The promise is a single chosen read in the finite interval.

## Exposure and verification status

I authored the new point and the factored derivative/action sources, along with several scalar/source/time ancestors, and checked related interfaces. The full derivative review and root action review were read completely here; their completed identities resolve the historical pending labels in those sources. The complete9685 point review was read, with the initially truncated middle recovered in separate reads. Its local prose qualifications about the absolute baseline versus IBP scaling are retained here. Unchanged exact source/local/outgoing/traveling/weighted-reference arguments and scoped checks are reused from prior complete reads at their verified identities. This is author composition requiring its own distinct check, not self-certification or blind/model-diverse review.

No scientific runner, numerical inverse, quadrature, dynamics, parameter sweep, optimization, Git/canonical/publication/checkpoint/prompt/model change or delegation occurred. Only this proposal was created. The source identities below record the actual inputs, not additional proof checks.

- `prepared_gate_load_action/PROPOSAL.md`: `89f04354d21d2ff9cb996dade6f1f92afb0f3f584ead81037978bc53055f5252`.
- `prepared_gate_load_action_check/REVIEW.md`: `fb5967fae2d36ba44dd8de92321b77ad5b78286e22a66a6ff5582b7d7b673275`.
- `prepared_full_recovery_factored_derivative/PROPOSAL.md`: `09606913b6bd71637b089ded04180b3afa6934ae39fa85926cb05d4e1f69423a`.
- `prepared_full_recovery_factored_derivative_check/REVIEW.md`: `1a00c38e88361c0ca0e825ee4e339f5c419c1d9a16ec4d6495e34802d0835244`.
- `three_site_faster_nominal/PROPOSAL.md`: `48cdce93fd998d94334182866a37d29bf69b674f58d84dd653e9cea5590f1263`.
- `three_site_faster_nominal_check/REVIEW.md`: `f28828c93e59f281ae2a8d813ba3d6a88b4088bbbb855fcc265a6e88e0dee433`.
- `prepared_background_ibp/PROPOSAL.md`: `90d42e3699496e7694ddda630672af778a506b795865118757ab1e57da4a9c5a`.
- `prepared_background_ibp_check/REVIEW.md`: `5c4c1e2b8930be39195181681c563cd0c150611ad07a201316f3096e5a55ea12`.
- `three_site_cubic_derivative_cancellation/PROPOSAL.md`: `d57ca3702567780319131cdcadd824588364b93d77575e26b56e00565fd292ac`.
- `three_site_cubic_derivative_cancellation_check/REVIEW.md`: `c65696bec16ece9a1080fd24100fb8d7130821f76136f35810d3d148c155d5d4`.
- `three_site_prepared_inverse_derivative/PROPOSAL.md`: `25052bad1d500f52d4e4f4d3913f0bf8a0a57d69801688b7109a549ac3756d84`.
- `three_site_prepared_inverse_derivative_check/REVIEW.md`: `3a76d76895c01dcbd7cf7e5b566f7146ae683ddc4568352df06c19224e59aa1c`.
- `three_site_actual_attachment/PROPOSAL.md`: `4278633f3436008a770088331a2424d3f42dda06d08853dfe18d9b8a6554f006`.
- `three_site_actual_attachment_check/REVIEW.md`: `ede902f9c1bebc768147e459894f98610689f33655f87d01d91d07531cbd157d`.
- `three_site_product_source/PROPOSAL.md`: `a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823`.
- `three_site_product_source_check/REVIEW.md`: `c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b`.
- `three_site_loaded_inverse/PROPOSAL.md`: `7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672`.
- `three_site_loaded_inverse_check/REVIEW.md`: `8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2`.
- `three_site_local_escape/PROPOSAL.md`: `0340895610d3a5ef709dd8a03c1bc5872c8f34cf00f21053c00adcc3d706468d`.
- `three_site_local_escape_check/REVIEW.md`: `e19767c8092fb856a3c24cb279f621deea38d69d65c41bef4a1aea44bad23074`.
- `three_site_outgoing/PROPOSAL.md`: `af580b44fc2ebfc35eb014ffc63b8bae17464150677ede4a8b8315886f6f36ac`.
- `three_site_outgoing_check/REVIEW.md`: `721a183db3e42527d7cb5bdda697e6c6d81312a94cf047dd7ea15897cb4c2f02`.
- `three_site_traveling_interface/PROPOSAL.md`: `75b1ba68fae3f34e54c15df80b3a39a165240b1759f8fc84eb2b24677cc7f9e3`.
- `three_site_traveling_interface_check/REVIEW.md`: `9cb7655b688a61ce32b950f2d95024762023770380a6e5df8afaa1939744230a`.
- `three_site_weighted_reference_time/PROPOSAL.md`: `d41e468ffec769a9f5a36a7796999366fddf04ff2b42c1a8083c20e46f243d36`.
- `three_site_weighted_reference_time_check/REVIEW.md`: `809c0e0b452b4d913d5750f3aa184473c4d4b20132de7a73b919e8d0be5415ac`.
- `output_lead_weight/PROPOSAL.md`: `58f99248986aebe14b4cd87f46237a293ed0c86ab720dd37a497c5b2a64a06cf`.
- `output_lead_weight_check/REVIEW.md`: `1c72e347fed86c96fcc491c550c136d08f3b7720d52ec1534af94066056d59dd`.

Canonical original endpoint source remains `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`; no recalibration performed.
