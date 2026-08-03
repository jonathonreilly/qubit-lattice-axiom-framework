# OpenReference cubic recurrent physical-M2 matter compiler — Cycle 870

**Date:** 2026-08-02

**Claim type:** bounded_theorem

**Authority:** none

**Audit:** unset

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

## Direct landed inputs

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
- one clean raw-input/syndrome/work/controller genesis domain with every root
  in `fresh=1, token=spent=0`;
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
| transient companion/global-order chart | bounded partial positive through Cycle 868 | local two-cell action closes, but the supplied global order chart and transient preparation are not the present recurrent code |
| direct Cycle-789 target-chart substitution | bounded partial positive in Cycle 869 | one seam and two-star transport close; nonzero primary/held Gram differences reject only literal substitution into that target chart |
| local OpenReference gauge/auxiliary route | positive here | exact one-shot `E` plus recurrent full `G` on open cubes, with explicit genesis/admission/topology conditions |
| staggered/fixed scheduling | positive for recurrent `G` | independent mod-three and mod-four schedules close without host-volume enumeration; autonomous scheduling of one-time `E` remains open |

No route-specific failure is promoted to constitutional evidence.

## No-go discipline and obstruction disposition

Cycle 870 makes no no-go, minimum-content, shared-obstruction, or axiom-pressure
claim.  The N1 route scan finds live alternatives to autonomous encoder
renewal: the Cycle-719 local refusal, one-marker, and two-rail mechanisms, plus
an untested alternating reset rail, entropy export, and periodic local-gauge
preparation.  Those alternatives prevent negative promotion; they are not
presented as failed routes or as a count of independent walls.

The hostile spent replay establishes only a property of this explicit emitted
word on a second invocation.  It does not constrain every local guard, reset
rail, noncubic controller, periodic sector, or all-volume preparation law.
Prior cell-parity, transient-chart, and target-chart residuals address
different objects and are not cited as evidence about renewal.  The strongest
counter-route is concrete: a token-conditioned double buffer could export the
old epoch locally and alternate rails under a fixed colour rule.  Its terminal
obligations remain injective reset, returned physical routing, proper-cubic
transport, and held-size recurrence.

Accordingly no route-independent obstruction survives this cycle.  The open
items listed above are supplied interfaces for future construction, not negative
physics conclusions.

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

The primary executable is the
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
```

Expected terminal markers are, respectively:

```text
OPENREFERENCE_PHYSICAL_PLACEMENT_PASS
OPENREFERENCE_NATIVE_UPDATE_PASS
OPENREFERENCE_JOINED_CUBE_PASS
INDEPENDENT_OPENREFERENCE_RECONSTRUCTION_PASS
INDEPENDENT_CHRONOLOGICAL_E_EXACTNESS_PASS_WITH_QUALIFICATIONS
INDEPENDENT_FIXED_MOD3_ROUTE_SCHEDULE_PASS
```

Cold package hashes before the citation manifest are:

```text
64b36432670f8a05179d0473e724afee1dfe6327cdd0233d3d788a6b8413c8a2  placement runner
687b22a0bd0fd71fc20e7597443886a4990b49fcef7c80164d5f685210e84237  native-update runner
81109892cf7c435f387fdfd71ea3d7d0b9affe0b301ca0339750db0f91c7a457  joined compiler runner
61adc5c70f116daf58c583c892eb6ecebd4d7d6872e341dc578c22599e4c0a92  independent update checker
d11791df361c719041bba7dbda9bacbfb3a6a0e2790c2f2e71d16eda04c029fe  independent encoder checker
74616bc16fc5329cb9cb6055a1e1f73f045350137d3eb2ecb158552aeb66e998  independent schedule checker
```

All six cold runs pass: the three primary `failures` lists and the three
independent `validation_failures` lists are empty.  The chronological encoder
receipt separately records `verification_status:
pass_with_deletion_and_domain_qualifications` and false per-occurrence deletion
completeness.

Authority remains `none`; audit remains `unset`.  Only the separate audit lane
may apply an audit verdict.
