# T04 pre-registration (written before any run of ring_flip_identity.py)

Wall T04 = L01-W10 (which record is which) + L06-W13 (field flip vs permanent records).
Attacker: Claude Sonnet 5.5 (same family as supervisor; same-family check).

## Question the test decides
L06-W13 says a ring flip realised as record motion "needs an identity rule". Reading in
the note being attacked (probe 9): "up" = record present; a flip = two records each move
two nearest-neighbour steps through a spectator (vertex / plaquette-centre) site.
Route R1 says: no identity rule is needed for the field dynamics. What is needed is the
records' *distinguishability class*: identical bosons, identical fermions, or distinguishable
(different locked contents). The ring coefficient J depends on that class only through the two
exchange channels a1 (both records shift to an ADJACENT link, via a vertex or via the centre)
and a2 (each record crosses to the OPPOSITE link, via the centre):
   identical bosons   J_B = a1 + a2
   identical fermions J_F = a1 - a2   (up to a gauge sign of the final state)
   distinguishable    two different final content arrangements, amplitudes a1 and a2, no interference.

## Model (supplied, not adopted)
9-site window of Z^2 (scaled coordinates, links at odd/even parity): 4 link sites b(1,0) r(2,1)
t(1,2) l(0,1); 4 vertex sites (0,0)(2,0)(2,2)(0,2); plaquette centre c(1,1). Nearest-neighbour
edges of Z^2 inside the window. Two hard-core records. Low states: A = {b,r} (CCW circulation),
B = {t,l} (CW circulation). H0 = Dv * (#records on vertex sites) + Dc * [c occupied]
+ U * [both records on links but occupancy not in {A,B}] (local Gauss/ice penalty).
V = -t * (NN hop). Effective coupling by 4th-order Schrieffer-Wolff (PVP = 0, odd orders vanish
by bipartiteness), cross-checked by exact diagonalisation.
Parameter sets: (Dv,Dc,U) = (1,1,1), (1,2,1), (1,0.5,1), (1,1,3), (1,4,1), (2,1,3).

## Pre-registered readings
PASS (R1 survives as a reduction): 
  (P1) J_B = a1 + a2 and |J_F| = |a1 - a2| to 1e-9 in all parameter sets (implementation check);
  (P2) exact-diagonalisation half-splitting matches |J| t^4 to within 5% at t = 0.02..0.05;
  (P3) the identity-rule dependence is exhausted by the three-way class (no tag-following rule enters).
The result is INFORMATIVE about the price if additionally:
  (P4) |J_F| / |J_B| is far from 1 (say <0.5 or >2) for the symmetric parameter set (1,1,1):
       then statistics is an O(1) factor on the ring coefficient, i.e. identity is not free gauge
       at the level of the physics; it is one named premise (exchange statistics, sibling T18).
FAIL readings:
  (F1) J_F = 0 exactly for all parameters -> fermionic records cannot flip at 4th order (a different,
       stronger statement; R1 still reduces identity to statistics but statistics is then decisive).
  (F2) J_B != a1 + a2 (implementation or conceptual error) -> discard the reduction, report.
  (F3) a1 or a2 depends on a tag-following rule (impossible by construction; listed so that
       a surprise would be reported).
Secondary: the leakage weight of the low eigenstate on off-link (readable) configurations
scales as t^2 while J scales as t^4 (records sit on vertex/centre sites with probability ~ (t/D)^2);
record the coefficient ratio.

## Addendum B (written before running tracer_1d.py): the L01-W10 half, 1D exact
Claim to test (Lemma L, 1D): if the added record carries a locked content different from the sea's
(content-distinguishable) and moves by NN hops into vacancies, then (B1) the TOTAL density evolution equals
that of identical fermions (open chain, exact rank-sector equivalence), and (B2) the tagged record is read out
by its content, its position law is a wave-function property, and its RMS displacement relative to the excess
density's RMS spread reproduces probe 8's hop-following 1D ratios (0.2 at N=16 half filling, falling with L).
Open chain L=16, N0=7 sea fermions in the free ground state, tracer at site 8 (0-based), free hopping amplitude -1.
PASS: max|n_dist - n_ident| < 1e-9 at all times; tracer/excess ratio at t=3 in [0.10, 0.40] and not increasing after t~1.5.
FAIL (Lemma L wounded in 1D): ratio > 0.6 at t=3 (tracer travels with the excess).
No claim is made for 2D; there the distinguishable problem is not a Slater problem and is not run.
(Result note, added after the run: B1 FAILED as pre-registered. My rank-sector equivalence claim was wrong:
in the identical model the tracer marks are summed coherently with sector signs (-1)^(k-1); in the
distinguishable model they are distinct basis states. Densities differ by up to 0.16 in n_x. B2 result is in results_tracer_1d.txt.)
