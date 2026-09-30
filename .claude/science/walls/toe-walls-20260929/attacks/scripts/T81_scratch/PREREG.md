# T81 pre-registration (written before any run)

Provenance: Claude Sonnet 5.5 (same family as the supervisor). Same-family checks only.

## Question the test decides

The wall: ordered-phase (memory of direction) thresholds of the six-axis formation law on (p,1,2)
are proved at p >= 4165 (block 30 T4, landed) / p >= 285718 (block 25) / p >= 84 (probe, unlanded)
while the observed onset is about 11 (10.5-11).  Every one of those proofs goes through the same
domination: actual law <= two-level noisy majority automaton eta' (eps1 = d1, eps2 = max(d2,d3)).

Q: Is the gap 84 -> 11 mostly (T) proof-technique slack on eta' (the dominating automaton itself
orders far below 84) or mostly (D) domination slack (eta' itself only orders near 84)?

## Tests

A. Exact arithmetic (no simulation).
   A1. Re-verify the four block-30 T4 rational certificates and the (84,1,2) refinement-history
       certificate (sigma=161/5000, Zbar=5119922891/1e9), exact Fractions.
   A2. Find the exact real-p feasibility boundary of the refinement-history recursion H1 on (p,1,2)
       (best sigma, smallest Zbar), and of the block-30 tree recursion (best t), i.e. what each
       counting technique can give at best.  Pass/fail: A1 passes iff every inequality holds;
       A2 is a computation, its value is reported.

B. Simulation (numpy, torus L x L level plane, site (i,j) at level n has predecessors
   (i-1,j),(i,j-1),(i,j) at level n-1; start all-a / all-zero).
   B1. eta' with eps1,eps2 of (p,1,2); B2. the actual six-state product law on (p,1,2).
   Observable: dissent density rho(T) after T levels, from the ordered start.
   Classification: ORDERED at p iff rho(T_end) < 0.2 and rho does not grow between T/2 and T_end
   (growth = rho(T_end) > 1.5 rho(T/2) + 0.005).  Onset p* = smallest scanned p that is ORDERED
   in a majority of seeds, refined by bisection to +-0.25.

## Pre-registered readings

R-T (technique slack dominates): p*(eta') <= 30.  Then the proof gap 84 -> p*(eta') is technique
    (a better count / computer-assisted bound on the same automaton could in principle close it) and
    eta' loses at most p*(eta') - p*(actual).
R-D (domination slack dominates): p*(eta') >= 60.  Then no better counting of eta' can go below
    ~60; only dropping the domination (new premise: a finer dominating process or the actual law) can.
R-M (mixed): 30 < p*(eta') < 60.
Sanity: p*(actual) should reproduce the wall's located onset (10.5, 11) within +-2; if p*(actual)
    is outside [8.5, 13] the wall's "observed" number is not reproduced and that is reported as a
    finding against the wall statement, not smoothed over.
Finite-size caveat pre-registered: near p* the finite torus may leave the ordered branch late; the
    scan uses two sizes (L=128, 256) and two horizons; a classification that changes with L or T is
    reported as "uncertain" and widens the bracket.

## Kill conditions for the report
- If A1 fails, the landed 4165 is not certified and the wall's "landed" claim stands unchanged.
- If p*(actual) does not reproduce (10.5, 11) the "located onset" is downgraded to unverified.
