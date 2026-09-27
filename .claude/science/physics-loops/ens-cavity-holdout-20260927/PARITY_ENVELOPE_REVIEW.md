# Parity-envelope code and claim review

Complete changed code/prose review of `parity_envelope.py`, `parity_extrema.py`, `RESULTS.md`; complete JSON structures checked through arithmetic/identity assertions and relevant numerical summaries. Prior independent physical-gauge derivation/direct spectra reused with unchanged model/calibration identities. No spectrum rerun, fit, source-image extraction or source-identity revalidation in this task. Author files unchanged.

## Findings

No consequential mapping, indexing, parameter-preservation or arithmetic error found. No material overclaim requiring correction was found in the current results note, provided its explicit conditional/numerical limitations remain attached to the table and conclusions.

The physical helper correctly calls the old endpoint at q'=q(1−G²/(4EC Omega)). Scalar energy changes cancel in all returned gaps. Stability is asserted. The sixth array entry `[5]` is E(0,6)−E(0,0)=f06, not an adjacent gap or f06/6. Pairing grid indices k and k+32 at65 equally spaced physical offsets compares q and q+.5. All33 pair splittings/centers independently recompute exactly from the saved13-frequency arrays.

Nominal cosine and Andreev parameters equal the original baseline and minimum-calibration-cost solution exactly. Every16/32 inherited rounding-corner parameter vector and sign tuple also matches its original source JSON. The selection code takes the minimum cost over all solutions without an explicit success filter; currently that minimum is the same successfultau=.2 row previously checked, so no change occurs. If future calibration content changes, the selection policy should stay explicit rather than assume that a minimum-cost row necessarily succeeded.

## Numerical/prose alignment

The saved nominal sampled maxima are.544476840808MHz (cosine) and3.464585004508MHz (Andreev); quarter-offset pair differences vanish to numerical precision. Sampled center ranges are.000044928388MHz and.001724180077MHz. Corner endpoint ranges are.540475594580–.548504471421MHz and2.586014736991–4.596981674883MHz. All numbers match the results table's rounding.

Five calibration-coordinate differences use indices[0,1,6,7,8], which are f01,f02 and resonator gaps for devicelevels0,1,2. Largest saved physical-minus-old mean change is.00119016Hz for Andreev; cosine's largest magnitude is.00015632Hz. The “at most.0012Hz” summary is accurate for this calculation. Those minute values are near numerical subtraction/truncation scales and should mean negligible at the original reported calibration precision, not an experimentally established millihertz bound. Prior independent endpoint checks support the much larger but still small f06 convention shifts: about337Hz/53Hz in the splitting.

The four finer points agree with the primaryf06 values within.002477Hz for cosine and.000100Hz for Andreev. All65 rows retain unique14-label assignments; minimum reported overlap is.890232 for Andreev, versus.912454 for cosine. Unique/high-overlap labels are numerical assignment diagnostics, not state-preparation evidence. The extrema receipt hashes match the reviewed input JSON and runner.

## Envelope and claim limits

The fixed65-point scan covers a complete physical period. The four bounded optimization intervals partition[0,.25], exploiting even/periodic parity symmetry; they are four subintervals of a quarter period, not four full quarter-period intervals. Explicit endpoint values are retained, correctly handling the bounded optimizer's inability to land exactly on a boundary. Every returned local search value is below the recorded endpoint maximum.

`minimize_scalar(method="bounded")` supplies a local numerical search, not certified global maximization; neither it nor the grid rules out a narrow unseen structure. The finite corner control calculates only q0/.5 endpoints, not each corner's full continuous charge envelope and not the interior of the parameter box. The prose states both limitations and labels the table column “endpoint range.” Keep that distinction: a corner endpoint range cannot be promoted to a uniform parameter-envelope exclusion.

The Andreev compatibility argument is an existence argument along the assumed continuous physical energy branches: the endpoint splitting exceeds the indicated scale and quarter offset gives zero, so an intermediate compatible splitting exists. It does not infer that offset trajectory or its occupation. The source discussion's reverse-triangle inequality for absolute Ramsey detunings is correct; same-sign peaks give their separation, opposite signs give their sum. There is no six-photon division of free-evolution f06. The quoted source extraction/2019–2024 linkage was reviewed separately and is not newly certified here.

The wording “opposite-sign detunings…incompatible with these computed envelopes” must retain “computed”: these are numerical sampled/refined envelopes, not rigorous all-offset/all-parameter bounds. The note appropriately limits the cosine comparison to numerical tension for the frozen model/source mapping, acknowledges the differing four-versus-five calibration coordinates/parameters, and does not turn the envelope-compatible Andreev scale into a precise prediction. The title and status remain support for a conditional scale comparison, not native or holdout confirmation.

## Preserved evidence and SHA256

`parity_envelope_review_arithmetic.py/json` preserve parameter/corner equality checks, all grid pair arithmetic, frequency-array sizes, assignment uniqueness and extrema receipt consistency.

- `parity_envelope.py`: `c8763aa40d16e0396d9d35c5683c613ffbd29599ed11643015d4d0e0242f9dd4`
- `parity_extrema.py`: `ef85d6feb5853733ed3602f2b2f67989cd6138b6973b5837820a6908430917cc`
- `parity_envelope.json`: `95bcad96ee184fd32829b07453de36eaea50f4c28ca9f1a562f3a848ba8c1817`
- `parity_extrema.json`: `42685d5c1f0732d24b6c383ce8c4c57de35666e80baa46825f9f06191c912a52`
- `RESULTS.md`: `c12c6523d2031057dc137636f99249563f52776372058359a4aca5c6b70d69e5`
- `PARITY_GAUGE_REVIEW.md`: `dc647e7533f0816bb8cd0c314f883750d1a57ab2c54fcd16cf11e3f1f035ec74`
- `../ens-independent-cavity/model.py`: `6129a23fe0d9cb6cf1b0862702650e13c6a607d0cb6f0208042247a9e53c6090`
- `../ens-independent-cavity/calibration.json`: `a29d0a620d69f34aea0df124e94a7438206ccc6efe0970f815aca2549d99a284`
- `../ens-independent-cavity/baseline_corners.json`: `4fc3e8e79de760011f66ae859043b17caf63973762e2d5f1137fed38e412b9ef`
- `../ens-independent-cavity/rounding_corners.json`: `4a2ce34948f635f2e13ad370f05842334e2983a705b63151c3380af5b97a712d`
- `parity_envelope_review_arithmetic.py`: `399ffd92710a8f358018f600423666ccd14067c82e1c63f8e1d9631f88d247a2`
- `parity_envelope_review_arithmetic.json`: `53a68f5585089801b63f934395acbb8b0d5b59e8a5451719f5728e1471888647`
