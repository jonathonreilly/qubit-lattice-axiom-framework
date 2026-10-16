# Independent derivation before reading author code/output

Frozen identities are in frozen_sources.json. Only source prose has been read so far.

For each h,j and visited bit, the missing current bit is fair conditional on all allowed processing randomness. Summing the indicator Z=X xor Y over that bit gives exactly 1/2. Integrating over history/route proves exact equality and additive response cancellation. This needs joint freshness conditional on H,J (and all latent variables governing response), not just separate pairwise independence.

Let W_t be the win and F_{t-1} include all preceding settings, outputs and device state. Then E[W_t|F_{t-1}]=1/2. Conditional mgf <=exp(s^2/8) for W_t-1/2 yields exp(-snd+ns^2/8); optimizing s=4d yields exp(-2nd^2), for fixed n and d>=0. No optional stopping assertion follows.

TV controls expectations of [0,1] functions by epsilon when the same response kernel is applied under both laws. All hidden response variables and exception eligibility must be included or conditioned consistently. A lambda mixture bound 1/2+lambda/2 requires freshness within the nonexception component, e.g. exceptions selected from prior information independently of fresh bits. Merely bounding the unconditional mass of arbitrary exceptional current-setting events is insufficient: select exceptions exactly where X xor Y=1, output zero on other events and XOR on exceptions. With lambda=1/2 this wins 1 rather than the claimed 3/4 while unconditional settings are fully fresh. Exception eligibility itself may carry current information. State this condition explicitly or use the weaker coupling bound 1/2+lambda+epsilon where appropriate.

Fixed-block cache: an error at event t requires all t routes identical (probability 2*2^-t) and the other initial cache wrong (1/2), giving 2^-t. Sum t=1..B gives (1-2^-B), so mean win is 1-(1-2^-B)/B. Fresh settings give 1/2 immediately from missing-bit fairness.

Stationary flip process: current visited cache is exact, so the parity score is the sign correlation of the unvisited bit with its last visit. Balanced independent route ages have P(K=k)=2^-k. Hence score rho/(2-rho) and win 1/(2-rho). For route-0 probability q, on a current route-0 event the missing route-1 age law is (1-q)q^(k-1); conversely q(1-q)^(k-1). Weighting gives q(1-q)rho[1/(1-q*rho)+1/(1-(1-q)*rho)]. Requires iid routes independent of input evolution, stationary ages, 0<q<1; rho in [-1,1]. At nu=1 the cache is poor but a predictor can exploit alternation. These are performance formulas, not optimality bounds.

Two current signals allow a local future XOR and win 1. This does not derive single-particle energy or continuous interference, and the source explicitly acknowledges that limitation. Append-only memory is an abstract computational embedding, not an established covariant lattice realization.
