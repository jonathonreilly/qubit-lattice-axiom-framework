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

## Cycle 3 search

Refreshed `origin/main` immediately before the search. Commit
`d9b869b97944676aaa759915462c529dc276a04c`.

Command and what it returned:

- `git grep` on `origin/main` for `directed six`, `c_21-c_12`, and
  `directed stabilizer` in markdown and Python. The hits are unrelated
  historic notes. No CHSH evaluation of the directed coefficient pattern.

Classification: open after that search. The executed route is the elementary
CHSH square of the declared directed density, plus the signed-axis
enumeration. The formation triple stays queued.

## Cycle 4 search

Refreshed `origin/main` immediately before the search. Commit
`d9b869b97944676aaa759915462c529dc276a04c`.

The formation sentence is still present. It is quoted in `HANDOFF.md` and
was not given a note of its own.

Commands and what they returned, for the readout-weight pivot:

- `git grep` for `readout weight` with `twist`, for `symmetric readout`,
  and for `w_yx`, under `docs/*.md`. Hits are complementation, Wilson
  lines, and a clock no-go. None is this correlation matrix.
- `git grep` for `diag(1,-1,1)` and `improper reflection`. One historic
  intake uses `diag(1,1,-1)` as an input to a different kill. It is not
  the action of `diag(1,-1,1)` on `T`.
- `git grep` for `one-site reduction` and `partial trace` on the directed,
  CHSH, bond, twist, and Moriya notes. No hit.
- Title scan for readout-weight notes. The June selector-tangent prototype
  is a different carrier.

Classification: open after that matched-hit review. The executed route is
the partial trace and the coordinate-weight coefficient of `t`. The
conjugation by `P` is included. No CHSH square is part of the route. The
formation triple stays unsupplied.

## Cycle 5 search

Refreshed `origin/main` immediately before the search. Commit
`d9b869b97944676aaa759915462c529dc276a04c`. No content conflict with this
branch. The one main-only commit is audit metadata and was not merged.

Commands and what they returned:

- `git grep` for quadratic invariant polynomials, for `Q_T2`, and for
  `6(u-v)` under `docs/*.md` on `origin/main`. No statement of this
  four-channel basis or of the directed substitution.
- The cubic-anisotropy note of 2026-06-17 states a two-weight count on the
  traceless symmetric block `Sym^2_0(R^3)` only. It uses a floating-point
  argument and a lattice harmonic. It does not row-reduce the nine entries.
- `git grep` for `c_21-c_12` under `docs/*.md` and `scripts/*.py` on
  `origin/main` returned no path. The directed pattern is on this branch.
- A dilute-thermodynamics note names different pair amplitudes inside a
  different Hamiltonian. It is not this nullspace.

Classification: open after that matched-hit review. The executed route is
the degree-2 invariant space of one `3×3` correlation and its restriction
to the directed pattern. No CHSH square and no readout weight is part of
the route. The formation triple stays unsupplied.

## Cycle 6 search

Refreshed `origin/main` immediately before the search. Commit
`d9b869b97944676aaa759915462c529dc276a04c`. No content conflict with this
branch. The one main-only commit is audit metadata and was not merged.

Commands and what they returned:

- `git grep` for `orbit of (0, 1, 2)` under `docs/*.md` and `scripts/*.py`
  on `origin/main`. No path.
- `git grep` for `(0, 1, 2)` inside the order-blind note of 2026-09-22.
  No path. That note's chiral pair is the mirror union of `(1, 2, 3)`.
- The boundary sentence of that note still says generic orbits beyond the
  exhibited rules, higher-rank bond spaces, and mixed alphabets are not
  classified.
- A degree-3 count of the cycle-5 matrix was not opened. It is the same
  carrier.

Classification: open after that matched-hit review. The executed route is
the proper orbit of `(0, 1, 2)` and one axis-role bond product. No CHSH
square, no readout weight, and no polynomial of the bond matrix is part of
the route. The formation triple stays unsupplied.

## Cycle 7 search

Refreshed `origin/main` immediately before the search. Commit
`d9b869b97944676aaa759915462c529dc276a04c`. No content conflict with this
branch. The one main-only commit is audit metadata and was not merged.

Commands and what they returned:

- `git grep -l` for `soldered-covariant` on `origin/main` under `docs` and
  `scripts`. The hits are the order-blind note of 2026-09-22 and its
  runner. That note leaves `kappa` as a supplied scale on the exhibited
  factors and does not decide the orbit of `(0, 1, 2)`.
- `git grep` for `achiral_zero_one_two` on `origin/main`. No path. The
  cycle-6 note is on this branch only.
- `git merge-tree` against `origin/main` reported no content conflict.

Classification: open after that matched-hit review. The executed route is
the homogeneous expansion of `1 + kappa F` and the quarter-turn sectors on
this orbit. No path correlation is part of the route. The formation triple
stays unsupplied.

## Cycle 8 search

Refreshed `origin/main` immediately before the search. Commit
`d9b869b97944676aaa759915462c529dc276a04c`. No content conflict with this
branch. The one main-only commit is still audit metadata and was not merged.

Commands and what they returned:

- `git grep` for `kappa^2` and `t^2 G` on `origin/main` under `docs/*.md`.
  The hits are Majorana flux comparators and curvature gates. None is a
  bond factor on the orbit of `(0, 1, 2)`.
- `git grep` for `partner-cap` on `origin/main` under `docs/*.md`. No path.
- `git merge-tree` against `origin/main` reported no content conflict.

Classification: open after that matched-hit review. The executed route is
the quadratic pencil in the span of the two odd cap lines, inside one
coefficient box. No path correlation is part of the route. The formation
triple stays unsupplied. A factor that is not `1` at `t = 0` is cycle 9.

## Cycle 9 search

Refreshed `origin/main` immediately before the search. Commit
`d9b869b97944676aaa759915462c529dc276a04c`. No content conflict with this
branch. The one main-only commit is still audit metadata and was not merged.

Commands and what they returned:

- `git grep -l` for `odd cap` on `origin/main` under `docs/*.md` and
  `scripts/*.py`. No path.
- `git grep -l` for `orbit of (0, 1, 2)` on `origin/main` under `docs/*.md`.
  No path.
- `git grep -l` for `partner-cap` on `origin/main` under `docs/*.md`. No path.
- `git grep -l` for `unique nonzero` on `origin/main` under `docs/*.md`.
  One hit, `docs/KREALITY_PREDICATE_ONE_SHARED_ATOM_ONE_CONSUMER_BOUNDED_NOTE_2026-06-12.md`.
  That note is not this bond factor.
- `git merge-tree` against `origin/main` reported no content conflict.

Classification: open after that matched-hit review. The executed route is
one shifted factor on the two odd cap lines. No path correlation is part
of the route. The formation triple stays unsupplied. The odd cap alphabet
stops. Another pencil is not queued. The following block's supplier is
the formation rule.

## Cycle 10 search

Refreshed `origin/main` immediately before the search. Commit
`d9b869b97944676aaa759915462c529dc276a04c`. No content conflict with this
branch. The one main-only commit is still audit metadata and was not merged.
`git merge-tree` reported no `CONFLICT` and no `changed in both`.

Commands and what they returned:

- `git grep` for `forming record locks` on `origin/main` under `docs/*.md`.
  The hits quote reading note (2) or, in the Cycle-913 selection note,
  apply a stipulated fingerprint table. None is a census of binary shells.
- `git grep` for `orbits on {0,1}`, `binary six-neighbor`, `six-bit orbits`,
  `1024 covariant`, and `constant on orbits` under `docs/*.md` and
  `scripts/*.py`. The six-bit hits are D4 capacity notes and receiver
  tables. The constant-on-orbits hits are unrelated scripts. No path states
  this 10-orbit table.
- The Q8 conditional-law note of 2026-08-13 uses one parity bit of a
  six-neighbor shell and two supplied output measures. It does not list
  the stabilizer orbits.
- The soldering-menu note of 2026-09-22 bounds an independent broadcast.
  It is not this conditional lock.
- The menus-and-Born note forces a fair coin for one antipodal pair of
  recorded Bloch vectors. That carrier is not a binary shell.

Classification: open after that matched-hit review. The executed route is
the 64 binary shells and the two supplied output actions. No bond factor
and no `3×3` correlation is part of the route. The site and the rate stay
unsupplied. The odd cap alphabet stays stopped.

## Cycle 11 search

Refreshed `origin/main` immediately before the search. Commit
`d9b869b97944676aaa759915462c529dc276a04c`. No content conflict with this
branch. The one main-only commit is still audit metadata and was not merged.
`git merge-tree` reported no `CONFLICT` and no `changed in both`.

Commands and what they returned:

- `git grep` for `blank neighbor`, `exactly one blank`, `one blank
  direction`, and `blank direction` on `origin/main` under `docs/*.md` and
  `scripts/*.py`. The markdown hits are the affine channel probe, in which
  a blank slot contributes `I/2`; the priority-formation note, which
  orients an edge toward a blank neighbor; the algebra-action note, which
  counts initially blank neighbors; and an extensional-rule phrase. None
  is a 12-orbit census of one-blank shells.
- `git grep` for `output type` under the same paths. The hits are stretch
  labels and other carriers, not stabilizer orbits of a one-blank shell.
- The reading-note sentence in `docs/MINIMAL_AXIOMS_2026-06-29.md` still
  withholds the formation site, probability, and rate. It is not this
  census.
- Cycle 10 on this branch leaves a blank neighbor outside its binary
  census. It does not compute these orbits.

Classification: open after that matched-hit review. The executed route is
the 192 one-blank shells and the soldered six-direction action. No bond
factor and no unsoldered label is part of the route. The site and the rate
stay unsupplied. The odd cap alphabet stays stopped. Two or more blanks
stay outside.
