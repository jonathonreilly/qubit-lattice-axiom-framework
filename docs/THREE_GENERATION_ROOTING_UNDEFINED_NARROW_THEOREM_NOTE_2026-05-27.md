# Three-Generation Rooting Undefined Narrow No-Go Theorem

**Date:** 2026-05-27
**Claim type:** no_go
**Claim scope:** exact finite no-go for nonempty proper BZ-corner/taste
coordinate projections on the Hamiltonian `Cl(3)` / `Z^3` eight-corner
carrier. Any such projection fails to preserve the projected Clifford
anticommutators and fails to preserve the transitive taste-flip orbit. This
is a finite algebraic obstruction, not a physical species-semantics claim.
**Status authority:** independent audit lane only. This source note queues a
standalone no-go packet for audit; it does not apply or imply an audit
verdict.
**Primary runner:** `scripts/frontier_three_generation_rooting_coordinate_no_go.py`

---

## Theorem

Let

```text
H_taste = C^8
```

have basis labelled by BZ-corner bits `s in {0,1}^3`. Let the
Kawamoto-Smit Hamiltonian `Cl(3)` generators be

```text
G_1 = X tensor I tensor I,
G_2 = Z tensor X tensor I,
G_3 = Z tensor Z tensor X,
```

so that

```text
G_i G_j + G_j G_i = 2 delta_ij I_8.
```

For any nonempty proper coordinate subset

```text
S subset {0,1}^3,
```

let `P_S` be the diagonal projector onto the span of the corner basis states
in `S`. Then the compressed matrices

```text
P_S G_i P_S |_{P_S H_taste}
```

do not satisfy the `Cl(3)` anticommutator relations on `P_S H_taste`.

Equivalently, removing a nonempty proper set of BZ-corner tastes is not an
algebra-preserving Hamiltonian operation on this finite carrier.

---

## Independent Finite Obstructions

The no-go has two exact finite checks.

1. **Projected Clifford obstruction.** The runner exhausts all `254`
   nonempty proper coordinate subsets of the eight-corner basis. For every
   subset, at least one compressed anticommutator fails the required
   `2 delta_ij I` relation.
2. **Taste-flip orbit obstruction.** The three bit flips generate a
   transitive `(Z_2)^3` action on `{0,1}^3`. No nonempty proper coordinate
   subset is closed under all three flips.

These are exact finite algebra facts. No observed mass, fitted selector,
continuum regulator argument, same-surface family assumption, or Standard
Model generation interpretation is used.

---

## Explicit Non-Claims

This row does not claim that every arbitrary non-coordinate subspace of
`C^8` fails to carry some equivalent Clifford representation.

This row does not make a path-integral fourth-root statement.

This row does not identify the `hw=1` triplet with Standard Model
generations.

This row does not prove physical species semantics, substrate physicality,
CKM mixing, chirality, flavor structure, or full matter-content closure.

This row does not add a new axiom.

---

## Boundary

The auditable content is exactly:

1. the full eight-corner carrier satisfies the Hamiltonian `Cl(3)`
   anticommutators;
2. every nonempty proper BZ-corner/taste coordinate projection breaks those
   anticommutators after compression;
3. every nonempty proper BZ-corner/taste coordinate projection breaks closure
   under the transitive taste-flip orbit.

This is the missing no-rooting packet requested by the latest audit of the
parent `THREE_GENERATION_STRUCTURE_NOTE.md`. It does not by itself update the
parent row's audit status.

---

## Command

```bash
python3 scripts/frontier_three_generation_rooting_coordinate_no_go.py
```

Expected result:

```text
PASS=12 FAIL=0
```

---

## Relation To The Parent Row

The parent `three_generation_structure_note` audit blocker said the broader
four-item scope needed either a scope split or a retained-grade no-rooting
narrow theorem as a direct dependency. This row supplies the source-side
no-rooting theorem packet for the BZ-corner/taste-projection part of that
blocker. Independent audit still decides whether it becomes retained-grade.
