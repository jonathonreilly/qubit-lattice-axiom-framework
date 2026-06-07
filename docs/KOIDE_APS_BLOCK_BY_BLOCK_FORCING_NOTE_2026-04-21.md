# Delta Support Route C3 Local-Density Boundary Manifest

**Date:** 2026-04-21 (original); 2026-05-28 (narrowed to the explicit
algebraic certificate); 2026-06-06 (dependency surface sharpened: `p = 3` and
weights `(1,2)` are now sourced from the fixed-locus bridge; global PL/ABSS
applicability remains conditional); 2026-06-07 (retargeted to the bounded
local-density manifest that the current framework can actually carry).
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only.
**Status:** bounded local-density manifest. The direct load-bearing row target
is the C₃ fixed-locus operator, forced weights `(1,2)`, and exact local density
`2/9`. The supplied global `Cl(3)/Z³ → PL S³ × ℝ` / ABSS route is **not** a
load-bearing premise for this row.
**Runner:** `scripts/frontier_koide_aps_block_by_block_forcing.py` — 35/35 PASS.
All checks are executable symbolic or numeric computations; no literal
`True` placeholders remain.

## 2026-06-07 Local-Density Boundary Retargeting

The latest audit surface already records the exact distinction this source must
respect:

- the local matrix/spectrum/weight arithmetic closes;
- the global `Cl(3)/Z³ → PL S³ × ℝ` identification and global ABSS
  applicability do not close from the finite cone-cap authorities;
- the physical selected-line Brannen-phase readout is also outside the proved
  local-density statement.

This edit therefore changes the source-side target from a conditional global
APS certificate into a bounded local-density manifest. The row no longer asks a
future audit to accept the global PL/ABSS route as a premise. Instead, it asks
only whether the current framework can carry the closed subclaim already
available on the audited surface:

1. the `C₃[111]` cyclic operator has order `p = 3`;
2. its transverse fixed-locus representation forces weights `(1,2)` up to swap;
3. the exact local Lefschetz / fixed-point density arithmetic evaluates to
   `2/9`;
4. all global PL/ABSS and physical-readout assertions are explicitly out of
   scope.

The runner now checks this boundary directly against the note text and the
ledger status of the fixed-locus bridge
`koide_aps_c3_fixed_locus_weights_bridge_narrow_theorem_note_2026-06-05`,
whose audited scope is exactly the C₃ fixed-locus / local-density subclaim.
The old ABSS prerequisite block remains as a diagnostic for future bridge work
only; it is not part of the direct claim closure here.

## 2026-05-28 Audit Repair (conditional algebraic certificate)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The exact APS arithmetic closes only after stipulating p=3, weights
> (1,2), and ABSS applicability on PL S^3 x R. The one-hop
> retained-bounded deps are finite cone-cap certificates and explicitly
> do not identify the compactification with PL S^3 or provide the global
> topological/ABSS bridge."*

Repair instruction offered two paths: (a) supply an approved theorem for the
`Cl(3)/Z³ → PL S³ × ℝ` APS route and the C₃ fixed-locus weights, or (b) narrow
this source to the explicit algebraic certificate conditional on the missing
inputs.

Path (a) is now **partially** available. The fixed-locus/weight subpart is
supplied by the 2026-06-05 fixed-locus bridge cited below. The global PL/ABSS
subpart is still unavailable: the cone-cap deps
([`s3_cap_uniqueness_note`](S3_CAP_UNIQUENESS_NOTE.md),
[`pl_topology_infrastructure_textbook_import_note_2026-05-17`](PL_TOPOLOGY_INFRASTRUCTURE_TEXTBOOK_IMPORT_NOTE_2026-05-17.md))
are **finite-R** cone-cap construction certificates only; per the
2026-05-28 narrowing of `s3_general_r_derivation_note`, the all-R PL S³
identification still imports the PL Poincaré / Moise / van Kampen bridge.
There is no source-side `Cl(3)/Z³ → PL S³ × ℝ` global topological bridge to cite
here.

Before the 2026-06-07 retargeting, this parent note was a **conditional
algebraic certificate** with a smaller conditional surface than before:

**Load-bearing (source-supplied or computed in this packet):**

- `p = 3` (the C₃ rotation order), supplied by the fixed-locus bridge;
- C₃ fixed-locus tangent weights `(1, 2) mod 3`, supplied by the fixed-locus
  bridge;
- the exact block-by-block arithmetic that turns those local inputs into
  `η = 2/9` under the ABSS fixed-point formula.

**Remaining conditional input for the historical global route:** applicability
of the ABSS equivariant fixed-point formula on the global `PL S³ × ℝ` route.

**Non-load-bearing / still open:** the identification of the `Cl(3)/Z³`
compactification with `PL S³ × ℝ`, the global ABSS topological bridge, and the
physical selected-line Brannen-phase identification. The finite-R cone-cap deps
do **not** supply these; downstream consumers must carry these remaining
conditions.

No new axioms are introduced by this repair. After the 2026-06-07 retargeting,
the historical global route is recorded as future bridge context rather than a
load-bearing premise of this row.

## 2026-06-06 Dependency Surface Sharpening

The source surface has changed since the 2026-05-28 narrowing. The fixed-locus
sub-part of path (a) is now supplied by
[`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md):

- the body-diagonal `C₃[111]` operator is the cyclic axis permutation;
- its characteristic polynomial is `1 - x³`, so `p = 3` is operator-read;
- the fixed locus is the body diagonal with transverse eigenvalues
  `(ω,ω²)`, so the transverse weights are `(1,2)` up to swap;
- `(1,2)` is the unique trace-free transverse pair and gives the local
  Lefschetz / fixed-point density `2/9`.

Accordingly, this parent note no longer asks a reader to stipulate `p = 3` or
the weights `(1,2)`. It still remains conditional because the linked fixed-locus
bridge explicitly does **not** supply the global `Cl(3)/Z³ → PL S³ × ℝ`
identification, the global ABSS theorem application on the framework surface, or
the physical selected-line readout. Those are still the remaining open inputs.

This edit is a dependency-surface repair only. It does not retag this note or
set an audit outcome.

## Statement

The direct claim retained by this source is the bounded C₃ local-density
subclaim: the framework's `C₃[111]` cyclic operator forces `p = 3`, transverse
weights `(1,2)` up to swap, and the exact local fixed-point density `2/9`.
There is no hidden internal choice inside that local route. This note does not
prove the global PL S³ identification + global ABSS bridge, does not use that
route as a premise for its direct claim, and does not prove the remaining
physical bridge identifying a selected-line Brannen phase with an ambient APS
invariant.

## Bounded local-density building blocks

| # | Block | Verified / stipulated input |
|---|---|---|
| (a) | C_3[111] = 2π/3 rotation about (1,1,1)/√3 | Supplied by fixed-locus bridge; Rodrigues formula = cyclic permutation matrix P |
| (b) | Eigenvalues (1, ω, ω²) on R³ | det(R − λI) = 1 − λ³ uniquely; no other root of unity triple possible |
| (c) | Fixed locus: body-diagonal, codim-2 on S³ | rank(R − I) = 2 |
| (d) | Tangent weights (1, 2) mod 3 | Supplied by fixed-locus bridge; forced by transverse eigenvalues (ω, ω²) |
| (e) | Local Lefschetz / fixed-point density formula | Used only for the bounded local-density value; the global PL S³ × ℝ / ABSS route is diagnostic-only in this row |
| (f) | Core algebraic identity (ω − 1)(ω² − 1) = 3 | Exact algebraic fact for primitive cube root of unity |
| (g) | Result: η = (1/3)(1/3 + 1/3) = 2/9 | Unique computation from (a)–(f) |
| (h) | Alternative weights/p give different η | Consistency enumeration: once the fixed-locus bridge supplies `(p,a,b) = (3,1,2)`, nearby alternatives do not reproduce the same value |

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
  only (1, 2) is consistent with the fixed-locus bridge's C₃ rotation eigenvalues.

## ABSS applicability diagnostics outside the direct claim

This section is kept only as a future-route diagnostic. It does not supply the
direct bounded local-density claim above, and it does not establish the global
`Cl(3)/Z³ → PL S³ × ℝ` route. The source boundary is:

- **claimed here:** C₃ local fixed-locus structure, weights `(1,2)`, local
  density `2/9`;
- **not claimed here:** global PL S³ compactification, global ABSS
  applicability, ambient APS invariant, or physical selected-line readout.

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
  executively, so the ABSS fixed-point formula has the stated local-prerequisite
  support inside the conditional global route.

## Why this answers the reviewer question "is the local 2/9 value a choice?"

**No hidden internal choice is made inside the local C₃ route.** Once
the fixed-locus bridge supplies the C₃[111] cubic rotation, `p = 3` and the
tangent weights `(1, 2)` follow from the eigenvalues `(ω,ω²)`. The local density
formula then reduces to the exact algebraic identity
`(ζ − 1)(ζ² − 1) = 3`.

There is no alternative construction under those sourced local inputs that gives
a different local density value. The remaining open issues are the global
topological/ABSS bridge and the physical-observable bridge
`delta_physical = eta_APS`.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links for
finite-R/topology support related to the historical conditional
`Cl(3)/Z^3 -> PL S^3 x R` route and the ABSS-prerequisite authorities used by
the diagnostic block above. It does not promote this note or change the audited
claim scope.

- [KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md) — supplies the local C₃ fixed-locus structure, `p = 3`, transverse weights `(1,2)`, and local density `2/9`; explicitly leaves global PL/ABSS and physical readout open.
- [S3_CAP_UNIQUENESS_NOTE.md](S3_CAP_UNIQUENESS_NOTE.md) — finite-R cone-cap construction support only; it does not close the global `Cl(3)/Z^3 -> PL S^3 x R` identification consumed as a remaining conditional premise above.
- [PL_TOPOLOGY_INFRASTRUCTURE_TEXTBOOK_IMPORT_NOTE_2026-05-17.md](PL_TOPOLOGY_INFRASTRUCTURE_TEXTBOOK_IMPORT_NOTE_2026-05-17.md) — bundles the textbook PL-smoothability (Cerf-Munkres / Cerf-Hauptvermutung dim ≤ 6), Atiyah-Singer index theorem, and standard ABSS-prerequisite imports used by the conditional ABSS applicability blocks (h1)-(h5). The `(ω - 1)(ω² - 1) = 3` core algebraic fact remains an exact symbolic identity verified by the runner.
