# Finite standalone resonant launch: distinct analytical check

Disposition: SUPPORT for the actual finite standalone source, whole-horizon finite/infinite comparison and complete normalized output on the stated window. No required correction found. The fixed-diagonal cut, centered Taylor bound, distance/log prescription, target fit, counts and channel consequences are supported. No router or record theorem is implied.

## Exact evidence and exposure

Read the complete new `common_product_resonant_finite_launch/PROPOSAL.md` and verified SHA256 `41878812eb8afeb214cb9deb8b0da976fcf200542dd7675237fe14efd360e880`. Paths below are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

Reused the complete immediately preceding launch-window read and its completed review, refreshing both identities:

- `common_product_resonant_launch_window/PROPOSAL.md`: `c5acbc2c71cf352563e196bfb24225590f2f02718a86d39cc611461fadff5e5a`.
- `common_product_resonant_launch_window_check/REVIEW.md`: `539037ccb03cd5c2641774f890362cc07b911cd8fcea6d41ee945a51bf7aa649`.

The finite source's pending launch-review wording is historical: review539037 now supports the complete standalone infinite launch, not this new finite cut by itself. The full recently read geometric source `be2ab9da4b62ca7f595c17fea5ec6e62849cdada2c34416154996ad15180538e` and distinct review `cfd880ac1dcd866fe47fd51c7b8f29764270fc028e67e540c1cb1a6b1f86dfed` retain their free-profile scope. The standalone physical block/measure source `fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4` and survival source `306174fb0a884c62d5c6de401492a742a3d8a55670ef273f9d376258e531c002`, with own survival review `de9dbd20bf873f194d969ec6570e77224a2dfb192ba3ac4035b0933fc3d610bd`, are reused at the exact scopes and complete reads recorded in review539037. No broad ancestry re-audit is claimed.

ROOT suggested the centered-series route, fixed-diagonal cut and distance scale. The author wrote the exposed component chain; I checked the preceding complete launch and earlier scalar components. This is source-exposed same-model selective analytical verification, not blind replication or retained audit. Applicable previously read reviewer/workflow instructions are reused. Only this report was written; no source/W/Git/checkpoint/axiom/editable-prompt/model change, scientific executable, delegation or publication occurred.

## 1. Positive finite device and exact comparison operator

The combined source block is positive term by term for 0<gamma<j. In its one-head basis (s,0) it is [[2j,-gamma],[-gamma,j]], while its double-occupation value is 3j. Its one-head largest eigenvalue is (3j+sqrt(j^2+4gamma^2))/2<3j, so its full norm is exactly 3j. The first uniform bond adds j to site0; the far cap adds j to siteM. Therefore every one-head diagonal of the complete finite device is exactly 2j, including both ends. All blocks annihilate global vacuum and conserve head number.

The exterior restriction also has endpoint diagonal 2j. Consequently the difference between cut and infinite one-head operators is exactly the off-diagonal pair j(|M><M+1|+|M+1><M|). It has norm j, and there is no diagonal defect or extra common phase. The finite summand is reducing, so its evolution from the seed is precisely the physical finite evolution embedded with zero exterior coordinates.

The cap is load-bearing: an uncompensated Laplacian cut would not give this operator identity. The source uses the compensated cut throughout.

## 2. Centered norm, graph distance and full boundary estimate

K=H_infinity-2jI is the self-adjoint weighted adjacency on the half-line, with edge magnitudes gamma,j,j,... . Absolute row sums are gamma at s, gamma+j at 0 and at most 2j elsewhere. The symmetric Schur bound therefore gives ||K||<=2j on the complete one-head space. The infinite many-head sum is not used or claimed bounded.

The shortest path from s to M has M+1 edges. Hence P_far K^p|s>=0 for p<d=M+1, including every coordinate n>=M, not just one endpoint. Factoring out exp(-i2jt) and bounding the norm-convergent remainder of exp(-itK) gives R_d(2jt). The common diagonal contributes no spurious propagation scale.

V acts only on M and M+1, so its norm on the evolving seed is exactly j sqrt(|psi_M|^2+|psi_(M+1)|^2). Both coordinates lie in P_far, proving the stated bound without an omitted second endpoint or a lead-length factor. Ordered Duhamel uses the actual cut propagator on the left, whose norm is one. Thus the full embedded-vector difference is <=j integral_0^t R_d(2js)ds<=jT R_d(2jT). This pays both the missing exterior field and changes inside the finite chain, and does not assume exact finite-speed agreement.

## 3. Factorial tail and logarithmic allowance

For integer d>=1, (d+l)!>=d!l! yields R_d(x)<=e^x x^d/d!. The elementary factorial lower bound d!>=(d/e)^d then gives (6). If d>=8e jT, x=2jT<=d/(4e), so

    e^x(ex/d)^d <= exp[d/(4e)]4^-d <= exp(-d),

because log4-1/(4e)>1. These estimates are valid also at x=0, with the zero tail handled directly.

The ceiling in (8) guarantees d>=2, d>=8e jT and d>=log(8jT/epsilon). Therefore M>=1 and jT exp(-d)<=epsilon/8. A negative logarithm at small positive T is harmless: the same exponential inequality still follows from d>=that logarithm. This proves the whole closed horizon bound, including t=0, with no selected-time or light-cone assumption. The stated general O(1+jT+log_+(jT/epsilon)) count follows from the ceiling/max formula.

## 4. Target fit, phase and complete output

The adopted launch-window family has u0>1, T=2u0/j and rho<1/2. Its emitter-plus-two-lead-term comparison already pays the incoming field and band-edge remainder and has complete error <epsilon/4 uniformly on [u0/j,2u0/j]. That established component result is applied to the same infinite launcher, not to a different graph or supplied wavepacket.

For the chosen finite distance, M=d-1>=8e jT-1. Since jT=2u0>2, this is strictly greater than 2jT+1/2. Also m(t)=floor(2jt+1/2)<=2jT+1/2. Thus the entire geometric target support 0,...,m(t) fits in 0,...,M throughout the window. It is exactly the prior normalized target, with no new truncation or renormalization loss.

The finite target's squared norm is rho^2 sum_(n=0)^m a^(2(m-n))/(1-a^(2(m+1)))=1. Its denominator is positive. The phase exp(-i2jt)exp(im pi/2), source factor i and power (-ia)^(m-n) are unchanged, including the specified rounding convention. Comparator jumps are pointwise comparison choices, not switched dynamics. A separately supplied scalar c adds exp(-ict) on the target.

Triangle inequality combines the finite comparison <=epsilon/8 with the infinite complete error <epsilon/4, giving <3epsilon/8. Since the target lies entirely in the source-empty support 0,...,m(t), projection onto its complement gives failure probability <9epsilon^2/64. The actual evolved vector has norm one by finite unitarity; it is not projected or normalized to obtain either conclusion.

## 5. Coherence, channels and hardware bookkeeping

For two identical finite copies, the unused copy is exactly vacuum of energy zero. A single head in either copy therefore sees the same complex target and evolution; there is no extra common-diagonal phase from the empty copy. Orthogonal path sectors give the single-source operator bound unchanged for arbitrary coherent logical inputs and passive references. The actual and target maps are isometries, so the unhalved complete-channel/diamond distance is <3epsilon/4. Both emitters and every head site remain in the declared output. This is logical identity transport, not a controlled gate or record operation.

One device has M+2 head qubits and M+2 listed blocks: one B, M bonds and one cap. Full-support incident sums are 3j at s, 5j at 0, 4j at strict interior sites and 3j at M. For M=1, 0 and M are distinct and the same endpoint loads hold. Thus j<=Lambda/5 satisfies the cap. Two copies double qubits and block counts without changing any incident sum. Passive program/reference factors are supplied, not silently counted as newly realized apparatus.

## 6. Costs and limits

On this family jT=2(64/epsilon)^3[log(32/epsilon)]^(3/2). The distance term 8e jT gives a matching lower bound, while the logarithmic term and ceiling are asymptotically smaller. Thus the proposed device size and T orders follow with both upper and lower bounds for this chosen sufficient prescription. They are not lower bounds on all source constructions. With j=Lambda/5 the time has the stated Lambda^-1 factor; gamma remains an exactly supplied coefficient, not a tolerance claim.

The new Taylor/Duhamel cut estimate controls the actual source trajectory from time zero and is independent of geometric propagation. The geometric component is used only to identify the complete target on the finite window. A cutoff target with infinite spatial support would need a further finite-tail estimate, as the source explicitly says. Finite recurrences beyond T, routers, record flags, thermal preparation, native coefficients, readout/capture/reset, old literal processor transfer and permanent halt remain outside this result. The supported extension is precisely a finite standalone emitter-to-lead interface with all physical outputs retained.
