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

## Cycle 2 (2026-05-29): R-HIGGS attacked on the g_* census count

Branch: `physics-loop/sm-gstar-higgs-sector-count-stretch-2026-05-29`.

R-HIGGS (item 3 above, flagged "HARD OPEN ... highest-blast-radius
unattempted residual") was attacked **for the census count specifically** via
an EWSB-Higgs vs flavor-sector-Higgs reconciliation. Deliverables:

- Note: `docs/SM_GSTAR_HIGGS_SECTOR_COUNT_STRETCH_NOTE_2026-05-29.md`
  (bounded_theorem).
- Runner: `scripts/frontier_sm_gstar_higgs_sector_count_2026_05_29.py`
  (`PASS=51 FAIL=0`).

**Outcome (a):** the EWSB scalar entering the census and the flavor-sector
"two-Higgs" are **DIFFERENT** objects. The framework-native EWSB scalar is
**one** composite `SU(2)_L` doublet `H_unit` (4 dof), the unique `(1,1)` scalar
composite on `Q_L` (D9/D16/D17, sourced from the **retained_bounded** Ward
theorem; one-doublet EW bookkeeping **retained**). The **retained** charged-
lepton two-Higgs canonical reduction governs **Yukawa textures** (two distinct
effective `Z_3` offsets making `Y` non-monomial; an exact 7-real-parameter
class), realized **within the one-doublet field content** via `H`/`tilde H` and
the gauge-redundant `Z_3` charge `q_H`; it adds **no** thermalized dof. A
genuine two-thermalized-doublet 2HDM needs an **independent** scalar (admitted
extension, not retained). Therefore **`g_* = 106.75` stands** (`110.75` only
under an admitted second-doublet import).

**R-HIGGS census-count content: partially_closes.** The single-EWSB-doublet
count for the census is no longer a bare assumption — it is sourced from
retained / retained_bounded structure. The **flavor-sector textures** (7
quantities) remain the separate open object, and R-POL/R-U1Y/R-MATTER/R-FSB/
R-SPIN and imports I11/I12 are unchanged. So R-HIGGS shrinks from "single
doublet assumed" to "framework-native single EWSB doublet; flavor textures
open"; it is NOT fully retired.

Residual still open after cycle 2 (queue): a framework derivation of the
flavor-sector Yukawa textures (the 7 quantities of the canonical two-Higgs
class), and the unchanged R-POL/R-U1Y/R-MATTER/R-FSB/R-SPIN/I12 items above.

## Parallel cycle (2026-05-29): R-FSB + R-U1Y retired-to-retained-sourced (PR #2225)

Branch `physics-loop/sm-gstar-retire-fsb-u1y-residuals-2026-05-29` (ran in
parallel off main, not stacked on cycle 2). Deliverables:
`docs/SM_GSTAR_RESIDUAL_RETIREMENT_FSB_U1Y_BOUNDED_NOTE_2026-05-29.md` +
`scripts/frontier_sm_gstar_residual_retirement_fsb_u1y_2026_05_29.py`.

- **R-FSB** retired-to-retained-sourced: the census consumes only the
  dimensionless `7/8` ratio (retained `hierarchy_seven_eighths`;
  `R_lat(3) = 7/8`, `eta(4)/zeta(4) = 7/8`), NOT the full substrate fermionic-SB
  law (unaudited, separately blocked on the Wightman chain).
- **R-U1Y** retired-to-retained-sourced: the census consumes only the
  one-abelian-factor RANK (the `gl(1)` of the retained `gl(3)+gl(1)` commutant
  from `native_gauge_closure` / `graph_first_su3_integration`), giving one
  massless vector. The hypercharge VALUES stay bounded/unaudited and are NOT a
  dof-count input. The `2`-polarization factor stays R-POL.

## Cycle 3 (2026-05-29): R-MATTER partially reduced on the g_* census count

Branch `physics-loop/sm-gstar-retire-r-matter-residual-2026-05-29`. Attacked the
per-generation thermalized fermion dof count (the `30 = 15 gauge-charged Weyl *
2` that enters the high-T g_* census). Deliverables:

- Note: `docs/SM_GSTAR_R_MATTER_RESIDUAL_REDUCTION_BOUNDED_NOTE_2026-05-29.md`
  (bounded_theorem).
- Runner: `scripts/frontier_sm_gstar_r_matter_reduction_2026_05_29.py`
  (`PASS=89 FAIL=0`).

**Outcome.** The thermalized per-generation count `30 = 15 (gauge-charged Weyl)
* 2 (particle/antiparticle)` has all its **multiplicities** re-sourced to
retained / decoration-under-retained authorities:

- color triplet `3` + `N_c = 3`: **retained** `graph_first_su3_integration` /
  `cl3_color_automorphism`;
- isospin doublet `2`: **retained** `native_gauge_closure`;
- LH per-rep assignment `(2,3) = Q_L:6`, `(2,1) = L_L:2`:
  **decoration_under_graph_first_su3_integration_note** `lhcm_matter_assignment`
  + `left_handed_charge_matching`;
- RH gauge-charged completion `u_R:3, d_R:3, e_R:1`: **retained_bounded**
  `one_generation_anomaly_singlet_completion`;
- generation count `3`: **retained** `three_generation_observable`;
- cardinality `2`: **retained** `spin_statistics_cardinality`.

Per-rep breakdown: `Q_L 3*2=6, u_R 3, d_R 3, L_L 2, e_R 1 = 15` gauge-charged
Weyl; `* 2 = 30` dof/gen; `* 3 gens = 90`; `g_* = 28 + (7/8)*90 = 106.75`.

**R-MATTER partially_reduced (NOT retired).** The framework matter content is
**16 Weyl** including the gauge-singlet `nu_R : (1,1)_0`; the thermalized count
excludes `nu_R` (no gauge charge -> need not thermalize). The genuine residual
sharpens to:

1. **I12** — the `nu_R` thermal-exclusion fork (the load-bearing residual):
   `30/gen -> g_* = 106.75` (excluded) vs `32/gen -> g_* = 112` (thermalized
   Dirac). Not derived; an admitted sector import. **Carried explicitly; not
   retired.**
2. **R-SPIN** — the per-site spin-`1/2` carrier (audited_conditional) that
   identifies the matter as spin-`1/2` Weyl. The cardinality `2` is retained;
   the spin-`1/2` carrier stays a residual.
3. **The neutral-singlet branch convention** (`Y(nu_R) = 0`, the `e_R <-> nu_R`
   relabelling) — a convention selecting the SM labelling, NOT load-bearing on
   the thermalized count (both branches give the same `(1,1)` singlet
   multiplicities), but it stays a named residual of the full matter closure.

The full `16`-Weyl one-generation closure (`one_generation_matter_closure_note`,
unaudited) stays a separate, stronger, unaudited target that the thermalized
count does not consume.

## Remaining g_* campaign residuals after cycle 3

- **R-POL** — massless-vector 2-polarization (gated on the emergent-Lorentz
  repair currently in flight; cf. the l=4 cubic-harmonic coefficient fix
  2026-05-29). Until emergent-Lorentz lands, the 2-pol count stays bounded over
  admitted Lorentzian signature.
- **R-SPIN** — per-site spin-`1/2` carrier (audited_conditional). Target: retire
  its conditional dependency.
- **Neutral-singlet branch convention** — the `Y(nu_R) = 0` labelling. Target:
  a framework derivation of the branch selection, or ratify the bounded
  conditional completion (not load-bearing on the g_* count).
- **I11** — high-T thermal regime (honest import).
- **I12** — `nu_R` thermal exclusion (honest import; the `106.75` vs `112`
  fork). Target: a framework statement of the neutrino sector (Dirac vs
  Majorana, `nu_R` thermal coupling) at the census scale.

Already addressed for the dof count: **R-FSB** + **R-U1Y** retired-to-retained-
sourced (PR #2225); **R-HIGGS** census-count single-EWSB-doublet sourced (PR
#2226; flavor textures open); **R-MATTER** thermalized-count multiplicities
retained / decoration-under-retained-sourced (this cycle).

## Next exact action

Run the review-loop self-review; record disposition in REVIEW_HISTORY.md;
commit; push branch; `gh pr create`; verify with `gh pr view`. Confirm
`git status` shows no `docs/audit/` files staged.
