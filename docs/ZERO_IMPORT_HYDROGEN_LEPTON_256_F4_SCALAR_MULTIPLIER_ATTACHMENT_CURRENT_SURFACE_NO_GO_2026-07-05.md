# Zero-Import Hydrogen: Lepton `1/256` F4 Scalar-Multiplier Attachment Current-Surface No-Go

**Date:** 2026-07-05
**Type:** current-surface no-go / import-retirement target
**Status:** support-only. This note does not ratify F4, does not ratify F,
does not derive retained `S_l = 1/256`, does not derive `m_e`, does not derive
`alpha(0)`, and does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_f4_scalar_multiplier_attachment_current_surface_no_go.py`

## Scope

The F-clause handoff needs the fourth source/action subinput:

```text
F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED.
```

The F4 scalar-multiplier attachment target gives the positive route:

```text
D17_BLOCK + FULL_CELL_SOURCE + SCALAR_MULTIPLIER
  + BLOCK_PRESERVATION + RATIFICATION
  -> S_lep[j] = h * B_lep * J(j)
  -> dS_lep/dj_c = h * B_lep * O_c.
```

Current Lane 6 surfaces supply meaningful support: the D17 scalar block,
D17/full-cell separability, source-coupled attachment, tensor-lift firewall,
and the F4 target discriminator. They do not supply retained F4. The narrow
result is not "F4 cannot be retained." The narrow result is that current
retained, primitive, and open-PR surfaces do not supply
`F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED`.

## F4 Contract

A future retained F4 handoff needs the attachment inputs plus the normal review
controls:

```text
D17_BLOCK
FULL_CELL_SOURCE
SCALAR_MULTIPLIER_ATTACHMENT
D17_BLOCK_PRESERVATION
NO_DIRECT_PRODUCT_UNIT_NORMALIZATION
NO_NEW_PRIMITIVE_OR_AXIOM
NO_EMPIRICAL_COMPARATOR_INPUT
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

If accepted, the conditional consequence would be:

```text
F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED
B_lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R
J(j) = sum_{c in C} j_c O_c
S_lep[j] = h * B_lep * J(j)
dS_lep/dj_c = h * B_lep * O_c.
```

That consequence is not supplied here. The current missing inputs include:

```text
SCALAR_MULTIPLIER_ATTACHMENT
D17_BLOCK_PRESERVATION
NO_DIRECT_PRODUCT_UNIT_NORMALIZATION
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

F4 supplies only the attachment rule between the D17 block and the full-cell
source carrier. It does not supply the F1 source/action insertion convention,
the F2 charged-lepton D17 source-block selector, the F3 full-cell source
locality theorem, source-strength normalization, or the `S_l` readout identity.

## Finite Target Arithmetic

The retained F4 target would license separated scalar-multiplier attachment:

```text
sum_alpha |1/sqrt(2)|^2 = 1
|C| = 4^4 = 256
w_c = 1/256
coefficient(alpha,c) = (1/sqrt(2))*(1/256).
```

The one-input-removed witnesses remain load-bearing guards:

```text
no D17_BLOCK: full-cell source only has no charged-lepton scalar block
no FULL_CELL_SOURCE: D17 singlet only has no 256 source carrier
no SCALAR_MULTIPLIER_ATTACHMENT: direct product unit vector gives (1/sqrt(2))*(1/16)
no D17_BLOCK_PRESERVATION: arbitrary product weights u_{alpha,c} create 512 free weights
no RATIFICATION: the scalar-multiplier rule remains a candidate convention
```

These witnesses show why exact D17/full-cell compatibility can be positive
support without already being retained F4.

## Current-Surface Audit

| surface | supplies | does not supply |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md` | F4 target: D17 block, full-cell source, scalar multiplier, block preservation, ratification | current retained F4 |
| `LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md` | bounded charged-lepton scalar singlet and `1/sqrt(2)` block normalization | full-cell carrier or source/action attachment |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md` | compatibility of a supplied scalar source multiplier with D17 normalization and `256` weights | proof of F4 as physical scalar-multiplier attachment |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md` | conditional derivative `dS_lep/dj_c = h * B_lep * O_c` after source-coupled convention and lepton-specific full-cell source are supplied | retained F1, F3, or F4 |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md` | direct product unit-vector firewall: `2 * 256 = 512` gives `(1/sqrt(2))*(1/16)` | positive scalar-multiplier theorem |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md` | sibling F1 current-surface non-supply boundary | scalar-multiplier attachment |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md` | sibling F2 current-surface non-supply boundary | scalar-multiplier attachment |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md` | sibling F3 current-surface non-supply boundary | scalar-multiplier attachment |
| approved primitives | minimal axioms, scale reference, kinetic-form isotropy, realized-state evaluation discipline | scalar-multiplier attachment theorem, block-preservation rule, source/action bridge, `S_l`, mass, or empirical match |

The primitive registry was checked with the current origin-main methodology.
No registered primitive supplies `scalar_multiplier_attachment_primitive`,
`source_action_attachment_primitive`, `d17_block_preservation_primitive`,
`direct_product_unit_normalization_firewall_primitive`, `f4_attachment_primitive`,
`f_clause_primitive`, `source_probe_interface_primitive`, or
`electron_mass_primitive`.

## Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC. The newest rows are clean and green,
but they do not close the F4 handoff:

| PR | state at refresh | F4 effect |
|---|---:|---|
| `#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS` | theta gauge-side work; no scalar-multiplier attachment theorem |
| `#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS` | adjacent chirality science; no F4 attachment ratification |
| `#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS` | runner stabilization; no D17/full-cell scalar multiplier |
| `#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS` | diagnostic repair; no F4 clause |
| `#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS` | bounded S3 support context; no scalar-multiplier attachment theorem |
| `#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS` | quark context; no charged-lepton scalar attachment |
| `#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS` | Koide/electron route support, not F4 attachment closure |
| `#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS` | static-source hygiene; no charged-lepton F4 clause |
| `#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS` | governance/status progress, not an F4 theorem |

Merge-state labels are moving review metadata, not proof inputs.

## What This Moves

| before this note | after this note |
|---|---|
| F4 had a ratification target discriminator but no dedicated current-surface non-supply boundary | the current retained, primitive, and open-PR gap for `F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED` is explicit |
| F could treat D17/full-cell separability as enough attachment | F now points to the exact upstream scalar-multiplier attachment wall |
| exact-source closure could count F without tracking the fourth subinput | the D17/full-cell attachment route is separated from F1, F2, F3, and L/P/R |

## No-Go Discipline Gate

This section prevents overclaiming. The broad F4 no-go is not shipped. The
narrowed claim is:

```text
the current retained, primitive, and open-PR surfaces do not supply
F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full F4 attachment contract | Accept D17 block, full-cell source, scalar-multiplier attachment, block preservation, no-direct-product/no-comparator controls, owner ratification, and audit acceptance. | OPEN POSITIVE ROUTE. This would close F4, but the contract is not accepted here. |
| direct product unit-vector route | Unit-normalize over `2 * 256` components. | ATTEMPTED. It gives `(1/sqrt(2))*(1/16)`, not separated source-density weights. |
| arbitrary product-weight route | Let every `(alpha,c)` have an independent coefficient. | ATTEMPTED. It creates `512` free weights and double-counts the D17 block. |
| D17-only route | Use the charged-lepton scalar singlet without full-cell source directions. | ATTEMPTED. It gives `1/sqrt(2)` but no `256` source carrier or attachment. |
| full-cell-only route | Use the OS0 full-cell source without the D17 block. | ATTEMPTED. It gives `256` coordinates but no charged-lepton scalar block. |
| source-coupled derivative route | Use `dS_lep/dj_c = h * B_lep * O_c`. | ATTEMPTED. It supports F4 after F1 and F3 are supplied; it does not ratify those prerequisites or F4. |
| F1/F2/F3 sibling shortcut | Treat local action, D17 block selection, or full-cell locality as enough for F4. | ATTEMPTED. They are separate F walls and do not choose scalar-multiplier attachment. |
| primitive shortcut | Treat approved primitives as supplying F4. | RULED OUT BY CURRENT METHODOLOGY. The registry supplies no scalar-multiplier attachment primitive. |
| open-PR shortcut | Treat current green PRs, especially `#5013`, `#5009`, `#5007`, or `#5006`, as F4 closure. | ATTEMPTED. They supply theta, S3, Koide route, and static-source context, not F4 ratification. |
| empirical route | Use observed charged-lepton masses, `m_W/256`, or hydrogen spectroscopy to accept F4. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is target data, not an attachment theorem. |

### N2 - Wall-Independence Audit

The collapsed F4 current-surface wall set is:

```text
D17_BLOCK + FULL_CELL_SOURCE + SCALAR_MULTIPLIER_ATTACHMENT
  + D17_BLOCK_PRESERVATION + NO_DIRECT_PRODUCT_UNIT_NORMALIZATION
  + NO_NEW_PRIMITIVE_OR_AXIOM + NO_EMPIRICAL_COMPARATOR_INPUT
  + OWNER_RATIFICATION + AUDIT_ACCEPTANCE.
```

| pair | closes automatically? | conclusion |
|---|---|---|
| D17_BLOCK <-> FULL_CELL_SOURCE | no | block uniqueness does not supply source locality, and source locality does not choose the lepton block |
| D17_BLOCK <-> SCALAR_MULTIPLIER_ATTACHMENT | no | sector specificity does not choose separated multiplication |
| D17_BLOCK <-> D17_BLOCK_PRESERVATION | no | the block can be selected and still be double-counted in a product vector |
| FULL_CELL_SOURCE <-> SCALAR_MULTIPLIER_ATTACHMENT | no | carrier count does not choose how it attaches |
| FULL_CELL_SOURCE <-> NO_DIRECT_PRODUCT_UNIT_NORMALIZATION | no | `256` coordinates do not rule out `512` product weights |
| SCALAR_MULTIPLIER_ATTACHMENT <-> D17_BLOCK_PRESERVATION | no | formal multiplication still needs block-preservation authority |
| NO_NEW_PRIMITIVE_OR_AXIOM <-> OWNER_RATIFICATION | no | avoiding primitive status is not owner acceptance |
| NO_EMPIRICAL_COMPARATOR_INPUT <-> AUDIT_ACCEPTANCE | no | excluding comparator data does not imply audit acceptance |
| OWNER_RATIFICATION <-> AUDIT_ACCEPTANCE | no | owner decision and audit acceptance are separate controls |

F1, F2, F3, L, P, R, A3, Koide/electron readout, and `alpha(0)` are downstream
or sibling walls, not F4 walls.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `B_lep`, `D17`, `1/sqrt(2)` | cited bounded block support, not retained F4 |
| `J(j)`, `O_c`, `full-cell` | explicit full-cell source input, not attachment |
| `scalar multiplier`, `block preservation` | explicit F4 target |
| `512`, `1/16`, `direct product` | explicit firewall and one-input-removed witness |
| `1/256` | later source-density value, not derived by F4 |
| `registered` / `primitive` | registry checked; no shortcut exists |
| `S_l`, `m_e`, `alpha(0)`, `hydrogen` | downstream non-claims |

No scalar attachment, block-preservation rule, source/action convention,
readout identity, mass input, or atomic result is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| F4 target discriminator | D17/FULL_CELL/SCALAR/BLOCK/RATIFICATION target and one-input-removed witnesses | F4 handoff | yes |
| D17 scalar-singlet theorem | charged-lepton scalar block and `1/sqrt(2)` normalization | D17_BLOCK | yes, conditional |
| D17/full-cell separability support | scalar multiplier preserves D17 normalization and `256` source weights after supplied inputs | SCALAR_MULTIPLIER_ATTACHMENT and D17_BLOCK_PRESERVATION compatibility | yes, conditional |
| source-coupled attachment support | derivative attachment after F1 and lepton-specific full-cell source are supplied | F4 target consequence | yes, conditional |
| tensor-lift firewall | direct product gives `(1/sqrt(2))*(1/16)` class | NO_DIRECT_PRODUCT_UNIT_NORMALIZATION witness | yes |
| F1 current-surface no-go | source-coupled local-action non-supply boundary | F1, not F4 | no; sibling context only |
| F2 current-surface no-go | charged-lepton D17 source-block selector non-supply boundary | F2, not F4 | no; sibling context only |
| F3 current-surface no-go | full-cell tensor source-locality non-supply boundary | F3, not F4 | no; sibling context only |
| current open PR surface | moving review context | no F4 closure | no closure; context only |
| primitive registry | approved primitive boundary | no F4 primitive | guard only |

Non-matching citations are not used as closure evidence.

### N5 - Rhetoric Audit

The negative phrase is narrow: "current surfaces do not supply
`F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED`."

| resolution | tested? | outcome |
|---|---:|---|
| D17 scalar-block level | yes | support only |
| full-cell source-carrier level | yes | support only |
| scalar-multiplier attachment level | yes | not supplied as retained F4 |
| D17 block-preservation level | yes | not supplied as retained F4 |
| direct product unit-vector level | yes | gives `(1/sqrt(2))*(1/16)`, not the separated source-density class |
| F level | kept separate | also needs F1, F2, F3, owner/audit |
| source-side `S_l` level | kept separate | also needs L, P, R |
| hydrogen level | kept separate | no statement that hydrogen is impossible or retained |

No universal no-go against future F4 retention is claimed.

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| retained derivation that the full-cell source multiplies the fixed D17 block as a scalar source factor | `F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED` |
| owner/audit acceptance of the scalar-multiplier attachment target | F4 convention route |
| D17/full-cell separability upgraded with physical attachment authority | SCALAR_MULTIPLIER_ATTACHMENT and D17_BLOCK_PRESERVATION |
| source-coupled attachment upgraded after retained F1 and F3 | derivative attachment for F4 |
| tensor-lift firewall retained as the product-unit exclusion while scalar multiplication is accepted | NO_DIRECT_PRODUCT_UNIT_NORMALIZATION |

The primitive registry was checked. Registered primitives are not walls, but
they also do not supply source/action, scalar attachment, block preservation,
weighting, normalization, readout bridge, dynamics, mass value, or empirical
match.

### N7 - Steelman

A hostile reviewer can argue that F4 is already supplied by the source-coupled
attachment support: once `S_lep[j] = h * B_lep * J(j)` is written and
`dS_lep/dj_c = h * B_lep * O_c` follows, scalar multiplication and block
preservation are present. The narrow reply is that the source-coupled support
is conditional on the local-action convention and a lepton-specific full-cell
source, while F4 still needs retained physical attachment authority or explicit
owner/audit acceptance before F can spend it.

### N8 - Cross-Cycle Echo

Earlier source/readout lanes overclaimed when a finite support calculation was
mistaken for retained physical source authority. The same mechanism could
retire F4: keep D17/full-cell separability and source-coupled attachment as
finite support, then derive or ratify the scalar-multiplier attachment target.
This note therefore ships as a current-surface non-supply boundary, not as a
broad no-go and not as a retained theorem.

## Explicit Non-Claims

- No derivation or ratification of `F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED`.
- No derivation or ratification of F4.
- No derivation or ratification of F.
- No derivation or ratification of F1, F2, or F3.
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
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_f4_scalar_multiplier_attachment_current_surface_no_go.py
```
