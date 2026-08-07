# The C₃ Sector Dial Is Invariant Under a Common Mass Rescaling, So It Has a Convention-Free Common-Scale Value (Bounded Theorem + Comparator Correction)

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

## Question

[`QUARK_MASS_SPECTRUM_KOIDE_SCHEME_OPEN_GATE_NOTE_2026-05-26.md`](QUARK_MASS_SPECTRUM_KOIDE_SCHEME_OPEN_GATE_NOTE_2026-05-26.md)
opens the quark lane with a warning: quark masses are renormalization-scheme
and scale dependent, so "any numerical comparison must make the quark mass
scheme explicit," and its own displayed quark dials are labelled
"observational comparators only" under a "packet-local central-value
comparator convention."

That warning is correct as stated. This note asks the sharper question it
leaves open:

> Is the **dial** `(r, δ)` itself scheme- and scale-dependent, or only the
> mass **scale** it sits on?

The answer is a clean split. The dial is invariant under any common rescaling
of a sector's three masses, and flavour-universal QCD running is exactly such
a rescaling. So the dial has a **single value per sector**, independent of the
common reference scale chosen — while the overall scale does not.

The practical consequence is that the open gate's displayed numbers do not
measure the dial: they mix reference scales, and mixed-scale re-quoting is
precisely the operation the invariance does *not* cover.

## Setting

For three generation coordinates `x_k = sqrt(m_k)` with `S = Σ x_k ≠ 0`, the
Brannen/C₃ circulant parametrization is `x_k = a + 2|b| cos(δ + 2πk/3)` with
`a = S/3`, and the dial is `r = |b|²/a²`, `δ = arg b`, with
`Q = Σm_k / S² = (1 + 2r)/3`.

Ordering `x_0 ≥ x_1 ≥ x_2`, the Fourier coefficient
`b = (1/3) Σ_k x_k ω^{-k}` (with `ω = e^{2πi/3}`) has

```text
C = Re(b)/a        = (x_0 - (x_1 + x_2)/2) / (3a)
J = Im(b)/(a·√3)   = (x_2 - x_1) / (6a)
r = C² + 3J²       δ = atan2(√3·J, C)
```

`C` and `J` are **rational** in the `x_k`, so the whole dial is pinned by an
exact rational pair. The runner's load-bearing checks take no square roots and
use no floating point.

## Theorem

### T1 — homogeneity (exact)

`Q`, `r`, `C`, and `J` are unchanged under `m_k ↦ λ m_k` for every `λ > 0`,
equivalently `x_k ↦ μ x_k` with `μ = √λ`. Each is a ratio of forms of equal
degree in `x`, so `μ` cancels identically. Since `μ > 0` preserves the
descending order, the ordering convention is applied to the same ordering
before and after.

This is elementary and is **not claimed as new** — degree-0 homogeneity of the
Koide ratio is standard, and the coordinate identity `Q = (1 + 2r)/3` is repo
prior art
([`CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md`](CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md)).
It is reproduced exactly here because T3 is its converse and needs the same
coordinates.

### T2 — flavour-universal running is a common rescaling (supplied condition)

**Supplied, not derived:** in QCD the MSbar mass anomalous dimension `γ_m`
depends on the coupling and the active flavour number only, not on which quark
is being run, so on a fixed-flavour surface

```text
m_q(μ) = R(μ, μ₀) · m_q(μ₀)   with one R for every q in the sector.
```

This is already recorded in the repo at
[`CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md`](CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md)
eq. (5.6), which uses it for mass *ratios*. Applying it to the dial is
immediate from T1 with `λ = R`: **a sector's dial does not depend on the
common reference scale.**

The same universality survives flavour thresholds: the decoupling coefficient
`ζ_m` relating `m_q^{(n_f)}` to `m_q^{(n_f-1)}` depends on the decoupled heavy
mass, the coupling and `μ` — not on `q`. It is therefore also common to the
sector, provided every mass being matched is a light flavour at that
threshold. See the scope boundary for where that proviso bites.

### T3 — the converse: unequal factors do move the dial (exact)

A **mixed-scale** convention quotes different generations at different
reference scales. That applies `m_k ↦ λ_k m_k` with the `λ_k` not all equal,
which is outside T1's hypothesis — and the failure is not an edge case:

*Lemma (exact).* On the triple `x = (1, 1, 0)`, scaling the first two
coordinates by `μ₁, μ₂` gives `Q = (μ₁² + μ₂²)/(μ₁ + μ₂)²`, and

```text
2(μ₁² + μ₂²) − (μ₁ + μ₂)²  =  (μ₁ − μ₂)² ,
```

so `Q` returns its unscaled value `1/2` **iff** `μ₁ = μ₂`. Any unequal pair of
factors moves it. The runner also exhibits strictly positive, nondegenerate
rational triples on which unequal factors move both `Q` and `r`, with the
before/after values displayed as exact fractions.

So "the dial is convention-free" is true for the common-scale class and false
outside it. There is nothing to choose *within* the common-scale class, and
the choice *between* common-scale and mixed-scale is not a free convention —
only one of them is measuring the dial.

## What this does to the open gate's numbers (comparator)

Everything in this section is a **comparator**. It uses external PDG central
values and floating point, is not exact, is not a derivation step, and
supplies no premise. T1–T3 stand without it.

Reading the same PDG MSbar inputs at their quoted (mixed) scales versus at any
common scale:

```text
                                 r_up       r_down
open-gate note's displayed      0.773642    0.597141     (mixed scales)
common-scale, invariant         0.830971    0.621090
                                +0.0573     +0.0239
```

The runner reproduces the open gate's two displayed values to six decimals
from that note's own quoted mass list, which confirms the convention being
compared is the one it actually used.

With linear error propagation from PDG input uncertainties, the common-scale
dials are

```text
sector          Q                      r
charged lepton  0.666660511            0.499990767      (no QCD running)
up-type         0.887314 ± 0.001469    0.830971 ± 0.002204
down-type       0.747393 ± 0.004890    0.621090 ± 0.007335
```

and the six-common-scale invariance table agrees to float noise
(`2.4e-12` and `4.4e-16` spread across `μ = 2 GeV … 1 TeV`).

## What this buys the lane

The open gate's live blocker is stated as: "a retained positive quark-mass
spectrum lane must first supply a sector-specific mass scheme/scale **and**
quark dial theorem."

T1–T3 split that conjunction. The dial half is not scheme-blocked: no
framework-native mass scheme is needed to give a sector's `(r, δ)` a
well-defined value, only the discipline of quoting the three masses at a
common scale. The scale half — the overall `v₀` that turns a dial into masses
— is untouched and remains fully open.

That is a narrowing of an open gate, not a closing of it. Nothing here derives
a quark dial from the framework; it says only that the target the framework
would have to hit is a well-posed, convention-free number rather than a
scheme-contingent one.

It also hardens an existing negative direction without adding a new one: the
three sector dials sit at `0.4999907`, `0.6211 ± 0.0073`, `0.8310 ± 0.0022`,
which are `17σ` and `150σ` from the leptonic `1/2`. That spread can no longer
be attributed to scheme bookkeeping. Whether it forbids any particular
sector-blind supply of `r` is a question for a no-go note under the negative
gate, and is **not** claimed here.

## Prior art this note does NOT duplicate, and defers to

- Degree-0 homogeneity of `Q` is standard textbook Koide algebra and is not
  claimed as new.
- `Q = (1 + 2r)/3` and `r = 1/2 ⟺ Q = 2/3` are repo prior art
  ([`CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md`](CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md)),
  reproduced here only as a coordinate consistency check.
- Flavour-universality of QCD mass running is repo prior art
  ([`CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md`](CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md)
  eq. 5.6), there applied to mass ratios rather than to the dial. It enters
  here as a **supplied physics condition**, not as something derived.
- The `C₃` circulant/character algebra and the Koide-cone equivalence are
  prior art cited by the open gate itself and are not re-derived.

The content claimed here is: **T3** (the exact converse and its witness),
the identification that the open gate's comparator convention is a mixed-scale
one and therefore does not measure the dial, the corrected common-scale
comparator values, and the resulting split of the open gate's stated blocker.

## Non-claims

- This note **derives no quark mass**, no mass scale, no `v₀`, no quark
  Brannen phase, no sector weight, no species map, and no dial *value* from
  the framework. Every number in the comparator section is external.
- This note **does not close** the quark-mass-spectrum open gate, and supplies
  no part of a closing theorem.
- This note asserts **no** no-go. The `17σ`/`150σ` sector spread is displayed
  as a comparator; converting it into a negative claim about any candidate
  supply of `r` is separate work under the negative gate and is not attempted.
- No claim is made that a common reference scale is *physically* preferred.
  The claim is narrower: the dial is constant across the common-scale class,
  so that class has a single well-defined answer, and mixed-scale conventions
  do not.
- Charged-lepton QED running is neglected in the comparator, as it is in the
  open gate.
- No axiom, approved primitive, registry entry, or audit verdict is added,
  edited, retired, or predicted. The Tier-A count is unchanged.

## Scope boundary

Three-generation sectors, real nonnegative generation coordinates, nonzero
coordinate sum. `Q` and `r` are undefined at `Σx = 0`, which the runner
excludes rather than samples.

The common scale must be one at which all three masses of the sector are
legitimate active-flavour MSbar masses. Taking it **above all thresholds**
(`n_f = 6`) satisfies this with no extrapolation. The `μ = 2 GeV` row of the
invariance table runs `m_t` below its own threshold, which is a formal
extrapolation; it is displayed only to exhibit the invariance and no result
here depends on it.

Residual comparator systematics not separately itemized: the active-flavour
convention attached to the quoted 2 GeV light-quark masses, and neglected
higher-order decoupling. Both are well inside the quoted PDG input errors,
which are dominated by `m_s` in the down sector and `m_t` in the up sector.

## Reproduce

```bash
python3 scripts/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.py
```

Parts A–C are standard library only — `fractions.Fraction` and integers
throughout, no floating point, no randomness. Part D is explicitly marked
comparator-only and uses `math` for the four-loop running.
