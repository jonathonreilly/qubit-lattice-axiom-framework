# Route portfolio

## Cycle 2 search

Refreshed `origin/main` immediately before the search. Commit
`17a95e60d85afc246fc7c163adef8869ab3f4194`.

Commands and what they returned:

- `git grep` for `(p, q, r)` and `(p,q,r)` in `docs` and `scripts` on
  `origin/main`. Hits are formation, binding-scale, and uniqueness notes.
  They leave the weights free. The binding-scale note states the odd
  eigenvalue `(p-q)/(p+q+4r)` and does not mention CHSH.
- `git grep` file lists for `(p, q, r)` and for `CHSH` under `docs/*.md`.
  The intersection is empty.
- `git grep` for `product class` and `CHSH` in the same path. No path hit.
- The dynamics-clause Bell note of 2026-09-24 proves `|CHSH| ≤ 2` for a
  different records-only formation reading, and `2√2` for a supplied
  dynamics clause. It does not evaluate `(p,q,r)`.
- Cycle 1's density squares are on this branch, not on `origin/main`, and
  use a representation this cycle does not assume.

Classification: open after the matched-hit review. The executed route is
the exact CHSH comparison of the one-edge product-class law. The directed
six-parameter density maximum stays queued.
