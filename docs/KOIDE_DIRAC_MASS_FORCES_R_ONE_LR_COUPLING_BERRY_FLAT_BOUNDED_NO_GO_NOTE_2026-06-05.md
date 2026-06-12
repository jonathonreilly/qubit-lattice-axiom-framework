# Dirac Current-Surface Algebraic Sign-Blindness and L-R Berry Flatness at the r=1 Branch (Bounded No-Go; Readout-to-Branch Selection Bridge Open)

**Date:** 2026-06-05
**Type:** no_go
**Claim type:** no_go (**bounded**, computable-side). Narrowed claim: for the declared C₃-circulant Dirac
current-surface mass operator `M(b)` and factor-crossing L-R coupling `M(b)⊗σ₊`, the runner proves algebraic
sign-blindness and algebraic flatness. In the tested coupling class, `det D` is modulus-squared, `D²` carries
singular-value data, the generation eigenvectors are b-independent Fourier modes, and the signed-vs-absolute
readout differs at the declared `r=1/2` Koide dial point. This coupling class cannot distinguish the signed
`√m` orientation by generation-bundle curvature. It does not prove a physical readout->branch-selection theorem,
and it does not claim `r=1` is physically selected.
**Claim scope:** **bounded — not a hard universal no-go.** It establishes only the algebraic
flatness/sign-blindness of this current `A_min` coupling class. The readout->branch-selection bridge is the named
open target `READOUT_TO_BRANCH_SELECTION_BRIDGE`: derive, from repo-internal admitted inputs, whether the
Berry-flat/sign-blind Dirac current-`A_min` readout selects, distinguishes, or leaves open any branch among the
distinct dial locations `r=0`, `r=1/2`, and `r=1`. This note neither supplies nor denies that bridge; the open
staggered-Dirac corner realization (`AC_φλ` substep-4) remains outside this theorem's claim.
**r = 1/2 firewall:** `r = 1/2` is a stable dial setting, never forced by this note; `r = 0`, `r = 1/2`, and
`r = 1` are distinct framework locations. This note concerns the declared `r = 1` branch as an algebraic branch
for the tested coupling class, not as a physically selected branch.
**Status authority:** independent audit lane only. No effective-status change; independent audit required.
**Runner:** [`scripts/audit_companion_koide_dirac_mass_forces_r_one_exact.py`](./../scripts/audit_companion_koide_dirac_mass_forces_r_one_exact.py)

## The four exact facts (runner 6/6, including source-boundary check)

1. **The declared Dirac block has a modulus-squared determinant.** For
   `D = [[0, M],[M†, 0]]` on generation⊗{L,R}, `det D = |det M|²` up to the fixed block sign (runner (1)).
   This is the algebraic determinant statement for the declared block form, not a branch-selection result.
2. **The declared singular-value readout is sign-blind.** `D² = diag(MM†, M†M)` (runner (2)), so the block
   spectrum is `±` the singular values `|λ_k|` of `M`. The runner proves sign-blindness of this readout; it does
   not identify that readout as the physical branch-selection authority.
3. **The L-R coupling `M(b)⊗σ₊` is Berry-flat.** Its generation eigenvectors are the b-independent C₃-Fourier
   modes `f_k` (runner (3)); the operator factorizes as `(Fourier mode)⊗(spinor)`, so the generation bundle is
   flat (zero Berry curvature). This is the algebraic flatness result for the tested `r=1` branch; it is not a
   physical selection result.
4. **The signed-vs-absolute readout split is visible at the `r=1/2` dial point.** At the declared operator Koide
   point (`s=√2`, `r=1/2`) some `√m_k = a+2|b|cos(δ+2πk/3)` are negative (because `2|b|>a`). The signed readout
   gives `Q=2/3` on the sampled δ checks (runner (4a)); the absolute-value readout gives `Q≠2/3` on sampled
   negative-eigenvalue checks (runner (4b)). The masses `m_k=(√m_k)²` are identical; the runner isolates the sign
   of `√m` as the readout datum not carried by the sign-blind algebra.

## The narrowed wall and named open target

> Narrowed wall: in the declared C₃-circulant current-surface algebra, the factor-crossing L-R coupling
> `M(b)⊗σ₊` is Berry-flat and the singular-value readout is sign-blind. This coupling class therefore cannot
> distinguish the signed `√m` orientation by generation-bundle curvature.

> Named open target: `READOUT_TO_BRANCH_SELECTION_BRIDGE` is the missing theorem deriving the physical
> readout->branch-selection map, if any, for the distinct dial locations `r=0`, `r=1/2`, and `r=1`. This note
> does not claim `r=1` is physically selected, and it does not claim `r=1/2` is physically excluded.

Thus the deliverable is the algebraic flatness/sign-blindness boundary for one tested coupling class. The
physical readout->branch-selection bridge remains an explicit open target.

## 2026-06-12 narrowing repair

- Physical bridge sentences identified: the prior headline, claim type, claim scope, wall paragraph, N5 wording,
  and runner summary ranged over physical readout->branch selection. They are narrowed here to the
  algebraic flatness/sign-blindness result that the runner actually checks.
- Algebraic content preserved: determinant modulus-squared, `D²` singular-value sign-blindness, Fourier-mode
  b-independence/Berry flatness for `M(b)⊗σ₊`, and the signed-vs-absolute readout split at the declared `r=1/2`
  dial point.
- Open target named: `READOUT_TO_BRANCH_SELECTION_BRIDGE` is not claimed and not denied.
- Dial firewall restored: `r=1/2` is a stable dial setting, never forced; `r=0`, `r=1/2`, and `r=1` remain
  distinct framework locations.

## No-Go Discipline Gate (N1-N8)

**N1 — Alternative routes against the narrowed claim (≥5):**
- ATTEMPTED: determinant/modulus route. Runner (1) proves the declared Dirac block has a modulus-squared
  determinant, so this route supports sign-blind algebra only.
- ATTEMPTED: `D²` route. Runner (2) proves the declared block carries singular-value data, so this route supports
  sign-blind algebra only.
- ATTEMPTED: L-R coupling localization route. Runner (3) proves the generation eigenvectors remain
  b-independent Fourier modes, so this route supplies Berry flatness, not branch selection.
- ATTEMPTED: signed-vs-absolute readout route. Runner (4a/4b) proves the sign datum matters at the declared
  `r=1/2` dial point and is absent from the absolute-value readout.
- RULED OUT BY PRIOR FOR THE R³ CHIRALITY-CROSSING COUPLING ONLY: the chirality-crossing route remains bounded
  by [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](./KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md).
  It is not used here to assert physical readout->branch selection.
- OPEN TARGET: `READOUT_TO_BRANCH_SELECTION_BRIDGE` is the named open target, not part of the negative
  claim.

**N2 — Wall independence:** the narrowed claim has one load-bearing wall: the tested coupling class is
Berry-flat/sign-blind. The R³ chirality-crossing obstruction is boundary context for a different coupling, and
the physical readout->branch-selection bridge is an open target rather than a wall counted as resolved.

**N3 — Hidden-wall scan:** the broad "physical" and branch-selection language has been removed
or demoted to the named open target. "Dirac" means the declared block form checked in runner (1)/(2). No
"by construction" admission is used as a load-bearing bridge.

**N4 — Residual matching:** the runner is load-bearing for the narrowed residual: algebraic
flatness/sign-blindness of `M(b)⊗σ₊`. The cited boundary notes
([`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](./KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md),
[`KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md`](./KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md),
[`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md`](./KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md))
remain boundary/comparator authorities only. None is used to assert the missing bridge.

**N5 — Rhetoric audit:** phrases asserting physical `r=1` selection have been replaced by "the specified coupling
class is Berry-flat/sign-blind." The untested physical readout->branch-selection statement is named open.

**N6 — Partial-closure scan:** the signed-`√m` readout may be a convention/definition handle or may require a
separate theorem. This note does not classify that bridge; it records `READOUT_TO_BRANCH_SELECTION_BRIDGE` as the
next target.

**N7 — Steelman:** a reviewer can argue that the signed Yukawa eigenvalue, not the absolute value, is the relevant
readout because it hits the `Q=2/3` comparator in the checked signed-readout samples at the declared `r=1/2` dial
point. That objection is not answered by the flatness runner; it is exactly the named bridge target.

**N8 — Cross-cycle echo:** signed-vs-singular readout issues recur in the Koide lane. This note preserves that
handle as open and uses the runner only for the algebraic sign-blindness/Berry-flatness boundary.

## Forbidden-import / reprove-and-cite

All four algebraic facts are reproven from the C₃ primitive in the runner (sympy/numpy, 6/6 including the
source-boundary check). Singular-value-vs-signed, Berry-monopole, McKean-Singer are comparators only. No PDG
values; the existing `r=1/2`/`Q=2/3` labels are restated only as declared Koide-lane dial/comparator labels, with
no physical selection claimed.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-04.md`](./MINIMAL_AXIOMS_2026-06-04.md)
- [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](./KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
- [`KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md`](./KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md)
- [`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md`](./KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md)
- [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](./STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)

**Independent audit required.** This note asserts no effective-status change.
