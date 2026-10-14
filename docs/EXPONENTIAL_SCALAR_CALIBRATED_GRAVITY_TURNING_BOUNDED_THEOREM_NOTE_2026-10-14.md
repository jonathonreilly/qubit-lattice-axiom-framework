# Force-calibrated gravity has a scalar turning point

Status: conditional support.
Claim type: bounded_theorem.
Scientific author: /root.
Primary runner: `scripts/exponential_scalar_calibrated_gravity_turning_check.py`.

A reported drift of a gravity parameter motivates first deriving the force
coefficient that the candidate predicts in a specified measurement regime.
Within that regime the total attraction has a strict maximum along the coupling coordinate,
so its instantaneous first derivative need not detect scalar motion there.
This is an inverse-conditioning result, not agreement with an orbital dataset.

The [candidate action](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md)
and [local response](EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md)
are supplied premises. Their parameters and the actual environment remain free.
The following complete derivation separates a force value, its instantaneous
derivatives and a chosen synthetic finite-window fit.

## The calibrated gravity turning point

Scientific author: /root. Observational determinations of temporal gravity
variation motivate deriving the candidate's actual force normalization, rather
than replacing a measured G by its bare tensor coefficient. The result below
is an ideal long-range common-background bridge; it is not a reanalysis of any
ephemeris or an environmental matching theorem.

### 1. Declared readout domain

Use the supplied candidate's canonical scalar chi with chi=0 at u=0, universal
coupling A, beta=d ln A/dchi>0, q=beta^2, 0<k<1/3,
a=(1-k)(1+3k)/4, and Q=Q0(1+k). Freeze a sufficiently slowly varying ambient
background on the duration/size of each ideal weak force measurement. Take
unscreened complete weak bodies, effectively pointlike compared with the scalar
range, with negligible ambient linear response and controlled relativistic,
finite-size, range and apparatus corrections. Within this domain,

    Gforce=A^2(1+q)/(8 pi Q),    Gref=1/(8 pi Q0).

This is the total tensor-plus-scalar attraction coefficient in Jordan physical
units. It is not automatically the G parameter of an orbital likelihood. Q0
and Gref remain free normalization parameters; Gref is not an independently
observed vacuum value. A time derivative below uses a common physical Jordan
clock and assumes the readout approximation remains controlled as it varies.

### 2. Exact elimination of the field coordinate

The supplied coupling gives q=a/[1+(1-3a)s exp(2 sqrt(a) u)] and
A^2=(1+s)exp(2sqrt(a)u)/[1+s exp(2sqrt(a)u)], with
s=(1+k)/[k(1-3k)]. Eliminating u yields

    A^2=4(a-q)/[(1+k)(1-3q)],     0<q<a<1/3.

Consequently

    Gforce/Gref = 1 - 4(q-k)^2/[(1+k)^2(1-3q)].             (1)

Thus the ideal force coefficient has a strict maximum Gref at q=k, u=chi=0.
It stays positive for finite allowed u. The negative-u branch has k<=q<a;
the positive-u branch has 0<q<=k. This is a consequence of the supplied coupling
and Q normalization, not a derivation of Newton's absolute scale.

The bare coefficient Gbare=A^2/(8piQ) varies linearly near chi=0. Its variation
is canceled to first order by the scalar-force factor (1+q). Treating Gforce
as Gbare would miss this cancellation.

### 3. Derivative and inverse conditioning

Write d=-beta_chi=(a-q)(1-3q)/(1-3a). Then

    q_chi=-2 beta d,
    d ln Gforce/dchi = 2 beta [1-d/(1+q)]
      =2 beta(q-k)[2-3(q+k)]/[(1-3a)(1+q)].                (2)

At the vacuum q=k and d=1+k, so this derivative vanishes exactly. Since
q_chi(0)=-2sqrt(k)(1+k), expanding (1) in the canonical coordinate gives

    Gforce/Gref = 1 -16k chi^2/(1-3k)+O(chi^3),
    (ln Gforce)_chichi(0) = -32k/(1-3k).                  (3)

For a smooth physical-time crossing chi(t0)=0,

    (dot Gforce/Gforce)(t0)=0,
    (ddot Gforce/Gforce)(t0)=-32k dot chi(t0)^2/(1-3k).   (4)

The second identity is independent of chi acceleration at that instant because
the first field derivative vanishes. It holds only for the ideal readout; a
time-dependent correction to the readout may have its own first/second
derivatives. A small correction amplitude alone does not bound those derivatives.

A first-derivative limit cannot be uniformly inverted into a scalar-speed limit
near this turning point. If q is known away from k and the full forward model
justifies a pointwise drift error epsilon, then |dot chi|<=epsilon/|d ln G/dchi|
is conditional; its conditioning diverges as q approaches k. This is not an
assertion that arbitrarily rapid fields remain inside the quasistatic regime.

The value inverse also has two branches. Let D=1-Gforce/Gref and
C=D(1+k)^2/4. Then

    q-k = [-3C +/- sqrt(9C^2+4C(1-3k))]/2.              (5)

For D>0 the plus sign is the negative-u branch, and the minus sign is admissible
only while q>0. Allowed q must also satisfy q<a. Near D=0, the displacement is
proportional to sqrt(D), so its derivative with respect to D is singular. Neither
the sign branch nor the free reference scale is supplied by a force value alone.
For 0<D<1 the plus root is admissible. Both roots are admissible precisely
when 0<D<4k^2/(1+k)^2; at that threshold the minus root is q=0 and is
excluded from the finite-field domain. D=0 gives one coincident vacuum root.

### 4. Finite observation windows and what is not inferred

An orbital estimate of a linear G drift is obtained from an extended data model,
not an instantaneous derivative. Equation (4) does not establish compatibility
with such data: curvature, source sensitivities, timing, other gravity parameters
and nuisance correlations may be observable. A symmetric synthetic crossing can
have zero leading fitted linear drift while a nonzero quadratic change remains.
The initial phase/time of crossing is not selected by this identity.

The observation source is the published LLR analysis arXiv:2012.12032, exposed
earlier in this campaign. It motivates this bridge check, not a new fit, likelihood
or independent observed test. No uncertainty is converted to a scalar-speed bound.
The absolute scale, actual ambient field, range, source response and full orbital
mapping remain open. Retired within the ideal readout is the extra assumption
that bare and force-calibrated gravity have the same field derivative.

### 5. Explicit finite-window calculation

To make the finite-window caveat reproducible, choose a synthetic trajectory
q(t)=k+v t on [-T/2,T/2], with 0<q(t)<a. This is a chosen local trajectory,
not a solved cosmology or a selected crossing phase. Let g=1-3k and
xi=3|v|T/(2g)<1. For a uniform continuous least-squares fit with free intercept,
the dimensionless force slope is b=integral t [Gforce(t)/Gref]dt / (T^3/12).
Using the exact square deficit and pairing positive and negative times gives

    b = -9 v^3 T^2/[5(1+k)^2 g^2] * (1+r),
    0 <= r <= xi^2/(1-xi^2).

Indeed the numerator is -[4v^2/(1+k)^2] integral t^3/(g-3vt)dt.
Its even part is (3v/g^2) t^4/[1-(3vt/g)^2], and integral t^4dt=T^5/80.
The positive weighted remainder is bounded by the maximal denominator change.
Thus the leading linear-fit term is cubic in v, while the instantaneous
quadratic curvature survives. The fit is not generally exactly zero for this
chosen q-linear trajectory. A specially symmetric force history can have an
exactly zero fitted slope, but it is a different imposed history. Neither
synthetic fit represents the timing, sampling or nuisance correlations of LLR.

The complete parent control preserves its initial 114/1 roundoff failure in
the inverse at the double root. Raising arithmetic precision from80 to130
digits, without changing formulas, fixtures or the1e-55 acceptance, gives115/0.
That numerical difficulty is expected from the square-root inverse and is
not evidence for additional physical branches.


## Controls and limits

The canonical calculation executes115 controls with15 original-coordinate
field cases, two-sided canonical small-field limits, inverse-domain checks and
six chosen finite-window trajectories. All are synthetic development data;
none was reserved as an observed holdout. The original114/1 double-root
roundoff failure, complete profiles, exact precision-only repair, raw streams
and actual altered implementations are retained. Acceptance1e-55 is unchanged.
Assertion counts are implementation checks, not observational experiments.

The independently chosen controls differentiate the original coupling and
metric, check signed canonical derivatives, admissible root counts and the
finite-window distinction. Their report and all failed controls are preserved
in the recovery evidence. No separate formula is silently assumed for a
measured gravitational constant.

### Published LLR context and data role

[Biskupek, Mueller and Torre, arXiv:2012.12032](https://arxiv.org/abs/2012.12032) report an estimated temporal variation of G of (-5.0 +/-9.6) times10^-15 per year. The abstract describes a multi-parameter relativistic analysis using lunar laser ranging. The parent re-opened that abstract on2026-10-14; this is not a new raw-data or full-likelihood analysis.

The paper was exposed earlier in this campaign and serves as model-development context. The turning-point identity tests a necessary force-calibration distinction before interpreting such an estimate. It neither predicts that estimate nor converts its uncertainty into a scalar-speed bound. The actual ambient state, body sensitivities, finite-range corrections, orbital dynamics, sampling, covariance and nuisance parameters remain to be supplied and checked. There is no independent observed holdout in this block.

An arbitrary force-reference normalization, the realized ambient field, source
sensitivities, incoming fields, range and apparatus corrections survive. The
first-derivative cancellation does not license arbitrary rapid motion, and
small correction amplitudes do not bound their derivatives. The exact turning
identity does not derive the theory's coupling or potential and does not select
a crossing history, vacuum state, absolute scale or observational confidence
region. A real lunar-ranging test requires a full forward likelihood.

Recovery: `docs/work_history/physics/revised-scalar-calibrated-gravity-turning-20261014/README.txt`.
