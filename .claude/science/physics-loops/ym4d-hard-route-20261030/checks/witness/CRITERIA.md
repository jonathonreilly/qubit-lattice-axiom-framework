# Criteria for queue item 8f (nt2-rewrite), written before any run

Source: `be5e58b30`. Worker anthropic/claude-opus-5-5/max mac-mini-worker, 2026-11-01.
Each run: numeric lock, BLAS threads 1, `nice`, self-stop above 2 GB RSS, 50 percent memory free or more.

## W1. No gauge-invariant observable reads the vertex alone (`v0_jets.py`)

Claim under test (Proposition V0): if a finite linear combination of T has zero quartic jet, it has zero cubic jet.

- Build T jets on a small lattice from the part's BCH formulas for t_3 and t_4 (Text 0). Cross-check both jets against a finite-difference Taylor fit of the exact SU(2) product.
- Pass: jet check agrees to 1e-6 relative; every null vector of the t_4 evaluation matrix has t_3 norm below 1e-9 of the largest singular value.
- Fail: a null vector with non-zero t_3. That is a pure-vertex combination, Proposition V0 is false, and the chart-free clause should use it.
- Report: rank of the t_3 map, rank of the t_4 map, dimension of the null space. The test is a finite search. It does not replace the proof.

## W2. The blocked near covariance (`near_flux.py`)

Claim under test: for the map (B-1) in the limit n -> infinity, plaquette flux is the average of F_ab against a positive density, and P_infinity at an ordered offset is the Maxwell tensor averaged against B-splines.

- Compute P_infinity at each listed offset in two ways: a rounded-out enclosure in position space (exact spline masses on sub-boxes, monotone bounds of the rational kernel), and the Fourier integral (B-4) by Schwinger parameter.
- Pass: Fourier value inside the enclosure, and the relative width of the enclosure at most 0.2 at the near offset.
- Fail: Fourier value outside the enclosure.
- Report: the enclosure is a computed bound, valid up to floating-point rounding, which is far below its width. It says nothing on the actual Wilson law.

## W3. The fibre split (`fibre_split.py`)

Claim under test: P^fib = P^inf - delta, delta >= 0 as a form, with delta_pp of order L^-4 and P^fib -> P_infinity at fixed offset as L grows.

- Bloch formula with rank-3 coarse closed currents, Schwinger parameter for the sum over l.
- Pass: (a) L = 1 gives P^fib = 0 to 1e-3 relative on a plaquette; (b) a W-measurable test current has fibre variance below 1e-3 relative at L = 3; (c) delta_pp >= 0 and delta_pq^2 <= delta_pp delta_qq at every L; (d) L^4 delta_pp changes by at most 15 percent from L = 15 to L = 21.
- Fail: any of (a) to (c). If only (d) fails, report the trend and do not claim a power.
- Report: table of P^inf, delta, P^fib for L = 3 to 21. This is a computed value, not a bound.

## W4. Singlet RP reads the reflected kernel (`singlet_rp.py`)

Claim under test (Lemma R4): at small amplitude, E[Theta F F] for F = sum c_kl B(Gamma_k, Gamma_l) has leading term (h^4/16)[9 (Tr cP)^2 + 6 Tr(cRcR)].

- Exact check of the Wick coefficient 9, 3, 3 by direct enumeration of pairings; then Monte Carlo on a small lattice with a Gaussian potential of non-RP reflected kernel.
- Pass: Wick enumeration exact; Monte Carlo sign of E[Theta F F] negative by at least 4 standard errors at the chosen small h, with c chosen from the kernel only.
- Fail: the Monte Carlo value is positive by 4 standard errors. Then the leading term is not what the lemma says.

## W5. The abelian top-down law (`abelian_td.py`)

Claim under test: for a finite-depth abelian Gaussian top-down law on a d = 3 lattice, the reflected flux kernel is positive at constant amplitude and has a negative eigenvalue at a decreasing amplitude.

- Pass: constant amplitude, smallest eigenvalue at least -1e-9 relative. Decreasing amplitude: smallest eigenvalue below -1e-6 relative.
- Fail: a negative eigenvalue at constant amplitude means the code is wrong.
- Report: this is the abelian analogue only. It does not decide RP for SU(2) mu^TD.
