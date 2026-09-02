---
claim_id: cubic_response_even_sector_hopping_relocation_bounded_theorem_note_2026-09-01
claim_type: bounded_theorem
claim_scope: "Under a declared parity-grading hypothesis the proper-cubic classification of real-linear neighbor responses is recomputed and its record-faithfulness corollary is inverted at one site, while the first-order directed response relocates to the hopping channel of the graded product. The closure of Rz and Rx is the 24-element group of integer rotations of determinant +1; each permutes the six directed unit vectors, and R -> Pi_R is an injective homomorphism onto a 6x6 permutation group of order 24. The real-linear maps L : R^6 -> Herm(2) equivariant for that action, written L(c) = alpha(c) 1 + beta(c).Gamma with Gamma_mu = s_mu obeying {Gamma_mu, Gamma_nu} = 2 delta_{mu nu} 1, form a space of real dimension exactly 2, spanned by c -> [sum_d c_d] 1 and c -> sum_mu (c_{+mu} - c_{-mu}) Gamma_mu. For F(c) = a [sum_d c_d] 1 + b sum_mu (c_{+mu} - c_{-mu}) Gamma_mu with nonzero vector part v the nontrivial spectral projectors are (1 +- v_hat.Gamma)/2, parity-even exactly when v is parallel to e_3; at c = e_{+1} they are (1 +- s1)/2 and fail to commute with s3, at c = e_{+3} they are E00 and E11 and commute with it. Requiring the rank-one record possibilities to be the nontrivial spectral projectors and to be parity-even at c = e_{+1} and c = e_{+2} has the unique solution b = 0, leaving the scalar response F(c) = a [sum_d c_d] 1; at (a, b) = (-1, 0) with c_d = u_d - u_0 this is minus the seven-point graph Laplacian times 1, with one eigenvalue of multiplicity 2, so its spectral projector is 1 of rank 2 and it carries no rank-one content. On the graded product the hopping bilinears are parity-even: Jordan-Wigner on the three-site line gives c_1^dag c_0 and c_1^dag c_2 commuting with the total parity and with the number operator and restricting on the one-particle subspace to the matrix units E_{1,0} and E_{1,2}. The real-linear equivariant maps M : R^6 -> Herm(7) valued in the twelve-dimensional hopping span of the seven-site star form a space of real dimension exactly 6, not 2, the real commutant of the directed-neighbor permutation representation being span{1, S, J} of dimension 3 and acting in both the transposition-even and the transposition-odd channel; H_A(c) = sum_d c_d (E_{0,d} + E_{d,0}) and H_T(c) = i sum_d c_d (E_{0,d} - E_{d,0}) are two of the six basis maps. On the directed input c = e_{+1} - e_{-1} the operator H_T is the centered first-order difference along direction 1 with no internal Clifford factor; on the L = 3 and L = 4 rings the directed hop has eigenvalue multiset {2 sin(2 pi m / L)} and the symmetric hop {2 cos(2 pi m / L)}. On the 3x3x3 block the three first-difference operators are Hermitian, commute pairwise, have nonvanishing anticommutators, and their squares sum to an operator whose diagonal is the coordination numbers 3, 4, 5, 6 with trace 108, so no Clifford relation arises from the hopping channels alone. The grading hypothesis is declared by this note and consumed from no row. No axiom is amended and no status is set."
upstream_dependencies: []
runner: scripts/cubic_response_even_sector_hopping_relocation_check_2026_09_01.py
---

# The cubic neighbor response under the grading: scalar at one site, hopping in the directed-edge channel

**Date:** 2026-09-01
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/cubic_response_even_sector_hopping_relocation_check_2026_09_01.py`](../scripts/cubic_response_even_sector_hopping_relocation_check_2026_09_01.py)
**Runner cache:**
[`logs/runner-cache/cubic_response_even_sector_hopping_relocation_check_2026_09_01.txt`](../logs/runner-cache/cubic_response_even_sector_hopping_relocation_check_2026_09_01.txt)
**Parents:** none. Every premise used below is declared in this note.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-dimensional theorem on one site, the seven-site star, two rings and a 3x3x3 block: the cubic classification recomputed, the effect of a declared grading on its record-faithfulness corollary, and the equivariant hopping channels of the graded product."
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

The target is the conjunction of the three statements below, which are exactly the three check groups `A`, `B`, `C` of the primary runner.

1. `T1` (`A`). The proper cubic rotations form a 24-element group acting on the six directed unit vectors by permutation; the real-linear equivariant maps `R^6 -> Herm(2)` form
   a space of real dimension exactly `2`, spanned by the scalar and the directed-vector map; and the spectral projectors of the realized response are parity-even exactly when
   its vector part is parallel to `e_3` or vanishes.
2. `T2` (`B`). Under the declared hypothesis, even faithfulness at the witnesses `c = e_{+1}` and `c = e_{+2}` forces `b = 0`, so cubic equivariance leaves the scalar response;
   and that scalar point is a graph-Laplacian-type multiple of `1` with no rank-one spectral content at one site.
3. `T3` (`C`). Hopping bilinears of the graded product are parity-even and restrict on the one-particle subspace to matrix units; the equivariant maps into the
   twelve-dimensional hopping span of the star form a space of real dimension exactly `6`; the directed channel carries the ring symbol `2 sin k` against the symmetric
   channel's `2 cos k`; and the three directional first differences commute on the block, so no Clifford relation arises from the hopping channels alone.

## Declared hypothesis

The following is a hypothesis declared by this note. It is not axiom content, it is consumed from no row, and it carries no dependency weight.

```text
Grading hypothesis (declared): the site algebra M_2(C) carries the parity grading Ad(s3)
(even = span{E00, E11}, odd = span{E01, E10}); distinct sites compose by the graded
product; a state is readable only through its parity-even content.
```

It mirrors a candidate clause recorded elsewhere as a science-level decision awaiting its owner, plain-text pointer with no grade and no weight:
`MATTER_GRADED_COMPOSITION_AXIOM_UPDATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md`, "no grade, no weight". Theorem 1 is unconditional: it is a statement about intertwiners of
two explicit finite-dimensional representations. Theorems 2 and 3 are conditional on the displayed hypothesis, which is what gives the words "readable" and "parity-even" their
force; read without it, they are statements about the commutant of `s3` and about hopping matrix units, which is what the runner actually computes.

## Imports and authority

Imported scientific authority: none load-bearing. Finite-group intertwiner counting, the Jordan-Wigner transformation, and plane-wave diagonalization of a ring hop are standard
methodology; every object is redeclared here and every statement is recomputed by the primary runner. No observational value, no fitted number, and no framework premise enters
any proof. Non-load-bearing context pointers, plain file names with no grade and no dependency weight:

- `RECORD_FAITHFUL_CUBIC_NEIGHBOR_RESPONSE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md`, which classifies the same equivariant maps and adds a conditional corollary: if
  the rank-one record possibilities are the nontrivial spectral projectors of the realized `F(c)`, then `b != 0`. Theorem 1 re-derives that classification in this note's own
  words; Theorem 2 computes what the declared grading does to that corollary.
- `MATTER_GRADED_COMPOSITION_AXIOM_UPDATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md`, whose clause the declared hypothesis mirrors.
- `STAGGERED_DIRAC_SUBSTEP1_STATISTICS_GL_F_CONDITIONAL_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-06-10.md` and
  `STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`, named in the Corollary as the interface where site-dependent sign structure is handled. Nothing about
  either is used in any proof here.

This note re-declares everything it uses and cites none of their grades.

## Obligation graph

The proof is acyclic. Each node after `P0` is checked by the correspondingly lettered runner group.

1. `P0` (declared here): the Pauli matrices used as `Gamma_mu`, the grading `Ad(s3)`, the six directed unit vectors and their indexing, the generators `Rz` and `Rx`, the
   seven-site star with its matrix units, the Jordan-Wigner modes of the three-site line, the two rings, and the `3x3x3` block.
2. `P1` (`A`): the rotation group and its directed-neighbor permutation representation, the two-dimensional space of equivariant responses, and the projector parity.
3. `P2` (`B`): even faithfulness forcing `b = 0`, and the rank-one content of the surviving scalar point.
4. `P3` (`C`): the Jordan-Wigner restriction, the equivariant hopping classification and its dimension, the ring symbols, and the block commutators.

The strongest supported scope is precisely `P0`--`P3`.

## Definitions

Write `1` for the `2 x 2` identity, `s1, s2, s3` for the Pauli matrices, `E00, E01, E10, E11` for the matrix units of `M_2(C)`, and `n = E11`. Set `Gamma_mu = s_mu`, so
`{Gamma_mu, Gamma_nu} = 2 delta_{mu nu} 1` and `Herm(2) = R 1 (+) R^3 Gamma`. The **parity grading** of the site algebra is `Ad(s3)`, whose `+1` eigenspace is `span{E00, E11}`
and whose `-1` eigenspace is `span{E01, E10}`; an operator is **parity-even** when it commutes with `s3`. The six **directed unit vectors** are
`+e_1, -e_1, +e_2, -e_2, +e_3, -e_3`, indexed `d = 0..5` in that order, and the **neighbor sensitivities** are the six real numbers `c_d`. The **proper cubic rotations** are
the closure of

```text
Rz = [[0,-1,0],[1,0,0],[0,0,1]],   Rx = [[1,0,0],[0,0,-1],[0,1,0]],
```

and `Pi_R` is the `6 x 6` permutation matrix of the induced action on directed unit vectors, `(Pi_R c)_d = c_{R^{-1}(d)}`. A real-linear `L : R^6 -> Herm(2)`, written
`L(c) = alpha(c) 1 + beta(c).Gamma` with `alpha` a real `1 x 6` and `beta` a real `3 x 6` matrix, is **equivariant** when `alpha Pi_R = alpha` and `beta Pi_R = R beta` for
every `R`. The **direction matrix** `D` is the real `3 x 6` matrix whose `d`-th column is the `d`-th directed unit vector, so `beta = D` is the map
`c -> sum_mu (c_{+mu} - c_{-mu}) e_mu`.

The **seven-site star** is `{0} u {+-e_mu}`, the center indexed `0` and the neighbor `d` indexed `1+d`, with matrix units `E_{i,j}` of `M_7(C)` and the twelve **hopping units**
`E_{0,d}, E_{d,0}` (writing `E_{0,d}` for `E_{0,1+d}`). Their real span intersected with `Herm(7)` is twelve-dimensional and consists of the
`V(z) = sum_d (z_d E_{0,d} + conj(z_d) E_{d,0})` for `z in C^6`. A rotation acts on the star by fixing the center and permuting the neighbors by `Pi_R`, giving the `7 x 7`
permutation matrix `U_R`, and `M : R^6 -> Herm(7)` valued in that span is **equivariant** when `M(Pi_R c) = U_R M(c) U_R^T`. The **inversion** `S` is the `6 x 6` permutation
`d -> -d` and `J` is the all-ones `6 x 6` matrix. The two displayed channels are

```text
H_A(c) = sum_d c_d (E_{0,d} + E_{d,0}),      H_T(c) = i sum_d c_d (E_{0,d} - E_{d,0}).
```

**Jordan-Wigner** on the three-site line `{-e_1, 0, +e_1}`, indexed `0, 1, 2` with the center at `1`, sets `c_0 = a (x) 1 (x) 1`, `c_1 = s3 (x) a (x) 1`,
`c_2 = s3 (x) s3 (x) a` with `a = E01`, the vacuum being `|000>` and the **one-particle subspace** the span of the `c_j^dag |000>`. The **`L`-ring hops** are
`D_ring = i sum_j (E_{j,j+1} - E_{j+1,j})` and `A_ring = sum_j (E_{j,j+1} + E_{j+1,j})`, indices modulo `L`. The **`3x3x3` block** has sites `x in {0,1,2}^3`, index
`9x_1 + 3x_2 + x_3`, and open-boundary first differences `D_mu = i sum_x (E_{x, x+e_mu} - E_{x+e_mu, x})` over pairs in the block.

## Theorem 1 — the classification, recomputed

**Conclusion.** (1) The closure of `Rz` and `Rx` has `24` elements, each an integer matrix of determinant `+1` with `R R^T = 1`; each permutes the six directed unit vectors;
the `24` matrices `Pi_R` are pairwise distinct, closed under multiplication, and `R -> Pi_R` is an injective homomorphism onto a permutation group of order `24`. (2) The
equivariant real-linear maps `L : R^6 -> Herm(2)`, a homogeneous linear system in `24` real unknowns, form a solution space of real dimension exactly `2`, equal to the span of
`alpha = (1,1,1,1,1,1), beta = 0` and `alpha = 0, beta = D`; both displayed maps are equivariant for all `24` rotations, since `(1,...,1) Pi_R = (1,...,1)` and `D Pi_R = R D`,
so every equivariant response is

```text
F(c) = a [sum_d c_d] 1 + b sum_mu (c_{+mu} - c_{-mu}) Gamma_mu.
```

(3) For `F = m 1 + t (n_hat . Gamma)` with `t != 0` and `n_hat` a unit vector, the projectors `P_pm = (1 pm n_hat.Gamma)/2` satisfy
`P_pm = (F - lambda_mp 1)/(lambda_pm - lambda_mp)` with `lambda_pm = m pm t` and `F = lambda_+ P_+ + lambda_- P_-`, so each is a polynomial in `F` and `F` is a combination of
them; and `[P_pm, s3] = pm i(n_2 s1 - n_1 s2)`, which vanishes exactly when `n_1 = n_2 = 0`. Hence the spectral projectors of `F(c)` are parity-even exactly when the vector
part `b (c_{+mu} - c_{-mu})_mu` is parallel to `e_3`, or is zero, in which case `F(c)` is a multiple of `1` and its single spectral projector is `1`. (4) At the witness
`c = e_{+1}` the projectors are `(1 pm s1)/2`, rank one, summing to `1`, resolving `F = a 1 + b s1`, and failing to commute with `s3`; at the witness `c = e_{+3}` they are
`E00` and `E11`, rank one, and commuting with `s3`.

**Proof.** Item 1 closes the two generators under left multiplication, checks determinant, orthogonality and integrality entrywise, verifies that the induced map on the six
directed unit vectors is a bijection, and verifies closure and the homomorphism property on all `24 x 24` pairs. Item 2 assembles `alpha Pi_R - alpha = 0` and
`beta Pi_R - R beta = 0` for the two generators, which generate the group, and takes the null space of the coefficient matrix: the dimension is `2`, and the stacked rank of
that basis together with the two displayed vectors is again `2`, so the two spans coincide. Item 3 is four exact `2 x 2` identities, including `(n_hat.Gamma)^2 = (n.n) 1`,
checked with `n_1, n_2, n_3, m, t` symbolic. Item 4 evaluates.

## Theorem 2 — the corollary under the declared hypothesis

**Conclusion.** Under the declared hypothesis, call the response **even-faithful** when for every admissible `c` the rank-one record possibilities are the nontrivial spectral
projectors of `F(c)` and are parity-even. Then: (1) even faithfulness at `c = e_{+1}` and at `c = e_{+2}` requires `b (c_{+1} - c_{-1}) = 0` and `b (c_{+2} - c_{-2}) = 0`, that
is `[F(c), s3] = 0` at those two inputs, and each of those two linear conditions has the unique solution `b = 0`; so even faithfulness together with cubic equivariance forces
the scalar response `F(c) = a [sum_d c_d] 1`. (2) At the scalar point `(a, b) = (-1, 0)` with the star input `c_d = u_d - u_0`, the sum `sum_d c_d` equals `sum_d u_d - 6 u_0`,
the seven-point graph Laplacian at the center, and `F = -(sum_d c_d) 1`. That operator commutes with `s3` and with every even element `x(1-n) + y n`, has a single eigenvalue of
multiplicity `2`, and is a multiple of `1`: its spectral decomposition has the one projector `1`, of rank `2`. On the even sector, at one site, spectral faithfulness has no
rank-one content.

**Proof.** Item 1 solves `[F(c), s3] = 0` for `b` at the two witnesses; sympy returns the single solution `b = 0` in each case, and the same solve for symbolic `c` returns a
single solution as well. Substituting `b = 0` into the general equivariant form of Theorem 1 item 2 gives `a [sum_d c_d] 1` identically. The contrapositive reading is Theorem 1
item 4: with `b != 0` the projectors at `c = e_{+1}` are `(1 pm s1)/2`, rank one and not parity-even, so an even-faithful response with `b != 0` does not exist. Item 2 expands
`sum_d (u_d - u_0)` symbolically in the seven star values, compares with the Laplacian expression, and evaluates the commutators and the eigenvalue multiplicities exactly.

**Reading, not theorem.** The parent's conditional corollary and this one run in opposite directions from the same classification: rank-one spectral faithfulness forces
`b != 0`; requiring those same possibilities to be readable forces `b = 0`. The two are consistent, imposing different conditions; what changes is which condition the grading
makes available. This observes two computations and derives neither.

## Theorem 3 — relocation to the hopping channels

**Conclusion.** (1) On the Jordan-Wigner three-site line the canonical anticommutation relations hold exactly on `C^8`, and the hopping bilinears `c_1^dag c_0` and
`c_1^dag c_2` commute with the total parity `s3 (x) s3 (x) s3` and with the number operator, preserve the one-particle subspace, and restrict there to the matrix units
`E_{1,0}` and `E_{1,2}` exactly, with no residual Jordan-Wigner sign. (2) The equivariant real-linear maps `M : R^6 -> Herm(7)` valued in the twelve-dimensional hopping span, a
homogeneous system in `72` real unknowns, form a solution space of real dimension exactly `6`, **not** `2`. Writing `M(c) = V(Z c)` with `Z = X + i Y` and `X, Y` real `6 x 6`,
equivariance is exactly `Z Pi_R = Pi_R Z`; the real commutant of the directed-neighbor permutation representation is `span{1, S, J}` of dimension `3`, and the solution space is
the span of the six maps `c -> H_A(K c)` and `c -> H_T(K c)` for `K in {1, S, J}`. (3) `H_A` and `H_T` are Hermitian and equivariant for all `24` rotations, and both lie in
that space, being the members `K = 1` of the two families. (4) Edge reversal `E_{0,d} <-> E_{d,0}` is transposition, and `H_A(c)^T = H_A(c)` while `H_T(c)^T = -H_T(c)`
identically in `c`; since the identity holds for arbitrary input, the six-dimensional space splits as `3 + 3` into a transposition-even and a transposition-odd half. Under the
input inversion `S` alone, with the site labels held fixed, neither channel is even nor odd on all of `R^6`: `H_A(Sc) != H_A(c)` and `H_T(Sc) != -H_T(c)` as maps. What is true
is the restricted statement: `H_A` is even under `S` on `S`-symmetric inputs and `H_T` is odd under `S` on `S`-antisymmetric inputs. (5) On the directed input
`c = e_{+1} - e_{-1}`,

```text
H_T(c) = i(E_{0,+1} - E_{+1,0} - E_{0,-1} + E_{-1,0}),   (H_T psi)_0 = i(psi_{+1} - psi_{-1}),
```

the centered first-order difference along direction `1`, carried with no internal Clifford factor; the symmetric channel gives `(H_A psi)_0 = psi_{+1} - psi_{-1}` at the same
input. On the `L = 3` and `L = 4` rings the directed hop `D_ring` has eigenvalue multiset `{2 sin(2 pi m / L)}` and the symmetric hop `A_ring` has `{2 cos(2 pi m / L)}`; on
`L = 4` the plane wave `psi_j = i^{m j}` is an exact eigenvector with eigenvalues `-2 sin(pi m / 2)` and `2 cos(pi m / 2)`. (6) On the `3x3x3` block the three operators
`D_1, D_2, D_3` are Hermitian and commute pairwise, their pairwise anticommutators are nonzero, and `D_1^2 + D_2^2 + D_3^2` is not a multiple of `1`: its diagonal takes the
four values `3, 4, 5, 6`, the coordination numbers of the open block, with trace `108`. No Clifford relation arises from the hopping channels alone.

**Proof.** Item 1 builds the three Jordan-Wigner modes, checks all anticommutator pairs of each kind on `C^8`, computes the two bilinears and their commutators, and expands
each bilinear on each one-particle basis vector in that basis, verifying that the remainder vanishes and that the resulting `3 x 3` matrix is the named unit. Item 2 imposes
`M(Pi_R c) = U_R M(c) U_R^T` entrywise at the six basis inputs for the two generators, splits each entry into real and imaginary parts, and takes the null space of the
coefficient matrix in the `72` unknowns: the dimension is `6`. Separately `X Pi_R = Pi_R X` is solved in `36` unknowns, giving dimension `3` with basis `1, S, J`; the stacked
rank of the six explicit maps is `6` and adjoining the computed null-space basis leaves it at `6`, so the two spans coincide. Item 3 checks Hermiticity for symbolic `c` and
equivariance for each of the `24` rotations. Item 4 is two symbolic transposition identities, two explicit non-identities, and two restricted identities. Item 5 evaluates `H_T`
and `H_A` on the directed input against a symbolic wavefunction, matches the exact eigenvalues of the two `3 x 3` and two `4 x 4` ring matrices as multisets against the closed
forms, and verifies the `L = 4` plane waves. Item 6 builds the three `27 x 27` operators and checks Hermiticity, the commutators, the anticommutators, and the diagonal and
trace of the sum of squares.

## Corollary — what this changes

Under the declared hypothesis, and on the surfaces proved above:

1. The parent's conditional corollary inverts at one site. Where `RECORD_FAITHFUL_CUBIC_NEIGHBOR_RESPONSE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md` (plain-text
   pointer, no grade, no weight) concludes `b != 0` from rank-one spectral faithfulness, requiring those possibilities to be readable gives `b = 0` (Theorem 2 item 1).
2. The scalar branch the parent wanted to exclude is what survives, and it is inert as a record carrier: it is a multiple of `1`, so at one site the even sector has no rank-one
   spectral content for faithfulness to constrain (Theorem 2 item 2).
3. The first-order directed response relocates to the hopping channel of the graded product. The `sin k` structure the parent carried on `Gamma_mu` at one site is here carried
   between sites with no internal Clifford factor, and the three directions enter as three scalar `sin k_mu` terms unless site-dependent phases are supplied (Theorem 3 item 5).
   The relocation is not tight: the equivariant hopping space has real dimension `6`, not `2` (Theorem 3 item 2), so `H_T` is one member of a three-dimensional
   transposition-odd family rather than a unique directed channel, and nothing here selects among them.
4. A Clifford structure on the cube does not follow from the hopping channels: the three directional first differences commute (Theorem 3 item 6). Any such structure requires
   additional site-dependent sign structure, named below as an interface.

## What does not move

- No dynamics are selected. The channels of Theorem 3 are a classification of equivariant maps, not a choice of Hamiltonian; no rate, coupling, action, or absolute unit
  appears.
- No phases are supplied. The site-dependent sign structure a Clifford relation would need is named as an interface.
- No parameter values move. `a` and `b` of Theorem 1, the six coefficients of Theorem 3 item 2, and the star values `u_d` stay free throughout.
- No axiom text is amended, extended, reworded, or reinterpreted, and the grading hypothesis is declared here rather than consumed from a row.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.

## Interfaces named for other lanes, not moved here

These interfaces are named so that a later note can consume them; nothing here moves them.

- Lanes needing a Clifford relation on the cubic lattice: by Theorem 3 item 6 the hopping channels supply commuting operators, so the sign structure has to come from elsewhere.
  The statistics side of that interface is named in `STAGGERED_DIRAC_SUBSTEP1_STATISTICS_GL_F_CONDITIONAL_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-06-10.md` and the staggered
  phase structure itself in `STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md` (plain-text pointers, no grade, no weight).
- Lanes consuming a one-site vector response on `Gamma_mu`: by Theorem 2 item 1 they receive `b = 0` under the declared hypothesis, and must either name odd content as readable
  or take the response at more than one site.
- Lanes needing a first-order directed operator: by Theorem 3 item 5 the directed hopping channel supplies one with ring symbol `2 sin k` per direction. Which member of the
  three-dimensional transposition-odd family is meant is left to the consuming lane.

## Remaining live routes

1. More than one site for the response itself: Theorems 1 and 2 are one-site statements, and the two-site equivariant response is a separate computation not attempted here.
2. A derivation of the grading hypothesis, rather than its declaration, from the axioms and the approved primitives. This note proves nothing about whether such a derivation
   exists.
3. A selection principle inside the six-dimensional hopping space of Theorem 3 item 2. Equivariance alone leaves six parameters; what narrows them is not addressed here.
4. Site-dependent phase structure and whether it restores a Clifford relation on the cube. Theorem 3 item 6 shows the phase-free hopping channels do not.

## Executable claim block

The canonical machine-bound restatement of the three theorem conclusions.

```text
declared_grading: Ad(s3) on M_2(C), even = span{E00,E11}, odd = span{E01,E10}
clifford_convention: Gamma_mu = s_mu, {Gamma_mu, Gamma_nu} = 2 delta 1
proper_cubic_rotations_and_permutation_group_order: 24 and 24
one_site_equivariant_unknowns_and_solution_dimension: 24 and 2
one_site_equivariant_basis: c -> [sum_d c_d] 1 and c -> sum_mu (c_{+mu} - c_{-mu}) Gamma_mu
projector_parity_condition: [P_pm, s3] = pm i(n_2 s1 - n_1 s2), zero iff n_1 = n_2 = 0
witness_plus_1_projectors_and_parity: (1 pm s1)/2 and not parity-even
witness_plus_3_projectors_and_parity: E00, E11 and parity-even
even_faithfulness_solution_for_b: 0
surviving_response: F(c) = a [sum_d c_d] 1
scalar_point_and_laplacian: (a,b) = (-1,0), sum_d (u_d - u_0) = sum_d u_d - 6 u_0
scalar_point_distinct_eigenvalues_and_spectral_projector_rank: 1 and 2
jordan_wigner_dimension_and_restricted_bilinears: 8, E_{1,0} and E_{1,2}
hopping_span_dimension_and_equivariant_unknowns: 12 and 72
hopping_equivariant_solution_dimension: 6
directed_neighbor_commutant_and_basis: 3, span{1, S, J}
hopping_solution_basis: H_A(K c) and H_T(K c) for K in {1, S, J}
transposition_parity_of_channels: H_A even, H_T odd
directed_first_difference: (H_T psi)_0 = i(psi_{+1} - psi_{-1})
ring_symbols_directed_and_symmetric: 2 sin(2 pi m / L) and 2 cos(2 pi m / L), L = 3 and 4
block_sites_and_commutators: 27 and [D_mu, D_nu] = 0
block_square_sum_diagonal_and_trace: 3, 4, 5, 6 and 108
clifford_relation_from_hopping_channels: none
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=14 FAIL=0
```

## Proof boundary

Every statement is proved on one site, the seven-site star, the three-site Jordan-Wigner line, the `L = 3` and `L = 4` rings, and the `3x3x3` block, in complex dimensions `2`,
`7`, `8`, `3`, `4` and `27`, in the single-particle sector throughout except the Jordan-Wigner check of Theorem 3 item 1, a full `8 x 8` computation. Nothing is claimed about
many-particle sectors, about infinite lattices, about the improper cubic rotations, or about responses at more than one site. The grading hypothesis is declared, not derived,
and Theorems 2 and 3 are conditional on it. Theorem 3 item 2 reports the dimension the computation returns, `6`: this note was framed against an expected dimension of `2`, and
that expectation is wrong, `H_A` and `H_T` spanning a two-dimensional subspace of a six-dimensional solution space, the extra four dimensions coming from `S` and `J` acting in
either channel. The ring statement concerns the two named ring lengths and the closed forms matched against their exact spectra, not a general-`L` theorem. No axiom is amended,
no status is set, and no registry entry is created.

## Review record

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", the grading hypothesis is displayed verbatim in "Declared hypothesis"
and used nowhere implicitly, and all four context notes named in "Imports and authority" are plain-text pointers carrying no grade and no weight. Hard landing conditions are a
fresh exact runner and cache pair closing at `PASS=14 FAIL=0` with runtime under one second and stdout under `5500` characters, a current zero-dependency citation-manifest
entry, and passing repository pipeline, strict-lint, and changed-evidence gates; independent audit remains a separate lane.
