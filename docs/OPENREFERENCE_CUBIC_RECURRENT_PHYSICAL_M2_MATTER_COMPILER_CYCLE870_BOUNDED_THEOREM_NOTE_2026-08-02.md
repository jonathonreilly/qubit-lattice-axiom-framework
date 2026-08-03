# OpenReference cubic recurrent physical-M2 matter compiler — Cycle 870

**Date:** 2026-08-02

**Claim type:** bounded_theorem

**Authority:** none

**Audit:** unset

**Primary runner:**
[Cycle-870 cold package acceptance](../scripts/frontier_cycle870_openreference_package_acceptance_2026_08_02.py)

**Result scope:** positive recurrent matter update after one supplied
clean-domain encoding invocation

**Frozen target:**
[`OPENREFERENCE_CUBIC_RECURRENT_PHYSICAL_M2_MATTER_COMPILER_CYCLE870_TARGET_SPEC_2026-08-02.md`](work_history/repo/review_feedback/OPENREFERENCE_CUBIC_RECURRENT_PHYSICAL_M2_MATTER_COMPILER_CYCLE870_TARGET_SPEC_2026-08-02.md),
SHA-256
`84f25c8fb2323f67556122898647d31df571529798e5894cded438344bf8ac2a`.

Circuit stages, route microsteps, colours, and controller traversals below are
supplied circuit structure.  None is physical time, duration, rate, energy,
occurrence, or realized history.

## Result

Cycle 870 constructs an executable local-gauge compiler for the framework's
six-mode M64 matter cell on finite open cubic M2 lattices.  It uses one common
physical address map for a clean-domain encoder `E_joined` and for the complete
native matter update

```text
coin/mass -> onsite reverse FSWAP -> every directed seam FSWAP -> contact.
```

On the declared OpenReference code space it proves, for every logical input
vector,

```text
G_physical_exact E_joined = E_joined G_native_exact.
```

The returned routed word `U_routed` is the executable physical operation; its
channel, equivalently its projective class, is the fixed recurrent physical
law on the encoded bank.  The notation
`G_physical_exact = exp(-i phi) U_routed` selects a formal vector
representative so the displayed equation has literal vector equality.  The
unrouted scalar is not a physical gate or observable operation.

The encoder is not autonomous: it is invoked once on a supplied clean
open-cube domain.  No physical admission/reset law prepares or renews that
domain.  This distinction is load bearing.

Within this campaign, this is the first package to join an executable physical
encoder and the complete free-plus-contact update on the same M2 carrier bank
without a global Jordan--Wigner string or host parity service.  It is not a
general fermion-encoding novelty claim.

## Direct supplied inputs

- the [Cycle-219 `beta=-0.3` one-particle coin/mass](work_history/repo/review_feedback/COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md)
  and [Cycle-230 `g=0.37` contact](work_history/repo/review_feedback/SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md)
  fixtures, re-executed on the [Cycle-709 physical seam compiler
  surface](LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md);
- the [Cycle-703 OpenReference/local-Gauss BKSF code, coherent loader, and
  reversible echo/ack semantics](RECURRENT_ENDPOINT_INCIDENCE_PHYSICAL_M2_COMPILER_TOURNAMENT_CYCLE703_NOTE_2026-07-25.md);
- the [Cycle-232 spacing-16 local physical placement](work_history/repo/review_feedback/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_NOTE_2026-07-17.md)
  and returned Manhattan routing primitives; and
- the proper-cubic signed transport conventions from the
  [Cycle-706 OpenReference/PatchGraph equivalence](OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md)
  and [Cycle-707 literal M2 placement/controller](LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md).

Each dynamically consumed runner is byte-pinned by the package.  The
independent verifiers reconstruct the relevant algebra and schedules rather
than importing the joined compiler as an oracle.

## Physical encoding and update

For `N` coarse cells and `E` coarse-cell seams, the encoded carrier has

```text
18N + 3E
```

M2 sites.  The one-time preparation also has `36N` persistent auxiliary M2.
These are not the full physical resource: every route-transit coordinate is
declared as substrate capacity.  Forward/gate/reverse routing restores an
arbitrary transit state, including a state entangled with an external
reference; no clean transit-ancilla premise is used.

The seven encoder stages are

```text
triangle extract
-> triangle correction
-> coarse extract
-> echo correction and acknowledgement
-> bond extract
-> bond correction
-> logical load.
```

The controller expands every root epoch into the literal word

```text
SWAP(fresh, token)
-> token-gated depth-first traversal
-> SWAP(token, spent).
```

`Toffoli` and `CCZ` are decomposed into the declared one- and two-M2
Clifford+T gate language.  The three echo-router permutations are independently
reduced to exact `X/CNOT` words, including an explicit little-endian port-bit
convention.  Every two-site primitive is then compiled into a
nearest-neighbour returned route.

The emitted encoder is tied to the abstract isometry by operator checks, not
by a declared boolean.  The literal extraction macros conjugate each syndrome
`Z` into the signed physical check; the triangle, coarse, and bond correction
incidence maps have zero residual; and the physical constraints plus all
logical `Z` rows have unique-vacuum ranks `180/180` and `648/648`.  The
clean-carrier premise checks those logical `Z` rows explicitly, and every
physical stream-`Z`/coarse-plaquette commutator column equals the same box
incidence column consumed by the controller ANF.  The
controller is executed symbolically over the complete lawful syndrome image
with one Boolean indeterminate per coarse edge.  Its correction and work ANFs
have zero residual and maximum degree one.  Finally the literal signed
controlled-logical-`X` and parity-unload macros prove all `96` L2 and `324` L3
logical-generator identities.  Returned-route label permutations prove that
the routed word conjugates to the same primitive word.

The recurrent update uses exactly the same carrier addresses.  Every
Hermitian native `A/B` generator is lifted through the signed repetition
isometry, preserves the local OpenReference constraints, and is compiled into
an exact Pauli rotation.  Functional calculus and induction through the fixed
factor order establish the displayed all-vector intertwiner without
materializing an exponentially large dense isometry.

## Primary and held exactness

No parameter or placement rule is refitted between the primary `L=2` and held
`L=3` cubes.

| quantity | open L2 | held open L3 |
|---|---:|---:|
| cells / internal seams | 8 / 12 | 27 / 54 |
| logical input qubits | 48 | 162 |
| encoded carrier M2 | 180 | 648 |
| persistent preparation auxiliary M2 | 288 | 972 |
| bounded transit-route substrate M2 | 4,760 | 18,518 |
| total observed declared support M2 | 5,228 | 20,138 |
| `E` primitive gates | 3,889 | 15,473 |
| `E` returned-NN gates | 48,913 | 207,027 |
| `G` rotations | 1,392 | 4,752 |
| `G` primitive gates | 17,048 | 61,038 |
| `G` returned-NN gates | 173,352 | 703,550 |
| combined returned-NN gates | 222,265 | 910,577 |
| maximum observed route distance | 42 | 42 |
| NN / operand / route-return failures | 0 / 0 / 0 | 0 / 0 / 0 |
| emitted-encoder / exact-intertwiner failures | 0 / 0 | 0 / 0 |

The earlier sampled controller tests still exhaust all 32 lawful L2 coarse
syndromes and cover 118 L3 unit/pair cases.  The load-bearing proof is now
stronger: exact algebraic-normal-form execution parameterizes the complete
lawful image using all 12 L2 or 54 L3 coarse-edge variables.  Every output
coefficient residual is zero and no correction polynomial exceeds degree one.
This is a complete basis-and-linearity proof, not a dense
`2^(physical M2)` state-vector run.

Every endpoint and Manhattan path lies inside
`center(owner)+[-25,25]^3`.  Thus `51^3 = 132,651` is a conservative a-priori
total-support capacity bound per coarse cell for the joined `E+G` compiler.
The smaller independent `G` scheduling atlas separately proves that its own
routes fit a radius-9 dense capacity, at most `19^3 = 6,859` sites per coarse
cell.  The two numbers refer to different certified atlases and are not
interchanged.

## Mass, contact, seam, and overlap fixtures

The one-particle coin reconstruction residual is
`9.774239351035397e-16`; the QR off-diagonal residual is
`9.058932439513524e-16`; and maximum proper-cubic coin covariance residual is
zero.  The analytic and compiled rest masses agree as

```text
0.4534056541748852
0.4534056541748851.
```

The complete 64-word local contact fixture has maximum residual
`1.8610729195778454e-15` up to its explicitly tracked global phase.  Every
directed seam FSWAP is a full-space Hermitian involution; the four-rotation
factorization residual is zero.  Minimum active seam-term and seam-rotation
deletion residuals are `0.5590169943749475` and `0.7653668647301795`.

On the literal two-overlapping-maximal-star update fixture, all 12 cells and
15 seams share one global register bank.  The physical constraint bank has
rank 189, every abstract and physical constraint commutator/preservation
failure is zero, the routed update uses 253,320 NN gates with maximum route
distance 33, and the two star views agree on every shared address.  The held
`3x2x2` open box uses the same rule with 20 seams, rank 204, and zero
constraint, placement, route, translation, and 24/576 transport failures.

## Fixed recurrent scheduling

The joined runner supplies a conservative fixed schedule for `G`: 45 complete
factor templates times owner coordinate modulo four, hence 2,880 colours
independent of volume.  Same-colour route-footprint collisions are zero on an
independent held L5 stress, and an analytic owner-envelope separation makes
the conclusion independent of that stress sample.

An independent checker constructs a different mod-three rotation-layer
schedule.  It freezes 180 local rotation types times 27 owner residues:

```text
4,860 fixed macro layers
97,331,220 conservative routed micro-layers.
```

The a-priori caps are rotation weight 72, L1 diameter 70, 431 primitives, and
20,027 routed microsteps per rotation.  No held-size growth is used to choose
them.

| split | L | cells / seams | rotations | macro layers used | same-layer route collisions | overlap-order commutator failures |
|---|---:|---:|---:|---:|---:|---:|
| primary | 2 | 8 / 12 | 1,392 | 1,392 | 0 | 0 / 1,780 |
| primary | 3 | 27 / 54 | 4,752 | 4,752 | 0 | 0 / 8,181 |
| held, no refit | 4 | 64 / 144 | 11,328 | 4,860 | 0 | 0 / 22,224 |
| held, no refit | 5 | 125 / 300 | 22,200 | 4,860 | 0 | 0 / 46,540 |

All 4,900 positions in the distance-1-through-70 symbolic returned-route shape
family are deleted and detected: forward, central, and reverse positions are
covered for every distance.  This is a complete mutation of the bounded route
shape family, not 4,900 mutations sampled from the emitted volume word.
Arbitrary/entangled transit restoration, operand
order, nearest-neighbour routing, and code-safe reorder checks have zero
failures.  A carrier-only negative control is active: it omits 1,624, 6,783,
17,768, and 36,775 required route sites at L2--L5.  This rejects only the
carrier-only resource census; the explicit bounded transit capacity closes
that route, so there is no carrier-only no-go.

The fixed schedule is a circuit implementation schedule.  No schedule counter
or layer index is used as a physical clock.

## Proper-cubic covariance

The joined signed code, carrier/auxiliary coordinate atlas, encoder semantics,
and native update close under all 24 proper-cubic frames and all 576 ordered
products with zero failures.  The independent schedule transports its paths,
type semantics, and mod-three colours through the same 24/576 family with zero
coordinate, residue, unit-step, or direction-semantics failures.

The coframe is supplied and transported.  The claim is code-space covariance
of a transported atlas, not equality of one lab-fixed textual Manhattan word
after a frame reversal.  In particular, a first-rail `Z` representative may
change by the local repetition `ZZ` stabilizer; covariance is exact modulo the
declared code constraint.

## Independent reconstruction and deletion qualification

The independent ordered-action verifier does not import the primary joined
runner.  It reconstructs the one- and two-cell even-CAR action, the physical
repetition lift, free/contact blocks, hostile order witnesses, and 24/576
transport.  Its validation-failure list is empty.

The independent chronological encoder checker likewise imports only the
byte-pinned root atlas and landed dependencies.  It independently emits all
seven stages, reconstructs local matrices using the substrate's little-endian
wire convention, and compares against frozen target metrics.  More
importantly, it independently rebuilds the complete-lawful-domain controller
ANFs, correction incidence maps, unique-vacuum ranks, signed loader identities,
and returned-SWAP conjugation certificate.  Every L2/L3 emitted-isometry
failure field is zero.

It also falsifies a stronger deletion claim.  On the lawful clean domain, 8
L2 and 20 L3 root-child `parent-XOR` Toffolis are redundant.  Exact execution
is unaffected, but per-occurrence deletion completeness is false.  The primary
receipt therefore claims only deletion-class witnesses, not that every listed
semantic occurrence is essential.  Separately, all 15 Toffoli-decomposition
and 17 CCZ-decomposition subgate deletions are active, with minimum residual
`1.5307337294603587`.

The repaired check, loader, router, Toffoli, and CCZ semantic certificates all
have active subgate mutations.  The primary aggregate
check/correction/loader deletion fields are sensitivity censuses;
they are not promoted to an executed deletion of every such gate.  The joined
route checks delete the first forward SWAP of eligible macros, whereas the
independent fixed-schedule checker performs the complete 4,900-position
symbolic route-shape deletion suite.  This distinction is preserved in the
receipts.

## Supplied, derived, and open

Supplied:

- finite open cubic `L=2` or `L=3` boundary, spacing-16 origin, transported
  proper-cubic coframe, incident-edge gauge, and serial `E/G` factor order;
- one arbitrary raw-input bank tensor a clean carrier/syndrome/work/controller
  genesis domain with every root in `fresh=1, token=spent=0`;
- Cycle-703 check, decoder, loader, echo-forest, and one-invocation semantics;
- the OpenReference constraint grammar and target `+1` sector definition;
- Cycle-219 `beta=-0.3` and Cycle-230 `g=0.37`; and
- enough physical transit-substrate capacity for the declared returned routes.

Cycle-870-derived:

- one collision-free physical carrier/register map shared by `E` and `G`;
- an executable seven-stage coherent encoder with literal token-conditioned
  traversal and fresh-to-spent acknowledgement;
- preparation of the local `+1` OpenReference code sector from the supplied
  clean physical domain;
- the exact recurrent coin/reverse/seam/contact update and all-vector
  intertwiner, with a formal vector-representative scalar convention distinct
  from the executable physical channel;
- bounded carrier, persistent-auxiliary, and transit-substrate formulas;
- two independent volume-independent schedules for recurrent `G`;
- exact two-overlapping-star consistency, held-size checks, and 24/576
  covariance; and
- active hostile-order, spent-replay, route-deletion, seam/contact-deletion,
  unlawful-domain, and carrier-only resource controls.

Open, not disproved:

- intrinsic clean genesis, a physical start/occurrence trigger, and autonomous
  boundary/coframe selection;
- a compiled local spent-sector admission guard, reset/renewal, and fault
  repair for repeated encoder invocation;
- a volume-independent parallel controller schedule for the one-time `E`
  word, noncubic controller composition, and periodic Wilson sectors; and
- the downstream Cycle-612 causal-interval, source/gravity, Record, Born, and
  prediction interfaces.

On hostile unguarded replay from the spent sector, the encoder produces 3
token and 3 spent failures at L2 and 8 plus 8 at L3.  That is evidence for the
declared one-invocation domain boundary, not evidence that a local guard or
autonomous preparation law is impossible.

## Constructive-route disposition

| route family | disposition | exact boundary |
|---|---|---|
| seven cell-parity bits | route-specific negative from Cycle 657 | 74,400 of 83,244 branch-term pairs mismatch at L5 and held L6; this rejects that feature set only |
| endpoint-incidence qutrit | exact sign/constraint positive from Cycle 658 | zero errors on all 83,244 L5/L6 cases and exact 24/576 cocycle; coherent extraction and recurrent physical execution were then open |
| transient companion/global-order chart | bounded partial positive through [Cycle 868](TRANSIENT_TWO_CELL_COMPANION_ENCODER_GLOBAL_ORDER_CHART_BOUNDARY_CYCLE868_BOUNDED_THEOREM_NOTE_2026-08-02.md) | local two-cell action closes, but the supplied global order chart and transient preparation are not the present recurrent code |
| direct Cycle-789 target-chart substitution | bounded partial positive in [Cycle 869](BOUNDED_TWO_STAR_BKSF_CYCLE789_TARGET_CHART_BRIDGE_CYCLE869_BOUNDED_THEOREM_NOTE_2026-08-02.md) | one seam and two-star transport close; nonzero primary/held Gram differences reject only literal substitution into that target chart |
| local OpenReference gauge/auxiliary route | positive here | exact one-shot `E` plus recurrent full `G` on open cubes, with explicit genesis/admission/topology conditions |
| staggered/fixed scheduling | positive for recurrent `G` | independent mod-three and mod-four schedules close without host-volume enumeration; autonomous scheduling of one-time `E` remains open |

No route-specific failure is promoted to constitutional evidence.

## No-go discipline and obstruction disposition

Cycle 870 makes no no-go, minimum-content, shared-obstruction, or axiom-pressure
claim.  The full N1--N8 stress test below fails any negative promotion and
therefore leaves the result in its present positive bounded class.

### N1 -- alternative routes

| route against a broad renewal/genesis obstruction | marker | exact disposition |
|---|---|---|
| [Cycle-719 local refusal, one-marker, and two-rail mechanisms](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md) | ATTEMPTED by prior bounded construction | local typed refusal and recurrent rails exist, but their clean genesis and integration with this encoder remain open |
| token-conditioned alternating double buffer | UNTESTED/OPEN | exporting the old epoch and alternating rails under a fixed colour rule could make encoder use recurrent |
| reversible local garbage conveyor / entropy-export rail | UNTESTED/OPEN | a bounded moving garbage register could preserve injectivity while renewing the local work bank |
| periodic-sector local-gauge preparation | UNTESTED/OPEN | local stabilizer preparation plus explicit Wilson-sector handling could extend the open-cube encoder |
| direct endpoint-incidence preparation without the emitted loader word | UNTESTED/OPEN | the Cycle-658 qutrit discriminant leaves a distinct coherent preparation route |
| staggered pump or fault-repair layer on the OpenReference stabilizers | UNTESTED/OPEN | a fixed covariant local layer could prepare or repair the declared code sector without replaying `E` |

Fewer than five alternatives are closed.  N1 therefore forbids a no-go,
minimum-content, shared-obstruction, or axiom-pressure conclusion.  The open
rows are not counted as failed attempts.

### N2 -- collapsed wall set

The raw open-item list collapses to four load-bearing boundary classes.  A
downstream interface is not counted as an additional condition on the
compiler theorem itself.

| wall | exact content |
|---|---|
| `W_G` | supplied clean one-invocation genesis, open-cube boundary, and transported coframe/code sector |
| `W_R` | local admission, spent-sector reset/renewal, and fault repair for reuse of `E` |
| `W_X` | periodic/noncubic extension and a volume-independent parallel controller for the one-time `E` word |
| `W_L` | selection of the numeric coin/contact law compiled by the fixed update |

No member of this collapsed set automatically closes another: `W_G` provides
the first lawful invocation but not renewal; `W_R` does not choose a coframe
or periodic sector; `W_X` does not prepare or renew the code; and `W_L` does
not compile any of those physical resources.  Clean ancillas, start token,
boundary, coframe, code sector, and first-use admission are components of
`W_G`, not extra independent walls.  Reset, renewal, and fault repair are
components of `W_R`.  The Cycle-612/source/Record/Born interfaces are future
consumers outside this compiler theorem, not extra compiler walls.

### N3 -- hidden-wall scan

Before this checklist was inserted, the prescribed phrase scan found no use
of its trigger vocabulary as a load-bearing shortcut.  The quoted trigger
list in this paragraph is itself non-load-bearing review metadata.  The
supplied/derived/open inventory explicitly names
the clean sector, boundary, coframe, numeric parameters, local schedules,
carrier, persistent auxiliary, transit substrate, and one-use admission.

### N4 -- residual matching

| witness | residual actually tested | residual not inferred from it |
|---|---|---|
| Cycle 657 | 74,400/83,244 mismatches for the seven-cell-parity feature set | all bounded fermion encodings |
| Cycle 868 | supplied global-order chart and transient preparation | recurrence of the present OpenReference bank |
| Cycle 869 | nonzero primary/held Gram differences for literal Cycle-789 target-chart substitution | the OpenReference representation used here |
| Cycle 870 hostile replay | 3 token plus 3 spent failures at L2; 8 plus 8 at L3 on a second unguarded `E` invocation | every local guard, reset rail, or preparation law |
| Cycle 870 carrier-only deletion | thousands of required route sites absent from a carrier-only substrate | bounded execution after the explicit transit capacity is retained |

Only the hostile-replay row matches the declared one-invocation boundary.
The other residuals are retained as route diagnostics and are not witnesses
for renewal or genesis.

### N5 -- rhetoric and resolution audit

The all-vector intertwiner and no-global-parity-service statements are tested
on complete lawful open-cube code spaces at L2 and held L3, with recurrent
schedule geometry held through L5 and covariance over all 24 proper-cubic
frames and 576 products.  They are not extended to periodic Wilson sectors,
noncubic regions, arbitrary faulted inputs, or autonomous preparation.  The
spent-replay negative is only about this explicit emitted word at its second
unguarded invocation on L2/L3.  The note does not broaden it to arbitrary
encoders, sites, topologies, schedules, or all-volume preparation laws.

### N6 -- partial-closure paths

The legitimate import-retirement paths remain constructive: integrate a
Cycle-719 refusal/two-rail controller, add a covariant alternating reset rail,
compile periodic stabilizer preparation, or ratify only those boundary/coframe
choices that are genuinely conventions rather than laws.  Approved axioms and
framework primitives are not counted as walls, and no proposed primitive or
axiom is silently promoted.  These paths are implementation or governance
tests until an executable physical law closes them.

### N7 -- steelman

A hostile reviewer should reject any renewal obstruction: a
token-conditioned double buffer can, in principle, move the spent epoch into a
bounded garbage rail, switch to a clean partner bank under a fixed local
colour rule, and run the same exact recurrent update while the first bank is
repaired.  Cycle 719 already demonstrates the relevant refusal, marker, and
two-rail ingredients.  Until injective reset, returned physical routing,
proper-cubic transport, and held-size recurrence are tested for that
counter-route, the one-use boundary is an implementation fact about this word,
not a substrate theorem.

### N8 -- cross-cycle echo

Earlier global-parity and ordered-carrier walls in Cycles 232--257 were
repeatedly narrowed by changing representation; Cycles 703/706 then supplied
the local OpenReference gauge route used here.  Cycle 789's apparent input
collision was repaired by a distinct third bank.  Those echoes show that
genesis, role collision, and global-order residuals in this campaign have often
been retired by additional local carriers or a representation change.  The
same mechanisms remain live against `W_G`, `W_R`, and `W_X`.

**Gate disposition:** `FAIL` for every negative promotion.  The required
repair is already applied: Cycle 870 ships only as a positive bounded theorem
with the collapsed walls above.  Accordingly no route-independent obstruction
survives this cycle, and the open items are supplied interfaces for future
construction rather than negative physics conclusions.

## TOE dependency effect

| campaign ledger coordinate | Cycle-870 effect |
|---|---|
| `C_ref` | unchanged at law level: proper-cubic covariance closes on a supplied transported coframe; intrinsic frame/topology selection remains open |
| `C_num` | materially narrowed: local reference/gauge constraints and `E` derive the `+1` code sector without a global parity service, but physical clean-domain genesis and the numeric coin/contact parameters remain supplied |
| `C_wrap` | fixed volume-independent update schedules close host-volume enumeration for `G`; no schedule variable is time and occurrence remains open |
| `C_int` | mass, reverse, seam, and the supplied contact are one exact recurrent word; interaction selection, rate, and protection remain external |
| `C_local` | major constructive closure: bounded physical carrier, auxiliary constraints, transit capacity, overlapping-star consistency, exact `E G` intertwining, held sizes, and 24/576 covariance; autonomous `E` admission/renewal and periodic topology remain open |
| `C_source` | unchanged: no source identification, reciprocal response, conserved resource, backreaction, or gravity law is derived |

Campaign percentages are intentionally kept out of this theorem surface.
They are project-management estimates rather than theorem outputs.  This note
records only the dependency changes above; audit retention and later lane
scoring must evaluate the executable evidence independently.

## Breakthrough log and novelty boundary

Scientifically interesting positives within the framework:

- the local OpenReference gauge route eliminates the global parity/Jordan--Wigner
  service while preserving the complete supplied matter update;
- the exact all-vector `G_physical E = E G_native` relation now uses one
  literal M2 map, with carrier, persistent auxiliary, and transit substrate
  all counted;
- two independent volume-independent schedules close recurrent physical `G`
  through held L5 without host-volume enumeration; and
- the one-particle mass, seam, contact, overlapping-star, held-size, and
  proper-cubic fixtures survive together without refit.

Scientifically useful negatives/qualifications:

- hostile spent replay proves the present `E` is one-invocation only;
- semantic review exposed and repaired a big-endian convention in the former
  independent encoder checker; the authoritative substrate gate matrices are
  little-endian and are now compared directly;
- 28 root-child parent-XOR Toffolis are redundant on the tested lawful clean
  domains, preventing a false per-occurrence deletion claim; and
- carrier-only execution misses thousands of route sites, while explicit
  bounded substrate capacity repairs the issue and prevents a false no-go.

Local fermion-to-qubit encodings, BKSF/OpenReference-style gauge constructions,
Clifford+T decompositions, and returned SWAP routing are prior art.  Cycle 870
claims no general priority over them.  Its new content is the
framework-specific exact integration and adversarial resource/accounting
closure.  It becomes broader physics only if the remaining autonomous and
cross-lane interfaces close and reach a prediction without discretionary
law choices.

## Reproduction

The audit entry point is the
[cold package-acceptance harness](../scripts/frontier_cycle870_openreference_package_acceptance_2026_08_02.py),
which reruns and hash-checks every source below.  The primary physical
executable is the
[joined recurrent compiler](../scripts/frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02.py).
Its explicit helper/independent runners are the
[physical placement runner](../scripts/frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py),
[native update runner](../scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py),
[independent ordered-update checker](../scripts/frontier_cycle870_openreference_recurrent_update_independent_check_2026_08_02.py),
[independent emitted-encoder checker](../scripts/frontier_cycle870_openreference_chronological_encoder_independent_check_2026_08_02.py),
and [independent fixed-route checker](../scripts/frontier_cycle870_openreference_fixed_route_schedule_independent_check_2026_08_02.py).

From the repository root run, in order:

```bash
python3 -B scripts/frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py
python3 -B scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py
python3 -B scripts/frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02.py
python3 -B scripts/frontier_cycle870_openreference_recurrent_update_independent_check_2026_08_02.py
python3 -B scripts/frontier_cycle870_openreference_chronological_encoder_independent_check_2026_08_02.py
python3 -B scripts/frontier_cycle870_openreference_fixed_route_schedule_independent_check_2026_08_02.py
python3 -B scripts/frontier_cycle870_openreference_package_acceptance_2026_08_02.py
```

Expected terminal markers are, respectively:

```text
OPENREFERENCE_PHYSICAL_PLACEMENT_PASS
OPENREFERENCE_NATIVE_UPDATE_PASS
OPENREFERENCE_JOINED_CUBE_PASS
INDEPENDENT_OPENREFERENCE_RECONSTRUCTION_PASS
INDEPENDENT_CHRONOLOGICAL_E_EXACTNESS_PASS_WITH_QUALIFICATIONS
INDEPENDENT_FIXED_MOD3_ROUTE_SCHEDULE_PASS
CYCLE870_PACKAGE_ACCEPTANCE_PASS
```

Cold package hashes before the citation manifest are:

```text
64b36432670f8a05179d0473e724afee1dfe6327cdd0233d3d788a6b8413c8a2  placement runner
687b22a0bd0fd71fc20e7597443886a4990b49fcef7c80164d5f685210e84237  native-update runner
1b66c061dcb8e0082fd9e7264e78ccbd0f77440c0f517aa93696bde49f78c1bd  joined compiler runner
49d76550de2d1d44adb2703be0ce7d3bc1ebfdc4914c8eee0413b29ad8dc8af9  independent update checker
6ae587e6bd8769e0b6880199d7a95023649464f625211bcb0530c21634a7e3ab  independent encoder checker
7d2a074dda9bf89566895c7df99de32a675e0ba0706304f4db964d2f053cbdbd  independent schedule checker
d69857a709e73dec059fd1de943fb866930c02231dac9f191e65f72e214900d9  package acceptance harness
```

All six component cold runs and the package-acceptance harness pass: the three
primary `failures` lists and the three independent `validation_failures` lists
are empty.  The chronological encoder
receipt separately records `verification_status:
pass_with_deletion_and_domain_qualifications` and false per-occurrence deletion
completeness.

Authority remains `none`; audit remains `unset`.  Only the separate audit lane
may apply an audit verdict.
