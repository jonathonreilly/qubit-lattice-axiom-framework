# Route Portfolio

| route | result |
| --- | --- |
| Raise timeout | Rejected for default audit path; source logs report 128s, 167s, and slow held-out batch behavior. |
| Recompute live by default | Rejected. It keeps the audit queue fragile. |
| Frozen-log verifier plus `--recompute` | Chosen. It preserves evidence and makes cache checks deterministic. |
