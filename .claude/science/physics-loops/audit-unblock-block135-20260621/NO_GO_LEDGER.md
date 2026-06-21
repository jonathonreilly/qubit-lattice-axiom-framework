# No-Go Ledger

- Do not apply source-note cycle repairs in block135.
  - Reason: an exploratory apply plus full pipeline regeneration before the
    final rebase produced broad unrelated audit-support churn. The tooling PR
    should stay narrow; source-note apply belongs in a follow-up branch with a
    settled support-refresh base.

- Do not treat cross-reference movement as an audit verdict.
  - Reason: it is graph hygiene only; independent audit still owns status.
