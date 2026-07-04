# Born Rule From Finite Ideal Records

**Date:** 2026-05-20
**Claim type:** bounded_theorem — bounded support note
**Primary runner:** `scripts/born_rule_framework_bridge_check.py`
**Type:** conditional / support

## Scope

This row proves a finite ideal-record Born-rule bridge on qubit-lattice
regions. It replaces the earlier raw Gleason/Busch/Lueders import wording with
direct framework source rows for the finite effect-probability form, the
pre-record tracial reference, finite Kraus/Choi representation, and canonical
projective-record update.

The binding surface is intentionally narrow:

- finite qubit-lattice regions only;
- POVM/effect probabilities represented as `p(E) = Tr(rho E)`;
- unique tracial state `tau = I/d` on a finite region, with the physical
  identification `tau = rho_ref` treated as the open conditional bridge;
- ideal unrefined sharp-projective records with update
  `rho -> P rho P / Tr(P rho P)`;
- sequential projective effects of the form `P E P`;
- rank-one post-record probabilities
  `Tr(|psi><psi| |phi><phi|) = |<phi|psi>|^2`.

This row does not claim durable/native persistent-record formation, arbitrary
unsharp-instrument uniqueness, or closure of the older gravitational-Hartree
Born route.

## Framework-Dependency Repair

Earlier versions treated the Gleason/Busch, Lueders, and Kraus/readout pieces
as raw standard-math imports. This note now routes the finite ideal-record
claim through in-repo source rows:

- [`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
- [`BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
- [`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md)
- [`KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
- [`LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md`](LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md)
- [`LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md`](LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md)
- [`LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md`](LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md)

Background textbook mathematics remains useful context, but the load-bearing
finite-region steps above are sourced through these framework rows. The
pre-record tracial source row supplies the unique normalized tracial state;
it does not by itself supply the physical identification of that state with
the pre-record reference.

## Claim

Let `A_Lambda = tensor_x M_2(C)` be a finite qubit-lattice region with Hilbert
dimension `d = 2^|Lambda|`. Let `E` be a POVM effect on that finite algebra.
The finite effect-probability rows supply

```text
p(E) = Tr(rho E)
```

for a unique density matrix `rho`. The pre-record tracial row supplies the
finite tracial state

```text
tau = I_d / d.
```

This row conditionally sets `rho_ref = tau` for the finite ideal-record
bridge. That physical pre-record identification remains open until a direct
bridge supplies it.

For an ideal sharp projective record `P`, the projective-record rows supply the
canonical update

```text
rho | P = P rho P / Tr(P rho P),
```

and the sequential effect

```text
P then E  ->  P E P.
```

If `P = |psi><psi|` is a complete rank-one projective record on a subsystem,
then applying the update to the conditionally identified tracial reference
gives

```text
rho_ref | P = |psi><psi|.
```

A subsequent rank-one projective effect `E = |phi><phi|` therefore has
probability

```text
Tr(|psi><psi| |phi><phi|) = |<phi|psi>|^2.
```

This is the Born form on the finite ideal-record surface.

## Proof

1. The finite Gleason/Busch source rows give the trace-density form
   `p(E) = Tr(rho E)` for finite-region effects, including the single-site
   POVM case.
2. The pre-record tracial-reference source row gives the unique finite
   tracial state `tau = I_d/d`; this row conditionally identifies
   `rho_ref = tau` for the ideal-record bridge.
3. For a rank-one projective record `P = |psi><psi|`, the projective update
   gives

   ```text
   P rho_ref P / Tr(P rho_ref P)
   = P (I_d/d) P / Tr(P/d)
   = P/d / (1/d)
   = P.
   ```

4. For a later rank-one effect `E = |phi><phi|`,

   ```text
   Tr(P E) = Tr(|psi><psi| |phi><phi|)
           = <psi|phi><phi|psi>
           = |<phi|psi>|^2.
   ```

5. The sequential-effect row supplies the same conditional result through
   `Tr(rho_ref P E P) / Tr(rho_ref P)`.

These are finite-dimensional matrix identities once the cited framework rows
supply the probability representation and ideal projective-record update.

## Non-Claims

This row does not claim:

- durable/native persistent-record formation;
- arbitrary unsharp-instrument uniqueness;
- that native apparatus dynamics have been reduced to the ideal projective
  record surface;
- a repair of every failed gravitational-Hartree Born argument;
- a closed physical identification of the unique tracial state with the
  pre-record reference;
- a numerical-prediction change.

## Validation

The runner `scripts/born_rule_framework_bridge_check.py` checks:

- finite tracial probabilities `Tr((I/d)E)`;
- single-site POVM probabilities through `Tr(rho E)`;
- projective-record Lueders conditioning from `I/2` to a rank-one projector;
- the rank-one identity `Tr(|psi><psi| |phi><phi|) = |<phi|psi>|^2`;
- sequential projective effects `P E P`;
- projective Kraus trace preservation;
- source-note dependency and firewall wording.

## Context Pointers

Plain-text context only, not load-bearing dependencies of this row:

- `BORN_RULE_ANALYSIS_2026-04-11.md` - older gravitational-Hartree route.
- `NONLINEAR_BORN_GRAVITY_NOTE.md` - adjacent repair target.
- `PERSISTENT_RECORD_OVERLAP_KERNEL_NOTE.md` - durable/native record
  formation context.
- `LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md`
  - locality context for record conditioning.
