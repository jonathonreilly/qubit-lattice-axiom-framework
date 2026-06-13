# Dirac Singular-Value Readout Is Sign-Blind and the Chiral L-R Coupling Is Berry-Flat on the Current A_min Surface (Bounded Algebraic No-Go Support)

**Date:** 2026-06-05
**Type:** no_go
**Claim type:** no_go (**bounded**, computable-side). On the current A_min algebra, the Dirac block
operator is sign-blind: `D² = diag(MM†, M†M)`, so its spectrum reads singular values `|λ_k|`.
The allowed factor-crossing chiral L-R coupling `M(b)⊗σ_+` has b-independent C3-Fourier
generation eigenvectors and is Berry-flat. Therefore this algebraic route does **not** derive the
`r=1/2` signed-root Koide branch; the residual is exactly the signed-vs-singular readout choice.
**Claim scope:** **bounded — not a hard universal no-go.** It establishes only the algebraic
flatness and sign-erasure statements for the current A_min matrix surface. It does **not** assert a
retained bridge from framework matter carriers to physical charged-lepton masses, and it does not
foreclose a future corner-realization theorem. The open residual is the genuinely unforced **sign of
`√m`** (signed-eigenvalue vs singular-value readout).
**Status authority:** independent audit lane only. No effective-status change; independent audit required.
**Runner:** [`scripts/audit_companion_koide_dirac_mass_forces_r_one_exact.py`](./../scripts/audit_companion_koide_dirac_mass_forces_r_one_exact.py)

## 2026-06-12 audit-scope repair

Prior scope feedback required either support for a physical-readout theorem or a narrowing to the
algebraic flatness plus signed-vs-singular residual, with the determinant sign repaired and the
unaudited staggered-gate dependency removed from closure. This note takes the narrowing route.

- The determinant fact is now sign-correct for the odd `3+3` Dirac block:
  `det [[0,M],[M†,0]] = - det(M) det(M†) = -|det M|²`. The sign is
  irrelevant to the modulus/Jacobian point, but it is not erased in the
  algebraic determinant identity.
- The live no-go is the algebraic statement that the singular-value Dirac
  readout is sign-blind and the allowed L-R coupling is Berry-flat.
- The open corner-realization reference is plain text and non-load-bearing,
  not a markdown citation dependency for this theorem.

## The four exact facts (runner 6/6)

1. **A 3-generation Dirac block determinant is the negative modulus-squared.** For the Dirac block
   operator `D = [[0, M],[M†, 0]]` on the three-generation `generation⊗{L,R}` space,
   `det D = (-1)^3 |det M|² = -|det M|²` (runner (1)). The sign is the odd-generation chiral
   block orientation; the load-bearing fact is still that the Dirac determinant is a second-order
   modulus of the Weyl determinant, not `det M` itself. Only a **Weyl** block keeps `det M` alone
   (first-order).
2. **The Dirac block singular-value readout is sign-blind.** `D² = diag(MM†, M†M)` (runner (2))
   → the Dirac block spectrum is `±` the **singular values** `|λ_k|` of `M`, which are sign-blind.
3. **The L-R coupling `M(b)⊗σ₊` is Berry-flat.** Its generation eigenvectors are the b-independent C₃-Fourier
   modes `f_k` (runner (3)); the operator factorizes as `(Fourier mode)⊗(spinor)`, so the **generation bundle
   is flat** (zero Berry curvature) → `r=1`. The block-1 escape *exists in the algebra* but **does not curve the
   generation bundle**, hence does not deliver `r=1/2`.
4. **`r=1/2` needs the signed `√m` readout, which the singular-value readout erases.** At the operator Koide point
   (`s=√2`, `r=1/2`) some `√m_k = a+2|b|cos(δ+2πk/3)` are **negative** (because `2|b|>a`). The **signed** readout
   gives `Q=2/3` for all δ (runner (4a)); the **singular-value** readout gives `Q≠2/3`
   wherever an eigenvalue is negative (runner (4b)). The masses `m_k=(√m_k)²` are identical; they differ **only
   by the sign of `√m`**.

## The wall, named exactly

> On the current A_min surface the generation mass is the C₃-circulant `M(b)`, whose Dirac realization gives
> **singular-value (sign-blind) masses → `r=1`**. The bundle-curving coupling that would produce `r=1/2`
> (b-dependent generation eigenvectors, a nonzero Berry monopole) is **chirality-crossing within R³**, and is
> **forbidden by `C³=I`** (`comm(C)∩anticomm(Γ_χ)={0}`). The factor-crossing L-R coupling that *is* allowed
> (`M(b)⊗σ₊`) is **Berry-flat**. So `r=1/2` reduces to the **un-forced sign of `√m`** — a choice no A_min
> structure (kinetic operator, ε grading, complex structure `J_cs`, Record) fixes.

So the singular-value Dirac readout on this current matrix surface erases the sign needed by the
signed-root Koide branch; `r=1/2` is not derived by this algebraic route. This is a bounded
route-pruning result, not a retained physical-mass theorem.

## No-Go Discipline Gate (N1-N8)

**N1 — Alternative routes (≥5 listed A_min algebraic routes → r=1 or foreclosed):** modulus `Tr log(M†M)` (rank-2 → r=1, #2624);
det-extremum (r=1, r=4, never 1/2); taste-multiplicity (M₂(ℂ) simple → r=1); Connes-Lott (Schur → r=1);
ε-grading (phase-only, moves δ not r); `J_cs` (measure-neutral); Record (dimension count → r=1); native-mass
Berry (flat → r=1); **L-R coupling `M(b)⊗σ₊` (Berry-flat → r=1, this note)**; bundle-curving within R³
(forbidden by C³=I). The twelve listed A_min algebraic routes land on `r=1` or are foreclosed.
**N2 — Wall independence:** two distinct walls — (i) *within R³* the bundle-curving coupling is forbidden
(`C³=I`); (ii) *across factors* the allowed coupling is Berry-flat (factorization). They are independent (one is
a forbidding, one is a flatness). The singular-value-vs-signed residual is the *consequence*, not a third wall.
**N3 — Hidden-wall scan:** "Dirac" here is the tested block-operator readout, not an asserted
retained physical-mass bridge. The complex structure `J_cs` is named explicitly as measure-neutral,
not assumed.
**N4 — Residual matching:** the cited no-gos
([`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](./KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md),
[`KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md`](./KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md),
[`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md`](./KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md))
match the residual exactly (Berry-flat ⟺ r=1; signed-vs-singular = the sign of √m).
**N5 — Rhetoric audit:** "r=1" language is scoped to **the singular-value Dirac matrix readout on
the current A_min surface**, per-operator. It is **not** claimed lattice-wide, retained as a physical
mass bridge, or asserted for the open corner realization.
**N6 — Partial-closure scan:** the signed-`√m` readout is a *convention/definition* (which root of `m`), not a
new axiom — that is the import-retirement handle, recorded as the open residual, not called "new axiom required."
**N7 — Steelman:** the strongest case for `r=1/2` is that the **signed** readout *does* give `Q=2/3` exactly (the
operator sits at the Koide point for the Yukawa eigenvalues), so the physical readout *should* be the signed
Yukawa eigenvalue, not the singular value. This steelman is **real and unresolved** — hence the **bounded**
status (not a hard no-go): the sign of `√m` is the genuine open residual.
**N8 — Cross-cycle echo:** structurally similar walls (modulus, det) were not retired by any later mechanism;
the signed-vs-singular handle is the only one not yet foreclosed, and it is preserved here as open.

## Forbidden-import / reprove-and-cite

All four facts are reproven from the C₃-circulant matrix algebra in the runner (sympy/numpy, 6/6). Singular-value-vs-signed,
Berry-monopole, McKean-Singer are comparators only. No PDG values; `r=1/2`/`Q=2/3` named only as the empirical
target this note does **not** derive.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-04.md`](./MINIMAL_AXIOMS_2026-06-04.md)
- [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](./KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
- [`KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md`](./KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md)
- [`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md`](./KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md)

Plain-text non-load-bearing context pointer: `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`
(`AC_phi_lambda`/corner realization remains open and not theorem-foreclosed).

**Independent audit required.** This note asserts no effective-status change.
