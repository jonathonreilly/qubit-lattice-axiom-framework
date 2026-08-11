# A one-CNOT inter-site dependence witness in the Cycle-719 substrate — Cycle 970

Date: 2026-08-09

Audit: unset; independent audit remains a separate lane

Status: bounded support on the declared finite family

**Type:** bounded_theorem

Runners:

- [`frontier_cycle970_inter_site_gate_2026_08_09.py`](../scripts/frontier_cycle970_inter_site_gate_2026_08_09.py)
- [`frontier_cycle970_gate_independent_check_2026_08_09.py`](../scripts/frontier_cycle970_gate_independent_check_2026_08_09.py)

Pinned caches:

- [`frontier_cycle970_inter_site_gate_2026_08_09.txt`](../logs/runner-cache/frontier_cycle970_inter_site_gate_2026_08_09.txt)
- [`frontier_cycle970_gate_independent_check_2026_08_09.txt`](../logs/runner-cache/frontier_cycle970_gate_independent_check_2026_08_09.txt)

Receipts:

- [`inter_site_gate_cycle970_receipt_2026_08_09.json`](../outputs/inter_site_gate_cycle970_receipt_2026_08_09.json)
- [`inter_site_gate_independent_check_cycle970_receipt_2026_08_09.json`](../outputs/inter_site_gate_independent_check_cycle970_receipt_2026_08_09.json)

The source delta preserves the four-axiom and registered-primitive rosters.

## Load-bearing sources and declared domain

The finite gate semantics come from the
[`RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md`](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md)
package and its Cycle-719/Cycle-715 executable chain. That source row is an
unaudited dependency, so this row enters the audit graph as bounded and pending
with the dependency edge visible.

The [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) memo supplies
the names for the two neighboring sites, their basis possibilities, and the
condition-varying distribution reading. The theorem domain is exactly:

- one labeled nearest-neighbor patch with sites `0=(0,0,0)` and `1=(1,0,0)`;
- target and neighbor basis values in `{0,1}`;
- the five words `I`, `X(0)`, `X(1)`, `CNOT(0->1)`, and `CNOT(1->0)`;
- a fixed target input `x` shared by both neighbor branches.

For gate word `W`, target site `t`, fixed target input `x`, neighbor bit `n`,
and target output `y`, define

```text
D[W,t,x](y | n)
  = 1{ applying W to (target t=x, nearest neighbor=n) outputs t=y }.
```

This is the deterministic point distribution induced by the cited basis-state
semantics.

## Exact census

The complete declared family has 20 site/input/word comparisons and 40
neighbor-conditioned configurations. Four comparisons separate the two
neighbor branches, covering eight conditioned configurations:

```text
PASS A_STATE_RESOLVED_CENSUS :: state_resolved_changed=4/20 paired comparisons; changed_pair_configurations=8/40
```

The certificate reconciles the family size, changed-row list, conditioned-row
count, and replay digest.

## One-CNOT witness

Choose target site `0`, neighbor site `1`, and supplied target input `x=0`.
The word `[CNOT(1->0)]` gives

```text
D(y | n=0) = [1,0]
D(y | n=1) = [0,1]
(0,0) -> (0,0)
(0,1) -> (1,1)
```

Thus the target point distribution depends on the neighbor condition on this
declared finite surface. The executable certificate records the exact word,
both input/output traces, both point distributions, and target mutation.

## Declared scope certificate

The result is the tuple

```text
route: one_cnot_finite_family_witness
family_words: 5
comparison_contexts: 20
supplied_input: fixed target input x=0 on both neighbor branches
```

The bounded claim is precisely this finite-family census and explicit witness.
The separate audit lane owns any effective-status transition.

## Provenance and independent recomputation

The primary cache input fingerprint binds:

- the axiom memo;
- the Cycle-719 wrapper;
- the Cycle-715 file that implements `cn` and `apply_semantic`.

The independent checker uses an internal XOR interpreter while reading the
substrate sources as AST/text. It validates the stable source hashes, parses
the fresh primary cache envelope, recomputes
the primary input fingerprint, checks the Cycle-715 CNOT construction and XOR
update by AST, and independently enumerates the 20 comparisons.

The required execution order is primary cache refresh followed by independent
cache refresh. Both receipts and both cache envelopes are generated from that
order.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "does the Cycle-719 controller substrate host a site-local distribution that varies with a nearest-neighbor condition?"
source_of_blocker_text: user_goal
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "independent audit the exact finite-family witness and its Cycle-719 dependency chain"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "exact finite two-site basis-menu census with a supplied fixed target input"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite two-site basis-menu census plus an explicit one-CNOT neighbor-conditioned witness at supplied target input x=0"
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/frontier_cycle970_gate_independent_check_2026_08_09.py
```

The `packet_helper_runner` line declares the independent checker as a
claim-scoped packet source. The restricted packet is complete when the graph
builder carries the matching explicit helper mapping.

## Review record and hard landing conditions

Review-loop hard landing conditions for this repaired final state:

1. `EXPLICIT_PACKET_HELPER_RUNNER_PATHS` in
   `docs/audit/scripts/build_citation_graph.py` carries exactly
   `"inter_site_gate_cycle970_bounded_theorem_note_2026-08-09":
   ["scripts/frontier_cycle970_gate_independent_check_2026_08_09.py"]`.
2. The citation graph manifest is regenerated on the integration tree and the
   Cycle-970 ledger row names the Cycle-719 claim id in `deps` and the checker
   in `helper_runner_paths`.
3. A fresh primary-cache execution followed by a fresh independent-cache
   execution passes, and a Cycle-715 CNOT-semantics mutation invalidates the
   bound evidence.

## Result

Cycle 970 supplies an exact one-CNOT neighbor-conditioned point-distribution
witness on the declared two-site basis-menu family: `4/20` separating
comparisons, `8/40` conditioned configurations in those rows, and the explicit
`[CNOT(1->0)]` trace above.
