---
claim_id: proper_cubic_group_is_24_and_contains_no_boost_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "The Lattice named symmetry on Z^3 is the 24-element group G of 3x3 monomial signed-permutation matrices with det=+1. Enumeration gives |G|=24. Every R in G satisfies R^T R = I_3 and preserves x1^2+x2^2+x3^2, hence is orthogonal for diag(1,1,1) and not for diag(1,1,-1). A 1+1 boost prototype L=[[2,1],[1,2]], and its 3D block embedding diag(L,1), is not a proper cubic matrix. Lattice and the kinetic-isotropy primitive name Euclidean cubic rotations and one Euclidean tick c_t=c_s; neither sentence names a boost. A Lorentzian boost would require a fourth direction plus a (3,1) form; those extras are displayed and not adopted. The note does not claim Lorentz closure is impossible, does not install a=1, and does not identify G with SO(3)."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
runner: scripts/proper_cubic_group_is_24_and_contains_no_boost_2026_08_13.py
---

# Proper Cubic Group Is 24 Matrices In SO(3); None Is A Boost

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact integer 3×3 named-symmetry algebra of the Lattice proper
cubic rotations. No Wick parameter, no fourth-direction form, and no
axiom edit.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/proper_cubic_group_is_24_and_contains_no_boost_2026_08_13.py`](../scripts/proper_cubic_group_is_24_and_contains_no_boost_2026_08_13.py)

Parents on `origin/main`:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — current axiom memo
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)

## Result Up Front

Lattice supplies a finite named symmetry: the proper cubic rotations of the
spatial lattice `Z^3`. That named object is a set `G` of exact integer 3×3
matrices. It is not a Lorentz boost, and it is not the continuous group
`SO(3)`.

Five exact statements locate the object.

1. There are `3! × 2^3 = 48` signed-permutation matrices. Exactly half have
   `det = +1`, so `|G| = 24`.
2. Every `R ∈ G` preserves the Euclidean form: `R^T R = I_3`, and
   `x ↦ R x` preserves `x_1^2 + x_2^2 + x_3^2`. In particular every `R` is
   orthogonal with respect to `diag(1,1,1)`, not `diag(1,1,-1)`.
3. A 1+1 boost prototype `L = [[2,1],[1,2]]` is not a 3×3 cubic matrix. Its
   block embedding `diag(L,1)` fails the monomial ±1 test.
4. The axiom memo names “standard translations, and proper cubic rotations
   about each site.” Kinetic isotropy supplies one Euclidean tick
   `c_t = c_s`, not a Lorentz theorem. Neither sentence names a boost.
5. The extra object for a Lorentzian boost is a fourth direction plus a
   `(3,1)` form. That extra is displayed below and is not adopted. This note
   does not claim Lorentz closure is impossible, does not install `a = 1`,
   and does not say that the cubic 24 is `SO(3)`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 24-element count, Euclidean orthogonality, and non-membership of the boost prototype are proved on declared integer 3x3 matrices. A fourth direction, a (3,1) form, Lorentz closure, and identification of G with SO(3) remain outside the claim."
trace_class: named_symmetry_localization
target_claim_id: proper_cubic_named_symmetry_is_24_euclidean_matrices
target_blocker_text: "name the Lattice cubic symmetry as a finite Euclidean rotation group and separate it from a Lorentz boost"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for |G|=24, Euclidean preservation, and non-membership of diag(L,1); Lorentzian extras remain displayed-only"
hypothetical_axiom_status: "no edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

A **signed-permutation matrix** of size 3 is a 3×3 integer matrix with
exactly one nonzero entry in each row and each column, and with every
nonzero entry in `{+1, −1}`.

A **proper cubic matrix** is a signed-permutation matrix with `det = +1`.
Write `G` for the set of all proper cubic matrices. Identity gates in the
runner call `proper_cubic_count()` and `is_proper_cubic(M)` on these objects.

The Euclidean spatial form is

```text
q_E(x) = x_1^2 + x_2^2 + x_3^2,
```

equivalently the matrix `diag(1,1,1)`. The Minkowski 2-form used only as a
rejector contrast is `η_2 = diag(1,−1)`. The 3×3 contrast form that `G` does
not preserve as its defining form is `diag(1,1,−1)`.

The 1+1 boost prototype is the integer matrix

```text
L = [[2, 1],
     [1, 2]].
```

Its 3-dimensional block embedding is

```text
diag(L, 1) = [[2, 1, 0],
              [1, 2, 0],
              [0, 0, 1]].
```

## Theorem 1 — `|G| = 24`

Every signed-permutation matrix is uniquely a pair `(σ, s)` with `σ ∈ S_3`
and `s ∈ {±1}^3`: the unique nonzero in column `j` sits in row `σ(j)` and
equals `s_j`. There are `3! = 6` permutations and `2^3 = 8` sign patterns,
hence `48` signed-permutation matrices.

The determinant of that matrix is

```text
det = sign(σ) · s_1 s_2 s_3 ∈ {±1}.
```

Flipping one sign sends the determinant to its opposite and is a bijection of
the 48-element set onto itself. Exactly half the signed-permutation matrices
therefore have `det = +1`, so

```text
|G| = 48 / 2 = 24.
```

The runner enumerates the 48 matrices over exact integers and counts the
`det = +1` subset by `proper_cubic_count()`. A predicate `|G| ≠ 24` fails.

## Theorem 2 — every `R ∈ G` preserves the Euclidean form

Let `R` be a proper cubic matrix. Each column is a signed standard-basis
vector, the three columns are pairwise orthogonal as integer vectors, and
each has Euclidean length squared `1`. Hence

```text
R^T R = I_3
```

as an exact integer matrix identity. For every integer (or real) column
`x = (x_1, x_2, x_3)`,

```text
q_E(R x) = (R x)^T (R x) = x^T (R^T R) x = x^T x = q_E(x).
```

The same matrices are therefore orthogonal for `diag(1,1,1)`. They are not
defined as the orthogonal group of `diag(1,1,−1)`: that form has signature
`(2,1)`, while every `R ∈ G` is a Euclidean rotation matrix (an element of
the compact group `SO(3)`, not a parametrization of that whole group).

## Theorem 3 — a boost prototype is not a proper cubic matrix

The prototype `L = [[2,1],[1,2]]` fails to be a proper cubic matrix for three
independent reasons, each already visible before any continuum Lorentz
discussion:

1. `L` is 2×2, not 3×3.
2. `L` is not monomial with entries in `{±1}` only: the entry `2` is not
   `±1`.
3. `L` does not preserve the Euclidean plane form. On `(1,0)` one has
   `L(1,0) = (2,1)` and `2^2 + 1^2 = 5 ≠ 1`.

Embed the same prototype as a 3×3 block `M = diag(L, 1)`. The `(1,2)` entry
is `1`, but the first row is `(2, 1, 0)` and therefore contains two nonzero
entries. So `M` is not a signed-permutation matrix, and
`is_proper_cubic(M)` is false. A predicate “`diag(L, 1)` is a proper cubic
matrix” fails.

The same rejection applies to any integer 2×2 matrix that preserves
`η_2 = diag(1,−1)` other than the Euclidean-type elements `±I` and the
swap-with-signs that remain in `O(1,1)` of Euclidean type: those matrices
are still 2×2, and a nontrivial boost-like integer block still fails the
3×3 monomial ±1 test after `diag(·, 1)` embedding.

## Theorem 4 — the parent sentences name no boost

The current axiom memo states the Lattice named symmetry as:

> standard translations, and proper cubic rotations about each site.

That is a 3-dimensional cubic rotation statement on `Z^3`. It does not name
a boost, a fourth axis, or a `(3,1)` form.

The kinetic-isotropy primitive supplies one structural graining equality

```text
c_t = c_s,
```

one Euclidean tick equal in form to one spatial edge. It is a regulator
normalization on a Euclidean block, not a Lorentz theorem. The primitive
states that full Lorentz restoration remains a separate claim and is not
supplied by the declaration. Neither parent sentence names a boost.

## Theorem 5 — extra Lorentzian object, displayed only

A Lorentzian boost is not an element of `G`. The extra object that would
make a boost well-typed is:

- a **fourth direction**, so that linear maps act on a 4-component
  `(t, x_1, x_2, x_3)` rather than on the three Lattice coordinates;
- a **`(3,1)` form**, for example `η = diag(1,1,1,−1)` or
  `η = diag(−1,1,1,1)`, whose preservation — not preservation of
  `x_1^2+x_2^2+x_3^2` — would define the boost.

Those two extras are displayed so the type gap is explicit. They are not
adopted. No fourth lattice direction is added to Lattice. No `(3,1)` form
is installed. No Wick parameter is chosen. In particular this note does not
install `a = 1`.

The 24 matrices of `G` sit inside `SO(3)` as exact rotation matrices. This
note does not say that the cubic 24 is `SO(3)`. The continuous group
`SO(3)` is larger than `G`.

This note does not claim that Lorentz closure is impossible. A later
construction may introduce a fourth direction and a `(3,1)` form by a
separate theorem. That construction is outside the present named-symmetry
count.

## What This Does Not Claim

- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not add a primitive, and it does not adopt the displayed
  fourth-direction or `(3,1)` extras.
- It does not install `a = 1` or any other Wick parameter.
- It does not identify `G` with `SO(3)`.
- It does not claim that Lorentz closure is impossible.
- It does not derive kinetic isotropy, and it does not promote
  `c_t = c_s` to a Lorentz theorem.
- It does not cite unmerged work.

## No-Go Gate

Shipping any of the following would be a failure of this note:

- asserting `|G| ≠ 24` after the enumeration above;
- asserting that `diag(L, 1)` is a proper cubic matrix;
- asserting that the Lattice cubic rotations are boosts;
- asserting that the cubic 24 is `SO(3)`;
- installing `a = 1`;
- claiming Lorentz closure is impossible;
- editing an axiom or adopting the displayed `(3,1)` extra.

## Exact Target And Obligation Graph

**Exact target.** Name the Lattice proper cubic symmetry as the 24-element
integer matrix group `G`, prove Euclidean preservation, and reject the
boost prototype as a member of `G`, without closing or forbidding a later
Lorentzian construction.

| Obligation | Role | Disposition |
|---|---|---|
| count signed-permutation matrices | Theorem 1 | proved: `3! × 2^3 = 48` |
| split by `det = +1` | Theorem 1 | proved: `|G| = 24` |
| Euclidean form preservation | Theorem 2 | proved: `R^T R = I_3` |
| reject `diag(1,1,−1)` as the defining form | Theorem 2 | proved as signature contrast |
| reject `L` and `diag(L,1)` | Theorem 3 | proved by size, entries, and monomial test |
| quote Lattice and kinetic isotropy | Theorem 4 | quoted; neither names a boost |
| display fourth direction and `(3,1)` form | Theorem 5 | displayed, not adopted |

The runner identity gates call `proper_cubic_count()` and
`is_proper_cubic(M)`. Those functions, not a hardcoded banner, decide the
order and membership checks.
