# Zero-Import Hydrogen: Static-Source NR Coulomb Three-Gate Target Bundle

**Date:** 2026-07-05
**Type:** target bundle / review-compression packet
**Status:** support-only. This packet does not ratify the static-source
nonrelativistic Coulomb limit, does not ratify static-source readout, does not
derive the physical-unit one-body theorem, does not derive the Hartree mapping,
does not derive `m_e`, does not derive `alpha(0)`, and does not claim hydrogen
is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_static_source_nr_coulomb_three_gate_target_bundle.py`

## Purpose

The parent static-source NR Coulomb packet now has an eleven-input contract,
and the assembly ladder review packet has compressed the direct rows. The
remaining science pressure is concentrated in three sibling content gates:

```text
STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED
ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED
HARTREE_SCALE_MAPPING_RATIFIED
```

This packet packages those three unresolved gates as one coherent target
bundle. It is useful because the gates are adjacent in the static-source
Coulomb proof, but none of them automatically closes either of the other two.
They should be reviewed together for dependency order, not conflated into one
retained theorem.

## Three-Gate Target Object

The child target under the parent NR Coulomb contract is:

```text
STATIC_SOURCE_NR_COULOMB_THREE_GATE_TARGET =
  STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED
  + ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED
  + HARTREE_SCALE_MAPPING_RATIFIED.
```

The target is not a retained consequence by itself. The parent still also
requires text lock, scalar lattice operator ratification, Green-kernel
ratification, atomic harness verification, comparator exclusion, no-new-
primitive guard, owner ratification, and audit acceptance.

## Gate 1: Static-Source Readout

The readout gate is the framework-local replacement for silently importing a
standard Coulomb potential. Current I1 material supports the arithmetic

```text
V(r) = -C g_bare^2 G(r)
     -> -C g_bare^2/(4 pi |r|)
     =  -C alpha/r,  alpha := g_bare^2/(4 pi).
```

The retained target is not just that substitution. A retained static-source
readout gate would need at least:

```text
STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED =
  STATIC_SOURCE_READOUT_TEXT_LOCK
  + NATIVE_STATIC_FIELD_INTEGRATION_HANDOFF
  + SOURCE_NORMALIZED_QUADRATIC_ACTION_HANDOFF
  + LINEAR_RESPONSE_ENERGY_READOUT_HANDOFF
  + UNIT_ELECTROMAGNETIC_SOURCE_COEFFICIENT_HANDOFF
  + NO_ACCEPTED_PREMISE_AS_RETAINED_THEOREM
  + OWNER_RATIFICATION
  + AUDIT_ACCEPTANCE.
```

The exact final owner/audit phrasing may differ, but the target must not hide
the source-normalization, energy-readout, or unit-source coefficient choices as
background. The existing I1 bridge and hygiene notes are useful support; they
are not the retained theorem by themselves.

The static-source readout ratification decision packet
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_READOUT_RATIFICATION_DECISION_PACKET_2026-07-05.md`
packages this Gate 1 target as an eight-input handoff:
STATIC_SOURCE_READOUT_TEXT_LOCK, NATIVE_STATIC_FIELD_INTEGRATION_HANDOFF,
SOURCE_NORMALIZED_QUADRATIC_ACTION_HANDOFF,
LINEAR_RESPONSE_ENERGY_READOUT_HANDOFF,
UNIT_ELECTROMAGNETIC_SOURCE_COEFFICIENT_HANDOFF,
NO_ACCEPTED_PREMISE_AS_RETAINED_THEOREM, OWNER_RATIFICATION, and
AUDIT_ACCEPTANCE. If accepted, it conditionally supplies
`STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED`.

The static-source readout current-surface no-go
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
that readout handoff. It keeps I1 accepted-premise arithmetic, native
field-integration relocation, complete-square support, RP/Kubo context, and
#5006 hygiene as support rather than retained readout closure.

## Gate 2: One-Body NR Physical-Unit Limit

The one-body gate is the framework-local replacement for importing the
textbook one-particle Schrodinger/Coulomb Hamiltonian in physical units.

The target theorem has to connect the already narrowed scalar lattice operator
and static Coulomb kernel to the low-energy one-particle atomic operator whose
dimensionless bound-state bookkeeping is:

```text
epsilon_n = -1 / (2 n^2).
```

The retained target is:

```text
ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED =
  ONE_BODY_NR_TEXT_LOCK
  + SCALAR_OPERATOR_SURFACE_CONSUMED
  + STATIC_COULOMB_KERNEL_CONSUMED
  + LOW_ENERGY_ONE_PARTICLE_REDUCTION_HANDOFF
  + DIMENSIONLESS_COULOMB_SPECTRUM_HANDOFF
  + NO_TEXTBOOK_SCHRODINGER_IMPORT
  + OWNER_RATIFICATION
  + AUDIT_ACCEPTANCE.
```

The atomic harness verifies `1/n^2` shape bookkeeping and rejects scale-only
overclaims. It does not, by itself, make the one-body physical-unit theorem a
retained framework theorem.

## Gate 3: Hartree Mapping

The Hartree mapping gate is the bridge from the dimensionless one-body target
to the physical static-source Rydberg scale:

```text
E_n = E_H * epsilon_n
E_H = m_e alpha(0)^2
Rydberg = E_H / 2.
```

The retained target is:

```text
HARTREE_SCALE_MAPPING_RATIFIED =
  HARTREE_MAPPING_TEXT_LOCK
  + RETAINED_ELECTRON_MASS_INPUT_CONSUMED
  + RETAINED_ALPHA0_INPUT_CONSUMED
  + UNIT_SOURCE_COEFFICIENT_MATCHED_TO_ALPHA0
  + PHYSICAL_UNIT_SCALE_FORMULA_HANDOFF
  + NO_RYDBERG_COMPARATOR_PROOF_INPUT
  + OWNER_RATIFICATION
  + AUDIT_ACCEPTANCE.
```

This gate consumes retained `m_e` and retained `alpha(0)` if those sibling
lanes close. It does not derive either value. It also cannot use observed
Rydberg spectroscopy, observed `m_e`, observed `alpha(0)`, or textbook
constants as proof inputs.

The static-source one-body/Hartree ratification decision packet
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_ONE_BODY_HARTREE_RATIFICATION_DECISION_PACKET_2026-07-05.md`
packages Gate 2 and Gate 3 together as one fourteen-input handoff:
STATIC_SOURCE_ONE_BODY_HARTREE_TEXT_LOCK,
SCALAR_OPERATOR_SURFACE_CONSUMED, STATIC_COULOMB_KERNEL_CONSUMED,
LOW_ENERGY_ONE_PARTICLE_REDUCTION_HANDOFF,
DIMENSIONLESS_COULOMB_SPECTRUM_HANDOFF, NO_TEXTBOOK_SCHRODINGER_IMPORT,
HARTREE_MAPPING_TEXT_LOCK, RETAINED_ELECTRON_MASS_INPUT_CONSUMED,
RETAINED_ALPHA0_INPUT_CONSUMED, UNIT_SOURCE_COEFFICIENT_MATCHED_TO_ALPHA0,
PHYSICAL_UNIT_SCALE_FORMULA_HANDOFF, NO_RYDBERG_COMPARATOR_PROOF_INPUT,
OWNER_RATIFICATION, and AUDIT_ACCEPTANCE. If accepted, it conditionally
supplies `ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED` and
`HARTREE_SCALE_MAPPING_RATIFIED`.

The static-source one-body/Hartree current-surface no-go
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_ONE_BODY_HARTREE_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
that two-gate handoff. It keeps scalar-operator narrowing, Green-kernel
normalization, atomic `1/n^2` shape support, physical-unit boundary checks,
and Hartree formula bookkeeping as support rather than retained one-body or
Hartree closure.

## Parent Contract Fit

The parent static-source NR Coulomb contract remains:

```text
STATIC_SOURCE_NR_COULOMB_TEXT_LOCK
SCALAR_LATTICE_OPERATOR_SURFACE_RATIFIED
COULOMB_KERNEL_ASYMPTOTIC_RATIFIED
STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED
ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED
HARTREE_SCALE_MAPPING_RATIFIED
ATOMIC_OPERATOR_HARNESS_VERIFIED
NO_RYDBERG_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

If and only if the full parent contract is accepted, the conditional
consequence remains:

```text
STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED
RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT.
```

This three-gate packet does not perform that acceptance.

## Source Surface

| surface | support carried into the three-gate target | boundary preserved |
| --- | --- | --- |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_LIMIT_RATIFICATION_DECISION_PACKET_2026-07-04.md` | parent eleven-input contract | no retained consequence unless all inputs are accepted |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md` | direct-row assembly under the parent | review compression only |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary | no broad impossibility claim |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_ONE_BODY_HARTREE_RATIFICATION_DECISION_PACKET_2026-07-05.md` | two-gate one-body/Hartree handoff target | no current one-body or Hartree ratification |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_ONE_BODY_HARTREE_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface boundary for one-body/Hartree | no broad impossibility claim |
| `STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md` | accepted-premise static-source readout arithmetic | not retained readout ratification |
| `STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md` | dependency-resolution hygiene for I1 | no status promotion |
| `I1_STATIC_READOUT_IS_NATIVE_FIELD_INTEGRATION_2026-06-06.md` | native field-integration relocation for I1 | residual energy-readout and source-normalization gates remain |
| `I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08.md` | finite complete-square support for supplied quadratic action | no physical source-coupling normalization or gauge-action theorem |
| `HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md` | scalar lattice operator and Coulomb-kernel narrowing | no absolute-eV atomic theorem |
| `LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md` | framework-local `G(r) -> 1/(4 pi |r|)` coefficient | no one-body physical-unit theorem |
| `ATOMIC_LANE2_PHYSICAL_UNIT_LIMIT_BOUNDARY_NOTE_2026-04-29.md` | `1/n^2` shape and Hartree-scale boundary | no scale selection |
| `ATOMIC_HYDROGEN_HELIUM_PROBE_NOTE.md` | standard-QM comparator scaffold | not zero-import proof input |
| `frontier_atomic_hydrogen_lattice_companion.py` | coupling-relative atomic harness | no physical eV scale |

## Current Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC before this packet was added. The
queue signal here is that a PR is open and lane-relevant; clean/green status is
not a proof input. No currently open PR supplies the three-gate target bundle:

| PR | queue signal | effect on this three-gate target |
| --- | ---: | --- |
| `#5033` RP two-step runner scope cleanup | open, clean | runner-scope cleanup; no static-source readout, one-body NR, or Hartree mapping theorem |
| `#5030` finite multisite Pauli carrier provenance | open, clean | finite carrier provenance support; no atomic physical-unit theorem |
| `#5021` primitive-retirement review | open draft, dirty | no registry edit and no static-source primitive shortcut |
| `#5018` domain-wall edge content vs SM chiral fermions map | open | chirality/domain-wall context; no static-source Coulomb theorem |
| `#5017` domain-wall anomaly inflow spectral flow | open | chirality/anomaly context; no atomic physical-unit theorem |
| `#5016` zero-import hydrogen retained lane bundle | open | carries this packet if merged; not owner/audit retention by itself |
| `#5015` wave-collapse-block01 measurement-collapse gate | open draft | measurement/collapse context; no static-source Coulomb handoff |
| `#5014` record-formation front/domain-wall chirality | open | chirality context; no atomic physical-unit theorem |
| `#5012` chirality domain-wall free-field note | open | adjacent chirality science; no static-source Coulomb theorem |
| `#5011` eta twisted walk family runner | open | Koide/eta route context; no static-source Coulomb closure |
| `#5007` Koide native zero-section route guard repair | open | electron-route context; no static-source Coulomb closure |
| `#5006` static-source I1 hygiene companion | open, clean | relevant I1 hygiene support; does not ratify all three gates |
| `#4991` owner-governed Tier-A retirement | open | governance context; no atomic physical-unit theorem |

## Primitive Registry Check

The primitive registry was checked through
`docs/audit/data/axiom_premise_nodes.json` and the current primitive notes.
Registered premise nodes are:

- `minimal_axioms`
- `scale_reference_primitive`
- `kinetic_isotropy_primitive`
- `realized_state_primitive`

Those nodes chain-satisfy only their declared scopes. They do not supply
static-source linear-response readout ratification, the one-body NR
physical-unit limit, the Hartree scale mapping, the static-source NR Coulomb
limit, static-source Rydberg, or hydrogen.

No node named `static_source_readout_primitive`,
`one_body_schrodinger_primitive`, `one_body_nr_primitive`,
`hartree_scale_mapping_primitive`, `static_source_nr_coulomb_primitive`,
`static_source_rydberg_primitive`, or `hydrogen_primitive` is registered.

## What This Moves

| before this packet | after this packet |
| --- | --- |
| the parent NR Coulomb packet named the three hard gates but did not give them one shared child review target | the three gates are one explicit sibling bundle |
| I1 hygiene, one-body shape, and Hartree mapping could be reviewed out of order | the dependency separation is visible: readout, one-body NR, and Hartree mapping are independent gates |
| the static-source lane was compressed only at the parent level | the next layer down is compressed without claiming retention |

## Distance To Hydrogen

This moves review distance, not retained physics distance. The static-source
NR Coulomb side is now easier to attack because the three unresolved child
gates are explicit together. The hard remaining static-source gates are still:

1. `STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED`.
2. `ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED`.
3. `HARTREE_SCALE_MAPPING_RATIFIED`.
4. `OWNER_RATIFICATION`.
5. `AUDIT_ACCEPTANCE`.

After those close, final static-source Rydberg still also needs retained
physical-unit `m_e`, retained alpha0, comparator exclusion, and final audit.

## No-Go Discipline Gate

The negative claim gated here is narrow:

```text
current retained, primitive, and open-PR surfaces do not supply the three-gate
static-source child bundle.
```

The broad claim "the static-source NR Coulomb limit cannot be retained" is not
shipped. The full parent contract remains an open positive route.

### N1 - Alternative Route Enumeration

| Route | Attempt | Outcome |
| --- | --- | --- |
| Full parent NR contract | Accept all eleven parent inputs. | OPEN POSITIVE ROUTE. This would close the static-source NR Coulomb handoff if accepted. |
| Three-gate child target | Ratify readout, one-body NR, and Hartree mapping together. | OPEN TARGET. This packet names it but does not accept it. |
| I1-only route | Treat I1 accepted-premise arithmetic and hygiene as the readout theorem. | ATTEMPTED. It omits retained source normalization, energy-readout, unit-source coefficient, owner, and audit handoff. |
| Green-kernel route | Treat `G(r) -> 1/(4 pi r)` and `V_lat -> -g/r` as the full one-body theorem. | PARTIAL ONLY. Kernel asymptotics do not supply the one-particle physical-unit reduction. |
| Atomic shape route | Treat `epsilon_n = -1/(2 n^2)` as the eV spectrum. | ATTEMPTED BY PRIOR. Shape preserves ratios but does not select the Hartree scale. |
| Hartree-map-only route | Declare `E_H = m_e alpha(0)^2` and `Rydberg = E_H/2` as closure. | PARTIAL ONLY. It consumes retained `m_e`, alpha0, and unit-source matching but derives none of them. |
| Comparator route | Select the scale from observed Rydberg or textbook constants. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data can check arithmetic, not supply proof. |
| Open-PR shortcut | Spend #5006 or newer open PRs as closure. | ATTEMPTED. #5006 is relevant I1 hygiene support, not the three-gate bundle. |
| Primitive shortcut | Treat approved primitives as supplying one of the three child gates. | RULED OUT BY REGISTRY. No approved primitive supplies readout, one-body NR, Hartree mapping, static-source NR Coulomb, Rydberg, or hydrogen. |

### N2 - Wall-Independence Audit

| Pair | Does first close second? | Does second close first? | Independent? |
| --- | --- | --- | --- |
| readout / one-body NR | no | no | yes |
| readout / Hartree mapping | no | no | yes |
| one-body NR / Hartree mapping | no | no | yes |
| readout / owner ratification | no | no | yes |
| one-body NR / owner ratification | no | no | yes |
| Hartree mapping / owner ratification | no | no | yes |
| owner ratification / audit acceptance | no | no | yes |

The collapsed child wall set is exactly the three content gates plus owner and
audit action at the parent level.

### N3 - Hidden-Wall Scan

| Phrase scanned | Classification |
| --- | --- |
| `native` | cited I1 relocation support only; not a hidden retained theorem |
| `quadratic action` | supplied-action support; source coupling remains explicit |
| `linear response` | explicit readout target, not background |
| `unit electromagnetic source` | explicit coefficient target, not assumed |
| `Schrodinger` / `one-body` | explicit physical-unit target, not imported |
| `Hartree` | explicit scale-mapping target, not a proof input |
| `registered` / `primitive` | tied to the primitive registry check above |
| `comparator` / `observed` / `textbook` | explicitly excluded as proof input |

No hidden source normalization, energy readout, one-body Hamiltonian, Hartree
scale, comparator value, owner decision, or audit decision is left as
background.

### N4 - Residual Matching

| Witness | Residual attacked | Residual used here | Match? |
| --- | --- | --- | --- |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_LIMIT_RATIFICATION_DECISION_PACKET_2026-07-04.md` | eleven-input parent handoff | parent contract context | yes |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md` | direct-row assembly | source of the three hard child rows | yes |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply of retained NR Coulomb | current non-supply of parent and child bundle | yes |
| `STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md` | accepted-premise readout bridge | readout support only | yes |
| `I1_STATIC_READOUT_IS_NATIVE_FIELD_INTEGRATION_2026-06-06.md` | native relocation with residuals | readout support with explicit residuals | yes |
| `ATOMIC_LANE2_PHYSICAL_UNIT_LIMIT_BOUNDARY_NOTE_2026-04-29.md` | `1/n^2` shape does not fix eV scale | Hartree-scale residual | yes |
| primitive registry notes | approved premise boundary | prevents primitive shortcut | guard only |

No non-matching citation is used as evidence that the three-gate bundle is
closed or impossible.

### N5 - Rhetoric Audit

The negative phrase is narrow: "current surfaces do not supply the three-gate
static-source child bundle."

| Resolution | Tested? | Outcome |
| --- | ---: | --- |
| readout gate | yes | support exists; retained readout ratification remains unsupplied |
| one-body NR gate | yes | harness exists; physical-unit theorem remains unsupplied |
| Hartree mapping gate | yes | formula target exists; retained mapping remains unsupplied |
| parent NR Coulomb contract | yes | open positive route; not currently supplied |
| static-source Rydberg | yes | downstream after retained `m_e`, alpha0, NR Coulomb, and audit |
| full hydrogen spectroscopy | kept separate | not claimed here |

No broader claim that static-source Coulomb cannot be retained is made.

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain live:

| Path | What it could close |
| --- | --- |
| successor to #5006 plus I1 native relocation | static-source readout, if it supplies source normalization, energy readout, and unit-source coefficient |
| scalar-operator plus Green-kernel low-energy theorem | one-body NR physical-unit reduction |
| retained `m_e` plus retained alpha0 plus unit-source matching | Hartree mapping |
| owner decision on the parent NR Coulomb boundary | owner ratification |
| normal audit lane acceptance | audit acceptance |

None of these is a new axiom requirement. They are the intended import-
retirement paths.

### N7 - Steelman

A hostile reviewer could argue that this packet is too conservative: the I1
bridge plus hygiene companion plus native field-integration note already show
the needed `-C alpha/r` static-source readout, the scalar lattice operator and
Green-kernel notes already fix the one-body Coulomb surface, and the atomic
harness plus physical-unit boundary already identify the Hartree mapping. On
that reading, the three gates are review bookkeeping, not new science. The
reply is that the cited surfaces still explicitly preserve accepted-premise,
source-normalization, energy-readout, physical-unit, and scale-selection
residuals, and none carries owner/audit retained consequence for the three
named gates.

### N8 - Cross-Cycle Echo

Prior similar wall patterns were checked in the static-source current-surface
no-go, the physical-unit boundary, I1 hygiene, primitive registry notes, and
the parent NR Coulomb packet. Similar walls were retired in other lanes only
by explicit target theorem, convention/owner decision, or independent audit
acceptance. The same mechanism is available here and is not rejected.

**Gate result:** PASS for the narrowed current-surface non-supply claim. The
open positive route is the three-gate target plus parent owner/audit acceptance.

## Explicit Non-Claims

- No derivation or ratification of `STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED`.
- No derivation or ratification of `ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED`.
- No derivation or ratification of `HARTREE_SCALE_MAPPING_RATIFIED`.
- No derivation or ratification of `STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED`.
- No derivation or ratification of `RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT`.
- No derivation of `m_e`.
- No derivation of `alpha(0)`.
- No static-source Rydberg retained claim.
- No retained hydrogen calculation.
- No use of observed Rydberg, observed hydrogen lines, PDG `m_e`, observed
  `alpha(0)`, or textbook constants as proof inputs.
- No audit status change for any cited row.
- No new axiom, primitive, Tier-A admission, or empirical import.

## Verification

The verifier checks the three-gate target text, parent contract fit, finite
Coulomb/Hartree arithmetic, source-surface boundaries, primitive-registry
boundary, open-PR alignment, no-go discipline markers, and explicit non-claims:

```bash
python3 scripts/frontier_zero_import_hydrogen_static_source_nr_coulomb_three_gate_target_bundle.py
```
