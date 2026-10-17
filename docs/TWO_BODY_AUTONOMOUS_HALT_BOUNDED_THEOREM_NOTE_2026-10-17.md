---
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: product_source_controlled_stop_bounded_theorem_note_2026-10-16
target_blocker_text: "Mathematical target: replace the externally scheduled old-pair operation by an explicit time-independent controller/plant Hamiltonian and independently specified ready state, with strict nearest-neighbor two-body added blocks."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Review this wrapper, execute the root-owned portable canonical program, and complete publication conformance; retain physical coefficient supply and native incoming-packet preparation as open obligations."
conditional_surface_status: "Supplied literal old K, positive nearest-neighbor two-body source ladder, exact isolated one-head clock and independently prepared common clock packet, in product with the old input and source vacuum. Fixed calibrated residual; only added old-site loads meet two. Infinite blank tail for all later times, with finite readiness and finite-apparatus horizons distinguished."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "A complete-output autonomous reflection construction for a fixed old-pair target under explicit apparatus and preparation premises, with exact finite residual certificates and conditional quantitative packet estimates."
source_science_acceptance_complete: true
wrapper_root_approval: separately_recorded
canonical_execution: separately_recorded
publication: separate_from_source_acceptance
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Autonomous reflection from a positive two-body source ladder

The supplied positive nearest-neighbor two-body ladder implements the fixed
old-pair operation by reflection of an escaping one-head clock, with a
certified nonzero calibration ceiling and explicit complete-output packet
errors. Its source vacuum leaves no persistent added old interaction. Its old added-incident loads are below
two; its source and entrance-clock loads are larger. The all-future version
uses an infinite clock tail.

Claim type: `bounded_theorem`. Source-status request: `proposed_retained`.
The actual source surface is `conditional-support`, with no retained audit. Root's source decision of 2026-10-17 accepts the frozen
stationary, generic packet and concrete interval composition for conditional
provisional reuse. That decision has SHA256
fba41e11ee5e282800547e7571ab520abddeda1d9d3947d7095b9dfbf6fbc4fb;
its qualification has SHA256
33f4e340f2909d907e4c8fe166c86b306e82e369a6fa3ddb5eca1ab4f19405c8.
The source decision (`outputs/two_body_autonomous_halt_2026_10_17_inputs/root/SOURCE_ACCEPTANCE.json`)
and qualification (`outputs/two_body_autonomous_halt_2026_10_17_inputs/root/QUALIFICATION.md`)
are separate from wrapper review, portable execution and publication. Their
actual integration outcomes are recorded in the
[review history](../.claude/science/physics-loops/toe-two-body-autonomous-halt-20261017/REVIEW_HISTORY.md)
and [publication checks](../.claude/science/physics-loops/toe-two-body-autonomous-halt-20261017/PUBLISH_CHECKS.json).

**Primary runner:** `scripts/two_body_autonomous_halt_2026_10_17.py`.
The root-owned [primary](../scripts/two_body_autonomous_halt_2026_10_17.py)
directly imports the separately written
[check module](../scripts/two_body_autonomous_halt_check_2026_10_17.py).
The result (`outputs/two_body_autonomous_halt_2026_10_17.json`),
point witnesses (`outputs/two_body_autonomous_halt_2026_10_17_point_witnesses.json`)
and [cache](../logs/runner-cache/two_body_autonomous_halt_2026_10_17.txt)
are evidence only for their actual recorded execution and freshness in the
[execution record](../.claude/science/physics-loops/toe-two-body-autonomous-halt-20261017/CANONICAL_EXECUTION.json).
The [source manifest](../.claude/science/physics-loops/toe-two-body-autonomous-halt-20261017/SOURCE_MANIFEST.json)
binds the unchanged mathematical bodies, and the
artifact manifest (`outputs/two_body_autonomous_halt_2026_10_17_inputs/ARTIFACT_MANIFEST.json`)
binds the historical evidence. Historical absolute paths label original runs;
the portable programs consume repository-local declared inputs.

## Conditional result

Keep the literal old pair and fixed target

\[
 K=2I+Z_1Z_2,\qquad
 W=\frac{(9+12i)I+(-16+12i)X_1X_2}{25}.
\tag{W1}
\]

Write \(\Omega=|00\rangle_{AB}\) and \(\iota\psi=\psi\otimes\Omega\).
Use the exact coefficients and physical Hamiltonian below. Supply one common
normalized finite-support incoming clock vector \(\chi_N\), independent of the
old input and any passive reference, as constructed in the concrete source.
The readiness is a product across old input, source vacuum and clock; the
one-head clock vector need not be a product across its individual qubits.
Let \(\beta_s\) be the generic theorem's normalized free reflected packet,
including its free reflection phase and positive-real normalization. The
physical complete-output comparator is

\[
 \zeta e^{-i\nu t}\,\beta_{t-T}\otimes
 \iota e^{-itK}W,\qquad
 \zeta=-e^{-4ik_0}\alpha,\quad
 \alpha=r^{\mathrm{site1}}_{s=-1,p=-1}(k_0),\quad |\alpha|=1.
\tag{W2}
\]

Here \(s=Z_1Z_2\), \(p=X_1X_2\), and \(\nu=1.459892813020969\).
The full elapsed old evolution \(e^{-itK}\), physical well scalar and common
phase are retained. No commutation of the interacting Hamiltonian with \(K\)
is assumed. The comparison contains both old qubits, both source qubits and
the entire clock output.

| Supplied apparatus and readiness | Time domain | Complete isometry error |
|---|---|---|
| Infinite half-line; exact untruncated incoming packet | Every \(t\ge2\cdot10^{13}\) | At most \(269134782504763/27062500000000000<0.009945\) |
| Infinite half-line; supplied finite packet on \(N=22\cdot10^{12}\) clock sites | Every \(t\ge2\cdot10^{13}\) | At most \(296197282504763/27062500000000000<0.011\) |
| Finite clock of \(M=9\cdot10^{14}\) sites; same finite packet and stated output embedding | \(2\cdot10^{13}\le t\le4\cdot10^{13}\) | At most \(323259782504763/27062500000000000<0.012\) |

All times and coefficients are in the declared mathematical units. The
complete unhalved output trace-distance ceiling, with any passive reference,
is twice the corresponding isometry bound, capped at two. Thus the two finite
preparation rows give strict ceilings 0.022 and 0.024. A separately certified
preparation-isometry error \(\eta_a\) would be added to the vector bound. The
displayed result supplies the mathematical ready vector exactly, so
\(\eta_a=0\) is a premise; no native emitter or preparation procedure is supplied.
The enormous support and clock sizes are sufficient arithmetic bounds. No
state or device of either size was allocated, evolved or constructed.

The stationary certificate proves only
\[
 \|R^{\mathrm{site1}}(k_0)-\alpha W\|<1.76\cdot10^{-13}.
\tag{W3}
\]
Here R(k0) denotes four logical columns at the same kinetic momentum but
old-dependent total energies 2+s+epsilon(k0); it is not a single-energy
four-open-channel scattering matrix. This fixed calibration ceiling remains
in every packet estimate. It is not an
exact equality or a proof of arbitrary accuracy below that guarantee; it is
also not a lower bound on the best possible error. The target was supplied to
the search and check. Optimizer convergence is discovery history, not evidence
for (W3) or a prediction.

## Positive two-body apparatus and exact resources

Place old1 at \((0,0,0)\), old2 at \((1,0,0)\), source \(A\) at \((0,1,0)\),
source \(B\) at \((1,1,0)\), and clock sites \(c_n=(n,2,0)\), \(n\ge0\).
Each non-onsite support below is a nearest-neighbor pair on this square ladder.
With \(n=(I-Z)/2\), \(a=|0\rangle\langle1|\), and
\(L_{AB}=a_A^\dagger a_B+a_B^\dagger a_A\), set

\[
\begin{aligned}
C&=\Delta_A n_A+\Delta_B n_B+
 h(n_A+n_B-L_{AB})+u n_A n_B,\\
G&=g_A n_A(I+X_1)+g_B n_B(I+X_2),\\
H_c&=Jn_{c_0}
 +J\sum_{n\ge0}\bigl(n_{c_n}+n_{c_{n+1}}
 -a^\dagger_{c_{n+1}}a_{c_n}-a^\dagger_{c_n}a_{c_{n+1}}\bigr),\\
H_{\mathrm{phys}}&=K+C+G+H_c
 +\lambda_A n_{c_0}(I+X_A)+\lambda_B n_{c_1}(I+X_B)
 +\mu_0n_{c_0}+\nu(I-n_{c_1}).
\end{aligned}
\tag{W4}
\]

Every displayed physical block is positive. All strengths are finite.
The entrance term \(Jn_{c_0}\) makes the one-head bulk diagonal \(2J\).
The Hamiltonian is defined on the positive finite-excitation representation;
clock number is invariant, with \(H_c\le4JN_{\rm clock}\) on each fixed-number
sector. The prepared sector has one head. No target \(W\) occurs in a hopping
bond, and no cancellation by a three-body term is used.

| Coefficient | Exact terminating decimal | Coefficient | Exact terminating decimal |
|---|---:|---|---:|
| \(J\) | 0.030021107107032 | \(g_A\) | 0.996878563816670 |
| \(g_B\) | 0.599319315560298 | \(h\) | 3.999349697888060 |
| \(\lambda_A\) | 3.801781381581202 | \(\lambda_B\) | 2.575033765788497 |
| \(u\) | 0.544607276405587 | \(\Delta_A\) | 2.192035527016003 |
| \(\Delta_B\) | 2.186826508897014 | \(\mu_0\) | 0.321494607058201 |
| \(\mu_1=-\nu\) | -1.459892813020969 | \(\cot(k_0/2)\) | 4.510351185997098 |

Every listed decimal is an exact rational coefficient, not an uncertainty
interval. The signed matching problem replaces the last physical well by
\(\mu_1 n_{c_1}\); hence \(H_{\mathrm{phys}}=H_{\mathrm{signed}}+\nu I\).
The shift changes both total-energy bands and the full evolution scalar.

The source vacuum is exactly dark for \(C+G\), and the contact flips vanish
when the head is absent. In that sector the remaining old generator is exactly
\(K\), with no added persistent old interaction. Actual finite-packet return is
approximate: both contact-site source components and every evanescent source
tail are included in (W2)'s error. Exact source return at a finite time is not
asserted.

| Site | Sum of norms of incident added positive blocks |
|---|---:|
| old1 | 1.993757127633340 |
| old2 | 1.198638631120596 |
| source \(A\) | 20.332662089993454 |
| source \(B\) | 17.078839343776311 |
| clock \(c_0\) | 8.015120691541701 |
| clock \(c_1\) | 6.730044773026091 |
| interior clock | 0.120084428428128 |

The unchanged old edge \(K\) has norm three and is counted separately.
Only added old-site loads meet the cap two. The source hopping contributes
\(2h\) at both sources; each contact contributes \(2\lambda\); the vacancy
projector contributes \(\nu\) at \(c_1\). A finite clock also includes
\(Jn_{c_{M-1}}\) to retain its final diagonal \(2J\); its far-end added load is
\(3J=0.090063321321096\). These are incident block sums, not a fabrication,
cooling, precision-control or energy-identification cost.

## Complete channels and the packet implication

The sixteen-dimensional bulk \(B=K+C+G\) reduces into two eight-dimensional
\(p=X_1X_2\) sectors. In each sector the source-vacuum eigenvalues are exactly
1 and 3. Every bulk eigenvalue \(b\) produces the band
\([b,b+4J]+\nu\). Positivity on the source-excited subspace gives
\(B\ge1+\min(\Delta_A,\Delta_B)\), there. The exact margins are

\[
 2-4J=1.879915571571872,\qquad
 \min\Delta-2-4J=0.066742080468886.
\tag{W5}
\]

Thus closure pays for the full possible old-energy release of two. For either
incident old energy and either parity there is one open channel; all seven
other channels in that parity sector are closed. The proof uses analytic
bounds, with the complete eigenvalue displays retained only as diagnostics.

The concrete interval source uses \(I_{\rm cert}=[k_0-10^{-3},k_0+10^{-3}]\).
It establishes a source gap greater than \(9/50\), closed roots
\(|q_\ell|\le1/7\), velocity \(v=1/40\), and curvature ceiling \(E_2=2J\).
Exact point residuals give \(\|M_{16}^{-1}(k_0)\|_2<164\), using complex symmetry
to pass from the certified row sums without a dimension factor. The derivative
ceiling

\[
 \|M_{16}'(k)\|_2\le
 \frac{2J}{1-(1/7)^2}=0.061293093676857
\tag{W6}
\]

and a Neumann estimate give the uniform bound \(166\).
The explicit arbitrary-right-hand-side Schur reconstruction then gives
\(\|M_{24}^{-1}\|_2\le2(166)+1/J<366\) in the generic theorem's actual
coefficient norm. This certifies an interval, not a momentum grid.

The generic proof, preserved in full below, supplies exact normalized packet
columns \(\Gamma_s\) and the identity

\[
 e^{-i(T+s)H_{\rm signed}}\Gamma_{-T}
   =\Gamma_s e^{-i(T+s)D_b}.
\tag{W7}
\]

Normalization follows from Parseval at past infinity and constancy of the
Gram matrix under the bounded evolution. No completeness assertion excluding
bound states is needed. The input-column energy matrix \(D_b\), rather than a
commutation of the interacting propagator through \(K\), gives (W2)'s literal
old aging. Integration by parts controls incoming/reflected half-line tails
and the entire localized closed-channel vector. The two localized old-energy
columns in each parity block need not be orthogonal: the bound includes their
Euclidean column sum. Orthogonal parity blocks may then be combined by a
maximum.

The reference-origin conversion is
\(r^{\rm abs}(k)=e^{-2ik}r^{\rm site1}(k)\), whereas
\(r_0^{\rm abs}(k)=-e^{2ik}\). Hence the single phase in (W2) satisfies
\(r_0^{\rm abs}(k_0)\zeta=e^{-2ik_0}\alpha\).
For the parabolic packet of half-width \(\sigma=10^{-6}\), the concrete
absolute-site derivative bound \(L=700\) gives
\(\Delta\le1.76\cdot10^{-13}+702\sigma\).
The conservative constants are
\(C_A=C_B=2001\), \(D=88000\), \(T=10^{13}\).
The generic all-future estimate is

\[
 \Delta+\frac{2(C_A+C_B)}{\sqrt{\pi vT}}
       +\frac{3D}{\sqrt{2\pi}\,vT}.
\tag{W8}
\]

The exact packet is orthogonal to point spectrum by its weak past limit.
The physical product input need not be: its possible bound-state amplitude
is already bounded by the preparation comparison. After finite truncation
the concrete ceiling is \(91279763/16237500000<0.005622\) for the infinite
operator. This statement is not transferred to a finite Hamiltonian, whose
whole spectrum is point spectrum.

Finite readiness adds \(\eta_p=10^{-3}\) by a proved Fourier-tail truncation
and positive-real renormalization. Finite apparatus comparison uses the full
internal operator: \(1\le B<20\), signed contact norm
\(V_{\max}=7.925057370220605\), and centered radius \(\rho=18\).
The physical \(\nu\) shifts only the spectral center. Polynomial locality
through degree below \(M-N+1\), followed by a Chebyshev/Bessel tail bound,
adds less than \(10^{-3}\) through \(T_{\rm obs}=4\cdot10^{13}\).
This establishes the stated finite horizon after isometrically embedding
the finite output into the half-line space. A fixed finite clock has no
all-future claim here.

## Proof, certificate and review scope

| Obligation | Mathematical source and evidence | Accepted scope |
|---|---|---|
| Positive two-body full-qubit extension, source darkness, parity and complete channel closure | Historical ROUTE plus active OLD_CAP_RESULT; exact physical-matrix checks | Supplied Hamiltonian and one-head sector; all-site cap two is false |
| Four stationary amplitudes with one common phase | Active exact rational certificate; separate full-physical-basis stationary certificate | Fixed central mismatch below \(1.76\cdot10^{-13}\), at the two old-dependent total energies |
| Uniform matching inverse, phase conversion and generic hypotheses | Concrete interval argument and exact certificate; separate interval review | Whole common interval, with candidate constants unchanged |
| Full-channel normalization, literal aging, localized-column and bound-state bounds | Complete generic V2 proof and separate generic review | Conditional operator estimate with all outputs and passive references |
| Finite preparation and finite observation window | Generic sections 9–10 and concrete arithmetic | Supplied finite vector; huge sufficient costs; horizon only for finite apparatus |
| Native coefficient supplier, emitter, general noise, exact capture, reset/reuse and Record formation | No construction supplied here | Open physical obligations or excluded conclusions |

The stationary review (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/dark_source_certificate_review/REVIEW.md`)
has SHA256 23b78506dc56fe141f9e19347b60ed0e420b4e817b599cafa246a502a2a3f830.
It independently assembled the full physical basis and exact root, inverse
and state residuals, reproducing the active point ceiling. The
generic review (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/finite_channel_wavepacket_review/REVIEW.md`)
has SHA256 bba09ef378466a3787ebfbbbd942a81fbe200031a24d04f799d2543e510673f6.
V2 changes only velocity/curvature equalities to certified lower/upper bounds,
as the proof already requires. Historical executions remain pinned to the
versions they actually read.

The later concrete review (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/two_body_interval_review/REVIEW.md`)
has SHA256
a3ab8c94ce4c842980e2144766be0994b5f5d783f29d14d1cd25a7a2567dfe8a,
with freeze 26b4295697311102b543303ef3f441dd8ef620a4eab6b34e3609a5da87b185a4.
Its new full-basis Frobenius/spectral residual calculation independently
supports the interval inverse bound and checks Schur signs, origin phase and
resource inequalities. Its single run exited zero in 2.465158416889608 seconds,
largest matrix 32, under 60 CPU-second and 90 wall-second caps. That run
rechecks root and inverse witnesses; the four point-state/reflection
amplitudes remain inherited from the pinned prior stationary review and
execution. The candidate's looser sufficient constants are unchanged.

The author interval run took 0.6565569159574807 seconds under the same caps,
with maximum computed matrix dimension 16. The 24-dimensional theorem
conversion was algebraic. No large clock evolution was used in either run.
The full source map distinguishes original author checks, independent
implementation checks, inherited point-state evidence and this drafting
task's packaging verification.

These are source-exposed same-model checks with shared target, assumptions
and, where stated, prior reviewer-owned proposals. They are not blind
discovery, model diversity, proof-assistant verification, a retained audit
or laboratory evidence. Exact rational fields and proved strict ceilings
control; older fields named upper_float are round-to-nearest displays and
must not be treated as outward enclosures.

The scientific source base is c86e61caf46c848fe8cee57ecbea6e6fdad7a4bc.
This drafting task read the packaging worktree at
f5f5eda7427453aac726b394381c965f9e28ac03, the published PR9659 branch tip.
Root later recorded main at 2bb6c1a54721e70512922fb10d4495adf8ea3042 and
scoped the authority/target provenance update in the new source qualification.
The current-main scope (`outputs/two_body_autonomous_halt_2026_10_17_inputs/integration/current_main_scope.json`)
records ten unchanged instruction sources, the unchanged original target
body and the complete narrow publication-provenance changes. No science was
merged or pushed to main by this campaign, and no audit verdict was adopted. Historical process snapshots in
the evidence pack are immutable records; editable prompts and physical
axioms are unchanged.

This is the distinct two-body source construction. The preceding
[autonomous boundary note](AUTONOMOUS_BOUNDARY_REFLECTION_BOUNDED_THEOREM_NOTE_2026-10-16.md)
used a supplied positive three-qubit boundary block. Its small loads and
accuracy-family conclusion are not imported here. This milestone is packaged against current main at
69cf6a289b2ec06213473f1549c51a57c29b6d70 after PR9659 was landed externally
and its branch deleted. Only this new milestone was rebased; its original
science parent and prior execution remain preserved historical sources. The
portability review (`outputs/two_body_autonomous_halt_2026_10_17_inputs/portability/REPORT.md`)
checks the complete code adaptation without relabeling the original runs.
Full combined-current-main pipeline, strict lint and changed-evidence checks
remain shared landing gates under conformance section12; independent retained
audit is separate. No landing is authorized or claimed here.

## Unchanged mathematical source bodies

The four complete bodies below preserve their exact source bytes, including
historical provisional and pending-review language. Later acceptance is
recorded outside them. The generic proof and concrete application appear
first; the original uncapped route supplies historical finite-algebra detail,
and the capped result supplies the selected coefficients and discovery record.
Only the capped coefficients in (W4) and the concrete application are active
in this theorem. The original route's larger loads are not substituted.

The capped result is included as a literal Markdown transcript because its
relative links belong to its original directory. Its separately preserved
rendered file remains available below. This avoids treating historical
relative links as active canonical links while leaving every source byte
unchanged. The source map records each body's exact byte interval and hash.

| Frozen body | Bytes | SHA256 |
|---|---:|---|
| Generic theorem V2 (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/finite_channel_wavepacket_bridge/THEOREM_V2.md`) | 27028 | db1a25ee639337a99800f8b8c27dbf366861a6707116f559029697c9f8aaf0e3 |
| Concrete interval application (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/two_body_interval_bridge/CANDIDATE.md`) | 23457 | b386126649516e533da29182a6cf9eac2da314538ae9b072a2262d7c5c78ed45 |
| Historical stationary route (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/dark_source_two_body_halt/ROUTE.md`) | 21276 | 04ffdf68d3bdadf17f5c0838dde2a8a2bd1608d786ea58e427c5c25fd33ef8d1 |
| Selected capped result (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/dark_source_two_body_halt/old_cap_search/RESULT.md`) | 12175 | 397c18e02c0d583bdc3e51df8f5c513f677b448862526a362eac4cc43577af00 |


<!-- BEGIN UNCHANGED SOURCE: finite_channel_wavepacket_bridge/THEOREM_V2.md; SHA256=db1a25ee639337a99800f8b8c27dbf366861a6707116f559029697c9f8aaf0e3 -->
---
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
independent_review: pending
audit_required_before_effective_retained: true
---
# From finite-channel scattering certificates to a persistent wavepacket gate

Provisional mathematical construction, 2026-10-16. This note proves a
conditional implication for the specified half-line Hamiltonian. No concrete
two-body scattering fit, interval certificate or native apparatus is supplied
here. The separate on-shell fitting worker's results were not read or assumed.

The main estimate is

    isometry error <= Delta
      + 2(CA+CB)/sqrt(pi v T) + 3D/[sqrt(2pi) v T],           (1)

for every physical elapsed time t>=2T, with s=t-T. Delta is the certified
reflection-phase mismatch over the entire packet band. D includes the
operator-norm cost of localized and closed-channel columns that need not be
orthogonal. The proof retains the actual asymptotic input energies; it never
commutes the old K through the full interaction.

## 1. Model, target and exact certificate contract

Let the finite internal Hilbert space be old plus source, and let

    iota x = x tensor Omega,
    ||Omega||=1,
    H = h0 tensor I + I tensor B
        + |0><0| tensor V0 + |1><1| tensor V1,
    h0 = 2J I - J sum(n>=0)(|n+1><n|+|n><n+1|), J>0.        (2)

B,V0,V1 are fixed finite selfadjoint matrices. H is a bounded selfadjoint
operator on the half-line one-head Hilbert space. This is the supplied
mathematical model, not a derivation of a full-qubit implementation.

Choose an orthonormal logical basis e_j, j=1,...,m, with

    u_j=iota e_j,       B u_j=b_j u_j,
    Db=diag(b_j).                                           (3)

The old-pair application has m=4 and literal K=2I+Z1 Z2, whose eigenvalues
are 1 and 3. To express (3) as literal old aging plus a common source phase,
one must additionally certify

    B iota = iota(K+bOmega I).                              (4)

Without (4) the theorem still holds, but the aging matrix is the actual Db;
one may not replace it by K. No assertion [H,I tensor K]=0 is made.

Let Q_g be orthogonal internal projections summing to identity and commuting
with B,V0,V1. Each u_j lies in one such block, denoted g(j). Different j may
belong to the same block. All following scattering work is in that block.

Fix a common kinetic-momentum interval

    I=[k0-sigma,k0+sigma] subset (0,pi),
    E(k)=2J(1-cos k),
    0<v<=min_I E'(k),      E2>=max_I |E''(k)|.              (5)

Here v and E2 are certified lower and upper bounds, respectively.
The use of one common kinetic packet is essential to the old-independent
product preparation below. Different total energy bands are allowed:
lambda_j(k)=b_j+E(k).

For each j, the finite scattering certificate must establish all of:

1. **One open channel.** In Q_g(j), u_j is the only B eigenchannel whose
   band [b_l,b_l+4J] contains lambda_j(k), for every k in I. Every other
   channel has a positive uniform closed-channel gap g_j:

       dist(lambda_j(k),[b_l,b_l+4J]) >= g_j > 0.             (6)

   Multiplicity counts: two degenerate open eigenvectors in the same block
   violate this hypothesis. Open channels in decoupled symmetry blocks do
   not matter.
2. **Finite matching.** The unit-incoming stationary solution exists, its
   row-zero convention is fixed, and the finite system specified in section
   2 is invertible on all of I with a checked inverse-norm bound. A grid
   of nonsingular matrices alone is not this certificate.
3. **Target phases.** A desired logical unitary W is diagonal in e_j,
   W e_j=omega_j e_j, with |omega_j|=1. One common phase gamma is supplied.
   Put S=exp(i gamma)W and zeta_j=exp(i gamma)omega_j. Certify

       Delta_j >= sup_(k in I) |r_j(k)-r0(k) zeta_j|,
       r0(k)=-exp(2ik),      Delta=max_j Delta_j.             (7)

   Independent per-column choices of a “global phase” are not allowed.
   This elastic one-open-channel result covers such a diagonal phase gate;
   it does not assert an arbitrary noncommuting logical W.

For the prior target W=exp(i theta)exp(i theta X1 X2), one can choose a
common K,W eigenbasis. Whether the actual B and interactions provide the
required source-vacuum eigenvectors and reducing blocks remains a concrete
certificate, not a consequence of the target's algebra.

## 2. A finite matching certificate supplies the regularity needed

Work in a block of internal dimension d_j, with fixed orthonormal B
eigenvectors u_j and v_l for the other channels. Set

    s_jl(k)=(2J+b_l-lambda_j(k))/J,
    q_jl(k)=(s_jl-sign(s_jl)sqrt(s_jl^2-4))/2.               (8)

By (6), q is real, nonzero and |q|<1. A sufficient common bound is

    a_j=2+g_j/J,
    kappa_j=(a_j-sqrt(a_j^2-4))/2 < 1,
    |q_jl|<=kappa_j,
    |q'_jl|<=Q1_j:=2 kappa_j^2/(1-kappa_j^2).               (9)

The derivative follows by differentiating q+q^(-1)=s:
q'=2 sin(k) q^2/(1-q^2). In particular
|(q^(-1))'|<=2/(1-kappa_j^2). Branch signs cannot change on I without
violating the gap. The B eigenvectors themselves are k-independent.

Write the unnormalized unit-incoming eigenfunction as

    phi_j(k,0)=x0_j(k),       phi_j(k,1)=x1_j(k),
    phi_j(k,n)=(exp(-ikn)+r_j(k)exp(ikn))u_j
                + sum_l alpha_jl(k) q_jl(k)^(n-2) v_l,
                                    n>=2.                 (10)

The unknown vector z_j=(x0_j,x1_j,r_j,alpha_j) has dimension 3d_j. Define
D_a=2J I+B+V_a-lambda_j I on the selected block. The matching equations
are exactly

    D_0 x0 - J x1 = 0,
    -J x0 + D_1 x1 - J r exp(2ik)u_j - J sum_l alpha_l v_l
        = J exp(-2ik)u_j,
    -J x1 + J r exp(ik)u_j + J sum_l q_l^(-1) alpha_l v_l
        = -J exp(-ik)u_j.                                  (11)

The last line is the n=2 equation after inserting the bulk recurrence;
equivalently it matches the exterior solution extrapolated to site 1.
All n>=3 equations are then automatic. Thus the finite system
M_j(k)z_j(k)=d_j(k) is the actual half-line eigenfunction condition.

Suppose a certificate supplies

    inf_I sigma_min(M_j(k)) >= nu_j>0.                     (12)

Since all entries are C1, this proves C1 solutions. The right-hand side
of (11) has norm sqrt(2)J and derivative norm sqrt(5)J. A sufficient
derivative bound for the matrix is

    LM_j=J sqrt[9+4/(1-kappa_j^2)^2],
    ||M'_j||<=LM_j.                                        (13)

To check (13), split the input vector into (x0,x1), r and alpha. Their
derivative images have norms at most 2J, sqrt(5)J and
2J/(1-kappa_j^2), respectively, times the corresponding input norm.
Cauchy–Schwarz over these three groups gives (13).

Consequently one may use

    X0_j=sqrt(2)J/nu_j,
    X1_j=[sqrt(5)J+LM_j X0_j]/nu_j,
    sup_I ||z_j||<=X0_j,    sup_I ||z'_j||<=X1_j.           (14)

Sharper directly certified bounds are welcome. With no closed channels,
delete the alpha terms, take LM_j=3J, and delete closed-tail terms below.

Selfadjointness supplies |r_j(k)|=1, rather than a fitted normalization.
For a stationary solution the current
2J Im<phi(n),phi(n+1)> is independent of n. The absent n=-1 bond makes
it zero at the entrance. At n>=2, orthogonality of B eigenchannels and
real q make every closed-channel current zero. The open-channel current
is 2J sin(k)(|r_j|^2-1), proving the claim. Thus

    Lj:=X1_j  is a sufficient bound on sup_I |r'_j|.         (15)

This derivation uses exact selfadjoint matrices. Approximate non-Hermitian
matching data require their own residual-to-exact-solution certificate.

## 3. Localized corrections, including the entire source output

Define c_j(k,n) by subtracting the open wave at **all** sites:

    c_j(k,n)=phi_j(k,n)-(exp(-ikn)+r_j(k)exp(ikn))u_j,
    C_j(k)=(c_j(k,n))_(n>=0).                               (16)

C_j lies in l2(N0) tensor Q_g(j). It includes both finite interaction
amplitudes at n=0,1 and all closed-channel tails. It is not a traced-out
or ignored source component. The matching certificate gives the following
explicit sufficient Hilbert-space C1 bounds:

    C0_j = sqrt[2(X0_j+2)^2+X0_j^2/(1-kappa_j^2)],

    C1_j = sqrt[(2X1_j)^2+(2X1_j+2)^2]
         + X1_j/sqrt(1-kappa_j^2)
         + X0_j Q1_j sqrt[(1+kappa_j^2)/(1-kappa_j^2)^3],

    sup_I ||C_j(k)||<=C0_j,
    sup_I ||C'_j(k)||<=C1_j.                               (17)

For the first two coordinates, use |r|=1, |r'|<=X1 and the derivatives
of exp(+-ik). For the tail, orthonormality of v_l gives
sum_(m>=0)|q_l|^(2m)=1/(1-q_l^2). Differentiating the tail produces
alpha'_l q_l^m plus alpha_l m q_l^(m-1)q'_l; use

    sum_(m>=1) m^2 kappa^(2m-2)=(1+kappa^2)/(1-kappa^2)^3.

These uniformly convergent square sums also justify differentiating in
the l2 norm, not only coordinatewise. No bound-state completeness claim
is needed. When a gap closes or nu_j approaches zero, these bounds may
become arbitrarily costly; a successful central fit does not bound them.

## 4. Packet constants and nonorthogonal columns

Choose f in W^(1,1)_0(I), ||f||_2=1, and write F0=||f||_1,
F1=||f'||_1. One explicit choice is the parabolic packet

    f(k)=sqrt(15)/(4sqrt(sigma)) [1-((k-k0)/sigma)^2]
               on I, and zero outside,
    F0=sqrt(15sigma)/3,     F1=sqrt(15)/(2sqrt(sigma)).       (18)

The interval is inside (0,pi), so v>0. The central choice k0=pi/2,
sigma<=pi/6 permits v=sqrt(3)J and E2<=2J.

Use the finite constants

    CA=F1+(E2/v)F0,
    CB=max_j [F1+(Lj+E2/v)F0],
    Dj=F1 C0_j+F0 C1_j+(E2/v)F0 C0_j,
    D=max_g sqrt(sum_(j:g(j)=g) Dj^2).                      (19)

The universally safe alternative is D=sqrt(sum_j Dj^2). The grouped
version uses only the exactly reducing Q_g. Within a group the error
columns are not assumed orthogonal. In particular D<=sqrt(m)max_j Dj,
but replacing D by max_j Dj without an additional orthogonality certificate
is unjustified.

Define vectors and column maps, with all clock sums over n>=0,

    a_s(n)=1/sqrt(2pi) integral_I f(k)exp(-ikn-iE(k)s) dk,
    b_s^j(n)=1/sqrt(2pi) integral_I f(k)r_j(k)exp(ikn-iE(k)s) dk,
    ell_j(s)=1/sqrt(2pi) integral_I f(k)C_j(k)exp(-iE(k)s) dk,
    Gamma_s e_j=(a_s+b_s^j) tensor u_j + ell_j(s).           (20)

For u>0 with vu>=1, integration by parts and the square-sum bound
sum_(n>=0)(n+vu)^(-2)<=2/(vu) give

    ||a_u|| <= CA/sqrt(pi v u),
    max_j ||b_-u^j|| <= CB/sqrt(pi v u).                    (21)

The endpoint terms vanish because f does. The phase derivative of
kn+E(k)u is at least n+vu, and its second derivative is bounded by E2 u.

For the localized component, integration by parts in the Hilbert-space
integral, using phase E(k)s, gives for s!=0

    ||ell_j(s)|| <= Dj/[sqrt(2pi) v |s|],
    ||L_s|| <= D/[sqrt(2pi) v |s|],
    L_s e_j=ell_j(s).                                      (22)

Here the derivative of 1/E' contributes E2/v inside Dj. The factor
outside is 1/(v|s|), not 1/sqrt(v|s|). The second inequality follows from
the Hilbert–Schmidt bound within each column group and orthogonality
between distinct Q_g output groups.

In contrast, the open outgoing map e_j -> b_s^j tensor u_j has exactly
orthogonal columns because the u_j are orthonormal. Its operator norm is
max_j||b_s^j||. These different treatments are intentional.

## 5. Exact normalized packet dynamics without commuting K

Put

    Psi_s=Gamma_s exp(-is Db).                             (23)

Every column is an integral of the stationary eigenfunction phi_j(k)
at its actual energy E(k)+b_j. The open-wave synthesis maps are bounded
Fourier restrictions. The localized synthesis is bounded by the Bochner
integral estimate with C0_j. Energies are bounded on I. Therefore Psi_s
is norm differentiable and satisfies i d_s Psi_s=H Psi_s strongly.
Bounded selfadjoint evolution gives

    Psi_s=exp[-i(s-r)H]Psi_r.                              (24)

On the full integer line, Parseval gives ||a_-T||=1. Its negative-site
part tends to zero by the same nonstationary phase estimate, with n=-m.
Thus its half-line norm A_T tends to one. Equations (21)–(22) show
Gamma_-T minus the map e_j -> a_-T tensor u_j tends to zero in operator
norm. Hence

    ||Gamma_-T^* Gamma_-T-I|| -> 0.

The Gram matrix Psi_s^*Psi_s is constant by (24). Conjugating the last
display by exp(iT Db) does not change its distance to identity. It follows
that

    Psi_s^*Psi_s=Gamma_s^*Gamma_s=I  for every real s.       (25)

This proves the required normalized isometries without claiming continuum
completeness or absence of bound states.

Most importantly, (23)–(24) give the exact column identity

    exp[-i(T+s)H] Gamma_-T
       = Gamma_s exp[-i(T+s)Db].                           (26)

This is an incoming-channel intertwining identity. It is not the generally
false factorization of exp(-itH) into exp(-itB) times an interaction
propagator with unchanged coefficients. No commutator of K with V0,V1
has been set to zero.

## 6. Common preparation and complete-output theorem

Choose T with vT>=1 and define

    delta_in(T)=CB/sqrt(pi v T)+D/[sqrt(2pi) v T].           (27)

Assume delta_in(T)<=1/4 and CA/sqrt(pi v T)<=1/4. Let

    A_T=||a_-T||,       chi=a_-T/A_T,
    V_ready x=chi tensor iota x.                          (28)

These are common clock/source preparations, independent of the old input.
For any unit old vector, (25) and reverse triangle inequality give
|A_T-1|<=delta_in(T), so A_T>=3/4. Consequently

    ||V_ready-Gamma_-T|| <= 2 delta_in(T).                 (29)

For the common outgoing clock, use the free reflection r0=-exp(2ik):

    b_s^0(n)=1/sqrt(2pi) integral_I f(k)r0(k)exp(ikn-iE(k)s) dk,
    beta_s=b_s^0/||b_s^0||.                               (30)

The free half-line solution a_s+b_s^0 has norm exactly one by the same
past-limit normalization proof, or by the elementary sine transform.
Hence | ||b_s^0||-1 |<=||a_s||; for s>=T it has norm at least 3/4.
Normalization in (28) and (30) is positive real. The entire Fourier and
free reflection phase is retained in beta_s.

By Parseval on the full integer line, followed by half-line restriction,

    ||b_s^j-zeta_j b_s^0|| <= Delta_j.                     (31)

The corresponding output columns lie in orthogonal u_j channels. Therefore
their aggregate operator error is bounded by Delta, with no sqrt(m) factor.
Combining (20)–(22), (30) and (31) gives

    ||Gamma_s - [x -> beta_s tensor iota Sx]||
       <= 2CA/sqrt(pi v s)+D/[sqrt(2pi) v s]+Delta,
                                                        s>=T. (32)

**Conditional wavepacket theorem.** Under (2)–(19), (27)–(28), for every
physical elapsed t>=2T and s=t-T,

    ||exp(-itH)V_ready
       - [x -> beta_s tensor iota S exp(-itDb)x]||
       <= 2 delta_in(T)+2CA/sqrt(pi v s)
                      +D/[sqrt(2pi) v s]+Delta
       <= Delta+2(CA+CB)/sqrt(pi v T)+3D/[sqrt(2pi) v T].    (33)

Proof: propagate (29) under the same H, use (26), then use (32).
Multiplication on the input by exp(-itDb) preserves operator norm. All
source and clock components remain in the comparison. This proves (1).

When (4) holds and e_j is the K,W eigenbasis, the comparator is exactly

    x -> exp(i gamma) exp(-it bOmega)
          beta_(t-T) tensor iota exp(-itK)W x.             (34)

Thus the old generator ages for the full physical time t, and both the
common fitted phase and source-vacuum dynamical scalar remain explicit.
Transient old/source mixing is included in L_s, not prohibited.

Tensoring any passive reference leaves (33) unchanged. For every normal
old/reference density, the unhalved trace-norm distance of the complete
old/source/clock/reference outputs is at most twice the right side of (33),
capped at 2. This follows by inserting the two isometries into the density
and splitting their difference into two terms. No partial trace is used.

An explicit sufficient choice for an escape contribution <=epsilon_e,
0<epsilon_e<=1, with fixed f and certificates, is

    T >= max{1/v,
       16(CA+CB)^2/(pi v epsilon_e^2),
       6D/[sqrt(2pi) v epsilon_e],
       64 CB^2/(pi v),
       8D/[sqrt(2pi) v]}.                                 (35)

The last two terms ensure delta_in<=1/4; the second term also ensures
CA/sqrt(pi v T)<=epsilon_e/4. The two travel-time terms in (1) then sum
to at most epsilon_e. If D=0, its two time constraints are zero.

## 7. Bound states and the actual prepared input

The exact packets are orthogonal to every normal bound eigenvector of H.
Indeed Gamma_-T converges weakly to zero: for each fixed clock coordinate,
the incoming phase -kn+E(k)T is nonstationary for all sufficiently large T;
the reflected and localized parts tend to zero in norm. Bounded norms then
extend this to every l2 test vector. The same holds columnwise for Psi_-T.
For a bound eigenvector v with energy lambda, (24) says the magnitude of
<v,Psi_-T e_j> is independent of T, so it must be zero. No completeness
assertion about the complementary spectrum is used.

Let Ppp be the point-spectral projection of the infinite half-line H.
The physically prepared input can have nonzero bound-state amplitude, but

    ||Ppp V_ready|| <= 2 delta_in(T).                      (36)

It remains bounded by the same number at every elapsed time because Ppp
commutes with exp(-itH). This residual is already included in (29) and
(33); it must not be silently removed or counted as a new independent
error. Other physical-input components outside the exact packet family
are likewise covered by (29). For a finite chain its entire spectrum is
point spectrum; (36) is a statement about the infinite apparatus only.

## 8. What an on-shell fit does and does not certify

Suppose the separate fit certifies at k0, using the same common gamma,

    |r_j(k0)/r0(k0)-zeta_j|<=delta0_j.                     (37)

With the interval regularity certificate (15), one may choose the certified
band-mismatch bound

    Delta = max_j [delta0_j+(Lj+2)sigma].                  (38)

Here 2 is |r0'|. Equation (38), the gap (6), the inverse bound (12), and
the actual input-energy identity (3)/(4) are separate requirements. A
central fit alone proves none of the three others. In particular it does
not bound the long-lived localized packet near a matching resonance.

Shrinking sigma can reduce the variation term while increasing F1 and the
required travel time. A positive certified upper bound delta0_j leaves
that term in the guaranteed accuracy; it is not itself a theorem that the
physical optimum has a nonzero error floor. Arbitrary accuracy for a fixed
Hamiltonian would require, for example, an exact central phase match and
fixed positive gap/inverse certificates on a neighborhood of k0. Under
those additional certificates, narrowing the packet and increasing T does
give arbitrary accuracy. No such concrete exact-fit certificate, or
uniform family of fitted hardware, is supplied in this note.

## 9. Explicit finite-support product readiness

The incoming packet is the same scalar vector for every old/source column,
so a finite-support truncation remains an independent product preparation.
For n>2JT, integration by parts in -kn+E(k)T gives

    |a_-T(n)| <= [F1/(n-2JT)+2JT F0/(n-2JT)^2]/sqrt(2pi).

For d=N-2JT>=max(1,2JT), its tail therefore obeys

    ||1_(n>=N) a_-T|| <= (F1+F0)/sqrt(pi d).                (39)

For 0<eta_p<=1/2, take

    N=ceil[2JT+max{1,2JT,16(F1+F0)^2/(pi eta_p^2)}],
    chi_N=1_(0<=n<N)a_-T / ||1_(0<=n<N)a_-T||.             (40)

The discarded norm is <=eta_p/4. Since A_T>=3/4, normalizing the
orthogonal truncation costs at most 2 times the discarded norm divided
by A_T, hence ||chi_N-chi||<=eta_p. Its retained norm is at least 5/8.
The infinite-clock bound (33) increases by at most eta_p, uniformly for
all t>=2T; the bound-state amplitude (36) also increases by at most eta_p.

Formula (40) specifies finitely many one-dimensional integrals. It does
not assert exact finite-machine emission or a native preparation algorithm.
A separately certified preparation-isometry error eta_a adds at most eta_a
to every displayed vector bound. The complete source remains Omega at
preparation and in the comparator; actual source excitation is included
in the output error.

## 10. Finite clock through an explicit horizon, without a K commutator

Let M>=max(N,2), retain sites 0,...,M-1, and use the compression H_M of H:
the scalar clock diagonal stays 2J at both endpoints. In a positive clock
bond representation this entails the usual added J n_(M-1) term. No other
full-qubit positivity or locality statement is inferred here.

Let bmin,bmax bound the spectrum of B and set

    Vmax=max(||V0||,||V1||),
    c=(bmin+bmax+4J)/2,
    rho=2J+(bmax-bmin)/2+Vmax.                              (41)

The perturbations at clock0 and clock1 have disjoint clock support, so
their sum has norm Vmax. Both H and H_M have spectrum inside
[bmin-Vmax,bmax+4J+Vmax]. Thus (H-cI)/rho and (H_M-cI)/rho are
selfadjoint contractions. This estimate uses the **full internal B and
interactions**, not an invalid factorization through old K.

An input supported on clock0,...,N-1 cannot reach the first omitted site M
in fewer than d_M=M-N+1 hops. Internal matrices and diagonal shifts do not
move clock support. Therefore degree k<d_M polynomials in these contractions
agree on the input after embedding the finite clock in the half-line.
The Chebyshev expansion of the exponential and the Bessel generating
function contour |z|=exp(mu) give, for mu>0,

    ||exp(-itH)V_N - embed exp(-itH_M)V_N||
      <=4 sum_(k>=d_M)|J_k(rho t)|
      <=4 exp[-mu d_M+rho t sinh(mu)]/[1-exp(-mu)], t>=0,   (42)

where V_N x=chi_N tensor iota x. The expansion contributes a factor 2,
and the difference of two contraction images contributes the other factor
2. The contour bound is |J_k(x)|<=exp[-mu k+x sinh(mu)] for x>=0.
This argument applies directly to the complete input isometry and any
passive reference. It does not assume old K is conserved.

For an observation horizon Tobs>=2T and tolerance zeta>0, it suffices that

    M>=max(N,2),
    M-N+1 >= [rho Tobs sinh(mu)
                +log(4/((1-exp(-mu))zeta))]/mu.            (43)

Then for every 2T<=t<=Tobs, the embedded finite output has isometry error
at most the uniform right side of (33) plus eta_p+eta_a+zeta. The complete
trace bound is twice this number, capped at 2. The common target is the
half-line beta_(t-T) with the scalar and aging in (34), or the actual Db
comparator when (4) has not been certified. This is an explicitly embedded
distance; it does not say a finite device contains the omitted output sites.
A fixed finite M is covered only through its stated horizon.

## 11. Distinct finite algebra check: column errors can align

The companion `column_norm_check.py` uses exact two-dimensional matrices:

    K=diag(1,3),       P=ones(2,2)/2,
    z=3/5+4i/5,       U=I+(z-1)P.

U and I are both isometries, but their error E=U-I satisfies

    E*E=(2/5)ones(2,2),
    max_j ||E e_j||^2=2/5,    ||E||^2=4/5.

Thus orthogonal actual and comparator columns do not make their error
columns orthogonal. The sum-of-column-squares operator bound is sharp in
this example. Also [K,P]!=0. This exact check resolves the specific risk
of replacing D by a maximum merely because the incident old states are
orthogonal. It is not a scattering fit or a certificate for (6), (12) or
(37). The full output and execution/source identities are in
`check_stdout.txt` and `CHECK_EXECUTION.json`. The calculation uses SymPy
exact arithmetic, dimension 2, a 10 CPU-second and 30 wall-second cap.

## 12. Provenance, status and next certificates

The one-channel prior context is the frozen boundary-reflection
`CANDIDATE_V2.md`, SHA256
`694484853b731991d97f11f5d9a3a012ff30b9badb7fe57a7c57f6fee7e2fd36`,
and `FINITE_READINESS_ADDENDUM.md`, SHA256
`ce01691b49abf924d2fc610cf2dd6c71c565c0c21df6f1bc39960ecb2c546a2f`.
Their methods supply context, not the new multi-channel certificates.
The present proof rederives the needed normalization and tail estimates,
adds closed-channel/interaction-site decay, and uses (26) to replace the
old global commutation argument. Standard tools used with their hypotheses
shown are Fourier Parseval, integration by parts, bounded selfadjoint
evolution, finite matrix inversion, and the explicit Chebyshev/Bessel
expansion. No framework primitive or observed physical value is used as a
hidden premise. The supplied Hamiltonian and preparations are conditional
model assumptions; no new framework axiom is proposed.

Scope of prior search: a local textual search in the current correlation
worktree docs for nearby combinations of scattering, wavepacket and
closed-channel terms returned no matches. It was not a complete repo or
literature search; no novelty claim follows. The explicit task prohibited
Git and network calls. The procedural snapshot was the already identified
science workflow at SHA256
`71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3`.

This is a new author derivation, separate from the earlier source-exposed
reviewer role. It has not received independent mathematical review. The
finite algebra check is an author check of a distinct load-bearing risk;
it does not independently certify the whole theorem. The result supplies
a conditional analytic bridge for a future scattering certificate. It does
not promote the independently pursued numerical fit or establish native
hardware, reset/reuse, a selected Record, energy-resource pricing, arbitrary
noise robustness or any actual uniform fit family.

The remaining concrete obligations for use on a fitted device are:

1. Freeze the actual B,V0,V1 and source-vacuum embedding, prove exact
   selfadjointness and reducing symmetries, and verify (3). Verify (4)
   before using literal K plus one source scalar in the comparator.
2. Certify exactly one propagating eigenchannel in each relevant block
   throughout a common kinetic interval, with explicit positive gaps (6).
3. Build the actual matching matrices (11), certify nu_j>0 over that
   interval, and obtain explicit constants (14)–(19). Near-zero matching
   singular values are a resource cost, not a negligible fit detail.
4. Certify the actual reflection convention and target phases with one
   common gamma, preserving the nonzero residuals. Supply (7) directly or
   a valid combination of (15) and (37). A finite central fit alone is
   insufficient; exact or uniform accuracy remains unestablished unless
   separately certified.
5. Choose a single f,T and finite preparation specification from the
   resulting constants. If the apparatus is finite, certify its actual
   compression/endpoint term and choose its horizon from (41)–(43).
6. Independently check this bridge before substantial downstream reliance.
   Separately establish any strict two-body full-qubit realization,
   invariant one-head subspace, native readiness or physical interpretation.

The next decision is quantitative: insert genuine interval certificates,
compute Delta and the constants, and compare the resulting accuracy and
resource bound with the actual target. No existing fit is declared to have
met these obligations.
<!-- END UNCHANGED SOURCE: finite_channel_wavepacket_bridge/THEOREM_V2.md -->

<!-- BEGIN UNCHANGED SOURCE: two_body_interval_bridge/CANDIDATE.md; SHA256=b386126649516e533da29182a6cf9eac2da314538ae9b072a2262d7c5c78ed45 -->
---
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
independent_review: pending
audit_required_before_effective_retained: true
---
# An explicit interval certificate for the fixed old-cap ladder

The frozen old-cap stationary witness satisfies the finite-channel bridge's
scattering hypotheses on the nonzero common interval

    Icert=[k0-10^-3,k0+10^-3],
    k0=2 arctan(1/q), q=4.510351185997098 exactly.           (1)

The following are uniform, rigorously bounded quantities, not values from a
momentum grid:

| Quantity | Sufficient bound on Icert |
|---|---:|
| Gap from each incident energy to every other channel band | >=0.18 |
| Closed root magnitude | <=1/7 |
| Physical-basis 16 by 16 matching inverse, spectral norm | <166 |
| Bridge's 24 by 24 matching inverse, spectral norm | <366 |
| Bridge matching minimum singular value | >1/366 |
| Absolute-site reflection derivative | <=700 |
| Localized correction norm and derivative | <=31 and <=2700 |

Using the root-qualified provisional bridge `THEOREM_V2.md` at frozen SHA256
`db1a25ee639337a99800f8b8c27dbf366861a6707116f559029697c9f8aaf0e3`,
these certificates give the finite preparation and complete-output example
in section 7: isometry error below 0.011 for every elapsed time t>=2*10^13
on the infinite half-line. A finite clock of 9*10^14 sites gives error below
0.012 through t=4*10^13. These large sufficient costs are analytic bounds,
not simulated device sizes or optimized resources.

The generic bridge has received a separate check and root acceptance for
conditional provisional use. This concrete composition is a new source-exposed
author calculation awaiting its own separate check. Its interval certificate
is explicit; its wavepacket conclusion remains conditional on the analytic
bridge and on supplying the stated Hamiltonian and preparation. No arbitrary
exact accuracy, native clock generator, all-site cap 2, retained audit status,
or hardware closure is claimed.

## 1. Fixed physical model and exact input identity

Use the square ladder from the frozen `inputs/RESULT.md` and `inputs/ROUTE.md`:
old1=(0,0,0), old2=(1,0,0), A=(0,1,0), B=(1,1,0), and clock sites
c_n=(n,2,0). All listed non-onsite blocks are nearest-neighbor two-body blocks.
Let n=(I-Z)/2, a=|0><1|, L_AB=a_A^dagger a_B+a_B^dagger a_A, and

    K=2I+Z1 Z2,
    C=DeltaA nA+DeltaB nB+h(nA+nB-L_AB)+u nA nB,
    G=gA nA(I+X1)+gB nB(I+X2),
    B=K+C+G,
    VA=lambdaA(I+XA)+mu0 I,
    VB=lambdaB(I+XB)+mu1 I.                                (2)

The following terminating decimals are exact:

| Parameter | Value | Parameter | Value |
|---|---:|---|---:|
| J | 0.030021107107032 | gA | 0.996878563816670 |
| gB | 0.599319315560298 | h | 3.999349697888060 |
| lambdaA | 3.801781381581202 | lambdaB | 2.575033765788497 |
| u | 0.544607276405587 | DeltaA | 2.192035527016003 |
| DeltaB | 2.186826508897014 | mu0 | 0.321494607058201 |
| mu1 | -1.459892813020969 | nu=-mu1 | 1.459892813020969 |

In the supplied one-clock-head sector the physical Hamiltonian is

    Hphys=h0 tensor I+I tensor B+P0 tensor VA+P1 tensor VB+nu I,
    h0=2J I-J(S+S*),       Pn=|n><n|.                     (3)

The physical well is nu(I-n_c1), rather than a negative physical block.
The clock's positive bond representation contains the entrance term J n_c0,
which is required for the constant diagonal 2J. C, G, both contact blocks,
mu0 n_c0, the vacancy block, and all clock bonds are positive. Clock number
is conserved by the full qubit Hamiltonian. The supplied one-head and
finite-excitation representation assumptions are those of the frozen route.

For Omega=|00>_AB and iota x=x tensor Omega,

    B iota=iota K,
    (B+nu I)iota=iota(K+nu I).                             (4)

This holds exactly because C+G annihilates the source vacuum. The calculation
checks it in the complete sixteen-dimensional old/source basis, not only at
one incident energy. It also checks exact reduction by p=X1 X2. Within a
parity block use the normalized old vectors proportional to
|00>+p|11> and |10>+p|01>, with s=Z1 Z2=+1 and -1 respectively. There are
two independent incident logical columns per parity block.
The code orders source before old; the fixed tensor-factor swap to iota's
notation is unitary and does not change any of the norms.

No commutator [Hphys,K]=0 is assumed: the contact-excited source allows G to
mix the two old energies locally. The full operator is static; actual old
aging in the comparator will be e^(-itK), for the entire elapsed time t.

## 2. Uniform closed-channel gaps without numerical eigenvectors

Let epsilon(k)=2J(1-cos k), lambda_s(k)=2+s+epsilon(k), with nu added to
both sides for the physical energies. At k0, cos k0 and sin k0 are exactly
(q^2-1)/(q^2+1) and 2q/(q^2+1). The program reads these rational strings
and checks the trigonometric identity and epsilon0 exactly.

Since |epsilon'|<=2J, on Icert one has the exact rational bounds

    epsilon0-2J/1000 <= epsilon(k) <= epsilon0+2J/1000,
    epsilon(k) lies between 0.005566295300504832... and
                            0.005686379728932960....       (5)

The decimals in explanatory displays are not outward interval endpoints;
the rational expressions in (5) and `CERTIFICATE.json` control the proof.
Sin k>=sin k0-1/1000 gives

    epsilon'(k)>=2J(sin k0-1/1000)>0.02531671586811827,
    v=1/40 is a valid lower bound,  E2=2J,  E2/v<5/2.       (6)

The interval is inside (0,pi): sin k0>1/1000, together with the Lipschitz
bound for sine, excludes either endpoint. Each source-excited eigenvalue
of B is at least 1+min(DeltaA,DeltaB), because K>=I, the penalty is at least
min Delta on that subspace, and the other blocks are positive. Source number
is preserved by B. Thus the least source-band gap, occurring for s=+1, is
at least

    min Delta-2-(epsilon0+2J/1000)
      = 0.18114012916808103... > 9/50.                    (7)

The two old-vacuum bands are separated by the exact number
2-4J=1.879915571571872. This is also a valid lower bound for the separation
of each incident energy from the other old-vacuum band on Icert. Every parity
sector therefore has exactly one open channel for each chosen incident energy;
all seven other channels are closed. All source outputs are included.

For any closed eigenchannel b define q_b by

    q_b+q_b^-1=(2J+b-lambda_s(k))/J,   q_b real, |q_b|<1.

The common gap g=9/50 gives

    2+g/J > 1/7+7,
    |q_b|<=kappa=1/7,
    |q_b'|<=2 kappa^2/(1-kappa^2)=1/24.                   (8)

The roots and the underlying spectral projections vary regularly: the
eigenvectors of the fixed B can be chosen once, while no threshold is crossed.
There is no dependence here on the rounded eigenvalue lists in the route.

## 3. From the exact point certificate to a uniform physical inverse

Write M16 for the witness's matching matrix in the physical parity basis:

    M16(k) = [[lambda_s-2J-B_p-VA, J I8],
              [J I8, F_p(lambda_s)-VB]],
    F_open=-J exp(-ik),       F_closed=-J/q_b.             (9)

The companion code replays the point certificate from its exact rational
parameters, with no optimizer or binary64 parameter reconstruction. Mpmath
at 90 digits proposes source square roots, inverses and states; they are
rounded to denominator 10^55. Exact Fraction residuals certify them.

For a positive candidate square root S_hat of A=D^2-4J^2 I, with certified
positive lower bounds a for the true root and b for S_hat, the Sylvester
identity gives ||S_hat-sqrt(A)||2<=||S_hat^2-A||2/(a+b). The code uses
a=d-2J and b=d-||S_hat-D||infinity. Symmetry bounds the residual spectral
norm by the row sum; sqrt(6)<3 converts the six-dimensional F error to an
infinity-norm bound. The other closed vacuum channel is treated by the
scalar analogue. Exact inverse and state residuals then give the Neumann
certificate for the true M16. All root and inverse proposal matrices are
saved in `POINT_WITNESSES.json`.

The replay reproduces the four point inverse bounds:

| (s,p) | Certified infinity-norm ceiling, decimal display |
|---|---:|
| (+1,+1) | 163.9029010203209... |
| (-1,+1) | 154.9928305605314... |
| (+1,-1) | 128.4349384249287... |
| (-1,-1) | 124.1992107742216... |

In particular, exact rational comparisons establish a common ceiling 164.
The true matrix is complex symmetric: B_p and the closed spectral function
are real symmetric, and the open term is diagonal in the real vacuum basis.
Its inverse is complex symmetric too. Consequently its ordinary modulus
induced norms satisfy ||M16^-1||1=||M16^-1||infinity, and

    ||M16(k0)^-1||2
       <=sqrt(||M16^-1||1 ||M16^-1||infinity)<164.          (10)

The certificate's row sums |Re|+|Im| dominate the ordinary modulus row sums.
Thus (10) does not incur an undocumented dimension factor.

On Icert, differentiating the spectral entries gives

    |F_open'|=J,
    F_closed'=2J sin(k)/(1-q_b^2),
    ||M16'(k)||2 <= 2J/(1-kappa^2)
                  = 0.061293093676857 exactly.            (11)

M16' is block diagonal, so this is a spectral-norm bound in the physical
basis, regardless of a numerical eigenvector basis. Therefore

    eta=164*(2J/(1-kappa^2))*10^-3
       =0.010052067363004548...<1,
    sup_Icert ||M16(k)^-1||2
       <=164/(1-eta)=165.6652785395908...<166.             (12)

This Neumann argument proves invertibility at every momentum in the interval.
It is not an extrapolation from a nonsingular grid.

## 4. Conversion to the bridge's exact 24 by 24 convention

The bridge uses unknowns z=(x0,x1,r,alpha) with d=8, dimension 3d=24.
Its exterior wave at n>=2 is

    (exp(-ikn)+r exp(ikn))u + sum_l alpha_l q_l^(n-2) v_l.

To establish the norm conversion without uncertified eigenvectors, choose
any fixed orthonormal B_p eigenbasis with open vector u. On the d-dimensional
coefficient vector y=(r,alpha), define

    Amap y = exp(ik)r u+sum_l q_l^-1 alpha_l v_l,
    Emap y = exp(2ik)r u+sum_l alpha_l v_l,
    Qlead=Emap Amap^-1
         =exp(ik)|u><u|+sum_l q_l |v_l><v_l|.              (13)

Then ||Amap^-1||2=1 and ||Qlead||2=1. For arbitrary right-hand side
f=(f0,f1,f2), the bridge's three matching rows read

    D0 x0-J x1=f0,
    -J x0+D1 x1-J Emap y=f1,
    -J x1+J Amap y=f2,     Da=2J+B_p+Va-lambda_s.          (14)

Eliminating y gives exactly

    M16 [x0;x1] = -[f0; f1+Qlead f2],
    y=Amap^-1 x1+J^-1 Amap^-1 f2.                        (15)

Indeed D1-J Qlead=-(F_p-VB), using q+q^-1 and z+z^-1 in the closed and
open channels respectively. This checks the Schur-complement signs as well
as the norm conversion. The right side for [x0;x1] has norm at most
sqrt(2)||f||. Stacking x and Amap^-1 x1 costs another factor sqrt(2), and
the last term of y costs at most J^-1||f||. Hence

    ||M24^-1||2 <= 2*166+J^-1
                =365.3098974809548...<366.                (16)

All basis changes on the internal rows and x coordinates are unitary, and
the coefficient basis for y is orthonormal. This is the bridge's actual
Euclidean norm convention, not a comparison between unrelated row norms.

Use nu24=1/366. The bridge's matrix derivative estimate gives

    LM24=J sqrt(9+4/(1-kappa^2)^2)<11/100,
    X0=sqrt(2)J/nu24<16,
    X1=[sqrt(5)J+LM24*16]/nu24<700.                        (17)

These exact inequalities certify the scattering unknowns and derivatives.
Conserved flux gives |r|=1, so L=700 bounds |r'|. Substitution in the
bridge's full localized correction (both contact sites and every closed
tail) gives C0=31 and C1=2700 as valid ceilings. The code checks these
inequalities by squaring positive rational bounds, without treating a
floating square root as an enclosure. In particular it includes the
closed-tail derivative sum

    sum_(m>=1) m^2 kappa^(2m-2)
       =(1+kappa^2)/(1-kappa^2)^3.

## 5. Reflection origin and the single common phase

The witness's incident wave is exp[-ik(n-1)] and its reflected wave is
r_site1 exp[ik(n-1)]. Multiplying the entire stationary column by exp(-ik)
normalizes the absolute-site incident wave to exp(-ikn). Thus

    r_abs(k)=exp(-2ik) r_site1(k).                         (18)

The free boundary is at n=-1, so its site-1 reflection is -exp(4ik).
In the bridge's absolute-site convention it is r0(k)=-exp(2ik). An exact
finite algebra check sets the free contact values to x0=z-z^3, x1=1-z^4;
the two rows of (9) give [0;2iJ sin k] identically. The code checks this
with the exact rational z0 and also checks the scalar identity below.

Let alpha be the exact unit-modulus witness coefficient
r_site1_(s=-1,p=-1)(k0). The target is

    W=((9+12i)I+(-16+12i)X1X2)/25,

with eigenvalues w_+=(-7+24i)/25 and w_-=1. It commutes with K, so the
chosen (s,p) basis is their common eigenbasis. The single scalar required
by the bridge is

    zeta=exp(i gamma)=-exp(-4ik0)alpha,     |zeta|=1.       (19)

In fact r0(k0)zeta=exp(-2ik0)alpha. Thus the certified central comparison
is transferred unchanged, in all four old channels, to

    max_(s,p) |r_abs_(s,p)(k0)-r0(k0)zeta w_p|
       <= exact stored rational bound
       =1.752474830885985...*10^-13 < 1.76*10^-13.         (20)

The new replay reproduces the frozen rational bound. It does not assume
exact central matching or fit separate phases for different old energies.
The rational approximation to zeta and its error below 3*10^-52 are stored
in the certificate, but the theorem comparator uses the exact unit scalar
defined in (19). The separate physical scalar remains exp(-i nu t).

On any packet interval |k-k0|<=sigma<=10^-3, (17) and |r0'|=2 give

    Delta <= 1.76*10^-13+702 sigma.                        (21)

At the full certificate width this is a loose 0.702000000000176 ceiling;
the resource example uses sigma=10^-6, giving
Delta<=0.000702000000176. The positive central ceiling remains in every
guaranteed accuracy statement. It is neither an exact fit nor a lower bound
on the true optimum. No arbitrary-accuracy family is inferred.

## 6. Complete wavepacket comparator and bound-state residual

Choose the bridge's normalized parabolic packet on
Ipacket=[k0-10^-6,k0+10^-6]:

    f(k)=sqrt(15)/(4sqrt(sigma))*(1-((k-k0)/sigma)^2),
    sigma=10^-6,           ||f||2=1,
    F0=||f||1<1/750,       F1=||f'||1<2000.                (22)

With (6), (17), C0=31 and C1=2700, valid common packet constants are

    CA=CB=2001,
    Dj <= 2000*31+(2700+(5/2)*31)/750
        =62003.703333333...,
    D=88000 > sqrt(2) max_j Dj.                            (23)

There are two incident old-energy columns per parity block. Their localized
errors need not be orthogonal; (23) explicitly pays the square-sum cost.
Outputs in the two different parity blocks are orthogonal. The propagating
columns, which end in distinct orthonormal vacuum old states, are orthogonal
and use the maximum phase error in (21), with no additional square root.

Define the scalar incoming packet and free outgoing packet by

    a_-T(n)=1/sqrt(2pi) integral f(k)exp[-ikn+i epsilon(k)T] dk,
    b_s^0(n)=1/sqrt(2pi) integral f(k)r0(k)
                                      exp[ikn-i epsilon(k)s] dk,
    chi=a_-T/||a_-T||,    beta_s=b_s^0/||b_s^0||.           (24)

The norms are taken on n>=0 and normalized by positive real numbers.
For the old-independent ready isometry V_ready x=chi tensor iota x, the
bridge supplies, for every elapsed t>=2T,

    ||exp(-it Hphys)V_ready - Uideal(t)||
       <= Delta+2(CA+CB)/sqrt(pi v T)+3D/(sqrt(2pi) v T),
    Uideal(t)x = zeta exp(-i nu t)
                 beta_(t-T) tensor iota exp(-itK) W x.    (25)

This retains all old, source and clock amplitudes. The exact bridge's
incoming-channel intertwining identity supplies the aging in (25); it
does not commute K through the full interaction. Transient source excitation
and all closed-channel tails are bounded by the localized correction.

Its normalization argument does not assume a complete scattering basis or
absence of bound states. The exact packet columns are orthogonal to point
spectrum. The supplied product input can have residual point-spectrum
amplitude at most

    2 delta_in(T),
    delta_in(T)=CB/sqrt(pi v T)+D/(sqrt(2pi) v T).           (26)

This contribution remains for all elapsed times and is already included in
(25). It is not removed by postselection or by discarding the source.
All operator bounds persist with an arbitrary passive reference; the complete
unhalved output trace-norm distance is at most twice the isometry bound.

## 7. One explicit finite readiness and finite-clock example

Take T=10^13 in the dimensionless time units of (2). The code proves the
following ceilings using only pi>3, sqrt(2pi)>12/5, and
866000^2<3vT:

    delta_in(T) <= 75042263/32475000000,
    RHS of (25) <=269134782504763/27062500000000000.        (27)

Their rounded displays are 0.002310770223248653 and 0.009944934226503945.
Both readiness normalization conditions in the bridge are comfortably met.
For eta_p=10^-3 choose the integer

    N=22000000000000,
    chi_N=1_(0<=n<N)a_-T / ||1_(0<=n<N)a_-T||.             (28)

This N satisfies the stronger rational version of the bridge's sufficient
cutoff inequality:

    N-2JT >= max(1,2JT,16(F1+F0)^2/(3 eta_p^2)).           (29)

Since pi>3, the actual omitted norm is at most eta_p/4; positive-real
normalization then gives ||chi_N-chi||<=eta_p. This specifies a finite
one-head vector by finitely many integrals, independent of the old input,
with source exactly Omega. It assumes that vector is supplied. It provides
no native preparation, emission or calibration algorithm. A preparation
isometry error eta_a would add eta_a to the following bounds; the displayed
example uses the specified exact mathematical vector, eta_a=0.

For V_N x=chi_N tensor iota x and the infinite Hamiltonian, the result is

    sup_(t>=2*10^13) ||exp(-it Hphys)V_N-Uideal(t)||
       <=296197282504763/27062500000000000 < 0.011.        (30)

The complete unhalved trace-norm distance is consequently below 0.022.
The infinite apparatus's point-spectrum amplitude is at most
91279763/16237500000<0.005622, uniformly in time, including the truncation
error. This is not an absence-of-bound-states assertion. For a finite clock
its entire spectrum is point spectrum, so that projection statement is
only about the infinite operator.

For a finite-clock version use sites 0,...,M-1, M=900000000000000, and
the compression of (3). The positive clock-bond realization includes the
far endpoint term J n_(M-1), preserving the diagonal 2J there. No additional
old or source contact is introduced. On the complete internal space,

    I<=B<=[3+DeltaA+DeltaB+2h+u+2gA+2gB]I<20I,
    Vmax=max(||VA||,||VB||)=7.925057370220605,
    rho=18>2J+(20-1)/2+Vmax.                              (31)

The physical nu shifts the spectral center by nu and leaves rho unchanged.
The first omitted clock site is M; from support 0,...,N-1 its shortest
path has exactly

    dM=M-N+1=878000000000001

hops. Onsite internal mixing does not shorten that path. The bridge's
Chebyshev bound at mu=1 is

    ||exp(-itHphys)V_N-embed exp(-itHphys_M)V_N||
       <=4 exp[-dM+rho t sinh(1)]/(1-exp(-1)).             (32)

For Tobs=4*10^13, zeta_boundary=10^-3, the exact rational inequalities
sinh(1)<6/5 and log[4/((1-exp(-1))*10^-3)]<9 imply that it suffices to
have dM>rho Tobs*(6/5)+9. The chosen integers satisfy this. The elementary
exponential estimates are checked from 8/3<e<11/4, with the latter obtained
from the first five Taylor terms and a geometric bound on the tail.

For every 2*10^13<=t<=4*10^13, the embedded finite output therefore has

    complete isometry error
       <=323259782504763/27062500000000000 <0.012,
    complete unhalved trace error <0.024.                  (33)

The comparator is the half-line state Uideal(t), with the same scalar and
aging. A finite M is covered through this stated horizon only. No chain of
these sizes was allocated or simulated. The bounds are deliberately loose
finite analytic costs and provide no feasible apparatus claim.

## 8. Resource scope, execution and remaining obligations

The fixed witness's added incident positive-block norm sums remain:

| Site | Added sum |
|---|---:|
| old1 | 1.993757127633340 |
| old2 | 1.198638631120596 |
| source A | 20.332662089993454 |
| source B | 17.078839343776311 |
| c0 | 8.015120691541701 |
| c1 | 6.730044773026091 |
| later clock sites | 0.120084428428128 |

The existing old edge has norm 3 and is additional. The old added cap 2
is met; source and boundary-clock caps of 2 are not. No optimization of
these costs, preparation cost, full-qubit operator norm over all clock
number sectors, or physical units is supplied. Static coefficients have
zero runtime slew but their installation and precision are assumptions.

`certify_interval.py` exited 0 in the single recorded execution; the wrapper
elapsed time was 0.657 seconds. The cap was 60 CPU seconds and 90 wall
seconds. The largest executed matrix was 16 by 16, source square roots were
6 by 6, and the 24-dimensional matching bound was proved by (13)-(17), not
by uncertified eigenvector numerics. Python 3.13.5, NumPy 2.4.4 and mpmath
1.3.0 were used; exact certification arithmetic was Python Fraction.
The requested BLAS/OMP thread counts were 1, without a claim of measured
hardware thread use. No search or interval grid was run.

The exact rational certificate, full stdout/stderr, actual command/runtime,
source hashes and rational point witnesses are preserved in `CERTIFICATE.json`,
`certificate.stdout`, `certificate.stderr`, `EXECUTION.json`,
`SOURCE_MANIFEST.json`, and `POINT_WITNESSES.json`. Numeric JSON displays are
named `display_float`; they are not outward enclosures and are never read
back as proof bounds. The input identities include the complete frozen
route, capped result, point verifier, point certificate and bridge. The
central replay follows the source-exposed point verifier's residual method;
it is not independent discovery or independent review. The phase-convention
algebra and Schur norm reconstruction address distinct additional risks.

The original execution read the immutable generic `THEOREM.md` at SHA256
`fffd7d405935226aba4a5e6528112b984b6dde4580747641159f554e97e2189a`.
Its actual run pins remain unchanged. The subsequent controlling V2 changes
only equation (5) to permit certified bounds 0<v<=min E' and E2>=max|E''|,
with one explanatory sentence. Those are precisely the inequalities already
used by this calculation. `BRIDGE_V2_DELTA.json` records the complete checked
diff and identities, and `inputs/THEOREM_V2.md` saves the controlling source.
No original evidence has been relabeled as a V2 execution. Root qualification
was read from `root_followup_qualification/QUALIFICATION.md` and
`ACCEPTANCE.json`; this note does not claim to have reread its full separate
review reports.

There is no remaining interval-existence, gap or matching-inverse obligation
for these exact coefficients within the stated conditional model: the
explicit bounds above provide them. The remaining dependencies are a separate
check of this concrete composition, exact physical coefficient/symmetry
realization, supplying the independently specified finite
ready vector, and any requested native-generation or physical interpretation.
No new prompt, axiom, retained claim, audit result, Git state or PR was changed.
The note does not assert reset, reuse, exact finite-time capture, a selected
classical Record, noise robustness, an all-site cap, or arbitrary exact
accuracy below the fixed central calibration ceiling.
<!-- END UNCHANGED SOURCE: two_body_interval_bridge/CANDIDATE.md -->

<!-- BEGIN UNCHANGED SOURCE: dark_source_two_body_halt/ROUTE.md; SHA256=04ffdf68d3bdadf17f5c0838dde2a8a2bd1608d786ea58e427c5c25fd33ef8d1 -->
# Dark-vacuum two-body ladder: a certified on-shell approximation to W

Status: conditional mathematical support for a stationary scattering fiber.
The normalizable-input, all-future autonomous-operation theorem remains open.
This is an exploratory source proposal, with author calculations and a different
assembly/path check; it has no independent reviewer or retained audit status.

There is a concrete finite-coefficient, strictly nearest-neighbor two-body
Hamiltonian whose four elastic reflection amplitudes at one specified momentum
obey

    ||R(k0) - alpha(k0) W|| < 5.2e-13,
    W = ((9+12i)I + (-16+12i)X1X2)/25,
    alpha(k0) = r_(s=-1,p=-1)(k0), |alpha(k0)| = 1.

The bound is certified by exact rational residual calculations, not by the
optimizer's convergence report. Both old energies, both XX labels, all source
channels and the clock reflection phase are retained. No W is put in a hopping
bond. The source vacuum is exactly dark away from the two clock contacts.

This supplies a useful stationary ingredient for the renewal5 target. It does
not yet replace PR9657's external stop: a plane wave is not a normalizable ready
clock, the apparatus uses an infinite half-line, the added strength budget is
larger than PR9656's, and finite-time source return has not been bounded here.
No arbitrary-accuracy family follows from this one calibrated point.

## Source contract and provenance

The sole campaign contract is the frozen copy in `sources/TARGET_CONTRACT.md`,
originally at
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/worktree/.claude/science/physics-loops/toe-dynamics-bridge-20261009/TARGET_CONTRACT.md`.
This ROUTE file is the requested worker deliverable, not a replacement campaign
checkpoint. All writes are confined to this worker directory.

Scientific source revision: `c86e61caf46c848fe8cee57ecbea6e6fdad7a4bc` in
`correlation_worktree`. Supplied current-main authority:
`5b0e1cc44f422fb0138b02eb071d3d16b40dfbb2`. No network refresh was authorized.
`sources/MANIFEST.json` binds the saved exact source bytes. In particular:

- PR9656 note, `PRODUCT_SOURCE_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-16.md`:
  SHA256 `4e68ea3c55620eb0ad3c721084780d2af44bc5eaa249cb8c205e516575189d20`.
  Its construction, scalar, product source, window, resource limits and
  controlling qualifications were read, principally lines17-220 and579-700.
- PR9657 note, `PRODUCT_SOURCE_CONTROLLED_STOP_BOUNDED_THEOREM_NOTE_2026-10-16.md`:
  SHA256 `b25d812dc1a4cdad2959f003ddd36346f2de0058292c74c7d0e07c9c5e395a4d`.
  Its overview, external-stop/C1 arguments and controlling qualifications were
  read, principally lines19-66,161-293,1123-1160. Its external switch-off and
  exact-zero endpoint are the interface being replaced, not resources obtained
  by this calculation.
- The current science workflow, physics-loop entry point and relevant
  Discovery/Claim Status/Delivery references were read. The installed skill
  entry point differed from the chosen repository revision; the repository
  entry point was then read and used. Its three read references were identical.
  The task's explicit no-network/no-commit/no-PR and sole-checkpoint instructions
  control delivery. No full campaign or audit workflow was launched.

The present scattering calculation does not import PR9656's perturbative
corrector theorem: it uses the literal K and target W as its design specification.
The registered primitive list was inspected. None of its units, kinetic-isotropy
or pointwise-state primitives supplies these dimensionless couplings, a ready
clock, a Hamiltonian law or a source preparation mechanism; those remain stated
conditional resources. No primitive or axiom is added.

A bounded local prior-art search at the supplied main ref used
`dark.{0,30}vacuum|vacuum.{0,30}dark|closed.{0,20}channel|multichannel.{0,20}scatter`
and `scattering.{0,30}(clock|mediator)|boundary.{0,30}reflection|reflection.{0,30}phase`
over `docs/*.md`. The returned lines concerned cosmology, unrelated channel
closure, reflection positivity, lattice-gas clocks or finite spin clocks.
They did not supply this dark-source stationary construction. This is not a
global novelty claim. The contract's existing half-line gate-bond clock remains
prior art for approximate completion, and is not rebranded as the present result.

## Physical operator and square-ladder embedding

Put old1=(0,0,0), old2=(1,0,0), A=(0,1,0), B=(1,1,0), and clock site
c_n=(n,2,0), n=0,1,... . Every non-onsite term below lies on a cubic nearest-
neighbor edge. There are six entrance qubits and an infinite blank clock tail.

Let n=(I-Z)/2 and a=|0><1|. Write h for the auxiliary hopping coefficient and
tau for physical time. Define

    K = 2I + Z1 Z2,
    L_AB = a_A^dagger a_B + a_B^dagger a_A,
    C = DeltaA nA + DeltaB nB + h(nA+nB-L_AB) + u nA nB,
    G = gA nA(I+X1) + gB nB(I+X2),
    H_clock = J n_c0
            + J sum_(n>=0)[n_cn+n_c(n+1)
                            -a_c(n+1)^dagger a_cn-a_cn^dagger a_c(n+1)],
    H = K + C + G + H_clock
        + lambdaA n_c0(I+XA) + lambdaB n_c1(I+XB)
        + mu0 n_c0 + nu(I-n_c1),       nu=-mu1>0.

Every displayed physical block is positive. The hopping block has source
eigenvalues 0,0,2h,2h; nA(I+X1), nB(I+X2) and the clock/source blocks are
positive because their commuting factors are positive. No projector on the
global one-head sector appears in H. Clock number is preserved, and the
operation is considered in its supplied one-head input sector.

In that sector H_clock is exactly `2J I - J(S+S*)` on the half-line, with a
Dirichlet boundary at -1. The endpoint `J n_c0` is essential for its constant
2J diagonal and is included in the resource count. Fixed clock-number sectors
are bounded, with `0<=H_clock<=4J N_clock`. Adding the finite old/source and
contact operators gives bounded positive restrictions; their orthogonal direct
sum is a nonnegative selfadjoint realization on the finite-excitation clock
representation. The infinite prepared tail and this representation are supplied.

For source vacuum v=|00>, `(C+G)(psi tensor v)=0` exactly for every old psi.
When neither clock contact is occupied, the source cannot be excited and the
added old interactions vanish on that sector. There is no persistent effective
old interaction hidden in a dark-sector energy shift. The old term remains
literal K. During a collision `[H,K]` need not vanish: the old-energy claim is
about asymptotic elastic channels, while the complete static H is conserved.

The positive vacancy block is `nu I + mu1 n_c1`. The scattering algebra below
subtracts only the explicitly retained common scalar nu. Physical time evolution
therefore has the extra factor `exp(-i nu tau)`, and physical total scattering
energies are the displayed E plus nu. This scalar must be part of the clock
output/comparator; it is not dropped as free phase control.

The supplier differs from PR9656's. It requires occupation-conditioned old X
couplings, source hopping/penalties, two clock/source contacts and specified
clock onsite projectors. This is an explicit conditional Hamiltonian, not a
derivation of those couplers from the microscopic axioms or original actuator set.

## Exact finite reduction and all channel thresholds

The full bulk internal Hamiltonian is B=K+C+G, dimension16. It commutes with
P=X1X2. For p=+/-1 choose the old basis so that ZZ=Z, X1=X and X2=pX.
For example its unnormalized s=+ and s=- vectors are respectively
`|00>+p|11>` and `|10>+p|01>`. In source order00,01,10,11 the resulting block is

    B_p = I4 tensor (2I+Z) + C_p tensor I + F_p tensor X,
    C_p = (DeltaA+gA)nA + (DeltaB+gB)nB
          + h(nA+nB-L_AB) + u nA nB,
    F_p = gA nA + p gB nB.

This 8x8 identity is checked exactly against a separately assembled full
four-qubit Pauli operator in `independent_check.py`. Its vacuum energies are
1 and3. Source excitation number is conserved by B, so its remaining eigenvalues
have the following exact description. Let

    aA=2+DeltaA+h+gA,  aB=2+DeltaB+h+gB,
    xA=lambda-aA,     xB=lambda-aB.

The four one-source-excitation eigenvalues are the four roots of

    (xA*xB+1+p*gA*gB-h^2)^2 - (xA+xB)^2
      - (gA*xB+p*gB*xA)^2 + (gA-p*gB)^2 = 0.

The remaining two are

    2+DeltaA+DeltaB+2h+u+gA+gB +/- sqrt(1+(gA+p*gB)^2).

The quartic is checked against the exact rational characteristic polynomial.
For the fixed coefficients, all sixteen bulk eigenvalues are, rounded here:

| p | Eight eigenvalues of B_p |
|---|---|
| +1 | 1, 3, 6.671573387110, 34.169062964188, 46.681890304244, 66.392282238574, 79.043854253349, 126.164916518934 |
| -1 | 1, 3, 14.130637131516, 18.540987107274, 58.828927362578, 75.065829307524, 86.098948786312, 106.458249971196 |

Every eigenvalue b supplies the bulk clock band `[b,b+4J]`, with the common nu
added physically. Full numerical band endpoints are saved in
`evidence/different_path_check.json`. Channel closure uses an analytic bound,
not those rounded eigenvalues. If Q excludes source vacuum, positivity gives

    Q B Q >= (1+min(DeltaA,DeltaB)) Q.

For this witness

    4J = 1.555612607490684,
    min(DeltaA,DeltaB) - 2 - 4J > 1.11106871217564,
    2 - 4J > 0.44438739250931.

Thus both entire incoming vacuum bands `[1,1+4J]` and `[3,3+4J]` lie below
every source-excited band; the two vacuum bands are also disjoint. The possible
release of two units by old relaxation is fully paid. For each fixed p, s and
interior k there is exactly one open channel at `E_s=2+s+2J(1-cos k)`.
At the certified k0, `E_-=2.553124953460740...` and
`E_+=4.553124953460740...`, before adding nu. Both parity sectors are included.

## Stationary reflection algebra

Set z=exp(ik), epsilon(k)=2J(1-cos k), and E=2+s+epsilon(k). For a bulk
eigenvalue b define D_b=b+2J-E and choose the solution of

    r_b + r_b^-1 = D_b/J

that is z in the single open channel and has |r_b|<1 in each closed channel.
For closed channels this gives the real branch

    F_b = -J/r_b = -(D_b+sign(D_b)*sqrt(D_b^2-4J^2))/2,

while the open value is `F_open=-J conjugate(z)`. Functional calculus gives
F_p(E) on the 8-dimensional bulk internal space. There are no open source
channels, so this accounts for every asymptotic channel.

Let `V_A=lambdaA(I+XA)+mu0 I` and
`V_B=lambdaB(I+XB)+mu1 I`, including identities on the old coordinates.
For incoming unit vector e_s in vacuum at reference site c1, the two boundary
vectors x0,x1 solve the exact finite system

    M_(s,p)(k) [x0;x1] = [0; 2iJ sin(k) e_s],
    M = [[E-2J-B_p-V_A, J I8],
         [J I8,          F_p(E)-V_B]],
    r_(s,p)(k) = <e_s,x1>-1.

The lead solution for n>=1 is the open incoming wave `z^(-(n-1))e_s`, its
outgoing reflected wave and all the decaying closed eigenchannels. This fixes
the orientation and common propagation phase. Invertibility of M at k0 is
certified below. A discrete-current identity for a Hermitian nearest-neighbor
Hamiltonian equates incoming and outgoing flux: the closed real roots carry
zero current and the endpoint carries none. Hence `|r_(s,p)|=1` exactly.
There is no channel to discard in this statement. The fiber operator R(k0) is
diagonal in the four joint (ZZ,XX) eigenstates and commutes with K.

Since W has eigenvalue `w_+=(-7+24i)/25` for p=+1 and `w_-=1` for p=-1,
the four certified scalar differences yield the displayed full old operator
norm bound. Tensoring a passive reference preserves that norm. This is a
stationary scattering-fiber assertion; it does not normalize a monochromatic
plane wave or create a finite ready state.

## Fixed rational witness and certificate

The following terminating decimals are exact inputs. Define

    q = 0.040021355301287,
    cos(k0)=(q^2-1)/(q^2+1), sin(k0)=2q/(q^2+1),
    epsilon0=2J(1-cos(k0)),
    DeltaA=2+epsilon0+1/20+1.143803166553335,
    DeltaB=2+epsilon0+1/20+1.063556366205592.

| coefficient | exact value |
|---|---:|
| J | 0.388903151872671 |
| gA | 19.999998155265832 |
| gB | 9.869584235578144 |
| h | 19.999999311960544 |
| lambdaA | 0.359303251635283 |
| lambdaB | 2.497330381697014 |
| u | 14.99540892430831 |
| mu0 | 0.520036275799164 |
| mu1 | -0.151066135275764 |
| nu | 0.151066135275764 |

The JSON stores exact fractions for every coefficient and energy. The source
penalties need more than the 10^15 coefficient grid because they contain the
rational epsilon0. These parameters are calibrated to the supplied target W;
no prediction or microscopic derivation of the numbers is claimed.

`certify_point.py` uses 90-decimal mpmath values only to propose matrices rounded
to denominator10^55. All certification arithmetic is exact Python Fraction
arithmetic. For each 6x6 source-excited block let

    D=B_Q+2J-E, A=D^2-4J^2 I, D>=d I, d>2J,
    S_hat = proposed positive square root,
    b=d-||S_hat-D||_infinity >0,
    a=d-2J >0.

The exact residual bounds the true positive square root S by

    ||S_hat-S||_2 <= ||S_hat^2-A||_infinity/(a+b).

Indeed `S_hat(S_hat-S)+(S_hat-S)S=S_hat^2-S^2`; the inverse Sylvester map is
the integral of `exp(-t S_hat) R exp(-t S)` and has norm at most1/(a+b).
Symmetry bounds the residual's spectral norm by its maximum row sum. Multiplying
the root error by3/2 safely bounds the 6x6 F-block infinity-norm error because
sqrt(6)<3. The other closed vacuum channel uses the analogous scalar residual.

For rational M_hat and inverse proposal N, exact
`gamma=||I-M_hat N||_infinity<1` gives
`L=||N||_infinity/(1-gamma)`. If the certified M error is delta and L*delta<1,
then `||M^-1||_infinity<=L/(1-L*delta)`. A separately rounded state x_hat obeys

    ||x-x_hat||_infinity
      <= [L/(1-L*delta)]
         (||M_hat x_hat-b_rhs||_infinity + delta ||x_hat||_infinity).

Complex row sums use `abs(real)+abs(imag)` as a conservative upper bound.
All positivity and Neumann conditions are asserted by exact comparisons.
The largest certified inverse bound is1033.45652395759; the largest resulting
reflection-amplitude certificate error is below9.7e-50. The larger target
error below5.2e-13 is the actual mismatch of the fixed rational design, not an
arithmetic uncertainty. Alpha is the exact unit-modulus r_(-1,-1), and the
certificate compares each amplitude with alpha*w_p; it does not fit away
separate old-energy phases.

The unrounded floating search, including failed starts, is preserved separately.
One contact did not match W in its stated bounded search; this is not a no-go.
Two contacts with nonnegative clock potentials reached a residual0.003368 in
the saved search. Allowing mu1<0 produced the saved floating fit, which motivated
the distinct positive vacancy-projector resource and the rational certificate.
Search success is not the certificate and search failure establishes no exclusion.

## Strength and preparation resources

These are sums of norms of the separately supplied incident positive blocks,
with literal old K additional. The source-edge hopping is counted as the one
displayed positive two-qubit block; splitting it into other actuators changes
that convention and must be recounted.

| site | added incident block-norm sum |
|---|---:|
| old1 | 2gA = 39.999996310532 |
| old2 | 2gB = 19.739168471156 |
| A | DeltaA+2gA+2h+u+2lambdaA = 100.460938482046 |
| B | DeltaB+2gB+2h+u+2lambdaB = 84.395918102446 |
| c0 | 3J+2lambdaA+mu0 = 2.405352234688 |
| c1 | 4J+2lambdaB+nu = 6.701339506160 |
| later clock sites | 4J = 1.555612607491 |

The old edge has norm3. All strengths are finite; there is no infinite-penalty
limit or hidden three-body cancellation. The original added cap2 is not met.
The precise couplings, calibration, occupation-conditional directions, source
product initialization, one-head clock input, infinite blank tail and energy/time
units remain supplied. Static coefficients have zero runtime slew; this says
nothing about fabrication, installation, source/clock preparation work or renewal.

## Different-path author check and actual execution

`independent_check.py` assembles the literal four-qubit Pauli operator, checks
vacuum darkness and the two symmetry blocks with exact fractions, and checks
the one-excitation quartics. It then solves full16-internal-channel finite leads
of lengths12,20,32. Only the open vacuum channel has an outgoing termination;
all closed channels terminate at a hard wall. This calculation never evaluates
the closed-channel surface square root. At length32 its two old-energy results
agree with the certified surface amplitudes within2.7e-13 in double precision;
the largest matrix dimension is512 and each solve has two right-hand sides.
The length12 lower-energy discrepancy2.89e-11 decreases at length20. These are
numerical checks of a different implementation/path, not independent review or
a proof of a finite-clock horizon.

All executed scientific programs exited0. Full stdout and stderr are retained
under `evidence/`; empty stderr files remain present. Versions: Python3.13.5,
NumPy2.4.4, SciPy1.17.1, SymPy1.14.0, mpmath1.3.0. Commands set
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`; no assertion about measured hardware
thread use is made. Search caps were80 and120 starts, each with SciPy
`max_nfev=350`, and a180-second checkpoint between starts. Finite-difference
calls are additional to SciPy's reported nfev; no total call count was measured.
Refinement used `max_nfev=12000` and reported nfev363. Source/internal/boundary
dimensions are16/8/16 as stated; the largest finite-lead solve is512. Actual
elapsed times and all optimizer results are in the respective JSON files.

Reproduce from this directory, in order:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 certify_point.py
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 independent_check.py

The certificate uses the preserved refinement file to select its rational point.
The exact chosen point is also completely specified above and in its JSON. The
discovery programs `probe.py`, `probe_ladder.py`, `refine_ladder.py` are retained
for provenance, but do not need rerunning to inspect this fixed certificate.

## Precise next theorem and unproved joins

The next target is a full joint norm inequality for a normalized, independently
specified clock packet f initially placed a finite distance from the contacts:

    sup_(tau>=T_ready) || exp(-i tau H) J_f
       - [exp(-i tau K) W] tensor |00>_AB tensor chi_out(tau) || <= eta.

Here J_f appends the SAME source vacuum and clock f for every old/reference
input, and chi_out includes `exp(-i nu tau)`, actual reflection phase alpha(k),
clock dispersion and the chronology of launch. All outputs remain. This theorem
is not proved by the point certificate. Necessary steps are:

1. Certify a compact momentum interval around k0, separated from0,pi and all
   thresholds, on which all four boundary matrices stay invertible. The bulk
   closure inequalities above are already uniform over the whole clock band;
   they do not themselves bound a contact resonance or its derivatives.
2. Bound derivatives of the closed-channel roots, inverse matrices and the four
   reflection functions. Then bound
   `sup_k ||R(k)-alpha(k)W||` on the packet support. Narrowing support has a
   localization/time cost and does not convert this fixed nonzero calibration
   residual into arbitrary accuracy.
3. Construct normalized incoming/outgoing generalized-eigenfunction transforms
   with their exact normalization and phase orientation. Prove their comparison
   with the independent finite-distance product input. An exact scattering
   state is generally correlated near the contacts and cannot simply be called
   an independently prepared ready state.
4. Control all closed-channel, incoming and near-contact tails uniformly for
   every tau>=T_ready, including arbitrary old superpositions and references.
   Closed asymptotic channels mean zero outgoing excitation flux, not exactly
   zero source occupation at a finite time. A rate or explicit computable bound
   is still needed.
5. Account for localized/bound states, possible threshold singularities and
   the overlap of the actual finite-distance prepared packet with them. No
   bound-state inventory, absence theorem or uniform overlap estimate was run.
   A boundary inverse certified at one continuum energy does not settle this.
6. For a finite clock, replace the infinite-tail assertion by a quantified
   horizon and a finite-boundary error. The finite linear solves above are
   stationary cross-checks, not a dynamical recurrence or horizon theorem.

These are analytic and preparation obligations for this explicit model, stronger
than its stationary-fiber statement but substantially more specific than the
original arbitrary-supplier question. The exact calibration equation or a
certified tunable family would additionally be needed for arbitrary requested
accuracy below this fixed point's residual. Nothing here asserts finite-time
exact permanent capture, permanent classical Records, reset or indefinite reuse.

The next useful action is a fresh check of the rational certificate and the
channel/phase derivation, followed by a quantitative packet theorem for this
same fixed Hamiltonian. Source identities and the failed single-contact route
should be retained. No shared source, editable prompt, axiom, audit state, Git
commit, push, PR or other chat was changed by this worker.
<!-- END UNCHANGED SOURCE: dark_source_two_body_halt/ROUTE.md -->

<!-- BEGIN UNCHANGED SOURCE: dark_source_two_body_halt/old_cap_search/RESULT.md; SHA256=397c18e02c0d583bdc3e51df8f5c513f677b448862526a362eac4cc43577af00 -->
~~~~markdown
# Two-contact ladder with the old added-incident cap

The bounded search found a finite stationary witness satisfying the original **added old-site incident cap 2** on both old qubits. A separately executed exact rational-residual calculation certifies

\[
 \|R(k_0)-\alpha W\|\;<\;1.76\,10^{-13},\qquad
 \alpha=r_{s=-1,p=-1}(k_0),\quad |\alpha|=1,
\]

for all four \((s=Z_1Z_2,p=X_1X_2)\) fibers, with the literal old Hamiltonian \(K=2I+Z_1Z_2\) and \(W=((9+12i)I+(-16+12i)X_1X_2)/25\). This is one clock momentum, corresponding to two old-dependent total energies. It is an operator-norm comparison and therefore includes arbitrary old-reference entanglement at that stationary fiber. The largest wrapped relative-phase error is consequently below \(1.77\,10^{-13}\) radians: for unit complex amplitudes the angle is \(2\arcsin(\text{chord}/2)\).

The exact computed upper bound is approximately \(1.752474830885985\,10^{-13}\); its full rational value is in rational_point_certificate.json (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/dark_source_two_body_halt/old_cap_search/rational_point_certificate.json`). This is a fixed-point witness. No arbitrary-accuracy statement, all-future finite-packet theorem, independent reviewer acceptance, or original all-site hardware closure is asserted. The separate packet bridge remains a separate obligation.

## Exact selected coefficients and physical implementation

Use the positive strict nearest-neighbor ladder and scattering convention in the immutable route (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/dark_source_two_body_halt/ROUTE.md`). Every terminating decimal in this table is **exact**, not an uncertainty interval. The certificate calls the source hopping coefficient `t`; it is denoted \(h\) here.

| Coefficient | Exact value | Coefficient | Exact value |
|---|---:|---|---:|
| \(J\) | 0.030021107107032 | \(g_A\) | 0.996878563816670 |
| \(g_B\) | 0.599319315560298 | \(h\) | 3.999349697888060 |
| \(\lambda_A\) | 3.801781381581202 | \(\lambda_B\) | 2.575033765788497 |
| \(u\) | 0.544607276405587 | \(\Delta_A\) | 2.192035527016003 |
| \(\Delta_B\) | 2.186826508897014 | \(\mu_0\) | 0.321494607058201 |
| \(\mu_1\) | -1.459892813020969 | \(q=\cot(k_0/2)\) | 4.510351185997098 |

Define \(\cos k_0=(q^2-1)/(q^2+1)\), \(\sin k_0=2q/(q^2+1)\), with \(0<k_0<\pi\). Thus both trigonometric inputs are exact rationals, while \(k_0\simeq0.436365793409261\). The kinetic energy is exactly

\[
 \epsilon_0=\frac{30021107107032000000000000000}{5335816955256357129429116105401}
 \simeq0.005626337514718896.
\]

The square ladder is old1 \((0,0,0)\), old2 \((1,0,0)\), source A \((0,1,0)\), source B \((1,1,0)\), and one-head clock sites \(c_n=(n,2,0)\), \(n\ge0\). Writing \(n=(I-Z)/2\), \(a=|0\rangle\langle1|\), and \(L_{AB}=a_A^\dagger a_B+a_B^\dagger a_A\), the source/old terms are

\[
 C=\Delta_A n_A+\Delta_B n_B+h(n_A+n_B-L_{AB})+u n_A n_B,
 \quad G=g_A n_A(I+X_1)+g_B n_B(I+X_2).
\]

The clock is the positive half-line hopping sum

\[
 H_c=Jn_{c_0}+J\sum_{n\ge0}(n_{c_n}+n_{c_{n+1}}
 -a_{c_{n+1}}^\dagger a_{c_n}-a_{c_n}^\dagger a_{c_{n+1}}),
\]

and the physical contacts/wells are

\[
 \lambda_A n_{c_0}(I+X_A)+\lambda_B n_{c_1}(I+X_B)
 +\mu_0 n_{c_0}+|\mu_1|(I-n_{c_1}).
\]

All blocks displayed are positive and at most two-body, with their supports on the listed nearest-neighbor edges or sites. No target \(W\) is placed in a hopping bond. The vacuum \(|00\rangle_{AB}\) is exactly dark for \(C+G\); the contact flips vanish when the clock head is absent. In that sector there is no added persistent old interaction. This does not assert that a finite packet has already returned the source exactly at a finite time.

The signed-potential scattering algebra replaces the last well by \(\mu_1 n_{c_1}\). The **physical** Hamiltonian therefore equals that signed Hamiltonian plus

\[
 \nu I=1.459892813020969\,I.
\]

Both physical total-energy bands acquire \(+\nu\), and time evolution acquires \(e^{-i\nu\tau}\). This scalar is retained alongside actual old aging; it is not discarded as an uncounted well offset.

## Complete channel closure

The full asymptotic old/source operator \(B=K+C+G\) has dimension 16. It commutes with \(p=X_1X_2\), giving two eight-dimensional blocks. The complete eigenvalue lists below are numerical displays of the exact block matrices; exact vacuum values, the exact single-excitation quartics, and the double-excitation formulas are recorded in different_path_check.json (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/dark_source_two_body_halt/old_cap_search/different_path_check.json`) and the immutable route.

| \(p\) | All eight eigenvalues of \(B_p\), before \(+\nu\) |
|---|---|
| +1 | 1, 3, 3.705042189110481, 6.249366370510604, 11.711927442874522, 14.281182619636610, 14.634793474973128, 18.401939699970256 |
| -1 | 1, 3, 3.906519299420971, 5.891344983196852, 12.066787162441920, 14.082867177072476, 15.442237712348375, 17.594495462595010 |

Every eigenvalue \(b\) generates the band \([b,b+4J]+\nu\), with \(4J=0.120084428428128\). The incident vacuum bands before the common shift are \([1,1.120084428428128]\) and \([3,3.120084428428128]\). Their exact separation is

\[
 2-4J=1.879915571571872>0.
\]

The analytic lower bound on every excited-source eigenvalue is \(1+\min\Delta=3.186826508897014\). It exceeds the entire upper incident band by the exact positive margin

\[
 \min\Delta-2-4J=0.066742080468886>0.
\]

This bound pays for the full old-energy release of 2. Each incident total energy \(1+\epsilon_0+\nu\) or \(3+\epsilon_0+\nu\) has exactly one open channel per \(p\); the other old-vacuum band and every source-excited band are closed. No channel exclusion relies on the numerical eigenvalue approximation. The elastic outgoing source is vacuum in all four stationary fibers; localized evanescent amplitudes are included in the boundary solve.

## Actual added incident block norms

Each entry is the sum of norms of the **displayed positive physical blocks** incident on that site. The existing old edge has norm 3 and is separate from the added cap. Source hopping contributes \(2h\) at A and B, the contact contributes \(2\lambda\), and the positive vacancy projector contributes \(|\mu_1|\) at \(c_1\).

| Site | Immutable original witness | Selected capped witness |
|---|---:|---:|
| old1, added | 39.999996310531664 | **1.993757127633340** |
| old2, added | 19.739168471156288 | **1.198638631120596** |
| A | 100.460938 (rounded) | 20.332662089993454 |
| B | 84.395918 (rounded) | 17.078839343776311 |
| \(c_0\) | 2.405352 (rounded) | 8.015120691541701 |
| \(c_1\) | 6.701340 (rounded) | 6.730044773026091 |
| tail site | 1.555613 (rounded) | 0.120084428428128 |

The selected source loads are substantially reduced, but the clock boundary load increases. The witness meets the **old added cap**, not a cap of 2 at every added site. No global resource minimization is claimed. Its small \(J\) also reduces the clock group velocity, here approximately 0.025376758082332338.

## Retained alternative and actual search limits

The first search allowed either clock well to be a positive vacancy projector. Its best point, start 11, has numerical chord error \(6.0569652953395666\,10^{-12}\), phase-residual 2-norm \(7.529830276171857\,10^{-12}\), and a vacancy well at \(c_0\). It is retained as a **numerical** resource variant, without a separate rational certificate:

```
J=.376316199540247; k=1.537671975130416
gA=.6439382393073481; gB=.9998709290686835
h=3.6826317080947124; lambdaA=2.6196847825624525
lambdaB=3.770053749674341; u=2.948020046167829
DeltaA=4.508808839911606; DeltaB=3.564102565658795
mu0=-1.7498956277270894; mu1=.9245821797866128
```

Its scalar is 1.7498956277270894, source closure margin 0.0588377674978071, old-band gap 0.4947352018390121, old added loads 1.2878764786146962 / 1.999741858137367, source loads 21.349338346 / 23.417235386, and clock loads 8.118213791 / 9.969954477 (last four rounded). Its raw parameters and complete outputs are in SEARCH.json (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/dark_source_two_body_halt/old_cap_search/SEARCH.json`). The later comparison constrained \(\mu_0\ge0\) and kept \(\mu_1\) signed; it found the selected point at global start 40. Both physical well locations were authorized. The comparison is retained as an outcome, not as a necessity for positivity.

The shared budget was at most 60 starts, `max_nfev=500` per start, and a cumulative 180-second search-wall checkpoint tested between completed starts. Actual use was **41 starts, 47.09935441613197 seconds**: 12 starts / 13.409708832856268 seconds with seed 2026101603, then 29 starts / 33.689645333215594 seconds with seed 2026101604. Both searches stopped upon a useful fit. The wider coefficient box coded after first-search start 30 was never used; all runs used \(J\in[.03,.49]\), \(k\in[.08,\pi-.003]\), \(g_A,g_B\in[.005,1]\), \(h,\lambda_A,\lambda_B\in[.001,4]\), \(u,e_A,e_B\in[0,4]\), and \(\mu_j\in[-4,4]\), with \(\mu_0\ge0\) only in the second search. Penalties were \(\Delta_j=2+4J+.05+e_j\).

There were zero exception failures, 34 starts reaching the evaluation limit, and 7 solver-success terminations; only 2 starts reached numerical target error below \(10^{-9}\). SciPy's `nfev` excludes finite-difference calls: the actual optimizer residual-call count was **213,016**, or **213,098** including recorded detail evaluations. Every initialization, termination reason, residual, coefficient, and load is retained in SEARCH.json (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/dark_source_two_body_halt/old_cap_search/SEARCH.json`) and ALLOWED_SEARCH.json (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/dark_source_two_body_halt/old_cap_search/ALLOWED_SEARCH.json`), with full stdout/stderr. Unsuccessful starts supply no no-go evidence.

## Verification and provenance

certify_old_cap.py (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/dark_source_two_body_halt/old_cap_search/certify_old_cap.py`) reuses the original residual-certification algorithm on the new rational coefficients. It uses 90-digit mpmath only to propose roots/inverses, rounds certificate matrices to denominator \(10^{55}\), then uses exact `Fraction` residuals and positivity/Neumann/Sylvester bounds. The largest certified inverse infinity bound is below 163.903, and every reflection approximation has rigorous error below \(2.33\,10^{-51}\). The final exact assertion is `error < 176/10**15`, with explicit positive-block, old-coupling, and closure checks. The certificate is stronger than the binary64 discovery residual because it evaluates a slightly rounded point with higher-precision proposals and exact residual control; neither binary64 fit is the certificate.

check_old_cap.py (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/dark_source_two_body_halt/old_cap_search/check_old_cap.py`) separately assembles the full physical four-qubit matrices. It checks vacuum darkness, \(XX\) symmetry, both block identities, and the exact single-excitation quartic identities. A different numerical method uses full 16-channel leads of lengths 12, 20, and 32, with only the open vacuum channels outgoing-terminated and all closed channels hard-wall terminated. The maximum matrix dimension is 512 with two right-hand sides. Across these runs its disagreement with the certified surface amplitudes is below \(2.90\,10^{-13}\), its linear residual below \(1.28\,10^{-15}\), and off-diagonal reflection below \(6.92\,10^{-15}\). These are author checks by different assembly/method, not independent review or a packet calculation.

Versions: Python 3.13.5, NumPy 2.4.4, SciPy 1.17.1, mpmath 1.3.0, SymPy 1.14.0; macOS 26.6.2 arm64. The boundary matrix is 16 by 16 per parity, with an eight-dimensional bulk block; the exact square-root residual is six-dimensional. Runs set `PYTHONDONTWRITEBYTECODE=1`, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`. Full outputs, actual elapsed times, exact coefficient fractions, and provenance are stored locally.

Source scope remains the scientific branch at `c86e61caf46c848fe8cee57ecbea6e6fdad7a4bc`, supplied main `5b0e1cc44f422fb0138b02eb071d3d16b40dfbb2`, and the frozen PR9656/PR9657/workflow/contract sources identified in the original manifest (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/dark_source_two_body_halt/sources/MANIFEST.json`). The sole campaign recovery checkpoint remains the parent's `worktree/.claude/science/physics-loops/toe-dynamics-bridge-20261009/TARGET_CONTRACT.md`; this note is a bounded result artifact, not a replacement checkpoint.

All new files are confined to `old_cap_search/`. ORIGINAL_SNAPSHOT.json (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/dark_source_two_body_halt/old_cap_search/ORIGINAL_SNAPSHOT.json`) pins all 36 preexisting files; RECEIPT.json (`outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/dark_source_two_body_halt/old_cap_search/RECEIPT.json`) records their unchanged verification and the new execution summary. No shared sources, editable prompts, axioms, audits, Git state, PRs, or other chats were changed. No network calls were used.
~~~~
<!-- END UNCHANGED SOURCE: dark_source_two_body_halt/old_cap_search/RESULT.md -->
