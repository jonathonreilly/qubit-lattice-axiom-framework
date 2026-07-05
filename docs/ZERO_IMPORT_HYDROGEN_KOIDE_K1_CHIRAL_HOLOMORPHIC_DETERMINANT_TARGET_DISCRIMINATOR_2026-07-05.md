# Zero-Import Hydrogen: Koide K1 Chiral/Holomorphic Determinant Target Discriminator

**Date:** 2026-07-05
**Type:** target discriminator / Koide K1 determinant subhandoff
**Status:** support-only. This note does not ratify
`K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED`, does not ratify
`CHIRAL_OR_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED`, does not ratify
`K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED`, does not derive `r = 1/2` or
`Q = 2/3`, does not derive the physical electron mass, and does not claim
hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_koide_k1_chiral_holomorphic_determinant_target_discriminator.py`

## Scope

The K1 selector/default-exclusion subtarget has two mathematical inputs still
separated on the current surface:

```text
CHIRAL_OR_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED
REAL_VECTOR_TRACE_DEFAULT_EXCLUDED
```

This packet attacks only the first one. It names the reviewable subtarget:

```text
K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED.
```

If that subtarget is later accepted, its conditional consequence is:

```text
CHIRAL_OR_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED
```

That consequence does not supply `REAL_VECTOR_TRACE_DEFAULT_EXCLUDED`,
`DIMENSION_BORN_DEFAULT_EXCLUSION`,
`K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED`, full K1, physical electron mass,
alpha, or hydrogen. It is one nested theorem lane inside the K1 selector gate.

## Target Contract

`K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED` requires all fourteen
inputs:

```text
K1_DETERMINANT_TEXT_LOCK
C3_CIRCULANT_FORM_RETAINED
BLOCK_VS_DIMENSION_FORK_REPROVEN
NATIVE_DOUBLET_COMPLEX_STRUCTURE_PRESENT
FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED
READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT
CHIRAL_HOLOMORPHIC_COUNT_COMPUTED_ON_RETAINED_REALIZATION
VECTOR_TRACE_DEFAULT_NOT_USED_AS_PROOF
NO_RECORD_OCCUPANCY_PREMISE_INPUT
NO_K2_K3_K4_OR_MASS_INPUT
NO_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

The clauses mean:

| clause | content |
|---|---|
| K1_DETERMINANT_TEXT_LOCK | the object is only the K1 determinant/readout theorem lane, not the full selector/default-exclusion subtarget, full K1, K2, K3, K4, mass, alpha, or hydrogen |
| C3_CIRCULANT_FORM_RETAINED | the charged-lepton readout uses the retained C3 circulant carrier and `Q = 1/3 + (2/3)r` algebra |
| BLOCK_VS_DIMENSION_FORK_REPROVEN | the two cells are reproduced as `(1,1) -> r = 1/2 -> Q = 2/3` and `(1,2) -> r = 1 -> Q = 1` |
| NATIVE_DOUBLET_COMPLEX_STRUCTURE_PRESENT | the doublet complex structure `J_cs` is present and native, while remaining measure-neutral by itself |
| FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED | the relevant framework fluctuation determinant/readout object is identified, not inferred from generic static C3 algebra |
| READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT | the readout functional is proved to factor through the one-complex-slot doublet quotient |
| CHIRAL_HOLOMORPHIC_COUNT_COMPUTED_ON_RETAINED_REALIZATION | the retained realization computes the doublet count chirally or holomorphically, so the complex doublet is counted once |
| VECTOR_TRACE_DEFAULT_NOT_USED_AS_PROOF | the vector/real trace cell is not consumed as proof of the chiral theorem and is not silently erased |
| NO_RECORD_OCCUPANCY_PREMISE_INPUT | Record or orbit-occupancy wording is not consumed as an adopted premise or shortcut |
| NO_K2_K3_K4_OR_MASS_INPUT | no R-eta phase, species bridge, absolute scale, branch map, native bridge, or electron-mass input is consumed |
| NO_COMPARATOR_PROOF_INPUT | observed lepton masses, fitted `Q`, fitted `delta`, observed `m_e`, `alpha(0)`, and Rydberg data are excluded as proof inputs |
| NO_NEW_PRIMITIVE_OR_AXIOM | the subtarget does not add a primitive, axiom, or new Tier-A numerical admission |
| OWNER_RATIFICATION | the owner accepts this exact determinant theorem object |
| AUDIT_ACCEPTANCE | the normal independent review/audit path accepts the object and dependency consequences |

No proper subset of those fourteen inputs supplies the determinant theorem.

The companion ratification decision packet
`ZERO_IMPORT_HYDROGEN_KOIDE_K1_CHIRAL_HOLOMORPHIC_DETERMINANT_RATIFICATION_DECISION_PACKET_2026-07-05.md`
packages this same subhandoff as a fourteen-input owner/audit contract. The
matching current-surface no-go
`ZERO_IMPORT_HYDROGEN_KOIDE_K1_CHIRAL_HOLOMORPHIC_DETERMINANT_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, merged-PR, and open-PR surfaces do
not supply `K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED`.

The nested object-identification target
`ZERO_IMPORT_HYDROGEN_KOIDE_K1_FLUCTUATION_DETERMINANT_OBJECT_TARGET_DISCRIMINATOR_2026-07-05.md`
packages `K1_FLUCTUATION_DETERMINANT_OBJECT_IDENTIFICATION_RETAINED`, which
could feed only `FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED` if later accepted.
It does not supply factorization, the chiral count, this parent theorem, full
K1, physical electron mass, alpha, or hydrogen.

The complex-slot factoring and chiral-count batch
`ZERO_IMPORT_HYDROGEN_KOIDE_K1_COMPLEX_SLOT_FACTORING_AND_CHIRAL_COUNT_BATCH_TARGET_DISCRIMINATOR_2026-07-05.md`
packages the next two coupled determinant-theorem inputs:
`K1_READOUT_COMPLEX_SLOT_FACTORING_RETAINED` and
`K1_CHIRAL_HOLOMORPHIC_COUNT_ON_RETAINED_REALIZATION_RETAINED`. Its
current-surface no-go and decision packet keep the readout factorization proof
separate from the retained count computation. If later accepted, the batch can
feed only `READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT` and
`CHIRAL_HOLOMORPHIC_COUNT_COMPUTED_ON_RETAINED_REALIZATION`.

These nested packets do not supply the real-vector default exclusion, full K1,
physical electron mass, alpha, or hydrogen.

## Source Surface

The narrow synthesis
`CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md`
records the one-bit residual. It also records that native `J_cs` is present on
the doublet but measure-neutral by itself.

The open lead
`SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md`
is the positive source lane for this subtarget. It verifies that a
holomorphic/chiral count would count the complex doublet mode once, while a
real/vector count counts two real components separately. It explicitly remains
an open gate because the framework still lacks the retained determinant/readout
theorem.

The fork mechanism
`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md` separates
holomorphic polarization from statistics. It records the tested four-cell
mechanism and leaves open the route to derive a native polarization selector or
to show that the readout functional factors through the doublet complex-slot
quotient.

The finite-lattice WZ/Fujikawa note
`AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md` supplies
finite staggered-grading trace structure, not a Koide determinant readout
theorem.

The staggered-Dirac realization gate
`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` supplies bounded
realization context under declared premises. It is not, by itself, this
determinant theorem and does not promote downstream Koide or hydrogen status.

The Berezin subsumption note
`OCCUPANCY_READOUT_EXPONENT_BEREZIN_SUBSUMPTION_BOUNDED_THEOREM_NOTE_2026-06-09.md`
and the retained-corner kernel coefficient note
`KOIDE_OCCUPANCY_KERNEL_COEFFICIENT_NOT_FIXED_BY_RETAINED_CORNER_MEASURE_BOUNDED_NOTE_2026-06-12.md`
are compatible future supports. They do not currently supply the determinant
theorem or the real-vector default exclusion.

This packet is subordinate to the parent selector/default-exclusion chain:
`ZERO_IMPORT_HYDROGEN_KOIDE_K1_SELECTOR_DEFAULT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md`
names the eleven-input selector target, and this packet can feed one of those
eleven inputs only after acceptance.

## Current Surface Classification

| surface | useful content | boundary here |
|---|---|---|
| fluctuation determinant object target | sixteen-input target for `K1_FLUCTUATION_DETERMINANT_OBJECT_IDENTIFICATION_RETAINED` | can feed only `FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED` if later accepted |
| complex-slot factoring and chiral-count batch target | coupled targets for `READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT` and `CHIRAL_HOLOMORPHIC_COUNT_COMPUTED_ON_RETAINED_REALIZATION` | not accepted; no parent determinant theorem |
| counting-bit synthesis note | reduces K1 to the block/orbit versus dimension/Born binary and identifies native `J_cs` | support only; no determinant theorem |
| supertrace / equivariant-index / holomorphic route | right-shaped route for counting the doublet once | open positive route; not retained here |
| det_C versus det_R fork mechanism | separates holomorphic polarization from statistics | mechanism support only; no adopted selector |
| finite WZ/Fujikawa theorem | finite staggered-grading trace structure | no Koide determinant readout theorem |
| staggered-Dirac realization gate | bounded realization context under declared premises | no downstream K1 theorem ratified here |
| Berezin subsumption note | conditional determinant-exponent route | possible future support, not current closure |
| retained corner-measure coefficient note | keeps coefficient/occupancy open under retained corner measure | no determinant shortcut |
| primitive registry | premise discipline | no determinant theorem, `r`, `Q`, `m_e`, `alpha(0)`, or hydrogen |
| merged `#5029` | runner-only Koide labeling no-go strengthening with audit success | no determinant theorem or K1 closure |
| open `#5016` | carries this hydrogen lane bundle once pushed | queue vehicle only |

The primitive registry was checked. Registered primitives are approved premise
nodes, not walls, but no primitive supplies
`K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED`,
`CHIRAL_OR_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED`,
`K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED`, `K1_COUNTING_MEASURE_RETAINED`,
`r = 1/2`, `Q = 2/3`, `m_e`, `alpha(0)`, or hydrogen.

## Dependency Boundary

| object | if this target is accepted | still not supplied |
|---|---|---|
| determinant-object subtarget | `K1_FLUCTUATION_DETERMINANT_OBJECT_IDENTIFICATION_RETAINED` | factorization, count, parent owner/audit |
| complex-slot factoring/count batch | `K1_READOUT_COMPLEX_SLOT_FACTORING_RETAINED` and `K1_CHIRAL_HOLOMORPHIC_COUNT_ON_RETAINED_REALIZATION_RETAINED` | determinant object and parent owner/audit |
| determinant theorem subtarget | `K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED` | default exclusion and selector/default-exclusion acceptance |
| parent selector/default-exclusion | gains `CHIRAL_OR_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED` | `REAL_VECTOR_TRACE_DEFAULT_EXCLUDED`, owner/audit acceptance, and the rest of the selector contract |
| K1 counting measure | no direct retained consequence | full K1 still needs the selector/default-exclusion decision and K1 owner/audit decision |
| physical electron mass | still blocked | K1, K2, native bridge, K3, branch map, K4 scale |
| hydrogen | still blocked | retained `m_e`, retained `alpha(0)`, static-source NR Coulomb limit, harness, and audit |

This target can move K1 closer by one nested theorem input. It cannot close the
selector/default-exclusion subtarget or hydrogen by itself.

## What This Moves

| before this note | after this note |
|---|---|
| the holomorphic route was a live lead inside the selector gate | the determinant theorem is a named fourteen-input subtarget |
| native `J_cs` could be overread as enough for `det_C` | `J_cs` is explicitly prerequisite/support only |
| Berezin and fork material could be overread as retained theorem closure | the readout-functional and retained-realization inputs are explicit |
| the real-vector default could be quietly collapsed into the same issue | default exclusion remains a separate parent input |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the chiral/holomorphic
determinant theorem is retained" is not shipped. The narrowed claim is:

```text
K1 chiral/holomorphic determinant theorem is a named fourteen-input target; it
is not a retained result here.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full determinant theorem contract | Accept all fourteen inputs. | OPEN POSITIVE ROUTE. This would supply the determinant theorem input, but the contract is not accepted here. |
| static `J_cs` route | Treat native complex structure as the determinant readout. | ATTEMPTED. Source synthesis marks `J_cs` as native but measure-neutral. |
| one-binary synthesis | Treat the binary reduction as proving the chiral count. | ATTEMPTED. It reduces the residual but does not identify the determinant object. |
| supertrace / holomorphic determinant | Retain a determinant/readout theorem that counts the complex doublet once. | OPEN POSITIVE ROUTE. This is the intended theorem lane. |
| det_C/det_R fork mechanism | Treat the four-cell fork as closure. | ATTEMPTED. It is mechanism support and leaves the selector open. |
| WZ/Fujikawa trace route | Treat finite staggered chirality as Koide readout. | ATTEMPTED. It supplies finite grading structure, not this determinant theorem. |
| Berezin subsumption | Treat conditional exponent bookkeeping as unconditional closure. | ATTEMPTED. It remains conditional and bounded. |
| Record/orbit premise | Adopt one slot per record outcome. | PREMISE CANDIDATE ONLY. It is not consumed here. |
| primitive shortcut | Treat approved primitives as supplying determinant, weighting, or selector content. | ATTEMPTED. Registry and source notes do not supply that content. |
| empirical comparator route | Use observed charged-lepton or hydrogen data to choose `Q = 2/3`. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is excluded. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| determinant theorem <-> real-vector trace default exclusion | no | this packet supplies at most the theorem input; default exclusion remains separate |
| determinant theorem <-> selector/default-exclusion subtarget | no | the parent eleven-input contract remains separate |
| determinant theorem <-> full K1 | no | full K1 owner/audit decision remains separate |
| determinant theorem <-> K2 R-eta exactness | no | independent |
| determinant theorem <-> physical electron mass | no | downstream composition remains open |
| owner ratification <-> audit acceptance | no | independent |

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `chiral` / `holomorphic` / `supertrace` | target theorem content, not already retained |
| `J_cs` | native prerequisite, not a measure selector |
| `det_C` / `complex slot` | mechanism support unless the readout functional is proved to factor through it |
| `Berezin` / `staggered` | conditional support, not unconditional K1 closure |
| `Record` | supplies no occupancy or weighting rule |
| `primitive` | registry checked; approved primitives supply no determinant theorem |
| `observed` / `fitted` / `PDG` | comparator data, excluded |

No determinant theorem, default exclusion, primitive shortcut, Record occupancy
premise, comparator input, owner decision, or audit decision is hidden as
background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| K1 selector/default-exclusion target | two mathematical selector inputs | this is one nested theorem input | yes |
| counting-bit synthesis note | one-binary reduction | prerequisite support | yes |
| supertrace/equivariant-index open lead | chiral/holomorphic count route | intended theorem lane | yes |
| det_C/det_R fork mechanism | mechanism and polarization split | target support, not closure | yes |
| WZ/Fujikawa note | finite graded trace structure | prerequisite context only | yes as guard |
| Berezin subsumption note | conditional determinant-exponent route | possible future support | yes |
| retained corner-measure coefficient note | coefficient non-supply and transfer route | no shortcut | yes |
| primitive registry | primitive boundary | no shortcut primitive | yes as guard |

Non-matching surfaces are not used as determinant theorem closure evidence.

### N5 - Rhetoric Audit

The negative phrase is narrow: "this packet does not retain the determinant
theorem." It is not a no-go against the theorem, and it is not a claim that the
holomorphic route is weak. It makes the route easier to review by naming the
exact missing inputs.

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| retained proof that the Koide fluctuation determinant is the chiral/holomorphic readout | `FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED` and `CHIRAL_HOLOMORPHIC_COUNT_COMPUTED_ON_RETAINED_REALIZATION` |
| retained proof that the readout functional factors through the doublet complex-slot quotient | `READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT` |
| owner/audit acceptance of this determinant packet after all inputs exist | `K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED` |
| a separate retained default-exclusion theorem | `REAL_VECTOR_TRACE_DEFAULT_EXCLUDED` in the parent selector gate |

These are live import-retirement paths, not new-axiom requirements.

### N7 - Steelman

A hostile reviewer can argue that this lane is close: the C3 carrier is native,
the doublet complex structure exists, the supertrace note computes exactly the
desired one-complex-mode count, and the Berezin/fork material gives the right
mechanism. That is why this is the right next lane. The boundary is that the
current surface still lacks the retained identification of the relevant
fluctuation determinant/readout object and its factorization through the complex
slot.

### N8 - Cross-Cycle Echo

Earlier Koide overclaims treated a candidate structure as a derived value. This
packet avoids that failure mode by separating native structure, mechanism
support, retained determinant theorem, default exclusion, full K1, and hydrogen.

## Explicit Non-Claims

- No derivation or ratification of
  `K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED`.
- No derivation or ratification of
  `CHIRAL_OR_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED`.
- No derivation or ratification of `REAL_VECTOR_TRACE_DEFAULT_EXCLUDED`.
- No derivation or ratification of `K1_SELECTOR_DEFAULT_EXCLUSION_RETAINED`.
- No derivation or ratification of `K1_COUNTING_MEASURE_RETAINED`.
- No adoption of orbit-occupancy or any owner-governed occupancy premise.
- No derivation of `r = 1/2` or `Q = 2/3`.
- No derivation of physical electron mass, `alpha(0)`, static-source Rydberg,
  or hydrogen.
- No audit status change for any cited row.
- No new axiom, primitive, Tier-A admission, or empirical import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_koide_k1_chiral_holomorphic_determinant_target_discriminator.py
```
