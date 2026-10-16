# V3 domain and author-source correspondence confirmation

Reviewer: `/root/localized_history_check`. Direct scientific authorship remains
with `/root`. This is a new immutable scoped confirmation; it does not amend the
v1 Gram review, the v2 mass/error supplement, or any original source/result.
No audit verdict, combined landing verdict, branch mutation or publication is
performed here.

## Coverage and independent execution

I read the complete DERIVATION_v2 note, then the complete v2-to-v3 diff and full
DERIVATION_v3.md (129 lines). I read all 156 lines of residual_energy_check_v1.py
and the author result metadata and all 149 control entries. I verified every
recorded numerical error is finite and within its stored tolerance, every
Boolean control is true, and the source/note hashes in the result match the
unchanged v1 implementation and v2 note on disk.

The author implementation was not imported, executed or rerun by this reviewer.
Its top-level code writes a result file, so reading it rather than importing it
also preserves the author's output. The author results remain 149 author
synthetic controls, not independent executions by this reviewer. They bind v2,
not v3. The 110 original and 59 new reviewer controls were completed before
access to that implementation and remain distinct records. A wording/domain
confirmation of v3 is not represented as execution against v3.

## Author's v3 repairs

The complete diff adds square-integrability of f_i, so the raw entries
B_ij=integral f_i.f_j/(6pi) are finite. It explicitly treats B as an auxiliary
matrix for bounded contrasts, rather than asserting boundedness of raw velocity
readouts. It restricts full-space inverse-root whitening to positive-definite B,
all energy divisions to positive q, and the scalar contrast division to positive
c^T B c. It replaces zero-response divisions with compatibility conditions,
requires positive Q_J/G_bare/G_meas in the physical conversion and keeps singular
feasibility rather than silently dropping unsupported components. It also makes
the T_{i+1} denominator unambiguous and includes the general singular nuisance
quotient with its proof.

These changes resolve the missing-domain finding preserved in
V2_DOMAIN_FINDING_v1.json. They leave the formulas exercised on the positive
matrices in both existing suites unchanged. In particular, positive quotient
rank does not imply raw B invertibility, and the note now makes this distinction.
The added singular nuisance statement follows by applying the same Hilbert
observation theorem to C A; no additional state-selection premise is introduced.
The compact-weight, positive-mass, fixed-point and supplied-calibration limits
remain essential.

## Implementation correspondence

The closed Gram implementation at lines 25-26 and inverse/spectrum/cross-term
controls at lines 57-65 match G=L/(6pi T^3) and E_min=r^T G^-1 r/2 from the
original independent derivation. The explicit joint two-window cost
18.84955592153876 differs from the diagonal-only cost 9.42477796076938; the
negative neighbor overlap cannot be discarded as an independent-window budget.
The unequal-window and count-kernel sections were read in full for source
correspondence; their detailed focused independent review belongs to the
separate count-kernel reviewer and is not claimed as new controls here.

Lines 94-112 implement positive-definite nuisance quotients, direct weighted
least squares, symmetric whitening and error-ball minimization with consistent
1/2 energy factors. The optimizer uses a Euclidean ball in already whitened
coordinates, which is equivalent to the displayed ellipsoid. Its tested radius
is 0.4 times the projected norm. The new independent extension additionally
checks zero/large radii, dependent nuisance columns and optimization in original
coordinates. The singular fixture correctly checks membership in range(G),
including the false-zero result from a pseudoinverse without feasibility. The
script does not by itself test every singular nuisance quotient; the original
independent proof/control supplies that scope. No code path silently evaluates
B^(-1/2) on a singular example.

Lines 113-132 are actual smooth Fourier-field constructions, not only evaluation
of the closed matrix formula. For a chosen spatial direction, the represented
initial data are the real KG Riesz fields multiplied by
chi(k)=exp[-eps(k^2+k^(-2))], with the zero-frequency value extended smoothly.
This removes both ultraviolet and infrared singularities. The unitary spatial
Fourier factor is (2pi)^(-3); angular integration contributes 4pi/3. The resulting
radial measure k^2/(6pi^2) is exactly the massless gradient-energy measure.
G_chi uses one filter while field energy uses chi squared. Real coefficients
and the Riesz fields' conjugate symmetry produce real initial data. The
positive-definite filtered observation matrix fixes the coefficients, and the
subsequent independent time integration applies the hat observations to the
constructed evolving field. This matches the analytic smooth-approximation
argument and the independently constructed fields in GRAM_REVIEW_v1.

The four author energies are approximately 3.643531, 2.992355, 2.752953 and
2.620753 versus the energy-class infimum 2.450442. Recorded residual errors are
below 1.64e-15. Those finite quadratures show a decreasing excess for the four
chosen filters; they do not alone prove convergence for every filter family or
exact equality in the continuum. Smooth exact-constraint approximation follows
from the separate density/finite-rank argument. Finite numerical quadrature and
truncation are not interval-certified field reconstructions.

Lines 133-137 check the odd angular moment of a radial Gaussian's gradient and
its positive massless energy 3pi^(3/2)A^2/4 for width one. Rotational invariance of
free evolution preserves the vanishing center gradient, so this is a valid
specific invisible-field witness. It is not a broad theorem about actual
observations, nonlinear fields or arbitrarily large physically admissible energy.
The original independent review gives the more general width/mass formula and
explains the orthogonality and finite-observation kernel limits.

Lines 138-146 use a common positive finite frequency quadrature. Its matrices
have the correct coefficient (omega^2-mu^2)^(3/2)/omega and compare each massive
matrix with the massless matrix on the same discrete grid. This tests the
positive-quadratic-form enclosure at finite quadrature, not an error-certified
infinite integral. Despite the section comment, it does not explicitly form a
mixed-mass sum. The direct-sum analytic proof and separate reviewer mixture
controls cover that new claim; the 149 author controls must not be described as
including a numerical mixed-mode sum they do not compute.

Lines 147-153 implement E_phi=2Q_J E_tot with q>0 and
G_bare=1/(8pi Q_J), then the q<1/3 and G_meas>=G_bare lower bound. The factors
match the independent algebra. Randomly supplied positive Q, q and G_meas
exercise that conditional formula; they are not measured gravity tests. The
result correctly records measured_gravity_tests=0 and fitted_parameters=0.
The author script has no componentwise-box error control; the componentwise
inequality is covered by the new independent proof and two box optimizations.

## Source/result correspondence and remaining limits

No additional mathematical discrepancy was found in the inspected scope after
the explicit v3 repairs. This is not a guarantee beyond that scope. Full physical
ODF-to-velocity/force calibration, retarded observation geometry, moving-path
response, environmental/frame identification, initial-state resource bounds,
actual error covariance or deterministic radii and a physical upper energy
budget remain open. The invisible-energy statement stays within the supplied
infinite-dimensional linear KG model. The minimum-energy field is a variational
reconstruction, not a selected physical initial condition. No raw/held-out data,
empirical test or new fitted value was accessed or created by this reviewer.

Source identities:

- DERIVATION_v2.md: 1e31731ea505da305b4a6250a63aa0b2b6c85909eb4f89b56e244ee37e9e02e1
- DERIVATION_v3.md: 1eca5b9a13278c819e221955518150cbcc44e4a9d012fbcba85db8df08dc707f
- residual_energy_check_v1.py: 8ce220112159929fc05bbfa2e532f2263cf3a94293742dc2319836fb3738127d
- AUTHOR_RESULTS_v1.json: cb2f36aaab8cb6d81cb8431e594cc469281f9ec7f77b461b04cd2eba4d6b654f

V3_SOURCE_CONFIRMATION_IDENTITY_v1.json binds this report, the exact complete
diff, source files, original review and separate mass/error supplement. No
original reviewer report was replaced and no source/state/index/lock was edited.
