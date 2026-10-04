# CKM Five-Sixths Bridge Support Note

**Date:** 2026-04-16
**Status:** bounded support tool for the down-type CKM-dual mass-ratio lane
**Type:** bounded_theorem
**Primary runner:** `scripts/frontier_ckm_five_sixths_bridge_support.py`


## Landing correction to the comparator (2026-10-04)

The common-scale diagnostic uses four-loop mass/coupling running with
explicit **two-loop** bottom-threshold coupling and strange-mass matching:
`m_s^(4)(mb) = [1 + (89/432)(alpha_s^(5)(mb)/pi)^2] m_s^(5)(mb)`.
It is a mixed-truncation diagnostic, not a fully matched four-loop prediction;
three-loop decoupling and truncation/systematic uncertainties remain open.
The earlier precise numbers below omitted strange-mass matching and are
superseded by the corrected runner. The mismatch remains about 19%.
The quoted PDG-2024 quark-mass errors are **90% confidence halfwidths**;
combining them with the 68% coupling error in quadrature measures sensitivity,
not a one-sigma significance or a joint statistical rejection. Any “16 sigma”
reading below is withdrawn. Ratio scale invariance applies to a common,
fixed-flavour, mass-independent QCD theory. The SM example only checks its
sampled scales in a supplied truncated one-loop flow (fixed tau Yukawa,
imported initial data, no threshold matching); it supplies no all-scale bound.
Mixed-scale root fits are restricted to the bracket `[1.3,8] GeV`; a root below
that bracket is not evaluated without charm matching.
Source for decoupling conventions: [RunDec, Eqs. 20 and 28](https://arxiv.org/pdf/hep-ph/0004189).
No framework coefficient, exponent or scale is derived by this comparison.

## Corrigendum (2026-09-30)

**What was wrong.** The `+0.20%` agreement quoted below compares the bridge with
the mixed-scale ratio `m_s(2 GeV)/m_b(m_b)`. That is not a scale-consistent test:
the ratio of two MS-bar masses at one energy is independent of that energy, so a
bridge on `m_s/m_b` has to be compared at one common scale. There, with four-loop
QCD running and PDG 2024 inputs (`m_s(2 GeV) = 93.5(8) MeV`,
`m_b(m_b) = 4.183(7) GeV`, `alpha_s(M_Z) = 0.1180(9)`), the transport is
`m_s(2 GeV)/m_s(m_b) = 1.184`, `m_s(m_b) = 78.97 MeV`,
`m_s(m_b)/m_b(m_b) = 0.018878`, and the bridge prediction `0.0223897` misses by
`+18.6% +- 1.2%` (about 16 sigma with PDG errors, atlas `|V_cb|` taken as exact;
`+16.9%` to `+20.4%` across standard input sets; `+20.6%` from lattice mass
ratios with no running). The "about `+15%`" and the one-loop transport factor
quoted below understate it: one-loop truncation gives `1.14` to `1.15`
against `1.184`.

**Corrected statement.** The exponent that fits the common-scale ratio is
`p = ln|V_cb| / ln(m_s/m_b) = 0.7975`, not `5/6` (at exponent `5/6` the prefactor
would have to be `1.153`), and it stays `0.79` to `0.80` up to the Planck scale
under one-loop Standard-Model running. The `+0.20%` needs the strange mass quoted
at `1.99 GeV`; the same mixed ratio fits `4/5` at `3.9 GeV`. It is a convention
coincidence. The sentences below that call the mixed-scale match "strong
support", call the threshold-local surface "the live observation surface", or say
the scale qualifier "is no longer just an unexplained PDG convention
coincidence" are withdrawn, as is the "Deviation decomposition" as evidence
(its arithmetic is unchanged; it decomposes a comparison that is not
scale-consistent).

**What still stands.** `C_F - T_F = 5/6`, `|V_cb|_atlas = alpha_s(v)/sqrt(6)`
as a supplied model, `R_pred = 0.0223897`, the exact `12/25` one-loop
coefficient, and every non-claim in "What is not claimed". The status of this
note is unchanged by this corrigendum; audit status remains with the independent
audit lane. Full table and evidence:
`CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md` (Corrigendum). Check:
`python3 scripts/frontier_ckm_five_sixths_common_scale_four_loop_correction_2026_09_30.py`.

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
