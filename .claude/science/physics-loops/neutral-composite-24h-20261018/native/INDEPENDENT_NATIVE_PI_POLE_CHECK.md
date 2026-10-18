# Focused momentum-pi native finite response check

Disposition: PASS for source convention, finite L8 prediction, and residual-qualified comparison. Reuses the periodic-H construction check in neutral-native-periodic-pole-check.md. No full32 replay, repository edits, or formal audit.

The only physical-source change is coefficient (-1)^(j+1), precisely exp(i*pi*(j+1)) for the midpoint of the longitudinal NNN pair (j,j+2). Even L8 makes the midpoint convention periodic and real Hermitian. Dividing by sqrt(L) is unchanged. A uniform minus sign relative to exp(i*pi*j) changes amplitudes, not auto-spectral weights. This is momentum pi of the supplied observable, not an inferred new coupling.

An independent finite-band control reconstructs the momentum-pi transverse source by signed single-rung flips of the equal eight-vacuum representative. Its norm squared is exactly 4 numerically. Applying the original diagonal centered NNN operator to the first-order dressed vacuum gives the NEGATIVE of this source times lambda, with error 2.3e-16, independently confirming the physical leading amplitude -2lambda and its normalization.

Using the previously checked complete native energy-8 band matrices, a two-vector Krylov basis from this source gives exactly [[1/2,1/4],[1/4,-1/4]]. K1 annihilates both columns and K2 closure residual is zero at floating precision. Thus the finite eigenvalue shifts are (1±sqrt(13))/8, with source coefficients 2±6/sqrt(13): upper .5756939094329987 and 3.6641005886756877, lower -.32569390943299864 and .33589941132431256. These are finite L8 coefficients, distinct from infinite-chain limits. The independent control is neutral-native-pi-independent.py/json.

The first and third candidates (zero-based indices 0 and 2) have small reconstructed full-H residuals at BOTH couplings. At .1 these are 6.26e-13 and 2.05e-12; at .2, 1.17e-13 and 3.14e-14. Every other listed candidate must be rejected as an eigenmode. In particular, at .2 index1 has residual .00796566 despite nearly duplicating the accepted upper energy and source weight. Its reported weight must not be added to a spectral sum. The three-term Lanczos recurrence has no full reorthogonalization; near-unit reconstruction norm or quadrature-node agreement does not establish independent eigenvectors.

For the accepted upper candidate the following scaled errors are diagnostic only:

- lambda=0.1: (gap-prediction)/lambda^4=-0.194599363; (weight/lambda^2-predicted coefficient)/lambda^2=0.4422985235.

- lambda=0.2: (gap-prediction)/lambda^4=-0.1924951514; (weight/lambda^2-predicted coefficient)/lambda^2=0.4118144521.

These two points are consistent with quartic energy corrections and quadratic corrections to the normalized leading weight; they are not an asymptotic proof. Small residuals certify nearby spectrum but do not by themselves certify isolation or an exact individual spectral weight. The computation supplies selected-sector finite native-H evidence with a specified state/source, not a global-ground, thermodynamic pole, decay width, or physical scalar result.

## SHA-256 identities

- `/private/tmp/neutral_native_periodic_pi_pole.py`: `db697dfa580be2b1afa6e5578f810d0ac41b1175004fcb72ba361b88720bccdd`

- `/private/tmp/neutral_native_periodic_pi_pole.json`: `57c6f13b35ac717897c75581c4066602bbd1baa1757b31a7e3bb608763ec47b9`

- `/private/tmp/neutral-native-pi-independent.py`: `4cc77adada221074dbcd3b53886737e9968e857330bde4d3c3cd264069289225`

- `/private/tmp/neutral-native-pi-independent.json`: `7f7e50d8b12fc205f3581a13303e9bbadee4bffb8bfbdb9a57ac9fbc6757d43a`

- `/private/tmp/neutral_kink_core.py`: `62cc36f85bb1d6932ccc81db8a9ebe3f0171a7443adc74d2d6564c4da45e4dd8`
