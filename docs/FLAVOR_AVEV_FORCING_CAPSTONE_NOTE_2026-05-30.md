# Flavor — bridge-gap capstone: a_VEV=0 (exact Q=2/3) reduces to the one chiral input

**Date:** 2026-05-30
**Claim type:** bridge-gap attack capstone (move 6) / rigorous reduction. Imports
nothing; identifies precisely what input is required.
**Runner:** `scripts/flavor_avev_forcing_capstone_2026_05_30.py` (+ cache).

## The question
Moves 1–5 left one open quantitative piece: is the uniform generation-mass
component `a_VEV ≈ 0` (which puts the charged leptons exactly at the block-count
point `Q=2/3`) **forced**, or only consistent? Concretely: does any symmetry
forbid the uniform generation mass `a·I`?

## Result — not native; needs the chiral input
**Native symmetries ALLOW the uniform mass** (so `a_VEV` is not forced to 0):
- **S₃** (axis permutations): `a·I` is S₃-invariant → allowed.
- **Native reflections** (CPT / charge-conjugation): generation-blind (`~ ±I` on
  the generation space) → commute with `a·I` → allowed.
- **Generic dynamics:** the uniform condensate *wins* (this session, 3
  computations) → `a_VEV ≠ 0` → `Q=1/3` (degenerate). The generic vacuum is *not*
  at the block-count point.

**Only the chiral grading forbids it.** `Γ_χ=(2/3)J−I` has `Tr(Γ_χ)=−1`, so
`{M,Γ_χ}=0 ⟹ Tr(M Γ_χ)=0 ⟹ a=0` — the chiral anticommutation forces the uniform
mass to vanish (the retained `koide_anticommuting_operator` route → Q=2/3). But
`Γ_χ` is non-circulant on the C₃ orbit → **not native** (the retained_bounded
no-go `koide_z3_equivariant_anticommuting_no_go`) → the single user-approval
import. Equivalently, the **chiral-critical point** (condensate → 0) gives
`a_VEV → 0` dynamically.

## What this settles
The charged-lepton Koide **value** reduces, cleanly and rigorously, to the **one
chiral input** — exactly the central gate the campaign identified. The new,
genuine contribution of this session's bridge-gap attack:

- the off-diagonal coupling `b` is **native** (double-shift, moves 1);
- `Q=2/3 ⟺ b/a=1/√2`, import-free, RP-bounded (move 2);
- the covariant matrix-field measure **ranks block-count (2/3) over dimension (1)**
  — the first native tie-breaker (move 3);
- the fermion loop **preserves** block-count → 2/3 is the **import-free EXPECTED
  value**, RG-stable (move 4);
- so the chiral input's role is **reduced** from "explains 2/3" to "**promotes the
  expected 2/3 to exact** / selects `a_VEV=0`."

The cross-sector overreach (quarks) was caught and retracted (move 5); the result
is lepton-specific.

## Live forward path (not a closure)
There are **two** ways to force `a_VEV=0`, and they are not the same:
1. the **operator-level** chiral grading `Γ_χ` (non-native, the import);
2. **dynamical selection of the chiral-critical point** (condensate → 0).

Route 2 is a genuine, untested alternative: the charged leptons are **light**
(small mass) — plausibly *near* the chiral-critical point. **If the framework's
vacuum sits at/near chiral criticality for the lepton sector, `a_VEV → 0` and
`Q → 2/3` without the operator-level import** — a dynamical-criticality route
distinct from the chiral operator. Whether the `g_bare=1` lepton sector is
dynamically near chiral criticality is the next attack. No false closure; the
value's exact forcing is pinned to a single, concrete, still-open input.
