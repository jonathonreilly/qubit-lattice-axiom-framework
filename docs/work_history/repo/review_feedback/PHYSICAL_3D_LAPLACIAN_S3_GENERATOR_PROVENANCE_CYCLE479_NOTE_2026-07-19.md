# Physical 3D-lattice provenance for the S3 generator — Cycle 479

Date: 2026-07-19

Authority: none

Audit: unset

Constitutional effect: none.  This cycle edits no axiom, foundation,
Qualification, primitive, registry, policy, queue, or audit-status surface.

Companion runner:

```text
scripts/physical_3d_laplacian_s3_generator_provenance_cycle479_2026_07_19.py
```

## Result up front

Cycle 479 constructs a bounded **candidate provenance compiler** between the
framework's supplied three-dimensional cubic substrate and the existing
Route-2/S3 time consumer.  It does not add a fourth primitive dimension.
The retained physical route is a **96-layer retained divide-six relaxation**
carried through **all 24 proper-cubic frames**.

The far-side 1,052-mode Route-2 matrix is not an arbitrary dense numerical
object.  The runner reconstructs it as the exact Dirichlet-to-Neumann Schur
complement of a **nearest-neighbor cubic Laplacian** on a finite `15^3` box:

```text
Lambda_R = H_tt - H_tb H_bb^(-1) H_bt.
```

The trace has 1,052 modes and the harmonic exterior bulk has 888 modes.  The
matrix built independently by the existing Route-2 time code and the matrix
built from the 3D Schur surface agree to machine precision.

Cycle 479 then replaces the exact bulk inverse by the same retained local
divide-six relaxation family physically compiled in Cycles 467, 470, and 474:

```text
X_(k+1) = (A X_k + B)/6,
A = 6 I - H_bb,
B = -H_bt,
X_0 = 0,
Lambda_k = H_tt + H_tb X_k.
```

For the frozen 96-layer program, `Lambda_96` approaches `Lambda_R` with
operator residual about `4.27e-8` and maximum-entry residual about `1.15e-9`.
The exact contraction factor is about `rho(A/6)=0.8370565`, so convergence is
proved rather than inferred from one fitted endpoint.  Exact 249-bit word
impulses on three training trace orbits and three held trace orbits reproduce
the same `X_96` columns with zero divide-six remainder.

Using `Lambda_96` in the Cycle-469 candidate seed family,

```text
V_96(r) = exp(-r Lambda_96) u_*,
r in {3/4, 1, 5/4},
```

gives one held `5:4` output without refitting the generator.  Each dilated
seed output has an adjacent-Givens physical schedule and inverse.  The finite
seed family remains within roughly `1e-8` of the exact Route-2 family.

This is a real bridge across the 3D/time interface, but it is **not proper
time**, not a unique time law, not a lapse, not a rate, not energy, not
probability, not occurrence, not a Record, and **not gravity**.  The Laplacian
law, finite boundary, cutoff, 96 layers, uniform seed, and identification of a
clock ratio with the semigroup parameter remain supplied candidate structure.
Update count is not time.  A generator element is not a rate.  Norm is not
probability.  There is no axiom pressure.

## Reconnaissance of both shores

The canonical premise registry describes physical sites as `Z^3` with
nearest-neighbor adjacency, translations, and proper-cubic rotations.  That
is the near spatial shore.  It does not silently select a scalar Laplacian
update, boundary, seed, or clock law.  The approved kinetic-isotropy primitive
supplies only structural `c_t=c_s` at the grained level; it explicitly does not
supply dynamics, calibration, a spacing theorem, or Lorentz closure.

The far shore was already scientifically nontrivial:

1. the Route-2 shell work derives `Lambda_R` as the exact Schur boundary
   action of the same local 3D lattice Laplacian;
2. the Route-2 time probe constructs the conditional semigroup
   `exp(-r Lambda_R)u_*`;
3. Cycle 469 physically connects classified relational clock words `3:4`,
   `4:4`, and held `5:4` to that seed family, but lists `Lambda_R` provenance
   as supplied at its compiler boundary; and
4. Cycles 467/470/474 separately compile the local divide-six arithmetic,
   seven-supercell word delivery, and whole-layer conflict schedule.

Cycle 479 composes those facts.  It does not claim that the earlier far-side
Schur theorem was absent; the repository advance is the explicit physical-M2
finite-relaxation provenance and its quantified effect on the actual held
Cycle-469 seed consumer.

## Exact Schur and convergence identity

On the exterior domain, partition the finite negative Laplacian into trace
and harmonic-bulk indices:

```text
H = [ H_tt  H_tb ]
    [ H_bt  H_bb ].
```

Because `H_bb=6I-A` and the spectral radius of `A/6` is below one,

```text
H_bb^(-1) = (1/6) sum_(n>=0) (A/6)^n,
X_infinity = -H_bb^(-1) H_bt.
```

The retained recurrence gives the exact truncated series

```text
X_K = (1/6) sum_(n=0)^(K-1) (A/6)^n (-H_bt),
X_infinity-X_K = (A/6)^K X_infinity.
```

Therefore

```text
||Lambda_R-Lambda_K||
 <= ||H_tb|| rho(A/6)^K ||X_infinity||.
```

At `K=96` the executable checks the actual operator residual against this
bound.  It also checks every stored checkpoint `K=1,2,4,8,16,32,64,96`, the
next-layer fixed-point residual, symmetry, and positive definiteness.  This is
a finite convergence theorem for the declared geometry, not an infinite-
volume or continuum theorem.

## Exact physical words

Set `D=6^96`, whose bit length is 249.  For a unit trace impulse, retain blank
bulk histories and write the boundary word `D` at the selected trace site.
The integer update is

```text
Q_x^(k+1) = [sum_(y bulk-NN x) Q_y^k + D B_xj] / 6.
```

For all `k<=96` the numerator is exactly divisible by six.  Dividing the final
integer word by `D` gives the corresponding column of `X_96`.  The runner
tests representatives of trace orbits

```text
train: (3,2,2), (4,1,0), (5,0,0)
held:  (4,2,1), (6,5,4), (6,5,5),
```

where each tuple is the sorted absolute coordinate orbit.  The held rows do
not tune any parameter.  A deleted boundary impulse and deleted layer 96 both
change the result.

Every sampled nonzero numerator is also passed through Cycle 467's frozen
totalized divider, rather than checked only with host integer division.  The
full Cycle-467 compiler supplies the 249-bit NCT trace, inverse, and work
reset; Cycle 470 supplies the seven-supercell port paths; Cycle 474 supplies
the mod-`3^3` schedule.  Their runner hashes are frozen and checked.

The irregular harmonic bulk has 888 updated cells.  The same 27 colors cover
every target exactly once at each of 96 layers, and same-round stars are
pairwise disjoint.  The runner inventories the finite `15^3` supercell
capacity and maximum simultaneous seven-star support.  This is a bounded
physical manifest, not a statement about efficient hardware time.

## Proper-cubic covariance

Every proper-cubic signed permutation maps the finite box, cutoff sphere,
trace set, bulk set, adjacency, boundary drive, and mod-three color orbit into
the corresponding carried objects.  The runner constructs all 24 frames and
checks the full `X_96` and `Lambda_96` permutations.  No carried frame performs
a new fit or selects a runtime axis.

The reference box, cutoff, coordinate origin, boundary condition, and color
order are still supplied.  Covariance of their declared orbit is not a
derivation of a frame-selection law or spacetime covariance.

## Seed consumer and compiler boundary

For each of the two train ratios and held ratio, the runner diagonalizes the
compile-time `Lambda_96`, prepares the contraction-dilated seed target, and
decomposes a two-column completion into 1,065 adjacent Givens gates.  It tests
E/G, the inverse, exact finite semigroup composition, and one-Givens deletion.
No host matrix solve occurs during the compiled update.

The local word histories do not dynamically manufacture the dense program in
one run.  `Lambda_96`, its eigendecomposition, and the Givens angles are
computed at compile time from the frozen local rule and geometry.  Thus the
licensed claim is **physical provenance compilation**, not an autonomous
universal matrix-function computer.  An exact local rational Schur solver or
a physical program-synthesis mechanism would strengthen this boundary.

The matter coin is on a disjoint code factor.  The Cycle-219 one-particle mass
fixture is rechecked and unchanged.  This does not couple the time seed to
matter inertia, contact, source recoil, or a physical rate.

## Supplied, derived, and open inventory

Supplied:

1. `Z^3` cubic adjacency from the framework baseline;
2. the candidate six-neighbor Laplacian law, `15^3` box, cutoff `R=4`, zero
   outer boundary, and trace/bulk partition;
3. 96 retained layers, `D=6^96`, 249-bit word meaning, and blank histories;
4. the Route-2 uniform seed, contraction sink, and candidate map from the
   decoded relational ratio to semigroup parameter;
5. compile-time sparse solves/eigendecomposition, adjacent-Givens synthesis,
   placement, tolerances, and resource caps; and
6. the frozen Cycle-467/470/474 physical compilers.

Derived and executed:

1. exact equality of the far-side Route-2 generator and the local 3D Schur
   complement;
2. the finite Neumann/Jacobi identity, contraction factor, error theorem, and
   `Lambda_96` residual;
3. exact 249-bit train/held word columns, zero remainders, boundary/layer
   deletions, and divider agreement;
4. complete irregular-domain color coverage, disjoint-star/capacity ledger,
   and all-24 carried covariance;
5. train/held seed residuals, adjacent-Givens E/G, inverse, semigroup, and
   deletion controls; and
6. preservation of the one-particle mass fixture.

Open:

1. physical selection of the Laplacian rather than another covariant local
   generator, and selection of box, cutoff, boundary, layer count, and seed;
2. why the classified relational interval is the physical time parameter and
   its calibration to duration;
3. exact finite Schur compilation or a controlled infinite/continuum limit,
   plus a full arbitrary-input operator rather than one seed orbit;
4. literal autonomous program synthesis, renewal, noise tolerance, boost and
   Lorentz recovery, lapse, and proper time;
5. the separate E-center readout selector; and
6. occurrence, Record formation, Born probability, realized history,
   energy/rate calibration, source tensor, backreaction, and gravity.

## Six-wall and lane effect

| wall | Cycle-479 change | remaining import |
|---|---|---|
| `C_ref` | narrows one generator choice: the existing `Lambda_R` has exact local-3D provenance | why Nature selects this Laplacian, geometry, boundary, seed, and compiler remains supplied |
| `C_num` | fixes an explicit 96-layer error envelope and held seed residual | no empirical duration, continuum scale, or precision law is derived |
| `C_wrap` | materially narrowed: physical local words now generate the finite operator family behind the Cycle-469 consumer | ratio-as-time selection, calibration, lapse, proper time, renewal, and occurrence remain open |
| `C_int` | unchanged in interpretation | no generator element is a rate and no phase is energy |
| `C_local` | narrowed: bulk relaxation, port delivery, conflict scheduling, exact word columns, and seed Givens are bounded physical programs | dense-program synthesis is compile-time; exact Schur and arbitrary-input compilation remain open |
| `C_source` | unchanged except for explicit E-shell provenance | E-center selection, mass/stress source meaning, and backreaction remain open |

This raises causal-time bridge maturity, but it does not move the Record/Born
terminal or turn a spatial relaxation ordinal into duration.

## No-Go Discipline Gate

Cycle 479 is positive but bounded with named walls.  The current no-go skill
from `origin/main` is applied.  Its result is deliberately a failed broad
negative gate.

### N1 — Alternative route enumeration

| normalized route | mechanism / terminal obligation | status |
|---|---|---|
| retained Jacobi words | local divide-six Neumann series / bounded physical `Lambda_96` provenance | **ATTEMPTED — POSITIVE** |
| exact Schur algebra | sparse elimination / exact far-side `Lambda_R` identity | **RULED IN BY PRIOR AND RECHECKED**; not yet a literal physical solver |
| reversible rational elimination | fraction-free local/bounded elimination / exact finite physical Schur action | **OPEN — NOT ATTEMPTED** |
| conjugate-gradient or Chebyshev | polynomial residual minimization / faster controlled finite solver | **OPEN — NOT ATTEMPTED** |
| multigrid/domain decomposition | local coarse corrections / size-stable convergence | **OPEN — NOT ATTEMPTED** |
| quantum-walk/resolvent | unitary local dilation / operator or spectral implementation | **OPEN — NOT ATTEMPTED** |
| other clock-derived generators | different local covariant law / empirical and operational time selection | **OPEN — NOT ATTEMPTED** |

The positive route closes “no spatial provenance” for this candidate.  The
open alternatives forbid uniqueness, optimality, minimum-content, or a time-
law no-go.

### N2 — Wall-independence audit

Collapse the remaining contracts to `W_L` law/geometry selection, `W_K`
finite-to-exact/continuum control, `W_T` ratio-as-time calibration, `W_S`
seed/readout selection, and `W_O` occurrence/Record formation.

| pair | first closes second? | second closes first? | independent here? |
|---|---:|---:|---:|
| `W_L,W_K` | no | no | yes |
| `W_L,W_T` | no | no | yes |
| `W_L,W_S` | no | no | yes |
| `W_L,W_O` | no | no | yes |
| `W_K,W_T` | no | no | yes |
| `W_K,W_S` | no | no | yes |
| `W_K,W_O` | no | no | yes |
| `W_T,W_S` | no | no | yes |
| `W_T,W_O` | no | no | yes |
| `W_S,W_O` | no | no | yes |

For example, an exact Schur solver would not identify its parameter as time;
clock calibration would not select the generator; and occurrence would not
derive continuum control.  No raw implementation detail is inflated into a
separate wall.

### N3 — Hidden-wall scan

The proof and note expose size, cutoff, boundary, trace/bulk split, Laplacian,
layer count, `D`, word precision, blank histories, seed, ratio map, compile-
time solvers, Givens completion, frames, tolerances, and resource caps.
“Framework baseline” refers only to the cited cubic adjacency premise.  No
phrase such as “naturally” or “standard QFT” carries a physics conclusion.

### N4 — Residual matching

| witness | witness residual | Cycle-479 residual | match? |
|---|---|---|---:|
| Cycle 469 | actual relational words reach a supplied `Lambda_R` seed family | physical-local provenance and finite error of that same `Lambda_R` | yes |
| Route-2 Schur boundary action | `Lambda_R` is a local 3D Schur complement | exact same matrix and partition | yes |
| Cycles 467/470/474 | arithmetic, delivery, and overlapping-star schedule | same local recurrence blocks on the irregular bulk | yes |
| Cycle 456 | classified `3:4,4:4,5:4` words | not reclassified here; consumed through the Cycle-469 ratio contract | partial provenance only |
| Record/occurrence work | actual history formation | not attacked | no; not cited as closure |
| gravity/Einstein work | metric/source/backreaction law | not attacked | no; not cited as closure |

Only the first three matching residuals support the positive provenance claim.

### N5 — Rhetoric audit

“Local” is tested per six-neighbor bulk update, per seven-supercell physical
block, per mod-three round, and over the finite `15^3` box.  It is not tested
as an autonomous infinite-lattice matrix-function compiler.  “Derived” means
matrix identity and finite recurrence from the supplied Laplacian/geometry;
it does not mean Nature selects that law.  “Time bridge” means the declared
seed consumer accepts the output; it does not mean the update ordinal is time.

### N6 — Partial-closure path scan

An exact rational Schur compiler, Chebyshev acceleration, or multigrid route
could retire `W_K` without changing axioms.  A calibrated operational clock
comparison could retire part of `W_T`.  A selected source/readout theorem
could retire `W_S`.  The approved kinetic-isotropy primitive chains only the
structural `c_t=c_s` premise and is not misrepresented as a dynamical law.

### N7 — Steelman

A hostile reviewer should reject any uniqueness or obstruction rhetoric.  The
exact finite matrix is already a Schur complement, so a reversible fraction-
free elimination or a polynomial solver could remove the `96`-layer error.
More importantly, an empirically calibrated clock could select a different
local covariant generator or seed while satisfying the same finite clock-word
fixtures.  The terminal obligations are an exact physical operator compiler
and operational duration comparison, neither of which this cycle supplies.

### N8 — Cross-cycle echo

Cycles 463, 467, 470, and 474 successively retired apparent capacity,
arithmetic, delivery, and overlap walls without axiom edits.  Cycle 469 then
retired the absence of an executable word-to-seed connection.  The same
constructive pattern now retires arbitrary-dense-matrix provenance for the
finite candidate.  It would be an error to turn the remaining precision,
selection, calibration, or occurrence work into constitutional evidence.

**Broad time-law or no-go claim: FAIL. Minimum-content claim: FAIL. Shared-
obstruction claim: FAIL. Axiom-pressure claim: FAIL. There is no axiom
pressure.**

## Optimal next campaign

The best next time-lane discriminator is an exact or accelerated local Schur
action compiler on the same physical word substrate, followed by additional
held interval ratios and a genuine operational calibration test.  It should
compare Jacobi, Chebyshev/conjugate-gradient, and multigrid routes under the
same all-24, inverse, leakage, capacity, and finite-size controls.  It must
continue to keep solver depth separate from physical duration.

The separate global priority remains occurrence/Record formation: closing the
spatial provenance of a candidate generator does not choose one realized
history or supply Born probability.

## Frozen executable disposition

The final-content cold run reports `RESULT pass=7 fail=0` in `7.3561`
seconds with raw Darwin peak RSS `870694912` bytes, below the declared
180-second and 2-GiB caps.  Runner SHA-256:
`2154075b3f1bfa3dee849eb859bad46adf3f8d07670e6ac5200f6c720b119d30`.
Authority remains none and audit remains unset.
