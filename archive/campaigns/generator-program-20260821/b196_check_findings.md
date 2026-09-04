# Block 196 candidate adversarial check — window-Schur theorem

**Status:** COMPLETE. Exact `QQ` arithmetic only; no floats, tolerances, `evalf`, or `nsimplify`.

## Source and provenance lock

- Construction authority is restricted to the Block 190 width-family note and the Block 193 parity-window note named in the dispatch.
- The exact Block 190 source is commit `e75ad9f4998ae4cc6a25a2e20191e0b9d76ff3fd`; its note blob is `42c93e5b4833faaf9d535bce3bd0205af3e7311c`.
- The exact Block 193 source is commit `37a5f926c9e15745faaffda66b308f0d04e76e47`; its note blob is `310022e30f02ae9219384c71806ff2582b6f273a`.
- Those blobs are unchanged at this worktree's current Block 195 tip. A fresh `origin/main` fetch on 2026-08-26 does **not** contain the two named note or runner paths, so “landed” here means landed in the stacked physics-loop branch history, not present on canonical `origin/main`. No audit-history or prior Block 196 finding was used.
- Fixture: `m = 9/20`, `c = 5/13`, unit-volume Hodge block
  `B = [[1,0,0,0],[0,169/144,-65/144,0],[0,-65/144,169/144,0],[0,0,0,1]]`.

## Exact target contract

For each requested `(T,t0)`, form the Block 190 wrap-edge action `Q`, `G = Q^{-1}`, the eight-cell core, `K_c`, `W1 = K_c^{-1}L_1`, `W = K_c^{-1}L_2`, and the one- and two-step defect columns. Let the proposed three-slice window be

`J(t0) = [2 floor(t0/2)+1, 2 floor(t0/2)+3] x Z_4`

and `A = Q^T[:,J]`, a `(4T) x 12` exact rational matrix.

The candidate survives only if: `rank(A)=12`; every one- and two-step defect is in `im(A)`; the padded unique one-step solution equals `G^T d` for all eight columns; the two-step solution-support union is all 12 window rows; the one-step union has the claimed parity form; and the disjoint-source consequence is logically valid and exactly instantiated. Minimality, the non-control fixture `(1/2,1/3)`, and all valid `T=20` cores are separate hostile probes. Proper-subset minimality is not inferred from rank or from the union of supports; it is tested as an image-membership question.

## Findings

### Verdict

**No refutation of C1–C5 was found.** At the fixture, C1–C5 survive on all five requested `T=16` cores and on **all seven valid `T=20` cores** `t0=1..7`. P1 qualifies, but does not refute, full-window minimality: the full 12 rows are minimal for the two-step family and for the joint one-/two-step family, while the one-step family alone collapses to four rows at every even core. P2 survives at the non-control point on all twelve cores. Details below are exact.

### Independent reconstruction and two solve routes

The checker `b196_exact_check.py` imports neither landed runner. It rebuilds `Q` from the displayed `v=1` Hodge family and the entrywise wrap-edge construction, inverts over `QQ` with `DomainMatrix`, and obtains each defect solution in two ways:

1. the global inverse route `u = G^T d`, with `Q^T u-d = 0`;
2. an independent restricted solve: exact RREF of `A^T` selects 12 independent rows, their `12 x 12` minor is inverted over `QQ`, and the resulting `x` is checked against all `4T` equations before padding.

For both `T=16` and `T=20`, `QG-I = GQ-I = 0` entrywise. Every restricted-solve residual, every padded/global comparison residual, and every displayed identity residual below is exactly zero.

### C1 — rank / uniqueness: CONFIRMED

At each of the 12 fixture cores,

`rank_QQ(A) = 12`.

There is also a short independent proof: `Q` is invertible (the exact two-sided inverse residual is zero), hence `Q^T` is invertible, and every subset of 12 columns of an invertible matrix is linearly independent. Therefore the selected 12 columns have rank 12 and any window-supported solution is unique.

### C2 — existence for all defects: CONFIRMED

For every core, both eight-column systems solve exactly:

`A X_1 = [d_b^(1)]_{b=0}^7`,  `A X_2 = [d_b^(2)]_{b=0}^7`.

This is 192 exact vector solves at the fixture: 12 cores × 8 columns × 2 steps, with zero residual in every equation. The unique global preimages `G^T d_b^(s)` have no support outside the proposed window.

### C3 — one-step identification: CONFIRMED 8/8 per core

For all `96 = 12 cores x 8 columns` one-step defects, padding the independently solved 12-vector by zeros outside the window gives exactly `G^T d_b^(1)`. The comparison residual is the zero vector in every case.

A useful exact detail: for `b=0,1,2,3` the one-step defect and its solution are themselves zero at every core. The nontrivial one-step content is in `b=4,5,6,7`.

### C4 — support law: CONFIRMED, with the exact per-family qualification

For the two-step family, the union over `b=0..7` of solution row supports is all 12 window rows at every core. Thus its slice union is the full three-slice window.

For the one-step family:

- odd `t0`: the union is all 12 rows on all three window slices;
- even `t0`: the union is exactly the four rows on the first window slice — slice `3` at `t0=2`, slice `5` at `t0=4`, and, in the `T=20` extension, slice `7` at `t0=6`.

The per-column slice pattern sharpens this. At odd cores the four nonzero one-step columns `b=4..7` each meet all three slices. At even cores they each have exactly four nonzero coordinates, all on the first slice. For the two-step family at even cores, `b=0..3` each live on that first slice, while `b=4..7` each meet all three slices; at odd cores all eight meet all three slices.

### C5 — disjoint-source consequence: CONFIRMED, but the missing logical condition matters

For the b193 two-step functional `u_b = G^T d_b^(2)`, the exact computation gives both

`supp(u_b) subset J(t0)` and `supp(D_s u_b) subset J(t0)`

for every `b`, every fixture core, and both widths. The second containment is essential: disjointness of `dH` from `supp(u_b)` alone would not prove the claim.

Indeed,

`u_b^T dQ = u_b^T dH (mI + D_s) - (D_s u_b)^T dH`.

For a reflected source cell, `dH` has identical row and column support `S`. If `S` is disjoint from the window, then both `u_b|_S` and `(D_s u_b)|_S` vanish, so both terms above vanish identically. This proves the consequence for the source-cell family; it is not merely a sampled cancellation.

The checker nevertheless exhausts the available disjoint source cells as a guard: 16 per `T=16` core and 24 per `T=20` core, `248` source/core cells in total, with zero failures for the eight `u_b` simultaneously.

Exact parity instances at `T=16`:

- odd `t0=1`, window slices `{1,2,3}`: source `(s,x)=(4,0)` has `dH` slice support `{4,5,11,12}` and `u^T dQ = 0_(8 x 64)`;
- even `t0=2`, window slices `{3,4,5}`: source `(s,x)=(0,0)` has `dH` slice support `{0,1,15}` and `u^T dQ = 0_(8 x 64)`.

### P1 — smaller row sets: QUALIFICATION, not a refutation of the joint theorem

Because C1 gives uniqueness, a row index may be deleted from the allowed solution support for a family if and only if that coordinate is zero in every member of the unique solution family. Therefore the union supports above decide **all** proper subsets, not only the tested two-slice ones.

- Two-step family alone: minimal uniform support is all 12 rows at every core. No proper subset works. In particular, all three two-slice / 8-row subsets fail at every core.
- Joint one-step + two-step family: minimal uniform support is all 12 rows at every core. No proper subset works.
- One-step family alone, odd core: minimal uniform support is all 12 rows; every two-slice subset fails.
- One-step family alone, even core: minimal uniform support is only the first slice's four rows. Of the three two-slice subsets, `first+middle` and `first+last` solve all eight one-step defects; `middle+last` fails. Thus the 12-row “window” is not minimal for one-step transport at even cores — a real attribution weakening if C2 is narrated step-by-step, but not a weakening of the two-step window or of a single support set required to handle both steps.

### P2 — non-control `(m,c)=(1/2,1/3)`: STRUCTURE PERSISTS

Using the exact `v=1` continuation of the displayed Hodge,

`B(1/3,1) = [[1,0,0,0],[0,9/8,-3/8,0],[0,-3/8,9/8,0],[0,0,0,1]]`,

C1–C4 all pass on the same full domain: `T=16`, `t0=1..5`, and `T=20`, `t0=1..7`. The ranks, zero residuals, padded identifications, parity slice unions, per-column slice patterns, and P1 minimal uniform row counts are unchanged. This is a non-control persistence result at one additional exact point, not a generic `(m,c)` theorem.

### P3 — `T=20` width extension: COMPLETED

All valid cores `t0=1..7` were checked, not only the requested minimum `3,4`. C1–C5 pass at all seven. The parity pattern continues through the farthest valid pair: `t0=6` uses window `{7,8,9}` and has the four-row one-step collapse on slice `7`; `t0=7` uses the same window and has full three-slice one-step support.

### Construction fingerprints and final compact certificate

Two exact landed fingerprints were recomputed from the independent construction before accepting the support results:

- b190, `T=20`, `t0=3`:
  `(W-V^2)[0,4] = 53601896033238042551256 / 229758595220483765728625`; residual from the b190 value: `0`.
- b193, `T=16`, `(t0,s,x)=(2,5,0)`:
  `R[0,4] = 303717414128393981002946552450301011272963193469691599136505997554493148222247708710000000 / 77707725095998816829080256798567544217876202163787270905242891606801827087957579200283634261`; residual from the b193 value: `0`.

The final compact rerun returned:

```text
summary_all = true
control_core_count = 12
noncontrol_core_count = 12
C5_all = true
C5_disjoint_cells = 248
```

### Claim boundary

The finite candidate as dispatched is **not refuted**. The strongest honest statement is: at the two exact fixtures and the finite domains above, the window-Schur systems have the claimed unique supported solutions and parity law; the 12-row window is uniformly minimal for the two-step and joint families, but not for the one-step family at even cores. This does not prove the support law for arbitrary even `T` or generic `(m,c)`, and it does not cure the provenance fact that the two construction notes are absent from current `origin/main`.
