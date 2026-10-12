# Frozen galaxy response comparison

The declared nonlinear circular-acceleration response predicts this processed SPARC test sample substantially better than the locally normalized positive linear finite-range family. The latter selects zero massive weights and the upper allowed stellar mass-to-light ratio, reducing to Newtonian baryons. This is a reproducible model-development comparison, not a raw observational likelihood, a general exclusion of positive spectral responses, a dark-matter test, or a field-theory completion.

The current main source pin is `516cb69d8487ff04f8a48e065d3dcbe71d7dd237`. The [protocol](FROZEN_COMPARISON.md) was frozen at 2026-10-12T18:13:24.226146Z, SHA256 `7bc3c4e668f551b7093ec3bcd9e8204dc4c5544bc38d03aca8a41059ced1e459`. Code and actual galaxy split were frozen at 18:20:46.303965Z; every trained global parameter was saved at 18:20:46.525640Z before any test score. The result file was written at 18:20:46.655513Z. Prior public-data exposure, including six training-only example galaxies, is declared in the protocol. No claim is adopted or retained.

## Primary inputs and their limits

The [official SPARC project](https://astroweb.case.edu/SPARC/) supplies the [sample table](https://astroweb.case.edu/SPARC/SPARC_Lelli2016c.mrt), [mass-model archive](https://astroweb.case.edu/SPARC/Rotmod_LTG.zip), photometry and bulge/disk decompositions. These are author-distributed processed products. Their original H I/H-alpha reference codes are preserved for each galaxy. The [master paper](https://astroweb.case.edu/ssm/papers/AJv152n157.pdf) specifies thin gas, an exponential stellar vertical profile, and a helium factor of 1.33 in Vgas; unit mass-to-light ratio applies to Vdisk. Signed component speed means signed V|V|. Its velocity-error construction includes fitted and approaching/receding-side terms, but not the inclination systematic. A covariance matrix of all processed points and baryonic components is not supplied in these files.

The official copy's sample-table separator spaces do not match the historic byte-column offsets; the runner uses the documented token order and verifies 175 rows. H I surface-density profiles are not included in the standard rotation-model archive. A Yukawa field therefore requires an explicitly assumed inverse density reconstruction; multiplying each supplied disk acceleration by a spherical exterior factor would be unjustified.

| Pinned file | SHA256 |
|---|---|
| SPARC_Lelli2016c.mrt | `5aa0501f6b0d881fa579030e315e7b5b6ef561a5bd3a07472f9929c7e5728243` |
| Rotmod_LTG.zip | `0a80cc90714828cc28b7dd57923576714d209f2490328c087c4a4ad607faf588` |
| sfb_LTG.zip | `2ca5c5e16517d2096dde47247f2b78837e33fed2e323ea77b0412cf6de66eb27` |
| BulgeDiskDec_LTG.zip | `0733de0d357cbd45c673fd4321a3b339e160abf68530684c09d28e413855fb6d` |
| Master paper, typeset PDF | `87fa39590a0cded15e6dc7a51355fa2354eea8a130f477b92e4cee15c4e36a19` |

The fixed nonlinear response is the known functional form in [McGaugh et al., arXiv:1609.05917v1](https://arxiv.org/abs/1609.05917v1), eq. (4); it is not a new discovery or a fit to previously unseen SPARC observations. That primary PDF is pinned with hash `80357e5b689f1ae7c087359ff936a4543ad09bd4619498026d9e0bcf828fe8a8`. We refit its single acceleration scale on the declared training subset and objective rather than importing the paper's fitted scale.

## The actual disk kernel

Let an axisymmetric component have surface mass density Sigma(R) and normalized exponential height p_h(z)=exp(-|z|/h)/(2h), with h=0 interpreted as a plane. Use the order-zero Hankel transform

`Sigma_tilde(k) = integral_0^infinity R dR J0(kR) Sigma(R)`.

For a Yukawa Green function exp(-mu s)/s, Fourier transformation in the plane gives 2pi exp(-q|z-z'|)/q, q=sqrt(k²+mu²). Integrating the exponential height at z=0 yields 1/(1+qh). Differentiating the potential then gives

`g_mu(R,0) = 2pi G integral_0^infinity dk [k²/q] J1(kR) Sigma_tilde(k)/(1+qh)`.

This is the cylindrical finite-source force, including contributions from matter outside the evaluation radius. The latter can point outward; there is no pointwise disk-force inequality obtained merely from the fact that every pairwise Yukawa force is weaker than Newton's after local normalization.

The positive basis is a circular ring of radius A convolved with a planar Gaussian of width sigma:

`Sigma_A(R) = M/(2pi sigma²) exp[-(R²+A²)/(2sigma²)] I0(RA/sigma²)`.

It is nonnegative and integrates to M, with transform `M exp(-sigma²k²/2)J0(kA)/(2pi)`. Substitution gives precisely the forward integral in the protocol and runner. Every reconstructed density is a positive sum of these basis profiles. The central Gaussian has independent closed Newtonian potential `-GM sqrt(pi/2)/sigma exp(-z)I0(z)`, z=R²/(4sigma²). A separate direct real-space calculation integrates the angular elliptic kernel after an integration by parts in source radius, avoiding the local force singularity. It agrees with the Hankel code to 4.2e-12 relative or better. The code's analytic Gaussian, distant point-pole and noncentral finite-height controls also pass. These are numerical checks; no interval certificate is claimed.

The first real-space check used ellipk(1-p) and encountered roundoff at the integrable logarithmic singularity p=0. Switching to the stable complementary-argument ellipkm1(p) fixed it before target fitting; thresholds were unchanged. The initial metadata byte-parser failure and both repairs are preserved in the runtime evidence.

## Baryonic reconstruction and selection

The frozen cuts retain Q=1/2, i>=30 degrees, zero tabulated bulge, at least six radial points and five at R>=0.5 Rd. There are 116 eligible galaxies. A deterministic nonnegative fit uses 64 Gaussian-ring masses for each gas and stellar component, calibrated only to the supplied signed baryonic V² and total mass. Gas mass is 1.33 MHI, stellar mass is the unit-U luminosity. Stellar height is h=0.196 Rd^0.633 kpc. A small 1e-10 squared-coefficient preference resolves numerical nonuniqueness without using Vobs. The mass interval is +/-5%; the fixed acceptance gates are RMS <=2% and maximum <=5% of the component's maximum absolute V² (with a 1 (km/s)² floor).

103 galaxies pass. Their source coefficients are numerous baryonic calibration variables (up to 128 per galaxy), **not** observed-rotation-fitted gravity parameters. They do not establish unique gas or stellar density profiles. The reconstructed stellar surface brightness differs from the supplied profile by median fractional L1 0.0806, interquartile range 0.0363..0.1297, maximum 0.2747. This diagnostic was not used to retune the source fit. Thirteen failures remain excluded, with exact residuals in the reconstruction receipt: NGC0055, NGC0289, NGC0801, NGC2403, NGC2903, NGC2915, NGC3198, NGC3521, NGC5055, NGC5371, UGC00128, UGC01281 and UGC05721. This is an explicit source-family limitation.

The hash split gives 84 training galaxies/1154 scored radii and 19 test galaxies/309 radii. The test names are DDO170, F583-1, NGC0247, NGC3726, NGC3917, NGC3953, NGC3972, NGC4559, UGC00191, UGC04499, UGC05414, UGC05716, UGC05750, UGC05986, UGC07524, UGC07603, UGC09037, UGC11455 and UGCA444. All are plotted in the runtime figure, avoiding a residual-selected illustration.

## Responses, fit and result

Use the locally measured G convention. The positive linear family has pair potential

`-G_N m_A m_B/s * [1-sum(w_j)+sum(w_j)exp(-s/lambda_j)]`,

where w_j>=0, sum(w_j)<=1, and lambda=[0.3,1,3,10,30,100] kpc. Each term is evaluated on the finite disk source above. The normalization is not a free galaxy strength: G_N includes the total short-distance attractive response. Fixing a bare large-distance G instead would change the observable model and must not be substituted silently.

The nonlinear circular rule is `g=nu(gbar/a0)gbar`, `nu(y)=1/[1-exp(-sqrt(y))]`. It has one global a0 in [1e-12,1e-8] m/s². All models share a single global stellar U in [0.1,1.0], or the declared fixed-U=0.5 variant. No per-galaxy gravity, D, i or U was fit. N, L and NL have respectively 1,7,2 global free parameters, reduced by one in the fixed-U table. N means baryonic Newtonian gravity, not Newtonian gravity plus a fitted dark halo.

The objective is the galaxy-equal mean squared log10 velocity residual. It is not a likelihood; neighboring radii and galaxy nuisances are correlated and their full covariance is unavailable. No sigma exclusion, posterior odds or information criterion follows from these scores.

| Model | Trained U | Trained physics parameter | Train RMS log10 V | Test RMS log10 V |
|---|---:|---|---:|---:|
| Newtonian baryons N | 1.000000, upper boundary | none | 0.226977 | 0.200649 |
| Positive linear L | 1.000000, upper boundary | all six w=0 | 0.226977 | 0.200649 |
| Nonlinear circular NL | 0.560512 | a0=7.658058668e-11 m/s² | 0.102353 | 0.060689 |
| N, fixed U | 0.5 | none | 0.304254 | 0.283405 |
| L, fixed U | 0.5 | all six w=0 | 0.304254 | 0.283405 |
| NL, fixed U | 0.5 | a0=8.533673475e-11 m/s² | 0.102523 | 0.061584 |

For free U the test mean signed log residual is -0.15050 for N/L and -0.002350 for NL. Multistart constrained optimization and the exact nested-Newtonian control find the displayed L solution. This is not a theorem that no other global optimum exists: the squared-log objective is not globally convex over all feasible predictions; four training galaxies violate a simple sufficient pointwise curvature condition. All six local weight gradients at the displayed boundary are positive. The result is a numerical best-found comparison within the frozen finite grid, not an obstruction theorem for all positive measures.

The 96-ring sensitivity passes 108 galaxies; the frozen comparison uses the 103-object common sample, avoiding a changed-sample explanation. Its free-U NL test RMS is 0.060685, a change of 4.26e-6 dex. On the same sample using the original published baryonic components, NL gives 0.060685 and N 0.200646. On all 116 initially eligible galaxies, including the 13 inverse-density failures, the narrower original-component diagnostic has 25 test galaxies and gives NL 0.062456 versus N 0.200964. These controls expose the reconstruction's role; they do not remove its density ambiguity.

## Nuisance and cross-scale accounting

Central tabulated D and i are fixed throughout the primary comparison. Under a homologous distance change d=D/D0 at fixed angular structure, R scales by d, luminosity and gas mass by d², and Newtonian component V² by d. A finite-range field depends additionally on lambda/d in the fiducial source geometry. Thus gbar is distance independent at fixed angular profile and U, but observed V²/R is not. Under the additional uniform-tilt model, the same line-of-sight speeds imply `Vobs(i)=Vobs(i0) sin(i0)/sin(i)`; the quoted random errors scale the same way. A new inclination also changes deprojection of the source and may not preserve the original warped velocity-field reduction. Simple speed rescaling is not a full source/kinematic reanalysis. Exact per-galaxy D, e_D, i, e_i, distance method and original-source codes are retained. No nuisance intervals were mislabeled as confidence regions, and no nuisance optimization on test velocities was performed. The reported U-boundary solution depends on the explicit common [0.1,1.0] population prior.

For a point or spherical exterior source, a positive locally normalized linear force factor `(1+mu r)exp(-mu r)` decreases with r. The disk computation, rather than that spherical fact, supplies the comparison above. Under the additional unscreened linear metric-response premises used in the earlier gravity packet, let f2 and f0 be the fractions of the locally calibrated nonrelativistic force carried by massive spin-2 and scalar sectors. At mu times AU <<1, `gamma=1-f2/2-2f0`. All present galactic lengths meet that long-range Solar condition. Positivity prevents their PPN deficits from canceling each other; the earlier Cassini fit belongs to this effectively constant-gamma response class, subject to its stated source/nuisance limitations. The fit here allowed much larger weights anyway and still selected zero. This does not apply to screened or otherwise nonlinear completions.

For the nonlinear rule, gbar>>a0 gives fractional local enhancement `1/[exp(sqrt(gbar/a0))-1]`, while gbar<<a0 gives g~sqrt(a0 gbar). An isolated spherical far field then has V⁴=G M a0. These are consequences of the supplied rule, not separately fitted laws. The small local Solar correction **does not establish Solar-system compatibility**: an action/field completion can produce a nonlocal external-field quadrupole even where local accelerations are large.

The known [QUMOND field equation](https://arxiv.org/abs/0911.5464v2), `laplacian Phi=div[nu(|grad Phi_N|/a0) grad Phi_N]`, is one explicit next completion. It is an additional physical premise. In a nonspherical galaxy its conservative field is generally not identical to the algebraic radial map fitted above. A Solar external-field calculation using the fitted a0 therefore remains conditional on a provisional disk calibration until the actual QUMOND galaxy problem is solved. Relativistic lensing, wave propagation and cosmology remain open as well.

The concrete falsifier is now available: retain the response function and galaxy-calibrated a0 without Solar retuning, specify the Galactic external field, and compare the resulting anomalous Solar quadrupole with its primary Cassini observable. This is distinct from both the gamma measurement and the rejected GW ridge extraction. A failure would reject that specified completion/parameter box, not every acceleration law.

## Evidence and reproduction

Scripts here are `moving_envelope_check.py`, `galaxy_forward.py`, `preflight_checks.py`, `compare_responses.py`, and `make_figure.py`. The comparison runner intentionally refuses to overwrite its frozen test-evaluation receipt. Use a separately documented runtime copy for a new block. All numerical libraries run with one thread. The 64- and 96-ring calibration jobs took 3.11 and 4.89 seconds respectively; target fitting/scoring took under one second. No detached jobs, commits, pushes or governance changes were made.

Runtime root: `/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/galaxy_response/`. `inputs/source_manifest.json` pins official URLs, UTC and hashes. `protocol_freeze.json`, `fit_code_and_split_freeze.json`, `training_parameters_frozen.json`, `baryonic_reconstruction_{64,96}.json`, `baryonic_forward_{64,96}.npz`, `preflight_checks.json`, `comparison_results.json`, and logs preserve inputs, failed gates and successful calculations. `galaxy_test_predictions.png` and `.pdf` show every primary test galaxy. `CHECK_RECEIPT.json` hashes the final packet and evidence. The moving-current independent check is separate in [MOVING_ENVELOPE_REVIEW.md](MOVING_ENVELOPE_REVIEW.md).
