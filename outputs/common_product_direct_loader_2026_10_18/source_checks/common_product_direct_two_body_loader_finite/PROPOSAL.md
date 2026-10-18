# Finite endpoint launch for the direct two-body SWAP loader

New author derivation requiring a distinct finite-composition check. The stationary source89489 and its now-completed distinct review9818c7 are used only for their actual graph, positive blocks, full stationary operator, phase and ordered feedback bound. This note constructs a fresh finite endpoint device and a complete normalized output on a positive-width window. No earlier gadget runtime or cat-preparer finite theorem is transferred as a conclusion.

The result is conditional on the supplied real positive one-/two-qubit range498 installation, freely degenerate Q,P,R data, physical two-emitter logical input, blank remaining heads and R=0. Old P and its passive environment are retained and relocated coherently. There is no supplied entangled cat, perturbative loader gadget, physical wavepacket preparation or timed switching. The sufficient family below has size Theta(epsilon^(-11/2)) and physical duration Theta(Lambda^-1 epsilon^(-15/2)), with large explicit prefactors. These are analytical sufficient orders for this changed architecture, not optimality, practical efficiency or a native-physics identification.

## 1. Fixed graph, actual finite blocks and input

Fix every interstage cable length to ONE hopping edge in stationary89489. The finite interaction region has496 heads, three ordinary data qubits Q,P,R and920 listed positive blocks. It consists of fourteen eight-head controlled cores, sixteen24-head writing/scalar modules and forty cable bonds. It has eight distinct exterior origins: four left and four right, labeled by head paths(a,b) in{0,1}². The path labels are a one-head encoding across sites, not extra physical data qubits. All modules share the SAME Q,P,R. The source's line embedding puts the499 qubits at distinct(i,0,0), i=0,...,498, with maximum pair range498; the eight distinct +z exterior rays are disjoint. Keep this installation exactly. Its degree36 obstruction to a cubic NN realization remains.

Use beta for the core hopping, so logical path b is unambiguous. Write

    j=beta²/D0, eta=beta/D0, zeta=D0/D1,
    c=112beta+64(sqrt(2)-1)j, D=105.                         (1)

There is no additional data Hamiltonian, record bias, uniform head penalty or receiving-gadget penalty. The positive block expansion gives the common scalar c on every data state and head position. All other module terms annihilate their head vacuum after this scalar is subtracted.

Select ONLY the two left a=1 rays, b=0,1, as input rays. For integer ell>=1 and M=ell+1, add heads n=1,...,M to each selected origin n=0. Use ell ordinary Q_j bonds from0 through ell, followed by the combined positive source block

    B_gamma(ell,M)=Q_gamma(ell,M)
                         +(j-gamma)n_ell+(2j-gamma)n_M,
    gamma=rho j, 0<rho<1.                                   (2)

The source block has full-support norm3j. Its one-head emitter diagonal is2j, and its adjacent site has total diagonal2j after its other ordinary bond is included. On ALL SIX remaining rays—the two unused left a=0 rays and all four right rays—add heads n=1,...,ell, all ell ordinary bonds, and the terminal repair j n_ell. These terminal diagonals are also2j. No ray is removed from the actual problem. These are fixed-diagonal cuts, not deletion of a Laplacian bond together with its diagonal.

Sources and terminal repairs add no scalar. All interactions are static and positive on their complete one-/two-qubit supports. The one-head sector is invariant. Counts, with each source counted as ONE combined block, are

    heads=498+8ell,
    total qubits=501+8ell,
    listed positive blocks=928+8ell.                         (3)

Indeed the two source rays add2(ell+1) heads and blocks; the six ordinary cut rays add6ell heads and6(ell+1) blocks. All496 interaction-region heads and all three shared data qubits were already counted. Extending the supplied +z rays introduces only NN bonds, so range498 and the degree bound do not grow with ell.

The seed isometry E_seed puts one head at the chosen a=1,b emitter M, supplies R=0 and every other head vacant, and leaves the ordinary Q/P/reference factors arbitrary. The logical path is the TWO actual emitter qubits in their span{|10>,|01>}; an arbitrary superposition is supplied logical coherence, not claimed to be a product across those two sites. Q contains the new program. Old P may be entangled with a passive E, and logical Q/b may be entangled with passive Z. The proof is an operator-norm statement before specializing any such state. For a channel interpretation one may choose a fixed old joint state sigma_PE independent of the new logical input. All Q,P,R,E,Z outputs are retained.

The desired output permutation on the ordinary input basis is

    (b,q,p,0_R)->(b xor(1-q),p_Q,q_P,1_R),                    (4)

with auxiliary head path a=1 restored. Thus old sigma_PE becomes sigma_QE, without erasure or a partial trace. The finite target has its head only on the TWO right a=1 rays at1<=n<=ell, and EVERY other head, including all emitters and all496 interaction-region heads, vacant.

## 2. Parameter and exact scalar-source prescription

Fix0<epsilon<=1 and Lambda>0. Supply

    h=eta²=zeta=epsilon/10^7,
    D1=Lambda/64, D0=zeta D1, beta=eta D0,
    j=eta² D0=Lambda epsilon²/(64*10^14),
    rho=epsilon sqrt(h)/10^4, gamma=rho j.                    (5)

These obey eta<=1/8, zeta<=1/4, h<=10^-3, rho<=1/2 and rho²<h. Let q=k-pi/2, z=exp(ik), e(k)=2(1-cos k), E(k)=j e(k), and u=jt. On |q|<=h,

    1.9<=nu:=2cos h<=e'(k)<=2,
    |e''(k)|,|e'''(k)|<=2.                                  (6)

Use the EXACT standalone outgoing amplitude, including its phase,

    F(k)=-i sqrt(2/pi) rho exp(ik)
                         /[(2-rho²)cot k-i rho²].             (7)

Its checked scalar source measure has ||F||_2=1 on(0,pi), and the raw incoming amplitude is conjugate(F). The associated standalone source is precisely(2) attached to an otherwise empty uniform half-line; no assertion about the spectral measure of the full loader is being made.

Choose the real quintic cutoff chi(q): one for|q|<=h/2, zero for|q|>=3h/4, and1-10s³+15s⁴-6s⁵ on each transition, with s=4(|q|-h/2)/h. Put

    P_loss=3rho²/h,
    p_chi=||chi F||_2², g=chi F/sqrt(p_chi),
    G0=2, G1=80/rho, G2=600/rho³.                            (8)

The checked source measure gives1>=p_chi>=1-P_loss>1/2 and ||F-g||_2<=2sqrt(P_loss). The checked shrinking-cutoff lemma applies because rho²<=h, rho<=1/2 and the actual mass condition has just been established. It gives ||g^(r)||_1<=Gr for r=0,1,2; G0=2 is a safe loose bound. The same bounds hold for conjugate(g). This use retains the actual complex F and positive normalization, not a Lorentzian or modulus replacement. The comparison cutoff is not a physical pulse.

For an additional direct check of the first-derivative premise, write the denominator as D_q=-(2-rho²)tan q-i rho². On |q|<=h, |D_q|>=sqrt(q²+rho⁴), |D_q'|<=4, integral|D_q|^-1<=2h/rho² and integral|D_q|^-2<=pi/rho². The raw differentiated profile costs at most sqrt(2/pi)(2+4pi)/rho. On the cutoff transitions, whose total length is h/2, |F|<=2sqrt(2/pi)rho/h and |chi'|<=8/h, so their additional cost is<=8sqrt(2/pi)/rho using rho²<=h. Dividing by sqrt(p_chi)>=1/sqrt(2) gives G1<80/rho. The second-derivative bound600/rho³ retains both phase derivatives and the localized transition terms as proved in source550946 and its distinct check.

The stationary source/check give on this band

    delta=max{13eta²+5zeta,33h}=33epsilon/10^7,
    d_s=144delta/(1-11delta)<epsilon/2048,
    S^0(k)=z^105 [[0,U_f*],[U_f,0]],
    U_f=I_a tensor[X_R C_P^(b) SWAP_QP].                     (9)

The denominator is positive. For the displayed strict inequality,4752*2048<10^7-363 and epsilon<=1 suffice. All reflected ports, both a values and the full data fiber are covered by(9); no program sector is fixed globally. The physical common phase remains exp(-ict), with c in(1).

## 3. Complete local inverses and ordered network derivative bounds

All derivatives in this section are with respect to k; the constants are dimensionless. For each actual core or writer module, let H_v/j be its scalar-subtracted internal head matrix, retaining the diagonal contributions of attached ordinary external leads. It acts on that module's heads and the SAME eight-dimensional Q,P,R fiber. If E_v embeds its port coordinates and Pi_v=E_v E_v*, define

    M_v(k)=H_v/j-e(k)I-z Pi_v,
    L_v(k)=-2i sin(k) M_v(k)^-1 E_v,
    S_v(k)=E_v* L_v(k)-I.                                   (10)

The outgoing boundary sign is -z: substituting the lead value psi_1=z psi_0+(z^-1-z)incoming into its actual hopping equation proves(10). L_v includes every head of that module, not just its ports.

A common bound ||M_v^-1||<=B=11 holds on the band. For a writer, the checked exact two-chain certificate bounds the center inverse by sqrt(159/2)<9, and ||M_v(k)-M_v(pi/2)||<=3h yields inverse<9/(1-27h)<10. This includes both local target-X sectors and the scalar + specialization. These are local sector calculations only; their targets can be changed by other modules.

For a core, the inverse mediator block in units j has norm at most eta²/(1-3eta²), its endpoint-mediator incidence has norm at most2/eta, and the exact endpoint Schur inverse has norm<=1/sin k<=2. The block inverse therefore obeys

    ||M_core^-1||
      <=2[1+2eta/(1-3eta²)]²+eta²/(1-3eta²)<4.                (11)

This uses the actual one-control Schur matrix, with both detunings retained. It is not an effective Hamiltonian substitution. Local control sectors prove the bound for arbitrary coherent control/reference input. The full matrix M_v' and M_v'' have norm<=3, regardless of the large k-independent mediator energies. Inverse differentiation and(10) consequently give

    ||L_v||<=2B,
    ||L_v'||,||S_v'||<=s1=6B²+2B,
    ||L_v''||,||S_v''||<=s2=36B³+18B²+2B.                    (12)

Each S_v has exact norm1. Taking direct sums over all module/head sectors preserves these maxima; the shared ordinary data qubits are not duplicated.

Use the stationary source's eight exterior and eighty interior ends. Let S_loc be the direct sum of the eleven stage matrices, with exterior/interior blocks, and let P_c pair internal ends with the common unit-edge phase z. Thus ||P_c'||=||P_c''||=1. The exact feedback is

    R=(I-P_c S_ii)^-1,
    S=S_ee+S_ei R P_c S_ie.                                 (13)

The checked ideal internal transition has eleventh power zero. Hence ||R||<=r0=11/(1-11delta). Define the explicit ceilings

    a1=1+s1, a2=1+2s1+s2,
    r1=r0² a1,
    r2=2r0³ a1²+r0² a2,
    y0=r0, y1=r1+r0 a1,
    v0=1+r0, v1=y1,
    S1=s1+s1 r0+r1+r0 a1,
    S2=s2+s2 r0+2s1 r1+2s1 r0 a1
                         +r2+2r1 a1+r0 a2.                 (14)

The inverse identities and ordered product rule give ||S'||<=S1, ||S''||<=S2. For example the matrix B_map=P_c S_ie has bounds1,a1,a2; differentiating S_ee+S_ei R B_map gives exactly the terms displayed in(14). No writer is commuted through a control. Unitarity of S follows from the local flux identities and exact matching, as checked in the stationary source.

Let I_in embed the two left a=1 ports, tensor all data and passive references. Set

    Q_out(k)=z^-D S(k)I_in,
    Q1=S1+D, Q2=S2+2D S1+D²,
    H0=G0, H1=G1+Q1 G0,
    H2=G2+2Q1 G1+Q2 G0.                                   (15)

Thus H_r bound the L1 derivative integrals of Q_out g through order2. Removing the single common z^D does not fit data-dependent phases.

All cables have one edge, so there are NO cable-interior heads. For incoming x, the complete stage incoming vector is the exterior x together with y=R P_c S_ie x; its norm is<=v0 and its derivative norm<=v1. Applying the direct sum of L_v maps gives the COMPLETE496-head map T(k), including the eight exterior origins, once each. Therefore

    T0=2B v0, T1=s1 v0+2B v1,
    ||T||<=T0, ||T'||<=T1,
    J0=T0 G0, J1=T0 G1+T1 G0.                              (16)

Every core mediator, writer arm, terminal, junction, module port and shared-data sector is included. No square-root factor496 is needed: the local maps form an orthogonal head direct sum, and v0 already bounds the entire incident vector. These bounds need not be small, even when the exterior scattering defect is small.

## 4. Exact normalized full packet

On each of the eight external rays use n>=1; their n=0 origins are already among the496 coordinates of T. For arbitrary input/data/reference vector xi define

    Psi_n(t)=(2pi)^-1/2 integral exp(iell k-itE(k)) g(k)
               [z^-n I_in+z^n S(k)I_in]xi dk, n>=1,
    Psi_internal(t)=(2pi)^-1/2 integral
               exp(iell k-itE(k)) T(k)I_in g(k)xi dk.            (17)

Here T before restriction maps the full exterior incoming space to the496 heads; restriction by I_in cannot increase(16). The first formula is one vector over ALL eight external rays, not a selected outgoing column with other ports erased. In applications R is initialized to0 only after these full operator formulas have been formed.

The complete stationary module equations, interstage matching and external recurrences imply exactly i dPsi/dt=(H_infinity-cI)Psi. This operator is bounded on the one-head space for fixed positive parameters: it has a finite internal/data matrix attached to eight bounded lead operators. Fourier synthesis bounds the external maps and(16) bounds the finite internal integral. Compact C2 support and bounded E justify strong time differentiation.

The packet is EXACTLY normalized: ||Psi(t)||=||xi|| at every time. To prove this without spectral completeness, send t to minus infinity. The full-integer incoming Fourier field has norm ||g||_2||xi||=||xi|| by Parseval. Its missing n<=0 tail tends to zero by nonstationary integration. The positive-ray outgoing field and all496 internal coordinates also tend to zero by the same integration by parts and(15)--(16). Thus ||Psi(t)|| tends to||xi|| in the remote past. Exact unitary evolution makes that norm constant. Linearity and polarization give an isometry on the full input/data/reference space. No localized eigenstate is assumed absent from the actual seeded finite network.

Restoring the physical scalar gives exp(-ict)Psi(t). The incoming translation is exp(iell k), fixed by reversing the scalar launcher coordinate x=ell-n. It is not independently fitted for the two input rails or any Q/P column.

## 5. Explicit integration-by-parts bounds

For compact C2 vector amplitude f write b_r=||f^(r)||_1. For a phase of the form +/-nk+Lk-u e(k), suppose its derivative magnitude is at least n+g_* with g_*>=1. Its second/third derivatives have magnitude<=2u for u>=0. One integration and sum_(n>=0)(n+g_*)^-2<=2/g_* give

    Tail(f;u,g_*) <=[b1+2u b0/g_*]/sqrt(pi g_*).               (18)

For one fixed coordinate, two integrations give

    |integral f exp(i phi) dk|/sqrt(2pi)
      <=[b2/g_*²+(6u b1+2u b0)/g_*³
                              +12u² b0/g_*⁴]/sqrt(2pi).     (19)

The differentiated terms are f''/(phi')², -3f'phi''/(phi')³, -f phi'''/(phi')³ and3f(phi'')²/(phi')⁴, up to factors of modulus1. Both boundary terms vanish because the cutoff and its first derivative vanish at the ends. These are Hilbert-space norm inequalities; the path/data/reference dimension introduces no factor.

Define

    B_in=G2+6G1+14G0,
    B_out=H2+24H1+200H0.                                    (20)

For u>=u0>=1 at radial levels n=ell,ell+1,ell+2, the incoming phase ell-n-u e has derivative magnitude>=nu u>=u. Formula(19) gives amplitude<=B_in/(sqrt(2pi)u²). At any such level the outgoing phase n+ell+D-u e has derivative>=ell/4 for u<=7ell/8. Its amplitude is at most16B_out/(sqrt(2pi)ell²): here u/(ell/4)<=7/2, so the precise numerator coefficients21 and154 are below24 and200. The incoming vector is supported on the selected two rays, whereas the outgoing vector covers all eight. Treating them as vectors at each radial level retains every port.

The internal phase ell k-u e has no radial n. If |ell-u e'|>=q_*>0, single integration gives

    ||Psi_internal(t)||
       <=[J1/q_*+2u J0/q_*²]/sqrt(2pi).                     (21)

This is the complete496-head restriction, including all exterior origins. It is not an internal population inferred from a scattering probability.

## 6. Literal endpoint source and complete early match

The comparison time t0=u0/j is mathematical only; no Hamiltonian changes there. For the comparison, add auxiliary negative-n chains beyond the TWO selected input origins, and decoupled exterior continuations beyond every finite cut. Auxiliary diagonals are2j. The actual extended finite operator keeps all those added continuations decoupled.

Define a reference operator by giving each selected input ray an ordinary continuation through n=0 into its negative-n chain, changing that origin's diagonal from its actual3j to2j, and disconnecting its two beta mediator edges. Retain the ENTIRE actual finite operator submatrix on all other heads, including the unused left rays, all writers, core mediators, data interactions and six finite capped rays, with their diagonals unchanged. The two reference launchers are scalar, identical and disjoint, with emitter M and lead coordinate x=ell-n>=0. The complementary head subspace is vacant on the reference trajectory and, after subtracting c, causes no data evolution. Large mediator energies are retained in that complementary operator; they are not bounded by4j or removed from an actual evolution.

Let V be actual minus reference in this common one-head Hilbert space. At each selected origin it contains a +j diagonal, deletion of the artificial ordinary edge, and the actual two mediator hoppings -beta. The diagonal/edge part has norm<2j. The two selected origins belong to distinct first-stage cores, so their mediator contact sets are disjoint and the latter incidence norm is sqrt(2)beta. Consequently

    ||V||<=2j+sqrt(2)beta.

Its contact support includes the selected origins, their artificial neighbors and their mediator neighbors. The scalar reference seed reaches none of it in fewer than M powers. On its invariant launcher subspace the reference generator has norm<=4j. Ordered Duhamel, with the ACTUAL full unitary on the other side, therefore gives

    E_contact<=u0(2+sqrt(2)/eta)
                     sum_(m>=M)(4u0)^m/m!.                  (22)

For ell>=100u0 and u0>=1, the factorial tail is at most2*8^-M<=2/M². For instance (4e u0/M)^M<8^-M and the successive-term ratio is below1/25. Hence

    E_contact<=(2+sqrt(2)/eta)/(5000u0).                     (23)

This estimate pays beta/j=1/eta and does not use a false4j bound for the whole physical generator.

The checked EXACT scalar decomposition of a standalone source is occupied-emitter amplitude A(t), plus outgoing Fourier field O_t F and incoming field I_t conjugate(F). It has |A(t0)|<=1/(rho²u0). Replacing the two spectral amplitudes by g and conjugate(g) costs at most4sqrt(P_loss) by(8) and Fourier contraction. The unwanted incoming scalar field and the part of the full-integer outgoing field beyond the emitter each cost at most(G1+2G0)/sqrt(u0) by(18), since nu>=1.9. After x=ell-n reversal, the surviving full-integer outgoing field is precisely the incoming field of(17), with its exact exp(iell k) phase. Identical reference launchers give the same operator error for a coherent two-emitter input, without summing two branch errors.

At u0 with ell>=100u0, the missing n<=0 portion of this full-integer incoming field and the unwanted outgoing positive-ray field in(17) together cost at most

    2(G1+G0+H1+H0)/sqrt(ell).

Their phase gaps are at least ell-2u0>=.98ell; D=105 only increases the outgoing early gap. The entire496-head vector costs at most2(J0+J1)/ell by(21). One may count the selected origin amplitudes in both this upper bound and the missing n<=0 tail: that is a triangle overestimate, not omission or a duplicate physical coordinate in(17).

Thus the actual full seeded state at t0 and the exact normalized infinite packet, embedded in the same extended space, differ in operator norm by at most

    E_init=E_contact+rho^-2/u0
       +2(G1+2G0)/sqrt(u0)+4sqrt(P_loss)
       +2(G1+G0+H1+H0)/sqrt(ell)+2(J0+J1)/ell.              (24)

The true physical factor exp(-ict0) is common. This is a full-vector comparison, so it pays every seeded component not present in the packet, including possible localized spectral contributions. The actual finite or infinite loader is NOT assigned the standalone source's spectral measure or asserted to have no point spectrum.

## 7. Exact cuts, integrated propagation and full finite target

Write the extended actual finite relative generator as K_ext and the uniform infinite relative generator as K_infinity. In K_ext-K_infinity, either selected source ray contributes exactly

    Delta_src=(j-gamma)Adj(ell,ell+1)
                            +j Adj(ell+1,ell+2).             (25)

On each of the other SIX rays it is Delta_cap=j Adj(ell,ell+1). These are adjacency changes only. Equation(2) and the six positive endpoint repairs are what keep every diagonal equal to the infinite value2j. The extended finite operator is the actual physical finite generator direct-summed with auxiliary diagonal2j Dirichlet lines. Its full cut perturbation has norm<=sqrt(2)j; the eight separate contacts form a head-position direct sum on the shared fiber.

There are at most three sampled radial levels per contact. Using the complete port-vector amplitudes in(20), their norm is bounded by sqrt(3) times the sum of the incoming and outgoing ceilings. Duhamel from t0 to t, with u<=7ell/8 and dt=du/j, gives

    E_cut<=100[B_in/u0+B_out/ell].                           (26)

Explicitly the coefficient sqrt(6)/sqrt(2pi) is below1, integral_(u0)^u v^-2 dv<=1/u0, and the outgoing constant16/ell² integrates for at most7ell/8 to14/ell. The factor100 safely covers those bounds and the smaller two-level caps. No ray or repeated reflection is omitted: the exact infinite packet already contains the full ordered network feedback.

Choose ell>=100D and the final window

    t_minus=3ell/(4j), t_plus=7ell/(8j).                     (27)

Then throughout this window, u nu-ell>=.425ell. Equations(18),(21) bound the remaining incoming external field and complete internal field by

    d_late=2(G1+6G0)/sqrt(ell),
    m_late=(3J1+11J0)/ell.                                  (28)

Define the full-integer scalar outgoing sequence with NO extra fitted -i:

    B_n(t)=(2pi)^-1/2 integral
                     exp(i[n+ell+105]k-itE(k)) g(k) dk.       (29)

The four writer-stage -i factors have already multiplied to1 in(9); the source's own phase remains inside g. By Parseval over all integer n, ||B(t)||=1 exactly. The n<=0 omitted tail has gap at least .425ell-D>=.4ell, and the n>=ell+1 tail has gap at least ell/4. Applying(18) to both gives combined omitted norm at most

    d_F=5(G1+8G0)/sqrt(ell).                                (30)

If d_F<1, let beta_ell(t) be the restriction of(29) to1<=n<=ell divided by its POSITIVE norm. The full-integer scalar field differs from this normalized finite restriction by at most2d_F. No physical renormalization, measurement or output trace is performed.

Let V_log be the exact basis permutation(4), and J_F insert the head on the two right a=1 finite rays, with all other heads vacant. The physical comparator is

    exp(-ict) J_F[beta_ell(t) tensor V_log],                  (31)

with ordinary Q,P,R and every passive reference retained. The outgoing spectral error is at most d_s by(9) and Parseval. Combining (24),(26),(28)--(30), propagating the initial error by the exact finite unitary, proves the complete actual output comparison

    sup_(t_minus<=t<=t_plus)
      ||exp(-itH_fin)E_seed
          -exp(-ict)J_F[beta_ell(t) tensor V_log]||
      <=E_init+100(B_in/u0+B_out/ell)
                         +d_late+m_late+d_s+2d_F.             (32)

Only the mathematical target in(31) is normalized. The actual residual emitters, all496 heads, all eight finite rays, wrong records, wrong paths and relocated old-state/reference correlations are all in the norm. This is not a conditioned successful-output comparison.

## 8. Explicit simultaneous split policy and allocations

Evaluate all constants in(5),(8),(12)--(16),(20) BEFORE choosing a distance or time. Define

    L=1+(G1+2G0)+(H1+H0)+(G1+8G0),
    Q=1+eta^-1+rho^-2+J0+J1+B_in+B_out,
    u0=10^12 max{1,(L/epsilon)²,Q/epsilon},
    ell=ceil max{100u0,100D}, M=ell+1,
    t0=u0/j, t_minus=3ell/(4j), t_plus=7ell/(8j).             (33)

These are exact noncircular prescriptions. The local/network jets depend on the fixed graph and eta,zeta,h, but not on ell or u0. They obey

    L/sqrt(u0)<=epsilon/10^6,
    Q/u0<=epsilon/10^12,
    L/sqrt(ell)<=epsilon/10^7,
    Q/ell<=epsilon/10^14.                                  (34)

In particular u0>=10^12, ell>=100u0, ell>=100D and t0<t_minus. Every inverse, spectral mass, factorial condition and early/late derivative gap used above holds. The split keeps first-derivative terms divided by square roots separate from second-derivative terms divided by time or distance; it does not square an unnecessary G2 contribution.

The complete bound(32) is paid by the following explicit allocations:

| Term | Ceiling under(33) |
|---|---|
|Early physical/reference contact(23)|Q/u0<=epsilon/10^12|
|Occupied-emitter residual|Q/u0<=epsilon/10^12|
|Two unwanted standalone/reference tails|2L/sqrt(u0)<=2epsilon/10^6|
|Both spectral replacements|4sqrt(3)epsilon/10^4<epsilon/1024|
|Early external packet match|2L/sqrt(ell)<=2epsilon/10^7|
|Early complete internal vector|2Q/ell<=2epsilon/10^14|
|Integrated cuts|100Q/u0+100Q/ell<=100epsilon/10^12+100epsilon/10^14|
|Late incoming field|2L/sqrt(ell)<=2epsilon/10^7|
|Late complete internal vector|11Q/ell<=11epsilon/10^14|
|Full stationary operation|d_s<epsilon/2048|
|Finite outgoing restriction and normalization|10L/sqrt(ell)<=10epsilon/10^7|

For the contact line,2+sqrt(2)/eta<4Q and(23) are sufficient. The definition of L bounds every first-derivative combination used in the table, including G1+G0+H1+H0; Q bounds both internal constants and both boundary coefficients. No actual norm was replaced by an assumed small internal population. The sum is below epsilon/8. Also d_F<=5epsilon/10^7<1 before normalization is used.

Thus the proposed complete finite endpoint theorem is

    sup_(t_minus<=t<=t_plus)
      ||exp(-itH_fin)E_seed
          -exp(-ict)J_F[beta_ell(t) tensor V_log]||
          <epsilon/8.                                      (35)

The associated unhalved channel distance is below epsilon/4, including arbitrary passive references and every output, by the two-isometry inequality. In the final window, the joint event of R=1 and the single head on the two retained right a=1 output rays has probability greater than1-epsilon²/64; all other heads are then vacant in the one-head sector. The full logical/old-state accuracy is the stronger operator statement(35), not inferred solely from this event probability. The interval width is ell/(8j)>0 and its relative width with respect to t_minus is1/6. No physical switch occurs at any of these comparison times.

## 9. Cap, actual sufficient orders and limits

The stationary full-support data loads remain

    Q:32(D1-2beta)+8j,
    P:24(D1-2beta)+16j,
    R:16j.

At the scale(5), beta<=D1/32 and j<=D1/256, so the safe ceilings are Lambda/2+Lambda/2048,3Lambda/8+Lambda/1024 and Lambda/1024. Core endpoint6beta+4j, mediator D1+2beta and writer-head12j ceilings are also below Lambda. New combined-source loads are3j at the emitter and5j at its neighboring lead head; six repaired ends have load3j; ordinary ray interiors have4j. Thus every actual incident block-norm sum, on full qubit support, is below Lambda. Sources replace their last ordinary bond; they are not added on top of a still-present j hopping. The scalar remains exactly(1).

The resource orders follow from the DISPLAYED constants, not from extrapolating an older theorem. At epsilon down to zero, delta tends to zero and r0 tends to11. B=11,s1,s2 are fixed; all S1,S2,Q1,Q2,T0,T1 have finite positive bounds and limits by(14)--(16). The large ratio D0/j is harmless in the proved core inverse(11), so no hidden eta^-1 derivative has been omitted. The physical early-contact eta^-1 is separately retained in Q.

The exact policy has rho=Theta(epsilon^(3/2)), so G1=Theta(epsilon^(-3/2)) and the chosen ceiling G2=Theta(epsilon^(-9/2)). With fixed G0=2, H1,J1 have order at most epsilon^(-3/2), and H2,B_in,B_out have order epsilon^(-9/2). Their positive G2 terms give matching lower bounds. Therefore

    L=Theta(epsilon^(-3/2)),
    Q=Theta(epsilon^(-9/2)).

The two growing terms in the maximum(33) have orders epsilon^-5 and epsilon^(-11/2), respectively. The latter is asymptotically dominant. Since D=105 is fixed and j=Lambda epsilon²/(64*10^14),

    u0, ell, head count, qubit count, block count,
        and j t_plus =Theta(epsilon^(-11/2)),
    t_plus =Theta(Lambda^-1 epsilon^(-15/2)),
    gamma =Theta(Lambda epsilon^(7/2)).                       (36)

These are orders of this sufficient recipe, not lower bounds on any physically possible implementation. Rounding and the fixed interaction-region addends do not change them. The source and coupling magnitudes are exact supplied values; their smallness is not a fabrication tolerance or a coefficient-production cost certificate. Large fixed jet bounds and asymptotic crossovers are not suppressed by the exponent notation. No comparison to a fixed old apparatus, old17 runtime, or plain-router runtime is used to prove(35).

This result is finite-window operation only. It does not imply an all-time record1 branch, a normalized rare-success guarantee, permanent halt, capture, reset or output isolation. The record can change during an internal terminal visit and on a later return. It supplies no cooling or rest-energy certificate, no physical Q/path preparation or old-environment decoupler, and no native interaction/readout identification. Active H_PE, receiving penalties, or any additional head-independent Q/P/R dynamics are outside its hypotheses. The new ordinary program and the old P/E state are retained; neither is discarded.

## 10. Exact dependencies, exposure and work record

All N paths are under /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. Complete direct source/check texts were read at the identities below. The stationary source was authored and fully reread in the immediately preceding coherent task, then hash-refreshed here; its distinct check was read completely here after ROOT reported its completion.

| Direct premise | Source SHA256 | Distinct-check SHA256 |
|---|---|---|
|common_product_direct_two_body_loader/PROPOSAL.md and sibling_check/REVIEW.md|89489c13a6450f142c8ac2212ee680bc7272addcff30c53fcb01e52dff4ee7a9|9818c72551eec2d2be17224dde6e07335f1ff7157b94a91c4a372aff3873343d|
|common_product_endpoint_launch/PROPOSAL.md and sibling_check/REVIEW.md|fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4|51247de9ba58bbfeb7f731c478d939e05e2e9d90956192d2e9e6f612401662c1|
|common_product_writer_resolvent_sharpening/PROPOSAL.md and sibling_check/REVIEW.md|22bca57ebcbfb8cfabebbe044cd5302e784e585b503cee28d6172afc72e54cf0|d96ed6b26856490d802ceed2009f75aa9c0919eb8760bcfffe0389807965d1b5|
|common_product_narrow_cutoff_derivative/PROPOSAL.md and sibling_check/REVIEW.md|550946fdebc4e68522c997ed914e23a8baf40cb660dfc22e4f09e00add1216a3|6a4866e76cc5c6c760284c9a3f6c07c71410f701d727e8765edc8f6a57d328a4|

Here sibling_check means the same directory name with `_check` appended, not a literal folder named sibling_check. The writer's exact positive matrix, signs, two-chain inverse certificate and derivative proof were read in full in the source/check; no historical program was rerun. The scalar source's complete measure and phase are adopted at the checked standalone scope; the new loaded network's spectrum is not identified with it. The narrow-cutoff dependency supplies its local derivative lemma only, not its downstream finite or flag conclusions.

The stationary source's exact primitive sources/core checks were fully read in the preceding coherent task and reused at their recorded identities: one-control76b5, core60bc and writer93445, with full hashes and recovery paths in source89489 section9. Their hypotheses are checked explicitly in sections1--3 here. Their older finite performance results are not inputs.

Additional complete source reads used as exposed proof-method context, without transferring their finite conclusions, were:

- common_product_stage_record_packet/PROPOSAL.md,3477197cdf54d18ab538c517726d64f3dbc556f6ddb7a6d4b2608b458d34eeb9: packet normalization, local inverse and derivative methods.
- common_product_stage_record_finite_seed/PROPOSAL.md,7286105ffd9b6b6d0caa97b121c5e79d37dfcf638128d63c6bbc144e9aa2a995: early source comparison and fixed-diagonal cuts.
- common_product_autonomous_cat_preparer_finite/PROPOSAL.md,942a98e3d2d84bfe4e2393bf6cd4119c8c2fd63e5589031280272b7582914459: full-fiber stage composition and finite comparison layout. Its six-stage graph, target, geometry, counts and theorem are NOT this eleven-stage result.

The general-cutoff derivative source378086 was initially inspected only in part; it is not an additional adopted premise. First-derivative inequalities were checked directly in section2 and the full newer550946 source/check were read. Any tool output truncated during the load-bearing source/check reads was reread over the missing content before use. No truncated output was counted as completed coverage.

ROOT proposed the direct-loader architecture and requested a fresh finite proof while its stationary check was running. That check subsequently completed at the exact9818c7 identity above. ROOT also suggested a coarse squared-policy exponent; the sharper split policy here is derived from the actual1/sqrt(u) and1/u error terms. This is source-exposed continuation by the stationary proposal's author, using the same model and effort. The completed stationary/local checks do not independently check the new normalized packet, finite source/cuts, counts, allocations or resource orders. A distinct finite-composition review is still required.

Separate range21 and possible all-horizon branch developments were mentioned during this work; neither is incorporated as a premise or conclusion here. The exact fixed range498 graph and finite-window scope remain frozen in this source.

Only common_product_direct_two_body_loader_finite/PROPOSAL.md was written. Work was analytical derivation, complete text reads and deterministic file/hash bookkeeping. No scientific executable, dynamics simulation, numerical solver, parameter sweep, W/Git/checkpoint/axiom/editable-prompt/model change, publication or delegation occurred. No editable prompt file changed, and no retained or independent finite acceptance is claimed.


