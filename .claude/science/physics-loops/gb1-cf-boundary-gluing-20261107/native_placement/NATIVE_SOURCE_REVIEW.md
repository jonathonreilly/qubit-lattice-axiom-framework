# Focused native-placement source review

Status: completed mathematical/source review of the frozen sources below.
This is not a formal landing recommendation, audit verdict, or claim-status
change. The review found no error in the placement, detector, or Hamiltonian
theorems. One scope clarification is requested before the text is finalized.

## Sources and independence boundary

Primary worktree:
`/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics`,
HEAD `17f68f575f3de7c1a24a4761e01c8307a9e99955`.

The following files were read completely and matched the supplied SHA-256s:

| Source | SHA-256 |
|---|---|
| `docs/SU2_HOMOGENEOUS_NATIVE_QUBIT_CODE_BOUNDED_THEOREM_NOTE_2026-11-08.md` | `b80894286228826227ad6e58fb5376ee16426cb128ac59dad2621166691ef23b` |
| `docs/SU2_HOMOGENEOUS_NATIVE_QUBIT_CODE_SCOPE_CHECK_2026-11-08.md` | `11e750a6b3fc4789dc6ea1419bba30da218e19149d622be029c856dbabe5d6c2` |
| `scripts/gb1_cf_native_placement_exact_2026_11_08.py` | `01b492f31004ede51696fb73f0f391fbba272ba186f8e93757586c29f7f03819` |

The one additionally inspected execution artifact was read in full:

`logs/runner-cache/gb1_cf_native_placement_exact_2026_11_08.txt`, SHA-256
`cfd420f676a9d5e28f21abb6172c233761fe27d1cf830b63bcdf05e54b1e920e`.

The independently derived predecessor was frozen before any supervisor
candidate exposure. It remains unchanged at
`INDEPENDENT_PLACEMENT.md`, SHA-256
`f8a14f5669aebc865f3daedcb6c2c454525ed8b6c30def7c2dbde254a1085244`.
That predecessor used a spacing-five code containing the all-zero vector and
a separate spacing-nine marker construction. The present review challenges
the supervisor's improved spacing-five code after exposure; it does not
relabel that improvement as an independent prior discovery.

The inherited model and effort were not overridden. No new numerical job,
script, source modification, GitHub action, commit, or extra artifact was
created. Runtime model/effort metadata was not exposed; no stronger model
provenance is claimed. This file is the review's only write.

## Finding requiring a narrow wording change

At theorem lines 210–212, the phrase “including the previously constructed
gluing maps when used within a fixed phase” is too broad without identifying
the source and target registers. The current construction allocates exactly
four qubits per edge of one fixed coarse cubic graph. It supports regional
Gauss gluing and compatible operators on that graph. The earlier boundary
note also has a link-subdivision map into two link registers with an
artificial new vertex; this source does not allocate that additional target
graph or its registers.

Narrow the statement to regional Gauss gluing on the chosen coarse graph.
If subdivision is mentioned, say that transporting a cut map requires
separately supplied source and target encodings and does not place an
artificial subdivision vertex on the native lattice. This clarification
does not alter the placement theorem or the Hamiltonian identity.

The supervisor has acknowledged this scope issue and plans only that
clarification. This review remains bound to the original hashes above;
it does not preapprove unseen revised prose.

## Independent check of the critical mathematics

### Link isometry, corner identity, and actual geometric action

The one-excitation pairs `{1000,0001}` and `{0100,0010}` give four
orthonormal symmetric/antisymmetric vectors. The remaining antisymmetric
pair `{1100,0011}` is orthogonal to all of them. Thus `J*J=I_5`. Reversal
has signs `(+,-,-,-,+)` in the supplied logical order, and none of the five
columns has a `0000` component. These directly establish
`FJ=JK`, `Q=JJ*`, `FQF*=Q`, and `Q|0000>=0`.

For every pair of logical matrices,

\[
(JAJ^*)(JBJ^*)=JABJ^*,\qquad (JAJ^*)^*=JA^*J^*.
\]

The encoded identity is exactly `Q`. There is no unital embedding of the
five-state full matrix algebra into the complete four-qubit matrix algebra
being asserted. Products on shared logical links use the same physical
corner; spectators and other links are separate tensor factors.

Proper cubic rotations are signed coordinate permutations. On a collinear
four-site edge block, they either preserve order or reverse it. Rotations
about the edge axis fix the sites pointwise, so no internal SU(2) spatial
vector action is hidden. The reversal intertwiner supplies precisely the
logical inversion needed when the canonical edge orientation flips.
Translations and rotations map spectator sites to the corresponding phase's
spectator sites. Composing origin-centered rotations with translations also
accounts for rotations about every native site.

### All 125 phases are orthogonal

I checked the separation argument directly rather than inferring it from
an abstract dimension comparison. Translate one phase to zero and let
`d=q-p mod 5` be nonzero. A phase-zero active site has exactly one nonzero
coordinate modulo five.

If `d` has one nonzero coordinate, take a `q`-edge along a different axis;
all its interior points have the fixed nonzero coordinate and a nonzero
coordinate along the chosen axis. If `d` has two nonzero coordinates, take
the remaining axis. If it has three, any axis leaves two fixed nonzero
coordinates. Each case supplies an entire `q`-edge whose four native sites
are spectators of phase zero. The first code is exactly `0000` on those
sites; the second lies in `Q`, which annihilates that vector.

This proves subspace orthogonality even for arbitrary entangled logical
states. Pairwise phase differences exhaust the same argument for every pair
of origins. No external marker or independent phase register is needed.
The direct sum nevertheless contains a real additional 125-valued encoding
origin degree of freedom. The theorem states that distinction correctly.

### The six-edge detector works locally

At any `x`, the six length-five interiors have 24 distinct sites on every
torus of side `5n`, `n>=3`. Opposite interiors have offsets `1,2,3,4` and
`-1,-2,-3,-4`, which do not coincide modulo `5n`; different axes cannot
coincide away from their excluded common endpoint. Their `Q` factors
therefore commute and their product `D_x` is a projector.

If `x` has the code's phase, all six blocks are true data blocks and each
factor acts as identity. If its phase is wrong, the preceding separation
argument chooses one of its three positive-direction edges as a four-site
spectator block of the actual phase. That `Q` kills the state, and it is
disjoint from the other five factors. Hence `D_x` has exactly the stated
zero-or-identity action on every code sector. Arbitrary noncommutation of
different detectors on the off-code complement causes no contradiction.

### Hamiltonian extension and normalization

Here `H` is the stated self-adjoint electric/plaquette Hamiltonian: real
coefficients and the Hermitian real part of the color trace. Different links
commute entrywise. Cyclic color trace and adjoint reversal therefore make
the magnetic sum invariant when rotations move plaquettes or reverse their
chosen traversal. Electric terms are invariant because `KE^2K=E^2`.

The seed's three positive outgoing electric terms count every edge once;
its three positive coordinate-plane plaquettes count every plaquette once
after all coarse translations. For `n>=3`, each plaquette has four distinct
edges and no size-two periodic double-counting issue occurs.

Let `tau_z` and `rho_R` denote the logical coarse translations and rotations.
For `x=p+5z`, equivariance and the corner encoding give

\[
T_xU_R a_0U_R^*T_x^*J_p
=J_p\tau_z\rho_R h_0\rho_R^*\tau_z^*.
\]

For other `x`, the right translated detector annihilates `J_p`. Summing
over `z` gives `rho_R H rho_R*=H`; summing over the 24 rotations and dividing
by 24 gives exactly `H_native J_p=J_p H`. There is no extra factor of 125,
because only the true phase's coarse anchors contribute. Finite sums can
be reindexed under native translations and rotations, proving ambient
geometric invariance. Each summand preserves the true phase and kills every
other phase, so the Hamiltonian does not mix phases or leak from the code.

The radius-nine support bound follows from the star offsets and far
plaquette-edge coordinates of the form `5 e_i + k e_j`, `1<=k<=4`.
Diameter at most 18 follows immediately; the certificate's sharper value
13 is consistent with the explicit support set. For `5n>=15`, no two
support sites are identified accidentally by wrapping a coordinate whose
span is at most nine. Torus shortest-path distances can only reduce the
infinite-lattice support-distance bound.

### Capacity and scope

The even-subgraph dimension argument matches the separate frozen derivation.
Each even occupied-edge pattern has a nonzero invariant after regrouping
endpoints, and occupation sectors are orthogonal. Incidence rank `V-1`
gives `2^(E-V+1)` independent sectors. Thus the displayed open and periodic
27-site witnesses have lower bounds `2^28` and `2^55`, respectively.
The graph parameters and inequalities are correct.

The note and sidecar do not promote these finite witnesses into an
impossibility of coarse or low-energy gauge encodings. Tensor composition,
code choice and preparation, spectators, Hamiltonian, and phase degree are
explicit. The Qubit axiom is not enlarged. The positive code and finite-range
Hamiltonian do not supply a nearest-neighbor admissibility probability law,
Record formation or readout, a selected physical state, or a continuum limit.
Gauge preservation is a statement about the encoded sectors; the note does
not establish a new physical gauge or admissibility law on all off-code states.

## Static runner and actual evidence coverage

The runner's rational matrix arithmetic directly checks all 25 inner
products, the five reversal/exclusion conditions, all 625 corner matrix-unit
products, and the rank-five invariant projector. The geometry code enumerates
all 125 residues, 24 signed-permutation rotations, and 124 nonzero relative
phases. It separately checks disjoint allocation on the side-15 torus, the
24-site detector star, seed radius/diameter, and the two 27-vertex incidence
ranks. The spin-half fusion recurrence provides the even-degree singlet
multiplicities `[1,1,2,5]`.

The canonical cache names exactly the reviewed runner hash in both its header
and stdout. It records normal exit 0, empty stderr, `PASS=795 FAIL=0`, radius
9, diameter 13, the full phase witness list, and both capacity certificates.
Those assertion counts also agree with the static control flow. This is a
read of an execution receipt, not a new execution or independently authored
numerical implementation.

The runner does not build a full 24-qubit detector matrix, the complete
native Hamiltonian, general-`n` tensor matrices, a thermodynamic limit, or a
physical law. General phase separation, all-`n` geometry, and Hamiltonian
intertwining rest on the mathematical proof checked above. The note accurately
describes its runner as supplementing that proof rather than replacing it.

The static mutation branches have the stated effect: the sign mutation fails
the reversal condition, including the quiescent vector fails exclusion, and
retaining a single origin fails unit-translation closure. The inspected
canonical cache contains only the normal run, so it does not establish that
the three mutation executions actually occurred. The supervisor explicitly
retains responsibility for those separate execution receipts. This review
does not certify that execution claim.

Prior-paper attributions, the historical PR description, and the sidecar's
additional historical source summaries were not independently re-fetched.
None is load-bearing for the complete finite-dimensional proof reviewed here.
Their verification remains separate from this mathematical/source review.

## Disposition and remaining work

No counterexample or error was found in the stronger spacing-five placement,
all-origin orthogonality, local detector, corner algebra, finite-range
Hamiltonian identity, or finite capacity witnesses. The construction improves
the independent marker construction without contradicting it. The one
requested source change is the explicit restriction of the gluing sentence;
the rest of the review is bounded by the three hashes recorded above.

The predecessor proof remains untouched. This report grants no retained
status or formal review/audit outcome and makes no claim that the native
physical-law problem is solved.
