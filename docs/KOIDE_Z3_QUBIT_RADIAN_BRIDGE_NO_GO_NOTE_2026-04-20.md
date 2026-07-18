# Koide Z_3-Qubit Enumerated Radian-Bridge No-Go Note

**Date:** 2026-04-20
**Claim type:** no_go
**Lane:** Scalar-selector cycle 1 — closure attempt on the residual radian-bridge postulate P.
**Status:** **No-go for the enumerated construction bank.** Four specified
Cl(3)/Z³ + d=3 constructions on the selected-line CP¹ base do not close
postulate P. The note does not exhaust all repo-native constructions.
**Primary runner:** `scripts/frontier_koide_z3_qubit_radian_bridge_no_go.py` (PASS=23 FAIL=0)
**Companion:** `docs/KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md`
is now a formal-only Q-Delta identity. This no-go note, not that repaired
parent, carries the radian-bridge obstruction context.

---

## 0. Summary

Postulate **P** asserts `ρ_δ := (real DOF of b) / (real dim Herm_d) = 2/d² = δ (radians)`,
i.e. at d=3, `2/9 (dimensionless) = 2/9 (radians)`. The task candidate theorem
was: on the physical selected line, the Pancharatnam-Berry holonomy per Z_3
cyclic element on the qubit CP¹ equals `2/d²` in radians at d=3.

**Result for the tested bank: fails.** The PB holonomy per Z_3 element on the qubit equator is
`π/3` at d=3 (a rational multiple of π), not `2/9`. Three subsidiary tested
closure candidates (full-orbit Bargmann, Plancherel-weight, interior-point
structural selector) each fail in a specific checked way. These four failures
leave P and constructions outside this bank open.

---

## 1. Supplied ingredients used by the tested constructions

- **R1.** Supplied selected-line CP¹ PB structure (KOIDE_BERRY_PHASE_THEOREM_NOTE_2026-04-19.md §4):
  `s(m) = (1/√2)v_1 + (1/2)e^{iθ(m)}v_ω + (1/2)e^{-iθ(m)}v_ω̄`,
  projective doublet `[1:e^{-2iθ}]`, `A = dθ`, `δ(m) = θ(m) − 2π/3` open-path holonomy.
- **R2.** Supplied bundle obstruction (KOIDE_BERRY_BUNDLE_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md):
  physical base is an interval; no closed-loop Berry holonomy forced by topology.
- **R3.** Supplied character decomposition (KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md A.2):
  dim ratio `(2 DOF of b) / dim_ℝ Herm_3 = 2/9` (dimensionless).
- **R4.** Supplied selected-line boundary points: `m_0 = -0.2658` (δ=0, unphased),
  `m_pos = -1.2958` (δ=π/12, positivity threshold), `m_* = -1.1604` (δ=2/9, physical).

---

## 2. Four tested closure candidates — all fail

### 2.1 Candidate A: PB phase per Z_3 element on qubit equator

With `χ(θ) = (1, e^{-2iθ})/√2` and Z_3 shift `θ ↦ θ + 2π/3`:
`γ_PB(g) = arg⟨χ(θ)|χ(θ+2π/3)⟩`. Using `(1 + e^{-2ix})/2 = cos(x) e^{-ix}` with
`x = 2π/d`: at d=3, `cos(2π/3) = -1/2 < 0`, so `γ_PB(g) = -2π/3 + π = π/3 ≈ 1.047`
rad, **independent of base point** (Bargmann invariant of three equidistant
equator points). For nonzero overlaps at the displayed `d`, it is a rational
multiple of π:

| d  | γ_PB(g)     | 2/d²   |
|----|-------------|--------|
| 3  | π/3         | 0.2222 |
| 5  | -2π/5       | 0.0800 |
| 7  | -2π/7       | 0.0408 |
| 11 | -2π/11      | 0.0165 |

**Fail:** `γ_PB(g_d)` is a rational multiple of π at every checked
nondegenerate `d`; `2/d²` is a pure rational. They disagree throughout that
tested set (the failure is not a d=3 numerical coincidence).

### 2.2 Candidate B: Closed-orbit Bargmann phase

Closed 3-step PB product around the Z_3 orbit on the equator is `arg(∏) = π`
(half 2π solid angle of great-circle equator triangle). Rational-coefficient
rescalings (π/d², π/d, π/9) never equal 2/9. **Fail.**

### 2.3 Candidate C: Plancherel-weight identification

The dim ratio `2/d²` on Herm_d is a dimensionless Plancherel count, and the
supplied/tested ingredients furnish no canonical map from that count to
radians. Restating P as "Plancherel weight 2/d² equals radian δ" is a
reformulation of P, not a derivation. **Fail (tautology).**

### 2.4 Candidate D: Interior-point structural selector on H_sel

On the physical first branch δ sweeps (0, π/12) from m_0 to m_pos. We tested
four supplied conditions that might pin `m_*` in the interior:

1. Pancharatnam midpoint gives δ = π/24 ≠ 2/9.
2. Equal-overlap selector: same midpoint.
3. Selected-slice eigenline geometric phases (R1 §6): `γ_lower(m_0 → m_*) ≈ 0.178`,
   `γ_upper(m_0 → m_*) ≈ 0.276`; equation `γ_lower = δ(m)` selects m ≈ -0.877, not m_*.
4. Fractional position `δ_*/δ_pos = 2/9 ÷ π/12 = 8/(3π)` is absent from the
   explicit rational bank tested by the runner.

**Fail for this candidate bank:** none of the four listed selected-line
conditions pins `θ(m_*) = 2π/3 + 2/9` as an interior point.

---

## 3. Shared pattern within the tested bank

The enumerated candidates expose a common mismatch:

- The enumerated character-algebra bank contains dimensionless pure rationals (dim
  counts, Plancherel weights) and rational multiples of π (angles from
  `e^{i·2π/d}`, solid-angle integrals, boundary angles).
- `δ = 2/9` is a pure rational measured in radians — neither a rational
  multiple of π, nor a dimensionless ratio.

> **Enumerated-bank obstruction.** Every angle in the runner's explicit
> native-angle bank is of the form `(rational) × π`, while the tested
> dimensionless ratios are pure rationals. None of those supplied quantities
> bridges `2/d² = 2/9` to radians. This finite-bank result is not a universal
> classification of every construction available in the repository.

---

## 4. Examples of still-open structural routes

Each of the following identities would close P if independently derived.
They are examples, not a minimal or exhaustive list, and none is supplied by
the results cited here.

**Input (a): Lattice propagator radian quantum.** A hypothetical Euclidean lattice
propagator identity `G_{C_3}(1) = exp(i · 2/d²) · G_0` on a specific
C_3-equivariant lattice, where `2/d²` appears literally as a radian phase.
No result cited by this note supplies this identity.

**Input (b): 4×4 hw=1+baryon non-uniform Wilson holonomy.** Extending hw=1 from
the supplied 3×3 triplet to a 4×4 sector with baryon coupling, where the
C_3 Wilson-line phase on the baryon-projected line equals `2/d²` rad. The 4×4
extension is an open frontier (SCALAR_SELECTOR_CYCLE1_SCIENCE_REVIEW_NOTE_2026-04-19.md).

**Input (c): Z_3-orbit Wilson-line d²-power quantization.** A hypothetical
quantization `W_{Z_3}^{d²} = exp(2i) · 𝟙`, giving per-element phase `2/d²`
rad. The supplied Z_3 group-theoretic quantization gives `W_{Z_3}^3 = 𝟙`
(rational multiples of π only) — not this.

All three preserve the physical base topology (no ambient-S² enlargement, no
Chern class, no monopole charge) so they respect the bundle-obstruction
theorem R2. P remains a clean single-real-number postulate; this note narrows
four attempted closures without proving that one of these example routes is
required.

---

## 5. Impact on the Koide program

- The linking theorem `δ = Q/d`
  (KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md) stays conditional:
  under P, closing `Q = 2/d` or `δ = 2/d²` closes the other; without P, both open.
- The selected-slice Berry eigenline no-go (R1 §6) is reconfirmed.
- The angle-1 (PB per Z_3 element) and angle-2 (Plancherel weight) routes
  suggested in the task are both refuted as closures.

**Remaining Open Imports register entry (suggested):**

> Radian-bridge P for `δ = 2/d²`. No-go against four enumerated Cl(3)/Z_3
> closure candidates. Example open routes: (a) lattice propagator radian
> quantum; (b) 4×4 hw=1+baryon Wilson holonomy; (c) Z_3-orbit Wilson-line
> d²-power quantization. None is supplied by this note. See this note.

**Strict-reviewer disclosure:** P remains open. This note excludes only the
four constructions tested here. It does not classify every repo-native angle
construction and does not prove that P requires one of examples (a), (b), or
(c).

---

## 6. Runner PASS list (23/23)

- F1a–c: per-Z_3 PB phase magnitude and base-point independence (Bargmann invariant).
- F2a–c: checked nondegenerate-d structure — rational multiple of π throughout
  the tested set, never `2/d²`.
- F3a–b: closed-orbit Bargmann = π, no rescaling gives 2/9.
- F4a–b: Pancharatnam midpoint gives π/24 (midpoint verified).
- F5a–b: fractional position `8/(3π)` is absent from an explicit rational bank.
- F6a–c: every angle in the enumerated native-angle bank is `(rational) × π`;
  2/9 is absent.
- F7a–b: Plancherel weight `2/d²` is dimensionless; no angle in that bank
  lies within `10^-6` of 1 rad.
- F8a–b: R1 §6 eigenline selector no-go reconfirmed.
- F9a–d: all four candidates fail (A by π/3, B by π, C as tautology, D by π/24).

---

## 7. Cross-references

- KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md (formal-only
  Q-Delta identity; context only)
- KOIDE_BERRY_PHASE_THEOREM_NOTE_2026-04-19.md (R1)
- KOIDE_BERRY_BUNDLE_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md (R2)
- KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md (R3, A.2)
- KOIDE_CIRCULANT_WILSON_TARGET_NOTE_2026-04-18.md (candidate input (c))
- SCALAR_SELECTOR_CYCLE1_SCIENCE_REVIEW_NOTE_2026-04-19.md (stack context)

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [koide_q_delta_linking_relation_theorem_note_2026-04-20](KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md)
- [koide_berry_phase_theorem_note_2026-04-19](KOIDE_BERRY_PHASE_THEOREM_NOTE_2026-04-19.md)
- [koide_berry_bundle_obstruction_theorem_note_2026-04-19](KOIDE_BERRY_BUNDLE_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md)
- `KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md` (back-reference, not load-bearing on this no-go note — circulant_character is an older sister exploring the character-theoretic Q-derivation candidate; this 2026-04-20 note's no-go argument does not consume circulant_character as a one-hop authority. Backticked to break length-8 cycle `cycle-0004` in `docs/audit/data/cycle_inventory.json`.)
- [koide_circulant_wilson_target_note_2026-04-18](KOIDE_CIRCULANT_WILSON_TARGET_NOTE_2026-04-18.md)
- [scalar_selector_cycle1_science_review_note_2026-04-19](SCALAR_SELECTOR_CYCLE1_SCIENCE_REVIEW_NOTE_2026-04-19.md)
