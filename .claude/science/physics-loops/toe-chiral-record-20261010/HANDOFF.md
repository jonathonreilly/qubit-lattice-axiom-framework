# Handoff — toe-chiral-record-20261010

Base `0b208e91cfc`. Branch `physics-loop/toe-chiral-record-20261010`.
Worktree: `/Users/jonreilly/.grok/campaigns/toe-chiral-20261010/wt`.
One worktree. Do not touch PR 9475 or the Codex photon and D3Q27 trees.

## Done

PR https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9477
is open. Do not merge it and do not open a second PR.

Cycle 1. Soldered bond-symmetric factors on one proper orbit of
`(1, 2, 3)`: linear dimension 84, six direction-record orbits, far-end
rank 6, affine dimension 78. Runner `PASS=14 FAIL=0`. No factor is
selected.

Cycle 2. Order-blindness on the 7-site cross does not cut that family
to the exhibited modulus-3 line. The same cap sign on `a·d = 1` and
`a·d = 2` gives two further strictly positive soldered lines, and the
parent converse makes each order-blind. A mixture of modulus 3 and
modulus 2 has a two-neighbour moment `25/24`. Runner `PASS=22 FAIL=0`.
The rest of the order-blind set is not classified.

Cycle 3. Inside the span of those three cap signs, a nonzero scale has
every product mean equal to 1 only on the three axes. A two-modulus
witness has moment `13/12`. The mixture `(-2, -2, 1)` cancels the
pairwise moments and still has three-neighbour moment `-3`. Runner
`PASS=9 FAIL=0`. Factors outside the span are not classified.

Cycle 4. Each opposite cap `a·d = -m` for `m` in `{1, 2, 3}` is a
strictly positive soldered line, with product mean 1 on all 729 weight
patterns. The bond from `(1, -2, -3)` to `(1, 2, 3)` along `e_z` has
level `-3` product `-1` and positive-cap product 0, so that line sits
outside the positive span. Levels `-1` and `-2` have the same
separation. Runner `PASS=23 FAIL=0`. Slices outside the six oriented
caps are not classified.

Cycle 5. The transverse cross product on the caps `a·e_z = -3` and
`b·e_z = 3`, kept when the transverse absolute values match, extends
by proper rotations to a soldered kernel with values in `{-1, 0, 1}`.
Each record activates one direction and every slice sums to 0, so
every neighbour product has mean 1. The slice at `(-2, 1, 3)` is
nonzero and orthogonal to all six cap signs. Runner `PASS=14 FAIL=0`.
The rest of the order-blind set on this orbit is not classified.

## Next exact action

Count soldered bond-symmetric factors on the 48-point chiral pair.
Search first. Do not repeat the existence of the pair, the
transverse-cross kernel, or the dimension count on the 24-point orbit.
Do not invent a formation rate. Do not return to shells, plaquette
corner weights, or the `(0,1,2)` and `(1,1,2)` alphabets.

## Cleanup

Keep this one worktree. Delete `docs/audit/data/citation_graph.json` after
each manifest refresh. Remove the worktree only when the session can no
longer continue or free disk falls below 10Gi.
