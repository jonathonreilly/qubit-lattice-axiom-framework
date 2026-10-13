# Actual calibration-control gap and separate correction

The independent checker replaced only the new runner's calibration-only
supernova intercept with an all-row mean. All1746 original controls passed,
although the strong-case transfer quadratic changed from833.909399118 to
832.641483300. The original positive formula was correct. Preserve the actual
mutant, fresh source pins, v1 runner/results and all failures.

Version2 adds calibration-only normal equations for each actual returned
intercept, binds each actual transfer prediction to the conditional mean,
and binds the actual predictive covariance to the previously checked exact
processed-data covariance hash. The unchanged thresholds are2e-8 for the
normal equation and2e-11 magnitudes for prediction arithmetic. Its CLI now
returns nonzero when any check fails. No dynamics, candidate parameter,
calibration data selection, original numerical output or old assertion changes.
No observational fit improvement is claimed from validation changes.
