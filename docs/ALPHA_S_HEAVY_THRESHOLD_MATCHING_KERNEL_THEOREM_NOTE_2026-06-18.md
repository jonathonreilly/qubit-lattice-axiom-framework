# Finite Marked Piecewise-Affine Map Structural Theorem (2026-06-18)

**Type:** exact structural theorem
**Claim type:** positive_theorem
**Status:** proposed_retained
**Dependencies:** none; definitions and exact rational arithmetic only
**Primary runner:** `scripts/frontier_alpha_s_heavy_threshold_matching_kernel_2026_06_18.py`
**Runner summary:** `SUMMARY: PASS=32 FAIL=0`

## 1. Purpose

This note proves the algebra of a finite family of explicitly defined affine
maps.  The data are exact rational coefficients and positive exact rational
interval lengths.  No differential equation, measured quantity, physical
interpretation, or external theorem is an input.

The filename is retained for stable repository identity.  The theorem proved
here is only the formal piecewise-affine statement below.

## 2. Exact domain and definitions

Let `Q` denote the rational numbers.  An admissible index is an integer `n`
such that

```text
n >= 0,                    c(n) := 11 - 2 n / 3 > 0.
```

Thus the admissible indices are exactly `0, 1, ..., 16`.  The expression
`c(n)` is a definition of a rational coefficient sequence; it is not imported
from another result.

For `x in Q`, `c in Q_{>0}`, and `L in Q_{>0}`, define

```text
T_{c,L}(x) := x - c L,
U_{c,L}(x) := x + c L.
```

An admissible segment is a supplied triple `(n, c, L)` for which `n` is an
admissible index, `c = c(n)` exactly, and `L > 0`.  An admissible marked path
is a nonempty ordered finite tuple of admissible segments

```text
P = (s_0, s_1, ..., s_m)
```

whose adjacent indices satisfy `n_{j+1} = n_j - 1`.  A marker is the boundary
between two adjacent segments.  At every marker define the carry map to be

```text
I(x) := x.
```

The identity carry is part of the definition of this formal object.  It is
not inferred from continuity, dynamics, or any other law.  A one-segment path
has an empty marker list and is admissible.

## 3. Exact coefficient identities

For every admissible index for which both sides exist,

```text
c(n - 1) = c(n) + 2/3.
```

In particular,

```text
c(6) = 7,  c(5) = 23/3,  c(4) = 25/3,  c(3) = 9.
```

These are substitutions into the definition of `c`; they carry no additional
interpretation.

## 4. Fixed-coefficient affine identities

For exact admissible inputs,

```text
U_{c,L}(T_{c,L}(x)) = x = T_{c,L}(U_{c,L}(x)),
T_{c,L_2}(T_{c,L_1}(x)) = T_{c,L_1+L_2}(x).
```

More generally, function composition is associative, and for three supplied
segments the two parenthesizations both equal

```text
x - c_1 L_1 - c_2 L_2 - c_3 L_3.
```

The inverse map is stated as `U_{c,L}` so that negative lengths never enter
the admissible segment domain.

## 5. Finite marked-path theorem

Let `P = (s_0, ..., s_m)` be an admissible marked path, where segment `s_j`
has coefficient `c_j` and length `L_j`.  Sequentially applying its segment
maps and the defined identity carry at each marker gives exactly

```text
T_P(x) = x - sum_{j=0}^m c_j L_j.
```

The result covers an empty marker list, one marker, or any finite number of
markers.  It is independent of parenthesization.  Applying the inverse maps
in reverse order returns `x` exactly.

### Proof

For one segment the result is the definition of `T_{c,L}`.  Suppose the
formula holds after segment `j`.  The marker applies `I`, so it changes
nothing.  Applying segment `j+1` subtracts exactly `c_{j+1} L_{j+1}`, which
gives the claimed sum through `j+1`.  Finite induction proves the formula.
The inverse statement follows by adding the same terms in reverse order.
Every equality is in `Q`; no approximation or tolerance is used.

## 6. Marker-jump counterexample

Replace a defined identity carry at marker `r` by

```text
J_r(x) := x + j_r
```

for a supplied rational `j_r`.  The final value becomes

```text
T_{P,J}(x) = x - sum_{j=0}^m c_j L_j + sum_{r=0}^{m-1} j_r.
```

Consequently a single nonzero jump changes the output exactly by that jump.
More generally the original closed form survives precisely when the supplied
jumps sum to zero.  This is a counterexample to silently replacing the defined
identity carry by an arbitrary marker rule; it is not an assertion that any
physical marker must have zero jump.

## 7. Domain discipline

The theorem rejects:

- inexact numbers, including binary floating-point values;
- booleans masquerading as integers;
- nonpositive coefficients or lengths;
- coefficients that do not equal the defined `c(n)`;
- empty segment tuples;
- repeated, ascending, or skipped adjacent indices.

The runner implements these guards with exact `Fraction` arithmetic.  Its
normal, independent-reconstruction, hostile-input, and intentional-failure
modes exercise the theorem, exact inverse and associativity identities, empty
and nonempty marker lists, and individual plus aggregate mutation fixtures.

## 8. Physical nonclaims

This formal theorem supplies no physical coupling, QCD beta function,
active-flavor threshold, threshold mass or placement, coupling-continuity or
no-jump condition, decoupling rule, Lambda parameter, `alpha_s(M_Z)` value,
or scale-setting prescription.  It does not establish that any physical
system realizes the defined coefficient sequence, segment data, or identity
carry.  A physical consumer would need independent authority for every such
identification.

The earlier conditional physical interpretation of this row is withdrawn.
The exact affine algebra may be reused only after a consumer supplies its own
typed data and separately proves any physical interpretation.

## 9. Audit boundary

`proposed_retained` is an author-side proposal for the exact theorem above,
not an audit verdict.  The independent audit lane owns the effective status.
This note neither derives nor registers a new premise and does not alter any
audit artifact.

## 10. Reproducibility

Run:

```bash
python3 scripts/frontier_alpha_s_heavy_threshold_matching_kernel_2026_06_18.py
python3 scripts/frontier_alpha_s_heavy_threshold_matching_kernel_2026_06_18.py --independent
python3 scripts/frontier_alpha_s_heavy_threshold_matching_kernel_2026_06_18.py --hostile
```

Expected summaries:

```text
SUMMARY: PASS=32 FAIL=0
SUMMARY: PASS=12 FAIL=0
SUMMARY: PASS=23 FAIL=0
```

The cached normal-mode output is recorded at
`logs/runner-cache/frontier_alpha_s_heavy_threshold_matching_kernel_2026_06_18.txt`.
