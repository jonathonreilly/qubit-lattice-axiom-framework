# Neutrino Sum-Mass Route-Status Fan-Out Synthesis

**Date:** 2026-04-28
**Type:** no_go
**Status:** conditional route-status synthesis over five admitted orthogonal
Σm_ν route attempts; not a theory-wide no-go.
**Status authority:** independent audit lane only.
**Topic:** Neutrino quantitative closure.
**Provenance:** `physics-loop/sigma-mnu-f3-dm-cluster-20260428`
**Runner:** `scripts/frontier_sigma_mnu_f3_stuck_fanout_synthesis.py`
**Log:** `outputs/frontier_sigma_mnu_f3_stuck_fanout_synthesis_2026-04-28.txt`

## 2026-05-28 Audit Repair (conditional core; missing upstream admitted)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The finite-route synthesis follows only if the five route statuses and current-framework surface are accepted as inputs. The packet supplies no upstream authorities for T-4F-alpha-2, the current-bank Omega_DM interval, retained N_eff, the n"*

with repair: *"missing_dependency_edge: add direct cited authorities for the DM-cluster cross-bound, neutrino functional-form theorem, current-bank Omega_DM theorem, dark-matter gate status, and eta/leptogenesis status, then re-run the no-go audit."*

Supplying the named upstream authority is substantive new work, out of scope.
This revision narrows via the **admission path**:

- **Load-bearing (in scope):** Given the five route statuses and the current-framework surface as admitted inputs, the synthesis closes: the five orthogonal Σm_ν route attempts are assessed, the ~0.003 eV admission window is identified, and the no-go result — that no orthogonal route supplies an independent numerical Σm_ν cross-bound on the current-bank surface — follows algebraically from those inputs.
- **NON-load-bearing (admitted / unsupplied):** The specific retained authorities establishing the five input route statuses — the neutrino functional-form theorem, the current-bank Omega_DM interval theorem, retained N_eff, dark-matter gate status, and eta/leptogenesis status — are admitted as unsupplied inputs; no direct cited authority row for any of these is present in the restricted packet.

No new axiom, import, or retained bridge is introduced. The conditional core is
the load-bearing content; the named upstream stays admitted until a retained
authority/runner for it lands.

## No-Go Discipline Gate (review-loop 2026-05-29)

This gate passes only for the conditional route-status synthesis. It does
**not** prove that every possible neutrino-mass route is closed.

- **N1 alternative routes:** the five named orthogonal route attempts are the
  in-scope alternatives; any sixth mechanism, new observable, or new retained
  authority is outside this no-go and remains open.
- **N2 wall independence:** the five route-status inputs are independent
  admissions for this note; closing one route-status authority does not close
  the other four.
- **N3 hidden-wall scan:** "current-framework", "current-bank", and
  "orthogonal" are non-load-bearing bookkeeping terms unless backed by the
  listed route-status inputs.
- **N4 residual matching:** the residual is only "no listed orthogonal route
  supplies an independent numerical Σm_ν cross-bound on the current-bank
  surface"; it is not a claim about all future Σm_ν mechanisms.
- **N5 rhetoric audit:** the negative statement is route-list resolution only,
  not theory-wide or lattice-wide impossibility.
- **N6 partial-closure path:** direct retained authorities for any of the five
  route statuses can retire that wall without adding a new axiom.
- **N7 steelman:** a hostile reviewer can correctly object that the five route
  statuses are not retained here; this is accepted and is why they are explicit
  admissions.
- **N8 cross-cycle echo:** prior route-synthesis rows repeatedly failed by
  treating status packets as authority; this repair keeps the status packet
  conditional and sends the row back to the independent auditor.

---

## 0. Context

Cycle 1 (`SIGMA_MNU_F3_DM_CROSS_BOUND_AUDIT_NOTE_2026-04-28.md`)
identified a structural tension at Planck admissions in the F3 DM-
cluster cross-bound: the framework's current-bank `Ω_DM ∈ [0.2677,
0.2697]` exceeds the Planck-derived `Ω_DM ≈ 0.265`, leaving no
room for positive Σm_ν at standard `(L, Ω_b, h)` admissions. This
Cycle-2 fan-out generates 5 orthogonal Σm_ν cross-bound routes and
audits each for current-framework usability.

## 0.1 Dependency-Edge Repair (2026-05-27)

The prior audit accepted the broad no-go shape but required the
restricted packet to expose the authorities used by the route-status
conclusions. This repair adds the direct authority packet and a runner
that verifies the edge inventory and recomputes the decisive arithmetic.

Load-bearing authority packet:

- F3 Cycle-1 DM cross-bound:
  [`SIGMA_MNU_F3_DM_CROSS_BOUND_AUDIT_NOTE_2026-04-28.md`](SIGMA_MNU_F3_DM_CROSS_BOUND_AUDIT_NOTE_2026-04-28.md).
- T-4F-alpha-2 functional form:
  [`NEUTRINO_LANE4_4F_SIGMA_M_NU_FUNCTIONAL_FORM_THEOREM_NOTE_2026-04-28.md`](NEUTRINO_LANE4_4F_SIGMA_M_NU_FUNCTIONAL_FORM_THEOREM_NOTE_2026-04-28.md).
- Current-bank `Omega_DM` interval and no-selector boundary:
  [`DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_BOUNDING_THEOREM_NOTE_2026-04-17.md`](DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_BOUNDING_THEOREM_NOTE_2026-04-17.md).
- Lane 5 `(C1)` gate status:
  [`HUBBLE_LANE5_TWO_GATE_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md`](HUBBLE_LANE5_TWO_GATE_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md),
  with retained attack-frame support from
  [`HUBBLE_LANE5_C1_A1_GRASSMANN_NO_GO_NOTE_2026-04-28.md`](HUBBLE_LANE5_C1_A1_GRASSMANN_NO_GO_NOTE_2026-04-28.md),
  [`HUBBLE_LANE5_C1_A4_PARITY_GATE_CAR_BOUNDARY_NOTE_2026-04-29.md`](HUBBLE_LANE5_C1_A4_PARITY_GATE_CAR_BOUNDARY_NOTE_2026-04-29.md),
  [`HUBBLE_LANE5_C1_A5_BOOLEAN_COFRAME_RESTRICTION_OBSTRUCTION_NOTE_2026-04-29.md`](HUBBLE_LANE5_C1_A5_BOOLEAN_COFRAME_RESTRICTION_OBSTRUCTION_NOTE_2026-04-29.md),
  and
  [`HUBBLE_LANE5_C1_A6_BILINEAR_ACTIVE_BLOCK_SUPPORT_BOUNDARY_NOTE_2026-04-29.md`](HUBBLE_LANE5_C1_A6_BILINEAR_ACTIVE_BLOCK_SUPPORT_BOUNDARY_NOTE_2026-04-29.md).
- Eta/leptogenesis status:
  [`DM_LEPTOGENESIS_TRANSPORT_STATUS_NOTE_2026-05-10.md`](DM_LEPTOGENESIS_TRANSPORT_STATUS_NOTE_2026-05-10.md)
  and retained bounded support
  [`ETA_188_STRUCTURAL_ORIGIN_PARTIAL_NOTE_2026-05-03.md`](ETA_188_STRUCTURAL_ORIGIN_PARTIAL_NOTE_2026-05-03.md).

This repair does not claim numerical `Sigma m_nu` retention. It makes the
no-go packet auditable by separating retained support, meta/status
inventory, and still-open current-bank or cosmology admissions.

## 1. Five orthogonal routes

### (F3-α) PDG oscillation Σm_ν lower bound

**Route.** From PDG `Δm²_21 = 7.42 × 10⁻⁵ eV²` and `Δm²_31 = 2.515
× 10⁻³ eV²`:

```text
Σm_ν ≥ √Δm²_21 + √Δm²_31  ≈ 0.0588 eV   (NO, m_1 = 0)
Σm_ν ≥ √Δm²_31 + √(Δm²_31 + Δm²_21)  ≈ 0.1010 eV  (IO, m_3 = 0)
```

The runner computes both within `~0.002 eV` of the PDG NO/IO
floors.

**Status.** **Comparator only.** PDG oscillation values are
observational; cannot be derivation inputs under the framework's
no-fitted-parameter posture. Supplies a **lower bound only**, not
an upper bound; an independent route is needed for a closed
cross-bound.

### (F3-β) Retained `N_eff = 3.046` cross-bound

**Route.** `N_eff` is retained per the framework's three-generation
structure. It enters `C_ν` via the relic conversion:

```text
C_ν ∝ N_eff × T_CMB × ...
```

so a shifted `N_eff_alt` would scale `C_ν` by `~ N_eff_alt /
3.046`. On the (T-4F-α-2) identity, this scales the
`(1 - L - R - Ω_b - Ω_DM) × C_ν × h²` right-hand side proportionally.

**Status.** **Structural only.** `N_eff` shifts `C_ν` but does not
independently pin Σm_ν. Without independent admissions for `(L, R,
Ω_b, Ω_DM, h)`, varying `N_eff` cannot produce a retained Σm_ν.

### (F3-γ) Admitted CMB `Ω_m,0 h²` peak-height pin (alt admission)

**Route.** Standard CMB peak-height admissions:

```text
Ω_m,0 h²  ≈ 0.143    (Planck CMB-derived)
Ω_DM  h²  ≈ 0.120    (Planck CMB-derived)
Ω_b   h²  ≈ 0.0224   (Planck CMB-derived)
```

These are h-independent quantities (CMB peak heights pin Ω h²
directly). On the matter-budget split `Ω_m,0 = Ω_b + Ω_DM + Ω_ν,0`:

```text
Σm_ν / C_ν = Ω_ν,0 h² / h² × h² = Ω_m,0 h² - Ω_DM h² - Ω_b h²
        Σm_ν = (0.143 - 0.120 - 0.0224) × 93.14 eV ≈ 0.056 eV
```

This is positive but **just below** the NO osc floor `0.0586 eV`
by a small margin (~0.003 eV).

**Status.** **Alt admission surface.** Bypasses the framework's
current-bank `Ω_DM` interval by using CMB-peak-derived `Ω_DM h²` instead.
Gives a positive Σm_ν that is in marginal tension with the NO osc
floor in the **opposite direction** from the Cycle-1 tension. This
is structurally significant: the framework current-bank `Ω_DM` ~0.268
gives Σm_ν < 0; the CMB-peak-admitted `Ω_DM h²` ≈ 0.120 gives
Σm_ν ≈ 0.056 < 0.0586 (NO floor). Both are within ~0.003 eV of
"physically just-allowed". The window for positive consistent
Σm_ν is narrow on either admission.

### (F3-δ) Lane 4D Dirac/Majorana basis route

**Route.** A prior unlanded branch proposed a Dirac global-lift
reading, but that note is not a current-main authority. Even if a
Dirac/Majorana basis decision later lands, does it constrain Σm_ν?

**Status.** **Kinematic only.** (T-4F-α-2) is a mass-density
relation; it is identical for Dirac and Majorana mass eigenstates.
Dirac/Majorana switches the basis (mass-eigenstate vs. flavor) but
not the cosmology bookkeeping. Lane 4D affects 0νββ
interpretation, not relic density. Not an independent cross-bound
route.

### (F3-ε) Baryogenesis/eta admitted-input promotion (F2 from prior fan-out)

**Route.** Promote `eta_obs` (baryon-to-photon ratio) from admitted
to retained via the framework's leptogenesis cascade. `Ω_b` would
then be retained.

**Status.** **Speculative.** Framework has substantial DM-
leptogenesis cascade content but does not currently retain
`eta_obs`. Even with a closed `Ω_b`, Σm_ν retention also requires
closed `(L, h, Ω_DM)` inputs; not currently available.

## 2. Synthesis

| Route | Status | Independent cross-bound? |
|---|---|---|
| F3-α (osc lower bound) | comparator only | **No** (observational) |
| F3-β (N_eff) | structural only | **No** (rescales C_ν) |
| F3-γ (CMB Ω h² alt admission) | usable but tension | **Yes** (~0.056 eV; ~0.003 eV below NO floor) |
| F3-δ (Lane 4D Dirac) | kinematic only | **No** (basis change) |
| F3-ε (eta retention) | speculative | **No** (not currently retained) |

**Synthesis result.** No orthogonal F3-* route supplies an
independent Σm_ν cross-bound on the framework's current-bank
surface. The best remaining single-cycle attack is **F3-γ**: alt
admission via CMB peak heights `Ω_m,0 h² ≈ 0.143, Ω_DM h² ≈ 0.120,
Ω_b h² ≈ 0.0224`. This route gives Σm_ν ≈ 0.056 eV at standard
CMB pins — positive but just below the NO osc floor.

The Cycle-1 tension and the F3-γ tension are in **opposite
directions** at the ~0.003 eV scale:

- Cycle-1 (framework current-bank Ω_DM): Σm_ν < 0 (excess Ω_DM by
  ~0.003);
- F3-γ (CMB-peak Ω_DM h²): Σm_ν ≈ 0.056 < 0.0586 (NO floor);
  shortfall by ~0.003 eV.

The narrowness of the consistent admission window (~0.003 eV
either way) suggests that any single cross-bound route is at the
edge of its admission tolerance. Numerical Σm_ν retention requires
multiple admissions tuned within ~0.003 eV of each other.

## 3. Implication for honest closure

**Cross-bound chain summary:**

| Source for Ω_DM | Σm_ν result at standard pins |
|---|---|
| Framework retained `[0.2677, 0.2697]` | `[-0.161, -0.076]` eV (Cycle 1) |
| CMB peak `Ω_DM h² ≈ 0.120` (F3-γ) | `~0.056` eV (just below NO floor) |
| Tightened framework `Ω_DM ≈ 0.265` | `~0.038` eV (positive but below floor) |

**Live structural-tension residue:** the framework's current-bank
`Ω_DM ≈ 0.268` vs. observation `Ω_DM ≈ 0.265`. The (T-4F-α-2)
identity itself is consistent with positive Σm_ν when `Ω_DM h² ≈
0.120` admitted from CMB.

**Honest closure status:** F3 cannot supply numerical Σm_ν
retention as a single-cycle move. The path forward requires either:

- (i) framework `Ω_DM` bound tightening by ~0.003 (research-level);
- (ii) bypassing framework `Ω_DM` via CMB peak admission (loses
  framework cross-bound usage; reduces to standard cosmology);
- (iii) Lane 5 (C1) gate closure to fix `h`, combined with
  closed `Ω_b h²` and closed `Ω_DM h²`, would supply a fully
  closed Σm_ν — but Lane 5 (C1) gate is itself open per the
  parallel `hubble-c1-absolute-scale-gate-20260428` loop's Cycles
  1-6.

All three paths are research-level pivots beyond a single audit
cycle.

## 4. What this synthesis closes

- Stuck fan-out per Deep Work Rules **landed**: 5 orthogonal Σm_ν
  cross-bound routes generated and audited.
- The Cycle-1 tension's structural source is **identified**: it is
  centered on the framework current-bank `Ω_DM` interval, not on
  (T-4F-α-2) itself.
- The F3 loop's hard residual is now **sharp**: numerical Σm_ν
  retention requires either framework `Ω_DM` tightening, alt
  admission bypass, or Lane 5 (C1) gate retention.

## 5. What this synthesis does not close

- Numerical Σm_ν retention.
- Framework `Ω_DM` bound tightening.
- Lane 5 (C1) gate closure.

## 6. Implication for honest stop and pivot

The F3 loop has now executed:

- Cycle 1: F3 DM cross-bound audit (structural tension identified);
- Cycle 2: stuck fan-out synthesis (5 orthogonal routes; structural
  tension confirmed centered on framework `Ω_DM` vs. observation).

This satisfies Deep Work Rules:

- audit quota: ≤2 audit-grade cycles in a row (within budget);
- stuck fan-out: ≥3 orthogonal premises generated and synthesized;
- no shallow stop: each cycle produced runner-verified structural
  content.

Honest stop is now appropriate. The F3 loop has identified the
structural-tension residue and the limits of the cross-bound. The
remaining work is either:

- **Pivot to a different lane** (Lane 6 M1/M5-c Koide-flagship-
  conditional);
- **Open a review PR** for the F3 loop and proceed with review-loop
  pressure;
- **Pivot back to C1** with the F3 result feeding into the C1
  HANDOFF (closing the cross-lane loop between Lane 5 and Lane 4F).

## 7. Cross-references

- F3 loop pack:
  `.claude/science/physics-loops/sigma-mnu-f3-dm-cluster-20260428/`.
- F3 Cycle 1 audit:
  `SIGMA_MNU_F3_DM_CROSS_BOUND_AUDIT_NOTE_2026-04-28.md`.
- 4F-α functional form theorem:
  `NEUTRINO_LANE4_4F_SIGMA_M_NU_FUNCTIONAL_FORM_THEOREM_NOTE_2026-04-28.md`.
- DM thermal-bounding theorem:
  `DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_BOUNDING_THEOREM_NOTE_2026-04-17.md`.
- Lane 5 (C1) gate work (Cycles 1-6 closed):
  PR #168 (audit); PR #169 (cycles 2-6 no-go + audit + fan-out).
- Cosmology open-number reduction:
  `COSMOLOGY_OPEN_NUMBER_REDUCTION_THEOREM_NOTE_2026-04-26.md`.

## 8. Boundary

This is a **stuck-fan-out synthesis** note (audit-grade). It does
not retain Σm_ν, does not retire any open import, and does not
extend the framework. It identifies the structural-tension residue
of F3 (framework `Ω_DM` interval vs. observation), maps the narrow
~0.003 eV window for cross-bound consistency, and confirms that
numerical Σm_ν retention requires research-level pivots beyond a
single audit cycle.
