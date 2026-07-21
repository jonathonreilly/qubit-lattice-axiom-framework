# Cycle 515 — exact all-order Cycle-330 isometry and relational-code bridge

Date: 2026-07-20
Authority: none
Audit: unset
Disposition: CONDITIONAL PASS on the declared seven-cell, total-N<=2 domain

## Result

Cycle 330 materialized eight of the 5,040 physical cell-factor orders on one
seven-cell maximal cubic star. Cycle 515 removes that sampling wall without
constructing the other 5,032 matrices.

For every structural branch b, let a_b be its exact 21-bit pair
anticommutation mask and I_pi the inversion mask of pi in S7. Exact Pauli
algebra gives

    product_pi(b) = (-1)^popcount(a_b AND I_pi) product_id(b).

The Cycle-515 train-L5 and held-L6 censuses each enumerate all 2,459,648
structural branch products. Every branch reaches a distinct physical
auxiliary ray globally, including across logical columns:

| field | L=5 | held L=6 |
|---|---:|---:|
| logical columns | 904 | 904 |
| structural branches | 2,459,648 | 2,459,648 |
| physical rows | 2,459,648 | 2,459,648 |
| row reuses / collision pairs | 0 | 0 |
| maximum multiplicity | 1 | 1 |
| incompatible mask pairs | 0 | 0 |
| exact mask-histogram SHA-256 | 398beef0400305f150184ab23afcfeb6da1da102b8d3f0ab7c45443e09806a4d | same |
| maximum amplitude-squared diagnostic residual | 1.1102230246251565e-16 | same |

The exact sector census at both sizes is:

| sector | columns | branches |
|---|---:|---:|
| n=0 | 1 | 128 |
| n=1 | 42 | 26,880 |
| n=2, same cell | 105 | 13,440 |
| n=2, split cells | 756 | 2,419,200 |
| total | 904 | 2,459,648 |

The amplitude theorem is not inferred from term counts alone. The runner
hash-binds the Cycle-311 and Cycle-315 implementations, checks their exact
unit-phase, permutation-sign, sqrt(6-n), and duplicated-sqrt2 grammar, and
gates the theorem on the realized amplitude-squared diagnostic at both sizes.
No machine-zero or magnitude cutoff selects structural support.

It follows exactly, on the declared branch shell and logical domain, that

    E_pi^dagger E_pi = I_904

for all 5,040 pi. The correlated role encoding

    E7 = (1/sqrt(5040)) sum_pi |pi> tensor E_pi

therefore also has Gram I_904. Cycle 330's eight matrices remain the only
materialized order matrices; Cycle 515 proves all 5,040 through the exact
character theorem and leaves zero order isometries unproved on this domain.

## Correction to the role-only shortcut

A uniform S7 role constraint acting only on the order register is not a
physical relational constraint when E_pi differs with pi. Cycle 515 does not
use Cycle 330's hard-coded joint-update zero residuals.

Let U_pi be the diagonal exact character operator on physical branch rays.
For the right action pi -> pi s_i, define

    K_i(pi) = U_(pi s_i) U_pi^dagger,
    C_i = sum_pi |pi s_i><pi| tensor K_i(pi).

All 30,240 adjacent-role transports, six involutions, five braid families,
and ten far-generator families pass through exact endpoint and XOR-mask
identities. There are zero involution, braid, far-commutator, or endpoint
failures.

The common C_i=+1 shell has rank 2,459,648, not 904. A separate transported
code-shell projector is required:

    Q = sum_pi |pi><pi| tensor E_pi E_pi^dagger.

Its rank is 5,040*904 = 4,556,160. The intersection of Q with the common
relational plus sector is exactly the E7 image and has rank 904.

An explicit two-role discriminator prevents the old shortcut from returning:
the role-only invariance residual squared is 1.9999999999999991, while the
controlled physical transport residual is zero. The relational projector has
rank two in the toy shell; its intersection with Q has rank one.

## Algebraic update lift

For the existing Cycle-330 six-seam logical unitary G_star, define

    A_pi = E_pi G_star E_pi^dagger + I - E_pi E_pi^dagger.

Then, on the 5,040 lawful role states,

    G_physical = direct-sum_pi A_pi

is unitary and satisfies

    E7 G_star = G_physical E7.

The full thirteen-M2 role register has 8,192 computational states. The 3,152
unused states are explicitly excluded from the lawful domain and receive an
identity completion. The transported A_pi blocks commute with Q and the C_i
constraints by the exact U transport identity. Repeated powers on this same
bounded patch retain the intertwiner.

This is a bounded algebraic physical-shell completion. Cycle 515 does not
execute primitive synthesis. Dense Q coefficients, bounded-patch branch-shell
matrix units, their application, the off-code identity completion,
unused-state exclusions, physical realization and enforcement of U_pi/K_i/C_i
and Q, and preparation of the correlated role state remain supplied.

The one-particle Cycle-219/Cycle-330 fixture remains
0.4534056541748852 at beta=-0.3. The computed rest-mass value is
0.45340565417488515, the uniform eigenvector residual is
2.594441202963249e-16, and the coin unitarity residual is
1.2236950713340232e-15. There are 105 contact-active columns, the
nontrivial-contact deletion residual is 0.36789306705608243, and all 720
logical orders of the six disjoint-port FSWAPs agree.

## Covariance boundary

The runner executes 24 one-particle direction permutations and 576 logical
frame group products with zero group-law failures. These checks do not prove
proper-cubic covariance of every U_pi, E_pi, or A_pi physical block.

Therefore:

- all-order physical E_pi proper-cubic covariance: OPEN;
- all-order A_pi frame equivariance: OPEN;
- full physical compiler covariance: NOT CLAIMED.

This quarantine is load-bearing. Cycle 515 must not be described as the final
proper-cubic physical compiler.

## Bounded support and resource record

The inherited Cycle-330 patch uses 263 physical M2 before the role and 276
after its thirteen M2 are included. The largest structural branch uses 39 M2
before the role and 52 after it. These are observed upper counts on one
seven-cell patch, not lower bounds and not recurrent-volume costs.

The corrected attempt-2 target passed 13/13 predicates in
69.10966804099735 seconds with 1,435,680,768 bytes maximum process RSS and
zero process swap. The 1,200-second
alarm is hard. The 3 GB RSS ceiling and zero-swap conditions are checked at
bounded progress intervals; they are not OS-enforced hard limits. Partial
rows survive caught Python exceptions in memory but are not durable across an
OS kill or process OOM.

The dry contract passed 14/14. Review-history details are process provenance,
not part of the hash-bound scientific receipt.

## Supplied structure

Cycle 515 still supplies or inherits:

1. the fixed-Wilson all-B=+1 reference and preparation;
2. the Cycle-269 face/port dictionary and orientations;
3. the addressed center and six neighbors;
4. the Cycle-311 carrier, cell flag, companion, and gauge preparation;
5. the global total-N<=2 cutoff;
6. the E_pi/E7 branch-shell coefficient tables, the 5,040-state lawful S7
   role domain, and correlated E7 preparation;
7. exclusion and identity completion of 3,152 unused role states;
8. physical realization and enforcement of U_pi, K_i, and C_i;
9. the dense transported code-shell projector Q and its enforcement;
10. dense A_pi coefficients, bounded-patch branch-shell matrix-unit
    application, and off-code completion;
11. beta=-0.3, contact coupling g=0.37, and coin-stream-contact order;
12. all physical state preparation;
13. patch placement and boundary conditions.

Cycle 514 contributes only exact-support discipline and the fact that its
comparison domain also retains total N<=2. Cycle 515 does not import the
Cycle-514 Q6/L15 receiver, Q(zeta_9)[z] coefficients, beta=-4pi/9 fixture,
mediator dynamics, response law, resource selector, or prediction surface.
The two encodings and laws are not identified.

## Dependency ledger

| wall | movement | still open |
|---|---|---|
| C_ref | the physical role relation is corrected and its required Q shell is explicit | reference genesis, autonomous Q/role preparation, unused-state law |
| C_num | exact branch normalization and the total-N<=2 sector ledger are closed | the N<=2 cutoff, full Fock widening, number/source selection |
| C_wrap | unchanged | no order slot or update count is physical time or a rate |
| C_int | the bounded contact and same-code update survive every S7 order algebraically | interaction selection, beta bridge to Cycle 514, protection, calibrated rate |
| C_local | all 5,040 one-star order isometries and the corrected relational shell close | all-order proper-cubic physical covariance, primitive synthesis, adjacent stars, recurrent volume |
| C_source | unchanged | conserved source/stress, source renewal, gravity law and backreaction |

Planning estimates after this result are operational quantum/Records
92/51/99, causal time 65/40/99, matter/inertia 82/44/99,
gravity/source/resource 61/32/94, and Born/probability/realized history
76/44/99 (integrated / strict / conditional). These are campaign planning
estimates, not audit grades or probabilities.

## No-go discipline gate N1-N8

The current origin/main no-go-discipline skill is applied to the named open
conditions. The exact positive theorem above is not converted into a negative
claim.

### N1 — normalized alternative-route enumeration

The families differ in primary object, mechanism, and terminal obligation.
No route is marked RULED OUT BY PRIOR because every cited predecessor retains
authority none and audit unset. The current skill permits ATTEMPTED only for
Cycle-515 work. Prior incomplete routes are therefore labeled PRIOR PARTIAL
ATTEMPT / OPEN; those labels deliberately fail negative closure rather than
pretend the routes were tested in this cycle or ruled out.

| family | honesty | attempted object and mechanism | outcome and cited evidence |
|---|---|---|---|
| literal order matrices | PRIOR PARTIAL ATTEMPT / OPEN | construct every E_pi and test each Gram directly | Cycle 330 materialized eight matrices and left 5,032 open (PHYSICAL_CYCLE269_SEVEN_CELL_MAXIMAL_STAR_CYCLE330_NOTE_2026-07-18.md:32-46); incomplete, not a no-go |
| exact character quotient | ATTEMPTED | prove every order from branch injectivity and Pauli inversion characters | succeeds in the Cycle-515 attempt-2 payload (outputs/physical_cycle330_all_order_isometry_bridge_cycle515_attempt2_2026_07_20.log:1) |
| overlapping lower-subgroup checks | PRIOR PARTIAL ATTEMPT / ROUTE-SPECIFIC FAILURE | intersect the two S6 plus sectors | does not produce an order-independent physical code on its full plus sectors (PHYSICAL_CYCLE269_SEVEN_CELL_MAXIMAL_STAR_CYCLE330_NOTE_2026-07-18.md:80-115); route-specific failure only |
| role-only uniform S7 constraint | ATTEMPTED | act on the order flag while leaving the physical ray unchanged | falsified by the Cycle-515 two-role residual-squared 2 witness; corrected transport gives zero (outputs/physical_cycle330_all_order_isometry_bridge_cycle515_attempt2_2026_07_20.log:1) |
| correlated U transport plus Q | ATTEMPTED | transport the physical sign ray with the role and intersect with the code shell | succeeds with common-shell rank 2,459,648, Q rank 4,556,160, and intersection rank 904 in the same payload |
| slot serialization | PRIOR PARTIAL ATTEMPT / OPEN TERMINAL | replace simultaneous order data with an active-edge slot cycle | Cycle 330 succeeds as a bounded compiler schedule (PHYSICAL_CYCLE269_SEVEN_CELL_MAXIMAL_STAR_CYCLE330_NOTE_2026-07-18.md:154-162), but it does not by itself prove the all-order physical shell or physical time |

At least two Cycle-515 constructive families succeed, and three predecessor
families remain only partial/open. Therefore N1 cannot support any negative
closure: any broad claim that no bounded compiler route exists fails N1 and is
not proposed.

### N2 — pairwise wall-independence and collapsed set

For the route from Cycle 515 to a primitive recurrent physical compiler, use:

- W_domain: widen beyond global total N<=2;
- W_dense: synthesize/apply the dense bounded-patch branch-shell operators;
- W_prepare: autonomously prepare and enforce the reference, role, C_i, and Q;
- W_cov: prove proper-cubic covariance of the physical E_pi/A_pi shell;
- W_recur: make adjacent stars and recurrent volume compatible.

| pair | first closes second? | second closes first? | independent? |
|---|---|---|---|
| W_domain / W_dense | no | no | yes |
| W_domain / W_prepare | no | no | yes |
| W_domain / W_cov | no | no | yes |
| W_domain / W_recur | no | no | yes |
| W_dense / W_prepare | no | no | yes |
| W_dense / W_cov | no | no | yes |
| W_dense / W_recur | no | no | yes |
| W_prepare / W_cov | no | no | yes |
| W_prepare / W_recur | no | no | yes |
| W_cov / W_recur | no | no | yes |

No implication was found, so the collapsed wall set remains the five items
above. Time, source/gravity, Born/Records, and prediction bridges are
downstream TOE lanes, not inflated as independent walls of the Cycle-515
bounded theorem.

### N3 — hidden-wall phrase scan

The runner and this note were scanned case-insensitively for: “we assume,”
“by construction,” “as is standard,” “the framework provides,” “bridge
context,” “background,” “naturally,” “obviously,” “standard QFT,”
“registered,” and “canonical.” The final scan returns only these checklist
lines, where the phrases are a non-load-bearing required search inventory;
after excluding that inventory there are zero hits. Earlier hidden
conditions—assumed amplitude normalization, role-only rank inflation,
non-hard RSS wording, unused role states, and unconditional failure
accounting—were promoted into explicit proof predicates or supplied
conditions before attempt 2. No new hidden wall is added, so N2 does not need
another wall.

### N4 — exact residual matching

| cited path and line | witness residual | Cycle-515 residual | match? / disposition |
|---|---|---|---|
| PHYSICAL_CYCLE269_SEVEN_CELL_MAXIMAL_STAR_CYCLE330_NOTE_2026-07-18.md:32-46 | 5,032 S7 physical order Grams unmaterialized | prove all 5,040 order Grams from exact character/injectivity | yes; direct predecessor witness |
| PHYSICAL_CYCLE269_SEVEN_CELL_MAXIMAL_STAR_CYCLE330_NOTE_2026-07-18.md:80-115 | two S6 full-plus checks do not commute/order-independently intersect | correlated physical C_i transport plus Q | no; mechanism context only, dropped as direct witness |
| PHYSICAL_CYCLE269_COMMON_M64_FIXED_SEAM_CYCLE311_NOTE_2026-07-18.md:87-107 | raw one-cell tag collisions and relational f+r repair | global seven-cell branch-row injectivity | no; dependency only, dropped as direct witness |
| PHYSICAL_CYCLE269_OVERLAP_AWARE_TWO_CELL_CYCLE315_NOTE_2026-07-18.md:41-84 | AB and BA endpoint codes differ before local edge-role repair | all-S7 role-correlated transport | no; similar mechanism, different residual, dropped as direct witness |
| PHYSICAL_ROUTE_C_Q6_SYMBOLIC_AXIS_DIAGNOSTIC_CYCLE514_NOTE_2026-07-20.md:17-38 | machine nonzero is not exact symbolic support | forbid machine-zero/cutoff support selection in Cycle 515 | yes for support instrumentation only; not evidence for an order Gram |

After dropping mismatches, Cycle 330 remains the exact witness for the closed
sampling residual. Cycle 514 remains only the exact-support methodology
witness. Neither is cited against covariance, synthesis, or recurrence.

### N5 — rhetoric and resolution audit

| narrow statement | element/site/mode | bounded block | lattice-wide | licensed wording |
|---|---|---|---|---|
| primitive synthesis was not executed | not tested | tested: no synthesis routine is called | not tested | “Cycle 515 does not execute primitive synthesis on this bounded patch” |
| physical proper-cubic covariance is not proved | one-particle logical modes tested; E_pi/D_pi physical action not tested | open | open | “all-order physical E_pi/A_pi covariance remains open” |
| an update count is not a physical-time result | no time observable or calibration tested | no causal-time bridge executed | not tested | “Cycle 515 executes no causal-time bridge” |
| adjacent/recurrent compatibility is not proved | not applicable | one star only | not tested | “adjacent stars and recurrent volume are untested” |

No per-block absence is promoted to a universal per-site, per-mode, or
lattice-wide impossibility.

### N6 — partial-closure and import-retirement paths

| path | status | what it closes or could close |
|---|---|---|
| exact character quotient | Cycle 515 complete on N<=2/L5,L6 | retires literal 5,032-matrix materialization |
| correlated U transport plus Q | Cycle 515 complete on the branch shell | retires the incorrect role-only constraint and rank-904 shortcut |
| dense algebraic A_pi bound | Cycle 515 complete conditionally | proves an intertwiner while exposing later synthesis/application retirement |
| six-slot serialization | Cycle 330 executed | supplies a bounded schedule alternative, not time or recurrent volume |
| affine frame plus fermionic permutation-sign correction | queued next-cycle constructive target | could retire W_cov without an axiom |
| adjacent-star interaction-character quotient | exploratory, not Cycle-515 evidence | could shrink W_recur before the full row census |

This note makes no “no retained primitive supplies this” or “new axiom
required” claim, so the primitive-registry gate is not triggered. Approved
axioms/primitives are neither edited nor silently counted as walls. Every
supplied object follows the import -> bounded theorem -> future
retire-import-audit shape.

### N7 — hostile steelman

A hostile reviewer should reject any covariance or recurrence obstruction:
the Cycle-330 frame machinery already supplies all 24 logical direction
actions, while Cycle 515 supplies exact role-conditioned diagonal transports.
A concrete live construction is to add the cross-cell fermionic
permutation-sign correction on the rank-904 code shell, prove its affine
frame cocycle for all 24 frames at L5 and held L6, and then verify the 576
group products and G_star covariance. Its terminal obligation is finite and
executable. Likewise, the adjacent-star order data may descend to a finite
interaction-character quotient rather than require a global order. These
routes make any broad no-go premature; they are the next campaign targets.

### N8 — cross-cycle echo

| prior wall | later mechanism | relevance now |
|---|---|---|
| Cycle-311 raw cell-role collision (Cycle-311 note:87-107) | local flag plus relational companion (Cycle-311 note:90-111) | keep raw order information as constrained gauge data |
| Cycle-315 endpoint-order mismatch (Cycle-315 note:41-84) | doubled edge role plus relational edge companion (Cycle-315 note:48-84) | a local ordering mismatch need not be a global obstruction |
| Cycle-327 overlapping subgroup checks (Cycle-327 note:84-134) | joint S5 role or four-slot transport (Cycle-327 note:116-194) | enlarge the local role or serialize it |
| Cycle-330 5,032-order sampling wall (Cycle-330 note:32-46) | Cycle-515 injective character theorem | replace exhaustive matrices by an exact quotient proof |

Every similar wall was narrowed or retired constructively. The same
mechanisms are explicitly considered for covariance and adjacent recurrence.

Gate outcomes:

- Cycle-515 result: positive bounded-with-corrected-wall-count theorem;
- broad no-go gate for impossibility, minimum content, shared-substrate
  obstruction, or axiom pressure: FAIL / NOT PROPOSED.

## Next campaign

The immediate next target is a separate exact proper-cubic frame bridge for
the correlated E_pi/A_pi shell, including the cross-cell fermionic
permutation sign rather than assuming the logical frame test lifts.

After that, run the adjacent-maximal-star preflight on the twelve-cell,
eleven-seam union. Its static order dependence should be tested through the
exact anticommutation interaction graph and a lawful local role quotient
before any full physical-row census. The recurrent update must count the
shared seam and shared onsite operations once.

## Evidence hashes

| artifact | SHA-256 |
|---|---|
| Cycle-515 runner | 93afe1600cb3fb8b7844729521b005ce62f957a128a6ffb9493a03a1d9932e96 |
| dry contract | 7ef8b552f8dd08770691c1281b354970641bb75191c5a15e26b1e54078204b56 |
| target attempt 2 | 636d067ddd9284e59f24999666c5110fce425e60a7baa48d714b2a023abab1b1 |
| Cycle-311 amplitude dependency | 4495bf39e1e2661866501e377b8ec1aefff656e261e428fa5b6738f73b49699c |
| Cycle-315 gauge dependency | 52c18f96a1f8db9b79e4d0fba5ff76905170e6a8dc8c3e818fdf69984a1778c3 |
| Cycle-330 runner | 4428d1f73ff315987edabd7f838a1c58414d0a982f0cd28656ddef3bd230d19f |
| Cycle-330 note | 4edb939ca520bc5b148814e8c274e93e16c87e8f639d925db130fdfe16fd3b64 |
