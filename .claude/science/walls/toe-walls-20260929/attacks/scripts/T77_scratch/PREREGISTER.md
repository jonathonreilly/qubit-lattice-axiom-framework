# T77 pre-registration (written before any script was run)

Claude Sonnet 5.5, same vendor family as the supervisor; same-family checks.

Wall T77: Gauss-law (ice-rule) patterns are not outputs of directed local
formation, and the link-and-role pattern breaks one-qubit-everywhere covariance.

Two small tests, one per half of the wall. Each is a route's decisive first artifact.

## Test A (covariance half; route R2 "roles from broken symmetry")

Question (the L06-W12 queued item): if every site of Z^3 carries one qubit and the
balance rule is the SAME at every site (fully covariant, nearest-neighbour star:
"the six neighbours of every site balance"), is there an extensive manifold of
patterns (a Coulomb-phase candidate), as in the parity-typed ice?

Model: Z_L^3 torus, L even. tau_s in {+1,-1} at every site. For every site s the
neighbour sum S_s = sum_{t~s} tau_t must lie in an allowed set A.
Sites split into two sublattices that never constrain each other (bipartite), so
count = c_E * c_O = c^2 with c the count on one sublattice (translation gives c_E=c_O).
Allowed sets tried: A0 = {0} (exact 3-of-6 balance), A1 = {-2,0,2}.
Control: the parity-typed ice on the vertex-link incidence graph, side-2 coarse torus
(landed count 9600).

PASS for the route (covariant every-site rule keeps a liquid): log2(count)/#variables
stays bounded away from 0 as L grows (extensive), for A0.
FAIL (route wounded to "roles are forced"): for A0 the count is a handful of crystals or
0, i.e. log2(count)/L^3 -> 0, and A1 either also rigid or extensive only by dropping the
exact balance.
Prediction (mine, before running): A0 is rigid (counts of order 2^{O(L)} or smaller, each
solution a periodic crystal); A1 extensive. If A0 is extensive I am wrong and R2 is alive.

## Test B (formation half; route R1 "the order carries the law")

Model: ICE_SUPPORT note's soldered model (2026-09-22): a vertex takes a uniform consistent
record (one of the 20 ice patterns consistent with its already-recorded links) or none;
a link copies the vertex assignments of its formed vertices, takes a fair coin if none
formed, and has no record if two formed vertices disagree.
Sites are vertices of Z^3 (coarse), links between them.

Orders: (i) lexicographic sweep on an open box (3 back, 3 forward); (ii) diagonal front
t = x+y+z on an open box; (iii) i.i.d. random order on a torus; (iv) diagonal front plus
Gaussian time jitter sigma; (v) lexicographic order on a torus (closed volume).
Measures: fraction of unrecorded vertices and links (each unrecorded link is a +-1
charge mismatch); for (iii)/(iv) the block-charge variance scaling.

Predictions:
 P1. (i),(ii): zero defects in the bulk (n_v <= 3 for every vertex).
 P2. (iii): defect fraction of order 10 percent of links; mismatch charges do not screen.
 P3. (iv): defect fraction grows roughly linearly in the fraction of order-flipped edges,
     from 0 at sigma = 0.
 P4. (v): defects concentrated on the wrap layers, count ~ surface, not volume; at least
     one defect always.
FAIL of the route ("order carries the law" is not a price but a free lunch): a random or
jittered order also gives zero defects; or a closed torus order gives zero defects.
PASS as a PRICE: P1 true and P2-P4 true. This does not pass the wall: the uniform measure
and covariance halves are untouched by Test B (landed notes prove them separately).
