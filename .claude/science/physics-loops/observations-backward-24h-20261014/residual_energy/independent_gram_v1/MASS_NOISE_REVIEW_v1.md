# Focused independent mass, nuisance and error extension

Reviewer: `/root/localized_history_check`. Direct scientific authorship remains with `/root`.
This immutable supplement preserves the checks of DERIVATION_v2 separately from the
previous 110-control Gram review. It is a scoped mathematical/source assessment, not
an applied audit verdict, a combined landing verdict or empirical validation.

## Reading and execution boundary

The reviewer read the complete v2 note, saved the missing-domain finding and the
extension proof in MASS_NOISE_PRECHECK_v1.md, and executed 59 new independent
controls before opening residual_energy_check_v1.py or AUTHOR_RESULTS_v1.json.
The original 110 controls were not rerun. The precheck was written after reading
the v2 mathematical claims; it is an independent derivation of those claims, not
an assertion of blind topic discovery. Its formulas were not copied from author
code. Later implementation/v3 correspondence is recorded in a separate report.

The v2 snapshot is preserved byte-for-byte. The earlier GRAM_REVIEW_v1.md and
GRAM_REVIEW_IDENTITY_v1.json remain unchanged. Their initial-state reconstruction,
real-data, energy-completion, smooth approximation, singular feasibility and
invisible-field arguments are not superseded by this supplement.

## Matrix mass enclosure

For compact real vector weights W_i at the same fixed spatial point, form
V=sum_i b_i W_i for any real coefficient vector b. The real KG energy inner
product, with norm squared 2E, gives

    b^T G_mu b = (1/(6 pi^2)) integral_0^infinity
        a_mu(omega) |Vtilde(omega)|^2 d omega,
    a_mu(omega) = (omega^2-mu^2)^(3/2)/omega for omega>=mu,
                 0 otherwise.

For nonnegative mass, 0<=a_mu<=omega^2, including the zero-frequency limit.
Thus 0<=G_mu<=G_0 in the Loewner sense. Parseval gives
G_0(W,V)=integral W'.V'/(6 pi), with the same unitary spatial-Fourier and
un-normalized temporal-transform convention as the earlier review. The angular
factor 4pi/3 contracts vector components; it assumes no isotropy of the initial
field. The inequality is about every real quadratic form, not every matrix entry.

Independent modes lie in a direct-sum real energy space. The combined observation
representer has components alpha_j g_j, so its exact Gram is
sum_j alpha_j^2 G_mu_j <= q G_0, q=sum_j alpha_j^2. There are no cross-mode terms
in this specified independent, common-normalization model. Finite modes suffice;
an infinite direct sum additionally needs a well-defined bounded response and
finite q. No covariance or interaction between modes is inferred.

For H_0=C B C^T positive definite and q>0, every consistent contrast z obeys
|b.z|^2<=2 E_tot q b^T H_0 b. Taking b=H_0^-1 z proves
E_tot>=z^T H_0^-1 z/(2q), without inverting a potentially singular actual
massive Gram. Equality as a least-energy statement is restricted to the supplied
massless response, not a general massive response. The proof uses a common fixed
spatial point and common time weights across masses. Moving-worldline phases and
the full conformal force require their own operator or enclosure.

## Weighted nuisance quotient and deterministic errors

For positive-definite B, supplied nuisance design Z, and a full-row-rank C with
ker(C)=range(Z), the row span of C B^(1/2) is the orthogonal complement of
range(B^(-1/2)Z). Writing P for that orthogonal projector gives

    C^T(C B C^T)^(-1)C = B^(-1/2) P B^(-1/2),
    (Cy)^T(C B C^T)^(-1)(Cy)
      = min_beta (y-Z beta)^T B^(-1)(y-Z beta)
      = ||P B^(-1/2)y||^2.

Dependent columns of Z are interpreted by their span. The identity is valid
also when nuisance columns span the whole observation space: the minimized
residual then vanishes. It supplies a quotient, not a physical nuisance prior.

For a declared error ellipsoid ||B^(-1/2)e||<=rho, rho>=0, projection is
contractive. The exact minimum residual norm is
max(0,||P B^(-1/2)y||-rho). It is attained by a whitened error parallel to the
projected data, with length min(rho,||P B^(-1/2)y||). This includes zero radius,
a ball containing the projected data, and a zero projected residual. Multiplying
its square by 1/(2q) gives the mass-enclosure energy lower bound. This is an
exact minimized residual norm, not an asserted exact energy for arbitrary masses.

For supplied component bounds |e_i|<=eta_i with eta_i>=0, a contrast c that
annihilates Z satisfies |c^T(y-e)|>=max(0,|c^T y|-sum |c_i|eta_i). Dividing its
square by 2q c^T B c is valid only for q>0 and c^T B c>0. A zero-Gram contrast
instead imposes compatibility |c^T y|<=sum |c_i|eta_i. The q=0 response has no
scalar signal in any contrast; errors/nuisances must explain the data.

## Preserved missing-domain finding

V2 wrote B^(-1/2) without requiring B positive definite, although the preceding
raw Gram construction allowed singular B. A positive quotient alone does not
repair this: B=diag(1,0), Z=(0,1)^T and C=(1,0) give C B C^T=1 while B remains
singular. V2 also said the component bound held for every annihilating contrast,
without excluding c^T B c=0, including c=0. Those expressions are undefined
outside their stated positive denominators, rather than counterexamples to the
positive-definite formulas. The finding was sent to root and preserved in
V2_DOMAIN_FINDING_v1.json; no hidden regularizer or unsupported pseudoinverse
was used. The following v3 confirmation records the author's explicit repair.

The original singular nuisance extension remains useful: for general positive
semidefinite G and ker(C)=range(X), feasibility is C r in range(C G C^T), and
E_min=(C r)^T(C G C^T)^+(C r)/2. Applying the original bounded observation theorem
to C A proves this directly. An unconstrained minimization of a G^+ quadratic
form without feasibility can falsely return zero for an impossible residual.

## Physical conversion and limits

If Q_J>0, q>0 and the supplied constant-frame normalization holds,
E_phi=2 Q_J E_tot and G_bare=1/(8pi Q_J). The coefficient is therefore
Q_J/q=1/(8pi G_bare q). Under the additional candidate ceiling q<1/3 and
same-environment relation G_meas>=G_bare>0, the weaker coefficient
3/(8pi G_meas) follows. For diagonal B_ii=1/(6pi T_i), the resulting coefficient
of the duration-weighted residual variance is 9/(4 G_meas). These are conditional
conversions. This reviewer does not rederive the entire candidate action,
ceiling or environmental identification here, and no measured normalization,
SI value, energy upper budget or error radius is obtained from these formulas.

## New independent numerical evidence

The new script has 59 successful controls, separately recorded from the earlier
110. It uses vector hats with widths [1,1,0.7,1.3], unequal centers and distinct
directions. Exact piecewise time-domain derivative overlaps are compared with
finite positive spectral quadrature to cutoff 800 for masses 0,0.4,1.7,6.
The massless omitted trace is approximately 0.00082629, below the analytic tail
upper bound 0.00220038. The bound follows from |hat transform|<=4/(T^2 omega^2).
These are ordinary floating-point quadratures; neither the displayed errors
nor the tail comparison is an interval-certified infinite-integral computation.
The analytic coefficient argument supplies the general theorem.

A concrete control shows why entrywise comparison is invalid: one massless
cross entry is -0.0530516476973 while the mass-6 entry is -0.00683030057477,
even though the Loewner enclosure holds. A three-mode mixture with coefficients
[-0.2,0.7,1.1] checks the sum and energy comparison for three residual vectors.

Separate non-diagonal positive matrices of sizes 4 and 6 and redundant nuisance
columns are checked by quotient, direct Cholesky-weighted least squares and
symmetric whitening. The error solution is compared with SLSQP optimization
over the unwhitened ellipsoidal error and nuisance coefficients, using zero,
0.35 and 1.4 multiples of the projected norm. All executed optimizer controls
succeeded; the largest reported optimized-cost discrepancy is about 6.2e-14.
Componentwise bounds are checked against a joint box-constrained nuisance/error
optimization. Full nuisance span, singular-raw/positive-quotient, zero-response
compatibility and two physical conversion cases are included.

No actual measurement, held-out record, physical energy calibration or fitted
parameter entered these controls. The vector-kernel/unequal-window derivation
was read for context, but its separate focused author/peer check must not be
relabelled as part of these 59 controls. No scientific suite was rerun merely to
increase the count, and no broader no-go or theory-wide exclusion is asserted.

## Exact artifact identities

DERIVATION_v2.md and DERIVATION_v2_SNAPSHOT.md:
1e31731ea505da305b4a6250a63aa0b2b6c85909eb4f89b56e244ee37e9e02e1

MASS_NOISE_PRECHECK_v1.md:
ac6a47cdd9e654f3ae70f594f64e69921dae8a95062ed4058c9ee85a26db70cd

independent_mass_noise_check_v1.py:
aa61e5592a5c1d62d628be9403666f6ba3cc9c85e6171a402831d4c58c390a0e

INDEPENDENT_MASS_NOISE_RESULTS_v1.json:
a78dc04470cd8f2919c7c1aab55451bb8d12e96c0eadc458942016e5b930db0c

V2_DOMAIN_FINDING_v1.json:
c6e0f951b08e0f872dcdaaf00eeccd01e11a05d679a172f58be0600ee5975027

The accompanying MASS_NOISE_REVIEW_IDENTITY_v1.json binds these files, the
separate original review and this report. It does not hash itself.
