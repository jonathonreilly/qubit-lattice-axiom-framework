# Local one-step-deviation and generator/source tournament — Cycle 228

**Date:** 2026-07-17

**Type:** bounded_theorem

**Status:** exact conditional theorem on the Cycle-215/219 one-particle
fixtures plus bounded candidate tournament; audit unset

**Authority:** none

**Constitutional effect:** none

**Packaging:** draft parking branch and draft PR #5389 only

Companion runner:

```text
scripts/local_generator_source_tournament_cycle228_2026_07_17.py
```

This note and runner change no foundation, axiom, Qualification, primitive,
registry, policy, audit, or queue surface.

## Result up front

Cycle 227 showed `Q`-only blindness on named field and moving fixtures; it did
not construct a complete archive ledger. Cycle 228 asks what the already-built
strict proper-cubic update actually determines before any one coordinate is
called physical energy, mass, or gravitational source.

One fixed-representative result is exact. Choose a phase reference `alpha` and
write

```text
U_alpha = exp(-i alpha) U,
K_alpha = 2I - U_alpha - U_alpha^dagger,
S_alpha = (U_alpha - U_alpha^dagger)/(2i).
```

Then

```text
K_alpha = (I-U_alpha)^dagger (I-U_alpha) >= 0,
U = exp(i alpha) [I - K_alpha/2 + i S_alpha].
```

Thus `(K_alpha,S_alpha)` is a **complete local spectral pair** for a chosen
representative of the one-step update. For every `alpha`, both operators have
exact one-edge kernels on this fixture, commute with `U`, and transform under
all 24 proper-cubic frames. `K_alpha` is positive and loses phase orientation;
`S_alpha` retains orientation and is signed. The algebra is generic for a
fixed unitary representative. The fixture-specific gain is exact strict
locality.

Positivity, locality, and conservation do not choose `alpha`. The runner
compares `U` with the projectively identical `exp(0.4 i)U` at the massless
rest point. Both give the same density-matrix update, while

```text
<K>:     0 -> 0.157878,
<S>:     0 -> 0.389418,
<H_abs>: 0 -> 0.4.
```

Even `exp(i alpha)I` receives nonzero values until a phase-zero reference is
supplied. This does not assume that global phase is unphysical in the final
framework. It proves that the current one-particle fixture has not supplied
the clock, vacuum, composition, or cross-sector reference needed to make that
phase physical. Below, unqualified `K,S` mean the supplied `alpha=0`
representative.

For that representative define the derived deviation vector

```text
chi_t = (I-U) Psi_t.
```

Then

```text
<K>_t = ||chi_t||^2,
chi_(t+1) = U chi_t.
```

So `K` has the positive local one-step deviation density

```text
k_x(t) = ||Psi_t(x) - (U Psi_t)(x)||^2.
```

Its total is exactly conserved and the derived deviation vector is transported
by the same strict local update. This is not yet physical activity or energy:
it depends on the chosen phase representative and is quadratic at small phase.
Exact phase-linearity is an imposed candidate selection criterion motivated by
the current rest and positive-frequency targets, not a consequence of the
framework axioms.

The exact positive phase magnitude

```text
H_abs = 2 asin(sqrt(K)/2) = |Arg U|
```

does give the chosen linear calibration on the selected positive scalar
branch. It equals the supplied analytic rest-mass calibration algebraically,
tracks massive kinetic quasienergy, and sees the `U=-1` flat modes. Its
finite-torus kernel is nonzero through every tested range and the massless
scalar data are stable and consistent with an approximately `r^-4` tail. It is
therefore not finite range on this fixture. The independently finite-differenced
held-out curvature mass agrees only within the runner's declared tolerance.

There is also an interpretation wall: `H_abs` is positive, but on a
negative-phase mode `exp(i H_abs) != U`. A chosen signed spectral `Arg` lift
generates the complete `U`; it is indefinite, branch-dependent, generally
nonlocal, and not ordinarily additive after phase wrapping. Because `-1` lies
in the spectrum, an analytic principal matrix logarithm is unavailable. The
runner explicitly tests the `+pi` and `-pi` spectral lifts and their exact
`2pi` projector difference.

The outcome is not a universal no-go. It leaves several construction
hypotheses live:

> A positive-frequency or particle-hole/Fock lift may turn signed local update
> data into a positive additive energy. A selected action or autonomous clock
> may instead provide a normalized response and continuity ledger. A nonlinear
> clock map such as Cycle 204's `tan(omega)`, a fundamental `K` source with
> emergent nonlinear calibration, a mixed operator-valued source, or a direct
> local conserved current may also survive. None is selected here.

Physical energy remains unselected. No axiom conclusion follows.

## Candidate tournament

For an eigenmode `U psi = exp(i theta) psi`, after choosing `alpha=0` and one
spectral `Arg` branch `theta in (-pi,pi]`, the candidates are

```text
K          = 4 sin^2(theta/2),
S          = sin(theta),
sqrt(K)    = 2 |sin(theta/2)|,
H_abs      = |theta|,
H_Arg      = theta.
```

The Cycle-213 projected wave energy is a separate two-slice quadratic form,
not merely another scalar function of `U` on the full six-mode space.

| candidate | positive | exact spatial range on the named fixture | conserved | field/kinetic coverage | exact tested rest linearity | main residual |
|---|---:|---:|---:|---:|---:|---|
| supplied rest scalar `Q` | yes on `beta <= 0` branch | onsite species label | if the species register is fixed | no massless or kinetic content | yes | blind to named field/moving coordinates |
| phase reference `alpha` | not a scalar | onsite rephasing | exact projective channel | shifts every spectral coordinate | unselected | clock/vacuum zero absent |
| `K` | yes relative to `alpha` | one edge | exact | massless, moving, and `U=-1` deviation | no; quadratic | reference-relative stiffness/deviation, not calibrated energy |
| `S` | no | one edge | exact | signed; cancels on symmetric packets | approximate | blind at `theta=0,pi` and indefinite |
| Cycle-213 `E_wave` | yes | two edges | exact only at `beta=0` | scalar acoustic sector | no common massive calibration | sector- and two-slice-specific |
| `sqrt(K)` | yes | non-finite-range; finite-torus tail measured | exact | yes | approximate | nonlocal and not ordinarily additive |
| `H_abs=|Arg U|` | yes | non-finite-range; finite-torus tail measured | exact as a spectral magnitude | yes | exact rest calibration | does not generate negative-phase `U` |
| chosen signed spectral `Arg U` | no | generally nonlocal | branch-conditional | signed | exact rest calibration | `+/-pi` branch, winding, and positivity |
| active commit current | not a static positive density | local candidate | depends on supplied process | sees writes | no | misses dormant matter and free radiation |
| tangent response of a candidate local deformation | open | local in tested families | not automatic | target: all sectors | zero and scale unselected | action, reference, normalization, and Ward law absent |

The table is deliberately a tournament over named candidates, not an
exhaustive classification of every possible local action, QCA, field content,
Fock lift, or stress tensor.

## Exact massless identities

At `beta=0`, let

```text
gamma(k) = [cos(k_x)+cos(k_y)+cos(k_z)]/3,
L(k)     = 6 [1-gamma(k)].
```

For a scalar input `f tensor |s>`, the runner verifies

```text
<K>       = L/3 = 2(1-gamma),
<S>       = 0,
<sqrt(K)> = sqrt(L/3),
<H_abs>   = arccos(gamma),
E_213     = (3/2)(1-gamma^2).
```

The point carrier makes the distinction especially clear:

```text
<S> = 0,
<K>/2 = 1,
E_213 = 5/4.
```

These are not three normalizations of an already selected energy. They are
different exact coordinates: signed temporal antisymmetry, one-step deviation or
static stiffness, and a projected two-slice wave energy.

The flat modes are a second discriminator:

```text
U=+1 flat pair: K=0, S=0, sqrt(K)=0, H_abs=0;
U=-1 flat pair: K=4, S=0, sqrt(K)=2, H_abs=pi.
```

All four are scalar-projection invisible. At the eigenmode level, every
`U=+1` vector lies in the same `f(1)=0` eigenspace for any spectral scalar with
`f(1)=0`; the runner has not constructed a vacuum or occupation sector. A
future law may prove those modes gauge/unphysical or supply an occupation or
number structure that distinguishes them. This is an open route, not an axiom
recommendation.

## The chosen-reference local one-step-deviation theorem

For any state of the named one-particle walk and any chosen phase reference,

```text
U_alpha = exp(-i alpha)U,
K_alpha = 2I-U_alpha-U_alpha^dagger
        = (I-U_alpha)^dagger(I-U_alpha).
```

Therefore `K_alpha` is positive semidefinite. Rephasing does not change the
one-edge support of the update or its inverse, so the simplified kernel has
radius one. At the supplied `alpha=0`, if `Psi_(t+1)=U Psi_t`, then

```text
chi_(t+1)
  = (I-U) U Psi_t
  = U (I-U) Psi_t
  = U chi_t.
```

Hence `sum_x ||chi_t(x)||^2` is conserved, and the derived deviation density is
transported by a graph-local unitary. The runner checks this identity on
generic complex states at both the massless endpoint and a massive family
member. Existing quantum-walk current theorems support a graph-local norm
current for this transported vector; neither theorem assigns it the physical
meaning “energy.”

The runner also checks only the taut but useful tensor statement
`U_total=U tensor I`: normalized inert logical spectator factors leave the
original-sector deviation norm unchanged. No correlated copy, witness, record
write, changed physical update, reset reservoir, or archive redundancy is
modeled. The framework's physical redundancy-invariance test therefore remains
open for this candidate coordinate.

## Why exact positive phase becomes nonlocal

On the massless acoustic branch,

```text
theta(k) = arccos(gamma(k)) ~ |k|/sqrt(3).
```

Any finite-range translation-invariant scalar spectral function has a finite
Laurent-polynomial Bloch symbol and is analytic near `k=0`. If a real analytic
function `e(theta)` satisfies `e(0)=0` and is nonnegative on both sides of the
origin, then zero is a local minimum and `e'(0)=0`. It cannot have the linear
behavior `c |theta|` with `c>0`.

This proves only the following narrow statement:

> Within chosen-reference-zero, finite-range, analytic scalar functions of this `U`,
> positivity across both acoustic signs and exact linear phase energy cannot
> all hold at once.

It does not rule out a signed local generator plus particle-hole/Fock
reinterpretation, an enlarged onsite alphabet, a local action with an
autonomous clock, a time-dependent local generator, or a different candidate
law.

The executable kernel check agrees with the analytic boundary:

```text
sqrt(K) scalar kernel: approximately r^-4;
H_abs scalar kernel:   approximately r^-4 on its nonzero parity sublattice.
```

The selected positive-branch inverse used here is

```text
Q_mass = 6 asin(sqrt(K_rest)/2),
```

which is `3 H_abs` and inherits the nonlocal spectral tail when promoted from
a rest-sector calibration to an operator on the complete field space.

## Massive rest, motion, and inertia

For the common family,

```text
phi(beta) = -tan(beta/2),
M_Q       = 3 phi.
```

At scalar rest,

```text
3 K       = 12 sin^2(phi/2),
3 S       = 3 sin(phi),
3 sqrt(K) = 6 sin(phi/2),
3 H_abs   = 3 phi = M_Q.
```

`H_abs` therefore equals the supplied analytic rest calibration exactly on the
selected positive scalar branch. The independently finite-differenced held-out
curvature mass agrees within `4e-6` relative tolerance; that comparison is
numerical, not an exact identity. `S` and `sqrt(K)` approximate the rest
calibration at small phase; `K` is quadratic and does not.

For `beta=-0.3`, the same `H_abs` expectation increases across the tested
moving scalar states while the species-level `Q` remains fixed. This repairs
Cycle 227's kinetic blindness only as a one-particle spectral magnitude. It
does not yet supply a local density, an additive Fock energy, or a stress
tensor.

The tested `beta=-0.3` complete fixture does not remove the nonlocal boundary:
the runner locates transverse `+1` and `-1` crossings on its diagonal momentum
line. A gap-qualified quasi-local route remains live on restricted sectors;
the complete tested six-band fixture is not such a restricted sector.

## Composition and the need for physical carrier structure

For same-sign positive independent eigenphases below a branch crossing, the
signed phase and positive phase magnitude add, but `K`, `S`, and `sqrt(K)` are
nonlinear periodic functions and do not. Once the sum crosses the principal branch,
even `Arg` and `|Arg|` cease ordinary addition. Two phases `2+2` are represented
by the same global one-step eigenvalue as `4-2pi`.

This does not mean energy cannot add. It means the global one-step phase alone
does not store its own winding or carrier multiplicity. An additive generator
requires extra composition or carrier structure absent from that global phase.
Tensor-factor/Fock, branch-unwrapping/history, selected-action, and direct-current
constructions are examples; none is established here. Which construction, if
any, is licensed by the common law remains open.

In the existing same-space one-particle fixture, finite-range quadratic forms
do add exactly when packet supports are farther apart than their kernel
ranges: one edge for `K,S` and two edges for `E_213`. The algebraic tails of
`sqrt(K)` and `H_abs` retain interference across every tested separation, with
nonzero finite-torus coefficients at distant ranges. This is not yet the
many-body composition theorem the TOE lane needs.

## A one-step update does not select its deformation

The runner gives an exact internal nonuniqueness control. Starting from the
same undeformed proper-cubic `U`, it constructs two strict-local unitary
families: one perturbs the onsite scalar projector and one perturbs the onsite
vector projector. Both are proper-cubic and coincide exactly at deformation
zero. Their response operators

```text
h = i U^dagger (d U_epsilon / d epsilon)|_(epsilon=0)
```

differ, and neither is automatically conserved.

There is a second, same-channel ambiguity. For

```text
U_tilde(epsilon) = exp(-i c epsilon) U(epsilon),
```

the projective channel is identical for every `epsilon` and both families
coincide at zero, while

```text
h_tilde = h + c I.
```

Reparameterizing `epsilon -> a epsilon` also rescales `h` by `a`. The runner
checks both identities. Thus the undeformed `U`, and even the complete family
of projective channels, does not select the response zero or normalization.

This does not show that a physically constructed clock or geometry deformation
is nonunique. It shows that the current fixture has not supplied one. A gate
schedule, action, autonomous clock, or geometric coupling may supply or derive
the distinction. The resulting `h` remains a Hermitian tangent response until
a phase zero, parameter normalization, clock coupling, positivity result,
continuity identity, and universal source reciprocity are independently
established.

One live construction hypothesis is a complete autonomous law
`U_*[epsilon_x]` with

```text
h_x = i U_*^dagger
      (partial U_*[epsilon] / partial epsilon_x)|_(epsilon=0),
```

where `epsilon_x` is a candidate local deformation parameter. The desired
theorem would go beyond the derivative definition: it would derive a
normalized local continuity identity accounting for matter, field,
interaction, archive carrier, clock, and blank/reset reservoir, with spatial
responses producing momentum and stress. This is a live construction hypothesis,
not the only live source route and not a result of Cycle 228.

Bare-metal language:

> **Target bare-metal hypothesis, not a result:** Can every physical update,
> including a record lock, be represented as a transfer in one locally
> conserved ledger?

“Compute cost” or “storage cost” is only an analogy until that ledger, its
continuity law, positivity, and coupling are derived.

## Conditional application to clocks and records

Under the proposed physical-witness criterion, an autonomous clock could
trigger or participate in a second outcome-dependent write; elapsed time by
itself supplies no outcome-dependent carrier. To count as a witness in this
candidate, the clock or detector would have to acquire or emit a durable,
distinguishable, outcome-dependent physical state. That introduces an explicit
carrier interaction whose resource ledger and back-reaction must be modeled;
an irreversible tick channel is possible but is neither derived nor universally
required here.

The favored two-stage bare-metal hypothesis remains conditional:

1. a local interaction creates a reversible candidate correlation; and
2. an independent physical carrier receives an outcome-dependent write and is
   hypothesized to close the relevant local ledger transfer.

The clock may participate in step 2. An outcome-independent phase advance is
not itself a second outcome-bearing witness. It may nevertheless gate or
trigger a distinct physical write under a future occurrence law. This cycle
does not derive record occurrence, permanence, or Born frequency.

## Cross-lane effect

### O — operational quantum

The result distinguishes coherent working dynamics from permanent records.
The complete fixed-reference local `(K,S)` pair and derived deviation vector
live on nonrecord quantum possibilities. Only inert logical tensor spectators
were tested; physical witness hardware and archive redundancy remain outside
this cycle. Missing are an autonomous record-write process, an occurrence law,
and Born frequencies.

### T — time

The chosen representative contains local deviation and signed phase data but
does not select a physical rate, positive energy, or clock. A leading next
probe should test whether an autonomous clock can select a phase zero,
normalization, and local action/continuity ledger, rather than equating elapsed
ticks with energy or record formation. Non-action and nonlinear clock-map
routes remain live.

### I — matter

`H_abs` exactly matches the supplied rest calibration, agrees numerically with
held-out curvature/inertia, and tracks moving quasienergy on the selected
scalar branch. At a chosen phase reference, `K` supplies a positive local
deviation coordinate for the complete one-particle update. A leading missing
bridge is a derived positive-frequency/Fock compiler that makes total energy
positive, local in the enlarged law, and additive while retaining binding and
interaction energy.

### G — gravity

Cycle 227's rest-only source fork is narrowed: chosen-reference `K` is a local
positive candidate but has quadratic low-phase calibration; `H_abs` has the
chosen linear calibration but is not finite range. Gravity still needs a
derived local energy-momentum/source law. Live routes include an
action/clock-response construction, `K` as a fundamental source with nonlinear
emergent calibration, mixed operator-valued sources, direct conserved currents,
and different or enlarged local laws. No source equation, reciprocity, tensor
geometry, self-coupling, or Einstein limit is derived.

### B — boundary/history

An explicitly constructed history register or autonomous clock could retain a
bounded tick count, phase winding, or carrier multiplicity. The cited clock
papers do not provide a QCA quasienergy unwrapper; that state and resource
account would have to be part of the law. The current boundary/history process
does not yet generate the family, positive-frequency sector, clock, archive
carriers, or their abundance.

## Primary-source boundary

The following sources support the surrounding mathematical mechanisms, not a
claim that this repository selected physical energy:

- Zimboras, Farrelly, Farkas, and Masanes, “Does causal dynamics imply local
  interactions?”, *Quantum* 6, 748 (2022),
  <https://doi.org/10.22331/q-2022-06-29-748>. They prove that causal
  discrete updates need not have local static logarithms and give special
  quasi-local results under additional hypotheses. This supports the
  local-update versus generator distinction; it does not prove this fixture's
  exact tail.
- Gupta and Short, “The Dirac Vacuum in Discrete Spacetime,” *Quantum* 9,
  1845 (2025), <https://doi.org/10.22331/q-2025-09-03-1845>. They show that a
  naive filled negative-quasienergy sea in a discrete-time Dirac QCA creates a
  modular-zone boundary at which pair creation can become favorable, and they
  propose modifying their model. This is direct prior art and a warning for the
  live particle-hole/Fock route, not a theorem about the current cubic fixture.
- Tate, “The Hamiltonians Generating One-Dimensional Discrete-Time Quantum
  Walks,” *Interdisciplinary Information Sciences* 19, 149–156 (2013),
  <https://doi.org/10.4036/iis.2013.149>. The constructed `D(T)` has infinite
  support; `D(T)^2` is essentially coin-register-free, and a related scaled
  scalar operator is compared with the one-dimensional continuous-time walk
  in a limit. The paper does not show `D(T)^2` to be finite range. This is close
  prior art for phase-generator versus quadratic-coordinate comparisons.
- Ciaurri et al., “Nonlocal discrete diffusion equations and the fractional
  discrete Laplacian, regularity and applications,” *Advances in Mathematics*
  330, 688–738 (2018), <https://doi.org/10.1016/j.aim.2018.03.023>. Fractional
  powers of discrete Laplacians have long-range kernels. The repository runner
  independently checks its own cubic kernel.
- Mister, Arayathel, and Short, “Local Probability Conservation in Discrete
  Time Quantum Walks,” *Physical Review A* 103, 042220 (2021),
  <https://doi.org/10.1103/PhysRevA.103.042220>. A graph-local walk admits
  graph-local probability currents. Applied here, it supports a norm-current
  for `chi`; it does not establish an energy current.
- Debbasch, “Action Principles for Quantum Automata and Lorentz Invariance of
  Discrete Time Quantum Walks,” *Annals of Physics* 405, 340–364 (2019),
  <https://doi.org/10.1016/j.aop.2019.03.005>. The paper gives a discrete action
  construction and, in its DTQW setting, derives energy/momentum conservation
  and a discrete stress-energy tensor by coordinate variation. This is a
  constructive discrete-action/coordinate-variation precedent, not a general
  Ward theorem and not a derivation for the current cubic family.
- Arrighi, Nesme, and Werner, “Unitarity plus causality implies localizability,”
  *Journal of Computer and System Sciences* 77, 372–378 (2011),
  <https://doi.org/10.1016/j.jcss.2010.05.004>. Local circuit implementation
  is distinct from a local static logarithm.
- Woods, Silva, and Oppenheim, “Autonomous Quantum Machines and Finite-Sized
  Clocks,” *Annales Henri Poincare* 20, 125–218 (2019),
  <https://doi.org/10.1007/s00023-018-0736-9>, and Erker et al., “Autonomous
  Quantum Clocks: Does Thermodynamics Limit Our Ability to Measure Time?”,
  *Physical Review X* 7, 031022 (2017),
  <https://doi.org/10.1103/PhysRevX.7.031022>. In these constructions,
  autonomous clocks are finite physical subsystems with explicit resources and
  back-reaction; they are not free phase labels. These papers do not establish
  a record-formation criterion or a universal nonzero per-tick energy cost.

The broad comparison of `Q`, `K`, phase lifts, action response, additivity, and
source coverage has substantial prior-adjacent literature. The executable
regression across this repository's exact Cycle-215/219 fixtures is new
relative to those internal cycles; global novelty has not been established.

## No-go discipline gate

The broad claims “no local energy exists,” “a Hamiltonian axiom is required,”
“`K` is gravity,” “the axioms are wrong,” and “a positive-frequency/Fock lift
cannot work” all fail this gate and are not shipped.

Only two bounded statements pass:

1. after fixing the supplied phase representative, no explicitly tested scalar
   on the named Cycle-215/219 fixtures simultaneously has positivity, exact
   finite range, common-family conservation, named field/kinetic coverage,
   exact chosen linear rest calibration, negative-phase generator compatibility,
   and ordinary additive composition; and
2. within chosen-reference-zero finite-range analytic scalar functions of this `U`,
   positivity across both small acoustic phase signs forces zero linear term,
   so exact `|theta|` calibration is unavailable without leaving that class.

### N1 — alternative routes

Executed routes are separated from unexecuted escape routes:

| route | honesty marker | executable evidence | result |
|---|---|---|---|
| static rest scalar `Q` | **ATTEMPTED** | `massive_calibration_controls` | exact supplied rest calibration; zero on massless endpoint and blind to tested kinetic state |
| chosen-reference local `K` | **ATTEMPTED** | `complete_local_pair_controls`, `deviation_transport_controls` | exact radius-one positive deviation density; quadratic at small phase and reference-dependent |
| local signed `S` | **ATTEMPTED** | `complete_local_pair_controls`, `massless_and_flat_mode_controls` | exact radius-one orientation coordinate; indefinite and aliases phases `0,pi` |
| projected Cycle-213 energy | **ATTEMPTED** | `projected_wave_energy_controls` | positive, radius-two, conserved at `beta=0`; not conserved across tested massive family |
| `sqrt(K)` and positive `H_abs` | **ATTEMPTED** | `full_kernel_locality_controls`, `scalar_tail_controls`, `massive_calibration_controls` | selected-branch calibration gains; non-finite-range kernels and negative-phase generation failure |
| chosen signed spectral `Arg` lifts | **ATTEMPTED** | `signed_phase_lift_controls`, `composition_controls` | generate `U`; indefinite, nonlocal, `+/-pi` ambiguous, and winding-sensitive |
| phase-reference family `K_alpha,S_alpha` | **ATTEMPTED** | `phase_reference_controls` | every tested reference is equally local, positive, conserved, and reconstructing; projective channel does not select `alpha` |
| scalar/vector and same-channel tangent deformations | **ATTEMPTED** | `deformation_nonuniqueness_controls` | undeformed update does not select deformation, zero, or normalization |

Excluded from the bounded negative because they remain live and unexecuted here:

| live route | why it remains live |
|---|---|
| positive-frequency/particle-hole/Fock lift | may make signed branches positive and additive after occupation structure is derived |
| selected local action plus clock-response construction | may provide phase zero, normalization, continuity, momentum, and stress; not forced by this cycle |
| Cycle-204 nonlinear `tan(omega)` clock map | preserves a nonlinear route between local update coordinates and operational energy |
| fundamental `K` source with emergent nonlinear calibration | gravity could couple to a local quadratic source while measured energy emerges nonlinearly |
| mixed `Q,K,S,E_wave` or sector-dependent operator source | the tournament tested individual scalars, not every operator-valued combination |
| direct conserved current or gate-schedule/Floquet micromotion | need not arise from a static logarithm |
| autonomous history/clock construction | could store bounded winding or carrier multiplicity and trigger a separate physical write |
| different QCA or enlarged onsite alphabet | may evade the exact fixture tradeoff; no global law-space claim is made |

The live routes defeat every broad no-go and prevent an axiom-minimum claim.

### N2 — wall-independence

Candidate failures are not counted as independent physics atoms. They collapse
into seven residual workstreams; archive/record construction remains outside this scalar
tournament:

| residual | independent content | coupling to other residuals |
|---|---|---|
| `R_phase` | the projective channel does not select a global phase reference | a physical clock, vacuum, composition law, or geometry may fix it |
| `R_offset` | epsilon-dependent projective rephasing shifts the tangent by `c I` even at fixed undeformed phase | a deformation/clock construction may independently fix the additive response zero |
| `R_norm` | reparameterizing the deformation rescales its tangent response | a physical clock or geometry may fix normalization independently of zero |
| `R_select` | the fixed one-step `U` does not select its physical deformation, schedule, or local action | choosing a construction may also solve continuity or composition |
| `R_sign` | strict local analytic positivity is quadratic at a reference-zero minimum, while signed linear phase is indefinite | a positive-frequency/Fock lift can resolve sign and additivity together |
| `R_comp` | workstream bundle: a chosen one-step spectral phase omits winding and carrier multiplicity | physical clock/history or Fock state can carry either or both; no indivisible wall is claimed |
| `R_stress` | a conserved scalar is not yet a local energy-momentum/stress response | an action/coordinate-variation or direct-current construction may solve it |

The required directional pair audit is:

| pair | left closes right? | right closes left? | independent at current evidence? |
|---|---|---|---|
| `R_phase -> R_offset` | no: fixing undeformed phase does not fix epsilon-dependent rephasing | no | yes |
| `R_phase -> R_norm` | no: a phase zero does not fix scale | no: a scale does not fix phase zero | yes |
| `R_phase -> R_select` | no | no: a deformation can retain global-phase freedom | yes |
| `R_phase -> R_sign` | no | no | yes |
| `R_phase -> R_comp` | no | no: winding storage need not fix phase zero | yes |
| `R_phase -> R_stress` | no | no: a stress current may retain phase-reference freedom | yes |
| `R_offset -> R_norm` | no: an additive response zero does not fix scale | no | yes |
| `R_offset -> R_select` | no | no: a selected deformation can retain additive tangent gauge | yes |
| `R_offset -> R_sign` | no | no | yes |
| `R_offset -> R_comp` | no | no | yes |
| `R_offset -> R_stress` | no | no: a stress current may retain an additive-zero convention | yes |
| `R_norm -> R_select` | no | no: a selected deformation can retain scale freedom | yes |
| `R_norm -> R_sign` | no | no | yes |
| `R_norm -> R_comp` | no | no | yes |
| `R_norm -> R_stress` | no | no | yes |
| `R_select -> R_sign` | no | no | yes |
| `R_select -> R_comp` | no | no | yes |
| `R_select -> R_stress` | no: selected tangents need not be conserved | no: a conserved current need not be the selected geometry response | yes |
| `R_sign -> R_comp` | no | no | yes, although one Fock construction may close both |
| `R_sign -> R_stress` | no | no | yes |
| `R_comp -> R_stress` | no | no | yes |

Constructive routes may close several residuals together; none automatically
or logically closes another on the current evidence. They are not advertised
as axiom atoms.

### N3 — hidden-wall scan

The current canonical axiom/primitive registry, minimal axiom source,
Qualification context, active review queue, and adjacent Cycle-204/213/215/216/
219/227 notes were scanned for `Hamiltonian`, `generator`, `energy`, `stress`,
`clock`, `phase`, `Fock`, `source`, `current`, `action`, and `Ward` content.

The canonical registry explicitly says the four axioms supply no update law,
source/action bridge, physical-observable bridge, rate, or formation process.
Kinetic isotropy supplies equal graining treatment, not an energy generator,
phase selector, clock readout, or source map. The realized-state primitive does
not supply coherent dynamics or a Hamiltonian. The scale primitive supplies a
reference scale, not the missing dimensionless law selection.

The cycle's own hidden premises were also classified:

| hidden premise | disposition |
|---|---|
| supplied global phase representative/vacuum zero | exposed as `R_phase`; no physical selection claimed |
| exact `E proportional abs(theta)` at small phase | retained only as a candidate criterion motivated by current targets, not axiom-derived physics |
| `K` norm means physical activity or compute cost | rejected; renamed reference-relative one-step deviation |
| inert tensor spectator is a witness/record | rejected; no physical redundancy result claimed |
| tangent response is clock rate or energy | rejected; `R_offset` and `R_norm` remain open |
| one-particle phase is already Fock energy | rejected; occupation/particle-hole structure remains absent |
| supplied common family is selected law | rejected; it remains a falsifiable fixture |
| finite-torus tail fit is an infinite-volume asymptotic proof | rejected; only non-finite-range analytic boundary and tested approximately `r^-4` data retained |

No current primitive discharges `R_phase`, `R_offset`, `R_norm`, `R_select`,
`R_sign`, `R_comp`, or `R_stress`. This is a dependency boundary, not evidence that new primitive or
axiom content is required. A retained derivation may still close them.

### N4 — residual matching

External mechanism sources are attribution controls, not prior no-go witnesses:

| source | exact supported result | use here | mismatch avoided |
|---|---|---|---|
| Zimboras et al. 2022 | static generators of causal discrete updates can be nonlocal; special quasi-local classes exist | warns against inferring local `log U`; keeps escape classes live | not cited as a theorem about this 3-D six-band kernel |
| Tate 2013 | `D(T)` has infinite support; its square has a simpler coin-register-free relation | prior adjacency for phase versus quadratic coordinate | not cited as finite-range or as physical energy |
| Ciaurri et al. 2018 | fractional discrete Laplacians have long-range kernels | supports the mechanism behind `sqrt(K)` tails | repository tail is independently executed; dimensions differ |
| Mister et al. 2021 | local probability currents for graph-local walks | applies to norm transport of `chi` | not upgraded to energy/stress current |
| Debbasch 2019 | discrete action and coordinate-variation energy/momentum/stress example | constructive discrete-action precedent | not a general Ward theorem or current-family derivation |
| autonomous-clock sources | finite autonomous controls have explicit physical resources/back-reaction | motivates explicit clock-carrier modeling | not a QCA unwrapper, record criterion, or universal energy-cost theorem |

Prior-cycle residual matching is explicit:

| cited witness (`path:line`) | witness residual | Cycle-228 residual | match? | use |
|---|---|---|---|---|
| `docs/work_history/repo/review_feedback/REST_INERTIAL_LAPSE_SOURCE_TRIANGLE_CYCLE204_NOTE_2026-07-16.md:23`, `docs/work_history/repo/review_feedback/REST_INERTIAL_LAPSE_SOURCE_TRIANGLE_CYCLE204_NOTE_2026-07-16.md:92` | supplied clock/energy map and composition seam; nonlinear `tan(omega)` escape | context only | no | preserves a live nonlinear route; not counted as a residual witness |
| `docs/work_history/repo/review_feedback/RETARDED_CUBIC_MASS_FIELD_CYCLE213_NOTE_2026-07-16.md:147` | stress-energy and clock remain open | `R_stress` | yes | prior scope witness for the still-open stress response |
| `docs/work_history/repo/review_feedback/RETARDED_CUBIC_MASS_FIELD_CYCLE213_NOTE_2026-07-16.md:147` | supplied action/source | `R_select` | no | adjacent context only |
| `docs/work_history/repo/review_feedback/FINITE_COIN_SCALAR_WAVE_DILATION_CYCLE215_NOTE_2026-07-16.md:118`, `docs/work_history/repo/review_feedback/FINITE_COIN_SCALAR_WAVE_DILATION_CYCLE215_NOTE_2026-07-16.md:162` | exact source-free wave; source port unresolved | fixture context only | no | fixture authority, not a residual witness |
| `docs/work_history/repo/review_feedback/VIRTUAL_EXCHANGE_GREEN_KERNEL_CYCLE216_NOTE_2026-07-16.md:127` | supplied action/source vertex | `R_select` | yes | exact prior witness that the construction was not selected |
| `docs/work_history/repo/review_feedback/VIRTUAL_EXCHANGE_GREEN_KERNEL_CYCLE216_NOTE_2026-07-16.md:127` | stress/clock remain open | `R_stress` | yes | exact prior witness for the stress residual |
| `docs/work_history/repo/review_feedback/VIRTUAL_EXCHANGE_GREEN_KERNEL_CYCLE216_NOTE_2026-07-16.md:127` | positive Hamiltonian remains open | `R_sign` | no | adjacent context only |
| `docs/work_history/repo/review_feedback/COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md:118` | vacuum-relative interpretation and global scalar-phase freedom | `R_phase` | yes | requires the explicit phase-reference control |
| `docs/work_history/repo/review_feedback/COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md:103` | common family and `Q` are supplied | `R_select` | no | domain boundary, not an exact residual match |
| `docs/work_history/repo/review_feedback/ARCHIVE_CARRIER_SOURCE_LEDGER_CYCLE227_NOTE_2026-07-17.md:231` | quasienergy zero and Hamiltonian remain unselected | `R_phase` | yes | exact absolute-zero warning |
| `docs/work_history/repo/review_feedback/ARCHIVE_CARRIER_SOURCE_LEDGER_CYCLE227_NOTE_2026-07-17.md:186`, `docs/work_history/repo/review_feedback/ARCHIVE_CARRIER_SOURCE_LEDGER_CYCLE227_NOTE_2026-07-17.md:197` | quasienergy, stiffness, and physical energy remain unidentified; the static source vertex is not universal for moving systems and a stress-energy-like source remains open | `R_stress` | yes | exact prior stress/source warning |
| `docs/work_history/repo/review_feedback/ARCHIVE_CARRIER_SOURCE_LEDGER_CYCLE227_NOTE_2026-07-17.md:16` | `Q`-only field/motion blindness | `R_select` | no | motivates the tournament; does not establish `K`, `H_abs`, or any other candidate as physical |

Only literal `yes` rows count as residual matches. `No` rows are context and
are not used as wall evidence.

No prior cycle closes a Cycle-228 residual. These witnesses only match, bound,
or motivate the current open conditions.

No citation is used to claim global novelty, a general impossibility, or an
axiom requirement.

### N5 — resolution

| level | what is proved | what remains open |
|---|---|---|
| eigenmode/fixed representative | exact phase functions, flat-mode responses, supplied rest calibration | physical phase zero, occupation, and positive-frequency meaning |
| packet | reference-relative deviation density/transport and point-packet discriminators | interacting many-body energy density |
| carrier/object | numerical held-out rest/curvature agreement | binding/interaction energy and physical redundancy in one ledger |
| separated same-space supports | exact additivity for finite-range quadratics beyond their support | Fock/tensor carrier-number additivity and nonlocal spectral interference |
| finite torus | exact range for `K,S` and `E_213` at `beta=0`; stable approximately `r^-4` phase-magnitude data | infinite-volume domains and exact asymptotic theorem |
| proper-cubic frames | all 24 frames for named one-particle operators | boosts, Lorentz theorem, tensor stress response |
| records/clocks | inert `U tensor I` spectators only; bounded clock literature | correlated write, physical redundancy, reset, occurrence, rates, Born frequencies |
| gravity | local-source candidate discrimination at chosen reference | phase zero, active field, reciprocity, stress tensor, backreaction, nonlinear geometry |

No one-particle or finite-torus result is promoted to a complete many-body or
continuum statement.

### N6 — primitive and reframe

The approved premise registry was checked directly. Relevant reframes were
also tested:

| reframe | effect |
|---|---|
| call chosen-reference `K` “energy” | changes vocabulary only; does not select phase zero, rest calibration, or geometric response |
| call `H_abs` “the Hamiltonian” | hides its nonlocal tail and failure to generate negative-phase modes |
| treat global phase zero as a harmless convention | valid for an isolated fixed-number projective sector, but potentially load-bearing for clock comparison, changing carrier number, composition, or gravity; no universal choice is made |
| use nonlinear `tan(omega)` calibration | remains a live Cycle-204 clock-map route; would need composition and source controls |
| couple gravity fundamentally to `K` | remains live with emergent nonlinear operational-energy calibration; reciprocity/stress still absent |
| mix `Q,K,S,E_wave` by sector | outside the single-scalar tournament and remains live until constructed without lookup |
| treat the kinetic-isotropy primitive as a clock generator | primitive explicitly withholds phase, selector, and readout content |
| treat record count as carrier number | fails Cycle-227 logical/physical distinction; Cycle 228 did not retest physical redundancy |
| treat one-step phase wrapping as a convention | composition makes winding algebraically load-bearing |
| use a basis or proper-cubic presentation change | runner verifies conjugation covariance; residuals persist |
| use the scale primitive | supplies units only; every conflict here is dimensionless |
| invoke Fock language without construction | would supply the missing occupation/additivity structure rather than derive it |

No open review finding or primitive silently closes the target.

### N7 — steelman

The strongest hostile alternative is:

> Stop demanding one positive scalar on the first-quantized update. A local
> relativistic law can carry signed positive/negative-frequency
> branches. Second quantization can make the many-body Hamiltonian positive and
> additive under a derived positive-sector/occupation construction, while a
> selected local action can provide energy-current and stress under additional
> continuity conditions. `K` is then only a useful stiffness/action
> coordinate, and the apparent conflict is an artifact of asking a one-particle
> Floquet phase to do the Fock law's job.

This steelman is scientifically strong and remains live. Cycle 228 supports it
by showing that `(K,S)` already retains the complete local update and that
`H_abs` meets the selected linear calibration only after a positive sector is
chosen. Zimboras et al.'s local-update/static-generator distinction supports
not demanding a local one-particle `log U`. Gupta and Short are the direct
Fock/Dirac-sea authority and show why a naive discrete-time sea can fail at a
modular quasienergy boundary. The next probe should execute that boundary on
the current fixture before any axiom-gap claim.

A second strong alternative is an autonomous local action/clock history that
stores winding physically. It may select a time-dependent local generator or
coordinate-variation continuity ledger without using a static spectral
logarithm. It also remains live.

A third hostile alternative is that `K`, not phase-linear energy, is the
fundamental local source coordinate. Operational rest energy could then be a
nonlinear emergent calibration such as the live `asin` or `tan(omega)` maps.
Cycle 228 shows that this requires a phase reference and does not yet provide
stress or reciprocity; it does not eliminate the route.

### N8 — cross-cycle echo

Cycle 204 left the nonlinear `tan(omega)` clock map and operational
energy/composition law open. Cycle 215 left alternative finite-coin/action
constructions and full physical source selection open. Cycle 219 explicitly
retained vacuum-relative interpretation and global scalar-phase freedom. Cycle
227 warned that neither `K` nor quasienergy zero had been selected while
narrowing only a `Q`-only extrapolation. Cycle 228 executes the missing phase
shift control and does not restate any predecessor residual as a global wall.

The cross-cycle retirement audit is explicit:

| narrow candidate expectation | retired? | mechanism | applicability |
|---|---|---|---|
| `Q`-only covers the displayed massless/moving coordinates | yes | Cycle-227 field/motion controls plus current tournament comparison | named Cycle-215/219/227 fixtures only |
| chosen-reference `K` is exact phase-linear rest/energy and projectively intrinsic | yes | small-phase formula plus `K_alpha` projective control | tested common one-particle family |
| `S` alone is positive and flat-mode complete | yes | signed spectrum and `theta=0,pi` alias controls | named six-band fixture |
| `E_213` alone is conserved across the common family | yes | conserved at `beta=0`, explicit failure at `beta=-0.3` | tested projected operator only |
| chosen positive phase magnitude is strict finite range | yes | analytic cusp boundary plus finite-torus distant coefficients | named complete fixture; restricted gapped sectors remain live |
| undeformed `U` selects deformation, response zero, and normalization | yes | scalar/vector family plus same-channel rephasing and rescaling controls | tested tangent families only |

No broader Fock, clock, nonlinear-source, direct-current, action, archive, or
different-law route is retired.

Retirement conditions are explicit:

- a derived positive-frequency/Fock compiler with local additive energy and
  exact rest calibration plus declared curvature/inertial validation retires
  `R_sign` and `R_comp`;
- a physical clock/composition/reference construction fixing global phase zero
  retires `R_phase`; a deformation construction fixing its additive tangent
  zero retires `R_offset`; and a derived deformation scale retires `R_norm`;
- a complete construction selecting a clock-rate deformation and exact
  continuity current retires `R_select`;
- a spatial-response theorem producing conserved momentum/stress and universal
  source/response retires `R_stress`.

An alternative strict local scalar outside the tested analytic spectral class
that passes all held-out controls would expand the tournament and could close
the architecture target. It would not falsify either historical bounded claim:
one concerns the candidates actually tested here and the other concerns only
the stated analytic class.

Until then the result remains a conditional candidate discriminator on the
draft parking branch.

## Scope boundary

This is not a derivation of a physical Hamiltonian, stress-energy tensor,
equivalence principle, gravitation, record formation, Born frequencies,
particle spectrum, or empirical prediction. It is not a classification of all
QCAs or all local actions. `U_beta`, the common-cone relation, the candidate
species, phase representative, and one-particle interpretation remain
supplied. The chosen-reference one-step-deviation theorem is exact on that
supplied fixture. Every physical source and TOE interpretation beyond it
remains conditional.

There is no axiom conclusion.

## Verification

```text
python3 scripts/local_generator_source_tournament_cycle228_2026_07_17.py
```

Predecessor coexistence is checked separately against Cycles 213, 215, 216,
219, and 227 before parking.
