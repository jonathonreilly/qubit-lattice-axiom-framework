# M18 working-proof correspondence, after independent derivation

I read all of root's `WORKING_v2.md`, frozen here as `AUTHOR_EXPOSURE_v1__WORKING_v2.md`, SHA-256 `92d5f254b652c176fa3ee668ccc2c55ad84ed9c0700ca0345dbdb8ff2faba7f8` (5544 bytes). This comparison is explicitly post-exposure. The original independent derivation/freeze, 37 controls and failure witnesses are unchanged. No root extension code or numerical output was read or executed. This is focused mathematical source correspondence, not a formal audit or empirical validation.

No material mathematical discrepancy was found within the stated necessary-comparison scope. The new oscillating-lapse example is root's construction. I independently checked its complete analytic argument after exposure; it was not part of my pre-exposure derivation.

## General equation, threshold and measurement scope

The arbitrary-power product identity, its fixed power p=lambda, the drift weight N^(2lambda+1), and the coefficient C=lambda R3/2+lambda^2|grad ln N|^2 agree with the independent derivation. The positive gradient-square term remains in the unfavorable zeroth-order source, with the correct sign. The root chooses wB=zB/m^lambda, with m the minimum on the entire closure. This valid, deliberately looser threshold ensures both the complete boundary condition and w>wB implies z>zB>=1. It avoids the exact boundary-only and unnormalized-threshold failures preserved in my independent report. No sharper threshold is needed for root's stated result.

The positive Dirichlet inverse is that of the drift Laplacian, and the truncation has a constant threshold. Therefore the Kato/Green/sup argument is the same valid one as in my independently frozen proof. In particular, eta in this version is sup P because C already includes lambda; no extra lambda is to be multiplied into it. Constant time-coordinate scaling cancels from the operator, P and physical ceiling.

The spherical quadrature and sufficient envelope R^(2lambda+1) Cmax L^2/(6Bmin) have the correct factors. The outward clock/range expression follows by B'/B=-2(f'/f+g'/g). It uses f' and g'=tau'', not f''. The note properly preserves whole-domain and boundary coverage, areal-radius calibration, static and vacuum propagation assumptions, and specifically limits the ball estimate to a regular ball. Outward data beyond a noncentral emitter do not furnish a missing interior or an annulus's inner boundary.

## Uniform rational bound for the oscillating family

For k=1/10, lambda=117/49. With epsilon=3/20, K=2 pi n and positive integer n,

    ell=epsilon[cos(Kr)-1]/K,
    ell'=-epsilon sin(Kr),
    min ell=-epsilon/(pi n).

The radial function is smooth at the center because its Taylor series contains only even powers of r. Each fixed-n metric is smooth and positive; there is no claim of uniform higher-derivative bounds over n. Integer n gives N(0)=N(1)=1, Nmax=1, and the stated minimum. For B=1, R3=0 and the transformed nonnegative source is exactly lambda^2 epsilon^2 sin^2(Kr).

The Green envelope gives

    eta <= exp[(2lambda+1)epsilon/(pi n)] lambda^2 epsilon^2/6.

Since n>=1 and pi>3, let x=(2lambda+1)epsilon/3=283/980 and y=lambda epsilon/3=117/980. Both lie in (0,1). The inequality exp(t)<=1/(1-t) for 0<=t<1 follows from -ln(1-t)-t>=0; its derivative is t/(1-t). Consequently

    Ebar=41067/1366120 <1,
    sup z/zB <= 1/[(1-y)(1-Ebar)]
               =1338797600/1143520739 <6/5.

Thus the author's uniform bound is valid for every positive integer n under the common comparison premises, without a quadrature or numerical-solver premise. It is not merely a statement about the four displayed numerical frequencies.

## Original positive-curvature criterion at n=64

The physical curvature source in M17 is c_old=(R4)_+/2, with

    R4/2=epsilon K cos(Kr)-epsilon^2 sin^2(Kr)
                          +2epsilon sin(Kr)/r.

The apparent central quotient is regular, with limit 3epsilon K for the complete raw source. From m<=N<=1, positivity of c_old and Fubini give the exact original Green lower bound

    P_old(0)>=m integral_0^1 r(1-r)c_old(r) dr.

On [1/4,3/4], r(1-r)>=3/16 and

    c_old>=epsilon K (cos Kr)_+-(epsilon^2+8epsilon).

For cos Kr<0 the right side is negative, so this inequality remains valid there; it does not incorrectly replace cos by its positive part inside an equality. For cos Kr>=0 the negative remainder has magnitude at most epsilon^2+8epsilon. Positivity of c_old permits replacing the weight by 3/16 before using this possibly negative lower bound.

For even n the half-length interval contains exactly n/2 full periods, regardless of phase at its endpoints. The integral of (cos Kr)_+ over it is 1/(2pi). Therefore

    lambda P_old(0)>=lambda exp[-epsilon/(pi n)]
                        *3[2epsilon n-epsilon^2-8epsilon]/32.

At n=64 the bracket is positive. The replacement exp[-epsilon/(pi n)]>=1-epsilon/(3n) is then in the correct lower-bound direction. The resulting exact rational lower bound is

    3228248439/802816000 >4.

The outside lambda here is required: M17's old P solves the source c_old without lambda. Root consistently distinguishes that convention from the transformed P. The old sufficient condition eta<1 therefore definitely fails at n=64 while the new sufficient metric criterion remains admitted for every n>=1.

## Usefulness and limitations

This proves a strict difference between the sufficient criteria on a family of supplied smooth static geometries. It is not a counterexample to M17: M17's small-Green-norm premise fails. Nor does it prove that this family admits a full solution of the candidate metric, matter and scalar equations, or that any physical instrument realizes it. The note explicitly keeps that distinction. Its statement about reducing the lapse supplier's derivative order is justified, while spatial geometry, first derivatives, boundary values and their calibration remain required.

Root separately reported a numerical v3 run with 60 passing and 3 failing checks, involving old-source quadrature at n=16 and n=64 and the n=64 scalar BVP node limit. I have not inspected or diagnosed those records and do not convert this analytic confirmation into a validation of them. The analytic inequalities above neither depend on numerical success nor resolve the outstanding numerical implementation claims. A changed grid or node cap must retain its failed predecessors and still satisfy the originally stated tolerances.

The independent post-exposure program `postexposure_analytic_controls_v1.py` verifies 31 exact identities/inequalities, all passing, including the complete curvature source, center limits, rational constants, period integral, weight kernel and threshold/source factors. It imports no author code. These 31 checks are distinct from the earlier 37 pre-exposure controls. No additional data, initial state, covariance, matter solution, or physical noise budget was selected.
