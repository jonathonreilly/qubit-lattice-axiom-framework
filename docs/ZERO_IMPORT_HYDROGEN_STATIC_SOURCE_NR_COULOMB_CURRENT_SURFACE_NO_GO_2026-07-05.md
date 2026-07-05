# Zero-Import Hydrogen: Static-Source NR Coulomb Current-Surface No-Go

**Date:** 2026-07-05
**Type:** current-surface no-go / import-retirement target
**Status:** support-only. This note does not ratify the static-source
nonrelativistic Coulomb limit, does not derive `m_e`, does not derive
`alpha(0)`, does not derive static-source Rydberg, and does not claim
hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_static_source_nr_coulomb_current_surface_no_go.py`

## Scope

The static-source Rydberg lane consumes one final structural input:

```text
RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT.
```

The static-source NR Coulomb decision packet packages that input through the
conditional consequence:

```text
STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED
RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT.
```

Current static-source surfaces supply real support: scalar `Z^3` lattice
operator bookkeeping, Green-kernel asymptotics, I1 static-source readout
hygiene, native complete-square support, and atomic `1/n^2` harness checks.
They do not supply the retained physical-unit one-body Coulomb theorem. The
narrow result is not "the framework cannot retain the static-source NR
Coulomb limit." The narrow result is that current retained, primitive, and
open-PR surfaces do not supply `STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED` or
`RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT`.

## Static-Source NR Coulomb Contract

A future static-source NR Coulomb handoff needs all eleven inputs:

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

If all eleven inputs are accepted, the conditional consequence would be:

```text
STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED
RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT.
```

That consequence is not supplied here. The current missing inputs include:

```text
STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED
ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED
HARTREE_SCALE_MAPPING_RATIFIED
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

The scalar lattice operator, `Z^3` Green-kernel asymptote, I1 hygiene, and
atomic operator harness remain important support. They are not identical to a
retained physical-unit one-body Schrodinger/Coulomb theorem for the unit
electromagnetic static source.

The static-source NR Coulomb assembly ladder review packet
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md`
groups those direct support rows under the parent contract for review
compression only. It does not supply `STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED`
or `RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT`.

The static-source NR Coulomb three-gate target bundle
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_THREE_GATE_TARGET_BUNDLE_2026-07-05.md`
packages the unresolved content gates beneath the parent contract:
`STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED`,
`ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED`, and
`HARTREE_SCALE_MAPPING_RATIFIED`. It records the next positive target surface;
it does not ratify any child gate and does not supply the parent retained
handoff.

The static-source readout ratification decision packet
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_READOUT_RATIFICATION_DECISION_PACKET_2026-07-05.md`
and current-surface no-go
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md`
package the first child gate under that target. They record that I1
accepted-premise arithmetic, native field-integration relocation,
complete-square support, RP/Kubo context, and #5006 hygiene are support only;
they do not supply `STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED`.

## Target Arithmetic

The structural atomic target is:

```text
epsilon_n = -1 / (2 n^2)
E_n = E_H * epsilon_n
E_H = m_e alpha(0)^2
Rydberg = E_H / 2.
```

The static-source kernel support is:

```text
G(r) -> 1/(4 pi |r|)
V_lat(r) = -4 pi g G(r) -> -g/|r|
```

The I1 readout support is:

```text
V(r) = -C g_bare^2 G(r)
     -> -C g_bare^2/(4 pi |r|)
     =  -C alpha/|r|,  alpha := g_bare^2/(4 pi).
```

Those equations are support and target bookkeeping. The retained
static-source NR Coulomb limit still requires the unit-source physical
coefficient, one-body NR physical-unit reduction, Hartree mapping, comparator
exclusion, owner ratification, and audit acceptance.

## Current-Surface Audit

| surface | supplies | does not supply |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_LIMIT_RATIFICATION_DECISION_PACKET_2026-07-04.md` | eleven-input owner/audit handoff | current retained consequence |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_THREE_GATE_TARGET_BUNDLE_2026-07-05.md` | shared target for readout, one-body NR, and Hartree mapping child gates | child-gate ratification or parent retained consequence |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_READOUT_RATIFICATION_DECISION_PACKET_2026-07-05.md` | eight-input readout handoff | current retained readout consequence |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface boundary for readout | retained readout |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_ONE_BODY_HARTREE_RATIFICATION_DECISION_PACKET_2026-07-05.md` | fourteen-input one-body/Hartree handoff | current retained one-body or Hartree consequence |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_ONE_BODY_HARTREE_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface boundary for one-body/Hartree | retained one-body NR physical-unit theorem or retained Hartree mapping |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md` | downstream Rydberg predicate | NR Coulomb limit derivation |
| `ATOMIC_LANE2_PHYSICAL_UNIT_LIMIT_BOUNDARY_NOTE_2026-04-29.md` | proof that `1/n^2` shape does not fix eV scale | physical-unit closure |
| `HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md` | scalar operator and kernel dependency narrowing | absolute-eV prediction |
| `LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md` | framework-local `G(r) -> 1/(4 pi |r|)` normalization | one-body physical-unit theorem |
| `STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md` | accepted-premise `V -> -C alpha/r` substitution bridge | derived static-source readout ratification |
| `I1_STATIC_READOUT_IS_NATIVE_FIELD_INTEGRATION_2026-06-06.md` | relocation of I1 toward native field integration | elimination of energy-readout/source-normalization residuals |
| `I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08.md` | finite complete-square support for supplied quadratic action | physical source-coupling normalization or gauge action |
| `ATOMIC_HYDROGEN_HELIUM_PROBE_NOTE.md` | standard-QM physical-unit scaffold | framework-retained inputs |
| `frontier_atomic_hydrogen_lattice_companion.py` | coupling-relative `1/n^2` harness | physical eV scale |
| approved primitives | minimal axioms, scale reference, kinetic-form isotropy, realized-state evaluation discipline | static-source readout, one-body NR reduction, Hartree scale, or hydrogen |

The primitive registry was checked with the current origin-main methodology.
No registered primitive supplies `static_source_nr_coulomb_primitive`,
`retained_static_source_nr_coulomb_primitive`,
`one_body_schrodinger_primitive`, `static_source_readout_primitive`,
`hartree_scale_mapping_primitive`, or `hydrogen_spectrum_primitive`.

## Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC. The newest rows are clean and
green, but they do not close the static-source NR Coulomb handoff:

| PR | state at refresh | static-source NR Coulomb effect |
|---|---:|---|
| `#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS` | theta gauge-side work; no atomic one-body NR limit |
| `#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS` | adjacent chirality science; no static-source Coulomb theorem |
| `#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS` | runner stabilization; no static-source NR Coulomb package |
| `#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS` | diagnostic repair; no atomic one-body NR limit |
| `#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS` | bounded S3 tensor context; no static-source Coulomb limit |
| `#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS` | quark context; no atomic one-body theorem |
| `#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS` | electron-readout route support, not atomic NR Coulomb closure |
| `#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS` | closest input; repairs I1 hygiene, but does not retain the full one-body NR Coulomb limit |
| `#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS` | status progress for old Tier-A atoms; no atomic NR Coulomb package |

The `#5006` file list is limited to the I1 hygiene companion note, runner, and
runner cache. That is relevant static-source hygiene, not a retained
`RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT` consequence. Merge-state labels are
moving review metadata, not proof inputs.

## What This Moves

| before this note | after this note |
|---|---|
| the static-source packet supplied a decision contract | the current-surface non-supply boundary is explicit |
| lattice `1/n^2` and Green-kernel support could be overread as physical eV Rydberg | shape, kernel, readout, NR reduction, and Hartree scale are separated |
| I1 hygiene could be mistaken for full static-source closure | PR #5006 is recorded as relevant but insufficient |

## No-Go Discipline Gate

This section prevents overclaiming. The broad static-source-retention no-go is
not shipped. The narrowed claim is:

```text
the current retained, primitive, and open-PR surfaces do not supply
STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED or
RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full static-source NR contract | Accept all eleven contract inputs. | OPEN POSITIVE ROUTE. This would close the handoff, but the contract is not accepted here. |
| standard-QM scaffold route | Use the textbook Schrodinger Coulomb Hamiltonian from the atomic probe. | VALID COMPARATOR/HARNESS ONLY. It imports the physical-unit one-body limit and constants. |
| lattice shape route | Use coupling-relative `1/n^2` ratios as the eV spectrum. | ATTEMPTED BY PRIOR. Shape does not select `E_H = m_e alpha(0)^2`. |
| Green-kernel-only route | Use `G(r) -> 1/(4 pi r)` and `V_lat -> -g/r` as the whole atomic theorem. | PARTIAL ONLY. It supplies the far-field kernel, not the one-body physical-unit reduction. |
| I1 hygiene route | Treat accepted-premise I1 plus PR #5006 hygiene as retained closure. | ATTEMPTED. It improves readout hygiene but does not promote all contract inputs. |
| native complete-square route | Use the finite supplied-action complete square as full Coulomb closure. | PARTIAL ONLY. Physical source normalization, gauge action, and energy-readout residuals remain explicit. |
| retained `m_e` plus retained `alpha(0)` shortcut | Supply the two physical numbers and call hydrogen retained. | INCOMPLETE. The final predicate also requires the retained static-source NR Coulomb limit, harness, comparator exclusion, and audit. |
| comparator-fit route | Select the Hartree scale from observed Rydberg or textbook hydrogen levels. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is target data, not proof input. |
| open-PR shortcut | Treat the current clean open PR surface, especially `#5006`, as closure. | ATTEMPTED. `#5006` is I1 hygiene context, not a one-body physical-unit theorem. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| scalar operator surface <-> Green-kernel asymptotic | no | independent support gates |
| Green-kernel asymptotic <-> static-source readout | no | independent |
| static-source readout <-> one-body NR physical-unit reduction | no | independent |
| one-body NR reduction <-> Hartree scale mapping | no | independent |
| Hartree mapping <-> retained `m_e` and `alpha(0)` | no | mapping consumes those retained inputs; it does not derive them |
| owner ratification <-> audit acceptance | no | independent |

The collapsed wall is the eleven-input contract above, with current pressure
on readout ratification, physical-unit one-body reduction, Hartree mapping,
owner decision, and audit acceptance.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `1/n^2` / `epsilon_n` | shape support, not eV scale |
| `G(r)` / `1/(4 pi r)` | kernel support, not full atomic theorem |
| `I1` / `linear response` / `complete square` | static-source readout support with residuals |
| `Schrodinger` / `one-body` / `physical unit` | explicit missing contract input |
| `Hartree` / `m_e alpha(0)^2` | explicit mapping target, not derived here |
| `registered` / `primitive` | registry checked; no shortcut exists |
| `observed` / `textbook` / `comparator` | excluded as proof input |

No static-source readout theorem, one-body NR physical-unit limit, Hartree
mapping, comparator exclusion, owner decision, or audit decision is hidden as
background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| static-source NR decision packet | owner/audit handoff | current-surface non-supply | yes |
| static-source Rydberg discriminator | downstream consumer predicate | consumer only, not closure | yes |
| physical-unit boundary note | shape does not set eV scale | Hartree-scale residual | yes |
| kinetic dependency repair | scalar operator/kernel narrowing | support only | yes |
| Green-kernel note | `1/(4 pi r)` kernel | kernel only | yes |
| I1 accepted-premise bridge | readout substitution | readout remains not retained as full package | yes |
| I1 native relocation | native field-integration route | residual energy-readout/source-normalization gates | yes |
| I1 quadratic bridge | supplied-action complete square | no physical source-coupling normalization | yes |
| current open PR surface | moving review context | no retained NR Coulomb closure | no closure; context only |

Non-matching citations are not used as closure evidence.

### N5 - Rhetoric Audit

The negative phrase is narrow: "current surfaces do not supply
`STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED` or
`RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT`."

| resolution | tested? | outcome |
|---|---:|---|
| scalar operator and `1/n^2` harness | yes | support/shape only |
| Green-kernel asymptotic | yes | kernel only |
| I1 accepted-premise/hygiene route | yes | support, not full retained package |
| native complete-square route | yes | support with explicit residuals |
| physical-unit one-body theorem | not closed | left open as a valid future route |
| owner/audit packet acceptance | not closed | left open as the positive handoff |

No universal no-go against future static-source NR Coulomb retention is
claimed.

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| retained scalar operator theorem or owner/audit adoption | `SCALAR_LATTICE_OPERATOR_SURFACE_RATIFIED` |
| retained Green-kernel asymptotic handoff | `COULOMB_KERNEL_ASYMPTOTIC_RATIFIED` |
| retained static-source readout theorem | `STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED` |
| retained one-body low-energy theorem | `ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED` |
| retained Hartree-scale mapping theorem | `HARTREE_SCALE_MAPPING_RATIFIED` |
| owner/audit acceptance of the existing static-source packet | `STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED` after all inputs are present |

These are import-retirement paths, not new-axiom requirements.

### N7 - Steelman

A hostile reviewer can argue that this note is too conservative: the scalar
operator, native Green kernel, I1 bridge, native complete-square route, and
atomic harness already look like ordinary Bohr hydrogen. The strongest version
says the one-body Schrodinger/Coulomb limit should be infrastructure, not a
separate retained theorem. This note preserves that positive route, but
zero-import retained hydrogen cannot import the physical-unit one-body limit,
unit-source coefficient, Hartree mapping, or observed Rydberg scale as
background.

### N8 - Cross-Cycle Echo

This echoes the prior Rydberg and Lane 2 firewalls: shape and high-quality
support can be real while still failing to supply the physical value. The same
mechanism applies here: keep scalar operator shape, Green kernel, static-source
readout, one-body NR reduction, Hartree mapping, and final audit separate until
the owner/audit contract is accepted without comparator proof input.

**Gate result:** broad static-source NR Coulomb no-go fails; narrowed
current-surface non-supply claim passes.

## Explicit Non-Claims

- No derivation or ratification of `STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED`.
- No derivation or ratification of `RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT`.
- No derivation or ratification of the scalar lattice-operator atomic surface.
- No derivation or ratification of the static-source linear-response readout.
- No derivation of the physical-unit one-body Schrodinger reduction.
- No derivation or ratification of the Hartree scale mapping.
- No derivation of `m_e`.
- No derivation of `alpha(0)`.
- No static-source Rydberg retained claim.
- No retained hydrogen calculation.
- No use of observed Rydberg, observed hydrogen lines, PDG `m_e`, observed
  `alpha(0)`, or textbook constants as proof inputs.
- No audit status change for any cited row.
- No new axiom, primitive, Tier-A admission, or empirical import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_static_source_nr_coulomb_current_surface_no_go.py
```

The verifier checks the current-surface boundary, static-source NR Coulomb
predicate, finite Coulomb/Hartree arithmetic, primitive registry, open PR
alignment, No-Go Discipline markers, and explicit non-claims.
