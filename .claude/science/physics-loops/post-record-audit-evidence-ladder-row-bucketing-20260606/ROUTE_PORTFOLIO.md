# Route Portfolio

| Route | Description | Result | Reason |
|---|---|---|---|
| A | Edit audit ledger rows directly | rejected | Audit verdict/data ownership stays independent. |
| B | Read-only keyword bucketing with ledger hash check | selected | Gives a useful queue without status churn. |
| C | Hand-curated row list only | rejected | Too narrow for "all bounded/conditional lanes." |
| D | Use buckets as verdicts | rejected | Buckets are triage, not audit outcomes. |

Route B is the safe campaign move.
