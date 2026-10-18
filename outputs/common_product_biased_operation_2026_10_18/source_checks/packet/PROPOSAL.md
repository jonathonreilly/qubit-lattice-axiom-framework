# Complete inelastic packet and explicit derivative interface

New bounded author derivation requiring distinct review. For the actual one-control, shared-record network with one positive kappa n_R bias, this note constructs an exact normalized physical packet from record-0 I incidence. It bounds the first and second k derivatives of the full scattering matrix and every finite head-coordinate map, retaining the biased channel measure and the feedback inverse margin. Normalization follows from remote-past incoming separation, not an assumption of spectral completeness.

The network dependency was provisional at assignment. Its distinct stationary check1bd4a2 arrived during drafting and was fully read; it is now adopted only at that stationary scope. This packet derivation itself remains provisional. No finite emitter/cut, runtime, thermal supply or faithful all-time flag theorem is claimed.

## 1. Physical object, domain and conventions

Use precisely networkcdf35: the literal positive one-control76b5 core, two identical24-head writers sharing ONE R, two34-edge cables, the four external infinite rays and the one onsite block kappa n_R. The common vacancy scalar is c=8b+8(sqrt(2)-1)j. On the bounded one-head space H=cI+K_0+kappa I_head tensor n_R. Each coordinate region sees the same threshold by restriction of this ONE record operator. There is no per-region physical duplication. The complete program/path/reference fiber is retained; X_R is not conserved. An optional separately installed uniform mu N would add the common one-head phase exp(-i mu t), but is not required here.

Take positive j=b^2/D0, eta=b/D0<=1/8, zeta=D0/D1<1/2, and

    |k-pi/2|<=h<=10^-3, 0<=r=kappa/j<=10^-3,
    E(k)=2j(1-cos k), q(k)=acos(cos k+r/2),
    k_0=k, k_1=q, J=diag(sin k,sin q),
    Z=diag(exp(ik),exp(iq)), P_c=Z^34,
    e=13eta^2+5zeta, w=33h+480r, den=1-ew>0.              (1)

Identities on the required path/program factors are implicit in J,Z,P_c. All stationary scattering coefficients use flux amplitudes sqrt(sin k_a) times ordinary spatial amplitudes; the common physical sqrt(2j) cancels. The energy is c+E(k) in both record channels, since E(k)=2j(1-cos q)+kappa. The coefficient matrices below act on the entire incoming(I,F)/path/program/record fiber, with arbitrary passive references tensored unchanged.

The network scattering matrix S is unitary in these flux coordinates and has error Delta=min{2,[2(e+w)+ew]/den} against the ordered comparator in network(12). In particular for the injection V_0 of a program/path vector into I,record0,

    ||S V_0 - V_F1 [-i exp(57ik)] C||<=Delta,             (2)

where C is the coherent controlled path operation and V_F1 injects into F,record1. This common phase belongs to this incident column; it is not the entire all-record comparator.

## 2. Channel derivatives with explicit uniform constants

Both sines exceed .99, |cos k|<=.001 and |cos q|<=.0015. Differentiating sin(q)q'=sin(k) yields

    .99<=q'<=100/99,
    q''=[cos k-cos q(q')^2]/sin q,
    q'''=[-sin k+sin q(q')^3-3cos q q'q'']/sin q.          (3)

Consequently

    |q''| <= [.001+.0015(100/99)^2]/.99 <.003,
    |q'''| <= [1+(100/99)^3+3(.0015)(100/99)(.003)]/.99 <3.

These estimates follow from the displayed trigonometric bounds and include r=0, where q=k exactly. No strict k-q<r assertion is made at r=0. We use deliberately looser derivative bounds2 and6 for q',q'' in the coefficient bookkeeping below; the sharper .003 and3 remain available in phase estimates.

For D=J^(1/2) and R_J=J^(-1/2), safe triples of operator-norm bounds for orders0,1,2 are

    D : (1,2,8),       R_J : (2,4,40),
    Z : (1,2,10),      P_c : (1,68,4828).                (4)

For example J' has norm<=2, J''<=10, and the scalar square-root/inverse-square-root differentiation formulas with J>=.99I give(4). A power Z^l,0<=l<=34, has derivative bounds2l and4l^2+6l; hence the same P_c triple bounds every cable propagation factor. No differentiation of r is performed: the physical device fixes kappa and j while k varies.

## 3. Explicit derivative algebra and local component bounds

To present fully evaluable constants without hiding product terms, define for nonnegative triples x,y

    x star y=(x0 y0, x1 y0+x0 y1,
                         x2 y0+2x1 y1+x0 y2).           (5)

Addition and scalar multiplication are componentwise. If operator maps have derivative ceilings x,y, their ordered product has ceiling x star y by Leibniz, independent of commutation. Sums and row/column concatenations are bounded by the sum of triples; this is conservative. All formulas below are finite arithmetic expressions in eta,zeta,e,w,den and fixed numbers. In particular these are explicit constants, not unknown norms to be estimated later.

For the biased writer let B=11. Its checked outgoing inverse G satisfies ||G||<=10/(1-20r)<B. Its matrix L=H_int+r n_R-(E/j)I-E_P Z E_P* has ||L'||<=4 and ||L''||<=12 by(4). Inverse differentiation gives

    G_1=4B^2, G_2=32B^3+12B^2.                          (6)

The full-record flux scattering and physical internal maps are

    S_w=-I-2i D E_P*G E_P D,
    V_w=-2i G E_P D.

Their uniform triples are respectively

    W=(1,w1,w2),
    w1=8B+8B^2,
    w2=48B+88B^2+64B^3,
    A_w=(2B, 4B+8B^2, 16B+56B^2+64B^3).                (7)

For clarity, the second scattering derivative bound is2[2(8)B+2(2)^2B+4(2)G_1+G_2]. The second internal derivative bound is2[G_2+2(2)G_1+8B]. These calculations use the full48-dimensional matrix and no record-X decomposition. Two writers give a direct sum over head path of the same maps, on ONE record fiber, so(7) has no multiplicative path/record count.

Here is a self-contained core derivative bound on its larger momentum band s in[pi/3,2pi/3], which includes BOTH k and q. Put lambda=1-3eta^2 and

    alpha1=2eta^2/lambda^2,
    alpha2=2eta^2/lambda^2+8eta^4/lambda^3,
    beta1=2eta^2 zeta^2/(1-3eta^2 zeta)^2,
    beta2=2eta^2 zeta^2/(1-3eta^2 zeta)^2
                          +8eta^4 zeta^3/(1-3eta^2 zeta)^3,
    l1=1+2(alpha1+beta1), l2=1+2(alpha2+beta2),
    c1_raw=4+8l1,
    c2_raw=4+16l1+32l1^2+8l2.                            (8)

Indeed the exact core boundary matrix is V=2I-alpha(I+R_p)-beta(I+S_p), alpha=D0/(D0-E_0(s)), beta=D0/(D1-E_0(s)). Its outgoing L_c=exp(-is)I-I+V has inverse norm<=1/sin s<=2, because V is real self-adjoint. Its scattering matrix is -I+(exp(-is)-exp(is))L_c^-1. Differentiating this expression, using |E_0'|,|E_0''|<=2j and D0-E_0(s)>=D0 lambda, gives(8). Thus the record-diagonal composed core S_c(k) has triple

    C_s=(1,c1,c2), c1=2c1_raw, c2=4c2_raw+6c1_raw,        (9)

by the chain rule and the loose bounds |q'|<=2,|q''|<=6. These are sufficient estimates; no small-error derivative cancellation is assumed.

Let d0=D0-3j>0 and define

    F_m=(b/d0, 2jb/d0^2, 2jb/d0^2+8j^2b/d0^3).

This bounds b(D_e-E_0(k_a))^-1 on the mediator channels: E_0(k_a)=E(k)-a kappa, so its first/second k derivatives are just E'(k),E''(k), without an extra q-chain penalty. The unoriented four-edge endpoint incidence matrix has norm2. Consequently the intrinsic physical core endpoint and mediator maps for core flux input have triples

    A_end=R_J star (2,c1,c2),
    A_med=2 F_m star A_end.                              (10)

In(10) R_J denotes its numerical triple from(4). The underlying maps are J^-1/2(I+S_c) and b(D-E_a)^-1 N^T J^-1/2(I+S_c). This explicitly includes the flux-to-ordinary amplitude conversion at every endpoint and mediator.

## 4. Entire feedback and external derivatives

Use the exact blocks S_c=[[A,B_c],[C_c,D_c]], S_w=[[a,b_w],[c_w,d_w]] and K=(I-a P_c D_c P_c)^-1 from the network. Let numerical triples

    C_ref=(e,c1,c2), W_ref=(w,w1,w2),
    P=(1,68,4828), I_jet=(1,0,0),
    F=W_ref star P star C_ref star P,
    K_jet=(den^-1, den^-2 F1,
                              2den^-3 F1^2+den^-2 F2).  (11)

F0=ew. Thus(11) follows from the proved feedback inverse margin and its differentiated inverse identities; it does not infer a pole margin from external unitarity.

The exact maps from a full external incident column f to outgoing cable coefficients are

    U=K[a P_c C_c,b_w],
    V=[C_c,0]+D_c P_c U.

Their explicit derivative ceilings are

    U_jet=K_jet star (W_ref star P star C_s + W),
    V_jet=C_s+C_ref star P star U_jet.                   (12)

The actual external outputs are [A,0]+B_c P_c U and c_w P_c V+[0,d_w]. Define

    S_bound=C_ref+C_s star P star U_jet
                         +W_ref+W star P star V_jet,
    s1=(S_bound)1, s2=(S_bound)2, S_jet=(1,s1,s2).        (13)

Equations(11)--(13) bound ||S'|| and ||S''|| for the FULL all-incidence matrix, including every reflection, both record thresholds and all input program coherences. Its order0 norm is replaced by the exact1 from flux unitarity. Products in the actual maps retain their displayed order; star merely bounds their norms. These constants remain finite for every admissible positive den, and explicitly diverge if that sufficient margin is lost.

## 5. Every finite coordinate through second order

There are122 finite head vertices: eight core,48 writer and66 cable-interior heads. Four are external ray origins (two core I and two writer F); the strict internal subspace therefore has118 heads. Program/record are fibers, not additional head positions. There are68 cable EDGES, but only66 new interior HEADS.

The core incoming flux map is [I, P_c U] and the two-writer incoming flux map is [P_c V,I]. Their triples are

    N_c=I_jet+P star U_jet,
    N_w=I_jet+P star V_jet.

At cable coordinate l=1,...,33, the physical path/record amplitude is

    J^-1/2 [Z^l V+Z^(34-l) U] f.

This expression uses the outgoing wave from each endpoint at its own reference plane; the second term has34-l, not a duplicated cable phase. A conservative bound for ALL cable-interior sites is sqrt(66) R_J star P star(V_jet+U_jet). Hence set

    T_jet=(A_end+A_med) star N_c + A_w star N_w
                      +sqrt(66) R_J star P star(V_jet+U_jet).
    t_a=(T_jet)a, a=0,1,2.                              (14)

Then ||T_all^(a)||<=t_a, where T_all is the actual physical-amplitude map for all122 finite head coordinates from external flux input. Restriction to the strict internal118 heads defines T_int with the same ceilings. No arm, terminal, junction, mediator, cable site or record sector is omitted. The sum over groups is a safe bound on their orthogonal direct-sum norm. The larger sqrt(66) bound also safely bounds the two path-vectors at33 cable depths. All origin values in T_all agree with the corresponding lead boundary equations; they will be counted only once in the packet.

## 6. R0 incidence measure and exact complete packet

Fix a scalar g in C_c^2((pi/2-h,pi/2+h)) with ||g||_2=1; no prescribed launch profile or derivative scaling is assumed. Let G_a=||g^(a)||_1. Fix ell>=0 and arbitrary program/path/reference input xi. V_0 embeds it into I,record0 and is constant in k. Write

    d_in(k)=sqrt(sin k),
    O(k)=J^-1/2 S(k) d_in(k) V_0,
    T_0in(k)=T_int(k) d_in(k) V_0.                       (15)

The numerical triple D_in=(1,2,8) bounds d_in. Uniform triples for these maps are

    O_jet=R_J star S_jet star D_in,
    T_in,jet=T_jet star D_in.                            (16)

For a later calculation that extracts the phase57, define Q=e^(-57ik)S, with triple Q_jet=(1,s1+57,s2+114s1+57^2). The ordinary outgoing demodulated map e^(-57ik)O then has explicit triple O_demod,jet=R_J star Q_jet star D_in. Its phase is n k_a(k)+(ell+57)k-tE. This extraction removes only exp(57ik), so the ideal coefficient is still -i times the controlled record-flip column; that fixed -i is not discarded. These constants are independent of ell. Either raw or demodulated maps may be used with their own consistent phase in the bounds below.

Let O_a denote record-a projection of O. For each external ray radius n>=0, define the complete external vector

    Psi_ext,n(t)=1/sqrt(2pi) integral exp(iell k-itE(k))g(k)
             [exp(-ikn)V_0+sum_(a=0,1) exp(ik_a n) O_a(k)]xi dk.

The strict internal vector is

    Psi_int(t)=1/sqrt(2pi) integral
                    exp(iell k-itE(k))g(k) T_0in(k)xi dk. (17)

The physical solution is exp(-ict)Psi(t). Record-a projectors and all port/path labels in(17) act on the actual common record fiber. At external origins the incoming and outgoing pieces add; those four heads are excluded from Psi_int. Every internal head amplitude, including small erroneous record components, is retained. Neither an internal projection nor a normalization of a success branch is performed.

For a record-a outgoing full-integer lead, let p=k_a(k). Since p'=sin k/sin k_a and O_a=sqrt(p') P_a S V_0, changing variables gives its Fourier coefficient

    [P_a S(k(p))V_0 xi] g(k(p))
                      exp(iell k(p)-itE(k(p)))/sqrt(p').

Parseval therefore gives the EXACT full-line outgoing norm identity

    sum_a ||Psi_out,a,full||^2
             = integral |g(k)|^2 ||S(k)V_0 xi||^2 dk
             =||xi||^2.                                (18)

There is no missing or inverse velocity factor. The incoming full-integer vector likewise has norm||xi||. Their sum is not asserted to have norm2 or1 at finite time; it has interference on the physical half-lines and shares dynamics with the internal coordinates. Each piece is square summable by(18), and each finite internal integral is bounded by(16). The same arguments with E(k)g(k) show strong time differentiability. The actual bounded one-head generator can be interchanged with the synthesis; every stationary component obeys its exact coordinate equations. Thus i dPsi/dt=(H-cI)Psi strongly.

For t tending to minus infinity the incoming half-line vector approaches its full-line norm, while all outgoing half-line and strict internal vectors tend to zero by the estimates in section7. Consequently ||Psi(t)|| tends to||xi||. Exact self-adjoint evolution conserves the norm, proving

    ||Psi(t)||=||xi|| for every real t.                  (19)

Linearity and polarization give an isometric complete packet map, including arbitrary passive references. This is a constructed scattering family only. It makes no completeness claim and does not declare the point-spectrum part of an arbitrary finite seed absent.

## 7. Explicit nonstationary interfaces and remote-past justification

The following bounds apply to vector/operator-valued amplitudes, so no reference-dimension factors appear. If ||a||_1<=A0,||a'||_1<=A1, the phase derivative at integer n>=0 obeys |Phi_n'|>=Q+a_* n, and |Phi_n''|<=b_* n+2j|t|, then one integration by parts and the integral bound for the decreasing square sequence give

    Tail(A0,A1;t,Q,a_*,b_*)
       =[A1+(b_*/a_*)A0+(2j|t|/Q)A0]/sqrt(2pi)
                                  *sqrt(Q^-2+1/(a_* Q)), (20)

provided Q>0,a_*>0. This bounds the l2 norm over those n. Indeed n/(Q+a_*n)<=1/a_*, and sum_(n>=0)(Q+a_*n)^-2<=Q^-2+1/(a_*Q). Compact support removes the endpoint terms.

For any coefficient triple M define

    A0(M)=M0 G0,
    A1(M)=M0 G1+M1 G0,
    A2(M)=M0 G2+2M1 G1+M2 G0.                           (21)

Use M=O_jet for either outgoing record channel, and M=T_in,jet for all strict internal coordinates. Write J0=A0(T_in,jet), J1=A1(T_in,jet). For internal phase ell k-tE, whenever its derivative magnitude is at least Q>0,

    Internal(t,Q)=[J1/Q+2j|t|J0/Q^2]/sqrt(2pi).          (22)

The same formula with T_all's converted triple bounds all122 finite vertices if needed. With v_min=2j cos h, v_max=2j, t<0 and Q=ell+|t|v_min, the outgoing phases ell k+n k_a(k)+|t|E have derivative at least Q+.99n and second derivative at most .003n+2j|t|. Hence the outgoing half-line norm is bounded by sqrt(2) times(20) with M=O_jet,a_*=.99,b_*=.003. The sqrt(2) combines the two orthogonal record-channel bounds; path/program/reference dimensions contribute no factor. The missing incoming negative-radius tail is bounded by(20) with A0=G0,A1=G1,a_*=1,b_*=0 and gap Q (using Q+1 would be slightly sharper). Equation(22) bounds the internal part. All three quantities tend to zero as t tends to minus infinity, establishing the normalization argument in(19).

For future boundary applications, a second integration by parts gives an explicit pointwise interface: if on the support |Phi'|>=d>0, |Phi''|<=M2 and |Phi'''|<=M3, then

    ||(2pi)^-1/2 integral exp(iPhi)a||
       <=[A2/d^2+3M2 A1/d^3+M3 A0/d^3
                                  +3M2^2 A0/d^4]/sqrt(2pi). (23)

This is obtained by differentiating the amplitude twice through1/Phi'; it uses no fitted phase or generic locality estimate. For outgoing phases ell k+n k_a(k)-tE(k), valid choices are M2=.003|n|+2j|t| and M3=3|n|+2j|t|. For incoming and strict internal phases take M2=M3=2j|t|. The actual positive gap d must be proved in each application; (23) does not assert that it exists at arbitrary times/sites. The ideal outgoing target below has ell+57 in place of ell and uses q. All coefficient choices for A0,A1,A2 are explicit in(16),(21). This is an interface for later cut integration, not that integration itself.

## 8. Common late outgoing target on infinite rays

Define the ideal inelastic scalar sequence on the full integer line by

    B_n(t)=(-i)/sqrt(2pi) integral exp[i n q(k)+i(ell+57)k-itE(k)]
                                      sqrt(q'(k))g(k) dk. (24)

Its full-line norm is1 by the same variable change; ell and57 multiply the incoming coordinate k, not q. The physical common factor exp(-ict) is fixed. The record energy cost is already in E(k)=E_0(q)+kappa, so no additional record phase may be multiplied in without changing the kinetic-time convention consistently.

For t with Q=tv_min-ell>0, the incoming physical half-line tail is bounded by Tail(G0,G1;t,Q,1,0), and the strict internal part by(22). The complete outgoing discrepancy from J_F[B_(n>=0)(t) tensor C xi tensor|1>_R] is at most Delta: by the record-wise Fourier variable change its full-line squared norm is integral |g|^2||(S V_0-S_*V_0)xi||^2, and half-line restriction cannot increase it. Therefore

    ||Psi(t)-J_F[B_(n>=0)(t) tensor C xi tensor|1>_R]||
       <=D_late(t)||xi||,
    D_late=Tail(G0,G1;t,Q,1,0)+Internal(t,Q)+Delta.       (25)

J_F sets every other head vacant and retains the physical program and passive references. If D_late<1, normalization(19) implies ||B_(n>=0)||>=1-D_late>0. Define its positive normalization beta_F=B_(n>=0)/||B_(n>=0)||. Then the complete normalized output error is at most min{2,2D_late}; restore exp(-ict) on both vectors. Wrong I outgoing fields, wrong record, every internal field and all coherences are paid by(25). This is an infinite-ray packet statement, not a finite device, fixed observation-window claim or an assertion that record1 faithfully certifies completion at every time.

## 9. Exact dependencies, exposure and remaining obligations

N is /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. Exact primary pins:

- common_product_biased_record_network/PROPOSAL.md: cdf35dd3f9a8ea32ce0b52745ac00756885dba014d67db7e12f706e58e63b666, authored and completely read in the immediately preceding task; hash refreshed here. Its newly supplied common_product_biased_record_network_check/REVIEW.md was completely read: 1bd4a2878923495df99a219cce1c520cc03674bce2da5ff1d61d64d0940f8d40. It supports stationarity only, not this packet extension.
- common_product_biased_writer_scattering/PROPOSAL.md: dfe071282ac3d160073b85caa0bd11d4e1834e58278e1da8a3c354fec5440c18, complete read in that task. Its check was fully read/hash-verified here: c568fe01ce4c6e9e89e6488808bb39c9ba7a98e1df4b0fc5bcc8d21439315829. The r=0 strict-inequality endpoint is corrected explicitly in the network and in section2 here; the check's valid non-strict norm estimates are used.
- common_product_stage_record_packet/PROPOSAL.md: 3477197cdf54d18ab538c517726d64f3dbc556f6ddb7a6d4b2608b458d34eeb9, fully reread/hash-refreshed here. Its exact core matrix and derivative method informed(8); its elastic packet constants, sector assumptions and normalized packet theorem are NOT imported. Its previously read check17029fa32989bae3869c4ffee81def65201edc0f0b996013ede8996ca8cf1453 does not check the present inelastic formulas.

The exact actual core60bc, record geometryc913/check61de, single-control76b5/check549b, writer934/checkc5f3 and inverse22bca/checkd96ed premises retain their full pins and scoped complete reads recorded in networkcdf35 and local checkc568. This note changes none of their physical blocks or geometry. The checked B<11 local inverse is reused; no certificate program was rerun. ROOT's separate phase-envelope proposal54e054 was reported during drafting but was not read or used as evidence. ROOT also suggested sharp q derivatives; equations(3) explicitly reconstruct them before use.

This author wrote the network, one-control and several earlier packet/finite sources. ROOT requested this continuation and provided exposed design suggestions; this is same-model author work, not independent or blind checking. The new derivative bookkeeping, complete inelastic measure/normalization and tail implications require a distinct check, especially the flux conversions in(10),(14)--(18), origin partition, all product/inverse derivatives, and remote-past proof. Pending that check, the present packet claim is provisional despite checked stationary dependencies.

Still open are an actual finite endpoint seed's full-vector early match, all localized-component payment, source/record-threshold preparation details, actual finite I/F cut operators and their integrated error, simultaneous window/length/parameter budgets, finite output normalization and all apparatus vacancies. No old finite theorem is imported by analogy. This note supplies no bath/cooling/loading/readout mechanism, thermal improvement, native interaction coefficients, old literal processor theorem, robustness claim, physical capture/reset or permanent halt. No normalized rare-flag conclusion is made.

Only this proposal was created. Verification was author algebra and source/file/hash bookkeeping. No scientific executable, numerical sweep/simulation, source/W/Git/checkpoint/axiom/editable-prompt/model change, publication or delegation occurred. No retained status is assigned.
