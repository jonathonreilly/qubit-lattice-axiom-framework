# Vacuum-preserving local errors without head-number conservation

New bounded author derivation requiring a distinct check. The same length-independent finite-time robustness bound survives removal of head-number conservation from the perturbed local blocks, provided their local head-vacuum action remains a scalar on every program/record fiber. The key estimate is rectangular: it bounds the perturbation applied to nominal one-head inputs, with outputs in the full many-head Hilbert space. Duhamel then propagates those outputs with the actual full unitary. No invariant one-head sector is assumed for the perturbed device, and all resulting multi-head leakage is paid in the complete-output error.

ROOT proposed the weighted input/output support factorization. The proof below reconstructs it, checks the actual supports, and corrects a degenerate proposed example before giving a nontrivial positive real replacement. Frozen f9e427 and321867 are unchanged. This is source-exposed author continuation, not independent checking, a native-law claim or an unrestricted error theorem.

## 1. Admissible local class and the changed obligation

The nominal H=sum_l h_l is the same finite one-control record device76b5, with164+4ell listed positive blocks on126+4ell qubits. Its head number is conserved. Keep exactly the listed onsite/two-qubit supports and their combined-source/combined-mediator conventions. For each nominal block write

    h_l=c_l I+A_l, w_l=||h_l||,

where c_l=b for each of eight core vacancies, c_l=(sqrt(2)-1)j for each of eight writer junction vacancies, and c_l=0 otherwise. A_l=-c_l n_v for a vacancy and A_l=h_l otherwise. Every A_l annihilates local head vacuum for every local program/record fiber state.

For0<=delta<=1/2, permit any static self-adjoint replacement

    h'_l=c'_l I+A'_l                                      (1)

on the same listed support, subject to:

1. h'_l is positive on the FULL local Hilbert space.
2. A'_l annihilates the entire local head-vacuum subspace, for every program/record state on that support.
3. c'_l=0 if c_l=0; otherwise c'_l is real and |c'_l-c_l|<=delta c_l.
4. ||A'_l-A_l||<=delta w_l on the FULL local support.

There is NO condition that h'_l conserve head number, P or X_R. Positivity and the vacuum condition remain independent admissibility requirements, not consequences of a small matrix-norm difference. Replacements may differ arbitrarily across blocks within this class; there is no probabilistic independence or cancellation assumption.

The scalar decomposition gives on the full finite physical Hilbert space

    H=cI+K, H'=c'I+K',
    c=8b+8(sqrt(2)-1)j, c'=sum_l c'_l,
    Delta c=c'-c, |Delta c|<=delta c,
    E_l=A'_l-A_l, Delta K=K'-K=sum_l E_l.                (2)

Each E_l is self-adjoint, has norm at most delta w_l, and annihilates local head vacuum. Both global head-vacuum restrictions remain scalar on the full P/R fiber. But H' can map a one-head state into sectors with more heads. Consequently the self-adjoint quadratic-form argument on an invariant perturbed one-head space from f9e427 cannot simply be reused. The following rectangular estimate supplies the missing step.

## 2. Input and output projections on the full space

Let the full finite head Hilbert space have occupation basis |Z>, where Z is a subset of its head sites. Tensor the unrestricted fiber F=C²_P tensor C²_R and any passive reference. Let Pi_1 project onto |Z|=1. Define S_l to be the HEAD sites in the support of block l, excluding P and R. Every actual listed block has one or two head sites; there is no fiber-only block.

On this full space define

    Pi_l^in=sum_(v in S_l)|{v}><{v}| tensor I_F,
    Q_l^out=sum_(empty != Z subset S_l)|Z><Z| tensor I_F. (3)

The basis vectors in Q_l^out have every head OUTSIDE S_l vacant. Thus Q_l^out is not merely the projector onto an occupied local region while allowing other heads elsewhere. It selects configurations supported entirely inside S_l. This distinction is essential to the output multiplicity bound below.

For one-head input outside S_l, the local heads are vacant, so E_l annihilates it. Thus E_l Pi_1=E_l Pi_l^in. For one-head input inside S_l, all outside heads are vacant and the local operator cannot change them. Since E_l is self-adjoint and annihilates local head vacuum, its range is orthogonal to that local vacuum: for any local-vacuum vector v, <v,E_l psi>=<E_l v,psi>=0. It can therefore output only a NONEMPTY head configuration inside S_l. Program/record states may change freely. These facts establish exactly

    E_l Pi_1 = Q_l^out E_l Pi_l^in.                       (4)

No head-number conservation is used in this argument. On an actual two-head-site bond the possible output is one or two heads; on a head/program or head/record contact it remains one head but can rotate the fiber. Later actual evolution can generate further heads on other supports; equation(4) bounds only the instantaneous perturbation acting on the nominal one-head state, as needed by Duhamel.

## 3. Weighted row/column factorization

Define the nominal maximum head incident norm sum

    L_head=max_(head v) sum_(l:v in S_l)w_l.              (5)

The input projection sum satisfies

    sum_l w_l Pi_l^in <= L_head Pi_1.                   (6)

For the output sum, all Q_l^out are diagonal in the same head-occupation basis and identity on the fiber. Its eigenvalue at the empty configuration is0. For a nonempty configuration Z it is

    sum_(l: Z subset S_l) w_l.

Choose ANY v in Z. Every such block also contains v, so this sum is at most sum_(l:v in S_l)w_l<=L_head. Therefore on the FULL head/fiber space,

    sum_l w_l Q_l^out <= L_head I.                       (7)

For configurations with more than two heads, the actual supports give eigenvalue0, but no extra factor from the two-head configurations is needed. The bound is not based on the total number of P/R contacts or on the dimension of their fiber.

For completeness write an explicit factorization through a direct sum of copies of the full physical Hilbert space. Blocks have w_l>0; any zero block can be omitted. Define

    B psi=(sqrt(w_l) Pi_l^in psi)_l,
    D=direct_sum_l (E_l/w_l),
    A(x_l)_l=sum_l sqrt(w_l) Q_l^out x_l.

Then B*B=sum_l w_l Pi_l^in, AA*=sum_l w_l Q_l^out, and ||D||<=delta. Equations(4), (6), (7) imply

    A D B=sum_l Q_l^out E_l Pi_l^in=Delta K Pi_1,
    ||Delta K Pi_1||<=||A||||D||||B||<=delta L_head.      (8)

This is a rectangular norm from one-head inputs to unrestricted outputs. It does NOT assert ||Delta K||<=delta L_head on the whole many-head space. It requires neither mutual commutation of E_l nor conservation of the fiber axes. All identities tensor with an arbitrary passive reference without changing the bounds. Since Delta K also annihilates global head vacuum, the same estimate extends to vacuum-plus-one-head inputs, but no extensive-input theorem is claimed.

For the nominal inventory, full block norms are2|a| for head bonds, their coefficients for onsite terms/vacancies, D1-2b for mediator/program blocks,2j for terminal/record contacts and3j for a combined source. Nominal head incident sums are D1+2b at mediators,6b+4j at core endpoints, at most(4+sqrt(2))j at writer heads and at most5j elsewhere. With eta<=1/8,zeta<1/2, j=eta b<=b/8 and D1>16b, the mediator dominates. Thus

    L_head=D1+2b.                                       (9)

The shared-P load4(D1-2b) and shared-R load8j remain necessary for the separate all-qubit cap, but neither supplies an extra occupancy factor in(8). The full fiber norm of each such contact has already been included in w_l.

## 4. Duhamel uses nominal invariance only

The nominal K conserves head number, so exp(-isK)Pi_1 stays in the one-head subspace. The perturbed K' is a self-adjoint finite matrix on the FULL physical space. For t>=0, the exact identity is

    [exp(-itK')-exp(-itK)]Pi_1
       =-i integral_0^t exp(-i(t-s)K') Delta K
                                      exp(-isK)Pi_1 ds.

The left propagator has norm1 on the full space; it is not replaced by a one-head compression. Insert Pi_1 after Delta K on the right because the nominal right trajectory stays there. Equation(8) therefore gives, also for negative t,

    ||[exp(-itK')-exp(-itK)]Pi_1||
                        <=min{2,delta L_head |t|}.       (10)

Full perturbed dynamics can populate any head sector and is still paid by(10). No bound on the full many-head norm of H' is substituted for this unitary argument, and no spectral completeness or absence of bound states is assumed.

With true scalars restored,

    ||[exp(-itH')-exp(-it Delta c)exp(-itH)]Pi_1||
                        <=min{2,delta L_head |t|},       (11)

while the FIXED nominal phase obeys

    ||[exp(-itH')-exp(-itH)]Pi_1||
      <=min{2,delta L_head |t|+2|sin(Delta c t/2)|}
      <=min{2,delta(L_head+c)|t|}.                       (12)

The norm2 caps compare two isometries from the one-head input domain. No phase fitting is performed. A density-channel comparison can ignore the common scalar because it cancels, but relative program/record errors remain paid. In addition,

    ||(I-Pi_1)exp(-itH')Pi_1||
                         <=min{1,delta L_head |t|}.      (13)

Indeed the corresponding nominal evolution, including any scalar rephasing, is entirely one-head. Thus multi-head leakage has an explicit norm and probability bound. Global head vacuum itself is a reducing subspace for H' by self-adjointness and the scalar-vacuum condition, so starting from one head cannot reach zero heads; no conservation of the positive head number beyond that is inferred.

## 5. A nontrivial real positive number-changing local block

The suggested rotation of Q_j's positive one-head eigenvector with|11> does NOT produce a counterexample to number conservation: those two vectors both have energy2j. Any orthogonal rotation entirely inside that degenerate eigenspace leaves Q_j unchanged. That failed example is preserved here rather than presented as evidence of a larger class.

A working example instead uses

    S=(|10>+|01>)/sqrt(2), A=(|10>-|01>)/sqrt(2),
    D=|11>, V=|00>.

The nominal positive bond is Q_j=2j|A><A|+2j|D><D|, with S and V zero modes. Put D_s=cos(s)D-sin(s)S and define

    h'_bond=2j|A><A|+2j|D_s><D_s|.                       (14)

This is a real positive two-qubit matrix with eigenvalues0,0,2j,2j and the same support. It annihilates V exactly; c'=c=0. The difference of the two rank-one projectors onto D_s and D has norm|sin s|, hence

    ||h'_bond-Q_j||=2j|sin s|<=2j|s|.

For |s|<=delta this meets the full-support norm condition because ||Q_j||=2j. For0<|s|<=delta<=1/2, its S/D off-diagonal element is-2j sin(s)cos(s), which is nonzero. It genuinely mixes one and two local heads and fails to commute with head number. This is not a formal relabeling of degenerate eigenvectors.

For example evolution of input S under this single block alone develops D amplitude proportional to sin(s)cos(s)[exp(-i2jt)-1], showing the number-changing effect directly. The phase/sign of that proportionality is not needed for the norm certificate. Equation(14) may replace an ordinary two-head bond in the apparatus as one admissible error while all other blocks stay nominal. Later dynamics need not preserve the span of S,D; the full-space proof(10) already handles it.

The example is an allowed supplied positive local matrix in the stated perturbation class. It does not derive that matrix from a narrower native interaction inventory or claim physical production. No complex coefficient or enlarged support is required. Vacuum-creating errors, such as mixing V with a positive mode, would fail condition2 and are not covered by this extension.

## 6. Cap, finite-window output and absolute branch

The full-space norm and scalar assumptions imply

    ||h'_l||<=w_l+delta w_l+|c'_l-c_l|
                          <=(1+2delta)w_l.              (15)

The one-control nominal choice D1=Lambda/8 has maximum incident sum over ALL physical qubits strictly below Lambda/2. Therefore delta<=1/2 gives a perturbed full-support incident cap strictly below Lambda. This uses positivity as a separate admissibility premise and does not count only one-head expectation values.

For eta<=1/8,zeta<1/2 the same nominal parameters satisfy

    L_head+c=D1+10b+8(sqrt(2)-1)j
        <[(25+sqrt(2))/128]Lambda<Lambda/4.             (16)

Choose desired0<epsilon<=1 and instantiate the checked nominal one-control logarithmic family at tau=epsilon/2. In particular h=eta²=zeta=tau/10^5, D1=Lambda/8, j=Lambda tau²/(8*10^10), rho=alpha tau sqrt(h), with alpha and all source/budget constants calculated by the pinned nominal prescription. Let its certified horizon and final window be

    T=7ell/(8j), t_minus=3ell/(4j),
    delta_safe=min{1/2,epsilon/(Lambda T)}.              (17)

For any replacements in the declared class with delta<=delta_safe, (16) gives delta(L_head+c)T<epsilon/4. Keep the SAME supplied seed E, whose range lies in Pi_1: one path head over the two I emitters, ordinary program P, blank R and all other heads vacant, with arbitrary joint program/path/reference input.

Keep the exact normalized nominal target

    T_nom(t)=exp(-ict)J_F[beta_F(t) tensor C tensor|1>_R],

on[t_minus,T]. It has exactly one head on retained F sites1..ell, every other head vacant, program retained coherently and the prescribed controlled path action C. Its nominal error is<3epsilon/16. Combining with (12) yields on the FULL physical output space

    sup_(t_minus<=t<=T)||exp(-itH')E-T_nom(t)||
                           <7epsilon/16<epsilon/2.      (18)

All zero-/one-/many-head sectors, erroneous program/record amplitudes and internal/source outputs are included. Only the comparator has vacant apparatus. Actual and target maps are isometries, giving unhalved complete output-channel discrepancy<7epsilon/8<epsilon with passive references.

On the ENTIRE horizon[0,T] retain the SAME unnormalized nominal target

    V_nom(t)=exp(-ict)J_F[B_fin(t) tensor C tensor|1>_R],
    B_n(t)=(-i)/sqrt(2pi) integral
                  exp(i[n+ell+57]k-itE_nom(k))g(k)dk,
    B_fin=P_(1<=n<=ell) B.

The nominal branch error is<epsilon/4. Contracting (12) by the mathematical P_R1 proves

    sup_(0<=t<=T)||P_R1 exp(-itH')E-V_nom(t)||
                                    <epsilon/2.         (19)

No conservation or commutation of P_R1, P or X_R is used. In particular actual record1 with multiple heads is part of the discrepancy. Both maps are contractions, so the unhalved subnormalized-channel/diamond error is<epsilon. No early target switch, phase fitting or normalized rare-success guarantee is introduced.

To state final success unambiguously beyond the one-head sector, define

    Pi_good=P_R1 tensor
           sum_(v on F0/F1,1<=n(v)<=ell)|{v}><{v}|
           tensor I_P,

with the identity also on the passive reference and the natural factor ordering. This projector requires EXACTLY ONE total head, located on retained F, and all other heads vacant. The normalized target lies in its range. Orthogonality and(18) give

    Prob(Pi_good)>1-(7epsilon/16)²,
    Prob(R=1)>1-(7epsilon/16)²                          (20)

throughout the final window. A weaker statement allowing several heads somewhere on F is not silently substituted. The complete map bound also supplies logical accuracy; the probability alone does not.

Throughout[0,T], equation(13) separately bounds the probability of leaving the one-head sector by (delta L_head T)²<(epsilon/4)². This leakage estimate is included in, not added to, the complete errors above. No claim of exact head-number conservation for H' has reappeared.

## 7. Quantitative meaning and limits

The nominal checked logarithmic family at tau=epsilon/2 has ell=Theta(epsilon^(-11/2)) and T=Theta(Lambda^-1 epsilon^(-15/2)). Equation(17) therefore gives the same sufficient admissible local-matrix tolerance delta_safe=Theta(epsilon^(17/2)). There is no extra length factor in (8), even though the physical horizon itself grows with length. Constants and coefficient magnitudes remain supplied and can be large or small; this is not optimality, a fabrication-cost model or a practical error budget.

This extension removes head-number conservation from the allowed perturbations, not the local vacuum-annihilation requirement. Errors that create a head from local vacuum can act at many initially empty locations, and neither the input support identity nor the output projection factorization above then follows. Their behavior is outside this theorem; no general impossibility or halt conclusion is claimed. Nonscalar vacuum fiber drives, new supports, nonpositive replacements and input-state errors are likewise outside the declared class.

The nominal Hamiltonian and seed continue to be supplied. The perturbation class admits real positive local matrices beyond the exact original block forms; admitting those as possible physical errors is an explicit apparatus assumption, not a derived native interaction or an edit to physical axioms. Record/readout, initialization, coefficient-production, old literal processor transfer, permanent halt, irreversible capture/reset and guarantees past the finite horizon remain open.

## 8. Frozen sources, exposure and independent-check target

N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. Precursor sources, fully authored/read in the immediately preceding coherent tasks and hash-refreshed unchanged here:

- common_product_local_matrix_robustness/PROPOSAL.md:f9e427ccd5ec0a25f0c28639f9707728489a7a7dcca139e6f9fe03289d9b8a20. Its distinct check remains a separate task; no completed acceptance was supplied for this derivation.
- common_product_single_control_robustness/PROPOSAL.md:3218676f11bbc39ecfcf3c84a568a2ffc8107a7b303f349195394a338b2b0623.

The exact nominal source and scope remain76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01, with distinct review549bf5e4862f9ad384fddaca6b6e73ae6c4da74c397b981c93a2d16473b418d0. The logarithmic recipe is7160387f62fdb71afadd3e30a37bf93d9dd566c9bfd9a3739177331bb68254a8, with reviewd1787938d55970246d222b91df1824c165bf16b58924cd7f5f3936a6d5cc16b3. Their integrated common_product_single_control_publication/NOTE.md is02b43286a352594910b14e3dcbc2a5181d86f1ad806d1585c547f67138567cde, hash-refreshed unchanged. Complete prior reads and scoped component evidence are reused; the integrated note is not another independent check.

ROOT supplied the rectangular Q_l/Pi_l route and proposed a local rotation example. The author independently reconstructed the factorization after exposure, found the positive-mode/11 rotation degenerate, and replaced it by(14), retaining the failed attempt explicitly. The decisive new check should reconstruct (4), (7), (8) on the FULL output space with arbitrary P/R fibers, verify that the actual unitary in Duhamel is unrestricted, and test(14) for positivity, vacuum action, full-support norm and genuine number change. It should then check the exact-one-F-head projector and inherited nominal-phase budget. A proof that only compresses H' to one head would not validate this result.

Only common_product_vacuum_preserving_robustness/PROPOSAL.md was created. No frozen source, W/Git/checkpoint/axiom/editable-prompt/model change, scientific executable, numerical solver/simulation/sweep, publication or delegation occurred. Verification is exposed author algebra and file/hash bookkeeping. Distinct review is required and no retained status is assigned.
