# Independent boundary source from the microscopic source: the Schur bridge theorem

**Date:** 2026-07-25
**Runner:** `scripts/frontier_oh_schur_independent_boundary_source_bridge.py`

## Purpose

Given a source `rho` on the zero-Dirichlet interior grid of a `size`-cubed box with 6-NN
negative Laplacian `H_0`, this note constructs a shell-boundary source
`j_micro = j_micro(rho, H_0)` from the microscopic source and the lattice operator alone,
and shows that the shell trace of the microscopically sourced field is the unique
stationary point of a quadratic boundary action driven by it. The construction takes
`rho` as its only field input: it does not read the target trace, does not build a
harmonic extension of it, and is not assembled from the object it predicts. The trace it
yields is therefore compared against one from a separate factorisation and solve of the
same full lattice system: for four independently prescribed sources at three box sizes,
and for two exactly specified field classes built by
`scripts/frontier_same_source_metric_ansatz_scan.py` and
`scripts/frontier_coarse_grained_exterior_law.py` at size 15.

## Setup

Let `H_0, interior = build_neg_laplacian_sparse(size)` be the 6-NN negative Laplacian on
the `interior = size - 2` cubed grid of sites strictly inside the box, `n = interior^3`,
with zero Dirichlet data on the outer faces. Fix `R = 4` and partition the `n` sites
using the exterior classification of `scripts/frontier_discrete_dtn_shell_kernel.py`:
`b` = exterior sites (radius `> R`) all six of whose neighbours are also exterior;
`t` = exterior sites with at least one non-exterior neighbour, the shell; `I` =
everything else, the strictly interior region (radius `<= R`).

**Separation lemma.** No site of `I` is 6-NN adjacent to a site of `b`: if a `b` site had
a neighbour in `I`, that neighbour would be non-exterior, so the site would have been
classified into `t`. Hence `H_Ib = 0` and `H_bI = 0` exactly, as an absence of stored
matrix entries rather than to rounding. The runner verifies this instead of assuming it,
and verifies `H_tI`, `H_tb` non-empty, so neither elimination is vacuous. Over `(I, t, b)`:

```
H_0 = [[H_II, H_It, 0   ],
       [H_tI, H_tt, H_tb],
       [0,    H_bt, H_bb]]
```

## Theorem (two-sided trace equation)

Let `phi` solve `H_0 phi = rho` and write `f := phi_t`. Eliminating `phi_I` via row `I`
and `phi_b` via row `b`, then substituting both into row `t`, gives the exact identity

```
S f      =  j_micro
S       :=  H_tt - H_tI H_II^{-1} H_It - H_tb H_bb^{-1} H_bt
j_micro :=  rho_t - H_tI H_II^{-1} rho_I - H_tb H_bb^{-1} rho_b
```

`H_II` and `H_bb` are principal submatrices of the symmetric positive definite `H_0`, so
both are invertible and `S`, the two-sided Schur complement of `H_0` onto `t`, is itself
symmetric positive definite. The right-hand side is a functional of `rho` and `H_0` only.

## Corollary (honest stationarity)

Because `S` is symmetric positive definite, `f` is the unique minimiser of
`I_R(g ; j_micro) = (1/2) g^T S g - j_micro^T g`, whose gradient is
`grad I_R(g) = S g - j_micro`, so `grad I_R(f) = 0`. The gradient identity carries content
here: the source on the right was assembled without consulting `f`, so its vanishing at
`f` is a statement checkable against an independent solve. It is sensitive to `j_micro`
termwise -- `S` is invertible, so any change to `j_micro` moves the minimiser, and rows
5a-5c exhibit that for each of its three terms. It is **not** sensitive to `S` entrywise:
`S f = j_micro` constrains `S` only on the ray through `f`, so `S + eps w w^T` with `w`
orthogonal to `f` reproduces `f` exactly, and stays symmetric positive definite, at any
`eps`. Measured at size 13 on the random-in-`I` source, `eps = 1e+04` leaves the
reconstruction error at `8.7e-15` while moving `S` by `1.5e+02` in largest absolute entry.
What pins `S` here is the derivation and rows 2-3, not the reconstruction gate.

## Relation to the exterior-only operator

The exterior-only Schur complement is `Lambda_R = H_tt - H_tb H_bb^{-1} H_bt`, so
`S = Lambda_R - H_tI H_II^{-1} H_It`: the stationarity operator for a microscopically
sourced configuration carries an extra interior Schur term, and on this family that term
is not small. The largest absolute entry of `H_tI H_II^{-1} H_It` is `6.188088e-01`
against an `H_tt` diagonal of `6`; the runner reports this quantity, under the
max-absolute-entry convention its legend states, and an off-line computation puts the
induced infinity norm of the same matrix at `3.000000e+00`, half that diagonal. Both are
identical at all three sizes because the inner region and its adjacent shell layer do not
change with the box. Pairing `j_micro` with `Lambda_R` misses the true trace by `2.4e-01`
to `5.1e-01` relative on the four prescribed sources, and by `7.2e-01` on both exact
classes, so the independent source must be paired with `S` unless the interior Schur term
annihilates the configuration at hand.

## Why the previous construction's gradient equation was an identity

The earlier note `OH_SCHUR_BOUNDARY_ACTION_NOTE.md`, implemented in
`scripts/frontier_oh_schur_boundary_action.py`, pairs `Lambda_R` with a source obtained
by taking the target trace `f`, forming the harmonic extension `u_f` of that same `f`
into the exterior bulk, and reading the trace flux `(H_0 u_f)|_t`. For such an extension,
with the strictly interior region held at zero,
`(H_0 u_g)|_t = H_tt g - H_tb H_bb^{-1} H_bt g = Lambda_R g` identically, for *any* trace
vector `g`, physical or not. The runner exhibits this with a random `g`: the residual is
`8.9e-15` at size 13 and comparable at 15 and 17, against `||Lambda_R g||_inf` about
`1.8e+01`. A residual that vanishes for an arbitrary trace vector cannot distinguish the
physical trace from any other, so that gradient equation was an algebraic identity of the
construction rather than a stationarity result. The two sources also differ as objects.
Their difference is exactly the interior Schur term applied to the trace,
`j_taut(f) - j_micro = H_tI H_II^{-1} H_It f`, verified off-line to `1.0e-15` against a
`||j_micro||_inf` of order `1e+00`; rows 7b-7d therefore measure the relative size of that
term, and no gate here can detect a source reconstructed from the trace — that property
is established by inspecting which arguments the construction reads, not by a number.
Relative to `j_micro` the difference runs `1.9e-01` to `5.8e-01` on the four prescribed
sources and about `2.8e+00` on both exact classes, the latter because those classes are
sourced strictly inside `I` (below).

## Numerical verification

Seed `20260725`, `cutoff_radius = 4.0`, sizes `13, 15, 17`, runtime about 4 s. Site counts
`(|I|, |t|, |b|)` are `(257, 782, 292)`, `(257, 1052, 888)`, `(257, 1364, 1754)`.

| # | Check | size 13 | size 15 | size 17 |
|---|-------|---------|---------|---------|
| 1 | `nnz(H_Ib)`, `nnz(H_bI)`; block sum vs `n`; `t_box` | `0`, `0`; `1331`=`1331`; `602` | `0`, `0`; `2197`=`2197`; `866` | `0`, `0`; `3375`=`3375`; `1178` |
| 2 | `\|\|S - S^T\|\|_inf` ; `lambda_min(S)` | `4.440892e-16` ; `6.049261875e-01` | `4.440892e-16` ; `5.507655684e-01` | `5.551115e-16` ; `5.118567811e-01` |
| 3 | `\|\|S - (Lambda_R - H_tI H_II^-1 H_It)\|\|_inf` ; `\|\|S - S_joint\|\|_inf` | `0.000000e+00` ; `8.881784e-16` | `8.881784e-16` ; `8.881784e-16` | `8.881784e-16` ; `8.881784e-16` |
| 4a | reconstruction rel. error, point source at centre | `1.107992e-14` | `1.396884e-14` | `1.113781e-14` |
| 4b | reconstruction rel. error, random source in `I` | `6.409667e-15` | `9.426632e-15` | `7.600553e-15` |
| 4c | reconstruction rel. error, random source in `b` | `3.470925e-15` | `5.767796e-15` | `6.530465e-15` |
| 4d | reconstruction rel. error, random source on `I`,`t`,`b` | `3.954689e-15` | `6.854863e-15` | `7.043622e-15` |
| 4e | reconstruction rel. error, exact local `O_h` class (`xchk` `1.454791e-15`) | — | `1.280216e-14` | — |
| 4f | reconstruction rel. error, exact finite-rank class (`xchk` `1.224906e-15`) | — | `1.378019e-14` | — |
| 5a | rejector: drop `-H_tb H_bb^-1 rho_b` | `4.175394e-01` | `5.717319e-01` | `5.032162e-01` |
| 5b | rejector: drop `-H_tI H_II^-1 rho_I` | `2.661020e-01` | `2.472237e-01` | `3.123370e-01` |
| 5c | rejector: drop `rho_t` | `1.013921e+00` | `6.526345e-01` | `7.329871e-01` |
| 6a | rejector: `Lambda_R^-1 j_micro` vs true trace | `2.387521e-01` | `5.113928e-01` | `3.528884e-01` |
| 6b | same, exact local `O_h` class | — | `7.180982e-01` | — |
| 6c | same, exact finite-rank class | — | `7.151571e-01` | — |
| 7a | `\|\|Lambda_R g - (H_0 u_g)\|_t\|\|_inf`, random `g` | `8.881784e-15` | `7.105427e-15` | `8.881784e-15` |
| 7b | rel. `\|\|j_taut(f) - j_micro\|\|_inf` | `1.901801e-01` | `5.832805e-01` | `3.987182e-01` |
| 7c | same, exact local `O_h` class | — | `2.765731e+00` | — |
| 7d | same, exact finite-rank class | — | `2.754925e+00` | — |
| 8a | perturbed source: prediction vs full solve | `3.827607e-15` | `6.339742e-15` | `6.150760e-15` |
| 8b | perturbed source: rel. motion of the trace | `5.776783e-04` | `4.167462e-04` | `4.542326e-04` |

Gate directions: row 1 requires the two cross blocks to be empty and both eliminations
non-vacuous; row 2 requires `||S - S^T||_inf` below `1e-9` and `lambda_min(S)` strictly
positive; rows 3, 4a–4f, 7a and 8a require small numbers (tolerance `1e-9`); rows 5a–5c,
6a–6c, 7b–7d and 8b require *large* ones (`> 1e-3` for the rejectors, `> 1e-6` for the
motion row), so the reconstruction gate cannot pass vacuously. Full run:
`TOTAL: PASS=51 FAIL=0` over 21 named gates — fifteen at each of the three sizes, six at
size 15 only. The runner prints each gate statement once, with its tolerance, under a
`GATES` legend preceded by a preamble factoring out the shared definitions. That legend
is ordered by the gates' insertion order rather than by row label, so the six
size-15-only gates are listed after `8b` instead of beside their numeric siblings; each
states "size 15 only" in its own text. One numeric line per gate per size follows.

Row 3 reports two comparisons that are not of equal standing. `split` compares two
spellings of the same elimination through the same factorisation; it is bit-exactly
`0.000000e+00` at size 13 and is solver agreement, not an independent route. `joint`
compares the two-term split against a single Schur complement of `H_0` onto `t` over
`X = I ∪ b` from one factorisation of `H_XX`; that agreement is the numerical content of
the separation lemma.

An off-line probe, not gated by the runner, bounds how sharply row 4 discriminates.
Scaling one diagonal entry of `S` by `1 + 1e-6`, swept over all `782` entries at size 13
on the random-in-`I` source, raises the row-4 error to a median of `7.0e-08`, the sweep
spanning `7.6e-10` to `1.2e-06`. Three of the `782` entries stay below the `1e-9`
tolerance, so the gate discriminates against a diagonal perturbation of this size at
`779` of `782` entries rather than at all of them. `j_micro` is itself nonzero at only
`186` of the `782` shell sites for these sources, so a probe perturbing an entry of
`j_micro` relative to its own magnitude is undefined on the remaining `596`.

**What the two exact classes do and do not exercise.** Both classes are sourced strictly
inside `I`: the runner reports `rho_t` and `rho_b` at the `1e-16` level in rows 4e and 4f,
against a `rho_I` of order `1e+00`. That pair of numbers, not the `xchk` self-guard, is
what ties each class's field to this operator's site indexing — `xchk` re-solves
`H_0 x = rho` for the same `rho` the class produced and would return the same vector under
any flattening convention, so it guards the factorisation and the provenance of `f_true`,
not the ordering. Even that discriminator is degenerate against one specific confusion:
both classes are `O_h`-symmetric, so C-order and Fortran-order flattening produce the
identical vector and the two conventions cannot be told apart here — harmlessly, since
they agree. On these classes `j_micro` reduces to its single interior term
`-H_tI H_II^{-1} rho_I`; the `rho_t` and `-H_tb H_bb^{-1} rho_b` terms sit at roundoff
rather than merely being small. Two consequences, stated rather than hidden. First, the
two classes test the interior elimination channel only; the full three-term structure of
`j_micro` is exercised by rows 4a–4d and 5a–5c, whose sources are supported on `I`, on
`b`, and across all three blocks. Second, a 5a- or 5c-style rejector applied to these
classes would be vacuous by construction: dropping a term already at roundoff leaves
`j_micro` unchanged to that order, so such a rejector would return the row-4e/4f error
itself, of order `1e-14` and far below the `1e-3` floor a rejector must clear. That is why
rows 5a–5c are not extended to them. The rejector that would move here is the 5b form,
dropping the interior term, which collapses `j_micro` to roundoff and drives the error to
`1` — a statement about the classes, not a discriminating test of the theorem.

## What this does not yet supply

1. The box is finite with zero Dirichlet data on its outer faces, so no continuum or
   infinite-volume limit is addressed. The shell set `t` also contains the outermost
   interior layer of the box, and that layer is the majority of `t`: `602` of `782` sites
   at size 13 (`76.98%`), `866` of `1052` (`82.32%`) at size 15, `1178` of `1364`
   (`86.36%`) at size 17. The fraction grows with the box, so `t` is dominated by box
   artefact rather than by shell, increasingly so at larger sizes. The runner reports this
   count as `t_box` in row 1.
2. `rho` is given data. Nothing here derives it from a variational principle for the
   matter sector, so the boundary source is independent of the trace but still downstream
   of an unmodelled source.
3. The field is a single scalar on a cubic lattice; no tensorial or metric structure is
   carried. Three box sizes at one cutoff radius are covered, with no scaling law in `R`
   or `size` for `S` or for the interior Schur term.

## What this opens next

- **Infinite volume.** Enlarge the box at fixed `R` and track `S`, `Lambda_R` and their
  difference. The interior Schur term is already size-stable at `6.188088e-01` in largest
  absolute entry and `3.000000e+00` in induced infinity norm, so the correction plausibly
  has a box-independent limit worth isolating. Isolating it means first separating the
  shell proper from the outermost box layer that currently dominates `t` — a partition
  reporting the two subsets separately is the next path this opens.
- **A derived matter source.** Couple `j_micro` to a `rho` produced by a variational
  matter sector rather than prescribed, making the chain from action to shell trace
  derived on the source side too; the axiom surface is
  [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).
- **The tensorial lift.** Repeat the three-block elimination for a multi-component field,
  where `H_II` and `H_bb` acquire internal indices, and ask whether the separation lemma
  and the positive definiteness of `S` survive.
- **Cutoff dependence.** Vary `R` and measure how the interior Schur term and the rejector
  margins move, separating shell placement from operator.
