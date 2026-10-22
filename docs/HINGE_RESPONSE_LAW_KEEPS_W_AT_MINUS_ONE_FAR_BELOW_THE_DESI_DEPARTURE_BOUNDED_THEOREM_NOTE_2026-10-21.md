---
claim_id: hinge_response_law_keeps_w_at_minus_one_far_below_the_desi_departure_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Under the register's response law with Lambda a constant per proper 4-volume, the hinge Friedmann law H^2 = X - X^2 l^2/2 + O(l^4) gives |w + 1| of order 1e-121, a uniform rescaling of H projects onto (w0, wa) = (-1, 0) exactly, and every rule effect estimated here projects to |dw| below about 1e-18 for known content and 6e-4 for the heaviest allowed species, against the roughly 0.1 of the DESI fits; the projections are linearised fits to supplied toy BAO errors, and the comparison with DESI is an estimate."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/hinge_response_law_keeps_w_at_minus_one_far_below_the_desi_departure_2026_10_21.py
---

# The hinge response law keeps w at -1, far below the DESI departure

Claim type: bounded_theorem.
Primary runner: `scripts/hinge_response_law_keeps_w_at_minus_one_far_below_the_desi_departure_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its response law fixes Lambda as a constant per proper 4-volume in the hinge part. This note asks how far any rule effect can move the inferred dark-energy equation of state, and so what the register predicts against the DESI fits that prefer w0 > -1, wa < 0. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix no Lambda.

## Statement

1. The hinge area function is A(u) = u^2 + 2u^4 + O(u^6), so H^2 = X - X^2 l^2/2 + O(l^4) with X = (8 pi G/3) rho. An observer using GR with the same G infers w + 1 = -(H l)^2 (3 Omega_m - 1)/(3 Omega_Lambda) when edges grow as l ~ a between splits, and w + 1 = -(H l)^2 Omega_m/Omega_Lambda at a fixed edge.
2. A uniform rescaling H -> lam H at every redshift leaves every D/r_d and the CMB acoustic angle unchanged, so a constant ratio of cosmological to Newtonian G projects onto (w0, wa) = (-1, 0) exactly.
3. Every rule effect estimated here projects to |dw| below about 1e-18 for known content, and below 6e-4 for the heaviest species the rules allow, against the roughly 0.1 of the DESI fits.

## Derivation

Expanding the hinge area function in the edge-to-curvature ratio u gives the series of item 1, and inverting for H^2 gives the correction -X^2 l^2/2. Mapping this onto a GR observer's dark-energy density and differentiating with respect to ln a gives the two expressions for w + 1, which differ according to whether l grows with a or stays fixed. With H0 a = 5.93e-61 (a = sqrt(8 pi) l_P) these are 1.19e-122 and 4.76e-122 for l = a and 2a with growing edges, and -1.58e-121 for l = a fixed, slightly phantom. The legacy main-branch dark-energy notes also predict w = -1, on a different surface (a spectral-gap identity on S^3); their claim of a constant shift with no time dependence does not hold on the hinge carrier, where the correction changes with time at about 1e-121.

BAO distances are ratios D/r_d and the acoustic angle is a ratio of distances, so a uniform factor in H cancels from every one. With Lambda constant and matter conserved, continuity makes the inferred dark-energy density constant; a phantom crossing then needs energy exchange with a varying vacuum term or a non-standard matter or G history. The response law fixes Lambda per proper 4-volume and the register's transport conserves the Born-mean energy, so nothing produces a systematic exchange. Earlier results are cited, not rerun: triggered splits keep Lambda continuous, the nearest-unitary split carries the sea onto the sea, and H has no dependence on the step eps.

The projection engine fits DESI-like BAO (1% errors at the DR2 redshifts) plus the acoustic angle with omega_m and omega_b fixed, fitting h, w0 and wa. A matter step of fractional size delta at a split epoch gives |dw| <= 7.04 delta, and a sawtooth of amplitude s with period ln 2 in ln a (one split cycle) gives |dw| <= 3.87 s.

## Checks

The runner ends with `TOTAL: PASS=8 FAIL=0`. Its lines:

- `[PASS] THEOREM (series): A(u) = u^2 + 2u^4 + O(u^6), so H^2 = X - X^2 l^2/2 + O(l^4), X = (8 pi G/3) rho`.
- `[PASS] hinge law, H0 a = 5.93e-61 ...: w + 1 = -(H0 l)^2 (3 Om - 1)/(3 OL) with edges growing (l ~ a), -(H0 l)^2 Om/OL at fixed edge; exact A(u) at 420 digits matches`.
- `[PASS] engine self-test: a CPL universe (w0, wa) = (-0.75, -0.86) is recovered by the fit  fit w0 -0.7500, wa -0.8600`.
- `[PASS] THEOREM: a uniform rescaling H -> lam H at all z ... leaves every D/r_d and theta* unchanged: it projects onto (w0, wa) = (-1, 0) exactly  max |d obs/obs| = 2e-16 at lam = 1.07`.
- `[PASS] split step response: matter losing a fraction delta at a split epoch z_s gives |dw0|, |dwa| <= C delta  C = 7.04`.
- `[PASS] log-periodic sawtooth in H^2 (period ln 2 in ln a: one split cycle), amplitude s, worst phase: |dw| <= C s  C = 3.87`.
- `[PASS] no rule effect reaches the DESI level: largest known-content |dw| vs needed ~0.1; the cap-allowed ceiling also misses  known content 9e-19; heaviest-allowed ceiling 6e-04; needed f 0.04`.
- `[PASS] SPECULATIVE (not adopted): a constant vacuum decrement per split is thawing (w >= -1, wa < 0) but lies off the DESI degeneracy line wa/(1+w0) ~ -3.4; it needs q ~ 0.4 rho_L0 per split by hand ...  q = 0.5: (-0.761, -0.157)`.

Candidate effects and their projected |dw|: the residual hinge correction 6e-121 and the split-junction slab mismatch 4e-120 (both from the theorems); a rolling step 5e-66 (Lambda never sees eps); the split energy change of radiation 8e-66 (finite diagnostic); that of protons 7e-38 and of the heaviest allowed species (mass angle up to 0.075) 6e-4 (estimates, the latter a ceiling); sea heating at splits 0; an adiabatic reference vacuum about 5e-120 and an instantaneous one about 9e-19 (estimates). An instantaneous reference leaves an induced kinetic coefficient that would shift the gravitational-wave speed, and GW170817 bounds it below about 1e-15, so measurement already forces the adiabatic reference.

## Prediction and estimates against measurement

The response law as written predicts w(z) = -1 with |w + 1| < 1e-18 at all z < 3 for known content and |w + 1| < 1e-3 for any species the rules allow. A robust measurement of |w + 1| > 1e-3 at any redshift, any phantom value, or a log-periodic step in H(z) at 1 + z_k = 2^k (1 + z_0) would falsify it. In practice it stands or falls with LCDM. If BAO + CMB alone, or every supernova compilation, came to exclude (w0, wa) = (-1, 0) at 5 sigma, the failure would be pinned to the clause that Lambda is a constant per proper 4-volume, since every other rule effect is bounded far below detectability. A rough forecast, assuming the DR2 central values hold and errors scale as 1/sqrt(effective volume), moves BAO + CMB from 3.1 to about 4.0 sigma with DESI's five-year data. In the DR2 fits w crosses -1 near z = 0.35 to 0.50 with wa/(1 + w0) between -3.0 and -3.8; the speculative per-split decrement lies off that line and contradicts the response law, so it is not proposed.

## Boundary

Supplied: Lambda itself and the adiabatic reference clause; the unit map a = sqrt(8 pi) l_P with edges between a and 2a; H0 = 67.7, Omega_m = 0.31, omega_m and omega_b; toy 1% BAO errors; the DR2 central values; the massive-split coefficient 0.05 mu^2 (an estimate anchored to one data point); the induced-coefficient size; the kinetic-only effect on the gravitational-wave speed; and the step range. The projections are linearised least-squares fits, not a likelihood, and the forecasts are estimates. No dynamical dark energy is derived; a real DESI signal would need a vacuum term that exchanges energy with matter or a dynamical field, neither of which is in the register.
