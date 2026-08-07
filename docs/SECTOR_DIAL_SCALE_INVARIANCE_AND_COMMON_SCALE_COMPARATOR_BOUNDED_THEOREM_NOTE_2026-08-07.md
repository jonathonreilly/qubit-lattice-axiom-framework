# The Quark-Lane Dial Comparators Are Mixed-Convention; Corrected Common-Scale Values (Comparator Correction with Exact Support)

**Date:** 2026-08-07
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** proposed_retained
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit outcome, and edits no registry.
**Primary runner:**
[`scripts/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.py`](../scripts/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.py)
**Cached runner output:**
[`logs/runner-cache/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.txt`](../logs/runner-cache/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.txt)

## What this corrects

[`QUARK_MASS_SPECTRUM_KOIDE_SCHEME_OPEN_GATE_NOTE_2026-05-26.md`](QUARK_MASS_SPECTRUM_KOIDE_SCHEME_OPEN_GATE_NOTE_2026-05-26.md)
displays quark dial values `r_up = 0.773642` and `r_down = 0.597141`, correctly
labelled "observational comparators only" under a "packet-local central-value
comparator convention."

That convention quotes the three masses of a sector at **different reference
scales** — and, in the up-type sector, mixes a pole mass with MSbar masses.
Re-quoting a mass triple with unequal per-generation factors is precisely the
operation the dial is *not* invariant under. So those numbers do not measure
the dial, and this note supplies the values that do.

This is the repo's only source note carrying them; the two audit-data files
that also contain them are pipeline-generated and belong to the audit lane.

## The correction

```text
                                       r_up       r_down
open-gate note, as displayed         0.773642    0.597141   (mixed scale; pole top)
same inputs, MSbar top m_t(m_t)      0.767630    0.597141   (mixed scale only)
canonical common scale               0.830971    0.621090
                                     ± 0.002204  ± 0.007335
```

The runner reproduces the open gate's two displayed values to six decimals from
that note's own quoted mass list, which confirms the convention being compared
is the one it actually used. The `+0.0573` shift in `r_up` splits as `−0.0060`
from pole→MSbar and `+0.0633` from the scale correction.

For reference, the charged-lepton dial under the same treatment is
`r = 0.499990767 ± 0.0000102`, i.e. `0.9σ` from exactly `1/2`.

The corrected values sit *further apart* than the ones they replace. Anyone
using the sector spread should note that this correction widens it rather than
narrowing it.

## Why the common-scale convention is the well-defined one

Two ingredients, both **prior art**, and one exact step that is not.

**Homogeneity (prior art, not claimed here).** `Q`, `r` and the rational pair
`(C, J)` pinning `δ` are ratios of equal-degree forms in `x_k = √m_k`, so a
common rescaling `m_k ↦ λ m_k` cancels identically.
[`CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md`](CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md)
already records that `r` "is invariant under every permutation of the mass
triple and under a common positive rescaling of all three masses." The runner
reproduces it exactly only because the step below needs the same coordinates.

**Flavour-universal running (prior art, supplied physics).** In QCD the MSbar
mass anomalous dimension depends on the coupling and the active flavour number
only, so on a fixed-flavour surface one factor `R(μ, μ₀)` rescales the whole
sector. Recorded at
[`CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md`](CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md)
eq. (5.6), there used for mass ratios. Combined with homogeneity: **within a
fixed scheme, a sector's dial does not depend on which common reference scale
is chosen.** The runner exhibits this across six common scales spanning three
decades, agreeing to `4e-12`.

**Sharpness (exact, the one thing claimed here).** The equal-factor hypothesis
is doing real work, not sitting there as a removable technicality. On the
triple `x = (1, 1, 0)`, scaling the two nonzero coordinates by `μ₁, μ₂` gives

```text
2(μ₁² + μ₂²) − (μ₁ + μ₂)²  =  (μ₁ − μ₂)² ,
```

so `Q` returns its unscaled value **iff** `μ₁ = μ₂`. The runner also moves both
`Q` and `r` on strictly positive nondegenerate rational triples, with exact
before/after fractions.

This is a **sharpness witness, not a converse**, and the distinction is
load-bearing. The literal converse — dial unchanged ⟹ all `λ_k` equal — is
**false**: the dial depends only on the mass *multiset*, so `x = (4, 2, 1)`
with `λ = (1/4, 1, 4)` permutes the multiset and leaves `Q` and `r` exactly
fixed. The runner exhibits that counterexample so the stronger reading cannot
return by accident.

## Canonical prescription (load-bearing)

The common scale must be one at which all three masses are legitimate
active-flavour MSbar masses. A quark below its **own** threshold is decoupled,
so `μ ≥ m_t` for up-type and `μ ≥ m_b` for down-type; **taking `μ ≥ m_t`
satisfies both and is the prescription adopted here.** At `μ ≥ m_t` every mass
is transported *upward* only, so at each threshold it crosses it is a light
(active) flavour, no sector member is ever the decoupled one, and the
decoupling coefficient is common to the sector.

The sub-threshold rows of the runner's invariance table are **display-only**:
they extrapolate `m_t` (both sectors, four of six rows including `μ = M_Z`) and
`m_b` (down sector, at 2 GeV) below their own thresholds. They exist to exhibit
the invariance; every one agrees with the canonical value to `4e-12`, so no
displayed digit depends on them.

## Two named conditions

**Mass scheme is a named residual, not a resolved one.** Everything here sits
inside one fixed scheme (MSbar); the invariance covers the reference scale
only. A change of scheme is generally *not* a common rescaling — the MSbar→pole
factor `1 + 4α_s(m_q)/3π + …` is evaluated at each quark's own mass (`≈1.164`
at `m_c` against `≈1.046` at `m_t`), so converting the up-type sector to pole
masses moves `r_up` by about `−0.010`, roughly `4.5σ` of the propagated input
error. A framework-native dial target must still name its scheme.

**The mass-to-dial dictionary is non-retained.** The values above are not
measured values of `r`. They are computed from PDG masses through the
C₃-circulant parametrization *together with* the identification of its
eigenvalues as one-leg amplitudes `√m` rather than masses.
[`QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md`](QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md)
records that identification verbatim among its "non-retained inputs" (`P1`).
The exact content above is unaffected — it concerns a defined function of three
masses and holds whatever that function is later identified with — but any
reading of these numbers *as the framework's dial* is conditional on `P1`.

## What this buys the lane

The open gate's blocker is stated as a conjunction: a quark-mass lane needs a
sector-specific mass scheme/scale **and** a dial theorem. This separates the
two. Fixing a scheme leaves no residual freedom in the reference scale, so the
scale half of that conjunction is not an obstruction to defining the dial —
only to fixing `v₀`. The scheme half stands, unreduced.

That is a narrowing, and a corrected set of comparators to aim at. It **does
not close** the open gate and supplies no part of a closing theorem.

## Prior art this note does NOT duplicate, and defers to

- Degree-0 homogeneity, and the rescaling invariance itself, are already in
  `CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11`,
  along with `Q = 1/3 + 2r/3` and `r = 1/2 ⟺ Q = 2/3`.
- Flavour-universality of QCD mass running is in
  `CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22` eq. (5.6), which
  also carries the principle that a mixed quantity has an extra scale
  prescription baked in.
- The C₃ circulant/character algebra and the Koide-cone equivalence are prior
  art cited by the open gate itself.
- That a single universal `r` cannot fit all three sectors is already recorded
  qualitatively in `FOURTH_AXIOM_RG_SCALE_DYNAMICS_SCOPING_2026-06-05` §2.1.
  This note does not restate or quantify it; it only supplies corrected inputs.

Claimed here: the sharpness witness and its counterexample, the identification
that the open gate's convention is mixed-scale and mixed-scheme, the canonical
`μ ≥ m_t` prescription, and the corrected comparator values.

## Dependency standing (disclosure)

The open-gate dependency is `unaudited`/`open_gate`; the CKM dependency is
`audited_conditional`. Both are retained-grade blockers, so whatever
chain-derived grade this note receives will be limited by them. That is the
audit lane's determination, not this note's.

## Non-claims

- This note **derives no quark mass**, no mass scale, no `v₀`, no Brannen
  phase, no sector weight, no species map, and no dial *value* from the
  framework. Every number is an external comparator.
- It **does not close** the quark-mass-spectrum open gate.
- It asserts no no-go, and makes no claim about why the sectors differ.
- It does not claim the dial is scheme-independent — see the named conditions.
- No claim that a common reference scale is *physically* preferred; only that
  the dial is constant across the common-scale class while mixed conventions
  give convention-dependent answers.
- Charged-lepton QED running is neglected, as it is in the open gate.
- Reconciling the open gate's own displayed values is left to that note's
  owners; nothing here edits it.
- No axiom, approved primitive, registry entry, or audit verdict is added,
  edited, retired, or predicted. The Tier-A count is unchanged.

## Scope boundary

Three-generation sectors, real nonnegative generation coordinates, nonzero
coordinate sum; `Q` and `r` are undefined at `Σx = 0`, which the runner
excludes rather than samples. Symmetric linear error propagation from PDG
inputs. Residual comparator systematics — the active-flavour convention on the
quoted 2 GeV light-quark masses, and neglected higher-order decoupling — act on
only the subset of masses quoted at 2 GeV and are therefore themselves unequal
per-generation factors; the runner bounds them directly, and a common `+0.3%`
shift on the 2 GeV masses moves `r_down` by `4.2e-4` (`0.06σ`).

## Reproduce

```bash
python3 scripts/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.py
```

Load-bearing parts are standard library only — `fractions.Fraction` and
integers, no floating point, no randomness. The comparator part is tallied
separately and supplies no premise.
