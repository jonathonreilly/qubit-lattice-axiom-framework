# Dirac Singular-Value Readout Is Sign-Blind and the Chiral L-R Coupling Is Berry-Flat on the Current A_min Surface (Bounded Algebraic No-Go Support; Readout Bridge Open)

**Date:** 2026-06-05
**Type:** no_go
**Claim type:** no_go (**bounded**, computable-side). On the current A_min algebra, the Dirac block
operator is sign-blind: `D² = diag(MM†, M†M)`, so its spectrum reads singular values `|λ_k|`.
The allowed factor-crossing chiral L-R coupling `M(b)⊗σ_+` has b-independent C3-Fourier
generation eigenvectors and is Berry-flat. Therefore this algebraic route does **not** derive the
`r=1/2` signed-root Koide branch; the residual is exactly the signed-vs-singular readout choice.
It does not prove a physical readout-to-branch selection theorem, does not claim `r=1` is physically
selected, and does not claim `r=1/2` is physically excluded.
**Claim scope:** **bounded — not a hard universal no-go.** It establishes only the algebraic
flatness and sign-erasure statements for the current A_min matrix surface. It does **not** assert a
retained bridge from framework matter carriers to physical charged-lepton masses, and it does not
foreclose a future corner-realization theorem. The open residual is the genuinely unforced **sign of
`√m`** (signed-eigenvalue vs singular-value readout). The named open target is
`READOUT_TO_BRANCH_SELECTION_BRIDGE`: derive, from repo-internal admitted inputs, whether the
Berry-flat/sign-blind Dirac current-`A_min` readout selects, distinguishes, or leaves open any branch
among the distinct dial locations `r=0`, `r=1/2`, and `r=1`.
**r = 1/2 firewall:** `r = 1/2` is a stable dial setting, never forced by this note; `r = 0`, `r = 1/2`,
and `r = 1` are distinct framework locations.
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
- The physical readout-to-branch map is named as the open target
  `READOUT_TO_BRANCH_SELECTION_BRIDGE`, not supplied or denied here.
- The `r = 1/2` dial firewall is explicit: the algebraic flatness/sign-blindness
  result does not physically select `r=1` or exclude `r=1/2`.

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
   is flat** (zero Berry curvature). The block-1 escape *exists in the algebra* but **does not curve the
   generation bundle**, hence does not deliver `r=1/2` by this algebraic route.
4. **`r=1/2` needs the signed `√m` readout, which the singular-value readout erases.** At the operator Koide point
   (`s=√2`, `r=1/2`) some `√m_k = a+2|b|cos(δ+2πk/3)` are **negative** (because `2|b|>a`). The **signed** readout
   gives `Q=2/3` for all δ (runner (4a)); the **singular-value** readout gives `Q≠2/3`
   wherever an eigenvalue is negative (runner (4b)). The masses `m_k=(√m_k)²` are identical; they differ **only
   by the sign of `√m`**.

## The narrowed wall and named open target

> Narrowed wall: in the current A_min C₃-circulant matrix surface, the factor-crossing L-R coupling
> `M(b)⊗σ₊` is Berry-flat and the singular-value Dirac readout is sign-blind. This coupling class therefore
> cannot distinguish the signed `√m` orientation by generation-bundle curvature.

> Named open target: `READOUT_TO_BRANCH_SELECTION_BRIDGE` is the missing theorem deriving the physical
> readout-to-branch map, if any, for the distinct dial locations `r=0`, `r=1/2`, and `r=1`.

Thus the singular-value Dirac readout on this current matrix surface erases the sign needed by the
signed-root Koide branch; `r=1/2` is not derived by this algebraic route. This is a bounded
route-pruning result, not a retained physical-mass theorem. It does not claim `r=1` is physically selected,
and it does not claim `r=1/2` is physically excluded.

## No-Go Discipline Gate (N1-N8)

**N1 — Alternative routes against the narrowed claim:** determinant/modulus, `D²`, L-R coupling localization,
signed-vs-absolute readout, and the R³ chirality-crossing route have all been checked only against the algebraic
flatness/sign-blindness boundary. They do not supply physical readout-to-branch selection. The R³
chirality-crossing route remains bounded by the prior C₃ obstruction; `READOUT_TO_BRANCH_SELECTION_BRIDGE`
remains open.
**N2 — Wall independence:** the narrowed claim has one load-bearing wall: the tested coupling class is
Berry-flat/sign-blind. The R³ chirality-crossing obstruction is boundary context for a different coupling, and
the physical readout-to-branch bridge is an open target rather than a wall counted as resolved.
**N3 — Hidden-wall scan:** "Dirac" here is the tested block-operator readout, not an asserted retained
physical-mass bridge. The complex structure `J_cs` is named explicitly as measure-neutral, not assumed. No
branch-selection premise is hidden in the algebra.
**N4 — Residual matching:** the runner is load-bearing for the narrowed residual: algebraic
flatness/sign-blindness of `M(b)⊗σ₊`. The cited boundary notes
([`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](./KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md),
[`KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md`](./KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md),
[`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md`](./KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md))
match the residual exactly and are not used to assert the missing bridge.
**N5 — Rhetoric audit:** "r=1" language is scoped to the singular-value Dirac matrix readout on the current
A_min surface, per-operator. It is not claimed lattice-wide, retained as a physical-mass bridge, or asserted for
the open corner realization. The untested physical readout-to-branch statement is named open.
**N6 — Partial-closure scan:** the signed-`√m` readout may be a convention/definition handle or may require a
separate theorem. This note does not classify that bridge; it records `READOUT_TO_BRANCH_SELECTION_BRIDGE` as
the next target.
**N7 — Steelman:** the strongest case for `r=1/2` is that the **signed** readout *does* give `Q=2/3` exactly (the
operator sits at the Koide point for the Yukawa eigenvalues), so the physical readout *should* be the signed
Yukawa eigenvalue, not the singular value. This steelman is real and unresolved; it is exactly the named bridge
target.
**N8 — Cross-cycle echo:** signed-vs-singular readout issues recur in the Koide lane. This note preserves that
handle as open and uses the runner only for the algebraic sign-blindness/Berry-flatness boundary.

## Forbidden-import / reprove-and-cite

All four facts are reproven from the C₃-circulant matrix algebra in the runner (sympy/numpy, 6/6).
Singular-value-vs-signed, Berry-monopole, McKean-Singer are comparators only. No PDG values; `r=1/2`/`Q=2/3`
are restated only as declared Koide-lane dial/comparator labels, with no physical selection claimed.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-04.md`](./MINIMAL_AXIOMS_2026-06-04.md)
- [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](./KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
- [`KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md`](./KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md)
- [`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md`](./KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md)

Plain-text non-load-bearing context pointer: `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`
(`AC_phi_lambda`/corner realization remains open and not theorem-foreclosed).

**Independent audit required.** This note asserts no effective-status change.
