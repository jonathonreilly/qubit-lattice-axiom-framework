# Independent check of the two-excitation contact pump

**Finding: the proposed capture-and-stay-dark mechanism works in the declared conditional model.** Both local states are normalized eight-spin j=2 highest weights. The completed local operator is an SU(2) scalar. In the global exactly-two-flip sector it acts as the rank-one transfer |psi><chi|. Every translated/rotated target evolves under the full homogeneous Heisenberg Hamiltonian with identically zero nearest-neighbor contact amplitudes, so every source overlap stays zero. The installed monitors therefore cease to produce clicks after a successful pump without an externally commanded shutdown. The target's nodal plane, including its chosen center, stays in q.

This is a positive conditional construction, not a native-instrument derivation or a physical Record-registration theorem. Its domain is exactly two flips over a supplied common q background with no pre-existing Records claimed protected. No almost-sure first capture is established. An adjacent product seed has strictly positive first-capture probability, with the explicit bound below. The pump is an engineered finite-range eight-spin dissipative operation and can inject energy; calling it passive cooling would be incorrect.

## Independent provenance and controls

The argument and script were developed from the task brief without reading the separate author's forthcoming CONTACT source. Existing foundation boundaries and the homogeneous H convention were reused at source snapshot `584755767deb8dfb670f07211d8446873fd0999b`, worktree HEAD `688e7b02a3dabd6254193992e1f18da2532e683d`. No new foundation claim or audit status is assigned. Model/profile: OpenAI Astra/medium, unchanged; same-family mathematical check, not an external independent referee.

Files in this directory:

- CONTACT_PUMP_INDEPENDENT_TARGET.md: pre-test registration.
- contact_pump_independent_check.py: exact SymPy 1.14.0 controls.
- CONTACT_PUMP_INDEPENDENT_RESULT.json: complete output.
- CONTACT_PUMP_INDEPENDENT_SHA256.json: artifact identities.

All 22 gates passed. The local check uses all 256 computational basis states; the lattice check applies the exact physical unordered-pair Hamiltonian without a finite box through H^6, reaching 14,448 nonzero configurations. Every checked order has zero contact and zero x=0-plane occupancy. These finite orders corroborate the all-time proof; they are not its substitute. The same script independently enumerates all 24 proper cubic rotations and relevant translations for a fixed edge. Parent-suggested rate and energy values were treated as hypotheses and checked, not accepted as inputs. No independent author's code or new source text was consulted.

## 1. Exact local normalization and scalar completion

Let the local eight sites be B={(x,y,0): x=-2,-1,1,2; y=0,1}. Write A=(1,0,0), Bp=(2,0,0), C=(2,1,0), D=(1,1,0). The source is

    chi=(|A Bp>-|Bp C>+|C D>-|D A>)/2.

Its four configurations are distinct, so ||chi||=1. Total spin raising J_+ removes either flip; at each of the four vertices the two incident coefficients cancel. Thus J_+ chi=0. The eight-spin magnetization is m=4-2=2, so this is a highest weight of total spin j=2, not a mixture of larger-j irreps.

Use normalized exterior products u wedge v=(u tensor v-v tensor u)/sqrt(2), with f1=(delta_1-delta_-1)/sqrt(2), f2=(delta_2-delta_-2)/sqrt(2). The ordered two-particle amplitude is

    F=(f1 wedge f2)(x1,x2) (delta_0 wedge delta_1)(y1,y2)
      delta_0(z1)delta_0(z2).

The two antisymmetric factors make F symmetric under simultaneous particle exchange. Its norm on ordered pairs is one, and it vanishes on coincident particles. Consequently the unordered physical amplitude psi({r1,r2})=sqrt(2)F(r1,r2) is normalized. There are eight nonzero unordered configurations, each with amplitude +/-1/(2sqrt(2)). The one-flip amplitude after J_+ is a sum over the second site; the x factor already sums to zero because each f_a has zero sum. Hence J_+ psi=0, and psi also has m=j=2. It is orthogonal to chi, since psi has no nearest-neighbor contact configurations.

For r=0,...,4 put n_r=r!4!/(4-r)! and

    chi_(2-r)=J_-^r chi/sqrt(n_r),
    psi_(2-r)=J_-^r psi/sqrt(n_r).

The raw squared norms are 1,4,24,144,576. The next lowering vanishes. Define

    V=sum_(m=-2)^2 |psi_m><chi_m|.

The matching ladder coefficients imply [V,J_z]=[V,J_+]=[V,J_-]=0. V is an intertwiner between two orthogonal copies of the same irreducible representation, with V†V equal to the projector onto the chi multiplet and VV† the projector onto the psi multiplet. The exact script checks the commutators on the full eight-spin space and checks its isometric/adjoint action on every multiplet vector. No directional q measurement is needed to specify this scalar. The physical spatial pattern and source/target choice are nevertheless supplied.

In the global exactly-two-flip sector, every lowered source chi_m with m<2 would require at least three flips inside B and therefore cannot occur. The m=2 component requires both global flips inside B; the exterior is then the aligned background. Thus on this global sector the embedded operator is exactly V=|psi><chi|. It annihilates states with zero or one flip in its support. Local scalar covariance is sufficient to repeat this statement for every q; no ill-defined infinite-volume total-spin generator is invoked.

## 2. Full actual-Z3 Hamiltonian, including contact interaction

On unordered distinct pairs X={r1,r2}, the homogeneous Heisenberg Hamiltonian H=2j sum_edges(I-SWAP) acts as

    (H f)(X)=2j[12-2 c(X)]f(X)
             -2j sum_(allowed single-particle NN moves X->Y) f(Y),

where c(X)=1 if the two sites are adjacent and zero otherwise. An attempted move onto the occupied site is excluded. In particular its diagonal is 24j-4j c(X), not the free diagonal 24j. Its bounded norm is at most 48|j|.

Under the symmetric ordered-pair identification, this is the compression of the distinguishable two-particle free Laplacian, minus 4j times the contact projection. To prove exact evolution, evolve both x orbitals by the same one-dimensional Hamiltonian 2j L_Z, evolve both y orbitals likewise, and evolve each z delta by that same one-dimensional Hamiltonian. The product of the x wedge, y wedge and symmetric z tensor then solves the full distinguishable free equation on actual Z3 x Z3.

At every time:

- x and y factors remain antisymmetric within their respective coordinate pairs;
- the x orbitals remain odd under x->-x, since L_Z commutes with reflection;
- the ordered amplitude remains symmetric overall and normalized;
- collisions vanish because x1=x2 makes the x wedge vanish;
- a contact along x has y1=y2, so its y wedge vanishes;
- a contact along y or z has x1=x2, so its x wedge vanishes;
- a particle at x=0 has zero x-orbital amplitude.

Thus the free solution remains in the hard-core subspace and has zero contact correction at every time. It solves the physical Heisenberg equation above, so uniqueness of the bounded-H evolution proves it is exp(-itH)psi. This is an exact all-time argument with no finite-box limit and no omitted interaction term. Proper cubic rotations and translations transport it to every installed target. The preserved plane passes through the target's center and has the rotated x normal.

## 3. Countable generator and positive first-event probability

Keep precisely the proposed label convention: every translation c in Z3 and all 24 proper cubic rotations R, even when some source effects are duplicates. Write chi_lambda, psi_lambda for the transformed states. Within the exactly-two-flip sector,

    L_lambda=sqrt(gamma)|psi_lambda><chi_lambda|,
    L_lambda†L_lambda=gamma|chi_lambda><chi_lambda|.

Let C be the diagonal projection onto all adjacent-pair configurations. Every adjacent edge belongs to 32 labeled source supports, and every source coefficient has magnitude 1/2. The count follows directly from four edges per source and eight rotations taking an unoriented edge to a fixed coordinate direction, each then admitting one matching translation; the script explicitly enumerates the labels. Equivalently there are four plaquettes around each edge and eight source realizations per plaquette.

For any two-flip vector f, Cauchy-Schwarz on each four-edge source gives

    sum_lambda |<chi_lambda,f>|² <= 32 ||C f||².

Therefore A=sum_lambda |chi_lambda><chi_lambda| exists strongly and 0<=A<=32 C. This sufficient bound is not claimed sharp. The dimensionful total effect is gamma A; the total instantaneous click rate is at most 32 gamma. On a localized adjacent product seed |e>, its initial total rate is exactly 32 gamma/4=8 gamma. If labels are deduplicated, gamma/rate conventions must change; the numbers here apply to the specified 24-rotation family.

For positive trace-class rho, the countable jump map sum_lambda L_lambda rho L_lambda† converges in trace norm, with total trace <=32 gamma Tr(rho). It extends boundedly and completely positively, including passive references. This is pointwise trace-norm convergence, not operator-norm convergence of finite-center truncations on the full trace-class unit ball. Together with bounded H it defines the conservative bounded Lindblad generator

    G(rho)=-i[H,rho]+sum_lambda L_lambda rho L_lambda†
           -(gamma/2){A,rho}.

The usual bounded Dyson path expansion follows directly: retain every label/time sequence and the no-click branch, and use the rate bound for convergence and nonexplosion. Its no-click contraction is K_t=exp[(-iH-gamma A/2)t]. Unlike the prior uniform one-excitation projector process, no commutation of A and H is assumed or needed here.

Every first-label density is gamma|<chi_lambda,K_t eta>|² and its output is psi_lambda. For adjacent eta=|e>, choose any source label containing e, whose initial overlap has magnitude 1/2. With M=48|j|+16 gamma, contractivity gives ||(K_t-I)eta||<=Mt. Thus for 0<t<=1/(4M) that label's amplitude is at least 1/4 and

    Pr(first click has this label and time<=t) >= gamma t/16.

This verifies an explicit strictly positive event probability. The aggregate small-time probability is 8 gamma t+O(t²). The unnormalized no-click state remains K_t|e>, and its squared norm is the complete no-click probability. The long-time no-click mass and almost-sure capture for this pump are not evaluated or claimed.

## 4. Why all later channels are dark

For every installed target psi_lambda and every s>=0, section 2 gives C exp(-isH)psi_lambda=0. Every source is supported in C, hence

    L_mu exp(-isH)psi_lambda=0 for every mu,
    A exp(-isH)psi_lambda=0.

Consequently K_s psi_lambda=exp(-isH)psi_lambda, by uniqueness of the bounded no-click differential equation. Its norm remains one. The total next-click density is identically zero; all subsequent monitor labels are dark, not merely the channel that clicked. The unconditional density after a first click follows H alone, because the jump and loss terms both annihilate that orbit.

This addresses the earlier monitored-singlet obstruction: there is no second-center pump click with positive probability in this exact two-flip domain. No physical switch, external stop message or hidden omission of later outcomes is used. The pumps remain installed; their rates vanish on the invariant output orbit. Every pre-first-click failure/no-click branch is retained. If a successful event is separately interpreted as registering q at its center, the subsequent spin dynamics preserves that center and its plane. Actual registration, admissibility of that content and readout are separate physical bridges.

## 5. Resource and claim limits

Exact energy checks give <chi,H chi>=20j and <psi,H psi>=24j. The former has the contact diagonal reduction and no internal nearest-neighbor configuration moves; the latter has free diagonal 24j and no internal contributing hops. For j>0 the selected transfer increases expected system energy by 4j. A supplied environment/drive can provide this; it is not automatically passive cooling, energy-conserving system-only control, or a selected thermal process.

The operator is finite-range but acts coherently on an eight-site pattern spanning both sides of the nodal plane. Its source-to-target choice, full SU2 completion, bath/Born detection law, gamma, initial aligned two-flip representation and homogeneous H remain supplied. The scalar completion removes the need for q-axis programming; the contact-free invariant target removes external monitor shutdown within this model. Neither follows from symmetry alone: the source/target map was engineered to have these properties.

No statement is made for arbitrary excitation numbers. Outside exactly two flips, the lowered multiplet terms become active and exterior excitations need not factor out; the rank-one reset and global dark-orbit proof no longer apply. Nor is there a proof preserving arbitrary pre-existing Records, of almost-sure capture, of formation from the zero-flip vacuum, or of an R-only state law before first capture. Before that event the no-click quantum state and elapsed time remain additional prediction inputs while R can remain empty. The no-click ensemble is not itself identified with the framework's realized Record configuration.

Within the stated model no mathematical failure was found. The positive gain is a complete positive-probability preparation process whose own installed pumps become dark after capture, with full-H permanence proved. Its native physical supplier, state/Record interface and actual registration remain open.
