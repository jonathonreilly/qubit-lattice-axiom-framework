# Goal

Produce a reviewable science block for the S3/Route-2 readout endpoint triple
without auditing or applying verdicts.

Block52 target:

```text
Split the missing bridge c_TE = -R_conn into:
1. a typed magnitude bridge |c_TE| = R_conn, and
2. sign selection from the existing positivity bound q_E > 0.
```

The block succeeds if it gives an exact checked support theorem that narrows
the remaining import while leaving the endpoint target honestly open on the
current bank.

This block must not push to `main`, refresh old PRs to `main`, or inspect PR
conflict/mergeability state.
