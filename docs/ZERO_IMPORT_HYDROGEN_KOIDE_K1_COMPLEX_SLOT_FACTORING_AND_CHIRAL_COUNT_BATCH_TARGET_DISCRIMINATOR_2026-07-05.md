# Zero-Import Hydrogen: Koide K1 Complex-Slot Factoring and Chiral Count Batch Target Discriminator

**Date:** 2026-07-05
**Type:** target discriminator / batched Koide K1 determinant subhandoff
**Status:** support-only. This note does not ratify
`K1_READOUT_COMPLEX_SLOT_FACTORING_RETAINED`, does not ratify
`K1_CHIRAL_HOLOMORPHIC_COUNT_ON_RETAINED_REALIZATION_RETAINED`, does not
ratify `K1_CHIRAL_HOLOMORPHIC_DETERMINANT_THEOREM_RETAINED`, does not derive
`r = 1/2` or `Q = 2/3`, does not derive the physical electron mass, and does
not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_koide_k1_complex_slot_factorization_and_chiral_count_batch.py`

## Scope

The parent K1 chiral/holomorphic determinant theorem still needs:

```text
FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED
READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT
CHIRAL_HOLOMORPHIC_COUNT_COMPUTED_ON_RETAINED_REALIZATION
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

The determinant-object packet attacks the first item. This batch attacks the
next two science inputs together because the count lane depends on the
factorization lane:

```text
K1_READOUT_COMPLEX_SLOT_FACTORING_RETAINED
K1_CHIRAL_HOLOMORPHIC_COUNT_ON_RETAINED_REALIZATION_RETAINED
```

If later accepted, the conditional consequences are only:

```text
READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT
CHIRAL_HOLOMORPHIC_COUNT_COMPUTED_ON_RETAINED_REALIZATION
```

Those consequences do not supply the determinant object, the parent determinant
theorem, real-vector default exclusion, selector/default-exclusion, full K1,
physical electron mass, `alpha(0)`, or hydrogen.

## Factoring Contract

`K1_READOUT_COMPLEX_SLOT_FACTORING_RETAINED` requires all fifteen inputs:

```text
K1_COMPLEX_SLOT_FACTORING_TEXT_LOCK
C3_CIRCULANT_FORM_RETAINED
BLOCK_VS_DIMENSION_FORK_REPROVEN
NATIVE_DOUBLET_COMPLEX_STRUCTURE_PRESENT
FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED
GENERATION_FLUCTUATION_DETERMINANT_READOUT_CONTEXT_NAMED
READOUT_FUNCTIONAL_DEFINED_ON_ACCEPTED_OBJECT
READOUT_FUNCTIONAL_COMPLEX_LINEAR_ON_DOUBLET_QUOTIENT
REAL_VECTOR_TRACE_NOT_USED_AS_FACTORING_PROOF
NO_RECORD_OCCUPANCY_PREMISE_INPUT
NO_K2_K3_K4_OR_MASS_INPUT
NO_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

The key scientific clause is
`READOUT_FUNCTIONAL_COMPLEX_LINEAR_ON_DOUBLET_QUOTIENT`: the actual accepted
Koide readout functional must factor through the one-complex-slot quotient,
not merely coexist with the native static complex structure `J_cs`.

## Chiral Count Contract

`K1_CHIRAL_HOLOMORPHIC_COUNT_ON_RETAINED_REALIZATION_RETAINED` requires all
sixteen inputs:

```text
K1_CHIRAL_COUNT_TEXT_LOCK
C3_CIRCULANT_FORM_RETAINED
BLOCK_VS_DIMENSION_FORK_REPROVEN
NATIVE_DOUBLET_COMPLEX_STRUCTURE_PRESENT
FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED
READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT
STAGGERED_DIRAC_REALIZATION_SURFACE_NAMED
CHIRAL_OR_HOLOMORPHIC_READOUT_SELECTED_ON_RETAINED_REALIZATION
SINGLE_COMPLEX_DOUBLET_MODE_COUNT_COMPUTED
VECTOR_REAL_TWO_SLOT_COUNT_NOT_USED_AS_PROOF
NO_RECORD_OCCUPANCY_PREMISE_INPUT
NO_K2_K3_K4_OR_MASS_INPUT
NO_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

No proper subset of the fifteen factoring inputs supplies the factoring
predicate. No proper subset of the sixteen count inputs supplies the count
predicate. In particular, the count target cannot be accepted until the
factoring consequence is accepted or independently supplied.

## Source Surface

`SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md`
is the positive route. It verifies that a holomorphic/chiral count weights the
complex doublet mode `b` once, while the real/vector count weights `Re b` and
`Im b` separately. It explicitly remains open because the framework's
generation fluctuation determinant has not been shown to be chiral or
holomorphic.

`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md` supplies the
four-cell mechanism and the exact distinction between real-slot and
holomorphic-slot counting. It also states that the positive route is to derive
a native polarization selector or to show that the readout functional factors
through the doublet complex-slot quotient. It does not adopt the holomorphic
polarization.

`CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md`
shows that native `J_cs` is present but measure-neutral and that the remaining
Koide value choice is the block-count versus dimension-count bit.

`OCCUPANCY_READOUT_EXPONENT_BEREZIN_SUBSUMPTION_BOUNDED_THEOREM_NOTE_2026-06-09.md`
keeps the determinant exponent route conditional on the existing staggered
gate and K/CPT registration surface. It does not turn the route into an
unbounded K1 determinant theorem.

`AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md` and
`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` supply finite
staggered-grading and realization context. They do not identify the Koide
readout object, factor the readout functional, or compute the retained Koide
count.

Merged PR `#5031` supplies an audited A_min joint-C3 automorphism bridge for
the labeling no-go. It is selector-invariance context only here; it does not
supply K1 readout factorization, the chiral count, electron mass, or hydrogen.

The primitive registry was checked. Registered primitives are approved premise
nodes, not walls, but no primitive supplies
`K1_READOUT_COMPLEX_SLOT_FACTORING_RETAINED`,
`READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT`,
`K1_CHIRAL_HOLOMORPHIC_COUNT_ON_RETAINED_REALIZATION_RETAINED`,
`CHIRAL_HOLOMORPHIC_COUNT_COMPUTED_ON_RETAINED_REALIZATION`, full K1,
physical electron mass, `alpha(0)`, or hydrogen.

## Dependency Boundary

| object | if this target is accepted | still not supplied |
|---|---|---|
| complex-slot factoring subtarget | `K1_READOUT_COMPLEX_SLOT_FACTORING_RETAINED` | determinant object, chiral count, parent owner/audit |
| chiral count subtarget | `K1_CHIRAL_HOLOMORPHIC_COUNT_ON_RETAINED_REALIZATION_RETAINED` | determinant object, parent owner/audit |
| parent determinant theorem | gains factoring and count inputs if both are accepted | `FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED`, owner/audit |
| selector/default-exclusion | no direct retained consequence | parent determinant theorem plus default exclusion remain open |
| hydrogen | still blocked | retained `m_e`, retained `alpha(0)`, static-source NR Coulomb limit, harness, and audit |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the readout factors and
the chiral count are retained" is not shipped. The narrowed claim is:

```text
the complex-slot factoring and chiral-count inputs are named as coupled
subtargets; neither is retained here.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full factoring contract | Accept all fifteen factoring inputs. | OPEN POSITIVE ROUTE. This would supply only the factorization input. |
| full count contract | Accept all sixteen count inputs after factoring. | OPEN POSITIVE ROUTE. This would supply only the count input. |
| static `J_cs` route | Treat native complex structure as factorization and count. | ATTEMPTED. The synthesis note says `J_cs` is measure-neutral. |
| supertrace route | Treat the open lead as retained closure. | ATTEMPTED. It is right-shaped but explicitly open. |
| det_C/det_R mechanism route | Treat the four-cell fork as adopted polarization. | ATTEMPTED. The mechanism note does not adopt holomorphic polarization. |
| Berezin subsumption route | Treat conditional exponent bookkeeping as unconditional theorem closure. | ATTEMPTED. The note remains bounded and conditional. |
| WZ/Fujikawa route | Treat finite staggered grading as Koide readout. | ATTEMPTED. It supplies trace/index context, not the Koide determinant readout. |
| #5031 selector-invariance route | Treat A_min selector invariance as K1 determinant factorization. | ATTEMPTED. It repairs labeling no-go support, not Koide readout factorization. |
| primitive/Record shortcut | Treat approved primitives or Record as supplying a weighting/count selector. | ATTEMPTED. The registry supplies no determinant, weighting, normalization, probability, or readout bridge. |
| empirical comparator route | Use observed charged-lepton or hydrogen data. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is excluded. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| determinant object <-> complex-slot factoring | no | object identification is a separate accepted input |
| complex-slot factoring <-> chiral count | no | factoring is prerequisite; count still needs retained realization computation |
| chiral count <-> parent determinant theorem | no | parent owner/audit and object inputs remain separate |
| parent determinant theorem <-> real-vector default exclusion | no | selector/default-exclusion remains separate |
| K1 determinant inputs <-> K2/K3/K4/electron mass | no | downstream gates remain separate |
| owner ratification <-> audit acceptance | no | independent retained-status gates |

### N3 - Hidden-Wall Scan

Terms such as `complex slot`, `holomorphic`, `chiral`, `supertrace`,
`Berezin`, `staggered`, `registered`, `merged PR`, and `canonical` are route or
status terms unless a retained theorem supplies the exact factorization or
count predicate. No determinant object, primitive shortcut, comparator input,
owner decision, or audit decision is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| parent determinant target | missing factorization and count inputs | this batch | yes |
| supertrace open lead | chiral/holomorphic count route | count support, not closure | yes |
| det_C/det_R fork mechanism | polarization/count mechanism | factorization support, not closure | yes |
| one-bit synthesis | unforced count bit and measure-neutral `J_cs` | no shortcut from `J_cs` | yes |
| Berezin subsumption note | conditional determinant exponent route | possible support, not unconditional closure | yes |
| WZ/Fujikawa and staggered gate | finite grading and realization context | no Koide readout theorem | yes as guard |
| #5031 A_min automorphism bridge | labeling no-go selector invariance | no K1 determinant factorization/count | yes as guard |
| primitive registry | primitive boundary | no shortcut primitive | yes as guard |

### N5 - Rhetoric Audit

The negative phrase is narrow: current artifacts do not retain the two named
subtargets. It is not a no-go against the supertrace route and not a claim that
factorization or count cannot be retained.

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain: identify the Koide determinant object;
prove the accepted readout functional is complex-linear on the doublet quotient;
compute the single complex doublet count on the retained realization; then seek
owner/audit acceptance.

### N7 - Steelman

A hostile reviewer can argue that this pair is almost closed: `J_cs` is native,
the supertrace note computes exactly the desired count, and the fork/Berezin
notes explain the exponent mechanism. This packet accepts that this is the
right route. The remaining gap is that right-shaped support is not the same as
a retained proof that the actual Koide readout functional factors through that
complex slot and computes the count on the accepted realization.

### N8 - Cross-Cycle Echo

The recurring Koide failure mode is promoting a candidate route to a retained
readout once the algebra and desired cell are visible. This packet keeps the
candidate route live while separating factorization, count, owner, and audit.

## Explicit Non-Claims

- No derivation or ratification of `K1_READOUT_COMPLEX_SLOT_FACTORING_RETAINED`.
- No derivation or ratification of
  `READOUT_FUNCTIONAL_FACTORS_THROUGH_COMPLEX_SLOT`.
- No derivation or ratification of
  `K1_CHIRAL_HOLOMORPHIC_COUNT_ON_RETAINED_REALIZATION_RETAINED`.
- No derivation or ratification of
  `CHIRAL_HOLOMORPHIC_COUNT_COMPUTED_ON_RETAINED_REALIZATION`.
- No derivation or ratification of the parent determinant theorem, selector,
  full K1, physical electron mass, `alpha(0)`, static-source Rydberg, or
  hydrogen.
- No audit status change for any cited row.
- No new axiom, primitive, Tier-A admission, or empirical import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_koide_k1_complex_slot_factorization_and_chiral_count_batch.py
```
