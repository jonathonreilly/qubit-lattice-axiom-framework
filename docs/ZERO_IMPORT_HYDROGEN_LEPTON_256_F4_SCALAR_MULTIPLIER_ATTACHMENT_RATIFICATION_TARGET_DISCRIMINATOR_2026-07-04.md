# Zero-Import Hydrogen: Lepton `1/256` F4 Scalar-Multiplier Attachment Ratification Target Discriminator

**Date:** 2026-07-04
**Type:** partial discriminator / attachment target
**Claim type:** conditional source-action attachment support
**Status:** support-only. This note does not ratify F4, does not ratify F,
does not derive retained `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_f4_scalar_multiplier_attachment_ratification_target_discriminator.py`

## Scope

The F-clause source/action assembly discriminator decomposed F into:

| subinput | content |
|---|---|
| F1 | source-coupled local-action convention |
| F2 | charged-lepton sector specificity |
| F3 | full OS0-cell tensor source locality |
| F4 | scalar-multiplier attachment to the D17 block, not a direct product unit vector over `2 * 256` components |

This note attacks only F4. F2 selects the charged-lepton D17 scalar block, and
F3 supplies the target full-cell source carrier. F4 is the attachment rule that
keeps the D17 block as a fixed scalar multiplier on the full-cell source
family.

The existing D17/full-cell separability and source-coupled attachment support
notes prove finite conditionals. They do not ratify F4 as a physical
charged-lepton source/action premise.

## Conditional F4 Target

F4 is supplied if the framework derives or explicitly ratifies the following
attachment target:

```text
B_lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R,
J(j) = sum_{c in C} j_c O_c,
S_lep[j] = h * B_lep * J(j),
dS_lep/dj_c = h * B_lep * O_c.
```

The target inputs are:

| input | content |
|---|---|
| D17_BLOCK | the charged-lepton scalar block `B_lep` and its `1/sqrt(2)` normalization are available |
| FULL_CELL_SOURCE | the source family has `C = {0,1,2,3}^4` and `256` matrix-unit controls |
| SCALAR_MULTIPLIER | `J(j)` multiplies `B_lep` as a scalar source factor |
| BLOCK_PRESERVATION | the D17 two-component block is fixed and not replaced by `512` independent product weights |
| RATIFICATION | the scalar-multiplier attachment is derived or explicitly ratified for framework use |

All five inputs close the narrow F4 target conditionally:

```text
D17_BLOCK + FULL_CELL_SOURCE + SCALAR_MULTIPLIER + BLOCK_PRESERVATION + RATIFICATION
  -> S_lep[j] = h * B_lep * sum_c j_c O_c
  -> dS_lep/dj_c = h * B_lep * O_c.
```

Every one-input-removed target fails:

| missing input | witness | result |
|---|---|---|
| no D17_BLOCK | full-cell source only | no charged-lepton scalar block |
| no FULL_CELL_SOURCE | D17 singlet only | no `256` source carrier |
| no SCALAR_MULTIPLIER | direct product unit vector over `2 * 256` components | coefficient class `(1/sqrt(2))*(1/16)`, not separated `1/256` source weights |
| no BLOCK_PRESERVATION | arbitrary product weights `u_{alpha,c}` | `512` free weights double-count the D17 block |
| no RATIFICATION | the rule remains a candidate convention | no retained premise for F |

## Finite Checks

The D17 block is normalized inside the stated charged-lepton scalar block:

```text
sum_alpha |1/sqrt(2)|^2 = 1.
```

The full-cell source carrier has `256` source coordinates:

```text
|C| = 4^4 = 256.
```

The direct product unit-vector shortcut has `512` components:

```text
2 * 256 = 512,
1/sqrt(512) = (1/sqrt(2)) * (1/16).
```

The scalar-multiplier route keeps the D17 block fixed and leaves source
weights on `C`:

```text
w_c = 1/256  =>  coefficient(alpha,c) = (1/sqrt(2))*(1/256).
```

The last line is not an A2 derivation. It is the F4 attachment target after a
later source-density theorem supplies `w_c = 1/256`.

## What This Moves

| before this note | after this note |
|---|---|
| F4 was named only as scalar-multiplier attachment. | F4 is narrowed to a ratifiable attachment target: D17 block, full-cell source, scalar multiplication, D17 block preservation, and explicit ratification or retained derivation. |
| D17/full-cell separability was a support note outside the F sublane. | Its hydrogen-facing use is isolated: it supports F4 only after physical scalar-multiplier attachment is supplied. |
| The `512` product-vector route could be mistaken for the desired source factor. | It is separated as a one-input-removed witness that gives the `1/16` unit-amplitude class, not the `1/256` source-density class. |

The F4 scalar-multiplier attachment current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
`F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED`. The positive route remains a
retained derivation or owner/audit acceptance of the scalar-multiplier
attachment target.

If F4 is ratified, F still needs F1 source-coupled local action, F2
charged-lepton sector specificity, and F3 full-cell tensor source locality.
All four are needed before F can be treated as supplied.

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md` | bounded charged-lepton scalar singlet and `1/sqrt(2)` block normalization | no full-cell carrier or source/action attachment |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md` | compatibility of a supplied scalar source multiplier with D17 normalization and `256` weights | does not prove F4 as physical attachment |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md` | conditional derivative `dS_lep/dj_c = h * B_lep * O_c` after source-coupled convention and lepton-specific full-cell source are supplied | does not ratify F1, F3, or F4 |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md` | direct product unit-vector firewall: `2 * 256 = 512` gives `(1/sqrt(2))*(1/16)` | no positive scalar-multiplier theorem |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md` | D17 block-selector target | no F4 attachment ratification |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md` | full-cell source-locality target | no D17 scalar-multiplier attachment |
| `MINIMAL_AXIOMS_2026-06-29.md` | one-site `M_2(C)` possibility algebra | no source/action bridge, selector, weighting, normalization, or mass value |
| approved primitives | OS0 kinetic-form isotropy, scale reference, realized-state discipline | no charged-lepton source/action attachment theorem, selector, readout bridge, dynamics, mass value, or empirical match |

The primitive registry was checked with the current origin-main methodology.
Registered primitives chain-satisfy their declared dependencies, but they do
not supply F4, F, L, P, R, A3, `m_e`, `alpha(0)`, or hydrogen.

## Current Open PR Alignment

Open PRs were checked on 2026-07-04 after `origin/main` was refreshed and
after `#4992` through `#4995` appeared. The moving review surface does not
close the F4 scalar-multiplier attachment target:

| PR | state at refresh | effect on this F4 lane |
|---|---:|---|
| `#4995` theta retirement-basis re-match | `CLEAN` | theta winding-account governance/rematch context; no charged-lepton scalar-multiplier attachment |
| `#4994` record-instrument polar contrast stabilization | `CLEAN` | numerical record/instrument robustness repair; no F4 attachment theorem |
| `#4993` DELTA0 route inventory sibling-total refresh | `CLEAN` | stale route-inventory total repair; no D17/full-cell attachment theorem |
| `#4992` g_bare two-Ward scope repair | `CLEAN` | keeps `g_bare = 1` conditional on residue normalization; no lepton source/action attachment |
| `#4991` owner-governed Tier-A retirement | `CLEAN` | governance retirement of live Tier-A admissions; no source-side hydrogen theorem |
| `#4990` Tier-A residual owner decision packet | `CLEAN` | proposal-only governance packet; no F4 closure |
| `#4989` Tier-A residual governance readiness packet | `CLEAN` | governance readiness context; no scalar-multiplier theorem |
| `#4988` theta G2 registration stretch no-go | `CLEAN` | theta physical sector/readout registration remains open; no lepton F4 attachment theorem |
| `#4987` theta G4 theta-bar assembly no-go | `CLEAN` | theta assembly hygiene; no charged-lepton source/action attachment |
| `#4986` AC R-eta h-class stretch no-go | `CLEAN` | AC/R-eta h-class pruning; no F4 closure |
| `#4985` AC R-eta h-unit primitive no-go | `CLEAN` | primitive-registry methodology context; no D17/full-cell scalar multiplier |

Merge-state labels are moving review metadata, not proof inputs here.

## No-Go Discipline Gate

This section prevents overclaiming. The broad retained-F4 claim is **not**
shipped. The narrowed claim is:

```text
If D17_BLOCK, FULL_CELL_SOURCE, SCALAR_MULTIPLIER, BLOCK_PRESERVATION, and
RATIFICATION are supplied, F4 conditionally supplies the scalar-multiplier
attachment target; every one-input-removed F4 target fails.
```

Verdict tag: broad F4 retention not shipped; narrowed F4 attachment target
supported conditionally.

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full F4 target | Supply D17 block, full-cell source, scalar multiplication, D17 block preservation, and ratification. | SUPPORTED CONDITIONALLY. It gives `S_lep[j] = h * B_lep * J(j)`. |
| direct product unit-vector route | Unit-normalize over `2 * 256` components. | ATTEMPTED. It gives `(1/sqrt(2))*(1/16)`, not separated source-density weights. |
| arbitrary product-weight route | Let every `(alpha,c)` have an independent coefficient. | ATTEMPTED. It creates `512` free weights and double-counts the D17 block. |
| D17-only route | Use the scalar singlet without full-cell source directions. | ATTEMPTED. It gives `1/sqrt(2)` but no `256` source carrier. |
| full-cell-only route | Use OS0 full-cell source without the D17 block. | ATTEMPTED. It gives `256` coordinates but no charged-lepton scalar block. |
| source-coupled derivative route | Use `dS_lep/dj_c = h * B_lep * O_c`. | PARTIAL POSITIVE. It supports F4 after F1 and F3 are supplied; it does not ratify them. |
| approved-primitive shortcut | Appeal to minimal axioms or approved primitives for F4. | RULED OUT AS CLOSURE by registry-limited scope. They do not supply source/action attachment or readout. |
| latest open PR shortcut | Treat `#4985` through `#4995` as new F4 science. | ATTEMPTED. They are theta, record/instrument, DELTA0, `g_bare`, AC/R-eta, or governance surfaces; none ratifies the D17/full-cell scalar multiplier. |

### N2 - Wall-Independence Audit

The collapsed F4 wall set is:

```text
D17_BLOCK + FULL_CELL_SOURCE + SCALAR_MULTIPLIER + BLOCK_PRESERVATION + RATIFICATION.
```

Pairwise independence:

| pair | closes automatically? | conclusion |
|---|---|---|
| D17_BLOCK <-> FULL_CELL_SOURCE | no | block uniqueness does not supply source locality, and source locality does not choose the lepton block |
| D17_BLOCK <-> SCALAR_MULTIPLIER | no | sector specificity does not choose separated multiplication |
| D17_BLOCK <-> BLOCK_PRESERVATION | no | the block can be selected and still be double-counted in a product vector |
| FULL_CELL_SOURCE <-> SCALAR_MULTIPLIER | no | carrier count does not choose how it attaches |
| FULL_CELL_SOURCE <-> BLOCK_PRESERVATION | no | `256` coordinates do not rule out `512` product weights |
| SCALAR_MULTIPLIER <-> RATIFICATION | no | formal multiplication can remain an unratified convention |

### N3 - Hidden-Wall Scan

| term | status |
|---|---|
| `B_lep` | explicit D17 block gate |
| `J(j)` / `O_c` | explicit full-cell source gate |
| `scalar multiplier` | explicit F4 attachment gate |
| `512` / `1/16` | explicit product-vector firewall |
| `1/256` | only a later source-density value, not an F4 derivation |

No attachment, product-normalization, or readout premise is left as background.

### N4 - Residual Matching

| source | claimed support | matched residual | counted? |
|---|---|---|---|
| D17 scalar-singlet theorem | `B_lep` and `1/sqrt(2)` | D17_BLOCK | yes |
| D17/full-cell separability support | scalar multiplier preserves D17 normalization and `256` weights | SCALAR_MULTIPLIER/BLOCK_PRESERVATION compatibility | yes, conditional |
| source-coupled attachment support | derivative attachment after F1/F3 inputs | F4 target consequence | yes, conditional |
| tensor-lift firewall | direct product gives `1/16` class | no-SCALAR_MULTIPLIER witness | yes, boundary |
| F2 selector discriminator | charged-lepton block target | D17_BLOCK context | no; sibling support only |
| F3 source-locality discriminator | full-cell source-locality target | FULL_CELL_SOURCE context | no; sibling support only |
| `#4985` through `#4995` | theta, record/instrument, DELTA0, `g_bare`, AC/R-eta, and governance residuals | F4 attachment target | no; review context only |

Only matching F4 residuals are counted as support.

### N5 - Rhetoric Audit

The negative phrase used here is narrow: "one-input-removed F4 targets fail."
The note does not say F4 is impossible, does not say F is retained, and does
not say `S_l = 1/256` is retained. The positive phrase is conditional:
"supported conditionally."

### N6 - Partial-Closure Path Scan

| partial path | closes F4? | remaining wall |
|---|---|---|
| D17 + source-coupled action | no | full-cell source locality and ratification |
| D17 + full-cell source | no | scalar-multiplier attachment and block preservation |
| full-cell source + scalar multiplier | no | D17 charged-lepton block |
| scalar multiplier + block preservation | no | physical source family and ratification |
| source-coupled attachment support | no | F1 and F3 remain prerequisites |

### N7 - Steelman

A hostile reviewer can argue that F4 is already supplied by the source-coupled
attachment note: once `S_lep[j] = h * B_lep * J(j)` is written, the scalar
multiplier is present. This note accepts the finite consequence but rejects
retention. The source-coupled note is conditional on the local-action
convention and lepton-specific full-cell source. F4 therefore needs retained
derivation or explicit ratification before F can close.

### N8 - Cross-Cycle Echo

Earlier lanes overclaimed when a finite support calculation was mistaken for
retained source/readout authority. The same error would occur here if D17
separability were treated as physical attachment. This note therefore ships as
F4 ratification-target support only.

## Acceptance Checklist

- Finite direct-product shortcut isolated: `2 * 256 = 512` gives
  `(1/sqrt(2))*(1/16)`.
- Separated scalar-multiplier target isolated:
  `S_lep[j] = h * B_lep * J(j)`.
- F4 remains unratified.
- No derivation or ratification of F4.
- No derivation or ratification of F1, F2, or F3.
- No derivation or ratification of F.
- No derivation that `S_l = 1/256` is retained.
- No derivation of the `256.082435...` precision correction.
- No derivation of the Koide/electron branch or physical `m_e`.
- No derivation of `alpha(0)` or hydrogen spectroscopy.
- No use of latest open PRs as proof inputs.
- No new axiom, primitive, or admitted import.
- No audit status change for any cited row.
