# Finite seeds on distinct input rays of the positive four-port router

New authored conditional theorem requiring a distinct check. The checked four-port core admits quantitative exact packets and a finite product-basis seed comparison on a nonzero relative observation window. The output target occupies the two distinct O rays, with all I-ray heads, four emitters and four mediators vacant. The claim is a complete vector/isometry comparison, not postselection or a permanent record. ROOT proposed the extension and candidate derivative/contact constants; the new constants and interfaces are derived below after that exposure.

The physical Hamiltonian and preparation remain supplied. In particular twelve separate program bits encode the two legal settings; arbitrary coherent inputs are not claimed to be sitewise product states. The theorem is conditional on the exact source contracts below, including the checked standalone launch. Checks of those sources do not independently check this composition.

## 1. Literal finite device and conventions

Use the four-cell K2,2 core of source60bc, with port order I0,I1,O0,O1. Its legal encoded program selects an active matching R_p=[[0,C_p],[C_p,0]], C_0=X, C_1=I, and the complementary inactive matching S_p. Four mediators and twelve distinct controls are retained. On each of the four rays put head sites n=0,...,M, where n=0 is the core endpoint and ell=M-1. Take M>=2. Install uniform Q_j bonds through (M-2,M-1) and the final positive block

    B=Q_gamma(M-1,M)+(j-gamma)n_(M-1)+(2j-gamma)n_M.

Here j=b²/D0, a=2j, eta=b/D0<=1/8, 0<zeta=D0/D1<1/2, gamma=rho j with 0<rho<1. Thus D0>2b. Both outer one-head diagonals are exactly2j. The four B blocks are identical even though the initial head is restricted to emitter I0,M or I1,M. All O-ray heads, including their emitter sites, start vacant. All mediators start vacant. Every absent interaction and all roles, coefficients and legal-program correlations are supplied just as in the core source.

Let E_seed embed an arbitrary encoded I-path/program/reference vector xi, with ||xi||=1, in those two physical emitter states. The legal program space is the span of the two twelve-bit strings of60bc. Neither a bare logical program qubit nor identification of physical controls is substituted. Coherent program/path/reference entanglement is allowed and preserved by the controlled estimates. Basis legal program/path seeds are literal sitewise product states.

Write h_F=H_phys-8bI on the conserved one-head space. The scalar is exactly8b from the four cells, independent of head location and program; the outer B blocks add no scalar. The infinite comparison h has the same core and four infinite uniform positive rays. Its exact Schur scattering, with z=e^(ik), E=2j(1-cos k), is

    V=2I-alpha(I+R_p)-beta(I+S_p),
    alpha=D0/(D0-E), beta=D0/(D1-E),
    S_phys=(z^-1 I-I+V)^-1[(1-z)I-V],
    Q=e^-ik S_phys.

On the central band K=[pi/3,2pi/3], E<=3j, vmin=sqrt(3)j, vmax=2j. More restricted spectra inside this band may use these same conservative velocities. The core source proves ||Q||=1 and

    ||Q-R_p||<=d_S=13eta²+5zeta.                 (1)

The sum in (1) is essential; the previous two-port maximum is not valid here.

## 2. New four-port derivative bounds

The commuting real symmetric involutions R_p,S_p have fixed joint eigenchannels (r,s) in {+1,-1}². In each channel put

    v=2-alpha(1+r)-beta(1+s), w=1-r,
    d=v-w=-(alpha-1)(1+r)-beta(1+s),
    W=1-z+vz, N=1+r z, F=N/W.

Exact fractional subtraction gives q=r-dF, where q=e^-ik sigma(v;k). This identity retains the phase and applies to both w=0 and w=2.

Set delta=eta²+zeta. Writing e=E/D0 gives 0<=e<=3eta², |e'|<=2eta², |e''|<=2eta². Differentiating alpha=(1-e)^-1 and beta=zeta(1-zeta e)^-1 yields

    |d|<=6eta²/(1-3eta²)+2zeta/(1-3eta²zeta)<=7delta,
    |v'|<=5eta²(1+zeta²)<=5delta,
    |v''|<=6eta²(1+zeta²)<=6delta.               (2)

For example each doubled alpha second derivative is bounded by
4eta²/(1-3eta²)²+16eta^4/(1-3eta²)³<6eta². The doubled beta bound is the same expression with denominators 1-3eta²zeta and the respective zeta²,zeta³ numerators, bounded by6eta²zeta². The first derivatives follow from4eta²/(1-3eta²)²<5eta² and its beta counterpart. These estimates prove (2) without treating inactive and active channels as disjoint errors.

Also |v|<=2: its largest value is2 and its smallest is -2(alpha-1)-2beta, whose magnitude is less than2 on the stated domain. The stronger absolute estimates |v'|<=5(1+1/4)/64<1 and |v''|<=6(1+1/4)/64<1 follow. Therefore

    |W|=|z^-1-1+v|>=sin k>=sqrt(3)/2,
    |W^-1|<=2, |W'|<=4, |W''|<=6,
    |(W^-1)'|<=16, |(W^-1)''|<=280.

Since |N|<=2 and |N'|=|N''|=1, these imply |F|<=4, |F'|<=34, |F''|<=594<600. Differentiating q=r-dF now proves, uniformly over all four channels and both programs,

    ||Q'||<= (5*4+7*34)delta<=260delta,
    ||Q''||<= (6*4+2*5*34+7*600)delta<=4600delta. (3)

The joint basis is k-independent. Thus (3) is an operator bound, including references, with no eigenvector derivative or dimension multiplier.

Let N_inc be the endpoint-edge incidence matrix (columns e_u+e_v), whose norm is2. The full four-mediator coefficient map before Fourier normalization is

    R_med=diag[c_e] N_inc^T(I+zQ), c_e=b/(D_e-E).

Here max c_e<=eta/(1-3eta²)<2eta, and max|c_e'|<=2eta³/(1-3eta²)²<3eta³. Consequently

    ||R_med||<=4eta/(1-3eta²)<5eta,
    ||R_med'||<=12eta³+4eta(1+260delta)<=600eta. (4)

For the last inequality delta<=33/64 and 12eta²<=3/16, so the coefficient is below541. These are whole-vector mediator norms, not per-mediator bounds summed four times. Formula (4) includes the derivative of the explicit z phase.

## 3. Exact packet, normalization and elementary envelopes

Take g in C_c²((0,pi)), supported in K, ||g||_2=1, with its exact source phase and positive normalization specified below. Define, for n>=0,

    Psi_n(t)=(2pi)^-1/2 integral g(k){
       exp(i[(ell-n)k-tE])xi
       +exp(i[(n+ell+1)k-tE])Q(k)xi} dk,
    Psi_med(t)=(2pi)^-1/2 integral
                    exp(i[ell k-tE])R_med(k)g(k)xi dk.  (5)

These are vector amplitudes in all four ports and mediators. For each legal program, the bulk recurrence, exact boundary equation and eliminated mediator equation prove hPsi=i d_t Psi. Full-integer Fourier synthesis bounds the lead maps, and the finite mediator integral is bounded by its L1 coefficient. Multiplication by bounded E on K permits strong differentiation in the one-head Hilbert space. The full h is a bounded self-adjoint operator at each fixed finite D0,D1; its bound need not be4j. Hence (5) has constant norm.

As t tends to minus infinity, the incoming full-integer state has norm||xi|| and its omitted negative-radial part tends to zero by nonstationary phase. The outgoing positive-ray part tends to zero by the same argument with velocity pointing away from that sector in reverse time. The mediator integral tends to zero by one integration by parts, using (4). Thus ||Psi(t)||=||xi||. Linearity and polarization prove an isometry, including coherent program/reference input. This proves normalization of this family without a global spectral-completeness or no-bound-state assumption.

Set G_a=||g^(a)||_1 and

    H0=G0, H1=G1+260delta G0,
    H2=G2+520delta G1+4600delta G0,
    J0=5eta G0, J1=5eta G1+600eta G0.

These bound the L1 norms of Qg and its first two derivatives, and R_med g and its first derivative. For any vector amplitude with first two L1 bounds A0,A1 define

    T_A(t,q)=[A1+(2j|t|/q)A0]/sqrt(2pi)
                                      *sqrt(q^-2+q^-1),
    M(t,q)=[J1/q+2j|t|J0/q²]/sqrt(2pi), q>0.    (6)

T_G and T_H use G0,G1 and H0,H1. These follow by a single integration by parts: at successive radial sites the phase gradient magnitude is at least q+r, so each amplitude norm is at most [A1+(2j|t|/q)A0]/[sqrt(2pi)(q+r)], and sum_(r>=0)(q+r)^-2<=q^-2+q^-1. For the mediator there is one four-dimensional vector, with no radial sum. The bounds hold for arbitrary passive-reference dimension because they use vector norms before integration.

For later boundary control, two integrations by parts give the pointwise envelope

    (2pi)^-1/2[A2/q²+6j|t|A1/q³
                      +(2j|t|/q³+12j²t²/q^4)A0]. (7)

Indeed the differentiated integrand is bounded by |a''|/q²+3|phi''||a'|/q³+(|phi'''|/q³+3|phi''|²/q^4)|a|, with |phi''|,|phi'''|<=2j|t|. Compact C2 support kills all boundary terms. All time factors in (6),(7) are explicit.

## 4. Early actual contact and exact launch interface

Use four integer-coordinate port lines and four physical mediator coordinates as a common auxiliary space. Extend the finite h_F by independent Dirichlet half-lines n<=-1 and n>=M+1 with diagonal2j. The reference h_ref is four independent standalone source chains with emitter M, inward source coordinate x=ell-n>=0, and the same detached exterior n>=M+1. Its four detached mediators have exactly the same diagonal D_p as the actual operator. Only the two I emitters carry the reference seed.

The difference h_F,ext-h_ref has on each (0,-1) pair the block [[j,j],[j,0]], since the actual core endpoint has diagonal3j and the reference line diagonal2j. Each such block has norm<2j. In addition it contains the actual mediator coupling B and its adjoint, of norm||B||=2b. No mediator diagonal changes. Therefore

    ||h_F,ext-h_ref||<=2j+2b.                    (8)

Four orthogonal copies of the contact block do not multiply its norm by four. Although the full reference includes large D_p, the seed evolves in its mediator-vacant source/lead invariant subspace, where ||h_ref||<=4j. The compensated emitter has row sum2j+gamma<=3j, and all ordinary source-lead rows have absolute sum<=4j. A reference power cannot reach contact n=0 from M in fewer than M hops, and never populates a mediator. Thus, with u0=jt0,

    E_early=min{2,u0(2+2/eta)
                         sum_(r=M)^infinity (4u0)^r/r!} (9)

bounds the actual/reference evolved-seed difference at t0. This follows by the Taylor tail for the reference contact projection and Duhamel with the actual unitary. It never assigns norm4j to the actual microscopic generator.

Use the exact checked standalone launch profile g_+, real cutoff chi, p=||chi g_+||_2², and g=chi g_+/sqrt(p), with the positive square root. Let g_-=conjugate(g_+) and P be its exterior spectral probability ceiling. Its launch error is2delta_launch, where

    delta_launch=sqrt[R0²+(L0+2sqrt(P))²],
    R0=min{1,2j/(pi gamma²t0)},
    L0=B_minus/sqrt(2pi)*sqrt[(t0vmin)^-2+(t0vmin)^-1],
    B_minus=||(chi g_-)'||_1+(2j/vmin)||chi g_-||_1.

Require delta_launch<1. The two occupied input copies have the same source phase and normalization, so the source isometry bound applies to arbitrary superposition/reference input without a factor counting rays. O copies remain vacant under the reference.

Coordinate reversal x=ell-n identifies the reference outgoing packet with the positive normalization of the n<=ell projection of the incoming full-integer Fourier packet with phase (ell-n)k-tE. Its replacement by that full state costs at most2d_right, where d_right=T_G(t0,1+t0vmin). This is an exact source phase match, not an incoming-packet preparation assumption.

When ell-t0vmax>0, the full incoming integer state and (5), embedded in the same space, differ by at most

    e_match={T_G(t0,ell+1-t0vmax)²
             +T_H(t0,ell+1-t0vmax)²
             +M(t0,ell-t0vmax)²}^1/2.           (10)

The three terms concern negative-radial incoming tails, nonnegative-radial outgoing amplitudes and all four mediators, respectively. Their coordinate sectors are orthogonal. Equations (8)-(10) give the complete finite-vector match

    ||exp(-it0 h_F)E_seed xi-Psi(t0)||<=e0,
    e0=E_early+2delta_launch+2d_right+e_match.    (11)

All actual emitter/core amplitudes and spectral components missing from (5) are paid in this norm. The infinite core has bound states; none is assumed to have zero seed overlap. No identification of finite and infinite spectral projections is made or required. Auxiliary negative sites have zero amplitude in both vectors in (11).

## 5. Fixed finite boundary and full normalized O-ray target

On every infinite ray add the fixed-diagonal perturbation

    Delta=(j-gamma)Adj(ell,ell+1)+j Adj(ell+1,ell+2).

The result is exactly h_F plus decoupled exterior Dirichlet half-lines; all contact diagonals stay2j. On the three contact sites its matrix is [[0,j-gamma,0],[j-gamma,0,j],[0,j,0]], of norm

    d_hop=sqrt((j-gamma)²+j²).

The four-ray operator is a direct sum of this matrix, tensor identity on program/reference, so its norm is still d_hop. At each of the three sites, (7) bounds the entire port vector. Therefore ||Delta Psi|| is bounded by sqrt(3)d_hop times the single-site envelope, with no additional port factor.

For t0vmin>2 and tplus vmax<2ell-2 put qi(t)=tvmin-1 and qo(t)=2ell-tvmax. At n=ell,ell+1,ell+2 the incoming gradient has magnitude at least qi(t), while the outgoing gradient is at least qo(t). The slightly weaker incoming offset -1 also covers n=ell-1. Since t/qi(t)<=2/vmin for t>=t0, define

    A_i=G2+(12j/vmin)G1+(4j/vmin+48j²/vmin²)G0,
    A_o=H2+(6jtplus/qo(tplus))H1
          +(2jtplus/qo(tplus)+12j²tplus²/qo(tplus)²)H0,
    E_outer=sqrt(3)d_hop/sqrt(2pi){
      (A_i/vmin)[1/qi(t0)-1/qi(tplus)]
      +(A_o/vmax)[1/qo(tplus)-1/qo(t0)]}.        (12)

Here t/qo(t) increases up to tplus, so A_o bounds all earlier coefficients. Integrating qi^-2 and qo^-2 gives exactly (12). The integrands are nonnegative; it uniformly bounds every shorter integration interval. Ordered Duhamel, using the exact normalized packet (5), yields

    ||exp(-it h_F)E_seed xi-Psi(t)||<=e0+E_outer

for t in[tminus,tplus], provided tminus>=t0. There is no accumulated effective-cell replacement term and no alteration of the central core.

Suppose also tminus vmin>ell. Define

    d_L=T_G(tminus,tminus vmin-ell),
    m_L=M(tminus,tminus vmin-ell),
    d_packet=d_L+d_S+m_L,
    n_O=T_G(tplus,2ell+2-tplus vmax),
    d_O=n_O/(1-d_packet).

Require d_packet<1 and d_O<1. Incoming and mediator late bounds decrease with t: q=tvmin-ell grows, while t/q and t/q² decrease. The outgoing omitted-tail numerator increases with t because q=2ell+2-tvmax decreases. These prove the mixed-endpoint uniform bounds; no monotonicity of the normalization quotient is presumed.

Define the common scalar sequence

    B_n(t)=(2pi)^-1/2 integral exp(i[(n+ell+1)k-tE])g(k)dk,
    beta_F(t)=P_(0<=n<=ell)B(t)/||P_(0<=n<=ell)B(t)||.

Replacing Q by R_p in the outgoing full-integer synthesis costs at most d_S by Plancherel, and restriction cannot increase it. Dropping the incoming half-line and mediator costs d_L+m_L. Since Psi has norm1, the unnormalized ideal positive-ray outgoing vector has norm at least1-d_packet. Its finite restriction has a nonzero norm because its tail ratio is at most d_O<1. Two positive normalizations cost at most2d_packet+2d_O, by the elementary inequality ||u-v/||v||||<=2||u-v|| when ||u||=1 and v nonzero, applied first to the whole outgoing ray and then to its truncation.

Because xi has only I components, R_p xi has only O components with logical map C_p. Let J_O embed beta_F on the O0,O1 ordinary sites and the controlled logical map C, preserving twelve-bit legal programs. The full physical comparison is

    sup_(tminus<=t<=tplus)
      ||exp(-it H_phys)E_seed
           -exp(-i8bt)J_O(beta_F(t) tensor C)||
        <=min{2,e0+E_outer+2d_packet+2d_O}.      (13)

This is the induced isometry norm, including arbitrary passive references. The target has all I-ray heads, four emitter heads and four mediators vacant. Actual wrong-ray amplitudes, reflections and all non-target coordinates are counted, not traced out. The target packet moves and its phase is retained throughout a finite window. No writer or Record system is attached.

## 6. Explicit simultaneous sufficient family

For completeness the same exponents as the checked two-port microscopic family can be certified here, after paying every changed constant. Define one fixed cutoff with plateau |k-pi/2|<=pi/24, transition width pi/12, and zero for |k-pi/2|>=pi/8. On the transition use 1-10s³+15s^4-6s^5, s in[0,1]. This is C2 with ||chi'||_infinity<8, ||chi''||_infinity<100. Use the conservative band halfwidth pi/6. The exact launch profile is

    g_+(k)=-i sqrt(2/pi) rho exp(ik)
                           /[(2-rho²)cot k-i rho²].

This fixes the source phase as well as its modulus. The checked resonance-integrated derivative source378086, with L=tan(pi/6), S=sec²(pi/6), supplies

    G0<2, G1<=100/rho, G2<=2000/rho³,
    B_minus<=200/rho, P<=11rho², p>1/2          (14)

for the family below. In detail its explicit constants are C1=(2/sqrt(pi))[2L(K1+1)+pi] and C2=(2/sqrt(pi))[2L(K2+2K1+1)+(2K1+2)pi+4L+8S], below100 and2000 for K1<8,K2<100. Its incoming identity is B_minus=sqrt(p)[G1+sec(pi/6)G0]. The exterior-probability bound4rho²/[pi(2-rho²)²tan(pi/24)] is below11rho². With rho<=1/256 this ensures p>1/2. No empirical source linewidth is used.

For 0<epsilon<=1 and fixed incident cap Lambda>0 choose

    rho=epsilon/256,
    u0=10^12 rho^-2 epsilon^-2,
    ell=ceil(100u0), M=ell+1,
    t0=u0/j, tminus=3ell/(4j), tplus=7ell/(8j),
    eta²=zeta=epsilon/1024,
    D1=Lambda/2, D0=zeta D1, b=eta D0,
    j=b²/D0, gamma=rho j, a=2j.                (15)

Then eta<=1/32,zeta<=1/1024,delta=epsilon/512. The gap inequalities are

    ell-2u0>=ell/2, u0/(ell-2u0)<=1/50,
    tminus vmin-ell>ell/4,
    2ell-tplus vmax=ell/4,
    2ell+2-tplus vmax=ell/4+2.

They ensure every required early, boundary and late strict inequality, including t0vmin>2 and tplus vmax<2ell-2. From (3),(4),(14),

    H0<2, H1<=200/rho, H2<=3000/rho³,
    J0<=10eta, J1<=1700eta/rho.                (16)

For J1 use500eta/rho+1200eta<=1700eta/rho. The larger mediator map has been explicitly charged.

For (9), consecutive factorial-tail ratios are <=1/25 since M>=100u0. The factorial lower bound and e<3 give

    sum_(r=M)^infinity(4u0)^r/r!
      <=(25/24)(4eu0/M)^M<2*8^-M<=2/M².

Thus E_early<=(2+2/eta)/(5000u0)<=1/(50u0 sqrt(epsilon))<epsilon/16, because 2+2/eta<=66/sqrt(epsilon). This pays the changed b/j prefactor; simply importing a weak propagation ceiling would not suffice.

The unchanged normalized launch and right-tail calculation, with (14), gives

    2R0<=2epsilon²/10^12,
    2L0<=400epsilon/10^6,
    4sqrt(P)<=4sqrt(11)epsilon/256<epsilon/16,
    2d_right<=208epsilon/10^6.

Each is below epsilon/16, in particular delta_launch<1 before it is used. For the new early match, (16) and the gaps give

    T_G(t0,ell+1-2u0)+T_H(t0,ell+1-2u0)
       <=500/(rho sqrt(ell))<=500epsilon/10^7,
    m_early=M(t0,ell-2u0)<=3500eta/(rho ell).

The mediator numerator J1+2u0J0/q is at most1701eta/rho; division by q>=ell/2 gives the latter ceiling. At late time uminus/(tminus vmin-ell)<3, so

    m_L<=7100eta/(rho ell),
    d_L<=230epsilon/10^7,
    n_O<=230epsilon/10^7,
    d_S=18epsilon/1024.                        (17)

For the mediator, the numerator is at most1760eta/rho and q>ell/4. Both mediator ceilings are far below epsilon/64 because 1/(rho ell)<=rho epsilon²/10^14 and eta<=1. The scalar late-tail estimates follow directly from (6): q>ell/4, t/q<3/j for d_L and t/q<3.5/j for n_O, with G1<=100/rho and G0<2. Thus a common230/(rho sqrt(ell)) suffices.

Here d_S<2epsilon/64; unlike the two-port certificate it need not be belowepsilon/64. Together d_L,m_L<epsilon/64 imply d_packet<4epsilon/64<1/2. Hence d_O<=2n_O<1. The terms2d_L,2d_S,2m_L,2d_O are each belowepsilon/16: specifically2d_S=36epsilon/1024<epsilon/16 and2d_O<=920epsilon/10^7.

For the boundary, A_i<=4000/rho³. Since jtplus/qo(tplus)=7/2, (16) gives A_o<=H2+21H1+154H0<=8000/rho³. Moreover sqrt(3)d_hop/sqrt(2pi)<j, qi(t0)>=u0/2 and qo(tplus)=ell/4. Therefore

    E_outer<=8000/(rho³u0)+16000/(rho³ell)
       <=8160/(rho³u0)<(8200*256/10^12)epsilon<epsilon/16.

The twelve allowances are E_early;2R0;2L0;4sqrt(P);2d_right; early lead match;m_early;E_outer;2d_L;2d_S;2m_L;2d_O. Each is belowepsilon/16. Equations (11)-(13) consequently give a uniform isometry error below3epsilon/4<epsilon. This is a new conditional finite four-port statement, requiring its own check. For unhalved channel/trace tolerance epsilon, use epsilon/2 as the isometry accuracy argument; the usual channel bound is at most twice the isometry difference, with a common phase irrelevant to that bound but retained in (13).

## 7. Counts, cap and limits of the resource statement

There are20+4M=24+4ell physical qubits: four endpoints, four mediators, twelve controls and four sets of M additional radial heads. The combined positive block count is28+4M=32+4ell, since each final B replaces one Q_j bond. Auxiliary comparison sites are not physical resources. The physical graph is the explicit cubic nearest-neighbor embedding of60bc extended along its four disjoint rays.

Full-space incident sums are6b+6j at each core endpoint, D1+2b at each mediator,2j at each endpoint control,D1-2b at each mediator control,4j at ordinary lead interiors,5j at each emitter-adjacent site, and3j at each emitter. The final B has full norm3j: on the one-head block its diagonal is(j,2j) and off-diagonal -gamma, with maximum eigenvalue<=3j; its double-occupied energy is exactly3j. Thus adding its neighboring Q_j costs at most5j. These counts use combined projector and outer blocks; splitting them requires consistent recounting.

All incident sums are below Lambda for (15). In particular the endpoint sum is3Lambda zeta(eta+eta²), and the mediator sum isLambda(1/2+eta zeta). No legal-sector deletion of the inactive cell's positive load is used. Exact scales are

    D0=Lambda epsilon/2048,
    b=Lambda epsilon^(3/2)/65536,
    j=Lambda epsilon²/2097152,
    gamma=Lambda epsilon³/536870912,
    u0=10^12*256²*epsilon^-4,
    tplus=(7ell/8)*2097152/(Lambda epsilon²),
    tminus=(6/7)tplus.

The sufficient size and dimensionless durations are Theta(epsilon^-4), physical durations Theta(Lambda^-1 epsilon^-6). The relative window (tplus-tminus)/tminus is exactly1/6. Gamma is the smallest supplied positive scalar coefficient in this family: gamma<j, j-gamma>gamma, b>j, (D0-2b)>j, and the remaining coefficients exceed these. This is a coefficient magnitude, not a tolerance or precision guarantee. The constants and resource burden are very large; no optimality or practical gain is asserted. Four output-stage separation doubles ray resources relative to the two-port comparison; preserving its sufficient exponents does not make the architecture free.

No timed switching occurs. This device has reciprocal scattering and eventual finite-system returns remain possible. Separate O rays remove the previous same-lead inbound/outbound placement problem for a potential writer, but there is no writer here. This establishes neither a Record bit nor a faithful completion flag, capture/reset, permanent halt, old-processor transfer, native supplier or all-late-time result.

## 8. Pins, exposure and check gate

Paths are relative to the parent renewal directory. Complete source reads used here, with hashes checked:

* common_product_stage_separated_router/PROPOSAL.md —60bc91b6ad085a722b3805de1d1b0d93a9cabcf77b1c3f5a74e43045354c3182.
* common_product_stage_separated_router_check/REVIEW.md —8fcee7e6ee6579196141e8e67d5adbf9887969cbbbd3de3c7d00c9caf8777e5d; supports the core at its exact infinite-ray/packet scope.
* common_product_microscopic_finite_seed/PROPOSAL.md —452231afa993c7a14e1b55c0b302d499e0284ce02266f8a1039a75474053392a.
* common_product_microscopic_finite_seed_check/REVIEW.md —50148e56b0e38556f633cf225df82403b66d2e60c43f6391d355f84d6c4f2a51; qualifies the two-port launch/contact/finite-boundary proof architecture, not the new four-port constants or target.
* common_product_launch_derivative_bounds/PROPOSAL.md —378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8; exact normalized source derivative contract, also incorporated and checked at the preceding finite-source scope.

Earlier fully read premises reused at their pinned scopes are the literal cell739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088, original launchfb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4, and microscopic packetc105226ebeead1f87bb11c6afcc8dadac59520401d5f8c0fa6dba4ba3ef90e4e. The last packet supplies the analytical method, not an unverified numerical dimension transfer. Equations (2)-(4),(8),(12) explicitly reconstruct those changed interfaces.

ROOT proposed the task, derivative identity and candidate bounds. I authored the core and previous packet work. This is source-exposed author continuation using the inherited model/effort, not blind, model-diverse or independent validation. A distinct check must cover the joint-channel derivatives, full mediator norms, early actual/reference contact, source coordinate reversal, dimension-free boundary norm, complete target normalization, bound-state payment, twelve-term budget, physical scalar and counts. Only after that gate should this composition be integrated as checked bounded work; no retained/audit status is assigned here.

Only this proposal was created. No scientific executable, numerical simulation/integration, symbolic solver, sweep, upstream source edit, W/Git/PR/checkpoint/axiom/editable-prompt/model change or delegation occurred. Analytical estimates and file/hash bookkeeping constitute the evidence in this note.
