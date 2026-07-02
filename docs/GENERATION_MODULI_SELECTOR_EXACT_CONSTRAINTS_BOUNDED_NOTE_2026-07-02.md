# Generation-Moduli Selector Exact Constraints

**Date:** 2026-07-02
**Type:** bounded support (exact selector constraints; frontier map)
**Claim type:** bounded_theorem
**Status authority:** branch-local science draft only. The independent audit
lane remains the only authority for audit status; this note sets no audit row,
moves no ledger row, and closes no wall.

## Boundary

This note records exact algebraic constraints on any future
generation-moduli selector. It proposes no selector and derives no selected
modulus. It uses no empirical moduli values, asserts no sector has generic
`r`, adds no axiom or primitive, and does not close any wall. The
generic-`r` statements below are conditional frontier statements only.

Trace: this is frontier/constraint-map work. Consumer: the flavor-moduli
frontier; no existing ledger row is claimed to be moved.

## Load-Bearing Inputs

1. `docs/FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md`.
   Role: finite generation coordinate and carrier-measure boundary. The source
   writes

   ```text
   r = b^2/a^2 = 1/(N-1)
   ```

   under supplied generator-channel Hilbert-Schmidt scoring, and for `N=3`
   writes the generation coordinate

   ```text
   Q = 1/3 + (2/3)r = 2/3.
   ```

   It also states the boundary: Record supplies finite additive readout
   coordinates, while the carrier-measure scoring rule remains unselected.

2. `docs/OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md`.
   Role: quoted dictionary-flow maps. The source gives the two explicit
   dictionaries:

   ```text
   x = 2r: r -> (2r)^2/2 = 2r^2, with finite fixed set {0, 1/2}.
   x = r:  r -> r^2,             with finite fixed set {0, 1}.
   ```

3. `docs/MINIMAL_AXIOMS_2026-06-29.md`.
   Role: axiom surface and open-gate firewall. The source names the four
   primitives as Lattice, Qubit, Admissibility, and Record. It separates the
   spatial carrier from the internal factor: physical sites are points of
   `Z^3`, while the one-site possibility domain has presentation `M_2(C)`.
   Its open gates include, outside the axiom content, readout-context
   selection, measurement basis selection, Born weights, probability rules,
   update laws, occurrence rules, source/action identification, P2/modulus
   content, log-det readout, dynamics, and scale-reference handling.

Throughout, write the finite `C_3` circulant surface as

```text
Y(a,b) = a I + b U + conjugate(b) U^{-1},
```

with `a > 0` in the positive scale gauge and `b in C`. The ratio coordinate is

```text
r(Y) = |b|^2/a^2.
```

Equivalently, before fixing the positive `a` gauge one may write the same
projective ratio as `|b|^2/|a|^2`; the positive gauge reduces it to the
source coordinate above.

## T1. Ratio-Directness

Let `lambda in R^x` be a common dimensionful rescaling. Then

```text
r(lambda a, lambda b)
  = |lambda b|^2/(lambda a)^2
  = lambda^2 |b|^2/(lambda^2 a^2)
  = r(a,b).
```

Let `mu in C` with `|mu| = 1` be a global phase dressing of `b`. Then

```text
r(a, mu b) = |mu b|^2/a^2 = |mu|^2 |b|^2/a^2 = r(a,b).
```

If the common phase acts on both entries before the positive gauge is chosen,
the invariant statement is

```text
|mu b|^2/|mu a|^2 = |b|^2/|a|^2.
```

Thus any joint rescaling of `(a,b)` by a common nonzero real dimensionful
factor, any common complex projective phase before gauge fixing, and any
global phase on `b` leave the ratio coordinate fixed exactly.

Consequently, a selector functional intended to fix `r` cannot act through a
common multiplicative dressing or a dimensionful scale alone. Formalize the
scale projection by

```text
Pi_scale(Y(a,b)) = a
```

in positive gauge. If a selector factors as

```text
S(Y) = F(Pi_scale(Y)),
```

then for every fixed scale `sigma > 0`, `S` is constant on the whole scale
fiber

```text
Pi_scale^{-1}(sigma)
  = {Y(sigma,b): b in C}.
```

That fiber contains all ratio values `r = |b|^2/sigma^2` allowed by the
chosen domain. The exact witness at scale `sigma = 1` is

```text
Y_0 = Y(1,0),       r(Y_0) = 0,
Y_1 = Y(1,1),       r(Y_1) = 1.
```

They have identical scale data but different ratio data. Therefore any
scale-only factorization gives `S(Y_0) = F(1) = S(Y_1)` and cannot select
between their `r` values. A selector that fixes `r` must act on the ratio
coordinate, or on data that distinguishes that coordinate, directly.

## T2. Dial-Point Structure Of Fixed-Point Selection

Let

```text
f(r) = 2r^2,
g(r) = r^2,
```

on `[0, infinity)`.

The single-step fixed sets are exact:

```text
f(r) = r  <=>  2r^2 - r = r(2r - 1) = 0,
Fix(f) = {0, 1/2}.

g(r) = r  <=>  r^2 - r = r(r - 1) = 0,
Fix(g) = {0, 1}.
```

The pure same-family iterates add no new positive fixed point. For `n >= 1`,

```text
g^n(r) = r^(2^n),
```

so `g^n(r) = r` has nonnegative fixed set `{0,1}`. Also

```text
f^n(r) = 2^(2^n - 1) r^(2^n),
```

so `f^n(r) = r` has nonnegative fixed set `{0,1/2}`.

The four pairwise compositions are:

| map | formula | nonnegative fixed set |
|---|---:|---|
| `f after f` | `8r^4` | `{0, 1/2}` |
| `f after g` | `2r^4` | `{0, 2^(-1/3)}` |
| `g after f` | `4r^4` | `{0, 2^(-2/3)}` |
| `g after g` | `r^4` | `{0, 1}` |

Thus the two quoted single-step dictionary maps have exactly the advertised
fixed sets, and their pure iterates add no new fixed points. However, the
mixed pairwise compositions do add exact fixed points. Therefore this note
does not claim the stronger statement that arbitrary finite mixed
compositions add no new points in `[0, infinity)`. The exact finite check
instead marks that stronger statement as outside the retained content of this
bounded draft.

Conditional consequence. For a sector whose realized modulus `r_sector` is
not in `{0, 1/2, 1}`, no fixed point of the two quoted single-step maps, nor
of their pure same-family iterates, selects it. A selector for such a sector
must be non-fixed-point relative to that quoted dictionary-flow family. If
mixed finite compositions are admitted as candidate selector flows, the
admissible dial-point set must be recomputed for the admitted composition
class; it is not exhausted by `{0, 1/2, 1}`.

This is a hypothetical-conditional statement. It does not assert that any
sector actually has generic `r`.

## T3. Sector-Structure / Non-Color Label

Let `Sigma` be a finite sector index set. Model each sector as an independent
circulant surface

```text
Y_s = Y(a_s,b_s),       s in Sigma,
r_s = |b_s|^2/a_s^2.
```

Let `C` be an abstract color-label set and let

```text
c: Sigma -> C
```

be the supplied color data. Suppose a selector assigns selected moduli through
color data only:

```text
r*_s = G(c_s)
```

for some function `G: C -> [0, infinity)`. If two sectors have equal color
data, `c_s1 = c_s2`, then exact function factoring gives

```text
r*_{s1} = G(c_s1) = G(c_s2) = r*_{s2}.
```

Contrapositive: distinct selected moduli across equal-color sectors require
the selector domain to include some non-color sector label, or other data that
distinguishes the two sectors.

Exact witness. Let

```text
Sigma = {s1, s2},
c_s1 = c_s2 = c0,
r*_{s1} = 1/2,
r*_{s2} = 1.
```

No function `G` on color data alone can satisfy both assignments, because it
would require `G(c0) = 1/2` and `G(c0) = 1`. The contradiction is purely
function-theoretic. It imports no Standard Model content and treats color as
an abstract supplied label.

## T4. Constraint Map Summary

Any generation-moduli selector in this frontier lane must satisfy these exact
constraints:

1. Ratio-directness: it must act on the ratio coordinate, or on data that
   distinguishes the ratio coordinate, because common scale and phase
   dressings leave `r = |b|^2/a^2` invariant exactly.
2. Dictionary-flow boundary: if it is to select a hypothetical generic
   modulus not in `{0, 1/2, 1}`, it must be non-fixed-point relative to the
   two quoted single-step dictionary maps and their pure same-family iterates.
   Mixed finite compositions are a separate admitted-flow question and have
   their own exact dial points.
3. Sector-label requirement: if it is to select distinct moduli across
   equal-color sectors, its domain must include a non-color sector label or
   other non-color distinguishing data.

These constraints delimit the selector search space. No selector is proposed.
No selector is excluded unconditionally beyond the factoring and fixed-point
statements proved here.

## Does NOT Claim

- Does not propose, derive, or fit a generation-moduli selector.
- Does not use or imply empirical moduli values.
- Does not assert any sector has generic `r`.
- Does not introduce a new axiom, primitive, readout context, or occurrence
  rule.
- Does not close a wall or move an audit ledger row.
- Does not claim arbitrary mixed finite compositions of `f` and `g` add no
  new fixed points.
- T2's consequence is hypothetical-conditional and applies only to the
  explicitly stated flow class.
