# Distinct check: nominal cubic derivative cancellation

Verdict: conditional support; no necessary correction found. The selected exact finite-band derivative ceiling 3.00002 r² is valid, and its substitution into the ordered D3 bounds preserves their full-input scope. No complete performance conclusion is supplied.

The complete reviewed target is `three_site_cubic_derivative_cancellation/PROPOSAL.md`, SHA-256 `d57ca3702567780319131cdcadd824588364b93d77575e26b56e00565fd292ac`. The immediately preceding complete D3 source/check and exact nominal source polynomial are reused at their unchanged verified identities below.

## Physical Weyl and exact cancellation

Write sigma=sqrt(1-delta²/(4j²)). Direct differentiation of the physical upper-lip Weyl function gives

    m'=1/(2j²)+i delta/(4j³ sigma),
    |m'|=1/(2j² sigma).

The selected physical band has |delta|/(2j)<=sin h, h<=4e-6, so sigma>=cos h and this is strictly below .501/j². The conjugate lower lip has the same modulus.

Also m+i/j=delta/(2j²)+i(1-sigma)/j. Since 1-sigma=delta²/[4j²(1+sigma)], its triangle bound is at most |delta|/(2j²)+delta²/(4j³). For nonzero delta, division by |delta|/j² gives at most .5+|delta|/(4j)<=.500002<.501. At delta=0 the discrepancy is exactly zero; the source correctly handles this case without claiming a false strict zero inequality.

Expanding the cubic decomposition gives

    (delta+i lambda)^3-3jlambda P2(m+i/j)
      =delta³-3lambda² delta-3jlambda P2 m,

because the imaginary terms 3i lambda delta²-i lambda³ cancel i3lambda P2 exactly. This equals the physical q0. Differentiating the equality, not a modulus envelope, yields the displayed q0' formula. Its leading term has modulus 3|delta+i lambda|²=3r²; it is not bounded by separately adding its real and imaginary components.

The remainder is bounded by

    3jlambda[1.002 delta²/j²+.501|P2|/j²]
       <=4.509(lambda/j)r².

Thus |q0'|<=[3+4.509eta]r². On lambda<=1e-8 and j>.0027, 4.509eta<.0000167<.00002, proving the requested strict 3.00002 ceiling. This includes delta=0, preserves the physical load derivative, and does not replace the finite-band determinant by a Markov cubic.

## Propagation through the full ordered derivative

The selected reference inverse derivative becomes A/(s²r⁴), A=3.00002. It still dominates the separate complementary bound 4000 across the original narrow window. The selected derivative of P2/q0 is bounded by (2/s+A/s²)/r². The complementary derivative ceiling 200 is retained independently; it is not reduced by claiming the selected cancellation on closed channels.

The exact ordered identities from the checked D3 source remain

    Q^-1=N U0,
    Kload'=kappa²[T0'(G-G0)+T0(G-G0)'],
    (Q^-1 V_seed)'=N U0' V_seed+N Kload' N U0 V_seed.

Only U0' and the selected part of T0' change. Therefore replacing 6.01 by A and A_s by 2/s+A/s² in equations (9),(11)–(14) is legitimate. The first term in the integrated bound becomes n A pi/(2s²); the coefficient of the T0' integrals changes to the new A_s. All 400a lambda², 400b lambda³ and Z_g terms remain unchanged. These observations reconstruct the displayed tightened formula, rather than assuming a global factor-of-two improvement to the actual D3.

The sharper nominal Neumann criterion Theta, the actual discrepancy derivative Z_g, n² factor, fixed prepared input and full complementary inverse are unchanged. The separate complementary D3_C allowance uses the smaller A_s but still retains U0'C<4000 and T0'C<200. It is not added to the full bound a second time. The per-window/lip supremum conventions and later Stone multiplicities remain distinct.

## Scope and exposure

This improvement is for nominal ratios, zero residual detunings and Delta=0 on the original physical band. The same selected cancellation has not been proved for common offsets or perturbed sources. Actual Q does not commute with D, and the lower ordered Q is not assumed to be the upper adjoint. The claim improves a majorant for an integrated prepared inverse derivative; it does not prove a full L' bound, temporal output, receiver size or complete-state certificate. Endpoints, both windows/lips, spatial synthesis and actual outside mass remain separate obligations.

Root authored the new calculation. I checked the prior D3 source and have shared nominal inverse and attachment/reference ancestry; I also authored the background-IBP candidate referenced as motivation. Those exposures do not independently validate this cancellation. Here I reconstructed the Weyl modulus, exact polynomial identity, derivative slack and all changed substitutions directly. The prior D3 check is reused evidence, not a new independent check of its unchanged physical premises.

Only this review was written. No scientific computation, numerical integration, sweep, dynamics, solver, Git/publication/checkpoint action, prompt/model modification or delegation occurred. Deterministic source identities were verified. No retained-status determination is made.

## Exact unchanged premises

- `three_site_prepared_inverse_derivative/PROPOSAL.md`: `25052bad1d500f52d4e4f4d3913f0bf8a0a57d69801688b7109a549ac3756d84`.
- `three_site_prepared_inverse_derivative_check/REVIEW.md`: `3a76d76895c01dcbd7cf7e5b566f7146ae683ddc4568352df06c19224e59aa1c`.
- `three_site_loaded_inverse/PROPOSAL.md`: `7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672`.
