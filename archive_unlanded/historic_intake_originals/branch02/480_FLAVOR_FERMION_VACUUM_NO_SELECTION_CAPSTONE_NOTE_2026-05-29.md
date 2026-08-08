# Flavor — the fermion vacuum does not produce 2/3; it relocates the origin

**Date:** 2026-05-29
**Claim type:** capstone synthesis / honest negative + relocation (NOT a
derivation, NOT a permanent no-go). Imports nothing as derived; the
density-wave NJL interaction is a **model**, not the framework's derived action.
**Runner:** `scripts/flavor_effpot_no_selection_2026_05_29.py` (+ cache).
Synthesizes the dynamical investigation in
`FLAVOR_FULL_OPERATOR_NONPERTURBATIVE_VALUE`,
`FLAVOR_JAHN_TELLER_CUBIC_BREAKING`,
`FLAVOR_YUKAWA_DIAG_OFFDIAG_CONSOLIDATION`,
`FLAVOR_GAP_EQUATION_COMPETING_ORDERS` (all 2026-05-29).

## The question this arc answered
"Go after the value in the full theory": does the framework's **nonperturbative
fermion-vacuum dynamics** produce the charged-lepton Koide value Q=2/3 (i.e.
`r = |b|²/a² = ½`, the off-diagonal/diagonal corner-coupling ratio)?

## Three independent computations, one answer: the vacuum gives Q=1/3
1. **Full free+Wilson operator** — corner mass = `m+2r·hw` (Hamming-weight only)
   → the three hw=1 generations are **degenerate** → Q=1/3.
2. **Coupled density-wave gap equation** (uniform `a` vs staggered `b` at
   `Q=(π,π,0)`) — only the uniform condensate forms (`b=0`) at every coupling;
   enhancing the staggered coupling 4× doesn't turn `b` on; the pure-staggered
   branch doesn't condense. Uniform and staggered are **competing orders**;
   uniform wins → r=0 → Q=1/3.
3. **Fermion effective potential** `U(a,b)` — minimized at `b=0` (pure uniform)
   for every `m` and radius; **no feature at `b/a=1/√2`**, not even an O(2) flat
   direction (the staggered direction strictly costs energy).

All three agree: the fermion vacuum **robustly prefers the uniform, unbroken
condensate** → degenerate generations → **Q=1/3, never ½ → never Q=2/3.**
(General reason: the translation-invariant scalar condensate maximizes `|det|`
— a Vafa-Witten-flavored preference for the unbroken vacuum.)

Along the way the e–μ "gap" **dissolved**: the e/μ/τ splitting is the C₃ phase
`θ`, which is exactly Q-orthogonal (the retained Brannen δ), so it contributes
nothing to the value.

## What this establishes (and what it does not)
- **Robust negative for one hypothesis:** "Q=2/3 emerges from fermion-vacuum
  dynamics" is **false at mean-field** — the fermion sector gives the democratic
  Q=1/3. This is a *definite prediction of the fermion sector*, not a flat
  direction. The optimistic "the value will appear nonperturbatively in the
  fermion determinant" reading (from the start of this arc) is **not borne out**.
- **It is NOT a permanent wall.** Two untested routes remain, and the
  computation explicitly *locates the splitting outside the fermion determinant*:
  1. the action's **explicit (bridge-gap) structure** — the framework's derived
     `g_bare=1` action is not pinned; its channel structure could carry the
     staggered order;
  2. a **non-fermionic (gauge/link) sector** — the vacuum gauge configuration
     (instanton/condensate analog) could carry the cubic/staggered breaking that
     the fermion determinant alone will not.

## Where this leaves the value
Consistent — now *from the dynamics side* — with the original campaign's
conclusion: `r=½` is **not a dynamical output of the fermion sector**; it is the
"counting-vs-dimension measure" / chiral-grading input identified earlier
(`koide_anticommuting_operator_derivation_theorem` makes the chiral
anticommutation `{H,Γ_χ}=0` *sufficient* for r=½, and
`koide_z3_equivariant_anticommuting_no_go` forbids it natively on the generation
R³). The dynamical arc adds: **even the full nonperturbative fermion vacuum does
not supply it** — so the origin must lie in the (unpinned) action structure or a
non-fermionic sector.

## Status
Capstone of the dynamical investigation. Robust mean-field negative ("the
fermion vacuum gives Q=1/3, not 2/3"), no false closure, no permanent-lock
language: the origin of the generation splitting is **relocated** to the
derived-action structure or the gauge sector — both untested here and both open.
The sharpest target is unchanged and now triangulated from both sides:
`b/a = 1/√2` (off-diagonal corner-coupling = `1/√2 ×` diagonal corner-mass),
which the fermion vacuum does not select and which therefore must come from
structure the fermion determinant does not contain.
