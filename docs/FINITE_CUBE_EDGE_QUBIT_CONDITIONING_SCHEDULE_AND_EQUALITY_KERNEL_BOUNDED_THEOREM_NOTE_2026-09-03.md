---
claim_id: finite_cube_edge_qubit_conditioning_schedule_and_equality_kernel_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "For the explicitly defined 2x2x2 cube graph with one abstract qubit on each of its 12 edges, the displayed superfast matrices, the 896-dimensional weight-two vertex-parity sector, one specified -4 eigenvector, coordinate-mask conditioning, the declared sub-sum generators H_R, five named schedules at tau=0.5, and 12 independent geometric clocks: (T1) the finite encoding relations, sector closure, five-valued spectrum, and 384 coordinate zeros hold exactly; (T2) full coordinate conditioning gives an aggregated 28-outcome Born law with sixteen probabilities 1/16 and twelve zeros, independent of mask order; (T3) the averaged projected mass has local expansion m(t)=t^2/8+O(t^4), with zero cubic coefficient, and four pinned finite-time values; (T4) the common action-equality kernel of the explicitly stated generator-difference equations is zero; (T5) the five named schedules give the pinned, pairwise-distinct terminal distributions for this one state and tau; and (T6) the geometric completion law and expectation hold for 0<p<=1 and integer ticks. Edge, vertex, parity, occupation, conditioning, and schedule are abstract graph, basis, and algorithmic labels. No physical-site realization, framework Record semantics, state-invariance theorem, universal schedule claim, update law, or large-system limit is asserted."
upstream_dependencies: []
runner: scripts/finite_cube_edge_qubit_conditioning_schedule_and_equality_kernel_check_2026_09_03.py
---

# Finite cube edge-qubit conditioning, schedule distributions, and an action-equality kernel

**Date:** 2026-09-03

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Primary runner:**
[`scripts/finite_cube_edge_qubit_conditioning_schedule_and_equality_kernel_check_2026_09_03.py`](../scripts/finite_cube_edge_qubit_conditioning_schedule_and_equality_kernel_check_2026_09_03.py)

**Runner cache:**
[`logs/runner-cache/finite_cube_edge_qubit_conditioning_schedule_and_equality_kernel_check_2026_09_03.txt`](../logs/runner-cache/finite_cube_edge_qubit_conditioning_schedule_and_equality_kernel_check_2026_09_03.txt)

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite algebra and deterministic finite-dimensional evaluations for one declared graph, sector, state, generator family, and schedule list."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Independently reproduce the exact algebra, the local Taylor coefficient, the pinned schedule values, and the geometric-clock identities."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Scope boundary

This is a self-contained theorem about finite matrices and finite probability
distributions. The words *edge*, *vertex*, *parity*, and *occupation* name graph
objects and basis labels. A coordinate mask is a mathematical projector onto a
chosen computational-basis value; it is not asserted to be a physical
measurement, a formation process, or a framework update rule.

The result does not identify edge qubits with physical lattice sites. It does
not prove that any state is or is not invariant under a family of dynamics. In
particular, the action-equality equations in Theorem 4 are narrower than common
eigenvector, invariant-ray, or stationary-density-matrix conditions. The five
schedule results apply only to the declared state, `tau=0.5`, and the five named
schedules. No statement is made for every state, every positive time, another
graph, or a thermodynamic limit.

## Imports and authority

There are no load-bearing scientific dependencies. The finite graph,
operators, sector, state, masks, schedules, and clock process are all declared
below and reconstructed by the runner. Pauli multiplication, commuting
projectors, Slater vectors, finite-dimensional unitary evolution, and the
geometric distribution are standard mathematical methods, not imported
results. No empirical input, fitted value, open change request, or audit verdict
is used.

## Definitions

Let the vertices of the open cube graph be the bit strings `0,...,7`, with an
edge between vertices that differ in one bit. There are twelve edges and six
square faces. Put one abstract qubit on each edge, with the following operators:

```text
A_ij = X_ij times the ordered Z strings at i and j,   A_ji = -A_ij,
B_v  = product of Z_e over edges incident on v,
S_f  = ordered product of A_ij around face f,
T_e  = (i/2) A_ij (B_i - B_j),
H    = sum_e T_e.
```

For a computational-basis bit string `y`, define the vertex-parity dictionary

```text
n_v(y) = (1 - B_v(y))/2 = |y intersect star(v)| mod 2.
```

The working sector is the span of all `y` for which `sum_v n_v(y)=2`. It has
dimension `896`: 28 unordered vertex pairs, each with 32 edge-bit strings.
The 28-dimensional code-sector reference matrix is the ordinary two-particle
signed hopping matrix on the same vertex-pair labels.

Choose the exact `-4` Slater eigenvector `g` constructed by the runner. Its
896-dimensional lift has Gaussian-integer coordinates divided by `sqrt(2048)`.
Let `Q` project onto the 384 coordinates associated with the twelve vertex pairs
whose vertices lie in a common `x` face; these coordinates vanish in `g`.

For a set `R` of masked edge coordinates, define

```text
H_R = sum of T_e over e not in R.
```

This is only the maximal sub-sum of the displayed fixed-coefficient term family
that omits every masked coordinate. It is not claimed to be the unique operator
with any broader property.

A schedule is a finite list of `(gap, coordinates masked next)` pairs. At each
masking stage the runner enumerates both coordinate values with their Born
weights, restricts to the corresponding subspace, normalizes, and evolves for
the declared gap under the current `H_R`. Thus every terminal distribution is a
deterministic enumeration, not a sample.

## Exact target and proof graph

The target is exactly `T1` through `T6`, corresponding to runner groups `A`
through `F`. The dependency graph is acyclic:

```text
P0  declared graph, matrices, sector, state, masks, schedules, clock
 |-- P1 / A  finite encoding and spectrum
 |-- P2 / B  full-mask Born law and order independence
 |-- P3 / C  conditioned variances and local projected leakage
 |-- P4 / D  explicitly defined common action-equality kernel
 |-- P5 / E  five distributions at tau=0.5
 `-- P6 / F  independent geometric-clock law
```

Statements tagged `[exact]` in the cache use binary, integer,
Gaussian-integer, or rational arithmetic. Statements tagged `[numerical]` use
deterministic double-precision diagonalization and are pinned to absolute error
`1e-12`. Decimal renderings of exact rational values are labelled as displays,
not exact decimal equalities.

## Theorem 1: finite encoding, sector, spectrum, and coordinate zeros

On the declared cube, the checked superfast relations `R0` through `R4` hold;
the independent face-stabilizer rank is five, `-I` is absent, and the code
dimension is `2^12/2^5=128`. Every `T_e` preserves the 896-dimensional
weight-two parity sector with unit Gaussian-integer amplitudes, and `H` is
Hermitian there.

On the 28-dimensional code sector, the scaled encoded matrix is
Gaussian-integer and an exact diagonal gauge in `{1,i,-1,-i}` maps it entrywise
to the declared reference matrix. The 28 integer Slater vectors are mutually
orthogonal and form a complete eigenbasis with spectral set
`{-4,-2,0,2,4}`. The selected `-4` eigenvector lifts exactly to the
Gaussian-integer vector over `sqrt(2048)` and has precisely 384 zero
coordinates, corresponding to twelve same-`x`-face vertex pairs times 32.

## Theorem 2: full coordinate conditioning

Conditioning all twelve commuting `Z_e` coordinates before evolution produces
the computational-basis Born law of `g`. Aggregating by the 28-outcome parity
dictionary gives sixteen probabilities `1/16` and twelve zeros, summing to one.

All 66 pairs of coordinate projectors commute. The runner also checks all 264
ordered `(coordinate,value)` pairs entrywise and follows 20 deterministic
permutations of all twelve masks for three nonzero target bit strings. Every
chain-rule product equals the same exact rational Born weight.

## Theorem 3: local projected leakage for the declared generator family

Condition `g` on either value of one edge coordinate. For each of the eight
edges lying inside an `x` face, the conditioned variance of `H_R` is `1/4`; for
each of the four edges joining the two `x` faces it is `3/8`. Every one of the
24 conditioned states has variance `3/4` under `H`.

For the same conditioned vectors,

```text
||Q H_R g_(e,b)||^2 = 0    on the eight in-face edges,
||Q H_R g_(e,b)||^2 = 3/8  on the four cross-face edges.
```

Averaging both values at each edge with their exact weights, the projected mass
after one conditioning and one evolution interval has the local expansion

```text
m(t) = t^2/8 + O(t^4).
```

The quadratic coefficient is computed exactly and every one of the 24 cubic
coefficients is checked to vanish exactly. This is a local expansion; it does
not assert positivity at every later time. Direct deterministic evaluations are

| `t` | `m(t)` |
|---:|---:|
| 0.01 | 0.000012499583337962187 |
| 0.1 | 0.0012458378813747014 |
| 0.5 | 0.028693840474726454 |
| 2.0 | 0.11867214924360606 |

## Theorem 4: a common action-equality kernel

For the twelve single-coordinate masks, consider only the explicitly displayed
linear equations

```text
(H_R - H_R') v = 0  for all 66 unordered pairs R,R',
(H_R - H) v = 0     for all 12 single-coordinate R.
```

Their common kernel on the 896-dimensional sector has dimension zero. The
runner proves this with 69,888 unit-ratio constraints and exact union-find phase
bookkeeping in `Z4`. It separately verifies that every term matrix has a
nonzero exact commutator with `H`.

This theorem concerns equality of generator actions under those equations. It
does not concern common eigenrays or invariant density matrices and carries no
negative conclusion about states.

## Theorem 5: five distributions for one state and one time

For `g`, `tau=0.5`, and the five named schedules below, all schedules eventually
mask the same twelve coordinate positions. They produce the following
28-outcome parity-dictionary distributions:

| schedule | projected mass on the 12 zero-at-start outcomes | L1 to the initial aggregated Born law |
|---|---:|---:|
| A: all 12 at the first stage | 0 | 0 |
| B: one per stage, order 0 through 11 | 0.5351269054666328 | 1.1023355969148596 |
| C: one per stage, order 11 through 0 | 0.3337405248788735 | 0.7704538825748932 |
| D: one every five intervals | 0.14798987244388517 | 0.6919682523557236 |
| E: two per stage for six stages | 0.2603867692315665 | 0.5513993863148097 |

Additionally, `L1(A,B)=1.1023355969148596`,
`L1(B,C)=0.9027794461083645`, and the smallest distance among the ten schedule
pairs is `0.5513993863148097`. These are existence results at the stated state,
time, and schedule list only.

## Theorem 6: independent geometric-clock identity

Let twelve independent coordinate-activation times be geometric random
variables supported on the positive integers, each with `0<p<=1`, and let
`T` be their maximum. For integer `t>=0`,

```text
P(T <= t) = (1 - (1-p)^t)^12,
E[T] = sum_{j=1}^{12} (-1)^(j+1) C(12,j) / (1 - (1-p)^j).
```

The runner checks the inclusion-exclusion expression exactly against a finite
tail decomposition and pins exact rational values at
`p in {1,1/2,1/5,1/20,1/100}`. Their decimal displays are approximately
`1.000, 4.977, 14.407, 60.999, 309.267`. At `p=1/2`, the exact CDF values are
also pinned for `t in {1,3,5,7}`. This clock calculation is independent of the
matrix and conditioning theorems.

## Reproduction

```bash
python3 scripts/precompute_audit_runners.py \
  --runners scripts/finite_cube_edge_qubit_conditioning_schedule_and_equality_kernel_check_2026_09_03.py \
  --force --push-mode none --allow-non-main
```

The cache must identify the runner by path and SHA-256, complete within the
declared timeout, contain the exact pinned output, report zero failures, and
carry a successful exit code. No audit verdict is created or changed here.
