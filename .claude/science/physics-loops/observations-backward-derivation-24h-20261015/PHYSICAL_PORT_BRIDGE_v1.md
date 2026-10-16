# Physical port calibration for the sampled coupling test

Status: exploratory conditional-support; author derivation checked separately from published apparatus evidence. This is a bridge to a mechanical experiment, not a derivation of electrodynamics, quantum measurement, the scalar action or physical scales. The standard electromechanical coenergy identities and Kibble principle are prior art. No new measured dataset or held-out test is used here.

## Observation-led problem and intake

The sampled-coupling inverse in PR9634 consumes a held coordinate and its conjugate force. An arbitrary position-sensor label and an actuator current are not automatically that pair. Published dynamic-force metrology explicitly corrects electrical impedance, moving-assembly inertia and support forces; a nominal current-to-force conversion alone can create an apparent environmental response.

Strait and Chijioke's 2024 two-page paper gives the corrected dynamic expression
F_DUT = (U_meas - I Z) I / v - M a - Xi. It describes a design target of10N and1% over100Hz–10kHz; those targets are not achieved measurements. Its example expects |IZ/U| about8 at500Hz and anticipates an impedance calibration accuracy about0.5e-3. The measured material described is the coil impedance versus frequency and DC resistance, with a fitted temperature proxy. We use these as exposed design/calibration context, not a validation dataset. Source: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957415, read both pages including equations1–2.

Chijioke and Vlajic2018 explicitly distinguish actuator Lorentz force from force transmitted to a target and discuss calibration difficulties near antiresonances. Its design/uncertainty estimates are also context, not candidate tests: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=925140, read both pages. The general Kibble cancellation is established prior art. A separate hysteresis paper's abstract warns that coil-current history can alter the magnet field: https://arxiv.org/abs/1912.06694v2 (abstract only; no result imported).

The exact PDF identities and access limitations are in PHYSICAL_PORT_INTAKE_v1.json. Current main and execution refs remain bbada1fe09b2d10d610560864d86b68c24a59713 and3a4b2c66a1ead7a1c48b4359627e968f681e3c39. The64open-PR head inventory has no change since04:40Z. Distinctive-term repository searches found no adopted port-calibration result. Absence from this search is not a novelty claim.

## Target, assumptions and physical obligations

We seek a test using independently calibrated electrical port quantities that is invariant under a nonlinear visible-coordinate relabeling. The candidate hidden interaction must not be used to calibrate its own force channel.

Adopt, rather than derive, the following separate calibration model:

1. One constrained mechanical coordinate q on an interval; the actuator's other motions and losses have separately bounded effects.
2. A memoryless C2 electromagnetic coenergy W(q,I), with flux linkage Lambda = partial_I W and actuator force F_em = partial_q W. An independently justified Maxwell/Lorentz description or equivalent calibration establishes this relation. Hysteresis, thermal memory and a coupling of this calibration port directly to the unknown hidden state are outside the exact model.
3. A zero-current flux lambda0(q)=Lambda(q,0), C1 with k(q)=lambda0'(q) nowhere zero on the interval. Its sign may be either; zero crossings require a new chart.
4. Open-circuit motion voltage e0=d lambda0/dt, with fixed documented winding/polarity conventions. The sensor label y=h(q) is one-to-one over the sampled interval. The calibration map is reproducible across the candidate measurements.
5. In the sampled experiment, q is truly held at its designated values at all six force-readout times. Static supports and current-independent actuator forces can be absorbed into the visible offset. Residual acceleration, current-dependent force terms, thermal history and servo dynamics require corrections/bounds.
6. The supplied candidate remains tau w''+gamma w'+C w=-b(q), R_hold=u(q)+a(q)w, with tau,C>0 and gamma>=0, common coefficients and no derivative impulses. This port argument does not select that class.

Electrical unit realizations, Maxwell theory and the physical realization are empirical imports, not retired assumptions of the TOE.

## Derivation A: use flux as the visible coordinate

Set x=lambda0(q). Along a zero-current calibration sweep,
x(y2)-x(y1)=integral e0(t) dt.
This is a measured coordinate map up to an additive origin. It does not require knowing the coil geometry, magnetic field or a length-conversion function h inverse separately. It does require the chart, stable actuator and voltage/time calibration.

Write Lambda(q(x),I)=x+h_c(x,I), with h_c(x,0)=0. By integrating the coenergy identity in current,

W(q,I)-W(q,0)=integral_0^I Lambda(q,j) dj.

Divide its q derivative by k(q). The actuator's generalized force conjugate to x is

F_em/k = W_q(q,0)/k + I + c(x,I),
c(x,I)=integral_0^I partial_x h_c(x,j) dj.                 (A1)

The current-independent term joins the visible offset. Thus the corrected port reading J=I+c(x,I), with the chosen force sign, obeys

J(t)=u_bar(x)+a_bar(x)w(t),
a_bar(x)=a(q(x))/k(q(x)),  b_bar(x)=b(q(x)).               (A2)

Here u_bar includes the static support/background correction. Reading bare I is valid only when c is negligible within a separately justified budget. For Lambda=x+L(x)I, c=L'(x)I^2/2. Current reversal cancels this even term at fixed x only when the actuator state and conditions agree; it does not prove absence of hysteresis.

For a constant-bias calibration sweep, the integral of voltage after resistive correction determines Delta Lambda between sensor positions. The exact coenergy-work difference is

Delta W(I)-Delta W(0)
 = integral_0^I [Lambda(q2,j)-Lambda(q1,j)] dj.             (A3)

Position-independent integration constants in Lambda cancel. Finite observations of Delta Lambda do not by themselves bound its x derivative or certify a continuum force correction; a derivative/model-error calibration remains required. EquationA3 is a route to independent work calibration, not permission to infer an arbitrary derivative from a few samples.

## Derivation B: preserve the candidate compatibility test

Within the stipulated candidate class, reciprocity of a common interaction potential with positive hidden inertia multiplier lambda is a(q)=lambda b_q(q), lambda>0. The port transformation gives

a_bar(x)=lambda b_bar_x(x).                               (B1)

This follows by the chain rule, for either sign of k. The interaction action is not supplied in this transformation: the relation can still fail for the unknown candidate. The electromagnetic actuator's independent reciprocity is a separate calibration premise.

The clamped recurrence and same-run baseline cancellation are unchanged because the hidden equation still has common coefficients and the corrected output is affine in w at each fixed x. Centered pulse responses therefore reconstruct relative a_bar and b_bar. Test B1 using x and J, not a raw sensor voltage and an uncorrected actuator reading.

Two exact comparison witnesses show why this matters. On q>=0 let b(q)=q+q^3, and use sensor label y=b(q).

- If a(q)=1, the physical interaction is not reciprocal with any constant lambda. Falsely calling the unchanged force coefficient1 conjugate to y makes b_y=1 and can yield a spurious pass. The properly transformed coefficient is1/(1+3q^2), so the test fails.
- If a(q)=1+3q^2, the physical interaction is reciprocal. Leaving that force unchanged under the same relabeling can yield a spurious rejection. Dividing by dy/dq gives the correct constant coefficient1.

These are explicit examples, not a universal no-go theorem.

Constant gains and origins do not need to be assigned to test shape compatibility. If X=g_x x+X0 and Y=g_J J+Y0 with nonzero constant gains, then a_Y=g_J a_bar and b_X=b_bar_x/g_x. Thus the fitted compatibility factor is lambda_Y=g_x g_J lambda. A known positive gain product preserves its positivity. Setting-dependent gains, nonlinear current response and an unknown sign do not cancel. No absolute action normalization follows.

## Derivation C: finite deterministic calibration/error bounds

For a calibration sweep lasting T with a known absolute voltage-error envelope epsilon_e(t), the flux-difference error is at most integral epsilon_e dt. A uniform epsilon gives epsilon*T. Offset errors accumulate; the arbitrary coordinate origin does not.

A useful finite-complex-number error bound for the published dynamic force formula keeps the repeated current factor. Let N=VI-ZI^2, where V=U_meas, and let errors have moduli eV,eI,eZ,ev,em,ea,eXi. Suppose true |I|<=M_I, |V|<=M_V, |Z|<=M_Z, |N|<=M_N, |v|>=v_min>ev, |m|<=M_m, |a|<=M_a. Then

eN = M_I eV + M_V eI + eV eI
   + M_I^2 eZ + M_Z(2 M_I eI+eI^2)
   + eZ(2 M_I eI+eI^2),

|F_hat-F|
 <= eN/(v_min-ev)
  + M_N ev/[v_min(v_min-ev)]
  + M_m ea + M_a em + em ea + eXi.                         (C1)

Proof: expand N_hat-N exactly, apply the triangle inequality, and use
N_hat/v_hat-N/v = (N_hat-N)/v_hat
                         -N(v_hat-v)/(v_hat v).
This is a deterministic interval bound, not a standard-uncertainty formula. Additional physical-model discrepancy must be added separately.

At v=0 the simultaneous Kibble ratio is undefined. Our stationary clamped force samples cannot be obtained by dividing their instantaneous voltage by their zero velocity. Use the separately established flux/current calibration and its transfer error instead. A physical actuator that cannot transfer its calibration between moving and held modes does not satisfy this bridge.

Using only the2024 paper's anticipated example,8*(0.5e-3)=0.004: impedance uncertainty alone contributes a0.4% first-order relative error to the Lorentz term, before velocity, transmitted-force, calibration-transfer and other errors. Uncorrected1% impedance variation would give8%. These are arithmetic consequences of exposed design values, not newly observed errors or achieved bounds.

If corrected port readings have errors |eta_n|<=epsilon_J, the six-sample extrapolation error is bounded by ||w(s,p)||_1 epsilon_J for known recurrence coefficients, with

w=(-p,s+p,-(1+s),(s+p)/p,-(1+s)/p,1/p).

Centering two such pulse results doubles the conservative uniform bound. PR9634's separate coefficient-error bound must also be included if s,p are uncertain. A small transmitted-force residual does not establish an uncalibrated source map.

## Derivation D: actual finite pulse edges remain an obligation

A physical coordinate transition has duration. Do not replace it with the ideal instantaneous step silently. Compare an actual pulse q(t), equal to baseline x before0 and after Delta, with an ideal plateau y on(0,Delta). Assume the same hidden linear dynamics and no hidden-state impulses. Let g solve g''+Gamma g'+Omega^2 g=0, g(0)=0,g'(0)=1, Gamma>=0,Omega^2>0. The hidden state difference at pulse end is exactly

delta w(Delta)=-(1/tau) integral_0^Delta
       g(Delta-s)[b(q(s))-b(y)] ds.                       (D1)

If the forcing discrepancy is confined to a set S of length ell and bounded by B, the energy identity gives |g'|<=1 and hence |g(t)|<=t. Therefore

|delta w(Delta)| <= B/tau * integral_S (Delta-s) ds
                 <= B Delta ell/tau.                    (D2)

At the final held coordinate the corrected output error is at most
|a_bar(x)| B Delta ell/tau. This bound is independent of a continuous-frequency branch, but it still needs a physical bound on |a_bar|B/tau. The sampled recurrence alone does not provide that bound. A mere nonzero pulse anchor does not certify small relative edge error, especially near full-period cancellation.

Exact undamped example: an ideal unit forcing plateau on[0,1] with Omega=2pi has zero endpoint response. Replace it by a symmetric linear-ramp trapezoid of edge width r=1/4; its forcing is1 on[r,1-r]. The endpoint integral of sin[Omega(1-s)]/Omega against that symmetric profile is also zero, so endpoint-only comparison would miss the profile change. An asymmetric first-edge-only ramp (r=1/4) instead has a nonzero endpoint integral. Both need checking; a symmetric example alone would conceal the failure. This degeneracy is a concrete comparison, not a universal impossibility result.

## Separation and next experimental route

Calibration: establish the port mapping and sign, x chart, impedance/current correction, inertial/support effects, temperature/history reproducibility, timing and residual envelopes using references independent of the candidate hidden coupling. Do not fit those corrections to make B1 pass.

Development: choose the candidate mode order and common recurrence from designated exposed histories; explore whether finite edges and source backaction fit a justified error budget. The KDFR publications are already exposed.

Reserved tests: freeze the calibration and candidate region, then compare new pulse endpoints, durations, traversal directions, environmental states and independent force/work readouts. No such raw test dataset was accessed in this block.

The port construction replaces a separately supplied mechanical coordinate-conversion function by a measured electromagnetic flux coordinate under an explicitly adopted and independently testable calibration theory. It does not eliminate actuator reciprocity, common dynamics, finite-edge bounds, physical source separation or absolute units. Before a new canonical PR, the useful next step is a finite-edge protocol that can be evaluated in one actual instrument, not another relabeling of coenergy prior art.

