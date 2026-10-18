# Independent real-axis arm-contrast limit check

Read `/private/tmp/neutral_realaxis_proof.md`. The repaired regular term and the full-minus-arm-deleted limit are algebraically consistent. This is a theorem for the explicitly specified leading NN coefficient model, conditional on the stated uniform Weyl/turning-point estimates, not the phase of the corrected native model.

## Source normalization and Schur reduction

The exact physical expression has a prefactor 2lambda^2 multiplying b^T h_s b. With b approaching -(1,2)/2, twice this bilinear product becomes u^T h_s u for u=(1,2)/sqrt(2). Thus no factor two is missing in

(G_C-G_C^0)/lambda^2 -> u^T(h_s-h)u.

For fixed positive beta, the local slow Green matrix is bounded in the chosen window, even though the full resolvent norm can grow as lambda^-2. Therefore lambda M=o(1), M=V^T R V, suffices to replace (I-lambda h_s M)^-1 by I in this local expression. The fast direct term 2lambda Rdd cancels exactly in this particular comparison because both models retain the identical fast block. This cancellation is not a claim that the physical baseline is smooth.

## Slow-arm regular part

The specified slow arm has hopping -1 and potential f(n+2), n>=1. Its lowest Dirichlet energy is -2+alpha1 f^(2/3)+2f+O(f^(4/3)), and its endpoint residue is f+O(f^(4/3)). At

e=-2+alpha1 f^(2/3)+f(2+Re a)+lambda^2(x+i beta),
f=lambda^2/8,

the pole part tends 1/y, y=Re a+8(x+i beta). The regular endpoint part tends -1. Keeping both gives g_s=-1+1/y+o(1). The O(f^(4/3)) energy correction divided by f tends zero, so using this approximate center is sufficient for the asserted limit. Fixed beta>0 keeps y uniformly away from zero for real x in compact intervals.

The endpoint regular term -1 is essential: replacing g_s by just its pole part changes both the constant background and the dressed pole location. The repaired formula includes it correctly.

## Exact scalar simplification

Write sigma=h_AA(-2), L=u^T h(-2) A, and a=sigma/(1+sigma). Then

u^T(h_s-h)u=L^2 g_s/(1-sigma g_s).

Substitution of g_s=-1+1/y gives the exact rational identity

g_s/(1-sigma g_s)=-1/(1+sigma)+[1/(1+sigma)^2]/(y-a).

Since y-a=8[x+i(beta-Im a/8)], the limiting contrast is

B+R/[x+i(beta-Im a/8)],
B=-L^2/(1+sigma),
R=L^2/[8(1+sigma)^2].

The factor 1/8 is correct. B and R are complex bilinear expressions, not positive weights. Continuity of the regular punctured-host boundary value justifies replacing h(e) by h(-2) in the local limit. The outgoing/retarded host value must be approached from the upper half-plane here.

For real x the broadened contrast is -Im of this quantity divided by pi. At x=0, the pole term contributes Re R/[pi(beta-Im a/8)], so a negative Re R indeed corresponds to a depletion. The additional constant contributes -Im B/pi; it must also be retained when discussing the actual full contrast. Neither the contrast nor its pole part is individually a positive probability.

## Fast NN phase checks

Given the stated interior Bessel asymptotic g_f=-tan(theta)/2+o(1), the coupled-host limit gives Rdd=-1/(4g_f)+o(1)=-(i/2)(1+q)/(1-q)+o(1), q=exp(2i theta). With Im z=beta lambda^3 and f_fast=lambda^3/16, Im theta tends 8pi beta; hence |q| tends exp(-16pi beta). The resulting full leading spectral baseline is lambda Re[(1+q)/(1-q)]/pi, a positive Poisson kernel. The derivative of the interior phase gives a physical energy period asymptotic to 2lambda f_fast=lambda^4/8. These factors and signs are correct. This check does not replace a uniform complex-order Debye error proof, which remains the analytical input for the stated Bessel limit.

Uniformity requires beta fixed and positive, or bounded in a compact positive interval. No beta->0 bound follows. The NN phase is especially sensitive to omitted fast coefficients and cannot be relabeled a native phase prediction. The contrast result exploits exact counterfactual cancellation of that shared baseline; it is not an experimentally established subtraction scheme.

Conclusion: no further missing normalization or regular term was found after restoring B. The exact coefficient-model limit remains separate from numerical corrected-fast diagnostics, omitted source terms, and any complete microscopic real-axis spectral claim.
