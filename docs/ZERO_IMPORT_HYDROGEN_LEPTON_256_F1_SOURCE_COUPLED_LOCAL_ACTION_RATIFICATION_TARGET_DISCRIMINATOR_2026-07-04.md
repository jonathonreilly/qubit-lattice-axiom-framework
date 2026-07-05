# Zero-Import Hydrogen: Lepton `1/256` F1 Source-Coupled Local-Action Ratification Target Discriminator

**Date:** 2026-07-04
**Type:** partial discriminator / source-action convention target
**Claim type:** conditional source-action convention support
**Status:** support-only. This note does not ratify F1, does not ratify F,
does not derive retained `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_f1_source_coupled_local_action_ratification_target_discriminator.py`

## Scope

The F-clause source/action assembly discriminator decomposed F into:

| subinput | content |
|---|---|
| F1 | source-coupled local-action convention |
| F2 | charged-lepton sector specificity |
| F3 | full OS0-cell tensor source locality |
| F4 | scalar-multiplier attachment |

This note attacks only F1. It asks what the phrase "source-coupled
local-action convention" must mean before the F source family can use

```text
dS_lep/dj_c = h * B_lep * O_c
```

as a physical local source insertion rather than as formal algebra.

## Conditional F1 Target

F1 is supplied if the framework derives or explicitly ratifies the following
source-side convention for the local action:

```text
S[j] = S_0 + sum_{c in C} j_c A_c,
dS/dj_c = A_c,
```

where local source derivatives of `S` define the local operator insertions
coupled to source controls. For the lepton F target, F2-F4 later identify

```text
A_c = h * B_lep * O_c.
```

F1 therefore contributes only the source/action insertion rule. It does not
select the D17 charged-lepton block, does not supply the full-cell `256`
carrier, does not choose scalar-multiplier attachment, does not normalize
source strength, and does not identify the coefficient with `S_l`.

## Ratification Target Discriminator

The tested F1 inputs are:

| input | content |
|---|---|
| ACTION | the source-side object is a local action `S[j]`, not only `W = log Z` response data |
| LINEAR | source controls enter linearly as `sum_c j_c A_c` |
| DERIVATIVE | local source derivatives of `S` define source insertions |
| RATIFICATION | the convention is derived or explicitly ratified for framework use |

All four inputs close the narrow F1 target conditionally:

```text
ACTION + LINEAR + DERIVATIVE + RATIFICATION
  -> dS/dj_c = A_c is the licensed local source insertion.
```

Every one-input-removed target fails:

| missing input | witness | result |
|---|---|---|
| no ACTION | `W = log Z` responses can be differentiated, but they are downstream response data | no local action insertion rule |
| no LINEAR | `S[j] = S_0 + sum_c j_c^2 A_c` gives `dS/dj_c = 2 j_c A_c`, not a fixed insertion |
| no DERIVATIVE | a formal source map `J(j)` can be written, but derivatives are not licensed as physical insertions | no source/action bridge |
| no RATIFICATION | the rule remains a candidate convention | no retained premise for F |

## Finite Checks

The finite derivative fact is elementary:

```text
S[j] = S_0 + sum_c j_c A_c
=> dS/dj_k = A_k.
```

It is also load-bearing:

| source form | derivative witness | F1 result |
|---|---|---|
| linear local source `sum_c j_c A_c` | `dS/dj_k = A_k` | correct insertion shape |
| nonlinear source `sum_c j_c^2 A_c` | `dS/dj_k = 2 j_k A_k` | no fixed insertion independent of source strength |
| mixed source `j_0(A_0 + A_1)` | `dS/dj_0 = A_0 + A_1` | no one-coordinate/one-insertion selector |
| response-only `W[j]` | differentiates connected responses after `S` is supplied | not the local action insertion rule |

Thus F1 is a convention/ratification target, not a new finite count and not a
source-density theorem.

## What This Moves

| before this note | after this note |
|---|---|
| F1 was named only as "source-coupled local-action convention." | F1 is narrowed to a ratifiable source/action insertion target: local action, linear source controls, derivative insertion rule, and explicit ratification or retained derivation. |
| The observable-principle source-coupled local-action note was a broad open-gate candidate. | Its hydrogen-facing consequence is isolated: `dS/dj_c = A_c` can be used only after the convention is adopted or derived. |
| F could be confused with the full F/L/P/R source-probe interface. | F1 is only the action-insertion license. F2-F4, L/P/R, A3, Koide/electron readout, `alpha(0)`, and hydrogen remain separate. |

If F1 is ratified, F still needs F2 charged-lepton sector specificity, F3
full OS0-cell tensor source locality, and F4 scalar-multiplier attachment.

The F1 source-coupled local-action current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
`F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED`. The current positive route remains
the source-coupled convention: local linear action source,
derivative-insertion license, no-new-primitive/no-comparator controls, owner
ratification, and audit acceptance.

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md` | open-gate candidate: local source derivatives of `S` define local operator insertions; derivatives of `W = log Z` generate responses | not retained authority for F1 |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md` | F1-F4 dependency-order target and F assembly formula | does not ratify F1-F4 |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md` | if F1 and a lepton-specific full-cell source are supplied, `dS_lep/dj_c = h * B_lep * O_c` | does not ratify F1 or prove lepton-specific source locality |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md` | if F1 and slot-resolved source family are supplied, source controls add linearly | no F1 ratification, positivity, normalization, or `S_l` identity |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md` | conditional F2 target for selecting the D17 charged-lepton block | does not supply F1 |
| `MINIMAL_AXIOMS_2026-06-29.md` | lattice, one-site algebra, admissibility, record formation, fixed record readout | no source/action bridge, local operator insertion convention, weighting, normalization, readout bridge, or mass value |
| approved primitives | scale reference, OS0 kinetic-form isotropy, realized-state evaluation discipline | no source/action bridge, local insertion convention, selector, normalization, readout bridge, dynamics, mass value, or empirical match |

The primitive registry was checked with the current origin-main methodology.
Registered primitives chain-satisfy their declared dependencies, but they do
not supply F1, F, L, P, R, A3, `m_e`, `alpha(0)`, or hydrogen.

## Current Open PR Alignment

Open PRs were checked on 2026-07-04 after `origin/main` was refreshed and
after `#4986` through `#4991` appeared, then refreshed again after `#4992`
through `#4995` appeared. The moving review surface does not
close the F1 source-coupled local-action target:

| PR | state at refresh | effect on this F1 lane |
|---|---:|---|
| `#4995` theta retirement-basis re-match | `CLEAN` | theta winding-account governance/rematch context; no source-coupled local-action ratification |
| `#4994` record-instrument polar contrast stabilization | `CLEAN` | numerical record/instrument robustness repair; no source-coupled local-action ratification |
| `#4993` DELTA0 route inventory sibling-total refresh | `CLEAN` | stale route-inventory total repair; no F1 source/action convention |
| `#4992` g_bare two-Ward scope repair | `CLEAN` | keeps `g_bare = 1` conditional on residue normalization; no source/action bridge for hydrogen |
| `#4991` owner-governed Tier-A retirement | `CLEAN` | governance retirement of live Tier-A admissions; explicitly not an axiom/primitive addition or theorem derivation, and no source-coupled local-action ratification |
| `#4990` Tier-A residual owner decision packet | `CLEAN` | proposal-only governance packet; no F1 source/action convention |
| `#4989` Tier-A residual governance readiness packet | `CLEAN` | governance readiness context; no F1 closure |
| `#4988` theta G2 registration stretch no-go | `CLEAN` | theta physical sector/readout registration remains open; no lepton source/action convention |
| `#4987` theta G4 theta-bar assembly no-go | `CLEAN` | theta assembly hygiene; no F1 source/action family |
| `#4986` AC R-eta h-class stretch no-go | `CLEAN` | AC/R-eta h-class pruning; no F1 source-coupled local-action convention |
| `#4985` AC R-eta h-unit primitive no-go | `CLEAN` | primitive-registry methodology context; no source/action bridge for hydrogen |
| `#4980` through `#4984` theta and AC/R-eta surfaces | `CLEAN` | review context only; no F1 source/action ratification |

Merge-state labels are moving review metadata, not proof inputs here.

## No-Go Discipline Gate

This section prevents overclaiming. The broad retained-F1 claim is **not**
shipped. The narrowed claim is:

```text
If ACTION, LINEAR, DERIVATIVE, and RATIFICATION are supplied, F1 licenses
dS/dj_c = A_c as the local source insertion; every one-input-removed F1 target
fails.
```

Verdict tag: broad F1 retention not shipped; narrowed F1 ratification-target
discriminator support passes.

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full F1 target | Supply local action, linear source controls, derivative insertion rule, and ratification or retained derivation. | SUPPORTED CONDITIONALLY. It licenses `dS/dj_c = A_c` as a local source insertion. |
| response-only `W = log Z` route | Use connected response derivatives without first licensing source insertions in `S`. | ATTEMPTED. It gives response data after a source is named, not the local action insertion rule. |
| formal source-map route | Write `J(j) = sum_c j_c O_c` without the derivative-insertion convention. | ATTEMPTED. It is algebraic bookkeeping only and does not define physical insertions. |
| nonlinear source route | Use source terms such as `j_c^2 A_c`. | ATTEMPTED. The derivative depends on source strength and does not give fixed insertion `A_c`. |
| mixed-control route | Let one source coordinate couple to multiple insertions. | ATTEMPTED. The derivative gives a sum of insertions and loses the one-source/one-insertion selector. |
| approved-primitive shortcut | Appeal to minimal axioms or approved primitives for source/action. | RULED OUT AS CLOSURE by registry-limited scope. They do not supply source/action or local insertion conventions. |
| latest open PR shortcut | Treat `#4986` through `#4995` as new F1 science. | ATTEMPTED. They are theta retirement/rematch, record/instrument, DELTA0, `g_bare`, Tier-A governance, theta, or AC/R-eta surfaces; none ratifies source-coupled local action for hydrogen. |
| empirical mass shortcut | Use `m_W/256`, PDG lepton masses, or hydrogen targets to infer F1. | RULED OUT AS ZERO-IMPORT ROUTE. Comparator data is target data, not a source/action convention. |

### N2 - Wall-Independence Audit

ACTION and LINEAR collapse into the local linear source-action shape. The
collapsed F1 target is:

| collapsed input | content |
|---|---|
| LOCAL_LINEAR_ACTION_SOURCE | the source-side object is local action `S[j] = S_0 + sum_c j_c A_c` |
| DERIVATIVE_INSERTION | local source derivatives of `S` define source insertions |
| RATIFICATION | the convention is derived or explicitly ratified for framework use |

Pairwise audit:

| pair | does one close the other? | conclusion |
|---|---|---|
| LOCAL_LINEAR_ACTION_SOURCE with DERIVATIVE_INSERTION | no | a linear formula does not by itself license physical insertions |
| LOCAL_LINEAR_ACTION_SOURCE with RATIFICATION | no | a formula can be written without adoption or retained derivation |
| DERIVATIVE_INSERTION with RATIFICATION | no | a candidate convention still needs adoption or derivation |

This note uses the collapsed target and does not inflate the wall count.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `source-coupled` / `local action` | explicit F1 target, not retained closure |
| `linear` | explicit source-shape input |
| `derivative` / `insertion` | explicit derivative-insertion input |
| `ratification` | explicit adoption or retained-derivation input |
| `W = log Z` | response boundary only, not F1 closure |
| `registered` / `approved primitives` | registry-limited content only |
| `S_l`, `m_e`, `alpha(0)`, `hydrogen` | downstream non-claims |

No source convention, sector selector, full-cell carrier, source-strength rule,
readout identity, mass input, or atomic result is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| source-coupled local-action candidate | source derivatives of `S` define local insertions as open-gate convention | F1 target | yes, open-gate candidate only |
| source-coupled attachment support | derivative attachment after F1 and lepton-specific full-cell source are supplied | F1 consequence | yes, conditional boundary |
| source-control linearity support | linear control additivity after F1 and source family are supplied | F1 consequence | yes, conditional boundary |
| F-clause assembly discriminator | F1 is one required F subinput | F1 target placement | yes, target placement only |
| F2 source-block selector discriminator | D17 charged-lepton block selector | F2, not F1 | no; sibling context only |
| `#4986` through `#4995` | theta retirement/rematch, record/instrument, DELTA0, `g_bare`, Tier-A governance, theta, and AC/R-eta residuals | F1 source-coupled local action | no; review context only |

Only matching F1 residuals are counted as support.

### N5 - Rhetoric Audit

The negative phrase used here is narrow: "one-input-removed F1 targets fail."
Tested resolutions are:

| resolution | tested? | result |
|---|---:|---|
| local action level | yes | without ACTION, `W` responses do not define local action insertions |
| source-shape level | yes | without LINEAR, derivatives need not give fixed insertions |
| convention level | yes | without DERIVATIVE, formal derivatives are not physical insertions |
| ratification level | yes | without RATIFICATION, F1 remains a candidate convention |
| F level | not claimed as closed | F still needs F2, F3, and F4 |
| source-side `S_l` level | not claimed as closed | L, P, R remain separate |
| hydrogen level | not claimed | no statement that hydrogen is impossible or retained |

No broader no-go is shipped.

### N6 - Partial-Closure Path Scan

The legitimate closure path is not "add a new axiom." It is:

1. derive the source-coupled local-action insertion convention from retained
   source/action structure; or
2. ratify it as an explicit convention and send the interface through review
   and audit.

The observable-principle source-coupled local-action admission candidate is a
direct partial-closure path for F1. The source-coupled attachment and
source-control linearity notes are conditional consequence checks after F1 is
supplied. None alone closes retained F1.

The primitive registry was checked. Registered primitives are not walls, but
they also do not supply source/action, local insertion conventions, weighting,
normalization, readout bridge, dynamics, mass value, or empirical match.

### N7 - Steelman

A hostile reviewer can argue that F1 is already the standard source convention:
the observable-principle source-coupled local-action candidate explicitly says
local source derivatives of `S` define local operator insertions, and the
hydrogen F lane merely uses that conventional vocabulary. That is a serious
ratification route. The narrow reply is that the source note is currently an
`open_gate` candidate and says it is not derived from retained primitives; this
hydrogen packet can target that convention but cannot silently promote it.

### N8 - Cross-Cycle Echo

Similar source/action and observable-principle walls have been retired by
narrowing broad physical claims into explicit conventions, then sending the
convention through review and audit. The same mechanism could retire F1. This
note therefore ships as F1 ratification-target support, not as a no-go and not
as a retained theorem.

## Non-Claims

- No derivation or ratification of F1.
- No derivation or ratification of F.
- No derivation or ratification of F2, F3, or F4.
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
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_f1_source_coupled_local_action_ratification_target_discriminator.py
```
