# Zero-Import Hydrogen: Koide K1 Counting-Measure Target Discriminator

**Date:** 2026-07-05
**Type:** target discriminator / Koide K1 counting-measure handoff
**Status:** support-only. This note does not ratify K1, does not derive
`r = 1/2` or `Q = 2/3`, does not derive the physical electron mass, and does
not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_koide_k1_counting_measure_target_discriminator.py`

## Scope

The Koide/electron-readout firewall splits the charged-lepton readout into
separate gates. K1 is the counting-measure gate:

```text
block/orbit/holomorphic count  -> r = 1/2 -> Q = 2/3
dimension/Born/trace count     -> r = 1   -> Q = 1
```

The existing source notes reduce the charged-lepton Koide value to this one
binary, but the current retained surface does not choose the block/orbit count
as a zero-import theorem. This discriminator names the hydrogen-facing target
for spending that binary later without importing the old `AC_phi_lambda`
admission, lepton comparator data, species identity, phase readout, or scale.

The target is the specific retained handoff:

```text
K1_COUNTING_MEASURE_RETAINED.
```

## Target Contract

`K1_COUNTING_MEASURE_RETAINED` requires all ten inputs:

```text
K1_COUNTING_TEXT_LOCK
C3_CIRCULANT_FORM_RETAINED
BLOCK_VS_DIMENSION_FORK_REPROVEN
ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED
DIMENSION_BORN_DEFAULT_EXCLUSION
NO_K2_K3_K4_OR_MASS_INPUT
NO_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

The clauses mean:

| clause | content |
|---|---|
| K1_COUNTING_TEXT_LOCK | the object being decided is only the Koide count/measure bit, not phase, species, scale, or mass |
| C3_CIRCULANT_FORM_RETAINED | the charged-lepton readout uses the retained C3 circulant carrier and `Q = 1/3 + (2/3)r` algebra |
| BLOCK_VS_DIMENSION_FORK_REPROVEN | the two canonical cells are explicitly reproduced as `(1,1) -> r = 1/2 -> Q = 2/3` and `(1,2) -> r = 1 -> Q = 1` |
| ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED | a retained theorem selects the block/orbit/holomorphic count rather than treating it as a premise or comparator choice |
| DIMENSION_BORN_DEFAULT_EXCLUSION | the dimension/Born/trace default is excluded by the same retained reasoning, not merely disliked |
| NO_K2_K3_K4_OR_MASS_INPUT | the K1 decision does not consume R-eta/radian phase, physical species bridge, absolute scale, branch mass-map, or electron-mass inputs |
| NO_COMPARATOR_PROOF_INPUT | observed lepton masses, fitted `Q`, fitted `delta`, observed `m_W`, observed `m_e`, `alpha(0)`, and Rydberg data are excluded as proof inputs |
| NO_NEW_PRIMITIVE_OR_AXIOM | the decision does not add a primitive, axiom, or new Tier-A numerical admission |
| OWNER_RATIFICATION | the owner accepts this as the K1 counting-measure object |
| AUDIT_ACCEPTANCE | the normal independent review/audit path accepts the target and dependency consequences |

No proper subset of those ten inputs supplies K1.

## Source Surface

The narrow synthesis
`CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md`
already records the useful reduction: the Koide value is one binary
counting-measure bit, with the block count giving `r = 1/2` and the dimension
count giving `r = 1`. That is positive progress, but it is not a retained
selector.

The supertrace/equivariant-index/holomorphic note
`SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md`
names the right-shaped route: a chiral or holomorphic determinant would count
the doublet complex mode once. It remains an open gate, conditional on the
staggered-Dirac mass/Yukawa realization and the relevant readout theorem.

The occupancy independence note
`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`
states that the current checked Record/Koide bookkeeping surface does not
supply the occupancy rule. Its orbit-occupancy proposal is an owner-decision
candidate, not an adopted theorem.

The Berezin subsumption and kernel-coefficient notes,
`OCCUPANCY_READOUT_EXPONENT_BEREZIN_SUBSUMPTION_BOUNDED_THEOREM_NOTE_2026-06-09.md`
and
`KOIDE_OCCUPANCY_KERNEL_COEFFICIENT_NOT_FIXED_BY_RETAINED_CORNER_MEASURE_BOUNDED_NOTE_2026-06-12.md`,
sharpen the same object. They route the exponent through existing conditional
realization structure and show that the retained corner measure does not by
itself fix the doublet-block coefficient. They do not close K1 on the current
zero-import retained surface.

The two-gate companion
`CHARGED_LEPTON_KOIDE_TWO_GATE_TIER_A_BOUNDED_THEOREM_NOTE_2026-06-02.md`
records the conditional consequence of consuming the old `AC_phi_lambda`
registry premise. That is not the zero-import target here. The K1 target asks
for a retained selector, not a bounded consequence under an imported registry
premise.

## Current Surface Classification

| surface | classification |
|---|---|
| counting-bit synthesis note | reduces K1 to one binary; does not force the block/orbit count |
| supertrace / equivariant-index / holomorphic route | right-shaped live route; open gate, not retained K1 |
| orbit-occupancy independence note | current-surface non-supply plus premise candidate; not theorem closure |
| Berezin subsumption note | conditional under existing staggered gate and K/CPT registration; not unconditional K1 |
| retained corner-measure coefficient note | measure-level non-supply; transfer/kernel route remains live |
| `CHARGED_LEPTON_KOIDE_TWO_GATE_TIER_A_BOUNDED_THEOREM_NOTE_2026-06-02.md` | conditional under `AC_phi_lambda`; not zero-import retained K1 |
| open `#4932` | blocks the updated-axiom/primitives shortcut for AC(i)'s measure-side binary |
| open `#4991` | would move old occupancy atoms to owner-governed premise standing, not theorem closure |
| merged `#5019` | Koide `AC_phi_lambda` premise-hygiene context; no K1 derivation |
| approved primitives | premise discipline only; no counting-measure selector |
| Koide electron-readout firewall | K1/K2/K3/K4 separation; no mass closure |
| `ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md` | subtarget for the selector and dimension/Born default-exclusion inputs; not full K1 |
| `ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md` | owner/audit decision contract for `K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED`; not full K1 |
| `ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current non-supply boundary for `K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED`; not full K1 |

The primitive registry was checked. Registered primitives are approved premise
nodes, not walls, but no primitive supplies `K1_COUNTING_MEASURE_RETAINED`,
`r = 1/2`, `Q = 2/3`, `m_e`, `alpha(0)`, or hydrogen.

The K1 counting-measure current-surface no-go
`ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records the corresponding non-supply boundary: current retained, primitive,
merged-PR, and open-PR surfaces do not supply
`K1_COUNTING_MEASURE_RETAINED`.

The K1 counting-measure ratification decision packet
`ZERO_IMPORT_HYDROGEN_KOIDE_K1_COUNTING_MEASURE_RATIFICATION_DECISION_PACKET_2026-07-05.md`
packages the same ten-input owner/audit contract as a decision object. It is
not accepted here and does not ratify `K1_COUNTING_MEASURE_RETAINED`.

The K1 selector/default-exclusion target discriminator
`ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md`
attacks the two technical K1 inputs
`ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED` and
`DIMENSION_BORN_DEFAULT_EXCLUSION` through the named subtarget
`K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED`. It is a subhandoff only: it does not
ratify K1, owner/audit acceptance, `m_e`, `alpha(0)`, or hydrogen.
The K1 selector/default-exclusion ratification decision packet
`ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_RATIFICATION_DECISION_PACKET_2026-07-05.md`
packages the subhandoff as an eleven-input owner/audit contract, and the
matching current-surface no-go
`ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, merged-PR, and open-PR surfaces do
not supply `K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED`. Both are upstream of full
K1 and do not supply `K1_COUNTING_MEASURE_RETAINED`.

## Dependency Boundary

| object | if this target is accepted | still not supplied |
|---|---|---|
| K1 counting measure | `K1_COUNTING_MEASURE_RETAINED` | K2 exact phase/readout |
| K1 selector/default-exclusion | could supply `ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED` and `DIMENSION_BORN_DEFAULT_EXCLUSION` if accepted | full K1 owner/audit decision still absent |
| Koide shape surface | gains the retained `r = 1/2`, `Q = 2/3` count | physical branch and mass still absent |
| native Koide bridge | gains a K1 input | Z1-Z3 native bridge acceptance still separate |
| physical electron readout | still blocked | K2 exactness, K3 species bridge, branch mass-map, K4 scale |
| physical electron mass | still blocked | `NATIVE_ZERO_SECTION_BRIDGE_RETAINED`, `PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED`, `KOIDE_BRANCH_MASS_MAP_RETAINED`, `ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED` |
| hydrogen | still blocked | retained `m_e`, retained `alpha(0)`, static-source NR Coulomb limit, harness, and audit |

This target can move the Koide K1 lane. It cannot close Lane 6 by itself.

## What This Moves

| before this note | after this note |
|---|---|
| K1 existed only as a firewall row and source-side residual | K1 has an explicit ten-input hydrogen-facing target contract |
| occupancy premise material could be overread as zero-import K1 closure | theorem closure and owner-governed premise standing are separated |
| hydrogen had no spendable K1 successor predicate | the next K1 lane is `K1_COUNTING_MEASURE_RETAINED` |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the current retained
surface supplies K1" is not shipped. The narrowed claim is:

```text
K1 counting is a named ten-input target; it is not a retained result here.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| static C3/Koide algebra | Treat `Q = 1/3 + (2/3)r` as selecting `r = 1/2`. | ATTEMPTED. The algebra supplies the form, not the count selector. |
| native `J_cs` complex structure | Treat the doublet complex structure as the block-count measure. | ATTEMPTED. The synthesis note identifies `J_cs` as native but measure-neutral. |
| Record/orbit wording | Treat Record outcomes as an occupancy rule. | RULED OUT ON CURRENT SURFACE. Record explicitly supplies no weighting, normalization, probability, or occupancy rule. |
| orbit-occupancy premise | Adopt one slot per record outcome. | PREMISE CANDIDATE. Not adopted and not a zero-import theorem here. |
| supertrace / holomorphic determinant | Use a chiral or holomorphic determinant to count the doublet once. | OPEN TARGET. Right-shaped live route, not retained closure. |
| Berezin realization route | Use determinant exponent bookkeeping under the existing staggered gate. | CONDITIONAL. Useful if the realization gate is retained; not unconditional K1. |
| primitive shortcut | Treat approved primitives as supplying the counting selector. | RULED OUT. Primitives police premise use; they do not choose the Koide count. |
| Tier-A `AC_phi_lambda` shortcut | Consume the old registered premise. | CONDITIONAL ONLY. Not a zero-import retained derivation. |
| K2/K3/K4/mass route | Infer K1 from phase, species, scale, or electron mass. | RULED OUT. Those are independent downstream gates. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| K1 counting <-> K2 R-eta exactness | no | independent |
| K1 counting <-> K3 physical species | no | independent |
| K1 counting <-> K4 absolute scale | no | independent |
| K1 counting <-> native zero-section bridge | no | independent |
| K1 counting <-> branch mass-map | no | independent downstream gate |
| K1 counting <-> physical electron mass | no | independent downstream gate |
| K1 counting <-> alpha(0) | no | independent |

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `block` / `orbit` / `holomorphic` | target selector content, not already retained |
| `dimension` / `Born` / `trace` | competing default to be excluded, not a straw target |
| `Record` | supplies record readout after context is given; supplies no occupancy rule |
| `primitive` | premise discipline, not value selector |
| `AC_phi_lambda` | bounded registry premise, not zero-import theorem |
| `observed` / `fitted` / `PDG` | comparator data, excluded |
| `owner` / `audit` | required retained-status gates |

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| counting-bit synthesis note | reduces Koide value to one binary | K1 target content | yes |
| supertrace/equivariant-index open lead | chiral/holomorphic count route | live theorem route | yes |
| orbit-occupancy independence note | current-surface non-supply and premise candidate | not retained K1 | yes |
| Berezin subsumption note | conditional determinant-exponent route | possible future input, not full K1 | yes |
| retained corner-measure coefficient note | measure-level coefficient non-supply | no shortcut from retained measure | yes |
| two-gate Tier-A companion | conditional K1/K2 under `AC_phi_lambda` | not zero-import closure | yes |
| Koide electron-readout firewall | K1/K2/K3/K4 separation | hydrogen-facing dependency boundary | yes |
| primitive registry notes | primitive boundary | guard only | yes |

### N5 - Rhetoric Audit

The negative phrase is narrow: "K1 is not retained here."

| resolution | tested? | outcome |
|---|---:|---|
| Koide algebraic form | yes | prerequisite only |
| native complex structure | yes | measure-neutral by source note |
| current Record/Koide surface | yes | non-supply by explicit clause and model witness |
| supertrace/holomorphic determinant | named | live route, not closed |
| owner-governed premise standing | separated | not theorem closure |
| physical electron mass | kept separate | still downstream |

### N6 - Partial-Closure Path Scan

Legitimate follow-ups remain:

| path | what it could close |
|---|---|
| retained supertrace/equivariant-index/holomorphic determinant theorem | `ORBIT_OR_HOLOMORPHIC_COUNT_SELECTOR_RETAINED` |
| retained transfer/kernel coefficient theorem for the corner realization | `DIMENSION_BORN_DEFAULT_EXCLUSION` if it selects the block/orbit cell |
| owner/audit acceptance of the selector/default-exclusion subtarget | `K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED` and the two technical K1 inputs |
| owner/audit acceptance of an occupancy premise | premise standing only, not zero-import theorem closure unless explicitly scoped as such |
| owner/audit acceptance of this target after all inputs are present | `K1_COUNTING_MEASURE_RETAINED` |
| K2/K3/K4 packets | physical electron mass path after K1 is improved |

### N7 - Steelman

A strong positive reading is that the block/orbit cell has the right shape:
it counts record outcomes rather than real components, it matches the
holomorphic determinant exponent, and it is exactly the charged-lepton target
`Q = 2/3`. That is real progress. The retained-status burden remains the
selector theorem or explicitly scoped owner/audit premise decision, because
hydrogen needs a spendable electron-mass dependency, not only a plausible cell.

### N8 - Cross-Cycle Echo

This mirrors the K2 exactness and `1/256` source-probe work: a clean finite
scaffold becomes spendable only after the physical readout convention,
comparator boundary, owner acceptance, and audit path are explicit. K1 now has
the same discipline.

**Gate result:** broad K1-closure claim fails; narrowed counting-measure target
discriminator passes.

## Explicit Non-Claims

- No derivation or ratification of `K1_COUNTING_MEASURE_RETAINED`.
- No derivation of `r = 1/2` or `Q = 2/3` from the current retained inventory.
- No adoption of orbit-occupancy or any owner-governed occupancy premise.
- No derivation or ratification of K2 exactness, K3 physical species bridge,
  K4 absolute scale, native Z1-Z3 bridge, or Koide branch mass-map.
- No derivation or ratification of `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`.
- No derivation of `S_l`, A3, `alpha(0)`, static-source Rydberg, or hydrogen.
- No new axiom, primitive, Tier-A admission, or empirical import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_koide_k1_counting_measure_target_discriminator.py
```

The verifier checks the K1 target contract, the source-surface boundaries,
the primitive-registry boundary, the goal/firewall wiring, the no-go discipline
section, and the explicit non-claims.
