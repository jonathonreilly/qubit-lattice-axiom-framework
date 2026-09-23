# Source-bound comparison of the rotor-clock tail extension

No required mathematical correction or consequential code/prose mismatch was found in the authorized packet. Its exact second-moment identity, the single-circulation tail coefficient, the continuous-density qualification, and the exceptional parameter a=eta-4 delta=0 agree with the frozen independent reconstruction. This is a bounded scientific comparison, not a formal audit or publication decision.

The PRE report and all its evidence remain unchanged. The independent full Laplace law, complete positive-moment criterion, finite-variance density example, and coherent cancellation example are additional results in that PRE. They are not claims to attribute retroactively to the author note.

## Identities and read coverage

The independent PRE is `0aac7b39eefeacd4464660b824af56638ed05f30865abcc2cd16024a756bbb2c`; its report is `72124a5757a5de2185f4139528d77a37dd0f59248b70c6c0e9b57e7380cccd21`. All five source and thirteen artifact bindings authenticate.

The authorized author seal is `0ffc4d68970054377f6b80c4b5cc0ec593d38380944d8e5d202a6aa0090648c7`. Its two source and six artifact bindings authenticate. The principal source identities are:

- `ROTOR_CLOCK_LONG_TIME_TAIL_AND_MOMENTS.md`: `8043a10bb42ac45cc207d06ed53a23a9a500c376acdc0f13ee3b5b8ab4ddceea`.
- `tail_moment_check.py`: `73c886d0272361700397a74cfd5a30bd09f31fc3538fff5f9da20e5e0db82309`.
- `TAIL_AND_MOMENT_RESULTS.json`: `4b1ee316e90f4b74ab7df55edb367d9144da3e730ff61d95a62ed8a875583ac0`.
- `CHECK_RUN_RECEIPT.json`: `bc32951badbc9c28f36a1f7e6b5a13eac1bea25dcbda1dc87ccbca6ab06a38e6`.

The entire author argument, runner, result JSON, receipt, and streams were inspected. The successful stdout equals the result JSON byte-for-byte, and stderr is empty. The receipt records source hash, start time, elapsed time, and exit code; it is not a complete invocation/environment record. Authentication of that receipt is not claimed as independently observing or replaying the author's execution.

The author explicitly credits the previously sealed independent exact block law as its starting dependency. The new author formulas were frozen before the new tail reconstruction was requested; that dependency boundary is consistent with the supplied packet. Only this authorized packet was opened. No other author folder, finite-spin material, campaign plan/checkpoint/registry, Git, publication, or audit action was accessed or performed.

## Moment identity and hypotheses

For nonzero omega, both eigenvalues of K_omega=[[-2 kappa,i omega],[i omega,0]] have strictly negative real parts. The mean and second-moment matrices therefore exist as convergent finite-dimensional integrals. Differentiating exp(tK*)exp(tK), then integrating by parts, gives K*X+XK=-I and K*Y+YK=-2X, with Y=2 integral t exp(tK*)exp(tK)dt. The author's signs and factors are correct.

As a separate post-source check, `comparison_check.py` solves the two linear systems for unknown Hermitian matrices. Both complete matrices equal the author's expressions, not merely their 11 entries. In particular

    Y11=1/(2 kappa²)+1/(2 omega²).

At omega=0 the full mean matrix does not exist because of the opposite dark coordinate, while the actual initial lossy coordinate has second moment 1/(8 kappa²). The author makes precisely this distinction. It does not assert a uniform-in-frequency matrix bound.

The flat first-output weight contributes 1/(16 kappa²); the other weights and identity

    s_+^-2+s_-^-2=1/[2 sin²(alpha/2)]

give the exact physical expression

    E[T²]=5/(16 kappa²)+(1/(16a²))
            integral g(theta) sum_j b_j(theta)csc²(alpha_j/2) dtheta/(2pi).

This agrees with independent PRE Eq. (12). Tonelli applies to the original nonnegative survival integrals and permits the value infinity. The exceptional points themselves have zero weight for a normalizable field, but their neighborhoods cause the divergence. For g=1 there is a positive singular contribution for both instruments, so the infinite second moment and variance follow without fitting a numerical tail. The mean remains finite by the previously established first-moment identity.

The author does not generalize this divergence to every normalizable density. That qualification matters: the independent PRE gives explicit finite-variance countercontrols. They limit broader interpretations, but do not refute any assertion in this packet. The author also states a=0 separately, with Exp(4 kappa) survival, rather than applying its nonzero-a formula there.

## Tail constant and the limits involved

The squared slow-mode amplitude is correctly suppressed by omega²/(4 kappa²), while its decay exponent is omega²/kappa+O(omega^4). The small singular frequency near theta_e is |a|(sqrt(2)/3)|theta-theta_e|+O(|theta-theta_e|³). Combining these with the first-output factor 1/4, measure dtheta/(2pi), and integral of y² exp(-y²) yields

    C_g=3 sum_(theta_e) g(theta_e)b_e
                                  /[64 |a| sqrt(2pi kappa)].

This is exactly the independently obtained coefficient. For g=1, the four b_e sum to 2/3 for either instrument, yielding C_1=1/[32 |a| sqrt(2pi kappa)].

The asymptotic argument is sufficient under the stated continuous angular-density hypothesis on the circle. On small fixed neighborhoods, the scaled slow term has a Gaussian integrable bound; the exponentially decaying remainder has an integral bounded by a polynomial in t times an exponential, which vanishes. Away from those neighborhoods the positive-frequency compact family has a uniform exponential bound, with the critical-damping polynomial factor harmless. This supplies the needed domination rather than assuming a uniform nonzero angular gap.

The author requires the displayed sum to be positive for a nonzero leading t^-3/2 term, and expressly declines to infer that tail if it vanishes. It also declines a general tail assertion for merely L1 densities without examining their exceptional-angle behavior. These are the right boundaries. The independent PRE's more detailed vanishing-density and coherent-instrument power laws are separately derived extensions.

The author correctly distinguishes its tail from the fixed-time fast limit. Uniform absolute convergence of survivals does not justify integrating tS(t) to obtain a second moment. Here every finite nonzero a has an infinite second moment for g=1, while the limiting exponential mixture has 5/(16 kappa²). Nor does a fixed laboratory-time microscopic approximation control a subsequent t->infinity limit. No finite-spin or microscopic long-time theorem is asserted in this packet.

## Independent comparison controls and numerical coverage

No author function or model builder was imported or executed. The new comparison script reuses only the already sealed independent scalar function definitions, and it solves the Lyapunov equations afresh. All 36 saved two-state rows were checked against independent formulas and direct matrix exponentials; the largest difference between corresponding saved and independent fields is 2.23e-16. The author's reported matrix-versus-formula maximum, 1.16e-15 after rounding, is accurate.

For a distinct check of every saved tail quadrature, I derived an exact one-dimensional frequency reduction for the three tested densities g=1+sigma cos(theta), sigma=0,+1,-1. Resolved formation has the same folded integral as the uniform input. For coherent formation, four theta-translates give the weight 1+(sigma/2)cos(alpha). Consequently its survival is

    (1/2)e^(-4 kappa t)
       +(1/pi) integral_0^(pi/2) [1+(sigma/2)cos(4v)]
                                  f_(2sqrt(2)|a|sin(v))(t)dv.

This post-source comparison identity follows by averaging the four cosine phases; it was not copied from the author's six-branch angle quadrature. The predicted tail coefficients are respectively C_1, 3C_1/2, and C_1/2 for the coherent cases, and C_1 for the resolved cases. Recomputing all 24 saved scaled tails at a=4.2, kappa=.9 agrees within 2.72e-16. The saved relative errors at t=100000 range from 1.02e-5 to 1.13e-5, consistent with the prose. Quadrature error estimates remain numerical diagnostics, not certified asymptotic bounds.

The five angular-excision values agree with the independently derived exact singular contribution 3/[4 pi a² tan(2r)] and its limiting r-times coefficient 3/(8 pi a²). The largest numerical discrepancy in the saved integral is approximately 2.22e-13. These values corroborate the analytic divergence; the proof does not depend on a cutoff experiment.

`COMPARISON_RESULTS.json` records every compared field, exact identities, sources, and limits. Its stdout is identical to the result file; `comparison_run_RECEIPT.json` records the actual new command and zero exit code, with empty stderr. No new failed attempt occurred. The PRE is preserved byte-for-byte, and `FINAL_SEAL.json` binds the old reconstruction and the new comparison separately.

The bounded disposition is confirmation of the author packet within its stated supplied-rotor scope. No source repair is requested. The additional independent Laplace and general-moment results remain in their own frozen PRE, with their own hypotheses and attribution.
