# Zero-Import Hydrogen: Lepton `1/256` F-Clause Current-Surface No-Go

**Date:** 2026-07-05
**Type:** current-surface no-go / import-retirement target
**Status:** support-only. This note does not ratify F1-F4, does not ratify the
F clause, does not derive retained `S_l = 1/256`, does not derive `m_e`, does
not derive `alpha(0)`, and does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_f_clause_current_surface_no_go.py`

## Scope

The exact source singleton route needs the first source-side subdecision:

```text
F_CLAUSE_RETAINED.
```

The F decision packet gives the positive handoff:

```text
F1 + F2 + F3 + F4 + six contract inputs
  -> F_CLAUSE_RETAINED
  -> S_lep[j] = h * B_lep * sum_{c in C} j_c O_c
  -> dS_lep/dj_c = h * B_lep * O_c.
```

Current Lane 6 surfaces supply meaningful support: the F-clause assembly
discriminator, F1/F2/F3/F4 target discriminators, D17/full-cell separability
support, and the source-coupled attachment support. They do not supply the
retained F clause. The narrow result is not "F cannot be retained." The narrow
result is that current retained, primitive, and open-PR surfaces do not supply
`F_CLAUSE_RETAINED`.

## F-Clause Contract

A future retained F handoff needs all four F subinputs and all six decision
contract inputs:

```text
F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED
F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED
F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED
F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED
F_CLAUSE_TEXT_LOCK
CHARGED_LEPTON_SCOPE_LOCK
NO_NEW_PRIMITIVE_OR_AXIOM
NO_EMPIRICAL_COMPARATOR_INPUT
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

If accepted, the conditional consequence would be:

```text
F_CLAUSE_RETAINED
S_lep[j] = h * B_lep * sum_{c in C} j_c O_c
dS_lep/dj_c = h * B_lep * O_c.
```

That consequence is not supplied here. The current missing inputs include:

```text
F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED
F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED
F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED
F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

The F clause is source/action support only. It does not supply L label-free
source-coordinate ratification, P positive projective source-strength
ratification, R `S_l` readout identity ratification, A3 precision placement,
Koide/electron readout, `alpha(0)`, or static-source Rydberg closure.

## Finite Target Arithmetic

The full F target is:

```text
B_lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R
C = {0,1,2,3}^4
|C| = 4^4 = 256
J(j) = sum_{c in C} j_c O_c
S_lep[j] = h * B_lep * J(j)
dS_lep/dj_c = h * B_lep * O_c.
```

The one-input-removed witnesses remain load-bearing guards:

```text
no F1: J(j) remains formal rather than a physical local source insertion
no F2: the source may be regulator-generic rather than charged-lepton-specific
no F3: slot-additive, diagonal, and scalar carriers have counts 16, 4, and 1
no F4: direct product unit normalization gives (1/sqrt(2))*(1/16)
```

The separated source-density target remains `1/256`; the direct product
unit-vector witness remains `1/16`. Those are different classes, so F4 cannot
be bypassed by product-vector normalization.

## Current-Surface Audit

| surface | supplies | does not supply |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md` | six-input owner/audit handoff for F1-F4 | current retained F clause |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md` | F1-F4 assembly target and one-input-removed witnesses | retained F1-F4 or F |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md` | F1 target: local action, linear source controls, derivative insertion, ratification | retained F1 |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary for F1 | retained F1 source/action convention |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md` | F2 target: D17 block, sector restriction, scalar block, attachment | retained F2 |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary for F2 | retained charged-lepton D17 source-block selector |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md` | F3 target: OS0 geometry, full-cell tensor source locality, independent controls, ratification | retained F3 |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary for F3 | retained full-cell tensor source-locality theorem |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md` | F4 target: D17 block, full-cell source, scalar multiplier, block preservation, ratification | retained F4 |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary for F4 | retained scalar-multiplier attachment theorem |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md` | outer F/L/P/R source-probe contract | F retained status |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md` | downstream exact-source boundary | F-clause retention |
| approved primitives | minimal axioms, scale reference, kinetic-form isotropy, realized-state evaluation discipline | source/action convention, charged-lepton source-block selector, full-cell source-locality theorem, scalar attachment, `S_l`, mass, or empirical match |

The primitive registry was checked with the current origin-main methodology.
No registered primitive supplies `source_action_convention_primitive`,
`charged_lepton_source_block_selector_primitive`,
`full_cell_source_locality_primitive`, `scalar_multiplier_attachment_primitive`,
`f_clause_primitive`, `source_probe_interface_primitive`, or
`electron_mass_primitive`.

## Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC. The newest rows are clean and
green, but they do not close the F-clause handoff:

| PR | state at refresh | F-clause effect |
|---|---:|---|
| `#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS` | theta gauge-side work; no charged-lepton source/action ratification |
| `#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS` | adjacent chirality science; no F1-F4 handoff |
| `#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS` | runner stabilization; no charged-lepton source/action convention |
| `#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS` | diagnostic repair; no charged-lepton F clause |
| `#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS` | bounded S3 support context; no F1-F4 ratification |
| `#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS` | quark context; no charged-lepton source/action family |
| `#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS` | Koide/electron route support, not source/action F closure |
| `#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS` | static-source hygiene; no charged-lepton F clause |
| `#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS` | governance/status progress, not an F1-F4 theorem |

Merge-state labels are moving review metadata, not proof inputs.

## What This Moves

| before this note | after this note |
|---|---|
| F had a decision packet but no dedicated current-surface non-supply boundary | the current retained, primitive, and open-PR gap for `F_CLAUSE_RETAINED` is explicit |
| exact-source closure could treat F as merely pending governance | F is separated into four scientific subinputs plus owner/audit controls |
| K4 could read the source-probe route as closer than it is | K4 now has an upstream F-specific wall before exact source singleton retention |

## No-Go Discipline Gate

This section prevents overclaiming. The broad F-clause no-go is not shipped.
The narrowed claim is:

```text
the current retained, primitive, and open-PR surfaces do not supply
F_CLAUSE_RETAINED.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full F decision contract | Accept F1-F4 and all six contract inputs. | OPEN POSITIVE ROUTE. This would close the F handoff, but the contract is not accepted here. |
| F1-only route | Use only the local-action derivative convention. | ATTEMPTED. It lacks charged-lepton block selection, full-cell source locality, and scalar attachment. |
| F2-only route | Use only the charged-lepton D17 scalar block selector. | ATTEMPTED. It lacks source/action convention, full-cell source locality, and attachment. |
| F3-only route | Use only the `4^4 = 256` full-cell carrier. | ATTEMPTED. It lacks the physical charged-lepton source convention, D17 block selection, and attachment. |
| F4-only route | Use only scalar-multiplier attachment. | ATTEMPTED. It presupposes F1-F3 and cannot stand alone. |
| exact arithmetic route | Use `4^4 = 256` or `1/256` directly. | ATTEMPTED. Arithmetic gives a target count, not source/action authority. |
| primitive shortcut | Treat approved primitives as supplying F source/action. | RULED OUT BY CURRENT METHODOLOGY. The registry supplies no such primitive. |
| open-PR shortcut | Treat current green PRs, especially `#5007` or `#5006`, as F closure. | ATTEMPTED. They supply Koide route context and static-source hygiene, not F1-F4 ratification. |
| empirical route | Use observed `m_W/256`, charged-lepton masses, or hydrogen spectroscopy to accept F. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is target data, not proof input. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| F1 <-> F2 | no | source/action convention does not select the charged-lepton D17 block |
| F1 <-> F3 | no | source/action convention does not supply full-cell tensor locality |
| F1 <-> F4 | no | source/action convention does not choose scalar attachment |
| F2 <-> F3 | no | charged-lepton block selection does not imply the `256` carrier |
| F2 <-> F4 | no | the D17 block does not choose separated source-density attachment |
| F3 <-> F4 | no | the full-cell carrier does not choose D17 block preservation |
| F_CLAUSE_TEXT_LOCK <-> OWNER_RATIFICATION | no | locked text can remain unaccepted |
| NO_EMPIRICAL_COMPARATOR_INPUT <-> AUDIT_ACCEPTANCE | no | excluding comparator data does not imply audit acceptance |

No F subinput is counted twice. L, P, R, A3, Koide/electron readout, and
`alpha(0)` are downstream walls, not F walls.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `source-coupled local-action` | explicit F1 gate |
| `charged-lepton` / `B_lep` | explicit F2 gate |
| `full OS0-cell` / `4^4 = 256` | explicit F3 gate |
| `scalar-multiplier attachment` | explicit F4 gate |
| `decision-ready` | contract status only, not decision authority |
| `registered` / `primitive` | registry checked; no shortcut exists |
| `S_l`, `m_e`, `alpha(0)`, `hydrogen` | downstream non-claims |

No source/action rule, sector selector, source-locality theorem, attachment
rule, source-strength normalization, readout identity, mass input, or atomic
result is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| F decision packet | six-input owner/audit contract for F1-F4 | F handoff | yes |
| F-clause assembly discriminator | F1-F4 formal assembly and one-input-removed witnesses | F target | yes |
| F1 target discriminator | source-coupled local-action insertion convention | F1 | yes |
| F1 current-surface no-go | source-coupled local-action non-supply boundary | first F subinput wall | yes |
| F2 target discriminator | D17 charged-lepton source-block selector | F2 | yes |
| F2 current-surface no-go | charged-lepton D17 source-block selector non-supply boundary | second F subinput wall | yes |
| F3 target discriminator | full-cell tensor source-locality target | F3 | yes |
| F3 current-surface no-go | full-cell tensor source-locality non-supply boundary | third F subinput wall | yes |
| F4 target discriminator | scalar-multiplier attachment target | F4 | yes |
| F4 current-surface no-go | scalar-multiplier attachment non-supply boundary | fourth F subinput wall | yes |
| source-probe decision packet | outer F/L/P/R source-side contract | F placement | yes for placement only |
| exact source singleton no-go | downstream exact-source non-supply | F as upstream missing subdecision | yes |
| current open PR surface | moving review context | no F closure | no closure; context only |
| primitive registry | approved primitive boundary | no F primitive | guard only |

Non-matching citations are not used as closure evidence.

### N5 - Rhetoric Audit

The negative phrase is narrow: "current surfaces do not supply
`F_CLAUSE_RETAINED`."

| resolution | tested? | outcome |
|---|---:|---|
| F1 local-action level | yes | support-only |
| F2 charged-lepton block level | yes | support-only |
| F3 full-cell source-locality level | yes | support-only |
| F4 scalar attachment level | yes | support-only |
| F/L/P/R source-probe level | kept separate | also needs L, P, R, owner/audit |
| exact source singleton level | kept separate | also needs the full source-probe decision |
| hydrogen level | kept separate | no statement that hydrogen is impossible or retained |

No universal no-go against future F retention is claimed.

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| owner/audit acceptance or retained derivation of the F1 source/action convention | local source insertion convention |
| retained F1 derivation or ratification | local source insertion convention |
| retained F2 derivation or ratification | charged-lepton D17 source-block selector |
| owner/audit acceptance of the F2 charged-lepton source-block selector | charged-lepton D17 source-block selector |
| retained F3 derivation or ratification | full-cell tensor source-locality theorem |
| owner/audit acceptance of the full-cell tensor source-locality target | full-cell tensor source-locality theorem |
| retained F4 derivation or ratification | separated scalar-multiplier attachment |
| owner/audit acceptance of the scalar-multiplier attachment target | separated scalar-multiplier attachment |
| owner/audit acceptance of the F decision packet | `F_CLAUSE_RETAINED` |
| equivalent retained source/action theorem | F without convention adoption |

These are import-retirement paths, not new-axiom requirements.

### N7 - Steelman

A hostile reviewer can argue that F is almost closed already: source-coupled
action is a standard physics convention, D17 supplies the charged-lepton scalar
block, OS0 gives the `4^4 = 256` full-cell carrier, and the scalar attachment
is just bookkeeping. That is the strongest positive route. This note preserves
it, but zero-import retained hydrogen cannot spend the route until the four
F subinputs and owner/audit contract make the F clause current retained content.

### N8 - Cross-Cycle Echo

This echoes the previous source-chain pattern: a clean finite target can be
available before the physical readout is retained. F sits before L/P/R and
before exact source singleton retention. The disciplined move here is to keep
source/action assembly, retained F status, exact `S_l = 1/256`, and downstream
hydrogen-scale consumption separate until the relevant contracts land.

**Gate result:** broad F-clause no-go fails; narrowed current-surface
non-supply claim passes.

## Explicit Non-Claims

- No derivation or ratification of `F_CLAUSE_RETAINED`.
- No derivation or ratification of F1-F4.
- No derivation or ratification of L, P, or R.
- No derivation that `S_l = 1/256` is retained.
- No derivation of A3 precision placement, `C_A3`, or `N_A3`.
- No derivation of the Koide/electron branch or physical `m_e`.
- No derivation of `alpha(0)`, static-source Rydberg, or hydrogen spectroscopy.
- No use of observed `m_W`, observed charged-lepton masses, fitted `a_l`,
  fitted `N_A3`, or hydrogen spectroscopy as proof inputs.
- No audit status change for any cited row.
- No new axiom, primitive, Tier-A admission, or empirical import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_f_clause_current_surface_no_go.py
```

The verifier checks the current-surface boundary, F predicate, finite
one-input-removed witnesses, primitive registry, open PR alignment, No-Go
Discipline markers, and explicit non-claims.
