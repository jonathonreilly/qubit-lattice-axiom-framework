# B3 independent check: confirmed with corrections

Provenance: a fresh-context agent of the same model family, not an independent reviewer. Saved by the supervisor from the agent's hand-back; the harness blocked the agent's own write.

## Verdicts

- **Confirmed:** Lemma 1, Lemma 2 (stopping set), T1, Lemma 3 / T2, T2′, T3, C1 and C2 (mixing, no long-range order, entire structure factor, no pinch points).
- **Confirmed with corrections:** Prop 4 (scope), C3 (citation), C4 (attribution), and the claim that the repo's formation is an instance.

## Corrections

1. **Rate laws.** The 09-22 clock-and-rate note uses state-dependent rates (1+k, (1+k)², 1/(1+k)), restarted after each formation. These are not covered. Only the uniform-rate law and rules that merely read the clocks are in the class. Add the state-dependent rates and the 09-07 all-or-none eligibility variant to §7 as unproved.
2. **Prop 4.** The bound is (λ₊/λ₋)^n/(n+1)!, since the k = 0 factor is 1. Replace "deterministic bounded clock-rate fields" with "fixed, state-independent rate profiles".
3. **C3.** Cite Holroyd–Schramm–Wilson, Ann. Probab. 45 (2017), Thm 2(ii): every finitary-factor-of-iid proper 3-colouring of Z^d (d ≥ 2) has E[R²] = ∞. Replace the holes wording with "≤ 3 output symbols including holes".
4. **C4.** The critical-point finitary codings are due to van den Berg–Steif 1999, not Spinka 2020. Spinka 2020 covers spatial-mixing Markov random fields.
5. **T2′ proof.** "Centred" means shifted to the midrange (|f| ≤ osc f/2), not mean-centred.
6. **Lemma 1 credit.** Crediting it to Harris 1972 is loose.

## Re-derivations and simulation

- **Re-derivation of the repo definition.** Clocks are iid Exp(λ). The race reads only already-formed neighbours plus the start slice. "Ongoing support" is checked afterwards; it does not look ahead.
- **Pinch points.** Excluded, because Σ|Cov| e^{s|x|} < ∞ for every s makes the structure factor entire.
- **Independent simulation** (`independent_check.py`, 15/15 PASS). It implements the actual exponential race and an adversarial rule.
  - Lemma 1 on Z² (OEIS A001411): mean path counts match c_n/(n+1)!.
  - Locality and controls on a 16³ torus: resampling outside the determining set never changes the Record; perturbing inside does.
  - Covariance on a 24³ torus stays under the two-copy bound for d = 1–11.
  - Prop 4's path-ordering formula matches Monte Carlo.
