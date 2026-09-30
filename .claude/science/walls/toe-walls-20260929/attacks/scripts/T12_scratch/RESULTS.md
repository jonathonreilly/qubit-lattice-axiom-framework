# T12 test results (numbers from interval_exponent_results.json and scale_check_results.json)

Code validated: sanity_level_order.py feeds the level order to the generic estimator; 2571 pairs, 0 mismatches
with the exact product-order interval size prod(|d_i|+1).

Site-once ensembles (lemma says N <= B3(h) = (2h+1)(2h^2+2h+3)/3; every sample obeys it; max N/B3 = 0.16)
- E1 level/product order (exact): fitted exponent of the maximal interval 2.56 over h=4..60, 2.83 in the top third
  (analytic local exponent 3h/(h+3) -> 3).  Pre-registered band [2.7,3.3]: passes on the top-third reading only.
- E2 Eden growth, point seed (61^3, 12 targets): p_max 1.32 (h=4..32); N/B3 falls 0.078 -> 0.003.
- E2b Eden growth, flat seed plane: p_max 1.01; N/B3 falls 0.062 -> 0.001.
- E3 iid formation times: longest chain to any of 40 targets is 12 (degenerate order).
Reading (e) holds: generic cubic-covariant site-once growth is far below 2+1; only the fixed-direction level order
reaches exponent 3. (f) holds: 3 of the 24 proper cubic rotations preserve the level predecessor set.
(g) holds: mean (1/3,1/3), cov [[2/9,-1/9],[-1/9,2/9]], third moments 2/27 and -1/27, ball formula, 3(I0+I2)/2 = 0.59049.

Turnover ensembles (events per site grow with time)
- E6 exact synchronous Z^3 x N (a true 3+1 poset), calibration: p_max 3.59, top third 3.87 (3.67 at L48,T60);
  N/B3 rises 0.32 -> 1.30 (h=39) -> 2.13 (h=54): it LEAVES the site-once ball.
- E4 asynchronous CA: top-third slope 3.63 (L44), 3.69 (L64), 3.51 (L56,T40); independent of L (no wrap effect);
  whole-range p_max 3.13; N/B3 at the top 0.03 (still under the ball, zigzag chains inflate h).
- E5 moving records (exclusion), rho=0.5: top-third 3.58; rho=0.2: 3.85; whole-range 2.5-3.0; N/B3 0.016 / 0.015.
Pre-registered reading (c) (p_max >= 3.6 and N/B3 rising by 2x) was NOT met by E4/E5; the follow-up criterion
(top-third slope > 3.3, disclosed in PREREG Addendum 2) was met by all six runs, but the slope did not
grow with run size. Sufficiency of turnover for a 3+1 count is therefore "consistent, not decided" for the random
ensembles; it is decided (checked) only for the exact synchronous E6. Necessity is the lemma.
