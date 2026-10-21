# Integrated launch derivatives: distinct bounded check

No required mathematical correction was found. The exact complex cancellation, cotangent integrals and cutoff product rules prove the stated explicit bounds G1<=C1/rho, G2<=C2/rho³ and B_minus<=C_minus/rho on the specified fixed-cutoff domain. The exact B_minus identity is also correct. This report draws no new complete-device runtime or resource conclusion.

## Pins and exposure

Paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.

* New source, read completely and SHA-256 verified: `common_product_launch_derivative_bounds/PROPOSAL.md`, `378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8`.
* Previously fully read and checked launch source, hash refreshed unchanged: `common_product_endpoint_launch/PROPOSAL.md`, `fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4`.
* Previously fully read and checked composition source, hash refreshed unchanged: `common_product_finite_seed_router/PROPOSAL.md`, `3a195efcf8d5196ed54a74228033d0888e7f18c864e481ce61b2efea6c67992b`.

Their existing checks in this coherent session are reused at their stated scopes, not treated as checks of these new integrals. I also checked the separate conservative baseline resource family, but its resource claims are not premises of this derivative result. ROOT suggested the cancellation and possible exponents; I read the new source formulas before reconstructing them. This is source-exposed same-model checking with inherited effort, not blind or model-diverse replication. Existing workflow snapshots are reused. No formal audit or retained status is assigned.

## Complex identity and normalization

Write X=a_src cos k and Y=d_src sin k. The original amplitude is `c gamma sin(k)exp(ik)(Y-iX)/(X²+Y²)`. Since Y-iX=-i(X+iY), cancellation gives `-i c gamma sin(k)exp(ik)/(X-iY)`. On 0<k<pi, division by j sin k yields exactly `-i c rho exp(ik)/(A cot k-i delta)`. The denominator's sign and overall -i are therefore fixed, not fitted. The incoming amplitude is the complex conjugate because the original spectral square-root density is real.

For the fixed real cutoff, p<=1 follows from 0<=chi<=1 and exact ||F||_2=1. Its central plateau gives p>=1 minus the exact spectral exterior mass, and hence the stated tail-based lower bound. If rho<=min{1/2,sqrt(pi tan(sigma)/8)}, then A>=7/4 and `4rho²/(pi A² tan sigma)<=1/(2A²)<=1/2`. Thus p>=1/2 is valid. In fact this argument has slack, but no stronger bound is needed. The true p remains the normalization constant, independent of k.

## Cotangent derivatives and exact integrals

For x=cot k, dx/dk=-(1+x²). Direct differentiation of h=(Ax-i delta)^-1 gives

    h' = A(1+x²)/(Ax-i delta)²,
    h'' = -2Ax(1+x²)/(Ax-i delta)²
                   +2A²(1+x²)²/(Ax-i delta)³.

These formulas include the derivative of x and of its Jacobian factor. The interval maps onto [-L,L] with positive integration measure dx/(1+x²) after orientation reversal. For h, dropping only this denominator bounds the integral by `(2/A)asinh(AL/delta)`. For h', its numerator cancels the Jacobian exactly, giving

    A integral_{-L}^L dx/(A²x²+delta²)
       = (2/delta)arctan(AL/delta).

This is equality for the norm over the full conservative cutoff interval. Norms over the actual support are at most this value; no equality over a possibly smaller support is required.

For the first h'' term, its integrated absolute value is `2A integral |x|/(A²x²+delta²) dx`. Integrating x/(A²x²+delta²) on [0,L] and doubling gives `(2/A)log(1+(AL/delta)²)`. For the second term, the canceled Jacobian leaves 1+x²<=1+L²=S. The primitive of `(A²x²+delta²)^(-3/2)` is `x/[delta² sqrt(A²x²+delta²)]`, so its bound is `4A²SL/[delta² sqrt(A²L²+delta²)]<=4AS/delta²`. Adding the two absolute terms proves H2. Their possible interference is not needed. No linewidth approximation or substitution for the exact denominator enters.

## Cutoff and phase derivatives

F=-ic rho exp(ik)h gives F'=-ic rho exp(ik)(ih+h') and F''=-ic rho exp(ik)(-h+2ih'+h''). Applying the cutoff product rule adds chi'F in the first derivative and chi''F+2chi'F' in the second. Taking L1 norms yields exactly `(K1+1)H0+H1` and `(K2+2K1+1)H0+(2K1+2)H1+H2`, respectively. Thus no cutoff or phase derivative is omitted. Division by the same sqrt(p) proves (7).

Because the support has measure at most 2sigma' and g has L2 norm one, Cauchy–Schwarz gives G0<=sqrt(2sigma'). This is independent of the alternate H0 estimate and can be used with it by taking a minimum.

At fixed cutoff, A stays bounded above and away from zero as rho decreases. The displayed H0,H1,H2 give orders log(1/rho), rho^-2 and rho^-4. Multiplication by rho/sqrt(p), with p>=1/2, proves the stated big-O upper bounds, without asserting asymptotic equalities.

For the pure-power constants, |h|<=1/delta and the x-domain estimate give H0<=2L/delta. H1<=pi/delta is immediate. The inequality log(1+y²)<=2y follows by differentiation or integration, yielding H2<=4L/delta+8S/delta² since A<=2. The factor c/sqrt(p)<=2/sqrt(pi) then produces C1 exactly. In G2, the terms proportional to rho/delta=rho^-1 can be bounded by rho^-3 because rho<=1. The resulting C2 is precisely the displayed expression. All constants depend only on the fixed cutoff and its conservative band; changing those with rho would require a new estimate.

## Raw incoming launch constant

Reality of chi gives chi g_-=conj(chi F). Hence its derivative L1 norm is sqrt(p)G1 and its L1 norm is sqrt(p)G0. The coefficient 2j/vmin is sec(sigma'), proving the exact identity `B_minus=sqrt(p)[G1+sec(sigma')G0]`. There is no reciprocal normalization or additional phase term.

Using the unnormalized product derivative estimate and `||chi F||_1<=sqrt(2sigma')sqrt(p)<=sqrt(2sigma')` proves (11). Substitution of H0<=2L/delta and H1<=pi/delta gives a first term `c[2L(K1+1)+pi]/rho`. The remaining fixed term is bounded by the same term divided by rho since rho<=1. This proves C_minus exactly as stated. These coefficients therefore apply directly to the raw incoming-launch term in the checked composition.

## Scope and record

The improved integral estimates concern the same exact source amplitude, cutoff normalization, phase and supplied Hamiltonian. They do not change preparation premises or establish optimal derivative growth. Existing looser derivative bounds remain valid. A complete resource improvement requires a separate simultaneous substitution into every launch, geometric, boundary, normalization and whole-time microscopic error, with its own physical cap proof; none is claimed here.

Only this report was written. No scientific executable, numerical integration, symbolic solver, sweep, source/W/Git/PR/canonical/checkpoint/editable-prompt change, model override or delegation occurred. The calculations were reconstructed analytically; hashing and directory creation were bookkeeping. No retained or audit status is assigned.
