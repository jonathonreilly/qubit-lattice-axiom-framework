# Zero-Import Hydrogen: Koide Branch Mass-Map Ratification Decision Packet

**Date:** 2026-07-04
**Type:** decision packet / import-retirement handoff
**Status:** support-only. This packet does not ratify the Koide branch mass
map, does not derive a physical electron mass, does not derive `alpha(0)`, and
does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_koide_branch_mass_map_ratification_decision_packet.py`

## Purpose

The physical electron mass packet names one Lane 6 input that was not yet
packaged as its own decision object:

```text
KOIDE_BRANCH_MASS_MAP_RETAINED.
```

This packet packages that missing input. It is narrower than the physical
electron mass handoff. It only decides the branch-to-mass composition:

```text
given a retained Brannen/Koide branch form and a retained square-root mass
readout, a supplied branch ratio and supplied scale compose as
m_k = a_l^2 [x_k(delta) / a_l]^2.
```

It does not select `delta`, does not identify the electron species, and does
not supply the absolute scale `a_l^2`.

## Decision Object

The decision object is exactly:

```text
the Koide/Brannen branch-to-mass map used by the hydrogen electron-mass lane.
```

It has five clauses:

| clause | decision text |
|---|---|
| BM.1 | branch form: the supplied branch ratios have the Brannen/Koide form `x_k/a_l = 1 + sqrt(2) cos(delta + 2 pi k / 3)` |
| BM.2 | square-root readout: the branch coordinate is a charged-lepton square-root mass amplitude, not a mass, mass-squared, or arbitrary coordinate |
| BM.3 | positive chamber or sign rule: the physical readout specifies the chamber/sign convention under which `sqrt(m_k) = x_k` rather than silently replacing it with `|x_k|` |
| BM.4 | scale composition: a supplied absolute scale `a_l^2` multiplies the dimensionless branch factors to produce a mass triple |
| BM.5 | scope boundary: phase value, physical species identity, absolute scale, comparators, and final hydrogen substitution are outside this decision |

This object is deliberately not a Koide closure theorem. It is the mass-map
composition needed between native branch/readout work and the physical
electron-mass handoff.

## Ratification Decision Contract

This packet is decision-ready only if all ten contract inputs are visible:

```text
KOIDE_BRANCH_MASS_MAP_TEXT_LOCK
BRANNEN_CIRCULANT_BRANCH_FORM_RETAINED
SQUARE_ROOT_MASS_READOUT_RETAINED
POSITIVE_CHAMBER_OR_SIGN_RULE_RETAINED
SCALE_PARAMETER_COMPOSITION_RETAINED
PHASE_SCALE_SPECIES_SCOPE_LOCK
NO_LEPTON_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

The contract means:

1. **KOIDE_BRANCH_MASS_MAP_TEXT_LOCK:** the BM.1-BM.5 text above is the full
   object being decided.
2. **BRANNEN_CIRCULANT_BRANCH_FORM_RETAINED:** the Brannen/Koide branch form is
   accepted on its own graph.
3. **SQUARE_ROOT_MASS_READOUT_RETAINED:** the branch coordinate is accepted as
   a square-root mass amplitude on the charged-lepton lane.
4. **POSITIVE_CHAMBER_OR_SIGN_RULE_RETAINED:** the sign/chamber rule needed to
   read `sqrt(m_k)` from the branch coordinate is accepted.
5. **SCALE_PARAMETER_COMPOSITION_RETAINED:** the rule
   `m_k = a_l^2 [x_k/a_l]^2` is accepted as a scale composition rule for a
   supplied `a_l^2`.
6. **PHASE_SCALE_SPECIES_SCOPE_LOCK:** the decision is only the branch mass map;
   it does not select `delta`, identify the physical electron, or supply
   `a_l^2`.
7. **NO_LEPTON_COMPARATOR_PROOF_INPUT:** observed charged-lepton masses,
   observed `m_W`, fitted `a_l`, fitted `delta`, and fitted A3 precision are
   excluded as proof inputs.
8. **NO_NEW_PRIMITIVE_OR_AXIOM:** the decision does not add an axiom, approved
   primitive, or Tier-A admitted numerical input.
9. **OWNER_RATIFICATION:** the owner explicitly accepts the branch mass-map
   composition boundary.
10. **AUDIT_ACCEPTANCE:** the normal review/audit path accepts the mass-map
    decision and its dependency consequences.

No proper subset of those ten contract inputs is a retained Koide branch
mass-map decision.

## Conditional Consequence

If all ten contract inputs are accepted, the conditional consequence is:

```text
KOIDE_BRANCH_MASS_MAP_RETAINED.
```

That consequence is Lane 6 support only. It does not by itself give:

```text
NATIVE_ZERO_SECTION_BRIDGE_RETAINED
PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED
ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED
RETAINED_ELECTRON_MASS_PHYSICAL_UNIT
RETAINED_ALPHA0_LOW_ENERGY_COULOMB
STATIC_SOURCE_RYDBERG_RETAINED
```

## Finite Map Witness

For any supplied phase `delta`, define:

```text
r_k(delta) = 1 + sqrt(2) cos(delta + 2 pi k / 3)
m_k = a_l^2 r_k(delta)^2
```

Then:

| witness | consequence |
|---|---|
| permutation of `k = 0,1,2` | gives the same unordered mass triple; no species identity follows |
| `delta = 2/9` | all three `r_k` are positive and the electron-like factor is `0.001628115093...` |
| `delta = 0` | all three `r_k` are positive but the smallest mass factor is more than 50 times larger |
| `delta = 1` | one branch is negative; the signed algebraic ratio still has `Q=2/3`, but the physical `sqrt(m_k)=|r_k|` Koide expression is different |
| scale replacement `a_l^2 -> 1.01 a_l^2` | all masses scale by `1.01`; branch factors do not supply the scale |

The witness shows why the positive chamber/sign rule and scale input are
load-bearing. It does not use observed charged-lepton masses as proof.

## Current Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC before this packet was written.

| PR | audit status | effect on this branch mass-map packet |
|---|---:|---|
| `#5013` theta native positive-class adjudication | `SUCCESS` | theta gauge-side work; no Koide branch mass map |
| `#5012` chirality domain-wall free-field note | `SUCCESS` | adjacent chirality science; no branch mass-map handoff |
| `#5011` eta twisted walk family runner | `SUCCESS` | runner stabilization; no Lane 6 branch mass-map closure |
| `#5010` YT P1 I_s re-audit packet bridge repair | `SUCCESS` | diagnostic repair; no branch mass-map closure |
| `#5009` S3 spacetime tensor primitive runner | `SUCCESS` | bounded S3 tensor context; no charged-lepton branch mass map |
| `#5008` quark mass-ratio CP probe repair | `SUCCESS` | quark context; no charged-lepton branch mass map |
| `#5007` Koide native zero-section route guard repair | `SUCCESS` | useful native-route context, not the square-root mass map |
| `#5006` static-source I1 hygiene companion | `SUCCESS` | relevant final-lane hygiene, not Lane 6 mass-map closure |
| `#4991` owner-governed Tier-A retirement | `SUCCESS` | status progress for old `AC_phi_lambda` atoms, not branch mass-map theorem closure |

Merge-state labels and branch ordering are moving review metadata, not proof
inputs here.

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md` | abstract trigonometric branch identity and formal `m_k := x_k^2` corollary | explicitly does not identify symbols with physical charged-lepton masses |
| `CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md` | algebra on abstract positive 3-vectors | square-root mass assignment remains downstream |
| `KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md` | pure `C_3` character/circulant identities | no spectral-to-physical-readout law |
| `KOIDE_SQRTM_AMPLITUDE_PRINCIPLE_NOTE_2026-04-18.md` | candidate positive-parent / one-leg-amplitude route for `sqrt(m)` | narrows the route but does not derive charged-lepton masses |
| `KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md` | bounded umbrella: circulant commutant plus conditional square-root readout implication | records square-root readout and phase/scale as open |
| `ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md` | final physical electron-mass consumer predicate | consumes `KOIDE_BRANCH_MASS_MAP_RETAINED`; does not derive it |
| approved primitives | minimal axioms and scale-reference primitive | no branch form, square-root readout, chamber rule, phase, species, or mass-map theorem |

The primitive registry was checked. Registered primitives are approved premise
nodes, not walls, but no primitive supplies a Koide branch mass map,
square-root readout law, positive chamber/sign rule, branch selector, species
identity, or charged-lepton scale.

The Koide branch mass-map current-surface no-go
`ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current surfaces do not supply `KOIDE_BRANCH_MASS_MAP_RETAINED`.
It preserves the positive route but makes the missing square-root readout,
positive chamber/sign rule, and scale-composition inputs explicit on the
current surface.

## What This Moves

| before this packet | after this packet |
|---|---|
| the physical electron-mass packet named `KOIDE_BRANCH_MASS_MAP_RETAINED` without a local handoff packet | the branch mass map has a ten-input owner/audit decision contract |
| abstract squaring could be confused with physical mass readout | square-root readout and positive chamber/sign rule are explicit inputs |
| branch factor, phase, species, and scale could be conflated | the packet separates map, phase value, species identity, and scale |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the Koide branch mass map
is retained" is not shipped. The narrowed claim is:

```text
the Koide branch-to-mass map is packaged as a decision-ready ratification
contract.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full branch mass-map decision contract | Accept all ten contract inputs. | SUPPORTED CONDITIONALLY. It is the only route in this packet that accepts `KOIDE_BRANCH_MASS_MAP_RETAINED`. |
| abstract algebraic squaring route | Treat the narrow theorem's formal `m_k := x_k^2` as the physical mass map. | ATTEMPTED. The theorem explicitly excludes identifying `x_k` with charged-lepton square-root masses. |
| square-root amplitude note alone | Treat the positive-parent route as already deriving the mass map. | ATTEMPTED. It narrows the route but says the parent and readout bridge remain open. |
| Q-only route | Use `Q=2/3` to force the branch map. | ATTEMPTED. `Q=2/3` is phase-blind and does not determine branch factors or readout. |
| phase comparator route | Use `delta = 2/9` and the smallest squared branch. | ATTEMPTED. It is comparator-sharp but does not derive square-root readout, species, or scale. |
| species sorting route | Declare the smallest branch the electron. | ATTEMPTED. Sorting does not supply the physical species bridge or square-root readout rule. |
| scale route | Use `a_l^2` to turn every branch factor into a physical mass. | ATTEMPTED. Scale multiplication needs the branch map and does not select phase or species. |
| primitive shortcut | Treat minimal axioms or scale-reference primitive as supplying the map. | RULED OUT. The registry supplies no branch form, square-root readout, chamber rule, or mass-map theorem. |
| empirical comparator route | Use observed lepton masses, observed `m_W`, fitted `delta`, or fitted `a_l`. | RULED OUT AS ZERO-IMPORT CLOSURE. Comparator data is target data, not proof input. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| Brannen branch form <-> square-root readout | no in either direction | independent |
| Brannen branch form <-> positive chamber/sign rule | no in either direction | independent |
| Brannen branch form <-> scale composition | no in either direction | independent |
| square-root readout <-> positive chamber/sign rule | no in either direction | independent |
| square-root readout <-> scale composition | no in either direction | independent |
| positive chamber/sign rule <-> scale composition | no in either direction | independent |
| comparator exclusion <-> audit acceptance | no in either direction | independent |

The collapsed decision wall is exactly the ten-input contract above.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `formal squaring` | algebraic context only until square-root mass readout is accepted |
| `positive` / `chamber` / `sign` | explicit input, not background |
| `sqrt(m)` / `amplitude` | explicit square-root readout input |
| `scale` | supplied scale parameter only; no value is derived |
| `electron-like` / `smallest branch` | comparator bookkeeping; no species identity |
| `registered` / `primitive` | registry checked; approved primitives do not supply the map |
| `observed` / `fitted` / `PDG` | excluded as proof input |

No branch form, square-root rule, chamber rule, scale value, phase value,
species identity, or comparator is left as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| Koide circulant Q narrow theorem | abstract algebraic squaring only | branch-form support, not physical map closure | yes as guard |
| Koide cone algebraic equivalence | abstract positive-vector Koide algebra | square-root assignment remains downstream | yes as guard |
| Koide circulant character bridge | pure `C_3` circulant identities | branch-form support only | yes |
| sqrt(m) amplitude principle | positive-parent route to square-root readout | square-root readout input | yes |
| Koide circulant character derivation | bounded umbrella with square-root readout open | map boundary and open readout | yes |
| physical electron mass packet | consumer of `KOIDE_BRANCH_MASS_MAP_RETAINED` | downstream use only | yes |

Non-matching surfaces are not used as branch mass-map closure evidence.

### N5 - Rhetoric Audit

The negative phrase used here is narrow: "this packet does not ratify the
Koide branch mass map."

| resolution | tested? | outcome |
|---|---:|---|
| abstract branch algebra | yes | supplies symbolic support only |
| formal `m_k := x_k^2` squaring | yes | not physical without square-root readout |
| positive-chamber square-root readout | named, not closed | explicit input |
| scale composition | named, not closed | explicit input |
| electron branch/species | kept separate | handled by physical species bridge and electron-mass packet |
| final hydrogen substitution | kept separate | needs electron mass, alpha0, NR Coulomb limit, harness, and audit |

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| Brannen/circulant algebra audit | `BRANNEN_CIRCULANT_BRANCH_FORM_RETAINED` |
| positive-parent / one-leg-amplitude route | `SQUARE_ROOT_MASS_READOUT_RETAINED` |
| positivity-window or retained sign convention | `POSITIVE_CHAMBER_OR_SIGN_RULE_RETAINED` |
| scale-composition owner/audit route | `SCALE_PARAMETER_COMPOSITION_RETAINED` |
| this packet's owner/audit route | `KOIDE_BRANCH_MASS_MAP_RETAINED` after all inputs are present |

Because these paths are live, this packet is a partial-closure handoff, not a
negative theorem.

### N7 - Steelman

A hostile reviewer can argue that the existing narrow Koide theorem already
defines `m_k := x_k^2`, the square-root amplitude note already explains why
`sqrt(m)` is the natural one-leg amplitude, and the physical electron-mass
packet only needs the product `a_l^2 rho_e(delta)`. On that reading this
packet is redundant bookkeeping.

The narrow reply is that zero-import retained status is a dependency-graph
claim. The existing algebra explicitly refuses the physical `sqrt(m)` readout,
and the square-root amplitude note leaves the positive parent/readout bridge
open. This packet makes those load-bearing inputs visible so a formal algebra
corollary or comparator fit cannot silently become a physical mass map.

### N8 - Cross-Cycle Echo

This mirrors the existing Koide firewall pattern: abstract algebra, candidate
readout, physical species identity, scale, and final hydrogen substitution are
separate layers. The present packet gives the mass-map layer the same explicit
owner/audit contract used by the native bridge, K3 species bridge, K4 scale,
and physical electron-mass packets.

**Gate result:** broad branch-mass-map-retention claim fails; narrowed Koide
branch mass-map handoff packet passes.

## Explicit Non-Claims

- No derivation or ratification of the Koide branch mass map.
- No derivation or ratification of the Brannen/circulant branch form.
- No derivation or ratification of square-root mass readout.
- No derivation or ratification of the positive chamber/sign rule.
- No derivation or ratification of a physical electron species bridge.
- No derivation of `Q=2/3`, `delta = 2/9`, `rho_e(delta)`, or `a_l^2`.
- No use of observed lepton masses, observed `m_W`, fitted `a_l`, fitted
  `delta`, or observed Rydberg as proof input.
- No derivation of physical electron mass, `alpha(0)`, static-source Rydberg,
  or full hydrogen spectroscopy.
- No new axiom, primitive, Tier-A admission, or empirical import.
- No audit status change for any cited row.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_koide_branch_mass_map_ratification_decision_packet.py
```
