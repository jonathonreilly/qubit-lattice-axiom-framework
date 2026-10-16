# Focused independent geometry-transport check

The two conservative gradient constants, admissible-path argument, product-mass
transport inequality and complex/real harmonic conversion are valid under the
stated hypotheses. No mathematical correction is required in the checked note.
This is conditional support for a missing geometry certificate, not apparatus
validation, an empirical uncertainty region, new theory or a formal audit.

Checked note: `LAB_GEOMETRY_TRANSPORT_v1.md`, SHA256
`ebecac4abf41d8757eeefc3c188498d4acfa3419a093b32f3bf19c49df885991`.
Reproduced runner: `check_lab_geometry_transport_v1.py`, SHA256
`212ce9574ffc18cbf9cc0a9079d4f1fa1e819b88a71bdaec739733529ebf8c32`.
The independent derivation, fixtures, implementation and actual output were
frozen before any author runner/results were read. That output freeze has
SHA256 `8302ca224cc64e97ff476d4eabe4d2f0059eda5132e07e5c091743775027f164`.
The lossless source snapshots, final binding and manifest preserve the sources
and execution order; author files were not edited.

An alternative proof uses `g(r)=exp(-mr)/r` and
`K=-(Jx).gradient_y g`. Its radial Hessian eigenvalues are

    lambda_r = exp(-mr)[(mr)^2+2mr+2]/r^3,
    lambda_t = -(1+mr)exp(-mr)/r^3.

For m>=0, the Hessian norm is lambda_r. Consequently
`|gradient_y K|<=L lambda_r` and
`|gradient_x K|<=r h+L lambda_r`. Since
`lambda_r<=exp(-mr)(mr+2)^2/r^3`, these imply the printed bounds after
monotonicity replaces r by d. Symbolic derivatives verify monotonicity through
positive-coefficient polynomials, including m=0. Complex-step derivatives of
the original kernel agree with the Hessian expressions at independent points.
The extra x term is necessary: at x=0, its lever is zero but the x gradient
need not vanish. The printed constants are conservative, not optimal.

The uniform path certificate is essential to this proof. The triangle estimate
`d0-epsilon_A-epsilon_B>0` and convexity of the endpoint transverse lever justify
straight interpolation. Two endpoints at separation 1 can have zero midpoint
separation; the corresponding one-atom unconstrained transport distance is
finite although its sole straight path is inadmissible. This is a counterexample
to endpoint-only certification, not an assertion that every possible endpoint
inequality fails. Infima may replace first moments only in a common compatible
admissible class with uniform constants, as the note stipulates.

A distinct split coupling with masses 2.4 and 1.7 checks the mass factors:
integrating a displacement of A against the product measure contributes
`M_B D_A`, and the B term contributes `M_A D_B`. D values are mass-weighted
first moments. The independently certified vertical gap and lever apply to
all rotations, not merely the sampled angles. Numerical samples support the
point, product-integral and harmonic inequalities; they are not a proof of
unsampled apparatus geometry.

For nonzero Fourier harmonics, sine/cosine coefficients and real amplitudes
carry the factor two. The amplitude difference also obeys the reverse triangle
inequality. A generic bounded test function `sign(cos phi)` has complex first
coefficient `2/pi` and real cosine coefficient `4/pi`, demonstrating why a
complex envelope cannot simply be reused as a real envelope. This waveform is
not claimed to be an apparatus response. A separate signed-contrast example
has zero net mass but torque `8/27`, confirming the net-mass shortcut is invalid.

Exact-rational SI conversions reproduce the source's deliberately stipulated
scale illustration:

| m, per meter | Complex envelope, N m | Real envelope, N m |
| ---: | ---: | ---: |
| 0 | 1.027483097823e-10 | 2.054966195646e-10 |
| 20000 | 8.617181992343e-11 | 1.723436398469e-10 |

The displacements, reference coupling and unit strength remain stipulated.
These envelopes neither estimate actual corrections nor supply a confidence
region or exclusion. No measured harmonic was used as a comparison target.

The independent run passed **63 controls**, including two source-binding
checks, in **0.423 s**. The unchanged author runner then passed **366 controls**
in **0.365 s**; all 51,426 stdout bytes match the stored receipt, SHA256
`74730ce6ebf6c899287905fb26a86d6baa3fee417b5ecfe41fde996785572a77`.
Both runs used `-B`, `PYTHONDONTWRITEBYTECODE=1` and an external 120 s timeout.
Complete stdout/stderr, commands, timings, CPU/memory costs and before/after
hashes are preserved. No process failed or timed out; sources and independent
freeze artifacts stayed unchanged.

The remaining obligation is an independently justified actual mass
correspondence and uniform displacement/gap/lever certificate over the relevant
angular readout. A marginal metrology error does not provide it. Positive equal
masses, a fixed torque axis and the stated material/source response remain
premises; unequal masses and signed contrasts need their separate terms or
decompositions. Successful support checks do not fill any of those inputs.
