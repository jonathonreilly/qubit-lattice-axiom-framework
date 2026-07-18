# Foundation Site-Net Record Equivalence Classification — Cycle 21

**Date:** 2026-07-14

**Type:** authority-free exact theorem and physical-closure probe

**Authority:** none. This note does not amend an axiom, define the final
physical-equivalence relation, select a microscopic law or boundary, register
a premise, issue an audit verdict, or authorize a repository publication.

## Question

The finite adaptive transport theorem proves that a history-dependent unitary
change of frame can preserve every transported protocol statistic. Which of
those algebraic frame changes also preserve the foundation's *physical*
ontology: named lattice sites, one `M_2(C)` possibility algebra per site, at
most one record per site, and scalar-additive record readout?

The distinction is between two categories:

1. the **foundation-maximal site-record category**, in which every one-site
   rank-one possibility can occur in some transported law/context; and
2. a **law-selected record category**, in which the exact dynamics may select
   a smaller pointer algebra such as local `Z`.

## Result Up Front

There is an exact finite-dimensional classification.

> Let `A=(M_2)^(tensor n)` with named site factors `A_i`. Any star
> automorphism of `A` that permutes the set of named factors `{A_i}` is a site
> permutation followed by onsite unitary recodings, up to an irrelevant global
> phase. If translations and the common qubit recoding are also respected, the
> onsite recoding is common across translated sites.

Thus an entangling finite-depth circuit is not an automorphism of the
foundation-maximal named site-record category. It maps at least one one-site
possibility algebra to a distributed subfactor. For example,

```text
Ad_CZ(X_1)=X_1 Z_2,
Ad_CZ(Z_1)=Z_1.
```

`CZ` therefore preserves the local `Z` record algebra but not the full
one-site `M_2` record net. It can be gauge for a law-selected `Z`-record
category, but it is not automatically gauge merely because it is finite
depth. Exact record-net closure is still required.

This closes the fixed foundation-maximal named-net classification. It does not
select the exact law-selected record category or decide whether physical
equivalence may transport the whole net. A final law may derive a pointer
algebra whose normalizer is larger. If every site factor, record, rule,
boundary, and readout is transported together, an entangling frame is an exact
groupoid morphism between net presentations. Whether that is the same physical
site ontology is the remaining semantic cut.

No axiom sentence follows. The exact-law referent may be quotiented by the
foundation group immediately and by any larger law-relative group only after
record, boundary, and cost closure are proved.

## 1. Exact Classification Proof

Every star automorphism of a finite full matrix algebra is inner, so write

```text
alpha = Ad_U.
```

Suppose `alpha(A_i)=A_(pi(i))` for a permutation `pi`. Compose `U` with the
inverse tensor-factor permutation. The resulting unitary `W` normalizes every
`A_i` separately. Its restriction to each `A_i ~= M_2` is an inner
automorphism, so choose an onsite `u_i` implementing it. Then

```text
V = tensor_i u_i
```

has the same action as `W` on every factor. Hence `V^dagger W` fixes every
`A_i` pointwise. The factors generate all of `A`; their pointwise commutant in
`A` is the center, so

```text
V^dagger W = exp(i theta) I.
```

Undoing the factor permutation gives

```text
U = exp(i theta) P_pi (tensor_i u_i).
```

The converse is immediate. This is an if-and-only-if theorem.

On a translated lattice, covariance of the recoding gives
`u_(x+a)=u_x` in projective action, so all `u_x` are one common `PU(2)`
recoding. A factor permutation also has to be an allowed lattice symmetry to
preserve the named nearest-neighbor relation. The already supplied
foundation-licensed group is therefore translations and proper cubic
rotations, together with common complex-linear `PU(2)` recoding. Reflections,
antiunitaries, site-dependent frames, and distributed QCA factors require
additional physical justification.

## 2. Exact Clifford Census

The two-qubit Pauli quotient gives a complete finite control. Ignoring Pauli
signs, two-qubit Clifford automorphisms are the symplectic group
`Sp(4,2)`, of size `720`. The two site factors are the symplectic planes

```text
V_1=span(X_1,Z_1),
V_2=span(X_2,Z_2).
```

Exactly `72` symplectic maps permute `{V_1,V_2}`:

```text
|Sp(2,2)|^2 * 2! = 6^2 * 2 = 72.
```

These are precisely the local-Clifford actions plus site swap at the Pauli
level. The other `648` are entangling factor maps. Restoring the `16` Pauli
translations gives `1152` site-net-preserving elements inside the
`11520`-element two-qubit Clifford group modulo phase.

The census is not the general proof; it is an exhaustive exact control against
an unnoticed entangling exception.

## 3. Records And Additive Cost

A rank-one one-site record projector has the form

```text
P_(n,+) tensor I = (I+n.X)/2 tensor I.
```

Preserving every such projector is equivalent to preserving its full named
site factor. `CZ` fails on the `X` and `Y` rays even though it succeeds on `Z`.
Because the Qubit axiom privileges no possibility, foundation-level
equivalence cannot quietly test only the `Z` ray.

The same example exposes record cost. A one-site `X` content is carried by a
weight-one Pauli; after `CZ` it is `X_1 Z_2`, supported on two named sites. If
the distributed subfactor is called one record, the physical site occupancy
and max-one-record/site rule have been redefined. If it is called two records,
scalar-additive readout and capacity change. Either choice is additional
structure. By contrast, onsite recodings and site permutations preserve the
number of named record slots exactly.

This does not forbid distributed error-correcting records in a selected law.
It says their encoding map and cost decoder must be part of that law and must
be proved equivalent; they are not licensed by the bare site ontology alone.

## 4. Consequence For The Minimum Constitutional Content

The adaptive theorem and this classification fit together:

```text
finite adaptive algebraic transport
  + foundation-maximal site-record closure
  => translations/proper cubic maps + common onsite PU(2) recoding

finite adaptive algebraic transport
  + law-selected pointer/record subcategory
  => possibly larger law-relative quotient, only after an exact closure proof
```

The exact law cannot be replaced by a bare finite-depth, QCA, anomaly, or
intrinsic-simulation class. A quotient is physical only when it preserves the
complete record protocol and its named-site/cost ontology. The universal
constitutional residue remains one stable exact law identity or a fully
defined record-faithful equivalence class, unless uniquely derived.

## No-Go Discipline Gate

The narrow negative claim is:

> Entangling finite-depth conjugacy alone is not a foundation-licensed physical
> equivalence of the maximal named one-site record category.

This is not a no-go against a larger equivalence derived from a selected law.

### N1 — Alternative-route enumeration

Attempted routes: arbitrary inner automorphism; factor-permuting
automorphism; fixed-factor normalizer; exhaustive Clifford census; local
`Z`-record normalizer; all-ray record normalizer; transported distributed net;
translation covariance; and readable additive-cost preservation.

### N2 — Wall-independence audit

Algebraic adaptive equivalence does not imply physical category closure;
physical closure does not select the exact update; a selected pointer algebra
does not cause record occurrence; occurrence does not select a boundary or
weights. These fields remain logically distinct and are not multiplied into
new axiom sentences.

### N3 — Hidden-wall scan

`Site`, `local`, `record`, `same`, `transport`, `cost`, `factor`, and
`equivalence` are expanded above. In particular, transporting the tensor net
is not called free: it changes the interpretation of the named Lattice and
Record clauses unless an exact isomorphism preserves their operational tests.

### N4 — Exact residual matching

The general factor theorem addresses site-net closure. The `Sp(4,2)` census
checks the finite Clifford case. `CZ` supplies the exact all-ray versus
pointer-subalgebra separator. Pauli support supplies the cost/occupancy
separator. None of these witnesses is used to select dynamics or actuality.

### N5 — Resolution and rhetoric audit

The theorem is exact for finite tensor products and extends quasilocally to
strict factor-permuting net automorphisms. The note does not classify every
bounded-range QCA after stabilization, every encoded record subfactor, or
every law-selected pointer category.

### N6 — Partial-closure paths

A selected law can: derive a local pointer algebra normalized by a larger
frame family; provide an exact distributed encoding with unchanged operational
cost; or make the representative phase empirically visible. Each is a
positive path. The foundation group remains available without those imports.

### N7 — Strongest surviving steelman

The physical sites themselves may be relational, with a QCA transporting the
entire net so that a distributed subfactor is the same abstract site in a
different presentation. The stronger companion classification proves that
this is algebraically consistent when factors, adjacency/rule, records,
boundary, readout, and cost are all transported. The current axioms name
`Z^3` sites and one `M_2` at each but do not explicitly define isomorphisms of
that structure. Thus the algebraic route is positive and the semantic
fixed-versus-transported reading remains live.

### N8 — Cross-cycle echo

Cycle 19 found that a fixed record decoder separates finite-depth-related
updates. Cycle 20 proved full finite adaptive transport and isolated physical
category closure. This finite census proves the maximal factor-preserving
closure; the stronger named-site classification proves selected-pointer and
transported-net positive routes. The remaining issue is semantic site
identity. None revives a Record trigger, witness count, clock lock, or
presentation-counting sentence.

## Companion Runner

Run:

```bash
python3 scripts/foundation_site_net_record_equivalence_classification_cycle21_2026_07_14.py
```

It exhausts `Sp(4,2)`, checks the factor-preserving subgroup, verifies exact
`CZ`/swap Pauli images and support costs, and enforces the authority and
N1--N8 contracts.
