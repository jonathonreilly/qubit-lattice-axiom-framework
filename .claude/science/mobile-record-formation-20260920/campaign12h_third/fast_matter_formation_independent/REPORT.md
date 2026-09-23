# Source-informed review: fast matter, fourth-order interactions and formation

No required mathematical correction was found in the current authorized note.
Its fixed-volume theorem retains an epsilon-dependent fast-matter generator;
its further joint spin limit identifies a rotor field evolution only before
the first formation. These are distinct assertions, and the note keeps their
different scopes. The full-W-cluster rotation, canonical fourth-order
coefficient, dissipative correction and trace-norm argument withstand the
checks below. The unbounded electric Hamiltonian in the first-event corollary
is treated separately from the bounded direct-unit-rotor theorem.

This is **source-informed scientific review**, not a blind reconstruction,
formal audit, publication decision or extension of the preceding balanced
formation disposition. No PRE-stage independence is asserted. Independent
calculations use this agent's already sealed electric-tuple Gauss builder;
no author microscopic builder was imported or executed. No author source or
older independent evidence was modified.

## 1. Exact source boundary and authenticated premises

The reviewed current note is
FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md, SHA256
`002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e`.
Its current FAST_MATTER_FORMATION_AUTHOR_SEAL.json is
`5aeee4c3db513daafc32c22ceb7e2a7c5dc0c1a3e7d89208fec4244806c67577`.
All 36 bound artifacts authenticate. The earlier 33-artifact seal also
recovers through the archived earlier note as explicitly specified by the
source history. The prior current-note hashes c66d... and seal 585903... are
historical bytes, not the sources assigned for this review.

The complete current note, both current scientific runners, source-context
receipt, complete relevant outputs/receipts, and all changed failure-history
content were inspected. The exact source-history deltas are retained in
AUTHOR_HISTORY_DIFFS.txt. The 72 complete-density result rows and 25 first-event
rows were computationally checked; every stored H2/H4 matrix entry was compared
to independently assembled complete physical sectors. This is not a claim to
have independently rerun all those trajectories.

The following unchanged premises are reused at verified identities:

- FINITE_RATE_REPEATED_RECORD_FORMATION.md:
  `b577c14e992fe74feb8a9f17c33e503f446f7052f83512031c2bf82cf2e3538d`.
- LOCAL_FINITE_RATE_FORMATION_AND_ROTOR_LIMIT.md:
  `1d3aad074b15777a20ef09f90bc1ca1ce4a55f441299ad2187b50b4b3cc6b976`.
- ELECTRIC_AND_MAGNETIC_DYNAMICS_FROM_RECORD_MOTION.md:
  `52f5ce8bd8f1b39049ebbb0407e6881ed8e11de80bc2c29db9e0e56c5cdd3fc2`.
- The corresponding already checked field packet FINAL_SEAL:
  `7620bb6ff3b16ec319f12ad0d588d45a56f0fd084ed192b59e8c86d0f9ac30d4`.

The field-coefficient source was reread completely to confirm the changed
scaling uses its coefficients, not its different decreasing-birth dynamical
theorem. Its canonical block formula and even-period-at-least-six hypothesis
are the imports needed here. The older finite-circuit gauge issue does not
identify arbitrary finite-S block gauges: this new note fixes the canonical
positive-overlap gauge explicitly.

The separate FOURTH_SCALE_REPEATED_FORMATION_AUTHOR_SEAL packet, later
frontier files, campaign checkpoint and registry were not opened. The
Bravyi--DiVincenzo--Loss citation is contextual only; no theorem from the
author's abstract-only read is imported into this review. The bounded
functional-calculus and residual argument are checked directly below.

## 2. Full-cluster rotation and coefficients

Write h(epsilon)=W+epsilon T, with integer W spectrum and T changing W by
exactly one. For example, choose contours of fixed radius 1/3 about each
occupied W grade and then epsilon small compared with 1/||T||. The contour
resolvent expansion gives Q_r(epsilon)-P_r=O(epsilon) in operator norm.
There are only |A|+1 possible grades. These estimates, and a sufficiently
small common epsilon_0, depend on the fixed graph but not the spin dimension.

For S0=sum_r Q_r P_r one has

    S0^dagger S0 = sum_r P_r Q_r P_r.

It is positive, block diagonal, and close to identity. Its inverse square
root is a norm-convergent power series. Thus U=S0(S0^dagger S0)^(-1/2) is the
near-identity unitary mapping every bare grade to its perturbed cluster. This
works equally on the infinite-dimensional rotor physical Hilbert space:
boundedness, spectral separation and finitely many grades suffice. There is
no hidden finite-matrix spectral multiplicity assumption.

Xi=(-1)^W conjugates h(epsilon) to h(-epsilon), hence also conjugates their
Riesz projections and the polar construction. Because U^dagger h U is exactly
W-block diagonal, it commutes with Xi, and is even in epsilon. Consequently

    U^dagger h U = W+O(epsilon^2)

globally, not just in the P block. This global statement is essential to the
dissipative estimate. A rotation of P against its complement alone would leave
an O(epsilon) hopping term between nonzero W grades, becoming O(epsilon^-3)
after the microscopic scaling; the stated O(epsilon^-2) remainder bound would
then be unjustified.

Independently reconstruct the low graph map X:P->Q, with R=W_Q^-1:

    epsilon A+(W_Q+epsilon QTQ)X=epsilon X A^dagger X,
    X1=-A,       X2=Z/2,
    X3=R[X1 A^dagger X1-QTQ X2].

Here A=Pi1 T P and Z=Pi2 T Pi1 A. The grade-one part of X3 is
A M-(Pi1 T Pi2)Z/2, giving

    H2=-M,             H4=M^2-Z^dagger Z/2.          (1)

The graph-coordinate low matrix is epsilon A^dagger X. Passing to the
canonical orthonormal coordinates conjugates it by (I+X^dagger X)^(1/2).
The only possible fourth-order change is [M/2,-M]=0. The full-cluster
positive-overlap U has exactly that canonical restriction on P, so (1)
matches the author's chosen U, rather than an unspecified block gauge.

The selection rules also give U'(0)P=-A. Since jP=0,

    U^dagger j U P = -epsilon jA+O(epsilon^2)
                  = epsilon B_j+O(epsilon^2),
    B_j=-P j Pi1 T P.                                (2)

The leading term lands in P because the birth lowers W by one. No factor of
delta belongs in B_j: the hopping/detuning ratio is epsilon, while the jump
amplitude is sqrt(kappa)/epsilon. A relative sign within a coherent channel
must remain; the common minus sign in B_j does not affect its dissipator.

Exact independent Riccati calculations check H2, vanishing H3, H4 and the
normalization commutator on the nine-state path and complete spin-one and
spin-two cycles, of dimensions 19 and 39. A separate SVD polar implementation
constructs each cluster's canonical overlap map, rather than reusing the
author's global Gram-matrix code. At epsilon 0.07,0.035,0.0175 its coefficient
errors have the predicted O(epsilon^2) behavior. These finite checks support
the coefficient algebra; the graph-map derivation establishes it generally.

## 3. Off-block source, corrector and complete error estimate

Let G_epsilon be the exact rotated generator and E0 the P embedding. Use the
target L_P,epsilon in the note, retaining the fast delta epsilon^-2 H2 term.
Write R_epsilon=G_epsilon E0-E0 L_P,epsilon. Equation (2) implies

    P j_tilde P = epsilon B_j+O(epsilon^2),
    Q j_tilde P = O(epsilon^2).

The PP recycling and loss terms therefore equal kappa D[B_j] with
O(epsilon) error. QQ recycling is O(epsilon^2). The Hamiltonian's P
truncation is O(epsilon^2) and has no off-block part. In contrast,
Q j_tilde^dagger j_tilde P can be O(epsilon), so its scaled anticommutator
contributes O(epsilon^-1) to QP/PQ. Thus

    ||Off R_epsilon||=O(epsilon^-1),
    ||Diag R_epsilon||=O(epsilon).                   (3)

These are induced trace-norm estimates from bounded left/right products.
They are uniform in S because the analytic remainders and jump norms are
uniform. There is no small full-generator discrepancy without a correction.

On Off matrices, A0=-i delta[W,.] has a bounded inverse. For a QP block Y it
is i W_Q^-1 Y/delta; the adjoint block has the opposite sign. This inverse
is bounded independently of spin and preserves Hermiticity on the paired
off-block space. Define

    C_epsilon=-epsilon^4 A0^-1 Off R_epsilon,
    E_epsilon=E0+C_epsilon.

Then ||C_epsilon||=O(epsilon^3), and exact algebra gives

 G_epsilon E_epsilon-E_epsilon L_P,epsilon
  =Diag R_epsilon
    +(G_epsilon-epsilon^-4 A0)C_epsilon
    -C_epsilon L_P,epsilon.                          (4)

The full-cluster rotation implies
||G_epsilon-epsilon^-4 A0||=O(epsilon^-2), including the complete
dissipator. Also ||L_P,epsilon||=O(epsilon^-2). Every term in (4) is therefore
O(epsilon). The fast target has not been treated as a bounded-in-epsilon
generator; its amplification of the corrector is explicitly included.

E_epsilon need not be positive. It preserves Hermiticity, and both actual
semigroups are CPTP, so trace-norm contraction applies to the Hermitian
defects. Duhamel in the rotated frame gives

    error <=2||C_epsilon||+T0||residual||.

Returning the initial and final densities to the original frame costs at
most 4||U-I||=O(epsilon). This proves the stated uniform-over-initial-P-
densities fixed-time O(epsilon) result. It includes the bare initial layer;
there is no silently required dressed initial state, fast excited population
gap, or Markovian factorization of recycled states.

The independent numerical control forms the *entire matrix-unit discrepancy
map* on the path and spin-one cycle for both instruments. At epsilon 0.0175,
the off-source norm is approximately 68.47 on the path and 96.77 on the
cycle, while the corrected residual divided by epsilon is approximately
5.58 and 10.88. The correction divided by epsilon^3 stays bounded. These
are Hilbert--Schmidt map-norm diagnostics, not a substitute for the uniform
trace-norm proof or a dimension-uniform empirical extrapolation.

## 4. Finite-volume rotor theorem and registers

At fixed graph, ||T||<=m and sum ||j||^2<=2m uniformly for integer S>=1.
For example, ||H2||<=m^2, ||H4||<=3m^4/2 and sum ||B_j||^2<=2m^3. The
contour radius and all perturbative constants can therefore be chosen
independently of S. None is asserted uniform in graph volume.

For unit rotor links the shifts are bounded and W still has finitely many
integer grades. Every operator in this part of the theorem is bounded at
fixed epsilon. The same norm functional calculus, trace-class generator and
corrector proof apply. This assertion contains **no electric-square energy**:
it is the direct unit-shift version of the epsilon-dependent full matter
target. It must not be confused with the separate joint large-S limit below.

The number-energy qualification is correct. Delta N_B differs from Delta W
by Delta(N-|A|). It can be removed on number-block-diagonal densities, a
property preserved from the declared initial-number preparation; it cannot
in general be removed on arbitrary coherences between different N sectors.
The theorem stated for H_epsilon using W does not require that extra
restriction. Neither description supplies the energy reservoir.

A finite count/mark register does not change the W selection rules or bounded
Hamiltonian rotation. On the physically reachable subspace no overflow occurs,
because each jump adds two records. The same argument therefore controls
joint register states and fixed finite sets of count or first-event CDF
observations. It does not establish total variation convergence of arbitrary
continuous histories. Post-birth target motion remains fast and potentially
nontrivial; no epsilon-independent target on all later sectors follows.

## 5. Joint large-spin first-event field corollary

The new even-period-at-least-six qualification matches the reused field
coefficient source. Before a birth, P with the initial number N=|A| forces
all A charges to be plus and all B sites vacant. Gauss then gives div E=0.
The target Hamiltonian preserves this sector, denoted P_v.

For an edge with A-to-B orientation sign sigma_e the first outward hop has
squared amplitude F_e=1-(E_e^2-sigma_e E_e)/C, C=S(S+1). The linear terms
sum to sum_A div E=0. Hence exactly

    H2|P_v=-m I+C^-1 sum_e E_e^2.

With epsilon^2 C=delta/K and J=2delta, subtracting the scalar
-delta m epsilon^-2 gives precisely K sum E^2. The inherited canonical
fourth-order coefficient tends strongly on finite electric vectors to

    c_G I-2 sum_p(U_p+U_p^dagger),
    c_G=d|V|(4d-1).

The constant counts m single-edge returns and twice the unordered adjacent
edge pairs: each edge has 4d-2 adjacent distinct edges. Short wrapping cycles
would alter that argument; the current source explicitly excludes them.
The source's earlier dynamical theorem with a decreasing birth rate is not
being reused outside its assumptions. Its coefficient calculation is reused;
the new corrector theorem supplies the present formation scaling.

On the unit-rotor initial field sector, a birth on a given A-centered edge
must follow an old plus record's hop to a different B neighbor. For that
fixed edge/channel, distinct destinations have different final matter
occupations, and coherent charge outputs are orthogonal at A. The remaining
electric shifts are unitary. This gives the operator identity

    kappa sum_j B_j^dagger B_j|P_v
        =r I,       r=2kappa sum_{a in A} z_a(z_a-1). (5)

It is an identity on arbitrary coherent field states in P_v, not just on
basis states. Finite-spin blocked amplitudes need not give a constant loss.
On a three-dimensional periodic cubic graph, r=30kappa |V|. The resulting
no-event branch is exp(-rt) times the unitary density evolution under

    H_field=K sum E^2-J sum_p(U_p+U_p^dagger).

The marked first-event integral stated in the note follows by applying the
specified B_j to that branch. Coherent and resolved marks are different
operational outputs even though (5) is common.

The passage to this unbounded H_field is not a naive strong limit of the
full epsilon-dependent generators. On P_v the electric part is extracted
**exactly**, and each finite-spin problem is extended with the common
self-adjoint diagonal K sum E^2. Its electric box is reducing. H4,S and the
restricted loss are uniformly bounded and converge strongly, together with
adjoints. In the electric interaction picture their Dyson expansions have
uniform factorial bounds. Strong convergence of products and dominated
integration give no-event propagator convergence uniformly on compact times.
Finite-rank approximation and trace-norm contraction extend this to every
trace-class initial field density, provided the embedded initial densities
rho_S converge to that density in trace norm. Normalized electric cutoffs
supply such approximants and preserve P_v and Gauss.

No uniform electric moment is required for this qualitative fixed-volume
limit. There is no uniform assertion over arbitrary S-dependent states whose
mass escapes to the spin cutoff. Likewise there is no operator-norm
convergence of spin shifts to rotor shifts. Products B_j,S rho_S B_j,S^dagger
converge in trace norm by boundedness and strong convergence, which also
justifies the finite-time marked integrals. These are the needed domain and
state hypotheses for the corollary as stated in its proof.

After combining this limit with the S-uniform estimate in Section 3, the
microscopic pre-event density and first time/mark probabilities converge.
At a fixed finite graph and finite time the limiting no-event probability
is strictly positive, so the conditional field density can also be normalized.
That normalization is not uniform as volume or time grows. After the event,
the available theorem is still the full epsilon-dependent generator, not the
unchanged pure-field Hamiltonian. Any further weak-field packet approximation
requires its own preparation and ordered-limit hypotheses; it cannot remove
this before-first-event boundary.

## 6. Independent finite controls and author implementation coverage

The independent builder enumerates electric tuples and infers every matter
charge from Gauss. It is byte-identical to this agent's earlier sealed builder
at `abb86e2fec6d9202471dc1cd3a0a1cc27a4758202b42550d3231ededc8c728d1`.
The author uses site words and a circulation coordinate instead. Both give
the complete physical cyclic sectors, rather than a guessed low-state subset.

In addition to the exact graph-series and complete residual-map tests above:

- All stored H2/H4 entries on the star, path, S=1 cycle and S=2 cycle were
  independently reconstructed, with the author's basis ordering made explicit.
- The exact cyclic low-sector formulas were checked at S=1,2:
  H2_mm=-4+4m^2/C;
  H4_mm=12(1-m^2/C)^2-4m^2/C^2;
  H4_(m+1,m)=-2[1-m(m+1)/C]^2.
- The complete first-loss formula on that cycle is
  sum B_j^dagger B_j=8(1-m^2/C)^2 on flux m. It tends to the scalar 8,
  and displays why a finite-spin constant-loss assumption would be wrong.
- All 72 stored full-density rows were checked for count normalization,
  nonnegative probabilities up to roundoff and error/epsilon bookkeeping.
  All 25 first-event rows were checked against exp(-rt), the rank-two
  trace-distance identity and the recorded conditional-distance normalization.
- One first-event endpoint was reconstructed without the author's builder
  or propagator: S=4,t=0.25, full dimension 79, N=2 dimension 49. A direct
  matrix exponential and explicit enlarged-space density-difference
  diagonalization give no-event probability 0.3657911556860345 and trace
  distance 0.31687335894335195. Differences from the author are 2.61e-15
  and 4.33e-15, respectively.

These cycle controls are standalone four-edge models. They are not a
three-dimensional simulation or a period-four instance of the cubic field
corollary. The finite rotor cutoff was changed to 20 in the independent
endpoint control; the author's 32/64 refinement is also authenticated. This
is numerical convergence evidence, not an interval enclosure or an exact
bound on the infinite cutoff tail. The theorem rests on the analytic
bounded-perturbation argument, not those floating results.

The author runners faithfully implement the displayed rates and target.
Their common B_j sign, coherent normalization, fourth-order factor one-half,
electric coefficient and no-event factor one-half are consistent. No drift
requiring a source repair was identified. The full author trajectory grid was
not rerun, and the independent numerical residual diagnostics do not claim
rigorous floating-point error certificates.

## 7. Preserved failures, source scope and remaining limits

All three author numerical histories were examined and recovered by exact
source identities:

1. The initial polar-unitarity threshold failure was repaired by changing
   both Hermitian eigensolvers to the divide-and-conquer driver. The declared
   2e-13 threshold and scientific coefficients were unchanged.
2. The first non-Hermitian eigenvector condition-number rejection was
   replaced by a unitary complex Schur propagator, avoiding inversion of a
   poorly conditioned eigenbasis. The previous vacuous self-comparison was
   replaced by an actual time-zero state reconstruction check.
3. The subtractive rank-two distance lost precision at identical time-zero
   states. Its stable perpendicular-component formula is mathematically
   equivalent and retains the target mass outside the microscopic spin box.
   It remains a comparison to a numerically truncated rotor target, whose
   cutoff refinement is reported separately.

The old note/seal and the exact even-period qualification are preserved;
the correction was already present at first source access here. The new
independent scientific and evidence controls all passed their first runs.
Complete scripts, outputs, streams and command receipts are included in this
packet. No failed independent probe has been omitted.

The bounded disposition is therefore: the stated fixed-volume approximation
and joint pre-first-event corollary are supported under the supplied model
and initial-state hypotheses. The target depends on epsilon after births;
there is no general ordinary density limit, guaranteed filling, persistent
post-birth photon regime, finite fuel construction, uniform-volume error,
native-axiom derivation or empirical match. The extensive first-event rate
makes global no-event conditioning restrictive at large volume. The separate
fourth-scale packet retains its own obligations and was not opened.

All exact current source and evidence identities are bound in FINAL_SEAL.json.
