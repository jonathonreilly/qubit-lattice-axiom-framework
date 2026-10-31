# checks/nd1_criteria.md — pre-registered criteria for check nd1 (target T55-P, file NQ_DEF.md)

Written 2026-10-28 21:56 UTC, **before `nd1_qrow.py` existed**. No constant below is derived in session 25.
Provenance of every constant used as a threshold:
- **L = 3, d = 4, L odd, block B(X) = LX + {0,…,L−1}^d with root c_X = LX + (L−1)/2** — Setting SC's own hypotheses,
  PROOF.md "Setting SC (linearised soft chain)" and LINEAR_PACKAGE.md §1.1. Pre-session.
- **L^j = 3, 9** — arithmetic in L.
- **𝔮₀ = 1 + d(L+1)/(2L) = 11/3 and the sharp form L^j + (d(L²−1)/(2L))(L^j−1)/(L−1) = 25/3, 91/3** — NQ_CHECK.md
  Theorem NQ-1, a **session-24** file. Permitted as a threshold (not session-25).
- **p_L = 11** — PROOF.md "`p_L := 5L - 4`". Pre-session.
- **205/27, 2021/81** — NQ_CHECK.md §Q2 and REVIEW_NQ_S1.md NQ-18, both **session-24**. Used only as the
  reproduction target of gate C, not as a threshold for any new claim.

Exact `fractions.Fraction` / integer arithmetic, plain python, `python3 -I`, one process, single thread, no numpy,
no BLAS, no numeric lock (brief rule 6's exemption for exact rational arithmetic). `nice -n 10`.

## The operators built, each from its primary definition only

All rows are anchored at the coarse site 0, in level-0 relative coordinates, so the block is B = {−1,0,1}^d and the
far root is c_Y = Le_μ.

1. **Q_root** — PROOF.md "**S4' [S3] Order-averaged averaging**": `T^σ_y = P^σ(c_X → y) · S_y · P^σ(c_Y → y + L e_μ)^dag`,
   averaged over the d! orders σ and the L^d sites y ∈ B(X); LINEAR_PACKAGE.md "the averaged link is
   Q_rootA(X, μ) := avg_{σ,y}∫_{T^σ_y}A (the "root map")".
2. **Q_str^LP** — LINEAR_PACKAGE.md: "(Q_strA)(X, μ) := L^{-4}Σ_{y∈B(X)}Σ_{j<L}A_μ(y + je_μ)". L^d block legs,
   weight L^{−d}.
3. **Q_str^NORMS** — NORMS.md §N1 Conventions: "Q_str B(c) := L^{−(d−1)}Σ_{paths}Σ_{b∈path}σ_bB_b over the L^{d−1}
   straight paths of L links". L^{d−1} transverse paths, weight L^{−(d−1)}; path for transverse offset t = the L
   links (t + je_μ, μ), j < L, t on the near face (t_μ = −(L−1)/2).
4. **h** — PROOF.md L3g(a)-slice / LINEAR_PACKAGE.md: "h(A)(X) := avg_σavg_{y∈B(X)}∫_{P^σ(c_X→y)}A".

## Gates. Every gate has a designed-FAIL control. A control that does NOT fail voids its gate.

| id | statement | PASS | designed-FAIL control | the control must |
|---|---|---|---|---|
| **A** | slice identity: `Q_root = Q_str^LP − d∘h` entrywise, all d directions | 0 differing entries in all 4 | **A′**: the same comparison with `Q_str^NORMS` in place of `Q_str^LP` | **FAIL** (≥ 1 differing entry), in all 4 directions |
| **B** | Setting SC's Q is **not** norm-L: `‖Q_root‖_{∞→∞} > L` | strict inequality, all 4 directions | **B′**: the same code path with `Q_root := Q_str^LP` | **FAIL** the `> L` test, returning exactly L |
| **C** | reproduction: `‖Q_root^{(1)}‖ = 205/27` and `‖Q_root^{(2)}‖ = 2021/81`, and both ≤ the session-24 sharp bound (25/3, 91/3) and ≤ 𝔮₀L^j | both exact values match and both inequalities hold | **C′**: compare against the *crude* one-level iterate bound `p_L^j = 11, 121` and against `L^j = 3, 9` | the values must lie strictly **between** L^j and p_L^j at both j (a criterion that fails if either frame is the right one) |
| **D** | telescoping at j = 2: `Q^{(2)} = Q_str^{(2)} − D_2[ev_1 h_0 + h_1 S_0]` entrywise | 0 differing entries, all 4 directions | **D′**: the same with `D_2`'s far-end shift taken as `Le_μ` instead of `L²e_μ` | **FAIL** (≥ 1 differing entry) |
| **E** | root covariance through the composite: `Q_root^{(j)}(d_0λ) = λ(L^je_μ) − λ(0)` for a non-linear λ, j = 1, 2 | exact equality, all 4 directions | **E′**: the same with `Q_str^LP` in place of `Q_root` | **FAIL** (Q_str∘d = d∘block-mean, not d∘ev, so a non-linear λ must give a different value) |

λ for gates E/E′ is fixed in advance as `λ(x) := x₀³ + 2x₁² − x₂x₃ + 5x₀` (non-linear in every coordinate that
matters, so that a block mean and a root value differ).

## Pre-registered verdicts

- **(V1)** A PASS and A′ FAIL ⟹ the slice identity `Q_root = Q_str − d∘h` is about LINEAR_PACKAGE's Q_str (the L^d
  block legs) and **not** about NORMS §N1's Q_str; NORMS §N1's convention line defines a different operator.
- **(V2)** B PASS and B′ FAIL ⟹ **𝔮₀ = 1 is FALSE for Setting SC's Q**, with the explicit witness ‖Q‖/L at j = 1;
  the "straight average ⟹ 𝔮₀ = 1" route is unavailable, not merely unproven.
- **(V3)** C PASS ⟹ the session-24 exact values reproduce under an independent implementation, and the session-24
  analytic bound dominates them.
- **(V4)** D PASS and D′ FAIL ⟹ Theorem NQ-1's Step-1 operator identity holds at the first non-trivial composite,
  with the far-end offset pinned.
- **(V5)** E PASS and E′ FAIL ⟹ the constructed operator really is the **root** map (endpoints at the roots), not a
  block-mean map; this is the gate with power over "did I build the right operator at all".
- **Any gate whose control does not fail is VOID and is reported as void.** Any gate that fails is reported as a
  FAIL with this criteria file and the script output unaltered, and any re-run is done under a new id.

## Not success
Reporting a PASS whose control also passed; adjusting λ, the block convention or the path convention after seeing a
result; treating gate C's reproduction of session-24 numbers as a proof of (N-Q) for all j (it is evidence at j ≤ 2
only — the all-j statement is an analytic argument in NQ_DEF.md §D3, not a computation).

## Not run, and why
`j = 3` (‖Q^3‖ = 6115/81 in NQ_CHECK §Q2 and REVIEW_NQ_S1 NQ-18): the row has ~4.1·10⁶ entries and ≥ 480 MB was
needed by both previous implementations. It adds a third data point to a question already settled analytically, on a
machine shared with seven agents. Declared here, in advance, as not attempted.
