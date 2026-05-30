# Teleportation Resource From Poisson/CHSH: First Audit

**Type:** open_gate
**Claim type:** open_gate
**Primary runner:** `scripts/frontier_teleportation_resource_from_poisson.py`

Status: planning / first artifact. This note records a narrow audit of whether
the existing Poisson-driven CHSH lane already yields an encoded two-qubit Bell
resource for ordinary quantum state teleportation.

**Source boundary:** This is a **planning / first-artifact** note. The
limitation has moved, but is not closed: the runner certificate covers only the
small-surface (`1D N=8`, `2D 4x4`) bounded extraction. The native
preparation/readout theorem selecting the last taste bit as a physical
deterministic carrier remains open.

It does not claim matter teleportation, charge transfer, mass transfer, or
faster-than-light transport. The only audited object is a quantum state
teleportation resource extracted from the two-species ground state used by
`scripts/frontier_bell_inequality.py`.

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The runner computes the bounded extraction diagnostics, but the packet does not prove the native preparation/readout theorem or justify selecting the last taste bit as a physical deterministic carrier. The note itself keeps that bridge open"*

with repair: *"missing_bridge_theorem: prove the native preparation/readout and last-taste-bit logical-carrier selection, then rerun the small-surface checks with the Poisson/CHSH machinery source included in the restricted packet."*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** The runner's bounded extraction diagnostics on the two small surfaces (1D N=8 and 2D 4x4): traced Bell overlap, negativity, and standard teleportation fidelity under the last-taste-bit logical-qubit identification, confirming a positive first artifact for the Poisson/CHSH cases relative to the null case.
- **NON-load-bearing (split off / admitted):** The native preparation/readout theorem selecting the last taste bit as a physical deterministic teleportation carrier (distinct from offline ground-state extraction), and the packet-completeness step including the Poisson/CHSH machinery source in the restricted packet; both are missing bridge theorems recorded here as admitted, not-derived inputs.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

## Script

New runner:

```bash
python3 scripts/frontier_teleportation_resource_from_poisson.py
```

The runner imports the existing Poisson/CHSH machinery, builds the small
ground-state cases, and then extracts a candidate resource as follows:

1. Use the Kogut-Susskind cell/taste factorization already used in the CHSH
   lane.
2. Keep the last taste bit of each species as the logical qubit.
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
| `1d_null`, `G=0` | `2.000000` | `0.500000` (`Psi+`) | `2.000000` | `0.000000` | mean `0.669817`, min `0.500038`, max `0.987949` | no |
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

Current status: small-surface positive first artifact. The existing Poisson/CHSH
ground-state machinery can yield a high-fidelity encoded two-qubit resource on
the audited `1D N=8` and `2D 4x4` cases after tracing to the last taste bit per
species.

Still open before promotion:

- Harden beyond the two small default surfaces.
- Check mass, coupling, dimension, boundary, and degeneracy sensitivity.
- Add a native preparation/readout story for the logical resource, not only an
  offline ground-state extraction.
- Separate deterministic traced extraction from diagnostic postselection.
- Keep the claim restricted to quantum state teleportation.

## Scope Repair Boundary (2026-05-27)

This row is now intentionally framed as an `open_gate`, not as a
deterministic-resource theorem. The small-surface Poisson/CHSH calculation is
still useful: it verifies that the chosen offline last-taste-bit reduction
produces high Bell overlap, high CHSH, positive negativity, and high ideal
state-teleportation fidelity on the stated `1D N=8` and `2D 4x4` cases. That
does not by itself prove native preparation/readout, operational carrier
selection, or a physical deterministic resource.

The source claim is therefore narrower than promotion:

- The original runner remains the numerical source for the small-surface
  certificate.
- The Poisson/CHSH source chain must be visible in the restricted packet.
- The current A1+A2 premise is [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md);
  no new axiom is introduced here.
- No sentence in this note asserts that the last taste bit has been derived as
  a native physical carrier.
- The missing native preparation/readout theorem remains the next positive
  science target if this open-gate boundary passes audit.

Source-boundary checker:

```bash
PYTHONPATH=scripts python3 scripts/frontier_teleportation_poisson_resource_scope_repair.py
```

## Citation Chain And Repair Path (2026-05-10)

The runner's reduced-resource diagnostics support the small-surface positive
observation, but the packet does not close the native preparation/readout
theorem selecting the last taste bit as a deterministic teleportation resource.
The source chain on this row currently stands as follows.

| Source | Note / file | Role | Conditional on |
|---|---|---|---|
| Poisson/CHSH small-surface ground states | `scripts/frontier_bell_inequality.py` (imported by this runner) | source script | packet inclusion of the Poisson/CHSH machinery source |
| This row's runner | `scripts/frontier_teleportation_resource_from_poisson.py` | quoted bounded certificate | bounded extraction on `1D N=8` and `2D 4x4` only |
| Adjacent Poisson resource sweep | [`TELEPORTATION_POISSON_RESOURCE_SWEEP_NOTE.md`](TELEPORTATION_POISSON_RESOURCE_SWEEP_NOTE.md) | adjacent diagnostic | not a substitute for the missing native-carrier bridge theorem |
| Adjacent resource fidelity note | [`TELEPORTATION_RESOURCE_FIDELITY_NOTE.md`](TELEPORTATION_RESOURCE_FIDELITY_NOTE.md) | bounded fidelity protocol | not a derivation of last-taste-bit selection |
| Adjacent measurement-record / apparatus-dynamics-closure | [`TELEPORTATION_MEASUREMENT_RECORD_NOTE.md`](TELEPORTATION_MEASUREMENT_RECORD_NOTE.md), [`TELEPORTATION_APPARATUS_DYNAMICS_CLOSURE_NOTE.md`](TELEPORTATION_APPARATUS_DYNAMICS_CLOSURE_NOTE.md) | adjacent bounded results | do not select the last taste bit as native carrier |
| Current framework axiom premise | [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) | A1+A2 premise | the native preparation/readout theorem has not yet been derived from A1+A2 |

The repair path is to prove the native preparation/readout and
last-taste-bit logical-carrier selection, then rerun the small-surface checks
with the Poisson/CHSH machinery source included in the restricted packet. Until
both land, the small-surface positive numbers in the table are bounded
diagnostics, not a deterministic resource derivation.
