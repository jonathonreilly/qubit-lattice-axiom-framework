# Casimir-Equivariant Tensor-Action Class No-Go on `Sym^2(R^4)`

**Claim type:** positive_theorem (no-go on a named class)
**Date:** 2026-05-17
**Branch:** `physics-loop/universal-gr-tensor-action-blocker-block06-2026-05-17`
**Status authority:** source-note proposal only; audit verdict and effective
status are set by the independent audit lane.
**Role:** universal GR / tensor-action blocker / named-obstruction sharpening
**Primary runner:** [`scripts/frontier_universal_gr_tensor_action_casimir_equivariant_class_nogo.py`](../scripts/frontier_universal_gr_tensor_action_casimir_equivariant_class_nogo.py)
**Cached runner output:** [`logs/runner-cache/frontier_universal_gr_tensor_action_casimir_equivariant_class_nogo.txt`](../logs/runner-cache/frontier_universal_gr_tensor_action_casimir_equivariant_class_nogo.txt)
(`runner_sha256 = e1aab7cdacb75a29b512c2d0c73b8ce6cf362b6a9eedf9e542d1ce849e6a6fdb`; `exit_code = 0`; `status = ok`; `PASS=28 FAIL=0 TOTAL=28`).

## Purpose

The cluster sibling
[`UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md`](UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md)
records, as an inventory-style blocker label, that the direct universal GR
route is incomplete because no retained-grade tensor-localization primitive
identifies the scalar-generator Hessian with Einstein/Regge dynamics. That
statement is currently `audited_conditional` (load-bearing step class E)
because it is an inventory claim without cited authorities or
machine-checkable evidence.

The present note converts the blocker-label statement, on a single
well-defined linear-projector tensor-action class, into a sharp **named
obstruction theorem**. The class is the linear span of bilinear forms built
from the canonical SO(3)-equivariant Casimir block projectors of the
retained sibling [`UNIVERSAL_GR_CASIMIR_BLOCK_LOCALIZATION_NOTE.md`](UNIVERSAL_GR_CASIMIR_BLOCK_LOCALIZATION_NOTE.md).

The result is a class-(A) no-go: no element of this class can canonically
section the SO(3) orbit on the universal `E ⊕ T1` complement. This does
not close the full universal-GR route, but it sharpens the blocker label
into a structural theorem about a specific, exhaustively characterized
action class.

## Claim scope (proposed)

Let `V := Sym^2(R^4)` be the real 10-dimensional space of symmetric `4 x 4`
real matrices with Frobenius inner product `<a, b>_F := sum_{i,j} a_{ij} b_{ij}`.
Let `SO(3)` act on `V` by `rho(R) h := R^T h R` with `R := diag(1, R_3)`,
`R_3 ∈ SO(3)` (the spatial-block action used in the retained sibling
notes).

Let `(P_lapse, P_shift, P_trace, P_shear)` be the four canonical
SO(3)-equivariant Casimir block projectors of
[`UNIVERSAL_GR_CASIMIR_BLOCK_LOCALIZATION_NOTE.md`](UNIVERSAL_GR_CASIMIR_BLOCK_LOCALIZATION_NOTE.md):

- `P_lapse := diag(1, 0, 0, 0, 0, 0, 0, 0, 0, 0)` (rank 1, j=0, trivial irrep)
- `P_shift` (rank 3, j=1)
- `P_trace := diag(0, 0, 0, 0, 1, 0, 0, 0, 0, 0)` (rank 1, j=0, trivial irrep)
- `P_shear` (rank 5, j=2)

in the canonical orthonormal polarization basis `B` defined in that
retained note. The four projectors are mutually orthogonal, idempotent,
complete (`P_lapse + P_shift + P_trace + P_shear = I_10`), and
SO(3)-equivariant (`[P_a, G_x] = [P_a, G_y] = [P_a, G_z] = 0`); these
properties are imported as already-retained.

**Class CB(V) — Casimir-equivariant bilinear forms.**
Define `Class CB(V)` to be the set of real bilinear functionals
`S: V × V → R` of the form

```
S(h, k) := a · <P_lapse h, P_lapse k>_F
         + c · <P_trace h, P_trace k>_F
         + e · ( <P_lapse h, P_trace k>_F + <P_trace h, P_lapse k>_F )
         + b · <P_shift h, P_shift k>_F
         + d · <P_shear h, P_shear k>_F
```

for real coefficients `(a, b, c, d, e) ∈ R^5`. Symmetry of `S` (`S(h, k)
= S(k, h)`) is built in by construction. The "shape" of the cross term
between `P_lapse` and `P_trace` (the only same-isotypic cross allowed by
Schur, since lapse and trace are both trivial irreps) is fixed by Schur's
lemma up to the single real coefficient `e`.

**Theorem.** With definitions as above:

1. **(T1) Schur classification.** Every SO(3)-equivariant symmetric
   bilinear functional on `V` that is `Sym^2(R^4)`-linear in each
   argument and is constructed as a linear combination of bilinear forms
   `<P_a h, P_b k>_F` with `a, b ∈ {lapse, shift, trace, shear}` lies in
   `Class CB(V)`. Equivalently, `Class CB(V)` is exhausted by the five
   real parameters `(a, b, c, d, e)`.

2. **(T2) Orbit-flatness.** For every `(a, b, c, d, e) ∈ R^5` and every
   `R ∈ SO(3)`:
   ```
   S_{a,b,c,d,e}(rho(R) h, rho(R) k) = S_{a,b,c,d,e}(h, k)
   ```
   for all `h, k ∈ V`. As a corollary, the quadratic functional
   `Q(h) := S(h, h)` satisfies `Q(rho(R) h) = Q(h)` for all `R ∈ SO(3)`.

3. **(T3) Section no-go (orbit-tangent gradient).** For every `(a, b, c,
   d, e) ∈ R^5` with either `b ≠ 0` or `d ≠ 0`, and every `h ∈ V`
   with nonzero `P_shift h` or `P_shear h`, the SO(3) orbit
   `O(h) := {rho(R) h : R ∈ SO(3)}` is a level set of `Q`. Equivalently,
   the Euler-Lagrange equations `delta Q / delta h = 0` are satisfied
   identically along `O(h)` — `Q` does not single out a preferred orbit
   representative on the `E ⊕ T1` complement.

4. **(T4) Exhaustiveness corollary.** Any candidate symmetric bilinear
   tensor action `S: V × V → R` obtained as a linear combination of the
   canonical Casimir block projectors of
   [`UNIVERSAL_GR_CASIMIR_BLOCK_LOCALIZATION_NOTE.md`](UNIVERSAL_GR_CASIMIR_BLOCK_LOCALIZATION_NOTE.md)
   lies in `Class CB(V)`. The no-go (T3) is therefore sharp on the
   entire class of such candidates.

**Interpretation.** The blocker recorded in
[`UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md`](UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md),
restricted to the natural linear-projector class built from the retained
Casimir decomposition, is now a structural theorem rather than an
inventory label. No `Class CB(V)` action can section the SO(3) gauge on
the complement. To escape the no-go, a candidate tensor action would have
to leave `Class CB(V)`, e.g. by:

- using a NONLINEAR functional of `h` (out of scope here);
- using projectors that are NOT Casimir-equivariant (would violate the
  retained `casimir_block_localization_note` provenance);
- using SO(3)-equivariant projectors with multiplicity > 1 in any non-trivial
  irrep (would violate the retained rank table `(1, 3, 1, 5)`);
- breaking the retained `Pi_A1` invariance (would violate the retained
  `A1_invariant_section_note` provenance);
- introducing a fresh external selector beyond `A_min` (forbidden in
  the present axiom budget).

The five-parameter exhaustion shows that no LINEAR rearrangement of the
retained block projectors can break the SO(3) gauge — the named obstruction
on this class is genuine.

## Scope and audit boundary

This note proves a representation-theoretic class no-go on the abstract
pair `(V, rho)`. It does **not** claim:

- closure of the universal-GR route as a whole;
- non-existence of any tensor action outside `Class CB(V)` (e.g.,
  nonlinear functionals, derivative-dependent functionals, functionals
  built from non-Casimir-equivariant projectors);
- a uniqueness or non-existence theorem for the missing primitive
  `Pi_curv` of
  [`UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md`](UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md)
  outside `Class CB(V)`;
- a derivation of the linearized Einstein-Hilbert action from
  `Class CB(V)` — the result is only that, if the linearized
  Einstein-Hilbert action lies in `Class CB(V)`, it inherits the
  orbit-flat no-go and cannot canonically section the complement;
- a closure of any other sibling blocker (`polarization_frame_bundle_blocker`,
  `curvature_localization_blocker`, `invariant_frame_obstruction`).

The class definition is intentionally narrow: linear combinations of
bilinear forms `<P_a h, P_b k>_F` over the four canonical Casimir
projectors. This is the natural "linear-projector tensor-action class"
on the retained decomposition. Wider classes (derivative operators,
non-projector tensors, nonlinear functionals) are out of scope.

## Bounded admissions

Every load-bearing step below reduces to elementary linear algebra and
representation theory plus the already-retained Casimir decomposition.

- **(BA-1) Real linear algebra on `Sym^2(R^4)`.** Frobenius inner
  product `<a, b>_F`, bilinearity, additivity, and standard matrix
  arithmetic over `R`.
- **(BA-2) Orthogonality of `SO(3)`.** For `R_3 ∈ SO(3)`, `R_3^T R_3
  = I_3` and `det(R_3) = 1`. Hence `R := diag(1, R_3)` satisfies `R^T R
  = I_4`.
- **(BA-3) Retained Casimir block projectors.** The four canonical
  projectors `(P_lapse, P_shift, P_trace, P_shear)` of the retained
  `UNIVERSAL_GR_CASIMIR_BLOCK_LOCALIZATION_NOTE.md` are imported with
  the following exact properties (T6-T7 of that note, retained as
  bounded textbook output):
  - mutually orthogonal: `P_a P_b = 0` for `a ≠ b`;
  - idempotent: `P_a^2 = P_a`;
  - complete: `P_lapse + P_shift + P_trace + P_shear = I_10`;
  - SO(3)-equivariant: `[P_a, G_x] = [P_a, G_y] = [P_a, G_z] = 0` for
    each `a ∈ {lapse, shift, trace, shear}`;
  - irrep ranks `(1, 3, 1, 5)` with `(P_lapse, P_trace)` carrying two
    copies of the trivial irrep and `(P_shift, P_shear)` carrying the
    `j=1` and `j=2` irreps respectively.
- **(BA-4) Schur's lemma in real-orthogonal form.** For two finite-dim
  real SO(3)-modules `U, W` and any real-linear SO(3)-equivariant map
  `phi: U → W`, the space `Hom_{SO(3)}(U, W)` of such maps is:
  - 1-dimensional over R if `U` and `W` are isomorphic as real
    SO(3)-modules;
  - 0-dimensional (only `phi = 0`) if `U` and `W` are non-isomorphic
    real SO(3)-modules.
  (Real-orthogonal Schur: for real irreps of compact `SO(3)`, the
  endomorphism algebra is R for each irrep type, so the multiplicity
  space is described over R.)
- **(BA-5) Orbit-tangent gradient is a corollary of (BA-2)–(BA-4).** If
  a smooth real functional `Q: V → R` is invariant under a Lie group
  action (`Q(rho(R) h) = Q(h)` for all `R`), then the gradient
  `nabla Q(h) ∈ V` is orthogonal to every orbit-tangent vector at `h`.
  Conversely, if every orbit `O(h)` is a level set of `Q`, then `nabla
  Q(h)` is orbit-normal at every `h`, and the EL equations `nabla Q(h)
  = 0` are either solved identically along an orbit or solved nowhere
  on it; in either case the EL system cannot single out a preferred
  orbit representative.

(BA-1) through (BA-5) are the only bounded admissions. (BA-3) is the
specific bridge to the retained `casimir_block_localization` note;
(BA-4) is the only representation-theoretic input beyond elementary
linear algebra.

## Proof-walk

### Proof of (T1) — Schur classification

Let `S: V × V → R` be a real-bilinear functional constructed as
`S(h, k) = sum_{a, b ∈ {lapse, shift, trace, shear}} M_{ab} <P_a h, P_b k>_F`
for some real coefficients `M_{ab}` (16 in total).

By (BA-3), `rho(R) P_a = P_a rho(R)` for each block `a` and each `R ∈
SO(3)`. By (BA-1), the Frobenius product satisfies
`<rho(R) x, rho(R) y>_F = tr((rho(R) x)^T (rho(R) y)) = tr(R^T x^T R R^T y R)
= tr(x^T y) = <x, y>_F`
using `R^T R = R R^T = I_4` from (BA-2) and the cyclic property of
trace.

So under `(h, k) ↦ (rho(R) h, rho(R) k)`:
```
S(rho(R) h, rho(R) k) = sum_{a, b} M_{ab} <P_a rho(R) h, P_b rho(R) k>_F
                      = sum_{a, b} M_{ab} <rho(R) P_a h, rho(R) P_b k>_F   [by P_a commutes with rho(R)]
                      = sum_{a, b} M_{ab} <P_a h, P_b k>_F                  [by <rho R x, rho R y> = <x, y>]
                      = S(h, k).
```
So every such `S` is automatically SO(3)-equivariant by virtue of
(BA-3). This shows the inclusion: `{linear combinations of <P_a h, P_b
k>_F} ⊂ {SO(3)-equivariant bilinear functionals on V}`.

The reverse: by (BA-4) (Schur) applied to the retained block
decomposition `V = range(P_lapse) ⊕ range(P_shift) ⊕ range(P_trace) ⊕
range(P_shear)`, the space `Hom_{SO(3)}(V, V)` of SO(3)-equivariant
endomorphisms decomposes into a direct sum of the multiplicity-block
endomorphism algebras:
- the trivial-isotypic block (multiplicity 2: lapse + trace) contributes
  `Mat_{2,2}(R)`, the 2×2 real matrices — 4 real dimensions;
- the `j=1` block (multiplicity 1: shift) contributes `R` — 1 real
  dimension;
- the `j=2` block (multiplicity 1: shear) contributes `R` — 1 real
  dimension.
Total: `4 + 1 + 1 = 6` real dimensions for `Hom_{SO(3)}(V, V)`.

A general element of `Hom_{SO(3)}(V, V)` therefore has the form
```
T = m_LL P_lapse + m_LT P_lapse_to_trace + m_TL P_trace_to_lapse + m_TT P_trace
  + m_S  · J_shift + m_R · J_shear
```
where `P_lapse_to_trace` is a fixed isomorphism between `range(P_lapse)`
and `range(P_trace)` (both 1D trivial reps), `P_trace_to_lapse` its
transpose, and `J_shift`, `J_shear` are the identity on their respective
blocks. (Specifically, in basis `B`, `P_lapse_to_trace` is the rank-1
linear map sending `e_0` to `e_4` and annihilating the rest; its
transpose `P_trace_to_lapse` sends `e_4` to `e_0` and annihilates the
rest.)

The space of SO(3)-equivariant bilinear forms `S(h, k) = <h, T k>_F`
inherits this 6-dimensional structure. **Symmetry** in `(h, k)` then
restricts to the symmetric part:
```
T_symm = (T + T^T) / 2
       = m_LL P_lapse + (m_LT + m_TL)/2 · (P_lapse_to_trace + P_trace_to_lapse) + m_TT P_trace
       + m_S · J_shift + m_R · J_shear
```
which has 5 real parameters: `m_LL`, `m_TT`, `e := (m_LT + m_TL)/2`, `m_S`,
`m_R`. Identifying `a := m_LL`, `c := m_TT`, `b := m_S`, `d := m_R`, and
`e` as above, we recover the explicit `Class CB(V)` parameterization
in the claim. The bilinear form `<P_lapse h, P_trace k>_F` is non-zero
only on the trivial-isotypic 2-block and is precisely the Schur cross
term; `<P_trace h, P_lapse k>_F` is its transpose. Their symmetric sum
`<P_lapse h, P_trace k>_F + <P_trace h, P_lapse k>_F` gives the `e`
term in the claim. Setting the antisymmetric combination to zero is the
symmetrization condition. ∎ (T1)

### Proof of (T2) — Orbit-flatness

Given (T1)'s display of `S = S_{a,b,c,d,e}`, the computation in the
inclusion direction of (T1) already shows:
```
S(rho(R) h, rho(R) k) = S(h, k)
```
for every `R ∈ SO(3)` and every `h, k`. Set `k = h` to get the
quadratic-form version. ∎ (T2)

### Proof of (T3) — Section no-go

By (T2), every quadratic functional `Q(h) := S_{a,b,c,d,e}(h, h)` is
SO(3)-orbit-invariant: `Q(rho(R) h) = Q(h)` for every `R ∈ SO(3)`. So
every orbit `O(h) = {rho(R) h : R ∈ SO(3)}` is a level set of `Q`.

By (BA-5), the gradient `nabla Q: V → V` (defined by `Q(h + eps w) =
Q(h) + 2 eps <nabla Q(h), w>_F + O(eps^2)`) is orthogonal to every
orbit-tangent vector at `h`. For an orbit `O(h)` of positive dimension
(which is the case whenever the stabilizer of `h` in `SO(3)` has
dimension less than 3, equivalently whenever `P_shift h` or `P_shear
h` is non-zero), the gradient `nabla Q(h)` cannot point along the
orbit. So `nabla Q(h)` is orbit-NORMAL at every point of `O(h)`, and
the EL system `nabla Q(h) = 0` is solved either at no point of `O(h)`
or at every point (since `Q` is constant on the orbit, critical points
must come in full orbits).

Conclusion: no `Q ∈ Class CB(V)` with `b ≠ 0` or `d ≠ 0` can single
out a preferred orbit representative on the `E ⊕ T1` complement. The
EL system is **degenerate along the SO(3) gauge** — exactly the
section-no-go formulated in the theorem statement. ∎ (T3)

### Proof of (T4) — Exhaustiveness corollary

Any "linear-projector tensor-action candidate" built as a real linear
combination of bilinear forms `<P_a h, P_b k>_F` over the four canonical
Casimir block projectors of the retained `casimir_block_localization`
note is, by definition, an element of `Class CB(V)`. (T1) shows that
symmetry restricts this to a 5-parameter family. (T3) shows every
nonzero-complement element of this family is section-no-go. So the
no-go is sharp on the entire linear-projector class on the retained
decomposition. ∎ (T4)

## Cached runner output

The runner is fully reproducible and self-contained (imports `sympy`
only; constructs every Casimir projector from scratch following the
retained sibling note). Cached output is at
[`logs/runner-cache/frontier_universal_gr_tensor_action_casimir_equivariant_class_nogo.txt`](../logs/runner-cache/frontier_universal_gr_tensor_action_casimir_equivariant_class_nogo.txt).

Key cached identities:
- Schur classification: `dim Hom_SO(3)(V, V) = 6 (4 + 1 + 1)` (4 trivial-isotypic block + 1 j=1 + 1 j=2);
- Symmetric class dimension: `dim Class CB(V) = 5 (3 + 1 + 1)` (3 trivial-isotypic symmetric + 1 j=1 + 1 j=2);
- Orbit-flatness symbolic: `S(rho(R_a(theta))h, rho(R_a(theta))k) - S(h, k) ≡ 0` for each single-axis rotation `R_a, a ∈ {x, y, z}` (single-axis rotations generate `SO(3)`) and symbolic `h, k`;
- Section no-go: `<nabla Q(h), tangent_a(h)>_F = 0` for the three orbit-tangent vectors `tangent_a(h) := G_a h` (a ∈ {x, y, z}), for symbolic `h`, every `Q ∈ Class CB(V)`;
- Class exhaustion: comparison of dimensions matches the (T1) prediction;
- Anisotropic-control negative test: replacing `<·, ·>_F` with a non-isotropic weight breaks orbit-flatness, confirming (BA-2) is load-bearing.

## Verification

Re-run from a clean working tree with:

```bash
PYTHONPATH=scripts python3 scripts/frontier_universal_gr_tensor_action_casimir_equivariant_class_nogo.py
```

Expected (matches cache):

```
PASS=N FAIL=0 TOTAL=N
```

All checks are class-(A) exact algebraic identities over `Q[sqrt 2,
sqrt 3, sqrt 6]` (the field of the retained Casimir basis) plus
symbolic SO(3) single-axis rotation identities reduced by
`sympy.trigsimp` and `sympy.simplify`. No random sampling, no numeric
tolerance, no fitted constants. The exhaustiveness rank computation
uses standard sympy `Matrix.rank()` over the polynomial coefficient
ring on monomials `h_i k_j`.

## Provenance and load-bearing inputs

The following retained authorities are load-bearing for the present
theorem (graph edges that anchor the algebraic inputs):

- [`UNIVERSAL_GR_CASIMIR_BLOCK_LOCALIZATION_NOTE.md`](UNIVERSAL_GR_CASIMIR_BLOCK_LOCALIZATION_NOTE.md)
  supplies the four canonical SO(3)-equivariant Casimir block projectors
  `(P_lapse, P_shift, P_trace, P_shear)` with ranks `(1, 3, 1, 5)`,
  mutual orthogonality, completeness, idempotence, and SO(3)-equivariance.
  Load-bearing for (BA-3).
- [`UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT_NARROW_THEOREM_NOTE_2026-05-10.md`](UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT_NARROW_THEOREM_NOTE_2026-05-10.md)
  supplies the SO(3)-orbit-flat invariance of the 2-block decomposition
  with isotropic spatial weight. The present note REFINES that result
  from a 2-block (Pi_A1 vs Pi_perp) statement to a 4-block (lapse,
  shift, trace, shear) statement and extends it from a one-parameter
  energy `E_{alpha, beta}` to a five-parameter `Class CB(V)`.
  Load-bearing for (T2)/(T3) as a partial precursor; the present
  theorem strictly subsumes its statement.

The following sibling notes are cited for **context** only (graph
bookkeeping, no load-bearing dependency for the present theorem):

- [`UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md`](UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md)
  is the blocker-label sibling that the present note SHARPENS into a
  named obstruction (within `Class CB(V)`). The present note does not
  promote that sibling; the sibling's `audited_conditional` status is
  set by the independent audit lane.
- [`UNIVERSAL_GR_A1_INVARIANT_SECTION_NOTE.md`](UNIVERSAL_GR_A1_INVARIANT_SECTION_NOTE.md)
  records the rank-2 `Pi_A1 = P_lapse + P_trace` invariant section.
- [`UNIVERSAL_GR_BLOCK_NORMALIZATION_NOTE.md`](UNIVERSAL_GR_BLOCK_NORMALIZATION_NOTE.md)
  records the block-orbit-canonical-but-not-section-canonical structure.
- [`UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md`](UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md)
  records the frame-bundle obstruction from a complementary angle.

## Forbidden-imports check

- No PDG observed values consumed.
- No literature numerical comparators consumed.
- No fitted selectors consumed.
- No admitted unit conventions are load-bearing.
- No same-surface family arguments.
- No new axioms introduced — the theorem is on abstract `Sym^2(R^4)`
  with the generic spatial-block SO(3) action; framework axioms appear
  only as cross-reference anchors.
- No new repo vocabulary — `Class CB(V)`, "Casimir-equivariant
  bilinear form" are local definitions internal to this note;
  "Schur's lemma" is standard representation-theory terminology.
- Runner imports: `sympy` only. No `numpy`, no random sampling, no
  external data; only `pathlib.Path` for reading the source note in
  the scope-discipline check section.

## What this theorem does NOT close

- The full universal-GR route on `PL S^3 × R` — the present theorem is
  a NO-GO on a single named action class, not a closure of the route.
- Action classes outside `Class CB(V)`: nonlinear functionals,
  derivative-dependent functionals (e.g. those involving spatial
  gradients of `h`), functionals built from non-Casimir-equivariant
  projectors. These remain logically open; the no-go does not extend
  to them.
- Whether the linearized Einstein-Hilbert action on `PL S^3 × R`
  belongs to `Class CB(V)` is a separate question. If it does, the
  no-go (T3) shows it inherits the section-no-go, sharpening the
  Einstein/Regge identification gap into a concrete operator-class
  obstruction. The present note does not claim this membership.
- No promotion of any sibling note. Each sibling's audit status is set
  independently.
- No claim that `Class CB(V)` is the "physically correct" action class
  — its definition is a structural choice, namely the linear-projector
  class on the retained Casimir decomposition.

## Honest status

The present theorem converts the inventory-style blocker label of
[`UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md`](UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md),
on the named class `Class CB(V)`, into a structural class-(A)
no-go theorem. The blocker on this class is now a sharp named
obstruction. The wider universal-GR route remains open beyond
`Class CB(V)`; no claim about that wider scope is made here.
