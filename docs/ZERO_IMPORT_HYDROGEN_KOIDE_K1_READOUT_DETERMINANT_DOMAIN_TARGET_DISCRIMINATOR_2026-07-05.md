# Zero-Import Hydrogen: Koide K1 Readout Determinant Domain Target Discriminator

**Date:** 2026-07-05
**Type:** target discriminator / Koide K1 determinant-domain subhandoff
**Status:** support-only. This note does not ratify
`K1_KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED_RETAINED`, does not ratify
`KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED`, does not ratify
`K1_FLUCTUATION_DETERMINANT_OBJECT_IDENTIFICATION_RETAINED`, does not identify
the full fluctuation determinant object, does not derive `r = 1/2` or `Q =
2/3`, does not derive the physical electron mass, and does not claim hydrogen
is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_koide_k1_readout_determinant_domain.py`

## Scope

The determinant-object target still needs:

```text
KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED
POSITIVE_KOIDE_READOUT_OBJECT_DISAMBIGUATED_FROM_VECTOR_MODULUS
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

This note attacks only the first of those four missing inputs. It names the
reviewable subtarget:

```text
K1_KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED_RETAINED.
```

If that subtarget is later accepted, its conditional consequence is only:

```text
KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED
```

That consequence does not supply the positive determinant object, does not
distinguish that object from the vector/modulus family, does not supply
complex-slot factorization, does not compute the chiral/holomorphic count, does
not close full K1, and does not derive `m_e`, `alpha(0)`, or hydrogen.

## Target Contract

`K1_KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED_RETAINED` requires all sixteen
inputs:

```text
K1_READOUT_DOMAIN_TEXT_LOCK
C3_CIRCULANT_FORM_RETAINED
BLOCK_VS_DIMENSION_FORK_REPROVEN
NATIVE_DOUBLET_COMPLEX_STRUCTURE_PRESENT
STAGGERED_DIRAC_REALIZATION_SURFACE_NAMED
GENERATION_YUKAWA_FLUCTUATION_TARGET_NAMED
READOUT_DOMAIN_IS_KOIDE_GENERATION_DETERMINANT
EFFECTIVE_POTENTIAL_VECTOR_TRACE_NOT_USED_AS_DOMAIN
DYNAMIC_VECTOR_MODULUS_PRUNING_RESPECTED
NO_GENERIC_C3_STATIC_ALGEBRA_SUBSTITUTION
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
| K1_READOUT_DOMAIN_TEXT_LOCK | the target is only the determinant/readout domain beneath the object gate |
| C3_CIRCULANT_FORM_RETAINED | the domain is attached to the retained charged-lepton C3 circulant carrier |
| BLOCK_VS_DIMENSION_FORK_REPROVEN | the `(1,1)` versus `(1,2)` fork is reproduced |
| NATIVE_DOUBLET_COMPLEX_STRUCTURE_PRESENT | native `J_cs` support is present but not treated as the domain |
| STAGGERED_DIRAC_REALIZATION_SURFACE_NAMED | the hw=1 staggered/Kawamoto-Smit realization surface is named as candidate context |
| GENERATION_YUKAWA_FLUCTUATION_TARGET_NAMED | the generation Yukawa/fluctuation determinant is the named target of the next computation |
| READOUT_DOMAIN_IS_KOIDE_GENERATION_DETERMINANT | the domain is accepted as the Koide generation determinant/readout domain, not merely route text |
| EFFECTIVE_POTENTIAL_VECTOR_TRACE_NOT_USED_AS_DOMAIN | the plain effective potential/vector trace is not used as the Koide domain |
| DYNAMIC_VECTOR_MODULUS_PRUNING_RESPECTED | pruned Hermitian/vector/modulus determinant routes are not promoted to the positive domain |
| NO_GENERIC_C3_STATIC_ALGEBRA_SUBSTITUTION | static C3 algebra and the `Q` lever are not used as a substitute for domain specification |
| NO_RECORD_OCCUPANCY_PREMISE_INPUT | Record or occupancy wording is not consumed as a readout-domain shortcut |
| NO_K2_K3_K4_OR_MASS_INPUT | no R-eta, species bridge, native bridge, scale, branch map, or electron-mass input is consumed |
| NO_COMPARATOR_PROOF_INPUT | observed lepton masses, fitted `Q`, observed `m_e`, `alpha(0)`, and Rydberg data are excluded as proof inputs |
| NO_NEW_PRIMITIVE_OR_AXIOM | the target does not add a primitive, axiom, or new Tier-A numerical admission |
| OWNER_RATIFICATION | the owner accepts this exact readout-domain specification |
| AUDIT_ACCEPTANCE | the independent review/audit path accepts the domain consequence |

No proper subset of those sixteen inputs supplies the readout-domain
specification.

The companion decision packet
`ZERO_IMPORT_HYDROGEN_KOIDE_K1_READOUT_DETERMINANT_DOMAIN_RATIFICATION_DECISION_PACKET_2026-07-05.md`
packages the same subhandoff as a sixteen-input owner/audit contract. The
matching current-surface no-go
`ZERO_IMPORT_HYDROGEN_KOIDE_K1_READOUT_DETERMINANT_DOMAIN_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, merged-PR, and open-PR surfaces do
not supply `K1_KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED_RETAINED`.

## Source Surface

The determinant-object target
`ZERO_IMPORT_HYDROGEN_KOIDE_K1_FLUCTUATION_DETERMINANT_OBJECT_TARGET_DISCRIMINATOR_2026-07-05.md`
names `KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED` as its first remaining
scientific input.

`SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md`
is the right-shaped conditional: if the generation fluctuation determinant is
chiral or holomorphic, the doublet is counted once. It also states that the
antecedent is not established and that the plain effective potential remains
the vector trace `(1,2)`.

`KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04.md`
names the next action: compute the generation Yukawa fluctuation determinant
on the hw=1 corners and determine whether it is chiral/holomorphic or
vector/real. That is domain-lane guidance, not retained domain closure.

`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md` records the
det_C versus det_R fork mechanism. It does not adopt the holomorphic
polarization and does not identify the physical Koide readout object.

`KOIDE_R_HALF_DYNAMICAL_DETERMINANT_ROUTE_PRUNING_NO_GO_NOTE_2026-06-08.md`
prunes tested Hermitian/vector/modulus determinant routes. It leaves
non-tracial, chiral, finite-gap, explicit block-measure, and
holomorphic-superpotential-style routes outside its no-go.

`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` supplies bounded
realization context under declared premises. It does not specify the Koide
readout determinant domain.

The primitive registry was checked. Registered primitives are approved premise
nodes, not walls, but no primitive supplies
`K1_KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED_RETAINED`,
`KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED`,
`K1_FLUCTUATION_DETERMINANT_OBJECT_IDENTIFICATION_RETAINED`,
`FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED`, full K1, physical electron mass,
`alpha(0)`, or hydrogen.

## Current Surface Classification

| surface | useful content | boundary here |
|---|---|---|
| determinant-object target | names this domain input | object gate remains open |
| supertrace/holomorphic open lead | right-shaped conditional | antecedent and domain not retained |
| chiral/vector Yukawa binary note | names the domain computation | computation not performed or ratified here |
| det_C/det_R fork mechanism | explains polarization fork | no adopted Koide readout domain |
| dynamical determinant route-pruning no-go | prunes tested vector/modulus routes | not the positive domain |
| staggered-Dirac realization gate | candidate realization context | no Koide readout-domain specification |
| primitive registry | premise discipline | no determinant domain, selector, mass, alpha, or hydrogen |

## Dependency Boundary

| object | if this target is accepted | still not supplied |
|---|---|---|
| readout-domain subtarget | `K1_KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED_RETAINED` | positive object disambiguation, owner/audit for object gate |
| determinant-object target | gains `KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED` | `POSITIVE_KOIDE_READOUT_OBJECT_DISAMBIGUATED_FROM_VECTOR_MODULUS`, owner/audit |
| parent determinant theorem | no direct retained consequence | object, factorization, count, owner/audit |
| K1 counting measure | no direct retained consequence | selector/default-exclusion and K1 decision remain separate |
| hydrogen | still blocked | retained `m_e`, retained `alpha(0)`, static-source NR Coulomb limit, harness, and audit |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the Koide determinant
readout domain is retained" is not shipped. The narrowed claim is:

```text
K1 Koide readout determinant domain specification is a named sixteen-input
target; it is not a retained result here.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full readout-domain contract | Accept all sixteen inputs. | OPEN POSITIVE ROUTE. This would supply only the domain input, but the contract is not accepted here. |
| static C3 algebra route | Infer the domain from the retained C3 circulant form and `Q` lever. | ATTEMPTED. This gives the binary surface, not the Koide determinant domain. |
| supertrace lead route | Treat the right-shaped conditional as already specifying the domain. | ATTEMPTED. The lead explicitly keeps the determinant antecedent open. |
| Yukawa next-action route | Treat "compute the generation Yukawa determinant" as a completed domain theorem. | ATTEMPTED. It is the next action, not closure. |
| det_C/det_R fork route | Treat the mechanism fork as domain adoption. | ATTEMPTED. The note does not adopt the holomorphic polarization. |
| effective-potential route | Use the plain effective potential as the readout domain. | ATTEMPTED. The source surface says this is still the vector trace `(1,2)`. |
| Hermitian/vector/modulus route | Use the pruned determinant family as the positive domain. | ATTEMPTED. The pruning note identifies that family as the vector/modulus readout. |
| staggered realization route | Treat realization context as domain specification. | ATTEMPTED. It names context only. |
| primitive/Record shortcut | Treat approved primitives or Record additivity as domain selection. | ATTEMPTED. The registry and primitive source notes supply no determinant domain or readout bridge. |
| empirical comparator route | Use observed lepton or hydrogen data to select the domain. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is excluded. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| readout domain <-> positive object disambiguation | no | object disambiguation remains separate |
| readout domain <-> full determinant object | no | object target still needs disambiguation and owner/audit |
| readout domain <-> complex-slot factorization | no | separate parent determinant input |
| readout domain <-> chiral/holomorphic count | no | separate parent determinant input |
| readout domain <-> real-vector default exclusion | no | separate selector input |
| readout domain <-> physical electron mass | no | downstream gates remain open |
| owner ratification <-> audit acceptance | no | independent retained-status gates |

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `domain` / `readout` | target vocabulary, not already retained |
| `generation Yukawa fluctuation determinant` | named computation target, not a completed theorem |
| `supertrace` / `holomorphic` | conditional route boundary, not domain closure |
| `effective potential` / `vector trace` | excluded substitute domain |
| `staggered` / `hw=1` | realization context, not readout-domain ratification |
| `registered` / `primitive` | checked; supplies no determinant domain, selector, or readout bridge |
| `observed` / `fitted` | comparator data, excluded |
| `owner` / `audit` | required retained-status gates |

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| determinant-object target | missing readout-domain input | readout-domain subtarget | yes |
| supertrace open lead | chiral/holomorphic determinant antecedent | route support, not closure | yes |
| chiral/vector Yukawa binary note | next computation target | domain action only | yes |
| det_C/det_R fork mechanism | polarization/statistics mechanism | support, not domain closure | yes |
| dynamical route-pruning no-go | tested vector/modulus routes | guard against wrong domain | yes as guard |
| staggered realization gate | realization context | not domain closure | yes as guard |
| primitive registry | primitive boundary | no shortcut primitive | yes as guard |

### N5 - Rhetoric Audit

The negative phrase is narrow: "this note does not retain the readout domain."
It is not a no-go against the positive route and not a claim that the domain
cannot be retained.

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| retained computation identifying the generation Yukawa fluctuation determinant domain on hw=1 | readout-domain target |
| retained proof that the plain effective potential/vector trace is not the Koide readout domain | domain exclusion support |
| retained positive selection of the Koide chiral/holomorphic readout domain | domain target and part of object support |
| owner/audit acceptance after the domain input is supplied | retained domain predicate |

### N7 - Steelman

A strong objection is that the domain is almost named already: the supertrace
open lead names the generation fluctuation determinant, the Yukawa binary note
names the hw=1 computation, and the route-pruning note removes the obvious
vector/modulus substitute. That is why this is the next lane. The remaining
gap is that the current surface has not retained the Koide generation
determinant as the readout domain.

### N8 - Cross-Cycle Echo

Prior Koide packets repeatedly distinguish named route, mechanism support, and
retained readout object. This packet follows that discipline by making the
domain specification a small owner/audit subtarget instead of promoting route
language to object closure.

## Explicit Non-Claims

- No derivation or ratification of
  `K1_KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED_RETAINED`.
- No derivation or ratification of
  `KOIDE_READOUT_DETERMINANT_DOMAIN_SPECIFIED`.
- No derivation or ratification of
  `K1_FLUCTUATION_DETERMINANT_OBJECT_IDENTIFICATION_RETAINED`.
- No derivation or ratification of
  `FLUCTUATION_DETERMINANT_OBJECT_IDENTIFIED`.
- No derivation or ratification of the parent K1 determinant theorem.
- No derivation of full K1, physical electron mass, `alpha(0)`, static-source
  Rydberg, or hydrogen.
- No audit status change for any cited row.
- No new axiom, primitive, Tier-A admission, or empirical import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_koide_k1_readout_determinant_domain.py
```
