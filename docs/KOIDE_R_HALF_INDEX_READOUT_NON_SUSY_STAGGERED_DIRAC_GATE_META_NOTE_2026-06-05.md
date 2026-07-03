# The Koide r=1/2 Index Readout Does Not Require SUSY — It Is Gated on the Staggered-Dirac Realization (Foreclosure-Correction + Localization)

**Date:** 2026-06-05
**Type:** meta route-boundary note
**Claim type:** meta

The Koide magnitude `r = |b|²/a² = 1/2` (Q=2/3) needs the C₃ doublet counted **once** (the multiplicity/index
readout, block weighting `(singlet,doublet)=(1,1)`); the modulus/energy readout counts the doublet's
**two** real modes `(1,2)` → `r=1`. This note **corrects** the prior framing that the "count once"
route requires a SUSY superpotential: that conflates the holomorphic **action** (a superpotential,
which needs SUSY — Seiberg) with the holomorphic **readout** (the ordinary Dirac-fermion determinant /
the index). The supertrace/index "count once" is a **Z₂-graded-Dirac** fact (McKean-Singer:
`ind D = Str(e^{−tD²})` for any Dirac operator with a chirality grading, **no supercharge**), realized
on the lattice for Kähler-Dirac/staggered fermions. The local runner checks both finite ingredients
used by this boundary test: the chirality grading `ε` and the Schur-native flavor complex structure
`J_cs=(C−C²)/√3`.
**Claim scope:** this is **not a derivation of `r = 1/2`**. The native pieces are
**necessary-not-sufficient**: `J_cs` is **measure-neutral** (`exp(θ J_cs)=SO(2)` preserves *both* the
real `det_R` and holomorphic `det_C` measures), so the static `ε`/`J_cs`
ingredients checked here do not **select** the count. The selector is
**first-order** (Dirac/Berezin index, count once → `r=1/2`) vs **second-order**
(modulus/energy, count twice → `r=1`) — a **dynamics** question gated on the open staggered-Dirac
corner realization (`AC_φλ`). The contribution here is to **remove SUSY as a blocker** and **localize**
the open atom to that gate.
**Status authority:** independent audit lane only. This source note does not
assert an audit verdict or effective-status change.
**Runner:** [`scripts/audit_companion_koide_r_half_index_readout_non_susy_gated_exact.py`](../scripts/audit_companion_koide_r_half_index_readout_non_susy_gated_exact.py)

## The correction: the index "count once" is non-SUSY

The standing obstacle to `r=1/2` was the fork (`KOIDE_BEREZIN_DETC_VS_DETR_FORK`): the doublet counted
**holomorphically** (once) gives `r=1/2`; counted by **real dimension** (twice) gives `r=1`; and every
real/non-holomorphic energy functional gives the dimension count (rank-2 Hessian → `r=1`; see
[`KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md`](./KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md)). The
holomorphic count was believed to require a SUSY superpotential.

That is too strong, on three standard facts:

1. **Supertrace = a Z₂-graded trace, not SUSY.** `Str(·)=Tr(ε·)` is defined from a Z₂-grading alone.
   **McKean-Singer:** for a Dirac operator `D` anticommuting with a chirality grading `ε`,
   `ind D = Str(e^{−tD²})` for all `t>0` (nonzero modes pair `±`-chirality and cancel). No supercharge
   enters — SUSY QM (Witten 1982) is the *repackaging* of this index, not a prerequisite. Runner (3).
2. **Index → multiplicity; trace → dimension.** The equivariant/G-index lands in the representation
   ring `R(C₃)` with integer **multiplicities**: each irrep of the 3-corner regular rep appears
   **once** → `(triv,ω,ω̄)=(1,1,1)` → `(singlet,doublet)=(1,1)` → `r=1/2`. A plain trace returns the
   **dimension** `χ(e)=(1,2)` → `r=1`. The "count once" is the *natural output of an index/character*,
   needing only a group action and a graded operator. Runner (2).
3. **A holomorphic *readout* needs only a complex structure, not a holomorphic action.** The
   Dolbeault index / holomorphic Euler characteristic counts holomorphic modes from a complex/Kähler
   structure alone (HRR); Seiberg-holomorphy gates the *superpotential*, an object the framework does
   not need. The ordinary **Dirac** (complex) fermion determinant `det M` is holomorphic and counts
   each mode once — no SUSY.

So the checked local structure — `ε` (a Z₂ chirality grading) and `J_cs=(C−C²)/√3` (a
Schur-native flavor complex structure, runner (4a)) — is in principle **enough** to *define* the index
readout. **SUSY is not required.**

## The remaining gate: the selector is dynamics, not static structure

Having the ingredients is **not** selecting the count. The decisive local obstruction is **measure
neutrality** (runner (4b)): `J_cs` restricted to the doublet acts as a genuine complex structure
(`J²=−1`), but `exp(θ J_cs)=SO(2)` is orthogonal with `det=1` — an automorphism of **both** the real
and the holomorphic measure. The static complex structure checked here does not distinguish the two
counts it is simultaneously compatible with. Likewise `ε` is **phase-only** for the magnitude (it moves the
determinant *phase* `δ`, not the modulus that sets `r` in
[`KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md`](./KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md)),
and the dimension-count readout in the fork returns the
**dimension** count (`log|det| = log|λ_s| + 2 log|λ_d|`, → `r=1`).

What is left is a genuine **dynamics** choice:

> Is the charged-lepton generation determinant **first-order** (a Dirac/Berezin / Kähler-Dirac index,
> counting the doublet mode **once** → `r=1/2`) or **second-order** (the fluctuation modulus / effective
> potential, counting it **twice** → `r=1`)?

This is decided by the **staggered-Dirac corner realization** — the open `AC_φλ` gate
(`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03`). The index option is structurally available to a
Kähler-Dirac/staggered fermion (which the framework's generation sector is) **without SUSY**; whether
the framework's specific realization *delivers* the first-order index is the un-foreclosed question.

## Net

| statement | status |
|---|---|
| `r=1/2` = the index/multiplicity (count-once) readout | exact fork (runner (1),(2)) |
| that readout requires SUSY | **FALSE — corrected** (McKean-Singer; Dolbeault; Kähler-Dirac index) |
| `ε`, `J_cs` suffice to *define* the index readout | yes (runner (3),(4a)) |
| `ε`/`J_cs` *select* the count | **no — `J_cs` measure-neutral, `ε` phase-only** (runner (4b)) |
| which readout sets the masses | **open — gated on the staggered-Dirac corner realization** |

So `r=1/2` is **not** SUSY-blocked and is **not selected by the static `ε`/`J_cs` ingredients checked here**; it is **localized** to a
single dynamics gate: does the staggered-Dirac realization give the first-order (index) or second-order
(modulus) generation determinant. This sharpens the one open atom and identifies the next attack (the
Kähler-Dirac index of the generation operator); it does **not** by itself derive `r=1/2`.

## Forbidden-import / reprove-and-cite discipline

- The fork, the multiplicity/dimension counts, the McKean-Singer t-independence, and the `J_cs`
  measure-neutrality are **reproven** from the C₃ primitive in the runner (sympy, 7/7 exact).
- McKean-Singer, Dolbeault/HRR, the Kähler-Dirac/staggered index theorems, and Seiberg holomorphy are
  **comparators** only (they establish *non-SUSY availability*; they are not derivation inputs).
- No PDG values appear; `r=1/2` is named only as the empirical target the index reading would meet and
  this note does **not** derive.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
- [`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`](./KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
- [`SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md`](./SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md)
- [`KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md`](./KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md)
- [`KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md`](./KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md)
- [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](./STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)

**Independent audit required.** This note asserts no effective-status change.
