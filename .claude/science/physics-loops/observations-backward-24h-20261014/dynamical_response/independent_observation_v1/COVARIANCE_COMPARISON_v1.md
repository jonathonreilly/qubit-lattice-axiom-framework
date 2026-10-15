# Equal-time covariance lift: independent result and source comparison

The proposed lift is correct on its stated ideal-input domain. Adding C_SS and its total derivative permits elimination of the separate mixed time-leg derivative without a common-transfer premise. Five independent rows give a unique linear lift, with two nonlinear compatibility conditions required before recovering physical x,y,R. This is a sufficient construction, not a minimum-data theorem or a claim that these inputs are already measured.

I completed and froze `COVARIANCE_DERIVATION_v1.md` and its 39 exact symbolic controls before reading the author's new note. Freeze SHA256 is `fc15a3b9481705981dedb11d0f7f7861bab81c4b6217ed86ece39896f7d132fa`. I then read the complete `COVARIANCE_LIFT_v1.md`, SHA256 `3af34348187408767f12cd604f969f3b22475a4aa493622b8c66843c2ce28e18`, and preserved its exact bytes.

My independent derivation writes S′−yV′=−alpha S−gamma V, with alpha=1+(x−y)/2 and gamma=JR+hy. The author uses a=−alpha and c=−gamma. Both yield the same eliminated total-covariance equation. In particular, the author's row

    [A/2, -A/2-B′+(h-1)B, C′/2+B/2-hC, B, -C]

with z=(x,y,y^2,JR−xy/2,JRy) equals the independent elimination exactly. A,B,C denote C_SS,C_SV,C_VV. The stated monomial checks z3=z2^2 and z5=(z4+z1 z2/2)z2 are essential and correct. The equations recover R=(z4+xy/2)/J and q=x/y only on the stated positive, nonzero-denominator chart.

Multiplying by S−yV at one epoch is legitimate with y held as the common coefficient. It must not be mistaken for differentiating the power of a time-varying combination S−y(N)V, which would introduce y′ terms. The source explicitly distinguishes these operations.

The author's physical-feature row reduction is also exact. Its map from (C_SS,C_SV,C_VV,C_ST,C_VT) to the five row columns has determinant 1/8. The positive-definite covariance cone projects onto an open set of these five entries, so the rank argument is valid. An explicit independent witness strengthens this availability statement: in (S,V,V′), take covariance epsilon^2(tt^T+delta I), delta>0, with t=(r,1,w) for (-1,0), (-2,0), (-3,0), (-1,1), (-2,1). The author's five-row determinant is (1+delta)epsilon^10; my differently parameterized lift has twice that determinant. Both are nonzero for positive delta,epsilon.

These covariances are admissible local initial states: b!=0 maps arbitrary V′ into T and X; phi and dust velocity follow from S,V; rho>0 allows the 00 constraint to determine n with scalar velocity data still free. Bounded ensembles and a small common amplitude make the construction compatible with linear initial perturbations. This does not establish actual cosmological preparation, measured rank, independent survey bands or a full history. No scalar mode or initial covariance was selected by the inverse.

The pre-source independent control result is 39 matched, zero failed. The subsequent affected-source comparison has 16 matched, zero failed, checking row equivalence, every reduced physical-feature column, the lift compatibility/recovery formulas and the invertible change of row basis. These are separate algebraic checks, not an additive scientific score. No author code, author ODE, new observations, external-source acquisition, Git mutation, source edit or formal audit was used for this continuation.

The earlier admission report remains historically correct: P and velocity-power growth alone did not isolate the separate time leg. The larger equal-time covariance collection and the dynamical/full-rank conditions supply information absent from that earlier input set. Current lensing/RSD summaries still do not directly supply the enlarged, unprojected covariance histories and total derivatives. Noise, physical-frame calibration, time/scale windows, derivative errors and conditioning remain explicit downstream measurement obligations. Background/candidate membership and q at turning points remain separate tests.

No correction to the checked author source is required for this narrow algebra/supplier scope. Exact source, independent derivation, control and comparison hashes are bound in `COVARIANCE_IDENTITY_v1.json`; this report is not a formal audit or a canonical-delivery gate.
