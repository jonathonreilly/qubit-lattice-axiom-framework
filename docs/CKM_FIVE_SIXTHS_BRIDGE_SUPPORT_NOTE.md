# CKM Five-Sixths Bridge Support Note

**Date:** 2026-04-16
**Status:** bounded support tool for the down-type CKM-dual mass-ratio lane
**Type:** bounded_theorem
**Primary runner:** `scripts/frontier_ckm_five_sixths_bridge_support.py`

## Safe statement

On the current `main` surface:

- exact `SU(3)` group theory gives `C_F - T_F = 5/6`
- the promoted CKM atlas package gives `|V_cb| = alpha_s(v) / sqrt(6)`
- the bounded `5/6` bridge then gives
  `m_s/m_b = [alpha_s(v)/sqrt(6)]^(6/5)`

This bounded extraction matches the threshold-local self-scale comparator
`m_s(2 GeV)/m_b(m_b)` at `+0.20%`.

If `m_s` is first run to the common scale `m_b`, the same comparison moves to
`m_s(m_b)/m_b(m_b)` and the deviation widens to about `+15%`. The two
comparison surfaces are related by the standard 1-loop transport factor

$$
\frac{m_s(2\,\mathrm{GeV})}{m_b(m_b)}
=
\frac{m_s(m_b)}{m_b(m_b)}
\left[\frac{\alpha_s(2\,\mathrm{GeV})}{\alpha_s(m_b)}\right]^{12/25}.
$$

That is strong support for using the threshold-local mixed/self-scale
comparator as the live observation surface for this bounded bridge. It is not
yet a theorem-grade derivation of either:

- the full non-perturbative `5/6` exponentiation mechanism at `g = 1`, or
- the exact scale-selection rule from the framework alone.

## Exact content

The exact part of the support stack is narrow but real:

- `C_F = 4/3`
- `T_F = 1/2`
- `C_F - T_F = 5/6`
- promoted CKM atlas/axiom package gives `|V_cb| = alpha_s(v)/sqrt(6)`

So the only non-exact step in this note is the bridge from the CKM quantity to
the down-type mass ratio:

$$
|V_{cb}| = \left(\frac{m_s}{m_b}\right)^{5/6}.
$$

## Bounded bridge read

Using the canonical same-surface value `alpha_s(v) = 0.103303816122` gives

$$
|V_{cb}|_{\mathrm{atlas}} = \frac{\alpha_s(v)}{\sqrt{6}} = 0.0421736
$$

and therefore

$$
\left(\frac{m_s}{m_b}\right)_{\mathrm{pred}}
=
|V_{cb}|_{\mathrm{atlas}}^{6/5}
=
\left[\frac{\alpha_s(v)}{\sqrt{6}}\right]^{6/5}
=
0.0223897.
$$

The PDG threshold-local self-scale comparator is

$$
\frac{m_s(2\,\mathrm{GeV})}{m_b(m_b)} = \frac{93.4\,\mathrm{MeV}}{4.180\,\mathrm{GeV}}
= 0.0223445,
$$

so the bounded bridge misses by only `+0.20%`.

## Deviation decomposition

The current small residual error separates cleanly into:

1. **bridge intrinsic accuracy on the observation surface**

   $$
   \left(\frac{m_s}{m_b}\right)_{\mathrm{obs\ from}\ |V_{cb}|}
   =
   |V_{cb}|_{\mathrm{PDG}}^{6/5}
   =
   0.0224065,
   $$

   which differs from the threshold-local comparator by `+0.28%`;

2. **atlas `|V_cb|` shift**

   the promoted CKM package gives `|V_cb| = 0.0421736`, which is `-0.06%`
   relative to the current comparator value `0.0422`, and translates into a
   `-0.075%` shift on the extracted ratio.

These multiply exactly:

$$
\frac{(m_s/m_b)_{\mathrm{pred}}}{(m_s/m_b)_{\mathrm{self}}}
=
\frac{(m_s/m_b)_{\mathrm{pred}}}{(m_s/m_b)_{\mathrm{obs\ from}\ |V_{cb}|}}
\cdot
\frac{(m_s/m_b)_{\mathrm{obs\ from}\ |V_{cb}|}}{(m_s/m_b)_{\mathrm{self}}}.
$$

That is why the live `m_s/m_b` prediction lands at `+0.20%` rather than the
`+0.28%` bridge-only offset.

## Scale statement

The live comparison surface is now:

- **threshold-local self-scale comparator**
  `m_s(2 GeV)/m_b(m_b)`

The current safe interpretation is:

- the bounded bridge is numerically coherent on the threshold-local
  self-scale surface;
- forcing a common-scale comparison strips off the one-loop transport factor
  and creates the larger mismatch;
- a theorem-grade derivation that this is the unique exact framework scale
  surface is still open.

So the mass-ratio lane should not say only “mixed-scale works, same-scale is
open.” The sharper current statement is:

- threshold-local self-scale support is real;
- full scale-choice closure is not yet theorem-grade.

## What this buys

This note upgrades the down-type mass-ratio lane in two ways:

1. the `5/6` bridge is no longer a naked bounded phrase with no current-main
   support note;
2. the scale qualifier is no longer just an unexplained PDG convention
   coincidence.

The lane is still bounded, but it now sits next to an explicit current-main
support stack. The first and third bullets below are non-authority peer or
downstream pointers for orientation; they are deliberately not one-hop
dependencies of this `5/6` bridge support note.

- GST support peer:
  `CKM_FROM_MASS_HIERARCHY_NOTE.md`
- `5/6` bridge support:
  this note
- down-type extraction downstream:
  `DOWN_TYPE_MASS_RATIO_CKM_DUAL_NOTE.md`

## What is not claimed

- a retained or theorem-grade derivation of the `5/6` bridge on the full
  framework surface
- a theorem-grade derivation of the exact scale-selection rule
- a closure of absolute `m_b` or `y_b`
- an upgrade of the down-type mass-ratio lane to retained / theorem-grade

## Validation

Run:

```bash
python3 scripts/frontier_ckm_five_sixths_bridge_support.py
```

Current expected result on `main`:

- `EXACT PASS=15`
- `BOUNDED PASS=7`
- `FAIL=0`

The runner checks:

- exact `SU(3)` identity `C_F - T_F = 5/6`
- exact Fraction derivation `C_F - T_F = (N^2-1)/(2N) - 1/2 = 5/6` at
  `N = 3` from SU(3) representation data, with the float constants `C_F`, `T_F`
  asserted equal to the exact values and the runner's compound float exponent
  asserted within one ulp of the exact `5/6`
- `N = 3` uniqueness in the scan window `N = 2..6` via the factorization
  `3N^2 - 8N - 3 = (3N+1)(N-3)`
- exact one-loop transport `gamma_0/(2 beta_0) = 12/25` at the threshold-local
  `n_f = 4` point (convention `gamma_0 = 6 C_F`,
  `beta_0 = 11 - 2 n_f/3`), with explicit `n_f = 3` (`4/9`) and `n_f = 5`
  (`12/23`) rejectors and an `N = 2` (`1/4`) exponent rejector
- exact promoted CKM input `|V_cb| = alpha_s(v)/sqrt(6)`
- bounded `m_s/m_b` extraction from the `5/6` bridge
- threshold-local self-scale transport from same-scale to PDG comparator
- exact multiplicative decomposition of the remaining deviation
