# Complete-source mathematical review: immutable transverse curl limits

Date: 2026-09-21. This is a post-source scientific review, separate from
the earlier blind reconstruction. It applies to the frozen note SHA-256
d5d3951bb4c84d26c468c6e5567b6bb7dd6f3eb7322d6dced9e84cadc30b3ac3
and canonical runner SHA-256
1283709aafb037f699b9e79d20e26577a09814c1b1304e473dfd80821e96ab29.

**Disposition:** one necessary scope correction, F1 below. Apart from
that explicit degenerate-parameter wording, no unresolved mathematical
defect was found in the supplied-model, smooth-profile and fixed-finite-mode
claims reviewed here. This is not an audit, retention verdict, landing
action, physical-field identification or general claim certification.

## 1. Actionable finding

**F1 — qualify the full-occupancy propagation count.**
The frontmatter claim_scope (line 4) and Section 3 (line 255) state that
the fourteen-label fully occupied model has four propagating and nine
static modes without repeating the nonzero-drive condition. The generator
allows gamma=0, and then all homogeneous current derivatives vanish.
The thirteen independent fields all have zero speed. At K=0 the same
degeneration occurs; the nonzero-K condition is stated earlier for the
vector block and should accompany the repeated count.

The displayed characteristic polynomial is correct:
lambda^9[lambda^2-gamma^2 rho_A(1-rho_A)|K|^2/3]^2.
It itself becomes lambda^13 at gamma=0 or K=0.

Narrow correction: qualify both full-occupancy count assertions by
gamma!=0 and nonzero wave vector, and state in Section 3 that all thirteen
modes have zero speed when gamma=0 or K=0. No formula, generator, proof
mechanism or runner calculation needs to change.

The author acknowledged this finding and preserved the frozen sources
pending completion of this review. F1 remains open on the exact source
hash above. A later correction acknowledgment should compare only the
affected text and source identities; it should preserve this report.

## 2. Complete source and dependency coverage

I read all 558 lines of the note, all 100 lines of the canonical runner,
and all five auxiliary author scripts (449 lines total). An initially
truncated combined tool output was repaired by targeted complete reads of
the note's remaining section and the affected process references. No
truncated argument was treated as reviewed.

The generator, currents, complete fourteen-field spectrum, conservative
limit hypotheses, separate full-occupancy model, uniform-birth noise and
empty-start extension were compared with the prior blind reconstruction:

- report: 9de24aa5265ec720e24f8ce0d95b34fa7760d1112baed3cbca7cb05e44689dcf;
- seal: 35138e3ac676833b4a4764225853fca20828956928bf734b92baa271ff7856c3.

The prior growing-fluctuation report has hash
168ae65623d124f2aa10a0c215c75e8767950f7fb1c50fc5a3fc287f1667b1dc.
Its actual-evolving-law energy argument, rather than a stationary
adjoint shortcut, remains the relevant dependency.

The inherited acoustic note has hash
4c9c671678b4d2be2f6ada61412398a2fd797f1c9bb1f101f072e3d4968082da,
matching the previously reviewed and narrowly corrected source. The axiom
memo remains
93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753.
These unchanged identities justified reuse of the earlier proofs; they
were not treated as new independent evidence merely by rerunning scripts.

The publication's portable verifier succeeded: seven capsules, 77 sealed
artifacts, 45 source links and two instruction snapshots authenticated.
Its complete output is CAPSULE_VERIFICATION.log. The count authenticates
bytes, not mathematical truth.

## 3. Reconstructed new arguments

### Polar/axial covariance and generalized reversal

For a signed orthogonal coordinate matrix R,

\[
 (Re)\times[\det(R)Rb]
 =\det(R)^2R(e\times b)=R(e\times b).
\]

Both finite label sets are closed under the stated action, and
det(RQ)RQ=(det(R)R)(det(Q)Q) on the B representation. Thus it is a genuine
48-element group action, not merely separate fitted maps.

The tensor transforms as a polar vector. If a positive edge transforms
to a negative coordinate direction, representing it again as a positive
edge reverses its four-site word. Tensor symmetry makes that reversal
change the drive sign, cancelling the negative directional component.
The actual rate is consequently covariant for both rate implementations.
The both-polar assignment would supply the unwanted determinant. The
note correctly labels the polar/axial assignment as supplied structure.

For Theta fixing e and negating b, h(Theta eta)=-h(eta), the same drive
change as the endpoint transposition. Under a homogeneous product,
configurations related by a swap have equal weight, so its adjoint
off-diagonal exchange rates are c(eta^edge). The linewise identity
sum_edges h=0 also gives equality of the original and reversed escape
rates. Therefore L*=Theta L Theta, including the diagonal rates. The
path-law conclusion needs the additional Theta-invariance of the stationary
product, which the note states. One can formulate this on full support
or on the appropriate invariant active support. Ordinary detailed balance
does not follow.

The generalized reversal statement concerns the conservative L_N.
Uniform births remain irreversible and are not covered by that identity.
Theta is a comparison of histories, not a forward label-rewriting event.
Y and the B triple character are odd; the orbit populations, X, A
quadrupoles and B pair characters have the stated even parities.

A separate exact 240-state five-cycle count-sector calculation checks
both rate implementations at negative gamma=-3/5. It verifies stationarity,
escape-rate matching and Q^T=Theta Q Theta, while ordinary matrix symmetry
fails in 800 entries. This differs from the author's four-cycle sector
construction and supports the new waiting-time part of the argument.

### Nonlinear entropy, energy and stress

With theta=grad h and dp=C dtheta, J_i=C grad Psi_i implies
dPsi_i=J_i.dtheta. Hence q_i=theta.J_i-Psi_i satisfies
dq_i=theta.dJ_i. Smooth conservative Euler solutions therefore have the
claimed entropy conservation law. At the fixed isotropic background,
Jbar=Psibar=0, so subtracting the affine entropy tangent gives exactly
the stated relative flux; no omitted constant affects it.

For a pure vector perturbation,

\[
 \delta p_{A,\pm i}=\pm X_i/2,\qquad
 \delta p_{B,\sigma}=Y\cdot\sigma/8,\qquad\delta p_0=0.
\]

The quadratic relative entropy is
3|X|^2/(2rho_A)+|Y|^2/(2rho_B). At second order the entropy-flux term
theta_1.J_1 equals p_1.grad Psi_2=2Psi_2, since Psi_2 is homogeneous
quadratic. Subtracting Psi_2 leaves gamma X cross Y, with the displayed
sign and no extra factor of two. This also shows why the positive
quadratic energy is a probability-profile functional, not a fixed
additive energy carried by each record.

For normalized vectors and signed
c=gamma sqrt(rho_A rho_B/3), the equations are
E_t=c curl B and B_t=-c curl E. They imply the energy continuity equation
without Gauss conditions. Direct vector differentiation gives

\[
 \partial_t(E\times B/c)
 +\nabla\cdot\left[\tfrac12(|E|^2+|B|^2)I-EE^T-BB^T\right]
 =-E\,\nabla\cdot E-B\,\nabla\cdot B.
\]

The sign, signed-speed normalization and both divergence terms are correct.
The note restricts the momentum definition to gamma!=0 and does not erase
the right side in an unconditioned product ensemble.

The independent checker differentiates the logarithmic relative entropy
directly along a fifteen-probability path, computes the quadratic flux
from the pair tensor, and tests an exact affine-space curl solution with
negative signed speed -3/7. In that solution div E=2, div B=3 and the
stress defect at the origin is (-8,-1,-9), a decisive counterexample to
omitting the divergence terms.

### Second-order record transport

At a constant isotropic background and with a first-order vector
perturbation, Psi begins at order epsilon^2. Therefore the second-order
orbit flux is (1-2rhobar_A)Psi_2 or (1-2rhobar_B)Psi_2; the total is
2pbar_0 Psi_2. The first-order scalar perturbations vanish by the specified
pure-vector hypothesis. A second-order perturbation of an orbit density
cannot change these order-two flux coefficients.

Using E_wave,t+div Psi_2=0 in each second-order conservation equation
proves all three displayed time-constant differences. The offsets may
depend arbitrarily on space. The note correctly avoids identifying
record density with wave energy and keeps the other generated
second-order moments. It does not assume a nonexistent nonlinear closure
of the six vector components.

The independent species-sum control uses rhobar_A=2/7,rhobar_B=3/8
and finds the three coefficients 3/7,1/4,19/28 directly from the tensor
current, matching the separate entropy-flux calculation.

### Ordered Gauss conditioning and later births

For a fixed finite list of nonzero modes, choose only one representative
of each conjugate pair. For all sufficiently large N there is no
self-conjugate alias in this fixed list. The product CLT has nondegenerate
real/imaginary longitudinal coordinates and zero covariance with the
transverse coordinates. At an isotropic background it also has zero
covariance between these vector coordinates and the eight other field
coordinates.

At fixed epsilon>0 the box has limiting probability p_epsilon>0 and a
Gaussian-null boundary. Dividing the joint path expectation by the box
probability transfers both distributional convergence and the existing
L2 propagation error. This does not require that the conditioned law
remain product or stationary. Its entropy cost is exactly minus the log
of the conditioning probability, hence bounded in N at fixed epsilon.

Only after the N limit is taken may epsilon tend to zero using the
Gaussian independence. The longitudinal coordinates vanish and the
transverse Gaussian is unchanged. The note correctly calls the
intermediate fixed-box law a truncated Gaussian and does not assert a
simultaneous epsilon_N limit or conditioning of all lattice modes.
The resulting constraints are for the selected finite modes. Conservative
curl dynamics preserves them.

The independent check retains the entire moment covariance, not only a
six-vector submatrix. Conditioning lowers its rank from 14 to 12 in the
interior and from 13 to 11 in the fully occupied restriction. The other
static covariance block is unchanged. Thus the eight, respectively seven,
additional static fields have not been removed by the preparation.

For the growing process the same bounded reweighting is applied to the
joint unconditioned limit at time s and later observations. The limiting
future birth noise is independent of the time-s Gaussian state. This is
a statement after the fixed-epsilon limit, not finite-N conditional
product independence. Curl has no longitudinal drift, and the independent
birth jump sum gives covariance 8 beta p_0 I for each of U=2X and V=Y,
with no cross covariance. Therefore the complex longitudinal variance
increment is exactly

\[
 \int_s^t8\beta p_0(u)\,du
   ={4\over7}[\rho(t)-\rho(s)].
\]

Each real or imaginary part of a nonzero complex mode has half that
variance. The displayed note formula is consistent with its conjugate
covariance convention. The ordering in this argument is N first,
epsilon second, for fixed s,t and a fixed mode list.

## 4. Reused theorem checks and scope

The finite-alphabet adaptations preserve every relevant hypothesis:
bounded fixed range and rates, a positive exchange floor on every
unequal-label nearest-neighbor swap, homogeneous product invariance,
polynomial currents and the positive entropy symmetrizer. The change
from seven to fifteen active labels changes the explicit loose canonical
bound to 2M^2 15^M; logarithmically growing blocks still suffice. A
full-support C2 solution on a fixed interval is assumed, not constructed.
No post-shock result or physical hydrodynamic identification is implied.

The stationary finite-mode theorem retains its supremum outside
expectation, fixed wave vectors and time horizon, and all fourteen
fields. Its longitudinal covariance term is correct. The exactly fully
occupied process is treated in thirteen independent probabilities on
fourteen active labels, with a nonsingular metric there, rather than
by a singular vacancy limit. Its wave count needs F1's qualification.

For uniform births, the exact homogeneous product trajectory, fourteen
species reaction matrix -beta 11^T and noise beta p_0 I match the blind
reconstruction. The covariance identity follows because A C=C A^T
cancels the transport part and the birth Lyapunov equation has the stated
source. The covariance of random event counts is essential; fixed-count
categorical noise would be wrong.

The actual-law backward energy identity and the canonical dual bound
remain valid for time-dependent products. In particular, for the backward
solution u, the exact additive-functional variance equals
E|u_a|^2+integral E Gamma; the floor makes
E Gamma >=2N c_* E_0. Cauchy-Schwarz then gives the stated
2/(N c_*) energy estimate. No stationary adjoint is substituted for the
time-dependent law.

For empty start the direct finite-state energy identity divides by no
probability, while conditional arrangements on positive-mass count
sectors remain uniform. Alternatively the explicit positive-time cutoff
and its O(delta) early-interval control give the required ordered limit.
The note does not use a singular entropy inverse at time zero.

The equal-label normalization U=2X,V=Y is twice the vector normalization
used in the blind reconstruction, consistently multiplying its covariance
and noise by four. The signed phase, off-diagonal Fourier signs, static
longitudinal drift and added noise all agree. Generic unequal orbit
ratios require time ordering. The late-speed statement refers to the
continuum family on fixed intervals first, not to infinite-time
undamped propagation at fixed finite N.

The declared extra label menu, axial assignment, tensor, floor, clock,
uniform birth rule and any preparation remain supplied structure.
The note does not claim that the minimal axioms select them, that the
classical labels are physical qubit outcomes, or that the entropy/stress
functionals are physical electromagnetism, gravity or quantum dynamics.

## 5. Executable evidence, repairs and limits

The canonical runner hashes the note and declared input sources, copies
the five author scripts before execution, records complete child output
and checks child-source hashes. Its 91 controls consist of the wrapper
scope check plus 38+13+15+21+3 auxiliary controls. I inspected every
auxiliary script. Their algebraic assertions do not supply the limit
proofs; the note states this distinction. No implementation/prose drift
beyond F1 was found.

Existing source-bound author executions were authenticated rather than
rerun for another PASS count. The baseline identities, all five executed
sources and result counts match. For each of the thirteen mutations I
reconstructed the uniquely specified source replacement, checked its
executed hash, authenticated its full result file and verified an actual
mathematical assertion failure in the declared suite. This verifies the
recorded mutations, not universal adequacy of mutation coverage.
AUTHOR_EVIDENCE_VERIFICATION.json retains the exact mappings and failures.

New independent controls are in independent_check.py. Two executions are
retained. The first completed, but inspection identified that its final
degenerate-case check merely counted a literal list of thirteen zeros;
that line was not independent executable evidence of the current matrix.
The second replaces it by the derivative of the actual tensor current
in thirteen independent full-occupancy coordinates: rank four at
gamma=1, rank zero and characteristic polynomial lambda^13 at gamma=0.
The analytic F1 finding did not depend on that weak first fixture.
The original script, full result and raw log are preserved, and no failed
or corrected route was discarded. The final run completes ten exact
finite/symbolic groups and has no assertion failure.

The checks do not numerically test the infinite-N limit, global smooth
existence or microscopic quantum realization. Those are either supported
by the bounded proofs stated above or explicitly outside the theorem.
No new simulation was used.

The two cited literature abstracts were checked for attribution and
methodological scope only: [Mendoza and Munoz](https://arxiv.org/abs/0806.2678)
describe a lattice-Boltzmann electromagnetic construction using auxiliary
vectors, and [Hanasoge, Succi and Orszag](https://arxiv.org/abs/1108.2651)
describe a pseudovector distribution formulation. Neither is used as a
proof of this stochastic generator or a novelty claim. Their full papers
were not imported as mathematical dependencies.

All hashes and execution evidence are bound in SOURCE_REVIEW_SEAL.json.
The review used the supplied worktree and unchanged local methodology
snapshots; no Git fetch, branch operation, source fix, PR, audit,
delegation or model/effort change was performed. No editable prompt file
was changed. The next authorized source action belongs to the author:
apply F1 and request a narrow affected-text/hash acknowledgment.
