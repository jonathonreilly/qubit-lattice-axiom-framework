# Physical state/contact bridge synthesis — Cycle 301

**Date:** 2026-07-17

**Type:** constructive physical state-and-interaction synthesis with N1--N8

**Status:** exact localized state and contact intertwiners relative to one
supplied fixed-Wilson vacuum; coherent coin/full-Fock compiler open

**Authority:** none

**Audit:** unset

**Constitutional effect:** none. No axiom, foundation, Qualification,
primitive, registry, policy, queue, or audit status is edited or proposed.

Companion runner:

```text
scripts/physical_state_contact_bridge_synthesis_cycle301_2026_07_17.py
```

## Answer in plain English

The physical compiler lane now has its first exact state-level and contact
equations on the same constrained M2 code, with a deliberately narrow domain.

In the fixed `+++` Wilson sector, the local checks, positive Wilsons, all
vacuum occupations `B_v=+1`, and zero auxiliary tags specify one unique
stabilizer reference ray.  Relative to that supplied global ray, every
localized adjacent identical-fermion pair has two bounded physical columns:
the pair before streaming and the pair after the two outer FSWAPs plus
collision-safe tag catch-up.  Their Gram matrix is exactly `I_2`, and the
restricted physical word obeys

```text
E G_coarse = G_physical E,
G_coarse = X.
```

The maximum physical Pauli/tag support relative to the supplied reference is
19 M2, independent of volume.  This is an exact two-column state isometry,
not a decoded permutation table.

On the same physical code, the Cycle-230 contact is

```text
C_x(g) = product_(u<v) exp(i g n_u n_v),
n_v=(I-B_v)/2,
g=0.37.
```

The fifteen pair projectors commute and exactly reproduce
`exp(i g binom(N_x,2))` on all 64 local occupation states.  On the two encoded
columns the input pair receives `exp(ig)` and the separated output pair
receives one, so

```text
E C_coarse = C_physical E,
C_coarse = diag(exp(ig),1).
```

The contact uses an 18-face union inside the inherited allocation of 21 M2
per cell.  It preserves local checks, Wilsons, port constraints, all 24
proper-cubic frames, translations, and the imported one-particle mass
fixture.

The boundary matters.  The reference vacuum is supplied and globally fixed;
it is not prepared by a bounded circuit.  `G_physical` means the restricted
action of the supplied two-edge FSWAP/catch-up word on the two columns, not an
assembled full-Hilbert macrostep.  Source/carrier reversal is the same
identical-fermion ray up to one common minus sign, not two species.  The mass
test is a **coarse-only one-particle mass firewall**, because the fixed-even
Cycle-269 code does not contain an odd lone-particle ket.

No coin is executed, no coherent position superposition is encoded, and no
full-Fock update exists.  Contact/stream ordering is supplied law structure,
not physical time.  The coupling and wrapped phase are not energy or a rate;
the stabilizer reference and port tags are not Records; nothing here is
gravity or probability.

## Exact route disposition

| route | strongest earned result | exact controls | open boundary |
|---|---|---|---|
| reference-relative localized lift | exact `2 x 2` Gram identity and restricted stream/catch-up intertwiner on every adjacent pair patch | route `7/0`; full reference ranks through held `L=6` (`4536/4536`); `5,184` held lifts; support at most 19 M2; frame/translation common-column phase; inverse, deletion, constraint leakage zero | fixed `+++` reference supplied; no absolute preparation, coherent position/Wilson superposition, distinguishable species, coin, or full-Fock `E` |
| physical Cycle-230 contact | exact 15-factor contact and exact encoded diagonal contact block | route `9/0`; all 64 occupations; pair support 9/10, union 18; inverse, `g=0`, occupied-pair deletion; `5,184` held intertwiners; all frames/translations; leakage zero | contact-only restricted block; no assembled contact-plus-stream/coin update, independent species, resource selection, or interaction rate |

## Supplied structure inventory

Load-bearing imports are:

1. the Cycle-269 fixed-Wilson face code, `A/B` dictionary, FSWAP polynomials,
   incident-order repair, and three positive Wilson characters;
2. all `B_v=+1` vacuum occupations and the supplied unique global
   `|Omega_+++>` stabilizer ray;
3. six auxiliary port M2 per cell, zero reference tags, and local
   `B_v Z_port(v)=+1` constraints;
4. one ordered adjacent pair patch and the two-edge stream-then-catch-up word;
5. Cycle-230 contact form, `g=0.37`, and contact-only schedule position;
6. training `L=3,4,5`, held `L=6`, frame, translation, deletion, inverse, and
   lawful-domain acceptance conditions;
7. imported Cycle-219/Cycle-230 coarse one-particle mass fixtures and
   tolerances.

Not derived are absolute vacuum preparation, a common encoder across Wilson
sectors or positions, distinguishable matter species, the six-mode coin/port
routing, coherent free-plus-contact evolution, the rank-73 sea, coupling
selection, energy/stress, clock, source normalization, metric/tensor response,
occurrence, Record formation, or Born weights.

## Updated six-wall dependency ledger

| wall | Cycle-301 movement | still open |
|---|---|---|
| `C_ref` | the exact reference dependence is exposed: one unique `+++` ray is sufficient for bounded relative columns | absolute preparation, cross-Wilson reference equivalence, physical phase/reference genesis |
| `C_num` | the fixed-even pair sector and port constraints are exact; source/carrier labels are shown not to create species | odd one-particle physical sector, distinguishable source role, common prepared full-Fock state |
| `C_wrap` | unchanged; contact/stream order is law structure and substeps are not time | event equivalence, recurrent clock, interval/rate calibration |
| `C_int` | materially advanced: the supplied Cycle-230 contact is exactly compiled on the same physical two-column state code and preserves the coarse mass firewall | coin-closed multiparticle domain, resource/recoil ledger, coupling selection, rate/protection, dressed mass |
| `C_local` | materially advanced: bounded reference-relative `E`, exact restricted `G_physical`, collision-safe tags, contact, constraints, frames, held size, and deletion all coexist | absolute/coherent-position state map, joint coin/port routing, assembled full-Hilbert/free-plus-contact and full-Fock compiler |
| `C_source` | unchanged; the labels in this identical-pair slice do not create a source law | physical moving source/response observable, reciprocal two-source law on this code, gravity/clock/tensor bridge |

## TOE lane update

These are evidence-weighted planning estimates, not audit verdicts or
probabilities.

| TOE lane | integrated | strict floor | conditional | maturity | disposition |
|---|---:|---:|---:|---:|---|
| operational quantum / Records | 55% | 24% | 78% | 2.8/5 | raised: an exact physical two-column state isometry and two restricted operator intertwiners now exist; occurrence, Record, coherent position, and full-Fock compilation remain open |
| causal time / clock | 33% | 17% | 60% | 1.7/5 | unchanged; gate ordering and compiler slices are not time |
| inertia / matter | 64% | 28% | 84% | 3.3/5 | raised narrowly: physical identical-pair contact preserves the imported one-particle mass firewall, but no physical odd one-particle lift or dressed dispersion exists |
| gravity / source / resource | 38% | 15% | 63% | 1.9/5 | unchanged; identical-pair role labels and contact phase do not select a source or gravity law |
| Born / probability / realized history | 33% | 14% | 79% | 1.7/5 | unchanged; no state norm is promoted to occurrence or probability |

## No-Go Discipline

The scoped candidate negative is: “no exact physical state or contact
intertwiner can be written on the Cycle-269 code.”  The two constructions
defeat that statement on their declared localized fixed-reference domain.

The broader negative—“no coherent/full-Fock compiler exists”—fails N1 because
coin routing, coherent position, alternative sector/preparation, and larger
state-map routes remain open.

**Gate status: FAIL for the candidate broad negative; do not ship it.**

### N1 — alternative routes

| route | marker | disposition |
|---|---|---|
| six-port collision-safe catch-up | **ATTEMPTED** | bounded physical gate and decoded collision action close |
| fixed-reference localized two-column state lift | **ATTEMPTED** | exact state isometry and restricted stream/catch-up intertwiner close |
| same-code localized Cycle-230 contact | **ATTEMPTED** | exact contact intertwiner closes |
| joint Cycle-219 coin/port word | **OPEN / UNTESTED** | required for coherent direction mixing |
| coherent position/direction state lift | **OPEN / UNTESTED** | required for one linear mobile encoded subspace |
| bounded absolute preparation of the `+++` reference | **OPEN / UNTESTED** | could retire the supplied-reference condition |
| sector-indexed or open-boundary compiler | **OPEN / UNTESTED** | may avoid one global fixed-Wilson preparation |
| larger full-Fock/contact domain | **OPEN / UNTESTED** | required for the six-mode CAR update and seam block |
| distinguishable source register/species | **OPEN / UNTESTED** | required before source/carrier roles become independent |

The broad obstruction fails N1.

### N2 — wall-independence audit

The remaining conditions are `W_reference` (absolute/cross-sector
preparation), `W_coin` (joint six-mode coin/port routing), `W_coherent`
(one coherent position state map), and `W_species` (independent source role).

| first condition | second condition | closing first closes second? | closing second closes first? | independent? | reason |
|---|---|---:|---:|---:|---|
| `W_reference` | `W_coin` | no | no | yes | preparing one ray supplies no coin word; a coin word supplies no absolute preparation |
| `W_reference` | `W_coherent` | no | no | yes | one reference ray does not construct an address superposition; a relative encoder need not prepare the ray |
| `W_reference` | `W_species` | no | no | yes | Wilson preparation does not add a matter species |
| `W_coin` | `W_coherent` | no | no | yes | a local coin can preserve a code without constructing one common position map |
| `W_coin` | `W_species` | no | no | yes | direction mixing does not create an independent source register |
| `W_coherent` | `W_species` | no | no | yes | coherent identical pairs remain one species |

The four conditions are independent constructive tasks, not witnesses for one
shared obstruction.

### N3 — hidden-condition scan

The fixed Wilson character, global reference ray, ordered adjacent patch,
identical species, six-port constraints, two-edge word, contact coupling and
schedule, finite sizes, and all acceptance tolerances are explicit.  No
continuum, energy, clock, gravity, probability, hidden metric, or host renewal
premise is used.

The literal rhetoric-trigger scan returned zero hits across all six package
paths.  It is a prose control, not a physics premise.

### N4 — residual matching

| witness and file line | residual class | exact scope | cross-route match? |
|---|---|---|---:|
| reference rank/Wilson deletion, `scripts/physical_cycle269_reference_relative_localized_pair_lift_2026_07_17.py:313` | binary stabilizer rank/character | unique supplied `+++` reference through `L=6` | no contact residual |
| exact Gram/intertwiner/inverse, `scripts/physical_cycle269_reference_relative_localized_pair_lift_2026_07_17.py:467` | stabilizer-column algebra | two columns for every adjacent patch | state route only |
| 64-state contact reconstruction, `scripts/physical_cycle269_local_contact_intertwiner_2026_07_17.py:237` | local diagonal phase | all local six-mode occupations | local contact algebra only |
| encoded contact phases/mixing, `scripts/physical_cycle269_local_contact_intertwiner_2026_07_17.py:467` | restricted two-column matrix | same localized state code | yes, matched through shared `E` |
| imported one-particle masses, `scripts/physical_cycle269_local_contact_intertwiner_2026_07_17.py:680` | coarse numerical fixture | separate odd one-particle model | no physical-state match; firewall only |

Only the shared two-column contact residual is joined.  Stabilizer rank and
coarse mass numbers are not pooled as a full-compiler witness.

### N5 — rhetoric and resolution audit

| resolution | tested | unresolved |
|---|---|---|
| reference | one fixed `+++` stabilizer ray | preparation and arbitrary Wilson superposition |
| state | one two-column adjacent-pair orbit at a time | one common coherent position/direction encoder |
| update | restricted two-edge stream/catch-up and contact separately | assembled coin/stream/contact full-Hilbert macrostep |
| matter | one identical even pair | odd one-particle physical state, distinguishable species, full Fock |
| symmetry | full family of patch descriptors/columns under frames/translations | coherent global code action |
| semantics | exact phases, supports, constraints, dimensionless coupling | energy, rate, time, source, gravity, Record, occurrence |

“Physical state lift” means exact stabilizer columns relative to a supplied
ray, not absolute preparation.  “Physical contact” means the displayed local
projector product and restricted encoded action, not an interaction rate or
full-Fock theorem.

### N6 — partial-closure paths

1. construct the joint Cycle-219 six-mode coin/port word;
2. assemble the localized stream/contact pieces on one coherent proper-cubic
   direction orbit;
3. extend one linear `E` across positions while keeping the fixed reference
   explicit;
4. test sector-indexed, open-boundary, or supplied-resource preparation routes;
5. only then extend contact to larger full-Fock sectors and moving response.

All are non-axiom constructive continuations.

### N7 — steelman

A hostile reviewer should combine the dimension-neutral six-port constraints
with the unique fixed-sector stabilizer tableau, define the six-mode coin by
conjugation on the common direction-orbit span, and assemble the already exact
stream/catch-up and contact blocks.  The two current intertwiners are positive
counter-authority that this can work.  Alternatively, an open-boundary or
sector-indexed target may avoid absolute Wilson preparation.  These routes are
strong enough that no coherent/full-Fock obstruction can be claimed.

### N8 — cross-cycle echo

| earlier seam | search/retirement mechanism | status |
|---|---|---|
| Cycle 269 local code had sector-dependent global stream | fix one explicit Wilson character and keep preparation separate | unique reference-relative ray becomes available |
| Cycle 297 catch-up had one decoded carrier plus spectator | add six collision-safe ports and local constraints | collision-safe bounded gate/decoded word closes |
| Cycle 299 still lacked a state `E` | act with bounded physical `A`/tag representatives on the supplied unique ray | exact localized state isometry/intertwiner closes |
| Cycle 230 contact remained on coarse M64 cells | substitute `n_v=(I-B_v)/2` and retain all 15 pairs | exact local physical contact and encoded diagonal close |

The recurring mechanism is to make the reference/auxiliary structure explicit
and test a bounded physical operator on exact states.  The same mechanism
should be tried on coin routing and coherent position before escalation.

**Disposition:** **no shared obstruction was identified** and **no axiom
pressure was established**.  The current result is genuine physical compiler
progress on a restricted fixed-reference slice, not a completed CAR compiler.

## Optimal next campaign

Construct the actual Cycle-219 six-mode coin jointly with the auxiliary port
constraints.  In parallel, build one coherent position/direction state map
from the reference-relative columns.  The decisive next equation is one common
`E G_coarse = G_physical E` for coin plus stream plus contact on a proper-cubic
superposition, still in the fixed-Wilson sector.  Absolute preparation and
cross-sector equivalence remain separate campaigns.

## Verification

```text
python3 -m py_compile \
  scripts/physical_cycle269_reference_relative_localized_pair_lift_2026_07_17.py \
  scripts/physical_cycle269_local_contact_intertwiner_2026_07_17.py \
  scripts/physical_state_contact_bridge_synthesis_cycle301_2026_07_17.py

PYTHONPATH=scripts python3 \
  scripts/physical_state_contact_bridge_synthesis_cycle301_2026_07_17.py
```
