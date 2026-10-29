# Numerical criteria before independent implementation

Frozen target SHA256:
`c85ce075fdae1249b520089a462c8cf3107c0b26901d4dcd55a78c48b78ebc8b`.
Source aggregate diagnostic values were seen; author scientific code and raw
evidence have not been opened. All failures and substitutions will be kept.
These criteria do not certify the theorem's conservative t0.

1. SU(3) Fourier-determinant normalizer at identity, t=32,64,128, using 60
   decimal digits and winding cutoffs 48 and 64: relative cutoff discrepancy
   below 1e-25. With the analytic prefactor `27 sqrt(3)/pi`, require
   `abs(t E_t+1)<0.15` at each sample and decreasing discrepancy as t grows.
   An intentional leading-power substitution t^-3/2 must violate the 0.15
   criterion. No cutoff or tolerance changes after observing these results.
2. The same representation at t=128, S=1 and lambda=0, with a symmetric
   difference using lambda=+/-1e-5 and at +/-5e-6, must give second derivative
   estimates agreeing within 1e-6. Require
   `abs(t partial_lambda^2 E_t+10/3)<0.25`. Replacing lambda by zero in the
   normalizer must violate this criterion. This probes a parameter derivative
   on the fixed small domain, not an independently larger algebra-only chart.
3. Exact rational bivariate Gaussian moments of the SU(3) leading Weyl
   polynomial must give 324; the ratio of its weighted fourth-trace moment
   is 360 and weighted squared third-trace moment is 1080. These constants
   were analytically derived before the script. They separately check the
   full-dimension prefactor and the Haar/quartic/cubic coefficients.
4. Independently enumerate the actual paired S4-prime words for L=3,T=2.
   Require exactly `24 L^4` labels per coarse link, endpoint displacement
   `L e_mu`, maximum length `5L-4`, no support outside the lifted brick,
   and at most `8L^4` distinct positive reader links. Compute the reader
   incidence across all coarse labels and require maximum at most eight.
   At arbitrary noncommuting SU(2) coarse holonomy, evaluate all baseline
   words for one wrapping coarse link and require maximum HS error below
   1e-12 from its coarse link. Do not replace paired endpoint orders.
5. Before every numerical child: native free-memory percentage at least50,
   one-minute load below20, active coordinator lock, library threads1,
   nice>=10. Each child has a60-second wall cap and resident-memory watchdog
   strictly below2GiB; preserve raw stdout/stderr, resource failure, timeout
   or nonzero exit. A resource failure is no scientific result.

No numerical tests are needed for purely analytic source-domain bookkeeping.
