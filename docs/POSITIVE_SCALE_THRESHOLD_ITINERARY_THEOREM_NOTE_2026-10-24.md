# Endpoint-clipped positive-scale itineraries

**Date:** 2026-10-24
**Type:** bounded_theorem
**Primary runner:** `scripts/positive_scale_threshold_itinerary_2026_10_24.py`
**Scope:** exact finite partitions and oriented integrals for supplied positive scales and piecewise-constant coefficients. No physical running law is derived.

## Contract

Supply finite positive real endpoints u,v and a finite strictly ascending list of distinct positive thresholds q_1<...<q_n (n may be zero). Reject nonfinite, nonpositive, duplicate or unordered inputs. In t=log(mu), let Q_i=log(q_i). Regime j, for j=0,...,n, is the open interval between Q_j and Q_(j+1), with the extreme bounds interpreted as minus/plus infinity. Assign each threshold itself to the regime immediately to its right for a right-continuous pointwise convention. Those finitely many point values do not affect the integrals below.

If u=v, return an empty itinerary. Otherwise retain only thresholds strictly between min(u,v) and max(u,v), sort them in travel direction, and join them between u and v. For each consecutive endpoint pair (a,b), assign the regime of any interior point of (log(min(a,b)),log(max(a,b))). This is independent of the selected interior point. Equivalently j is the number of thresholds less than or equal to min(a,b). In particular, a decreasing segment ending exactly at a threshold belongs to the regime above that threshold, not the lower regime associated with further travel. Endpoint equality cannot select an unrelated regime.

## Partition theorem and proof

The constructed nonzero segments are adjacent, strictly monotone in the chosen direction, have disjoint interiors and cover exactly the requested interval, with no overshoot. Reversing u,v reverses the segment order and each orientation, preserving the interior regime labels.

**Proof.** Strict monotonicity of log preserves the ordering of all positive supplied scales. Every retained threshold is strictly interior, so the finite sorted list together with the endpoints is strictly ordered; consecutive pairs are nonzero and share exactly their common boundary. Their union telescopes from the first endpoint to the last, leaving no gaps. Their interiors are disjoint by strict order. No threshold lies strictly inside a consecutive pair: any such threshold would have been inserted between the two endpoints. Hence every interior point has the same number j of thresholds below it. A threshold equal to the lower boundary is below every interior point and must be counted, giving the stated less-than-or-equal formula. Reversal uses the same retained set in reversed order and the same open segment interiors. Equal endpoints give the stipulated empty partition. This proves every assertion.

## Oriented integral theorem

Supply finite real coefficients c_0,...,c_n, constant on the corresponding log-scale regimes. Let f(t)=c_j there, with the preceding endpoint convention at thresholds. Then

```text
integral from log(u) to log(v) of f(t) dt
  = sum over itinerary (a,b,j) of c_j [log(b)-log(a)].
```

**Proof.** On each open segment f is constant, so its integral is its coefficient times oriented length. Values at finitely many boundaries do not affect a Riemann integral. Finite additivity on the exact partition gives the displayed sum. For reversed endpoints each summand changes sign and order, so the integral changes sign. Equal endpoints have integral zero. No continuity or physical matching across the thresholds is assumed.

The implementation uses binary search at the lower scale boundary rather than computing a floating midpoint, which could round onto an endpoint. Mathematical assertions above are exact for real inputs; floating log arithmetic in the checker is a finite numerical implementation, not interval certification.

## Historical counterexample retained as supplied data

Take u=246.28, v=91.1876 and thresholds (1.27,4.18,172.69), with illustrative regime coefficients 11-2 n_f/3 for n_f=(3,4,5,6). The valid path is246.28->172.69->91.1876. The historical YT path246.28->172.69->4.18->1.27->91.1876 overshoots its endpoint and then returns under a different coefficient. Its one-loop log-integral numerator is -2.4762308783881095 instead of -7.380570677615257, a difference4.904339799227147. These supplied examples preserve the independently checked itinerary failure; they are not physical coefficient derivations or repaired YT predictions.

The original long YT note, full-chain runner/cache, declared-anchor note/runner/cache and canonical plaquette helper remain unchanged and recoverable at b7fc5726160fdd49babf43474efb699e9da344c8. This distinct owner does not apply its algorithm to that pipeline. CW curvature, Ward/root validity, two-loop normalization, running-versus-pole interpretation and actual downstream authority remain separate obligations.

## Checks and limits

The standalone runner declares this note as its input and a120-second execution cap. It checks empty/no/interior/multiple/outside thresholds, exact endpoint ties, reversal, adjacency, a closest-representable endpoint pair, invalid data rejection, analytic constant/dyadic integrals and the historical wrong-route discriminator. It imports no repository helper and reads no external model. Numerical tests support the implementation; the proof above supplies the general result. No execution outcome is asserted before a source-bound capture.
