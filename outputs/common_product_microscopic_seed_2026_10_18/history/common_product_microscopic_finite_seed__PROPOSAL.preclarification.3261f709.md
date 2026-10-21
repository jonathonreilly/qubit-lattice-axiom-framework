# Finite endpoint seeds matched directly to microscopic packets

New authored conditional composition requiring a distinct check. The exact physical packet of source c105226e replaces the accumulated effective-cell comparison. An explicit early full-vector match pays all omitted spectral components, including bound states, before a fixed-diagonal outer-boundary comparison and final common-target normalization. No absence of bound states or global scattering completeness is assumed.

The scattering source59b59ea3 has a completed distinct check3e1dc925. The packet sourcec105226e was fully read and hash-verified, but its distinct check was pending at assignment. All conclusions below remain conditional on that packet premise and require their own composition check. ROOT suggested the contact-residual route and candidate parameters; the common-space operators, bounds, normalization and simultaneous family are derived below, not accepted from the suggestion.

## 1. Fixed physical device and exact packet premise

Use exactly the finite positive physical Hamiltonian H_phys of composition3a195efc: the six-qubit program cell, two rays n=0,...,M, emitters at M, ordinary target sites0,...,ell with ell=M-1, and outer blocks

    B_r=Q_gamma(M-1,M)+(j-gamma)n_(M-1)+(2j-gamma)n_M.

Here j=b^2/D0, a0=2j, D1>D0>2b, eta=b/D0<=1/8, 0<zeta=D0/D1<1/2, 0<rho=gamma/j<1. All physical terms, absent interactions, local roles, coefficient correlations and input conditions remain those of the source. No new physical term is installed. The input E_seed xi has one head at emitter M in its encoded path, legal program |ppp>, and all other heads vacant; arbitrary encoded input and passive-reference entanglement are supplied. Only basis program/path inputs are sitewise products.

Write h_F^mic=H_phys-2bI on the one-head domain. The exact infinite microscopic packet source uses h^mic, obtained by replacing the finite emitter ends with uniform infinite leads while retaining the physical mediator. Its normalized packet is

    Psi_n(t)=(2pi)^(-1/2) integral g(k){
       exp(i[(ell-n)k-tE])xi
       +exp(i[(n+ell+1)k-tE])Q(k)xi} dk,
    Psi_m(t)=(2pi)^(-1/2) integral
                      exp(i[ell k-tE])R(k)g(k)xi dk,       (1)
    E(k)=2j(1-cos k).

The source proves exact strong evolution and ||Psi(t)||=1, as an isometry in xi, by remote-past separation. It does not claim completeness. Use its precise controlled Q,R and bounds, on [pi/3,2pi/3]:

    delta=eta^2+zeta,
    ||Q||=1, ||Q'||<=260delta, ||Q''||<=4600delta,
    ||Q-C||<=d_S=max(13eta^2,5zeta),
    ||R||<=3eta, ||R'||<=420eta,
    C=P0 tensor X+P1 tensor I.                         (2)

Let g be the positively normalized cutoff launch spectrum of fb72f4ed, G_r=||g^(r)||_1. Define

    H0=G0, H1=G1+260delta G0,
    H2=G2+520delta G1+4600delta G0,
    J0=3eta G0, J1=3eta G1+420eta G0.

For amplitude L1 bounds A0,A1 and q>0, use the packet source's envelopes

    T_A(t,q)=[A1+(2j|t|/q)A0]/sqrt(2pi)
                                      *sqrt(q^-2+q^-1),
    M_med(t,q)=[J1/q+2j|t|J0/q^2]/sqrt(2pi).          (3)

T_G and T_H denote the G0,G1 and H0,H1 versions. Every phase in (1), including the scattering +1 and the later common scalar exp(-i2bt), is retained.

## 2. Early comparison for the actual microscopic finite seed

Use a common auxiliary space with two integer-coordinate port lines and the physical mediator. Extend h_F^mic by independent Dirichlet half-lines n<=-1 and n>=M+1, each retaining diagonal2j. Define h_ref as two disjoint standalone launchers, with emitter n=M, lead coordinate x=ell-n>=0, and the same decoupled positive exterior n>=M+1. Give its decoupled mediator the SAME legal-program diagonal D_p as h_F^mic. Both generators are bounded and self-adjoint, although their norms can depend on D_p. Add the common scalar2b equally if writing physical rather than relative evolution.

The difference V=h_F,ext^mic-h_ref is supported at n=0,-1 and mediator. In each port it has endpoint diagonal change a_p-j (equal to +j enabled, -j disabled) and removed reference hopping represented by +j Adj(0,-1). It also has the actual mediator couplings -b(|L,0>+|R,0>)<m| and adjoint. There is no change of mediator diagonal and no endpoint-to-endpoint effective bond. Thus

    ||V||<=2j+sqrt(2)b.                            (4)

Indeed the two port contact blocks [[a_p-j,j],[j,0]] have norm at most2j and form orthogonal copies; the mediator coupling has norm sqrt(2)b. This is a deliberately sufficient combined norm, not an assertion of equality.

The reference evolution of an emitter seed has ZERO mediator amplitude at every time. Its invariant source/lead subspace has norm bound4j, regardless of D_p. If P_contact projects onto n=0,-1 in both ports and m, the reference powers on the seed obey

    P_contact h_ref^r E_seed=0 for r<M,
    ||P_contact exp(-it h_ref)E_seed||
               <=sum_(r=M)^infinity (4jt)^r/r!, t>=0.

Reaching n=0 requires M nearest-neighbor steps. Diagonal factors cannot shorten that distance. The isolated mediator powers vanish on the reference seed, so no factor D_p is inserted into this Taylor bound. Since V=V P_contact, ordered Duhamel and unitarity of the ACTUAL full generator imply

    E_early^mic=min{2,u0(2+sqrt(2)/eta)
                      sum_(r=M)^infinity(4u0)^r/r!},
    ||e^{-it0 h_F^mic}E_seed-log xi
           -e^{-it0 h_ref}E_seed-log xi||<=E_early^mic,
    u0=jt0.                                       (5)

The notation E_seed-log here is only the one-head seed without the common scalar; its physical program encoding is the same on both sides. The expression in the norm means the difference of the two evolved seed vectors. The large actual generator norm is never used as a4j bound. The physical scalar cancels in this comparison only because it is common and restored later.

## 3. Matching the emitted packet with the exact microscopic packet

The standalone checked launch gives error2delta_launch at t0 to the positively normalized outgoing reference packet, with source vacant. The cutoff chi, exact raw amplitudes g_+,g_-, p=||chi g_+||_2^2 and g=chi g_+/sqrt(p) are the unchanged source quantities. Its error is

    delta_launch=sqrt[R0^2+(L0+2sqrt(P))^2],
    R0=min{1,2j/(pi gamma^2t0)},
    L0=B_minus/sqrt(2pi)*sqrt[(t0vmin)^-2+(t0vmin)^-1],
    B_minus=||(chi g_-)'||_1+(2j/vmin)||chi g_-||_1,

with P the checked exterior spectral probability ceiling and delta_launch<1 required.

The source reversal x=ell-n identifies that normalized reference packet exactly with the normalized projection n<=ell of the full-integer incoming Fourier state A_full(t0) with phase (ell-n)k-t0E. Its omitted right tail costs at most2d_right, where

    d_right=T_G(t0,1+t0vmin).

This identification retains exp(ik ell), source spectral phase and positive normalization. It is the same exact Fourier step as in3a195efc; it does not assume a physical packet was prepared by hand.

Require ell-t0vmax>0. The new microscopic early comparison from packet equation11 is

    e_match={T_G(t0,ell+1-t0vmax)^2
             +T_H(t0,ell+1-t0vmax)^2
             +M_med(t0,ell-t0vmax)^2}^(1/2).      (6)

The three terms occupy negative radial, nonnegative radial and mediator coordinate sectors respectively. In particular the mediator term is present and uses its stronger gap. Therefore the ACTUAL finite state at t0 satisfies

    ||e^{-it0 h_F^mic}E_seed-log xi-Psi(t0)||<=e0^mic,
    e0^mic=E_early^mic+2delta_launch+2d_right+e_match. (7)

The auxiliary negative-coordinate states were used only to establish this distance; both vectors in (7) have zero negative-coordinate support. All actual emitter/mediator amplitudes and any spectral components not represented by (1) are charged. No bound-state seed weight is set to zero. For example any spectral projection orthogonal to this exact packet family has norm on the compared state at most the full error in (7), when that projection is applied to the corresponding infinite extension; no separate spectral completeness assertion is needed for the vector inequality.

## 4. Finite boundary evolution and normalized common output

On the physical microscopic infinite operator, add precisely

    Delta=(j-gamma)Adj(ell,ell+1)+j Adj(ell+1,ell+2)

on both ports, and zero on the mediator. Then h^mic+Delta is the actual finite h_F^mic direct-summed with exterior Dirichlet half-lines. It leaves all diagonals unchanged, including2j at the two outer contact/cut sites. Its contact norm is d_hop=sqrt((j-gamma)^2+j^2). The central microscopic cell is not changed or approximated.

For t0vmin>2 and tplus vmax<2ell-2, use packet equation14 with incoming G and outgoing H. Explicitly set qi(t)=tvmin-1, qo(t)=2ell-tvmax, and

    A_i=G2+(12j/vmin)G1+(4j/vmin+48j^2/vmin^2)G0,
    A_o=H2+(6jtplus/qo(tplus))H1
             +(2jtplus/qo(tplus)+12j^2tplus^2/qo(tplus)^2)H0,
    E_outer=sqrt(3)d_hop/sqrt(2pi){
      (A_i/vmin)[1/qi(t0)-1/qi(tplus)]
      +(A_o/vmax)[1/qo(tplus)-1/qo(t0)]}.          (8)

The nonnegative twice-IBP integrals or their increasing endpoint bounds show this controls every duration from t0 through t in[tminus,tplus]. All Q derivatives are paid through H1,H2; the ideal g-only outgoing bound is not reused. Delta has no mediator column, so it requires no extra mediator residual. Ordered Duhamel with the exact Psi(t) gives

    ||e^{-it h_F^mic}E_seed-log xi-Psi(t)||
                  <=e0^mic+E_outer.              (9)

Assume tminus vmin>ell and define uniform late allowances

    d_L=T_G(tminus,tminus vmin-ell),
    m_L=M_med(tminus,tminus vmin-ell),
    d_packet=d_L+d_S+m_L,
    n_O=T_G(tplus,2ell+2-tplus vmax),
    d_O=n_O/(1-d_packet).

Require d_packet<1 and d_O<1. The late T_G and M_med terms decrease with t: besides the increasing gap, t/(tvmin-ell) and t/(tvmin-ell)^2 decrease. The outgoing unnormalized tail increases, so the separate endpoint bounds are legitimate. No monotonicity of the quotient is needed.

Define the COMMON scalar sequence and normalized finite target by

    B_n(t)=(2pi)^(-1/2) integral
                      exp(i[(n+ell+1)k-tE])g(k)dk,
    beta_F(t)=P_(0<=n<=ell)B(t)/||P_(0<=n<=ell)B(t)||.

Packet equation12, using its exact normalization and scattering bound, proves that this denominator is positive throughout the window and that the packet-to-target cost is <=2d_packet+2d_O. Thus the complete finite physical comparison is

    sup_(tminus<=t<=tplus)
    ||e^{-itH_phys}E_seed
          -e^{-i2bt}J_out(beta_F(t) tensor C)||
       <=min{2,e0^mic+E_outer+2d_packet+2d_O}.     (10)

All input/reference dimensions are covered by the isometry norm. The target has both emitters and mediator vacant, unchanged legal programs and a common packet; actual output is never postselected, normalized or traced away. No effective-cell Duhamel term accumulating over tplus is added or silently assumed zero: that comparison has been replaced by exact physical packet evolution and an explicitly bounded initial match. The physical common scalar remains in (10).

## 5. One simultaneous sufficient family

Use the same fixed quintic cutoff as refined family79f5bd9c: plateau sigma=pi/24, transition width pi/12 ending at pi/8, with conservative sigma'=pi/6. Thus vmin=sqrt(3)j, vmax=2j, and the checked derivative bounds give

    G0<2, G1<=100rho^-1, G2<=2000rho^-3,
    B_minus<=200rho^-1, P<=11rho^2, p>1/2.

For any 0<epsilon<=1 choose

    rho=epsilon/256,
    u0=10^12rho^-2epsilon^-2,
    ell=ceil(100u0), M=ell+1,
    t0=u0/j, tminus=3ell/(4j), tplus=7ell/(8j),
    eta^2=epsilon/1024, eta>0,
    zeta=epsilon/1024,
    D1=Lambda/2, D0=zeta D1, b=eta D0,
    j=b^2/D0, gamma=rho j, a0=2j.                (11)

Then eta<=1/32, zeta<=1/1024 and delta=epsilon/512. All scattering/packet coefficient hypotheses hold. The geometric gaps satisfy

    ell-2u0>=ell/2, u0/(ell-2u0)<=1/50,
    tminus vmin-ell>ell/4,
    2ell-tplus vmax=ell/4,
    2ell+2-tplus vmax=ell/4+2,

as well as t0vmin>2, tminus>t0 and tplus vmax<2ell-2. These are the required microscopic mediator gap as well as the prior lead gaps.

From (2), with delta<=1/512,

    H0<2, H1<=200rho^-1, H2<=3000rho^-3,
    J0<=6eta, J1<=1140eta/rho.                    (12)

For example H2<=2000rho^-3+(520/512)100rho^-1+(9200/512), which is below3000rho^-3. Thus the microscopic outgoing coefficients do not acquire an inverse power of eta or time.

### Early actual/reference error with its large prefactor

The sum in (5) must not be replaced by the old loose3/M estimate before paying u0/eta. Since M>=100u0, consecutive tail ratios are <=1/25. The elementary factorial bound and e<3 give

    sum_(r=M)^infinity(4u0)^r/r!
          <=(25/24)(4eu0/M)^M <2*8^-M <=2/M^2.

The last inequality follows from8^M>=M^2 for positive integers M (induction suffices). Consequently

    E_early^mic <=(2+sqrt(2)/eta)/(5000u0)
           <=1/(100u0 sqrt(epsilon))<epsilon/16. (13)

Here 2+sqrt(2)/eta=2+32sqrt(2)/sqrt(epsilon)<50/sqrt(epsilon). This is an explicit payment of the microscopic contact strength b/j=1/eta. The mediator's large diagonal never entered the reference propagation estimate.

### Launch, early matching and late normalization

As in the checked refined family,

    2R0<=2epsilon^2/10^12,
    2L0<=400epsilon/10^6,
    4sqrt(P)<=4sqrt(11)epsilon/256<epsilon/16,
    2d_right<=208epsilon/10^6.

Each displayed term is below epsilon/16, so delta_launch<1 follows before its use. For the changed early match (6), bound its square root by the sum of lead and mediator norms. Using (12) and the early gaps gives

    T_G(t0,ell+1-2u0)+T_H(t0,ell+1-2u0)
                   <=500rho^-1/sqrt(ell)
                   <=500epsilon/10^7<epsilon/16,
    m_early=M_med(t0,ell-2u0)
                   <=2300eta/(rho ell)<epsilon/16. (14)

The single-coordinate mediator bound uses 1/sqrt(2pi)<1 and
J1+(2u0/q)J0 <=1141eta/rho, with q>=ell/2. At late times the corresponding bound is

    m_L<=5000eta/(rho ell),
    d_L<=230epsilon/10^7,
    n_O<=230epsilon/10^7,
    d_S=13epsilon/1024.                          (15)

Indeed uminus/(tminus vmin-ell)<3 gives the mediator numerator <=1176eta/rho, then divide by a gap greater than ell/4. The parameter choices imply 1/(rho ell)<=rho epsilon^2/10^14. Since eta<=1, the mediator terms in (14),(15) are below epsilon/64 even under this loose ceiling, and 2m_L<epsilon/16.

Both d_L and d_S are below epsilon/64, so d_packet<3epsilon/64<1/2. Therefore d_O<=2n_O<1 and

    2d_L<=460epsilon/10^7<epsilon/16,
    2d_S=26epsilon/1024<epsilon/16,
    2d_O<=920epsilon/10^7<epsilon/16.             (16)

These verify all complete-target normalization assumptions. They pay the order-eta mediator coefficient using its finite-time oscillatory integral, rather than treating that coefficient as a population or discarding it.

### Changed microscopic outer boundary and total

In (8), A_i<=4000rho^-3 as before. The actual outgoing coefficients (12) instead give

    A_o<=H2+21H1+154H0<=8000rho^-3.

The common prefactor sqrt(3)d_hop/sqrt(2pi)<j, qi(t0)>=u0/2 and qo(tplus)=ell/4 imply

    E_outer<=8000rho^-3/u0+16000rho^-3/ell
           <=8160rho^-3/u0
           <(8200*256/10^12)epsilon<epsilon/16.  (17)

There are exactly twelve nonnegative allowances in this sufficient budget:

    E_early^mic; 2R0; 2L0; 4sqrt(P); 2d_right;
    early lead match; m_early; E_outer;
    2d_L; 2d_S; 2m_L; 2d_O.

Each is below epsilon/16. Thus (10) gives a complete uniform isometry error below3epsilon/4<epsilon. The unhalved channel/trace bound is below2epsilon; replace the accuracy argument by epsilon/2 for channel tolerance epsilon, without changing the exponents. This candidate quantitative conclusion is conditional on the pinned microscopic packet premise and still needs a distinct combined check.

## 6. Physical cap, exact scale and comparison limits

The supplied parameters in (11) give exactly

    D0=Lambda epsilon/2048,
    b=Lambda epsilon^(3/2)/65536,
    j=Lambda epsilon^2/2097152,
    gamma=Lambda epsilon^3/536870912,
    u0=10^12*256^2*epsilon^-4,
    ell=ceil(100u0),
    tplus=(7ell/8)*2097152/(Lambda epsilon^2),
    tminus=(6/7)tplus.                           (18)

The previously checked incident sums remain D1+2b, 3b+4j at central endpoints, program2j and D1-2b, lead interior4j, emitter-adjacent5j and emitter3j, under the same combined-block convention. With eta<=1/32 and zeta<=1/1024 all are strictly below Lambda. D1>D0>2b, 0<gamma<j and exact a0=2j are satisfied. The number of qubits is8+2ell and combined positive blocks9+2ell; no auxiliary comparison sites are physical resources.

For fixed Lambda and decreasing epsilon, (18) yields size and dimensionless observation times Theta(epsilon^-4), physical observation times Theta(Lambda^-1 epsilon^-6), and smallest supplied positive scalar coefficient gamma=Theta(Lambda epsilon^3). The latter is the smallest by the same direct comparisons gamma<j, j-gamma>gamma, b/j=1/eta>1, and (D0-2b)/j=(1-2eta)/eta^2>1. It is a magnitude of an EXACT coefficient, not an allowed precision error, minimal eigenvalue or a cost for physically supplying it.

This may be compared to the separately checked refined family's sufficient Theta(epsilon^-14) physical duration at the same induced isometry accuracy convention, relative window width1/6, architecture and incident cap. The comparison concerns two parameter families and proofs, not a fixed-device measured speedup, optimal exponents or practical performance. The constants in u0 and ell remain extremely large. No timing mixture or coefficient-tolerance theorem is imported here.

## 7. Exact sources and verification status

New complete reads and hash checks:

* common_product_microscopic_scattering/PROPOSAL.md — 59b59ea3fc51e6ae364716a63ff4b9e001390cba112f48f0b4214c01318865a6.
* common_product_microscopic_scattering_check/REVIEW.md — 3e1dc92540af46ec3a20b928001c7796795bf6c6a6b8580fe307c3e3ca3f8eb6; supports the exact scattering source at its stated column/spectrum scope.
* common_product_microscopic_packet/PROPOSAL.md — c105226ebeead1f87bb11c6afcc8dadac59520401d5f8c0fa6dba4ba3ef90e4e; distinct check pending at assignment. Its exact evolution, normalized packet and derivative/tail bounds are provisional premises of this note.

Previously fully read/authored exact sources reused at their identified revisions:

* finite composition3a195efcf8d5196ed54a74228033d0888e7f18c864e481ce61b2efea6c67992b and its check5f5b1727a31df17facb9232e902c1d6985cd175058d66e54862ae614fef148a9.
* original launchfb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4 and derivative378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8, with their checks recorded in refined family79f5bd9c07fe0eb0f37d051446f69759a32559ba7ce9e8bb835db01287188bb3.

ROOT proposed the actual contact comparison and candidate time-independent detuning ratios. I reconstructed the early extension/residual, its factorial payment, microscopic packet match, final target and all twelve simultaneous allocations. Component checks do not independently validate this composition. Required distinct-check points include the actual contact operator, reference invariant subspace despite D_p, all coordinate/phase conventions, mediator tails, changed outgoing derivatives, uniform final normalization, bound-state qualification and physical scale exponents.

The physical Hamiltonian, roles, absent interactions, coefficient correlations, occupation basis, legal program/input preparation and any native identification remain supplied. This is not an old literal processor result, native law, capture/reset, permanent halt, all-late output or practical resource claim. The target is a coherent moving packet on a finite observation interval.

Only common_product_microscopic_finite_seed/PROPOSAL.md was created. No scientific executable, numerical simulation, integration, symbolic solver, sweep, upstream source edit, canonical/W/Git/PR/checkpoint/editable-prompt/model change or delegation occurred. No retained status or independent acceptance is assigned.
