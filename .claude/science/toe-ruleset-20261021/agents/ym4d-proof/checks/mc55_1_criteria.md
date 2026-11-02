# mc55_1 — criteria (written 2026-10-29T06:05:18Z, before any mc55 script exists)

Purpose: check the exponent bookkeeping of MINCB55 Proposition DENS (b): the per-cube bound of the critical-chain densities is
k-uniform iff the transport weight sigma > 0. Exact rational arithmetic (fractions.Fraction), plain python, no floats in verdicts.

Objects (d = 4): for L in {3, 5}, sigma in {1, 1/2} (so L^(-2 sigma m) is rational), m = k-1-i:
- soft-term level sum A_k(sigma, L) := sum_{m=0}^{k-1} 4 * L^(4m) * L^(-2(2+sigma)m)   [count 4L^(4m) times squared residual factor]
- closed bound B(sigma, L) := 4 / (1 - L^(-2 sigma))
- level-0 count identity: 6 * L^(4k) * (L^(-2k))^2

Gates (all must hold for PASS):
- G1: for each (L, sigma) and every k = 1..200: A_k <= B exactly, and A_k is strictly increasing in k.
- G2: for each (L, sigma) and m = 0..60: L^(4m) * L^(-2(2+sigma)m) == L^(-2 sigma m) exactly (the d = 4 cancellation).
- G4: for each L and k = 1..60: 6 * L^(4k) * (L^(-2k))^2 == 6 exactly.
Designed controls (each must FAIL its boundedness gate, otherwise the check is declared NON-DISCRIMINATING and the verdict is FAIL):
- C1: sigma = 0, L = 3: the gate "A_k <= 400 for all k <= 200" must FAIL (A_k = 4k).
- C2: mutant count exponent d = 5 with sigma = 1/2, L = 3 (terms 4 L^(5m) L^(-5m)): the gate "A_k <= B(1/2, 3)" for all k <= 200
  must FAIL.
Verdict: PASS iff G1, G2, G4 hold and both C1 and C2 FAIL. Anything else: FAIL (reported as such).
Scope (stated in advance): this checks arithmetic of the level sums only; it does not check BFT-1's inputs, the term counts as
geometric facts, or NA-alg (b).
