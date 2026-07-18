# Physical Cycle-269 four-cell star role gauge — Cycle 324

Date: 2026-07-18

Authority: none

Audit: unset

Constitutional effect: none. No axiom, foundation, Qualification, primitive,
registry, policy, queue, or audit status is edited or proposed.

Companion runner:

```text
scripts/physical_cycle269_four_cell_star_cycle324_2026_07_18.py
```

Methodology freshness: the no-go-discipline procedure, freshness instructions,
and all case studies were read directly from freshly fetched `origin/main` at
`8e1adb5bc486b3236f3988214ce49946e9bccd65`. The dirty worktree was not moved.

## Result up front

Cycle 324 closes the smallest four-cell degree-three-star discriminator through
total number `n=2`. Four actual Cycle-311 M64 cells occupy a straight path, a
right-angle corner path, or a three-arm star. All 24 cell-factor orders are
multiplied on the same physical M2 patch for every geometry. The declared
logical input is

```text
H_4,<=2 = direct sum from n=0 to 2 of wedge^n(C^24),
dimension = 1+24+276 = 301.
```

Every factor order gives an isometry with 301 columns, 89,296 occupied physical
rays, and 89,296 nonzero amplitudes. All 24 orders together carry 2,143,104
nonzero amplitudes. Processed Gram residuals vanish. The maximum raw order Gram
entry is `1.043609643148e-14`; the joint-order raw Gram entry is at most
`1.054711873394e-14`, and its minimum eigenvalue is at least
`0.9999999999999883`. The result is unchanged at training `L=5` and held
`L=6` on path, corner, and star.

The physical factor orders remain different. Both `ABCD-BACD` and
`ABCD-ACBD` have operator residual `1.414213562373`. Selecting one order is
extra structure, so the actual compiler retains the order relation locally.

## The local encoding and update

Write `E_pi` for the actual Cycle-311 four-cell isometry in factor order
`pi in S4`, and let `|pi>` be a lawful state of the local 24-state role
register. The bounded relational encoding is

```text
E_4 = (1/sqrt(24)) sum_(pi in S4) |pi> tensor E_pi.
```

The 24 role states fit in five M2; eight unused states in the 32-state
computational shell are removed by a local register-domain constraint. For a declared logical update
`G`, a bounded block realization is

```text
G_physical = sum_pi |pi><pi| tensor (E_pi G E_pi^dagger) + G_perp,
```

where `G_perp` is a supplied unitary completion outside the image. Since every
tested `E_pi^dagger E_pi` is the 301-dimensional identity, the code-space
equation is

```text
E_4 G = G_physical E_4.
```

The dense bounded block coefficients, the off-code completion, and their
primitive application are in the supplied inventory. Thus this is a local
finite compiler with explicit primitive debt, not a synthesis of that matrix
rule from a smaller gate alphabet.

## Three overlapping S3 checks

The priority comparator places three Cycle-319-style subgroup checks on the
overlapping triples `ABC`, `ABD`, and `CBD` inside the 24-state `S4` order
shell. Each subgroup average has rank factor four. Each pair and all three
share the uniform role vector:

```text
pairwise common rank factors = (1,1,1),
all-three common rank factor = 1,
all-three logical common rank = 301.
```

However, those three subgroup checks cannot be treated as a commuting,
order-independent stabilizer family on this shell:

```text
maximum constraint commutator       = 1.257078722109,
maximum projector commutator        = 0.314269680527,
projector braid residual             = 0.104756560176,
maximum six-sequence spread          = 0.181443684651,
matrix associator residual = 0.
```

The zero associator is ordinary associativity of matrix multiplication. The
nonzero sequence spread is order dependence of three different projectors;
it is not an associativity defect. A common code exists, so the measured
failure is only the proposal that the three S3 checks form a commuting,
order-independent constraint set. It is not evidence against a joint role
gauge, local M2, degree-three incidence, or a recurrent volume.

## Joint bounded S4 role gauge

The repair uses the whole four-cell order group in one local register. With

```text
|u_24> = (1/sqrt(24)) sum_(pi in S4) |pi>,
J_S4 = 2 |u_24><u_24| - I_24,
```

the `J_S4=+1` sector has rank 301. The joint constraint involution, its
commutators with all three adjacent exchanges, both adjacent braid residuals,
and the far-exchange commutator vanish after tolerance. The raw uniform
eigenvector residual is `9.440976529271e-16`.

One joint S4 register costs five M2, compared with nine M2 for three literal
three-M2 S3 registers. The result supplies a bounded common code and removes
the tested order dependence. It does not test the compatibility of two joint
S4 registers on adjacent degree-three stars.

No global Jordan-Wigner string, global parity service, global ordering,
preferred lattice axis, or host-side order query is used.

## Free-plus-contact update on three incident edges

For each geometry, let `S_1,S_2,S_3` be the three incident FSWAPs on literal
ports. The six
edge orders use

```text
U_sigma = D_4 S_(sigma(3)) S_(sigma(2)) S_(sigma(1))
          Gamma(C direct-sum C direct-sum C direct-sum C),
D_4 = exp(i g sum_j binom(n_j,2)),
g = 0.37.
```

There are 8,701 active coin coefficients. Each FSWAP has 301 signed entries,
and the Cycle-230 contact is nontrivial on 60 columns. The raw unitarity maxima
are `6.661438e-16` for the coin, zero after tolerance for each FSWAP,
`2.226535e-17` for contact, and at most `6.661449e-16` for a composed update.

The three FSWAPs use distinct addressed port modes. All three pairwise
commutators and all six ordered-update differences vanish on the declared
domain. This is a measured fact about these three path/corner/star edge lists,
not an all-collision policy.

| total number | dimension | composed-update unitarity after tolerance |
|---:|---:|---:|
| 0 | 1 | 0 |
| 1 | 24 | 0 |
| 2 | 276 | 0 |

All six edge orders commute with the lifted joint constraint and satisfy the
joint-code intertwining equation with processed and raw residual zero. The
uniform one-particle state retains mass `0.45340565417488515`, matching the
Cycle-219 fixture `0.4534056541748851`; its eigenvector residual is at most
`3.717330675495e-16`.

Contact phase is not called mass or physical energy, a generator element is
not called a rate, and the compiler schedule is not called time.

## Three-edge local slot comparator

The staggered comparator uses a three-state slot encoded in two M2, with one
of four computational states locally excluded. One active-edge flag plus
companion costs two more M2. With the three slots ordered cyclically,

```text
W_slot = |1><0| tensor S_1
       + |2><1| tensor S_2
       + |0><2| tensor S_3.
```

Its cube contains the three cyclic products of `S_1,S_2,S_3`. Slot unitarity,
the cube identity, three-slot macro unitarity, active-constraint involution,
active-constraint transport, and all-frame slot covariance have residual zero.
The slot is changed by the local matrix rule. `host queries = 0`.

This route is viable on the tested path, corner, and star. It does not provide
a recurrent-volume collision policy or initialization law.

## Proper-cubic covariance and translations

All 24 proper-cubic frames act on every geometry. Ordered edge-direction orbit
sizes are 6 for the straight path, 24 for the corner, and 24 for the star. For
each frame, the exterior representation is unitary and maps the base
coin-FSWAP-contact update to the rotated update. Processed covariance residuals
vanish and the maximum raw entry is `6.206335383118e-17`.

There are 576 frame group-law tests per geometry with zero failures. Each
geometry also passes 15,625 explicit `L=5` translation-address tests with zero
failures. The slot operator passes the same 24-frame action.

## Physical support and constraints

The face, port, cell-flag, and cell-companion patch union is 155 M2 on every
tested geometry and size. Adding the joint S4 register gives a 160-M2 patch.
The largest tested physical branch uses 34 M2 before the register on path and
corner, 36 on star, and therefore at most 41 after the register. The largest
single-cell input branch is 35 M2 on path, 36 on corner, and 34 on star. These
are observed upper counts, not minima.

Every branch has zero inherited `B_v Z_port(v)` commutator failures and zero
local-check/fixed-Wilson commutator failures at `L=5` and held `L=6`. The dense
`J_S4` and eight unused-state exclusions are additional supplied local
register rules. Their primitive synthesis remains open.

## Leakage, deletion, and lawful-domain controls

| deletion | residual |
|---|---:|
| one of 24 joint-order amplitudes | Gram `1/24 = 0.041666666667` |
| one composed-update column | unitarity `1` |
| active coin coefficient `-0.659236842151+0.049064365032 i` | unitarity `0.760508963277` |
| nontrivial contact | `0.367893067056` |
| slot cycle | unitarity `1` |
| eight S4 unused-state exclusions | rank surplus `8` |
| retain only one S3 subgroup check | common rank factor `4` rather than `1` |

Lawful-domain controls reject total number above two, a geometry outside
path/corner/star, and aliased path `L=4`. Removing a joint-order amplitude
breaks the relational isometry; removing the unused-state rule admits eight
off-domain role states.

## Supplied-structure inventory

Supplied are:

1. the Cycle-269 fixed-Wilson reference and face/port dictionary;
2. the Cycle-311 local M64 cell, cell flag, cell companion, and preparation;
3. four addressed cells and one declared path, corner, or star edge-direction
   list;
4. the total-four-cell cutoff `n<=2` and arbitrary amplitudes in 301 columns;
5. one 24-state S4 role register encoded in five M2 and eight local unused-state
   exclusions;
6. the dense `J_S4` coefficients and the off-code unitary completion;
7. the three overlapping S3 subgroup definitions used by the comparator;
8. the Cycle-219 coin, Cycle-230 contact, three port FSWAPs, coupling, and
   application order;
9. a three-state slot encoded in two M2, one unused-state exclusion, one
   active-edge flag-plus-companion pair, and the explicit slot cycle;
10. fixed-reference, role-register, and logical-amplitude preparation; and
11. primitive realization and application of the bounded matrix units.

Derived are all 24 actual physical order isometries on all three geometries,
the overlapping-S3 rank and order diagnostics, the rank-301 joint S4 gauge,
all six three-edge updates, joint-code preservation, slot-cycle identities,
all-frame covariance, translations, held-size stability, mass preservation,
and deletion residuals.

Still open are `n=3,...,24`, full `M64 tensor M64 tensor M64 tensor M64`,
overlap of joint S4 registers on adjacent stars, degree-four or higher
incidence, recurrent all-edge stream/contact, a volume collision schedule,
primitive synthesis, and arbitrary reference/role preparation.

## Prior-art and novelty boundary

Cycle 235 supplies the local even/Gauss operator grammar. Cycle 308 supplies
the higher-number carriers. Cycle 311 supplies one common M64 physical cell.
Cycle 315 supplies the successful one-edge Z2 relational role and full
two-cell update. Cycle 319 supplies the path/corner S3 and two-edge slot
repairs.

Cycle 324 claims only the actual four-cell path/corner/star product, the exact
failure mode of three overlapping S3 subgroup checks, and the bounded joint
S4 and slot-cycle repairs through total `n=2` on this repository substrate.
Regular representations, symmetric-group braid relations, group averaging,
auxiliary gauge codes, fermionic swaps, and matrix-unit completions are
prior-art territory. Global novelty priority is not asserted.

Thirring machinery is not used or compared.

## TOE dependency ledger

`C_local` advances from a shared-cell two-edge patch to the first tested
degree-three star. `C_int` advances to three incident Cycle-230 seams through
`n=2`. `C_num` does not advance beyond Cycle 315's full two-cell result or
Cycle 319's three-cell `n<=3` result. `C_ref` retains supplied reference and
role preparation. `C_wrap` and `C_source` are unchanged.

| wall | Cycle-324 movement | still open |
|---|---|---|
| `C_ref` | joint local S4 role replaces a selected four-cell order | reference genesis and conditional role preparation |
| `C_num` | exact four-cell sectors `n=0,...,2` | `n=3,...,24`, number change, volume full Fock |
| `C_wrap` | unchanged | event equivalence, interval, clock, and rate |
| `C_int` | three incident FSWAP seams plus four-cell contact | repeated arrivals, overlapping-star collision, recoil |
| `C_local` | 160-M2 path/corner/star, joint S4 gauge, frames, held size | adjacent joint registers, recurrent volume schedule, synthesis |
| `C_source` | unchanged | action/energy/stress/source response and gravity relation |

Planning maturity becomes: operational quantum / Records `3.4/5`
(`63/29/90`), causal time / clock `1.8/5` (`34/17/62`), inertia / matter
`4.2/5` (`75/36/96`), gravity / source / resource `2.1/5` (`40/16/67`), and
Born / probability / realized history `2.0/5` (`34/14/85`). Only matter and
local compiler evidence moves. No Record, source, clock, occurrence, or
probability result is added.

## No-Go Discipline Gate

The narrow result is that the three literal overlapping S3 subgroup checks do
not form a commuting, order-independent constraint family on the tested
24-state role shell. Their common rank-one factor survives, and the joint S4
and slot-cycle routes both succeed. Full-number, adjacent-register, and
recurrent-volume routes remain open.

Gate status: **FAIL / DO NOT SHIP the broad degree-three or volume negative.**

### N1 — alternative routes

| route | marker | actual attack and disposition |
|---|---|---|
| one selected physical factor order | **ATTEMPTED** | each selected order is isometric, but adjacent selections differ by `sqrt(2)` and selection remains supplied structure |
| three overlapping three-cell S3 checks | **ATTEMPTED** | common rank factor one survives, but commutator, braid, and sequence residuals rule out a commuting/order-independent reading |
| one joint 24-state S4 role gauge | **ATTEMPTED** | succeeds with five M2, rank factor one, exact adjacent exchanges, and held-size closure |
| one active edge role with a three-slot cycle | **ATTEMPTED** | succeeds on path, corner, and star with exact slot transport and frame covariance |
| straight path physical shell | **ATTEMPTED** | succeeds through `n=2`, all 24 frames, translations, and held `L=6` |
| right-angle corner physical shell | **ATTEMPTED** | succeeds through `n=2`, all 24 frames, translations, and held `L=6` |
| degree-three star physical shell | **ATTEMPTED** | succeeds through `n=2`, all 24 frames, translations, three incident seams, and held `L=6` |
| complete four-cell M64^4 widening | **OPEN / UNTESTED** | sectors `n=3,...,24` are not constructed here |
| overlapping joint S4 registers on adjacent stars | **OPEN / UNTESTED** | compatibility may close recurrent incidence without separate patch choices |
| alternative bounded role encoding | **OPEN / UNTESTED** | a smaller or more local constraint may preserve the same rank-one role code |

The two constructive role repairs and three open routes block a
route-independent negative.

### N2 — wall-independence audit

The collapsed open set is `W_full_number`, `W_overlap_stars`, `W_primitive`,
`W_prepare`, and `W_schedule_global`.

| left | right | closing left closes right? | closing right closes left? | independent? |
|---|---|---:|---:|---:|
| W_full_number | W_overlap_stars | no | no | yes |
| W_full_number | W_primitive | no | no | yes |
| W_full_number | W_prepare | no | no | yes |
| W_full_number | W_schedule_global | no | no | yes |
| W_overlap_stars | W_primitive | no | no | yes |
| W_overlap_stars | W_prepare | no | no | yes |
| W_overlap_stars | W_schedule_global | no | no | yes |
| W_primitive | W_prepare | no | no | yes |
| W_primitive | W_schedule_global | no | no | yes |
| W_prepare | W_schedule_global | no | no | yes |

The five walls respectively concern full four-cell number, compatibility of
several joint registers, primitive gate synthesis, reference/role
preparation, and an autonomous volume collision schedule.

### N3 — hidden-condition scan

The literal procedure-trigger scan runs over both Cycle-324 release paths and
must return zero. The fixed reference, addresses, geometries, edge-direction
lists, number cutoff, role register, unused states, dense coefficients,
off-code completion, coupling, slot rule, preparation, sizes, and tolerances
are listed above.

### N4 — residual matching

| cited witness | witness residual | Cycle-324 residual | match? |
|---|---|---|---:|
| Cycle-311 common M64 runner, exact file and line | one-cell physical M64 isometry | each of the four physical factors | yes |
| Cycle-315 edge-role runner, exact file and line | AB/BA order mismatch and one-edge repair | each adjacent exchange before the overlap test | yes |
| Cycle-319 multi-edge runner, exact file and line | independent checks versus joint S3 on one three-cell patch | each three-cell subgroup inside the S4 test | yes |
| exact Cycle-324 runner witnesses | path/corner/star Gram, role algebra, updates, covariance, deletions | current retained result | yes |

Exact predecessor locations are
`scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py:1018`,
`scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py:1272`,
`scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py:1280`,
`scripts/physical_cycle269_three_cell_multiedge_cycle319_2026_07_18.py:1135`,
and
`scripts/physical_cycle269_three_cell_multiedge_cycle319_2026_07_18.py:1151`.

| current witness | exact file and line |
|---|---|
| 24 actual physical factor orders | `scripts/physical_cycle269_four_cell_star_cycle324_2026_07_18.py:1108` |
| overlapping-S3 common rank and sequence failure | `scripts/physical_cycle269_four_cell_star_cycle324_2026_07_18.py:1121` |
| bounded joint S4 repair | `scripts/physical_cycle269_four_cell_star_cycle324_2026_07_18.py:1131` |
| three-FSWAP update | `scripts/physical_cycle269_four_cell_star_cycle324_2026_07_18.py:1142` |
| six update intertwiners and mass | `scripts/physical_cycle269_four_cell_star_cycle324_2026_07_18.py:1164` |
| frames, geometry orbits, and slot cycle | `scripts/physical_cycle269_four_cell_star_cycle324_2026_07_18.py:1181` |

No Cycle-319 three-cell result is cited against a joint S4 or three-slot
construction.

### N5 — rhetoric and resolution audit

| resolution | tested | disposition |
|---|---|---|
| one Cycle-311 cell | all 64 labels | predecessor M64 isometry retained |
| one Cycle-315 edge | full two-cell Fock | predecessor edge gauge retained |
| one Cycle-319 three-cell patch | all total `n<=3` labels | predecessor joint S3 and two-edge update retained |
| one Cycle-324 four-cell path/corner/star | all total `n<=2` labels | exact 24-order shell and three-edge update |
| three overlapping S3 subgroup checks | complete 24-state S4 role shell | exact common rank and noncommuting/order-dependent result |
| one joint four-cell S4 register | complete 24-state role shell | exact rank-factor-one repair |
| overlapping four-cell S4 registers | not tested | no compatibility or negative claim |
| recurrent full-number volume | not tested | no closure or negative claim |

The negative wording is restricted to the three named S3 subgroup checks on
the tested 24-state role shell.

### N6 — partial-closure paths

Cycle 311 supplies each physical cell. Cycle 315 supplies one relational edge
role. Cycle 319 supplies the joint S3 and staggered repairs for one
three-cell patch. Cycle 324 supplies a joint S4 and three-slot repair for the
first degree-three star. Adjacent-star S4 compatibility, a shared larger
register, slot serialization, full-number widening, and smaller bounded role
codes remain direct construction paths. No premise edit is requested.

The optimal next attack is two adjacent four-cell stars sharing cells, first
through total `n<=2`. Compare two S4 registers, one joint five-cell role
register, and a locally transported slot cycle under all 24 frames before
widening number.

### N7 — hostile steelman

A hostile reviewer should reject any degree-three or recurrent-volume no-go.
The failed object is only a commuting/order-independent interpretation of
three overlapping S3 subgroup checks. Their uniform common code survives,
the bounded joint S4 register closes the whole tested star, and the slot cycle
avoids simultaneous subgroup constraints. Two adjacent stars can share an S4
role register, use a larger S5 role, or transport one active slot across both
patches. Neither compatibility route has been tested. The evidence demands
the adjacent-star construction, not constitutional pressure.

### N8 — cross-cycle echo

| prior result | retirement mechanism | Cycle-324 lesson |
|---|---|---|
| Cycle 235 total-even boundary | bounded operator algebra | preserve useful local algebra after a state limitation |
| Cycle 308 odd-carrier boundary | oriented complement carrier | enlarge the local code before a parity negative |
| Cycle 311 cell-order collision | relational cell companion | turn raw order loss into gauge data |
| Cycle 315 endpoint order | local Z2 edge role | repair one adjacent exchange without a global order |
| Cycle 319 independent S3 checks | joint S3 role or staggered slot | match one patch's role group to its overlap graph |
| Cycle 324 overlapping S3 checks | joint S4 role or three-slot cycle | enlarge or serialize before extending a route failure |

Every echo supports the adjacent-star attack. No shared obstruction and no
axiom pressure follow.

## Verification

```text
python3 scripts/physical_cycle269_four_cell_star_cycle324_2026_07_18.py
```
