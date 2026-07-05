# Record Pointer Controlled-Coupling Finite Example Bounded Theorem

**Date:** 2026-06-15
**Claim type:** bounded_theorem
**Status:** source-side split; no audit verdict or effective-status change.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/record_pointer_controlled_coupling_finite_example_2026_06_15.py`](../scripts/record_pointer_controlled_coupling_finite_example_2026_06_15.py)

## Purpose

This note splits the clean finite controlled-coupling example out of
`RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`.

The parent packet stated an over-broad equivalence between objective record
formation and pointer non-demolition dynamics. This split proves only a
concrete finite sufficiency example with explicit record-forming coupling and
persistence hypotheses.

## Finite Model

Use one system qubit `S` and `n` environment qubits `E_1..E_n`, all finite.
The pointer observable is

```text
Pi_S = sigma_z(S).
```

The environment starts in `|0>^{tensor n}` and the system starts in a generic
off-axis qubit state, so the pointer entropy `H(Pi_S)` is nonzero and below
one bit.

For any `g > 0`, define the controlled record-forming Hamiltonian

```text
H_rec(g) = g sigma_z(S) sum_k sigma_x(E_k).
```

At the explicitly rescaled recording time

```text
t_rec = pi / (4g),
```

the unitary `U_rec = exp(-i H_rec t_rec)` writes a full pointer record into
each singleton fragment.

## Theorem

In the finite model above:

1. `[H_rec(g), Pi_S] = 0` for every `g > 0`.
2. `U_rec` preserves the pointer populations of `S`.
3. At `t_rec = pi/(4g)`, the conditional fragment states for pointer outcomes
   `0` and `1` are orthogonal.
4. Therefore each singleton fragment carries the full pointer information
   `H(Pi_S)`.
5. If a first fragment has finished recording, a later local controlled
   recording step on another fragment preserves the first fragment's record.
6. The value of `g` is not selected by the finite example: changing `g` only
   rescales the recording time.

## Boundary

This note does not claim:

- the broad equivalence "objective record formation iff pointer
  non-demolition";
- derivation of the quantum-Darwinism record convention from the Record axiom;
- derivation of the physical pointer observable from the framework;
- derivation of a dynamics/action/coupling magnitude;
- any `beta = 6` or gauge-coupling result;
- any audit verdict.

The demolition control in the runner is only a boundary check: replacing the
system handle by `sigma_x(S)` fails the pointer commutant condition and changes
the pointer populations. It is not a proof of the broad necessity theorem.

## Verification

Run:

```bash
python3 scripts/record_pointer_controlled_coupling_finite_example_2026_06_15.py
```

Expected:

```text
TOTAL: PASS=18 FAIL=0
```
