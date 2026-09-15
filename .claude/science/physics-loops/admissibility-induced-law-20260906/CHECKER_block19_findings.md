# Refuting pass — block 19 (supervisor-run, disjoint machinery; 2026-09-15)

Routes compared (control `specs/supervisor_control_block19_sphere_static.py`, refuting pass `specs/supervisor_control_block19_refuter.py`, outputs in `.out.txt`):

| item | runner's route | refuting route | result |
|---|---|---|---|
| the Legendre coefficients of `e^{βt}` (G1) | the Rodrigues form against direct integration, symbolically in `β`, `ℓ ≤ 4` | the orthogonality route with the Taylor series of `e^{βt}` truncated at order 40, at `β = 1, 3`, `ℓ ≤ 3` | agree to `10^{−12}`; all positive |
| the gradient sum of the plane wave (G2) | the `4³` torus at two wavevectors | direct bond enumeration on a `6×4×4` torus at `k = (π/3, 0, 0)` (`E = 1`): `48 = E · N/2` | equal |
| the single-bond second-derivative identity (G4) | the generator about `e_2` | the generator about `e_1` (transverse pair `(s^2, s^3)`) | the same identity |
| the cosine inequality and the ball integral (G3) | sample points; the radial integral | the Taylor lower bound `u²/2 − u⁴/24` at the sample points; the ball integral in spherical coordinates | consistent; `4√3π²` |

Findings: none in the primary. The control caught the generator's sign convention (`L s^3 = −s^1`, `L s^1 = s^3`) before the contract; it enters G4 only through an absolute value.

Attempts to refute (nothing refuted): G2's domination step was re-read for the crossing bonds after the site shift (the crossing weight is the untwisted positive-definite kernel; the shifted site measures are single-site factors; the iteration ends at fields constant along every direction, where `Z` equals `Z(0)`); G2's expansion for wavevectors with `2k = 0` (the gradient sum is then `E(k) N`, which only strengthens the bound); G3's Riemann-sum limit (the integrand's singularity `π²/(4|k|²)` is integrable in three dimensions); G4's use of `|m̂| ≤ 1` and of the component symmetry `⟨m̂²⟩ = M_N²/3`; G5's subsequence for a fixed wavevector. Verdict of this pass: PASS-NO-BLOCKER at the supervisor's own standard, pending the owner's independent review.
