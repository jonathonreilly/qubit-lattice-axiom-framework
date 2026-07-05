# Zero-Import Hydrogen: AC R-Eta Upstream Cluster Impact Discriminator

**Date:** 2026-07-05
**Type:** merged-main / open-PR impact discriminator for Koide K2 R-eta
**Status:** support-only. This note does not derive `R_ETA_H_CLASS_RETAINED`,
does not derive `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`, does not derive
`R_ETA_READOUT_IDENTIFICATION_RETAINED`, does not derive
`K2_R_ETA_EXACTNESS_RETAINED`, does not derive `m_e`, does not derive
`alpha(0)`, and does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_ac_r_eta_upstream_cluster_impact_discriminator.py`

## Scope

The 2026-07-05 refresh found new AC/R-eta material on `origin/main` plus one
still-open AC/R-eta PR. This note records the hydrogen-facing consequence:
the new material sharpens K2 route boundaries, but it does not supply any
spendable retained hydrogen input.

| source signal | state at refresh | hydrogen-facing impact |
|---|---:|---|
| commit `8b2bea3148` / PR `#4982` AC occupancy formation non-supply | landed on `origin/main`; PR closed without GitHub merge flag | K1/AC(i) occurrence is not occupancy dictionary closure |
| commit `4a47f56db0` / PR `#4983` AC R-eta doublet-clock no-go | landed on `origin/main`; PR closed without GitHub merge flag | clock/rate typing only; no R-eta normalization |
| commit `c671996ebf` / PR `#4984` AC R-eta direct-license no-go | landed on `origin/main`; PR closed without GitHub merge flag | splits direct license into h-class plus h-unit; no retirement |
| commit `8ca8adaa0b` / PR `#4985` AC R-eta h-unit primitive no-go | landed on `origin/main`; PR closed without GitHub merge flag | approved primitives do not supply identity-radian `beta = 1` |
| commit `8c033532f1` / PR `#4986` AC R-eta h-class stretch no-go | landed on `origin/main`; PR closed without GitHub merge flag | first-principles h-class stretch leaves class coefficient free |
| commit `89768b461c` AC R-eta occurrence axiom-hygiene no-go | landed on `origin/main` after the PR-state refresh | `Records form` supplies generic occurrence only; no event law, rate normalization, or R-eta readout license |
| commit `e2d1dec095` AC measure binary axiom-update no-go | landed on `origin/main` after the PR-state refresh | updated axioms/primitives do not select the AC(i) doublet reading/occupancy binary |
| PR `#4981` AC R-eta C3 ratification non-supply | open and lane-relevant | C3 ratification context only; no physical density-read-as-angle license |

These states matter because the user workflow treats opened lane-relevant PRs
as useful queue signals while the reviewer may land only the relevant commit.
Here, `#4982` through `#4986` are not GitHub-merged PRs, but their science
commits are present on `origin/main`; `89768b461c` and `e2d1dec095` are
additional landed-main science commits; `#4981` remains an open route signal.

## Hydrogen-Facing Classification

| R-eta object | cluster effect | hydrogen boundary |
|---|---|---|
| occupancy formation append | separates generic Record occurrence from AC(i) occupancy dictionary | no K1 counting-measure closure |
| occurrence axiom-hygiene boundary | separates `Records form` from coherence-event law, activation/rate normalization, and readout license | no R-eta occurrence-route closure |
| measure binary axiom-update boundary | checks that updated axioms/primitives do not choose count-once versus count-twice statistics | no K1/AC(i) measure binary closure |
| doublet clock | exposes the free `|b| / a_act` rate-normalization relation | no K2 R-eta readout retirement |
| direct R-eta license | splits the shortcut into h-class plus h-unit | no full `A_R-eta` retirement |
| h-unit approved primitive check | rules out laundering `beta = 1` through approved primitives | no `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED` |
| h-class first-principles stretch | shows C3-additive scalar class coefficient remains free | no `R_ETA_H_CLASS_RETAINED` |
| C3 ratification non-supply PR | records C3 context/naming support as non-closure | no physical density-read-as-angle theorem |
| K2 exactness | better residual split only | no `K2_R_ETA_EXACTNESS_RETAINED` |
| hydrogen | downstream | no `m_e`, no `alpha(0)`, no static-source Rydberg closure |

The useful progress is dependency leverage: K2 is now less vague. The live
R-eta readout target is h-class plus h-unit, with separate physical carrier,
single fixed-point readout, identity-unit, owner, and audit obligations. That
is closer to a retained calculation path, but it is not retained hydrogen.

## Finite Witness Summary

The cluster's hydrogen-relevant finite checks can be stated without importing
the upstream notes as new local source files:

```text
L = 2/9
S_sum = 3 L = 2/3
```

For h-class, a C3-covariant additive scalar on one three-cell orbit has

```text
I_alpha(x0, x1, x2) = alpha (x0 + x1 + x2).
```

The fixed-locus-density member on `(1,1,1)` has `alpha = 2/27`, but
`alpha = 0`, `1/9`, `1/3`, `1`, and `2/27` are all additive and C3-invariant
on the same finite frame. Selecting `2/27` is the h-class readout content.

For h-unit, after the fixed-locus class is selected, the angle-family is

```text
Phi_beta = beta S_sum.
```

Only `beta = 1` gives `Phi = 2/3`. Approved primitives supply no such
identity-radian coefficient, and using `c_t/c_s = 1` or another unrelated
numeric `1` would be a type error without an extra readout bridge.

For the doublet-clock route,

```text
Omega(delta) = 2 sqrt(3) sin(delta).
```

At `delta = 2/9`, this is not `2/3`. Event-rate recovery needs an additional
normalization relation between `|b|` and `a_act`, which is not supplied by the
current retained/primitive/merged-PR/open-PR surface.

## Current Packet Wiring

| hydrogen packet | required treatment of this cluster |
|---|---|
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md` | cite the h-class stretch as support for non-supply, not closure |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_CURRENT_SURFACE_NO_GO_2026-07-05.md` | cite the h-unit primitive boundary as support for non-supply, not closure |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md` | keep h-class and h-unit as independent subinputs |
| `ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_CURRENT_SURFACE_NO_GO_2026-07-05.md` | treat the cluster as K2 residual sharpening, not exactness |
| `ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md` | update K1/K2 standing to include the landed cluster |
| `ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md` | record `#4982`-`#4986`, `89768b461c`, and `e2d1dec095` as landed-main support and `#4981` as open context |

## Primitive Boundary

The primitive registry was checked. Registered primitives are approved premise
nodes, not walls, but no primitive supplies h-class, h-unit, R-eta readout,
K2 exactness, a phase selector, a physical readout bridge, `m_e`, `alpha(0)`,
or hydrogen.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the new AC/R-eta cluster
closes K2 for hydrogen" is not shipped. The narrowed claim is:

```text
the AC/R-eta upstream cluster sharpens K2 h-class/h-unit residuals and prunes
current shortcuts, but does not supply retained K2, electron-mass, alpha, or
hydrogen inputs.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| occupancy formation route | Treat `Records form` as AC(i) occupancy dictionary closure. | ATTEMPTED. The landed formation note separates occurrence from dictionary/rule selection. |
| occurrence axiom route | Treat the 2026-07-04 Record append as R-eta event/readout closure. | ATTEMPTED. The landed occurrence hygiene note leaves event law, rate normalization, and readout license open. |
| measure binary route | Treat the updated axioms/primitives as selecting the AC(i) measure rule. | ATTEMPTED. The landed measure binary note leaves count-once versus count-twice statistics open. |
| doublet-clock route | Treat the doublet clock as normalized R-eta readout. | ATTEMPTED. The clock leaves `|b| / a_act` or equivalent normalization open. |
| direct-license route | Treat Record additivity plus fixed-locus arithmetic as `Phi = S_sum = 2/3`. | ATTEMPTED. The landed direct-license note splits the gap into h-class and h-unit. |
| h-unit primitive route | Treat approved primitives as supplying `beta = 1`. | ATTEMPTED. The landed primitive-boundary note finds no approved h-unit primitive. |
| h-class first-principles route | Treat C3 covariance and additivity as selecting the fixed-locus-density class. | ATTEMPTED. The landed h-class note leaves the additive coefficient free. |
| C3 ratification route | Treat open `#4981` C3 context as the physical density-read-as-angle theorem. | ATTEMPTED AS OPEN CONTEXT. It is lane-relevant support only, not retained closure. |
| K2 exactness route | Treat the whole cluster as `K2_R_ETA_EXACTNESS_RETAINED`. | RULED OUT. Exactness still needs retained h-class/h-unit/readout/domain/owner/audit inputs. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| h-class <-> h-unit | no | independent subinputs of R-eta retirement |
| h-class <-> physical carrier context | no | independent |
| h-unit <-> identity-unit theorem | h-unit depends on it; the theorem does not follow from h-class | keep explicit |
| doublet-clock normalization <-> direct-license theorem | no | alternative route families |
| K1 occupancy dictionary <-> K2 R-eta readout | no | separate Koide inputs |
| K2 exactness <-> physical electron mass | no | K1/K3/K4 and mass-map remain separate |

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `landed on origin/main` | source-state context, not retained theorem promotion |
| `closed without GitHub merge flag` | review workflow metadata, not proof input |
| `fixed-locus` | retained arithmetic support only; physical readout is separate |
| `approved primitive` | registry-approved premise only within declared scope |
| `C3 context` / `ratification` | support/governance context, not physical angle license |
| `normalization` / `identity` | explicit h-unit wall, not hidden |

### N4 - Residual Matching

| source | residual it attacks | residual here | match? |
|---|---|---|---|
| occupancy formation note | occurrence-to-occupancy shortcut | K1/AC(i) shortcut boundary | yes as adjacent guard |
| occurrence axiom-hygiene note | Record-append-to-R-eta shortcut | K2 R-eta occurrence/event route | yes |
| measure binary axiom-update note | updated-axiom-to-AC(i)-binary shortcut | K1/AC(i) measure binary route | yes as adjacent guard |
| doublet-clock note | clock/rate normalization shortcut | K2 R-eta clock route | yes |
| direct-license note | direct h-class/h-unit shortcut | R-eta readout retirement | yes |
| h-unit primitive note | approved-primitive h-unit shortcut | h-unit current-surface non-supply | yes |
| h-class stretch note | first-principles h-class shortcut | h-class current-surface non-supply | yes |
| open `#4981` | C3 ratification non-supply | context-only K2 support | yes as open context |

### N5 - Rhetoric Audit

The negative phrase is narrow: "the cluster does not supply retained K2 or
hydrogen."

| resolution | tested? | outcome |
|---|---:|---|
| K1 occurrence/dictionary | yes | occurrence is not dictionary closure |
| K1 measure/binary | yes | updated axioms/primitives do not select the measure rule |
| K2 occurrence/event law | yes | generic record formation is not event/readout closure |
| K2 h-class | yes | class coefficient remains open |
| K2 h-unit | yes | identity-radian coefficient remains open |
| K2 exactness | yes | subinputs plus owner/audit remain open |
| electron mass | kept separate | K1/K3/K4/mass-map remain needed |
| hydrogen | kept separate | `alpha(0)` and static-source lanes remain needed |

### N6 - Partial-Closure Path Scan

Legitimate follow-ups remain:

| path | what it could close |
|---|---|
| retained h-class theorem or owner/audit handoff | `R_ETA_H_CLASS_RETAINED` |
| retained h-unit theorem or owner/audit handoff | `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED` |
| combined direct readout-license theorem | `R_ETA_READOUT_IDENTIFICATION_RETAINED` |
| coherence-event/rate normalization theorem | an alternate R-eta route |
| owner-approved narrow readout primitive | governance supply, not derivation |

### N7 - Steelman

A strong positive reading is that the AC/R-eta cluster materially advances K2:
it isolates the exact h-class/h-unit handoff and removes several distracting
shortcuts. That makes a later owner/audit decision or retained theorem easier
to target. The boundary is that sharper residuals are not spendable inputs;
they do not by themselves select the fixed-locus physical readout class or the
identity-radian coefficient.

### N8 - Cross-Cycle Echo

This echoes the earlier value-face and occurrence-route work: a value, context,
or correctly typed slot can become useful retained support without becoming
the selector/readout law. Hydrogen should track the cluster, but must not
spend it as K2 until the relevant retained theorem or owner/audit handoff
lands.

**Gate result:** broad K2/hydrogen closure claim fails; narrowed AC/R-eta
cluster impact discriminator passes.

## Explicit Non-Claims

- No derivation or ratification of `R_ETA_H_CLASS_RETAINED`.
- No derivation or ratification of `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`.
- No derivation or ratification of `R_ETA_READOUT_IDENTIFICATION_RETAINED`.
- No derivation or ratification of `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.
- No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.
- No derivation of K1 occupancy/counting, K3 physical species bridge, K4
  absolute scale, native Koide bridge, or Koide branch mass-map.
- No derivation or ratification of `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`.
- No derivation of `S_l`, A3, `C_A3`, `alpha(0)`, static-source Rydberg, or
  hydrogen.
- No spending of PR `#4981` as R-eta closure.
- No spending of `#4982`-`#4986` landed-main notes as retained K2 closure.
- No spending of landed-main `89768b461c` or `e2d1dec095` as K1/K2 closure.
- No new axiom, primitive, Tier-A admission, or empirical import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_ac_r_eta_upstream_cluster_impact_discriminator.py
```

The verifier checks the finite witness arithmetic, parent-packet wiring,
primitive boundaries, no-go discipline markers, and explicit non-claims.
