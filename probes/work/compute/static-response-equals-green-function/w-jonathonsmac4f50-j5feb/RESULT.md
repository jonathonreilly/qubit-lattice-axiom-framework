static-response-equals-green-function, independent run 1 of 2
worker w-jonathonsmac4f50-j5feb (claude-opus-5), unit C-static-response-equals-green-function-a1

Linear light-cone formation on Z^3: theta_{t+1} = P theta_t + noise + f delta_0, with P the average over a site
and its six neighbours (n = 7 predecessors).
Overlap disclosure: the identity 1 - phi = E/7 is the one I proved in C:static-against-lightcone-kernel:a2 and
used again in C:meanfield-threshold-by-dimension:a2; the operator form, the field coefficient and the
fluctuation-response check here are new.

(1) THE STATIONARY MEAN IS THE LATTICE GREEN FUNCTION TIMES SEVEN
  (P theta)(x) = (1/7)[theta(x) + sum_{6 neighbours} theta(y)], so
    ((1 - P) theta)(x) = (6 theta(x) - sum_{neighbours} theta(y))/7 = (-Delta theta)(x)/7 exactly,
  with -Delta the Z^3 lattice Laplacian whose symbol is E(k) = 2 sum_j (1 - cos k_j). Hence
    (1 - P)^{-1} = 7 (-Delta)^{-1}: the lattice Green function times 7, symbol 7/E(k).
  symbol check 1 - phi(k) = E(k)/7: True
  L=3: 1 - P equals (-Delta)/7 entrywise: True; the exact solution of (1-P)R = delta - 1/N satisfies its equation: True; R = 7 G entrywise with G the lattice Green function: True; R(0) = 308/243 = 1.267490
  L=4: 1 - P equals (-Delta)/7 entrywise: True; the exact solution of (1-P)R = delta - 1/N satisfies its equation: True; R = 7 G entrywise with G the lattice Green function: True; R(0) = 10619/7680 = 1.382682
  L=5: 1 - P equals (-Delta)/7 entrywise: True; the exact solution of (1-P)R = delta - 1/N satisfies its equation: True; R = 7 G entrywise with G the lattice Green function: True; R(0) = 30044/20625 = 1.456679
  The operator statement is stronger than the symbol statement and needs no Fourier transform: the averaging
  operator over a site and its six neighbours differs from the identity by exactly one seventh of the lattice
  Laplacian, entrywise, on every torus.

(2) THE FIELD
  with the predecessors aligned, S = n u, the weight exp(beta s.S + h s.t) is the von Mises-Fisher law
  with concentration vector V = n beta u + h t, so |V| = sqrt(n^2 beta^2 + h^2) and
    mean DIRECTION V/|V|: transverse part h/sqrt(n^2 beta^2 + h^2) = h/(n beta) + O(h^3),
    mean VECTOR A(|V|) V/|V|: transverse part A(sqrt(n^2 beta^2 + h^2)) h/sqrt(n^2 beta^2 + h^2)
                              = A(n beta) h/(n beta) + O(h^3) = sigma^2 h,  sigma^2 = A(n beta)/(n beta).
  So the exact first-order coefficient is A(n beta)/(n beta) for the mean record and 1/(n beta) for its
  direction: the 'something' is 1, and the two differ by exactly A(n beta).
  the simulator's quoted ratios against A(n beta):
    light cone: n=7 beta=6.0 -> A(n beta) = 0.9762, quoted 0.99 (difference 0.0138); 1/(n beta) = 0.023810, A(n beta)/(n beta) = 0.023243
    backward: n=4 beta=6.0 -> A(n beta) = 0.9583, quoted 0.96 (difference 0.0017); 1/(n beta) = 0.041667, A(n beta)/(n beta) = 0.039931
  finite h (n=7): h | transverse mean direction | transverse mean vector | ratio to h sigma^2
    beta=2.0 h=0.01: 0.00071429 | 0.00066327 | 1.000000
    beta=2.0 h=0.05: 0.00357141 | 0.00331631 | 0.999994
    beta=2.0 h=0.2: 0.01428426 | 0.01326406 | 0.999906
    beta=2.0 h=1.0: 0.07124705 | 0.06617091 | 0.997654
    beta=6.0 h=0.01: 0.00023810 | 0.00023243 | 1.000000
    beta=6.0 h=0.05: 0.00119048 | 0.00116213 | 0.999999
    beta=6.0 h=0.2: 0.00476185 | 0.00464847 | 0.999989
    beta=6.0 h=1.0: 0.02380278 | 0.02323621 | 0.999724
  quadrature check of the vMF mean at |V|=14.0: <cos> = 0.9285714286 vs A(|V|) = 0.9285714286
  quadrature check of the vMF mean at |V|=42.0: <cos> = 0.9761904762 vs A(|V|) = 0.9761904762
  quadrature check of the vMF mean at |V|=5.0: <cos> = 0.8000908040 vs A(|V|) = 0.8000908040

(3) THE FLUCTUATION-RESPONSE RELATION
  L=3: (1 + P) C / sigma^2 equals (1 - P)^{-1} exactly: True  (C(0) = 59143/53460 sigma^2 = 1.106304 sigma^2)
  L=4: (1 + P) C / sigma^2 equals (1 - P)^{-1} exactly: True  (C(0) = 18179/15360 sigma^2 = 1.183529 sigma^2)
  L=5: (1 + P) C / sigma^2 equals (1 - P)^{-1} exactly: True  (C(0) = 79542661478/65247579375 sigma^2 = 1.219090 sigma^2)
  the identity is (1+P)(1-P^2)^{-1} = (1-P)^{-1}, which needs P self-adjoint - true for this symmetric
  neighbourhood. On the backward lattice P is not self-adjoint and the relation fails (the response is
  one-sided while the covariance is inversion symmetric).

(4) READING
  (1 - P)^{-1} = 7 (-Delta)^{-1} exactly, so the stationary mean of a pinned source is f times seven lattice
  Green functions, with symbol 7/E(k); on L = 3, 4, 5 the exact rational solution equals 7G entrywise, with
  R(0) = 308/243, 10619/7680 and 30044/20625.
  The field's exact first-order coefficient is A(n beta)/(n beta) = sigma^2 for the mean record and 1/(n beta) for
  its mean direction - the factor between them is exactly A(n beta), and the finite-h correction is below 0.03
  percent up to h = 1 at beta = 6. Against the simulator's quoted ratios, A(n beta) is 0.9762 for the light cone
  at beta = 6 (quoted 0.99, 1.4 percent away) and 0.9583 for the backward lattice at beta = 6 (quoted 0.96, 0.2
  percent away), so the quoted numbers are the A(n beta) factor, measured.
  The fluctuation-response relation (1 + P) C/sigma^2 = (1 - P)^{-1} holds exactly, as rational identities on
  every torus checked. It rests on P being self-adjoint, which the symmetric light cone is and the backward
  neighbourhood is not.
  Everything the task states is confirmed; no HIT. Numbers, not a verdict on the physics.
