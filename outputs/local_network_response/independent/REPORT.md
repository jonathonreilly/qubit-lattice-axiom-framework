# Focused final-source check

Disposition: PASS within the explicitly conditional finite-network mathematical scope. No consequential mathematical or code-source mismatch found. This is independent source checking, not an audit verdict, empirical validation, current-main preservation certification, or the combined landing gate.

## Exact reviewed source

Complete note and both Python files were read, including all proof, scope, provenance and executable statements. They were frozen before reproduction:

| Path | SHA256 |
|---|---|
| docs/LOCAL_NETWORK_INTERVENTION_RESPONSE_NOTE_2026-10-16.md | 405eb15fba1d42d8f24f39500ba14375dda3d926b3f0c50919b84c1e954c4699 |
| scripts/local_network_response_math.py | 7a5199d3f7db9a5b9ded229d2529aa7f748b97f93a161636734c7b484b65f8e1 |
| scripts/local_network_response.py | d2fae47522371b3770d7d451ce3945fffa1405be819dfbc23f4dca28880c856b |
| logs/runner-cache/local_network_response.txt | c57a8ba721f420dce66ea542ba88c7592eb8f10d6386ded38dbee21a646767ce |
| outputs/local_network_response/mutation_controls_v1.json | dde68d187f70d8889d2e9b3c1a062ce53d33b12bffd70654c7fc28977b4dd905 |

Read also all 13 mutation failure tracebacks, original primary execution receipt, canonical execution receipt and prose status. Evidence hashes are in evidence_hashes.json. The v1 mutation manifest binds the prior note b5deed646136478a7f6411f3d760fc7f179043afe869e89e5f8e6c95107a0be9 but exactly the final two code hashes. Its 13 intended failures were verified against their actual tracebacks. They establish mutation sensitivity of the unchanged code, not final-note binding. Fresh canonical cache and this independent reproduction bind the final note. This provenance distinction was reported to the author; no source amendment was needed. Any later mutation rerun is outside this frozen report unless separately checked.

## Independent mathematics and scope

The preceding independent block09/10 derivations were reused and checked against the complete final argument. The decisive reasoning is restated here so this report does not rely on a prior PASS label.

Solving x''+Cx=-bq by variation of constants gives x=x_h minus the sine convolution. Substitution in q''+aq+b^Tx=f therefore puts the memory convolution on the left with a minus sign and the homogeneous hidden force on the right with a minus sign. The zero-data Laplace Schur complement has the same sign. Positive C and a>b^TC^-1b give positive full K; nonzero hidden initial data cannot be silently dropped. The note keeps these conditions explicit.

An orthogonal change O fixing observed e0 leaves e0^T(z²I+K)^-1e0 invariant. For the displayed rotation K'=[[4,-3/5,-4/5],[-3/5,33/5,-1/5],[-4/5,-1/5,22/5]]. Its negative off-diagonal entries and positive row sums give positive pair springs and grounding; K has positive leading minors 4,19,110. This supplies two declared nodal networks, not a unique inverse reconstruction or an identification of microscopic coordinates.

Multiplying the rank-one inverse formula by A+theta ww^T proves Delta=theta H/(1+theta J). Both inverses must exist. Symmetry uses ordinary transpose even at complex frequency; distinct source and readout do not yield positivity of H. Eliminating H,J gives the displayed polynomial for three settings. Clearing denominators retains blind/zero/repeated-setting cases but gives no identifying power there. The condition is necessary, not sufficient for rank one. For certified complex errors, expand each Delta_i Delta_j-d_i d_j; the three triangle-inequality terms are eps_i|d_j|+eps_j|d_i|+eps_i eps_j. Arbitrary common-baseline correlation is allowed. Calibration errors in theta or changes to b,c,K,w are not covered.

For collocated unit e, w^T(z²I+K)^-1e first has coefficient (-1)^d mu_d z^(-2d-2). Squaring yields theta mu_d² z^(-4d-4); the rank-one denominator starts at one. The convergent impulse series therefore first differs at t^(4d+3), coefficient theta mu_d²/(4d+3)!. Cayley-Hamilton extends vanishing first n moments to all moments; the Krylov subspace then never sees ww^T. Zero theta, zero direction and inaccessible directions give identical responses rather than a finite nonzero leading order.

At graph distance r, the first power entry is a sum of length-r shortest-path products. Strictly positive springs make their signs uniformly (-1)^r, so they cannot cancel. For an edge with unequal endpoint distances the nearer endpoint determines d; equal endpoint distances can cancel. Bipartite neighbors have opposite parity distances and hence differ by one. Connected accessibility is required; disconnected components remain invisible. With unit e each remaining coefficient is bounded by 2M^k. Starting k=2d+2 and bounding (4d+5+2r)! from below by (4d+5)!(2r)! gives exactly the stated all-real-time cosh remainder. This requires finite positive M, fixed finite d, and both stable positive matrices as stated; the Python floating helper is not an arbitrary-magnitude interval-arithmetic certificate.

For the same labeled w=(0,1,-1), mu1 is -1 versus 1/5 for K and K', producing the factor 25. Rotating w as well removes this distinction. Thus the intervention is calibrated extra information. Analytic small-time tails do not give a hard causal cone, and finite impulse displacement is not automatically a physical detector record.

All physical bridges remain supplied/open: quadratic action, unit kinetic normalization, nodal coordinates, preparation, source/readout, rank-one intervention and error certificates. The source neither derives these from current axioms nor infers observations from synthetic agreement. Established Schur/rank-one/Taylor mathematics is not promoted as novel physical law.

## Independent execution

check.py directly expands matrix powers rather than deriving expected coefficients from the helper under test. It checks d=0,1,2; negative stable, positive and zero interventions; complex noncollocated responses; repeated and zero settings; zero direction; t=0 and negative-time remainder symmetry; and factor25. It then runs the final runner with bytecode writes disabled and a 120-second subprocess timeout. The outer independent computation also has a 120-second timeout.

Result: 64 independent assertions passed, including exact equality of the reproduced JSON payload with the fresh canonical cache; the final runner reports 14 passing, zero failing controls. See check.py, independent_results.json, check_execution.json, execution.json, and preserved stdout/stderr. All computations finished successfully; no independent failure or timeout occurred. The 13 deliberate author mutation failures are separate evidence, not failures of the unmodified source. No canonical file was edited, and no external source or new physics route was used.

This check covers the named note, its full helper dependency and runner, their internal interactions, and the enumerated evidence. Cross-unit landing validation, repository-wide claim disposition, changed-head validation, audit application and empirical realization remain outside this assignment.
