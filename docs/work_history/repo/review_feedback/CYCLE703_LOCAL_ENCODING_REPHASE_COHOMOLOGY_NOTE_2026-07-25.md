# Cycle 703 local encoding-rephase cohomology — 2026-07-25

Authority: none

Audit: unset

## Result and claim ceiling

This checkpoint tests a genuinely different route from the target-derived
H/K/P correction hierarchy.  It asks whether one static diagonal rephase of
the same occupation register can conjugate away the fixed-register local-owner
residual:

```text
r(n) = delta_S f(n) = f(n) xor f(S n),
```

where `S` is the declared coarse seam-stream permutation.  The first attempt
uses target-independent, coframe-transported onsite/edge/plaquette/cube
quadratic bases for `f`.  The second removes locality and translation
constraints entirely, giving an independent quadratic coefficient to every
mode-address pair on each fixture.

The route is obstructed before a coefficient vector can be frozen:

- all four geometric training systems have augmented rank one above
  coefficient rank;
- even the unrestricted per-patch quadratic system is inconsistent on the
  adjacent, L, and square fixtures;
- the reason is exact: `S` is an involution, so every same-register diagonal
  coboundary is `S`-invariant and zero on `S`-fixed configurations;
- the residual violates that necessary condition on 4 adjacent, 22 L, and 34
  square two-particle pair orbits;
- held `3x3` and cube diagnostics have 100 and 156 such orbits.

The conclusion is strictly limited to a static diagonal rephase on the same
occupation register satisfying the displayed conjugation equation.  It also
covers nonlocal and nonquadratic diagonal `f` on the tested `n<=2` sector,
because the involution identity does not use locality or polynomial degree.
Auxiliary-updated, time-dependent/two-frame, and non-diagonal encodings remain
live.  This is not a shared substrate obstruction and creates no axiom
pressure.

## Necessary orbit condition

For any Boolean phase function `f` and `S^2 = I`,

```text
delta_S f(S n)
  = f(S n) xor f(S^2 n)
  = f(S n) xor f(n)
  = delta_S f(n).
```

Thus `r(n)` must be constant on every two-cycle of `S`.  If `S n = n`, then
`delta_S f(n)=0`.  This is a necessary condition for any static diagonal
same-register rephase, without assuming that `f` is quadratic, local, or
translation invariant.

On quadratic pair coefficients, `delta_S = I + S^(2)`.  Every two-element
pair orbit contributes one image vector with equal bits on its two members;
every fixed pair contributes zero.  Consequently the image rank is exactly
the number of two-element pair orbits.  A residual pair orbit with odd XOR is
outside that image, and one mismatch per such orbit is the exact closest
distance in the unrestricted quadratic image.

The exact rows are:

| Fixture | Modes / pair dimension | Fixed / two-cycle pair orbits | `rank(delta)` / augmented | Odd residual orbits | Closest unrestricted quadratic miss |
|---|---:|---:|---:|---:|---:|
| adjacent centers | `72 / 2,556` | `1,236 / 660` | `660 / 661` | 4 | 4 |
| three-center L | `96 / 4,560` | `2,032 / 1,264` | `1,264 / 1,265` | 22 | 22 |
| `2x2` centers | `120 / 7,140` | `3,180 / 1,980` | `1,980 / 1,981` | 34 | 34 |
| `3x3` centers | `234 / 27,261` | `11,217 / 8,022` | `8,022 / 8,023` | 100 | 100 |
| `2x2x2` cube | `192 / 18,336` | `7,176 / 5,580` | `5,580 / 5,581` | 156 | 156 |

The corresponding counts of two-particle configurations on which
`r(n) != r(Sn)` are `8,44,68` for training and `200,312` for held.  Every one
of the six L owner orders retains 178 residual pairs and exactly 22 odd
orbits.  Owner-order choice therefore does not rescue this equation.

No training solution exists, so there is no coefficient vector to freeze.
The `3x3` and cube rows are held orbit diagnostics, not claimed predictions
from a fitted rephase.

## Independent Cycle-330 witness

The runner independently reconstructs the adjacent fixture without calling
the predecessor's `owner_residual` helper.  It starts from the six direction
modes of
`physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18`, enumerates
the two center stars and first-owner edges, constructs the local seam words
from the declared intermediate-interval grammar, constructs the global
exterior target from the actual permutation inversion pairs, pulls the local
words back through prior swaps, and obtains the same 12 cells, 11 edges, and
24 residual pairs.

One explicit two-particle orbit is:

```text
a = {
  address 18: cell (0,0,0), mode 0 / direction +x,
  address 38: cell (1,-1,0), mode 2 / direction +y
}

S a = {
  address 49: cell (1,0,0), mode 1 / direction -x,
  address 51: cell (1,0,0), mode 3 / direction -y
}.
```

The independently reconstructed residual bits are `r(a)=1` and `r(Sa)=0`,
while applying the stream twice returns `a`.  But every candidate rephase has

```text
delta_S f(a) = f(a) xor f(Sa) = delta_S f(Sa).
```

This one concrete grammar-level orbit already contradicts the necessary
condition.  The complete orbit census supplies the stronger counts above.

## Target-independent local bases

The local phase basis is defined geometrically before reading the residual.
For an unordered pair of mode sites, translate the first cell to the origin,
express the displacement and both direction modes in the local coframe, and
identify the reversed representation.  Four nested bases are tested:

1. onsite plus nearest-neighbor edge pairs;
2. onsite, edge, and elementary face-diagonal pairs;
3. all onsite and taxi-distance-at-most-two pairs, including collinear
   two-step pairs;
4. every pair in one elementary `3x3x3` cell neighborhood, including body
   diagonals of a unit cube.

The adjacent, L, and square systems contribute 14,256 pair equations with 452
nonzero target bits.  Exact elimination gives:

| Basis | Geometric coefficients | Coefficient rank | Augmented rank | Maximum taxi support |
|---|---:|---:|---:|---:|
| onsite-edge | 123 | 120 | 121 | 1 |
| onsite-edge-face | 339 | 318 | 319 | 2 |
| onsite-edge-two-step | 447 | 397 | 398 | 2 |
| elementary-cube | 483 | 432 | 433 | 3 |

All four are inconsistent.  These are target-independent basis definitions;
the residual is used only as the equation right-hand side.  The unrestricted
orbit calculation proves that expanding the static same-register diagonal
basis beyond these neighborhoods cannot cure the displayed residual.

## Covariance, bounded CZ routing, mass, and domain

The largest 483-key basis is transported with the proper-cubic coframe.  Local
feature keys have zero failures in 11,592 key/frame cases and zero composition
failures in 278,208 key/ordered-frame-product cases.  This tests all 24 frames
and all 576 products without rebuilding ambient common-`E` matrices.

Every individual basis monomial has a bounded realization.  Onsite terms use
an intra-cell CZ.  For offsite terms, a fixed coframe-axis path swaps one mode
to adjacency, applies CZ, and reverses the path.  All 13 non-onsite cube
displacement programs reach adjacency and return routing exactly.  Maximum
taxi length is 3 and maximum out-and-back cost is four SWAPs.  This proves the
basis gates themselves are bounded and returned; it does not produce a
compiler because no coefficient vector satisfies the training equations.

The residual is zero on vacuum and one-particle inputs, so the rephase question
preserves the one-particle mass fixture at the tested level.  No physical
common-`E` map is constructed and physical code-space leakage remains
undefined.  The lawful scope is the declared vacuum/one-/two-particle sector.

## Supplied structure and dependency effect

The fixed-register residuals are supplied as equation right-hand sides; `S`
comes from the declared seam swaps; the homogeneous coframe and six direction
labels are supplied; and the geometric neighborhood class for `f` is chosen.
No target-derived H/K/P masks enter this route.

| Wall | Effect |
|---|---|
| `C_ref` | unchanged: the local basis is covariant under a supplied coframe, but no rephase solution or coframe genesis is produced |
| `C_num` | unchanged: the exact obstruction is established only through the declared `n<=2` sector, although it permits arbitrary diagonal `f` there |
| `C_wrap` | unchanged: no causal time or realized-history mechanism is constructed |
| `C_int` | unchanged: the tested object is the stream-sign residual |
| `C_local` | sharpened: the same-register static diagonal rephase route is exactly closed by an orbit condition, while auxiliary/two-frame/non-diagonal routes remain live |
| `C_source` | unchanged |

No TOE maturity score changes.  This route-specific closure does not touch
Records, causal time, gravity/source, or Born/probability.

## No-go-discipline N1-N8 gate

The current `origin/main` no-go-discipline instructions were applied before
shipping the negative claim.  The permitted conclusion is the exact
same-register diagonal coboundary obstruction above.  Any claim about all
encodings, minimum physical content, shared substrate obstruction, or axiom
pressure fails the gate.

### N1 — alternative route enumeration

1. **Onsite/edge rephase — ATTEMPTED.** Rank `120/121`; inconsistent.
2. **Face, two-step, and full elementary-cube diagonal bases — ATTEMPTED.**
   Ranks `318/319`, `397/398`, and `432/433`; inconsistent.
3. **Unrestricted nonlocal quadratic f per fixture — ATTEMPTED.** Exact pair
   orbit ranks remain augmented by one; the closest misses are 4, 22, and 34
   on training.
4. **Higher-degree or arbitrary diagonal f on the same register — ANALYTICALLY
   TESTED on `n<=2`.** The involution identity is degree independent and the
   concrete residual violates it.
5. **All six L owner schedules — ATTEMPTED.** Each retains 22 odd pair orbits.
6. **Auxiliary-updated rephase — OPEN.** A lifted gauge state can change the
   orbit and terminal equation; it is not the same-register problem.
7. **Time-dependent/two-frame phases `f_in,f_out` — OPEN.** Their equation is
   not `f xor f composed with S` and does not obey this symmetry condition.
8. **Non-diagonal encoding, modified local executor, or even-bond gauge
   algebra — OPEN.** These change the object and escape the theorem.

### N2 — wall independence

`W_rephase-orbit` is the same-register diagonal coboundary obstruction;
`W_common-E` is absence of a physical gauge compiler and leakage bound;
`W_coframe-genesis` is supplied reference structure; and the earlier
`W_periodic-color` concerns scheduling.  They are logically distinct.  The
first does not establish any of the others.

### N3 — hidden-wall scan

The residual RHS, stream permutation, particle sector, static/same-register
assumption, diagonal character, coframe, mode labels, neighborhood choices,
routing realization, covariance scope, and missing common-E/leakage are
explicit.  “Unrestricted” means unrestricted quadratic pair coefficients on
one finite fixture, not unrestricted physical encodings.

### N4 — residual matching

The runner reproduces the predecessor residual counts 24, 178, 250, 942, and
1,136.  The adjacent 24-pair result and one odd orbit are independently rebuilt
from the Cycle-330 direction/seam/inversion grammar.  All six L owner orders
are separately reconstructed.  H/K/P and local-Gauss candidates are different
routes and are neither smuggled into nor ruled out by this residual.

### N5 — resolution audit

Tests cover every pair address on adjacent, L, square, `3x3`, and cube;
unrestricted quadratic pair cochains; the arbitrary-diagonal necessary
condition on all vacuum/one-/two-particle configurations; four local bases; 24
frames; 576 products; and bounded CZ routing.  They do not cover higher-number
residuals, auxiliary registers, two-time encodings, non-diagonal circuits, or
a different local executor.

### N6 — partial-closure paths

The geometric bases and every monomial route covariantly and with returned
work.  The failure is solely that one static diagonal phase cannot reproduce
an orbit-asymmetric RHS.  Adding a locally updated gauge label, using distinct
input/output frame phases, rephasing the local executor as well as the
encoding, or adopting a non-diagonal bond representation all change that RHS
or coboundary operator and remain constructive paths.

### N7 — steelman

A hostile reviewer should lift the equation to a bounded auxiliary chart
whose update remembers which member of the problematic stream orbit is being
crossed, or use a two-frame encoding with separate bounded phases before and
after the stream.  The explicit Cycle-330 witness gives the exact local bit
such a lift must distinguish.  The next terminal test is whether the lifted
state is locally constrained, returned or lawfully advanced, covariant, and
held without exterior-order tables.

### N8 — cross-cycle echo

The earlier direct common-E failure was retired by adding gauge state, and the
H/K square residual was partially retired by a plaquette channel.  Those
results are direct warnings not to promote a same-register cohomology class to
an obstruction for enlarged encodings.  The correct inference is a route
closure and a targeted auxiliary/two-frame retask, not constitutional change.

## Reproduction

With the Cycle 703 predecessor and its dependencies on `PYTHONPATH`, run:

```text
python3 scripts/frontier_cycle703_local_encoding_rephase_cohomology_2026_07_25.py
```

The terminal marker is
`CYCLE703_REPHASE_ODD_ORBITS_4_22_34_HELD_100_156`.
