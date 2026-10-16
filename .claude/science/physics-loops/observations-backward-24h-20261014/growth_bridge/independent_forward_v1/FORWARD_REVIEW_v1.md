# Focused independent reduced-forward check

Root remains author. This report checks the supplied full homogeneous radial backgrounds coupled to the explicitly reduced r=q perturbation equations. It is not a test of exact full-action perturbations, observed data or physical initial-state selection. I wrote only this directory and made no author-source, runtime, Git or audit changes.

## Independent derivation and exposure chronology

I derived and froze the perturbation equations before reading the forward protocol or author code. `PRECHECK_FREEZE_v1.json` has SHA256 `3e86e6b08e37b4349f24208654432ffae3fc2f91b0d9c06773bfe67a90531b78`. For Phi=-c delta and exact linear dust continuity delta'=W+3Phi', the derivative of Phi is implicit in delta'. Solving gives

    delta'=(W-3c' delta)/(1+3c),
    c'/c=-1-F'/F-q'/(1-q),
    W'=-(2+h)W+rho(1+q)delta/(2FH²), I'=W.

The c derivative uses conserved physical dust and K=k_com/a, so rho'/rho=-3 and (K²)'/K²=-2. In particular the q' term has a minus sign. The integrated identity is delta-delta0=I+3(Phi-Phi0). For W0!=1, the observable primitive must be J=[I+3(Phi-Phi0)]/W0. Dropping either the implicit denominator or this normalization would change the system.

After freezing this oracle, I read the complete author `forward_controls_v2.py` and `FORWARD_PROTOCOL_v1.json`, and copied their results and original serialization-failed version. I then wrote a separate numerical implementation. That implementation is explicitly **post-source-exposure**, following a pre-exposure equation derivation; it is not represented as blind code validation. It imports no author module and does not run the old M12 aggregate.

## Complete source comparison

The author v2 source SHA256 is `f72a91a02850a149bd0d002aadac6647039838cbb1c85e6b8b26a551fddad8fa`; protocol SHA256 is `1a3e541a71573b43b6c7ffc26d8a61680cc75d4f8fa96403f31937cc62edc088`. The reused M12 background helper is exactly the previously reviewed `1bf2d30207b99cea8508a612a739ed8b82dc7d6860920e101fb4e1374eccd9be`. Its identity matches the author's result record; a copy is retained here. The reuse is explicit, not a claim of a new self-contained background derivation in this script.

The background uses Einstein proper time and physical velocity, density and scale factor. Its lapse conversion is correct: dN/dt_E=HE+b*v, H_J=(HE+b*v)/A, where A=sqrt(C). N=ln(A*aE/A0) sets the physical initial scale factor to unity. This makes rho_J=rho0 exp(-3N) and K=K0*H0 exp(-N) consistent. The code uses actual initial Jordan H0, not Hv or Einstein H. The Fpp conversion, F''=(Fddot-Hdot*F')/H², and the analytic q' agree with the independent oracle. Each perturbation N derivative is multiplied by dN/dt_E in the integrated Einstein-time state equation. The cphi derivative and implicit continuity solution are correct.

The inverse receives only generated q,P,What,J. `inverse_rows` has no access to the source case, density contrast, beta, B, Fc or initial density answer. The three fixed calibration epochs determine the quadratic and returned candidate set. Truth is used afterward to evaluate set-membership/recovery diagnostics, and all returned candidates are retained for the three later residual tests. Selecting the closest returned beta for a recovery diagnostic is not used to construct roots or to delete a competing root. All six present fixtures have one admissible returned candidate; this does not establish generic uniqueness, and the earlier manufactured ambiguity remains a separate result.

The generated q is an ideal Euler readout using W'/W and h supplied by the integrated equations. It is not a noisy derivative estimate. Likewise the Weyl readout is synthesized from the supplied gravitational closure, and the metric correction uses its Phi. Those are valid internal forward/inverse checks, but several source identities are algebraically tied to that same closure. They are not independent tests of whether the physical scalar has this slip/range behavior. The order-unity density/velocity initial values are arbitrary mode normalization of linear equations; they do not establish nonlinear perturbation validity or select an actual primordial state.

## Independent six-case implementation

`independent_forward_v1.py` was frozen before its execution in `IMPLEMENTATION_FREEZE_v1.json`. It evolves the same three backgrounds and two modes in dimensionless Einstein time tau=Hv*t_E, with N integrated directly instead of aE. It writes analytic K and potential derivatives without calling the parent's symbolic helper, and uses q_u=-2sqrt(beta)q(1-q/beta). The Weyl readout is assembled directly from separate Phi and Psi. Its inverse forms a polynomial from the equality of two observed slopes, evaluates that polynomial at 0,+1,-1 to recover its coefficients, and uses a stable quadratic formula. It receives only the same three observable calibration rows.

All solver methods, tolerances, sample fractions, interval and recovery thresholds follow the original frozen protocol. The first independent execution reached result serialization and failed on a NumPy boolean. The source and stderr remain unchanged. `SERIALIZATION_FAILURE_v1.json` records the defect; `independent_forward_v2.py` changes only the output filename and JSON conversion. The successful second execution uses the same equations and thresholds. This is an output repair, not a scientific failure being hidden.

The independently generated six systems yield one candidate each. All candidates pass the fixed later-epoch residual test. The maximum independent relative recovery errors are 2.220446049250313e-14 in beta, 9.059419880941277e-14 in B and 1.0669243266647754e-13 in C. The maximum later relative identity residual is 4.747104709584635e-15. The maximum absolute normalized continuity residual is 1.7763568394002505e-15; dust-conservation relative residual is 9.992007221626409e-16; slip absolute residual is 9.71445146547012e-16. These are floating numerical checks without a rigorous integration-error enclosure.

The complete all-row comparison covers 36 sampled rows. Its largest absolute readout differences are 3.9968028886505635e-15 in P, 1.7763568394002505e-15 in q and 9.43689570931383e-16 in N. Maximum relative candidate differences are 5.739853037312059e-14 in beta, 1.3389289676979388e-13 in B and 1.9273471707492718e-13 in C. All six candidate counts and later acceptance decisions agree. The original author result has 60 passing controls and no failing control; these are inspected author controls, not a claim that my separate implementation reran those 60 checks verbatim.

## Retained limits and narrower test scope

The exact continuity control in v2 tests the **absolute** error in normalized delta/W0. Its protocol key is named `integrated_identity_relative_tolerance`, but the computation does not divide that continuity error by a solution magnitude. The later identity test using the same threshold does compute a relative error. The current normalized values are finite and of order unity, and all six cases pass by many orders of magnitude. This report preserves the actual definition instead of silently calling both relative controls. A generic amplitude- or shape-scale claim would need its own declared normalization.

The later-candidate loop checks the algebraic residual but does not itself impose beta>q and J+C>0 at later epochs. The separate positive-chart control uses generating beta. I independently checked every returned candidate at all six saved epochs: all pass the candidate-specific gates, with minimum beta-q about .0534377861, minimum J+C about 1.6666666667 and positive B. `CANDIDATE_DOMAIN_CHECK_v1.json` retains the individual margins. Thus there is no current fixture failure, but this v2 routine should not be described as a generic all-interval admission or positivity certificate. Pole crossings, sign changes, singular calibration and interval-wide uncertainty need explicit treatment for other inputs.

The three backgrounds and two initial wave numbers exercise the proposed conversions but do not bound the error of the supplied light/quasistatic r=q closure. No full-action scalar perturbation, finite-mass transfer, omitted time derivative, nonlinear growth, observation operator, derivative covariance, survey window or actual likelihood is tested. Exact linear dust continuity inside the reduced system does not cure those missing inputs. Higher precision in the quadratic inverse acts on rounded synthetic readouts; it does not create observed precision.

The parent v1/v2 source delta was checked exactly: only output filename and JSON fallback conversion differ. The original partial v1 JSON is invalid as JSON and remains preserved as failed output. My independent v1/v2 delta is likewise output-only. Both failures and their original sources survive. No canonical publication, final cache or newly amended parent source is covered by this report; those require their own narrow final binding if supplied.

`FORWARD_CORRESPONDENCE_RESULTS_v1.json` preserves all comparison maxima and identities. `FORWARD_IDENTITY_v1.json` binds this report, original derivation, author snapshots, reused helper, independent implementations, results and serialization evidence. This is focused computational support only.
