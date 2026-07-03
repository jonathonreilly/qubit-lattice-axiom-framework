# The Explicit Kähler-Dirac / Cl(3) Generation Realization Gives r=1; the Index "Count-Once" Route Is Closed at the Realization Level (Bounded No-Go)

**Date:** 2026-06-08
**Type:** no_go
**Claim type:** no_go (**bounded**, computable-side). Building the **explicit** Kähler-Dirac /
Cl(3) generation realization — not the abstract Dirac operator — gives `r = |b|²/a² = 1`
(Koide `Q=1`), and the **index "count-once" route** (which the meta-note
[`KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md`](KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md)
left as the open question — *"whether the framework's specific staggered-Dirac realization
delivers the first-order index"*) **does not deliver the count on this realization**. The
index is a signed mode-count, not the energy functional that sets the Koide weighting.
**Claim scope:** **bounded — not a hard universal no-go.** It establishes that the explicit
Cl(3)/Kähler-Dirac realization gives `r=1` (extending the abstract-Dirac result
[`KOIDE_DIRAC_MASS_FORCES_R_ONE_LR_COUPLING_BERRY_FLAT_BOUNDED_NO_GO_NOTE_2026-06-05.md`](KOIDE_DIRAC_MASS_FORCES_R_ONE_LR_COUPLING_BERRY_FLAT_BOUNDED_NO_GO_NOTE_2026-06-05.md)
from the abstract operator to the built realization), and that the index route is the wrong
*kind* of functional to produce `r=1/2`. It does **not** forbid `r=1/2`: that remains the
genuinely un-forced **signed / `U(1)_b` one-slot readout**, quantized away by `C³=I`.
**Status authority:** independent audit lane only. No effective-status change; independent
audit required.
**Primary runner:**
[`scripts/frontier_koide_kahler_dirac_realization_gives_r_one_2026_06_08.py`](../scripts/frontier_koide_kahler_dirac_realization_gives_r_one_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/frontier_koide_kahler_dirac_realization_gives_r_one_2026_06_08.txt`](../logs/runner-cache/frontier_koide_kahler_dirac_realization_gives_r_one_2026_06_08.txt)

---

## Role

The meta-note
[`KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md`](KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md)
removed SUSY as a blocker for the `r=1/2` index reading (McKean-Singer needs only a
chirality grading) and **localized** the open atom to one question: *does the framework's
specific staggered-Dirac realization deliver the first-order (count-once) index, or the
second-order (count-twice) modulus?* The reassessment
[`STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md`](STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md)
then verified that the realization is concrete: `D = d − δ` is the **Cl(3) geometric-algebra
action** on `Λ(ℂ³)` (one qubit = one Cl(3) chiral block; Hamming grading `1,3,3,1`).

This note **builds that realization explicitly** and computes the count. Runner **22/22**.

## The six exact facts (runner)

1. **Cl(3) is the qubit's geometric algebra.** `γ_μ = e_μ∧ − ι_{e_μ}` on `Λ(ℂ³)` satisfy
   `{γ_μ, γ_ν} = −2δ_{μν}`; the Hamming grading is `(1,3,3,1)`; the volume element (chirality)
   splits `8 = 4_+ ⊕ 4_-`. The de Rham / Kähler-Dirac **Euler characteristic is
   `1−3+3−1 = 0`** (runner A).
2. **The generation triplet is a dim-3 taste sector, and the two dim-3 sectors are the L/R
   chiralities.** The `C₃` cycle acts as the circulant `C` (`C³=I`); `M = aI + bC + b̄C²`;
   `Q = (Σλ_k²)/(Σλ_k)² = (1+2r)/3` is reproven from the spectrum `λ_k = a + 2|b|cos(δ+2πk/3)`
   (so `Q=2/3 ⇔ r=1/2` in the **signed-eigenvalue** readout, runner B).
3. **The built determinant is the modulus-squared.** With the two taste-3 sectors as L/R,
   `D = [[0, M],[M†, 0]]` gives `det D = |det M|²` (second-order **by construction**; only a
   Weyl fermion keeps `det M`), and `D²` has spectrum `=` the **singular values²** of `M`
   (sign-blind) — the physical Dirac masses (runner C).
4. **The index route is closed on the realization.** For the physical L/R grading,
   `Str(ε e^{−tD²}) = 0` (`MM†, M†M` isospectral). Over all 8 `C₃`-equivariant `ℤ₂`
   gradings, the index is a signed **mode-count** in `{±1, ±3}` — it can drop paired modes
   but **cannot re-weight the doublet *energy* by ½ in both `Σm_k` and `(Σ√m_k)²`**. The
   `(1,1,1)` multiplicity is the *static* regular-rep decomposition (measure-neutral), **not**
   a mass weighting (runner D). **This answers the meta-note's open question: the realization
   does not deliver the first-order count.**
5. **The energy readout is non-holomorphic → rank-2 → counts twice.** The doublet energy
   `Tr(M†M) = 3a² + 6|b|²` has `(Re b, Im b)` Hessian `diag(12,12)` (rank 2) — both real modes
   counted → `r=1`. A holomorphic functional of `b` alone would see one complex mode (`r=1/2`);
   the modulus sees `|b|² = b·b̄` → two (runner E). Taste cannot help: `dim Cl(3) = 2³` with a
   2-dim chiral (qubit) block, so there is **no taste-copy factor to root** (`|det M|² → det M`
   is unavailable; runner F).
6. **The residual, and the `θ` clarification.** `r=1/2` requires the **signed** readout — the
   `U(1)_b` doublet-frame quotient collapsing `(Re b, Im b)` to one complex slot *before* the
   readout — and `C³=I` quantizes that `U(1)_b` away; `J_cs=(C−C²)/√3` is a genuine complex
   structure but `[J_cs, M]=0` (measure-neutral). A global axial `θ` acts as a `C₃`-**scalar**
   phase on `M` (commutes with `C`), rotating all three channels equally; it **cannot** flip
   one eigenvalue's sign relative to the others. So the signed-`√m` (the `r=1/2` selector) and
   `θ` share the signed-spectrum **class** but `θ` does **not** force `r=1/2` (runner G, H).

## The wall, named exactly

> Built explicitly, the Kähler-Dirac / Cl(3) generation realization gives the **second-order
> (modulus / singular-value) count → `r=1`**. The taste `1,3,3,1` grading is the **L/R
> chirality doubling** (= the qubit), not an extra multiplicity factor; the McKean-Singer
> **index is a signed mode-count** (`0` for the physical L/R grading, `{±1,±3}` for the
> equivariant gradings), which is the **wrong kind of functional** to deliver the `(1,1)`
> energy weighting `r=1/2` needs. The only opening — the signed / `U(1)_b` one-slot readout —
> is **quantized away by `C³=I`**, and is measure-neutral to every static structure
> (`ε`, `J_cs`, taste, CPT). A single `θ` cannot manufacture it.

So `r=1` is forced on the realization; `r=1/2` is not derived. This **extends** the
abstract-Dirac partial-falsification to the explicit Kähler-Dirac realization: **the framework
does not derive the charged-lepton mass ratios**, and the index route does not change that.

## No-Go Discipline Gate (N1-N8)

**N1 — Alternative routes (all → r=1 or unforced):** abstract Dirac modulus (`|det M|²`,
landed #2758/06-05); explicit Kähler-Dirac realization (this note); McKean-Singer index
(signed mode-count, never an energy ½-reweight — closed here); equivariant `(1,1,1)`
multiplicity (static rep-count, measure-neutral); fluctuation modulus (rank-2 Hessian → r=1);
taste rooting (taste = qubit, no copy factor); `J_cs` (measure-neutral, `[J_cs,M]=0`); global
`θ` (`C₃`-scalar, cannot flip one sign). All land on `r=1` or are unforced.
**N2 — Wall independence:** the determinant order (Dirac ⇒ modulus), the index *kind*
(mode-count ≠ energy weighting), and the `C³=I` quantization of `U(1)_b` are independent
walls. The signed-vs-singular residual is the *consequence*, not a new wall.
**N3 — Hidden-wall scan:** "Dirac" is forced (charged leptons have both chiralities,
non-circular). "Kähler-Dirac = Cl(3)" is the verified 06-06 lead, reproven in the runner, not
assumed. No "by construction" admission beyond the Dirac chirality content.
**N4 — Residual matching:** the residual (signed `√m` / `U(1)_b` one-slot readout) matches
the landed signed-vs-singular and Berry-flat residuals exactly; the index closure matches the
meta-note's named open question.
**N5 — Rhetoric audit:** "the index route is closed" is scoped to *this realization* and to
the *mass-weighting* use of the index (a mode-count cannot be an energy ½-reweight). It is
**not** a claim that no index anywhere is `(1,1,1)`, nor that `r=1/2` is impossible.
**N6 — Partial-closure scan:** the signed-`√m` / `U(1)_b` readout is a *convention*
(which root of `m` / whether to quotient the doublet frame before reading), not a new axiom —
recorded as the open residual, not "new axiom required."
**N7 — Steelman:** the strongest case for `r=1/2` is that the **signed** readout gives
`Q=2/3` exactly. This is **real and unresolved** — hence the **bounded** status. What this
note adds: the index (the most natural non-modulus functional) is shown *not* to supply that
signed readout on the realization, narrowing the steelman to the bare `U(1)_b`-quotient
convention.
**N8 — Cross-cycle echo:** structurally similar walls (modulus, det, Berry-flat) were not
retired by later mechanisms; the index was the one route the meta-note left open, and it is
closed here at the realization level without a new axiom.

## Forbidden-import / reprove-and-cite

All facts reproven from the Cl(3) + `C₃` primitives in the runner (sympy/numpy, 22/22). The
lepton masses appear **only** as a comparator (the `D²` spectrum equals them); they are **not**
a derivation input. McKean-Singer, Dolbeault/HRR, Kähler-Dirac/Becher-Joos, Frobenius-Schur,
and the Berezin polarization are comparators only. No PDG values as inputs; `r=1/2`/`Q=2/3`
named only as the empirical target this note does **not** derive.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- [`KOIDE_DIRAC_MASS_FORCES_R_ONE_LR_COUPLING_BERRY_FLAT_BOUNDED_NO_GO_NOTE_2026-06-05.md`](KOIDE_DIRAC_MASS_FORCES_R_ONE_LR_COUPLING_BERRY_FLAT_BOUNDED_NO_GO_NOTE_2026-06-05.md)
- [`KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md`](KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md)
- [`STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md`](STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md)
- [`KOIDE_DOUBLET_IS_FROBENIUS_SCHUR_COMPLEX_TYPE_ORIENTATION_BOUNDED_NOTE_2026-06-07.md`](KOIDE_DOUBLET_IS_FROBENIUS_SCHUR_COMPLEX_TYPE_ORIENTATION_BOUNDED_NOTE_2026-06-07.md)
- [`KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md`](KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md)

## What this note does NOT claim

- It does **not** prove `Q = 2/3` impossible — the signed / `U(1)_b` one-slot readout remains
  genuinely OPEN; this note closes only the **index** route on the realization.
- It does **not** claim `Q=1` is the framework's final charged-lepton prediction.
- It does **not** retire, split, or re-grade the `AC_φλ` Tier-A admission; the realization
  selection remains the open gate.
- **No** new axiom, primitive, repo vocabulary, or class tag; no PDG input. It sets **no**
  audit status.

**Independent audit required.** This note asserts no effective-status change.
