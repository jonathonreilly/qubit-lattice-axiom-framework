# The KO-Dimension / Real-Structure Route to a Koide Hard No-Go Is Empty (an Inversion); r=1/2 Is J-Allowed, and r Is Undetermined by {Axioms + Real Structure} (Bounded No-Go + Independence Corollary)

**Date:** 2026-06-08
**Type:** no_go
**Claim type:** no_go (blocks a re-walk-prone *hard* no-go) + independence corollary.
**Claim scope:** This note **blocks** a proposed KO-dimension hard no-go (that the real
structure forbids `r = |b|²/a² = 1/2` and forces `r=1`). It establishes the *opposite*:
`r=1/2` is **J-allowed**, the real structure is **silent on the value r** (`[M, J] = 0`
for every coupling `b`), and therefore — with both readouts already being K/CPT-orbit-
invariant readouts of the same operator — `r` is **undetermined by {Lattice, Quantum,
Record} together with the real structure / KO-dimension**. It does **not** derive `r`
(either value); the physical selection remains exactly the two admitted bits of `AC_φλ`.
**Status authority:** independent audit lane only. No effective-status change.
**Primary runner:**
[`scripts/frontier_koide_kodim_route_empty_independence_2026_06_08.py`](../scripts/frontier_koide_kodim_route_empty_independence_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/frontier_koide_kodim_route_empty_independence_2026_06_08.txt`](../logs/runner-cache/frontier_koide_kodim_route_empty_independence_2026_06_08.txt)

---

## Role

A candidate **hard** no-go was proposed: *"`Cl(3,0)=M₂(ℂ)` ⇒ KO-dimension 3, sign table
`(J²,JD,Jχ)=(−1,+1,−)` ⇒ `Jχ=−χJ` ⇒ the count-once (holomorphic / 2-sector) projection
giving `r=1/2` is not J-real ⇒ `r=1/2` forbidden ⇒ `r=1` forced."* If true, it would
upgrade the bounded
[`KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md`](KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md)
to a hard no-go.

**It is a triple inversion.** Using the framework's *actual* real structure
`J = U_swap ∘ conj` (the `C₃` reflection `C→C²` composed with conjugation; the landed
[`BAE_NCG_KODIM_REAL_STRUCTURE_PARTIAL_NARROWING_NOTE_2026-05-17.md`](BAE_NCG_KODIM_REAL_STRUCTURE_PARTIAL_NARROWING_NOTE_2026-05-17.md)
construction), the runner (**15/15**) shows each leg fails — and the honest content is the
**opposite**: `r=1/2` is J-allowed and `r` is undetermined by the real structure.

## The three inverted legs (runner)

1. **`J² = +1`, not `−1`** (A,B). KO-dimension 3 *requires* `J²=−1`; the framework's
   `J=U_swap∘conj` is an involution (`J²=+1`). With `JD=+DJ` the pair `(+,+)` is KO-dim 0
   or 7, and since **no within-generation `ℤ₂` grading `χ` anticommutes with a generic
   circulant `D`**, the generation triple is **odd = KO-dim 7, ungraded**. So the claim's
   pivotal `Jχ=−χJ` is **ill-posed** — there is no canonical `χ` at an odd KO-dimension
   (the `χ` of the Kähler-Dirac note is the *extrinsic* `Cl(3)` volume element / L-R
   doubling, not a within-generation grading).
2. **The count-once (2-sector) projection is J-REAL** (C). `f_singlet=(1,1,1)/√3` is real
   and `[M,J]=0`, so `P_singlet, P_doublet` (and in fact every eigenprojector) satisfy
   `J P J⁻¹ = P`. The claim that "the count-once projection is not J-real" is **backwards**:
   the count-once / 2-sector partition is exactly the J-compatible one (consistent with the
   einselection note: a K-real coupling einselects the 2 sectors).
3. **`[M, J] = 0` for every `b`** (A,E). `J M J⁻¹ = U M̄ U = M` for all `a, b` (because
   `U C U = C²`). So the real structure commutes with the mass at `r=0.25, 0.5, 1.0` alike:
   **J fixes the (J-real) 2-sector partition but is provably silent on the
   equipartition-vs-dimension weight** — i.e. silent on the value `r`.

Supporting (D,F): the `r=1/2` condition (HS equipartition `‖aI‖²=3a² = ‖bC+b̄C²‖²=6|b|²`,
i.e. `|b|²=a²/2`) is **J-symmetric** (`|b|²` is invariant under `b↔b̄=J`), so `r=1/2` is
reached J-evenly, not by a J-odd "holomorphic pick." The landed Berezin orientation
(holomorphic/det_C ↔ `r=1/2`; realified/det_R ↔ `r=1`) is **preserved, not inverted**;
since the count-once partition is J-real, `r=1/2` is J-**allowed**.

## The wall, named exactly

> The framework's real structure `J=U_swap∘conj` has `J²=+1` (the generation triple is the
> ungraded KO-dim-7 one, not KO-dim 3), the count-once / 2-sector projection `P_doublet` is
> J-real, and `[M,J]=0` for every coupling. Therefore the real structure **does not forbid
> `r=1/2`** — it is J-allowed — and it is **silent on the value `r`**: both `r=1` (dimension
> weight) and `r=1/2` (equipartition weight) are J-real readouts of the same J-real
> 2-sector partition.

## Independence corollary

Both readouts — `|det M|²` (realified/dimension → `r=1`) and the signed/2-sector
equipartition (holomorphic → `r=1/2`) — are **K/CPT-orbit-invariant scalar readouts** that
satisfy {Lattice, Quantum, Record} verbatim, and now also commute with the real structure
(`[M,J]=0 ∀b`). The axioms and the real structure **name no `r`**. So **`r` is undetermined
by {Lattice, Quantum, Record} + the real structure / KO-dimension** — the discriminating
datum lives below their resolution. The physical selection requires exactly **two admitted
bits**: a **K-odd (T-violating) `δ=0` pin** (the orientation; note `J`-cleanliness of the
*plain*-conjugation real structure holds only on the degenerate `δ=0` locus) and the
**det_C-vs-det_R measure** (the value). These two bits are the content of the `AC_φλ`
admission. This is the precise, structural form of "both `r=1` and `r=1/2` are valid
readings; the framework cannot select between them."

## No-Go Discipline Gate (N1-N8)

**N1 — routes:** (a) KO-dim hard no-go — *empty/inverted* (this note: `J²=+1`, `P_doublet`
J-real, `[M,J]=0`); (b) modular/thermal time selecting the 2-sector — *degeneracy-trapped*
(δ=0 only); (c) einselection selecting the value — *no-op on `r`* (landed); (d) index
count-once — *mode-count, not an energy reweight* (landed); (e) plain-conjugation real-structure
route — *J-clean only on the degenerate `δ=0` locus and still leaves `P_doublet` J-real*; (f)
Berezin-orientation inversion route — *inverted by the landed det_C/det_R orientation*. All leave
`r` undetermined.
**N2 — wall independence:** the three inverted legs are independent (`J²` sign; partition
J-reality; `[M,J]=0`). **N3 — hidden-wall scan:** "KO-dim 3", "holomorphic", "chiral" are
tested, not imported; the chirality `χ` invoked by the claim is shown not to exist within
the generation triple. **N4 — residual matching:** the residual attacked here is only the proposed
KO-dim/real-structure hard no-go. It matches the Kähler-Dirac `r=1` route only as a proposed upgrade
of that route; it does not claim to close the det_C-vs-det_R measure residual or the T-odd `δ=0`
orientation residual. **N5 — rhetoric audit:** "empty/inverted" means the *specific*
proposed hard no-go fails on the framework's actual `J`; it is **not** a claim that `r=1/2`
is derived. **N6 — partial-closure:** the two admitted bits remain the open residual; a
future derivation of either (a framework-native T-odd `δ=0` selector; a forced det_C
measure) could still move `r` without a new axiom. **N7 — steelman:** a different real
structure (`J=plain conj`, `J²=+1` but `JMJ=M̄`) makes the eigenmodes non-J-real — but it is
J-clean only on the `δ=0` degenerate locus and *still* leaves `P_doublet` J-real; it does
not forbid `r=1/2` either. **N8 — cross-cycle echo:** this is the same `det_C` inversion
pattern flagged repeatedly (an inverted reality-class mapping once passed a runner); blocked
here by cross-checking the landed Berezin orientation and the explicit `J` construction.

## Forbidden-import / reprove-and-cite

All facts reproven from the `C₃` primitive in the runner (numpy, 15/15): the `U_swap`
existence, `J²=+1`, `JCJ⁻¹=C²`, `[M,J]=0 ∀b`, the J-reality of `P_singlet/P_doublet`, the
absence of a within-generation `χ`, the J-symmetry of `|b|²`. McKean-Singer / KO-dimension
sign tables, the Berezin polarization, and the einselection/superselection theorems are
**comparators** only. No PDG values; `r=1/2`/`Q=2/3` named only as the empirical target this
note does **not** derive.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- [`BAE_NCG_KODIM_REAL_STRUCTURE_PARTIAL_NARROWING_NOTE_2026-05-17.md`](BAE_NCG_KODIM_REAL_STRUCTURE_PARTIAL_NARROWING_NOTE_2026-05-17.md)
- [`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
- [`KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md`](KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md)
- [`KOIDE_DOUBLET_IS_FROBENIUS_SCHUR_COMPLEX_TYPE_ORIENTATION_BOUNDED_NOTE_2026-06-07.md`](KOIDE_DOUBLET_IS_FROBENIUS_SCHUR_COMPLEX_TYPE_ORIENTATION_BOUNDED_NOTE_2026-06-07.md)

## What this note does NOT claim

- It does **not** derive `r` (either value); it shows the KO-dim/real-structure route is
  silent and the proposed hard no-go is inverted.
- It does **not** prove `Q=2/3` impossible (it shows `r=1/2` is J-allowed) **nor** that
  `Q=1` is the prediction.
- It does **not** retire or re-grade `AC_φλ`; the two admitted bits remain the open residual.
- **No** new axiom, primitive, repo vocabulary, or class tag; no PDG input. It sets **no**
  audit status.

**Independent audit required.** This note asserts no effective-status change.
