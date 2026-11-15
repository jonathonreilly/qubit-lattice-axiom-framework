# checks/nq1_criteria.md — pre-registered criteria for check nq1 (the (N-Q) row norms ‖Q^j‖_{∞→∞})

Written 2026-10-28 13:08 UTC, BEFORE `checks/nq1_qnorm.py` exists. Exact integer / `Fraction` arithmetic in plain
python, one process, no numpy, no BLAS, no numeric lock (brief rule 6: exact rational/symbolic arithmetic does not
need the lock). Memory target < 1 GB, wall time target < 20 min.

**No constant below is derived in this session.** The constants used are: L = 3, d = 4 (Setting SC, PROOF.md l.2058);
d! = 24 and L^d = 81 (the S4′ average's order count and block size, PROOF.md S4′ l.596-600); p_L = 11, the S4′
contour length bound at L = 3, d = 4 (NORMS.md §N1 conventions, from PROOF.md); L^j = 3, 9, 27 and
p_L^j = 11, 121, 1331 (the two comparators named in NORMS.md §N4 and in its FOR-OTHER-FILES item 8); p_L/L = 11/3,
quoted from NORMS.md [N1-corr 1] ("(p_L/L)² = (11/3)² ≈ 13.4").

## What nq1 computes

For L = 3, d = 4 and Setting SC's averaging operator Q (level-i 1-forms → level-(i+1) 1-forms, the linearised S4′
root map Q_root of PROOF.md L3g(a)-slice), the exact rational

  **𝔫_j := max_c Σ_b |Q^j(c, b)|**  for j = 1, 2, 3,

where c runs over level-j links and b over level-0 (fine) links, and Q^j := Q_{j-1}∘⋯∘Q_0. It also computes the same
quantity for Q := Q_str (the straight average), as the control (G4). Q^j is built iteratively as a composition of j
single-level transports — one level at a time, by translating a precomputed one-level row pattern — so that nothing
of size L^{dj} is ever formed. Numerators are integers over the exact denominator (d!·L^d)^j = 1944^j; the reported
value is the exact `Fraction`.

Only the two row-ℓ¹ quantities and the gates are computed. No kernel of the chain, no covariance, no minimiser and no
measured constant enters; nothing here bears on (H-K), (N-loc), (N-bg) or any other clause of (H-C).

## Verdicts (pre-registered; a failure is reported as a FAIL and voids the corresponding claim)

Put **R_j := 𝔫_j / L^j**. A priori R_j ≤ (p_L/L)^j = 11/3, 121/9, 1331/27.

- **nq1-1 (BOUNDED).** PASS the "bounded" reading iff R_j ≤ 11/3 for every j ∈ {1, 2, 3} AND R_3 − R_2 ≤ R_2 − R_1.
  Consequence if it holds: 𝔮_0 bounded at the computed j, 𝔮_0 ≥ max_j R_j; COMPUTED (exact) evidence for (N-Q), not a
  proof of boundedness in j.
- **nq1-2 (POLYNOMIAL).** PASS the "polynomial" reading iff some R_j > 11/3 AND
  (R_3 − R_2)/(R_2 − R_1) ∈ [1/2, 2]. Consequence: NORMS.md [N1-corr 1] case 2, C_♭^{(k)} ≲ k².
- **nq1-3 (CRUDE).** PASS the "crude" reading iff R_3 ≥ (1/2)(p_L/L)³ = 1331/54. Consequence: [N1-corr 1] case 3.
- **nq1-4 (OTHER).** If none of nq1-1/2/3 fires: no verdict; the numbers are reported and the three-case reading is
  declared unresolved at j ≤ 3.
  These four are mutually exclusive by construction except that nq1-2 and nq1-3 can both fire; if they do, the
  reported verdict is CRUDE and the ambiguity is disclosed.

## Correctness gates (ALL must PASS; any FAIL voids every verdict above)

- **(G1) slice identity.** The one-level row of Q built from the S4′ contours equals (row of Q_str) − (row of d∘h),
  entrywise and exactly, with Q_str and h built independently from their own definitions
  (Q_str A(X,μ) = L^{-d}Σ_{y∈B(X)}Σ_{m<L}A_μ(y+me_μ); h(A)(X) = avg_σ avg_{y∈B(X)}∫_{P^σ(c_X→y)}A). FAIL on any
  entry mismatch.
- **(G2) constant reproduction.** For every direction pair (ν_0, μ) and j ∈ {1, 2, 3}: applying the computed Q^j row
  for a level-j link of direction μ to the constant 1-form A_ν ≡ δ_{νν_0} gives exactly L^j if ν_0 = μ and exactly 0
  otherwise. FAIL on any deviation (this is Q(const) = L·const together with h(const) = 0 by centring).
- **(G3) pure-gauge covariance.** For λ(x) := c·x + (a non-linear test term) on level-0 sites, the computed Q^j row
  applied to d_0λ equals λ(far root) − λ(near root) exactly, for j ∈ {1, 2, 3}. FAIL on any deviation.
- **(G4) straight-average control.** With Q := Q_str the same code path returns exactly L^j for j ∈ {1, 2, 3}, with
  every entry ≥ 0. FAIL otherwise.
- **(G5) direction invariance.** 𝔫_j does not depend on which direction μ the level-j link c has (S4′ is covariant
  under axis permutations and reflections, PROOF.md S4′ / check c8). All four directions are computed and must agree;
  FAIL otherwise. (This is also what licenses writing max_c as the value at one c: Q^j is covariant under level-j
  translations, so only the direction can matter.)

## Not success

A PASS on nq1 is an exact statement about j = 1, 2, 3 only. It is NOT a proof that 𝔮_0 is bounded in j; only a
written-out all-j argument is, and that argument must stand on its own in NQ_CHECK.md. No claim in NORMS.md, PROOF.md
or any other file may be upgraded on the strength of nq1 alone, and this check says nothing about (N-loc) or (N-bg).
