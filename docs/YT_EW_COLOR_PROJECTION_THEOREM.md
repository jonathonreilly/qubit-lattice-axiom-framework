# EW Color Projection Kappa-Family No-Go

**Date:** 2026-04-14; kappa-family repair 2026-05-26
**Runner:** `scripts/yt_ew_kappa_family_nogo_certificate.py`
**Claim type:** no_go
**Status:** exact algebraic support for the `K_EW(kappa_EW)` family plus a
bounded no-go for deriving the connected-trace specialization
`kappa_EW = 0` from the current packet.

## Scope

The exact SU(3) Fierz/channel-count support gives

```text
F_adj = (N_c^2 - 1) / N_c^2 = 8/9.
```

That algebra is not the problem. The missing step is the physical
EW-current readout selector: whether the disconnected/singlet channel is
discarded, included, or assigned an intermediate coefficient. Write that
coefficient as `kappa_EW`.

The binding algebraic family is:

```text
R_phys(kappa_EW) = F_adj + kappa_EW (1 - F_adj)
K_EW(kappa_EW) = 1 / R_phys(kappa_EW)
```

At `N_c = 3`:

```text
K_EW(kappa_EW) = 1 / (8/9 + kappa_EW/9).
```

The familiar package number `K_EW = 9/8` is the specialization
`kappa_EW = 0`. The full-trace specialization `kappa_EW = 1` gives
`K_EW = 1`. The current packet does not derive which value Nature or the
framework readout must select.

No new axiom, fitted selector, or audit verdict is introduced.

## Binding Claim

On the current packet:

1. `F_adj = 8/9` is exact SU(3) Fierz/channel-count algebra.
2. `K_EW(kappa_EW) = 1 / (8/9 + kappa_EW/9)` is exact rational algebra for
   any fixed `kappa_EW`.
3. The same multiplicative factor `sqrt(K_EW(kappa_EW))` applies to the EW
   gauge couplings `g_1` and `g_2`, so the weak-angle ratio is preserved for
   any fixed `kappa_EW`.
4. The value `kappa_EW = 0` is not selected by the Fierz fraction, by common
   rescaling, by the weak-angle preservation property, or by the historical
   numerical agreement after choosing that value.

Therefore this row is not an unconditional color-projection theorem for
`K_EW = 9/8`. It is a finite kappa-family/no-go boundary: downstream uses of
`9/8` must say "conditional on the connected-trace specialization
`kappa_EW = 0`" unless a future retained selector theorem closes that
coefficient.

## Historical Numerical Diagnostic

The old numerical comparison remains useful as a diagnostic after choosing
`kappa_EW = 0`: applying `sqrt(9/8)` to the historical lattice-side
`g_1(v)` and `g_2(v)` values moves them close to the quoted physical values.
That agreement is not a derivation of `kappa_EW = 0` and is not used as a
load-bearing proof input in this repaired row.

## What This Note Does Not Claim

- It does not claim that `kappa_EW = 0` is derived.
- It does not claim an unconditional package coefficient `K_EW = 9/8`.
- It does not use observational agreement to fit or ratify the selector.
- It does not add a new axiom or convention.
- It does not apply an audit verdict.

## Runner Certificate

The companion runner verifies:

- the exact `F_adj = 8/9` fraction at `N_c = 3`;
- `K_EW(0) = 9/8`, `K_EW(1/2) = 18/17`, and `K_EW(1) = 1`;
- the kappa-family identity for several rational `kappa_EW` values;
- weak-angle preservation under the common `sqrt(K_EW)` rescaling;
- CMT-style common-scale invariance of the family; and
- source-note hygiene for this no-go boundary.

Expected local certificate:

```text
RUNNER STATUS: PASS (PASS=26 FAIL=0)
```

## Reopen Conditions

Reopen the unconditional `K_EW = 9/8` theorem only with a retained-grade
lattice-current selector theorem or an exact disconnected-current coefficient
computation that fixes `kappa_EW = 0` from accepted primitives. Until then,
the science retained by this row is the exact kappa-family algebra, not a
closed selector.
