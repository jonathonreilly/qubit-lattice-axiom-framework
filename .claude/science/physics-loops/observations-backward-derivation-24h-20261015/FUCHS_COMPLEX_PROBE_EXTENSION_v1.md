# Complex probe extension and source-scope clarifications

The primary v1 note restricted w to be real. Its integration-by-parts identity
also holds for complex w by linearity, using bilinear integrals with no
implicit conjugation. For w=p(t) exp[-i kappa(t-t0)],

    w'=(p'-i kappa p) exp[-i kappa(t-t0)],
    w''=(p''-2i kappa p'-kappa^2 p) exp[-i kappa(t-t0)].

Endpoint conditions persist because p=p'=0. No new initial-state premise is
introduced. Modulation can prevent the forcing integral from cancelling;
it is a measurement design choice, not a selected law of nature. All
previous noise, rank and channel-correspondence obligations remain.

Two source qualifications identified during the focused check are made
explicit in FUCHS_RELATIVE_MOTION_AND_WEAK_INVERSE_v2.md. Equation(4) applies
when the calibration force is off; in general solving for g_t subtracts f/m.
Full column rank guarantees uniqueness conditional on exact consistency, or
a unique least-squares estimate; it does not establish model consistency.
The v1 source and its controls remain unchanged.

The post-exposure development extension uses each candidate source's sampled
unwrapped phase and the slope of its affine least-squares fit on every sample
only to set kappa. The phase-fit residual is reported. Windows include kappa=0
and that slope, at the same600,1200,2400second durations. All time samples
remain included; no amplitude cuts or selection by fit quality. Multiple
probes on one window are correlated summaries of the same observations.
