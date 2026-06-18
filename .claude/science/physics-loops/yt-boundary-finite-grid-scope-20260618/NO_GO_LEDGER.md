# No-Go Ledger

| Route | Result | Why it should not be repeated here |
|---|---|---|
| Treat 33-point grid monotonicity as continuum monotonicity | blocked | The runner samples a finite grid and does not provide interval/validated-numerics proof. |
| Treat `brentq` agreement as exact uniqueness | blocked | Bracketed root stability is a finite diagnostic, not a theorem over every point of the interval. |
| Treat implementation constants as retained authorities | blocked | The note explicitly keeps them as declared implementation inputs. |
| Retag the audit ledger from this branch | forbidden | User policy: source-side PR only; auditor/reviewer owns verdicts and landing. |
