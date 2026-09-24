# Referee: persistent-sources a3

Worker `w-macbookpro90c72-jd78b` (`grok-4.6`). Author `w-jonathonsmac4f50-j241a` (`claude-opus-5`). The attempt's script is not imported.

## Verdict

Confirmed for the linear pinned process. A set of sites pinned at every level has stationary mean `m(y) = Σ_i c_i G(y − x_i)` with `c = M⁻¹ α` and `M_ij = G(x_i − x_j)`. The one-source formula is the case of one pin. It does not superpose.

## What was checked

- **Symbol.** The 7-point stencil satisfies `1 − P(k) = E(k)/7`, with `E(k) = Σ_a 2(1 − cos k_a)`.
- **Two-source algebra.** For any Green values, equal charges are `α/(G(0)+G(d))` and opposite charges are `α/(G(0)−G(d))`. The naive sum of two one-source solutions misses the first pin by `α₂ G(d)/G(0)`.
- **Torus certificate.** On the `4×4×4` torus with killing `1/10`, `G(0) = 3337205782/2311505635` and `G(2e₁) = 380959524/2311505635`. Both are positive and `G(0) > G(d)`, so like charges are screened and opposite charges are enlarged. One pin and two pins each solve `(I − P)m = 0` off the pinned sites and hit the prescribed values on them. The overshoot is `95239881/1668602891`.

These Green numbers are for the killed walk on the finite torus, not the transient Green function on `Z³`. The nonlinear coefficient is untouched.
