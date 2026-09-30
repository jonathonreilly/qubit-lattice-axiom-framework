# Sharp occupation readout has a linear energy price in the native pair model

**Status:** author mathematical candidate, conditional-support; focused independent check pending. No formal review, audit, premise promotion or physical Record identification.

**Result.** On the unchanged landed full-site qubit Hamiltonian, complete occupation dephasing has the sharp operator bound

    Delta(H0) >= c_read N,    c_read=min(mu,mu/3+2tau).             (1)

Consequently an input with small energy per particle requires a positive energy supply under this specified readout. A spatial version charges the energy already present near the measured region, using the actual positive Hamiltonian terms. These statements concern the supplied occupation instrument. They do not assign this price to every record, select an instrument from the axioms, or make its outputs permanent under H0.

The parent brief exposed candidate axial/plane coefficients. The derivation below was reconstructed directly from the actual pair words; it is author work, not an independent check. The author previously helped derive native thermodynamic bounds and record compatibility. Only the landed density-onset theorem is used for state/energy consequences. Open PR9413, threshold PR9401 and rotor/apparatus proposals are prior comparison, not mathematical premises.

## 1. Actual carrier, Hamiltonian and instrument

Let Lambda=(Z/LZ)^3, L>=5, V=L^3. Each site has its actual tensor factor C^2, with b_x=|0><1|, n_x=b_x^dagger b_x, N=sum_x n_x and empty vector Omega. Operators on different sites commute. No pair-boson substitution is made. The parameters mu,tau are arbitrary supplied positive numbers.

For axes e_i define

    d_i(x)=b_(x+e_i)b_(x-e_i),
    v_ij^(s,t)(x)=st b_(x+s e_i)b_(x+t e_j), i<j,
    Q_E1=(d_1-d_2)/sqrt2,
    Q_E2=(d_1+d_2-2d_3)/sqrt6,
    Q_Tij=(1/2)sum_(s,t=+/-1) v_ij^(s,t).

Let P_E=sum_(A=E1,E2) Q_A^dagger Q_A and P_T=sum_(i<j)Q_Tij^dagger Q_Tij. Write D for the eighteen displacements +/-2e_i and +/-e_i+/-e_j and m_x=sum_(d in D)n_(x+d). The actual Hamiltonian is

    H0=mu N-2mu sum_x P_E(x)-mu sum_x P_T(x)+V3+W,
    V3=mu sum_x n_x binom(m_x,2),
    W=tau sum_(x,k,A) |Q_A(x+e_k)-Q_A(x)|^2.                 (2)

Here |R|^2=R^dagger R. Its full-carrier positive decomposition, restated to fix every local term, is

    H0=S+mu Ddiag+W,
    S=(2mu/3)sum_x |d_1(x)+d_2(x)+d_3(x)|^2
      +(mu/4)sum_(x,i<j)sum_(r<s)|v_ij^r(x)-v_ij^s(x)|^2,
    Ddiag=sum_x n_x f(m_x),    f(m)=(m-1)(m-2)/2.           (3)

The identities sum_E Q_A^dagger Q_A=sum_i d_i^dagger d_i-|sum_i d_i|^2/3 and sum_(r<s)|v_r-v_s|^2=4sum_r|v_r|^2-|sum_r v_r|^2 give (3), because an axial pair occurs once and a plane pair twice. Indeed 2sum|d|^2+sum|v|^2=sum_x n_xm_x, and 1-m+binom(m,2)=f(m). Each summand in (3) is positive: f(m)>=0 for every integer m=0,...,18. The identity and positivity hold on the entire tensor product, not just on occupation vectors.

For every occupation configuration eta, let P_eta=|eta><eta|. Supply the joint occupation Lüders instrument I_eta(rho)=P_eta rho P_eta. Its outcome-averaged channel is

    Delta(rho)=sum_eta P_eta rho P_eta.                       (4)

The same expression acts on observables and is self-adjoint for the trace pairing. In particular Delta(N)=N, and all instantaneous occupation statistics are unchanged. Throughout, rho is an arbitrary density matrix; no sharp N, translation invariance or stationarity is assumed unless explicitly stated.

Equation (4) is also forced by any CP instrument with effects exactly P_eta and outputs supported in the same rank-one P_eta. If K_(eta,a) are its Kraus operators, the locked output implies K_(eta,a)=|eta><v_(eta,a)|. Its effect sum_a |v_(eta,a)><v_(eta,a)|=P_eta then gives I_eta(rho)=Tr(P_eta rho)P_eta=P_eta rho P_eta. This familiar rank-one normal form does not cover destructive measurement followed by a different re-preparation, unsharp effects or incomplete readout. For a proper subset of sites we use the Lüders instrument specifically; its output sectors are not rank one on the full carrier, so the same uniqueness assertion is unavailable.

## 2. Exact diagonal and sharp constant

Let E_a=sum_(unordered axial edges xy)n_xn_y and E_p=sum_(unordered plane edges xy)n_xn_y. Every occupied pair contributes one to the relevant count, independent of its other neighbors. Then

    Delta(H0)=mu Ddiag+w_a E_a+w_p E_p,
    w_a=2mu/3+4tau,    w_p=3mu/2+3tau.                       (5)

Here is the full diagonal calculation. For a pair annihilator B_e=b_xb_y, x!=y, an occupation vector eta is mapped to its configuration with e removed, or zero. Distinct unordered pairs produce orthogonal output vectors. Hence

    Delta(|sum_e a_e B_e|^2)=sum_e |a_e|^2 n_xn_y.           (6)

For the first part of S, each axial word has coefficient 2mu/3 and unique center. In a plane, each signed word occurs in three pair differences, giving 3mu/4 at each of its two centers, hence 3mu/2 per plane edge.

The sum of squared E-component coefficients of each d_i is 2/3; each plane word has squared coefficient1/4 in its T component. On summing the three positive-direction gradients over all centers, each same-center Q_A^dagger Q_A occurs six times. Thus W supplies axial weight6*(2/3)tau=4tau, and plane weight6*2*(1/4)tau=3tau. No gradient cross term has a diagonal: axial pairs have one center; the two centers of a plane pair differ by a diagonal displacement +/-e_i+/-e_j, never a nearest-neighbor displacement. Thus an identical pair cannot occur at both adjacent centers in the same Q component. These elementary center facts hold modulo L for every L>=5, including odd L. There is no global bipartite-parity assumption.

One can also compute directly in (2): Delta(P_E)=(2/3)E_a and Delta(P_T)=(1/2)E_p. This gives the equivalent identity

    Delta(H0)=mu N+V3+(4tau-4mu/3)E_a+(3tau-mu/2)E_p.       (7)

The coefficients in (7) can be negative; replacing them independently by positive terms would be incorrect. Equation (5) retains the full positive diagonal combination.

To prove (1), allocate half of each edge weight to each endpoint. For an occupied site with m=m_a+m_p neighbors, its allocated diagonal energy is

    mu f(m)+(w_a m_a+w_p m_p)/2.                            (8)

At m=0 it is mu. At m>=1 it is at least min(w_a,w_p)/2, since f(m)>=0. Thus the best candidate among these alternatives is min(mu,w_a/2,w_p/2). This equals c_read in (1). If tau<=mu/3, then w_p/2-w_a/2=5mu/12-tau/2>=mu/4, while c_read=w_a/2. If tau>=mu/3, both w_a/2 and w_p/2 are at least mu. Summing (8) proves the diagonal operator inequality, and hence every-state expectation version.

The constant is sharp, at every stated torus size: a single occupied site has Delta(H0)=mu and N=1; an isolated axial pair has Ddiag=0, E_a=1, E_p=0 and N=2, giving ratio w_a/2. No larger uniform constant can satisfy (1). Plane dimers do not improve it.

For a concrete coherent example, the normalized uniform E1 pair vector

    psi_E=V^(-1/2)sum_x Q_E1(x)^dagger Omega

has N=2 and H0 energy zero by (3). Every occupation configuration in its support is an axial edge, so its fully dephased energy is exactly w_a>0. The state and its dephased twin have the same full occupation distribution. This is both an energy discriminator and a warning: that distribution alone does not recover the initial coherent energy. It is not a new general pinching principle; prior repository occupation-pinching notes already establish that distinction for other Hamiltonians.

## 3. System energy injected by full readout

Define the expected injection, with H0 and its reference unchanged, by

    J_full(rho)=Tr[H0(Delta(rho)-rho)].

Writing E=Tr(H0rho), nbar=Tr(Nrho), (1) yields

    J_full(rho)>=c_read nbar-E.                             (9)

The same injection is obtained for H0-nu N, because the channel preserves N. Equation (9) is an energy difference, not an entropy bound. For an arbitrary input it need not be positive. A diagonal input is unchanged and has J_full=0. For any family with E/nbar tending to zero and nbar>0, it implies

    liminf J_full/nbar >=c_read.                            (10)

Neither existence of that family nor its physical preparation follows from (10). If the readout is followed by the supplied closed Hamiltonian evolution exp(-itH0), both H0 and N expectations remain constant because [H0,N]=0. For nbar>0 its dephased output therefore retains energy per particle at least c_read at every such later time. Closed evolution alone cannot restore a smaller energy-per-particle expectation; this is an energy statement, not permanence of the occupation record. The landed onset theorem gives actual controlled low-energy inputs without importing the open EOS, as follows.

Set A=10199347200(182mu+240tau), B0=3870720. The exact normalized full-carrier trial psi(u)=exp(-iuK)Omega, K=sum_x i(Q_E1(x)^dagger-Q_E1(x)), has at every finite L

    0<=E_u/V<=A u^4,
    |nbar_u/V-2u^2|<=B0 u^4.

Consequently

    J_full(psi(u))/V >=2c_read u^2-(A+c_read B0)u^4.         (11)

It is positive for 0<u^2<2c_read/(A+c_read B0), uniformly in volume. The particle density is then positive: this range lies within u^2<2/B0. In the limit u->0, E_u/nbar_u->0 uniformly in L. There is no requirement V u^2<<1 and no number-sector projection or bosonic trial.

For a ground-state density matrix of Hnu=H0-nu N, let E_g be its ground energy. The landed theorem gives

    nbar/V>=nu/(A+nu B0),    E_g/V<=-nu^2/(A+nu B0).

Since E=E_g+nu nbar, (9) gives

    J_full >=(c_read-nu)nbar-E_g.

For every 0<nu<=c_read, both landed inequalities can be inserted with their correct signs, yielding the positive extensive bound

    J_full/V >=c_read nu/(A+nu B0).                        (12)

This holds for every finite-volume ground-state density matrix, including degenerate mixtures. No differentiable equation of state, thermodynamic uniqueness or state polarization is assumed. For arbitrary nu>c_read this substitution is not valid because the coefficient of nbar changes sign; no extension of (12) is claimed.

The price in (9)-(12) is per particle or expected occupied outcome, not a positive constant per measured site. A complete readout reports V bits, most of which can be zero at low density. Neither n_x=1 nor a bit result is identified with occurrence of a framework Record.

## 4. Spatial readout with the actual boundary terms

Let B be any subset of the finite torus, and Delta_B the Lüders dephasing of all n_x with x in B, leaving the exterior factors otherwise untouched. Use nearest-neighbor torus graph distance and define

    B^-3={x: every site at distance<=3 from x belongs to B},
    B^+2={x: distance(x,B)<=2}.

An empty interior makes the bounds below weak but valid. No large-box hypothesis or infinite-volume limit is needed.

Index the individual positive summands in (3) by alpha: each singlet square, each of the six differences for each plane, each Q-gradient square, and each mu n_x f(m_x). Write them h_alpha>=0. Assign their center to x exactly as in (3), and let

    h_x^+=sum_(alpha based at x) h_alpha,    H0=sum_x h_x^+.

Every h_x^+ has support within the graph-distance ball of radius2 about x. In particular the diagonal term uses the actual eighteen neighbors; none is removed or reset. Define H_touch(B) as the sum of the individual h_alpha whose support meets B. Positivity gives

    0<=H_touch(B)<=sum_(x in B^+2) h_x^+.                  (13)

Let H_in(B) be the sum of the individual h_alpha wholly supported in B. Untouched terms cancel from Delta_B(H0)-H0. The images under Delta_B of all positive touched terms remain positive. Therefore

    Delta_B(H0)-H0 >=Delta_B(H_in(B))-H_touch(B).           (14)

The decisive exact boundary statement is

    Delta_B(H_in(B))>=c_read N_(B^-3).                    (15)

To prove it, first retain the actual diagonal summands mu n_x f(m_x) at every x in B^-3: their radius is2, so they are wholly inside. For any graph edge e={x,y} incident to such x, every S or W row contributing to its full diagonal coefficient in (5) is also inside B. An S row has a center at distance1 from x and endpoints at most2 from x. For a W row, one of its two adjacent centers is at distance1 from x; all endpoints of both stars are at most3 from x. The statement covers both centers of each plane pair, all relevant components, all gradient directions and both gradient appearances of that center. It uses individual complete rows, not the stronger demand that an entire centered family h_z^+ be contained in B.

All these rows dephase completely because their supports lie in B. Equation (6) makes their images nonnegative diagonal edge sums; they therefore supply the entire w_e for every edge incident to B^-3, as well as possibly other positive edge weights. Allocate half w_e to each endpoint in B^-3. An edge with one endpoint there is underused by a factor two; with two endpoints it is used exactly once. Combining this allocation with its actual Ddiag_x is exactly (8) at each interior site. This proves (15), without replacing any physical m_x, assuming monotonicity under edge deletion or introducing an independently minimized cell model.

Combining (13)-(15) gives the local operator inequality and its energy version

    Delta_B(H0)-H0 >=c_read N_(B^-3)-sum_(x in B^+2)h_x^+,
    J_B(rho)>=c_read <N_(B^-3)>_rho
                   -<sum_(x in B^+2)h_x^+>_rho.           (16)

The upper local energy debit is the energy actually present in the original state near B. It is not a putative modified-boundary Hamiltonian. If rho is translation invariant, with r=nbar/V and e=E/V, then

    J_B(rho)>=c_read r |B^-3|-e |B^+2|.                   (17)

For a cube of side ell with no wrap or overlap of its radius2 enlargement, |B^-3|=(ell-6)^3 for ell>=6 and |B^+2|<=(ell+4)^3. Thus, for ell>=7,

    J_B >=c_read r(ell-6)^3-e(ell+4)^3.                  (18)

The exact graph-distance enlargement is generally smaller than this enclosing cube. In particular (18) is a safe inequality, not an asserted volume identity. For any fixed such ell, (18) is positive for a sufficiently small energy-per-particle ratio e/r. The exact unitary trial above is translation invariant, so (11)'s inputs directly supply

    J_B(psi(u))>=2c_read |B^-3|u^2
                -[c_read B0 |B^-3|+A |B^+2|]u^4.        (19)

This can be a genuinely local readout in a much larger torus. Its positive leading cost is the occupied weight in the interior, not an assumption of uniform energy allocation for an inhomogeneous state. For such an inhomogeneous state, use the full expression (16).

Three steps are sufficient for this allocation proof. Two steps are insufficient to retain all the actual gradient coefficients: a gradient containing the pair {-2e_1,0} can also contain the pair {-3e_1,-e_1}. The literal control finds such rows explicitly. This does not prove that every possible two-step bound fails; it identifies the exact support requirement of this proof.

For B=Lambda, (16) reduces to (9). For B empty it reads zero>=zero. Partial readout followed by arbitrary exterior feedback is a different channel and is not covered by (16).

## 5. What is, and is not, supplied energy or work

Theorems (9) and (16) price the actual expected system-energy change at an unchanged Hamiltonian. They require no apparatus realization. To translate that change into an apparatus budget, supply a composite system plus apparatus, including controller, memory and any battery in the apparatus energy H_A. Let H_int denote their interaction energy, and W_ext the externally supplied work in the chosen process. The common-reference first-law ledger is

    W_ext=Delta E_system+Delta E_A+Delta E_int.             (20)

It follows that the system injection obeys

    W_ext-Delta E_A=J+Delta E_int.

If the interaction vanishes at both endpoints (or its expected change is explicitly zero), then W_ext-Delta E_A=J. For an autonomous energy-conserving implementation W_ext=0, so the apparatus loses energy J. If H_A>=0 and its initial expected energy is E_A,in, then E_A,in>=J whenever J>0. Insert (9), (11), (12) or (16) only with their stated input domains. If the endpoint interaction change is uncontrolled, no apparatus lower bound follows from system injection alone. Correlations do not remove (20); their interaction-energy contribution must be included when present.

This ledger is a necessary condition, not an existence theorem for exact sharp readout under a finite positive-energy apparatus. In particular no finite-dimensional controller, energy-conserving exact instrument, autonomous timing, state preparation or permanent memory is constructed. An externally controlled device may provide the injection as work, or a reservoir/battery may supply it; the system calculation alone does not identify that split. It is not Landauer erasure, a thermodynamic free-energy lower bound, or an entropy cost for writing each bit.

Occupation readout can also be altered to avoid this endpoint constraint: a destructive outcome measurement can re-prepare another state; different bases or coarse observables need not dephase these pair coherences; a separate record carrier may store information while changing the system less. Those routes require their own actual instruments and energy ledgers. They are not excluded. The preceding record-compatibility packet additionally shows that sharp full-carrier same-site permanence under this H0 is a separate obstruction; the present one-shot readout does not repair it.

The current axioms say that records form, lock an admissible possibility, persist and alone are readable. They do not choose the basis, H0, tensor state/expectation rule, Born-Lüders map, number-as-record dictionary, controller, energy reference or time. The three approved primitives keep their registered grants; none selects those missing objects. This is an optional-model compatibility result, not an axiom inconsistency or a physical source law.

## 6. Exact controls, source scope and open obligation

The standard-library Fraction runner imports no previous author assembly. Before execution, CONTRACT.md and CONTROL_FREEZE.json bound the expected identities and exact runner/wrapper bytes. One managed run passed with scientific CPU11.356853 seconds, scientific wall11.384672 seconds and peak RSS33,996,800 bytes; the supervisor recorded wall11.798171 seconds. The original30 CPU/90 wall/150 MiB envelope, one BLAS thread, original deadline and STOP sentinel were enforced. No failed scientific execution or runner repair occurred after the freeze.

Actual finite coverage:

- On L5 and L6, all literal S rows (2375 and4104), gradient rows (1875 and3240) and direct attraction diagonals agree at all1125 and1944 graph edges. Adjacent-center pair collisions are explicitly rejected; odd-torus parity is not used.
- Fifty deterministic occupation configurations check the direct original diagonal against the positive degree decomposition, including empty, monomer, axial dimer, plane dimer and full occupancy on both tori. This is not exhaustive full-state enumeration.
- The allocated degree inequality is checked in546 rational parameter/degree cases. Its all-mu,tau and all-state proof is (8), not this finite list.
- Literal infinite-lattice rows around the origin supply all18 incident edge weights inside its radius3 ball;110 relevant gradient rows extend beyond the radius2 ball. The output records an actual missed row. These are support controls, not a numerical verification of (16) for every density matrix.
- The L5 uniform E1 pair is tested against every actual S and W row, with norm250 before the 1/sqrt2 and 1/sqrtV normalization, and has N2, energy0 and dephased energy(2/3)mu+4tau. Equality of occupation distributions follows from the channel definition.

The general proof is independent of a volume expansion, a phase assumption, a wavepacket substitution or numerical diagonalization. The only external mathematical input used for the low-energy examples is the actual landed onset source at the exact identity listed in SOURCE_BINDINGS.json. Prior generic pinching and CP normal-form mechanisms are credited there; historical priority is not claimed. No literature theorem is imported.

The precise remaining physical obligation is to supply a law and preparation implementing a readable permanent record on the stated carrier, and to account for its actual system/apparatus endpoints. For the specific full occupation instrument on low-energy native matter, a proposed implementation must supply at least the energy in the proved conditional bounds. For alternative records no such universal price or obstruction is established. This is a decisive scoped tradeoff, not a proposal to replace the Hamiltonian or infer a phase.
