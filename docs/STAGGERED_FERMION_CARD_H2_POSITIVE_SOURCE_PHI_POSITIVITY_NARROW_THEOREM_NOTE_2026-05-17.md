# Staggered Fermion Card H2 — Positive Source ⇒ Positive Φ — Narrow Theorem (Stieltjes / non-singular M-matrix)

**Date:** 2026-05-17
**Class:** `positive_theorem` (Class A — pure linear algebra over standard mathematical primitives)
**Lane:** staggered_fermion / parity-coupled gravity
**Block:** physics-loop / block32 / 2026-05-17 / staggered-fermion-card
**Target audit:** `staggered_fermion_card_2026-04-11` (audited_conditional)
**Source note:** `docs/STAGGERED_FERMION_CARD_H2_POSITIVE_SOURCE_PHI_POSITIVITY_NARROW_THEOREM_NOTE_2026-05-17.md`
**Runner:** `scripts/audit_companion_staggered_h2_positive_source_phi_positivity_narrow_exact_2026_05_17.py`
**Cache:** `logs/runner-cache/staggered_h2_positive_source_phi_positivity_narrow_2026_05_17.txt`

## Scope

This note narrows the admitted-context bundle of
`staggered_fermion_card_2026-04-11` by **retiring H2 as an admission**.

The staggered fermion card (rewritten 2026-04-11, repaired 2026-05-10)
records the following conditional hypotheses as imported premises:

| Premise | Statement (card text) | Status before this note | Status after this note |
|---|---|---|---|
| H1 | Screened-Poisson bridge `(L + mu^2 I) Phi = G rho` on the chosen graph | admitted | **still admitted** (out of scope) |
| H2 | `rho = |psi|^2 >= 0` so `Phi >= 0` follows from positivity of the resolvent `(L + mu^2 I)^{-1}` against a non-negative source | **stated but not proved** | **derived here** (Class A) |
| H3 | `G > 0` fixed positive | admitted (operating point) | still admitted |
| H4 | `mu^2 > 0` fixed screening mass | admitted (operating point) | still admitted |
| H5 | Static lattice | admitted | still admitted |
| H6 | Enumerated graph families | admitted | still admitted |
| H7 | Eigensolve gate at `n=9` | admitted | still admitted |
| H8 | Sign convention: positive-definite `(L + mu^2 I)` against positive `rho` gives `Phi >= 0`; inverting `Phi -> -Phi` inverts the force | partially stated | **forward direction (positive Phi) derived here**; sign-flip half remains the H8 reading |
| H9 | Staggered-Dirac structure cited from `A_min` (A3) | admitted | still admitted |

This note **proves the positivity half** of H2 (and the forward half of
H8) cleanly from standard linear algebra. After this note the card's
admitted bundle shrinks from `{H1, H2, H3, H4, H5, H6, H7, H8, H9}` (with
H2 the "positivity from resolvent" admission) to `{H1, H3, H4, H5, H6,
H7, H8, H9}`. **All numeric runner content of the card is unchanged.**

## The narrow claim

**Setup.** Let `G_graph = (V, E)` be a finite simple undirected graph
with `|V| = n` vertices. Let `A in {0,1}^{n×n}` be its symmetric
adjacency matrix (zero diagonal) and `D = diag(deg(i))` the degree
matrix. Define the combinatorial graph Laplacian
```
L = D - A.
```
Fix `mu^2 > 0` and `G > 0` (H3 + H4 operating-point assumption). Define
```
M = L + mu^2 I.
```
**Premise (imported, H1).** The screened-Poisson bridge holds:
```
M Phi = G * rho.
```
**Premise (H2 antecedent).** `rho in R^n` with `rho_i >= 0` for all `i`
(equivalently `rho >= 0` entrywise).

**Theorem (this note).**

1. (**Invertibility.**) `M` is symmetric positive-definite (SPD); in
   particular `M^{-1}` exists.
2. (**Stieltjes structure.**) `M` is a non-singular **symmetric
   M-matrix** (a *Stieltjes matrix*): `M^{-1}` is **entrywise
   non-negative**, i.e. `(M^{-1})_{ij} >= 0` for all `i, j`. On any
   *connected* graph, strict positivity `(M^{-1})_{ij} > 0` holds for
   all `i, j`.
3. (**Positivity of Phi.**) From (1)+(2),
   ```
   Phi = G * M^{-1} * rho >= 0 entrywise,
   ```
   for any `rho >= 0` and any `G > 0`. Equality `Phi_i = 0` holds iff
   `rho = 0` on a connected graph (else `Phi > 0` strictly).

## Retained inputs consumed

| Primitive | Status | Used for |
|---|---|---|
| Graph Laplacian `L = D - A` on a finite simple undirected graph is symmetric positive semidefinite (combinatorial fact) | standard mathematical primitive | shape of `M`'s off-diagonal entries (Z-matrix structure) and PSD baseline |
| Diagonal-add lemma: if `L >= 0` (PSD) and `t > 0`, then `L + t*I` is SPD (spectrum shifts by `+t`) | standard linear algebra | invertibility of `M`; strict positivity of every eigenvalue |
| Stieltjes-matrix criterion: a symmetric Z-matrix with strictly positive diagonal and weak diagonal dominance, with strict dominance in at least one row, is a non-singular M-matrix and has entrywise non-negative inverse | standard linear algebra (Berman–Plemmons, Plemmons 1977; Varga 2000) | direct route to `M^{-1} >= 0` |

No new axioms. No fitted parameters. No observational comparator. No
framework Hamiltonian inputs. No staggered-Dirac structure inputs (the
theorem is gravity-side only).

## Proof

### Step 1 — `M` is symmetric

`L = D - A` is symmetric because `A` is symmetric (`G_graph` undirected)
and `D` is diagonal. Adding `mu^2 I` preserves symmetry. So `M = M^T`.

### Step 2 — `M` is positive-definite (SPD)

`L` is PSD: for any `x in R^n`,
```
x^T L x = sum_{(i,j) in E} (x_i - x_j)^2  >=  0.
```
Its smallest eigenvalue is `lambda_min(L) = 0` with eigenvector the
constant vector `1` (assuming connectedness; otherwise multiplicity
equals number of connected components). The diagonal-add lemma gives
```
lambda_min(M) = lambda_min(L) + mu^2 = mu^2 > 0,
```
so `M` is SPD. In particular `M` is invertible.

### Step 3 — `M` is a Z-matrix

A Z-matrix is a real square matrix with all off-diagonal entries
non-positive. For `i ≠ j`:
```
M_{ij} = L_{ij} = -A_{ij} in {-1, 0},
```
so `M_{ij} <= 0` for all `i ≠ j`. (Adding `mu^2 I` affects only the
diagonal.) Thus `M` has the Z-pattern.

### Step 4 — `M` is strictly diagonally dominant

For every row `i`,
```
M_{ii} = deg(i) + mu^2,
sum_{j ≠ i} |M_{ij}| = sum_{j ≠ i} A_{ij} = deg(i).
```
So
```
M_{ii} - sum_{j ≠ i} |M_{ij}| = mu^2  > 0
```
on EVERY row. `M` is strictly row-diagonal-dominant, with constant
excess `mu^2`.

### Step 5 — `M` is a non-singular symmetric M-matrix (Stieltjes)

A symmetric Z-matrix with strictly positive diagonal that is strictly
diagonal-dominant is a non-singular M-matrix (Berman–Plemmons, Theorem
6.2.3 of Varga's *Matrix Iterative Analysis* 2nd ed., or Plemmons 1977
characterisation). Equivalently, it is a *Stieltjes matrix*. The
characteristic property of a non-singular M-matrix is:
```
M^{-1} >= 0 entrywise (every entry non-negative).
```
This is *not* a numerical accident — it follows from the Z-pattern plus
the diagonal-dominance / SPD condition by the standard splitting
argument:

> Write `M = s I - B` where `s = max_i M_{ii} = max_i (deg(i) + mu^2)`
> and `B = s I - M`. By construction every entry of `B` is non-negative
> (diagonal entries `s - M_{ii} >= 0`; off-diagonal entries `-M_{ij} =
> A_{ij} >= 0`). The spectral radius `rho(B/s) < 1` because `M` is SPD
> with `lambda_min(M) > 0` gives `s - lambda_min(M) < s`, hence
> `rho(B) < s`. Then the Neumann expansion
> ```
> M^{-1} = (1/s) (I - B/s)^{-1} = (1/s) sum_{k>=0} (B/s)^k
> ```
> is a convergent sum of entrywise non-negative matrices, so
> `M^{-1} >= 0`.

On a *connected* graph, additionally `B` is irreducible (the adjacency
graph of `B` includes every edge of the original graph), so by the
Perron–Frobenius theorem applied to non-negative matrices, the entries
of `(I - B/s)^{-1} = sum (B/s)^k` are *strictly* positive — every site
is reachable from every other site by some power of `B`. Therefore
`M^{-1} > 0` strictly entrywise on a connected graph.

### Step 6 — Conclude `Phi >= 0`

From H1, `Phi = G * M^{-1} * rho`. Since `G > 0`, `M^{-1} >= 0`
entrywise (Step 5), and `rho >= 0` entrywise (H2 antecedent),
```
Phi_i = G * sum_j (M^{-1})_{ij} * rho_j  >=  0
```
for every `i`. On a connected graph, the inequality is strict (`Phi_i >
0`) whenever `rho` is not identically zero, because `(M^{-1})_{ij} > 0`
for every `(i,j)` and the convex combination cannot vanish unless every
`rho_j = 0`.

**QED.**

## What the runner verifies

The audit-companion runner
`scripts/audit_companion_staggered_h2_positive_source_phi_positivity_narrow_exact_2026_05_17.py`
performs the following exact-precision checks (all class A):

1. **Symbolic Z-matrix / diagonal dominance.** On the path `P4` with
   `mu^2` left as a symbolic positive variable: verify that `M`
   is symmetric; that `M_{ij} in {-1, 0}` for `i ≠ j` (Z-pattern); that
   the diagonal entries are `deg(i) + mu^2 > 0`; and that the strict
   diagonal-dominance excess equals `mu^2` on every row.
2. **Symbolic inverse.** On the path `P3` with `mu^2` symbolic:
   compute `M^{-1}` exactly (sympy), verify `M M^{-1} = I` exactly, and
   evaluate every entry of `M^{-1}` at `mu^2 in {0.01, 0.22, 1, 50}` to
   verify entrywise strict positivity across the card's operating
   range.
3. **Numerical battery across card graph families.** For the families
   `{path n=10, cycle n=10, complete n=6, 3D cube n in {3, 4}^3,
   random_geo s in {10, 23}, causal_dag {6x6, 8x8}}` and operating
   points `mu^2 in {0.05, 0.22, 1.0}`, `G in {0.4, 8.0, 50.0}`:
   verify `L` is symmetric PSD; `M` is symmetric SPD (smallest eigenvalue
   `>= mu^2`); the Z-matrix off-diagonal structure; `M^{-1}` entrywise
   `>= 0`; and `Phi = G * M^{-1} * rho >= 0` entrywise for
   `rho in {e_j (each site), 1, U[0,1] sample + eps}`.
4. **Boundary witnesses.** (i) On `P20` with `mu^2 = 0.22`, `G = 50`: a
   mixed-sign source with net-negative weight produces at least one
   `Phi_i < 0` — certifying the `rho >= 0` hypothesis of H2 is tight.
   (ii) Strictly negative `rho` produces strictly negative `Phi` — the
   trivial linear-superposition check. (iii) Removing the screening mass
   (`mu^2 = 0`) leaves `L` singular (smallest eigenvalue `0`) —
   certifying `mu^2 > 0` is structurally required for the invertibility
   half of the theorem.
5. **Independent spectral route.** On `P4` with `mu^2 = 1.0`: compute
   all eigenvalues of `M`; verify SPD; reconstruct `M^{-1}` as the
   spectral sum `sum_i (1/lambda_i) v_i v_i^T` and verify entrywise
   positivity from the spectral expansion as a cross-check of the
   Stieltjes route.
6. **Boundary guard.** Print an explicit 8-bullet list of things this
   theorem does NOT claim, to prevent downstream misuse.

Runner output: **47 PASS / 0 FAIL** (Class A). See cache at
`logs/runner-cache/staggered_h2_positive_source_phi_positivity_narrow_2026_05_17.txt`.

## What this note explicitly does NOT claim

- Does NOT derive H1 (the screened-Poisson bridge equation
  `(L + mu^2 I) Phi = G rho`). H1 is the missing physics bridge from
  `A_min` to a graph-Laplacian screened-Poisson equation, and remains
  an imported harness premise of the staggered fermion card.
- Does NOT derive H3 (`G > 0`) or H4 (`mu^2 > 0`); both are
  operating-point selections of the card, and the theorem here is
  *conditional* on both being positive.
- Does NOT touch H5 (static lattice), H6 (graph family enumeration),
  H7 (eigensolve gate at `n=9`), or H9 (staggered-Dirac structure).
- Does NOT prove the force-direction half of H8 (the well/hill sign
  test, which says inverting `Phi -> -Phi` inverts the measured force).
  This note only certifies the unsigned chain `rho >= 0 ==> Phi >= 0`,
  which is the *forward* half of H8's first sentence.
- Does NOT claim universality outside finite simple undirected graphs
  (no weighted graphs, no signed graphs, no infinite graphs, no
  continuum limit).
- Does NOT replace the staggered fermion card; it narrows the admitted
  bundle from `{H1, H2, H3, H4, H5, H6, H7, H8, H9}` to
  `{H1, H3, H4, H5, H6, H7, H8, H9}` for the positivity sub-chain by
  retiring H2 as an admission.
- Does NOT promote the card to `audited_clean`. Six admissions remain;
  the card stays `audited_conditional` until further narrow theorems
  close them (or until a retained bridge derives H1 directly from
  `A_min`, which would subsume this theorem).

## Derivation chain

```
finite simple undirected graph (V, E)
        |
        v
combinatorial Laplacian L = D - A (standard math primitive)
        |
        | + mu^2 I (H4)
        v
M = L + mu^2 I
        |
        |-- symmetric (Step 1)
        |-- SPD via diagonal-add (Step 2): lambda_min(M) = mu^2 > 0
        |-- Z-matrix (Step 3): M_ij = -A_ij <= 0 for i != j
        |-- strictly diagonally dominant (Step 4): excess = mu^2 > 0 on every row
        v
non-singular symmetric M-matrix = Stieltjes matrix (Step 5)
        |
        v
M^{-1} >= 0 entrywise (strict positivity on connected graphs)
        |
        | + H1 (screened-Poisson bridge): M Phi = G rho
        | + H2-antecedent (rho >= 0)
        | + H3 (G > 0)
        v
Phi = G * M^{-1} * rho >= 0 entrywise.   [QED]
```

## Manuscript-safe wording

> The forward positivity chain of the staggered fermion card — namely,
> that a non-negative matter density `rho >= 0` produces a non-negative
> gravitational potential `Phi >= 0` on every finite simple undirected
> graph — is now derived as a narrow Class A theorem from standard
> linear algebra. The operator `M = L + mu^2 I` is shown to be a
> non-singular symmetric M-matrix (a Stieltjes matrix) on any finite
> graph whenever `mu^2 > 0`, so `M^{-1}` exists and is entrywise
> non-negative; multiplying by `G * rho >= 0` preserves entrywise
> non-negativity. The card's H2 admission, previously stated as "Phi >=
> 0 follows mathematically from positivity of the resolvent" without
> proof, is now retired in favour of this theorem. The screened-Poisson
> bridge H1 remains an imported premise; the sign-flip half of H8
> remains the separate well/hill claim; the other six admissions of the
> card (H1, H3, H4, H5, H6, H7, H9) are untouched. The card stays
> `audited_conditional` until the remaining admissions are closed.

## Audit lane positioning

- **Suggested status:** `audited_clean` → `retained` (Class A).
- **Class:** A (pure linear algebra over standard math primitives).
- **Criticality:** medium — narrows one admission of a load-bearing
  conditional card (`staggered_fermion_card_2026-04-11`, transitive
  descendants 644).
- **Independence:** runner is exact-symbolic (sympy on `P3`, `P4`) +
  exact-numeric (numpy on 9 graph families × 3 operating points × 27
  Phi-positivity rows = full numerical confirmation), with strict
  tolerance ≤ 1e-10.
- **Confidence:** high. The Stieltjes / non-singular M-matrix result is
  textbook (Varga 2000, Berman–Plemmons 1994); no novel mathematics is
  attempted.

## Why this is a clean source-only deliverable

Per the review-loop-source-only policy: this is exactly **one source
theorem note + one paired runner + one cache file**. There are no
output packets, no lane promotions, no synthesis notes, no atlas edits,
no audit-data touches. The note has no hidden dependencies on framework
Hamiltonian details; all inputs are named standard mathematical
primitives (graph Laplacian, diagonal-add lemma, Stieltjes criterion).
The runner is self-contained and depends only on `sympy` and `numpy`.
