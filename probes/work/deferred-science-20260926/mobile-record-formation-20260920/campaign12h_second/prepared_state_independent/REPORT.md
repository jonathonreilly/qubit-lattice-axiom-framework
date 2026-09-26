# Prepared finite-mode state: bounded independent review

2026-09-21. The smooth-weight refinement's limiting covariance, entropy,
fixed-site marginal estimate and positive microscopic charge variances check,
conditional on the pinned stationary propagator. One finite-volume example
needs a narrow mode-set qualification. No displayed limiting formula needs
correction. This review neither re-proves the inherited fluctuation theorem
nor establishes a local preparation mechanism, physical emergence or audit status.

## F1: the finite-volume nonstationarity witness is too broadly worded

The paragraph beginning “The prepared microscopic law is generally not
invariant” correctly identifies the uniform invariant law within each
irreducible content-count sector. Its two-`+x`-record witness works when M
consists of the first axis shell. But the following phrase is too broad:

> For a symmetry-closed set containing the first axis shell the other axis
> modes do not remove this difference.

Take `N=5` and

    M/(2 pi)={e_x,e_y,e_z,2e_x,2e_y,2e_z}.

This set is cubic closed up to conjugacy, with no aliases or self-conjugate
modes. With only two `+x` records separated by `d e_x`,

    Q(d)=[4+2 cos(2 pi d/5)+2 cos(4 pi d/5)]/[125(rho_A/3)].

The two cosines interchange at `d=1,2`, so `Q(1)=Q(2)` exactly. At
`rho_A=3/8` both equal `24/125`. The purported distinguishing weights are
identical for every lambda. Separating the same records by `e_y` instead
gives `Q=64/125`, so nonstationarity itself still holds in this example.

**Narrow correction:** replace “a symmetry-closed set containing the first
axis shell” with **“the first-axis-shell choice of M.”** Alternatively qualify
the larger fixed set by sufficiently large N. For that alternative,
`N>3 max_{K in M}|K_x/(2 pi)|` makes every relevant
`cos(K_x/N)-cos(2K_x/N)` nonnegative and the first x-axis contribution strict.
The current author checker does not test extra harmonics. This finding was
sent to the parent author before opening the checker. No source was edited.

## Reconstruction of the new claims

The hypothesis is a fixed full-support isotropic fifteen-label product with
positive `rho_A,rho_B` and vacancy probability, no births, fixed bounded
positive-floor rates, finite fixed M, fixed finite lambda and fixed finite T.
The imported microscopic remainder has its supremum **outside** expectation.
Modes are nonzero and counted once modulo conjugacy; aliases and self-conjugate
frequencies are excluded for sufficiently large N. Boundary densities,
growing mode sets and increasing observation windows are outside this argument.

The normalized single-site six-vector has mean zero and covariance `I_6`.
Discrete Fourier orthogonality and product CLT give independent proper complex
Gaussian limits for the selected representatives. There are `2m` complex
longitudinal coordinates, each with mean-square one. For one such coordinate,

    E exp(-lambda |z|^2)=(1+lambda)^(-1).

Consequently the weighted CLT gives

    Z_N -> (1+lambda)^(-2m),
    Sigma_lambda=P_T+(1+lambda)^(-1)P_L.

The transverse coordinates and the other eight moment fields remain
independent spectators in that limiting Gaussian decomposition. Finite-N
independence or exact finite-N Gaussianity is not being asserted.

The unchanged path kernel gives the exact initial path-density ratio
`g_N(eta_0)/Z_N <= 1/Z_N`. This transfers the pinned L2 remainder without
microscopic stationarity of the tilted initial law. It is the same bounded
path-density mechanism already used by the first-campaign box conditioning;
the present addition is a smooth distribution and its quantitative statistics.

With signed `c=gamma sqrt(rho_A rho_B/3)`, `C_K^T=-C_K` makes
`G=i c [[0,C_K],[-C_K,0]]` anti-Hermitian. Its exponential has diagonal blocks
`P_L+cos(c|K|t)P_T` and upper cross block `i sin(c|K|t)C_K/|K|`.
The lower cross block is its negative. The tilted covariance commutes with G,
proving stationarity of the **limiting** Gaussian family and the displayed
two-time covariances. At `c=0` all vector modes are static. Product fourth
moments and the bounded density justify second-moment convergence as well
as convergence in distribution at finite lists of times. No microscopic
stationarity or path-space convergence is inferred.

The exact finite-N entropy identity is

    H(mu_N|nu_N)=-log Z_N-lambda E_mu Q_N.

For positive lambda, `Q exp(-lambda Q)` is bounded, so the weighted CLT gives
`E_mu Q_N -> 2m/(1+lambda)`. At lambda zero, entropy is zero exactly. Thus

    H(mu_N|nu_N) -> 2m[log(1+lambda)-lambda/(1+lambda)].

These are exact finite-lambda *limiting* formulas. The entropy per site tends
to zero. The domination constant can grow with lambda or m, so these facts
do not establish a joint large-N/large-lambda limit. The stated ordered limit
suppresses only the chosen longitudinal modes.

For the local estimate, view all complex Fourier components as a finite real
vector Y and let P be its longitudinal projector. The gradient bound for
`exp(-lambda ||PY||^2)` is

    L_lambda=sqrt(2 lambda/e),  L_0=0.

Removing a fixed site set A changes Y by at most
`|A| sqrt(m) M_0/sqrt(V)`, where
`M_0=max(sqrt(3/rho_A),sqrt(3/rho_B))`. The remaining sums are independent of
the variables in A under the product law. Subtracting the product expectation
inside a covariance with g gives the quantitative bound

    TV(mu_N|A,nu_N|A)
      <= L_lambda |A| sqrt(m) M_0/[Z_N sqrt(V)].

This proves the claimed `O(V^-1/2)` estimate at fixed parameters without
assuming finite-N local independence. The centered divergences use six
distinct neighboring sites. Their product variances are `rho_A/2` and
`3 rho_B/2`, and the six-site marginal estimate transfers these limits.
Global A/B sign symmetries give zero initial means exactly. These positive
charge variances rule out microscopic Gauss preparation by this argument.

## Independent exact controls and author comparison

The independent derivation and checker were sealed before any prepared-state
author code/output was opened. Besides exact covariance, spectral and Gaussian
integral controls, two finite constructions test consequential limits:

- The entire `N=4` sector containing two identical `+x` records has 2016
  arrangements. Since there are no B records, its context drive vanishes;
  it is exactly symmetric stirring. At `rho_A=3/8`, first-axis-shell M and
  `lambda=4 log 2`, Q has values `0,1/4,1/2` with multiplicities
  `512,1024,480`. The conditional normalizer is `143/252`.
  For records at `000,100`, `(mu L)(configuration)=1/1144>0` for unit
  unaccelerated floor. Euler acceleration multiplies it by N. This directly
  confirms finite-volume nonstationarity for the corrected witness.
- A separate exact convolution evaluates the **full 15-label product law**
  at `N=4`, `rho_A=3/8`, `rho_B=1/4`, one mode `2 pi e_x` and
  `lambda=16 log 2`. The real/imaginary groups each contain 32 sites; their
  sufficient-statistic law has coefficients of
  `[10+x+x^-1+2y+2y^-1]^32/16^32`. The tilt is rational on these 2113 states.
  Marking one or two sites gives exact local marginals and charge moments.

The second control yields the following rounded values. Underlying rationals
are preserved in the results; entropy uses the exact identity above:

| Quantity | Finite `N=4` value |
|---|---:|
| Normalizer Z_N | 0.00709888423536531 |
| Relative entropy | 3.15545575572514 |
| One-site TV from the original product | 0.0188103504166393 |
| E_mu abs(D e)^2 | 0.183808585888066 |
| E_mu abs(D b)^2 | 0.360551556183041 |

At the same lambda the Gaussian-limit normalizer is `0.00684103641446995`
and entropy `3.15023715236121`. Thus the finite-volume law is decisively not
being mistaken for its Gaussian limit; its local charge variances stay
positive and its vector means vanish exactly.

After sealing, the complete 94-line author checker, result JSON and full log
were read. Their four groups agree with the reconstructed claims. All nine
recorded Gaussian integral/entropy cases and the spectator eigenvalues/local
charge values were compared exactly. The eight toy path-bound rows satisfy
their stated arithmetic. The four-site toy is explicitly separate from the
actual fifteen-label propagation theorem; the source does not misrepresent
it as proving that theorem. Matrix-exponential decimals were authenticated,
not independently rerun; the signed propagator and covariance identities had
already been checked symbolically before comparison. No further code/prose
drift was found. The author checker was neither executed nor imported.

## Identities, reproducibility and remaining scope

| Source | SHA-256 |
|---|---|
| Prepared note | `d0f31d58931cdce1671d252ec77a9ffe2296c03940ab761584245816857317d8` |
| Prepared checker | `215b7e73909eb016ebf62a09738bf24617ab9a0d5028379eff6714b685eabbb4` |
| Prepared results | `4d733358114dcf78426306dff3c545322bc7cc2e1ca3d5e7a8785fe93c87ada2` |
| Prepared run log | `ba70343da064bdf7323c3654da95f06b04821c4e1b639f28d8687be307174d45` |
| Earlier Gauss-sector preparation | `96ff2a8b16e0e5b65d0e4024b4b943102c080024d74948b499a754802006308d` |
| Pinned transverse construction | `1403c91ef041838347bc72c9a30a63d4db73619dcca7fd7775158cfaa2586d32` |
| Pinned stationary fluctuation proof | `0c0b3713caa0769a2a711c7a75480f6db59f01bea5088982fb97b1acf7edc85e` |

`PRE_COMPARISON_SEAL.json` has SHA-256
`baa1f772c2a61acd569d1cbabfe095fb03e59dfec5fe9b812944d69debb385bc`.
It binds the complete derivation, independent code, exact results and full
execution logs. Its eight artifacts remain unchanged. Both independent and
comparison scripts passed on their first execution; no failed attempt was
discarded. Reproduce into fresh output files using
`independent_check.py --out <fresh.json>` and
`compare_sources.py --out <fresh-comparison.json>`.

The preceding periodic/parity prose correction was separately acknowledged
without numerical reruns in `periodic_parity_independent/F1_ACK.json`, SHA
`7b6b74de86025be783a68e04416c6899ea65b7376a831bf115d1a34d4da30db6`.
All 18 artifacts of that earlier review were preserved. It is a separate
correction acknowledgment, not evidence for the prepared-state mathematics.

F1 remains the sole actionable correction at the frozen prepared-note hash.
The stationary propagator stays an explicit imported dependency. No formation
from empty, extensive conditioning, continuing-birth theorem, boundary-density
extension, finite-amplitude Maxwell dynamics, quantum interface, vacuum
selection or physical field identification was proved or assumed. Primary
files, Git state, audit status and unrelated candidate sources were untouched.
`FINAL_SEAL.json` binds this report and the full evidence at these identities.
