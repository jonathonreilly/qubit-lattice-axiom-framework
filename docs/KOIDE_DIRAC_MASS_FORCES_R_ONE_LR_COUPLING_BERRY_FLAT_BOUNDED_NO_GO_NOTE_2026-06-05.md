# The Dirac Generation Mass Forces r=1 on the Current Surface; the Chiral L-R Coupling Is Berry-Flat (Bounded No-Go; the Open Corner Realization Is Not Theorem-Foreclosed)

**Date:** 2026-06-05
**Type:** no_go
**Claim type:** no_go (**bounded**, computable-side). On the current A_min surface, `r = |b|²/a² = 1` (Koide
`Q=1`) is the **forced** reading of the charged-lepton generation mass, and the chiral L-R coupling localized as
the selector (the block-1 result, PR #2758) **does not reach `r=1/2`**. This **closes the open route from
block-1**: localizing the selector to a coupling does not, by itself, open `r=1/2` — the specific C₃-circulant
L-R coupling is Berry-flat.
**Claim scope:** **bounded — not a hard universal no-go.** It establishes `r=1` is forced *for the
physical (singular-value) Dirac mass on the current A_min algebra*, and that the bundle-curving coupling which
would give `r=1/2` is forbidden *within R³* by `C³=I`. It does **not** rule out a future derivation: the open
staggered-Dirac corner realization (`AC_φλ` substep-4) is **not theorem-foreclosed**, and the residual is the
genuinely un-forced **sign of `√m`** (signed-eigenvalue vs singular-value readout).
**Status authority:** independent audit lane only. No effective-status change; independent audit required.
**Runner:** [`scripts/audit_companion_koide_dirac_mass_forces_r_one_exact.py`](./../scripts/audit_companion_koide_dirac_mass_forces_r_one_exact.py)

## The four exact facts (runner 5/5)

1. **A Dirac fermion's determinant is the modulus-squared.** For the genuine Dirac operator
   `D = [[0, M],[M†, 0]]` on generation⊗{L,R}, `det D = |det M|²` (runner (1)) — second-order *by construction*.
   Only a **Weyl** fermion keeps `det M` alone (first-order). Charged leptons are Dirac, so the determinant
   route is second-order, full stop.
2. **The physical masses are singular values.** `D² = diag(MM†, M†M)` (runner (2)) → the Dirac spectrum is
   `±` the **singular values** `|λ_k|` of `M`, which are **sign-blind**.
3. **The L-R coupling `M(b)⊗σ₊` is Berry-flat.** Its generation eigenvectors are the b-independent C₃-Fourier
   modes `f_k` (runner (3)); the operator factorizes as `(Fourier mode)⊗(spinor)`, so the **generation bundle
   is flat** (zero Berry curvature) → `r=1`. The block-1 escape *exists in the algebra* but **does not curve the
   generation bundle**, hence does not deliver `r=1/2`.
4. **`r=1/2` needs the signed `√m` readout, which the physical mass erases.** At the operator Koide point
   (`s=√2`, `r=1/2`) some `√m_k = a+2|b|cos(δ+2πk/3)` are **negative** (because `2|b|>a`). The **signed** readout
   gives `Q=2/3` for all δ (runner (4a)); the **singular-value** (physical Dirac mass) readout gives `Q≠2/3`
   wherever an eigenvalue is negative (runner (4b)). The masses `m_k=(√m_k)²` are identical; they differ **only
   by the sign of `√m`**.

## The wall, named exactly

> On the current A_min surface the generation mass is the C₃-circulant `M(b)`, whose Dirac realization gives
> **singular-value (sign-blind) masses → `r=1`**. The bundle-curving coupling that would produce `r=1/2`
> (b-dependent generation eigenvectors, a nonzero Berry monopole) is **chirality-crossing within R³**, and is
> **forbidden by `C³=I`** (`comm(C)∩anticomm(Γ_χ)={0}`). The factor-crossing L-R coupling that *is* allowed
> (`M(b)⊗σ₊`) is **Berry-flat**. So `r=1/2` reduces to the **un-forced sign of `√m`** — a choice no A_min
> structure (kinetic operator, ε grading, complex structure `J_cs`, Record) fixes.

So `r=1` is forced on the current surface; `r=1/2` is not derived. This is the robust partial-falsification at
its deepest point: **the framework does not derive the charged-lepton mass ratios.**

## No-Go Discipline Gate (N1-N8)

**N1 — Alternative routes (≥5, all → r=1 or foreclosed):** modulus `Tr log(M†M)` (rank-2 → r=1, #2624);
det-extremum (r=1, r=4, never 1/2); taste-multiplicity (M₂(ℂ) simple → r=1); Connes-Lott (Schur → r=1);
ε-grading (phase-only, moves δ not r); `J_cs` (measure-neutral); Record (dimension count → r=1); native-mass
Berry (flat → r=1); **L-R coupling `M(b)⊗σ₊` (Berry-flat → r=1, this note)**; bundle-curving within R³
(forbidden by C³=I). Twelve routes; all land on r=1 or are foreclosed.
**N2 — Wall independence:** two distinct walls — (i) *within R³* the bundle-curving coupling is forbidden
(`C³=I`); (ii) *across factors* the allowed coupling is Berry-flat (factorization). They are independent (one is
a forbidding, one is a flatness). The singular-value-vs-signed residual is the *consequence*, not a third wall.
**N3 — Hidden-wall scan:** "Dirac" is forced (charged leptons are Dirac, non-circular); no "by construction"
admission beyond that. The complex structure `J_cs` is named explicitly as measure-neutral, not assumed.
**N4 — Residual matching:** the cited no-gos
([`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](./KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md),
[`KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md`](./KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md),
[`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md`](./KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md))
match the residual exactly (Berry-flat ⟺ r=1; signed-vs-singular = the sign of √m).
**N5 — Rhetoric audit:** "r=1 is forced" is scoped to **the singular-value/physical Dirac mass on the current
A_min surface**, per-operator. It is **not** claimed lattice-wide or for the open corner realization.
**N6 — Partial-closure scan:** the signed-`√m` readout is a *convention/definition* (which root of `m`), not a
new axiom — that is the import-retirement handle, recorded as the open residual, not called "new axiom required."
**N7 — Steelman:** the strongest case for `r=1/2` is that the **signed** readout *does* give `Q=2/3` exactly (the
operator sits at the Koide point for the Yukawa eigenvalues), so the physical readout *should* be the signed
Yukawa eigenvalue, not the singular value. This steelman is **real and unresolved** — hence the **bounded**
status (not a hard no-go): the sign of `√m` is the genuine open residual.
**N8 — Cross-cycle echo:** structurally similar walls (modulus, det) were not retired by any later mechanism;
the signed-vs-singular handle is the only one not yet foreclosed, and it is preserved here as open.

## Forbidden-import / reprove-and-cite

All four facts reproven from the C₃ primitive in the runner (sympy/numpy, 5/5). Singular-value-vs-signed,
Berry-monopole, McKean-Singer are comparators only. No PDG values; `r=1/2`/`Q=2/3` named only as the empirical
target this note does **not** derive.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-04.md`](./MINIMAL_AXIOMS_2026-06-04.md)
- [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](./KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
- [`KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md`](./KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md)
- [`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md`](./KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md)
- [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](./STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)

**Independent audit required.** This note asserts no effective-status change.
