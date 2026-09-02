---
claim_id: born_form_parity_even_readable_algebra_bounded_theorem_note_2026-09-01
claim_type: bounded_theorem
claim_scope: "Under a declared grading hypothesis, the parity-even part of the one-site algebra M_2(C) is span{1, n} with n = E11, the even effects are exactly a(1-n) + b n with a, b in [0,1], and the even rank-one projectors are exactly n and 1-n. Every effect-additive normalized functional on that even effect algebra is the one-parameter trace form m(a(1-n) + b n) = a(1-p) + b p = Tr(diag(1-p, p) E) with p = m(n); on the dyadic grid of step 1/8 additivity together with m(1) = 1 determines m at all 81 grid points from m(n) alone, and positivity is exactly p in [0,1]. At one site the even sector carries no trine and no rogue carrier: three scaled rank-one even effects summing to the identity always repeat a direction, and the frame function g = 1/2 + n_z^3/2 agrees with the trace form exactly at the two even directions and differs off them. At two sites with total parity P = s3 (x) s3 the even subalgebra is the commutant of P, of complex dimension 8, and is M_2(C) (+) M_2(C) in the parity basis {|00>, |11>} (+) {|01>, |10>}; the positive normalized functionals on it are exactly the parity-diagonal trace forms Tr(sigma .) with each block positive semidefinite; the even projector onto (|01> + |10>)/sqrt(2) carries Born values 1, 1/2, 0 and fails to commute with |01><01|; and the trine reappears inside the odd-parity block as three even effects of spectrum {0, 2/3}, none a projector and none one-site. For every parity-diagonal two-site state the one-site marginal is diag(1-p, p) with vanishing odd part, a record locking n_x = 1 gives Born values exactly 1 and 0, and all eight odd two-site Pauli strings take the value zero. The grading hypothesis is declared by this note and consumed from no row. No axiom is amended and no status is set."
upstream_dependencies: []
runner: scripts/born_form_parity_even_readable_algebra_check_2026_09_01.py
---

# The Born form on the parity-even readable algebra: one probability at one site, a trace form at two

**Date:** 2026-09-01
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/born_form_parity_even_readable_algebra_check_2026_09_01.py`](../scripts/born_form_parity_even_readable_algebra_check_2026_09_01.py)
**Runner cache:**
[`logs/runner-cache/born_form_parity_even_readable_algebra_check_2026_09_01.txt`](../logs/runner-cache/born_form_parity_even_readable_algebra_check_2026_09_01.txt)
**Parents:** none. Every premise used below is declared in this note.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-dimensional theorem on one and two sites: the even effect algebra and its unique one-parameter Born form, the two-site even algebra and its trace forms, and the record-versus-reconstruction split."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-dimensional theorem and route the declared grading hypothesis to the owner as a science-level decision."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

One site carries `M_2(C)`; two sites carry `M_4(C)` in the basis `|00>, |01>, |10>, |11>`. The target is the conjunction of the three statements
below, which are exactly the three check groups `A`, `B`, `C` of the primary runner.

1. `T1` (`A`). Under the declared hypothesis the parity-even part of `M_2(C)` is `span{1, n}` with `n = E11`; the even effects are exactly
   `a(1-n) + b n` with `a, b in [0,1]`; the even rank-one projectors are exactly `n` and `1-n`; every effect-additive normalized functional on the
   even effects is the one-parameter trace form with `p = m(n)`; and at one site the even sector carries no trine and no rogue carrier.
2. `T2` (`B`). At two sites with `P = s3 (x) s3` the even subalgebra has complex dimension `8` and is `M_2(C) (+) M_2(C)` in the parity basis; its
   positive normalized functionals are exactly the parity-diagonal trace forms; a genuinely noncommutative even Born value exists; and the trine
   reappears inside the odd-parity block as three even non-projective effects that are not one-site.
3. `T3` (`C`). For every parity-diagonal two-site state the one-site marginal is `diag(1-p, p)` with `p = Tr(sigma n_x)` and vanishing odd part; a
   record locking `n_x = 1` gives Born values exactly `1` and `0`; and every such state gives `0` to each of the eight odd Pauli strings.

## Declared hypothesis

The following is a hypothesis declared by this note. It is not axiom content, it is consumed from no row, and it carries no dependency weight.

```text
Grading hypothesis (declared): the site algebra M_2(C) carries the parity grading Ad(s3)
(even = span{E00, E11}, odd = span{E01, E10}); distinct sites compose by the graded
product; a state is readable only through its parity-even content.
```

It mirrors a candidate clause recorded elsewhere as a science-level decision awaiting its owner, plain-text pointer with no grade and no weight:
`MATTER_GRADED_COMPOSITION_AXIOM_UPDATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md`, "no grade, no weight". Nothing here amends, extends, or
reinterprets an axiom, and nothing here sets a status of any kind. Every theorem below is conditional on the displayed hypothesis; read without
it, the theorems are statements about the commutant of `s3` and the commutant of `s3 (x) s3`, which is what the runner actually computes.

## Imports and authority

Imported scientific authority: none load-bearing. Effect algebras, frame functions on the qubit, and the positivity characterization of trace
forms are standard methodology; every object is redeclared here and every statement is recomputed in full by the primary runner. No observational
value, no fitted number, and no framework premise enters any proof. Non-load-bearing context pointers, plain file names with no grade and no
dependency weight:

- `MATTER_GRADED_COMPOSITION_AXIOM_UPDATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md` (whose clause the hypothesis mirrors).
- `BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md` (the one-site bridge whose one-site marginal trace form the
  Corollary re-derives inside the even sector).

This note re-declares everything it uses and cites none of their grades.

## Obligation graph

The proof is acyclic. Each node after `P0` is checked by the correspondingly lettered runner group.

1. `P0` (declared here): the Pauli matrices, the matrix units of `M_2(C)`, `n = E11`, the grading `Ad(s3)`, the dyadic grid, the two-site basis,
   `P = s3 (x) s3`, the pseudo-qubit operators of the odd block, and the trine directions.
2. `P1` (`A`): the even part, the even effects, the even rank-one projectors, the one-parameter Born form and its converse on the grid, the
   absence of an even trine, and the rogue frame function on the even directions.
3. `P2` (`B`): the two-site even subalgebra, its block isomorphism, its states and functionals, the even Born value, and the relocated trine.
4. `P3` (`C`): the parity-diagonal marginal, the locked record, and parity superselection at two sites.

The strongest supported scope is precisely `P0`--`P3`.

## Definitions

Write `one` for the `2 x 2` identity, `s1, s2, s3` for the Pauli matrices, and `E00, E01, E10, E11` for the matrix units of `M_2(C)`, with
`E01 = |0><1|` and `n = E11`. The **parity grading** of the site algebra is `Ad(s3)`, whose `+1` eigenspace is `span{E00, E11}` and whose `-1`
eigenspace is `span{E01, E10}`. An **effect** is a Hermitian `X` with `0 <= X <= 1`. The **even effect algebra** is
`E_even = { a(1-n) + b n : a, b in [0,1] }`, with dyadic grid `a, b in {k/8 : k = 0..8}`. A functional `m` on `E_even` is **effect-additive** when
`m(E + F) = m(E) + m(F)` for every pair with `E + F <= 1`, **normalized** when `m(1) = 1`, and **positive** when `m(E) >= 0` for every `E`. Two
sites carry `M_4(C)` in the basis `|00>, |01>, |10>, |11>`, with **total parity** `P = s3 (x) s3`, **even block** `{|00>, |11>}`, **odd block**
`{|01>, |10>}`, and `n_0 = n (x) one`, `n_1 = one (x) n`. The **even subalgebra** at two sites is the commutant of `P`. Inside the odd block the
**pseudo-qubit operators**, block identity, and block projector are

```text
t1 = |01><10| + |10><01|,  t2 = -i|01><10| + i|10><01|,  t3 = |01><01| - |10><10|,
1_b = |01><01| + |10><10|,  P_b(v) = (1_b + v.t)/2.
```

The **trine directions** are the three coplanar unit vectors at `120` degrees in the `(1,3)`-plane, `v_0 = (0,0,1)`, `v_1 = (sqrt(3)/2, 0, -1/2)`,
`v_2 = (-sqrt(3)/2, 0, -1/2)`, with `v_0 + v_1 + v_2 = 0`. The **rogue frame function** is `g(n_hat) = 1/2 + n_z^3/2`, which satisfies
`g(n_hat) + g(-n_hat) = 1` and is not a trace form on the full sphere.

## Theorem 1 — the one-site even sector carries one probability

**Conclusion.** Under the declared hypothesis: (1) the parity-even part of `M_2(C)` is the commutant of `s3`, equal to `span{1, n}` of complex
dimension `2`, the odd part `span{E01, E10}` carrying the eigenvalue `-1` of `Ad(s3)`; (2) an even Hermitian `X = a(1-n) + b n` has spectrum
`{a, b}` and `1 - X` has spectrum `{1-a, 1-b}`, so `0 <= X <= 1` exactly when `a, b` lie in `[0,1]`, and the even effects are exactly `E_even`;
(3) `P = P^2 = P^dagger` with `[P, s3] = 0` has exactly four solutions `0, n, 1-n, 1`, the rank-one ones being exactly `n` and `1-n`; (4) with
`p := m(n)`, effect-additivity and normalization force

```text
m(a(1-n) + b n) = a(1-p) + b p = Tr(diag(1-p, p) E),
```

that form being additive on every grid pair with `E + F <= 1`, normalized, and nonnegative, while conversely on the dyadic grid additivity with
`m(1) = 1` determines `m` at all `81` grid points from `m(n)` alone, leaving exactly one free parameter, the determined values being exactly the
displayed form, and since `m(n) = p` and `m(1-n) = 1-p` positivity is exactly `p in [0,1]`; (5) there is no even trine: the `M_2(C)` trine
`(2/3) P(v_k)` does resolve the identity, each member rank one, Hermitian, and not a projector, but exactly one of the three is parity-even, and
on the rational grid `c in {k/6 : k = 1..6}` there are `30` triples of scaled rank-one even effects summing to `1`, every one of them repeating a
direction and none using three pairwise distinct directions; (6) there is no even rogue carrier: `g` satisfies `g(n_hat) + g(-n_hat) = 1` and
equals `Tr(diag(1,0) P(n_hat))` at the two even directions, `g(+z) = 1` and `g(-z) = 0`, while off them it differs, giving `9/16` against the
trace value `3/4` at the unit vector `(sqrt(3)/2, 0, 1/2)`.

**Proof.** Item 1 solves `[X, s3] = 0` for a symbolic `2 x 2` matrix: the solution space has complex dimension `2` and equals
`span{1-n, n} = span{1, n}`. Item 2 is the symbolic spectrum of a diagonal matrix and of its complement. Item 3 solves `P^2 = P`, `P^dagger = P`,
`[P, s3] = 0` simultaneously; the four solutions are exhibited and the two of rank `1` identified. In item 4 the direct half is the exact identity
`a(1-p) + b p = Tr(diag(1-p, p)(a(1-n) + b n))`, checked symbolically, with additivity on all grid pairs having `E + F <= 1` and nonnegativity on
the grid of `(a, b, p)`. The converse half solves the linear system generated by the unit-step additivity instances

```text
m((j+1)/8 (1-n) + k/8 n) = m(j/8 (1-n) + k/8 n) + m(1/8 (1-n)),
m(j/8 (1-n) + (k+1)/8 n) = m(j/8 (1-n) + k/8 n) + m(1/8 n),   with m(1) = 1;
```

each is an instance of the hypothesis because both coordinates of the sum stay at or below `1`. The solution space is one-dimensional and every
grid value equals `(j/8)(1-p) + (k/8)p` with `p = m(n)`; the runner separately verifies that this one-parameter family satisfies every additivity
instance, not merely the unit-step ones, so the solution set of the full system is exactly that family. Item 5 is the stated enumeration, together
with the observation that by item 3 there are two even rank-one directions in all, so three distinct ones are unavailable. Item 6 evaluates.

**Reading, not theorem.** Items 5 and 6 are the two features that make the qubit a special case in the standard effect-algebra treatment, and both
belong to the odd sector: the trine needs directions off the grading axis, and the rogue is a rogue through its behaviour off that axis.
Restricted to the even sector both disappear. This observes two computations, deriving neither.

## Theorem 2 — two sites: the even algebra, its trace forms, and the relocated trine

**Conclusion.** With `P = s3 (x) s3`: (1) the even subalgebra, the commutant of `P`, has complex dimension `8`, all eight cross-block entries
vanish identically, and the eight in-block matrix units span it; (2) the parity-basis block map `M_2(C) (+) M_2(C) -> commutant(P)` is a unital
`*`-isomorphism, additive, multiplicative, adjoint-compatible, and landing in the commutant, verified on symbolic blocks; (3) a parity-diagonal
Hermitian `sigma` is exactly `sigma_+ (+) sigma_-`, an `8`-real-parameter family, and `E -> Tr(sigma E)` is additive, gives `Tr(sigma)` at
`E = 1`, and splits as `Tr(sigma_+ E_+) + Tr(sigma_- E_-)`, its positivity being the exact identity
`Tr(A A^dagger B B^dagger) = sum_ij |(B^dagger A)_ij|^2` applied with `sigma = A A^dagger` and `E = B B^dagger`; (4) conversely every linear
functional on the `8`-dimensional even algebra is `Tr(sigma .)` for one and exactly one even `sigma`, the `8`-by-`8` trace-pairing system having a
unique solution in the eight prescribed values; (5) positivity on the rank-one even projectors of each block forces each block positive
semidefinite, since for a Hermitian block `[[r, x+iy], [x-iy, s]]` and `v = (1, z1 + i z2)` both of

```text
Q = r + 2(x z1 - y z2) + s(z1^2 + z2^2),    s Q = (s z1 + x)^2 + (s z2 - y)^2 + (r s - x^2 - y^2)
```

are exact identities, so for `s > 0` nonnegativity of `Q` for all `v` is exactly `r s >= x^2 + y^2` while `r = Q(0)` and `s = <e_1|block|e_1>` are
values of the same test, and for `s = 0` the substitution `(z1, z2) = (-t x, t y)` gives `r - 2t(x^2 + y^2)`, forcing `x = y = 0`; (6) a genuinely
noncommutative even Born value exists, the projector `Q` onto `(|01> + |10>)/sqrt(2)` commuting with `P` and `Tr(sigma Q)` equalling `1` in the
state `Q`, `1/2` in `|01><01|`, and `0` in `|00><00|`, with `Q` failing to commute with `|01><01|`; (7) the trine relocates, the three effects
`(2/3) P_b(v_k)` built inside the odd-parity block commuting with `P`, being Hermitian of spectrum `{0, 2/3}`, pairwise non-proportional, and
summing to `1_b`; (8) none of the three is a projector and none is one-site, since `{M (x) 1}` and `{1 (x) M}` span a `7`-dimensional space and
adjoining any one of the three raises the rank to `8`.

**Proof.** Items 1 and 2 solve `[Y, P] = 0` for a symbolic `4 x 4` matrix, giving eight free entries and eight identically vanishing cross-block
entries, followed by symbolic verification of the block map on generic `2 x 2` blocks. Item 3 is the same solve for a symbolic Hermitian matrix in
real parameters, together with the trace identities, all exact. Item 4 solves the eight equations `Tr(sigma F_i) = f_i` for the eight in-block
matrix units `F_i`; the solution is unique and every even entry is a combination of the `f_i`, which is nondegeneracy of the trace pairing on the
even algebra. Item 5 is the two displayed identities plus the two substitutions, all verified symbolically. Items 6, 7 and 8 are direct exact
computations, the rank statements taken on stacked row vectors.

**Consequence.** The distinction between effects and projectors, at one site the whole content of the trine, is at two sites a statement inside
the even sector: the `(2/3) P_b(v_k)` are even effects, not projectors, and not one-site. The structure does not vanish here; it moves to two sites.

## Theorem 3 — records register, reconstructions carry weights

**Conclusion.** For two sites under the declared hypothesis: (1) for every parity-diagonal Hermitian `sigma` of trace `1` the one-site marginal at
each site is `diag(1-p, p)` with `p = Tr(sigma n_x)`, its off-diagonal entries vanishing identically, so its odd part, the `s1` and `s2`
components, is zero; (2) a record locking `n_x = 1`, that is a state with `n_x sigma = sigma` and `Tr(sigma) = 1`, gives Born value exactly `1` on
the even effect `n_x` and exactly `0` on `1 - n_x`, so on the two-outcome even readout `{n_x, 1 - n_x}` the value is a Kronecker delta; (3) parity
superselection holds at two sites, in that with `P_+ = (1 + P)/2`, `P_- = (1 - P)/2` and symbolic `4 x 4` matrices `X, Y` the parity-diagonal form
`sigma = P_+ X P_+ + P_- Y P_-` gives the value `0` to each of the eight odd two-site Pauli strings, those with an odd number of factors drawn
from `{s1, s2}`, while the eight even strings take nonzero values on it.

**Proof.** Item 1 is the partial trace of the general parity-diagonal trace-one matrix over either factor: the two contributions to each marginal
off-diagonal entry are cross-block entries of `sigma` and vanish, and the surviving diagonal entry at each site is `Tr(sigma n_x)`. Item 2 solves
`n_x sigma = sigma` with `Tr(sigma) = 1` for a symbolic Hermitian `sigma` in real parameters; the solution satisfies `sigma n_x = sigma` as well,
so `Tr(sigma n_x) = 1` and `Tr(sigma (1 - n_x)) = 0`, and the explicit lock `|01><01|` is exhibited. Item 3 is the exact trace computation for all
sixteen two-site Pauli strings, the odd ones identified by their anticommutation with `P`.

**Reading, not theorem.** Items 2 and 3 are the framework's "register, not read" in its own words: records register even content, reconstructions
carry the weights. A record surface returns a Kronecker delta, never an intermediate weight; the weights of item 1 and of Theorem 2 item 6 belong
to multi-site even observables. This aligns two computations and derives neither.

## Corollary — what this replaces

Under the declared hypothesis, and on the one-site and two-site surfaces proved above:

1. The one-site effect-additive trace-form statement, the content that the bridge
   `BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md` supplies to its consumers as a one-site marginal trace
   form (plain-text pointer, no grade, no weight), is here the one-parameter Bernoulli form of Theorem 1 item 4: a single number `p in [0,1]`,
   with no trine and no rogue carrier at one site (Theorem 1 items 5 and 6). A consumer of that form receives the same object here.
2. The distinction between effects and projectors, which the one-site bridge was written to supply, relocates to two sites in the even sector
   (Theorem 2 items 6, 7, 8). It is neither lost nor weakened; it is two-site content.
3. Born values on the record surface are Kronecker deltas, and Born values on reconstructions, meaning multi-site even observables, are trace
   forms (Theorem 3). In the framework's own words this is "register, not read": records register even content; reconstructions carry the weights.

## What does not move

- No weight values move. The parameter `p` of Theorem 1 and the blocks `sigma_+, sigma_-` of Theorem 2 stay free throughout; nothing here
  computes, constrains, or predicts any of them.
- No state is selected. Theorem 2 exhibits an eight-parameter state family and three different Born values on one even projector.
- No formation rule and no dynamics are supplied: no Hamiltonian, action, rate, coupling, or absolute unit appears.
- No axiom text is amended, extended, reworded, or reinterpreted, and the grading hypothesis is declared here rather than consumed from a row.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.

## Interfaces named for other lanes, not moved here

These interfaces are named so that a later note can consume them; nothing here moves them.

- Lanes consuming a one-site marginal trace form: by Corollary item 1 they receive the same object under the declared hypothesis, and may cite
  Theorem 1 in place of the bridge if they want the narrower premise.
- Lanes needing a non-projective effect decomposition: by Theorem 2 item 7 the earliest place one exists in the even sector is two sites, inside
  the odd-parity block; a lane needing one at a single site names odd content as readable and must say so.
- Lanes that source on records: by Theorem 3 item 2 the record-surface value is `1` or `0`, so a source density built from record readouts is
  integer-valued on this surface. No coupling and no absolute unit is supplied here.

## Remaining live routes

1. Three or more sites: nothing here is claimed beyond two, the commutant of a longer parity string being a separate computation.
2. A derivation of the grading hypothesis itself, rather than its declaration, from the axioms and the approved primitives. This note proves
   nothing about whether such a derivation exists.
3. Functionals on the two-site even algebra defined on effects rather than on the whole algebra: Theorem 2 item 4 takes linearity as given, the
   linear-extension step being treated below as standard.

## Executable claim block

The canonical machine-bound restatement of the three theorem conclusions.

```text
site_algebra_and_declared_grading: M_2(C) with Ad(s3), even = span{E00,E11}, odd = span{E01,E10}
one_site_even_part: span{1, n} with n = E11, complex dimension 2
even_effects: a(1-n) + b n with a, b in [0,1]
even_projector_solutions: 4, the rank-one ones exactly n and 1-n
one_site_born_form: m(a(1-n)+bn) = a(1-p) + b p = Tr(diag(1-p,p) E)
one_site_free_parameters_and_range: 1, p in [0,1]
dyadic_grid_step_and_points: 1/8 and 81
one_site_trine_members_parity_even: 1 of 3
even_trine_grid_solutions: 30, with three distinct directions 0
rogue_frame_function: 1/2 + n_z^3/2
rogue_versus_trace: 1 and 0 at both even directions, 9/16 against 3/4 off them
two_site_even_algebra: commutant of P = s3 (x) s3, M_2(C) (+) M_2(C), complex dimension 8
parity_basis_and_forced_zero_cross_entries: {|00>,|11>} (+) {|01>,|10>}, 8
parity_diagonal_hermitian_parameters_and_representing_sigma: 8 and 1
block_positivity_condition: r >= 0, s >= 0, r s >= x^2 + y^2
noncommutative_even_born_values: 1, 1/2, 0
relocated_trine: scale 2/3, spectrum {0, 2/3}, block {|01>, |10>}
one_site_image_span_dimension: 7, with one relocated trine member 8
marginal_form_and_odd_part: diag(1-p, p) and 0
record_born_values: 1 and 0
odd_two_site_pauli_strings_and_values: 8 and 0
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=19 FAIL=0
```

## Proof boundary

Every statement is proved on one site and on two sites, in complex dimensions `2` and `4`. Nothing is claimed about three or more sites, about
infinite lattices, or about any algebra other than `M_2(C)` and `M_4(C)`. The grading hypothesis is declared, not derived, and every theorem is
conditional on it; nothing is claimed about whether it follows from anything else. The step from effect-additivity to linearity is the standard
finite-dimensional argument, recomputed here on the spanning grid rather than proved as a new theorem: the dyadic grid of Theorem 1 item 4 spans
the even effects, additivity determines the functional on it, and the extension to the real span is the usual one. Theorem 2 item 4 takes
linearity as given and proves representation and uniqueness. The rogue statement concerns named directions, not a classification of frame
functions. No axiom is amended, no status is set, and no registry entry is created.

## Review record

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", the grading hypothesis is displayed
verbatim in "Declared hypothesis" and used nowhere implicitly, and both context notes named in "Imports and authority" are plain-text pointers
carrying no grade and no weight. Hard landing conditions are a fresh exact runner and cache pair closing at `PASS=19 FAIL=0` with runtime under
two seconds and stdout under `5500` characters, a current zero-dependency citation-manifest entry, and passing repository pipeline, strict-lint,
and changed-evidence gates; independent audit remains a separate lane.
