# B8 independent check: confirmed with corrections

Provenance: a fresh-context agent of the same model family, not an independent reviewer. It used new simulation code (`independent_check.py`, PASS=10 FAIL=0, 400 tori of size 24³, ferro rule). Saved by the supervisor from the hand-back.

**Disclosure.** A first test, that n·Var stops growing, failed for the random-permutation sequence. That is the expected finite-size growth toward χ. Before the final run it was replaced by the exact variance identity.

## Verdicts

- **Lemma 0: confirmed.** Own Γ from exact self-avoiding-walk counts gives χ ≤ 4027.7; with the runner's extension, 4068.7. Minor: the ball term needs d(S, S+z) ≥ 3; below that only p(1−p) applies.
- **Theorem A: confirmed.** Almost-sure convergence between squares is deterministic: |F_n − F_{k²}| ≤ 2(2k+1)/k². Monte Carlo: n·Var ≤ χ̂ = 1.69. The separated sequence gives 0.148–0.164 against p(1−p) = 0.139.
- **Theorem B: confirmed.** k₁₄ = 30913 is correct. Nit: exact c₁₃ already gives m = 13.
- **Theorem C: confirmed with corrections.**
  - The combined constant is 6, not 3.
  - m and k_m must use |S ∪ S_c| and diam(S ∪ S_c).
  - m must satisfy δ_m ≤ qε/16.
  - Any fixed q > 0 is enough; the constants scale as q⁻².
- **§4 limits: confirmed with a correction.** Own-mark rules need U₀ independent of T₀ (the race satisfies this; Definition 1 allows dependence). Monte Carlo: Record context 0.5115, formation-time context 0.8004.
- **Reading of the 09-02 obligation: confirmed with corrections.** The §0 headline overstates.
  - 09-02 premise 7 concerns repeated trials of one conditional experiment.
  - B8 gives spatial site-sampling within one realisation. Its limits equal the one-use weight only for order-blind positive rules.
  - Recommended wording: a partial and conditional discharge. The 09-02 dependency row stays "supplied".
