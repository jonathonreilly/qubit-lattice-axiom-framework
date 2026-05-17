# Gauge-Vacuum Plaquette U(1) Density and Sign-Alternation Sharpening Note (Narrow)

**Date:** 2026-05-17
**Claim type:** positive_theorem (narrow)
**Status authority:** source-note proposal only; the audit lane sets
effective status.
**Primary runner:** [`scripts/frontier_gauge_vacuum_plaquette_u1_density_sign_alternation_narrow.py`](../scripts/frontier_gauge_vacuum_plaquette_u1_density_sign_alternation_narrow.py)
**Parent obstruction (already retained):**
[`GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_INFINITE_HIERARCHY_OBSTRUCTION_NOTE.md)

## Claim

For the abelian U(1) one-plaquette diagonal generator

```text
K_1 ( t )  :=  log Z_1 ( t )  -  log Z_1 ( 0 ),
Z_1 ( t )  :=  ∫_0^{2π} exp ( t · cos θ ) dθ / ( 2π )  =  I_0 ( t ),
```

the Taylor expansion `K_1 ( t ) = Σ_{n ≥ 0} c_n t^n` at `t = 0`
satisfies, for every integer `k ≥ 1`,

```text
(D1)   c_{2k - 1}      =  0,                                              (parity)
(D2)   c_{2k}          ≠  0,                                              (density on even orders)
(D3)   sign ( c_{2k} ) =  ( - 1 )^( k + 1 ).                              (sign alternation)
```

Concretely the first few coefficients are

```text
c_2  =  1 / 4,
c_4  =  - 1 / 64,
c_6  =  1 / 576,
c_8  =  - 11 / 49152,
c_10 =  19 / 614400,
c_12 =  - 473 / 106168320,
...
```

The proof is by an explicit two-term recurrence on the coefficients
`a_n` of `r ( t ) := K_1' ( t ) = I_1 ( t ) / I_0 ( t )`, combined with
an elementary induction on `n`.

## Why this sharpens the parent no-go (and does not duplicate it)

The parent retained no-go theorem says: `K_1 ( t )` is not a polynomial
of any finite degree.  The companion lemma note
`GAUGE_VACUUM_PLAQUETTE_HIERARCHY_OBSTRUCTION_LEMMAS_BOUNDED_NOTE_2026-05-10.md`
supplies the four BA-1 — BA-4 endpoint, analyticity, and polynomial-
growth premises that the parent uses.

Neither parent nor companion rules out the structural escape

> "perhaps `K_1` is non-polynomial only because of a sparse infinite
> subsequence of nonzero coefficients, and a sparse / gap-pattern
> truncation could still close the hierarchy"

The present note rules out that escape on U(1) by proving:

- (D2) every even-order Taylor coefficient is strictly nonzero (no gaps
  at any order, no sparse truncation),
- (D3) the signs alternate strictly with `k`, so adjacent even-order
  contributions to `K_1` always cancel in opposite directions (no
  "monotone tail truncation" approximation can match the exact `K_1` to
  arbitrary order with only finitely many positive-sign terms either).

This is strictly stronger than "non-polynomial".

## Setup

The U(1) Bessel function `I_0` satisfies the modified Bessel ODE

```text
I_0''  +  I_0' / t  -  I_0   =   0,         I_0 ( 0 )  =  1.             (BesselODE)
```

Together with the standard derivative identities

```text
I_0' ( t )   =   I_1 ( t ),
I_1' ( t )   =   I_0 ( t )  -  I_1 ( t ) / t,                            (Bessel')
```

set `r ( t ) := I_1 ( t ) / I_0 ( t ) = K_1' ( t )`.  Then

```text
r' ( t )   =   ( I_1 ' I_0  -  I_1 I_0' ) / I_0 ^ 2
           =   ( ( I_0 - I_1 / t ) · I_0  -  I_1 · I_1 ) / I_0 ^ 2
           =   1   -   r ( t ) / t   -   r ( t ) ^ 2.
```

Multiplying by `t` and rearranging gives the **Riccati equation**

```text
t · r' ( t )   +   r ( t )   +   t · r ( t ) ^ 2   =   t,                (Riccati)
r ( 0 )        =   0,        r' ( 0 )   =   1 / 2.
```

The initial conditions follow from `I_1 ( t ) = t / 2 + O ( t ^ 3 )` and
`I_0 ( t ) = 1 + t ^ 2 / 4 + O ( t ^ 4 )`.

Since `I_1` is odd and `I_0` is even (immediate from the cosine
representation `I_0 ( t ) = ∫ exp ( t cos θ ) dθ / ( 2π )` and the
substitution `θ → π - θ` ⇒ `cos θ → - cos θ`), the ratio `r = I_1 / I_0`
is **odd**.  Write the Taylor expansion at `t = 0`,

```text
r ( t )   =   Σ_{n ≥ 0} a_n t ^ ( 2 n + 1 )                              (rTaylor)
```

with `a_0 = 1 / 2` and `a_n ∈ R` to be determined.

## The explicit recurrence

Substitute (rTaylor) into (Riccati).  Each term contributes the
following coefficient of `t ^ ( 2 n + 1 )`:

```text
t r' ( t )                    →   a_n · ( 2 n + 1 ),
r ( t )                       →   a_n,
t r ( t ) ^ 2                 →   Σ_{j + k = n - 1, j, k ≥ 0} a_j a_k,
t                             →   δ_{ n, 0 }.
```

Matching coefficients gives, for every integer `n ≥ 0`,

```text
a_n · ( 2 n + 2 )   +   Σ_{j + k = n - 1, j, k ≥ 0} a_j a_k   =   δ_{ n, 0 }.    (rec)
```

The `n = 0` instance gives `2 a_0 = 1`, i.e. `a_0 = 1 / 2`, matching the
initial condition.  For `n ≥ 1` the Kronecker delta vanishes and (rec)
reduces to the explicit two-term recurrence

```text
a_n   =   -   ( 1 / ( 2 ( n + 1 ) ) )   ·   Σ_{j + k = n - 1, j, k ≥ 0} a_j a_k.    (rec*)
```

The first few terms are `a_1 = - 1 / 16`, `a_2 = 1 / 96`,
`a_3 = - 11 / 6144`, `a_4 = 19 / 61440`, in exact rational arithmetic.

## Proof of (D1) - (D3)

**(D1) Parity.**  Since `I_0` is even and `K_1 ( t ) = log I_0 ( t )` is
the composition of an even function with `log` (real-analytic on a
neighborhood of `1`), `K_1` is itself even.  Hence every odd-order
Taylor coefficient `c_{ 2 k - 1 } = 0`.  ∎

**(D2) and (D3) jointly: every `a_n` is nonzero with sign `( - 1 ) ^ n`.**

By strong induction on `n ≥ 0`.

*Base case (`n = 0`)*: `a_0 = 1 / 2 > 0` and `( - 1 ) ^ 0 = + 1`.  ✓

*Inductive step.*  Fix `n ≥ 1`.  Assume `a_m ≠ 0` and
`sign ( a_m ) = ( - 1 ) ^ m` for every `0 ≤ m ≤ n - 1`.

For any `( j, k )` with `j + k = n - 1` and `j, k ≥ 0`, both `j` and
`k` lie in `[ 0, n - 1 ]`, so the inductive hypothesis applies and

```text
sign ( a_j a_k )   =   ( - 1 ) ^ j  ·  ( - 1 ) ^ k   =   ( - 1 ) ^ ( j + k )
                   =   ( - 1 ) ^ ( n - 1 )
                   =   -  ( - 1 ) ^ n.
```

Each summand `a_j a_k` is strictly nonzero (product of two nonzero
factors) and all `n` summands share the same sign `- ( - 1 ) ^ n`.
Therefore the sum is strictly nonzero with that common sign:

```text
sign  ( Σ_{j + k = n - 1} a_j a_k )   =   -  ( - 1 ) ^ n,
Σ_{j + k = n - 1} a_j a_k             ≠   0.
```

Apply (rec*):

```text
a_n   =   -  ( 1 / ( 2 ( n + 1 ) ) )   ·   Σ_{j + k = n - 1} a_j a_k.
```

The prefactor `- 1 / ( 2 ( n + 1 ) )` is negative.  The sum has sign
`- ( - 1 ) ^ n`.  The product of a negative and `- ( - 1 ) ^ n` is
`( - 1 ) · ( - ( - 1 ) ^ n )  =  ( - 1 ) ^ n`.  Hence
`sign ( a_n ) = ( - 1 ) ^ n` and `a_n ≠ 0`.  ✓

This completes the induction.  Therefore for every `n ≥ 0`,

```text
a_n   ≠   0,        sign ( a_n )   =   ( - 1 ) ^ n.                       (a-sign)
```

**Translate (a-sign) to (D2) and (D3).**  From (rTaylor),
`K_1 ' ( t ) = r ( t ) = Σ a_n t ^ ( 2 n + 1 )`, so integrating
term-by-term,

```text
K_1 ( t )   =   Σ_{n ≥ 0} a_n   ·   t ^ ( 2 n + 2 ) / ( 2 n + 2 )
            =   Σ_{k ≥ 1} ( a_{ k - 1 } / ( 2 k ) )  ·  t ^ ( 2 k ).
```

Therefore `c_{ 2 k } = a_{ k - 1 } / ( 2 k )` for every `k ≥ 1`.

Combining with (a-sign):

```text
c_{ 2 k }            =   a_{ k - 1 } / ( 2 k )                   ≠   0,           (D2)
sign ( c_{ 2 k } )   =   sign ( a_{ k - 1 } )   =   ( - 1 ) ^ ( k - 1 )
                     =   ( - 1 ) ^ ( k + 1 ).                                       (D3)
```

This establishes (D2) and (D3).  Combined with (D1), the full claim
follows.  ∎

## Admitted inputs (A_min-compatible)

The proof uses only the following inputs, already admitted by the
parent obstruction note's BA-1—BA-4:

- (B1) Haar normalization on U(1) and the integral
  `Z_1 ( t ) = ∫ exp ( t cos θ ) dθ / ( 2π ) = I_0 ( t )`
  (parent BA-1 / BA-3).
- (B2) The modified Bessel ODE `I_0 '' + I_0 ' / t - I_0 = 0` and the
  derivative identities `I_0 ' = I_1`, `I_1 ' = I_0 - I_1 / t`.
  These are textbook special-function calculus.  No additional
  framework primitive is invoked.
- (B3) `I_0` is even and `I_1` is odd in `t`.  Either read off the
  power-series definitions or use the cosine representation under
  `θ → π - θ`.

No new framework primitives are introduced.  All inputs are
A_min-compatible (A1 = Cl(3) local algebra, A2 = `Z^3` substrate),
with the U(1) plaquette being the abelian one-plaquette block already
admitted in the parent.

## What this closes and does not close

**Closes (within stated scope):**

- (D1) - (D3) for the U(1) one-plaquette diagonal generator,
- A strictly stronger no-go than "K_1 is non-polynomial": every
  even-order coefficient is strictly nonzero with sign `(- 1) ^ (k + 1)`,
- The structural escape "sparse truncation might still close" on U(1).

**Does not close:**

- Analytic `P ( 6 )` or any `chi_L ( β )` expression,
- An explicit nonpolynomial solution of the connected hierarchy on
  SU(3) (the physical gauge group),
- Sign-alternation / density for SU(2) or SU(3) generators (separate
  theorem, requires different recurrence machinery; out of scope
  here),
- The parent obstruction theorem's `retained_no_go` status remains as
  set by the audit lane.

## Audit-row authority

This note is a **source-note proposal**.  Its `effective_status` is
set by the independent audit lane, not by this note.  The parent
obstruction note `gauge_vacuum_plaquette_infinite_hierarchy_obstruction_note`
is `audited_clean` / `retained_no_go` per the 2026-05-12 judicial third-
pass audit and this note does not modify that row.

## Runner verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_gauge_vacuum_plaquette_u1_density_sign_alternation_narrow.py
```

Expected summary line:

```text
SUMMARY: THEOREM PASS=8 SUPPORT=5 FAIL=0
```

The runner verifies (D1) — (D3) at exact rational precision through
order 40 in `t` (i.e., k = 1 .. 20), checks the recurrence (rec*) on
`a_n` matches symbolic Taylor of `I_1 / I_0`, and cross-checks the
sign-alternation persists numerically to order 100.

## Dependencies

- `gauge_vacuum_plaquette_infinite_hierarchy_obstruction_note` (parent
  no-go that this note sharpens; row remains `retained_no_go`),
- `gauge_vacuum_plaquette_hierarchy_obstruction_lemmas_bounded_note_2026-05-10`
  (companion lemma note BA-1 — BA-4 supplies (B1); B2 and B3 are
  textbook Bessel calculus not requiring an additional framework
  admission),
- `MINIMAL_AXIOMS_2026-05-03.md` (A_min baseline A1, A2).

The directional graph is parent obstruction → companion lemmas → this
sharpening note.  This note does not load-bear on any open downstream
gates.
