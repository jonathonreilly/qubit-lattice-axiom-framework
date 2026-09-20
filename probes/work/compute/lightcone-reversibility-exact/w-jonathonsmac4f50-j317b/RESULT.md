lightcone-reversibility-exact, independent run 1 of 2
worker w-jonathonsmac4f50-j317b (claude-opus-5), unit C-lightcone-reversibility-exact-a1

Is light-cone formation reversible? The record at (t+1,x) is drawn with probability proportional to
exp(beta s.S_x), S_x the sum of the level-t records over N(x) = {x} union {x +- e_j} - the site itself
included. Claim tested: the synchronous chain is reversible with respect to pi(s) proportional to
prod_x Z(S_x(s)).
Every check below is exact integer arithmetic: for the six-axis menu each weight is t^(+1), t^(-1) or t^0 with
t = e^beta, so the joint weight pi(s)P(s->s') is a single monomial t^E(s,s') and E is an integer.

(1) THE PROOF
  pi(s) = prod_x Z(S_x(s))/Norm and P(s->s') = prod_x exp(beta s'_x . S_x(s))/Z(S_x(s)), so the
  normalisers cancel: pi(s) P(s->s') = exp(beta sum_x s'_x . S_x(s))/Norm.
  sum_x s'_x . S_x(s) = sum_{x} sum_{y in N(x)} s'_x . s_y = sum_{y} sum_{x in N(y)} s_y . s'_x
  = sum_y s_y . S_y(s'), because y in N(x) iff x in N(y) for a symmetric neighbourhood (self-inclusion
  and the +-e_j are both symmetric). Hence pi(s)P(s->s') = pi(s')P(s'->s): detailed balance, and pi is
  stationary. Note this needs no property of the menu beyond the dot product being symmetric.

(2) EXACT VERIFICATION ON THE TWO WINDOWS
  periodic 4-cycle (neighbourhood sizes [3, 3, 3, 3], 1296 states): E(s,s') = E(s',s) for all 1679616 ordered pairs: True  -> detailed balance, since pi(s)P(s->s') = t^E(s,s')/Norm
  periodic 4-cycle: sum_s t^E(s,s') equals prod_x Z(S_x(s')) as a Laurent polynomial in t, for every s': True  -> pi is exactly stationary, for every t at once
  periodic 4-cycle: at beta = 1/2 (t = e^beta = 1.648721) the normalisation is Norm = sum_s prod_x Z = 2810717.919325
  periodic 4-cycle: at beta = 1 (t = e^beta = 2.718282) the normalisation is Norm = sum_s prod_x Z = 16544024.909055
  2x2 torus (neighbourhood sizes [5, 5, 5, 5], 1296 states): E(s,s') = E(s',s) for all 1679616 ordered pairs: True  -> detailed balance, since pi(s)P(s->s') = t^E(s,s')/Norm
  2x2 torus: sum_s t^E(s,s') equals prod_x Z(S_x(s')) as a Laurent polynomial in t, for every s': True  -> pi is exactly stationary, for every t at once
  2x2 torus: at beta = 1/2 (t = e^beta = 1.648721) the normalisation is Norm = sum_s prod_x Z = 8530503.365409
  2x2 torus: at beta = 1 (t = e^beta = 2.718282) the normalisation is Norm = sum_s prod_x Z = 4583974618.890029
  Both checks are for every t at once, not for particular rational stand-ins: detailed balance is the integer
  identity E(s,s') = E(s',s), and stationarity is an identity between Laurent polynomials with integer
  coefficients. The two normalisations quoted at beta = 1/2 and 1 are the numerical value of sum_s prod_x Z.

(3) THE BACKWARD NEIGHBOURHOOD
  backward neighbourhood N(x) = {x, x - e_j}: no longer symmetric, so the identity fails. Kolmogorov's
  criterion settles reversibility for ANY pi: around a cycle the normalisers cancel, so reversibility
  requires E(s,s')+E(s',s'')+E(s'',s) = E(s,s'')+E(s'',s')+E(s',s) for every triple.
  periodic 3-cycle backward: E(s,s') = E(s',s) fails for 31512 of 46656 ordered pairs
  periodic 3-cycle backward: Kolmogorov cycle found - states [4, 5, 1], [0, 3, 0], [1, 0, 2] (menu indices) give forward exponent -5 and backward 0 (difference -5), so the forward and reverse cycle products differ by a factor t^-5: no pi whatever makes this chain reversible
  periodic 4-cycle backward: E(s,s') = E(s',s) fails for 1189800 of 1679616 ordered pairs
  periodic 4-cycle backward: Kolmogorov cycle found - states [4, 5, 1, 1], [0, 3, 0, 3], [1, 0, 2, 4] (menu indices) give forward exponent -3 and backward -2 (difference -1), so the forward and reverse cycle products differ by a factor t^-1: no pi whatever makes this chain reversible
  2x2 torus backward: E(s,s') = E(s',s) fails for 0 of 1679616 ordered pairs
  2x2 torus backward: no Kolmogorov violation found in 200000 random triples  - and none exists: on a torus of side 2, x - e_j and x + e_j are the same site, so the backward neighbourhood IS symmetric there and the window cannot tell the two rules apart
  2x2 torus: with the backward neighbourhood the joint weight is still symmetric in every one of the 1679616 ordered pairs, so that window is reversible under the backward rule as well - it cannot be used to separate the two neighbourhoods

(4) GENERAL SIX-AXIS WEIGHTS
  for general (p,q,r): log W(a,b) = alpha + gamma (a.b) + delta (a.b)^2 with alpha = log(r), gamma = log(p)/2 - log(q)/2, delta = log(p)/2 + log(q)/2 - log(r)
  so the rule's exponent is gamma (a . S_x) + delta * (number of neighbours on a's axis), and what
  replaces s.S is that pair: the dot-product term and the same-axis count.
  Both are symmetric functions of the two records ((a.b) and (a.b)^2 are), so the same double counting
  argument applies to each, and reversibility survives for every (p,q,r) with pi prop. to prod_x Z_x(s).
  periodic 4-cycle: the exponent triple (of p, of q, of r) in pi(s)P(s->s') is symmetric under s <-> s' for all 1679616 ordered pairs: True  -> detailed balance for every (p,q,r), not just q = 1/p
  2x2 torus: the exponent triple (of p, of q, of r) in pi(s)P(s->s') is symmetric under s <-> s' for all 1679616 ordered pairs: True  -> detailed balance for every (p,q,r), not just q = 1/p

(5) THE HIT
  HIT: expectation (3) fails on one of the two windows the task names. The backward neighbourhood {x, x - e_j} does NOT break detailed balance on the 2x2 torus: there x - e_j and x + e_j are the same site, so the backward neighbourhood is symmetric, the joint weight pi(s)P(s->s') is symmetric in all 1679616 ordered pairs (zero asymmetric pairs, no Kolmogorov violation in 200000 random triples), and the backward chain is reversible with respect to the same pi prop. to prod_x Z(S_x). The failure the task expects does appear on the windows of odd or larger side: the periodic 3-cycle has 31512 asymmetric pairs of 46656 and a Kolmogorov cycle off by t^-5, the periodic 4-cycle 1189800 of 1679616 and a cycle off by t^-1. So any side-2 window is blind to the difference between the backward and the light-cone rule.

(6) READING
  (1) and (2) hold exactly, and more strongly than stated: the argument needs nothing of the menu beyond the
  symmetry of the dot product, and it holds for every t simultaneously.
  (3) holds on the periodic 3-cycle and 4-cycle, and there in the strongest form - an explicit Kolmogorov cycle
  whose forward and reverse products differ by a factor of t, which rules out reversibility with respect to ANY
  measure, not just a product-form one. It does not hold on the 2x2 torus, and cannot: on a torus of side 2,
  x - e_j and x + e_j are the same site, so the backward neighbourhood is symmetric there and the backward chain
  is reversible with respect to the same pi. A side-2 window is blind to the difference between the two rules.
  (4) The general weights replace s.S by the pair (gamma (a.S_x), delta x the number of neighbours on a's axis),
  gamma = (log p - log q)/2 and delta = (log p + log q)/2 - log r. Both (a.b) and (a.b)^2 are symmetric in their
  arguments, so the exponent of each of p, q and r is separately symmetric under s <-> s' - verified over all
  1679616 ordered pairs on both windows - and reversibility survives for every (p,q,r), not only for q = 1/p.
