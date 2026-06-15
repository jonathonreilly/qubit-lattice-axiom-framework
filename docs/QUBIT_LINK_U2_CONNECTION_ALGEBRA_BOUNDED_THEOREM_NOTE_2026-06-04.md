---
claim_id: qubit_link_u2_connection_algebra_bounded_theorem_note_2026-06-04
claim_type_author_hint: bounded_theorem
---

# Qubit-Link U(2) Connection Algebra (Bounded Theorem)

**Date:** 2026-06-04
**Type:** bounded theorem
**Status:** source note awaiting independent audit handling.
**Primary runner:**
[`scripts/audit_companion_qubit_link_u2_connection_algebra_bounded_2026_06_04.py`](../scripts/audit_companion_qubit_link_u2_connection_algebra_bounded_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_qubit_link_u2_connection_algebra_bounded_2026_06_04.txt`](../logs/runner-cache/audit_companion_qubit_link_u2_connection_algebra_bounded_2026_06_04.txt)

## Claim

Condition on the narrow connection convention that a link connection between
two repo-baseline qubit fibers is a unitary map between their two-dimensional
complex Hilbert spaces. After choosing the standard Pauli frame on the target
fiber, the infinitesimal connection algebra is

```text
u(2) = su(2) + u(1)
```

as a Lie algebra direct sum. The `su(2)` summand is the Pauli spin-half
operator triple `S_i = sigma_i / 2`; the `u(1)` summand is the central phase
generator `i I_2`.

The same finite-dimensional algebra check also gives the color boundary: a
single two-dimensional qubit fiber has no faithful native `su(3)` color
algebra. Its full anti-Hermitian endomorphism algebra has real dimension 4,
and its traceless Hermitian part has dimension 3. A faithful `su(3)` algebra
would require an 8-dimensional simple Lie algebra embedding, equivalently the
usual three-dimensional fundamental color carrier or some additional
non-qubit multiplicity/selector structure. That structure is not supplied by
the Lattice, Quantum, and Record axioms.

This is a bounded theorem because the link-connection convention is an input
to this note, not an axiom and not derived here.

## Load-Bearing Inputs

- [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md) supplies
  the Lattice + Quantum + Record baseline, including the one-qubit local
  operator algebra `M_2(C)` at each site. The axiom baseline is a premise
  chain satisfier only; it is not a source of bounded status.
- [`PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md`](PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md)
  supplies the per-site Pauli `su(2)` spin-half module.
- [`INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md`](INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md)
  identifies the internal Pauli `su(2)` and the Clifford `Spin(3)`
  infinitesimal generators on the same `C^2` carrier.
- [`CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md`](CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md)
  supplies the two-dimensional per-site Hilbert carrier.

## What The Result Does Not Claim

- It does not derive a physical Standard Model gauge group.
- It does not identify the central `u(1)` with hypercharge assignments.
- It does not derive the chiral `SU(2)_L` restriction or matter multiplets.
- It does not derive gauge invariance of observables, gauge boson dynamics,
  an action, couplings, mixing angles, beta functions, or electroweak
  symmetry breaking.
- It does not derive color. It says the opposite narrow fact: native color is
  absent on a single qubit fiber unless an additional carrier or selector is
  supplied elsewhere.

The safe downstream phrase is therefore: the qubit-fiber unitary connection
has the same Lie-algebra shape as the electroweak `su(2) + u(1)` algebra, but
this note does not perform the physical electroweak identification.

## Runner Certificate

The runner verifies:

1. `S_i = sigma_i/2` satisfies `[S_i, S_j] = i epsilon_ijk S_k`;
2. `i I_2` is central and linearly independent from the `su(2)` generators;
3. the real anti-Hermitian endomorphism algebra of `C^2` has dimension 4;
4. the traceless Hermitian local operator space has dimension 3;
5. the spin-half Casimir is `3/4 I_2`;
6. a faithful native `su(3)` embedding into the single-qubit connection
   algebra is dimension-obstructed;
7. the source note keeps hypercharge, chirality, dynamics, gauge invariance,
   and matter content out of scope.

Run:

```text
python3 scripts/audit_companion_qubit_link_u2_connection_algebra_bounded_2026_06_04.py
```

Expected result:

```text
SUMMARY: PASS=19 FAIL=0
```
