# Zero-Import Hydrogen: Absolute Charged-Lepton Scale Current-Surface No-Go

**Date:** 2026-07-05
**Type:** current-surface no-go / import-retirement target
**Status:** support-only. This note does not ratify the absolute
charged-lepton scale, does not derive a physical electron mass, does not
derive `alpha(0)`, does not derive static-source Rydberg, and does not claim
hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_absolute_charged_lepton_scale_current_surface_no_go.py`

## Scope

The physical electron mass lane consumes one K4 input:

```text
ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED.
```

The absolute charged-lepton scale decision packet packages that input as the
conditional consequence of weak-front base, exact source singleton, exactly
one A3 precision placement, no source/A3 double count, owner ratification, and
audit acceptance.

Current K4 surfaces supply route support, a decision contract, finite
bookkeeping, and sharper upstream current-surface boundaries. They do not
supply the retained K4 handoff. The narrow result is not "the framework cannot
retain the absolute charged-lepton scale." The narrow result is that current
retained, primitive, and open-PR surfaces do not supply
`ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED`.

## K4 Scale Contract

A future K4 handoff needs all ten inputs:

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

If all ten inputs are accepted, the conditional consequence would be:

```text
ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED.
```

That consequence is not supplied here. The current missing upstream inputs
include:

```text
WEAK_FRONT_BASE_RETAINED
EXACT_SOURCE_SINGLETON_RETAINED
A3_PRECISION_PLACEMENT_RETAINED
```

The no-double-count rule also remains load-bearing: the same A3 correction
cannot be spent as source readout, weak-front matching, Koide/electron
readout, and direct divisor unless an explicit retained composition theorem
permits that spending.

## Target Arithmetic

The K4 target is the charged-lepton scale factor:

```text
y_scale = g_2 * (1/sqrt(2)) * S_l
S_0 = 1/256
N_A3 = 256.08243522600384
C_A3 = 256 / N_A3 = 0.9996780910571587
S_l = C_A3 * S_0 = 1/N_A3
```

The one-correction placements are product-equivalent after the same retained
correction is supplied:

```text
P1: F_0 * (C_A3 * S_0) * R_0
P2: (C_A3 * F_0) * S_0 * R_0
P3: F_0 * S_0 * (C_A3 * R_0)
P4: F_0 * (1/N_A3) * R_0
```

They are not dependency-equivalent. Spending two placements gives a
`C_A3^2` product and is not the K4 target.

These quantities are target/witness quantities only. `g_2`, exact `S_l`,
`C_A3`, `N_A3`, `m_e`, `alpha(0)`, and hydrogen are not derived in this note.

## Current-Surface Audit

| surface | supplies | does not supply |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md` | ten-input owner/audit K4 handoff | current retained consequence |
| `ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_RATIFICATION_DECISION_PACKET_2026-07-05.md` | weak-front-base contract for `F_0 = g_2 * (1/sqrt(2))` | exact source singleton, A3 placement, or K4 assembly |
| `ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary for weak-front base | `WEAK_FRONT_BASE_RETAINED` |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md` | source-side F/L/P/R decision contract | current retained exact source singleton |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary for exact source singleton | `EXACT_SOURCE_SINGLETON_RETAINED` |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md` | one-placement/no-double-count A3 decision contract | current retained A3 placement |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md` | current-surface non-supply boundary for retained A3 placement | `A3_PRECISION_PLACEMENT_RETAINED` |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md` | P1 boundary | no retained corrected source-readout placement |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md` | P2 boundary | no retained weak-front matching placement |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md` | P3 boundary | no retained Koide/electron readout correction placement |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P4_DIRECT_NONINTEGER_DIVISOR_CURRENT_SURFACE_NO_GO_2026-07-05.md` | P4 boundary | no retained direct noninteger divisor placement |
| `LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md` | factorization target and `1/256` isolation | retained K4 scale assembly |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md` | finite `N_A3` and `C_A3` target firewall | correction theorem or retained placement |
| `ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md` | downstream consumer predicate | K4 scale derivation |
| approved primitives | minimal axioms, scale reference, kinetic-form isotropy, realized-state evaluation discipline | weak front, exact source singleton, A3 placement, K4 scale, electron mass, or hydrogen |

The primitive registry was checked. No registered primitive supplies
`absolute_charged_lepton_scale_primitive`, `weak_front_base_primitive`,
`exact_source_singleton_primitive`, `a3_precision_placement_primitive`,
`charged_lepton_scale_primitive`, or `electron_mass_primitive`.

## Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC. The newest rows are clean and
green, but they do not close the K4 scale handoff:

| PR | state at refresh | K4 effect |
|---|---:|---|
| `#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS` | theta gauge-side work; no charged-lepton scale |
| `#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS` | adjacent chirality science; no K4 scale |
| `#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS` | runner stabilization; no K4 scale |
| `#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS` | diagnostic repair; no K4 scale |
| `#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS` | bounded S3 tensor context; no charged-lepton scale |
| `#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS` | quark context; no lepton K4 scale |
| `#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS` | useful Koide native-route context, not K4 scale assembly |
| `#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS` | final-lane hygiene; no Lane 6 scale closure |
| `#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS` | status progress for old `AC_phi_lambda` atoms, not theorem closure |

Merge-state labels are moving review metadata, not proof inputs.

## What This Moves

| before this note | after this note |
|---|---|
| the K4 packet supplied a decision contract | the current-surface non-supply boundary is explicit |
| weak-front, exact source, and A3 support could be overread as a composed scale | the three independent upstream handoffs remain separate |
| Koide/native progress could be overread as K4 scale closure | Koide context remains downstream or adjacent unless it supplies a retained A3/K4 input |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the absolute
charged-lepton scale cannot be retained" is not shipped. The narrowed claim is:

```text
the current retained, primitive, and open-PR surfaces do not supply
ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full K4 contract | Accept all ten contract inputs. | OPEN POSITIVE ROUTE. This would close the handoff, but the contract is not accepted here. |
| weak-front base alone | Treat `F_0 = g_2 * (1/sqrt(2))` as the whole scale. | ATTEMPTED. It omits exact source singleton and A3 placement. |
| exact source singleton alone | Treat exact `S_l = 1/256` as the full K4 scale. | ATTEMPTED. It omits weak-front base and A3 placement. |
| A3 placement alone | Treat `C_A3` or `N_A3` as the scale. | ATTEMPTED. It is a correction placement, not the front/source/scale assembly. |
| placement product shuffle | Move the same A3 correction through P1/P2/P3/P4 and spend more than one placement. | ATTEMPTED. Product-equivalence holds for one supplied correction only; double counting gives `C_A3^2`. |
| Koide/native route | Treat `#5007` or Koide route support as the scale theorem. | ATTEMPTED. It is Koide native/readout context, not a K4 scale handoff. |
| primitive shortcut | Treat approved primitives as already supplying K4. | RULED OUT. The registry supplies no weak-front base, source singleton, A3 placement, or charged-lepton scale primitive. |
| empirical comparator route | Use observed lepton masses, observed `m_W`, fitted `a_l`, fitted `N_A3`, observed `m_e`, or Rydberg. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is target data, not proof input. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| weak-front base <-> exact source singleton | no | independent |
| weak-front base <-> A3 placement | no | independent |
| exact source singleton <-> A3 placement | no | independent |
| A3 placement <-> no-double-count rule | no | independent |
| K4 scale <-> physical electron species bridge | no | independent |
| K4 scale <-> Koide branch mass map | no | independent |
| owner ratification <-> audit acceptance | no | independent |

The collapsed wall is the ten-input K4 contract, with current pressure on the
weak-front base, exact source singleton, A3 placement, and no-double-count
inputs.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `weak front` / `F_0` | explicit K4 input |
| `source singleton` / `S_l = 1/256` | explicit K4 input |
| `A3` / `C_A3` / `N_A3` | explicit precision-placement input |
| `double count` / `placement` | explicit composition rule |
| `scale` / `a_l^2` | explicit K4 target, not electron mass |
| `registered` / `primitive` | registry checked; no shortcut exists |
| `observed` / `fitted` / `comparator` | excluded as proof input |

No weak-front theorem, exact source theorem, A3 placement theorem, composition
law, owner decision, or audit decision is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| K4 ratification packet | owner/audit handoff | current-surface non-supply boundary | yes |
| weak-front current-surface no-go | `WEAK_FRONT_BASE_RETAINED` non-supply | direct K4 input | yes |
| exact-source current-surface no-go | `EXACT_SOURCE_SINGLETON_RETAINED` non-supply | direct K4 input | yes |
| A3 precision-placement current-surface no-go | `A3_PRECISION_PLACEMENT_RETAINED` non-supply | direct K4 input | yes |
| P1/P2/P3/P4 no-gos | individual A3 placement non-supply | A3 sub-input support | yes |
| lepton-scale frontier probe | factorization target | target support, not closure | yes |
| physical electron mass packet | downstream consumer | consumer only, not closure | yes |

Non-matching surfaces are not used as K4 closure evidence.

### N5 - Rhetoric Audit

The negative phrase is narrow: "current surfaces do not supply
`ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED`."

| resolution | tested? | outcome |
|---|---:|---|
| weak-front base | yes | current-surface non-supply recorded |
| exact source singleton | yes | current-surface non-supply recorded |
| A3 placement aggregate | yes | current-surface non-supply recorded |
| individual A3 placements P1-P4 | yes | current-surface non-supply recorded |
| composition/no-double-count rule | yes | explicit K4 input |
| physical electron mass | kept separate | still needs species/readout and branch mass-map inputs |

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| retained weak-front base theorem or owner/audit adoption | `WEAK_FRONT_BASE_RETAINED` |
| retained exact source singleton or owner/audit adoption | `EXACT_SOURCE_SINGLETON_RETAINED` |
| retained A3 placement theorem or owner/audit adoption | `A3_PRECISION_PLACEMENT_RETAINED` |
| retained composition law preventing source/A3 double count | `NO_SOURCE_A3_DOUBLE_COUNT` for the accepted handoff |
| owner/audit acceptance of the existing K4 packet | `ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED` after all inputs are present |

These are live import-retirement paths, not new-axiom requirements.

### N7 - Steelman

A hostile reviewer can argue that K4 is now close: weak front has a decision
packet, exact source has a source-probe contract, A3 has four sharpened
placements plus an aggregate decision packet, and all product placements give
the same finite target if exactly one correction is supplied. That is the
strongest positive route. This note preserves it, but current surfaces still
do not supply the three upstream retained inputs or the owner/audit accepted
composition needed to spend them as the absolute charged-lepton scale.

### N8 - Cross-Cycle Echo

This echoes the exact-source and A3 campaign pattern: finite target arithmetic
and product-equivalent bookkeeping sharpen the route before the retained
handoff exists. The disciplined move is to keep weak front, exact source, A3
placement, and composition/no-double-count separate until the K4 contract is
accepted without comparator proof input.

**Gate result:** broad K4 no-go fails; narrowed current-surface non-supply
claim passes.

## Explicit Non-Claims

- No derivation or ratification of `ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED`.
- No derivation or ratification of `WEAK_FRONT_BASE_RETAINED`.
- No derivation or ratification of `EXACT_SOURCE_SINGLETON_RETAINED`.
- No derivation or ratification of `A3_PRECISION_PLACEMENT_RETAINED`.
- No derivation of `C_A3 = 0.999678091...` or `N_A3 = 256.082435...`.
- No derivation or ratification of any P1/P2/P3/P4 placement theorem.
- No derivation of `a_l^2`, `m_e`, `alpha(0)`, static-source Rydberg, or
  hydrogen.
- No use of observed charged-lepton masses, observed `m_W`, fitted `a_l`,
  fitted `N_A3`, observed `m_e`, or Rydberg spectroscopy as proof input.
- No audit status change for any cited row.
- No new axiom, primitive, Tier-A admission, or empirical import.
