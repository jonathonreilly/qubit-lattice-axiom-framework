# Review history

2026-10-09 cycle 1 author pass. Runner re-executed through `runner_cache.py`:
`status ok`, exit 0, `TOTAL: PASS=31 FAIL=0`.

2026-10-09 cycle 2 author pass. Value gate, searched `origin/main` at
`17a95e60d85`:

- V1. The queued discriminator is whether the product-class menu law
  `(p,q,r)` reaches CHSH squares 4 and 8 without a two-qubit density.
  Source: `OPPORTUNITY_QUEUE.md` item 1 and the cycle-1 handoff.
- V2. New exact squares for that pair law. Search commands were `git grep`
  for `(p, q, r)` and for `CHSH` under `docs/*.md`. The two file sets are
  disjoint. The formation census and the dynamics-clause Bell note do not
  state these squares.
- V3. Theorems 1–4 of the cycle-2 note, checked by the paired runner.
  The density representation and the dynamics clause remain open.
- V4. Before, the menu weights were known to be free and their CHSH squares
  were unevaluated. After, the coordinate square is at most `8/9`, the
  global-sign square equals 4 only on a named boundary, and neither is 8.
- V5. Not a corollary of cycle 1. Cycle 1 uses a density and leaves the menu
  route queued. The closest landed object is the odd eigenvalue
  `(p-q)/(p+q+4r)`, which is not a CHSH square.

No-go gate for the scoped squares is recorded in the source note. A universal
claim that no representation reaches square 8 is not made. Independent review
has not been requested. No audit grade.

PR 9475 remains open against main. Not merged. CI is not a landing signal.
