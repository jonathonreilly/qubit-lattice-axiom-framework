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

2026-10-09 cycle 4 author pass. Value gate, searched `origin/main` at
`d9b869b97944676aaa759915462c529dc276a04c`:

- V1. The formation sentence is still reading note (2) of
  `docs/MINIMAL_AXIOMS_2026-06-29.md`. It was quoted in `HANDOFF.md` and
  not made into its own note. The discriminator actually executed is which
  readout weights of the directed pattern see the twist. Source: the
  axiom open-gate list names Born weight values, and the parent CHSH note
  says a one-site reduction was not tested.
- V2. Not on `origin/main`. Commands were `git grep` for readout-weight
  with twist, for `diag(1,-1,1)`, for one-site reduction of the directed
  bond, and a title scan for readout-weight notes. Hits are other
  matrices, the six-letter handed census, the Moriya dynamics ground
  state, and a June selector-tangent prototype. None is this partial trace.
- V3. Theorems 1–3 of the cycle-4 note, checked by the paired runner.
  The density, the instrument, and the formation triple remain open.
- V4. Before, local weights of this pattern were untested. After, they
  are independent of `t`, symmetric joint weights miss `t`, and one
  antisymmetric weight equals `2t`. The improper reflection flips only
  that sign.
- V5. Not a corollary of the cycle-3 square. That square depends on
  `u^2+t^2` and does not reduce the state. The partial trace and the
  weight coefficient `W_yx-W_xy` are not Gram eigenvalues.

No-go gate for the scoped blindness is in the cycle-4 source note. The
antisymmetric weight does see `t`. A universal claim that every readout
misses it, or that the physical rule is handed, is not made. Author
mutations, each on a scratch copy that was deleted: reversing the
antisymmetric difference fails four checks; demanding the wing-1 Bloch
number equal `p` fails three. Independent review has not been requested.
No audit grade.

Conformance sections touched by this author pass, not a review-loop verdict:
the note states its hypotheses, pins one runner and cache, keeps the
negative claim inside the pattern, and does not write an audit verdict.
Sections that belong to independent review were not run.

PR 9475 remains open against main. Not merged. CI is not a landing signal.

2026-10-09 cycle 5 author pass. Value gate, searched `origin/main` at
`d9b869b97944676aaa759915462c529dc276a04c`:

- V1. The queued discriminator is whether proper-cubic covariance selects
  a quadratic scalar action of one bond correlation, including the sign of
  `t`. Source: `OPPORTUNITY_QUEUE.md` item 5 before this cycle, and the
  axiom open-gate bullet naming source/action.
- V2. Not on `origin/main`. The cubic-anisotropy note counts weights on
  the traceless symmetric block only. Commands were `git grep` for
  quadratic invariant polynomials, for `Q_T2`, for `6(u-v)`, and for
  `c_21-c_12`. None is this nine-entry basis or this directed substitution.
- V3. Theorems 1–3 of the cycle-5 note, checked by the paired runner.
  The matrix, the pattern, and the formation triple remain open.
- V4. Before, the quadratic scalars of this matrix were uncounted. After,
  both groups leave four channels, one rational rotation forces the middle
  ratio `9/2` on a tested pair, and the directed pattern is even in `t`.
- V5. Not a corollary of the cycle-1 linear nullspace or of the cycle-4
  readout. The linear nullspace fixes matrices, not degree-2 polynomials.
  The readout sees the sign of `t`. These scalars do not.

No-go gate for the scoped channels is in the cycle-5 source note. The
antisymmetric square does see `t^2`. A universal claim that every
functional misses the sign, or that a physical action has been selected,
is not made. Author mutations, each on a scratch copy that was deleted:
replacing the antisymmetric difference by a sum fails four checks;
demanding the directed antisymmetric channel equal `t^2` fails one.
Independent review has not been requested. No audit grade.

Conformance sections touched by this author pass, not a review-loop verdict:
the note states its hypotheses, pins one runner and cache, keeps the
negative claim inside degree 2, separates the trace check from Theorems
1–3, and does not write an audit verdict. Sections that belong to
independent review were not run. The hand multiplication and the directed
substitution are the checks that do not share the row-reduction path.

2026-10-09 cycle 6 author pass. Value gate, searched `origin/main` at
`d9b869b97944676aaa759915462c529dc276a04c`:

- V1. The queued discriminator is whether chirality of a record alphabet
  other than the bond matrix is what lets a soldered product vary. Source:
  the order-blind note's boundary that generic orbits beyond `(1, 2, 3)`
  and its chiral pair are not classified, and the axiom open-gate bullet
  naming source/action.
- V2. Not on `origin/main`. Commands were `git grep` for `orbit of (0, 1, 2)`
  under `docs/*.md` and `scripts/*.py`, and for `(0, 1, 2)` inside the
  order-blind note. No path hit. The chiral pair named there is the mirror
  union of `(1, 2, 3)`.
- V3. Theorems 1–3 of the cycle-6 note, checked by the paired runner.
  The product, `kappa`, and the formation triple remain open.
- V4. Before, this orbit was unclassified. After, it is one achiral
  24-point orbit, the transverse-sign factor is identically `0`, and one
  axis-role product is normalised, mirror-fixed, and has path correlation
  `1/72` at `kappa = 1/2`.
- V5. Not a corollary of the cycle-5 channels or of substituting `4` for
  `3` in the `(1, 2, 3)` sign. Those objects are a `3×3` matrix and a
  triple of nonzero absolute values. The transverse product here is `0`.

No-go gate for the scoped orbit is in the cycle-6 source note. The
axis-role product does vary the alphabet. A universal claim that every
24-point orbit varies, or that variation requires a chiral pair, is not
made. Author mutations, each on a scratch copy that was deleted: replacing
the opposite cap by the same direction fails five checks; demanding the
correlation equal `1/36` fails one. Independent review has not been
requested. No audit grade.

Conformance sections touched by this author pass, not a review-loop verdict:
the note states its hypotheses, pins one runner and cache, keeps the
negative claim inside this alphabet, separates the mirror fold from the
path enumeration, and does not write an audit verdict. Sections that
belong to independent review were not run.
