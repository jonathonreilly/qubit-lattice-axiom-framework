# Independent reception-gain robustness supplement

The finite one-field matrix attains rank 12, but is poorly conditioned even after column normalization (condition number 729814.62). Crucially, dropping the gain-derivative path term survives the predeclared unused-angular-row test exactly. Additional cross-shell and original-equation residuals reject this particular omitted-term reconstruction. A single-shell coefficient fit therefore does not establish the existence of a homogeneous physical history.

This supplement retains all earlier reports and freezes. It reads no root implementation or new joint-gain source. The candidate note SHA256 is 3b2990808323f90ec02922f1b572985b99b00edf6ab73224e2dde0fb04c63f78. Exact inputs, code, outputs and receipts are bound in robustness_final_bindings.json. Computations used bytecode-disabled Python and 120-second bounds; the preserved receipts record actual commands and elapsed times. No execution failure occurred in this supplement; the scientifically important failed detection is retained, not relabeled as success.

## Frozen finite-field protocol

ROBUSTNESS_PLAN.json predates these calculations. Use the already independently verified 24 physical modes with ell=2,...,25 and n cycling through 0,3,4,5. Their amplitudes are 10^-5 sqrt((2ell+1)/2)/(2^n(ell+1)^4). Sum them into one field with Legendre angular profiles. All 48 Gauss–Legendre angular samples share eta=-2,r=1. Even-indexed rows train; odd-indexed rows are unused. Rows receive square-root quadrature weights. Divide each column by its baseline weighted training norm, frozen across perturbations and mutation. This rescales coefficient coordinates without adding information or removing physical degeneracy. Fixture units have t=r=a=1 at the evaluation point.

Unscaled condition number is 2290722.92. Scaled singular values are

    2.81309834, 1.81474658, .80529637, .27352778,
    .21552557, .14897310, .02814233, .01823355,
    .00916648, .00044205, .0000591763, .00000385454.

The noiseless 80-digit solve recovers coefficients to about 1.15e-69. This checks numerical implementation against the exact modal result; it does not alleviate finite-input sensitivity.

Seed 2026101607 supplies a fixed Gaussian perturbation direction. Matrix perturbations have spectral norm epsilon times the scaled matrix norm; target perturbations have norm epsilon times the target norm. These are generous derivative-level inputs, not errors propagated from photon instruments, cone inversion, registration, angular differentiation, or primitive correlated noise. Some arbitrary feature perturbations need not be realizable by a single underlying field.

| epsilon | Relative coefficient error | Unused-row relative residual | Recovered beta |
|---|---:|---:|---:|
| 0 | 4.14e-12 | 2.29e-15 | .099999999996 |
| 1e-12 | 6.10e-8 | 4.80e-12 | .099999993545 |
| 1e-9 | 6.09e-5 | 4.80e-9 | .099993523693 |
| 1e-6 | .03508 | 4.71e-6 | .065652126134 |

For scaled unknown z, the perturbation estimate follows from sigma_min(A+E)>=sigma_min(A)-||E|| and ||z_hat-z|| <= (||delta_y||+||E||||z||)/(sigma_min(A)-||E||), when the denominator is positive. Recorded nonzero perturbation errors lie below this bound. The zero-noise bound is zero in exact arithmetic; the tiny reported floating-point error is roundoff, outside that input-only bound.

## Preserved omission survivor

Set W to gY, deleting only 2g_u I_P, while preserving X,B and the underlying physical fields. Both exact modal and augmented matrices have rank 12. The unused-row relative residual is 4.45e-15, below the predeclared 1e-8 threshold. This is an exact model-fit survivor, not merely a tolerance accident. It yields beta_fit=0, C_fit=.4, d_fit=2, e_fit=3.8 at the shell. Comparing these with the generator would expose the error, but that is not an observational rejection and is not counted as one here.

For this mutant, the first-order equations still imply an elimination identity without B terms. Expanding it gives fitted histories

    beta_fit=0, C_fit=C-beta, d_fit=d, e_fit=e-d beta,
    k_fit=k+2 beta.

This explains the exact survivor. The fitted histories need not satisfy the candidate's other constraints. For the affine reception gain beta'=-h beta-beta², K_fit=C_fit'+h C_fit=K+beta². Therefore the separately observable coefficient relation K_fit'/K_fit=k_fit is not automatic.

## Explicitly adaptive unused-residual checks

These checks were added after the frozen protocol exposed survival. They are not retrospectively called predeclared. At the same eta=-2, exact independent solves at r=.9 and1.1 still fit all angular rows but yield

    C_inner=79/198, C_outer=81/202,
    e_inner=376/99, e_outer=384/101.

Thus C_outer-C_inner=20/9999 and e_outer-e_inner=40/9999. The required homogeneous background fails. These are differences of data-inferred coefficients, not differences from known generator coefficients.

As a further original-equation check, use the inferred coefficient histories at reference shell r=1 and freeze them spatially before taking spatial derivatives. With G=2/d, reconstruct q=h-(e-1)/d, R=CG, B=q/G, x=sqrt(qG), b=sqrt(B), ell=h-q. Integrate A'/A=q with A=1 at the evaluation point, then reconstruct H_E=Aell, v=Ax, r_E=A²R, rho=AR and V=A²(3ell²-x²/2-R). These use the candidate reconstruction and supplied a,h; no generator truth is used as a residual target.

At eta=-2,r=1 the original residuals are:

| Equation | Residual |
|---|---:|
| Friedmann (used to define V) | 0 |
| Raychaudhuri | -3/5 |
| Original scalar background | 127 sqrt(65)/650 |
| Bare-dust background transport | -1/50 |
| K_fit'/K_fit minus inferred k_fit | -16/65 |

For the n=0,ell=2 angular component, reconstruct Z=-N/K, J=d(P'+ell P)+CZ, scalar perturbation J/b, and density from the Hamiltonian equation, using these same inferred histories. The original Euler residual is -3473/338, bare-dust continuity is -113629/351520, and corrected-redshift residual is -123/26. The full finite field cannot cancel these in its independent ell=2 sector. Momentum/Hamiltonian are reconstruction definitions here; their satisfaction alone is not evidence. Because the background already fails, these are additional inconsistency diagnostics, not a valid alternate action. This supplement does not claim to enumerate every perturbation-equation residual.

The independent script robustness_original_residuals.py records the exact reconstruction, derivatives and equation evaluations. These tests reject this omission under the supplied calibrated continuum/background contract. They do not prove that every gain omission or every alternative physical model is identifiable. Cross-shell homogeneity, temporal coefficient consistency and the original background/dust equations remain essential acceptance obligations. Rank attainability is a conditional mathematical milestone, not empirical validation, primitive-noise robustness, generic conditioning or a global uniqueness theorem.
