# Trace Gate

```yaml
trace_class: methodology
target_claim_id: null
target_blocker_text: "orphan runner-cache cleanup can delete cache files still linked by live repo notes"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: tooling
next_trace_action: "Open stacked PR, then review the 8 remaining dry-run orphan candidates in a later block."
```

If this artifact is true, it does not change any claim status. It makes the
cleanup command safer by preventing broken evidence links.
