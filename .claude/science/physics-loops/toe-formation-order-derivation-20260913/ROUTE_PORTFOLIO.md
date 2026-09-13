# Route portfolio

Searched `origin/main` `b8c9d9d819` for the result before producing it.

Commands:

```text
git grep -n -iE "(order.blind|invariant total order|exchange identity)" origin/main -- 'docs/*.md'
git ls-tree -r --name-only origin/main -- docs/ | grep -iE 'FORMATION|ORDER_BLIND|MONOTONE_ORDER'
```

Classification of hits:

- Formation-versus-static (2026-09-06) and monotone-order (2026-09-07)
  notes: related, different target (product-rule six-projector menu;
  monotone class versus static law). Not this lemma, not this
  classification.
- Q8 covariant law pair: model-pair precedent, not a pair of orders.
- No hit for an invariant-total-order lemma on `Z^3`.
- No hit for the path3 residual `(pminus-pplus)^2`.

Target state: open after matched-hit review.

Executed route: exchange characterization plus path3 polynomial plus
Ising witness. Score 3. Live.

Not executed: Bloch-alphabet classification; deterministic 0/1 kernels;
random covariant order-laws. Parked as later blocks, not as this PR.
