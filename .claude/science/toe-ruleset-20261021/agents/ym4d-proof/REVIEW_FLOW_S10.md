# REVIEW_FLOW_S10: hostile review of lane C session 10 (FLOW.md §73-§83 and the [RFL9-fix] / [S10-corr] edits)

Reviewer: an independent agent. I wrote none of FLOW.md, FLOW_LOG.md or checks/f13*. This file is the only one I edited.
No commits, PRs or pushes.

Inputs (read-only, by offset):
- REVIEW_FLOW_S9.md (all).
- FLOW.md §64-§72 (l.3137-3473, every [RFL9-fix] site and the [S10-corr] at l.3319-3323), §73-§83 (l.3475-3870) in full.
- FLOW_LOG.md l.400-455 (session 10).
- checks: f13_criteria.md, f13_uir_vbord.py (Part C l.203-475 line by line; Parts A/B by function), f13_out.txt, f13_time.txt.
  - BSD stat (UTC; local EDT +4 h): f13_criteria.md born 08:53:32 (5025 B); f13_uir_vbord.py born 08:57:27, modified
    09:02:24 (19775 B, md5 bacb258e…, matches FLOW_LOG l.432); f13_out.txt born 09:08:34, modified 09:09:31
    (6810 B); f13_time.txt 09:09:56 (101 B). FLOW.md mtime 09:18:26, FLOW_LOG.md 09:19:32. All agree with FLOW_LOG l.421-455.
  - The §73 pre-statement stat (FLOW_LOG l.412: 08:44:49, 381424 B, md5 40853da…) cannot be re-verified, because FLOW.md
    has changed since (now 424517 B). The order criteria → script → smoke → official run → proofs is confirmed by the stats.

Numerics (scratchpad `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revflow10/`):
- ONE lock acquisition, 09:34:02-09:34:58 UTC, released once with `rmdir` (no trap). Load 6.15 (1-min) and memory free 43%
  were checked inside the lock before starting (< 8, >= 35%). Everything ran under nice 10 with all BLAS threads = 1,
  plain `python3` (no -I) and no `timeout`. No process is left running, the lock directory is empty, and nothing was
  written to checks/ (no `__pycache__`).
  - f13 re-run from byte-identical scratchpad copies (f13 md5 bacb258e…, f12 md5 fea3107e…): 54.5 s, peak RSS 660 MB,
    **23/23 PASS, output identical to checks/f13_out.txt apart from the start-time and timing lines.**
  - `echeck.py` (reviewer): the ε-order of the defect E_U, using f13's own `E_formula` (validated against H·D_U to 3e-15) at
    ε = 1e-3, 2e-3, 4e-3. 1.2 s, 127 MB.

Line numbers are FLOW.md lines as of this review.

---

## Bottom line

- **Provenance: CLEAN.** Pre-statement (08:44:49) → [RFL9-fix] (08:45-08:52) → criteria (08:53:32) → script (08:57:27-09:02:24)
  → smoke (09:02:35) → official run (09:08:34-09:09:31) → proofs §74-§83 (09:10-09:18). Two statement changes after §73,
  both logged and both honest ((T4) strengthened; (T7) (b) corrected). Nine lock acquisitions as logged (not
  independently verifiable). As in session 9, the proofs were written after the numerics and quote them; the
  statements were not.
- **[RFL9-fix] S9-1..S9-7 + scope annotations: all APPLIED, correct; 16 tag occurrences at fix sites (l.3186-3463),
  as claimed (l.3842; FLOW_LOG's 18→16 correction is right).**
- **[S10-corr] (l.3319-3323): CORRECT, and S-fix STILL PROVEN.** The false sentence served only a C² claim AT K = 0,
  which (S3) never makes ("away from K = 0"). The C⁰ statement is even stronger than stated: |γ_k − γ_*| ≤ CL^{-2k}
  uniformly, without the |K̂|² weight. I checked the expansion 1 − (1 − ℓ^{-2})ΣK_μ⁴/(12|K|²) + O(K⁴).
- **Lemma FINE-IR: CONFIRMED** (every step re-derived: vertices, Ward rewrite, the k ↦ −k − pe_2 symmetrisation, the
  closed form x_0 = 16 sin²(p/2)J/p², the Bessel factorisation, the angular mean 1/24, 2c_g = 1/(48π²), the three error
  regions). One import-free standard input of S9-1 is discharged.
- **Proposition IR-id: CONFIRMED.** The level-unit scaling (ℓ^{-4}·ℓ²·ℓ² = 1), the identity h_n = (p²/2)[x_0(p) − x_n(ℓp)],
  and a_n = a_0 − ρ_n are correct; the second-order recombination YΛ^{-1}Y^† (Y = M_1 − MΛ^{-1}Δ_1) is exact algebra.
  Scope: the §75 fibre formulas for b_n, w_n are used structurally only and are **not numerically tested** by f13
  (Part B computes Y_n through the identity from f12's h_n, not from F_n) (S10-4).
- **Theorem UIR-S: CONFIRMED. The scalar (UIR), (V-IR-S) and (S4) with θ = L^{-2} are PROVEN** for the scalar proxy,
  at the rigour level of the document (Lemma A and Lemma VC (iii) are dominated-convergence sketches with explicit
  dominators; I checked the dominators and found them summable, with |x|²-weighted summability where the
  ℓ^{-2} rate needs it). The decisive step is right: the degree ≤ 5 Taylor polynomial of N_n is n-independent
  (I re-derived N_n = −2|K+P|²|K−P|² + 4K_1²|K+P|² + O(r⁶) and checked that every n-dependent piece — the K⁴
  terms of λ̃_n, the K² terms of d_0, h_n, the n-dependent linear coefficient of ũ, c_n, m̃, c_2 and the m ≠ 0
  aliases — enters at degree ≥ 6), and with the Ward identity at P = 0 and joint parity the P² extraction costs no IR
  power. Two harmless overstatements (S10-3). f13 B and my re-run agree with the asserted uniform L^{-2} rate.
- **Lemma V-bord, Lemma V-Jac, Proposition V-tel: CONFIRMED** (all three re-derived; the Woodbury/Schur signs, the
  K_F D = DΔ + E identity, the covariance M_U D_U = D_ℓ^{𝔪(U)}ι^*, the Jacobi telescoping, the X-recursion and
  Sylvester). V-bord holds for every U, as claimed. A k-uniform vector step gap is correctly NOT claimed.
- **§79 (a): the exact formula E_U = ½[Ad(U_b^{-1})λ(x) + λ(x+μ), J_b] is CORRECT** (re-derived; f13 matches to 3e-15).
  **The expansion "E_U = εp̂²Ê + O(ε³)" (l.3772; also §73 (T7) (a), l.3517) is FALSE**: Ad(U_b^{-1}) = 1 − εa_b ad H_1 + …
  gives a nonzero ε²p̂² term (S10-1). Reviewer check: (E/ε)(2ε) − (E/ε)(ε) scales with ratio 2.000
  (an O(ε²) term), not 4, and ||E_2||/||E_1|| = 1.2247 at both p and both backgrounds.
- **§79 (b), corrected in session 10, is still INCOMPLETE**: the ε² term of E (once, against U = 1 objects) is missing
  (S10-1). Its normalisation 4𝔮_1 + 16 sin²(p/2)𝔮_2 is right.
- **(DEF) verdict: the wall is real as stated, but it is NOT the right wall.** The defect is an artifact of reading c from
  U = 1 plane waves. E_U ≡ 0 on the whole critical family U_f that DEFINES c (MS (iv), F-id-exp), so in the constant-field
  reading the defect is identically absent. (DEF) can be replaced by a defect-free constant-field "ghost-pair"
  statement (GP) (§5 below). No Ward/Nielsen identity makes the plane-wave defect vanish by itself: gauge invariance
  leaves the zero-momentum coefficient of the defect kernel unconstrained (§5.2).
- **Corrected tally: 59 PROVEN-HERE (claimed 59)**, with scope annotations; under a stricter convention that folds the
  non-pre-stated Lemma A and Lemma VC into UIR-S, 57. §79 (a) is counted for the exact formula only.

---

## 1. Priority 1: provenance, the [RFL9-fix] edits, and the [S10-corr]

### 1.1 Provenance

| Event | Time (UTC) | Evidence | Verdict |
|---|---|---|---|
| §73 pre-statement (first edit) | 08:44:49, 381424 B | FLOW_LOG l.406-412 | not re-verifiable (file changed); consistent |
| [RFL9-fix] | 08:45-08:52 | FLOW_LOG l.413-420 | consistent with the tags |
| f13_criteria.md | 08:53:32 | BSD stat (birth = mtime) | ✓ before the script |
| f13_uir_vbord.py | 08:57:27 / 09:02:24 | BSD stat, md5 bacb258e… | ✓ |
| smoke | 09:02:35-09:03:11 | FLOW_LOG l.434 | after the last script edit ✓ |
| official run | 09:08:34-09:09:31 | f13_out.txt birth/mtime; load 4.57, mem 49% | ✓ |
| §74-§83 | 09:10-09:18 | FLOW.md mtime 09:18:26 | after the run |

- The five pre-smoke development fixes (FLOW_LOG l.427-431) are bug fixes to the implementation, including a factor-2 bug
  in Y_n that was fixed toward the criteria formula. No threshold changed. Disclosed. ✓
- The proofs postdate the numerics (as in session 9). The pre-stated statements (T1)-(T3) were not changed; the proofs
  quote f13 numbers only in their *Readings*. ✓
- Statement changes after §73: (T4) proved for every U (strengthening, honest); (T7) (b) corrected (quadratic defect
  terms added, honest — but still incomplete, S10-1).

### 1.2 [RFL9-fix]

| Fix | Where | Verdict |
|---|---|---|
| S9-1 ((IRR*) retired; ρ_n = a_0 − a_n; (UIR)) | l.3347-3353, 3436, 3446 | APPLIED, correct |
| S9-2 ("RG contraction" struck; three tasks) | l.3354-3360, 3445 | APPLIED |
| S9-3 (n = 6 unconverged; 4→5 = 0.1111; I1 ε-fit) | l.3421-3424, 3434 | APPLIED, numbers match REVIEW_FLOW_S9 §4 |
| S9-4 (mass remark withdrawn; (S6) narrowed) | l.3383-3385, 3391-3394, 3450, 3453 | APPLIED |
| S9-5 ("explicit" → "defined"; Δ'(1) gap ≍ ℓ^{-4}) | l.3186-3188, 3376-3378 | APPLIED |
| S9-6 ("summable" → bounded partial sums) | l.3303 | APPLIED |
| S9-7 (provenance disclosures) | l.3425-3432 | APPLIED, complete |
| §72 scope annotations | l.3463-3466 | APPLIED |

16 tags at fix sites (l.3186-3463), 4 further mentions (l.3475, 3478, 3543, 3841): matches l.3842. One wording slip:
l.3360 says all three S9-2 tasks "are done in §76" — true after this session, but it is a forward reference written into
a [RFL9-fix] tag; acceptable.

### 1.3 [S10-corr] in S-fix (l.3319-3323): is S-fix still proven? YES.

- The claim "|K̂|²t_0^{(ℓ)} is analytic there" is indeed false: |K̂|²t_0^{(ℓ)} = Π_μ[sin(K_μ/2)/s_ℓ(K_μ)]²·|K̂|²/λ̃_ℓ(K), and
  |K̂|²/λ̃_ℓ = [|K|² − ΣK_μ⁴/12 + …]/[|K|² − ΣK_μ⁴/(12ℓ²) + …] = 1 − (1 − ℓ^{-2})ΣK_μ⁴/(12|K|²) + O(K⁴): C^{1,1}, not C² (the ratio
  ΣK⁴/|K|² is homogeneous of degree 2 and not a polynomial). ✓
- (S3) claims (i) uniform C⁰ convergence of |K̂|²γ_k, (ii) derivatives of order ≤ 2 only AWAY from K = 0, (iii) bounds on
  L^{-2k}H_k(1). The false sentence was used for none of these:
  - (i) The m = 0 term has relative error O(|K|²ℓ^{-2}) and absolute error O(ℓ^{-2}) (l.3317-3318), so in fact |γ_k − γ_*| ≤ CL^{-2k}
    uniformly, without the weight.
  - (ii) Away from K = 0 every term is analytic.
  - (iii) Uses only γ_k ≥ s^{-1} and (i).
- **S-fix: PROVEN, unchanged in substance.** UIR-S uses λ̃_n, not |K̂|², as the IR normaliser (l.3704-3705), so the
  correction is consistent with its use.

## 2. Priority 2: FINE-IR, IR-id, UIR-S

### 2.1 Lemma FINE-IR (§74): CONFIRMED

- (1) Vertices: the 1-links carry a(x_2) at fixed x_2, so the first-order vertex between k and k ± pe_2 is exactly 2 sin k_1
  (no midpoint shift), and the ϑ-free second-order vertex is ¼ε²·2cos k_1. With −½tr(Δ^{-1}𝔐_1)², the ε² density is
  ¼∫[W/λ − Σ²/(λλ_p)]. ✓ L¹ at both singular points. ✓
- (2) ∂_1(Σ/λ) = W/λ − Σ²/λ² (∂_1Σ = W, ∂_1λ = Σ). ✓ Boundary term O(r²) → 0. ✓ The involution k ↦ −k − pe_2 swaps λ, λ_p and fixes
  Σ². ✓ λ_p − λ = 4 sin(k_2 + p/2)sin(p/2). ✓ Hence the ε² density is 8 sin²(p/2)J(p) and x_0 = 16 sin²(p/2)J/p². ✓
  Bessel form: direction 1 gives e^{-2τ}½(I_0 − I_2)(2τ) = e^{-2τ}I_1(2τ)/(2τ); directions 3, 4 give e^{-2τ}I_0(2τ); direction 2
  gives e^{-2τ}½[I_0(2R) − cos 2ψ I_2(2R)], with R² = s² + t² + 2st cos p. ✓
- (3) (i) Smooth part, even in p (f(k, p) is even pointwise: λ_- ↔ λ_+). ✓ (ii) k_1² ≤ |k_-||k_+| (they differ only in component
  2), k_2² ≤ 4p², and the scaling count a − b − b' = −2 gives O(p²) on |k| ≤ 2|p|; |∂_p²(f − c)| ≤ C|k|^{-4} gives O(p² log(1/p)). ✓
  (iii) |q_-|²|q_+|² = (|q|² + ¼)² − q_2², even in 1/|q|; ⟨n_1²n_2²⟩_{S³} = 1/(d(d + 2)) = 1/24; (2π²/24)(2π)^{-4} = 1/(192π²);
  × 4 = 1/(48π²) = 2c_g. ✓
- Numerics: x_0(10^{-3}) − 2c_g log 10³ = 1.70943e-2 − 1.45813e-2 = 2.5130e-3 = a_0 to the fit's O(p²log p). ✓
- A2 is a genuine independent test: the unsymmetrised form evaluates the pre-Ward integrand by its own proper-time
  representation.

### 2.2 Proposition IR-id (§75): CONFIRMED (one scope note)

- (b) h_n = [ε²]τ log Δ + ℓ^{-4}[ε²]τ_n log Γ_n (S-red (ii)); Γ_n^{-1} = ℓ²Γ̃_n^{-1}, [ε²] = ℓ²[ε̃²], P² = ℓ²p², so ℓ^{-4}[ε²]τ_n log Γ_n^{-1}
  = (p²/2)x_n(ℓp). Hence h_n = (p²/2)[x_0(p) − x_n(ℓp)]. ✓ Torus → infinite volume, continuity, density of the momenta. ✓
- (c) x_n(P) − 2c_g log(1/P) = [x_0(P/ℓ) − 2c_g log(ℓ/P)] + 2c_g log ℓ − Π_n(P/ℓ) → a_0 − ρ_n. ✓
- (a) The second-order recombination: the four cross/intermediate terms of M_UΔ_U^{-1}M_U^† at ε² are exactly
  (M_1 − MΛ^{-1}Δ_1)Λ^{-1}(M_1 − MΛ^{-1}Δ_1)^†. ✓ The ¼ normalisations of the ϑ-free parts. ✓ The sign F_n = −¼[…] matches x_n
  using log Γ̃^{-1}. ✓ Ward consistency: at P = 0 the §75 b_n equals ∂_1γ_n iff ũ = ∂_{x_1}d, which holds because
  G_κ = ∂_qδ_κ·Π_{r≠κ}δ_r. ✓
- **Scope (S10-4):** the explicit b_n, w_n of l.3596-3597 are not numerically tested anywhere. f13 B evaluates Y_n through
  the identity (b) from f12's h_n. UIR-S uses them only through their structural classes (l.3703-3704), so this is a
  disclosure, not a defect.

### 2.3 Theorem UIR-S (§76): CONFIRMED — the scalar (V-IR-S) is PROVEN

**Verdict: the scalar (UIR) sup_n|a_n| < ∞, hence (V-IR-S) sup_n|ρ_n| < ∞, and (S4) with θ = L^{-2}, are PROVEN for the
scalar proxy** (given S-red (i)-(iv), S-2pt, S-tel, which are reviewed).

Step-by-step:
- **Lemma A.**
  - (A1), (A2): elementary. ✓
  - (A3): closed forms of the partial digit products; the case split on |sin A'| is right. ✓
  - (A4): the κ-th term of ũ is ≤ CL^{-1-j}min(L^{-1-j}, 1/|x_1|) for |x_1| ≤ πL^j, and ≤ C/|x_1| per j otherwise (using
    |Π_{r<κ}δ_r| ≤ πL^{j+1}/|x_1|). The j-sum is ≤ C(1 + log(1 + |x_1|))/(1 + |x_1|). The log is genuine for the j with
    πL^j < |x_1|. ✓ (The stated min(L^{-2-2j}, 1/|x_1|) is a slight misstatement of the per-j bound, harmless; S10-3.)
  - (A5): digit products converge to infinite products with tail |x|²L^{-2n}; the j-series tails are ≤ CL^{-2n}. ✓
- **Lemma VC.**
  - (i) Dominators.
    - σ²d²/(λ̃²λ̃') ≲ Π_{μ≥2}(1 + |x_μ|)^{-2}|x|^{-6};
    - (ũ^±)²/λ̃^± ≲ log²(2 + |x_1|)(1 + |x_1|)^{-2}Π_{μ≥2}(1 + |x_μ|)^{-2}|x|^{-2};
    - dm̃/λ̃ ≲ Π(1 + |x_μ|)^{-2}|x|^{-2}.
    Each remains summable over Z⁴ after multiplication by |x|². That is exactly what absorbs the relative error
    O(|x|²/ℓ²) and gives the ℓ^{-2} rate. ✓ Alias tails beyond πℓ are ≤ Cℓ^{-2}; I checked the worst one, ~log²ℓ/ℓ³. ✓
  - (ii) The decisive point. I re-derived the expansion term by term:
    - ω_n's degree-4 part is −2|K+P|²|K−P|² + 4K_1²(|K−P|² + |K+P|²), from −d²ŵλ̃_+λ̃_- and the two intermediate terms;
    - β_n = −2K_1 + O(r³);
    - N_n = ω/h − β²λ̃_-/(hh_+) has degree-4 part −2|K+P|²|K−P|² + 4K_1²|K+P|².
    - The n-dependent pieces all enter at degree ≥ 6:
      - λ̃_n's K⁴/ℓ² term (degree 6 after the degree-4 prefactors);
      - d_0 = 1 − (1 − ℓ^{-2})K²/24 + … and h_n − 1 (degree 2, times a degree-4 numerator);
      - ŵ − 2 = O(K_1²/ℓ²);
      - the n-dependent LINEAR coefficient of ũ, −(2/3)K_1Σ_{j<n}L^{-2-2j}. In β it multiplies an extra λ̃, so it is degree 3
        in β and degree 6 in N;
      - m̃ (degree 6), c_2 (degree 10), and the m ≠ 0 aliases (β: degree 5, so degree 6 in β²).
    - Degree 5 vanishes by joint parity. ✓ Parity: d, ŵ, m̃, λ̃ even and σ, ũ, ũ^± odd under (x, P) ↦ (−x, −P). ✓ The P = 0
      check against ½∂_1(K_1/|K|²). ✓
  - (iii) |λ̃_n − λ̃_m| ≤ Cε|K|⁴ and |1/λ̃_n − 1/λ̃_m| ≤ Cε. ✓
  - (iv) ✓
- **Estimate.**
  - (B1) The two-term split and the telescoping of the reciprocal product give Cεr⁶/(ρ_0²ρ_+²ρ_-²). ✓
  - (B2) is degree −2. ✓
  - Inner ball: CεP⁴I_* with I_* < ∞ (three separated |q|^{-2} singularities in 4D). ✓
  - Outer region: the zeroth Taylor term is fixed by the Ward identity, which forces ∫_{T⁴}F_n(·, 0) = 0. The constant-field
    gauge covariance (level site at ℓX, g_lev(X) = e^{-iε̃cosϑX_1}) gives b_n(K; 0) = ∂_1γ_n and w_n(K; 0) = ∂_1²γ_n (the ϑ-free
    half of ½cos²ϑ ε̃²∂_1²γ). ✓ The first-order term is odd. ✓ The remainder is ≤ CεP². ✓
  - So |x_n − x_m| ≤ Cε_{nm}, uniformly for 0 < |P| ≤ P_0. ✓ (5) is the limit P → 0 via IR-id. ✓
- **Soft points (not gaps at this document's rigour; S10-3):**
  - (a) |h_n(K + P)| ≥ ½ needs K + P ∈ 𝔻: shrink the polydisc to radius r_0/2 for K and P.
  - (b) (A5)'s "uniformly on the same complex region" for the κ-series is asserted; it follows from the closed forms
    because L^{-1-j}Im x stays bounded.
  - (c) "F_n(K, P) → F_n(K, 0) pointwise" is used as the continuity of the alias sums at P = 0 for K ≠ 0. That is true
    because the intermediate poles 1/λ̃(K ± P) are continuous there.
- f13 B (and my re-run, §7): Δ_n = 1.4582e-4, 1.3794e-5, 1.5161e-6, 1.6829e-7, ratios → 0.1110. The maximum sits at the
  smallest P and approaches its P → 0 limit like P² (|ΔY|(0.05) − |ΔY|(0.1) ≈ 1e-4 relative). This is consistent with
  |a_n − a_m| ≤ Cε_{nm}.
- ρ_∞ = a_0 − a_* ≈ −1.76805e-3 (f12 + REVIEW_FLOW_S9 §4.3), so a_* ≈ 4.28102e-3, consistent with Y_5(0.05) = 4.281041e-3
  minus the ~4.8e-8 O(P²) remainder.

## 3. Priority 3: V-bord, V-Jac, V-tel — CONFIRMED

- **V-bord (a).**
  - Ã = K_F + B^*JB with B = (M; ι^*D^*) and J = diag(𝒞^{-1}, −1).
  - J^{-1} + BK_F^{-1}B^* = [[X, b], [b^*, −δ]]. The Schur complement gives det X·det(−δ − b^*X^{-1}b), and (−1)^{N_ℓ} cancels
    against det J. ✓
  - Ghost: Jacobi's complementary minor. ✓
  - Adding logarithms gives the stated total. ✓
- **V-bord (b).** K_FD = HD + DD^*D = E + DΔ ⟹ K_F^{-1}D = DΔ^{-1} − K_F^{-1}EΔ^{-1}. Then δ = ι^*D^*K_F^{-1}EΔ^{-1}ι (using D^*D = Δ and
  ι^*ι = 1). ✓
  - Covariance: 𝔪_n(U^{e^{tλ}}) = 𝔪_n(U)^{e^{tλ}|_{level}} differentiated in the right-exponential chart gives
    M_UD_U = D_ℓ^{𝔪(U)}ι^* for every U. This needs only that 𝔪 is a covariant map whose level link X → X + μ transforms at
    the level sites ℓX, ℓ(X + μ). ✓
  - At critical U the two log det g cancel. ✓ The ⊥ form: det(V^*X^{-1}V) = det_⊥X/det X (Jacobi). ✓
- **V-Jac.** det(A|_{Λ_k∖Λ_{k+1}}) = det A·det(A^{-1}|_{Λ_{k+1}}) with A = Δ^{(k)} and (Δ^{(k)})^{-1}|_{Λ_{k+1}} = (Δ^{(k+1)})^{-1}. It
  telescopes to det Δ/det Δ^{(n)} = det(Δ|_{Λ∖Λ_n}). ✓
  - The 4D remark is correct: g_k = ℓ_k^{-2}/λ̃ + g_reg, with g_reg → G_{Z⁴}(0) ≈ 0.155.
  - Note: Δ^{(k)} is a Schur complement onto a sparse set. It is exponentially local only on the scale ℓ_k√G(0) level
    sites, so "n-independent" here is exact but not "uniformly local". The remark says this in substance. ✓
- **V-tel.** A^{(k+1)}_j = T_kA^{(k)}_j ⟹ X^{(k+1)} = T_kX^{(k)}T_k^T + κ^{-1}Π_{k+1}^{-1}. ✓
  - Sylvester. ✓ ½log det K_F + ½log det X_n = ½ΣΦ^V_k. ✓ 𝒢_n = g^{-1}(δ + b^*X^{-1}b)g^{-1}. ✓
  - The steps depend only on K_F, T_{≤k}, Π_{≤k+1}. ✓
  - Gaps per k, not k-uniform: correctly stated (l.3757-3759). ✓
- **Scope (S10-5):**
  - f13 C1, C2, C6 are pure linear-algebra identities. They hold for ANY symmetric H, M, D of compatible shapes, so they
    test the implementation, not lattice-gauge content.
  - The substantive Part C tests are C3 (covariance, for the straight-path map only, with 𝒞 = 1), C4 (the FD Hessian is
    gauge-degenerate at a flat background) and the reported E-formula match.
  - §81 Reading (3) ("exact on a real lattice gauge configuration, off-shell included") overreads C1.
  - M_UD_U = D_ℓι^* for the actual S4'/W_♮ map is proven by covariance (§77 (b)) but not checked numerically.

## 4. Priority 4: §79 (a) and §79 (b)

### 4.1 The exact formula: CORRECT

∂_s∂_tS(Ue^{sY}e^{tV}) = H(Y, V) + ½∇S·[Y, V] (H = the symmetric chart Hessian, which is the one f13 uses: `0.5*(Hm + Hm.T)`). With
∂_YV_λ = −[Y, Ad(U^{-1})λ(x)], this gives HV_λ = ½[Ad(U_b^{-1})λ(x) + λ(x + μ), J_b]. ✓ f13: 2.4e-15 (flat), 3.3e-15, 2.7e-15 (plane
waves). The raw FD asymmetry 1.9e-3 = 2·max|∇S| at p = 2π/6 is the expected ½∇S·[Y, V] term, a good internal
consistency check.

### 4.2 The expansion order: FALSE as written (S10-1)

- l.3517 and l.3772 assert J = εJ_1 + O(ε³), which is correct (the Cartan plaquette angles are exactly linear in ε and J is
  odd). They then conclude **E_U = εp̂²Ê + O(ε³)**, which does not follow. The coefficient Ad(U_b^{-1}) = exp(−εa_b ad H_1) on
  the 1-links has an O(ε) term, so
  - E_U = εp̂²Ê_1 + ε²p̂²Ê_2 + O(ε³);
  - (Ê_1λ)_b = ½[λ(x) + λ(x + e_1), c_NH_1cos(px_2 + ϑ)];
  - (Ê_2λ)_b = −½cos²(px_2 + ϑ)[[H_1, λ(x)], c_NH_1], on 1-links.
- In the root sector, Ê_2 ∝ c_Nq_α²cos²(px_2 + ϑ)λ(x): a multiplication operator with a nonzero zero-momentum part
  (½cos²→¼).
- Reviewer check (`echeck.py`, f13's own E_formula). Let r(ε) := ||E(2ε)/2ε − E(ε)/ε||/||E(ε)/ε||. Then r(1e-3) = 1.225e-3 and
  r(2e-3) = 2.449e-3, ratio **2.000** (an O(ε³) remainder would give 4). The ratio ||E_2||/||E_1|| = **1.2247** (≈ √(3/2)) is
  the same at p = 2π/6 and 4π/6, at U = 1 and at the twisted flat background, and the normalised overlap ⟨E_1, E_2⟩ is ≤ 1.5e-3.
  So E_U = εE_1 + ε²E_2 + …, with E_2 of the same size as E_1 per power of ε.
- f13 C5 cannot see this. Ê_2 is also ∝ p̂², and its Frobenius overlap with Ê_1 vanishes (a 90° root-plane rotation against
  the identity), so ||E|| changes only at relative O(ε²) ≈ 1e-6.
- Normalisation slip in the same sentence: ½[λ_x + λ_{x+μ}, J] = [avg λ, J], so Ê_1 is −i c_Nq_α cos(px_2 + ϑ) × (link-end
  AVERAGE), not "(i/2) × average". Either "(i/2) × sum" with a sign, or "−i × average". Not load-bearing (c_N is free).

### 4.3 §79 (b): the formula is right; the term list is INCOMPLETE (S10-1)

- 𝒢_n = (D_ℓ − η̃)^*X^{-1}(D_ℓ − η̃) + δ̃: re-derived from bg^{-1} = D_ℓ − MK_F^{-1}E𝔥 and g^{-1}δg^{-1} = 𝔥^*ΔD^*K_F^{-1}E𝔥. ✓ 𝔥 is
  the harmonic extension. ✓
- The ε² coefficient of ½log det 𝒢_n has THREE defect pieces, not two:
  1. p̂²𝔮_{0,n}(p): Ê_2 once against U = 1 objects (new; missing from the text);
  2. p̂²𝔮_{1,n}(p): Ê_1 once against one first-order vertex;
  3. p̂⁴𝔮_{2,n}(p): Ê_1 twice.
  So 𝔡_{n,α} = lim_{p→0}[4𝔮_{0,n} + 4𝔮_{1,n} + 16sin²(p/2)𝔮_{2,n}].
- 𝔮_{0,n} is the U = 1 linear response ½tr(𝒢_0^{-1}d𝒢[Ê_2^{(0)}]), with d𝒢[E] = 𝔥^*D^*E𝔥 − 2Re D_ℓ^*X^{-1}MK_F^{-1}E𝔥 at U = 1
  (where D^*K_F^{-1} = Δ^{-1}D^*). I see no symmetry that kills it.
- The "correction to the pre-statement, logged" (l.3783-3784) should also record this.

## 5. Priority 5: the (DEF) verdict and a route

### 5.1 What (DEF) is

- §79 (c)'s two-scale picture is correct as a description:
  - c_0(K) = 1/(1 + ℓ²λ̃_n g_reg) with g_reg → G_{Z⁴}(0);
  - at |K| ≲ ℓ^{-1} nothing is suppressed;
  - the p → 0 limit at fixed n probes exactly that region.
- Size counts decide nothing, as §79 (c) says honestly.
- But (DEF) as posed asks for a two-scale asymptotic of explicit defect bubbles that need not be computed at all.

### 5.2 Is there a structural reason for the defect contribution to vanish? Partly — and it changes the wall

**(i) What does NOT work: a Ward / Nielsen identity at U = 1 alone.**
- Δ_def(U) := total_n(U) − T^c(U), with T^c(U) := −log det Δ_U + ½Σ_{k<n}Φ^V_k(U) + ½log det(D_ℓ^{𝔪(U)*}X_n(U)^{-1}D_ℓ^{𝔪(U)}). It is
  gauge invariant (every constituent is a covariant construction) and vanishes on the critical set.
- Hence Δ_def = ⟨J_U, Ψ(U)⟩ + O(J²): the one-loop Nielsen structure.
- Its U = 1 Hessian is ⟨d^*da, B a⟩ + ⟨d^*da, Q d^*da⟩. Gauge invariance gives only d^*dBd = 0, i.e. P_T(q)B(q)q = 0.
- That constrains the components of B̂(q) along q, and nothing about B̂_{11}(pe_2) as p → 0. A cubic-symmetric B̂(0) = b_0·1 is
  allowed, and it contributes 4b_0 to 2c.
- So no identity at U = 1 forces 𝔡 = 0. This matches the textbook fact that the finite part of the off-shell one-loop
  2-point function is gauge-fixing dependent, while its log coefficient is not.

**(ii) What DOES work: the critical family.**
- U_f (constant Cartan flux, quantised on the torus) is critical, so E_{U_f} ≡ 0 and **Δ_def(U_f) ≡ 0 for every f**.
- The quantity in (V-IR) is c^tot_n := [f²]total_n(U_f) (MS (iv), F-id-exp, given (L-loc2)). The plane wave is only a device
  for computing it from the U = 1 Hessian.
- Therefore, exactly at each n,
  c^tot_n = ½Σ_{k<n}[f²]Φ^V_k(U_f) + γ_n,  γ_n := [f²]Γ_n^crit(U_f),  Γ_n^crit := −log det Δ_U + ½log det(D_ℓ^{𝔪(U)*}X_n^{-1}D_ℓ^{𝔪(U)}).
- Every piece is well defined:
  - total_n is C² in f (gapped);
  - each Φ^V_k is C² for |f| ≤ ε_k (IMS, as in S-tel (b));
  - so γ_n = [f²](total_n − ½ΣΦ^V_k)(U_f) is a finite Taylor coefficient. The f² log|f| terms of the two massless pieces of
    Γ^crit (fine ghost, level ghost) necessarily cancel.
- No E, no K_F^{-1} (cancelled by V-tel) and no Nielsen-Olesen mode appear. Δ_{U_f} and D_ℓ^*X^{-1}D_ℓ are nonnegative scalar-
  type operators with no spin coupling. X_n^{-1} enters only through the Woodbury form κΠ − κ²ΠT(H^V)^{-1}T^TΠ of gapped steps.
  - Caution: X_U ≥ 𝒞 FAILS at U_f because K_F(U_f) has the NO negative mode. So the K_F^{-1} form of X must not be used
    there; the V-tel form must.
- Equivalently, 𝔡_{n,α} = c^pw[Δ_def] is the failure of the plane-wave/constant-field exchange (the F-id link) for Δ_def,
  and c^cf[Δ_def] = 0. **If the plaquette-reduced U = 1 Hessian kernel of Δ_def has a Fourier transform continuous at
  q = 0 in the (12, 12) channel (e.g. it is summable), then 𝔡_{n,α} = 0 EXACTLY for every n** (F-id applied to Δ_def).
  - Heuristic power counting (ARGUED, not a proof): each defect term carries J = d^*F, i.e. one derivative more than a
    critical massless bubble, but the massless K_F(1)^{-1} between E and M can leave a |x|^{-4}-type tail. So
    summability is plausible, not evident.

### 5.3 Sharper statement and route (binding)

Replace (DEF) by either of two equivalent (DEF*) forms:
- **(GP) the constant-field ghost pair (preferred; defect-free).**
  - Statement: sup_n|γ_n − γ_n^{log}| < ∞ (more precisely: γ_n − [the q_α²·log ℓ part fixed by GH-log (c)] is n-uniformly
    bounded), where γ_n := [f²](−log det Δ_{U_f} + ½log det(D_ℓ^*X_n^{-1}D_ℓ)(U_f)).
  - This is a critical-background statement of exactly the GH-log (c) type (it pairs the fine ghost with the level ghost
    across the capacity scale).
  - Route:
    - (a) prove it like GH-log (c), whose two-scale (capacity) analysis handles −log det Δ' = −log det Δ − log det g
      exactly;
    - (b) check it numerically at constant field by magnetic Bloch, as f11 did for the scalar, for n = 1, 2, 3 (root sector,
      L = 3), against the plane-wave reading of T^c. Their difference IS 𝔡_n.
- **(DEF-F) the exchange lemma.** The plaquette-reduced U = 1 Hessian kernel of Δ_def is continuous at q = 0 in Fourier
  space. Then 𝔡 = 0 exactly and no two-scale asymptotics of defect bubbles is needed.
- What NOT to do: compute 𝔮_1, 𝔮_2 (and the missing 𝔮_0) bubble by bubble through 𝔥 at the capacity scale. That is the hard
  way to compute a quantity whose constant-field value is identically zero.
- Status: (DEF) remains OPEN in every form. (GP) is the correct wall. Its only two-scale content is the fine-ghost/level-
  ghost pairing, which GH-log (c) already solves in the closely analogous Δ' case.

## 6. Priority 6: how close are (VFINE) and (VC-V)?

- **(VFINE): close; the same proof with more vertices.**
  - Ghost −log det Δ_U (root sector, charge q_α): §74 verbatim. The adjoint covariant Laplacian at a Cartan plane wave has the
    same scalar vertices with ε → q_αε. So the ghost is a corollary of FINE-IR (coefficient 2c_gq_α², finite part q_α²a_0).
  - Feynman ½log det K_F:
    - the same Ward rewrite (gauge covariance at constant field);
    - plus the spin (field-strength) vertex 2[F_{μν}, ·] of H, which is not a total derivative. It contributes the
      paramagnetic part of the log coefficient. That coefficient must come out as the standard background-Feynman value
      relative to the ghost, which is a check.
    - The symmetrisation k ↦ −k − pe_2 still applies, because the spin vertex lives on 12-plaquettes and is symmetric under it.
  - Estimate: one session. Needed input: the explicit second-order plane-wave vertices of H(U) at U = 1, which are not
    written anywhere yet.
- **(VC-V): moderate. Same skeleton as Lemma A/VC + UIR-S, with three genuinely new points.**
  - (1) Tensor block form factors (A_0)_{μν}(k) of the S4'/W_♮ map. The scalar d(0) = 1 becomes A_0(0) = 1 on constant 1-forms.
    The degree-4 numerator's n-independence needs the leading small-K form of A_0 (and of T_k, Π_k) to be n-independent. This
    is the "charge normalisation" again, plausible but unchecked.
  - (2) The ⊥ compression det_⊥X involves the non-analytic transverse projector at K = 0. Avoid it: keep
    ½log det X + ½log det(D_ℓ^*X^{-1}D_ℓ), whose data are analytic after λ̃-normalisation. The second term is then part of (GP),
    not of (VC-V).
  - (3) The vector analogue of IR-id: x^V_n(P) linked to the fine Feynman polarisation through det A = det K_F·det 𝒞^{-1}·det X
    (exact for every U, no E). So the X-part needs (VFINE) for K_F only, and does not need (DEF).
  - Also: 𝔪_n of a fine Cartan plane wave is a level Cartan plane wave with a convergent form factor up to O(ε³) (abelian
    averages; projection corrections are O(ε³)). To be checked for W_♮.
- With the §5 route, (VC-V) applies to the steps Φ^V_k and X_n, (GP) to the ghost pair, and (DEF) disappears.

## 7. Priority 7: f13 re-run under the numeric lock

- Re-run under one lock acquisition (see the header): **23/23 PASS, identical to checks/f13_out.txt** apart from timing.
  54.5 s, 660 MB (official: 56.4 s, 560 MB).
- Criteria compliance:
  - A1-A3, B1-B3 and C1-C6 are as pre-stated.
  - The Part C Hessian adds a Richardson step to the "central finite differences" of the criteria. That is stronger;
    say so.
  - B3 compares P = 0.05 with P = 0.4 only. The theorem's P → 0 uniformity is supported by the monotone approach of
    |ΔY|(P) to its limit (1.4582e-4 at 0.05 vs 1.4571e-4 at 0.1).
- Implementation (Part C read line by line):
  - grad_S, D_matrix, M_and_level (straight-path decimation and its covariant derivative), E_formula and the
    determinant bookkeeping match §73 (T4) with 𝒞 = 1.
  - The root block is legitimate: at a Cartan background the Cartan action decouples root from Cartan.
- **Reviewer extension:** E_U has an O(ε²) term (§4.2). This finding is not under the f13 criteria.

## 8. Per-item verdicts

| Item | Verdict | Fix |
|---|---|---|
| Provenance | **CLEAN** | — |
| [RFL9-fix] S9-1..S9-7, 16 tags | **APPLIED**, correct | — |
| [S10-corr] in S-fix | **CORRECT; S-fix still PROVEN** (C⁰ is even unweighted) | — |
| (T1) Lemma FINE-IR | **CONFIRMED** | — |
| (T2) Proposition IR-id | **CONFIRMED** | S10-4 (b_n, w_n untested numerically; disclose) |
| Lemma A, Lemma VC | **CONFIRMED** (sketch-level dominated convergence, dominators checked) | S10-3 (per-j bound wording; polydisc radius) |
| (T3) Theorem UIR-S | **CONFIRMED: scalar (UIR), (V-IR-S), (S4) θ = L^{-2} PROVEN** | — |
| (T4) Lemma V-bord | **CONFIRMED**, every U | S10-5 (C1 is pure algebra) |
| (T5) Lemma V-Jac | **CONFIRMED** | — |
| (T6) Proposition V-tel | **CONFIRMED** (no k-uniform gap, correctly) | — |
| (T7) (a) exact formula | **CONFIRMED** | — |
| (T7) (a) expansion "O(ε³)" (l.3517, 3772) | **FALSE**: an ε²p̂²Ê_2 term exists | S10-1 |
| (T7) (b) corrected (§79 (b)) | **INCOMPLETE** (missing 𝔮_0) | S10-1 |
| (T7) (c) / (DEF) | **OPEN; wall mis-aimed.** Replace by (GP) or (DEF-F) | S10-2 |
| (T8) / §80 | reduction **CORRECT** as a list; to be restated with (GP) | S10-2, S10-6 |
| f13 | **CONFIRMED**; re-run 23/23 identical; E_U has an O(ε²) term (reviewer) | S10-5 |

## 9. Corrected tally

**59 PROVEN-HERE (claimed 59)** = 50 + FINE-IR + IR-id + Lemma A + Lemma VC + UIR-S + V-bord + V-Jac + V-tel + §79 (a).
- Scope annotations:
  - Lemma A and Lemma VC were not pre-stated. They are counted as in the session-8 convention; a stricter count that
    folds them into UIR-S gives 57.
  - §79 (a) is counted for the exact formula only; its expansion clause is wrong (S10-1).
  - IR-id's b_n, w_n are structural (S10-4).
  - V-Jac gives no uniform bounds (its own remark).
  - V-2pt remains conditional on (L-loc2).
- **IMPORTED-AND-REVERIFIED:** L4b; the Lévy-process functional CLT. No new import. ✓
- **ARGUED, not counted:** (L-loc2); the §79 (c) size count; the reviewer heuristic of §5.2 (ii).
- **OPEN:**
  - (V-IR) on G_⊥;
  - (VFINE), (VC-V);
  - (DEF), to be restated as (GP) or (DEF-F);
  - (L-loc2);
  - a k-uniform vector step gap (only needed if the vector proof goes through the steps rather than closed forms, as
    UIR-S did);
  - the rest of §83's list.

## 10. Binding fixes for the next lane-C session

1. **S10-1 (§73 (T7) (a) l.3517; §79 (a) l.3772-3773; §79 (b) l.3779-3784).**
   - Replace "E_U = εE_1 + O(ε³)" / "E_U = εp̂²Ê + O(ε³)" with E_U = εp̂²Ê_1 + ε²p̂²Ê_2 + O(ε³), where
     Ê_2λ = −½cos²(px_2 + ϑ)[[H_1, λ(x)], c_NH_1] on the 1-links (from Ad(U_b^{-1}) = 1 − εa_b ad H_1 + …).
   - Add the term p̂²𝔮_{0,n} (Ê_2 once against U = 1 objects) to §79 (b), so 𝔡 = lim[4𝔮_0 + 4𝔮_1 + 16sin²(p/2)𝔮_2]. Log it as a
     further correction of the pre-statement.
   - Fix "(i/2) … link-end average" to "−i … link-end average" (or "(i/2)·sum", with the sign of the chosen convention).
2. **S10-2 (§79 (c), §80, §82, §83).** Record that E ≡ 0 on the critical family U_f that defines c^tot_n, so the defect is
   a plane-wave artifact. Restate the wall as (GP): γ_n := [f²](total_n − ½Σ_{k<n}Φ^V_k)(U_f) = [f²](−log det Δ + ½log det
   D_ℓ^*X_n^{-1}D_ℓ)(U_f), n-uniform up to its GH-log (c) log part. Keep (DEF-F) as the equivalent exchange form. State
   that X_U ≥ 𝒞 fails at U_f (NO mode), so X_n^{-1} must be taken in V-tel's Woodbury form there.
3. **S10-3 (§76 Lemma A (A4), Lemma VC (i)).** The per-j bound is CL^{-1-j}min(L^{-1-j}, 1/|x_1|) for |x_1| ≤ πL^j and C/|x_1|
   otherwise (the log comes from the second case). Take K, P in the half-radius polydisc so that K ± P ∈ 𝔻.
4. **S10-4 (§75, §76 Reading (4), §81).** Disclose that the explicit b_n, w_n (l.3596-3597) are not numerically tested.
   f13 B tests x_n through the identity (b) from f12's h_n, i.e. the conclusion of UIR-S, not (VC)'s vertex data.
   "The direct test of (VC)" (l.3836) → "a direct test of UIR-S's conclusion".
5. **S10-5 (§77 Reading (3), §81 Part C, Reading (3)).** Say that C1, C2, C6 are linear-algebra identities, valid for any
   matrices. The lattice-gauge content of Part C is C3 (straight-path map, 𝒞 = 1), C4 and the E-formula match. Strike
   "off-shell included" as evidence.
6. **S10-6 (§80).** In (VC-V), move ½log det(D_ℓ^*X^{-1}D_ℓ) into (GP), and keep the X-part with the vector IR-id through
   det A = det K_F det 𝒞^{-1} det X (no E). Note that (VFINE) for the ghost is a corollary of FINE-IR (ε → q_αε).

## 11. Remaining list for Theorem UNIV for SU(N)

Theorem UNIV for SU(N) does NOT rest only on (L-loc2). That is correct as stated (l.3814). After this review it rests on:
1. **(L-loc2)**, which is the V-2pt hypothesis.
2. **(VFINE-K)**: the fine IR expansion of the Feynman ½log det K_F root polarisation, including the spin vertex.
   (VFINE-ghost) is a corollary of FINE-IR.
3. **(VC-V)**: level-unit convergence of the X_n vertex data, i.e. the tensor A_0, T_k, Π_k form factors with an
   n-independent degree-4 numerator. Plus the vector IR-id through det A = det K_F det 𝒞^{-1} det X, and the plane-wave form
   factor of 𝔪_n for W_♮.
4. **(GP)** (replacing (DEF)): the constant-field fine-ghost/level-ghost pair γ_n, n-uniform up to its log. Alternatively
   (DEF-F).
5. Cross-lane and rate-only items unchanged:
   - (s1), (s2⊥) rate; the rate of c'(φ) → c'_0;
   - (COV-GI) at non-critical backgrounds. The (GP) route uses critical backgrounds only, so it does not need this;
   - FI-1; HIST's restatement of CL^J's Setting.
6. Not needed if the vector proof follows UIR-S's closed-form method: a k-uniform vector step gap.

Suggested check f14 (pre-state): (GP) at n = 1, 2, 3 by magnetic Bloch at constant Cartan flux. Report the plane-wave
reading of T^c alongside it, so that their difference measures 𝔡_n directly (including 𝔮_0). Jobs < 20 min, < 1 GB, under
the lock.
