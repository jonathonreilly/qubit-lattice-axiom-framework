# Zero-Import Hydrogen: Lepton `1/256` F2 Charged-Lepton Source-Block Selector Current-Surface No-Go

**Date:** 2026-07-05
**Type:** current-surface no-go / import-retirement target
**Status:** support-only. This note does not ratify F2, does not ratify F,
does not derive retained `S_l = 1/256`, does not derive `m_e`, does not derive
`alpha(0)`, and does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_f2_charged_lepton_source_block_selector_current_surface_no_go.py`

## Scope

The F-clause handoff needs the second source/action subinput:

```text
F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED.
```

The F2 charged-lepton source-block selector discriminator gives the positive
route:

```text
D17 + SECTOR + SCALAR + ATTACHMENT
  -> the F source block is B_lep
  -> the F block anchor is 1/sqrt(2).
```

Current Lane 6 surfaces supply meaningful support: the D17 bounded scalar
singlet theorem, the F2 selector discriminator, the full-cell source-carrier
support, the D17/full-cell separability support, and the source-coupled
attachment support. They do not supply retained F2. The narrow result is not
"F2 cannot be retained." The narrow result is that current retained, primitive,
and open-PR surfaces do not supply
`F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED`.

## F2 Contract

A future retained F2 handoff needs the selector inputs plus the normal review
controls:

```text
D17_SCALAR_BLOCK
CHARGED_LEPTON_SECTOR_RESTRICTION
SCALAR_SINGLET_SCOPE
SOURCE_BLOCK_ATTACHMENT
NO_NEW_PRIMITIVE_OR_AXIOM
NO_EMPIRICAL_COMPARATOR_INPUT
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

If accepted, the conditional consequence would be:

```text
F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED
B_lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R
Z_lep^2 = N_c N_iso = 1 * 2 = 2
the F source block is B_lep.
```

That consequence is not supplied here. The D17 note supplies the bounded
scalar-singlet block inside its declared inputs, but current surfaces still do
not supply a retained decision that the physical F source family is restricted
to that charged-lepton block and attached as the source block in F. The current
missing inputs include:

```text
CHARGED_LEPTON_SECTOR_RESTRICTION
SOURCE_BLOCK_ATTACHMENT
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

F2 supplies only the charged-lepton source-block selector. It does not supply
the F1 source/action insertion convention, full-cell tensor source locality,
scalar-multiplier attachment, source-strength normalization, or the `S_l`
readout identity.

## Finite Target Arithmetic

The retained F2 target would license the D17 block as the block sourced in F:

```text
N_c = 1
N_iso = 2
Z_lep^2 = N_c N_iso = 2
B_lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R.
```

The one-input-removed witnesses remain load-bearing guards:

```text
no D17: a lepton label alone does not supply the normalized scalar singlet
no SECTOR: a full-cell source carrier can be regulator-generic
no SCALAR: triplet or tilde-H channels are outside the stated D17 scalar block
no ATTACHMENT: D17 alone gives a bounded scalar block, not a source/action family
```

These witnesses show why the D17 theorem can be positive support without
already being retained F2.

## Current-Surface Audit

| surface | supplies | does not supply |
|---|---|---|
| `LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md` | bounded D17 charged-lepton scalar singlet and `Z_lep^2 = 2` under stated block inputs | retained F2 source-block selector |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md` | F2 target: D17, SECTOR, SCALAR, ATTACHMENT | current retained F2 |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md` | F-level current-surface non-supply boundary | retained F2 subinput |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md` | F1-F4 assembly target and one-input-removed witnesses | retained F2 or F |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md` | conditional derivative attachment after source-coupled convention and lepton-specific full-cell source are supplied | proof that the source family is restricted to the D17 block |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md` | conditional `4^4 = 256` carrier if full-cell source locality is supplied | charged-lepton sector selector |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md` | D17 compatibility with a supplied full-cell scalar source multiplier | physical source-block selector |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md` | sibling F1 current-surface non-supply boundary | charged-lepton D17 source-block selector |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md` | sibling F3 full-cell source-locality target | F2 source-block selector |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md` | sibling F4 scalar attachment target | F2 source-block selector |
| approved primitives | minimal axioms, scale reference, kinetic-form isotropy, realized-state evaluation discipline | charged-lepton source-block selector, source/action bridge, normalization, `S_l`, mass, or empirical match |

The primitive registry was checked with the current origin-main methodology.
No registered primitive supplies `charged_lepton_source_block_selector_primitive`,
`d17_source_block_selector_primitive`, `sector_restriction_primitive`,
`scalar_singlet_source_block_primitive`, `source_block_attachment_primitive`,
`f_clause_primitive`, `source_probe_interface_primitive`, or
`electron_mass_primitive`.

## Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC. The newest rows are clean and green,
but they do not close the F2 handoff:

| PR | state at refresh | F2 effect |
|---|---:|---|
| `#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS` | theta gauge-side work; no charged-lepton D17 source-block selector |
| `#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS` | adjacent chirality science; no F2 source-block ratification |
| `#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS` | runner stabilization; no charged-lepton source-block selector |
| `#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS` | diagnostic repair; no charged-lepton F2 clause |
| `#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS` | bounded S3 support context; no D17 source-block selector |
| `#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS` | quark context; no charged-lepton D17 source family |
| `#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS` | Koide/electron route support, not F2 source-block closure |
| `#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS` | static-source hygiene; no charged-lepton F2 clause |
| `#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS` | governance/status progress, not an F2 theorem |

Merge-state labels are moving review metadata, not proof inputs.

## What This Moves

| before this note | after this note |
|---|---|
| F2 had a target discriminator but no dedicated current-surface non-supply boundary | the current retained, primitive, and open-PR gap for `F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED` is explicit |
| F could treat the D17 bounded block as enough sector selection | F now points to the exact upstream source-block selector wall |
| exact-source closure could count F without tracking the second subinput | the D17 selector/attachment route is separated from F1, F3, F4, and L/P/R |

## No-Go Discipline Gate

This section prevents overclaiming. The broad F2 no-go is not shipped. The
narrowed claim is:

```text
the current retained, primitive, and open-PR surfaces do not supply
F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full F2 selector contract | Accept D17 scalar block, charged-lepton sector restriction, scalar-singlet scope, source-block attachment, no-new-primitive/no-comparator controls, owner ratification, and audit acceptance. | OPEN POSITIVE ROUTE. This would close F2, but the contract is not accepted here. |
| D17-only route | Use the D17 scalar-singlet theorem by itself. | ATTEMPTED. It gives the bounded block and `Z_lep^2 = 2`, but not a physical source family or retained F2 selector. |
| sector-label-only route | Say the source is charged-lepton without D17 block authority. | ATTEMPTED. A label does not supply the normalized scalar singlet or attachment as the F source block. |
| scalar-projection-only route | Use only the singlet/triplet discrimination. | ATTEMPTED. It rules out triplet and `tilde H` alternatives inside D17, but does not choose the physical source family. |
| attachment-only route | Attach a source block without D17 sector and scalar scope. | ATTEMPTED. Attachment without the D17 scalar block can source a generic regulator or wrong sector. |
| full-cell carrier route | Use `M_2(C)^tensor4` and `4^4 = 256`. | ATTEMPTED. That is F3 carrier support, not the charged-lepton D17 block selector. |
| D17/full-cell separability route | Use D17 compatibility with a supplied scalar multiplier. | ATTEMPTED. It presupposes source locality and attachment; it does not choose the F2 source block. |
| primitive shortcut | Treat approved primitives as supplying F2. | RULED OUT BY CURRENT METHODOLOGY. The registry supplies no charged-lepton source-block selector primitive. |
| open-PR shortcut | Treat current green PRs, especially `#5013`, `#5007`, or `#5006`, as F2 closure. | ATTEMPTED. They supply theta, Koide route, and static-source context, not F2 ratification. |
| empirical route | Use observed `m_W/256`, charged-lepton masses, or hydrogen spectroscopy to accept F2. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is target data, not proof input. |

### N2 - Wall-Independence Audit

D17 and SCALAR collapse into `D17_SCALAR_BLOCK`. The collapsed F2
current-surface wall set is:

```text
D17_SCALAR_BLOCK + CHARGED_LEPTON_SECTOR_RESTRICTION
  + SOURCE_BLOCK_ATTACHMENT + NO_NEW_PRIMITIVE_OR_AXIOM
  + NO_EMPIRICAL_COMPARATOR_INPUT + OWNER_RATIFICATION
  + AUDIT_ACCEPTANCE.
```

| pair | closes automatically? | conclusion |
|---|---|---|
| D17_SCALAR_BLOCK <-> CHARGED_LEPTON_SECTOR_RESTRICTION | no | a block theorem does not say the source family selects it |
| D17_SCALAR_BLOCK <-> SOURCE_BLOCK_ATTACHMENT | no | a block theorem does not attach itself as a source/action family |
| CHARGED_LEPTON_SECTOR_RESTRICTION <-> SOURCE_BLOCK_ATTACHMENT | no | sector restriction does not specify the normalized block unless attached |
| SOURCE_BLOCK_ATTACHMENT <-> OWNER_RATIFICATION | no | a support note can describe attachment without decision authority |
| NO_NEW_PRIMITIVE_OR_AXIOM <-> OWNER_RATIFICATION | no | avoiding primitive status is not owner acceptance |
| NO_EMPIRICAL_COMPARATOR_INPUT <-> AUDIT_ACCEPTANCE | no | excluding comparator data does not imply audit acceptance |
| OWNER_RATIFICATION <-> AUDIT_ACCEPTANCE | no | owner decision and audit acceptance are separate controls |

F1, F3, F4, L, P, R, A3, Koide/electron readout, and `alpha(0)` are downstream
or sibling walls, not F2 walls.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `D17`, `scalar-singlet`, `Z_lep^2 = 2` | cited bounded block authority, not retained F2 |
| `charged-lepton sector` | explicit selector input |
| `source-block attachment` | explicit selector input |
| `full-cell`, `M_2(C)^tensor4`, `256` | F3 context only, not F2 closure |
| `scalar multiplier` / `512` | F4 context only, not F2 closure |
| `registered` / `primitive` | registry checked; no shortcut exists |
| `S_l`, `m_e`, `alpha(0)`, `hydrogen` | downstream non-claims |

No sector selector, source/action rule, full-cell locality theorem, attachment
rule, source-strength normalization, readout identity, mass input, or atomic
result is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| D17 scalar-singlet note | bounded charged-lepton scalar block and `1/sqrt(2)` normalization | D17_SCALAR_BLOCK | yes, conditional |
| F2 selector discriminator | D17/SECTOR/SCALAR/ATTACHMENT target and one-input-removed witnesses | F2 handoff | yes |
| F-clause current-surface no-go | F1-F4 plus owner/audit non-supply boundary | F2 as second missing subinput | yes |
| F-clause assembly discriminator | F2 is one required F subinput | F2 target placement | yes |
| source-coupled attachment support | derivative attachment after F1 and lepton-specific full-cell source are supplied | ATTACHMENT context | yes, conditional boundary |
| full-cell source-carrier support | `256` carrier after full-cell source locality is supplied | F3, not F2 | no; review context only |
| D17/full-cell separability support | D17 compatibility with supplied full-cell scalar multiplier | F4/attachment boundary | boundary only |
| F1 current-surface no-go | source-coupled local-action non-supply boundary | F1, not F2 | no; sibling context only |
| current open PR surface | moving review context | no F2 closure | no closure; context only |
| primitive registry | approved primitive boundary | no F2 primitive | guard only |

Non-matching citations are not used as closure evidence.

### N5 - Rhetoric Audit

The negative phrase is narrow: "current surfaces do not supply
`F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED`."

| resolution | tested? | outcome |
|---|---:|---|
| D17 scalar-block level | yes | bounded support only |
| charged-lepton sector level | yes | support-only target, no retained selector |
| scalar-singlet channel level | yes | D17 rules out triplet and `tilde H` inside the stated block |
| source-block attachment level | yes | not supplied as retained F2 |
| F level | kept separate | also needs F1, F3, F4, owner/audit |
| source-side `S_l` level | kept separate | also needs L, P, R |
| hydrogen level | kept separate | no statement that hydrogen is impossible or retained |

No universal no-go against future F2 retention is claimed.

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| retained derivation that the charged-lepton scalar source family is restricted to the D17 scalar-singlet block | `F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED` |
| owner/audit acceptance of the charged-lepton source-block selector | F2 convention route |
| D17 bounded theorem plus an explicit retained source-family selector | D17_SCALAR_BLOCK and SECTOR |
| source-coupled attachment theorem upgraded with lepton-specific source-family authority | ATTACHMENT |
| equivalent retained charged-lepton source/action theorem | F2 and part of F |

These are import-retirement paths, not new-axiom requirements. Approved
primitives are chain-satisfied but do not supply the charged-lepton
source-block selector.

### N7 - Steelman

A hostile reviewer can argue that F2 should be automatic: D17 already names the
charged-lepton scalar-singlet block, the F clause is explicitly the
charged-lepton source/action family, and choosing any other block would change
the lane. That is the strongest positive route. This note preserves it, but
zero-import retained hydrogen cannot spend that route until owner/audit action
or a retained derivation makes the D17 source-block selector current retained
F2 content.

### N8 - Cross-Cycle Echo

This echoes earlier selector walls where a clean finite theorem did not by
itself supply the physical-license sentence that lets another lane spend it.
Those walls can be retired by deriving or ratifying the selector explicitly.
The same mechanism could retire F2: keep D17 as the bounded block theorem,
then derive or ratify the charged-lepton source-block selector. The disciplined
move here is to keep bounded D17 support, retained F2 status, retained F, exact
`S_l = 1/256`, and downstream hydrogen scale consumption separate until the
selector lands.

**Gate result:** broad F2 no-go fails; narrowed current-surface non-supply
claim passes.

## Explicit Non-Claims

- No derivation or ratification of `F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED`.
- No derivation or ratification of F2.
- No derivation or ratification of F.
- No derivation or ratification of F1, F3, or F4.
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
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_f2_charged_lepton_source_block_selector_current_surface_no_go.py
```

The verifier checks the current-surface boundary, F2 predicate, finite
one-input-removed witnesses, primitive registry, open PR alignment, No-Go
Discipline markers, and explicit non-claims.
