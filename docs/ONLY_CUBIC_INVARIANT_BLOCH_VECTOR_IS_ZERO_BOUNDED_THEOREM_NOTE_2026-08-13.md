---
claim_id: only_cubic_invariant_bloch_vector_is_zero_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "For the determinant-+1 signed-permutation group G acting on Q^3, the generated representation is irreducible and has fixed space {0}. The Q-linear Pauli-coordinate map carries this result to the rational-Pauli traceless Hermitian space. On the rational Bloch body x^2+y^2+z^2 <= 1, the unique G-fixed density is I/2."
upstream_dependencies: []
runner: scripts/only_cubic_invariant_bloch_vector_is_zero_2026_08_13.py
---

# The only cubic-invariant Bloch vector is 0

**Date:** 2026-08-13

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/only_cubic_invariant_bloch_vector_is_zero_2026_08_13.py`](../scripts/only_cubic_invariant_bloch_vector_is_zero_2026_08_13.py)

**Parents:** none. Every premise used below is declared in this note.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-group and Q-linear Pauli-coordinate theorem with a precisely declared rational Bloch body."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained algebraic theorem."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

Let `G` be the group generated over `Q^3` by the two matrices `R_z` and `R_x`
displayed below; prove that `G` is the `24`-element determinant-`+1`
signed-permutation group, that its representation on `Q^3` is irreducible
with `Fix_G(Q^3) = {0}`, that the transported `Q`-linear Pauli action has
fixed traceless Hermitian subspace `{0}`, and that on
`B_Q = {(x,y,z) in Q^3 : x^2+y^2+z^2 <= 1}` the matrix
`rho(r) = (I+r·sigma)/2` is a density matrix whose unique `G`-fixed member is
`I/2`.

## Imports and authority

Imported scientific authority: none. The group, its action, the Pauli map,
and the rational Bloch body are definitions internal to this theorem. Its
complete target is the finite algebraic statement in the previous section.
No observational value or framework premise enters the proof.

## Obligation graph

The proof is acyclic and closes through the following nodes.

1. `P0` (proved here): declare `R_z`, `R_x`, and the generated group `G`.
2. `P1` (proved here): enumerate `G` and identify its `24` determinant-`+1`
   signed-permutation matrices.
3. `P2` (proved here): prove irreducibility of the `G`-representation on
   `Q^3`.
4. `P3` (proved here): solve the generator fixed equations and obtain
   `Fix_G(Q^3) = {0}`.
5. `P4` (proved here): define the rational-Pauli Hermitian space and prove the
   Pauli map is a `Q`-linear isomorphism intertwining the declared actions.
6. `P5` (proved here): characterize `B_Q` exactly by Hermiticity, trace one,
   and positive semidefiniteness of `rho(r)`.
7. `P6` (proved here): combine `P3`--`P5` to identify the unique fixed density.

The primary runner checks each node with exact rational arithmetic. The
strongest supported scope is precisely `P0`--`P6`.

## Definitions

The generating right-hand quarter turns are

```text
R_z = [[ 0, -1, 0],
       [ 1,  0, 0],
       [ 0,  0, 1]],
R_x = [[ 1,  0,  0],
       [ 0,  0, -1],
       [ 0,  1,  0]].
```

Let `G = <R_z,R_x>`. For `r = (x,y,z) in Q^3`, define

```text
r·sigma = [[ z,      x - i y ],
           [ x + i y,   -z    ]],
rho(r)  = (I + r·sigma)/2.
```

The rational-Pauli Hermitian space is the `Q`-span of
`{sigma_x,sigma_y,sigma_z}` inside the Hermitian `2 x 2` matrices. The action
on that space is declared by transport: `R·(r·sigma) = (Rr)·sigma`.

## Theorem 1 — the generated representation is irreducible

**Conclusion.** `G` has order `24`, consists exactly of the determinant-`+1`
signed-permutation matrices, and acts irreducibly on `Q^3`.

**Proof.** Both generators are determinant-`+1` signed permutations. Closure
under multiplication gives `24` distinct matrices. Independent enumeration
of all signed permutations gives `3! 2^3 / 2 = 24` determinant-`+1` matrices,
so the two sets agree.

For a direct irreducibility proof, take any nonzero `r`. Its `G`-orbit spans
all of `Q^3`: an axis vector is rotated onto all three axes; a vector with two
nonzero coordinates and third coordinate zero spans its coordinate plane
together with its `R_z` image because the relevant determinant is
`x^2+y^2`, and a quarter turn supplies the third direction; for three nonzero
coordinates, `R_z r-r` is a nonzero vector in a coordinate plane and reduces
to the preceding cases. Coordinate permutations cover the placements used in
this argument. Hence every nonzero invariant subspace contains a spanning
orbit and equals `Q^3`.

As exact cross-checks, the character inner product is
`|G|^-1 sum_g trace(g)^2 = 1`, and the commutant of `R_z,R_x` is `Q I`.

## Theorem 2 — the fixed space is zero

**Conclusion.** `Fix_G(Q^3) = {0}`.

**Proof.** If `R_z r=r`, then `(-y,x,z)=(x,y,z)`, so `x=-y` and `y=x`,
which gives `x=y=0`. With `r=(0,0,z)`, the equation `R_x r=r` reads
`(0,-z,0)=(0,0,z)`, so `z=0`. The two generator equations therefore have
rank `3`. Equivalently, the Reynolds average `|G|^-1 sum_g g` is the zero
matrix.

## Theorem 3 — the Pauli-coordinate fixed space is zero

**Conclusion.** The `G`-fixed subspace of the rational-Pauli traceless
Hermitian space is `{0}`.

**Proof.** The displayed Pauli map sends the standard basis of `Q^3` to
`sigma_x,sigma_y,sigma_z`; it is therefore a `Q`-linear isomorphism onto the
declared three-dimensional `Q`-space. The transported action intertwines by
definition. It can also be realized independently by conjugation with the
quarter-turn lifts `(I-i sigma_z)/sqrt(2)` and
`(I-i sigma_x)/sqrt(2)`. Theorem 2 now transfers the fixed-space result.

## Theorem 4 — the rational Bloch density body

**Conclusion.** `rho(r)` is a density matrix exactly when
`r in B_Q`, and the unique `G`-fixed density in this body is `rho(0)=I/2`.

**Proof.** For rational `r`, `rho(r)` is Hermitian and has trace `1`. Its
determinant is

```text
det rho(r) = (1 - x^2 - y^2 - z^2)/4.
```

A Hermitian `2 x 2` matrix with trace `1` is positive semidefinite exactly
when its determinant is nonnegative. Thus `rho(r)` is a density exactly on
`B_Q`. The group preserves `x^2+y^2+z^2`, so it acts on this body. Theorem 2
then makes `r=0` the unique fixed coordinate, giving `rho(0)=I/2`.

For exact boundary, interior, and exterior controls, `(1,0,0)` belongs to
`B_Q` and gives a determinant-zero rank-one density, `(3/5,0,0)` has
determinant `4/25` and lies in the interior of `B_Q`, and `(6/5,0,0)` has
determinant `-11/100` and lies in the affine Hermitian trace-one space outside
`B_Q`.

## Executable claim block

The following block is the canonical machine-bound restatement of the four
theorem conclusions.

```text
group_order: 24
representation_dimension: 3
irreducible_over: Q
fixed_space_dimension: 0
commutant_dimension: 1
pauli_map_scalar_field: Q
density_domain: x^2 + y^2 + z^2 <= 1
unique_fixed_density: I/2
```

## Proof boundary

The theorem proposed here is the self-contained finite-group representation
theorem and its rational Bloch-body corollary. Covered cases include `r=0`,
the full-rank interior `0 < ||r||^2 < 1`, the singular positive-semidefinite
unit sphere `||r||^2 = 1`, and affine Hermitian trace-one exterior controls
with `||r||^2 > 1`. Vectors outside `Q^3` and every lattice or physical
covariance interpretation are outside this target. No lemma in `P0`--`P6`
remains open; any physical application would be a separate target with its
own premises.

## Review record

This revision narrows the earlier draft to `P0`--`P6`. It withdraws rather
than refutes the minimal-axiom import, physical covariance corollary,
six-component neighborhood tuple, and negative-claim framing. The preserved
scope ends at the self-contained finite-group, Pauli-coordinate, and rational
Bloch-body theorem. Hard landing conditions are a fresh exact-boundary
runner/cache pair, a current zero-dependency citation-manifest entry, and
passing repository pipeline, strict-lint, and changed-evidence gates;
independent audit remains a separate lane.
