# Independent ENS numerical review

**Disposition:** the frozen successful five-parameter model's predictions are independently reproduced. No consequential harmonic-normalization, Hamiltonian, conditional-cavity indexing, or calibration/evaluation separation defect was found in the reviewed files. This is a retrospective conditional imported-model comparison; neither numerical agreement nor the fitted transparency identifies a physical mechanism or native TOE prediction.

## Independent construction

The frozen tau=.2-start solution is

    EC=0.1841990760792327, EJ1=21.829772186093592,
    Omega=7.738912856323958, G=0.18858878602560333,
    tau=0.15464897201354028.

I constructed the raw potential −sqrt(1−tau sin²(phi/2)) independently. Writing it as −sqrt(1−tau/2)sqrt(1+rho cos(phi)), rho=tau/(2−tau), its Fourier coefficients follow from a binomial expansion and exact integer coefficients of powers of cosine. At the frozen rho≈0.084, 140 terms make series truncation negligible at double precision. The coefficient of cos(phi) is explicitly normalized to −EJ1; the irrelevant constant is discarded. No author FFT coefficients or bare-transmon effective Hamiltonian are imported.

The author's alternative stable numerator 4s/(1+sqrt(1−tau s)) equals 4(1−sqrt(1−tau s))/tau. Its normalization by −2c1 correctly makes the complex first Fourier coefficient −1/2, hence the real cosine coefficient −1. The tau=0 limit is also correct. The difference between this form and the raw square root is only a positive scale and a scalar after normalization.

The full independent Hamiltonian is assembled directly in charge⊗photon space, retaining G n(a+a†) without rotating-wave or transmon-subspace truncations. Bare transmon eigenvectors enter only to assign dressed states. All photon and charge units are GHz, with no extra 2pi factors. Outputs fres1…fres7 are the photon0→1 energy differences conditional on physical transmon levels0…6.

An earlier quadrature construction of the raw Fourier coefficients hit roundoff warnings at requested tolerances near machine precision. Those logs/results are retained. Replacing it with the independent binomial construction removes the warning, and the two constructions agree in final frequencies within 0.00012 Hz. No analytic error certificate is inferred from that numerical agreement.

## Reproduced held-out residuals

The following use the declared arithmetic mean of ng=0 and ng=0.5 endpoint transition frequencies. Qubit rows are drive-frequency errors (total-frequency difference divided by j); cavity rows are direct frequency errors.

| Held-out quantity | Independent model minus measured, MHz |
|---|---:|
| f03/3 | −0.218230944 |
| f04/4 | −0.389980321 |
| f05/5 | −0.951250359 |
| f06/6 | −2.323108226 |
| fres4 | −0.019386599 |
| fres5 | +0.033543117 |
| fres6 | −0.546384726 |
| fres7 | −0.789388136 |

All five calibration coordinates are independently reproduced to much better than 1 Hz. Direct cutoffs (N,K)=(16,9),(20,12),(28,18), meaning 2N+1 charges and K photon states, change every averaged frequency by less than 0.001 Hz. The finest direct Hamiltonian has dimension1026. The original primary truncation differs by at most37.210 Hz at fres7; its finer N20,M18,K12 output agrees with the direct calculation within0.001 Hz. These differences cannot explain the MHz-scale point residuals.

Across all cutoff and coupling checks, eigenpair residual norms are below0.001 Hz. Fourteen bare-product labels are unique and agree with a one-to-one overlap assignment. Their minimum dominant squared overlap is about0.915476; the largest runner-up is below0.051268. At both charge endpoints, eleven coupling values from zero to fitted G also give agreement between consecutive-eigenvector overlap tracking and bare-state labels. This is sampled continuation, not a proof excluding every intermediate crossing.

## Separation and numerical interpretation

The calibration source converts only f01,f02,fres1,fres2,fres3 from the ENS row. Its objective and fixed starting guesses do not use held-out cells. The baseline converts only the first four of those inputs. Evaluation selects the smallest calibration cost from the saved solutions; for these files that is the successful tau=.2-start solution. Its prediction parameters were already fixed by calibration.json before evaluation. Evaluation then reads the remaining values and applies the correct qubit divisors/cavity indexing. The CSV, protocol and calibration hashes recorded in the author outputs match the inspected inputs.

The other two starts terminate at the iteration limit with nonzero residuals. They are unsuccessful searches, not certified alternative exact roots. This review verifies the successful root's forward map; it does not prove global identifiability or independently repeat optimization. The author's scaled Jacobian singular values imply condition number about202630 in its stated scaling. This warns that small calibration changes may materially move tau and the held-out predictions; an exact five-coordinate fit alone is not strong predictive evidence. The extra fres3 calibration also means that baseline and extended model use different amounts of calibration information.

The endpoint-mean convention is implemented correctly as declared. It is not established by that implementation as the experimental ENS mean. In particular the fres7 endpoint half-difference is about1.035824 MHz, larger than its averaged residual magnitude0.789388 MHz. Therefore its mean residual sign or apparent closeness cannot be declared robust against the unknown charge convention. The f06 drive endpoint half-difference is about0.288686 MHz. Neither endpoint half-difference is an experimental error bar or a proven bound over all offsets.

SOURCE_READING.md reports parity exposure and level-conditioned cavity preparation, while explicitly withholding a claim of exact endpoint averaging or Gaussian MHz accuracy. This numerical review does not independently re-audit the original experiment's complete precision/readout analysis. No significance, confidence level, unique mechanism identification, or conclusion robust to all allowed calibration errors follows from the nominal residual table. Subsequent author sensitivity outputs are outside this frozen-source numerical check; the original conditioning and charge-convention limits remain in force.

## Reproduction and evidence

Run `python3 independent_direct_check.py` in this directory. It writes independent_direct_results.json, preserving cutoff spectra, overlaps, eigenpair residuals and sampled continuation. independent_direct_run.log records its final clean execution. independent_quadrature_results.json/log and independent_direct_first_results.json/run.log preserve the earlier quadrature checks and warnings. Only independent review files were written; author sources and other checkouts were not changed.

The independent construction was developed after reading the primary model and displayed evaluation as requested. Its independence is the different raw-potential construction and direct basis, not blindness to the expected output or an independent experiment. Both use SciPy eigensolvers.

## Exact source identities

- `PROTOCOL.md`: `26b6e2f99375e9df5d17caa338a1fade2ed15470cb1c9aa59caf9333bedfae88`
- `model.py`: `6129a23fe0d9cb6cf1b0862702650e13c6a607d0cb6f0208042247a9e53c6090`
- `calibrate.py`: `2b70f60ab9f4a6a675041b927171c703b25dc351381d165497e6910fa0b62e76`
- `evaluate.py`: `ec7614e856d32b08a66127f908cf5e6b9483b40368b81f450d118a052e4a32f8`
- `calibration.json`: `a29d0a620d69f34aea0df124e94a7438206ccc6efe0970f815aca2549d99a284`
- `evaluation.json`: `b0fa8eeb20ad6c1dc41d732dadee8277f42c2b1db284c0f6b68b7be2fd473f5a`
- `SOURCE_READING.md`: `83e1fd504db1a8ecba5a150c2e1f1bf65db47f3c852f16ad26c5872bdbb2d1f0`
- `independent_direct_check.py`: `0eda785db1b959b35ff3835a13eeb4b05c0aac908f0074942cfa799069e057c9`
- `../stronger-test/Experiment.csv`: `0b6abf45a5b574f2ecc492b19560d44ff1638894a0579504dc850c1cb628a01b`
