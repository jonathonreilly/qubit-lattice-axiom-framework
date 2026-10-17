# Integrated prepared cubic inverse derivative from actual endpoint compression

Status: new conditional author derivation requiring a distinct check. The actual emitter-free endpoint derivative follows directly from the assembled physical matching equation and checked full recovery VALUES. This gives an explicit finite bound for the nominal three-source prepared inverse derivative D3, without differentiating the small real error envelope or using a whole inverse norm. It supplies no full L', runtime or complete-device claim.

## 1. Domain and exact background derivative

Keep the original calibrated .0027<j<.003, 0<g<=1e-6, 0<h<=4e-6, d=2j sin h, d/g<=1/2, with all original physical source, converter, cap, record gate and shared internal premises. Work separately on each of the two physical old-energy windows, each parity/record sector and both spectral lips. Every finite matching matrix retains the complete eight-coordinate fiber.

The checked emitter-free background has235 finite heads, a slow lead eliminated at gate output o and a fixed forcing inclusion V_p at the source attachment endpoint. In the fixed real coordinate basis,

    M(E)=E I-H_finite+j V_o Q_slow(E)V_o^T,
    R=M^-1, F=R V_p, F_o=V_o^T F,
    G=V_p^T R V_p.

The coefficient j of the eliminated slow root is the actual connector selfenergy tau²/g, with tau=sqrt(jg). No artificial lead or changed diagonal is used. Both V inclusions and H_finite are energy independent. The physical retarded M and R are complex symmetric, not Hermitian. Exact differentiation and transpose reciprocity give

    G'=-V_p^T R M' R V_p
       =-F^T F-j F_o^T Q_slow' F_o.                   (1)

Equation (1) is not a positive Gram identity: the transpose is literal. The operator-norm inequality nevertheless uses ||F^T||=||F|| and needs no normality of R. The checked prepared-core recovery VALUE result is actually full forcing-domain:

    ||F||<14000, ||F_o||<3270.

The first follows by restricting its finite-plus-closed-tail L; the second is its actual gate-output restriction. Neither is a selected-only incoming-wave estimate. The wider root calculation gives ||Q_slow'||<1/(1.93g), including every closed channel. Thus

    ||G'||<196000000+16622/g.                          (2)

For the coefficient, .003*3270²/1.93<16622. The same formula and norms apply on the lower lip. In particular (2) requires no newly proposed direct-core or converter derivative theorem, nor the large RF or full R inverse estimates.

The physical reference is G0=m_j(D), D=(E-c_att-2j)I-B, D'=I. On the selected old-j channel m_j=-exp(iq)/j, so |m_j'|=1/(2j² sin q)<1/(j*.0053)<70000. On complementary |x|>=.185 the half-line resolvent has distance at least .179 from [-2j,2j], giving |m_j'(x)|<=1/.179²<32. Fixed B projectors therefore give ||G0'||<70000. Set

    Z_g=2e8+17000/g.

Then the ACTUAL derivative of the discrepancy obeys

    ||(G-G0)'||<Z_g,                                  (3)

while its separately checked value obeys

    ||G-G0||<=a+b|delta|,
    a=8e-18, b=46000/.0053+290/g.                     (4)

Equation (3) was derived from physical equations and full values, not by differentiating the inequality (4). The fixed calibration floor a has not been declared differentiably constant.

## 2. Ordered source factorization and margins

Use the nominal Delta=0 source only:

    0<lambda<=1e-8,
    a1=lambda/sqrt(3), a2=lambda sqrt(8/3),
    kappa²=3jlambda, s=sqrt(1-3lambda/j)>0.

Let P2=D²-lambda² I/3 and define

    Q0=P2(D-kappa²G0)-(8lambda²/3)D,
    Q=P2(D-kappa²G)-(8lambda²/3)D,
    U0=Q0^-1, T0=U0 P2,
    Kload=kappa² T0(G-G0), N=(I-Kload)^-1.

The exact order is

    Q=Q0(I-Kload), Q^-1=N U0.                         (5)

Only reference functions of D commute. The checked nominal source criterion is

    Theta=(j a+kappa² b)/s+6kappa²(a+bd)<1,
    n=1/(1-Theta).

It supplies ||N||<=n. With r_delta=sqrt(delta²+lambda²), the reference estimates are

    ||U0||<=1/(s r_delta³),
    ||T0||<=1/(s r_delta)+6,
    ||U0 C||<170, ||T0 C||<6.                         (6)

The selected P2/q0 envelope in (6) is deliberately looser than the sharper1/(3lambda s) identity used to establish Theta. The latter criterion remains exactly the checked one; it is not recomputed from this looser derivative envelope.

V_seed denotes the fixed prepared internal inclusion, of norm one. On a given physical window it retains both the selected prepared old-energy input and the wrong-window prepared old-energy input. It is not an energy-dependent scattering eigenvector. All differentiation below acts on Q^-1, not on an input or reference vector.

## 3. Derivatives of the genuine finite-band reference

The scalar physical reference denominator is

    q0(x)=x³-3lambda²x-kappa² m_j(x)(x²-lambda²/3).

On the selected real band, |m_j|=1/j and |m_j'|<70000. Differentiating this exact expression yields

    |q0'|<=3(delta²+lambda²)
               +kappa²*70000*(delta²+lambda²)
               +6lambda|delta|
            <=6.01 r_delta².                        (7)

Here 6lambda|delta|<=3r_delta² and kappa²<=9e-11. The bound is for the exact finite-band determinant, not the Markov cubic.

On a complementary x, |x|>=.185, the checked |q0|>.99|x|³ and |P2|<1.000001 x² hold. Using |m_j'|<32 (or even70000), lambda/|x|<6e-8 and the same exact derivative gives |q0'|<4x². Therefore

    |(1/q0)'|<4/(.99²*.185⁴)<4000,
    |(P2/q0)'|
        <[2/.99+4*1.000001/.99²]/.185²<200.          (8)

Both energy signs and both real closed roots are included. Because Q0 is a fixed-projector function of D, channel maxima yield matrix bounds without a fiber-count factor. The selected derivative envelope below dominates4000 over the whole narrow window, since r_delta<2.6e-8. Thus

    ||U0'||<=6.01/(s² r_delta⁴),
    ||U0' C||<4000,
    ||T0'||<=A_s/r_delta²+200,
    A_s=2/s+6.01/s².                                 (9)

For the selected T0 derivative use 2|delta|/|q0|+|P2||q0'|/|q0|² and |P2|<=r_delta². This proves (9), including the complementary additive allowance. These are derivatives of reference functions only; no actual G commutation is introduced.

## 4. Exact prepared differentiation and an explicit integral

Differentiate (5) in order:

    Kload'=kappa²[T0'(G-G0)+T0(G-G0)'],
    N'=N Kload' N,
    (Q^-1 V_seed)'=N U0' V_seed+N Kload' N U0 V_seed. (10)

Combining (3),(4),(6),(9),

    ||Kload'||<=kappa²{
       (A_s/r_delta²+200)(a+b|delta|)
                               +(1/(s r_delta)+6)Z_g}. (11)

No inverse bound has been differentiated as an inequality. The Neumann derivative includes TWO factors N in its second term, as required. The actual lower ordered denominator need not be the adjoint of the upper; (10) is applied independently on both lips.

Define the requested quantity

    D3=a1a2 sup_(physical window,lip,sector)
       integral_-d^d ||(Q^-1 V_seed)'|| ddelta.

All resulting bounds are uniform in those indices. Extending positive scalar integrands to the whole real line gives

    int r_delta^-4 = pi/(2lambda³),
    int r_delta^-5 = 4/(3lambda⁴),
    int |delta| r_delta^-5 = 2/(3lambda³),
    int r_delta^-3 = 2/lambda²,
    int |delta| r_delta^-3 = 2/lambda.

Since a1a2=c_a lambda² with c_a=2sqrt(2)/3, (10)–(11) prove the explicit bound

    D3 <= c_a lambda² {
       n*6.01*pi/(2s² lambda³)
       +(n² kappa²/s)*[
          A_s(4a/(3lambda⁴)+2b/(3lambda³))
          +200(2a/lambda²+2b/lambda)
          +Z_g(pi/(2s lambda³)+12/lambda²)] }.        (12)

Equivalently, substituting kappa²=3jlambda,

    D3 <= (c_a/lambda) {
       n*6.01*pi/(2s²)
       +(3j n²/s)*[
          A_s(4a/3+2b lambda/3)
          +400a lambda²+400b lambda³
          +Z_g(pi lambda/(2s)+12lambda²)] }.         (13)

This is finite on every allowed positive domain point with Theta<1. It has a leading1/lambda scale and explicit actual-background derivative terms. For fixed g and bounded inverse margin as lambda decreases, the b lambda and Z_g lambda terms in its dimensionless bracket decrease. The calibration floor a remains. If g co-varies, Z_g lambda and b lambda must be evaluated; they cannot be declared decreasing without an additional relation. Neither a zero-lambda limit nor a full temporal conclusion is asserted.

There is no logarithmic resonance loss in the full bound (12); all its weighted integrals converge. This does not imply the exact D3 has that value or that no sharper constant exists. The estimate may be conservative and diverges as Theta approaches one.

## 5. Wrong-window columns explicitly retained

For clarity, retaining the complementary reference-input bounds instead of the full selected envelope gives a separate estimate. Let C V_seed be the wrong-window prepared inclusion (and, more generally, any complementary fixed input contraction). Then

    D3_C:=a1a2 integral ||(Q^-1 C V_seed)'||
      <=c_a lambda² {8000dn
       +170n² kappa²[
          A_s(a*pi/lambda+b log(1+d²/lambda²))
          +200(2ad+bd²)
          +Z_g(2asinh(d/lambda)/s+12d)]}.             (14)

Indeed U0 acts on C BEFORE N in (10), so its norm is <170 even though the actual output can mix into the selected channel. Likewise U0' C<4000, integrated over width2d. Formula (14) integrates exactly the appropriate terms in (11), with safe full-line bounds only where displayed. It does not discard induced selected output or pretend Q^-1 is diagonal.

Equation (12) already covers the entire V_seed without needing to add (14); (14) exposes the wrong-window control separately. D3 is a supremum of per-window integrals, not their sum. A later two-window Stone/IBP application must retain its own two-window/two-lip factors exactly as in the source contract. Orthogonal sector maxima and passive-reference tensoring introduce no new derivative or multiplicity here. No omitted outside spectral state is bounded by these in-band estimates; that remains a distinct actual seed-moment obligation.

## 6. Scope and exact evidence

The main structural step is endpoint compression (1), which uses the full actual F value twice and pays the slow-root derivative only on F_o. This bypasses the large arbitrary R or RF norm for G' and does not need the newly drafted prepared-core/converter derivative results. It does NOT by itself improve the full finite recovery derivative L': compression to G is essential. The integrated bound (12) supplies the nominal D3 obligation named in prepared_core_recovery §8; it is not a complete integration-by-parts result, since L', endpoint terms, all spatial ranges and actual outside mass must still be assembled separately.

All actual old/reference phases, the physical E variable, c_att, shared B/K and literal W remain unchanged. Delta is zero and the source ratios are nominal. Common offsets, residual source perturbations or nonidentity detunings would require new reference derivative bounds and cannot be inserted by relabeling lambda or delta.

Exact dependencies:

- three_site_loaded_inverse/PROPOSAL.md: 7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672; distinct check8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2. Both complete arguments refreshed for ordered full-fiber margins.
- prepared_core_recovery/PROPOSAL.md: cce29994b7141df161ca12f377765fdaf760f7e64fc56043bbf370e2cd437ea9; selective checks88274b8b49e583bdb9b5f933f7406b1a96a6ca79049e57b83e8030c834d16819 and52edba6061be49eef40b5c06754a7425b5f7f62671f175cc72a093d4a60de65c. Its fully read and checked full-domain VALUES14000/3270 are reused; its large derivative bound is not a premise.
- slow_lead_wide_derivative/PROPOSAL.md: c2b9d6917db45faa1e9974cb69ef9bc683f45147bcb47b3588df36e94b630f2a; checkc74a8118cccafe3e64dc6f4aa499fc7fa9abb194dae5cedbb2c253fb06054c79. Exact assembled physical equation, real transpose structure and all-channel1/(1.93g) root derivative are reused; necessary passages refreshed.
- slow_lead_wide_endpoint/PROPOSAL.md: c4c99408686166ba4d80bc973f5c22afdd1185bbf38e4539512dc26afd5cd5e3; checkc6cc2ed747956e70bba1a7af3a5d65d3d36a7f708367727cb6f5e8a74386feb5. Only unchanged emitter-free value envelope(4) and channel classification are imported, not its one-site emitter conclusions.
- Original physical source/calibration identity remains71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff within those inherited hypotheses.

I authored the wide derivative and several source/reference ancestors, checked the dwell interface and have shared prior exposure to the loaded inverse. Root requested this bounded D3 problem and suggested ordered differentiation, not its validity or a numerical outcome. This is new author derivation with explicit ancestry, not independent recertification. A distinct check should reconstruct especially the transpose endpoint identity, full forcing scope of14000, physical selfenergy coefficient j, complementary reference derivatives, noncommuting order and every integration factor in(12)–(14).

Only this proposal was written. No dynamics, numerical inverse/integration, sweep, scientific runner, solver, W/Git/PR/checkpoint/prompt/model change or delegation occurred. No runtime, finite device point, performance guarantee, native supply or permanent halt claim is made.
