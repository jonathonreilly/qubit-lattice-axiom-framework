# Cycle 516 — Koszul-corrected proper-cubic frame bridge for Cycle 515

Date: 2026-07-21
Authority: none
Audit: unset
Disposition: CONDITIONAL PASS on the declared seven-cell, global-total-N<=2 code

## Result

Cycle 515 proved all 5,040 cell-factor order isometries on one seven-cell
maximal cubic star but left the proper-cubic covariance of the physical
all-order shell open. Cycle 516 closes that residual algebraically on the
declared code. It does not synthesize the dense physical correction or its
constraints from primitive M2 updates.

For a proper-cubic frame `f`, let `rho_f` be its permutation of the seven
cells. Every one of the 24 frames fixes cell 0, the star center. On a logical
label with cell occupations `n_i`, define the block-exchange character

    C_f(label) = (-1)^sum_(i<j, rho_f(i)>rho_f(j)) n_i n_j.

The bare affine physical frame `B_f` carries each local cell factor with its
local exterior-direction sign and transports the order role by
`pi -> rho_f o pi`. The exact order characters `D_pi` cancel under this role
transport. Thus the correction on the correlated Cycle-515 code is `C_f`, not
an additional `D_rho` factor:

    B_f E7 = E7 Rbar_f,
    Rbar_f = R_f C_f,
    Y_f E7 = E7 C_f,
    K_f = B_f Y_f,
    K_f E7 = E7 R_f.

Here `R_f` is the true graded exterior-frame action and `Rbar_f` retains only
the within-cell direction signs. With the Cycle-515 `G_physical` shell and
the supplied bounded-patch realization of `Y_f`, the runner proves on the
code

    K_f G_physical E7 = G_physical K_f E7

for all 24 proper frames. The restricted `K_f` actions also obey all 576
proper-cubic group products. This retires Cycle 515's all-order frame wall on
one bounded star and through total number two. It is not a primitive physical
compiler or a recurrent-volume covariance theorem.

## Exhaustive physical cross-factor certificate

The target passed 12/12 predicates. At both train `L=5` and held `L=6`, it
uses every structurally declared Cycle-311/Cycle-315 local gauge term. It
performs no machine-zero or magnitude-cutoff support query.

Each frame has 7 cells and 42 ordered distinct-cell pairs. The local term
counts at cell number 0, 1, and 2 are respectively 2, 60, and 30. Imposing
`n_i+n_j<=2` leaves 3,964 ordered local-term products per ordered cell pair.

| physical certificate field | train L=5 | held L=6 |
|---|---:|---:|
| affine local-term/frame rows | 15,456 | 15,456 |
| ordered distinct-cell physical pairs | 3,995,712 | 3,995,712 |
| expected physical pairs | 3,995,712 | 3,995,712 |
| target lookup failures | 0 | 0 |
| auxiliary/reference failures | 0 | 0 |
| normalized S+ reference failures | 0 | 0 |
| local discrete-phase failures | 0 | 0 |
| pair target/reference failures | 0 | 0 |
| `S_i`-`Q_rho(j)` commutator failures | 0 | 0 |
| `S_i`-`S_j` commutator failures | 0 | 0 |
| anticommutation-mask transport failures | 0 | 0 |
| pair phase failures | 0 | 0 |
| maximum local amplitude covariance residual | 0 | 0 |
| maximum pair amplitude covariance residual | 0 | 0 |

The source and target pair-mask supports agree at both sizes and are exactly

    0, 1, 2, 4, 8, 16, 32.

These are zero plus the six one-bit masks for the center-arm physical
anticommutation supports, which occupy the first six entries of the 21-pair
index. The arm-arm representatives commute in the witnessed cases even when
their exterior block exchange is odd. This physical support is separate from
the 21 one-bit generators used to prove the full `D_pi` character identity.

For each mapped representative, the audited reference factor is

    S_i = Q_rho(i)^dagger F(P_i),
    q_i = vacuum_phase(S_i),
    S_i^+ = i^(-q_i) S_i.

The certificate verifies `vacuum_phase(S_i^+)=0`,
`[S_i,Q_rho(j)]=0`, and `[S_i,S_j]=0` on every declared pair before reducing
the product phase to `q_i+q_j`. This is the physical cross-factor check that
was absent from the purely logical Cycle-515 covariance boundary.

The exact two-cell occupation cocycle has 3,024 rows
(`24 * C(7,2) * 6`), 180 nontrivial minus rows, and zero failures. Since cell
0 is fixed by every proper frame, only the 15 unordered arm-arm pairs can
carry a nontrivial two-occupied-cell Koszul inversion. Both sizes realize the
exact support

    (1,2) (1,3) (1,4) (1,5) (1,6)
    (2,3) (2,4) (2,5) (2,6)
    (3,4) (3,5) (3,6)
    (4,5) (4,6)
    (5,6).

No center-arm pair is in this support.

## Order characters, group laws, and update covariance

The order-character audit checks zero plus all 21 one-bit pair generators.
Character multiplicativity then extends the identity to every 21-bit branch
mask. The executed counts are:

| exact algebraic audit | rows | failures |
|---|---:|---:|
| frame/order role transports (`24 * 5,040`) | 120,960 | 0 |
| `D_pi` character rows (`24 * 5,040 * 22`) | 2,661,120 | 0 |
| `C_f` cocycle rows (`576 * 904`) | 520,704 | 0 |
| combined `B-D-C-Y` relation (`24 * 904`) | 21,696 | 0 |
| restricted `K_f E7 = E7 R_f` rows | 21,696 | 0 |
| graded, ungraded, and restricted-K group products | 576 each | 0 |

The ungraded maps form a logical permutation representation, but that fact
does not make them the exterior action. The `C_f` factor is load bearing for
the physical/logical intertwiner and for the update. On the exact 904 by 904
Cycle-330 free-plus-contact update:

| quantity | value |
|---|---:|
| `G_star` unitarity residual | `1.877427078863363e-14` |
| maximum corrected `K_f` covariance residual | `1.387000447936191e-15` |
| maximum ungraded covariance residual | `36.33180424917016` |
| maximum deleted-`Y_f` logical intertwiner residual | `2` |
| deleted-`Y_f` physical pair-phase residual | `2` |

The corrected residual is numerical roundoff below the runner tolerance
`4e-12`. Every combinatorial character, map, support, and group-law predicate
is checked exactly.

The update reconstructs the Cycle-219 coin at `beta=-0.3`, the six seam
FSWAP stream, and the Cycle-230 onsite contact at coupling `g=0.37`; therefore
the covariance test is for the full free-plus-contact block rather than its
free part alone. The one-particle sector has `C_f=+1`, so the correction does
not alter the Cycle-515 one-particle fixture. Its inherited rest-mass value is
`0.45340565417488515` (reported fixture `0.4534056541748852`). Cycle 516 does
not refit that value or interpret an update count as physical time.

## Attempt history and test-spec correction

Attempt 1 returned 7/12 solely because its witness gate expected all 21
unordered cell pairs to exhibit a nontrivial two-occupied-cell Koszul
inversion. All 7,991,424 physical pair cases, all substantive failure counts,
and all substantive residuals had already passed. The expectation was wrong:
proper frames fix the center, so the six center-arm pairs cannot be inverted.
The exact nontrivial support is the 15-pair arm domain above: the union of
the three antipodal arm pairs and the twelve perpendicular arm pairs.

This was a test-specification failure, not a physical-route failure. The
runner was corrected to gate equality with that exact support rather than a
count. An intermediate rerun made under stale support nomenclature was
interrupted before evidence packaging so the names could be corrected. It
produced no scientific predicate failure and is not evidence for an
obstruction. The corrected final target passed 12/12.

## Lawful domain, leakage, deletion, and resources

The held `L=6` mask support, histogram, term counts, and exact 15-pair Koszul
support match train `L=5`. An aliased `L=4` request is rejected. A determinant
minus-one reflection is rejected, so the certificate is confined to the 24
proper-cubic frames and makes no parity/reflection claim.

The final captured attempt 4 completed in `337.5217365839053` seconds with
maximum process RSS `139,182,080` bytes and process swap count zero. A
1,200-second alarm is hard.
The 3 GB RSS ceiling and zero-swap conditions are checked at bounded progress
points; the RSS ceiling is not an OS-enforced hard limit. Partial rows survive
caught Python exceptions in memory but are not durable across an OS kill or
process OOM.

Deletion is decisive but narrow. Removing the Koszul correction produces
residual 2 in both the physical pair-phase and logical intertwiner witnesses,
and the ungraded update covariance residual is 36.3318. This falsifies the
bare-frame shortcut on the declared code. It does not falsify other local
gauge, auxiliary, staggered, or primitive-synthesis realizations of the same
`C_f` correction.

## Proven versus supplied

| object | status in Cycle 516 | exact boundary |
|---|---|---|
| 24 proper-cubic cell/direction maps | exhaustive finite proof | all 576 geometry products close; center fixed |
| affine action on inherited local gauge representatives | exhaustive at L5 and held L6 | every declared local term and ordered distinct-cell product tested through N<=2 |
| `D_pi` role-character transport | exact generator proof | zero plus 21 one-bit generators; multiplicativity supplies every mask |
| `C_f` block character | exact on all 904 labels and 24 frames | factorization, cocycle, deletion, and 15-pair support proven |
| `K_f E7 = E7 R_f` and restricted group law | exact on the declared code | 904 columns, 24 frames, 576 products |
| free-plus-contact update covariance | numerical matrix proof below tolerance | full 904-dimensional `G_star`; no support pruning |
| Cycle-515 `E_pi`, `E7`, `Q`, `A_pi`, and lawful S7 role shell | inherited, hash-bound dependency | their Cycle-515 theorem is not reproved here |
| dense `E_pi C_f E_pi^dagger` realization of `Y_f` | supplied | no primitive decomposition or circuit synthesis |
| dense `Q`, off-code completion, and branch-shell matrix-unit application | supplied | bounded algebraic completion only |
| reference, correlated role state, constraint preparation and enforcement | supplied | no autonomous preparation or local-constraint synthesis |
| adjacent-star compatibility and recurrent volume | open | one seven-cell maximal star only |

The complete supplied-structure inventory is:

1. the fixed-Wilson all-`B=+1` reference, its boundary conditions, and its
   preparation;
2. the addressed center and six neighbor cells and their direction/face/port
   dictionary;
3. the Cycle-311 carrier, cell flag, companion, doubled gauge terms, and
   preparation;
4. the global total-`N<=2` cutoff and the 904-label logical basis;
5. all 5,040 lawful S7 order states, the thirteen-M2 role register, the
   correlated `E7` state, and exclusion/identity completion of 3,152 unused
   role states;
6. Cycle 515's `U_pi`, `K_i`, `C_i`, `Q`, `A_pi`, and bounded-patch
   branch-shell matrix-unit application;
7. the dense frame correction `Y_f`, its off-code completion, and physical
   constraint enforcement;
8. `beta=-0.3`, contact coupling `g=0.37`, and the coin-stream-contact update
   order;
9. all physical state and role preparation;
10. patch placement and boundary conditions.

Cycle 516 imports no Cycle-514 mediator, response law, beta fixture, resource
selector, or prediction surface. It makes no adjacent-star, recurrent-volume,
Record, physical-time, source, gravity, Born, probability, response, or broad
TOE closure claim. No global Jordan-Wigner string, volume-wide cell ordering,
or nonlocal parity service appears in the bounded algebra. Autonomous local
realization of the supplied dense correction remains open, so that statement
must not be strengthened into a completed physical-site compiler claim.

## Dependency ledger

| wall | movement | still open |
|---|---|---|
| `C_ref` | the correlated all-order frame relation is now exact on the code | reference genesis; autonomous role, Q, Y, and constraint preparation/enforcement |
| `C_num` | exact pair masks and the 15-pair Koszul support close through total N<=2 | the N<=2 cutoff, full Fock widening, number/source selection |
| `C_wrap` | unchanged | no frame slot, order role, or update count is physical time or a rate |
| `C_int` | the complete coin-stream-contact update is proper-cubic covariant under corrected K on the bounded code | interaction selection, protection, calibrated rate, repeated arrivals and recoil |
| `C_local` | Cycle 515's all-order proper-cubic frame wall closes algebraically on one seven-cell patch | primitive synthesis, local constraint synthesis, adjacent stars, recurrent volume |
| `C_source` | unchanged | conserved source/stress, source renewal, gravity law and backreaction |

Planning estimates after this result are operational quantum/Records
93/54/99, causal time 65/40/99, matter/inertia 82/44/99,
gravity/source/resource 61/32/94, and Born/probability/realized history
76/44/99 (integrated / strict / conditional). These are campaign planning
estimates, not audit grades or probabilities.

## No-go discipline gate N1-N8

The current `origin/main` no-go-discipline skill is applied to the bounded
theorem and its four named open conditions. The exact positive result is not
promoted into an impossibility or minimum-content claim.

### N1 — normalized alternative-route enumeration

Families are distinguished by their primary object, load-bearing mechanism,
and terminal obligation. Only Cycle-516 work is marked ATTEMPTED. Earlier
partial results have authority none and audit unset, so none is marked ruled
out by prior authority.

| family | honesty | object / mechanism | terminal obligation and outcome |
|---|---|---|---|
| bare affine Clifford frame | ATTEMPTED | use `B_f` and within-cell exterior signs only | fails narrowly: deleted-Y residual 2 and ungraded update residual 36.3318 |
| order-character compensation | ATTEMPTED | retain an extra bare `D_rho` character after role transport | exact 2,661,120-row transport shows `D_pi` cancels; this does not supply the missing block-exchange sign |
| Koszul block correction | ATTEMPTED | use the occupation cocycle `C_f` and `K_f=B_fY_f` | succeeds on all 904 labels, 24 frames, and 576 products |
| literal dense frame matrices | OPEN / UNTESTED | materialize every physical `Y_f`/`K_f` block and synthesize its matrix units | algebraic action supplied; primitive synthesis remains terminal |
| local auxiliary/gauge correction | OPEN / UNTESTED | encode the 15 arm-pair character in bounded constrained auxiliaries | must implement `Y_f`, its group law, and constraint enforcement without host control |
| staggered frame transport | PRIOR PARTIAL / OPEN | serialize the six arm roles using the Cycle-330 slot mechanism | bounded logical schedule exists, but no corrected physical `Y_f` synthesis or recurrent overlap proof |
| adjacent-star interaction-character quotient | OPEN / UNTESTED | quotient two overlapping local order/frame roles by their shared interaction character | must close the twelve-cell, eleven-seam overlap and every proper-frame product |

One constructive family succeeds and four materially different
implementation/recurrence families remain open. Therefore a broad no-go has
insufficient route coverage and fails N1. No such no-go is proposed.

### N2 — pairwise wall-independence and collapsed set

The route from the Cycle-516 bounded theorem to a recurrent primitive
physical compiler has four open conditions:

- `W_domain`: widen beyond global total `N<=2`;
- `W_dense`: synthesize and apply the supplied dense `Y_f`, `Q`, `A_pi`, and
  off-code completions from allowed physical primitives;
- `W_prepare`: autonomously prepare and enforce the reference, correlated
  role, `Q`, `C_i`, and frame-correction constraints;
- `W_recur`: make overlapping adjacent stars and recurrent volume compatible
  without a global order or parity service.

| pair | first closes second? | second closes first? | independent? |
|---|---|---|---|
| `W_domain` / `W_dense` | no | no | yes |
| `W_domain` / `W_prepare` | no | no | yes |
| `W_domain` / `W_recur` | no | no | yes |
| `W_dense` / `W_prepare` | no | no | yes |
| `W_dense` / `W_recur` | no | no | yes |
| `W_prepare` / `W_recur` | no | no | yes |

Closing any one does not automatically close another, so the collapsed set
remains four. Cycle 515's former `W_cov` is not retained as a fifth wall: it
is closed algebraically on this bounded code. Time, source/gravity, Records,
Born probability, and prediction are downstream TOE lanes, not inflated as
independent walls of this theorem.

### N3 — hidden-wall phrase scan

The runner and this note were scanned case-insensitively for “we assume,” “by
construction,” “as is standard,” “the framework provides,” “bridge context,”
“background,” “naturally,” “obviously,” “standard QFT,” “registered,” and
“canonical.” Apart from this required search inventory, the final note has no
hits, and the runner has no hits. Dense realization, constraint enforcement,
global `N<=2`, fixed reference preparation, patch placement, and boundary
conditions are explicit supplied conditions rather than hidden walls. The N2
count remains four.

### N4 — exact residual matching

| cited path and line | witness residual | Cycle-516 residual | match? / disposition |
|---|---|---|---|
| `PHYSICAL_CYCLE330_ALL_ORDER_ISOMETRY_BRIDGE_CYCLE515_NOTE_2026-07-20.md:127-140` | physical all-order `E_pi/A_pi` proper-cubic covariance open | construct the missing corrected frame intertwiner and update equivariance | yes; exact predecessor residual |
| `PHYSICAL_CYCLE269_SEVEN_CELL_MAXIMAL_STAR_CYCLE330_NOTE_2026-07-18.md:154-166` | logical slot/frame covariance on six arms | correlated all-order physical-shell covariance | no; logical mechanism context only, dropped as a direct witness |
| `PHYSICAL_CYCLE269_OVERLAP_AWARE_TWO_CELL_CYCLE315_NOTE_2026-07-18.md:169-173` | two-cell endpoint-role frame covariance | seven-cell all-order frame correction | no; local predecessor mechanism only, dropped as a direct witness |
| `PHYSICAL_CYCLE330_ALL_ORDER_ISOMETRY_BRIDGE_CYCLE515_NOTE_2026-07-20.md:97-117` | algebraic `A_pi` update lift with dense physical application supplied | corrected `K_f` covariance conditional on the same shell | dependency match, not an independent covariance witness |

Only Cycle 515 is used as a direct witness for the residual closed here. No
prior no-go is used to support an impossibility, and no mismatched residual is
counted toward negative evidence.

### N5 — rhetoric and resolution audit

| narrow statement | per-site/mode | bounded block | lattice-wide | licensed wording |
|---|---|---|---|---|
| primitive synthesis was not executed | not tested | true for this runner | not tested | “Cycle 516 does not synthesize the bounded dense correction from primitives” |
| local constraint synthesis remains open | not tested | supplied, not synthesized | not tested | “local constraint synthesis is open on this patch” |
| covariance beyond total N<=2 remains open | one-particle and two-particle sectors tested | N<=2 only | not tested | “the proof is confined to the 904-label N<=2 code” |
| adjacent/recurrent compatibility remains open | not applicable | one star tested | not tested | “adjacent stars and recurrent volume are untested” |
| physical time is absent from the result | no clock observable or calibration tested | no time bridge executed | not tested | “Cycle 516 executes no causal-time bridge” |

No bounded non-execution statement is promoted into a universal per-site,
per-mode, per-block, or lattice-wide impossibility.

### N6 — partial-closure and import-retirement paths

| path | status | what it closes or could close |
|---|---|---|
| exact `D_pi` transport quotient | complete on the Cycle-516 domain | retires an unnecessary extra `D_rho` correction |
| exact Koszul `C_f` quotient | complete on the Cycle-516 domain | retires Cycle 515's bounded all-order covariance wall without constitutional change |
| exhaustive physical pair-stabilizer audit | complete at L5 and held L6 | closes the cross-factor phase premise for every declared N<=2 term pair |
| bounded local auxiliary/gauge synthesis of the 15-pair character | open constructive route | could retire `W_dense` and part of `W_prepare` |
| Cycle-330 slot serialization | prior partial route | could organize overlap scheduling, but does not establish physical time |
| adjacent-star interaction-character quotient | next constructive target | could retire `W_recur` before a full recurrent-volume census |

This note makes no claim that a new axiom is required and no claim equivalent
to absence of an approved primitive. Existing premises are neither edited nor
silently promoted. The positive result follows the explicit-import, bounded
theorem, future import-retirement pattern.

### N7 — hostile steelman

A hostile reviewer should reject any broad obstruction immediately: Cycle 516
has already reduced the missing frame action to a finite 15-pair occupation
character, proved its cocycle, and shown that it repairs the full update. A
concrete unclosed mechanism is to compute that character into bounded
arm-pair auxiliaries, enforce their parity relations with local commuting
constraints, apply the phase, and uncompute. The terminal obligations are an
explicit primitive decomposition of `Y_f`, exact local constraint closure,
and compatibility of two overlapping seven-cell centers under all 24 proper
frames at train and held sizes. The Cycle-315 local role-gauge repair and
Cycle-330 slot construction show that local role enlargement and
serialization remain live mechanisms. This steelman is actionable, so any
broad no-go is premature.

### N8 — cross-cycle echo

| prior wall | later mechanism | relevance now |
|---|---|---|
| Cycle-311 raw cell-role collisions | relational flag plus companion | preserve local order data as constrained gauge data rather than erase it |
| Cycle-315 AB/BA endpoint-order mismatch | doubled local edge role plus gauge companion | a fermionic ordering mismatch need not force a volume-wide order |
| Cycle-327 overlapping subgroup mismatch | joint local role or slot transport | enlarge or serialize a bounded role before claiming incompatibility |
| Cycle-330 5,032 unmaterialized orders | Cycle-515 exact anticommutation-character quotient | replace exhaustive dense matrices by a generator theorem |
| Cycle-515 all-order frame covariance wall | Cycle-516 `D_pi` cancellation plus Koszul `C_f` correction | isolate and prove the exact residual character before seeking new premises |

Every closely matching local-order wall in this chain was narrowed or retired
constructively. The same mechanisms are included in the next recurrence and
synthesis targets.

Gate outcomes:

- Cycle-516 result: positive bounded theorem with four explicit supplied/open
  conditions;
- broad no-go for compiler impossibility, minimum physical content,
  route-independent substrate obstruction, or axiom pressure: **FAIL / NOT
  PROPOSED**;
- constitutional effect: none; authority remains none and audit remains unset.

## Next campaign

The optimal next campaign is the two-adjacent-maximal-center overlap with
corrected frame roles. Begin with the twelve-cell, eleven-seam union and an
exact interaction-character quotient before attempting a full physical-row
census. The construction must count the shared seam and shared onsite terms
once, reconcile the two local S7 roles without a global order, prove every 24
proper-frame action and 576 group product, retain the contact/update block,
and repeat at a lawful held size. In parallel within that campaign, reduce the
15-pair `C_f` character to an explicit bounded auxiliary/gauge phase gadget so
the algebraic `Y_f` import can begin a primitive-synthesis retirement audit.

## Evidence hash

| artifact | SHA-256 |
|---|---|
| Cycle-516 runner | `3c4318a84c661893932c8d41a90db36445f80cefd092a6a3fffb56cbf8abfa9c` |
| dry contract | `2240ce21169dc6e9ba42277c1c68cc0b70b188d4a83b2bb49c91e1a0c9381920` |
| target attempt 4 | `710673f10229675789ab84abe24d15238f0b9b1674608b0254a77c02860ebcce` |

The dry contract passed 10/10. The final target log is
`outputs/physical_cycle515_koszul_frame_bridge_cycle516_attempt4_2026_07_21.log`;
it reports PASS 12/12, elapsed `337.5217365839053` seconds, maximum RSS
`139,182,080` bytes, and zero process swap. The packet receipt is generated
separately after this note is frozen so it can bind the note hash without a
circular dependency.
