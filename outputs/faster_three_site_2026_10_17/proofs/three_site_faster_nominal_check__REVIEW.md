# Distinct check of the faster nominal three-site complete point

Disposition: **conditional support for the complete bound, with two nonblocking prose qualifications below.** The specified point

    lambda=1e-12, g=5e-8, h=4e-6,
    T=2e13, M=5,000,000

obeys the proposed complete operator-error ceiling <.00086 at every t in [T,2T], under the retained exact physical, calibration, preparation and checked matching premises. Reconstructing the individual allowances gives the displayed sum <.0008522132. The alternative absolute-background sum <.0018422132 is also valid. No necessary change to a numerical allowance, physical block, waveform or time interval was found.

The complete reviewed source is `three_site_faster_nominal/PROPOSAL.md`, 20,591 bytes, SHA256 `48cdce93fd998d94334182866a37d29bf69b674f58d84dd653e9cea5590f1263`. This is a distinct, source-exposed check of the new composition and changed point. I authored the earlier large-receiver composition and prepared-core recovery, and checked the background IBP interface. Those are not independently revalidated by this review. Their separate checks are reused at exact identities. In particular the new cubic cancellation has its own distinct check; my prior IBP review did not include it. The present work reconstructs its substitution and the new point arithmetic, rather than treating the earlier .000134 component evaluation as applicable here.

## 1. Hardware, domain and the complete target

The six source blocks are the nominal compensated installation. The structured port block has eigenvalues 0, j-kappa, j+kappa and 2j on its two physical qubits, so it is positive because kappa<j. The other two exchange blocks have eigenvalues 0 and 2a_i, and all three remaining occupation coefficients are positive. At the new point a1+a2<3e-12 and a2<2e-12, while j>.0027. The source diagonals are exactly 2j. Compressing away the three source heads leaves exactly j n_p, preserving the emitter-free background and its full internal forcing space. The old one-site restriction kappa<=1e-8 is not needed by that unchanged background; the relevant source condition is the full three-site inverse margin checked below.

The coordinates and installed edge set are unchanged. The source extension introduces no new contacts, copies of B or vacuum scalar. The internal identity B iota=iota K is used on the supplied source vacuum only. It does not assert [H,K]=0 for the interacting apparatus. The positive receiver connector and last-site cap retain the prescribed 2j receiver diagonals and exact compression. This remains a supplied local Hamiltonian and product-seed construction, with exact correlated coefficients; no native supplier or robustness theorem is obtained.

The new point satisfies lambda<=1e-8, g<=1e-6, h<=4e-6, lambda/j<1/16 and d/g<.48<1/2. The lower estimate d>2.15e-8 follows from j>.0027 and sin h>=h-h^3/6; the upper is d<2.4e-8. The actual calibrated j and J remain fixed, not selected afresh within their enclosures.

The coefficient F_s is precisely the three-site scalar comparator: its physical source factor is a1a2/q3, its slow Jacobian is dq/dk=g sin k/(j sin q), and its flux multiplier is t_f. Multiplying the stated phases gives 61.5q+.5k+172k_old, with the full phase of 1/q3 still present. The extra source heads do not introduce an independently chosen propagation shift. In particular m=0 is the first slow site, not the old gate port, and 61 fast-chain phases are not 61 slow-site translations.

The normalized target uses the exact physical-halfline norm r_phys(t) of the fixed evolved packet. It retains exp(-it c_att), the 2j carrier inside beta, literal exp(-itK)W, record1, source vacuum, the other prescribed registers and every passive reference. The two W eigenvalues are (-7+24i)/25 and 1, both of modulus one, and W commutes with K in their common ideal basis. This checks that the comparator is an isometry once r_phys>0; it does not factor old aging out of actual dynamics. The finite actual state and this infinite comparison target occupy the same embedded output space.

## 2. Full ordered inverse and the actual outside vector

The reference denominator Q0 is a function of D, whereas the actual G need not commute with D. The exact factorization is

    Q=Q0(I-K_load),
    K_load=kappa^2 Q0^-1(D^2-a1^2)(G-G0),
    Q^-1=(I-K_load)^-1 Q0^-1.

The scalar identity

    |q0|^2/lambda^6
      =(1+y^2)^3-(lambda/j)(3y^6-10y^4+3y^2)
      >=(1-3lambda/j)(1+y^2)^3

supplies the selected margin s=sqrt(1-3lambda/j). The sharper ratio bound for (D^2-a1^2)Q0^-1, together with its closed-channel ceiling 6, gives the stated Theta. Complementary inverse columns retain their separate ceiling 170 before loading. These full-fiber estimates are applied separately on the two physical lips; no assertion Q_minus=Q_plus^* is needed.

At this point b0<5.81e9, kappa^2<9e-15 and s>.9999999994. Thus the leading numerator j a0+kappa^2 b0 is <2.4e-20+5.229e-5. Division by s and the additional complementary term <7.53e-12 still give Theta<5.24e-5. Consequently

    n=(1-Theta)^-1<1.00005241,
    c3=(1-Theta)s>.9999475.

This is the nominal condition, without a common offset or residual detuning. The accompanying actual matching and physical-root regularity remain necessary for the represented Stone formulas; merely writing a real resolvent inverse would not establish absence of singular seed measure in the retained windows.

The sixth moment is an installed-device fact, not an inference from the isolated scalar density. On a prepared old-energy input with center E_e, the first three actions give

    (H-E_e)V_e=-a1 |s1> iota_e,
    (H-E_e)^2 V_e=(a1^2 |s0>+a1a2 |s2>) iota_e,
    (H-E_e)^3 V_e=
      [-a1(a1^2+a2^2)|s1>-a1a2 kappa |p>] iota_e.

The two final head positions are orthogonal. Their squared norm is exactly

    mu6=a1^2(a1^2+a2^2)^2+a1^2 a2^2 kappa^2
       =3lambda^6+(8/3)j lambda^5.

The port term is essential. A downstream contact would first act after the third application and hence does not alter this identity. The source-contact and prepared-vacuum hypotheses are still essential. With lambda=1e-12, mu6<8.00000001e-63. A squared witness for the claimed outside ceiling is

    2mu6<1.600000002e-62,
    (1.3e-8)^2(2.15e-8)^6>1.66e-62.

The spectral theorem and Cauchy-Schwarz over the two input-energy projections therefore give ||E_H(I^c)V||<1.3e-8. They do not presume orthogonal omitted output images or [H,K]=0. This is one complete omitted vector, including all outside spectral types and passive references, and it must be charged once globally.

## 3. All three represented source coordinates

The ordered subtraction is

    (R-R0)e0=kappa^2 (R0 e2)(G-G0) a1a2 Q^-1.

The reference last-source column has numerator (a1a2,-a2D,D^2-a1^2). On a scalar reference channel x its squared joint norm is exactly

    (a1a2)^2+a2^2 x^2+(x^2-a1^2)^2=(x^2+lambda^2)^2.

This identity includes both intermediary sites. Multiplying its selected bound 1/(s sqrt(delta^2+lambda^2)) and its complementary bound 6 by the full ordered inverse gives the quoted local resolvent errors. The integrals of v^-2, |delta|v^-2, v^-3/2 and |delta|v^-3/2, with v=delta^2+lambda^2, are respectively pi/(2lambda^3), 1/lambda^2, 2/lambda^2 and 2/lambda. They reproduce D_sel. The two lips and the Stone factor 1/(2pi) leave the prefactor 1/pi, not an additional factor two.

For wrong-window inputs the reference jump vanishes, but the actual complementary column is still bounded. Integrating v^-1/2 and |delta|v^-1/2 over [-d,d] gives 2 asinh(d/lambda) and 2(sqrt(d^2+lambda^2)-lambda), which reproduce D_wrong. There is no deletion of complementary forcing.

The new arithmetic is conservative. Using a1a2<.944lambda^2 gives the selected prefactor <2.706e-39. Its dominant b0/(s^2 lambda^2) contribution is <1.573e-5; the other terms leave the stated D_sel<1.574e-5. For the complement, the prefactor is <4.61e-37 and the bracket is <280: its dominant piece is <278.881, the 6b0 d^2 term is <2.01e-5, and the calibration terms are negligible but retained. Thus D_wrong<1.4e-34.

The isolated finite-band reference is not silently made Markovian. Its three weighted-density errors E0,E1,E2 include the physical denominator correction and the exterior rational tails. At eta<3.704e-10 and C=6eta+9eta^2<2.223e-9, the exact displayed formulas give every E_i<2.3e-9 and E_vec<4e-9. In particular the coefficients multiplying C in E1 and E2 are less than one, and q^-2 differs from one by less than 2.23e-9.

For the rational three-coordinate norm, the squared polynomial at z=20 is

    (463/3)^2+420^2/3+320000/9
      =1,063,569/9<344^2.

Each nonnegative polynomial term times exp(-2z) decreases for z>=20. The finite Taylor lower bound exp(5)>148 therefore gives F(z)<344*148^-4<7.3e-7 throughout the required interval, indeed for all z>=20. This is a joint source norm, not a seed-return probability.

The separate reference truncation costs eta_ref<1.3e-8. It changes the full isolated reference into its represented part and is distinct from the actual outside vector. The selected input aggregation costs sqrt(2)D_sel, the two wrong-window pieces at most 2D_wrong, and orthogonal record/parity sectors combine by maximum. With sqrt(2)<1.415,

    S_I <7.3e-7+4e-9+1.3e-8+1.415(1.574e-5)+2.8e-34
        <2.30192e-5<.0000231.

## 4. Both raw traveling errors and physical incoming identification

The exact scalar second moment is lambda^2/3. Applied to the unchanged emitter-free outgoing-row error, flux contraction and Minkowski give the proposed E_sel, including both the calibration floor and the loading term. No old Lorentzian moment or one-site source restriction is reused. Numerically,

    [304/(2j cos h)+.302/g]lambda/sqrt(3)
       <6.0963e6*.578e-12=3.5236614e-6,
    1.384 Theta/(1-Theta)<7.25255e-5.

Adding 2.1e-13 gives E_sel<7.61e-5. The complementary row includes the 170 reference inverse and loading-induced mixing; its B_wrong and Fourier-window factors give E_wrong<1e-34. Thus 2E_raw<2*1.415*7.61e-5+2e-34<.000216. The p factors are upper-bounded by one only where that is conservative.

Reality of the physical Hamiltonian and the fixed real sector/domain inclusions identifies the lower rectangular resolvent column by entrywise conjugation. Self-adjointness alone would give an adjoint with reversed domain/range and would not suffice. The real Stone jump gives an outgoing Fourier term and a conjugate incoming term with the same physical exp(-itE), both with plus signs. Conjugation changes the ideal W coefficient to W*, while retaining the same norm bound and all cross-window input columns.

The outgoing and incoming errors can occupy the same physical halfline; they therefore cost two raw errors by triangle. They are not combined in quadrature, and neither is replaced by a normalized outgoing-error allowance. Record/parity orthogonality does not remove the two-old-energy or wrong-window costs already included here. These are complete operator estimates before a success projection.

## 5. New background IBP substitution

The absolute background bound is still valid. The full-forcing L0<14000 includes the 235 finite background heads and all closed slow tails, excluding all three source heads and the propagating open component. Using the new kappa and c3 gives

    8sqrt(2)kappa L0/(3pi c3)<.0016.

This is an upper bound, not a physical residual floor.

For the improved bound, each fixed physical window has a fixed closed-channel projector. Its finite-plus-closed-tail range embeds in one physical Hilbert space. The geometric closed tails and their derivatives are square summable with the stated operator bounds, so the recovery columns are absolutely continuous there. No energy-dependent moving basis or unproved actual-source complex strip is introduced. The lip column is exactly -kappa a1a2 L Q^-1 V_seed in that order.

The new cancellation concerns the exact physical q0, not a rational replacement. With physical upper Weyl m=delta/(2j^2)-i sqrt(1-delta^2/(4j^2))/j,

    q0=(delta+i lambda)^3-kappa^2(delta^2-lambda^2/3)(m+i/j).

The imaginary cubic terms cancel exactly when this is expanded. Direct differentiation gives |m'|=1/[2j^2 sqrt(1-delta^2/(4j^2))]<.501/j^2 and |m+i/j|<=.501|delta|/j^2 on the retained band. Hence

    |q0'|<=[3+4.509lambda/j](delta^2+lambda^2)
           <3.00002(delta^2+lambda^2).

The lower lip has the same bound by conjugation of the scalar reference. This reduces only the selected reference derivative constant. The complementary derivative constants 4000 and 200 and the actual discrepancy derivative Z_g remain. It is not a global factor-of-two assertion for the actual Q derivative.

Writing U0=Q0^-1 and N=(I-K_load)^-1, the exact prepared derivative is

    (Q^-1 V_seed)'=N U0' V_seed+N K_load' N U0 V_seed.

Thus both n and n^2 are needed. The full G derivative, derived from physical recovery rather than by differentiating its value bound, supplies Z_g=2e8+17000/g=3.402e11. Integrating the resulting real-line majorants gives precisely the new D3 formula in the target, with A=3.00002 and A_s=2/s+A/s^2. Wrong-window prepared inputs remain in this full D3; D3_C is not an additional charge.

The dimensionless arithmetic can be bounded term by term without evaluating a spectrum or integral numerically:

| Term in the D3 formula | Upper ceiling |
|---|---:|
| n A pi/(2s^2) | 4.715 |
| A_s(4a0/3+2b0lambda/3) | .019372 |
| 400a0lambda^2+400b0lambda^3 | 3e-24 |
| Z_g(pi lambda/(2s)+12lambda^2) | .53461 |
| Multiplier 3j n^2/s | .009001 |
| Product of that multiplier and the preceding three terms | .004987 |

Here pi<22/7, s>.9999999994, n<1.00005241 and A_s<5.001 suffice. Therefore

    D3<.944(4.715+.004987)/lambda<4.46e12.

The retained recovery derivative is the FULL forcing bound

    M_g=1.00068(7.29e16+3.31e7/g)+30<7.37e16.

It is not replaced by a selected-column converter derivative. At the hard endpoints, the two lip-column values cost 2kappa a1a2 L0/[c3(d^2+lambda^2)^(3/2)] per lip. The product derivative splits into L'Q^-1 V_seed and L(Q^-1 V_seed)'. Integrating the first uses int (delta^2+lambda^2)^(-3/2)<=2/lambda^2, and the second is exactly bounded by L0 D3 after removing kappa. Paying two lips and two windows produces

    B_IBP(t)<=2kappa/(pi|t|) *
      [2c_a lambda^2 L0/(c3(d^2+lambda^2)^(3/2))
                                  +2c_a M_g/c3+L0 D3].

There is no assumption of orthogonal old-energy error images. The physical center phases, both hard edges and both lips remain. The bracket entries are respectively <2700, <1.392e17 and <6.244e16, with sum <2.017e17. Thus

    B_IBP(t)<[1.8974e-7/(3.14*2e13)]2.017e17*(T/t)
             <.000610*(T/t),  t>=T.

The two bounds concern the same represented background map, so their minimum is valid. At this point the recovery-derivative term exceeds the inverse-derivative term; the tighter cubic bound does not eliminate the former. No actual outside mass is charged inside either background estimate.

## 6. Weighted reference, physical phase and normalization

The proof cutoff D=g/4=1.25e-8 lies below d; it changes no hardware. With x=2g(k-pi/2), delta(x)=2g sin(x/(2g)), the central interval obeys |delta|>=alpha_D|x|. The exact scalar determinant margin gives

    |q3(delta(x))|>=s alpha_D^3 (x^2+lambda^2)^(3/2).

Since D/(2g)=1/8 and sin y/y>1-y^2/6, alpha_D>383/384, m_D=s alpha_D^3>.9922 and delta_D>.997D. There is no old cutoff-displacement smallness condition to check: inversion uses this separate positive margin.

The physical phase bound can also be verified directly with the exact original J=.030021107107032 and j<.003. Put a=sqrt(j/J), so a<.317. On |q-pi/2|<=4e-6, both sin(q/2) and cos(q/2) are <.708. Therefore

    k_old'(q)=a cos(q/2)/sqrt(1-a^2 sin^2(q/2))<.24,

using j/J<.1, a numerator <.224436 and denominator >.97. This uses the same calibrated j/J relation; it does not retune j or discard the old-chain phase. Consequently

    |phi'(x)|<=1/(4g)+(61.5+172*.24)/(2j cos h)
                =1/(4g)+102.78/(2j cos h)<5.02e6.

The scalar comparison is phase sensitive. Against the cubic density rho_M=C^2/(x^2+lambda^2)^3, its exact full second and fourth moments are lambda^2/3 and lambda^4. The numerator/flux and denominator-displacement errors give the coefficient 1/(4j^2)+11/(8g^2); the phase difference costs P|x|. Minkowski with those two moments and the lower margin m_D therefore gives the stated E_c. At this point its numerator is <2.904e-6 and the sharper displayed substitutions give E_c<2.93e-6.

Dispersion is paid only after the central amplitude comparison, on the rational amplitude. It therefore does not acquire another 1/m_D. The full sixth moment of rho_M is divergent. The valid truncated calculation is

    int_(-D)^D x^6 rho_M(x) dx<=16lambda^5 D/(3pi),

which gives the proposed E_disp. With t<=4e13 and pi>3.14, the square root is <1.458e-34 and the prefactor is <=(2/3)e27, so E_disp<9.8e-8. This explicitly charges the actual nonlinear dispersion; it does not replace the physical dispersion in the target.

The physical raw tail uses the threshold delta_D, whereas the cubic tail uses D. Taking the stated full-band scalar tail alternative, rather than the installed moment as an outgoing density, gives U<3.4e-11. The rational tail gives V_D<3.4e-11. The two-sided lattice alias sum, with exact period 4pi g in x, gives Z<3e-14. These remain distinct from actual outside mass and from one another. The alias bound is uniform in time because its real time factors have modulus one.

Transmission and scalar truncation give

    1-p<=mu6/d^6+lambda^2/(3g^2)
        <8.45e-17+1.333333334e-10<1.334e-10.

Thus p is positive and 1-sqrt(p)<7e-11. Summing the central, dispersion, both tails, aliases and this scalar normalization costs <3.1e-6. This E_w compares the normalized scalar Fourier coefficient to the sampled cubic comparator; the latter is not assumed to be a unit lattice vector.

The conjugate cubic packet has the opposite pole and is supported on t+m/(2g)<=0. For t>0 it vanishes on physical m>=0. The same phase-sensitive comparison therefore bounds normalized incoming mass there by E_w, and the RAW incoming allowance is sqrt(p)E_w<3.1e-6. This is combined with the actual incoming coefficient error already paid in the preceding section; it is not substituted for that error.

For outgoing concentration the H polynomial at z=20 equals 1,063,569/9+32/15<344^2 at the chosen lambda/g. Its nonnegative terms times exp(-2z) decrease for z>=20. Hence H<7.3e-7 and H+E_w<3.9e-6 uniformly for 20<=lambda t<=40. This bounds the larger excluded set m<=0 and therefore also the physical complement m<0. Parseval now gives

    r_phys>=sqrt(p)sqrt(1-(3.9e-6)^2)>0,
    1-r_phys<7e-11+(3.9e-6)^2/[1+sqrt(1-(3.9e-6)^2)]
                  <1e-10.

This is one physical-halfline normalization of the ideal packet. The 1-sqrt(p) inside E_w is needed for the scalar comparison used to bound incoming/concentration norms; it is not added again as a normalized traveling-coefficient error. No actual output is renormalized in the complete operator inequality.

## 7. Exact finite cut, full sum and consequences

The output-only weight is zero on all source, processor, converter and gate coordinates and on r0. Only the retained g edges of the slow ray have nonzero weight gradient. On the full internal fiber the weighted imaginary generator therefore has row/column bound 2g sinh(a), irrespective of the unchanged core hopping strengths or noncommuting onsite blocks. The cap g n_last is exactly the deleted bond's compressed diagonal. In the decoupled evolution only the retained-to-omitted cut orientation acts on the seed, so the one-cut Duhamel integral contains g, not 2g.

The established bound consequently specializes with g, last weight M-1 and no graph-distance shift. At a=1 and t<=2T it is <1.2 exp[-M+4gT sinh(1)]. Here 4gT=4,000,000 and sinh(1)<1.176, giving exponent <-296,000. The quoted <1e-10 is vastly conservative. This compares complete actual evolutions including returns and every spectral component, not just output leakage. The same infinite normalized comparator is retained after embedding the finite evolution.

The spatial/Stone decomposition is now closed with each actual component represented once:

| Contribution | Uniform ceiling on [T,2T] |
|---|---:|
| One actual outside vector | .000000013 |
| All three represented source heads | .0000231 |
| Full represented finite/closed-tail background, using IBP | .000610 |
| Both raw traveling coefficient errors | .000216 |
| Raw ideal incoming halfline packet | .0000031 |
| One ideal physical-halfline normalization | .0000000001 |
| Complete finite/infinite cut | .0000000001 |
| Sum | .0008522132 |

Replacing only the background row by .0016 gives .0018422132. The stronger sum is below .00086, and the absolute-background sum is below .00185. The upper time endpoint is paid in dispersion and finite transfer, while source decay and IBP use their lower time endpoint. Thus this is uniform on the entire stated interval, not just an evaluation at T.

The ideal target has record1. Projecting the full operator error onto record0 gives the failure effect <epsilon^2 I, with epsilon=.00086 and epsilon^2=7.396e-7. Success is therefore >.9999992604 for every input, including reference-entangled inputs. Projection onto record1 is a contraction within epsilon of the ideal isometry. Its successful norm is >=sqrt(1-epsilon^2), so its normalized-vector distance is <epsilon+1-sqrt(1-epsilon^2)<.000861. Standard two-term isometry/contraction estimates give complete-channel and successful subnormalized CP-map diamond distance <2epsilon=.00172. The normalized conditioned map is not claimed to be a linear channel.

The inventory follows from the same installed graph: two extra source heads/edges and four extra unmerged blocks relative to the one-site baseline. Substituting M gives 5,000,238 heads, 5,000,243 physical qubits, 5,000,239 head edges and 10,000,281 positive blocks. Shared old/source/record qubits are counted once; passive references are not counted. Receiver M and certified onset are exactly tenfold lower than the earlier large three-site point and fiftyfold lower than the cited PR9679 point. Ratios of total physical qubits have the fixed offsets and are not exactly those integers. These comparisons concern sufficient certificates for different source coefficients/waveforms, not measured error, minimum time, minimum resource count or dominance of every earlier tradeoff.

## 8. Prose qualifications and limits

Two local wording qualifications are advisable for later packaging; neither changes the proof or point:

1. The sentence in the absolute-background section saying that no derivative or pending IBP result is used describes **that baseline calculation only**. The stronger final certificate explicitly uses the separately checked IBP and cancellation inputs. The later section makes the distinction, but the sentence should retain its local scope if quoted elsewhere.
2. The closing phrase “background as sqrt(lambda)” describes the **absolute** upper bound. At fixed g and lambda*T, the IBP recovery term kappa M_g/T scales as lambda^(3/2), while its leading inverse term kappa L0 D3/T scales as sqrt(lambda); margin and smaller terms remain explicit. The final .000610 allowance must not be rescaled using only sqrt(lambda). The target correctly recomputes both terms at the chosen point, so this qualification does not invalidate .00086.

The result is nominal: Delta=0, exact critical ratios, original calibration and the stated product/vacuum/record preparation. Neither perturbed-source families nor later phase-family positive-block decompositions are included. The finite read window is certified, not irreversible capture, permanent halt, indefinite storage, repeated monitoring, source reset, native coefficient generation or arbitrary hardware fault tolerance. The new derivative inputs remain conditional on their physical matching and recovery premises. This review establishes no new microscopic Hamiltonian or Record identification and makes no retained-status or audit determination.

## 9. Exact evidence and coverage

The complete target, new cubic-cancellation source/check, weighted-reference source/check, scalar source, installed attachment, loaded inverse, represented local-source source/check, outgoing source, traveling interface, IBP source and output-weight source/check were read in full for this review. Necessary exact canonical parameter and comparison passages were refreshed. The remaining unchanged component checks and D3/recovery arguments were fully read in earlier coherent tasks and are reused only at their unchanged identities and stated scopes. I used the distinct large-point and dwell/composition checks for my own authored ancestors; my current review is not an additional independent check of those ancestors.

All 31 local source/check pins listed by the target were deterministically verified against their actual bytes. The canonical endpoint pin was also verified. Source identities are evidence of what was read, not additional mathematical validation. No scientific program, numerical quadrature, dynamics, parameter sweep, optimization, calibration replay, external search, model change or delegation was performed. The only execution was read-only text/hash bookkeeping. Only this review file was written; no original source, W, Git, PR, checkpoint, prompt or axiom file changed.

Paths below are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`, except the final canonical path, relative to the read-only `correlation_worktree` sibling.

| Source | SHA256 |
|---|---|
| three_site_complete_candidate/PROPOSAL.md | b64b5a073aeedf47c8d1f3b604763af43edd0ac0d61ac572638a6bfac2ab0e5a |
| three_site_complete_candidate_check/REVIEW.md | b660546cf354778d99dc08c7277e386069aa62ab9ef9efba5fb44596a19cc821 |
| three_site_weighted_reference_time/PROPOSAL.md | d41e468ffec769a9f5a36a7796999366fddf04ff2b42c1a8083c20e46f243d36 |
| three_site_weighted_reference_time_check/REVIEW.md | 809c0e0b452b4d913d5750f3aa184473c4d4b20132de7a73b919e8d0be5415ac |
| three_site_product_source/PROPOSAL.md | a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823 |
| three_site_product_source_check/REVIEW.md | c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b |
| three_site_actual_attachment/PROPOSAL.md | 4278633f3436008a770088331a2424d3f42dda06d08853dfe18d9b8a6554f006 |
| three_site_actual_attachment_check/REVIEW.md | ede902f9c1bebc768147e459894f98610689f33655f87d01d91d07531cbd157d |
| three_site_loaded_inverse/PROPOSAL.md | 7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672 |
| three_site_loaded_inverse_check/REVIEW.md | 8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2 |
| three_site_local_escape/PROPOSAL.md | 0340895610d3a5ef709dd8a03c1bc5872c8f34cf00f21053c00adcc3d706468d |
| three_site_local_escape_check/REVIEW.md | e19767c8092fb856a3c24cb279f621deea38d69d65c41bef4a1aea44bad23074 |
| three_site_outgoing/PROPOSAL.md | af580b44fc2ebfc35eb014ffc63b8bae17464150677ede4a8b8315886f6f36ac |
| three_site_outgoing_check/REVIEW.md | 721a183db3e42527d7cb5bdda697e6c6d81312a94cf047dd7ea15897cb4c2f02 |
| three_site_traveling_interface/PROPOSAL.md | 75b1ba68fae3f34e54c15df80b3a39a165240b1759f8fc84eb2b24677cc7f9e3 |
| three_site_traveling_interface_check/REVIEW.md | 9cb7655b688a61ce32b950f2d95024762023770380a6e5df8afaa1939744230a |
| prepared_core_recovery/PROPOSAL.md | cce29994b7141df161ca12f377765fdaf760f7e64fc56043bbf370e2cd437ea9 |
| prepared_core_dwell_check/REVIEW.md | 88274b8b49e583bdb9b5f933f7406b1a96a6ca79049e57b83e8030c834d16819 |
| prepared_core_composition_check/REVIEW.md | 52edba6061be49eef40b5c06754a7425b5f7f62671f175cc72a093d4a60de65c |
| three_site_reference_time/PROPOSAL.md | d21632c8660f92e9478433bb564b357fe623aaa86c465d82537cfb28b77b315f |
| three_site_reference_tail/PROPOSAL.md | 92a14fa12ccb489bfe311278683b6aa12b67b6549449273ba181383f5f779fb1 |
| three_site_reference_time_check/REVIEW.md | 0439d990a12b51561257038b1ef14aeb88302adf12bb546de0f00571ac44a553 |
| output_lead_weight/PROPOSAL.md | 58f99248986aebe14b4cd87f46237a293ed0c86ab720dd37a497c5b2a64a06cf |
| output_lead_weight_check/REVIEW.md | 1c72e347fed86c96fcc491c550c136d08f3b7720d52ec1534af94066056d59dd |
| slow_lead_wide_publication/NOTE.md | feec1a7b2d48b758c86d5bdcde4ef0043a3b51ee09fb773024fbd7fd52d5bb38 |
| prepared_background_ibp/PROPOSAL.md | 90d42e3699496e7694ddda630672af778a506b795865118757ab1e57da4a9c5a |
| prepared_background_ibp_check/REVIEW.md | 5c4c1e2b8930be39195181681c563cd0c150611ad07a201316f3096e5a55ea12 |
| three_site_cubic_derivative_cancellation/PROPOSAL.md | d57ca3702567780319131cdcadd824588364b93d77575e26b56e00565fd292ac |
| three_site_cubic_derivative_cancellation_check/REVIEW.md | c65696bec16ece9a1080fd24100fb8d7130821f76136f35810d3d148c155d5d4 |
| three_site_prepared_inverse_derivative/PROPOSAL.md | 25052bad1d500f52d4e4f4d3913f0bf8a0a57d69801688b7109a549ac3756d84 |
| three_site_prepared_inverse_derivative_check/REVIEW.md | 3a76d76895c01dcbd7cf7e5b566f7146ae683ddc4568352df06c19224e59aa1c |
| docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md | 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff |
