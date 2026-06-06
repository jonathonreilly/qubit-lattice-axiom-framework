# Goal

Repair the audited conditional row
`lsp_projective_canonical_kp_equals_p_narrow_theorem_note_2026-06-05`.

The exact blocker is:

```text
scope_too_broad: add an explicit nonzero-outcome projection hypothesis or
weaken the necessity clause to rows mixing into labels s with P_s != 0 and
s != r, then rerun with a zero-projector edge-case check.
```

This branch adds that hypothesis, weakens the zero-label boundary explicitly,
and adds a runner edge-case test.
