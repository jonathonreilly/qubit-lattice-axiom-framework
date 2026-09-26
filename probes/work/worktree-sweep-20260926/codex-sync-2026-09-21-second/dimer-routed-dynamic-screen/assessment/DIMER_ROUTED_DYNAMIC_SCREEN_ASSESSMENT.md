# Finite-size record-color dynamics: completed screen

2026-09-21. Root finite numerical assessment; no formal audit or retained status.

All 960 declared histories completed with verified output receipts and without
exclusions. At the tested sizes, the color-wave signals have substantial finite
damping. The mean-square error from the conditional Euler propagator decreases
across the four tested sizes, but remains large at N=128. These data neither
establish the limit nor give a contradiction to its asymptotic statement.
No damping law or convergence exponent has been fitted.

## Protocol and measured quantities

The frozen protocol uses N=16,32,64,128 with respectively 256,128,64,32
independent histories for each of two frozen matching fixtures. One fixture
has maximal winding along the first coordinate; the other is generated from
a columnar matching by a fixed number of seeded plaquette proposals. The
second fixture is not claimed to be sampled from a uniform matching law.
The records exchange whole pairs with gamma=1, k0=1.1. Geometry is fixed.
Each history starts with independent uniform fourteen-color keys. This is
a stationary-color test, not an empty-start preparation simulation, and
does not test the new moving-geometry extension.

For each of the three positive fundamental axis modes, let z=(E,B) with
E=sqrt(7)X and B=sqrt(7)Y/2. The exact initial second moment is I_6. The
continuum predictor is U=P_L+cos(theta)P_T+sin(theta)D, where
theta=4 pi t/7, D=[[0,i C_hat],[-i C_hat,0]], and C_hat v=q_hat cross v.
The four recorded statistics are ||z_t-U z_0||^2/6,
Re[(P_T z_0)^dagger z_t]/4, Re[(D z_0)^dagger z_t]/4,
and Re[(P_L z_0)^dagger z_t]/2. Their limit targets are respectively
0, cos(theta), sin(theta), and 1. Both longitudinal components are retained.
There is no division by an observed initial sample variance.

Each independent history is the sampling unit. The plotted values average
the three mode statistics inside that history before averaging histories.
Ten thousand whole-history resamples preserve correlations among all modes,
times and components. Reported intervals are pointwise percentile 95%
intervals, not simultaneous confidence bands or selected hypothesis tests.
All individual modes and component variances are retained in RESULTS.json.

## Quarter-period observations

At t=7/8 the exact limit targets are error 0, transverse autocovariance 0,
signed cross covariance 1, and longitudinal autocovariance 1. The following
entries give mean [pointwise 95% interval].

| N | Geometry | Histories | Propagation error | Signed cross | Longitudinal |
| --- | --- | ---: | --- | --- | --- |
| 16 | irregular | 256 | 1.9245 [1.8731, 1.9772] | 0.0377 [0.0117, 0.0631] | 0.0129 [-0.0225, 0.0491] |
| 16 | winding | 256 | 1.8749 [1.8180, 1.9334] | 0.0754 [0.0502, 0.1005] | 0.0603 [0.0260, 0.0948] |
| 32 | irregular | 128 | 1.6312 [1.5671, 1.6946] | 0.1559 [0.1211, 0.1893] | 0.1565 [0.1084, 0.2077] |
| 32 | winding | 128 | 1.6331 [1.5641, 1.7034] | 0.1803 [0.1464, 0.2144] | 0.2116 [0.1565, 0.2665] |
| 64 | irregular | 64 | 1.1572 [1.0983, 1.2193] | 0.4289 [0.3733, 0.4846] | 0.5009 [0.4122, 0.5970] |
| 64 | winding | 64 | 1.2103 [1.1414, 1.2850] | 0.3949 [0.3356, 0.4552] | 0.3564 [0.2769, 0.4402] |
| 128 | irregular | 32 | 0.7304 [0.6722, 0.7855] | 0.6799 [0.5839, 0.7782] | 0.6980 [0.5567, 0.8456] |
| 128 | winding | 32 | 0.7763 [0.7035, 0.8502] | 0.5455 [0.4871, 0.6030] | 0.5993 [0.4502, 0.7652] |

The signed cross term has the predicted orientation and grows in magnitude
with the tested size at this time. Even at N=128 its intervals remain below
the unit limit target. The propagation error is about 0.73–0.78, so it would
be misleading to describe these runs as a clean undamped-wave demonstration.
The longitudinal modes also lose substantial finite-time correlation.

## Half-period observations at the largest completed size

At t=7/4 the targets are error 0, transverse autocovariance -1, signed cross
covariance 0, and longitudinal autocovariance 1.

| Geometry | Propagation error | Transverse auto | Signed cross | Longitudinal |
| --- | --- | --- | --- | --- |
| irregular | 1.1254 [1.0421, 1.2070] | -0.4605 [-0.5475, -0.3755] | -0.0476 [-0.1127, 0.0163] | 0.4852 [0.3572, 0.6125] |
| winding | 1.2057 [1.0948, 1.3204] | -0.3383 [-0.4031, -0.2747] | -0.0217 [-0.0675, 0.0244] | 0.3625 [0.2389, 0.4919] |

The negative transverse correlations and near-zero signed cross term are
consistent with the predicted half-period phase. Their amplitudes and the
mean-square residual still show strong finite corrections. Unequal sample
counts across sizes are displayed explicitly; the two geometries are not
pooled or treated as independent draws from a geometric equilibrium.

## Verification and limits

The author analyzer authenticated every byte of all 3,840 production payloads
against the saved history receipts, then read every history JSON. It hashed
the binary endpoint states but did not decode them. Exact current, covariance,
Fourier-sign and unitary-propagator controls were frozen before aggregate
access. The complete source and all output identities are bound separately.

The selective independent implementation check reconstructed all contexts,
the generator normalization, two small logged event histories and 16
preselected production endpoints. It reproduced selected initial and final
Fourier fields with maximum complex error 5.651e-14, and checked physical
record identities. It did not replay all production trajectories or inspect
the aggregate analyzer and bootstrap. A separate aggregate check remains
pending at the time of this assessment.

The independent asymptotic theorem check and this finite screen answer
different questions. Neither establishes a physical electromagnetic field,
quantum dynamics, a geometric photon, empirical validity, or a TOE.

A fixed 16-history N=256 follow-up was declared after these N<=128 outcomes
were inspected. Its protocol, source identities, resource limit and hard
campaign deadline are separate. It is not silently appended to the original
screen or presented as an outcome-blind extension. No N=256 result was used
in this assessment.

Analyzer SHA-256: `752ccdd5506c5f7714bb7c97175dde7fc179ba8592a9248df4a8dc00760e283c`.

Aggregate results SHA-256: `08aab30040e7b0c50c60486bf769f7c87247d8771f3f2315d577725fd4d60345`.

Per-history values SHA-256: `433459f27af8320e915c9568bfa8d726d94483c8cf85cffec6b0f20d1fdfcf92`.

Protocol SHA-256: `d8cbfed1ba55a4a11048c7d68135f0ee7f6d0c98c38dc685e43bb43ead90952d`.
