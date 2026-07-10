# Single-Clock Blocked-Time Unit Split: N2 Internal Support Boundary

**Date:** 2026-06-17
**Claim type:** bounded_theorem
**Claim boundary:** source support for the internal two-step
blocked-transfer denominator; no derivation of an absolute physical clock
unit from the current framework surface.
**Target blocker:** `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`
declares (B-AXIS.1) as "one supplied blocked time step `2a_tau` (= N2)".
This note splits that phrase into a source-proved internal denominator and an
undischarged absolute-unit premise.
**Audit boundary:** this source note does not edit audit ledgers, queue rows,
effective-status files, or publication status surfaces. Independent audit
owns any effective verdict.
**Primary runner:** [`scripts/single_clock_blocked_time_unit_split_n2_support_2026_06_17.py`](../scripts/single_clock_blocked_time_unit_split_n2_support_2026_06_17.py)
(`TOTAL: PASS=37 FAIL=0`).

## Result

For the single-clock parent row, the N2 blocked-time clause has two distinct
meanings:

1. **Internal blocked-transfer denominator.** Given the retained-bounded
two-step transfer supply `T_hat^2`, the denominator in the reconstructed
Hamiltonian is fixed to the two-step block `2 a_tau`:

   ```text
   H_block := -(1/(2 a_tau)) log(T_hat^2 / M_T).
   ```

   This is not an additional free import. It is exactly the source-side
   consequence of using the two-step staggered transfer object. Using
   `1/a_tau` with the same `T_hat^2` doubles every non-vacuum energy.

2. **Absolute physical clock unit.** The current minimal framework still does
   not derive the physical scale or metric content represented by `a_tau`.
   Rescaling the supplied clock denominator rescales the reconstructed
   generator while preserving the same dimensionless transfer data. Record
   histories likewise preserve word order and counts under inequivalent
   strictly increasing clock maps. Therefore a physical clock/rate unit must
   still be supplied by a separate clock/rate bridge if a physical-rate claim
   needs it.

So the parent row should no longer treat the whole N2 sentence as a single
opaque import. The internal denominator `2 a_tau` is source-supported for the
supplied `T_hat^2`; the absolute unit carried by `a_tau` remains outside the
minimal axioms and outside Record alone.

## Inputs

- **Two-step blocked-time normalization bridge.**
  [`AXIOM_FIRST_SPECTRUM_CONDITION_BLOCKED_TIME_NORMALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](AXIOM_FIRST_SPECTRUM_CONDITION_BLOCKED_TIME_NORMALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
  proves that `T_hat^2` advances one physical block of two lattice steps and
  that `H = -(1/(2 a_tau)) log(T_hat^2/M_T)` is the aligned reconstruction for
  that object.
- **Single-clock scope boundary.**
  [`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md)
  keeps Stone uniqueness transfer-relative and tau-relative; it does not let
  the transfer alone derive an absolute clock unit, axis uniqueness, or
  no-second-clock result.
- **Minimal framework axioms.**
  [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) states that
  Lattice supplies no metric scale, lattice spacing, or physical unit
  conversion, and Record supplies no time metric or dynamics. This markdown
  link is a load-bearing dependency edge (added 2026-07-10): the `2026-06-05`
  path is an aliased path of the canonical `minimal_axioms` premise node in
  `docs/audit/data/axiom_premise_nodes.json` (current path
  `MINIMAL_AXIOMS_2026-06-29.md`), so the edge resolves to the live
  minimal-axioms authority and its full text and effective status enter this
  note's dependency packet.
- **Post-record clock/rate boundary.**
  [`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md)
  proves that finite record histories determine event order and counts, not a
  physical clock metric or rates without a supplied clock map.
- **Record clock/rate normalization gate.**
  [`RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md`](RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md)
  separates stable locations under supplied generators from physical
  rate/clock normalization.

No observed values, fitted selectors, PDG comparators, lattice-MC values,
`beta = 6` values, or `g_bare` conventions enter this note.

## The Split

### N2a: internal blocked-transfer denominator is supported

The two-step normalization bridge already supplies:

```text
T_hat^2 = exp(-2 a_tau H_hat),
H_hat = -log(T_hat^2)/(2 a_tau).
```

Let `M_T` be the top transfer eigenvalue used for vacuum normalization. Finite
functional calculus gives

```text
H_block = -(1/(2 a_tau)) log(T_hat^2 / M_T) = H_hat - E_0.
```

If the same imported object `T_hat^2` is reconstructed with the one-step
denominator instead, then

```text
H_wrong = -(1/a_tau) log(T_hat^2 / M_T) = 2 H_block.
```

Thus, for the parent single-clock row's supplied `(T_hat^2, 2 a_tau)` object,
the factor of two is fixed internally by the framework source chain. It is not
a literature convention and not a new axiom.

### N2b: absolute physical clock unit is not derived

The same algebra also shows what is not closed. For any positive scale factor
`c`, declaring a block time `2 c a_tau` for the same dimensionless transfer
reconstructs

```text
H_c = -(1/(2 c a_tau)) log(T_hat^2 / M_T) = H_block / c.
```

The transfer object has not changed; only the physical clock denominator has.
Minimal Lattice gives the site set and adjacency but no metric scale, lattice
spacing, or physical unit conversion. Record gives durable realized outcomes
and finite scalar additivity but no time metric, physical elapsed time, clock
map, Hamiltonian, or transition rate. Post-record count streams can be embedded
into many inequivalent clocks while preserving the same word and counts.

Therefore the current framework proves the internal denominator of the
two-step transfer but does not derive the absolute physical value of `a_tau`.
Any downstream physical-rate or unitful mass claim must still identify the
separate clock/rate bridge it consumes.

## Parent-Row Consequence

The single-clock parent can safely refine (B-AXIS.1) as follows:

```text
(B-AXIS.1a) supported internally: the supplied RP/SC transfer object is
T_hat^2, so the source-side block denominator is 2 a_tau.

(B-AXIS.1b) still open/supplied: the absolute physical clock unit or time
metric represented by a_tau is not derived from Lattice, Quantum, Record, or
post-record counts alone.
```

This does not close (B-AXIS.2) axis/transfer-construction uniqueness and does
not close (B-AXIS.3) exclusion of independent commuting transfer factors. It
also does not promote the parent row to retained status. It narrows one
sub-blocker and gives the reviewer/auditor a cleaner re-audit target.

## Proof

**Step 1.** The two-step normalization bridge proves that the imported
transfer object is not a one-step transfer but the period-two blocked object
`T_hat^2 = T_odd T_even`. The positive, time-translation-invariant transfer
therefore advances one block of two lattice spacings. The only aligned
spectral reconstruction is the finite functional calculus with denominator
`2 a_tau`. This proves N2a.

**Step 2.** The single-clock scope boundary remains transfer-relative and
tau-relative. A positive transfer plus Stone reconstruction fixes a generator
only after the time denominator is supplied. Replacing `2 a_tau` by
`2 c a_tau` rescales `H` by `1/c` without changing `T_hat^2`. This proves that
the absolute clock unit is not contained in the transfer spectrum alone.

**Step 3.** Minimal Lattice and Record exclude the missing physical clock
content: no metric scale, lattice spacing, physical unit conversion, time
metric, dynamics, clock map, Hamiltonian, or transition rate is supplied by
those axioms. The post-record clock/rate boundary independently shows that a
fixed finite record word admits many strictly increasing clock maps with
different elapsed times and rates. This proves N2b.

**Step 4.** Since N2a is source-supported and N2b remains open/supplied, the
parent should treat B-AXIS.1 as a split boundary rather than as one monolithic
declared premise. B-AXIS.2 and B-AXIS.3 are untouched.

## Validation

Run:

```bash
python3 scripts/single_clock_blocked_time_unit_split_n2_support_2026_06_17.py
```

The runner checks:

- source anchors for the parent B-AXIS.1 wording and the two-step
  normalization bridge;
- finite-dimensional reconstruction of diagonal positive transfers;
- the wrong one-step denominator doubling falsifier;
- tau-rescaling and dimensionless-transfer invariance;
- post-record histories preserving words and counts under inequivalent clocks;
- minimal-axiom and Record clock/rate no-go anchors;
- the minimal-axioms markdown dependency edge and its aliased-path mapping to
  the canonical `minimal_axioms` premise node;
- no audit-ledger, audit-queue, effective-status, or publication-surface
  edits in the branch;
- explicit boundaries that keep this support from becoming a status or audit
  verdict.

Expected output: `TOTAL: PASS=37 FAIL=0`.

## Boundaries

- Does not derive the axis-selection part of B-AXIS.2.
- Does not exclude independent commuting transfer factors for B-AXIS.3.
- Does not derive an absolute physical time unit, physical lattice spacing,
  physical mass scale, or rate normalization.
- Does not add a framework axiom.
- Does not update audit results, audit queues, effective-status summaries, or
  publication matrices.
- Does not claim retained, promoted, or audit-ratified status.
