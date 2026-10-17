# Fixed-spectrum orientation: supplied precision is still present

Root analytical assessment, proposed pending selective check. This is a local parameter interpretation, not a device theorem or impossibility claim. Source: endpoint_precision_root_notes/FIXED_EIGENVALUE_INTERFACE.md SHA256548c8579d603200db45c7c7f4fdd3f2cef08aee53846efe524ef94591b692057 and its checked full-space algebra endpoint_fixed_spectrum_interface_check/REVIEW.md. Nominal kappa0=1e-8, J=.030021107107032, E0=2J(1-cos k0), k0=2atan(1/4.510351185997098).

Let g=J-E0>0, R=sqrt(g²+4kappa0²), eigenvalues lambda_minus=(E0+J-R)/2 and lambda_plus=(E0+J+R)/2. In the one-excitation basis choose

 B(theta)=[[lambda_minus+R sin²theta,-R sin theta cos theta],[-R sin theta cos theta,lambda_plus-R sin²theta]].

Then theta0=(1/2)atan(2kappa0/g) in (0,pi/4), R cos(2theta0)=g, R sin(2theta0)=2kappa0. Changing theta to theta_a<=theta0 with nonnegative theta_a changes kappa to R sin(2theta_a)/2 and Delta=R(sin²theta_a-sin²theta0)<=0. This recovers the exact determinant correlation. The full four-state extension leaves vacuum0 and double occupation E0+J fixed, so it is a static local design, not an applied preparation gate.

For r=kappa_a/kappa0 in [1-eta,1], 0<=eta<=1, theta_a=arcsin(r sin(2theta0))/2. On this interval dtheta/dr=sin(2theta0)/(2sqrt(1-r²sin²(2theta0))) <= kappa0/g. Hence

  0<=theta0-theta_a<=eta*kappa0/g.

Also dtheta/dr>=kappa0/R, giving (1-r)kappa0/R<=theta0-theta_a. Thus an eta=1e-6 contract is an absolute angular interval of order4e-13 radians for these nominal parameters. A conservative bound g>.024 (from exact tan-half-angle identities) gives width<4.167e-13. This upper width bound is only an envelope of the allowed interval; it is NOT a sufficient allowable angular-error radius. The exact permissible one-sided angle reduction is [asin(sin(2theta0))-asin((1-eta)sin(2theta0))]/2. A sufficient conservative angle radius is the LOWER width bound eta*kappa0/R. These are sufficient structured contracts, not necessary fabrication lower bounds. No statistical, thermal, digital synthesis or experimental angle model is assumed.

The correlation improves the effect of orientation uncertainty on emitter detuning: |Delta|<=(1-r²)kappa0²/g. It does not eliminate exact eigenvalue supply. If eigenvalues change by epsilon_minus and epsilon_plus at fixed theta_a, the emitter diagonal changes by epsilon_minus cos²theta_a+epsilon_plus sin²theta_a and the endpoint diagonal by epsilon_minus sin²theta_a+epsilon_plus cos²theta_a; positive coupling magnitude kappa changes by (epsilon_plus-epsilon_minus)sin theta_a cos theta_a; the off-diagonal matrix element changes with the opposite sign. In particular a common eigenvalue shift epsilon changes both one-excitation diagonals by epsilon, independent of small theta_a. If vacuum remains0 this is not a removable global phase, and generic eigenvalue errors cannot be covered by orientation-only estimates.

The paired onsite/coupling compensations can therefore be encoded in an isospectral positive block family rather than specified as independent entries. That is an explicit structured supplier contract. It is not a native mechanism for realizing those spectra or maintaining their precision, and should not be advertised as generally robust coefficients. A full-device theorem still has to propagate simultaneous Delta, kappa_a and endpoint shift -Delta into actual mass/profile/complete source/runtime estimates against the fixed nominal target.

No numerical scientific program was run for this assessment. The order-of-magnitude angle statement is supported by the explicit conservative g>.024 bound; it does not rely on floating diagonalization. No W/Git/prompt or physical axiom changes.

Correction provenance: the original assessment is retained unchanged. The selective checker identified the upper-width-versus-sufficient-radius distinction, eta domain, and hopping-sign wording; this qualified version incorporates those corrections. Exact g lower bound: q0>4.5 gives g=J(q0²-3)/(q0²+1)>.03*(17.25/21.25)>.024.
