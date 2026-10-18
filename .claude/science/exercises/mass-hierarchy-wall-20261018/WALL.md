# The fermion mass hierarchy wall (exercise, 2026-10-18)

## Plain version

The quarks and leptons come in three generations. Their masses span about a million to one, from the electron (0.5 MeV) to the top quark (173 GeV). The generations also mix in a hierarchical pattern (CKM).

We want the grid's rules to produce these ratios rather than having them put in by hand.

What keeps happening:
- **The ladder only carries the small number.** Zooming out from the grid passes a breaking strength along unchanged, but nothing in the ladder sets its size.
- **A single symmetry breaking gives too few levels.** It produces masses at only two orders, which is not enough for three generations.
- **The grid treats every particle type alike.** Up quarks, down quarks and leptons get the same pattern, and quark mixing comes out trivial.
- **Free integer powers prove nothing.** If the powers are chosen freely, they fit any spectrum, including random ones.

Getting past the wall means either the observed pattern (all 9 charged masses within ×3, plus the CKM hierarchy) from structure the axioms fix, or a proof of exactly which extra numbers are unavoidable.

## Precise version

**Targets.**
- The 9 charged-fermion masses, ratios spanning 1e-6 to 1, all within ×3.
- The CKM hierarchy: |V_us| ≈ 0.22, |V_cb| ≈ 0.04, |V_ub| ≈ 0.004.

**Evidence.**
- **HIER-2** (packet `.claude/science/exercises/hierarchy-scale-ladder-20261018/` on branch `claude/hierarchy-scale-ladder-20261018`, PR #9783; same-family referee). Reading OPEN.
  - Proved: ε is not a ladder ratio in period-2 Bloch breaking, and the exponents are sector-blind.
  - Checked numerically: one symmetry-fixed period-2 spurion gives Dirac gaps only at orders {1, 3}.
  - Not excluded: dilute or longer-period breaking (ε = ε₀(a/L)³, with the rung assignment supplied), two amplitudes, and interaction-driven masses.
- **Generation placement** (chirality branch `claude/chirality-grid-exercise-20261014`, PR #9693).
  - GEN-1: X2′, generations as an internal label at Γ, puts the "3" in by hand.
  - GEN-2: generations as orientations force an Eg strain order.
  - Corner generations conflict with CKM (OBS-4, CLS-1).

**Prior art on main.**
- CHARGED_LEPTON_MASS_HIERARCHY_*, YT_GENERATION_HIERARCHY_PRIMITIVE_ANALYSIS_NOTE, CKM_FROM_MASS_HIERARCHY_NOTE.
- Koide notes, and GST textures.

**Route R5 (added at Jon's prompt).** Read the scale ladder as lossy compression. A rung is a quantum channel. In a code, a protected mode's mass arises from error leakage of order ε^d, where d is the code distance. Do the code distances of generation-protecting codes give framework-fixed integer exponents?
