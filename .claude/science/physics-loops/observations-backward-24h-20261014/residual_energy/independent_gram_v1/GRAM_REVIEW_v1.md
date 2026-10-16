# Focused independent check of finite residuals and KG energy

Reviewer: `/root/localized_history_check`. Date: 2026-10-15 UTC.

The working statement in `residual_energy/DERIVATION_v1.md`, SHA-256 `fd0f660b86d47f444236ad0a2e13c416c23a0f9d52442d7a5dafd7afb8aa05e1`, has no mathematical discrepancy within the specified real free-KG energy space and bounded observation model. The normalization, triangular-window cross terms, finite-dimensional minimum, and stated positive-definite nuisance quotient are correct. The minimum is a lower consistency bound; it is not a physical principle selecting that field or an observed upper energy budget.

I preserved an independent derivation before opening the new working note or any new author implementation. After reading the note, I implemented and executed 110 separate mathematical controls without importing or reading author code. These include actual real smooth Fourier initial fields, independent angular and temporal integrations, an explicit invisible field, singular compatibility tests and a direct nuisance-constrained KKT calculation. No raw data, physical residual, fitted parameter, PR operation or formal audit verdict is involved.

## Real-data normalization and Gram operator

For the adopted stable flat operator, the real energy Hilbert norm is

    ||(q,p)||_H^2 = integral (|grad q|^2+mu^2 q^2+p^2) dx = 2E.

For positive mass the completion is H1 x L2. For zero mass use the homogeneous-H1 x L2 completion of real smooth compact data, with the usual zero-norm identification where constants are used as representatives. Observations extend continuously from smooth data; a pointwise gradient is not presumed to exist for every energy-class field.

With unitary spatial Fourier factor `alpha=(2pi)^(-3/2)`, `Omega=sqrt(k^2+mu^2)`, and real temporal transforms `W_i=C_i+iS_i`, the Riesz datum for a fixed-point observation in a common unit direction n is

    qhat_i(k) = -i alpha (n.k) exp(-i k.x0) C_i(Omega)/Omega^2,
    phat_i(k) = -i alpha (n.k) exp(-i k.x0) S_i(Omega)/Omega.

These obey the conjugate-symmetry constraint for real initial data. The real energy inner product gives

    G_ij = 1/(6pi^2) integral_0^infinity
           [k^4/(k^2+mu^2)] Re[W_i(Omega) conjugate(W_j(Omega))] dk.

Equivalently the frequency measure is `((omega^2-mu^2)^(3/2)/omega) d omega`. The angular average and the real positive/negative frequency pairing introduce neither another factor two nor a factor three. For massless fields and real H1 temporal weights, Parseval gives exactly

    G_ij = integral w_i'(t) w_j'(t) dt / (6pi).

G is the observation operator's energy Gram matrix, not a measured noise covariance. The off-diagonal entries are essential. The massive spectral formula is correct, but its generally different matrix cannot be replaced by the massless tridiagonal matrix.

## Triangular windows and exact constrained minimum

The two constant pieces of the derivative of `w_i(t)=(T-|t-c_i|)_+/T^2` give the arbitrary center-separation formula in the note. For adjacent centers separated by T, the derivative self-overlap is `2/T^3`, neighbor overlap is `-1/T^3`, and all other overlaps vanish. Thus

    G = L/(6pi T^3),  L=tridiag(-1,2,-1),
    E_min = 3pi T^3 r^T L^-1 r.

For finite N and T>0 the eigenvalues `2-2cos(j pi/(N+1))` are strictly positive. The stated inverse with one-based indices is correct. The one-window minimum `(3pi T^3/2) r^2` matches inversion of the earlier one-window norm. Coincident or linearly dependent observations require the general singular treatment; they are not covered by assuming this particular positive-definite L.

For any finite bounded real observation map A, `G=AA*` and `Range(G)=Range(A)`. Exact consistency requires `r in Range(G)`. The unique minimum-energy element is `h_min=A*G^+r`, with

    E_min = (1/2) r^T G^+ r.

Every consistent field decomposes as `h_min+z`, `Az=0`, and `E=E_min+||z||_H^2/2`. The factor one half is fixed by the definition of energy. A pseudoinverse quadratic form evaluated on incompatible data is not a feasible lower-energy solution: it silently discards the inconsistent null-space component. The working note correctly states compatibility first.

My independent algebra controls used direct interval intersection lengths at N=1,2,4,9 and T=0.6,1.7, the separately closed inverse/eigenvalue formulas, eleven nonadjacent center separations, and duplicated/linearly dependent constraint rows. An explicitly incompatible vector was detected even though its pseudoinverse quadratic form equals that of its compatible projection. The zero observation map with zero data has the expected zero minimum. These finite numerical checks supplement the exact Hilbert-space proof.

## Smooth data, exact constraints and actual Fourier fields

The minimizer is attained in the energy completion and need not itself be Schwartz. The note appropriately distinguishes attainment there from the smooth constrained infimum. Its full-rank smooth-approximation argument is correct. A slightly more general proof also covers compatible singular observation families:

Let D be the real smooth compact data or real Schwartz data, dense in H. Its image A(D) is a linear subspace dense in the finite-dimensional Range(A), hence equals that range. Choose finitely many elements of D whose observation vectors form a basis and a linear right inverse S on Range(A). If `phi_m` tends to `h_min` in H, then

    psi_m = phi_m + S(r-A phi_m)

has exactly the required observations, remains in D, and tends in H to `h_min`. Therefore the constrained smooth infimum equals the completion minimum. This does not claim smooth attainment of the minimum or select a cosmological initial state.

I also constructed explicit real Schwartz Fourier fields independently. Each Riesz datum was multiplied by the radial factor

    rho(k)=exp[-(k T/K)^2-(epsilon/(k T))^2], epsilon=1/K,

extended flatly at k=0. The infrared flatness removes the possible Riesz singularity and the ultraviolet factor makes the data rapidly decreasing. Writing `G_rho=<g_i,rho g_j>` and `G_rho2=<rho g_i,rho g_j>`, coefficients `a=G_rho^-1 r` give exact finite constraints in the analytic construction and energy `a^T G_rho2 a/2`. Positivity and convergence to G follow from the integral representation and dominated convergence; for this independent triangular family, positive rho preserves independence.

For residuals `(0.14,-0.08,0.23)`, T=1 and centers `(-0.8,0.2,1.2)`, the exact Hilbert minimum is approximately `0.44555637809537246`. The smooth controls give:

| K | Smooth field energy | Relative excess above minimum |
| ---: | ---: | ---: |
| 4 | 0.5320833042935136 | 0.1941997252 |
| 12 | 0.4780925705873840 | 0.0730237386 |
| 36 | 0.4562451410562477 | 0.0239896980 |
| 108 | 0.4490899174354827 | 0.0079306223 |

These are numerical controls of the analytically exact construction, not interval certificates for exact equality. At K=4 I evaluated the actual complex qhat/phat fields on a separate spherical quadrature, using a spatial direction `(1,2,3)/sqrt(14)`. The resulting three-dimensional energy and constraints agree with the reduced Gram construction. Separately integrating the evolved field gradient through each triangular time window gave `(0.13999999999999974,-0.07999999999999974,0.2299999999999995)`. A massive `mu=0.7` field control also agrees with its actual massive Gram and gives the same requested residuals. It does not assume the massive minimum equals the massless one.

## Nuisance quotient and singular caution

For a supplied nuisance design X with unrestricted real coefficients, the note's positive-definite result is correct. If U has full column rank spanning `ker(X^T)`, then

    min_beta E_min(r-X beta)
      = (1/2)(U^T r)^T (U^T G U)^-1(U^T r).

This is an exact quotient of a specified nuisance subspace, not an inferred instrument model. I compared it with a direct block KKT solve, weighted least-squares projection, nonorthogonal changes of quotient basis, and redundant quotient rows, using constant and affine nuisance designs. They agree.

For a singular G the useful extension is to choose C with `ker(C)=Range(X)` and define `Hq=C G C^T`. Feasibility then requires `C r in Range(Hq)` and the minimum is `(C r)^T Hq^+(C r)/2`. Equivalently, minimization over beta must retain `r-X beta in Range(G)`. Dropping this condition is wrong. An explicit control has

    G=diag(1,0), X=(1,1)^T, r=(0,1)^T.

Feasibility forces beta=1 and the minimum is 1/2. Naively minimizing the pseudoinverse form without compatibility chooses beta=0 and falsely returns zero. The quotient `C=(1,-1)` returns the correct 1/2. This is a boundary qualification for future singular extensions, not a discrepancy in the current note, which explicitly restricts this nuisance formula to positive-definite G. If the nuisance span is the whole observation space, the quotient is empty and the minimum is zero under the usual empty-space convention.

The proposed further minimization over an error set is not yet an empirical construction. Its numerical size, geometry and correlations require a supplied or measured error model. No covariance, force residual or source-forcing budget was invented in this review.

## Invisible energy and physical normalization

A finite bounded observation map on the stated infinite-dimensional Hilbert space has an infinite-dimensional kernel. Adding a kernel vector to the orthogonal minimizer preserves all those observations and increases the mathematical energy. This is a statement about that fixed map and supplied linear space; it does not apply automatically after additional physical constraints, nonlinear validity limits or other observations are imposed.

For the common fixed-point gradients an explicit smooth kernel datum is a radial Gaussian centered on the observation point,

    q(x)=A exp(-|x-x0|^2/(2sigma^2)), p=0.

Rotational invariance of the free KG evolution makes its center gradient zero at every time. Its exact energy is `A^2 pi^(3/2)[3sigma/4+mu^2 sigma^3/2]`. It is orthogonal in energy to the odd-direction Riesz reconstruction. The independently evaluated field with A=1.7 and sigma=0.8 has invisible energy about `9.65548074650618` for mu=0; adding it increases the constructed field energy by that amount while leaving the observation vector unchanged. The corresponding massive control also agrees. Scaling its amplitude gives the limited mathematical upper-energy ambiguity without assigning that amplitude to the real environment.

The final physical normalization in the working note is also consistent for its explicitly same-normalization, massless coupled combination: with `Q_J>0` and nonzero squared coupling `q>0`, `E_phi,min=(Q_J/q) r^T G^-1 r`, hence `E_phi,min=[3 T^3/(4 G_bare q)] r^T L^-1 r` when `G_bare=1/(8pi Q_J)`. This follows directly from `E_phi=2Q_J E_math` and the coupling-rescaled Gram. The zero-coupling limit must instead be treated as a zero observation map; division by q is then unavailable. The note's coupled-sector wording is compatible with the nonzero condition. No SI numerical substitution, actual energy calibration, varying-mass generalization or realistic moving-path Gram is established here.

## Evidence, independence and unresolved inputs

The source identities are:

| Artifact | SHA-256 |
| --- | --- |
| Author `residual_energy/DERIVATION_v1.md` | `fd0f660b86d47f444236ad0a2e13c416c23a0f9d52442d7a5dafd7afb8aa05e1` |
| Independent `GRAM_PRECHECK_v1.md` | `0f9ed691bca4e74bb58fb544186dee7506ccff291f91a85e54d3b8984a81081d` |
| Independent `independent_gram_check_v1.py` | `36f859f4c14992740f31bbaf23ff597c115348099013b045855959ff914f6fda` |
| Independent `INDEPENDENT_GRAM_RESULTS_v1.json` | `16de0423d86484e05d9134347ca4ea87d670df4c3da576e84d66020951899071` |
| Author `residual_energy/ALGEBRA_PROBE_v1.json` | `f360264df8f18fdd49279cb4e42823ea02079ad30a9386fbec25fe38c27bd8c5` |
| Inherited M4 canonical note | `059e1ff0ef5ab67e71763a55b022e130348b54e8477b478ecf5e0aaa25f0a74e` |

The author's algebra probe was opened only after my independent run. Its ten algebra comparisons are separately attributed; the runtime file named in the note is byte-identical to the local `ALGEBRA_PROBE_v1.json`, so there is no missing-probe identity discrepancy. No new author implementation was available for review at the time of this report; the report is bound to the working mathematical note and that small author probe, not to any subsequent implementation. A later implementation needs its own affected source confirmation.

All 110 independent controls passed on the first run; no failed attempt was overwritten. The largest recorded comparison error is approximately `2.78e-11`, in a larger-magnitude finite matrix energy calculation. The separate actual-field/time-observation errors are at floating-point scale. These ordinary numerical computations and their quadratures are not rigorous interval bounds or independent experiments. Run stdout and empty stderr are retained with the result.

Physical residual extraction, an actual calibrated observation operator, the error region, the energy normalization appropriate to the real environment, and any independent upper energy bound remain open. The supplied stable free operator and its range of validity also remain assumptions. The mathematical minimum reconstructs a norm-compatible representative; treating it as the real initial state would add a variational assumption that has not been derived. The narrowly invisible kernel does not prove a theory-wide no-go or exhaustion. No M4 source, state, lock, branch, index or external application was changed by this check.
