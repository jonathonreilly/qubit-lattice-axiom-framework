# Focused independent mathematical check: analytic fluid completion

The corrected handwritten construction supports the claimed global future
vacuum convergence within the supplied finite-dimensional homogeneous model.
The full covariant scalar equations, matter exchange, coercive energy bound,
forward continuation and LaSalle argument check out. This conclusion uses
fixed a>0, nu>0, H_v>0, the Einstein expanding branch, and nonnegative ideal
fluid densities. It does not establish attraction to the calibrated finite-time
history or general spacetime stability.

Two original-text findings were reported to the parent and are preserved:

1. The v1 u mode list omits the generalized solution at the permitted value
   nu=9/4. Both displayed exponentials then coincide; their Wronskian is zero.
   The complete critical solution is (C1+C2 t)exp(-3H_v t/2).
2. Einstein H>0 alone does not imply physical H_J>0 at intermediate times for
   unrestricted a>0. For a=nu=H_v=1, fields and densities zero and
   v=(-3,0,0), the constraint gives H=2 but H_J=-1. The original convergence
   proof survives; bounded u bounds A above and away from zero, yielding
   physical proper-time completeness and H_J->H_v in the future.

The parent preserved v1 and wrote `HAND_DERIVATION_v2.md`. I read and checked
the complete affected text. Only these mode/frame clarifications changed;
the potential, metric, reconstructed trajectory and attractor proof remain
byte-identical outside the three identified replacements. V2 correctly
resolves both findings. I found no additional material mathematical error in
this scoped handwritten construction.

## Source and role coverage

Both original inputs were copied byte-for-byte before the checks. The complete
v1 derivation and protocol were read, followed by the complete affected v2
wording and its identity record. No parent runner was read, imported or
executed. No observational data, numeric implementation, future fixtures,
other source block, Git state or external primary source was used for this
review. The parent retains scientific authorship and implementation work.

| Source | SHA-256 | Disposition |
| --- | --- | --- |
| HAND_DERIVATION_v1.md | 41dc33bd1b0ac810d4c3da493b9fb34b433ecc1a1f5a06bca773a1b244ff1801 | Entire handwritten argument checked; original findings retained; source unchanged. |
| PROTOCOL_v1.json | b7d06776617627f79177b2db64ccb25baf4b4132f5382f4f7b46a5b7e0b82dfc | Entire protocol read; scope and supplied assumptions checked; source unchanged. |
| HAND_DERIVATION_v2.md | 322a932eef3ede5de4d963aae2c623693d12a5942828f971335cc7a6c03ef7d2 | Affected-source confirmation; inherited proof checks reused; both corrections verified. |
| MODE_AND_FRAME_CORRECTION_v2.json | 9ef6f8c60e4ad2b12780bd48b18630d8438eb5565eca53bd3b31991211be3cfa | Entire identity record read; original and corrected hashes verified. |

`SOURCE_DISPOSITIONS.json` gives absolute source and exact snapshot recovery
paths. `RECEIPT.json` binds this report, the full independent derivation,
executed checking sources, raw returns and all evidence. All outputs are
confined to this `independent_math_review/` directory.

## Load-bearing mathematical checks

The full derivation is in `INDEPENDENT_DERIVATION.md`. The main independent
steps were as follows.

- Starting from the supplied action and conformal matter metric gives the
  scalar force +K^AB alpha_B sigma inside the homogeneous equation and
  dot sigma=(-3H+sqrt(a)u_dot)sigma. The cancellation of their exchanged energy
  is exact. Radiation's vanishing trace supplies no direct u force.
- Direct differentiation of K reproduces all 27 three-field connection
  entries, including every zero and lower-index symmetry. The exact branch
  satisfies each of the three covariant Klein–Gordon equations separately.
  The gradient proof uses the Levi-Civita Hessian and metric compatibility;
  it is not just a consequence of the Friedmann energy identity.
- The potential remainder above its displayed quadratic lower bound is
  exactly 2H_v^2(u-sqrt(a)/4)^2 x^2. For
  Q=E0/H_v^2-3/2, explicit coordinate bounds give
  D<=1+34(1+a)Q/(9a) and a positive lower bound on K on the entire energy
  sublevel. They bound velocities and both densities as well as the fields.
- The nonnegative-fluid sublevel is compact and forward invariant. H stays
  between H_v and sqrt(2E0/3); the proper-time vector field remains smooth on
  a neighborhood of the sublevel. These facts justify continuation for all
  future proper time before LaSalle is applied. Density boundaries are
  invariant and do not require logarithmic coordinates.
- Zero energy dissipation requires v=0 and sigma=r=0. Staying there also
  requires grad V=0. The strict positivity of f(u) forces x=y=0, after which
  nu>0 forces u=0. There is exactly one invariant limiting vacuum. No global
  convexity assumption or chosen-history attraction is needed or inferred.
- Canonical vacuum masses are H_v^2(nu,9/4,2). V2 includes the critical u
  solution. The word “free” in the mode statement is appropriate: a dust
  density perturbation additionally drives
  u_part=-sqrt(a)delta sigma/(nu H_v^2), which also decays. The slower y mode
  decays absolutely while growing relative to the selected exact y branch.
- Pulling the proper-time system through v=Hp reproduces every N-coordinate
  equation. Its denominator equals 2(sigma+r+V)/H^2>0 and stays bounded away
  from zero on a fixed energy sublevel. The log-density chart cannot represent
  the zero-density boundary, as the note correctly states.

## Independent computations and actual failures

These controls are mathematical checks, not empirical tests or the parent's
numeric implementation.

| Executed reviewer source | Method and result |
| --- | --- |
| check_analytic_fluid_v1.py | Exact SymPy differentiation. 81 assertions: 79 passed, one real v1 source finding, one unevaluated-radical simplification failure. Exit 1 retained. |
| check_analytic_fluid_v2.py | Same independent equations, with factorization before symbolic simplification. 81 assertions: 80 passed, the real frozen-v1 source finding still fails. Exit 1 retained. |
| check_momenta_fraction_v1.py | Independent stdlib Fraction Euler–Lagrange momentum route, without Christoffels or SymPy. 80 fixtures, 402 assertions, all passed. Exit 0. |
| AFFECTED_V2_CHECKS.json | 18 affected-source and identity checks passed; no broad science rerun. |

The first symbolic execution left a residual proportional to
F-sqrt(F^2), with F=3+2(1+a)(x^2+y^2)>=3. It is mathematically zero on the
declared domain, rather than a source error. The complete original failed
output, original executed source and exact reviewer-normalization diff remain
preserved. Factoring before simplification resolves it without a forced or
incorrect square-root branch choice. The second reviewer source still checks
the original frozen v1 mode claim, so its source-finding failure remains an
honest recorded failure after the parent separately corrected the prose.

The second derivation route checks all coordinate scalar equations in 80
exact rational fixtures, including zero and single-fluid boundaries, signed
field amplitudes, small and large a, and nu=9/4. It also checks explicit
compact-sublevel inequalities. Removing the metric-derivative terms produces
nonzero residuals in all 64 nonvacuum fixtures. The independent energy controls
detect either missing matter-exchange term. The admissible H_J=-1 example is
preserved as an exact frame-scope control. These are targeted failure-sensitivity
checks rather than replay of the proposed equations alone.

## Boundaries of this confirmation

The supplied action introduces a curved field metric, a third scalar and a
positive nu restoring term. Neither those premises nor H_v or the calibrated
initial amplitudes were inferred from data by this proof. The initial-amplitude
algebra works for nonnegative supplied fractions with a positive remainder;
photon units, observational input processing and implementation have not been
checked here. The proof uses standard c=1 and positive G_* conventions.

The attractor is a vacuum of this flat homogeneous classical model. It does
not select the observed finite-time expansion, dust/radiation abundances,
photon temperature, neutrino sector, entropy, primordial perturbations or a
quantum state. The strict parameter inequalities matter: no a=0, nu=0 or
H_v=0 limiting theorem is inherited. Physical proper-time completeness here
does not imply a theorem for general inhomogeneous spacetime or all geodesics.
V2 states the relevant frame and history limitations without overclaiming.

This is a focused independent proof check, not a formal audit, scientific
status promotion, or approval of a future implementation or observational
comparison.
