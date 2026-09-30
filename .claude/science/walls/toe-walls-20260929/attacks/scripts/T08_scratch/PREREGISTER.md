# T08 pre-registration (written before any run of test_T08.py)

Attacker: Claude Sonnet 5.5 (same family as supervisor; same-family check).

## What is tested
Route R2 ("co-formation"): Theorem 1 of the Bell-values note assumes each record is drawn with
INDEPENDENT fresh noise given already-formed neighbours (outcome independence, one site at a time).
The axiom text fixes only each site's own distribution ("determined by nearest-neighbour conditions").
Test: let the interior of a Bell patch form JOINTLY given already-formed, exogenous, independent
setting records s,t in {0,1}; joint law = normalised nearest-neighbour Gibbs weight (positive pair
weights). Outcome a = f(content of A), b = g(content of B) (first half of alphabet = +1).
Graphs: G1 chain s-A-C-B-t (cut = one site); G2 plaquette s-A-{C1,C2}-B-t (4-cycle A,C1,B,C2).
Objective: S = E00+E01+E10-E11 (all sign patterns are relabelling-equivalent).

Locality readings (constraints on single-site MARGINALS over the joint draw):
 - DLR   : none (only the site CONDITIONALS given co-forming neighbours are local).
 - PI    : marginal of A independent of t; of B independent of s (parameter independence / no signalling).
 - ML    : PI plus every middle site's marginal independent of (s,t) (its nearest neighbours are
           unformed, so no recorded condition may change its law).

## Pre-registered claims and readings
P1 (Theorem 5, proof sketch: Markov + one-site cut with P(C|s,t) constant => LHV, so S<=2).
   G1 under ML: PASS reading = best S <= 2 + 1e-6 at feasibility residual < 1e-9 over >=200 restarts.
   FAIL reading = any feasible S > 2 + 1e-6 (then Theorem 5 or the code is wrong).
P2 (machinery sanity). G1 under PI (and DLR): best S > 2.5 (target: >= 2*sqrt(2) reachable with small alphabets;
   4 reachable in DLR with large alphabets). FAIL reading = best S <= 2 (code wrong or route dead outright).
P3 (the decisive one). G2 under ML.
   Route SURVIVES (patch of 4 sites with per-site marginal locality beats 2): best feasible S > 2.05
   at residual < 1e-9, confirmed by independent high-precision recomputation.
   Route DEAD in Gibbs class at these alphabets: best S <= 2 + 1e-6 in every restart family
   (alphabets (na,nb,nc) in {(2,2,2),(2,2,3),(4,4,2)}) AND the tolerance sweep S_max(eps) -> 2 as eps -> 0.
   Anything in between (S_max(eps) > 2 only for eps >= 1e-4) = route dead for exact locality, alive only as an
   approximate/leaky locality; report the number.
My prior: 50/50 on P3 (no general argument known to me either way).

## What each outcome would move
 - P3 survives: T08 is not an axiom-level wall; the wall is the extra premise "co-forming sites draw independently"
   (outcome independence), and the cheaper question is the patch-size clause of the formation law.
 - P3 dead: co-formation does not rescue the records-only reading under literal per-site locality; the lane's
   price (a second ingredient or non-local odds) stands and is sharpened to "no Markov patch with per-site
   marginal locality".

## Amendments (written after the first exploratory runs, before the final campaigns; recorded for honesty)
- The first full-Gibbs search (test_T08.py, exp-parametrised positive weights) never exceeded S = 2.0 even in
  PI mode, so it could not decide P2/P3 (positive weights cannot reach the hard-zero constraints). It is NOT used.
- I replaced it by a relaxation (test_T08_reduced.py): any Gibbs patch has P(a,b,lam|s,t) = F[s,a,lam]G[t,b,lam]/Z;
  maximise CHSH over arbitrary nonnegative F, G (zeros allowed) under the locality constraints. Upper bound for
  Gibbs patches; realisability is then shown by an explicit exact gadget (gadget_exact.py, gadget_gibbs_check.py).
- The cluster-locality mode CML (joint law of the cut independent of s,t; equivalently, no readable record cluster
  not adjacent to a setting may depend on it) and the 2-rail ladder gadget were NOT pre-registered; they came from
  the analytic step "single-site marginal locality at the cut only fixes single-site marginals".
  Prediction recorded now, before the CML campaign finishes: chain ML <= 2, plaquette ML = 4 (PR), plaquette CML <= 2.
