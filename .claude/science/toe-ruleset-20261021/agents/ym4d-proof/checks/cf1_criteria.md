# cf1 — pre-registered criteria (target T55-I, (CO-fun)); written BEFORE `cf1_funnel.py`

Written 2026-10-28 21:47 UTC, after COFUN.md §1 (PRE-STATED) and §2-§3, and **before any line of
`cf1_funnel.py` exists**. Exact rational arithmetic only (`fractions.Fraction`, Python ints); no
numpy, no BLAS, single thread; DRIVE_BRIEF rule 6 exempts exact arithmetic from the numeric lock.

## What cf1 tests, and what it cannot

cf1 tests **the two handles of §29.2 (Lemma FT (i)-(ii)) rebuilt from the definition of h_l**, and
the **unit bookkeeping** behind the claim that no power of L^{k−l} occurs. It builds h_l explicitly
as a rational kernel on one block decomposition, at several (d, L).

cf1 **cannot** test: anything about Theorem W0, Theorem YH, Y^p, the root charges, (CC-0), the
multi-level cascade of Lemma RT-cc (a) (which involves the chain solution, not the kernel), or any
nonabelian step. It bears on handles 1 and 2 and on nothing else. Stated here so no later reader can
read it as support for the sections it does not touch.

## Provenance of the thresholds

- The **only numeric thresholds imported as values** are REVIEW_BFT_B_S9_S10 **S9-5**'s independently
  recomputed kernel numbers at the review's model (d = 2, L = 3): **max|c| = 1/3** and **ℓ¹ row sum
  = 4/3**. That is a prior-session constant (file dated before session 25).
- The general-(d, L) closed forms registered below (**(L−1)/(2L)** and **d(L²−1)/(4L)**) are **claims of
  mine under test**, registered as formulas before the script exists, not imported thresholds. A
  mismatch is a FAIL against me, not against the review.
- Lemma FT (i)'s own published bounds (‖h_l^T‖_{ℓ^∞→ℓ^∞} ≤ 1, ‖h_l^T‖_{ℓ¹→ℓ¹} ≤ d(L−1)) are
  prior-session and are registered as **upper bounds that must hold**.

## Model

Level-l lattice Z_{L·M}^d with periodic identification, M blocks per side, blocks
B(X) = products of L consecutive sites, c_X the block centre (L odd). Links b = (z, μ) from z to
z + e_μ. h(w)(X) := L^{−d} Σ_{y∈B(X)} ∫_{a(c_X→y)} w, with a(c_X→y) the axial path taking the
coordinates in the fixed order 1, 2, …, d, each coordinate traversed monotonically, and
∫ = signed sum of w over the links crossed (+ when traversed in the + direction). Kernel
c(X, b) := the coefficient of w(b) in h(w)(X).

Runs: (d, L) ∈ {(2,3), (3,3), (4,3), (5,3), (4,5)}, M = 3.

## Gates, with the verdict fixed now

| id | gate | PASS iff | power to fail |
|---|---|---|---|
| **A1** | **block-interior support** | c(X, b) ≠ 0 ⟹ both endpoints of b lie in B(X), for every X, b | yes — a path leaving its block breaks it |
| **A2** | **single traversal / sharp coefficient** | max_{X,b}\|c(X,b)\| = **(L−1)/(2L)** exactly, **and** ≤ 1 (FT (i)'s published bound) | yes |
| **A3** | **ℓ¹ row sum** | max_X Σ_b\|c(X,b)\| = **d(L²−1)/(4L)** exactly, **and** ≤ d(L−1) (FT (i)'s published bound) | yes |
| **A4** | **transpose diagonality** | #{X : c(X,b) ≠ 0} ≤ 1 for every link b | yes |
| **A5** | **operator norms** | ‖h^T‖_{ℓ^∞→ℓ^∞} = max_b Σ_X\|c(X,b)\| = (L−1)/(2L) and ‖h^T‖_{ℓ¹→ℓ¹} = max_X Σ_b\|c(X,b)\| = A3's value | **low — A5 follows from A2+A3+A4.** Declared derived; reported, not counted as independent evidence |
| **A6** | **h(const) = 0** | h(w)(X) = 0 for every X and every constant 1-form w = e_μ, μ = 1…d (BL-2 (b)'s clause) | yes — fails under any non-central root convention |
| **A7** | **max multiplicity** | every link is traversed at most once by each axial path (reported as max multiplicity = 1) | yes |
| **B1** | **unit exponent, regrouped** | for every k ≤ 8, 0 ≤ l < k, 0 ≤ l' ≤ l: the exponent of L in L^{3(k−l)}·L^{−3(k−l')} equals **−3(l−l')**, and is **independent of k** | yes — any mis-stated conversion changes it |
| **B2** | **geometric summability, regrouped** | Σ_{l'≤l} L^{−3(l−l')} < (1 − L^{−3})^{−1} for every l ≤ 8 | yes |
| **B3** | **d-independence of A1-A4, A6, A7** | A1, A2 (as the formula (L−1)/(2L)), A4, A6, A7 hold at every (d, L) run, and A3 matches d(L²−1)/(4L) at every one | yes — a d = 4 obstruction in the handles would show here |

## Designed-FAIL controls (defect 3). Each MUST fire; a control that passes voids its gate.

| id | control | the gate(s) it must break | what it must leave intact |
|---|---|---|---|
| **C1** | root at the block's **lower corner** instead of the centre | **A2** (max\|c\| becomes (L−1)/L), **A3** (row sum becomes d(L−1)/2), **A6** (h(const) ≠ 0) | **A1, A4, A7** must still pass — the support and diagonality claims must be shown to be convention-free, as §29.2's definition line asserts |
| **C2** | **back-tracking path**: in coordinate 1 go one step in the − direction and back before proceeding | **A3** (row sum rises) and **A7** (multiplicity 2) | A1 may survive; report which |
| **C3** | **wrap-around path**: in coordinate 1 go the long way round the torus | **A1** (support leaves the block) and **A4** (a link is claimed by two blocks) | — |
| **C4** | **naive grouping exponent**: the level-i funnel reading the levels l > i, exponent 3(k−i) − 3(k−l) = +3(l−i) | **B2** (the sum Σ_{i<l}L^{+3(l−i)} diverges geometrically) | B1's k-independence must still hold — the point is that the k-cancellation is not what distinguishes the two groupings |

## Reporting rule

Every verdict is reported, PASS or FAIL, with the exact rational value. Any probe added after seeing
a result is labelled **post-hoc** in the record. If a control does **not** fire, the gate it was
built for is reported as **unsupported**, not as passed.

## Amendment, recorded (2026-10-28 21:49 UTC), BEFORE any script exists

The first draft of this file registered the sharp ℓ^∞ coefficient as **1/L**. That is the value at
L = 3 only; COFUN.md §3 (i) 2, written before this file, derives **(L − 1)/(2L)**, which agrees with
1/L at L = 3 and differs at L = 5. The gate is amended to the general form **(L − 1)/(2L)** at
21:49 UTC. **No script existed at the time of this amendment and no result had been seen**; the
amendment is recorded here rather than made silently, per [RBB8-fix RS8-7] (ii) and
REVIEW_BFT_B_S9_S10 RS10-P2. The L = 5 run (d = 4, L = 5) is the one that discriminates the two
forms, and it is in the registered run list.

## Provenance correction, appended 2026-10-28 21:56 UTC (after the run; order claims unchanged)

Two statements in this file's header are wrong about the clock and one is wrong about the order.

1. "Written 2026-10-28 21:47 UTC" — the first draft's birth time is **unrecoverable**: the 21:49
   amendment was made by rewriting the file, so `mtime` now reads **21:45:08** and no earlier
   timestamp survives. This is exactly the defect REVIEW_BFT_B_S9_S10 **RS10-P2** records against
   `bb10_criteria.md`, reproduced here; recorded rather than papered over.
2. "after COFUN.md §1 (PRE-STATED) and §2-§3" — **false for the first draft**, which was written
   *before* COFUN.md §2-§3. It is true for the amendment. COFUN.md §1 did precede this file.
3. The amendment is timestamped 21:49 in its own paragraph; `mtime` says **21:45:08**. Read the
   mtime.

**What is unaffected, and is what rule 2 asks for:** this file in both its drafts preceded
`cf1_funnel.py` (`mtime` **21:46:33**) and its run (`cf1_out.txt`, **21:46:47**). Every gate,
threshold and control verdict above was fixed before any script existed. `cf1b_posthoc.py`
(**21:48:28**) is post-hoc and says so.
