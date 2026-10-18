# Standalone resonance survival bound: distinct check

No required mathematical correction was found. The exact energy density and its comparison with a normalized Cauchy measure prove the uniform phase-preserving survival-amplitude error <=4rho²/3 for 0<rho<=1/2. The tolerance corollary and substitution into the unchanged standalone complete-output estimate are valid. This is not pure exponential decay and supplies no new finite-router resource exponent.

## Exact pins and exposure

Paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.

* New source, completely read and SHA-256 verified: `common_product_resonance_tail/PROPOSAL.md`, `306174fb0a884c62d5c6de401492a742a3d8a55670ef273f9d376258e531c002`.
* Previously fully read and checked launch source, hash refreshed unchanged: `common_product_endpoint_launch/PROPOSAL.md`, `fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4`.
* Previously fully read and checked derivative source, hash refreshed unchanged: `common_product_launch_derivative_bounds/PROPOSAL.md`, `378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8`.

The already checked exact standalone spectral probability measure and amplitude cancellation are reused at their stated operator scope. Their measure ancestry is not re-audited here. ROOT suggested the resonance route and read this source; I read the candidate formulas before reconstructing them below. The unchecked ROOT design file is not a mathematical premise and was not needed for this check. This is source-exposed same-model verification with inherited effort, not blind or model-diverse replication. Existing workflow snapshots are reused, and no retained or formal audit status is assigned.

## Rational identity and its limited use

For z=exp(ik), cot k=i(z²+1)/(z²-1). Since A-d=2(1-rho²) and A+d=2, the denominator A cot k-i d is exactly `2i[1+(1-rho²)z²]/(z²-1)`. Multiplying its reciprocal by -icrho z yields the proposed negative coefficient -crho/2 in (2). The poles are ±i/sqrt(1-rho²), outside the unit circle for 0<rho<1. This confirms both phase and sign.

The source correctly separates this rational continuation from a justified contour argument. The physical k integral occupies a half-circle; exp[ijt(z+z^-1)] has an essential singularity at zero for nonzero t; and the fixed compact C2 cutoff has no supplied analytic continuation. The subsequent energy-density calculation does not rely on any of those unproved transformations.

## Exact energy-coordinate density

Set d=rho², r=1-rho² and x=cos k. Then A²-d²=4r, sin k=sqrt(1-x²), and the reversed measure has |dk|=dx/sqrt(1-x²). Therefore

    w(k)|dk| = [2rho² sqrt(1-x²)/(pi(4r x²+rho⁴))] dx
              = [sqrt(1-x²)/sqrt(r)] L_lambda(x) dx,
    lambda=rho²/(2sqrt(r)), |x|<1.

There is no doubled k interval or missing Jacobian. The energy phase is exactly exp(-i2jt)exp(i2jtx), retaining the common physical onsite shift. Extending this compact density by zero gives f_rho on the entire real line.

Mass one of f_rho follows from the adopted complete emitter measure through this one-to-one change of variable. The Cauchy density has mass one by its elementary arctangent integral. The comparison thus uses two actual normalized nonnegative densities; it does not assume the compact density has the same normalization as an unnormalized Lorentzian approximation.

## L1 discrepancy and constant

Write f_rho=q_rho L_lambda, with q_rho=0 outside (-1,1). Equal total masses imply the positive and negative parts of f_rho-L_lambda have equal integrals. Consequently the L1 difference is twice the positive-part integral. On the positive region, q_rho-1<=r^-1/2-1; integrating L_lambda over that region costs at most its total mass one. This proves `||f_rho-L_lambda||_1<=2(r^-1/2-1)`.

The positive region is exactly |x|<rho, since sqrt(1-x²)>sqrt(1-rho²) there. The negative part includes both the band-edge reduction and all Cauchy mass outside the physical band. Equal masses are what pay those contributions; they are not omitted from the estimate.

Rationalizing gives `2(r^-1/2-1)=2rho²/[sqrt(r)(1+sqrt(r))]`. For rho<=1/2, the denominator is at least 3/4+sqrt(3)/2>3/2. Hence the claimed 4rho²/3 bound holds uniformly, without an asymptotic expansion. The restriction away from rho=1 is material to this constant.

## Characteristic function, phase and all-time bound

For s>0, the Cauchy integrand lambda exp(isz)/(pi(z²+lambda²)) has one upper-half-plane pole at i lambda. On a large upper semicircle its rational factor is O(R^-2), arc length is O(R), and exponential modulus is at most one, so the arc contribution tends to zero. The residue gives exp(-lambda s). Conjugation handles s<0 and mass one handles s=0. This contour concerns the real-energy Cauchy comparison, not the earlier nonanalytic cutoff or z-plane phase.

The exact characteristic functions differ by at most the L1 discrepancy because |exp(i2jtx)|=1 for all real t. Multiplying by the unit phase exp(-i2jt) and using 2jlambda=jrho²/sqrt(1-rho²) proves (6) for all real times, with the stated complex phase. This is an amplitude estimate; it neither identifies survival probabilities nor states an exact exponential law.

For t>0, the old variation bound becomes 2/(pi jrho²t). Taking its minimum with one and the new exponential-plus-remainder ceiling preserves all three valid amplitude bounds. In particular the algebraic branch still tends to zero at late times, while the new branch alone has a nonzero uniform remainder. Thus (7) does not erase the band-edge tail.

If rho²<=3tau/8, the new remainder is at most tau/2. If t>=sqrt(1-rho²)log(2/tau)/(jrho²), the exponential is at most tau/2. Their sum is at most tau, so the tolerance corollary follows. It is a sufficient scalar survival-amplitude ceiling only; spatial packet errors are independent obligations.

## Unchanged complete-output substitution

The exact seeded state remains `a_s(t)|s>+O_tg_++I_tg_-`. The source coordinate is orthogonal to all lead coordinates, and the old cutoff/incoming analysis still bounds the lead discrepancy from W_t by L_t+2sqrt(P). Replacing only the source amplitude ceiling by R_res gives delta_res in quadrature exactly as written.

If delta_res<1, reverse triangle inequality gives ||W_t||>=1-delta_res>0. Positive normalization adds at most |1-||W_t|||<=delta_res, proving the 2delta_res estimate and its independent unit-vector distance cap two. No target phase, cutoff, spectral normalization or physical preparation has changed. Identical disjoint branches and passive-reference tensors preserve the same induced norm without a branch-count factor.

All actual source and lead coordinates remain in this comparison. The improved scalar envelope is not a new incoming-tail estimate, boundary residual, microscopic packet theorem or simultaneous finite-device parameter choice. No new runtime exponent follows from this component, and the frozen microscopic composition is not altered here.

Only this report was written. No scientific executable, symbolic solver, numerical integration, simulation, sweep, source/W/Git/PR/canonical/checkpoint/editable-prompt change, model override or delegation occurred. The check was analytical; hashing and directory creation were bookkeeping. No retained or formal audit status is assigned.
