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

2026-10-09 cycle 3 author pass. Value gate, searched `origin/main` at
`d9b869b97944676aaa759915462c529dc276a04c`:

- V1. The queued discriminator is the exact CHSH maximum of the directed
  six-parameter family inside the density representation. Source:
  `OPPORTUNITY_QUEUE.md` item 2 before this cycle, and the parent note's
  statement that the directed region was not computed.
- V2. Not on `origin/main`. The grep named in `ROUTE_PORTFOLIO.md` found no
  CHSH evaluation of `c_21-c_12` or of the directed stabilizer. Cycle 1 on
  this branch locates square `8` only for `w = -1` and for two undirected
  corners, and it leaves the six-parameter region uncomputed.
- V3. Theorems 1–5 of the cycle-3 note, checked by the paired runner.
  The density representation and the formation triple remain open.
- V4. Before, the directed square was unknown. After, the elementary square
  is at most `8`, with equality on a circle, and signed-axis settings attain
  square `8` at four diagonal points but not at the singlet.
- V5. Not a corollary of setting `t = 0` in cycle 1. The Gram eigenvalue
  `u^2 + t^2`, the equality circle, and the axis strategy `2u - 2t` are new.
  Specializing `t = 0` recovers the two undirected corners as a check.

No-go gate for the scoped squares is in the cycle-3 source note. Square `8`
is attained on the circle. A universal claim that every representation
attains it, or that none does, is not made. Author mutations, each on a
scratch copy that was deleted: flipping the sign in `T` fails the Gram
check; returning `8 r^2` on every branch fails the split-length check;
changing the `e_y` image fails the six-pair enumeration. Independent review
has not been requested. No audit grade.

Conformance sections touched by this author pass, not a review-loop verdict:
the note states its hypotheses, pins one runner and cache, keeps the
negative claim inside the pattern, separates the parent's nullspace from
Theorems 1–5, and does not write an audit verdict. Sections that belong to
independent review were not run.

PR 9475 remains open against main. Not merged. CI is not a landing signal.
