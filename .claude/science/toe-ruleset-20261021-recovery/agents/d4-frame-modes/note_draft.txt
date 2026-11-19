D4 hinge sum: the frame doublet is the long-root S3 doublet of W(F4); nothing in the register gaps it; it is harmless against measurement, and a metric-only edge reading removes it with linear GR intact

Claim type: bounded_theorem (exact group theory and identities; finite supplied-model numerics; estimates against measurement).
Runner: d4_hinge_sum_frame_doublet_identification_gap_audit_and_metric_reading_removal_2026_10_26 (12/12, 1.3 s, seeded; re-run identical).
Pre-registration: criteria_pre_run.txt (written before any computation).
Builds on: d4-gravity (campaign PR #10100; G4/R2/R4/M1), time-blind D4 events (#10094), main's D4 cone (#9714/#9772/#9774/#9821).

VERDICT (pre-registered rule): PAIR HARMLESS, NOT GAPPED by the register as written.
- Not gapped by (a) the four-derivative hinge terms, (b) the nonlinear hinge sum, or (c) the matter loop.
  CL-3's vacuum standard removes the loop term.
- (d) A metric-only reading of the edge registers REMOVES the pair and keeps linear GR exactly. This is
  the recommended amendment, because (b) shows that keeping the pair is nonlinearly risky.
- beta = 1 is ARGUED, not computed. The pair cannot shift beta by more than l/r ~ 1e-45.

1. Identification
Theorems [T], exact on all 1152 elements:
- [T] A1. W(F4) permutes the three orthogonal root 4-frames through a quotient S3 = W(F4)/W(D4_short).
  The kernel has order 192, contains every short-root reflection and no long one.
- [T] A2. The pair is the 2-dimensional irrep of this S3, pulled back to W(F4) (<chi,chi> = 1). It is
  absent from Sym^2 V, so no metric component can carry it; under W(F4), Sym^2 V = 1 + 9. It occurs
  once in Sym^4 V, which is why matter first sees it at (r.p)^4. It also occurs once in
  Sym^2(Sym^2 V), so symmetry allows an h h y vertex.
- [T] A3. The frames are the three nonzero classes of D4/2D4*. The three hole types are the three
  nonzero classes of D4*/D4, and they are permuted by the OTHER S3 (kernel W(D4_long)): that is
  triality. The joint image is S3 x S3 (order 36). The dual rotation D4* -> D4 swaps the two
  quotients, so the pair is "triality's doublet as carried by the root frames".
- FLAG ONLY (no claim): three frames permuted by S3 give singlet + doublet. Any link to three families
  would need a derivation, and none is attempted.

2. Gapping audit
- (a) B1: Q(0) is exactly zero on the doublet (2e-10 relative). The hinge sum gives
  yy = -k^2 (1 - 0.068 k^2), with no constant term. Higher-derivative terms only add k^4, so (a)
  cannot gap the pair.
- (b) B2, nonlinear at k = 0 [F]. Per D4 cell, with the 12 gapped modes relaxed:
  S = 45.28 Sum u^3 + 40.00 (Sum u^2)^2, where u = the frame length changes.
  - The S3 structure is confirmed: the quartic ratio is 9 and the cubic vanishes on (1,-1,0).
  - The doublet carries linear curvature (deficits 5.66 per unit) but has no quadratic action.
  - So the flat point is an INFLECTION, not a modulus.
  - With the d4-gravity sign reading (I = -Sum A delta / 8 pi G; the tensor and the doublet are both
    healthy), the static energy has a cubic term and a negative quartic.
  - B3: a uniform traceless lattice strain t lifts exactly the doublet, at order t^2, and the lift is
    tachyonic (m^2 = -(5.5, 15.8) t^2). Isotropic strain keeps it massless.
  - Caveat: the Euclidean hinge sum is indefinite (the gapped eigenvalues have both signs), so the
    sign of the energy is a supplied reading. A Lorentzian check is OPEN. Whether lattice strain is
    physical is the vertex-gauge question, also OPEN.
  - Conclusion: (b) does not gap the pair, and it flags a possible nonlinear instability.
- (c) C1, one-loop vacuum energy. Supplied per-edge readings w = (V/V0)^q l^-s, with (q,s) fixed by
  two-derivative covariance: scalar (2,6), fermion hop (3/2,3).
  - Scalar: M = -0.594 per unit 4-volume (tachyonic).
  - Wilson-type Dirac: M = +5.148 (gapping).
  - Either way m^2 = 8 pi G M/4, i.e. Planck scale, with a species-dependent sign.
  - CL-3's vacuum standard ("respond only to departures from the vacuum of the same edges") removes
    this same-edge vacuum term exactly. So as written the loop does not gap the pair, and the
    vacuum standard is load-bearing here.
- (d) D1, records/metric-only reading.
  - [T] The doublet is exactly orthogonal to every metric reading: Sum_r a_g (r^T h r) = 4 tr h Sum a_g = 0.
  - [F] The RAW metric block (nothing integrated out) is already 2.0000 x linearised sqrt(g) R
    (resid 5e-5).
  - At second order the doublet reads only as volume.
  - Records that register only order and count (the metric) therefore cannot read the pair.
    Restricting the edge registers to metric-read lengths deletes it, together with the 12 gapped
    modes, and keeps G4/R1/N1-N3 of d4-gravity at linear order.

3. If kept (per-edge reading): couplings and observables (estimates)
- E1 [T]: Sum_frame (r.p)^4 = 4 Sum p^4 + 24 P_g, so the vertex is (s/6) Sum a_g P_g. Rest matter
  (p = E t) charges the frame that holds the tick root: P_traceless = E^4 (2,-1,-1)/12.
- Fifth force: alpha = s^2 (l E1)^2 (l E2)^2 / 6912 relative to gravity. It is composition-dependent
  and has infinite range. For nucleons, alpha = 4.6e-76, against Eot-Wash 1e-3 at 50 um and
  MICROSCOPE eta 1e-15: passes by about 60 orders.
- Extra GW polarisation power relative to the tensor: 6e-80 from mixing at 100 Hz, 9e-76 from matter.
  LIGO/Virgo polarisation tests pass.
- Delta N_eff:
  - 0 if the pair was never thermalised (its couplings are below gravitational strength);
  - 0.054 if it was thermalised at the Planck scale (comparator g* = 106.75), against < ~0.17-0.3.
    A CMB-S4-class target.
- PPN: gamma is untouched. The pair enters g_tt only at O(U^3) or through the O(k^3) mixing, so
  |beta - 1|_pair <~ l/r = 8e-46 at 1 AU.

4. beta (metric sector): ARGUED, not computed. The linear D4 block equals linearised sqrt(g) R
   (d4-gravity R1, and D1 here even raw). The D4 cone is a fat complex, so Regge -> EH convergence
   (Cheeger-Mueller-Schrader; supplied literature theorem) fixes the cubic vertex. Hence beta = 1 + O(a^2/r^2).
   A numerical nonlinear static solve (with the gapped modes relaxed) is OPEN.

Proposed CL amendment (working, not adopted)
"Edge registers enter the hinge sum and the matter odds only through the metric their records read
(order and count); the hinge sum is taken on metric-read lengths of the coned D4 cells."
- It removes the frame doublet, the 12 gapped modes, the inflection and the strain tachyon.
- Linear GR is unchanged (raw block = 2 x sqrt(g) R).
- Untested: whether the graviton birefringence of R5 survives the metric-only reading.

Smuggling gate
- No measured number chosen. g* is used only as a comparator in an estimate.
- No observed structure named. "Metric" is the reading already supplied in d4-gravity, not a new import.
- Prediction: none it was built for, apart from removing the pair. The birefringence carry-over is
  UNTESTED, so the amendment is marked UNTESTED.
- Bent clause: d4-gravity's "every edge responding" (CL-3 response variables). Axioms unchanged.
- Gate: PASS as UNTESTED.

Supplied: the coning centres; the per-edge readings (q,s) and the Wilson fermion kernel (C1); the
Euclidean sign reading (B2/B3); the identification l = sqrt2 x 8.1e-35 m; and CMS for beta.
