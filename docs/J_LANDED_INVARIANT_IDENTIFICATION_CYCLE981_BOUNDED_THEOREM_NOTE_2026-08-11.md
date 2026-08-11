# Is the witness control-sum norm already a landed invariant?

Date: 2026-08-11
Cycle: 981
Claim type: `bounded_theorem`
Audit-status authority: independent audit lane only
Effective status: pipeline-derived only after independent audit ratification and dependency closure

## Trace gate

```yaml
trace_class: negative_route_pruning
reachability_to_target: prunes
target_claim_id: null
target_blocker_text: "is J a NEW object, or does it coincide with something the corpus already carries?"
source_of_blocker_text: user_goal
artifact_role: theorem
next_trace_action: "independent audit of the bounded identification census"
```

## Status fields

```yaml
claim_id: cycle981_j_landed_invariant_identification
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: bounded-support
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "finite pinned-corpus identification census; no branch-local retained-grade proposal"
claim_type_reason: "mechanical candidate extraction and exact shared-domain comparison on a pinned finite witness family"
audit_required_before_effective_retained: true
bare_retained_allowed: false
audit_status_authority: independent audit lane only
negative_assertion_classes: []
packet_primary_runner: scripts/frontier_cycle981_j_landed_invariant_identification_2026_08_11.py
packet_helper_runner: scripts/frontier_cycle981_j_landed_invariant_identification_independent_check_2026_08_11.py
packet_helper_claim_scope: cycle981_j_landed_invariant_identification
```

## Review record

```yaml
review_loop_disposition: pending
hard_landing_packet_helper_mapping:
  j_landed_invariant_identification_cycle981_bounded_theorem_note_2026-08-11:
    - scripts/frontier_cycle981_j_landed_invariant_identification_independent_check_2026_08_11.py
```

## Result

Within the declared search of pinned `origin/main`, **`J` is landed-new**:
no landed candidate is the same integer-valued function on the 21 target-centred
neighbour-dependence witness words. This is a bounded corpus-identification
statement, not a claim that no future or syntactically disguised formula can
equal `J`.

The two quantities already adjacent to `J` on the pinned Cycle 980 substrate
are mechanically comparable and disagree:

| candidate | result | first witness | `J` | candidate |
|---|---|---|---:|---:|
| control arity | `DISAGREES` | `TOF(+x,-x->C)` | 0 | 2 |
| off-diagonal control-Gram sum | `DISAGREES` | `CNOT(+x->C)` | 1 | 0 |

Every actually landed cross-lane candidate has a different domain or type, as
listed below. There is therefore no exact agreement table to report. Had any
candidate agreed on all shared inputs, the runner would have reported
`COINCIDES` with all 21 rows; that outcome would pass the same integrity gates.

## A_CANDIDATE_ENUMERATION

The landed-corpus snapshot is the literal commit
`ea0968c71ad46c39c6dacb39f88a18780363b71f`. The Cycle 980 substrate is read
separately at literal commit `c186c8ba7f44f2245cf38e59fc429ce90a6e0d7d`.
All source bodies are read with `git show`; the runner reads exactly six.

The declared search has three layers:

1. a path/token index over `docs/**/*.md` and `scripts/**/*.py` using the
   lexicon `charge-space`, `three-parity`, `parity law`, `control-sum`,
   `squared norm`, `cell-cut`, `cover`, `leverage`, `local word`, and
   `local configuration`;
2. an exact-`J` token scan for `control_sum_norm_squared`, centre-relative
   control displacement, `norm2(sum_controls)`, and `sum_i c_i`; and
3. AST extraction on the two Python bodies among the six full reads, with
   Markdown token windows on the other four.

The candidate list actually extracted is:

| candidate | landed at pin? | native domain -> codomain | native spectrum |
|---|---:|---|---|
| Cycle 980 control arity | no; pinned comparison substrate | witness word -> integer | `{1,2}` |
| Cycle 980 off-diagonal control-Gram sum | no; pinned comparison substrate | witness word -> integer | `{-1,0}` |
| Cycle 719 B-rail occupation `sum(b)` | yes | controller trace -> integer | finite rail occupancy |
| Cycle 719 two-rail token total | yes | controller state -> integer | `{2}` on the declared code |
| `O_h` star shell leverage | yes | six-arm representation -> rational constant | `{3/2}` |
| Cycle 732 cell adjacency cost | yes | least-volume dissection -> integer | `{108,110,...,128}` |
| Cycle 732 228-point cover parity | yes | least-volume dissection -> integer mod 2 | `{0}` |
| Cycle 733 column-subset cost parity | yes | piece/dissection plus column subset -> integer mod 2 | ten laws, one exception |
| Cycle 735 piece-borne charge | yes | least-cost cutting -> integer mod 2 | `{0,1}` |

The landed sources are the
[`Cycle 719 controller core`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py),
[`O_h` star shell-leverage note](OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md),
[`Cycle 732 parity/cost intake`](historic_intake/HISTORIC_PHYSICAL_PARITY_CERTIFICATE_COST_SPECTRUM_CYCLE732_NOTE_2026_08_04_INTAKE_NOTE_2026-08-05.md),
[`Cycle 733 column-parity intake`](historic_intake/HISTORIC_PHYSICAL_COLUMN_FAMILY_PARITY_LAW_FORCED_ORBITS_CYCLE733_NOTE_2026_08_04_INTAKE_NOTE_2026-08-05.md),
and [`Cycle 735 piece-charge intake`](historic_intake/HISTORIC_PHYSICAL_LEAST_COST_CUTTING_PIECE_CHARGE_CYCLE735_NOTE_2026_08_05_INTAKE_NOTE_2026-08-05.md).

The specifically requested Cycle 736 three-dimensional charge space, Cycle
746 three-parity law, and later Cycle 752/753/754/761 cell-cutting
sharing/variance/shadow/cover surfaces are absent from the pinned main tree.
Their known non-main PR heads are not treated as landed candidates. Presence is
tested mechanically by exact path lookup at the pin; no branch name or PR title
is evidence of landing.

## B_IDENTIFICATION_TEST

The common normalization is source-native: no affine rescaling, value
permutation, sign change, or spectrum relabeling is allowed. For the two
same-word candidates the runner reconstructs every witness and compares values
row by row:

| orbit | members | `J` | control arity | off-diagonal Gram sum |
|---|---:|---:|---:|---:|
| CNOT | 6 | 1 | 1 | 0 |
| perpendicular-control TOF | 12 | 2 | 2 | 0 |
| opposite-control TOF | 3 | 0 | 2 | -1 |

Per-candidate results:

| candidate | result | mechanical reason |
|---|---|---|
| Cycle 980 control arity | `DISAGREES` | first mismatch `TOF(+x,-x->C)`: `0 != 2` |
| Cycle 980 off-diagonal control-Gram sum | `DISAGREES` | first mismatch `CNOT(+x->C)`: `1 != 0` |
| Cycle 719 B-rail occupation | `NOT_COMPARABLE` | controller-trace domain, not gate-word domain |
| Cycle 719 two-rail token total | `NOT_COMPARABLE` | controller-state domain, not gate-word domain |
| `O_h` shell leverage | `NOT_COMPARABLE` | representation constant of type rational, not an integer word functional |
| Cycle 732 adjacency cost | `NOT_COMPARABLE` | cell-dissection domain |
| Cycle 732 cover parity | `NOT_COMPARABLE` | cell-dissection domain and mod-2 codomain |
| Cycle 733 column parity | `NOT_COMPARABLE` | piece/dissection-with-column-subset domain |
| Cycle 735 piece charge | `NOT_COMPARABLE` | least-cost-cutting domain and mod-2 codomain |

The type test is mechanical: candidate and `J` domain-schema identifiers must
match before a value comparison is admitted. A shared geometric phrase such as
“star,” “charge,” “norm,” or “parity” does not create shared inputs.

## C_VERDICT

`J(w)=||sum_i c_i||^2` is new relative to the landed objects found by this
pinned search. No cross-lane numeric bridge is established.

Even if a future candidate produces a 21-row exact agreement table, that would
identify two functions on this finite shared domain only. It would not identify
their physics, turn a cell-cutting charge into a controller observable, supply
a probability rule, or extend either object beyond its declared domain.

## D_CONTROLS

- Six literal source-body reads, all by immutable `git show`, with SHA-256 and
  Git-blob pins.
- Repository-wide candidate discovery is a declared path/token index; Python
  AST inspection is restricted to the two read Python bodies.
- Main-tree absence of the requested non-main surfaces is tested at the
  literal snapshot commit.
- The 21-word comparison is exhaustive and deterministic; there is no sample,
  fitted map, rescaling, or observed input.
- Integrity gates check inventory/comparison/verdict reconciliation only. They
  do not require the landed-new result.
- No axiom, framework primitive, audit verdict, effective status, or
  probability interpretation is added.

## Artifacts and reproduction

Primary:

- [`frontier_cycle981_j_landed_invariant_identification_2026_08_11.py`](../scripts/frontier_cycle981_j_landed_invariant_identification_2026_08_11.py)
- [`j_landed_invariant_identification_cycle981_receipt_2026_08_11.json`](../outputs/j_landed_invariant_identification_cycle981_receipt_2026_08_11.json)
- [`frontier_cycle981_j_landed_invariant_identification_2026_08_11.txt`](../logs/runner-cache/frontier_cycle981_j_landed_invariant_identification_2026_08_11.txt)

Independent refutation checker:

- [`frontier_cycle981_j_landed_invariant_identification_independent_check_2026_08_11.py`](../scripts/frontier_cycle981_j_landed_invariant_identification_independent_check_2026_08_11.py)
- [`j_landed_invariant_identification_cycle981_independent_check_receipt_2026_08_11.json`](../outputs/j_landed_invariant_identification_cycle981_independent_check_receipt_2026_08_11.json)
- [`frontier_cycle981_j_landed_invariant_identification_independent_check_2026_08_11.txt`](../logs/runner-cache/frontier_cycle981_j_landed_invariant_identification_independent_check_2026_08_11.txt)

```bash
python3 scripts/cached_runner_output.py --refresh --timeout-sec 300 scripts/frontier_cycle981_j_landed_invariant_identification_2026_08_11.py
python3 scripts/cached_runner_output.py --refresh --timeout-sec 300 scripts/frontier_cycle981_j_landed_invariant_identification_independent_check_2026_08_11.py
```

The checker imports and executes neither the primary nor the Cycle 980
substrate. It parses the primary as inert text/AST, independently reconstructs
the 21 inputs and comparison values, binds the primary receipt/cache, and
actively rejects the declared corruptions.
