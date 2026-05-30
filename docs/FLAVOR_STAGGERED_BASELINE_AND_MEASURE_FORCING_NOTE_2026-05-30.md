# Flavor — staggered baseline holds; covariant measure ranks sector (2/3) over dimension (1)

**Date:** 2026-05-30
**Claim type:** two import-free results (a baseline confirmation + a measure
ranking). Imports nothing.
**Runner:** `scripts/flavor_staggered_baseline_and_measure_forcing_2026_05_30.py`
(+ cache). Executes the two next moves from
`FLAVOR_ROUTE2_VERDICT_AND_CORRECTIONS_NOTE_2026-05-30`.

## Move A — the Q=1/3 condensate baseline survives on the chiral operator
The Route-2 press flagged that this session's three "vacuum → Q=1/3" computations
used the chiral-breaking **Wilson** operator. Re-running the coupled density-wave
gap equation on the **chiral (naive/staggered, Wilson-term-removed) operator**:
the **uniform condensate still wins** (`b=0 → Q=1/3`) on *both* the Wilson (`r=1`)
and the chiral (`r=0`) operator, for every coupling tested. (New detail: the
off-diagonal `b` *can* condense alone on the `Gu=0` branch, but loses to the
uniform channel when both compete.) **So the `Q=1/3` baseline is not a Wilson
artifact.** Consequence: the condensate **VEV is degenerate**; the value `Q=2/3`
is the fluctuation **measure**, not the VEV — exactly as the press relocated.

## Move B — the covariant measure ranks sector (2/3) over dimension (1)
The mass operator is a **concrete 3×3 matrix** on the three generations
(eigenvalues `λ₀` = singlet ×1, `λ₁` = doublet ×2). Two candidate measures:

- **(1) standard covariant action** `Tr(M²)=λ₀²+2λ₁²` — correctly counts the
  doublet **twice** (it is 2 physical generations). `e^{−Tr(M²)/2}` gives
  `⟨λ₀²⟩=1, ⟨λ₁²⟩=½`, so isotype weights `⟨singlet⟩=⟨doublet⟩=1` → **sector /
  block-count → Q=2/3**.
- **(2) dimension / Plancherel** — treats the doublet eigenvalue as **one** dof
  (drops the multiplicity) → `⟨singlet⟩:⟨doublet⟩=1:2` → **Q=1**.

**Measure (2) mis-counts:** it gives the 2-fold-degenerate doublet the *same*
variance as the singlet — treating 2 physical generations as 1 dof. The standard
covariant action on the concrete 3-dim operator (trace over all 3 states) is (1),
and it is **unitarily invariant**; the `Q=1` form `a²+b²` is basis-dependent
(it requires normalizing `{I, J−I}` to unit). **So the campaign's long-standing
"rep theory ranks neither" fork is RESOLVED — toward sector / 2/3** — once the
mass operator is treated as the concrete 3-generation matrix it physically is,
with the standard covariant measure.

## Honest gap (Move B)
This forces the **expected** isotype balance (`Q=2/3` in expectation). A single
operator fluctuates about it, so it does **not** by itself explain the observed
`Q=2/3` to ~1e-5 — that needs the mass operator to **be** the typical/max-entropy
draw, or a separate exactness mechanism. The fork is **ranked**; exactness is open.

## Net
- **A:** the `Q=1/3` condensate baseline is robust (Wilson *and* staggered) — the
  value is the measure, not the VEV. Methodological worry resolved.
- **B:** the covariant standard matrix measure `Tr(M²)`, correctly counting the
  doublet's 2-fold multiplicity, is **forced** over the dimension measure →
  **sector → Q=2/3 in expectation** — the strongest the campaign's trace-vs-sector
  fork has been ranked, and it lands on 2/3.

Remaining, cleanly isolated: the **exactness** gap (expected 2/3 vs observed
1e-5), i.e. whether the lepton mass operator is the max-entropy/typical draw from
the (now-ranked) covariant measure, or is pinned exactly by a further mechanism.
No false closure; the value is reduced to one ranked measure + an exactness
question, with every dynamical/criticality/lightness red herring removed.
