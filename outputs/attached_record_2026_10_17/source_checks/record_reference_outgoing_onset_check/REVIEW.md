# Selective check: shifted-reference concentration

Disposition: support the scalar-reference statement at source SHA256 3a554c4edf266a8e53cd43b57bb03c280dcf601b4eb3da502fa6a3d33bfc5fe0. The complete source was read. The supervisor requested this derivation but did not author it. This is a source-exposed analytical reconstruction, with an alternative pole-location check and direct Fourier-space norm argument. It is not blind or model-diverse verification, independent recertification of all inherited reference premises, or actual attached dynamics certification.

## Domain and pole check

Use exactly the supplied fixed j, kappa, phase and reference measure. Set x0=kappa²/j² and h=x0/4. In w=exp(iq) coordinates the denominator is

    D=-(j-gamma)w-j/w.

Its zeros have |w|=(1-x0)^(-1/2). Since -log(1-x0)>x0 for 0<x0<1, their imaginary depth is -log(1-x0)/2>x0/2=2h. Thus the strip from the real hard band to depth h crosses no outgoing pole. This checks the particularly important sign: the poles are below the real q axis, but the contour stops above them. The incoming proof used a different denominator and cannot substitute here.

On the actual strip, the explicit arcsin argument is within the unit disk and away from its cuts. The derivative formula bounds |k'|<.25, hence |61+172k'|<104. The resulting phase growth is exp(104y), not decay. The temporal factor decays because Im E=-2j sin(x)sinh(y)<-.0053y. For n=-m<=0 the spatial factor is exp(-my). These signs include m=0 and the gate-origin coordinate.

## Horizontal norm without a peak estimate

For fixed t, extend g_t=1_I F(x-ih)exp(-itE(x-ih))/sqrt(p0) by zero to a period of length2pi. Its integer Fourier coefficient sequence has squared norm integral|g_t|². For the selected negative integers, multiply the coefficients by exp(-mh), which has norm at most1. Bessel/Parseval therefore bounds the whole bottom contribution by ||g_t||. This remains valid though the hard cutoff is discontinuous: no analytic continuation of the indicator is used. Cauchy deformation is applied to the analytic integrand on the finite rectangle, with both cutoff sides retained.

Direct expansion gives |D(x-iy)|²=A_y²cos²x+B_y²sin²x. Here B_y>=gamma exp(y)/2 and A_y>A0/2; consequently the bottom denominator is at least half the real denominator pointwise, including the resonant center. The exact numerator ratio is 1+sinh²h/sin²x, below1.000001. Squared phase growth is also below1.000001. It follows that ||F(.-ih)||<2.000002 sqrt(p0). Combining with temporal decay yields the claimed 2.01 exp(-.0053th). No large peak times band width or geometric-series factor is required. This is the load-bearing improvement over the former scalar bound.

## Cutoff contributions and constants

At either endpoint, A_y sin Delta>.0053 Delta follows from j>.0027, gamma exp(h) tiny compared with .0001 and sin Delta/Delta>1-Delta²/6. Both endpoints are far from the resonance relative to gamma. With sqrt(2pi)>2.5, the coefficient excluding its phase growth is bounded by170 kappa/Delta after dividing by sqrt(p0). Each vertical integral contributes at most this coefficient divided by (vt-104+m), times the outer Fourier normalization. Paying both sides gives136 kappa/[Delta(vt-104+m)].

The decreasing positive series is bounded by s^-2+s^-1<=2/s for s>=1. Its norm is therefore at most136 sqrt(2) kappa/(Delta sqrt(s)), which is less than .75/sqrt(s). Neither cancellation nor orthogonality between the sides or bottom is assumed. The triangle bound stated in the proposal follows.

At T=10^15, h>1/(3.6*10^11), hence vTh>14, and vT-104>(2.3*10^6)². The displayed elementary lower bound exp(14)>845000 makes the bottom term smaller than2.38e-6; the sides are smaller than.327e-6. Their sum is below2.8e-6. Both decrease for larger t. Exact full-lattice normalization then gives right-ray squared mass>1-7.84e-12 for every t>=T. The unnormalized reference multiplies by p0, so its omitted left norm is no larger and its total mass remains p0, not1.

## Scope

The reference identity p0>1-1.1e-6 and unit-modulus calibration scalar are inherited checked premises. Source/header physical phases and n>=1 agree with the attached profile currently under composition. Literal old aging and passive references preserve the scalar norm; actual off-diagonal input/window contributions still require their own operator estimate. No interacting resolvent is continued into this strip, no local apparatus decay rate is proved, and no old temporal theorem is transferred. This is a sufficient reference onset, not an optimum, simulation or full-state attached runtime.

No new code execution, parameter sweep, numerical integration, model change, audit verdict or editable prompt change occurred. This review supports using the scalar concentration premise in a separately checked actual branch/finite-window composition.
