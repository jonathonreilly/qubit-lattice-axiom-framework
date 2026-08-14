# Translation-uniform dependence law on an adjacent two-centre `Z^3` patch

Date: 2026-08-11
Cycle: 983
Claim type: `bounded_theorem`
Audit-status authority: independent audit lane only
Effective status: pipeline-derived only after independent audit ratification and dependency closure

## Trace gate

```yaml
trace_class: direct_blocker_closure
reachability_to_target: closes
target_claim_id: null
target_blocker_text: "determine whether one neighbour-dependence rule has the same class structure at every target of a multi-star patch, or identify an exact overlap obstruction"
source_of_blocker_text: user_goal
artifact_role: theorem
next_trace_action: "independent audit of the bounded adjacent-two-centre patch packet"
```

## Status fields

```yaml
claim_id: cycle983_translation_uniform_two_star_patch
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: bounded-support
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "finite two-target theorem; no branch-local retained-grade proposal"
claim_type_reason: "exact exhaustive classification of one explicitly capped relative rule on both targets of the named finite patch"
audit_required_before_effective_retained: true
bare_retained_allowed: false
audit_status_authority: independent audit lane only
negative_assertion_classes: [bounded_with_named_walls]
packet_primary_runner: scripts/frontier_cycle983_translation_uniform_two_star_patch_2026_08_11.py
packet_helper_runner: scripts/frontier_cycle983_translation_uniform_two_star_patch_independent_check_2026_08_11.py
packet_helper_claim_scope: cycle983_translation_uniform_two_star_patch
```

## Packet binding

```yaml
hard_landing_packet_helper_mapping:
  translation_uniform_two_star_patch_cycle983_bounded_theorem_note_2026-08-11:
    - scripts/frontier_cycle983_translation_uniform_two_star_patch_independent_check_2026_08_11.py
```

The helper mapping is a hard landing condition: the restricted independent-
audit packet must contain the refutation checker. This note records no audit
verdict; audit-status authority remains with the independent audit lane.

Current-main [Cycle 980](WITNESS_ORBIT_MULTIPLICITY_CYCLE980_BOUNDED_THEOREM_NOTE_2026-08-11.md)
already owns the one-centre 21-witness `6/12/3` classification and the `J`
separator. Cycle 983 does not claim those values as new. It independently
reconstructs them at both translated centres and adds only the bounded
two-star pointwise-covariance, hosting, and overlap-consistency result.

## Exact bounded theorem

Let

```text
P2x = { A=(0,0,0), B=(1,0,0) }
Omega = union over t in P2x of ({t} union {t+d : ||d||_1=1}).
```

At each target `t` in `P2x`, apply the same relative 23-program rule schema:

```text
I;
X(t);
CNOT(t+d -> t) for all six signed unit directions d;
TOF({t+d,t+e} -> t) for every unordered pair d != e.
```

On this exact target domain and hosting support, both target sites have 21
neighbour-dependence witnesses. At each target, the proper cubic action gives
classes of sizes `6`, `12`, and `3`, with stabilizers `4`, `2`, and `8`; the
separator

```text
J = || sum of centre-relative control vectors ||^2
```

takes values `1`, `2`, and `0`, respectively. Translation by `(1,0,0)` maps
the entire relative rule table at `A` to the table at `B`; the primary checks
the pointwise covariance equation on all 2944 descriptor/input cases. The two closed
stars' bindings, geometric/semantic relation labels, class label, `J` value,
and nearest-neighbour path agree on their shared sites and pair.

Therefore the executable verdict is

```text
TRANSLATION_UNIFORM_AT_PATCH_SCOPE
named patch: P2x_ADJACENT_TWO_CENTRE_CLOSED_STAR_PATCH
```

This is a theorem only at the named two-target finite-patch scope. It is not
an infinite-lattice translation-uniformity theorem.

## A_PATCH_CONSTRUCTION

### Geometry and site count

The target domain has the two adjacent sites `A=(0,0,0)` and `B=(1,0,0)`.
Each target receives its complete closed radius-one `Z^3` star:

```text
S_A = {A} union {A+d : ||d||_1=1},
S_B = {B} union {B+d : ||d||_1=1}.
```

Each star has seven sites. Their intersection and union are

```text
S_A intersection S_B = {A,B},
|S_A intersection S_B| = 2,
|Omega| = |S_A union S_B| = 7 + 7 - 2 = 12.
```

Thus the named patch has two target sites and twelve hosting-support sites.
The other ten points of `Omega` are explicit support-only halo: this theorem
does not silently count them as additional tested targets.

The construction is smallest in both relevant senses. Two is the smallest
number of distinct stars exceeding one. For two distinct closed unit stars in
`Z^3`, nonempty intersection requires centre separation at most two, and the
intersection contains at most two sites. Hence their union has at least
`14-2=12` sites. Adjacent centres attain that bound. The primary also exhausts
all 24 nonzero relative offsets in the `L1<=2` overlap range and obtains the
same minimum. The minimizer is not unique (a diagonal separation of `L1=2`
also has a two-site intersection); `P2x` is the chosen connected-centre
minimizer, not a uniqueness claim.

### Program family and cap

- Site menu: `{0,1}`.
- Target domain: both sites of `P2x`.
- Support for each target: its complete six-neighbour closed star in `Omega`.
- Words: identity or one landed semantic gate.
- Semantic boundary: the 23 rows are the pairwise-distinct semantic quotient
  with distinct, unordered TOF controls. The linked constructors also accept
  repeated controls, and exchanged TOF controls are distinct gate objects;
  the runner checks that repeated-control TOF reduces to CNOT action and that
  exchanged-control TOFs have identical Boolean action. Thus 23 is not the
  complete constructor-object population.
- Relative family per target: `I`, `X`, six target-local CNOTs, and fifteen
  target-local TOFs.
- Family size: `1 + 1 + 6 + C(6,2) = 23` per target.
- Multi-star family: `2 * 23 = 46` site-program instances.
- Truth-table cap: both target bits, every one of `2^6` neighbour conditions,
  and every neighbour-bit edge comparison for every descriptor at both sites.
- Routing cap: every expanded primitive of all 46 instances; no sampling.

This is one relative rule schema with one relative-family digest. It is not a
pair of independently chosen or fitted site rules.

The two embedded `K_7` semantic pair shadows have one shared pair, hence 41
distinct global semantic pairs. The two six-edge geometric stars share their
central edge, hence 11 distinct global `Z^3` star edges. These union counts are
reconstructed rather than conflated.

## B_UNIFORMITY_TEST

### Per-site census

| target | complete star | programs | target evaluations | witnesses | non-witnesses | routed |
|---|---|---:|---:|---:|---:|---|
| `A=(0,0,0)` | yes | 23 | 2944 | 21 | 2 (`I`, `X`) | yes |
| `B=(1,0,0)` | yes | 23 | 2944 | 21 | 2 (`I`, `X`) | yes |

At both targets, landed basis-state semantics agree with the independent
descriptor-level Boolean evaluator on every evaluation. The relative witness
lists and normalized structure digests are identical.

More strongly, the primary embeds a global Boolean assignment on `S_A`,
translates the assignment and every operand by `tau=(1,0,0)`, and exhausts

```text
R_(t+tau)(tau.assignment; descriptor)
  = R_t(assignment; descriptor)
```

for all `23 * 2 * 2^6 = 2944` cases. The pointwise translation-covariance
failure count is zero. This equation, not equality of aggregate witness counts,
is the executable one-rule test.

### Per-site class assignment

The following complete relative assignment holds separately at `A` and `B`;
global witnesses at `B` are the `(1,0,0)` translates of those at `A`.

| class at each target | relative controls | witnesses per target | stabilizer | `J` |
|---|---|---:|---:|---:|
| CNOT | `+x`, `-x`, `+y`, `-y`, `+z`, `-z` | 6 | 4 | 1 |
| perpendicular-control TOF | `(+x,+y)`, `(+x,-y)`, `(+x,+z)`, `(+x,-z)`, `(-x,+y)`, `(-x,-y)`, `(-x,+z)`, `(-x,-z)`, `(+y,+z)`, `(+y,-z)`, `(-y,+z)`, `(-y,-z)` | 12 | 2 | 2 |
| opposite-control TOF | `(+x,-x)`, `(+y,-y)`, `(+z,-z)` | 3 | 8 | 0 |

Each orbit-stabilizer product is 24. The primary enumerates all 24
determinant-`+1` signed-permutation rotations; it does not hard-code the three
orbit sizes.

### Host result

Per target, the landed router expands 232 primitives into 292 nearest-
neighbour gates. Across both targets the totals are 464 and 584. The maximum
logical-pair route distance is two, at most three sites are touched by any
word, and all non-nearest-neighbour, operand-order, and route-return failure
counts are zero. Hosting is word-by-word under the pinned Cycle-719 route-
blueprint contract; no simultaneous schedule is inferred.

## C_OVERLAP_CONSISTENCY

### Shared-site agreement table

Both star charts bind a shared coordinate to the same global Boolean site
variable. Different local roles are the expected result of changing centre,
not a conflicting value assignment.

| global site | star `A` local role | star `B` local role | binding agreement |
|---|---|---|---|
| `(0,0,0)` | centre `C` (wire 0) | neighbour `-x` (wire 2) | exact: `q_(0,0,0)` |
| `(1,0,0)` | neighbour `+x` (wire 1) | centre `C` (wire 0) | exact: `q_(1,0,0)` |

### Shared-pair agreement table

The induced semantic-pair intersection contains exactly one unordered pair.

| global pair | star `A` wires | star `B` wires | semantic pair | `Z^3` edge | class at each target | `J` | routed path |
|---|---|---|---|---|---|---:|---|
| `{(0,0,0),(1,0,0)}` | `(0,1)` | `(2,0)` | yes in both | yes in both | `CNOT(+x->C)` / `CNOT(-x->C)` | 1 in both | same edge, reversed orientation |

The two target-specific equations on this pair are

```text
at A: q_(0,0,0)' = q_(0,0,0) XOR q_(1,0,0),
at B: q_(1,0,0)' = q_(1,0,0) XOR q_(0,0,0).
```

They are distinct target components, not two claims about the same output
component. Under centre/target exchange their complete shared-edge table is

| `q_A` | `q_B` | star `A` target output | star `B` target output |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |

Both witnesses change on 64 neighbour-bit edge comparisons. Thus the pointwise
table, witness strength, class, `J`, relation labels, and route agree—not only
their aggregate counts. Both target equations belong to the one relative schema. The primary's exact
overlap classification is
`exact_agreement_on_all_shared_sites_and_pairs`; no overlap obstruction was
found at this scope.

## D_VERDICT

```text
TRANSLATION_UNIFORM_AT_PATCH_SCOPE
P2x_ADJACENT_TWO_CENTRE_CLOSED_STAR_PATCH
```

What is established is one translation-covariant rule schema, with the same
witness set, class structure, separator values, and overlap bindings at both
targets of `P2x`.

What is not established:

- the same result for target sites outside `P2x`;
- an infinite allocation of `M_2(C)` sites over every point of `Z^3`;
- a simultaneous global execution or conflict-free schedule of the 23
  alternative local words;
- a translation-uniform admissibility probability or selection rule; or
- equality of semantic operand availability and geometric adjacency.

The ten support-only halo points are not counterexamples and are not additional
targets: their complete stars would require a larger declared support. Extending
the asserted target domain therefore remains a separate finite-patch step.

## E_CONTROLS

### Inputs and imports

| item | class | load-bearing role | disposition |
|---|---|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | zero-input structural | supplies `Z^3` nearest-neighbour geometry, translations, and proper cubic rotations | byte and Git-blob pinned |
| [Cycle 719 controller theorem](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md) and pinned core | one computed lattice input | supplies landed basis-state semantics and Manhattan routing | immutable commit, SHA-256, and Git blob checked |
| [Cycle 980 witness theorem](WITNESS_ORBIT_MULTIPLICITY_CYCLE980_BOUNDED_THEOREM_NOTE_2026-08-11.md) | current-main bounded provenance | already owns the one-centre `6/12/3` and `J` result | cited but neither imported nor executed; reconstructed here |
| `P2x` and `Omega` | explicit finite boundary condition | fixes the two targets and twelve-site host support | declared exactly above |
| 23-program relative family | explicit finite boundary condition | fixes the target-local alphabet and word-length cap | exhausted at both targets |

The pinned core is commit
`39c74017b870c27c804e3992f2a11e90336476b2`, path
[`frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py),
SHA-256
`0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4`.
No observed value, fit, selector, probability weight, normalization rule,
literature value, new axiom, or new framework primitive is load-bearing.
The cited Cycle 719 and Cycle 980 notes are absent from the primary's literal
input set and are neither imported nor executed; only the immutable Cycle 719
core is loaded.

### Current Record boundary

The pinned current minimal-axiom memo is checked against the simplified Record
axiom: records form; a present record locks one admissible local possibility;
no site carries more than one record; records are permanent; only records are
readable; readout depends on record content alone; and an unrecorded site
cannot be read. No Record property enters the patch geometry, Boolean rule,
router, group action, or overlap test. Finite additivity, scalar `I`, and
`I(empty)=0` are not used and are not current Record content.

### Proof obligations

1. **Patch obligation — closed at the declared cap.** Construct both closed
   stars, their intersection and union, and independently reconcile the
   twelve-site minimum.
2. **Rule obligation — closed at the declared cap.** Use one relative family
   digest and translate every one of its 23 descriptors from `A` to `B`.
3. **Per-site witness obligation — closed at the declared cap.** Exhaust all
   5888 target evaluations and all neighbour-bit edge comparisons.
4. **Class obligation — closed at the declared cap.** Enumerate the proper
   cubic action, orbits, stabilizers, and `J` values independently at both
   targets.
5. **Overlap obligation — closed at the declared cap.** Reconcile both shared
   site bindings and the single shared semantic/geometric pair, including the
   reversed nearest-neighbour paths and distinct target components.
6. **Infinite-extension obligation — open and outside this theorem.** No
   induction, compatible exhaustion, global allocation, simultaneous schedule,
   or probability/selection rule is supplied.

The strongest result is exactly the finite two-target theorem; no prose step
turns obligation 6 into a consequence of obligations 1–5.

### Refutation specification

The primary's five checks gate only construction and bookkeeping. A coherent
`OBSTRUCTED` or `NOT_HOSTABLE` finding passes those gates when its data and
verdict reconcile.

The independent checker imports and executes neither the primary nor the
Cycle-719 core. It byte-pins the primary source and receipt, binds the complete
canonical primary cache, and independently reconstructs:

- the two-centre/twelve-support geometry and minimality census;
- the two complete 23-program Boolean families and both 21-witness lists;
- all 24 proper cubic actions, orbit sizes, stabilizers, and `J` values;
- the 232/292 per-target routing arithmetic;
- both shared-site bindings and the one shared-pair table; and
- the bounded verdict and false infinite-scope flag.

Science agreement is reported data rather than an integrity condition. The
checker rejects fourteen single-field corruptions covering target/support
counts, family instances, a per-site witness count, orbit size, hostability,
uniformity classification, pointwise translation covariance, overlap counts/path agreement, verdict, infinite
scope, source binding, and cached stdout. It separately constructs coherent
synthetic `OBSTRUCTED` and `NOT_HOSTABLE` receipts; both pass the same
bookkeeping validator. Thus an obstruction is not penalized by the controls.

## No-Go Discipline: N1-N8

The negative surface is limited to the absence of an overlap obstruction on
the declared two-star patch and the minimum twelve-site union among two
distinct overlapping closed unit stars. It is not an infinite-lattice no-go.

### N1 — alternative routes

Five routes were executed. The primary performs the full relative-offset
census for overlapping closed unit stars; the checker repeats it separately.
Pointwise covariance is tested on all 2,944 translated descriptor/input cases,
not inferred from equal witness counts. Both shared site bindings and the
single shared semantic pair are reconstructed globally. A reversed-path check
attacks routing disagreement on the shared edge. Finally, coherent synthetic
`OBSTRUCTED` and `NOT_HOSTABLE` receipts are accepted by the same bookkeeping
gate, so a positive outcome is not built into PASS.

### N2 — wall independence

The two-target wall, twelve-site hosting wall, 23-program semantic-quotient
wall, word-by-word routing wall, and no-simultaneous-schedule wall are kept
separate. Exhausting one does not close another. In particular, exact
translation covariance of a supplied relative schema does not supply an
infinite target allocation or a global update schedule.

### N3 — hidden walls

The selected adjacent centres, complete radius-one stars, pairwise-distinct
controls, unordered TOF controls, Boolean site menu, one-word cap, proper
cubic group, and centre-relative convention are explicit. Repeated operands,
constructor-object multiplicity, longer words, larger supports, support-halo
targets, asynchronous/simultaneous composition, and admissibility
probabilities are outside the theorem.

### N4 — residual matching

The offset census supports only the stated minimum-union claim. The 2,944
truth checks support only translation covariance between `A` and `B`. The two
site rows and one pair row support only overlap consistency on
`S_A intersection S_B`. Zero failures on these residuals are not used to
exclude an obstruction on a larger patch or under simultaneous execution.

### N5 — rhetoric audit

The primary cache carries substantive `per_element:`, `per_site:`,
`per_mode:`, `per_block:`, and `lattice_wide:` lines. The verdict always says
`AT_PATCH_SCOPE`; the note names the two tested targets and ten untested halo
sites, and explicitly says it is not an infinite-lattice
translation-uniformity theorem.

### N6 — partial-closure paths

A third target with a complete hosted star can be added and checked without a
new axiom. Finite connected patches can be exhausted in increasing size. A
simultaneous schedule needs a separately declared composition rule. An
infinite result would need a compatible exhaustion or an induction/locality
theorem. These are open continuations rather than impossibility claims.

### N7 — steelman

A larger patch may expose a support conflict absent here; two alternative
local words may be individually routable but not simultaneously schedulable;
and an admissibility or probability law may fail to be translation uniform
even though this supplied Boolean rule schema is covariant. None of those
possibilities is excluded.

### N8 — cross-cycle echo

Cycle 980 remains the current-main provenance for the one-centre witness
classes and `J`. Cycle 983 reconstructs those quantities only to test the new
two-centre relation. It does not convert Cycle 980's finite semantic quotient
into a lattice-wide dynamics claim or treat the current Record axiom as a
source of translation uniformity.

### Artifacts and reproduction

Primary:

- [`frontier_cycle983_translation_uniform_two_star_patch_2026_08_11.py`](../scripts/frontier_cycle983_translation_uniform_two_star_patch_2026_08_11.py)
- [`translation_uniform_two_star_patch_cycle983_receipt_2026_08_11.json`](../outputs/translation_uniform_two_star_patch_cycle983_receipt_2026_08_11.json)
- [`frontier_cycle983_translation_uniform_two_star_patch_2026_08_11.txt`](../logs/runner-cache/frontier_cycle983_translation_uniform_two_star_patch_2026_08_11.txt)

Independent refutation checker:

- [`frontier_cycle983_translation_uniform_two_star_patch_independent_check_2026_08_11.py`](../scripts/frontier_cycle983_translation_uniform_two_star_patch_independent_check_2026_08_11.py)
- [`translation_uniform_two_star_patch_cycle983_independent_check_receipt_2026_08_11.json`](../outputs/translation_uniform_two_star_patch_cycle983_independent_check_receipt_2026_08_11.json)
- [`frontier_cycle983_translation_uniform_two_star_patch_independent_check_2026_08_11.txt`](../logs/runner-cache/frontier_cycle983_translation_uniform_two_star_patch_independent_check_2026_08_11.txt)

```bash
python3 scripts/cached_runner_output.py --refresh --timeout-sec 1400 scripts/frontier_cycle983_translation_uniform_two_star_patch_2026_08_11.py
python3 scripts/cached_runner_output.py --refresh --timeout-sec 300 scripts/frontier_cycle983_translation_uniform_two_star_patch_independent_check_2026_08_11.py
```

Both canonical caches pin runner SHA-256, declared inputs, timeout, exit status,
and stdout. Both runners replay deterministically, keep stdout below 6000
bytes, end in `TOTAL: PASS=5 FAIL=0`, and write machine-readable receipts.
