# Post-exposure working-source correspondence, v1

This is a focused mathematical/source comparison performed after the independent proof and controls were frozen. It is not a formal audit, a new empirical test, or a replacement for root's authorship. The pre-exposure report `INDEPENDENT_MATH_v1.md` (SHA256 de40057de817a745e52beebb6a162802ff4215b862932ef5b7bad818f8a8f811) and its exact evidence remain unchanged. Parent-supplied target formulas had been disclosed before that derivation; author working files had not.

No substantive mathematical discrepancy was found in the authorized working argument or critical implementation formulas on their declared domains. The angular law, waveform/timing model, training separation and quantizer enclosure remain supplied physical assumptions. This comparison does not establish those assumptions from receiver data.

## Exact complete read scope

I read the entire working derivation, the entire geometry and sampling source files, and both entire retained output files. They were copied byte for byte into this independent directory before analysis; `AUTHOR_EXPOSURE_v1.json` records that exposure and source identities. `AUTHOR_CORRESPONDENCE_BINDINGS_v1.json` verifies that the source, exposure snapshot and frozen hash still agree for all five files. It also verifies all recorded source-hash fields and that every file in the pre-exposure identity remains unchanged.

| Author file | SHA256 | Bytes |
| --- | --- | ---: |
| WORKING_DERIVATION_v1.md | b56992df97bc2c69f579b2bc7e58cc69d8e7549f4aa10a1ee102bcc562a25656 | 11336 |
| direction_geometry_v1.py | d9892abaadee8cdab6a65ac679ffd3c41b433bd5cd77202bb306b1105632ba6b | 7593 |
| direction_sampling_controls_v1.py | d9848c9cdc92e42d0b797a7ff29001109ca3b909a9f1d1302176673fc63e5f38 | 5010 |
| AUTHOR_GEOMETRY_CONTROLS_v1.json | d33189172d4aaec0bc5c9b5e54b2bd08fad8ea423d55d9fd97095b63b797d8de | 2126 |
| AUTHOR_SAMPLING_CONTROLS_v1.json | 050d8ac0ff3cf090da4fb00d5590b4a6b26e704fcdabebd352db644dd48f7afe | 1788 |

The author directory is `calibration_supplier` under the current campaign pack. Full absolute source and snapshot paths are in the exposure/binding JSON. I did not open `DIRECTION_TEST_PROTOCOL_v1.json`, the empirical execution implementation, observations, prior source documents, or any other new author files. I did not execute either author program, rerun author aggregates, use the network, or write outside this assigned independent directory.

## Conditional inference and exact geometry

The note's probability model matches Sections 1–2 of the independent proof: at fixed true parameters, conditional on training, the error direction is uniform on the complex sphere and its norm is positive. An arbitrary actual radial law, including direction dependence, cancels from the pivots. The Gaussian representation is used only to represent uniform direction; it does not smuggle in Gaussian receiver noise. Complex ranks give twice those ranks in the real F degrees of freedom. In the two-template case, r=1 and s=N-2, so the note's closed form tau²=alpha^(-1/s)-1 is correct.

`ratio_tau` implements that closed form with `expm1` for the rank-one case and otherwise uses sqrt((r/s)*F_isf(alpha,2r,2s)). The rank-one branch is numerically preferable to subtracting nearly equal values. It rejects nonpositive ranks and invalid tail levels; the geometric ranks are supplied as integers by the stated callers. The proof does not make arbitrary noninteger ranks a geometric model.

`carrier_components` projects off u_f and the normalized orthogonal part of u_g. Writing delta as an aliased difference and using expm1 followed by subtraction of its mean gives the same span as the direct two-tone projection, including the common phase produced by centered sample times. The exact-delta-zero branch has rank one; `carrier_accepts` deliberately accepts it instead of dividing by r=0. The near-alias construction avoids one direct cancellation but does not constitute a certified numerical rank decision.

The cone-distance proof matches the independent minimizing radial construction, including b=0 with a nonempty B range and preservation of the unused component. It does not assume convexity of the cone. `cone_distance` implements the correct positive-part quotient. The author controls also cover tau=0, whose separate limiting geometry is valid. The quantizer-safe frequency acceptance uses the exact Euclidean-ball enlargement q*sqrt(1+tau²), not the unsafe q-only enlargement exposed by the independent orientation witness.

`amplitude_disk` uses c_hat=u_f*z/N, the full orthogonal residual norm, and [tau_c*residual+q*sqrt(1+tau_c²)]/sqrt(N), with the correct N-1 complex residual rank. This is the exact union over the enclosing ball; an ADC box inside that ball yields a conservative disk. It does not replace the physical error by quantization or equate residual energy with a deterministic noise budget. A phase interval needs the disk to exclude zero. Amplitude is defined relative to the supplied time origin and frequency representative: replacing f by an aliased representative can rephase c for centered times. The current formula is consistent for its actual supplied f; any physical phase interpretation must preserve that convention.

The note uses the union bound 1-alpha_f-alpha_c for a joint frequency/amplitude region. This is valid, though the nested unquantized decomposition admits the stronger product coverage proved independently. The source notes that optional fact and does not rely on it for the empirical procedure. It correctly avoids transferring that independence to arbitrary color statistics or to quantized statistics.

## Color diagnostic and global finite-arc logic

The DFT split removes the true tone's DC component after derotation and creates orthogonal residual subspaces. Both ranks must be positive to invoke the F law. The author source's `ratio_tau` guard enforces this when thresholds are constructed; the stated N=500 case has exactly 248 low and 251 high complex coordinates, plus one DC coordinate. I independently counted those indices from integer inequalities after exposure. Small N=3 or 4 would have no low group and is outside this color-test domain, as shown in the pre-exposure controls.

The far-candidate argument is sound. From q_g=rho*q_f+sqrt(1-k²)*v, one obtains the stronger lower bound (R-k)_+*||z||/sqrt(1-k²). Dropping its denominator is conservative. Combining the weaker bound with ||Bz||<=||z|| gives the stated sufficient exclusion. `global_carrier_arc` forms m=R-tau-q*sqrt(1+tau²)/||z||. When m<=1/N, or the stricter k=.999*m does not exceed 1/N, it returns an uninformative half-period. Otherwise the chosen D solves 1/[N*sin(pi*D/fs)]=k<m, giving strict real-arithmetic exclusion for circular distances at least D. The z=0 branch is explicitly uninformative. The retained remaining arc contains the rank-one reference itself.

This argument requires positive fs, actual uniform sample times, 0<D<=fs/2, nonzero z for the normalized expression and nonnegative q. It does not apply to arbitrary irregular physical time coordinates. The code uses the stated centered nominal grid; no physical timing equivalence was checked here.

`spectral_parts` uses a unitary-normalized FFT and the stated half-band masks. For each upper tail, the ratio threshold has the correct rank order; reversing the low/high groups reverses the ranks. `color_arc_exclusion` uses alpha_record/2 for carrier and alpha_record/4 per color tail. Each midpoint score is reduced by its appropriate (1+tau)*2*pi*||t*z|| times the half-cell width and by the ADC margin. Taking the larger of the two tail lower bounds for a cell is valid: either positive lower bound excludes that entire cell. Taking the minimum over all cells requires every cell to be excluded. The cells span the full retained arc. If the carrier arc cannot be bounded usefully, the function reports inconclusive rather than silently adopting a local interval.

The proposed Lipschitz constant follows from projection contraction and the diagonal-unitary derivative. It is conservative; the independent proof also gives a sharper coefficient, which is not necessary for correctness. Periodic score magnitudes permit a centered-time alias seam without changing the norms. The .999 margin supplies a strict analytic inequality in real arithmetic, but does not quantify floating roundoff. The note and returned `roundoff_certified=False` explicitly preserve this limitation.

The three direction statistics need not be independent. The chosen allocation yields a false-rejection probability at most alpha_record under the fixed procedure's conditional premises; summing across 1200 fixed records yields the stated .01 upper bound without record independence. That is a property of the fixed mathematical procedure. Because the observations motivated the model/procedure and remain exposed development data, this comparison does not validate a newly independent empirical p-value or a selected physical explanation. The note explicitly makes that distinction.

## Sampling code and retained evidence

The geometry output contains 22 recorded controls, including five nearest-cone witnesses, four projection/rank cases, three rank-one quantile comparisons, three color Parseval/Lipschitz cases, three scale transformations, the covariance counterexample and three pure-tone nonrejection fixtures. The stored source hash matches the fully read geometry file. I inspected these results; I did not reproduce them.

The sampling output contains nine recorded controls. It uses one fixed set of 50,000 proper-complex Gaussian directions, then reuses the directions with constant, lognormal and direction-dependent radii. These three radial checks are pointwise invariance controls, not three independent empirical experiments. The code verifies identical decisions and close numerical pivots. Its clipped radial perturbation construction stays inside the prescribed ball because nonnegative-coordinate projection is nonexpansive. It checks that every accepted analog fixture remains accepted after the correct enlargement.

The nested joint simulation uses the correct full residual denominator U+V. The reported .97986 against .9801 is a Monte Carlo implementation control, not the proof of independence. The pre-exposure report already supplies the separate beta/gamma factorization and exact simplex controls.

For validation leakage, the author selects the largest among m=N-1 residual coordinates. If W is uniform on the residual simplex, inclusion-exclusion gives

    P(max W_j>u)=sum_j (-1)^(j+1) C(m,j) (1-j*u)_+^(m-1).

This follows because translating any chosen j coordinates by u leaves a simplex with linear scale 1-j*u and dimension m-1. The code's formula and truncation at floor(1/u) therefore match the claimed analytic probability. The stored decimal 0.3518716581129069 is an ordinary floating evaluation of that exact expression; it is not a numerical interval certificate. The measured synthetic fraction .35262 is consistent as a control. This mechanism agrees with the independently derived N=3 exact doubled-tail witness, without relying on the author's simulation to establish failure.

The general color check uses r=16, s=23 with total N-1=39 and the correct (s/r) energy scaling. Multiplying one subspace energy by four deliberately violates the angular law and makes the rejection probability large; it is explicitly a synthetic variance mismatch, not a receiver calibration. The covariance-isotropy witness in the note is also valid: atomic coordinate directions with independent random phase have identity-proportional covariance but fail the spherical law. Its explicit handling of the atom giving a zero denominator by the cone inequality is coherent. The independent nonzero-denominator finite witness is stronger but is not needed to repair the author's example.

## Remaining domains and actual limits

The routines are working scientific helpers, not a fully hardened public API. They trust the caller to supply finite arrays/frequencies, positive fs, the stated sample-count regime, and finite nonnegative q; not every one of those conditions is validated inside every function. The physical ADC and angular assumptions are external to the helper. This is a scope condition rather than a discrepancy in the declared N=500 working use. Changing those domains would require additional validation and possibly different formulas.

I did not verify the empirical statements about the previous constant-modulus failure, which records were used, training/validation extraction, instrument flags/settings, measured margins, competing peaks, or raw-data exposure history. Those are outside the authorized mathematical comparison and require their own evidence. No theorem here derives or excludes a scalar action, initial field, potential, absolute scale, environmental solution or measured-gravity bridge. No new retained physical claim follows merely because these conditional tests are mathematically valid.

There is no requested mathematical repair from this source comparison. The explicit domain qualifications and ordinary-floating limitation must remain attached to any canonical adaptation. All historical independent proof, controls, failures of weaker claims, author exposure snapshots and output receipts remain preserved. No source, index, branch, publication or state file was modified.
