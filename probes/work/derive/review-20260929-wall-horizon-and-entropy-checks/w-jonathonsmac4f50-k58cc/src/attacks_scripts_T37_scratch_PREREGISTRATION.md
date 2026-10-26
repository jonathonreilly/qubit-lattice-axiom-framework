# T37 pre-registration (written before any T37 script was run)

Wall: T37 = {L08-W6 (why leptons sit at r = 1/2 and quarks do not), L09-W9 (no native quark mass;
dial does not transfer), L08-W7 (mass scheme/scale of the lepton relation)}.
Dial: x_k = sqrt(m_k), Q = sum m / (sum x)^2, r = (3Q-1)/2. Comparators: charged leptons at POLE
masses; quarks = the repo's common-scale MSbar set (runner
`scripts/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.py`, exec'd
read-only: r_up 0.831 +- 0.002, r_down 0.621 +- 0.008). Nothing is fitted to derive anything; every
"fit" below is a diagnostic of a route, and a fit with as many parameters as data counts as no test.

## S1  Is the spread real, i.e. robust against the mass scheme? (step 1 check; L09-W9, L08-W7 legs)
Compute r_up, r_down under: common-scale MSbar; mixed-as-quoted; one-loop pole factor on c,b,t only;
and an envelope where EVERY entry gets an independent factor in [0.85, 1.15] (a non-common
excursion three times the repo's own one-loop c-vs-t pole-factor difference of ~12%).
- REAL (spread is scheme-robust): envelope minimum r_down >= 0.55 AND r_up >= 0.75.
- SCHEME-SOFT: otherwise (the scheme alone could plausibly hide part of the spread).

## S2  Route A (in-lane dynamics): sector-blind bare r + calculable running. SM one-loop RGEs
Diagonal Yukawas (CKM = 1), start at mu = m_t with MSbar masses (quarks from the repo's RG factor,
leptons from pole masses + one-loop QED), run to M_Pl = 1.22e19 GeV. Track r_e, r_d, r_u.
Spread(mu) = max_s r_s - min_s r_s. IR spread at mu = m_t is ~0.33.
- PASS (a sector-blind r at some scale is dynamically plausible): min over mu in [m_t, M_Pl] of
  Spread(mu) <= 0.10.
- FAIL: min Spread(mu) > 0.20.  Between: inconclusive.
Expectation stated in advance (from the repo's own T36 P4 and the flavour-universality of gauge
running): FAIL.

## S3  Route A': flavour-blind dressing families shared between the two quark sectors
(a) power tilt m -> m^(1+eta); (b) additive shift m -> m + Delta (constituent-mass-like), masses
taken at 2 GeV. Solve for the smallest |parameter| giving r = 1/2 in the down and up sectors.
- PASS (a shared dressing is plausible): tilt: eta_d and eta_u have the same sign and differ by
  <= 25%; shift: Delta_d, Delta_u both in [0.15, 0.6] GeV and within a factor 1.5 of each other.
- FAIL: otherwise.
Expectation: FAIL (the up hierarchy is ~3x longer).

## S4  Route B (outside-lane sector link): Georgi-Jarlskog-type integer Clebsch factors
(H. Georgi, C. Jarlskog, Phys. Lett. 86B (1979) 297: m_d = 3 m_e, m_s = m_mu/3, m_b = m_tau at the
unification scale.) Build the down-type triple from lepton POLE masses, r_d^GJ and the Brannen
phase delta_d^GJ (same branch convention as delta_lep = 2/9), compare with the data common-scale
r_d = 0.621 +- 0.008 and the data delta_d. Then the same with all six masses run to 2e16 GeV.
Look-elsewhere: all 7^3 = 343 triples (k1,k2,k3) from {1/3,1/2,2/3,1,3/2,2,3} for
m_d,m_s,m_b = (k1 m_e, k2 m_mu, k3 m_tau); count how many land within 0.02 of r_d^data.
- LIVE (as an outside template): |r_d^GJ - r_d^data| <= 0.02 AND the look-elsewhere hit fraction
  <= 5% AND |delta_d^GJ - delta_d^data| <= 0.05 rad.
- WOUNDED: r_d passes but the hit fraction > 5% or delta_d fails (postdiction, trial factor).
- DEAD: |r_d^GJ - r_d^data| > 0.05.
Also: does any analogous link exist for the up sector (needs a partner sector with a measured
dial)? Only the neutrino Dirac partner (SO(10)) - unmeasured; reported, not tested.

## S5  Route A'': abelian / electroweak-charge laws (the wall's own "cheapest test")
Quantum numbers of the left-handed fields: nu (T3 1/2, Y -1/2, Q 0), e (-1/2, -1/2, -1),
u (1/2, 1/6, 2/3), d (-1/2, 1/6, -1/3). Fit r = r0 + alpha T3 + beta Y to (e, d, u) (3 parameters
for 3 data = no test) and predict r_nu; also r = r0 + kappa Q (2 parameters, 1 dof).
r_nu band: oscillation data (NO: dm21^2 = 7.42e-5, dm31^2 = 2.515e-3 eV^2; IO: |dm32^2| = 2.498e-3),
lightest mass m0 in [0, 0.3] eV, r_nu = (3Q-1)/2 (Dirac-type sqrt(m) dictionary, band only).
- LAW SURVIVES: predicted r_nu inside the achievable band (both the (T3,Y) law and the Q law
  tested separately; the Q law also must reproduce r_u to within 0.06).
- LAW DEAD: predicted r_nu outside the band by > 0.1, or the Q law misses r_u by > 0.06.
Also list |Q|-ordering: any C-even rule f(Q^2) must order d < u < e by |Q| - report whether
monotone against e < d < u.

## S6  Misframing check: r is the top-two hierarchy in Koide coordinates
For each sector compute r from the full triple and from the two-generation truncation (x1 -> 0),
and tabulate m3/m2 that gives r = 1/2, r_d, r_u at x1 = 0.
- MISFRAMING SUPPORTED: |r_full - r_trunc| <= 0.03 for all of e, d, u (the dial is essentially the
  m3/m2 ratio), so the sector spread is a hierarchy statement in other coordinates.
- NOT SUPPORTED: otherwise.

## Outcome rule
- If S1 REAL, S2 FAIL, S3 FAIL, S5 DEAD, S4 WOUNDED or DEAD, S6 SUPPORTED: outcome PRICED
  (price: per-sector r as sector-labelled realized-state data, i.e. the same state-selection input
  as T36 plus the scheme convention), with the GJ-type link named as the only route that survives
  as an external template and what it would still need.
- If S4 LIVE: STANDS with the link route as best route (or MISFRAMED if the link removes the
  modulus problem for d and leaves only u).
- If S1 SCHEME-SOFT: report the part of the wall that is a scheme issue as MISFRAMED for that part.
