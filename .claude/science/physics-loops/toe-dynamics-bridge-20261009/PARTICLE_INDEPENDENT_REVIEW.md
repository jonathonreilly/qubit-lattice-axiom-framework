# Independent check of the spatial particle and kinetic unit

**Result: no material mathematical finding; no mathematical correction is
requested for the frozen sources identified below.** The stated conclusions
are supported under their supplied-model, initial-error, fixed-prefactor, and
classical-lifetime hypotheses. This is a focused independent check of another
author's packet, not an audit verdict or retained-status promotion. Author
sources were not edited.

## Scope and identities

Reviewed in full:

| File in this directory | SHA-256 |
|---|---|
| `PARTICLE_KINETIC_DRAFT.md` | `5107c7f0b49172d91470965843f570a0258ff1f36d1a0c5c94fa6218dab41f87` |
| `particle_generator_check.py` | `86adf5d60d740331e17d641abbac02e6bcfc78c77e7c6c474acb3095e7475420` |

The claimed source checkout is
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/worktree`,
HEAD `b178e3a5d4c1d1301255596d10ac4e1bc2aeb192`. The previously read complete
collision note has SHA-256
`888ede1aba130d9bf4df5ffecfbadf9c4e45dd94a49ca3a350894a052e0677c0`.
The new particle/PDE argument uses only its finite collision relation and
four-distinct-species conservation facts, which are reconstructed below.
The hydrodynamic source, persistence import, and quantum continuation are not
premises of this review's mathematical conclusions.

Applicable source workflow and reviewer instructions were read at the identified
checkout revision; current-source freshness was not fetched because network
access is excluded. No model/reasoning setting was changed. Author source files
remain read-only. Reviewer helpers and outputs use only `particle_review_*`.

## Coverage and conditions

The complete written argument and primary runner were inspected. This review
covers the exact drift and quadratic variation, conservation and units,
global/local density distinctions, energy/Doob factor 5, stopping and overshoot,
both restored full-process estimates, multinomial initialization, the local
`C^2` PDE lifetime and derivative bounds, upwind consistency, and the sufficient
`N h^7` and `N h^10` limits. The decisive arguments were independently
rederived below; the finite generator identities were additionally exercised
by a separate complete small-state generator.

The principal conditions that must remain visible in downstream reuse are:
`w=m^-3` rather than unconverted physical cell volume; the stated initial
mean-square error condition (in particular (22) for the displayed polynomial
population scales); time inside the stated classical interval; and fixed
prefactors for the `O`-notation in Section 7. No global nonlinear PDE theorem,
uniform diffusive-scaling lifetime, native carrier identification, or nonlinear
fluid limit is supplied by this unit.

## Independent analytic reconstruction

### Density normalization, drift, bracket, and units

Write `a=M/(Nw)` for one particle's density increment. A hop has rate
`sigma |v_d| n/h=(sigma |v_d|/h) p/a` and increment `a(e_y-e_x)`.
Its weighted squared jump is `2wa^2`. Therefore its trace contribution is
`2wa (sigma |v_d|/h)p=2 sigma M |v_d| p/(Nh)`. Summing gives exactly
draft (10), including the apparently absent `w`: that factor has cancelled
against the density increment, but returns through `sum p=M/w` in (11).

A directed reaction has rate `gamma kappa a n_i n_j` and increment
`a nu`. Its coordinate drift is `gamma kappa p_i p_j nu`. Since four
distinct species give `||nu||_2^2=4`, its weighted bracket contribution is
`4 gamma kappa w a^3 n_i n_j=4 gamma kappa M p_i p_j/N`.
The two directions give the sum of input products in draft (10).
On the component box `[0,R]`,

`ab+cd <= (R/2)(a+b+c+d) <= (R/2) rho_z`,

so summing the reaction coefficients and cells gives
`Q_coll <= 2 gamma K R M^2/(Nw)`. No cell-mass conservation is used.
For example, a hop changes two local mass totals, whereas each collision
preserves all five moments at its own cell. Every jump preserves their global
totals; their martingale quadratic variations are therefore zero globally.

Here `w` is dimensionless normalized measure, `h` is physical length, and
`sigma/h` is a rate. The factor `gamma kappa` has units inverse density per
time, so the reaction clock `gamma kappa a n_i n_j` is a rate and both
weighted bracket expressions have units density squared per time. Replacing
`w` with `h^3` without the fixed torus-volume conversion changes the model.

### Energy estimate, rederived with a sharper scalar comparison

Let `Y=||e||^2`, `Z_t=integral <e_{s-},dM_s>`, and assume the exact hypotheses
of draft (15). The energy identity and expectation give

`phi(t) <= E0 + 2L integral_0^t phi(s) ds + Ct`.

Instead of the author's looser intermediate majorant, solve this scalar
comparison exactly:

\[
 \psi(t)=
 \begin{cases}
 E_0e^{2Lt}+C(e^{2Lt}-1)/(2L),&L>0,\\
 E_0+Ct,&L=0.
 \end{cases}
\]

Then `phi<=psi`, and the expected nonmartingale terms in the supremum
identity sum to at most `psi(T)`, because
`psi(T)=E0+CT+2L integral_0^T psi(s) ds`.
The positive-semidefinite bracket matrix implies

`E|Z_T|^2 <= C integral_0^T phi(s) ds <= CT psi(T)`.

Doob and Cauchy–Schwarz therefore give

\[
 \mathbb E\sup_{t\le T}\|e_t\|^2
 \le\psi(T)+4\sqrt{CT\psi(T)}
 \le5\psi(T)
 \le5(E_0+CT)e^{2LT}.
\]

Thus the factor 5 in (15) is valid. The finite-state application supplies
all needed square integrability; a general unbounded-process version would
first use localization. Dissipativity of the upwind term eliminates it from
`<e,D>`; no operator-norm estimate of `A_h` belongs in the exponential.
The reaction Jacobian gives `L=4 gamma K R`, hence exponent `8 gamma K R T`.

### Stopping and overshoot

For `tau_R=inf{max p>=R}`, stop both fields at the same time:
`e_t=p(t wedge tau_R)-u(t wedge tau_R)`. Its drift and bracket are multiplied
by the predictable stopping indicator. At a crossing jump the compensator
and stochastic-integral coefficient use the state just before the jump,
where `p<R`; after the jump the stopped process is frozen. It is neither
necessary nor true that the post-jump state must stay below `R`.

At an exit, including time zero, a coordinate has
`p_{zi}-u_{zi} >= R-B=eta`, hence `||e||_h^2>=w eta^2`.
This gives the exit probability in (18). The event in (19) is contained
in a single event `sup||e_stopped||_h^2 >= min(r^2,w eta^2)`; an extra union
bound factor is unnecessary.

The inequalities used to restore the full chain are correct:

`||a||_{1,h}^2 <= q ||a||_h^2`,
`||p-u||_{1,h} <= 2M`, and
`||p-u||_h^2 <= ||p||_h^2+||u||_h^2 <= 2M^2/w`.

The last estimate uses nonnegativity of the cross term and total mass, not
a pointwise density bound on the exited chain. These yield (20)–(21).
The multinomial initial trace in (22) follows from
`w a^2 sum N pi(1-pi)`, with `pi=w u^0/M`.

### PDE lifetime, differentiability, and cell comparison

For each species, the collision polynomial is a nonnegative gain minus that
species times a nonnegative loss coefficient. Along its own characteristic
this preserves nonnegativity. Each species' gain is at most `K X^2`, with
`X=max_i||f_i||_infinity`, so the Riccati comparison in (24) is valid.
The diagonal translation semigroup is strongly continuous on `C^2`; the
polynomial map is locally Lipschitz there. Bounded first and second derivatives
then give continuation up to every strict time in (24).

The collision Jacobian row sum is at most `4K B_T`. Each second spatial
derivative has that same linear term, plus four products of first derivatives
per reaction, bounded by `4K G_1^2`. Thus (25) is valid; its forcing exponential
is conservative. For instance the sharper integral majorant is

`G2(t) <= exp(a t)[G20+4 gamma K G10^2 integral_0^t exp(a s) ds]`,

where `a=4 gamma K B_T`, which is no greater than the displayed bound.
The same box estimate controls the grid solution by the maximum principle
for the upwind generator. Total mass and the other four global moments are
conserved by integrating the local flux laws. Pointwise density is not fixed.

For a sampled continuum field, each active velocity coordinate contributes
at most `(h/2)||partial_dd f||_infinity` to its one-sided difference error.
There are at most three active coordinates, giving `3 sigma h G2/2`.
The grid transport semigroup is a maximum-norm contraction, so the error
Gronwall exponent is `4 gamma K B_T` as stated.

The cell-average initialization error is the sum of three one-dimensional
symmetric-average errors `h^2 G20/24`, hence `h^2 G20/8`. A telescoping
composition of averaging operators justifies this without uncontrolled mixed
Taylor points. The within-cell coordinate displacement sums to at most
`3h/2`, giving the interpolation term in (28). Normalized spatial measure
has total one, yielding the factors `sqrt(q)` and `q` in the two norms.

### Volume powers and applicable initial laws

With fixed positive streaming prefactor, fixed other data, fixed time inside
(24), and `E0=O((Nw)^-1)`, the stochastic term has scale

`D_R=O((N w h)^-1)`.

The exit factor contributes another `w^-1`, so mean-square `L^1` and fixed
threshold `L^2` probability errors are `O((N w^2 h)^-1)`. Since
`w=h^3/(2pi)^3`, this is `O((N h^7)^-1)`. The full `L^2` mean-square exit
bound instead contributes `w^-2`, giving `O((N w^3 h)^-1)` or
`O((N h^10)^-1)`. The deterministic squared interpolation error is `O(h^2)`.
The powers 7 and 10 are valid sufficient powers of this proof.

These power statements need (22) or another initial-error estimate of that
order; arbitrary initial laws with nonvanishing `E0` do not converge. The
draft's Section 7 invokes (22), so this is an applicability condition, not a
discovered counterexample. At zero streaming the same calculation improves
the sufficient powers to 6 and 9 when the other fixed-data assumptions hold.
None of these fixed-prefactor conclusions permits `gamma=delta^-2` to diverge
on a fixed macroscopic interval without checking the complete constants and
providing an adequate classical lifetime.

## Computational evidence

The independent helper is `particle_review_generator.py`. It imports no
author code, uses exact rational arithmetic, and builds sparse generator rows
from one-particle label hops and fair assignments of reacting labelled pairs.
It applies the resulting generator to coordinate functions and the squared
weighted norm. In particular the trace bracket is independently computed as
`Q||p||_h^2-2<p,Qp>_h`, rather than by the primary runner's jump-increment
trace formula.

The complete reviewer output is `particle_review_generator.log`. Two complete
fixed-count state spaces, with four axis velocities and one reversible
axis-pair collision, were checked:

| Grid side count | Particle count | Occupation states | Outgoing generator edges |
|---|---:|---:|---:|
| 3 | 2 | 5,886 | 11,718 |
| 2 | 3 | 5,984 | 17,408 |

Every coordinate drift and both trace brackets agree with the independently
assembled formulas; all positive targets remain admissible and preserve all
five global moments. This exercises the periodic boundary case with two cells per direction,
multiple input particles, nonunit mass `M=5/7`, side length `7/3`, and physical
mesh distinct from normalized cell weight. A separate full-D3Q27 pair-signature
census recovers all 288 four-species exchanges by grouping unordered input
pairs, a different enumeration from the primary four-subset matchings.

An independently enumerated initial product law gives exact initial errors
`825/196` for the first state space and `1100/1323` for the second, matching
(22). An explicit crossing jump has pre-maximum `10/7`, threshold `15/7`,
and post-maximum `20/7`; its full squared error `275/196` exceeds the exit
threshold `3025/6272`, illustrating why a post-jump box restriction is neither
available nor needed.

Four reviewer mutations were executed separately and each exited 1:
omit collision cell-volume normalization, omit collision mass normalization,
remove the factor 2 from the claimed hop bracket, and allow collisions between
different cells. The complete expected failures are in
`particle_review_mutations.log`. These demonstrate sensitivity to specific
defects; they do not certify absence of other errors.

The frozen primary runner and its packaged version were each executed with
`PYTHONDONTWRITEBYTECODE=1` and exited 0. Their complete outputs are
`particle_review_author_rerun.log` and `particle_review_final_runner.log`,
which are byte-identical. The reported exact bracket values and 17,010 event
types match those outputs. The primary's built-in phrase `mutations detected`
describes wrong-formula contrasts inside that runner, not a record of external
mutated-source executions by itself.

Separately, the supervisor's `SPATIAL_RUNNER_MUTATIONS.txt` contains seven
scratch executions targeting this exact packaged primary source: reaction
census, cell normalization, collision bracket metric, transport orientation,
single-particle displacement, initial covariance, and collision locality.
The complete seven particle entries, including their before/after text,
mutant hashes, and intended assertion failures, were inspected. The record's
SHA-256 is `db58ce3346ea4fc6d808f2aeca40a5a0d40ed59f0c72cd237e91c780a572aec3`.
Each of the seven patches was reconstructed from the pinned final primary
source; all resulting mutant hashes match the record. Those executions were
performed by the supervisor; they were not rerun as a second reviewer series.
The other units' mutation entries are outside this particle review's coverage.

The primary and reviewer computations test finite algebra. They do not
numerically prove the energy, stopping, continuum-PDE, or limiting theorems;
the explicit analytic reconstruction above is the check of those statements.
The complete-state reviewer examples use four velocities and one channel,
not the entire D3Q27 many-particle state space. The full-velocity quantifiers
are supported by the written componentwise proofs and complete finite reaction
census, not by extrapolating these two generator examples.

## Final packaging confirmation

The final source note and runner were compared in full against the frozen
draft pair. Every change was inspected. Mathematical equations, inequalities,
proofs, hypotheses, and limiting statements are unchanged. The note changes
only packaging/title/status, source/premise description, a proof-obligation
table, two theorem headings, artifact paths, and review/formalization scope.
The runner adds only `AUDIT_TIMEOUT_SEC` and `AUDIT_INPUT_PATHS` metadata.
The packaged sources covered by this confirmation are:

| Path relative to the source checkout | SHA-256 |
|---|---|
| `docs/SPATIAL_PARTICLES_AND_NONLINEAR_KINETIC_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-09.md` | `76ca0244ac3f4f1bcaf345f614e8acd418047e155ce0b40e035c5d3bc4c70c5e` |
| `scripts/spatial_particles_and_nonlinear_kinetic_limit_2026_10_09.py` | `4881c3fd7e3df9a446eb83b7e93df28bb7e683e667ba9364e3694eaa0f8f28a8` |

The explicit conditional-support language and physical exclusions agree with
the checked scope. The final note's reference to this report as branch-local
is a packaging commitment: at review time the report and reviewer evidence
are in the sibling `spatial_continuation` directory. The supervisor states
they will be copied into the branch loop pack, preserving content and original
identities, with any Markdown-link rebasing recorded. That copy should retain
this source-bound review record; this reviewer has not written inside the
repository. The named canonical runner-cache file was absent when checked;
its subsequent generation and mechanical envelope validation are outside this
mathematical confirmation. Actual raw successful executions are preserved in
the reviewer logs named above.

## Independence and verification limits

This reviewer previously authored a companion quantum-register draft using
the same supplied cell/velocity conventions. The review is by a different
author of the particle packet, with no imports from its code, but is not a
blind fresh-context or cross-model certification. The common model contract
and the target inequalities were known. Formal audit status is unchanged.
No Lean formalization, long-time theorem, empirical test, physical clock or
rate derivation, or native-carrier realization was performed. No editable
prompt file or platform instruction was changed. All mathematical conclusions
are tied to the exact source identities above; changed arguments, premises,
or bounds require an affected-scope recheck.


<!-- Packaging: relative repository links rebased; historical draft links rendered as provenance text. Mathematical/review assertions unchanged. Original raw report SHA-256: eb624e379d7e9083b9fe30b6e640aa6e63669427eb594c08684b4ad70b13c501. -->
