---
claim_id: proper_cubic_group_is_24_and_contains_no_boost_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "For the standard linear point action on the six nearest-neighbor displacements of Z^3, the orientation-preserving stabilizer G is exactly the 24 signed-permutation matrices with determinant +1. It is a group, every element preserves the Euclidean form, and exactly 8 of its elements also preserve diag(1,1,-1). Under the explicitly displayed 3+1 comparison iota(R)=diag(1,R), every element fixes the time axis and hence none is a nontrivial time-space-mixing boost. The exact rational boost with 1+1 block [[5/3,4/3],[4/3,5/3]] supplies a correctly typed contrast. The 3+1 comparison is not adopted as framework structure, and no Lorentz-closure claim is made."
upstream_dependencies:
  - minimal_axioms
runner: scripts/proper_cubic_group_is_24_and_contains_no_boost_2026_08_13.py
---

# The Proper Cubic Point Group Has Order 24; Its Canonical Spacetime Embedding Has No Nontrivial Boost

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact finite linear algebra on the nearest-neighbor displacement
set of the supplied cubic lattice, followed by one explicitly displayed 3+1
comparison. No spacetime metric or time direction is added to the framework.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/proper_cubic_group_is_24_and_contains_no_boost_2026_08_13.py`](../scripts/proper_cubic_group_is_24_and_contains_no_boost_2026_08_13.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  the cubic lattice `Z^3`, nearest-neighbor adjacency, translations, and
  proper cubic rotations about each site.

Everything after that quoted input is defined and proved here. In particular,
this note does not import a boost matrix, a Lorentz metric, or a continuous
symmetry theorem from another science note.

## Result Up Front

Fix a site `a in Z^3` and write

```text
N = {+e1, -e1, +e2, -e2, +e3, -e3}
```

for its six nearest-neighbor displacement vectors. A linear point symmetry
acts on sites by

```text
x |-> a + R(x-a).
```

Define

```text
G = {R in GL(3,Z) : R N = N and det(R)=+1}.
```

Then:

1. `R N=N` is equivalent to `R` being a signed-permutation matrix.
2. `G` is a group and has exactly `3! 2^2 = 24` elements.
3. Every `R in G` satisfies `R^T R=I_3`. The full group does not preserve
   `D=diag(1,1,-1)`: exactly 8 elements do and 16 do not.
4. In the displayed 3+1 comparison on columns `(t,x1,x2,x3)`, with
   `eta=diag(1,-1,-1,-1)`, put `iota(R)=diag(1,R)`. Every `iota(R)`
   preserves `eta` but has zero time-space mixing, so none is a
   **nontrivial boost** in the declared sense below.
5. The exact rational block
   `B_2=[[5/3,4/3],[4/3,5/3]]` really is Lorentzian:
   `B_2^T diag(1,-1) B_2=diag(1,-1)`, `det(B_2)=1`, and its positive
   time-time entry is `5/3`. Its 3+1 extension mixes time and space and is
   not in `iota(G)`.

The point group `G` is not the infinite affine symmetry group. Adding the
supplied translations gives the orientation-preserving space group
`Z^3 semidirect G`; the order-24 statement concerns the fixed-site point
stabilizer only.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact nearest-neighbor point-group characterization, finite group proof, metric census, and canonical-embedding boost separation are proved; adoption of spacetime structure and Lorentz closure remain outside the claim."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "separate the finite proper-cubic point action from a nontrivial time-space-mixing boost under one explicit comparison"
source_of_blocker_text: handoff
reachability_to_target: advances
next_trace_action: "Use this result only as a finite point-group/type-separation lemma; any dynamical Lorentz-restoration claim needs its own carrier and proof."
artifact_role: theorem
conditional_surface_status: "exact on the declared point action and displayed canonical 3+1 comparison"
hypothetical_axiom_status: "no axiom or primitive is edited or proposed"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects And Conventions

Matrices act on column vectors. A 3 by 3 **signed-permutation matrix** has
one nonzero entry in every row and column, with each nonzero entry in
`{+1,-1}`.

The phrase **proper cubic point group** in this note means the standard
orientation-preserving linear stabilizer of `N` at a fixed site:

```text
G = {R in GL(3,Z) : R N=N, det(R)=+1}.
```

For the displayed comparison only, set

```text
eta = diag(1,-1,-1,-1),       iota(R) = diag(1,R).
```

A **nontrivial boost** in this bounded note means a proper, time-oriented
Lorentz matrix `Lambda` satisfying

```text
Lambda^T eta Lambda = eta,    det(Lambda)=1,    Lambda_00 > 0,
```

with at least one nonzero time-space entry `Lambda_0i` or `Lambda_i0` for
`i=1,2,3`. This convention excludes the identity/zero-rapidity overlap and
is sufficient for the finite membership question. It does not claim that
every Lorentz transformation with mixing is a pure boost rather than a
boost-rotation composition.

## Theorem 1 — The Fixed-Site Linear Stabilizer Is Signed-Permutation

If `R N=N`, each column `R ej` is one of the six vectors `+/- ek`. Since
`R` is invertible, distinct columns cannot lie on the same coordinate axis.
Thus the three columns are signed, distinctly permuted standard-basis
vectors: `R` is a signed-permutation matrix.

Conversely, every signed-permutation matrix permutes `N`, has integer inverse
`R^T`, and therefore lies in `GL(3,Z)`. Imposing `det(R)=+1` selects exactly
the orientation-preserving point stabilizer. The affine map about an
arbitrary site `a` is `x |-> a+R(x-a)`; this is what “about each site” means
in the supplied Lattice sentence.

## Theorem 2 — `G` Is A Group Of Order 24

A signed-permutation matrix is uniquely specified by a permutation
`sigma in S_3` and three signs `s1,s2,s3`. Hence there are
`3! 2^3=48` such matrices and

```text
det(R) = sign(sigma) s1 s2 s3.
```

For every fixed permutation, exactly four sign triples give determinant
`+1`. Therefore `|G|=3! 2^2=24`.

The identity is in `G`. Products of signed-permutation matrices are
signed-permutation matrices, and determinants multiply, so `G` is closed.
For every `R in G`, the inverse is `R^T`, again a signed-permutation matrix
with determinant `+1`. Thus the counted set is a group, not merely a
24-element list. The runner checks identity, all `24^2` products, and all
24 transpose inverses exactly.

## Theorem 3 — Euclidean Preservation And The Indefinite Intersection

The columns of a signed-permutation matrix are an orthonormal Euclidean
basis, so for every `R in G`,

```text
R^T R = I_3.
```

This does **not** imply that each `R` fails to preserve every indefinite
form. For

```text
D = diag(1,1,-1),
```

the identity and the rotations that keep the distinguished third axis setwise
do preserve `D`. Exact enumeration gives

```text
|G intersect O(D)| = 8.
```

The other 16 do not preserve `D`. For example,

```text
Ry = [[ 0, 0, 1],
      [ 0, 1, 0],
      [-1, 0, 0]]
```

has determinant `+1` and lies in `G`, but

```text
Ry^T D Ry = diag(-1,1,1) != D.
```

The honest conclusion is that `G` is a subgroup of Euclidean `SO(3)`, while
the full `G` is not a subgroup of `O(2,1)` for this displayed `D`. The
8-element intersection is stated rather than erased.

## Theorem 4 — Canonical 3+1 Embeddings Fix Time

For every `R in G`, define

```text
iota(R) = [[1, 0],
           [0, R]].
```

Because `R^T R=I_3` and `det(R)=1`,

```text
iota(R)^T eta iota(R) = eta,    det(iota(R))=1.
```

Moreover `iota(R)` fixes the time basis vector and has zero time-space row
and column. It therefore fails the declared nontrivial-mixing predicate for
every one of the 24 elements. The matrices are spatial rotations inside the
displayed Lorentz group, not nontrivial boosts. The identity may be called a
zero-rapidity boost in another convention; that is why “nontrivial” and the
mixing predicate are part of this note's exact claim.

## Theorem 5 — A Correctly Typed Exact Boost Contrast

Let

```text
B2 = [[5/3, 4/3],
      [4/3, 5/3]],              eta2 = diag(1,-1).
```

Exact rational multiplication gives

```text
B2^T eta2 B2 = eta2,    det(B2)=25/9-16/9=1,    (B2)_00=5/3>0.
```

Its 3+1 extension on `(t,x1,x2,x3)` is

```text
B4 = [[5/3, 4/3, 0, 0],
      [4/3, 5/3, 0, 0],
      [  0,   0,  1, 0],
      [  0,   0,  0, 1]].
```

It preserves `eta`, is proper and time-oriented, and has nonzero time-space
entries. Thus it satisfies the declared nontrivial-boost predicate. It cannot
equal `iota(R)` for any `R in G`, since every `iota(R)` has zero time-space
entries. This is a type-correct contrast; no conclusion depends on rejecting
an arbitrary non-Lorentz matrix.

## No-Go Discipline Gate

The negative statement gated here is only:

> Under the displayed canonical embedding `iota(R)=diag(1,R)`, no element of
> the finite point group `G` is a nontrivial time-space-mixing boost.

It is not a no-go for Lorentz emergence, noncanonical embeddings, continuum
limits, or later dynamics.

### N1 — Alternative routes

| Route | Status | Attempt and disposition |
|---|---|---|
| fixed-time-axis block test | ATTEMPTED | Inspect the time row and column of all `iota(R)`; each is `(1,0,0,0)`, so the required mixing is absent. |
| finite-order/eigenvalue test | ATTEMPTED | Every `iota(R)` has finite order because `G` is finite, whereas a nonzero-rapidity pure boost has real reciprocal eigenvalues `exp(+chi),exp(-chi)` and infinite order. |
| Euclidean-versus-boost action test | ATTEMPTED | `iota(R)` fixes the unit time vector; a nontrivial boost sends it to a vector with nonzero spatial component. |
| exhaustive declared-predicate test | ATTEMPTED | The runner constructs all 24 embeddings, verifies their Lorentz identities, and finds zero with time-space mixing. |
| exact boost-witness intersection test | ATTEMPTED | The rational `B4` satisfies the boost predicate but cannot equal any `iota(R)` because its time-space block is nonzero. |
| 2+1 indefinite-intersection test | ATTEMPTED | Eight matrices preserve `D=diag(1,1,-1)`, but those preservers keep the unique negative axis setwise; the time-oriented subset has no mixing of that axis with the positive plane. |

These are distinct structural, spectral, vector-action, finite-census,
witness, and alternate-signature attacks. Each is closed by an exact proof
above and a corresponding runner gate; no prior negative result is used as
authority.

### N2 — Wall independence

There is no multi-wall impossibility claim. The fixed 3+1 carrier, its
signature, the canonical embedding, and the nontrivial-mixing predicate are
one declared comparison contract, not four independently claimed physical
walls. The earlier phrasing that separated a “fourth direction” from a
`(3,1)` form is collapsed here: a `(3,1)` form already specifies a
four-dimensional carrier.

### N3 — Hidden-wall scan

The load-bearing conditions are explicit: fixed site, column action,
nearest-neighbor set `N`, determinant orientation, 3+1 coordinate order,
metric signature, canonical embedding, time orientation, and nonzero mixing.
“Standard linear action” names the definition displayed in this note; it is
not an unspoken theorem. No framework time axis, spacetime metric, continuum
limit, dynamics, or Lorentz-restoration premise is used.

### N4 — Residual matching

No prior no-go, wall, or campaign is cited as a witness. The minimal-axiom
source supplies only the lattice sentence; it does not supply the matrix
classification or the boost exclusion. Those residuals are closed directly
here, so there is no borrowed residual to mismatch.

### N5 — Rhetoric audit

The runner and note resolve the following exact granularities:

```text
per_element: all 24 proper-cubic matrices and their canonical spacetime embeddings are checked exactly
per_site: the point action is proved at one arbitrary fixed lattice site and transported by the supplied translations
per_mode: every canonical embedding fixes the displayed time axis, while no momentum or dynamical mode is asserted
per_block: one exact rational boost block is Lorentzian and lies outside the zero-mixing embedded point group
lattice_wide: checked and not executed — no lattice-wide dynamics, continuum limit, or Lorentz restoration is claimed
```

The negative conclusion is per element and per canonical block. It is not
upgraded to a lattice-wide dynamical or continuum statement.

### N6 — Partial-closure paths

No new axiom is required for this finite type separation: making the
comparison convention explicit closes it. A later theory may choose a
different spacetime carrier, a noncanonical embedding, or emergent Lorentz
dynamics. Those are live construction paths, not forbidden escapes and not
premises of this theorem.

### N7 — Steelman

The strongest counterargument is to conjugate `iota(G)` by a Lorentz matrix.
The conjugated finite subgroup can have nonzero time-space entries in the
original coordinates, so the visual zero-block argument is not invariant
under changing the embedding. In addition, identity is a zero-rapidity boost
under a permissive convention, and a 2+1 comparison has an 8-element
indefinite-metric intersection. These points defeat any embedding-free claim.
They do not defeat the stated result, which fixes the canonical embedding,
excludes zero rapidity through the mixing predicate, and reports the 2+1
intersection explicitly. A noncanonical or embedding-free theorem remains
open.

### N8 — Cross-cycle echo

A targeted current-main search found similar discrete-versus-continuous
boundaries in `LORENTZ_BOOST_COVARIANCE_2D_THEOREM_NOTE.md`,
`LORENTZ_BOOST_COVARIANCE_3PLUS1D_THEOREM_NOTE.md`, and
`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`. They reinforce the need to distinguish
microscopic cubic symmetry from a continuum boost, but they are not imported
as proof here. No previously retired wall is being revived: this note closes
only a finite canonical-embedding membership question and leaves Lorentz
restoration open.

**Gate result:** the narrowly stated finite negative passes N1-N8. This is a
source-side scope check, not an audit verdict.

## What This Does Not Claim

- It does not identify the 24-element group with continuous `SO(3)`.
- It does not claim that `G` has empty intersection with every indefinite
  orthogonal group; the displayed 8-element intersection is explicit.
- It does not claim that identity is excluded from zero-rapidity terminology;
  it excludes only nontrivial time-space mixing.
- It does not adopt `eta`, a time axis, a 3+1 carrier, or a boost as framework
  structure.
- It does not claim that Lorentz symmetry cannot emerge or that Lorentz
  closure is impossible.
- It does not edit Lattice, Qubit, Admissibility, Record, or any primitive.
- It does not use observational, fitted, or literature values.

## Exact Target And Obligation Graph

| Obligation | Disposition |
|---|---|
| bind “about each site” to the fixed-site affine action | proved from the displayed action |
| characterize the linear stabilizer of six neighbors | proved in Theorem 1 |
| prove the determinant-positive subset is a group | identity, closure, and inverses proved in Theorem 2 |
| count the proper point group | proved `|G|=24` in Theorem 2 |
| preserve the Euclidean form | proved for all 24 in Theorem 3 |
| state the indefinite intersection honestly | exactly 8 preserve `D`; explicit nonpreserver given |
| define the common 3+1 action and boost predicate | declared before Theorem 4 |
| exclude all 24 canonical embeddings | proved by the zero-mixing block in Theorem 4 |
| supply a genuine boost contrast | exact rational Lorentz identity in Theorem 5 |
| protect the negative boundary | committed N1-N8 record above |

The runner recomputes every finite census and matrix identity. It does not
treat source-text presence as mathematical proof.
