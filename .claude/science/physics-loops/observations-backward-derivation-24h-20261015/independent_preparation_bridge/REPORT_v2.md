# Final focused preparation-bridge check, v2

No material mathematical discrepancy remains within the explicit supplied class and transition premises. The v1 clamp-to-drive continuity ambiguity is resolved by v2; the new sharp annulus noise-cost bound is correct. This is a focused mathematical/code check, not a formal audit, novelty determination, empirical validation or publication authorization.

## Final source binding

- PREPARATION_BRIDGE_v2.md: `ecb67821847f062a6c13632826beb2a37d4f91d7b72eca4aeb823626decb5d77`
- check_preparation_cost_v1.py: `4fc26c28a85da9b7fa1afa1a8016799b76de0fb989d5e6a44b3081efad436e6e`
- PREPARATION_COST_CONTROLS_v1.json: `1ba3fd7381f1214fb5fc65a4e6fcd7270bda1d271c51b75aafcaf03a83e43baf`
- PREPARATION_BRIDGE_CONTROLS_v1.json: `7d27d26071e40460990731a869d99615a3a887ce9799054f74963c89692241c9`

Original v1 note/plan/runner/controls and REPORT_v1.md remain unchanged with their original bindings in frozen_sources.json and final_bindings_v1.json. Complete v2 delta, cost runner and cost controls were read. note_v1_v2.diff preserves the exact delta. Final rehash confirms both generations unchanged.

## Evidence and conclusions

The original complete bridge received an independent pre-code derivation plus a different state-transition/complex-prefix/complex-step-tangent implementation:127 checks passed. Its133author controls reproduced exactly. No unchanged original run was repeated for v2. The narrow addition received an independent dual-polynomial proof and17new checks, including linear-program minimum-L1 solutions for different annuli, six-point equilateral attaining designs, augmented irregular designs, aligned deterministic readout errors and fixed-radius infeasibility. All27new author controls reproduced as exact parsed JSON. All executed computations were bytecode-disabled and bounded by120seconds; receipts and full outputs/stderr are preserved. No computation failed. Scientific negative controls and the kick counterexample are expected results, not execution failures.

The general-k moving and nonstationary tangent equations include the required inertia/coupling gradients. Affine hidden-state evolution for prescribed x implies exact degree-two force dependence on initial state for finite drives. The prefix fundamental f=n c supplies homogeneous linear coordinates because n is nonzero and omega>0. Q u=e0 is the precise feasibility condition for all quadratic output coefficients. Signed weights, the fixed-radius obstruction, lower-rank feasible cases, unmatched plus/minus ensembles and the deterministic feature/readout envelope agree with independent derivation. See derivation_before_code.md and REPORT_v1.md for the full self-contained proof and numerical details.

For equation12 an independent dual polynomial is p(f)=(rmax²+rmin²-2|f|²)/(rmax²-rmin²). It has |p|<=1 on the true annulus and p(0) equal to the proposed lower bound. Moment reproduction yields p(0)=sum u_j p(f_j)<=||u||1. Two isotropic phase ensembles at the boundary radii attain equality. The author's two four-phase circles are valid; independent LP checks used two three-phase circles. Aligned errors epsilon*sign(u_j) attain epsilon||u||1 at one time. The cost is worst-case deterministic amplification, not variance. It assumes0<rmin<rmax and feasible weights; it neither guarantees any given design's feasibility nor certifies uncertain radii. Narrow annuli diverge consistently with the fixed-radius obstruction.

## Transition finding and its significance

V2 explicitly requires a C2 drive with x(0)=x0 and xdot(0)=0 continuously from the clamp, no impulse/hidden kick/unrecorded state change, and the same transition convention for the plus/minus protocol. This is a physical measurement premise, not something interpolated from the moving-force records.

The preserved exact counterexample shows why: for prefix samples a=1,2,3 with weights3,-3,1 and a valid quadratic force R=z+z², the unkicked coordinate z=2a has rest force0. A common unobserved kick gives z=2a+0.3, so synthesis yields39/100 instead. Quadratic closure and reserved-preparation prediction still hold because the unknown translation preserves polynomial degree. Thus the method cannot infer an unrecorded origin shift from interpolation success. The corrected transition premise excludes this example rather than claiming it is automatically detected.

## Remaining boundaries

The model/action class, common inputs, physical force/pole/phase/time calibration, nonzero observable prefix, finite-band certificates and a well-conditioned feasible moment design remain supplied obligations. The frozen plan and actual model/drives/preparation split agree, but no empirical data or historical timing audit was performed. The cost runner reads prior synthetic coordinates/weights as declared. Six-point interpolation is not a class check; reserved preparations catch the specific cubic alteration, not every alternative. Small centered-drive amplitudes amplify synthesis errors; the third-derivative bound is additional. No physical reset, universal initial-state solution, new action derivation or broad novelty claim follows. Commit-only conditional-support scope is consistent with the evidence.
