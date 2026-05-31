# Beta=6 SU(3) Plaquette D8 Coefficient and Single-Complex-Pair Verdict

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. The independent audit lane sets audit and
effective status.
**Primary runner:** [`frontier_beta6_connected_coefficient_2026_05_30.py`](../scripts/frontier_beta6_connected_coefficient_2026_05_30.py)

## Scope

This note extends the exact strong-coupling coefficient calculation from
[`BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md)
to order `beta^8`. Write

```text
Delta(beta) = P_full(beta) - P_1plaq(beta) = sum_{n>=5} d_n beta^n.
```

The prior notes established

```text
d_5 = 1/472392,
d_6 = 7/5668704,
d_7 = 5/17006112,
```

and certified (GF(3) cycle-space certificate) that no color-closable distinct
support of size 7, 8 or 9 exists, so the order-7 AND order-8 coefficients come
only from the four elementary cube shells through the marked plaquette via their
multiplicity sums. This note supplies the exact order-8 multiplicity sum and the
single-complex-pair falsification it enables.

## Result

The exact order-`beta^8` connected coefficient is

```text
d_8 = 5/272097792   (POSITIVE, ~= +1.8376e-8).
```

Equivalently, each of the four cube shells contributes `5/1088391168`. The
contiguous ratios are therefore

```text
d_6 / d_5 = 7/12,
d_7 / d_6 = 5/21,
d_8 / d_7 = 1/16.
```

In the per-shell bracket `Delta = (4/18^5) beta^5 [1 + c1 beta + c2 beta^2 +
c3 beta^3 + ...]`, the new coefficient is `c3 = 5/576` (with `c1 = 7/12`,
`c2 = 5/36`). The three ratios decrease super-geometrically.

## How The Runner Computes It (shape-collapse)

The order-8 per-shell contribution is a sum over the 56 multiplicity vectors
(`m_p0 >= 0`, five faces `>= 1`, total 8), each a 9-plaquette joint free-Haar
cumulant whose naive set-partition fan-out is `Bell(9) = 21147`. The brute
56-vector evaluation is the >30 min wall the order-7 optimization stopped short
of.

The single cube shell is a closed elementary 3-cube (six plaquette densities: the
marked `P0` plus five action faces; `V = 8` vertices, `E = 12` links, each link
touched by exactly two faces). Its lattice automorphism group is the full
octahedral group `O_h` (order 48). Any automorphism permutes the six faces and
leaves the joint cumulant invariant (it is a Haar integral of a symmetric function
of the six densities), so the cumulant depends ONLY on the multiset of
density-multiplicities `{1 + m_p0} U {m_s}` -- the "value shape". At order 8 the
56 vectors fall into exactly three value shapes, so the 56 distinct 9-plaquette
cumulants collapse to THREE evaluations:

```text
(1,1,1,2,2,2):  kappa = + kappa_5 / 6^3 = + 1/408146688   (three densities doubled)
(1,1,1,1,2,3):  kappa = 0                                  (one tripled, one doubled)
(1,1,1,1,1,4):  kappa = - 5 kappa_5 / 6^3 = - 5/408146688  (one density quadrupled)
```

with `kappa_5 = 1/18^5` the engine-anchored bare cube cumulant
([`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md)
Theorem 4: `kappa_5 = 2 (1/6)^6 3^(V-E) = 1/18^5`), and the `-5` the
single-plaquette `kappa_5(X) = -5/3888`. Assembled with the exact rational
symmetry weights `sum 1/(m_p0! prod m_s!)` per shape (`3/8`, `15/4`, `15/4`):

```text
per-shell d_8 = (3/8)(-5/408146688) + (15/4)(0) + (15/4)(+1/408146688)
              = 5/1088391168,
        d_8   = 4 x per-shell = 5/272097792.
```

The runner does NOT assume the octahedral invariance: for each shape it computes
a SECOND, geometrically-distinct representative (a different `m_p0` split,
including the `m_p0 = 0` face-only case and an `m_p0 > 0` case) and raises if the
two disagree, so the collapse is self-validated each run. It was so validated:
e.g. the `(1,1,1,1,1,4)` shape gives `-5/408146688` both for a quadrupled face
(`m_p0 = 0`) and for a quadrupled `P0` (`m_p0 = 3`).

### Two-engine verification

The order-8 novelty is the SU(3) link integrals at the higher per-link degrees the
9-plaquette words reach (each moment factorizes over links into single-link
invariant-projector integrals; busiest realized link `(4,1)/(1,4)`); the Moebius
cumulant assembly is identical set-partition combinatorics in both engines (V4b
validated it at order `<= 6`). The order-8 verification therefore has three legs:

- The optimized `Fraction` engine reproduces the sympy engine's `d_5` and `d_6`
  exactly (V4b, unchanged), and reproduces `d_7 = 5/17006112` exactly.
- At order 8, each shape cumulant matches the closed-form law `kappa_5/6^k`
  (V7), an engine-independent cross-check of all three values.
- The in-runner second-engine check (V7) is the EXACT per-link tensor agreement:
  the sympy invariant-projector tensor reproduces the optimized `Fraction` link
  tensor at every per-link degree realized in order-8 cube-shell moments
  (including the busiest `(4,1)/(1,4)`, 1080 nonzero entries each, zero
  mismatches; ~2 s). This independently validates the SU(3) integral formulas --
  the genuinely-new order-8 content -- at the per-link level.
- The full sympy `joint_cumulant` on a 9-plaquette word walks `Bell(9) = 21147`
  set partitions of sympy moments and hits the documented ~270 s/word contraction
  wall (worse at 9 plaquettes than the 8-plaquette case). It is therefore not
  gated in the default run; the runner exposes it behind a `deep` flag
  (`python3 ... 8 deep`) as the one-time publication-grade 9-plaquette two-engine
  confirmation on the cheap `(1,1,1,2,2,2)` shape (`= 1/408146688`).

The review-loop run reproduced the runner's `maxorder=8` path:

```text
d_5 = 1/472392
d_6 = 7/5668704
d_7 = 5/17006112
d_8 = 5/272097792
```

## Single-Complex-Pair Verdict (the decisive falsifier)

A constant-amplitude single dominant complex-conjugate pair -- the analytic class
on which the d-log-Pade route is premised
([`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`](BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md))
-- makes the connected coefficients satisfy a 2-term recurrence with complex
roots. The minimal `[0/2]` Pade of the bracket, fixed by `d_5, d_6, d_7`, has
denominator `1 - c1 beta + (c1^2 - c2) beta^2` with discriminant

```text
4 c2 - 3 c1^2 = -67/144 < 0   (a complex-conjugate pair),
```

and predicts the next bracket coefficient `c3^pred = c1 c2 - (c1^2 - c2) c1`,
giving a NEGATIVE predicted `d_8` -- a SIGN CHANGE relative to the positive
`d_5, d_6, d_7`. (The exact predicted magnitude is convention-dependent across
single-pair fits: the `[0/2]` recurrence gives `~ -7.7e-8`, and a
constant-amplitude pure-oscillation fit gives `~ -3.26e-7`; the robust falsifiable
feature shared by all single-pair conventions is the sign change to negative.)

The exact `d_8` was computed INDEPENDENTLY above (shell multiplicity + exact SU(3)
link integrals), then compared:

```text
d_8^exact = 5/272097792 = +1.8376e-8   (POSITIVE, same sign as d_5, d_6, d_7).
```

There is NO sign change. The single-complex-pair ansatz is **falsified** at order
8: the series is not controlled by a single dominant complex-conjugate pair. This
independently corroborates and extends the order-7 tadpole/geometric falsification
(`d_7/d_6 = 5/21 != 7/12`); the clean super-geometric ratios `7/12, 5/21, 1/16`
look entire-function-like.

## d-log-Pade Activation (and its self-contradiction at [1/1])

`d_5..d_8` are the four contiguous coefficients the resummation harness
([`BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md`](BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md))
names as the d-log-Pade activation minimum: three coefficients of
`H = (log h)'`. The new `d_8` supplies the third,

```text
H0 = 7/12,   H1 = 2 c2 - c1^2 = -1/16,   H2 = 3 c3 - 3 c1 c2 + c1^3 = -1/54,
```

with `H0, H1` matching the analytic-class note exactly. So the `beta^8` rank floor
is now met and the `[1/1]` d-log-Pade predictive test is ACTIVATED.

However, the activation coefficient `d_8` immediately contradicts the `[1/1]`'s
own single-pole premise. The `[1/1]` d-log-Pade from `d_5..d_8` returns a spurious
REAL pole at `beta_c ~ 3.375` (`arg = 0`) and a non-physical `Delta(6) ~ 1.19`, so
the implied `<P>(6) = P_1plaq(6) + Delta(6) ~ 1.62` -- far from the `0.594`
Monte-Carlo comparator. The `[1/1]` is the lowest-order balanced d-log-Pade and,
with only the activation-minimum data, does not localize the physical off-axis
complex pair; it manufactures a real pole instead. This matches the analytic-class
note's verdict that proving the analytic class buys the correct CLASS of tool but
not a controlled closure: reliable continuation past the radius to `beta = 6`
needs far more than four coefficients.

## Boundary

This is not a `P(beta=6)` derivation, not an `alpha_s` derivation, and not a
closed boosting form. It proves one exact coefficient (`d_8 = 5/272097792`), rules
out the single-complex-pair continuation pattern, and ACTIVATES (but does not pass)
the `[1/1]` d-log-Pade predictive test.

Per the retained infinite-hierarchy obstruction
([`GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md)),
no finite-order truncation of the connected hierarchy closes the thermodynamic
`<P>(6)`. The GF(3) certificate also shows `Delta = 4 C_cube` is exact only through
`d_8`: the distinct-support side reopens at 2-cycle weight 10 (the order-`beta^9`
coefficient `d_9` acquires 80 new non-cube supports), so this engine's
shape-collapse does not by itself continue past `d_8` without enumerating the new
support class. With the single-complex-pair continuation falsified and the `[1/1]`
d-log-Pade self-contradicting, beta=6 closure still requires a separate dynamical
input for the boundary character measure `rho_{p,q}(6)` (under-determined by local
data and treewidth-29 infeasible at `L_s >= 3`); this note does not supply one.
`0.594` is a Monte-Carlo comparator, never a derivation input.

## Key Files

- [`scripts/frontier_beta6_connected_coefficient_2026_05_30.py`](../scripts/frontier_beta6_connected_coefficient_2026_05_30.py) (this note's runner; `maxorder=8` adds V7/V7b/V7c)
- [`BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md)
- [`BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md)
- [`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`](BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md)
- [`BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md`](BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md)
- [`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md)
- [`GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md)
- [`BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md)
