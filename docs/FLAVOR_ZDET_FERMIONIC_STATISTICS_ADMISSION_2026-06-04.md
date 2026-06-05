# Flavor Z=det fermionic-statistics admission locator

**Date:** 2026-06-04
**Claim type:** open_gate.
**Runner:** `scripts/flavor_zdet_fermionic_statistics_admission_2026_06_04.py`.

This note sets no claim grade, edits no existing row, and does not ask any
consumer to treat an axiom or primitive as a grade source. Lattice, Quantum,
Record, and approved primitives may chain-satisfy premise edges; they do not by
themselves make a downstream consumer bounded or grade-complete.

## Context

The log-det generator

`W = log |det(D + J)|`

separates into three inputs:

1. additive record composition;
2. determinant/log character mathematics;
3. the determinant-valued matter amplitude `Z = det(D + J)`.

The Record axiom supplies the first item as baseline framework structure, not
as a consumer grade source. This note only analyzes the third item: why the
matter amplitude is determinant-valued rather than built from an ordinary
commuting cross-site carrier.

## Result

Given Grassmann/CAR matter variables, the finite Berezin Gaussian is the
determinant. That is the realization side of the gate. It does not derive the
choice of Grassmann/CAR variables.

The one-qubit site carrier on an ordinary tensor product has commuting
cross-site ladder operators. A Jordan-Wigner dressing changes generators and
produces CAR, but the dressing is an additional representation choice unless a
separate principle selects it.

Per-site dimension two also does not select the fermionic frame. The hard-core
boson has the same local nilpotency and the same two-state site carrier, while
keeping ordinary commuting cross-site ladders. Dimension excludes the free
bosonic tower; it does not decide fermion versus hard-core boson.

The determinant-valued amplitude therefore localizes to one candidate
owner-approved admission:

> **FS:** matter record variables in determinant-amplitude rows are represented
> by Grassmann/CAR generators across lattice sites, rather than by ordinary
> commuting hard-core-boson generators.

FS is not introduced here as a new axiom. It is a candidate Tier-A admission
statement for owner approval and later independent review. If approved, it
would supply the determinant-amplitude input for the log-det cluster; this file
does not promote those consumers or rewrite their dependency state.

## Scope

FS addresses the spatial cross-site statistics needed for `Z = det(D + J)`.
It does not close the Koide chirality gate. The Koide operator
`Gamma_chi = (2/3)J - I` acts on the internal generation factor; the runner
verifies that it is circulant and commutes with every tested C3-equivariant
mass operator. The spatial CAR choice and the internal generation grading share
a broad fermionic-frame theme, but they are different atoms.

The relevant existing comparison notes are:

- `SPIN_STATISTICS_BEREZIN_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10.md`:
  determinant realization once Grassmann variables are supplied;
- `STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`:
  local dimension excludes the free bosonic tower;
- `GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md`:
  hard-core-boson versus fermion remains the statistics fork;
- `KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`:
  internal generation chirality is a separate residual.

These are comparison and dependency-context anchors. Their existing labels do
not serve as the source of this note's grade.

## No-Go discipline gate

This section gates the narrow negative statement: Lattice + Quantum + Record do
not by themselves force FS.

### N1 - Alternative route enumeration

| Route | What it attempts | Result |
| --- | --- | --- |
| On-site Clifford route | Use on-site gamma anticommutation to force cross-site CAR. | Fails for the narrow claim: on-site operator relations are not cross-site statistics; the runner checks the ordinary two-site tensor product. |
| Local-dimension route | Use `dim H_x = 2` to force Grassmann matter. | Fails for the narrow claim: a hard-core boson has the same two-state site carrier and nilpotency. |
| Jordan-Wigner route | Build CAR by dressing ordinary ladders with a string. | Succeeds as a realization, not as a derivation; it adds an ordering/generator choice. |
| Determinant-character route | Use multiplicativity plus logarithm to select `det`. | Conditional only; it works after the determinant amplitude is supplied. |
| Koide-transport route | Identify spatial CAR with the generation chirality gate. | Fails for the claimed transport: `Gamma_chi` lives on the internal generation factor and commutes with the tested C3-equivariant mass operators. |
| Continuum spin-statistics route | Add dynamics, locality, and positivity in a continuum limit to force fermions. | Not tested here and not part of the three baseline axioms; it remains a possible future adoption or derivation path. |

### N2 - Wall independence

The collapsed wall set for the log-det determinant amplitude is one admission:
FS. The Koide generation-chirality residual is separate and is not counted as a
second wall for this log-det claim.

### N3 - Hidden-wall scan

The word "ordinary" names the explicit tensor-product carrier tested by the
runner. The note does not claim that every possible extension of the framework
must use that carrier. The word "standard" is not load-bearing and is avoided
in the claim statement. Existing comparison notes are cited for context and
mathematical contrast, not as grade sources.

### N4 - Residual matching

The Berezin determinant identity matches only the realization residual: once
Grassmann variables are supplied, the Gaussian gives `det`. The dimension
bridge matches only the free-boson exclusion residual and is not cited as a
proof of FS. The Koide comparison matches only the internal-generation
chirality residual and is kept separate from the spatial determinant-amplitude
residual.

### N5 - Rhetoric audit

The negative phrase is restricted to "not forced by Lattice + Quantum +
Record." It is checked at the on-site, two-site, and three-generation toy
levels represented in the runner. No continuum, interacting QFT, or OS
reconstruction theorem is claimed.

### N6 - Partial-closure path scan

FS can be adopted as an owner-approved Tier-A admission without adding a fourth
baseline axiom. If later work derives FS from an approved continuum or
spin-statistics package, that would be an import-retirement path, not a silent
retroactive promotion. Approved axioms and primitives chain-satisfy dependency
edges but remain non-grade sources for consumers.

### N7 - Steelman

A hostile reviewer can fairly argue that the note only tests finite
operator-algebra carriers, while a genuine spin-statistics theorem could force
CAR after adding continuum dynamics, locality, and positivity. That steelman is
accepted: this note is not a universal physics no-go. It is only a baseline
framework localization of the missing admission.

### N8 - Cross-cycle echo

Prior flavor and graph-braid notes already isolate the hard-core-boson versus
fermion fork. This note uses the same fork to localize the determinant-amplitude
gate and narrows the earlier "same admission as Koide" framing. Owner approval
of FS would apply to the log-det determinant amplitude; it would not by itself
settle the internal generation-chirality residual.

**Gate result:** pass for the narrow statement only.
