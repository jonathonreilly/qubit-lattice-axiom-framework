# Independent conditional-direction inference mathematics, v1

This is the final pre-author-source mathematical report. The complete proof below was frozen separately before control execution. No author derivation, implementation, result, protocol file, raw observations or network source was opened. The parent supplied the mathematical targets and optional extensions, so this is independent derivation from shared premises, not answer-blind work. Root remains the scientific author. This report supplies no formal audit verdict or empirical calibration result.

The carrier F pivot, exact cone distance and quantization-safe set are correct on their stated nondegenerate domains. The amplitude disk is also exact under the conditional angular law. Radial independence is unnecessary. In this nested decomposition the unquantized carrier and amplitude pivots are independent, giving exact product joint coverage; this does not imply carrier/color independence. The three material hazards are replacing the conditional angular law by covariance, selecting the reference from validation, and treating fitted residuals as an unconditional physical noise bound. The proof and explicit counterexamples below state the repairs.


This proof was written before opening any author derivation, implementation, result or new protocol file for this block. The parent supplied the target formulas and optional extension formulas; this is independent derivation from shared premises, not answer-blind work. No observations, external sources or author code are used. Root retains authorship. No formal audit verdict is supplied.

## 1. Precise probability model and degenerate cases

Condition on the training sigma-field T, including any supplied design/sample times, sample count and training-selected reference g(T). At the true candidate f, write y=c*u_f+epsilon, with u_f nonzero and ||u_f||²=N for the stated unit-modulus waveform. Treat f and c as fixed parameters, or condition on any additional parameter variables so that the angular hypothesis below actually holds. The essential assumption is

    epsilon=R*U,  0<R<infinity almost surely,
    law(U | T)=uniform probability on the unit sphere of C^N.

No moment of R is needed. Its conditional law may be arbitrary and can even depend on U: all pivots below are homogeneous of degree zero, so R cancels pointwise. Direction–radius independence is stronger than needed. Uniform direction conditional only on T suffices; uniform direction merely marginally does not suffice if T leaks directional information. Training-independent proper white complex Gaussian noise with a positive scalar variance is one sufficient special case. Properness and scalar covariance alone are not sufficient.

Let P_f be orthogonal projection onto span(u_f), P_S onto S=span(u_f,u_g), and A=P_S-P_f, B=I-P_S. These are mutually orthogonal projections with ranks r=p-1 and s=N-p, while P_f has rank one. In this two-template problem p is at most two. The nondegenerate carrier test has p=2, r=1 and N>=3, so s=N-2>0. Exact aliases/collinearity give p=1 and r=0: the F statistic is not defined and the carrier contrast carries no information. One may explicitly accept every candidate on this branch, giving conservative rather than exact nominal coverage. If s=0, the denominator residual is absent, and the proposed statistic and cone-distance formula cannot be used as stated. Near-collinearity is not exact rank loss but creates a numerical conditioning obligation.

Positive R and s>0 imply ||B epsilon||>0 almost surely under the angular law. If R can equal zero, 0/0 can have positive probability. Accepting the zero-error case gives conservative set coverage but not the stated exact F distribution. Deterministic zero-denominator or overflow handling in code is not supplied by the continuous-law argument.

## 2. Carrier F law, derived without a scale supplier

A normalized standard proper complex Gaussian vector is uniform on the complex unit sphere, because its density depends only on Euclidean radius and is invariant under every unitary transformation. Thus for calculating functions of U we may represent U=Z/||Z||, where the complex coordinates of Z are independent with density pi^-1 exp(-|z|²). Integration in polar coordinates gives |Z_j|²~Gamma(1,1), independently.

Choose a unitary basis adapted to P_f, A and B. Let C, X and Y denote the independent sums of squared Gaussian coordinates in these subspaces. Their laws are Gamma(1,1), Gamma(r,1) and Gamma(s,1). This representation is for direction; it does not assert that the actual error radius is Gaussian or independent. At the true f, A and B remove c*u_f. Therefore

    ||Ay||²/||By||² = X/Y,
    F_g(f)=(s/r)*||Ay||²/||By||² ~ F_(2r,2s),  r,s>0.

The factor two in both degrees of freedom comes from complex coordinates: 2X and 2Y are chi-squared variables with 2r and 2s degrees. This is a conditional law given T. A training-selected g is valid because the projections are then fixed. It does not justify choosing g from the same validation direction.

For alpha_g in (0,1), define h_g as the (1-alpha_g) F_(2r,2s) quantile and tau_g=sqrt((r/s)*h_g). The unquantized acceptance cone is

    K_f={y: ||A_f y|| <= tau_g ||B_f y||}.

At the true nondegenerate f it has conditional probability exactly 1-alpha_g. Inverting these pointwise tests gives a confidence set for the single true frequency. No union over all tested f is needed just to cover that one true f. This does not provide simultaneous error control for every reported false-candidate assertion or justify selecting a single fitted candidate and then treating it as known true.

## 3. Two concrete failures of weaker assumptions

Covariance-only failure: in an orthonormal basis (signal,A,B), choose with equal probability the magnitude triples (1,7/5,1/5) and (1,1/5,7/5). Independently multiply every coordinate by a uniform phase in {1,i,-1,-i}. The mean is zero, covariance is I, pseudo-covariance is zero and radius is always sqrt(3). Nevertheless, for r=s=1 the energy ratio is either 49 or 1/49, equally often. The nominal alpha=1/20 upper F_(2,2) critical value is 19. Actual rejection probability is 1/2. This is an exact proper white-covariance counterexample with no zero denominator.

Validation selection failure: take N=3 uniformly sampled times and the three orthogonal DFT tones. The true tone is the DC one. With spherical noise, the two residual Fourier energies X1,X2 have the independent exponential representation. If g is chosen from those two validation modes to maximize the projected energy, the tested ratio becomes max(X1,X2)/min(X1,X2), rather than one fixed ordered ratio. For alpha<=1/2 and critical h=(1-alpha)/alpha>=1, rejection has probability 2/(1+h)=2alpha, since the two tail events are disjoint. Thus Gaussian white noise itself does not rescue this selection shortcut. If the selected direction is put into T, the required conditional uniformity has become false.

## 4. Exact distance to the acceptance cone

Let A and B be orthogonal projections with AB=0 and rank(B)>0. Set a=||Az||, b=||Bz|| and tau>0. The remaining orthogonal component may be held fixed when minimizing distance. For any y, the reverse triangle inequality gives

    ||z-y||² >= (a-||Ay||)²+(b-||By||)².

For x=||Ay||, w=||By||, minimize this scalar expression over x,w>=0 with x<=tau*w. If a<=tau*b, z is already feasible. Otherwise the minimizer lies on the boundary x=tau*w, and

    w*=(tau*a+b)/(1+tau²),
    x*=tau*(tau*a+b)/(1+tau²),
    distance²=(a-tau*b)²/(1+tau²).

It is attained by preserving the directions of Az and Bz and using these new magnitudes. When b=0 and a>0, choose any unit direction in range(B), which is why nonzero B rank matters. When a=0 the point is already inside. This proves, including attainment for the closed set,

    dist(z,K)=(a-tau*b)_+/sqrt(1+tau²).

K need not be convex in the original vector space; the proof does not assume it is. If B=0 and a>0, the actual distance is a, not a/sqrt(1+tau²), so merely reusing the formula after a zero-rank residual is wrong. At tau=0 the separate limiting statement is dist(z,ker A)=a.

## 5. Quantization-safe frequency inversion

Suppose the recorded center z and unknown analog validation vector y obey ||z-y||<=q, q>=0, as a genuine pointwise bound in the same units and coordinates. No independence from the error is needed for this geometric inclusion. The exact union of the unquantized cone over that full closed ball is

    dist(z,K_f)<=q,
    ||A_f z||-tau_g ||B_f z|| <= q*sqrt(1+tau_g²).

Thus this accept set covers the true f with conditional probability at least 1-alpha_g. Coverage need not remain exact after quantization. Rejection is valid only when the entire admissible ball misses K_f. If actual quantizer cells are a subset of the ball, the ball version is conservative, not an iff characterization for those individual cells. Saturation, an unknown cell map or an invented q does not satisfy this premise.

The factor sqrt(1+tau²) is important. For tau=3/4, z has A component 5/4 and B component zero. The vector y with A component 9/20 and B component 3/5 is on the cone, and ||z-y||=1. Therefore q=1 must accept z. The shortcut a<=tau*b+q would reject it. It misses the error orientation that changes both orthogonal components. The triangle-inequality shortcut a<=tau*b+(1+tau)q is safe but looser.

If a proposed q-bound itself holds only with probability 1-delta, a generic lower coverage statement is 1-alpha_g-delta by a union bound. Multiplication by 1-delta requires additional independence. No physical or statistical q is obtained from the fitted residual.

## 6. Fixed-f complex amplitude disk

At a fixed true f define c_hat=u_f^*y/N and R_f=||(I-P_f)y||. Then

    N*|c_hat-c|²=||P_f epsilon||²,
    ((N-1)*N*|c_hat-c|²)/R_f² ~ F_(2,2(N-1)),  N>=2.

The same directional proof applies. For X~Gamma(1,1) and H~Gamma(N-1,1), the survival probability of X/H>kappa² is (1+kappa²)^(-(N-1)); this follows by conditioning on H and taking the Gamma Laplace integral. Therefore

    kappa²=alpha_c^(-1/(N-1))-1,
    D_f(y)={c: |c-c_hat| <= (kappa/sqrt(N))*R_f}

has exact conditional coverage 1-alpha_c. It is a frequentist confidence disk under the angular model, not a deterministic bound on physical error, a posterior credible set, or a scale estimate valid outside that model. Zero amplitude is allowed; physical phase is undefined there. N=1 supplies no residual pivot of this form. The amplitude convention depends on time origin and sampled-frequency alias convention.

For quantized z with the same deterministic q, apply the cone-distance theorem to z-c*u_f with A=P_f and B=I-P_f. This gives the exact ball-union disk

    |c-u_f^*z/N| <= [kappa*||(I-P_f)z|| + q*sqrt(1+kappa²)]/sqrt(N).

Its coverage is at least 1-alpha_c. Adding only q/sqrt(N) is not generally enough, because quantization can change the residual radius too. Again, a full ball enlargement need not be sharp for the actual rectangular quantizer cells.

## 7. Correct joint coverage, including a stronger exact fact

The carrier and amplitude pivots in this particular nested decomposition are independent conditional on T at the true f. To see this, use the Gamma representation C~Gamma(1), X~Gamma(r), Y~Gamma(s). The change of variables V=X/(X+Y), H=X+Y has factorized density Beta(r,s) times Gamma(r+s). C is independent of both. The carrier pivot depends only on V, while the amplitude pivot depends only on C/H. Hence the acceptance events are independent, regardless of the actual radial law.

For a region consisting of frequency-cone acceptance at level alpha_g and the fixed-f amplitude disk at alpha_c, unquantized joint coverage is exactly

    (1-alpha_g)*(1-alpha_c),

when r,s>0. Using alpha for both does not give 1-alpha joint coverage. Equal allocations alpha_g=alpha_c=1-sqrt(1-alpha) give exact total 1-alpha. More generally, choose allocations with that product at least the desired coverage. Bonferroni 1-alpha_g-alpha_c is always a valid weaker statement and remains useful when the projectors/tests no longer have this nested independence.

After replacing each component by its quantization-safe enlargement, the true-pair acceptance event contains the unquantized joint event, so joint coverage is at least the product. Quantized statistics need not themselves be independent. If g is exactly aliased to f and that branch accepts all frequencies, the carrier event has probability one and joint coverage is at least 1-alpha_c. No nominal amplitude disk at a data-selected wrong fitted frequency is certified by the fixed-true-f result. Joint inference must retain candidate pairs (f,c), not silently replace f by a selected estimate.

## 8. Optional direction diagnostic and deterministic covering extensions

These extensions were derived after the parent supplied their proposed formulas but before reading any author protocol, draft, code or observation.

For nominal uniform sample times, derotation D_f^* sends the true tone to a constant. A unitary DFT then puts its signal in DC. Split non-DC modes into L with 0<|frequency|<f_s/4 and H with |frequency|>=f_s/4. When both complex ranks l,h are positive, their normalized noise-energy ratio (h/l)*||P_L D_f^*y||²/||P_H D_f^*y||² has F_(2l,2h) law at the true f. Reversing numerator groups reverses the degrees and scaling. Small N can leave an empty group: for example N=3 or 4 has no low non-DC mode at these thresholds. The pivot is not generally independent of the carrier pivot, since those projectors need not align. A union bound over the actually declared direction tests is safe. It is not legitimate to invoke independent-test multiplication without proving it. The fixed-f amplitude pivot is independent of all functions of the residual subspace direction, but that fact does not make two arbitrary direction diagnostics independent of each other.

For the far-candidate bound, let q_f=u_f/sqrt(N), q_g=u_g/sqrt(N), k=|q_f^*q_g|, and R=|q_g^*z|/||z||, requiring ||z||>0. If k<1, choose a normalized v orthogonal to q_f so that q_g=(q_f^*q_g)q_f+sqrt(1-k²)*v. Then

    R*||z|| <= k*||z|| + sqrt(1-k²)*||A_f z||,

and hence ||A_f z|| >= (R-k)_+*||z||/sqrt(1-k²), which implies the parent's weaker bound without that denominator. Since ||B_f z||<=||z||, the condition

    R-k > tau_g + q*sqrt(1+tau_g²)/||z||

is sufficient for exclusion. It is deliberately conservative; it does not need a carrier-state estimate. At z=0 the normalized formula is undefined and the cone itself accepts. Exact k=1 is a rank-degenerate carrier branch and must be treated separately.

For nominal uniform spacing 1/f_s, let d be the circular aliased frequency separation in [0,f_s/2]. The exact overlap is |sin(pi*N*d/f_s)|/[N*sin(pi*d/f_s)] away from d=0, where its continuous limit is one. Thus for 0<D<=f_s/2 and d>=D,

    k <= min(1, 1/[N*sin(pi*D/f_s)]).

The denominator is monotone on this half-period and the numerator is at most one. D=0 is not an admissible division. Irregular physical sample times do not obey this Dirichlet formula merely because an FFT was used.

For fixed q and tau, the color score

    F(f)=||P_L D_f^*z|| - tau*||P_H D_f^*z|| - q*sqrt(1+tau²)

obeys |F(f)-F(g)| <= (1+tau)*2*pi*||t*z||*|f-g| for the declared centered times. This follows from the reverse triangle inequality, projection contraction and |exp(ix)-exp(iy)|<=|x-y|. Orthogonality of L,H even gives the sharper sqrt(1+tau²) coefficient by Cauchy-Schwarz on the two norm changes, but the proposed looser constant is valid. Magnitudes are periodic at the sampled-frequency seam, although centered complex vectors may acquire a common phase. A grid can exclude a whole remaining arc only with an actual covering radius and a positive lower enclosure F(grid)-L*radius. Floating evaluations require a quantified outward-rounding allowance for a numerical certificate. This proof supplies no such machine-error budget, hardware timing identity or real-data conclusion.

## 9. Scientific scope

The angular law, training/validation separation, waveform and time coordinate, quantizer bound and calibration units remain explicit suppliers. Eliminating the radial scale from a pivot does not derive these suppliers. Finite observations can test a declared directional model, but passing or failing a chosen statistic is not a scalar-force observation. No actual data were examined. The mathematical results do not select an initial field, scalar action/potential, scale or environment, and make no theory-wide no-go claim.

## 10. Actual independent controls and provenance

The standalone control source was frozen before execution. It uses only the Python standard library. It imports no author module, contains no observations and does not call a distribution package or a random sampler. Execution exited zero in approximately 0.039 seconds under Python 3.12.8. There were 51 recorded checks: 40 exact rational checks and 11 ordinary floating deterministic controls. Every recorded check passed; stderr was empty. There was no failed execution, setup repair or discarded attempt in this block. Counterexamples are deliberately successful demonstrations of invalid weaker claims, not suppressed failures.

The exact checks comprise a 128-point proper identity-covariance counterexample with rejection probability 1/2 at nominal 1/20; independently integrated beta-density versus finite binomial-tail identities at several ranks; the nonunit rank scaling; the validation-selection tail; direct two-dimensional simplex integration of joint coverage; amplitude tail identities; cancellation under a direction-dependent positive radius; closest-point cone attainment in complex directions against feasible radial grids; the unsafe quantizer-margin witness; the zero-denominator-rank counterexample; and the amplitude enlargement orientation witness. The radial grid is only an auxiliary control; global optimality is proved in Section 4.

The floating checks directly form small deterministic DFTs and orthogonal projections to compare Parseval/ranks, Dirichlet overlap, the conservative far bound, centered-time Lipschitz inequalities and alias degeneracy. They are illustrative implementation controls, not outward-rounded bounds or independent empirical tests. Small-N empty-color ranks were checked exactly from integer bin indexing. No Monte Carlo frequency was used to substantiate a probability theorem.

The code does not itself prove a receiver meets the conditional angular law, identify physical calibration, provide an observed scalar residual, or turn an IEEE calculation into a certificate. It does not rerun the author's controls. Exact algebra/proofs are the load-bearing evidence; numerical comparisons exercise the formulas on declared synthetic fixtures.

Additional joint qualification: if the quantization enclosure itself holds only on an event of conditional probability at least 1-delta, the safe joint bound is at least (1-alpha_g)(1-alpha_c)-delta, truncated at zero, without further independence. A simultaneous carrier/color/amplitude construction may use a union bound for direction tests and preserve the separate fixed-true-f amplitude statement. Any selected point estimate requires its own interpretation.

### Frozen independent identities

- Independent proof PRECHECK_v1.md: `2e9c6bfd76e6abb7eab78652bb62b9af971edde040224b7d20a175911a217f5b`.
- Independent control source independent_controls_v1.py: `8d2c70b442ae770321c1f2b46b36053feb8f31eff1703f62be7b0403115f8095`.
- Full control results CONTROL_RESULTS_v1.json: `6200b26ed1d757f870d8a334b9a1afef47a5251a6cb89cc9c239d88f2097a68a`.
- PRECHECK_FREEZE_v1.json and CONTROL_SOURCE_FREEZE_v1.json preserve the pre-exposure and pre-execution ordering. CONTROL_EXECUTION_v1.json records the command, runtime, source/result identities and empty stderr. The companion INDEPENDENT_MATH_IDENTITY_v1.json pins every file in this independent pre-exposure block.

No author-source correspondence has yet been performed. Any later comparison must be recorded in a separate immutable supplement; these files are not to be rewritten.
