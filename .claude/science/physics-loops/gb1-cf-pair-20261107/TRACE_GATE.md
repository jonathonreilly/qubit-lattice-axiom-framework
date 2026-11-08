# Trace to the requested proof obligation

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: Make two overlapping plaquettes work at finite register size within the current lattice axioms (GB1-CF).
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: Extend the joint patch construction to compatible overlaps, a homogeneous native qubit allocation and a covariant nearest-neighbor schedule; check Admissibility and Record.
```

Known downstream consumer: the open GB1-CF construction in assembly PR #10139.
No adopted claim identifier for that draft obligation is assumed. The pair
calculation resolves a concrete shared-link algebra and supplies one invariant
finite patch update. It does not transfer its zero-external-charge boundary
sector to an interior patch of a larger lattice.

The next patch must explicitly include its boundary flux sectors. A naive
tiling by the two-logical-qubit closed-patch compression is not yet a gluing
construction: neighboring plaquettes share link variables and constraints.
The next decisive question is whether one fixed local encoding and schedule
implements consistent overlap actions while preserving the required spatial
symmetries. This remains an open positive construction problem.
