# Physical Cycle-269 five-cell adjacent-star role gauge — Cycle 327

Date: 2026-07-18

Authority: none

Audit: unset

Constitutional effect: none. No axiom, foundation, Qualification, primitive,
registry, policy, queue, or audit status is edited or proposed.

Companion runner:

```text
scripts/physical_cycle269_five_cell_adjacent_star_cycle327_2026_07_18.py
```

Methodology freshness: the no-go-discipline procedure, freshness instructions,
and all case studies were read directly from freshly fetched `origin/main` at
`689ae2c8018fb23ac0d9b92ea2d3324c9249938b`. The dirty worktree was not moved.

## Geometry and result up front

Cycle 327 closes the smallest five-cell overlap of two Cycle-324 star charts
through total number `n=2`. The cubic patch is a center B with four arms
A(-x), C(+x), D(+y), and E(+z). The two degree-three star charts are

```text
left  star = ABCD,
right star = ABCE,
shared cells = ABC,
union = ABCDE.
```

Thus “adjacent-star” here means adjacent overlapping four-cell charts at one
center. Two distinct adjacent cubic centers of degree three require at least
six cells; that geometry is not tested here.

All 120 cell-factor orders are multiplied on the same physical M2 patch. The
declared logical input is

```text
H_5,<=2 = direct sum from n=0 to 2 of wedge^n(C^30),
dimension = 1+30+435 = 466.
```

Every factor order gives an isometry with 466 columns, 295,232 occupied
physical rays, and 295,232 nonzero amplitudes. All 120 orders carry
35,427,840 nonzero amplitudes. Processed Gram residuals vanish. The maximum
raw order Gram entry is `1.587618925214e-14`; the joint-order raw Gram entry is
`1.443289932013e-14`, and its minimum eigenvalue is at least
`0.9999999999999849`. Training `L=5` and held `L=6` agree.

The runner computes one actual five-word Pauli product per branch and obtains
all other factor orders from the exact pairwise Pauli swap signs. Four full
120-order direct-multiplication branch checks have zero support or phase
failures. `ABCDE-BACDE` has residual `1.414213562373`; `ABCDE-ABCED` has
residual zero because that tested D/E exchange commutes. Some orders agreeing
does not remove the measured A/B order role.

## Local encoding and physical update

Write `E_pi` for the actual five-cell isometry in factor order `pi in S5`.
With one lawful local order state `|pi>`, the relational encoding is

```text
E_5 = (1/sqrt(120)) sum_(pi in S5) |pi> tensor E_pi.
```

For a declared logical update `G`, a bounded block realization is

```text
G_physical = sum_pi |pi><pi| tensor (E_pi G E_pi^dagger) + G_perp,
E_5 G = G_physical E_5,
```

on the code space. `G_perp` is a supplied unitary completion outside the
image. The dense bounded coefficients, completion, and primitive application
are explicit imports. The result is a finite local compiler with primitive
synthesis debt, not a derivation of the matrix rule from a smaller gate set.

## Two overlapping S4 projectors

Inside the 120-state S5 order shell, the left projector averages the 24
permutations of `ABCD` and the right projector averages the 24 permutations of
`ABCE`. Each plus sector has rank factor five. Their intersection is the
uniform S5 vector:

```text
each S4 plus rank factor = 5,
common rank factor = 1,
logical common rank = 466.
```

The two checks do not form a commuting, order-independent constraint pair:

```text
constraint commutator             = 0.968245836552,
projector commutator              = 0.242061459138,
P_left P_right P_left
  versus P_right P_left P_right   = 0.0605153647845.
```

Ordinary matrix associativity remains intact. The projector/S5 matrix
associator is zero. In explicit five-dimensional S4 plus bases, the
register-change associator is `1.110223024625e-16`, and the uniform common
vector transports with residual `1.755416734289e-16`. Direct S4-to-S4 change
versus projection through only the one-dimensional joint S5 code differs by
`0.250000000000` off the common vector.

This is a narrow failure of treating the two subgroup checks as simultaneous
commuting and path-independent on their full five-dimensional plus sectors.
Their common rank-one code survives. It is not evidence against a joint S5,
local M2, another bounded role code, distinct-center incidence, or a volume.

## Joint bounded S5 role gauge

The repair uses the full five-cell order group. The 120 lawful states fit in
seven M2, and eight unused states of the 128-state computational shell are
removed by a local domain rule. Let

```text
|u_120> = (1/sqrt(120)) sum_(pi in S5) |pi>,
J_S5 = 2 |u_120><u_120| - I_120.
```

The `J_S5=+1` sector has rank 466. Constraint involution, commutators with the
four adjacent exchanges, all three adjacent braid residuals, and all three far
commutators vanish after tolerance. The raw uniform eigenvector residual is
`3.358883388006e-15`.

The joint role costs seven M2 versus ten M2 for two literal five-M2 S4 role
registers. It closes this five-cell overlap only. Compatibility between
several joint S5 registers is open.

No global Jordan-Wigner string, global parity service, global ordering,
preferred axis, or host-side order query is used.

## Four-seam free-plus-contact update

The four addressed edges are `AB`, `BD`, `BC`, and `BE`. Their center ports
are `-x,+y,+x,+z`, so the four literal FSWAPs use distinct modes. For every
`sigma in S4`, the tested update is

```text
U_sigma = D_5 S_(sigma(4)) S_(sigma(3)) S_(sigma(2)) S_(sigma(1))
          Gamma(C direct-sum C direct-sum C direct-sum C direct-sum C),
D_5 = exp(i g sum_j binom(n_j,2)),
g = 0.37.
```

The coin has 14,116 active coefficients. Each FSWAP has 466 signed entries,
and the Cycle-230 contact is nontrivial on 75 columns. Raw unitarity maxima are
`6.661438741028e-16` for the coin, zero after tolerance for each FSWAP,
`2.226534750407e-17` for contact, and `6.661448395737e-16` for a composed
update. All six stream commutators and all 24 ordered-update differences are
zero on this declared patch.

| total number | dimension | composed-update unitarity after tolerance |
|---:|---:|
| 0 | 1 | 0 |
| 1 | 30 | 0 |
| 2 | 435 | 0 |

The lifted update is `I_120 tensor U_sigma`, while the role constraint is
`J_S5 tensor I_466`; their commutator and code intertwiner vanish by the tested
Kronecker factors for all 24 orders. The code Gram residual is
`2.220446049250e-16`. The uniform one-particle state retains mass
`0.4534056541748853`, matching the Cycle-219 fixture within
`2e-16`; its eigenvector residual is `1.520235486122e-16`.

Contact phase is not called mass or physical energy, a generator element is
not called a rate, and the compiler schedule is not called time.

## Transported four-slot comparator

The staggered route uses four slot states in two M2 and one active-edge
flag-plus-companion pair in two M2. No slot state is unused. The local rule is

```text
W_slot = |1><0| tensor S_AB
       + |2><1| tensor S_BD
       + |3><2| tensor S_BC
       + |0><3| tensor S_BE.
```

The fourth power carries the four cyclic products of the incident FSWAPs.
Slot unitarity, the fourth-power identity, four-slot macro unitarity,
active-constraint involution, active-constraint transport, and all-frame slot
covariance have residual zero. The slot advances under the local matrix rule;
`host queries = 0`.

This is a compiler schedule on the tested patch. It supplies neither physical
time nor a recurrent-volume collision policy.

## Covariance, translations, support, and held size

All 24 proper-cubic frames act on the five-cell cross. The ordered four-arm
orbit has size 24. Each exterior representation is unitary and maps the base
coin-FSWAP-contact update to the rotated update. Processed covariance
residuals vanish; the maximum raw entry is `6.206335383118e-17`.

There are 576 frame group-law tests with zero failures and 15,625 explicit
`L=5` translation-address tests with zero failures. The slot rule passes the
same frame action.

The face, port, cell-flag, and cell-companion patch union is 192 M2. Adding the
joint S5 register gives 199 M2. The largest tested physical branch uses 37 M2
before the role and 44 after it; the largest single-cell input branch uses 34.
These are observed upper counts, not minimum claims.

Every branch has zero inherited `B_v Z_port(v)` commutator failures and zero
local-check/fixed-Wilson commutator failures at `L=5` and held `L=6`. The dense
`J_S5` and eight unused-state exclusions are supplied local register rules.

## Leakage, deletion, and lawful-domain controls

| deletion | residual |
|---|---:|
| one of 120 joint-order amplitudes | Gram `1/120 = 0.008333333333` |
| one composed-update column | unitarity `1` |
| active coin coefficient `-0.659236842151+0.049064365032 i` | unitarity `0.760508963277` |
| nontrivial contact | `0.367893067056` |
| slot cycle | unitarity `1` |
| eight S5 unused-state exclusions | rank surplus `8` |
| retain only one S4 check | common rank factor `5` rather than `1` |

Lawful-domain controls reject total number above two and aliased `L=4`.
Deleting one role amplitude breaks relational normalization; deleting the S5
unused-state rule admits eight off-domain role states.

## Supplied-structure inventory

Supplied are:

1. the Cycle-269 fixed-Wilson reference and face/port dictionary;
2. the Cycle-311 local M64 cell, cell flag, cell companion, and preparation;
3. five addressed cells in the declared `ABCD/ABCE` shared-center geometry;
4. the four edge directions `AB,BD,BC,BE` and their application cycle;
5. the total-five-cell cutoff `n<=2` and arbitrary amplitudes in 466 columns;
6. one 120-state S5 role register encoded in seven M2 and eight local
   unused-state exclusions;
7. the dense `J_S5` coefficients and off-code unitary completion;
8. the two S4 subgroup definitions and the selected plus-sector bases used by
   the register-change comparator;
9. the Cycle-219 coin, Cycle-230 contact, four port FSWAPs, coupling, and
   application order;
10. a four-state slot, one active-edge flag-plus-companion pair, and the
    explicit slot cycle;
11. fixed-reference, role-register, and logical-amplitude preparation; and
12. primitive realization and application of the bounded matrix units.

Derived are the 120 actual physical order isometries, both S4 ranks and order
residuals, register-change diagnostics, the rank-466 S5 gauge, all 24
four-seam updates, joint-code preservation, slot identities, all-frame
covariance, translations, held-size stability, mass preservation, and deletion
residuals.

Still open are `n=3,...,30`, full
`M64 tensor M64 tensor M64 tensor M64 tensor M64`, the six-cell geometry with
distinct adjacent degree-three centers, overlap among several S5 registers,
degree-five or degree-six incidence, recurrent all-edge stream/contact, a
volume collision schedule, primitive synthesis, and arbitrary reference/role
preparation.

## Prior-art and novelty boundary

Cycle 235 supplies the local even/Gauss grammar. Cycle 308 supplies higher
number carriers. Cycle 311 supplies one common M64 physical cell. Cycle 315
supplies the one-edge Z2 role. Cycle 319 supplies the S3 two-edge repair.
Cycle 324 supplies one four-cell S4 star and three-edge slot.

Cycle 327 claims only the actual five-cell shared-center overlap, the exact
failure mode of the two named S4 subgroup projectors, and the bounded joint S5
and four-slot repairs through total `n=2` on this repository substrate.
Regular representations, symmetric-group relations, group averaging,
auxiliary codes, fermionic swaps, and matrix-unit completions are prior-art
territory. Global novelty priority is not asserted.

Thirring machinery is not used or compared.

## TOE dependency ledger

`C_local` advances from one degree-three star to two overlapping star charts on
a 199-M2 patch. `C_int` advances to four distinct incident Cycle-230 seams
through `n=2`. `C_num` does not advance beyond the prior full two-cell and
bounded three/four-cell sectors. `C_ref` retains supplied reference and role
preparation. `C_wrap` and `C_source` are unchanged.

| wall | Cycle-327 movement | still open |
|---|---|---|
| `C_ref` | joint local S5 role replaces two overlapping S4 chart choices | reference genesis and conditional role preparation |
| `C_num` | exact five-cell sectors `n=0,...,2` | `n=3,...,30`, number change, volume full Fock |
| `C_wrap` | unchanged | event equivalence, interval, clock, and rate |
| `C_int` | four incident FSWAP seams plus five-cell contact | repeated arrivals, distinct-center collision, recoil |
| `C_local` | 199-M2 overlap, joint S5, slot transport, frames, held size | multiple S5 overlaps, recurrent schedule, synthesis |
| `C_source` | unchanged | action/energy/stress/source response and gravity relation |

Planning maturity becomes: operational quantum / Records `3.5/5`
(`64/30/91`), causal time / clock `1.9/5` (`35/17/64`), inertia / matter
`4.3/5` (`76/37/97`), gravity / source / resource `2.1/5` (`40/16/67`), and
Born / probability / realized history `2.0/5` (`34/14/85`). Only matter and
local compiler evidence moves. No Record, source, clock, occurrence, or
probability result is added.

## No-Go Discipline Gate

The narrow result is that the two named S4 subgroup projectors do not form a
commuting, order-independent full-plus-sector constraint pair. Their common
rank-one factor remains, the joint S5 succeeds, and the transported slot route
succeeds. Full number, distinct centers, multiple S5 overlaps, and recurrent
volume remain open.

Gate status: **FAIL / DO NOT SHIP the broad adjacent-star or volume negative.**

### N1 — alternative routes

| route | marker | actual attack and disposition |
|---|---|---|
| one selected physical factor order | **ATTEMPTED** | every selected order is isometric, but A/B selection differs by `sqrt(2)` and remains supplied structure |
| two overlapping four-cell S4 projectors | **ATTEMPTED** | common rank factor one survives, but commutator and order residuals defeat a commuting/order-independent reading |
| one joint 120-state S5 role gauge | **ATTEMPTED** | succeeds with seven M2, rank factor one, exact adjacent exchanges, and held-size closure |
| one active edge role with a transported four-slot cycle | **ATTEMPTED** | succeeds with exact slot transport and frame covariance, using no host query |
| five-cell adjacent-star physical shell | **ATTEMPTED** | succeeds through `n=2` for all 120 factor orders, frames, translations, and held `L=6` |
| all four incident FSWAP update orders | **ATTEMPTED** | all 24 orders are unitary, equal on the declared ports, covariant, and mass preserving |
| complete five-cell M64^5 widening | **OPEN / UNTESTED** | sectors `n=3,...,30` are not constructed here |
| overlapping joint S5 registers in a recurrent volume | **OPEN / UNTESTED** | compatibility may close repeated incidence without patch choices |
| alternative bounded role encoding | **OPEN / UNTESTED** | a smaller or sparser local rule may preserve the same rank-one code |

The two constructive role routes and three open routes block a
route-independent negative.

### N2 — wall-independence audit

The collapsed open set is `W_full_number`, `W_overlap_volume`, `W_primitive`,
`W_prepare`, and `W_schedule_global`.

| left | right | closing left closes right? | closing right closes left? | independent? |
|---|---|---:|---:|---:|
| W_full_number | W_overlap_volume | no | no | yes |
| W_full_number | W_primitive | no | no | yes |
| W_full_number | W_prepare | no | no | yes |
| W_full_number | W_schedule_global | no | no | yes |
| W_overlap_volume | W_primitive | no | no | yes |
| W_overlap_volume | W_prepare | no | no | yes |
| W_overlap_volume | W_schedule_global | no | no | yes |
| W_primitive | W_prepare | no | no | yes |
| W_primitive | W_schedule_global | no | no | yes |
| W_prepare | W_schedule_global | no | no | yes |

These walls concern full five-cell number, compatibility of several joint
registers, primitive synthesis, reference/role preparation, and an autonomous
volume collision schedule.

### N3 — hidden-condition scan

The literal procedure-trigger scan runs over both Cycle-327 release paths and
must return zero. The reference, addresses, shared-center geometry, edge list,
number cutoff, role states, unused states, dense coefficients, off-code
completion, coupling, slot rule, preparation, sizes, and tolerances are listed
above.

### N4 — residual matching

| cited witness | witness residual | Cycle-327 residual | match? |
|---|---|---|---:|
| Cycle-311 common M64 runner, exact file and line | one-cell physical M64 isometry | each of five physical factors | yes |
| Cycle-324 four-cell star runner, exact file and line | overlapping subgroup checks versus one joint role | each S4 chart before the S5 overlap | yes |
| exact Cycle-327 runner witnesses | five-cell Gram, role algebra, updates, covariance, deletion | current retained result | yes |

Exact predecessor locations are
`scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py:1018`,
`scripts/physical_cycle269_four_cell_star_cycle324_2026_07_18.py:1121`, and
`scripts/physical_cycle269_four_cell_star_cycle324_2026_07_18.py:1131`.

| current witness | exact file and line |
|---|---|
| 120 actual physical factor orders | `scripts/physical_cycle269_five_cell_adjacent_star_cycle327_2026_07_18.py:1011` |
| overlapping-S4 common rank and order failure | `scripts/physical_cycle269_five_cell_adjacent_star_cycle327_2026_07_18.py:1025` |
| bounded joint S5 repair | `scripts/physical_cycle269_five_cell_adjacent_star_cycle327_2026_07_18.py:1037` |
| four-FSWAP update orders | `scripts/physical_cycle269_five_cell_adjacent_star_cycle327_2026_07_18.py:1047` |
| 24 update intertwiners and mass | `scripts/physical_cycle269_five_cell_adjacent_star_cycle327_2026_07_18.py:1066` |
| frames, geometry orbit, and transported slot | `scripts/physical_cycle269_five_cell_adjacent_star_cycle327_2026_07_18.py:1079` |

No Cycle-324 single-star result is cited against a joint S5 or transported
slot construction.

### N5 — rhetoric and resolution audit

| resolution | tested | disposition |
|---|---|---|
| one Cycle-311 cell | all 64 labels | predecessor M64 isometry retained |
| one Cycle-315 edge | full two-cell Fock | predecessor edge role retained |
| one Cycle-324 four-cell star | all total `n<=2` labels | predecessor joint S4 and three-edge update retained |
| one Cycle-327 five-cell overlap | all total `n<=2` labels | exact 120-order shell and four-edge update |
| two overlapping S4 projectors | complete 120-state role shell | exact common rank and noncommuting/order-dependent result |
| one joint five-cell S5 register | complete 120-state role shell | exact rank-factor-one repair |
| distinct adjacent cubic centers | not tested; requires at least six cells | no compatibility or negative claim |
| overlapping five-cell S5 registers | not tested | no compatibility or negative claim |
| recurrent full-number volume | not tested | no closure or negative claim |

Negative wording is restricted to the two named S4 subgroup projectors on the
tested S5 shell.

### N6 — partial-closure paths

Cycle 311 supplies each physical cell. Cycle 324 supplies one bounded S4 star.
Cycle 327 supplies the joint S5 and four-slot repairs for the first two-chart
overlap. A six-cell distinct-center patch, two overlapping S5 registers, one
larger joint symmetric-group role, slot serialization, full-number widening,
and a smaller bounded role remain direct construction paths. No premise edit
is requested.

The optimal next attack is two overlapping five-cell crosses on the smallest
six- or seven-cell patch, first through total `n<=2`. Compare separate S5
registers, one joint S6/S7 role, and a transported slot before widening number.

### N7 — hostile steelman

A hostile reviewer should reject any adjacent-star or recurrent-volume no-go.
The failed object is only a commuting/order-independent interpretation of two
S4 subgroup checks on their full plus sectors. Their uniform common vector
survives, the bounded joint S5 closes the tested overlap, and the four-slot
route avoids simultaneous subgroup constraints. Two five-cell crosses can
share an S5 role register, use one larger symmetric-group role, or transport
one active slot across their union. Neither volume-compatibility route has
been tested. The evidence calls for the next overlap, not constitutional
pressure.

### N8 — cross-cycle echo

| prior result | retirement mechanism | Cycle-327 lesson |
|---|---|---|
| Cycle 235 total-even boundary | bounded operator algebra | preserve local algebra after a state limitation |
| Cycle 308 odd-carrier boundary | oriented complement carrier | enlarge the local code before a parity negative |
| Cycle 311 cell-order collision | relational cell companion | turn raw order loss into gauge data |
| Cycle 315 endpoint order | local Z2 edge role | repair one adjacent exchange without global order |
| Cycle 319 independent S3 checks | joint S3 role or staggered slot | match one shared-cell patch's overlap group |
| Cycle 324 overlapping S3 checks | joint S4 role or three-slot cycle | enlarge or serialize at degree three |
| Cycle 327 overlapping S4 checks | joint S5 role or four-slot cycle | repeat the constructive retirement at the first star overlap |

Every echo supports a larger-overlap attack. No shared obstruction and no
axiom pressure follow.

## Verification

```text
python3 scripts/physical_cycle269_five_cell_adjacent_star_cycle327_2026_07_18.py
```
