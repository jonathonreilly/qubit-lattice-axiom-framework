# Dependence classes on a true `Z^3` nearest-neighbour star

Date: 2026-08-11
Cycle: 982
Claim type: `bounded_theorem`
Audit-status authority: independent audit lane only
Effective status: pipeline-derived only after independent audit ratification and dependency closure

## Trace gate

```yaml
trace_class: direct_blocker_closure
reachability_to_target: closes
target_claim_id: null
target_blocker_text: "determine whether the 6/12/3 neighbour-dependence classes survive when adjacency is genuine Z3 nearest-neighbour adjacency"
source_of_blocker_text: user_goal
artifact_role: theorem
next_trace_action: "independent audit of the bounded true-Z3 local-star packet"
```

## Status fields

```yaml
claim_id: cycle982_z3_adjacency_dependence_classes
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: bounded-support
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "finite local-star and finite-family theorem; no branch-local retained-grade proposal"
claim_type_reason: "exact exhaustive classification on the explicitly capped seven-site true-Z3 target-local family"
audit_required_before_effective_retained: true
bare_retained_allowed: false
audit_status_authority: independent audit lane only
negative_assertion_classes: []
packet_primary_runner: scripts/frontier_cycle982_z3_adjacency_dependence_classes_2026_08_11.py
packet_helper_runner: scripts/frontier_cycle982_z3_adjacency_dependence_classes_independent_check_2026_08_11.py
packet_helper_claim_scope: cycle982_z3_adjacency_dependence_classes
```

## Review record

```yaml
review_loop_disposition: pending
hard_landing_packet_helper_mapping:
  z3_adjacency_dependence_classes_cycle982_bounded_theorem_note_2026-08-11:
    - scripts/frontier_cycle982_z3_adjacency_dependence_classes_independent_check_2026_08_11.py
```

The helper mapping above is a hard landing condition so the restricted
independent-audit packet contains the refutation checker.

## Exact target claim

For the declared 23-program target-local family on the origin and its six
genuine `Z^3` nearest neighbours, the 21 Boolean target-output dependence
witnesses form three proper-cubic orbits of sizes `6`, `12`, and `3`, with
stabilizer orders `4`, `2`, and `8`; the invariant

```text
J(w) = || sum of centre-relative control vectors ||^2
```

takes the respective values `1`, `2`, and `0`.  This is a theorem only of the
finite instance and family declared below.

## A_ADJACENCY_MAP

Let the landed semantic wires be `W={0,...,6}`.  The coordinate injection is

```text
phi(0) = (0,0,0)
phi(1..6) = (+x,-x,+y,-y,+z,-z).
```

Two distinct relations must be kept separate.

1. The semantic-wiring relation is the pair shadow of the landed distinct-wire
   constructors.  CNOT is available on every ordered distinct pair and TOF on
   every distinct control/control/target triple, so its undirected pair shadow
   is `K_7`, with `C(7,2)=21` edges.
2. The pulled-back `Z^3` nearest-neighbour relation is
   `||phi(i)-phi(j)||_1=1`.  On these seven sites it is the six-edge star
   `K_{1,6}`, with edges `{0,i}` for `i=1,...,6`.

Therefore the true `Z^3` relation is a **strict sub-relation** of the semantic
wiring relation at this scope:

```text
E_Z3 = {{0,i}: 1 <= i <= 6}  proper-subset  E_sem = {{i,j}: i != j}.
```

It is not a quotient.  The map `phi` is injective and identifies no vertices.
The obstruction to equality is explicit: semantic wires `+x` and `+y` may be
joint operands, while their images have `L1` distance two.

The Cycle-719 physical compiler supplies a different map: it sends a semantic
pair to a Manhattan **path**, not necessarily to one edge.  All 21 semantic
pairs on this star were reconstructed.  The six genuine edges map to paths of
length one; the other 15 pairs map to length-two paths through the centre.  All
paths stay inside the seven-site set and every step has `L1` length one.  This
path realization explains the relation without identifying the two relations.

## B_Z3_WITNESS_CENSUS

### Minimal instance

The finite instance contains seven sites: the origin and its six signed unit
vectors.  Seven is minimal for representing one site together with its six
distinct `Z^3` nearest neighbours.  The census targets the centre, so the
additional ambient neighbours of the six boundary sites are outside the
declared radius-one support.

### Declared family and cap

- Site menu: `{0,1}`.
- Support: the centre `C` and the six sites at `L1` distance one from `C`.
- Words: identity or one landed semantic gate.
- Target-local family:
  - `I`;
  - `X(C)`;
  - `CNOT(n -> C)` for each of six neighbours;
  - `TOF({n,m} -> C)` for each unordered pair of distinct neighbours.
- Family size: `1 + 1 + 6 + C(6,2) = 23`.
- Evaluation cap: all 23 descriptors, both centre inputs, all `2^6`
  neighbour conditions, and every neighbour-bit edge comparison; no sampling.
- Routing cap: every expanded primitive of every one-word program on the
  explicit seven coordinates.

The executable semantics and router are loaded from immutable commit
`39c74017b870c27c804e3992f2a11e90336476b2`, path
[`frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py),
SHA-256
`0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4`.
The lattice geometry and proper rotations are supplied by the
[`Z^3` lattice axiom](MINIMAL_AXIOMS_2026-06-29.md).

### Host construction

The primary gives the 23 semantic words the coordinate list `phi(W)` and calls
the landed Manhattan router.  Across the family it expands 232 primitives into
292 routed nearest-neighbour gates.  The maximum logical-pair route distance is
two, at most three of the seven sites are touched by any word, and the reported
non-nearest-neighbour, operand-order, and route-return failure counts are all
zero.  Thus the landed machinery hosts this finite local `Z^3` instance word by
word under the Cycle-719 route-blueprint contract.  This packet checks the
landed path construction and its operand-return invariants; it does not add a
second unitary execution proof beyond the pinned substrate's compiler contract.

### Census

Identity and `X(C)` are independent of all six neighbour bits.  Each
`CNOT(n -> C)` supplies one witness,

```text
x' = x XOR n,
```

and each `TOF({n,m} -> C)` supplies one witness,

```text
x' = x XOR (n AND m).
```

The exhaustive count is therefore

```text
6 + C(6,2) = 6 + 15 = 21 witnesses.
```

This 23-word family is the target-relevant projection of the earlier 155-word
seven-wire menu: the other 132 one-gate descriptors either act away from the
centre or have a non-central target, so they cannot change the centre output in
one word.  The projection removes only centre-irrelevant descriptors; it does
not remove a neighbour-dependence witness.

Landed truth tables agree with a separate descriptor-level Boolean evaluator
on all `23 * 2 * 2^6 = 2944` target evaluations.

## C_STRUCTURE_TRANSFER

The effective group on centre-relative data is the 24-element proper cubic
rotation group.  The primary enumerates it from determinant-`+1` signed
permutation matrices and computes every orbit and stabilizer.

| class | members | stabilizer | orbit-stabilizer | `J` |
|---|---:|---:|---:|---:|
| CNOT control direction | 6 | 4 | `6 * 4 = 24` | 1 |
| perpendicular TOF control pair | 12 | 2 | `12 * 2 = 24` | 2 |
| opposite TOF control pair | 3 | 8 | `3 * 8 = 24` | 0 |

Thus the `6/12/3` orbit structure and `J` separator transfer exactly on the
declared genuine-`Z^3` local family.  The transfer works because every derived
dependence control is one of the six actual nearest neighbours of the target.
The extra semantic edges enter only as length-two compilation paths; they do
not change which input sites are neighbour conditions for the target rule.

## D_HONEST_SCOPE

The hosted object is a finite radius-one `Z^3` star exercised one alternative
word at a time.  The delivered construction does not claim a simultaneous
infinite-lattice realization.  The following structures are outside the
delivered instance:

- an infinite allocation of one `M_2(C)` site at every point of `Z^3`;
- one translation-uniform admissibility probability rule applied at every
  lattice site;
- a simultaneous global execution choosing among the 23 alternative local
  words; and
- an identification of semantic operand availability with geometric
  adjacency.

These are explicit scope exclusions, not inferred impossibility claims.  The
finite local census is feasible and exercised; extension to a full axiom-wide
host is not tested here.

## Assumptions and imports

| item | class | load-bearing role | disposition |
|---|---|---|---|
| `minimal_axioms` | zero-input structural | supplies `Z^3` nearest-neighbour geometry and proper cubic rotations | used directly |
| pinned Cycle-719 core | one computed lattice input | supplies executable basis-state semantics and Manhattan routing | commit, SHA-256, and Git blob checked |
| seven-coordinate injection | explicit finite boundary condition | fixes the local induced graph | declared above |
| 23-program family | explicit finite boundary condition | fixes the alphabet, target, support, and word-length cap | exhaustively evaluated |

No observed value, fitted selector, probability weight, normalization rule,
literature value, new axiom, or new framework primitive is load-bearing.
Cycles 970/972/977/979/980 are provenance context only: their notes, receipts,
and modules are absent from the primary's literal input set and are neither
imported nor executed.

## Proof-obligation graph

1. **Relation obligation — proved here.** Enumerate the `K_7` semantic pair
   shadow and the induced `L1=1` relation under `phi`; compare the two sets and
   exhibit `(+x,+y)` as an equality obstruction.
2. **Host obligation — proved here at the declared finite cap.** Reconstruct
   every landed Manhattan path and every word-level routing certificate; check
   nearest-neighbour steps, operand order, and route return.
3. **Witness obligation — proved here.** Exhaust all target truth tables and
   neighbour-bit edge comparisons, with an independent Boolean evaluator.
4. **Orbit obligation — proved here.** Enumerate all 24 proper cubic rotations,
   orbits, stabilizers, coverage, and orbit-stabilizer products.
5. **Separator obligation — proved here.** Compute `J` directly on every
   witness and check constancy within and distinction across the three orbits.

The boundary cases `I` and `X(C)` are included and yield no witnesses.  The
target-local family includes every unordered neighbour pair, including the
three opposite pairs.  Multi-word programs, other alphabets, boundary-site
target laws, and a simultaneous infinite translation-uniform rule are outside
the theorem.  The strongest extension not proved here is the existence and
classification of one infinite translation-uniform admissibility probability
rule whose local support realizes this finite menu.

## Refutation specification and controls

The primary's checks gate only construction, reconciliation, and provenance.
A non-hosted, deformed, failed-transfer, or unavailable outcome is a valid
reportable finding when its bookkeeping is internally consistent.

The independent checker imports and executes neither the primary nor
Cycle-719.  It byte-pins the primary source and deterministic receipt,
input-fingerprints the complete current primary cache so any cache change
forces checker refresh, and authenticates that cache's source/status/stdout
semantics without assigning its variable elapsed-time envelope a fixed
expected hash.  It independently rebuilds the graph, 23 Boolean laws, 21
witnesses, cubic action, orbits, stabilizers, `J` values, and exact
routing-count arithmetic, and rejects ten corruptions:

1. relation classification;
2. semantic edge count;
3. local hostability flag;
4. witness count;
5. orbit size;
6. stabilizer order;
7. `J` value;
8. infinite-scope flag;
9. primary-source pin; and
10. cached witness headline.

Primary check-family mutations separately corrupt A edge count, B family size,
C transfer orbit data, D scope inventory, and E source pin; each makes its
target check fail.  A separate coherent synthetic non-hosted receipt—with a
route failure, absent hosted census, and not-applicable transfer result—passes
the checker's bookkeeping validator.  Agreement with the rich independent
reconstruction is reported data, not an integrity condition.

## Artifacts and reproduction

Primary:

- [`frontier_cycle982_z3_adjacency_dependence_classes_2026_08_11.py`](../scripts/frontier_cycle982_z3_adjacency_dependence_classes_2026_08_11.py)
- [`z3_adjacency_dependence_classes_cycle982_receipt_2026_08_11.json`](../outputs/z3_adjacency_dependence_classes_cycle982_receipt_2026_08_11.json)
- [`frontier_cycle982_z3_adjacency_dependence_classes_2026_08_11.txt`](../logs/runner-cache/frontier_cycle982_z3_adjacency_dependence_classes_2026_08_11.txt)

Independent refutation checker:

- [`frontier_cycle982_z3_adjacency_dependence_classes_independent_check_2026_08_11.py`](../scripts/frontier_cycle982_z3_adjacency_dependence_classes_independent_check_2026_08_11.py)
- [`z3_adjacency_dependence_classes_cycle982_independent_check_receipt_2026_08_11.json`](../outputs/z3_adjacency_dependence_classes_cycle982_independent_check_receipt_2026_08_11.json)
- [`frontier_cycle982_z3_adjacency_dependence_classes_independent_check_2026_08_11.txt`](../logs/runner-cache/frontier_cycle982_z3_adjacency_dependence_classes_independent_check_2026_08_11.txt)

```bash
python3 scripts/cached_runner_output.py --refresh --timeout-sec 1400 scripts/frontier_cycle982_z3_adjacency_dependence_classes_2026_08_11.py
python3 scripts/cached_runner_output.py --refresh --timeout-sec 300 scripts/frontier_cycle982_z3_adjacency_dependence_classes_independent_check_2026_08_11.py
```

Both canonical cache envelopes pin runner SHA-256, declared inputs, timeout,
exit status, and stdout.  Both runners replay deterministically, keep stdout
below 6000 bytes, end in `TOTAL: PASS=5 FAIL=0`, and write machine-readable
receipts.  Audit-status authority remains with the independent audit lane.
