# Zero-Import Hydrogen: Static-Source Rydberg Closure Discriminator

**Date:** 2026-07-04
**Type:** final-lane closure harness discriminator
**Claim type:** meta / dependency discriminator
**Status:** support-only. This note does not promote a retained hydrogen
claim, does not derive `m_e`, does not derive `alpha(0)`, and does not derive
full hydrogen spectroscopy.
**Verifier:** `scripts/frontier_zero_import_hydrogen_static_source_rydberg_closure_discriminator.py`

## Scope

The zero-import hydrogen goal packet uses the static-source one-body target

```text
E_n = -m_e alpha(0)^2 / (2 n^2).
```

This is the Rydberg-scale hydrogen harness: an infinitely heavy proton or
static unit positive source, nonrelativistic Coulomb operator, and physical
electron mass readout. It is the right final substitution target for the
packet's `-13.6057 eV / n^2` claim. It is not the full precision hydrogen
spectrum.

The discriminator answers a narrow question:

```text
If retained m_e, retained alpha(0), and the retained static-source
nonrelativistic Coulomb limit are supplied, is anything else needed to get
the Rydberg-scale eV series?
```

For that static-source target, the remaining final step is bookkeeping:
substitute the retained inputs into the already-scoped one-body harness and
send the resulting theorem through audit. The hard work is still upstream:
Lane 6 for `m_e`, Lane 2 for `alpha(0)`, and the physical-unit
nonrelativistic Coulomb limit.

## Closure Predicate

Use the following predicate for this packet's final target:

```text
STATIC_SOURCE_RYDBERG_RETAINED =
  RETAINED_ELECTRON_MASS_PHYSICAL_UNIT
  and RETAINED_ALPHA0_LOW_ENERGY_COULOMB
  and RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT
  and ATOMIC_OPERATOR_HARNESS_VERIFIED
  and NO_RYDBERG_COMPARATOR_PROOF_INPUT
  and AUDIT_ACCEPTANCE
```

Where:

| input | content |
|---|---|
| `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT` | Lane 6 supplies `m_e` as a physical-unit electron mass, not only a Koide shape or scale scaffold. |
| `RETAINED_ALPHA0_LOW_ENERGY_COULOMB` | Lane 2 supplies the low-energy Coulomb coupling `alpha(0)`, not only `alpha_EM(M_Z)`. |
| `RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT` | the framework supplies the one-body nonrelativistic Schrodinger/Coulomb limit in physical units for a static positive source. |
| `ATOMIC_OPERATOR_HARNESS_VERIFIED` | the lattice/atomic harness checks the `1/n^2` spectral bookkeeping. |
| `NO_RYDBERG_COMPARATOR_PROOF_INPUT` | observed Rydberg, observed hydrogen lines, PDG `m_e`, or observed `alpha(0)` are not proof inputs. They may be post-hoc comparators only. |
| `AUDIT_ACCEPTANCE` | independent audit accepts the theorem and its dependency graph. |

This predicate deliberately does not require a retained proton mass. The target
is the static-source Rydberg scale. Real finite-proton hydrogen spectroscopy is
a stronger target:

```text
FULL_PRECISION_HYDROGEN =
  STATIC_SOURCE_RYDBERG_RETAINED
  and RETAINED_PROTON_MASS
  and RETAINED_REDUCED_MASS_BRIDGE
  and RETAINED_FINE_STRUCTURE_QED_CORRECTIONS
  and RETAINED_LAMB_SHIFT_CORRECTIONS
  and RETAINED_HYPERFINE_AND_SPIN_STRUCTURE
```

That stronger target is not needed to answer the current `-13.6057 eV / n^2`
critique.

## Arithmetic Harness

With physical electron mass in eV and dimensionless `alpha`, the harness is:

```text
R_inf = (1/2) m_e alpha(0)^2
E_n = -R_inf / n^2.
```

Comparator arithmetic, using observed constants only as a check:

```text
m_e = 510998.95 eV
alpha(0)^-1 = 137.035999084
R_inf = 13.605693122994 eV
E_1 = -13.605693122994 eV
E_2 = -3.401423280749 eV
E_3 = -1.511743680333 eV
```

The same harness with the retained high-energy value

```text
alpha_EM(M_Z)^-1 = 127.67
```

gives

```text
E_1 ~= -15.68 eV,
```

about a 15 percent overshoot. So the final closure predicate cannot replace
`alpha(0)` with `alpha_EM(M_Z)`.

## Current Standing

| gate | current hydrogen-facing standing |
|---|---|
| atomic operator shape | scaffolded and narrowed. `frontier_atomic_hydrogen_lattice_companion.py` checks coupling-relative `1/n^2`; the 2026-06-02 repair narrows the scalar graph-Laplacian and Coulomb-kernel dependency. |
| `m_e` | open through Lane 6. The physical electron mass ratification packet now packages the exact `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT` handoff, but the native bridge, physical species bridge, absolute scale, branch-to-mass map, owner ratification, and audit still have to be accepted before this predicate can consume it. |
| `alpha(0)` | open through Lane 2 QED running. The alpha loop-kernel target discriminator names QED loop-kernel, threshold/matching moment, R-Lep, R-Q-Heavy, R-Had-NP, scheme/decoupling, and no-comparator inputs. |
| static-source NR Coulomb physical-unit limit | scaffolded by standard-QM, lattice-operator, Green-kernel, and I1 static-source companions. The ratification decision packet below packages the retained-theorem handoff, but this discriminator does not promote it. |
| final Rydberg substitution | shallow after the first three gates are retained; currently not retained. |

The alpha0 transport ratification decision packet
`ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md`
packages the Lane 2 handoff for `RETAINED_ALPHA0_LOW_ENERGY_COULOMB`:
ALPHA0_TRANSPORT_TEXT_LOCK, ALPHA_MZ_RETAINED, QED_LOOP_KERNEL_RETAINED,
R_LEP_THRESHOLDS_RETAINED, R_Q_HEAVY_THRESHOLDS_RETAINED,
R_HAD_NP_RETAINED, SCHEME_DECOUPLING_MATCHING_RETAINED,
NO_COMPARATOR_PROOF_INPUT, NO_NEW_PRIMITIVE_OR_AXIOM, OWNER_RATIFICATION, and
AUDIT_ACCEPTANCE. If accepted, `ALPHA0_TRANSPORT_RETAINED` and
`ALPHA0_RETAINED` follow conditionally, but this final Rydberg predicate still
also needs retained physical-unit `m_e`, retained static-source NR Coulomb
limit, harness verification, no Rydberg comparator proof input, and audit.

The alpha0 transport current-surface no-go
`ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
the Lane 2 `alpha(0)` handoff. The final predicate therefore still treats
`RETAINED_ALPHA0_LOW_ENERGY_COULOMB` as an unsupplied upstream input, not as
current retained content.

The static-source NR Coulomb limit ratification decision packet
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_LIMIT_RATIFICATION_DECISION_PACKET_2026-07-04.md`
packages the final structural handoff for
`RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT`:
STATIC_SOURCE_NR_COULOMB_TEXT_LOCK,
SCALAR_LATTICE_OPERATOR_SURFACE_RATIFIED,
COULOMB_KERNEL_ASYMPTOTIC_RATIFIED,
STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED,
ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED,
HARTREE_SCALE_MAPPING_RATIFIED, ATOMIC_OPERATOR_HARNESS_VERIFIED,
NO_RYDBERG_COMPARATOR_PROOF_INPUT, NO_NEW_PRIMITIVE_OR_AXIOM,
OWNER_RATIFICATION, and AUDIT_ACCEPTANCE. If accepted,
`STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED` and
`RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT` follow conditionally, but this final
Rydberg predicate still also needs retained physical-unit `m_e`, retained
`alpha(0)`, harness verification, no Rydberg comparator proof input, and audit.

The static-source NR Coulomb current-surface no-go
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
the final structural handoff. The final predicate therefore still treats
`RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT` as an unsupplied upstream input, not
as current retained content.

The physical electron mass ratification decision packet
`ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md`
packages the Lane 6 handoff for `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`:
PHYSICAL_ELECTRON_MASS_TEXT_LOCK,
NATIVE_ZERO_SECTION_BRIDGE_RETAINED,
PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED,
ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED, KOIDE_BRANCH_MASS_MAP_RETAINED,
SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED,
NO_LEPTON_COMPARATOR_PROOF_INPUT, NO_RYDBERG_COMPARATOR_PROOF_INPUT,
NO_NEW_PRIMITIVE_OR_AXIOM, OWNER_RATIFICATION, and AUDIT_ACCEPTANCE. If
accepted, `PHYSICAL_ELECTRON_READOUT_RETAINED` and
`RETAINED_ELECTRON_MASS_PHYSICAL_UNIT` follow conditionally, but this final
Rydberg predicate still also needs retained `alpha(0)`, retained static-source
NR Coulomb limit, harness verification, no Rydberg comparator proof input, and
audit.

The physical electron mass current-surface no-go
`ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
the Lane 6 `m_e` handoff. The final predicate therefore still treats
`RETAINED_ELECTRON_MASS_PHYSICAL_UNIT` as an unsupplied upstream input, not as
current retained content.

## Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC before this discriminator was
updated.
The current moving science does not close the final hydrogen predicate:

| PR | audit status | hydrogen effect |
|---|---:|---|
| `#5013` theta native positive-class adjudication | `SUCCESS` | no static-source Rydberg closure, no `m_e`, no `alpha(0)` |
| `#5012` chirality domain-wall free-field note | `SUCCESS` | adjacent chirality science; no static-source Rydberg closure |
| `#5011` eta twisted walk family runner | `SUCCESS` | runner stabilization; no atomic one-body NR limit |
| `#5010` YT P1 I_s re-audit packet bridge repair | `SUCCESS` | diagnostic repair; no static-source Rydberg closure |
| `#5009` S3 spacetime tensor primitive runner | `SUCCESS` | bounded S3 tensor context; no hydrogen closure |
| `#5008` quark mass-ratio CP probe repair | `SUCCESS` | quark context; no electron readout or low-energy Coulomb coupling |
| `#5007` Koide native zero-section route guard repair | `SUCCESS` | useful route-guard context, but not a physical electron-mass readout |
| `#5006` static-source I1 hygiene companion | `SUCCESS` | relevant I1 hygiene context, but not retained static-source Rydberg closure |
| `#4991` owner-governed Tier-A retirement | `SUCCESS` | status improvement for old Tier-A atoms, not a hydrogen calculation |

## Lane Consequence

This artifact moves the end of the program from a slogan to an auditable
predicate. The distance to retained static-source hydrogen is now:

```text
Lane 6 closes m_e
  + Lane 2 closes alpha(0)
  + retained static-source NR Coulomb limit
  + audit
  -> retained static-source Rydberg series
```

It also prevents two common overclaims:

1. `m_e` and `alpha(0)` do not by themselves prove full precision hydrogen.
   They close the static-source Rydberg target after the one-body NR Coulomb
   limit is retained.
2. the observed Rydberg value cannot be used to select `m_e`, `alpha(0)`, or
   a hidden threshold. It is only a post-hoc comparator.

## No-Go Discipline Gate

The broad claim "hydrogen cannot be calculated" is **not** shipped. The
narrowed claim is: the current repo has a final substitution harness for the
static-source Rydberg series, but the retained zero-import predicate is not
closed until `m_e`, `alpha(0)`, the static-source NR Coulomb limit, and audit
acceptance are supplied without Rydberg comparator input.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| textbook comparator route | Use observed `m_e` and observed `alpha(0)` in the Bohr formula. | VALID COMPARATOR ONLY. It verifies the harness but imports both physical inputs. |
| high-energy alpha shortcut | Use retained `alpha_EM(M_Z)` as the atomic coupling. | ATTEMPTED BY PRIOR. The Rydberg firewall and this harness show an about 15 percent overshoot. |
| retained `m_e` plus imported `alpha(0)` | Close Lane 6 and consume observed low-energy alpha. | VALID NONZERO-IMPORT ROUTE. It is not zero-import retained hydrogen. |
| retained `alpha(0)` plus imported `m_e` | Close QED running and consume observed electron mass. | VALID NONZERO-IMPORT ROUTE. It is not zero-import retained hydrogen. |
| lattice companion shape route | Use the lattice atomic companion's `1/n^2` ratios as the full eV spectrum. | PARTIAL ONLY. It supplies coupling-relative shape, not the physical Hartree scale. |
| static-source retained route | Supply retained `m_e`, retained `alpha(0)`, retained static-source NR Coulomb limit, and audit. | TARGET ROUTE. It closes the packet's `-13.6057 eV / n^2` Rydberg target. |
| full spectroscopy route | Add proton mass, reduced-mass bridge, fine structure, Lamb shift, and spin/hyperfine terms. | STRONGER FUTURE TARGET. It is beyond the current static-source Rydberg claim. |

### N2 - Wall-independence audit

| pair | closes automatically? | conclusion |
|---|---|---|
| `m_e` <-> `alpha(0)` | no in either direction | independent |
| `m_e` <-> static-source NR limit | no in either direction | independent |
| `alpha(0)` <-> static-source NR limit | no in either direction | independent |
| comparator exclusion <-> input retention | no in either direction | independent |
| static-source target <-> full spectroscopy target | no; full spectroscopy is stronger | keep collapsed target as static-source Rydberg |

No wall is counted twice. The collapsed final target is static-source Rydberg,
not full precision spectroscopy.

### N3 - Hidden-wall scan

| phrase class | classification |
|---|---|
| `static-source` | explicit target restriction; avoids hidden proton-mass import. |
| `physical-unit` | carried by the retained electron-mass readout and the NR limit, not supplied by the formula alone. |
| `harness` | verification/bookkeeping role only, not a retained theorem. |
| `comparator` | explicitly excluded as a proof input. |
| `Schrodinger/Coulomb` | explicit NR-limit wall, not background context. |

No hidden admission is left as standard background.

### N4 - Residual matching

| cited surface | residual it attacks | match? |
|---|---|---|
| `ATOMIC_RYDBERG_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md` | direct `alpha_EM(M_Z)` substitution and missing `m_e`, `alpha(0)`, NR limit | yes |
| `HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md` | scalar graph-Laplacian and Coulomb-kernel dependency narrowing | yes for operator shape, not eV scale |
| `frontier_atomic_hydrogen_lattice_companion.py` | coupling-relative `1/n^2` lattice harness | yes for shape, not physical inputs |
| `ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md` | electron-mass readout boundary | yes |
| `ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md` | physical electron-mass handoff boundary | yes |
| `ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary for the Lane 6 `m_e` handoff | yes |
| `ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md` | `alpha(0)` transport boundary | yes |
| `ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary for the Lane 2 `alpha(0)` handoff | yes |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary for the static-source NR Coulomb handoff | yes |
| `axiom_premise_nodes.json` | primitive boundary | guard only; it does not supply hydrogen inputs |

Non-matching citations are not used as closure evidence.

### N5 - Rhetoric audit

The note avoids "hydrogen is solved" and uses the narrow target
"static-source Rydberg series."

| resolution | tested? | outcome |
|---|---|---|
| one-body static-source Rydberg | yes | closes once the predicate inputs are retained and audited. |
| finite-proton nonrelativistic hydrogen | not claimed | needs proton mass and reduced-mass bridge. |
| fine structure / Lamb shift / hyperfine | not claimed | needs separate QED and spin inputs. |
| helium or many-body atoms | not claimed | outside this discriminator. |

### N6 - Partial-closure path scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| Lane 6 physical electron mass packet | `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`. |
| alpha QED loop-kernel and threshold/matching program | `RETAINED_ALPHA0_LOW_ENERGY_COULOMB`. |
| atomic lattice-operator and NR-limit program | `RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT`. |
| independent audit lane | `AUDIT_ACCEPTANCE`. |

Because these paths are live, this note is a closure discriminator, not a
negative theorem.

### N7 - Steelman

A hostile reviewer can argue that the atomic harness is already just standard
nonrelativistic quantum mechanics, so once the framework has any plausible
electron mass and any plausible electromagnetic coupling, calling the final
hydrogen step "open" is procedural hair-splitting. The strongest version is:
the formula is elementary, the lattice companion already checks the spectral
shape, and the scale-reference primitive handles units. The narrow reply is
that zero-import retained status is a dependency-graph claim, not a numerical
familiarity claim. The observed Rydberg value, observed `m_e`, observed
`alpha(0)`, and imported NR Coulomb bridge cannot be silent proof inputs.

### N8 - Cross-cycle echo

This mirrors the repo's recurring atomic firewall: a correct textbook or
bounded-scaffold calculation is easy to overread as a framework-retained
prediction. The present note keeps the levels separated: shape harness,
physical inputs, static-source target, full spectroscopy, and audit status.

**Gate result:** broad no-go fails; narrowed static-source Rydberg closure
predicate passes.

## Explicit Non-Claims

- No derivation of `m_e`.
- No derivation of `alpha(0)`.
- No derivation of the physical-unit nonrelativistic Coulomb limit.
- No retained static-source hydrogen claim.
- No full precision hydrogen spectroscopy.
- No proton mass, reduced-mass, fine-structure, Lamb-shift, hyperfine, helium,
  or many-body atomic closure.
- No use of observed Rydberg, observed `m_e`, or observed `alpha(0)` as proof
  inputs.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_static_source_rydberg_closure_discriminator.py
```

The verifier checks the closure predicate, the comparator arithmetic, the
high-energy-alpha substitution firewall, the static-source versus full
spectroscopy split, the primitive-registry boundary, the no-go discipline
section, and the explicit non-claims.
