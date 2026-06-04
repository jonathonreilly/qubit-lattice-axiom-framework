# Beta=6 SU(3) Plaquette Weight-10 Two-Cube Candidate: Bounded Finite-Order Validation

**Date:** 2026-06-04
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. The independent audit lane sets audit and
effective status.
**Primary runner:** [`frontier_beta6_twocube_closedform_2026_06_04.py`](../scripts/frontier_beta6_twocube_closedform_2026_06_04.py)

## Scope

This note validates a **candidate** closed-form contribution for the leading
non-cube weight-10 class in the SU(3) Wilson single-plaquette connected
strong-coupling series

```text
Delta(beta) = P_full(beta) - P_1plaq(beta) = sum_{n>=5} d_n beta^n.
```

It builds on the cube-sector closed-form surface
[`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`](BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md)
and the first non-cube coefficient surface
[`BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md).
The imported cumulant/projector implementation is
[`scripts/frontier_beta6_d9_coefficient_2026_06_04.py`](../scripts/frontier_beta6_d9_coefficient_2026_06_04.py).

The bounded landed claim is finite-order:

- enumerate the weight-10 two-cube supports through `p0`;
- verify the geometric count `60`;
- compute the exact weight-10 class coefficients at orders 9 and 10;
- check that the candidate `1080 K''(K')^9` matches those orders, with order 10
  held out after fixing the order-9 normalization;
- reject the naive wrong-exponent control `(K'')^2(K')^9` at order 10.

This note does **not** prove the all-order closed form for the weight-10 class.
It records the all-order expression as a candidate that has passed the bounded
finite-order checks above. Weight 11, weight 12, higher clusters, and the
retained infinite-hierarchy obstruction remain open.

## Candidate Form

The cube sector is

```text
Delta_cube(beta) = 72 * K''(beta) * (K'(beta))^5,   K = log J,
```

where `J(beta)` is the SU(3) single-link generating integral from the
dominant-weight recurrence. Structurally this is

```text
(# cubes through p0) * 18 * K'' * (K')^(F-1),   F = 6 faces,
```

with `# cubes through p0 = 4` and `18 = 1/<X_p0^2>`.

The candidate leading non-cube class is the weight-10 two-cube class: two
elementary cubes sharing one face, with GF(3) coefficients `(1,2)` so the
shared face cancels, leaving `F = 10` distinct faces. The runner verifies that
there are exactly `60` such configurations through `p0`, stable between radius
2 and radius 3. Applying the same marked-face pattern gives the candidate

```text
Delta_2cube_candidate^(w10)(beta)
    = 1080 * K''(beta) * (K'(beta))^9
    = (60 configs) * 18 * K'' * (K')^(F-1),   F = 10.
```

The prefactor `1080 = 60 * 18` is forced **for this candidate pattern**. The
runner does not prove that the pattern continues to all orders for the
weight-10 class.

## Finite-Order Validation

The runner computes the exact weight-10 class coefficients by orbit collapse.
The 60 supports form one lattice-symmetry orbit; with `nreps=1` the cache uses
one canonical representative, and optional larger `nreps` runs can re-check
representative equality. Each per-support contribution is an exact `Fraction`
connected-cumulant sum over multiplicity vectors, with each moment evaluated by
the SU(3) invariant-projector machinery imported from the D9 runner.

Primary cache scope:

```text
order   exact weight-10 class      1080 K''(K')^9 [beta^n]       role
  9     5/16529940864              5/16529940864                 fixes A
 10     55/198359290368            55/198359290368               held out
```

The order-9 value regresses the D9 note's new-support part. The order-10 value
is the bounded out-of-sample check in this landed packet.

## Discrimination Control

The runner rejects the nearest wrong-exponent control

```text
19440 * (K'')^2 * (K')^9.
```

That form can be normalized to match order 9, but it predicts order 10 as
`65/198359290368`, while the exact weight-10 class gives
`55/198359290368`; the actual/predicted ratio is `11/13`. This is a real
discrimination check, not a uniqueness theorem over all possible multi-term or
higher-derivative forms.

## Candidate Beta=6 Readout

Because the candidate expression is built from `K'` and `K''`, the runner can
evaluate it at `beta = 6` using the same `J` recurrence:

```text
1080 K''(K')^9 at beta=6 = 0.030079587...
```

This is a **candidate resummed contribution**, not a derivation of
`P(beta=6)`. If inserted into the existing backbone, it moves the model readout
from `0.485445` to `0.515525` and shrinks the comparator gap by about `28%`.
The Monte-Carlo value near `0.594` is a comparator only, never an input.

## Boundary

This packet is bounded to the exact order-9/order-10 validation of the weight-10
two-cube candidate and the associated candidate beta=6 readout. It does not
close beta=6, does not prove the all-order two-cube closed form, does not supply
weight-11/12 or higher-cluster forms, and does not repin any canonical
plaquette value, `u_0`, or `alpha_s`.

## Key Files

- [`scripts/frontier_beta6_twocube_closedform_2026_06_04.py`](../scripts/frontier_beta6_twocube_closedform_2026_06_04.py)
- [`scripts/frontier_beta6_d9_coefficient_2026_06_04.py`](../scripts/frontier_beta6_d9_coefficient_2026_06_04.py)
- [`BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md)
- [`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`](BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md)
- [`GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md)
