# Moduli Composition-Word Dial Sets Densify; The Word-Supplier Residual

**Date:** 2026-07-02
**Type:** bounded theorem (exact enumeration + density + boundary)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This note sets no audit row,
moves no ledger row, and closes no wall.

## Boundary

This note recomputes the fixed points of all finite mixed compositions of the
two dictionary-flow maps

```text
f(r) = 2r^2,
g(r) = r^2
```

from the supplied dictionary-flow surface. It proposes no selector, supplies
no composition word, bounds no physical number of composition steps, and uses
no empirical moduli. The result is an exact bounded theorem about this
composition class only.

Trace: this is frontier/constraint-map work stacked on the Block07 residual.
The consumer is the generation-moduli selector search space. The result
recontextualizes the owner-flagged mixed-composition lead: the pairwise mixed
points are real exact dial points, but they are not special once unrestricted
composition words are admitted.

## Load-Bearing Inputs

1. [`GENERATION_MODULI_SELECTOR_EXACT_CONSTRAINTS_BOUNDED_NOTE_2026-07-02.md`](GENERATION_MODULI_SELECTOR_EXACT_CONSTRAINTS_BOUNDED_NOTE_2026-07-02.md).
   Role: Block07 sibling with the two maps `f(r) = 2r^2`, `g(r) = r^2`,
   the single-step fixed sets, the pairwise mixed fixed points
   `2^(-1/3)` and `2^(-2/3)`, and the residual instruction to recompute
   the dial set for any admitted mixed-composition class. This sibling is a
   landed bounded source note; status remains independent-audit owned.

2. [`OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md`](OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md).
   Role: dictionary source for the maps. The source supplies the component
   dictionary `x = 2r`, giving `r -> 2r^2`, and the slot dictionary `x = r`,
   giving `r -> r^2`.

No other scientific inputs are used.

## T1. Closed Form For Every Composition Word

Let a length-`k` word be

```text
w = w_k o ... o w_1,        w_i in {f,g},
```

where `w_1` acts first. Then `w` acts on `r` as

```text
w(r) = 2^e_w r^(2^k),
```

with

```text
e_w = sum_{1 <= i <= k, w_i = f} 2^(k-i).
```

Proof by exact induction. For `k = 1`, `g(r) = r^2 = 2^0 r^2` and
`f(r) = 2r^2 = 2^1 r^2`, which agrees with the formula.

Assume the prefix

```text
w_j o ... o w_1
```

acts as `2^e r^(2^j)`. Appending one more letter gives two cases:

```text
g(2^e r^(2^j)) = (2^e r^(2^j))^2
               = 2^(2e) r^(2^(j+1)),
```

so the exponent updates as `e -> 2e`; and

```text
f(2^e r^(2^j)) = 2(2^e r^(2^j))^2
               = 2^(2e+1) r^(2^(j+1)),
```

so the exponent updates as `e -> 2e + 1`. Therefore each new letter shifts
all earlier binary contributions one place left, and contributes a final
binary digit `1` exactly when the new letter is `f`. After `k` letters this is
exactly

```text
e_w = sum_{w_i = f} 2^(k-i).
```

The fixed-point equation is

```text
2^e_w r^(2^k) = r.
```

Thus `r = 0` is always fixed. For `r > 0`, division by `r` gives

```text
r^(2^k - 1) = 2^(-e_w),
```

and the unique positive fixed point is

```text
r*_w = 2^(-e_w/(2^k - 1)).
```

This reproduces Block07's `k = 1,2` cases exactly:

| word | `e_w` | map | nonzero fixed point |
|---|---:|---:|---:|
| `f` | `1` | `2r^2` | `2^-1 = 1/2` |
| `g` | `0` | `r^2` | `1` |
| `f o f` | `3` | `8r^4` | `2^-1 = 1/2` |
| `f o g` | `1` | `2r^4` | `2^(-1/3)` |
| `g o f` | `2` | `4r^4` | `2^(-2/3)` |
| `g o g` | `0` | `r^4` | `1` |

The asymmetric pair is worth making explicit. In `f o g`, the `f` is the
second applied letter, so it contributes `2^(2-2) = 1`. In `g o f`, the `f`
is the first applied letter and is then squared by the later `g`, so it
contributes `2^(2-1) = 2`.

## T2. Achievable Exponents And Exact Dial Sets

For words of length `k`, `e_w` ranges over every integer

```text
0, 1, ..., 2^k - 1.
```

Indeed, the subset of positions at which `w_i = f` is exactly the binary
expansion

```text
e = b_1 2^(k-1) + b_2 2^(k-2) + ... + b_k 2^0,
```

where `b_i = 1` if `w_i = f` and `b_i = 0` if `w_i = g`. This is the standard
length-`k` binary numeral map from subsets of `{1,...,k}` to
`{0,...,2^k - 1}`. It is injective because binary expansions of fixed length
are unique, and it is surjective because each integer in that range has a
unique fixed-length binary expansion.

Therefore the length-`k` dial set is exactly

```text
D_k = {0} union {2^(-e/(2^k - 1)) : e = 0, 1, ..., 2^k - 1}.
```

The first four dial sets are:

```text
D_1 = {0, 2^0, 2^-1}

D_2 = {0, 2^0, 2^(-1/3), 2^(-2/3), 2^-1}

D_3 = {0, 2^0, 2^(-1/7), 2^(-2/7), 2^(-3/7),
       2^(-4/7), 2^(-5/7), 2^(-6/7), 2^-1}

D_4 = {0, 2^0, 2^(-1/15), 2^(-2/15), 2^(-3/15),
       2^(-4/15), 2^(-5/15), 2^(-6/15), 2^(-7/15),
       2^(-8/15), 2^(-9/15), 2^(-10/15), 2^(-11/15),
       2^(-12/15), 2^(-13/15), 2^(-14/15), 2^-1}
```

These lists are exact powers of `2`; no numerical approximation is used.

## T3. Densification And The Exact Lower Boundary

Write

```text
x_e = e/(2^k - 1),        e = 0, 1, ..., 2^k - 1.
```

Then the exponents in `D_k` are the uniform grid

```text
0, 1/(2^k - 1), 2/(2^k - 1), ..., 1,
```

with exact adjacent spacing

```text
x_(e+1) - x_e = 1/(2^k - 1).
```

As `k -> infinity`, this spacing tends to `0`. Hence the positive dial points

```text
2^(-x_e)
```

densify in the interval

```text
[2^-1, 2^0] = [1/2, 1].
```

The endpoints are fixed exactly for every `k`:

```text
e = 0          <=> all-g word <=> r* = 1,
e = 2^k - 1   <=> all-f word <=> r* = 1/2.
```

No positive fixed point below `1/2` is reached by any word in this class. For
every length-`k` word,

```text
0 <= e_w <= 2^k - 1,
```

so

```text
0 <= e_w/(2^k - 1) <= 1,
```

and therefore

```text
r*_w = 2^(-e_w/(2^k - 1)) >= 2^-1 = 1/2.
```

Thus the unrestricted finite-word composition class has dial range

```text
{0} union a dense subset of [1/2, 1],
```

and has no positive dial point in `(0, 1/2)`. This asymmetry is an exact
structural fact of the class.

## T4. Consequences

**Deflation.** Block07's mixed points `2^(-1/3)` and `2^(-2/3)` are not
special within the unrestricted finite-composition class. They are the two
interior positive points of `D_2`. For large `k`, the class approximates any
target in `[1/2, 1]` by choosing an appropriate binary word. Therefore
fixed-point selection has no discriminating power inside `[1/2, 1]` unless
the composition word itself is supplied or bounded.

The sharpened residual is the word-supplier question: what physical structure
supplies, selects, or bounds the composition word? A finite number of supplied
registration steps would be one possible shape of a bound on `k`, but this
note does not assert such a structure.

**Structure.** The exact lower boundary remains nontrivial. Every positive
fixed point of every word in this class satisfies

```text
r*_w >= 1/2.
```

Consequently, any hypothetical sector modulus below `1/2` cannot be a fixed
point of any finite word in the composition class generated by `f(r)=2r^2`
and `g(r)=r^2`. This statement is purely hypothetical and imports no
empirical sector modulus.

## Does NOT Claim

- Does not propose, derive, or fit a selector.
- Does not supply the composition word.
- Does not answer the word-supplier question.
- Does not supply or prove a physical bound on word length `k`.
- Does not use empirical moduli or any literature value.
- Does not assert any sector has a modulus in `[1/2,1]` or below `1/2`.
- Does not close a wall or move an audit ledger row.
- Does not claim the Block07 mixed points are false; it shows they are exact
  but not discriminating without a supplied or bounded word.

## Runner

Primary runner:

[`scripts/frontier_moduli_composition_word_dial_sets_2026_07_02.py`](../scripts/frontier_moduli_composition_word_dial_sets_2026_07_02.py)

Expected output cache:

[`logs/runner-cache/frontier_moduli_composition_word_dial_sets_2026_07_02.txt`](../logs/runner-cache/frontier_moduli_composition_word_dial_sets_2026_07_02.txt)
