# Zero-Import Hydrogen: Static-Source One-Body Hartree Current-Surface No-Go

**Date:** 2026-07-05
**Type:** current-surface no-go / import-retirement target
**Status:** support-only. This note does not ratify the one-body NR
physical-unit limit, does not ratify Hartree mapping, does not ratify the
static-source NR Coulomb limit, does not derive `m_e`, does not derive
`alpha(0)`, and does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_static_source_one_body_hartree_ratification_decision_packet.py`

## Scope

The static-source NR Coulomb parent consumes two adjacent child gates:

```text
ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED
HARTREE_SCALE_MAPPING_RATIFIED
```

Current atomic surfaces supply real support: scalar operator narrowing,
Green-kernel normalization, `1/n^2` shape bookkeeping, physical-unit boundary
checks, and the Hartree target formula. They do not supply the retained
one-body/Hartree handoff. The narrow result is not "the framework cannot
retain the one-body atomic theorem or Hartree mapping." The narrow result is
that current retained, primitive, and open-PR surfaces do not supply the
combined one-body/Hartree decision contract from
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_ONE_BODY_HARTREE_RATIFICATION_DECISION_PACKET_2026-07-05.md`.

## One-Body Hartree Contract

A future one-body/Hartree handoff needs all fourteen inputs from the decision
packet:

```text
STATIC_SOURCE_ONE_BODY_HARTREE_TEXT_LOCK
SCALAR_OPERATOR_SURFACE_CONSUMED
STATIC_COULOMB_KERNEL_CONSUMED
LOW_ENERGY_ONE_PARTICLE_REDUCTION_HANDOFF
DIMENSIONLESS_COULOMB_SPECTRUM_HANDOFF
NO_TEXTBOOK_SCHRODINGER_IMPORT
HARTREE_MAPPING_TEXT_LOCK
RETAINED_ELECTRON_MASS_INPUT_CONSUMED
RETAINED_ALPHA0_INPUT_CONSUMED
UNIT_SOURCE_COEFFICIENT_MATCHED_TO_ALPHA0
PHYSICAL_UNIT_SCALE_FORMULA_HANDOFF
NO_RYDBERG_COMPARATOR_PROOF_INPUT
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

If all fourteen inputs are accepted, the conditional consequences would be:

```text
ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED
HARTREE_SCALE_MAPPING_RATIFIED
```

Those consequences are not supplied here. The current missing inputs include:

```text
LOW_ENERGY_ONE_PARTICLE_REDUCTION_HANDOFF
DIMENSIONLESS_COULOMB_SPECTRUM_HANDOFF
RETAINED_ELECTRON_MASS_INPUT_CONSUMED
RETAINED_ALPHA0_INPUT_CONSUMED
UNIT_SOURCE_COEFFICIENT_MATCHED_TO_ALPHA0
PHYSICAL_UNIT_SCALE_FORMULA_HANDOFF
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

The atomic harness and physical-unit boundary remain important support. They
are not identical to retained one-body/Hartree ratification because the
framework-local low-energy theorem, retained physical inputs, unit-source
matching, no-comparator proof firewall, and owner/audit acceptance remain
explicit.

## Current-Surface Audit

| surface | supplies | does not supply |
| --- | --- | --- |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_ONE_BODY_HARTREE_RATIFICATION_DECISION_PACKET_2026-07-05.md` | fourteen-input one-body/Hartree owner/audit handoff | current retained consequence |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_THREE_GATE_TARGET_BUNDLE_2026-07-05.md` | parent three-gate target context | one-body/Hartree ratification |
| `ATOMIC_LANE2_PHYSICAL_UNIT_LIMIT_BOUNDARY_NOTE_2026-04-29.md` | proof that `1/n^2` shape does not fix eV scale; names `E_H = m_e alpha(0)^2` | retained physical-unit theorem |
| `HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md` | scalar operator and Coulomb-kernel dependency narrowing | absolute-eV atomic theorem |
| `LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md` | framework-local `G(r) -> 1/(4 pi |r|)` normalization | one-body physical-unit theorem |
| `ATOMIC_HYDROGEN_HELIUM_PROBE_NOTE.md` | textbook one-body and helium scaffold | framework-retained inputs |
| `frontier_atomic_hydrogen_lattice_companion.py` | coupling-relative `1/n^2` harness | physical eV scale |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md` | downstream static-source Rydberg predicate | one-body/Hartree closure |
| `ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md` | sibling `m_e` decision target | retained `m_e` consumed here |
| `ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md` | sibling alpha0 target surface | retained alpha0 consumed here |
| approved primitives | minimal axioms, scale reference, kinetic-form isotropy, realized-state evaluation discipline | one-body Schrodinger theorem, Hartree mapping, retained `m_e`, alpha0, or hydrogen |

The primitive registry was checked with the current origin-main methodology.
No registered primitive supplies `one_body_schrodinger_primitive`,
`one_body_nr_primitive`, `hartree_scale_mapping_primitive`,
`unit_source_coefficient_primitive`, `electron_mass_primitive`,
`alpha0_primitive`, `static_source_rydberg_primitive`, or
`hydrogen_primitive`.

## Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC. The newest open rows do not close
the one-body/Hartree handoff:

| PR | state at refresh | one-body/Hartree effect |
| --- | ---: | --- |
| `#5033` RP two-step runner scope cleanup | `CLEAN` | runner-scope cleanup; no one-body/Hartree theorem |
| `#5030` finite multisite Pauli carrier provenance | `CLEAN` | finite carrier support; no atomic physical-unit theorem |
| `#5021` primitive-retirement review | draft, `DIRTY` | no registry edit and no one-body/Hartree primitive shortcut |
| `#5018` domain-wall edge content vs SM chiral fermions map | `CLEAN` | chirality context; no one-body/Hartree theorem |
| `#5017` domain-wall anomaly inflow spectral flow | `CLEAN` | chirality/anomaly context; no atomic physical-unit theorem |
| `#5016` zero-import hydrogen retained lane bundle | `UNSTABLE` | carries this target work if merged; not owner/audit retention |
| `#5015` wave-collapse-block01 measurement-collapse gate | draft, `DIRTY` | measurement/collapse context; no one-body/Hartree handoff |
| `#5014` record-formation front/domain-wall chirality | `CLEAN` | chirality context; no atomic physical-unit theorem |
| `#5012` chirality domain-wall free-field note | `CLEAN` | adjacent chirality science; no one-body/Hartree theorem |
| `#5011` eta twisted walk family runner | `CLEAN` | Koide/eta context; no one-body/Hartree closure |
| `#5007` Koide native zero-section route guard repair | `CLEAN` | electron-route context; no atomic physical-unit closure |
| `#5006` static-source I1 hygiene companion | `CLEAN` | readout hygiene support; no one-body/Hartree ratification |
| `#4991` owner-governed Tier-A retirement | `CLEAN` | governance context; no atomic physical-unit theorem |

Merge-state labels are moving review metadata, not proof inputs.

## What This Moves

| before this note | after this note |
| --- | --- |
| atomic shape support could be overread as retained physical spectrum | shape support is separated from one-body reduction and Hartree mapping |
| `E_H = m_e alpha(0)^2` could be mistaken for an `m_e` or alpha0 derivation | the mapping is recorded as a consumer of retained sibling inputs |
| the parent three-gate bundle named one-body NR and Hartree mapping but lacked a current-surface boundary for those two gates | the two adjacent gates now have a scoped non-supply claim and positive target |

## No-Go Discipline Gate

This section prevents overclaiming. The broad one-body/Hartree no-go is not
shipped. The narrowed claim is:

```text
the current retained, primitive, and open-PR surfaces do not supply the
fourteen-input one-body/Hartree handoff that would conditionally yield
ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED and HARTREE_SCALE_MAPPING_RATIFIED.
```

### N1 - Alternative Route Enumeration

| Route | Attempt | Outcome |
| --- | --- | --- |
| Full one-body/Hartree contract | Accept all fourteen contract inputs and owner/audit acceptance. | OPEN POSITIVE ROUTE. This would close the two child gates if accepted. |
| Atomic harness shape route | Treat the coupling-relative `1/n^2` harness as a physical eV spectrum. | ATTEMPTED. The harness checks shape only and does not set the Hartree scale. |
| Physical-unit boundary route | Treat `ATOMIC_LANE2_PHYSICAL_UNIT_LIMIT_BOUNDARY_NOTE_2026-04-29.md` as the retained theorem. | PARTIAL ONLY. It names the Hartree residual and shows scale degeneracy. |
| Green-kernel route | Treat `G(r) -> 1/(4 pi r)` as the one-body physical-unit theorem. | PARTIAL ONLY. It supplies kernel normalization, not the low-energy one-particle reduction or Hartree mapping. |
| Hartree formula-only route | Treat `E_H = m_e alpha(0)^2` as a retained hydrogen scale. | PARTIAL ONLY. It consumes retained `m_e` and retained alpha0; it does not derive them. |
| Static-source readout route | Use static-source readout support as one-body/Hartree closure. | PARTIAL ONLY. Readout is a sibling child gate and does not close the atomic physical-unit theorem. |
| Open-PR shortcut | Spend open Koide, RP, static-source hygiene, or primitive-review PRs as closure. | ATTEMPTED. No open PR supplies the fourteen-input handoff. |
| Primitive shortcut | Treat approved primitives as supplying one-body NR, Hartree mapping, `m_e`, or alpha0. | RULED OUT BY REGISTRY. No approved primitive supplies those bridges. |
| Comparator route | Select the Hartree scale from observed Rydberg, observed `m_e`, observed alpha0, or textbook constants. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data can check arithmetic, not supply proof. |

### N2 - Wall-Independence Audit

| Pair | Does first close second? | Does second close first? | Independent? |
| --- | --- | --- | --- |
| low-energy one-particle reduction / dimensionless spectrum | no | no | yes |
| dimensionless spectrum / Hartree mapping | no | no | yes |
| Hartree mapping / retained `m_e` | no | no | yes; mapping consumes `m_e` but does not derive it |
| Hartree mapping / retained alpha0 | no | no | yes; mapping consumes alpha0 but does not derive it |
| unit-source coefficient / alpha0 transport | no | no | yes |
| no-comparator firewall / owner ratification | no | no | yes |
| owner ratification / audit acceptance | no | no | yes |

The collapsed surface is one fourteen-input handoff, not a broad claim that
the one-body theorem or Hartree mapping cannot be retained.

### N3 - Hidden-Wall Scan

| Phrase scanned | Classification |
| --- | --- |
| `one-body` / `Schrodinger` | explicit target, not a hidden textbook import |
| `dimensionless` / `1/n^2` | explicit shape handoff, not physical eV scale |
| `Hartree` / `m_e alpha(0)^2` | explicit mapping target requiring sibling retained inputs |
| `unit-source` / `coefficient` | explicit matching target, not hidden Casimir or comparator fit |
| `retained m_e` / `retained alpha0` | explicit consumed inputs, not derived here |
| `primitive` / `registered` | tied to the primitive registry check above |
| `comparator` / `observed` / `textbook` | explicitly excluded as proof input |

No hidden one-body theorem, Hartree scale, retained electron mass, alpha0
transport, unit-source matching, owner decision, or audit decision is left as
background.

### N4 - Residual Matching

| Witness | Residual attacked | Residual used here | Match? |
| --- | --- | --- | --- |
| `ATOMIC_LANE2_PHYSICAL_UNIT_LIMIT_BOUNDARY_NOTE_2026-04-29.md` | `1/n^2` shape does not fix physical eV scale | Hartree-scale and no shape-to-eV shortcut residual | yes |
| `HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md` | scalar operator and kernel narrowing without absolute eV prediction | support only | yes |
| `LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md` | framework-local Green-kernel normalization | kernel support only | yes |
| `frontier_atomic_hydrogen_lattice_companion.py` | coupling-relative atomic harness | shape support only | yes |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_THREE_GATE_TARGET_BUNDLE_2026-07-05.md` | child-gate target separation | parent target context | yes |
| primitive registry notes | approved premise boundary | prevents primitive shortcut | guard only |

No non-matching citation is used as evidence that the one-body/Hartree handoff
is closed or impossible.

### N5 - Rhetoric Audit

The negative phrase is narrow: "current surfaces do not supply the
fourteen-input one-body/Hartree handoff."

| Resolution | Tested? | Outcome |
| --- | ---: | --- |
| scalar operator narrowing | yes | support exists; retained one-body theorem remains unsupplied |
| Green-kernel normalization | yes | support exists; physical-unit theorem remains unsupplied |
| `1/n^2` shape harness | yes | support exists; Hartree scale remains unsupplied |
| Hartree formula | yes | mapping target exists; retained `m_e` and alpha0 remain consumed inputs |
| unit-source coefficient | yes | not supplied by shape, kernel, or comparator data |
| parent NR Coulomb | yes | downstream and still open |
| hydrogen spectroscopy | kept separate | not claimed here |

No broader claim that the one-body theorem or Hartree mapping cannot be
retained is made.

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain live:

| Path | What it could close |
| --- | --- |
| retained low-energy one-particle reduction theorem | `LOW_ENERGY_ONE_PARTICLE_REDUCTION_HANDOFF` |
| retained dimensionless Coulomb spectrum theorem | `DIMENSIONLESS_COULOMB_SPECTRUM_HANDOFF` |
| owner/audit acceptance of the Hartree mapping as a pure physical-unit formula | `PHYSICAL_UNIT_SCALE_FORMULA_HANDOFF` |
| retained electron mass lane | `RETAINED_ELECTRON_MASS_INPUT_CONSUMED` |
| retained alpha0 transport lane | `RETAINED_ALPHA0_INPUT_CONSUMED` |
| retained unit-source coefficient matching | `UNIT_SOURCE_COEFFICIENT_MATCHED_TO_ALPHA0` |
| normal owner/audit action | `OWNER_RATIFICATION` and `AUDIT_ACCEPTANCE` |

None of these is a new axiom requirement. They are the intended import-
retirement paths.

### N7 - Steelman

A hostile reviewer could argue that this current-surface note is too
conservative: the scalar operator, Green-kernel coefficient, and atomic harness
already reproduce the standard dimensionless Coulomb `1/n^2` structure, while
the Hartree formula is only dimensional bookkeeping once retained `m_e` and
alpha0 are supplied by sibling lanes. On that view the two child gates are
nearly closed and the remaining work is owner/audit bookkeeping. The reply is
that the cited notes themselves preserve the low-energy one-particle reduction,
shape-to-physical-unit, retained-input, unit-source, no-comparator, owner, and
audit residuals, so this note must expose those residuals rather than promote
support into retained one-body/Hartree closure.

### N8 - Cross-Cycle Echo

Similar walls appear in the atomic physical-unit boundary note, static-source
NR Coulomb packet, static-source Rydberg discriminator, electron-mass packet,
and alpha0 transport packet. Their shared pattern is not "new axiom required";
it is import relocation followed by explicit target theorem, retained sibling
input, owner decision, and audit acceptance. The same mechanism is available
here and is not rejected.

**Gate result:** PASS for the narrowed current-surface non-supply claim. The
open positive route is the fourteen-input one-body/Hartree contract.

## Explicit Non-Claims

- No derivation or ratification of `ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED`.
- No derivation or ratification of `HARTREE_SCALE_MAPPING_RATIFIED`.
- No derivation or ratification of `STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED`.
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
