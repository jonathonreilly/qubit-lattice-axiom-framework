# Koide Convention-Invariant Scalar-Selector Doublet Constancy (Narrow Theorem)

**Date:** 2026-07-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Primary runner:**
[`scripts/koide_convention_invariant_scalar_selector_doublet_constancy_2026_07_12.py`](../scripts/koide_convention_invariant_scalar_selector_doublet_constancy_2026_07_12.py)
**Cache:**
[`logs/runner-cache/koide_convention_invariant_scalar_selector_doublet_constancy_2026_07_12.txt`](../logs/runner-cache/koide_convention_invariant_scalar_selector_doublet_constancy_2026_07_12.txt)

## Purpose

The einselection-era calculation distinguished two facts. The Hermitian
operator `C+C^2` is conjugation-even and resolves singlet from doublet, while
the Hermitian operator `i(C-C^2)` resolves the two doublet sectors but changes
sign under conjugation.

This note proves the narrow statement supported by that algebra. On the
supplied abstract `C_3` sector surface, a convention-invariant selector into a
pointwise-fixed scalar-label space is constant on the conjugate doublet. The
result is about fixed scalar labels. It does not say that the finest unlabeled
sector partition has two blocks: an unordered three-atom spectral PVM is a
decisive counterexample to that stronger claim.

## Theorem (narrow)

### T1 — The complex-unit orientation is not named content

The argument is a positive-list one, not an exclusion one. The sentence
"adds no further primitive structure" constrains what the real presentation
contributes; by itself it does not exclude the complex structure of the
`M_2(C)` presentation from the primitives. What decides the question is the
memo's named-content burden. The live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) states:

> These axioms state only their named primitive content. Further physical
> structure requires a retained derivation or bridge, or explicit approved-
> primitive registration, before use as a premise. A choice not fixed by the
> supplied structure remains a named conditional or open dependency.

The axioms do not name an orientation of the complex unit. The runner makes
this mechanical with a two-model witness. The standard Pauli presentation and
its entrywise-conjugate satisfy the same `Cl(3,0)` relations and the same
abstract `M_2(C)` presentation, while their central pseudoscalars are `+iI`
and `-iI`. Entrywise conjugation is multiplicative and real-linear on the full
eight-monomial real spanning basis. Holding the Lattice, Admissibility, and
Record data fixed therefore gives two presentations of the named content that
differ only in complex-unit orientation. The label `M_2(C)` does not select
between them: field conjugation maps the presentation to its conjugate.

The real presentation reinforces this conclusion without supplying the
positive-list burden. The memo also states:

> A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently and
> adds no further primitive structure.

There the complex unit is represented by the central pseudoscalar
`omega_ps=e_1e_2e_3`, with `omega_ps^2=-1`. Reversing generator orientation
changes its sign, and the canonical grade involution `e_i -> -e_i` sends
`omega_ps -> -omega_ps`.

Thus the complex-unit orientation is not fixed by the named supplied
structure. Under the live Qualification it remains a named conditional or
open dependency; it is not available to an `A_min`-only fixed-label selector.

### T2 — Conjugation swaps the doublet sectors on the abstract sector surface

On the supplied abstract `C_3` sector algebra, let `C` be the real cyclic
matrix and define

`P_chi=(1/3)(I+conjugate(chi)C+conjugate(chi^2)C^2)`

for `chi` in `{1,w,conjugate(w)}`, where
`w=-1/2+(sqrt(3)/2)i`. These character projectors resolve the identity.
Entrywise conjugation fixes `C` and `P_1` and swaps
`P_w <-> P_conjugate(w)`. The cyclic translation operator has a real
permutation-matrix presentation; its two nonreal character labels are
exchanged rather than individually fixed.

This is a statement about the defined abstract sector algebra. It does not
identify that algebra with a physical charged-lepton carrier.

### T3 — Fixed-label scalar selectors are doublet-constant

Let `tau` fix the singlet sector and exchange the two doublet sectors. Let
`f` map the three sectors into a scalar-label space on which `tau` acts
trivially. A selector derived without an orientation choice must satisfy

`f(tau(x))=f(x)`.

Therefore

`f(w-sector)=f(conjugate(w)-sector)`.

The exhaustive finite check evaluates all 27 functions from the three sectors
to three fixed labels. Exactly 9 are invariant under domain pullback by `tau`,
and every invariant function is doublet-constant. Their fiber partitions are
only the one-block partition and `{singlet,doublet-orbit}`.

The two-block scalar distinction is attained, not merely bounded above:
`C+C^2` is conjugation-fixed and has eigenvalue `2` on the singlet projector
and eigenvalue `-1` on the rank-two doublet projector. Hence the finest fiber
partition available to a convention-invariant **fixed-label scalar selector**
has the two blocks `{singlet,doublet-orbit}`.

The bold qualifier is load-bearing. This theorem does not classify unlabeled
partitions, equivariant labels, or PVMs whose atoms are permuted.

## Decisive counterexample to the stronger partition claim

Set

`O=i(C-C^2)`.

The runner verifies that `O` is Hermitian, has eigenvalues
`{-sqrt(3),0,+sqrt(3)}`, and obeys `conjugate(O)=-O`. Choosing the signed
observable `O` rather than `-O`, or attaching the fixed sign labels
`+sqrt(3)` and `-sqrt(3)` to the two doublet sectors, requires an orientation.

But the unordered spectral PVM is the same for either representative:

`{P_1,P_w,P_conjugate(w)}`.

Conjugation swaps two atoms and fixes the set. Thus the unlabeled three-block
partition is convention-stable and resolves all three sectors without
privileging either doublet member. Convention freeness alone does not derive
ORBIT-INDEXING or identify the conjugate sectors as one record content.

## Boundary consequence — the sibling partition is not discharged

The landed sibling context
`ACPHILAMBDA_OCCUPANCY_GRAIN_RULE_CLASS_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-07-11.md`
declares:

> The charged-lepton 2-sector occupancy surface is the K/CPT-orbit partition
> `{singlet sector, doublet orbit}` with occupancy distribution `(p_s,p_d)`,
> `p_s+p_d=1`, where the equal-power-per-block grain reads `r=1/2` at
> `p_s=p_d`.

The fixed-label scalar-selector theorem does not derive that supplied
occupancy partition. The existing context handle
`KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md`
states explicitly that ORBIT-INDEXING is supplied and is not derived from
Record. Distinct conjugate record contents with an unordered PVM remain
compatible with the current axioms.

Accordingly, no registry or bridge discharge is available from this theorem.
Any future registry action remains owner-gated and requires a retained source
for ORBIT-INDEXING or an equivalent physical identification.

## What is not derived

1. K-reality's value face is not derived: there is no claim that `delta=0`
   and no claim about a registered phase magnitude.
2. The K-odd monitor `i(C-C^2)` exists, is Hermitian, and resolves the
   doublet. Its signed privileging is convention-dependent, while its
   unordered three-atom PVM remains convention-stable. Existence, signed
   privileging, and unlabeled partition structure are kept distinct.
3. A complex-unit orientation is not derived. Under current main it can only
   remain a named conditional/open dependency or follow a separately retained
   bridge or owner-approved primitive registration. For provenance, the
   superseded Qualification phrased the conditional escape as "unless that
   choice is admitted." Current main has no admission class, so that historical
   wording carries zero premise authority.
4. The physical charged-lepton carrier identification and ORBIT-INDEXING are
   not derived here.
5. No normalized weights, probability simplex, measure, or occupancy/grain
   selection is derived. The sibling's `p_s+p_d=1` and `r=1/2` readings remain
   supplied conditions there.
6. No R-eta bridge, mass content, comparator, threshold, record-formation
   rule, process, state, site, weight, or rate is selected.

## Scope boundary

- This is a finite theorem about fixed-label scalar selectors on a supplied
  abstract `C_3` sector algebra.
- It proves doublet constancy only when the selector codomain is pointwise
  fixed under the convention automorphism.
- Equivariant selectors and unordered PVMs whose outputs are permuted are
  explicitly allowed; their existence blocks the broader orbit-partition
  discharge.
- The K/CPT vocabulary, landed sibling declaration, and existing
  ORBIT-INDEXING bridge are context handles only. They carry no load-bearing
  citation-graph edge in this note.
- Effective status and any downstream use remain owned by the independent
  audit lane.

## Load-bearing dependency

| dependency | consumed content |
|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | the Qubit algebra presentations, no-privilege clause, and live named-content/conditional-choice Qualification |

## Runner verification map

| check block | exact verification | result |
|---|---|---:|
| V1 | five whitespace-flattened current-memo clauses: Qubit real presentation, no privilege, live conditional/open choice clause, Record additivity as a boundary check, and the named-content burden | PASS (5) |
| V2 | Pauli `Cl(3,0)` relations; `ps=+iI`, `ps^2=-I`; conjugated relations and `ps=-iI`; exact two-root center check and exchange; multiplicative and symbolic real-linear two-model witness | PASS (10) |
| V3 | grade involution multiplicativity on all `8 x 8` basis-monomial products and `alpha(ps)=-ps` | PASS (2) |
| V4 | projector resolution, idempotence, orthogonality, character equation, conjugation action, and fixed rank-two doublet block | PASS (8) |
| V5 | exhaustive domain-swap action on 27 fixed-label selectors, exactly 9 invariant selectors, doublet constancy, and the two possible fiber partitions | PASS (4) |
| V6 | K-odd Hermitian resolver, its conjugation-stable unordered three-atom PVM, K-even singlet/doublet scalar resolver, and character-`w` fixed-label flip | PASS (8) |
| V7 | landed sibling declaration and existing bridge's supplied ORBIT-INDEXING framing, checked as non-load-bearing boundary context | PASS (3) |

```text
TOTAL: PASS=40 FAIL=0
```

**No check passes by literal stipulation.**
