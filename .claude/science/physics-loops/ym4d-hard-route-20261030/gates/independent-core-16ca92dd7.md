lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-01T03:49Z

# Gate: independent-core, first outside read of the independent attempt

**Provenance.** Model anthropic/claude-opus-5-5, effort high, worker mac-mini-worker, pinned at commit 16ca92dd7 of branch claude/ym4d-hard-route. Fresh session with no memory of the derivation. Same model as the attempt, so this is not independent in model and it is not an audit. Verdicts steer research and grant no status.

**Firewall.** Side: independent. Read only `GOAL.md`, `FINISH.md`, `parts/hard-core--independent.md`, its four library files, and upper-chain statements. Not read: the mapped file, any other file in `library/`, gates on the mapped attempt, the Sussman-Alpoge repository, the charters, or `checks/` of the attempt.

**Status: in progress.** Sections are appended as they finish. Numerics: memory free was 44 percent at start, below the 50 percent floor, so no numeric job has been started.

## Interim notes (reading in queue order; superseded by the verdict table when that appears)

- Read by hand with no break so far: Lemma 4.5k Steps 0 to 3; Lemma 4.5h (Caccioppoli, Gehring, exponents); library Lemma 8; Lemma 4.5j; (EI) arithmetic; Theorem 4.2; Theorem 5.5 Steps 1 to 5.
- Under test: complex W in the analytic sector, where the Gaussian of xi_eff has a complex centre s(W, xi'), and the constant c' of (TAIL) against "C absolute" in Lemma 4.7c.

## Registered criteria, written before any run (`checks/gate_ic/toy_tail_centre.py`)

A toy, on a one-dimensional chain with a strictly local H_1 = -Delta + m^2 + u(W), P a Chebyshev polynomial of degree D in H_1 approximating H_1^{-1/2}, Z an interval. It tests linear algebra used by two arguments of the attempt. It cannot test the attempt's actual chart, and it establishes no bound.

- TAIL. Compute d xi_c / d u_j at fixed b_Z, for xi = P_Z^+ b, with P_Z^+ the right inverse on Z. **PASS-TAIL-LOCAL** if it vanishes (below 1e-13) for all j at distance above 5 D from c. **FAIL-TAIL-LOCAL** if some such j has it above 1e-13, which means the coordinate xi_c read at fixed (v, xi^perp) depends on far W.
- CENTRE. With u = i alpha on all sites and xi' a spike of height q, s := P^+ G xi'. **PASS-CENTRE-SMALL** if |Im s| / (alpha q) falls below 1e-3 as the size of the spike or of alpha varies, so that |Im s| <= c holds for all q <= p_4 uniformly in p. **FAIL-CENTRE-SMALL** if |Im s| / (alpha q) stays at a positive constant, independent of q and alpha, to within a factor 2.
- CONTOUR. For one variable, h analytic, s = i y: I := int_{-p}^{p} rho(x - s) h(x) dx. **PASS-CONTOUR** if |I| <= 1.05 and the shifted-contour bound (main term plus side walls) holds at y up to p / 3, while the modulus bound exp(y^2 / 2) exceeds it by at least 1e3 at the largest y. **FAIL-CONTOUR** otherwise.

No numeric job has run yet at the time of writing this section.
