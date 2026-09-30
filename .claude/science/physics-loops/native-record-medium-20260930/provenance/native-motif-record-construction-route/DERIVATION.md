# Local motif permanence with a finite-time quantum medium

Root author candidate. No independent check, formal review, audit, law selection or axiom adoption is implied. This is a new supplied law on the exact native M2 tensor carrier. It changes H0. A motif is a proposed one-content record implementation, not the axiom's unique meaning or the original rotor record instrument.

## 1. Literal definitions and local modification

Use the actual native H0 of current-main NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md, SHA7180c065165cb5db45f3405fcc9711ec38145a3d2391962ed767d55f4cc25ee0. On a cubic torus with L>=18 let b_x=|0><1|, n_x=b_x* b_x, N=sum n_x. The parameters mu,tau,gamma are positive, and 0<nu<mu/3. Let B_r(x) denote the coordinate cube of radius r in the torus metric, and v=|B_2|=125. Supply

    P_x=n_x product_(y in B_2(x),y!=x)(1-n_y),
    Q_x=product_(y in B_2(x))(1-n_y),
    J_x=sqrt(gamma) b_x* product_(y in B_2(x),y!=x)(1-n_y).       (1)

P_x marks an isolated occupied center with an empty radius-two collar. Its content is the fixed occupation |1> at x. This is a finite-block presence encoding; n_x=1 alone does not identify a formed record. Its basis/content choice and readout identification are supplied. Blank or mobile occupations are not declared readable records.

All P_x commute. Define their simultaneous pinching on the finite torus by composing

    E_x(A)=P_x A P_x+(1-P_x)A(1-P_x),  E=product_x E_x.

The order is immaterial. Define a NEW Hamiltonian and a NEW formation law

    H'_0=E(H0),  H'_nu=H'_0-nu N,
    L(rho)=-i[H'_nu,rho]+sum_x D[J_x](rho).                     (2)

E is a mathematical definition of Hamiltonian coefficients. It is not an actual measurement, extra grade observation, added site factor or intermediate physical operation. The jumps in (1) are the observed site labels of this new model. They are not substituted for any original compensated rotor jump.

The whole local law is translation and proper-cubic covariant. No record sublattice or distinguished position appears in it. The internal basis, motif radius, quantum tensor realization, expectation/Born rule, clock and parameters are nevertheless additional choices; no nearest-neighbor admissibility distribution or complete framework realization is derived.

The landed source groups H0=sum_x h_x, supp h_x subset B_2(x), ||h_x||<=J=182mu+240tau. A projector P_y disjoint from supp h_x commutes with h_x. Since all the pinches commute, its action remains irrelevant after applying the other pinches. Only y in B_4(x) can act, and their supports lie in B_6(x). Thus h'_x=E(h_x) has support in B_6(x) and norm at most J. Equation(2) is uniformly finite range, despite using a convenient global formula for E. L>=18 suffices for these support/count upper bounds without creating distinct-site assumptions across a seam.

E is positive, unital, and fixes every function of N and every diagonal occupation operator. Consequently the actual landed inequalities pass unchanged:

    H'_0>=0,  H'_0>=c N(N-2)/V,
    c=min(tau,mu/12)/99090432,  V=L^3.                         (3)

Also [H'_nu,N]=[H'_nu,P_x]=0. These are full-carrier identities.

The completion H0=S+mu Ddiag+Wtau in the source gives a useful record debit. Ddiag=(1/2)sum_x n_x(m_x-1)(m_x-2), with m_x the eighteen-neighbor pair-graph occupation. Each summand is nonnegative; on P_x, m_x=0 and that summand equals1. Therefore Ddiag>=M:=sum_x P_x, and

    H'_0>=mu M,  H'_nu>=mu M-nu N.                            (4)

No record energy has been subtracted or hidden in a changed energy zero.

## 2. Full-state persistence and exact formation balances

If x=y, P_x J_x=J_x, J_x P_x=0 and J_x*J_x=gamma Q_x. If 0<dist_infinity(x,y)<=2, both P_y J_x and J_x P_y vanish: a jump whose empty collar contains an existing occupied y is blocked, and its output occupied x is incompatible with P_y's empty collar. If dist_infinity(x,y)>2, the offdiagonal factor at x is outside supp P_y and all remaining factors are diagonal, so J_x commutes with P_y. These statements include overlapping empty collars.

Every jump preserves each already formed marker. The no-event generator -iH'_nu-(gamma/2)sum_x Q_x commutes with every P_y. Hence every range P_y is invariant under the full quantum semigroup, including arbitrary input correlations and mixtures. Along the usual finite-volume quantum-jump realization, marker patterns can only gain the jump's site. There is at most one such event at each site, and total rate is at most gamma V, so no finite-volume explosion occurs. An all-blank start is not asserted to generate the prepared quantum medium below.

The adjoint generator obeys the exact operator identities

    L*(P_x)=gamma Q_x,
    L*(M)=L*(N)=gamma sum_x Q_x,
    L*(N-M)=0.                                                (5)

Thus the number of non-motif particles is conserved in expectation and, from a simultaneous definite N/M input, along each trajectory. This does not prove that they remain mobile or in a phase. Because the Q_x are all-empty projectors, the elementary union bound on each occupation word gives

    sum_x Q_x >= V-v N,  0<=sum_x Q_x<=V.                      (6)

The lower bound may be negative at high density, where it says nothing useful. It is an operator inequality since all its terms are diagonal.

## 3. Explicit quantum preparation with no markers

Choose integer ell>=10 large enough that

    3 pi^2 tau/(ell+1)^2 <= nu.

Set D=ell+8, and require L to be a positive multiple of D. Partition the torus into D-cubes. Inside each choose center cube {1,...,ell}^3, with coordinates relative to that cell. On this center cube take the normalized Dirichlet sine function

    f(x)=[2/(ell+1)]^(3/2) product_(i=1,2,3) sin(pi x_i/(ell+1)),

and extend it by zero. In each cell prepare

    phi_f=sum_x f(x) Q_E1(x)* Omega,
    Q_E1(x)=(b_(x+e1)b_(x-e1)-b_(x+e2)b_(x-e2))/sqrt(2).

Its physical occupied support lies in {0,...,ell+1}^3. The opposite axial pairs have unique centers and are mutually distinct at L>=5. Therefore ||phi_f||=1, N phi_f=2 phi_f, and Q_A(y)phi_f=delta_(A,E1)f(y)Omega. The source's D0 singlet and all plane-difference squares kill it; each configuration is a pair-graph edge so Ddiag also kills it. Thus its exact isolated energy is

    <phi_f,H0 phi_f>=tau sum_(x,i)|f(x+e_i)-f(x)|^2
                   =12tau sin^2(pi/[2(ell+1)]) <=nu.           (7)

This is an exact qubit two-particle calculation, not a bosonic replacement or numerical spectral estimate.

Tensor these states over the disjoint cells, with every remaining site empty, obtaining Phi_L. Neighboring occupied supports are separated by at least seven lattice spacings. H0 has interaction diameter at most four; no interaction term meets two occupied supports. Every local term vanishes in the empty product, so the expectation is exactly the sum of the isolated packet expectations. The particle density is exactly rho0=2/D^3.

Every occupied particle in every basis configuration has its pair partner at coordinate distance at most two. Consequently P_x Phi_L=0 for every x. The entire state lies in the zero-marker block of E, whence <H'_0>=<H0>. With eta=nu/D^3,

    <Phi_L,H'_nu Phi_L>/V <=-eta<0,
    <M>_0=0,  <N>_0/V=2/D^3 <=1/(2v).                        (8)

The last bound follows from D>=18. No global small-particle-number approximation is used: Phi_L has 2V/D^3 actual qubits occupied. Averaging its density matrix over all torus translations gives a translation-invariant preparation with exactly the same bounds and no markers. Proper-cubic averaging is also possible. This averaging is a supplied preparation, not a typicality or realized-state assertion.

## 4. Actual positive-time coexistence, with energy cost retained

Evolve that literal initial density matrix by(2); no trajectory conditioning or postselection is used. From(5)-(6),

    <N>_t/V <=rho0+gamma t,
    d<M>_t/dt >=gamma[V-v<N>_t].                              (9)

For 0<=t<=1/(4v gamma), rho0<=1/(2v) gives

    gamma t/4 <= <M>_t/V <=gamma t.                           (10)

For the energy set h'_(nu,x)=h'_x-nu n_x, with norm at most J+nu and support B_6(x). D[J_y]*h'_(nu,x) vanishes when dist_infinity(x,y)>8; at most17^3=4913 jump centers can contribute per x. Each individual dissipator norm is at most2gamma||h'_(nu,x)||. The Hamiltonian part cancels in L*(H'_nu). Therefore, defining C=9826(J+nu),

    |d<H'_nu>_t/dt|/V <=gamma C.                              (11)

This includes complete gain and loss; it is not a per-click energy formula or an energy-conserving reservoir model. Fix the positive volume-independent time

    T_*=min(1/(4v gamma), eta/(2gamma C)).                      (12)

For every 0<t<=T_* the actual evolving state satisfies

    <M>_t/V >=gamma t/4>0,
    <H'_nu>_t/V <=-eta/2<0.                                   (13)

Existing and newly created motif records remain permanent for all later times, even though the negative-energy estimate is asserted only on this interval. There is no promise of a stationary birth flux or indefinitely sustained negative-energy medium. Equation(4) explicitly charges record creation and is consistent with the finite-time restriction.

## 5. Why this is a quantum-medium witness, and its precise limits

There is a simple coherence discriminator that needs no phase assumption. On a classical occupation word, the diagonal of S_E gives2mu/3 per axial pair edge, while the diagonal of S_T gives3mu/2 per plane pair edge. Since Wtau is positive its diagonal is nonnegative. Thus, writing m for each occupied site's pair degree,

    <word,H0 word> >=mu sum_x n_x[(m_x-1)(m_x-2)/2+m_x/3]
                    >=(mu/3)N(word).                          (14)

For integer m=0,...,18 the bracket has minimum1/3 at m=1 (m=0 gives1, m=2 gives2/3, m>=3 gives at least2). Pinching leaves all occupation-basis diagonal entries unchanged. Every occupation-diagonal state consequently has <H'_nu>>=(mu/3-nu)<N>>=0. The strictly negative expectation in(13) proves that the actual evolving state retains occupation coherences. It does not establish entanglement, a thermodynamic phase, ODLRO, a sound pole, homogeneous susceptibility or a gravitational mode.

The construction supplies an extensive permanent one-content motif density at actual positive times together with an extensive quantum low-energy witness on the same M2 factors. It preserves positivity/coercivity but changes native transport near motifs. No claim is made that H'_0 has the original H0 kernel, equation of state, scattering, spectrum or record incompatibility theorem. The earlier full-carrier obstruction for unchanged H0 remains true. Here P_x is a finite-block presence projector, not the common rank-one site projector n_x on the whole carrier.

Open physical obligations: select/derive this changed law or another law; relate motif presence and the fixed local content to the actual admissibility/readout rule; supply meaningful multiple contents and a physical preparation; include an apparatus/source conserving physical energy; identify a physical clock; prove longer-time/thermodynamic collective behavior and any coupling to gravity. The nearest-neighbor admissibility distribution and content variation are not supplied by(1). This is a conditional feasibility result for an optional mechanism, not a completed framework realization or evidence of axiom inconsistency.
