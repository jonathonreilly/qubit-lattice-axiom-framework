# Beta=6 SU(3) Plaquette D8 Coefficient and Single-Complex-Pair Verdict

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no status verdict.
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
feature shared by the tested single-pair closures is the sign change to negative.)

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
(`BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md`)
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

Per the infinite-hierarchy obstruction
([`GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md)),
no finite-order truncation of the connected hierarchy closes the thermodynamic
`<P>(6)`. The GF(3) certificate also shows `Delta = 4 C_cube` is exact only through
`d_8`: the distinct-support side reopens at 2-cycle weight 10 (the order-`beta^9`
coefficient `d_9` has a new weight-10 two-cube support class; the current exact
`d_9` source enumerates 60 distinct supports, while the GF(3) certificate's
`weights[10] = 80` is a combination count), so this engine's shape-collapse does
not by itself continue past `d_8` without enumerating the new support class. With
the tested single-complex-pair continuation falsified and the `[1/1]`
d-log-Pade self-contradicting, beta=6 closure still requires a separate dynamical
input for the boundary character measure `rho_{p,q}(6)` (under-determined by local
data and treewidth-29 infeasible at `L_s >= 3`); this note does not supply one.
`0.594` is a Monte-Carlo comparator, never a derivation input.

## No-go discipline gate (N1-N8)

This gate scopes the **negative/bounded component only**: the
Single-Complex-Pair Verdict. The defended claim is the single falsifiable
statement that

> a constant-amplitude single **dominant** complex-conjugate pair (the analytic
> sub-class on which the d-log-Pade route is premised) is **falsified at order
> 8**, because the tested single-pair closures predict a **sign change to
> negative** at `d_8`, whereas the independently computed exact
> `d_8 = 5/272097792 = +1.8376e-8` is **positive** (same sign as
> `d_5, d_6, d_7`); and the `[1/1]` d-log-Pade, now ACTIVATED by the four
> contiguous coefficients `d_5..d_8`, **self-contradicts** its own single-pole
> premise (manufactures a spurious real pole at `beta_c ~ 3.375`,
> `arg = 0`, instead of the expected off-axis pair).

The exact value `d_8 = 5/272097792` is a **positive** result (a two-engine
verified arithmetic identity), not a no-go; it is the *witness*, not the
*claim*. The robust falsified feature is the **sign** of `d_8`, NOT the
convention-dependent predicted magnitude (`[0/2]` recurrence gives `~ -7.7e-8`,
the constant-amplitude pure-oscillation fit gives `~ -3.26e-7`).

### N1 - Alternative route enumeration

Routes by which the single-complex-pair (constant-amplitude, single dominant
pair) continuation could *survive* order 8, and why each fails for this scoped
falsifier:

| route | what it would attempt | why it fails for this scoped claim | marker |
|---|---|---|---|
| `[0/2]` Pade recurrence | Fit the bracket `[1, c1, c2] = [1, 7/12, 5/36]` to a 2-term recurrence `1 - c1 beta + (c1^2 - c2) beta^2` and read off `c3^pred = c1 c2 - (c1^2 - c2) c1`. | `disc = 4 c2 - 3 c1^2 = -67/144 < 0` (genuine complex pair), but the predicted `d_8 < 0` (sign change); exact `d_8 = +1.8376e-8 > 0`. | ATTEMPTED |
| Constant-amplitude pure oscillation | Fit `d_n ~ A R^{-n} cos(n theta + phi)` to `d_5, d_6, d_7` and extrapolate to `d_8`. | A single constant-amplitude oscillator forces an eventual sign change; this convention predicts `d_8 ~ -3.26e-7 < 0`. Exact `d_8 > 0`. | ATTEMPTED |
| Convention-shift escape within the tested closures | Argue the negative prediction is an artifact of a particular Pade/fit convention, so the tested route can absorb `d_8 > 0`. | The two closures tested here (`[0/2]` recurrence and constant-amplitude pure oscillation) both predict `d_8 < 0`; only the magnitude is convention-dependent inside this test. A different parametrization is a new ansatz, not a rescue of this one. | ATTEMPTED |
| `[1/1]` d-log-Pade rescue | Use the four contiguous `d_5..d_8` to build the activated `[1/1]` d-log-Pade and claim it localizes the physical off-axis pair. | The activated `[1/1]` returns a **spurious real pole** at `beta_c ~ 3.375` (`arg = 0`) and `Delta(6) ~ 1.19` (`<P>(6) ~ 1.62` vs `0.594`); the activation coefficient `d_8` contradicts the `[1/1]`'s own single-pole premise. | ATTEMPTED |
| Wrong-sign arithmetic route | Claim the single-pair route survives because the exact `d_8` sign is a computation error. | The sign is checked by the shape-collapse assembly, the `kappa_5/6^k` closed-form law for all three shapes, and exact per-link sympy-vs-Fraction tensor agreement at every order-8 degree. | ATTEMPTED |
| Multi-pair / variable-amplitude | Drop "single dominant" and allow several pairs or a non-constant amplitude consistent with `d_8 > 0`. | This is **outside** the scoped claim: the verdict falsifies only the *constant-amplitude single dominant pair*. Multi-pair and amplitude-varying (entire-function-like) models are explicitly left open. | OUT OF SCOPE |
| Higher-order continuation | Push to `d_9` and beyond, where the cube-shell engine reopens. | This neither rescues nor refutes the order-8 single-pair verdict; it is a separate future computation. The current exact `d_9` source handles the reopened weight-10 two-cube support class. | OUT OF SCOPE |

### N2 - Wall-independence audit

The collapsed wall set for the scoped falsifier is **one wall**: the *sign* of
the exact order-8 coefficient (`d_8 > 0`) contradicts the *negative* sign
predicted by the two constant-amplitude single-pair closures tested here. The
`[1/1]` self-contradiction (spurious real pole) is **not an independent wall**;
it is the same fact viewed in the d-log-Pade representation (the same positive
`d_8` that breaks the sign also breaks the `[1/1]` single-pole localization). The
order-7 tadpole/geometric falsification (`d_7/d_6 = 5/21 != 7/12`) is a *prior,
weaker* wall against a narrower (geometric / single-real-pole) sub-class, which
this note extends — it is corroborating, not a second independent wall for the
*complex*-pair claim. What could change the verdict: a corrected exact `d_8`
(ruled out by the two-engine + closed-form `kappa_5/6^k` cross-checks, V7), or a
re-scoping to multi-pair / amplitude-varying models (which the claim does not
touch).

### N3 - Hidden-wall scan

No rhetorical phrase carries a hidden accepted input. "Falsified", "decisive
falsifier", and "self-contradiction" are not load-bearing premises — they label
explicit arithmetic. The EXPLICIT load-bearing inputs of the scoped negative
claim are:

1. the exact bracket coefficients `c1 = 7/12`, `c2 = 5/36` (from `d_5, d_6, d_7`,
   themselves two-engine verified in the predecessor notes);
2. the exact order-8 coefficient `d_8 = 5/272097792`, computed **independently**
   of any continuation ansatz (octahedral shape-collapse of the four cube-shell
   9-plaquette cumulants + exact SU(3) single-link integrals; V7/V7b/V7c);
3. the definition of the constant-amplitude single dominant complex-conjugate
   pair class (a 2-term real recurrence with `disc < 0`), taken from
   [`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`](BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md);
4. the elementary fact that the `[0/2]` and pure-oscillation closures predict a
   negative next coefficient for these inputs.
The infinite-hierarchy obstruction and the GF(3) cycle-space
certificate bound the *positive* d_8 computation's validity window (exact only
through `d_8`); they are not used to manufacture the negative verdict. `0.594`
is a Monte-Carlo comparator, consumed only to display the `[1/1]`'s failure, not
as a derivation input.

### N4 - Residual matching

| cited witness | residual attacked | residual here | match? |
|---|---|---|---|
| [`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`](BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md) | The d-log-Pade route is premised on a single dominant complex-conjugate pair, but with only `d_5..d_7` the class is *type-discriminated, not tested* (and `d_8` is "at/past the treewidth-29 wall"). | Supplies the exact `d_8` and tests that premise: the tested single-pair closures are falsified by the positive sign. | yes |
| [`BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md) | The single-ratio geometric / tadpole continuation (`d_7^pred = (d_6/d_5) d_6`) is falsified (`d_7/d_6 = 5/21 != 7/12`). | Extends that to the *complex*-pair sub-class via the sign of `d_8`; the geometric falsification is the order-7 predecessor of this order-8 verdict. | yes |
| `BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md` | `d_5..d_8` (`beta^8`) is the class-independent rank floor that ACTIVATES the `[1/1]` d-log-Pade predictive test. | The new `d_8` meets the floor and activates the test, which then self-contradicts. | yes |
| [`GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md) | No finite-order truncation closes the thermodynamic `<P>(6)`. | Boundary disclaimer: this note does **not** claim beta=6 closure. Not load-bearing for the single-pair *falsifier* itself. | not load-bearing |
| [`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md) Theorem 4 | Engine-anchored bare cube cumulant `kappa_5 = 1/18^5`. | Positive arithmetic input to the exact `d_8` witness (the `kappa_5/6^k` shape law). Supports the witness, not the negative claim's logic. | not load-bearing |

Witnesses marked "not load-bearing" are cited for boundary/witness context and
are not used as proof of the single-complex-pair falsification.

### N5 - Rhetoric audit

The broad phrases are scoped to the exact claim:

- **"the decisive falsifier" / "falsified"** — scoped to the *constant-amplitude
  single dominant complex-conjugate pair* class. It does **not** mean the broader
  off-axis complex-conjugate-pair *class* (multiple pairs, varying amplitude,
  entire-function-like ratios) is falsified; the clean super-geometric ratios
  `7/12, 5/21, 1/16` in fact "look entire-function-like", which is consistent
  with the surviving broader class.
- **"verdict"** — a verdict on one ansatz at one order (`d_8`), not a verdict on
  the beta=6 lane.
- **"self-contradiction at `[1/1]`"** — scoped to the lowest-order balanced
  d-log-Pade built from exactly the activation-minimum data; it does **not** mean
  higher-order `[n/n]` d-log-Pade is foreclosed (the harness shows `[10/10]`
  localizes a complex pair on the proxy).
- **"bounded"** — the note is a bounded source proposal; it asserts **no** value
  of `P(beta=6)`, `u_0`, or `alpha_s`, and **no** status verdict.

Disclaimer against an over-broad reading: this note does **not** claim "no
resummation/analytic continuation can ever reach beta=6", does **not** claim the
complex-pair *class* itself is wrong, and does **not** repin the canonical
plaquette value. It removes exactly one ansatz (constant-amplitude single
dominant pair) at exactly one order.

### N6 - Partial-closure path scan

Open, non-axiom partial-closure paths that remain after this falsifier (none is
a new axiom or fitted input):

1. **Multi-pair / variable-amplitude continuation** — a model with two or more
   complex-conjugate pairs, or a non-constant amplitude, consistent with a
   positive `d_8`; explicitly left open.
2. **Higher-order coefficients** `d_9, d_10, ...` — past the cube-shell window
   (GF(3) certificate reopens at 2-cycle weight 10; the current exact `d_9`
   source enumerates 60 distinct weight-10 two-cube supports), via a contraction
   engine that defeats the treewidth wall.
3. **Higher-order d-log-Pade** `[n/n]`, `n >= 2`, fed by additional exact
   coefficients, which could still localize an off-axis pair the `[1/1]` cannot.
4. **An independent dynamical input** for the boundary character measure
   `rho_{p,q}(6)` (the existing beta6 lane-killer), which no coefficient supplies.
None of these is foreclosed and none is a new framework axiom; this note neither
opens nor consumes any new primitive.

### N7 - Steelman

**Strongest objection.** "The single-complex-pair *class* is the rigorously
corroborated analytic class for `Delta` (off-axis Lee-Yang / Fisher pair, no
real branch point on `[0,6]`); falsifying it at order 8 would contradict the
finite-volume positivity theorem and the literature Fisher-zero evidence —
therefore the order-8 `d_8 > 0` should be re-examined as a candidate computation
error rather than read as falsifying the pair."

**Why it does not break the scoped claim.** The objection conflates two distinct
objects. The corroborated *class* is "the nearest singularity is **a**
complex-conjugate pair off the real axis" — it does **not** assert that the
series is controlled by a **single constant-amplitude dominant** pair, which is
the stronger ansatz the d-log-Pade *route* assumes. A positive `d_8` is fully
compatible with the broader class (multiple pairs, subleading singularities, or
a varying amplitude all keep the nearest singularity an off-axis pair while
breaking the single-dominant-pair sign pattern). And `d_8 > 0` is not a
re-examinable fit residual: it is an exact rational from an independent
octahedral cube-shell computation, cross-validated three ways (the optimized
`Fraction` engine reproduces `d_5, d_6, d_7`; each shape cumulant matches the
closed-form `kappa_5/6^k`; the in-runner second-engine per-link tensor agrees to
zero mismatches at the busiest `(4,1)/(1,4)` link). So the steelman correctly
blocks any over-broad reading ("the off-axis-pair class is wrong") but leaves the
narrow falsifier (the single dominant constant-amplitude pair) intact.

### N8 - Cross-cycle echo

The repo's characteristic negative-claim failure mode is promoting one
representative computation to a whole-lane closure (a single exact coefficient,
or one fit, declared to "close beta=6" or to refute "all continuation"). This
note avoids that echo three ways: (i) the negative claim is restricted to a
single named ansatz (constant-amplitude single dominant complex-conjugate pair)
at a single order (`beta^8`), with the broader off-axis-pair class and all
higher-order routes explicitly left open; (ii) the falsifier's robust content is
isolated to the convention-independent **sign** of `d_8`, with the
convention-dependent magnitudes (`-7.7e-8`, `-3.26e-7`) flagged as non-load-
bearing; (iii) the `[1/1]` self-contradiction is reported as an **activation
that fails**, not as a closure — the Boundary section states explicitly this is
"not a `P(beta=6)` derivation" and that beta=6 still needs a separate dynamical
input for `rho_{p,q}(6)`.

## Key Files

- [`scripts/frontier_beta6_connected_coefficient_2026_05_30.py`](../scripts/frontier_beta6_connected_coefficient_2026_05_30.py) (this note's runner; `maxorder=8` adds V7/V7b/V7c)
- [`BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md)
- [`BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md`](BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md)
- [`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`](BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md)
- `BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md`
- [`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md)
- [`GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md)
- [`BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md)
