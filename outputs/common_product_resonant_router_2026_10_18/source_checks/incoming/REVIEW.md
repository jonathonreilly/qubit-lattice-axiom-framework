# Resonance-resolved incoming boundary tail: distinct check

Disposition: SUPPORT for the stated normalized-cutoff scalar amplitudes and their incoming finite-boundary interface. No required correction found. The exact energy transform, removable pole, residue, cutoff remainder, improper Fourier integrations and sqrt(6) boundary factor are supported. No new complete finite family or end-to-end exponent follows.

## Evidence and exposure

Read the complete `common_product_resonant_boundary_tail/PROPOSAL.md` and verified SHA256 `4eb53a9531fa977e0ef775aadd3a5ca37f4e3d42d83488d44a9fbc6d730150bc`. Paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

Reused complete recent reads of the exact standalone launcher `fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4` and phase-preserving cancellation source `378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8`. Their mass-one measure and real-cutoff conventions remain scoped standalone premises. The finite incoming-interface source `532866ed3e3d9117906c4f5b6be3839fdc45c522bae727d1980e724ad11b7123` and my complete finite review `5ef953f745c598888b329aa8fafa94d226a18f2cc01fa57f09b165e0e7a1a936` supply only the phase offsets, common fiber and actual hopping-cut norm used here.

The geometric source `be2ab9da4b62ca7f595c17fea5ec6e62849cdada2c34416154996ad15180538e` and distinct review `cfd880ac1dcd866fe47fd51c7b8f29764270fc028e67e540c1cb1a6b1f86dfed` were fully read recently, as were survival source `306174fb0a884c62d5c6de401492a742a3d8a55670ef273f9d376258e531c002` and my prior review `de9dbd20bf873f194d969ec6570e77224a2dfb192ba3ac4035b0933fc3d610bd`. Their geometric/survival conclusions are not premises for the new pole-remainder calculation. No full-circle replacement or scalar-to-spatial theorem transfer is used.

ROOT proposed the incoming-boundary route and reported a full read. The author wrote the finite source and checked geometric ancestry; I checked earlier launch/survival/finite interfaces and read the exposed new calculation. This is same-model selective analytical checking, not blind replication or retained audit. Applicable previously read reviewer/workflow instructions are reused. Only this report was written; no source/W/Git/checkpoint/axiom/editable-prompt/model change, scientific executable, delegation or publication occurred.

## 1. Exact normalized quantity and energy variable

The hypotheses imply p>=1-3rho^2/h>=13/16, so the actual positive normalization is controlled. They also imply delta=rho^2<=10^-3/16, a>.99 and lambda=delta/(2a)<h. The original source policy satisfies these hypotheses with ample margin.

In F, replacing cot k by x/s gives numerator -i sqrt(2/pi)rho exp(ik)s divided by Ax-i delta s. The Jacobian dk=-dx/s cancels this s. The two Fourier normalizations combine to 1/pi, and reversal of limits leaves no extra sign. The residual phase factor exp(i(d+1)k) is x+is, 1 or x-is for d=0,-1,-2 respectively. This proves (3), including its coefficient rho exp(-i2u)/sqrt(p), from the physical upper-semicircle integral with g rather than conjugate(g).

Rationalization gives A^2x^2+delta^2s^2=4a^2(x^2+lambda^2). Also s_lambda=A/(2a), delta s_lambda=A lambda and

    (x+i lambda)[A-i delta(x-i lambda)/(s+s_lambda)]
      =Ax+i delta s.

This checks the exact cancellation of x+i lambda, leaving b_d(x)/(x-i lambda). It removes the lower pole; it does not discard its residue by approximation. The remaining upper pole is correct for exp(+i2ux) at u>0.

## 2. Analytic coefficients and cutoff derivative constants

On |z|<=1/2, 1-z^2 has real part at least 3/4. The branch s(0)=1 therefore has Re s>=sqrt(3/4) and |s|<=sqrt(5/4); s+s_lambda has no zero. Each t_d has modulus below 2. With the stated small delta, the bracket in b_d is below 3 and 4pi a^2>11, proving the loose bound |b_d|<=1 on this disk.

At z=i lambda, the bracket reduces exactly to A. Since lambda+s_lambda=1/a and lambda-s_lambda=-a, the three t-values are i/a, 1 and -ia. Thus both the phases and magnitudes of (6) are correct.

For real |x|<=h, the segment from i lambda to x lies within |z|<=h. Radius-1/4 Cauchy disks lie inside |z|<1/2. Writing the divided difference as an integral of b_d' gives derivative ceilings m!4^(m+1), hence 4,16,128 for R_d,R_d',R_d''. These bounds are uniform as rho shrinks.

The transformed cutoff is constant one on |x|<=sin(h/2), which contains |x|<=h/3, and vanishes beyond sin(3h/4)<h. Chain differentiation gives |theta'|<=16/h and |theta''|<=400/h^2+16/h<=500/h^2. Support length at most 2h yields the three L1 bounds in (8). The product second derivative is bounded by

    4*(1000/h)+2*16*32+128*2h
      =4000/h+1024+256h<=5280/h.

Compact C2 joining produces no distributional boundary terms.

For W=(theta-1)/(x-i lambda), theta'' and theta' are supported away from |x|<h/3, and theta-1 also vanishes there. Its three second-derivative terms have respective L1 ceilings 3000/h^2, 576/h^2 and 18/h^2. The last follows by integrating 2/|x|^3 over both exterior intervals. Therefore ||V_d''||_1<=5280/h+3594/h^2<9000/h^2 on the specified h domain. All cutoff derivative and artificial exterior-tail costs are present.

## 3. Improper transforms and residue

Outside a compact interval, V_d=-b_*/(x-i lambda). Consequently V_d tends to zero, V_d'=O(x^-2) is integrable and tends to zero, and V_d''=O(x^-3) is integrable. Integration by parts first defines the oscillatory integral for u>0 via an absolutely integrable derivative; a second integration gives its norm bound ||V_d''||_1/(4u^2). Absolute integrability of V_d itself is neither true in general nor required.

The pole integral likewise exists as an improper oscillatory integral. Closing above, the arc estimate has bounded prefactor R/(R-lambda) and angular integral exp(-2uR sin theta), which tends to zero by dominated convergence for fixed u>0. The residue at i lambda is exp(-2lambda u), giving 2pi i times that value. No continuation of the real cutoff or k-circle time factor is involved.

The compact integrand equals b_*/(x-i lambda)+V_d pointwise: outside the cutoff these artificial tails cancel exactly. Multiplication by rho exp(-i2u)/sqrt(p) gives C_d=rho A t_d(i lambda)/(2a^2 sqrt(p)), with the fixed physical exp(-i2u). The remainder ceiling is 9000sqrt(2)rho/(4h^2u^2)<4000rho/(h^2u^2). Finally |C_d|/rho<=1.5/.99^3<2. This proves (14)--(15) with all phases and constants retained.

## 4. Integrated amplitude and actual boundary factor

Integrating the positive exponential ceiling gives

    (2a/rho)[exp(-rho^2 u0/a)-exp(-rho^2 U/a)],

and integrating u^-2 gives (4000rho/h^2)(1/u0-1/U). The infinite-upper-limit convention is valid because both tails are integrable for u0>0. Dropping the upper subtraction and using a<=1 proves the advertised (2/rho)exp(-rho^2 u0/a)+4000rho/(h^2u0). No cancellation is assumed after taking absolute values.

At finite532866's incoming cut levels n=ell,ell+1,ell+2, the scalar offset ell-n is exactly 0,-1,-2. Each coefficient multiplies the same supplied path/program/reference vector in record0, so no channel/path/reference multiplicity is added. At each time the three-level norm is bounded by sqrt(3) times the common scalar bound. The hopping-only perturbation has norm <=sqrt(2)j. Converting dt to du/j cancels j and leaves exactly sqrt(6) multiplying the integrated allowance in (17). The incoming record threshold is zero and any common physical scalar has modulus one.

This improves only the incoming portion of that Duhamel estimate. The outgoing field, internal maps, initial match, survival, final truncation and all simultaneous budgets remain separate. The ratio rho^4/h^2<=1/256 concerns coefficient dependence, not uniform numerical superiority at every time; taking a minimum with the earlier valid incoming bound is legitimate.

## Limits

The result applies to the exact normalized compact-cutoff profile. It does not immediately apply to uncut F: omitted spectral mass would need its own integrated estimate, and multiplying a uniform L2 error by an arbitrarily long interval would not supply one. Nor does it establish full incoming half-line decay, outgoing q-channel bounds, a new finite length/time family, preparation or thermal improvement, native coefficients, readout/capture/reset or permanent halt. The checked new result is the resonance-resolved incoming scalar integral and its explicitly bounded physical cut interface.
