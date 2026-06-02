# Carrier-Locus Decomposition: matter operator import localized; Hamming-weight-1 locus labels are native

**Date:** 2026-06-01
**Claim type:** bounded_theorem
**Claim boundary:** bounded source decomposition. This note corrects prior
frontier labels, verifies native Hamming-weight shell labels, and localizes the
remaining matter-operator import. It does not derive the matter frame, approve an
import, close a Koide value, or set an audit verdict.
**Primary runner:**
`scripts/frontier_koide_carrier_locus_decomposition.py`
with cache
`logs/runner-cache/frontier_koide_carrier_locus_decomposition.txt`
(11/11 checks).

## Setting

The charged-lepton carrier reduces to a **carrier type** (momentum, derived) and a
**carrier locus** -- the operator with massless modes at the Hamming-weight-1 (3-corner)
generation triplet. This note decomposes the locus's fermionization chain
(`bosonic M₂(ℂ) qubit → Grassmann (L1) → single-mode (L2) → first-order/{ε,D}=0 (L3) →
hw=1-locus (L4)`) leg by leg, locates the irreducible import, and corrects three
mislabels in the prior framing.

## Three frontier mislabels, corrected

The framing "the staggered operator selects hw=1 via an S₃-breaking blocked by
`gauge_wilson_isotropy`" is a **double mislabel** (verified, runner):

1. **No spectral hw=1 selection (C1).** The free staggered `D` keeps **all 8**
   Brillouin-zone corners massless: `|D(k)|² = Σ_μ sin²(k_μ) = 0` at every corner
   `k_μ ∈ {0,π}`. A Wilson term lifts all but `hw=0`. So "staggered selects hw=1"
   is false *as a gap-claim*.
2. **hw=1 naming needs no axis-anisotropy (C2).** `hw=1` is singled out by two
   **S₃-*invariant*** labels — ε-parity `(−1)^hw = −1` **and** S₃-orbit-size `= 3`
   (uniquely; `hw=3` has orbit-size 1, `hw=2` has ε `= +1`) — neither of which picks
   a spatial axis
   ([`STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md)
   + `staggered_axis_symmetry_is_s3`, both retained).
3. **`gauge_wilson_isotropy` is the wrong wall (C3).** Its scope is unequal
   plaquette *coefficients* — a different object from the hw=1 corner selection.

## Where the import is: the matter Dirac operator M

The locus does **not** reach no-import. The irreducible import is **two orthogonal
scoped-frame knobs on the matter Dirac operator M**, which couple on a single object:

- **L1 — statistics.** Native cross-site qubit ladders **commute** (disjoint tensor
  factors) — a **hard-core boson**, not a fermion. JW dressing gives CAR but is an
  invertible change of generators inside one ungraded algebra, so the fermionic frame
  is a **choice** (the dim-2 / Berezin readout excludes only the *free/CCR* boson, never
  the hard-core one;
  [`STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md`](STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md),
  cited no-go authority).
- **L3 — range.** First-order vs the ε-even Wilson/second-order/mass sector (a scoped
  frame; the substep-2 note declines Class-A uniqueness,
  [`STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md),
  cited bounded authority).

The two knobs couple on **the sign of the cross-site hopping bilinear `c_x†c_y`** — the
only frame-distinguishing quantity, which is *simultaneously* what makes the frame
fermionic (L1) and what lives in the first-order operator (L3). So both imports reduce to
one sentence — "**M is the first-order, cross-site-anticommuting (fermionic), chiral
`{ε,D}=0` staggered operator**" — supplied as a scoped frame. This is the carrier-frame
object (the reconstruction `R`); **the carrier locus adds no separate import.**

## What is native given M (mislabel-native, no import)

- **L2 — single-mode count.** `2^p = 2 ⟹ p = 1` uniquely (Dirac-4 → `2^4=16`,
  2-flavor → `2^2=4`); multi-mode is excluded by the 2-dim site. Occupation `{0,1}` is
  supported by the cited integer-spectrum and parity-grading authorities.
- **L4 — hw=1 naming.** The S₃-invariant labels above (no import).
- **L3a — `{ε,D}=0` given first-order.** Every nearest-neighbour real-antisymmetric `D`
  is ε-odd (verified for random weights); the converse fails (a Hamming-change-2 hop is
  ε-even = the Wilson sector). So chirality `{ε,D}=0` is *derived* given range-1.

## The lone residual: one Z₂ Hodge-orientation bit

Beyond M, the only remaining discrete DOF is a **single global Z₂ Hodge-orientation
bit**: `hw=1` (1-forms / vector) vs `hw=2` (2-forms / pseudovector) — both S₃-triplets,
**Hodge-dual** in `d=3` (the Hodge star is charge-conjugation there). It equals
`sign(Pfaffian of the doublet block) = sign(β)`, left **free** by CPT-exactness
([`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md),
retained-bounded), and no cited no-go blocks it. Records-growth (the pointer-vacuum
`|000⟩`'s Hamming-shell-1 *is* hw=1) is a candidate source, but the
`{records-pointer Z₂ = sign(β)}` bridge is open, not a theorem.

## Net and the next path

The carrier is: **one operator M (= `R`), two coupled knobs hinging on a single sign,
plus one harmless Z₂ Hodge bit.** Three fronts (none routing through any blocked wall):
**(i)** select the cross-site hopping sign -- probe whether reflection-positivity / CPT /
locality on M (or a non-local records structure) selects the anticommuting frame
(collapses L1+L3 at once); **(ii)** pin first-order via the substep-2 Class-A enumeration;
**(iii)** close the `records-pointer = sign(β)` bridge for the lone Z₂ Hodge bit (the
smallest residual). Front (i) is the same microcausality/reflection-positivity lever the on-site
Weyl-boost note's faithfulness-selection residual hands off to — the two converge.

## Non-circularity

`Q=2/3` never appears (the chain stops at the carrier locus, upstream of any Koide value);
`hw=1` is derived from the operator's own zero-mode structure + S₃-invariant labels, never
assumed (runner).

## Load-bearing authorities

[STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md](STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md),
[STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md](STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md),
[STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md),
[STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23.md](STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23.md),
[GAUGE_WILSON_ISOTROPY_BOUNDARY_NOTE_2026-05-04.md](GAUGE_WILSON_ISOTROPY_BOUNDARY_NOTE_2026-05-04.md),
[Q_INTEGER_SPECTRUM_THEOREM_NOTE_2026-05-02.md](Q_INTEGER_SPECTRUM_THEOREM_NOTE_2026-05-02.md),
[FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md](FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md),
and
[CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md).
