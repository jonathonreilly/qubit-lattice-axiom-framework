# Uniform slow-output family: local integral, all-time branch and finite single read

Status: authored conditional composition requiring a distinct check. This supplies explicit parameter formulas, not an optimized family or a new numerical target. The full physical construction, exact nominal calibration and supplied initialization remain premises. The finite theorem concerns a selected single read; the sharper complete-state limit is separately qualitative and infinite-device only.

## 1. Domain, comparator and evidence

Keep the original upstream device and supplied .0027<j<.003 fixed. Require

    0<kappa<=10^-8, 0<g<=10^-6, 0<h<=4e-6,
    gamma=kappa^2/j, d=2j sin h,
    H=d/gamma>=100, L=g/gamma>=100, H/L=d/g<=.024. (1)

The emitter diagonal remains2j, its coupling is -kappa, and the new slow ray has hopping g, connector sqrt(jg) and the exact positive compensating occupations preserving diagonal2j. The old gate output o is finite; the first slow site is m=0 at (100,3,2), distinct from o=(100,2,2). The common vacancy scalar c_att is unchanged. There is one shared old/source system and one record; no shared register is duplicated. Original selective installed pairs, exact correlations and source calibration are retained.

Let U(t)=exp(-it H_infinity)V be the seeded one-head evolution on arbitrary old input, including any passive reference. The seed is emitter occupied, other heads blank, source vacuum and record0. P1 retains computational record1 and all other coordinates. Literal K=2I+Z1Z2 and W=[(9+12i)I+(-16+12i)X1X2]/25 enter only the ideal comparator, not a presumed commutation with the interacting Hamiltonian.

Use the EXACT transmitted scalar coefficient F_s(k) from uniform reference, including phase61.5q+.5k+172k_old(q), physical first-site origin and flux/Jacobian. Let beta_t be its unnormalized outgoing Fourier packet restricted to m>=0, p_s=integral|F_s|^2 and r(t)=||beta_t||. Define

    T1(t)=exp(-it c_att) Jout[beta_t tensor exp(-itK)W],
    A1(t)=P1 U(t).                               (2)

Jout places source vacuum, record1 and the slow head packet in the physical Hilbert space. The target is subnormalized; its operator norm is r(t)<=sqrt(p_s)<=1.

Complete arguments read/reused: uniform endpoint c8d2b7681f2059ec986bc3e41bf0a3eea8fefbc43c86addc17539b2f258bb887/root check f3e449109bc4bac6b4e4692d0db5f40c4d282d663b32f3b89a7ff1065ded28e0; uniform reference5f2026dc3f63a757f13cf58bc468f05de10cfca9f04fda9c6615b816c9b94907/distinct check338e554834f994741982842c555589db5e62dba9ad121233989ce60068f26c93; fixed recovery f0f39510b65133d8399720c53ce2822bfe60a378ab2e50e1773a3dc8d0fe880f/root check488d0a9e8871f77f40d44803ee9bfe7fda25388c66b367944eea3376f51f5195; fixed synthesis ab552c4002af8388d5e223cf81390cdcbaa74685affda5c263048cbea73cdb2a/distinct checkc6d82eaf1e4789f6b4f6b6f5c0fe97a0201fce1dbe7e99b294995d76e516a628. The latter four sources/checks were completely refreshed for this task. Uniform sources and endpoint check were completely read in the immediately preceding coherent tasks and remain unchanged.

The exact general-g cap/weight source is slow_lead_resources/PROPOSAL.md84b76d1ec9b1e45811b74ecd2594a0622dfb01ef69d1acadf98931c0ed3f9967 with checkdd944d8803da24fdfbccfd010e2fd865196aa08ac244605303093a605fef22fe. The general operator interface69aa54015825bd6e240b1da5f856cb062157e2686d5403698592315fa4d529ac and original canonical source71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff retain their qualified ancestry. I authored uniform endpoint/reference and recovery, not the fixed synthesis. This is exposed author composition, not independent recertification. No solver, sweep, scientific execution, further agents, W/Git, publication, checkpoint, prompt or model change occurred.

## 2. Uniform actual local recovery, rather than fixed numerical inheritance

All unloaded background maps precede the emitter and final return, hence are independent of kappa,g. On the smaller selected interval retain ||P B_e||<400, ||B_e||<521, ||S P||<3, |S_PP|=1, ||S_CP||<2, ||S||<2e8, ||K_U P||<1000 and ||K_U||<2e18. The uniform endpoint proof supplies actual individual return <.0062, sector difference <=68u and closed return <e=10^-63. It does NOT supply an individual1540u bound uniformly in g; that bound is unnecessary here.

Closed elimination therefore gives the same actual full-forcing bounds ||P b_x||<403, ||C b_x||<1100 and ||C a_x||<1100e. The selected sector-difference equation has

    A=||P Delta a|| <=.0062 A+.0062*(2e8)*2200e+403*68u,
    A<=27600u+3e-54.

Applying selected physical recovery and the tiny closed remainder gives Delta L_U<2.76e7u+5e-42. For the eighteen cable sites, Delta b=S Delta a costs at most3A plus the closed floor; the open incoming term costs A. The growing closed root is paid BEFORE taking a norm, by |s|^(36-n)|r_gate|<3*60^(-(36-n)), n<=17. Summing the cable gives <20A+1e-28. Thus

    ||Delta L_up||<=1e-24+2.9e7u.

Absolute recovery still pays the nonnegligible closed outgoing coefficient at n=0: finite arms/buffers <240001, input sites <4670, attached upstream correction <2499 and cable <7530 sum to <3e5. At n=17 the closed coefficient has60^-17, so the gate-boundary response is <406.

The uniform gate proof retains forced recovery <5.064 including all closed slow tails. Its relaxed closed-tail multiplier .00068 still gives each closed block <1/55; it does not amplify the selected gate block. Therefore gate-plus-closed-tail recovery is <2060 per record sector and difference <4120. Combining these actual uniform inequalities gives

    ||L_x||<L0=4e5,
    ||Delta L||<=a_L+b_L|delta|,
    a_L=4121, b_L=5.5e9.                         (3)

Here |delta|>=.0053u. L recovers every finite background coordinate, including o, and the complete closed slow tails. The propagating stationary ray alone is excluded. Each physical window has its own fixed closed-channel projection; window errors are added. Every input direction in the eight-dimensional forcing fiber remains present. The uniformity of (3) follows from the displayed uniform margins, not from retaining the old fixed integral .000410.

## 3. Explicit parameter-dependent core integral

The uniform endpoint proof gives, on both lips and both sectors,

    ||T_x||<=1.03/sqrt(delta^2+gamma^2),
    ||Delta G||<=a_G+b_G|delta|,
    a_G=10^-45, b_G=1.27e7.                       (4)

The full inverse1.03 is required; the selected scalar .98 denominator is not substituted. Reality in fixed conjugations transfers column norms to the lower lip, without identifying a rectangular column with its adjoint. The exact ordered difference is

    Delta F=[kappa^2 T_+ DeltaG T_-;
       -kappa DeltaL T_- -kappa^3 L_+ T_+ DeltaG T_-]. (5)

Define the EXACT envelope integrals

    IG=2a_G atan(H)/gamma+b_G log(1+H^2),
    IL=2a_L asinh(H)+2b_L gamma(sqrt(1+H^2)-1),
    Ecore=(1.03)^2 kappa^2 IG/(2pi),
    Bcore=1.03 kappa IL/(2pi)
                      +(1.03)^2 kappa^3 L0 IG/(2pi),
    epsilon_local=2 sqrt(Ecore^2+Bcore^2).        (6)

These functions are finite for every positive triple in (1). The direct kappa DeltaL term is retained. The record1 half-difference and the two Stone lips yield1/(2pi) per-window integral. Emitter and background coordinate ranges justify the square sum. The leading factor2 adds the two physical old-energy windows; parity blocks combine by maximum. No fixed bound on H, logarithm or kappa is inserted into (6). This represented local/closed error holds for all times, and contains no omitted spectral charge.

For example its parameter dependence is explicitly kappa asinh H in the direct constant recovery term, while the emitter floor contributes a nonvanishing O(j a_G). Smaller kappa does not automatically erase all certificate floors. Formula (6), rather than that observation, is the quantitative bound used below.

## 4. Mass, outgoing and incoming parameter functions

Use the uniform endpoint's exact reference mass p0(kappa,h), exact transmitted p_s=p0-R and explicit moments M2,MD2 (or their upper bounds). Put

    b(g)=41000/.0053+244/g, a=8e-18,
    eta=1.05 kappa^2/pi *
       [2a atan(H)/gamma+b(g) log(1+H^2)],
    epsilon_sp=sqrt(min{1,1-p0+2eta}),
    Esel=2e-13 sqrt(p_s)+400 sqrt(M2)+(1.01/g)sqrt(MD2),
    Eout=sqrt(2) Esel+8.4e-25 kappa sqrt(2h),
    Iin=min{sqrt(p_s),2.7/sqrt(L)+sqrt(1-p0)}.     (7)

The full matrix seed theorem supplies epsilon_sp on the COMMON union I_1 union I_3, including all outside spectral types. It is charged once. It includes off-diagonal and wrong-window old inputs, not just scalar diagonal masses. The complete outgoing coefficient bound Eout includes the complementary prepared-input Schur rows, which retain their actual output-window energies. The incoming parameter Iin is the RAW reference bound; using normalized scalar estimates without restoring sqrt(p_s) would obscure this distinction.

The physical Stone formula is the lower-minus-upper column divided by2pi i. With F=iE'_k A/sqrt(2pi), the open spectral evolution has two PLUS terms exp(ikm)F+exp(-ikm)conjugate(F), integrated against the actual physical energy phase. Conjugation acts on matrix entries, leaving a linear map on arbitrary complex inputs. Record1 takes the half-difference of record-X coefficients. The ideal incoming logical factor is W* in the common real basis, whereas the outgoing target is W. Its norm is paid by Iin. Incoming and outgoing coefficient errors occupy the same ray and add, costing2Eout.

Local finite and closed-tail synthesis follows from actual seed AC, finite inverse recovery and norm-continuous geometric tails for each fixed positive triple. Open-ray synthesis extends by Fourier isometry. Consequently the complete actual subnormalized record1 map obeys

    ||A1(t)-T1(t)||<=epsilon_infinity,
    epsilon_infinity=epsilon_sp+epsilon_local+Iin+2Eout,
    every t>=0.                                  (8)

This bound can be uninformative for some triples; no desired performance is assumed. All actual wrong-window terms are charged before factoring the ideal exp(-itK)W. Passive-reference tensoring preserves the operator bound. The successful CP map differs from its subnormalized comparator by diamond norm at most2epsilon_infinity, since both underlying maps are contractions. Conditioning is nonlinear; no normalized-channel diamond claim follows.

## 5. Quantitative finite single-read sufficient condition

For sigma>0 with L sigma>=1 define the normalized outgoing-left ceiling

    C_out(sigma)=min{1,2.1 exp(-.4975 sigma)
                                +.8/[H sqrt(p_s sigma)]}.

Choose any T>0 with L gamma T>=1. For all t>=T, orthogonality of the physical ray and its complement, and monotonicity of the displayed ceiling, give

    r(t)>=R_T:=sqrt(p_s)*sqrt(1-C_out(gamma T)^2). (9)

No numerical onset is selected. Retain M>=1 NEW slow sites m=0,...,M-1 and the exact cap g n_last. With all occupations intact H_M is precisely the compression of the infinite one-head operator. For M=1 the first-site occupation and cap are separate terms at that site; there is no internal slow edge. The finite state is embedded into the infinite space for comparison with (2).

Weight zero through firstslow and weight m thereafter. Only internal g bonds have nonzero increments; the connector has zero increment. The exact one-cut Duhamel bound yields on0<=t<=2T

    ||U(t)-embed U_M(t)||<=D_M(T),
    D_M(T)=min{2,1.2 exp[-M+4gT sinh1]}.

The reverse cut orientation does not add a second factor. All internal coordinates, onsite blocks and both record sectors remain in this comparison. Set

    epsilon_M=epsilon_infinity+D_M(T).            (10)

Then ||embed A1,M(t)-T1(t)||<=epsilon_M throughout[0,2T]. For any ONE chosen read time t in[T,2T], if R_T>epsilon_M, every normalized old/reference input satisfies

    probability(record1)>= (R_T-epsilon_M)^2,
    normalized successful vector error <=2epsilon_M/R_T,
    successful subnormalized CP-map diamond error <=2epsilon_M. (11)

These are sufficient conditions with the same ideal comparator beta_t/r(t). A requested probability lower bound p_* and successful-vector tolerance e_* would be ensured by (R_T-epsilon_M)^2>=p_* and2epsilon_M/R_T<=e_*, together with R_T>epsilon_M. No such targets are chosen here.

For a separately allocated transfer budget epsilon_tr>0, the explicit integer condition

    M>=max{1,ceil(4gT sinh1+log(1.2/epsilon_tr))}  (12)

ensures D_M(T)<=epsilon_tr. The apparatus has M+236 head qubits, M+241 total physical qubits, M+237 head edges and2M+277 blocks in the unmerged positive decomposition. Shared qubits and passive references are counted as in the exact resource source. The infinite comparator is not truncated and renormalized silently.

A weaker quantitative COMPLETE finite vector bound follows from the same branch estimate, without borrowing any asymptotic rate. Since y=T1(t)psi/r(t) lies in record1 and is normalized, Re<y,U_M(t)psi>>=r(t)-epsilon_M. Therefore

    ||embed U_M(t)-T1(t)/r(t)||
       <=min{2,sqrt(2(1-R_T+epsilon_M))}, t in[T,2T]. (13)

It is distinct from the sharper qualitative limit below. The finite theorem concerns a single chosen read within its absolute horizon, not repeated reads or a stopping-time protocol.

## 6. Separate complete infinite asymptotics

For each FIXED positive parameter triple in (1),

    limsup_(t->infinity)||U(t)-T1(t)||<=epsilon_sp+Eout,
    r(t)->sqrt(p_s).                              (14)

To justify the first statement, retain both record sectors. Actual finite-coordinate boundary columns are bounded and continuous on compact windows for this fixed triple. Entire closed tails have a norm-continuous Hilbert-space envelope by geometric domination. Their spectral densities are Bochner L1, whose Fourier transforms tend to zero in norm by L1 approximation with vector-valued interval step functions. Finite input dimension upgrades column convergence to operator-norm convergence.

Actual incoming coefficients, including wrong-window rows, are L2 on a compact slow band with strictly positive velocity for this triple. Smooth interior approximation, integration by parts for phase -km-tE_s(k), and square summation over m>=0 give decay of their positive-halfline norm; Fourier contraction controls the approximation error. This qualitative argument requires neither a uniform lower velocity across triples nor a complex continuation of the interacting source. It supplies no quantitative rate uniform in kappa,g.

The remaining outgoing sector errors are bounded by Eout; orthogonal record-X ranges average their squared norms and the ideal opposite signs reconstruct record1. The one omitted seed amplitude adds epsilon_sp. This proves (14) without discarding record0. The scalar curve proves r(t)->sqrt(p_s). For sufficiently late times the normalized target exists, with

    limsup ||U(t)-T1(t)/r(t)||
       <=epsilon_complete:=epsilon_sp+Eout+1-sqrt(p_s).

Thus limiting record1 probability is bounded below by max{0,1-epsilon_complete^2}, uniformly over inputs. This is an INFINITE-device complete-state statement with no supplied numerical onset. It is not inserted into the finite read window in (11). Omitted point or singular spectrum may persist within the charged amplitude.

## Limits and check targets

The three scopes are explicit: (8) is all-time absolute infinite record1 accuracy; (11)–(13) are finite single-read sufficient conditions; (14) is qualitative complete infinite asymptotics. No permanent halt, irreversible latch, autonomous reset/reuse, native Record semantics, supplied-state preparation or coefficient tolerance theorem is claimed. Elapsed time and exact physical correlations remain obligations of any practical interpretation.

Distinct checking should reconstruct the uniform recovery margins rather than assume the fixed .000410, retain full inverse1.03/r and the direct DeltaL term, verify both-lip factors and full-input aggregation, charge omitted amplitude once, and distinguish finite branch success from the separate complete asymptotic error. This authored composition has not itself been independently checked.
