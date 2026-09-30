# Contract: rare-hole global source tilt

Status: candidate analytic route; not independently checked, not formal review.

The target is the ACTUAL supplied finite-spin microscopic dynamics from bare Omega, with both original instruments treated separately. On an even cubic torus let n=|A|, W=count of A holes, Kd=W+NB. For fixed theta, delta, kappa>0 seek constants independent of spin and volume such that, for sufficiently small epsilon,

    Tr[W exp(theta Kd) rho_micro(t)]
      <= C_theta epsilon^2 (n+n^2 t) exp[C_theta n(t+epsilon^2)].

Increasing the polynomial in n is permissible only if explicitly derived. A successful theorem must retain an epsilon^2 prefactor. It is not a local-cluster bound: the exponential volume factor is retained.

Concrete consumer: bound epsilon^-2-weighted instantaneous/integrated bounded fast currents in high GLOBAL count sectors on a common short physical interval. Do not infer local occupied-island UI inside a much larger volume, microscopic electric moments, or full M4. No modified dilution ensemble or observed internal projection is introduced.

Allowed premises: actual main30a compensated spin law and bare product preparation; the checked finite-depth normal form, two-corrector defect proof, positive GLOBAL count theorem and local gate inequality; exact occupation/charge/Gauss identities. The newly checked local/multiple-hole response bounds motivate the source problem but are not assumptions in this proof. No rotor-generator extension is asserted. The joint epsilon^2 S(S+1)=delta/K may be imposed after uniformity is proved.

Candidate family A: conjugate the positive state by the global count weight; remove the nonconservative generator's off-grade potential by finite-depth LOCAL invertible congruences; preserve complete positivity, allow trace growth, and adapt the defect correction with its explicit volume price. Endpoint costs must be proved for bare preparation and physical W, not guessed from a global near-identity norm.

Alternative B: exact cascade harmonic/Poisson lift for finite global excitation, preserving mark strings. This may construct a signed corrector but has no automatic local thermodynamic extension. Alternative C: direct local count tilt/instantaneous G absorption, already refuted by the actual seven-B dark-to-dark witness; it will not be reused. Alternative D: Hölder between mean holes and unweighted global moments loses the epsilon^2 power and cannot meet this target.

Prior art: GLOBAL_MOMENT proves exp(C n(t+epsilon^2)) without a hole factor; its APPROACH_REGISTRY explicitly leaves the tilted W moment open. INITIAL_CLUSTER_SEED proves the conditional rare-hole cluster tail at t=0 only; LOCAL_TILT refutes instantaneous bare-loss domination. Open PR9399 at5bec44a concerns effective thermodynamic dynamics, excluding microscopic elimination. PR9400 atb0d159b is a fixed finite-ring numerical curvature proposal. Their actual sources/sections were read in preceding continuous work; refreshed heads and main are unchanged.

Proof obligations: exact congruence transformation formula and homological signs; local interaction-norm uniformity and no volume-dependent homological inverse; grade/number/Gauss preservation; CP with an explicit Hermitian potential; bounded positive trace growth; two-corrector drift including nonlocal products of potential and W; local preparation/physical conversion; exact restrictions of the source-tail/current consequence.

Controls initially <=30 CPU seconds/150 MB, BLAS1, no dense lattice enumeration. Analytic uniformity will not be inferred from samples. Check original campaign deadline and STOP before scripts. Writes only this directory; no old report edits, commit, PR, audit, registry or remote mutation. Root focused independent check required before downstream reuse.
