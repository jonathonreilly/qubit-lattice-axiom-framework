# First thermal execution: results and scope

Parent /root personally wrote and executed the coupled background model.
The immutable first execution completed 13573 computational checks with zero
failures, eight finite-mass electron histories, eight massless controls and
four preselected refinement/scale histories. These counts are not observations.
The expanding Einstein branch is supplied explicitly; positive H squared by
itself would not select it. All integrations reached T=0.01 m_e.

For 101 predeclared logarithmic temperature samples per history:

| k at initial vacuum normalization | fluid coupling | minimum H_J/H_GR | maximum H_J/H_GR | final u |
|---:|---|---:|---:|---:|
| 0.01 | equal | 1.09687423037 | 1.11467484048 | 0.139391936 |
| 0.01 | split | 0.999805330212 | 1.0001738823 | 0.00169503889 |
| 0.001 | equal | 1.09867742661 | 1.11769852823 | 0.146763338 |
| 0.001 | split | 0.999979379458 | 1.00001864885 | -0.00285088703 |
| 1e-05 | equal | 1.09886284146 | 1.11803063464 | 0.14764252 |
| 1e-05 | split | 0.999999792467 | 1.00000018788 | -0.00334618331 |
| 1e-06 | equal | 1.09886451455 | 1.11803365334 | 0.147650579 |
| 1e-06 | split | 0.999999979246 | 1.00000001879 | -0.00335068213 |

Equal means b=a; split means the separately calibrated b=k. All parameters
remain fixed during evolution. The positive electron trace drives u away
from zero; the ideal radiation tracking history is not imposed. The above
are sampled extrema, not certified continuous extrema. The reference uses
the same physical densities, the supplied H_v and the initial local G_N.

Refining from 128 to 256 quadrature nodes and tightening Radau tolerance
changes the sampled expansion ratio by at most 7.26e-12 for the preselected
k=.001 equal case and 1.12e-15 for k=1e-5 split. The largest absolute plasma
log-entropy invariant residual among the eight base runs is 6.11e-10. The
finite-initial-temperature neutrino/photon endpoint is about .71393016905;
the difference from (4/11)^(1/3) follows from starting fully decoupled at
T=10 m_e, and is not a noninstantaneous transport prediction.

The first execution emitted a real SciPy finite-difference Jacobian scaling
overflow warning. Its complete stderr is preserved, SHA256
8f3602474bd26b7f57b6113d6d1d8901b03af8e229b313afef66b0845b02bec0.
It did not abort or produce a failed endpoint. The k=1e-6 equal case used
208763 function evaluations and 5403 Jacobian evaluations. This stiffness
and warning remain part of the result; the two refinement checks do not
establish convergence for every other case. An independent implementation
check is active. No unchanged positive execution is rerun to hide warnings.

This imports an equilibrium photon/electron gas, initially decoupled massless
neutrinos, electron mass units, zero chemical potentials, flat homogeneous
expansion and supplied normalization Rstar=1e30. It omits baryons, weak and
nuclear reactions, neutrino collisions, QED corrections and perturbations.
No light-element abundance is calculated or tested; no BBN/CMB likelihood
is claimed. The near-reference branch follows a calibrated b and has not
predicted that parameter. The chosen initial scalar state is unselected.

The full handwritten argument was independently checked (62 controls),
and the parent read the complete proof and verified all 17 source identities.
That mathematical check does not yet cover this implementation. All first-run
source, fixtures, input freeze, raw outputs and per-history samples remain
under evidence_v1.
