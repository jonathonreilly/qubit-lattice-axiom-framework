# Slow output storage for a static local coherent record

**Type:** bounded_theorem
**Status:** conditional mathematical support; unaudited.

Runner: [control_output_family_2026_10_17.py](../scripts/control_output_family_2026_10_17.py).

Publication evidence boundary: the analytical argument and its named supporting proofs remain controlling. The shared runner supplies finite algebra, matrix, flux and budget corroborations only; it does not prove the continuum/contour estimates, certify all parameter families, or establish physical realization. Statements below about no new computation describe the original authoring stage; its exact source is preserved in `outputs/control_family_landing_2026_10_17/originals/SLOW_OUTPUT_LOCAL_RECORD_FINITE_WINDOW_BOUNDED_THEOREM_NOTE_2026-10-17.md`. Historical author reviews are provenance, not independent landing authority.

Status: conditional mathematical note prepared for review. Component and distinct synthesis checks are complete; publication integration review is recorded separately. The exact supplied Hamiltonian, initial state and calibration premises remain conditional. No retained audit status is asserted.

Replacing the final receiver hopping by g=10^-6, while retaining its carrier diagonal2j, gives a finite single-read construction with 5,000,000,241 physical qubits. Its absolute record1-map error is below .003401 through time 2×10^15, and record1 probability exceeds .9932 throughout [10^15,2×10^15]. Time is dimensionless. These are sufficient mathematical bounds, not practical engineering estimates.

| Scope | Bound and comparator |
|---|---|
| Infinite device, every t>=0 | Subnormalized record1 map error<.0034 against the common outgoing packet and literal old operation |
| Infinite device, asymptotically | Complete unconditioned normalized-target state-map limsup error<.001332; no quantitative onset for this bound |
| Finite device,0<=t<=2×10^15 | Subnormalized record1 map error<.003401 against the same embedded infinite-space packet |
| Finite device,10^15<=t<=2×10^15 | Single-read success>.9932; normalized successful vector error<.00681; complete unconditioned vector error<.083 |

All map bounds include arbitrary passive references and every apparatus output. The finite complete-state bound .083 is deliberately distinguished from the sharper qualitative infinite asymptotic ceiling. Early rare successful reads have an absolute subnormalized bound, not a uniform relative-correctness theorem.

The [earlier attached-record note](AUTONOMOUS_LOCAL_RECORD_FINITE_WINDOW_BOUNDED_THEOREM_NOTE_2026-10-17.md), associated with PR9675, supplies a comparison at the SAME finite single-read metric and horizon: old M=1.5×10^13, branch error<.004501 and success>.991; new M=5×10^9, error<.003401 and success>.9932. Here M counts NEW slow sites, whereas the old M includes its gate output origin; exact physical counts are 15,000,000,000,240 versus 5,000,000,241. The receiver count is reduced by a factor 3000 under these sufficient bounds. Both have the same proved onset 10^15 and absolute horizon 2×10^15, so there is no speed improvement established. The infinite complete asymptotic ceiling worsens from .001061 to .001332. There is no blanket accuracy or speed advantage, no optimality claim, and no removal of coefficient-supply or initialization assumptions.

## Supplied static construction and changed positive blocks


The old system consists of two qubits with K=2I+Z1Z2 and literal target

    W=[(9+12i)I+(-16+12i)X1X2]/25.

There is one shared pair of source qubits A,B, not one copy per arm. With n=(I-Z)/2 and a=|0><1|, its internal Hamiltonian is

    B=K+DeltaA nA+DeltaB nB
      +h_src(nA+nB-aA* aB-aB* aA)+u_AB nA nB
      +gA nA(I+X1)+gB nB(I+X2).

Head occupations at positions c0,c1 of each original arm supply contacts VA=lambdaA(I+XA)+mu0 I and VB=lambdaB(I+XB)-nu I, with the positive-block realization in the original source. The exact terminating-decimal coefficients are:

| J | h_src | gA | gB |
|---:|---:|---:|---:|
| .030021107107032 | 3.999349697888060 | .996878563816670 | .599319315560298 |

| lambdaA | lambdaB | mu0 | nu |
|---:|---:|---:|---:|
| 3.801781381581202 | 2.575033765788497 | .321494607058201 | 1.459892813020969 |

| DeltaA | DeltaB | u_AB |
|---:|---:|---:|
| 2.192035527016003 | 2.186826508897014 | .544607276405587 |

Put k0=2 arctan(1/4.510351185997098), C0=cos k0, S0=sin k0. The nominal new-lead parameters are

    j=J(1-C0), tau_c=sqrt(j J S0), kappa=10^-8,
    .0027<j<.003.

The inherited original arm filter at positions 20/21 uses hopping -J S0/C0 and diagonal shift -J/C0. Its positive vacancy coefficient is beta_f=J[(1+S0)/C0-1]. Converter vacancies have gamma_c=tau_c-j; original junction vacancies have gamma_J=(sqrt(2)-1)J. The scalar after adding the record gate is

    c_att=2nu+2beta_f+4gamma_J+4gamma_c
                             +4(sqrt(2)-1)j.

This is a global scalar, present before the head reaches the gate. K is retained in B and need not commute with the source contacts. Only the common scalar is factored from actual evolution.

For definiteness the cubic-lattice embedding uses old1=(0,0,0), old2=(1,0,0), A=(0,1,0), B=(1,1,0). Arm0 is (n,1,1), 0<=n<=36, followed by (36,1,2),(36,1,3),(37,1,3),(38,1,3),(38,1,2),(38,1,1),(39,1,1),(40,1,1). Arm1 is (n,1,-1), 0<=n<=41, followed by (41,2,-1),(41,2,0),(41,2,1). Both have 45 vertices. The junction ports are out=(41,1,1) and in=(40,2,1), with hopping block -JU for U=2^-1/2[[1,1],[1,-1]]. Retain old-J port sites out_m=(41+m,1,1), in_m=(40,2+m,1), 0<=m<=40. Each converter joins its last old site to the first new site. The input new sites are (40,43+n,1), 0<=n<=20; the emitter is (40,64,1). The retained output cable is v_n=(82+n,1,1), 0<=n<=17.

The new local gate is specified first in local coordinates. Its record is R=(0,0,0). Arm0 is (1,0,0),(2,0,0),(2,1,0),(1,1,0),(1,2,0),...,(1,8,0). Arm1 is (-1,0,0),(-1,1,0),...,(-1,8,0),(-1,8,1),(0,8,1). Each has eleven heads. Add ports p=(0,8,0), o=(1,8,1) and the four signed square bonds -jU. On arm1 replace bonds y=2--3 and y=5--6 by phase cells of hopping -sqrt(2)j, each with positive occupations (2-sqrt(2))j at its two endpoints. At each square site add vacancy (sqrt(2)-1)j(I-n). Couple both terminals to the SAME record by j n_T(I+X_R). Apply the rigid map

    F(x,y,z)=(108-y,1+x,1+z).

The actual gate input is (100,1,1), its output is (100,2,2), and its record is (108,1,1). Join v17 to the input by -j. Retain o as a finite gate site. The new slow ray begins at r_m=(100,3+m,2), m>=0, with hopping -sqrt(jg) from o to r_0 and hopping -g between successive new sites, g=10^-6. The old port and first slow site are distinct and counted once each. New gate vertices lie at first coordinate 100 through 108; old retained heads lie at first coordinate at most 99. The slow ray is disjoint from the gate and joined only through the installed connector at o. All installed bonds and contacts are nearest-neighbor; extra geometric adjacencies remain uninstalled under the selective-coupling premise.

Every real head hopping h uses Q(h)=|h|(n_x+n_y)+h(a_x* a_y+a_y* a_x), PSD on all two-qubit occupations. The emitter bond is instead j(n_e+n_end)-kappa(exchange), with positive onsite j n_e; this gives both one-head diagonals 2j without a kappa-dependent compensation. All source, contact, occupation and vacancy terms retain their supplied positive realizations. The new terminal contacts are PSD on the full head/record space, of norm 2j each; their shared record incident load is 4j. Original large source loads remain present; no all-site norm cap of 2 is claimed. The delivered seed has the emitter occupied, all other heads blank, source vacuum and record0, with arbitrary old/reference input.

The exact inventories and full-space block identities are in the `outputs/attached_record_2026_10_17/source_checks/bandcenter_resources/PROPOSAL.md`, `outputs/attached_record_2026_10_17/source_checks/autonomous_record_route/PROPOSAL.md` and `outputs/attached_record_2026_10_17/source_checks/record_attached_kernel/PROPOSAL.md`. Their checks are preserved alongside them. These supplied coefficients and states are not derived here from native framework physics.

The changed full-space positive blocks are Q(-tau_s) on the connector, Q(-g) on each slow bond, and

    (j-tau_s)n_o,  (2j-tau_s-g)n_r0,
    2(j-g)n_rm for m>=1,   tau_s=sqrt(jg).

All coefficients are positive because0<g<j. They restore the old port and every slow one-head diagonal to2j; the shared internal B is unchanged. No new vacancy or common scalar is introduced. A finite receiver retains m=0,...,M-1 and adds cap g n_r(M-1), exactly the compression of the omitted exchange. At M=1 there is no internal slow edge and no later-site occupation: tau_s+(2j-tau_s-g)+g=2j. Compensation and cap are distinct positive blocks at that site. This is a reflecting exact compression, not an absorber.

At the new sites incident block-norm sums are2j+tau_s+g at the first site (2j+tau_s when M=1),2j+2g at later interior sites, and2j+g at the final site. At gate o the sum is3sqrt(2)j+tau_s. Large original source loads remain unchanged. Slow transport is not a claim that the full Hamiltonian or every local load has norm of order g.

## Actual map and slow reference packet

Retain the selective installed-pair premise. Let H be the bounded self-adjoint seeded one-head operator of this infinite device; no bounded infinite many-head norm is asserted. V embeds arbitrary four-dimensional old input with emitter occupied, all other heads blank, shared source vacuum and record0. The record-X sectors s=+,- are conserved. P1 projects onto computational record1, retaining ALL remaining coordinates. Define A1(t)=P1 exp(-itH)V.

Use literal K=2I+Z1Z2 and W=[(9+12i)I+(-16+12i)X1X2]/25. They have a common real basis labeled by old energy b=1,3 and parity, with W eigenvalues (-7+24i)/25 and1. They commute with each other; no commutation of K with H is assumed.

Set h=4e-6, q in J=[pi/2-h,pi/2+h], w=exp(iq), E(q)=2j(1-cos q), delta=E(q)-2j, gamma=kappa^2/j. The slow momentum k obeys delta=-2g cos k on its principal real interval K_s centered at pi/2, halfwidth H_s=asin((j/g)sin h)<.01201. The original converter momentum is k_old(q)=2 asin(sqrt(j/J) sin(q/2)), using its branch near k0. The fixed unimodular zeta is the unchanged single calibration phase, equivalently rho_n(q)=zeta exp(172i k_old(q)); no phase is selected separately by input. It is not the slow momentum k. Define

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

## Changed load and actual spectral proof chain

For the scalar interface, the old endpoint and first slow coordinate are distinct. Solving their two boundary equations gives

    rL=(w-v)/(v-w^-1), tL=sqrt(j/g)v(1+rL), v=exp(ik),
    |rL|^2+|tf|^2=1, tf=sqrt(g sin k/(j sin q)) tL.

At the band center rL=0 and tf=i. The slow surface resolvent is -v/g, so the new old-port selfenergy is -jv rather than -jw. This actual changed load is included in the gate inversion; matching at one point alone would not establish the theorem. Throughout the band the full gate inverse is<38/j, and its forced-column recovery including closed slow tails is<5.064. The input-plane selected return is<=1540u, its sector difference<=68u, u=|q-pi/2|; the eighteen-edge cable supplies the return phase w^36. The resulting source selected feedback margin is>.9937. Closed-return suppression uses the complete root and inverse bounds, not the propagating scalar formula for closed channels.

The modified background Green comparison has full8 operator envelope

    ||Gslow-Gref||<8e-18+1.51e6u
                          <=8e-18+2.85e8|delta|.

Complement off-diagonal and closed blocks retain their explicit <2e-24 margins, complement emitter inverse<6, selected ImD>326kappa^2 and full inverse norm<1.03/sqrt(delta^2+gamma^2). The full8 reference Gref is the direct sum of endpoint j chains shifted by every B eigenvalue and the common scalar, including the six excited-source directions in each parity fiber. Only its four prepared-vacuum restrictions have literal old energies b=1,3; those seed measures are normalized and absolutely continuous. The two distinct b=1 and b=3 continuum supports of width4j are disjoint. On either physical window, other old-energy reference densities vanish, but their real resolvents remain in the full comparison. No scalar comparison discards these complement columns.

The resolvent identity with both full inverse bounds and the imaginary jump gives the seed MATRIX density comparison with prefactor1.05 kappa^2/pi, integrated against (8e-18+2.85e8|delta|)/(delta^2+gamma^2). The constant term integrates as2 atan(d/gamma)/gamma; the slope integrates as log(1+d^2/gamma^2). The resulting norm error is<2.8e-7 per window and<5.6e-7 for their union. The reference outside mass<1.1e-6 therefore gives actual outside mass<1.66e-6 by measure normalization and the Loewner norm bound. This energy-resolved argument avoids interpreting the worst-band relative error as omitted amplitude. Full finite inverse/root continuation gives the local absolute continuity used below; all spectral types outside the windows remain charged.

## Full seed measure and exact physical Stone synthesis

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

## Outgoing, incoming and all input columns

The outgoing proof uses the ordered actual row

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

## Actual full8 inverse and local recovery integration

Use the full emitter inverse margin from the modified-device emitter argument,

    ||T_s||<1/[c sqrt(delta^2+gamma^2)], c=1/1.03,
    ||DeltaG||<aG+bG|delta|, aG=1e-45, bG=1.27e7.

The selected scalar margin .98 is NOT substituted for c. The energy slope follows from67000|q-pi/2| and |delta|>=.0053|q-pi/2|. The full recovery and its check give

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

## All-time infinite record-1 theorem and instrument meaning

Combining (3), (7), (9) gives the actual, subnormalized all-time bound

    ||A1(t)-T1(t)|| <.00129+.000410+.0016+2*.000041
                    =.003382<epsilon_infinity=.0034,
                                         every t>=0.    (10)

For normalized old/reference input psi and p_psi(t)=||A1(t)psi||^2,

    max(0,r(t)-.0034)^2 <=p_psi(t)<=min(1,(r(t)+.0034)^2).

When r(t)>.0034 the normalized successful vector differs from T1(t)psi/r(t) by at most2*.0034/r(t). There is no relative early-herald claim when r is tiny.

For the trace-nonincreasing successful CP map Phi_t(rho)=A1 rho A1*, and comparator Psi_t(rho)=T1 rho T1*, the completely bounded trace norm (diamond norm) difference is at most2*.0034, since both map operators have norm<=1. Tracing head/source registers is contractive, leaving comparator r(t)^2 e^-itK W rho W* e^itK on the old register, with the passive reference untouched. Conditioning on success is nonlinear in general; no normalized-channel diamond bound is inferred. These statements concern ONE chosen read, not a sequence of measurements.

## Separate asymptotic COMPLETE unconditioned theorem

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

## Finite apparatus, absolute horizon and single-read guarantees

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

## Proof sources, status and verification limits

The exact-byte `outputs/slow_record_2026_10_17/SOURCES.json` records all source/check hashes and explicit original-path to repository-path mappings. New artifacts are preserved under source_checks in this packet; inherited artifacts remain in the `outputs/attached_record_2026_10_17/SOURCES.json`, without copying its52 files again. Relative links inside immutable research sources retain their original research-directory meaning; the manifest supplies their portable repository resolution. The publication note's links use repository-relative targets.

The unchanged source, geometry, positive-block calibration and converter premises are those of the [original endpoint note](REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md) and [nominal converter note](NOMINAL_BANDCENTER_CONVERTER_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md). The [weighted finite-transfer note](HOPPING_CONTROLLED_FINITE_OUTPUT_TRANSFER_BOUNDED_THEOREM_NOTE_2026-10-17.md) supplies the general compression framework; the changed-g resource argument reconstructs its hypothesis and cut bound here.

| New proof leg | Source | Selective check |
|---|---|---|
| Scalar interface and PSD realization | `outputs/slow_record_2026_10_17/source_checks/same_carrier_slow_lead/PROPOSAL.md` | `outputs/slow_record_2026_10_17/source_checks/same_carrier_slow_lead_check/REVIEW.md` |
| Actual gate load and reference planes | `outputs/slow_record_2026_10_17/source_checks/slow_lead_gate_load/PROPOSAL.md` | `outputs/slow_record_2026_10_17/source_checks/slow_lead_gate_load_check/REVIEW.md` |
| Full emitter inverse and seed matrix mass | `outputs/slow_record_2026_10_17/source_checks/slow_lead_emitter/PROPOSAL.md` | `outputs/slow_record_2026_10_17/source_checks/slow_lead_emitter_check/REVIEW.md` |
| All finite coordinates and closed tails | `outputs/slow_record_2026_10_17/source_checks/slow_lead_recovery/PROPOSAL.md` | `outputs/slow_record_2026_10_17/source_checks/slow_lead_recovery_check/REVIEW.md` |
| Actual full-input outgoing coefficients | `outputs/slow_record_2026_10_17/source_checks/slow_lead_outgoing_profile/PROPOSAL.md` | `outputs/slow_record_2026_10_17/source_checks/slow_lead_outgoing_profile_check/REVIEW.md` |
| Slow scalar reference and onset | `outputs/slow_record_2026_10_17/source_checks/slow_lead_reference_packet/PROPOSAL.md` | `outputs/slow_record_2026_10_17/source_checks/slow_lead_reference_packet_check/REVIEW.md` |
| Exact counts and finite transfer | `outputs/slow_record_2026_10_17/source_checks/slow_lead_resources/PROPOSAL.md` | `outputs/slow_record_2026_10_17/source_checks/slow_lead_resources_check/REVIEW.md` |
| Complete synthesis and three scopes | `outputs/slow_record_2026_10_17/source_checks/slow_lead_alltime_composition/PROPOSAL.md` | `outputs/slow_record_2026_10_17/source_checks/slow_lead_alltime_composition_check/REVIEW.md` |

These are selective same-model analytical checks with shared ancestry and disclosed source exposure, not blind independent recalibration. The publication drafter authored the emitter, scalar reference and synthesis and checked several ancestors; packaging does not independently recertify them. Original exact matrix evidence is inherited, not rerun. No new scientific runner, parameter sweep, full pipeline or audit was executed for this draft. Publication copying, link and dependency-graph verification, and final integration-review evidence are recorded separately. Preparing this source packet involved no new scientific runner, full pipeline or audit, and changed no model or editable prompt files.

Historical component headers reporting a then-pending check describe their drafting stage; the exact paired checks control only their stated scope. Earlier scalar matching alone, old actual mass/runtime substitution, selected-column-only aggregation, and worst-band density-to-mass shortcuts are not premises. Historical failed contact alternatives, early-relative-herald obstructions and rejected routes in ancestry are not converted into global impossibility claims. Correction histories in the inherited manifest remain recovery evidence; controlling corrected versions and the endpoint erratum retain their existing qualifications.

The infinite lead is essential to all-time and asymptotic assertions. Finite recurrence and reflected return remain possible beyond the horizon. This is a single chosen read on a coherent record; continuous or repeated monitoring alters the dynamics and is not covered. No permanent halt, irreversible latch, autonomous reset/reuse or stopping-time protocol follows. The supplied product seed, exact correlated nominal coefficients, installed-pair selectivity, readout identification and physical-time units remain assumptions. No native coefficient generator, manufacturing tolerance, native preparation or native Record semantics is derived.
