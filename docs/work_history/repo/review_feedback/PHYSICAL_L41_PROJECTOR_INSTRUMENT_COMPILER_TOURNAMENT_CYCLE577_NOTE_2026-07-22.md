# Physical L41 projector/instrument compiler tournament — Cycle 577

Date: 2026-07-22

Authority: none

Audit: unset

Authority remains none. Audit remains unset. This cycle changes no axiom,
foundation, Qualification, primitive, registry, policy, queue, audit status,
or PR surface.

Runner:

`scripts/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.py`

## Result up front

Cycle 577 closes the representation gap named by Cycle 574 at finite
instrument resolution. The original Cycle-41 alphabet consists of eleven
nonorthogonal, pairwise-distinct rank-one projectors in one `M_2`, not eleven
orthogonal role labels. This tournament keeps that operator geometry and the
Cycle-41 `P/E/X/Z` three-site candidate instrument intact through three
independent bounded physical-M2 routes:

1. **Route A — direct local channel.** The original one-M2 projectors are
   represented identically and the exact reset/CZ/projective instrument is a
   bounded three-M2 CPTP map. This is positive at channel level, but a local
   nonunitary channel primitive or an unshown discarded environment remains
   supplied.
2. **Route B — priority gauge/environment/Naimark route.** Each logical M2 is
   isometrically encoded by `|0> -> |00>`, `|1> -> |11>` in a two-M2 block
   with local `Z tensor Z=+1` constraint. Projectors preserve their complete
   Gram matrix. Three encoded fresh `X+` reset blocks receive the old inputs
   by SWAP; three pointer M2 and three named dephasing-environment M2 realize
   the exact instrument. Old input, pointer coherence, and every spent carrier
   remain explicit. The runner materializes the single `262144 x 8` output
   isometry for all 18 physical M2 and obtains both branch and nonselective
   reduced channels from that object. The precise CPTP/instrument intertwiner
   is exact on the declared code space.
3. **Route C — staggered sequential dilation.** Three fresh `X+` reset M2,
   three pointers, three dephasing carriers, and a nine-rail in-state head
   perform three resets, two CZs, and the `X/Z/Z` instrument in eight explicit
   phases. The head is an actual nine-dimensional one-excitation code factor
   in every code-coordinate isometry column, not a Python cursor. An explicit
   `H9:C^9 -> (C^2)^tensor9` maps those coordinates to the nine physical head
   M2, yielding a sparse `2^21 x 8` retained-environment isometry. No full
   `2^21 x 2^21` unitary extension is constructed. Phase is carried in state;
   the schedule is not time.

The four Cycle-41 `1/4` candidate weights are pinned prior-law data. Their
matching branch traces are instrument diagnostics, not derived Born
probabilities. No route uses them to select an actual branch, assert an
occurrence, or create a framework Record.

Contract spelling: the eleven nonorthogonal projectors are retained. The
candidate weights are pinned prior-law data. They are not derived Born
probabilities and do not select an actual branch.

Exact firewall phrase: not derived Born probabilities.

Route B is the strongest constructive result because it simultaneously
preserves the original nonorthogonal operator geometry, gives locally
checkable auxiliary code conditions, exposes the complete reset and pointer environment, and supplies
an exact code-space instrument intertwiner. Its positivity is conditional on
fresh encoded-plus and blank dephasing resources. It does not derive their
genesis, renewal, entropy sink, autonomous recurrence, or physical selection.

All three routes are finite positive constructions. The refreshed N1 gate has
only three qualifying attempted families; prior open families cannot be
misreported as ruled out. The artifact is therefore demoted to a positive
partial construction with explicit residuals. Broad no-go, minimum-content,
shared-obstruction, and axiom-pressure conclusions are all **DO NOT SHIP**.

## Exact Cycle-41 object retained

The role dictionary is

```text
H1/H0 = P(+/-Y)
B1/B0 = P(+/-(X+Y)/sqrt(2))
D1/D0 = P(+/-(X+Z)/sqrt(2))
C     = P((X+Y+Z)/sqrt(3))
X+/X- = P(+/-X)
Z0/Z1 = P(+/-Z).
```

Every value is a rank-one projector in the same one-site `M_2`. The runner
tests all eleven ranks, all 55 unordered distinctions, and the full
`Tr(P_i P_j)` Gram matrix. Therefore it does not repeat Cycle 574's bounded
one-hot label recoding and call that the same projector identity.

On three sites, Cycle 41 applies:

```text
P: rho -> |+++><+++| Tr(rho)
E: CZ_left,middle CZ_middle,right
X/Z/Z instrument: P_X(sign) P_Z(left) P_Z(right).
```

Equivalently, with reset Kraus operators

```text
A_0=|+><0|, A_1=|+><1|,
```

the branch maps have Kraus family

```text
K_(h,k) = M_h CZ (A_k1 tensor A_k2 tensor A_k3).
```

The runner verifies

```text
sum_(h,k) K_(h,k)^dagger K_(h,k) = I_8.
```

Four algebraic histories have zero trace and the four Cycle-41-supported
histories have trace `1/4`. This equality is pinned candidate-law agreement,
not an amplitude-to-actuality or frequency theorem.

## Route A — direct local CPTP channel

The local isometry is the identity `E_A:C^2 -> C^2`; therefore every role
projector is literally unchanged. For two independent density fixtures the
runner evaluates every branch CP map and compares it to the semantic
reset/cluster/projector branch. It also sums all branches and checks trace
preservation.

The route uses three data M2. Its apparent minimal overhead is not a
minimum-content theorem: it has taken the noninjective CPTP map as an allowed
local primitive. If the framework instead requires globally reversible
physical-M2 dynamics, the missing reset and dephasing environment is hidden
and Route A is incomplete at that stronger boundary.

## Route B — local gauge/environment/Naimark compiler

### Faithful local code

Define the two-M2 isometry

```text
W|0> = |00>,   W|1> = |11>,
Q = W W^dagger,
Z tensor Z = +1 on ran(Q).
```

For every Cycle-41 role projector `P_r`, the physical representative is

```text
P_r^physical = W P_r W^dagger.
```

The runner verifies

```text
W^dagger P_r^physical W = P_r
Tr(P_r^physical P_s^physical) = Tr(P_r P_s)
(I-Q) P_r^physical Q = 0
```

for all roles and pairs. Thus nonorthogonal overlaps are faithfully retained.
The code does not claim that an arbitrary state outside `Q` is lawful.

### Reset and Naimark resources

For the three-site instrument Route B inventories 18 physical M2:

| carrier | M2 | status after one invocation |
|---|---:|---|
| encoded system | 6 | branch-conditioned encoded data |
| encoded fresh `X+` reset environment | 6 | spent block retaining the complete old input |
| outcome pointer | 3 | coherent branch label before reduction |
| dephasing environment | 3 | duplicate branch label retaining discarded coherence |

There are six local parity constraints: three on the active encoded system and
three on the reset environment. They are supplied, locally checkable code-space
conditions; no penalty/check dynamics that enforces them is constructed. The
exact retained-environment map is an isometry. It is materialized as eight
columns in the full 18-M2 output space:

```text
V_B : C^8 -> C^(2^18),
axes = encoded system(64) x encoded old-input environment(64)
       x pointer(8) x dephasing copy(8).
```

Only 64 amplitudes are nonzero on this candidate input family, but no output
axis is omitted. `V_B^dagger V_B=I_8` is tested directly. Projecting the
pointer in this same tensor and tracing the encoded reset and dephasing axes
gives, branch by branch,

```text
E_B Phi_h(rho) = Phi_h^physical E_B(rho).
```

This is the declared precise CPTP/instrument intertwiner. The system reset
trace distance changes `1 -> 0`, while the spent environment retains distance
one. No information vanishes globally.

This route constructs the full bounded-block output isometry and its exact
branch/nonselective reductions. It does **not** construct an exact spatial gate
layout, a two-/three-M2 gate decomposition of that isometry, or a full unitary
extension on all `2^18` inputs. Those are separate open implementation
obligations and are not hidden inside the word “Naimark.”

The dephasing environment is also load-bearing for the declared
quantum-classical pointer channel. Omitting it leaves nonzero off-diagonal
pointer/system blocks. That coherent Naimark dilation still defines
conditional branches when projected, but is not silently called a classical
outcome or Record.

The exact fresh low-entropy auxiliary bill per invocation is twelve physical
M2: three two-M2 encoded-plus reset blocks, three zero pointer M2, and three
zero dephasing M2. The finite dilation does not derive reusable reset entropy,
bath renewal, temperature, or an irreversible sink.

## Route C — staggered in-state-phase instrument

Route C has 21 physical M2 at the declared three-site resolution:

- three data M2;
- three fresh `X+` reset-environment M2;
- three pointer M2;
- three dephasing-environment M2; and
- a nine-M2 one-hot phase head.

Thus eighteen auxiliary M2 begin in supplied low-entropy states: three plus
reset carriers, six zero pointer/dephasing carriers, and the nine-rail head.

The head first appears as a nine-dimensional one-excitation code-coordinate
axis inside the materialized `36864 x 8` isometry (`4096`
data/environment/pointer states times `9` head coordinates). The runner then
constructs

```text
H9 |r> = |00...010...00> in (C^2)^tensor9
```

with the one on physical head rail `r`. `H9^dagger H9=I9`. Sparse row
embedding gives the actual physical output shape `2^21 x 8`; its Gram residual
is checked without allocating a dense 2,097,152-row matrix. Thus `36864 x 8`
is explicitly the code-coordinate shape, while `2^21 x 8` is the physical-M2
shape. Exactly-one head occupancy is a supplied lawful-domain condition. The
controlled operations and head SWAPs preserve it, but no local enforcement or
repair dynamics is constructed. The head authorizes these phases:

```text
0 reset-left
1 reset-middle
2 reset-right
3 CZ-left-middle
4 CZ-middle-right
5 measure-X-middle
6 measure-Z-left
7 measure-Z-right
8 terminal.
```

Each phase operation is the block-diagonal unitary that applies its base SWAP,
CZ, H, or CNOT only when the corresponding physical head rail is occupied.
The base gates have support at most two M2, and the head-rail SWAP advance has
support two. A head-controlled two-M2 base gate has logical support three M2.
No exact two-M2 decomposition of those controlled gates is supplied here, so
Cycle 577 claims bounded support three—not literal support two—for Route C.
The runner constructs all eight input columns, obtains a retained-environment
isometry, and compares it to the direct sum of exact Cycle-41 branch vectors, old-input
environment, pointer word, dephasing word, and terminal physical head.
Deleting the phase-2 head advance leaves every column on nonterminal rail 2
and changes the isometry by norm `4`; it does not rely on a host exception.
Deleting one CZ changes the branch channel.

The terminal head, reset history, pointer, and dephasing word are retained.
There is no anonymous work debris. An inverse can restore the supplied input
and fresh blocks, but then erases the output episode. The in-state head removes
an unrecorded internal cursor for this bounded invocation. It does not derive
an autonomous rule for clearing/reseeding the head or choosing the next
front, and eight phases are not eight units of physical time.

## Exact tests and residual classes

The frozen runner requires:

- exact hashes for Cycle 41 and the relevant committed instrument/Born/Record
  shores through Cycles 280, 288, 430, 483, 488, 502, 565, 571, and 574;
- all eleven role ranks, distinctions, direct/gauge intertwiners, and Gram
  overlaps;
- Route-A completeness, branch square, and trace preservation;
- Route-B code-space CPTP/instrument square, isometry, local gauge constraints,
  materialized `2^18 x 8` output, exact branch/nonselective reductions, zero
  code leakage, reset-distance export, and named environment ledger;
- Route-C exact retained-environment-isometry equality, eight branch-channel
  squares, explicit `H9` physical embedding, supplied exactly-one head domain,
  in-state terminal phase, and bounded phase-controlled support three;
- train L3 and held L6 spectator invariance;
- deletion of reset Kraus, supported pointer branch, retained reset
  environment, dephasing environment, head advance, and CZ;
- malformed density and noncode gauge-state refusal;
- all24 route covariance and all576 ordered products for all eleven roles;
- full supplied / derived / open and N1–N8 inventories.

## Supplied / derived / open

### Supplied

1. the exact Cycle-41 eleven-projector dictionary, `P/E/X/Z` candidate law,
   four supported histories, and four `1/4` trace targets;
2. the finite three-site boundary and held L6 spectator extension;
3. Route A's local CPTP primitive or implicit discarded environment;
4. Route B's two-M2 code, local parity convention, six fresh encoded `X+`
   carriers, blank pointers, blank dephasing carriers, and supplied code-space
   membership; no enforcement dynamics or gate/layout decomposition;
5. Route C's reset/pointer/dephasing carriers, explicit `H9` physical head
   embedding, exactly-one lawful-domain condition, initial phase, and
   eight-phase candidate-law order;
6. finite low-entropy capacity, noiseless gates, routing chart, and the
   Cycle-41 site-only proper-cubic presentation;
7. the trace functional as candidate-instrument diagnostics, without an
   actual-member or empirical interpretation.

### Derived

1. faithful direct and two-M2 gauge representations of all eleven projectors,
   including every overlap;
2. exact direct CPTP and branch maps;
3. an exact local gauge/Naimark/Stinespring code-space intertwiner;
4. explicit export of reset input and pointer coherence into named carriers;
5. an exact staggered retained-environment isometry with in-state phase;
6. four supported and four null trace diagnostics matching Cycle 41;
7. held L6 spectator invariance, deletion signatures, lawful-domain refusal,
   and all24/all576 covariance.

### Open

1. selection of Cycle 41 as the actual framework law;
2. one actual branch, occurrence, framework Record formation, readability,
   permanence, and realized history;
3. derivation/calibration of the trace targets as Born probabilities or
   empirical frequencies;
4. genesis, renewal, entropy export, temperature, and reentry law for reset
   and dephasing environments;
5. autonomous repeated phase invocation, asynchronous boundary epoch and
   absence finalization, collision-safe volume, noise, and arbitrary horizon;
6. composition with the full Cycle-563/569 interacting matter update without
   the noninjective reset destroying its matter distinction;
7. metric time/rate/lapse, energy/stress/source, backreaction, gravity,
   continuum/Lorentz/CPT, authority, or audit promotion.
8. local enforcement/repair of Route B parity and Route C exactly-one head
   domains, Route B gate/layout decomposition, and full physical unitary
   extensions of the bounded isometries.

## Route dispositions

| route | disposition | strongest residual |
|---|---|---|
| A | positive exact channel-level compiler | CPTP primitive/discarded environment supplied |
| B | strongest positive conditional bounded-block physical-M2 isometry | fresh resources, enforcement, exact gate/layout decomposition, renewal, selection, and autonomous recurrence open |
| C | positive exact staggered retained-environment isometry with sparse physical `H9` embedding | exactly-one domain, initial head/order, local enforcement, full unitary extension, and repeated-invocation law supplied/open |

No route-specific limitation is constitutional evidence.

## TOE dependency ledger

| wall | Cycle-577 movement | residual |
|---|---|---|
| `C_ref` | original one-M2 projector relations now have faithful direct and local-gauge physical representations | law, boundary, code-frame, and fresh-environment genesis supplied |
| `C_num` | exact finite CP/isometry/intertwiner, Gram, held, deletion, and covariance residuals | trace targets remain candidate data; no calibration, noisy-volume, or continuum theorem |
| `C_wrap` | coherent pointer and dephasing outputs expose an exact instrument boundary | no actual branch, Record admission, permanence, or realized history |
| `C_int` | old input is retained in Route B/C environment instead of destroyed globally | reduced system still performs Cycle-41 reset; no integration with the full interacting matter compiler |
| `C_local` | all routes have bounded constant overhead; B has locally checkable parity conditions; C has explicit sparse `H9` embedding and bounded controlled support three | code enforcement, Route-B gate/layout synthesis, Route-C two-M2 decomposition/full unitary extension, routing, phase/bath renewal, and collision-safe autonomous volume remain open |
| `C_source` | reset/dephasing carriers and their spent outputs are counted | no entropy-renewal, energy/stress/source, temperature, backreaction, or gravity law |

The global evidence coordinates carried forward through Cycle 576 are shown
below on both the repo-wide and strict-physical-M2 surfaces. Parentheses give
the requested 0–5 equivalent by division by twenty. Cycle 577 does not regrade
those coordinates: it adds exact bounded-block representation evidence but
closes none of the global lane-defining residuals.

| lane | repo-wide evidence | strict-M2 evidence | Cycle-577 delta |
|---|---:|---:|---|
| operational quantum / Records | `96/100 (4.80/5)` | `93/100 (4.65/5)` | faithful finite projector/instrument compiler; no actual branch or framework Record |
| causal time | `79/100 (3.95/5)` | `76/100 (3.80/5)` | in-state phase for one invocation only; no metric duration or recurrent clock |
| inertia / matter | `94/100 (4.70/5)` | `97/100 (4.85/5)` | old input retained globally; full matter-compatible composition remains open |
| gravity / source | `82/100 (4.10/5)` | `77/100 (3.85/5)` | resource carriers counted; no energy/stress/source response |
| Born / probability | `84/100 (4.20/5)` | `73/100 (3.65/5)` | pinned trace targets reproduced conditionally; no selection or calibration law |

These are evidence-planning coordinates, not probabilities, audit grades, or
constitutional status. The unchanged coordinates avoid presenting Cycle
577's narrower local readiness as a global lane regression.

## No-Go Discipline gate

The current `origin/main` no-go skill was fetched and read. The gate result is
**FAIL at N1**, and that is the honest acceptance result: this note ships only
a positive partial construction and refuses every negative promotion.

### N1 — normalized alternative families

Families are normalized by `(object/formulation, mechanism/invariant,
terminal obligation)`. Open prior instances do not count as ruled out.

| family | object / formulation | mechanism / invariant | terminal obligation | honesty / evidence |
|---|---|---|---|---|
| direct local CPTP channel | three-M2 density channel with 64 branch/reset Kraus operators | Kraus completeness and exact branch CP maps | reversible realization plus one framework-owned actual branch/Record | **ATTEMPTED** here; exact channel still emits the complete conditional family ([runner](../../../scripts/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.py)) |
| local gauge + retained Naimark environment | two-M2 `ZZ=+1` code and sparse `2^18 x 8` output | code projector, pointer/dephasing sectors, old-input export | renewable resources plus non-trace-driven actuality/Record map | **ATTEMPTED** here; every branch/environment remains ([runner](../../../scripts/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.py)) |
| staggered physical head | `H9` exactly-one code embedded in sparse `2^21 x 8` output | phase-controlled gates, head SWAPs, retained environments | local head enforcement, autonomous repetition, actual Record | **ATTEMPTED** here; one bounded episode only ([runner](../../../scripts/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.py)) |
| repeated-instrument product | tensor-product conditional history and finite corpus | Stinespring completeness and product traces | actual history plus Record/frequency law | **UNTESTED / NOT COUNTED**; Cycle 430 leaves sampler/occurrence/history reopen obligations ([Cycle 430](REPEATED_PHYSICAL_INSTRUMENT_CONDITIONAL_HISTORY_FREQUENCY_CYCLE430_NOTE_2026-07-19.md)) |
| supplied-bath FORM channel | many-to-one reduced reset/repair channel with retained bath | old-state export, spent ledger, finite repair | coherent member, stationary renewal, unconditional Record | **UNTESTED / NOT COUNTED**; Cycle 483 leaves concrete reopen routes ([Cycle 483](PHYSICAL_RESET_ENVIRONMENT_RECORD_OCCURRENCE_CYCLE483_NOTE_2026-07-19.md)) |
| hard-core/rotor formation | finite one-winner apparatus and deterministic rotor | exclusion, reversible conveyor, response grading | actual member and Record site/content binding | **UNTESTED / NOT COUNTED**; Cycle 502 leaves both terminal mechanisms open ([Cycle 502](PHYSICAL_KRAUS_RECORD_LOCK_CANDIDATE_GRADE_FORMATION_TOURNAMENT_CYCLE502_NOTE_2026-07-20.md)) |
| finite Naimark menu + binder | effect-menu isometry, pointer sectors, independent member-law cell | effect completeness, coherent retention, conditional binding | menu/member genesis and non-erasing actuality/Record owner | **UNTESTED / NOT COUNTED**; Cycle 565 leaves reopen routes ([Cycle 565](PHYSICAL_BORN_MENU_COMPILER_OCCURRENCE_INTERFACE_CYCLE565_NOTE_2026-07-21.md)) |

Only three normalized families qualify as `ATTEMPTED` or `RULED OUT BY PRIOR`,
below the required five. N1 therefore **FAILS**. None of the four cited prior
instances closes its normalized family.

### N2 — collapsed wall-independence audit

Use `W_L` law selection, `W_R` reset/dephasing resources, `W_A` actual
branch/Record, `W_Q` autonomous recurrence/volume, `W_M` matter-compatible
nonerasure, and `W_B` mathematical trace-to-Born identification. Empirical
frequency calibration is collapsed as a downstream composite of `W_A` and
`W_B`, not counted as a seventh independent wall.

| pair | close first => second? evidence | close second => first? evidence | collapse |
|---|---|---|---|
| `W_L,W_R` | no—law choice creates no low-entropy carriers | no—renewal chooses no law | retain both |
| `W_L,W_A` | no—law choice supplies no Record map | no—one occurrence identifies no law | retain both |
| `W_L,W_Q` | no—finite rule choice proves no recurrence | no—a scheduler may run several candidate laws | retain both |
| `W_L,W_M` | no—choice does not repair reset erasure | no—injectivity chooses no law | retain both |
| `W_L,W_B` | no—choice does not identify trace | no—Born identification chooses no dynamics | retain both |
| `W_R,W_A` | no—capacity is not actuality | no—one Record replenishes no carrier | retain both |
| `W_R,W_Q` | no—fresh carriers give no scheduler | no—recurrence can exhaust a reservoir | retain both |
| `W_R,W_M` | no—renewal does not prevent erasure | no—matter preservation generates no bath | retain both |
| `W_R,W_B` | no—renewal does not identify trace | no—Born identification supplies no resource | retain both |
| `W_A,W_Q` | no—one Record gives no repeated schedule | no—QCA may remain coherent | retain both |
| `W_A,W_M` | no—typing does not repair reset | no—matter preservation chooses no branch | retain both |
| `W_A,W_B` | no—one Record proves no trace theorem | no—weights produce no actual member | retain both |
| `W_Q,W_M` | no—recurrence may erase matter | no—matter dynamics need not tile | retain both |
| `W_Q,W_B` | no—QCA recurrence identifies no trace law | no—Born identification supplies no QCA | retain both |
| `W_M,W_B` | no—injectivity identifies no trace law | no—Born identification preserves no matter | retain both |

All fifteen collapsed pairs are bidirectionally independent.

### N3 — hidden-wall scan

The runner scans the refreshed phrase list. Standardness language occurs only
in the prior-art attribution and is non-load-bearing. The projector dictionary,
supplied Route-B parity domain, absent Route-B gate/layout decomposition, reset
inputs/outputs, pointer/dephasing carriers, supplied Route-C exactly-one domain,
absent local head enforcement, phase order, trace functional, law table, frame
chart, blanks, and held boundary are explicit.

### N4 — exact residual matching

| witness | witness residual | residual claimed closed | match / use |
|---|---|---|---|
| [Cycle 41](COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md) | eleven nonorthogonal projectors plus instrument | faithful bounded representation | **yes** |
| [Cycle 574](PHYSICAL_L41_CANDIDATE_LAW_INTEGRATION_TOURNAMENT_CYCLE574_NOTE_2026-07-22.md) | one-hot recode omitted overlaps/instrument | faithful overlaps/intertwiner | **yes** |
| [Cycle 483](PHYSICAL_RESET_ENVIRONMENT_RECORD_OCCURRENCE_CYCLE483_NOTE_2026-07-19.md) | reset state must be exported | finite retained reset export | **yes** |
| [Cycle 280](SAME_CODE_INSTRUMENT_BRIDGE_SYNTHESIS_CYCLE280_NOTE_2026-07-17.md) | instrument is not occurrence/Record | projector representation | **no**; boundary only, dropped as closure witness |
| [Cycle 430](REPEATED_PHYSICAL_INSTRUMENT_CONDITIONAL_HISTORY_FREQUENCY_CYCLE430_NOTE_2026-07-19.md) | product traces do not select history | one-use compiler | **no**; dropped as closure witness |
| [Cycle 565](PHYSICAL_BORN_MENU_COMPILER_OCCURRENCE_INTERFACE_CYCLE565_NOTE_2026-07-21.md) | generic finite Naimark menu | specific Cycle-41 compiler | **no**; analogous only, dropped |

Three exact witnesses remain after dropping nonmatches.

### N5 — rhetoric and resolution

| phrase | tested | untested | permitted wording |
|---|---|---|---|
| trace is not a derived Born law | eight L3 branches; held L6 spectators | repeated lattice/empirical calibration | these finite traces are diagnostics only |
| pointer is not framework Record | one reversible bounded output | framework admission/all-future permanence | Cycle-577 outputs are not promoted to Records |
| head phase is not physical time | one eight-phase episode | metric/lattice-wide calibration | no duration/rate is assigned here |
| carrier count is not energy/source | no source functional on this block | future calibrated map | Cycle 577 makes no source identification |

No lattice-wide negative is inferred from a per-block control.

### N6 — partial-closure and import-retirement paths

| path | status | could close |
|---|---|---|
| Route-B bounded gate/layout synthesis | open proof obligation, not new axiom | isometry versus local-layout distinction |
| local check/penalty dynamics for `H9` | open constructive route | supplied head domain |
| Cycle483-style fresh/spent stream | finite export retained; stationary renewal open | resource import |
| independent Record formation law | physics/owner obligation; definition relabeling forbidden | pointer versus Record wall |

No “new axiom required” claim is made.

### N7 — hostile steelman

A concrete collision-safe reversible QCA could stream locally prepared
encoded-plus/zero carriers through Route-B blocks, export spent carriers,
transport an `H9`-like phase excitation, preserve interacting matter, and
couple an independent non-trace-driven occurrence field to one pointer sector.
Its terminal obligation is to construct one bounded-neighborhood unitary
recurrence for arbitrary finite volume, prove stationary fresh/spent balance,
and derive a framework-owned unique Record without reading branch trace.
Cycles 483 and 565 are finite precedents but do not close this obligation. The
mechanism is untested and actionable, so a broad no-go is premature.

### N8 — cross-cycle echo

| prior wall | retired? | mechanism | application |
|---|---|---|---|
| Cycle574 faithful projector gap | yes at one finite block | Gram-preserving two-M2 isometry | retired without axiom edit |
| Cycle483 hidden reset/discard | finite export yes; renewal no | retain old/spent carriers | used in B/C; renewal remains target |
| Cycle565 bounded Naimark menu | compilation yes; selector no | explicit pointer/resource ledger | specialized here |
| Cycle280/288 instrument-to-occurrence | no | later candidate FORM/typing only | enforces conditional wording |

N1 status: **FAIL**.

Artifact status: **POSITIVE PARTIAL CONSTRUCTION WITH EXPLICIT RESIDUALS**.

Broad impossibility: **FAIL / DO NOT SHIP**.

Minimum-content theorem: **FAIL / DO NOT SHIP**.

Shared-obstruction claim: **DO NOT SHIP**.

Axiom-pressure claim: **DO NOT SHIP**.

## Interpretation firewall

- The Cycle-41 four equal traces are candidate weights, not derived Born
  probabilities, sampled frequencies, or actual members.
- A Naimark pointer and its dephasing environment do not select an actual
  branch.
- A coherent or quantum-classical instrument output is not a framework Record
  or realized history.
- System reset is not global erasure: the old input remains in the spent
  environment. Finite fresh blocks are not reusable reset entropy.
- The gauge code is an explicit two-M2 representation, not a new axiom or a
  proof of minimum physical content.
- Head position, phase number, circuit depth, and gate count are not time,
  duration, lapse, or rates.
- Kraus operators and generator entries are not rates.
- Branch trace, M2 count, and environment count are not energy, work, stress,
  source, temperature, or gravity.

## Prior-art and novelty boundary

Stinespring dilation, Naimark dilation, repetition/subsystem codes, projective
measurement circuits, SWAP reset, environment-induced dephasing, unary heads,
and reversible circuit compilation are standard. No general novelty or
priority claim is made.

The repo-local result is the exact-pinned, executable joining of Cycle 41's
specific eleven-projector geometry and branch instrument to three bounded
physical-M2 representations, including a locally constrained two-M2 gauge
code and a fully itemized reset/dephasing environment, while maintaining the
repository's occurrence/Record/Born/resource firewalls.

## Cold verification

Frozen command:

```bash
/usr/bin/time -l python3 -u scripts/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.py
```

Frozen receipt:

- runner SHA-256:
  `93bf1fa2859289b13037bfe7882cce86732e9377ed8b60e56c3bd55ebc0ce74f`;
- transcript SHA-256:
  `0ba0c1b5d6223df39faa5f3a30275f858201bd0d354de9b0b8b1dd6021ecd21a`;
- `RESULT pass=11 fail=0`;
- eleven role rank/distinction failures `0`, all 55 pair distinctions pass,
  direct/gauge intertwiner maximum `0`, Gram residual `0`, gauge leakage `0`;
- Route-A completeness residual `1.2560739669470201e-15`, branch-square and
  trace failures `0`;
- Route-B materialized full-isometry shape `(262144,8)` with 64 nonzero
  amplitudes; dilation residual `1.88411095042053e-15`, physical
  code-completeness residual `1.2560739669470201e-15`, branch/nonselective
  reduction, intertwiner, and leakage failures all `0`; reset trace-distance
  ledger `system 1 -> 0`, `spent environment 0 -> 1`; this is a full bounded
  output isometry, while gate/layout synthesis and a full unitary extension
  are both reported `false`;
- Route-C `H9` physical embedding shape `(512,9)`, code-coordinate isometry
  shape `(36864,8)`, sparse physical output shape `(2097152,8)`, and 64
  nonzero amplitudes; `H9` residual `0` and retained-environment/physical
  sparse isometry residual `2.198129442157285e-15`; explicit-sequence residual
  `4.440926982597988e-16`, branch failures `0`, and all terminal physical
  heads at phase `8`; the exactly-one domain is supplied and not locally
  enforced; deleted phase-2 advance leaves all heads at rail `2` and changes
  the isometry by `3.9999999999999996`; maximum phase-controlled support is
  three M2, with no exact two-M2 decomposition or full unitary extension
  supplied;
- held L6 branch failures `0`, gauge residual `0`, staggered residual
  `6.217248937900877e-15`, four malformed densities and five malformed
  staggered auxiliary states refused;
- reset deletion residual `1.0`, retained trace after supported-branch deletion
  `0.7499999999999997`, missing reset-environment isometry residual
  `7.483314773547877`, coherent cross block without dephasing environment
  `0.2499999999999999`, and deleted-CZ branch shift `0.24999999999999994`;
- 72 all24 route tests and 6,336 all576 projector-role tests with zero frame,
  mapped-code-edge, or group failures;
- N1 has seven normalized families but only three qualifying attempts, so N1
  is `FAIL`; N2 contains all 15 bidirectional pairs among the six collapsed
  walls; the artifact is a positive partial construction and broad no-go,
  minimum-content, shared-obstruction, and axiom-pressure claims are all
  `DO_NOT_SHIP`;
- external elapsed `0.25 s`, maximum resident set size `159,612,928` bytes,
  peak memory footprint `146,702,912` bytes;
- internal scientific-section elapsed `0.1525968339992687 s`, reported RSS
  `159,596,544` bytes;
- authority `none`; audit `unset`.

The run is below 360 seconds and 3 GiB. The transcript is frozen evidence;
this receipt-only note edit does not alter the runner or transcript.
