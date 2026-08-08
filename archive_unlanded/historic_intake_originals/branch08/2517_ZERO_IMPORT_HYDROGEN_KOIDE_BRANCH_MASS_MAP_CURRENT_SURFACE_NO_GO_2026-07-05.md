# Zero-Import Hydrogen: Koide Branch Mass-Map Current-Surface No-Go

**Date:** 2026-07-05
**Type:** current-surface no-go / import-retirement target
**Status:** support-only. This note does not ratify the Koide branch mass
map, does not derive a physical electron mass, does not derive `alpha(0)`,
does not derive static-source Rydberg, and does not claim hydrogen is
retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_koide_branch_mass_map_current_surface_no_go.py`

## Scope

The physical electron mass lane needs:

```text
KOIDE_BRANCH_MASS_MAP_RETAINED.
```

The intended map is:

```text
r_k(delta) = 1 + sqrt(2) cos(delta + 2 pi k / 3)
m_k = a_l^2 r_k(delta)^2
```

Current Koide surfaces supply strong algebraic support for the branch shape
and for `Q = 2/3`, but they do not supply the physical branch-to-mass map.
The narrow result is not "no Koide branch mass map can be retained." The
narrow result is that current retained, primitive, and open-PR surfaces do not
supply `KOIDE_BRANCH_MASS_MAP_RETAINED`.

## Branch Mass-Map Contract

A future branch mass-map handoff needs all ten inputs:

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

If all ten inputs are accepted, the conditional consequence would be:

```text
KOIDE_BRANCH_MASS_MAP_RETAINED.
```

That consequence is not supplied here. The current missing inputs include:

```text
BRANNEN_CIRCULANT_BRANCH_FORM_RETAINED
SQUARE_ROOT_MASS_READOUT_RETAINED
POSITIVE_CHAMBER_OR_SIGN_RULE_RETAINED
SCALE_PARAMETER_COMPOSITION_RETAINED
```

The cleanest current wall is the square-root readout/chamber side: the
algebraic theorem permits formal `m_k := x_k^2`, while explicitly refusing to
identify the symbols with physical charged-lepton square-root masses.

## Target Arithmetic

For the comparator phase:

```text
delta = 2/9
r_e(delta)^2 = 0.001628115093...
m_e = a_l^2 * r_e(delta)^2
```

These are target/witness quantities only. `delta`, `a_l^2`, the physical
species identity, and the branch-to-mass map are not derived in this note.

## Current-Surface Audit

| surface | supplies | does not supply |
|---|---|---|
| `KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md` | abstract branch identity and formal `m_k := x_k^2` corollary | physical charged-lepton square-root readout or mass map |
| `CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md` | abstract positive-vector Koide algebra | charged-lepton square-root mass assignment |
| `KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md` | pure C3 character/circulant identities | spectral-to-physical mass readout |
| `KOIDE_SQRTM_AMPLITUDE_PRINCIPLE_NOTE_2026-04-18.md` | positive-parent / one-leg-amplitude route shape | charged-lepton parent and retained readout bridge |
| `KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md` | bounded umbrella for circulant commutant plus conditional square-root readout implication | retained square-root readout, phase, and scale |
| `ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_RATIFICATION_DECISION_PACKET_2026-07-04.md` | ten-input owner/audit contract | current retained consequence |
| `ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md` | downstream consumer predicate | branch mass-map derivation |
| approved primitives | minimal axioms, scale reference, kinetic-form isotropy, realized-state evaluation discipline | branch form, square-root readout, chamber rule, phase, species, scale, or mass-map theorem |

The primitive registry was checked. No registered primitive supplies
`koide_branch_mass_map_primitive`, `square_root_mass_readout_primitive`,
`positive_chamber_sign_rule_primitive`,
`brannen_circulant_branch_form_primitive`, or
`scale_parameter_composition_primitive`.

## Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC. The newest rows are clean and
green, but they do not close the branch mass-map handoff:

| PR | state at refresh | branch mass-map effect |
|---|---:|---|
| `#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS` | theta gauge-side work; no charged-lepton branch mass map |
| `#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS` | adjacent chirality science; no branch mass-map handoff |
| `#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS` | runner stabilization; no Lane 6 branch mass-map closure |
| `#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS` | diagnostic repair; no branch mass-map theorem |
| `#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS` | bounded S3 tensor context; no charged-lepton branch mass map |
| `#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS` | quark context; no charged-lepton branch mass map |
| `#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS` | useful native-route context, not a square-root mass map |
| `#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS` | final-lane hygiene; no Lane 6 mass-map closure |

Merge-state labels are moving review metadata, not proof inputs.

## What This Moves

| before this note | after this note |
|---|---|
| the branch mass-map packet supplied a decision contract | the current-surface non-supply boundary is explicit |
| formal `m_k := x_k^2` could be overread as physical mass readout | algebraic squaring and charged-lepton square-root readout are separated |
| positive-parent language could be overread as retained square-root readout | the missing charged-lepton parent/readout bridge remains explicit |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the Koide branch mass map
cannot be retained" is not shipped. The narrowed claim is:

```text
the current retained, primitive, and open-PR surfaces do not supply
KOIDE_BRANCH_MASS_MAP_RETAINED.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full branch mass-map contract | Accept all ten contract inputs. | OPEN POSITIVE ROUTE. This would close the handoff, but the contract is not accepted here. |
| abstract algebraic squaring | Treat formal `m_k := x_k^2` as the physical mass map. | ATTEMPTED. The narrow theorem explicitly says the symbols are not identified with charged-lepton masses. |
| positive-parent / one-leg route | Use the square-root amplitude principle as retained readout. | ATTEMPTED. It narrows the route but leaves the charged-lepton parent and readout bridge open. |
| chamber/sign convention route | Ratify a positivity window or sign convention. | OPEN POSITIVE ROUTE. It could close one input, but no retained current-surface convention is supplied here. |
| scale-composition route | Ratify `m_k = a_l^2 r_k^2` for a supplied scale. | OPEN POSITIVE ROUTE. It would still need square-root readout and chamber/sign inputs. |
| species sorting route | Declare the smallest squared branch the electron. | ATTEMPTED. Sorting is a species/readout issue and does not supply the mass-map theorem. |
| primitive shortcut | Treat minimal axioms or approved primitives as already supplying the map. | ATTEMPTED. The registry supplies no branch form, square-root readout, chamber, or mass-map primitive. |
| empirical comparator route | Use observed lepton masses, observed `m_W`, fitted `delta`, fitted `a_l`, or Rydberg. | RULED OUT AS ZERO-IMPORT PROOF. Comparator data is target data, not proof input. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| Brannen branch form <-> square-root readout | no | independent |
| Brannen branch form <-> chamber/sign rule | no | independent |
| square-root readout <-> chamber/sign rule | no | independent |
| square-root readout <-> scale composition | no | independent |
| scale composition <-> phase/species scope lock | no | independent |
| owner ratification <-> audit acceptance | no | independent |

The collapsed wall is the ten-input contract above, with current pressure on
the square-root readout/chamber and scale-composition inputs.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `formal squaring` | algebraic corollary only |
| `positive` / `chamber` / `sign` | explicit contract input |
| `sqrt(m)` / `square-root readout` | explicit missing readout input |
| `scale` / `a_l^2` | supplied scale parameter only; no value derived |
| `electron-like` / `smallest branch` | comparator/species bookkeeping |
| `registered` / `primitive` | registry checked; no shortcut exists |

No branch form, square-root rule, chamber rule, scale value, phase value,
species identity, comparator, owner decision, or audit decision is hidden as
background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| Koide circulant Q narrow theorem | abstract Q identity and formal squaring | not physical mass-map closure | yes as guard |
| Koide cone algebraic equivalence | abstract positive-vector Koide algebra | square-root assignment remains downstream | yes as guard |
| Koide character bridge | C3/circulant identities | branch-form support only | yes |
| square-root amplitude principle | positive-parent route shape | square-root readout input remains open | yes |
| Koide character derivation | umbrella with square-root readout open | same readout residual | yes |
| branch mass-map packet | owner/audit handoff contract | current-surface non-supply boundary | yes |
| physical electron mass packet | downstream consumer | consumer only, not closure | yes |

Non-matching surfaces are not used as closure evidence.

### N5 - Rhetoric Audit

The negative phrase is narrow: "current surfaces do not supply
`KOIDE_BRANCH_MASS_MAP_RETAINED`."

| resolution | tested? | outcome |
|---|---:|---|
| abstract branch algebra | yes | support only |
| formal `m_k := x_k^2` | yes | not physical without readout |
| square-root readout | yes | open on current surfaces |
| chamber/sign rule | yes | open on current surfaces |
| scale composition | yes | open on current surfaces |
| species identity and electron mass | kept separate | downstream Lane 6 inputs |

### N6 - Partial-Closure Path Scan

Legitimate partial-closure paths remain:

| path | what it could close |
|---|---|
| retained Brannen/circulant branch-form theorem | `BRANNEN_CIRCULANT_BRANCH_FORM_RETAINED` |
| charged-lepton positive-parent / one-leg readout theorem | `SQUARE_ROOT_MASS_READOUT_RETAINED` |
| retained positivity-window or sign convention | `POSITIVE_CHAMBER_OR_SIGN_RULE_RETAINED` |
| retained scale-composition convention | `SCALE_PARAMETER_COMPOSITION_RETAINED` |
| owner/audit acceptance of the existing branch mass-map packet | `KOIDE_BRANCH_MASS_MAP_RETAINED` after all inputs are present |

These are live import-retirement paths, not new-axiom requirements.

### N7 - Steelman

A hostile reviewer can argue that this no-go is bookkeeping: the retained
algebra already gives the exact Brannen branch shape and `Q=2/3`; the
square-root amplitude note gives a concrete positive-parent route; and a
positive chamber at `delta = 2/9` makes the physical readout look like simple
multiplication by a supplied scale. That is the strongest positive route. This
note preserves it, but current surfaces still do not supply the charged-lepton
parent/readout bridge, the sign/chamber ratification, or the owner/audit
decision needed to spend the map as a retained Lane 6 input.

### N8 - Cross-Cycle Echo

This echoes prior Koide work where abstract algebra was retained before
physical readout, phase, species, and scale were retained. The disciplined
move is to keep the algebraic support visible while preventing formal
squaring, comparator phase, or sorting from silently becoming a physical mass
map.

**Gate result:** broad branch mass-map no-go fails; narrowed current-surface
non-supply claim passes.

## Explicit Non-Claims

- No derivation or ratification of `KOIDE_BRANCH_MASS_MAP_RETAINED`.
- No derivation or ratification of `BRANNEN_CIRCULANT_BRANCH_FORM_RETAINED`.
- No derivation or ratification of `SQUARE_ROOT_MASS_READOUT_RETAINED`.
- No derivation or ratification of `POSITIVE_CHAMBER_OR_SIGN_RULE_RETAINED`.
- No derivation or ratification of `SCALE_PARAMETER_COMPOSITION_RETAINED`.
- No derivation of `delta = 2/9`, `rho_e(delta)`, `a_l^2`, or a physical
  electron species identity.
- No use of observed lepton masses, observed `m_W`, fitted `delta`, fitted
  `a_l`, observed `m_e`, observed `alpha(0)`, or observed Rydberg as proof
  input.
- No derivation of physical electron mass, `alpha(0)`, static-source Rydberg,
  or full hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, Tier-A admission, or empirical import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_koide_branch_mass_map_current_surface_no_go.py
```

The verifier checks the current-surface boundary, branch-map target
arithmetic, contract predicate, primitive registry, open PR alignment, no-go
discipline markers, and explicit non-claims.
