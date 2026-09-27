# Independent microscopic-transfer numerical review

2026-09-27. Bounded source and selected forward-spectrum review; no optimization, higher-target comparison, or empirical model selection. Complete PROTOCOL.md, model.py, calibrate.py, INPUTS.json and all eight fits were inspected. All frozen-input manifest hashes match. No consequential numerical or algebraic defect was found in the checked path.

## Construction and conventions

For an arm with uniform local potential u and rectangular phase ramp, its normalized spatial average is (1/2) integral from −1 to 1 of u(phi+phase+pi B x/Bnode) dx. Its mth Fourier component is therefore multiplied by sinc(m B/Bnode), where sinc(z)=sin(pi z)/(pi z). The harmonic index belongs inside sinc; replacing it by the fundamental envelope for every harmonic would change this supplied model. The primary default field_harmonics=True is correct. The field_harmonics=False option is not used by calibration.

The primary coefficient is the complex exponential Fourier coefficient, so division by −2c1 sets the local first cosine harmonic to −J. The raw short-channel potential −sqrt(1−tau sin²(phi/2)) is equivalent, up to constant and positive scale, to the rationalized primary expression; both are normalized by their own zero-field first harmonic before spatial averaging. Jsum is the zero-field sum of the two arm first-harmonic strengths, not the first harmonic remaining at finite field. The independently recomputed area asymmetry is (256*257−178*143)/(256*257+178*143)=0.44207965280669836.

At psi=pi the arm coefficients combine as Ja sinc(m B/Ba)+(-1)^m Jb sinc(m B/Bb); odd harmonics subtract and even harmonics add with their signed envelopes. B=.15 T, Ba=.8 T, Bb=.8*256/178 T are used as declared. This is not a justification of uniform current density, common local tau, area-proportional current, the node assignment, or exact experimental psi=pi. Those remain supplied premises covered separately by source review.

For general psi the primary hopping exp(i(n−n')psi) is Hermitian because the reverse hopping is its conjugate. With charge plane waves exp(i n phi), that convention corresponds to a second-arm potential u(phi+psi). Dropping its diagonal Fourier constant changes only a scalar. The charging and cavity operators correctly use n−q; the cavity quadrature is X=a+a† and all Hamiltonian coefficients are in GHz. Bare labels are selected uniquely by overlaps.

## Independent numerical evidence

`independent_spatial_transfer_check.py` does not import the author model. It spatially integrates each raw arm potential by Gauss–Legendre quadrature, projects the resulting real phase function onto charge plane waves, and diagonalizes the full charge tensor photon Hamiltonian. Isolated-device eigenvectors are used only for label assignment, not Hamiltonian truncation. It checks q=0 and .5 for shape start .01 in both source versions and processed cosine.

Coarse checks use charge cutoff N=22, 12 photon states, phase grid4096, 64 spatial nodes; fine checks use N=28, 16 photon states, grid16384, 128 nodes. Primary is N20/M16/K9/grid8192. Across all first-three ground gaps in the selected cases, fine versus primary mean/full-dispersion discrepancies are below 0.000671 Hz; independent coarse-to-fine changes are below 0.000548 Hz. Minimum fine bare-label weight exceeds 0.99807. Endpoint labels [0,1,3,5] are unique in these checks. These floating-point comparisons support the selected spectra at scales far above numerical roundoff; they are not rigorous interval bounds or physical sub-millihertz accuracy claims.

| Frozen case | Fine mean f03 (GHz) | Fine full endpoint δ03 (GHz) |
|---|---:|---:|
| archive / shape start .01 | 14.658812062761 | 0.057572038376 |
| processed / cosine | 14.693214234822 | 0.009509654014 |
| processed / shape start .01 | 14.669695550686 | 0.037795597478 |

Full δ03 is abs(f03(0)−f03(.5)); no half-amplitude or three-photon division is hidden here. The endpoint mean remains an imported fitted-center interpretation, not a demonstrated continuous-offset mean or measured line center. Neither this code nor the selected endpoint check proves global offset extrema.

## Cosine mapping and objective separation

At tau=0 and psi=pi, EJ_eff=Jsum[(1+alpha)sinc(B/Ba)−(1−alpha)sinc(B/Bb)]/2. The processed cosine gives EJ_eff=13.477096630512918 GHz, matching the earlier single-junction fitted EJ=13.477096630513303 GHz within 0.000386 Hz. EC differs by 0.000010 Hz. Their saved first-three means and cavity mean agree within 0.000064 Hz; full endpoint dispersions agree within 0.000159 Hz. This exact model reduction, up to roundoff in separate fits, is an implementation control rather than empirical success. The comparison and earlier source-file identity are retained in independent_cosine_map.json.

Calibration uses only the two centers and (shape only) full 01 splitting. It correctly computes 12 as mean f02−mean f01. No 03 target or measured 12/02 dispersion enters the objective. Some unused metadata are loaded with energy_prediction.json, so this is objective separation, not absence of prior exposure. The relative-log splitting residual and MHz-scaled center residuals are numerical weights, not a likelihood. Cosine leaves splitting out; all three shape starts and both source versions are retained. Absolute finite-difference steps avoid tiny relative tau steps near zero. Tiny residuals and consistent starts do not establish uniqueness, global optimality, fit confidence, or a microscopic interpretation of tau.

The fixed Omega/G transfer, source-version ambiguity, same-state/center assumptions, common gap multiplier and uniform-area premises remain unresolved physical dependencies. A common gap scale can be absorbed into Jsum at this fixed field and shared local shape; unequal arm gap changes or field-dependent shape changes are not covered. No targets were compared here, and no native-theory or independent microscopic confirmation follows from the successful forward check.

## Exact evidence identities

Selected immutable rows, endpoint energies, overlaps, eigen-residuals, cutoff comparisons and execution output are retained beside this report. SHA-256:

- `PROTOCOL.md`: `d5d6ffc5674ccd62e5468c29e9980a55dbcc74927120548d391ad3c82afce061`
- `calibrate.py`: `4a995d96ef058109f142b20df18716c317ef17bf3d2693917c86eada1b53fd30`
- `model.py`: `d9db69aa06122958dc81120c1518ef2e3148a01dfd46a2f1820e0d593eac8cf3`
- `INPUTS.json`: `b80627a0662c143d033780ebb50c722f0badf801a10a5c103bc20f9371f7ddb3`
- `fits.json`: `1db744ff5ff43d6165f1ae7dfec5a49911be64e413ecfd7addb7d09fc9615786`
- `independent_spatial_transfer_check.py`: `72e0d499a2184c2ba921bdd0592f7cd0656a62f451f421908dba36b47eb15306`
- `independent_spatial_transfer_snapshot.json`: `8a8015d9f55a2cfff633664c27a51c14e2a1078678cb18ab2f9e265af6f96f4c`
- `independent_spatial_transfer_results.json`: `56d9ecc0052845b39c1c18fe1f60c152281dc0aa8b4d871ffdbc282d9e9cb963`
- `independent_spatial_transfer_check.log`: `d76eb792b04a55177970e415e54a2f3daadc305b71193d290b1a97c3320f33b8`
- `independent_cosine_map.json`: `a0ba2b1db657f794bbb5e18f0f386ec7633f7908f15f42d2b5c94745ac41118c`
