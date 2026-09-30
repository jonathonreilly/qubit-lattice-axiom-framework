# T78 pre-registration (written before any production run)

Date: 2026-09-29. Author: Claude Sonnet 5.5 (same vendor family as supervisor; same-family check only).

## Question
Near the RK point (V = K - eps), the model H = -K sum F_p + V sum F_p^2 has, by Hellmann-Feynman on each
plaquette-flip component C (finite volume), E_C(eps) = -eps <N_f>_C + O(eps^2), with <N_f>_C the mean number of
flippable plaquettes in the UNIFORM ensemble of C (this is the RK ground state's weight).
So the electric stiffness of the winding sectors to first order in eps is
   Delta E(q) = E(q) - E(0) = eps [<N_f>_0 - <N_f>_q] = eps * c_L * q^2 / L      (Phi = q, prior-art convention of
   docs/SPIN_HALF_CUBIC_ICE_POSITIVE_TOPOLOGICAL_ELECTRIC_STIFFNESS_..._2026-09-03.md).
A Maxwell-type (linear-photon) low-energy theory near RK needs U = 2 c eps to stay positive as L -> infinity, i.e.
c_L -> c_inf > 0.  A quadratic-only (Lifshitz) low-energy theory near RK would have c_L -> 0 (power law in 1/L).

Prior data (same quantity, main, 2026-09-03, chains ~ 10% errors): c_L = 1.67(14), 1.88(15), 1.45(16), 1.26(17)
at L = 6, 8, 10, 12. That sequence is ambiguous (flat within ~2 sigma but its last two points drift down).

## Test (cheapest decisive on this premise)
High-statistics classical MC of the uniform ice ensemble (directed-loop reversal, flux-sector preserving),
L = 4, 6, 8, 12, 16, 24 (as time allows), flux q values with q <= L/2, fit <N_f>(L,q) = a_L - c_L q^2/L.
Validation first: L = 2 sector-uniform means must equal exact rationals 432/55 (q=0, whole 880-state sector)
and 188/29 (q=1, 464 states) up to MC error.

## Pass / fail readings (fixed now)
- PASS-for-linear (premise "first-order stiffness survives the thermodynamic limit" supported):
  c_L for L in {12,16,24} agree with their mean within 2 sigma each, and the fitted power law
  c_L ~ L^(-p) has p < 0.25 with p = 0 inside 2 sigma. And c_inf > 0.5 (i.e. > 5 sigma from 0).
- FAIL (near-RK electric stiffness vanishes; evidence FOR quadratic-only): p > 0.5 at 2 sigma, or c_24 < 0.5 c_8.
- INCONCLUSIVE: otherwise; then state the observed p and its error and what size would decide.
- Validation FAIL (sampler wrong): L=2 means off from 432/55 or 188/29 by > 3 sigma. Then no production result is claimed.
- Secondary: the ratio [<N>_0 - <N>_{2q}]/[<N>_0 - <N>_q] should be 4 (Gaussian, quadratic in q); report it.
- Secondary: c_L * 2 = U_fit/eps should be compared with the pure-ring U_W (1.46, 1.11, 0.67 at L=4,6,8 in the
  2026-09-25 winding note; convention factor 2 stated in the report).

## What this test can NOT decide
It gives no lower bound on any excitation energy, does not test the O(eps^2) remainder's uniformity in L,
and does not test single-mode dominance or the absence of an ordering/confining transition.
