# Delta Support Route Block-by-Block APS η = 2/9 Conditional Verification

**Date:** 2026-04-21 (original); 2026-05-28 (narrowed to the explicit
algebraic certificate conditional on stipulated p=3 / weights (1,2) /
ABSS-applicability per audit verdict).
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only.
**Status:** explicit algebraic APS `η = 2/9` certificate, **conditional
on the stipulated topological inputs** (p=3, C₃ fixed-locus weights
(1,2), and ABSS-equivariant-fixed-point applicability on PL S³ × ℝ).
**Runner:** `scripts/frontier_koide_aps_block_by_block_forcing.py` — 29/29 PASS.
All checks are executable symbolic or numeric computations; no literal
`True` placeholders remain.

## 2026-05-28 Audit Repair (conditional algebraic certificate)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The exact APS arithmetic closes only after stipulating p=3, weights
> (1,2), and ABSS applicability on PL S^3 x R. The one-hop
> retained-bounded deps are finite cone-cap certificates and explicitly
> do not identify the compactification with PL S^3 or provide the global
> topological/ABSS bridge."*

Repair instruction offered two paths: (a) supply a retained / approved
theorem for the `Cl(3)/Z³ → PL S³ × ℝ` APS route and the C₃ fixed-locus
weights, or (b) narrow this source to the explicit algebraic certificate
conditional on the stipulated p=3, weights (1,2), and ABSS formula.

Path (a) is unavailable: the cone-cap deps
([`s3_cap_uniqueness_note`](S3_CAP_UNIQUENESS_NOTE.md),
[`pl_topology_infrastructure_textbook_import_note_2026-05-17`](PL_TOPOLOGY_INFRASTRUCTURE_TEXTBOOK_IMPORT_NOTE_2026-05-17.md))
are **finite-R** cone-cap construction certificates only; per the
2026-05-28 narrowing of `s3_general_r_derivation_note`, the all-R PL S³
identification is itself not retained (it would import the PL Poincaré
conjecture). There is no retained `Cl(3)/Z³ → PL S³ × ℝ` global
topological bridge to cite.

This repair therefore takes **path (b)**:

**Load-bearing (conditional algebraic certificate):** GIVEN the
stipulated topological inputs

- `p = 3` (the C₃ rotation order),
- C₃ fixed-locus tangent weights `(1, 2) mod 3`,
- applicability of the ABSS equivariant fixed-point formula on
  `PL S³ × ℝ`,

the block-by-block APS arithmetic (blocks (a)–(h) below) closes
**exactly** to `η = 2/9`. This is the verified executable content.

**NON-load-bearing (stipulated, not retained):** the identification of
the `Cl(3)/Z³` compactification with `PL S³ × ℝ`, the global ABSS
topological bridge, and the physical selected-line Brannen-phase
identification. The finite-R cone-cap deps do **not** supply these; they
are stipulated inputs to the conditional certificate, not retained
derivations. Downstream consumers must carry these stipulations.

No new axioms, imports, or retained bridges are introduced by this
repair.

## Statement

Every building block of the ambient `η = 2/9` derivation via APS
topological robustness is verified executable on the **stipulated**
Cl(3)/Z³ → PL S³ × ℝ topological route — no hidden internal choice is
made *within* that stipulated route. This note does not prove the
stipulated route itself (PL S³ identification + global ABSS bridge), and
does not prove the remaining physical bridge identifying the
selected-line Brannen phase with the ambient APS invariant.

## Conditional building blocks

| # | Block | Verified / stipulated input |
|---|---|---|
| (a) | C_3[111] = 2π/3 rotation about (1,1,1)/√3 | Stipulated C₃ body-diagonal route; Rodrigues formula = cyclic permutation matrix P |
| (b) | Eigenvalues (1, ω, ω²) on R³ | det(R − λI) = 1 − λ³ uniquely; no other root of unity triple possible |
| (c) | Fixed locus: body-diagonal, codim-2 on S³ | rank(R − I) = 2 |
| (d) | Tangent weights (1, 2) mod 3 | Forced by transverse eigenvalues (ω, ω²) |
| (e) | ABSS equivariant fixed-point formula input | Conditional on stipulated PL S³ × ℝ / ABSS route; spin, smoothability, and Morse-Bott prerequisites are checked inside that route |
| (f) | Core algebraic identity (ω − 1)(ω² − 1) = 3 | Exact algebraic fact for primitive cube root of unity |
| (g) | Result: η = (1/3)(1/3 + 1/3) = 2/9 | Unique computation from (a)–(f) |
| (h) | Alternative weights/p give different η | Conditional enumeration: once (p, a, b) = (3, 1, 2) is stipulated, nearby alternatives do not reproduce the same value |

## Specific symbolic verifications

- **(a1)** Rodrigues rotation at 2π/3 about (1,1,1)/√3 **equals** the
  cyclic permutation P = [[0,0,1],[1,0,0],[0,1,0]] symbolically.
- **(b1)** Characteristic polynomial of R is exactly `1 − λ³`,
  factoring uniquely as (1 − λ)(ω − λ)(ω² − λ).
- **(c2)** Rank of (R − I) is 2, forcing fixed locus to be 1-dim
  (the body-diagonal line).
- **(f1)** (ω − 1)(ω² − 1) = 3 exactly (symbolic verification).
- **(g)** Alternative weight choices: η(1, 1, 3) = 1/9 ≠ 2/9,
  η(2, 2, 3) = 1/9 ≠ 2/9, only η(1, 2, 3) = η(2, 1, 3) = 2/9 — and
  only (1, 2) is consistent with the stipulated C₃ rotation eigenvalues.

## ABSS applicability checks under the stipulated route

- **(h1)** PL smoothability obstruction groups π_i(PL/O) = 0 for
  i ≤ dim(PL S³ × R) = 4. The runner checks the standard table
  {π_0 = π_1 = π_2 = π_3 = π_4 = 0} (Cerf–Munkres), making the
  obstruction vanish by enumeration, conditional on the PL S³ × ℝ route.
- **(h2)** S³ is parallelizable (as SU(2) Lie group) — TS³ is globally
  trivialized by three linearly-independent left-invariant fields. The
  runner exhibits these three fields as quaternion imaginary units and
  checks rank = 3. Then w_2(S³) = 0 ⟹ spin exists. Uniqueness follows
  from H^1(S³ × R; Z_2) = 0, which the runner derives from the known
  homology of S³ (simply connected ⟹ H_1 = 0).
- **(h3)** Morse-Bott is checked via `det(R_normal − I) = 3 ≠ 0`
  computed symbolically from (ω − 1)(ω² − 1) = 3.
- **(h4)** C_3 ⊂ SO(3) lifts to SU(2) as an explicit unit quaternion
  `q = cos(π/3) + sin(π/3) · (1,1,1)/√3 ·(i,j,k)`. The runner verifies
  (i) |q|² = 1, (ii) q³ = −1, confirming the 2:1 double cover.
- **(h5)** Composite: (h1) ∧ (h2) ∧ (h3) ∧ (h4) all verified
  executively, so the ABSS fixed-point formula has the stated prerequisite
  support inside the stipulated route.

## Why this answers the reviewer question "is η = 2/9 a choice?"

**No hidden internal choice is made inside the stipulated route.** Once
the C₃[111] cubic rotation is stipulated, `p = 3` and the tangent
weights `(1, 2)` follow from the eigenvalues `(ω, ω²)`. The ABSS formula
is used as the stipulated fixed-point formula, with prerequisite checks
listed above. The core identity `(ζ − 1)(ζ² − 1) = 3` is an exact
algebraic fact.

There is no alternative construction under those stipulated topological
inputs that gives a different ambient `η` value. The remaining open
issues are the global topological/ABSS bridge and the physical-observable
bridge `delta_physical = eta_APS`.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links for
finite-R/topology support related to the stipulated `Cl(3)/Z^3 -> PL S^3 x R`
route and the ABSS-prerequisite authorities used by the conditional
block-by-block executable verification above. It does not promote this note
or change the audited claim scope.

- [S3_CAP_UNIQUENESS_NOTE.md](S3_CAP_UNIQUENESS_NOTE.md) — finite-R cone-cap construction support only; it does not close the global `Cl(3)/Z^3 -> PL S^3 x R` identification consumed as a stipulated premise above.
- [PL_TOPOLOGY_INFRASTRUCTURE_TEXTBOOK_IMPORT_NOTE_2026-05-17.md](PL_TOPOLOGY_INFRASTRUCTURE_TEXTBOOK_IMPORT_NOTE_2026-05-17.md) — bundles the textbook PL-smoothability (Cerf-Munkres / Cerf-Hauptvermutung dim ≤ 6), Atiyah-Singer index theorem, and standard ABSS-prerequisite imports used by the conditional ABSS applicability blocks (h1)-(h5). The `(ω - 1)(ω² - 1) = 3` core algebraic fact remains an exact symbolic identity verified by the runner.
