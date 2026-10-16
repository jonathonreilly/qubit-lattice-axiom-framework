# Independent preparation-bridge check, preserved v1

The displayed moving/tangent equations, exact quadratic dependence, moment construction and deterministic error bounds are correct within their supplied class. One measurement-premise clarification is needed: the fitted prefix endpoint must transfer to the drive without a hidden kick or impulsive coordinate transition. V1 says common prescribed history and no externally forced hidden channel, but does not explicitly specify its clamp-to-drive regularity/continuity. Root separately raised this same point; I recommended x at least C2 during the drive, x(0)=x0, xdot(0)=0 continuous from the clamp, and no hidden state kick between prefix and drive. The equations need no correction.

## Source binding

- PREPARATION_BRIDGE_v1.md: `c7039b5a4b1335e39f679b4f33f22c576d68b93fe76906f5bdae539359d23d4e`
- PREPARATION_BRIDGE_PLAN_v1.json: `9d9e84115a74243a08f3c4ce41f71858b457037553cd8f30b6d00e3049c6201f`
- check_preparation_bridge_v1.py: `e874f3d7f8822bd7817754502d5187dc7ed2c2ae31f3945208ecc5ee62b4fd7e`
- PREPARATION_BRIDGE_CONTROLS_v1.json: `7d27d26071e40460990731a869d99615a3a887ce9799054f74963c89692241c9`

The complete note and plan were read, then derivation_before_code.md saved before reading the complete runner. Published controls were read in full. Final v1 hashes remain unchanged. check.py passed127 independent checks. The author run passed133 controls and complete parsed JSON matched the frozen output exactly. Every computation used bytecode-disabled Python with a120-second subprocess bound; execution_receipts.json preserves commands, elapsed times and return codes. Full stdout/stderr remain present. No computational failure occurred.

## Independent evidence

The independent model differs from the author model and uses a prescribed t²exp(-t) coordinate history. I propagated the affine reference state and its2x2 transition matrix together, separately integrated arbitrary preparations, and compared their entire trajectories. Prefix fundamental coefficients were fitted with a complex exponential basis instead of the author's real cosine/sine representation. Measured-prefix moment weights recovered finite-drive rest-start force and predicted new preparations. A complex-step Jacobian of the full moving field independently propagated the nonstationary tangent; centered direct simulations agreed, while the nonrest tangent differed from rest. Different preparation ensembles on the two drive signs exhibited second-order centered convergence. Lower-rank feasible designs, fixed-radius dual obstruction and100 correlated feature/readout error cases also passed.

Direct variation confirms the k' xdot² hidden term and cancellation of k' xdot wdot in the visible equation. All tau',tau'',gamma',nu',k' tangent terms and their signs agree. For fixed x(t), the hidden system is affine linear, and force after hidden acceleration elimination is quadratic in state; therefore its dependence on arbitrary initial deviation is exactly quadratic, not a perturbation approximation. The unknown nonzero n maps c to measured f by an invertible real homogeneous map, so the prefix origin identifies rest only if that coordinate survives the transition. The determinant of the c-to-position/velocity map is nonzero for omega>0.

Moment feasibility is precisely e0 in col(Q). It is sufficient and necessary for all quadratic output functions, not necessarily every individual restricted force observable. Six full-rank samples are sufficient; three amplitudes on a line can work. Nonnegative normalized weights away from0 cannot cancel the nonnegative second radial moment. A fixed nonzero radius fails even with signed weights. Signed synthesis is a linear combination of observations, not a physical negative-weight preparation.

## Explicit transition counterexample

transition_counterexample.py gives exact rational evidence. Prefix a samples1,2,3 admit weights3,-3,1. At a point of a valid quadratic class, force may be R=z+z² with z=2a. A common unobserved position kick0.3 between prefix and drive gives R=(2a+0.3)+(2a+0.3)². It remains quadratic and passes arbitrary reserved-preparation interpolation, but weighted force is39/100 instead of the unkicked rest value0. Thus quadratic closure alone cannot certify transition continuity. This is a measurement-boundary issue, not a counterexample once no-kick smooth transition is explicit.

## Scope and error assessment

The feature Frobenius bounds and Neumann/resolvent weight bound are valid under A*eta<1; the force bound permits correlated errors. Known-pole prefix coefficient errors follow from the pseudoinverse norm; a singular or poorly conditioned fit cannot certify its own missing pole/model errors. Taylor's centered-response bound requires a uniform third derivative certificate and common starting clamp, and force errors amplify as1/|epsilon|. Arbitrary input-history mismatch is not removed.

The frozen plan's model, preparation lists, drives, tolerances and negative control correspond to the actual runner. Synthesis uses extracted prefix coordinates and force records, not hidden-state values or n; hidden parameters/reference are generator-side verification. Six-point fitting always interpolates six outputs and is not a class test. Additional preparations reject the constructed moving cubic output. Reserved drives/preparations are synthetic checks; no empirical observation or temporal provenance audit was performed. Prior art is background, not an imported proof. Physical class, input reproducibility, calibrated force/pole/phase/time, model stability and continuous preparation transfer remain premises. No novelty, physical reset, formal audit or publication claim follows.
