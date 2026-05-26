# Koide ρ_δ = 2/d² Dimensionless DOF-Ratio Bridge

**Date:** 2026-05-25
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/koide_rho_delta_dimensionless_dof_ratio_runner.py`](../scripts/koide_rho_delta_dimensionless_dof_ratio_runner.py)

## Claim

Given the retained `C_d` Fourier decomposition of the `d × d`
Hermitian algebra Herm_d (from the circulant character derivation
note's R1–R2), the **dimensionless** character-algebra ratio

```text
rho_delta := (real DOF of circulant phase b) / (real dim of Herm_d)
           = 2 / d²
```

is exact rational arithmetic on the retained `C_d`-symmetric circulant
Hermitian family. At `d = 3` (retained per the three-generation
structure), `rho_delta = 2 / 9` as a dimensionless real number.

The proof-walk uses only:

1. The retained Hermitian-algebra real-dimension count
   `dim_ℝ Herm_d = d²` (`d` real diagonal entries + `d (d-1) / 2`
   complex off-diagonal entries, each carrying 2 real DOF, for a total
   of `d + d (d - 1) = d²`).
2. The retained `C_d[1, 1, …, 1]` circulant trivial-isotypic
   subalgebra `H = a I + b C + b̄ C²` with `a ∈ ℝ`, `b ∈ ℂ`, supplying
   the single circulant phase parameter `b` with `dim_ℝ ℂ = 2` real
   DOF.
3. Rational arithmetic on these two integer dimensions.

This is **only** the dimensionless half of the broader linking-relation
identity. The identification of `rho_delta = 2 / d²` as a radian-valued
Berry holonomy is a **separate admission** (the radian-bridge postulate
`P` in the parent linking-relation note's §4) and is **not** addressed
by this bridge — that half is foreclosed on the current retained
surface per the two retained no-gos cited below.

This is a bounded proof-walk satisfying the auditor's explicit
"missing_bridge_theorem" hint on the parent
[`KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md`](KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md)
(`notes_for_re_audit_if_any`: "derive or cite a retained theorem
identifying rho_delta = 2/d² with the selected-line CP1 Berry holonomy
in radians"). It identifies the dimensionless ratio with a retained
real-DOF count; it does **not** identify the radian reading, which
remains conditional on postulate `P`.

## Proof-walk

| Step | Statement | Load-bearing input |
|---|---|---|
| (B1) | The retained trivial-isotypic circulant Hermitian subalgebra is `H = a I + b C + b̄ C²` with `a ∈ ℝ`, `b ∈ ℂ` | R3 (circulant character derivation) |
| (B2) | `dim_ℝ ℂ = 2` (the circulant phase parameter `b` carries 2 real DOF) | rational arithmetic |
| (B3) | `dim_ℝ Herm_d = d² = d (real diagonal) + d (d − 1) (real off-diagonal: d(d−1)/2 complex entries × 2 real each)` | retained Hermitian-matrix dimension count |
| (B4) | `rho_delta = 2 / d²` | rational arithmetic on (B2)/(B3) |
| (B5) | At `d = 3`: `rho_delta = 2 / 9` | rational arithmetic |

The proof-walk does **not** cite the Wilson plaquette action, staggered
phases, Brillouin-zone labels, link unitaries, lattice scale `u_0`, a
Monte Carlo measurement, or a fitted observational value.

## Exact arithmetic check

For general `d`:

```text
dim_ℝ Herm_d
   = d  · 1                              [diagonal entries are real]
   + d (d − 1) / 2  · 2                  [d(d−1)/2 complex off-diagonals × 2 real each]
   = d + d (d − 1)
   = d + d² − d
   = d².
```

The numerator is `dim_ℝ ℂ = 2`.

```text
rho_delta  =  2 / d².
```

At `d = 3`:

```text
rho_delta  =  2 / 9.
```

At `d = 5`: `rho_delta = 2/25`. At `d = 7`: `rho_delta = 2/49`. The
identity is rational for every positive integer `d` and matches the
parent linking-relation note's §3.2 dimensional-ratio identity I2
exactly.

## Dependencies

- [`KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md`](KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md)
  — the parent whose dimensionless identity `δ = 2 / d²` this bridge
  formally ratifies as a retained real-DOF count. The bridge does not
  address the parent's radian-reading half (postulate `P`).
- [`KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md`](KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md)
  — supplies the retained R3 circulant decomposition
  `Herm_3 = 3 · trivial ⊕ 3 · ω ⊕ 3 · ω̄` and the trivial-isotypic
  circulant Hermitian subalgebra `H = a I + b C + b̄ C²`.
- `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md`
  — retained_no_go authority documenting that the radian-reading
  identification (the half this bridge does NOT close) is **not**
  derivable from retained Cl(3)/Z³ alone.
- `KOIDE_SELECTED_LINE_LOCAL_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md`
  — companion retained_no_go on the local radian bridge.

These are imported authorities for a bounded theorem. The row remains
unaudited until the independent audit lane reviews this note, its
dependencies, and the runner.

## Boundaries

This bridge does **not** close:

- the radian-reading half of the parent identification (the dimensionless
  ratio `2 / d²` is not, by this bridge, identified with a Berry-phase
  reading in radians; that identification is precisely the postulate
  `P` of the parent linking-relation note, and it remains conditional
  / foreclosed by the cited retained no-gos);
- the equal-sector-norm input `I1` for `Q = 2 / d`;
- the joint linking relation `δ = Q / d` (which requires both I1 and
  P per the parent note);
- the ambient-`S²` completion (independently blocked by the
  bundle-obstruction theorem);
- any retained closure of the full Koide `Q = 2/3, δ = 2/9` package
  on the current retained surface.

The bridge closes the dimensionless-DOF-ratio half only. Downstream
rows that need only the dimensionless identity `rho_delta = 2/d²` can
now cite this companion directly; rows needing the radian reading must
continue to wait on postulate `P`.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/koide_rho_delta_dimensionless_dof_ratio_runner.py
```

Expected:

```text
TOTAL: PASS=7 FAIL=0
VERDICT: bounded bridge passes; rho_delta = 2 / d² is exact rational
arithmetic on the retained circulant Hermitian DOF count for all tested
d ∈ {2, 3, 4, 5, 7, 11}.
```
