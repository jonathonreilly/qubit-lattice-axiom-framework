# Zero-Import Hydrogen: Koide R-Eta hw1 Physical Generation Locus Target Discriminator

**Date:** 2026-07-05
**Type:** target discriminator / Koide R-eta carrier-realization sublane
**Status:** support-only. This note does not ratify
`HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`, does not ratify
`CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED`, does not ratify
`PHYSICAL_CARRIER_CONTEXT_RETAINED`, does not derive a single fixed-point
readout, and does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_koide_r_eta_hw1_physical_generation_locus.py`

## Scope

The physical carrier-context lane requires the missing theorem

```text
CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED.
```

This discriminator isolates one immediate subinput of that theorem:

```text
HW1_PHYSICAL_GENERATION_LOCUS_RETAINED.
```

The target sentence is:

```text
the physical charged-lepton generation locus is the hw=1 C3 triplet on the
staggered/Kawamoto-Smit generation carrier.
```

This is a locus-realization target only. It does not choose one fixed-point
summand as the physical readout, does not select `r = 1/2`, does not derive
`Q = 2/3`, does not select `delta = 2/9`, and does not label the triplet as
`e`, `mu`, `tau`.

## Target Contract

`HW1_PHYSICAL_GENERATION_LOCUS_RETAINED` requires all fifteen inputs:

```text
HW1_PHYSICAL_GENERATION_LOCUS_TEXT_LOCK
MOMENTUM_TYPE_THEOREM_ACCEPTED
STAGGERED_KS_REALIZATION_SURFACE_ACCEPTED
K1_FLUX_SELECTOR_WITHIN_SURFACE_ACCEPTED
HW1_C3_TRIPLET_ALGEBRA_ACCEPTED
COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_ACCEPTED
PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED
NO_SPECIES_LABEL_BIJECTION_INPUT
NO_SINGLE_FIXED_POINT_READOUT_INPUT
NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT
NO_K1_K3_K4_OR_MASS_INPUT
NO_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

No proper subset supplies the handoff.

| input | role |
|---|---|
| HW1_PHYSICAL_GENERATION_LOCUS_TEXT_LOCK | fixes the object as physical `hw=1` generation-locus realization only |
| MOMENTUM_TYPE_THEOREM_ACCEPTED | accepts that flavor-separating observables live on the momentum/BZ factor rather than position-diagonal local readouts |
| STAGGERED_KS_REALIZATION_SURFACE_ACCEPTED | accepts the bounded staggered/Kawamoto-Smit phase, Grassmann, and chirality support surfaces at their audited scope |
| K1_FLUX_SELECTOR_WITHIN_SURFACE_ACCEPTED | accepts the flux-`-1`/K1 selector within the licensed two-class kinetic surface, without promoting the whole kinetic surface beyond its grade |
| HW1_C3_TRIPLET_ALGEBRA_ACCEPTED | accepts the `1+3+3+1` Hamming decomposition and the exact `hw=1` C3 triplet algebra |
| COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_ACCEPTED | accepts the common finite `2 x 2 x 2` representative identifying Hamming `hw=1`, AC_lambda translation triples, and C3 action at its narrow scope |
| PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED | supplies the missing theorem that this bounded staggered/KS locus is the physical charged-lepton matter-state law |
| NO_SPECIES_LABEL_BIJECTION_INPUT | excludes the downstream convention that labels the three slots as `e`, `mu`, and `tau` |
| NO_SINGLE_FIXED_POINT_READOUT_INPUT | excludes the theorem that one intensive local density is the physical readout |
| NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT | excludes `r = 1/2`, `Q = 2/3`, `delta = 2/9`, h-unit, and R-eta value selection |
| NO_K1_K3_K4_OR_MASS_INPUT | excludes occupancy/counting, physical electron species, absolute scale, branch mass map, and electron mass |
| NO_COMPARATOR_PROOF_INPUT | excludes observed lepton masses, fitted `delta`, observed `m_e`, observed `alpha(0)`, and observed hydrogen |
| NO_NEW_PRIMITIVE_OR_AXIOM | keeps this as import retirement rather than adding a primitive, axiom, or new Tier-A numerical admission |
| OWNER_RATIFICATION | owner accepts this exact locus handoff |
| AUDIT_ACCEPTANCE | independent audit accepts the target and dependency consequences |

If accepted, this target supplies exactly:

```text
HW1_PHYSICAL_GENERATION_LOCUS_RETAINED.
```

It can feed a future retained theorem for
`CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED`, but it does not supply
that theorem by itself. It also does not supply `PHYSICAL_CARRIER_CONTEXT_RETAINED`,
`SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED`, h-class, h-unit, R-eta, K2
exactness, electron mass, alpha, or hydrogen.

## Current Surface

| surface | useful content | residual |
|---|---|---|
| `FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md` | proves momentum/BZ carrier type for flavor-separating observables within the tested class | physical `hw=1` locus |
| `FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED_2026-05-31.md` | parent integration map; states half of the carrier problem is solved and the `hw=1` locus remains the recurring chirality import | retained physical-locus bridge |
| `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` | bounded synthesis of Grassmann, KS phase, corner, and algebraic species-surface clauses on declared premises | current physical-state-law/locus selection remains bounded |
| `STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md` | reduces P-KIN to a flux-`-1` selector and discharges P-SD on the K1 branch | K1 selector and surface grade remain separate |
| `P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md` | selects K1 within the licensed two-class surface at the chain's grade | no wholesale kinetic-surface or physical lepton-locus theorem |
| `STAGGERED_DIRAC_CHIRALITY_PARITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md` | derives the scalar chirality/parity sign field | no full realization gate or species-label bridge |
| `STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md` | exact `1+3+3+1` Hamming orbit decomposition | pure combinatorics, no physical species reading |
| open `#5032` common `hw=1` BZ-corner carrier identification | proposes one finite representative for Hamming `hw=1`, AC_lambda translations, and C3 action | support only; no physical locus theorem, no species reduction, no labeling |
| `ZERO_IMPORT_HYDROGEN_KOIDE_COMMON_HW1_PR5032_CARRIER_IDENTIFICATION_IMPACT_DISCRIMINATOR_2026-07-05.md` | records #5032 as `PR5032_COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_CONTEXT` and the support input `COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_ACCEPTED` | no `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`, no carrier context, no R-eta, no mass, no hydrogen |
| `STAGGERED_DIRAC_SUBSTEP3_SPECIES_REDUCTION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md` | arithmetic/species-count bridge support | not a framework physical-locus theorem |
| `KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md` | locates the matter-state spinor-law residual on the KS route | physical state-law bridge remains open |
| `CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md` | refutes the spinor-module escape and names the live KS/physical-state-law route | retained physical-state-law bridge |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md` | packages `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED` as the next state-law bridge target | target only, not retained consequence |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-05.md` | forked owner/audit contract for the state-law bridge | no retained consequence unless accepted |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md` | records current non-supply of the state-law bridge | no retained state-law consequence |
| `KOIDE_DELTA_RANK2_SELECTOR_IS_THE_CLIFFORD_CHIRALITY_DOMAIN_WALL_EDGE_BOUNDED_NOTE_2026-06-05.md` | identifies a native chirality/domain-wall selector candidate | rooting, endpoint, and physical carrier remain open |
| open `#5014`/`#5017`/`#5018` domain-wall/chirality stack | free-field domain-wall, anomaly-flow, and SM-content map support | no physical `hw=1` charged-lepton locus theorem |
| merged `#5023` / merged `#5024` Koide W4 stack | audit-readiness and gate-readiness progress | no physical `hw=1` charged-lepton locus theorem |
| approved primitives | minimal axioms, scale reference, kinetic isotropy, realized-state evaluation discipline | no locus selector, physical readout bridge, value, mass, alpha, or hydrogen |

The primitive registry was checked. The approved primitive nodes are
`minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
and `realized_state_primitive`. They are premise nodes, not walls, but their
source notes do not supply `COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_ACCEPTED`,
`HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`,
`CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED`,
`PHYSICAL_CARRIER_CONTEXT_RETAINED`, h-class, h-unit, R-eta, `m_e`,
`alpha(0)`, or hydrogen.

The companion current-surface no-go
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, merged-PR, and open-PR surfaces do
not supply `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`. This target remains a
positive import-retirement route, not a retained consequence.

The physical matter-state law bridge lane
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md`,
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-05.md`,
and
`ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md`
packages the missing `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED` input under
this target. It does not itself supply `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.

## Hydrogen Effect

If accepted, this target retires one subinput of the charged-lepton carrier
realization theorem. Hydrogen would still need the rest of that theorem, the
physical carrier-context handoff, the single fixed-point readout theorem,
h-class owner/audit acceptance, h-unit, full R-eta owner/audit acceptance,
two-ninths/radian and K2 exactness, K1, K3, K4, physical electron mass,
`alpha(0)`, and the static-source NR Coulomb limit.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "`hw=1` physical generation
locus is retained" is not shipped. The narrowed claim is:

```text
HW1_PHYSICAL_GENERATION_LOCUS_RETAINED is the next immediate import-retirement
target beneath the charged-lepton carrier realization theorem.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full locus contract | Accept all fifteen contract inputs. | OPEN POSITIVE ROUTE. This would close the handoff, but the contract is not accepted here. |
| momentum-type route | Treat the momentum/BZ carrier-type theorem as physical `hw=1` locus closure. | PARTIAL ONLY. It proves type, not which BZ locus is physical. |
| staggered realization route | Treat the realization gate as physical charged-lepton locus closure. | PARTIAL ONLY. It is bounded on declared premises and labels residuals. |
| K1 flux route | Treat K1 within-surface selection as physical lepton-locus selection. | PARTIAL ONLY. It selects a kinetic branch within a surface; physical matter-state law remains separate. |
| Hamming/C3 algebra route | Treat the `1+3+3+1` and `hw=1` triplet algebra as physical selection. | PARTIAL ONLY. It supplies exact finite algebra, not the physical locus. |
| common-carrier #5032 route | Treat common finite carrier identification as physical `hw=1` locus selection. | PARTIAL ONLY. It can supply a common-representative support input if adopted, but the physical matter-state-law bridge remains separate. |
| KS state-law route | Supply a retained KS-to-physical-matter-state-law bridge. | OPEN POSITIVE ROUTE. This is the missing theorem input. |
| domain-wall PR route | Treat #5014/#5017/#5018 as physical charged-lepton locus closure. | ATTEMPTED. They are free-field/domain-wall support and maps with named gaps, not the retained `hw=1` lepton-locus theorem. |
| W4 PR route | Treat #5023/#5024 as locus closure. | ATTEMPTED. They improve AC_phi_lambda/W4 readiness only. |
| primitive shortcut | Treat approved primitives as supplying the locus. | ATTEMPTED. Registered primitives supply no physical locus selector or readout bridge. |
| comparator route | Use observed lepton or hydrogen data. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is target data, not proof input. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| momentum carrier type <-> physical `hw=1` locus | no | type does not choose locus |
| K1 flux selector <-> physical matter-state law | no | kinetic branch and physical state law are distinct |
| `hw=1` algebra <-> physical locus | no | exact algebra is not the physical-selection theorem |
| common `hw=1` carrier identification <-> physical locus | no | common finite representative is support, not physical state-law selection |
| physical `hw=1` locus <-> single fixed-point readout | no | locus does not choose readout functional |
| physical `hw=1` locus <-> R-eta value | no | locus is upstream of value selection |
| owner ratification <-> audit acceptance | no | independent |

The collapsed target wall set is the physical matter-state-law/locus theorem,
owner ratification, and audit acceptance, with K1, KS, Hamming/C3, and
domain-wall surfaces as support rather than closure.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `momentum factor` / `BZ` | carrier-type support, not locus closure |
| `staggered/Kawamoto-Smit` | bounded route surface, not physical state-law theorem |
| `K1` / `flux-1` | within-surface kinetic selector, not physical lepton-locus theorem |
| `hw=1` / `C3 triplet` | exact algebraic target locus, not physical selection |
| `common carrier` / `#5032` | finite representative support, not physical matter-state-law closure |
| `domain-wall` / `chirality` | support and route context, not retained charged-lepton locus |
| `open PR` / `merged PR` / `audit success` | queue/status signal only |
| `registered` / `primitive` | registry checked; no shortcut |
| `observed` / `fitted` | comparator data, excluded |

No physical matter-state-law bridge, owner decision, audit decision, primitive
shortcut, or comparator input is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| momentum-type theorem | position-vs-momentum carrier type | physical `hw=1` locus still open | yes |
| realization gate | bounded staggered realization on declared premises | physical matter-state/locus handoff | yes |
| kinetic-class forcing / P-FLUX | K1 branch within licensed surface | physical locus and state law | yes |
| Hamming orbit / species reduction | exact finite corner algebra | physical charged-lepton locus | yes |
| #5032 common-carrier bridge | Hamming/AC_lambda/C3 common representative | physical matter-state law still open | yes |
| matter attachment to KS | state-law residual location | retained state-law bridge | yes |
| carrier attachment sharpening | spinor-module escape and KS route boundary | retained physical-state-law bridge | yes |
| domain-wall PRs | free-field/domain-wall support | no physical charged-lepton locus theorem | yes |
| W4 PRs | gate readiness | no physical `hw=1` locus theorem | yes |
| primitive registry | primitive boundary | no shortcut primitive | yes as guard |

Non-matching surfaces are not used as locus closure evidence.

### N5 - Rhetoric Audit

The negative phrase is narrow: "this target does not retain the physical
`hw=1` generation locus here."

| resolution | tested? | outcome |
|---|---:|---|
| momentum/BZ carrier type | yes | support only |
| K1 flux branch | yes | within-surface selector only |
| KS phase/chirality algebra | yes | bounded route support |
| `hw=1` C3 triplet algebra | yes | exact target algebra only |
| common `hw=1` finite carrier | yes | support only |
| physical matter-state-law bridge | yes | target |
| single fixed-point readout | kept separate | still separate |
| R-eta / h-class / h-unit | kept separate | still downstream |
| K2/electron mass/hydrogen | kept separate | still downstream |

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| retained KS-to-physical-matter-state-law bridge selecting the staggered `hw=1` locus as the physical charged-lepton generation locus | `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED` |
| landing and audit adoption of #5032 at its own narrow scope | `COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_ACCEPTED` support input |
| retained kinetic-surface audit that makes the K1 branch spendable beyond within-surface selection | strengthens `K1_FLUX_SELECTOR_WITHIN_SURFACE_ACCEPTED` |
| retained domain-wall/record-formation theorem tying the edge chirality to the charged-lepton locus rather than only free-field support | part of the physical locus bridge |
| owner/audit acceptance of this packet after the physical locus theorem exists | `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED` |

These are import-retirement paths, not new-axiom requirements.

### N7 - Steelman

A hostile reviewer can argue that the locus is now close: carrier type is
momentum/BZ, the staggered realization gate gives the `1+3+3+1` structure with
an exact `hw=1` triplet, #5032 proposes the common finite representative for
Hamming/AC_lambda/C3 support, the K1 branch has a strong within-surface
selector, and the domain-wall PR stack supplies fresh free-field chirality
support. That is real progress. The boundary is that none of those surfaces
proves the physical charged-lepton matter-state law selects the `hw=1` triplet
as the physical locus.

### N8 - Cross-Cycle Echo

This echoes prior carrier/readout walls that were narrowed from broad
"physical identification" language to one import-retirement target. The
mechanism that can retire this wall is a retained physical matter-state-law
bridge plus owner/audit acceptance, not a new primitive and not a comparator
fit.

**Gate result:** broad `hw=1` physical-locus-retained claim fails; narrowed
locus target passes.

## Explicit Non-Claims

- No derivation or ratification of `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.
- No adoption or ratification of open PR `#5032`, and no derivation or
  ratification of `COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_ACCEPTED`.
- No derivation or ratification of `CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED`.
- No derivation or ratification of `PHYSICAL_CARRIER_CONTEXT_RETAINED`.
- No derivation or ratification of `SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED`.
- No derivation or ratification of h-class, h-unit, R-eta, K2, electron mass,
  alpha, or hydrogen.
- No claim that #5014, #5017, #5018, #5023, or #5024 supplies the physical
  `hw=1` locus theorem.
- No new axiom, primitive, Tier-A admission, empirical import, or audit status
  change.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_koide_r_eta_hw1_physical_generation_locus.py
```
