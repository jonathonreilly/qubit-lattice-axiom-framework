# Charged-lepton Koide two-gate companion over the existing AC_phi_lambda registry

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set,
predict, or propose an audit outcome. It does not add, approve, or promote any
Tier-A entry; it consumes the already-existing `AC_phi_lambda` registry entry as
an explicit bounded premise and leaves audit/pipeline status to the independent
post-landing process.
**Primary runner:** [`scripts/frontier_charged_lepton_koide_two_gate_tier_a_bounded_verifier.py`](../scripts/frontier_charged_lepton_koide_two_gate_tier_a_bounded_verifier.py)

## Purpose

The parent row
`CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md` (backticked non-load-bearing
context reference; the parent is an open-gate admission surface preserved,
not consumed, by this companion)
keeps the charged-lepton Koide lane as an open two-gate problem:

- **Gate 1:** derive the dimensionless Koide surface selection
  `Q=2/3`, equivalently `r^2/a^2=1/2`.
- **Gate 2:** derive the Brannen phase identification `delta=Q/3=2/9`
  without an observed phase pin or convention-only period choice.

The chain-of-custody note
[`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)
documents the current chain modulo the existing Tier-A registry entry
`AC_phi_lambda` (the generation mass-pattern input: C3-breaking
phase/orientation plus the abstract-sector to physical-species bridge). This
note is a bounded companion that records exactly what follows once that
registry entry is explicitly consumed, while preserving the parent open-gate
row and all retained no-go boundaries.

## Claims

### S1 - Algebraic surface

On the Brannen-style cyclic parametrization with scalar amplitude `a>0` and
doublet radius `r>=0`, set

```text
c := 2r/a,
Q := 1/3 + c^2/6.
```

Then

```text
Q = 2/3  <=>  c^2 = 2  <=>  r^2/a^2 = 1/2.
```

This is pure polynomial algebra, verified exactly in the runner and supported
by the retained Koide algebraic rows listed below.

### S2 - Gate 1 as an explicit existing-registry premise

This note does not derive `r^2/a^2=1/2`. It states the conditional consequence
of consuming the already-registered `AC_phi_lambda` bounded premise — carried
by the registered Tier-A target
[`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
per `docs/audit/data/tier_a_admissions.json` — for the
charged-lepton K-reality / determinant-selector input. Under that premise,
S1 gives `Q=2/3` exactly.

The retained boundary rows remain active and are not weakened:

- [`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
- [`KOIDE_Q_DELTA_RESIDUAL_COHOMOLOGY_OBSTRUCTION_NO_GO_NOTE_2026-04-24.md`](KOIDE_Q_DELTA_RESIDUAL_COHOMOLOGY_OBSTRUCTION_NO_GO_NOTE_2026-04-24.md)
- [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)

### S3 - Gate 2 as an explicit existing-registry premise plus retained readouts

This note does not derive `delta=2/9`. It records the conditional readout once
the same `AC_phi_lambda` premise is consumed:

- formal readout: `delta=Q/3`, so at `Q=2/3`, `delta=2/9`;
- topological readout: `delta=L_3(1,2)=(N-1)/N^2|_{N=3}=2/9`, using
  [`AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md`](AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md)
  and
  [`KOIDE_APS_BLOCK_BY_BLOCK_FORCING_NOTE_2026-04-21.md`](KOIDE_APS_BLOCK_BY_BLOCK_FORCING_NOTE_2026-04-21.md).

The radian-bridge no-go boundaries remain active and are not weakened:

- [`KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md`](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md)
- [`KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO_NOTE_2026-04-24.md`](KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO_NOTE_2026-04-24.md)
- [`KOIDE_DELTA_MARKED_RELATIVE_COBORDISM_NO_GO_NOTE_2026-04-24.md`](KOIDE_DELTA_MARKED_RELATIVE_COBORDISM_NO_GO_NOTE_2026-04-24.md)

### S4 - Phase-independent guardrail

The retained Brannen/circulant algebra shows that the `sqrt(2)` coefficient
surface has `Q=2/3` independently of the phase. This is an internal guardrail,
not a derivation of either selector.

Load-bearing support:

- [`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
- [`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
- [`KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)

### S5 - Chain-of-custody anchor

The chain-of-custody note is cited as a source reference for the L1-L10 chain
and the existing `AC_phi_lambda` dependency. It is not modified here and is not
used to apply an audit verdict.

## No-Go Discipline Gate

This gate applies to the bounded/open part of the claim: this note consumes an
existing registry premise and does not prove the two selectors from the current
retained inventory alone.

- **N1 alternative routes:** (1) pure Koide algebra; (2) Frobenius/isotype
  weighting; (3) residual cohomology/zero-section; (4) Z3-equivariant
  anticommuting route; (5) radian-bridge and marked-cobordism routes; (6)
  topological `L_3(1,2)` readout. Routes (2)-(5) are boundary no-gos; route
  (6) supplies the topological value readout but does not derive the selector
  premise by itself.
- **N2 wall independence:** Gate 1 selection, Gate 2 phase/readout, and the
  absolute charged-lepton scale are separate residuals. This note touches only
  the dimensionless two-gate chain under `AC_phi_lambda`; it does not close the
  scale residual.
- **N3 hidden-wall scan:** `AC_phi_lambda`, the `sqrt(2)` amplitude, and the
  absolute scale are explicit dependencies or exclusions, not hidden premises.
- **N4 residual matching:** the no-go rows cited for Gate 1 and Gate 2 match
  the selection/readout residuals they are used to bound. They are not cited as
  positive derivations.
- **N5 rhetoric audit:** "under the existing registry premise" means a
  conditional bounded statement. It does not mean the registry premise is
  derived, promoted, or newly approved by this note.
- **N6 partial-closure scan:** if a retained derivation later retires
  `AC_phi_lambda`, the conditional dependency can be revisited by the audit
  pipeline. This note does not perform that retirement.
- **N7 steelman:** a reviewer could reject this row if the registry entry is
  judged too narrow to cover the umbrella two-gate statement. In that case the
  parent open-gate framing remains intact and no retained row is modified.
- **N8 cross-cycle echo:** the companion delta-only pattern and the
  chain-of-custody note motivate this source row, but neither is treated as an
  audit verdict or as authority to promote status.

## What This Does Not Claim

- It does not derive `r^2/a^2=1/2`, `Q=2/3`, `delta=2/9`, or the `sqrt(2)`
  amplitude from the retained inventory alone.
- It does not derive charged-lepton masses in physical units and does not
  consume PDG values.
- It does not derive the absolute charged-lepton scale.
- It does not make neutrino-sector claims.
- It does not modify or promote the Tier-A registry.
- It does not modify the parent open-gate row or the chain-of-custody note.
- It does not weaken any retained no-go.
- It does not add an axiom or new theory language.
- It does not set, predict, or propose an audit/effective-status outcome.

## Authorities

| Authority | Role |
|---|---|
| [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) | baseline one-qubit operator algebra and `Z^3` spatial substrate |
| [`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md) | human-readable Tier-A registry |
| [`docs/audit/data/tier_a_admissions.json`](audit/data/tier_a_admissions.json) | machine-readable registry for `AC_phi_lambda` |
| [`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md) | chain-of-custody source reference |
| [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md) | registered Tier-A `AC_phi_lambda` carrier consumed as the S2/S3 bounded premise |
| `CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md` (backticked, context only) | parent open-gate row preserved, not consumed, by this companion |
| [`CHARGED_LEPTON_BRANNEN_BAE_DELTA_TIER_A_BOUNDED_THEOREM_NOTE_2026-05-30.md`](CHARGED_LEPTON_BRANNEN_BAE_DELTA_TIER_A_BOUNDED_THEOREM_NOTE_2026-05-30.md) | delta-only companion source row |

## Verification

Run:

```bash
python3 scripts/frontier_charged_lepton_koide_two_gate_tier_a_bounded_verifier.py
```

The runner checks the exact algebra, the registry and authority files, the
Gate-1/Gate-2 no-go boundary portfolios, the phase-independent guardrail at
sample phases, and hostile-review exclusions.

## Sidecar References

Historical physics references for context only: Koide (1981), Brannen (2005),
and Buckingham (1914). No external value is load-bearing here.
