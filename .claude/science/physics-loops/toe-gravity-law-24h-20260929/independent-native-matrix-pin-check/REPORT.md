# Focused independent check of the native internal matrix-pin lower bound

No material mathematical error was found in the complete WORKING_PROOF.md at SHA25656920870a2e2a29900c8a6a0365ca1764b2ef0450b89433b87a0a4ca4b631c1c. The finite-cell matrix Green comparison, physical all-state extraction, ordered dilute lower coefficient and strict improvement hold for the supplied Hamiltonian at their stated scope. This is a focused analytic check, not formal review/audit, source-law selection, a full-threshold equation of state or a phase result.

The principal checked new conclusion is

    liminf_(rho down0) liminf_(L to infinity) <H0>/(L^3 rho^2)
      >=c_pin/4,
    c_pin=lambda_min[U* G(0)^(-1)U]>a/g,
    G(0)=integral K(k)^(-1)dk/(2pi)^3,
    a=min(tau,mu/12).

The inner bound is uniform over full-carrier states with the stated MEAN density, with volume taken first. K is the actual nine-forward-bond S+W amplitude form and U its normalized five constant soft vectors. The result is a relaxed one-pair pin capacity; it does not assert the actual many-pair energy equals this coefficient or the full15-channel T0 coefficient.

## Independence and byte identities

PRE.md was frozen at2026-09-30T10:20:46.589558UTC, SHA256b5d5a1549a543cf6f97ea31c333b8d7fa0ceb34e2384944a9091802110128046, before opening any of the new author CONTRACT, TARGET_EXTENSION or WORKING_PROOF. The brief had disclosed the target improvement, nine-forward-bond family and the need to check matrix capacity, physical boundary/counting and ordered limits. It had not disclosed the logarithmic L6 cutoff proof.

Before PRE, the actual landed native source was read completely from main30a9461ee19a49b99fa6628fe942f08e504e8903, SHA7180c065165cb5db45f3405fcc9711ec38145a3d2391962ed767d55f4cc25ee0. The complete earlier native Neumann REPORTa837bb64fe72a88a8913fa9c5f181f516a4ec45dc91733bbeb9e27d3d789ca6c and focused receipt67b6b7e55d5cc835099755dcf12fe58d9b7b70896c30c79378ff5a716ccfd6dd were also read. Selected methodology remains7146fe17a76de41badcaca3c3c7cac6d11eb2a00; the continuous campaign's unchanged exact procedure/primitive closure is reused. No open proposal on another law is a premise.

My PRE independently reconstructs the complete symbol and an explicit strict infinite-pin margin, then names the unsolved finite-cell Green UPPER comparison, first-order high-channel boundary issue, physical extraction and limit order as the checks needed. It does not presume that an infinite symbol improvement solves the finite-cell theorem.

The new author files were first opened at10:21:03.836765UTC and read in full:

- CONTRACT.md:06385d33e1be099b0b389875c8396bc04a5ddbb5ffc784254a8f7c177d2bb09e.
- TARGET_EXTENSION.md:4c06d881c697c1a8775aa3dbe4035497adab90e41f017b449d964a71f33a74d3.
- WORKING_PROOF.md:56920870a2e2a29900c8a6a0365ca1764b2ef0450b89433b87a0a4ca4b631c1c.

After the analytic comparison, the complete author runner08f8ea1c024069b689729970cb90e97ba56e3f4a4808f355e426ea993dfb6cf0, its control freeze, output and execution record were read. They were neither imported nor executed. No new numerical computation was required by this check.

A mechanical metadata attempt initially looked for the landed native note in the campaign working checkout, where that newer main file is absent. It was corrected to the exact git-show bytes already read. PRE remained unchanged, and no new author proof was opened during that repair. This is preserved in PRE_FREEZE.json; the working checkout is not misidentified as current main.

## Actual symbol, positive row comparison and normalization

For each full occupation residual eta, f_(eta,d)(x)=<eta|b_x b_(x+d)|psi> retains the complete output and the same physical input state. Summing its literal S/W row squares over eta gives exactly<S+W>. Splitting those positive forms into1-epsilon and epsilon parts, selecting complete rows in disjoint anchor cubes, and using S+W>=a Egrad_9 on the epsilon part produces the stated lower comparison. It never requires disjoint physical Hilbert factors for the cubes; a bond may extend outside its anchor cube. The nonmonotone physical Ddiag is not replaced by a deleted-neighbor version.

I independently derived the Fourier rows before reading the proof. Axial d_i(k)=exp(-ik_i)f_i gives

    K_ax=2mu P_v+tau l(I-P_v), P_v=v* v/3.

For a plane, the two signed centered occurrences of forward type eta=+/-1 give
q_eta=-eta[exp(-i eta k_j)+exp(-ik_i)]/2. Hence

    K_ij=2mu I+(tau l-mu)q* q,
    ||q||²=1+cos(k_i)cos(k_j).

Both blocks and their displayed eigenvalues match the author. The axial E vectors have norm one. Each plane soft vector is(-1,+1)/sqrt2 in the FORWARD-bond basis; this accounts for the two centered appearances rather than silently importing a unit triplet Gram. The actual infinite form satisfies a l I<=K<=b I, b=2mu+24tau. Thus K_e=(1-epsilon)K+epsilon a l I lies between(1-epsilon)K and K and still dominates a l I.

The previously checked regularized complete-row cell has exactly the five constant U modes and gap at least epsilon a/(14ell²). Their actual proof applies without modification: the epsilon gradients force a zero vector to be componentwise constant, and an interior S cell then imposes the four complementary constraints. These are auxiliary amplitude-form facts, not a physical many-particle cell spectrum or a claim that independent removal fibers can all be attained by one state.

## The finite-cell L6 estimate

The scalar/vector zero-mean Neumann Sobolev inequality is valid uniformly in ell. Reflect a cube field into a fixed larger cube and cut it off on scale ell. Its infinite-lattice gradient is bounded by C(||grad q||_2+ell^-1||q||_2); the mean-zero Neumann Poincare inequality controls the second term. The discrete Sobolev estimate follows from the telescoping-coordinate BV/Loomis-Whitney argument, then applying the BV inequality to |q|^4. Its L^(3/2) norm is ||q||_6^4, and the edge differences are bounded by C(|q_x|³+|q_y|³)|Dq|. Cauchy gives ||q||_6^4<=C||q||_6³||grad q||_2. Using the vector norm makes this valid for all nine complex components.

For f orthogonal to constant U, its spatial mean m lies in U-perp. The complete interior S rows give exactly

    ell³|m|²<=27 S_inner(f)/mu+54||q||².

The left side follows from S_inner(m)=2mu(ell-2)³|m|². The q contribution is bounded by the actual infinite S norm2mu after zero extension. Multiplying by ell^-2 converts this estimate to the L6 norm of the constant m, while Poincare controls q. Since the cell form contains(1-epsilon)S_inner and epsilon a times the gradients, the resulting ||f||_6<=C_e E(f)^(1/2) is uniform in ell for FIXED epsilon,mu,tau. There is no hidden positive many-body gap or volume factor in this step.

On the infinite lattice, the energy completion also embeds into L6 because K_e>=a Delta. One- or two-point evaluation functionals are continuous. Their Riesz solutions are therefore legitimate finite-energy fields, even though the zero-energy inverse is not generally an l2 operator. The integrable three-dimensional inverse symbol gives the same Green compression. No finite-volume inverse is substituted for an unproved infinite l2 resolvent.

## Matrix Green upper and lower comparison

The crucial cutoff argument is sound and avoids the earlier unresolved pointwise-residual estimate. For an interior point, a logarithmic cutoff between radii w^(1/4) and w^(1/2) has cubed gradient sum O((log w)^(-2)). Two such cutoffs can be combined by eta=1-(1-eta1)(1-eta2); their support volume remains O(w^(3/2)) and their gradient L3 norm is O((log w)^(-2/3)), uniformly in the separation of the points.

For a finite-range literal row R, the commutator with eta is bounded by local differences of eta times the field. Finite overlap and Holder give

    sum_R ||[R,eta]f||²
       <=C||grad eta||_3²||f||_6².

Every row touching the cutoff is a true interior row for large w. The main row vector eta(x_R)Rf costs at most the original energy. Taking the norm triangle inequality and then squaring gives E(eta f)<=(1+s_w)E(f), s_w=C_e(log w)^(-2/3). The first-order soft/high mixing is INCLUDED in this row commutator. It is not divided by the ell^-2 cell gap. This is why the method fixes the exact obstacle recorded in the previous Neumann report.

The variational direction was checked explicitly. For f=K_cell^+r on the mean-soft complement, E(f)=<r,f>=q_L. The cutoff equals one at the sources, so the infinite source pairing is still q_L. Optimizing a scalar multiple of eta f in the infinite variational principle gives q_inf>=q_L/(1+s_w), hence the required finite Green UPPER bound. A mere trial Green function giving the opposite inequality would not have sufficed; that error is absent.

In the reverse direction, cut the infinite Riesz field and project it off the finite constant-U kernel. Projection changes no finite energy. Its pairing error is bounded by

    C||r|| ell^-3||eta f||_1
      <=C||r|| ell^-3 w^(5/4)||f||_6
      <=C w^(-7/4)||r||².

The exponents are correct: support volume w^(3/2), Holder exponent5/6, and ell>=w. For q_inf above this error, the optimized finite value is at least(q_inf-error)^2/[(1+s_w)q_inf]. For q_inf below it, q_L>=0 gives the needed lower estimate directly. The finite and infinite point functionals are uniformly bounded by their L6 inequalities, so both directions imply the stated absolute quadratic-form error C_e(log w)^(-2/3)||r||². Complex polarization of one- and two-point sources yields all matrix blocks, uniformly in their separation. No diagonal-only estimate is misreported as an offdiagonal one.

## Infinite decay and common-pin capacity

The offdiagonal decay argument uses more than scalar ellipticity. Positivity and analyticity make the fixed soft block O(k²), the soft/high block O(k), and the high block uniformly invertible. Minimizing over the high component gives a soft Schur complement bounded below by a l times the soft norm. Its analytic derivatives and the inverse/block-inverse identities therefore give ||partial^alpha K_e^-1||<=C|k|^(-2-|alpha|). Away from zero the matrix is smooth. Dyadic-shell integration by parts gives a shell bound Cs(1+s|x|)^(-J), whose sum is C/(1+|x|). This justifies the matrix Green decay without a scalar positivity or heat-kernel domination assumption.

For m separated pins, the block-row bound is consequently
||Gamma-I_m tensor G_e(0)||<=C_e m[R^-1+(log w)^(-2/3)]. Also G_e(0)>=I/b, so its inverse has norm at most b. For a field f=Uz+q vanishing at every pin, take the common test vector v=G^-1 Uz. Its pairing with q is exactly-m z*U*G^-1 Uz. Energy Cauchy and the block bound give

    E(f)>=m z*U*G^-1Uz/(1+b zeta).

This retains the matrix capacity U*G^-1U; replacing it by the inverse of U*GU would generally be a different claim. No inversion of the full many-pin matrix is needed. The cell gap bounds the complementary norm, and m<=M gives precisely the denominator

    1+b zeta_max+M c_e/(ell³ Delta_cell).

All units and factors of ell³ match the norm of the constant field. The m=0 case is harmless and no positive pin-matrix inverse is required there.

## Actual all-state counting and ordered limits

An occupied residual site pins all nine amplitudes because annihilation at that site could not leave it occupied in the output. Selecting one endpoint of every residual R-isolated dimer in the cell interior gives mutually separated common pins. When one original interior isolated dimer is removed, every other selected original dimer survives as a residual pin. There is one forward graph edge for the removed dimer and one input occupation for a fixed annihilator/output pair. Thus the literal count is g_j(g_j-1), not half that value. Extra removals contribute nonnegative terms. Arbitrary coherences are retained by the full output amplitudes; purity is unnecessary by linearity or purification.

The translated tiling counts omitted particles, not omitted energy. Since the interiors are separated by at least three coordinate steps and graph edges have Chebyshev length at most two, any lost isolated dimer has an endpoint in the omitted region. Its expectation is bounded by theta<N>, theta<=3ell/L+6w/ell. Combining this with the checked B_R estimate gives the stated beta and Gtot lower bound. Jensen then yields the finite inequality(14), including its necessary negative subtraction rho/(2ell³). The physical diagonal stabilizer retains its original neighbors throughout.

For fixed epsilon, the scales ell~rho^(-1/3)h, R~rho^(-1/3)/h, w~rho^(-1/3), h=loglog(1/rho), satisfy all required geometric hypotheses for sufficiently small rho. In particular ell/R~h², rho ell³~h³, rho R³~h^-3 and w/ell~h^-1. The matrix row error vanishes because h^6(log w)^(-2/3)->0; its other term M/R and the variance cost M/ell also vanish. Constants may depend on epsilon,mu,tau, which are held fixed here.

The branch e<=b rho² controls beta through rho R³. The complementary branch already exceeds c_e rho²/4 because c_e<=b. Thus no energy-smallness hypothesis survives. Volume is taken first to remove ell/L, and the result is uniform over states at each fixed mean density. It does not apply to a fixed-N2 zero mode with volume diverging at the wrong mesoscopic scale.

Finally (1-epsilon)K<=K_e<=K gives G0<=G_e<=G0/(1-epsilon), and after inversion/compression,(1-epsilon)c_pin<=c_e<=c_pin. Sending epsilon down zero AFTER the volume and density limits is valid. There is no unproved uniform control of the epsilon-dependent L6 or gap constants.

## Strict improvement and the optional channel integrals

The proof's qualitative strictness argument is correct. If a<tau, the axial block is strictly above a l on a nonzero small-momentum region. If a=tau, its positive deficit contains the moving singlet; no fixed nonzero axial vector is orthogonal to all three distinct phase monomials on an open set. Every plane block is strictly above a l on a small nonzero region. Thus the integrated positive difference is positive definite in the finite nine-dimensional space.

The independent PRE provides an additional elementary check of this strictness. Since a l<=mu, each plane block obeys K_plane>=2a l I. For the axial block,

    (a l)^-1 I-K_ax^-1 >=P_v/(24a),
    integral P_v dk/(2pi)^3=I3/3.

Indeed the high inverse deficit is at least1/(12a)-1/(2mu)>=1/(24a), and the low inverse deficit is nonnegative. Therefore

    G0_ax<=(g-1/72)I3/a, G0_plane<=g I2/(2a).

Since g>=1/12, the first bound dominates, giving the explicit algebraic corroboration
c_pin>=a/(g-1/72)>a/g. This does not numerically evaluate g or identify the capacity with T0; the author's weaker strict statement already follows.

The optional E/T expressions also have the correct normalization. The axial integrated Green matrix has diagonal2g/(3tau)+1/(6mu) and offdiagonal-g_diag/(3tau), so its E eigenvalue is(2g+g_diag)/(3tau)+1/(6mu). For a plane, Sherman-Morrison gives K^-1=(2mu)^-1I-(tau l-mu)q*q/(2mu lambda). The normalized soft vector has |q u|²=(1+cos² k_j+2cos k_i cos k_j)/2. Symmetry makes that vector an eigenvector of the integrated plane block, producing the displayed gamma_T. The soft compressed inverse consequently has E and T eigenvalues1/gamma_E and1/gamma_T, with the stated multiplicities.

## Controls, failures, and reuse boundary

The author control was read after the analytic comparison, not run by this checker. It independently assembles literal endpoint words and compares15552 exactly represented Gaussian-integer Fourier entries at192 momentum/coupling combinations. Its complete-row cells of dimensions243,576,1125 have five numerical zero modes, satisfy the analytic gap bound and test finite one-/two-pin capacities, complex pinned fields and attaining mean-energy minimizers. The equality tests use exact integer-valued entries in the stated bounded range; the eigenvalue/capacity checks are explicitly floating finite diagnostics.

Reported execution was2.036599CPU seconds,2.045675wall seconds and145,276,928bytes peak RSS; the separate supervised record reports exit0, no stop,2.342272CPU seconds including monitoring and2.542550wall seconds. These controls corroborate finite formulas and do NOT prove the Green limit, strict integral gap, all-state counting or dilute limits. Those rest on the analytic arguments checked above. No assertion failure or repaired science result appears in the supplied control packet. This independent check launched no new compute job and changed no author artifact.

The checked result improves an actual full-qubit-carrier lower coefficient while keeping physical pair removals and boundaries. It leaves the stronger compatible full15 T0 lower gluing, growing-particle scattering expansion, matching EOS, pair order, tensor polarization and readable records open. No native algebra alone derives the supplied quantum state interpretation or Hamiltonian. No formal retained status or foundational promotion follows from this receipt.
