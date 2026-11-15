# cm55 — pre-registered criteria (written 2026-10-29 before any cm55 script exists)

Owner: COFM55.md (Opus 5.5 worker, claude-opus-5-5). Exact integers / fractions.Fraction only; no floats in any verdict;
logarithms only through rigorous rational enclosures. Single thread, `python3 -I`, no third-party modules.
Nothing here can decide k- or T-uniformity; the checks decide finite combinatorial/arithmetic claims only.

Conventions (fixed now). d = 4, L = 3. Level-l sites are integer 4-vectors on the level-l torus of side T·L^{k-l};
coarse position of a level-l object = L^{l-k}·(its base point); distance = ℓ¹ torus distance of coarse positions on
(R/TZ)^4 (per coordinate min(|Δ| mod T, T − |Δ| mod T)). T = 6 coarse units (large enough that no wrap shortens any
distance ≤ 5). Roots = block centres (level-(l+1) site X has level-l root L·X + (L−1)/2·(1,1,1,1); its level-0 avatar is
L^{l+1}X + (L^{l+1}−1)/2·(1,1,1,1)). Axial paths: monotone lattice paths from the root to y in a fixed coordinate order;
the order-averaged h_l uses all 24 orders; the support of h_l(·)(X) is the union over orders and targets y ∈ B(X) of the
links traversed (all traversals of a given link have the same sign, so no cancellation; this is re-checked, item L0).

## Part A — locality radii (script cm55_loc.py)

- **L0 (sign consistency, sanity).** For every block-interior level-l link b and every (order, target) path through b,
  the traversal sign is the same. PASS iff no link is traversed with both signs. (Can fail on an indexing error.)
- **L1 (Lemma FLUX, weighted cost).** k = 2, l ∈ {0, 1}, every coarse link (X, μ) with X in one fixed cell and μ = 1..4:
  D_F(l) := max over the read set {(Z, μ): Z ∈ B_l(X), Z + e_μ ∉ B_l(X)} of dist(X, L^{l-k}Z).
  **PASS iff D_F(l) = 4(1 − L^{l−k}) exactly for both l, and D_F(l) < 4.** (Claim: FLUX costs e^{4m}.)
- **L2 (DEC subtraction Q_{k−1}^T b, weighted cost).** k = 2, every level-1 link ℓ = (y, μ) in one coarse cell:
  read set = {(X(y − i e_μ), μ): 0 ≤ i < L} (Q_str^T) ∪ {(X′ − e_ν, ν), (X′, ν): ν = 1..4} if h^T(·)(ℓ) ≠ 0 (X′ := the
  block of ℓ). D_Q := max dist(L^{-1}y, X̃) over ℓ and the read set (X̃ the coarse link's base site).
  **PASS iff D_Q ≤ 11/3** (= 4(L−1)/L + 1; claim: the subtraction costs ≤ e^{(11/3)m}). The exact D_Q is reported.
- **L3 (composite straight push-down transposes).** k = 2, (a, b) ∈ {(0,1), (1,2), (0,2)}: for a level-a ν-link with base
  y, the read set of (Q_str^{(a→b)})^T is {(Y, ν): y ∈ B_b(Y) + t e_ν for some 0 ≤ t < L^{b−a}} (level-a units).
  D_P(a, b) := max dist. **PASS iff D_P(a, b) = 4(ρ_b − ρ_a) + ρ_b·(1 − ρ_a/ρ_b)·0 + ρ_b exactly, i.e. D_P = 4(ρ_b − ρ_a) + ρ_b,
  for all three pairs.** (Claim used for C(j), T_i and the residual push-downs: cost < e^{5m}.)
- **L4 (Lemma FT (iv), funnel read radius).** k = 2 and k = 3 (k = 3 only for l = 2, cell-restricted enumeration),
  every level l ≤ k − 1 handled, every block-interior level-l link b with h_l^T(·)(b) ≠ 0, every l′ ≤ l: read set =
  the level-l′ links (Z′ − e_ν, ν), (Z′, ν) (ν = 1..4) where Z′ is the level-l′ site whose level-0 avatar is the level-0
  root of X(b). D_FT := max dist over all of these. **PASS iff D_FT ≤ 2** (FT (iv)'s "total displacement ≤ 2", in ℓ¹).
  The exact value is reported (prediction, not a criterion: 5/3).

Designed-FAIL controls (each must FIRE, i.e. the stated false claim must be violated by the enumeration):
- **C1:** D_F(1) ≤ 4(1 − L^{−1}) − L^{−1} (a radius one level-1 step too small) — must be FALSE.
- **C2:** D_Q ≤ 4(L−1)/L (ignoring the e_μ / e_ν step) — must be FALSE.
- **C3:** D_P(0, 2) ≤ 4(ρ_2 − ρ_0) (ignoring the shifted block) — must be FALSE.
- **C4:** with CORNER roots (root of X at L·X, avatar L^{l+1}X), the FT (iv) claim D_FT ≤ 2 — must be FALSE
  (shows the constant e^{2m} depends on the centre convention and that L4 can fail).

## Part B — rigorous numbers (script cm55_num.py)

- **N1:** rational enclosure [lo, hi] of ln 2 from 2·atanh(1/3) with a geometric tail bound; PASS iff 0 < hi − lo < 10^{-40}
  and the enclosure contains the Fraction 6931471805599453/10^16 (sanity).
- **N2 (size of m_Y, BFT_A §38.10's "m_Y ≤ 1.67·10^{-4}").** m_Y ≤ ln 2/(16·L^c) with L^c ≥ 260. **PASS iff hi/4160 ≤ 167/10^6.**
- **N3 (explicit-part weight in GU_m).** For L^c ≥ 260 and m ≤ ln 2/(16L^c): 4(L^c + 4) ≤ (41/10)L^c, and
  e^{4m(L^c+4)} ≤ 2^{(L^c+4)/(4L^c)} ≤ 2^{264/1040} ≤ 6/5. **PASS iff 260·41/10 ≥ 4·264 and 6^{1040} ≥ 2^{264}·5^{1040}.**
- **N4 (Lemma BW's coefficient at m_Y).** ¼·2^{4.2/16} ≤ ½ ⟸ 2^{42/160} ≤ 2: **PASS iff 42/160 ≤ 1** (sanity only).
- **N5 (which branch of m_Y binds for the tabulated strips).** For m_*′ ∈ {273, 384, 306, 140, 226, 216}/10^4 (LINEAR_PACKAGE
  §4 table): m′/2 = m_*′/6. **PASS iff min m_*′/6 > hi/4160** (then m_Y = ln 2/(16L^c) whenever L^c ≥ 260).
- **N6 (informational, no verdict):** the product of every e^{cm} locality factor used in COFM55 (c ≤ 40 in total) at
  m = hi/4160: report an upper bound for e^{40·hi/4160} via a rational exp enclosure.

Designed-FAIL controls:
- **C5:** hi/4160 ≤ 166/10^6 — must be FALSE (lo/4160 > 166/10^6).
- **C6:** at L^c = 100: 4(L^c + 4) ≤ (41/10)L^c — must be FALSE.

## What the run can and cannot decide
It decides: the exact locality radii used for the weighted constants of FLUX, DEC, the push-downs and FT (iv) at d = 4,
L = 3, k ≤ 3; and the arithmetic of m_Y's size and of the explicit-part weight. It cannot decide any analytic statement
(Theorem GU_m, COF_m, CC-FUN_m), any uniformity in k or T, or the value of C_j (so m_Y itself is only bounded above).
VERDICT line: "VERDICT cm55: ALL PASS (all controls fired)" iff every PASS criterion passes and every control fires;
otherwise list the failures. No criterion may be edited after the first run; any change goes to an appended note.

## Amendment A1 (appended 2026-10-29T00:21Z, BEFORE any cm55 script exists; no output seen; the text above is not edited)
L3's exact-equality formula above is my arithmetic slip (re-derived on paper before scripting): a level-a ν-link with base
y = sY_0 + r (0 ≤ r < s, s = L^{b−a}) reads (Y_0, ν) at ℓ¹ distance ρ_a|r|_1 ≤ 4(ρ_b − ρ_a), and (Y_0 − e_ν, ν) only when
r_ν ≤ s − 2, at distance ρ_a|r|_1 + ρ_b ≤ ρ_a(4s − 5) + ρ_b = 5(ρ_b − ρ_a). So the predicted exact value is
D_P(a, b) = 5(ρ_b − ρ_a), not 4(ρ_b − ρ_a) + ρ_b. **L3 is re-registered as: PASS iff D_P(a, b) < 5ρ_b for all three pairs
(the load-bearing claim, cost < e^{5m}); the exact value is reported and compared with 5(ρ_b − ρ_a) as a prediction,
not as a criterion.** C3 is unchanged (4(ρ_b − ρ_a) must be violated). Nothing else is changed.

## Amendment A2 (appended 2026-10-29T00:23Z, BEFORE any cm55 script exists; no output seen; text above not edited)
N1's sanity clause is mis-stated: ln 2 = 0.69314718055994530941…, so the 16-digit truncation 6931471805599453/10^16 lies
≈ 9.4·10^{-18} BELOW ln 2 and cannot be inside an enclosure of width < 10^{-40}. **N1 is re-registered as: PASS iff
0 < hi − lo < 10^{-40} and 0 ≤ lo − 6931471805599453/10^16 < 10^{-16}.** Nothing else is changed.
