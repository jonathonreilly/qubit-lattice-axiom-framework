# Independent numerical review of the frozen two-field radiation block

## Disposition

The checked numerical values support the stated conditional construction. The photon calibration, all 43 FIRAS baseline/rounding diagnostics, all 24 old-potential residuals, all 72 local grids, all six stored history runs, and all 20 endpoint rows agree with an independent formulation to the relevant numerical precision. No empirical success, full CMB likelihood, cosmological stability theorem, unique reconstruction, or negative-claim delivery certification follows from these checks.

**R1 remains a required test-sensitivity correction for the frozen author runner:** replacing its complete coordinate-acceleration expression by literal zero preserves all 1,195 reported passes. This makes the initially supplied p=-3 persist by construction. Thus this suite does not independently check that the implemented x dynamics is the actual coupled system. The unchanged source equation is consistent with independent canonical equations, and an independent canonical-velocity integration reproduces the background. The finding is a missing executable discriminator, not a falsification of the proposed exact background. A narrow repair is to compare the actual implemented operator on nearby non-solution states with independently obtained canonical Klein–Gordon accelerations, and demonstrate that the zero-acceleration mutation fails. The parent was notified promptly; no author files were edited by this reviewer.

The separate mathematical reviewer owns the continuum proof, including the corrected dust-speed factor. This report supplies numerical and source-provenance checks; it does not borrow that review as positive evidence.

## Exact source scope and evidence

The immutable author snapshot is `snapshot/`. It contains all eight frozen inputs and the complete initial source snapshots, results, freeze, execution receipt, stdout, and stderr. The input receipt accounts for 21 paths. The first execution is the recorded run from 04:34:17 to 04:35:34 UTC on 13 October 2026: exit 0, 77.1025 seconds, 1,195 passes and no failed assertions. The stderr file is empty. This reviewer did not replace that run with a clean historical rerun.

Key identities:

| Source | SHA-256 |
| --- | --- |
| Author runner v1 | `01cf3b23ccf55fd4ee8905368beef1b13dae58cb8270a5e51da19147aba53ee7` |
| Hand derivation v1 | `b8dd9cc0e26787ba32475c93b57034a9482aba0db7559e193703ab41f47d2570` |
| Hand derivation v2 | `4d62ed249c42ed532b41b87ebee1a482236e404463da891c77dfffbf9485f95b` |
| Protocol | `bfd06bb72d44088b742c551fe2537559110c317efa26bbca53d68a52513b95a1` |
| Fixtures | `1c125242e99770a9a3387f2a17358cad8b705c7c82dec9136794e4951218811c` |
| Source ledger | `5752d548ba306bdd29fd3ffc9aa8c05191ef718e41d170f28dd19059b45868fc` |
| Dust-speed correction | `ac1fc454b38531eaa137631249151c99d30e80dfe6df424f739131f237a86a68` |
| FIRAS table | `df793c3dca09ebfa7dbc5aa0ec1951daa8884431bc30eff28a710d7516cf50fa` |
| Original author results | `8c0bb51294f924530c5068b61fda0ebfca8818870fea0cb68556381faed01fe7` |

Complete receipts bind every author, primary, reviewer, mutation, and output path. They exclude the final receipt's own bytes to avoid self-reference. Original sources were checked for changes again when the receipt was written. This is an exact-source local numerical review, not a Git-tree review, formal audit, combined repository gate, or permission to land.

## Read ledger and primary provenance

The reviewer read the complete v1/v2 derivations, correction, protocol, fixtures, source ledger, runner, freeze, execution record, and raw logs. All result sections were inspected; all 1,195 assertion rows were exhaustively parsed and checked against their stored fields, while the physically relevant numeric sections were independently recomputed. Recorded solver step/evaluation counts and quoted quadrature error estimates are accounted-for run metadata, not separately reproduced physical claims.

Primary source reading was local against the exact downloaded bytes:

| Primary source | Exact reading scope | SHA-256 |
| --- | --- | --- |
| [Fixsen, arXiv 0911.1955v2](https://arxiv.org/pdf/0911.1955v2) | All six extracted pages; page 5/Table 2 independently rendered and visually inspected. Other figures were not visually assessed. | `36cbaee69b8106ca45d007f46a2e002f9f593b67c310f6d808007a5c3d998f85` |
| [NASA FIRAS monopole product](https://lambda.gsfc.nasa.gov/product/cobe/firas_monopole_spect.html) | Complete scientific product description, including the construction of the posted absolute column. | `e42bcf7e3e2eccac3ac8c210d4287e2477c394ad03d76ac7f719515d29753f2a` |
| [NASA spectrum table](https://lambda.gsfc.nasa.gov/data/cobe/firas/monopole_spec/firas_monopole_spec_v1.txt) | Complete header and all 43 five-column rows. | `df793c3dca09ebfa7dbc5aa0ec1951daa8884431bc30eff28a710d7516cf50fa` |
| [NIST 2022 CODATA table](https://physics.nist.gov/cuu/Constants/Table/allascii.txt) | Header and h, k_B, c, G entries; no use of other table quantities. | `77fb90e66c40db3e6eb16630bc9c88e4c7c8beddbe5e71be406f2f26e3f67e67` |

The download receipt and all four download stderr files were read and preserved. The stderr files are empty and the receipt records successful downloads. The source ledger's earlier ill-formed NIST parameter-page request is preserved as an author-reported operational failure; this reviewer did not independently reproduce that earlier web failure.

The combined temperature is 2.72548 ± 0.00057 K. The distinct WMAP/FIRAS differential result in the same primary is 2.7260 ± 0.0013 K. Table 2 confirms the distinction. The four relevant SI constants agree with CODATA; h, k_B and c are exact SI values and G carries the listed uncertainty. The Mpc conversion and H0=70 are supplied fixture conversions/normalizations here, not measurements by this review. The runner propagates temperature alone, exactly as the protocol says; the stored G uncertainty is not silently included in that temperature-only interval.

## Photon normalization and all spectral rows

The independent calculation starts from two photon polarizations and phase-space measure d^3p/(2πℏ)^3, with E=cp. It evaluates the Bose integrals at 100 digits and independently uses Γ(n+1)ζ(n+1). This gives

  energy density = π²(k_B T)^4 / (15 ℏ³c³),
  number density = 2ζ(3)(k_B T)^3 / (π²ℏ³c³),
  mass-equivalent density = energy density/c²,
  Ω_gamma = 8π G_N rho_gamma/(3H0²).

At the central temperature:

| Quantity | Independent value |
| --- | --- |
| Photon energy density | 4.17467838080037544 × 10^-14 J m^-3 |
| Mass-equivalent density | 4.64495613440336677 × 10^-31 kg m^-3 |
| Photon number density | 410.717806123327 cm^-3 |
| Ω_gamma at supplied H0=70 | 5.04674028922726894 × 10^-5 |

All three temperature rows and their SI conversions match the stored results. The independent linkage check also verifies the old and new S0/R0/b/L parameters from the fixtures and this independently computed Ω_gamma, rather than trusting copied source-density rows. The use of S0=3m/[2(1+a)] and R0=3Ω_gamma/[2(1+a)] encodes the inherited calibration convention G_N=(1+a)G_* with H0 as the time unit. This is a conditional normalization import, not a new measurement or a demonstration of local-gravity viability of the reconstructed potential. An eventual standalone presentation should name that bridge explicitly.

For every spectrum row the reviewer evaluates Planck intensity in spatial wavenumber, considers both rounded-frequency endpoints and the stationary point when inside the interval, and adds the published residual plus the two rounding allowances. All 43 intervals contain the published absolute value. The smallest interval margin is 0.0105041780 MJy sr^-1. All 215 source cells and all 86 stored interval endpoints were checked. The residual-only diagonal sum is 45.0257543116527 and the stated weighted RMS is 18.8962810302335 kJy sr^-1.

These last numbers are descriptive diagnostics. The NASA absolute column is intentionally constructed from a 2.725 K blackbody plus earlier residuals; reconstructing it is not an independent blackbody test. The per-bin errors are not a supplied covariance matrix. No likelihood, parameter fit, p-value, evidence ratio, or held-out validation is claimed. The calibration contains photons only; no neutrino multiplier, baryon abundance, entropy injection or radiation-distribution prediction is supplied by this construction.

## Old-potential residuals and small-number sensitivity

For each of the 24 fixtures the independent calculation differentiates the forced Friedmann solution directly along N, setting S(N)=S0 exp(-3N) and R(N)=R0 exp(-4N), then compares F_N/2 with Raychaudhuri. It does not import the author's partial-derivative helper. The normalized discrepancy agrees at high precision with

  2 a R S [(2+a)S-L] / [3 ((2+a)S+2L)^2 H²].

The largest absolute disagreement of the stored closed-form residue from the independent result is 6.75 × 10^-19. The smallest case is about -3.7848691 × 10^-13; subtracting the two large floating terms loses relative precision there, with maximum relative error 3.7518 × 10^-4. It remains inside the deliberately absolute-normalized assertion bound. The smallest zero-rejection margin is 12.6115 tolerance units.

An actual copied-source mutation sets only the numerical `delta` residue to zero. Executing the affected author function, with unchanged checks/tolerances, yields **0 passes and 24 failed residue assertions**. This is negative sensitivity evidence, not positive use of an author helper. Every raw row, assertion and mutated source diff is retained. No claim of a tiny-residue blind spot is made for this family.

The discrepancy concerns the exact constant-u trajectory of the unchanged dust potential with the stated positive conserved radiation. It is not an empirical exclusion of the full two-field family. Turning this scoped negative result into a certified no-go delivery remains outside this check.

## Curvature and potential grid

The independent coordinate is z=S^(1/6), so R=bz^8 and

  dchi/dz = -2 sqrt(a) z² sqrt(1+4bz²/3)/Hbar.

Canonical derivatives are obtained by applying (dchi/dz)^(-1)d/dz. The reviewer computes U_chichi from repeated canonical differentiation, then M, the full Hessian, its stable eigenvalues, and the actual quadratic minimum U-aS²/(2M). This differs from the author's x=ln(S) differentiation path.

All 72 local rows and their 12 stored local fields agree within the specified numerical budgets. All 504 sampled potential values/bounds are independently reconstructed, and the global-in-u quadratic minimum is separately evaluated. The smallest stable normalized Hessian eigenvalue is approximately 7.49999 × 10^-19; the smallest actual minimum divided by U on this grid is 0.6800000792, comfortably above 1/2. Positivity is conditional on the stated model, domain and parameter values; it is not a cosmological stability result.

Direct double-precision eigenvalues and determinants are ill-conditioned in some large-L, small-a rows. The largest relative discrepancy in the stored minimum eigenvalue is about 9.11 × 10^-4; for the direct determinant it is 5.73 × 10^-4. The signs remain positive and high-precision canonical reconstruction confirms them. The report does not assign machine-relative precision to those tiny displayed eigenvalues merely because a broad absolute comparison passes. Nor is a finite numerical grid a substitute for the separate continuum positivity proof. Grid rows with b=0 or L=0 are explicit limiting controls; they do not change the proof's stated positive-parameter domain.

## Stored histories and an independent operator

All six stored DOP853 histories, their 432 state components and target arrays are checked. Their maximum componentwise absolute errors relative to the supplied exact trajectory are small: below 7.56 × 10^-12 for x, 2.73 × 10^-12 for p, and 1.01 × 10^-12 for log matter density. The reviewer also reconstructs the physical H² at all 72 stored time samples and verifies the supplied normalization, instead of treating a correct-looking coordinate trajectory as sufficient.

For independent integration the state is (u, ell=log z, u_N, chi_N, log sigma_m, log sigma_r, chi). Canonical field velocities appear directly in the Friedmann denominator 3-u_N²-chi_N². The two scalar accelerations are obtained from their canonical Klein–Gordon equations. Conversion back to p occurs only when comparing output:

  ell_N = chi_N/(dchi/dell),
  p = 6 chi_N/(dchi/dell).

RK45, with 2e-12 relative tolerance, 1e-16 absolute tolerance and maximum N step 0.01, is used instead of the author's DOP853 representation. No p=-3 constraint is enforced. Independent direct quadratures in N check the canonical coordinate at every supplied site.

| a | Independent RHS evaluations | Maximum original tolerance units | Minimum Friedmann denominator |
| --- | --- | --- | --- |
| 1e-6 | 12,002 | 5.46537e-5 | 2.99999800296 |
| 1/2499 (stored float) | 13,358 | 2.55452e-5 | 2.99920118186 |
| 0.01 | 15,728 | 2.20018e-5 | 2.98022727375 |

The matching histories are positive corroboration of the stated background and source normalization. The six original step-refinement results alone are not a test of arbitrary changes to the force operator, because the chosen initial condition lies exactly on its constructed trajectory.

## R1: actual forced-acceleration mutation

The copied author runner's sole scientific edit is

  -(3+h)*p - Gamma*p² - V_x/(g*H²)  ->  0.

No checks, expected values or tolerances are edited. The actual full run exits 0 after 67.4393 seconds with **all 1,195 checks passing**. Mutant SHA-256: `fd623fdf3bf7d8130b7ab45597a67bdb7d1600a0c641fdbb18d9ca2c9883dda2`. The symbolic identities are separate expressions and therefore do not test the modified implementation. All numerical background/on-trajectory p tests retain p=-3 by construction.

The reviewer supplies 36 nearby non-solution canonical states, one at every coupling/site combination, varying field displacement, field velocities and both densities. On these states the independently derived p accelerations have magnitudes between 0.0235778 and 0.223197. For example, at a=1e-6 and N=0 a listed state gives p_N=0.0674355026. A zero-acceleration implementation is decisively wrong on these inputs. The full states, canonical accelerations and converted p accelerations are retained in `RESULTS_v2.json`.

The required fix is an executable comparison of the actual author operator against such independently derived canonical accelerations on non-solution inputs. Merely adding more exact-background samples, another refinement, or another symbolic copy of the exact trajectory would leave this defect. The correct scope remains background reconstruction and operator verification, not a claim of stability of those nearby trajectories.

## Endpoint fractional series and numerical precision

The reviewer maps the endpoint quadrature to a fixed [0,1] interval in z=S^(1/6), works at 100 decimal digits, and forms q=delta_chi/[2sqrt(a)/(3H_vac)]. Repeated canonical differentiation gives U_chichi and U_chichichi. All four parameter combinations and all five S values per combination are compared, including intermediate rows where the asymptotic third-derivative sign has not yet settled.

The last-row S coefficient lies between approximately -0.799999999999912 and -0.799999999911619, approaching -4/5. The U coefficient lies between approximately -0.0666666666666580 and -0.0666666666580317, approaching -1/15. The second derivative approaches 3L/2, and the scaled third derivative approaches the positive stated limit. These numerical checks support the one-sided C2/non-C3 diagnosis for b>0. They do not make the potential analytic at the endpoint or prove a smooth extended theory.

The first reviewer script deliberately attempted approximately 32-digit comparisons across all endpoint fields. Five U-series comparisons failed, with discrepancies from 8.87e-31 to 1.414e-23. Diagnosis: the author first adds order-one L at 70 digits, then subtracts it and divides by a*b*q^(8/3), as small as about 1e-49. It is inappropriate to demand 32 trustworthy coefficient digits from that calculation. The v1 source, output, five failures and logs are immutable. Reviewer v2 replaces only that coefficient's comparison budget with an explicit conditioning allowance; all other checks are unchanged. This allowance is a floating-point error budget, not an interval certificate. Every discrepancy is vastly below the author's predeclared 2e-8 coefficient tolerance. No author correction is required for this numerical-precision observation.

## Failures, reproducibility and final limits

Real failures and sensitivity outcomes are retained:

1. Optional BeautifulSoup was unavailable during the review's first extraction attempt. It failed before source reads/writes and was replaced with standard-library HTMLParser. No environment was changed.
2. The first reviewer comparison run recorded 3,607 passes and five overly stringent endpoint precision failures. Its diagnosed correction is preserved as a source diff and separate v2 execution.
3. The old-residue zero mutation produces 24 expected failures.
4. The forced-coordinate-acceleration mutation produces the material unexpected all-pass result described in R1.
5. The author's earlier dust-speed typo and its pre-execution v2 correction remain intact, as do the original primary download and NIST-query failure descriptions.

The current reviewer core has 3,612 passes and no failures; the additional source-linkage/payload coverage program has 1,339 passes and no failures. These are 4,951 checks/accounting entries in total, including exhaustive accounting of the author's 1,195 recorded assertions. They are not 4,951 independent physical experiments or theorem proofs. Reviewer source SHA-256 values are `647d98806a4c0a1336856e342a141eb3513075a5ab0e89788d8181184c86fc70` for the core v2 and `0fe2ec107f4d23d8bcef3ee9761b8c29cc6bde2d18d99bf93a743f2aecf5b515` for the coverage program. The recipe and complete machine-readable read/identity receipt specify reproduction and source closure. Neither positive program imports or executes author numerical helpers. The zero-residue author's function is executed only as an explicitly labeled negative mutation control; the forced-acceleration mutant is a complete copied-source run.

This source remains a conditional two-field construction from exposed data calibration and supplied target/initial conditions. This review supplies no evidence for a TOE, photon microphysics, baryon/neutrino contents, early thermal history, unique observations-to-action inversion, full perturbation stability or independent observational acceptance. R1 is open for the pinned v1 runner; any parent correction should be checked as a separate affected-source version, preserving these results.
