# Poisson Self-Gravity Loop — Zero-Coupling Exact-Reduction Narrow Theorem

**Date:** 2026-05-17
**Claim type:** positive_theorem
**Review class:** Class A -- purely algebraic code-level identity
**Lane:** poisson_self_gravity / discrete gravity probes
**Block:** physics-loop / block31 / 2026-05-17 / poisson-self-gravity-loop
**Source note:** `POISSON_SELF_GRAVITY_ZERO_COUPLING_EXACT_REDUCTION_NARROW_THEOREM_NOTE_2026-05-17.md`
**Primary runner:** [`scripts/audit_companion_poisson_self_gravity_zero_coupling_exact_reduction_narrow_2026_05_17.py`](../scripts/audit_companion_poisson_self_gravity_zero_coupling_exact_reduction_narrow_2026_05_17.py)
**Runner cache:** [`logs/runner-cache/audit_companion_poisson_self_gravity_zero_coupling_exact_reduction_narrow_2026_05_17.txt`](../logs/runner-cache/audit_companion_poisson_self_gravity_zero_coupling_exact_reduction_narrow_2026_05_17.txt)

## Scope

This note proves a single narrow code-level identity about the runner
`scripts/poisson_self_gravity_loop.py`:

> **Theorem (Zero-Coupling Exact Reduction).** With the runner's
> screened-Poisson-like field function `_poisson_like_field` and outer
> self-consistency iteration `_self_consistent_loop` taken as defined,
> for every input combination
> `(source_strength, epsilon)` with `epsilon * source_strength = 0`,
> the converged field is identically zero on every lattice cell and
> every layer, and the outer iteration returns with `field_delta == 0.0`
> in **at most two iterations** (generically two; one only if the initial
> weights already equal the zero-field fixed weights), independently of:
>
> - the source patch geometry,
> - the source weight distribution,
> - the screening parameters `(FIELD_EPS, FIELD_MU)`,
> - the field-target gain calibration,
> - the lattice geometric details from `scripts/minimal_source_driven_field_probe.py`.
>
> Consequently, the propagation step `_propagate_from_sources(lat, field_layers≡0, k, src)`
> reduces to the **bare lattice propagator** of the dependency runner, recovering
> the original free phase factor `complex(cos(k·L), sin(k·L))` per offset.

This is the structural reason the cached zero-epsilon reduction check in
`logs/runner-cache/poisson_self_gravity_loop.txt` reports an EXACT
`+0.000000e+00` centroid shift and `1.000000` escape ratio: the
arithmetic identity `0.0 * x = 0.0` for finite `x` is **bit-exact** in
IEEE-754, so the cached numeric digits are not a cancellation-floor
coincidence but an algebraic consequence.

## Why this is a narrow positive theorem and not a re-promotion

The most recent independent audit record for the broad parent
`poisson_self_gravity_loop_note` (2026-05-16) is conditional on
`missing_dependency_edge`: the loop runner inherits exact-lattice
geometry, amplitude propagation, and detector readout (recorded as
bounded admissions BA-1 through BA-3 in the parent note) from
`minimal_source_driven_field_probe.py`, which is not yet a retained-grade
dependency.

This note carves out a sub-claim that is provably true from **only the
loop runner's own code** (the function bodies of `_poisson_like_field`
and `_self_consistent_loop`), without relying on the contents of the
inherited primitives. The narrow theorem therefore:

- does **not** promote the parent note;
- does **not** close BA-1/BA-2/BA-3;
- does **not** make any claim about the nonzero-coupling rows;
- does **not** claim a self-gravity mechanism, weak-field saturation,
  or backreaction phase.

It only asserts that **one specific algebraic identity** in the loop
runner is structural, not numerical.

## Inputs consumed

| Primitive | Role | Used for |
|---|---|---|
| IEEE-754 floating-point identity `0.0 * x = 0.0` for finite `x` | platform invariant | exact bit-equality of the kernel return value |
| Python `list` and `for`-loop algebra | language semantics | iteration over `lat.nl`, `lat.npl` cells |
| The runner's own function definitions (loop / kernel as written) | runner source | scope of the identity |

No new axioms, no fitted parameters, no observational comparator, no
literature import, no upstream lattice details.

## Proof

### Part 1 — Kernel identity `_poisson_like_field(..., coupling=0.0) ≡ 0`

The kernel function (lines 139–160 of
`scripts/poisson_self_gravity_loop.py`) is:

```python
def _poisson_like_field(lat, source_nodes, weights, coupling):
    if not source_nodes:
        return [[0.0 for _ in range(lat.npl)] for _ in range(lat.nl)]
    source_pos = [lat.pos[i] for i in source_nodes]
    field = [[0.0 for _ in range(lat.npl)] for _ in range(lat.nl)]
    for layer in range(lat.nl):
        ls = lat.layer_start[layer]
        for i in range(lat.npl):
            x, y, z = lat.pos[ls + i]
            val = 0.0
            for w, (mx, my, mz) in zip(weights, source_pos):
                r = math.sqrt((x-mx)**2 + (y-my)**2 + (z-mz)**2) + FIELD_EPS
                val += w * coupling * math.exp(-FIELD_MU * r) / r
            field[layer][i] = val
    return field
```

**Case A: `source_nodes` is empty.** The early return assigns the
identically-zero field by construction. The identity is immediate.

**Case B: `source_nodes` is non-empty.** Each contribution to `val` is

```
w * coupling * math.exp(-FIELD_MU * r) / r
```

with `coupling = 0.0`. By IEEE-754 semantics, for any finite real
value `y` (and `w`, `math.exp(-FIELD_MU * r) / r` are finite given
`FIELD_EPS > 0` and `r ≥ FIELD_EPS > 0`), the multiplication
`0.0 * y = 0.0` is **bit-exact**, with no rounding error. Hence
`val += 0.0` in every inner-loop iteration, so `val` remains exactly
`0.0`. The assignment `field[layer][i] = 0.0` therefore stores exactly
`0.0`.

The outer two `for` loops over `range(lat.nl)` and `range(lat.npl)`
visit every entry of `field`, and each is assigned exactly `0.0`. So
the returned `field` is the identically-zero list of lists, regardless
of `lat`'s geometric details (which only enter as the LOOP RANGES, not
as the VALUES stored).

The boundary conditions used in Case B:
- `FIELD_EPS = 0.5` (module-level constant) is strictly positive, so
  `r = sqrt(...) + FIELD_EPS ≥ 0.5 > 0` and the division `1/r` is
  finite, never `inf`;
- `math.exp(-FIELD_MU * r)` is bounded in `(0, 1]` for `FIELD_MU > 0`
  and `r ≥ 0`, so the factor is finite;
- `w` comes from `_normalize_weights` (non-negative, bounded by 1).

All of these establish that the multiplicand `y = w * math.exp(...) / r`
is finite, so the IEEE-754 identity `0.0 * y = 0.0` applies pointwise.

**Conclusion of Part 1.** For every `lat`, every non-empty
`source_nodes`, every weight vector, and every `(FIELD_EPS, FIELD_MU)`
parameter pair with `FIELD_EPS > 0`, `_poisson_like_field(lat,
source_nodes, weights, 0.0)` returns a `lat.nl × lat.npl` list of
`0.0` entries. ∎

### Part 2 — Outer-loop convergence in at most two iterations at `epsilon * source_strength = 0`

The outer loop (lines 262–302 of `scripts/poisson_self_gravity_loop.py`):

```python
def _self_consistent_loop(lat, source_strength, epsilon, source_nodes, gain, max_iters=MAX_ITERS):
    field = [[0.0 for _ in range(lat.npl)] for _ in range(lat.nl)]
    weights = [1.0 / len(source_nodes)] * len(source_nodes)
    origin = [lat.nmap[(0, 0, 0)]]
    for iteration in range(1, max_iters + 1):
        amps = _propagate_from_sources(lat, field, m.K, origin)
        density = [abs(amps[i]) ** 2 for i in source_nodes]
        weights_next = _normalize_weights(density)
        coupling = epsilon * source_strength
        raw_field = _poisson_like_field(lat, source_nodes, weights_next, coupling)
        field_next = [[gain * v for v in row] for row in raw_field]
        field_delta = max(...)
        weight_delta = max(...)
        if field_delta < TOL and weight_delta < TOL:
            return field_next, weights_next, True, iteration, field_delta
        field = ...
        weights = weights_next
    return field, weights, False, max_iters, field_delta
```

**Hypothesis:** `epsilon * source_strength = 0` (e.g. `epsilon = 0` or
`source_strength = 0`).

**Iteration 1 walk-through:**

- `field` is initialized to all zeros.
- `coupling = epsilon * source_strength = 0` (by hypothesis; the IEEE
  identity `0 * anything = 0` is exact for finite values).
- `raw_field = _poisson_like_field(lat, source_nodes, weights_next, 0.0)`
  is the identically-zero field, by **Part 1**.
- `field_next = [[gain * v for v in row] for row in raw_field]` —
  with `raw_field[i][j] = 0.0` everywhere, `gain * 0.0 = 0.0`
  (IEEE-754 bit-exact), so `field_next` is also the identically-zero
  field.
- `field_delta = max(abs(field_next[layer][idx] - field[layer][idx])) =
  max(abs(0.0 - 0.0)) = 0.0`.

The convergence test `field_delta < TOL` becomes `0.0 < 1e-10`, which
is true. The condition `weight_delta < TOL` depends on the initial
weights vs `weights_next`. Both are non-negative and sum to 1; the
runner uses `weights = [1.0 / len(source_nodes)] * len(source_nodes)`
initially, but `weights_next = _normalize_weights(density)` is computed
from `density = [abs(amps[i])**2 for i in source_nodes]`. In general
the two weight vectors differ, so we need to check what `weights_next`
is when `field ≡ 0`.

With `field ≡ 0`, the inner propagator `_propagate_from_sources(lat, 0,
m.K, origin)` produces a layer-0-to-final-layer amplitude pattern that
is just the bare-lattice propagator from the origin. The density
samples at `source_nodes` are determined by that propagator. So
`weights_next` is generically nonzero on at least one of `source_nodes`
(see Part 3 below). The first iteration's `weight_delta` is therefore
generically positive, so the convergence test on iteration 1 may FAIL
on the conjunction with `weights`.

However:

- on iteration 2, `field` is updated via the relaxation step (`field =
  (1 - RELAX) * field + RELAX * field_next`); both summands are
  identically zero, so `field` remains identically zero;
- `weights = weights_next` is set after iteration 1, so on iteration
  2 `weights` already equals the previous `weights_next`;
- on iteration 2, `_propagate_from_sources(lat, 0, m.K, origin)` again
  produces the same amplitude pattern (deterministic function of zero
  field), so `density` and `weights_next` are bit-identical to the
  iteration-1 values, giving `weight_delta = 0.0`.

Therefore on iteration 2, **both** `field_delta = 0.0` and `weight_delta
= 0.0`, so the convergence test passes and the loop returns
`(field_next ≡ 0, weights_next, True, 2, 0.0)`.

The cached run reports `zero-epsilon iters/residual: 2 / 0.000e+00`,
which matches this prediction exactly.

**Conclusion of Part 2.** For every `(source_strength, epsilon)` with
`epsilon * source_strength = 0`, the outer self-consistency loop
converges in exactly 2 iterations (1 iteration if the initial weights
happen to equal `weights_next`, which is not guaranteed) with a
returned field identically zero and a final `field_delta` of exactly
`0.0`. ∎

### Part 3 — Reduction to the bare lattice propagator

With `field_layers ≡ 0`, the propagator inner loop (lines 196–202 of
`scripts/poisson_self_gravity_loop.py`):

```python
lf = 0.5 * (sf[si] + df[di])    # both sf, df are zero rows
act = L * (1.0 - lf)
amps[ld + di] += ai * complex(math.cos(k * act), math.sin(k * act)) * w / (L * L)
```

evaluates `lf = 0.5 * (0.0 + 0.0) = 0.0` and `act = L * (1.0 - 0.0) =
L` (the bare offset-weight). The complex phase factor reduces to
`complex(cos(k*L), sin(k*L))`, which is the FREE phase per offset of
the bare lattice propagator.

So `_propagate_from_sources(lat, field_layers ≡ 0, k, src)` reduces to
the bare lattice propagator from `src`, with no field-correction
contribution. This is independent of the lattice-specific details of
`scripts/minimal_source_driven_field_probe.py` — those details only
enter as the offset table `lat.offsets`, the per-layer indexing
`lat.layer_start`, and the per-cell weighting `lat.npl`, all of which
are LOOP STRUCTURE, not VALUE INJECTIONS.

In particular, the zero-epsilon centroid shift `_centroid_z(amps, lat)
- _centroid_z(free, lat) = 0` is automatic, because both are computed
from the **same bare-lattice amplitudes**. Likewise the zero-epsilon
escape ratio `_detector_prob(amps, lat) / _detector_prob(free, lat) =
1` is automatic.

**Conclusion of Part 3.** The zero-coupling reduction of the loop
runner to the bare lattice propagator is structural and bit-exact,
not a numerical coincidence. ∎

## What the runner verifies

The audit-companion runner
`scripts/audit_companion_poisson_self_gravity_zero_coupling_exact_reduction_narrow_2026_05_17.py`
checks the above three parts directly:

1. **Part 1 (kernel identity).** Construct synthetic `source_nodes`,
   `weights`, and a stub `lat` with arbitrary positions (so that the
   identity is provably independent of the lattice details). Call
   `_poisson_like_field(..., coupling=0.0)`. Verify EVERY returned
   entry equals `0.0` bit-exactly (`v == 0.0`, not `abs(v) < tol`).
   Repeated over multiple weight vectors, source patches, and
   `(FIELD_EPS, FIELD_MU)` parameter values.

2. **Part 1 — finite-multiplicand sanity.** Verify
   `0.0 * math.exp(-FIELD_MU * r) / r = 0.0` exactly for a stress sweep
   of `r` values in `[0.5, 100]`, demonstrating the IEEE-754 identity
   applies on the actual numerical regime used by the kernel.

3. **Part 2 (outer-loop convergence at ε=0).** Call
   `_self_consistent_loop(lat, source_strength=1.0, epsilon=0.0,
   source_nodes, gain=1e6)` for several `gain` values and verify the
   returned `converged=True`, `n_iter <= 2`, `final_field_delta == 0.0`,
   and `field_next` is identically zero. Repeat with
   `source_strength=0.0, epsilon=1.0` (the other zero-coupling case).

4. **Part 3 (bare-lattice reduction).** Construct a small lattice
   (using the actual `minimal_source_driven_field_probe.Lattice3D` so
   we exercise the real runner code) with zero field and compute the
   centroid shift and escape ratio. Verify both reduce EXACTLY to the
   free-propagator values (bit-equality, not tolerance check).

5. **Floating-point identity stress check.** For 10,000 pseudo-random
   finite floats `y` drawn from a wide log-uniform range, verify
   `0.0 * y == 0.0` bit-exactly in pure Python and via `math.fsum` to
   pin the IEEE-754 invariant on the host platform.

6. **Cross-check vs cached run.** Confirm the cached
   `logs/runner-cache/poisson_self_gravity_loop.txt` indeed shows
   `zero-epsilon centroid shift: +0.000000e+00` and
   `zero-epsilon escape ratio: 1.000000` and
   `zero-epsilon iters/residual: 2 / 0.000e+00`, validating the
   theorem against the on-disk numerical record.

## What this note explicitly does NOT claim

- Does **not** promote `poisson_self_gravity_loop_note`; the conditional
  audit finding on the parent note still rests on the inherited bounded
  admissions (BA-1)-(BA-3).
- Does **not** claim the nonzero-coupling rows converge or that the
  weak-field TOWARD sign at nonzero coupling is structural.
- Does **not** claim a self-gravity mechanism, weak-field saturation
  of GR, or any new backreaction phase.
- Does **not** claim the runner's reported Born-I3 floor at machine
  precision is structurally zero (that would require Part 5 of the
  V1-V5 angles, which is separate; here we only treat the kernel
  identity at zero coupling).
- Does **not** claim the loop/inst centroid ratio is structurally
  unity outside the zero-coupling reduction.
- Does **not** depend on or imply anything about the V3 sibling note
  (`poisson_self_gravity_loop_v3_note`), which is a separate runner
  with a separate `_run_loop` and a separate ε=0 short-circuit.
- Does **not** ratify or improve the upstream
  `minimal_source_driven_field_probe_note` audit posture. That row is
  not promoted by this theorem.

## Honest boundaries

- The proof rests on IEEE-754 semantics for `0.0 * y = 0.0` on finite
  `y`. This holds on every standards-compliant float64 implementation
  (CPython on x86_64, arm64, Apple silicon, Linux). It does NOT hold
  if any term in the inner product is `inf`, `nan`, or a non-finite
  signaling-NaN; the runner's choice `FIELD_EPS = 0.5 > 0` ensures the
  multiplicand `math.exp(-FIELD_MU * r) / r` is always finite, so
  this hypothesis is satisfied.
- The bit-exact convergence in 2 iterations depends on the runner's
  initial field `[[0.0]*lat.npl for _ in range(lat.nl)]` and the
  relaxation step `field = (1-RELAX)*field + RELAX*field_next` being
  invariant under `(0, 0) → 0`. Any future change that initialises
  the field non-zero, or that uses a relaxation other than the affine
  combination, would invalidate the convergence-iteration count
  (though not the kernel identity itself).
- Part 3's reduction holds **regardless** of the upstream lattice
  details, because the inherited primitives only contribute the LOOP
  STRUCTURE (offsets, layer indices, cell counts), not values that
  alter the zero-field arithmetic. This is the precise sense in which
  the theorem does not transit the conditional upstream.

## Derivation chain

```
IEEE-754 invariant: 0.0 * finite = 0.0
        |
        v
Part 1: _poisson_like_field(..., coupling=0.0) ≡ 0 (bit-exact)
        |
        +-- independent of lat geometry, source patch, weights,
        |   FIELD_EPS, FIELD_MU, gain
        |
        v
Part 2: _self_consistent_loop converges in <= 2 iterations at
        epsilon * source_strength = 0, with field ≡ 0
        |
        v
Part 3: _propagate_from_sources(lat, field ≡ 0, k, src) reduces
        EXACTLY to the bare lattice propagator
        |
        +-- centroid shift = 0 bit-exact
        +-- escape ratio = 1 bit-exact
```

## Manuscript-safe wording

> The `epsilon = 0` reduction of the screened-Poisson-like self-gravity
> loop runner is a bit-exact code-level identity, not a numerical
> coincidence. The IEEE-754 invariant `0.0 * y = 0.0` for finite `y`
> forces the screened-kernel field at zero coupling to be identically
> zero on every lattice cell, which in turn forces the local field
> update in the propagator inner loop to reduce to the bare lattice
> offset weight. The cached zero-epsilon centroid shift of
> `+0.000000e+00` and escape ratio of `1.000000` are therefore
> structural, not artefacts of cancellation. This narrow identity is
> independent of the upstream lattice and propagation primitives
> inherited from the dep runner; it follows purely from the loop
> runner's own kernel and outer-iteration definitions.

## Audit lane positioning

Independent audit lane only. This source note proposes a `positive_theorem`
claim type for a narrow code-level identity; it does not set or predict an
audit verdict.

- **Review class:** A (purely algebraic identity on the runner's own code).
- **Criticality:** low (a narrow code-level identity, not a physics closure).
- **Independence:** runner is self-contained exact-arithmetic verification
  using only Python `==` (bit-equality) on float64 zeros.

## Why this is a clean source-only deliverable

Per the review-loop source-only policy:

- one source theorem note,
- one paired runner,
- one cache.

No output packets, no lane promotions, no synthesis notes, no atlas
edits, no audit-data edits, no harness edits. The runner depends only
on the existing `scripts/poisson_self_gravity_loop.py` (consumed as
source-of-truth for the function bodies) and on Python's standard
`math` module. No upstream conditional row is transited.
