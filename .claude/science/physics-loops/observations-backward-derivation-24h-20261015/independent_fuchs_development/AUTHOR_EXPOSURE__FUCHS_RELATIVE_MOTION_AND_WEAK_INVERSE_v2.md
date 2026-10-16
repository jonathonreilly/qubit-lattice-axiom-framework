# Relative motion and an initial-state-free weak observation equation

Status: conditional-support. These standard mechanical and adjoint identities
confront an actual measurement-chain gap. They neither select a scalar action
nor establish an apparatus identification.

Source: [Fuchs et al., arXiv2303.03545v2](https://arxiv.org/html/2303.03545v2).
Exact reading scope and source identities: FUCHS_PRIMARY_REVIEW_v1.json.
The development file has nine labeled streams: three amplitudes, three phases
and three oscillator frequencies. Demodulators2 and3 share the reference
26.6992697817Hz. Wiring identities and filter settings are not in those labels.
Receiver2/source3 and the reverse assignment are diagnostic hypotheses;
a better fit does not independently establish either wiring assignment.

## Relative motion and calibration

Let q=x-X be test-body displacement relative to its support. Adopt a reciprocal
linear spring/damper k,c between test mass m and support mass M, and support
stiffness K,damping C to a fixed inertial base. Let g_t,g_p be external
accelerations and f_p a further support force. An internal calibration force
f acts on the test body with equal opposite reaction on the support:

    m(q''+X'')+c q'+kq = m g_t+f,
    M X''+C X'+KX-c q'-kq = M g_p+f_p-f.                 (1)

For exp(i omega t), define Z=k+i omega c, D=Z-m omega^2,
P=K-M omega^2+i omega C, and Delta=DP-m omega^2 Z. When Delta is nonzero,

    q = [mP g_t+m omega^2(M g_p+f_p)+(P-m omega^2)f]/Delta. (2)

Dividing the source-driven response by the internal-force calibration, when
P-m omega^2 is nonzero, gives

    f_equiv = m[P g_t+omega^2(M g_p+f_p)]/(P-m omega^2).   (3)

It is not m g_t unless support contributions are independently bounded.
For K=C=f_p=0 and uniform g_t=g_p, the particular relative response vanishes.
Homogeneous relative motion need not vanish. A small support displacement
can still produce important acceleration. A small m/M alone does not bound a
relative correction near a narrow sensor pole.

The two-body support is a candidate class, not a model inferred for this
multi-body apparatus. Selecting K,C,M to reproduce a published normalization
does not derive them. Calibration with reaction elsewhere has a different
numerator; its physical force path must be established.

With the calibration force off (f=0), the calibrated relative coordinate obeys

    g_t = q''+gamma q'+omega0^2 q+X''.                   (4)

For any proposed smooth g_t on a finite record, an unmeasured X'' can be chosen
as the difference in(4), then integrated twice. This restricted missing-channel
ambiguity does not exclude experiments with independently measured support
motion, geometry or transfer.

## Weak observation equation

Suppose the real coordinate is Re[z exp(i Omega t)], with a known constant
positive carrier Omega and a registered forcing envelope u. In one linear
mode, take

    z''+(gamma+2i Omega)z'
       +(omega0^2-Omega^2+i gamma Omega)z=2i Omega b u.  (5)

Complex b includes unresolved gain, force and phase conversion. Put
a=-gamma/2 and nu=(omega0^2-Omega^2)/(2 Omega). For a real compact window
with w=w'=0 at both endpoints, define

    Cw=integral w z, Dw=integral w' z, Ew=integral w'' z,
    Uw=integral w u,
    Rw=-Dw-i Ew/(2 Omega), Bw=Cw+i Dw/Omega.

Integration by parts twice gives exactly

    Rw=a Bw+i nu Cw+b Uw.                              (6)

Initial displacement, velocity and homogeneous amplitude need not be supplied
or subtracted as a fitted decay. This is conditional elimination of initial
state, not derivation of the linear class, instrument state or unobserved-mode
history. Nonlinearity and changing coefficients can invalidate(5).

Each window gives two real rows in (a,nu,Re b,Im b), with complex columns
(Bw,i Cw,Uw,i Uw). Full real column rank gives at most one exact solution when consistent,
or a unique least-squares estimate. It does not establish model consistency;
rank loss and conditioning must be reported. For z proportional
to a monochromatic u, the four coefficients are not separately identified.
No finite-noise precision guarantee follows from algebraic uniqueness.

Omitting Ew/(2 Omega) and Dw/Omega gives a conventional first-order comparison;
the full equation remains primary. Variable source frequency can reside in u.
A varying demodulation carrier would require extra known derivative terms.

## Remaining measurement premises and planned diagnostics

A common time-invariant linear filter on both sides commutes with the operator
on full histories with compatible boundary handling. Different unknown
filters generally do not. Compact windows do not remove arbitrary instrument
transients or missing channel registration.

A fixed source geometry predicts force harmonics from rotor phase. Photodiode
amplitude is not calibrated source force. Its unit phasor and measured voltage
phasor are different input hypotheses; neither is silently promoted to a
physical force map. Small source amplitudes can corrupt phase. Keep all rows
and report this limitation rather than choose a favorable amplitude cut.

The frozen development plan compares both channel directions and input
hypotheses at fixed window durations. Report coefficient stability, rank,
residuals, quadrature thinning and chronological predictions within this
already exposed development file. No noise-covariance or statistical-coverage
certificate exists; least squares with noisy regressors is descriptive only.
There is no scalar-strength, potential or action fit.

Seven other raw arrays remain unopened pending a separate protocol. Published
aggregate outcomes are exposed, so later raw-file checks cannot be described
as unseen physical predictions.
