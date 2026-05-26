# Y_T Connected-Source Augmentation-Ideal Selector Narrow Theorem

**Date:** 2026-05-26
**Claim type:** bounded theorem / exact support bridge.
**Status authority:** independent audit lane only. This source note does not
set, predict, or estimate an audit verdict.
**Primary runner:** `scripts/frontier_yt_connected_source_augmentation_ideal_selector.py`
**Generated certificate:** `outputs/yt_connected_source_augmentation_ideal_selector_2026-05-26.json`

## Purpose

The repaired Y_T color-projection row leaves one precise selector open:

```text
K_Y(kappa_Y) = 8/9 + kappa_Y/9.
```

The open physical question is whether the Yukawa-side source reads the full
color trace (`kappa_Y = 1`) or only the connected/traceless channel
(`kappa_Y = 0`).  The existing no-go correctly says this cannot be derived
from Fierz channel counts alone.

This note proves a narrower positive bridge:

> On a normalized connected source-response surface for trace-one color
> records, the identity color source is a pure normalization direction.  The
> nonzero tangent source space is the augmentation ideal
> `End(C^N) / C I ~= sl_N`, with dimension `N^2 - 1`.  Therefore a
> Yukawa-side readout that is accepted to be this normalized connected source
> tangent selects `kappa_Y = 0` and `K_Y = (N^2 - 1)/N^2`, hence `8/9` at
> `N = 3`.

This is the same structural kind of move that the open Brannen/lepton stack
uses: remove the trivial character / identity orbit and read the nontrivial
augmentation-ideal part.  Here the object is the finite color matrix algebra,
not a phase convention.

## Setup

Let `V = C^N` be the color space, with `N >= 2`, and let
`A = End(V)` with Hilbert-Schmidt inner product

```text
<X, Y> = Tr(X^dagger Y).
```

The scalar identity line and traceless subspace give the orthogonal
decomposition

```text
A = C I  direct_sum  sl_N.
```

Let `rho` be a trace-one color record/state:

```text
Tr rho = 1.
```

For a Hermitian source insertion `J`, define the normalized source family

```text
R_J(rho) = exp(Tr(J rho)) / Z(J).
```

The connected score for source direction `J` at `J = 0` is

```text
score_J(rho) = Tr(J rho) - E_0[Tr(J rho)].
```

This is the standard normalized Radon-Nikodym source tangent: constants in
`Tr(J rho)` vanish because they are absorbed by `Z(J)`.

## Theorem

For the normalized source family above:

1. **Identity source is null in connected response.**

   If `J = a I`, then

   ```text
   Tr(J rho) = a Tr rho = a
   ```

   is constant on the trace-one source surface, so

   ```text
   score_(a I)(rho) = a - E_0[a] = 0.
   ```

   Therefore the identity/singlet color source is a normalization direction,
   not a physical connected tangent.

2. **Connected tangent depends only on the traceless projection.**

   Write

   ```text
   J = (Tr J / N) I + J_0,       Tr J_0 = 0.
   ```

   Then

   ```text
   score_J(rho) = score_(J_0)(rho).
   ```

   Thus the normalized connected source map factors through the quotient

   ```text
   End(C^N) / C I,
   ```

   equivalently through the augmentation ideal `sl_N`.

3. **Dimension fraction.**

   The full color matrix algebra has dimension `N^2`; the connected tangent
   image has dimension `N^2 - 1`.  The connected-source fraction is therefore

   ```text
   K_connected(N) = (N^2 - 1) / N^2.
   ```

   At the framework color value `N = 3`,

   ```text
   K_connected(3) = 8/9.
   ```

4. **Y_T selector consequence under the connected-source premise.**

   The corrected Y_T family is

   ```text
   K_Y(kappa_Y) = (N^2 - 1)/N^2 + kappa_Y/N^2.
   ```

   On the normalized connected source surface, the identity channel is in the
   kernel.  Therefore the singlet contribution coefficient is

   ```text
   kappa_Y = 0,
   ```

   and the selected readout is

   ```text
   K_Y = (N^2 - 1)/N^2 = 8/9  at N = 3.
   ```

## Proof

### Step 1: normalized source kills constants

For any source observable `O_J(rho) = Tr(J rho)`,

```text
log R_J(rho) = O_J(rho) - log Z(J).
```

Differentiating at zero source in the direction `J` gives the centered
observable

```text
d log R_(tJ)(rho)/dt |_(t=0)
  = O_J(rho) - E_0[O_J].
```

If `O_J` is constant, the centered observable is zero.

### Step 2: identity source is constant on trace-one color records

For `J = a I` and `Tr rho = 1`,

```text
O_(aI)(rho) = Tr(a I rho) = a.
```

By Step 1, its connected score vanishes.  This proves that the identity
source is normalization-only.

### Step 3: quotient by the identity line

Every `J in End(C^N)` decomposes uniquely as

```text
J = (Tr J / N) I + (J - (Tr J / N) I).
```

The first term is killed by Step 2.  The second term is traceless.  Therefore
the connected source tangent is represented by the traceless projection

```text
J_0 = J - (Tr J / N) I.
```

The kernel contains exactly the identity line on the matrix-source sector, so
the image has dimension `N^2 - 1`.

### Step 4: color fraction and kappa selector

The full color insertion algebra has dimension `N^2`; the nonzero connected
source tangent has dimension `N^2 - 1`.  Therefore the connected-source
dimension fraction is `(N^2 - 1)/N^2`.  Comparing with the repaired Y_T
family,

```text
K_Y(kappa_Y) = (N^2 - 1)/N^2 + kappa_Y/N^2,
```

the normalized connected source kernel excludes the identity/singlet
contribution.  Hence `kappa_Y = 0` on this source surface.  At `N = 3`, this
is `K_Y = 8/9`.  QED.

## What This Closes

This note closes the algebraic selector on the **connected normalized source
surface**:

```text
normalized connected color source tangent
  -> identity channel is normalization-only
  -> tangent space is sl_3
  -> kappa_Y = 0
  -> K_Y = 8/9.
```

It gives the missing positive route named by the repaired color-projection
no-go, but only after the Y_T lane accepts or derives that the physical
Yukawa-side scalar/source readout is this normalized connected source tangent.

## What Remains Open

This note does **not** by itself close retained Y_T:

- It does not prove that the physical neutral EW/Higgs source-action surface
  is the normalized connected color source family used here.
- It does not derive canonical `O_H`.
- It does not derive scalar LSZ normalization.
- It does not produce strict `C_ss/C_sH/C_HH` pole rows or a W/Z physical
  response bypass.
- It does not compute or claim a physical `y_t` value.
- It does not use or repair the old `H_unit` / Ward-identity route.

Thus the practical consequence is a narrowed blocker:

```text
derive/accept same-surface normalized connected source-action authority
  + canonical O_H / scalar LSZ
  -> this theorem supplies the kappa_Y = 0 selector.
```

## Firewalls

This theorem does not use `H_unit`, `yt_ward_identity`, `y_t_bare`, observed
top/Yukawa values, `alpha_LM`, plaquette/u0, package-v, Planck, alpha_s, or a
fitted selector.  The only numerical value `8/9` is the exact finite
dimension fraction `(3^2 - 1)/3^2`.

## Verification

Run:

```text
python3 scripts/frontier_yt_connected_source_augmentation_ideal_selector.py
```

Expected result:

```text
SUMMARY: PASS=90 FAIL=0
```

The green runner certifies the finite-dimensional source-tangent algebra and
the explicit claim boundary.  It does not certify full Y_T closure.
