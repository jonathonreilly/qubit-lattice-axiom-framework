Reviewer model: claude-opus-5-5

# REVIEW55_NORMS — Opus 5.5 re-review of batch C4: NORMS and the (N-Q) chain

## PRE-STATED (written 2026-10-28T22:12:51Z UTC, before reading any batch file or deriving anything; only the shared brief and the lead's scope message have been read)

Batch files: NORMS.md, REVIEW_NORMS_S1.md (earlier review), NQ_CHECK.md, REVIEW_NQ_S1.md (earlier review),
NQ_DEF.md (session 25). Check ids: r55n_*. Criteria files checks/r55n_<id>_criteria.md written before
any script; exact rational arithmetic (python fractions / integers) only.

Targets (each gets CONFIRMED / NOT-VERIFIED / REFUTED):
T1. Theorem N1-15 and the composite contraction A_soft = 1/3, uniform in k: the count
    sum_{n>=1} 3^{3-n} = 27/2, the per-level ratio, and WHAT A_soft IS (a contraction of a map F_k on a
    space M with norm || ||_M? a per-level ratio of a row-sum norm of a trilinear form? a data-only rate /
    unattained infimum with honest rate L^{-theta}?). Adjudicate NBG_B's and THETAW's re-readings.
T2. NORMS's original per-level no-go, and REVIEW_NORMS_S1's withdrawal of it (either may be wrong).
T3. Proposition N1-8: Z_col = 156 is the column mass of the curvature kernel (L^d * Kbar ~ 9.7 plus
    (2/(d-1)) K_rho ~ 1.5), not "27 crossing links x spread"; and whether PROOF.md [S24-fix 1] states it
    faithfully.
T4. The weight-pair claim: BFT-1 needs theta_w^c = 2 and theta_w^r = d-1 = 3; no common theta_w in (0,2]
    works, with A = L^{d - theta_w^r - 2 theta_A}, theta_A = min(1, theta_w^c - 1).
T5. Theorem NQ-1: ||Q^j|| <= q0 L^j with q0 = 1 + d(L+1)/(2L) = 11/3; REVIEW_NQ_S1's "confirmed and
    strengthened".
T6. NQ_DEF: Setting SC's Q is Q_root (S4' order-averaged root map); ||Q|| = 205/27 > L = 3 (to be
    re-enumerated independently by exact finite combinatorics); any valid q0 >= 205/81; N1-15 therefore
    "unconditional" at d=4, trivial background, abelian/linearised, uniform in k and T — and which
    hypotheses that still silently rests on. Also NQ_DEF's claim that Q_str names two different operators
    (NORMS §N1 vs LINEAR_PACKAGE l.71).
T7. A session-25 worker's claim that NORMS Definition N^F-2's vertex norm (fraktur N) is identically +infinity
    for every nonabelian consumer, via NORMS's own Ward identity applied to a nested pure gauge.
T8. Every other PROVEN / REFUTED / struck verdict and every decision-changing number found in the five
    files (enumerated as found; spot-checks labelled as such).

What counts as a refutation (verdict REFUTED for a claim):
- F1. An exact recomputation (rational arithmetic / exhaustive enumeration) of a stated number gives a
  different value (e.g. sum 3^{3-n} != 27/2; ||Q|| != 205/27; q0 formula != 11/3 at d=4, L=3; Z_col
  decomposition not summing to 156 or not matching the stated kernel), with my value and derivation given.
- F2. The stated inequality/bound fails on an explicit instance I construct (counterexample), or its
  proof uses a step that is false (with the false step identified and the correct statement given).
- F3. A symbol in the claim denotes, at its file:line definition, a different object from the one the
  comparison needs (symbol collision), so the stated conclusion does not follow.
- F4. A stated quantifier/uniformity (uniform in k, T, all j, "unconditional") fails: a hypothesis is used
  that the claim does not list, or the bound depends on k/T/j where it says it does not.
- F5. For a REFUTATION / no-go / withdrawal being reviewed: the refuting argument contains a false step or
  answers a different object than the claim it strikes; then the refutation itself is REFUTED.
- F6. A cited line/string does not exist where cited (reported as a drifted or missing citation; this
  alone downgrades to NOT-VERIFIED, not REFUTED, unless the content is contradicted).
A claim is CONFIRMED only when I re-derived its load-bearing step myself; "the file says PROVEN" is not
evidence. Where I can only partially re-derive, NOT-VERIFIED with what is missing.

---

## Reading record (what was read, and how)

- **Read in full:** NORMS.md (918 lines), NORMS_LOG.md, REVIEW_NORMS_S1.md (887), NQ_CHECK.md (366), REVIEW_NQ_S1.md (636),
  NQ_DEF.md (671), checks/n1_exponents.py.
- **Read by string-located range:** PROOF.md header l.1-47 ([S24-fix 1]-[S24-fix 4], [S25-fix 3]); S4′ ("For each of the d!
  coordinate orders σ", l.763-766); Setting SC ("Setting SC (linearised soft chain)", l.2225-2235); Lemma E3 + CURV-F2
  diagnosis ("Z_col ≥ the L^{d-1} = 27 crossing links", l.6335-6390); c38 ("N3(T) := max_x", l.6586-6600); the M-form
  recursion (fixed-string grep `Mh^{(m)}`: l.1324, 2956, 3149, 3160); PROOF_session23_snapshot.md l.2785-2790, 2978-2982;
  LINEAR_PACKAGE.md l.50-100; REVIEW_S22.md l.383-433 (BFT statement, 𝔐); SQ.md (grep only: l.352, l.655, l.710);
  HANDOFF.md l.30-110; THETAW.md l.255-345, 690-705; NBG_B.md l.300-360, 425-475; NBG_A.md l.130-215, 518; TUNIF.md
  l.96-215; NLOC.md l.300-400.
- **Codex gpt-6-astra/max reviews used, read as on disk 22:20-22:40 UTC:** CODEX_REVIEW_TUNIF.md (complete: ends "Review
  completed: 2026-10-28 22:09:33 UTC" + stdout summary); CODEX_REVIEW_THETAW.md (it grew from 21.8 KB to 36.6 KB during my
  session; I re-read the final version: F1-F14 + summary table + stdout summary, complete); CODEX_REVIEW_NBG2.md (F1-F6 in
  full and its closing dependency graph; complete).
- **Deliberately NOT read:** nq1_qnorm.py, nq1_telescope_posthoc.py, nd1_qrow.py, nd1b_hnorm.py and both reviewers'
  scratch probes, so that my enumeration r55n_q1 shares no code with the session-24/25 computations it tests.
- **Line numbers:** every citation below is to the file as on disk 2026-10-28 ~22:30 UTC and is paired with a quoted
  string. NQ_DEF's PROOF.md citations (written ~22:05) have since drifted by +4 (e.g. its "l.5885" C_♭ formula is now
  l.5889, "l.5890" C_Δ ≤ C_♭ is l.5894, "l.5896" ε_br is l.5900); the strings exist.

## Checks run (criteria written first: checks/r55n_*_criteria.md, all three at 2026-10-28T22:27Z, before any script)

All exact `Fraction`/integer arithmetic, plain python, `python3 -I -B`, single process, < 1 s each, no numpy/BLAS, no lock.
- **r55n_q1** (checks/r55n_q1.py, out r55n_q1_out.txt): independent enumeration of Setting SC's Q from the S4′ definition
  (1944 contours per coarse link). **All 8 gates PASS.** ‖Q‖_{∞→∞} = **205/27** with support **459** in all four directions;
  ‖Q^{(2)}‖ = **2021/81**, support **47 385** (μ = 0, 3); Q_root = Q_str^{LP} − d∘h with **0** differing entries (all μ);
  the same identity with NORMS §N1's Q_str fails by **108** entries (both path placements, all μ — control fired 8/8);
  root covariance Q(d₀λ) = λ(c_Y) − λ(c_X) exact for a λ cubic in every coordinate, while Q_str^{LP}(d₀λ) ≠ it in **4/4**
  directions (control fired); ‖h‖ = 8/3 = avg_y|y − c_X|₁ = d(L²−1)/(4L); Q_str^{LP} support 135, longitudinal multiplicity
  profile 1,2,3,2,1 (/81); NORMS Q_str support 81; Q_str^{(2)} row sum 9, all entries > 0. *Limitation, stated as the
  session-24 review stated it of G1:* q1-C builds both sides from the same contour primitives, so it tests my construction,
  not check c8(f)'s nonlinear-to-linear step; its discriminating content is its control (q1-C′) and q1-D/q1-D′.
- **r55n_w1** (checks/r55n_w1.py): SU(2) Wilson cubic vertex T = D³S_W(1) in the exponential chart, exact. **All 4 gates PASS.**
  H(dλ, ·) = 0 for all 20 candidates; the hand-derived Ward identity T(dλ, Y, W) = ½[H(Y, [λ̄, W]) + H(W, [λ̄, Y])]
  (λ̄_b := λ_x + λ_y) holds **exactly in 20/20** candidates, and its designed-FAIL control (BCH coefficient 1) fails 20/20;
  **T(dλ, Y, W) ≠ 0 in 20/20** candidates (abelian control: 0 in 20/20); positive witness Z := [λ̄, dμ]:
  Σ_p|dZ_p|² = 48 and T(dλ, dμ, Z) = **24** = ½·48. Informational w1-4: on a periodic 3×3 torus a constant (harmonic) 1-form h
  has T(h, Y, W) ≠ 0 in 9/10 seeds.
- **r55n_a1** (checks/r55n_a1.py): exact arithmetic. **All 5 gates PASS** (series, exponent identities d = 2..7, single-θ_w
  infeasibility on a 1/1000 grid, 𝔮₀ identities and monotonicity, the quoted decimals). Informational a1-6: the pigeonhole
  column bound (d(d−1)/2)(L^dK̄ + (2/(d−1))K_ρ) = 6 × 11.2155 = 67.29.

---

# FINDINGS

## A. Theorem N1-15 and A_soft (target T1)

### r55n-A1 The single pullback D³E_k^br(1) = D³𝔉_k(1)[ζ^c·, ζ^c·, ζ^c·] — CONFIRMED (re-derived)
Locating string: NORMS l.89-93 "a SINGLE pullback by the chain-minimiser map ζ^c"; (I2) "D³E_k^br(1) = D³𝔉_k(1)[ζ^c·".
Derivation (mine). Let F(A, B) be C³, a(B) a C² family with F_A(a(B), B) ≡ 0, E(B) := F(a(B), B), ζ_v := (a′v, v).
Then E′ = F_B, and differentiating F_A(a(B), B) ≡ 0 once gives D²F[(h, 0), ζ_v] = ⟨h, F_AA a′v + F_AB v⟩ = 0 for every h, v.
Hence E″[u, v] = D²F[ζ_u, ζ_v] + F_A a″[u, v] = D²F[ζ_u, ζ_v]. Differentiating this identity in w gives
D³F[ζ_u, ζ_v, ζ_w] + D²F[(a″[w, u], 0), ζ_v] + D²F[ζ_u, (a″[w, v], 0)], and the last two terms are zero by the previous
display. So D³E = D³F[ζ·, ζ·, ζ·] exactly; no derivative of the minimiser map survives, and no per-level recursion appears.
This uses only a C² critical family (agreeing with CODEX_REVIEW_NBG2 F1; REVIEW_NORMS_S1 RN1-10's "needs a‴" is
harmless over-requirement). At the trivial point a′(0) is the linear composite chain minimiser (the quadratic part of
𝔉_k is Setting SC's chain energy; LINEAR_PACKAGE §1.3 "E(B_0, …, B_{k-1}; B_k) = ½||dB_0||² + Σ_{i<k}(κ_i/2)||QB_i - B_{i+1}||²"),
determined up to fluctuation gauge, which Lemma N1-2 absorbs. Premise imported, not re-proved: TOWER-VAR (a)-(c) (that
E_k^br is this F at a C² composite critical family; CODEX_REVIEW_NBG2 F1 calls the lattice identification CONDITIONAL on
the (CL-4) input — at the trivial background I accept it as PROOF.md's PROVEN-HERE import).

### r55n-A2 Lemma N1-1 (one coboundary or one residual per cubic term; M_W ≤ 6) — CONFIRMED at the trivial background
Locating string: NORMS l.197 "Lemma N1-1 (field-strength representation of the composite cubic vertex)".
Wilson half re-derived: for X ∈ su(N), X³ is anti-Hermitian so Re tr X³ = 0, tr X = 0, hence S_W = ½Σ_p|log U_p|² + O(X⁴);
BCH for the ordered four-link product gives log U_p = Σσ_iA_i + ½Σ_{i<j}[σ_iA_i, σ_jA_j] + O(A³); the cubic part of
½|log U_p|² is ⟨(dA)_p, Q_2(A)_p⟩ — exactly one coboundary; |𝔅_p(Y, W)| ≤ ½·6·2|Y|_∞|W|_∞ = 6. My r55n_w1 builds exactly
this cubic and its Ward identity checks exactly (20/20), so the construction is right. Soft half: with φ̂ = ½|ρ|² + O(ρ⁴)
(no cubic term in ρ; TOWER-VAR (c)'s normalisation, imported) and ρ = r_j + ρ_2 + O(A³), the cubic part is κ_jΣ_c⟨r_j(c), ρ_2(c)⟩ —
exactly one residual; M_S < ∞ is asserted, not evaluated (as the file says). Scope: trivial background only — consistent
with CODEX_REVIEW_NBG2 F3, which exhibits a zero-differentiated-leg family at a NON-trivial background; Lemma N1-1 does not
claim otherwise ("nor a statement at a non-trivial background").

### r55n-A3 The exponent counts, the series Σ_{n≥1} 3^{3−n} = 27/2 and the per-level ratio — CONFIRMED (with one loose count)
Locating strings: NORMS l.507-555 (Theorem N1-15, steps (1)-(5)); l.514 "13.5·𝔖"; l.517 "A_soft = 1/L = 1/3 < 1 in every d ≥ 2".
Re-derived: step (1) (d−2)k − k − k = (d−4)k; step (2) (d−1)k − 2k − k = (d−4)k; soft step (4) (δ_x in a potential slot):
volume dn of level-j links − n (potential sup) − (d−1)(n−1) (residual sup, J-str (c)) − n (second potential) + 1
(level-(j+1) leg) ⇒ (d−1) − n up to the constant L absorbed in 𝔖. General identity (r55n_a1 a1-2, d = 2..7):
d·n − θ_w^r(n−1) − 2θ_A n = (d − θ_w^r − 2θ_A)n + θ_w^r, whose n-coefficient at (θ_w^r, θ_A) = (d−1, 1) is **−1 for every d**.
So the per-level ratio of the soft bound is exactly L^{−1} for every d ≥ 2 and every L ≥ 2 (agreeing with RN1-13/RN1-24).
Series (a1-1): S_K = Σ_{n=1}^{K}3^{3−n} satisfies 27/2 − S_K = (27/2)·3^{−K} exactly, so Σ_{n≥1} = **27/2 = L^{d−1}/(L−1)** at
(L, d) = (3, 4); for other L the prefactor is L³/(L−1) (31.25 at L = 5; agrees with CODEX_REVIEW_TUNIF F8).
**One count in step (3) is loose (new):** NORMS l.541-543 sums |r_j(δ_x)| with "n_link(j) = dL^{dn}", but r_j := QB_j − B_{j+1}
is a **level-(j+1)** 1-form (PROOF.md Setting SC: "Residuals r_i := QB_i - B_{i+1} (level-(i+1) 1-forms)"), so the correct
count is dL^{d(n−1)} and the residual ℓ¹ mass exponent is **n − 1**, not n + (d−1) (Remark N6-1's table row, l.563). The
printed bound is still a valid upper bound (it over-counts by L^d), and step (4) — which does carry (d−1) − n — is the
dominant term, so A_soft = 1/L and the sum are unaffected.

### r55n-A4 Theorem N1-15 as a theorem — CONFIRMED as a CONDITIONAL theorem; inputs named
Locating string: NORMS l.507 "PROVEN-HERE given (N-Q) and (N-loc)".
I re-derived the load-bearing steps (A1, A2, A3 above) and accept as imported premises the frozen LINEAR_PACKAGE v1.1
d = 4 results (I3) N2-lin (C_f, C_R "absolute, uncomputed"), (I4) J-str (b)(c) (I re-derived the Euler–Lagrange relation
κ_{i−1}r_{i−1} = κ_iQ^Tr_i, the co-closedness d*r_i = 0 by induction from the level-0 equation, and ‖Q_str^T‖_{∞→∞} = L·L^{−d}
= L^{1−d} from the column count), (I5) N2-exp′ locality, and TOWER-VAR (a)-(c). With (N-Q) now proven (E1 below) the
theorem is **CONDITIONAL on (N-loc)** in NORMS's own form, which has two clauses: a whole-torus weighted sup bound for the
potentials and an ℓ¹-mass bound for the same representative (l.422-423). Two repairs travel with it: Lemma N1-11's
constant (RN1-19: "|d_kλ|_∞ ≤ 2|Y|_∞" is not justified; the honest bound carries c_AX R_eff) and Lemma N1-11 being a
statement on a box of unfixed side R_eff, with a data change at level k that step (5) does not track (NLOC Theorem NL-3
step (3) — "The family (b^{(j)}) is the chain minimiser for the datum Y − d_k(ev^kλ_0)" — supplies the admissibility
correction; NLOC is batch C8 and was not reviewed by me). Status: **PROVEN given (N-loc) [or given NLOC's fixed-T
bypass], at d = 4, trivial background, uniformly in k** — the "for every d ≥ 2" of l.509/l.575 is exponent bookkeeping only,
because (I3)-(I5) are d = 4 theorems (LINEAR_PACKAGE §1.1 "d = 4"); agreeing with RN1-12.

### r55n-A5 What A_soft actually is — NBG_B CONFIRMED; THETAW REFUTED as applied to Theorem N1-15
A_soft = 1/L is **the common ratio of a geometric majorant**: the soft-vertex part of N3(D³E_k^br(1)) is bounded by
Σ_{n=1}^{k}𝔖·L^{(d−1)−n}, n = k − j, and consecutive terms differ by exactly L^{−1}. It is not the Lipschitz constant of any
map: NORMS itself says "the recursion is not a recursion, it is a convergent geometric series" (l.94-95).
- **NBG_B §7.1 (l.313-336): CONFIRMED.** (1) The theorem bounds a trilinear form in N3, the absolute row-sum norm defined at
  NORMS l.106; 𝔐 (REVIEW_S22 l.389-397: Hölder curvature leg, divergence-form source norm Y with ω_l) appears nowhere in its
  statement or proof — and NORMS's own "𝔐-restricted" vertex norm 𝔑 is +∞ on this very object (G1 below), so the theorem
  could not have been stated in it. (2) It is therefore not "one contraction for 𝔉_k in 𝔐" (REVIEW_S22 l.422-423). I did not
  adjudicate NBG_B's further "wrong direction / cannot reach (G♯_0-field)" point (outside this batch).
- **THETAW §T4.2 (l.332-338) and its F-item 2 (l.696-699): REFUTED as a statement about A_soft / Theorem N1-15.** Theorem N1-15
  is a statement about one Taylor coefficient at the trivial point; its only inputs are responses to level-k data. No source
  weight θ exists in it, so there is no θ → 1 limit to approach: the ratio 1/L is attained exactly by the bound, for every k.
  "1/3 is an infimum that is not attained" and "the honest composite rate is L^{−θ}" describe a **different, not-yet-defined
  object** — a contraction for a nonlinear problem whose residual-type sources sit in a θ-weighted norm. For that object the
  L^{−θ} rate is itself only a formal exponent count: CODEX_REVIEW_THETAW F5 (an upper bound "does not establish the 'and no
  further' optimality") and F10 (at the endpoint θ_w^r = 2 + θ the Σ-aggregated estimate loses a factor k) — I agree with both
  — so it is **NOT-VERIFIED** there. Correct statement: *A_soft = 1/L is the exact level ratio of the data-only, trivial-background
  N3 bound; any nonlinear analogue has no proven rate yet.*

### r55n-A6 NORMS's definition "N3(T) := max_x Σ_{y,z}|T(x,y,z)| = sup{|T(δ_x, Y, W)| : |Y|_∞, |W|_∞ ≤ 1}" — the "=" is REFUTED
Locating string: NORMS l.106. CODEX_REVIEW_NBG2 F4's counterexample, re-checked by hand: the symmetric tensor with
T111 = T112 = 1, T122 = T222 = −1 has slices [[1, 1], [1, −1]] and [[1, −1], [−1, −1]]; each has absolute entry sum 4, but
sup_{|Y|,|W|≤1} YᵀMW = max_W(|W₁+W₂| + |W₁−W₂|) = 2. So max_xΣ|T| = 4 > 2 = max_x sup|T(δ_x, Y, W)|. **I agree with Codex.**
Consequence: the consumer's C_♭ ("N_0(D³E_i[w]) ≤ C_♭^{(i)}|w|_∞", PROOF.md l.6343) is the *smaller*, bilinear quantity;
the coefficient-row quantity is stronger. **Theorem N1-15 is unaffected:** every step of its proof is a Hölder chain of
operator norms (ℓ¹ of a vector, M_W/M_S coefficient masses, row-ℓ¹ norms of ζ^c_sm and d_0ζ^c_0), which bounds the absolute
coefficient sum Σ_{y,z}|T(δ_x, δ_y, δ_z)| as well. Correction: define N3 as the absolute row sum and note N3 ≥ C_♭-object.

### r55n-A7 The scope label "abelian / linearised" for Theorem N1-15 — CONFIRMED with a correction to its wording
NQ_DEF §D6.2 item 3 (l.489) says "Abelian / linearised. One real colour component around the trivial SU(N) background".
That describes the **linear chain map** ζ^c (N²−1 copies of the abelian problem, LINEAR_PACKAGE §1.1), which is all
Theorem NQ-1 concerns. It does **not** describe the vertex: in one real colour component the cubic vertex at the trivial
point is zero (Wilson: r55n_w1's abelian control gives T ≡ 0; soft: for U(1) the quadratic part ρ_2 of the polar part of
M̄V^{−1} vanishes). Theorem N1-15's whole content is the **nonabelian** cubic vertex (M_W, M_S are commutator masses) pulled
back by the abelian linear map. Correct regime: *SU(N), trivial background, linear (componentwise) chain response, d = 4,
L ≥ 3 odd*. Read literally as "U(1)", the theorem would be vacuous.

## B. NORMS's per-level no-go and REVIEW_NORMS_S1's withdrawal of it (target T2)

### r55n-B1 Theorem N1-13 (i) (weight invariance) and check n1-D — the withdrawal's finding CONFIRMED
Locating strings: NORMS l.458 "Theorem N1-13 (NO-GO: A ≥ 1 in every scale-covariant norm family)"; checks/n1_exponents.py,
function n1D. I read the script: `emis` is computed twice and discarded, and the verdict quantity is
`total = k * eA + k * ((d - 4) - eA)`, which equals k(d−4) identically in eA (the line before it carries the comment
`# placeholder, replaced below`). **n1-D cannot fail for any input** (RN1-3 is right). n1-A reduces to integer identities
(`ok &= (4 - 4 == 0) and ...`) and n1-B's general-d clause likewise; n1-C does test that two orderings agree (RN1-4 right).
Analytically, (i) holds for the reason RN1-2 gives: the weights L^{θ(k−l)} equal 1 at l = k, so the level-k answer cannot
depend on them — a bookkeeping identity, not a no-go ingredient. There is a second, independent reason the 𝔑-formulated
statements are empty: **𝔑 = +∞ on every nonabelian vertex** (G1), so Theorem N1-12's "𝔑_{i+1}(T_{i+1}) ≤ A_per·𝔑_i(T_i) + B_per"
(l.444) and the 𝔑-rescaling in the proof of (i) compare ∞ with ∞.

### r55n-B2 Theorem N1-13 (ii) (A_per ≥ 1 forced) — NOT ESTABLISHED; the withdrawal is CORRECT and is not itself an error
(ii) concludes A_per ≥ 1 from an **upper** bound A_per ≤ 𝔠·L^{d−4}(L²K̄)^a: no field, direction or kernel row realising
growth is exhibited, and "scale-covariant norm family" is used at l.86, l.458, l.869 and never defined (grep confirms exactly
three occurrences; RN1-1 right). So the no-go is not proven, and REVIEW_NORMS_S1's withdrawal (Part K fix 1; PROOF.md
[S24-fix 1a]; HANDOFF "WITHDRAWN" item 2) **does not delete correct work**. Checking the withdrawal in the other direction:
the withdrawal does NOT claim A_per < 1 is achievable, and I agree with its reading "probably true, not proven". My own
reason it is probably true is cleaner than the file's: at tree level the coarse Wilson cubic vertex is an approximate fixed
point of the per-level pullback (c38 C: c_2, c_3 → 1 in the smooth limit), so in any norm given by the same formula at every
level the per-level linear map has a norm ≳ 1 on that direction. That is exactly pre-registered outcome **(O3)** (marginal
direction, possibly zero drive, irrelevant complement), which neither file tested; it would not kill the per-level route.
**Verdict on the pair:** NORMS's no-go — NOT-VERIFIED (conclusion plausible, proof absent); the withdrawal — CONFIRMED.
"The per-level route is OPEN, not refuted" (PROOF.md [S24-fix 1a]) is the correct disposition.

### r55n-B3 REVIEW_NORMS_S1's supporting arguments, checked one by one
- **RN1-7 (𝔠_ax ≥ 5.46 from Proposition N1-10's own bracket): CONFIRMED.** NORMS l.371's bracket is
  |B|_∞ + [(d−1)L²K̄ + K_ρ]|d_1B|_∞ once |d(ζB)| ≤ K̄|d_1B| is used; bounding it by 𝔠_ax(|B| + |d_1B|) needs
  𝔠_ax ≥ 3·9·0.1202 + 2.219 = 5.4644.
- **RN1-8 (𝔠_vol = c_m = coth(m′/2)^d, "no gain" at 𝒦's near-field rate): REFUTED in part.** The max-versus-average slack
  does not need any decay input. By translation invariance under level-(i+1) shifts the column mass of 𝒦_Z depends only on
  the coarse-plaquette type, and Σ_{types in one cell} col = Σ_{fine p in one cell} row(p) ≤ n_τ(i)·K_p (the same double count
  as Proposition N1-8). Hence **max col ≤ (d(d−1)/2)·avg col, i.e. 𝔠_vol ≤ 6 at d = 4**, and 𝔠_vol = 1 if the representative is
  hypercubic-symmetric. So the rows of RN1-8's table with 𝔠_vol = 79.6 or 7.4·10⁶ are artefacts of routing through Corollary
  N1-9; with the file's own 𝔠_ax ≥ 5.46 the per-level bound is A_per ≲ 37·𝔠_vol ≤ 2.2·10², still far above 1. RN1-8's
  headline conclusion (the ≈10³ gain is not established by the file's estimates) survives; its "no gain at all" row does not.
- **RN1-6 ("A_per ≤ 1.38 contradicts the measured R_3(ℤ⁴) ≥ 1.40 unless 𝔠 > 1.014"): REFUTED as a contradiction.** R_3 is a
  ratio of N3's of the full level-1 vertex (Wilson pullback **plus** the soft vertex: c38 B, PROOF.md l.6596 "Wilson part
  0.5152 / 0.7623, soft part 3.1428 / 3.9038"), whereas A_per bounds only the linear part M_{i+1} ≤ A_per M_i of an ℓ¹
  coefficient mass; the soft drive is B_per. The two numbers are not comparable, so no contradiction arises (and none is
  needed for RN1-7/8's point).
- **RN1-7b ("I verified the cancellation: 𝔑_{l,0}(T) = N3(T)/(2(d−1)) exactly", REVIEW_NORMS_S1 l.441): REFUTED.** See G1:
  𝔑 = +∞ on every nonabelian vertex, while N3 is finite. Only N3 ≲ 2(d−1)·𝔑 (δ_x in the ℓ¹ slot) holds. The same error is in
  NORMS Remark N^F-3 (iii) (l.178-182) and propagated to TUNIF §U2.2 l.158 ("N3 is NORMS Definition N^F-2's vertex norm
  𝔑_{k,m} at m = 0") — harmless there because TUNIF's displayed object is the δ-form.

### r55n-B4 The "≈10³ gain per level" headline (NORMS l.82-84, l.456, n1-E) — NOT-VERIFIED
Arithmetic CONFIRMED exactly (r55n_a1 a1-5): Z_col·Z_row² = 1266.8703; (1 + Z_col)(1 + Z_row)² = 2327.1089;
1266.87/(9·0.1202) = 1171.08 and 1266.87/(9·0.1236)³ = 920.34. But these are 1266.87/(L²K̄)^a, i.e. **the gain with
𝔠_vol = 𝔠_ax = 1**, which the file's own displayed bounds do not deliver (B3). With the file's own constants the gain in
the *bound* is ≤ ≈34 (𝔠_vol = 1) and ≈6 (pigeonhole 𝔠_vol ≤ 6). The *measured* signed ratio R_3 = 1.13-1.40 is consistent
with a ~10³ gain over E3's absolute bound, and PROOF.md l.6490's sound statement already records it; NORMS's estimates do
not prove it.
*Erratum to B3/B4 (append-only correction, my own):* the c38 B string "Wilson part 0.5152 / 0.7623" is at PROOF.md
**l.6599** (the c38 block starts at l.6586), not l.6596; and the "sound statement" ("at least ≈ 20 times below E3's 1267")
is at PROOF.md **l.6624** (REVIEW_NORMS_S1 cited it as l.6490 in session-24 numbering).

## C. Proposition N1-8, Z_col = 156, and PROOF.md [S24-fix 1] (target T3)

### r55n-C1 Proposition N1-8 (mass balance ρ_col = [n_τ(i)/n_plaq(i+1)]·ρ_row) — CONFIRMED (re-derived); Corollary N1-9 superseded
Locating string: NORMS l.337 "Proposition N1-8 (mass balance): PROVEN-HERE". Re-derivation: for a kernel 𝔎(z, P) invariant
under level-(i+1) translations, Σ_{z ∈ cell_0}Σ_{all P}|𝔎(z, P)| = Σ_{P ∈ cell_0}Σ_{all z}|𝔎(z, P)| (shift each P back into
cell_0 and z with it), i.e. n_τ(i)·ρ_row = n_plaq(i+1)·ρ_col. For 𝒦 (fine plaquettes) the ratio is (d(d−1)/2)L^d/(d(d−1)/2)
= L^d; for 𝒦_ρ (coarse links) it is d/(d(d−1)/2) = 2/(d−1). Numbers (a1-5): L^dK̄ = 81·0.1202 = **9.7362**; (2/3)·2.219 =
**1.4793**; sum 11.2155; Z_col/(L^dK̄) = 16.03; Z_col/11.2155 = 13.92 ("≈ 14"). These are **average** column masses. The
needed **max** column mass follows without any decay input by the pigeonhole of r55n-B3: max ≤ (d(d−1)/2)·avg, i.e.
≤ 6 × 11.2155 = 67.29 (a1-6), and = avg for a hypercubic-symmetric representative. Corollary N1-9's c_m = coth(m/2)^d route
is correct but unnecessary and, at proven decay rates, far worse.

### r55n-C2 PROOF.md [S24-fix 1] — REFUTED as written (symbol collision Z_col vs 𝔎_col); RN1-7c CONFIRMED
Locating string: PROOF.md l.12-15 "**[S24-fix 1] PROOF.md's Z_col diagnosis (l.6211-6213) is WRONG.** ... NORMS.md Proposition
N1-8 proves by an exact mass-balance identity that Z_col is the **column mass of the curvature kernel**, L^d·K̄ ≈ 9.7 plus
(2/(d-1))K_ρ ≈ 1.5", and l.24-25 (after [S24-fix 1a]) "Proposition N1-8's correction of the Z_col diagnosis stands".
- **Two different objects share the role.** Z_col is defined in Lemma E3 (PROOF.md l.6341: "Z_col := max_cΣ_b|a'(b, c)|") —
  the column ℓ¹ mass of the **potential** branch map a′ (= ζ), measured **156.08** (c37 D2). The quantity Proposition N1-8
  bounds is 𝔎_col, the column mass of the **curvature kernel** 𝒦_Z (and 𝒦_ρ), ≈ 11.2 on average. 11.2 ≠ 156.08; Proposition
  N1-8 says nothing about a′. NORMS itself states the relation correctly — Z_col "is replaced by" 𝔎_col when the leg is
  measured through d₁X (l.329 "Z_col ↦ ‖𝒦_Z‖_{ℓ¹→ℓ¹} + ‖𝒦_{ρ,Z′}‖_{ℓ¹→ℓ¹}", l.355 "the replacement is ≈ 9.7 + 1.5 ≈ 11.2
  instead of 156"). [S24-fix 1]'s "Z_col IS the column mass of the curvature kernel" is the lead's mis-transcription.
- **PROOF.md's diagnosis is not wrong.** The sentence (now PROOF.md l.6382-6386, it drifted from the cited l.6211-6213:
  "Z_col ≥ the L^{d-1} = 27 crossing links of one coarse link times the spread, and absolute-value N_0 norms of a pulled-back
  third derivative count every fine leg at its sup size, whereas the d = 4 cubic vertex is marginal only after one leg is
  differentiated ... What is needed is a Lipschitz bound for Hess E_i^br in a field-strength (curvature-adapted) norm")
  is a heuristic about Z_col consistent with the measurement (156.08 ≥ 27), and its prescription is exactly what NORMS then
  did. As a strict lower bound "Z_col ≥ 27" is not proved anywhere (Jδ_c has mass 27 but x = −C⁰d*ιd₁δ_c could cancel part of
  it; RN1-7c's "TRUE" skips this), so the right label is *heuristic, consistent with c37*, not *wrong*.
- **"The wrong diagnosis made the per-level route look like a norm problem"** inverts the record: PROOF.md's diagnosis is the
  one that called it a norm problem.
**Correct statement for PROOF.md:** *"[S24-fix 1, corrected] PROOF.md's Z_col diagnosis stands as a heuristic (Z_col = 156.08
measured). NORMS.md Proposition N1-8 adds a different quantity: in the field-strength estimate the differentiated slot costs
the column mass of the curvature kernels, whose cell average is L^d·ρ_row(𝒦_Z) + (2/(d−1))ρ_row(𝒦_ρ) ≤ 9.74 + 1.48 at the
measured K̄, K_ρ (max ≤ 6× that by pigeonhole); the L^{d−1} crossing-link count is a property of the potential lift J and
does not enter that slot."* REVIEW_NORMS_S1 RN1-7c asked for exactly this ("must be reworded as an addition, not a
correction. As a correction it would put a false erratum into the master ledger"); the lead's [S24-fix 1a] did not apply it.
*Erratum to C2 (append-only):* the NORMS heading "(a) The differentiated slot: Z_col ↦ ‖𝒦_Z‖_{ℓ¹→ℓ¹} + ‖𝒦_{ρ,Z′}‖_{ℓ¹→ℓ¹}"
is at NORMS **l.335**, not l.329.

## D. The weight-pair claim (target T4)

### r55n-D1 "BFT-1 needs θ_w^c = 2 and θ_w^r = d − 1 = 3; no solution in (0, 2] under a single common θ_w" — CONFIRMED (algebra), with the requirement stated precisely
Locating strings: NORMS l.646-676 (§N7), l.665 "Consequence for the statement of BFT-1"; PROOF.md [S24-fix 3] l.32-36.
Re-derivation. From the general exponent (r55n-A3) the soft series is k-uniform iff θ_w^r + 2θ_A > d and the Wilson term iff
θ_w^c + 2θ_A ≥ d (it occurs once). With a single common θ_w = θ_w^c = θ_w^r ∈ (0, 2]: the cap **θ_A ≤ 1 alone** already gives
θ_w + 2θ_A ≤ 2 + 2 = 4 = d, so the strict soft inequality fails; with NORMS's θ_A = min(1, θ_w − 1) it reads 4 > 4 at θ_w = 2
and 3θ_w − 2 > 4 ⟺ θ_w > 2 below it. No solution (r55n_a1 a1-3 confirms on a 1/1000 grid, both forms). The cap θ_A ≤ 1 is a
genuine lower bound, which I re-derived: for pure-gauge data d_kλ with |d_kλ(b)| = 1, any admissible representative d_jμ_j
(nested, ev^{k−j}μ_j = μ_k + const) must accumulate a difference 1 over L^{k−j} level-j steps, so some level-j link carries
≥ L^{−(k−j)} — no representative has θ_A > 1. So the negative is robust and does not depend on the floor θ_A ≥ θ_w^c − 1
(which is only what the axial construction gives).
**Precision:** the route needs **θ_w^c ≥ 2 and θ_w^r > 2** (at θ_A = 1); (2, 3) is what the linear chain *delivers*
(Lemma N1-4; J-str (c)). NORMS states the precise version (l.673 "A < 1 holds on {θ_w^r > 2} ∩ {θ_w^c ≥ 2}"); PROOF.md
[S24-fix 3] ("met at d = 4 by (curvature θ_w^c = 2, residual θ_w^r = 3)") is fine; **[S25-fix 3] / NBG_B §8 l.454-455 "the
composite contraction requires θ_w^r = 3" is REFUTED as stated** — the requirement is θ_w^r > 2 (CODEX_REVIEW_THETAW F11's
witness r = 5/2 satisfies the reduced system; I agree with F11), though NBG_B's conclusion that no single exponent in (0, 2]
serves all four jobs is unaffected. "[S24-fix 3] … with a single common θ_w there is no solution in (0, 2] **for any
consumer**" over-generalises: it is a statement about this route's soft series.
*Erratum to D1:* NORMS "A < 1 holds on {θ_w^r > 2} ∩ {θ_w^c ≥ 2}" is at **l.674**, not l.673.

## E. Theorem NQ-1 and its review (target T5)

### r55n-E1 Theorem NQ-1: ‖Q^{(m)}‖_{∞→∞} ≤ L^m + (d(L²−1)/(2L))(L^m−1)/(L−1) ≤ 𝔮₀L^m, 𝔮₀ = 1 + d(L+1)/(2L) = 11/3 — CONFIRMED (re-derived)
Locating string: NQ_CHECK l.191 "§Q3 Theorem NQ-1 — (N-Q) for all j: PROVEN-HERE".
My derivation, from the two defining identities only. (i) **Slice identity** Q_i = S_i − D_{i+1}H_i: each S4′ contour is
near funnel + straight leg − far funnel, and the far funnel P^σ(c_Y → y + Le_μ), y + Le_μ ∈ B(Y), is exactly a path of h at Y;
averaging gives Q = Q_str + h(X) − h(Y) = Q_str − d∘h, on **all** 1-forms (r55n_q1 q1-C: 0 differing entries). (ii) **Root
covariance** Q_iD_i = D_{i+1}E_i: every contour runs c_X → c_Y, so ∫_T dλ = λ(c_Y) − λ(c_X) (q1-D exact, with a λ cubic in all
coordinates; the Q_str control fires in all 4 directions). Induction: Q^{(j+1)} = Q_jQ^{(j)} with
Q^{(j)} = S^{(j)} − D_jΣ_{i<j}E_{j−1}⋯E_{i+1}H_iS^{(i)} gives Q_jS^{(j)} = S^{(j+1)} − D_{j+1}H_jS^{(j)} and Q_jD_j = D_{j+1}E_j, hence
the same form at j + 1 (the new i = j term has an empty E-product). Norms (max row ℓ¹, submultiplicative): ‖S^{(i)}‖ = L^i
(non-negative entries, row sums L^{−d}·L^d·L = L); ‖E⋯E‖ = 1 (one unit entry per row); ‖H_i‖ ≤ avg_y|y − c_X|₁ = d(L²−1)/(4L)
= 8/3 (q1-G: equality, so no cancellation); ‖D∘G‖ ≤ 2‖G‖ (D acts on 0-forms: two terms in every d). Summing:
L^j + Σ_{i<j}2·(8/3)·L^i = L^j + (8/3)(L^j − 1) ≤ (11/3)L^j at (L, d) = (3, 4); generally 𝔮₀ = 1 + d(L+1)/(2L) (a1-4 checks the
closed-form identity for L ∈ {3,5,7}, d ∈ {2,3,4}, j ≤ 8, and strict decrease in odd L: 11/3, 17/5, 23/7, …, 305/101 → 3).
Nothing uses the starting level, and Q_i is the same operator at every level in own units, so it holds for any m
consecutive levels (REVIEW_NQ_S1 NQ-17's quantifier repair is right and is needed by Lemma N1-11 step (4)).
Numerical consistency (q1-F): computed 205/27 ≤ 25/3 and 2021/81 ≤ 91/3. Scope: the linear (componentwise) transport around
the trivial background; input (i) has no nonabelian analogue (PROOF.md L3g(a)-slice [R3-fix], quoted by both session-24
files), so NQ-1 does nothing for (N-bg).

### r55n-E2 REVIEW_NQ_S1 "(N-Q) is PROVEN … confirmed and strengthened" — CONFIRMED (one sub-item NOT-VERIFIED)
- NQ-10 (telescoping is an operator identity on all 1-forms), NQ-11-NQ-16 (the four norms; torus) — CONFIRMED by E1.
- NQ-17 (quantifier: any m consecutive levels) — CONFIRMED (the "strengthening").
- NQ-18 (205/27, 2021/81, 6115/81; supports 459 / 47 385 / 4 113 747) — CONFIRMED for j = 1, 2 by my independent code; j = 3
  not re-run by me (two prior independent computations agree).
- NQ-3 (the j = 1 BOUNDED clause was vacuous a priori: 𝔫₁ ≤ p_L = 11) — CONFIRMED (a contour has ≤ 4 + 3 + 4 = 11 links).
- NQ-20 (𝔮₀ = p_L/L only at L = 3) — CONFIRMED: L𝔮₀ = L + d(L+1)/2 vs p_L = L + d(L−1), equal iff L = 3 (a1-4: 11 = 11 at
  L = 3; 17 vs 21 at L = 5).
- NQ-21 ("G1 strengthens c8(f)" is wrong) — CONFIRMED; my own q1-C has the same limitation and I say so.
- NQ-24/NQ-25 (NORMS's polynomial estimate is a bookkeeping loss on the same operator; NORMS misdefines Q_str) — CONFIRMED
  (E4, F4).
- NQ-27 (NQ_CHECK over-reaches in moving Lemma N1-11 to PROVEN-HERE) — CONFIRMED, and it is worse than an over-reach of
  scope: as written Lemma N1-11 is a box statement with an untracked level-k data change (r55n-A4).
- NQ-19 (measured ‖hQ_str^{(i)}‖ = 8/3, 56/9, 488/27) — **NOT-VERIFIED** (not recomputed; optional sharpening only).

### r55n-E3 NQ_CHECK's other claims
- §Q1 "Setting SC's Q is Q_root, not the straight average" — CONFIRMED by string (PROOF.md l.2227 "Q is the linearised S4'
  map from level i to level i + 1 (Q_root of L3g(a)-slice, with the S4' order average)"; LINEAR_PACKAGE l.70). The J-str /
  SHIFT "conflict" is not one — CONFIRMED: SQ.md l.655 "Q := Q_str (§0.4; …)" is SQ's declared local convention (§0.4 at
  l.352 "Q_str may replace Q_root in linear computations"), and d∘Q_root^{(m)} = d∘Q_str^{(m)} since the difference is exact.
- §Q2/FOR-OTHER-FILES 5(b) "G1 … strengthens check c8(f)'s 2e-16 to an identity" (NQ_CHECK l.348) — **REFUTED** (agree with
  NQ-21): both sides of G1 are assembled from the same contour primitives; c8(f)'s content (the nonlinear S4/S4′ map on small
  U(1) fields linearises to Q_root) is assumed, not tested.
- §Q4 "Theorem N1-15: CONDITIONAL on (N-loc) ALONE" — CONFIRMED (given r55n-A4's repairs to Lemma N1-11).
- FOR-OTHER-FILES 1(a): the quoted NORMS sentence "The files are ambiguous about what Q actually is" does not occur in
  NORMS.md (fixed-string grep: 0 hits) — RN1-18's observation CONFIRMED; the nearest text is NORMS FOR-OTHER-FILES item 1
  "The evidence is mixed in the files".

### r55n-E4 The h^{(m)} recursion citation — REVIEW_NORMS_S1 RN1-21's "not found" is REFUTED
REVIEW_NORMS_S1 l.527 asserts that NQ_CHECK's "PROOF l.2787, l.2980: h^{(m+1)} = Mh^{(m)} + hQ^{(m)}" is "**not found** — the
notation h^{(m)} occurs **nowhere** in PROOF.md". A fixed-string grep for `Mh^{(m)}` finds it in the live PROOF.md at
**l.1324, l.2956, l.3149, l.3160** (e.g. l.3149 "h^{(m+1)} = Mh^{(m)} + hQ^{(m)} (L3g(a)-slice, IT-str)"), and in
PROOF_session23_snapshot.md at **l.1155, l.2787, l.2980, l.2991** — i.e. at exactly NQ_CHECK's cited lines in the snapshot
numbering (REVIEW_NQ_S1 NQ-5 had this right). (A regex grep with unescaped `^{` returns nothing, which is the likely cause.)
So NQ_CHECK's diagnosis of NORMS's j-growth ("an artefact of expanding Q^j with the block mean M … h^{(m+1)} = Mh^{(m)} +
hQ^{(m)}") rests on an object that **does** exist in PROOF.md (IT', Lemma IT-line). Substance unchanged: the M-form is
self-referential, the ev-form (E1) is not, and h∘d = M − ev links them; NORMS l.415's "Q_str d_iμ = d_{i+1}(μ|centres)"
conflates M with ev (Q_str∘d = d∘M by telescoping Σ_{j<L}; Q_root∘d = d∘ev) — RN1-23 CONFIRMED.
*Erratum to E1:* NQ_CHECK's "§Q3 Theorem NQ-1 — (N-Q) for all j: PROVEN-HERE" heading is at NQ_CHECK **l.174**, not l.191.

## F. NQ_DEF (session 25) (target T6)

### r55n-F1 "Setting SC's Q is Q_root (the S4′ order-averaged root map)" — CONFIRMED
NQ_DEF §D1.1 (l.97-108). Verified by string in the live files (PROOF.md l.2227; S4′ l.763-766; LINEAR_PACKAGE l.70-72), and
by the consumer: r_i := QB_i − B_{i+1} is defined with this Q (PROOF.md l.2234), so Lemma N1-11 step (4)'s
B_j = Q^jB_0 − Σ Q^{j−1−i}r_i is an identity only for Q_root (NORMS Lemma N1-4's Q_str version holds "modulo a level-j pure
gauge", l.274-276). Exactly one defining sentence exists (NQ_DEF's Q-F1 disposition is right).

### r55n-F2 "‖Q‖ = 205/27 > L = 3, so any valid 𝔮₀ ≥ 205/81 ≈ 2.531" — CONFIRMED by independent exact enumeration
r55n_q1 (my code, from the S4′ definition, sharing no code with nq1/nd1): row ℓ¹ = **205/27** with **459** nonzero entries for
each of the four directions; ‖Q^{(2)}‖ = **2021/81** (47 385 entries). Since 𝔮₀ ≥ sup_j‖Q^{(j)}‖/L^j ≥ ‖Q‖/L = 205/81, the
lower bound is right. It is not the best available: NQ_DEF's own j = 2 value gives 𝔮₀ ≥ 2021/729 = 2.7723, and session 24's
j = 3 value 6115/2187 = 2.7961 — so "the true constant lies in [205/81, 11/3]" (l.172) is true but its lower end can be
raised to 6115/2187 (≥ 2021/729 from NQ_DEF's own computation). "𝔮₀ = 1 is FALSE for Setting SC's Q" — CONFIRMED.

### r55n-F3 "NORMS's '𝔮₀ = 1 if Q is the straight average' is a conditional with a false antecedent" — CONFIRMED
NORMS l.403 ("immediate with 𝔮_0 = 1 for the straight average") and tally item 15 (l.809-810) are true statements about
Q_str — both Q_str's have ‖Q_str^{(j)}‖ = L^j (non-negative, row sum L; q1-H/q1-E) — inside a conditional whose antecedent
(Setting SC's Q = Q_str) is false (F1). TUNIF l.678 repeats the conditional (batch C8's file; noted, not reviewed).

### r55n-F4 "Q_str is two different operators (NORMS §N1 vs LINEAR_PACKAGE l.71)" — CONFIRMED (exactly reproduced)
NORMS l.103-104: "Q_str B(c) := L^{−(d−1)}Σ_{paths}Σ_{b∈path}σ_bB_b over the L^{d−1} straight paths of L links" — support
**81**, uniform weight 1/27. LINEAR_PACKAGE l.71: "(Q_strA)(X, μ) := L^{-4}Σ_{y∈B(X)}Σ_{j<L}A_μ(y + je_μ)" — support **135**,
longitudinal multiplicities 1, 2, 3, 2, 1 over 5 positions (/81). Both have row sum L = 3 and transpose norm L^{1−d}, so every
*use* NORMS makes of Q_str survives; but the slice identity Q_root = Q_str − d∘h holds for the LINEAR_PACKAGE operator only
and fails for NORMS's by **108** entries — I reproduce 108 for both placements of NORMS's paths (from c_X + t, and from the
block's low face + t) in all four directions. NORMS's internal inconsistency (its own (I8), l.130-133, is the full block
average) is real, as RN1-22 says. Benign numerically; the definition must be corrected because Lemma N1-4's proof uses (I8).

### r55n-F5 "𝔮₀ enters only prefactors; A_soft is 𝔮₀-free; j-uniformity is what is load-bearing" — CONFIRMED
NQ_DEF §D5.1-D5.3. 𝔮₀ appears only inside 𝔠_P (NORMS l.387) — j-independent — and enters 𝔚, 𝔖 as 𝔠_P²: a factor ≤ (11/3)² =
121/9 = 13.44 (1.13 decades) relative to 𝔮₀ = 1. The exponents of r55n-A3 contain no 𝔮₀. Counterfactual re-derived: if only
‖Q^{(m)}‖ ≤ (𝔮₀L)^m held, the level-j potential sup would carry 𝔮₀^j = 𝔮₀^{k−n}, the two legs 𝔮₀^{2(k−n)}, and the soft sum
≍ 𝔖𝔮₀^{2k} = 𝔖(121/9)^k — NORMS [N1-corr 1] case 3's "13.4 per level"; 1266.87/(121/9) = 94.2 (NORMS's "≈ 95" is a round-up).

### r55n-F6 "Theorem N1-15 is therefore UNCONDITIONAL at d = 4, trivial background, abelian/linearised, uniformly in k and T" — NOT-VERIFIED
NQ_DEF §D6.1 (l.474-478): "With (N-Q) PROVEN (§D3) and (N-loc) discharged by T55-F's Corollary TU-5 / Theorem TU-6, Theorem
N1-15 has no remaining named conditional input". The (N-Q) half is CONFIRMED (E1). The rest does not follow on the record:
1. **The T-uniform (N-loc) discharge is TUNIF's TU-5/TU-6**, which CODEX_REVIEW_TUNIF F6 rates NOT-VERIFIED with a GAP ("the
   passage from the analytic fine curvature primitive to a single root-fixed chain representative with simultaneous row and
   column bounds"), plus F4's missing 𝔠₀ factor in the mean budget. **I agree with Codex F6 as it bears here:** Theorem N1-15's
   steps (1)-(4) need, for ONE admissible representative, both a whole-torus sup bound on the potentials and an ℓ¹-mass bound
   (NORMS l.422-423's two clauses); TUNIF §U2.3 states that only the ℓ¹ half is T-dependent, which presupposes a T-free
   whole-torus sup bound for the same representative — that is NLOC's Theorem NL-3′, not anything in NQ_DEF's input list.
   NQ_DEF itself flags TUNIF as unreviewed (l.499-502); the headline nevertheless says "unconditional". TUNIF/NLOC are batch
   C8 (REVIEW55_TUNIF), so I do not adjudicate them beyond this.
2. **Silent hypotheses that "unconditional" still rests on** (beyond the named (N-loc)):
   (a) NLOC Theorem NL-3/NL-3′ — the torus version of Lemma N1-11 with the admissibility correction at level k; NQ_DEF's list
       (l.497-499: "inside NORMS, Lemmas N1-1, N1-3, N1-4, N1-5, N1-11 … All are PROVEN or PROVEN-HERE") counts NORMS's
       Lemma N1-11, which as written is a box statement with an unfixed R_eff and an unjustified constant (r55n-A4);
   (b) LINEAR_PACKAGE v1.1's d = 4 theorems N2-lin 3.8 (C_f, C_R uncomputed), J-str 3.1, N2-exp′ 4.2′ (proven rate
       m_*′ = 0.0384) — frozen and imported;
   (c) TOWER-VAR (a)-(c): E_k^br as a C³ functional at a C² composite critical family through the trivial chain (CODEX_REVIEW_NBG2
       F1: CONDITIONAL on the lattice identification), and its quadratic part being Setting SC's chain energy;
   (d) Lemma N1-1's soft normalisation φ̂ = ½|ρ|² + O(ρ⁴) and M_S < ∞ (asserted, not evaluated);
   (e) T ≥ T₀ (a lower bound only) and L ≥ 3 odd;
   (f) the object: N3 in its absolute-row-sum form (r55n-A6), at V_k = 1 — not (H-C)'s C_♭ (Lipschitz on the class; (N-bg)
       OPEN), which NQ_DEF correctly says (§D6.4);
   (g) the regime label: "abelian/linearised" must read "SU(N) vertex, linear componentwise chain response" (r55n-A7).
3. **What IS supported:** k-uniformity **at fixed coarse side T** via NLOC Corollary NL-4 (+ [NL-corr 1], + NQ-1), which is
   what HANDOFF critical-path item 1 already records — NQ_DEF does not cite it. Correct statement: *"(N-Q) is PROVEN (NQ-1,
   𝔮₀ = 11/3); Theorem N1-15 is PROVEN uniformly in k at fixed T given NLOC NL-3′/NL-4 (batch C8), and uniformly in k and T
   only given TUNIF TU-5/TU-6, which Codex rates NOT-VERIFIED."*

### r55n-F7 NQ_DEF §D2.3 control E′ ("fired only for μ = 0"; "a quadratic test function cannot distinguish Q_str from Q_root") — CONFIRMED
For λ quadratic, Mλ − evλ is a constant (block-mean minus centre value = ½Σ_ν∂²_νλ·Var_ν), so d(Mλ − evλ) = 0; for λ = x₀³ the
difference depends on the coarse x₀ only, so it can fire only in direction 0. My q1-D′ used a λ cubic in every coordinate
and fired in 4/4 directions, which closes the gap NQ_DEF closed post hoc.

### r55n-F8 NQ_DEF §D5.4 (no factor from N1-15 reaches a smallness threshold today) — CONFIRMED (logic); margins spot-checked
Item 1 (the C_♭ N1-15 bounds is not the consumed C_♭; (N-bg) OPEN) is decisive and correct. Item 3's ratio
4.19·10⁻⁷/1.98·10⁻¹⁸ = 2.12·10¹¹ is correct arithmetic; the strings are at PROOF.md l.5900 ("ε_br = min{1.98·10⁻¹⁸/C_Δ,
4.19·10⁻⁷/C_♭"), l.5894 ("C_Δ ≤ C_♭"), l.5889 ("C_♭ := 4S_♭n_1/r_♭"), each +4 from NQ_DEF's citations.
*Erratum to F1:* NQ_DEF §D1.1 ("The defining sentence") begins at NQ_DEF **l.86** (its quotations run to l.108).

## G. NORMS Definition N^F-2's vertex norm 𝔑 (target T7)

### r55n-G1 "𝔑 is identically +∞ for every nonabelian consumer" (NBG_A §A1.3, l.180-200; SESSION25_RESULTS l.306) — CONFIRMED, and it holds already at the trivial background, for every k
Definition (NORMS l.156-171): ‖X‖^{(1)}_{l,m} depends on X only through d_lX and r_l(X); 𝔑_{l,m}(T) := sup{|T(X, Y, W)| :
‖X‖^{(1)} ≤ 1, ‖Y‖^{(∞)} ≤ 1, ‖W‖^{(∞)} ≤ 1}. NORMS's own Remark N^F-3 (i) (l.172-176) observes, for the ℓ^∞ legs, that by the
Ward identity "T does NOT vanish on a pure-gauge leg, so no norm that depends on Y only through d_lY can bound T" — and
does not notice that its ℓ¹ leg is exactly such a norm.
**Derivation (mine).** For U_b ↦ g_xU_bg_y^{−1}, g = e^{ελ}, the chart A ↦ e^A gives (BCH, first order in ε)
δ_λA_b = −(dλ)_b + ½[λ_x + λ_y, A_b] + O(A²). Gauge invariance S(A + εδ_λA) = S(A) with DS(0) = 0 and
DS(A)[v] = H(A, v) + ½T(A, A, v) + O(A³) gives, at order A: H(A, dλ) = 0; at order A²: T(A, A, dλ) = H(A, [λ̄, A]); polarised:
**T(dλ, Y, W) = ½[H(Y, [λ̄, W]) + H(W, [λ̄, Y])]**, λ̄_b := λ_x + λ_y. Checked exactly in r55n_w1 for the SU(2) Wilson vertex
(20/20 candidates; the BCH-coefficient-1 control fails 20/20), and **T(dλ, Y, W) ≠ 0 in 20/20** (abelian control 0/20).
With X = t·dλ: d_lX = 0, so ‖X‖^{(1)} = 0 for every t (at level l = k there is no level-(k+1) residual; at a composite level
r_l(d_lλ̂_l) = d_{l+1}(evλ̂_l − λ̂_{l+1}) = 0 for a nested family, by root covariance), while |T(tX, Y, W)| = |t|·|T(dλ, Y, W)|.
Hence **𝔑_{l,m}(T) = +∞ for every m ≥ 0** whenever the Ward term is nonzero.
- **k = 0** (T = D³S_W(1), the level-0 Wilson vertex T_0 of Theorem N1-12): exact witness above.
- **k ≥ 1** (T_k = D³E_k^br(1)): E_k^br is gauge invariant with DE_k^br(1) = 0 (the trivial chain is critical: S_W and
  φ̂ = ½|ρ|² + O(ρ⁴) have no linear term), so the same Ward identity holds with H_k = D²E_k^br(1). Take Y = d_kμ (so H_k(Y, ·) = 0)
  and W = Z := [λ̄, d_kμ]: T_k(dλ, dμ, Z) = ½H_k(Z, Z). H_k is (per colour) the minimised Setting SC energy, and
  H_k(Z, Z) = 0 would give a chain with d₀B₀ = 0 and all r_i = 0, hence d_kZ = d_k(Q^{(k)}B₀) = d_k(Q_str^{(k)}B₀) = (square
  identity) an average of fluxes of d₀B₀ = 0. So H_k(Z, Z) > 0 as soon as d_kZ ≠ 0, which r55n_w1 w1-3 exhibits
  (Σ|dZ|² = 48; at k = 0 the vertex value is exactly 24 = ½·48). **So 𝔑(D³E_k^br(1)) = +∞ for every k ≥ 0 and N ≥ 2** — on the very
  object Theorem N1-15 bounds. NBG_A's scope remark "𝔑 is finite exactly where NQ-1 lives and infinite exactly where (N-bg)
  lives" (l.195-196) is therefore **REFUTED**: NQ-1's regime (trivial background, linear transport) is where N1-15 lives, and 𝔑 is
  already infinite there; it is finite only where T vanishes on pure gauges (e.g. one real colour, where the cubic vertex is 0).
- NBG_A's proof writes r_l(dλ̂) = 0 "because Q_str d_iμ = d_{i+1}(μ|centres)" — the M/ev-conflated identity (r55n-E4); the
  conclusion holds via root covariance Q_root∘d = d∘ev. Citation-level defect only.
- **Consequences (all independent of N1-15, which is stated and proved in N3, l.510, l.531):** NORMS Remark N^F-3 (iii)'s
  "𝔑_{l,0}(T) = own-units N3(T)/(2(d−1))" and "N-F1 does not occur" are false (only N3 ≲ 2(d−1)·𝔑 holds — the norm is too
  strong, not too weak); Theorem N1-12's 𝔑 form and Theorem N1-13 (i)'s 𝔑-rescaling are ∞ ≤ ∞ (r55n-B1); REVIEW_NORMS_S1 RN1-7b's
  "verified … exactly" is wrong (r55n-B3); TUNIF §U2.2's identification of N3 with 𝔑_{k,0} is wrong in wording.

### r55n-G2 NBG_A's "one-line repair (X ∈ S_k)" — NOT-VERIFIED; insufficient in the level-k data reading on a torus
NBG_A l.197-200 / l.518: restrict the ℓ¹ leg to a composite slice S_k, which "excludes nested pure gauges". On a torus a slice
does not exclude **harmonic (constant) 1-forms** h: dh = 0, h is not a pure gauge, and in the level-k data reading ‖h‖^{(1)} = 0.
r55n_w1 w1-4 (informational): on a periodic 3×3 torus T(h, Y, W) ≠ 0 for 9 of 10 constant h. So for a vertex on level-k data,
𝔑 stays +∞ after the slice repair unless the harmonic sector is also excluded or separately normed. In the composite
fluctuation reading (data fixed, X = displacement of levels < k) a constant mode has r_{k−1}(X) = QX_{k−1} = L·X_{k−1} ≠ 0, so
the repair may work there — but S_k's definition (REVIEW_S22 l.389 "S_k a composite slice at the composite lift") does not say.
*Erratum to G1:* Theorem N1-15 is stated in N3 at NORMS **l.511** ("N3(D³E_k^br(1)) ≤ 𝔚·L^{(d−4)k} + …") and evaluated in N3 at
l.522 ("Evaluate N3 by putting X = δ_x"); the "l.510, l.531" I copied from NBG_A are one line off / not N3-specific.

## H. Remaining items of the batch (target T8)

### r55n-H1 NORMS lemmas not covered above
- **Lemma N1-4 (θ_w^c = 2 on the torus): CONFIRMED.** Arithmetic re-derived: the i-th term exponent (j−1−i) − 3(k−1−i) =
  j + 2 − 3k + 2i, geometric in i with ratio L², sum ≤ 4L²/(L²−1)·L^{−3(k−j)}. The step "B_j = Q_str^jB_0 − Σ… modulo a level-j
  pure gauge" (l.275) is in fact exact for the curvature: d∘Q_root^{(m)} = d∘Q_str^{(m)} because the difference is the single
  coarse exact form of E1's telescoping identity. Inputs (I3), (I4), (I8) imported (I8 needs the LINEAR_PACKAGE Q_str, F4).
- **Lemma N1-5 (axial gauge, |B − dλ|_∞ ≤ (d−1)R|dB|_∞): CONFIRMED** (standard induction over directions; abelian/linearised).
- **Lemma N1-6: CONFIRMED with RN1-11's fix** — its parenthesis "(so the family is an admissible reparametrisation …)" is
  false as written (λ̂_k = λ ≠ 0 at the level-k roots), but the use is right: the nested pure-gauge chain is a zero-energy
  minimiser for data d_kλ (r_j = d_{j+1}(evλ̂_j − λ̂_{j+1}) = 0 by root covariance), and the *difference* of two minimiser chains
  for the same data is a fluctuation gauge. CODEX_REVIEW_TUNIF F6's interpolation estimate ‖H_jh‖_∞ ≤ s^{−1}‖h‖_∞ is the same
  bound; I agree with it.
- **Lemma N1-7: CONFIRMED** (two lines). **Lemma N1-2: CONFIRMED** (F_AA annihilates fluctuation-gauge directions at a
  critical point; A1's derivation uses only criticality). **Lemma N1-3: CONFIRMED** as algebra given Lemma U0's QJ = 1,
  dJ = ιd₁ (imported; not used by N1-15).
- **Lemma N1-11: NOT-VERIFIED as written** (its (N-Q) condition is now discharged): a box statement with R_eff never fixed,
  "|d_kλ|_∞ ≤ 2|Y|_∞" unjustified (RN1-19 CONFIRMED: the bound carries c_AX R_eff), and the level-0 axial gauge changes the
  level-k data, which step (5) does not track (repaired in NLOC Theorem NL-3 step (3), batch C8).
- **Proposition N1-10, Theorem N1-12, Remark N8-2: NOT-VERIFIED** (ARGUED in the file; per-level route only; spot-read).
- **Remark N6-4 (COMP-F1 / Π_ex does not occur in §N6): CONFIRMED** — every response used is to level-k data, i.e. to an
  exact 2-form d_kX.
- **§N9 ("does not improve ε₁ or g_K²"; C_♭'s term "≈ 10³² below the binding one"): conclusion CONFIRMED, margin NOT-VERIFIED.**
  The conclusion follows already from NQ_DEF §D5.4 item 1 (no N1-15 factor reaches a threshold while (N-bg) is open). The
  "10³²" was evaluated at an implicit C_♭ = O(1) — a stale quantity: N1-15's actual constant is unevaluated (≳ 10⁷ at the
  proven locality rate, RN1-9; c_m ↦ T^d or 𝒮_T on NLOC's fixed-T route). The same "some 10³² above the C_♭ term" is in
  PROOF.md l.6903.
- **Checks n1-A, n1-B non-falsifiable, n1-C contentful, n1-C ratio label L^{d−5} wrong off d = 4 (RN1-4, RN1-14): CONFIRMED**
  by reading the script (the script runs d = 4 only; the correct ratio is L^{−1} in every d, r55n-A3).

### r55n-H2 REVIEW_NORMS_S1 items not covered above
RN1-1, RN1-2, RN1-3, RN1-5 (B1-B2), RN1-7 (B3), RN1-10 (A1), RN1-11 (H1), RN1-12 (A4), RN1-13 (A3), RN1-16 (H-C)'s C_♭ clause
is a class statement not discharged — CONFIRMED, also by CODEX_REVIEW_NBG2 F4's norm distinction), RN1-17, RN1-18, RN1-19,
RN1-22, RN1-23, RN1-24: **CONFIRMED**. RN1-6, RN1-7b, RN1-8 (partly), RN1-21: **REFUTED** (B3, E4). RN1-20 ((N-loc) unnecessary at
bounded T_k): the substitution c_m ↦ T_k^d is valid once a whole-torus sup bound holds — structure CONFIRMED; the sup bound
itself was supplied later by NLOC NL-3/NL-3′ (batch C8) — **NOT-VERIFIED by me**. RN1-9 (constant ≳ 10⁷): spot-checked, consistent.
RN1-A1-A4 (provenance timestamps): not re-checked. RN1-15 (anti-circularity satisfied): spot-CONFIRMED (N1-15 inverts no
per-level covariance; its linear inputs are composite).

### r55n-H3 REVIEW_NQ_S1 items not covered above
NQ-1, NQ-2 (provenance), NQ-4 (resources), NQ-5 (line-number convention) — not re-checked except NQ-5's resolution of the
h^{(m)} citation, which is right (E4). NQ-6-NQ-9 (identification of Q; SQ §0.4 is a gauge shift, correct and unavailable to a
potential bound) — CONFIRMED (E3, F1). NQ-22 (G2 cannot see a far-end offset: on a constant 1-form the two funnels of one
(σ, y) contour have the same offset y − c_X = (y + Le_μ) − c_Y and cancel contour by contour; G4/G5 cannot fail) — CONFIRMED.
NQ-23 (§Q6's post-hoc check imports the author's machinery) — CONFIRMED by NQ_CHECK l.355-366's own description.
NQ-26 (N1-15 conditional on (N-loc) alone) — CONFIRMED. NQ-28/NQ-29 (𝔠_P still carries C_f, C_R, R_eff; NQ-1 does nothing for
(N-bg)) — CONFIRMED.

---

# SUMMARY TABLE (every claim reviewed in batch C4)

| # | Claim (file, locating string) | Verdict | Finding |
|---|---|---|---|
| 1 | Single pullback D³E_k^br(1) = D³𝔉_k(1)[ζ^c·,ζ^c·,ζ^c·] (NORMS (I2); RN1-10) | CONFIRMED | A1 |
| 2 | Lemma N1-1: one coboundary / one residual per cubic term, M_W ≤ 6 (NORMS l.197) | CONFIRMED | A2 |
| 3 | N1-15 exponent counts; Σ_{n≥1}3^{3−n} = 27/2; level ratio exactly L^{−1} for every d, L | CONFIRMED | A3 |
| 4 | N1-15 step (3) count "n_link(j) = dL^{dn}" / residual ℓ¹ exponent n+(d−1) (l.542, l.563) | CONFIRMED as an upper bound (loose by L^d; sharp exponent n−1; no effect) | A3 |
| 5 | Theorem N1-15, PROVEN given (N-Q), (N-loc); uniform in k; d = 4 | CONFIRMED (conditional; Lemma N1-11 repairs travel with it) | A4 |
| 6 | "The result is true for every d ≥ 2" (NORMS l.575, l.517) | NOT-VERIFIED (exponent bookkeeping only; inputs are d = 4) | A4 |
| 7 | NBG_B §7.1: A_soft is a per-level ratio of an absolute row-sum bound on a trilinear form; 𝔐 never appears; not one contraction for 𝔉_k in 𝔐 | CONFIRMED | A5 |
| 8 | THETAW §T4.2/F-item 2: A_soft = 1/3 is the data-only rate, an unattained infimum; honest composite rate L^{−θ} — as a statement about N1-15 | REFUTED (N1-15 has no θ; 1/L is attained exactly) | A5 |
| 9 | THETAW: L^{−θ} as the rate of a nonlinear-source contraction | NOT-VERIFIED (formal count; Codex THETAW F5, F10) | A5 |
| 10 | NORMS l.106: N3 := max_xΣ|T| **=** sup|T(δ_x,Y,W)| | REFUTED (4 ≠ 2; Codex NBG2 F4); harmless to N1-15 | A6 |
| 11 | Regime "abelian/linearised: one real colour component" (NQ_DEF l.489 and lane-wide) | REFUTED as worded (vertex is nonabelian; label fits ζ^c only) | A7 |
| 12 | Thm N1-13 (i) as the no-go's PROVEN half, with check n1-D PASS (NORMS l.462-471, tally 8) | REFUTED as evidence (true but vacuous; n1-D cannot fail; 𝔑-form is ∞ ≤ ∞) | B1 |
| 13 | Thm N1-13 (ii): A ≥ 1 in every scale-covariant norm family (l.458) | NOT-VERIFIED (upper bound only; class undefined; conclusion plausible, (O3) untested) | B2 |
| 14 | REVIEW_NORMS_S1's withdrawal of the no-go; [S24-fix 1a]; HANDOFF "WITHDRAWN" 2 | CONFIRMED | B2 |
| 15 | RN1-6: A_per ≤ 1.38 contradicts R_3(ℤ⁴) ≥ 1.40 | REFUTED (different objects; soft drive B_per) | B3 |
| 16 | RN1-7: 𝔠_ax ≥ 5.46 from Prop N1-10's own bracket | CONFIRMED | B3 |
| 17 | RN1-8: 𝔠_vol = c_m = coth(m′/2)^d; "no gain" at 𝒦's near-field rate | REFUTED in part (pigeonhole: 𝔠_vol ≤ d(d−1)/2 = 6) | B3 |
| 18 | NORMS Remark N^F-3 (iii) "𝔑 = N3/(2(d−1))", "N-F1 does not occur"; RN1-7b "verified exactly" | REFUTED (𝔑 = +∞) | B3, G1 |
| 19 | NORMS "≈10³ gain per level", 920-1171 (l.84, l.456, n1-E) | NOT-VERIFIED (arithmetic exact at 𝔠 = 1; the file's estimates do not deliver 𝔠 = 1) | B4 |
| 20 | Prop N1-8 mass balance; 9.74 + 1.48 = 11.2 average column mass; Cor N1-9 | CONFIRMED (max ≤ 6× avg by pigeonhole; Cor N1-9 unnecessary) | C1 |
| 21 | PROOF.md [S24-fix 1]: "Z_col is the column mass of the curvature kernel ≈ 9.7 + 1.5"; "PROOF.md's Z_col diagnosis is WRONG"; "N1-8's correction stands" (also NORMS §N4(a) l.361-365, FOR-OTHER-FILES 2) | REFUTED (Z_col = 156.08 is a′'s column mass; 11.2 is 𝒦's) | C2 |
| 22 | RN1-7c: PROOF's diagnosis is not wrong; reword as an addition | CONFIRMED ("Z_col ≥ 27" is heuristic, not proved) | C2 |
| 23 | Weight pair: A = L^{d−θ_w^r−2θ_A}; no single θ_w ∈ (0,2] works ([S24-fix 3]; NORMS §N7) | CONFIRMED (needs only the cap θ_A ≤ 1, which I re-derived) | D1 |
| 24 | "The composite contraction requires θ_w^r = 3" ([S25-fix 3]; NBG_B §8 table) | REFUTED as stated (requires θ_w^r > 2; 3 is delivered) | D1 |
| 25 | Theorem NQ-1, 𝔮₀ = 1 + d(L+1)/(2L) = 11/3, uniformly in j | CONFIRMED (re-derived) | E1 |
| 26 | REVIEW_NQ_S1 "PROVEN … confirmed and strengthened" (NQ-10…NQ-18, NQ-20, NQ-21, NQ-24, NQ-25, NQ-27) | CONFIRMED | E2 |
| 27 | REVIEW_NQ_S1 NQ-19 measured ‖hQ_str^{(i)}‖ = 8/3, 56/9, 488/27 | NOT-VERIFIED (not recomputed) | E2 |
| 28 | NQ_CHECK §Q1: Q = Q_root; J-str/SHIFT is not a conflict | CONFIRMED | E3 |
| 29 | NQ_CHECK l.348: G1 "strengthens check c8(f)'s 2e-16 to an identity" | REFUTED (agree NQ-21) | E3 |
| 30 | RN1-21: "h^{(m)} occurs nowhere in PROOF.md" (REVIEW_NORMS_S1 l.527) | REFUTED (PROOF.md l.1324, 2956, 3149, 3160) | E4 |
| 31 | NQ_DEF: Setting SC's Q is Q_root | CONFIRMED | F1 |
| 32 | NQ_DEF: ‖Q‖ = 205/27 > 3 (support 459); ‖Q^{(2)}‖ = 2021/81; any 𝔮₀ ≥ 205/81 | CONFIRMED (independent enumeration; bound can be raised to 6115/2187) | F2 |
| 33 | NQ_DEF: "𝔮₀ = 1 if Q is the straight average" is a conditional with a false antecedent | CONFIRMED | F3 |
| 34 | NQ_DEF: Q_str is two operators (81 vs 135 entries; slice identity off by 108) | CONFIRMED (108 reproduced, both path placements) | F4 |
| 35 | NQ_DEF: 𝔮₀ only in prefactors; A_soft 𝔮₀-free; j-uniformity load-bearing (13.44^k counterfactual) | CONFIRMED | F5 |
| 36 | NQ_DEF: N1-15 UNCONDITIONAL at d = 4, trivial background, abelian/linearised, uniformly in k and T | NOT-VERIFIED (T-uniformity rests on TUNIF TU-5/6, Codex GAP; silent hypotheses listed) | F6 |
| 37 | NQ_DEF: control E′ fires only for μ = 0 because a quadratic test 0-form cannot separate M from ev | CONFIRMED | F7 |
| 38 | NQ_DEF §D5.4: no N1-15 factor reaches a smallness threshold today | CONFIRMED (logic; ratio 2.12·10¹¹ arithmetic) | F8 |
| 39 | NBG_A §A1.3: 𝔑 = +∞ for every nonabelian consumer | CONFIRMED (already at the trivial background, every k ≥ 0) | G1 |
| 40 | NBG_A: "𝔑 is finite exactly where NQ-1 lives" (l.195) | REFUTED | G1 |
| 41 | NBG_A: one-line repair "X ∈ S_k" | NOT-VERIFIED (fails on harmonic modes in the level-k data reading) | G2 |
| 42 | Lemma N1-4 (θ_w^c = 2) | CONFIRMED | H1 |
| 43 | Lemmas N1-2, N1-3, N1-5, N1-7; Remark N6-4 | CONFIRMED (N1-3 and N6-4 spot-level) | H1 |
| 44 | Lemma N1-6 (with its admissibility parenthesis) | CONFIRMED with RN1-11's fix (parenthesis false as written) | H1 |
| 45 | Lemma N1-11 as written (box, constant, data change) | NOT-VERIFIED (its (N-Q) condition is discharged) | H1 |
| 46 | Prop N1-10 value, Thm N1-12, Remark N8-2 | NOT-VERIFIED (ARGUED in file; spot-read) | H1 |
| 47 | §N9 / PROOF.md l.6903 "C_♭ term ≈ 10³² below the binding one" | NOT-VERIFIED (evaluated at implicit C_♭ = O(1); conclusion holds for another reason) | H1 |
| 48 | n1-A, n1-B non-falsifiable; n1-C contentful; n1-C ratio label wrong off d = 4 (RN1-4, RN1-14) | CONFIRMED | H1 |
| 49 | RN1-11, RN1-12, RN1-16, RN1-17, RN1-18, RN1-19, RN1-22, RN1-23, RN1-24 | CONFIRMED | H2 |
| 50 | RN1-20: (N-loc) unnecessary at bounded T_k | NOT-VERIFIED (structure confirmed; the torus sup bound is NLOC's, batch C8) | H2 |
| 51 | REVIEW_NQ_S1 NQ-6…NQ-9, NQ-22, NQ-23, NQ-26, NQ-28, NQ-29 | CONFIRMED | H3 |

**Counts: CONFIRMED 29 · NOT-VERIFIED 12 · REFUTED 10** (rows: CONFIRMED 1-5, 7, 14, 16, 20, 22, 23, 25, 26, 28, 31-35, 37-39,
42-44, 48, 49, 51; NOT-VERIFIED 6, 9, 13, 19, 27, 36, 41, 45, 46, 47, 50 and — counting row 11's wording issue separately from
its substance — none further; REFUTED 8, 10, 11, 12, 15, 17, 18, 21, 24, 29, 30, 40).

**Correction to the counts line just above (append-only; the totals there were mis-added, the row lists are right):**
**CONFIRMED 28 · NOT-VERIFIED 11 · REFUTED 12 = 51 rows.** CONFIRMED = rows 1-5, 7, 14, 16, 20, 22, 23, 25, 26, 28, 31-35, 37-39,
42-44, 48, 49, 51. NOT-VERIFIED = rows 6, 9, 13, 19, 27, 36, 41, 45, 46, 47, 50. REFUTED = rows 8, 10, 11, 12, 15, 17, 18, 21, 24,
29, 30, 40. (Ignore the phrase about "row 11's wording issue" in the line above; row 11 is counted once, as REFUTED.)

---

# CLOSING — for the lead (written 2026-10-28T22:48:20Z UTC)

**What A_soft is.** The exact level ratio L^{−1} (= 1/3 at L = 3, for every d) of the geometric majorant
Σ_{n=1}^{k}𝔖L^{(d−1)−n} of the soft part of N3(D³E_k^br(1)), at the trivial background, for data-only (level-k) inputs. Not a
contraction of any map, not measured in 𝔐 (NBG_B right), not an unattained infimum (THETAW wrong for N1-15; its L^{−θ} is a
formal count for an undefined nonlinear analogue). Σ_{n≥1}3^{3−n} = 27/2 exactly; the theorem is CONFIRMED as a conditional
theorem (on (N-loc), or on NLOC's fixed-T bypass), d = 4, uniform in k.

**REFUTED (12), each with its correction:**
1. THETAW "A_soft = 1/3 is an unattained infimum; honest rate L^{−θ}" (about N1-15) → 1/L is attained exactly; L^{−θ} belongs to a
   nonlinear extension and is NOT-VERIFIED there.
2. NORMS l.106 "max_xΣ|T| = sup|T(δ_x,Y,W)|" → only "≥"; consumer's C_♭ is the bilinear (smaller) one; N1-15 bounds the larger.
3. "Abelian/linearised: one real colour component" as N1-15's regime → "SU(N) cubic vertex, linear componentwise chain
   response" (in one real colour the vertex is 0).
4. Theorem N1-13 (i) + n1-D as the no-go's proven half → true but vacuous (l = k anchoring); n1-D cannot fail; in 𝔑 it is ∞ ≤ ∞.
5. RN1-6 "A_per ≤ 1.38 contradicts R_3 ≥ 1.40" → no contradiction (different objects; soft drive B_per).
6. RN1-8 "𝔠_vol = c_m, no gain" → 𝔠_vol ≤ d(d−1)/2 = 6 by pigeonhole, no decay input needed; the ≈10³ gain is still unproven.
7. NORMS Remark N^F-3 (iii) "𝔑 = N3/(2(d−1))", "N-F1 does not occur"; RN1-7b "verified exactly" → 𝔑 = +∞; only N3 ≲ 2(d−1)𝔑.
8. PROOF.md [S24-fix 1] "Z_col is the column mass of the curvature kernel ≈ 9.7 + 1.5; PROOF's diagnosis is WRONG; N1-8's
   correction stands" → Z_col = 156.08 is a′'s column mass; 11.2 is 𝒦's average column mass, a different quantity that
   *replaces* Z_col in the field-strength estimate; PROOF's diagnosis stands as a heuristic. Use the wording in C2.
9. [S25-fix 3]/NBG_B "the composite contraction requires θ_w^r = 3" → requires θ_w^r > 2 (θ_w^c ≥ 2, θ_A = 1); 3 is delivered.
10. NQ_CHECK l.348 "G1 strengthens c8(f)" → G1 is a construction self-consistency check (agree REVIEW_NQ_S1 NQ-21).
11. RN1-21 "h^{(m)} occurs nowhere in PROOF.md" → it is at PROOF.md l.1324, 2956, 3149, 3160 (s23 snapshot l.2787, 2980 as cited).
12. NBG_A "𝔑 is finite exactly where NQ-1 lives" → 𝔑 = +∞ already at the trivial background for every k ≥ 0 (N ≥ 2).

**Findings that change what PROOF.md / HANDOFF should say:**
- **PROOF.md is internally inconsistent on the no-go.** Its header withdraws it ([S24-fix 1a]), but the [S24] consolidation at
  **PROOF.md l.6898-6899** still reads "D2 (the per-level route is closed). **Upgraded from a judgement to a theorem** by NORMS.md
  §N5. No future session should attempt to repair the per-level induction in any norm." That paragraph must be struck: the
  no-go is NOT established (B2) and the per-level route is OPEN.
- **[S24-fix 1] must be rewritten** (C2); as written it is a false erratum against a correct diagnosis.
- **No tally change is forced by this batch.** If anything is counted: Theorem NQ-1 qualifies (CONFIRMED, linear transport,
  trivial background); Theorem N1-15 only as "PROVEN uniformly in k at fixed T given NLOC NL-3′/NL-4 (batch C8)", not as
  unconditional in k **and** T (NQ_DEF §D6.1 / SESSION25_RESULTS l.507 rest on TUNIF TU-5/TU-6, NOT-VERIFIED per Codex F6); and
  nothing here discharges (H-C)'s C_♭ clause ((N-bg) OPEN; the consumed C_♭ is a different, bilinear, class-wide object).
- **SESSION25_RESULTS l.548-553** still calls (N-Q) "the smallest remaining missing input" and repeats "if Setting SC's Q is the
  straight average, 𝔮₀ = 1 and Theorem N1-15 is UNCONDITIONAL" — (N-Q) is PROVEN (NQ-1, 𝔮₀ = 11/3), and that antecedent is false.
- **HANDOFF critical-path item 1** is consistent with these findings (fixed-T bypass; T-uniformity the open half). Add: never
  state anything "in NORMS's norm 𝔑" (it is +∞ on the nonabelian vertex), and state N1-15's regime as "SU(N) vertex, linear
  chain response, trivial background, d = 4".
- **PROOF.md l.6903** "(magnitude problem) some 10³² above the C_♭ term" is evaluated at an implicit C_♭ = O(1); N1-15's
  actual constant is unevaluated (≳ 10⁷ at the proven locality rate). The conclusion survives (no N1-15 factor reaches a
  threshold while (N-bg) is open), the number does not stand as stated.

**Codex verdicts used, and my position on each:**
- CODEX_REVIEW_TUNIF F6 (TU-5/TU-6 chain transfer NOT-VERIFIED, GAP; one representative must carry row and column bounds):
  **AGREE** — it is why NQ_DEF's "uniformly in T" is NOT-VERIFIED (F6 here). F8 (13.5 only at L = 3; L³/(L−1) in general):
  **AGREE** (a1-1). F3 (m > 0 does not follow from a sup bound alone): **AGREE** (its counterexample is valid; not load-bearing
  here). F4 (missing 𝔠₀ in the mean budget): consistent with my reading; not re-derived (TUNIF is batch C8).
- CODEX_REVIEW_THETAW F5 (data-only exponent 3; residual-type sources cap at 2 + θ; an upper bound is not an optimality proof),
  F10 (endpoint loses a factor k under Σ-aggregation), F11 (exponent algebra; single θ_w infeasible; witness r = 5/2):
  **AGREE** with all three; F11's witness is why row 24 is REFUTED-as-stated.
- CODEX_REVIEW_NBG2 F1 (envelope identity needs only a C² family; lattice identification CONDITIONAL): **AGREE** (A1).
  F4 (coefficient-row N3 ≠ bilinear N3; 4 vs 2): **AGREE**, hand-checked (A6).
- No Codex verdict used here is one I disagree with. All three Codex files were complete on disk when read.

## Addendum — the brief's three systemic defects, as found in this batch
1. **Symbol collisions:** Z_col (a′'s column mass, 156.08) vs 𝔎_col (𝒦's column mass, ≈ 11.2) — C2; Q_str (NORMS: 81 entries)
   vs Q_str (LINEAR_PACKAGE: 135) — F4; bare Q = Q_root (PROOF/NORMS/NQ) vs Q = Q_str (SQ §11.0 convention) — E3; N3 (absolute
   coefficient row sum) vs the consumer's bilinear sup — A6; 𝔑 vs N3 — G1; "A" = per-level factor A_per vs A_soft (a level
   ratio, not a contraction) — A5; θ_w (one symbol, three jobs) — D1/NBG_B.
2. **Stale quantities:** §N9 / PROOF.md l.6903's "10³²" at an implicit C_♭ = O(1) — H1; "13.5" valid at L = 3 only — A3; NQ_DEF's
   lower end 205/81 superseded by its own j = 2 value — F2; NQ_DEF's PROOF.md line numbers drifted +4; REVIEW_NORMS_S1's PROOF
   line numbers drifted (e.g. l.6490 → l.6624).
3. **Checks that cannot decide:** n1-D (identity in eA), n1-A, n1-B (integer identities) — B1/H1; NQ_CHECK G1 (same primitives
   both sides), G2 (funnels cancel on constants), G4, G5 — E3/H3; NQ_DEF gate A and control E′ (self-disclosed) — F7; and my
   own q1-C, whose discriminating content is its control q1-C′ — stated in the Checks section.

Provenance of my files: criteria checks/r55n_{q1,w1,a1}_criteria.md mtime 22:27:47 UTC; scripts r55n_q1.py 22:28:41,
r55n_w1.py 22:29:31, r55n_a1.py 22:29:58 UTC; outputs written by the runs immediately after. No other repository file was
written; no git command was run.

## Errata to this file found on proof-reading (append-only)
- **Verdict consistency, r55n-A7 vs summary row 11:** the A7 heading says "CONFIRMED with a correction to its wording"; the
  summary table's row 11 records the **wording** ("one real colour component" as N1-15's regime) as **REFUTED**. The table is the
  binding verdict: the claim as worded is REFUTED; the intended content (the chain map ζ^c is componentwise/abelian) is
  right and is covered by row 25/E1. Counts stand as corrected (28 / 11 / 12).
- Line citations in Section A: NORMS "### Lemma N1-1 (field-strength representation …)" is at **l.191** (not l.197); "≤ 𝔚 +
  13.5·𝔖" is at **l.515** (not l.514); Remark N6-1's residual row "| ℓ¹ mass of the level-j residual response" is at **l.564**
  (not l.563); NORMS §N7 begins at **l.642** (its table at l.646). PROOF.md's "Proposition N1-8's correction of the Z_col
  diagnosis stands" runs over **l.25-26**.
- **Addendum to B3 (RN1-6) and B2, from PROOF.md's own c38 B record (l.6599):** the Wilson-pullback part of N3(T_E) is
  0.5152 (T = 4) and 0.7623 (T = 5) against N3(T_W) = 3.000 — i.e. 0.17 and 0.25 of the level-0 Wilson vertex; the soft part
  (3.14 / 3.90) carries R_3 > 1. So the measured ratio that RN1-6 set against A_per is dominated by the soft drive, which
  confirms that no contradiction with A_per arises. It is **not** evidence that A_per < 1 either: torus N3 values are lower
  bounds for ℤ⁴ and the outer shell grows with T ([R22-fix S22-1], c38 D). The measurement does not decide the per-level
  question, which is one more reason the withdrawal (B2) is right.
- **Addendum to E3 (G1 vs c8(f)):** I deliberately did not read nq1_qnorm.py; the verdict rests on NQ_CHECK's own description
  of G1 ("The one-level row built from the S4′ contours equals (Q_str row) − (d∘h row)", l.151): an identity between linear
  contour averages that holds by construction (each contour = near funnel + leg − far funnel, the funnels being h's paths).
  c8(f) additionally exercised the implemented S4′ map on small U(1) fields; G1 does not, so "strengthens c8(f)" overstates.
