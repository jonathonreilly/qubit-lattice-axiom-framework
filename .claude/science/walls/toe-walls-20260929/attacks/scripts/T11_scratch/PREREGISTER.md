# T11 pre-registration (written before any script was run)

Attacker: Claude Sonnet 5.5 (same family as supervisor). 2026-09-29.

## Question under test
L04-W1 and L01-W11 say: records/ticks give order and counts, not a clock with a rate;
the 2026-08-11 witnesses (a) formation probability 1/3 vs 2/3 and (b) parallel vs
random-sequential two-site completions (correlation 0 vs 3/5) show "different clocks
on the same rule give different physics". The lane's cheapest test: "define one tick as
one record hop; do the parallel and random-sequential completions then agree?"

My reading (to be tested, not assumed): (a) and (b) are ONE phenomenon, simultaneous
formation of ADJACENT sites (each conditioning on the other as still empty). If events on
adjacent sites are never simultaneous, the physics depends only on the commutation class
of the event order (an acyclic orientation of the forming set), the overall rate scale
drops out, and only (i) a probability measure on acyclic orientations and (ii) rate RATIOS
remain. This would make T11 collapse into T01 (formation-order datum) plus a registered
unit, i.e. MISFRAMED.

Rule: the 2026-08-11 rule (2): content s in {-1,+1}; weight 4^(number of already
recorded neighbours equal to s); p(s) = w(s)/(w(-1)+w(+1)). Empty neighbours contribute 0.
Graphs: P3, P4, C4 (2x2 plaquette), K1,3, K1,6 (the 7-site star of the note), cube Q3
(2x2x2, 6-NN). All sites initially empty unless stated.

## Tests and readings
A. Trace invariance. For every permutation of the sites compute the exact final joint
   law. Group permutations two independent ways: (1) orientation signature (which endpoint
   of each edge comes first); (2) closure under swapping adjacent NON-adjacent-in-graph
   letters (BFS). 
   PASS: the two partitions coincide; the final law is identical within every class;
   number of classes = |chi_G(-1)| (Stanley 1973, computed by deletion-contraction).
   Also record whether laws differ ACROSS classes (schedule matters).
   FAIL (STANDS-ward): a law differs inside a class (hidden ordering data), or classes
   != acyclic orientations.
B. Simultaneity. Run the parallel product kernel (08-11 note eq. (5)) to absorption on
   K1,6 and K2 (and P3, C4) for q in {1/3, 2/3, 0.1, 0.01, 0.001}; compare with the
   uniform-random-order (i.i.d. clock) law; compute the L1 distance of the parallel law
   to the convex hull of the class laws (LP).
   PASS (supports "one phenomenon"): parallel absorbed law depends on q; tends to the
   random-sequential law as q -> 0; for q = 1/3, 2/3 it is at strictly positive L1
   distance from the hull of dependence-consistent laws (so it is NOT a scheduler mixture).
   FAIL: the parallel law lies inside the hull (then it is just one more orientation
   measure and the "simultaneity" story is wrong), or does not depend on q.
C. Rate ratios are physical. Path seed(+1)-b-c, exponential clocks rates (lam_b, lam_c):
   final law depends on lam_b/lam_c and not on a common scale.
   PASS: varies with the ratio. FAIL: constant (then even ratios are gauge for this rule).
D. Depth is inherited from the order measure. On L^3 tori (L=4,6,8,10) compute the
   longest directed path (Foata height) of the once-only formation trace under
   (i) i.i.d. labels, (ii) checkerboard (even before odd), (iii) lexicographic sweep.
   PASS (supports "depth clock is not scheduler-free"): the three differ by more than a
   factor 2 at L=10 although all satisfy the same local rule.
   FAIL: all equal within a factor 2.

## Overall decision rule
- A, B, C pass  -> outcome MISFRAMED (cheaper question: which probability measure on
  acyclic orientations, plus which rate-ratio field; the absolute rate is gauge and the
  unit is registered). D passing shows the residual is exactly T01's order datum.
- A fails -> STANDS.
- B fails -> witnesses (a),(b) are not one phenomenon; outcome STANDS or PRICED.
- C fails -> even ratios are gauge for this rule; report MISFRAMED with stronger claim.
Nothing here derives that a tick IS physical time; that identification remains a reading.

## Addendum (written after the first run; honest record)
- Test E (hop version of the lane's suggested test: 12-ring, 4 records, nearest-neighbour
  attraction K = 0.7, heat-bath moves) was coded together with A-D but its readings were NOT
  entered in this file before running. Prediction held in my head: single-bond moves commute
  iff their footprints do not overlap (bonds >= 3 apart); random-sequential and layers of
  pairwise-commuting moves keep the Gibbs (static) law; simultaneous even/odd layers do not.
  Status: checked, not pre-registered.
- First run of E used Metropolis acceptance; the colour-sweep chain then had 5 unit
  eigenvalues (downhill moves forced, chain reducible) so its "TV 0.999" was an artefact of
  my stationary-vector extraction. Switched to heat-bath acceptance (never 0 or 1),
  unit eigenvalue count 1 for all three schedules. Result in test_T11.out is from the fixed run.
- Tests A-D: readings as registered above; no changes after the first run except the K2 block of B
  (extended to q = 1, 2/3, 1/2, 1/3, 0.01 with a closed form).
