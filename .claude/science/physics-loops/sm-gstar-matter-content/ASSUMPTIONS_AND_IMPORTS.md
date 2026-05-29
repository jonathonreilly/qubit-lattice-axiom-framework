# ASSUMPTIONS & IMPORTS — SM g_* matter-content derivation

All ledger statuses below were verified against
`docs/audit/data/audit_ledger.json` (`rows[<cid>]['effective_status']`) on
2026-05-29, per the "verify ledger before citing memory" rule. They are NOT
copied from source-note prose.

## 1. Import / dof-input ledger

Each row is one dof input consumed by the high-T `g_*` assembly. "Role"
distinguishes what the framework **derives** (sourced from a retained or
retained_bounded authority) from what is still an **import / residual**
(unaudited or convention-bearing) — the latter being framework-derivation
targets, NOT external SM census.

| # | dof input | value | source authority | ledger eff. status | role in this loop |
|---|---|---|---|---|---|
| I1 | SU(3)_c color gauge sector exists; `N_c = 3`, `dim adj = N_c^2-1 = 8` | 8 generators | `cl3_color_automorphism_theorem`; `graph_first_su3_integration_note`; `native_gauge_closure_note` | **retained** (positive_theorem) | DERIVED |
| I2 | SU(2)_L weak gauge sector exists; `dim adj = 3` | 3 generators | `native_gauge_closure_note` (Cl(3) bivector su(2)); `graph_first_selector_derivation_note` | **retained** (positive_theorem) | DERIVED |
| I3 | U(1)_Y hypercharge gauge sector exists; one B boson | 1 generator | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | **unaudited** (positive_theorem) | RESIDUAL (abelian surface excluded from native_gauge_closure_note; hypercharge note itself unaudited) |
| I4 | 2 transverse polarizations per massless vector | factor 2 | `massless_vector_polarization_count_from_lorentz_and_gauge_bounded_theorem_note_2026-05-28` | **unaudited** (bounded_theorem) | RESIDUAL — load-bearing core is pure rank arithmetic `4-1-1=2` but admits Lorentzian R^{3,1} signature (AC1) which leans on emergent-Lorentz, currently under repair |
| I5 | one complex SU(2) Higgs doublet -> 4 real scalar dof | 4 | `sm_one_higgs_yukawa_gauge_selection_theorem_note_2026-04-26` (assumes a single doublet); `ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26` (retained, one-doublet bookkeeping) | one-higgs-Yukawa note **unaudited**; the *number* of doublets is **assumed not derived** | RESIDUAL — single-doublet minimality is NOT framework-derived; named residual |
| I6 | 3 generations | `n_gen = 3` | `three_generation_observable_theorem_note`; `three_generation_observable_m3c_burnside_narrow_theorem_note_2026-05-10` | **retained** (positive_theorem) | DERIVED |
| I7 | per-generation matter content (Q_L, u_R, d_R, L_L, e_R, +nu) | see below | `one_generation_matter_closure_note`; `one_generation_anomaly_singlet_completion_narrow_theorem_note_2026-05-10` | one_generation_matter **unaudited**; singlet-completion **retained_bounded** | RESIDUAL — bounded conditional one-generation completion (anomaly + neutral-singlet branch convention) |
| I8 | hypercharge VALUES `(4/3, -2/3, -2, 0)`; charge spectrum `{0,+-1/3,+-2/3,+-1}` | exact rationals | `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24`; `sm_hypercharge_uniqueness_algebraic_solution_enumeration_narrow_theorem_note_2026-05-10` | uniqueness-theorem **unaudited**; algebraic-enumeration **retained_bounded** | RESIDUAL — values fixed conditional on matter content + neutral-singlet convention |
| I9 | per-Dirac-fermion 4 dof (2 spin * 2 particle/anti); per-Weyl 2 dof | 4 / 2 | `per_site_su2_spin_half_theorem_note_2026-05-02` (spin); `spin_statistics_cardinality_pauli_exclusion_narrow_theorem_note_2026-05-10` | spin-half **audited_conditional**; cardinality **retained** | MIXED — spin-1/2 carrier audited_conditional, cardinality retained; the spin*antiparticle=4 / Weyl=2 count uses both |
| I10 | fermionic Stefan-Boltzmann weight 7/8 | `7/8 = eta(4)/zeta(4)` | `hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow_theorem_note_2026-05-10`; `axiom_first_fermionic_stefan_boltzmann_narrow_theorem_note_2026-05-26` | hierarchy-7/8 **retained** (positive_theorem); fermionic-SB **unaudited** (bounded_theorem) | DERIVED (7/8 ratio retained) + RESIDUAL (full fermionic-SB derivation unaudited) |
| I11 | high-T unbroken-phase thermal regime (T > EW crossover) | regime choice | conventional cosmology; `g_star_sm_content_at_leptogenesis...` premise P5 | NOT framework-derived | IMPORT — regime choice (counterfactual C-a) |
| I12 | RH neutrino NOT thermally counted at this T | choice | `one_generation_matter_closure_note` includes `nu_R: (1,1)_0` (a gauge singlet); thermal exclusion is a premise | NOT framework-derived | IMPORT — neutrino-sector choice (counterfactual C-c) |

### Per-generation count (30) breakdown sourced from I6-I9

```text
quarks:          (n_up + n_down=2) * (N_c=3) * (Dirac 4)  = 24
charged leptons: (1)                * (Dirac 4)            = 4
active neutrino: (1 LH Weyl)        * (2 helicity/anti)    = 2
per generation total                                       = 30
fermionic total = n_gen(3) * 30                            = 90
```

## 2. Derived vs residual summary

**DERIVED from RETAINED framework structure (positive_theorem retained or
retained_bounded):**

- SU(3)_c sector + `dim adj = 8` (I1, retained)
- SU(2)_L sector + `dim adj = 3` (I2, retained)
- `n_gen = 3` (I6, retained)
- spin-statistics cardinality (I9 part, retained)
- fermion thermal weight ratio `7/8` (I10 part, retained)
- hypercharge-value algebraic enumeration (I8 part, retained_bounded)
- one-generation anomaly singlet completion (I7 part, retained_bounded)

**NAMED RESIDUALS (framework-derivation targets, NOT external SM census;
each unaudited or convention-bearing):**

- R-U1Y: U(1)_Y hypercharge gauge sector existence (I3, unaudited; abelian
  surface explicitly excluded from `native_gauge_closure_note`).
- R-POL: massless-vector 2-polarization (I4, unaudited; admits Lorentzian
  signature AC1 — emergent-Lorentz under repair).
- R-HIGGS: single complex Higgs doublet minimality (I5, assumed not derived).
- R-MATTER: one-generation matter completion as a full framework theorem
  (I7, unaudited; bounded conditional on neutral-singlet branch convention).
- R-FSB: full fermionic Stefan-Boltzmann derivation (I10 part, unaudited; the
  `7/8` *ratio* is retained, but the substrate fermionic-SB note is unaudited).
- R-SPIN: per-site spin-1/2 carrier (I9 part, audited_conditional).

**IMPORTS (regime/sector choices, not framework-derived, recorded honestly):**

- I11 high-T unbroken-phase regime.
- I12 RH neutrino thermal exclusion.

## 3. Counterfactual pass (run BEFORE authoring, per feedback_run_counterfactual_before_compute)

For each implicit choice: "what if this is wrong, and what opens?" Mark CLOSED
(settled by a retained framework result or by the explicit regime declaration)
or OPEN (genuine residual / framework-derivation target).

### C-a. Thermal regime: high-T unbroken vs post-EWSB massive

**What if wrong?** If we counted the *broken-phase massive* spectrum instead
(massive W^+-, Z each with 3 polarizations; photon 2; Higgs 1 real scalar) the
bosonic dof bookkeeping is still 28 (`16 gluon + 2 photon + 9 massive W/Z + 1
Higgs = 28`, as the import note records), but the *sourcing changes
qualitatively*: massive-vector counts use `4-1=3` (no residual gauge orbit, see
massless-polarization note R8/§9), and the Higgs eaten-Goldstone bookkeeping
moves 3 of its 4 scalar dof into the longitudinal W/Z. The g_* relevant for the
leptogenesis cascade is the **high-T unbroken** count, where each gauge boson
is massless with 2 polarizations and the Higgs carries 4 scalar dof.

**Status: CLOSED by explicit regime declaration (I11).** The cascade consumer
(DM-leptogenesis at T > EW crossover) fixes the high-T regime; we count
gauge-GROUP dof (massless vectors) and 4 Higgs scalar dof. The broken-phase
total coincides (28) but is recorded only as a bookkeeping equality, not used.
The regime itself is an honest IMPORT (conventional cosmology), not framework-
derived — flagged as such.

### C-b. Massless-vector polarization count: 2 vs other

**What if wrong?** If a massless vector carried a different polarization count
(e.g. 3, as for a massive vector, or a Lorentz-violating modified count) the
gauge dof totals shift: `24 -> 36` for 3 pol, breaking the 28 bosonic total.
The count `2` rests on the rank arithmetic `4 - 1 - 1 = 2` (Lorenz constraint +
residual gauge orbit on the null shell), which is the content of
`massless_vector_polarization_count_...note_2026-05-28`.

**Status: OPEN (residual R-POL).** The rank-arithmetic core is a pure
linear-algebra identity, but it **admits the Lorentzian R^{3,1} signature
(AC1)** as standard relativistic-QFT context. The framework's emergent-Lorentz
derivation is **currently under repair** (cf. the l=4 cubic-harmonic coefficient
fix on EMERGENT/3+1D-boost/lorentz_violation, 2026-05-29). Honest scope: the
2-polarization count is a bounded narrow identity over admitted Lorentzian
signature, not a fully framework-derived count, until emergent-Lorentz lands.
Flagged as a named residual.

### C-c. Neutrino sector: LH-only / Dirac / Majorana / RH-present

**What if wrong?** This is the most load-bearing fermionic choice. Options:
- **LH-only (Weyl) active neutrino, RH not thermally counted** (the chosen
  inventory): per-generation neutrino dof = 2 -> per-gen 30 -> fermionic 90.
- **Dirac neutrino with thermalized nu_R**: per-generation neutrino dof = 4
  (like a charged lepton) -> per-gen 32 -> fermionic 96 -> g_* = 28 +
  (7/8)*96 = 28 + 84 = 112.
- **Majorana**: 2 dof per generation (same count as LH-only Weyl for thermal
  purposes), no separate thermalized nu_R.

The framework's `one_generation_matter_closure_note` and the hypercharge
uniqueness note **do include** a right-handed neutral singlet `nu_R: (1,1)_0`
in the anomaly-completion content. But `nu_R` is a **gauge singlet** (no SU(3),
SU(2), or U(1)_Y charge), so at the leptogenesis temperature it is **not
necessarily in thermal equilibrium** with the gauge plasma (its only coupling
is the Dirac Yukawa, which is tiny, or a Majorana mass). The chosen inventory
(matching the import note's "active neutrinos: 3 flavors * 2 helicity/anti =
6") treats only the LH active neutrino as thermally counted.

**Status: OPEN (residual R-MATTER / IMPORT I12).** The framework anomaly
content includes nu_R as a gauge singlet, but the *thermal exclusion* of nu_R
at the leptogenesis T is a premise (I12), not a framework derivation. If nu_R
were thermalized and Dirac, g_* would be 112 not 106.75. The honest scope:
g_* = 106.75 holds for the LH-active-neutrino-only thermal inventory, with the
nu_R thermal exclusion stated as an explicit premise. The neutral-singlet
branch convention (which assigns nu_R hypercharge 0) is itself a convention in
`one_generation_matter_closure_note` (audited_conditional residual). This is
the single most important honest caveat.

### C-d. One Higgs doublet vs more

**What if wrong?** A second Higgs doublet (2HDM) would add 4 more scalar dof
(bosonic 28 -> 32 -> g_* = 32 + 78.75 = 110.75); a real triplet would add
differently. The `sm_one_higgs_yukawa_gauge_selection_theorem_note` works the
gauge-selection of Yukawa monomials **given** one doublet, and the retained
`ew_higgs_gauge_mass_diagonalization` note uses one doublet, but **neither
derives that there is exactly one complex doublet** — the single-doublet choice
is an input. Repo no-go notes (`DM_NEUTRINO_CANONICAL_TWO_HIGGS_SLOT_NO_GO`,
`DM_NEUTRINO_TWO_HIGGS_23_SYMMETRIC_SLOT_NO_GO`) foreclose *specific* two-Higgs
DM-sector slot constructions but do not constitute a general single-doublet
minimality theorem for the thermal census.

**Status: OPEN (residual R-HIGGS).** The single complex Higgs doublet (4 scalar
dof) is a named residual: the framework uses one doublet downstream but does not
derive its minimality. Flagged as a framework-derivation target.

### C-e. Color count N_c = 3 and adjoint dim 8

**What if wrong?** N_c != 3 would rescale the quark dof (24 = 2*N_c*4) and the
gluon dof (2*(N_c^2-1)). But `N_c = 3` is **retained** via
`cl3_color_automorphism_theorem`, and `dim adj = N_c^2 - 1 = 8` is an elementary
Lie identity.

**Status: CLOSED by retained framework result (I1).**

### C-f. Generation count n_gen = 3

**What if wrong?** n_gen != 3 rescales the fermionic total linearly
(90 = 3*30). But `n_gen = 3` is **retained** via
`three_generation_observable_theorem_note` +
`three_generation_observable_m3c_burnside_narrow_theorem_note_2026-05-10`.

**Status: CLOSED by retained framework result (I6).**

### C-g. Fermion thermal weight 7/8

**What if wrong?** A different fermion/boson statistical weight changes the
combination. But the *ratio* `7/8 = eta(4)/zeta(4)` at d=4 is **retained** via
`hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow_theorem_note`.
The full substrate fermionic-SB derivation
(`axiom_first_fermionic_stefan_boltzmann...`) is unaudited.

**Status: CLOSED for the ratio (retained, I10); OPEN for the full
substrate-SB derivation (residual R-FSB).**

## 4. Counterfactual-pass conclusion

- **CLOSED by retained framework results:** color N_c=3 + adj 8 (C-e),
  generation count 3 (C-f), 7/8 ratio (C-g, ratio only), SU(2) adj 3 and SU(3)
  adj 8 sectors (C-e implies, retained).
- **CLOSED by explicit regime declaration (honest import):** thermal regime
  (C-a, high-T unbroken).
- **OPEN residuals (framework-derivation targets):** U(1)_Y existence (I3),
  massless-vector 2-polarization (C-b, emergent-Lorentz-dependent), single
  Higgs doublet (C-d), one-generation matter completion as a full theorem +
  neutral-singlet convention (C-c part), full fermionic-SB derivation (C-g
  part), per-site spin-1/2 (audited_conditional).
- **OPEN import (sector choice, honest):** RH-neutrino thermal exclusion (C-c,
  I12) — if nu_R were thermalized Dirac, g_* = 112.

The counterfactual pass confirms the honest claim type is **bounded_theorem**:
the assembly is sourced from framework structure, but several load-bearing
pieces remain unaudited/convention-bearing residuals. The advance is retiring
the monolithic external "declared SM census" import in favor of this
framework-internal assembly with named residuals.

## 5. No-new-axiom check

No new axiom is introduced. Every dof input is either (a) a retained /
retained_bounded framework authority, or (b) a named residual that is itself a
framework-derivation target (the legitimate import -> bounded -> retire path),
or (c) an explicitly-flagged regime/sector import. The import being retired is
the monolithic external SM census; it is replaced by framework-internal
structure, not by an enlarged axiom stack.
