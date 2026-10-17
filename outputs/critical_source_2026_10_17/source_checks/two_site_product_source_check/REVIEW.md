# Distinct analytical check: two-site product source

## Verdict and scope

Conditional support, no necessary correction, for the complete `two_site_product_source/PROPOSAL.md`, SHA256 `8892741e6a14bca4565aef77d5913a3afca43a850c202c43dc2afb8ed3d9e303`.

The exact halfline product-seed density, absence of hidden spectral mass, finite-band comparison including the weighted second-site amplitude, cubic actual spectral-tail ceiling, both-source-site escape bounds and finite-cut index are valid on 0<lambda/j<=1/8 with kappa^2/j=2lambda. The squared-Lorentzian return is a controlled reference, not the exact lattice return. No interacting-processor, outgoing W, receiver or whole-apparatus theorem follows.

I read and hash-verified the full source and reconstructed its Jacobi and Fourier calculations directly. Root's proposed critical relation and the task's intended test were exposed. I authored or checked several narrower emitter/reference and capture components in this campaign, but did not author this two-site source. This is a distinct calculation check with shared research context, not blind discovery or a novelty review. The cited paper's identity, historical priority and finite-channel results were not independently reviewed here and are not premises of the displayed halfline proof. No paper fidelity or optimized coefficient is needed for this verdict.

## Positive realization and exact halfline spectrum

For eta=lambda/j<=1/8, kappa/j=sqrt(2eta)<=1/2. Each listed occupation coefficient is therefore nonnegative. At sites 0,1,2 the incident exchange diagonals plus those occupations give respectively 2j, 2j and 2j; subsequent sites have two ordinary j bonds. The exchange block is positive on the full pair space, including its doubly occupied state. The carrier remains exp(-i2jt), and no vacuum shift is introduced. The exact coupling relation is a supplied correlation premise; no tolerance statement is proved.

Eliminating the uniform tail gives the displayed 2x2 source inverse, with positive lambda in z-h and R10=-lambda/D. On the physical upper lip, kappa^2 m_j=eta delta-i2lambda s. Expansion of the squared determinant gives

    |D_+|^2=[(1-eta)^2-eta^2]delta^4
              +[-2(1-eta)+4]lambda^2 delta^2+lambda^4,

which is exactly the polynomial in (3). Taking the imaginary part of the numerator divided by D cancels its delta^2 term, leaving -2lambda^3 s/|D|^2. Stone's sign therefore gives the positive density (4).

For x>=2j, m_j(x) is positive and at most 1/j. The lower bound x(x-2lambda)-lambda^2 increases on that range and is positive at 2j. Oddness of the physical exterior branch makes D even there. Both exterior half-lines and both thresholds are consequently pole-free. In the band, Im D can vanish only at delta=0, where D=-lambda^2, apart from the regular thresholds. The explicit algebraic resolvent is locally regular across each interior segment on its chosen lip. This excludes singular measure there; analytic exterior continuation excludes exterior support, and finite threshold values exclude atoms at the two remaining endpoints. Its 1/z asymptotic fixes total mass one. No singular mass is left unaccounted for.

All hoppings are strictly nonzero, so the endpoint seed is cyclic by the tridiagonal recurrence. Thus the measure does not conceal a decoupled bound subspace. From |1>=-h|0>/lambda, the complete two-site spectral matrix is exactly (5). In particular its cross measure is signed and its second moment is lambda^2. Both are necessary for the escape calculation.

## Reference density and both comparison errors

Replacing the surface selfenergy by -i2lambda gives the rational reference with denominator (z+i lambda)^2. Its positive normalized boundary density is the displayed squared Lorentzian. Differentiating the standard Cauchy Fourier integral in lambda gives A0,M=(1+lambda|t|)exp(-lambda|t|). The cross amplitude is -(i/lambda)A0,M', so for t>=0 it equals +i lambda t exp(-lambda t), with the correct positive small-time derivative from the negative hopping. Neither formula was substituted for the actual finite-band evolution without an error term.

The polynomial comparison D2-P=2eta delta^2(lambda^2-delta^2) implies both D2>=(1-2eta)P and |D2-P|<=2eta P. Subtracting the densities on the physical band proves (8). The estimate 1-s<=delta^2/(4j^2) is valid through the thresholds. Integrating its correction uses the full reference second moment lambda^2, while the missing reference tails outside [-2j,2j] cost at most eta^3/(6pi). This reconstructs E0 exactly. At eta<=1/8 its relaxed ceiling 3eta has slack.

The second-site amplitude cannot use E0 alone. Multiplication by |delta|/lambda gives the first reference absolute moment 2/pi and a finite-band third-moment correction. Direct integration of delta^3/(delta^2+lambda^2)^2 gives the logarithm and endpoint terms displayed in section 4. The exact weighted exterior tail is 2eta^2/[pi(4+eta^2)]. Thus E1 in (10) is valid. The derivative of eta log(1+4/eta^2) is positive on this domain; its endpoint is below 6/8. Together with 1-2eta>=3/4 and pi>3, the supplied numerical relaxation proves E1<2eta. This explicitly controls the actual signed cross-measure Fourier transform, not only the seed return.

The uniform Fourier comparisons follow by integrating absolute errors on the entire real line, with the actual density set to zero outside the physical band. They do not claim a small relative density error at an edge.

## Actual cubic tail and two-site escape

Directly, rho0<=rhoM/(1-2eta) on the actual band. Integrating the delta^-4 upper envelope from Delta to infinity on both sides gives 4lambda^3/[3pi(1-2eta)Delta^3]. Because the actual seed measure has no missing singular part, this bounds its entire outside mass. Taking a square root and capping by one gives the stated omitted-state amplitude. The E0 comparison floor is correctly absent from this direct tail proof. At Delta=2j the actual tail is zero, while the nonzero ceiling remains conservative. The sufficient lambda/Delta condition is the correct rearrangement of the amplitude inequality.

The two coordinate errors have Euclidean norm at most sqrt(E0^2+E1^2). Adding them to the reference vector gives (12). The relaxed sqrt(13)eta follows from E0<3eta and E1<2eta. The sufficient time condition is also valid: sqrt(1+2x+2x^2)<=sqrt(2)(x+1)<4exp(x/2), and x>=2log(8/zeta) makes this reference contribution less than zeta/2. The comparison floor is a limitation of that estimate, not evidence of a nonzero late occupation.

The separate decay estimate removes that floor. The actual density is even, decreasing for positive delta and zero at the thresholds, with integrable derivative there. Its total variation is 2rho0(0)=4/(pi lambda), yielding the A0 bound by integration by parts. For f=-(delta/lambda)rho0, the same endpoint behavior holds and

    integral |f'| <=[1+integral |delta||rho0'|]/lambda=2/lambda.

The equality follows from monotonicity and integration by parts on each half-band. Therefore the actual A1 amplitude is bounded by 2/(lambda t), and the combined norm is at most sqrt(16/pi^2+4)/(lambda t)<2.4/(lambda t). Taking the minimum with one and the comparison bound is legitimate. This proves escape from both source sites at each fixed positive lambda, not delivery to a distant receiver.

## Finite compression and remaining physical obligations

There are M+2 retained sites 0,...,M+1 and M+1 bonds. The extra cap j n_(M+1) precisely replaces the diagonal contribution of the removed ordinary bond. When M=1 it shares site 2 with the occupation j-kappa, and their sum with the retained kappa bond still gives 2j. The four separately listed occupation blocks and fullspace positivity are correctly counted.

The centered infinite and finite hopping operators have norm at most 2j by their row sums. The first omitted site is M+2, at distance M+2 from seed 0. Their action powers therefore agree for fewer than M+2 applications; bounding the remaining exponential series twice gives 2F_(M+2)(2j|t|). This is a finite-horizon estimate. It does not imply all-time escape on a finite chain or suppress recurrence.

Tensoring a supplied invariant internal preparation range carries its own exact K evolution and passive references, but does not implement W. Replacing the uniform downstream halfline by an interacting processor changes the surface resolvent to an operator-valued object and reopens the full-input measure, waveform, phase, escape and finite-transfer work. The source correctly keeps those obligations separate and does not import old apparatus runtimes or paper fidelity.

## Verification limits

No mathematical repair is required at the stated isolated-source scope. This check used analytical reconstruction and deterministic hashing only. There was no scientific runner, numerical integration, dynamics, parameter sweep, external literature verification, delegation, model change, Git/canonical edit, publication, checkpoint or editable prompt change. Exact nominal couplings, initialization and the stipulated Hamiltonian remain supplied premises; this review does not confer retained or audit status.
