# Upper-chain item 10: registered checks

Source: 0cad38f3644a6749b0e4a5782335744bc1f45732. Author check,
openai/gpt-6-astra/max macbook-codex; no independent review or audit.

These criteria are written before executing `check_history.py`.

1. **Killed-kernel expansion.** On a three-step, two-state reverse Markov
   chain with nontrivial kernels, signed sources and signed transport
   coefficients, check the pointwise positive history expansion by exact
   rational arithmetic. Check its domination of the generated observable.
   Check Jensen for every individual history term at q = 2 and q = 4,
   with both possible singleton top events and the full top event. Any
   failed equality/inequality is a failure of this implementation or formula.
   This checks a finite example, not the general proof or a Wilson kernel.
2. **Copied bounded seed.** With a Bernoulli bit copied through three
   levels, seed B (bounded by 1), zero sources, zero reference state and
   transport coefficient 16, compute the exact fourth moments. The ratio
   of consecutive fourth moments must be 16^4, disproving a factor-1/4
   homogeneous moment contraction even for a generated bounded seed.
   This is not a counterexample when an adequate explicit source/history
   error is included. No unspecified “tiny” term is tested.
3. **Radius admissibility.** Set x_(K-d) = x_K (5/4)^d, x_K = 1000,
   lambda_(K-d) = 100 + d/100. Evaluate at d = 0 and d = 1000, using logs
   to avoid enormous arrays. At d = 1000, 2 log(x) > lambda/5 proves
   x^2 > exp(lambda/5) >= M, making the capped A event certain even at
   a regular field. At d = 0 the ordering is reversed. The analytic
   argument, not these two samples, establishes the parameter obstruction.
   The examples test the stated FLOW inequalities, not an actual coupling
   trajectory of either hard-core construction.

Execution: preflight, confirm successful numeric-lock acquire, BLAS thread
counts 1, `nice`, address-space limit 2 GiB and a self-check of peak RSS.
Use exact rational arithmetic except for the two logarithmic diagnostics.
Keep stdout, preflight and lock receipts here. Release the lock afterwards.
