# Focused physical-port bridge check

PASS within the explicitly adopted coenergy, calibration-transfer and passive hidden-response assumptions. No material mathematical or code/source defect found. This is a focused mathematical/physics-scope check, not experimental validation, a formal audit or proof that an actual actuator realizes the model.

Complete note and intake read; independent derivation_before_code.md written before implementation inspection. Complete runner and published controls then read. Exact binding:

- PHYSICAL_PORT_BRIDGE_v1.md: 17f694e8770bd22190dc9d3e5a589b1dfd37f12f9341369801be8c167e6e815a
- PHYSICAL_PORT_INTAKE_v1.json: 0db561698358d8f5248f58e87807d34838f0968f0e3f83b7bc4ac9e3a05b3d7e
- check_physical_port_bridge_v1.py: 6043347258b23d987b4bbce3dfbc6aee8347cf9df1666c000c34cc4e5486a9c8
- PHYSICAL_PORT_CONTROLS_v1.json: 30fe2cbe48eae60a1ed441ad144c4a89679158010653eb0e9fa5087da4fe1a9a

## Mapping and physical scope

A1 follows by integrating W_I=Lambda from zero current, then differentiating and transforming the force as a covector by 1/k. It is valid for either orientation of a nowhere-zero flux gradient. A2 additionally uses the physical held force balance: electromagnetic force, corrected supports and the candidate conjugate source must refer to the same mechanical port. The note expressly adopts that bridge rather than deriving it. Arbitrary sensor labels are not sufficient. A3 follows by subtracting the current-integrated coenergy at two positions; position-independent linkage offsets cancel, but sampled flux differences do not establish continuum derivatives.

The memoryless C2 coenergy, sign convention, independent voltage/current calibration, one-coordinate constraint, negligible/bounded other motions, actuator independence from the unknown hidden state and moving-to-held transfer are substantive premises. Thermal/hysteretic history, direct actuator-hidden coupling and servo backaction can defeat A2 even if the coordinate algebra is exact. Those are accurately left outside the exact model or assigned additional correction budgets. Current reversal removes the specified even inductive term only under matched actuator state; higher odd terms need not cancel.

B1 is precisely the conjugate-coordinate chain rule, not an interaction derivation. The two false-pass/false-rejection examples are correct. Constant gains transform the apparent multiplier by g_x*g_J, so known positive product preserves the sign while absolute normalization remains open. Nonlinear/setting-dependent readout is not eliminated. The electromagnetic calibration reciprocity is distinct from the unknown candidate's reciprocal-interaction test and must be established independently to avoid circularity.

## Error and finite-edge checks

C1 retains both occurrences of uncertain current in VI-ZI². Its numerator, division and mechanical-product error terms are correct for arbitrary correlated finite complex errors and the stated positive velocity margin. This arithmetic is not a proof of an apparatus phasor model; physical-model discrepancy is separate. The zero-velocity warning is essential: stationary samples cannot use a simultaneous voltage/velocity ratio, and need the separate flux/current calibration and transfer certificate. Exposed 8×0.0005 and 8×0.01 values give 0.4% and 8% first-order arithmetic, not observed uncertainty.

The six-sample weight bound and conservative doubling under centering are valid, including correlated errors. Their epsilon_J must bound the corrected port, not merely bare current noise; recurrence coefficient and timing uncertainties remain additional. D1 follows from zero-difference initial data and no hidden impulses. Passive Green energy gives |g-prime|<=1 and |g(t)|<=t, proving D2 in every damping/frequency regime without a branch choice. It still needs a bound on the physical coupling/forcing discrepancy and gives no relative guarantee near a zero ideal anchor.

At a full undamped period, the symmetric trapezoid is invisible to endpoint displacement by antisymmetry, while the one-edge ramp gives 1/(4pi²)-1/(2pi³)>0. The source correctly states an endpoint comparison, not identity of the entire hidden state or later history. This avoids claiming that symmetric cancellation certifies actuator fidelity.

## Evidence

Independent check.py tests a decreasing nonpolynomial flux chart, work/coenergy differences, exact symbolic edge integrals, 128 deterministic complex-error corners and a sharp centered six-sample error witness. 137 independent assertions passed. Full author JSON reproduced exactly: 28 passing controls, zero failures. All frozen source hashes were rechecked unchanged. Both executions had explicit 120-second bounds; actual commands, timings and successful return codes are in the receipts, with complete stdout/stderr. No independent execution failure or timeout occurred.

Intake records openly distinguish prior-art/design estimates, measured impedance context and access limitations from a candidate dataset. No broad novelty or empirical-validation claim is made. This check did not independently re-read the external PDFs, verify their retrieval hashes or repository/PR inventories; those contextual provenance assertions are outside this algebraic check. No external source value is needed to prove A1–D2. No source files, canonical checkout, PR/git or audit state were modified.
