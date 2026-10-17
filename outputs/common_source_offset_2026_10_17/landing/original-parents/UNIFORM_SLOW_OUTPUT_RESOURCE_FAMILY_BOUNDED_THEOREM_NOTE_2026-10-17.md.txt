# Uniform slow-output resource family and fixed-dimensionless scaling

Status: conditional mathematical note prepared for review. The six component arguments have distinct selective checks. This publication synthesis requires its own integration review and is not retained audit certification. Exact nominal construction, calibration and supplied-state premises persist.

This note gives parameter-dependent sufficient error and resource bounds for the actual slow-output record device. It then proves an exact scaling implication: reducing emitter coupling by a factor a and slow hopping by a^2 can retain the same certified receiver length while increasing the read-time window by a^-2, provided the base data satisfy explicit common error inequalities. A separately checked example demonstrates nonempty sufficient conditions; no optimized frontier, faster operation, necessary resource lower bound or native coefficient supply is asserted.

The three dynamical scopes remain distinct:

| Scope | Conclusion |
|---|---|
| Infinite apparatus, every t>=0 | Explicit absolute subnormalized record1-map bound epsilon_infinity |
| Finite apparatus, one selected read in [T,2T] | Success and state-error bounds if R_T>epsilon_M, with exact cap/resources |
| Each fixed positive parameter triple, infinite apparatus only | Complete normalized-target limsup bound and a success-probability liminf bound; no uniform asymptotic onset |

All maps retain the entire apparatus output and arbitrary passive references. A separate restricted receiver-error lemma makes a sufficient finite-time implementation budget explicit; it does not certify the whole device or necessary manufacturing precision.

## Actual family and exact physical premises

Use exactly the geometry, original source coefficients, filter, converters, input stub ell=20, eighteen-site cable,24-head record gate and shared registers of the [parent slow-output construction](SLOW_OUTPUT_LOCAL_RECORD_FINITE_WINDOW_BOUNDED_THEOREM_NOTE_2026-10-17.md), at the source identity in the manifest. That note is associated with PR9676; its fixed numerical performance is not imported into this family. Keep the supplied original j with .0027<j<.003 and all original source/calibration parameters fixed.

Only the emitter off-diagonal coupling kappa and the final receiver hopping g vary physically. The bandwidth h is an analysis cutoff, not a hardware control. Require

    0<kappa<=10^-8, 0<g<=10^-6, 0<h<=4e-6,
    gamma=kappa^2/j, d=2j sin h,
    H=d/gamma>=100, L=g/gamma>=100, H/L=d/g<=.024.       (1)

Here H is a dimensionless bandwidth ratio; the physical Hamiltonians below are denoted mathcal H. The last constraint also forces L>4000. All parameters are strictly positive; no endpoint at kappa=0 or g=0 is part of the theorem.

The retained gate output is o=(100,2,2). The DISTINCT first slow site is r_0=(100,3,2), with r_m=(100,3+m,2). Its connector is -tau_s, tau_s=sqrt(jg), and subsequent receiver hoppings are -g. The old converter coefficient tau_c=sqrt(j J S0) stays unchanged. With n=(I-Z)/2 and lowering operator a, define the fullspace positive exchange

    Q(-b)=b(n_x+n_y-a_x* a_y-a_y* a_x), b>=0.

Install Q(-tau_s), the receiver Q(-g) bonds and occupations

    (j-tau_s)n_o,
    (2j-tau_s-g)n_r0,
    2(j-g)n_rm, m>=1.                                  (2)

All coefficients are positive on (1). These terms preserve the old gate diagonal and give each receiver one-head diagonal2j. The emitter uses the same structured positive block j(n_e+n_end)-kappa(exchange), plus j n_e, so its diagonal remains2j as kappa varies. All remaining physical blocks, selective installed-pair assumptions, old/source interactions and record contacts are exactly the parent construction. There is one shared old/source system and one record, not a copy at every head coordinate.

No new vacancy scalar appears. Retain literal

    K=2I+Z1Z2,
    W=[(9+12i)I+(-16+12i)X1X2]/25,
    c_att=2nu+2beta_f+4gamma_J+4gamma_c+4(sqrt(2)-1)j,

with the unchanged parent definitions of beta_f, gamma_J and gamma_c. K remains inside the interacting shared B; it is not assumed to commute with the physical Hamiltonian. The supplied seed is emitter occupied, all other heads blank, source vacuum and computational record0, with arbitrary old input. Exact coefficient correlations, seed preparation, readout identification and dimensionless physical units remain supplied premises.

For a finite receiver retain M>=1 NEW sites r_0,...,r_(M-1) and add cap g n_r(M-1). This is exact one-head compression. For M=1 there is no internal slow bond and no later occupation: tau_s+(2j-tau_s-g)+g=2j. First-site compensation and cap are distinct blocks. The unmerged inventory is

    head qubits=M+236, physical qubits=M+241,
    head edges=M+237, positive blocks=2M+277.             (3)

The five shared qubits are four old/source and one record; passive references are not counted. Small g controls receiver propagation, not all physical incident loads or the full many-head norm. The large original source loads persist.

## Reference packet and exact parameter functions

Let U(t)=exp(-it mathcal H_infinity)V be the seeded one-head map, P1 the computational-record1 projection retaining everything else, and A1(t)=P1 U(t). This invariant-sector Hamiltonian is bounded for each parameter triple; no bounded infinite many-head norm is asserted.

On q in[pi/2-h,pi/2+h], put w=exp(iq), E(q)=2j(1-cos q), delta=-2j cos q and Dref=delta+gamma w. Slow momentum k obeys delta=-2g cos k, so q(k)=pi/2-asin((g/j)cos k) on the centered slow interval with halfwidth asin(d/(2g)). The ORIGINAL converter momentum is k_old(q)=2asin(sqrt(j/J)sin(q/2)); it is not slow k. Retain the fixed common unimodular calibration phase zeta and define

    F(q)=kappa E'(q) zeta exp[i61q+i172k_old(q)]
                                /[sqrt(2pi)jDref],
    tf(q)=exp[i(q+k)/2]sqrt(sin q sin k)/sin((q+k)/2),
    Fs(k)=tf(q)F(q)sqrt(dq/dk), dq/dk=g sin k/(j sin q),
    beta_t(m)=1/sqrt(2pi) integral Fs(k)
                          exp[ikm-it(2j-2g cos k)]dk, m>=0.

Every integral in this paragraph is over the corresponding hard band. The exact phase is61.5q+.5k+172k_old(q), referred to firstslowm0; it is not a translation by61 slow sites. The common target is

    T1(t)=exp(-it c_att) Jout[beta_t tensor exp(-itK)W],
    ps=integral |Fs(k)|^2 dk, r(t)=||beta_t||.            (4)

Jout places source vacuum, blank other heads and record1 with the slow packet. No input-dependent phase alignment is allowed.

For an explicit reference mass set A=2j-gamma, alpha=gamma/A and y_h=tan h. The full old-j emitter-chain reference has total mass1, and its hard-band mass is exactly

    p0=4kappa^2/[pi A^2(1-alpha^2)]
                    *[atan(y_h/alpha)/alpha-h].         (5)

The exact scalar reflection is rL=(w-v)/(v-w^-1), v=exp(ik), and

    ps=p0-R, R=integral |rL(q)|^2 |F(q)|^2 dq,
    1-p0<.68/H, R<.043 H/L^2,
    ps>pbar:=1-.68/H-.043H/L^2>.9931.                    (6)

Thus normalization is well defined but must not be replaced by unit mass. These are mathematical reference measures; actual mass is established separately below.

Define the unnormalized reference moments

    M2=integral |q-pi/2|^2 |F(q)|^2 dq,
    MD2=integral delta^2 |F(q)|^2 dq.

They can be evaluated by their exact definitions or bounded by

    M2<=4kappa^2 h/[pi(2j-gamma)^2]*(h/sin h)^2,
    MD2<=16kappa^2 j^2 h/[pi(2j-gamma)^2].                (7)

No fixed old numerical tail or moment is inserted into the varying-parameter formulas.

## Uniform actual endpoint and spectral ingredients

The [uniform endpoint proof](../outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_endpoint/PROPOSAL.md) reconstructs the actual altered load at the old plane. The slow surface function is -v/g and its connector selfenergy is -jv. The domain d/g<=.024 keeps |v-w|<.01201; the gate one-output inverse stays<38/j and its forced recovery, including closed tails, stays<5.064. As g decreases, the physical closed-tail factor sqrt(j/g) is paired with a decaying root O(g); it is not bounded separately. The seven closed slow roots remain<1/160000.

The selected source-facing return is bounded by33u+.252|delta|/g<.0062, u=|q-pi/2|, whereas its record-sector difference is<=68u. Only the latter has the same slope uniformly in g. The old individual1540u bound is NOT used across the family. The eighteen-edge cable retains its w^36 return phase and closed return<1e-63. Ordered closed elimination and selected feedback retain margin>.9937. Consequently the complete eight-coordinate endpoint comparison is

    ||Gx-Gref||<a+41000u+244|delta|/g
                       <=a+b(g)|delta|,
    a=8e-18, b(g)=41000/.0053+244/g,
    Gref=-Q/j,
    ||G+-G-||<1e-45+67000u.                            (8)

The full reference is a direct sum of j chains shifted by EVERY B eigenvalue in each parity fiber. Its four prepared-vacuum restrictions have literal old energies1 and3. The two distinct old-energy continuum supports are disjoint; the other prepared input's real resolvent remains in each window's full matrix comparison. Tiny complete complementary blocks remain<2e-24. The actual full emitter inverse satisfies

    ||De_x^-1||<1.03/sqrt(delta^2+gamma^2),
    ||Dcc_x^-1||<6, Im D_x>326kappa^2.                  (9)

The peak inverse grows as kappa tends to zero; uniformity means these displayed inequalities, not a parameter-independent peak bound.

For each FIXED positive triple the complete finite matching inverse, the nonzero selected slow velocity and threshold-separated roots give local analytic continuations and continuous boundary values on the closed windows. This proves actual seed absolute continuity there, including cutoffs, without a uniform complex-strip or decay-rate assertion. All outside spectral types are retained.

Use the common physical union I=I1 union I3, with Ib=[c_att+b+2j-d,c_att+b+2j+d]. Full matrix resolvent subtraction, the independent reference inverse1.01/sqrt(delta^2+gamma^2), and the norm-contractive imaginary part yield per-window error

    eta=1.05kappa^2/pi *[2a atan(H)/gamma
                                +b(g)log(1+H^2)],
    epsilon_sp=sqrt(min{1,1-p0+2eta}).                   (10)

The actual omitted seed amplitude is at most epsilon_sp. Two physical windows cost2eta; parity blocks combine by maximum, and coherent record0 averages squared sector norms. Wrong-window prepared columns and off-diagonal seed entries remain in this calculation. This is not four separate scalar comparisons or a transmitted-reference mass substitution.

The actual outgoing coefficient comparison, using the physical connector and flux/Jacobian, has complete-input bound

    Esel=2e-13 sqrt(ps)+400sqrt(M2)+(1.01/g)sqrt(MD2),
    Eout=sqrt(2)Esel+8.4e-25 kappa sqrt(2h).             (11)

The last term pays both complementary prepared-input rows. Wrong-window terms keep their actual output-window energy; only the ideal diagonal comparator factors exp(-itK)W. All calibration floors are retained.

## Scalar directionality and complete all-time branch theorem

The [uniform scalar proof](../outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_reference/PROPOSAL.md) supplies the RAW incoming bound

    Iin=min{sqrt(ps),2.7/sqrt(L)+sqrt(1-p0)}, t>=0.       (12)

For sigma=gamma t with L sigma>=1 the normalized outgoing complement m<=-1 obeys

    C_out(sigma)=min{1,2.1exp(-.4975sigma)
                                 +.8/[H sqrt(ps sigma)]}. (13)

At earlier times its ceiling is1. These statements retain the hard cutoff, both contour sides, the first incoming slow site m=0, physical carrier phase and transmitted normalization. Only the explicit scalar integrand is continued away from the real band, not the calibrated interacting source. The outgoing strip has depth1/(4L), and its full denominator comparison gives the.49 pole margin. The incoming auxiliary full-slow-band rectangle pays its removed hard-band mass before normalization. Physical waiting time is sigma/gamma, not a uniform time independent of the couplings.

The [uniform composition](../outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_composition/PROPOSAL.md) reconstructs actual finite-coordinate recovery using unchanged unloaded source maps and the new uniform return ceilings. It retains the nonnegligible cable closed amplitude at its origin and cancels growing root factors before bounding them. With all finite background coordinates and all slow closed tails recovered,

    L0=4e5, ||Lx||<L0,
    ||DeltaL||<=aL+bL|delta|, aL=4121, bL=5.5e9,
    ||DeltaG||<=aG+bG|delta|, aG=1e-45, bG=1.27e7.

Use the FULL inverse constant c=1/1.03, not the selected scalar.98. Define the exact envelope integrals and resulting bounds

    IG=2aG atan(H)/gamma+bG log(1+H^2),
    IL=2aL asinh(H)+2bL gamma(sqrt(1+H^2)-1),
    Ecore=kappa^2 IG/(2pi c^2),
    Bcore=kappa IL/(2pi c)+kappa^3 L0 IG/(2pi c^2),
    epsilon_local=2sqrt(Ecore^2+Bcore^2),
    epsilon_infinity=epsilon_sp+epsilon_local+Iin+2Eout. (14)

These functions may be large for an unsuitable triple. The theorem is the sufficient bound

    ||A1(t)-T1(t)||<=epsilon_infinity, every t>=0.       (15)

The proof uses the exact ordered Schur difference

    DeltaF=[kappa^2 T+ DeltaG T-;
           -kappa DeltaL T- -kappa^3 L+ T+ DeltaG T-].

Stone's rectangular jump is (F_down-F_up)/(2pi i). Real conjugation gives both lips; it does not replace a rectangular column by its adjoint. The record half-difference and two lips yield1/(2pi) per-window integration. Emitter/background ranges combine in quadrature, two energy windows add, and parity blocks combine by maximum. The represented open evolution contains BOTH plus-sign Fourier terms exp(ikm)F+exp(-ikm)conjugate(F). Its ideal incoming logical factor is W*, whose reference norm is charged by Iin; incoming and outgoing coefficient errors share the same ray and therefore cost2Eout. The single omitted actual state is charged once. This proves (15) on the full prepared input and every apparatus coordinate after record1 projection.

The successful subnormalized CP-map diamond distance is at most2epsilon_infinity, also after tracing apparatus. Conditioning on success is nonlinear; this is not a normalized-channel diamond estimate. No uniform relative early-success accuracy follows when r(t) is tiny.

## Finite single-read theorem and resource condition

Choose T>0 with L gamma T>=1, and set

    R_T=sqrt(ps)*sqrt(1-C_out(gamma T)^2),
    D_M(T)=min{2,1.2exp[-M+4gT sinh1]},
    epsilon_M=epsilon_infinity+D_M(T).                  (16)

Orthogonality of the full-lattice packet's two halfline restrictions gives r(t)>=R_T for every t>=T. Exact cap compression and the weight zero through firstslow, f(r_m)=m, give full finite/infinite map difference<=D_M(T) on[0,2T]. Only g bonds contribute to the weighted imaginary-part bound2g sinh1; the connector has zero weight increment. The one-cut Duhamel identity retains source dynamics and return paths. Thus the finite record1 map, embedded in the infinite space, differs from T1(t) by at most epsilon_M throughout[0,2T].

Impose the useful-success condition R_T>epsilon_M. For EVERY ONE chosen read time t in[T,2T], every normalized old/reference input then satisfies

    success probability >=(R_T-epsilon_M)^2,
    normalized successful-vector error <=2epsilon_M/R_T,
    successful subnormalized CP-map diamond error <=2epsilon_M,
    complete unconditioned vector error
                <=min{2,sqrt(2(1-R_T+epsilon_M))}.       (17)

Both normalized vector comparisons use the same normalized INFINITE-space target T1(t)/r(t). The useful-success condition is standing for all normalized formulas in (17), so the comparator exists. No finite target is silently truncated or renormalized. The complete-vector inequality follows from Re<y,U_M psi> >=r(t)-epsilon_M for the ideal unit vector y in record1; it does not import an asymptotic rate.

For a chosen transfer allowance epsilon_tr>0 it suffices to choose

    M>=max{1,ceil(4gT sinh1+log(1.2/epsilon_tr))}.         (18)

Desired success p_* and successful-vector tolerance e_* are sufficiently certified by R_T>epsilon_M, (R_T-epsilon_M)^2>=p_* and2epsilon_M/R_T<=e_*. The general theorem does not select these targets; a separate example below shows nonemptiness. The exact inventories are (3), with no new shared register or measurement-resource claim.

## Separate complete infinite asymptotics

For EACH fixed strictly positive triple in (1),

    limsup_(t->infinity)||U(t)-T1(t)||<=epsilon_sp+Eout,
    r(t)->sqrt(ps),
    limsup_(t->infinity)||U(t)-T1(t)/r(t)||
       <=epsilon_complete:=epsilon_sp+Eout+1-sqrt(ps),
    liminf_(t->infinity) inf_(||psi||=1)
          ||P1 U(t)psi||^2 >=max{0,1-epsilon_complete^2}. (19)

The last line is explicitly a LIMINF lower bound; actual success probability need not converge. The normalized comparator exists for sufficiently late times because ps>0.

For fixed parameters, finite/core and complete closed-tail boundary columns are Bochner L1 on compact windows; their Fourier transforms vanish in norm. Uniform geometric domination controls the whole tail, not merely individual sites. Actual incoming coefficients, including wrong-window rows, are L2 on a compact band with positive velocity for this fixed triple; smooth approximation, integration by parts and Fourier contraction give vanishing incoming physical-halfline norm. Remaining outgoing sector errors have bound Eout and combine by orthogonal record-X averaging. Add the one omitted amplitude and then the limiting normalization cost. This proves (19) without discarding record0. Neither velocity nor the local analytic-neighborhood size is bounded below uniformly across the family. No uniform quantitative asymptotic onset or finite-device infinite-time result is inferred.

## Exact fixed-dimensionless scaling with common finite length

Fix any admissible base triple(kappa0,g0,h0) and T0>0 with sigma0=gamma0 T0 and L sigma0>=1. For0<a<=1 define EXACTLY

    kappa(a)=a kappa0, g(a)=a^2 g0,
    h(a)=asin(a^2 sin h0), T(a)=T0/a^2.                  (20)

Then gamma(a)=a^2 gamma0 and d(a)=a^2 d0, so H,L,sigma0 and g(a)T(a)=g0T0 are invariant. The domain survives and the SAME M can satisfy (18). This increases physical waiting as a^-2; it is not a speed improvement. The exact transmitted masses and waveforms need not be invariant or monotone.

The [checked scaling corollary](../outputs/slow_family_2026_10_17/source_checks/slow_lead_fixed_dimensionless_scaling/PROPOSAL.md) supplies the following explicit COMMON certificate. Let pbar be (6), C1=41000/.0053, and

    eta_bar(a)=1.05/pi *[2j*(8e-18)*atan(H)
                +(a^2 kappa0^2 C1+244kappa0^2/g0)log(1+H^2)],
    esp_bar(a)=sqrt(min{1,.68/H+2eta_bar(a)}),
    U2=4kappa0^2 h0/[pi(2j-gamma0)^2]*(h0/sin h0)^2,
    UD2=16kappa0^2 j^2 h0/[pi(2j-gamma0)^2],
    Eout_bar(a)=sqrt(2)[2e-13+400a^2 sqrt(U2)
                                    +(1.01/g0)sqrt(UD2)]
                         +8.4e-25 a^2 kappa0 sqrt(2h0).

For the local certificate define nonnegative fixed coefficients

    Gf=2aG atan(H)/gamma0, Gv=bG log(1+H^2),
    Lf=2aL asinh(H), Lv=2bL gamma0(sqrt(1+H^2)-1),
    Ef=kappa0^2 Gf/(2pi c^2), Ev=kappa0^2 Gv/(2pi c^2),
    Bl=kappa0 Lf/(2pi c)+kappa0^3 L0 Gf/(2pi c^2),
    Bc=kappa0 Lv/(2pi c)+kappa0^3 L0 Gv/(2pi c^2),
    Elocal_bar(a)=2sqrt[(Ef+a^2 Ev)^2+(a Bl+a^3 Bc)^2].   (21)

The inequalities h(a)<=a^2h0, increasing x/sin x, and2j-gamma(a)>=2j-gamma0 give moment bounds a^4 U2 and a^4 UD2. Hence the displayed outgoing envelope, rather than exact mass monotonicity, is justified. Direct substitution IG(a)=a^-2Gf+Gv and IL(a)=Lf+a^2Lv yields (21). The nonzero emitter floor Ef=j aG atan(H)/(pi c^2), the mass calibration floor and the kappa0^2/g0 term survive. They are certificate floors, not proved nonzero actual errors.

Now set

    Cbar=min{1,2.1exp(-.4975sigma0)+.8/[H sqrt(pbar sigma0)]},
    Rbar=sqrt(pbar)*sqrt(1-Cbar^2),
    Iin_bar=2.7/sqrt(L)+sqrt(.68/H),
    Dcut=min{2,1.2exp[-M+4g0T0 sinh1]},
    EM_bar(a)=esp_bar(a)+Elocal_bar(a)+Iin_bar
                                      +2Eout_bar(a)+Dcut. (22)

Every term upper-bounds its corresponding nominal error, and EM_bar(a)<=EM_bar(1). The reference norm in each member's read window is at least Rbar. If the BASE certificate satisfies

    Rbar>EM_bar(1),
    (Rbar-EM_bar(1))^2>=p_*,
    2EM_bar(1)/Rbar<=e_*,                              (23)

then the SAME M certifies every0<a<=1 at each ONE chosen read time in[T0/a^2,2T0/a^2], with success at least p_*, normalized successful-vector error at most e_*, subnormalized successful CP-map error at most2EM_bar(1), and complete-vector error at most min{2,sqrt(2(1-Rbar+EM_bar(1)))}. The normalized comparator is always that member's parameter-dependent packet and literal old aging, not a frozen base waveform.

These common envelopes can be more conservative than the exact functions. A base device accepted by a sharper separate estimate is not automatically accepted by (23). The general corollary does not choose p_*,e_*,T0 or M. Same dimensionless ratios and site count do not establish same actual error or success probability, necessary precision, energy cost or physical units. The endpoint a=0 is excluded: its emitter decouples and the reference/time parametrization cannot be substituted there.

## A checked nonempty family example

The [example argument](../outputs/slow_family_2026_10_17/source_checks/slow_lead_family_example/PROPOSAL.md) and its distinct check select H=10^6, L=10^8, sigma0=40, kappa0=10^-10 and M=20,000,000,000. For the supplied .0027<j<.003 put exactly

    gamma0=10^-20/j, g0=10^-12/j,
    h0=asin(10^-14/(2j^2)), T0=40j/10^-20.

These satisfy (1), with g0<3.704e-10, h0<7e-10 and H/L=.01. Elementary upper bounds log(1+H^2)<28 and asinh(H)<15, inserted into the common envelopes, give

    esp_bar(1)<.000905, Eout_bar(1)<.0000118,
    Iin_bar<.001095, Elocal_bar(1)<.0000041,
    Rbar>.9999993, Dcut<1e-9,
    EM_bar(1)<.002027701<.00204.

The finite-cut exponent is below -8e8 since g0T0=4e9 exactly and sinh1<1.2. Consequently every positive scaling member (20), with this SAME M and one chosen read in[T0/a^2,2T0/a^2], has success>.9959, normalized successful-vector error<.004081, successful subnormalized CP-map diamond error<.00408 and complete finite-vector error<.064. These follow directly from (23) and the complete branch-derived bound, not from infinite asymptotics. The common sufficient envelopes, rather than actual masses, are monotone along a.

The apparatus has20,000,000,241 physical qubits,20,000,000,236 head qubits,20,000,000,237 head edges and40,000,000,277 unmerged positive blocks. Already at a=1 the wait obeys1.08e19<T0<1.2e19 in supplied Hamiltonian units. Relative to the fixed PR9676 certificate T=1e15,M=5e9, this example uses a much longer wait and a larger receiver. It establishes nonempty common-envelope conditions, not optimization, same-tolerance improvement, physical seconds or native precision. No dynamics run or parameter sweep underlies these arithmetic inequalities.

## Restricted receiver coefficient errors

The separately checked [receiver-error interface](../outputs/slow_family_2026_10_17/source_checks/slow_lead_coefficient_robustness/PROPOSAL.md) applies to the finite graph only. Retain the same seed, all original source/emitter/gate blocks and record. Allow real coefficient errors only in the new connector, internal slow exchanges, compensating occupations and cap, with all realized coefficients nonnegative. They conserve head number and act as the full internal identity. Let their magnitude ceilings be e_tau,e_g,e_o,e_c, respectively. Then on the full seeded one-head sector

    ||Delta mathcal H||<=B=e_o+e_c+4e_g+2e_tau,
    ||(U_tilde(t)-U_M(t))V||<=min{2,|t|B}.              (24)

A bond error contributes to a diagonal and an off-diagonal entry of each endpoint row; each site has at most two slow bonds. The symmetric row bound proves (24) without a factor M. It is not a norm estimate on unrestricted many-head states. At M=1 the sharper e_o+e_c+2e_tau applies.

Add min{2,2TB} to epsilon_M on[0,2T]. If the resulting epsilon_pert is<R_T, replace epsilon_M by epsilon_pert in all single-read and complete finite-vector formulas (17). Literal phases are compared; no common-phase adjustment is used. An extra amplitude allowance e_impl is sufficiently ensured by B<=e_impl/(2T). The previously supplied illustrative T=1e15 and allowance1e-4 would require B<=5e-20 under THIS conservative sufficient certificate; this arithmetic does not choose a new family example or prove necessary engineering precision.

If realized occupations and cap enforce every nominal diagonal EXACTLY2j, a different stronger correlation premise removes diagonal errors and gives B_corr=2e_g+e_tau. Positivity of EACH compensating coefficient must still be checked independently; exact diagonals alone do not imply it. This includes inhomogeneous realized hopping but no new couplings.

Along (20), B(a)<=a^2 B0 suffices to keep the extra dynamical allowance2T0 B0 fixed. Fixed relative connector errors generally scale as a, while compensation coefficients approach nonzero values; they do not automatically meet this condition. These are sufficient restrictions of a receiver-only perturbation class, not necessary tolerances or native controllability. Source/emitter errors, seed errors, unwanted interactions, extra heads, readout and all other implementation changes remain outside this lemma.

## Evidence, provenance and boundaries

The [source manifest](../outputs/slow_family_2026_10_17/SOURCES.json) pins all twelve new source/check files and supplies explicit portable mappings to the existing [parent slow packet](../outputs/slow_record_2026_10_17/SOURCES.json) and its inherited attached-record packet. New proof sources are preserved byte-exactly. Historical pending-check headers describe drafting time; the paired final checks qualify their stated scope. The uniform composition check's two scope clarifications are explicit here: finite normalized comparators require R_T>epsilon_M, and the asymptotic probability statement is a liminf, not convergence.

| New argument | Selective check |
|---|---|
| [Uniform actual endpoint, mass and outgoing interface](../outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_endpoint/PROPOSAL.md) | [check](../outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_endpoint_check/REVIEW.md) |
| [Uniform scalar reference](../outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_reference/PROPOSAL.md) | [check](../outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_reference_check/REVIEW.md) |
| [Uniform actual composition](../outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_composition/PROPOSAL.md) | [check](../outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_composition_check/REVIEW.md) |
| [Fixed-dimensionless scaling](../outputs/slow_family_2026_10_17/source_checks/slow_lead_fixed_dimensionless_scaling/PROPOSAL.md) | [check](../outputs/slow_family_2026_10_17/source_checks/slow_lead_fixed_dimensionless_scaling_check/REVIEW.md) |
| [Nonempty family example](../outputs/slow_family_2026_10_17/source_checks/slow_lead_family_example/PROPOSAL.md) | [check](../outputs/slow_family_2026_10_17/source_checks/slow_lead_family_example_check/REVIEW.md) |
| [Restricted receiver errors](../outputs/slow_family_2026_10_17/source_checks/slow_lead_coefficient_robustness/PROPOSAL.md) | [check](../outputs/slow_family_2026_10_17/source_checks/slow_lead_coefficient_robustness_check/REVIEW.md) |

The publication drafter read the complete six arguments and their paired checks. This is authoring and composition of that evidence, not self-review or a fresh independent recalibration. The drafter authored the parent attachment/resource work and checked several parent legs. The component checks are same-model with shared ancestry and disclosed source exposure, not blind or model-diverse certification. Original exact matrix evidence and source inverses remain inherited conditional premises, not rerun evidence.

No scientific runner, numerical sweep, full pipeline, new subagent, audit, W/Git or prompt/model change occurred in preparing this research packet. Repository copying, link/graph verification at the final destination, publication integration review and any later PR are separate actions. No retained status is claimed.

This is a family of static coherent devices with one selected read, not a permanent halt, irreversible latch, reset/reuse or a repeated-read protocol. Infinite asymptotics are not finite-time finite-storage claims. Exact correlated coefficient supply, selective installation, product preparation, record identification and physical units remain premises. The restricted perturbation lemma makes one sufficient implementation budget explicit without removing those premises or establishing a native supplier.
