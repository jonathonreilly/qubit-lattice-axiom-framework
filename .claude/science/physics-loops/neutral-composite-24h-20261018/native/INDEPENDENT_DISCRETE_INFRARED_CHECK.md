# Independent discrete-symmetry and conditional infrared check

Checked `native/neutral_rung_discrete_symmetry.py`, its JSON, and the first two sections of `DERIVED_INFRARED_ROUTE.md`. The exact symmetry and finite canonical selection rule pass. The continuum discussion is a conditional route, not evidence that the native isotropic bulk is critical.

## Independent physical 16-dimensional rung calculation

I constructed the full four-spin matrices directly, before the parity compression. The transverse physical Hamiltonian is

h_phys=−X0X2−X1X3−Y0Y1−Y2Y3.

Let R permute sites by (x,y)->(y,1−x), and let U_z=exp(−i pi Z/4) act on each physical spin. Then S=R U_z^(tensor4), and P_x=X0X1. Exact SymPy matrix multiplication gives [S,h_phys]=[P_x,h_phys]=0. The spin rotation sends X to Y and Y to −X, compensating the exchange of x and y bonds by the square rotation. This uses the equal transverse x/y coefficients of the supplied rung, not an arbitrary anisotropic transverse model.

On an even-parity computational bit string with n occupied bits, the spin-rotation phase is −exp(i pi n/2), namely −1 at n=0 or4 and +1 at n=2. This exactly reproduces the signs used by the root's compressed S. P_x compresses to logical X0X1. For T=P_x S, the independent physical calculation finds

T^4=−(Z0Z1Z2Z3),

so T^4=−I throughout the positive-parity rung subspace, in particular in its low doublet.

The signed physical longitudinal action is

D0 -> −D1, D1 -> D3, D2 -> −D0, D3 -> D2.

This matches the JSON's signed-permutation matrix when columns label the transformed input D. The matrix is orthogonal. Therefore the same T on both ends leaves sum_a D_a tensor D_a invariant: signs square away and channels are permuted. Its product over rungs is an exact global symmetry of the native tube for any longitudinal coefficient. It is a discrete microscopic symmetry, not a continuous microscopic charge.

## Exact low action and canonical inheritance

Using the exact physical eigenspace at energy −2sqrt(2), I independently compressed sqrt(2)D0D1 and sqrt(2)D0D2 as tau1,tau2 and defined tau3=−i tau1 tau2. With the induced inner product retained, exact algebra gives

T_low=(I+i tau3)/sqrt(2),
T_low tau1 T_low^−1=−tau2,
T_low tau2 T_low^−1=tau1,
T_low tau3 T_low^−1=tau3.

This also checks the root's use of an inverse rather than transpose in its nonorthonormal eigen-coordinates. Physical unitarity need not appear as an ordinary Euclidean-coordinate transpose relation in that intermediate basis.

On the product low space, T_total=exp(i pi Q0/4), Q0=sum_j tau3,j, with the given local conventions. Hence commuting matrix elements must have Delta Q0 in 8Z: four net collective raising/lowering flips, since each flip changes Q0 by two. Two-creation terms change Q0 by four and are forbidden. Number-conserving two-feature exchange is allowed; the phrase “two-feature number-changing” should retain this distinction. Four-feature charge-changing processes are symmetry-permitted, not guaranteed by symmetry to have a nonzero coefficient or to arise at any particular perturbative order. The stated sixth-order occurrence relies on the separate earlier calculation, which this check does not rederive.

For a finite chain with an isolated continued band, let P0 be the unperturbed product low projector and P(lambda) its symmetry-invariant spectral continuation. The canonical polar identification built from P(lambda)P0 and [P0P(lambda)P0]^−1/2 intertwines the same global T because every factor commutes/intertwines it. The resulting canonical effective Hamiltonian therefore inherits the exact discrete symmetry, and every coefficient of a valid analytic expansion obeys the selection rule to all orders. This needs the finite-band isolation and invertibility assumptions. It gives neither a size-uniform convergence radius nor a quasi-local thermodynamic effective Hamiltonian automatically.

## Conditional continuum interpretation

For the stated leading spin Hamiltonian −(t/2)sum(XX+YY), the Jordan–Wigner hopping amplitude is −t: XX+YY=2(tau+ tau−+tau− tau+). The single-particle dispersion is −2t cos k. At half filling the velocity is 2t a_rung (hbar=1). The free one-dimensional continuum fixed point has K=1 in the supplied Luttinger conventions. This is the standard free-chain limit, not a novel scalar derivation. Giamarchi's lectures describe the bosonization framework: https://arxiv.org/html/cond-mat/0605472v1 .

Using H_LL=(v/2pi) integral[K(partial theta)^2+K^−1(partial phi)^2] with the usual compatible compactification, exp(i m phi+i n theta) has dimension (m²K+n²/K)/4. Thus cos(4phi) has dimension 4K and cos(4theta) has dimension 4/K. A one-site translation at half filling shifts phi by pi/2, forbidding the 2k_F vertex cos(2phi); “single umklapp” is a convention-dependent name for that forbidden vertex. The discrete quarter rotation shifts theta by pi/2 and forbids cos(2theta), while permitting cos(4theta). At K=1 both allowed vertices have dimension four and are perturbatively irrelevant in 1+1 dimensions. Derivative/marginal terms can renormalize K and velocity; symmetry allowance alone does not determine their coefficients.

This supports a conditional weak-perturbation infrared scenario, provided the effective interactions are appropriately local and controlled, the bulk translation symmetry and specified filling/state apply, and the full allowed perturbations do not move the theory out of the relevant Gaussian stability regime. Open boundaries need their own boundary analysis; they are not a proof that the bulk forbidden staggered vertex is generated everywhere. A finite sixth-order charge violation is compatible with an emergent infrared continuous symmetry because an irrelevant symmetry-breaking operator need not vanish microscopically.

Verresen et al. explicitly study emergent U(1) in different constrained-chain models, useful as methodological precedent only: https://arxiv.org/html/1903.09179v1 . It does not prove this tube's phase. The SciPost link in the root note returned access denial during this check, so its detailed conventions were not independently sourced here; the displayed dimensions were checked directly from the declared Gaussian normalization.

No conclusion follows here about equal-coupling native gaplessness, the three-dimensional thermodynamic phase, a cosmological scalar, a universal source vertex, or the original composite's infrared readout. The later one-pair readout section was outside the requested scope and was not checked in this report.

## Added full-rung projective symmetry and LSM applicability check

The added state constraint applies to the full eight-dimensional positive-parity rung, not only its low doublet. Independently constructing physical 16-dimensional Pauli matrices gives

P_x=X00 X01, P_y=Y00 Y10,
P_x²=P_y²=I, P_x P_y=−P_y P_x.

Both commute with the transverse Hamiltonian and with the physical rung parity, so these relations survive exactly after restriction to all eight positive-parity states. P_y sends the four D operators to (−D0,+D1,−D2,+D3); applying it on both neighboring rungs preserves every D_a tensor D_a term. The earlier P_x has the same bond-preservation property. Their products over the chain are therefore exact internal symmetries. Unlike the quarter-square-rotation argument, these plane-product symmetries do not require identifying the rung with a low effective spin.

Their ADJOINT actions commute and square to identity, defining the on-site group Z2 x Z2. The implementing matrices have gauge-invariant commutator −I, so this is a nontrivial projective class on the entire local Hilbert space. Multiple copies of that projective representation inside an eight-state rung do not cancel its common commutator phase. The algebra can be represented as a projective two-dimensional factor tensored with a four-dimensional multiplicity, but no low-energy projection is needed for the class.

I checked the actual statement of Ogata–Tachikawa–Tasaki, Theorem 4: a translation-invariant, group-invariant pure split state requires a trivial on-site projective class. The paper explains the connection from unique gapped ground states to the split property for the bounded finite-range one-dimensional setting. Source: https://arxiv.org/html/2004.06458 (Theorem 4 and its setup). Thus applying the established theorem, rather than asserting a new proof, is appropriate.

For the infinite positive-parity tube, each rung supplies the same finite eight-state on-site algebra, interactions have finite range and uniformly bounded norm at fixed finite couplings, one-rung translation is a symmetry, and the on-site class is nontrivial. A unique infinite-volume ground state would inherit the internal and translation symmetries; if also gapped in the theorem's sense it would contradict that obstruction. The claimed conclusion “no unique gapped ground state” is therefore justified for this full selected-parity tube.

Crucial boundaries of application:

- This is the full tensor product of eight-state positive-parity rungs. Further restricting the numerical Hilbert space by fixed GLOBAL plane labels is not itself an ordinary on-site tensor-product chain to which the theorem can automatically be reapplied. Such a restricted finite spectrum can miss symmetry-related excitations.
- A gapped symmetry-broken or translation-broken phase with multiple infinite-volume ground states is allowed. The theorem does not by itself prove a gapless phase, a conformal theory, a neutral pole, or a nonzero weight for the original composite.
- Enlarging the translation cell to two rungs makes the combined projective class trivial; spontaneous period doubling is a possible escape through broken one-rung translation, not a contradiction.
- Finite odd-length chains have anticommuting global P_x and P_y and hence exact paired spectra. Finite even-length chains have commuting global products and need not have exact pairs. Neither finite observation alone is the infinite theorem.
- The theorem does not choose positive rung parity over other physical sectors or turn the fixed-width tube into a three-dimensional thermodynamic model.

No incomplete warm-start spectrum was used in this applicability check. Small residuals certify accuracy of found vectors, not completeness of low symmetry sectors; the planned random-component reruns address a separate numerical issue.
