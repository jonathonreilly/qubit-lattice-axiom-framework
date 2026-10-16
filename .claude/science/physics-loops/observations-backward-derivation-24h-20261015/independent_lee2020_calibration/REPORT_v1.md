# Focused independent calibration and kernel check

No error was found in the checked force/energy signs, real Fourier factor,
cylindrical kernel normalization or finite-thickness wedge coefficient under
the stated model. The supplied six-sphere parameters do **not** reproduce the
published nominal calibration or all printed single-parameter uncertainties.
Those differences were independently obtained and preserved without retuning.
They do not establish an anomalous force, a measurement of G or a scalar-theory
constraint. This is a focused mathematical/source check, with no formal audit
status.

The source note is `LEE2020_CALIBRATION_DERIVATION_v1.md`, SHA256
`f4d4e11a139c3ffa18ead244778a9f14b5f4ddde0f2ebb283463578d65832b04`.
The input SHA256 is
`d237e334664e5b97ee7759432e842e60ad14acff20c852d3148a47e75786d0ec`,
and the primary runner SHA256 is
`939fa019d95dad301ac96b2839e914cd385ccea6b9396febd1a11f42d37bd341`.
The complete note, inputs and plan were read first. Independent derivation,
fixtures, implementation and actual outputs were frozen before opening any
author calibration runner or result. `PRE_CODE_FREEZE_v1.json` and
`INDEPENDENT_OUTPUT_FREEZE_v1.json` bind that sequence; the latter has SHA256
`a44796c278d5a5b3918307f6a32a5a450f996957c49e0000494e7aa9debd2f7e`.
Lossless source snapshots and final hashes include the subsequently inspected
author runner, receipts and discrepancy note. The supplied thesis transcription
is an input to this check; the PDF was not independently reread.

The independent route and actual evidence are as follows:

- Cartesian pair forces agree with complex-step derivatives of the separate
  energy implementation. Writing alpha for inner rotation and phi for outer
  rotation, `N_inner=-U_alpha`; centered axes give `N_inner=+U_phi`.
  Off axis, `N_inner-U_phi=(delta cross total F_inner)_z`, which was checked
  explicitly. The different-center torques need not be opposite.
- Adaptive integration and FFT grids 48, 96 and 192 agree on the third
  harmonic. The real amplitude is `2|c_3|`, and its signed sine coefficient
  is `-2 Im(c_3)`. Independent small-radius sequences approach `135/8` with
  quadratic relative remainder. Torque and `A3/G` have units of energy and
  kg squared per meter, respectively.
- The Fourier-space Green derivation, axial integral and source jump give
  `(Delta-mu^2)g=-4pi delta3`. Nine additional angular/Bessel point-harmonic
  comparisons use distinct fixtures from the author. For ordinary mass density,
  the energy coefficient is `-G`, without another `1/(4pi)`.
- Angular pattern coefficients, both signs of Fourier order and the two
  vertical integrals give the stated `-8/l^2` and `q^-3` wedge coefficient.
  The formula concerns nonzero `n=N*l`; the n=0 angular coefficient is
  `2N beta`, not zero. An independent N=3 synthetic fixture was integrated
  directly over all six volume coordinates of all nine wedge pairs. Gauss
  orders 4, 6 and 8 converge to the Bessel result, with separate phase and
  radial refinements. The finest cosine-energy coefficient is
  `-9.837979184129957e-6`, versus `-9.837979184103426e-6` spectrally, a relative
  difference of `2.70e-12`. Wrong `1/(4pi)` and single-Fourier-order expressions
  fail the comparison. These are floating diagnostics, not rigorous enclosures.

The independent published-model diagnostics are:

| Quantity | Supplied-model calculation | Published input |
| --- | ---: | ---: |
| Nominal torque, fNm, labeled G=6.6742e-11 candidate | 2.102067456 | 2.1094 |
| Radial correction, fNm, offset along x | +0.004713816 | +0.00475 table; +0.0042 prose |
| Vertical correction, fNm | -0.002724124 | -0.0027 |
| Inner-mass coherent parameter sigma, fNm | 0.000436485 | 0.000209 |
| Outer-mass coherent parameter sigma, fNm | 0.002589209 | 0.00125 |
| Inner-radius coherent parameter sigma, fNm | 0.004218488 | 0.00271 |
| Outer-radius coherent parameter sigma, fNm | 0.002652639 | 0.00333 |

The nominal deficit is `0.007332544 fNm`, or `0.347613%` of the published
nominal value. `G_consistency=6.697481301799359e-11` reconstructs a coupling
from a *calculated* calibration target, so it is not independent information
about G. The literal positive exponent is retained and predicts
`2.102067456e22 fNm`; it was never silently replaced. Radius sensitivities were
analytically differentiated and checked by complex step. They agree with the
author's separate finite differences. The coherent shared-parameter changes
do not reconstruct a sphere-by-sphere covariance or averaging convention.
Reported-torque arithmetic gives gamma `1.0119820033`; treating its supplied
errors as independent gives sigma `0.0047567651`. Independence is a conditional
calculation, not an established experimental fact. The cause or significance
of the nominal/sensitivity discrepancies remains unresolved.

The independent run passed **85 controls**, including two source-binding
checks, in **1.439 s**. After freezing it, the unmodified author runner passed
**62 controls** in **1.713 s**. Its 13,816 stdout bytes exactly match the original
receipt, SHA256
`566ea4bde7a09ddacf5df921c7f7212923c26929481bf02fd07fd675aca07244`.
Both runs used Python 3.12.8, `-B`, `PYTHONDONTWRITEBYTECODE=1` and an external
120 s subprocess timeout. Complete stdout/stderr, timings, CPU/memory cost,
commands and source hashes are retained. No checker failed or timed out;
the calibration mismatch is a scientific reproduction limitation, not a
failed numerical identity. Inputs stayed unchanged throughout.

The next obligation is to reconcile the original calibration model, primitive
metrology, averaging/covariance and component corrections before claiming a
faithful apparatus calibration. Disjoint spherical-body modeling, actual
alignment/tilt/coatings, density contrasts, complex phase conventions,
transfer corrections and their covariance remain measurement assumptions.
Applying this kernel to the scalar action additionally requires the physical
source and calibration responses, environmental mapping and relation between
G_N and G_T. None is supplied by the successful kernel checks. No torque-row
fit, empirical holdout, physical exclusion, scalar potential or absolute scalar
normalization was established.
