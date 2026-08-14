# Each finite event weighting has a product extension with the XOR kernel — Cycle 974

Date: 2026-08-10

Authority: none

Audit: unset; independent audit still required

On the stipulated finite record-write event model and the declared radius-one,
word-length-at-most-one basis-state family, each of the five finite-measure
candidates admits an exact product extension whose site conditional is the
covariant XOR kernel. This is a theorem about the declared extension criterion,
not a physical compatibility test or an event-weight selector.

Claim type: bounded_theorem

Primary runner:

- [`frontier_cycle974_covariant_law_weight_compatibility_2026_08_10.py`](../scripts/frontier_cycle974_covariant_law_weight_compatibility_2026_08_10.py)

Independent refutation checker:

- [`frontier_cycle974_compatibility_independent_check_2026_08_10.py`](../scripts/frontier_cycle974_compatibility_independent_check_2026_08_10.py)

Pinned caches:

- [`frontier_cycle974_covariant_law_weight_compatibility_2026_08_10.txt`](../logs/runner-cache/frontier_cycle974_covariant_law_weight_compatibility_2026_08_10.txt)
- [`frontier_cycle974_compatibility_independent_check_2026_08_10.txt`](../logs/runner-cache/frontier_cycle974_compatibility_independent_check_2026_08_10.txt)

Receipts:

- [`covariant_law_weight_compatibility_cycle974_receipt_2026_08_10.json`](../outputs/covariant_law_weight_compatibility_cycle974_receipt_2026_08_10.json)
- [`covariant_law_weight_compatibility_cycle974_independent_check_receipt_2026_08_10.json`](../outputs/covariant_law_weight_compatibility_cycle974_independent_check_receipt_2026_08_10.json)

Self-contained cited-primary provenance:

- [`cycle974_cited_primary_provenance_2026_08_10.json`](../outputs/cycle974_cited_primary_provenance_2026_08_10.json)

Constitutional effect: none. No axiom, primitive, registry, policy, audit
result, effective-status surface, probability postulate, or Born rule is added
or edited.

## Result in one sentence

`M1_COUNTING`, `M2_PER_WORLD_UNIFORM`, `M3_OCCUPATION_WEIGHTED`,
`M4_FORMATION_LIFETIME`, and `M5_FORMATION_MOMENT` all **SURVIVE**; none is
**EXCLUDED**. The candidate count stays five: reduction `0/5 = 0%`.

## Provenance boundary

The primary reads the three cited notes as text and parses the three cited
runners as AST at exact git objects. It never imports or executes them:

| Role | Commit | Note path / blob | Runner path / blob |
|---|---|---|---|
| event space and five weightings | `84e62249a0c4d3b043c0698464b693f70a25cb12` | `docs/EVENT_SPACE_GROUNDWORK_CYCLE878_SUPPORT_NOTE_2026-07-28.md` / `17c07f4d6d3dc07c81828827f25ab575dc7b722d` | `scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py` / `769f65e51ea2e896af750e92592a421464c3c0e1` |
| two-site dependence witness (provenance only) | `591b4364071e82de78ef6230dbeb00107688f9e2` | `docs/INTER_SITE_GATE_CYCLE970_BOUNDED_THEOREM_NOTE_2026-08-09.md` / `c32f8dc4a355d43cbcf81988579202b3a1465f2e` | `scripts/frontier_cycle970_inter_site_gate_2026_08_09.py` / `bebf2def543ed701f676203d98f994dab1ebcca2` |
| covariant dependence law (provenance only) | `621bc7521a1a314df700a2d8d09988beee1c4ad7` | `docs/COVARIANT_DEPENDENCE_LAW_CYCLE972_BOUNDED_THEOREM_NOTE_2026-08-09.md` / `f20755a0d83f8bd06f606b0c0c3f7a6e58ce4c35` | `scripts/frontier_cycle972_covariant_dependence_law_2026_08_09.py` / `71afd3b3e39e174d50fb9b07a79d5a715e93af1a` |

The event model is the stipulated model of the
[`Cycle-878 event-space authority`](EVENT_SPACE_GROUNDWORK_CYCLE878_SUPPORT_NOTE_2026-07-28.md),
rebuilt here from the landed
[`Cycle-719 controller authority`](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md)
through its
[`controller core`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py)
at SHA-256 `0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4`.
The [axiom memo](MINIMAL_AXIOMS_2026-06-29.md) is SHA-pinned text, not
executable input.

## A_REBUILD

The primary independently scans the landed base trajectory without executing
the Cycle-878 model. It reconstructs 92,260 record-write atoms: 164 `F`,
47,872 `B0`, and 44,224 `B1`, across 748 worlds. The `(world, tag, ordinal)`
atoms are singletons. The five defining data are:

| Candidate | Rebuilt definition | Positive events | Zero-weight events |
|---|---|---:|---:|
| `M1_COUNTING` | `w(e)=1` | 92,260 | 0 |
| `M2_PER_WORLD_UNIFORM` | `a(w)=1`, spread uniformly across the events in world `w` | 92,260 | 0 |
| `M3_OCCUPATION_WEIGHTED` | `a(w)=` clean-dwell occupation count, spread uniformly within `w` | 19,172 | 73,088 |
| `M4_FORMATION_LIFETIME` | `a(w)=B-f(w)+1` for formed worlds and zero otherwise, spread uniformly within `w` | 19,172 | 73,088 |
| `M5_FORMATION_MOMENT` | `a(w)=f(w)` for formed worlds and zero otherwise, spread uniformly within `w` | 16,076 | 76,184 |

Here `B=180,224` is the scanned boundary count and `f(w)` is the first
formation boundary. Each vector is nonnegative and has strictly positive
total mass.

The dependence-law rebuild enumerates 20 declared words, both target inputs,
and all 64 neighbour conditions. Six incoming CNOT words, 12 word/input rows,
and 384 one-bit edge pairs vary. All 768 witness truth-table rows satisfy

```text
y = x XOR n_d.
```

There are zero failures in 61,440 proper-rotation comparisons and 15,360
unit-translation comparisons. The six directions form one word-law class;
the fixed inputs form two state-resolved classes. Uniform averaging over `x`
gives zero changes in 3,840 one-bit marginal comparisons.

Finding verbatim:

```text
A_REBUILD PASS :: events=92260; candidates={"M1_COUNTING":{"definition":"w(e)=1","positive":92260,"zeros":0},"M2_PER_WORLD_UNIFORM":{"definition":"world score a(w)=1; uniform within each event-bearing world","positive":92260,"zeros":0},"M3_OCCUPATION_WEIGHTED":{"definition":"a(w)=clean-dwell occupation count; uniform within world","positive":19172,"zeros":73088},"M4_FORMATION_LIFETIME":{"definition":"a(w)=boundaries-formation_moment(w)+1 if formed, else 0; uniform within world","positive":19172,"zeros":73088},"M5_FORMATION_MOMENT":{"definition":"a(w)=formation_moment(w) if formed, else 0; uniform within world","positive":16076,"zeros":76184}}; dependence={"canonical_pair":{"condition_n_d_0":[0,0,0,0,0,0],"condition_n_d_1":[1,0,0,0,0,0],"distribution_n_d_0":[1,0],"distribution_n_d_1":[0,1],"fixed_target_input":0},"changed_edge_pairs":384,"dependent_word_input_rows":12,"family_words":20,"law":"y=x XOR n_d","neighbour_conditions":64,"rotation_count":24,"rotation_failures":[],"rotation_semantic_comparisons":61440,"state_resolved_class_count":2,"translation_failures":[],"translation_semantic_comparisons":15360,"uniform_target_input_changed_pairs":0,"uniform_target_input_edge_pairs":3840,"witness_word_count":6,"word_law_class_count":1,"xor_failures":[],"xor_truth_table_comparisons":768}
```

## B_COMPATIBILITY_TEST — the declared load-bearing criterion

The criterion is the **existential joint-extension criterion**:

> A normalized event weighting `p_i` survives exactly when there exists a
> joint distribution `P_i(e,x,n,y)` whose event marginal is `p_i(e)` and
> whose site conditional is `P_i(y|x,n)=1{y=x XOR n_d}` for every fixed-input
> radius-one configuration. Exclude it on a nonnegativity or normalization
> failure, an event-marginal mismatch, or the first conditional configuration
> mismatch.

The mechanical witness is

```text
P_i(e,x,n,y) = p_i(e) q(x,n) 1{y=x XOR n_d},
q(x,n) = 1/128.
```

The carrier `q` is part of the existence witness, not a physical state
weighting: every strictly positive normalized `q` gives the same result. Exact
summation gives

```text
sum_(x,n,y) P_i(e,x,n,y) = p_i(e),
P_i(y|x,n) = 1{y=x XOR n_d}.
```

The canonical separating configuration pair, common to every survivor, is

```text
x=0, n=(0,0,0,0,0,0): D(y|x,n)=[1,0]
x=0, n=(1,0,0,0,0,0): D(y|x,n)=[0,1].
```

There is no disagreeing quantity for any of the five. Exact per-weighting
extension witnesses are:

| Candidate | Verdict | Positive event atom | `p_i(e)` | `P_i(e,x,n,y_forced)` at either canonical configuration | First disagreement |
|---|---|---|---|---|---|
| `M1_COUNTING` | **SURVIVES** | `(176,0,F,0)` | `1/92260` | `1/11809280` | none |
| `M2_PER_WORLD_UNIFORM` | **SURVIVES** | `(176,0,F,0)` | `8320/802813440` | `1/12350976` | none |
| `M3_OCCUPATION_WEIGHTED` | **SURVIVES** | `(176,0,F,0)` | `86328320/897595870080` | `1297/1726145904` | none |
| `M4_FORMATION_LIFETIME` | **SURVIVES** | `(176,0,F,0)` | `1499472000/29530480287360` | `60075/151438360448` | none |
| `M5_FORMATION_MOMENT` | **SURVIVES** | `(327,1,B0,0)` | `4426240/2192349344640` | `19/1204587552` | none |

The 73,088/73,088/76,184 zero-weight diagnostics do not contradict this
criterion. The XOR law fixes a conditional distribution on local
configurations; it does not assert positive mass for every record-write atom.
A rule demanding `p_i(e)>0` for every realized event would exclude
`M3_OCCUPATION_WEIGHTED`, `M4_FORMATION_LIFETIME`, and
`M5_FORMATION_MOMENT`, but that would be an additional event-support premise,
not a consequence of covariance, uniqueness, or XOR dependence. No such
premise is added here.

Finding verbatim:

```text
B_COMPATIBILITY_TEST PASS :: criterion=existential joint-extension criterion: a normalized event weighting p_i survives iff there exists P_i(e,x,n,y) with event marginal p_i and conditional P_i(y|x,n)=1{y=x XOR n_d} on every fixed-input radius-one configuration; mechanically use P_i=p_i(e)*q(x,n)*1{y=x XOR n_d}, q=1/128.  Exclude only on nonnegative/normalization failure, event-marginal mismatch, or a first conditional configuration mismatch.; verdicts={"M1_COUNTING":"SURVIVES","M2_PER_WORLD_UNIFORM":"SURVIVES","M3_OCCUPATION_WEIGHTED":"SURVIVES","M4_FORMATION_LIFETIME":"SURVIVES","M5_FORMATION_MOMENT":"SURVIVES"}; witness_pair={"condition_n_d_0":[0,0,0,0,0,0],"condition_n_d_1":[1,0,0,0,0,0],"distribution_n_d_0":[1,0],"distribution_n_d_1":[0,1],"fixed_target_input":0}
```

## Exact target and proof-obligation graph

Target statement: for each of the five rebuilt normalized event weightings
`p_i` on the stipulated finite event space, construct a joint distribution
whose event marginal is `p_i` and whose local conditional is the rebuilt XOR
kernel on every declared fixed-input neighbour configuration.

| Obligation | Disposition |
|---|---|
| Rebuild each `p_i` as a nonnegative vector with positive finite total | proved here by the landed-substrate event scan; independently recomputed cell-for-cell by normalized-vector digest |
| Rebuild the local kernel and its declared covariance/class count | proved here by exhaustive primary and independent Boolean enumerations |
| Show the product construction is nonnegative and normalized | exact finite sum: `sum_e p_i(e)=1`, `sum_(x,n) q(x,n)=1`, and the indicator has one allowed `y` |
| Recover the event marginal | exact finite sum over `(x,n,y)` gives multiplicative factor `1` |
| Recover the XOR conditional at every declared configuration | exact numerator/denominator cancellation, checked in 256 scalar entries per weighting |
| Cover degenerate inputs | zero-total, negative-entry, missing-configuration, and XNOR corruptions are actively rejected; zero event weights remain allowed because they do not make any `(x,n)` conditioning event null |

No terminal lemma is imported or target-equivalent: the joint distribution is
given explicitly. The strongest missing statement is outside this theorem's
target—a derivation that identifies record-write atoms with local
configurations strongly enough to select an event marginal.

## C_SELECTION_STATUS

The conditional kernel and the event marginal live on different factors in the
declared product construction. With no supplied map from local `(x,n,y)`
configurations through Record to the 92,260 event atoms, this criterion contains
no term that can compare the five event marginals.

All five survive this criterion: the reported candidate count is `5 -> 5`, an
absolute reduction of `0` and a fractional reduction of `0%`. This result
supplies neither a local-to-event lift, an event-marginal selector, an
occurrence rule, nor a Born rule. The flat uniform-`x` marginal is consistent
with the state-resolved XOR conditional and selects no event weighting. Other
compatibility criteria and selector mechanisms are not tested here.

Finding verbatim:

```text
C_SELECTION_STATUS PASS :: case=MULTIPLE_SURVIVORS_UNDER_DECLARED_CRITERION; five_to=5; excluded=0; reduction=0/5 (0%); multiple_survivors_under_criterion=True; selected=None; refutation_target=None
```

## D_CONTROLS

The primary has literal, worktree-relative `AUDIT_INPUT_PATHS`, SHA/blob pins,
a committed bundle containing the full blob-pinned text/AST provenance inputs,
no normal-run dependency on branch-only Git objects, no loaded blocked module,
deterministic short-replay/full-prefix agreement, runtime below 1,400 seconds,
and stdout below both the 6 KB house ceiling and the requested 150 KB ceiling.

Finding verbatim:

```text
D_CONTROLS PASS :: sha_pins=True; BLOCKLIST_text_AST_only=True; determinism=True; runtime_s=68.611<1400; stdout_bytes=2480<6000<150000
```

## Independent refutation outcome

The checker does not import or execute the primary. It parses the primary as
AST, reads its cache/receipt as data, performs two independent full event
replays with bit-packed lane execution, rebuilds the XOR law with a separate
Boolean interpreter, constructs the 24 rotations from oriented frames, and
executes all 15,360 translated-coordinate commutation comparisons. It then
applies active corruptions. A negative weight, zero total mass, missing
conditioning configuration, XOR-to-XNOR mutation, and untranslated-control
transport mutation are all rejected. The XNOR corruption gives the exact counter-witness
`(x,n,y)=(0,(0,0,0,0,0,0),0)`, observed `0`, expected `1`.

```text
CYCLE974_COMPATIBILITY_INDEPENDENT_CHECK
R0_PINS_BLOCKLIST_AND_AST PASS :: pins=True; text_AST_JSON_only=True; blocked_modules_loaded=[]
R1_REFUTE_REBUILD PASS :: events=92260; candidate_digests_match=True; law={"canonical_pair":{"D0":[1,0],"D1":[0,1],"n0":[0,0,0,0,0,0],"n1":[1,0,0,0,0,0],"x":0},"changed_edge_pairs":384,"dependent_word_input_rows":12,"family_words":20,"rotation_count":24,"rotation_failures":[],"rotation_semantic_comparisons":61440,"state_resolved_class_count":2,"translation_failures":[],"translation_semantic_comparisons":15360,"uniform_target_input_changed_pairs":0,"uniform_target_input_edge_pairs":3840,"witness_word_count":6,"word_law_class_count":1,"xor_failures":[]}
R2_REFUTE_COMPATIBILITY PASS :: verdicts={"M1_COUNTING":"SURVIVES","M2_PER_WORLD_UNIFORM":"SURVIVES","M3_OCCUPATION_WEIGHTED":"SURVIVES","M4_FORMATION_LIFETIME":"SURVIVES","M5_FORMATION_MOMENT":"SURVIVES"}; disagreement_witnesses={"M1_COUNTING":null,"M2_PER_WORLD_UNIFORM":null,"M3_OCCUPATION_WEIGHTED":null,"M4_FORMATION_LIFETIME":null,"M5_FORMATION_MOMENT":null}
R3_ACTIVE_CORRUPTION_PROBES PASS :: rejected=negative_weight,zero_total,missing_configuration,XNOR; XNOR_witness={"configuration":[0,[0,0,0,0,0,0],0],"expected":"1","observed":"0","quantity":"P(y|x,n)"}
R4_CRITERION_SCOPE PASS :: case=MULTIPLE_SURVIVORS_UNDER_DECLARED_CRITERION; survivors=5/5; excluded=0; reduction=0/5; multiple_survivors_under_criterion=True
R5_CONTROLS PASS :: determinism=True; runtime_s=157.972<1400; stdout_bytes=1576<6000<150000
REFUTATION_OUTCOME: NO_DISCREPANCY_FOUND
TOTAL: PASS=6 FAIL=0
```

## Imports and open boundary

Load-bearing items:

- the landed Cycle-719 deterministic basis-state machinery: computed lattice
  input;
- the stipulated Cycle-878 composed record-write model definition and its
  declared caps: explicit finite-model boundary;
- the declared finite XOR-law family: radius one, basis states, word length at
  most one, and gate menu identity/`X`/`CNOT`.

The candidate vectors are stipulated finite nonnegative weights and are
normalized here by explicit finite sums. Any finite-additivity bookkeeping in
their Cycle-878 definition is separate finite-model structure, not content of
Record. The current Record axiom supplies no scalar collection functional `I`,
finite additivity, `I(empty)=0`, Born weights, or event-marginal selector.

No observed value, fitted selector, literature number, or physical
normalization is used. The open items remain the full continuous `M_2(C)`
Admissibility law, a derived local-to-event lift through Record, an occurrence
rule, and an event-marginal selector. Those are not repaired by the product
extension theorem.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "does the unique covariant nearest-neighbour dependence law exclude any of the five finite event weightings, and under what declared mechanical criterion?"
source_of_blocker_text: user_goal
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "if selection is pursued, derive a local-to-event lift or an event-marginal selector; covariance of the conditional XOR kernel alone leaves all five candidates"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: "exact on the stipulated 92,260-atom event model and declared radius-one basis-state law under the existential joint-extension criterion"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "explicit joint-extension theorem with exhaustive finite rebuilds; bounded by the stipulated event model and declared gate family"
proposal_allowed: false
proposal_allowed_reason: "finite stipulated event model and finite gate family; no full continuous-domain law and no event-weight selection"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Review record

Pre-review conformance converted both caches to the repository's
`runner_cache.execute_and_write_cache` envelope, refreshed every downstream
SHA pin, and reframed the headline as the positive existence theorem actually
proved. Review then rebound every premise/provenance pin to current main,
registered the independent checker as a claim-scoped packet helper, and
narrowed the draft's named-wall language. No-Go Discipline rejected the broad
wall phrasing because only this one criterion was tested; the landed claim is
the positive five-construction theorem and expressly leaves other selection
routes untested.

```yaml
packet_helper_runner: scripts/frontier_cycle974_compatibility_independent_check_2026_08_10.py
```

## Verdict

Under the declared existential product-extension criterion, the covariant XOR
kernel has an exact joint extension with each of the five finite event
weightings. The construction does not relate local configurations to event
atoms and therefore neither selects an event marginal nor evaluates any other
selection mechanism.
