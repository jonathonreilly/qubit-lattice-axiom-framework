# Zero-Import Hydrogen: Static-Source NR Coulomb Assembly Ladder Review Packet

**Date:** 2026-07-05
**Type:** support / review-compression packet
**Status:** review support only; this packet does not ratify the static-source
NR Coulomb limit, does not derive `m_e`, does not derive `alpha(0)`, does not
derive static-source Rydberg, and does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_static_source_nr_coulomb_assembly_ladder_review_packet.py`

## Result

This packet compresses the direct static-source nonrelativistic Coulomb
dependency ladder into one reviewable surface. It does not supply
`STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED` or
`RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT`; it records how the operator,
Green-kernel, static-source readout, one-body physical-unit, Hartree mapping,
harness, comparator-exclusion, owner, and audit rows sit under the parent
static-source NR Coulomb handoff.

The useful grouped lane is:

```text
SCALAR_LATTICE_OPERATOR_SURFACE_RATIFIED
  + COULOMB_KERNEL_ASYMPTOTIC_RATIFIED
  + STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED
  + ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED
  + HARTREE_SCALE_MAPPING_RATIFIED
  + ATOMIC_OPERATOR_HARNESS_VERIFIED
  + NO_RYDBERG_COMPARATOR_PROOF_INPUT
  + NO_NEW_PRIMITIVE_OR_AXIOM
  + owner/audit contract
  -> STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED
  -> RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT
```

This is the largest scientifically coherent next bundle on the final atomic
side because all listed rows are direct inputs to the parent static-source NR
Coulomb contract. It would be premature to bundle retained physical `m_e`,
retained alpha0, final static-source Rydberg, or full hydrogen into the same
claim: those are downstream or sibling lanes, not direct NR Coulomb closure
clauses.

## Parent Static-Source NR Coulomb Contract

The parent decision object remains the eleven-input handoff in
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_LIMIT_RATIFICATION_DECISION_PACKET_2026-07-04.md`:

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

No proper subset of those eleven contract inputs is treated here as a retained
static-source NR Coulomb limit handoff. If the parent contract is accepted with
all inputs, it conditionally supplies `STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED`
and `RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT`. This packet does not perform
that acceptance.

## Direct Ladder Rows

| Row | Existing packet or surface | Role in static-source NR Coulomb | Boundary preserved |
| --- | --- | --- | --- |
| SNR.0 | `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_LIMIT_RATIFICATION_DECISION_PACKET_2026-07-04.md` | parent eleven-input handoff | no current retained consequence |
| SNR.0 no-go | `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface boundary | current retained, primitive, and open-PR surfaces do not supply the handoff |
| SNR.0 child bundle | `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_THREE_GATE_TARGET_BUNDLE_2026-07-05.md` | bundles the three unresolved sibling content gates: readout, one-body NR physical-unit reduction, and Hartree mapping | review target only; no ratification of any child gate |
| SNR.1 | `HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md` | scalar lattice operator and Coulomb-kernel dependency narrowing | repair/support only; no absolute-eV prediction |
| SNR.2 | `LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md` | framework-local `Z^3` Green-kernel normalization `G(r) -> 1/(4 pi |r|)` | kernel coefficient only; no one-body NR physical-unit theorem |
| SNR.3 | `STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md` | conditional `V(r) -> -C alpha/r` static-source readout bridge | accepted-premise/bounded bridge; P1/readout not retained here |
| SNR.3 hygiene | `STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md`, `I1_STATIC_READOUT_IS_NATIVE_FIELD_INTEGRATION_2026-06-06.md`, `I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08.md` | hygiene and native relocation support for the I1 route | residual source normalization, energy readout, and physical source-coupling gates remain |
| SNR.4 | `ATOMIC_HYDROGEN_HELIUM_PROBE_NOTE.md`, `ATOMIC_LANE2_PHYSICAL_UNIT_LIMIT_BOUNDARY_NOTE_2026-04-29.md` | one-body Schrodinger/Coulomb and physical-unit boundary | textbook scaffold and boundary only; no framework-retained one-body theorem |
| SNR.5 | `ATOMIC_LANE2_PHYSICAL_UNIT_LIMIT_BOUNDARY_NOTE_2026-04-29.md`, `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md` | Hartree mapping `E_H = m_e alpha(0)^2`, `Rydberg = E_H/2` | mapping target only; does not derive `m_e` or alpha0 |
| SNR.6 | `frontier_atomic_hydrogen_lattice_companion.py` | coupling-relative `1/n^2` harness | shape only; no physical eV scale |
| SNR.7 | primitive registry and owner/audit lane | no-new-primitive, owner, and audit clauses | no primitive shortcut and no audit status change |

The final static-source Rydberg assembly packet
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md`
can consume `RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT` only after the parent
NR Coulomb contract is accepted. This packet is not that acceptance.

## Finite Witness Carried Forward

The finite arithmetic reviewed by this packet is only target bookkeeping:

```text
epsilon_n = -1 / (2 n^2)
E_n = E_H * epsilon_n
E_H = m_e alpha(0)^2
Rydberg = E_H / 2
```

Changing the Hartree scale changes the eV levels while preserving the same
ratios:

```text
E_n / E_1 = 1 / n^2.
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

The witness makes three boundaries visible:

- `1/n^2` shape does not select the Hartree scale;
- Green-kernel asymptotics do not by themselves supply the physical-unit
  one-body Schrodinger/Coulomb theorem;
- I1 readout arithmetic does not by itself ratify the unit electromagnetic
  static-source coefficient, source normalization, Hartree mapping, or final
  audit consequence.

## Current Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC before this packet was added. The
queue signal here is that a PR is open and lane-relevant; clean/green status
is not a prerequisite because reviewer cleanup and landing happen outside this
packet. No currently open PR supplies the static-source NR Coulomb assembly
handoff:

| PR | queue signal | effect on this static-source NR Coulomb assembly |
| --- | ---: | --- |
| `#5033` RP two-step runner scope cleanup | open, clean | runner-scope cleanup; no static-source NR Coulomb theorem |
| `#5030` finite multisite Pauli carrier provenance | open, clean | finite carrier provenance support; no atomic one-body theorem |
| `#5021` primitive-retirement review | open draft, dirty | no registry edit and no static-source NR Coulomb primitive shortcut |
| `#5018` domain-wall edge content vs SM chiral fermions map | open | chirality/domain-wall context; no atomic static-source theorem |
| `#5017` domain-wall anomaly inflow spectral flow | open | chirality/domain-wall context; no static-source NR Coulomb limit |
| `#5016` zero-import hydrogen retained lane bundle | open | carries this review packet if merged; not owner/audit retention by itself |
| `#5015` wave-collapse-block01 measurement-collapse gate | open draft | measurement/collapse work; no static-source NR Coulomb handoff |
| `#5014` record-formation front/domain-wall chirality | open | chirality context; no static-source NR Coulomb limit |
| `#5012` chirality domain-wall free-field note | open | adjacent chirality science; no atomic one-body theorem |
| `#5011` eta twisted walk family runner | open | Koide/eta route context; no atomic NR Coulomb closure |
| `#5007` Koide native zero-section route guard repair | open | electron-route context; no static-source NR Coulomb closure |
| `#5006` static-source I1 hygiene companion | open, clean | relevant I1 hygiene support; does not retain the full one-body NR Coulomb limit |
| `#4991` owner-governed Tier-A retirement | open | governance context for old atoms; no atomic NR Coulomb package |

Merge-state labels, branch ordering, and check status are moving review
metadata, not proof inputs here.

## Primitive Registry Check

The primitive registry was checked through
`docs/audit/data/axiom_premise_nodes.json` and the current primitive notes.
Registered premise nodes are:

- `minimal_axioms`
- `scale_reference_primitive`
- `kinetic_isotropy_primitive`
- `realized_state_primitive`

Those nodes chain-satisfy only their declared scopes. They do not supply a
static-source linear-response readout theorem, a one-body physical-unit
Schrodinger/Coulomb reduction, a Hartree scale mapping, a static-source NR
Coulomb limit, physical electron mass, alpha0 transport, static-source
Rydberg closure, or hydrogen spectroscopy.

No node named `static_source_nr_coulomb_primitive`,
`retained_static_source_nr_coulomb_primitive`,
`one_body_schrodinger_primitive`, `static_source_readout_primitive`,
`hartree_scale_mapping_primitive`, `static_source_rydberg_primitive`,
`electron_mass_primitive`, `alpha0_primitive`, or `hydrogen_primitive` is
registered.

## Distance To Hydrogen

This packet moves review distance, not retained physics distance. After this
packet, the static-source NR Coulomb blocker is easier to review as one
eleven-input assembly surface. The three-gate target bundle
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_THREE_GATE_TARGET_BUNDLE_2026-07-05.md`
now makes the unresolved content gates reviewable together, but the hard gates
remain:

1. Static-source readout ratification:
   `STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED`.
2. One-body physical-unit reduction:
   `ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED`.
3. Hartree mapping ratification:
   `HARTREE_SCALE_MAPPING_RATIFIED`.
4. Parent owner/audit acceptance for
   `STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED` and
   `RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT`.

Even after those close, final static-source Rydberg still needs retained
physical-unit `m_e`, retained alpha0, the final Rydberg predicate, and audit.

## No-Go Discipline Gate

The negative claim gated here is narrow: current retained, primitive, and
open-PR surfaces do not supply retained static-source NR Coulomb merely
because the direct assembly ladder is now review-compressed. The full
eleven-input static-source NR Coulomb contract remains an open positive route.

### N1 - Alternative Route Enumeration

| Route | Attempt | Outcome |
| --- | --- | --- |
| Full static-source NR contract | Accept all eleven contract inputs and owner/audit acceptance. | OPEN POSITIVE ROUTE. This packet does not reject it; it is the path to retained static-source NR Coulomb. |
| Standard-QM scaffold route | Use the textbook Schrodinger Coulomb Hamiltonian from the atomic probe. | VALID COMPARATOR/HARNESS ONLY. It imports the physical-unit one-body limit and textbook constants. |
| Lattice shape route | Use coupling-relative `1/n^2` ratios as the eV spectrum. | ATTEMPTED BY PRIOR. Shape does not select `E_H = m_e alpha(0)^2`. |
| Green-kernel-only route | Use `G(r) -> 1/(4 pi r)` and `V_lat -> -g/r` as the whole atomic theorem. | PARTIAL ONLY. It supplies the far-field kernel, not readout ratification or the one-body physical-unit reduction. |
| I1/readout route | Treat accepted-premise I1 plus hygiene and native relocation as retained closure. | ATTEMPTED. It improves readout hygiene but does not promote all contract inputs. |
| Native complete-square route | Use the finite supplied-action complete square as full Coulomb closure. | PARTIAL ONLY. Physical source normalization, gauge action, and energy-readout residuals remain explicit. |
| Hartree-map-only route | Treat `E_H = m_e alpha(0)^2` as the retained atomic theorem. | ATTEMPTED. It is a mapping target and still needs retained `m_e`, retained alpha0, one-body NR theorem, and audit. |
| Open-PR shortcut | Treat newly opened runner, primitive-review, chirality, Koide, or static-source PRs as closure. | ATTEMPTED. The refreshed open PR queue supplies no spendable static-source NR Coulomb theorem. |
| Primitive shortcut | Treat approved primitives as already supplying the NR Coulomb limit. | RULED OUT BY PRIOR. The checked registry contains no static-source readout, one-body Schrodinger, Hartree mapping, static-source NR, Rydberg, or hydrogen primitive. |

### N2 - Wall-Independence Audit

| Pair | Does first close second? | Does second close first? | Independent for NR Coulomb spending? |
| --- | --- | --- | --- |
| scalar operator surface / Green-kernel asymptotic | no | no | yes |
| Green-kernel asymptotic / static-source readout | no | no | yes |
| static-source readout / one-body NR physical-unit reduction | no | no | yes |
| one-body NR reduction / Hartree scale mapping | no | no | yes |
| Hartree mapping / retained `m_e` and alpha0 | no | no | yes; mapping consumes those lanes but does not derive them |
| atomic harness / retained theorem content | no | no | yes |
| comparator exclusion / retained theorem content | no | no | yes |
| owner ratification / audit acceptance | no | no | yes |

The collapsed surface is one eleven-input static-source NR Coulomb contract,
not final static-source Rydberg and not full hydrogen spectroscopy.

### N3 - Hidden-Wall Scan

| Phrase scanned | Classification |
| --- | --- |
| `support` | non-load-bearing review role; not a retained claim |
| `standard-QM` / `Schrodinger` | explicit one-body NR physical-unit input, not background |
| `framework-local` | source-scoped Green-kernel statement, not full atomic theorem |
| `accepted-premise` / `P1` | explicit static-source readout input requiring ratification |
| `physical-unit` / `Hartree` | explicit scale mapping target requiring retained `m_e` and alpha0 |
| `registered` / `primitive` | tied to the primitive registry check above |
| `comparator` / `observed` / `textbook` | explicitly excluded as proof input |
| `assembly` / `ladder` | review compression only, not an added axiom or retained consequence |

No hidden one-body Hamiltonian, readout convention, Hartree scale, comparator
value, owner decision, or audit decision is left as background.

### N4 - Residual Matching

| Witness | Residual attacked | Residual used here | Match? |
| --- | --- | --- | --- |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_LIMIT_RATIFICATION_DECISION_PACKET_2026-07-04.md` | eleven-input static-source NR handoff | parent contract | yes |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply | current non-supply boundary | yes |
| `ATOMIC_LANE2_PHYSICAL_UNIT_LIMIT_BOUNDARY_NOTE_2026-04-29.md` | shape does not determine eV scale | Hartree-scale residual | yes |
| `HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md` | scalar graph-Laplacian and Coulomb-kernel dependency narrowing | SNR.1 support | yes |
| `LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md` | `Z^3` graph-Laplacian `1/(4 pi r)` asymptotic | SNR.2 support | yes |
| `STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md` | readout substitution under accepted P1 | SNR.3 target | yes, partial |
| `I1_STATIC_READOUT_IS_NATIVE_FIELD_INTEGRATION_2026-06-06.md` | native field-integration relocation | SNR.3 hygiene only | yes, partial |
| `I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08.md` | supplied-action complete square | SNR.3 hygiene only | yes, partial |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md` | downstream final predicate consumer | consumer only, not NR closure | yes |
| `axiom_premise_nodes.json` | primitive boundary | registry guard only | yes |

Non-matching full-spectroscopy, helium, and many-body atomic surfaces are not
used as evidence for static-source NR Coulomb closure or non-closure.

### N5 - Rhetoric Audit

The phrase "static-source NR Coulomb is not closed by X alone" is tested only
at the contract-input resolution:

- scalar operator support alone;
- Green-kernel asymptotic alone;
- I1/readout support alone;
- atomic `1/n^2` harness alone;
- Hartree mapping alone;
- opened PR metadata alone;
- approved primitive registry alone.

The packet does not claim that the parent contract is impossible. It says that
the parent contract has not been accepted by current retained, primitive, or
open-PR surfaces.

### N6 - Partial-Closure Path Scan

| Partial closure | Can it be useful? | Why it is not final NR Coulomb |
| --- | --- | --- |
| Scalar operator ratification | yes | needed kinetic surface, but not Green coefficient or readout |
| Green-kernel ratification | yes | needed `1/r` coefficient, but not readout or one-body theorem |
| Static-source readout ratification | yes | needed source-coupling readout, but not one-body physical-unit reduction |
| One-body NR reduction | yes | needed low-energy theorem, but not Hartree mapping or audit |
| Hartree mapping | yes | needed physical scale map, but consumes retained `m_e` and alpha0 rather than deriving them |
| Harness and comparator exclusion | yes | protects bookkeeping and zero-import status, but supplies no retained input alone |
| Owner/audit acceptance | yes | final retained status gate, not a physics derivation |

Each partial closure remains a valid lane to pursue. This packet exists so
review can see them as one static-source NR Coulomb assembly surface instead
of many disconnected notes.

### N7 - Steelman Positive Route

The strongest positive route is straightforward: ratify the scalar operator
surface, ratify the Green-kernel asymptotic, replace or ratify the I1
accepted-premise readout, prove the one-body physical-unit low-energy
Schrodinger/Coulomb reduction, ratify the Hartree mapping that consumes
retained `m_e` and retained alpha0, verify the atomic harness, exclude
Rydberg comparator inputs, and send the resulting dependency graph through
owner/audit acceptance. If those steps are accepted, the consequence
`RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT` becomes spendable by the final
static-source Rydberg assembly. This packet does not claim that result now.

### N8 - Cross-Cycle Echo

The same boundary is echoed in the atomic physical-unit boundary, Rydberg
firewall, static-source NR Coulomb decision packet, current-surface no-go,
final static-source Rydberg discriminator, and static-source Rydberg assembly:
correct `1/n^2` shape and correct `1/r` kernel support are not the same thing
as a retained physical-unit atomic theorem.

**Gate result:** PASS for the narrowed current-surface claim. Broad
"static-source NR Coulomb cannot be retained" and broad "hydrogen is retained"
claims are not shipped.

## Explicit Non-Claims

- No derivation or ratification of `STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED`.
- No derivation or ratification of `RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT`.
- No derivation or ratification of the scalar lattice-operator atomic surface.
- No derivation or ratification of the Coulomb-kernel asymptotic.
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
