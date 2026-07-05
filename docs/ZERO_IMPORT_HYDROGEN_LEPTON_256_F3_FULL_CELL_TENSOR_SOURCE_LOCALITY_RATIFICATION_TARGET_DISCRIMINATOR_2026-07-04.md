# Zero-Import Hydrogen: Lepton `1/256` F3 Full-Cell Tensor Source-Locality Ratification Target Discriminator

**Date:** 2026-07-04
**Type:** partial discriminator / source-locality target
**Claim type:** conditional full-cell source-locality support
**Status:** support-only. This note does not ratify F3, does not ratify F,
does not derive retained `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_f3_full_cell_tensor_source_locality_ratification_target_discriminator.py`

## Scope

The F-clause source/action assembly discriminator decomposed F into:

| subinput | content |
|---|---|
| F1 | source-coupled local-action convention |
| F2 | charged-lepton sector specificity |
| F3 | full OS0-cell tensor source locality |
| F4 | scalar-multiplier attachment |

This note attacks only F3. The existing full-cell source-carrier support note
already proves the finite conditional:

```text
full OS0-cell linear source over x,y,z,tau qubit slots
  -> A_cell = M_2(C)^tensor4
  -> |C| = 4^4 = 256 matrix-unit coordinates.
```

F3 is the physical source-locality statement that lets the hydrogen lane use
that finite carrier for the charged-lepton scalar source. It is not F1's
source/action insertion convention, not F2's D17 charged-lepton block selector,
and not F4's scalar-multiplier attachment to D17.

## Conditional F3 Target

F3 is supplied if the framework derives or explicitly ratifies the following
source-locality target:

```text
A_x = A_y = A_z = A_tau = M_2(C),
A_cell = A_x tensor A_y tensor A_z tensor A_tau,
C = {0,1,2,3}^4,
O_c = E_{c_x} tensor E_{c_y} tensor E_{c_z} tensor E_{c_tau},
J(j) = sum_{c in C} j_c O_c.
```

The target inputs are:

| input | content |
|---|---|
| OS0 | the four local qubit-slot algebras `x,y,z,tau` are available as OS0 carrier geometry |
| SOURCE | the object is a physical source family, not only regulator bookkeeping |
| FULL_CELL | source locality is tensor-full over all four slots, not slot-additive, diagonal, scalar, or tracial |
| INDEPENDENT | the tensor-product matrix-unit coordinates have independent source controls |
| RATIFICATION | the charged-lepton source-locality target is derived or explicitly ratified for framework use |

All five inputs close the narrow F3 target conditionally:

```text
OS0 + SOURCE + FULL_CELL + INDEPENDENT + RATIFICATION
  -> C = {0,1,2,3}^4 and |C| = 256 is the physical source carrier.
```

Every one-input-removed target fails:

| missing input | witness | result |
|---|---|---|
| no OS0 | spatial-only `M_2(C)^tensor3` gives `4^3 = 64` | no four-slot carrier |
| no SOURCE | `M_2(C)^tensor4` is only regulator geometry | no physical source family |
| no FULL_CELL | slot-additive, diagonal, and scalar/tracial sources give `16`, `4`, and `1` coordinates | no 256-coordinate source locality |
| no INDEPENDENT | constrained or frame-unfixed controls do not provide one source coordinate per tensor matrix unit | no slot-resolved 256-control family |
| no RATIFICATION | the rule remains a candidate source-locality convention | no retained premise for F |

## Finite Checks

The finite carrier arithmetic is exact:

```text
dim_C M_2(C) = 4,
dim_C M_2(C)^tensor4 = 4^4 = 256.
```

The competing locality shapes are discriminating:

| source shape | coordinate count | F3 result |
|---|---:|---|
| full tensor source `A_x tensor A_y tensor A_z tensor A_tau` | `256` | target shape |
| spatial-only tensor source `A_x tensor A_y tensor A_z` | `64` | missing OS0 tick slot |
| slot-additive source `A_x + A_y + A_z + A_tau` | `16` | not full tensor locality |
| diagonal slot-locked source `c_x = c_y = c_z = c_tau` | `4` | not independent controls |
| scalar/tracial source only | `1` | no matrix-unit source carrier |

Thus F3 is a physical source-locality target, not a new finite count.

## What This Moves

| before this note | after this note |
|---|---|
| F3 was named only as "full OS0-cell tensor source locality." | F3 is narrowed to a ratifiable source-locality target: OS0 four-slot geometry, physical source family, full tensor locality, independent matrix-unit controls, and explicit ratification or retained derivation. |
| The full-cell carrier support proved `256` only under a supplied full-cell source. | Its hydrogen-facing use is isolated: it can support F3 only after the physical source-locality target is supplied. |
| F3 could be confused with F2 sector specificity or F4 attachment. | F3 supplies only the `256` source carrier. F2 and F4 remain separate. |

The F3 full-cell tensor source-locality current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
`F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED`. The positive route remains a
retained derivation or owner/audit acceptance of the full-cell tensor
source-locality target.

If F3 is ratified, F still needs F1 source-coupled local action, F2
charged-lepton sector specificity, and F4 scalar-multiplier attachment.

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md` | finite carrier count under supplied full OS0-cell source locality | does not prove physical charged-lepton source locality |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_OS0_M2_TENSOR_GEOMETRY_REPAIR_2026-07-04.md` | OS0 four-slot geometry and `4^4 = 256` bookkeeping | no source-locality theorem |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md` | A1 tensor-lift residual split | does not close the tensor lift |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md` | if slot-resolved source controls are supplied, they select their tensor-product matrix-unit frame | does not derive the slot-resolved source family |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md` | uniformity is invariant after the physical tensor-product matrix-unit source frame is supplied | does not select the frame or source locality |
| `MINIMAL_AXIOMS_2026-06-29.md` | one-site `M_2(C)` possibility algebra | no source/action bridge, selector, weighting, normalization, or mass value |
| approved primitives | OS0 kinetic-form isotropy, scale reference, realized-state discipline | no charged-lepton source-locality theorem, selector, readout bridge, dynamics, mass value, or empirical match |

The primitive registry was checked with the current origin-main methodology.
Registered primitives chain-satisfy their declared dependencies, but they do
not supply F3, F, L, P, R, A3, `m_e`, `alpha(0)`, or hydrogen.

## Current Open PR Alignment

Open PRs were checked on 2026-07-04 after `origin/main` was refreshed and
after `#4992` through `#4995` appeared. The moving review surface does not
close the F3 full-cell tensor source-locality target:

| PR | state at refresh | effect on this F3 lane |
|---|---:|---|
| `#4995` theta retirement-basis re-match | `CLEAN` | theta winding-account governance/rematch context; no charged-lepton full-cell tensor source locality |
| `#4994` record-instrument polar contrast stabilization | `CLEAN` | numerical record/instrument robustness repair; no F3 source-locality theorem |
| `#4993` DELTA0 route inventory sibling-total refresh | `CLEAN` | stale route-inventory total repair; no charged-lepton source-locality theorem |
| `#4992` g_bare two-Ward scope repair | `CLEAN` | keeps `g_bare = 1` conditional on residue normalization; no full-cell source carrier closure |
| `#4991` owner-governed Tier-A retirement | `CLEAN` | governance retirement of live Tier-A admissions; no source-side hydrogen theorem |
| `#4990` Tier-A residual owner decision packet | `CLEAN` | proposal-only governance packet; no F3 closure |
| `#4989` Tier-A residual governance readiness packet | `CLEAN` | governance readiness context; no full-cell source-locality theorem |
| `#4988` theta G2 registration stretch no-go | `CLEAN` | theta physical sector/readout registration remains open; no lepton F3 source-locality theorem |
| `#4987` theta G4 theta-bar assembly no-go | `CLEAN` | theta assembly hygiene; no charged-lepton source-locality theorem |
| `#4986` AC R-eta h-class stretch no-go | `CLEAN` | AC/R-eta h-class pruning; no F3 closure |
| `#4985` AC R-eta h-unit primitive no-go | `CLEAN` | primitive-registry methodology context; no charged-lepton full-cell source family |

Merge-state labels are moving review metadata, not proof inputs here.

## No-Go Discipline Gate

This section prevents overclaiming. The broad retained-F3 claim is **not**
shipped. The narrowed claim is:

```text
If OS0, SOURCE, FULL_CELL, INDEPENDENT, and RATIFICATION are supplied, F3
licenses C = {0,1,2,3}^4 as the physical full-cell tensor source carrier;
every one-input-removed F3 target fails.
```

Verdict tag: broad F3 retention not shipped; narrowed F3 source-locality
ratification-target discriminator support passes.

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full F3 target | Supply OS0 four-slot geometry, physical source family, full tensor locality, independent matrix-unit controls, and ratification. | SUPPORTED CONDITIONALLY. It supplies the `256` source carrier. |
| OS0 geometry-only route | Use `M_2(C)^tensor4` from regulator geometry. | ATTEMPTED. It gives the count but not a physical charged-lepton source family. |
| D17-only route | Use the charged-lepton scalar-singlet block. | ATTEMPTED. It gives the `1/sqrt(2)` block anchor, not the full-cell carrier. |
| slot-additive route | Couple separately to four one-slot algebras. | ATTEMPTED. It gives `16` coordinates, not `256`. |
| diagonal or scalar route | Lock coordinates diagonally or couple only to the scalar/trace channel. | ATTEMPTED. It gives `4` or `1` coordinate, not `256`. |
| source-slot frame route | Use the source-slot frame selector result. | ATTEMPTED. It selects the tensor frame after slot-resolved controls are supplied; it does not derive those controls. |
| approved-primitive shortcut | Appeal to minimal axioms or approved primitives for F3. | RULED OUT AS CLOSURE by registry-limited scope. They do not supply source/action, source locality, selector, or readout. |
| latest open PR shortcut | Treat `#4985` through `#4995` as new F3 science. | ATTEMPTED. They are theta, record/instrument, DELTA0, `g_bare`, AC/R-eta, or governance surfaces; none ratifies the lepton full-cell source family. |
| empirical mass shortcut | Use `m_W/256`, PDG lepton masses, or hydrogen targets to infer F3. | RULED OUT AS ZERO-IMPORT ROUTE. Comparator data is target data, not a source-locality theorem. |

### N2 - Wall-Independence Audit

OS0 and SOURCE do not collapse into full-cell tensor source locality. The
collapsed F3 target is:

| collapsed input | content |
|---|---|
| OS0_GEOMETRY | four `M_2(C)` qubit-slot algebras are available as OS0 carrier geometry |
| PHYSICAL_SOURCE_LOCALITY | the charged-lepton source family is local over those slots |
| FULL_TENSOR_INDEPENDENCE | the source controls range independently over tensor-product matrix units |
| RATIFICATION | the source-locality target is derived or explicitly ratified |

Pairwise audit:

| pair | does one close the other? | conclusion |
|---|---|---|
| OS0_GEOMETRY with PHYSICAL_SOURCE_LOCALITY | no | a regulator carrier does not say the charged-lepton scalar source uses it |
| OS0_GEOMETRY with FULL_TENSOR_INDEPENDENCE | no | four slots do not force independent matrix-unit controls |
| OS0_GEOMETRY with RATIFICATION | no | geometry alone is not physical adoption |
| PHYSICAL_SOURCE_LOCALITY with FULL_TENSOR_INDEPENDENCE | no | source locality may be slot-additive or constrained |
| PHYSICAL_SOURCE_LOCALITY with RATIFICATION | no | a candidate physical reading still needs retained authority |
| FULL_TENSOR_INDEPENDENCE with RATIFICATION | no | a formal tensor basis still needs physical source-locality license |

This note uses the collapsed target and does not inflate the wall count.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `OS0`, `Z^3 x Z_tau`, `M_2(C)^tensor4` | cited geometry/carrier support, not retained F3 |
| `source`, `source family`, `source locality` | explicit F3 target |
| `full-cell`, `tensor`, `matrix-unit` | explicit full-tensor independence target |
| `charged-lepton` | inherited sector context from F2, not supplied by F3 |
| `registered` / `approved primitives` | registry-limited content only |
| `S_l`, `m_e`, `alpha(0)`, `hydrogen` | downstream non-claims |

No source-locality theorem, sector selector, source/action convention, readout
identity, mass input, or atomic result is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| full-cell source-carrier support | `256` carrier under supplied full-cell source locality | finite F3 consequence | yes, conditional |
| OS0 geometry repair | OS0 four-slot geometry and `4^4 = 256` count | OS0_GEOMETRY | yes for geometry, not source locality |
| tensor-lift firewall | A1 carrier attachment residual | F3 target placement | yes |
| source-slot frame selector support | frame selection after slot-resolved controls are supplied | FULL_TENSOR_INDEPENDENCE consequence | boundary only |
| restricted tensor-frame invariance support | uniformity after physical tensor-product source frame is supplied | downstream A2 support | no; review context only |
| F1 ratification target discriminator | source/action insertion convention | F1, not F3 | no; sibling context only |
| F2 source-block selector discriminator | D17 charged-lepton block selector | F2, not F3 | no; sibling context only |
| `#4985` through `#4995` | theta, record/instrument, DELTA0, `g_bare`, AC/R-eta, and governance residuals | F3 source-locality target | no; review context only |

Only matching F3 residuals are counted as support.

### N5 - Rhetoric Audit

The negative phrase used here is narrow: "one-input-removed F3 targets fail."
Tested resolutions are:

| resolution | tested? | result |
|---|---:|---|
| OS0 geometry level | yes | without OS0, spatial-only gives `64` |
| source-family level | yes | without SOURCE, `256` is regulator bookkeeping only |
| locality-shape level | yes | without FULL_CELL, weaker source shapes give `16`, `4`, or `1` |
| coordinate-control level | yes | without INDEPENDENT, no one-coordinate/one-source family is supplied |
| ratification level | yes | without RATIFICATION, F3 remains a candidate target |
| F level | not claimed as closed | F still needs F1, F2, and F4 |
| source-side `S_l` level | not claimed as closed | L, P, R remain separate |
| hydrogen level | not claimed | no statement that hydrogen is impossible or retained |

No broader no-go is shipped.

### N6 - Partial-Closure Path Scan

The legitimate closure path is not "add a new axiom." It is:

1. derive that the charged-lepton scalar source is full-cell tensor-local over
   the OS0 `x,y,z,tau` qubit-slot algebras; or
2. ratify that source-locality target as part of the charged-lepton source/action
   interface and send it through review and audit.

The OS0 geometry repair is a partial-closure path for OS0_GEOMETRY. The
full-cell source-carrier support note is a partial-closure path for the finite
carrier consequence after F3 is supplied. The source-slot frame selector note is
a partial-closure path for frame selection after slot-resolved controls are
supplied. None alone closes retained F3.

The primitive registry was checked. Registered primitives are not walls, but
they also do not supply source/action, source-locality, selectors, weighting,
normalization, readout bridge, dynamics, mass value, or empirical match.

### N7 - Steelman

A hostile reviewer can argue that F3 is already forced: the minimal axioms give
one-site `M_2(C)`, the kinetic-isotropy primitive gives the OS0 four-slot
regulator cell, and a local charged-lepton scalar source should be local over
the whole regulator cell. The full-cell source-carrier support then gives
`256` exactly. That is a serious convention-retirement route. The narrow reply
is that "local over the whole regulator cell" is exactly the physical
source-locality license not yet retained; current primitives deliberately stop
before source/action, selector, and readout content.

### N8 - Cross-Cycle Echo

Similar carrier and source/action walls have been retired by separating a
finite carrier theorem from the physical-license sentence that authorizes its
use. The same mechanism could retire F3: keep OS0/full-cell support as the
finite theorem, then derive or ratify the charged-lepton full-cell tensor
source-locality target. This note therefore ships as F3 ratification-target
support, not as a no-go and not as a retained theorem.

## Non-Claims

- No derivation or ratification of F3.
- No derivation or ratification of F.
- No derivation or ratification of F1, F2, or F4.
- No derivation that `S_l = 1/256` is retained.
- No derivation of the `256.082435...` precision correction.
- No derivation of the Koide/electron branch or physical `m_e`.
- No derivation of `alpha(0)` or hydrogen spectroscopy.
- No use of latest open PRs as proof inputs.
- No new axiom, primitive, or admitted import.
- No audit status change for any cited row.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_f3_full_cell_tensor_source_locality_ratification_target_discriminator.py
```
