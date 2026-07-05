# Zero-Import Hydrogen: Lepton `1/256` F2 Charged-Lepton Source Block Selector Discriminator

**Date:** 2026-07-04
**Type:** partial discriminator / charged-lepton block-selector support
**Claim type:** conditional source-block selector support
**Status:** support-only. This note does not ratify F2, does not ratify F,
does not derive retained `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_f2_charged_lepton_source_block_selector_discriminator.py`

## Scope

The F-clause source/action assembly discriminator decomposed F into:

| subinput | content |
|---|---|
| F1 | source-coupled local-action convention |
| F2 | charged-lepton sector specificity |
| F3 | full OS0-cell tensor source locality |
| F4 | scalar-multiplier attachment |

In this decomposition, F2 charged-lepton sector specificity is the selector
that chooses the D17 charged-lepton scalar block as the block being sourced.

This note attacks only F2. It asks what must be supplied for the F source family
to use the charged-lepton D17 scalar block

```text
B_lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R
```

rather than a regulator-generic full-cell carrier, a quark/color block, a
triplet channel, or an unattached D17 scalar note.
This F2 selector does not supply F1.

## Conditional F2 Target

F2 is supplied if the source family is explicitly restricted to the D17
charged-lepton scalar-singlet block and that block is named as the block being
sourced in the F action family.

The finite target is:

```text
Z_lep^2 = N_c N_iso = 1 * 2 = 2,
B_lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R.
```

F2 contributes `B_lep` and the `1/sqrt(2)` D17 block anchor to F. It does not
contribute the `256` source carrier, the source/action convention, the
projective source-strength normalization, or the `S_l` readout identity.

## Selector Discriminator

The tested F2 selector inputs are:

| input | content |
|---|---|
| D17 | D17 charged-lepton scalar-singlet block authority |
| SECTOR | explicit charged-lepton sector restriction for the source family |
| SCALAR | singlet projection rather than triplet or `tilde H` channel |
| ATTACHMENT | statement that this block is the scalar source block in F |

All four inputs close the narrow F2 selector target conditionally:

```text
D17 + SECTOR + SCALAR + ATTACHMENT
  -> the F source block is B_lep
  -> the F block anchor is 1/sqrt(2).
```

Every one-input-removed target fails:

| missing input | witness | result |
|---|---|---|
| no D17 | a lepton label alone does not supply the normalized scalar singlet | no `B_lep` or `Z_lep^2=2` |
| no SECTOR | a full-cell source carrier can be regulator-generic | no charged-lepton-specific F2 selector |
| no SCALAR | triplet or `tilde H` alternatives are outside the stated D17 charged-lepton scalar block | no scalar-singlet F2 block |
| no ATTACHMENT | D17 alone gives a bounded scalar block, not a source/action family | no F2 source-block selector |

## Finite Checks

The D17 source note supplies the bounded scalar-singlet normalization:

```text
N_c = 1,
N_iso = 2,
Z_lep^2 = N_c N_iso = 2.
```

With two weak-isospin components, the unit block has two coefficients whose
squared magnitudes are `1/2`, so the total block norm is `1`.

This is not the same finite object as the full-cell source carrier:

| finite object | count | use here |
|---|---:|---|
| D17 charged-lepton scalar block components | `2` | supplies `1/sqrt(2)` block anchor |
| full OS0-cell source coordinates | `4^4 = 256` | belongs to F3, not F2 |
| direct product unit-vector class | `2 * 256 = 512` | wrong class for separated source-density route |

Thus F2 is a sector/block selector. It is not the `1/256` source-density
theorem.

## What This Moves

| before this note | after this note |
|---|---|
| F2 was named as "charged-lepton sector specificity" inside F. | F2 is narrowed to a concrete source-block selector target: D17 charged-lepton scalar-singlet block plus sector restriction plus source-block attachment. |
| D17 supplied a bounded scalar block but was not connected to F2. | D17 now supplies the positive block authority used by the F2 selector, still conditionally. |
| The next F work was "ratify F1-F4." | The next F work can be narrower: derive or ratify that the F source family is restricted to the D17 charged-lepton scalar block. |

If F2 is ratified, F still needs F1 source-coupled local-action convention,
F3 full OS0-cell tensor source locality, and F4 scalar-multiplier attachment.
Then the source-side chain still needs L, P, R, A3 precision placement, the
Koide/electron branch, `alpha(0)`, and the atomic harness.

The F2 charged-lepton source-block selector current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records the current boundary: current retained, primitive, and open-PR
surfaces do not supply `F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED`. The positive
route remains retained derivation or owner/audit acceptance of the
charged-lepton D17 source-block selector.

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md` | bounded D17 charged-lepton scalar singlet and `Z_lep^2 = 2` normalization under stated block inputs | does not supply a source/action family or retained F2 |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md` | F1-F4 dependency-order target and F assembly formula | does not ratify F1-F4 |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md` | conditional derivative attachment after source-coupled convention and lepton-specific full-cell source are supplied | does not prove lepton-specific source selection |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md` | if full OS0-cell source locality is supplied, `M_2(C)^tensor4` gives `256` matrix-unit source coordinates | does not select D17 charged-lepton sector |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md` | if the full-cell carrier is a scalar source multiplier, D17 `1/sqrt(2)` separates from `256` source weights | does not prove the source family is the D17 lepton source |
| `MINIMAL_AXIOMS_2026-06-29.md` | lattice, one-site algebra, admissibility, record formation, fixed record readout | no charged-lepton source selector, source/action bridge, normalization rule, source-readout bridge, or mass value |
| approved primitives | scale reference, OS0 kinetic-form isotropy, realized-state evaluation discipline | no charged-lepton source selector, source/action bridge, normalization, readout bridge, dynamics, mass value, or empirical match |

The primitive registry was checked with the current origin-main methodology.
Registered primitives chain-satisfy their declared dependencies, but they do
not supply F2, F, L, P, R, A3, `m_e`, `alpha(0)`, or hydrogen.

## Current Open PR Alignment

Open PRs were checked on 2026-07-04 after `origin/main` was refreshed and
after `#4986` through `#4991` appeared, then refreshed again after `#4992`
through `#4995` appeared. The moving review surface does not
close the charged-lepton F2 source-block selector:

| PR | state at refresh | effect on this F2 lane |
|---|---:|---|
| `#4995` theta retirement-basis re-match | `CLEAN` | theta winding-account governance/rematch context; no D17 charged-lepton source-block selector |
| `#4994` record-instrument polar contrast stabilization | `CLEAN` | numerical record/instrument robustness repair; no D17 charged-lepton source-block selector |
| `#4993` DELTA0 route inventory sibling-total refresh | `CLEAN` | stale route-inventory total repair; no F2 source-block closure |
| `#4992` g_bare two-Ward scope repair | `CLEAN` | keeps `g_bare = 1` conditional on residue normalization; no charged-lepton source selector |
| `#4991` owner-governed Tier-A retirement | `CLEAN` | governance retirement of live Tier-A admissions; explicitly not an axiom/primitive addition or theorem derivation, and no charged-lepton source-block selector |
| `#4990` Tier-A residual owner decision packet | `CLEAN` | proposal-only governance packet; no F2 source-block closure |
| `#4989` Tier-A residual governance readiness packet | `CLEAN` | governance readiness context; no D17 source-family theorem |
| `#4988` theta G2 registration stretch no-go | `CLEAN` | theta physical sector/readout registration remains open; no lepton source-block selector |
| `#4987` theta G4 theta-bar assembly no-go | `CLEAN` | theta assembly hygiene; no charged-lepton F2 selector |
| `#4986` AC R-eta h-class stretch no-go | `CLEAN` | AC/R-eta h-class pruning; no D17 source-block selector |
| `#4985` AC R-eta h-unit primitive no-go | `CLEAN` | primitive-registry methodology context; no charged-lepton source/action family |
| `#4980` through `#4984` theta and AC/R-eta surfaces | `CLEAN` | review context only; no F2 source-block selector |

Merge-state labels are moving review metadata, not proof inputs here.

## No-Go Discipline Gate

This section prevents overclaiming. The broad retained-F2 claim is **not**
shipped. The narrowed claim is:

```text
If D17, SECTOR, SCALAR, and ATTACHMENT are supplied, the F2 source-block
selector supplies B_lep and the 1/sqrt(2) D17 block anchor; every
one-input-removed F2 target fails.
```

Verdict tag: broad F2 retention not shipped; narrowed F2 block-selector
discriminator support passes.

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full F2 selector | Supply D17 block authority, charged-lepton sector restriction, scalar-singlet projection, and source-block attachment. | SUPPORTED CONDITIONALLY. It supplies `B_lep` and the `1/sqrt(2)` block anchor to F2. |
| D17-only route | Use the scalar-singlet D17 note by itself. | ATTEMPTED. It gives the bounded block and normalization, but not a source/action family or F2 selector. |
| full-cell-only route | Use `M_2(C)^tensor4` and `4^4 = 256` without sector restriction. | ATTEMPTED. It supplies a source-carrier count only, not the charged-lepton D17 block. |
| generic lepton-label route | Say the source is "leptonic" without D17 scalar-block authority. | ATTEMPTED. A label does not supply the normalized scalar singlet or source-block attachment. |
| triplet or `tilde H` route | Use a triplet insertion or the `tilde H` monomial as the sourced block. | RULED OUT BY D17 BLOCK SCOPE. Those channels are outside the stated charged-lepton scalar-singlet block. |
| approved-primitive shortcut | Appeal to minimal axioms or approved primitives for F2. | RULED OUT AS CLOSURE by registry-limited scope. They do not supply a charged-lepton source selector or source/action bridge. |
| latest open PR shortcut | Treat `#4986` through `#4995` as new F2 science. | ATTEMPTED. They are theta retirement/rematch, record/instrument, DELTA0, `g_bare`, Tier-A governance, theta, or AC/R-eta surfaces; none ratifies the D17 lepton source family. |
| empirical mass shortcut | Use `m_W/256`, PDG lepton masses, or hydrogen targets to infer F2. | RULED OUT AS ZERO-IMPORT ROUTE. Comparator data is target data, not a source-block theorem. |

### N2 - Wall-Independence Audit

The raw labels D17, SECTOR, SCALAR, and ATTACHMENT are discriminator inputs,
not four claimed independent walls. D17 and SCALAR collapse inside the stated
D17 scalar-singlet authority. The collapsed F2 selector inputs are:

| collapsed input | content |
|---|---|
| D17_SCALAR_BLOCK | D17 charged-lepton scalar-singlet block and `Z_lep^2 = 2` |
| SECTOR | source family is restricted to the charged-lepton sector |
| ATTACHMENT | the D17 block is attached as the F source block |

Pairwise audit:

| pair | does one close the other? | conclusion |
|---|---|---|
| D17_SCALAR_BLOCK with SECTOR | no | a block theorem does not say the source family selects it |
| D17_SCALAR_BLOCK with ATTACHMENT | no | a block theorem does not provide source/action attachment |
| SECTOR with ATTACHMENT | no | sector restriction does not specify the normalized block unless attached |

This note uses the collapsed selector target and does not inflate the wall
count.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `D17`, `scalar-singlet`, `Z_lep^2 = 2` | cited bounded block authority, not retained F2 |
| `charged-lepton sector` | explicit SECTOR selector input |
| `source-block attachment` | explicit ATTACHMENT selector input |
| `M_2(C)^tensor4`, `256` | F3 context only, not F2 closure |
| `registered` / `approved primitives` | registry-limited content only |
| `S_l`, `m_e`, `alpha(0)`, `hydrogen` | downstream non-claims |

No source/action convention, full-cell locality theorem, source-strength rule,
readout identity, mass input, or atomic result is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| D17 scalar-singlet note | bounded charged-lepton scalar block and `1/sqrt(2)` normalization | D17_SCALAR_BLOCK | yes, conditional |
| F-clause assembly discriminator | F2 is one required subinput for F | F2 target placement | yes, target placement only |
| source-coupled attachment support | derivative source attachment after lepton-specific full-cell source is supplied | ATTACHMENT context | yes, conditional boundary |
| full-cell source-carrier support | `256` carrier after full-cell source locality is supplied | F3, not F2 | no; review context only |
| D17/full-cell separability support | scalar multiplier can keep D17 and `256` factors separate | F4 context | boundary only |
| `#4986` through `#4995` | theta retirement/rematch, record/instrument, DELTA0, `g_bare`, Tier-A governance, theta, and AC/R-eta residuals | charged-lepton F2 source-block selector | no; review context only |

Only matching F2 residuals are counted as support.

### N5 - Rhetoric Audit

The negative phrase used here is narrow: "one-input-removed F2 targets fail."
Tested resolutions are:

| resolution | tested? | result |
|---|---:|---|
| block level | yes | without D17/SCALAR, no normalized `B_lep` block is supplied |
| sector level | yes | without SECTOR, a full-cell source is regulator-generic |
| source-attachment level | yes | without ATTACHMENT, D17 is not a source/action family |
| F level | not claimed as closed | F still needs F1, F3, and F4 |
| source-side `S_l` level | not claimed as closed | L, P, R remain separate |
| hydrogen level | not claimed | no statement that hydrogen is impossible or retained |

No broader no-go is shipped.

### N6 - Partial-Closure Path Scan

The legitimate closure path is not "add a new axiom." It is:

1. derive that the charged-lepton source family is restricted to the D17
   scalar-singlet block; or
2. ratify that source-block selector as part of the charged-lepton source/action
   interface and send it through review and audit.

The D17 note is a partial-closure path for D17_SCALAR_BLOCK. The source-coupled
attachment note is a partial-closure path for ATTACHMENT after lepton-specific
source inputs are supplied. The F-clause assembly discriminator is the target
placement. None alone closes retained F2.

The primitive registry was checked. Registered primitives are not walls, but
they also do not supply a charged-lepton source selector, source/action bridge,
normalization rule, source-readout bridge, dynamics, mass value, or empirical
match.

### N7 - Steelman

A hostile reviewer can argue that F2 is nearly automatic: D17 is explicitly the
charged-lepton scalar-singlet block, the F note asks for the charged-lepton
source/action family, and using any other sector would change the problem. That
is a strong convention-retirement argument. The narrow reply is that the repo
still needs retained authority or explicit ratification saying the physical
source family is restricted to that D17 block; this note exposes that target
instead of silently using it.

### N8 - Cross-Cycle Echo

Similar selector walls have been retired in the repo by separating a finite
positive theorem from the physical-license sentence that lets a later lane use
it. The same mechanism could retire F2: keep D17 as the finite block theorem,
then derive or ratify the charged-lepton source-block selector. This note
therefore ships as F2 block-selector support, not as a no-go and not as a
retained theorem.

## Non-Claims

- No derivation or ratification of F2.
- No derivation or ratification of F.
- No derivation or ratification of F1, F3, or F4.
- No derivation that `S_l = 1/256` is retained.
- No derivation of the `256.082435...` precision correction.
- No derivation of the Koide/electron branch or physical `m_e`.
- No derivation of `alpha(0)` or hydrogen spectroscopy.
- No use of latest open PRs as proof inputs.
- No new axiom, primitive, or admitted import.
- No audit status change for any cited row.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_f2_charged_lepton_source_block_selector_discriminator.py
```
