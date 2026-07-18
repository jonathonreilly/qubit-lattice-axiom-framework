# Physical Cycle-269 seven-cell maximal-star discriminator — Cycle 330

Date: 2026-07-18

Authority: none

Audit: unset

Constitutional effect: none. No axiom, foundation, Qualification, primitive,
registry, policy, queue, or audit status is edited or proposed.

Companion runner:

```text
scripts/physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18.py
```

Methodology freshness: the no-go-discipline procedure, freshness instructions,
and all case studies were read completely from freshly fetched `origin/main` at
`dff46683ef459767735303792c4143fc93956a58`. The dirty worktree was not moved.

## Result and sampling boundary

Cycle 330 tests one center and all six proper-cubic neighbors through total
number `n=0,...,2`. The exterior logical space is

```text
H_7,<=2 = direct sum from n=0 to 2 of wedge^n(C^42),
dimension = 1 + 42 + 861 = 904.
```

All 5,040 cell-factor orders have distinct exact 21-bit Pauli inversion masks.
Eight physical order matrices are materialized: identity order, its six
adjacent exchanges, and reversal. Each has 904 columns and 2,459,648 occupied
physical rays/nonzero amplitudes at training `L=5` and held `L=6`. The eight
orders contain 19,677,184 selected nonzero amplitudes. The maximum selected raw
Gram entry is `6.883382752676e-14`; the sampled joint raw Gram entry is
`6.905587213168e-14`, and its sampled minimum eigenvalue is at least
`0.999999999999`. Processed residuals vanish.

Eight selected branches against the eight selected orders give 64 direct
multiplication samples with zero support or phase failures. The other order
signs are exactly addressable from the branch anticommutation mask and order
inversion mask, but 5,032 physical matrices remain unmaterialized. This note
does not turn exact mask enumeration into 5,040 physical Gram calculations.
No sampled physical Gram is cited as an all-5040 Gram theorem.

Identity versus the first adjacent exchange has residual
`1.414213562373093`; identity versus reversal has residual
`1.414213562373087`. A role for physical factor order remains necessary on
this encoding.

## Candidate encoding and exact boundary

For a physical isometry `E_pi` in factor order `pi in S7`, the candidate local
relational encoding is

```text
E_7 = (1/sqrt(5040)) sum_(pi in S7) |pi> tensor E_pi.
```

For a declared logical update `G`, its code-space lift would be

```text
G_physical = sum_pi |pi><pi| tensor (E_pi G E_pi^dagger) + G_perp,
E_7 G = G_physical E_7.
```

The 5,040-state role algebra, logical update, and code-space Kronecker
identities below are exact. Only eight physical `E_pi` matrices and 64 direct
branch products are checked. Therefore the displayed physical intertwiner is
a sampled compiler candidate, not a completed all-order physical-site
compiler. `G_perp`, its dense bounded coefficients, and primitive application
are supplied imports.

No global Jordan-Wigner string, global parity service, preferred axis, global
ordering, or host-side order service appears. This remains one bounded
seven-cell patch, not a recurrent-volume theorem.

## Lower subgroups and joint S7 role

Nested S4, S5, and S6 subgroup averages inside S7 have plus-rank factors 210,
42, and 7, with vanishing nested projector commutators. The decisive overlap
uses the two S6 groups that omit opposite arms. Each has plus-rank factor 7;
their common factor is one, giving logical common rank 904.

The two overlapping S6 checks are not commuting or order-independent on their
full plus sectors:

```text
constraint commutator                       = 0.657342198122
projector commutator                        = 0.164335549531
P_left P_right P_left versus reverse order = 0.0273892582551
```

Ordinary matrix associativity remains: the matrix associator is
`1.603789345262e-16`, the explicit register-change associator is
`1.861900614935e-16`, and the common vector transports with residual
`2.557130686372e-15`. Direct register change versus transport through only the
joint code differs by `0.166666666667` away from that common vector. This is a
narrow failure of those two full-plus-sector checks, not a failure of their
intersection or of a joint role.

The repair uses all 5,040 lawful S7 order states in thirteen M2. A local domain
rule excludes 3,152 unused states of the 8,192-state computational shell. Let

```text
|u_5040> = (1/sqrt(5040)) sum_(pi in S7) |pi>,
J_S7 = 2 |u_5040><u_5040| - I_5040.
```

The `J_S7=+1` relational code has rank 904 after the logical factor is
included. Constraint involution, adjacent-swap invariance, all adjacent braid
maps, and all far-commutator maps pass. The uniform eigenvector residual is
`6.650270090601e-15`. Two literal S6 registers cost twenty M2; the joint S7
register costs thirteen M2. Dense `J_S7` coefficients and unused-state
exclusions remain supplied local rules.

## Six-seam free-plus-contact update

The six edges connect the center to `-x,+y,+x,-y,+z,-z`. They use six
distinct-port FSWAPs. For every `sigma in S6`, the tested update is

```text
U_sigma = D_7 S_(sigma(6)) ... S_(sigma(1))
          Gamma(C direct-sum ... direct-sum C),
D_7 = exp(i g sum_j binom(n_j,2)),
g = 0.37.
```

The coin has 28,834 active coefficients. Each FSWAP has 904 signed entries,
and the Cycle-230 contact is nontrivial on 105 columns. Coin, contact, and
composed-update raw unitarity maxima are respectively
`6.661438741028e-16`, `2.226534750407e-17`, and
`6.661448395737e-16`. All 15 pairwise stream commutators vanish, so all 720
six-edge order tokens are equal on the declared logical patch. Seven selected
direct order comparisons also vanish.

| total number | dimension | composed-update unitarity after tolerance |
|---:|---:|---:|
| 0 | 1 | 0 |
| 1 | 42 | 0 |
| 2 | 861 | 0 |

The exact role-factor lift has zero update/constraint commutator and zero
intertwining residual; the joint code Gram residual is
`3.330669073876e-15`. The uniform one-particle state retains mass
`0.453405654174885`, matching the Cycle-219 mass fixture within `2e-16`; its
eigenvector residual is `1.810439732249e-16`.

Contact phase is not called mass or physical energy, a generator element is
not called a rate, and the compiler schedule is not called time.

## Six-slot comparator, covariance, and support

The staggered comparator uses six lawful slot states in three M2, excludes two
unused states, and carries one active-edge flag-plus-companion pair in two M2.
The local rule cycles the active edge through the six center ports. Slot
unitarity, its sixth power, macro unitarity, active-constraint involution,
constraint transport, and frame covariance have residual zero. The slot moves
under the local matrix rule; `host queries = 0`. This is a compiler schedule,
not physical time or a volume collision policy.

All 24 proper-cubic frames give an ordered six-arm orbit of size 24. Exterior
representation unitarity and processed update-covariance residuals vanish;
the maximum raw covariance entry is `6.206335383118e-17`. There are 576 frame
group-law tests and 15,625 translation-address tests, both with zero failures.

The selected patch union is 263 M2 before the joint role and 276 M2 after its
thirteen M2 are added. The largest selected physical branch uses 39 M2 before
the role and 52 after it; the largest selected local input branch uses 36.
These are observed selected-order counts, not lower bounds. Every selected
branch has zero inherited port-constraint and fixed-sector commutator failures
at `L=5` and held `L=6`.

## Deletion and lawful-domain controls

| deletion | residual or surplus |
|---|---:|
| one of 5,040 joint-order amplitudes | Gram `1/5040 = 0.000198412698413` |
| one update column | unitarity `1` |
| active coin coefficient `-0.659236842151+0.049064365032 i` | unitarity `0.760508963277` |
| nontrivial contact | `0.367893067056` |
| slot cycle | unitarity `1` |
| omit 3,152 S7 unused-state exclusions | rank surplus `3,152` |
| omit two slot exclusions | rank surplus `2` |
| retain only one S6 check | common rank factor `7` rather than `1` |

Lawful-domain controls reject total number three and aliased `L=4`. These
deletion, exclusion, leakage, held-size, and lawful-domain controls do not
test sectors above the declared cutoff.

## Supplied-structure inventory

Supplied are:

1. the Cycle-269 fixed-Wilson reference and face/port dictionary;
2. the Cycle-311 local M64 cell, cell flag, cell companion, and preparation;
3. the center, six neighbor addresses, and their proper-cubic directions;
4. the total-seven-cell cutoff `n<=2` and arbitrary amplitudes in 904 columns;
5. the exact 21-bit inversion-mask grammar, eight selected physical orders,
   and the 64 direct multiplication samples;
6. the 5,040 lawful S7 states in thirteen M2 and 3,152 local exclusions;
7. the dense `J_S7` coefficients and off-code unitary completion;
8. the lower-subgroup definitions and selected plus-sector bases;
9. the Cycle-219 coin, Cycle-230 contact, six port FSWAPs, coupling, and
   application order;
10. the six-slot state in three M2, two exclusions, and active-edge pair in two
    M2;
11. fixed-reference, role-register, and logical-amplitude preparation; and
12. primitive realization and application of the bounded matrix units.

Derived are exact logical dimensions, the eight selected physical Grams and
held-size checks, all S7 inversion masks, the lower-subgroup ranks and overlap
algebra, the rank-904 joint role code, all 720 logical updates, mass
preservation, frame and translation checks, slot identities, support counts,
and deletion residuals.

Still open are the 5,032 unmaterialized physical S7 matrices, sectors
`n=3,...,42`, the complete seven-cell `M64^7` widening, adjacent maximal stars,
overlapping joint registers in a recurrent volume, autonomous volume
collision, primitive synthesis, and arbitrary reference/role preparation.

## Prior-art and novelty boundary

Cycle 235 supplies the local even/Gauss grammar. Cycle 308 supplies higher
number carriers. Cycle 311 supplies the common M64 physical cell. Cycle 315
supplies the one-edge Z2 role. Cycle 319 supplies the S3 repair. Cycle 324
supplies one S4 star, and Cycle 327 supplies its first S5 overlap.

Cycle 330 claims only the exact seven-cell logical update, exact S7 role
algebra, eight selected physical order isometries, exact order-mask grammar,
and six-slot/covariance checks through `n=2` on this repository substrate.
Regular representations, symmetric-group relations, group averaging,
auxiliary codes, fermionic swaps, and matrix-unit completions are prior-art
territory. Global novelty priority is not asserted. Thirring machinery is not
used or compared.

## TOE dependency ledger

`C_local` advances from a four-port overlap to one maximal-degree cubic cell,
with the important physical-order sampling wall retained. `C_int` advances to
all six incident Cycle-230 seams through `n=2`. `C_num` does not advance beyond
bounded low-number sectors. `C_ref` retains supplied reference, role, and
amplitude preparation. `C_wrap` and `C_source` are unchanged.

| wall | Cycle-330 movement | still open |
|---|---|---|
| `C_ref` | bounded joint S7 role removes a choice among two overlapping S6 charts | reference genesis and conditional role preparation |
| `C_num` | exact seven-cell sectors `n=0,...,2` | `n=3,...,42`, number change, volume full Fock |
| `C_wrap` | unchanged | event equivalence, interval, clock, and rate |
| `C_int` | six incident FSWAP seams plus seven-cell contact | repeated arrivals, adjacent maximal stars, recoil |
| `C_local` | one 276-M2 maximal star, role, slot, frames, held size | 5,032 physical orders, adjacent stars, recurrent schedule, synthesis |
| `C_source` | unchanged | action/energy/stress/source response and gravity relation |

Rebased on the accepted concurrent Cycle-331 and Cycle-332 evidence, planning
maturity becomes: operational quantum / Records `3.7/5` (`66/32/93`), causal
time / clock `2.1/5` (`37/19/68`), inertia / matter `4.4/5` (`77/38/98`),
gravity / source / resource `2.3/5` (`42/17/70`), and Born / probability /
realized history `2.0/5` (`34/14/85`). Only bounded compiler and matter
evidence moves in Cycle 330. No Record, source, clock, occurrence, or
probability result is added by Cycle 330.

## No-Go Discipline Gate

The narrow negative is that the two named overlapping S6 subgroup projectors
do not form commuting, order-independent checks on their full plus sectors.
Their common rank-one factor survives; the joint S7 role, all 720 logical
updates, and the slot route succeed. Full physical-order materialization,
full number, adjacent maximal stars, and recurrent volume remain open.

Gate status: **FAIL / DO NOT SHIP the broad maximal-star or volume negative.**

### N1 — alternative routes

| route | marker | actual attack and disposition |
|---|---|---|
| one selected physical factor order | **ATTEMPTED** | selected orders are isometric, but adjacent order selection differs by `sqrt(2)` |
| exact 21-bit S7 inversion-mask compression | **ATTEMPTED** | all 5,040 masks are distinct and 64 direct products validate the sign grammar; most full matrices remain open |
| overlapping lower-Sk subgroup projectors | **ATTEMPTED** | exact ranks survive but the two S6 full-plus checks do not commute or give order independence |
| one joint 5040-state S7 role gauge | **ATTEMPTED** | succeeds in thirteen M2 with one rank factor and explicit unused-state exclusions |
| one active edge role with a six-slot cycle | **ATTEMPTED** | succeeds with local transport, frame covariance, and no host query |
| all 720 six-edge logical update orders | **ATTEMPTED** | all orders coincide through `n=2` because every tested stream pair commutes |
| all 5040 physical order matrices | **OPEN / UNTESTED** | 5,032 matrices and their full Grams are not materialized |
| complete seven-cell M64^7 widening | **OPEN / UNTESTED** | sectors above total number two are absent |
| overlapping maximal-star registers in a recurrent volume | **OPEN / UNTESTED** | no adjacent maximal-star or volume compatibility test is run |
| alternative bounded role encoding | **OPEN / UNTESTED** | a smaller or sparser role may preserve the same common code |

Constructive joint-role and slot routes plus the four open routes block a
route-independent negative.

### N2 — wall-independence audit

The collapsed open set is `W_order_materialization`, `W_full_number`,
`W_overlap_volume`, `W_primitive`, `W_prepare`, and `W_schedule_global`.

| left | right | closing left closes right? | closing right closes left? | independent? |
|---|---|---:|---:|---:|
| W_order_materialization | W_full_number | no | no | yes |
| W_order_materialization | W_overlap_volume | no | no | yes |
| W_order_materialization | W_primitive | no | no | yes |
| W_order_materialization | W_prepare | no | no | yes |
| W_order_materialization | W_schedule_global | no | no | yes |
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

These walls respectively concern complete physical order evidence, full
number, multi-star compatibility, primitive synthesis, preparation, and an
autonomous volume schedule.

### N3 — hidden-condition scan

The literal procedure-trigger scan runs over both Cycle-330 release paths and
must return zero. The reference, cells, port directions, number cutoff, role
states, exclusions, dense coefficients, off-code completion, coupling, slot
cycle, preparation, selected orders, sizes, and tolerances are listed above.

### N4 — residual matching

Cycle-311 common M64 runner evidence supplies each local factor. The Cycle-327
five-cell overlap runner supplies the predecessor joint-role and multi-seam
comparators. The exact Cycle-330 runner witnesses below match the current
physical Gram, role, update, covariance, and deletion claims. No sampled
physical Gram is cited as an all-5040 Gram theorem.

Predecessor locations include
`scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py:1018`
and
`scripts/physical_cycle269_five_cell_adjacent_star_cycle327_2026_07_18.py:1011`.

| current witness | exact file and line |
|---|---|
| eight selected physical orders and exact masks | `scripts/physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18.py:1014` |
| overlapping lower-subgroup ranks and S6 residuals | `scripts/physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18.py:1031` |
| bounded joint S7 role | `scripts/physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18.py:1044` |
| all 720 logical update orders | `scripts/physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18.py:1055` |
| joint role update and mass fixture | `scripts/physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18.py:1078` |
| frames and local slot | `scripts/physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18.py:1088` |

### N5 — rhetoric and resolution audit

The tested resolutions are one cell, the eight materialized physical orders,
the complete 5040-state role shell, one seven-cell maximal star, and its six
logical seams through total `n<=2`. The untested resolutions are the remaining
physical order matrices, adjacent maximal stars, and a recurrent full-number
volume. A lower-subgroup failure is not promoted across those boundaries.

N5 separates sampled orders, role shell, maximal star, adjacent stars, and
volume. No volume closure or minimum-content statement is made.

### N6 — partial-closure paths

Cycle 311 supplies each local M64 cell. Cycle 327 supplies the predecessor
overlap and joint-role comparator. Cycle 330 supplies exact S7 order masks,
the joint role, maximal-star logical update, and six-slot comparator. The
optimal next attack is a streamed all-5,040 physical Gram proof or complete
batch calculation through `n=2`, followed by two adjacent maximal stars with
overlapping joint registers. Full-number widening, primitive synthesis, and a
smaller bounded role remain independent constructive paths. No premise edit
is requested.

### N7 — hostile steelman

A hostile reviewer should reject any maximal-star or recurrent-volume no-go.
The 5,032 unmaterialized physical orders could expose a Gram failure despite
the exact sign masks and selected direct products. An adjacent-star
construction could also share one larger role register or serialize incidence
with a transported slot. Neither route has been tested. The failed object is
only the simultaneous commuting/order-independent reading of the two named S6
full-plus sectors.

### N8 — cross-cycle echo

| prior result | retirement mechanism | current lesson |
|---|---|---|
| Cycle 235 total-even boundary | bounded operator algebra | preserve the algebra after a state limitation |
| Cycle 308 odd-carrier boundary | oriented complement carrier | enlarge the code before a parity negative |
| Cycle 311 cell-order collision | relational cell companion | retain raw order as gauge data |
| Cycle 315 endpoint order | local Z2 edge role | repair one exchange without global order |
| Cycle 319 independent S3 checks | joint S3 role or staggered slot | match the local overlap group |
| Cycle 324 overlapping S3 checks | joint S4 role or three-slot cycle | enlarge or serialize degree three |
| Cycle 327 overlapping S4 checks | joint S5 role or four-slot cycle | repeat the repair at the first chart overlap |
| Cycle 330 overlapping S6 checks | joint S7 role or six-slot cycle | retain both repair mechanisms at maximal degree |

Every echo supports further construction. No shared obstruction and no axiom
pressure follow.

Still open are the 5,032 unmaterialized physical S7 matrices and every
multi-maximal-star or recurrent-volume realization. No shared obstruction and
no axiom pressure follow.

## Verification

```text
python3 scripts/physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18.py
```
