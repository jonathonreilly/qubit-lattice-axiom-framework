# The Eta-Twisted Walk Family: Covariant 3D Dispersion With a Rigid Quantized Drift

**Date:** 2026-06-10
**Claim type:** bounded_theorem (a discovery: the eta-twisted-equivariant
licensed class transports, via an exactly solvable family; plus the exact
rigidity classification of its symmetric-point drift)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/eta_twisted_walk_family_discovery_2026_06_10.py`](../scripts/eta_twisted_walk_family_discovery_2026_06_10.py)
(SCORECARD: PASS=13, FAIL=0; cached:
[`logs/runner-cache/eta_twisted_walk_family_discovery_2026_06_10.txt`](../logs/runner-cache/eta_twisted_walk_family_discovery_2026_06_10.txt))

---

## What this answers (relative to block04)

Block04 (landed via reviewer rewrite, 89b054b5b) established that covariant
single ticks cannot transport in its two ANALYZED classes (f(D), exact;
linear permutation-equivariant, sweep-grade — the landed note's Result 4),
and its landed runner names the remaining variant in its own words: "the
projective-representation variant is the named refinement". This cycle
performs that enumeration and finds a DISCOVERY in the existence
direction:

> **The eta-twisted covariance class TRANSPORTS.** There is an exactly
> solvable six-phase family of licensed, covariant, dispersive single ticks
> — and its symmetric-point drift velocity is RIGID and QUANTIZED.

The kinetic-isotropy consequence, honestly scoped: the symmetric-point
velocity takes values in the DISCRETE set {+-1/6, +-1/(2 sqrt 3)} per axis
(exact, over the whole moduli torus) and the diagonal dispersion is exactly
linear for all moduli — while off-axis FRONT SPEEDS are continuously
moduli-dependent: the family's rigid kinetic invariants coexist with
genuinely continuous shape/front content. Which of these the realized
matter occupies is realization content for the named inputs.

## The eta twist (runner Part A)

Diagonal sign gauges `V12 = diag(1,1,1,1,1,1,-1,-1)`,
`V23 = diag(1,1,1,-1,1,1,1,-1)` make `W_sigma = V_sigma P_sigma` an
ETA-TWISTED LINEAR S3 action under which the eta-decorated per-axis shifts
transform covariantly (computed; all generator relations close to `+I` —
the cocycle is TRIVIAL, as it must be: S3 admits no genuine projective
representations). The content is the sign TWIST relative to the bare
permutation representation — supplied by the landed staggered `eta`
structure — and that twist is load-bearing (Part F below).

## The family (runner Parts B-C)

Orbit reduction of the W-equivariant (eta-twisted) licensed family: 4 diagonal + 12 hop
orbits, no sign obstructions (32 real parameters). Inside it, the
discovery subfamily: ALL diagonals zero, six hop orbits at amplitude
`(1/sqrt 3) e^{i phi_j}` —

- **exactly unitary for ARBITRARY phases, proven symbolically (C1)** — a
  six-torus moduli space of licensed covariant walks;
- **dispersive in all three axes simultaneously (C2)** — a genuinely 3D
  covariant walk, outside every class block04 analyzed: not f(D) (that
  class is flat: `D^2` scalar), not linear-equivariant (flat: the landed
  block04's Result 4 and its runner's leaf-sweep check), not factorized
  (block04's per-axis class), not a permutation tick;
- evading the known no-nontrivial-isotropic-walk obstruction on the
  primitive cubic lattice (literature comparator, non-derivation context;
  the linear-representation version of the obstruction is consistent with
  the landed block04's Result 4) — the eta-twisted sign representation is
  the escape route.

## The band structure (runner Part D), exact

- **D1 — the family-wide pairing:** the spectrum satisfies the
  `lambda -> -lambda` pairing at every moduli point; everywhere-double
  DEGENERACY is a property of the `phi = 0` / equal-phase-sum strata, not of
  generic moduli (computed; the first draft's "everywhere degenerate" was a
  stratum fact caught in review).
- **D2 — genuine curvature:** eigenvector-tracked band slopes vary by ~0.19
  along a momentum line. Curved covariant dispersion EXISTS at this carrier
  density — the landed block04 Result 6 structure, realized in the covariant
  class.
- **D3 — THE EXACT SOLUTION AND THE RIGID DRIFT (review-supplied proof,
  verified symbolically in the runner):** with
  `alpha = e^{i(phi0+phi3)}`, `beta = e^{i(phi1+phi4)}`,
  `gamma = e^{i(phi2+phi5)}`, the characteristic polynomial on EVERY axis
  line factors exactly as `9 p = Q_A(alpha,beta) Q_B(beta,gamma) / w^2`, with
  `Q_A = 3 lambda^4 w - lambda^2 [alpha(2w+1) + beta(w^2+2w)] + 3 alpha beta w`.
  `Q_B` is the same block with `alpha` replaced by `gamma`.
  Implicit differentiation gives the EXACT symmetric-point slopes over the
  WHOLE moduli torus: `-+1/6` iff the phase-sums differ (the precise
  genericity condition), `+-1/(2 sqrt 3)` on the equal-phase strata —
  **slope 0 never occurs**. The velocity set is the DISCRETE set
  `{+-1/6, +-1/(2 sqrt 3)}`. (The first draft's "flat phi = 0 stratum" was a
  central-difference artifact — the sorted spectrum is exactly even in `t`
  there; the one-sided rate is `1/(2 sqrt 3)`, computed and documented.)
  Along the BZ diagonal the factorization sharpens further:
  `4p = 4 (lambda^2 - beta w)^2 (lambda^2 w - alpha)(lambda^2 w - gamma)/w^2`
  — the diagonal dispersion is EXACTLY LINEAR (`theta_0 +- t/2`) for ALL
  moduli.
- **D4 — the geometry, honestly:** the symmetric-point structure is a rigid
  DRIFT VECTOR `+-(1,1,1)/6` (a tilted first-order plane, transverse-flat),
  not a cone; generic `U(0)` multiplicities are `[1,2,1,1,2,1]`. Transport is
  maximally ANISOTROPIC at first order — along the body diagonal — a notable
  fact for a kinetic-isotropy campaign, stated not hidden. And the no-dial
  statement is SCOPED: the rigid invariants are the drift vector and the
  exactly-linear diagonal dispersion; off-axis FRONT SPEEDS vary continuously
  with the moduli (computed: 0.19-0.24 across samples) — the moduli are NOT
  pure momentum translations. The family carries both rigid quantized
  kinetic invariants and genuinely continuous shape/front content.

## The eta twist is load-bearing (runner Part F)

The SAME six orbits with the SAME `1/sqrt 3` amplitudes but with the twist
signs stripped (the bare-permutation version) are NOT unitary (residual
exactly 2/3); with the signs, they are exactly unitary (~2e-16). The eta twist —
i.e., the landed staggered sign structure — is precisely what makes
covariant 3D transport possible. The linear family's flatness is the
landed block04 Result 4, cited not recomputed.

## Open-1 status (the full unrestricted family; honest)

The unrestricted licensed family's exact kill-propagation exceeds a
50,000-leaf cap (runner Part G, deterministic) — exhaustive enumeration is
combinatorially infeasible and is documented as such. Development-phase
structured hunts around the known structural cells (shifts, exchange cells,
staircases, mixed cycles, hybrids) found no curved or tunable cell outside
the eta-twisted family; those hunts are NOT shipped as runner content and
carry no claim weight here. The full-family classification question remains a
NAMED OPEN, sharpened from "unanalyzed" to
"infeasibility-documented, development-searched, not treated as exhaustive".

## 2026-07-04 live-runner repair

The live runner was rechecked after the 2026-07-04 queue sweep. Two
implementation-level issues were found without changing the exact D3
factorization or the claimed scope:

- **D3c phase wrapping:** the old numerical witness compared sorted raw
  `lambda` phases at the `phi = 0` stratum. Current eigensolver ordering can
  pair across the `+-pi` branch cut and report artificial rates near
  `pi/dq`. The repaired witness computes the one-sided rates on
  `X = lambda^2`, the branch-invariant variable used by the exact D3a-D3b
  factorization, then divides by two to recover the lambda-phase rate. It
  still fails if the equal-stratum rate is not `1/(2 sqrt 3)`.
- **E1 runtime:** the seeded least-squares census still uses the same
  32-parameter equivariant family, deterministic starts, three unitarity
  test momenta, and two held-out fine momenta. The repair precomputes the
  fixed-momentum linear basis matrices and evaluates the same residuals from
  those bases, reducing the live runtime from the old near-300-second cache
  window to about 80-100 seconds on the current local runner. The updated
  cache records a zero-fail run with at least `50` unitaries, at least `10`
  dispersive solutions, and every dispersive solution in the six-orbit
  family. This remains sweep-grade evidence only, not an exact classification
  of the 32-parameter variety.

## The conditional set after this cycle

| entry | status |
|---|---|
| block03/block04 set (readings, bridges, unaudited deps, premises) | unchanged |
| the named refinement (the eta-twisted/'projective-variant' enumeration) | ANSWERED: the class transports via the exact family; its symmetric-point velocity is quantized {+-1/6, +-1/(2 sqrt 3)} and its diagonal dispersion exactly linear; off-axis front speeds are continuous moduli content (honest scope) |
| the 3D matter cone | upgraded: a curved covariant candidate EXISTS at this density (this family); whether the realized matter sector occupies it is realization content (with the factorized class and its named input as the alternative) |
| full-family classification (open 1) | named open, sharpened (documented infeasibility + structured-search coverage) |
| amplitude-mixing tunability | subsumed into the open-1 wording above |

## What this note does NOT claim

- **No registry action, no status claim.**
- **Not a derivation of which cell the framework realizes.** The discovery
  family and the factorized per-axis class are now two exhibited realization
  candidates; selection between them (and among the family's own discrete
  drift cells {+-1/6, +-1/(2 sqrt 3)}) is realization content for the named inputs and
  the audit lane's grade calls.
- **The {1/6, 1/(2 sqrt 3)} values are the family's own quantized
  constants** — their relation to the saturating per-axis value 1 (and to
  the OS0 wording via the B-W bridges) is reconciliation work for the
  realization row, not asserted here.
- **The continuous front-speed content is stated, not hidden:** the family
  is NOT dial-free in every kinetic respect — its rigid invariants are
  named, its continuous content is named, and selection between and within
  realization candidates is the named-inputs row.
- **No empirical input.** The walk-obstruction comparator is context,
  entered in the loop import ledger, reproved-adjacent (the linear case is
  consistent with block04 F2b; the eta-twisted escape is exhibited, not
  imported).

## Falsifiers

- A moduli point whose symmetric-point velocity lies outside
  {+-1/6, +-1/(2 sqrt 3)} (now EXACT via the D3 factorization — a
  counterexample would falsify a symbolic identity).
- A licensed curved or tunable cell OUTSIDE the eta-twisted family (the
  open-1 surface; would localize new structure the classification misses).
- A framework derivation that the realized matter tick is NOT in the
  eta-twisted class and NOT factorized (would make both exhibited candidates
  moot).

## No-Go Discipline Gate (for the negative legs)

The negative claims: "the symmetric-point velocity set is discrete (exact)"; "no dispersive
equivariant unitary found outside the six-orbit family (sweep grade)".

- **N1 alternative routes:** (1) tune the six phases — settled on the exact
  D3 surface: the factorization classifies every moduli point and rejects a
  flat stratum;
  (2) leave the 1/sqrt-3 subfamily within the 32-parameter equivariant
  family — the runner's census (E1) finds every dispersive equivariant
  unitary INSIDE the six-orbit family (diagnostics computed per solution);
  an exact classification of the equivariant variety is a registered falsifier
  surface; (3) the full unrestricted family —
  NAMED OPEN (documented infeasibility); (4) amplitude-mixing — structured
  hunts found nothing, subsumed in open 1; (5) strip the eta signs and use
  the bare permutation action — rejected for this exhibited family by F1,
  and consistent with block04's linear-flatness result.
- **N2 wall independence:** the eta-sign wall (F1: signs stripped, unitarity
  dies) is independent of the license wall (A1 degree table) and of the
  quantization mechanism (D3 rigidity) — three separately computed legs.
- **N3 hidden-wall scan:** "generic stratum" — declared (the phi = 0 flat
  stratum is exhibited, not hidden); "symmetric point k = 0" — the drift is
  evaluated there; other band-touching geometry is part of the exact
  charpoly surface, available in the runner.
- **N4 residual matching:** block04's named refinement ("the general
  projective-equivariant family is the remaining variant") is the residual
  being answered, verbatim.
- **N5 rhetoric audit:** "transports" = existence (exhibited); "rigid" =
  symbolic symmetric-point drift classification; "no dial" = the discrete
  set {+-1/6, +-1/(2 sqrt 3)} for that drift plus exact diagonal linearity;
  off-axis front-speed continuity is stated as moduli content, and no
  exhaustiveness is claimed anywhere for open 1.
- **N6 partial-surface scan:** no prior note analyzes the eta-twisted class.
- **N7 steelman:** "the rigidity was sampled in the first draft." RESOLVED
  IN REVIEW: the referee-supplied factorization makes D3 symbolic over the
  whole torus; the steelman's residual is the off-axis front-speed
  continuity, which is now STATED as the family's honest continuous
  content rather than hidden under a blanket no-dial.
- **N8 cross-cycle echo:** block02's dichotomy gained intermediate
  quantized cells in block04; here the eta-twisted class adds an exactly
  solvable curved family whose symmetric-point drift is again quantized.
  Three rungs of the same pattern: structures multiply, the scoped
  symmetric-point dial never appears.

## Claim scope note

The discovery and rigidity claims are scoped to: the eta-twisted-equivariant
licensed class at the realized carrier density; symmetric-point drift data
on the generic and equal-phase strata, with the symbolic moduli-uniform
axis-line proof in the runner; the six-phase subfamily exhibited (the census
E1 finds no dispersive
equivariant unitary outside it at sweep grade). Open 1 (the unrestricted
family) is documented-infeasible, not classified exactly here.

## Reproduction

```bash
PYTHONHASHSEED=0 python3 scripts/eta_twisted_walk_family_discovery_2026_06_10.py
```

Expected scorecard: `PASS=13 FAIL=0` (Parts A-G; the E1 census, G1 cap, and the symbolic D3a
factorization dominate the runtime; the 2026-07-04 runner repair keeps the live
runtime below the required cache-helper timeout on the current local machine).

## Dependencies

- [KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK_BOUNDED_THEOREM_NOTE_2026-06-10.md](KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK_BOUNDED_THEOREM_NOTE_2026-06-10.md) — block04 (landed): the named refinement this answers; F2b (linear flatness) cited.
- [STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md](STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md) — block02 (landed): the site-license degree structure.
- [STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md) — the landed eta sign structure this consumes (`unaudited`, conditionality inherited).
- [STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md](STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md) — one Grassmann per site (`unaudited`, conditionality inherited).
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) — the campaign target.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or of the kinetic-isotropy primitive. The
independent audit lane is the only status authority.
