# Local-Frame Orbit Flat-Sector Converse and Holonomy Residual Bounded Theorem

**Date:** 2026-06-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope note:** conditional theorem on the supplied `C^3` carrier, the named
nearest-neighbor hopping, the local `SU(3)` frame action, and the named
record-instrument probes. It shows that the local-frame orbit of the free
hopping is exactly the flat link sector on the tested three-site cycle, that
holonomy is invariant under that frame action and record-separated by a tested
generic-flux probe, and that fixed-driver pointer-frame selection is not
dissolved by joint co-rotation.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_local_frame_orbit_flat_sector_converse_holonomy_residual_2026_06_10.py`](../scripts/frontier_local_frame_orbit_flat_sector_converse_holonomy_residual_2026_06_10.py)
(expected `TOTAL: PASS=18 FAIL=0`; deterministic exact linear algebra/numerics,
no Monte Carlo).

## Result

The runner establishes four scoped facts.

1. **Local fusion.** For the named hopping and record-instrument probes, record
   content is invariant under the simultaneous local action on state, local
   frames, and links. The underlying operator covariance identity is the
   identity from
   [`MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md`](MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md);
   this runner recomputes it at Fock level for general links and for the
   free-link case. The uncompensated free hopping still changes at order one
   under local frames, so this is not a vacuous identity.
2. **Orbit-converse.** Every trivial-holonomy link field on the tested
   three-site cycle is pure-gauge form by explicit construction:
   `g_0 = I`, `g_1 = W_01^dagger`, `g_2 = (W_01 W_12)^dagger`. Therefore
   `H[flat W] = Gamma(g) H_free Gamma(g)^dagger`, and the local-frame orbit
   of the free hopping is exactly the flat sector for this surface.
3. **Holonomy residual.** The holonomy conjugacy class is invariant under the
   local action, so nontrivial holonomy is frame-unreachable. A generic
   `SU(3)` flux is record-separated from the flat sector by the tested
   color-blind singlet probe, while every flat field gives the free value on
   that probe. This proves existence of a frame-unreachable record residual;
   it does not claim that holonomy is the complete gauge content.
4. **Fixed-driver selection residual.** With the dephasing driver fixed,
   changing the frame changes the dephasing outcome at order one, while joint
   co-rotation remains exactly covariant. The theorem therefore removes only
   the kinematic absolute-frame redundancy. It does not derive which
   pointer-frame dynamics selects.

## Inputs and Boundary

| Input | Role | Boundary |
|---|---|---|
| [`MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md`](MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md) | covariance identity and transporter context | cited context; the runner recomputes the identity on this finite Fock surface |
| [`FOUR_HATS_FRAME_CONNECTION_GENERATOR_STRATIFICATION_NON_REDUCTION_NARROW_THEOREM_NOTE_2026-06-09.md`](FOUR_HATS_FRAME_CONNECTION_GENERATOR_STRATIFICATION_NON_REDUCTION_NARROW_THEOREM_NOTE_2026-06-09.md) | pointer-frame stratification context | not promoted; used only to state what this theorem does not dissolve |
| [`BLOCKING_ISOMETRY_REDUCES_TO_POINTER_FRAME_ADMISSION_NARROW_THEOREM_NOTE_2026-06-09.md`](BLOCKING_ISOMETRY_REDUCES_TO_POINTER_FRAME_ADMISSION_NARROW_THEOREM_NOTE_2026-06-09.md) | pointer-frame selection context | not promoted; fixed-driver selection remains open here |
| [`COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09.md`](COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09.md) | unitary-primitivity fork context | not consumed as a closed selector |
| Standard finite-dimensional linear algebra | orbit construction, conjugacy invariance, Fock lift checks | all used facts are recomputed by the runner |

This note adds no framework premise, measure, weighting rule, gauge dynamics,
probability law, pointer-frame selector, empirical input, or completeness
claim. It is conditional on the named carrier, hopping, link class, frame
action, and instrument/probe class.

## No-Go Discipline Gate

**N1 -- Alternative routes tested.** Joint co-rotation is tested and removes
only absolute-frame kinematics. Uncompensated local frames are tested and still
change the free hopping at order one. The flat-sector converse is tested by
explicit pure-gauge reconstruction. Nontrivial holonomy is tested as
frame-unreachable by conjugacy invariance. Fixed-driver dephasing is tested and
still depends on the chosen frame.

**N2 -- Wall independence.** The flat-sector orbit theorem, the nontrivial
holonomy residual, and the fixed-driver pointer-frame selection residual are
independent. Closing one does not close the others.

**N3 -- Hidden-wall scan.** The carrier, hopping, frame action, and probes are
declared inputs. The note does not import dynamics, probability, measure, or a
selector.

**N4 -- Residual matching.** The residual proved here is kinematic
frame-redundancy versus holonomy. The pointer-frame selector residual is only
exhibited as not dissolved by joint co-rotation.

**N5 -- Rhetoric audit.** "Frame-unreachable" means unreachable under the
local-frame action tested here. "Record-separated" means separated by the
specific tested singlet probe. No statement is made about all observables or
all gauge content.

**N6 -- Partial-closure path scan.** Future work could still derive a
pointer-frame dynamics or a holonomy dynamics/action. This theorem does not
close either path.

**N7 -- Steelman.** A hostile reviewer could object that one probe does not
prove a complete record theory of holonomy. Correct: the theorem claims only
existence of a record separation for a generic flux on this finite surface.

**N8 -- Cross-cycle echo.** Prior local-orientation and pointer-frame notes
separate kinematic quotient claims from dynamics-selection claims. This note
keeps that separation rather than merging the residuals.

## Reproduction

```bash
python3 scripts/frontier_local_frame_orbit_flat_sector_converse_holonomy_residual_2026_06_10.py
```

Expected scorecard: `TOTAL: PASS=18 FAIL=0`. A passing run supports only the
finite-surface local fusion, flat-sector converse, holonomy residual existence,
and fixed-driver selection non-dissolution described above.
