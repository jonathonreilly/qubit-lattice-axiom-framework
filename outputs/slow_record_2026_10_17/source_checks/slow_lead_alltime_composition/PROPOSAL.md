# Slow-output actual device: conditional all-time synthesis and finite single-read window

Status: authored synthesis requiring a distinct check. All six component sources below now have the listed selective checks, including the new outgoing check. The theorem remains conditional on their explicit supplied physical/calibration hypotheses. This is neither retained audit certification nor independent verification of the author's emitter and scalar-reference arguments. No previous attached-device numerical mass, error or runtime is imported.

## Sources and exposure

All paths in this table are relative to the parent renewal directory; source means `<name>/PROPOSAL.md`, check means `<name>_check/REVIEW.md`.

| Name | Source SHA256 | Check SHA256 |
|---|---|---|
| slow_lead_emitter | 53916c906eda8cd5a1c8c6228c54002f4f74fe7986bee301d3162124d40544c0 | 23c228886a96e29071beabf5e3ae1f6c9caee8544eee4e5b5ddc38f854fda707 |
| slow_lead_gate_load | c1e1fe95ca3c9d390df0fad468c80c93d4c1c2aa1e3fee4c93c4326f44b0e61d | 8fb22bfddeeda9dd8abd1f3c90bafe4fd34916ec385d47aa017c99b08b221a65 |
| slow_lead_recovery | f0f39510b65133d8399720c53ce2822bfe60a378ab2e50e1773a3dc8d0fe880f | 488d0a9e8871f77f40d44803ee9bfe7fda25388c66b367944eea3376f51f5195 |
| slow_lead_outgoing_profile | 6f9ebabb3405b124e52582c313c342889c9146e0040306d0ec7b72e8e8371b17 | aeb147ff7d430562ff27ab7cbfc276e8066b48199ed6c9a163ee281357ecf528 |
| slow_lead_reference_packet | e6a9706d497d7c6abb5590d2baae0940efdf628e81101f5f4cfd91885e93ea8e | 6fb89d66d0a79e5c66c6dabd00c030ddb603308485f60c857b95f0e791b1a5f5 |
| slow_lead_resources | 84b76d1ec9b1e45811b74ecd2594a0622dfb01ef69d1acadf98931c0ed3f9967 | dd944d8803da24fdfbccfd010e2fd865196aa08ac244605303093a605fef22fe |

Complete changed arguments and these checks were read in this coherent work; unchanged, previously inspected upstream premises are conditionally reused through their exact source chains. In particular the original canonical note is 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff, attachment fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457/check7df395639ea91083d9321fd05f91ffbae94eb3ae87256beb09f7f4474fa2b005, and the core resolvent interface is 69aa54015825bd6e240b1da5f856cb062157e2686d5403698592315fa4d529ac/checkad38a71087013fcee8f9ef7f00f62177d053c7ff03ba5573b524bbc3f9993357. The old synthesis 7b618a13d8094d0535ca399025ca872b54b8fdb2c9a307a0b31f521306c18e73 was fully reread for its Stone/asymptotic structure, not its old numerical estimates. Root exposed the intended synthesis and full-inverse caution. I authored the new emitter and scalar-reference components and checked several ancestors; their independent checks are external premises, not checks performed by this composition. No scientific execution, sweeps, delegation, Git/W/publication/checkpoint/model or prompt modification occurred. This is the sole new artifact.

## 1. Actual geometry, supplied state and comparator

Use the original calibrated apparatus with kappa=1e-8, input stub ell=20, shared old/source registers, eighteen output cable sites v0=(82,1,1) through v17=(99,1,1), and all 24 record-gate sites. The old gate output o=(100,2,2) is a FINITE gate site. The DISTINCT first slow site is r0=(100,3,2), with ray rm=(100,3+m,2), m>=0. The connector hopping is tau_s=sqrt(jg), g=1e-6, .0027<j<.003; all slow one-head diagonals remain2j. The original converter tau_c is unchanged. The gate-port compensation (j-tau_s)n_o, first occupation (2j-tau_s-g)n_r0 and later occupations2(j-g)n_rm are part of the actual operator. They are positive, add no vacancy scalar and preserve the declared scalar

    c_att=c_total+4(sqrt(2)-1)j.

Retain the selective installed-pair premise. Let H be the bounded self-adjoint seeded one-head operator of this infinite device; no bounded infinite many-head norm is asserted. V embeds arbitrary four-dimensional old input with emitter occupied, all other heads blank, shared source vacuum and record0. The record-X sectors s=+,- are conserved. P1 projects onto computational record1, retaining ALL remaining coordinates. Define A1(t)=P1 exp(-itH)V.

Use literal K=2I+Z1Z2 and W=[(9+12i)I+(-16+12i)X1X2]/25. They have a common real basis labeled by old energy b=1,3 and parity, with W eigenvalues (-7+24i)/25 and1. They commute with each other; no commutation of K with H is assumed.

Set h=4e-6, q in J=[pi/2-h,pi/2+h], w=exp(iq), E(q)=2j(1-cos q), delta=E(q)-2j, gamma=kappa^2/j. The slow momentum k obeys delta=-2g cos k on its principal real interval K_s centered at pi/2, halfwidth H_s=asin((j/g)sin h)<.01201. The symbol k_old(q) below denotes the ORIGINAL converter momentum, not this slow k. Define

    Dref=delta+gamma w,
    F(q)=kappa E'(q) zeta exp[i61q+i172k_old(q)]/
                         [sqrt(2pi) j Dref],
    tf(q)=exp[i(q+k)/2] sqrt(sin q sin k)/sin((q+k)/2),
    Fs(k)=tf(q) F(q) sqrt(dq/dk),
    beta_t(m)=1/sqrt(2pi) integral_Ks Fs(k)
                        exp[ikm-it(2j-2g cos k)] dk, m>=0.

The phase is61.5q+.5k+172k_old(q), referred to FIRST SLOW m=0. It is not a shift of61 slow sites. Equivalently the prefactor is sqrt(g/j) sin k/sin((q+k)/2) times exp[i(q+k)/2]F(q). This follows from energy Jacobians and flux transmission, not a guessed spatial amplitude.

Let Jout embed the head packet on these slow sites with source vacuum, other heads blank and record1. The unnormalized target is

    T1(t)=exp(-it c_att) Jout[beta_t tensor exp(-itK)W].       (1)

Write ps=integral|Fs|^2 dk and r(t)=||beta_t||. The checked scalar result gives

    1-1.100044e-6 < ps <=1,
    r(t)<=sqrt(ps),  lim r(t)=sqrt(ps),
    ||left restriction of full beta_t to m<=-1||<1e-6
                                   for every t>=T=1e15.   (2)

Thus r(t)>=sqrt(ps)-1e-6>.9999984 for t>=T. The incoming reference with conjugate Fs and phase -ikm-itE_s(k), restricted to m>=0, has norm<.0016 at every t>=0. This is already valid for the unnormalized reference; its checked normalized version is no weaker. These scalar facts include the sharp cutoff and all phases. No actual source is analytically continued beyond its verified real band here.

## 2. Full seed measure and exact physical Stone synthesis

Use the SAME physical union for every input and both record sectors:

    I=I1 union I3,
    Ib=[c_att+b+2j-d,c_att+b+2j+d], d=2j sin h<2.4e-8.

The full matrix emitter proof compares all four prepared old inputs, including wrong-window columns and off-diagonal matrix measures, to four independent j-chain references shifted by the LITERAL old energies. Its result is actual omitted seed mass<1.66e-6 and therefore

    ||E_H(R outside I)V||<epsilon_sp=.00129.              (3)

The full8 fiber per parity, both sectors and arbitrary passive references are included. This actual omitted state, including atoms and singular spectrum, is charged ONCE for the union of windows in every comparison below. It is not replaced by reference lost reflection or separately charged for core and ray.

The finite inverse chain of the new source/gate/load/emitter is regular throughout the closed windows; slow closed roots are<1/160000 and other closed roots<1/60. The actual seed measure is absolutely continuous there, including cutoff endpoints. This supplies local boundary values and excludes local singular seed mass; it is not a quantitative complex-strip or decay-rate theorem. Cross spectral measures of any finite coordinate with the seed are then absolutely continuous as well.

Let R_s(z)=(z-H_s)^-1. In fixed real coordinate conjugations the lower boundary column is the conjugate of the upper column. For a coordinate restriction Q,

    Q dE_Hs(Lambda)V_s/dLambda
      =[Q R_s^down V_s-Q R_s^up V_s]/(2pi i).             (4)

This is a rectangular-column jump, not an adjoint or scalar imaginary-part replacement. Conjugating a coefficient matrix still defines a LINEAR map on complex inputs.

On window Ib let A_s,b(k) be the complete physical retarded seed-to-slow-origin row. The upper coordinate is exp(ikm)A_s,b and lower is exp(-ikm)conjugate(A_s,b). Put F_s,b=iE'_s(k)A_s,b/sqrt(2pi). The actual open spectral evolution equals

    1/sqrt(2pi) integral_Ks exp[-it(c_att+b+E_s(k))]
       [exp(ikm)F_s,b+exp(-ikm)conjugate(F_s,b)]dk.        (5)

Both traveling terms have PLUS signs: substituting F=iE'A/sqrt(2pi) reproduces lower-minus-upper in (4). Record0 preparation followed by record1 projection takes (F_+-F_-)/2, with the same half-difference of conjugates for incoming. No extra sqrt2 or probability factor appears.

Finite coordinate equality extends to the l2 open-ray vector by Fourier isometry. Entire closed tails are norm-continuous, uniformly geometrically summable Hilbert-space columns; their integrals converge in norm. This avoids assigning a finite norm to an open stationary wave. Closed-channel projections differ between windows, so their integrated errors are added, not declared orthogonal to another window's open range.

## 3. Outgoing, incoming and all input columns

The new outgoing proof uses the ordered actual row

    Lphys=tL w^18 (t_s/dgate) dsrc^-1 Beff,

with actual source return w^36Rleft and phase rho_att=-i w^40 rho_n. It proves each sector's selected relative coefficient error<(2e-13+6600|q-pi/2|), after the NEW emitter denominator comparison. The reference second moment remains<1.9e-17 since |tf|<=1. Two old-energy input columns within a parity cost sqrt2; parity blocks combine by maximum. The resulting complete-input coefficient error in EACH sector is

    epsilon_coef=4.1e-5.                                (6)

This includes the ordered complementary-input row

    -kappa[LC Dcc^-1+(Lj+kappa^2 LC Dcc^-1 GCj)
                              D^-1 kappa^2 GjC Dcc^-1],

not just its selected column. Its amplitude<1.4e-30 and aggregate coefficient error<1e-34 are included in (6). The physical transform tL (dq/dk)=tf sqrt(dq/dk) preserves the comparison and its flux contraction. Actual wrong-window errors retain phase exp[-it(c_att+b_OUTPUT+E_s)], not the prepared input's b. Rowwise energy multiplication and Fourier synthesis preserve the complete operator bound. Only the ideal diagonal part factors into exp(-itK)W.

Projection to record1 preserves (6) by the half-difference triangle bound. Before projection, orthogonal record-X ranges and seed weights1/sqrt2 also preserve (6). Conjugation preserves the bound for incoming errors. The ideal incoming multiplier is W* in the fixed real common basis, with conjugate Fs; its norm is<.0016 by the scalar theorem. Incoming and outgoing occupy the SAME ray; their errors are added. Hence the represented open record1 map differs from (1) by

    <.0016+2 epsilon_coef=.001682, uniformly t>=0.        (7)

Every bound is an operator bound before an input is chosen, so arbitrary passive-reference tensoring leaves it unchanged.

## 4. Actual full8 inverse and local recovery integration

Use the full emitter inverse margin from the new emitter argument,

    ||T_s||<1/[c sqrt(delta^2+gamma^2)], c=1/1.03,
    ||DeltaG||<aG+bG|delta|, aG=1e-45, bG=1.27e7.

The selected scalar margin .98 is NOT substituted for c. The energy slope follows from67000|q-pi/2| and |delta|>=.0053|q-pi/2|. The new recovery and its check give

    ||L_s||<4e5,
    ||DeltaL||<=4121+5.5e9|delta|.

L includes every nonemitter finite site, particularly old gate port o, and every slow CLOSED tail. It excludes only the slow propagating component beginning at m=0. Both lips satisfy these full-input bounds. The exact ordered difference is

    DeltaFcore=[kappa^2 T_+ DeltaG T_-;
        -kappa DeltaL T_- -kappa^3 L_+ T_+ DeltaG T_-].    (8)

The direct DeltaL term is retained. With record half-difference, Stone's two lips give prefactor1/(2pi) for the corresponding integral of an upper bound. Define

    IG=2aG atan(d/gamma)/gamma+bG log(1+d^2/gamma^2),
    IL=8242 asinh(d/gamma)+1.1e10(sqrt(d^2+gamma^2)-gamma).

Since d/gamma<720000, log(1+720000^2)<28, IL<123894 and IG<3.56e8. These are elementary enclosures; no numerical spectral integration is used. On each window the emitter and other recovered norms satisfy

    Ecore <= kappa^2 IG/(2pi c^2)<6.1e-9,
    Bcore <= kappa IL/(2pi c)+kappa^3(4e5)IG/(2pi c^2)
           <.000198*(1.03)+2.6e-11 <.000204.

The displayed .000204 bound has enough strict slack to include sqrt(Ecore^2+Bcore^2); in particular that combined norm is<.000205. Summing both windows therefore gives the convenient safe bound

    epsilon_local=.000410.                              (9)

This includes all finite coordinates and all closed tails, not merely the endpoint or selected channel. Time phases have modulus one. It adds no omitted spectral charge to (3).

## 5. All-time infinite record-1 theorem and instrument meaning

Combining (3), (7), (9) gives the actual, subnormalized all-time bound

    ||A1(t)-T1(t)|| <.00129+.000410+.0016+2*.000041
                    =.003382<epsilon_infinity=.0034,
                                         every t>=0.    (10)

For normalized old/reference input psi and p_psi(t)=||A1(t)psi||^2,

    max(0,r(t)-.0034)^2 <=p_psi(t)<=min(1,(r(t)+.0034)^2).

When r(t)>.0034 the normalized successful vector differs from T1(t)psi/r(t) by at most2*.0034/r(t). There is no relative early-herald claim when r is tiny.

For the trace-nonincreasing successful CP map Phi_t(rho)=A1 rho A1*, and comparator Psi_t(rho)=T1 rho T1*, the completely bounded trace norm (diamond norm) difference is at most2*.0034, since both map operators have norm<=1. Tracing head/source registers is contractive, leaving comparator r(t)^2 e^-itK W rho W* e^itK on the old register, with the passive reference untouched. Conditioning on success is nonlinear in general; no normalized-channel diamond bound is inferred. These statements concern ONE chosen read, not a sequence of measurements.

## 6. Separate asymptotic COMPLETE unconditioned theorem

Let U(t)=exp(-itH)V, without record projection. Then

    limsup_(t->infinity)||U(t)-T1(t)||
                            <=.00129+.000041=.001331.   (11)

To prove this, first retain both sectors rather than applying the record half-difference. On each compact window the full finite-coordinate boundary columns are continuous and bounded for fixed nonzero kappa, by the actual inverse margins. Each closed-tail column is also continuous as an l2 vector, by uniform geometric domination with root<1/160000. The resulting Hilbert-space spectral density is L1. Its Fourier transform tends to zero in norm: approximate in L1 by finite sums of fixed vectors times interval indicators, whose Fourier transforms vanish. The finite old-input dimension promotes column convergence to operator-norm convergence. This removes the represented finite/core/closed-tail contribution qualitatively in BOTH sectors, regardless of the numerical constant in (9).

Second, actual incoming coefficient matrices are L2 on compact K_s, including wrong-window rows. Their phase -km-tE_s(k) has derivative -(m+tE'_s(k)), with E'_s>1.99e-6. For smooth interior coefficients, integration by parts gives amplitude bounds C/(m+vt) for m>=0 and large t, whose squared sum tends to zero. Smooth approximation in L2 and Fourier contraction extend this to the actual sharply cut coefficients. Thus the entire represented incoming wave vanishes on the physical positive halfline. This uses actual L2 coefficients, not an assumption that the small reference incoming estimate tends to zero.

Third, each sector's remaining outgoing error is at most epsilon_coef. Orthogonal record-X ranges average the squared errors with weights1/2. The ideal signs s reconstruct record1; no unchecked record0 component is discarded. Adding the ONE omitted actual state proves (11). Passive references preserve the operator estimate.

For sufficiently large t define Tnorm(t)=T1(t)/r(t). Its limiting normalization cost is1-sqrt(ps)<5.6e-7, using (2). Hence

    limsup ||U(t)-Tnorm(t)|| <.001332,
    liminf inf_(||psi||=1) ||P1 U(t)psi||^2
                                      >=1-(.001332)^2. (12)

This is a complete unconditioned target-state approximation, including blank upstream heads, source vacuum and record1, with literal common scalar, old aging and W. It supplies no numerical onset for the sharper complete-state estimate and no convergence of the error to zero. Omitted point/singular spectrum may persist within its charged norm. Its associated complete pure-output CP-map asymptotic distance is at most twice the vector-map ceiling. This asymptotic statement applies to the INFINITE apparatus only.

## 7. Finite apparatus, absolute horizon and single-read guarantees

Take M=5,000,000,000 NEW slow sites m=0,...,M-1, retaining gate o separately. The exact finite cap is g n_r(M-1); all compensation occupations above are retained. At M=1 the first occupation and cap are separate blocks at the same site, with no later occupation or internal slow bond. The finite one-head operator is precisely H_M=P H P, not an absorbing end. The checked counts in this unmerged PSD decomposition are

    heads M+236 =5,000,000,236;
    total physical qubits M+241 =5,000,000,241;
    head edges M+237 =5,000,000,237;
    positive blocks 2M+277 =10,000,000,277.

The five shared qubits are four old/source plus one record; passive references are not counted. Receiver diagonals2j do not bound all physical incident loads; original source loads and shared B remain.

Use weight f=0 on upstream/gate and firstslow, f(rm)=m. Only internal g bonds acquire nonzero weight increments; the connector tau_s has zero increment. The checked weighted Duhamel estimate for the entire evolved seed, embedded in the infinite space, is

    ||U(t)-embed U_M(t)||
       <=exp[-a(M-1)] [exp(2g sinh(a)|t|)-1]/[2sinh(a)].

All internal coordinates and both sectors are included. With a=1, T=1e15 and0<=t<=2T this is<1.2 exp[-M+4gT sinh1]<1.2 exp(-2e8)<1e-6. This supplies no infinite-time finite theorem, but it does transfer (10) on the entire absolute horizon. Thus

    ||embed A1,M(t)-T1(t)||<epsilon_M=.003401,
                                         0<=t<=2e15.    (13)

For EVERY single chosen read time in [1e15,2e15], (2) and (13) imply uniformly over old/reference inputs

    success probability >=(r(t)-.003401)^2 >.9932;
    normalized successful vector error <2*.003401/r(t)<.00681;
    successful CP-map diamond distance <.006802.

The CP comparator is the same subnormalized T1 map; after tracing apparatus it is r(t)^2 times the ideal old/reference unitary channel. The vector comparator is the normalized infinite-space packet beta_t/r(t), with the finite state embedded. No truncation or renormalization of a finite target packet is performed without a charge.

There is also a weaker but quantitative COMPLETE unconditioned finite-vector statement on this window. For a normalized input, let y=T1 psi/r. Since ||embed U_M||=1 and the target has record1, (13) gives Re<y,embed U_M psi>>=r-epsilon_M. Therefore

    ||embed U_M(t)-Tnorm(t)||
        <=sqrt[2(1-r(t)+epsilon_M)]<.083.               (14)

This operator estimate includes failure, source and all head coordinates; it is not the sharper asymptotic .001332 bound. Its complete-channel diamond estimate is at most .166 by the same isometry inequality. The finite read interval is justified by actual new composition plus the slow-reference onset and exact resource transfer, not by an old attached runtime.

## Scope and independent check requested

The three scopes differ: (10) is all-time infinite SUBNORMALIZED record1 accuracy; (12) is qualitative infinite COMPLETE asymptotic accuracy; (13)–(14) are finite single-read guarantees only on the stated absolute horizon/window. Finite recurrence and reflected returns can occur later. No permanent halt, irreversible completion latch, repeated-measurement behavior, autonomous reset/reuse or stopping-time protocol follows.

The supplied seed, exact correlated nominal coefficients including slow compensation, installed interactions, record identification/readout and physical-time units remain premises. Nothing here supplies a native coefficient generator, precision/tolerance theorem, native seed preparation or native Record semantics. The inherited source calibration and reference moment retain their previous qualifications. Distinct review should check the full8 margin, both-lip factors, wrong-window phases, single omitted charge, sector recombination, qualitative Hilbert-space limit, and finite comparator/error distinctions. This authored composition must not be labeled independently checked until that distinct review is complete.
