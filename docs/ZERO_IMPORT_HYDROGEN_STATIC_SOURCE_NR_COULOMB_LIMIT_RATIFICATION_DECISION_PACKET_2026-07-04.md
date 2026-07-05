# Zero-Import Hydrogen: Static-Source NR Coulomb Limit Ratification Decision Packet

**Date:** 2026-07-04
**Type:** decision packet / import-retirement handoff
**Status:** support-only. This packet does not ratify the static-source
nonrelativistic Coulomb limit, does not derive `m_e`, does not derive
`alpha(0)`, and does not claim hydrogen is retained.
**Verifier:** `scripts/frontier_zero_import_hydrogen_static_source_nr_coulomb_limit_ratification_decision_packet.py`

## Purpose

The static-source hydrogen target needs three retained physical ingredients:

```text
E_n = -m_e alpha(0)^2 / (2 n^2).
```

The electron-mass and alpha0 packets package two of those ingredients. This
packet packages the third one:

```text
the one-body nonrelativistic Schrodinger/Coulomb limit in physical units for a
static positive source.
```

This is the step that prevents the final hydrogen calculation from silently
importing textbook quantum mechanics. The existing repo already has useful
operator and kernel support: a scalar graph-Laplacian surface, a `Z^3`
Green-kernel asymptote, a static-source I1 linear-response bridge, and atomic
`1/n^2` harnesses. Those are real support. They are not, by themselves, a
retained physical-unit one-body atomic theorem.

## Decision Object

The decision object is exactly:

```text
the zero-import static-source nonrelativistic Coulomb limit package for the
static-source hydrogen lane.
```

It has six content clauses:

| clause | decision text |
|---|---|
| SNR.1 | operator surface: the scalar nearest-neighbor `Z^3` graph-Laplacian used by the atomic harness is ratified for this one-body low-energy surface |
| SNR.2 | Coulomb kernel: the framework-local Green asymptote `G(r) -> 1/(4 pi |r|)` and the arithmetic `V_lat = -4 pi g G(r) -> -g/|r|` are ratified for the static-source lane |
| SNR.3 | static-source readout: the linear-response readout `V(r) = -C g_bare^2 G(r) -> -C alpha/r` is ratified rather than left as an accepted-premise bridge |
| SNR.4 | one-body NR reduction: the low-energy single-particle Schrodinger/Coulomb Hamiltonian in physical units is retained, not imported from the standard-QM scaffold |
| SNR.5 | Hartree mapping: physical units enter only through retained `m_e` and retained `alpha(0)`, giving `E_H = m_e alpha(0)^2` and `Rydberg = E_H/2` |
| SNR.6 | comparator exclusion: observed Rydberg spectroscopy, observed `m_e`, observed `alpha(0)`, and textbook physical constants are not proof inputs on the zero-import branch |

The object deliberately excludes the electron-mass derivation, the alpha0
transport derivation, finite-proton reduced-mass effects, fine structure, Lamb
shift, hyperfine structure, and helium.

## Ratification Decision Contract

This packet is decision-ready only if all eleven contract inputs are visible:

```text
STATIC_SOURCE_NR_COULOMB_TEXT_LOCK
SCALAR_LATTICE_OPERATOR_SURFACE_RATIFIED
COULOMB_KERNEL_ASYMPTOTIC_RATIFIED
STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED
ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED
HARTREE_SCALE_MAPPING_RATIFIED
ATOMIC_OPERATOR_HARNESS_VERIFIED
NO_RYDBERG_COMPARATOR_PROOF_INPUT
NO_NEW_PRIMITIVE_OR_AXIOM
OWNER_RATIFICATION
AUDIT_ACCEPTANCE
```

The contract means:

1. **STATIC_SOURCE_NR_COULOMB_TEXT_LOCK:** the SNR.1-SNR.6 text above is the
   complete object being decided.
2. **SCALAR_LATTICE_OPERATOR_SURFACE_RATIFIED:** the scalar graph-Laplacian
   surface used by the atomic harness is accepted as the one-body kinetic
   surface for this lane.
3. **COULOMB_KERNEL_ASYMPTOTIC_RATIFIED:** the `Z^3` Green-kernel asymptotic and
   `V_lat = -4 pi g G(r) -> -g/|r|` arithmetic are accepted for this lane.
4. **STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED:** the I1 static-source
   linear-response readout is accepted at retained theorem boundary or
   equivalent owner/audit authority, not merely hidden as standard background.
5. **ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED:** the physical-unit one-body
   nonrelativistic Schrodinger/Coulomb reduction is retained from the framework
   low-energy surface.
6. **HARTREE_SCALE_MAPPING_RATIFIED:** the physical scale is fixed as
   `E_H = m_e alpha(0)^2` with the static-source Rydberg scale `E_H/2`, using
   retained `m_e` and retained `alpha(0)` only.
7. **ATOMIC_OPERATOR_HARNESS_VERIFIED:** the atomic harness checks the
   `1/n^2` spectral bookkeeping and rejects scale-only overclaims.
8. **NO_RYDBERG_COMPARATOR_PROOF_INPUT:** observed Rydberg, observed hydrogen
   lines, PDG `m_e`, observed `alpha(0)`, and fitted textbook constants are
   excluded as proof inputs.
9. **NO_NEW_PRIMITIVE_OR_AXIOM:** the packet does not add an axiom, approved
   primitive, or Tier-A admitted numerical input.
10. **OWNER_RATIFICATION:** the owner explicitly accepts the static-source NR
    Coulomb boundary or retained theorem boundary.
11. **AUDIT_ACCEPTANCE:** the normal review/audit path accepts the decision and
    its dependency consequences.

No proper subset of those eleven contract inputs is a retained static-source
NR Coulomb limit decision.

## Conditional Consequence

If all eleven contract inputs are accepted, the conditional consequence is:

```text
STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED
RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT
```

That consequence is structural atomic support only. It does not by itself give
retained hydrogen. The final static-source Rydberg predicate still requires:

```text
STATIC_SOURCE_RYDBERG_RETAINED
  requires RETAINED_ELECTRON_MASS_PHYSICAL_UNIT
  + RETAINED_ALPHA0_LOW_ENERGY_COULOMB
  + RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT
  + ATOMIC_OPERATOR_HARNESS_VERIFIED
  + NO_RYDBERG_COMPARATOR_PROOF_INPUT
  + AUDIT_ACCEPTANCE.
```

This packet supplies only the static-source NR Coulomb side of that predicate
if accepted.

The static-source NR Coulomb current-surface no-go
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
`STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED` or
`RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT`. Its current missing inputs include
`STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED`,
`ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED`,
`HARTREE_SCALE_MAPPING_RATIFIED`, `OWNER_RATIFICATION`, and
`AUDIT_ACCEPTANCE`; scalar lattice operator support, Green-kernel support, I1
hygiene, native complete-square support, and atomic `1/n^2` harness checks
remain support, not the retained physical-unit one-body theorem.

The static-source NR Coulomb assembly ladder review packet
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md`
groups the direct rows under this parent contract for review compression only:
scalar operator, Green-kernel asymptotic, static-source readout, one-body NR
physical-unit reduction, Hartree mapping, atomic harness, comparator
exclusion, no-new-primitive guard, owner, and audit. It does not supply
`STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED` or
`RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT`.

The static-source NR Coulomb three-gate target bundle
`ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_THREE_GATE_TARGET_BUNDLE_2026-07-05.md`
is the next review layer beneath this parent: it groups
`STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED`,
`ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED`, and
`HARTREE_SCALE_MAPPING_RATIFIED` as sibling content gates. It does not accept
any of those gates and does not change the parent owner/audit contract.

## Finite Target Algebra

The dimensionless one-body Coulomb problem has shape:

```text
epsilon_n = -1 / (2 n^2).
```

For any positive Hartree scale `S`, the physical-looking spectrum

```text
E_n = S * epsilon_n
```

has the same ratios:

```text
E_n / E_1 = 1 / n^2.
```

So the lattice/atomic shape does not select the eV scale. The static-source
physical scale is:

```text
S = E_H = m_e alpha(0)^2
Rydberg = E_H / 2.
```

Three Hartree choices show the degeneracy:

| Hartree scale `S` | `E_1 = -S/2` | `E_2/E_1` | `E_3/E_1` |
|---:|---:|---:|---:|
| `20.000000 eV` | `-10.000000 eV` | `1/4` | `1/9` |
| `27.211386 eV` | `-13.605693 eV` | `1/4` | `1/9` |
| `40.000000 eV` | `-20.000000 eV` | `1/4` | `1/9` |

The operator/kernel arithmetic needed for the static-source shape is:

```text
G(r) -> 1/(4 pi |r|)
V_lat(r) = -4 pi g G(r) -> -g/|r|

V(r) = -C g_bare^2 G(r)
     -> -C g_bare^2/(4 pi |r|)
     =  -C alpha/|r|,  alpha := g_bare^2/(4 pi).
```

For the unit positive static-source hydrogen target, the Coulomb coefficient
must be the electromagnetic unit-source coefficient, not a hidden color
Casimir or fitted Rydberg coefficient.

## Current Open PR Alignment

Open PRs were refreshed on 2026-07-05 UTC before this packet was written.

| PR | audit status | effect on this static-source NR Coulomb decision packet |
|---|---:|---|
| `#5013` theta native positive-class adjudication | `SUCCESS` | theta gauge-side work; no static-source NR Coulomb package |
| `#5012` chirality domain-wall free-field note | `SUCCESS` | adjacent chirality science; no atomic one-body NR limit |
| `#5011` eta twisted walk family runner | `SUCCESS` | runner stabilization; no static-source NR Coulomb package |
| `#5010` YT P1 I_s re-audit packet bridge repair | `SUCCESS` | diagnostic repair; no atomic one-body NR limit |
| `#5009` S3 spacetime tensor primitive runner | `SUCCESS` | bounded S3 tensor context; no static-source Coulomb limit |
| `#5008` quark mass-ratio CP probe repair | `SUCCESS` | quark context; no atomic static-source theorem |
| `#5007` Koide native zero-section route guard repair | `SUCCESS` | electron-readout route support, not atomic NR Coulomb closure |
| `#5006` static-source I1 hygiene companion | `SUCCESS` | closest input; improves I1 hygiene, but does not retain the full one-body NR Coulomb limit |
| `#4991` owner-governed Tier-A retirement | `SUCCESS` | status progress for old Tier-A atoms; no atomic NR Coulomb package |

Merge-state labels and branch ordering are moving review metadata, not proof
inputs here.

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `ATOMIC_LANE2_PHYSICAL_UNIT_LIMIT_BOUNDARY_NOTE_2026-04-29.md` | proof that `1/n^2` shape does not fix the eV scale | boundary only; no physical-unit closure |
| `HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md` | scalar graph-Laplacian and Coulomb-kernel dependency narrowing | repair/support only; no absolute-eV prediction |
| `LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md` | `G(r) -> 1/(4 pi |r|)` framework-local Green-kernel normalization | kernel support, not one-body NR physical-unit theorem |
| `STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md` | conditional `V(r) -> -C alpha/r` from accepted-premise P1 plus Green kernel and alpha convention | accepted-premise/bounded bridge; P1 itself is not derived here |
| `STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md` | substance-vs-grade hygiene for I1 arithmetic | meta companion; no status promotion |
| `ATOMIC_HYDROGEN_HELIUM_PROBE_NOTE.md` | standard-QM physical-unit harness with textbook inputs | scaffold only; no framework inputs |
| `frontier_atomic_hydrogen_lattice_companion.py` | coupling-relative lattice `1/n^2` checks | coupling-relative only; not physical eV scale |
| `ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md` | final static-source predicate | still needs electron mass, alpha0, NR Coulomb limit, harness, comparator exclusion, and audit |
| approved primitives | minimal axioms, scale reference, kinetic isotropy, realized-state evaluation | no static-source linear-response readout, one-body NR reduction, electron mass, alpha0, or Rydberg value |

The primitive registry was checked with the current origin-main methodology.
Registered primitives are approved premise nodes, but they do not supply the
static-source NR Coulomb limit package.

## What This Moves

| before this packet | after this packet |
|---|---|
| static-source NR Coulomb physical-unit limit was named as an open final-lane blocker | the blocker has an eleven-input owner/audit decision contract |
| lattice `1/n^2` shape could be overread as an eV spectrum | the packet separates shape, readout, one-body NR reduction, and Hartree scale |
| I1 hygiene could be confused with full atomic closure | the packet keeps I1 as a necessary but insufficient input |
| standard-QM scaffold could be silently imported | the packet requires explicit one-body NR physical-unit ratification |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the static-source NR
Coulomb limit cannot be derived" is not shipped. The narrowed claim is:

```text
the static-source NR Coulomb limit is packaged as a decision-ready
ratification contract.
```

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full static-source NR contract | Accept all eleven contract inputs. | SUPPORTED CONDITIONALLY. It is the only route in this packet that accepts the retained static-source NR Coulomb limit. |
| standard-QM scaffold route | Use the textbook Schrodinger Coulomb Hamiltonian from the atomic probe. | VALID COMPARATOR/HARNESS ONLY. It imports the physical-unit one-body limit and textbook constants. |
| lattice shape route | Use the lattice companion's `1/n^2` ratios as the eV spectrum. | ATTEMPTED BY PRIOR. The physical-unit boundary shows shape does not select the Hartree scale. |
| Green-kernel-only route | Use `G(r) -> 1/(4 pi r)` and `V_lat -> -g/r` as the whole atomic theorem. | PARTIAL ONLY. It supplies the far-field `1/r` kernel, not the one-body physical-unit Schrodinger reduction or readout ratification. |
| I1 accepted-premise route | Use the static-source I1 bridge as final atomic closure. | PARTIAL ONLY. I1 formalizes `V -> -C alpha/r` under P1, but P1 remains an accepted premise and the physical-unit NR limit remains separate. |
| retained `m_e` plus retained `alpha(0)` shortcut | Supply the two physical numbers and call hydrogen retained. | INCOMPLETE. The final predicate also requires the retained static-source NR Coulomb limit, harness, comparator exclusion, and audit. |
| open-PR shortcut | Treat the current clean PR surface, especially `#5006`, as closure. | ATTEMPTED. `#5006` is relevant hygiene context, but it does not retain the full one-body static-source NR Coulomb limit. |
| full spectroscopy route | Add proton mass, reduced mass, fine structure, Lamb shift, and hyperfine corrections. | STRONGER FUTURE TARGET. It is beyond this static-source Rydberg lane. |

### N2 - Wall-Independence Audit

| pair | closes automatically? | conclusion |
|---|---|---|
| scalar operator surface <-> Green-kernel asymptotic | no in either direction | independent support gates |
| Green-kernel asymptotic <-> static-source readout | no in either direction | independent |
| static-source readout <-> one-body NR physical-unit reduction | no in either direction | independent |
| one-body NR reduction <-> Hartree scale mapping | no in either direction | independent |
| Hartree scale mapping <-> `m_e` / `alpha(0)` derivations | no; those are downstream inputs from other packets | separate lanes |
| atomic harness <-> theorem ratification | no in either direction | independent |
| comparator exclusion <-> input retention | no in either direction | independent |
| OWNER_RATIFICATION <-> AUDIT_ACCEPTANCE | no in either direction | independent |

The collapsed decision wall is the eleven-input contract above. The scalar
operator and Green-kernel gates are kept separate because ratifying the stencil
does not prove its asymptotic coefficient, and ratifying the asymptotic
coefficient does not by itself license that operator as the low-energy
one-body kinetic surface.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `standard-QM` / `Schrodinger` | explicit one-body NR limit input, not background |
| `framework-local` | source-scoped Green-kernel statement, not full atomic theorem |
| `accepted-premise` / `P1` | explicit static-source readout input requiring ratification |
| `physical-unit` / `Hartree` | explicit scale mapping requiring retained `m_e` and `alpha(0)` |
| `registered` / `primitive` | registry checked; approved primitives do not supply the static-source NR Coulomb limit |
| `observed` / `textbook` / `comparator` | excluded as proof input on the zero-import branch |

No one-body Hamiltonian, readout convention, Hartree scale, or comparator value
is left as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| physical-unit boundary note | shape does not determine the eV scale | Hartree scale mapping and no shape-to-eV shortcut | yes |
| lattice kinetic dependency repair | scalar graph-Laplacian and Coulomb-kernel dependency narrowing | SNR.1-SNR.2 operator/kernel support | yes |
| lattice Green-kernel note | `Z^3` graph-Laplian `1/(4 pi r)` asymptotic | SNR.2 kernel support | yes |
| static-source I1 bridge | `V -> -C alpha/r` under accepted P1 | SNR.3 readout ratification target | yes, but partial |
| I1 hygiene companion / `#5006` | substance-vs-grade hygiene around I1 | current open-PR context | yes for hygiene, not closure |
| standard-QM atomic probe | physical-unit scaffold with textbook inputs | SNR.4 import boundary | yes |
| static-source Rydberg discriminator | final predicate needs the NR Coulomb limit | conditional consequence | yes |
| primitive registry | approved primitive boundary | no primitive shortcut | guard only |

Non-matching citations are not used as closure evidence.

### N5 - Rhetoric Audit

The note avoids the broad phrase "hydrogen is impossible" and uses the narrow
target "static-source NR Coulomb limit package."

| resolution | tested? | outcome |
|---|---|---|
| lattice `1/n^2` shape | yes | support only; no eV scale |
| static-source one-body Rydberg | packaged conditionally | closes only after all contract inputs plus `m_e`, `alpha(0)`, and final audit |
| finite-proton nonrelativistic hydrogen | not claimed | needs proton mass and reduced-mass bridge |
| fine structure / Lamb shift / hyperfine | not claimed | needs separate QED and spin inputs |
| helium or many-body atoms | not claimed | outside this packet |

### N6 - Partial-Closure Path Scan

There are legitimate partial-closure paths:

| path | what it could close |
|---|---|
| retained scalar lattice-operator theorem for the atomic sector | SNR.1 |
| retained Green-kernel asymptotic/audit acceptance | SNR.2 |
| owner/audit ratification of static-source I1 or a derivation replacing P1 | SNR.3 |
| retained low-energy one-body NR reduction from the framework surface | SNR.4 |
| retained electron mass and alpha0 packets feeding the Hartree mapping | SNR.5 |
| atomic harness verification plus no-comparator proof-input audit | SNR.6 and final predicate hygiene |

These are import-retirement paths, not automatic new axioms.

### N7 - Steelman

A hostile reviewer can argue that this packet is overly procedural: the repo
already has the lattice graph Laplacian, the `1/r` Green kernel, and a standard
atomic scaffold, so the one-body Schrodinger/Coulomb limit is just ordinary
low-energy physics and should not require a separate ratification packet. The
strongest version points to the exact arithmetic `V -> -C alpha/r` and says the
remaining step is only notation. The narrow reply is that zero-import retained
hydrogen cannot spend "ordinary low-energy physics" as an untracked import.
The current I1 readout is explicitly an accepted-premise bridge, and the
standard-QM scaffold explicitly says no framework input is used. This packet
keeps those as visible ratification targets rather than pretending they are
already retained.

### N8 - Cross-Cycle Echo

This mirrors the earlier atomic physical-unit boundary and alpha0 packets:
shape support and coefficient support are real, but they do not become the
missing physical input until the import-bearing step is retired. The same
mechanism applies here: keep lattice `1/r` and `1/n^2` support, then require
explicit owner/audit ratification for the one-body physical-unit limit.

**Gate result:** broad no-go fails; narrowed static-source NR Coulomb decision
packet passes.

## Explicit Non-Claims

- No derivation or ratification of the static-source NR Coulomb limit.
- No derivation or ratification of the scalar lattice-operator atomic surface.
- No derivation or ratification of the static-source linear-response readout
  P1.
- No derivation of the physical-unit one-body Schrodinger reduction.
- No derivation of `m_e`.
- No derivation of `alpha(0)`.
- No retained hydrogen calculation.
- No full precision hydrogen spectroscopy.
- No use of observed Rydberg, observed hydrogen lines, PDG `m_e`, observed
  `alpha(0)`, or textbook constants as proof inputs on the zero-import branch.
- No new axiom, primitive, Tier-A admission, or empirical import.
- No audit status change for any cited row.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_static_source_nr_coulomb_limit_ratification_decision_packet.py
```

The verifier checks the contract predicate, finite Coulomb/Hartree arithmetic,
authority boundaries, primitive registry, current open-PR alignment,
No-Go Discipline sections, and explicit non-claims.
