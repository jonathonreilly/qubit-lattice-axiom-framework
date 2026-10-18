# Pending corollary: full-space comparison without a prepared product collar

**Status: proposed strengthening, distinct check pending.** ROOT suggested this interpretation of the source's existing full-space estimate and has requested its distinct check. It is not incorporated into the frozen NOTE.md, does not anticipate the check's verdict, and is not independently checked evidence. The initial manuscript is preserved byte-for-byte as NOTE_REVIEW_PENDING.md, SHA256`11b3bcaa48aa13af455340993a09649030c4dd26fb8d25f273fe622e49f71b24`.

The actual finite cube Hamiltonian H, its thirteen positive blocks, given old K installed once, cap and parameter assumptions are exactly those of N/native_weak_transverse_attachment/PROPOSAL.md, SHA256`323817300ff86682cca410da69aca9e99b484474e972bab0d263c9448c1297ed`. Here N=`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`. No microscopic source, geometry or installed term changes in this proposed corollary. Only the allowed initial states and the corresponding output semantics are enlarged.

## 1. Full-space target and operator estimate

Let O be the four-dimensional literal old-pair Hilbert space, E the six physical environment qubits and F any passive reference. Set

 X=X1X2, K=2I+Z1Z2,
 s=J_y+J_z, tau=theta/J_x,
 cos(theta)=3/5, sin(theta)=4/5,
 W=exp(i theta)exp(i theta X).

H_E is the actual sum of all seven positive E-to-E compass blocks. The source's exact decomposition on the FULL eight-qubit space is

 H=H_0+V,
 H_0=[K+J_x(I-X)] tensor I_E+I_O tensor H_E+2s I,
 ||V||<=2s.

Define the joint comparison UNITARY, rather than an isometry requiring a selected collar,

 U_*(t)=exp[-i((J_x+2s)t+theta)]
                   [exp(-itK)W] tensor exp(-itH_E).   (C1)

The scalar2I inside K and every identity contribution inside H_E remain in their displayed exponentials. The crossing-bond scalar2s and the old x-bond scalarJ_x occur exactly once in the prefactor. No old-input-dependent phase fitting or global-phase optimization is used.

Using [K,X]=0,

 exp(-itH_0)=exp[-i(J_x+2s)t]
                   [exp(-itK)exp(iJ_xtX)] tensor exp(-itH_E).

Both X eigenvalues are present on O. Therefore

 ||exp(-itH_0)-U_*(t)||=2|sin[J_x(t-tau)/2]|.

Full-space Duhamel and triangle inequality imply, for t>=0,

 ||exp(-itH)-U_*(t)|| <= d(t),
 d(t):=2st+2|sin[J_x(t-tau)/2]|
                       <=2st+J_x|t-tau|.             (C2)

This is independent of every initial state on O tensor E, including correlations. Tensoring identity on F leaves its operator norm unchanged. It extends the original collar-isometry estimate by retaining the full-space factors already used in its proof; it does not require a new approximate environment-decoupling mechanism.

Under the same sufficient policy

 0<epsilon<=1,
 r=s/J_x<=epsilon/[32(theta+1)],
 w=epsilon/(16J_x),
 t in[tau-w,tau+w],
 2J_x(1+r)<=Lambda-3,

one has t>0 and d(t)<epsilon/8 by the original two-term budget. No cap, count, time or ratio is improved. For a fixed nonzero r this policy does not imply arbitrary accuracy as epsilon tends to zero.

## 2. All initial states and complete channel distance

For EVERY density operator rho_OEF, define the actual and comparison full outputs

 rho_act(t)=(exp(-itH) tensor I_F)rho(exp(itH) tensor I_F),
 rho_*(t)=(U_*(t) tensor I_F)rho(U_*(t)^* tensor I_F). (C3)

Using U rho U^*-V rho V^*=(U-V)rho U^*+V rho(U^*-V^*) and the trace ideal inequality gives

 ||rho_act(t)-rho_*(t)||_1 <=2||exp(-itH)-U_*(t)||
                          <=2d(t),                 (C4)

capped by2. The same proof works for every passive F; equivalently the unhalved diamond distance between the two joint unitary channels on OE is at most2d(t). On the stated window it is strictly belowepsilon/4. For every normalized pure joint input the phase-pinned complete-vector difference is at mostd(t)<epsilon/8. Thus no purity, basis-state condition or internal product structure of E is required for this JOINT comparison.

For mixed states the common scalar in(C1) cancels in the channel but remains specified by the operator and pure-state comparison. It cannot be silently reassigned in a subsequent coherent composition.

Tracing only the six physical environment outputs as an optional consequence, not as the definition of success, gives

 ||Tr_E rho_act(t)
   -(exp(-itK)W tensor I_F)rho_OF
                       (W^*exp(itK) tensor I_F)||_1
 <=2d(t).                                          (C5)

Here rho_OF is the ACTUAL initial old/passive marginal. This identity follows because partial trace is invariant under the local unitary exp(-itH_E) on E. It remains valid even when rho initially correlates O,F with E. It does not assert that those correlations were absent or that E was discarded by the physical device. It also does not define one environment-independent preparation map from rho_OF to the joint actual output: correlated extensions with the same rho_OF can have different joint outputs, and all such differences are retained in(C3).

## 3. Common product output versus preserved initial correlations

If the initial state is rho_OF tensor sigma_E with arbitrary density operator sigma_E independent of the old/passive input, then(C3) factors exactly:

 rho_*(t)=[(exp(-itK)W tensor I_F)rho_OF
                      (W^*exp(itK) tensor I_F)]
           tensor sigma_E(t),
 sigma_E(t)=exp(-itH_E)sigma_E exp(itH_E).            (C6)

This supplies a common evolving environment output for each specified sigma_E. It may be mixed and internally entangled. There is no requirement that the six qubits start in the computational basis, be pure, or be mutually uncorrelated. If sigma_E is unknown, the uniform error bound remains valid for every sigma_E, but the complete comparator contains its actual evolved state; it is not one fixed numerical environment output independent of the supplied sigma_E.

For an initially correlated rho_OEF, the correct target is instead the local-unitary image in(C3). It generally remains correlated. Local unitary comparison is not productization, cooling, resetting or entropy removal. One must not replace(C3) by the tensor product of its marginals and claim the same error. The pure common product-environment contract in the original manuscript remains a valid special case, not the description of every enlarged input.

If E is initially correlated with a separate environment reference that is retained in F, the same joint formulation applies. A product comparison across the logical-input versus apparatus/environment split requires initial independence across that same split; it is not implied by independence of only the reduced E state. All passive systems are acted on by identity in(C1)–(C4).

## 4. Suppliers and limits unchanged

The proposed strengthening removes the special basis/purity/internal-product collar requirement for joint unitary correctness. It does not derive the given K, the compass Hamiltonian, finite open boundary, weak transverse anisotropy, coefficient/time calibration or a physical isolation procedure. It does not preserve the original source-contact inventory, introduce a spatial head or record flag, or establish autonomous release, capture, reset or permanent halt. The surrounding cube and its actual initial state remain part of the complete physical experiment; their outputs are retained.

The author's supplied-collar theorem remains unchanged in NOTE.md. This corollary is ROOT-exposed editorial/analytical development from its full-space proof, awaiting the specifically requested distinct check. It is not a new independent check of source323817. No scientific execution, additional agent, Git/canonical/checkpoint/source/axiom/editable-prompt/model change or publication occurred. Only the pending-manuscript preservation and this separate COROLLARY.md were written.
