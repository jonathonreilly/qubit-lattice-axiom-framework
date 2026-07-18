---
claim_id: g_bare_two_ward_rep_b_independence_theorem_note_2026-04-19
claim_type_author_hint: bounded_theorem
audit_authority: independent audit lane only
---

# Conditional Rep-B Matrix Corollary for the Two-Ward Route

**Date:** 2026-04-19 (source-boundary repair 2026-07-18)
**Type:** bounded_theorem
**Claim scope:** a conditional finite-matrix corollary. If a
parameter-indexed physical Rep-B operator is separately represented on a
fixed normalized six-dimensional basis by matrices that are positive
semidefinite, central in the full matrix algebra, and Hilbert--Schmidt unit,
and if the physical form factor is separately identified with a diagonal
matrix expectation, then the form factor is `1/sqrt(6)` at every parameter
value. The current dependency set does not derive either physical bridge.
**Status authority:** independent audit lane only.

## Abstract authority consumed

The
[central-positive Hilbert--Schmidt unit theorem](UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md)
proves the following statement for an abstract matrix `H in End(C^n)`:

```text
H >= 0,
[H,E_jk] = 0 for every matrix unit E_jk,
Tr(H^dagger H) = 1
    implies
H = I_n / sqrt(n).
```

That theorem does not mention a physical `H_unit`, a gauge parameter, a
carrier assignment, a Wick contraction, or a Ward identity.

## Local conditional bridge

Let `G` be any parameter domain. The following are ordinary local hypotheses
of this corollary; they are not framework axioms, admissions, premise-registry
entries, or established physical inputs.

**H-MATRIX.** For every `g in G`, a separate physical construction supplies
a matrix representative `K(g) in End(C^6)` such that

```text
K(g) >= 0,
[K(g),E_jk] = 0 for all 1 <= j,k <= 6,
Tr(K(g)^dagger K(g)) = 1.
```

Centrality here means commutation with the full algebra `End(C^6)`, not only
with a chosen color, isospin, gauge, or Ward-symmetry subalgebra.

**FORM-FACTOR IDENTIFICATION.** A separate construction identifies the
physical Rep-B form factor with a normalized diagonal expectation of that
same representative:

```text
F_RepB(g) = <e_j, K(g) e_j>
```

for a specified normalized basis vector `e_j`.

## Conditional conclusion

Under H-MATRIX, the abstract theorem applies pointwise in `g` and gives

```text
K(g) = I_6 / sqrt(6).
```

Under FORM-FACTOR IDENTIFICATION as well,

```text
F_RepB(g) = 1 / sqrt(6)  for every g in G.
```

Thus parameter independence follows only after both local bridges have been
supplied for the whole parameter domain. Absence of a parameter from the
abstract theorem is not itself a physical independence argument.

## Open physical boundary

This note does not derive H-MATRIX or FORM-FACTOR IDENTIFICATION for the
two-Ward construction. In particular, it does not prove that:

- the physical composite called `H_unit` has a positive matrix
  representative;
- it commutes with every endomorphism rather than a selected symmetry
  algebra;
- its physical residue convention is the Hilbert--Schmidt condition
  `Tr(K^dagger K)=1`;
- the labels in a factorization `6 = 2 * 3` have any physical assignment;
- a Wick matrix element, free-field residue, Ward identity, tree-level gauge
  sector, `g_bare` selector, top-Yukawa datum, or observed quantity is the
  abstract diagonal expectation.

Without H-MATRIX, a central family may have the form `K(g)=a(g)I_6` with an
unfixed scale, so its diagonal expectation can depend on `g`. Without the
form-factor identification, even a solved abstract matrix has no physical
readout attached to it.

The same-projected 1PI identification and any subsequent `g_bare` pinning
remain separate open steps. This conditional corollary supplies neither.

## Dependencies

- [UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md](UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md)
  for the abstract central-positive Hilbert--Schmidt uniqueness theorem only.

No physical bridge authority is cited because none is established here.
