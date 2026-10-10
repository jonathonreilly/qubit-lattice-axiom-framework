```yaml
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "source/action and physical-observable identification"
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "The only shared pair (u, v) covariant for the boundary-sign character is (0, 0). The zero pair is not a flux. The corner-weight family stops. The site and the rate stay unsupplied."
```

Cycle 16 prunes the reading that some nonzero shared pair, with color `0`
contributing `0`, color `1` contributing `u`, and blank contributing `v`,
is a covariant circulation. The relation lattice is all of `Z^2`, of
index `1`. Exact division returns only `(0, 0)`. That pair is not adopted
as a flux. The corner-weight family stops. The quoted blocker below is
not closed.

Cycle 15 prunes the reading that some nonzero integer corner weight, with
blank counted as `0`, is a covariant circulation. The relation lattice is
the even-sum sublattice of index `2`. Exact division returns only the
zero weight. That weight is not adopted as a flux. The quoted blocker
below is not closed.

Cycle 14 prunes the reading that this alternating corner sum is a
covariant circulation. The half-turn `(x, y, z) ↦ (y, x, -z)` fixes
`0101` and has character `-1`, while the sum there is `-2`. No
coefficient triple is assigned. The sum is not adopted as a flux. The
quoted blocker below is not closed.

Cycle 13 prunes the reading that proper-cubic covariance forces a unique
nonzero circulation on the 81 colorings of one unit square. The covariant
assignments are a free module of rank 3. Zero is covariant, and the three
coefficients are independent. None is adopted. The quoted blocker below is
not closed.

Cycle 12 prunes the reading that some shell with entries in `{0, 1, blank}`
forces one locked direction under the soldered six-direction action. No
shell has output type `(1,)`. The unique invariant laws are the uniform
law on `000000`, `111111`, and `bbbbbb`. None of those laws is adopted.
The quoted blocker below is not closed.

Cycle 11 prunes the reading that a shell with exactly one blank axis
direction forces one locked direction under the soldered six-direction
action. The blank and its antipode are both singleton output orbits. Both
point masses are invariant, support size 1 occurs, and neither mass is
adopted. The quoted blocker below is not closed.

Cycle 10 prunes the reading that a fully recorded binary six-neighbor
shell forces one locked possibility. Under the soldered six-direction
action the two constant shells force the uniform law of mass `1/6`.
Under the unsoldered two-label action both labels survive at every shell.
Neither action is adopted. The quoted blocker below is not closed.

The quoted blocker is an open-gate bullet in
`docs/MINIMAL_AXIOMS_2026-06-29.md`. Cycle 9 does not close it. It exhibits
one soldered factor `1 + (1 - 2 t) B^X + (t^2 - t + 1) B^Y` on the proper
orbit of `(0, 1, 2)`. The factor is not the constant `1` at `t = 0`.
Partial normalisation holds only at `t = 1/2`, where the bond values are
strictly positive. That root is supplied by `1 - 2 t`. The reading that
this root is a selected interaction is pruned. The odd cap alphabet stops.

Cycle 8 pruned the reading that an independent quadratic pencil
`1 + t (a X + b Y) + t^2 (c X + d Y)`, with coefficients in
`{-2,-1,0,1,2}`, isolates a unique nonzero `t`. Every such pencil
normalises at `0`. The balance pencil is normalised at both `0` and
`1/2`, and both are strictly positive.

Cycle 7 pruned the reading that soldered covariance of a bond factor
`1 + kappa F` on this orbit fixes a nonzero `kappa`. Even quarter-turn
families normalise only at `0`. Odd pure orbit lines normalise for every
`kappa`. Strict positivity on the unit line is an interval.

Cycles 1–6 are unchanged. Cycle 6 pruned the reading that this orbit is a
chiral pair and the reading that the transverse-sign factor of `(1, 2, 3)`
varies it. The axis-role product of that cycle is the odd positive-cap
line here. Its supplied `kappa = 1/2` was not a forced normalisation.
Cycle 5 pruned the reading that proper-cubic covariance of one `3×3`
correlation selects the quadratic channel ratios or the sign of `t`.
Cycle 4 pruned two readout readings of the directed pattern. Cycle 3 pruned
two CHSH readings inside the density hypothesis. Cycle 2 pruned local
readouts of the six-axis product-class pair as a source of CHSH square 8.
Cycle 1 pruned full proper-cubic invariance of a two-qubit state forcing
the singlet.
