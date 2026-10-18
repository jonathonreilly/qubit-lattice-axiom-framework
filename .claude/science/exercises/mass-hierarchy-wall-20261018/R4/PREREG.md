# R4 pre-registration (written 21:15Z, before any run)

Route agent R4: geometric / number-theoretic origins of masses
(worldsheet-area hierarchies, lattice spectra, Koide-type relations).

## Data (comparators, recalled, not fetched)
- MZ set (Xing-Zhang-Zhou MS-bar at M_Z, GeV): u 1.38e-3, c 0.638, t 172.1;
  d 2.82e-3, s 0.057, b 2.86; e 0.4866e-3, mu 0.10272, tau 1.7462.
- LOW set: u 2.16e-3, d 4.67e-3, s 0.0934 (2 GeV); c 1.27, b 4.18 (self scale);
  t 172.69 (pole); leptons pole 0.51099895e-3, 0.1056583755, 1.77686.
- CKM: |V_us| 0.2243, |V_cb| 0.0410, |V_ub| 0.00382.
- Tolerance: every mass within x3 (|ln| <= ln 3); CKM within x3.

## Null models (random spectra)
- N1: all 9 masses iid log-uniform on [m_e, m_t] (observed span), sorted per sector.
- N2: per sector heaviest fixed at observed; the two lighter log-uniform on
  [1e-6, 1] x heaviest, sorted.
- CKM null: |V_us|,|V_cb|,|V_ub| iid log-uniform on [1e-4, 1].

## Tests
- T0 (unexponentiated spectra). Values of lattice Bloch energies at
  high-symmetry momenta (k_i in {0, pi/3, pi/2, 2pi/3, pi}) for naive Dirac,
  Wilson-Dirac (r=1), Laplacian and the walker cos w = prod cos k_i; 3D and 4D;
  cubic-group integers. Report the largest ratio of two nonzero values.
  Prediction: <= O(10), so no large ratios without an exponential map.
- T1a (scalar exponential ladders). m_i = Lambda_f b^{S_i}. Library of exponent
  triples from hop counts {0..4} and squares {0,1,4,9,16}; library of
  lattice-fixed bases (alpha_bare, alpha_LM, alpha_s(v), <P>, u0, 1/2..1/16,
  e^-pi, e^-pi/2, 1/(16 pi^2)). Variants: universal (b,S); per-sector S with
  universal b; per-sector (b,S); continuous per-sector base (shape-only test).
  Score = largest factor off. Report observed pass/fail and N1/N2 pass rates.
  Prediction: per-sector choices pass for observed AND >50% of random spectra
  (no evidence); universal choices fail for observed.
- T1b (worldsheet-area texture). Y_ij = exp(-sigma A(l_i, h, r_j)) with
  A = lattice (L1) area of the triangle, l = {e_x,e_y,e_z}, r = hw1 or hw2
  orbit translated by t in {-1,0,1}^3, h in {-1..2}^3, sigma universal over
  sectors. Masses = singular values x Lambda_f. CKM = U_u^dag U_d.
  Prediction: masses pass at per-sector configuration choice for observed and
  for most random spectra; masses + CKM jointly fail for observed.
- T2 (Koide control). Observed Q and Brannen delta per sector; probability
  under N1 that a random triple sits as close to a simple rational
  (denominator <= 12) as observed leptons do, with trials counted.
  Quark sectors: nearest simple (r, delta) and whether x3 is met; random pass
  rate of the same grammar. Prediction: lepton Koide is significant
  (p < 1e-3 after trials); quark Koide-type fits are at the random rate.
- T3 (grammar density). For the main-branch formula grammar c * alpha_s(v)^p
  (p rational, denominator <= 6; c small-integer ratios and square roots),
  probability that a random target in [1e-4, 1] is matched within 1.3%, 3%,
  3.3%. Prediction: near 1, so those hits carry no evidence.

## Kill conditions (per route)
- Route W (area/hop ladder): killed as evidence if observed pass and N1 pass
  rate >= 50% at the same library level, or if no level passes observed.
- Route K (twisted circulant): killed for quarks if no simple (r, delta) beats
  the random rate.
