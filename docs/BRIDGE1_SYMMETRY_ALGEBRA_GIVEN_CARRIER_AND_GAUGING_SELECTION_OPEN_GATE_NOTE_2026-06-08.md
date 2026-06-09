# Bridge-1: Symmetry Algebra of the Supplied Color Carrier (Bounded Support) and the Gauging-Selection Open Gate

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** bounded-support algebra + named open gate
**Claim type:** open_gate
**Status:** open-gate / bounded-support proposal. **Supersedes the rejected, over-framed
#3275** ("SM gauge algebra forced from the axioms; gauging irreducibly admitted"): that
claim boundary was too strong (the color carrier and the gauging principle are not axioms)
and lacked the no-go-discipline gate required for a closed no-go. This note keeps only the
finite-algebra **support** under explicit admitted assumptions and names the gauging
selection an **open gate** (not a closed no-go). Adds no axiom, no fitted value. Audit
verdict set by the independent audit lane.
**Primary runners** (exact numpy; each PASS=4):
[`scripts/bridge1_gauge_algebra_forced_gauging_admitted_2026_06_08.py`](../scripts/bridge1_gauge_algebra_forced_gauging_admitted_2026_06_08.py)
(conditional algebra given the carrier),
[`scripts/bridge1_color_base_covariance_Nc_equals_d_2026_06_08.py`](../scripts/bridge1_color_base_covariance_Nc_equals_d_2026_06_08.py)
(counterfactual `N_c=d` support),
[`scripts/bridge1_gauging_discriminator_blindness_no_go_2026_06_08.py`](../scripts/bridge1_gauging_discriminator_blindness_no_go_2026_06_08.py)
(four tested discriminators; the gate is not closed). *(Runner filenames are legacy; this
note's bounded-support / open-gate framing governs, not the filename wording.)*

## Explicit admitted assumptions (not axioms)

The algebra result is **conditional** on a supplied color-carrier realization. None of the
following is supplied by `{Lattice, Quantum, Record}`; each is an admitted input with its
own ledger authority:

| admitted input | authority | ledger role |
|---|---|---|
| the taste-cube / fiber-base split and the **`C³(base) ⊗ C²(fiber)` carrier factorization** | [`COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md`](COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md) | `MR_color` residual (meta) |
| the **selected weak axis** + the residual-swap base split → `su(3)` on `Sym²(ℂ²)` | [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md), [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md) | retained (algebraic embedding; physical-color identification explicitly deferred there) |
| the **link-connection convention** `qubit → u(2)` | [`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md) | bounded / pending-chain |
| the **two-endpoint Gauss carrier / gauging principle** | [`TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md`](TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md) | unaudited model convention |

## Bounded support — the algebra, GIVEN the carrier

**Given** the supplied `C³(base) ⊗ C²(fiber)` carrier, the runner verifies (exact, finite):
`su(2) = Aut(M₂(ℂ))` closes on the fiber (`u(2) = su(2)⊕u(1)`); `su(3)` has no faithful irrep
below dim 3, so color needs the 3-dim base; `su(3)⊗I` and `I⊗su(2)` **commute**, and with the
central `u(1)` the symmetry algebra of this carrier is `su(N_c) ⊕ su(2) ⊕ u(1)` — at `d=3`,
dim `8+3+1 = 12`. This is the symmetry algebra **of the supplied carrier**; it is **not**
derived from the axioms (the carrier factorization above is admitted).

## Counterfactual support — `N_c = d`

Under an **assumed** `Z^d` taste-cube family with one selected weak axis, the residual base
is `Sym^{d-1}(ℂ²)` (dim `d`) and its `S_{d-1}` symmetric-isotype commutant is `gl(d)` →
color block `su(d)`, so `N_c = d` along the family (runner table `d=2..6`). At the `Z³`
baseline this gives `N_c = 3`, **consistent with** the retained graph-first `SU(3)` result on
the live `d=3` surface. This is **support** — it shows `N_c` tracks the (assumed) lattice
dimension, addressing a "matched-pair coincidence" worry — **not** a from-axioms derivation
(the `Z^d` family, taste-cube, and weak-axis selection are assumed). The repo baseline is
`Z³`; the live derivation of the `d=3` color structure remains the retained graph-first note.

## The gauging-selection open gate

`{Lattice, Quantum, Record}` (+ the admitted carrier) fix the symmetry **algebra** but do not
fix the **gauging selection**: which symmetry is dynamically gauged, the physical-color
identification `MR_color`, and the chiral `su(2)_L`. The discriminator runner tests **four**
candidate discriminators and finds each blind to or circular with the selection: (1)
maximality cannot distinguish the dim-12 algebra from the full `u(6)` (both irreducible →
same commutant); (2) the anomaly `d`-tensor is a one-sided filter (`su(2)` `d_{abc}≡0`,
`su(3)` `d_{abc}≠0`), never a selector; (3) the chirality grading `ε` commutes with the color
generators (blind to the coupling chirality); (4) color is strictly complex (`3 ≠ 3̄`) while
the spatial `so(3)` vector is real (color ≠ complexified spatial). These four do **not close**
the gate. (A broader lens set was explored in an exploratory campaign, but only these four are
runner-backed here; closing the selection as a *no-go* would require the full N1–N8 route
enumeration with retained-authority failures, which this note does **not** assert.)

## What is and is not claimed

- **Is:** GIVEN the supplied carrier, the symmetry algebra is `su(N_c)⊕su(2)⊕u(1)` (dim 12 at
  `d=3`), with the factors commuting and acting irreducibly (bounded support); `N_c=d` holds
  along an assumed `Z^d` family, consistent with the retained `d=3` graph-first result
  (counterfactual support); the gauging selection is **not closed** by the four tested
  discriminators (open gate).
- **Is not:** does **not** claim the SM gauge algebra is *forced from the axioms* (the carrier
  is admitted); does **not** claim the gauging selection is an *irreducible admission / no-go*
  (it is an open gate, not a closed no-go, and no N1–N8 walk is asserted); does **not** derive
  the carrier, the gauging, or `MR_color`; adds no axiom or fitted value.

## Boundaries (honest)

- **Conditional algebra, not a derivation.** Every algebra statement is "given the supplied
  `C³⊗C²` carrier"; the carrier itself is the admitted `MR_color`/graph-first realization.
- **Counterfactual support, not a theorem about `Z³`.** The `N_c=d` covariance lives in an
  assumed `Z^d` family; on the baseline `Z³` it only re-supports the retained `d=3` surface.
- **Open gate, not a no-go.** The four discriminators are runner-backed support that the
  selection is not closed by them; this is not a proof that no discriminator can close it.

## Forbidden-imports check

No PDG / fitted / literature value is consumed. The algebra (Aut `M₂`, the `su(3)` irrep
dimension, the `[su(3),su(2)]=0` commutation, the `Sym^{d-1}(ℂ²)`/`gl(d)` commutant, the
`d_{abc}` tensor, the `ε`/color commutator, the reality bilinear) is reproven in the runners
from the qubit and lattice primitives. The Standard Model gauge group is named as the
comparator target only.
