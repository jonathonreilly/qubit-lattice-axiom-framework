---
claim_id: composition_discriminator_record_statistics_bounded_theorem_note_2026-09-02
claim_type: bounded_theorem
claim_scope: "On four finite open clusters (chain6: 6 sites, 5 bonds; grid2x3: 6 sites, 7 bonds; cube 2x2x2: 8 sites, 12 bonds; grid3x3: 9 sites, 12 bonds) the covariant record-conserving nearest-neighbour law H(t,V) = -t sum_bonds (x_i^dag x_j + x_j^dag x_i) + V sum_bonds n_i n_j is written once and read on two compositions, x = b (ungraded ladders) and x = c (graded Jordan-Wigner ladders). On two qubits the Hermitian operators commuting with n_A + n_B and symmetric under exchanging the two tensor factors form exactly a 4-dimensional real span {1, n_A + n_B, n_A n_B, b_A^dag b_B + b_B^dag b_A}, the first two constant inside a record-number sector, and on a bipartite cluster the sign of t is a diagonal gauge U = (-1)^{N_A} verified exactly on grid2x3 for both compositions at N = 2 and N = 3; so the record statistics of the family depend on the single ratio g = V/t. In one dimension the two compositions give the identical sector matrix on chain6 at N = 2 (dimension 15) and N = 3 (dimension 20), entrywise, hopping and interaction alike, hence identical record statistics at every real g, with numerical L1 distance 0.00e+00 at g = 0 and g = 1. On grid2x3 N = 2 (15), grid2x3 N = 3 (20), cube N = 4 (70) and grid3x3 N = 3 (84) the ungraded off-diagonal at t = 1 is minus the 0/1 configuration adjacency, entries in {0, -1}, and the configuration graph is connected by exact BFS, so by Perron-Frobenius every ungraded member has a simple, strictly positive ground vector at every real g; numerically the smallest ground occupation probability over sixteen cluster-sector-g cases at g in {-2, 0, 1, 3} is 2.34e-04. The graded law instead has exact cancellation zeros: on grid2x3 N = 2 at g = 0 the ground energy is -(2 + sqrt2), simple, and the 15 pair probabilities are 0 on the 3 vertical pairs, 1/16 on 8 pairs and 1/8 on 4 pairs, summing to 1; on the cube N = 4 at g = 0 the ground energy is -6, simple, and the 70 pattern probabilities take {0, 1/64, 1/16} with counts 12, 56, 2, the 12 zeros being the 6 cube faces occupied and 6 patterns of two disjoint adjacent pairs; on grid3x3 N = 3 at g = 0 the ground energy is -4 sqrt2, simple, and the 84 pattern probabilities take {0, 1/256, 1/128, 1/64, 1/32, 9/256} with counts 8, 12, 32, 20, 8, 4, the 8 zeros being exactly the 3 rows, 3 columns and 2 diagonals of the cluster. A cubic-covariant classical bond-product Gibbs rule has a bond-hereditary zero set, and on grid2x3 N = 2 each of the 3 vertical and 4 horizontal adjacent pairs carries all three bond types, so any such rule zeroes all seven or none, while the graded law zeroes exactly the 3 vertical pairs and gives each horizontal pair 1/16. As a numerical witness, scanning g over 241 points of [-6, 6] with bounded refinement gives minimum L1 distances from the graded targets at g_target = 0 and 1 of 0.389 and 0.296 (grid2x3 N=2), 0.439 and 0.375 (grid2x3 N=3), 0.333 and 0.321 (cube N=4), 0.373 and 0.258 (grid3x3 N=3), all at or above 0.15, with the chain6 N=2 control returning 0.00e+00 at g = g_target. Those graded zeros are a symmetry selection rule. Each cluster has a group of bond-preserving site permutations, of order 4 on grid2x3, 48 on the cube and 8 on grid3x3; such a sigma acts on the graded sector by U_sigma |S> = sgn_S(sigma) |sigma S>, the Jordan-Wigner reordering sign, and on the ungraded sector by |S> -> |sigma S> with no sign, both actions commuting with H(1,V) for symbolic V and giving a homomorphism of image order 4, 48 and 8. At g = 0 the exact graded ground vector is an eigenvector of every U_sigma with character chi(sigma) = +-1, so amp(S) = 0 whenever some sigma fixes S with chi(sigma) sgn_S(sigma) = -1; that predicted set lies inside the exact zero set with sizes 3 of 3 on grid2x3 (the 3 vertical pairs), 12 of 12 on the cube (the 6 occupied faces and 6 patterns of two disjoint adjacent pairs) and 4 of 8 on grid3x3 (the 4 lines through the centre); ungraded the signs are absent and the Perron-Frobenius ground vector forces chi = +1, so the rule forbids nothing. As a numerical witness, at g in {0, +-0.25, +-0.4, 0.5, 0.75, 1, 2} the graded ground state stays simple, smallest gap 0.534, its zero set below 1e-12 contains the predicted set, and the intersection over those nine couplings equals it exactly, 3, 12 and 4, the other four grid3x3 zeros at g = 0 not persisting. No axiom is amended, no status is set, and this note adopts no hypothesis: it compares two declared constructions."
upstream_dependencies: []
runner: scripts/composition_discriminator_record_statistics_check_2026_09_02.py
---

# The composition discriminator: covariant nearest-neighbour laws give identical record statistics in one dimension and separate by exact cancellation zeros in two and three

**Date:** 2026-09-02
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/composition_discriminator_record_statistics_check_2026_09_02.py`](../scripts/composition_discriminator_record_statistics_check_2026_09_02.py)
**Runner cache:**
[`logs/runner-cache/composition_discriminator_record_statistics_check_2026_09_02.txt`](../logs/runner-cache/composition_discriminator_record_statistics_check_2026_09_02.txt)
**Parents:** none. Every premise used below is declared in this note.

Three independent reviewers of the composition question converged on one finite test: can any ungraded, cubic-covariant, nearest-neighbour law
reproduce the record statistics of the graded nearest-neighbour law on finite clusters? This note runs it. The **record statistics** of a law are
the occupation-basis diagonal of its lowest-energy state in a fixed record-number sector, the normalized ground-space projector diagonal if
degenerate. The answer splits: in one dimension the two compositions are the same matrix; in two and three the graded law forbids patterns every
ungraded member gives positive probability, exactly.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster theorem plus one numerical witness: identity of the two compositions in one dimension, strict positivity of every ungraded member, exact cancellation zeros of the graded member in two and three dimensions, the symmetry selection rule those zeros obey, and a scanned L1 separation."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-cluster theorem and route the composition question itself, which this note does not decide, to its owner as a science-level decision."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The test runs inside record-number sectors of dimensions `15`, `20`, `70` and `84` on four finite open clusters. The target is the conjunction of
the five statements below, exactly the runner's check groups `F`, `A`, `B`, `C`, `D`, `E`. `T1`, `T2`, `T3` and the first three parts of `T5`
are exact; `W4` and the persistence part of `T5` are floating-point witnesses, labelled as such wherever they appear.

1. `T1` (`F`, `A`). The family is one-parameter in `g = V/t`, and in one dimension its graded and ungraded members are the same matrix in every
  record-number sector, hence carry the same record statistics at every real `g`.
2. `T2` (`B`). Every ungraded member, at every real `g`, has a simple and strictly positive sector ground vector on `grid2x3` at `N = 2, 3`,
  `cube` at `N = 4`, `grid3x3` at `N = 3`.
3. `T3` (`C`). The graded member at `g = 0` has exact cancellation zeros there, `3` of `15`, `12` of `70`, `8` of `84`, with exactly determined
  rational multisets, and no classical bond-product rule reproduces the `grid2x3` zero pattern.
4. `W4` (`D`). Numerically, over `241` scan points of `g in [-6, 6]` with bounded refinement, the `L1` distance from each graded target to the
  scanned ungraded family stays at or above `0.15` on all eight pairs, while the one-dimensional control returns `0.00e+00`.
5. `T5` (`E`). The graded zeros obey a symmetry selection rule: a cluster automorphism fixing a pattern with `chi(sigma) sgn_S(sigma) = -1`
  forbids it, which at `g = 0` predicts `3` of `3`, `12` of `12` and `4` of `8` of the exact zeros and forbids nothing at all in the ungraded
  composition; numerically the predicted set is exactly the zero set shared by `g in {0, +-0.25, +-0.4, 0.5, 0.75, 1, 2}`.

## Imports and authority

Imported scientific authority: none load-bearing. The Jordan-Wigner transformation, the Perron-Frobenius theorem for irreducible matrices with
nonpositive off-diagonal entries, and the free-fermion fact that a quadratic law's `N`-particle ground state is the Slater determinant of its `N`
lowest occupied orbitals are standard methodology; every object is redeclared here, and the runner recomputes every statement, the
Perron-Frobenius hypotheses and an exact simplicity certificate for each ground energy included. No observational value, no fitted number, no
framework premise enters any proof. Non-load-bearing context pointers, plain file names with no grade and no dependency weight:

- `MATTER_GRADED_COMPOSITION_AXIOM_UPDATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md` (the composition gap this test was designed to probe).
- `RING_MONODROMY_DOES_NOT_FORCE_CAR_NOTE_2026-06-04.md` (the earlier ring and chain probes, whose negative outcome Theorem 1 explains).
- `GL_F_RECORD_VALUE_DICTIONARY_COMMUTING_LOCK_BOUNDED_THEOREM_NOTE_2026-09-01.md` (the dictionary under which "one site's occupation" is the
  record read here).

This note cites none of their grades and adopts no hypothesis: it compares two declared constructions.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the strongest supported scope is
precisely `P0`--`P6`.

1. `P0` (declared here): the four clusters and their bonds, the two ladder sets, the sectors, the law `H(t, V)`, and record statistics.
2. `P1` (`F`): the two-qubit covariant span is `4`-dimensional and the sign of `t` is a diagonal gauge, so the family reduces to `g = V/t`.
3. `P2` (`A`): the one-dimensional identity of the two compositions, exact and with a numerical witness.
4. `P3` (`B`): sign-uniformity and irreducibility of the ungraded sector matrices, and strict positivity of their ground vectors.
5. `P4` (`C`): the exact spectra, ground energies and their simplicity, the rational multisets and zero sets, and the classical comparator.
6. `P5` (`D`): the scanned `L1` distances and the one-dimensional control.
7. `P6` (`E`): the symmetry action and its commutation, the character at `g = 0`, the predicted zero set, and its persistence in `g`.

## Definitions

A **cluster** is a finite simple graph with an ordered site list and open boundaries. Four are used: `chain6`, six sites on a line, five bonds;
`grid2x3`, two rows by three columns, seven bonds, site `(r, c)` at index `3r + c`; the `2 x 2 x 2` `cube`, eight sites, twelve bonds, site `(x,
y, z)` at index `4x + 2y + z`; `grid3x3`, nine sites, twelve bonds, same row indexing. Each site carries `C^2` with basis `|0>, |1>`, ladder `a =
|0><1|`, number `n = a^dag a = |1><1|`, `s3 = 1 - 2n`. The **ungraded ladders** are `b_i = a` at site `i`, identity elsewhere; the **graded
ladders** are `c_i = (s3_0 ... s3_{i-1}) a_i`, the Jordan-Wigner string over the sites before `i`. Both share `n_i = b_i^dag b_i = c_i^dag c_i`.
The **law family** is one expression read on either composition,

```text
H(t, V) = -t sum_bonds (x_i^dag x_j + x_j^dag x_i) + V sum_bonds n_i n_j,   x = b or x = c,
```

with the same real `t` and `V` on every bond. **Cubic-covariant** means exactly that: one bond expression, identical on every bond, symmetric
under reversing a bond, commuting with `sum_i n_i`. A **record-number sector** is the span of the patterns `|S>` with `|S| = N`, of dimension
`C(L, N)`; its **configuration graph** joins two patterns whenever one hop across one bond takes one to the other. The **record statistics**
`P_law(g)` are the occupation-basis diagonal of the sector ground-space projector divided by that space's dimension, so they sum to `1`; for a
simple ground vector they are its squared amplitudes. Since `n_i` is shared, `P_graded` and `P_ungraded` live on the same finite set, compared in
`L1`. For a bond `(i, j)` with `i < j` the compositions differ by the string that survives between them, `b_i^dag b_j = a_i^dag a_j` against
`c_i^dag c_j = a_i^dag (s3_{i+1} ... s3_{j-1}) a_j`, so the graded matrix element across `(i, j)` in a pattern `S` carries the extra factor
`(-1)^{|S ∩ (i, j)|}`, the parity of the occupied sites strictly between `i` and `j`. The **classical comparator** is a cubic-covariant classical
nearest-neighbour Gibbs rule: three weights `w_00, w_01, w_11` per bond, identical on every bond, a pattern receiving the product of its bond
weights, so its probability vanishes exactly when some bond type it contains has zero weight. That zero set is **bond-hereditary**. A **cluster
automorphism** is a site permutation `sigma` preserving the bond set; it acts on a sector by `U_sigma |S> = sgn_S(sigma) |sigma S>` in the graded
composition, `sgn_S(sigma)` being the sign of the permutation carrying `[sigma(i) : i in sorted(S)]` to `sorted(sigma S)`, and by `|S> -> |sigma
S>` with no sign in the ungraded one; the **character** `chi(sigma) = +-1` is its eigenvalue on a simple ground vector.

## Theorem 1 — the family is one ratio, and in one dimension the two compositions coincide

**Conclusion.** (1) On two qubits the Hermitian operators commuting with `n_A + n_B` and invariant under exchanging the two tensor factors form
exactly a `4`-dimensional real space, the span of the linearly independent `{1, n_A + n_B, n_A n_B, b_A^dag b_B + b_B^dag b_A}`; the first two
act as constants inside a record-number sector, so up to an additive constant a covariant bond term is `-t (x_i^dag x_j + x_j^dag x_i) + V n_i
n_j`. (2) On a bipartite cluster the sign of `t` is a diagonal gauge: on `grid2x3` with sublattice `A = {0, 2, 4}` the operator `U = (-1)^{N_A}`
is diagonal with entries `+-1` and satisfies `U H(1, V) U = H(-1, V)` for symbolic `V`, in both compositions, at `N = 2` and at `N = 3`, and a
diagonal `+-1` conjugation leaves every squared amplitude, hence the occupation diagonal, unchanged. So the record statistics depend on the
single ratio `g = V/t`, taken at `t = 1`. (3) On `chain6` the graded and ungraded sector matrices at `t = 1` and symbolic `V` are the same matrix
entrywise, at `N = 2` (dimension `15`) and `N = 3` (`20`), interaction and hopping alike, because every nearest-neighbour bond of a line joins
consecutive site indices and its string is empty. Hence `P_graded(g) = P_ungraded(g)` at every real `g`, and numerically the `L1` distance on
`chain6` at `N = 2` is `0.00e+00` at `g = 0` and `0.00e+00` at `g = 1`, below the `1e-12` witness threshold.

**Proof.** Item 1 solves `[H, n_A + n_B] = 0` and `E H E = H`, with `E` the exchange of the two factors, on a symbolic Hermitian `4 x 4` matrix
in `16` real parameters: the solution space has exactly `4` free real parameters, the four named operators are linearly independent as row
vectors, and the solved matrix is a combination of them with a unique coefficient vector. Constancy is the observation that `1` and `n_A + n_B`
restrict to multiples of the identity on the one-particle block. Item 2 builds `U` and verifies the displayed identity symbolically in `V`, both
compositions, both sectors. Item 3 builds both sector matrices symbolically and compares them entry by entry. Items 1 to 3 are exact; the closing
numbers are the numerical witness `A2`.

**Reading, not theorem.** Item 3 is why earlier ring and chain probes came back silent. In one dimension the string between nearest neighbours is
empty, so a nearest-neighbour law cannot see the cross-site sign at all; the probe was not weak, the geometry was.

## Theorem 2 — every ungraded member gives every pattern positive probability

**Conclusion.** On `grid2x3` at `N = 2` (sector dimension `15`) and `N = 3` (`20`), `cube` at `N = 4` (`70`) and `grid3x3` at `N = 3` (`84`): the
ungraded sector matrix at `t = 1` has zero diagonal at `V = 0`, is symmetric, and its off-diagonal part is exactly minus the `0/1` adjacency of
the configuration graph, every entry lying in `{0, -1}`; and that graph is connected, by exact breadth-first search. Since the interaction term
is diagonal, the sector matrix at every real `g` is `D(g) - A_config`, and by Perron-Frobenius applied to `cI - (D(g) - A_config)`, entrywise
nonnegative and irreducible for large enough `c`, its lowest eigenvalue is simple with a strictly positive eigenvector. Hence at every real `g`
the ungraded record statistics are strictly positive on every pattern: no ungraded member of the family forbids anything. As a numerical witness,
the smallest ground occupation probability over the sixteen cluster-sector-`g` cases with `g in {-2, 0, 1, 3}` is `2.34e-04`, above the `1e-06`
threshold.

**Proof.** The structural statements are exact and checked entry by entry on all four cluster-sector pairs. Off-diagonal values are `0` or `-1`
and never below, because two patterns differing by one hop fix the displaced record and its destination uniquely, hence a single bond, so no two
bonds contribute to one entry. Perron-Frobenius is invoked with its hypotheses verified exactly rather than assumed. The closing sentence is the
numerical witness `B2`.

**Consequence.** Whatever else the ungraded family can do, it cannot produce a zero, so every exact zero in the graded record statistics is by
itself a separation from the whole ungraded family at every real `g`; no distance computation is needed for the discrimination, and none is used
for it.

## Theorem 3 — the graded family has exact cancellation zeros, and no classical rule reproduces them

**Conclusion.** At `g = 0` the graded law is quadratic, so its `N`-record ground state is the Slater determinant of the `N` lowest orbitals of
`-A`, `A` the site adjacency. Exactly:

1. `grid2x3`, `N = 2`. The spectrum of `A` is `{+-1} + {sqrt2, 0, -sqrt2}`; the two lowest orbitals of `-A` are `phi_1 = (1,1)/sqrt2 (x) (1,
  sqrt2, 1)/2` at `-(1 + sqrt2)` and `phi_2 = (1,1)/sqrt2 (x) (1, 0, -1)/sqrt2` at `-1`, row factor times column factor; the ground energy is
  `-(2 + sqrt2)`, simple. Over all `15` pairs, `P(i, j) = |phi_1(i) phi_2(j) - phi_1(j) phi_2(i)|^2` is `0` on the `3` vertical pairs (both
  sites of one column), `1/16` on `8` pairs (the `4` horizontal adjacent pairs and the `4` adjacent-column pairs in different rows) and `1/8` on
  the `4` pairs at distance two along a row; they sum to `1`.
2. `cube`, `N = 4`. The spectrum of `A` is `{3, 1, 1, 1, -1, -1, -1, -3}`; the four lowest orbitals of `-A` are the product orbitals at `-3`,
  namely `(1,1)^{(x)3}/sqrt8`, and at `-1`, the three with one factor `(1,-1)`, the fifth level being `+1`; the ground energy is `-6`, simple.
  The `70` probabilities take values in `{0, 1/64, 1/16}` with counts `12`, `56`, `2`, summing to `1`, and the `12` zeros are exactly the `6`
  cube faces occupied and `6` patterns of two disjoint adjacent pairs.
3. `grid3x3`, `N = 3`. The spectrum of `A` is `{2 sqrt2, sqrt2, sqrt2, 0, 0, 0, -sqrt2, -sqrt2, -2 sqrt2}`; the three lowest orbitals of `-A` are
  `w1 (x) w1` at `-2 sqrt2` and `w1 (x) w2`, `w2 (x) w1` at `-sqrt2`, orthonormal, with `w1 = (1, sqrt2, 1)/2`, `w2 = (1, 0, -1)/sqrt2` and the
  next level `0`; the ground energy is `-4 sqrt2`, simple, so the ground state is unique. The `84` probabilities take values in `{0, 1/256,
  1/128, 1/64, 1/32, 9/256}` with counts `8, 12, 32, 20, 8, 4`, summing to `1`, and the `8` zeros are exactly the `3` rows, `3` columns and `2`
  diagonals.
4. The comparator fails on the smallest of these. On `grid2x3` at `N = 2` each of the `3` vertical and `4` horizontal adjacent pairs contains at
  least one bond of each type, `n_00, n_01, n_11 >= 1`, so a bond-product rule gives all seven zero or none zero, while the graded law gives `0`
  to exactly the `3` vertical pairs and `1/16` to each horizontal pair. No cubic-covariant classical nearest-neighbour Gibbs rule reproduces the
  graded record statistics.

**Proof.** The spectra are exact symbolic eigenvalue computations on the integer adjacency matrices of sizes `6`, `8` and `9`; each named orbital
is verified exactly as an eigenvector at its stated eigenvalue, and for `grid3x3` the three are verified pairwise orthonormal. The Slater
amplitudes are exact `N x N` determinants of the orbital matrix on the occupied rows, in `Z[sqrt2]`, and the probabilities their exact squares.
Each ground energy is certified exactly, independently of any numerical eigenvalue routine, by three facts: `H v = E v` and `v^T v = 1` for the
Slater vector `v`; the sector matrix is integer, so its characteristic polynomial has integer coefficients; and an exact Sturm root count returns
`0` eigenvalues below a rational bound just under `E` and `1` below one just over `E`. So `lambda_min = E`, simple, and the record statistics are
the squared amplitudes of `v`. Item 4 enumerates bond-type counts of the seven named patterns. Theorem 3 is exact throughout; no float appears in
it.

**Reading, not theorem.** The zeros are exact cancellations of a determinant, not accidental small numbers. On `grid2x3` the two occupied
orbitals share a row factor, so the determinant sees only the column indices and vanishes whenever they agree — every vertical pair. On `grid3x3`
the eight zeros are the eight collinear triples of the site grid, the three occupied orbitals sending the nine sites to the nine points of a `3 x
3` grid in an affine plane. This aligns computations and derives none.

## Bounded witness 4 — how far apart the two families are

**Statement, numerical.** For `grid2x3` at `N = 2` and `N = 3`, `cube` at `N = 4` and `grid3x3` at `N = 3`, with graded targets at `g_target in
{0, 1}`, scanning the ungraded family over `241` equally spaced points of `g in [-6, 6]` and refining by bounded scalar minimization around the
best grid point gives, for `min_g || P_ungraded(g) - P_graded(g_target) ||_1`,

```text
grid2x3 N=2   0.389 at g = 1.850  (g_t = 0)     0.296 at g =  6.000  (g_t = 1)
grid2x3 N=3   0.439 at g = -0.898 (g_t = 0)     0.375 at g =  1.567  (g_t = 1)
cube    N=4   0.333 at g = -1.483 (g_t = 0)     0.321 at g =  1.674  (g_t = 1)
grid3x3 N=3   0.373 at g = 1.571  (g_t = 0)     0.258 at g =  2.971  (g_t = 1)
```

All eight are at or above the declared `0.15` threshold, the smallest being `0.258`. The control is `chain6` at `N = 2`, where Theorem 1 makes an
exact match available: the same procedure returns `0.00e+00` at `g = 0.000` for `g_t = 0` and `0.00e+00` at `g = 1.000` for `g_t = 1`, below
`1e-09` and attained at `g = g_target`.

**Character of the witness.** These are floating-point numbers from `scipy` eigensolves and a bounded scalar minimizer, to three decimals, with a
`1e-9` tolerance detecting a degenerate ground space. They are minima over a scanned window, not over the real line: for `grid2x3` at `N = 2`
with `g_t = 1` the minimum sits at the scan endpoint `g = 6.000`, so `0.296` is an upper bound on the infimum over all real `g`, not a located
interior minimum. Theorems 1 to 3 do not depend on these numbers.

## Theorem 5 — the persistent zeros are a symmetry selection rule

**Conclusion.** A cluster automorphism `sigma` acts on the graded sector by `U_sigma |S> = sgn_S(sigma) |sigma S>`, a signed permutation, and on
the ungraded sector by `|S> -> |sigma S>`, unsigned; both commute with `H(1, V)` for symbolic `V`, and `sigma -> U_sigma` is a homomorphism of
image order `4`, `48`, `8`, the group orders. A simple ground vector is then an eigenvector of each `U_sigma` with character `chi(sigma) = +-1`,
so `amp(sigma S) = chi(sigma) sgn_S(sigma) amp(S)`; at `sigma S = S` this forces `amp(S) = 0` when `chi(sigma) sgn_S(sigma) = -1`. At `g = 0`:

1. `grid2x3`, `N = 2`: the rule forbids the `3` vertical pairs, all `3` of the exact zeros. Each is fixed by the row reflection, which swaps its
  two sites, an odd permutation, while the ground state is even under that reflection.
2. `cube`, `N = 4`: it forbids `12` patterns, all `12` of the exact zeros, the `6` occupied faces and `6` two-disjoint-adjacent-pair patterns.
3. `grid3x3`, `N = 3`: it forbids `4` patterns, `4` of the `8` exact zeros, the `4` lines through the centre, that is the middle row, the middle
  column and the two diagonals. The other four zeros, the outer rows and columns, are free-particle collinearity accidents seen only at `g = 0`.

Ungraded, `sgn_S(sigma) = 1` always and the strictly positive Perron-Frobenius ground vector of Theorem 2 forces `chi(sigma) = +1`, so
`chi sgn_S = +1` and the rule forbids nothing on any of the three clusters. The rule is coupling-independent as long as the ground state stays
simple: `chi` is a `+-1`-valued continuous function of `g` on any interval without a level crossing, hence constant. As a numerical witness, at
`g in {0, +-0.25, +-0.4, 0.5, 0.75, 1, 2}` the graded ground state is simple, smallest gap `0.534`, its zero set at the `1e-12` threshold contains
the predicted set, and the intersection of the nine zero sets is exactly the predicted set, `3`, `12` and `4`.

**Proof.** Items 1 to 3 and the ungraded statement are exact. The automorphisms are enumerated by backtracking; `U_sigma` is built as an explicit
signed permutation on the basis; commutation with the exact sector matrix, split into its integer `V^0` and `V^1` parts, is checked entrywise in
both compositions; the homomorphism is checked on all pairs, giving the image orders. The character is read off the exact Slater ground vector of
Theorem 3, verified on every basis pattern, so the eigenvector property is checked, not assumed. The last paragraph is the witness `E4`.

**Reading, not theorem.** Some record patterns are their own mirror image in a way a fermionic state cannot be, so they never form; that is what
the sign does to records.

## Corollary — what the test says

Within the cubic-covariant, record-conserving, nearest-neighbour family declared above, and on the four clusters named:

1. In one dimension the two compositions are indistinguishable by record statistics, and not merely close: they are the same matrix in every
  record-number sector, at every `g` (Theorem 1 item 3).
2. In two and three dimensions they are distinguishable, exactly. The graded law forbids patterns every ungraded member gives positive
  probability: `3` of `15` on `grid2x3`, `12` of `70` on the cube, `8` of `84` on `grid3x3` (Theorem 3), against strict positivity at every
  ungraded `g` (Theorem 2). This compares supports and needs no tolerance.
3. Quantitatively, and as a numerical witness only, the two distributions stay at least `0.258` apart in `L1` across the scanned window `g in
  [-6, 6]`, above the `0.15` threshold set in advance.
4. No classical bond-product rule reproduces the separation either: its zero set is bond-hereditary, so it cannot forbid a vertical adjacent pair
  while permitting a horizontal one.
5. Hence, for this family, the composition rule is not representational: not a relabelling that record statistics cannot see. The readable shadow
  of the cross-site sign is exact cancellation zeros in record patterns, in two and three dimensions and not in one.
6. The readable shadow of the cross-site sign is a coupling-independent selection rule: a record pattern fixed by a lattice symmetry is
  forbidden whenever that symmetry permutes the pattern's sites with a sign opposite to the state's symmetry character. In the ungraded
  composition no such rule exists.

## What does not move

- This does not decide which composition the framework has. It is a discriminator, not a verdict: the question has a finite, readable answer on
  clusters of this size, and nothing here says which answer holds.
- It does not touch laws outside the covariant record-conserving nearest-neighbour family. Ungraded laws with a different record dictionary,
  where a matter excitation is a thread of records rather than one site's occupation, are not addressed at all.
- It supplies no update rule, no formation site, no formation rate, and no values. No coupling, no absolute unit, and no dynamical clause appears
  anywhere in this note.
- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted: two constructions are declared and compared.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.

## Interfaces named for other lanes, not moved here

These interfaces are named so that a later note can consume them; nothing here moves them.

- The update-clause question. A composition rule is a statement about the algebra of two neighbouring sites, and becomes meaningful for the
  framework once a tick is given a clause saying what it does to the joint state of a neighbourhood. This note gives the readable consequence for
  a stationary lowest-energy state and no update clause; a lane writing one should treat Theorem 3 as the target its clause must reproduce or
  contradict.
- A lane wanting fermionic record statistics from an ungraded lattice must leave this family. Theorem 2 is a complete obstruction inside it:
  strict positivity holds for every ungraded member at every real `g`, so the exact zeros of Theorem 3 are unreachable. The constructions known
  to give fermionic statistics from ungraded site algebras are string-net and gauge-constrained laws, whose bond terms are not of the declared
  form; naming them points at standard methodology, with no note here to cite.
- The one-dimensional identity is the Jordan-Wigner locality of one dimension and nothing more, and it is why earlier ring and chain probes could
  not see the sign (plain-text pointer, no grade, no weight: `RING_MONODROMY_DOES_NOT_FORCE_CAR_NOTE_2026-06-04.md`). A lane repeating such a
  probe needs a cluster of dimension two or higher.

## Remaining live routes

1. Larger clusters and other geometries. Nothing is claimed beyond the four named clusters; whether the zero counts `3/15`, `12/70`, `8/84`
  follow a pattern on larger grids is a separate computation.
2. Nonzero `g` for the graded law by exact means. The graded targets at `g = 1` enter only through the numerical witness, and the interacting
  graded law has no free-fermion structure to lean on.
3. Broader law families: longer-range bonds, laws breaking bond-reversal symmetry, laws not conserving the record number, ungraded laws under a
  different record dictionary. Theorem 2 says nothing about them.
4. Whether the infimum of the `L1` distance over the whole real line, rather than the scanned window, is attained and what it equals. Bounded
  witness 4 leaves this open; one of its eight values sits at a scan endpoint.

## Executable claim block

The canonical machine-bound restatement of the four theorem conclusions and the bounded witness.

```text
clusters_and_bonds: chain6 6/5, grid2x3 6/7, cube 8/12, grid3x3 9/12
compositions_and_shared_record: ungraded b_i = a at site i; graded c_i = Jordan-Wigner, s3 string before i; n_i = b_i^dag b_i = c_i^dag c_i
law_family: H(t,V) = -t sum_bonds (x_i^dag x_j + x_j^dag x_i) + V sum_bonds n_i n_j, x = b or c
two_qubit_covariant_span_dimension_and_basis: 4; 1, n_A + n_B, n_A n_B, b_A^dag b_B + b_B^dag b_A
t_sign_gauge_and_family_parameter: U = (-1)^{N_A} on {0,2,4}, U H(1,V) U = H(-1,V); g = V/t at t = 1
chain6_sector_dimensions_matrix_identity_and_l1: 15 and 20, identical entrywise; 0.00e+00 at g = 0 and g = 1, threshold 1e-12
ungraded_offdiagonal_and_connectivity: entries {0, -1}, minus the configuration adjacency; connected at grid2x3 N=2 15, N=3 20, cube N=4 70, grid3x3 N=3 84
ungraded_ground_vector_and_min_probability: simple and strictly positive at every real g; 2.34e-04 over 16 cases, threshold 1e-06
grid2x3_spectrum_orbitals_ground_energy_and_probabilities: {+-1} + {sqrt2, 0, -sqrt2}; -(1 + sqrt2) and -1; -(2 + sqrt2), multiplicity 1; 0 x 3, 1/16 x 8, 1/8 x 4, sum 1
cube_orbitals_ground_energy_probabilities_and_zeros: -3 x 1, -1 x 3, then +1; -6, multiplicity 1; 0 x 12, 1/64 x 56, 1/16 x 2, sum 1; 6 faces occupied, 6 pairs of disjoint adjacent pairs
grid3x3_three_lowest_orbitals_next_level_and_ground_energy: -2 sqrt2 x 1, -sqrt2 x 2, then 0; -4 sqrt2, multiplicity 1
grid3x3_probabilities_and_zero_patterns: 0 x 8, 1/256 x 12, 1/128 x 32, 1/64 x 20, 1/32 x 8, 9/256 x 4, sum 1; the 3 rows, 3 columns, 2 diagonals
classical_comparator: n00, n01, n11 >= 1 on all 3 vertical and 4 horizontal pairs; no bond-product rule reproduces the zero set
scan_points_and_window: 241 on [-6, 6], bounded refinement
l1_minima_grid2x3: N=2 0.389 at g = 1.850 and 0.296 at g = 6.000; N=3 0.439 at g = -0.898 and 0.375 at g = 1.567
l1_minima_cube_N4_and_grid3x3_N3: 0.333 at g = -1.483 and 0.321 at g = 1.674; 0.373 at g = 1.571 and 0.258 at g = 2.971
l1_minimum_over_all_eight_threshold_and_control: 0.258 and 0.15; chain6 0.00e+00 at g = 0.000 and 1.000, threshold 1e-09
cluster_automorphisms_and_action: 4, 48, 8 on grid2x3 N=2, cube N=4, grid3x3 N=3; graded U_sigma |S> = sgn_S(sigma) |sigma S>, ungraded unsigned; commutes with H(1,V); image order 4, 48, 8
character_predicted_zeros_and_persistence: chi = +-1 at g = 0; predicted inside exact, 3 of 3, 12 of 12, 4 of 8; ungraded chi = +1, predicted set empty; over g in {0, +-0.25, +-0.4, 0.5, 0.75, 1, 2} simple, gap 0.534, intersection = predicted, 3, 12, 4
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=19 FAIL=0
```

## Proof boundary

Every statement is proved on the four named finite clusters with open boundaries, inside record-number sectors of dimensions `15`, `20`, `70` and
`84`. Nothing is claimed about larger clusters, periodic boundaries, infinite lattices, other geometries, or any law outside the declared family,
which is complete under the stated symmetries and is not widened: Theorem 1 item 1 shows that record conservation, bond-reversal symmetry and one
identical bond expression on every bond leave exactly four Hermitian operators per bond, two of them constants inside a sector, so `H(t, V)` with
`g = V/t` is the whole family and "every ungraded member" means every member of it and nothing more. The free-fermion targets at `g = 0` are
exact, ground energies, simplicity and rational multisets alike, the certificates being exact Sturm root counts on integer characteristic
polynomials at rational bounds rather than numerical estimates. The graded targets at `g = 1` and every `L1` distance are numerical, floating
point, so labelled in the runner and above: they carry a `1e-9` degeneracy tolerance and are minima over a scanned window of `241` points with
bounded refinement rather than proved minima over the real line, one of the eight sitting at a scan endpoint. The selection rule of Theorem 5 is
proved for simple ground states and stated for the coupling range without a level crossing; its persistence is exhibited numerically at the nine
listed couplings and argued by continuity of a `+-1`-valued character. Perron-Frobenius is applied with its hypotheses verified exactly on each
cluster and sector rather than assumed; the Slater-determinant identification of the ground state is standard methodology and is not relied on,
since each ground energy is separately certified. No axiom is amended, no status is set, and no registry entry is created.

## Review record

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the three
context notes in "Imports and authority" are plain-text pointers carrying no grade and no weight. Every exact claim is checked in `sympy` with
`Rational`, `sqrt(2)` and integer matrices; every numerical claim is computed in `numpy` and `scipy` and carries a `[numerical]` tag and its
tolerance in the runner label. Hard landing conditions are a fresh runner and cache pair closing at `PASS=19 FAIL=0` with runtime under `120`
seconds and stdout under `5500` characters, a current zero-dependency citation-manifest entry, and passing repository pipeline, strict-lint, and
changed-evidence gates; independent audit remains a separate lane.
