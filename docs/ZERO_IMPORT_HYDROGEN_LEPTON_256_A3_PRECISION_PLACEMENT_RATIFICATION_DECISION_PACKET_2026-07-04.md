# Zero-Import Hydrogen: Lepton `1/256` A3 Precision-Placement Ratification Decision Packet

**Date:** 2026-07-04
**Type:** decision packet / import-retirement handoff
**Status:** support-only. This packet does not ratify A3, does not derive
`C_A3`, does not derive corrected `S_l`, does not derive `m_e`, does not
derive `alpha(0)`, and does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_a3_precision_placement_ratification_decision_packet.py`

## Purpose

The source-side F/L/P/R lane can, after owner/audit acceptance, supply only the
exact scaffold

```text
S_l = 1/256.
```

The A3 residual remains:

```text
N_A3 = 256.08243522600384
C_A3 = 256 / N_A3 = 0.9996780910571587
```

The A3 correction-placement discriminator showed that the same final product
can be written with `C_A3` in multiple places. This packet packages the
decision surface needed before any of those placements can be retained. It is
not a new derivation and not a fitted multiplier.

## Decision Object

The decision object is exactly:

```text
the charged-lepton A3 precision-placement decision for the 256.082435...
correction after exact source-side S_l = 1/256.
```

Four zero-import placement classes are admissible decision routes:

| route | retained theorem that must be supplied |
|---|---|
| P1 source-readout correction | `P1_SOURCE_READOUT_CORRECTION_RETAINED`: the source readout is corrected, for example `S_l = C_A3 * sigma([j])_c` or a retained nonuniform source ray gives `1/N_A3` |
| P2 weak-front matching | `P2_WEAK_FRONT_MATCHING_RETAINED`: the weak/lepton front is corrected, for example `F_phys = C_A3 * g_2 * (1/sqrt(2))` |
| P3 Koide/electron readout correction | `P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED`: the offset belongs to species, phase, pole-mass, or electron-branch readout |
| P4 direct noninteger divisor | `P4_DIRECT_NONINTEGER_DIVISOR_RETAINED`: a retained theorem derives `N_A3 = 256.082435...` directly |

The empirical-splice class P5 is not an admissible zero-import decision route.

The P1 source-readout correction current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current surfaces do not supply
`P1_SOURCE_READOUT_CORRECTION_RETAINED`. The missing theorem input is
`CORRECTED_SOURCE_READOUT_THEOREM_RETAINED`, so exact `S_l = 1/256` remains a
source scaffold rather than corrected `S_l = 1/N_A3`.

The P3 Koide/electron-readout correction current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current surfaces do not supply
`P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED`. The missing theorem input is
`KOIDE_ELECTRON_A3_CORRECTION_THEOREM_RETAINED`, so Koide route hygiene,
including `#5007`, remains P3-adjacent context rather than retained A3
readout-placement closure.

The P4 direct noninteger-divisor current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P4_DIRECT_NONINTEGER_DIVISOR_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current surfaces do not supply
`P4_DIRECT_NONINTEGER_DIVISOR_RETAINED`. The missing theorem input is
`DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED`, so exact `4^4 = 256` and the
empirical `256.082435...` target remain scaffold/target rather than retained
direct-divisor closure.

## Ratification Decision Contract

This packet is decision-ready only if all nine contract inputs are visible:

```text
A3_PLACEMENT_TEXT_LOCK
EXACT_SOURCE_SCAFFOLD_STATUS
ONE_PLACEMENT_SELECTED
PLACEMENT_THEOREM_RETAINED
NO_SOURCE_DOUBLE_COUNT
NO_EMPIRICAL_COMPARATOR_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

The contract means:

1. **A3_PLACEMENT_TEXT_LOCK:** the four admissible placement classes above are
   the full object being decided.
2. **EXACT_SOURCE_SCAFFOLD_STATUS:** the decision records whether source-side
   `S_l = 1/256` has been accepted independently of A3 data.
3. **ONE_PLACEMENT_SELECTED:** exactly one of P1, P2, P3, or P4 is selected, or
   a later packet supplies an explicit composition law that prevents double
   counting.
4. **PLACEMENT_THEOREM_RETAINED:** the selected placement has its own retained
   theorem, not just product algebra.
5. **NO_SOURCE_DOUBLE_COUNT:** the correction is not spent in source readout
   and then spent again in weak-front, Koide/electron, or direct-divisor form.
6. **NO_EMPIRICAL_COMPARATOR_INPUT:** observed `m_W`, observed charged-lepton
   masses, fitted `a_l`, fitted `N_A3`, and hydrogen spectroscopy are excluded
   as proof inputs.
7. **NO_NEW_PRIMITIVE_OR_AXIOM:** the decision does not add an axiom, approved
   primitive, or Tier-A admitted numerical input.
8. **OWNER_RATIFICATION:** the owner explicitly accepts the selected placement
   and its dependency boundary.
9. **AUDIT_ACCEPTANCE:** the normal review/audit path accepts the selected
   placement theorem and no-double-count boundary.

No proper subset of those nine contract inputs is a retained A3 placement
decision.

The A3 precision-placement current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
`A3_PRECISION_PLACEMENT_RETAINED`. The A3 placement target remains needed
unless this contract is accepted or an equivalent retained placement theorem
lands.

## Conditional Consequence

If all nine contract inputs are accepted and exactly one placement theorem is
retained, the conditional consequence is only:

```text
A3_PRECISION_PLACEMENT_RETAINED
```

This does not by itself derive `C_A3`. It says where a separately retained
`C_A3`, direct `N_A3`, or equivalent correction theorem may enter the
charged-lepton scale chain. Downstream hydrogen still needs Koide/electron
readout, retained `m_e`, retained `alpha(0)`, and the atomic harness.

## Finite Decision Witness

Let

```text
S_0 = 1/256
C   = C_A3
F_0 = g_2 * (1/sqrt(2))
R_0 = an already-derived Koide/electron readout factor
```

The following products are numerically identical if the same `C` is supplied:

```text
F_0 * (C * S_0) * R_0
(C * F_0) * S_0 * R_0
F_0 * S_0 * (C * R_0)
F_0 * (1/N_A3) * R_0
```

They are not dependency-identical. P1 spends the correction in source readout,
P2 in weak-front matching, P3 in Koide/electron readout, and P4 in a direct
noninteger-divisor theorem. The decision therefore requires one placement, or
an explicit later composition law.

## Current Open PR Alignment

Open PRs were refreshed live on 2026-07-04 before this packet was written.
The latest rows relevant to moving Koide and neighboring science all had
`audit_pipeline` result `SUCCESS`, but none supplies the A3 placement theorem:

| PR | state at refresh | effect on this A3 decision packet |
|---|---:|---|
| `#5011` eta twisted walk family runner | `SUCCESS` | runner stabilization; no A3 placement theorem |
| `#5010` YT P1 I_s re-audit packet bridge repair | `SUCCESS` | YT/P1 diagnostic repair; no charged-lepton A3 correction |
| `#5009` S3 spacetime tensor primitive runner | `SUCCESS` | bounded tensor support context; no A3 placement |
| `#5008` quark mass-ratio CP probe repair | `SUCCESS` | quark CP-area context; no lepton A3 placement |
| `#5007` Koide native zero-section route guard repair | `SUCCESS` | P3-adjacent route guard; no retained Koide/electron correction theorem |
| `#5006` static-source I1 hygiene companion | `SUCCESS` | static-source hygiene; no charged-lepton precision placement |

Merge-state labels are moving review metadata, not proof inputs here.

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md` | packages the F/L/P/R source-side decision that can conditionally yield exact `S_l = 1/256` | does not place A3 precision |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md` | quantifies `N_A3`, `C_A3`, and correction scale | does not derive a correction theorem |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md` | separates P1/P2/P3/P4/P5 placement classes | does not ratify a placement |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary for retained A3 placement | no `A3_PRECISION_PLACEMENT_RETAINED` on current retained, primitive, or open-PR surfaces |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface audit for P1 source-readout correction | no corrected-source theorem or retained P1 placement on current surfaces |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface audit for P2 weak-front matching | no charged-lepton matching theorem or retained P2 placement on current surfaces |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface audit for P3 Koide/electron-readout correction | no Koide/electron A3 correction theorem or retained P3 placement on current surfaces |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P4_DIRECT_NONINTEGER_DIVISOR_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface audit for P4 direct noninteger divisor | no direct divisor theorem or retained P4 placement on current surfaces |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_WEAK_FRONT_THRESHOLD_TARGET_DISCRIMINATOR_2026-07-04.md` | sharpens the P2 target as `F_phys = C_A3 * g_2 * (1/sqrt(2))` and `ell_A3 ~= 0.03768480771` | does not derive charged-lepton front matching |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md` | audits current P2 front-matching surfaces | current surfaces do not supply `P2_WEAK_FRONT_MATCHING_RETAINED` or `CHARGED_LEPTON_FRONT_MATCHING_RETAINED` |
| `ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md` | keeps electron-branch readout gates explicit | does not supply P3 |
| `ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md` | separates QED loop-kernel and threshold/matching work for `alpha(0)` | downstream of A3 for hydrogen |
| approved primitives | scale reference, OS0 kinetic-form isotropy, realized-state evaluation discipline | no mass ratio, correction factor, selector, readout bridge, weighting rule, or empirical match |

The primitive registry was checked. Registered primitives chain-satisfy their
declared roles, but they do not supply A3 precision placement, `C_A3`,
`N_A3`, `m_e`, `alpha(0)`, or hydrogen.

## What This Moves

| before this packet | after this packet |
|---|---|
| A3 was a precision residual plus placement discriminator | the owner/audit handoff is a single nine-input placement contract |
| product-equivalent placements could be conflated | the one-placement/no-double-count rule is explicit |
| the P2 target was sharpened but not integrated into the attack order | P2 is one admissible branch inside the A3 decision object |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "A3 is ratified" is not
shipped. The narrowed claim is:

```text
the A3 precision-placement problem is packaged as a decision-ready
ratification contract.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full A3 placement contract | Accept all nine contract inputs and exactly one retained placement theorem. | SUPPORTED CONDITIONALLY. It is the only route in this packet that accepts the A3 placement decision. |
| P1 source-readout route | Put `C_A3` in corrected source readout or derive a nonuniform source ray. | OPEN. It must not be double-counted with P2/P3/P4. |
| P2 weak-front route | Derive charged-lepton front matching or threshold placement. | OPEN. The target log is known, but the theorem is not supplied here. |
| P3 Koide/electron route | Put the offset in species, phase, pole-mass, or electron readout. | OPEN. Koide route guards sharpen this branch but do not retain it. |
| P4 direct divisor route | Derive `N_A3` directly. | OPEN. It bypasses P1/P2/P3 but must avoid fitted comparators. |
| P5 empirical splice | Fit the correction from observed masses or `m_W`. | RULED OUT AS ZERO-IMPORT ROUTE. Comparator data is target data, not proof input. |
| primitive shortcut | Treat an approved primitive as already supplying A3. | RULED OUT BY CURRENT METHODOLOGY. No registered primitive supplies the correction. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| exact source scaffold <-> A3 placement | no | exact `S_l = 1/256` does not place `C_A3` |
| placement selection <-> placement theorem | no | choosing P2 does not derive front matching |
| placement theorem <-> no-comparator boundary | no | a theorem can still be contaminated by fitted inputs unless audited |
| P1 <-> P2 | no | alternate placements; double-count risk |
| P2 <-> P3 | no | alternate placements; double-count risk |
| P3 <-> P4 | no | P4 bypasses readout correction |

The collapsed wall is not "derive every placement." It is "select one
placement with a retained theorem and no double counting."

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `placement` | explicit decision object, not background |
| `C_A3` / `N_A3` | target quantities, not proof inputs |
| `source readout` | P1 route; not assumed |
| `weak front` / `threshold` | P2 route; not assumed |
| `Koide` / `electron` | P3 route; not assumed |
| `primitive` / `registered` | registry checked; no A3 primitive exists |
| `empirical` / `observed` / `fitted` | forbidden as proof input |

No correction theorem is hidden as ordinary convention.

### N4 - Residual Matching

| cited surface | residual it attacks | match? |
|---|---|---|
| precision-correction firewall | size of the exact-256 versus `256.082435...` residual | yes |
| A3 placement discriminator | dependency placement of `C_A3` | yes |
| A3 P2 weak-front target | front-factor branch target | yes, branch only |
| source-probe decision packet | exact source-side scaffold | yes, upstream only |
| Koide/electron firewall and #5007 | P3 route guard context | partial, not retained P3 |
| primitive registry | approved primitive boundary | guard only |

No cited surface is counted as deriving the A3 correction.

### N5 - Rhetoric Audit

The negative phrase used here is narrow: "this packet does not ratify A3."
Tested resolutions:

| resolution | tested? | outcome |
|---|---|---|
| product algebra | yes | P1/P2/P3/P4 are numerically degenerate but dependency-distinct |
| exact source scaffold | yes | exact `1/256` is upstream and does not place precision |
| P2 weak-front branch | yes | target is sharp, theorem missing |
| future retained placement theorem | not closed | left open |

### N6 - Partial-Closure Path Scan

Legitimate import-retirement paths remain:

| path | what it could close |
|---|---|
| retained corrected source-readout theorem | P1 |
| retained charged-lepton weak-front matching theorem | P2 |
| retained Koide/electron correction theorem | P3 |
| retained direct noninteger-divisor theorem | P4 |
| retained composition law proving two corrections do not double-count | a later composite placement |

### N7 - Steelman

A hostile reviewer can argue that a separate decision packet is bureaucratic:
the correction is small, the P2 target log is plausible, and ordinary matching
should naturally absorb it. That steelman is useful. The response is that the
packet does not reject P2; it makes P2 an admissible placement while requiring
the matching theorem and excluding fitted comparator input.

### N8 - Cross-Cycle Echo

This mirrors prior lanes where a clean structural value was available before
the physical readout or pole-scale correction. The disciplined route is to
preserve the exact scaffold and make the final precision placement auditable
before promoting a physical mass or hydrogen claim.

**Gate result:** broad A3-retention claim fails; narrowed precision-placement
decision packet passes.

## Explicit Non-Claims

- No derivation or ratification of A3.
- No derivation of `C_A3 = 0.999678091...`.
- No derivation of `N_A3 = 256.082435...`.
- No derivation of corrected `S_l = 1/N_A3`.
- No derivation of a charged-lepton weak-front threshold correction.
- No derivation of a Koide/electron readout correction.
- No derivation of a direct noninteger-divisor theorem.
- No use of observed charged-lepton masses, observed `m_W`, fitted `a_l`, or
  fitted `N_A3` as proof inputs.
- No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, Tier-A admission, or empirical import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_a3_precision_placement_ratification_decision_packet.py
```

The verifier checks the decision contract, one-placement predicate, finite
product-degeneracy witness, source authority boundaries, open-PR alignment,
primitive boundary, no-go discipline section, and explicit non-claims.
