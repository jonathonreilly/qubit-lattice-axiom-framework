# Hierarchy on the scale ladder: tests (12-hour goal; started 2026-10-18T11:24Z)

**Request.** Jon (2026-10-18): "work hierarchy derivation on the scale ladder approach in the recent PR as a 12 hour goal (stop if you get it earlier)". He chose to cover both the scale hierarchy and the fermion mass hierarchy.

**Context.**
- **PR #9702 (scale ladder).** Its tools are transport of invariants, uniqueness from symmetry, and channel limits. It records that relevant couplings, i.e. masses and scales, "are transported by the ladder but never fixed by it".
- **The hierarchy lane on main.**
  - Candidate formula: v = M_Pl·(7/8)^{1/4}·α_LM^16, with 16 = 2^4, the naive-lattice species count.
  - Its magnitude comes from α_bare^16 = (4π)^-16.
  - Open gates: B3 (substrate/regulator selection) and B4 (coupling-power transport). B5 is the observable identification.
  - Status note: docs/HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md, including its corrigenda.

**HIER-1. Scale hierarchy on the ladder.** Can the ladder's tools derive a ratio of physical scale to grid scale ≲ 1e-15? Inputs must come from the framework's fixed data, with no supplied input below 1e-2 and no tuning.
- **Mechanisms to test.** At minimum, examine all three:
  - **(a) B4 as ladder transport.** Is the exponent 16 a cross-rung invariant (a species/index count that survives every admissible coarse-graining), so that α^16 is transported rather than chosen?
  - **(b) Dimensional transmutation.** A marginal coupling of the ladder's content, with b₀ fixed by its field content, gives exp(-c/g²).
  - **(c) Rung compounding.** (a/w)^p suppression multiplied across rungs.
- **Readings.**
  - **HIER-DERIVED:** some mechanism yields the ratio from fixed framework data, proved or checked, with every supplied input listed and none below 1e-2.
  - **HIER-REDUCED:** B3/B4, or the whole hierarchy, is reduced to one named, smaller primitive, stated precisely and strictly narrower than before.
  - **HIER-NO-GO:** proof that the ladder's tools cannot fix a relevant coupling's value within a stated class.
  - **OPEN:** otherwise.

**HIER-2. Fermion mass hierarchy on the ladder.** Can protected masses (PR #9702 item 4: m ∝ breaking) plus breaking that enters at different rungs or orders give the observed charged-fermion ratios? That means m_i ∝ ε^{n_i}, with integer n_i set by symmetry and ε a ladder parameter. The observed range is about 1e-6 to 1.
- **Readings.**
  - **MASS-DERIVED:** symmetry fixes the n_i, and with at most 2 continuous parameters all 9 charged-fermion masses come within a factor of 3. CKM must be consistent with the structure, at least its hierarchy pattern.
  - **MASS-PARTIAL:** the pattern holds for one sector, or within a factor of 10.
  - **MASS-NO:** a proof that the class cannot produce it.
  - **OPEN:** otherwise.

**Stop rule.** The goal stops early if HIER-1 reads HIER-DERIVED and a same-family referee confirms it.
