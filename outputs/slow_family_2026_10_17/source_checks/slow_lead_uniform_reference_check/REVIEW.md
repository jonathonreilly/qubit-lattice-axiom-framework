# Selective check: uniform slow scalar reference

Disposition: conditional support for the stated scalar-reference family, with no necessary correction. The outgoing curve (12) and incoming bounds (16)–(17) follow on the exact positive domain. They do not prove actual-device success, full apparatus dynamics or a finite storage theorem.

## Revision, exposure and coverage

Read the COMPLETE target `../slow_lead_uniform_reference/PROPOSAL.md`, SHA256 5f2026dc3f63a757f13cf58bc468f05de10cfca9f04fda9c6615b816c9b94907. I did not author it. Root's proposed uniform route and domain were exposed. I authored the fixed scalar ancestor e6a9706d497d7c6abb5590d2baae0940efdf628e81101f5f4cfd91885e93ea8e; its root check6fb89d66d0a79e5c66c6dabd00c030ddb603308485f60c857b95f0e791b1a5f5 and full source were previously read and remain unchanged. This is a distinct-author check of the NEW uniform argument, not independent recertification of my fixed proof, blind checking or model diversity.

Read the needed exact scalar-measure and moment premises in `../slow_lead_uniform_endpoint/PROPOSAL.md`, SHA256 c8d2b7681f2059ec986bc3e41bf0a3eea8fefbc43c86addc17539b2f258bb887, especially its sections3–4, and the COMPLETE root check `../slow_lead_uniform_endpoint_check/REVIEW.md`, SHA256 f3e449109bc4bac6b4e4692d0db5f40c4d282d663b32f3b89a7ff1065ded28e0. I do not claim a new complete review of its actual endpoint/source inequalities. This scalar result uses its reference measure and moment identities only. Original fixed calibration, supplied phase and coefficient relations retain their inherited qualifications. Applicable unchanged instructions and review discipline are reused.

No numerical solver, parameter sweep, dynamics execution, delegation, W/Git/publication, model or prompt modification occurred for this check. Only deterministic reads/hashes and this review were performed. Previously requested publication wording corrections belong to the separate publication task and supply no evidence for this review.

## Domain and exact normalization

The domain requires strictly positive kappa,g,h, with H=d/gamma>=100, L=g/gamma>=100 and H/L<=.024. It follows that L>=100/.024>4000, so the looser outgoing-strip use L>=100 is conservative. Zero parameters are excluded: normalization, the reference pole and the time scale cannot simply be evaluated at kappa=0 or g=0.

Energy matching gives q(k)=pi/2-asin((g/j)cos k). The hard q band maps bijectively to the centered slow band with halfwidth asin(d/(2g)). The physical first slow site is m=0; the old port is a distinct finite coordinate. Exact flux/Jacobian normalization gives Fs=tf sqrt(dq/dk)F and consequently ps=p0-R. The physical transmission amplitude by itself would not preserve this measure. The reference phase61.5q+.5k+172k_old(q), including the fixed unimodular calibration scalar, is retained without treating61 as a slow spatial shift.

I reconstructed the scalar measure directly: with x=q-pi/2, y=tan x, A=2j-gamma and alpha=gamma/A, |D|^2=A^2 sin^2 x+gamma^2 cos^2 x. Dividing |F|^2dq by this expression yields exactly

    2kappa^2/[pi A^2] dy/[(y^2+alpha^2)(1+y^2)].

The integral on the full real y line equals1, since alpha(1+alpha)=2kappa^2/A^2. The integral on [-tan h,tan h] yields the endpoint source's exact p0 formula. Bounding both outside tails by y^-2 gives4kappa^2/(pi A^2 tan h), which is at most8j^2/(pi A^2 H). With A/j>1.9999 this is<.68/H. This is a parameter-dependent reference bound, not the fixed old numerical tail.

The second energy moment follows by cancelling the real denominator A^2 sin^2 x against delta^2=4j^2 sin^2 x. Its bound16kappa^2j^2h/(pi A^2) is less than.68 gamma^2 H using h/sin h<1.000001. Multiplication by the uniform reflection bound .251|delta|/g gives R<(.251)^2*.68 H/L^2<.043 H/L^2. Hence ps>1-.68/H-.043H/L^2. On the domain H/L<=.024 and H>=100, the loss is at most .0068+.043*.024^2/100<.006801; the stated ps>.9931 and1/sqrt(ps)<1.004 are safe.

The full-integer Fourier packets therefore have norm one after division by sqrt(ps). The incoming physical halfline includes m=0; the outgoing complement starts at m=-1. These index sets are used correctly in the later sums.

## Widened outgoing rectangle, branches and pole margin

For y0=1/(4L)<=.0025, |cos(x-iy)| is bounded by the slow-band displacement and sinh y0. Together with epsilon<1/2700 this gives |epsilon cos z|<5e-6, including the rectangle corners. Thus the principal arcsin and square-root branches remain analytic and away from their cuts. The old arcsin argument stays in its fixed interior neighborhood as well. The estimates |q'|<.000371 and |k_old'|<.25 imply |Phi_s'|<.55. The latter costs exp(.55y), not the smaller fixed-parameter phase allowance. Temporal decay has the correct sign: Im E_s=-2g sin x sinh y<=-1.99g y for t>=0.

The denominator rewrite D_s=-(2g-gamma epsilon)cos z+i gamma S(z) is exact, with S=sqrt(1-epsilon^2 cos^2 z). Comparing to S(x) separates a real term whose absolute magnitude does not decrease and an imaginary term gamma S(x)-A_s sin x sinh y. Because2g y0=gamma/2 and sinh(y0)/y0<1.000002, the imaginary term retains more than .499 times its real-line value, while remaining positive. Thus the Euclidean modulus comparison with .499 is legitimate. The correction gamma|S(z)-S(x)|<5e-10 gamma is much smaller than the real-line lower bound gamma S(x)>.999999 gamma. The final .49 margin applies everywhere, not just at the center or on horizontal edges. It excludes poles throughout the contour deformation.

The numerator ratios for S and sin z, the lower sine-denominator margin and exp(.55*.0025) produce a factor below2.05 after division by .49. The real part of the sine argument stays within .006004 of pi/2: the initial slow halfwidth, the real q halfwidth and its vertical displacement all fit in that allowance. This establishes the pointwise relative bound and hence the L2 shifted-line bound2.05 sqrt(ps). It is not a peak-amplitude estimate multiplied by a shrinking or growing band length.

## Outgoing bottom and hard edges

For m=-l with l>=1, the spatial multiplier on the lowered contour is exp(-l y0). Temporal damping gives exp(-1.99g t y0)=exp(-.4975 gamma t). Parseval on a zero-extended interval bounds the bottom norm by the stated2.1 exponential after normalization. Only the analytic integrand is deformed; the sharp cutoff is paid by BOTH vertical edges.

On the edges |2g cos x|=d, so the real part of the comparison denominator remains at least (1-gamma/(2j))d, up to the tiny S correction. H>=100 bounds that correction by5e-12 d. The .99d lower bound is safe. The numerator divided by this denominator is at most sqrt(L)/(H sqrt(ps)) times exp(.55y), since kappa sqrt(g/j)/d=sqrt(L)/H. Its remaining constant is strictly below1 with the stated elementary sine and pi bounds.

The outer Fourier factor and two sides give .8 sqrt(L)/(H sqrt(ps)) times1/(s_t+l), s_t=1.99g t-.55. For L sigma>=1, sigma=gamma t, one has s_t>=1.44L sigma>=1.44. The decreasing-function bound sum_(l>=1)(s_t+l)^-2<=1/s_t then produces at most .8/[H sqrt(ps sigma)]; discarding1/sqrt(1.44) is conservative. Adding the bottom and clipping by the unit full-packet norm gives (12). Earlier times have the valid ceiling1. There is no claimed uniform onset independent of gamma: physical time is sigma/gamma.

## Incoming depth-one rectangle and m=0

The auxiliary expression over0<k<pi maps to an interior q interval and is an exact scalar extension, not an assertion about the interacting source outside its band. Its transmitted mass is at most1. The portion removed to return to the hard band has mass at most1-p0, since flux transmission is contractive and the mapped complement is contained in the old reference complement.

On the depth-one rectangle, |epsilon cos z|<.000575 keeps q and k_old analytic, with their imaginary parts nonpositive. The sine denominator stays above.7 in modulus. The analytic continuation of the CONJUGATE coefficient must use Dbar and negative phase; the source does so. For q=alpha-i beta, Im Dbar=-sin alpha[2j sinh beta+gamma exp(-beta)]<0, including beta=0 because gamma>0. Therefore no poles are crossed. The negative phase has modulus<=exp(-y/2), and the temporal multiplier is contractive for all t>=0. It has modulus one on the verticals, where q and energy are real.

On the bottom, |cos(x-i)|>=sinh1 and |exp(-iq)|<=1 yield |Dbar|>=2g sinh1-gamma>2g. The phase-free numerator then has magnitude<1/sqrt(L). Paying the Fourier factor, interval length and square-sum of exp(-m) over m>=0 gives<1.6/sqrt(L). The bound includes m=0 and does not rely on a late-time damping factor.

On either vertical side the real part of Dbar has modulus2g cosh y(1-gamma/(2j))>1.99g cosh y. Since |sin z|=sinh y, the coefficient is bounded by y/sqrt(L); the phase supplies exp(-y/2). Both sides and the Fourier factor give .8/sqrt(L) times integral_0^1 y exp[-(m+.5)y]dy. The m=0 term is<=1/2; the remaining integrals are<=1/m^2. Thus their squared sum is<=1/4+sum m^-4<=19/12, and .8 sqrt(19/12)<1.1. The total auxiliary incoming halfline norm is<2.7/sqrt(L). This explicitly pays the potentially troublesome first slow site rather than starting the sum at1.

Hard-band subtraction costs sqrt(1-p0) in raw L2 norm by Fourier isometry and restriction. Dividing the result by sqrt(ps), not sqrt(p0), yields (16). Substitution of the established tail bound yields (17). For raw packets all final normalized estimates multiply by sqrt(ps), so neither hard-band loss nor reflection loss is hidden by normalization.

## Supported scope and limits

The stated scalar mass, all-time incoming and outgoing concentration bounds are uniform on the specified open parameter domain with H>=100 and H/L<=.024. Their dependence on H,L,kappa is explicit, and both small-parameter singular scaling and possible weak numerical bounds remain visible. The formulas do not select parameters, optimize resources or transfer the old fixed onset.

No actual attached-device coefficient identity, full spectral mass theorem, local recovery, complete all-time state bound, finite-cap success theorem, repeated read, permanent storage, precision robustness or native source/preparation claim follows solely from this scalar lemma. Those require their separate actual-device interfaces and composition. Conditional support here is limited to the exact source revision and inherited fixed calibration/phase relations above.
