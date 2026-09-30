# T18 pre-registration (written before running any script)

Claim under test (Lemma L, "locality selects bosons"). Records are UNLABELLED
(MINIMAL_AXIOMS:92 "a state is a configuration of records"), at most one per site
(:80). Suppose the two-record amplitude rule is bounded-range (AMP-LOC): a hop's
amplitude depends on the other record only if it lies within range r of the hop.
Then for an exchange loop on which the two records stay farther than r apart, the
loop holonomy equals the one-body holonomy of the concatenated closed path, which
is the same for both statistics sectors; the free-fermion class has holonomy -1 on
every exchange loop. So no bounded-range rule, in ANY diagonal gauge, reproduces
the fermion class, for exchange loops longer than r.

## Test A (script t18_f2_locality.py): exact linear algebra over F_2
Setup: hard-core unordered configurations of N records on an L^d open grid.
Target cochain a_f = free-fermion (Jordan-Wigner, any fixed site order) hop signs.
Unknowns: an arbitrary gauge f(S) in F_2 for every configuration S, and a
bounded-range rule alpha[edge, pattern of other records within r of the edge].
Gauge fixing (WLOG): far hops (no other record within r) carry the one-body rule,
which for the fermion is flux-free, so alpha = 0 there.
Equation per config-graph edge: alpha + f(S) + f(S') = a_f(S,S').
Output: r*(L) = smallest r at which the system is solvable.

PASS reading (lemma supported): r*(L) grows with L (r*(L+1) >= r*(L), and
r*(L) >= L/2 - 1 for L >= 5) in 2D N=2, similar in 3D; and the 1D chain control
is solvable at r = 0. Also each infeasible case must exhibit an explicit exchange
cycle of far hops with fermion holonomy -1 (checked independently by BFS parity).
FAIL reading (lemma wrong / route lives): a solution at fixed small r (<= 2) for
all L up to 8, i.e. r*(L) bounded. That would mean a local correlated-hopping sign
reproduces fermion statistics in 2D at N = 2 and the wall is only a Hamiltonian bit.

## Test B (script t18_walker_coin.py): the actual coin walker
One-body blocks A_{+-e_a} = -+ i sigma_a / 2 (repo walker, block 54 form).
Far exchange loop: two records rotate half a turn around a rectangular ring (both
clockwise, alternating steps, never adjacent). Compute the 4x4 loop operator X on
C^2_x (x) C^2_y for the local (boson, K_+) rule and for the fermion sector K_-
(same blocks with the Jordan-Wigner sign for order flips).
Predictions: X_b^2 = 1 (unit-normalised); tr X_b = 2(-1)^A with A the enclosed
number of plaquettes; spec(X_f) = spec(-X_b). PASS: spec(X_b) != spec(-X_b) for
every ring tested (so no block-diagonal gauge maps K_- to a bounded-range rule).
FAIL: some ring with spec(X_b) = spec(-X_b) (then the coin case escapes Lemma L).

## Not testable in the time box
Route 2 (emergent fermion from an entangled vacuum) needs the T-junction protocol
on a chosen stabilizer Hamiltonian: named as first artifact only.
