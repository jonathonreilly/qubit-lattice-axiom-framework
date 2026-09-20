synchronous-rerecording-small-windows, independent run 1 of 2
worker w-jonathonsmac4f50-j811e (claude-opus-5), unit C-synchronous-rerecording-small-windows-a1

Six-axis menu, W(a,b) = p (same axis), q (opposite), r (orthogonal), at the exact rational weights (3,1,2) and
(5,2,4). Everything is exact rational arithmetic; no sampling except where a state space is too large to exhaust,
and there the sample is seeded and each checked equality is still exact.

CONVENTION. On a torus of side 2, x + e_j and x - e_j are the same site. The neighbour MULTISET is used in the
main run (so a site of the 2x2 torus has four neighbour slots, two per direction) and the static law carries one
bond per (site, forward direction), which makes its conditional at x exactly the re-recording rule. Section (4)
repeats every check with the SET convention (two distinct neighbours, four bonds) because the paired run may read
it that way, and the answers to the three questions are the same under both; only the numbers differ.

(1) ASYNCHRONOUS SINGLE-SITE RE-RECORDING: DETAILED BALANCE
  the rule at x draws a with probability prod_{y in N(x)} W(a, s_y) / Z_x(s), and Z_x depends only on the
  neighbours, which the move does not touch. The static law's ratio between s and s with x set to a is
    pi(s)/pi(s^{x->a}) = prod_{y in N(x)} W(s_x, s_y) / prod_{y in N(x)} W(a, s_y),
  so pi(s) P(s -> s^{x->a}) = (1/N) prod_y W(s_x,s_y) prod_y W(a,s_y) / Z_x, which is symmetric under
  exchanging s_x and a: detailed balance holds identically in (p,q,r), for any neighbour multiset.
  2x2 torus weights (3,1,2): exhaustive detailed balance over all 1296 states, 25920 moves: violations 0
  2x2x2 torus weights (3,1,2): exact detailed balance on 2510 random moves (seeded) out of 1679616 states: violations 0
  2x2 torus weights (5,2,4): exhaustive detailed balance over all 1296 states, 25920 moves: violations 0
  2x2x2 torus weights (5,2,4): exact detailed balance on 2510 random moves (seeded) out of 1679616 states: violations 0

(2) SYNCHRONOUS RE-RECORDING ON THE 2x2 TORUS
  the 2x2 torus is bipartite: sites (0,0),(1,1) on one sublattice, (0,1),(1,0) on the other, and every
  neighbour of a site lies on the other sublattice (twice). A synchronous re-draw therefore makes the new
  A-values depend only on the old B-values and vice versa, so the chain maps product measures to product
  measures and its unique stationary law (all transitions are positive) is a product mu(A) nu(B).
  sublattice A = [(0, 0), (1, 1)], B = [(0, 1), (1, 0)]
  weights (3,1,2): mu solves mu K = mu exactly (K = M_AB M_BA): True; sum mu = 1, sum nu = 1
  weights (3,1,2): the product law is stationary for the full 1296-state chain (worst deviation over 40 sampled targets: 0)
  weights (3,1,2): pi_sync equals prod_x Z_x(s) normalised: True
  weights (5,2,4): mu solves mu K = mu exactly (K = M_AB M_BA): True; sum mu = 1, sum nu = 1
  weights (5,2,4): the product law is stationary for the full 1296-state chain (worst deviation over 40 sampled targets: 0)
  weights (5,2,4): pi_sync equals prod_x Z_x(s) normalised: True

(3) TOTAL VARIATION AGAINST THE STATIC LAW
  weights (3,1,2): TV(synchronous stationary law, static law) = 505370471/1147076748 = 0.440573; TV(prod_x Z_x, static law) = 0.440573
  weights (5,2,4): TV(synchronous stationary law, static law) = 16118013809/44806080366 = 0.359728; TV(prod_x Z_x, static law) = 0.359728

(4) THE OTHER NEIGHBOUR CONVENTION
  the same three checks with the SET convention (each distinct neighbour counted once, so a site on the
  2x2 torus has two neighbours and the static law has four bonds), in case the paired run reads it that way:
  weights (3,1,2) (set convention): detailed balance violations 0 of 25920 moves; pi_sync = prod_x Z_x normalised: True; TV against the static law = 529411/2249868 = 0.235308
  weights (5,2,4) (set convention): detailed balance violations 0 of 25920 moves; pi_sync = prod_x Z_x normalised: True; TV against the static law = 2708336741/13074694566 = 0.207143

(5) READING
  (1) holds, and identically in (p,q,r): the rule at x is the static law's own conditional at x, and Z_x depends
  only on the neighbours the move leaves alone, so pi(s) P(s -> s') is symmetric in the old and new value at x.
  The exhaustive check on the 2x2 torus (1296 states, 25920 moves) and the seeded exact check on the 2x2x2 torus
  found no violation at either weight set, under either convention.
  (2) holds exactly, not approximately: the 2x2 torus is bipartite, so a synchronous re-draw makes each
  sublattice's new values depend only on the other's old values, the chain preserves product measures, and its
  unique stationary law (every transition is positive) is the product mu(A) nu(B) obtained from the 36x36
  sublattice matrices. That law equals prod_x Z_x(s) normalised, entry for entry over all 1296 states, at both
  weight sets and under both conventions. Note that prod_x Z_x(s) is itself a product over the sublattices,
  since Z_x depends only on the other sublattice - the claim is consistent with the structure that forces it.
  (3) is not zero: TV(synchronous, static) = 505370471/1147076748 = 0.440573 at (3,1,2) and
  16118013809/44806080366 = 0.359728 at (5,2,4) with the multiset convention, and 0.235308 and 0.207143 with the
  set convention. Synchronous re-recording does not reproduce the static law on this window.
  All three expectations hold; no HIT. Numbers, not a verdict on the physics.
