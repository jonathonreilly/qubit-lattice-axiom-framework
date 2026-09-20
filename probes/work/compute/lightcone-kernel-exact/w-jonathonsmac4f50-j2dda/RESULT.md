lightcone-kernel-exact, independent run 2 of 2
worker w-jonathonsmac4f50-j2dda (claude-opus-5), unit C-lightcone-kernel-exact-a2

The light-cone formation kernel on the 3+1 event lattice: seven predecessors {0, +-e_1, +-e_2, +-e_3},
phi(k) = (1 + 2 sum_j cos k_j)/7, linear gain-one model theta_{t+1} = P theta_t + noise,
sigma^2 = A(7 beta)/(7 beta).
Overlap disclosure: phi = 1 - E/7 and 1 - phi^2 = E(14-E)/49 are identities I proved in
C:static-against-lightcone-kernel:a2 and used in C:meanfield-threshold-by-dimension:a2 and
C:static-response-equals-green-function:a1; the partial-fraction split, the exponential rates and the exact
torus identity below are new here.

(1) THE KERNEL
  phi(k) = 1 - E(k)/7 with E(k) = 2 sum_j (1 - cos k_j): True
  1 - phi^2 = E(14 - E)/49: True
  sigma^2/(1 - phi^2) = (7 sigma^2/2)/(E (1 - E/14)): True
  so the kernel is the lattice Green function 1/E times 1/(1 - E/14); E runs over [0, 12] on the zone,
  so that factor runs over [1, 7]: 1 at k = 0 and exactly 7 at the corner E = 12, where
  phi(pi,pi,pi) = -5/7 and 1 - phi^2 = 24/49
  the factor is monotone in E, so [1, 7] is the exact range; at E = 7 (half the zone) it is 2

(2) REAL SPACE: THE CORRECTION TO THE GREEN FUNCTION
  1/(E(1 - E/14)) = 14/(E(14 - E)) = 1/E + 1/(14 - E), so
    C(x) = (7 sigma^2/2) [G(x) + H(x)],  G the Z^3 lattice Green function, H the transform of 1/(14 - E).
  check of the partial fractions: True
  shifting k by (pi,pi,pi) sends E to 12 - E, and 14 - E(k+pi) = 2 + E(k): True
  so H(x) = (-1)^{x_1+x_2+x_3} K(x) with K the massive lattice propagator of mass^2 = 2, the transform of
  1/(2 + E(k)). That is analytic on the zone (2 + E >= 2 > 0), so H decays exponentially, not as 1/r^3.
  the rate along an axis solves 2 + 2(1 - cosh mu) = 0, i.e. cosh mu = 2: mu = log(sqrt(3) + 2) = 1.316958 per site (= log(2 + sqrt 3))
  along the diagonal 2 + 6(1 - cosh mu) = 0, i.e. cosh mu = 4/3: mu = log(sqrt(7)/3 + 4/3) = 0.795365 per site in each coordinate, i.e. 1.377613 per unit length

(3) SPACE-TIME
  the space-time covariance is sigma^2 phi^s/(1 - phi^2); phi is real and even in k, so the lag-s kernel
  is symmetric in x -> -x: there is no drift, unlike the four-predecessor backward lattice.
  one-level recursion C_{s+1} = phi C_s: True
  the per-level decay rate is -log|phi| = -log(1 - E/7) = e**2/98 + e/7 + ... = E/7 + E^2/98 + O(E^3)
  (for E > 7 phi is negative and |phi| = E/7 - 1, the mode alternating in sign from level to level)

(4) EXACT VERIFICATION ON SMALL TORI (rational arithmetic)
  L=3: the stationary equation (1 - P^2) C = sigma^2 (delta - 1/N) holds exactly and sum C = 0: True; C(0) = 59143/53460 sigma^2 = 1.106304 sigma^2; every lag kernel C_s = P^s C is symmetric under x -> -x (no drift) for s = 1..4: True
  L=3: sum_x H(x) = 1/14 (must be 1/14 = the symbol at k = 0): True; C(x) = (7/2)(G(x) + H(x)) - 1/(4N) entrywise: max deviation 0 -> exact: True
  L=4: the stationary equation (1 - P^2) C = sigma^2 (delta - 1/N) holds exactly and sum C = 0: True; C(0) = 18179/15360 sigma^2 = 1.183529 sigma^2; every lag kernel C_s = P^s C is symmetric under x -> -x (no drift) for s = 1..4: True
  L=4: sum_x H(x) = 1/14 (must be 1/14 = the symbol at k = 0): True; C(x) = (7/2)(G(x) + H(x)) - 1/(4N) entrywise: max deviation 0 -> exact: True

(5) FFT CHECKS
  the correction H(x) at L = 64 and 128: its magnitude along the axis and the diagonal, and the fitted
  exponential rate against the exact arccosh values
  L=64: max |C - (G + H)| = 2.72e-07 (in units of 7 sigma^2/2)
    L=64 H along (1,0,0): r=1:-2.124e-02 r=2:+3.510e-03 r=3:-6.328e-04 r=4:+1.231e-04 r=5:-2.545e-05 r=6:+5.517e-06 r=7:-1.239e-06 r=8:+2.858e-07
    L=64 fitted rate along (1,0,0) from log(r|H|), r = 3..8: 1.344901 against the exact 1.316958 (ratio 1.0212); from log|H| alone it would read 1.538196, the difference being the 1/r prefactor
    L=64 r^3 |H| along (1,0,0) (flat would mean a 1/r^3 law): r=1:2.124e-02 r=2:2.808e-02 r=3:1.708e-02 r=4:7.877e-03 r=5:3.181e-03 r=6:1.192e-03
    L=64 H along (1,1,1): r=1:-2.702e-03 r=2:+1.353e-04 r=3:-8.525e-06 r=4:+5.957e-07 r=5:-4.417e-08 r=6:+3.402e-09 r=7:-2.692e-10 r=8:+2.172e-11
    L=64 fitted rate along (1,1,1) from log(r|H|), r = 3..8: 2.380200 against the exact 2.386096 (ratio 0.9975); from log|H| alone it would read 2.573495, the difference being the 1/r prefactor
    L=64 r^3 |H| along (1,1,1) (flat would mean a 1/r^3 law): r=1:2.702e-03 r=2:1.083e-03 r=3:2.302e-04 r=4:3.813e-05 r=5:5.521e-06 r=6:7.348e-07
  L=128: max |C - (G + H)| = 3.41e-08 (in units of 7 sigma^2/2)
    L=128 H along (1,0,0): r=1:-2.124e-02 r=2:+3.510e-03 r=3:-6.328e-04 r=4:+1.231e-04 r=5:-2.545e-05 r=6:+5.517e-06 r=7:-1.239e-06 r=8:+2.858e-07
    L=128 fitted rate along (1,0,0) from log(r|H|), r = 3..8: 1.344901 against the exact 1.316958 (ratio 1.0212); from log|H| alone it would read 1.538196, the difference being the 1/r prefactor
    L=128 r^3 |H| along (1,0,0) (flat would mean a 1/r^3 law): r=1:2.124e-02 r=2:2.808e-02 r=3:1.708e-02 r=4:7.877e-03 r=5:3.181e-03 r=6:1.192e-03
    L=128 H along (1,1,1): r=1:-2.702e-03 r=2:+1.353e-04 r=3:-8.525e-06 r=4:+5.957e-07 r=5:-4.417e-08 r=6:+3.402e-09 r=7:-2.692e-10 r=8:+2.172e-11
    L=128 fitted rate along (1,1,1) from log(r|H|), r = 3..8: 2.380200 against the exact 2.386096 (ratio 0.9975); from log|H| alone it would read 2.573495, the difference being the 1/r prefactor
    L=128 r^3 |H| along (1,1,1) (flat would mean a 1/r^3 law): r=1:2.702e-03 r=2:1.083e-03 r=3:2.302e-04 r=4:3.813e-05 r=5:5.521e-06 r=6:7.348e-07

(6) READING
  The light-cone kernel is the Z^3 lattice Green function times 1/(1 - E/14), a factor whose exact range on the
  Brillouin zone is [1, 7]: 1 at long wavelength and exactly 7 at the zone corner, where phi = -5/7.
  The split is exact and not just asymptotic: 14/(E(14 - E)) = 1/E + 1/(14 - E), so
  C(x) = (7 sigma^2/2)(G(x) + H(x)), and H is the mass-squared-2 lattice propagator carried to the zone corner,
  H(x) = (-1)^{x_1+x_2+x_3} K(x) with K the transform of 1/(2 + E). Being analytic on the zone, it decays
  exponentially - at log(2 + sqrt 3) = 1.316958 per site along an axis (fitted 1.3449 from log(r|H|), r = 3..8)
  and 3 arccosh(4/3) = 2.386096 along the diagonal (fitted 2.3802) - and not as 1/r^3: r^3|H| falls by four
  decades between r = 1 and r = 6 instead of staying flat.
  On the torus the identity is exact over the rationals: C(x) = (7/2)(G(x) + H(x)) - 1/(4N), the constant being
  the zero mode that C has had removed and H, whose symbol is finite at k = 0, has not.
  The space-time kernel sigma^2 phi^s/(1 - phi^2) is symmetric in x -> -x at every lag (checked exactly for
  s = 1..4 on both tori): the symmetric neighbourhood has no drift, unlike the four-predecessor backward lattice.
  Its per-level rate is -log|phi| = -log(1 - E/7) = E/7 + E^2/98 + O(E^3), the task's E/7 being the first term.
  All four parts hold; no HIT.
