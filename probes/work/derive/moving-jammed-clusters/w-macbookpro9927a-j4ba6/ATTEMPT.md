# Moving jammed clusters, attempt 3: how far a cluster can rearrange in T moves, exactly

Worker `w-macbookpro9927a-j4ba6` (Claude Opus 5.5, `claude-opus-5-5`). The checks are in `check.py` in this directory; they run in about 20 s with a peak of 0.9 GB. Everything in them is exact: breadth-first enumeration of arrangements, integer counts, sympy polynomials and a generating function.

## Sources, provenance and route

**Sources.**
- **Block 39** (PR #8530, head `31e5d0300e`, "records that move").
  - Its pair-weight transit visits "a bond with exactly one occupied end", and the record moves with probability `w_y/(w_x + w_y) > 0`.
  - So an arrangement is reachable in `T` moves iff `T` single moves of records to empty neighbouring sites produce it. Contents ride along with their records.
- **The task.**

Check family Q confirms 4 quoted lines verbatim, including attempt 2's open item.

**Prior attempts.** Both are on another machine and neither has been refereed.
- **Attempt 1** (`w-jonathonsmac4f50-j7b81`, claude-opus-5):
  - the one-move census `6L²`;
  - an upper bound on reachability;
  - a mean-field growth law;
  - the frozen interior.
- **Attempt 2** (`w-jonathonsmac4f50-j7b51`, claude-opus-5-5): it recounted evaporation per bond and stated that "the number of arrangements reachable in `T > 1` moves is still only a1's bound".

**Route.** I formed my plan before opening their files. I do not build on their claims. I take that open item, part (a) beyond one move, and prove it exactly.

**Overlap.** My unit #8728 (moving-clumping-bounds) treated uniqueness and Peierls bounds for block 39's equilibrium gas, not reachability. Nothing is reused.

## (1) Statement

The cluster is the full `L × L × L` box of aligned records in empty space, with no formation. `N_T(L)` is the number of arrangements first reached after exactly `T` moves.

- **T1 (who can move, and when).** A record at graph distance `d` from the outside can first leave its site at move `d`, and not earlier. So the records that can have moved within `t` moves are exactly those within distance `t` of the outside. The movable set grows by one layer per move, and the whole box is movable after `⌈L/2⌉` moves.
- **T2 (two moves, exact).** For every `L ≥ 2`:

  `N_1 = 6L²` and `N_2 = 18L⁴ + 33L² − 24L`.

  Of the two-move arrangements, `C(6L², 2) − 12L` have two displaced records and `36L² − 12L` have one.
- **T3 (every T).** The arrangements with `T` displaced records are exactly the sets of `T` outward moves by distinct surface records. They number

  `[x^T] (1+x)^{6(L−2)²} (1+2x)^{12(L−2)} (1+3x)⁸`,

  where the three factors count face records (1 outward move each), edge records (2) and corners (3). All other arrangements first reached at move `T` number `O(L^{2T−2})`. Hence

  `N_T(L) = (6L²)^T/T! + O(L^{2T−2})`.

  In words: the reachable count after `T` moves is the surface's one-move census raised to the `T`-th power over `T!`. It has no volume term, and no `L^{2T−1}` term.

## (2) Steps

**S0 — ASSUMED.**
- Block 39's transit as supplied.
- Reachability is taken with positive probability, counted in moves. In continuous time, any finite sequence of moves has positive probability in any time `t > 0`, so "reachable in time `T`" is read as "in `T` moves".
- Formation is left out.

**S1 — T1 — PROVED, CHECKED (D).**
- Let `δ(x)` be the graph distance from `x` to the nearest empty site.
- One move changes the set of empty sites by one site, from the mover's new position to its old one. So after `j` moves, `δ(x) ≥ δ₀(x) − j` for every `x`.
- A record can move only if `δ = 1`. So the record at `x` needs `j ≥ δ₀(x) − 1` prior moves, and its first move is at move `≥ δ₀(x)`.
- Conversely, walk the vacancy inward along a shortest path. Records `x_1, …, x_{d−1}`, from the outside inwards, each move one step outward in turn. Then the record at `x` is adjacent to a vacancy and moves at move `d`.
- For the box, `δ₀(x) = min_i min(x_i + 1, L − x_i)`.
- CHECKED (D): for `L = 2, 3, 4, 5` (`t ≤ 3`) and `L = 6, 7` (`t ≤ 2`), the union of sites vacated within `t` moves is exactly `{δ₀ ≤ t}`.

**S2 — the two-displacement part of T2, for every L — PROVED, CHECKED (N).**
- The numbers of vacated and of occupied outside sites are equal, since records are conserved. Each move changes their common value by at most 1. So an arrangement with two displaced records needs two moves, each increasing the number.
- Such a move takes a box record that has not yet moved to an outside site.
- That record must be on the original surface. Interior records are adjacent only to box sites, and at this stage those are vacated only inside.
- On the box, every outside neighbour touches exactly one box site. So the pair of targets determines the pair of movers, and different pairs of moves give different arrangements.
- So the count is the number of pairs of outward moves by distinct records: `C(6L², 2) − Σ_r C(m_r, 2) = C(6L², 2) − 12L`, with `m_r = 1, 2, 3` for face, edge and corner records.

**S3 — the one-displacement part of T2 — PROVED, CHECKED (N).**
- An arrangement with one displaced record `(u, t′)` has `u` within distance 2 of the outside and `t′` within distance 2 of `u`. Whether it is reachable in two moves, and not in one, is decided by the sites within distance 3 of `u`.
- For `L ≥ 7`, classify sites by their distance to each face, capped at 4. The number of sites in each class is a product of factors `(L − 8)` and constants, so the count is a polynomial in `L`.
- Only classes within distance 2 of some face contribute. Their counts are at most quadratic, since a face class has `O(L²)` sites.
- So for `L ≥ 7` the count is a polynomial of degree at most 2. The values at `L = 7, 8, 9` fix it as `36L² − 12L`.
- The enumeration then confirms it at `L = 10` and also at `L = 2 … 6`.
- Summing S2 and S3 gives `N_2 = 18L⁴ + 33L² − 24L`. The full enumeration for `L = 2 … 10` agrees, for example `183060` at `L = 10`.

**S4 — T3, the leading part — PROVED, CHECKED (T).**
- As in S2, arrangements with `T` displaced records are exactly the sets of `T` outward moves by distinct surface records. They are first reached at move `T`, with different sets giving different arrangements.
- Their number is the stated coefficient: choose, record by record, at most one of its `m_r` outward moves.
- Its expansion has leading term `6^T L^{2T}/T!` and no `L^{2T−1}` term. This is checked symbolically for `T = 1 … 5`.
- The reason for the missing term: `C(n, T) = n^T/T! − n^{T−1}/(2(T−2)!) + …` with `n = 6L²` produces only even powers at this order. The records with `m_r ≥ 2` number `O(L)` and remove `O(L · L^{2T−4})`.
- CHECKED (T): the enumeration at three moves for `L = 2, 3, 4, 5` gives, with the three-displaced counts equal to the coefficient:

  | L | arrangements at move 3 | with three displaced |
  |---|---|---|
  | 2 | 4184 | 1512 |
  | 3 | 38394 | 22948 |
  | 4 | 189128 | 138384 |
  | 5 | 668762 | 542436 |

**S5 — T3, the remainder — PROVED.**
- An arrangement first reached at move `T` with `j < T` displaced records is a set of `j` displaced records together with local rearrangements. Everything lies within distance `T` of `j` surface sites.
- For fixed `T` there are `O(L^{2j})` of them: `O(L²)` choices of site for each displaced record, times a bounded number of local patterns.
- Since `j ≤ T − 1`, this is `O(L^{2T−2})`.

## (3) Where the route stops

- The count is for the box. For another convex cluster the leading term is `(M₁)^T/T!`, with `M₁` its one-move census, when each outside neighbour touches one cluster site. That holds for boxes but not for all convex shapes.
- `N_3` is not given as an exact polynomial. It would need values at 7 or more box sizes with `L ≥ 7`, beyond this enumeration's memory.
- Parts (b) and (c) of the task are attempts 1 and 2's routes and are not redone.
- Formation is not included. With formation at rate `z Z_x`, each formation adds a surface record and a new first-move site.

## (4) What would finish it

1. The exact `N_T` for `T ≥ 3` as a polynomial, by a transfer count over surface patterns instead of enumeration.
2. The same census for the faceted shapes attempt 2 considered (octahedron, rhombic dodecahedron). There outside sites touch several surface sites, and the leading coefficient changes.
3. Combined with the per-bond rates of attempt 2: the typical number of moves by time `t` is about `6L²` times the per-bond rate times `t`. That would turn this count into an entropy-production rate for a jammed cluster.
