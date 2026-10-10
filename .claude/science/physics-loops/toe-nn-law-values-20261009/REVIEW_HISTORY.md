# Review history

2026-10-10 cycle 15 author pass. Value gate, searched `origin/main` at
`d9b869b97944676aaa759915462c529dc276a04c`:

- V1. The queued discriminator is which integer vectors
  `(w0, w1, w2, w3)` make the weighted corner sum, with blank counted as
  `0`, covariant for the character already defined. Source: cycle-14 N7
  and `OPPORTUNITY_QUEUE.md` item 16 before this cycle. The formation
  sentence was not given a note of its own.
- V2. Not on `origin/main`. Commands were `git grep` for `integer weight
  vector`, `weighted corner`, and `corner weight`, and for `blank counted
  as 0` and `even coordinate sum`, under `docs/*.md` and `scripts/*.py`.
  The corner-weight hits are physical cell cutting, a fermion
  Brillouin-zone corner, and a `C3` triplet. The even-sum hits are
  staggered-mass translations. None is this four-corner kernel.
  `git merge-tree --write-tree --name-only HEAD origin/main` exited 0
  with no conflict paths. The audit-metadata commit on `origin/main` was
  not merged.
- V3. Theorems 1 and 2 of the cycle-15 note, checked by the paired
  runner. The only solution is `0`. A basis is empty. The zero weight is
  not a flux. A separate blank weight, the site, and the rate remain
  open.
- V4. Before, every weight other than the alternating pattern was
  unclassified. After, the relation lattice is the even-sum sublattice
  of index `2`, and its integer orthogonal is `{0}`.
- V5. Not a corollary of the alternating-sum witness. That witness rejects
  one vector. It does not generate the relation lattice or divide the
  pivot `2`.

No-go gate for the scoped kernel is in the cycle-15 source note. The only
covariant corner weight is zero. A universal claim that no function of
the four colors can be covariant is not made. Author mutations, each on
a scratch copy that was deleted: demanding that the determinant be `1`
prints `FAIL=1`; demanding that the constant weight meet the required
value `-1` prints `FAIL=1`. Independent review has not been requested.
No audit grade.

Conformance sections touched by this author pass, not a review-loop verdict:
the note states its hypotheses, pins one runner and cache, keeps the
classification inside this four-integer family and the character already
defined, separates the kernel from the rank-3 orbit table, and does not
write an audit verdict. Sections that belong to independent review were
not run.

2026-10-10 cycle 14 author pass. Value gate, searched `origin/main` at
`d9b869b97944676aaa759915462c529dc276a04c`:

- V1. The queued discriminator is whether the alternating sum of the four
  corner values in boundary order, with blank counted as `0`, is covariant
  for the character already defined, and if so what its three coefficients
  are. Source: the campaign block after the rank-3 census, which forbade
  adopting a coefficient or forming an edge flux and left this sum
  unevaluated. The formation sentence was not given a note of its own.
- V2. Not on `origin/main`. Commands were `git grep` for `alternating sum`,
  `corner-preserving`, `covariant circulation`, `free module of rank 3`,
  and `blank counted as 0` under `docs/*.md` and `scripts/*.py`. The
  alternating-sum hits are a Weyl character, a charge-gas bound, and other
  carriers. None is this four-corner sum. `git merge-tree --write-tree
  --name-only HEAD origin/main` exited 0 with no conflict paths. The
  audit-metadata commit on `origin/main` was not merged.
- V3. Theorems 1 and 2 of the cycle-14 note, checked by the paired runner.
  The sum is not covariant. The witness is the half-turn
  `(x, y, z) ↦ (y, x, -z)` and the coloring `0101`, where the sum is `-2`
  rather than `+2`. No coefficient triple is assigned. The sum is not a
  flux. Other weight vectors, the site, and the rate remain open.
- V4. Before, this sum had not been tested against the character. After,
  it fails. The failure already occurs on a coloring with no blank.
- V5. Not a corollary of the rank-3 census. That census says a covariant
  assignment vanishes on `0101`. It does not evaluate this sum. The value
  `-2` is computed here.

No-go gate for the scoped miss is in the cycle-14 source note. The sum is
not covariant, and no coefficients are assigned. A universal claim that no
weight vector can be covariant is not made. Author mutations, each on a
scratch copy that was deleted: demanding that the image value on `0101`
equal `+2` prints `FAIL=1`; demanding that the number of failing pairs be
`0` prints `FAIL=1`. Independent review has not been requested. No audit
grade.

Conformance sections touched by this author pass, not a review-loop verdict:
the note states its hypotheses, pins one runner and cache, keeps the
negative claim inside this one assignment and the character already
defined, separates the witness from the rank-3 orbit table, and does not
write an audit verdict. Sections that belong to independent review were
not run.

2026-10-10 cycle 13 author pass. Value gate, searched `origin/main` at
`d9b869b97944676aaa759915462c529dc276a04c`:

- V1. The queued discriminator is whether proper-cubic covariance forces
  a unique nonzero circulation on the 81 colorings of one unit square by
  `{0, 1, blank}`, or whether every covariant assignment has circulation
  0 or a free sign. Source: the campaign block after the ternary-shell
  census, which closed the six-direction shell family and left the
  source/action gate open. The formation sentence was not given a note
  of its own.
- V2. Not on `origin/main`. Commands were `git grep` for `plaquette
  circulation`, `four corner records`, `81 color`, and `covariant
  circulation` under `docs/*.md` and `scripts/*.py`. The hits are a
  ring-model circulation matrix, a vector-magnetic null probe, fermion
  corner counts, and unrelated `3^4` arithmetic. None is this rank-3
  module. `git merge-tree --write-tree --name-only HEAD origin/main`
  exited 0 with no conflict paths. The audit-metadata commit on
  `origin/main` was not merged.
- V3. Theorems 1–3 of the cycle-13 note, checked by the paired runner.
  A menu that deletes blank corners, the site, and the rate remain open.
  No coefficient is adopted. No edge flux is formed.
- V4. Before, this square had no circulation census on this branch.
  After, the covariant integers have rank 3. Zero is covariant. The sign
  is free, and it is not the only freedom.
- V5. Not a corollary of the 729-shell census. That census classifies
  output orbits on six directions. It does not assign an integer
  circulation to four corner records.

No-go gate for the scoped miss is in the cycle-13 source note. The rank
is 3, not a unique nonzero value and not one global sign. A universal
claim that no carrier can constrain a circulation is not made. Author
mutations, each on a scratch copy that was deleted: demanding that
`0101` not be killed prints `FAIL=1`; demanding that the rank be 1
prints `FAIL=1`. Independent review has not been requested. No audit
grade.

Conformance sections touched by this author pass, not a review-loop verdict:
the note states its hypotheses, pins one runner and cache, keeps the
negative claim inside the four-corner character, separates the census
from the ring-model circulation matrix and the shell censuses, and does
not write an audit verdict. Sections that belong to independent review
were not run.

2026-10-10 cycle 12 author pass. Value gate, searched `origin/main` at
`d9b869b97944676aaa759915462c529dc276a04c`:

- V1. The queued discriminator is which shells with each axis direction
  in `{0, 1, blank}` have soldered output type `(1,)`, or a unique
  invariant probability on the six directions. Source: the campaign block
  after the one-blank census, which left two or more blanks outside and
  forbade a two-blank-only sequel. The formation sentence was not given
  a note of its own.
- V2. The 57-orbit count of the 729 profiles is on `origin/main`. It
  classifies support tables and a mirror count, not stabilizer output
  orbits. Commands were `git grep` for `729`, `57 proper`, `output type`,
  `unique invariant`, `bbbbbb`, and `singleton output` under `docs/*.md`.
  No hit names these seven output types or the three constant shells as
  the unique invariant laws. `git merge-tree` reported no content
  conflict. The audit-metadata commit on `origin/main` was not merged.
- V3. Theorems 1–3 of the cycle-12 note, checked by the paired runner.
  A menu that deletes blanks, the site, and the rate remain open. The
  uniform law is not adopted.
- V4. Before, shells with two or more blanks had no output-orbit census
  on this branch. After, no shell has type `(1,)`, and the only unique
  invariant laws are the uniform law on `000000`, `111111`, and `bbbbbb`.
- V5. Not a corollary of the one-blank census or of the binary census.
  Those censuses exclude part of the alphabet. The support-table count
  of 57 orbits does not name an invariant probability.

No-go gate for the scoped miss is in the cycle-12 source note. The
uniform law is forced only as a distribution on the three constant
shells, and it is not adopted. A universal claim that no menu can
constrain a direction is not made. Author mutations, each on a scratch
copy that was deleted: demanding that a point mass be invariant on
`bbbbbb` prints `FAIL=1`; demanding that the five-blank shells have
output type `(1,)` prints `FAIL=1`. Independent review has not been
requested. No audit grade.

Conformance sections touched by this author pass, not a review-loop verdict:
the note states its hypotheses, pins one runner and cache, keeps the
negative claim inside the soldered six-direction menu, separates the
census from the support-table count and the earlier shell censuses, and
does not write an audit verdict. Sections that belong to independent
review were not run.

2026-10-10 cycle 11 author pass. Value gate, searched `origin/main` at
`d9b869b97944676aaa759915462c529dc276a04c`:

- V1. The queued discriminator is whether a shell with one blank axis
  direction, and the other five entries in `{0,1}`, forces one locked
  direction under the soldered action. Source: the campaign block after
  the fully recorded binary census, which left a blank neighbor outside.
  The formation sentence was not given a note of its own.
- V2. Not on `origin/main`. Commands were `git grep` for `blank neighbor`,
  `exactly one blank`, `one blank direction`, and `blank direction` under
  `docs/*.md` and `scripts/*.py`. The hits are a channel probe with `I/2`,
  a priority rule, an algebra-action count, and unrelated output-type
  wording. None is this 12-orbit table. `git merge-tree` reported no
  content conflict. The audit-metadata commit on `origin/main` was not
  merged.
- V3. Theorems 1–3 of the cycle-11 note, checked by the paired runner.
  Two or more blanks, the site, and the rate remain open. Neither point
  mass is adopted.
- V4. Before, a one-blank shell had no such census on this branch. After,
  the blank and its antipode are both singleton output orbits, no shell
  forces one direction, and support size 1 occurs without being selected.
- V5. Not a corollary of the fully recorded binary census. That census
  excludes blanks. The constant-shell uniform law is not the unique law
  here.

No-go gate for the scoped miss is in the cycle-11 source note. Neither
point mass is adopted. A universal claim that no blank pattern can
constrain a possibility is not made. Author mutations, each on a scratch
copy that was deleted: demanding that the antipode point mass fail on
`00000b` exits `FAIL=1`; demanding that the `+x` point mass be invariant
on `00000b` exits `FAIL=1`. Independent review has not been requested. No
audit grade.

Conformance sections touched by this author pass, not a review-loop verdict:
the note states its hypotheses, pins one runner and cache, keeps the
negative claim inside the one-blank soldered menu, separates the census
from the binary-shell census and the bond-factor cycles, and does not
write an audit verdict. Sections that belong to independent review were
not run.

2026-10-10 cycle 10 author pass. Value gate, searched `origin/main` at
`d9b869b97944676aaa759915462c529dc276a04c`:

- V1. The queued discriminator is what one nearest-neighbor condition can
  force about which possibility a forming record locks, with the site and
  the rate left unsupplied. Source: the cycle-9 handoff, after the odd cap
  alphabet stopped, and the formation rule named as downstream supplier
  content. The formation sentence was not given a note of its own.
- V2. Not on `origin/main`. Commands were `git grep` for `forming record
  locks`, for binary-shell orbit phrases, and a reading of the Q8 parity
  pair, the soldering-menu broadcast bounds, and the antipodal fair-coin
  statement. None is this 10-orbit table. `git merge-tree` reported no
  content conflict. The audit-metadata commit on `origin/main` was not
  merged.
- V3. Theorems 1–4 of the cycle-10 note, checked by the paired runner.
  The two actions, blanks, the site, and the rate remain open.
- V4. Before, a binary shell had no such census on this branch. After,
  the constant shells force the uniform law of mass `1/6` under the
  soldered action, no shell forces one direction, and the unsoldered
  action leaves both labels available.
- V5. Not a corollary of the Q8 models, of the independent-broadcast
  bounds, or of the cap-factor cycles. The carrier is the shell, not a
  bond factor and not the directed correlation.

No-go gate for the scoped miss is in the cycle-10 source note. The uniform
law is forced only as a distribution on the constant shells, and it is not
adopted. A universal claim that no menu can constrain a possibility is not
made. Author mutations, each on a scratch copy that was deleted: demanding
that a point mass be invariant on the zero shell fails one check; demanding
that the `+x` bit agree with its quarter-turn image fails one check.
Independent review has not been requested. No audit grade.

Conformance sections touched by this author pass, not a review-loop verdict:
the note states its hypotheses, pins one runner and cache, keeps the
negative claim inside the two menus, separates the census from the earlier
bond-factor cycles, and does not write an audit verdict. Sections that
belong to independent review were not run.

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

2026-10-09 cycle 7 author pass. Value gate, searched `origin/main` at
`d9b869b97944676aaa759915462c529dc276a04c`:

- V1. The queued discriminator is whether every normalised
  soldered-covariant bond product on the orbit of `(0, 1, 2)` leaves
  `kappa` free, or whether covariance forces a value. Source: the cycle-6
  handoff, which left `kappa` unselected, and the campaign block that
  forbids inventing a forced value.
- V2. Not on `origin/main`. `git grep -l` for `soldered-covariant` hits
  only the order-blind note and its runner. `git grep` for
  `achiral_zero_one_two` returns no path. That note's factors keep `kappa`
  as a supplied scale.
- V3. Theorems 1–3 of the cycle-7 note, checked by the paired runner.
  The product shape, partial neighbour conditions, and the formation
  triple remain open.
- V4. Before, one axis-role product was normalised at a supplied
  `kappa = 1/2`. After, covariance does not contain `kappa`, normalisation
  at one nonzero value holds for every value or only at `0`, and both
  branches occur on this orbit. Strict positivity on the unit line is
  `|kappa| < 1`.
- V5. Not a corollary of repeating the cycle-6 path at another `kappa`.
  The expansion isolates powers for every `F` independent of `kappa`. The
  even sector is a family cycle 6 did not test. The path correlation is
  not recomputed.

No-go gate for the scoped shape is in the cycle-7 source note. The free
branch is nonempty. A universal claim that every nonlinear factor leaves
`kappa` free, or that `kappa` is forced to `0`, is not made. Author
mutations, each on a scratch copy that was deleted: demanding that the
even positive-cap indicator stay normalised at `kappa = 1` fails one
check; demanding that an odd pure line have a nonzero subset moment fails
one. Independent review has not been requested. No audit grade.

Conformance sections touched by this author pass, not a review-loop verdict:
the note states its hypotheses, pins one runner and cache, keeps the
negative claim inside the linear shape and the partial-neighbour reading,
separates the cocycle table from the raw quarter-turn product, and does
not write an audit verdict. Sections that belong to independent review
were not run.

2026-10-09 cycle 8 author pass. Value gate, searched `origin/main` at
`d9b869b97944676aaa759915462c529dc276a04c`:

- V1. The queued discriminator is whether a bond factor not of the shape
  `1 + kappa F` has partial normalisation selecting a unique parameter on
  the orbit of `(0, 1, 2)`. Source: cycle-7 N7 and `OPPORTUNITY_QUEUE.md`
  item 8 before this cycle.
- V2. Not on `origin/main`. `git grep` for `kappa^2` in `docs/*.md` hits
  Majorana flux comparators and curvature gates. `git grep` for
  `partner-cap` hits nothing. None is this pencil.
- V3. Theorems 1–4 of the cycle-8 note, checked by the paired runner.
  The formation triple remains open. `t = 1/2` is not a selected law.
- V4. Before, a second power was an unclassified escape. After, every
  independent pencil in the box normalises at `0`, and the three
  cardinalities are `32`, `256`, and `208`.
- V5. Not a corollary of the linear split. That split says a nonempty
  finite set of nonzero values cannot occur for `1 + kappa F`. The balance
  pencil is normalised exactly at `{0, 1/2}`.

No-go gate for the scoped box is in the cycle-8 source note. A universal
claim that no nonlinear factor isolates a parameter is not made. Author
mutations, each on a scratch copy that was deleted: demanding that the
balance pencil normalise only at `0` fails one check; demanding that the
opposite-`z` excess vanish for every coefficient pair fails one.
Independent review has not been requested. No audit grade.

Conformance sections touched by this author pass, not a review-loop verdict:
the note states its hypotheses, pins one runner and cache, keeps the
negative claim inside the coefficient box and the partial-neighbour
reading, separates the dependent linear shape from the independent census,
and does not write an audit verdict. Sections that belong to independent
review were not run.

2026-10-09 cycle 9 author pass. Value gate, searched `origin/main` at
`d9b869b97944676aaa759915462c529dc276a04c`:

- V1. The queued discriminator is whether one soldered bond factor on the
  odd cap lines, not equal to the constant `1` at the parameter origin, has
  a unique nonzero partial-normalisation value. Source: cycle-8 N7 and
  `OPPORTUNITY_QUEUE.md` item 9 before this cycle.
- V2. Not on `origin/main`. `git grep` for `odd cap`, for
  `orbit of (0, 1, 2)`, and for `partner-cap` hits nothing under the
  searched docs. The one `unique nonzero` hit is a K-reality predicate
  note, not this factor.
- V3. Theorems 1–3 of the cycle-9 note, checked by the paired runner.
  The formation triple remains open. `t = 1/2` is not a selected law.
- V4. Before, a non-constant value at `t = 0` was an unclassified escape.
  After, the declared factor is normalised exactly at `t = 1/2`, where
  `phi = 1 + (3/4) B^Y` and the bond values are strictly positive.
- V5. Not a corollary of the quadratic box. Every independent pencil in
  that box is normalised at `0`. This factor is not normalised at `0`.

No-go gate for the scoped factor is in the cycle-9 source note. A universal
claim that every shifted factor isolates a parameter is not made. Author
mutations, each on a scratch copy that was deleted: demanding that the
factor fail normalisation at `t = 1/2` fails one check; demanding that
`t^2 - t + 1` vanish at `t = 1` fails one. Independent review has not been
requested. No audit grade.

Conformance sections touched by this author pass, not a review-loop verdict:
the note states its hypotheses, pins one runner and cache, keeps the
existence claim inside this one factor and the partial-neighbour reading,
separates the supplied root from a selected interaction, and does not
write an audit verdict. Sections that belong to independent review were
not run.
