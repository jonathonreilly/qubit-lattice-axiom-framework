# Flavor — 7-angle panel verdict on the heat-kernel route (and a label fix)

**Date:** 2026-05-29
**Claim type:** panel synthesis / honest verdict + correction (NOT a derivation).
Imports nothing; the lit comparators below are flagged as imports.
**Runner:** `scripts/flavor_panel_heat_kernel_verdict_2026_05_29.py` (+ cache).
**Source:** 7-angle workflow panel (5 angles reported; 2 failed to return
structured output) attacking "what fixes the Casimir time `t` / why `b/a` (r=½,
Q=2/3)" with an import-filter, adversarial verify, and a lit-search
disambiguator. Verdict for `FLAVOR_CASIMIR_HEAT_KERNEL_CORNER_COUPLING_NOTE`.

## Headline
**No angle natively, non-circularly forced `t=1.2242` / `r=½`.** The heat-kernel
route is a real, import-free *characterization* (`r=tanh⁴(t)`), and genuinely
*independent of the chiral-grading import* — but it does not force the value, and
in the **physical basis it gives `Q=1/3`.** Three claims, all verified to ~1e-15.

## (a) The decisive caveat — wrong basis
The cube heat kernel `K_t` is **exactly diagonal in the character/momentum
(Hadamard) basis** (off-diagonal ~1e-16). The retained carrier
(`CL3_TASTE_GENERATION_THEOREM`, `SITE_PHASE_CUBE_SHIFT_INTERTWINER`) identifies
the hw=1 generation labels as **momentum/BZ-corner (taste) indices** — exactly
that Hadamard basis. So in the **physical** basis `b=0 → r=0 → Q=1/3`, matching
the fermion-vacuum capstone. The off-diagonal `b≠0` (hence `r=tanh⁴(t)` spanning
`(0,1)`) lives only in the **dual position-cube basis**; it is a taste-breaking
amplitude of *free strength*, generic to any 2-parameter C₃-symmetric ansatz —
not special to the cube. This substantially deflates the lead.

## (b) A label correction (mine, caught by the panel)
`b/a = tanh²(t) = 1/√2 = 0.7071` at `r=½` — **not** `2^{-1/4}`. The value
`2^{-1/4}=0.8409` is `tanh(t)`, the per-edge flip amplitude, one square-root off.
`r=½`, Q=2/3 are unaffected. This restores agreement with the consolidation note
(`b = (1/√2)·a`). `2^{-1/4}` carries no independent algebraic content — it is
literally `(1/2)^{1/4}`.

## (c) The isotype-equipartition reframing — same unforced `t`
The C₃ isotype equipartition `|c₀|²(singlet) = |c₁|²+|c₂|²(doublet)` **is exactly
`r=½`**, and for the heat kernel it requires `a/b = K_t(0)/K_t(2) = √2`, which
holds **only at `t=1.2242`**. The ratio varies continuously with `t`; no cube
symmetry forces it. So reframing `r=½` as "isotype equipartition" does not force
it either.

## Genuine positive — the route is chirality-independent
Angle 5 (survived adversarial verify, non-circular): the heat-kernel Yukawa
`Y=aI+bC+b̄C²` **commutes** with `Γ_χ` (`[Y,Γ_χ]=0`), so it reaches `r=½` by
**Fourier-weight balance** (`a²=2|b|²`), *not* by the anticommutation
`{H,Γ_χ}=0` the retained no-go forbids. It therefore lives in the case the no-go
**leaves open** — a genuinely independent frame, not the chiral import in
disguise.

## Imports the panel caught
- **Algebraic "2" = ℝ[Z₃] block count** → import/circular (the undetermined
  counting measure; the ledger ranks it vs the dimension measure → Q=1).
- **Cube hopping as kinetic metric** → import (the position-cube basis itself,
  per (a)).
- **Lit-search (wrong-escape-via-citation), caught:** Brannen's circulant
  amplitude `√2 ⇔ b/a=1/√2 ⇔ r=½` is numerically identical to the target, but
  Brannen's `√2` is *imposed to match observed Koide*, not derived — adopting it
  to "fix `t`" would import the answer. The `tanh⁴(t)` form itself appears
  genuinely native (no paper derives `t` from a proper-time/Casimir mechanism).

## Honest verdict
The `tanh⁴(t)` heat-kernel structure is a **new, native, chirality-independent
*frame*** for the Koide ratio — valuable — but **not a forcing of Q=2/3**: it
relocates the single `r=½` modulus to the Casimir time `t`, no native quantity
sets `t=1.2242` (naive `g_bare=1→t=1→Q=0.558`), and the retained taste=momentum
identification makes `K_t` diagonal (`b=0`, Q=1/3) in the physical basis. The
unforeclosed thread the panel leaves: whether a **native cube normalization**
(not Koide input, not the dual position basis) can equalize the C₃ isotype
weights at a derivable `t`. No false closure; no claim that 2/3 is derived.
