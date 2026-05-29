# Flavor — self-consistency does not force r=½; it locates 2/3 as multicritical

**Date:** 2026-05-29
**Claim type:** numerical experiment / honest negative + relocation (NOT a
derivation, NOT a promotion). Imports nothing as derived; the density-wave NJL
interaction used is a **model**, not the framework's derived action.
**Runner:** `scripts/flavor_gap_equation_competing_orders_2026_05_29.py` (+ cache).
Continuation of `FLAVOR_YUKAWA_DIAG_OFFDIAG_CONSOLIDATION_NOTE_2026-05-29.md`,
which reduced the value to `r = |b|²/a² = ½` (off-diagonal/diagonal corner
coupling).

## The test
Does the framework's vacuum **self-consistency / gap equation** force
`r = |b|²/a² → ½`? Physically: the diagonal mass `a` is the **uniform**
condensate `⟨ψ̄ψ⟩` (momentum 0); the off-diagonal corner-coupling `b` (which
splits the generations) is the **staggered** condensate at the corner-connecting
momentum `Q=(π,π,0)`. I solved the coupled density-wave mean-field gap equation
on the full Wilson-Dirac propagator on Z³ (4×4 in the `(k,k+Q)×spinor` basis)
with a single `g_bare` coupling.

## Result — the uniform condensate wins; r=0 (Q=1/3), robustly
1. **Single democratic coupling:** only the uniform condensate forms (`a≠0,
   b=0`) at every coupling above threshold → `r=0` → **Q=1/3 (degenerate)**.
   The generation-splitting condensate does not turn on.
2. **Enhancing the staggered coupling** (`Gs/Gu` up to 4): `b` stays 0 — once
   the uniform condensate gaps the spectrum it suppresses the staggered channel.
3. **Pure-staggered branch** (`Gu=0`): no condensation (the off-diagonal tadpole
   largely cancels over the BZ). So uniform and staggered are **competing
   orders**: generically one wins (here uniform → r=0), they do not coexist.

## What this means — 2/3 is a multicritical (coexistence) condition
`Q=2/3 ⟺ r=½ ⟺ b/a = 1/√2` requires **both** condensates on, in a fixed ratio —
a **uniform-staggered coexistence / multicritical point**. The generic
mean-field dynamics does **not** select it; it picks the uniform-only vacuum
(Q=1/3). So:

- **Self-consistency does not force r=½.** At mean-field it forces `r=0`
  (Q=1/3, degenerate) — the same democratic default as the free+Wilson operator
  and the generic Jahn-Teller outcome.
- The value **Q=2/3 is located precisely**: it is the condition that the vacuum
  sit at a **uniform-staggered condensate coexistence** with `b/a=1/√2`. Not a
  generic vacuum — a multicritical one.

## Honest scope and the next path (wall located, not broken)
Two caveats keep this from being a final no-go:
1. **Mean-field.** Beyond-mean-field fluctuations can shift competing-order
   phase boundaries into genuine coexistence windows.
2. **Model interaction.** The density-wave contact interaction is a *model*, not
   the framework's **derived action** (the long-standing "bridge gap"). The true
   action's channel structure could favor coexistence.

The forward question is therefore concrete and not foreclosed: **does the true
(`g_bare=1`, bridge-gap) action — or an enhanced symmetry at the
uniform-staggered coexistence point — select `b/a = 1/√2`?** Multicritical
points are frequently symmetry-selected (enhanced symmetry, special RG fixed
point), so this is a live, sharp target, not a dead end.

## Status
Honest negative + relocation. The chain now reads: "flat direction / exhausted"
(retracted) → nonperturbative vacuum output → native Jahn-Teller instability →
value = off-diagonal/diagonal ratio `r=½` → **`r=½` is a uniform-staggered
condensate coexistence (multicritical) condition that generic self-consistency
does not select.** The target is maximally sharp (one multicritical condition)
and the open question (does the true action / a coexistence symmetry select it)
is concrete. No false closure; no claim that 2/3 is derived.
