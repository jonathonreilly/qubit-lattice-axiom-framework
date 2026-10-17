# Selective check of the all-time incoming scalar reference

Disposition: support the stated scalar-reference bound, conditional on the explicitly supplied nominal reference parameters and phase. No correction is required. For precisely the coefficient and physical half-line in equation (3), the normalized hard-band norm is less than .00105 for every t>=0. This does not identify the actual attached incoming matrix coefficient or establish an actual all-time herald theorem.

## Sources and exposure

I read the complete proposal `../record_incoming_alltime/PROPOSAL.md` at SHA256 `1def426f0919789b6a1a8c4048756c3a95a6a2b9ed4b5223c90e0ca321db8bf7`. I did not author this contour argument. The requested target and preceding reference/endpoint results were exposed, so this is separate analytical reconstruction, not blind review or model-diverse certification.

The nominal converter note at SHA256 `f8480df631730d3e4e9fadb07b73486a1e02aec650511f7eae859ae2dabbe311` was previously read; its exact phase and coefficient definitions were refreshed here. I refreshed the complete reference-measure check `1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae`. The complete wider-band source `d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2` and its reference-tail calculation were refreshed in the immediately preceding outgoing-profile check. I authored that bandwidth extension, and rely conditionally on its separately checked unchanged parameter/tail premises; this is not independent recertification of my ancestry. The exact attachment phase comes from the previously read attachment `fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457`, whose distinct full review `7df395639ea91083d9321fd05f91ffbae94eb3ae87256beb09f7f4474fa2b005` was also read completely in the preceding check.

Applicable unchanged workflow and physics-claim-reviewer discipline were reused. Only source reading, deterministic identity bookkeeping and analytical reconstruction were performed. No scientific execution, integration, dynamics, delegation, W/Git, publication, prompt or model change occurred. This review is the sole deliverable; no editable prompt file changed.

## Phase, normalization and scalar extension

The supplied original rho_g=-zeta exp(92ik), followed by rho_n=-exp(80ik)rho_g, gives rho_n=zeta exp(172ik). Multiplying the original i exp(21iq) reference numerator by the attachment -i exp(40iq) gives exactly exp(i61q+i172k), with no remaining i. Conjugation on the real interval produces exp(-i61q-i172k)/Dbar and conjugate(zeta). Combining with exp(-iqn) gives n+61, with the favorable positive shift; neither the 61 nor the 172 can be replaced by a phase-free amplitude estimate.

The auxiliary branch k=2 arcsin(a sin(q/2)), a=sqrt(j/J), obeys cos k=1-2a^2 sin^2(q/2)=C0+(1-C0)cos q and agrees with the nominal positive branch. Its use for 0<q<pi extends only the explicit scalar reference expression. It imports no source scattering estimates outside the certified small band.

On that real interval the phase is unimodular, and |F_out|^2 is exactly 2kappa^2 sin^2 q/(pi |D|^2). The checked free-emitter measure therefore supplies total mass one and the stated reference tail. The reference parameter satisfies 0<kappa<j, so the reference's no-atom conclusion applies. Extending the coefficient by zero to a 2pi interval gives the usual integer Fourier isometry. Multiplication by exp(-itE(q)) is unitary on real q and restriction to n>=0 contracts the norm. Consequently the omitted auxiliary coefficient costs sqrt(1-p0), not 1-p0, and division by sqrt(p0) in (5) is correct. The hard cutoff has not been treated as analytic.

## Analytic rectangle, poles and time sign

For z=x-iy in the specified rectangle,

    Dbar(z)=-j exp(iz)-(j-gamma)exp(-iz).

Since 0<gamma<j, the first term's magnitude j exp(y) strictly exceeds the other's (j-gamma)exp(-y), including y=0. There is no denominator zero anywhere on the closed rectangle. Compactness and continuity allow a neighborhood of that rectangle on which it is nonzero, even though the distance to the nearest pole above the real axis can be very small. No uniform neighborhood in kappa is required.

C0>.9 implies a<1/3. The inequality |sin((x-iy)/2)|<=cosh(y/2), together with cosh(1/2)<1.2, puts the arcsin argument strictly inside the radius-.4 disk. The principal arcsin is analytic on a neighborhood of this image. Its real part lies between -pi/2 and pi/2, so Im v=cos(Re arcsin v) sinh(Im arcsin v) proves that its imaginary part has the same sign as Im v. Here Im v=-a cos(x/2)sinh(y/2)<=0. Thus Im k<=0 and exp(-i172k) has modulus at most one. This also covers x=pi, where the argument is real; no branch cut is crossed.

The signs of the remaining factors are likewise correct: |exp(-i(n+61)z)|=exp(-(n+61)y), while Im E(z)=-2j sin x sinh y<=0. Therefore |exp(-itE(z))|=exp(t Im E(z))<=1 for every t>=0. At the vertical edges E is real, so the latter modulus is exactly one. This is a genuine all-nonnegative-time bound, not a large-time oscillatory estimate. Negative times are outside its scope.

All factors are analytic near the finite closed rectangle. Cauchy deformation is therefore legitimate, with the bottom and both vertical edges retained. There is no omitted residue or contour-at-infinity term.

## Explicit norm estimates

On the bottom, reverse triangle gives |Dbar|>=2j sinh(1); |E'|<=2j cosh(1), hence the ratio is below 2. The Fourier prefactor kappa/(2pi j) and horizontal length pi give exactly the stated bottom coefficient ceiling (kappa/j)exp(-(n+61)). Its square-sum is the displayed geometric-series expression.

At either side, |Dbar|=2j cosh y-gamma exp(-y)>j and |E'|=2j sinh y. Paying both sides gives 2kappa/(pi j) times the integral in (6). For m=n+61>1,

    integral_0^infinity sinh(y) exp(-my)dy=1/(m^2-1).

The extension to infinity is only an upper bound on this positive scalar integrand, not an extension of the analytic contour or of its phase bounds. Also m^2-1 >= (n+60)^2. The decreasing-function sum estimate yields

    sum_(n>=0)(n+60)^-4
       <=60^-4+integral_0^infinity (x+60)^-4 dx
       =7/4320000 <1/750^2.

Thus Minkowski proves (7) without assuming that the bottom and sides are orthogonal. With j>.0027, pi>3, kappa=1e-8, the side norm is below 3.3e-9. The stated elementary exponential inequalities give bottom norm below 1e-22; hence 4e-9 is conservative.

Finally .001049^2=1.100401e-6 exceeds 1.1e-6, and (1-1.1e-6)^(-1/2)<1.000001. Therefore (.001049+4e-9)*1.000001<.00105. The normalized reference result follows, and the unnormalized hard-band version is no larger. The dominant allowance is the charged reference cutoff tail, not a demonstrated attached-seed tail.

## Safe downstream use

The proposal correctly limits its conclusion to the scalar expression (3). Actual incoming coefficient identification requires the attached two-lip spectral jump, record-sector signs, literal old/parity multipliers and compatible reference planes. Nothing here proves that complex conjugation of the chosen outgoing comparator is already the actual incoming matrix coefficient.

If the required actual coefficient discrepancy is bounded in L2 of operator norm, Fourier isometry for each fixed input and half-line contraction do bound its induced operator error by that L2 ceiling, also with passive references. The .00105 scalar reference allowance can then be added after correct coherent aggregation. Incoming and outgoing errors occupy the same physical ray and must be added by triangle inequality unless orthogonality is independently proved. Full local/closed output, omitted actual spectral mass, success, finite-device recurrence and normalized early-time claims remain outside this review. No retained/audit status is conferred.
