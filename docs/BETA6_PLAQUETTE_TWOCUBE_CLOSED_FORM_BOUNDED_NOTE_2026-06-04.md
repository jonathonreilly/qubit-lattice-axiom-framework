# Beta=6 SU(3) Plaquette Weight-10 Two-Cube Sector Closed Form

**Date:** 2026-06-04
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. The independent audit lane sets audit and
effective status.
**Primary runner:** [`frontier_beta6_twocube_closedform_2026_06_04.py`](../scripts/frontier_beta6_twocube_closedform_2026_06_04.py)

## Scope

This note supplies a **zero-parameter closed form** for the LEADING NON-CUBE
class of the SU(3) Wilson single-plaquette connected strong-coupling series
`Delta(beta) = P_full(beta) - P_1plaq(beta) = sum_{n>=5} d_n beta^n`, building on
the cube-sector closed form
([`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`](BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md))
and the first non-cube coefficient
([`BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md)).

The cube sector resums to the exact closed form

```text
Delta_cube(beta) = 72 * K''(beta) * (K'(beta))^5 ,   K = log J,
```

with `J(beta)` the SU(3) single-link generating integral from the in-file
dominant-weight recurrence (`a_0=1, a_1=0, a_2=1/36`;
`6(N+1)(N+4)(N+5) a_{N+1} = N(N+1) a_N + 2(2N+3) a_{N-1} + a_{N-2}`,
[`GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md)).
Read structurally, that closed form is

```text
Delta_cube = (#cubes through p0) * 18 * K'' (K')^(F-1),   F = 6 faces,
```

with `#cubes through p0 = 4`, `F = 6` and `18 = 1/<X_p0^2>` the universal
marked-face weight (each non-marked face contributes a magnetization leg `K'`; the
marked observable face contributes `K''`). This note proves the SAME RULE governs
the leading non-cube class.

## Result

The leading non-cube class is the **weight-10 two-cube 2-cycles through p0**: two
elementary 3-cubes sharing exactly one face, combined in GF(3) with coefficients
`(1,2)` so the shared face CANCELS (`6+6-2 = 10`), leaving `F = 10` distinct
faces (the marked `p0` + 9 action faces). There are exactly `60` such
configurations through `p0`; they are ONE lattice-symmetry orbit (the d_9
new-support class). Its all-order resummation is

```text
Delta_2cube^(w10)(beta) = 1080 * K''(beta) * (K'(beta))^9
                        = (60 configs) * 18 * K'' (K')^(F-1) ,   F = 10.
```

The prefactor `1080 = 60 * 18` is **forced**, not fitted: `60` is the
independently-counted number of weight-10 two-cube configurations through `p0`,
and `18` is the SAME universal marked-face weight `1/<X_p0^2>` that appears in the
cube case (`72 = 4 * 18`). The exponents `K'' (K')^(F-1)` follow the cube rule
(marked face -> `K''`, each other face -> `K'`).

### Zero-parameter, out-of-sample validation (theorem-grade)

A single overall constant is fixed by the LEADING (order-9) coefficient. Orders 10
and 11 are then **out-of-sample predictions** -- neither is used to fix the
constant -- and both match the exact directly-computed weight-10 class value:

```text
order   exact weight-10 class      1080 K''(K')^9 [b^n]       match
  9     5/16529940864              5/16529940864 (DERIVED)    yes
  10    55/198359290368            55/198359290368            yes (out-of-sample)
  11    5/44079842304              5/44079842304              yes (out-of-sample)
```

A constant forced by the geometry (`60 * 18`) PLUS two held-out coefficients
reproduced = theorem-grade. The exact weight-10 class values at orders 9, 10, 11
are computed DIRECTLY (Section "How the runner computes it"), independently of any
ansatz.

### Uniqueness / discrimination control

`1080 K''(K')^9` is the UNIQUE single K-monomial (leading `b^9`) that reproduces
all THREE orders. The runner enumerates every monomial
`(K')^a (K'')^b (K''')^c (K'''')^d` with leading `b^9`: six of them match orders 9
and 10 (with their constant fixed by order 9), but only `(K')^9 (K'')^1` (A=1080)
ALSO matches order 11; the others (`-2592 (K'''')(K')^8`,
`116640 K'' K''' (K')^9`, ...) MISS order 11. The naive `19440 (K'')^2 (K')^9`
(wrong exponent: a spurious extra `K''` "gluing" leg) matches order 9 by
construction but MISSES order 10 (it over-predicts; exact/predicted = `11/13`), and
a free two-term fit
`A (K'')^2(K')^9 + B (K''')(K')^10` tuned to orders 9, 10 misses order 11. So the
validated form is discriminated by the data, not over-fit.

## How The Runner Computes It

### Exact weight-10 class values -- orbit collapse

The 60 weight-10 supports are ONE lattice-symmetry orbit: at every order they
contribute the IDENTICAL per-support connected free-Haar cumulant (the two-cube
analog of the cube's octahedral shape collapse). The runner VERIFIES this at each
order on multiple geometrically-distinct representatives (it does not assume it),
then forms the class value as `60 * support_contrib(rep, n)`. This cuts the work
60x and is what makes orders 10 and 11 reachable. The per-support contribution at
order `n` is the exact `Fraction` connected-cumulant sum over multiplicity vectors
`(m_p0, {m_s})` with `m_p0 + sum m_s = n`, each cumulant the exact set-partition
(Moebius) sum of free-Haar moments, each moment an EXACT SU(3) single-link Haar
integral built as the invariant-tensor projector (delta-caps + epsilon/det sector),
reduced to a linearly-independent invariant basis. The engine is the validated
`frontier_beta6_d9_coefficient_2026_06_04.py` cumulant/projector machinery, imported
unchanged.

```text
weight-10 class:  order 9  = 5/16529940864      (= 60 * 1/198359290368)
                  order 10 = 55/198359290368    (= 60 * 11/2380311484416)
                  order 11 = 5/44079842304       (= 60 * 1/528958107648)
```

The order-9 value reproduces the d_9 note's new-support part exactly (regression).
A two-engine cross-check (sympy `joint_cumulant` == optimized `Fraction`
`joint_cumulant_frac` = `1/198359290368`) confirms the order-9 per-support cumulant.

### The closed form -- reproven, not asserted

The runner reproves the cube closed form `72 K''(K')^5` from the SAME exact `J`
recurrence (a Haar primitive) and verifies it reproduces the direct-engine
`d_5..d_8` exactly before reading off the structural rule. It then builds
`1080 K''(K')^9` from the identical `K = log J`, fixes the constant on order 9, and
checks orders 10, 11 against the directly-computed class values.

### Per-link-degree wall (the scope limit)

These supports reach per-link incidence 2 at order 9, 3 at order 10 and 4 at order
11. The order-11 contribution includes one multiplicity vector (`m_p0 = 2`, the
marked plaquette tripled) that drives a single link to a `(4,4)` invariant-projector
integral (`~10^6`-nonzero tensor); this is feasible but momentarily peaks several GB
(observed ~4 GB) -- the documented per-link-degree cost. Order 12 for these supports
drives incidence 5, i.e. a `(5,5)` integral (`~10^7`-`10^8` nonzeros) that exceeds a
practical memory budget -- the documented `scope_limit`; the runner GATES it and does
NOT force it. The cube part at all orders is supplied by the cube closed form, which
defeats the same wall on the cube side.

### Completeness of the 60 supports

The weight-10 support set STABILIZES between patch radius 2 and radius 3 (identical
60-support set), and the geometric count of weight-10 two-cube configurations through
`p0` is independently `60`, matching the streamed-enumeration count. (Radius-1 LOCAL
is insufficient -- 12 of the 60 reach coordinate-extent 2.)

## Beta=6 evaluation (NOT a closure)

`K'` and `K''` are rational in `J` and its derivatives, with poles only at the `J`
zero `|beta| = 8.2052` (a complex-conjugate pair) -- the SAME branch point as the
cube sector, and `> 6`. So `1080 K''(K')^9` CONVERGES at `beta = 6` (the runner
confirms stability across `J` truncations `N = 50, 75, 100`):

```text
Delta_2cube^(w10)(6) = 0.0300796 .
```

Dropped into the backbone (all recomputed from the SAME `J` recurrence, nothing
imported):

```text
P_1plaq(6)            = K'(6)            = 0.422532    (cited backbone)
Delta_cube(6)         = 72 K''(K')^5      = 0.062913    (cited backbone)
weight-10 two-cube    = 1080 K''(K')^9    = 0.030080    (THIS note)
```

The weight-10 closed form shrinks the non-cube remainder and the truncated model:

```text
non-cube remainder:   0.10796 -> 0.07788
<P>-model(6):         0.485445 -> 0.515525
gap to 0.594 comparator: 0.10796 -> 0.07788  (shrunk ~28%).
```

This is **not** a `P(beta=6)` derivation. The weight-11 two-cube class (66
supports, two cubes sharing one face UNcancelled, leading order 10), the weight-12
class (disjoint cube pairs through `p0`, leading order 11) and all higher clusters
remain, and the retained infinite-hierarchy obstruction
([`GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md))
stands: no finite truncation closes the thermodynamic `<P>(6)`, which still needs a
separate dynamical input for the boundary character measure `rho_{p,q}(6)`. `0.594`
is a Monte-Carlo comparator
([`PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md`](PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md)),
never a derivation input.

## Boundary

This note proves ONE exact closed form: the weight-10 two-cube class resums to
`1080 K''(K')^9 = (60 configs) * 18 * K''(K')^(F-1)`, the exact structural analog of
the cube `72 K''(K')^5 = (4 cubes) * 18 * K''(K')^(F-1)`. It establishes that the
LEADING non-cube cluster obeys the SAME "marked-face `K''`, each other face `K'`,
prefactor `(#configs) * 18`" rule as the cube. It does NOT (i) supply the
weight-11/12 or higher-cluster closed forms (the prefactor-rule extension is an open
follow-on, not proven here); (ii) close `beta = 6`; (iii) repin any canonical
plaquette value, `u_0`, or `alpha_s`.

## Literature comparator (not a derivation input)

The SU(3) Wilson plaquette strong-coupling character expansion is a classical object
(Munster, *Nucl. Phys. B* **190** (1981) 439; Drouffe-Zuber, *Phys. Rept.* **102**
(1983) 1). Those series are quoted ONLY as an after-the-fact comparator; every
coefficient here is reproven from the SU(3) Haar single-link integral and the `J`
recurrence (a Haar primitive), never imported. No Monte-Carlo or PDG value enters the
derivation path.

## Key Files

- [`scripts/frontier_beta6_twocube_closedform_2026_06_04.py`](../scripts/frontier_beta6_twocube_closedform_2026_06_04.py) (this note's runner)
- [`scripts/frontier_beta6_d9_coefficient_2026_06_04.py`](../scripts/frontier_beta6_d9_coefficient_2026_06_04.py) (the imported cumulant/projector engine)
- [`BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md)
- [`BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md`](BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md)
- [`GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md)
- [`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md)
