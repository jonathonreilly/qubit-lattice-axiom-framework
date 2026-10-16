# M19 post-exposure extension correspondence

The extended mathematical inverse agrees with the independently frozen radial equations. The integral formula genuinely avoids differentiating j, while retaining a third-lapse-derivative supplier. Local candidate sufficiency is valid under the complete interval identities, positivity, vacuum and supplied zero-transverse sector. Two implementation admission gaps are reproduced below. They concern the exposed helper, not a sign or identity defect in the written theorem.

## Exact exposure and scope

After freezing `INDEPENDENT_DERIVATION_v1.md` (c12283ad707e79cc5bf9b09ba34379d88eba7b78f516b19159436b644a556e72), I copied and read the complete author working note and complete helper:

- `DERIVATION_v1.md`: 367e9b5be9598ea512e92477cec90c371a6831676652cf9b6a83d9d142feb1f3.
- `scalar_vacuum_metric_inverse.py`: e29f7f116a71073abc7a85254f447f580c87a88296a9d022c95035a11f457926.

Those immutable snapshots are recorded by `AUTHOR_EXPOSURE_v1.json`. I also inspected the full explicit physical action and parameter/coefficient definitions in the inherited M17 note, with the exact read scope recorded separately. I did not reread or claim a new review of all its remaining comparison results. The original blind derivation and its 35 exact checks remain unchanged.

This is a labeled post-exposure mathematical/source comparison. I ran 23 additional exact checks and one short synthetic outside-candidate local ODE solely to demonstrate an admission failure. I did not invoke the author aggregate, reproduce its two positive-candidate integration runs, open observations, or establish empirical accuracy. No formal audit or new theory selection is claimed.

## Equivalence and integrated parameter inverse

The author's u is my p=F'/F, and the author's H equals B times my J. Its j is

j=B u²/(2H)=lambda Y/(s+Y)=lambda/Theta.

Thus my differential compatibility is exactly

j'=u(lambda-j).

For a fixed base a, integrating this linear equation gives

j_b=lambda+(j_a-lambda)exp(-I_ab),   I_ab=int_a^b u dr.

Solving for lambda yields the stated pair inverse. A single pair determines a possible lambda when 1-exp(-I_ab) is nonzero. Candidate membership requires the same identity throughout the open interval; one pair or a finite set of reserved rows does not establish it. Conversely, for sufficiently regular j,u, the integrated identity for every endpoint b implies the differential identity. On a connected chart with continuous u nowhere zero, any distinct pair has nonzero I, although its magnitude may be small and the inverse ill-conditioned.

The geometric j uses u', hence third lapse and second B derivatives. The pair formula does not require j' and therefore avoids a fourth lapse derivative as an explicit supplier. It still needs an integral with a controlled error, not merely an unqualified numerical quadrature. The array helper's Simpson calculation and fixed small-denominator cutoffs are synthetic diagnostics, not measured derivative/integration error certificates.

For lambda>1 the branch

k=(1-2/sqrt(1+3lambda))/3

is uniquely in 0<k<1/3, and a=lambda/(1+3lambda), s=(1+k)/[k(1-3k)] follow from the supplied candidate's parameterization. Recovering s here uses that action relation; it is not a generic conclusion for arbitrary F=f0(s+z²). The scalar profile is Y=s j/(lambda-j), requiring 0<j<lambda throughout. No boundary or f0 appears. A lapse normalization cancels, and an absolute radial length calibration remains necessary to assign dimensionful potential scales.

## Potential, complete sector and degeneracy

The author's Wg expression equals my radial potential readout algebraically. Its basis is correct because log Y=2 log z:

P=V/f0=Hv²[3(s+Y²)]+Hv²nu[Y²(log Y)²/(4a)].

A nonzero two-radius determinant identifies the two coefficients conditionally. Both coefficients must be positive, and the equality must hold across the interval. Values outside the reconstructed scalar range are not learned. These are reconstructed parameters of the supplied potential, not a derivation of the potential family from axioms.

The previously derived metric-difference and Bianchi argument then supplies the radial scalar equation because z'!=0. The inherited complete physical action independently supports x=y=0 as a consistent sector: F and Z have no transverse dependence, the diagonal transverse coefficients depend on x,y through D=1+2(1+k)(x²+y²)/3, and each additional potential term contains x² or y². At constant x=y=0 all their Euler-Lagrange terms vanish. The post-exposure exact checks verify the coefficient and potential derivatives there. This establishes consistency of a supplied sector, not selection of that sector from a metric alone. Full transverse gradients or matter modify the null differences as the note states.

The actual positive-Hv candidate has the stated local degeneracy. At z=1, P=3Hv²(s+1), P_z=12Hv², while Schwarzschild-de Sitter has G_t=G_r=G_a=-3Hv² and R=12Hv². Every allowed k and nu therefore gives the same metric on a regular static annulus. This is distinct from my earlier generic V=0 Schwarzschild witness; I do not identify that generic witness with the positive-Hv candidate. Neither degeneracy refutes the admitted nonconstant-scalar inverse.

The coupled generator's box, lapse-slope and B' formulas agree with independently eliminating R using the trace and scalar equation, then solving the original rr and tt equations. Its analytical jets are obtained along the synthetic field flow. They are not independently calibrated observational jets. The residual formulas use the original metric and scalar equations with the correct slots/signs; I have not independently rerun the author's reported positive-fixture residual magnitudes in this comparison.

## Finite-error formula

Let Ehat=exp(-Ihat), |I-Ihat|<=epsilon_I and Eerror=Ehat[exp(epsilon_I)-1]. For finite inputs, nonnegative errors and

g=|1-Ehat|-Eerror>0,

the true E obeys |E-Ehat|<=Eerror, E<=Ehat+Eerror and |1-E|>=g. With lambda_hat=(j_b_hat-Ehat*j_a_hat)/(1-Ehat), exact subtraction gives

lambda-lambda_hat = [delta j_b-E delta j_a+(E-Ehat)(lambda_hat-j_a_hat)]/(1-E).

The author's numerator and denominator therefore give a valid deterministic bound under those supplied errors. No independence assumption is needed. This does not derive the errors from data or certify floating arithmetic.

An exact sharp corner tests all three numerator terms and the denominator: Ehat=1/2, Eerror=1/20, j_a_hat=1/5, j_b_hat=11/10, epsilon_a=1/100, epsilon_b=1/50. Taking E=11/20, delta j_a=-1/100 and delta j_b=1/50 yields lambda_hat=2 and lambda-lambda_hat=77/300, exactly the bound. This Eerror corresponds to epsilon_I=log(11/10). Thus the error formula itself is not the finding below.

## Reproduced implementation findings

1. The exposed `invert_metric` solves for h2 and h2nu, but does not enforce their finiteness/strict positivity before computing nu=h2nu/h2. One short local synthetic geometry was generated with k=0.1, Hv=0.03 and nu=-1.2 on [1,1.2]. This is deliberately outside the candidate, while still a regular solution of the general radial equations. The exposed inverse returned Hv²=0.0009000000000003386 and nu=-1.2000000000004856 without refusal, with tiny integral and potential residuals. The written theorem requires both positive coefficients. A candidate-admission function must enforce those gates; a diagnostic coefficient readout must explicitly avoid implying admission. No threshold or candidate premise should be relaxed to accept this witness.

2. `lambda_error_bound` does not reject nonfinite inputs or nonfinite intermediate/output values. A NaN j_a_hat with otherwise ordinary finite arguments returns `(nan,nan)` without refusal because the comparisons do not catch it. This violates the finite-input domain needed for a usable certificate. Finite checks should precede the formula and catch exponential overflow/underflow or a nonfinite result. Nonnegative supplied errors and positive certified gap remain necessary. The source's ordinary floats do not become interval-certified merely by adding these guards.

Both failures and the exact exposed source are preserved in `POSTEXPOSURE_RESULTS_v1.json`. The 23 exact checks pass; the two implementation findings are separately labeled reproduced failures, not hidden within a passing aggregate. The original blind evidence is unchanged. No claim is made about source edits after the frozen e29f7f11 snapshot.
