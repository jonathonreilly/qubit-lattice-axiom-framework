# DM Neutrino Bosonic Normalization — Observable-Principle Bridge Narrow Theorem

**Date:** 2026-05-16
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/audit_companion_dm_neutrino_bosonic_normalization_observable_principle_bridge_exact_2026_05_16.py`](../scripts/audit_companion_dm_neutrino_bosonic_normalization_observable_principle_bridge_exact_2026_05_16.py)
**Claim scope:** the standalone finite-dimensional bridge implication that,
for the explicit matrix-algebra setup `Y = P_R Γ_1 P_L` on `C^16` with
`Γ_1` a Hermitian involution and `P_{L,R} = (I ± γ_5)/2` the chiral
projectors, the canonical Frobenius bridge ratio
`sqrt(Tr(Y^† Y) / Tr(Γ_1^† Γ_1)) = 1/sqrt(2)` is the exact ratio of the
raw chiral bridge to its real-symmetric Hermitian completion
`Γ_1 = Y + Y^†`. The scalar-baseline determinant identities
`det(mI+jY)=m^16` and `det(mI+jΓ_1)=(m^2-j^2)^8` are recorded only as
diagnostics on the auxiliary scalar baseline `mI`; they are not claimed to
be the real-D observable-principle response `det(D+jΓ_1)/det(D)`. The
active-space ratio `sqrt(Tr(Y^†Y)/Tr(P_L)) = 1` is recorded only as a
comparator because `P_L` is not the Hermitian completion. This row does
**not** apply the observable-principle real-D uniqueness theorem to either
`Y` or `Γ_1`, and does **not** by itself prove the physical readout
`y_ν^(0)/g_weak = 1/sqrt(2)`. This is purely a statement about
finite-dimensional matrix algebra on `C^16`. No PDG comparator enters, no
continuum identification is claimed, no Hermitian-Hamiltonian bridge is
imported, no Majorana / `Z_3` activation law is consumed.

**Scope role:** Narrow rescope of the bridge-selection
algebraic core of the parent
`dm_neutrino_bosonic_normalization_theorem_note_2026-04-15` row,
isolating the finite bridge-selection algebra from the prior
observable-principle-admissibility language and from the downstream
Schur-suppression and Majorana / `Z_3` activation content of the parent
cluster.

**Scope repair:** The binding claim is narrowed away from the prior
source-domain overreach. The scalar-baseline determinant calculations for
`mI+jY` and `mI+jΓ_1` remain exact diagnostics, but neither is treated as
an observable-principle source-domain theorem. The theorem conclusion is
only the finite Frobenius raw-to-Hermitian-completion ratio. The physical
`y_ν^(0)/g_weak` readout is also firewalled as downstream interpretation
requiring a separate readout authority.

## Statement

Let `Γ_1` be a Hermitian involutive matrix on `V = C^16`
(`Γ_1 = Γ_1^†`, `Γ_1^2 = I_{16}`), and let `γ_5` be the chirality
operator on `V` (Hermitian, involutive, anticommuting with `Γ_1`).
Define the chiral projectors

```text
P_L  :=  (I_{16} + γ_5) / 2,        P_R  :=  (I_{16} - γ_5) / 2,        (P)
```

so that `P_L^2 = P_L`, `P_R^2 = P_R`, `P_L P_R = P_R P_L = 0`, and
`P_L + P_R = I_{16}`. Define the raw chiral bridge and its Hermitian
completion:

```text
Y  :=  P_R Γ_1 P_L  on  V,                                              (Y)
Y + Y^†  =  Γ_1                       (Hermitian-completion identity).  (H)
```

Fix the following finite input:

**(F) Finite-dimensional bridge algebra on `C^16`.** With `Γ_1`
Hermitian-involutive and `γ_5` Hermitian-involutive-anticommuting with
`Γ_1`, the following four identities hold by direct matrix algebra on
`V = C^16`:

```text
Y^2  =  0                              (raw chiral bridge nilpotency)   (N)
Y + Y^†  =  Γ_1                        (Hermitian completion)           (H)
Tr(Γ_1^† Γ_1)  =  Tr(I_{16})  =  16    (Hermitian involution trace)     (T1)
Tr(Y^† Y)     =  Tr(P_L Γ_1 P_R Γ_1 P_L)  =  8                          (T2)
```

(N) follows from `P_L P_R = 0` and `P_R P_L = 0`. (H) follows from the
anticommutation `{γ_5, Γ_1} = 0`: `Y^† = P_L Γ_1 P_R`,
`Γ_1 P_L = P_R Γ_1`, and `Γ_1 P_R = P_L Γ_1`, hence
`Y + Y^† = (P_R + P_L) Γ_1 = Γ_1`. (T1) is the trace of the identity.
(T2) is computed exactly in the runner via direct sympy matrix
multiplication on a canonical `C^16` representation of `(γ_5, Γ_1)`
satisfying the above identities.

### Conclusion

Under the finite matrix setup (F), the theorem conclusion is:

**(C) Canonical bridge ratio is `1/sqrt(2)`, not `1`.** Combining (T1)
and (T2),

```text
sqrt( Tr(Y^† Y) / Tr(Γ_1^† Γ_1) )  =  sqrt( 8 / 16 )  =  1 / sqrt(2).   (R)
```

The active-space ratio `Tr(Y^† Y) / Tr(P_L)` evaluates to `1` on the
standard `Tr(P_L)=8` normalization, but it compares the raw bridge to a
projector rather than to the Hermitian completion. The canonical finite
bridge ratio is therefore

```text
raw-to-Hermitian-completion ratio  =  1 / sqrt(2).                       (U)
```

The following scalar-baseline determinant identities are exact
diagnostics only; they are not asserted to be real-D
observable-principle responses.

**(D1) Raw chiral bridge is scalar-baseline nilpotent.** On the
auxiliary scalar baseline `m I + j Y` with small real `j`, the
determinant satisfies

```text
det(m I_{16} + j Y)  =  m^{16}                                          (DZ)
```

identically in `j`, hence

```text
W_scalar[j Y]  =  log|m^{16}|  -  log|m^{16}|  =  0                    (WZ)
```

identically in `j`. This exact nilpotent calculation is a diagnostic
matrix identity, not an application of a real-D source-domain theorem to
`Y`.

**(D2) Hermitian completion has a nontrivial scalar-baseline determinant
surface.** On the auxiliary scalar baseline `m I + j Γ_1`,

```text
det(m I_{16} + j Γ_1)  =  (m^2 - j^2)^8                                 (DG)
W_scalar[j Γ_1]  =  log|(m^2 - j^2)^8|  -  log|m^{16}|
                 =  8 · log|1 - j^2 / m^2|.                             (WG)
```

This is an exact scalar-baseline diagnostic on `mI`. This note does not
prove that replacing a real-D block `D` by `mI` is legitimate, and does
not claim `det(D+jΓ_1)/det(D)` equals the displayed scalar-baseline form.

Interpreting this ratio as the physical readout
`y_ν^{(0)} / g_weak = 1/sqrt(2)` requires a separate readout bridge not
supplied by this narrow theorem.

This is the bridge-selection narrow statement. Outside scope: deriving
the downstream `T_1` Schur-suppression coefficient, deriving the
Majorana / `Z_3` activation law, or extending to non-real-D blocks.

## Proof

Pure finite-dimensional matrix algebra on `C^16`.

**Step 1 — `Y^2 = 0`.** From (P), `P_L P_R = 0` (and `P_R P_L = 0`).
Hence `Y^2 = (P_R Γ_1 P_L)(P_R Γ_1 P_L) = P_R Γ_1 (P_L P_R) Γ_1 P_L
= 0`. (Runner verifies on the canonical `C^16` representation.)

**Step 2 — `Y + Y^† = Γ_1`.** Compute `Y^†` using `(P_R Γ_1 P_L)^† =
P_L^† Γ_1^† P_R^† = P_L Γ_1 P_R` (using `P_L^† = P_L`, `P_R^† = P_R`,
`Γ_1^† = Γ_1`). So

```text
Y + Y^†  =  P_R Γ_1 P_L  +  P_L Γ_1 P_R.
```

Using `{γ_5, Γ_1} = 0`, one has `Γ_1 P_L = P_R Γ_1` and
`Γ_1 P_R = P_L Γ_1`. Substituting,

```text
P_R Γ_1 P_L  =  P_R P_R Γ_1  =  P_R Γ_1,
P_L Γ_1 P_R  =  P_L P_L Γ_1  =  P_L Γ_1,
Y + Y^†      =  (P_R + P_L) Γ_1  =  Γ_1.
```

**Step 3 — `det(m I + j Y) = m^{16}` identically in `j`.** Because
`Y^2 = 0`, the matrix `j Y` is nilpotent for any real `j`. The
determinant of `m I + j Y` is unchanged by adding a nilpotent that
commutes with itself (more directly: the characteristic polynomial of a
strictly upper-triangular-in-some-basis nilpotent matrix is `x^{16}`,
so all eigenvalues of `j Y` are zero and `det(m I + j Y) = m^{16}`).
Therefore `W_scalar[j Y] = log|m^{16}| - log|m^{16}| = 0` identically
in `j`, as claimed in (WZ). Runner verifies at exact sympy precision by
expanding `det(m I_{16} + j Y_{C^{16}})` as a polynomial in `j` and
checking all `j`-power coefficients above the leading `m^{16}` vanish.

**Step 4 — `det(m I + j Γ_1) = (m^2 - j^2)^8`.** Because `Γ_1^2 = I`,
the eigenvalues of `Γ_1` on `V = C^16` are each `±1`. The number of
`+1` eigenvalues is `dim ker(Γ_1 - I)` and the number of `-1`
eigenvalues is `dim ker(Γ_1 + I)`. Because `Γ_1` is a Hermitian
involution with `Tr Γ_1 = 0` on the canonical `C^16` representation
(verified in the runner), the two eigenspaces have equal dimension 8.
Therefore

```text
det(m I + j Γ_1)  =  prod_k (m + j λ_k)
                 =  (m + j)^8 (m - j)^8
                 =  (m^2 - j^2)^8.
```

Hence `W_scalar[j Γ_1] = 8 log|1 - j^2/m^2|`, as claimed in (WG).
Runner verifies this at exact sympy precision via the characteristic
polynomial of `Γ_1`.

**Step 5 — scope boundary for the scalar baseline.** Steps 3 and 4 are
exact diagnostics for the auxiliary scalar baseline `mI`. They do not
prove a real-D determinant response along `Γ_1`, and they do not use any
observable-principle source-domain theorem. The load-bearing theorem
conclusion below is therefore the Frobenius raw-to-Hermitian-completion
ratio, not a real-D `W`-response statement.

**Step 6 — trace ratios `8` and `16`.** Direct computation:
`Tr(Γ_1^† Γ_1) = Tr(I_{16}) = 16` (since `Γ_1^2 = I`).
`Tr(Y^† Y) = Tr(P_L Γ_1 P_R Γ_1 P_L)`. Using `Γ_1 P_R = P_L Γ_1`
(Step 2 derivation) and `Γ_1 P_L = P_R Γ_1`,

```text
P_L Γ_1 P_R Γ_1 P_L  =  P_L (P_L Γ_1) Γ_1 P_L
                    =  P_L P_L Γ_1^2 P_L
                    =  P_L · I · P_L
                    =  P_L.
```

Hence `Tr(Y^† Y) = Tr(P_L) = 8` on the canonical `C^16` representation
(where `P_L` projects onto the left-chiral 8-dimensional subspace).
Runner verifies `Tr(P_L) = 8` and `Tr(P_R) = 8` symbolically.

**Step 7 — collecting.** By Step 6,
`sqrt(Tr(Y^† Y) / Tr(Γ_1^† Γ_1)) = sqrt(8/16) = 1/sqrt(2)`. This is the
canonical raw-to-Hermitian-completion ratio on the finite `C^16` bridge
packet. The active-space ratio `Tr(Y^† Y) / Tr(P_L) = 8/8 = 1` is
recorded only as a trace comparator: it uses the chiral projector
denominator rather than the Hermitian-completion denominator `Γ_1`. ∎

## Derivable corollaries

**(R1) Active-space comparator is only a comparator.** The active-space
ratio `1` remains a mathematically exact trace comparator, but this row
does not identify it as a scalar-baseline normalization because the
denominator `P_L` is not the Hermitian-completion denominator.

**(R2) Hermitian-completion is the finite bridge denominator used here.**
The identity `Y + Y^† = Γ_1` (Step 2) supplies the Hermitian completion
used by this row. The pseudoscalar companion
`i(Y - Y^†)` also satisfies `(i(Y - Y^†))^2 = Γ_1^2 = I` (verifiable in
the runner), but it is trace-orthogonal to `Γ_1` and is not used in the
scalar bridge ratio (R).

Both corollaries follow algebraically from the proof.

## What this claims

- The finite bridge theorem
  `sqrt(Tr Y^† Y / Tr Γ_1^† Γ_1) = 1/sqrt(2)` from the matrix setup
  (F).
- The scalar-baseline diagnostic identities
  `det(mI+jY)=m^16` / `W_scalar[j Y]=0` and
  `W_scalar[j Γ_1] = 8 log|1 - j^2/m^2|`.
- The two derived corollaries (R1), (R2).
- The exact raw-to-Hermitian-completion Frobenius ratio `1/sqrt(2)` on
  the finite `C^16` bridge packet.

## What this does NOT claim

- Does **not** apply the observable-principle block-local uniqueness
  theorem to `Y`, `Γ_1`, or the scalar baseline `mI`.
- Does **not** derive or use a real-D determinant response along
  `Γ_1`; the determinant identities in this note are scalar-baseline
  diagnostics only.
- Does **not** derive the second-order coefficient
  `y_ν^eff = g_weak^2 / 64` of the bridge (this is the Schur-suppression
  content carried by the downstream cluster, outside this narrow theorem).
- Does **not** prove the physical readout
  `y_ν^{(0)} / g_weak = 1/sqrt(2)`; it proves only the finite-block
  raw-to-Hermitian-completion Frobenius ratio that a later readout
  authority may consume.
- Does **not** derive the Majorana / `Z_3` activation law or any
  three-generation `A/B/ε` structure or the full `η` benchmark.
- Does **not** identify `Γ_1` with any specific physical Hamiltonian
  beyond the Hermitian-involutive bridge structure on `C^16`.
- Does **not** import any PDG observed value, literature numerical
  comparator, fitted selector, or unit convention.
- Does **not** update the parent
  `dm_neutrino_bosonic_normalization_theorem_note_2026-04-15` row; this
  narrow theorem is a separate, narrower row.
- Does **not** claim a continuum limit or any effective-action
  statement. The statement is finite-block algebraic on `C^16`.
- Does **not** extend the scalar-baseline diagnostics to non-scalar
  Dirac blocks; that would require a separate determinant-response
  theorem.

## Relation to the parent DM neutrino bosonic normalization note

The parent
`dm_neutrino_bosonic_normalization_theorem_note_2026-04-15` row bundles
the bridge-selection algebraic content with several distinct
downstream items:

1. The observable-principle admissibility premise as a load-bearing
   domain input.
2. The downstream `T_1` Schur-suppression second-order coefficient.
3. The full denominator surface for the leptogenesis kernel rebuild.
4. The pure bridge-selection algebraic substitution on
   `Y, Γ_1, P_{L,R}` on `C^16` with `Γ_1` Hermitian involutive.

This narrow theorem isolates the finite matrix part of item 4 from
items 1-3. The observable-principle uniqueness theorem and the real-D
structural note are not load-bearing premises of this repaired row. No
downstream Schur content is imported and no full-denominator surface is
claimed.

## Open derivation gap

Out of scope of this narrow theorem (downstream items, to be carried
by separate authorities):

- Derivation of the second-order coefficient `y_ν^eff = g_weak^2 / 64`
  (Schur-suppression content; see
  `dm_neutrino_schur_suppression_theorem_note_2026-04-15` for the
  parent cluster's record).
- Derivation of the full leptogenesis kernel after rewriting in the
  transfer law.
- Derivation of the Majorana / `Z_3` activation law and its three-
  generation `A/B/ε` structure.
- Extension from the scalar baseline `mI` to a non-scalar real-D block.
- Numerical PDG matching of the resulting `η` benchmark.

## Cited dependencies

No load-bearing ledger dependencies. The finite-dimensional matrix
algebra on `C^16` is verified at exact sympy precision by the companion
runner.

## Forbidden imports check

- No PDG observed values consumed.
- No literature numerical comparators consumed.
- No fitted selectors consumed.
- No unit conventions load-bearing on the claim.
- No same-surface family arguments.

## Validation

Primary runner:
[`scripts/audit_companion_dm_neutrino_bosonic_normalization_observable_principle_bridge_exact_2026_05_16.py`](../scripts/audit_companion_dm_neutrino_bosonic_normalization_observable_principle_bridge_exact_2026_05_16.py)
verifies at exact sympy precision on the canonical `C^16` representation
of `(γ_5, Γ_1)`:

1. (F.N) `Y^2 = 0` exactly on `C^16` (matrix-equality reduction).
2. (F.H) `Y + Y^† = Γ_1` exactly on `C^16`.
3. (F.T1) `Tr(Γ_1^† Γ_1) = 16` symbolically.
4. (F.T2) `Tr(Y^† Y) = 8` symbolically.
5. (DZ) `det(m I_{16} + j Y) = m^{16}` identically in `j` and `m`
   (polynomial-coefficient match: all `j`-power coefficients above
   `j^0 · m^{16}` are zero in the sympy expansion).
6. (DG) `det(m I_{16} + j Γ_1) = (m^2 - j^2)^8` identically in `j` and
   `m` (polynomial-coefficient match).
7. (WG) `W_scalar[j Γ_1] = 8 log|1 - j^2/m^2|` evaluated on the scalar
   baseline at small rational `j` and verified equal to the closed-form
   prediction.
8. (R) `sqrt(Tr(Y^† Y) / Tr(Γ_1^† Γ_1)) = 1/sqrt(2)` symbolically.
9. (R1) active-space ratio `Tr(Y^† Y) / Tr(P_L) = 1` symbolically, and
   the corollary statement that it is a trace comparator rather than the
   Hermitian-completion denominator ratio.
10. (R2) pseudoscalar companion `i(Y - Y^†)` is a Hermitian
    companion with the same magnitude trace norm and is orthogonal to
    `Γ_1` in the trace inner product.
11. Counterfactual: a non-anticommuting candidate `Γ̃_1` (with
    `[γ_5, Γ̃_1] ≠ 0`) breaks Step 2's `Y + Y^† = Γ̃_1` identity,
    confirming `{γ_5, Γ_1} = 0` is load-bearing.

The companion runner is exact-symbolic (sympy `simplify` and
matrix-entry equality), with no floating-point tolerances on the
load-bearing identities.

## Cross-references

Load-bearing dependencies: none.

Context-only references (not load-bearing dependencies of this note;
named by `claim_id` in backticks rather than via markdown link, so the
citation graph does not register them as outgoing edges from this
narrow theorem):

- `dm_neutrino_bosonic_normalization_theorem_note_2026-04-15` — parent
  bundled note whose bridge-selection step this narrow theorem isolates
  as finite `C^16` matrix algebra.
- `dm_neutrino_veven_bosonic_normalization_theorem_note_2026-04-15` —
  sibling row using the same bridge structure on the even channel.
- `dm_neutrino_k00_bosonic_normalization_theorem_note_2026-04-15` —
  sibling row using the same bridge structure.
- `dm_neutrino_schur_suppression_theorem_note_2026-04-15` — downstream
  second-order coefficient note; not imported here.
- `observable_principle_real_d_block_uniqueness_narrow_theorem_note_2026-05-10`
  — context for the prior overbroad source-response reading; not imported
  by this repaired theorem.
- `cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10` —
  context for the prior real-D reading; not imported by this repaired
  theorem.
