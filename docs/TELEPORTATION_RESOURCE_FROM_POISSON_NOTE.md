# Teleportation Resource From Poisson/CHSH: First Audit

**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_teleportation_resource_from_poisson.py`
**Load-bearing helper source:** `scripts/frontier_bell_inequality.py`

Status: bounded offline-resource support. This note records the finite
small-surface theorem that the existing Poisson-driven CHSH lane yields an
encoded two-qubit Bell resource for ordinary quantum state teleportation after
retained-axis logical reduction.

**Source boundary:** This is a bounded finite-resource note, not a physical
deterministic apparatus theorem. The runner certificate covers only the
small-surface (`1D N=8`, `2D 4x4`) offline extraction. The finite algebraic
selection of the last-taste retained axis is routed through the retained-bounded
RALA source
[`TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md`](TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md).
The full native preparation/readout theorem realizing the same retained-axis
carrier as a physical deterministic teleportation apparatus is split off as a
downstream open bridge and is not load-bearing for this row's bounded theorem.

It does not claim matter teleportation, charge transfer, mass transfer, or
faster-than-light transport. The only scoped object is a quantum state
teleportation resource extracted from the two-species ground state used by
`scripts/frontier_bell_inequality.py`.

## 2026-05-28 Source Repair (load-bearing core split from unsupplied bridge)

Earlier source feedback identified the old overbroad boundary:

> *"The runner computes the bounded extraction diagnostics, but the packet does not prove the native preparation/readout theorem or justify selecting the last taste bit as a physical deterministic carrier. The note itself keeps that bridge open"*

with repair: *"missing_bridge_theorem: prove the native preparation/readout and last-taste-bit logical-carrier selection, then rerun the small-surface checks with the Poisson/CHSH machinery source included in the restricted packet."*.

The 2026-06-07 repair splits that target: the finite last-taste logical-carrier
algebra is now sourced through the retained-bounded RALA note, while the native
physical preparation/readout theorem remains open.

Supplying the missing native bridge is substantive new work, out of scope for
this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** The runner's bounded extraction diagnostics on the two small surfaces (1D N=8 and 2D 4x4): traced Bell overlap, negativity, and standard teleportation fidelity under the last-taste-bit logical-qubit identification, confirming a positive first artifact for the Poisson/CHSH cases relative to the null case. The 2026-06-03 repair exposes and checks the imported Poisson/CHSH helper source in the row runner; the 2026-06-07 repair exposes the retained-bounded RALA authority for the finite last-taste logical-operator selection.
- **NON-load-bearing (split off / downstream):** The native preparation/readout theorem realizing the retained-axis last taste bit as a physical deterministic teleportation carrier (distinct from offline ground-state extraction). That is a separate future bridge, not a premise of this bounded offline-resource row.

No new axiom, primitive, import, or approved bridge is introduced. The
runner-verified finite extraction is the load-bearing content; the physical
deterministic apparatus target is not claimed here.

## 2026-06-03 Source-Packet And Carrier-Label Repair

This repair discharges the restricted packet visibility part of the earlier
repair text, without claiming the missing native preparation/readout theorem.
The runner now:

- reads and hashes the load-bearing Poisson/CHSH helper source
  `scripts/frontier_bell_inequality.py`;
- asserts the helper contains the source functions used by this row:
  `build_H1`, `build_H2_tensor`, `build_pair_hop_X`, `build_poisson`,
  `build_sublattice_Z`, `build_cell_taste_operator`,
  `taste_identity_check`, `chsh_horodecki`, and the lattice builders;
- verifies on every default audited surface that the site basis decomposes
  into exactly one last-taste logical bit plus environment labels, each
  environment has one logical `0` and one logical `1`, and the imported
  pair-hop operator is exactly the last-taste logical flip;
- constructs the separate last-taste `Z` operator and checks the logical
  Pauli algebra used by the reduced Bell-resource calculation; and
- reports Bell-label ties in the traced resource, so the null-control traced
  label is no longer confused with the best fixed-environment postselected
  branch label.

On `1D N=8`, sublattice parity equals the last-taste `Z`. On `2D 4x4`,
sublattice parity is the full `xi5` product while the reduced resource uses a
separate last-taste `Z`; the runner prints this distinction rather than
silently treating the full parity as a traced logical readout.

The remaining open bridge is still the operational theorem: a native
preparation/readout and apparatus path that realizes this offline
last-taste-bit carrier as a physical deterministic teleportation resource.

## 2026-06-07 Retained-Axis Carrier Source Repair

The finite logical-carrier part of the earlier blocker no longer needs to be
carried as an unsourced convention. The retained-bounded RALA source
[`TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md`](TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md)
proves the finite retained-axis operator algebra used here:

- the site Hilbert space factorizes into cell/environment labels and a retained
  taste-axis logical bit;
- `Z_axis` and `X_axis` are in the retained-axis operator algebra;
- the axis Bell projectors are environment-blind logical Bell projectors;
- the prior fixed pair-hop `X` is the retained-axis `X` exactly when the
  retained axis is the last taste axis;
- the standard teleportation identity closes inside that finite algebra.

This row's runner now checks that RALA authority is present and retained-bounded
on the audit ledger before printing the last-taste carrier certificate. This
does **not** close the physical preparation/readout theorem, a microscopic
apparatus Hamiltonian, durable endogenous records, or a native detector path.
It only routes the finite logical-operator selection through a retained-bounded
source instead of leaving it as an unregistered convention.

## 2026-06-12 Native Preparation/Readout Split

The finite operator algebra is no longer a blocker for this bounded row: RALA supplies
the retained-axis `Z_axis`, `X_axis`, Bell projectors, and ideal logical
teleportation closure on the finite audited surfaces. The remaining physical
deterministic-resource blocker is operational and downstream.

What this packet can currently say:

- the Poisson/CHSH small-surface ground states, after tracing cells and
  spectator tastes, contain a high-fidelity retained-axis logical Bell
  resource relative to the null case;
- the retained-axis operator convention is finite-algebraic and
  retained-bounded;
- the standard teleportation channel algebra closes for a supplied
  logical resource.

What this bounded row still does not derive, and does not claim:

- a native preparation Hamiltonian or schedule that produces the
  Poisson resource without offline diagonalization;
- a physical detector/readout path for the retained-axis logical bit
  and Bell record;
- endogenous durable records or apparatus dynamics that implement the
  ideal logical operations.

The adjacent preparation/readout probe and operator-consistent end-to-end
artifacts are support for the downstream physical apparatus bridge. They are
not needed to prove the bounded offline-resource theorem in this row.

Source-surface summary: this row is bounded offline retained-axis
Bell-resource support. The physical deterministic-resource theorem remains a
separate open bridge. No new axiom, primitive, approved premise, or status
claim is introduced here.

## 2026-06-15 Native Apparatus Candidate Bridge

The 2026-06-15 source repair narrows the operational blocker without claiming
retained status:

- [`TELEPORTATION_MICROSCOPIC_CLOSURE_NOTE.md`](TELEPORTATION_MICROSCOPIC_CLOSURE_NOTE.md)
  supplies a bounded candidate for the retained-axis Bell-record transducer:
  native `Cl(3)/Z^3` stabilizers close, stabilizer-controlled Hamiltonian
  terms commute, finite-time evolution writes the Bell codewords, a
  pointer-plus-bath overlap bound suppresses record coherences exponentially,
  and the native taste-apparatus generator class commutes with the conserved
  support ledgers.
- [`TELEPORTATION_APPARATUS_DYNAMICS_CLOSURE_NOTE.md`](TELEPORTATION_APPARATUS_DYNAMICS_CLOSURE_NOTE.md)
  supplies a bounded coupled-dynamics candidate: a local retarded field front
  gives the eikonal record carrier, a finite-strength Bell transducer replaces
  a projective measurement placeholder, a finite spin bath decoheres the
  record, Bob's pre-delivery state is input-independent, and the checked
  apparatus ledger is branch independent.

Together these packets partially discharge the downstream physical
preparation/readout and apparatus bridge on its apparatus/readout side. They do
**not** change the bounded theorem proved by this row: the row's load-bearing
claim is the offline finite retained-axis Bell-resource extraction. The
physical deterministic-resource theorem is still separate and open.

## 2026-06-16 Finite Preparation-Path Support

The finite-resource side now has one additional bounded-support artifact:
[`TELEPORTATION_FINITE_GAPPED_PREPARATION_PATH_SUPPORT_NOTE_2026-06-16.md`](TELEPORTATION_FINITE_GAPPED_PREPARATION_PATH_SUPPORT_NOTE_2026-06-16.md)
and runner
`scripts/teleportation_finite_gapped_preparation_path_support_2026_06_16.py`.

That support runner checks, on the same `1D N=8` and `2D 4x4` audited
surfaces, that the Poisson/CHSH two-particle Hamiltonian is an exactly affine
finite path

```text
H(G) = H(0) + G W,  0 <= G <= 1000,
```

and that the sampled path grid has a positive finite ground-state gap while
the `G=1000` endpoint remains the high-fidelity traced retained-axis Bell
resource. This narrows the "offline diagonalization only" part of the blocker:
the resource endpoint is not just an isolated diagonalization, but lies at the
end of an explicit finite Hamiltonian path with sampled positive gap evidence.

This does not close physical detector/readout, native apparatus dynamics,
durable record formation, an analytic all-`G` gap lower bound, or any
continuum/infinite-volume preparation theorem. The new artifact is bounded
preparation-path support for the downstream physical bridge only; it
introduces no new axiom, primitive, approved premise, or status claim.

## Script

New runner:

```bash
python3 scripts/frontier_teleportation_resource_from_poisson.py
```

The runner imports the existing Poisson/CHSH machinery, builds the small
ground-state cases, and then extracts a candidate resource as follows:

1. Use the Kogut-Susskind cell/taste factorization already used in the CHSH
   lane.
2. Keep the last taste bit of each species as the logical qubit, using the
   retained-axis operator algebra source for the finite logical-operator
   selection.
3. Trace over cells and spectator taste bits to get a deterministic two-qubit
   logical resource.
4. Separately scan fixed-environment postselected branches as diagnostics only.
5. Measure Bell overlap, two-qubit CHSH, purity, negativity, and standard
   teleportation fidelity for random input states.

The script also checks the Bell teleportation convention against an ideal
`Phi+` resource before running the Poisson cases.

## Default Run Results

Command:

```bash
python3 scripts/frontier_teleportation_resource_from_poisson.py
```

Protocol sanity:

- Ideal `Phi+` resource mean fidelity: `0.9999999999999996`
- Ideal `Phi+` resource minimum fidelity: `0.9999999999999991`
- Maximum output trace error: `5.551e-16`

| case | full CHSH | traced Bell overlap | traced CHSH | negativity | standard teleportation fidelity | deterministic high-fidelity resource |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| `1d_null`, `G=0` | `2.000000` | `0.500000` (`Psi+`; tied with `Phi+`) | `2.000000` | `0.000000` | mean `0.669817`, min `0.500038`, max `0.987949` | no |
| `1d_poisson_chsh`, `G=1000` | `2.822668` | `0.997963` (`Phi+`) | `2.822668` | `0.497963` | mean `0.998621`, min `0.997964`, max `0.999470` | yes |
| `2d_poisson_chsh`, `G=1000` | `2.668376` | `0.970283` (`Phi+`) | `2.745662` | `0.470283` | mean `0.979360`, min `0.970287`, max `0.999810` | yes |

Postselected diagnostic branches:

| case | best branch Bell overlap | probability | branch CHSH | branch negativity |
| --- | ---: | ---: | ---: | ---: |
| `1d_null` | `0.500000` (`Psi+`) | `6.250000e-02` | `2.000000` | `0.000000` |
| `1d_poisson_chsh` | `0.998981` (`Phi+`) | `2.497454e-01` | `2.825546` | `0.498981` |
| `2d_poisson_chsh` | `0.999428` (`Psi+`) | `5.854540e-08` | `2.826809` | `0.499428` |

## Interpretation

The `G=0` null case does not produce an entangled Bell resource under this
extraction: the best Bell overlap is `0.500000` and negativity is zero.

The two audited Poisson/CHSH cases are positive on the deterministic traced
logical resource: both exceed the script's `0.90` Bell-overlap threshold and
both give high standard teleportation fidelity in the ideal Bell-measurement
protocol. This is stronger than merely observing a full-state CHSH violation.

The postselected branches are not promoted as resources here. They are useful
diagnostics, but a postselection scan is not a deterministic resource
preparation protocol.

## Limitation Status

The limitation has moved, but it is not closed.

Previous limitation: no Poisson-resource derivation artifact for teleportation.

Current status: bounded small-surface support. The existing Poisson/CHSH
ground-state machinery yields a high-fidelity encoded two-qubit resource on the
`1D N=8` and `2D 4x4` cases after tracing to the last taste bit per species.

Still open before promotion:

- Harden beyond the two small default surfaces.
- Check mass, coupling, dimension, boundary, and degeneracy sensitivity.
- Complete the native preparation/resource-production story for the
  retained-axis logical resource, not only an offline ground-state extraction.
  The 2026-06-15 microscopic/apparatus candidates narrow the readout/apparatus
  side but do not close resource preparation or uniqueness.
- Separate deterministic traced extraction from diagnostic postselection.
- Keep the claim restricted to quantum state teleportation.

## Scope Repair Boundary (2026-06-17)

This row is now intentionally framed as a bounded theorem for the offline
finite retained-axis resource, not as a physical deterministic-resource
theorem. The small-surface Poisson/CHSH calculation verifies that the chosen
offline last-taste-bit reduction produces high Bell overlap, high CHSH,
positive negativity, and high ideal state-teleportation fidelity on the stated
`1D N=8` and `2D 4x4` cases. That does not by itself prove native
preparation/readout, operational carrier selection, or a physical deterministic
apparatus.

The source claim is therefore narrower than promotion:

- The original runner remains the numerical source for the small-surface
  certificate.
- The Poisson/CHSH source chain is visible in the runner packet: the runner
  links, hashes, and checks `scripts/frontier_bell_inequality.py`.
- The current framework baseline is [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md):
  Lattice, Quantum, and Record. No new axiom or primitive is introduced here.
- This note asserts the finite retained-axis logical-operator source and the
  bounded offline resource extraction, not that the last taste bit has been
  derived as a native physical apparatus carrier.
- The missing native preparation/readout theorem remains the next positive
  science target for a separate physical-resource row.

Source-boundary checker:

```bash
PYTHONPATH=scripts python3 scripts/frontier_teleportation_poisson_resource_scope_repair.py
```

## Citation Chain And Repair Path (2026-05-10)

The runner's reduced-resource diagnostics support the bounded small-surface
positive theorem, and the retained-axis operator algebra source closes the
finite last-taste logical-operator selection. The packet does not claim the
native preparation/readout theorem realizing that retained-axis carrier as a
deterministic physical teleportation apparatus.
The source chain on this row currently stands as follows.

| Source | Note / file | Role | Conditional on |
|---|---|---|---|
| Poisson/CHSH small-surface ground states | `scripts/frontier_bell_inequality.py` (imported, linked, hashed, and source-checked by this runner) | source script | visible bounded helper source; not a native preparation/readout theorem |
| This row's runner | `scripts/frontier_teleportation_resource_from_poisson.py` | quoted bounded certificate | bounded extraction on `1D N=8` and `2D 4x4` only |
| Retained-axis logical carrier algebra | [`TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md`](TELEPORTATION_RETAINED_AXIS_OPERATOR_ALGEBRA_CLOSURE_NOTE.md) | finite operator-algebra source | retained-bounded RALA source for `Z_axis`, `X_axis`, axis Bell projectors, and last-axis `X_fixed`; not a physical apparatus theorem |
| Adjacent Poisson resource sweep | [`TELEPORTATION_POISSON_RESOURCE_SWEEP_NOTE.md`](TELEPORTATION_POISSON_RESOURCE_SWEEP_NOTE.md) | adjacent diagnostic | not a substitute for the missing native-carrier bridge theorem |
| Adjacent resource fidelity note | [`TELEPORTATION_RESOURCE_FIDELITY_NOTE.md`](TELEPORTATION_RESOURCE_FIDELITY_NOTE.md) | bounded fidelity protocol | not a physical apparatus theorem |
| Adjacent measurement-record / apparatus-dynamics-closure | [`TELEPORTATION_MEASUREMENT_RECORD_NOTE.md`](TELEPORTATION_MEASUREMENT_RECORD_NOTE.md), [`TELEPORTATION_APPARATUS_DYNAMICS_CLOSURE_NOTE.md`](TELEPORTATION_APPARATUS_DYNAMICS_CLOSURE_NOTE.md) | downstream apparatus support | not load-bearing for the bounded offline-resource theorem |
| Current framework baseline | [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md) | Lattice / Quantum / Record baseline | no new axiom is introduced; physical apparatus remains separate |

The remaining physical-resource path is to prove the native preparation/readout
theorem for this retained-axis last-taste carrier. Until that lands, the
small-surface theorem here is bounded offline resource support, not a physical
deterministic apparatus derivation.

## 2026-06-17 Bounded Offline Resource Scope Split

The current row is bounded offline retained-axis Bell-resource support. Its
load-bearing proof consists of:

- visible Poisson/CHSH helper-source construction of the small finite ground
  states;
- retained-axis logical-carrier algebra for the last taste bit;
- deterministic traced logical two-qubit resource diagnostics on `1D N=8` and
  `2D 4x4`;
- standard ideal Bell-protocol fidelity checks on that supplied logical
  resource; and
- null/postselection controls that keep the claim finite and deterministic at
  the traced-resource level.

Physical deterministic teleportation apparatus, native resource production,
detector hardware, durable record formation, and continuum/infinite-volume
preparation are downstream open bridges. They are not premises for this
bounded row and are not claimed here.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [teleportation_operator_consistent_end_to_end_note](TELEPORTATION_OPERATOR_CONSISTENT_END_TO_END_NOTE.md)

## 2026-06-15 audit-unlock residual certificate

This row is re-opened as finite-carrier resource support only. The useful
closed content is the explicit finite Hamiltonian diagonalization and logical
two-qubit Bell/resource diagnostic computed by the runner and helpers.

The live blocker is not the finite diagonalization. A later theorem must
derive native preparation and readout apparatus for the logical qubits, plus
the framework-native transport from the Poisson-like source to an operational
teleportation resource. Until then this row should not be read as an
apparatus-level teleportation theorem. No new apparatus axiom, observed
protocol, or audit status is introduced by this repair.
