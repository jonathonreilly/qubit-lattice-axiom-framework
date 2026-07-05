# Zero-Import Hydrogen: Absolute Charged-Lepton Scale Ratification Decision Packet

**Date:** 2026-07-04
**Type:** decision packet / import-retirement handoff
**Status:** support-only. This packet does not ratify the absolute
charged-lepton scale, does not derive `m_e`, does not derive `alpha(0)`, and
does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_absolute_charged_lepton_scale_ratification_decision_packet.py`

## Purpose

The Koide/electron-readout firewall names K4 as a separate dependency:

```text
ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED.
```

The prior source-side work made the scale problem much sharper. The
lepton-scale probe factors the charged-lepton scale handle as

```text
y_scale = g_2 * (1/sqrt(2)) * S_l,
```

and the source-probe packet packages an owner/audit route to exact

```text
S_l = 1/256.
```

The remaining precision issue is A3: the exact `256` scaffold and the
`256.082435...` comparator are not the same object. The A3 packet packages the
placement question but does not derive the correction theorem. This packet
therefore packages the K4 scale assembly as one decision object: weak-front
base, exact source singleton, one A3 placement, no double count, no comparator
input, owner, and audit.

## Decision Object

The decision object is exactly:

```text
the absolute charged-lepton scale assembly for the hydrogen electron-mass lane.
```

It has four clauses:

| clause | decision text |
|---|---|
| K4.1 | weak-front base: the charged-lepton scale front is `g_2 * (1/sqrt(2))` on its own retained dependency graph |
| K4.2 | exact source singleton: the source-probe interface supplies exact `S_l = 1/256` without using A3 data |
| K4.3 | A3 precision placement: exactly one retained placement theorem supplies the `C_A3`, direct `N_A3`, or equivalent correction location |
| K4.4 | no double count: the same A3 correction is not spent in source readout, weak-front matching, Koide/electron readout, and direct-divisor form at once |

The object deliberately excludes Koide phase/readout, physical species bridge,
`alpha(0)`, Rydberg substitution, and observed comparator values as proof
inputs.

## Ratification Decision Contract

This packet is decision-ready only if all ten contract inputs are visible:

```text
K4_SCALE_TEXT_LOCK
CHARGED_LEPTON_SCOPE_LOCK
WEAK_FRONT_BASE_RETAINED
EXACT_SOURCE_SINGLETON_RETAINED
A3_PRECISION_PLACEMENT_RETAINED
NO_SOURCE_A3_DOUBLE_COUNT
NO_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

The contract means:

1. **K4_SCALE_TEXT_LOCK:** the K4.1-K4.4 text above is the full object being
   decided.
2. **CHARGED_LEPTON_SCOPE_LOCK:** the decision is only the charged-lepton scale
   assembly needed by the electron-mass lane.
3. **WEAK_FRONT_BASE_RETAINED:** the front `g_2 * (1/sqrt(2))` is accepted on
   its own dependency graph, not imported from the observed electron scale.
4. **EXACT_SOURCE_SINGLETON_RETAINED:** the source-probe interface has been
   accepted so exact source-side `S_l = 1/256` follows without A3 data.
5. **A3_PRECISION_PLACEMENT_RETAINED:** exactly one A3 placement theorem, or an
   explicit no-double-count composition law, has been retained.
6. **NO_SOURCE_A3_DOUBLE_COUNT:** exact `S_l = 1/256` and A3 precision are not
   both used as if they independently carried the same correction.
7. **NO_COMPARATOR_PROOF_INPUT:** observed `m_W`, observed charged-lepton
   masses, fitted `a_l`, fitted `N_A3`, and hydrogen spectroscopy are excluded
   as proof inputs.
8. **NO_NEW_PRIMITIVE_OR_AXIOM:** the decision does not add an axiom, approved
   primitive, or Tier-A admitted numerical input.
9. **OWNER_RATIFICATION:** the owner explicitly accepts the scale-assembly
   convention or retained theorem boundary.
10. **AUDIT_ACCEPTANCE:** the normal review/audit path accepts the scale
    decision and its dependency consequences.

No proper subset of those ten contract inputs is a retained absolute
charged-lepton scale decision.

## Conditional Consequence

If all ten contract inputs are accepted, the conditional consequence is:

```text
ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED.
```

That consequence is K4 support only. It does not by itself give a physical
electron mass. The electron-readout predicate still requires:

```text
PHYSICAL_ELECTRON_READOUT_RETAINED
  requires NATIVE_ZERO_SECTION_BRIDGE_RETAINED
  + PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED
  + ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED.
```

The hydrogen predicate still also requires:

```text
ALPHA0_RETAINED
STATIC_SOURCE_RYDBERG_RETAINED
audit acceptance.
```

## Finite Scale Witness

The source-side and A3 packets supply exact finite bookkeeping for the K4
decision object:

| witness | exact consequence |
|---|---|
| full-cell source carrier `C = {0,1,2,3}^4` | `|C| = 4^4 = 256` |
| projective L1 singleton | for the uniform ray, `sigma([1])_c = 1/256` |
| lepton-scale front identity | `sqrt(2)/512 = (1/sqrt(2))/256` |
| A3 placement equivalence | `F_0 * (C_A3*S_0) * R_0`, `(C_A3*F_0) * S_0 * R_0`, `F_0 * S_0 * (C_A3*R_0)`, and `F_0 * (1/N_A3) * R_0` are product-equivalent only after the same correction is supplied |
| no-double-count rule | one placement or an explicit composition law is required before the correction can be spent |

The witness shows why K4 is a scale assembly decision. It does not show that
the weak-front base, exact source singleton, or A3 placement has already been
retained.

The weak-front base ratification decision packet
`ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_RATIFICATION_DECISION_PACKET_2026-07-05.md`
packages the K4.1 input `WEAK_FRONT_BASE_RETAINED` as its own ten-input
owner/audit handoff: WEAK_FRONT_BASE_TEXT_LOCK,
SU2_WEAK_COUPLING_CONTEXT_RETAINED,
CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED,
CHARGED_LEPTON_SCOPE_LOCK, UNCORRECTED_FRONT_SCOPE_LOCK,
NO_MW_OR_LEPTON_COMPARATOR_PROOF_INPUT,
NO_A3_OR_THRESHOLD_MATCHING_INPUT, NO_NEW_PRIMITIVE_OR_AXIOM,
OWNER_RATIFICATION, and AUDIT_ACCEPTANCE. If accepted, it supplies only the
uncorrected `F_0 = g_2 * (1/sqrt(2))` base front; source singleton, A3
matching, Koide/electron readout, `alpha(0)`, and hydrogen remain downstream.

The D17 block-normalization decision packet
`ZERO_IMPORT_HYDROGEN_WEAK_FRONT_D17_BLOCK_NORMALIZATION_RATIFICATION_DECISION_PACKET_2026-07-05.md`
sits one level below the weak-front-base packet. It packages
`CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED` only through
D17_BLOCK_NORMALIZATION_TEXT_LOCK, D17_STATED_BLOCK_SCOPE_ACCEPTED,
TWO_COMPONENT_UNIT_NORMALIZATION_CHECK, CHARGED_LEPTON_SCOPE_LOCK,
D17_ONLY_NO_SOURCE_SINGLETON_OR_A3_INPUT,
NO_WEAK_COUPLING_OR_FRONT_BASE_INPUT, NO_MASS_OR_COMPARATOR_PROOF_INPUT,
NO_NEW_PRIMITIVE_OR_AXIOM, OWNER_RATIFICATION, and AUDIT_ACCEPTANCE. It does
not supply `SU2_WEAK_COUPLING_CONTEXT_RETAINED`, `WEAK_FRONT_BASE_RETAINED`,
`EXACT_SOURCE_SINGLETON_RETAINED`, `A3_PRECISION_PLACEMENT_RETAINED`, or
`ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED`.

The SU2 coupling-context decision packet
`ZERO_IMPORT_HYDROGEN_WEAK_FRONT_SU2_COUPLING_CONTEXT_RATIFICATION_DECISION_PACKET_2026-07-05.md`
also sits one level below the weak-front-base packet. It packages
`SU2_WEAK_COUPLING_CONTEXT_RETAINED` only through
SU2_WEAK_COUPLING_CONTEXT_TEXT_LOCK, CL3_SU2_WEAK_CONTEXT_ACCEPTED,
BARE_G2_SYMBOL_SCOPE_LOCK, CHARGED_LEPTON_WEAK_DOUBLET_SCOPE_LOCK,
RUNNING_STRUCTURE_BOUNDARY_LOCK, NO_PHYSICAL_G2V_OR_MW_INPUT,
NO_THRESHOLD_OR_A3_MATCHING_INPUT, NO_D17_SOURCE_SINGLETON_OR_MASS_INPUT,
NO_NEW_PRIMITIVE_OR_AXIOM, OWNER_RATIFICATION, and AUDIT_ACCEPTANCE. It does
not supply physical `g_2(v)`, observed `m_W`, D17 normalization,
`WEAK_FRONT_BASE_RETAINED`, `EXACT_SOURCE_SINGLETON_RETAINED`,
`A3_PRECISION_PLACEMENT_RETAINED`, or `ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED`.

The weak-front-base current-surface no-go
`ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
`WEAK_FRONT_BASE_RETAINED`; K4 must treat the weak-front base as an unsupplied
upstream input until owner/audit acceptance or retained theorem status lands.

The exact source singleton current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
`EXACT_SOURCE_SINGLETON_RETAINED` or retained exact source-side
`S_l = 1/256`. The source-probe interface packet remains the positive route,
but K4 must treat the exact source singleton as an unsupplied upstream input
until owner ratification and audit acceptance land.

The A3 precision-placement current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
`A3_PRECISION_PLACEMENT_RETAINED`. K4 must treat A3 placement as an
unsupplied upstream input until owner/audit acceptance or retained theorem
status lands.

The A3 no-double-count composition decision packet
`ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_NO_DOUBLE_COUNT_COMPOSITION_RATIFICATION_DECISION_PACKET_2026-07-05.md`
packages the K4.4 single-spend control as its own ten-input handoff. If
accepted, it can conditionally supply `NO_SOURCE_A3_DOUBLE_COUNT` and
`NO_SOURCE_DOUBLE_COUNT`, but it does not supply
`A3_PRECISION_PLACEMENT_RETAINED`, any P1/P2/P3/P4 placement theorem,
`C_A3`, `N_A3`, or electron mass. K4 must still treat A3 placement itself as
an unsupplied upstream input.

## Current Open PR Alignment

Open PRs were refreshed on 2026-07-04 local time / 2026-07-05 UTC before this
packet was written and refreshed again on 2026-07-05 UTC before adding the
D17 block-normalization handoff. Opened and lane-relevant is the queue signal;
clean/green/check state is review metadata and not a proof input.

| PR | state at refresh | effect on this K4 decision packet |
|---|---:|---|
| `#5018` domain-wall edge content vs SM chiral fermions map | open | chirality/domain-wall edge-content work; no charged-lepton scale assembly |
| `#5017` domain-wall edge anomaly inflow via spectral flow | open | chirality/anomaly-inflow work; no charged-lepton scale assembly |
| `#5016` zero-import hydrogen retained lane bundle | open | carries this K4 and D17 handoff work |
| `#5015` wave-collapse-block01 measurement-collapse gate | open draft | measurement-collapse context; no K4 scale assembly |
| `#5014` record-formation front/domain-wall chirality | open | chirality/domain-wall context; no K4 scale assembly |
| `#5013` theta native positive-class adjudication | `SUCCESS` | theta gauge-side work; no charged-lepton scale assembly |
| `#5012` chirality domain-wall free-field note | `SUCCESS` | adjacent chirality science; no K4 scale assembly |
| `#5011` eta twisted walk family runner | `SUCCESS` | runner stabilization; no K4 scale assembly |
| `#5010` YT P1 I_s re-audit packet bridge repair | `SUCCESS` | YT/P1 diagnostic repair; no K4 scale assembly |
| `#5007` Koide native zero-section route guard repair | `SUCCESS` | Z1/Z2/Z3 route support, not K4 scale |
| `#4991` owner-governed Tier-A retirement | `SUCCESS` | status progress for old `AC_phi_lambda` atoms; not a charged-lepton scale theorem |

Merge-state labels and branch ordering are moving review metadata, not proof
inputs here.

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md` | factorization `y_scale = g_2 * (1/sqrt(2)) * S_l` and isolation of `1/256` | identifies K4 components, does not derive `1/256` or A3 |
| `ZERO_IMPORT_HYDROGEN_WEAK_FRONT_SU2_COUPLING_CONTEXT_RATIFICATION_DECISION_PACKET_2026-07-05.md` | conditional handoff for `SU2_WEAK_COUPLING_CONTEXT_RETAINED` | no physical `g_2(v)`, observed `m_W`, D17 normalization, weak-front base, exact source singleton, A3 placement, K4 scale assembly, or electron mass |
| `ZERO_IMPORT_HYDROGEN_WEAK_FRONT_D17_BLOCK_NORMALIZATION_RATIFICATION_DECISION_PACKET_2026-07-05.md` | conditional handoff for `CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED` | no weak-coupling context, weak-front base, exact source singleton, A3 placement, K4 scale assembly, or electron mass |
| `ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_RATIFICATION_DECISION_PACKET_2026-07-05.md` | conditional weak-front-base handoff | no exact source singleton, A3 correction, scale assembly, or electron mass |
| `ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary for weak-front base | retained weak-front base |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md` | source-side decision that can conditionally yield exact `S_l = 1/256` | source singleton only, not A3 or electron readout |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md` | one-placement/no-double-count decision for `C_A3` or `N_A3` | placement only, not the scale assembly by itself |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary for retained A3 precision placement | retained A3 placement remains an unsupplied upstream input |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_NO_DOUBLE_COUNT_COMPOSITION_RATIFICATION_DECISION_PACKET_2026-07-05.md` | conditional single-spend composition law for `NO_SOURCE_A3_DOUBLE_COUNT` | no A3 placement theorem, correction value, scale assembly, or electron mass |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface audit for P1 source-readout correction | no `P1_SOURCE_READOUT_CORRECTION_RETAINED` or `CORRECTED_SOURCE_READOUT_THEOREM_RETAINED` on current surfaces |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_WEAK_FRONT_THRESHOLD_TARGET_DISCRIMINATOR_2026-07-04.md` | sharp P2 weak-front target | target support only, not retained front matching |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface audit for P2 matching | no `CHARGED_LEPTON_FRONT_MATCHING_RETAINED` or `MATCHING_THEOREM_RETAINED` on current surfaces |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface audit for P3 Koide/electron readout correction | no `P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED` or `KOIDE_ELECTRON_A3_CORRECTION_THEOREM_RETAINED` on current surfaces |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P4_DIRECT_NONINTEGER_DIVISOR_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface audit for P4 direct noninteger divisor | no `P4_DIRECT_NONINTEGER_DIVISOR_RETAINED` or `DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED` on current surfaces |
| `ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md` | separates K1/K2/K3/K4 | prevents spending K4 as full `m_e` |
| `ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md` | K3 species-bridge handoff | species bridge only, not K4 scale |
| `ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md` | Z1/Z2/Z3 bridge handoff | native bridge only, not K4 scale |
| approved primitives | scale reference, OS0 kinetic-form isotropy, realized-state evaluation discipline | no dimensionless scale suppression, weak-front matching, A3 correction, selector, readout bridge, or empirical match |

The primitive registry was checked. Registered primitives are approved premise
nodes, not walls, but they also do not supply the K4 scale-assembly decision.

## What This Moves

| before this packet | after this packet |
|---|---|
| K4 was named as an absolute-scale blocker | K4 has a ten-input owner/audit decision contract |
| exact `1/256` and A3 precision could be conflated | exact source singleton and A3 placement are separated by a no-double-count rule |
| K4 could be confused with full electron mass | the packet keeps native bridge and species bridge downstream of the scale assembly |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the absolute
charged-lepton scale is retained" is not shipped. The narrowed claim is:

```text
the K4 scale assembly is packaged as a decision-ready ratification contract.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full K4 decision contract | Accept all ten contract inputs. | SUPPORTED CONDITIONALLY. It is the only route in this packet that accepts K4. |
| exact source singleton route | Treat source-side `S_l = 1/256` as the whole absolute scale. | ATTEMPTED. It omits weak-front base and A3 precision placement. |
| A3-only route | Treat `C_A3` or `N_A3` placement as the whole scale. | ATTEMPTED. It places precision but does not supply the source singleton or weak front. |
| weak-front-only route | Use `g_2 * (1/sqrt(2))` as the charged-lepton scale. | ATTEMPTED. The lepton-scale probe shows this overshoots without the `1/256` suppression. |
| Koide/readout route | Move the scale correction into Koide phase, species, or pole readout. | VALID ALTERNATIVE PLACEMENT P3, not K4 by itself. It must not double-count with K4 scale. |
| primitive shortcut | Treat approved primitives as already supplying K4. | RULED OUT BY CURRENT METHODOLOGY. The registry supplies no dimensionless scale suppression, front matching, or A3 correction. |
| empirical comparator route | Use observed `m_W`, observed charged-lepton masses, fitted `a_l`, fitted `N_A3`, or hydrogen spectroscopy. | RULED OUT AS ZERO-IMPORT CLOSURE. Comparator data is target data, not proof input. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| weak-front base <-> exact source singleton | no in either direction | independent |
| exact source singleton <-> A3 placement | no in either direction | independent |
| A3 placement <-> no-double-count rule | no in either direction | independent |
| K4 scale <-> native bridge Z1-Z3 | no in either direction | independent |
| K4 scale <-> physical species bridge K3 | no in either direction | independent |
| OWNER_RATIFICATION <-> AUDIT_ACCEPTANCE | no in either direction | independent |

The collapsed decision wall is exactly the ten-input contract above.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `weak front` | explicit K4 input, not background |
| `source singleton` | explicit K4 input, not background |
| `A3` / `C_A3` / `N_A3` | explicit precision-placement input, not proof data |
| `registered` / `primitive` | registry checked; approved primitives do not supply K4 |
| `electron` / `Koide` | downstream readout gates, not scale assembly |
| `observed` / `fitted` / `comparator` | excluded as proof input |

No source/action rule, threshold theorem, A3 placement theorem, Koide readout,
alpha, or hydrogen result is left as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| lepton-scale frontier probe | factorizes scale and isolates `1/256` | K4 component map | yes |
| source-probe decision packet | exact source-side `S_l = 1/256` handoff | exact singleton input | yes |
| A3 precision-placement packet | placement/no-double-count handoff | A3 input | yes |
| A3 P2 target discriminator | weak-front placement target | branch support only | yes, branch only |
| Koide electron firewall | K1/K2/K3/K4 separation | downstream boundary after K4 | yes |
| primitive registry notes | approved primitive boundary | guard only | yes as guard |

Non-matching surfaces are not used as K4 closure evidence.

### N5 - Rhetoric Audit

The negative phrase used here is narrow: "this packet does not ratify the
absolute charged-lepton scale."

| resolution | tested? | outcome |
|---|---:|---|
| source singleton | yes | exact `1/256` is only one K4 input |
| A3 placement | yes | placement is only one K4 input |
| weak front | yes | front base is only one K4 input |
| full electron mass | kept separate | needs native bridge and K3 species bridge |
| hydrogen spectroscopy | kept separate | downstream after `m_e` and `alpha(0)` |

### N6 - Partial-Closure Path Scan

Legitimate import-retirement paths remain:

| path | what it could close |
|---|---|
| owner/audit acceptance of the source-probe packet | exact source singleton |
| retained charged-lepton weak-front theorem | weak-front base |
| retained A3 placement theorem | precision placement |
| retained composition law preventing double count | composite K4 scale |
| retained Koide/electron correction theorem | P3 alternative, not silent K4 |

These are closure paths, not silent new axioms.

### N7 - Steelman

A hostile reviewer can argue that K4 is already nearly closed: the lepton-scale
probe gives the exact front factorization, the source-probe packet gives a
decision-ready exact `1/256`, and the A3 packet already isolates the only
remaining precision placement problem. That is a strong positive route. This
packet does not reject it; it packages the route while requiring explicit
front/base standing, source singleton standing, A3 placement standing,
no-double-count controls, no-comparator use, owner ratification, and audit
acceptance.

### N8 - Cross-Cycle Echo

This mirrors the Koide native bridge, K3 species bridge, F/L/P/R source-probe,
and A3 placement packets: a broad physical claim is reduced to a visible
decision object with no-comparator, no-new-primitive, owner, and audit
controls. The same import-retirement mechanism can work here, but only when
the K4 text and downstream electron-mass boundaries are explicit.

**Gate result:** broad K4-retention claim fails; narrowed absolute
charged-lepton scale decision packet passes.

## Explicit Non-Claims

- No derivation or ratification of the absolute charged-lepton scale.
- No derivation or ratification of the weak-front base.
- No derivation or ratification of exact source-side `S_l = 1/256`.
- No derivation or ratification of A3 precision placement.
- No derivation of `C_A3 = 0.999678091...` or `N_A3 = 256.082435...`.
- No derivation or ratification of Z1/Z2/Z3 native bridge clauses.
- No derivation or ratification of the physical electron species bridge.
- No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.
- No use of observed lepton masses, observed `m_W`, fitted `a_l`, fitted
  `N_A3`, or hydrogen spectroscopy as proof inputs.
- No new axiom, primitive, Tier-A admission, or empirical import.
- No audit status change for any cited row.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_absolute_charged_lepton_scale_ratification_decision_packet.py
```

The verifier checks the decision contract, finite scale witness, authority
boundaries, primitive registry boundaries, open-PR alignment, no-go discipline
section, and explicit non-claims.
