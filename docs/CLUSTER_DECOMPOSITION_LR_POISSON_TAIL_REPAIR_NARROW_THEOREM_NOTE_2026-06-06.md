# Lieb–Robinson / Poisson-Tail Estimate Repair for Cluster-Decomposition Step 3

**Date:** 2026-06-06
**Claim type:** bounded_theorem (proof repair)
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. It supplies the corrected Step-3 estimate the audit
of `axiom_first_cluster_decomposition_theorem_note_2026-04-29` requested.
**Primary runner:**
[`scripts/frontier_cluster_decomp_lr_poisson_tail_repair_2026_06_06.py`](../scripts/frontier_cluster_decomp_lr_poisson_tail_repair_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_cluster_decomp_lr_poisson_tail_repair_2026_06_06.txt`](../logs/runner-cache/frontier_cluster_decomp_lr_poisson_tail_repair_2026_06_06.txt)

---

## Role

The independent audit graded
[AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
**audited_failed**, with rationale: *"the load-bearing LR constant derivation has
a local proof break: `(a/n)^n <= exp(-n)·exp(n log(a/n))` is false, and the
Poisson-tail-to-light-cone step is not supplied correctly ... Repair Step 3 with a
correct LR/Poisson-tail estimate."* This note supplies that repair. The series
bound (eq. 6) and the light-cone conclusion (eq. 7) of the source note are the
**standard finite-range Lieb–Robinson result and are correct**; only the cited
justification line was wrong.

## The error

The note's Step 3 cited the "elementary inequality"
`(a/n)^n ≤ exp(-n)·exp(n log(a/n))`. Since `exp(n log(a/n)) = (a/n)^n`, the RHS is
`exp(-n)·(a/n)^n`, so the claim reduces to `1 ≤ exp(-n)`, i.e. `n ≤ 0` — **false**
for every `n > 0` (runner Block 1 exhibits this).

## The correct estimate (runner SCORECARD 13/13 PASS)

With `x = J_* D_int R_int |t|` and the light-cone index `R = d(x,y)/R_int`, the
LR series tail (eq. 6) obeys the **standard** chain:

```text
 (T1)  Σ_{n≥R} x^n/n!  ≤  e^x · x^R/R!
         [ Σ_{n≥R} x^n/n! = (x^R/R!) Σ_{k≥0} x^k R!/(R+k)! ≤ (x^R/R!) Σ_{k≥0} x^k/k! ]
 (T2)  x^R/R!  ≤  (e x / R)^R                         [ Stirling lower: R! ≥ (R/e)^R ]
 (T3)  (e x/R)^R = exp(-R log(R/(e x))) ≤ exp(-(R - e x))   [ tangent: log z ≥ 1 - 1/z ]
```

Chaining: `Σ_{n≥R} x^n/n! ≤ e^x (e x/R)^R ≤ e^{(1+e)x} e^{-R}`. With `R = d/R_int`
this is the light cone

```text
   ‖[A(t), B]‖  ≤  2‖A‖‖B‖ · exp( -(d − v_LR|t|)/ξ ),
   v_LR = O(1)·e·J_* D_int R_int ,   ξ = R_int ,
```

with **exponential decay for `d > v_LR|t|`** (equivalently `R > e x`). This is
exactly **(L1)** of the source note, with honestly-derived `O(1)` light-cone
constants (not a tuned fit). The runner verifies each inequality `(T1)–(T3)`
numerically across several `(x,R)`, exhibits the strict tail decay outside the
cone (`R > e x`), and confirms (teeth) that inside the cone (`R < e x`) the tail
is `O(e^x)` (no clustering), as it must be.

## Scope (what this repairs, and what it does not)

- **Repairs L1** — the Lieb–Robinson commutator bound (the failed Step-3 math).
  With the corrected estimate, `(6) → (7)` is a sound derivation.
- **Does not, by itself, promote L2** (static spatial cluster decomposition). As
  the source note already states, LR bounds control **commutators** outside a
  light cone; they do **not** prove static connected-correlator clustering — that
  needs a retained **mass-gap / target-state** authority (the audit's separate
  requirement). This note removes the *failure* (the false inequality) and makes
  L1 correct; the L2 spatial-clustering promotion remains gated on the gap.
- No axiom, no fitted input, no audit verdict.

## Reprove-and-cite ledger

- **Reproven here** (runner): the falsity of the cited inequality; Stirling
  `n! ≥ (n/e)^n`; the tangent bound `log z ≥ 1 − 1/z`; the tail chain
  `(T1)–(T3)` and the light-cone exponential, across multiple `(x,R)`.
- **Cited**: the LR series (eq. 4–6) and the target light-cone form (eq. 7) of
  `axiom_first_cluster_decomposition` (the standard finite-range LR structure);
  the classical Lieb–Robinson (1972) / Hastings–Koma / Nachtergaele–Sims bound as
  the literature comparator for the light-cone form (never an input to any
  constant).

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links so the audit
citation graph can track them. It does not promote any note or change any
audited claim scope.

- [AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
