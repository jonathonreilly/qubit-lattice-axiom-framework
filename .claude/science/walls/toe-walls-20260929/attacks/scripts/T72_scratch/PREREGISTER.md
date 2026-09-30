# T72 pre-registration (written before any script was run)

Attacker: Claude Sonnet 5.5 (same family as supervisor). Same-family check only.

## What is tested
Reduction R: for lattice matter whose whole generator is timed by a site clock,
H_w = sum of local terms each multiplied by the clock (bond terms by sqrt(w_x w_y),
on-site terms by w_x), a body at rest at a point where w = 1 accelerates at
  a = - W * grad(u)   (u = log w),   W = E0 * d2E/dP2 at P = 0  ( = Hess(E^2/2) at rest),
E(P) the body's own band from the UNTIMED generator. Universality of low-energy free
fall of the class of bodies then means W = 1 for every body class. The wall's "list of
conditions" would be a list of ways a body class gets W = 1 (or fails to).

## Models (1D, 2-component walker, exact numerics, no fits except where stated)
- W1  Dirac walker  H = beta sz S + m sx,  S=(T-T^dag)/2i  -> eps^2 = beta^2 sin^2 k + m^2.  W = beta^2.
- W2  same + scalar offset e0 (timed)  -> W = beta^2 (e0+m)/m.
- W3  bound pair of two distinguishable W1 walkers, contact attraction -lam at same site,
      binding term TIMED by w_x.  W_pair = E0 E'' from the pair band in the untimed relative problem.
- W4  same pair, binding term UNTIMED (constant lam).  Prediction by Hellmann-Feynman
      (passive weight = <kinetic+mass part>, inertia = M_pair).
- A   3D eight doubler species (site signs x coin half turn): accelerations of species packets.

## Measurement
Initial state = lowest positive-energy standing wave of the UNTIMED open chain
(single walker N=240; pair N=40). Acceleration = -<[H_w,[H_w,X_cm]]> in that state (exact
second time derivative of <X_cm> at t=0) at w=1 at the centre; odd part in g used
(g = +/- 1e-3). One time-evolution cross-check of the double-commutator for W1.

## Readings fixed in advance
P1 (reduction holds): for W1 (several m, beta) and W2, |a_meas/(-g) - W_pred| < 0.02*max(|W_pred|,0.1).
   FAIL reading: any single-walker class off by > 5% => reduction R is wrong or incomplete
   (dipole/ordering terms matter) and the whole reframing is withdrawn.
P2 (composite reduction): W3 direct a_meas/(-g) matches W_pair(band) within 3%.
   FAIL: composite fall is not fixed by the pair's own band; extra clause needed.
P3 (composite failure size): PASS for the "composites need an extra clause" reading if
   |W_pair - 1| >= 0.02 at binding fraction B/(2m) about 0.1, and |W_pair - 1| -> 0 as lam -> 0.
   FAIL reading (composites fine without a clause): |W_pair - 1| < 1e-3 at that binding.
P4 (timing of binding matters): W4 (untimed binding) differs from W3 by > 0.02 in W and matches the
   Hellmann-Feynman prediction within 5%.
P5 (species): eight doubler packets built as V_n of one packet have accelerations equal to 1e-10
   for arbitrary positive clock; if not, the "ledger not trajectory" reading is wrong.
Speed mismatch (beta_species != 1): W = beta^2 within 2% => fall universality is exactly equal-c (links T14).

## Outcome map (fixed in advance)
- P1,P2,P5 hold and P3 holds: reframing supported => outcome MISFRAMED (cheaper question: is Hess(E^2/2)|rest = 1
  per body class?), with composite W-1 = O(binding fraction) recorded as unresolved, priced by T14/T17.
- P1 fails: STANDS.
- P3 fails (composites are fine): candidate PASSED for the composite sector on this model only; would still be
  conditional on the supplied timing of the binding term.

## Amendments (recorded after the first runs; the readings above were not changed)
1. The 2-component chain (sz S + m sx) has two valleys (k=0 and k=pi), so pair states mixed valleys and the lowest
   two-body state was a different sector. Switched to the one-component staggered chain (single valley; the repo's
   "staggered rest energy"). The 2-component code is kept in `t72_single.py`, `t72_single2.py`, `t72_single_evolve.py`
   (single-walker cross-checks only); `superseded/` holds pair code that used it.
2. The undressed instantaneous acceleration is contaminated by Zitterbewegung when a scalar offset is present
   (it returned W = 1.00 for offsets whose band value is 1.5 and 3.0). The initial state is therefore dressed to first
   order in g by admixing the negative-energy states of the untimed generator. The undressed numbers are in RESULTS.txt
   (t72_single2 not re-run there; see superseded notes in the report).
3. The lowest pair state above the (+,-) sector on an open chain is a wall-bound pair; the bulk n=1 centre-of-mass
   standing wave is selected by centroid and variance instead.
4. P4 split into two halves. First half (untimed differs from timed by > 0.02): pass. Second half (Hellmann-Feynman
   within 5%): fail at strong binding (10-15%). Unresolved; probably internal polarisation missing from the start state.
5. P3 was written for binding/2m about 0.1; the run covers 0.018 to 0.178.
