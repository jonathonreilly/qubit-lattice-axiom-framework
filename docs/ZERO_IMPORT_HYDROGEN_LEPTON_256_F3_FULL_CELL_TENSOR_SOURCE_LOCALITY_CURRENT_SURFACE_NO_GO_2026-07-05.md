# Zero-Import Hydrogen: Lepton `1/256` F3 Full-Cell Tensor Source-Locality Current-Surface No-Go

**Date:** 2026-07-05
**Type:** current-surface no-go / import-retirement target
**Status:** support-only. This note does not ratify F3, does not ratify F,
does not derive retained `S_l = 1/256`, does not derive `m_e`, does not derive
`alpha(0)`, and does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_f3_full_cell_tensor_source_locality_current_surface_no_go.py`

## Scope

The F-clause handoff needs the third source/action subinput:

```text
F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED.
```

The F3 full-cell tensor source-locality target gives the positive route:

```text
OS0 + SOURCE + FULL_CELL + INDEPENDENT + RATIFICATION
  -> C = {0,1,2,3}^4 and |C| = 256 is the physical source carrier.
```

Current Lane 6 surfaces supply meaningful support: OS0 four-slot geometry,
full-cell source-carrier arithmetic, the tensor-lift firewall, source-slot
frame support, restricted tensor-frame invariance support, and the F3 target
discriminator. They do not supply retained F3. The narrow result is not "F3
cannot be retained." The narrow result is that current retained, primitive,
and open-PR surfaces do not supply
`F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED`.

## F3 Contract

A future retained F3 handoff needs the source-locality inputs plus the normal
review controls:

```text
OS0_GEOMETRY
PHYSICAL_SOURCE_FAMILY
FULL_CELL_TENSOR_LOCALITY
INDEPENDENT_MATRIX_UNIT_CONTROLS
NO_NEW_PRIMITIVE_OR_AXIOM
NO_EMPIRICAL_COMPARATOR_INPUT
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

If accepted, the conditional consequence would be:

```text
F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED
A_cell = M_2(C)^tensor4
C = {0,1,2,3}^4
|C| = 4^4 = 256
J(j) = sum_{c in C} j_c O_c.
```

That consequence is not supplied here. The current missing inputs include:

```text
PHYSICAL_SOURCE_FAMILY
FULL_CELL_TENSOR_LOCALITY
INDEPENDENT_MATRIX_UNIT_CONTROLS
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

F3 supplies only the physical full-cell tensor source-locality carrier. It
does not supply the F1 source/action insertion convention, the F2 charged-
lepton D17 source-block selector, F4 scalar-multiplier attachment,
source-strength normalization, or the `S_l` readout identity.

## Finite Target Arithmetic

The retained F3 target would license the full OS0-cell tensor carrier as the
physical charged-lepton source family:

```text
dim_C M_2(C) = 4
dim_C M_2(C)^tensor4 = 4^4 = 256.
```

The one-input-removed witnesses remain load-bearing guards:

```text
no OS0: spatial-only M_2(C)^tensor3 gives 4^3 = 64
no SOURCE: M_2(C)^tensor4 is only regulator geometry
no FULL_CELL: slot-additive, diagonal, and scalar carriers have counts 16, 4, and 1
no INDEPENDENT: constrained controls do not give one source per tensor matrix unit
no RATIFICATION: the source-locality rule remains a candidate convention
```

These witnesses show why exact `256` arithmetic can be positive support
without already being retained F3.

## Current-Surface Audit

| surface | supplies | does not supply |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md` | F3 target: OS0 geometry, physical source family, full tensor locality, independent controls, ratification | current retained F3 |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md` | finite `4^4 = 256` carrier under supplied full-cell source locality | proof that the charged-lepton scalar source has that physical full-cell source locality |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_OS0_M2_TENSOR_GEOMETRY_REPAIR_2026-07-04.md` | OS0 four-slot geometry and `M_2(C)^tensor4` bookkeeping | source-locality theorem |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md` | A1 tensor-lift residual split and carrier-attachment firewall | source-locality closure |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md` | frame selection after slot-resolved source controls are supplied | derivation of the slot-resolved source family |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md` | restricted invariance after the physical tensor-product matrix-unit source frame is supplied | source-frame selection or source-locality license |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md` | sibling F1 current-surface non-supply boundary | full-cell tensor source-locality theorem |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md` | sibling F2 current-surface non-supply boundary | full-cell tensor source-locality theorem |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md` | sibling F4 scalar attachment target | full-cell tensor source-locality theorem |
| approved primitives | minimal axioms, scale reference, kinetic-form isotropy, realized-state evaluation discipline | physical source family, source/action bridge, full-cell source-locality theorem, independent matrix-unit source controls, `S_l`, mass, or empirical match |

The primitive registry was checked with the current origin-main methodology.
No registered primitive supplies `full_cell_source_locality_primitive`,
`source_locality_primitive`, `physical_source_family_primitive`,
`independent_matrix_unit_controls_primitive`,
`f3_full_cell_tensor_source_locality_primitive`, `f_clause_primitive`,
`source_probe_interface_primitive`, or `electron_mass_primitive`.

## Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC. The newest rows are clean and green,
but they do not close the F3 handoff:

| PR | state at refresh | F3 effect |
|---|---:|---|
| `#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS` | theta gauge-side work; no full-cell tensor source-locality theorem |
| `#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS` | adjacent chirality science; no F3 source-locality ratification |
| `#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS` | runner stabilization; no charged-lepton full-cell source family |
| `#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS` | diagnostic repair; no F3 clause |
| `#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS` | bounded S3 support context; no full-cell source-locality theorem |
| `#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS` | quark context; no charged-lepton source family |
| `#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS` | Koide/electron route support, not F3 source-locality closure |
| `#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS` | static-source hygiene; no charged-lepton F3 clause |
| `#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS` | governance/status progress, not an F3 theorem |

Merge-state labels are moving review metadata, not proof inputs.

## What This Moves

| before this note | after this note |
|---|---|
| F3 had a ratification target discriminator but no dedicated current-surface non-supply boundary | the current retained, primitive, and open-PR gap for `F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED` is explicit |
| F could spend the `4^4 = 256` carrier support as if it were already physical source locality | F now points to the exact upstream source-locality wall |
| exact-source closure could count F without tracking the third subinput | the full-cell tensor source-locality route is separated from F1, F2, F4, and L/P/R |

## No-Go Discipline Gate

This section prevents overclaiming. The broad F3 no-go is not shipped. The
narrowed claim is:

```text
the current retained, primitive, and open-PR surfaces do not supply
F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full F3 source-locality contract | Accept OS0 geometry, a physical source family, full-cell tensor locality, independent matrix-unit controls, no-new-primitive/no-comparator controls, owner ratification, and audit acceptance. | OPEN POSITIVE ROUTE. This would close F3, but the contract is not accepted here. |
| OS0 geometry-only route | Use `M_2(C)^tensor4` from the OS0 regulator cell. | ATTEMPTED. It gives the `256` count, but not a physical charged-lepton source family. |
| full-cell carrier-only route | Use the full-cell source-carrier support theorem directly. | ATTEMPTED. It is conditional on supplied full-cell source locality; that condition is F3. |
| spatial-only route | Use only the three spatial `M_2(C)` slots. | ATTEMPTED. It gives `4^3 = 64`, not `256`. |
| slot-additive, diagonal, or scalar route | Couple to weaker locality shapes instead of the full tensor carrier. | ATTEMPTED. They give `16`, `4`, or `1` coordinates, not `256` independent source controls. |
| source-slot frame route | Use the source-slot frame selector result. | ATTEMPTED. It selects a tensor frame after slot-resolved controls are supplied; it does not derive those controls. |
| F1/F2 sibling shortcut | Treat source/action insertion or D17 source-block selection as enough for F3. | ATTEMPTED. F1 and F2 are separate walls and neither supplies full-cell tensor source locality. |
| primitive shortcut | Treat approved primitives as supplying F3. | RULED OUT BY CURRENT METHODOLOGY. The registry supplies no full-cell source-locality primitive. |
| open-PR shortcut | Treat current green PRs, especially `#5013`, `#5009`, `#5007`, or `#5006`, as F3 closure. | ATTEMPTED. They supply theta, S3, Koide route, and static-source context, not F3 ratification. |
| empirical route | Use observed charged-lepton masses, `m_W/256`, or hydrogen spectroscopy to accept F3. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is target data, not a source-locality theorem. |

### N2 - Wall-Independence Audit

The collapsed F3 current-surface wall set is:

```text
OS0_GEOMETRY + PHYSICAL_SOURCE_FAMILY + FULL_CELL_TENSOR_LOCALITY
  + INDEPENDENT_MATRIX_UNIT_CONTROLS + NO_NEW_PRIMITIVE_OR_AXIOM
  + NO_EMPIRICAL_COMPARATOR_INPUT + OWNER_RATIFICATION
  + AUDIT_ACCEPTANCE.
```

| pair | closes automatically? | conclusion |
|---|---|---|
| OS0_GEOMETRY <-> PHYSICAL_SOURCE_FAMILY | no | a regulator carrier does not say the charged-lepton scalar source uses it |
| PHYSICAL_SOURCE_FAMILY <-> FULL_CELL_TENSOR_LOCALITY | no | a physical source may be slot-additive, diagonal, scalar, or otherwise constrained |
| FULL_CELL_TENSOR_LOCALITY <-> INDEPENDENT_MATRIX_UNIT_CONTROLS | no | full-cell language does not by itself give one independent control per tensor matrix unit |
| INDEPENDENT_MATRIX_UNIT_CONTROLS <-> OWNER_RATIFICATION | no | a formal control family still needs decision authority |
| NO_NEW_PRIMITIVE_OR_AXIOM <-> OWNER_RATIFICATION | no | avoiding primitive status is not owner acceptance |
| NO_EMPIRICAL_COMPARATOR_INPUT <-> AUDIT_ACCEPTANCE | no | excluding comparator data does not imply audit acceptance |
| OWNER_RATIFICATION <-> AUDIT_ACCEPTANCE | no | owner decision and audit acceptance are separate controls |

F1, F2, F4, L, P, R, A3, Koide/electron readout, and `alpha(0)` are downstream
or sibling walls, not F3 walls.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `OS0`, `Z^3 x Z_tau`, `M_2(C)^tensor4` | cited geometry/carrier support, not retained F3 |
| `source`, `source family`, `source locality` | explicit F3 target |
| `full-cell`, `tensor`, `matrix-unit controls` | explicit full-tensor independence target |
| `charged-lepton` | inherited sector context from F2, not supplied by F3 |
| `registered` / `primitive` | registry checked; no shortcut exists |
| `S_l`, `m_e`, `alpha(0)`, `hydrogen` | downstream non-claims |

No physical source family, source-locality theorem, sector selector,
source/action rule, readout identity, mass input, or atomic result is hidden as
background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| F3 target discriminator | OS0/SOURCE/FULL_CELL/INDEPENDENT/RATIFICATION target and one-input-removed witnesses | F3 handoff | yes |
| full-cell source-carrier support | `256` carrier after supplied full-cell source locality | finite F3 consequence | yes, conditional |
| OS0 geometry repair | OS0 four-slot geometry and `4^4 = 256` count | OS0_GEOMETRY | yes for geometry, not source locality |
| tensor-lift firewall | A1 carrier attachment residual | F3 target placement | yes |
| source-slot frame selector support | frame selection after slot-resolved controls are supplied | INDEPENDENT_MATRIX_UNIT_CONTROLS consequence | boundary only |
| restricted tensor-frame invariance support | uniformity after physical tensor-product source frame is supplied | downstream A2 support | no; review context only |
| F1 current-surface no-go | source-coupled local-action non-supply boundary | F1, not F3 | no; sibling context only |
| F2 current-surface no-go | charged-lepton D17 source-block selector non-supply boundary | F2, not F3 | no; sibling context only |
| current open PR surface | moving review context | no F3 closure | no closure; context only |
| primitive registry | approved primitive boundary | no F3 primitive | guard only |

Non-matching citations are not used as closure evidence.

### N5 - Rhetoric Audit

The negative phrase is narrow: "current surfaces do not supply
`F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED`."

| resolution | tested? | outcome |
|---|---:|---|
| OS0 geometry level | yes | support only |
| physical source-family level | yes | not supplied as retained F3 |
| full-cell tensor locality level | yes | weaker locality shapes give `64`, `16`, `4`, or `1` |
| independent matrix-unit control level | yes | not supplied as retained F3 |
| ratification level | yes | not supplied |
| F level | kept separate | also needs F1, F2, F4, owner/audit |
| source-side `S_l` level | kept separate | also needs L, P, R |
| hydrogen level | kept separate | no statement that hydrogen is impossible or retained |

No universal no-go against future F3 retention is claimed.

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| retained derivation that the charged-lepton scalar source is full-cell tensor-local over the OS0 `x,y,z,tau` slots | `F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED` |
| owner/audit acceptance of the full-cell tensor source-locality target | F3 convention route |
| OS0 geometry repair plus source-locality theorem | OS0_GEOMETRY and PHYSICAL_SOURCE_FAMILY |
| full-cell source-carrier support after F3 is supplied | finite `256` consequence |
| source-slot frame selector upgraded with retained slot-resolved source controls | INDEPENDENT_MATRIX_UNIT_CONTROLS |

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
source-locality target. This note therefore ships as a current-surface
non-supply boundary, not as a broad no-go and not as a retained theorem.

## Explicit Non-Claims

- No derivation or ratification of `F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED`.
- No derivation or ratification of F3.
- No derivation or ratification of F.
- No derivation or ratification of F1, F2, or F4.
- No derivation that `S_l = 1/256` is retained.
- No derivation of A3 precision placement, `C_A3`, or `N_A3`.
- No derivation of the Koide/electron branch or physical `m_e`.
- No derivation of `alpha(0)`, static-source Rydberg, or hydrogen spectroscopy.
- No use of observed `m_W`, observed charged-lepton masses, fitted `a_l`,
  measured `alpha(0)`, or Rydberg/hydrogen comparator data as proof inputs.
- No audit status change for any cited row.
- No new axiom, primitive, Tier-A admission, or empirical import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_f3_full_cell_tensor_source_locality_current_surface_no_go.py
```
