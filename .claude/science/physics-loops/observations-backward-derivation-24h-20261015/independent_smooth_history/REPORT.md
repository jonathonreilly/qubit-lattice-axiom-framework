# Focused independent smooth-history check

No material mathematical or implementation defect found within the explicitly conditional scope. This is an independent mathematical/code check, not an empirical validation or formal audit.

Complete note was read and `derivation_before_code.md` saved before author implementation inspection. The complete runner and control output were then read. Frozen source SHA-256 values:

- SMOOTH_HISTORY_BRIDGE_v1.md: `cd443c52c1fe9a5cb9ccd7d517bd689a969b839fdb0a942272449ea9deaefcd5`
- check_smooth_history_bridge_v1.py: `570e2af0084a638cb0cd46facef78d30243a4a232f8f49bb3297c028978e6cab`
- SMOOTH_HISTORY_CONTROLS_v1.json: `a1dd8ed6d554f17e02ba308ca13a4e6168265ae47c166e1fdfea93dda6c73159`

Final rehash confirmed all unchanged. Exact command, elapsed time, return code and 120-second bounds are in execution_receipts.json. Independent check.py passed 112 assertions; independent_stdout.json preserves every result. Author reproduction passed 24 controls and parsed JSON equals the frozen published controls exactly. Full stdout/stderr and comparison are retained. There were no failed runs in this check.

The three-sample offset removes arbitrary homogeneous preparation without reset when its calibrated recurrence denominator is nonzero. The coefficient-error envelope includes mixed sample/coefficient perturbations. Independent examples cover critical, overdamped and oscillatory modes and 100 deterministic corner-error cases. A full undamped-period alias remains singular, correctly excluded.

Independent differentiation verifies H=a_r(w+b/C), the source K(B''+Gamma B'), weak feature signs and essential L=Gamma K constraint. The reciprocity condition gives K*kappa=a_r^2/(lambda*C)>0. An extra derivative forcing changes L independently and is not a compatible common-action fit. Rank four only identifies the unconstrained four coefficients on those chosen rows; the constraint and calibrated recurrence agreement are additional requirements.

The quotient and frozen-coefficient residual envelopes hold under the stated true-function margins; signed A cases were checked. They do not automatically cover uncertainty in fitted coefficients, timing, numerical quadrature or continuum calibration. The division-free adjoints are correct. An independently manufactured exact history with arbitrary homogeneous modes, A=t-1/2 and nonzero crossing passed an exact integrated identity, supplementing the author's symbolic checks. An identically zero coupling interval remains blind. Smoothness and calibrated time derivatives of A remain required.

Physical premises are explicit: corrected interaction force R=J-N, independently known moving inertial/dissipative and electrical corrections, signed source/readout/coordinate calibration, and supplied classical hidden dynamics. The variable-mass term M' xdot^2/2 is correct. Held-clamp identification alone does not establish these moving-history or continuum assumptions. Neither weak compatibility nor synthetic controls derive a physical action or prove uniqueness against arbitrary alternatives.

Implementation separation is faithful: three named development trajectories with arbitrary initial states fit coefficients; two distinct reserved trajectory shapes and windows evaluate frozen coefficients. These are synthetic reserved checks, not empirical holdout validation. The omitted-load and derivative-forcing alternatives are genuine incompatibility controls; no threshold scanning or empirical claim was found. Finite weak-test blindness is expressly retained.
