# Distinct check of the static product-reference SWAP

Disposition: SUPPORT at the stated standalone, supplied-reference finite-window scope. No required correction found. The full effective gate, exact comparison-trajectory residual, actual energy conservation, full-output phase, positive-block inventory and simultaneous window/cap prescription all check out. This is not a full path/record loader, a fixed-range construction, reference preparation or a retained audit.

Completely read `product_reference_static_swap/PROPOSAL.md`, SHA256 `1a9e0ee47c8cc5b4f874abb2c8fa47258ee00fbe3cf77a87a2c968b407f0a825`, including all changed arguments and scope statements. Paths here are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.

## 1. Exact four-dimensional comparison gate

The proposed Heff is symmetric under interchange Q,P. The antisymmetric singlet is annihilated by XQ+XP and ZQ+ZP; ZQZP is -1 on it. Its eigenvalue is therefore -c=-3lambda/4. This is a full state, not a classical input restriction.

To check the remaining three eigenvalues directly, use |00>, (|01>+|10>)/sqrt(2), |11>. The transverse matrix element from either end to the middle is sqrt(2)a=lambda. The diagonal elements of Heff are c+2b,-c,c-2b. After adding c and dividing by lambda, they become A=(3+sqrt(5))/2,0,B=(3-sqrt(5))/2. The resulting tridiagonal has unit off-diagonal entries, A+B=3 and AB=1. Expanding its determinant gives

    det(xI-M)=(x-A)x(x-B)-(x-A)-(x-B)
              =x^3-3x^2-x+3=(x-3)(x-1)(x+1).

Subtracting c gives eigenvalues -7lambda/4,lambda/4,9lambda/4 on the triplet. Thus ||Heff||=9lambda/4, after including the singlet as well. At tau=pi/lambda, all triplet phases are exp(-i pi/4): their differences are even integers times lambda. The singlet phase exp(+3i pi/4) is its negative. Consequently exp(-i tau Heff)=exp(-i pi/4) SWAP on the ENTIRE QP Hilbert space. It fixes00,11 and exchanges01,10 with the same phase. This is valid on arbitrary coherent QP input entangled with a passive reference.

The construction is a simultaneous Heff exponential; no separate implementation or ordering of its noncommuting terms is presumed. In particular this comparison generator is not itself asserted to conserve the active omega nP.

## 2. Actual Hamiltonian, positivity and scalar

Each single Pauli positive block has spectrum0,2 times its coefficient. The ZZ block has the same two eigenvalues, each with multiplicity two. The exchange on PB_j is zero on00,11 and is the Pauli X on span{01,10}; adding the identity gives eigenvalues0,1,1,2. Hence its scaled full-support norm is2g/N and it is real positive. The free occupations are positive with norm omega. This proves positivity on full supports rather than an excitation-sector compression.

Every installed block commutes with HE=omega(nP+sum nBj). Q is freely degenerate; ZP is diagonal; ZZ also preserves P occupation; the exchange conserves nP+nBj. Sharing P does not spoil this individual commutation. Thus [HE,HS+V]=0 even though the individual interactions in HS+V do not all commute. The identity shifts sum to

    s=a+2b+c+g=lambda(3/sqrt(2)+sqrt(5)/2+3/4),

which is exactly the scalar in the source. The decomposition e^{-itH}=e^{-ist} e^{-itHE} e^{-it(HS+V)} is consequently exact. No shift is dropped or counted twice. This ordinary-data/reference model does not impose the head-vacuum-annihilation rule of earlier head-clock constructions.

## 3. Complete residual, not a full-space approximation

Let S_X=sum X_Bj and S_Y=sum Y_Bj. The exact exchange identity gives V=g(XP S_X+YP S_Y)/(2N). On beta=|+>^N, S_X beta=N beta, while <beta,S_Y^2 beta>=N: each diagonal term is1 and every distinct-site term has zero expectation. Since g/2=a,

    (V-aXP)(psi tensor beta)
      =g/(2N) (YP psi) tensor S_Y beta,
    ||(V-aXP)(psi tensor beta)||=g/(2sqrt(N)) ||psi||.

The identity holds on arbitrary QP and passive-reference vectors because YP tensored with their identities is unitary. Thus it also holds after ANY amount of Heff evolution, regardless of its entangling QP action. The comparison trajectory retains beta in this interaction representation. Duhamel along precisely this trajectory, with the exact interacting propagator on the left of its integrand, proves g|t|/(2sqrt(N)). It neither asserts a small full-space operator norm nor assumes that the actual evolved reference stays product. The complete actual reference correlations are part of the paid norm error.

Multiplying by the exact free/scalar unitaries gives the source's comparator in the necessary order:

    e^{-ist} [e^{-it omega nP} e^{-itHeff} psi]
                          tensor beta(t).

HE does NOT commute with Heff. In particular it would be invalid to replace that ordered data product by a single exponential of their sum or to remove the free P factor at arbitrary times. Neither step is used in the proposal. The time-dependent reference beta(t) is supplied as a comparison profile, not reset during the actual evolution.

## 4. Revival and complete finite window

For lambda=omega/(2m), tau=2pi m/omega. All free energies are integer multiples of omega, so the entire free factor and reference rotation return to identity at tau. The exact effective gate therefore yields the source's literal center target

    exp[-i(s tau+pi/4)] SWAP psi tensor beta,

with error <=g tau/(2sqrt(N))=pi/sqrt(2N). This includes all reference outputs and arbitrary spectator entanglement; the common scalar has not been fitted to a state.

For t=tau+Delta>=0, factor the known free revival. The distance of e^{-it omega nP} from I is <=omega|Delta|. The distance of e^{-itHeff} from e^{-i tau Heff} is <=(9lambda/4)|Delta|. Applying the triangle inequality to their ordered product is sufficient and uses no false commutation. Keeping beta(t) and e^{-ist} exact gives equation(9).

The proposed w obeys

    w/tau=epsilon lambda/[32pi(omega+9lambda/4)]<1,

so the closed observation interval has positive times and t<=tau+w<2tau. From N>=ceil(512pi^2/epsilon^2),

    gt/(2sqrt(N)) < g tau/sqrt(N)
                  =sqrt(2)pi/sqrt(N)<=epsilon/16,
    (omega+9lambda/4)|Delta|<=epsilon/32.

Hence the complete isometry error is strictly below3epsilon/32 uniformly on the window. The twice-isometry estimate yields the unhalved stabilized complete-channel distance <3epsilon/16. At the center, pi/sqrt(2N)<=epsilon/32. These inequalities hold at both closed endpoints; the first is strict because w<tau. No postselection or success-conditioned normalization enters.

The relative width is exactly epsilon lambda/[16pi(omega+9lambda/4)], so it shrinks linearly in epsilon for fixed m. The target reference is beta(t), not a frozen beta across this interval; changing that comparison would introduce additional size-dependent error. The claim is an ordinary finite gate window, with no record event, autonomous capture or permanent retention.

## 5. Resources, active energy and scope

The N+2 qubits carry N exchange blocks, four other interaction blocks and N+1 free onsite blocks:2N+5 blocks. Their incident sums are exactly the displayed ones. P has load omega+lambda C with C=(sqrt(5)+3)/2+2sqrt(2). Q's coefficient is C-sqrt(2), while a reference qubit's additional coefficient is2sqrt(2)/N<C. Thus integer m>=max{1,ceil[omega C/(2(Lambda-omega))]} gives lambda C<=Lambda-omega and simultaneously bounds all vertices by Lambda. The hypothesis Lambda>omega is essential for this supplied positive-coupling prescription. This is a full-support load calculation including identity shifts, not a sector norm or canceled scalar.

At fixed omega and cap margin, m may be fixed independently of accuracy. The stated sufficient family then has N of order epsilon^{-2}, time2pi m/omega, an observation width of order epsilon, and pair coefficient g/N of order epsilon^2. These are consequences of the explicit prescription, not optimality, precision-tolerance or preparation-time results. The source correctly keeps the growing degree-N star at P and does not silently embed it in fixed-range hardware.

The actual total HE is conserved exactly, even though the desired SWAP can change P's energy because Q is degenerate. The compensating change resides in the actual reference and correlations. Complete-state closeness to beta at the revival is consistent with that compensation because the reference energy norm grows as N omega. It does not imply exact restoration of its energy moments or justify reuse without a new proof. The initial reference mean N omega/2, maximum N omega, and aligned product coherence are supplied resources. No cooling, phase preparation or coupling synthesis mechanism is established.

The source's arbitrary QP input is indeed treated, including the old P's passive-reference correlations, since the target is the full SWAP rather than a restricted transfer isometry. But no arbitrary active H_PE, path/record operation, head propagation or clock control has been included. This standalone component cannot inherit the earlier loader's all-output, early-record, range or finite-operation claims by analogy.

## 6. Exact exposure and work record

All changed source text was read completely. The motivational rotation source and its distinct check were also read completely and all three hashes were recomputed:

- `product_reference_two_body_rotation/PROPOSAL.md`: `9354342473198de039f429e55077b628db10c687aefc7eddfdd64b896f1f41fb`.
- `product_reference_two_body_rotation_check/REVIEW.md`: `0f5a7fc787a1f228316ad98179443fbeb62202fdd37f69f8bbd7493e69028e36`.
- New SWAP source: `1a9e0ee47c8cc5b4f874abb2c8fa47258ee00fbe3cf77a87a2c968b407f0a825`.

The SWAP proof was reconstructed above rather than inferred from the rotation check. ROOT authored the new source. My preliminary commensurate-spectrum pair-exchange idea inspired ROOT's search, and I had authored related timed/static gate proposals and earlier loader material. The source and design were visible during this review. This is a distinct source-exposed same-model calculation of the new SWAP composition, not blind replication or independent physical evidence for shared premises. My own static pair-exchange proposal is not needed as a mathematical premise here.

No numerical or symbolic solver, scientific executable, simulation, parameter search, external search or delegation was used. Work was complete reading, exact analytical reconstruction and deterministic hash/file bookkeeping. Only this REVIEW.md was created. No candidate source, W/Git/checkpoint/axiom/editable-prompt/model or publication/audit status was changed. The review supports the explicitly supplied static standalone gate and its finite complete-output error bound only.
