# Focused coupling reconstruction check

The baseline/pulse reconstruction and reciprocal-potential condition are mathematically supported within the anchored restricted class. One notation clarification is needed for the claimed all-pairs error bound: unsigned integrals in (14) must be over [min(x,y),max(x,y)], not oriented from x to y. This qualification was reported to root. No other material defect found. This is not a formal audit, landing review, empirical validation or novelty judgment.

Complete note read and independent derivation written before code inspection. Complete code and control JSON then read. Exact frozen sources:

- COUPLING_RECONSTRUCTION_v1.md: 237145817f188a4e3e5a19a1ac1b451bcdceeb03f7bdcaeda824f94f4d908679
- check_coupling_reconstruction_v1.py: 565a7fb25599691a655716ac9f0666a8f9ae68acab312a4a716f948257b2262d
- COUPLING_CONTROLS_v1.json: 19a2d5ed9faea2c37acf28f62cdd765fffd858e76a2446d3df8960adf2887308

## Findings and proof scope

Three same-run samples determine the affine oscillator continuation when the stated observation matrix is invertible. It is not necessary to recover the physical hidden state or static source offset separately. Unknown and unrelated hidden preparations between runs genuinely cancel. Pole/time calibration, observability, numerical conditioning and drift remain assumptions; steady records cannot identify poles, and aliased times can lose rank. Matrix exponentials cover repeated poles, although the author's Green-function numerical example is underdamped only. Independent computations cover undamped, critically damped and overdamped cases.

Variation of constants gives the negative pulse response -a(x)[b(y)-b(x)]J/tau with zero difference initial data. Same-run prehistory and no hidden impulsive derivative coupling are essential. The physical-transition bound is valid for matching prehistory and common returned readout, using a causal integration range; it does not account for settling or moving-coordinate delayed forces. Fixed linear baseline error amplification and ratio errors are correct, with positive true-denominator margin required. The positive early-lag sign of J must be established, not extrapolated to an arbitrary late oscillatory window.

Centered rank-one factorization reconstructs relative A,B only. Its converse uses both the definition E=D(x,y)-D(x,z) and D(x,x)=0, and applies to the pulse surface, not arbitrary histories. It cannot count modes or prove continuum functions from finite values. The selected polynomial degrees in the synthetic fit are explicitly chosen, including predictions beyond the development grid; this is a numerical control, not empirical identification.

Within the stated constant positive diagonal kinetic class, equality of mixed potential derivatives requires a=lambda b-prime. Integrating u supplies U and proves sufficiency for the displayed conservative force core; Rayleigh damping remains dissipation. The clamped data cannot certify moving-coordinate inertia, global stability or absence of additional velocity/non-diagonal/feedback terms. In the nonzero-anchor regime the normalized shape integral and E0*kappa<0 for J>0 are equivalent to positive lambda, including zeros of A without division by a. Fully decoupled or constant-b cases lack this anchor and are outside the identifiable inverse. Common positive force gain cancels shape ratios and preserves the sign, but unknown sign or setting-dependent gains do not.

Equation (14) is the triangle bound with nonnegative segment integrals. If its integrals were interpreted with the oriented x→y convention of (12), it fails for reversed pairs: choose y<x, epsilon_B=epsilon_kappa=0, epsilon_A>0 and nonzero khat; the written RHS would be negative. The mathematical result is correct using absolute orientation (or restricting the bound to x<=y). This is a notational domain ambiguity, not a defect in the reciprocal theorem. Independent reversed-pair controls use the nonnegative segment interpretation. No statistical confidence or calibration uncertainty is inferred.

## Independent computation and reproduction

check.py uses elementary homogeneous solution bases rather than the author's augmented matrix-exponential baseline implementation, and separately integrates piecewise hidden ODEs. It covers arbitrary preparations in three damping regimes, exact finite pulse response, a nonpolynomial reciprocal shape with a zero of a, reversed coordinate pairs and ratio-error corners. Thirty-one assertions passed. The full author JSON reproduced exactly: 25 passing controls, zero failures, including version metadata. No failure or timeout occurred. Both executions used explicit 120-second subprocess bounds; actual commands, timings and return codes are in check_receipt.json and reproduction_receipt.json, with stdout/stderr preserved. All source hashes were confirmed unchanged.

No network, git, PR, audit or author-source operations were performed. The cited external papers, current-main search and primitive registry provenance were not independently reverified; they are non-load-bearing contextual claims here. Exact equations supply the mathematical premises, not framework derivation. Physical action, source/time/coordinate registration, common channel, fidelity, continuum coverage and stability remain unresolved conditions as stated.
