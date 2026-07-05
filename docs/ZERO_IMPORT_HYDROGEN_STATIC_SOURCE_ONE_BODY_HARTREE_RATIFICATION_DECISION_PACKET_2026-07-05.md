# Zero-Import Hydrogen: Static-Source One-Body Hartree Ratification Decision Packet

**Date:** 2026-07-05
**Type:** decision packet / import-retirement handoff
**Status:** support-only. This packet does not ratify the one-body NR
physical-unit limit, does not ratify Hartree mapping, does not ratify the
static-source NR Coulomb limit, does not derive `m_e`, does not derive
`alpha(0)`, and does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_static_source_one_body_hartree_ratification_decision_packet.py`

## Purpose

The static-source NR Coulomb three-gate target bundle names two adjacent
atomic-unit child gates:

```text
ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED
HARTREE_SCALE_MAPPING_RATIFIED
```

Those gates should be reviewed together because the first supplies the
dimensionless one-body atomic operator target and the second maps that target
to the physical static-source Rydberg scale. They should not be conflated:
the one-body gate does not select `m_e` or `alpha(0)`, and the Hartree mapping
does not derive the one-body theorem.

## Decision Object

The decision target is:

```text
the zero-import static-source one-body NR plus Hartree mapping package.
```

It has six content clauses:

| clause | decision text |
| --- | --- |
| OBH.1 | scalar operator and static Coulomb kernel are consumed from the narrowed static-source surface |
| OBH.2 | the low-energy one-particle reduction is accepted without importing the textbook Schrodinger problem as proof |
| OBH.3 | the dimensionless Coulomb spectrum handoff is accepted with `epsilon_n = -1 / (2 n^2)` |
| OBH.4 | the physical-unit map is accepted as `E_n = E_H epsilon_n`, `E_H = m_e alpha(0)^2`, and `Rydberg = E_H / 2` |
| OBH.5 | the unit static-source coefficient is matched to the low-energy Coulomb `alpha(0)` input, not to a hidden color Casimir or comparator fit |
| OBH.6 | observed Rydberg spectroscopy, observed `m_e`, observed `alpha(0)`, and textbook constants remain comparator data, not proof inputs |

## Ratification Decision Contract

This packet is decision-ready only if all fourteen contract inputs are visible:

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

The contract means:

1. **STATIC_SOURCE_ONE_BODY_HARTREE_TEXT_LOCK:** the OBH.1-OBH.6 text above is
   the complete object being decided.
2. **SCALAR_OPERATOR_SURFACE_CONSUMED:** the scalar lattice-operator surface is
   consumed only after its own ratification.
3. **STATIC_COULOMB_KERNEL_CONSUMED:** the static `G(r) -> 1/(4 pi |r|)`
   kernel is consumed only after its own ratification.
4. **LOW_ENERGY_ONE_PARTICLE_REDUCTION_HANDOFF:** the framework-local low-energy
   one-particle reduction is accepted for this atomic lane.
5. **DIMENSIONLESS_COULOMB_SPECTRUM_HANDOFF:** the dimensionless `1/n^2`
   Coulomb spectrum is accepted as the atomic operator output.
6. **NO_TEXTBOOK_SCHRODINGER_IMPORT:** the textbook Schrodinger problem is not
   silently spent as a retained framework theorem.
7. **HARTREE_MAPPING_TEXT_LOCK:** the Hartree formula text in OBH.4 is the
   complete mapping object being decided.
8. **RETAINED_ELECTRON_MASS_INPUT_CONSUMED:** the mapping consumes a retained
   physical electron mass if the electron lane closes.
9. **RETAINED_ALPHA0_INPUT_CONSUMED:** the mapping consumes a retained
   low-energy Coulomb `alpha(0)` if the alpha lane closes.
10. **UNIT_SOURCE_COEFFICIENT_MATCHED_TO_ALPHA0:** the static-source unit
    coefficient is matched to the low-energy Coulomb coefficient rather than to
    a hidden Casimir, fitted Rydberg coefficient, or arbitrary convention.
11. **PHYSICAL_UNIT_SCALE_FORMULA_HANDOFF:** the physical scale formula
    `E_H = m_e alpha(0)^2` and `Rydberg = E_H / 2` is accepted as the
    physical-unit handoff.
12. **NO_RYDBERG_COMPARATOR_PROOF_INPUT:** observed hydrogen spectroscopy and
    textbook constants are excluded as proof inputs.
13. **OWNER_RATIFICATION:** the owner explicitly accepts the one-body/Hartree
    boundary or retained theorem boundary.
14. **AUDIT_ACCEPTANCE:** the normal review/audit path accepts the decision and
    its dependency consequences.

No proper subset of those fourteen contract inputs is a retained one-body plus
Hartree decision.

## Conditional Consequence

If all fourteen contract inputs are accepted, the conditional consequences are:

```text
ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED
HARTREE_SCALE_MAPPING_RATIFIED
```

Those consequences are two child gates under the static-source NR Coulomb
three-gate target. They do not by themselves supply:

```text
STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED
STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED
RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT
STATIC_SOURCE_RYDBERG_RETAINED
```

The one-body/Hartree current-surface no-go
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_ONE_BODY_HARTREE_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
the combined one-body/Hartree handoff. Its current pressure is on the
low-energy one-particle reduction handoff, dimensionless spectrum handoff,
retained `m_e`, retained alpha0, unit-source matching, physical-unit formula
ratification, owner ratification, and audit acceptance.

## Source Surface

| surface | support carried into this decision | boundary preserved |
| --- | --- | --- |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_THREE_GATE_TARGET_BUNDLE_2026-07-05.md` | parent child-gate target for readout, one-body NR, and Hartree mapping | no child-gate ratification |
| `HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md` | scalar lattice operator and Coulomb-kernel narrowing | repair/support only; no absolute-eV prediction |
| `LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md` | framework-local static Green-kernel coefficient | kernel coefficient only |
| `ATOMIC_LANE2_PHYSICAL_UNIT_LIMIT_BOUNDARY_NOTE_2026-04-29.md` | shows `1/n^2` shape is scale-degenerate and names the Hartree residual | boundary only, not retained theorem |
| `ATOMIC_HYDROGEN_HELIUM_PROBE_NOTE.md` | textbook one-body and helium scaffold for comparison | comparator/scaffold only |
| `frontier_atomic_hydrogen_lattice_companion.py` | coupling-relative `1/n^2` harness | shape only; no physical eV scale |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md` | downstream static-source Rydberg predicate | does not close one-body/Hartree |
| `ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md` | sibling `m_e` decision target | does not supply retained `m_e` here |
| `ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md` | sibling alpha0 target surface | does not supply retained alpha0 here |

## Current Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC before this packet was added. The
queue signal here is that a PR is open and lane-relevant; clean/green status is
not a proof input. No currently open PR supplies this one-body/Hartree handoff:

| PR | queue signal | effect on this decision |
| --- | ---: | --- |
| `#5033` RP two-step runner scope cleanup | open, clean | transfer-matrix cleanup; no one-body/Hartree theorem |
| `#5030` finite multisite Pauli carrier provenance | open, clean | finite carrier support; no atomic physical-unit theorem |
| `#5021` primitive-retirement review | open draft, dirty | no registry edit and no one-body/Hartree primitive shortcut |
| `#5018` domain-wall edge content vs SM chiral fermions map | open | chirality context; no atomic physical-unit theorem |
| `#5017` domain-wall anomaly inflow spectral flow | open | chirality/anomaly context; no one-body/Hartree theorem |
| `#5016` zero-import hydrogen retained lane bundle | open | carries this packet if merged; not owner/audit retention by itself |
| `#5015` wave-collapse-block01 measurement-collapse gate | open draft | measurement/collapse context; no atomic physical-unit handoff |
| `#5014` record-formation front/domain-wall chirality | open | chirality context; no one-body/Hartree theorem |
| `#5012` chirality domain-wall free-field note | open | adjacent chirality science; no one-body/Hartree theorem |
| `#5011` eta twisted walk family runner | open | Koide/eta context; no one-body/Hartree closure |
| `#5007` Koide native zero-section route guard repair | open | electron-route context; no atomic physical-unit closure |
| `#5006` static-source I1 hygiene companion | open, clean | readout hygiene support; no one-body/Hartree ratification |
| `#4991` owner-governed Tier-A retirement | open | governance context; no atomic physical-unit theorem |

## Primitive Registry Check

The primitive registry was checked through
`docs/audit/data/axiom_premise_nodes.json` and the current primitive notes.
Registered premise nodes are:

- `minimal_axioms`
- `scale_reference_primitive`
- `kinetic_isotropy_primitive`
- `realized_state_primitive`

Those nodes chain-satisfy only their declared scopes. They do not supply a
one-body Schrodinger theorem, a one-body NR physical-unit theorem, a Hartree
scale mapping, a unit electromagnetic source coefficient, retained `m_e`,
retained alpha0, static-source Rydberg, or hydrogen.

No node named `one_body_schrodinger_primitive`, `one_body_nr_primitive`,
`hartree_scale_mapping_primitive`, `unit_source_coefficient_primitive`,
`electron_mass_primitive`, `alpha0_primitive`,
`static_source_rydberg_primitive`, or `hydrogen_primitive` is registered.

## What This Moves

| before this packet | after this packet |
| --- | --- |
| the three-gate bundle named one-body NR and Hartree mapping but left them as prose targets | the two adjacent atomic-unit gates have one explicit fourteen-input decision object |
| the atomic `1/n^2` harness could be overread as a physical eV spectrum | shape, one-body reduction, retained inputs, and Hartree mapping are separated |
| Hartree mapping could be mistaken for an `m_e` or alpha0 derivation | the mapping is explicitly a consumer of sibling retained inputs |

## Distance To Hydrogen

This moves review distance, not retained physics distance. If this contract is
accepted, it would close two of the three child gates under the static-source
NR Coulomb three-gate bundle. Hydrogen would still need static-source readout
ratification, parent NR Coulomb owner/audit acceptance, retained `m_e`,
retained alpha0, final Rydberg audit, and later full-precision corrections.

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

## Verification

The verifier checks the one-body/Hartree decision contract, finite atomic
shape and Hartree arithmetic, source-surface boundaries, primitive-registry
boundary, open-PR alignment, and explicit non-claims:

```bash
python3 scripts/frontier_zero_import_hydrogen_static_source_one_body_hartree_ratification_decision_packet.py
```
