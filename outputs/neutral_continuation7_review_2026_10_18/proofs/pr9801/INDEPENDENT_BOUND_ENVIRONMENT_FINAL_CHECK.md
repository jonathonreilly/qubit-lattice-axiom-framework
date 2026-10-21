<!-- Original PR9801 source SHA256 31fa760a3eac9cd8d6cae7888bea8b7d5365e926913e2aeec45041a5e4c38bfc. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Final scoped check: bound mode and heavy environment

Reviewed the current native/BOUND_MODE_ENVIRONMENT_PROOF.md, public note, runner, three executed helpers, and the independent prepared-return and outgoing-flux checks. No repository files were edited and no formal audit was performed.

No blocking integration issue found. The actual matched prepared-return statement is a fixed-R, fixed-tau weak-coupling result. The static boundary-value problem and outgoing scattering are explicitly separate leading-coefficient problems with a held-fixed background. Neither proof nor public note multiplies them into a full native emission rate or relaxed charge.

## Prepared return

The vacuum correction has positive coefficient c=(gamma_L/Delta4)lambda^(L-4). Orthogonality gives the opposite flat component of the even pole, so the return amplitude involves r_e-r_0. This removes the spurious zero-time signal. With each shortest edge syndrome weighted 1/(sqrt(2)R), the edge sum is twice the single-defect trace difference. The fourth trace moment is -64, yielding the stated amplitude -(8sqrt(2)/3)(gamma_L/(Delta4 R))lambda^(L-4)tau^4 and squared coefficient 128/9.

The finite-rank perturbation has trace norm 8sqrt(2), and both signed hopping matrices have norm at most four. Telescoping their powers therefore gives the stated trace-difference bound n||V||_1 4^(n-1); bipartiteness removes odd moments. This controls the small-time remainder without a hidden transverse-volume factor.

The crucial microscopic-transfer refinement is present: background-preserving closed returns are constant on the flat orbit, so their generic O(lambda) correction must multiply the vacuum/pole admixture. Background-changing singleton terms start later. The proof does not use a generic O(lambda) preparation/evolution error to resolve an order-lambda^(L-4) signal. It expressly excludes bare preparation and an uncontrolled simultaneous tau(lambda) limit. Fixed-volume analytic control must be carried to the needed order, as stated.

## Environment calculations

The +2 off-diagonal defect bonds, outgoing equation (I+G_plus V)u=phi, positive imaginary Green term i/4, and six-site source normalization agree with the independent retarded check. The static and outgoing logarithmic limits differ by exactly two because g_R~log R/(2pi) whereas g_epsilon~log(1/epsilon)/(4pi). The reference to random-walk potential-kernel mathematics supplies normalization-aware analytic background, not physical parameters.

The quarter-turn argument removes a false free-wave selection rule; it does not itself show a finite threshold rate. This distinction is retained. The final text explicitly leaves recoil, energy transfer, other native vertices and the relaxed heavy-plus-neutral channel open.

## Reproduction

I executed all three helpers directly and repeated every assertion in the runner, without generating repository output files. All passed. Return trace differences at orders 4,6,8,10 were exactly -64,-1440,-26112,-439840. The R=128 static control had full-versus-Schur error 7.75e-15 and residual 1.29e-13. The last outgoing row, epsilon=1e-7, had relative error 1.176e-6 against the finite-g asymptotic expression, below the stated 2e-6 threshold.

Neither last numerical row is yet equal to its limiting scaled source: convergence is logarithmically slow. For example the outgoing scaled source was approximately -1.62174+0.27884i, while the limit is the real number -1.89276. The runner appropriately tests the finite-g expression, not a premature equality to the limit. The positive regulator is explicitly proportional to epsilon; these finite-regulator data corroborate, but do not prove, the analytic outgoing boundary limit.

The runner's replay consists of exact coefficient moments, finite sparse static controls and high-precision coefficient Green functions. It does not numerically simulate the full microscopic matched protocol or establish its analytic high-order cancellation independently. The current prose accurately distinguishes those roles.

The result remains conditional on the supplied slab Hamiltonian, matched dressed protocol and stated order of limits. It does not establish a universal matter coupling, cosmological scalar identification or measured emission observable.
