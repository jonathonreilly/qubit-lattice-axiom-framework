# Route Portfolio

| route | result |
| --- | --- |
| Raise timeout | Rejected. The broad runner timed out at 300 seconds in trial. |
| Narrow the evidence surface | Rejected. The frozen full-harness output already contains the broad protocol results. |
| Frozen-log verifier plus `--recompute` | Chosen. It preserves the historical full-harness evidence and makes the audit cache fast. |
