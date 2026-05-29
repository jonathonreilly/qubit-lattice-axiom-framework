# Koide F1-Selection — 14-Lens Panel Findings (the U(1)_b wall)

**Date:** 2026-05-28
**Claim type:** panel-exploration findings + one bounded correction.
NOT a closure. Imports no axiom, comparator, or convention; promotes no
row; sets no retained status. Local-branch working note for audit triage.
**Scope:** attack the F1-selection residual of
`KOIDE_Q23_BLOCK_WEIGHT_HARDENING_BOUNDED_NOTE_2026-05-28.md` — why the
charged-lepton packet sits at equal-block weight (`|b|²/a²=1/2`, Q=2/3 =
F1) rather than dimension-weighted (Q=1 = F3) or state-uniform (Q=1/3).
**Runner:** `scripts/koide_f1_selection_panel_findings_2026_05_28.py`;
cache `logs/runner-cache/koide_f1_selection_panel_findings_2026_05_28.txt`.

> **PARTIAL CORRECTION (2026-05-28, same day):** Findings 2, 3, 4 stand. The
> "single named wall" of Finding 1 — phrased here as the `U(1)_b` *angular*
> quotient on the doublet — was subsequently shown MIS-LOCATED by the
> 6-mechanism wall-attack: `θ = arg(b)` is exactly Q-orthogonal, so no phase
> quotient can fix `|b|²/a²`. The wall is RADIAL (real-dimension 2→1 /
> `det^{1/dim}`), not angular. See
> `KOIDE_U1B_WALL_RADIAL_RELOCATION_FINDINGS_2026-05-28.md`.

## Panel
10 physics lenses (representation theory, Jaynes MaxEnt, qubit/trine-POVM,
lattice path-integral measure, equipartition theorem, Kähler/Bargmann,
modular/KMS Tomita–Takesaki, RMT/Dyson, zeta-determinant, Cl(3) intrinsic)
+ 4 meta-exercises (assumptions audit, Elon first-principles, literature
disambiguator, d=3 math-rigor). All ran in parallel, framed as "find the
derivation," with a disambiguation stage on any claimed escape.

## Result: NO escape (14/14 reachesF1 = false)
No import-free, non-circular derivation of F1 exists in the panel. The
clean lenses (rep theory, lattice, equipartition, RMT, zeta, Cl(3),
modular) reach F1 only by an explicit import; the others (MaxEnt, QI,
Kähler, Elon, lit, math-rigor) flagged the F1-reaching route as smuggling
the 1/2 ratio.

## Finding 1 (sharpest obstruction, unanimous) — the U(1)_b wall
**Every canonical measure A1+A2+retained supplies counts the C_3 doublet
isotype by its real dimension (2), forcing F3 = (1,2) → Q=1.** Verified
mechanically across structures (runner §A): equipartition `kT/2 · 2 dofs`,
Plancherel `dim²/|G|`, Gaussian/Haar det, Dyson real-dim-per-mode,
Bargmann one-quantum, central trace — all give `(1/3, 2/3)`. Schur's
lemma fixes the invariant form on each simple block only up to an
independent positive scalar; nothing rep-theory-internal cross-normalizes
them, and modular/KMS theory is provably blind (the datum lives in the
`σ_t`-fixed center of the type-I algebra `R⊕C`).

The single missing ingredient is identical across all lenses: a **derived
`U(1)_b` / `SO(2)` angular quotient on the doublet `(Re b, Im b)` plane**
that collapses its two real dofs to one radial dof `|b|` BEFORE the
measure is applied (runner §C). Retained K/CPT supplies only the discrete
`Z_2` (`χ_ω ↔ χ_ω̄`); the continuous `U(1)_b` phase quotient is unprovided.
This unifies the scattered `KOIDE_*_OBSTRUCTION` corpus
(`KOIDE_MRU_WEIGHT_CLASS_OBSTRUCTION`,
`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS`,
`BAE_F1_F3_CANONICAL_SELECTION_BOUNDED_OBSTRUCTION_2026-05-17`,
`KOIDE_A1_PROBE_RETAINED_U1_HUNT_*`) into ONE wall.

## Finding 2 (bounded CORRECTION) — F1-vs-F3 is NOT a unit convention
Nine lenses initially read F1-vs-F3 as an audit-decidable measure
convention (counting-on-blocks vs dimension/Plancherel, of the
meter/GeV/radian class). **The assumptions-audit lens dissents and is
correct.** A legitimate unit/measure convention must leave every
dimensionless predicted-vs-measured ratio invariant — that is exactly the
admissibility criterion that licensed the radian and meter
reclassifications. F1↔F3 **moves the dimensionless, directly-measured
Koide ratio Q from 2/3 to 1** (runner §B, a 50% shift; PDG `Q=0.6667`
sits at F1). A choice that moves a dimensionless observable against data
cannot be a unit convention by the framework's own criterion. **Therefore
F1-selection must NOT be filed as audit-decidable convention; it is a
genuine, still-open physics measure-selection gap.** (Sharpens the
convention-adoption precedent: reclassification is admissible only when
it leaves dimensionless observables invariant.)

## Finding 3 (most promising route) — Jaynes MaxEnt, one residual step
Jaynes' transformation-group prior under retained `C_3`, sharpened by
operational distinguishability, genuinely **derives that the correct
macrostate variable is the 2-valued Frobenius–Schur block label** — the
only `C_3`-invariant observables are the circulant Hermitians
`H=aI+bC+b̄C²`, and no `C_3`-invariant observable separates the two real
dimensions inside the doublet (paired by the retained grade-2 `J`). This
defeats the state-uniform `Q=1/3` route and is fully A1+A2+retained-
derivable. Residual: MaxEnt on a partition is reparametrization-invariant,
so it cannot adjudicate **cell-counting (per distinguishable block → F1)
vs Haar-volume-counting (doublet = 2 real-dim → F3)** — the same `U(1)_b`
wall as Finding 1.

## Finding 4 (bankable) — d=3 transversal rigidity
`Δ(d)=(d−3)/2d` is a simple transversal zero only at `d=3` (slope 1/6):
equipartition value `2/d` equals range-midpoint `(1+d)/2d` uniquely at
`d=3`. Forces exactly three Koide-coherent generations and falsifies a
`Q=2/3` fourth charged lepton (`d=4` needs `Q_equi=1/2` but `Q_mid=5/8`).
This is a **consistency filter over `d`, NOT the selection law over the
ratio at fixed `d`** — file as rigidity/three-generation predictor with
F1-selection retained as a single named admission, not promoted.

## Next steps (both A1+A2-internal, neither an import)
1. **Attack the `U(1)_b` continuous quotient directly** — the unique named
   wall. Test whether the retained grade-2 `J` (which makes the doublet a
   genuine `C¹`) carries a canonical Kähler/coherent-state half-density on
   the `b`-dynamics that legitimately moves the path-integral measure from
   `(1,2)` to `(1,1)`. Verify the `1/N` mode-count flag in
   `CL3_GAMMA_INVOLUTION_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-10`
   against current main before treating the wall as closed.
2. **Retained `Z³` scalar potential** whose classical minimum lands at
   `r=|b|²/a²=1/2` — the only route that selects `r` dynamically rather
   than by measure choice. Currently an honest gap (`m_V ≈ −0.433` vs cone
   point `m_* ≈ −1.161`); flag that potential-engineering to hit `r=1/2`
   is F1-fitting unless the potential form is independently A1+A2-derived.

## Status
Bounded obstruction, promotion routes OPEN. No closure. The crux is
sharply localized to the `U(1)_b` doublet-plane quotient.
