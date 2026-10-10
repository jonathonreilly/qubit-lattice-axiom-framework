# Handoff — toe-nn-law-values-20261009

Base `17a95e60d85`. Branch `physics-loop/toe-nn-law-values-20261009`.
Stop at `2026-10-10T12:02:06Z`. One worktree only:
`/Users/jonreilly/.grok/campaigns/toe-24h-20261009/wt`.

## Formation sentence, still present

`origin/main` at `d9b869b97944676aaa759915462c529dc276a04c`, in
`docs/MINIMAL_AXIOMS_2026-06-29.md`, reading note (2), still says: "Read
with Record, the distribution concerns which possibility a forming record
locks, conditional on formation at that site; it does not supply the
formation site, probability, or rate." The open-gate list still names
"source/action and physical-observable identification." No note was opened
that only repeats those sentences. No hazard law was invented. Cycle 17
does not close the source/action gate. It asks a different question:
whether the proper orbit of the record value `(1, 1, 2)` equals its orbit
under the full signed-permutation group, including one improper mirror.
The site and the rate stay out of the object. This is the last science
block.

## Done this cycle

Cycles 1–16 are unchanged. Their runners remain `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=55 FAIL=0`, `TOTAL: PASS=102 FAIL=0`,
`TOTAL: PASS=61 FAIL=0`, `TOTAL: PASS=44 FAIL=0`,
`TOTAL: PASS=16 FAIL=0`, `TOTAL: PASS=30 FAIL=0`, `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=28 FAIL=0`, `TOTAL: PASS=13 FAIL=0`, `TOTAL: PASS=13 FAIL=0`,
`TOTAL: PASS=12 FAIL=0`, `TOTAL: PASS=12 FAIL=0`, `TOTAL: PASS=8 FAIL=0`,
`TOTAL: PASS=6 FAIL=0`, and `TOTAL: PASS=6 FAIL=0`. Do not repeat the CHSH
specializations, the readout split, the four quadratic channels, the
achiral-orbit path factor, the linear split of `1 + kappa F`, the
quadratic coefficient box, the shifted cap factor, the fully recorded
binary census, the one-blank census, the 729-shell census, the rank-3
circulation census, the alternating-sum witness, the four-weight theorem,
or the shared symbol pair.

Cycle 17 searched `origin/main` at `d9b869b97944676aaa759915462c529dc276a04c`
for a comparison of the proper orbit of `(1, 1, 2)` with its full
signed-permutation orbit. `git grep` for `(1, 1, 2)` together with orbit
or mirror, under `docs/*.md` and `scripts/*.py`, does not state that
comparison. The achiral note on this branch states it for `(0, 1, 2)` and
explicitly does not classify `(1, 1, 2)`. No merge with `origin/main` was
made: `git merge-tree --write-tree --name-only HEAD origin/main` exited 0
and listed no conflict paths. The one main-only commit is audit metadata.

On the same signed-permutation action:

- the full set has order `48`, and the determinant `+1` subgroup has order `24`
- the proper orbit of `(1, 1, 2)` has `24` points and equals the full orbit
- the improper mirror `[[0, 1, 0], [1, 0, 0], [0, 0, 1]]` fixes the seed
- that mirror carries every improper image into the proper orbit
- the orbit is exactly the `24` vectors of absolute values `1, 1, 2`
- the stabilizer has order `2`, and only the identity is proper
- a proper cycle sends the seed to `(2, 1, 1)`
- a proper matrix sends the seed to `(1, 1, -2)`
- `diag(-1, 1, 1)` does not fix this seed

The two orbits are equal. The orbit is not a chiral pair. The equality is
not a selected law and not a mass density. This does not derive a source
identification or a formation rate. The orbit of `(1, 2, 2)` was not
enumerated. The corner-weight family stays stopped. The odd cap alphabet
stays stopped. The six-direction shell family stays closed.

Runner: `TOTAL: PASS=6 FAIL=0`.

## Earlier cycle 16, unchanged

Cycles 1–15 are unchanged. Their runners remain `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=55 FAIL=0`, `TOTAL: PASS=102 FAIL=0`,
`TOTAL: PASS=61 FAIL=0`, `TOTAL: PASS=44 FAIL=0`,
`TOTAL: PASS=16 FAIL=0`, `TOTAL: PASS=30 FAIL=0`, `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=28 FAIL=0`, `TOTAL: PASS=13 FAIL=0`, `TOTAL: PASS=13 FAIL=0`,
`TOTAL: PASS=12 FAIL=0`, `TOTAL: PASS=12 FAIL=0`, `TOTAL: PASS=8 FAIL=0`,
and `TOTAL: PASS=6 FAIL=0`. Do not repeat the CHSH specializations, the
readout split, the four quadratic channels, the achiral-orbit path
factor, the linear split of `1 + kappa F`, the quadratic coefficient
box, the shifted cap factor, the fully recorded binary census, the
one-blank census, the 729-shell census, the rank-3 circulation census,
the alternating-sum witness, or the four-weight theorem.

Cycle 16 searched `origin/main` at `d9b869b97944676aaa759915462c529dc276a04c`
for a classification of one shared integer `u` on color `1` and one
shared integer `v` on blank. The hits that mention a blank corner are a
terminal-site channel. The hits that mention color `1` are a species
assignment. `boundary-sign` hits are a Ward overlap and a Maxwell
generator. `corner-preserving`, `blank counted`, `blank weight`, and
`contribute an integer` are absent. None evaluates this shared pair
against the boundary-sign character. No merge with `origin/main` was
made: `git merge-tree --write-tree --name-only HEAD origin/main` exited 0
and listed no conflict paths. The one main-only commit is audit metadata.

On the same unit square:

- the sum is `u N_1 + v N_b`, with color `0` contributing `0`
- every corner-preserving isometry permutes the four colors, so the sum
  is unchanged
- the residual is `(1 - χ) φ`; preserving elements contribute only `0`
- the other diagonal half turn has character `-1`, so `φ` vanishes on
  every coloring
- `1000` forces `u = 0` and `b000` forces `v = 0`
- the two unit rows are the identity, of determinant `1` and index `1`
- the four-blank row `(0, 4)` is dependent, and its quotient is `0`
- `(1, 0)` sends `1000` from `1` to `1` under that reversal, not to `-1`
- `(0, 1)` does the same on `b000` and `00b0`
- `(1, -1)` vanishes on `1b00` and still fails on `1000`

The only solution is `(0, 0)`. A basis is empty. The zero pair is not a
flux. No coefficient is a mass density. This does not derive a source
identification or a formation rate. The corner-weight family stops. A
third color, a fifth corner, another per-corner weight, and a menu that
deletes blank corners are not opened. The odd cap alphabet stays stopped.
The six-direction shell family stays closed.

Runner: `TOTAL: PASS=6 FAIL=0`.

## Earlier cycle 15, unchanged

Cycles 1–14 are unchanged. Their runners remain `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=55 FAIL=0`, `TOTAL: PASS=102 FAIL=0`,
`TOTAL: PASS=61 FAIL=0`, `TOTAL: PASS=44 FAIL=0`,
`TOTAL: PASS=16 FAIL=0`, `TOTAL: PASS=30 FAIL=0`, `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=28 FAIL=0`, `TOTAL: PASS=13 FAIL=0`, `TOTAL: PASS=13 FAIL=0`,
`TOTAL: PASS=12 FAIL=0`, `TOTAL: PASS=12 FAIL=0`, and
`TOTAL: PASS=8 FAIL=0`. Do not repeat the CHSH specializations, the
readout split, the four quadratic channels, the achiral-orbit path
factor, the linear split of `1 + kappa F`, the quadratic coefficient
box, the shifted cap factor, the fully recorded binary census, the
one-blank census, the 729-shell census, the rank-3 circulation census,
or the alternating-sum witness.

Cycle 15 searched `origin/main` at `d9b869b97944676aaa759915462c529dc276a04c`
for a classification of integer weights `(w0, w1, w2, w3)` on the four
corners, with blank counted as `0`. The corner-weight hits are physical
cell cutting, a fermion Brillouin-zone corner, and a `C3` triplet. None
evaluates this weighted sum against the boundary-sign character. The
even-coordinate-sum hits are staggered-mass translations, not this
relation lattice. No merge with `origin/main` was made: `git merge-tree
--write-tree --name-only HEAD origin/main` exited 0 and listed no
conflict paths. The one main-only commit is audit metadata.

On the same unit square:

- covariance of `sum_i w_i n(c_i)` is the 32 equations `w_{π(i)} = χ(π) w_i`
- every equation row has even coordinate sum, so the relation lattice sits
  in the index-2 even-sum sublattice
- four named rows have determinant `-2` and generate that sublattice
- exact division of the triangular pivot `2` returns the quotient `0`
- the only integer solution is `(0,0,0,0)`, and a basis is empty
- the constant weight `(1,1,1,1)` sends the count on `1000` from `1` to
  `1` under the other diagonal half turn, whose character is `-1`

The zero weight is not a flux. No corner entry is a mass density. This
does not derive a source identification or a formation rate. A separate
integer weight for blank stays unclassified. The odd cap alphabet stays
stopped. The six-direction shell family stays closed. A menu that deletes
blank corners stays outside.

Runner: `TOTAL: PASS=6 FAIL=0`.

## Earlier cycle 14, unchanged

Cycles 1–13 are unchanged. Their runners remain `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=55 FAIL=0`, `TOTAL: PASS=102 FAIL=0`,
`TOTAL: PASS=61 FAIL=0`, `TOTAL: PASS=44 FAIL=0`,
`TOTAL: PASS=16 FAIL=0`, `TOTAL: PASS=30 FAIL=0`, `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=28 FAIL=0`, `TOTAL: PASS=13 FAIL=0`, `TOTAL: PASS=13 FAIL=0`,
`TOTAL: PASS=12 FAIL=0`, and `TOTAL: PASS=12 FAIL=0`. Do not repeat the
CHSH specializations, the readout split, the four quadratic channels, the
achiral-orbit path factor, the linear split of `1 + kappa F`, the
quadratic coefficient box, the shifted cap factor, the fully recorded
binary census, the one-blank census, the 729-shell census, or the
rank-3 circulation census.

Cycle 14 searched `origin/main` at `d9b869b97944676aaa759915462c529dc276a04c`
for an evaluation of the alternating sum of four corner values in
`{0, 1, blank}`, with blank counted as `0`. The alternating-sum hits are
a Weyl character, a charge-gas bound, and other carriers. None evaluates
this sum against the boundary-sign character. Cycle 13 on this branch
defines that character and does not form the sum. No merge with
`origin/main` was made: `git merge-tree --write-tree --name-only HEAD
origin/main` exited 0 and listed no conflict paths. The one main-only
commit is audit metadata.

On the same unit square:

- the assignment is `n(c0) - n(c1) + n(c2) - n(c3)`, with `n(b) = 0`
- the half-turn `(x, y, z) ↦ (y, x, -z)` preserves the square, has
  character `-1`, and fixes `0101`
- the alternating sum on `0101` is `-2`, not the required `+2`
- that coloring has no blank, so the failure is not the blank convention
- the same half-turn fixes 27 colorings, and the sum is nonzero on 18
- the corner-permutation sign of this half-turn is also `-1` and does
  not repair the witness
- the quarter turn `x ↦ (1 - y, x, z)` sends the sum of `1000` from `1`
  to `-1`
- the character identity fails on 192 pairs
- no coefficient triple on `001b`, `011b`, and `01bb` is assigned

The sum is not a flux. No corner entry is a mass density. This does not
derive a source identification or a formation rate. Other integer weight
vectors on the four corners stay unclassified. The odd cap alphabet stays
stopped. The six-direction shell family stays closed. A menu that deletes
blank corners stays outside.

Runner: `TOTAL: PASS=8 FAIL=0`.

## Earlier cycle 13, unchanged

Cycles 1–12 are unchanged. Their runners remain `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=55 FAIL=0`, `TOTAL: PASS=102 FAIL=0`,
`TOTAL: PASS=61 FAIL=0`, `TOTAL: PASS=44 FAIL=0`,
`TOTAL: PASS=16 FAIL=0`, `TOTAL: PASS=30 FAIL=0`, `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=28 FAIL=0`, `TOTAL: PASS=13 FAIL=0`, `TOTAL: PASS=13 FAIL=0`,
and `TOTAL: PASS=12 FAIL=0`. Do not repeat the CHSH specializations, the
readout split, the four quadratic channels, the achiral-orbit path
factor, the linear split of `1 + kappa F`, the quadratic coefficient box,
the shifted cap factor, the fully recorded binary census, the one-blank
census, or the 729-shell census.

Cycle 13 searched `origin/main` at `d9b869b97944676aaa759915462c529dc276a04c`
for a census of covariant circulations on the 81 colorings of one unit
square. The hits that mention plaquette circulation are a ring-model
matrix kernel, a vector-magnetic null probe, and fermion corner-record
counts. None is this 81-coloring module. No merge with `origin/main` was
made: `git merge-tree --write-tree --name-only HEAD origin/main` exited 0
and listed no conflict paths. The one main-only commit is audit metadata.

On one unit square with each corner in `{0, 1, blank}`:

- exactly 8 proper isometries preserve the four corners; they are the
  dihedral group, and the circulation character is the boundary sign
- the 81 colorings form 21 orbits; enumeration and the Burnside average
  agree, and the group sum is `168`
- 57 colorings, in 18 orbits, are fixed by a reversing isometry, and
  every covariant integer assignment vanishes on them
- the alternating coloring `0101` is one of those zeros
- the free orbits are `001b`, `011b`, and `01bb`, each of size 8
- the covariant assignments are a free module of rank 3
- zero is covariant, `-φ` is covariant whenever `φ` is, and the `01bb`
  generator is not a sign flip of the `001b` generator

No coefficient is a selected circulation. No edge flux was formed. This
does not derive a source identification or a formation rate. The odd cap
alphabet stays stopped. The six-direction shell family stays closed. A
menu that deletes blank corners stays outside.

Runner: `TOTAL: PASS=12 FAIL=0`.

## Earlier cycle 12, unchanged

Cycles 1–11 are unchanged. Their runners remain `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=55 FAIL=0`, `TOTAL: PASS=102 FAIL=0`,
`TOTAL: PASS=61 FAIL=0`, `TOTAL: PASS=44 FAIL=0`,
`TOTAL: PASS=16 FAIL=0`, `TOTAL: PASS=30 FAIL=0`, `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=28 FAIL=0`, `TOTAL: PASS=13 FAIL=0`, and
`TOTAL: PASS=13 FAIL=0`. Do not repeat the CHSH specializations, the
readout split, the four quadratic channels, the achiral-orbit path
factor, the linear split of `1 + kappa F`, the quadratic coefficient box,
the shifted cap factor, the fully recorded binary census, or the
one-blank census.

Cycle 12 searched `origin/main` at `d9b869b97944676aaa759915462c529dc276a04c`
for a census of which ternary shells have soldered output type `(1,)` or
a unique invariant probability on the six directions. The 729 profiles
and their 57 proper-cubic orbits are already recorded, for support tables
and for a mirror count. None of those notes names the stabilizer output
types or the three constant shells as the unique invariant laws. No merge
with `origin/main` was made: `git merge-tree` reported no content
conflict. The one main-only commit is audit metadata.

On one shell with each of the six directions in `{0, 1, blank}`:

- the 729 shells form 57 orbits; enumeration and the Burnside average
  agree, and the group sum is `1368`
- the output types are `(6)`, `(4,2)`, `(3,3)`, `(4,1,1)`, `(2,2,2)`,
  `(2,2,1,1)`, and `(1,1,1,1,1,1)`, with shell counts `3`, `18`, `24`,
  `54`, `114`, `108`, and `408`
- no shell has output type `(1,)`
- singleton output orbits occur as none, one antipodal pair, or all six,
  on `159`, `162`, and `408` shells
- the unique invariant laws are the uniform law of mass `1/6` on
  `000000`, `111111`, and `bbbbbb`
- the 664 shells with one through five blanks have no unique invariant
  law
- the twelve five-blank shells have type `(4,1,1)`; on `bbbb0b` both pole
  point masses transport and disagree

The uniform law is not a selected possibility. Neither five-blank point
mass is selected. This does not derive a source identification or a
formation rate. The odd cap alphabet stays stopped. A menu that deletes
blank directions stays outside.

Runner: `TOTAL: PASS=12 FAIL=0`.

## Earlier cycle 11, unchanged

Cycles 1–10 are unchanged. Their runners remain `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=55 FAIL=0`, `TOTAL: PASS=102 FAIL=0`,
`TOTAL: PASS=61 FAIL=0`, `TOTAL: PASS=44 FAIL=0`,
`TOTAL: PASS=16 FAIL=0`, `TOTAL: PASS=30 FAIL=0`, `TOTAL: PASS=31 FAIL=0`,
`TOTAL: PASS=28 FAIL=0`, and `TOTAL: PASS=13 FAIL=0`. Do not repeat the
CHSH specializations, the readout split, the four quadratic channels, the
achiral-orbit path factor, the linear split of `1 + kappa F`, the quadratic
coefficient box, the shifted cap factor, or the fully recorded binary
census.

Cycle 11 searched `origin/main` at `d9b869b97944676aaa759915462c529dc276a04c`
for a census of shells with exactly one blank axis direction under the 24
proper cubic rotations. The hits that mention a blank neighbor are a
channel probe, a priority rule, and an algebra-action count. None is this
census. No merge with `origin/main` was made: `git merge-tree` reported no
content conflict. The one main-only commit is audit metadata.

On one shell with exactly one blank and the other five entries in `{0,1}`:

- the 192 shells form 12 orbits, sizes `6, 6, 6, 6, 12, 12`, and six orbits
  of size `24`
- enumeration and the Burnside average agree; the group sum is `288`
- the blank direction and its antipode are singleton output orbits on
  every shell
- the output types are `(4,1,1)`, `(2,2,1,1)`, and `(1,1,1,1,1,1)`, with
  `24`, `24`, and `144` shells
- no shell has output type `(1,)`, and no shell has a unique invariant law
- the point mass on the blank and the point mass on the antipode both
  transport, and they disagree on every shell
- support size 1 occurs, so it is false that every covariant conditional
  has support larger than one point
- neither point mass is selected, and the uniform law is not the only
  invariant law

This does not derive a source identification or a formation rate. The odd
cap alphabet stays stopped. Shells with two or more blanks stay outside.

Runner: `TOTAL: PASS=13 FAIL=0`.

## Earlier cycle 10, unchanged

Cycle 10 searched `origin/main` at `d9b869b97944676aaa759915462c529dc276a04c`
for a census of fully recorded `{0,1}` shells under the 24 proper cubic
rotations, and for what those shells force about a locked possibility.
The hits that quote the formation sentence are not that census. The Q8
parity pair, the independent-broadcast bounds, and the antipodal fair-coin
statement are different carriers. No merge with `origin/main` was made:
`git merge-tree` reported no content conflict. The one main-only commit is
audit metadata.

On one fully recorded binary shell, with no blank slot:

- the 64 shells form 10 orbits, sizes `1, 1, 3, 3, 6, 6, 8, 12, 12, 12`
- enumeration and the Burnside average agree
- under the soldered six-direction menu, the two constant shells force
  the uniform law of mass `1/6`, support size 6
- no shell has output type `(1,)`, and singleton output orbits occur only
  in pairs, so no shell forces one direction
- the shell `000001` admits both pole point masses and rejects an
  equatorial point mass
- under the unsoldered two-label menu there are `1024` covariant
  deterministic laws, and `511` varying laws lock each label at each shell
- the `+x` bit is not covariant

The uniform law is not a selected possibility. Neither action is adopted.
This does not derive a source identification or a formation rate. The odd
cap alphabet stays stopped.

Runner: `TOTAL: PASS=13 FAIL=0`.

## Earlier cycle 9, unchanged

Cycle 9 searched `origin/main` at `d9b869b97944676aaa759915462c529dc276a04c`
for a shifted bond factor on the odd cap lines of `(0, 1, 2)`. There is no
such note on `origin/main`. No merge with `origin/main` was made:
`git merge-tree` reported no content conflict.

On the one soldered factor

```text
phi(t) = 1 + (1 - 2 t) B^X + (t^2 - t + 1) B^Y
```

with partial neighbour conditions:

- `phi(0) = 1 + B^X + B^Y` is not the constant factor `1`
- partial normalisation holds at exactly one real value, `t = 1/2`
- there `phi = 1 + (3/4) B^Y`, with bond values `1/4`, `1`, and `7/4`
- the coefficient vectors at `0` and at `1` have determinant `2`, so this
  is not the shape `1 + kappa(t) H`
- `t = 1/2` is the root of the supplied polynomial `1 - 2 t`

`t = 1/2` is not a selected interaction. Covariance holds at every `t`.
This does not derive a source identification or the formation triple. The
odd cap alphabet stops. Another pencil is not queued. The supplier for a
following block is the formation rule, not a bond factor.

Runner: `TOTAL: PASS=28 FAIL=0`.

## Earlier cycle 8, unchanged

Cycle 8 searched `origin/main` at `d9b869b97944676aaa759915462c529dc276a04c`
for a quadratic partner-cap pencil on this alphabet. The `kappa^2` hits are
Majorana and curvature comparators, not this bond factor. No merge with
`origin/main` was made: `git merge-tree` reported no content conflict.

On pencils `1 + t (a X + b Y) + t^2 (c X + d Y)` with `X` and `Y` the odd
cap lines, coefficients in `{-2,-1,0,1,2}`, and partial neighbour
conditions:

- determinant `0` is the old shape `1 + kappa H` and is excluded (`129` tuples)
- the other `496` tuples always normalise at `t = 0`
- a nonzero rational is never the unique normalised value
- the counts are `32` only at `0`, `256` at two rationals, and `208` at three
- `(1, 0, 0, 1)` is only at `0`
- `(1, 1, 0, -2)` is exactly `{0, 1/2}`, and both are strictly positive
- `(1, 1, -1, -2)` is exactly `{0, 1/2, 1}`

`t = 1/2` is not a selected interaction. The constant rule remains. This
does not derive a source identification or the formation triple. The factor
that is not `1` at the parameter origin is cycle 9, not a second pass
through this box.

Runner: `TOTAL: PASS=31 FAIL=0`.

## Earlier cycle 7, unchanged

Cycle 7 searched that same `origin/main` commit for a result that already
decides whether soldered covariance forces `kappa` on the orbit of
`(0, 1, 2)`. It does not. The order-blind note still leaves generic orbits
unclassified, and its exhibited factors leave `kappa` as a supplied scale.
No merge with `origin/main` was made: the one newer main commit is audit
metadata, and `git merge-tree` reported no content conflict.

On bond factors `1 + kappa F` with `F` independent of `kappa`, and with
partial neighbour conditions:

- covariance at a nonzero `kappa` does not contain `kappa`
- normalisation at one nonzero `kappa` holds if and only if it holds for
  every `kappa`
- no such product is normalised exactly on a nonempty finite set of
  nonzero values
- on the proper orbit of `(0, 1, 2)`, nonzero even quarter-turn families
  normalise only at `kappa = 0`
- each odd pure quarter-turn orbit line normalises for every `kappa`
- the unit positive-cap line is the axis-role bond product of cycle 6,
  and strict positivity on it is the interval `|kappa| < 1`
- the bond factor of a pure line depends on `kappa c^2`, not on a
  preferred pair `(kappa, c)`

`kappa` is not selected. This does not derive a source identification or
the formation triple. Cycle 8 takes the second-power steelman inside one
box and does not select a unique nonzero `t`. The orbits of `(1, 1, 2)`
and `(1, 2, 2)` stay open.

Runner: `TOTAL: PASS=30 FAIL=0`.

## Do not touch

Codex already has dirty worktrees for `physics-loop/photon-vacuum-shift-20261009`
and `physics-loop/toe-dynamics-bridge-20261009` under
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009`. Leave them
alone. Do not open a second worktree. Home `~/Projects/Physics` stays uncommitted.

## Landed this cycle

Commits through cycle 16 are already on the branch. Cycle 17 is pushed
onto the same branch for PR 9475. Do not merge it. Do not open a second PR.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9475

## Next exact action

This was the last science block. The following run is deadline cleanup,
not another alphabet. Do not enumerate `(1, 2, 2)`. Do not repeat this
orbit count. Do not adopt the equality as a law. Do not repeat the
order-blind factor of `(0, 1, 2)`, the shell censuses, the cap-factor
cycles, or the corner-weight family. The odd cap alphabet stays stopped.
The six-direction shell family stays closed. Do not invent a hazard law.
Do not identify the count `24` with a mass density. The site and the rate
stay unsupplied. At the deadline, push any unpushed commits on this
branch, remove the worktree, and write the short handoff. Do not merge.
Do not open a second PR.

## Cleanup

At stop, push the branch if it has commits, remove this worktree with
`git worktree remove`, and delete the campaign scratch
`/Users/jonreilly/.grok/campaigns/toe-24h-20261009` except a short HANDOFF copy
under `~/.grok/campaigns/toe-24h-20261009-handoff.md` if the branch is on
origin. Do not delete the Codex trees or `~/.probe-workers`.
