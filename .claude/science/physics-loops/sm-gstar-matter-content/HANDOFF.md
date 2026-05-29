# HANDOFF — SM g_* matter-content derivation

## What this block delivered

A bounded_theorem derivation note + verification runner that retires the
**monolithic external** status of the declared SM relativistic inventory
(`sm_relativistic_dof_count_import_note_2026-05-17`) by sourcing each dof count
of the high-T unbroken-phase g_* = 106.75 census from framework structure, with
an explicit Derived-vs-residual table and the counterfactual-pass record.

- Note: `docs/SM_GSTAR_FROM_FRAMEWORK_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-05-29.md`
- Runner: `scripts/frontier_sm_gstar_from_framework_structure_2026_05_29.py`
- Trace: `direct_blocker_closure` / `partially_closes` on the
  "no framework derivation of the inventory" blocker.
- Claim type: `bounded_theorem`. Independent audit owns the verdict.

## Residual retirements queued (legitimate import -> bounded -> retire path)

Each named residual is a framework-derivation target, NOT an external SM
import. Queue these as follow-on loop blocks / PRs:

1. **R-U1Y — U(1)_Y hypercharge gauge sector existence.** The native gauge
   closure note explicitly EXCLUDES the abelian surface; the hypercharge
   uniqueness note (`standard_model_hypercharge_uniqueness_theorem_note_2026-04-24`)
   is unaudited. Target: audit-ratify the abelian-surface existence as a
   positive theorem (it currently lives as the bounded abelian eigenvalue
   surface in `NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md`).

2. **R-POL — massless-vector 2-polarization.** Audit the
   `massless_vector_polarization_count_..._note_2026-05-28` (unaudited) as a
   bounded narrow identity, AND retire its admitted Lorentzian-signature
   context (AC1) once emergent-Lorentz lands (currently under repair; cf. the
   l=4 cubic-harmonic coefficient fix 2026-05-29). Until emergent-Lorentz is
   ratified, the 2-pol count stays bounded over admitted signature.

3. **R-HIGGS — single complex Higgs doublet minimality.** HARD OPEN. The repo
   has only specific two-Higgs DM-slot no-gos, not a general single-doublet
   minimality theorem. Target: a framework derivation that the thermal scalar
   sector is exactly one complex SU(2) doublet (4 real scalar dof). This is the
   highest-blast-radius unattempted residual.

4. **R-MATTER — one-generation matter completion as a full theorem.** The
   `one_generation_matter_closure_note` is unaudited and conditional on the
   neutral-singlet branch convention (`Y(nu_R)=0`) — an `e_R <-> nu_R`
   relabelling ambiguity not derived from framework primitives. Target: derive
   the neutral-singlet branch selection from framework structure (or ratify the
   bounded conditional completion).

5. **R-FSB — full fermionic Stefan-Boltzmann derivation.** The 7/8 *ratio* is
   retained (`hierarchy_seven_eighths`); the substrate fermionic-SB note
   (`axiom_first_fermionic_stefan_boltzmann_..._note_2026-05-26`) is unaudited.
   Target: audit-ratify the substrate fermionic-SB law.

6. **R-SPIN — per-site spin-1/2 carrier.** `per_site_su2_spin_half_theorem_note_2026-05-02`
   is audited_conditional. Target: retire its conditional dependency.

7. **I12 — RH-neutrino thermal exclusion / neutrino sector.** The single most
   load-bearing fermionic choice. The framework anomaly content includes
   `nu_R: (1,1)_0` (gauge singlet), but its thermal exclusion at the
   leptogenesis T is a premise. If nu_R were thermalized Dirac, g_* = 112 not
   106.75. Target: a framework statement of the neutrino sector (Dirac vs
   Majorana, nu_R thermal coupling) at the leptogenesis scale.

## Proposed repo-wide weaving (for later review, NOT done in this science run)

- Once this note audits, the downstream cosmology rows
  (`dm_leptogenesis_equilibrium_conversion_theorem_note_2026-04-16`,
  `omega_lambda_derivation_note`,
  `g_star_sm_content_at_leptogenesis_..._note_2026-05-28`) could cite this
  framework-assembly note alongside the import note, narrowing their "declared
  SM census" dependency to a framework-internal assembly with named residuals.
- The existing `..._FROM_SUPPLIED_THERMAL_INVENTORY_...note_2026-05-28` could
  cross-reference this note for the inventory-sourcing of its premise P1.

These weavings are recorded here for the later review/integration process; they
are NOT applied to repo-wide authority surfaces in this science run.

## Next exact action

Run the review-loop self-review; record disposition in REVIEW_HISTORY.md;
commit; push branch; `gh pr create`; verify with `gh pr view`. Confirm
`git status` shows no `docs/audit/` files staged.
