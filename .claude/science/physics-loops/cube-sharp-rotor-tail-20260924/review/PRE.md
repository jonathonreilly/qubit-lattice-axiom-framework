# Independent PRE: rotor birth-energy upper-tail mechanism

This is an independent consequential proof check in the fifth personal
campaign. It is not an audit verdict or a source-readiness/landing decision.
The associated `PRE_SEAL.json` freezes this file before any new root derivation
or certificate is read. No source, branch, premise registry, audit state, or
publication surface was changed by this checker.

## Sources and independence boundary

The scientific inputs are exactly the two assigned already-main notes:

- `docs/ROTOR_CUBE_FAST_ENERGY_STRONG_DECAY_WITHOUT_UNIFORM_DECAY_BOUNDED_THEOREM_NOTE_2026-09-24.md`,
  SHA256 `072d6024923f05c00f5fd1e80e1dc3952a77c773b48886bd59b7be97adc28133`.
- `docs/ACTUAL_BIRTH_ROTOR_ENERGY_HAS_AN_ALGEBRAIC_LOWER_BOUND_BOUNDED_THEOREM_NOTE_2026-09-24.md`,
  SHA256 `7f6f2dbb4444f69dcc29c29b812e517074ebde65c4725317ccf2f0f2f4ea8d28`.

Both were checked byte-for-byte against `origin/main` at
`0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`. The read-only live main query
returned that same revision. The applicable execution instructions were at
`eb1f1ca8338848cf2046582e13aef372d8540937`, also matching the live remote.
The source copies and current-main workflow/workhorse instructions are pinned
in `SOURCE_PINS.json`. The shared checkout HEAD moved during the check; no
new HEAD source was consumed, and the two assigned files remained identical
to the pinned main revision. Exact consumed bytes, rather than the moving
checkout's HEAD, identify the mathematical input.

The complete arguments of the two notes were read. Their local-hop construction,
rank certificates, and supplied compact-time microscopic interpretation are
imported hypotheses here, not independently rebuilt in this bounded task.
I have not read the campaign checkpoint, the `rotor-tail-personal` directory,
any new root derivation, or a root computational implementation. I have not
delegated. The derivation below uses a quadratic Lyapunov functional and the
distribution of the smallest singular value. Supplemental finite controls
import neither a source runner nor root work.

## Quantified block estimate

Let the dark and bright spaces be finite-dimensional complex Hilbert spaces.
For fixed positive `delta, kappa`, let `Q: dark -> bright` and `B=B*` be
constant matrices. Choose nonnegative bounds

    ||Q|| <= q,       ||B|| <= beta.

Set

    L = [ 0             -i delta Q*          ],
        [ -i delta Q    -kappa I-i delta B   ]

    A = kappa^2 + delta^2 (q^2 + beta^2),
    alpha = kappa delta / A,
    c = 2 kappa delta^2 / (5 A).

Write `s = inf_{||d||=1} ||Qd||`; thus `s=0` whenever Q has a dark kernel.
For every `t>=0`, every initial vector, every permitted dimension, and every
permitted Q and B, the following energy estimate holds:

    ||exp(t L) x||^2 <= (5/3) exp(-c s^2 t) ||x||^2.                 (1)

The independent contraction bound is `||exp(t L)||<=1`, so the smaller of
that bound and (1) can be used. The constants in (1) are uniform over a
family with the stated fixed `delta, kappa, q, beta`. No normality,
diagonalizability, eigenbasis conditioning, or simplicity assumption is used.

### Direct proof

Use the inner product `a*b`, conjugate-linear in its first argument, and put

    E = ||d||^2 + ||b||^2,
    J = Im[(Qd)* b],
    H = E + alpha J.

Since `alpha q <= 1/2` by `2 kappa delta q <= kappa^2+delta^2 q^2`,

    (3/4) E <= H <= (5/4) E.                                      (2)

The equations give, by direct differentiation,

    E' = -2 kappa ||b||^2,
    J' = delta ||Q*b||^2 - delta ||Qd||^2
         - kappa Im[(Qd)*b] - delta Re[(Qd)*B b].                  (3)

Hermiticity of B implies

    ||(kappa I+i delta B)b||^2
      = kappa^2 ||b||^2 + delta^2 ||B b||^2
      <= (kappa^2+delta^2 beta^2) ||b||^2.

Consequently the last two terms of (3), in absolute value, are at most
`D ||Qd|| ||b||`, where `D^2=kappa^2+delta^2 beta^2`. Young's inequality
with the specified coefficient is

    D ||Qd|| ||b||
      <= (delta/2) ||Qd||^2 + D^2/(2 delta) ||b||^2.

Thus

    H' <= -(alpha delta/2) ||Qd||^2
          + [-2 kappa + alpha delta q^2 + alpha D^2/(2 delta)] ||b||^2
       <= -(alpha delta/2) ||Qd||^2 - kappa ||b||^2.                 (4)

The last inequality follows from

    alpha delta q^2 + alpha D^2/(2 delta)
      = kappa [delta^2 q^2 + D^2/2]/[D^2+delta^2 q^2] <= kappa.

Also `alpha delta s^2/2 <= alpha delta q^2/2 <= kappa/2`. Hence

    H' <= -(alpha delta s^2/2) E
        <= -(2 alpha delta s^2/5) H = -c s^2 H.

Integrating and using (2) gives (1). The proof also works for `q=0`; no
division by q, by s, or by a spectral eigenvalue was used.

### Singular Q and the meaning of decay

Let `P` be the orthogonal projection onto `ker Q` in the dark space, extended
by zero on the bright space. Then `LP=PL=0`; this kernel is reducing for L
and L*. Therefore

    exp(t L) x = P x + exp(t L)(I-P)x,
    ||exp(t L) x||^2 = ||P x||^2 + ||exp(t L)(I-P)x||^2.             (5)

If Q has positive rank, apply the same proof on `(ker Q)^perp` plus the full
bright space, replacing s by the smallest positive singular value `s_+`:

    ||exp(t L)(I-P)||^2 <= (5/3) exp(-c s_+^2 t).                   (6)

If Q is identically zero, the complement in (5) is the bright space and
decays in squared norm exactly as `exp(-2 kappa t)`. A positive uniform
decay rate for the full space when Q has a kernel would be false. Formula
(1) remains valid there, with its zero exponent, without hiding this fact.

### The squared singular-value scale is necessary in this generality

For one dark and one bright coordinate, take `Q=s>=0` and `B=b0` real.
The eigenvalue equation is

    lambda^2 + (kappa+i delta b0) lambda + delta^2 s^2 = 0.

The branch through zero is

    lambda(s) = -delta^2 s^2/(kappa+i delta b0) + O(s^4),
    Re lambda(s) = -delta^2 kappa s^2/(kappa^2+delta^2 b0^2) + O(s^4).

Thus a uniform replacement of the exponent's `s^2` by `s^p` with `p<2`,
and with a fixed positive rate coefficient and fixed finite prefactor,
fails as `s -> 0`: initialize along this eigenvector and let time grow.
This establishes sharpness of the small-s rate scale, not sharpness of the
constant `c`. At `b0=0, s=kappa/(2 delta)`, the matrix has a nontrivial
Jordan block; (1) still applies. A proof relying solely on eigenvalue real
parts without controlling the matrix exponential would miss this issue.

## What the physical five-torus still needs

In the supplied rotor representation, write

    Q(theta) = P_bright G(theta) P_dark,
    B(theta) = P_bright G(theta) P_bright,
    s(theta) = sigma_min(Q(theta)).

The supplied identically zero dark block gives exactly the block system
above. Continuity and compactness supply finite common q and beta. For any
physical finite-word first-birth input, `rhat_i(theta)` is a Laurent
polynomial vector, in particular bounded. With normalized Haar measure,

    f_i(t) <= (5/3) integral exp[-c t s(theta)^2]
                              ||rhat_i(theta)||^2 dtheta.           (7)

This bound controls the complete nonnormal exponential, not only its slow
eigenvalue, and is uniform through rank-loss phases.

### A precise sufficient global obligation

Define the weighted small-singular-value distribution

    M_i(u) = integral_{s(theta)^2 <= u} ||rhat_i(theta)||^2 dtheta.

A sufficient additional result for the desired sharp power is

    M_i(u) <= K_i u^(5/2),       0<u<=u0,                           (8)

with positive finite constants. In fact the input-independent geometric
bound

    Haar{theta: s(theta)<=epsilon} <= K epsilon^5                  (9)

for all sufficiently small epsilon implies (8), because each actual input
is bounded. No phase classification is logically required if (9), or the
weighted version (8), can be proved directly for the actual physical Q.

To verify the implication, extend (8) to every u>0 by increasing its constant
using the finite total input norm. Tonelli's theorem gives, for t>0,

    integral exp[-c t s(theta)^2] ||rhat_i(theta)||^2 dtheta
      = c t integral_0^infinity exp(-c t u) M_i(u) du
      <= K_i' Gamma(7/2) (c t)^(-5/2).                             (10)

The contraction bound handles `0<=t<=1`. Equations (7)-(10) would yield

    f_i(t) <= C_i (1+t)^(-5/2).

Combined with the imported actual-input lower bound, this proves two-sided
order `(1+t)^(-5/2)` for each specified first-birth vector. It does not by
itself prove an asymptotic coefficient `f_i(t) ~ A_i t^(-5/2)`.

### One geometric route that suffices for (9)

It is sufficient to establish ALL of the following for the actual Q:

1. Its full rank-loss set `Z={theta: rank Q(theta)<24}` is finite.
2. At every point `theta_j` of that set, in a real local torus chart,
   `sigma_min(Q(theta_j+h)) >= a_j |h|` for sufficiently small h,
   with `a_j>0`.
3. There are no unclassified rank-loss points elsewhere. Once item 1 is
   exhaustive, continuity and compactness imply a positive minimum for s
   outside the chosen neighborhoods.

Indeed, for small epsilon the sublevel set in (9) lies inside finitely many
balls of radius at most `epsilon/min_j a_j`. Their five-dimensional Haar
volume is bounded by a constant times `epsilon^5`.

For an isolated rank-23 point, a checkable sufficient local test for item 2
is the following. Let u span `ker Q(theta_j)` with norm one and let R be
the orthogonal projection onto `ker Q(theta_j)*` in the bright space.
Form the real 5 by 5 matrix

    T_ab = Re <R (partial_a Q) u, R (partial_b Q) u> at theta_j.     (11)

If T is positive definite, item 2 follows. To see why, decompose the dark
space as `span(u) + u^perp` and the bright space as `range(Q0) + ker Q0*`.
The block `Q0:u^perp -> range(Q0)` is invertible. At nearby phases,
bounded invertible row and column eliminations reduce Q to this continuing
invertible block and a one-column Schur complement

    h -> sum_a h_a R (partial_a Q)u + O(|h|^2).

Its squared first-order norm is `h^T T h`; positive definiteness provides
a lower bound proportional to `|h|`. Uniformly bounded eliminations then
give the same order lower bound for `sigma_min(Q)`. This projects out the
part removable by a changing dark vector; using the unprojected derivatives
would not be a valid test. Multiple-kernel points require a corresponding
uniform lower bound on the entire reduced block, not just one chosen vector.

An alternative sufficient route is a global inequality
`s(theta) >= a dist(theta,Z)` combined with the tube-volume bound
`Haar{dist(theta,Z)<=epsilon} <= K epsilon^5`. These are sufficient
geometric conditions, not claims made here about the actual phase set.

### What is not established by the assigned inputs

The rank witness proves almost-everywhere full rank. The flat-phase rank
and actual-input overlap provide the lower bound. These facts do not provide
(8), (9), an exhaustive rank-loss set, or positive definiteness of (11).

For example, in a scalar dark/bright block the analytic coupling
`Q(theta)=1-exp(i theta_1)` is full rank almost everywhere but vanishes on
a four-dimensional subtorus. A constant dark input has a slow branch with
decay scale `theta_1^2`; integrating its surviving projection over a tube of
width `t^(-1/2)` gives a lower bound of order `t^(-1/2)`, incompatible with
a `t^(-5/2)` upper bound. Conversely,
`Q(theta)=sum_{j=1}^5 (1-cos(theta_j))` has only one torus zero but opens
quadratically there; its slow decay scale is `|theta|^4`, and the same
projection argument gives a lower bound of order `t^(-5/4)`. Extra fixed
coupled blocks can embed these examples in larger dimensions. These are
counterexamples to inferring the missing geometric information from generic
analyticity and almost-everywhere full rank; they are not proposed physical
rotor matrices or counterexamples to the actual cube claim.

If the actual rank-loss set has additional components or higher-order
opening, special vanishing of the actual input's slow projections could
still recover a faster state-specific tail. Then those projections and
their vanishing orders must be checked, not inferred from finite support.
Condition (8), which weights by the full input norm, is a convenient
sufficient condition and is not claimed necessary for every possible input.

## PRE conclusion and released-source comparison targets

The general uniform estimate (1) is proved, including singular matrices
and nonnormality. The physical sharp upper bound is conditional on an
additional global small-singular-value estimate such as (8) or (9). No
classification of the actual physical phase set has been assumed or proved
in this PRE. The sequential fast-time interpretation and its original
fixed-laboratory-time limitation are preserved.

The supplemental script `independent_block_checks.py` checks the Lyapunov
identity and inequalities exactly on a complex rational matrix example,
checks a nontrivial Jordan example, checks the scalar slow-branch expansion,
and tests singular, nearly singular, and nonnormal finite matrices. It also
rejects cross-term/coupling-sign mutations. Its complete output and scope
are recorded in `INDEPENDENT_BLOCK_CHECKS.json` and the raw log. These finite
controls validate implementation and signs; the proof above establishes
the quantified matrix result. They supply no physical phase classification.

After this PRE is sealed, a released-source comparison should determine:

- whether the root block estimate actually controls the full exponential
  with constants uniform near every rank-loss phase;
- whether any proposed physical rank-loss classification is exhaustive;
- whether its certificate proves linear opening, including projections
  needed to allow the dark kernel vector to vary;
- whether any claimed t^(-5/2) exponent is two-sided order or a full
  asymptotic, and whether all additional hypotheses for the latter are met;
- whether physical finite-word weights, normalized Haar measure, and the
  original order of limits have remained unchanged.

No unproved favorable classification is a premise of this check.
