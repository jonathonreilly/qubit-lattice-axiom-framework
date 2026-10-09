---
claim_id: directed_stabilizer_six_parameter_chsh_maximum_bounded_theorem_note_2026-10-09
claim_type: bounded_theorem
claim_scope: "Conditional on one pair being a density on C^2 tensor C^2 whose real Pauli coefficients lie in the declared directed pattern: local Bloch numbers p and q, longitudinal correlation v, transverse correlation u, and twist t, with r^2=u^2+t^2. The operator is positive semidefinite exactly when |p+q|<=1+v and (p-q)^2+4 r^2<=(1-v)^2. For unit Pauli vectors the CHSH square equals 8 r^2 when r^2>=v^2 and equals 4(r^2+v^2) when r^2<=v^2. On the positive set that square is at most 8, with equality if and only if p=q=0, v=-1, and u^2+t^2=1. Signed coordinate-axis settings also have square at most 8. They attain 8 at the four circle points where |u|=|t|=1/sqrt(2), and at the singlet (u,t,v)=(-1,0,-1) their magnitude is at most 2. The axioms do not supply the density and do not select a point of the circle. No positive point has square above 8."
upstream_dependencies:
  - minimal_axioms
runner: scripts/directed_stabilizer_six_parameter_chsh_maximum_2026_10_09.py
---

# The directed six-parameter density has CHSH square at most 8

**Date:** 2026-10-09

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/directed_stabilizer_six_parameter_chsh_maximum_2026_10_09.py`](../scripts/directed_stabilizer_six_parameter_chsh_maximum_2026_10_09.py)

**Pinned cache:**
[`logs/runner-cache/directed_stabilizer_six_parameter_chsh_maximum_2026_10_09.txt`](../logs/runner-cache/directed_stabilizer_six_parameter_chsh_maximum_2026_10_09.txt)

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Pauli arithmetic, a positive-semidefinite criterion, and an elementary CHSH square on one declared coefficient pattern."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "It does not derive the dynamics clause, the trace rule, the menus or how settings are chosen."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "The formation site, probability, and rate are still unsupplied. Do not invent a hazard law, and do not treat a point of the equality circle as selected."
conditional_surface_status: "two-qubit density whose Pauli coefficients lie in the declared directed pattern"
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## What is conditional

The axioms used from
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
are the cubic lattice, the one-site algebra `M_2(C)`, one fixed
nearest-neighbor rule covariant under proper cubic rotations, and the record
rule that a readout is determined by record content. That memo says the
distribution does not supply the formation site, probability, or rate.

This note does **not** identify that distribution with a density. It takes
the following representation as a hypothesis and keeps it in every theorem.
A pair law is a density operator on `C^2 ⊗ C^2`, written
`(1/4) Σ c_ab σ_a ⊗ σ_b` with `σ_0 = I` and every `c_ab` real. The pattern
below is the coefficient pattern fixed by the directed stabilizer in
[the parent bond note](PROPER_CUBIC_TWO_QUBIT_BOND_INVARIANTS_BOUNDED_THEOREM_NOTE_2026-10-09.md).
This note does not recompute that nullspace. Its square theorems are proved
for the pattern itself. The sentence that every directed-invariant density
has this pattern is the parent's Theorem 1, carried in this same pull
request, and is not used as a step inside Theorems 1–5 here.

## Imports

- Lattice, qubit algebra, and proper cubic rotations, from the minimal-axiom
  memo cited above. Role: name the bond and the quarter turn about `e_z`.
  They do not provide the numerical coefficients.
- The directed basis named in the parent bond note. Role: say where the
  pattern came from. Provenance: that note's Theorem 1, on this branch, not
  on `origin/main`. Open: the axioms still do not force the pattern.
- No registered primitive is an input. `scale_reference_primitive`,
  `kinetic_isotropy_primitive`, and `realized_state_primitive` are not used.
- No literature value and no target square are inputs. The square `8` is
  the number computed below. A formal square `32` on a non-positive operator
  is rejected by the positivity test.

## Definitions

The declared pattern has `c_00 = 1`, `c_30 = q`, `c_03 = p`, `c_33 = v`,
`c_11 = c_22 = u`, `c_21 = t`, `c_12 = -t`, and every other coefficient
zero. Write `r^2 = u^2 + t^2`. The correlation matrix of the traceless
Pauli pairs is

```text
T = [[ u, -t, 0],
     [ t,  u, 0],
     [ 0,  0, v]].
```

The quarter turn about the lattice axis `e_z` is the matrix `R_z` from the
parent note. It fixes `e_z` and has order `4`.

An elementary CHSH comparison uses four unit vectors in `R^3` and the four
correlators of `a·σ` with `b·σ`. A signed-axis comparison uses only the six
vectors `±e_x, ±e_y, ±e_z`. These are two different comparisons.

## Obligation graph

The target sentence is Theorem 4: on the positive pattern, the elementary
CHSH square is at most `8`, with equality exactly on the circle
`p = q = 0`, `v = -1`, `u^2 + t^2 = 1`.

- Theorem 1, the Gram matrix of `T`, is proved here.
- Theorem 2, positivity, is proved here from the Pauli expansion.
- Theorem 3, the square formula, is proved here from Theorem 1.
- Theorem 4 applies Theorems 2 and 3 and does not drop either hypothesis.
- Theorem 5, the signed-axis square, is proved here by a separate
  enumeration. It is not an input to Theorem 4.
- The parent's nullspace theorem is not a lemma of Theorems 1–5.

Degenerate cases covered: `r^2 = v^2`, `r^2 = 0`, `v = ±1`, and `p` or `q`
nonzero. Not covered: POVMs, a readout that is not a Pauli unit vector, a
pair law that is not this density, and any window larger than one bond.

The strongest missing lemma is a derivation, from the four axioms, that the
nearest-neighbor distribution is a density of this pattern, together with
the formation site, probability, and rate. Selecting one point of the
equality circle is part of that gap. The dynamics clause remains a supplied
pointer, not a consequence.

## Theorem 1 — the Gram matrix

**Conclusion.** `T^T T` is diagonal, with entries `r^2`, `r^2`, and `v^2`.

**Proof.** The transverse block `u I + t J`, with
`J = [[0, -1], [1, 0]]`, satisfies `J^T = -J` and `J^2 = -I`. Therefore

```text
(u I + t J)^T (u I + t J) = (u I - t J)(u I + t J) = (u^2 + t^2) I.
```

The longitudinal row and column contribute `v^2` and no cross term. The
twist is absorbed into `r^2`. Replacing `-t` by `+t` produces the cross
term `2 u t` and is a different matrix.

## Theorem 2 — positivity

**Conclusion.** Let `H = 4ρ`. In the computational basis, `|00⟩` and `|11⟩`
are eigenvectors, with eigenvalues `1 + p + q + v` and `1 - p - q + v`. The
span of `|01⟩, |10⟩` is invariant, and that block has eigenvalues
`1 - v ± √((p - q)^2 + 4 r^2)`. Hence `ρ` is positive semidefinite exactly
when

```text
|p + q| ≤ 1 + v
and
(p - q)^2 + 4 r^2 ≤ (1 - v)^2.
```

**Proof.** Write `σ_x|0⟩ = |1⟩`, `σ_x|1⟩ = |0⟩`, `σ_y|0⟩ = i|1⟩`, and
`σ_y|1⟩ = -i|0⟩`. Then `XX` and `YY` exchange `|01⟩` and `|10⟩`, and

```text
(XX + YY)|00⟩ = 0,
(XX + YY)|11⟩ = 0,
(XX + YY)|01⟩ = 2|10⟩,
(XX + YY)|10⟩ = 2|01⟩.
```

The same expansion gives `(YX - XY)|01⟩ = 2i|10⟩` and
`(YX - XY)|10⟩ = -2i|01⟩`, with `|00⟩` and `|11⟩` again annihilated.
`Z⊗I`, `I⊗Z`, and `ZZ` are diagonal, with respective patterns
`(+1,+1,-1,-1)`, `(+1,-1,+1,-1)`, and `(+1,-1,-1,+1)`. Adding these
contributions produces the two eigenvalues above and the block

```text
[[1 + q - p - v,  2u - 2i t],
 [2u + 2i t,      1 - q + p - v]].
```

Its trace is `2(1 - v)` and its determinant is
`(1 - v)^2 - (p - q)^2 - 4 r^2`. The roots are real. Both are nonnegative
exactly when the trace and the determinant are nonnegative, that is
`v ≤ 1` and `(p - q)^2 + 4 r^2 ≤ (1 - v)^2`. The two computational
eigenvalues are nonnegative exactly when `|p + q| ≤ 1 + v`, which forces
`v ≥ -1`.

On the isotropic specialization `p = q = 0`, `t = 0`, and `u = v = w`, the
second inequality is `(1 - w)^2 - 4 w^2 ≥ 0`. That difference equals
`(1 - 3w)(1 + w)`, so the positive interval is `w ∈ [-1, 1/3]`.

## Theorem 3 — the elementary square

**Conclusion.** Every one-qubit Hermitian operator with eigenvalues `+1`
and `-1` is `a·σ` for a unit vector `a`. For such settings the maximum
CHSH square on this pattern is `8 r^2` when `r^2 ≥ v^2`, and
`4(r^2 + v^2)` when `r^2 ≤ v^2`. It does not depend on `p` or `q`.

**Proof.** Such an operator is traceless, and the traceless Hermitian
matrices on `C^2` are exactly the real Pauli span. Eigenvalues `±1` force
the coefficient vector to be a unit vector. The correlator of two traceless
observables is `a^T T b`; the local Bloch coefficients `p` and `q` multiply
a vanishing trace and do not appear.

For unit `b, b'`, the sums `c = b + b'` and `d = b - b'` are orthogonal and
satisfy `|c|^2 + |d|^2 = 4`. The CHSH expression is `a·T c + a'·T d`, whose
maximum over the two unit vectors `a, a'` is `|T c| + |T d|`. By Theorem 1
the eigenvalues of `T^T T` are `r^2`, `r^2`, and `v^2`. Let `λ1 ≥ λ2` be
the two largest, and let `α = |c|^2`, `β = |d|^2`. Aligning `c` and `d`
with those axes is possible: the repeated eigenvalue fills the `xy` plane,
and `v^2` belongs to the `z` axis. Cauchy's inequality in the form

```text
(√(λ1 α) + √(λ2 β))^2
  ≤ (λ1 + λ2)(α + β)
  = 4(λ1 + λ2)
```

has difference `(√(λ1 β) - √(λ2 α))^2`. Equality holds when
`α = 4 λ1 / (λ1 + λ2)` and `β = 4 λ2 / (λ1 + λ2)`, or at an endpoint if one
eigenvalue is zero. Therefore the maximum square is exactly `4(λ1 + λ2)`.

When `r^2 ≥ v^2`, this is `8 r^2`. The orthogonal vectors `c = (1,1,0)` and
`d = (1,-1,0)` have square length `2`, and `|T c|^2 = |T d|^2 = 2 r^2`, so
the square `8 r^2` is attained. When `r^2 ≤ v^2`, the split lengths above
attain `4(r^2 + v^2)`.

## Theorem 4 — the positive maximum

**Conclusion.** If `ρ` is positive semidefinite, the elementary CHSH square
is at most `8`. Equality holds if and only if `p = q = 0`, `v = -1`, and
`u^2 + t^2 = 1`. Every such point is positive, and `H` has eigenvalues
`0, 0, 0, 4`.

**Proof.** Theorem 2 forces `v ∈ [-1, 1]` and `4 r^2 ≤ (1 - v)^2`, so
`r^2 ≤ 1` and `v^2 ≤ 1`. Also

```text
8 - 2(1 - v)^2 = 2(3 - v)(1 + v),
```

which is nonnegative for `v ∈ [-1, 1]` and zero only at `v = -1`.

If `r^2 ≥ v^2`, Theorem 3 gives the square `8 r^2 ≤ 2(1 - v)^2 ≤ 8`.
Equality requires `r^2 = 1` and `v = -1`, hence `v^2 = r^2`, and the
positivity inequalities become `(p - q)^2 ≤ 0` and `|p + q| ≤ 0`. Thus
`p = q = 0`.

If `r^2 ≤ v^2`, the square is `4(r^2 + v^2) ≤ 8 v^2 ≤ 8`. Equality requires
`v^2 = 1` and `r^2 = v^2`. The case `v = 1` forces `r^2 ≤ 0`, so it cannot
have `r^2 = 1`. The case `v = -1` is the same point as above.

Conversely, at `p = q = 0`, `v = -1`, and `r^2 = 1`, both diagonal
eigenvalues are `0` and the block eigenvalues are `2 ± 2`, so `H` has
spectrum `0, 0, 0, 4`. Theorem 3 gives square `8`. The two undirected
corners `(u, v) = (±1, -1)` with `t = 0` lie on this circle. So do the pure
twists `(u, t) = (0, ±1)`. The circle is not a single state.

A non-positive Hermitian operator of trace one can have a formal square
above `8`. The point `r^2 = 4`, `v = -1` has formal square `32` and fails
Theorem 2. It is not a counterexample inside the positive set.

## Theorem 5 — signed coordinate axes

**Conclusion.** Restrict every setting to `±e_x, ±e_y, ±e_z`. On the
positive pattern the CHSH square is still at most `8`. It equals `8` at the
four points

```text
p = q = 0, v = -1, |u| = |t| = 1/√2,
```

all four sign combinations. At `(u, t, v) = (±1, 0, -1)` and at
`(0, ±1, -1)`, every such strategy has magnitude at most `2`.

**Proof.** There are `6^4 = 1296` strategy tuples. For each, the value is
`A u + B t + G v` with integer coefficients. The pairs
`(A^2 + B^2, G^2)` that occur are exactly

```text
(0, 0), (0, 4), (1, 1), (2, 0), (4, 0), (8, 0).
```

The identity `(A u + B t)^2 + (A t - B u)^2 = (A^2 + B^2) r^2` gives
`|A u + B t| ≤ √(K) r`, where `K = A^2 + B^2`. With Theorem 2,

```text
|A u + B t + G v| ≤ √(K) (1 - v) / 2 + |G| |v|.
```

The six pairs bound the square as follows.

- `K = 8`, `G = 0`: the upper square is `2(1 - v)^2 ≤ 8`, by the
  factorization in Theorem 4, with equality only at `v = -1` and `r^2 = 1`.
- `K = 4`, `G = 0`: the upper square is `(1 - v)^2 ≤ 4`.
- `K = 2`, `G = 0`: the upper square is `(1 - v)^2 / 2 ≤ 2`.
- `K = 1`, `G^2 = 1`: on `[-1, 0]` the upper value is `(1 - 3v) / 2`, and
  `4 - (1 - 3v) = 3(1 + v) ≥ 0`, so that value is at most `2`. On `[0, 1]`
  the upper value is `(1 + v) / 2 ≤ 1`. The square is at most `4`.
- `K = 0`, `G^2 = 4`: the square is at most `4 v^2 ≤ 4`.
- `K = 0`, `G = 0`: the value is `0`.

Thus no positive point has signed-axis square above `8`. Equality is
possible only for a strategy with `K = 8`, at `v = -1`, `r^2 = 1`, and
`p = q = 0`, and only when `(u, t)` is parallel to `(A, B)`. The strategies
include `(A, B) = (2, -2)`, realized by settings `(x, y)` against `(y, x)`.
Parallelism gives `u = -t` and `2 u^2 = 1`, so `u = ±1/√2` and
`t = ∓1/√2`. The other three sign patterns are the other three pairs
`(±2, ±2)`. At `u = 1/√2` and `t = -1/√2`, that strategy equals `2√2` and
its square equals `8`.

The same enumeration gives magnitude at most `2` at the four axial points
`t = 0, u = ±1` and `u = 0, t = ±1`, with `v = -1`. In particular the
singlet has elementary square `8` and signed-axis square at most `4`. The
equatorial vectors that attain square `8` there are not all coordinate
axes.

## What this does not do

- It does not derive a formation site, probability, rate, or clock.
- It does not show that the admissibility distribution is a two-qubit density.
- It does not select `p`, `q`, `u`, `t`, or `v`. Square `8` is attained on
  a circle, not forced at one point.
- It does not derive the dynamics clause. That clause remains a way to point
  at the singlet, which is one point of the circle.
- It does not recompute the parent's nullspace, and it does not claim a
  square for a coefficient outside this pattern.
- It does not evaluate POVMs or a readout whose value depends on the other
  wing.
- It does not say that signed-axis settings attain square `8` at the
  singlet. Theorem 5 says the opposite.
- It does not evaluate the sum rule, a window larger than one bond, or an
  infinite lattice.

## No-Go Discipline Gate

Scoped claim: no positive density of this pattern has elementary CHSH square
above `8`, and no signed-axis strategy has square above `8`. The equality
loci are Theorems 4 and 5. A claim that no representation of any kind can
have square `8` is not made. The in-domain attacks below are closed by
those theorems. This packet does not close an attack outside the stated
pattern.

N1. Five attacks on the scoped squares:

1. Let the local Bloch numbers `p` and `q` raise the correlator. A Hermitian
   with eigenvalues `±1` is traceless, so those numbers drop out of
   Theorem 3. `ATTEMPTED`.
2. Let the twist raise a singular value above `u^2 + t^2`. Theorem 1 puts
   the twist inside `r^2` and produces no larger eigenvalue. The symmetric
   sign choice is a different matrix and is not fixed by `R_z`.
   `ATTEMPTED`.
3. Let `λ1 + λ2` exceed `2` on a positive point. Theorem 2 caps `r^2` by
   `(1 - v)^2 / 4`, and Theorem 4 factors the resulting square. `ATTEMPTED`.
4. Let a signed-axis strategy exceed square `8`. Theorem 5 enumerates all
   `1296` tuples and bounds the six coefficient pairs. `ATTEMPTED`.
5. Let unequal lengths `|c|^2` and `|d|^2` exceed `4(λ1 + λ2)`. The
   difference in Theorem 3 is a square, so the split lengths are optimal.
   `ATTEMPTED`.

N2. The density representation and the coefficient pattern are one
hypothesis, not two walls: the pattern is the object inside the density.
The signed-axis menu is a second comparison, proved separately, not a second
wall under Theorem 4. No independent-wall count is asserted.

N3. The proof text was checked against the hidden-condition list in the
discipline note. The density, the pattern, the unit-vector comparison, and
the axis menu are written as hypotheses. No phrase on that list is doing
the work of a missing hypothesis.

N4. The parent bond note does not witness this square. Its residual is the
full proper-cubic family and the undirected sub-pattern; it says explicitly
that the directed region was not computed. The product-class note of this
same date evaluates a different pair law and uses no density. The
dynamics-clause Bell note bounds a different kernel. None of those residuals
is the one bounded here. Dropping all three citations leaves Theorems 1–5
intact.

N5. "The square is at most 8" means the elementary comparison, and
separately the signed-axis comparison, for one bond of this pattern. It was
not tested for a larger neighborhood, for the sum rule, or for an infinite
lattice. The runner prints those five resolutions.

N6. This note does not say that a new axiom is required. The three
registered primitives named above are not walls. The search of `origin/main`
at `d9b869b97944676aaa759915462c529dc276a04c` found no evaluation of this
directed square and no convention that turns the pattern into the singlet.

N7. Steelman, outside this domain: drop the density and evaluate a
directed-invariant record law directly. The product-class menu already
misses square `8`, but it is not this pattern, so a different record law
could still differ. POVMs are also outside Theorems 3 and 5. Those escapes
do not make a positive point of this pattern exceed square `8`. The
unclosed obligation is the missing derivation of the density and of the
formation site, probability, and rate.

N8. The records-only magnitude-`2` bound has not been retired, and its
kernel is not this density. The parent's cut down to `w = -1` has not been
reopened; this note uses the larger directed pattern that the parent left
uncomputed. No searched retirement mechanism changes the positivity
constraint inside the pattern.

## Review record

This note does not narrow or replace the parent bond note or the
product-class square note. The parent's two undirected corners sit on the
circle of Theorem 4. The parent's statement that the directed region was
uncomputed is the part this note fills, under the same density hypothesis.

Outstanding at landing, as hard landing conditions: the density hypothesis
stays open; formation site, probability, and rate stay unsupplied; no point
of the circle is selected; independent audit has not reviewed this note.
No helper runner is declared, and no packet-helper registry edit is made.

## Runner

`scripts/directed_stabilizer_six_parameter_chsh_maximum_2026_10_09.py`
rebuilds `H` from Pauli Kronecker products, multiplies `T^T T` from the
matrix definition, checks the block determinant against Theorem 2, attains
the equatorial and split-length squares, enumerates the `1296` axis
strategies, and evaluates the diagonal axis point in `Q(√2)`. A symmetric
twist, an unequal transverse pair, a formal square `32`, and a nonzero
Bloch number on the circle are negative controls. The author re-ran the
three load-bearing mutations below on scratch copies; each exited nonzero.
Those copies were not kept.

- Flip the transverse sign in `T`: the Gram check fails.
- Return `8 r^2` for every branch: the split-length comparison fails.
- Change the axis image of `e_y`: the six-pair set fails.
