---
claim_id: weighted_phase_corrector_and_magnetic_gram_certificates_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
runner: scripts/weighted_phase_corrector_and_magnetic_gram_certificates_check_2026_09_16.py
upstream_dependencies: ["docs/FINITE_BOX_ELECTRIC_OFFSET_RESPONSE_AND_TAIL_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md"]
claim_scope: "03: exact weighted phase-corrector variational identity and magnetic Gram lower-bound certificates. Cube-kernel witness excludes the stated whole-space comparison, not all possible correctors. One-plaquette harmonic-mean normalization is correct."
---

# Weighted phase correctors and magnetic Gram certificates

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Scope and provenance

03: exact weighted phase-corrector variational identity and magnetic Gram lower-bound certificates. Cube-kernel witness excludes the stated whole-space comparison, not all possible correctors. One-plaquette harmonic-mean normalization is correct.

The complete original mathematical argument follows. Its personal reading, timing, proposal and review statements describe historical work, not a new review or current execution. Model parameters are supplied. No PR8160, PR8162 or PR8163 result is implicitly a premise. Narrow quantitative bounds and explicit witnesses do not supply a broad negative certificate or a physical phase. No five-route no-go PASS is asserted.

Actual mathematical dependencies:

- [Finite-box electric offset response and factorial tail bounds](FINITE_BOX_ELECTRIC_OFFSET_RESPONSE_AND_TAIL_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md).

## Complete argument

# The electric response as an exact weighted phase problem

Working personal derivation, 2026-09-16. The finite-volume identities below
concern the supplied pure-gauge rotor Hamiltonian of BLOCK02. They do not
prove its thermodynamic phase. Ground-state transforms, spectral Cauchy
inequalities and conductivity cell problems are established machinery; the
purpose here is to identify their exact carrier and the missing uniform
estimate, without claiming a new general principle.

## 1. Exact phase corrector

Let Q be the compact physical configuration torus of a connected contractible
free spatial box, obtained from link angles by quotienting vertex gauge
transformations. Use normalized Haar measure. Gradients below use the metric
inherited from the link kinetic energy, so their values lie in ker D. The
constant vector f is a nonzero real vector in ker D. The zero-offset ground
wavefunction Psi on Q is real, smooth and strictly positive, normalized by
integral Psi^2=1. Set p=Psi^2 and write averages with density p as <.>_p.

The ground-state transform gives the exact quadratic-form identity

    <Psi u,(H_f(t)-E0)Psi u>
       =(g^2/2) integral p |gradient u-i t f u|^2.       (1)

For smooth periodic u this follows by expanding the kinetic form and using
the equation for Psi; density extends it to the form domain. In particular,
the offset does not change the positive weight p in this identity. Minimizing
(1) over complex u of weighted norm one gives e_f(t)-E0.

The simple ground eigenvector at t=0 is u=1. Its first-order change can be
chosen purely imaginary because complex conjugation sends t to -t. Expanding
u=1+i t b+O(t^2), with b real and periodic, gives

    e_f''(0)/g^2
       = min_b <|f-gradient b|^2>_p,                  (2)

where b is taken modulo constants. This is an equality, not just a phase
trial upper bound. To verify the equality directly, the positive smooth
weight on the finite compact torus makes the weighted gradient form coercive
on mean-zero H^1 functions. Its unique minimizer solves

    integral p gradient b dot gradient v
       = integral p f dot gradient v                 (3)

for every real periodic v. Equation (3) is precisely the imaginary
first-order ground-state perturbation equation obtained from (1). Substituting
that derivative gives (2). A real first-order change has only its nonnegative
gradient cost and no linear forcing, so cannot improve it.

Consequently the quantities in BLOCK02 have the exact expressions

    rho_f = min_b <|f-gradient b|^2>_p / |f|^2,
    eta_f = sup_b [2<f,gradient b>_p
                         -<|gradient b|^2>_p] / |f|^2. (4)

The second expression is the squared norm of the orthogonal projection of
the constant vector field f onto weighted square-integrable periodic
gradients, divided by |f|^2. It is also the variational electric susceptibility.
It is not an ordinary spatial conductivity: the cell is the many-link
configuration torus and its weight is the exact interacting ground density.

At every fixed finite box, p_min>0. The unweighted average of a periodic
gradient is zero, so (2) gives rho_f>=p_min>0. The electric-coordinate
positivity argument in BLOCK02 gives eta_f>0, hence 0<rho_f,eta_f<1 for this
nonzero cycle f. The lower bound p_min has no claimed volume-uniform control.

For any real smooth periodic magnetic observable B, optimize the scalar
trial b=a B in (4). If J_B=<f,gradient B>_p and
Q_B=<|gradient B|^2>_p>0, then

    eta_f >= J_B^2/(|f|^2 Q_B).                       (5)

The same bound follows independently from the spectral inequality
|<[A_f,B]>|^2<=4 m_-1(A_f) m_1(B), with
m_1(B)=(g^2/2)Q_B and m_-1(A_f)=eta_f|f|^2/(2g^2).
Thus the phase and spectral normalizations agree.

## 2. The exact magnetic Gram matrix

For B_h=sum_p h_p sin F_p, define G=C C*, m_p=<cos F_p> and

    ell_p=(Cf)_p m_p,
    M_pq=G_pq <cos F_p cos F_q>.

Then J_B=ell dot h, Q_B=h* M h, and (5) yields

    eta_f >= ell* M^+ ell/|f|^2.                     (6)

Here M^+ is its Moore-Penrose inverse. The numerator ell annihilates ker M:
a zero weighted gradient norm makes the gradient zero, hence J_B=0.
This verifies the compatibility needed when optimizing a singular matrix.

More generally take any finite family of integer physical cycles a_alpha,
use B_alpha=sin(a_alpha dot theta), and put

    mu_a=<cos(a dot theta)>,
    J_alpha=(f dot a_alpha) mu_(a_alpha),
    Q_alpha,beta=(a_alpha dot a_beta)
                  [mu_(a_alpha+a_beta)+mu_(a_alpha-a_beta)]/2. (7)

Equation (6) holds with J,Q. All mu_a are exact shift overlaps of the positive
electric ground vector. Enlarging the test family can only increase this
lower bound; a dense collection of characters recovers (4) in the limit at
each fixed finite box. No convergence rate uniform in volume is supplied.

If h happens to satisfy C*(m h)=f, decompose its denominator exactly as

    h* M h=|f|^2+
       sum_pq h_p h_q G_pq Cov(cos F_p,cos F_q).      (8)

This covariance quadratic form is nonnegative: it equals the mean squared
norm of C*[h(cos F-m)]. Controlling it by a constant times |f|^2 would prove
a useful uniform lower bound. A bound by a constant times |h|^2 alone is
insufficient for low spatial frequencies, where solving for h costs an
inverse curl. Thus a small local flux variance alone does not close TARGET.

## 3. A cube check that forbids one shortcut

The tempting estimate M<=K C C* with a finite scalar K cannot hold on the
whole plaquette space, even at one finite cube and arbitrarily weak positive
coupling. Let z be its signed oriented boundary, so C*z=0. Choose nonzero
small a and a plaquette flux with signed face values

    z_p F_p = (a,a,-2a,0,0,0).

Their sum vanishes, so this real F belongs to im C and is realized by link
angles. But z_p cos F_p is not a multiple of z: its factors include cos a,
cos 2a and 1. Since a single cube has ker C*=span(z),
C*(z cos F) is nonzero. It remains nonzero on an open set, and the exact
ground density is positive there. Hence z* M z>0 although z* C C* z=0.

This is a counterexample only to that whole-space matrix comparison. It
does not rule out a bound after choosing representatives or optimizing cube
components, a nonlocal nonlinear corrector, a defect expansion, or a phase.
The linear Bianchi identity for F does not become a linear Bianchi identity
for sin F. The exact periodic observables in (7) keep the correct identities.

## 4. A solvable one-plaquette normalization check

For one plaquette, use its flux angle x in [-pi,pi) and normalized measure
dx/(2pi). The scalar Hamiltonian is

    H=-2g^2 partial_x^2+(1-cos x)/g^2.

For f=c_p/4, |f|^2=1/4 and gradient b=c_p b'(x).
Solving (3) makes p(1/4-b') constant. Periodicity gives exactly

    rho_f = 1 / integral p(x)^(-1) dx/(2pi),
    eta_f = 1-rho_f.                                (9)

The normalization integral p=1 is essential. This harmonic-mean identity is
finite dimensional and establishes neither a spatial phase nor a universal
large-volume bound. It supplies a distinct check against the inverse-spectrum
formula of BLOCK02 and against direct offset-energy curvature.

## 5. What has become testable

The open phase question has a concrete variational sufficient condition:
construct periodic physical correctors b_L for low-curl transverse f_L with

    2<f_L,gradient b_L>_p-<|gradient b_L|^2>_p
         >=eta_* |f_L|^2, eta_*>0 independent of L.   (10)

The weight must be the actual fixed-g ground density. A harmonic reference,
finite-volume convergence of a test basis, or independent plaquette
concentration cannot be substituted for (10). The derivation supplies a way
to challenge and improve candidate correctors, not a claimed solution of
their many-body bound.

## Review and proposal status

The [claim-status contract](work_history/review_loop/pr8164/README.md) and
[premise inventory](work_history/review_loop/pr8164/README.md) apply to this author
proposal. The [negative-claim checklist](work_history/review_loop/pr8164/README.md)
records the scoped comparison restrictions and untested alternatives.
Independent review, formal registration and retained landing are pending.


## Canonical evidence boundary

[Program](../scripts/weighted_phase_corrector_and_magnetic_gram_certificates_check_2026_09_16.py); [current stdout cache](../logs/runner-cache/weighted_phase_corrector_and_magnetic_gram_certificates_check_2026_09_16.txt). The canonical TOTAL counts 3 completed finite control families, not each loop iteration or an analytical theorem. All original assertion expressions and tolerances are retained. No canonical capture has run during preparation. Historical outputs, failed refinements and mutations remain in the [exact recovery archive](work_history/review_loop/pr8164/README.md).
