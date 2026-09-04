---
claim_id: composition_discriminator_record_statistics_bounded_theorem_note_2026-09-02
claim_type: bounded_theorem
claim_scope: "For four explicitly declared finite open bipartite clusters and fixed occupation-number sectors, compare the occupation-basis diagonal of the normalized ground-space projector for the two matrices H(1,g) obtained from ungraded and Jordan-Wigner ladders. The chain6 matrices agree entrywise for N=2 and N=3 at every real g. On grid2x3 N=2, grid2x3 N=3, cube N=4, and grid3x3 N=3 the ungraded matrix has a simple strictly positive ground vector at every real g. At g=0 the graded matrices have the exact finite probability multisets and cancellation-zero sets stated below; their symmetry characters force 3, 12, and 4 of those zeros. A nine-coupling persistence check and a 241-point finite-window L1 scan with bounded scalar refinement are numerical witnesses only. The displayed hopping-plus-density expression is a declared subfamily rather than the complete family implied by all locally allowed two-site terms; t=0 is outside the normalized slice. Calling the occupation distribution a physical record distribution additionally requires separately supplied ground-state/Born and occupation-to-record bridges."
upstream_dependencies: []
runner: scripts/composition_discriminator_record_statistics_check_2026_09_02.py
---

# Finite-cluster occupation distributions for ungraded and Jordan-Wigner nearest-neighbour constructions

**Date:** 2026-09-02
**Type:** bounded_theorem
**Audit:** independent audit required
**Status:** proposed_retained
**Status authority:** effective status is pipeline-derived after independent audit ratification and dependency closure.
**Primary runner:**
[`scripts/composition_discriminator_record_statistics_check_2026_09_02.py`](../scripts/composition_discriminator_record_statistics_check_2026_09_02.py)
**Runner cache:**
[`logs/runner-cache/composition_discriminator_record_statistics_check_2026_09_02.txt`](../logs/runner-cache/composition_discriminator_record_statistics_check_2026_09_02.txt)
**Parents:** none. The finite mathematical constructions used by the claim are declared here.

This note compares two finite matrices and their occupation distributions. A physical record-statistics reading is conditional on two additional
bridges: selection of the normalized ground-space projector with Born weights, and identification of one-site occupation with record content.
Those bridges are inputs to such a reading; their derivation remains open outside the algebraic theorem below.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster matrix identities, positivity, spectra, rational probability multisets, and symmetry identities, together with explicitly numerical finite-sample witnesses."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Submit the finite mathematical result to the independent audit lane; route any physical occupation-to-record or state-selection bridge to its owning science lane."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target proved here is: for the declared normalized matrices `H(1,g)` on the named finite open clusters and sectors, establish the chain
identity, ungraded ground-vector positivity, exact graded `g=0` probability data, and exact symmetry implications stated below, while treating
the finite-window distance scan and nine-coupling persistence sample as numerical observations.

The result has five descriptive components:

1. **Local span and normalized slice.** The exchange-symmetric, number-conserving Hermitian two-qubit operator space has the stated four-element
   basis. Summing its linear number term over an open graph produces a degree-weighted site term, so the local span calculation supports only a
   local classification, while completeness of the displayed hopping-plus-density expression remains outside the claim. For nonzero hopping
   on a bipartite graph, a sign gauge and positive energy rescaling
   reduce the declared expression to `H(1,g)` with `g = V/|t|`. The diagonal limit `t=0` is excluded.
2. **One-dimensional identity.** On `chain6` at `N=2` and `N=3`, the graded and ungraded matrices agree entrywise for symbolic `g`.
3. **Finite-cluster positivity and exact distributions.** The ungraded ground vector is simple and strictly positive at every real `g` in the
   four named cluster-sector cases. The graded `g=0` distributions have exact rational multisets with 3, 12, and 8 cancellation zeros.
4. **Finite comparator and numerical scan.** The declared bond-product comparator gives the same support status to the vertical and horizontal
   adjacent-pair patterns on `grid2x3`; the graded distribution gives different support status. The reported `L1` minima come only from the
   declared finite scan and bounded local refinement.
5. **Symmetry identity and sampled persistence.** At `g=0`, exact signed permutation representations force 3, 12, and 4 zeros. The same forced
   sets occur at nine sampled couplings in a floating-point check. On any connected interval where the graded ground state is already known to
   remain simple, the character is constant; the nine samples alone do not certify such an interval.

## Imports, declared inputs, and authority

- **Explicit normalization and boundary conditions:** the four finite open graphs, their site orderings, the listed fixed-occupation sectors,
  nonzero hopping, normalization to `t=1`, and the real parameter `g` are declared model inputs. Their provenance is this note; their role is to
  define the finite target. Larger, periodic, infinite, and zero-hopping systems remain outside the target.
- **Declared algebraic constructions:** the ungraded ladders, Jordan-Wigner ladders, and homogeneous hopping-plus-density matrices are supplied
  definitions with framework provenance left open. Their provenance is this note; their role is the object being compared.
- **Explicit state-selection and probability convention:** the normalized ground-space projector and its occupation-basis diagonal are supplied
  for the mathematical comparison. A framework derivation of that state selector and Born weighting remains open and belongs to the science
  lane that proposes a physical readout.
- **Open occupation-to-record bridge:** the theorem uses occupation labels only. Equating those labels with record content requires a separately
  supplied dictionary and remains open here. The registered Record axiom supplies record constraints; the Hamiltonian, ground-state selector,
  probability values, formation process, and update dynamics all remain separately open.
- **Standard methodology:** finite-dimensional spectral theory, the Perron-Frobenius theorem, Jordan-Wigner signs, Slater determinants for a
  free quadratic matrix, determinants, and Sturm root counts are standard mathematical inputs. The runner checks their finite hypotheses and
  the stated spectra or ground certificates; their role is proof methodology.
- **Comparator convention:** three homogeneous bond weights indexed by endpoint occupations define a support-only classical comparator. Its
  provenance is this note, and its role ends at the enumerated finite support fact.
- **Numerical protocol:** the `[-6,6]` window, 241 grid points, bounded scalar refinement, target couplings, tolerances, and `0.15` reporting
  threshold are declared computational choices. They are neither measured nor fitted inputs.
- **Observational inputs:** none.

For context only, the composition question was previously discussed in
`MATTER_GRADED_COMPOSITION_AXIOM_UPDATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md`; the occupation-to-record dictionary question was discussed
in `GL_F_RECORD_VALUE_DICTIONARY_COMMUTING_LOCK_BOUNDED_THEOREM_NOTE_2026-09-01.md`. These plain-text pointers carry no dependency weight.

## Proof-obligation graph

1. **Definitions and admissibility — proved here:** construct the graphs, sector bases, two ladder realizations, Hamiltonian matrices, and
   normalized occupation distribution.
2. **Local operator span — proved here:** solve number conservation and exchange symmetry on a symbolic Hermitian two-qubit matrix; separately
   evaluate the summed linear term on the global open graphs.
3. **Nonzero-hopping normalization — proved here:** divide by `|t|` and conjugate the hopping sign on a bipartite graph.
4. **Chain matrix identity — proved here:** compare every symbolic sector-matrix entry at `N=2` and `N=3`.
5. **Ungraded positivity — proved here:** verify sign-uniform off-diagonal entries and exact connectivity, then apply Perron-Frobenius.
6. **Graded free-point data — proved here:** construct exact orbitals and Slater amplitudes and certify the simple lowest eigenvalue with exact
   characteristic-polynomial root counts.
7. **Comparator support identity — proved here:** enumerate the three bond-type counts for all seven adjacent pairs on `grid2x3`.
8. **Symmetry selection identity — proved here:** enumerate automorphisms, verify the signed representations and symbolic commutators, and apply
   the fixed-pattern character identity.
9. **Numerical observations — computed here:** diagonalize the finite matrices at the declared scan/sample points with stated tolerances.

Every lemma required by the finite mathematical target is closed. The strongest missing lemma for a physical record claim is the conjunction of
a framework state-selection/Born bridge and an occupation-to-record bridge. That conjunction is outside this theorem rather than a terminal
lemma used to close it.

## Definitions

A **cluster** is a finite simple graph with an ordered site list and open boundaries. The four graphs are `chain6` (six sites, five bonds),
`grid2x3` (six sites, seven bonds, index `3r+c`), the `2 x 2 x 2` cube (eight sites, twelve bonds, index `4x+2y+z`), and `grid3x3` (nine sites,
twelve bonds, index `3r+c`). Each site carries `C^2` with basis `|0>,|1>`, lowering operator `a=|0><1|`, number `n=a^dag a`, and
`s3=1-2n`.

The **ungraded ladders** place `a` at site `i` and identity elsewhere. The **graded ladders** are
`c_i=(s3_0 ... s3_{i-1})a_i`. Both give the same `n_i`. The declared matrix expression is

```text
H(t,V) = -t sum_bonds (x_i^dag x_j + x_j^dag x_i) + V sum_bonds n_i n_j,
          x = b or c.
```

This expression is an explicitly chosen homogeneous hopping-plus-density subfamily. For `t != 0`, positive rescaling and the bipartite sign gauge
give the normalized slice `H(1,g)` with `g=V/|t|`. The fixed-occupation sector has basis patterns `|S>` with `|S|=N`. Its **occupation
distribution** is the diagonal of the normalized projector onto the lowest eigenspace. For a simple ground vector it is the vector of squared
amplitudes.

For a bond `(i,j)` with `i<j`, the graded hopping matrix element includes `(-1)^{|S intersect (i,j)|}`, where the intersection counts occupied
sites strictly between the endpoints in the fixed site order. The classical comparator assigns a pattern the product of three supplied weights
`w_00,w_01,w_11`, one per bond according to its endpoint occupations. A cluster automorphism preserves the bond set and acts on a graded sector
by `U_sigma|S> = sgn_S(sigma)|sigma S>`, where the sign is the parity needed to reorder the occupied images.

## Local span and the boundary-degree correction

Solving `[K,n_A+n_B]=0` and exchange invariance for a general Hermitian `4 x 4` matrix gives a four-dimensional real space with basis

```text
1,  n_A+n_B,  n_A n_B,  b_A^dag b_B+b_B^dag b_A.
```

The first two are constant on the local one-particle block. Globally, however,

```text
sum_(i,j in bonds) (n_i+n_j) = sum_i degree(i) n_i.
```

On `chain6` in the one-particle sector the diagonal values are `1,2,2,2,2,1`; on `grid2x3` they are `2,3,2,2,3,2`; on `grid3x3` they are
`2,3,2,3,4,3,2,3,2`. Thus the allowed boundary-degree term remains present on those open graphs. The cube
is regular and gives the constant value `3` in its one-particle sector. The theorems below concern only the displayed declared subfamily.

The diagonal limit also lies outside the normalized slice. At `t=0,V=1`, the ungraded projector distributions already contain respectively
`7`, `18`, `68`, and `62` zero entries in the four named cluster-sector cases. This supplies an explicit boundary counterexample to extending
the nonzero-hopping positivity statement through `t=0`.

## Exact one-dimensional identity

On `chain6`, every nearest-neighbour edge joins consecutive site indices, so the Jordan-Wigner string between its endpoints is empty. At `N=2`
(dimension 15) and `N=3` (dimension 20), the graded and ungraded `H(1,g)` matrices therefore agree entrywise for symbolic real `g`. Their
normalized ground-projector occupation distributions agree at every real `g`, including degeneracies. Direct floating-point checks at `g=0`
and `g=1` return `L1` distance `0.00e+00`.

## Exact ungraded positivity on the normalized slice

For `grid2x3` at `N=2,3`, the cube at `N=4`, and `grid3x3` at `N=3`, the ungraded off-diagonal matrix at `t=1` is minus the configuration-graph
adjacency: every off-diagonal entry lies in `{0,-1}`. Exact breadth-first search finds the configuration graph connected in sector dimensions
15, 20, 70, and 84. Adding real `g` changes only the diagonal. Perron-Frobenius applied after a sufficiently large scalar shift gives a simple
lowest eigenvalue and a strictly positive ground vector for every real `g`. A numerical check at `g in {-2,0,1,3}` finds minimum occupation
probability `2.34e-04` over the sixteen cases.

## Exact graded distributions at the free point

At `g=0`, exact product orbitals and Slater determinants give:

1. On `grid2x3`, `N=2`, the simple ground energy is `-(2+sqrt(2))`. The fifteen probabilities have multiset
   `0 x 3`, `1/16 x 8`, `1/8 x 4`; the zero patterns are the three vertical pairs.
2. On the cube, `N=4`, the simple ground energy is `-6`. The seventy probabilities have multiset
   `0 x 12`, `1/64 x 56`, `1/16 x 2`; the zero patterns are six occupied faces and six configurations made from two disjoint adjacent pairs.
3. On `grid3x3`, `N=3`, the simple ground energy is `-4sqrt(2)`. The eighty-four probabilities have multiset
   `0 x 8`, `1/256 x 12`, `1/128 x 32`, `1/64 x 20`, `1/32 x 8`, `9/256 x 4`; the zero patterns are the three rows, three columns, and two
   diagonals.

The amplitudes are normalized exactly. Each claimed ground energy is checked by an exact eigenvector equation and Sturm counts showing zero
eigenvalues below a rational lower bracket and one below an upper bracket.

## Comparator support and bounded numerical scan

On `grid2x3` at `N=2`, each of the three vertical adjacent pairs and four horizontal adjacent pairs contains at least one bond of each endpoint
type `00`, `01`, and `11`. Their declared bond-product weights therefore have identical zero-versus-positive support status. The exact graded
distribution instead assigns probability zero to the three vertical pairs and `1/16` to the four horizontal pairs. This is a finite property of
the supplied comparator convention.

For numerical context, the runner compares graded targets at `g_target=0,1` with ungraded distributions on 241 equally spaced points of
`[-6,6]`, then uses bounded scalar refinement around the best grid point. The resulting `L1` values are:

| Cluster and sector | target `g=0` | target `g=1` |
|---|---:|---:|
| `grid2x3`, `N=2` | `0.389` at `g=1.850` | `0.296` at `g=6.000` |
| `grid2x3`, `N=3` | `0.439` at `g=-0.898` | `0.375` at `g=1.567` |
| cube, `N=4` | `0.333` at `g=-1.483` | `0.321` at `g=1.674` |
| `grid3x3`, `N=3` | `0.373` at `g=1.571` | `0.258` at `g=2.971` |

The chain control returns `0.00e+00` at both target couplings. These values describe the declared window and procedure only. In particular, the
`grid2x3,N=2,g_target=1` value at the endpoint is an upper bound on the infimum over the whole real line.

## Exact symmetry implication and sampled persistence

The bond-preserving site-permutation groups have orders 4, 48, and 8 on `grid2x3`, the cube, and `grid3x3`. Their signed graded actions and
unsigned ungraded actions commute with `H(1,g)` symbolically and form representations of those image orders. At `g=0`, every exact graded ground
vector is simple and hence carries a character `chi(sigma)`. If a pattern is fixed and `chi(sigma) sgn_S(sigma)=-1`, its amplitude equals its
negative and is zero. Exact enumeration predicts 3 of 3 zeros on `grid2x3`, 12 of 12 on the cube, and the four centre-crossing lines among the
eight zeros on `grid3x3`.

For the ungraded construction, the signed factor is `+1`; strict positivity makes the ground character trivial, so the corresponding predicted
set is empty. This contrast combines an exact Perron-Frobenius result with a floating-point eigenvector check in the runner.

On any connected interval already known to have a simple graded ground state, the discrete character is constant by continuity and the forced
set persists. The runner samples `g in {0,+-0.25,+-0.4,0.5,0.75,1,2}`. At those nine values it observes a smallest gap of `0.534`, containment of
the predicted set in the `1e-12` numerical zero set, and intersection sizes 3, 12, and 4. This sampled observation is evidence only at those
points; interval certification remains open.

## Executable claim block

```text
clusters: chain6 6 sites/5 bonds; grid2x3 6/7; cube 8/12; grid3x3 9/12; all open and ordered
declared_matrix_subfamily: H(t,V) = -t hopping + V nearest-neighbour density interaction; ungraded or Jordan-Wigner ladders
normalization_boundary: t is nonzero; g = V/abs(t); t=0 excluded
local_span: dimension 4 with basis 1, n_A+n_B, n_A n_B, exchange hopping
summed_linear_term: sum_i degree(i)n_i; nonconstant on chain6, grid2x3, and grid3x3 one-particle sectors
zero_hopping_counterexample_zero_counts: 7, 18, 68, 62 at V=1 in the four named cases
chain_matrix_identity: dimensions 15 and 20; exact for symbolic g
ungraded_configuration_graph: entries 0 or -1 and connected in dimensions 15, 20, 70, 84
ungraded_ground_state: simple and strictly positive for every real g on the normalized slice
graded_free_point_zero_counts: 3 of 15; 12 of 70; 8 of 84
graded_free_point_ground_energies: -(2+sqrt2); -6; -4sqrt2; all simple by exact certificates
comparator_support_fact: all seven adjacent pairs contain all three bond types; graded vertical probabilities 0 and horizontal probabilities 1/16
finite_scan: 241 points on [-6,6] plus bounded local refinement; minimum reported L1 value 0.258
symmetry_groups: orders and representation image orders 4, 48, 8
exact_symmetry_forced_zero_counts_at_g0: 3, 12, 4
sampled_persistence: nine couplings; minimum numerical gap 0.534; common numerical zero counts 3, 12, 4
physical_record_reading: conditional on separately supplied state-selection/Born and occupation-to-record bridges
runner_result_required: zero failed checks
```

## Proof boundary and degenerate cases

The exact claim covers only the displayed matrix subfamily, four finite open ordered graphs, named sectors, nonzero hopping normalized to `t=1`,
real `g`, and the explicitly exact free-point and symmetry statements. Completeness on an irregular open graph lies beyond the local two-site
span. The diagonal limit `t=0` is excluded and has the displayed counterexamples. Ground-space degeneracy is handled by the normalized
projector definition, although the positivity theorem and symmetry-character statement use simplicity where stated. Numerical scans cover only
their listed points, window, refinement rule, and tolerances. Physical state selection, Born weighting, record interpretation, formation,
updates, dynamics, larger geometries, other terms, and infinite-volume limits remain outside this proof.

## Review record

The review narrowed the original draft by removing its global family-completeness inference, zero-hopping coverage, physical formation reading,
whole-family exclusion language, and extrapolation from nine coupling samples to entire intervals. The retained scope ends at the finite
mathematical statements and bounded numerical observations above.

Hard landing conditions are: a fresh runner/cache pair with zero failed checks and invocation stdout below 6000 characters; one adversarial
mutation per descriptive check family; an independent implementation of the matrix construction and reported finite values; a current
citation-graph manifest containing this node; clean pipeline, strict-lint, changed-evidence, vocabulary, link, syntax, and diff checks; and
independent audit after landing. The independent audit lane owns every audit status or verdict.
