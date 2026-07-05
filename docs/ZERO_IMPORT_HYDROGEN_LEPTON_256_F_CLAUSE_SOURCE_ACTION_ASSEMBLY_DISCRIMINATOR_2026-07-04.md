# Zero-Import Hydrogen: Lepton `1/256` F-Clause Source/Action Assembly Discriminator

**Date:** 2026-07-04
**Type:** partial discriminator / source-action assembly support
**Claim type:** conditional source-action support
**Status:** support-only. This note does not ratify F, does not derive
retained `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_f_clause_source_action_assembly_discriminator.py`

## Scope

The source-probe ratification target discriminator reduced exact source-side
`S_l = 1/256` to a four-clause interface:

```text
F + L + P + R.
```

This note attacks only F, the full-cell charged-lepton source/action family.
It asks which inputs are necessary to assemble the formal source family

```text
S_lep[j] = h * B_lep * sum_{c in C} j_c O_c,
C = {0,1,2,3}^4,
|C| = 256,
dS_lep/dj_c = h * B_lep * O_c.
```

The answer is conditional. F is assembled if all four F-subinputs are supplied:

| subinput | content |
|---|---|
| F1 | source-coupled local-action convention: source derivatives of `S` define local operator insertions |
| F2 | charged-lepton sector specificity: the D17 scalar block `B_lep` is the block being sourced |
| F3 | full OS0-cell tensor source locality: one `M_2(C)` source algebra per `x,y,z,tau` slot, so `M_2(C)^tensor4` and `4^4 = 256` matrix-unit coordinates |
| F4 | scalar-multiplier attachment to the D17 block, not a direct product unit vector over `2 * 256` components |

This is not a ratification of F1-F4. It is a dependency-order discriminator:
all F1-F4 supplied closes the formal F assembly; every one-input-removed F
target fails with a concrete witness.

## Conditional Assembly

Let the charged-lepton D17 block be

```text
B_lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R.
```

Let a full OS0-cell source carrier be

```text
A_cell = M_2(C)^tensor4
C = {0,1,2,3}^4
O_c = E_{c_x} tensor E_{c_y} tensor E_{c_z} tensor E_{c_tau}.
```

Under F1-F4, the charged-lepton local source term is

```text
S_lep[j] = h * B_lep * sum_{c in C} j_c O_c.
```

Because the source controls enter linearly, each source derivative is

```text
dS_lep/dj_c = h * B_lep * O_c.
```

Thus F supplies the source/action family needed by the downstream L/P/R
interface: a charged-lepton D17 block, a full-cell `256`-coordinate source
carrier, and one local insertion per full-cell coordinate.

## One-Input-Removed Discriminator

| missing input | witness | result |
|---|---|---|
| no F1 | a formal map `J(j) = sum_c j_c O_c` can be written, but no source/action insertion rule ties `dS/dj_c` to a physical local source | no physical charged-lepton action-source family |
| no F2 | the full-cell source may be regulator-generic rather than charged-lepton-specific | no `B_lep` D17 block and no Lane 6 sector attachment |
| no F3 | slot-additive, diagonal, and scalar/tracial carriers have counts `16`, `4`, and `1` | no fixed 256 source family |
| no F4 | direct product unit normalization over `2 * 256 = 512` components gives `(1/sqrt(2))*(1/16)` | wrong class for the separated source-density route |

The discriminator therefore makes F smaller than "derive the whole
source-probe interface." F does not include label-free source-coordinate
naturality, positive projective source strength, or the `S_l` readout identity.
Those are L, P, and R.

## What This Moves

| before this note | after this note |
|---|---|
| F was named as one clause inside F/L/P/R. | F is decomposed into F1 source-coupled action, F2 charged-lepton sector specificity, F3 full-cell tensor source locality, and F4 scalar-multiplier attachment. |
| Full-cell carrier, D17 separation, and source-coupled attachment were separate support notes. | They now assemble into one auditable F target. |
| The next ratification work was "derive or ratify F/L/P/R" as a whole. | The dependency-order first target is "derive or ratify F1-F4 as the charged-lepton source/action family." |

If F1-F4 are ratified, the source-side chain still needs L, P, R, A3
precision placement, Koide/electron readout, `alpha(0)`, and the atomic harness.

**F1 source-coupled local-action follow-up:**
`ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md`
narrows F1 specifically. A local linear action source
`S[j] = S_0 + sum_c j_c A_c` gives the finite derivative
`dS/dj_c = A_c`, but F1 still needs an adopted or retained
source-insertion convention before that derivative can serve as a physical
local source insertion. This supports the F1 ratification target
conditionally; it does not ratify F1 or F.
The F1 source-coupled local-action current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_F1_SOURCE_COUPLED_LOCAL_ACTION_CURRENT_SURFACE_NO_GO_2026-07-05.md`
keeps that current boundary explicit: current retained, primitive, and
open-PR surfaces do not supply `F1_SOURCE_COUPLED_LOCAL_ACTION_RETAINED`.

**F2 charged-lepton source-block selector follow-up:**
`ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md`
narrows F2 specifically. D17 supplies the bounded charged-lepton scalar block
`B_lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R` with
`Z_lep^2 = 2`, but F2 still needs explicit charged-lepton sector restriction
and source-block attachment before that block can serve as the F source block.
This supports the F2 selector conditionally; it does not ratify F2 or F.
The F2 charged-lepton source-block selector current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md`
keeps that current boundary explicit: current retained, primitive, and
open-PR surfaces do not supply `F2_CHARGED_LEPTON_SOURCE_BLOCK_RETAINED`.

**F3 full-cell tensor source-locality follow-up:**
`ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md`
narrows F3 specifically. OS0 geometry supplies the four `M_2(C)` slots and the
full-cell carrier support proves `4^4 = 256` under supplied full-cell source
locality, but F3 still needs the physical charged-lepton source-locality
license, full tensor independence, and ratification before that carrier can
serve as the F source family. This supports the F3 ratification target
conditionally; it does not ratify F3 or F.
The F3 full-cell tensor source-locality current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_CURRENT_SURFACE_NO_GO_2026-07-05.md`
keeps that current boundary explicit: current retained, primitive, and
open-PR surfaces do not supply `F3_FULL_CELL_TENSOR_SOURCE_LOCALITY_RETAINED`.

**F4 scalar-multiplier attachment follow-up:**
`ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md`
narrows F4 specifically. D17 supplies the charged-lepton scalar block and the
full-cell source-locality target supplies the `256` source carrier, but F4
still needs scalar multiplication, D17 block preservation instead of `512`
product weights, and ratification before the attachment can serve as part of
F. This supports the F4 ratification target conditionally; it does not ratify
F4 or F.
The F4 scalar-multiplier attachment current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_F4_SCALAR_MULTIPLIER_ATTACHMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md`
keeps that current boundary explicit: current retained, primitive, and
open-PR surfaces do not supply `F4_SCALAR_MULTIPLIER_ATTACHMENT_RETAINED`.

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md` | open-gate source-coupling convention: local source derivatives of `S` define local operator insertions | not retained authority for F1 |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md` | if full OS0-cell source locality is supplied, `M_2(C)^tensor4` gives `256` matrix-unit coordinates | does not prove F3 as physical charged-lepton source locality |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md` | if a full-cell carrier is supplied as a scalar source multiplier, D17 `1/sqrt(2)` separates from `256` source weights | does not prove F4 as physical attachment |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md` | under source-coupled convention and lepton-specific full-cell source, `dS_lep/dj_c = h * B_lep * O_c` | does not ratify the convention or the full-cell lepton source |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md` | after F-style inputs are supplied, disjoint source controls add linearly | no positivity, projective normalization, or `S_l` identity |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md` | F/L/P/R minimality discriminator | does not decompose or ratify F1-F4 |
| `MINIMAL_AXIOMS_2026-06-29.md` | lattice, one-site algebra, admissibility, record formation, fixed record readout | no source/action bridge, weighting, normalization, selector, source-readout bridge, or mass value |
| approved primitives | scale reference, OS0 kinetic-form isotropy, realized-state evaluation discipline | no source/action, selector, normalization, readout bridge, dynamics, mass value, or empirical match |

The primitive registry was checked with the current origin-main methodology.
Registered primitives chain-satisfy their declared dependencies, but they do
not supply F1, F2, F3, F4, L, P, R, A3, `m_e`, `alpha(0)`, or hydrogen.

## Current Open PR Alignment

Open PRs were checked on 2026-07-04 after `origin/main` advanced to
`988fac7619`, after `#4980` through `#4985` appeared, and again after `#4986`
through `#4991` appeared, then refreshed again after `#4992` through `#4995`
appeared. The moving review surface does not close F1-F4 on
current main:

| PR | state at refresh | effect on this F-clause lane |
|---|---:|---|
| `#4995` theta retirement-basis re-match | `CLEAN` | theta winding-account governance/rematch context; no F1-F4 source-action assembly |
| `#4994` record-instrument polar contrast stabilization | `CLEAN` | numerical record/instrument robustness repair; no F1-F4 source-action assembly |
| `#4993` DELTA0 route inventory sibling-total refresh | `CLEAN` | stale route-inventory total repair; no F-clause closure |
| `#4992` g_bare two-Ward scope repair | `CLEAN` | keeps `g_bare = 1` conditional on residue normalization; no charged-lepton source/action family |
| `#4991` owner-governed Tier-A retirement | `CLEAN` | governance retirement of live Tier-A admissions; explicitly not an axiom/primitive addition or theorem derivation, and no charged-lepton source/action family |
| `#4990` Tier-A residual owner decision packet | `CLEAN` | proposal-only governance packet; no F1-F4 source-action assembly |
| `#4989` Tier-A residual governance readiness packet | `CLEAN` | governance readiness context; no F-clause closure |
| `#4988` theta G2 registration stretch no-go | `CLEAN` | theta physical sector/readout registration remains open; no charged-lepton source/action convention |
| `#4987` theta G4 theta-bar assembly no-go | `CLEAN` | theta assembly hygiene; no charged-lepton source/action family |
| `#4986` AC R-eta h-class stretch no-go | `CLEAN` | AC/R-eta h-class pruning; no F1-F4 source-action assembly |
| `#4985` AC R-eta h-unit primitive no-go | `CLEAN` | useful primitive-registry methodology context; no charged-lepton source/action family |
| `#4984` AC R-eta direct-license no-go | `CLEAN` | AC/R-eta readout-license hygiene; no F1-F4 source-action assembly |
| `#4983` AC R-eta doublet-clock no-go | `CLEAN` | AC/R-eta clock/rate hygiene; no lepton full-cell source family |
| `#4982` AC occupancy formation non-supply no-go | `CLEAN` | AC occupancy formation pruning; no charged-lepton source/action interface |
| `#4981` AC R-eta C3 ratification non-supply | `CLEAN` | AC/R-eta C3 hygiene; no Lane 6 F-clause ratification |
| `#4980` theta G1 kinetic 4D scaffold support | `CLEAN` | theta kinetic 4D scaffold support; no charged-lepton source/action convention |
| `#4979` theta G1 defect suppression support | `CLEAN` | theta supplied-penalty support; no F1-F4 source-action assembly |
| `#4978` theta G1 4D carrier supply no-go | `CLEAN` | theta carrier no-go; no charged-lepton full-cell source/action family |
| `#4975` primitive axiom absorption no-go | `CLEAN` | aligned methodology: approved primitives are not silently absorbed into axioms; no F1-F4 closure |
| `#4968`, `#4966` alpha-s kernel scoping PRs | `CLEAN` | later running/threshold hygiene; no Lane 6 source-action assembly |

Merge-state labels are moving review metadata, not proof inputs here.

## No-Go Discipline Gate

This section prevents overclaiming. The broad retained-F claim is **not**
shipped. The narrowed claim is:

```text
If F1-F4 are supplied, the formal F source/action family assembles; every
one-input-removed F target fails.
```

Verdict tag: broad F retention fails; narrowed F-clause assembly discriminator
support passes.

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full F1-F4 assembly | Supply source-coupled action, D17 lepton sector, full-cell source locality, and scalar-multiplier attachment. | SUPPORTED CONDITIONALLY. It gives `S_lep[j] = h * B_lep * sum_c j_c O_c` and `dS_lep/dj_c = h * B_lep * O_c`. |
| no F1 source/action route | Treat `J(j)` as a formal algebra source without a local-action derivative convention. | ATTEMPTED. It is formal bookkeeping only; no physical source insertion is licensed. |
| no F2 sector route | Use the full-cell source without attaching it to the charged-lepton D17 block. | ATTEMPTED. It gives a regulator/source carrier but not the Lane 6 scalar block `B_lep`. |
| no F3 carrier route | Use slot-additive, diagonal, or scalar/tracial source shapes. | ATTEMPTED. The counts are `16`, `4`, and `1`, not `256`. |
| no F4 product-vector route | Unit-normalize over `D17 x M_2(C)^tensor4` product components. | ATTEMPTED. It gives the `512`-component `(1/sqrt(2))*(1/16)` class, not separated source-density weights. |
| approved-primitive shortcut | Appeal to minimal axioms or approved primitives for source/action. | RULED OUT AS CLOSURE by registry-limited scope. They do not supply source/action, selector, normalization, readout, or mass value. |
| latest open PR shortcut | Treat `#4980` through `#4995` as new Lane 6 source-action input. | ATTEMPTED. They are theta retirement/rematch, record/instrument, DELTA0, `g_bare`, theta, AC/R-eta, or governance methodology/hygiene surfaces, not F1-F4 ratification. |
| empirical scale shortcut | Use `m_W/256` or `256.082435...` to infer F. | RULED OUT AS ZERO-IMPORT ROUTE. Comparator data is target data, not a source/action theorem. |

### N2 - Wall-Independence Audit

The collapsed F wall set is exactly F1-F4.

| pair | does one close the other? | conclusion |
|---|---|---|
| F1 with F2 | no | source/action convention does not select charged-lepton sector |
| F1 with F3 | no | source/action convention does not choose full-cell tensor locality |
| F1 with F4 | no | source/action convention does not alone force scalar-multiplier attachment |
| F2 with F3 | no | D17 sector specificity does not imply full-cell carrier locality |
| F2 with F4 | no | charged-lepton sector does not choose separated source multiplier versus product vector |
| F3 with F4 | no | full-cell carrier count does not choose how it attaches to D17 |

Downstream walls remain separate: L label-free naturality, P positive
projective source strength, R `S_l` readout identity, A3 precision, the
Koide/electron branch, and `alpha(0)`.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `source-coupled` / `local action` | explicit F1 gate, not retained closure |
| `charged-lepton` / `B_lep` | explicit F2 sector gate |
| `full OS0-cell` / `M_2(C)^tensor4` | explicit F3 source-locality gate |
| `scalar multiplier` | explicit F4 attachment gate |
| `256` | finite consequence of F3 only |
| `registered` / `approved primitives` | registry-limited content only |
| `S_l`, `m_e`, `alpha(0)`, `hydrogen` | downstream non-claims |

No source convention, sector selector, full-cell locality theorem, attachment
rule, readout identity, precision correction, or mass input is hidden as
background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| source-coupled local-action candidate | F1 source/action convention | F1 | yes as open-gate candidate, not closure |
| full-cell source-carrier support | finite `M_2(C)^tensor4` carrier under supplied full-cell locality | F3 | yes, conditional |
| D17/full-cell separability support | scalar source multiplier preserves D17 normalization and `256` weights | F4 | yes, conditional |
| source-coupled attachment support | derivative attachment after F1-F3 style inputs | F assembly | yes, conditional |
| source-control linearity support | algebraic additivity after source/action family is supplied | downstream of F | boundary only |
| ratification target discriminator | F/L/P/R minimality | F as one clause | yes for target placement, not F ratification |
| F1 source-coupled local-action ratification target discriminator | local linear action source plus derivative-insertion convention target for F1 | F1 | yes, conditional follow-up |
| F2 charged-lepton source-block selector discriminator | D17 block plus sector and attachment target for F2 | F2 | yes, conditional follow-up |
| F3 full-cell tensor source-locality ratification target discriminator | OS0 geometry plus physical full-cell tensor source-locality target for F3 | F3 | yes, conditional follow-up |
| `#4980` through `#4995` | theta retirement/rematch, record/instrument, DELTA0, `g_bare`, theta, AC/R-eta, governance, and methodology residuals | Lane 6 F1-F4 | no; review context only |

Only matching F residuals are counted as support.

### N5 - Rhetoric Audit

The negative phrase used here is narrow: "one-input-removed F targets fail."
Tested resolutions are:

| resolution | tested? | result |
|---|---:|---|
| source/action insertion rule | yes | without F1, `J(j)` is formal and not a physical source insertion |
| sector/block level | yes | without F2, no `B_lep` D17 block is sourced |
| carrier-count level | yes | without F3, weaker carriers give `16`, `4`, or `1` |
| attachment/norm level | yes | without F4, direct product unit normalization gives the `512`/`1/16` class |
| L/P/R interface level | not claimed as closed | F alone does not give label-free naturality, projective strength, or `S_l` |
| hydrogen level | not claimed | no statement that hydrogen is impossible or retained |

No broader no-go is shipped.

### N6 - Partial-Closure Path Scan

The legitimate closure path is not "add a new axiom." It is:

1. derive F1-F4 from retained source/action and charged-lepton source structure;
2. or ratify F1-F4 as an explicit charged-lepton source/action convention and
   send that interface through review and audit.

The observable-principle source-coupled local-action candidate remains a
partial-closure path for F1. The D17 scalar block remains partial support for
F2 inside its stated bounded scope. The full-cell carrier and D17/full-cell
separability notes remain partial-closure paths for F3 and F4. None alone
closes F.

The primitive registry was checked. Registered primitives are not walls, but
they also do not supply source/action, weighting, normalization, selector,
readout bridge, dynamics, mass value, or empirical match.

### N7 - Steelman

A hostile reviewer can argue that F is already implicit: source-coupled action
is a standard convention, D17 is the charged-lepton scalar block, OS0 has four
slots, and the scalar source multiplier is the only reading that keeps D17 from
double-counting. That is a strong convention-retirement argument. The narrow
reply is that this note makes exactly that route auditable, but the repo still
needs retained authority or explicit ratification for F1-F4 before F can be
used as a premise for `S_l = 1/256`.

### N8 - Cross-Cycle Echo

Similar source/action and normalization walls in the repo have been retired by
narrowing broad physical claims into explicit conventions, then auditing those
interfaces. The same mechanism could retire F if F1-F4 are accepted as the
charged-lepton source/action convention. This note therefore ships as
F-clause assembly support, not as a no-go and not as a retained theorem.

**Gate result:** `PASS` for the narrowed F-clause assembly discriminator.
Broad F retention is not claimed.

## Non-Claims

- No derivation or ratification of F1-F4.
- No derivation or ratification of F.
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
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_f_clause_source_action_assembly_discriminator.py
```
