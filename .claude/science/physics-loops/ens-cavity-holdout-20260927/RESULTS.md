# ENS result: separately calibrated junction shape improves withheld spectra

Exploratory supplied-model result, 2026-09-27. No native TOE derivation or unique identification of a microscopic mechanism. The one-transparency Andreev family is a physically motivated restriction; a distribution of transparencies or circuit inductance can yield different shapes.

Frozen protocol: fit f01,f02 and cavity lines with transmon states0,1,2; evaluate f03..f06 and remaining cavity lines. Three declared starts were attempted. The .2 start converged to an exact five-input solution; .01 and .6 reached the evaluation limit with nonzero calibration residuals. The selected solution minimizes calibration cost only. Existence of this solution does not prove uniqueness.

Parameters in GHz except tau: EC=.1841990760792327, EJ1=21.829772186093592, Omega=7.738912856323958, G=.18858878602560333, tau=.15464897201354028. Calibration residuals below8e-14GHz. The derived second harmonic is +.0104917249 EJ1 cos(2phi); the third is −.00022017684 EJ1 cos(3phi). No higher harmonic or evaluation target was fitted independently.

Signed prediction-minus-measurement drive errors (MHz):

| unused drive | cosine, four calibrations | Andreev shape, five calibrations |
|---|---:|---:|
| f03/3 | +.796329 | −.218231 |
| f04/4 | +2.898695 | −.389980 |
| f05/5 | +6.238759 | −.951250 |
| f06/6 | +11.008222 | −2.323107 |

Unused cavity fres4..7 errors are −.019387,+.033543,−.546382,−.789351MHz at the primary cutoff. The cosine fres3 error +.112512MHz is NOT comparable as a withheld datum after the Andreev model uses it in calibration. The higher-transition improvement comes with one additional physical observation and one additional parameter; it is not a parameter-free prediction.

Primary-to-fine cutoff change is at most .00003721MHz for the Andreev family. Independently reconstructed direct charge⊗photon matrices reproduce the frequencies; final frozen report INDEPENDENT_NUMERIC_REVIEW.md is complete and read fully. It uses independent binomial Fourier coefficients and a direct charge-photon basis; primary fine predictions agree within .001Hz. Its scope excludes the later sensitivity controls, which remain author checks. Both endpoint assignments have14 unique labels, minimum overlap about.91548. Small cutoff differences support numerical stability, not interval error certification.

Conditioning matters. The scaled calibration Jacobian has singular values about13.75,5.286,.05175,.007512,.00006786. Fifth-line perturbations of±1kHz alter the f06 drive residual by approximately±.123MHz;±10kHz gives residuals −3.562 and−1.094MHz. No adjustment was selected to improve an evaluation target.

All32 printed-decimal half-unit calibration corners converged. The four higher-drive residual ranges are [−.444,.007],[−1.043,.258],[−2.334,.415],[−4.874,.182]MHz. Separate16-corner cosine controls give [.743,.850],[2.813,2.984],[6.116,6.361],[10.842,11.174]MHz. Thus the correction is closer for these tested corners. These are finite rounding controls, not experimental uncertainty estimates, Gaussian confidence intervals or a proven continuous envelope. Actual covariance and systematic errors are unavailable in the inspected sources.

Charge convention remains exposed. The benchmark averages ng0 andng.5. Lescanne2019 observes parity pairs and drifting background charge, not a fixed endpoint pair. Evaluating paired offsets(ng,ng+.5) at ng=.125,.25 changes the f06 paired-center drive by at most .0032MHz in this sample, but the highest cavity center by as much as .929MHz. Its endpoint halfspread is1.036MHz. Therefore fres7 mean residual is not a robust precision comparison under unknown offset. Do not equate parity averaging with an arithmetic average of extreme charge endpoints without additional conditions.

Preparation and readout: level k is prepared with k-photon pulses at f0k/k; Ramsey detuning establishes transition index; state-dependent cavity spectroscopy supplies the independent calibration/evaluation observables. Our fifth calibration only requires preparing level2, whose f02 is already in calibration. Supplied dynamics retain counterrotating capacitive coupling; dissipation/finite-drive line shifts are not modelled here.

Conclusion scope: a reproducible improvement of retrospectively withheld measured observables under an explicit imported model and an additional independent calibration observable. Three nominal drive errors fall below the declared1MHz comparison scale, but that scale is not established as the ENS measurement uncertainty, and the highest line still misses. This is a useful empirical bridge exercise, not evidence that the TOE framework derives the observed correction. Next obligations are source uncertainty/offset characterization, independent final-source report, and a coherent milestone decision rather than additional fit parameters.
