# Three-Generation Rooting Undefined Narrow No-Go Theorem

**Date:** 2026-05-26
**Claim type:** no_go
**Claim scope:** exact Hamiltonian `Cl(3)` / `Z^3` no-rooting obstruction on
the eight BZ-corner taste carrier. Any proper BZ-corner/taste projection
that removes a nonempty proper subset of corners fails to preserve the
Hamiltonian `Cl(3)` carrier structure, the taste-flip symmetry, or the full
corner spectrum. This is a finite algebraic obstruction, not a physical
species-semantics claim.
**Primary runner:** `scripts/frontier_generation_rooting_undefined.py`
**Status authority:** independent audit lane only. This note queues a
standalone no-go packet for audit; it does not apply or imply an audit
verdict.

## Theorem

Let

```text
H_taste = C^8
```

be the eight-dimensional BZ-corner/taste carrier with basis labelled by
`s in {0,1}^3`. Let the Kawamoto-Smit `Cl(3)` generators act by the three
matrices

```text
G_1 = X tensor I tensor I
G_2 = Z tensor X tensor I
G_3 = Z tensor Z tensor X
```

so that `{G_i,G_j}=2 delta_ij I_8`.

For any nonempty proper corner subset `S subset {0,1}^3`, let `P_S` be the
coordinate projector onto the span of `S`. Then the projected matrices
`P_S G_i P_S` do not form a `Cl(3)` carrier on `P_S H_taste`. Exhaustively,
no coordinate subset of size `2..7` satisfies the three Clifford
anticommutator relations.

Equivalently, the Hamiltonian analogue of the staggered fourth-root trick is
not a well-defined operation on this finite `Cl(3)` carrier: removing taste
corners changes the defining algebraic object.

## Independent Obstructions

The no-go does not rest on one diagnostic. The runner verifies three exact
obstructions.

1. **Projected Clifford obstruction.** On the full carrier the
   anticommutators close exactly. On every proper coordinate subset of
   dimensions `2..7`, at least one projected anticommutator differs from
   `2 delta_ij I`.
2. **Taste-flip transitivity obstruction.** The three corner bit-flips
   generate a transitive `(Z_2)^3` action on `{0,1}^3`. A nonempty proper
   corner subset is not closed under all flips, so the taste symmetry is
   broken by any rooting projector.
3. **Spectrum obstruction.** Proper corner projection changes the finite
   Hamiltonian spectrum. The projected system is not the same Hamiltonian
   theory on a smaller taste carrier.

Each obstruction is internal finite algebra on the stated carrier. No PDG
values, observed masses, fitted selectors, continuum regulator assumption, or
same-surface family argument is used.

## Boundary

In scope:

- the exact `Cl(3)` anticommutator carrier on `C^8`;
- coordinate BZ-corner/taste projections;
- bit-flip taste symmetry on `{0,1}^3`;
- finite Hamiltonian spectrum comparison;
- the conclusion that rooting/removing tastes is not an algebra-preserving
  operation in this Hamiltonian carrier.

Out of scope:

- physical species semantics for the surviving `hw=1` triplet;
- identification with Standard Model generations;
- the full staggered-Dirac realization gate;
- any claim that the parent three-generation row is retained before this
  no-go packet and the parent row are independently audited.

## Relation To The Parent Three-Generation Row

The audited-conditional parent `THREE_GENERATION_STRUCTURE_NOTE.md` had a
`scope_too_broad` repair target: keep the broad four-item scope only after
adding a retained-grade no-rooting narrow theorem, or narrow the parent to
runner-backed spectral structure plus the retained `M_3(C)` no-proper quotient
theorem.

This note supplies the missing source-side no-rooting packet. It is not an
audit verdict. Once this no-go packet is independently audited, the parent can
be re-audited with two graph-visible one-hop packets:

- no-rooting: this note;
- no-proper-quotient: `THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md`.

## Validation

```bash
PYTHONPATH=scripts python3 scripts/frontier_generation_rooting_undefined.py
```

Expected result:

```text
FAIL=0
```

The runner exhausts all `246` nontrivial proper coordinate subsets of the
eight-corner carrier and checks additional named physically motivated
subsets plus random four-dimensional unitary subspace probes.
