# Route Portfolio

| Route | Description | Result | Reason |
|---|---|---|---|
| A | Select the dial from the bucket | rejected | User asked for stable location, not forced dial. |
| B | Read-only sub-bucket the selector/dial rows | selected | Gives actionable queues without verdict edits. |
| C | Edit audit rows directly | rejected | Audit ownership boundary. |
| D | Manual one-off list | rejected | Less useful than current-ledger scan. |

Route B is exact support for queue shaping.
