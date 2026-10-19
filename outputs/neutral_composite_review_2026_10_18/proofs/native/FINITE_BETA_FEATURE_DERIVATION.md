# Fixed-temperature large features: controlling the change of metric

Root derivation, independently checked. The physical hypotheses remain the supplied compass Hamiltonian and a high-temperature Gibbs state. This result does not derive the preparation or identify temperature with a cosmological field.

## Current follows from the same bonds

For E_f=sum_x f_x e_x, let p be a site, a<b two axes, s,t=±1, c the remaining axis, and epsilon_abc the Levi-Civita sign. Direct commutation gives

D E_f = −K² sum_(p,a<b,s,t) epsilon_abc [f_(p+t e_b)−f_(p+s e_a)] sigma_(p+s e_a)^a sigma_p^c sigma_(p+t e_b)^b.

Indeed E_f weights each bond(i,j) by(f_i+f_j)/2. Combining the two orderings of a pair of touching bonds leaves the difference of these weights; the shared endpoint cancels. Parallel-axis bonds commute. This proves the displayed identity. Compact-support integer profiles independently exercise the exact Pauli identity in energy_current_identity.py. No current or interaction coefficient is fitted.

## Mathematical high-temperature input

[Kliesch et al., Locality of temperature](https://arxiv.org/pdf/1309.0816v3), Theorem 3 (clustering) and Theorem 4 (locality), bound generalized Gibbs covariances and finite-buffer errors uniformly in volume. Ordinary covariance is included at the parameter endpoints. For interaction norm J and animal-growth bound alpha, their window is |beta|<log[(1+sqrt(1+4/alpha))/2]/(2J). We use this mathematical result, not a physical state-selection rule.

For this bond graph J=|K|. Each bond touches at most ten other bonds. A rooted connected set of m bonds admits a deterministic spanning-tree depth-first walk of length2(m−1) in that adjacency graph. The walk identifies the visited set, and there are at most10^(2m−2) such walks. Thus alpha=100 is a safe, deliberately loose bound. K=0 is excluded from this scale formula and is trivially static.

The theorem implies summable connected correlations for the finite set of local current types above. Its decay factor b=alpha exp(2|beta|J)[exp(2|beta|J)−1] is O(|beta|) near zero. We need no numerical claim that the entire clustering window has a chosen susceptibility lower bound.

## Residual in the thermal metric

Center operators by their thermal means and write ||A||_beta²=<A†A>_beta. Let J_(p,a,b,s,t) be the unit-norm three-spin Pauli word in the current. Time reversal sets its mean to zero. Exponential clustering supplies the finite Schur constant

M_beta = sup_i sum_j |<J_i J_j>_beta|.

Applying the Schur bound to the exact current sum gives

||D E_f||_beta² <= K⁴ M_beta sum_(p,a<b,s,t) |f_(p+t e_b)−f_(p+s e_a)|².

For the widthR Gaussian the last sum divided by sum_x f_x² is12/R²+O(R^−4). The energy covariance is absolutely summable; its Fourier transform S_e(q,beta) is continuous and nonnegative. At beta0, S_e(0,0)=3K². Local finite-buffer continuity and a uniform summable tail imply continuity of S_e(0,beta), so it remains positive on some smaller open interval around zero.

For a broad Gaussian, convolution and dominated convergence yield

Var_beta(E_f)/sum_x f_x² → S_e(0,beta).

This is a low-momentum packet statement, not a lower bound for every envelope. The checkerboard source e_(pi,pi,pi) is identically zero. Combining the estimates proves, at each fixed beta in the smaller interval,

limsup_(R→infinity) R² ||D E_f||_beta² / Var_beta(E_f)
 <= 12K⁴ M_beta / S_e(0,beta) < infinity.

Stationarity makes the thermal operator dynamics unitary, so the same exact time-change inequality as in the tracial calculation holds for centered E_f. Thus broad slow features are not an artifact of using beta=0. No diffusion constant, wave speed or particle pole has been presumed.

## Uniform composite overlap

Apply the same covariance summability to C_f=sum_x f_x C_x. For fixed beta the largeR normalized overlap tends to

S_Ce(0,beta)/sqrt[S_C(0,beta) S_e(0,beta)].

Continuity alone is insufficient to assign its beta derivative. To obtain the leading coefficients uniformly in volume, truncate covariance sums beyond a fixed sufficiently large support distance. The bound b^distance and the polynomial growth of distance shells make the tail O(beta^m), for any prescribed finite m after choosing a sufficiently distant fixed cutoff. For the finitely many remaining pairs, a fixed wider buffer gives a local-state error O(beta^(m+1)) by the locality estimate. Finite-box Taylor coefficients therefore determine the thermodynamic coefficients through the required order. The bond-reflection symmetry makes the mixed susceptibility odd and both diagonal susceptibilities even in beta.

The already enumerated local traces give

S_Ce(0,beta)=−6beta K²+O(beta³),
S_e(0,beta)=3K²+O(beta²),
S_C(0,beta)=3+O(beta²).

Hence the limiting normalized overlap is −2beta |K|+O(beta³), and its square is4beta²K²+O(beta⁴). The projection coefficient in energy units is S_Ce/S_e=−2beta+O(beta³). These are distinct normalizations. For sufficiently small fixed nonzero beta the overlap is nonzero while the energy-feature residual tends to zero as R grows.

This establishes a shared slow component under stated thermal premises. It does not identify the whole composite with that component, retire the temperature/history input, produce an autonomous relativistic scalar, or derive a universal matter coupling. In particular the small-inverse-temperature interval is existential beyond the explicit clustering threshold; no numerical safe interval for all the strengthened conclusions is claimed.

## Static high-temperature covariance bound

The same high-temperature theorem bounds the imaginary-time covariance uniformly in its parameter. The isothermal response to a weak local source −f e_0 is

chi_static(x)=beta integral_0^1 cov_tau(C_x,e_0) d tau.

It therefore decays exponentially in separation in the phase used above. Its Fourier transform is bounded and analytic near real q=0 under these premises. Equivalently, the quadratic cross term in equilibrium free energy for two distant weak local probes is exponentially bounded. This package retains that covariance bound without promoting the separate static-mediator exclusion theorem.

The negative static-response identification theorem is explicitly deferred. Its complete argument and phase restrictions remain recoverable in the original source; no five-family negative packet has been established. The present claim is the stated conditional covariance estimate and constructive broad-energy feature.